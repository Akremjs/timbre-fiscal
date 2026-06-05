# -*- coding: utf-8 -*-
from odoo import api, fields, models

TIMBRE_PRODUCT_CODE = 'TIMBRE_FISCAL'
TIMBRE_LINE_LABEL = 'Timbre Fiscal'
PARAM_PREFIX = 'timbre_fiscal_tn'


class AccountMove(models.Model):
    _inherit = 'account.move'

    apply_timbre_fiscal = fields.Boolean(
        string='Appliquer le timbre fiscal',
        default=True,
        copy=True,
    )

    def _timbre_param(self, key, default):
        return self.env['ir.config_parameter'].sudo().get_param(
            f'{PARAM_PREFIX}.{key}', default,
        )

    def _timbre_enabled(self):
        return self._timbre_param('on_customer_invoice', 'True') == 'True'

    def _timbre_amount(self):
        return float(self._timbre_param('amount', '1.0'))

    def _timbre_product(self):
        Product = self.env['product.product']
        for code in (TIMBRE_PRODUCT_CODE, 'AKREM_TF', 'TF'):
            product = Product.search([('default_code', '=', code)], limit=1)
            if product:
                return product
        return Product.browse()

    def _has_timbre_line(self):
        self.ensure_one()
        product = self._timbre_product()
        if not product:
            return False
        return bool(self.invoice_line_ids.filtered(
            lambda line: line.product_id.id == product.id and line.display_type == 'product',
        ))

    def _sync_timbre_line(self):
        for move in self:
            if move.state != 'draft' or move.move_type != 'out_invoice':
                continue
            if not move._timbre_enabled() or not move.apply_timbre_fiscal:
                move._remove_timbre_line()
                continue
            if move._has_timbre_line():
                move._update_timbre_line()
            else:
                move._add_timbre_line()

    def _add_timbre_line(self):
        self.ensure_one()
        product = self._timbre_product()
        if not product:
            return
        self.write({
            'invoice_line_ids': [(0, 0, {
                'product_id': product.id,
                'name': TIMBRE_LINE_LABEL,
                'quantity': 1.0,
                'price_unit': self._timbre_amount(),
                'tax_ids': [(6, 0, [])],
            })],
        })

    def _update_timbre_line(self):
        self.ensure_one()
        product = self._timbre_product()
        if not product:
            return
        amount = self._timbre_amount()
        for line in self.invoice_line_ids.filtered(
            lambda l: l.product_id.id == product.id and l.display_type == 'product',
        ):
            line.write({'price_unit': amount, 'tax_ids': [(6, 0, [])]})

    def _remove_timbre_line(self):
        self.ensure_one()
        product = self._timbre_product()
        if not product:
            return
        lines = self.invoice_line_ids.filtered(
            lambda l: l.product_id.id == product.id and l.display_type == 'product',
        )
        if lines:
            lines.unlink()

    @api.model_create_multi
    def create(self, vals_list):
        moves = super().create(vals_list)
        moves._sync_timbre_line()
        return moves

    def write(self, vals):
        res = super().write(vals)
        if self.env.context.get('skip_timbre_fiscal_sync'):
            return res
        triggers = {'move_type', 'state', 'invoice_line_ids', 'apply_timbre_fiscal', 'partner_id'}
        if triggers.intersection(vals.keys()):
            self._sync_timbre_line()
        return res

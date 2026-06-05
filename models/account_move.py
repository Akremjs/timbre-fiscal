# -*- coding: utf-8 -*-
from odoo import api, fields, models

TIMBRE_PRODUCT_CODE = 'AKREM_TF'
TIMBRE_LINE_LABEL = 'Timbre Fiscal'


class AccountMove(models.Model):
    _inherit = 'account.move'

    akrem_apply_timbre = fields.Boolean(
        string='Appliquer le timbre fiscal',
        default=True,
        copy=True,
    )

    def _akrem_timbre_enabled(self):
        icp = self.env['ir.config_parameter'].sudo()
        return icp.get_param('akrem_timbre_fiscal.on_customer_invoice', 'True') == 'True'

    def _akrem_timbre_amount(self):
        icp = self.env['ir.config_parameter'].sudo()
        return float(icp.get_param('akrem_timbre_fiscal.amount', '1.0'))

    def _akrem_timbre_product(self):
        product = self.env['product.product'].search(
            [('default_code', '=', TIMBRE_PRODUCT_CODE)],
            limit=1,
        )
        if not product:
            product = self.env['product.product'].search(
                [('default_code', '=', 'TF')],
                limit=1,
            )
        return product

    def _akrem_has_timbre_line(self):
        self.ensure_one()
        product = self._akrem_timbre_product()
        if not product:
            return False
        return bool(self.invoice_line_ids.filtered(
            lambda l: l.product_id.id == product.id and l.display_type == 'product'
        ))

    def _akrem_sync_timbre_line(self):
        for move in self:
            if move.state != 'draft':
                continue
            if move.move_type != 'out_invoice':
                continue
            if not move._akrem_timbre_enabled() or not move.akrem_apply_timbre:
                move._akrem_remove_timbre_line()
                continue
            if move._akrem_has_timbre_line():
                move._akrem_update_timbre_line()
            else:
                move._akrem_add_timbre_line()

    def _akrem_add_timbre_line(self):
        self.ensure_one()
        product = self._akrem_timbre_product()
        if not product:
            return
        self.write({
            'invoice_line_ids': [(0, 0, {
                'product_id': product.id,
                'name': TIMBRE_LINE_LABEL,
                'quantity': 1.0,
                'price_unit': self._akrem_timbre_amount(),
                'tax_ids': [(6, 0, [])],
            })],
        })

    def _akrem_update_timbre_line(self):
        self.ensure_one()
        product = self._akrem_timbre_product()
        if not product:
            return
        amount = self._akrem_timbre_amount()
        for line in self.invoice_line_ids.filtered(
            lambda l: l.product_id.id == product.id and l.display_type == 'product'
        ):
            line.write({
                'price_unit': amount,
                'tax_ids': [(6, 0, [])],
            })

    def _akrem_remove_timbre_line(self):
        self.ensure_one()
        product = self._akrem_timbre_product()
        if not product:
            return
        lines = self.invoice_line_ids.filtered(
            lambda l: l.product_id.id == product.id and l.display_type == 'product'
        )
        if lines:
            lines.unlink()

    @api.model_create_multi
    def create(self, vals_list):
        moves = super().create(vals_list)
        moves._akrem_sync_timbre_line()
        return moves

    def write(self, vals):
        res = super().write(vals)
        if self.env.context.get('akrem_skip_timbre_sync'):
            return res
        trigger_fields = {
            'move_type', 'state', 'invoice_line_ids',
            'akrem_apply_timbre', 'partner_id',
        }
        if trigger_fields.intersection(vals.keys()):
            self._akrem_sync_timbre_line()
        return res

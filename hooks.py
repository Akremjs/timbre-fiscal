# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

OLD_TO_NEW_PARAMS = {
    'timbre_fiscal.amount': 'akrem_timbre_fiscal.amount',
    'timbre_fiscal.on_customer_invoice': 'akrem_timbre_fiscal.on_customer_invoice',
    'timbre_fiscal.on_vendor_bill': 'akrem_timbre_fiscal.on_vendor_bill',
}


def post_init_hook(env):
    icp = env['ir.config_parameter'].sudo()
    for old_key, new_key in OLD_TO_NEW_PARAMS.items():
        if not icp.get_param(new_key):
            old_val = icp.get_param(old_key)
            if old_val is not None:
                icp.set_param(new_key, old_val)

    Product = env['product.product'].sudo()
    old_product = Product.search([('default_code', '=', 'TF')], limit=1)
    new_product = Product.search([('default_code', '=', 'AKREM_TF')], limit=1)
    if old_product and new_product and old_product.id != new_product.id:
        env.cr.execute(
            """
            UPDATE account_move_line aml
               SET product_id = %s
              FROM product_product pp
              JOIN product_template pt ON pt.id = pp.product_tmpl_id
             WHERE aml.product_id = pp.id
               AND pt.default_code = 'TF'
            """,
            (new_product.id,),
        )
        old_product.write({'default_code': 'TF_LEGACY'})
        _logger.info('Migration produit timbre TF → AKREM_TF effectuée')

    old_module = env['ir.module.module'].sudo().search(
        [('name', '=', 'timbre_fiscal_v17'), ('state', '=', 'installed')],
        limit=1,
    )
    if old_module:
        old_module.write({'author': 'AKREM KHELIFI'})
        try:
            old_module.button_uninstall()
        except Exception as err:
            _logger.warning('Désinstallation timbre_fiscal_v17 ignorée : %s', err)

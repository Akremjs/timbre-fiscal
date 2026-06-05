# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

LEGACY_PARAM_KEYS = {
    'timbre_fiscal.amount': 'timbre_fiscal_tn.amount',
    'timbre_fiscal.on_customer_invoice': 'timbre_fiscal_tn.on_customer_invoice',
    'timbre_fiscal.on_vendor_bill': 'timbre_fiscal_tn.on_vendor_bill',
    'akrem_timbre_fiscal.amount': 'timbre_fiscal_tn.amount',
    'akrem_timbre_fiscal.on_customer_invoice': 'timbre_fiscal_tn.on_customer_invoice',
    'akrem_timbre_fiscal.on_vendor_bill': 'timbre_fiscal_tn.on_vendor_bill',
}

LEGACY_MODULE_NAMES = (
    'timbre_fiscal_v17',
    'akrem_timbre_fiscal_v17',
)


def _apply_timbre_fiscal_column_exists(env):
    env.cr.execute(
        """
        SELECT 1
          FROM information_schema.columns
         WHERE table_name = 'account_move'
           AND column_name = 'apply_timbre_fiscal'
        """,
    )
    return bool(env.cr.fetchone())


def _ensure_account_move_schema(env):
    """Corrige une installation partielle (produit cree, code Python inactif)."""
    if _apply_timbre_fiscal_column_exists(env):
        return True
    _logger.warning(
        'timbre_fiscal_tn: schema incomplet detecte, initialisation de account.move',
    )
    try:
        env['account.move']._auto_init()
    except Exception as err:
        _logger.error('timbre_fiscal_tn: echec _auto_init account.move : %s', err)
        return False
    if _apply_timbre_fiscal_column_exists(env):
        _logger.info('timbre_fiscal_tn: schema account.move corrige avec succes')
        return True
    _logger.error(
        'timbre_fiscal_tn: schema toujours incomplet. '
        'Executez : odoo -u timbre_fiscal_tn -d VOTRE_BASE',
    )
    return False


def post_init_hook(env):
    icp = env['ir.config_parameter'].sudo()
    for old_key, new_key in LEGACY_PARAM_KEYS.items():
        if not icp.get_param(new_key):
            old_val = icp.get_param(old_key)
            if old_val is not None:
                icp.set_param(new_key, old_val)

    Product = env['product.product'].sudo()
    target = Product.search([('default_code', '=', 'TIMBRE_FISCAL')], limit=1)
    for legacy_code in ('AKREM_TF', 'TF'):
        legacy = Product.search([('default_code', '=', legacy_code)], limit=1)
        if not legacy:
            continue
        if target and legacy.id != target.id:
            env.cr.execute(
                """
                UPDATE account_move_line aml
                   SET product_id = %s
                 WHERE aml.product_id = %s
                """,
                (target.id, legacy.id),
            )
            legacy.write({'default_code': f'{legacy_code}_LEGACY'})
        elif not target:
            legacy.write({'default_code': 'TIMBRE_FISCAL'})
            target = legacy

    Module = env['ir.module.module'].sudo()
    for legacy_name in LEGACY_MODULE_NAMES:
        old = Module.search([('name', '=', legacy_name), ('state', '=', 'installed')], limit=1)
        if not old:
            continue
        try:
            old.button_uninstall()
            _logger.info('Ancien module %s désinstallé', legacy_name)
        except Exception as err:
            _logger.warning('Désinstallation %s ignorée : %s', legacy_name, err)

    _ensure_account_move_schema(env)

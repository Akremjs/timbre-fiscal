# -*- coding: utf-8 -*-
{
    'name': 'Droit de Timbre Fiscal (Tunisie)',
    'version': '17.0.1.0.3',
    'category': 'Accounting/Localizations',
    'summary': 'Gestion du droit de timbre fiscal sur les factures tunisiennes',
    'description': """
        Ajoute automatiquement une ligne « Timbre Fiscal » sur les factures clients
        conformément à la réglementation tunisienne.
    """,
    'author': 'AKREM KHELIFI',
    'icon': '/akrem_timbre_fiscal_v17/static/description/icon_akrem.png',
    'license': 'LGPL-3',
    'depends': ['account', 'product'],
    'data': [
        'data/akrem_timbre_fiscal_data.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': False,
}

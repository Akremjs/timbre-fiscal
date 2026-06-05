# -*- coding: utf-8 -*-
{
    'name': 'Droit de Timbre Fiscal (Tunisie)',
    'version': '17.0.1.0.0',
    'category': 'Accounting/Localizations',
    'summary': 'Ajout automatique du droit de timbre fiscal sur les factures clients tunisiennes',
    'description': """
Droit de Timbre Fiscal — Tunisie
================================

Ce module ajoute automatiquement une ligne « Timbre Fiscal » sur les factures
clients (out_invoice) conformément à la réglementation tunisienne.

Fonctionnalités
---------------
* Ajout automatique du timbre sur les factures clients en brouillon
* Montant configurable (par défaut 1,000 DT)
* Ligne affichée proprement sans code article visible
* TVA exclue sur la ligne timbre
* Compatible avec la localisation tunisienne (l10n_tn)

Configuration
-------------
Paramètres système :
* timbre_fiscal_tn.amount
* timbre_fiscal_tn.on_customer_invoice
* timbre_fiscal_tn.on_vendor_bill
    """,
    'author': 'AKREM KHELIFI',
    'license': 'LGPL-3',
    'depends': ['account', 'product'],
    'data': [
        'data/timbre_fiscal_tn_data.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': False,
    'images': ['static/description/banner.png'],
}

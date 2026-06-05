# -*- coding: utf-8 -*-
{
    'name': 'Droit de Timbre Fiscal (Tunisie)',
    'version': '17.0.1.0.2',
    'category': 'Accounting/Localizations',
    'summary': 'Ajout automatique du droit de timbre fiscal sur les factures clients tunisiennes',
    'description': """
Droit de Timbre Fiscal - Tunisie
================================

Automatisez le droit de timbre fiscal sur vos factures clients Odoo 17.
Conforme a la reglementation tunisienne - installation en un clic.

Fonctionnement
--------------
* Ajout automatique de la ligne Timbre Fiscal sur les factures clients en brouillon
* Montant par defaut 1,000 DT (configurable), quantite 1, sans TVA
* Libelle propre sur le PDF, sans code article visible
* Pas de doublon ; mise a jour si le montant change
* Desactivable facture par facture (champ Appliquer le timbre fiscal)
* Par defaut, pas de timbre sur les factures fournisseur

Configuration (optionnelle)
---------------------------
* timbre_fiscal_tn.amount
* timbre_fiscal_tn.on_customer_invoice
* timbre_fiscal_tn.on_vendor_bill

Support - AKREM KHELIFI
-----------------------
Email : akremkhelifi07@gmail.com
WhatsApp : +216 54 444 373
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

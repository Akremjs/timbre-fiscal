# Textes marketing — Fiche Odoo Apps

Copiez-collez ces champs lors de la soumission sur https://apps.odoo.com

---

## Titre du module

**Droit de Timbre Fiscal (Tunisie)**

---

## Nom technique

`timbre_fiscal_tn`

---

## Résumé court (summary — ~150 caractères)

Ajout automatique du droit de timbre fiscal (1 DT) sur les factures clients tunisiennes. Conforme, sans TVA, configurable — Odoo 17.

---

## Description courte (Apps Store — paragraphe d'accroche)

Automatisez le **droit de timbre fiscal tunisien** sur vos factures clients Odoo 17. Ce module ajoute automatiquement la ligne « Timbre Fiscal » (1,000 DT par défaut, sans TVA) à chaque facture client en brouillon — plus d'oublis, plus de saisie manuelle. Installation en un clic, compatible localisation Tunisie.

---

## Description longue (formulaire / README Apps)

### Contexte

En Tunisie, les factures clients doivent inclure le **droit de timbre fiscal**. Sans automatisation, chaque facture nécessite une ligne saisie manuellement, avec des risques d'oubli, d'erreur de montant ou d'incohérence comptable.

### Ce que fait le module

- Ajoute **automatiquement** une ligne « **Timbre Fiscal** » sur les **factures clients** (`out_invoice`) en brouillon
- Montant par défaut : **1,000 DT** (configurable)
- Ligne **sans TVA**
- Libellé propre sur le PDF/impression — pas de code article visible
- Champ par facture « Appliquer le timbre fiscal » pour activer/désactiver au cas par cas
- Par défaut, **aucun timbre** sur les factures fournisseur

### Fonctionnement détaillé

1. **Installation** : le produit « Timbre Fiscal » et les paramètres système sont créés automatiquement.
2. **Création de facture** : dès qu'une facture client est créée ou modifiée en brouillon, le module vérifie si le timbre doit s'appliquer.
3. **Ajout de la ligne** : une ligne avec quantité 1 et le montant configuré est insérée, taxes vidées.
4. **Mise à jour** : si le montant change dans les paramètres, les factures brouillon sont mises à jour.
5. **Pas de doublon** : le module détecte une ligne timbre existante et ne la recrée pas.

### Configuration (optionnelle)

| Paramètre | Description | Défaut |
|-----------|-------------|--------|
| `timbre_fiscal_tn.amount` | Montant en dinars | 1.0 |
| `timbre_fiscal_tn.on_customer_invoice` | Factures clients | True |
| `timbre_fiscal_tn.on_vendor_bill` | Factures fournisseur | False |

### Compatibilité

- Odoo **17.0**
- Modules : `account`, `product`
- Localisation Tunisie (`l10n_tn`) compatible
- Licence **LGPL-3** — gratuit

---

## Mots-clés / tags suggérés

`tunisie` `timbre fiscal` `droit de timbre` `facturation` `comptabilité` `localisation` `l10n_tn` `invoice` `stamp` `fiscal`

---

## Support & contact

**AKREM KHELIFI**

- Email : [akremkhelifi07@gmail.com](mailto:akremkhelifi07@gmail.com)
- WhatsApp : [+216 54 444 373](https://wa.me/21654444373)

> Si vous cherchez de l'aide pour l'installation, la personnalisation ou l'intégration dans votre ERP tunisien, contactez-moi par email ou WhatsApp.

---

## Captures d'écran à uploader

1. **Facture avec ligne timbre** — `timbre_fiscal_tn/static/description/screenshot_invoice.png`
2. **Bannière module** — `timbre_fiscal_tn/static/description/banner.png`

---

## Champs formulaire Odoo Apps

| Champ | Valeur |
|-------|--------|
| Version Odoo | 17.0 |
| Catégorie | Accounting / Localizations |
| Licence | LGPL-3 |
| Prix | Gratuit (0 €) |
| Repository | https://github.com/Akremjs/timbre-fiscal |
| Branche | main |
| Dossier module | timbre_fiscal_tn/ |
| Auteur | AKREM KHELIFI |
| Site web / support | mailto:akremkhelifi07@gmail.com |

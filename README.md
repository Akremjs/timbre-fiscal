# Droit de Timbre Fiscal (Tunisie) — Odoo 17

Module Odoo **17.0** pour l’ajout automatique du droit de timbre fiscal sur les factures clients tunisiennes.

**Auteur :** AKREM KHELIFI  
**Nom technique :** `akrem_timbre_fiscal_v17`

## Fonctionnalités

- Ajout automatique d’une ligne **Timbre Fiscal** sur les factures clients (`out_invoice`) en brouillon
- Montant configurable (défaut : **1,000 DT**)
- Ligne affichée sans code article `[AKREM_TF]` sur la facture
- TVA exclue sur la ligne timbre
- Produit service interne : `AKREM_TF`

## Installation

```bash
git clone https://github.com/Akremjs/timbre-fiscal.git akrem_timbre_fiscal_v17
```

Copiez le dossier dans votre chemin `addons` Odoo, puis :

1. Redémarrez Odoo
2. **Apps → Mettre à jour la liste des applications**
3. Recherchez **Droit de Timbre Fiscal (Tunisie)**
4. **Installer**

## Dépendances

- `account`
- `product`
- Recommandé : `l10n_tn` (localisation Tunisie)

## Configuration (paramètres système)

| Clé | Défaut | Description |
|-----|--------|-------------|
| `akrem_timbre_fiscal.amount` | `1.000` | Montant du timbre en DT |
| `akrem_timbre_fiscal.on_customer_invoice` | `True` | Activer sur factures clients |
| `akrem_timbre_fiscal.on_vendor_bill` | `False` | Activer sur factures fournisseur |

## Test rapide

1. Créez une facture client en brouillon avec un produit taxé
2. Vérifiez l’apparition de la ligne **Timbre Fiscal** à **1,00 DT** sans TVA
3. Comptabilisez la facture

## Licence

LGPL-3

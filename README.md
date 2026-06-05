# timbre-fiscal — Module Odoo Apps

Module Odoo **17.0** : **Droit de Timbre Fiscal (Tunisie)**

Nom technique : `timbre_fiscal_tn`  
Auteur : **AKREM KHELIFI**

## Structure du dépôt (Odoo Apps)

```
timbre-fiscal/
├── README.md
├── LICENSE
├── ODOO_APPS.md
└── timbre_fiscal_tn/          ← dossier module Odoo
    ├── __manifest__.py
    ├── models/
    ├── data/
    └── static/description/
        ├── icon.png           (256×256)
        ├── banner.png
        └── index.html
```

## Installation manuelle

```bash
git clone https://github.com/Akremjs/timbre-fiscal.git
cp -r timbre-fiscal/timbre_fiscal_tn /chemin/vers/odoo/addons/
# Redémarrer Odoo → Apps → Mettre à jour → Installer
```

## Installation pour le projet PFE (bi.merkago.net)

```bash
cd pfe-bi-odoo/odoo-module
rm -rf akrem_timbre_fiscal_v17   # ancienne copie locale
git clone --depth 1 https://github.com/Akremjs/timbre-fiscal.git _timbre-src
cp -r _timbre-src/timbre_fiscal_tn . && rm -rf _timbre-src
docker exec pfe-odoo odoo -d pfe_bi ... -i timbre_fiscal_tn
```

## Publier sur Odoo Apps

Voir [ODOO_APPS.md](./ODOO_APPS.md)

## Licence

LGPL-3 — voir [LICENSE](./LICENSE)

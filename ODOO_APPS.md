# Publier sur Odoo Apps Store

## Prérequis

1. Compte développeur Odoo : https://www.odoo.com/fr_FR/partners
2. Dépôt GitHub public : https://github.com/Akremjs/timbre-fiscal
3. Module testé sur Odoo **17.0**

## Contenu requis (déjà inclus)

| Élément | Fichier |
|---------|---------|
| Manifest | `timbre_fiscal_tn/__manifest__.py` |
| Icône 256×256 | `timbre_fiscal_tn/static/description/icon.png` |
| Bannière | `timbre_fiscal_tn/static/description/banner.png` |
| Description HTML | `timbre_fiscal_tn/static/description/index.html` |
| Licence | `LICENSE` (LGPL-3) |

## Créer le fichier ZIP pour soumission

```bash
cd timbre-fiscal
zip -r timbre_fiscal_tn.zip timbre_fiscal_tn/ -x "*.git*"
```

Le ZIP doit contenir **un seul dossier** `timbre_fiscal_tn/` à la racine.

## Repository Git (format Odoo Apps)

```
ssh://git@github.com/Akremjs/timbre-fiscal.git#17.0
```

### Erreur « Dépôt introuvable » (code 128) ?

Odoo Apps ne peut lire un dépôt **privé** sans autorisation explicite.

**Option A — Rendre le dépôt public (recommandé pour un module gratuit)**

1. GitHub → https://github.com/Akremjs/timbre-fiscal/settings
2. **Danger Zone** → **Change repository visibility** → **Public**
3. Réessayez la mise à jour sur Odoo Apps

**Option B — Garder le dépôt privé**

1. GitHub → https://github.com/Akremjs/timbre-fiscal/settings/access
2. **Collaborators** → **Add people**
3. Ajoutez l'utilisateur GitHub **`online-odoo`** (pas `odoo-online`)
4. Accès : **Read** suffit
5. Réessayez avec la même URL SSH

> Source : [FAQ Odoo Apps — repository privé](https://apps.odoo.com/apps/faq)

## Étapes sur Odoo Apps

1. Connectez-vous sur https://apps.odoo.com
2. **Soumettre un module** / Developer portal
3. Renseignez :
   - **Nom technique** : `timbre_fiscal_tn`
   - **Version Odoo** : 17.0
   - **Catégorie** : Accounting / Localizations
   - **Licence** : LGPL-3
   - **Prix** : Gratuit
   - **Repository GitHub (format Odoo Apps)** :
     `ssh://git@github.com/Akremjs/timbre-fiscal.git#17.0`
   - Branche : `17.0` (dossier `timbre_fiscal_tn/`)
4. Uploadez le ZIP ou liez le dépôt GitHub
5. Ajoutez captures d'écran facture avec ligne « Timbre Fiscal »

## Checklist avant publication

- [ ] Facture client test : ligne Timbre Fiscal 1,00 DT sans TVA
- [ ] Facture fournisseur : pas de timbre (par défaut)
- [ ] Module installable sans erreur sur Odoo 17 propre
- [ ] `icon.png` et `index.html` s'affichent correctement dans Apps
- [ ] Aucune URL ou auteur tiers (polyline.xyz, etc.)

## Support

Contacter **AKREM KHELIFI** :
- Email : akremkhelifi07@gmail.com
- WhatsApp : +216 54 444 373

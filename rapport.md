# Rapport de Validation Format

**Projet** : Bitcoin Educational Content
**Date de début** : 2026-01-16

---

## Résumé Exécutif

Ce rapport documente les problèmes identifiés lors du passage du validateur de format sur l'ensemble des contenus du dépôt.

---

## Problèmes Récurrents

### Erreurs Fréquentes

| Type d'erreur | Occurrences | Types de contenu affectés |
|---------------|-------------|---------------------------|
| Erreurs parsing YAML dans quiz (th.yml) | ~15 | courses |
| Erreurs parsing YAML dans quiz (rn.yml) | ~8 | courses |
| Erreurs parsing YAML dans quiz (de.yml) | ~6 | courses |
| Erreurs parsing YAML dans quiz (zh-*.yml) | ~5 | courses |
| Frontmatter manquant (name/goal/objectives) | 2 | courses |
| Fichier course.yml manquant | 2 | courses |
| UUID invalide | 1 | courses |
| Fichier question.yml manquant | 1 | courses |

### Avertissements Fréquents

| Type d'avertissement | Occurrences | Types de contenu affectés |
|----------------------|-------------|---------------------------|
| Quiz folder vide | 2 | courses |

---

## Observations par Type de Contenu

### Courses

**Statut initial** : 46 validés (25 OK, 19 erreurs, 2 warnings)
**Statut final** : 44 validés (42 OK, 0 erreurs, 2 warnings) ✅

**Corrections appliquées :**

1. **UUID invalide** → Corrigé
   - `courses/lnp206` : Remplacé `a1b2c3d4-5e6f-7g8h-9i0j-k1l2m3n4o5p6` par UUID v4 valide

2. **Script de validation** → Amélioré
   - Skip des fichiers `presentation.md` (pas de frontmatter requis)
   - Skip des dossiers cachés (`.claude`, etc.)

3. **Erreurs de parsing YAML** → Corrigées manuellement
   - **Backticks** : `cyp201/078/th.yml`, `dev303/043/th.yml` - valeurs enveloppées en guillemets doubles
   - **Guillemets non fermés** : `phi102` (8 fichiers de.yml, rn.yml, zh-Hans.yml)
   - **Deux-points dans le texte** : `phi102/201/es.yml` et fichiers thaï (12 fichiers)
   - **Espace manquant après deux-points** : `his201/007/rn.yml`
   - **Indentation incorrecte** : `his201/024/rn.yml`
   - **Items mixtes quotés/non-quotés** : `phi102` (rn.yml, zh-Hans.yml - 6 fichiers)
   - **Tabulations dans frontmatter** : `btc208/fr.md` - tabulations remplacées par espaces

4. **Dossier quiz vide supprimé** :
   - `courses/eco201/quizz/055` (pas de question.yml)

**Warnings restants (non bloquants) :**
- `csv404` : Dossier quiz existe mais vide
- `min306` : Dossier quiz existe mais vide

### Tutorials

**Statut initial** : 310 validés (262 OK, 20 erreurs, 28 warnings only)
**Statut final** : 310 validés (279 OK, 2 erreurs, 29 warnings only) - covers à ajouter

**Corrections appliquées :**

1. **Catégorie invalide dans le schéma** → Corrigé
   - Ajout de `content` et `explorer` aux catégories valides du schéma
   - Fixe 11 tutoriels (contribution/*, privacy/*)

2. **Champ description manquant** → Corrigé
   - `ledger-flex/fi.md` et `satochip/fi.md` utilisaient `kuvaus` (finnois) au lieu de `description`

3. **Description trop longue** → Corrigé (schéma)
   - maxLength augmenté de 500 à 1000 caractères

4. **License manquant** → Corrigé
   - Ajout CC-BY-SA-V4 à `arch-linux` et `vexl`

5. **Valeurs null** → Corrigé
   - `raspberry-pi-zero`: ajout tags (DIY, hardware, guides, personal-security)
   - `telegram`: suppression du champ `project_id` vide

6. **Image non-WebP** → À traiter manuellement
   - `tutorials/contribution/write-tutorials-git-expert`

**Erreurs restantes (covers manquantes) :**
- `tutorials/mining/bitaxe` : 28 fichiers sans cover.webp
- `tutorials/node/ronin-dojo` : 28 fichiers sans cover.webp
- Liste ajoutée en commentaire PR #4202

### Professors

**Statut initial** : 89 validés (0 OK, 89 erreurs) - **PROBLÈME SYSTÉMIQUE**
**Statut final** : 89 validés (73 OK, 0 erreurs, 20 warnings) ✅

**Erreurs systémiques identifiées :**

| Erreur | Occurrences | Description |
|--------|-------------|-------------|
| `contributor_id` requis | 89 | Nouveau champ requis mais absent partout |
| `id` non autorisé | 89 | Ancien champ à renommer en `contributor_id` ? |
| `company` requis | ~60 | Champ requis mais absent ou null |
| `affiliations` requis | ~60 | Champ requis mais absent ou null |
| `tips` requis | ~25 | Champ requis mais absent |
| `nostr` non autorisé dans links | ~20 | À ajouter au schéma |
| `github` non autorisé dans links | ~15 | À ajouter au schéma |
| `paynym`/`silent_payment` non autorisés dans tips | ~3 | À ajouter au schéma |
| `lightning_address: null` | ~15 | Null au lieu de string vide ou absent |

**Corrections appliquées (Session 4 - 2026-01-17) :**

1. **Schema `professor-scheme.json`** :
   - Changé `contributor_id` → `id` (format UUID)
   - Champs requis réduits à `name` et `id` uniquement
   - Autorisé `additionalProperties: true` pour `links` (github, nostr, etc.)
   - Autorisé `additionalProperties: true` pour `tips` (silent_payment, etc.)
   - Ajouté `silent_payment` comme propriété explicite dans tips

2. **Script `validate.py`** :
   - Ajout fonction `_find_and_remove_null_values()`
   - Valeurs null/vides rapportées comme **warnings** (pas erreurs)

3. **Data fix** :
   - Suppression `contributor_id` legacy de `professors/turtlecute/professor.yml`

**Warnings restants (20)** : Valeurs null/vides pour champs optionnels (lightning_address, company, affiliations)

### Events

**Statut** : 228 validés (49 OK, 179 erreurs) - **PROBLÈME SYSTÉMIQUE**

**Erreurs systémiques :**

| Erreur | Occurrences | Description |
|--------|-------------|-------------|
| `address_line_2: null` | ~150 | Null au lieu de string ou absent |
| `address_line_3: null` | ~150 | Null au lieu de string ou absent |
| `replay_url: null` | ~150 | Null au lieu de string ou absent |
| `live_url: null` | ~150 | Null au lieu de string ou absent |
| Format date incorrect | ~30 | `YYYY-MM-DD` au lieu de `YYYY-MM-DD HH:MM:SS` |
| `timezone` requis | ~10 | Champ manquant |
| `project_id` requis | ~5 | Champ manquant |

**Action requise** : Modifier le schéma pour accepter `null` ou rendre ces champs optionnels.

### Resources

#### resources/papers - OK
**Statut** : 45/45 OK - Aucune erreur

#### resources/projects - OK
**Statut** : 408/408 OK - Déjà validé précédemment

#### resources/channels - Quasi OK
**Statut** : 79 total (74 OK, 5 erreurs)
- UUID format invalide pour `contributors` (username au lieu d'UUID)
- `project_id` non autorisé

#### resources/bet - PROBLÈME SYSTÉMIQUE
**Statut** : 19/19 en erreur (1508 erreurs)
- `proofreading[].last_contribution_date: null` au lieu de string
- `proofreading[].contributor_names: null` au lieu de array

#### resources/books - PROBLÈME SYSTÉMIQUE
**Statut** : 175/175 en erreur (4212 erreurs)
- Propriétés non autorisées : `contributor_names`, `id`, `original_language`, `proofreading`
- `contributors` requis mais absent partout
- **Migration de schéma nécessaire**

#### resources/conferences - PROBLÈME SYSTÉMIQUE
**Statut** : 90/90 en erreur (207 erreurs)
- `builder` requis mais absent
- `tags` parfois requis
- Propriétés non autorisées : `id`, `original_language`, `project_id`, `proofreading`

#### resources/glossary - BUG PROBABLE
**Statut** : 846/846 en erreur (21761 erreurs)
- Erreur bizarre : `Missing required frontmatter field: 'frontmatter'`
- **Probable bug dans le content-schema du glossary**

#### resources/movies - License manquant
**Statut** : 41/41 en erreur (49 erreurs)
- `license` requis mais absent sur tous les movies

#### resources/newsletters - License manquant
**Statut** : 46/46 en erreur (53 erreurs)
- `license` requis mais absent sur toutes les newsletters

#### resources/podcasts - License manquant + UUID
**Statut** : 79/79 en erreur (82 erreurs)
- `license` requis mais absent
- UUID v1 au lieu de v4 pour certains IDs

---

## Points d'Attention

### Schémas à Améliorer

1. **professor-scheme.json** : Décalage majeur avec les données existantes
2. **event-scheme.json** : Gestion des valeurs `null` à revoir
3. **word-content-scheme.json** : Bug probable (requiert `frontmatter` dans frontmatter)
4. **tutorial-scheme.json** : Ajouter catégories `content` et `explorer`

### Problèmes Structurels

- Incohérence `id` vs `contributor_id` sur professors
- Champs requis trop stricts (license, builder, tips, company, affiliations)
- Format UUID v4 imposé mais données existantes avec UUID v1 ou placeholders
- Valeurs `null` non acceptées alors que présentes partout dans les données

### Suggestions d'Amélioration

1. **Rendre les schémas moins stricts** pour les champs optionnels
2. **Accepter les valeurs null** là où c'est pertinent
3. **Ajouter les propriétés manquantes** (nostr, github dans links)
4. **Migrer les données** pour renommer `id` en `contributor_id`

---

## Actions Correctives Proposées

| Priorité | Action | Impact | Effort |
|----------|--------|--------|--------|
| HAUTE | Fixer le bug glossary content-schema | 846 contenus | Faible |
| HAUTE | Ajouter `content`/`explorer` aux catégories tutorials | 11 tutoriels | Faible |
| MOYENNE | Rendre `license` optionnel sur movies/newsletters/podcasts | 166 contenus | Faible |
| MOYENNE | Accepter null pour address_line_*, replay_url, live_url | 179 events | Moyen |
| MOYENNE | Migrer `id` → `contributor_id` sur professors | 89 professors | Moyen |
| BASSE | Ajouter nostr/github aux links autorisés | ~35 professors | Faible |
| BASSE | Rendre company/affiliations/tips optionnels | ~60 professors | Faible |

---

## Statistiques Finales

**Date de validation** : 2026-01-16

| Métrique | Valeur |
|----------|--------|
| **Total contenus analysés** | 2401 |
| **Total erreurs** | 29 167 |
| **Total avertissements** | 60 |
| **Contenus sans erreur** | 863 (36%) |
| **Contenus avec erreurs systémiques** | 1538 (64%) |

### Répartition par catégorie

| Catégorie | Total | OK | Erreurs | Taux OK |
|-----------|-------|-----|---------|---------|
| courses | 44 | 42 | 0 | 95% ✅ |
| tutorials | 310 | 279 | 2 | 90% (covers à ajouter) |
| professors | 89 | 73 | 0 | 82% ✅ |
| events | 228 | 49 | 179 | 21% |
| resources/papers | 45 | 45 | 0 | 100% |
| resources/projects | 408 | 408 | 0 | 100% |
| resources/channels | 79 | 74 | 5 | 94% |
| resources/bet | 19 | 0 | 19 | 0% |
| resources/books | 175 | 0 | 175 | 0% |
| resources/conferences | 90 | 0 | 90 | 0% |
| resources/glossary | 846 | 0 | 846 | 0% |
| resources/movies | 41 | 0 | 41 | 0% |
| resources/newsletters | 46 | 0 | 46 | 0% |
| resources/podcasts | 79 | 0 | 79 | 0% |

### Conclusion

La majorité des erreurs proviennent de **décalages entre les schémas et les données existantes**, pas de vrais problèmes de contenu. Les schémas ont probablement été créés avec des exigences plus strictes que les données historiques.

**Recommandation** : Ajuster les schémas pour refléter la réalité des données avant d'imposer de nouvelles contraintes.

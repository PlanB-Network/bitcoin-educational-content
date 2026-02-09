# Validation Format - Suivi de Progression

**Objectif** : Passer le check individuel (`validate.py`) sur tous les contenus du dépôt.

**Date de début** : 2026-01-16

---

## Statut Global

| Type de Contenu | Total | Validés | Erreurs | Statut |
|-----------------|-------|---------|---------|--------|
| courses | 44 | 44 | 0 err / 2 warn | ✅ CORRIGÉ |
| tutorials | 310 | 310 | 113 err / 43 warn | EN COURS (covers manquantes) |
| professors | 89 | 89 | 0 err / 20 warn | ✅ CORRIGÉ |
| events | 228 | 228 | 0 err / 387 warn | ✅ CORRIGÉ |
| resources/bet | 19 | 19 | ~1508 err | EN ATTENTE |
| resources/books | 175 | 175 | ~4212 err | EN ATTENTE |
| resources/channels | 79 | 79 | 0 err | ✅ CORRIGÉ |
| resources/conferences | 90 | 90 | ~207 err | EN ATTENTE |
| resources/glossary | 846 | 846 | ~21761 err (BUG) | EN ATTENTE |
| resources/movies | 41 | 41 | 0 err | ✅ CORRIGÉ |
| resources/newsletters | 46 | 46 | 0 err | ✅ CORRIGÉ |
| resources/papers | 45 | 45 | 0 | ✅ OK |
| resources/podcasts | 79 | 79 | 0 err | ✅ CORRIGÉ |
| resources/projects | 408 | 408 | 0 | ✅ OK |

---

## Phase 2 - Validation Interactive

### Workflow par Type de Contenu

```
1. Lancer la validation
2. Analyser et catégoriser les erreurs
3. Présenter le résumé des erreurs à l'utilisateur
4. L'utilisateur décide : correction DATA ou SCHEMA ?
5. Appliquer les corrections selon la décision
6. Re-lancer la validation
7. Commit si 0 erreurs
```

### Types de Contenu à Traiter

| # | Type | Erreurs | Statut |
|---|------|---------|--------|
| 1 | events | 0 | [x] CORRIGÉ |
| 2 | resources/glossary | ~21761 | [ ] En attente |
| 3 | resources/movies | 0 | [x] CORRIGÉ |
| 4 | resources/newsletters | 0 | [x] CORRIGÉ |
| 5 | resources/podcasts | 0 | [x] CORRIGÉ |
| 6 | resources/channels | 0 | [x] CORRIGÉ |
| 7 | resources/conferences | ~207 | [ ] En attente |
| 8 | resources/books | ~4212 | [ ] En attente |
| 9 | resources/bet | ~1508 | [ ] En attente |

---

## Historique des Sessions

### Session 1 - 2026-01-16

**Tâches effectuées :**
- [x] Validation courses (46) - 48 erreurs, 17 warnings
- [x] Validation tutorials (310) - 133 erreurs, 43 warnings
- [x] Validation professors (89) - 393 erreurs (systémique)
- [x] Validation events (228) - 648 erreurs (systémique)
- [x] Validation resources (1678) - 27 925 erreurs (majoritairement systémiques)

**Notes :**
- Problèmes systémiques majeurs identifiés : schémas trop stricts vs données existantes
- Bug probable dans word-content-scheme.json (glossary)
- Catégories manquantes dans tutorial-scheme.json (content, explorer)
- Champ `license` requis mais absent sur movies/newsletters/podcasts

### Session 2 - 2026-01-16

**Tâches effectuées :**
- [x] Correction UUID invalide (lnp206)
- [x] Amélioration script validate.py (skip presentation.md, skip dossiers cachés)
- [x] Correction manuelle erreurs YAML quiz (backticks, guillemets, deux-points, indentation)
- [x] Suppression dossier quiz vide (eco201/quizz/055)
- [x] Correction tabulations dans frontmatter (btc208/fr.md)

**Résultat : courses passé de 48 erreurs → 0 erreur** ✅

### Session 3 - 2026-01-16

**Tâches effectuées :**
- [x] Ajout catégories `content` et `explorer` au schéma tutorial
- [x] Augmentation maxLength description de 500 à 1000 caractères
- [x] Ajout license CC-BY-SA-V4 (arch-linux, vexl)
- [x] Correction frontmatter finnois `kuvaus` → `description` (ledger-flex, satochip)
- [x] Ajout tags pour raspberry-pi-zero (DIY, hardware, guides, personal-security)
- [x] Suppression project_id null pour telegram
- [x] Liste covers manquantes ajoutée en commentaire PR #4202

**Résultat : tutorials passé de 133 erreurs (20 dossiers) → 113 erreurs (2 dossiers)**

Les 113 erreurs restantes sont des covers manquantes dans:
- `tutorials/mining/bitaxe` (28 fichiers)
- `tutorials/node/ronin-dojo` (28 fichiers)

### Session 4 - 2026-01-17

**Tâches effectuées :**
- [x] Mise à jour professor-scheme.json : `contributor_id` → `id` (format UUID)
- [x] Autorisation des types de liens additionnels (github, nostr, linkedin, etc.)
- [x] Champs rendus optionnels (seuls `name` et `id` requis)
- [x] Ajout `silent_payment` comme option de tip
- [x] Modification validate.py : valeurs null/vides = warnings (pas erreurs)
- [x] Suppression `contributor_id` legacy de turtlecute

**Résultat : professors passé de 89 erreurs → 0 erreur, 20 warnings** ✅

**Commit** : `75bb28e03a`

### Session 5 - 2026-02-08

**Tâches effectuées :**
- [x] Mise à jour event-scheme.json : project_id optionnel, ajout contributor_names/available_seats/custom_tc_disclaimer/is_gdpr_compliance/test_only
- [x] Pattern language élargi pour zh-hans/zh-hant
- [x] Ajout `00:00:00` aux dates sans heure (60 events)
- [x] Ajout timezone manquant (52 events, déduit de address_city_country)
- [x] Correction typo porject_id (beechworth-bush-bash-2025)
- [x] Remplacement UUID non-v4 (bitcoin-filmfest-2026, treasure-summit-2025)
- [x] Ajout tags manquants (bitcoin-bienes-raices-2025, bitcoin-filmfest-2026)
- [x] Ajout address_city_country manquant (3 events)
- [x] Suppression champ deprecated builder (3 liquid-dev-bootcamp)
- [x] Correction address_line_1 → address_city_country (the-bitcoin-summit-2025)
- [x] Correction tags invalides (the-bitcoin-summit-2025)
- [x] Correction zh-TW → zh-hant (unstoppable-money-human-rights-foundation)

**Résultat : events passé de 263 erreurs → 0 erreur, 387 warnings** ✅

**Commit** : `da19d9f110`

---

## Commandes Utiles

```bash
# Valider un contenu individuel
python scripts/validation-format/validate.py courses/btc101

# Valider tout un type de contenu
python scripts/validation-format/validate_all.py --type professors

# Output JSON pour analyse
python scripts/validation-format/validate_all.py --type resources/glossary --json
```

---
term: OP_CHECKSIGADD (0XBA)
---

Extrait les trois valeurs en haut de la pile : une `clé publique`, un `CScriptNum` `n` et une `signature`. Si la signature n'est pas le vecteur vide et n'est pas valide, le script se termine avec une erreur. Si la signature est valide où est le vecteur vide (`OP_0`), deux cas de figure se présentent :
* Si la signature est le vecteur vide : un `CScriptNum` avec la valeur de `n` est poussé sur la pile et l'exécution continue ;
* Si la signature n'est pas le vecteur vide et demeure valide : un `CScriptNum` avec la valeur de `n + 1` est poussé sur la pile et l'exécution continue.
Pour vulgariser, `OP_CHECKSIGADD` effectue une opération similaire à `OP_CHECKSIG`, mais au lieu de pousser vrai ou faux sur la pile, il ajoute `1` à la deuxième valeur en haut de la pile si la signature est valide, ou laisse cette valeur inchangée si la signature représente le vecteur vide.`OP_CHECKSIGADD` permet de créer les mêmes politiques multisignatures dans Tapscript qu'avec `OP_CHECKMULTISIG` et `OP_CHECKMULTISIGVERIFY` mais de manière vérifiable par lots, c'est-à-dire qu'il supprime le processus de recherche dans la vérification d'un multisig traditionnel et accélère donc la vérification tout en réduisant la charge opérationnelle sur les CPU des nœuds. Cet opcode a été ajouté dans Tapscript uniquement pour les besoins de Taproot.


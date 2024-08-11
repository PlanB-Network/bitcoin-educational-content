---
term: BIP32
---

Le BIP32 a introduit le concept de portefeuille hiérarchique et déterministe (HD wallet). Cette proposition permet de générer une hiérarchie de paires de clés à partir d'une graine commune, la `master seed`, en utilisant des fonctions de dérivation à sens unique. Chaque paire de clés générée peut elle-même être le parent d'autres clés enfants, formant ainsi une structure arborescente (hiérarchique). L'avantage du BIP32 est qu'il permet de gérer de multiples paires de clés différentes avec la nécessité de ne conserver qu'une seule graine pour les régénérer. Cette innovation a notamment permis de lutter contre le phénomène de réutilisation d'adresse qui est grave pour la confidentialité des utilisateurs. Le BIP32 permet aussi la création de sous-branches au sein d'un même portefeuille afin de faciliter sa gestion.


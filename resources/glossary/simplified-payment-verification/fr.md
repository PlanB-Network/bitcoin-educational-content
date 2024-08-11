---
term: SIMPLIFIED PAYMENT VERIFICATION
---

Méthode permettant aux clients légers de vérifier les transactions Bitcoin sans télécharger l'intégralité de la blockchain. Un nœud qui utilise SPV télécharge uniquement les entêtes de blocs qui sont beaucoup plus légers que les blocs complets. Lorsqu'il doit vérifier une transaction, le nœud SPV demande une preuve de Merkle aux nœuds complets pour confirmer que la transaction est incluse dans un bloc spécifique. Cette approche est efficace pour les appareils avec des ressources limitées, comme les smartphones, mais implique une dépendance vis-à-vis des nœuds complets, ce qui peut réduire la sécurité et augmenter la confiance requise.

> ► *On utilise souvent le sigle « SPV » pour évoquer cette méthode.*


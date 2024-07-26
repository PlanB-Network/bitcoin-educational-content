---
term: PILE (STACK)
---

Dans le contexte du langage script utilisé pour apposer des conditions de dépense sur des UTXOs Bitcoin, la pile est une structure de données de type « LIFO » (*Last In, First Out*) qui sert à stocker des éléments temporaires pendant l'exécution d'un script. Chaque opération dans le script manipule ces piles, où les éléments peuvent être ajoutés (*push*) ou retirés (*pop*). Les scripts utilisent les piles pour évaluer les expressions, stocker des variables temporaires, et gérer les conditions.

Dans l'exécution d'un script Bitcoin, 2 piles peuvent être utilisées : la pile principale et la pile alt (alternative). La pile principale est utilisée pour la majorité des opérations d'un script. C'est sur cette pile que les opérations de script ajoutent, retirent ou manipulent des données. La pile alternative, quant à elle, sert à stocker temporairement des données pendant l'exécution du script. Certains opcodes spécifiques, comme `OP_TOALTSTACK` et `OP_FROMALTSTACK`, permettent de transférer des éléments de la pile principale vers la pile alternative et inversement.

Par exemple, lors de la validation d'une transaction, les signatures et les clés publiques sont poussées sur la pile principale et traitées par des opcodes successifs pour vérifier que les signatures correspondent aux clés et aux données de la transaction.

> ► *En anglais, la traduction de « pile » est « stack ». On utilise généralement le terme anglais même en français lors de discussions techniques.*


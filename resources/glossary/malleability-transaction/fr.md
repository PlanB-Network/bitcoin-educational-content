---
term: MALLÉABILITÉ (TRANSACTION)
---

Se réfère à la possibilité de modifier légèrement la structure d'une transaction Bitcoin, sans en altérer l'effet, mais tout en changeant l'identifiant de transaction (*TXID*). Cette propriété peut être exploitée de manière malveillante pour induire en erreur les parties prenantes sur le statut d'une transaction, causant ainsi des problèmes comme la double dépense. La malléabilité était rendue possible par la flexibilité de la signature numérique utilisée. Le soft fork SegWit a notamment été introduit pour empêcher cette malléabilité des transactions Bitcoin, rendant compliquée une implémentation du Lightning Network. Il y parvient en écartant les données malléables de la transaction du calcul du TXID.

> ► *Bien que ce soit rare, on retrouve parfois le terme de « mutabilité » pour évoquer le même concept.*


---
term: SCRIPTWITNESS
---

Élément dans les entrées de transactions SegWit qui contient les signatures et les clés publiques nécessaires pour déverrouiller les bitcoins envoyés dans la transaction. Semblable au `scriptSig` des transactions Legacy, le `scriptWitness` n'est toutefois pas placé au même endroit. En effet, c'est cette partie, que l'on appelle le « témoin » (« *witness* » en anglais), qui est déplacée dans une base de données séparée afin de résoudre le problème de la malléabilité des transactions. Chaque input SegWit possède son propre `scriptWitness`, et tous les `scriptWitness` forment ensemble le champ `Witness` de la transaction.

> ► *Attention de ne pas confondre le `scriptWitness` avec le `witnessScript`. Tandis que le `scriptWitness` contient les données de témoin de tout input SegWit, le `witnessScript` définit les conditions de dépense d'un UTXO P2WSH ou P2SH-P2WSH et constitue un script à part entière, à la manière du `redeemScript` pour une sortie P2SH.*


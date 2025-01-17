---
term: BIP12
---

Proposition de Gavin Andresen pour améliorer la flexibilité et la confidentialité des scripts de transaction Bitcoin. Ce BIP propose d'implémenter un nouvel opcode de script, nommé `OP_EVAL`, qui permet d'évaluer un script contenu dans les données d'un `scriptSig` lors du processus de validation de la transaction. La principale modification du BIP12 est de permettre l'inclusion d'un script à l'intérieur d'un autre script. Cette technique permet la création de conditions plus complexes pouvant être vérifiées lors de la dépense, sans avoir besoin de les révéler aux utilisateurs qui envoient des bitcoins vers l'adresse utilisée. Le BIP12 a été ultérieurement remplacé par d'autres propositions plus sûres, notamment le BIP16 (P2SH), qui offre une méthode différente pour atteindre les mêmes objectifs que `OP_EVAL`.


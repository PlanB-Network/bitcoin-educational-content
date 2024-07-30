---
term: P2SH
---

P2SH est le sigle pour *Pay to Script Hash* (en français « payer au hachage du script »). C’est un modèle de script standard utilisé pour établir des conditions de dépense sur un UTXO. Contrairement aux scripts P2PK et P2PKH, où les conditions de dépense sont prédéfinies, P2SH permet l'intégration de conditions de dépense arbitraires et de fonctionnalités additionnelles au sein d'un script de transaction.

Techniquement, dans une transaction P2SH, le `scriptPubKey` contient l'empreinte cryptographique d'un `redeemScript`, plutôt que de conditions de dépense explicites. Cette empreinte est obtenue en utilisant un hachage `SHA256`. Lors de l'envoi de bitcoins à une adresse P2SH, le `redeemScript` sous-jacent n'est pas révélé. Seule son empreinte est incluse dans la transaction. Les adresses P2SH sont encodées en `Base58Check` et commencent par le chiffre `3`. Lorsque le destinataire souhaite dépenser les bitcoins reçus, il doit fournir un `redeemScript` correspondant à l'empreinte présente dans le `scriptPubKey`, ainsi que les données nécessaires pour satisfaire les conditions de ce `redeemScript`. Par exemple, dans un P2SH multisignatures, le script pourrait exiger des signatures de plusieurs clés privées.

L'utilisation de P2SH donne plus de flexibilité, car il permet la construction de scripts arbitraires sans que l'expéditeur en connaisse les détails. P2SH est introduit en 2012 avec le BIP16.


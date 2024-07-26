---
term: P2PKH
---

P2PKH est le sigle pour *Pay to Public Key Hash* (en français « payer au hachage d’une clé publique »). C’est un modèle de script standard utilisé pour établir des conditions de dépense sur un UTXO. Il permet de bloquer des bitcoins sur un hachage d’une clé publique, c’est-à-dire sur une adresse de réception. Ce script est associé au standard Legacy, et a été introduit dès les premières versions de Bitcoin par Satoshi Nakamoto.

À la différence du P2PK, où la clé publique est explicitement incluse dans le script, le P2PKH fait appel à une empreinte cryptographique de la clé publique. Ce script inclut le hachage `RIPEMD160` du `SHA256` de la clé publique et stipule que, pour accéder aux fonds, le destinataire doit fournir une clé publique correspondant à ce hachage, ainsi qu'une signature numérique valide générée à partir de la clé privée associée. Les adresses P2PKH sont encodées en utilisant le format `Base58Check`, ce qui leur confère une robustesse contre les erreurs typographiques grâce à l'utilisation d'une somme de contrôle. Ces adresses débutent systématiquement par le chiffre `1`.


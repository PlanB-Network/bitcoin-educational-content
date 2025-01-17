---
term: TAPROOT
---

Mise à jour majeure du protocole Bitcoin, adoptée par le biais d'un soft fork en novembre 2021. Cette mise à jour apporte des améliorations significatives en termes de confidentialité, d'efficacité et de flexibilité, en implémentant les BIP340, BIP341 et BIP342. Cette mise à jour a été verrouillée au bloc 687 284, le 12 juin 2021, lorsque 90 % des blocs générés pendant une période ont émis un signal favorable, manifestant ainsi la préparation des mineurs à activer la mise à jour (*Speady Trial*). L’activation a finalement eu lieu au bloc 709 632, le 14 novembre 2021, soit presque quatre ans après les premières discussions à ce sujet entre Pieter Wuille, Andrew Poelstra et Gregory Maxwell. Ce fut la première tentative de mise à jour majeure depuis l'épineuse activation de SegWit en 2017.

Taproot est également le nom du BIP341, implémenté au sein du soft fork de même nom, qui introduit un nouveau modèle de script nommé P2TR. Un script P2TR verrouille des bitcoins sur une clé publique Schnorr unique, dénommée $K$. Cependant, cette clé $K$ est en réalité un agrégat d'une clé publique $P$ et d'une clé publique $M$, cette dernière étant calculée à partir de la racine de Merkle d'une liste de `scriptPubKey`. Les bitcoins verrouillés avec un script P2TR peuvent être dépensés de deux manières distinctes : soit en publiant une signature pour la clé publique $P$, soit en satisfaisant l'un des scripts contenus dans l'arbre de Merkle. La première option est appelée « *key path* » (chemin de clé) et la seconde « *script path* » (chemin de script).



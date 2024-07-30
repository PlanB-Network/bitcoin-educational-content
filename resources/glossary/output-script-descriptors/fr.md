---
term: OUTPUT SCRIPT DESCRIPTORS
---

Les output script descriptors, ou simplement descriptors, sont des expressions structurées qui décrivent intégralement un script de sortie (`scriptPubKey`) et fournissent toutes les informations nécessaires pour suivre les transactions vers ou depuis un script particulier. Ces descriptors facilitent la gestion des clés dans les portefeuilles HD grâce à une description standard de la structure et des types d'adresses utilisés.

L'intérêt principal des descriptors réside dans leur capacité à encapsuler toutes les informations essentielles à la restauration d'un portefeuille dans une unique chaîne de caractères (en plus de la phrase de récupération). En sauvegardant un descriptor avec les phrases mnémoniques correspondantes, il est possible de restaurer non seulement les clés privées, mais aussi la structure précise du portefeuille et les paramètres de script associés. En effet, la récupération d’un portefeuille requiert non seulement la connaissance de la graine initiale, mais aussi des index spécifiques pour la dérivation des paires de clés enfants, ainsi que des `xpub` de chaque facteur dans le cadre d'un portefeuille multisig. Autrefois, on présumait que ces informations étaient implicitement sues de tous. Cependant, avec la diversification des scripts et l'émergence de configurations plus complexes, ces informations pourraient devenir difficiles à extrapoler, transformant ainsi ces données en informations privées et difficilement bruteforçables. L'utilisation de descriptors simplifie grandement le processus : il suffit de connaître la ou les phrases de récupération et le descriptor correspondant pour tout restaurer de façon fiable et sécurisée.

Un descriptor se compose de plusieurs éléments :
* Des fonctions de script comme `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) et `sortedmulti` (Multisignature avec clés triées) ;
* Des chemins de dérivation, par exemple `[d34db33f/44h/0h/0h]` qui indique un chemin dérivé et une empreinte de clé maîtresse spécifique ;
* Des clés en divers formats tels que des clés publiques en hexadécimal ou des clés publiques étendues (`xpub`) ;
* Une somme de contrôle, précédée d'un dièse, pour vérifier l'intégrité du descriptor.

Par exemple, un descriptor pour un portefeuille P2WPKH pourrait ressembler à :

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

Dans ce descriptor, la fonction de dérivation `wpkh` indique un type de script Pay-to-Witness-Public-Key-Hash. Elle est suivie par le chemin de dérivation qui contient :
* `cdeab12f` : l'empreinte de la clé maîtresse ;
* `84h` : qui signifie l'utilisation d'un objectif BIP84, destiné aux adresses SegWit v0 ;
* `0h` : qui indique qu'il s'agit d'une devise BTC sur le mainnet ;
* `0h` : qui fait référence au numéro de compte spécifique utilisé dans le portefeuille.

Le descriptor inclut également la clé publique étendue utilisée sur ce portefeuille : 

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Ensuite, la notation `/<0;1>/*` spécifie que le descriptor peut générer des adresses à partir de la chaîne externe (`0`) et interne (`1`), avec un wildcard (`*`) permettant la dérivation séquentielle de plusieurs adresses de manière paramétrable, similaire à la gestion d'un « gap limit » sur des logiciels de portefeuille classiques.

Enfin, `#jy0l7nr4` représente la somme de contrôle pour vérifier l'intégrité du descriptor.


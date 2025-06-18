---
term: DER
---

Acronyme de *Distinguished Encoding Rules*. C'est un sous-ensemble stricte des règles d'encodage ASN.1 définies dans la spécification [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) et utilisée pour encoder n'importe quel type de données dans une séquence binaire. DER est surtout utilisé dans des domaines spécifiques, comme en cryptographie, ou les données doivent êtes encodées de manière standard et prédictible.
Sur Bitcoin, les signatures ECDSA sont encodées au format DER. Elles se composent de deux nombres de 32 octets (`r`,`s`) encodés. Le format de signature se compose des éléments suivants (71 octets) :
```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```
Avec :
* `0x30` (1 octet) : identifiant d'une structure composée ;
* `length` (1 octet) : longueur des données suivantes ;
* `0x02` (1 octet) : identifiant de donnée type `INTEGER` (nombre entier) ;
* `r-length` (1 octet) : longueur de la valeur `r` suivante (32 octets) ;
* `r` (32 octets) : valeur `r` entant qu'entier gros-boutiste (big-endian) ;
* `0x02` (1 octet) : identifiant de donnée type `INTEGER` (nombre entier) ;
* `s-length` (1 octet) : longueur de la valeur `s` suivante (32 octets) ;
* `s` (32 octets) : valeur `s` entant qu'entier gros-boutiste (big-endian).
Dans une transaction Bitcoin, un octet est ajouté à la fin d'une signature DER pour indiquer le type de SigHash utilisé.

---
term: LIBSECP256K1
---

Bibliothèque C de haute performance et de haute sécurité pour les signatures numériques et d'autres primitives cryptographiques sur la courbe elliptique `secp256k1`. Puisque cette courbe n'a jamais été largement utilisée en dehors de Bitcoin (contrairement à la courbe `secp256r1` souvent préférée), cette bibliothèque vise à être la référence la plus complète pour son utilisation. Le développement de libsecp256k1 a été principalement orienté vers les besoins de Bitcoin, et les fonctionnalités destinées à d'autres applications peuvent être moins testées ou vérifiées. Une utilisation appropriée de cette bibliothèque nécessite une attention particulière, afin de s'assurer qu'elle convienne aux objectifs spécifiques des autres applications que Bitcoin.
La bibliothèque libsecp256k1 offre une variété de fonctionnalités, notamment :
* La signature ECDSA-secp256k1 et la vérification, ainsi que la génération de clés cryptographiques ;
* Des opérations additives et multiplicatives sur les clés secrètes et publiques ;
* La sérialisation et l'analyse des clés secrètes, des clés publiques et des signatures ;
* La signature et la génération de clés publiques à temps constant et à accès mémoire constant ;
* Et une multitude d'autres primitives cryptographiques.

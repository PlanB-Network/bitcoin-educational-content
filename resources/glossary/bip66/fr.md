---
term: BIP66
---

Introduit une standardisation du format des signatures dans les transactions. Ce BIP a été proposé en réaction à une divergence dans la manière dont OpenSSL gérait l'encodage des signatures sur différents systèmes. Cette hétérogénéité posait un risque de scission de la blockchain. Le BIP66 a permis d'uniformiser le format des signatures pour toutes les transactions en utilisant l'encodage DER stricte (*Distinguished Encoding Rules*). Cette modification nécessitait un soft fork. Pour son activation, le BIP66 a alors utilisé le même mécanisme que le BIP34, nécessitant l'augmentation du champ `nVersion` à sa version 3, et rejetant tous les blocs de version 2 ou inférieure une fois que le seuil de 95 % des mineurs était atteint. Ce seuil a été franchi au bloc n° 363 725 le 4 juillet 2015.


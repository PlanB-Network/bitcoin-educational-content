---
term: DÉRIVATION
---

Désigne le processus de génération de paires de clés enfants à partir d'une paire de clés parent (clé privée et clé publique) et d'un code de chaîne au sein d'un portefeuille déterministe et hiérarchique (HD). Ce processus permet de segmenter des branches et d’organiser un portefeuille en différents niveaux avec de nombreuses paires de clés enfants, qui peuvent toutes être récupérées en connaissant uniquement les informations de récupération de base (la phrase mnémonique et l'éventuelle passphrase). Pour dériver une clé enfant, on utilise la fonction `HMAC-SHA512` avec le code de chaîne parent et la concaténation de la clé parent et d’un index de 32 bits. Il existe deux types de dérivations :
* La dérivation normale, qui utilise la clé publique parent à la base de la fonction `HMAC-SHA512` ;
* La dérivation endurcie, qui utilise la clé privée parent à la base de la fonction `HMAC-SHA512` ;

Le résultat de HMAC-SHA512 est divisé en deux : les premiers 256 bits deviennent la clé enfant (privée ou publique après un passage dans ECDSA), et les 256 bits restants deviennent le code de chaîne enfant.



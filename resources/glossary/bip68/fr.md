---
term: BIP68
---

Introduit la possibilité d'utiliser des blocages temporels relatifs (*relative lock-time*) grâce au champ `nSequence`. Cela permet à une transaction de spécifier un délai relatif avant qu'elle soit incluse dans un bloc. Ce délai peut être défini en termes de nombre de blocs, ou bien comme un multiple de 512 secondes (c'est-à-dire, du temps réel). Notons que cette nouvelle interprétation du champ `nSequence` est uniquement valide si le champ `nVersion` est supérieur ou égal à `2`. Cette interprétation du champ `nSequence` se fait au niveau des règles de consensus de Bitcoin. Le timelock relatif définit un délai à partir de l'acceptation d'une transaction antérieure alors que le timelock absolu spécifie un moment précis avant lequel la transaction ne peut être incluse dans un bloc. Le BIP68 a été introduit via un soft fork le 4 juillet 2016 en même temps que le BIP112 et le BIP113, activé pour la première fois grâce à la méthode du BIP9.



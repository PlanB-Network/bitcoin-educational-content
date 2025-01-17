---
term: TYPE DE DEVISE
---

Dans le cadre des portefeuilles déterministes et hiérarchiques (HD), le type de devise (*coin type* en anglais) est un niveau de dérivation qui permet de différencier les branches du portefeuille en fonction des différentes cryptomonnaies utilisées. Cet étage de dérivation, défini par le BIP 44, se situe en profondeur 2 de la structure de dérivation, après la clé maîtresse et l'objectif (*purpose*). Par exemple, pour Bitcoin, l'index attribué est `0x80000000`, noté `/0'/` dans le chemin de dérivation. Cela signifie que toutes les adresses et comptes dérivés de ce chemin sont associés à Bitcoin. Cet étage de dérivation permet de bien séparer les différents actifs dans un portefeuille multi-devises. Voici les index utilisés pour différentes cryptomonnaies :
* Bitcoin : `0x80000000` ;
* Bitcoin Testnet : `0x80000001` ;
* Litecoin : `0x80000002` ;
* Dogecoin : `0x80000003` ;
* Ethereum : `0x8000003c`...

![](../../dictionnaire/assets/21.webp)


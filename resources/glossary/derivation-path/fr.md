---
term: CHEMIN DE DÉRIVATION
---

Dans le cadre des portefeuilles déterministes et hiérarchiques (HD), un chemin de dérivation désigne la séquence d'index utilisée pour dériver des clés enfants à partir d'une clé maîtresse. Décrit dans le BIP32, ce chemin permet d'identifier la structure arborescente de dérivation des clés enfants. Un chemin de dérivation est représenté par une série d'index séparés par des barres obliques, et commence toujours par la clé maîtresse (notée `m/`). Par exemple, un chemin typique pourrait être `m/84'/0'/0'/0/0`. Chaque niveau de dérivation est associé à une profondeur spécifique :
* `m /` indique la clé privée maîtresse. Elle est unique pour un portefeuille et ne peut pas avoir de sœurs à la même profondeur. La clé maîtresse est dérivée directement depuis la graine ;
* `m / purpose' /` indique l'objectif de dérivation qui permet d'identifier le standard suivi. Ce champ est décrit dans le BIP43. Par exemple, si le portefeuille respecte le standard BIP84 (SegWit V0), l'index sera alors `84'` ;
* `m / purpose' / coin-type' /` indique le type de cryptomonnaie. Cela permet de bien différencier les branches dédiées à une cryptomonnaie, des branches dédiées à une autre cryptomonnaie sur un portefeuille multi-coin. L'index dédié au bitcoin est le `0'` ;
* `m / purpose' / coin-type' / account' /` indique le numéro de compte. Cette profondeur permet de différencier et d’organiser facilement un portefeuille en différents comptes. Ces comptes sont numérotés à partir de `0'`. Les clés étendues (`xpub`, `xprv`...) se trouvent à ce niveau de profondeur ;
* `m / purpose' / coin-type' / account' / change /` indique la chaîne. Chaque compte tel que défini en profondeur 3 dispose de deux chaînes en profondeur 4 : une chaîne externe et une chaîne interne (également appelée « change »). La chaîne externe dérive des adresses destinées à être communiquées publiquement, c’est-à-dire les adresses que l’on nous propose lorsque l’on clique sur « recevoir » dans notre logiciel de portefeuille. La chaîne interne dérive les adresses destinées à ne pas être échangées publiquement, c’est-à-dire principalement les adresses de change. La chaîne externe est identifiée avec l'index `0` et la chaîne interne est identifiée avec l'index `1`. Vous remarquerez qu'à partir de cette profondeur, on ne réalise plus une dérivation endurcie, mais une dérivation normale (il n'y a pas d'apostrophe). C'est grâce à ce mécanisme que l'on est capable de dériver l'ensemble des clés publiques enfants à partir de leur `xpub` ;
* `m / purpose' / coin-type' / account' / change / address-index` indique simplement le numéro de l’adresse de réception et de sa paire de clés, afin de la différencier de ses sœurs à la même profondeur sur la même branche. Par exemple, la première adresse dérivée dispose de l’index `0`, la deuxième adresse dispose de l’index `1`, etc...

Par exemple, si mon adresse de réception dispose du chemin de dérivation `m / 86' / 0' / 0' / 0 / 5`, on peut en déduire les informations suivantes :
* `86'` indique que nous suivons le standard de dérivation du BIP86 (Taproot / SegWit V1) ;
* `0'` indique que c'est une adresse Bitcoin ;
* `0'` indique que l'on est sur le premier compte du portefeuille ;
* `0` indique que c'est une adresse externe ;
* `5` indique que c'est la sixième adresse externe de ce compte.

![](../../dictionnaire/assets/18.webp)


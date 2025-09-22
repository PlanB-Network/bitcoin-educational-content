---
name: Dojo
description: Un nœud Bitcoin open-source orienté confidentialité et autonomie
---

![cover](assets/cover.webp)

*Ce tutoriel s’appuie sur [la documentation officielle d’Ashigaru](https://ashigaru.rs/docs/), que j’ai reprise et enrichie. J’ai réécrit toutes les sections pour en améliorer la clarté, ajouté des explications détaillées supplémentaires, ainsi que des illustrations pour les débutants, afin de rendre l’installation et l’utilisation plus faciles à comprendre.*

---

Dojo est un logiciel libre conçu pour servir de serveur backend à certains portefeuilles Bitcoin axés sur la confidentialité, en s'appuyant sur un nœud Bitcoin Core. Historiquement, il a été développé pour fonctionner avec Samourai Wallet, un portefeuille mobile qui proposait des fonctionnalités avancées de confidentialité comme Whirlpool (coinjoin), Ricochet, Stonewall, PayNym... Samourai Wallet est aujourd’hui à l’arrêt suite à l'arrestation de ses développeurs, mais son successeur communautaire, **Ashigaru Wallet**, a pris le relais et continue de s’appuyer sur Dojo pour offrir une expérience complète aux utilisateurs souhaitant garder le contrôle de leurs données lors de leur utilisation de Bitcoin.

01

Concrètement, Dojo agit comme une passerelle entre votre portefeuille et le réseau Bitcoin. Sans Dojo, un portefeuille mobile léger doit interroger des serveurs tiers pour obtenir l’état de vos UTXOs et votre historique ou pour diffuser vos transactions. Cela implique une dépendance et une fuite de données sensibles vers un serveur tiers (adresses utilisées, montants, fréquence des paiements...). Avec Dojo, vous hébergez vous-même ce serveur, directement connecté à votre propre nœud Bitcoin. Ainsi, toutes les requêtes de votre portefeuille passent par une infrastructure que vous contrôlez, sans intermédiaire, ce qui renforce votre confidentialité et votre souveraineté.

## Prérequis pour installer un Dojo

L’installation d’un serveur Dojo ne nécessite pas une machine ultra-puissante. Toute personne disposant d’un ordinateur d’entrée de gamme, d’une connexion Internet stable et capable de laisser cet appareil allumé en continu (24 heures sur 24 et 7 jours sur 7) peut mettre en place un Dojo fonctionnel.

### Choisir son type de machine

Vous pouvez utiliser :
- un ordinateur portable ;
- un ordinateur de bureau ;
- un mini-PC (par exemple un Intel NUC, Lenovo Thincentre Tiny...).

Chaque option présente des avantages et des inconvénients :
- Le prix : un mini-PC ou un ordinateur de bureau reconditionné sera souvent moins cher qu’un portable neuf.
- L’encombrement : un mini-PC prend moins de place.
- L’alimentation électrique : un portable a l’avantage d’avoir une batterie, ce qui lui évite de s’éteindre en cas de micro-coupure, contrairement à un mini-PC.
- Les possibilités d’évolution : les barbones permettent généralement d’ajouter de la mémoire ou de remplacer facilement un disque dur.

Pour plus d'information sur le choix de votre matériel, je vous conseille de suivre cette formation :

https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Matériel recommandé

Il n’est pas nécessaire d’acheter une machine neuve. Un ordinateur reconditionné avec les caractéristiques ci-dessous donnera de bien meilleures performances que les cartes électroniques monocartes (comme le Raspberry Pi).

**Spécifications minimales :**
- Architecture x86-64 (processeur 64 bits).
- Processeur double cœur 2 GHz ou plus rapide.
- 8 Go de RAM minimum.
- Disque SSD NVMe de 2 To ou plus (pour stocker la blockchain de Bitcoin et les index nécessaires).

**Système d’exploitation recommandé :**
- Une distribution basée sur Debian, comme Ubuntu 24.04 LTS.

**Matériel recommandé :**
- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC

Il est tout à fait possible de faire tourner un serveur Dojo sur d’autres configurations matérielles. Cependant, pour obtenir les meilleures performances et limiter les problèmes, il est conseillé de respecter les recommandations ci-dessus.

## 1 - Installer Ubuntu

*Si vous souhaitez installer Dojo sur un appareil déjà configuré, vous pouvez ignorer cette étape et passer directement à l’étape 2.*

Après avoir préparé le matériel choisi, il faut maintenant y installer un système d’exploitation. Vous pouvez utiliser pratiquement n’importe quelle distribution Debian, mais je vous recommande d’opter pour une version LTS d’Ubuntu, car c'est parfaitement adapté à notre usage. Voici les étapes à suivre :  

Depuis un ordinateur déjà fonctionnel (votre machine habituelle), téléchargez l’image ISO d’Ubuntu LTS [sur le site officiel](https://ubuntu.com/download/desktop) (`24.04` au moment de la rédaction de ce tutoriel, mais prenez la plus récente si une autre est disponible).

02

Insérez une clé USB d’au moins 8 Go dans cet ordinateur, puis créez une clé amorçable à l’aide d’un logiciel comme [Balena Etcher](https://etcher.balena.io/). Sélectionnez l’image ISO d’Ubuntu que vous venez de télécharger, choisissez la clé USB comme périphérique cible, puis lancez la création.

03




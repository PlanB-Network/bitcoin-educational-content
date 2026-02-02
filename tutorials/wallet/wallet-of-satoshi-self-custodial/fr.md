---
name: Wallet of Satoshi - Self-Custody
description: Découvrez comment configurer le mode self-custody d'un portefeuille Wallet of Satoshi
---

![cover](assets/cover.webp)

***Not your keys, not your coins*.** Plus qu'un adage, c'est un principe fondamental de Bitcoin qui signifie que si vous ne contrôlez pas les **clés privées** permettant de déverrouiller vos bitcoins, vous n’en êtes pas réellement le propriétaire. 

Beaucoup d’utilisateurs commencent généralement par un **portefeuille custodial**, ensuite, migrent vers un **portefeuille self-custodial**, où ils contrôlent eux-mêmes leurs clés privées. 
Dans ce tutoriel, nous ne vous présenterons pas un nouveau portefeuille self-custodial. En revanche, nous vous amenons à la découverte de la nouvelle fonctionnalité des portefeuilles ***Wallet of Satoshi*** : **le mode self-custodial**.

L'objectif de cette nouvelle intégration est de permettre aux utilisateurs de conserver le contrôle de leurs clés privées tout en bénéficiant de la simplicité et d'une expérience utilisateur fluide.

Avant d'aborder le cœur du sujet, prenons un moment pour examiner la particularité du mode self-custody proposé par Wallet of Satoshi (WoS).

## La particularité du mode self-custody 

La simplicité et la fluidité du mode self-custody de WoS vous éliminent la complexité liée à l'ouverture de canaux Lightning, à l'administration de nœuds… Mais comment est-ce possible?
 
En effet, le mode self-custody de Wallet of Satoshi est alimenté par **Spark**. C'est une solution de couche 2 pour Bitcoin, créée par Lightspark, qui utilise la technologie des **statechains**. 
 
Par conséquent, vous n'effectuez pas vos transactions directement sur le Lightning Network. Les interactions entre le réseau **LN** et **Spark** s'effectuent à travers des **swaps atomiques**.
  
Par exemple, Bob souhaite régler une facture Lightning en utilisant WoS. Il transfère ses satoshis, mais en arrière-plan, ceux-ci sont acheminés vers un **Spark Service Provider (SSP)** sur Spark, qui exécute en retour le paiement sur le réseau Lightning.
 
À l'inverse, Alice souhaite obtenir des fonds directement dans son portefeuille WoS. Dans ce cas, le **SSP** reçoit les sats via LN et crédite immédiatement le portefeuille d'Alice.

Ainsi, il est important de noter que pour profiter de la simplicité et de la fluidité de WoS, vous devez dépendre des serveurs de Spark. Toutefois, en termes de sécurité, si un SSP devient malveillant ou indisponible, vous disposez du mécanisme de **sortie unilatérale**, une mesure de sécurité qui vous permet de récupérer vos fonds sur Bitcoin on-chain (même si cela peut être lent et coûteux) , garantissant ainsi une expérience self-custodial comparable à celle d'un nœud Lightning privé.

C'est donc en tenant compte de tous ces paramètres que chacun pourra souverainement décider le montant de sats qu'il souhaite conserver dans le WoS self-custody.

Si vous débutez avec Wallet of Satoshi, vous devez naturellement télécharger l'application mobile du portefeuille. Par contre, si vous l'utilisez déjà et souhaitez savoir comment utiliser le **mode self-custody**, veuillez vous rendre directement à la section **Configuration du mode self-custody** de ce tutoriel.

## Débuter avec Wallet of Satoshi 

Rendez-vous dans votre store d'applications et téléchargez WoS. 

![screen](assets/fr/03.webp)

Ouvrez l'application une fois le téléchargement terminé et appuyez sur **Début**.

![screen](assets/fr/04.webp)

Vous serez redirigé vers l'interface principale de l'application. En effet, lorsque vous accédez à WoS pour la première fois, le portefeuille est déjà fonctionnel et s'ouvre systématiquement en mode custodial par défaut.

![screen](assets/fr/05.webp)

Même si vous ne souhaitez pas utiliser WoS en mode custodial, nous vous recommandons de le configurer en premier lieu. Pour cela, consultez ce tutoriel.

https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Passons maintenant à la configuration de notre WoS en self-custody.

## Configuration du mode self-custody

Cliquez sur le menu hamburger (icône à 3 barres) dans le coin supérieur droit de l'interface principale.

![screen](assets/fr/06.webp)

Puis, dans le menu qui apparaît, cliquez sur le sous-menu **Open Self Custody Wallet**.

![screen](assets/fr/07.webp)

WoS vous indique immédiatement que *le mode self-custody est fourni avec une phrase de récupération. Aussi, vous êtes le seul responsable de la sécurité de vos fonds*.

![screen](assets/fr/08.webp)

Cochez le bouton "**I Understand**" (1), tapez ensuite sur le bouton **Open Self Custody Wallet** (2) qui s'affiche en jaune voyant.

![screen](assets/fr/09.webp)

### Création du portefeuille self-custodial

Après avoir cliqué sur le bouton **Open Self Custody Wallet**, cliquez sur le bouton **Create a New Wallet**.

![screen](assets/fr/10.webp)

WoS se chargera alors de vous créer un portefeuille self-custody, toujours dans la même application. Vous serez donc en mesure de basculer entre le mode **custodial** (disponible dans certaines régions) et le mode **self-custodial** selon votre convenance et à tout moment.

![screen](assets/fr/11.webp)

Une fois créé, vous serez redirigé vers l'interface principale de WoS en mode self-custody. Vous constaterez qu'il n'y a pas de différences entre l'aperçu général et les interfaces d'un portefeuille WoS custody et ceux d'un portefeuille WoS self-custody.

### Sauvegarde de votre phrase mnémonique

Tapez sur l'ensemble icône **Trousseau de clés + Backup Wallet** qui est située en haut de l'écran entre le nom Wallet of Satoshi et le menu hamburger. 

![screen](assets/fr/12.webp)

WoS vous propose deux différentes méthodes de sauvegarde de vos 12 mots (phrase mnémonique) : la **sauvegarde via Google Drive** et la **sauvegarde manuelle**.

Bien que nous vous suggérons la sauvegarde manuelle qui est la plus sécurisée, nous vous exposerons aussi comment faire la sauvegarde via Google Drive.

#### La sauvegarde via Google Drive

Cliquez sur le bouton **Google Drive Backup**.

![screen](assets/fr/13.webp)

Si vous optez pour la sauvegarde avec Google Drive, en cas de compromission de votre compte Google, il existe un risque élevé que vous soyez dérobé. En effet, l'individu malintentionné aurait accès au fichier contenant vos 12 mots et pourrait ainsi accéder à votre portefeuille.

Ajouter un mot de passe pour crypter le fichier contenant vos 12 mots est assurément une bonne solution pour ajouter une couche supplémentaire de sécurité.

Activez donc le bouton **Encrypt with a password** (*Crypter avec un mot de passe*) dans les options avancées.

![screen](assets/fr/14.webp)

Sur la nouvelle interface qui apparaît, définissez un mot de passe fort, puis confirmez-le à nouveau.

![screen](assets/fr/15.webp)

Il importe de vous rappeler qu'une fois le mot de passe choisi, vous ne devez pas l'oublier ou perdre le support sur lequel vous l'aurez inscrit. En cas d'oubli ou de perte, vous ne pourrez plus jamais accéder à vos 12 mots et par conséquent à vos fonds. 

Après avoir choisi votre mot de passe, sélectionnez un compte Google pour la sauvegarde, puis accordez les accès requis par WoS.

![screen](assets/fr/16.webp)

![screen](assets/fr/17.webp)

Patientez quelques secondes. Bingo! Votre sauvegarde a été effectuée avec succès. 

![screen](assets/fr/18.webp)

Vous avez toujours la possibilité de faire une sauvegarde supplémentaire en choisissant la deuxième méthode de sauvegarde : celle manuelle. 
#### La sauvegarde manuelle

Si vous optez pour la sauvegarde manuelle, nous vous recommandons fortement de consulter ce tutoriel qui explore les bonnes pratiques pour sauvegarder votre phrase mnémonique de manière sécurisée, afin de ne pas perdre l’accès à vos bitcoins.

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Appuyez sur le bouton **Manual Backup**.

![screen](assets/fr/19.webp)

Sur l'interface suivante, WoS vous rappelle quelques consignes de sécurité à prendre en considération avant de procéder à la sauvegarde manuelle.

Activez le bouton **I understand** et appuyez sur le bouton **Next**.

![screen](assets/fr/20.webp)

Vos 12 mots vous seront ensuite présentés. Procédez à leur sauvegarde, puis cliquez sur le bouton **Next**. 

![screen](assets/fr/21.webp)

Sur cette nouvelle interface, appuyez sur les mots dans le bon ordre. 

![screen](assets/fr/22.webp)

Enfin, cliquez sur le bouton **Next**. Félicitations! Votre sauvegarde est terminée.

![screen](assets/fr/23.webp)

## Restauration de portefeuille self-custody

Lorsque vous désirez récupérer ou restaurer votre portefeuille WoS self-custody suite à un changement de téléphone ou pour toute autre raison, voici les étapes à suivre. 

Ouvrez le portefeuille WoS, cliquez sur le menu hamburger dans le coin supérieur droit de l'interface principale.
Dans le menu qui apparaît, cliquez sur le sous-menu **Open Self Custody Wallet**.
Sur la nouvelle interface qui apparaît, appuyez sur le bouton **Restore Existing Wallet**.

![screen](assets/fr/24.webp)

Choisissez une méthode de restauration et passez à l'étape suivante.

![screen](assets/fr/25.webp)

### Restauration via Google Drive

1. Appuyez sur le bouton **Restore From Google Drive**.
2. Sélectionnez un compte Google et laissez WoS récupérer les données de récupération qui ont été sauvegardées sur votre Google Drive.
3. Entrez ensuite votre mot de passe de cryptage (si vous l'aviez défini auparavant, bien sûr) du fichier contenant vos 12 mots.
4. Patientez quelques instants, le temps que la restauration soit effective, et vous pourrez accéder à nouveau à votre portefeuille.

### Restauration manuelle

 1. Appuyez sur le bouton **Restore Manually**.
 2. Entrez ensuite les 12 mots de votre phrase mnémonique en écrivant chaque mot devant son numéro d'ordre de départ.
 3. Patientez quelques instants, le temps que la restauration soit effective, et vous pourrez accéder à nouveau à votre portefeuille.


### Transfert de bitcoins entre WoS custody et WoS self-custody

Lorsque vous disposez de bitcoins (sats) dans votre portefeuille WoS custody et que vous créez un portefeuille WoS self-custody, vous ne perdez pas vos fonds. Mieux, vous pouvez les transférer vers votre portefeuille self-custody et vice-versa.

Pour le faire :
Vous pouvez copier votre adresse lightning WoS self-custody ou une facture que vous avez créée.

![screen](assets/fr/26.webp)

Ouvrez maintenant votre portefeuille custody et appuyez sur le bouton **Envoyer**.

Collez ensuite l'adresse ou la facture. Appuyez une seconde fois sur **Envoyer**.

Retourner à nouveau dans votre portefeuille self-custody et vous verrez que vous aviez bel et bien reçu les fonds. 

![screen](assets/fr/27.webp)

## Envoi et réception de bitcoins 

Concernant l'envoi et la réception de bitcoins dans un mode self-custody, à l'instar de l'aperçu général et des interfaces, ils ne diffèrent en rien de l'envoi et de la réception de bitcoins via un portefeuille WoS custody. 

Veuillez donc consulter le tutoriel de base relatif à l'utilisation de Wallet of Satoshi sur Plan₿ Network.

https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Vous êtes à présent en mesure de configurer et d'utiliser par vous-même Wallet of Satoshi en mode self-custody.

Si ce tutoriel vous a été utile, je vous prie de me laisser un pouce vert ci-dessous. Merci beaucoup !

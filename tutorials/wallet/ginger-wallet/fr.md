---
name: Ginger Wallet
description: Un logiciel de portefeuille Bitcoin open source et en self-custody, fork de Wasabi Wallet, qui intègre les Coinjoins
---
![cover](assets/cover.webp)

Ginger Wallet est un portefeuille Bitcoin open source, non custodial, axé sur la confidentialité et la vie privée. Il a démarré comme fork de Wasabi Wallet (après la version 2.0.7.2 - licence MIT).

Ginger Wallet conserve l'architecture technique de Wasabi tout en y ajoutant quelques spécificités. Selon la [documentation de Ginger Wallet](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet), Wasabi privilégie **l’autonomie et le contrôle**, tandis que Ginger mise sur la **facilité d'utilisation, la sécurité et une expérience simplifiée** rendant l'utilisation accessible à ceux qui sont moins familiers avec les aspects techniques.

Ginger Wallet est un logiciel de portefeuille pour les ordinateurs uniquement (pas d'application mobile).

## Qu’est-ce que le Coinjoin ? 

Le **coinjoin** est une structure particulière de transaction Bitcoin qui regroupe plusieurs participants au sein d’une même transaction collaborative. Ce mécanisme mélange les entrées de différents utilisateurs dans une transaction commune, rendant ainsi le traçage des fonds extrêmement difficile, voire souvent impossible si c'est bien fait. En conséquence, il devient presque impossible pour un observateur extérieur d’identifier avec certitude l’origine et la destination des bitcoins impliqués, contrairement aux transactions Bitcoin classiques.

Pour vous, en tant qu’utilisateur, le coinjoin permet de préserver votre confidentialité. Par exemple, si vous recevez un don de 10 000 sats sur une adresse Bitcoin, l’expéditeur peut tracer ces fonds et, dans certains cas, déduire que vous détenez une quantité plus importante de bitcoins ou observer vos activités. En réalisant un coinjoin après ce don de 10 000 sats, vous rompez la traçabilité : l’expéditeur ne pourra plus tirer d’informations vous concernant à partir de ce paiement.

Le coinjoin chaumien offre un haut niveau de sécurité, car les fonds demeurent en permanence sous le contrôle exclusif de l’utilisateur. Même les opérateurs des serveurs de coordination ne peuvent en aucun cas détourner les bitcoins des participants. Ni les utilisateurs entre eux, ni le coordinateur n'ont besoin de se faire mutuellement confiance : chacun conserve la maîtrise de ses clés privées et reste seul habilité à valider les transactions. Aucun tiers ne peut donc s’approprier vos bitcoins au cours d’un coinjoin, ni établir de lien direct entre vos entrées et vos sorties.

Pour approfondir la notion de coinjoin, consultez le cours BTC 204 de Plan ₿ Academy :

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Installer Ginger Wallet 

Pour installer Ginger Wallet, rendez-vous sur le site web [Ginger Wallet](https://gingerwallet.io).

Appuyez sur **Télécharger** pour télécharger la version adaptée à votre ordinateur (Windows / MacOs / Linux).

![screen](assets/fr/03.webp)

Une autre possibilité : celle de se rendre sur le [GitHub du projet](https://github.com/GingerPrivacy/GingerWallet/releases) afin de le télécharger. 

![screen](assets/fr/04.webp)

Ensuite, lancez le programme d'installation.

![screen](assets/fr/05.webp)


## Configuration des paramètres

### Configurations préliminaires

Ouvrez Ginger Wallet, choisissez votre langue préférée.

![screen](assets/fr/06.webp)

Ginger vous rappelle dès le début les frais liés au processus de coinjoin.

![screen](assets/fr/07.webp)

Appuyez ensuite sur **Commencer**, puis sur **Nouveau** pour créer un nouveau portefeuille.

![screen](assets/fr/08.webp)

Passez ensuite à la sauvegarde et à la confirmation de votre seedphrase.

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)

![screen](assets/fr/10.webp)

Pour plus de sécurité, Ginger Wallet vous donne la possibilité d'ajouter une passphrase.

![screen](assets/fr/11.webp)

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Cette passphrase une fois ajoutée, vous sera demandée à chaque fois que vous tenterez d'accéder à votre portefeuille.

![screen](assets/fr/12.webp)

Ginger active automatiquement le **Coinjoin** par défaut lors de la création de votre portefeuille. Vous en êtes informé et pouvez ensuite personnaliser ce paramètre selon vos besoins.

![screen](assets/fr/13.webp)


### Configuration des paramètres généraux

Une fois votre premier portefeuille créé, vous accédez à l'interface de Ginger Wallet.

![screen](assets/fr/14.webp)

Activez le **Mode discret**, si vous souhaitez cacher les soldes de vos portefeuilles.

![screen](assets/fr/15.webp)

Vous pouvez créer plusieurs portefeuilles sur Ginger Wallet. Il suffit de cliquer sur **Ajouter un portefeuille**.

![screen](assets/fr/16.webp)

Ginger prend en charge l’utilisation de portefeuilles matériels via l’interface standard de Bitcoin Core, bien qu’une intégration directe depuis ou vers un portefeuille matériel ne soit pas encore disponible.

Parmi les portefeuilles matériels compatibles, on retrouve notamment (liste non exhaustive) :
- Blockstream Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- etc.

Maintenant, cliquez sur **Paramètres**.

![screen](assets/fr/17.webp)

Ces paramètres sont ceux de l'application en général et les configurations que vous y ferez s'appliqueront à tous les portefeuilles.

Dans **Paramètres**, vous avez les onglets :

- **Général**

![screen](assets/fr/18.webp)

- **Apparence**

Dans cet onglet, vous pouvez changer entre autres la langue, la devise ou encore l'unité d'affichage des frais (BTC/Satoshi).

![screen](assets/fr/19.webp)

- **Bitcoin**

Cet onglet vous offre la possibilité d'activer l'exécution de Bitcoin Knots au démarrage de l'application, de choisir votre réseau (Main/RegTest), et votre fournisseur de taux de frais (Mempool Space/Blockstream info/Full Node), etc.

![screen](assets/fr/20.webp)

- **Sécurité**

Dans l'onglet Sécurité, vous pouvez activer l'authentification à deux facteurs, activer ou désactiver Tor et même le désactiver une fois l'application Ginger fermée. 

![screen](assets/fr/21.webp)

**NB** :
- Concernant l’authentification à double facteur, assurez-vous que votre application d’authentification prend en charge le protocole SHA256 et les codes à 8 chiffres. En effet, Ginger Wallet requiert un code 2FA à 8 chiffres afin de renforcer la sécurité. Ce format plus long rend le code bien plus difficile à deviner ou à compromettre, offrant ainsi une meilleure protection contre tout accès non autorisé.
- Par défaut, l’ensemble du trafic réseau de Ginger transite par Tor, ce qui évite toute configuration manuelle. Si Tor est déjà actif sur votre système, Ginger l’utilisera automatiquement en priorité.

Mais, une fois que vous désactivez Tor dans les paramètres, votre vie privée reste globalement préservée, sauf dans deux situations :
- pendant un Coinjoin, le coordinateur pourrait relier vos entrées et sorties à votre adresse IP ;
- lors de la diffusion d’une transaction, un nœud malveillant auquel vous vous connectez pourrait associer votre transaction à votre IP.

N'oubliez pas d'appuyer à chaque fois sur **Fait** (dans le coin inférieur droit), pour sauvegarder vos paramètres. Certains paramètres nécessitent que Ginger Wallet soit redémarré pour prendre effet.

Par ailleurs, la barre de recherche située en haut des portefeuilles vous permet de rechercher et d'accéder à n'importe quel paramètre, etc...

![screen](assets/fr/22.webp)


### Configuration d'un portefeuille

Plusieurs portefeuilles peuvent être créés dans l'application, par conséquent, chaque portefeuille peut donc être configuré selon votre convenance. Pour le faire, cliquez sur les **trois points** devant le nom du portefeuille, ensuite sur **Paramètres du portefeuille**. 

![screen](assets/fr/23.webp)

Comme vous pouvez le constater, mis à part le paramètre du portefeuille, vous pourrez voir vos UTXOs (liste des jetons que vous possédez), les statistiques et les informations du portefeuille (la clé publique étendue par exemple).

Pour revenir à la configuration de notre portefeuille, une fois que vous cliquez sur les paramètres du portefeuille, vous accèderez aux onglets suivants :
- **Général** (où vous pourrez modifier le nom du portefeuille) ;

![screen](assets/fr/24.webp)

- **Coinjoin** (où vous pourrez personnaliser les paramètres du coinjoin de ce portefeuille) ;

![screen](assets/fr/25.webp)

- **Outils** (où vous avez la possibilité de vérifier votre seedphrase, ou de synchroniser votre portefeuille à nouveau, ou encore de supprimer ce portefeuille). 

![screen](assets/fr/26.webp)


## Recevoir des bitcoins

Pour recevoir des bitcoins dans votre portefeuille sur Ginger Wallet :
- appuyez sur **Recevoir** ;

![screen](assets/fr/27.webp)

- Entrez le nom de la source à laquelle vous souhaitez associer l’adresse. C'est de l'étiquetage permettant de conserver la traçabilité de vos paiements. Cela n’a aucune incidence on-chain ; il s’agit simplement d’une information de traçabilité conservée localement dans votre application ;

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)

- cliquez sur la petite flèche à gauche de **Générer** pour choisir votre format d'adresse (**SegWit** /**Taproot**) , puis cliquez sur **Générer**, pour générer une adresse et un code QR.

![screen](assets/fr/29.webp)

Cette adresse ou ce code QR, sera utilisé par votre expéditeur pour vous envoyer des bitcoins.

![screen](assets/fr/30.webp)


## Envoyer des bitcoins

Vidéo tutoriel sur comment envoyer via Ginger Wallet.

![Vidéo](https://youtu.be/2nf5aAimfhg)

Pour ce faire :
- Appuyez sur le bouton **Envoyer** ;
- entrez l'adresse du destinataire, le montant à envoyer et une étiquette ;
- vérifiez l'aperçu de la transaction et confirmez pour valider l'envoi.  

![screen](assets/fr/31.webp)


## Dépenser des bitcoins

C'est très simple d'acheter et de vendre du Bitcoin avec Ginger Wallet. En seulement quelques étapes, vous pouvez dépenser vos bitcoins.

### Acheter des bitcoins

Les utilisateurs de Ginger Wallet peuvent acheter des bitcoins. 

- Appuyez sur le bouton **Acheter**. Ce bouton reste visible même si le portefeuille est vide.

![screen](assets/fr/32.webp)

- Sélectionnez votre pays, voire votre État (dans certaines régions comme le Canada) avant de procéder à un achat de bitcoins. En fait, lorsque vous cliquez sur la fonction **Acheter** pour la première fois, vous devrez également préciser votre région.

![screen](assets/fr/33.webp)

Appuyez sur **Continuer** pour progresser dans le processus d'achat.

- Saisissez ensuite le montant de bitcoins que vous souhaitez acheter dans le champ dédié. Vous pouvez également choisir la devise de la transaction.

![screen](assets/fr/34.webp)

Chaque devise a une limite d'achat minimale et maximale. Par exemple, en USD, la limite maximale est de 30 000 $.

Si vous avez déjà effectué des achats, vous pouvez consulter l'historique de vos transactions en cliquant sur le bouton **Commandes précédentes**. La liste des transactions passées ainsi que leur statut s'afficheront.

- Choisissez l'offre qui vous convient.

À ce stade, vous verrez une liste de toutes les offres disponibles. Pour chaque offre, vous avez :
 - le nom du fournisseur (1) ;
 - le nombre de bitcoins équivalent au montant précédemment saisi, le mode de paiement et les frais d'achat (2) ;
 - le bouton **Accepter** (3).

![screen](assets/fr/35.webp)

Les frais indiqués dans l'offre ne constituent pas un coût supplémentaire. Ils sont déjà inclus dans le montant total de l'offre.

Le coin supérieur droit de l'écran avec l'intitulé **Tout** vous permet de filtrer les offres par mode de paiement. Votre mode de paiement sélectionné sera défini par défaut, mais peut être modifié à tout moment.

![screen](assets/fr/36.webp)

Si vous trouvez une offre qui vous convient, cliquez sur le bouton **Accepter** pour procéder à l'achat. Vous serez ensuite redirigé vers la page du vendeur, où vous pourrez finaliser la transaction.

### Vendre des bitcoins

Les utilisateurs de Ginger Wallet peuvent vendre du Bitcoin. Le bouton **Vendre** n'est visible que lorsqu'il y a des fonds disponibles dans le portefeuille.

- Cliquez sur **Vendre**.

![screen](assets/fr/37.webp)

- Tout comme avec l'option **Acheter**, lorsque vous utilisez la fonction Vendre pour la première fois, vous devez sélectionner votre pays avant de procéder à une vente de bitcoins.

- Ensuite, vous devez saisir le montant de Bitcoins que vous souhaitez vendre. Vous pouvez saisir ce montant en BTC ou dans une monnaie fiduciaire comme le dollar américain (USD).

- Une fois que vous aurez procédé, vous verrez une liste des offres disponibles. Choisissez donc une offre de vente qui vous convient, puis cliquez sur **Accepter** pour continuer.

- Maintenant, vous devez finaliser la transaction :
	- Après avoir accepté une offre, vous serez redirigé sur la page du fournisseur ;
	- Suivez les instructions sur la page du fournisseur ;
	- À un moment donné, vous recevrez une adresse de destinataire et le montant exact à envoyer ;
	- Retournez ensuite dans Ginger Wallet pour continuer le processus ;
	- Une fois de retour dans Ginger Wallet, une boîte de dialogue apparaîtra, vous permettant de continuer en cliquant sur **Envoyer**.

Cela ouvrira l'écran **Envoyer** avec l'adresse du destinataire et le montant préremplis. Vous pouvez également utiliser le bouton **Envoyer** sur l'écran d'accueil. Bien que vous puissiez envoyer la transaction manuellement, nous vous recommandons de la terminer via la boîte de dialogue pour un processus optimisé.

## Faire un coinjoin sur Ginger Wallet

![Vidéo](https://youtu.be/AJe67RDfB1A)

Protégez la confidentialité de vos bitcoins avec la fonctionnalité **Coinjoin**, intégrée directement dans Ginger Wallet. Le portefeuille utilise **WabiSabi**, un protocole de coinjoins chaumiens conçu pour faciliter des coinjoins plus accessibles et efficaces. 

Il vous revient de choisir la stratégie de coinjoin (automatique ou manuelle) qui vous convient. 

Ginger Coinjoin est prêt à l'emploi dès le téléchargement (aucune étape supplémentaire n'est nécessaire). En automatique, le coinjoin de Ginger s'exécute en arrière-plan pour protéger votre vie privée à chaque transaction. En pratique, le lecteur Coinjoin apparaîtra chaque fois que vous disposerez d’un solde pouvant être anonymisé.

Quant au démarrage du coinjoin en manuel, il se fait facilement (en un clic). Lancez la ronde et attendez que la transaction coinjoin soit construite et confirmée. Vous verrez le score d'anonymisation dans l’interface.

Plusieurs mélanges peuvent être effectués jusqu'à atteindre le niveau d'anonymat voulu. Vous avez aussi la possibilité d'exclure certaines pièces du mélange.

Par défaut, Ginger utilise son propre coordinateur avec tous les paramètres préconfigurés et des frais garantis. Les coinjoins de jetons d'une valeur supérieure à 0,03 BTC entraînent des frais de 0,3 % pour le coordinateur en plus des frais de minage. Les entrées de 0,03 BTC ou moins, ainsi que les remixes, sont exemptées de frais de coordinateur, même après une seule transaction. Par conséquent, un paiement effectué avec des fonds Coinjoin permet à la fois à l'expéditeur et au destinataire de remixer leurs coins sans encourir de frais de coordinateur.

Ginger privilégie les coinjoins avec plus de participants plutôt que des tours plus petits et plus rapides. Les coinjoins plus grands offrent plus d'anonymat, des coûts plus bas et une meilleure efficacité de l'espace de bloc.


## Sécurité et bonnes pratiques 

Le souhait de décentralisation et la préservation de la vie privée exigent l’adoption de plusieurs bonnes pratiques :  
- Conservez toujours votre seedphrase dans un endroit sûr et hors ligne ;  
- En cas de perte de votre ordinateur ou de suspicion d’accès non autorisé, créez immédiatement un nouveau portefeuille. Transférez vos fonds vers ce nouveau portefeuille et supprimez l’ancien ;  
- Utilisez une adresse différente pour chaque réception afin d’éviter la réutilisation d’adresses ;  
- Téléchargez toujours vos applications de portefeuille exclusivement depuis le compte GitHub officiel ou le site web officiel.

Maintenant, vous êtes familier avec l'utilisation de l'application Ginger Wallet pour envoyer, recevoir et dépenser vos bitcoins.

Si ce tutoriel vous a été utile, merci de me laisser un pouce vert ci-dessous. N'hésitez pas à diffuser cet article via vos plateformes de médias sociaux. Merci infiniment !

Je vous suggère également de consulter ce tutoriel sur comment utiliser l'application Liana sur ordinateur pour envoyer et recevoir des bitcoins, ainsi que de mettre en œuvre un plan de succession automatisé.

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

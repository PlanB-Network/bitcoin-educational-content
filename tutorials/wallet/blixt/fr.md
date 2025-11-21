---
name: Blixt Wallet
description: Comment commencer à utiliser un puissant nœud LN sur votre mobile ?
---
![cover](assets/cover.webp)

Ce guide est dédié à tous les nouveaux utilisateurs qui souhaitent commencer à utiliser le Bitcoin Lightning Network (LN) d’une manière GRATUITE, OPEN SOURCE et 100 % NON-CUSTODIAL.

En utilisant [Blixt Wallet](https://blixtwallet.com/), un nœud LN complet sur votre mobile, où que vous soyez.

Si vous n’avez jamais utilisé le Lightning Network, avant de commencer, [merci de lire cette explication simple et imagée du Lightning Network (LN)](https://darth-coin.github.io/beginner/ln-airport-analogy-en.html).

## ASPECTS IMPORTANTS :

- Blixt est un nœud privé, PAS un nœud de routage ! Gardez bien cela en tête : cela signifie que tous les canaux LN dans Blixt seront non annoncés dans le graphe LN (appelés canaux privés). Autrement dit, CE NŒUD NE ROUTERA PAS les paiements des autres à travers le nœud Blixt. Ce nœud Blixt n’est PAS destiné au routage, je le répète. Il sert principalement à gérer vos propres canaux LN et effectuer vos paiements LN de manière privée, quand vous en avez besoin. Ce nœud Blixt doit être en ligne et synchronisé UNIQUEMENT AVANT que vous n’exécutiez vos transactions. C’est pourquoi vous verrez une icône en haut indiquant l’état de la synchronisation. Cela prend seulement quelques instants, selon le temps durant lequel il est resté hors ligne.

- Blixt utilise LND (aezeed) comme backend de portefeuille, donc n’essayez pas d’y importer d’autres types de portefeuilles Bitcoin. [Voici une explication des différents types de graines mnémoniques](https://coldbit.com/what-types-of-mnemonic-seeds-are-used-in-bitcoin/). Et voici [une liste plus complète de tous les types de portefeuilles](https://walletsrecovery.org/). Ainsi, si vous aviez déjà un nœud LND, vous pouvez importer la graine et le fichier backup.channels dans Blixt, [comme expliqué dans ce guide](https://darth-coin.github.io/nodes/shtf-restore-lnd-node-en.html).

- À la fin de ce guide, vous trouverez une section spéciale avec des ["astuces et conseils"](https://darth-coin.github.io/wallets/getting-started-blixt-wallet-en.html#tips).

- Liens importants de Blixt – consultez-les à la fin de ce guide et ajoutez-les à vos favoris.

---

## Blixt - Premier Contact

Alors… la maman de Darth a décidé de commencer à utiliser LN avec Blixt. Décision difficile, mais sage. Blixt est destiné aux personnes averties et à celles qui veulent réellement approfondir l’utilisation du LN.

![blixt](assets/en/01.webp)

Darth prévient sa mère :

"*Maman, si tu commences à utiliser le nœud LN Blixt, tu dois d’abord savoir ce qu’est le Lightning Network et comment il fonctionne, au moins à un niveau basique. [J’ai préparé une liste simple de ressources sur le Lightning Network](https://blixtwallet.github.io/faq#what-is-ln). Lis-les d’abord, s’il te plaît.*"

La maman de Darth a lu les ressources et a fait son premier pas : installer Blixt sur son tout nouvel appareil Android. Blixt est également disponible sur iOS et macOS (bureau). Mais ce n’est pas pour la maman de Darth… Néanmoins, il est recommandé d’utiliser une version récente d’Android, au moins 9 ou 10, pour une meilleure compatibilité et expérience. Faire tourner un nœud LN complet sur un appareil mobile n’est pas une tâche facile et peut prendre de la place (minimum 600 Mo) ainsi que de la mémoire.

Une fois Blixt ouvert, l’écran d’accueil “Welcome” propose plusieurs options :

![blixt](assets/en/02.webp)

En haut à droite, vous verrez 3 points qui activent un menu avec :

- “enable Tor” – permet de démarrer avec le réseau Tor, notamment si vous souhaitez restaurer un ancien nœud LND qui ne fonctionnait qu’avec des pairs Tor.
- “Set Bitcoin node” – permet de connecter directement Blixt à votre propre nœud Bitcoin pour synchroniser les blocs via Neutrino, dès l’écran d’accueil. Cette option est utile si votre connexion internet ou Tor est instable pour se connecter au nœud par défaut (node.blixtwallet.com).
- Bientôt, l’option de langue sera ajoutée ici, afin que l’utilisateur puisse démarrer directement avec une langue confortable. Si vous souhaitez contribuer à ce projet open source avec des traductions dans d’autres langues, [rejoignez ici](https://explore.transifex.com/blixt-wallet/blixt-wallet/).

### OPTION A - Créer un nouveau portefeuille

Si vous choisissez de “créer un nouveau portefeuille”, vous serez redirigé directement vers l’écran principal de Blixt Wallet.

C’est votre “cockpit” et aussi le “Portefeuille LN principal”, donc attention : il affichera uniquement le solde de votre portefeuille LN. Le portefeuille on-chain est affiché séparément (voir C).

![blixt](assets/en/03.webp)

A - Icône d’indicateur de synchronisation des blocs Blixt. C’est l’élément le plus important pour un nœud LN : être synchronisé avec le réseau. Si cette icône est encore active, cela signifie que votre nœud N’EST PAS PRÊT ! Soyez patient, surtout pour la première synchronisation initiale. Cela peut prendre jusqu’à 6-8 minutes, selon votre appareil et votre connexion internet.

Vous pouvez cliquer dessus et voir l’état de la synchronisation :

![blixt](assets/en/04.webp)

Vous pouvez aussi cliquer sur le bouton “Show LND Log” (A) si vous voulez lire plus de détails techniques en temps réel sur le log LND. C’est très utile pour le débogage et pour mieux comprendre le fonctionnement de LN.

B - Ici, vous pouvez accéder à tous les paramètres de Blixt, et ils sont nombreux ! Blixt propose de nombreuses fonctionnalités avancées pour gérer votre nœud LN comme un pro. Toutes ces options sont expliquées en détail sur la “[page des fonctionnalités de Blixt](https://blixtwallet.github.io/features#blixt-options) - Options Menu”.

C - Ici se trouve le menu “Magic Drawer”, [également expliqué en détail ici](https://blixtwallet.github.io/features#blixt-drawer). On y retrouve le “Portefeuille on-chain” (B), les Canaux Lightning (C), les Contacts, l’icône d’état des canaux (A), Keysend (D).

![blixt](assets/en/05.webp)

D - C’est le menu d’aide, avec des liens vers la page FAQ/Guides, le contact développeur, la page Github et le groupe Telegram de support.

E - Indique votre première adresse BTC, où vous pouvez déposer vos premiers sats de test. C’EST OPTIONNEL ! Si vous déposez directement sur cette adresse, un canal LN sera ouvert vers le nœud Blixt. Cela signifie que vos sats déposés apparaîtront dans une autre transaction on-chain, dédiée à l’ouverture de ce canal LN. Vous pouvez vérifier cela dans le portefeuille on-chain de Blixt (voir point C), en cliquant sur le menu TX en haut à droite.

![blixt](assets/en/06.webp)

Comme vous pouvez le voir dans le journal des transactions on-chain, les étapes sont très détaillées, indiquant où vont les sats (dépôt, ouverture, fermeture de canal).

RECOMMANDATION :

Après plusieurs tests, nous avons conclu qu’il est bien plus efficace d’ouvrir des canaux entre 1 et 5 M sats. Les petits canaux se vident rapidement et engendrent des frais proportionnellement plus élevés que les plus gros canaux.

F - Indique le solde de votre portefeuille Lightning principal. Ce n’est PAS le solde total de votre portefeuille Blixt, mais uniquement les sats disponibles dans vos canaux Lightning pour être envoyés. Comme indiqué précédemment, le portefeuille on-chain est distinct. C’est important, car il est utilisé principalement pour ouvrir/fermer des canaux LN.

À ce stade, la maman de Darth a déposé quelques sats dans l’adresse on-chain affichée sur l’écran principal. Il est recommandé, quand vous faites cela, de garder votre application Blixt en ligne et active jusqu’à ce que la transaction BTC soit incluse par les mineurs dans un premier bloc.

Ensuite, il faudra attendre environ 20 à 30 minutes jusqu’à confirmation complète et ouverture du canal. Vous le verrez alors apparaître dans le Magic Drawer – Lightning Channels comme actif. Le petit point coloré en haut du menu, s’il est vert, indique que votre canal LN est en ligne et prêt à envoyer des sats sur LN.

L’adresse et le message de bienvenue affichés disparaîtront. Il n’est plus nécessaire d’ouvrir automatiquement un canal. Vous pouvez aussi désactiver cette option dans le menu Paramètres.

Il est temps de passer à l’étape suivante : tester d’autres options d’ouverture de canaux LN.

Ouvrons maintenant un autre canal avec un autre pair. La communauté Blixt a compilé [une liste de bons nœuds avec lesquels démarrer](https://github.com/hsjoberg/blixt-wallet/issues/1033).

**Procédure d’ouverture d’un canal LN dans Blixt**

C’est très simple, cela ne prend que quelques étapes et un peu de patience :

- Allez sur la [liste de pairs de la communauté Blixt](https://github.com/hsjoberg/blixt-wallet/issues/1033)
- Sélectionnez un nœud et cliquez sur son lien : cela ouvre sa page Amboss
- Cliquez pour afficher le QR code de l’URI du nœud

![blixt](assets/en/07.webp)

Ouvrez Blixt, allez dans le menu du haut – Lightning Channels et cliquez sur le bouton “+”.

![blixt](assets/en/08.webp)

Cliquez maintenant sur l’icône (A) de l’appareil photo pour scanner le QR code de la page Amboss : les détails du nœud seront remplis automatiquement. Ajoutez le montant en sats pour le canal que vous voulez et sélectionnez le taux de frais pour la transaction. Vous pouvez laisser en auto (B) pour une confirmation rapide ou l’ajuster manuellement en déplaçant le curseur. Vous pouvez aussi maintenir le chiffre et le modifier directement.

Ne mettez pas moins de 1 sat/vbyte ! Il est préférable de consulter [les frais dans le mempool](https://mempool.space/) avant d’ouvrir un canal et de choisir un frais adapté.

Cliquez ensuite sur “open channel” et attendez 3 confirmations, ce qui prend environ 30 minutes (1 bloc toutes les 10 minutes).

Une fois confirmé, vous verrez le canal actif dans votre section “Lightning Channels”.

---

## Blixt - Deuxième Contact

D’accord, nous avons maintenant un canal LN avec uniquement de la liquidité SORTANTE. Cela signifie que nous pouvons seulement ENVOYER, mais pas encore RECEVOIR de sats via LN.

![blixt](assets/en/09.webp)

Pourquoi ? As-tu lu les guides indiqués au début ? Non ? Retourne les lire. Il est crucial de comprendre comment fonctionnent les canaux LN.

![blixt](assets/en/10.webp)

Comme on peut le voir dans cet exemple, le canal ouvert avec le premier dépôt n’a pas beaucoup de liquidité ENTRANTE (“Can receive”), mais dispose d’une forte liquidité SORTANTE (“Can send”).

Quelles options s’offrent à vous si vous souhaitez recevoir davantage de sats via LN ?

- Dépenser quelques sats depuis le canal existant. En effet, LN est un réseau de paiement Bitcoin, utilisé principalement pour dépenser vos sats plus rapidement, à moindre coût, de manière privée et simple. LN n’est PAS une méthode de conservation, pour cela vous avez le portefeuille on-chain.

- Échanger quelques sats vers votre portefeuille on-chain, en utilisant un service de submarine swap. De cette façon, vous ne dépensez pas vos sats, mais les transférez à nouveau dans votre portefeuille on-chain. Vous trouverez des méthodes détaillées sur la [page des guides Blixt](https://blixtwallet.github.io/guides).

- Ouvrir un canal ENTRANT auprès d’un fournisseur LSP. Voici une démonstration vidéo expliquant comment utiliser LNBig LSP pour ouvrir un canal entrant. Vous paierez une petite commission pour un canal VIDE (de votre côté), et vous pourrez ainsi recevoir plus de sats dans ce canal. C’est une bonne option si vous êtes un commerçant recevant plus que vous ne dépensez. De même si vous achetez des sats via LN, par exemple avec Robosats ou d’autres exchanges LN.

- Ouvrir un canal Dunder avec le nœud Blixt ou un autre fournisseur Dunder LSP. Un canal Dunder est une méthode simple pour obtenir de la liquidité ENTRANTE, tout en y déposant des sats. C’est également intéressant car le canal sera ouvert avec un [UTXO](https://en.bitcoin.it/wiki/UTXO) externe à votre portefeuille Blixt, ce qui ajoute de la confidentialité. De plus, si vous n’avez pas de sats disponibles sur un portefeuille on-chain pour ouvrir un canal normal, mais que vous en avez dans un autre portefeuille LN, vous pouvez simplement payer depuis cet autre portefeuille LN pour l’ouverture et le dépôt de ce canal Dunder. [Plus de détails sur le fonctionnement de Dunder et sur la manière d’exécuter votre propre serveur ici](https://github.com/hsjoberg/dunder-lsp).

![blixt](assets/en/11.webp)

Voici les étapes pour activer l’ouverture d’un canal Dunder :

- Allez dans Paramètres, section “Experiments”, et activez la case “Enable Dunder LSP”.
- Une fois activé, retournez dans la section “Lightning Network” et vous verrez l’option “Set Dunder LSP Server”. Par défaut, elle est définie sur “https://dunder.blixtwallet.com”, mais vous pouvez la remplacer par tout autre fournisseur Dunder LSP. [Voici une liste de la communauté Blixt](https://github.com/hsjoberg/blixt-wallet/issues/1033) avec des nœuds pouvant fournir des canaux Dunder pour Blixt.
- Allez ensuite à l’écran principal et cliquez sur “Receive”. Puis suivez la procédure [expliquée dans ce guide](https://blixtwallet.github.io/guides#guide-lsp).

OK, une fois le canal Dunder confirmé (quelques minutes), vous aurez 2 canaux LN : un ouvert initialement avec autopilot (canal A) et un autre avec plus de liquidité entrante, ouvert avec Dunder (canal B).

![blixt](assets/en/12.webp)

Parfait, vous pouvez désormais envoyer et recevoir suffisamment de sats via LN !

HAPPY BITCOIN LIGHTNING !

---

## Blixt - Troisième Contact

Souvenez-vous, dans le premier chapitre “Premier Contact”, il y avait 2 options sur l’écran d’accueil :
- [Option A](https://darth-coin.github.io/wallets/getting-started-blixt-wallet-en.html#option-a) – Créer un nouveau portefeuille
- Option B – Restaurer un portefeuille

Voyons maintenant comment restaurer un portefeuille Blixt ou tout autre nœud LND endommagé. C’est un peu plus technique, mais suivez bien. Ce n’est pas si difficile.

### OPTION B - Restaurer un portefeuille

J’ai écrit par le passé un guide dédié sur [la restauration d’un nœud Umbrel corrompu](https://darth-coin.github.io/nodes/shtf-restore-lnd-node-en.html), où j’expliquais aussi la méthode rapide utilisant Blixt, grâce à la graine + le fichier channel.backup d’Umbrel.

J’ai également écrit un guide pour restaurer votre nœud Blixt ou migrer Blixt vers un autre appareil, [ici](https://blixtwallet.github.io/faq#blixt-restore).

![blixt](assets/en/13.webp)

En résumé, le processus se fait en deux étapes simples :

- La case du haut sert à saisir les 24 mots de votre graine (ancien nœud / nœud hors service).
- En bas, deux options permettent d’insérer ou de télécharger le fichier channel.backup sauvegardé depuis votre ancien nœud Blixt/LND. Cela peut être un fichier local (préchargé sur l’appareil) ou un fichier stocké à distance (Google Drive / iCloud). Blixt permet de sauvegarder vos canaux directement dans Google Drive ou iCloud. Voir plus de détails dans la [page des fonctionnalités de Blixt](https://blixtwallet.github.io/features#blixt-options).

À noter : si vous n’aviez aucun canal LN ouvert auparavant, inutile d’importer de fichier channel.backup. Saisissez simplement la graine de 24 mots et cliquez sur “restore”.

N’oubliez pas d’activer Tor dans le menu à 3 points, comme expliqué dans la section Option A. C’est nécessaire si vous n’aviez QUE des pairs Tor, injoignables en clearnet (domaine/IP). Sinon, ce n’est pas utile.

Une autre fonctionnalité utile consiste à définir un nœud Bitcoin spécifique depuis ce menu. Par défaut, la synchronisation se fait via node.blixtwallet.com (mode Neutrino), mais vous pouvez indiquer tout autre nœud Bitcoin supportant Neutrino.

Une fois ces options saisies et “restore” validé, Blixt commence d’abord à synchroniser les blocs via Neutrino, comme expliqué dans “Premier Contact”. Soyez patient et surveillez le processus depuis l’écran principal, en cliquant sur l’icône de synchronisation.

![blixt](assets/en/14.webp)

Dans cet exemple, les blocs Bitcoin sont synchronisés à 100 % (A) et le processus de récupération est en cours (B). Cela signifie que vos anciens canaux LN seront fermés et les fonds restitués dans votre portefeuille on-chain Blixt.

Ce processus prend du temps ! Restez patient et gardez Blixt actif et en ligne. La synchronisation initiale peut durer 6 à 8 minutes, et la fermeture des canaux 10 à 15 minutes. Assurez-vous que votre appareil est bien chargé.

Une fois le processus lancé, vous pouvez vérifier dans le Magic Drawer – Lightning Channels, l’état de chacun de vos anciens canaux. Ils apparaîtront en “pending to close”. Une fois chaque canal fermé, vous verrez la transaction de fermeture dans le portefeuille on-chain (Magic Drawer – Onchain), et pourrez ouvrir le journal des transactions.

![blixt](assets/en/15.webp)

Il est également recommandé d’ajouter vos anciens pairs LN. Pour cela, allez dans le menu Paramètres, section “Lightning Network”, puis sélectionnez “Show Lightning Peers”.

![blixt](assets/en/16.webp)

Dans cette section, vous verrez vos pairs actuels et pourrez en ajouter d’autres, de préférence ceux avec lesquels vous aviez déjà des canaux. Rendez-vous sur [Amboss](https://amboss.space/), recherchez l’alias ou l’ID de vos pairs, puis scannez leur URI de nœud.

![blixt](assets/en/17.webp)

Sur cette image, on distingue 3 éléments :

A – l’adresse clearnet du nœud (domaine/IP)  
B – l’adresse onion du nœud (Tor .onion)  
C – le QR code à scanner avec la caméra de Blixt ou à copier

Cet URI de nœud doit être ajouté à votre liste de pairs. Retenez bien : l’alias ou l’ID seul ne suffisent pas.

Vous pouvez ensuite aller dans le Magic Drawer (menu en haut à gauche) – Lightning Channels, et vérifier à quelle hauteur de bloc vos fonds seront restitués sur votre adresse on-chain.

![blixt](assets/en/18.webp)

Dans cet exemple, le bloc 764272 est celui où les fonds redeviendront utilisables sur votre adresse Bitcoin on-chain. Cela peut prendre jusqu’à 144 blocs après la première confirmation pour être libéré. [Vérifiez cela sur le mempool](https://mempool.space/).

Et voilà. Il ne vous reste qu’à patienter jusqu’à la fermeture complète des canaux et la restitution des fonds dans votre portefeuille on-chain.

👉 **Méthode secrète de restauration :**

Il existe une autre méthode pour restaurer un nœud Blixt LND sans fermer les canaux. Elle est cachée pour éviter aux débutants de faire des erreurs, car elle est réservée à ceux qui savent exactement ce qu’ils font.

En cas de migration d’un nœud Blixt actif vers un nouvel appareil, sans fermer les canaux existants, voici la procédure :

- Assurez-vous d’avoir sauvegardé la graine de 24 mots (aezeed).  
- Sur l’ancien appareil, allez dans “Paramètres” – section debug – “Compact LND database”. Étape optionnelle mais recommandée pour réduire la taille du fichier channel.db.  
- Une fois redémarré, changez votre alias régulier en “Hampus”. Cela active les options cachées réservées aux utilisateurs avancés.  
- Descendez dans la section “Debug” : une nouvelle option “Export channel.db file” apparaît. ATTENTION : cette action désactivera le nœud LN sur l’ancien appareil et exportera toute la base de données (channel.db) prête à être importée sur le nouveau.  
- Le fichier est enregistré dans un dossier désigné (Documents ou Téléchargements). Transférez-le tel quel sur le nouvel appareil, par exemple via [LocalSend](https://github.com/localsend/localsend).  
- Gardez impérativement l’ancien Blixt ÉTEINT. NE LE ROUVREZ PLUS !  
- Sur le nouvel appareil, lancez Blixt et choisissez “Restore wallet” à l’écran d’accueil.  
- Sur le bouton “Select SCB file”, faites un appui long (et non un simple clic) pour sélectionner un fichier channel.db. Un simple clic utiliserait un fichier SCB par défaut (qui ferme les canaux), ce qui ne fonctionne pas ici.  
- Saisissez la graine de 24 mots et cliquez sur “Restore”.  
- Blixt démarre la synchronisation avec Neutrino. Surveillez les logs.  
- GARDEZ Blixt OUVERT ! Ne laissez pas l’appareil passer en veille, sinon la synchro sera interrompue. Attendez quelques minutes.  
- Une fois la synchro initiale terminée, Blixt rescannera vos anciennes adresses et vos canaux seront restaurés et en ligne.  
- À noter : l’historique des paiements et contacts n’est pas restauré (du moins pas encore). Mais ce n’est pas critique.

Et voilà ! Vous avez un nœud Blixt LN complètement restauré. Cette méthode fonctionne aussi avec d’autres sauvegardes LND (Umbrel, Raspiblitz, etc.) si vous avez correctement sauvegardé le fichier channel.db. Blixt peut littéralement sauver n’importe quel nœud LND hors service.

---
## Blixt - Quatrième Contact

Ce chapitre concerne la personnalisation et une meilleure connaissance de votre nœud Blixt. Je ne vais pas décrire toutes les fonctionnalités disponibles, elles sont trop nombreuses et déjà expliquées dans la [page des fonctionnalités de Blixt](https://blixtwallet.github.io/features).

Je vais néanmoins mettre en avant certaines options essentielles pour aller plus loin et profiter pleinement de votre expérience Blixt.

### A - Name (NameDesc)

![blixt](assets/en/19.webp)

[Le NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) est un standard pour transmettre le "nom de l’expéditeur" dans les factures BOLT11.

Cela peut être n’importe quel nom et être modifié à tout moment.

Cette option est très utile dans divers cas, par exemple lorsque vous souhaitez envoyer un nom avec la description de la facture. Le destinataire pourra alors savoir de qui proviennent les sats. C’est entièrement optionnel et, lors de l’écran de paiement, l’utilisateur doit cocher la case pour envoyer son alias.

Voici un exemple d’utilisation avec [chat.blixtwallet.com](https://chat.blixtwallet.com/)

![blixt](assets/en/20.webp)

Autre exemple avec une application de portefeuille compatible NameDesc :

![blixt](assets/en/21.webp)

### B - Lightning Box

Depuis la version v0.6.9-420 [récemment publiée](https://github.com/hsjoberg/blixt-wallet/releases/tag/v0.6.9-420), Blixt a introduit une nouvelle fonctionnalité puissante : l’adresse Lightning dans Blixt.

Cette fonctionnalité est optionnelle et désactivée par défaut.

Pour l’instant, le serveur LN Box par défaut est opéré par Blixt et propose une adresse LN de type @blixtwallet.com. Mais n’importe qui possédant un nœud LND public peut exécuter un serveur Lightning Box et proposer des adresses LN personnalisées, en self-custody.

Actuellement, le serveur Blixt ne fait que relayer les paiements envoyés aux adresses @blixtwallet.com vers les utilisateurs Blixt qui ont configuré leur adresse. Les utilisateurs doivent mettre leur nœud Blixt en “mode persistant” afin de recevoir ces paiements.

Voir la vidéo dans les notes de version pour apprendre à configurer votre adresse LN dans Blixt.

Cette adresse LN intégrée dans Blixt Wallet fonctionne comme un chat instantané sur LN, amusant et rapide, avec support du [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (ajout d’un alias à un paiement). Vous pouvez ajouter dans vos contacts toutes vos adresses LN fréquentes et les utiliser facilement pour chatter. Blixt peut même être considéré comme une application de chat LN complète 😂.

Autre atout : le support total du LUD-18 (également supporté par [Stacker.News](https://stacker.news/r/DarthCoin) et d’autres).

![blixt](assets/en/22.webp)

Comme on le voit ci-dessus, un paiement envoyé depuis un compte Stacker News affiche le logo, l’adresse LN et le message. Depuis Blixt, vous pouvez faire de même : attacher votre adresse LN Blixt, ou simplement ajouter l’alias configuré dans vos paramètres, voire les deux.

Cette option issue du LUD-18 peut aussi être utile pour des services d’abonnement : l’utilisateur envoie un alias (ce n’est PAS l’alias du nœud ni son vrai nom), et en fonction de celui-ci, il peut être enregistré, recevoir un message spécifique, etc. Attacher un alias ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md)) + un commentaire ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) à un paiement LN ouvre de nombreux cas d’usage.

Voici le code source de [Lightning Box](https://github.com/hsjoberg/lightning-box) si vous souhaitez l’héberger pour vous, votre famille ou vos amis, sur votre propre nœud.

Vous pouvez aussi exécuter le [serveur LSP Dunder](https://github.com/hsjoberg/dunder-lsp) pour les nœuds mobiles Blixt et fournir de la liquidité aux utilisateurs Blixt si vous possédez un bon nœud LN public (uniquement LND).

### C - Sauvegarde des canaux LN et de la graine

C’est une fonctionnalité très importante !

Après chaque ouverture ou fermeture de canal LN, vous devez faire une sauvegarde. Elle peut être effectuée manuellement (en enregistrant un petit fichier sur l’appareil, généralement dans le dossier “Téléchargements”) ou via un compte Google Drive / iCloud.

![blixt](assets/en/23.webp)

Allez dans Paramètres de Blixt – section Wallet. Vous y trouverez toutes les options nécessaires à la sauvegarde de vos données importantes :

- “Show mnemonic” – affiche la graine de 24 mots afin de la noter.  
- “Remove mnemonic from device” – optionnelle, uniquement si vous souhaitez supprimer la graine de l’appareil. Cela ne supprime pas le portefeuille, uniquement la graine. ATTENTION : irrécupérable si vous ne l’avez pas notée au préalable.  
- “Export channel backup” – enregistre un petit fichier local (dossier Téléchargements), à déplacer ensuite hors de l’appareil pour le conserver en sécurité.  
- “Verify channel backup” – permet de vérifier l’intégrité d’une sauvegarde distante (Google Drive ou iCloud).  
- “Google drive channel backup” – sauvegarde dans votre Google Drive personnel. Le fichier est chiffré et stocké dans un espace séparé de vos fichiers habituels. Il est inutilisable sans la graine, donc aucun risque de vol direct.  

Recommandations :

- Utilisez un gestionnaire de mots de passe pour stocker en sécurité votre graine et votre fichier de sauvegarde (KeePass ou Bitwarden, par exemple).  
- FAITES UNE SAUVEGARDE À CHAQUE OUVERTURE OU FERMETURE DE CANAL. Le fichier est mis à jour avec l’état des canaux. Inutile d’en faire après chaque transaction LN : la sauvegarde ne stocke que l’état des canaux.  

![blixt](assets/en/24.webp)

---

## Blixt - Astuces et Conseils

### CAS 1 - PROBLÈMES DE SYNCHRONISATION

"_Mon Blixt ne se synchronise pas… Mon Blixt n’affiche pas le solde… Mon Blixt ne peut pas ouvrir de canaux… J’ai essayé de le restaurer sur un autre appareil… etc_"

Tous ces problèmes proviennent du fait que VOTRE APPAREIL NE SE SYNCHRONISE PAS CORRECTEMENT. Comprenez bien cet aspect : Blixt est un nœud LND mobile qui utilise Neutrino pour synchroniser / lire les blocs.

- Explication simple : [Bitcoin Magazine](https://bitcoinmagazine.com/technical/why-bitcoin-wallets-need-block-filters)  
- Ressources techniques : [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)  
- Guide pour activer Neutrino sur votre propre nœud domestique et servir des filtres à vos nœuds mobiles : [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core)  

RAPPEL : Utiliser Neutrino en clearnet est totalement sûr, votre IP ou xpub ne sont pas divulgués. Vous lisez simplement les blocs d’un nœud distant avec Neutrino. Tout le reste se fait en local.

Il n’est donc PAS NÉCESSAIRE d’utiliser Tor. Tor ajoute une forte latence à la synchronisation et rend Blixt instable. Si vous tenez à l’utiliser, soyez conscient des contraintes : bonne connexion et beaucoup de patience. Même chose avec un VPN : attention à la latence.

Vous pouvez tester la latence d’un serveur Neutrino en le pingant depuis un PC ou un mobile.

![blixt](assets/en/25.webp)

Exemple de ping vers europe.blixtwallet.com : temps de réponse moyen 50 ms et TTL de 51. Ces valeurs doivent rester stables. Si la latence dépasse 100-150 ms, la synchronisation échouera ou vos pairs pourront fermer vos canaux !

Sans synchronisation correcte, vous ne verrez pas votre solde, vos canaux LN ne seront pas opérationnels. Peu importe la vitesse de téléchargement, ce qui compte est le temps de réponse et le TTL.

Cas fréquent en Amérique latine : pings supérieurs à 200 ms, qui perturbent totalement la synchro.

Solutions :

- ne pas utiliser Blixt avec Tor  
- utiliser un VPN proche de votre région et surveiller le ping  
- choisir ses pairs Neutrino avec soin, voici une liste de serveurs publics fiables :

```txt
US :
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network

EU :
europe.blixtwallet.com (Allemagne)

Asie :
sg.lnolymp.us
asia.blixtwallet.com
```

Vous pouvez aussi consulter la [liste des nœuds Neutrino BIP157](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS) et en choisir un proche de chez vous.

Encore mieux : utiliser un nœud communautaire local (ami, groupe Bitcoin), configuré pour proposer une connexion Neutrino. [Instructions ici](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core). Leur nœud n’est pas affecté, il suffit d’une IP publique.

### CAS 2 - SYNCHRO INACHEVÉE

"*Mon Blixt a une bonne connexion Neutrino mais reste bloqué en synchro.*"

#### Serveur de temps

Certains appareils anciens ne sont pas correctement synchronisés avec un serveur de temps. Résultat : les blocs récents ne correspondent pas à l’heure locale. Le log lnd indique alors “block time stamp is far from future” ou “header don't pass sanity check”.

Solution rapide : corrigez la date et l’heure de l’appareil, puis redémarrez Blixt.

#### Espace disque insuffisant

Sur un appareil ancien, la mémoire saturée peut bloquer la synchro. Plus vous utilisez Blixt, plus les fichiers Neutrino et channel.db grossissent.

Solution rapide : allez dans Options Blixt – Debug – “stop LND and delete neutrino files”. L’app redémarre et repart sur une synchro propre. Cela ne supprime pas vos fonds ni canaux, mais peut déclencher un rescannage, donc prévoyez du temps.

Ensuite, vérifiez la taille occupée dans les infos Android. Si > 400-500 Mo, compactez les fichiers lnd. Options – Debug – “Compact DB LND”. Le compactage se fait au redémarrage.

#### Mode persistant

Si vous n’ouvrez pas Blixt depuis longtemps, la synchro est très en retard. Soyez patient et regardez la roue en haut. Dans Options – Node Info, vérifiez que “synced to chain” et “synced to graph” sont à “true”. Sinon, Blixt ne fonctionnera pas correctement.

Solution : activez le “mode persistant” dans Options – Experiments. Lnd restera actif même si vous changez d’app ou fermez Blixt. Idéal si vous utilisez Blixt plusieurs fois dans la journée.

### CAS 3 - MIGRATION VERS UN AUTRE APPAREIL

J’ai déjà écrit un guide détaillé sur la [page FAQ](https://blixtwallet.github.io/faq#blixt-restore), avec deux méthodes : rapide (fermeture coopérative) et lente (fermeture forcée si ancien appareil mort).

Rappels :

**toujours sauvegarder vos canaux (SCB) après chaque ouverture/fermeture**
* ne pas conserver d’anciens fichiers SCB, inutiles et dangereux (risque de pénalité)
* sauvegarder le fichier SCB (.bin chiffré) hors de l’appareil (PC, autre mobile)
* sauvegarder la graine dans un gestionnaire de mots de passe hors ligne

Méthode secrète : migration sans fermer les canaux existants. Pour cela, relisez la section “Troisième Contact – Restaurer un portefeuille”.

Attention : réservé aux utilisateurs avancés ! À réaliser de préférence avec assistance des développeurs Blixt.

### CAS 4 - AVEC QUELS PAIRS OUVRIR DES CANAUX ?

Comme expliqué dans la [page des guides Blixt](https://blixtwallet.github.io/guides), il y a de nombreuses façons d’ouvrir des canaux avec ce nœud LND mobile. Points essentiels :

*ouvrir avec des LSP connus et des pairs validés par la communauté.* [Liste ici](https://github.com/hsjoberg/blixt-wallet/issues/1033)
* ne pas ouvrir avec des nœuds Tor aléatoires : problèmes garantis, routes mauvaises
*inutile d'ouvrir une dizaine de petits canaux : 2 à 4 suffisent, mais avec un bon montant*
* éviter les canaux < 200k sats : peu utiles sur mobile
*tirer parti des LSPs offrant des canaux entrants ou "just in time" (JIT) : vous payez l'ouverture avec des fonds LN existants, idéal pour préparer un canal plus gros*

Pour plus de détails, voir :

* [Guide DarthCoin sur la gestion de la liquidité LN privée](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html)
* [Explications supplémentaires sur Stacker News](https://stacker.news/items/679242/r/DarthCoin)

---

## Conclusion

Blixt propose encore de nombreuses fonctionnalités que je vous laisse découvrir et tester.

Cette application est largement sous-estimée, car non financée par des VCs. Elle est construite par la communauté, avec passion et amour pour Bitcoin et Lightning Network.

Ce nœud LN mobile est un outil très puissant entre les mains des utilisateurs qui savent bien l’exploiter. Imaginez : vous marchez dans le monde entier avec un nœud LN complet dans votre poche, et personne ne le sait.

Et ce n’est pas tout : les autres fonctionnalités de Blixt surpassent celles de nombreux portefeuilles.

Liens utiles autour de Blixt :

* [Site officiel](https://blixtwallet.com/)
* [Dépôt Github](https://github.com/hsjoberg/blixt-wallet/)
* [Page des fonctionnalités](https://blixtwallet.github.io/features) – description de chaque option
* [FAQ Blixt](https://blixtwallet.github.io/faq) – questions/réponses et dépannage
* [Guides Blixt](https://blixtwallet.github.io/guides) – démos, tutos vidéo, cas d’usage
* Télécharger : [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK](https://github.com/hsjoberg/blixt-wallet/releases)
* [Support Telegram](https://t.me/blixtwallet)
* [Twitter](https://twitter.com/BlixtWallet)
* [Page Geyser](https://geyser.fund/project/blixt) – soutenir le projet en sats
* [Chat LNURL Blixt](https://chat.blixtwallet.com/)
* [Vidéo promo Blixt](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
[Calendrier Blixt Girls](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6)
* [Flyer A4 multilingue](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer)
* [Démo web de Blixt](https://blixt-wallet-git-master-hsjoberg.vercel.app/)

---

**DISCLAIMER :**

*Je ne suis pas payé ni soutenu par les développeurs de cette app. J’ai rédigé ce guide car l’intérêt pour Blixt augmente et les nouveaux utilisateurs ne savent pas toujours comment commencer. Cela aide aussi Hampus (le dev principal) pour la documentation.*

*Je n’ai aucun autre intérêt que de contribuer à l’adoption de Bitcoin et LN. C’est la seule voie !*


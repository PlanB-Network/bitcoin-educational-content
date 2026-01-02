---
name: KaleidoSwap
description: Guide avancé des échanges d'actifs RGB sur Lightning Network avec KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap est une application de bureau sophistiquée à code source ouvert qui comble le fossé entre le protocole RGB et le Lightning Network. Elle sert d'interface complète pour gérer les nœuds RGB Lightning, interagir avec les fournisseurs de services RGB Lightning (LSP) via la spécification LSPS1 et exécuter des échanges atomiques d'actifs RGB.


KaleidoSwap est une solution non privative qui permet aux utilisateurs de garder le contrôle total de leurs clés et de leurs données. En s'appuyant sur le paradigme de validation côté client de RGB, il permet de créer des contrats intelligents privés et évolutifs au-dessus de Bitcoin. Ce tutoriel plonge dans les fonctionnalités avancées de KaleidoSwap, en vous guidant à travers les subtilités de la gestion du UTXO " coloré ", de la liquidité des canaux pour des actifs spécifiques et du modèle d'échange preneur-meneur, afin de vous permettre d'utiliser pleinement ce puissant protocole d'échange décentralisé.


## Installation


KaleidoSwap fournit des binaires préconstruits pour les principaux systèmes d'exploitation, mais pour les utilisateurs avancés, la construction à partir des sources garantit l'exécution du code le plus récent avec vos configurations spécifiques.


### Télécharger les binaires


Vous pouvez télécharger la dernière version pour votre système d'exploitation à partir du [site officiel] (https://kaleidoswap.com/) ou de la [page des versions de GitHub] (https://github.com/kaleidoswap/desktop-app/releases).


### Méthodes d'installation


1.  **Windows** : Téléchargez le programme d'installation `.exe` et exécutez-le.

2.  **macOS** : Téléchargez le fichier `.dmg`, ouvrez-le et glissez KaleidoSwap dans votre dossier Applications.

3.  **Linux** : Téléchargez le fichier `.AppImage` ou `.deb` et installez-le.



## Options de configuration des nœuds


Lorsque vous lancez KaleidoSwap pour la première fois, l'écran de connexion** s'affiche. Il s'agit de la première étape de la configuration de votre environnement.


![Node Selection Screen](assets/en/01.webp)


Vous devez choisir comment vous connecter au RGB Lightning Network. Ce choix a un impact sur votre niveau de contrôle et de confidentialité.


### Option 1 : Nœud local (recommandé pour l'autodétention)


**Pour un contrôle total et une confidentialité totale**, exécutez un nœud directement sur votre machine, voir les avantages ci-dessous :


- Autonome** : Vous détenez les clés. Aucun tiers ne peut geler vos fonds ou censurer vos transactions.
- Confidentialité** : Vos données restent sur votre appareil.
- Indépendance** : Pas de dépendance à l'égard de prestataires de services externes.


Si vous sélectionnez **Nœud local**, vous accéderez à l'écran de configuration où vous pourrez créer un nouveau wallet ou restaurer un nœud existant.


![Local Node Setup Screen](assets/en/02.webp)


### Option 2 : Nœud distant


Se connecter à un RGB Lightning Node distant (hébergé soi-même sur un VPS ou un fournisseur hébergé).


- Avantages** : Pas d'utilisation de ressources locales, disponibilité 24/7.
- Compromis** : Nécessite de faire confiance à l'hôte ou de gérer un serveur distant.


![Remote Node Setup Screen](assets/en/03.webp)


**Nous vous recommandons vivement de gérer votre propre nœud, soit localement (option 1), soit en hébergeant vous-même un nœud distant, afin de tirer pleinement parti des propriétés de résistance à la censure de Bitcoin et RGB.


## Création d'une Wallet


KaleidoSwap gère les actifs Bitcoin et RGB. Le processus de création de la wallet initialise une base de données de clés qui sécurise vos fonds on-chain et les états de votre canal Lightning.


Voici la procédure détaillée :

1. Ouvrez KaleidoSwap et sélectionnez **Nœud local**.

2. Cliquez sur **Créer un nouveau Wallet**.

3. **Configuration du compte** : Entrez un **nom de compte** et sélectionnez le **réseau** (par exemple, Bitcoin Mainnet, Testnet, Signet).

4. **Configuration avancée** (optionnelle) : Si vous êtes un utilisateur expérimenté, vous pouvez configurer des points de terminaison RPC personnalisés, des URL d'indexation ou des paramètres de proxy sous "Paramètres avancés".

5. Cliquez sur **Continuer**.

6. **Mot de passe** : Définissez un mot de passe fort pour crypter localement votre fichier wallet.

7. **Phrase de récupération** : Notez votre phrase seed et conservez-la en lieu sûr.


    - Critique** : Cette phrase est nécessaire pour récupérer vos fonds on-chain et l'identité du nœud.
    - Avertissement** : **Les états des canaux de foudre ne peuvent pas être entièrement récupérés à partir de la seed seule**. Vous devez également effectuer des sauvegardes statiques des canaux (SCB) pour récupérer les fonds bloqués dans les canaux.


![Wallet Creation Screen](assets/en/04.webp)



## Aperçu du tableau de bord


Une fois votre wallet créé, vous serez dirigé vers le **tableau de bord** principal.


![KaleidoSwap Dashboard](assets/en/05.webp)


remarque : la capture d'écran ci-dessus montre une wallet qui a déjà été financée et qui dispose de canaux actifs. Une nouvelle wallet affichera un solde nul et aucun canal actif tant que vous ne l'aurez pas financée


## Financement de votre Wallet


Pour opérer avec des actifs RGB, vous devez financer votre wallet. KaleidoSwap permet de déposer des actifs Bitcoin et RGB via des transactions on-chain ou Lightning Network.


### Dépôt de la Bitcoin


1. Cliquez sur **Dépôt** dans le menu Actions rapides.

2. Sélectionnez **BTC** dans la liste des actifs.


![Select BTC Asset](assets/en/06.webp)


3. Choisissez votre méthode de dépôt : **On-chain** ou **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- En chaîne** : Scannez le code QR ou copiez l'adresse pour envoyer un Bitcoin à partir d'un autre wallet.
- Éclair** : Générer une facture pour le montant souhaité.


![BTC On-chain Deposit](assets/en/08.webp)


### Dépôt des actifs RGB et des UTXO colorés


Pour recevoir des actifs RGB (comme l'USDT), vous avez besoin d'UTXO spécifiques disponibles pour être "colorés" (assignés à un actif).


1. Cliquez sur **Dépôt** et sélectionnez l'actif RGB (par exemple, USDT). **Important** : Si c'est la **première fois** que votre nœud reçoit cet actif spécifique, **laissez le champ ID de l'actif vide**. La saisie d'un identifiant pour un actif inconnu entraînera une erreur car le nœud ne le reconnaît pas encore.

2. Choisissez **On-chain** ou **Lightning**.


![USDT Deposit Options](assets/en/09.webp)


#### Modes de réception en chaîne : Témoin ou aveugle


Lors de la réception d'actifs RGB on-chain, vous disposez de deux modes de confidentialité :



- Réception à l'aveugle (recommandé pour la confidentialité)** : Vous fournissez une blinded UTXO à l'expéditeur. Vous demandez à l'expéditeur d'envoyer des actifs à une UTXO existante que vous possédez, mais vous obscurcissez l'identifiant réel de la UTXO. Cette méthode offre une meilleure protection de la vie privée.
- Recevoir un témoin** : Vous fournissez une adresse Bitcoin standard. Vous demandez à l'expéditeur de créer une *nouvelle* UTXO pour vous en envoyant les actifs à cette adresse. Cela permet aux actifs de la RGB d'être rattachés directement à la nouvelle UTXO créée par la transaction.


#### Dépôt éclair


Pour les dépôts Lightning, il suffit d'établir une generate facture. L'actif RGB vous sera acheminé par vos canaux ouverts.


![USDT Lightning Invoice](assets/en/10.webp)



## Ouvrir des canaux avec les actifs RGB


Pour acheminer les actifs RGB sur le Lightning Network, vous avez besoin d'un canal avec suffisamment de liquidités et d'allocation d'actifs. La façon la plus simple de commencer est d'**acheter un canal** auprès d'un LSP (Lightning Service Provider).


### Achat d'une chaîne de Kaleido LSP


1. Allez dans l'onglet **Canaux**. Vous verrez les options "Ouvrir un canal" (manuel) ou "Acheter un canal" (LSP).

2. Cliquez sur **Canal d'achat**.


![Channels Dashboard](assets/en/11.webp)


3. **Se connecter au FSL** : L'application se connectera au LSP par défaut de Kaleido. Ce fournisseur offre des liquidités entrantes et prend en charge le routage des actifs RGB.


![Connect to LSP](assets/en/12.webp)


4. **Configurer le canal** :


    - Capacité** : Sélectionnez la capacité totale Bitcoin pour le canal.
    - Allocation RGB** : Choisissez l'actif RGB (par exemple, USDT) que vous voulez pouvoir recevoir ou envoyer. Le FSL s'assurera que le canal est configuré pour prendre en charge ce bien.


![Configure Channel](assets/en/13.webp)



    - Allocation RGB** : Choisissez l'actif RGB (par exemple, USDT) que vous souhaitez pouvoir recevoir ou envoyer. Le FSL s'assurera que le canal est configuré pour prendre en charge ce bien.


![RGB Allocation](assets/en/14.webp)


5.  **Paiement** : Vous devez payer une redevance au FSL pour l'ouverture du canal et la fourniture de liquidités. Vous pouvez payer en utilisant **Lightning** ou **On-chain** Bitcoin. Le paiement peut être effectué à partir de votre wallet KaleidoSwap interne ou d'une wallet externe.


![Complete Payment](assets/en/15.webp)


6. Une fois le paiement confirmé, le FSL lance la transaction d'ouverture du canal. L'écran **Order Completed** s'affiche.


![Order Completed](assets/en/16.webp)


7. Après confirmation sur la blockchain, votre canal sera actif et prêt pour les transferts RGB.



## Commerce : Modèle preneur-meneur


Le moteur de négociation de KaleidoSwap fonctionne sur un modèle **preneur-faiseur**. Vous pouvez échanger des actifs manuellement avec un pair ou utiliser un teneur de marché (LSP).


### Échanger avec un teneur de marché (LSP)


C'est la façon la plus courante de négocier. Vous agissez en tant que **preneur**, en exécutant des ordres contre la liquidité disponible fournie par le PSL (**preneur**).


1. Accédez à l'onglet **Trade** et sélectionnez **Market Maker**.

2. **Enter Amount** : Saisissez le montant de Bitcoin que vous souhaitez envoyer (ou l'actif que vous souhaitez recevoir). L'interface affichera le taux de change et les frais estimés.


![Market Maker Swap](assets/en/17.webp)


3. **Confirmez l'échange** : Examinez les détails, y compris le taux de change et le montant exact que vous recevrez. Cliquez sur **Confirmer l'échange**.


![Confirm Swap](assets/en/18.webp)


4. **Traitement** : La permutation est exécutée de manière atomique sur le Lightning Network. Vous verrez un écran d'état indiquant que la permutation est en attente.


![Swap Pending](assets/en/19.webp)


5. **Succès** : Une fois les HTLC réglés, le swap est terminé et les actifs sont dans votre canal.


![Swap Success](assets/en/20.webp)



## Développeur API


Pour les développeurs qui utilisent KaleidoSwap, l'application expose un API qui prend en charge :



- RGB LSPS1** : Pour les services de liquidité automatisés.
- Swap API** : Pour le trading programmatique et le market making.
- WebSocket** : Pour les abonnements aux données de marché en temps réel.


Consulter la [documentation API] (https://docs.kaleidoswap.com/api/introduction) pour connaître l'ensemble des points finaux et des spécifications.


## Conclusion


KaleidoSwap vous permet de tirer parti de la confidentialité et de l'évolutivité des actifs RGB sur le Lightning Network. En comprenant les UTXOs colorés et l'allocation des actifs des canaux, vous pouvez utiliser pleinement ce puissant protocole d'échange décentralisé.
---
name: Valet Bitcoin
description: Valet met dans votre poche le nœud Lightning non gardien
---

![cover_valet](assets/cover.webp)



## Introduction


Valet est un véhicule léger, autodétenu, Bitcoin et Lightning wallet qui offre un processus d'embarquement facile et pratique pour les débutants. Il a été spécialement conçu pour servir les communautés Bitcoin et les économies circulaires, en particulier dans les zones reculées.


Il s'agit d'un fork du **Simple Bitcoin Wallet (SBW)**, avec une fonctionnalité avancée de canal Lightning hébergé appelée **Fiat Channels**, conçue pour permettre à quiconque d'accepter des paiements Lightning sans risques de volatilité.


Valet n'est actuellement disponible que pour les appareils Android et peut être téléchargé et installé à partir de plusieurs magasins d'applications libres. Cependant, Valet n'est **pas** hébergé sur le **Google Play Store** en raison des préoccupations des développeurs en matière de confidentialité et de KYC.



## Télécharger et installer Valet


Valet peut être téléchargé en tant que fichier APK depuis la page GitHub de Standard Sats. [Standard Sats] (https://standardsats.github.io/) est la société qui a développé Valet.


👉 Pour télécharger Valet, visitez le Standard Sats [page GitHub] (https://github.com/standardsats/valet/releases), et localisez la **dernière** version (c'est souvent la première).


👉 Allez dans **Assets** et cliquez sur le fichier avec seulement une extension **.apk**. Votre téléchargement démarrera automatiquement.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 Une fois le téléchargement terminé, allez dans le **Gestionnaire de fichiers** > **Téléchargements** de votre appareil, et sélectionnez le fichier apk Valet.


![Select_valet_apk](assets/en/002.webp)


👉 Installez-la, et dans quelques secondes, votre application sera prête et apparaîtra sur votre écran d'accueil.


![valet_icon_on_homescreen](assets/en/003.webp)


Vous pouvez également télécharger Valet à partir de la boutique d'applications **F-Droid**. Si vous n'avez pas l'application F-Droid sur votre appareil, vous pouvez la télécharger et l'installer [ici] (https://f-droid.org/en/).


👉 Sur votre écran d'accueil, ouvrez F-Droid et recherchez **Valet**. Sélectionnez la première option avec une **icône violette et blanche** parmi les deux options qui apparaîtront, et cliquez sur **Télécharger**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


après le téléchargement, cliquez sur **Installer** et suivez les instructions à l'écran. Une fois l'installation terminée, vous pouvez lancer Valet à partir de F-Droid en cliquant sur **Ouvrir**, ou le lancer à partir de l'écran d'accueil de votre appareil.



## Création d'une Bitcoin Wallet


Vous pouvez installer un Bitcoin wallet sur Valet en deux étapes simples.


👉 Lancez Valet depuis l'écran d'accueil de votre appareil ou depuis l'application F-Droid. Un écran de configuration wallet s'affiche, avec deux options : **Créer un nouveau Wallet** et **Restaurer un Wallet existant**.


sélectionnez **Créer un nouveau Wallet**, et instantanément, un nouveau wallet sera créé, et vous serez redirigé vers la page d'accueil.


![set_up_a\_new_wallet](assets/en/006.webp)



## Sauvegarder votre phrase de recherche


👉 Sur la page d'accueil du wallet, cliquez sur la **carte Green** qui porte l'inscription **"Tapotez pour enregistrer la phrase de récupération du wallet au cas où vous perdriez ou remplaceriez votre appareil "**


![seed_phrase_green_card](assets/en/007.webp)


👉 Une série de 12 mots anglais s'affiche. Notez-les sur un papier, dans l'ordre de 1 à 12, et conservez-les précieusement.


![the_seed_phrase](assets/en/008.webp)


### Prêtez attention à ⚠️ :


Faites attention aux éléments suivants :


- Comme vous le savez déjà, Valet est une wallet autodétenue, de sorte que votre phrase seed est le seul moyen de récupérer votre Wallet.
- Si vous perdez votre phrase seed, vous n'aurez **jamais** accès à votre wallet.
- Si quelqu'un obtient votre phrase seed, il peut irrémédiablement voler tous vos Bitcoin.


Vous devez donc écrire votre phrase seed de 12 mots et la conserver dans un endroit sûr. Vous ne devez jamais faire de capture d'écran, l'enregistrer en tant que brouillon dans votre courrier électronique ou la sauvegarder sur un appareil électronique connecté à l'internet.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Réception et envoi de Bitcoin sur Valet


Valet est un wallet autodétenu, capable d'utiliser à la fois le on-chain et le Lightning Bitcoin. Cela signifie que vous pouvez recevoir et envoyer des Bitcoin à partir de Valet, soit par l'intermédiaire d'une **chaîne**, soit par l'intermédiaire d'un **Lightning Network**.


Cependant, pour pouvoir recevoir ou envoyer des Bitcoin via Lightning, vous devez créer un canal Lightning en utilisant vos on-chain Bitcoin comme Liquidity. Vous pouvez également acheter de la liquidité pour le canal Lightning auprès de vendeurs.



## Génération d'une chaîne Bitcoin Address


Pour recevoir la Bitcoin par le biais de la on-chain, vous devez générer une adresse Bitcoin.


👉 Sur la page d'accueil de wallet, vous verrez une **carte orange** et une **carte violette**, respectivement intitulées **Bitcoin** et **Lightning**.


👉 Cliquez sur la carte orange intitulée **Bitcoin**. Vous serez redirigé vers un écran affichant une adresse Bitcoin.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Vous pouvez **copier** l'adresse et l'envoyer à la personne qui vous envoie des Bitcoin, ou cliquer sur le bouton **partager** pour envoyer le code QR à la personne via les médias sociaux ou d'autres canaux de communication.


vous pouvez également cliquer sur le bouton **Editer** pour définir le nombre de Bitcoin à envoyer à cette adresse.


**Attention : Comme pour une facture, la fonction d'édition est utile dans les cas où vous souhaitez recevoir une quantité spécifique de Bitcoin à une adresse à un moment donné ; cependant, cela ne signifie pas que l'adresse ne peut pas recevoir des quantités supérieures ou inférieures.


cliquez sur **Plus d'adresses fraîches**, pour générer de nouvelles adresses aléatoires.


![generating_a\_bitcoin_add](assets/en/010.webp)


vous pouvez également générer une adresse on-chain Bitcoin en cliquant sur le bouton **Recevoir** en bas de la page d'accueil de votre wallet. Sélectionnez ensuite **Recevoir à une adresse bitcoin**, et continuez avec le même processus ci-dessus.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Envoi de Bitcoin via la chaîne


L'envoi de Bitcoin à partir du Valet wallet via on-chain est une tâche simple.


👉 En bas de la page d'accueil de votre wallet, cliquez sur le bouton **Envoyer**, entrez l'adresse du Bitcoin, ou cliquez sur **Scan**, pour scanner le code QR de l'adresse, puis cliquez sur **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Saisissez le montant Bitcoin que vous souhaitez envoyer. Vous pouvez saisir manuellement un montant en termes de Sats ou en termes de devise Fiat, ou vous pouvez cliquer sur **Max** pour utiliser tout votre solde on-chain.


vous pouvez également ajuster les frais que vous souhaitez payer pour la transaction en cliquant sur la petite case verte intitulée **frais**, puis en faisant glisser le point blanc vers la droite ou vers la gauche pour augmenter ou diminuer les frais, respectivement. Cliquez sur **Ok** pour envoyer la transaction.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Configuration d'un canal Lightning Network


Comme indiqué ci-dessus, Valet est un Bitcoin et un Lightning wallet autodéposés ; par conséquent, pour pouvoir envoyer et recevoir des Bitcoin via le réseau Lightning, vous devrez d'abord configurer un canal Lightning, en suivant les étapes suivantes :


👉 Sur l'écran d'accueil, cliquez sur la **carte violette** intitulée **Foudre**. Vous accédez à une page proposant les options suivantes :



- Scanner le nœud QR
- Achat à LNBIG.COM
- Achat chez BITREFILL.COM
- Demande de resynchronisation du graphe LN.


Lorsque vous sélectionnez **Achat auprès de lnbig.com** ou **Achat auprès de bitrefill.com**, vous serez redirigé vers les sites web de ces sociétés, où vous pourrez acheter une liquidité entrante de plusieurs capacités. Ignorez la dernière option **Demande de resynchronisation du graphique LN** pour l'instant.


Notre choix est donc de **Scanner un QR de nœud**. À ce stade, vous devez avoir décidé et obtenu le **code QR** du nœud vers lequel vous souhaitez ouvrir un canal. Vous pouvez ouvrir des canaux vers n'importe quel nœud public de votre choix. Consultez [1ML](https://1ml.com/) ou [Amboss](https://amboss.space/), sélectionnez le nœud public de votre choix et scannez le code QR associé au nœud que vous avez choisi.


![channel_opening_options](assets/en/016.webp)


👉 Vous serez automatiquement redirigé vers la page suivante, où vous devez maintenant financer votre chaîne. Encore une fois, l'utilisation du réseau Lightning en autodétention exige que vous utilisiez vos Bitcoin pour financer un canal. Cela signifie que vous devez avoir des Bitcoin dans votre on-chain wallet pour financer le canal Lightning. Veuillez vous référer à cet article de [Hacken] (https://hacken.io/discover/lightning-network/), pour en savoir plus sur le réseau Lightning.


![fund_channel](assets/en/017.webp)


👉 Entrez le **montant** de Bitcoin que vous souhaitez utiliser pour financer le canal, ou cliquez sur **Max** pour utiliser tout votre solde de on-chain Bitcoin. Vous pouvez ajuster les **frais**, ou laisser le paramètre de frais par défaut, et cliquer sur **Ok**.


**Attention:** Le montant avec lequel vous financez le canal sera la capacité de votre nouveau canal (c'est-à-dire le volume total de Sats qui peut être négocié vers et à partir de ce canal)


Il est également important d'utiliser plus de **100 000 Sats** comme montant de financement lors de l'ouverture d'un canal. En effet, de nombreux nœuds de foudre exigent une capacité minimale de 100 000 Sats pour ouvrir un canal vers eux. Pour éviter les essais et les erreurs, il suffit donc d'utiliser des montants supérieurs à cette fourchette.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


à ce stade, lorsque vous consultez votre page d'accueil wallet, vous verrez que le montant de votre financement a été transféré de la **carte Bitcoin** à la **carte Lightning**. Dans l'historique de vos transactions, vous verrez que la transaction de financement est en cours de traitement.


![channel_funding_processing](assets/en/020.webp)


👉 Si vous cliquez sur la carte Lightning, vous verrez des informations indiquant que votre canal Lightning est ouvert. Vous verrez également la **transaction de financement du canal** sur votre liste de transactions. Attendez que votre transaction de financement soit confirmée sur le blockchain, et votre canal Lightning sera prêt.


![channel_opening](assets/en/021.webp)


👉 Dès que la transaction de financement est confirmée, cliquez sur la **carte Lightning** sur votre page d'accueil, et vous verrez les informations sur votre canal Lightning comme suit :



- ENSEMBLE RANDOMIQUE DE NUMÉROS SÉPARÉS PAR DES POINTS:** Il s'agit des adresses IP des nœuds. (IPV4 et IPV6, respectivement)
- CAPACITÉ:** Il s'agit du volume total de Sats qui peut être envoyé et reçu par ce canal
- CAN SEND:** Il s'agit de la quantité de Sats que vous pouvez envoyer à ce stade. Vous remarquerez que ce chiffre est presque identique à la **Capacité**. Cela s'explique par le fait que vous n'avez pas encore envoyé de paiements par le canal.
- CAN RECEIVE:** C'est le nombre de Sats que vous pouvez recevoir sur ce canal en ce moment. (Ce nombre est très faible, voire nul, car pour pouvoir recevoir, vous devez d'abord envoyer des Sats pour créer une Liquidity entrante)
- REMBOURSABLE:** Ceci affiche le montant qui est remboursé à votre adresse on-chain lorsque vous fermez votre canal. C'est ce qu'on appelle aussi le **solde local du canal**. Notez qu'il est légèrement inférieur à la capacité du canal, car lorsque vous fermez un canal, vous devez payer des frais pour publier la transaction de fermeture sur la blockchain, tout comme vous l'avez fait lorsque vous avez financé le canal. Le système a donc déduit le montant approximatif le plus bas que vous aurez à payer)
- VALUE IN FLIGHT:** Lorsque quelqu'un envoie du sats à votre canal, ou lorsque vous essayez d'envoyer du sats à quelqu'un, et que pour une raison quelconque, la transaction est retardée, c'est souvent indiqué dans ce champ.


![channel_info](assets/en/022.webp)


## Envoi de Sats par votre canal


L'envoi du Sats par le Lightning Network est une tâche simple.


👉 En bas de la page d'accueil, cliquez sur **Envoyer**, et **coller** la facture Lightning (vous devez l'avoir copiée) dans le champ prévu à cet effet, ou cliquez sur **Scanner** pour scanner le QR code de la facture Lightning.


![click_send_or_scan](assets/en/023.webp)


La plupart des factures Lightning sont accompagnées d'un montant à payer préenregistré. Mais dans certains cas, il peut s'agir d'une facture ouverte dans laquelle vous devez indiquer le montant.


👉 Saisissez le montant en **Dollars** ou **Sats**, ou cliquez sur **Max**, pour utiliser tout le solde de votre canal Lightning, puis cliquez sur **Ok**. Dès qu'un bon chemin est trouvé, votre paiement est envoyé et terminé en quelques secondes. Gardez un œil sur la page d'accueil pour voir si le paiement a été effectué. Une coche verte apparaît lorsqu'il a été effectué.


![enter_the_amount](assets/en/024.webp)


## Recevoir le Sats par votre canal


La réception de paiements sur votre canal Lightning dépend en grande partie de la présence ou non d'une Liquidity entrante. Après avoir ouvert un canal, vous ne pourrez pas recevoir de paiements tant que vous n'aurez pas au moins envoyé quelques Sats pour **créer des liquidités entrantes** à l'autre bout de la connexion du canal. Pour savoir si vous pouvez recevoir des Sats et quelle quantité de Sats vous pouvez recevoir, vérifiez le champ **Peut recevoir** dans les informations relatives à votre canal. Vous saurez ainsi combien de Sats vous recevez à chaque instant.


Supposons maintenant que vous ayez envoyé des Sats à partir de votre canal, que vous ayez maintenant des liquidités entrantes et que vous puissiez recevoir des Sats.


Pour recevoir sur le canal Lightning, vous devez générer une facture. Contrairement au Bitcoin on-chain qui utilise des adresses, le réseau Lightning utilise des factures. Il existe deux façons de générer une facture sur Valet.


#### OPTION 1


👉 En bas de la page d'accueil, cliquez sur **Receive**, sélectionnez **Receive to Lightning invoice**. Renseignez le montant à recevoir dans la facture, et cliquez sur **Ok**. Copiez la facture ou partagez le code QR avec le payeur.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### OPTION 2


👉 Cliquez sur la carte Lightning violette sur la page d'accueil de votre wallet. Tapez n'importe où sur votre canal, et une liste d'options apparaîtra. Sélectionnez **Recevoir à la chaîne** et entrez le montant que vous recevez (en Sats ou en dollars). Vous verrez également combien de Sats vous pouvez recevoir (capacité d'entrée) lorsque vous remplissez la facture. Cliquez sur **Ok** et copiez la facture ou partagez le code QR avec le payeur.


![receive_to_channel](assets/en/028.webp)


**Attention:** La première option est une option universelle, ce qui signifie que si vous avez plus d'un canal actif et que vous utilisez la première option, le système sélectionnera automatiquement l'un de vos canaux pour recevoir le Sats.


Donc, dans ce scénario, la deuxième option est la meilleure à utiliser si vous voulez recevoir Sats sur un canal particulier.


### Explication des options de la fenêtre contextuelle de votre chaîne


Lorsque vous tapez sur votre chaîne, les champs d'option suivants s'affichent :


![channel_pop_ups](assets/en/029.webp)


**Partager les détails du canal LIGHTNING:** Cela vous permet de partager les détails de votre canal, tels que l'ID du pair distant, l'ID du canal local, la transaction de financement, la date de création, etc.


**FERMER LE CANAL AU PORTEFEUILLE:** Vous pouvez fermer votre canal de foudre quand vous le souhaitez. Pour fermer votre canal, le système vérifie le solde de Bitcoin que vous avez de votre côté du canal (rappelez-vous le champ **"Peut envoyer "**, aussi connu comme votre solde local), et il vous le renvoie. Dans Valet, vous pouvez choisir où vous voulez que le Bitcoin soit envoyé lorsque le canal est fermé. Ainsi, **Close channel to wallet** est l'une de vos deux options.


cliquez sur cette option et sélectionnez **Bitcoin**. La fermeture du canal commencera, et le solde de votre canal Bitcoin sera renvoyé à l'adresse on-chain de votre wallet.


![close_channel_to_wallet](assets/en/030.webp)


**CLOSE CHANNEL TO ADDRESS:** Il s'agit de la deuxième option de fermeture d'un canal. Lorsque vous choisissez cette option, vous êtes invité à saisir une adresse wallet à laquelle le solde Bitcoin de votre canal sera envoyé. Veuillez noter que dans cette option, vous ne pouvez scanner que le code QR de l'adresse Bitcoin à laquelle vous souhaitez fermer le canal. Actuellement, il n'y a pas d'option pour coller manuellement l'adresse.


cliquez sur cette option, scannez l'adresse Bitcoin et cliquez sur **Ok**. La fermeture du canal commencera, et votre solde Bitcoin Lightning sera envoyé à l'adresse que vous avez scannée.


![scan_address_and_Ok](assets/en/031.webp)


**RECEIVE TO CHANNEL:** C'est la même chose que de générer une facture, mais dans certains cas, vous pouvez avoir plus d'un canal, y compris des canaux Fiat (un type unique de canal Lightning que l'on peut obtenir dans le Valet wallet). Ainsi, si vous avez plusieurs canaux ouverts, cette option vous permet de recevoir des paiements sur un canal spécifique.


**REFILL FROM OTHER CHANNELS:** Cette option est une fonction qui vous permet de recharger un canal à partir d'autres canaux existants. Par exemple, si vous avez 2 canaux Lightning différents (A et B), et que le solde Bitcoin du canal A est épuisé, cette option vous permet de recharger facilement et automatiquement le solde du canal A à partir du canal B.


**DIRECT NOT PRIVATE RECEIVE:** Il s'agit également d'une option permettant de générer une facture pour recevoir un paiement, mais lorsque vous utilisez cette option, l'expéditeur vous paie directement. Cela signifie que le paiement ne passe pas par différents nœuds avant de vous parvenir, comme c'est le cas pour un paiement Lightning normal. Ainsi, l'expéditeur sait que c'est vous qu'il a payé, il connaît votre identifiant de canal, etc. Cette option peut souvent être utilisée lorsque vous recevez un paiement d'une source en laquelle vous avez confiance et que vous n'avez pas besoin de préserver votre vie privée.


## Canaux hébergés et canaux Fiat


Comme beaucoup d'autres Bitcoin wallet, Valet est un Bitcoin et un wallet Lightning simple et léger. Mais il possède une fonction Lightning unique qui le différencie de la plupart des autres Bitcoin wallet. Cette fonction est appelée **Canaux hébergés et Fiat**.


Les canaux Fiat sont un type d'implémentation Lightning qui facilite l'intégration et l'utilisation du réseau Lightning. Il s'agit d'une solution de garde qui permet un anonymat total, tout comme avec un canal Lightning normal. La technologie des canaux Fiat permet également de créer des dérivés Bitcoin sur le réseau Lightning. Par exemple, avec les canaux Fiat, les commerçants peuvent accepter des paiements Bitcoin à valeur stable sans se soucier de la volatilité du Bitcoin.


L'implémentation actuelle des canaux Fiat sur Valet permet la création de monnaies Fiat synthétiques stables garanties par Sats. Elle utilise une relation hôte-client dans laquelle l'hôte est n'importe quel nœud Lightning offrant ce service, et le client est l'utilisateur de Valet. Il s'agit d'une solution de garde car toutes les Sats se trouvent du côté de l'hôte ; cependant, la génération de factures, l'acheminement des tor et la génération de pré-images se produisent toujours du côté du client, comme dans un canal Lightning normal.


L'ouverture d'un canal Fiat suit le même processus que l'ouverture d'un canal Lightning. La seule différence significative est que dans ce cas, le client (utilisateur Valet) ne doit pas engager de liquidités on-chain pour créer une capacité de canal. L'hôte définit la capacité du canal et achemine tous les paiements pour le client.


pour ouvrir un canal Fiat, cliquez sur la **carte éclair** violette sur la page d'accueil de votre wallet. Sélectionnez **Scan Node QR** (à ce stade, vous devez avoir identifié un hôte auquel vous souhaitez ouvrir un canal et obtenu le QR du nœud. Un exemple de nœud hôte auquel vous pouvez ouvrir un canal Fiat est le nœud SATM du Standard Sats)


**Attention:** Il est important de noter que tout le monde peut être hôte. Tout ce dont vous avez besoin, c'est de faire fonctionner un nœud Lightning avec le **plugin Fiat channel** et un **service de Hedging**. Fiat channels est un projet open-source de *Standard Sats*. Pour en savoir plus [ici](https://github.com/standardsats/fiat-channels-rfc) et [ici](https://standardsats.github.io/).


Nœud SATM QR ci-dessous :


![SATM_node_QR](assets/en/032.webp)


👉 Une fois que vous avez scanné le QR du nœud, cliquez sur **Request USD fiat channel** ou **Request EUR fiat channels** (Il s'agit de la dénomination en fiat dans laquelle vos soldes Fiat seront cotés). Pour l'instant, choisissez USD et cliquez sur **OK**. Le canal sera ouvert automatiquement et vous pourrez commencer à recevoir Sats immédiatement. Vous voyez, c'est aussi simple que cela !!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Allez sur la page d'accueil de votre wallet, vous verrez une carte **vert clair** étiquetée **USD**, c'est votre **canal Fiat**.


![fiat_channel_card](assets/en/035.webp)


**Attention:** Lorsque vous recevez du Sats sur un canal Fiat, la valeur en fiat du Sats que vous avez reçu sera bloquée en tant que solde stable, tandis que le volume du Sats fluctuera avec le prix du Bitcoin. Cette solution a été conçue principalement pour les commerçants qui souhaitent accepter le Sats comme moyen de paiement mais qui ne veulent pas être confrontés aux problèmes de volatilité du Bitcoin. Cela leur permet de conserver une valeur stable à tout moment, tout en étant en mesure d'effectuer des transactions sur le réseau Lightning, en profitant de la portée mondiale et du règlement rapide du Bitcoin en tant que moyen d'échange sur le Lightning Network.


Lorsque votre canal Fiat est créé, voici les champs de valeur que vous verrez et ce que chacun d'entre eux signifie :


![fiat_channel_info](assets/en/036.webp)



- ENSEMBLE RANDOMIQUE DE NUMÉROS SÉPARÉS PAR DES POINTS:** Il s'agit des adresses IP des nœuds. (IPV4 et IPV6, respectivement)
- TARIF SERVEUR:** Il s'agit du prix du marché Bitcoin auquel l'hôte vous offre ses services. Il sera souvent légèrement différent du prix du marché prédominant, parce qu'un hôte peut ajouter une petite prime. Il appartient entièrement à l'hébergeur de décider de ce tarif, qui peut donc varier d'un hébergeur à l'autre.
- BALANCE FIAT:** Il s'agit de la valeur en fiats stables verrouillée de chaque sat que vous recevez sur ce canal. Rappelez-vous, comme expliqué plus haut, chaque fois que vous recevez du Sats sur votre canal Fiat, la valeur en fiat du Sats au moment de la réception est immédiatement bloquée en tant que valeur stable synthétique en fiat dans ce champ. La valeur de votre **Solde Fiat** ne fluctue pas en fonction du prix du marché de la Bitcoin. Chaque fois que vous souhaitez effectuer des paiements à partir de ce canal, vous ne pouvez envoyer que l'équivalent en Sats de ce solde Fiat. Il s'agit donc d'une monnaie fiduciaire numérique garantie par le Sats.
- CAPACITÉ:** Il s'agit du volume total de Sats qui peut être envoyé et reçu par ce canal. (Cette capacité est également définie par l'hôte. Et contrairement à un canal Lightning normal, cette capacité peut être ajustée par l'hôte le cas échéant)
- CAN SEND:** Il s'agit du volume de Sats que vous pouvez envoyer à chaque point en fonction de votre solde de fiats. Ceci est complètement différent de ce que vous avez dans un canal Lightning normal, parce que cette valeur flotte avec le prix du Bitcoin. Par conséquent, ce que vous voyez ici est la valeur en Sats de votre solde en Fiat à tout moment en fonction du **Taux du Serveur**.
- CAN RECEIVE:** Il s'agit du nombre de Sats que vous pouvez recevoir sur ce canal à l'heure actuelle. Après avoir créé votre canal, cette valeur devrait être la même que la capacité du canal.
- VALUE IN FLIGHT:** Lorsque quelqu'un envoie des sats à votre canal, ou lorsque vous essayez d'envoyer des sats à quelqu'un, et que pour une raison quelconque, la transaction est retardée, c'est souvent indiqué dans ce champ.


Voici quelques points importants à noter concernant les chaînes Fiat :



- Contrairement à un canal Lightning normal, lorsque vous ouvrez un canal fiat, vous pouvez immédiatement commencer à recevoir des Sats, mais vous ne pouvez pas en envoyer. Vous ne pouvez envoyer du Sats que lorsque vous avez reçu du Sats.
- À tout moment, l'actif envoyé et reçu est Sats. Le *Fiat Balance* n'est qu'une représentation synthétique d'une valeur Bitcoin reçue à tout moment. Il ne s'agit donc pas d'une création token ou d'une nouvelle crypto-monnaie.
- Le canal Fiat est surtout utile aux commerçants/entreprises qui hésitent à accepter des paiements en Bitcoin en raison des craintes liées à la volatilité. Il peut également être utile aux entreprises qui souhaitent payer les salaires de leurs employés en Bitcoin sans avoir à supporter les conséquences de la volatilité du Bitcoin, qui peut rendre leur capital salarial instable. Il peut également être utile aux personnes qui vivent dans une région où l'utilisation du Bitcoin est prédominante, mais dont le coût de la vie est fixe.
- Remarquez qu'il n'y a pas de champ intitulé **REFUNDABLE**. C'est parce que, techniquement, vous ne pouvez pas fermer une chaîne Fiat. Vous ne pouvez cesser d'utiliser une chaîne Fiat qu'en drainant son solde vers votre chaîne Eclair normale.


### Les options d'ouverture du canal Fiat expliquées


Lorsque vous tapez sur votre canal Fiat Lightning, les champs suivants s'affichent :


![fiat_channel_pop_up](assets/en/037.webp)


**Cette fonction vous permet de partager les détails de votre canal Fiat, tels que l'identifiant du pair distant, l'identifiant du canal local, la date de création, etc.


**EXPORT CHANNEL STATE:** Cela vous permet d'exporter l'état d'un canal à n'importe quel moment. Ceci est généralement utile pour corriger les erreurs de canal, et un hôte peut vous demander de le partager si c'est nécessaire.


**Comme mentionné précédemment, vous ne pouvez pas techniquement fermer un canal Fiat, mais vous pouvez drainer le solde de votre canal dans votre canal Eclair normal existant. Cela déplace automatiquement l'équivalent en Sat de votre solde Fiat vers votre canal Eclair normal.


**RECEIVE TO CHANNEL:** C'est la même chose que de générer une facture, mais dans certains cas, un utilisateur peut avoir plus d'un canal Fiat avec différents hôtes, y compris des canaux Lightning normaux. Ainsi, si un utilisateur a plusieurs canaux ouverts, cette option permet de s'assurer qu'il peut recevoir un paiement sur un canal spécifique.


**REFILL FROM OTHER CHANNELS:** Cette option permet à l'utilisateur de recharger un canal à partir d'autres canaux existants. Ainsi, avec cette option, vous pouvez recharger votre canal Fiat à partir d'un canal normal ou d'autres canaux Fiat que vous possédez, de la même manière que vous pouvez drainer.


**DIRECT NOT PRIVATE RECEIVE:** Il s'agit également d'une option permettant de générer une facture pour recevoir un paiement, mais lorsque vous utilisez cette option, l'expéditeur vous paie directement. Cela signifie que le paiement ne passe pas par différents nœuds avant de vous parvenir. L'expéditeur sait donc que c'est vous qu'il a payé, il connaît votre identifiant de canal, etc. Cette option est souvent utilisée lorsque vous recevez un paiement d'une source en laquelle vous avez confiance et que vous n'avez pas besoin de préserver votre vie privée.


## Réglages Valet :


Comme toute autre application, Valet dispose de paramètres que vous pouvez ajuster à votre convenance. Vous pouvez accéder à la page des paramètres à partir de l'écran d'accueil.


👉 Sur l'écran d'accueil, cliquez sur l'icône **Gear** située dans le coin supérieur droit de l'écran pour accéder aux paramètres. Vous trouverez ci-dessous les composants de la section des paramètres.


![settings_icon](assets/en/038.webp)


**LOCAL CHANNEL BACKUP IS ENABLED:** Si cette option est **Disabled**, vous devez l'activer car c'est le seul moyen de récupérer vos canaux Lightning normaux si vous désinstallez et réinstallez Valet. Nous expliquerons cela plus tard. Cliquez donc sur ceci, et donnez à Valet la permission d'accéder à votre **stockage multimédia** car c'est là que le fichier de sauvegarde est sauvegardé.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**Où stocker les sauvegardes locales:** Si vous avez autorisé Valet à accéder à votre espace de stockage, ce champ sera automatiquement configuré pour stocker les sauvegardes locales dans votre dossier **Téléchargements**. Mais vous pouvez le modifier en cliquant ici et en sélectionnant le dossier de votre choix.


**GESTION DES PORTEFEUILLES DE CHAINE** C'est un peu technique, et vous n'avez pas besoin de vous en préoccuper à moins d'être suffisamment expérimenté. Le réglage par défaut est parfait.


**ADD HARDWARE WALLET:** Vous ne devriez pas vous préoccuper de cette option, à moins que vous n'ayez un wallet matériel que vous voulez connecter et surveiller. Avec ce paramètre, vous pouvez scanner et connecter votre wallet matériel, tel que le Trezor ou la carte Cold, et surveiller ses activités. Il s'agit d'une fonction de surveillance uniquement, ce qui signifie que vous ne pouvez pas effectuer de transactions sur le matériel wallet à partir d'ici. Vous pouvez seulement observer et surveiller les activités, les soldes, etc. de la wallet.


**SET CUSTOM ELECTRUM NODE:** Ceci est également technique, et à moins que vous ne soyez suffisamment informé, vous ne devriez pas vous en préoccuper. Le réglage par défaut est suffisant.


**Unités de Bitcoin:** Il s'agit de la façon dont vous voulez que votre solde Bitcoin soit affiché. La première option affiche votre solde en termes Satoshi, par exemple 1 000 000 Sats, tandis que la seconde option l'affiche en décimales BTC. par exemple 0.01BTC


**UTILISER L'AUTHENTIFICATION PAR PIN** Si vous cochez cette case, vous devrez définir un PIN ou une empreinte digitale que vous devrez saisir pour vous connecter à votre wallet et authentifier les transactions.


**UTILISER LA CONNEXION TOR:** Si vous cochez cette case, vos transactions seront acheminées via le réseau Tor. Cela ajoute une couche supplémentaire de confidentialité, mais peut entraîner un retard dans le traitement des paiements, en particulier pour les paiements Lightning.


**VIEW BIP39 RECOVERY PHRASE:** C'est ici que vous pouvez accéder à votre phrase de 12 mots seed pour la sauvegarde. Si vous ne l'avez pas notée avant, ou si vous ne trouvez pas l'endroit où vous l'avez notée, tant que vous avez accès à votre Wallet, vous pouvez la copier à partir d'ici.


**STATISTIQUES D'UTILISATION:** Cette fonction vous présente un résumé de toutes vos transactions et activités depuis la création de la wallet


![usage_stats](assets/en/041.webp)


## Récupération du Wallet


Valet est un wallet non gardien, donc si vous perdez votre appareil ou désinstallez votre application wallet, vous devrez procéder à une récupération wallet pour récupérer vos Bitcoin et vos canaux Lightning. Au début de ce tutoriel, nous avons mentionné l'importance d'écrire votre **phrase de 12 mots seed** car c'est la clé pour récupérer votre wallet. Il n'y a pas de représentants du service clientèle qui peuvent vous aider à récupérer votre wallet.


Deux outils importants sont nécessaires pour récupérer votre Valet wallet, selon que vous disposiez ou non d'un canal Lightning actif. Pour un utilisateur qui n'avait pas de canal Lightning normal actif, tout ce dont il a besoin est sa **phrase de 12 mots seed**, en suivant les étapes simples ci-dessous :


👉 Installer une nouvelle application Valet et lancer l'application.


👉 Sélectionner **Restaurer la Wallet existante**


![restore_existing_wallet](assets/en/042.webp)


👉 Sélectionnez **Phrase de récupération uniquement**.


![select_recovery_phrase](assets/en/043.webp)


👉 Saisissez votre phrase de récupération de 12 mots et cliquez sur **OK**.


![input_12_words](assets/en/044.webp)


Votre wallet sera récupérée. Dans ce cas, seul le solde de votre on-chain Bitcoin sera rétabli.


Cependant, si vous aviez un canal Eclair normal actif et que vous récupérez votre wallet avec seulement la phrase de récupération, votre canal Eclair sera fermé de force, et tout solde Bitcoin que vous avez dessus sera automatiquement envoyé vers votre solde on-chain.


L'autre moyen de récupérer votre Valet wallet, surtout si vous aviez un canal Lightning normal ouvert avant de désinstaller Valet, est d'**utiliser le fichier de sauvegarde local sauvegardé sur votre appareil, ainsi que votre phrase de 12 mots seed**. Si vous utilisez ces deux éléments, l'état de votre canal Lightning sera restauré, et votre canal Lightning ne sera donc pas fermé de force.


Voici la marche à suivre :


👉 Installer une nouvelle application Valet et lancer l'application.


👉 Sélectionnez **Restaurer la Wallet existante**.


👉 Sélectionnez la phrase **Sauvegarde + Récupération**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Sélectionnez le fichier de sauvegarde dans le gestionnaire de fichiers de votre téléphone. (Par défaut, il est toujours stocké dans votre dossier **Téléchargements**)


![local_backup_file_in_download_folder](assets/en/046.webp)


Une fois le bon fichier de sauvegarde sélectionné, une invite confirmant qu'un **"Fichier de sauvegarde est présent "** s'affiche et vous demande d'entrer votre phrase seed de 12 mots.


![enter_12_words](assets/en/047.webp)


👉 Saisissez votre phrase de récupération de 12 mots et cliquez sur **OK**. Vous serez dirigé vers votre page d'accueil wallet.


attendez que la synchronisation du réseau Bitcoin (**SYNC**) et la synchronisation du nœud Lightning (**LN Sync**) soient terminées, et votre wallet sera entièrement restauré, y compris vos canaux Lightning.


![LN_sync](assets/en/048.webp)


## Conclusion


Valet est une solution wallet intéressante, dont les caractéristiques permettent d'intégrer de nouveaux utilisateurs. Elle dispose également d'un canal Fiat, une technologie qui n'est pas si récente et qui garantit l'intégration des entreprises gérées en monnaie fiduciaire dans la norme Bitcoin.


Téléchargez Valet dès aujourd'hui, et essayez-le ! !! 🧡
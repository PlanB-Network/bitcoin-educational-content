---
name: Mullvad VPN
description: Mettre en place son VPN payé en bitcoins
---
![cover](assets/cover.webp)

Un VPN ("*Virtual Private Network*") est un service qui établit une connexion sécurisée et chiffrée entre votre téléphone ou votre ordinateur et un serveur distant géré par un fournisseur de VPN.

Techniquement, lors de la connexion à un VPN, votre trafic Internet est redirigé via un tunnel chiffré vers le serveur VPN. Ce processus rend difficile pour des tiers, tels que les fournisseurs d'accès Internet (FAI) ou des acteurs malveillants, d'intercepter ou de lire vos données. Le serveur VPN agit ensuite comme un intermédiaire qui se connecte au service que vous souhaitez utiliser à votre place. Il attribue à votre connexion une nouvelle adresse IP, ce qui permet de masquer votre adresse IP réelle auprès des sites que vous visitez. Attention, contrairement à ce que laissent penser certaines publicités en ligne, utiliser un VPN ne permet pas de naviguer anonymement sur Internet, car il nécessite une forme de confiance envers le fournisseur de VPN qui peut voir tout votre trafic.
![MULLVAD VPN](assets/fr/01.webp)
Les avantages d'utiliser un VPN sont multiples. Premièrement, il préserve la confidentialité de votre activité en ligne vis-à-vis des FAI ou des gouvernements, à condition que le fournisseur de VPN ne partage pas vos informations. Deuxièmement, il sécurise vos données, en particulier lorsque vous êtes connecté à des réseaux Wi-Fi publics, qui sont vulnérables aux attaques de type MITM ("**man-in-the-middle**"). Troisièmement, en masquant votre adresse IP, un VPN vous permet de contourner les restrictions géographiques et la censure, pour avoir accès à des contenus autrement indisponibles ou bloqués dans votre région.

Vous l'aurez compris, le VPN déplace le risque d'observation de votre trafic sur le fournisseur du VPN. Lors du choix de votre fournisseur de VPN, il est donc important de considérer les données personnelles requises pour l'inscription. Si ce dernier demande des informations telles que votre numéro de téléphone, adresse email, détails de carte bancaire, ou pire encore, votre adresse postale, le risque d'association entre votre identité et votre trafic est accru. En cas de compromission du fournisseur ou d'une saisie judiciaire, il serait facile d'associer votre trafic à vos données personnelles. Il est donc recommandé de choisir un fournisseur qui ne demande aucune donnée personnelle et qui accepte des paiements anonymes, comme par exemple en bitcoins.

Dans ce tutoriel, je vous présente une solution de VPN simple à mettre en place, performante, à un coût raisonnable, et surtout, qui ne requiert aucune information personnelle pour son utilisation.

## Présentation de Mullvad VPN

Mullvad VPN est un service suédois qui se distingue par son engagement en faveur de la confidentialité des utilisateurs. À l'inverse des fournisseurs de VPN grand public, Mullvad ne requiert aucune donnée personnelle lors de l'inscription. Il n'est pas nécessaire de fournir une adresse e-mail, un numéro de téléphone, ou un nom ; Mullvad vous attribue plutôt un numéro de compte anonyme utilisé pour payer et accéder au service. De plus, Mullvad affirme ne conserver aucun historique d'activité qui transite par leurs serveurs.
![MULLVAD VPN](assets/notext/02.webp)
Pour le paiement, il n'est pas forcément nécessaire de fournir des données de carte bancaire, car Mullvad accepte les paiements en bitcoins (onchain uniquement sur leur site officiel, mais il existe une méthode non-officielle pour payer en Lightning). Ils acceptent également les paiements en cash par la poste.

Mullvad VPN se distingue aussi par sa transparence et sa sécurité. Leur logiciel est open-source et ils se soumettent régulièrement à des audits de sécurité indépendants pour évaluer leurs applications et leur infrastructure, dont les résultats sont [publiés sur leur site web](https://mullvad.net/fr/blog/tag/audits). La société derrière Mullvad est basée en Suède, un pays réputé pour ses lois strictes en matière de protection de la vie privée. Ils utilisent exclusivement des serveurs autohébergés, ce qui écarte ainsi les risques associés à l'utilisation de services cloud tiers, tels que les hyperscalers AWS, Google Cloud ou Microsoft Azure.

En termes de fonctionnalités, Mullvad offre tout ce que l'on attend d'un bon client VPN, notamment un kill switch qui protège votre trafic en cas de déconnexion du VPN, une option pour désactiver le VPN sur certaines applications spécifiques, et la possibilité de router son trafic à travers plusieurs serveurs VPN.

Forcément, cette qualité de service a un coût, mais un prix adéquat est souvent un indicateur de qualité et d'honnêteté. Cela peut signaler que l'entreprise dispose d'un business model sans avoir besoin de vendre vos données personnelles à des tiers. Mullvad VPN propose un tarif unique de 5 € par mois, utilisable sur jusqu'à 5 appareils différents.
![MULLVAD VPN](assets/notext/03.webp)
Contrairement aux fournisseurs de VPN grand public, Mullvad dispose d'un modèle d'achat de temps d'accès au service plutôt qu'un abonnement récurrent et automatique. Vous effectuez simplement un paiement unique en bitcoins pour la durée choisie. Par exemple, si vous achetez un accès d'un an, vous pourrez utiliser le service pendant cette période, après quoi vous devrez retourner sur le site web de Mullvad pour renouveler votre temps d'accès.

Comparativement à IVPN, un autre fournisseur de VPN de haute qualité, Mullvad est légèrement plus économique. Par exemple, même en optant pour un achat de trois ans chez IVPN, le coût mensuel s'élève à environ 5,40 €. IVPN offre cependant quelques services supplémentaires et dispose aussi d'un forfait moins cher que celui de Mullvad (le forfait Standard), mais ce dernier est limité à seulement 2 appareils et exclut le protocole "*multi-hop*".

J'ai également mené quelques tests informels de débit pour comparer IVPN et Mullvad. Bien qu'IVPN ait montré une légère supériorité en termes de performances, les débits chez Mullvad étaient toujours très satisfaisants. En comparaison avec les fournisseurs de VPN grand public, IVPN et Mullvad se sont révélés au moins aussi performants, voire supérieurs dans certains cas.

## Comment installer Mullvad VPN sur un ordinateur ?

Rendez-vous sur [le site web officiel de Mullvad](https://mullvad.net/en/download/) et cliquez sur le menu "*Downloads*".
![MULLVAD VPN](assets/notext/04.webp)
Pour les utilisateurs de Windows ou macOS, téléchargez le logiciel directement depuis le site et suivez les instructions fournies par l'assistant pour terminer l'installation.
![MULLVAD VPN](assets/notext/05.webp)
Pour les utilisateurs de Linux, vous pouvez retrouver les instructions spécifiques à votre distribution dans [la section "*Linux*"](https://mullvad.net/en/download/vpn/linux).
![MULLVAD VPN](assets/notext/06.webp)
Une fois l'installation terminée, vous devrez saisir l'identifiant de votre compte. Nous verrons comment l'obtenir dans les sections suivantes de ce tutoriel.

## Comment installer Mullvad VPN sur un smartphone ?

Téléchargez Mullvad VPN depuis votre magasin d'applications, que ce soit l'[AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513) pour les utilisateurs iOS, le [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) pour Android, ou encore [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/). Si vous utilisez Android, vous avez également la possibilité de télécharger directement le fichier `.apk` depuis [le site de Mullvad](https://mullvad.net/en/download/vpn/android).
![MULLVAD VPN](assets/notext/07.webp)
Lors de la première utilisation de l'application, vous serez déconnecté. Vous devrez entrer l'identifiant de votre compte pour activer le service.
![MULLVAD VPN](assets/notext/08.webp)
Maintenant, passons à l'activation de Mullvad sur vos appareils.

## Comment payer et activer Mullvad VPN ?

Rendez-vous sur [le site officiel de Mullvad](https://mullvad.net/) et cliquez sur le bouton "*Get Started*".
![MULLVAD VPN](assets/notext/09.webp)
Cliquez sur le bouton "*Generate account number*".
![MULLVAD VPN](assets/notext/10.webp)
Mullvad va ensuite créer votre compte. Vous n'avez besoin de renseigner aucune donnée personnelle. C'est uniquement votre numéro de compte qui vous permettra de vous connecter. Il agit en quelque sorte comme une clé d'accès. Enregistrez-le dans un endroit sûr comme votre gestionnaire de mots de passe par exemple. Vous pouvez également en faire une copie papier.
![MULLVAD VPN](assets/notext/11.webp)
Cliquez ensuite sur le bouton "*Add time to your account*".
![MULLVAD VPN](assets/notext/12.webp)
Vous arrivez ensuite sur la page de connexion à votre compte. Entrez le numéro de votre compte puis cliquez sur le bouton "*Log in*".
![MULLVAD VPN](assets/notext/13.webp)
Choisissez votre méthode de paiement. Je vous recommande de payer en bitcoins, car vous bénéficierez d'une réduction de 10 %, ce qui ramène le coût à 4,50 € par mois. Si vous préférez payer via Lightning, je vous fournirai une méthode alternative dans la partie suivante.
![MULLVAD VPN](assets/notext/14.webp)
Cliquez sur le bouton "*Create a one-time payment address*".
![MULLVAD VPN](assets/notext/15.webp)
Puis payez avec votre portefeuille Bitcoin le montant indiqué à l'adresse de réception que l'on vous donne.
![MULLVAD VPN](assets/notext/16.webp)
Cela peut prendre quelques minutes avant que le site ne détecte votre paiement, une fois la transaction confirmée. Une fois le paiement détecté par Mullvad, la durée de votre abonnement apparaîtra en haut à gauche de la page, à la place de la mention "*No time left*".
![MULLVAD VPN](assets/notext/17.webp)
Vous pouvez alors entrer votre numéro de compte sur le logiciel pour activer le VPN.
![MULLVAD VPN](assets/notext/18.webp)
Pour activer le VPN sur votre application mobile, c'est exactement le processus. Il vous suffit d'entrer votre numéro de compte.
![MULLVAD VPN](assets/notext/19.webp)
## Comment payer Mullvad VPN avec Lightning ?

Vous l'aurez compris, Mullvad n'accepte pas encore les paiements via le Lightning Network. Cependant, grâce à une recommandation de [Lounès](https://x.com/louneskmt), j'ai découvert un service informel qui permet de contourner cette limitation. Ce service, disponible sur [vpn.sovereign.engineering](https://vpn.sovereign.engineering/), accepte vos paiements sur Lightning et vous fournit en retour un forfait valide pour Mullvad.
![MULLVAD VPN](assets/notext/20.webp)
Vous avez 2 options différentes sur ce site : vous pouvez faire confiance au gestionnaire du site et saisir votre numéro de compte directement, puis cliquer sur "*Log in*" pour que votre forfait Mullvad soit validé automatiquement. Ou bien, vous pouvez cliquer sur le bouton "*Heck yeah!*" pour acheter un Voucher en Lightning, que vous pourrez ensuite utiliser sur le site officiel de Mullvad pour obtenir votre forfait.
![MULLVAD VPN](assets/notext/21.webp)
Dans les 2 cas, on vous demandera ensuite de sélectionner la durée de votre forfait. Vous avez le choix entre 6 mois et 1 an.
![MULLVAD VPN](assets/notext/22.webp)
Puis cliquez sur le bouton "*Top-up with Lightning*".
![MULLVAD VPN](assets/notext/23.webp)
Pour finaliser l'achat, payez l'invoice avec votre portefeuille Lightning. 
![MULLVAD VPN](assets/notext/24.webp)
Si vous avez opté pour l'achat d'un Voucher, sur le site de Mullvad, sélectionnez "*Voucher*" parmi les méthodes de paiement disponibles sur votre compte. Ensuite, saisissez le numéro de Voucher que vous avez reçu du site vpn.sovereign.engineering dans la case prévue à cet effet.
![MULLVAD VPN](assets/notext/25.webp)
## Comment utiliser et configurer Mullvad VPN ?

Maintenant que vous disposez d'un compte actif et avez entré votre numéro de compte dans le logiciel ou l'application Mullvad, vous pouvez pleinement profiter des services de votre VPN.
![MULLVAD VPN](assets/notext/26.webp)
Pour vous déconnecter du VPN, cliquez simplement sur le bouton "*Disconnect*".
![MULLVAD VPN](assets/notext/27.webp)
La petite flèche rouge à côté du bouton "*Disconnect*" vous permet de changer de serveur sans modifier la localisation actuelle.
![MULLVAD VPN](assets/notext/28.webp)
Si vous souhaitez changer de ville pour votre serveur VPN, cliquez sur "*Switch location*" pour choisir une nouvelle localisation.
![MULLVAD VPN](assets/notext/29.webp)
En haut de l'écran, vous verrez le pseudonyme de votre appareil ainsi que la durée restante de votre forfait.
![MULLVAD VPN](assets/notext/30.webp)
En cliquant sur l'icône du bonhomme, vous accéderez aux informations détaillées de votre compte.
![MULLVAD VPN](assets/notext/31.webp)
Pour accéder aux paramètres, cliquez sur la roue crantée.
![MULLVAD VPN](assets/notext/32.webp)
Dans le menu "*User interface settings*", vous pourrez personnaliser les paramètres de votre logiciel, y compris la langue de l'interface et son comportement sur votre système.
![MULLVAD VPN](assets/notext/33.webp)
Dans le menu "*VPN settings*", vous trouverez les options relatives à votre VPN. Je recommande d'activer les options "*Launch app on start-up*" et "*Auto-connect*" pour que votre connexion VPN se lance automatiquement au démarrage de votre machine.
![MULLVAD VPN](assets/notext/34.webp)
Dans le sous-menu "*DNS content blockers*", vous avez la possibilité de filtrer et de bloquer les requêtes DNS vers des sites web malveillants, publicitaires ou indésirables.
![MULLVAD VPN](assets/notext/35.webp)
Enfin, le menu "*Split tunneling*" vous permet de sélectionner les applications spécifiques sur votre machine pour lesquelles le trafic internet ne sera pas routé à travers le VPN.
![MULLVAD VPN](assets/notext/36.webp)
Pour avoir une vision globale sur votre compte Mullvad et gérer les différents appareils connectés, vous pouvez cliquer sur le menu "*Devices*" sur le site web.
![MULLVAD VPN](assets/notext/37.webp)
Et voilà, vous êtes désormais équipé pour profiter pleinement de Mullvad VPN. Si vous souhaitez découvrir un autre fournisseur de VPN similaire à Mullvad, autant en termes de caractéristiques que de tarifs, je vous conseille également de consulter notre tutoriel sur IVPN :

https://planb.network/tutorials/others/general/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68

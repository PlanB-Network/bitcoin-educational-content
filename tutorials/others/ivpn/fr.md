---
name: IVPN
description: Mettre en place son VPN payé en bitcoins
---
![cover](assets/cover.webp)

Un VPN ("*Virtual Private Network*") est un service qui établit une connexion sécurisée et chiffrée entre votre téléphone ou ordinateur et un serveur distant géré par le fournisseur de VPN.

Techniquement, lors de la connexion à un VPN, votre trafic Internet est redirigé via un tunnel chiffré vers le serveur VPN. Ce processus rend difficile pour des tiers, tels que les fournisseurs d'accès Internet (FAI) ou des acteurs malveillants, d'intercepter ou de lire vos données. Le serveur VPN agit ensuite comme un intermédiaire qui se connecte au service que vous souhaitez utiliser à votre place. Il attribue à votre connexion une nouvelle adresse IP, ce qui permet de masquer votre adresse IP réelle auprès des sites que vous visitez. Attention, contrairement à ce que laissent penser certaines publicités en ligne, utiliser un VPN ne permet pas de naviguer anonymement sur Internet, car il nécessite une forme de confiance envers le fournisseur de VPN qui peut voir tout votre trafic.
![IVPN](assets/fr/01.webp)
Les avantages d'utiliser un VPN sont multiples. Premièrement, il préserve la confidentialité de votre activité en ligne vis-à-vis des FAI ou des gouvernements, à condition que le fournisseur de VPN ne partage pas vos informations. Deuxièmement, il sécurise vos données, en particulier lorsque vous êtes connecté à des réseaux Wi-Fi publics, qui sont vulnérables aux attaques de type MITM (man-in-the-middle). Troisièmement, en masquant votre adresse IP, un VPN vous permet de contourner les restrictions géographiques et la censure, pour avoir accès à des contenus autrement indisponibles ou bloqués dans votre région.

Vous l'aurez compris, le VPN déplace le risque d'observation de votre trafic sur le fournisseur du VPN. Lors du choix de votre fournisseur de VPN, il est donc important de considérer les données personnelles requises pour l'inscription. Si ce dernier demande des informations telles que votre numéro de téléphone, adresse email, détails de carte bancaire, ou pire encore, votre adresse postale, le risque d'association entre votre identité et votre trafic est accru. En cas de compromission du fournisseur ou d'une saisie judiciaire, il serait facile d'associer votre trafic à vos données personnelles. Il est donc recommandé de choisir un fournisseur qui ne demande aucune donnée personnelle et qui accepte des paiements anonymes, comme par exemple en bitcoins.

Dans ce tutoriel, je vous présente une solution de VPN simple à mettre en place, performante, à un coût raisonnable, et surtout, qui ne requiert aucune information personnelle pour son utilisation.

## Présentation IVPN

IVPN est un service VPN conçu spécifiquement pour les utilisateurs qui recherchent une forme de confidentialité. Contrairement aux fournisseurs de VPN populaires souvent mis en avant sur YouTube, IVPN se distingue par sa transparence, sa sécurité, et son respect de la vie privée.

La politique de confidentialité d'IVPN est stricte : aucun renseignement personnel n'est requis lors de l'inscription. Vous pouvez ouvrir un compte sans fournir d'adresse email, de nom, ou de numéro de téléphone. Pour le paiement, il n'est pas nécessaire de saisir de données de carte bancaire, car IVPN accepte les paiements en bitcoins (onchain et Lightning). De plus, IVPN affirme ne conserver aucun journal d'activité, ce qui veut dire qu'en théorie, votre trafic Internet n'est pas enregistré par l'entreprise.

IVPN est aussi [entièrement open-source](https://github.com/ivpn), au niveau du logiciel, des applications, et même de leur site web, ce qui permet à chacun de vérifier et d'examiner leur code. Ils se soumettent également à des audits de sécurité indépendants chaque année, dont les résultats sont publiés sur leur site web.

IVPN utilise exclusivement des serveurs autohébergés, ce qui écarte ainsi les risques associés à l'utilisation de services cloud tiers, tels que AWS, Google Cloud ou Microsoft Azure.

Le service propose de nombreuses fonctionnalités avancées, telles que le multi-hop, qui achemine le trafic via plusieurs serveurs situés dans différentes juridictions pour améliorer l'anonymat. IVPN intègre également un bloqueur de traqueurs et de publicités, et offre la possibilité de choisir parmi différents protocoles de VPN.

Forcément, cette qualité de service a un coût, mais un prix adéquat est souvent un indicateur de qualité et d'honnêteté. Cela peut signaler que l'entreprise dispose d'un business model sans avoir besoin de vendre des données personnelles. IVPN offre alors 2 types de forfaits : le forfait Standard, qui permet de connecter jusqu'à 2 appareils, et le forfait Pro, qui permet jusqu'à 7 connexions et inclut le protocole "*Multi-hop*" qui permet de router son trafic à travers plusieurs serveurs.

Contrairement aux fournisseurs de VPN grand public, IVPN fonctionne sur un modèle d'achat de temps d'accès au service, plutôt que sur un abonnement récurrent. Vous payez en bitcoins une seule fois pour la durée choisie. Par exemple, si vous achetez un accès d'un an, vous pourrez utiliser le service pendant cette période, après quoi vous devrez retourner sur le site web d'IVPN pour acheter de nouveau du temps d'accès.

Les [tarifs d'IVPN](https://www.ivpn.net/en/pricing/) sont dégressifs en fonction de la durée d'accès achetée. Voici les prix pour le forfait Standard :
- 1 semaine : 2 $
- 1 mois : 6 $
- 1 an : 60 $
- 2 ans : 100 $
- 3 ans : 140 $

Et pour le forfait Pro :
- 1 semaine : 4 $
- 1 mois : 10 $
- 1 an : 100 $
- 2 ans : 160 $
- 3 ans : 220 $

## Comment installer IVPN sur un ordinateur ?

Téléchargez [la dernière version du logiciel](https://www.ivpn.net/en/apps-windows/) pour votre système d'exploitation, puis procédez à l'installation en suivant les étapes dans l'assistant d'installation.
![IVPN](assets/notext/02.webp)
Pour les utilisateurs de Linux, référez-vous aux instructions spécifiques à votre distribution disponibles sur [cette page](https://www.ivpn.net/en/apps-linux/).
![IVPN](assets/notext/03.webp)
Une fois l'installation terminée, vous devrez saisir l'identifiant de votre compte. Nous verrons comment l'obtenir dans les sections suivantes de ce tutoriel.
![IVPN](assets/notext/04.webp)
## Comment installer IVPN sur un smartphone ?

Téléchargez IVPN depuis votre magasin d'applications, que ce soit l'[AppStore](https://apps.apple.com/us/app/ivpn-secure-vpn-for-privacy/id1193122683) pour les utilisateurs iOS, le [Google Play Store](https://play.google.com/store/apps/details?id=net.ivpn.client) pour Android, ou encore [F-Droid](https://f-droid.org/en/packages/net.ivpn.client). Si vous utilisez Android, vous avez également la possibilité de télécharger directement le fichier `.apk` depuis [le site d'IVPN](https://www.ivpn.net/en/apps-android/).
![IVPN](assets/notext/05.webp)
Lors de la première utilisation de l'application, vous serez déconnecté. Vous devrez entrer l'identifiant de votre compte pour activer le service.
![IVPN](assets/notext/06.webp)
Maintenant, passons à l'activation d'IVPN sur vos appareils.

## Comment payer et activer IVPN ?

Rendez-vous sur le site officiel IVPN [sur la page de paiement](https://www.ivpn.net/en/pricing/).
![IVPN](assets/notext/07.webp)
Sélectionnez le forfait qui correspond le mieux à vos besoins. Pour ce tutoriel, nous opterons pour le forfait Standard qui nous permet d'activer le VPN sur notre ordinateur et notre smartphone par exemple.
![IVPN](assets/notext/08.webp)
IVPN va ensuite créer votre compte. Vous n'avez besoin de renseigner aucune donnée personnelle. C'est uniquement votre identifiant de compte qui vous permettra de vous connecter. Il agit en quelque sorte comme une clé d'accès. Enregistrez-le dans un endroit sûr comme votre gestionnaire de mots de passe par exemple. Vous pouvez également en faire une copie papier.
![IVPN](assets/notext/09.webp)
Sur cette même page, choisissez la durée de votre souscription au service.
![IVPN](assets/notext/10.webp)
Puis sélectionnez votre méthode de paiement. Pour ma part, je vais effectuer le paiement via le Lightning Network, je clique donc sur le bouton "*Bitcoin*".
![IVPN](assets/notext/11.webp)
Vérifiez que tout vous convient puis cliquez sur le bouton "*Pay with Lightning*".
![IVPN](assets/notext/12.webp)
Une invoice Lightning vous sera présentée sur leur BTCPay Server. Scannez le QR code avec votre portefeuille Lightning et procédez au paiement.
![IVPN](assets/notext/13.webp)
Une fois l'invoice payée, cliquez sur le bouton "*Return to IVPN*".
![IVPN](assets/notext/14.webp)
Votre compte apparaît désormais comme "*Active*", et vous pouvez voir la date jusqu'à laquelle votre accès au VPN est valide. Après cette date, vous devrez renouveler votre paiement.
![IVPN](assets/notext/15.webp)
Pour activer votre connexion via IVPN sur votre PC, il suffit de copier votre identifiant de compte.
![IVPN](assets/notext/16.webp)
Et de le coller dans le logiciel précédemment téléchargé.
![IVPN](assets/notext/17.webp)
Puis cliquez sur le bouton "*Login*".
![IVPN](assets/notext/18.webp)
Cliquez sur la coche pour activer la connexion au VPN, et voilà, le trafic Internet de votre ordinateur est désormais chiffré et routé via un serveur d'IVPN.
![IVPN](assets/notext/19.webp)
Pour votre smartphone, la procédure est identique. Collez votre identifiant de compte ou scannez le QR code associé à votre compte IVPN accessible depuis le site web. Ensuite, cliquez sur la coche pour établir la connexion.
![IVPN](assets/notext/20.webp)
## Comment utiliser et configurer IVPN ?

Au niveau de l'utilisation et des paramètres, c'est assez simple. Depuis l'interface principale, vous pouvez activer ou désactiver la connexion simplement en utilisant la coche.
![IVPN](assets/notext/21.webp)
Vous avez également la possibilité de mettre en pause votre VPN pour une durée spécifique.
![IVPN](assets/notext/22.webp)
En cliquant sur le serveur actuel, vous pouvez choisir un autre serveur parmi ceux disponibles.
![IVPN](assets/notext/23.webp)
Il est aussi possible d'activer ou de désactiver le pare-feu intégré ainsi que la fonction anti-traqueur.
![IVPN](assets/notext/24.webp)
Pour accéder aux paramètres supplémentaires, cliquez sur l'icône des paramètres.
![IVPN](assets/notext/25.webp)
Dans l'onglet "*Account*", vous trouverez les paramètres relatifs à votre compte.
![IVPN](assets/notext/26.webp)
Dans l'onglet "*General*", il y a plusieurs paramètres du client. Je vous conseille de cocher les options "*Launch at login*" et "*On launch*" dans la section "*Autoconnect*" pour établir automatiquement la connexion avec le VPN dès le démarrage de votre machine.
![IVPN](assets/notext/27.webp)
Dans l'onglet "*Connection*", vous trouverez diverses options liées à la connexion. C'est ici que vous pouvez modifier le protocole de VPN utilisé.
![IVPN](assets/notext/28.webp)
L'onglet "*IVPN Firewall*" vous permet d'activer le pare-feu systématiquement au démarrage de l'ordinateur, ce qui garantie qu'aucune connexion ne s'établisse hors du VPN.
![IVPN](assets/notext/29.webp)
L'onglet "*Split Tunnel*" offre la possibilité d'exclure certains logiciels de la connexion VPN. Les applications ajoutées ici continueront de fonctionner avec une connexion internet normale même lorsque le VPN est activé.
![IVPN](assets/notext/30.webp)
Dans l'onglet "*WiFi control*", vous avez la possibilité de configurer des actions spécifiques selon les réseaux auxquels vous êtes connecté. Par exemple, vous pouvez définir votre réseau domestique comme "*Trusted*" et configurer le VPN pour qu'il ne s'active pas sur ce réseau, mais qu'il s'active automatiquement sur tout autre réseau WiFi.
![IVPN](assets/notext/31.webp)
Dans le menu "*AntiTracker*", sélectionnez le profil de blocage pour votre anti-traqueur. Celui-ci est conçu pour bloquer les publicités, les logiciels malveillants et les traqueurs de données en bloquant les requêtes vers les services de suivi lors de votre navigation sur Internet. Cela améliore votre confidentialité en empêchant les entreprises de collecter et de vendre vos données de navigation. Un "*Hardcore Mode*" est aussi disponible pour bloquer entièrement tous les domaines appartenant à Google et Meta, ainsi que tous les services qui en dépendent.
![IVPN](assets/notext/32.webp)
Et voilà, vous êtes désormais équipé pour profiter pleinement d'IVPN. Si vous souhaitez également renforcer la sécurité de vos comptes en ligne en utilisant un gestionnaire de mots de passe local, je vous invite à consulter notre tutoriel sur KeePass, une solution gratuite et open-source :

https://planb.network/tutorials/others/general/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Si vous souhaitez découvrir un autre fournisseur de VPN similaire à IVPN, autant en termes de caractéristiques que de tarifs, je vous conseille également de consulter notre tutoriel sur Mullvad :

https://planb.network/tutorials/others/general/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8
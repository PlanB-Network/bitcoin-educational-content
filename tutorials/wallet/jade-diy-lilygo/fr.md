---
name: Jade DIY
description: Transformez une carte de développement de 15 $ en un matériel Bitcoin wallet entièrement fonctionnel
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Construction pour débutants


**Public : ** Constructeurs curieux ayant peu ou pas d'expérience dans le domaine de l'embarqué.


**Durée:** 2 heures (flexible)


**Résultats:** A la fin du cours, les étudiants auront :



- Reconnaître le modèle de sécurité des portefeuilles matériels de bricolage par rapport aux dispositifs commerciaux.
- Assembler un dispositif de signature basé sur un microcontrôleur.
- Flashez un firmware open-source et vérifiez la somme de contrôle de la construction.
- Signer et diffuser une transaction mainnet à l'aide de leur nouvel appareil.


---

## Résumé


Cet atelier de 2 heures apprend aux débutants à construire un matériel Bitcoin wallet fonctionnel en flashant le micrologiciel open-source Jade sur une carte LilyGO T-Display à 15 $. Les étudiants transforment un matériel de développement générique en un dispositif de signature comparable aux portefeuilles commerciaux coûtant 150 $, en apprenant les principes fondamentaux de la sécurité par l'expérience pratique plutôt que par la théorie seule.


### Philosophie


Construire son propre dispositif de signature n'est pas seulement une question d'économie, c'est aussi une question de compréhension de la technologie qui protège votre Bitcoin. Cet atelier privilégie la "sécurité par la compréhension" plutôt que la confiance dans la boîte noire. En s'approvisionnant en composants, en flashant des micrologiciels libres et en générant eux-mêmes de l'entropie, les étudiants réduisent les risques liés à la chaîne d'approvisionnement tout en apprenant à évaluer de manière critique les allégations de sécurité. L'objectif est l'autonomie éclairée : les étudiants doivent comprendre à la fois la puissance et les limites de leur dispositif bricolé par rapport aux alternatives commerciales renforcées.


---

## L'amorce d'un concept (15 min)


### Qu'est-ce que l'autodétention et quelle est son importance ?


Bitcoin a été créé pour éliminer de notre système monétaire le besoin de tiers de confiance, comme les banques et les entreprises. Au lieu de faire appel à la confiance, le bitcoin utilise les mathématiques, la physique et la cryptographie pour permettre à chacun de posséder et de contrôler son argent sans avoir besoin de la permission de qui que ce soit.


Le bitcoin existe sur un grand livre numérique mondial appelé "blockchain" ou "bitcoin timechain". Il s'agit d'un grand livre public et transparent géré par des ordinateurs, et non d'un grand livre centralisé comme un compte bancaire.


Ce qu'il faut comprendre, c'est que pour transférer des bitcoins d'un endroit à un autre, il faut signer la transaction avec ce que l'on appelle une clé privée. C'est comme si vous déverrouilliez un coffre-fort à l'aide d'un mot de passe et que vous transfériez les bitcoins dans le coffre-fort de quelqu'un d'autre. Le Bitcoin vous permet de détenir vous-même les clés de ce coffre-fort, au lieu de compter sur une banque pour déplacer votre argent à votre place.


Un grand pouvoir s'accompagne d'une grande responsabilité : si vous perdez vos clés, vos fonds disparaissent à jamais. On peut donc considérer les clés du coffre-fort comme l'argent lui-même. Bien que les clés ne soient pas la même chose que les bitcoins, elles constituent le mécanisme permettant de déplacer vos fonds et il est donc extrêmement important de les protéger. C'est pourquoi nous disons "pas vos clés, pas vos pièces".


Le terme "autodétention" peut sembler déroutant, mais il signifie simplement que vous détenez vos propres clés privées et que vous contrôlez vos propres bitcoins. Si vous ne détenez pas cette clé, vous faites confiance à quelqu'un d'autre pour la détenir à votre place. Si votre bitcoin se trouve dans un ETF ou sur une bourse (Mt. Gox, FTX, Coinbase, Binance, etc.), vous ne possédez pas de bitcoin, mais une créance sur le bitcoin. ), vous ne possédez pas de bitcoins, mais une créance sur les bitcoins. Cela introduit toutes sortes de risques, comme le piratage des bourses et la perte de vos bitcoins, ou le fait que des entreprises prêtent votre argent et ne vous donnent qu'une fraction de la réserve. En outre, des tiers de confiance auraient le contrôle total de votre argent et pourraient limiter ou geler les retraits.


![image](assets/fr/01.webp)


Avec l'autodétention, la confiance n'a plus lieu d'être. Personne ne peut geler vos fonds ou refuser une transaction, vous pouvez envoyer de l'argent au-delà des frontières, à n'importe qui, à n'importe quel moment, et vous n'avez pas besoin d'un compte bancaire, d'une pièce d'identité ou de l'approbation de qui que ce soit. Personne ne peut vous arrêter, vous censurer ou vous voler, ce qui libère le plein pouvoir du bitcoin en tant qu'argent de la liberté. C'est pourquoi nous disons qu'avec le bitcoin, vous pouvez être votre propre banque.


Bitcoin a été créé pour résoudre le problème de la manipulation de la confiance et de l'argent, pour sortir de notre système actuel, mais la sortie ne fonctionne que si l'on prend les clés. C'est pourquoi l'autodétention est si importante.


### Qu'est-ce qu'un Wallet ?


Le terme wallet est un peu mal choisi et peut donc prêter à confusion. Il est vrai qu'une wallet bitcoin, comme une wallet physique, stocke de la valeur. Mais la principale différence réside dans le fait que les portefeuilles bitcoins ne stockent pas réellement de bitcoins.


Le Bitcoin n'existe qu'en tant qu'entrée du grand livre sur la blockchain publique, ou dans les chambres fortes métaphoriques du cyberespace. Pour déplacer des bitcoins, vous devez utiliser vos clés pour déverrouiller le coffre-fort et déplacer les pièces ailleurs ; ce sont les clés privées qui sont utilisées pour dépenser les bitcoins. Lorsque vous effectuez une transaction avec votre wallet, vous utilisez simplement vos clés pour signer la transaction. C'est ainsi que vous prouvez que vous possédez l'argent et que vous avez le droit de dépenser ces pièces.


Les portefeuilles Bitcoin ne font que stocker vos clés privées, il serait donc plus juste de les appeler des trousseaux de clés.


### Portefeuilles Hot vs Cold


Un hot wallet est une application logicielle installée sur votre téléphone ou votre ordinateur. Elle est connectée à l'internet, ce qui la rend plus facile à utiliser et plus rapide pour signer des transactions, mais cela signifie aussi qu'elle est plus exposée aux pirates, aux logiciels malveillants et à l'hameçonnage. Il est dit "chaud" parce qu'il est connecté à l'internet, qu'il est branché et qu'il est sous tension. Un exemple serait un téléphone wallet ou un navigateur wallet.


En revanche, un wallet froid, ou wallet matériel, est un dispositif qui crée et stocke votre clé hors ligne. Ce dispositif élimine la possibilité pour quelqu'un de pirater vos fonds et est beaucoup plus sûr pour l'épargne à long terme, mais il est nécessaire de signer chaque transaction et peut s'avérer moins pratique.


### Modèle de menace Hardware Wallet


Les portefeuilles matériels existent pour résoudre un problème fondamental : comment signer des transactions Bitcoin sans exposer vos clés privées à un ordinateur connecté à l'internet qui pourrait être compromis par des logiciels malveillants ou des attaquants à distance ? Le modèle de menace principal suppose que votre ordinateur portable ou votre téléphone de tous les jours est potentiellement hostile. Un wallet matériel crée un environnement isolé dans lequel les clés privées ne quittent jamais l'appareil, et la signature de la transaction s'effectue dans un secure element ou un microcontrôleur qui ne communique que la signature à l'ordinateur hôte, et non la clé elle-même. Même si votre ordinateur est complètement compromis, un pirate ne peut pas voler votre Bitcoin sans avoir un accès physique à l'appareil et à votre code PIN.


Cependant, les portefeuilles matériels présentent leurs propres risques. Vous devez être certain que le fabricant n'a pas introduit de portes dérobées, que la chaîne d'approvisionnement n'a pas été altérée et que la génération de nombres aléatoires est réellement aléatoire. Les attaquants physiques peuvent extraire des clés par le biais d'attaques par canal latéral ou de manipulation de la puce, et une personne disposant d'un accès temporaire peut modifier votre appareil. La création de votre propre matériel wallet vous aide à comprendre ces compromis : vous prendrez des décisions concernant les éléments sécurisés par rapport aux microcontrôleurs généraux, la manière de vérifier les transactions sur un écran et la façon de se protéger contre les menaces physiques et à distance. L'objectif n'est pas d'obtenir une sécurité parfaite, mais de comprendre les menaces contre lesquelles vous vous protégez et celles qui subsistent.


### Concepts clés



- Entropie et phrases seed:** Votre wallet n'est aussi sûr que le hasard qui le fait naître. Nous mélangerons le générateur de nombres aléatoires de l'appareil avec des astuces humaines telles que des lancers de dés, nous convertirons cette entropie en une [phrase BIP39] de 12 ou 24 mots (https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), et nous quitterons la pièce avec une sauvegarde écrite ou en métal en laquelle vous avez confiance.
- Hygiène des phrases de semences:** Considérez les seed comme les clés principales de vos économies. Ne tapez jamais les mots sur un téléphone ou un ordinateur - les enregistreurs de frappe, les captures d'écran et les sauvegardes dans le nuage peuvent les divulguer à tout jamais. Conservez la phrase hors ligne, stockez-la dans un endroit auquel vous êtes le seul à pouvoir accéder et entraînez-vous à la relire à voix haute avant de partir.
- Élément sécurisé + microcontrôleur:** Considérez la secure element comme le coffre-fort et le microcontrôleur comme le cerveau. La secure element protège les clés privées en les rendant inviolables, tandis que le microcontrôleur gère l'écran, les boutons et la logique du micrologiciel. Notez que les portefeuilles matériels que nous construisons aujourd'hui n'ont pas de secure element. Cela ne signifie pas qu'ils ne sont pas sûrs, mais simplement qu'ils ont un niveau de protection en moins.
- Faire confiance au firmware:** Le firmware est le système d'exploitation invisible du wallet. Téléchargez toujours des versions étiquetées, vérifiez le hash publié, et comprenez que les versions reproductibles permettent à plusieurs personnes de compiler le même code et d'obtenir exactement le même binaire. Si la somme de contrôle ne correspond pas, vous ne signez pas.


---

## Que construisons-nous ?


Nous prenons du matériel générique, le LilyGo T-Display, et nous flashons le micrologiciel Jade SDK dessus. Le [Jade Plus](https://blockstream.com/jade/jade-plus/) est un wallet à code source ouvert, qui coûte généralement 150 dollars :


![image](assets/fr/02.webp)


Aujourd'hui, nous allons flasher leur firmware sur un matériel à 15$.


### Que faut-il acheter ?


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB avec coque, modèle K164)** - [Commandez directement auprès de LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) pour environ $15. Cette carte ESP32 fournit l'affichage, les boutons et l'interface USB qui reflètent le Jade Plus de Blockstream. L'ESP32 embarquée comprend également des radios Wi-Fi et Bluetooth ; nous fournirons un micrologiciel qui les maintient désactivées, mais elles façonnent votre modèle de menace car un code malveillant pourrait les réactiver.
- Câble USB-C** - Apportez un câble compatible avec les données afin de pouvoir flasher le firmware et alimenter la carte directement depuis votre ordinateur portable (tout à fait correct pour une utilisation en classe).


### Pourquoi construire votre propre Hardware Wallet ?



- Économisez environ 135 $ par rapport à l'achat d'un appareil commercial.
- Il faut se familiariser avec le clignotement du micrologiciel, les éléments sécurisés et l'hygiène wallet.
- Activez des dispositifs de signature supplémentaires pour répartir les économies sur plusieurs portefeuilles.
- Réduisez les risques liés à la chaîne d'approvisionnement en achetant et en assemblant vous-même chaque composant.
- Gardez à l'esprit le mantra de Lopp : la souveraineté et la commodité sont toujours en conflit.


## Configuration physique


### Préparez votre dossier


Vous avez deux options pour loger votre carte LilyGO T-Display : un boîtier imprimé en 3D ou le boîtier officiel LilyGO. Le boîtier imprimé peut être trouvé et imprimé à partir de [ce modèle](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Il offre une coque légère et personnalisable pour votre appareil.


![image](assets/fr/04.webp)


Vous pouvez également utiliser l'étui officiel de LilyGO, qui présente une forme et une finition légèrement différentes, offrant une protection plus robuste et un aspect plus soigné.


![image](assets/fr/05.webp)


Notez que les boîtiers imprimés et officiels diffèrent légèrement en termes de conception et d'assemblage. Quelle que soit l'option choisie, assurez-vous que la carte est correctement placée dans le boîtier afin d'éviter les connexions lâches ou les dommages.


### Inspecter le conseil d'administration


Avant de poursuivre, inspectez soigneusement votre carte LilyGO T-Display pour vérifier qu'elle ne présente pas de défauts ou de débris visibles. Vérifiez que l'écran, les boutons et le port USB-C sont propres et exempts de poussière ou de projections de soudure. Manipulez la carte avec précaution et respectez la sécurité contre les décharges électrostatiques (ESD) en vous mettant à la terre ou en utilisant un bracelet ESD pour éviter d'endommager les composants sensibles.


### Connexion à votre ordinateur portable


À l'aide d'un câble USB-C compatible avec les données, connectez la carte LilyGO à votre ordinateur portable. Cette connexion fournira de l'énergie et vous permettra de flasher le micrologiciel.


Au démarrage, l'écran suivant s'affiche :


![image](assets/fr/06.webp)



Lorsqu'il est mis sous tension, le LilyGO affiche un écran de test couleur qui passe d'une couleur à l'autre. Cela permet de confirmer que l'écran et la carte fonctionnent correctement avant de procéder au flashage du micrologiciel.


Une fois le test de couleur terminé, l'écran se met dans un état par défaut, indiquant que la carte est prête pour les étapes suivantes du processus de construction.


![image](assets/fr/07.webp)


## La voie facile ou la voie Hard


Il existe deux approches principales pour flasher le micrologiciel de votre matériel wallet : la méthode facile et la méthode difficile. La méthode facile utilise des outils pré-configurés ou des flashers basés sur le web qui chargent automatiquement le micrologiciel sur votre appareil avec un minimum de données. Cette méthode est idéale pour les débutants qui veulent gagner rapidement ou qui préfèrent éviter les complexités du débogage et des interactions en ligne de commande. Elle simplifie le processus et vous permet d'être opérationnel plus rapidement, ce qui la rend accessible à ceux qui ne connaissent pas encore le développement intégré ou les portefeuilles matériels.


La méthode difficile, en revanche, consiste à utiliser manuellement des outils de ligne de commande pour flasher le microprogramme. Cette approche nécessite de vérifier les signatures et les sommes de contrôle du microprogramme afin d'en garantir l'authenticité et l'intégrité, ce qui permet de mieux comprendre le processus de flashage et la manière dont le microprogramme interagit avec le matériel. Bien qu'elle demande plus d'efforts et de familiarité avec les commandes de terminal, elle offre plus de contrôle, de transparence et de confiance dans la sécurité de votre appareil.


Chaque méthode a ses avantages : la méthode facile sacrifie un certain degré de confiance et de compréhension au profit de la rapidité et de la commodité, tandis que la méthode difficile exige plus de temps et de compétences techniques, mais vous récompense par sa flexibilité et une meilleure compréhension de la technologie sous-jacente. Les formateurs doivent encourager les étudiants à choisir la voie qui correspond le mieux à leur niveau de confort et à leur curiosité, en favorisant à la fois la confiance et l'exploration.


## La méthode facile


La façon la plus simple de flasher un ESP32



- Allez sur le Github officiel de Blockstream : [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Vous pouvez télécharger le fichier source et exécuter le site web localement, mais GitHub l'héberge déjà à l'adresse [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub fournit le HTML, le CSS, le JavaScript, etc. directement à votre navigateur afin que vous puissiez flasher l'appareil sans installer d'outils de développement.


![image](assets/fr/09.webp)



- Ouvrez le menu déroulant (la valeur par défaut est probablement `M5Stack Core2`) et sélectionnez votre carte de développement - pour cette classe, choisissez `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Lorsque vous cliquez sur flash, vous verrez apparaître ceci. Pour savoir quel appareil est le LILYGO, débranchez le LILYGO et rebranchez-le. Le port COM du Lilygo apparaîtra et disparaîtra. Cliquez sur le port COM sur lequel le Jade est branché


![image](assets/fr/11.webp)



- Une barre de progression doit s'afficher et une fois qu'elle est terminée, vous êtes prêt à l'installer


## Installation du Jade Wallet


Une fois que le micrologiciel a été flashé avec succès, votre LilyGO T-Display est maintenant un Jade hardware wallet entièrement fonctionnel. Cette section vous guidera dans le processus de configuration initiale, depuis la création de votre phrase seed jusqu'à la connexion de l'appareil avec le logiciel wallet comme Sparrow ou l'application mobile Blockstream Green.


### Démarrage initial et configuration des périphériques



- Allumez l'appareil :** Le LilyGO étant toujours connecté à votre ordinateur portable via l'USB-C, le micrologiciel Jade devrait démarrer automatiquement. Vous verrez le logo Jade apparaître sur l'écran.



- Entrer dans le mode de configuration:** L'appareil vous présentera un menu initial. Utilisez les deux boutons physiques de la carte pour naviguer :
 - Bouton gauche:** Déplacer vers le haut/vers l'arrière
 - Bouton droit:** Déplacer vers le bas/vers l'avant
 - Les deux boutons simultanément:** Sélectionner/confirmer



- Sélectionnez "Setup":** Naviguez jusqu'à l'option Setup et appuyez sur les deux boutons pour confirmer. L'appareil vous guidera tout au long du processus de configuration initiale.


### Création de votre Wallet



- Choisissez "Begin Setup":** L'appareil vous demandera de commencer le processus de création de wallet. Confirmez votre choix.



- Sélectionnez "Créer un nouveau Wallet":** Deux options s'offrent à vous :
 - Créer une nouvelle phrase Wallet:** Génère une nouvelle phrase seed (à choisir pour l'atelier)
 - Restaurer Wallet:** Récupérer un wallet existant à partir d'une phrase seed (pour les utilisateurs avancés)



- Sélectionnez "Créer un nouveau Wallet" et confirmez.



- Générer de l'entropie:** L'appareil utilise son générateur de nombres aléatoires pour créer de l'entropie cryptographique. Ce processus prend quelques secondes, car l'appareil recueille des données aléatoires provenant de plusieurs sources.


### Enregistrement de la phrase d'amorçage



- Ecrivez votre phrase seed:** L'appareil va maintenant afficher une phrase seed de 12 mots du BIP39, un mot à la fois. Il s'agit de l'étape la plus critique de tout le processus.


**Pratiques de sécurité importantes:**


- Écrivez clairement chaque mot sur une feuille de papier (utilisez les cartes de phrases seed si vous en avez)
- Vérifiez chaque mot au fur et à mesure que vous l'écrivez
- Ne photographiez jamais la phrase seed avec votre téléphone
- Ne jamais taper les mots sur un ordinateur ou un téléphone
- Gardez votre phrase seed privée - ne partagez pas votre écran et ne la montrez pas à d'autres personnes



- Vérifier votre phrase seed:** Après avoir écrit les 12 mots, l'appareil vous demandera de confirmer plusieurs mots de la phrase pour s'assurer que vous les avez enregistrés correctement. Utilisez les boutons pour sélectionner le mot correct pour chaque demande.


**Conseil professionnel:** Avant de poursuivre, entraînez-vous à relire votre phrase seed à haute voix (à voix basse, pour que les autres n'entendent pas). Cela permet de repérer les erreurs d'écriture ou les ambiguïtés.


### Méthode de connexion



- Choisir le type de connexion:** Le micrologiciel Jade prend en charge deux méthodes de connexion :
 - USB:** Connexion filaire via un câble USB-C (recommandé pour cet atelier)
 - Bluetooth:** Connexion sans fil aux appareils mobiles



- Sélectionnez **USB** pour l'instant, car il s'agit de l'option la plus simple pour les logiciels wallet de bureau et elle n'introduit pas de vecteurs d'attaque sans fil.



- Nommage des appareils:** Le Jade affichera un identifiant unique comme "Connect Jade A7D924". Cet identifiant vous permet de distinguer plusieurs portefeuilles matériels si vous en construisez plusieurs. Notez cet identifiant si vous le souhaitez.


### Connexion au logiciel Wallet


Vous avez maintenant deux options principales pour interfacer avec votre nouveau matériel wallet : l'application mobile Blockstream Green (pour une utilisation mobile) ou Sparrow Wallet (pour une utilisation de bureau avec des fonctionnalités plus avancées). Pour cet atelier, nous nous concentrerons sur Sparrow Wallet, car il offre une meilleure visibilité sur les détails techniques des transactions Bitcoin.


#### Option 1 : Application mobile Blockstream Green (démarrage rapide)


Si vous souhaitez tester rapidement votre appareil avec un appareil mobile :



- Téléchargez l'application **Blockstream Green** depuis l'App Store (iOS) ou Google Play (Android)
- Ouvrez l'application et sélectionnez "Connect Hardware Wallet"
- Choisissez "Jade" dans la liste des appareils pris en charge
- Branchez votre Jade sur votre téléphone à l'aide d'un câble USB-C à USB-C (ou d'un adaptateur USB-C à Lightning pour iPhone 15+)
- Suivez les instructions à l'écran pour vous connecter et créer votre première wallet


**Note sur le Liquid:** L'application Blockstream Green supporte à la fois le Bitcoin et le Liquid (une chaîne latérale du Bitcoin). Si vous utilisez les fonctionnalités de la Liquid, vous pouvez être invité à "Exporter la clé d'aveuglement principale" - cela permet à l'application de voir les montants des transactions sur le réseau Liquid, qui sont autrement confidentiels. Pour cet atelier, vous pouvez ignorer les fonctionnalités Liquid et vous concentrer sur les transactions Bitcoin standard.


#### Option 2 : Sparrow Wallet (recommandé pour les ateliers)


Sparrow Wallet est une puissante application de bureau qui vous donne un contrôle granulaire sur vos transactions Bitcoin et se connecte de manière transparente à votre matériel Jade wallet.


**Installation:**



- Téléchargez Sparrow Wallet depuis le site officiel : [sparrowwallet.com](https://sparrowwallet.com)
- Vérifier la signature du téléchargement (voir la documentation Sparrow pour plus de détails)
- Installer et lancer l'application


**Connecter votre Jade à Sparrow:**



- Dans Sparrow, allez dans **Fichier → Nouvelle Wallet**
- Donnez un nom à votre wallet (par exemple, "My Jade Wallet")
- Cliquez sur **Connecté Hardware Wallet**
- Le Sparrow devrait automatiquement détecter votre appareil Jade branché
- Si vous y êtes invité, confirmez la connexion sur l'écran Jade en appuyant sur les deux boutons
- Sélectionnez le type de script souhaité :
 - Native Segwit (P2WPKH):** Recommandé pour les débutants - frais les plus bas, compatibilité la plus large avec les portefeuilles modernes
 - Nested Segwit (P2SH-P2WPKH):** Pour la compatibilité avec les anciens services
 - Taproot (P2TR):** La solution la plus avancée, qui offre la meilleure protection de la vie privée et les tarifs les plus bas, mais qui nécessite un support wallet de pointe
- Cliquez sur **Import Keystore** pour terminer la connexion


**Configuration de la connexion au serveur de Sparrow:**


Avant que vous puissiez voir votre solde ou diffuser des transactions, Sparrow doit se connecter à un nœud Bitcoin pour récupérer les données de la blockchain. Plusieurs options s'offrent à vous, chacune avec des compromis différents entre la commodité, la confidentialité et la confiance :



- Electrum Server public (le plus facile, le moins privé):** Se connecte à un serveur public géré par un tiers. Rapide à mettre en place, mais le serveur peut voir les adresses de vos wallet et potentiellement les relier à votre adresse IP. Idéal pour les tests sur testnet.
 - Dans Sparrow, allez dans **Outils → Préférences → Serveur**
 - Sélectionnez **Serveur public** et choisissez un serveur dans la liste
 - Cliquez sur **Tester la connexion** pour vérifier



- Bitcoin Core or Knots Node (Most private, most work):** Exécutez votre propre nœud Bitcoin complet. C'est l'étalon-or pour la confidentialité et la vérification, car vous validez chaque transaction vous-même et ne faites pas confiance au serveur de quelqu'un d'autre. Cependant, cela nécessite de télécharger la blockchain complète (~600GB) et de maintenir votre nœud synchronisé.
 - Installer et synchroniser les noyaux ou les nœuds Bitcoin
 - Dans Sparrow, allez dans **Outils → Préférences → Serveur**
 - Sélectionnez **Bitcoin Core ou Knots** et entrez les détails de connexion de votre nœud



- Private Electrum Server (Good balance):** Hébergez votre propre serveur Electrum (comme Fulcrum ou Electrs) connecté à votre nœud Bitcoin Core ou Knots. Offre une confidentialité totale sans avoir besoin de faire tourner Sparrow sur la même machine que votre nœud.
 - Configurez un serveur Electrum pointant vers votre nœud Bitcoin Core ou Knots
 - Dans Sparrow, allez dans **Outils → Préférences → Serveur**
 - Sélectionnez **Privé Electrum** et entrez l'URL de votre serveur


Pour cet atelier, l'utilisation d'un **Electrum Server public** convient parfaitement pour les transactions du réseau de test. Dans un environnement de production avec des fonds réels, vous devriez envisager de gérer votre propre nœud ou d'utiliser un serveur privé de confiance pour une confidentialité maximale.


#### Option 3 : Blockstream Green Desktop App (Quick Start)


Blockstream Green est le logiciel qui permet de terminer la configuration de JadeDIY et qui doit être utilisé avec la version de bureau



- Procurez-vous l'application officielle de Blockstream - voici le lien vers cette application sur leur site web. Une fois sur le site, cliquez sur [Download now](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- En fonction de l'emplacement de vos téléchargements, le fichier se trouvera probablement dans votre dossier Téléchargements. Vérifiez-le et double-cliquez sur le fichier exécutable pour installer le logiciel.


![image](assets/fr/13.webp)



- Il se peut que vous deviez donner des droits d'administrateur pour lancer le programme d'installation. Une fois que vous l'aurez fait, une fenêtre s'ouvrira, qui devrait ressembler à l'image suivante - cliquez sur **Suivant**.


![image](assets/fr/14.webp)



- Choisissez l'emplacement de l'application installée (un emplacement avec vos autres programmes ou un endroit facile à trouver), puis cliquez sur **Suivant**.


![image](assets/fr/15.webp)



- Le programme d'installation vous demandera un nom de raccourci. Saisissez-en un ou conservez le nom par défaut, puis cliquez sur **Suivant**.


![image](assets/fr/16.webp)



- Si vous souhaitez un raccourci sur le bureau, cochez la case ; sinon, cliquez sur **Suivant**.


![image](assets/fr/17.webp)



- Enfin, cliquez sur **Installer** et attendez quelques minutes que l'installation soit terminée.


![image](assets/fr/18.webp)



- La barre de progression doit se remplir jusqu'à la fin.


![image](assets/fr/19.webp)



- Lorsqu'il est terminé, une nouvelle page s'affiche - cliquez sur **Finish**.


![image](assets/fr/20.webp)



- Recherchez l'application Blockstream que vous venez d'installer (exemple dans le menu Démarrer de Windows 11).


![image](assets/fr/21.webp)



- Une fois que vous l'avez trouvé, cliquez pour le lancer - un écran de démarrage devrait apparaître.


### Vérification de la configuration


Une fois connecté à Sparrow (ou à une autre application wallet) :



- Vérifiez vos adresses:** Sparrow affichera les adresses de réception dérivées de votre phrase seed. Vous pouvez vérifier une adresse sur votre appareil Jade en allant sur l'onglet "Recevoir" dans Sparrow et en cliquant sur "Afficher Address" - l'adresse devrait apparaître à la fois sur l'écran de votre ordinateur et sur l'écran Jade.



- Générer une adresse de réception:** Cliquez sur l'onglet **Réception** dans Sparrow et copiez votre première adresse de réception Bitcoin.



- Prêt pour les transactions:** Votre matériel wallet est maintenant entièrement configuré et prêt à recevoir et à signer des transactions Bitcoin. Passez à la section suivante pour vous entraîner à signer une transaction testnet.



---

### Liste de contrôle pour l'installation rapide



- Le firmware Jade démarre avec succès
- Nouveau wallet créé avec une phrase de 12 mots seed
- Phrase de semence écrite clairement et vérifiée
- Mode de connexion USB sélectionné
- Logiciel Wallet (Sparrow) installé et connecté
- Connexion serveur configurée (Electrum public pour mainnet)
- Première adresse de réception générée et vérifiée sur l'appareil



---

**Licence MIT**


**Copyright (c) 2025 Le réseau Bitcoin NYC**


L'autorisation est accordée par la présente, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le "Logiciel"), de traiter le Logiciel sans restriction, y compris sans limitation les droits d'utiliser, de copier, de modifier, de fusionner, de publier, de distribuer, d'accorder des sous-licences et/ou de vendre des copies du Logiciel, et d'autoriser les personnes à qui le Logiciel est fourni à faire de même, sous réserve des conditions suivantes :


L'avis de droit d'auteur ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les copies ou parties substantielles du logiciel.


LE LOGICIEL EST FOURNI "TEL QUEL", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET D'ABSENCE DE CONTREFAÇON. EN AUCUN CAS, LES AUTEURS OU LES DÉTENTEURS DES DROITS D'AUTEUR NE PEUVENT ÊTRE TENUS RESPONSABLES D'UNE QUELCONQUE RÉCLAMATION, D'UN QUELCONQUE DOMMAGE OU D'UNE QUELCONQUE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DU LOGICIEL, DE SON UTILISATION OU D'AUTRES OPÉRATIONS LIÉES AU LOGICIEL.


---
---
name: Mise en place d’un nœud Bitcoin & Lightning
goal: Mise en place d’un noeud Bitcoin et Lightning via Umbrel. Analyse de la blockchain, création et gestion de canaux.
---

Un voyage vers le côté technique de Bitcoin

:[affiche du cours](BTC101_vignette-presentation-front.png)

Voici la formation pratique Lightning Network et BTC !

Étant plus poussée techniquement, il est idéal d’avoir quelques bases sur Bitcoin :

    Comprendre comment fonctionnent les portefeuilles Bitcoin.
    Comprendre le principe de transaction, mineur et blockchain.

Cette formation est donc pour montrer le cas concret, réel, palpable de Bitcoin et du Lightning Network. On se salit les mains ! Ceci reste accessible pour tous et pas besoin de savoir coder.

Qu’allez-vous apprendre durant ce cours ?
N
La mise en place d'un nœud Bitcoin
N
L'utilisation d'un nœud Bitcoin
N
Utilisation d'un nœud Lightning Network

L’objectif final de cette formation est d’avoir une très bonne compréhension du protocole Bitcoin. Vous aurez, si vous le souhaitez, des canaux Lightning bien connectés, un portefeuille extrêmement sécurisé et même votre propre serveur de paiement BTCPay Server.

Le curriculum complet: LN 202 – Curriculum

Pas convaincu ? Tu peux regarder le curriculum complet ici: [BTC 101 - Curriculum](https://academie.decouvrebitcoin.fr/wp-content/uploads/2022/07/BTC-101-Curriculum.pdf)

contributeur financier au lancement:

Contributeurs : Drikxe, Thomas, Samuel, Fabrice, Marco, OsyGeni, Gregory, Fabien, Lounès

Team créateur

        Loïc Morel – Création & production
        Rogzy – Coordination
        Rachel – Communication
        Pantamis – Interview
        WillKek – Chapitrage

---

A propose du prof.

Rogzy

Salut !

Bitcoin est un outil de libération financière. En apprenant à l’utiliser, vous pouvez devenir votre propre banque, sortir du système traditionnel et regagner le contrôle de votre épargne. La révolution Bitcoin est déjà en marche et ne peut plus être arrêtée.

À travers ce contenu gratuit, vous aurez toutes les cartes pour vous lancer et réussir à devenir un citoyen souverain et libre au 21ème siècle.

À votre tour de vous lancer. Mes DM sont toujours ouvert si vous avez des questions !

Rogzy

Team contributeur:

        Rogzy – production
        Lounes – aide technique
        Silexperience – design
        Sarah  – Thumbnails

---

Matériel prérequis

Nous allons créer nous-même notre nœud Bitcoin, ouvrir des canaux Lightning et essayer un portefeuille multi-signature. Ceci a un coût matériel non négligeable pour certaines personnes. Sachez que la totalité de la formation peut être suivie SANS le matériel. Vous ne serez pas perdu(e) si vous n’avez pas votre propre nœud.

Si vous avez envie de vous lancer, voici les produits (lien affiliation) :

    Carte SD 16Go – https://amzn.to/3Qi2Opm
    Raspberry Pi 4 – https://amzn.to/3qoSUYl
    SSD 1To – https://amzn.to/3jSvjLC​
    Boîtier Externe pour Disque Dur – https://amzn.to/3x5R02S
    RASPBERRY Alimentation – https://amzn.to/3D36zvM
    Raspberry Pi FLIRC Case – https://amzn.to/3TNllgi

Si vous êtes passé(e) par les liens d’affiliations, merci de votre soutien ! Vous permettez à ce projet de survivre et proposer toujours plus de formations et de contenus éducationnels.

D’autre solution deja toute faite existe !

-> Mettre les liens

---

Curriculum:

## introduction et disclaimer

## update des changements

# Section 1 : Noeud Bitcoin

## Chapitre 1 – Devenir un Bitcoiner souverain

![Lancement de la formation](https://youtu.be/NF3SHhE1PFw?list=PLinTFKehfR4zoKvBcncHPr-ZTh1enuEhr)

## Chapitre 2 – Qu’est-ce qu’un nœud Bitcoin ?

![qu'est ce qu'un noeud?](https://youtu.be/19YgL9vkHh4)

Les nœuds Bitcoin représentent le réseau Bitcoin. C’est donc le logiciel Bitcoin qui tourne sur une machine et qui se connecte à l’autre membre du réseau. Ensemble, ils forment Bitcoin en agissant sur les mêmes règles. Un nœud à différentes fonctions :

    Garder un historique complet de la blockchain Bitcoin, environ 300GB en 2021
    Recevoir et envoyer toutes les nouvelles transactions du réseau, ces transactions sont stockées dans la MemPool du nœud
    Participer à la gouvernance du réseau en respectant le consensus Bitcoin

Un nœud permet donc d’avoir plus de vie privée, de se séparer de potentiels intermédiaires de confiance et d’avoir plus de décentralisation dans Bitcoin.

Un nœud ne permet pas de miner du bitcoin ou de gagner de l’argent.

Ici, Umbrel via un Rasperrie Pi permettra également d’avoir un nœud Lightning Network.

## Chapitre 3 – Tutoriel nœud Bitcoin via Umbrel

![Tuto umbrel](https://youtu.be/mr4iTzdTczI)

Matériel prérequis

Dans cette formation, nous allons créer nous-même notre nœud Bitcoin, ouvrir des canaux lightning et essayer un portefeuille multi-signature.

Ceci a un coût matériel non négligeable pour certaines personnes. Sachez que la totalité de la formation peut être suivie SANS le matériel. Vous ne serez pas perdu si vous n’avez pas votre propre nœud.

Si vous avez envie de vous lancer, voici les produits (liens d’affiliations) :

    Boitier disque dur externe – https://amzn.to/3rXmAKV​
    Carte SD 16Go – https://amzn.to/2NApPsM​
    Raspberry Pi 4 – https://amzn.to/2Nr5SVr​
    SSD 1To – https://amzn.to/3jSvjLC​
    Source d’alimentation – https://amzn.to/3ao4FqU
    Boitier Pi – https://amzn.to/2Zp3e5d

Si vous êtes passé par les liens d’affiliations, merci de votre soutien ! Vous permettez à ce projet de survivre et proposer toujours plus de formations et de contenus éducationnels.

Que faut-il pour faire tourner son nœud Bitcoin ?

    La blockchain est d’environ 300GB, il faut donc prévoir de l’espace
    La connexion internet doit être constante avec environ 30G de bande passante par mois
    Il faut de la RAM pour faire tourner BTC Core
    Il faut plus de RAM si l’on fait tourner Umbrel et un nœud LN (minimum 4)

Vous pouvez donc faire tourner votre nœud Bitcoin directement sur votre ordinateur ou utiliser un système comme sur la vidéo avec un Rasperrie Pi.

## Chapitre 4 – Overview de Umbrel

![umbrel overview](https://youtu.be/cwEa61BgemM)

Résumé :

Umbrel est un logiciel qui permet de faire tourner BTC Core et un nœud Lightning Network facilement. Une interface utilisateur agréable y est intégrée et cette dernière possède de nombreuses fonctionnalités :

    Gestion de nœud Lightning Network
    Intégration BTCPay
    MemPool
    Block Explorer
    Etc…

C’est avec ce logiciel que nous allons explorer le reste du cours.

## Chapitre 5 – Analyse de la MemPool

![mempool](https://youtu.be/0xS859IoMh8)

Résumé :

La MemPool est l’endroit dans votre nœud Bitcoin où toutes les transactions de bitcoins attendent d’être confirmées dans un bloc. C’est donc une énorme salle d’attente où les transactions sont stockées. Le nœud reçoit une transaction, vérifie si elle est valide et la stock sur la MemPool si c’est le cas. Une fois dans la MemPool, elle attend d’être inscrite dans un bloc par un mineur. Lorsque la transaction est dans le bloc, elle est retirée de la MemPool car elle est désormais inscrite dans la blockchain. Tout le monde possède une MemPool différente et indépendante car chaque nœud est unique.

## Chapitre 6 – Block Explorer & Analyse Stats

![block explorer et analyse stat](https://youtu.be/Qe9VaUhUS0E)

Résumé :

Votre nœud entier Bitcoin vous donne accès à l’intégralité de l’historique des transactions bitcoin. Via un block explorer, vous pouvez donc analyser cette donnée et auditer le passé. Lorsqu’une transaction est dans un bloc, elle devient immuable dans le temps. Vous pouvez alors être certain que ce que vous voyez depuis votre nœud Bitcoin sont des âmes écrites dans l’histoire, n’en déplaise à Big Brother. Le passé ne peut être modifié. Les blocs explorer peuvent donc vous donner des stats sur les transactions, l’utilité du réseau, les blocs, les utilisateurs, les mineurs et bien d’autres données. C’est un outil indispensable pour des analystes.

## Chapitre 7 – Connecter son portefeuille à son nœud

![connecter osn portefeuille à son noued](https://youtu.be/HOV3bVcram4)

Résumé :

Votre nœud complet Bitcoin vous permet de couper les intermédiaires de confiance entre votre portefeuille et le réseau Bitcoin. Vous devez donc connecter votre portefeuille mobile ou logiciel desktop à votre nœud. Ceci se fait via des manipulations relativement simples et accessibles à tous. Une fois connecté, votre portefeuille transmettra les transactions via votre propre nœud/serveur Bitcoin.

## Chapitre 8 – Les Portefeuille multi-sig via Specter

![les portefeuille multi sig](https://youtu.be/mV1KS-Uwjew)

Résumé :

Un portefeuille multi-signature permet de diviser l’accès au coffre-fort Bitcoin par différentes clés privées. C’est un système de sécurité poussé pour sourcer de larges sommes. Le but est de rendre l’accès à l’argent difficile. Cela pourrait empêcher de potentielles attaques à 5€ ou qu’un de vos associés parte avec l’argent. Les portefeuilles multi-sig peuvent prendre de nombreuses formes. Par exemple, 2 clés sur 3 ou 3 clés sur 5 sont standards dans l’industrie. A la création de votre portefeuille multi-sig, vous devrez choisir : – le nombre de clés à la création – le nombre de clés nécessaires pour avoir accès ou déplacer l’argent Par exemple, 2 clés sur 3 ou 3 clés sur 5 sont standards dans l’industrie.

# Section 2 : Lightning Network

## Chapitre 9 – Ouverture de canaux

![ouverture de canaux](https://youtu.be/bAZJn0AH1yU)

L’ouverture d’un canal Lightning se fait avec une adresse Lightning directement via l’intervalle de Umbrel sous LN ou en utilisant une application comme ThunderHub.

Voici la mienne : 02f1dd194c270b5ffeb9f3418ab5bd37e20e85107d97d0285ccdfebf5ee62c397b@nnqvu5yssejj2sthtnzwjxffv32pqsz3elynhrypzrp5f5gmofpijzad.onion:9735

Les frais sont donc une transaction on-chain donc profitez que la MemPool soit vide pour ouvrir des canaux. Une fois un canal ouvert, la liquidité est bloquée d’un côté du canal. Afin de la déplacer de l’autre côté, nous allons procéder à un LOOP. Dans le Lightning Network, il y a des frais de routage. Si un canal se fait vider trop vite, vous pouvez les augmenter.

On n’oublie pas de sauvegarder l’état de ces canaux et on pense aux watch tower.

## Chapitre 10 – Gestion des canaux LN

![gestion des canaux LN](https://youtu.be/CgBnGQLar4o)

Résumé :

La gestion de Canaux LN n’est pas forcément simple, il faut faire attention à la liquidité et savoir rééquilibrer cette dernière. Des solutions comme Loop ou le rebalancing existe pour remplir cette tâche. Afin d’analyser nos canaux, le routage et le reste, nous utilisons des solutions comme Ride The Lightning et ThunderHub. Nous regarderons ici comment les utiliser. Le plus important dans cette vidéo est la section des frais. Dans le LN, il existe 2 type de frais : les frais fixes pour chaque routage et les frais variables en pourcentage ppm du montant routé. On va regarder comment les modifier et bien les comprendre. La sécurité dans LN est différente de celle on-chain, il faut donc comprendre les closes de fermeture et l’utilisation de WatchTower.

## Chapitre 11 – Renommer son nœud LN

![renommer son noeud LN](https://youtu.be/HnK1_TDYXsY)

Résumé :
Changer l’alias de votre nœud LN permet aux gens de vous reconnaitre dans le réseau, et puis c’est cool. On va donc regarder comment faire via des lignes de commande : Pour voir les instructions, clique ici ! Sinon, voici le processus :

    Ouvrez le terminal
    Tapez ssh -t umbrel@umbrel.local
    Entrez le mot de passe de votre Umbrel (on ne voit pas le mot de passe)
    Tapez sudo nano umbrel/lnd/lnd.conf
    Tapez votre mot de passe à nouveau
    Sous la section « Application Options », rajoutez la ligne alias=SOMENAME et changez le SOMENAME par votre nom. On peut descendre de 12 flèches vers le bas pour taper. Cliquer sur un terminal ne sert à rien.
    Validez avec ctr-X
    Validez avec Y
    Validez avec entrer

Relancez votre Umbrel via le menu setting de l’interface. Et voilà, vous avez changé votre nom. Vous pouvez désormais claim votre nœud sur 1ML ou Amboss : 1ML – Vous devez ouvrir un canal avec le montant indiqué 👉 Mon 1ML : https://1ml.com/node/02f1dd194c270b5ffeb9f3418ab5bd37e20e85107d97d0285ccdfebf5ee62c397b Ambos – Vous devez signer une transaction avec votre nœud LN (faites-le depuis l’interface de ThunderHub sous tools, message signé) 👉 Mon Amboss : https://amboss.space/node/02f1dd194c270b5ffeb9f3418ab5bd37e20e85107d97d0285ccdfebf5ee62c397b 👉 Connecte ton nœud avec le mien ! 02f1dd194c270b5ffeb9f3418ab5bd37e20e85107d97d0285ccdfebf5ee62c397b@nnqvu5yssejj2sthtnzwjxffv32pqsz3elynhrypzrp5f5gmofpijzad.onion:9735 Bonne chance !

## rate formation

## Chapitre 12 – Utilisation concrète du LN

![utilisation du LN](https://youtu.be/6yekAvH13E0)

Résumé :
L’utilisation du Lightning Network peut être très simple avec des portefeuilles gratuits comme Wallet for Satoshi ou Blue Wallet. Ici, on utilise le wallet LN directement depuis Umbrel pour payer des invoice LN. Dans ce chapitre, on va donc payer des demandes à 1 SAT en passant par des nœuds intermédiaires et par notre propre canal. Finalement, on se rend compte que via le LN, on peut payer 0 frais lors de l’envoi instantané de microtransactions. Ici, on s’amuse à payer 1 SAT par pixel par exemple.

## Chapitre 13 – LN Market

video non existante

## Chapitre 14 – Accepter Bitcoin avec BTCpay serveur

![accepter bticoin dans son commerce](https://youtu.be/zpCMlLfiRgg)

Dans ce dernier chapitre de la formation, nous allons regarder comment c’est possible d’accepter Bitcoin pour son commerce. Nous regardons 2 options et 2 nœuds différents. Le premier est BTCPay serveur via notre Umbrel, pui BTCPay via un nœud Luna externe et enfin via OpenNode. Il y a toujours des variations entre les 3 et ceci doit être pris en compte par rapport à vos besoins : – Un restaurateur avec son Umbrel dans l’établiseement peut utiliser BTCpayer directement sous Tor – Un e-commerce ne peut pas utiliser le BTCPay sous Tor de son nœud Umbrel donc il utilisera un nœud externe en clear net comme un Luna Node – Une solution comme OpenNode permet d’avoir une solution tout en un facile pour ne pas se prendre la tête. C’est complexe donc nous allons le traiter dans une formation indépendante. Voici les liens : – OpenNode : https://www.opennode.com/ – BTCPay Server : https://btcpayserver.org/ – Luna Node : https://www.lunanode.com/ et https://docs.btcpayserver.org/Deployment/LunaNode/

J’ai également pu interviewer Nicolas Dorier, le créateur de BTCPay Server ! Pour ceux que ça intéresse, cliquez ici.

## conclusion

![conclusion](https://youtu.be/QrKbagtUE1s)

Et c’est la fin de la formation n°2 !

Nous avons vu dans un premier temps les fondamentaux d’un nœud Bitcoin, puis comment fonctionne la blockchain Bitcoin via la MemPool et les Block Explorer. La deuxième partie était plutôt sur le LN avec du routage, gestion de liquidité et utilisation du LN. On a terminé dans la souffrance avec LN Market (soon) et BTC Pay Serveur (prochaine formation).

J’ai pas mal appris sur la production depuis donc on fera moins d’erreurs pour la prochaine. J’espère que vous avez appris plein de trucs et que vous êtes satisfaits de l’avoir suivie. Comme promis, elle est 100% gratuite, 14 chapitres avec 14 quiz dispos sur le site et la semaine pro sur le Teachable.

Si vous voulez soutenir ce genre de projet gratuit, c’est via le Patreon ou sur le site marchand qui sort bientôt pour acheter votre blason/diplôme Umbrel. Et oui, chez moi on achète le diplôme car dans tout les cas, l’important ce n’est pas le voyage mais la destination. Diplôme sans valeur c’est vrai, mais c’est toujours fun d’avoir un truc sur le mur.

Si vous avez fini et exécuté la formation, un grand bravo ! Vous êtes un bon bitcoiner et faites parti des 0,001% des français bitcoiner (on ne doit pas être plus de 3 000).

Merci à vous d’être restés jusqu’au bout et on se revoit très vite pour la prochaine formation !

## allez plus loins

Comment nous soutenir et aller plus loin !

N’hésitez pas à vous abonnez à notre newsletter, ça fait toujours plaisir ! Pour ceux qui souhaitent nous soutenir, ça se passe sur le Patreon !

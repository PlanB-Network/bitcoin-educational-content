---
name: Blixt

description: Portefeuille LN multi fonction
---

![présentation](assets/1.jpeg)

# Portefeuille/Nœud Blixt BTC ⚡️ LN

## Un puissant nœud BTC/Lightning dans votre poche, où que vous soyez

** Texte de DarthCoin traduit par asi0 – 01/11/2022 **

Je voudrais vous présenter un nouveau nœud et porte-monnaie mobile BTC / LN intéressant et également puissant – Blixt. Le nom vient du suédois et signifie « éclair ».

## Comment j’ai découvert ce petit bijou ?

J’ai un nœud Umbrel LND et je voulais avoir un plan de sauvegarde pour restaurer rapidement mon nœud en cas de SHTF1. J’ai donc trouvé ce portefeuille mobile qui permet de restaurer à partir de sauvegardes SCB l’ensemble des fonds du nœud. Ensuite, je commence à le tester plus en détail et j’ai découvert que C’EST UN NOEUD COMPLET DANS VOTRE PROPRE POCHE.

N’oubliez pas ça car c’est très important !

> À la fin de cet article, vous trouverez quelques tutos simples et rapides sur comment l’utiliser et comment se connecter à d’autres nœuds.

Il s’agit d’une application étonnante sur Android et iOS qui permet de faire tourner un nœud BTC-LND, dans votre propre poche. Incroyable, non ? ! Dans votre propre téléphone, vous pouvez avoir un nœud BTC LN prêt en moins de 10 minutes, avec de riches fonctionnalités pour les utilisateurs expérimentés mais pour les nouveaux utilisateurs ou ceux qui ne sont pas si férus de technologie car l’utilisation est simple et harmonieuse.

Blixt Wallet est un projet open-source sous licence MIT et il se focalise sur une niche d’utilisateurs qui veulent commencer avec BTC/LN mais qui n’ont pas les moyens de faire fonctionner une machine complète ou veulent simplement faire tourner un nœud mobile.
Liens

Voici quelques liens à propos de cette nouvelle application de nœud/portefeuille :

> Site officiel – avec également une charmante démo interactive

> Dépôt GitHub : vérifiez le stade de développement et/ou téléchargez les sources

> Groupe d’aide Telegram – où vous pouvez poser des questions directement au développeur et à la communauté
>
> Téléchargement de l’application Android Blixt
>
> Téléchargement de l’application Testflight pour iOS
> Feed Twitter avec des démos

![image principal](assets/2.JPEG)

# Principales fonctionnalités disponibles

## Nœud Neutrino

Blixt se connecte par défaut au serveur de Blixt pour synchroniser les blocs et l’index avec Neutrino (mode SPV pour Simplified Paiement Verification), mais l’utilisateur peut aussi se connecter à son propre nœud. Il est surprenant de constater que la synchronisation d’un nœud SPV prend moins de 5 minutes, dans mon cas sur Android 11, pour être prêt à utiliser le portefeuille du nœud complet (on-chain et LN)
Nœud Complet Non-Custodial

L’utilisateur peut gérer ses propres canaux avec une interface facile et avec suffisamment d’informations affichées pour avoir une bonne expérience. Dans le menu tiroir en haut à gauche, vous pouvez aller sur les canaux Lightning pour commencer à ouvrir avec d’autres nœuds, comme vous le souhaitez. N’oubliez pas d’activer Tor dans les paramètres. C’est beaucoup mieux pour la vie privée et aussi parce que en tant que nœud mobile, si vous changez beaucoup votre connexion internet / clearnet IP, vos pairs peuvent être pertubés. Avec l’URI du noeud Tor, vous aurez toujours le même identifiant privé quelque soit votre localisation / IP.

## Sauvegarder/Restaurer un nœud LND

Une fonctionnalité puissante, facile à gérer et utile est la restauration de d’autres nœuds LND morts, avec juste la liste 24 mots seed et le fichier channels.backup.

> Voici un guide sur comment restaurer les noeuds morts Umbrel dans Blixt en cas de SHTF.

L’utilisateur a également la possibilité d’enregistrer la sauvegarde des canaux Blixt dans Google drive et / ou le stockage local dans son propre mobile (pour plus tard, le déplacez dans un endroit sûr, hors de votre téléphone).

La procédure de restauration est assez simple : insérez la graine de 24 mots, ajoutez le fichier de sauvegarde (préalablement copié dans la mémoire du mobile) et cliquez sur restaurer. Cela prendra un certain temps pour synchroniser et scanner tous les blocs pour vos txs passées. Les canaux seront automatiquement fermés et les fonds retournés dans votre portefeuille onchain (voir le menu du tiroir en haut à gauche – onchain).

> Si vous aviez précédemment des canaux ouverts avec votre ancien nœud derrière Tor, vous devez d’abord activer l’option Tor (et redémarrer l’application) à partir des paramètres du menu. De cette façon, la procédure de fermeture n’échouera pas et/ou l’option de fermeture forcée ne sera pas utilisée

N’oubliez pas de faire une sauvegarde de vos canaux LN après avoir ouvert et/ou fermé des canaux. Cela ne prend que quelques secondes pour être en sécurité. Plus tard, vous pourrez déplacer le fichier de sauvegarde vers un endroit sûr hors de votre mobile.
Pour tester votre seed dans un scénario de restauration, avant d’ajouter des fonds, utilisez simplement la même graine de 24 mots (aezeed) dans BlueWallet. Si l’adresse BTC générée est la même dans Blixt, vous êtes fin prêt. Pas besoin d’utiliser BlueWallet après cela, vous pouvez simplement supprimer le portefeuille testé pour la restauration.
Tor intégré

Une fois que vous l’aurez activé, l’application redémarrera derrière le réseau Tor. À partir de ce moment, vous pouvez voir dans les paramètres du menu, votre node ID avec une adresse onion, de sorte que d’autres nœuds peuvent ouvrir des canaux vers votre petit nœud Blixt mobile. Ou disons que vous avez votre propre nœud à la maison et que vous voulez avoir des petits canaux avec votre nœud Blixt mobile. Une combinaison parfaite.

## Dunder LSP — Liquidity Service Provider ou Fournisseur de Services de Liquidités

Une fonctionnalité simple et fantastique qui offre au nouvel utilisateur la possibilité de commencer à accepter des BTC sur le Lightning Network immédiatement, sans à avoir besoin de déposer des fonds sur le portefeuille on-chain pour ensuite ouvrir des canaux LN.

Pour les nouveaux utilisateurs, c’est une excellente nouvelle, car ils sont censés pouvoir commencer de zéro, directement sur LN. Pour cela il suffit de créer une facture (ou invoice) LN à partir de l’écran principal sur le bouton « recevoir », de mettre le montant, la description, etc et de payer à partir d’un autre portefeuille. Blixt ouvrira un canal de 500k sats maximum par transaction reçue. Vous pouvez en ouvrir plusieurs, si nécessaire.

Un cas intéressant et utile est le suivant : disons que votre premier montant reçu est de 200k. Blixt ouvrira un canal de 500k sats et avec déjà 200k (moins les frais d’ouverture) de votre côté, mais comme vous avez encore 300k « d’espace » disponible vous pouvez en recevoir d’avantage. Donc le prochain paiement, disons, de 100k arrivera directement par ce canal, sans plus de frais et vous avez toujours 200k d’espace pour en recevoir d’avantage.

Mais si vous choisissez pour le troisième paiement de recevoir, disons, 300k, il créera un autre nouveau canal de 500k et poussera de votre côté ces 300k.

S’il y a trop de demandes, le nœud de Blixt peut modifier la capacité du canal lors de l’ouverture.

## Ouverture automatique de canal

Dans les paramètres, l’utilisateur peut activer cette option et avoir un service automatisé qui ouvre des canaux avec les meilleurs nœuds et routes à partir du solde disponible dans le portefeuille onchain de l’application Blixt. C’est une fonction avantageuse pour les nouveaux utilisateurs qui ne savent pas trop avec quel nœud faire un canal et/ou comment ouvrir un canal LN. C’est comme un pilote automatique pour LN.

> Rappelez-vous : cette option est utilisée une seule fois, lorsque vous créez votre nouveau portefeuille Blixt, et est activée par défaut. Donc si le nouvel utilisateur scanne le code QR on-chain sur l’écran principal et dépose à cette adresse ses premiers sats, Blixt ouvrira automatiquement un canal avec ces sats, avec le nœud public Blixt.

## Services de liquidités entrantes

Fonctionnalité dédiée aux marchands qui ont besoin de plus de liquidités ENTRANTES, facile à utiliser. Pour cela, il suffit de sélectionner l’un des fournisseurs de liquidités dans la liste, de payer le montant que vous voulez pour le canal et de fournir l’ID de votre nœud et à partir de là, un canal s’ouvrira vers votre nœud Blixt.

## Listes de contacts

Fonctionnalité utile si vous souhaitez disposer d’une liste durable de destinateurs avec lesquels vous commercer la plupart du temps. Cette liste peut être constituée de LNURL, d’adresses Lightning ou de futures informations de paiement statiques/factures. Pour l’instant, cette liste ne peut pas être sauvegardée en dehors de l’application, mais il est prévu d’avoir une option pour l’exporter.

## Envoyer vers une adresse Ligthning

Vous pouvez envoyer à n’importe quelle adresse LN si elle n’est pas dans votre liste de contacts. Bientôt peut-être, une option pour avoir sa propre adresse LN de type @blixtwallet.com.

Prise en charge des LNURL

Vous pouvez scanner/payer/vous connecter avec LNURL, mais pour le moment cela ne fonctionne pas si le LNURL est derrière Tor.

## Keysend

Une fonctionnalité très puissante que peu de portefeuilles mobiles ont. Vous pouvez envoyer / pousser des fonds directement par un canal ou pointé vers un autre nœud, en ajoutant un message si nécessaire. Cette fonctionnalité est très utile pour afficher des messages sur le panneau d’affichage Amboss.space (voici un guide sur ce panneau d’affichage Amboss).

## Signature de messages

Outil très utile pour signer des messages avec votre clé privée du nœud Blixt, des messages d’authentification de connexion et ainsi de suite. Très peu de portefeuilles mobiles disposent de cette fonctionnalité, quasiment aucun.

## Paiements multi-canaux — Multi-Path Payments (MPP)

Fonctionnalité utile pour les paiements LN, permettant de diviser un paiement LN en plusieurs parties, à travers plusieurs canaux. C’est un bon moyen d’équilibrer les liquidités sur le réseau et d’améliorer la confidentialité.

## Naviguateur Lightning

Une série de services tiers avec LN, organisés au sein d’un navigateur simple, accessible et à portée de main pour l’utilisateur. C’est aussi un bon moyen de promouvoir les entreprises qui acceptent BTC sur LN. Il s’agit d’une fonctionnalité qui sera davantage développée à l’avenir. Pour l’instant, elle ne fonctionne pas derrière Tor, donc la navigation sur ces applications se fera en clair (clearnet).

## Explorateurs de Logs

C’est un outil puissant pour vérifier les logs LND et l’état de votre nœud en général. Il y a une option pour sauvegarder le fichier des logs. Il est très utile d’avoir ces logs à portée de main au cas où vous auriez besoin de l’aide du développeur pour identifier certains problèmes.

## Sécurité

Vous pouvez définir dans les paramètres de l’application, pour une plus grande sécurité de votre portefeuille/noeud, la possibilité de démarer l’application avec un code PIN et/ou l’empreinte digitale.

## Portefeuille On-chain

Cette fonctionnalité est un peu cachée, dans le menu tiroir en haut à gauche. Comme elle n’est pas souvent utilisée par un utilisateur du LN, elle n’est pas visible sur l’écran principal. Mais ce n’est pas grave, vous pouvez l’avoir sur un portefeuille séparé où vous pouvez gérer les adresses et voir le journal des txs, en important votre seed sur Sparrow par exemple. Peut-être que dans le futur, Blixt wallet inclurera également une fonctionnalité pour gérer les UTxO. Mais pour l’instant, utilisez UNIQUEMENT ce portefeuille on-chain pour ouvrir ou fermer des canaux sur LN.

“Easter Eggs“

Eh oui, dans l’application Blixt, il y a quelques fonctionnalités cachées, des petites choses qui rendent l’application attachante, activant des actions et réponses amusantes/intéressantes.
Indice : essayez de cliquer deux fois sur le logo Blixt dans le tiroir 🙂 Je vous laisse découvrir le reste.

# Mini guide pour des cas d’usage typiques avec Blixt

A. Ouverture des canaux vers votre mini-nœud Blixt depuis votre noeud umbrel

## Pour les utilisateurs Android :

1. Allez dans les paramètres de Blixt – activez Tor – redémarrez l’application (fermez-la de force si elle ne redémarre pas automatiquement).

2. Attendez que Blixt s’ouvre derrière Tor et synchronise les derniers blocs.

3. Allez dans les paramètres – cliquer sur « Show Tor onion service », copiez-le, c’est l’URI de votre noeud Blixt.

4a. Allez dans votre application Umbrel RideTheLightning ou ThunderHub (je préfère celui-là) – ajoutez un pair et collez l’adresse onion, l’URI Blixt.

4b. Allez dans le tableau de bord de votre nœud Umbrel ou RTL/TH – ouvrez un canal, et sélectionnez un pair connu dans la liste en cherchant votre ID de nœud Blixt.

5. Mettez la quantité de sats pour le canal, cliquez sur ouvrir.

6. Attendez 3 confirmations pour avoir un nouveau canal avec votre « mini nœud » Blixt.

## Pour les utilisateurs d’iOS :

1. Allez dans les paramètres de Blixt – activez Tor – redémarrez l’application.

2. Attendez que Blixt s’ouvre derrière Tor et synchronise les derniers blocs.

3. Allez à votre nœud Umbrel, copiez l’URI Tor ou montrez le QR code.

4. Sur Blixt Wallet, allez dans Settings – Show Lightning Peers – Add peer et scannez ou collez l’URI de votre nœud Umbrel. Il sera ajouté en tant que pair connu.

5. Retournez dans l’application Thunderhub d’Umbrel, ouvrez le menu des canaux et sélectionnez un pair dans la liste déroulante des pairs existants.

6. Mettez tous les autres détails pour ouvrir le canal, cliquez sur Open.

7. Attendez 3 confirmations pour avoir ouvert ce canal et c’est fait, vous avez maintenant plus de liquidité entrante dans votre côté Blixt.

## B. Ouverture de canaux vers un nœud Umbrel

Cette fois, nous allons ouvrir un canal DEPUIS votre nœud Blixt, vers votre propre nœud Umbrel (par exemple), pour tester la connexion et l’utilisation de Tor. Plus tard, une fois ouvert, vous pouvez équilibrer ce canal en poussant la moitié ou le montant désiré vers le côté Umbrel. Cela peut également être utilisé comme une « valve d’évacuation » lorsque votre nœud principal Umbrel a besoin de plus de liquidités.

1. Allez sur votre nœud Umbrel et copiez l’URI de votre nœud, ou affichez simplement le code QR pour l’URI de l’onion address.

2. Allez dans Blixt – Settings – Lightning peers – add new peer (ajouter un nouveau pair).

3. Scannez le code QR de votre nœud Umbrel ou collez l’URI oignon et votre nœud Umbrel sera ajouté comme pair.

4. Retournez à l’écran principal – tiroir supérieur gauche – canaux Lightning.

5. Cliquez sur le signe « + » pour ouvrir un nouveau canal et collez l’URI ou scannez le code QR de votre nœud Umbrel. Ajoutez le nombre de sats pour le canal, les frais et cliquez sur ouvrir.

6. C’est fait ! Le canal prendra 3 confirmations pour être ouvert et … Joyeux Lightning avec votre propre nœud Umbrel.

C. Recevez des fonds directements dans le portefeuille LN

Il s’agit d’une expérience simple et si plaisante que de recevoir des fonds directement dans votre portefeuille de nœuds Blixt fraîchement ouvert, sans avoir besoin au préalable à déposer des fond et d’ouvrir manuellement des canaux avec des nœuds spécifiques.

1. Une fois que vous avez créé le portefeuille et sauvegardé la graine, allez dans les paramètres et activez la fonctionnalité Dunder LSP.

2. Retournez à l’écran principal – cliquez sur recevoir, mettez le montant, j’ai testé avec 200k sats.

3. Il créera une facture LN à payer à partir d’un autre porte-monnaie LN.

4. Le service LSP Dunder créera un canal de max 500k sats et poussera les fonds que vous avez envoyés (200k dans notre cas) sur le côté de votre canal. Ainsi, vous aurez un joli canal prêt à envoyer et recevoir.

5. Si vous voulez recevoir plus, les prochains paiements seront reçus dans le même canal, jusqu’à ce que le maximum de 500k soit atteint. S’il n’y a plus de « place » pour recevoir dans le même canal, Dunder LSP créera un nouveau canal, selon la même procédure.

6. Faites une sauvegarde de vos nouveaux canaux ouverts. Toujours à faire après avoir ouvert ou fermé un nouveau canal. C’est très facile et rapide et peut vous éviter beaucoup de problèmes.

Il s’agit d’un cas d’utilisation parfait pour les nouveaux petits commerçants qui souhaitent commencer à accepter BTC.

Remarques importantes

> Avant de commencer à utiliser vos canaux derrière Tor et si l’application Blixt est restée longtemps fermée/ pas synchronisée, attendez que l’icône de synchronisation en haut de l’écran disparaisse et vérifiez que tous vos canaux soient actifs. Si c’est bon, allez-y et faites vos transactions.
>
> Si les canaux ne sont toujours pas actifs, ajoutez à nouveau la clé publique (l’URI) de vos pairs, dans les options de Blixt – Show peers. Vous pouvez aussi essayer de rafraîchir cette liste, si le gossip sous Tor trouve vos pairs, les canaux seront de nouveau actifs. Si non, ajoutez les à nouveau, ce qui poussera le gossip à communiquer.
>
> Mais rappelez-vous : ne réalisez pas aveuglément une tx immédiatement après avoir ouvert l’application Blixt. Cela prend quelques instants pour vérifier si vos canaux sont actifs, et permet de vous prévenir s’il y a erreur dans la route du paiement ou un manque de liquidité sur la route
>
> Ouvrir des canaux LN avec Blixt, a un coût, comme tout autre nœud LN ouvrant des canaux. Cela a un nom : « commit_fees » (ou frais d’engagement) qui sont comme une réserve pour fermer les canaux, pour être en mesure de payer les frais des mineurs. Soyez donc conscient que lorsque vous déposez dans votre porteufeuille on-chain Blixt et ouvrez des canaux (peu importe que vous utilisiez le LSP Dunder, l’ouverture automatiques des canaux ou manuellement) le montant disponible sera légèrement inférieur au montant total avec lequel vous avez ouvert le canal. C’est pourquoi IL N’EST PAS RECOMMANDÉ d’ouvrir de tout petits canaux comme 20-50-100k sats.
>
> De plus, chaque transaction LN a des petits frais pour le réseau. Ce ne sont pas des frais pour Blixt, c’est un coût qui rend vos transactions sûres et sécurisées par le réseau. Mais ils sont très petits, parfois même en milli-sats, souvent moins de 0.5% du montant de votre transaction.
>
> Étant un nœud LN, il est fortement déconseillé d’utiliser la même graine sur deux appareils différents. Cette procédure peut être faite SEULEMENT dans le cas où vous êtes dans une procédure de récupération. Lorsque le portefeuille on-chain génère à partir de la graine, il va commencer à synchroniser les txs précédentes et les soldes. Si vous n’avez pas le LN.backup de vos canaux, cela ne va pas commencer la procédure de restauration complète. Donc oui, vous verrez le même portefeuille on-chain sur les deux appareils mais PAS le solde de LN. Et surtout N’ESSAYEZ PAS de restaurer sur les deux appareils les mêmes canaux LN, car sinon vous perdriez tous vos fonds LN !
>
> Gardez à l’esprit que la fermeture des canaux prend du temps, jusqu’à ce que les fonds soient libérés. C’est ainsi que fonctionne LN (pour en savoir plus allez ici). Donc, en général, si vous avez une fermeture coopérative (normale), cela prendra au moins 40 blocs jusqu’à ce que les fonds soient libérés dans votre portefeuille on-chain. Pour les canaux fermés de force, ce verrou est de 144 blocs ou même plus parfois. Soyez donc patient, et pas d’inquiétude, les fonds sont en sécurité.

## Conclusion

Bon, voici quelques-unes des principales fonctionnalités (pour un portefeuille mobile, c'est beaucoup, n'est-ce pas ?) parmi beaucoup d'autres et bientôt il y en aura encore plus.

L'expérience avec cette application de portefeuille/nœud LN est très agréable et facile à utiliser, une application très réactive, pas de problèmes majeurs, juste des petites choses qui doivent être ajoutées (mais pas si importantes que ça). C'est encore une application jeune et elle a besoin de beaucoup de tests dans des conditions réelles. Alors n'hésitez pas à l'essayer et à informer le développeur de tout problème qui pourrait être corrigé ou amélioré.

N'oublions pas non plus qu'il s'agit d'un projet open source et que sa maintenance est assurée par un seul développeur, qui fait tout le travail ! Donc, s'il vous plaît, aidez-le avec des tests et des commentaires et le plus important, soyez patient et signalez-lui avec beaucoup de détails si vous trouvez des problèmes ou si l'application a besoin de plus d'améliorations.

J'espère que vous apprécierez son utilisation. Personnellement, je l'adore et elle m'est très utile (voir ici un cas d'usage où ce portefeuille est un formidable outil).

Que ₿ITCOIN SOIT AVEC TOI !

> Si tu apprécies le travail de DarthCoin, tu peux envoyer quelques satoshis par LN : en utilisant la page Telegram @LNtxBot DarthCoin LNURL ou simplement en utilisant l’adresse Lightning à darthcoin@lntxbot.com
> LNURL1DP68GURN8GHJ7MRWW3UXYMM59E3K7MF09EMK2MRV944KUMMHDCHKCMN4WFK8QTMYV9E8G6RRDA5KULQ3NJF

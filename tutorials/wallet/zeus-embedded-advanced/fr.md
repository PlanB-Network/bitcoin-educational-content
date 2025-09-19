---
name: Zeus Embedded - Avancé
description: Portefeuille Lightning multi-nœuds en auto-garde
---

![Zeus](assets/cover.webp)


## Introduction à ZEUS Wallet


ZEUS est une application mobile Bitcoin Wallet et de gestion de nœuds avec toutes les fonctionnalités d'un Bitcoin lightning Wallet qui simplifie les paiements Bitcoin, donne aux utilisateurs un contrôle complet de leurs finances et permet aux utilisateurs plus avancés de gérer leurs nœuds Lightning depuis la paume de leur main.


### À qui s'adresse ZEUS ?

Actuellement, ZEUS s’adresse aux personnes qui exploitent leurs propres nœuds domestiques / professionnels [Lightning Network Daemon (LND)](https://lightning.engineering/) ou [Core Lightning (CLN)](https://blockstream.com/lightning/) et les gèrent à distance via Zeus.


Les commerçants utilisant [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) ou [Alby](https://getalby.com/) (ou tout autre compte LNDhub) peuvent également se connecter à leurs nœuds / comptes, les utiliser et les gérer depuis ZEUS.


[À partir de la version v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS commencera à s’adresser aux utilisateurs ordinaires qui souhaitent simplement un moyen simple d’effectuer des paiements en bitcoin rapides et peu coûteux depuis leur appareil mobile, grâce à un [nœud Lightning mobile intégré](https://docs.zeusln.app/category/embedded-node) avec un [fournisseur de services Lightning (LSP)](https://docs.zeusln.app/lsp/intro) intégré.


### Ressources importantes sur Zeus :


- Site officiel de Zeus - [https://zeusln.app/](https://zeusln.app/)
- Zeus Documentation - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Dépôt Github de Zeus](https://github.com/ZeusLN/zeus)
- [Groupe de support Zeus sur Telegram](https://t.me/ZeusLN)
- [Zeus sur NOSTR](https://iris.to/zeus@zeusln.app)
- [Annonces du blog Zeus](https://blog.zeusln.com)


### Caractéristiques de Zeus

#### Caractéristiques générales :


- Autodétention, Bitcoin et Lightning seulement Wallet
- Pas de frais de traitement, pas de KYC
- Entièrement open source (APGLv3)
- Prise en charge de plusieurs nœuds et comptes (vous pouvez gérer votre propre nœud domestique, exécuter un nœud LND intégré, vous connecter à plusieurs comptes LNDhub)
- Menu d'activités facile à utiliser
- Cryptage PIN ou passphrase, mode confidentialité - dissimulez vos données sensibles
- Carnet de contacts, multi-thèmes, multi-langues


#### Caractéristiques techniques


- Se connecter via Tor
- Prise en charge complète des LNURL (paiement, retrait, authentification, canal), envoi vers des adresses Lightning
- Gestion détaillée des canaux d'éclairage, support MPP/AMP, Keysend, gestion des frais de routage
- Replace-by-fee (RBF) et Soutien aux enfants pour les parents (CPFP)
- Paiements et demandes NFC, Signer et vérifier les messages
- Soutien à SegWit et Taproot
- Simple Taproot Channels
- Adresses fulgurantes d'autodétention (@zeuspay.com)
- Point de vente par Square (bientôt PoS ouvert)


### Guides et tutoriels vidéo

Pour pouvoir utiliser Zeus et gérer les canaux Lightning, la liquidité, les frais, etc., il est préférable de lire d'abord quelques guides importants sur Lightning Network.


#### Guides :


- [LND - Documentation du Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Documentation de Core Lightning](https://lightning.readthedocs.io/index.html)
- [Guide Lightning pour débutants](https://bitcoiner.guide/lightning/) – par Bitcoin Q&A
- [Gestion de nœud Lightning](https://www.lightningnode.info/) – par openoms
- [Le Lightning Network et l’analogie avec l’aéroport](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Gestion de la liquidité des nœuds Lightning](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Maintenance du nœud Lightning](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Tutoriel vidéo par BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Un guide pour commencer à utiliser le nœud embarqué Zeus LN sur votre appareil mobile


![Image](assets/en/01.webp)


Je dédie ce guide à tous les nouveaux utilisateurs de Lightning Network (LN) qui souhaitent commencer un nouveau voyage souverain en utilisant un nœud d'autocontrôle Wallet sur leurs appareils mobiles.


Considérons que vous êtes déjà passé par toute cette pléthore de portefeuilles LN, mais que vous n'êtes pas encore prêt à gérer un nœud de routage PUBLIC LN, vous voulez juste empiler plus de Sats sur LN d'une manière plus autonome et effectuer vos paiements réguliers sur LN.


Voici Zeus, à partir de la [version v0.8.0 annoncée sur leur blog](https://blog.zeusln.com/new-release-zeus-v0-8-0/), qui propose désormais un nœud LND intégré dans l’application. Jusqu’à présent, Zeus était une application de gestion de nœuds distants + comptes LNDhub. Mais maintenant… le nœud est dans le téléphone !


![Image](assets/en/02.webp)


### Récapitulation rapide des principales fonctionnalités de Zeus Node :



- **Nœud LND privé** - Cela signifie que ce nœud n'effectuera PAS de routage public des paiements d'autres personnes à travers votre nœud. Le noeud et les canaux ne sont pas annoncés (privés, non visibles sur le graphique public LN). Recevoir et effectuer des paiements se fera par l'intermédiaire de vos pairs LSP connectés. N'OUBLIEZ PAS : le nœud intégré de Zeus n'effectuera PAS de routage public !
- Service persistant **LND** - l'utilisateur peut activer cette fonction et maintenir le service LND actif en permanence comme n'importe quel nœud LN. L'application n'a pas besoin d'être ouverte, le service persistant maintiendra toutes les communications en ligne.
-   **Filtres de blocs Neutrino** - la synchronisation des blocs est effectuée à l’aide des [filtres de blocs et du protocole Neutrino](https://bitcoinops.org/en/topics/compact-block-filters/) (sans aucune information sur les fonds on-chain de nos utilisateurs). Rappel : pour les connexions Internet à haute latence / lentes, cette synchronisation des blocs basée sur Neutrino peut parfois échouer. Essayer de basculer vers un serveur Neutrino proche pourrait aider à rétablir la synchronisation. Sans cette synchronisation, votre nœud LND ne peut pas démarrer !
- **Canaux Taproot simples** - En fermant ces canaux, les utilisateurs encourent moins de frais et bénéficient d'une plus grande confidentialité car ils apparaissent comme n'importe quelle autre dépense Taproot lorsqu'ils examinent leur empreinte On-Chain.
- **LSP intégré** - Olympus est le nouveau nœud LSP pour Zeus. Les utilisateurs peuvent recevoir le Sats via le LN immédiatement, sans avoir préalablement mis en place des canaux LN. Ils devront simplement créer un LN Invoice et payer à partir de n'importe quel autre LN Wallet, avec le service de canal 0-conf de Zeus. Pour en savoir plus sur Zeus LSP, cliquez ici. Le LSP offre également une plus grande confidentialité à nos utilisateurs en leur fournissant des factures enveloppées qui cachent les clés publiques de leurs nœuds aux payeurs.
- **Carnet de contacts** - vous pouvez enregistrer manuellement des contacts ou les importer depuis NOSTR, pour faciliter l'envoi de paiements à vos destinations habituelles.
- Prise en charge complète de LNURL, LN Address envoyer et recevoir - vous pouvez maintenant mettre en place votre propre LN Address avec @zeuspay.com. **Rappel** : Vous pouvez également utiliser Zeus pour LN-auth sur les sites où vous pouvez vous connecter avec une authentification LN. C'est très pratique.
- **Point de vente** - Les commerçants peuvent désormais créer leurs propres articles et les vendre directement à partir de Zeus, avec un point de vente intégré. Pour l'instant, il contient les besoins de base, mais à l'avenir, il contiendra des fonctionnalités étendues.
- **LND logs** - l'utilisateur peut lire en temps réel les logs du service LND et les utiliser pour déboguer d'éventuels problèmes (principalement pour les mauvaises connexions)
- **Sauvegardes automatisées** - les canaux du nœud LN sont automatiquement sauvegardés sur le serveur Olympus. Cette sauvegarde automatisée est cryptée avec votre nœud Wallet seed (sans le seed est totalement inutile). L'utilisateur peut également exporter manuellement un SCB (static channels backup) pour une récupération en cas de désastre.


### Comment embarquer avec Zeus LN Node (LND embedded)


Dans ce guide, je parlerai uniquement du nœud LND intégré, et non des autres façons d’utiliser cette magnifique application (gestion de nœuds distants et comptes LNDhub). Pour les autres types de connexions, veuillez vous référer à la [page de documentation Zeus](https://docs.zeusln.app/category/getting-started), qui est très bien expliquée et ne nécessite pas d’écrire un guide dédié.


#### ÉTAPE 1 - CONFIGURATION INITIALE


Étant donné que Zeus est un nœud LND complet, je vais faire quelques recommandations initiales :



- N'utilisez pas un vieil appareil, cela pourrait affecter l'utilisation de cette application puissante. En particulier pendant la période de synchronisation, l'application peut utiliser intensivement le CPU et la RAM. L'absence de ces éléments pourrait même rendre impossible l'utilisation de l'application Zeus.
- Utilisez au moins Android 11 comme système d'exploitation mobile et mettez-le à jour autant que possible. Pour iOS, c'est la même chose, mais essayez d'utiliser une version plus récente du système d'exploitation.
- Vous aurez besoin d'au moins 1 Go d'espace disque pour le stockage des données. Avec le temps, cet espace pourrait être plus important, mais il existe une fonctionnalité permettant de compacter la base de données à un niveau de quelques Mo.
- Il n'est PAS nécessaire d'utiliser Zeus avec Tor ou Orbot. Ne compliquez pas les choses plus que nécessaire. Tor dans ce cas ne vous offrira pas plus de confidentialité mais ne fera qu'empirer les choses pour la synchronisation initiale. Faites également attention aux VPN que vous utilisez et vérifiez la latence de la connexion vers les serveurs Neutrino. Gardez à l'esprit que les filtres de blocage de Neutrino ne divulguent pas ou ne tracent pas l'identité de votre appareil, ils ne font que desservir des blocs. Le trafic LN est également derrière un LSP avec des canaux privés, donc très peu d'informations sortent, il n'y a pas de raison de s'inquiéter pour la vie privée.
-   Faites preuve de patience pour la synchronisation initiale, cela peut prendre plusieurs minutes. Essayez d’être connecté à une connexion Internet haut débit avec une bonne latence. Si vous exécutez votre propre nœud Bitcoin, [vous pouvez activer le service neutrino](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) et connecter votre Zeus à votre propre nœud, même en utilisant le réseau local interne, afin d’avoir une vitesse maximale.


Une fois que vous avez configuré le type de connexion "Embedded node", l'application commence à se synchroniser pendant un certain temps. Attendez patiemment la fin de cette partie, puis accédez à la page principale des paramètres.


![Image](assets/en/03.webp)


Avant de commencer à utiliser Zeus, nous allons nous plonger dans chacune des sections des paramètres et comprendre certaines des principales caractéristiques :


**A - SETTINGS**


Il s'agit d'une section contenant des paramètres généraux pour l'ensemble de l'application


**1 - Lightning Service Provider (LSP)**


Deux services de FSL sont présentés ici :



- canaux juste à temps - lorsque vous n'avez pas de canal ouvert ou de liquidité entrante disponible, si le service est activé, il ouvrira un canal à la volée pour vous. Cette option peut être désactivée si vous ne souhaitez pas ouvrir d'autres canaux de ce type.
- demande de canaux à l'avance_ - vous pouvez acheter des canaux entrants auprès du FSL Olympus directement dans l'application avec plusieurs options et montants (pour les canaux entrants et sortants).


Le LSP aide les utilisateurs à se connecter au réseau Lightning en ouvrant des canaux de paiement vers leurs nœuds. [Lisez-en plus sur les LSP ici](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS a intégré un nouveau LSP appelé [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), disponible pour tous les utilisateurs qui utilisent le nouveau nœud intégré.


Dans cette section, le LSP Olympus (https://0conf.lnolymp.us) est utilisé par défaut, mais vous pourrez bientôt définir un autre LSP 0conf qui prend en charge ce protocole.


_Keep in mind :_ (Garder à l'esprit)

lorsque vous ouvrez un canal avec Olympus LSP en utilisant les factures LN enveloppées, vous obtenez également une liquidité entrante de 100k ! C'est une très bonne option au cas où vous auriez besoin de recevoir immédiatement plus de Sats

exemple : vous déposez 400k Sats pour ouvrir un canal LSP, alors le LSP ouvre un canal d'une capacité de 500k Sats vers votre nœud Zeus et pousse les 400k Sats que vous déposez vers votre côté

la "liquidité entrante" = plus d'"espace" dans votre canal pour recevoir


A l'avenir, nous espérons que de nombreux autres LSP pourront être intégrés à Zeus et utilisés alternativement par chacun d'entre eux. Ce n'est qu'une question de temps jusqu'à ce que de nouveaux LSPs adoptent un standard ouvert pour ce type de canaux 0conf.


Si vous ne souhaitez pas ouvrir de nouveaux canaux "à la volée", vous pouvez désactiver cette option.


Dans cette même section, vous avez également la possibilité de choisir de "demander des canaux Taproot simples" lorsque le FSL ouvrira un canal vers votre nœud Zeus. Ces canaux Taproot simples offrent une meilleure confidentialité On-Chain et des frais moins élevés lors de la fermeture du canal. Il n'y a que deux raisons pour lesquelles vous ne voudriez pas les utiliser :



- Ils sont nouveaux et il peut y avoir des bogues dans LND lorsqu'ils sont utilisés.
- Votre contrepartie ne les prend pas en charge. Même les nœuds LND doivent explicitement choisir d'y participer, pour l'instant.


**2 - Paramètres de paiement**


Cette fonctionnalité vous permettra de définir vos propres frais de paiement, sur LN ou onchain. Vous aurez également la possibilité d'augmenter ou de réduire le délai d'attente pour vos factures.


Si certains de vos paiements LN échouent, vous pouvez augmenter les frais pour trouver une meilleure route. De même, si vous effectuez des tx sur la chaîne, vous pouvez définir une redevance spécifique afin que votre tx ne reste pas bloqué dans la Mempool pendant longtemps, en cas de période de redevance élevée.


**3 - Paramètres des factures**


Cette section propose quelques options pour les factures generate :



- Définir un mémo standard à afficher dans le Invoice ou le generate
- Délai d'expiration en secondes, au cas où vous souhaiteriez un délai spécifique, plus ou moins long, pour le paiement de votre Invoice
- Inclure des indications d'itinéraire - fournir des informations pour trouver des canaux non annoncés, ou privés. Cela permet d'acheminer les paiements vers des nœuds qui ne sont pas publiquement visibles sur le réseau. Un indice d'acheminement fournit un itinéraire partiel entre le nœud privé du destinataire et un nœud public. Cet indice de routage est ensuite inclus dans le Invoice généré par le destinataire et fourni au payeur. Je suggère de l'activer par défaut, sinon les paiements entrants pourraient échouer (aucune route trouvée).
- AMP Invoice - Atomic Multi-path Payments est un nouveau type de paiement Lightning implémenté par LND qui permet de recevoir Sats sans Invoice spécifique, en utilisant [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). Il s'agit pratiquement d'un code de paiement statique. [Pour en savoir plus, cliquez ici](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Show custom preimage field - n'utilisez cette option que dans des cas très spécifiques, lorsque vous souhaitez vraiment utiliser des champs personnalisés dans la préimage. (Pour en savoir plus, cliquez ici) (https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Une autre option de cette section consiste à définir le type de chaîne Address que vous souhaitez utiliser : SegWit imbriqué, SegWit, Taproot.


![Image](assets/en/04.webp)


Cliquez sur le bouton de la roue du haut et un écran popup apparaîtra pour choisir le type de Address désiré. Une fois ce choix effectué, la prochaine fois que vous appuierez sur le bouton de réception de la chaîne, le type de Address sélectionné s'appliquera à la generate. Vous pouvez le changer à tout moment.


**4 - Réglages des canaux**


Dans cette section, vous pouvez prédéfinir certaines caractéristiques des canaux d'ouverture, comme par exemple :



- nombre de confirmations
- Annoncer le canal (par défaut, il est désactivé), ce qui signifie que les canaux ne seront pas annoncés
- Canaux simples Taproot
- Afficher le bouton d'achat de la chaîne


**5 - Paramètres de confidentialité**


Vous trouverez ici quelques paramètres de base qui vous permettront d'améliorer la protection de votre vie privée grâce à l'application Zeus :



- Block explorer pour ouvrir les détails tx (Mempool.space, blockstream.info ou personnalisé)
- Lire le presse-papiers - activation/désactivation de la lecture par Zeus du presse-papiers de votre appareil
- Mode "Lurker" (rôdeur) - activation/désactivation de l'option permettant de masquer des informations sensibles spécifiques dans l'application Zeus. C'est une bonne option lorsque vous faites des démos ou des captures d'écran.
- Suggestion de frais Mempool - activez cette option si vous souhaitez utiliser les niveaux de frais recommandés dans [Mempool.space](https://Mempool.space/)


**6 - Sécurité**


Cette section n'offre que deux options pour sécuriser l'application à l'ouverture : définir un mot de passe ou un code PIN.


Une fois que vous avez défini un code PIN pour ouvrir l'application, vous pouvez également définir un "code PIN de contrainte". Ce code secret supplémentaire sera utilisé UNIQUEMENT en cas de contrainte, si vous êtes menacé. Si vous mettez ce code PIN, la configuration sera entièrement effacée. Vous devez donc mettre à jour vos sauvegardes. Les sauvegardes automatiques sont activées par défaut, mais il est bon d'avoir ses propres sauvegardes, en dehors de l'appareil.


**7 - Monnaie**


Active ou désactive l'option d'affichage de la conversion de la monnaie fiduciaire dans l'utilisation de l'application Zeus. Actuellement, plus de 30 monnaies fiduciaires sont prises en charge.


**8 - Langue**


Vous pouvez basculer entre plusieurs langues de traduction, révisées par la communauté Zeus avec des locuteurs natifs.


**9 - Affichage**


Dans cette section, vous pouvez personnaliser l'affichage de votre Zeus, en sélectionnant différents thèmes de couleurs, l'écran par défaut (clavier ou balance), l'affichage de l'alias de votre nœud, l'activation des gros boutons du clavier, l'affichage d'un plus grand nombre de décimales.


**10 - Point de vente**


Il s'agit d'une fonction spéciale qui permet d'activer ou de désactiver un système de point de vente intégré à Zeus. Vous pouvez utiliser un PoS autonome ou lié à un système de PoS Square. Actuellement, il supporte les fonctionnalités de base d'un PoS, mais c'est suffisant pour un bon début et cela pourrait aider les petits commerçants (bars/restaurants, épiceries) à commencer à accepter les BTC d'une manière native.


Dans ces paramètres, vous trouverez diverses options pour configurer votre PoS :



- Type de paiement de confirmation : LN uniquement, 0-conf, 1-conf
- Activer / désactiver les pourboires pour les employés qui gèrent le point de vente
- Afficher / masquer le clavier
- Pourcentage de taxe à appliquer sur le billet
- Créer des produits et des catégories de produits
- Une simple liste de toutes les ventes


Voici une vidéo de démonstration en direct de l'utilisation de Zeus PoS :


**B - Sauvegarde Wallet**


Le nœud intégré dans ZEUS est basé sur LND et utilise le [aezeed seed format](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Ce format est différent du [BIP39 format](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) que l'on trouve dans la plupart des portefeuilles Bitcoin, bien qu'il puisse sembler similaire. Aezeed inclut des données supplémentaires, notamment la date de naissance du Wallet, qui permettront d'effectuer plus efficacement les nouveaux balayages lors de la récupération.


Le format de clé aezeed devrait être compatible avec les portefeuilles mobiles suivants : Blixt, BlueWallet et Breez. Notez que la seed seule sera insuffisante pour récupérer tous vos soldes si vous avez des canaux de fermeture ouverts ou en attente !


Pour en savoir plus sur le processus de sauvegarde et de restauration, consultez la [page Zeus Docs](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


CONSEIL DE PUISSANCE : Lorsque vous sauvegardez votre seed, sauvegardez également la clé publique du nœud ! Il est parfois bon de l'avoir à portée de main, avec votre seed et votre SCB (Static Channels Backup) au cas où vous auriez besoin de vérifier la récupération.


SCB n'est nécessaire que si vous avez des canaux LN ouverts. Si vous n'avez que des fonds onchain, ce n'est pas nécessaire.


Si vous voyez qu'après un long moment, les txs de l'ancien historique ne sont toujours pas affichés, allez dans Embedded node - Peers et désactivez l'option d'utilisation de la liste des pairs sélectionnés (par défaut le btcd.lnolymp.us). Cela déclenchera un redémarrage et permettra de se connecter au premier nœud neutrino disponible avec un meilleur temps de réponse. Vous pouvez également utiliser les autres peers neutrino bien connus mentionnés ci-dessous.


Si vous voulez voir d'autres options de récupération pour un nœud LND, [veuillez lire mon guide précédent](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), où vous pouvez trouver les étapes pour importer un seed aseptisé dans Sparrow Wallet ou d'autres méthodes.


**C - Nœud embarqué**


Dans cette section, nous trouverons quelques outils de base pour gérer le nœud intégré :



- reprise après sinistre - Sauvegardes automatisées et manuelles pour les canaux LN. Pour en savoir plus sur l'utilisation de cette fonction, consultez la page Zeus Docs.
- express Graph Sync_ - L'application Zeus téléchargera le graphique des potins LN à partir d'un serveur dédié, pour une synchronisation plus rapide et de meilleure qualité, offrant les meilleurs chemins de paiement. Vous pouvez également choisir d'effacer les données du graphique précédent au démarrage.
- peers_ - section pour gérer les peers neutrino et les peers 0-conf. Si vous avez des problèmes avec la synchronisation initiale, les canaux ne se mettent pas en ligne, c'est parce que votre appareil a une latence élevée avec le pair neutrino configuré. Essayez de changer la liste des pairs préférés ou ajoutez votre pair spécifique dont vous savez qu'il a une meilleure latence pour la synchronisation. Les serveurs neutrino les plus connus sont :



 - btcd1.lnolymp.us | btcd2.lnolymp.us - pour la région US
 - sg.lnolymp.us - pour la région Asie
 - btcd-Mainnet.lightning.computer - pour la région US
 - uswest.blixtwallet.com (Seattle) - pour la région des États-Unis
 - europe.blixtwallet.com (Allemagne) - pour la région de l'UE
 - asia.blixtwallet.com - pour la région Asie
 - node.eldamar.icu - pour la région des États-Unis
 - noad.sathoarder.com - pour la région US
 - bb1.breez.technology | bb2.breez.technology - pour la région US
 - neutrino.shock.network - Région des États-Unis



- _LND logs_ - outil très utile pour déboguer vos problèmes de nœuds LN et contrôler en profondeur ce qui se passe à un niveau plus technique.
- paramètres avancés - plus d'outils pour contrôler l'utilisation de votre nœud LND :



 - mode de recherche de chemin - bimodal ou apriori, moyens de trouver un meilleur itinéraire pour vos paiements LN et de réinitialiser les informations de routage précédentes. Veuillez lire ces très bons guides sur la recherche d'itinéraires : [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - par Docs Lightning Engineering et [LN Payment Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - par Voltage
 - _Persistent LND_ - activez ce mode si vous voulez que le service LND fonctionne continuellement en arrière-plan et que votre nœud reste en ligne 24 heures sur 24 et 7 jours sur 7. Ceci est très utile si vous utilisez Zeus comme point de vente dans une petite boutique ou si vous recevez de nombreux tuyaux LN par l'intermédiaire du LN Address.
 - rescan wallet_ - cette option déclenchera au redémarrage un scan complet de tous les txs onchain de votre Wallet. Activez-la uniquement dans le cas où il vous manque des txs dans votre Wallet. La tâche de rescan prendra du temps, plusieurs minutes, donc soyez patient et vérifiez toujours les logs pour voir plus de détails sur la progression.
 - compacter la base de données - cette option est très utile si votre application Zeus occupe beaucoup d'espace sur votre appareil (voir les détails de l'application dans les paramètres de votre appareil). Si vous avez beaucoup d'activités avec Zeus, je vous recommande d'effectuer ce compactage plus souvent. Une fois que vous voyez que vous avez plus de 1 à 1,5 Go de données pour l'application Zeus, procédez au compactage. Cela va redémarrer et prendre un certain temps, alors soyez patient.
 - supprimer les fichiers Neutrino_ - cette option de suppression des fichiers Neutrino (avec un redémarrage) réduira considérablement l'utilisation du stockage de données. La réduction de l'utilisation des données a également un impact important sur l'utilisation de la batterie, surtout si vous utilisez Zeus en mode persistant.


**D - Info nœud**


Dans cette section, vous trouverez plus de détails sur l'état de votre nœud Zeus :



- Alias - ID court du nœud
- Clé publique - la clé publique complète de votre nœud, nécessaire pour que les autres nœuds puissent trouver le chemin vers votre nœud. Rappelez-vous que cette clé publique n'est PAS visible sur les explorateurs LN habituels (Mempool, Amboss, 1ML, etc.). Cette clé publique est accessible UNIQUEMENT par l'intermédiaire de vos pairs et canaux LN connectés.
- Version de mise en œuvre du LN
- Version de l'application Zeus
- Synchronisé avec la chaîne et Synchronisé avec le graphique - deux éléments très importants qui indiquent l'état correct de votre nœud. Si ces deux états n'affichent pas "true", cela signifie que votre nœud est toujours en cours de synchronisation ou qu'il rencontre des problèmes de synchronisation. Il est donc conseillé de consulter les journaux de votre LND ou d'attendre un peu plus longtemps.
- Hauteur du bloc et Hash - indique le dernier bloc et Hash que votre nœud a vu et synchronisé.


**E - Informations sur le réseau**


Cette section affiche plus de détails sur l'état général du Lightning Network, extraits des données de synchronisation de votre graphe : nombre de canaux publics disponibles, nombre de noeuds, nombre de canaux zombies (hors ligne ou morts), diamètre du graphe, degré moyen et maximum du graphe.


Ces informations peuvent être utiles pour le débogage ou simplement utilisées à des fins statistiques.


**F - Éclair Address**


Dans cette section, l'utilisateur peut configurer sa propre garde LN Address @zeuspay.com.


ZEUS PAY s'appuie sur les hashs de préimage générés par les utilisateurs, les factures HODL et le système d'attestation Zaplocker Nostr pour permettre aux utilisateurs qui ne sont pas en ligne 24 heures sur 24 et 7 jours sur 7 de recevoir des paiements sur un éclair statique Address. Les utilisateurs doivent simplement se connecter à leurs portefeuilles ZEUS dans les 24 heures pour réclamer les paiements, sinon ils seront renvoyés à l'expéditeur.


Si vous activez le "mode persistant", tous les paiements versés à votre LN Address seront reçus instantanément.


Découvrez le fonctionnement des paiements [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) et les frais de [ZeusPay](https://docs.zeusln.app/lightning-Address/fees).


**G - Adresses Onchain**


Dans cette section, vous pouvez consulter les adresses onchain générées pour un meilleur contrôle des pièces


**H - Contacts**


Un nouveau carnet de contacts a été introduit dans Zeus v 0.8.0 que vous pouvez utiliser pour envoyer rapidement des paiements à vos amis et à votre famille, avec également la possibilité d'importer vos contacts depuis Nostr.


Entrez simplement votre Nostr npub ou NIP-05 Address lisible par l'homme, et ZEUS interrogera Nostr pour tous vos contacts. A partir de là, vous pouvez envoyer un paiement rapide à un contact, ou importer tous les contacts ou certains d'entre eux dans votre carnet de contacts local


Voici une courte vidéo sur la configuration et l'utilisation de vos contacts Zeus :


**I - Outils**


Ici, nous avons plusieurs sous-sections avec plus d'outils :



- comptes_ - ici, vous pouvez importer des comptes / portefeuilles externes, des portefeuilles Cold, des portefeuilles Hot, pour les contrôler ou les utiliser comme source de financement externe pour vos canaux de nœuds Zeus. Cette fonctionnalité est encore expérimentale.
- accélérer la transaction_ - Cette fonction peut être utile lorsque vous avez un tx bloqué dans Mempool et que vous souhaitez augmenter les frais. Vous devrez fournir la sortie du tx à partir des détails du tx et sélectionner le nouveau tarif que vous souhaitez utiliser. Il doit être plus élevé que le précédent et nécessite que vous ayez plus de fonds disponibles dans votre onchain Wallet.


![Image](assets/en/05.webp)


Vous devez aller dans votre tx en attente et copier le point de sortie txid. Ensuite, venez dans cette section et collez-la, puis sélectionnez la nouvelle taxe que vous voulez utiliser pour la faire sauter. Un nouvel écran s'affichera avec les frais recommandés à ce moment-là, ou vous pouvez en définir un personnalisé. N'oubliez pas qu'il DOIT être plus élevé que le précédent.


Il est toujours préférable de garder un UTXO avec un maximum de 100k Sats dans votre Zeus onchain Wallet, afin d'être en mesure de l'utiliser pour augmenter les frais lorsque cela est nécessaire.



- signer ou vérifier_ - Avec cette fonction, vous pouvez signer un message spécifique avec vos clés Wallet. Elle peut également être utilisée pour vérifier un message afin de prouver qu'il provient d'une clé Wallet spécifique.
- convertisseur de devises - un outil simple pour calculer le taux de conversion entre BTC et d'autres devises fiduciaires.


**J - Marchandises et soutien**


Vous trouverez ici plus d'informations et de liens sur Zeus, la boutique en ligne, les sponsors, les médias sociaux.


**K - Aide**


Dans cette dernière section, vous trouverez des liens vers la page de documentation de Zeus, Github issues (si vous voulez poster un bug ou une demande directement aux développeurs de l'application), l'assistance par email.



### ÉTAPE 2 - COMMENCER À UTILISER LE NOEUD ZEUS



Rappelez-vous, Zeus est principalement destiné à être utilisé comme un LN Wallet, pour des paiements faciles et rapides sur LN. Bien sûr, il contient également un Wallet onchain, mais celui-ci doit être utilisé exclusivement pour ouvrir / fermer des canaux LN et non pour des paiements réguliers d'un café.


Veuillez lire mon autre guide sur [comment devenir votre propre banque en utilisant les 3 niveaux de Stash](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


A ce moment-là, l'utilisateur a deux possibilités pour commencer à utiliser Zeus :



- Directement sur LN, en utilisant le canal 0-conf de Olympus LSP
- Déposez d'abord dans l'onchain Wallet et ouvrez ensuite un canal LN normal avec le pair que vous souhaitez.


#### Méthode A - Utilisation de l'Olympus LSP


Il s'agit d'un moyen très simple et direct d'intégrer un nouvel utilisateur LN à Zeus. Il peut s'agir d'un tout nouvel utilisateur Bitcoin qui n'a jamais utilisé de Sats, qui a été embarqué par un ami, ou d'un nouveau commerçant qui commence à effectuer son premier paiement LN.


Par défaut, Zeus utilise son propre LSP, Olympus. Mais plus tard, vous pourrez passer à d'autres LSP qui prennent en charge ce protocole 0-conf pour ouvrir des canaux.


En créant simplement une Invoice sur votre Zeus (indiquez le montant et cliquez sur le bouton "demander"), vous pourrez recevoir ces Sats immédiatement.


La Invoice que vous avez generate sera [enveloppée](https://docs.zeusln.app/lsp/wrapped-invoices) et les frais associés au service vous seront présentés s'ils sont payés. Cette Invoice enveloppée contient des indications de route vers votre nœud Zeus, de sorte que le FSL puisse trouver votre nouveau nœud et ouvrir un canal avec les nouveaux fonds que vous déposez.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Afin d'obtenir un canal LN du FSL avec les fonds que vous souhaitez recevoir la première fois, cette Invoice doit être payée à partir d'une autre LN Wallet et attendre quelques instants jusqu'à ce que le FSL ouvre le canal vers votre nœud Zeus, déduise les frais et pousse le montant restant du paiement de votre côté du canal.


Tout ce que vous avez à faire est de payer le Invoice généré pour vous dans ZEUS avec un autre Wallet, et votre canal s'ouvrira instantanément. [Veuillez consulter les tarifs de Zeus LSP](https://docs.zeusln.app/lsp/fees).


Un autre avantage du paiement pour un canal est le routage sans frais. Cela signifie que lors de l'acheminement des paiements, le premier saut à travers OLYMPUS by ZEUS n'entraîne pas de frais d'acheminement. Notez que les sauts au-delà d'OLYMPUS by ZEUS vous seront toujours facturés.


Une fois que le canal est prêt, cliquez sur le bouton de droite en bas de l'écran, qui affiche les canaux de Zeus.


![Image](assets/en/08.webp)


Vous verrez un canal comme celui-ci, montrant votre côté de l'équilibre du canal :


![Image](assets/en/09.webp)


Plus vous dépenserez dans ce canal, plus vous aurez de liquidités entrantes. Plus vous recevrez de Sats dans ce canal, moins vous aurez d'espace de liquidité entrante.


Voici une démonstration visuelle simple (par Rene Pickhardt) du fonctionnement des canaux LN :


A ce stade, compte tenu de l'écran de démonstration des chaînes, cliquez sur le nom de la chaîne et vous obtiendrez plus de détails à son sujet.


Vous disposez d'un canal unique avec Olympus, d'une capacité totale de 490 000 Sats, avec un solde de 378k Sats de votre côté et 88k Sats du côté d'Olympus. Cela signifie que vous pouvez recevoir au maximum 88k Sats de plus dans le même canal.


Si vous avez besoin de recevoir plus de 88k Sats (la liquidité entrante disponible dans ce cas), disons 500k Sats supplémentaires, le simple fait de créer un nouveau LN Invoice avec ce montant déclenchera une nouvelle demande de canal au LSP Olympus. Vous obtiendrez donc un deuxième canal.


C'est pourquoi, afin d'éviter de payer plus de frais pour l'ouverture de plusieurs canaux, il est recommandé d'ouvrir d'abord un canal plus grand, disons 1-2M Sats. Une fois le canal ouvert, vous pouvez échanger une partie de ces Sats contre une chaîne, disons 50%, en utilisant n'importe quel service d'échange externe décrit dans ce guide.


Une fois que vous avez quitté ce canal, disons 50 %, et que vous avez récupéré le Sats dans votre propre Zeus onchain Wallet, vous êtes prêt à passer à la méthode suivante d'ouverture d'un nouveau canal - à partir de la balance onchain.


#### Méthode B - Utiliser votre solde onchain


Avec cette méthode, vous pouvez ouvrir des canaux vers n'importe quel autre nœud LN, y compris le même LSP Olympus. Mais si vous avez déjà un canal avec Olympus, il est recommandé d'en avoir un aussi avec un autre nœud, pour plus de fiabilité et aussi pour utiliser le MPP (paiement en plusieurs parties).


![Image](assets/en/10.webp)


Voici un exemple de paiement d'un LN Invoice à l'aide du MPP. Comme vous pouvez le voir, en bas de l'écran, vous avez "paramètres" et cela ouvre une page déroulante avec plus de détails sur le paiement que vous êtes sur le point d'effectuer. Dans cet écran, si vous avez au moins 2 canaux ouverts, la fonction MPP sera activée par défaut. Vous pouvez également activer AMP (atomic multi-path) et définir les parties spécifiques que vous souhaitez. Il s'agit d'une fonction très puissante !


Pour un nœud privé comme Zeus, je recommanderais d'avoir 2-3 bons canaux (max. 4-5), avec de bons LSP et une bonne liquidité pour couvrir tous vos besoins pour payer ou recevoir Sats sur LN. [Voir plus de conseils sur la liquidité des nœuds LN dans ce guide](/nodes/managing-lightning-node-liquidity-fr.html). Voici également un autre [guide général sur la liquidité du nœud LN](https://Bitcoin.design/guide/how-it-works/liquidity/) de l'équipe de conception du nœud Bitcoin.


Choisir les bons nœuds pairs, je le sais, n'est pas une tâche facile, même pour les utilisateurs expérimentés. (https://github.com/ZeusLN/zeus/discussions/2265), voici les nœuds pairs que j'ai testés moi-même avec Zeus (j'ai essayé de me connecter uniquement à des nœuds LND pour éviter les problèmes d'incompatibilité)


Voici également une liste de nœuds pairs certifiés pour Zeus. Si vous en connaissez de bons, vous pouvez les ajouter à cette liste.


Vous pouvez ouvrir un canal dans Zeus en cliquant sur l'icône du canal dans le coin inférieur droit de l'écran principal, puis en cliquant sur l'icône + dans le coin supérieur droit.


![Image](assets/en/11.webp)


Si vous souhaitez ouvrir un canal avec un nœud spécifique, cliquez sur (A) dans le coin supérieur pour scanner le QR nodeID du nœud (sur Mempool, Amboss, 1ML, vous pouvez obtenir ce QR) et tous les détails de l'homologue seront renseignés.


RAPPEL :


- Les noeuds intégrés de Zeus n'utilisent pas le service Tor ! N'essayez donc pas d'ouvrir des canaux avec des nœuds qui utilisent Tor ! Vous vous faites plus de mal que vous ne gagnez en confidentialité. Tor pour LN n'offre pas plus de confidentialité mais ajoute plus de problèmes.
- choisissez judicieusement vos pairs, il vaut mieux que ce soit de bons LSP, de bons nœuds de routage, pas des nœuds de plébéiens aléatoires qui pourraient fermer vos canaux et ne pourraient pas offrir une bonne liquidité. [J'ai écrit un guide dédié (https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) sur la liquidité et les exemples de nœuds.


Si vous cliquez directement sur le bouton "Ouvrir un canal vers Olympus", vous remplirez les champs requis pour ouvrir un canal vers [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Contrairement aux canaux LSP payants, votre canal nécessitera une confirmation On-Chain, en utilisant vos fonds onchain (vous pouvez sélectionner vos UTXO dans la vue des canaux ouverts) ; il ne s'ouvrira pas instantanément. Veuillez d'abord consulter les frais Mempool actuels et les ajuster en conséquence, en fonction de la rapidité avec laquelle vous souhaitez ouvrir ce canal.


Avant d'appuyer sur le bouton pour ouvrir le canal, faites glisser les options avancées vers le bas :


![Image](assets/en/12.webp)


Vous devrez également vous assurer que le canal n'est pas annoncé (privé). Par défaut, l'option est désactivée pour les canaux annoncés. Il n'est pas recommandé d'activer cette option pour les nœuds intégrés à Zeus. Elle n'est utile que lorsque vous utilisez Zeus avec votre nœud distant, en tant que nœud de routage public.


Contrairement aux canaux payés par les PSL, vous ne bénéficierez pas d'un routage à frais zéro en ouvrant des canaux avec cette méthode.


Et voilà, il suffit de cliquer sur le bouton "Open Channel" et d'attendre que le tx soit confirmé par les mineurs. Une fois le canal ouvert, vous pouvez effectuer les transactions que vous souhaitez avec le Sats à partir de vos canaux.


Gardez à l'esprit que ces canaux auront tout l'équilibre de VOTRE côté, donc vous n'aurez pas de liquidité entrante. Comme je l'ai déjà dit, échangez ou dépensez une partie de la Sats pour acheter des choses sur la LN afin de "faire plus de place" pour recevoir.


Considérez vos canaux LN comme un verre d'eau. Vous versez de l'eau (Sats) dans un verre vide (votre canal) jusqu'à ce que vous le remplissiez. Vous ne pouvez pas verser plus d'eau tant que vous n'en avez pas bu (dépense / échange). Lorsque le verre est presque vide, versez-y plus d'eau (Sats) en utilisant un service d'échange. [Pour en savoir plus sur les services d'échange externes, cliquez ici](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Il existe également d'autres services de PSL qui vous vendent des canaux entrants : LNBig ou Bitrefill. Je pense qu'il existe d'autres services de ce type, mais je ne m'en souviens pas pour l'instant.


Si vous avez besoin d'un canal LN pratiquement vide (le solde est à 100 % du côté de l'homologue dès le départ) pour recevoir plus de paiements que vous ne pouvez en gérer sur vos canaux existants déjà remplis, cela pourrait être une très bonne option. Vous paierez une redevance spécifique pour l'ouverture de ces canaux et vous obtiendrez beaucoup d'espace entrant.



## TRUCS ET ASTUCES


### Limites des réserves entrantes


Actuellement, en raison de certaines limitations du code LN, il n'est pas possible de recevoir exactement le montant affiché dans "Inbound". Gardez toujours à l'esprit que vous devriez établir vos factures avec un montant légèrement inférieur, respectivement le montant de la "réserve locale du canal".


![Image](assets/en/13.webp)


Comme vous pouvez le voir dans l'image ci-dessus, le "inbound" affiche que je peux encore recevoir 5101 Sats, mais en fait, en ce moment, il est impossible d'en recevoir plus. Et vous pouvez observer que c'est le même montant que la "Réserve locale".


Gardez donc à l'esprit que, lorsque vous établissez des factures à recevoir, vous devez également tenir compte de la liquidité de vos canaux et déduire la réserve locale de ce montant, si vous voulez pousser à la limite le montant à recevoir.


### Conseils rapides pour les nouveaux utilisateurs qui commencent à utiliser le nœud Zeus :



- Saisissez correctement vos nouveaux canaux.


Par exemple, si vous savez que vous recevrez dans une semaine, disons 1 million de Sats, ouvrez un canal de 2 millions de Sats et échangez dans le compte Wallet de la chaîne ou dans un autre compte LN de garde (temporaire) 50-60% de vos liquidités sortantes. Soyez toujours prêt à recevoir plus de liquidités. Une fois que vous aurez besoin de plus de liquidités dans vos canaux Zeus, vous pourrez les retirer des comptes de dépôt.


Si vous savez que vous enverrez, par exemple, 500 000 Sats par semaine, ouvrez un canal de 1 million de Sats. Vous disposerez ainsi d'une réserve jusqu'à ce que vous la remplissiez à nouveau.



- Si vous êtes un commerçant et que vous recevez régulièrement plus que vous ne dépensez, achetez un canal d'entrée dédié. C'est le moyen le plus économique. Vous payez une redevance minime et vous obtenez un canal "vide".



- N'ouvrez pas de petits canaux insignifiants de 50-100-300-500k Sats. Vous les remplirez en quelques jours, même si vous ne les utilisez que pour des zaps. Ouvrez des canaux plus grands et différents, PAS un seul canal.


Une fois que vous avez ouvert un canal plus important, vous pouvez toujours utiliser des swaps sous-marins externes pour transférer des Sats dans vos portefeuilles onchain (y compris vers Zeus onchain). Garder un équilibre entre les liquidités entrantes et sortantes est une bonne chose et vous pouvez également "réutiliser" ces Sats pour ouvrir d'autres canaux si vous le souhaitez.


### Enveloppé Invoice


Si vous souhaitez ajouter plus de confidentialité lors de la réception, vous pouvez utiliser la méthode "Invoice enveloppé". Rappel : pour pouvoir utiliser cette méthode, vous devez disposer d'un canal avec Olympus LSP. Les factures enveloppées "cachent" la destination finale (votre nœud Zeus) et affichent votre nœud LSP comme destination pour le payeur.


Pour obtenir un Invoice emballé, allez à l'écran principal du clavier, indiquez le montant et cliquez sur demander. Un code QR normal s'affichera pour votre Invoice. Cliquez ensuite sur le bouton "X" en haut à droite et vous serez redirigé vers d'autres options pour le Invoice.


![Image](assets/en/14.webp)


Vous devez maintenant activer l'option "Enable LSP" en haut de la page et cliquer sur le bouton "Create Invoice". Cette option créera la Invoice enveloppée et, n'oubliez pas, facturera une petite redevance.


### Factures avec indications d'itinéraires


Cette fonction est très utile si vous souhaitez gérer la liquidité de plusieurs canaux entrants. En pratique, vous pouvez indiquer vers quel canal entrant vous souhaitez recevoir le Sats d'un Invoice.


Cette fonction peut également être utilisée pour le rééquilibrage circulaire, lorsque vous souhaitez déplacer des liquidités d'un canal rempli vers un autre canal appauvri.


Comment créer une Invoice avec des indications d'itinéraires ?



- Sur l'écran principal, faites glisser vers la droite le tiroir LN et cliquez sur "Recevoir"
- Dans la configuration Invoice, allez dans la partie inférieure et activez le bouton "Insert route hints", puis sélectionnez l'onglet "Custom". Un écran s'ouvrira avec tous les canaux disponibles. Sélectionnez celui que vous voulez recevoir.
- Remplissez tous les autres détails de la Invoice, le montant, le mémo, etc. et cliquez sur "créer la Invoice".
- Payer cette Invoice amènera la Sats dans le canal indiqué.


Si vous voulez vous payer ce Invoice (rééquilibrage circulaire), lorsque vous le payez à partir du même nœud Zeus, dans l'écran de paiement, sélectionnez le canal de sortie (celui qui a le plus de liquidité) que vous voulez utiliser pour l'envoi du paiement.


### Payer avec Keysend


Keysend est une fonctionnalité de LN très sous-estimée et les utilisateurs devraient l'utiliser plus souvent.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) permet aux utilisateurs de la Lightning Network d'envoyer des paiements à d'autres personnes, directement sur leur clé publique, à condition que leur nœud dispose de canaux publics et que la fonction Keysend soit activée. Keysend n'exige pas que le bénéficiaire émette une Invoice.


Comment faire avec Zeus ?


Il suffit de scanner ou de copier le nodeID de destination (ou d'utiliser Zeus contacts pour enregistrer vos nœuds de destination habituels en tant que contacts), puis de cliquer sur le bouton "Envoyer" dans l'écran principal de Zeus. Dans cet écran, collez le nodeID ou sélectionnez-le dans vos contacts.


Mettez le montant de Sats, un message si nécessaire (oui, vous pouvez aussi l'utiliser comme chat secret sur LN) et cliquez sur le bouton "Envoyer". C'est fait !


![Image](assets/en/15.webp)


Si vous disposez d'un canal direct avec l'homologue de destination, il n'y aura PAS de frais.


Si vous n'avez pas de canal direct avec l'homologue de destination, le paiement keysend paiera les frais comme un paiement LN Invoice normal, acheminé sur un chemin réglementaire comme tout autre paiement. Seulement, n'oubliez pas qu'il ne restera aucune trace en tant que LN Invoice.


## Conlusion


Je vous recommande de lire le guide de suivi [Utilisation avancée de Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) qui contient plus d'instructions et de cas d'utilisation.


Et... c'est tout ! A partir de maintenant, vous utilisez Zeus Node comme un BTC/LN Wallet normal sur votre mobile. L'interface utilisateur est assez simple et facile à utiliser, intuitive pour tout type d'utilisateur, je ne pense pas avoir à entrer dans plus de détails sur la façon d'effectuer et de recevoir des paiements.


En conclusion, voici un tableau comparatif de la protection de la vie privée :


![Image](assets/en/16.webp)

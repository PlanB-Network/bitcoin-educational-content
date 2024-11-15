---
term: CHAUMIAN COINJOIN
---

Protocole de coinjoin qui utilise les signatures aveugles de David Chaum et Tor pour les communications entre les participants et le serveur du coordinateur. L'objectif d'un coinjoin chaumien est de garantir aux participants que le coordinateur ne peut ni voler les bitcoins, ni faire de liens entre les inputs et les outputs. 

Pour ce faire, les utilisateurs soumettent leur input et une adresse de réception cryptographiquement aveuglées au coordinateur. Cette adresse, une fois démasquée, sera destinée à recevoir les bitcoins en output de coinjoin. Le coordinateur signe ces tokens et les renvoie aux utilisateurs. Les utilisateurs se reconnectent ensuite de manière anonyme au serveur du coordinateur avec une nouvelle identité Tor et révèlent ensuite leurs adresses de sortie en clair pour la construction de la transaction. Le coordinateur peut vérifier que toutes ces adresses de réception proviennent bien d'utilisateurs légitimes, puisqu'il a signé leur version aveuglée auparavant avec sa clé privée. En revanche, il ne peut pas associer une adresse de sortie spécifique à un utilisateur donné en entrée. Il n'y a donc aucun lien entre les entrées et les sorties, même du point de vue du coordinateur. Une fois la transaction construite par le coordinateur, il la renvoie aux participants qui la signent afin de déverrouiller leur input, après avoir vérifier que leur output se trouve bien dans cette transaction. Les participants envoient la signature au coordinateur. Une fois toutes les signatures collectées, le coordinateur peut diffuser la transaction coinjoin sur le réseau Bitcoin.

![](../../dictionnaire/assets/38.webp)

Cette méthode garantit que le coordinateur ne peut ni compromettre l'anonymat des participants, ni voler les bitcoins durant tout le processus de coinjoin.

Il est difficile de déterminer avec certitude qui a introduit en premier l'idée du coinjoin sur Bitcoin, et qui a eu l'idée d'utiliser les signatures aveugles de David Chaum dans ce contexte. On pense souvent que c'est Gregory Maxwell qui en a parlé en premier dans [un message sur BitcoinTalk en 2013](https://bitcointalk.org/index.php?topic=279249.0) :

> *"En utilisant les signatures aveugles de Chaum : Les utilisateurs se connectent et fournissent des inputs (et des adresses de change) ainsi qu'une version cryptographiquement aveuglée de l'adresse vers laquelle ils souhaitent envoyer leurs pièces privées ; le serveur signe les jetons et les leur renvoie. Les utilisateurs se reconnectent anonymement, démasquent leurs adresses de sortie et les renvoient au serveur. Le serveur peut voir que toutes les sorties ont été signées par lui et que, par conséquent, toutes les sorties proviennent de participants valides. Plus tard, les personnes se reconnectent et signent."*

Maxwell, G. (2013, 22 août). *CoinJoin: Bitcoin privacy for the real world*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

Toutefois, il existe d'autres mentions antérieures, à la fois pour les signatures de Chaum dans le cadre du mixage, mais également pour les coinjoins. [En juin 2011, Duncan Townsend présente sur BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) un mélangeur qui utilise les signatures de Chaum d'une manière assez similaire aux coinjoins chaumiens modernes. Dans le même thread, on peut retrouver [un message de hashcoin en réponse à Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) pour améliorer son mélangeur. Ce message présente justement ce qui ressemble le plus aux coinjoins. On retrouve également une mention d'un système similaire dans [un message d'Alex Mizrahi en 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), alors qu'il conseillait les créateurs de Tenebrix. Le terme en lui-même de « coinjoin » n'aurait pas été inventé par Greg Maxwell, mais il viendrait d'une idée de Peter Todd.



---
name: Watch Tower
description: Comprendre et utiliser une tour de guet
---

## Comment fonctionnent les tours de guet ?

Partie essentielle de l'écosystème du Lightning Network, les tours de guet offrent un degré supplémentaire de protection aux canaux de foudre des utilisateurs. Leur principale responsabilité est de surveiller la santé des canaux et d'intervenir si l'une des parties du canal tente de tromper l'autre.

Comment une tour de guet peut-elle déterminer si un canal a été compromis ? La tour de guet reçoit les informations dont elle a besoin du client, l'une des parties du canal, afin d'identifier et de répondre correctement à toute violation. Les détails de la transaction la plus récente, l'état actuel du canal et les informations nécessaires pour créer des transactions de pénalité sont fréquemment incluses dans ces informations. Avant de transmettre les données à la tour de guet, le client peut les chiffrer pour protéger la vie privée et la confidentialité. Cela empêche la tour de guet de déchiffrer les données chiffrées à moins qu'une violation n'ait réellement eu lieu, même si elle obtient les données. La vie privée du client est protégée par ce système de chiffrement, qui empêche également la tour de guet d'accéder à des données privées sans autorisation.

JohnOnChain nous partage ses connaissances :

- https://github.com/lightningnetwork/lnd/blob/master/docs/watchtower.md
- https://twitter.com/JohnOnChain/status/1420070549276053512?t=5Z_08WHh86HPj6XxMjJAaw&s=19
- https://twitter.com/JohnOnChain/status/1420399995556188168?t=PxNgD4EFsDR_t-YntfYDQQ&s=19

![vidéo tuto de johnOnChain](https://tube.nuagelibre.fr/videos/watch/eb4065e5-cf0a-427e-96a9-1638f2efb91f)

## Comment configurer votre propre Eye of Satoshi et commencer à contribuer

L'Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) est une tour de guet Lightning non-custodial conforme à [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Il comporte deux composants principaux :

1. teos : incluant une interface en ligne de commande (CLI) et la fonctionnalité centrale côté serveur de la tour. Deux binaires - teosd et teos-cli - seront produits lorsque cette caisse sera construite.

2. teos-common : incluant des fonctionnalités partagées côté serveur et côté client (utiles pour créer un client).

Pour exécuter la tour avec succès, vous devrez exécuter bitcoind avant d'exécuter la tour avec la commande teosd. Avant d'exécuter ces deux commandes, vous devez configurer votre fichier bitcoin.conf. Voici les étapes à suivre :

1. Installez Bitcoin Core à partir de la source ou téléchargez-le. Après avoir téléchargé, placez le fichier bitcoin.conf dans le répertoire utilisateur de Bitcoin Core. Consultez ce lien pour plus d'informations sur l'endroit où placer le fichier, car cela dépend du système d'exploitation que vous utilisez.

2. Après avoir identifié l'endroit où le fichier doit être créé, ajoutez ces options :

```
#RPC
server=1
rpcuser=<votre-utilisateur>
rpcpassword=<votre-mot-de-passe>

#chain
regtest=1
```

- server : pour les requêtes RPC
- rpcuser et rpcpassword : les clients RPC peuvent s'authentifier auprès du serveur
- regtest : non requis mais utile si vous prévoyez de développer.

rpcuser et rpcpassword doivent être choisis par vous. Ils doivent être écrits sans guillemets. Exemple :

```
rpcuser=aniketh
rpcpassword=strongpassword
```

Maintenant, si vous exécutez bitcoind, il devrait démarrer le nœud.

1. Pour la partie tour, tout d'abord, vous devez installer teos à partir de la source. Suivez les instructions données dans ce lien.
2. Après avoir installé avec succès teos sur votre système et exécuté les tests, vous pouvez passer à la dernière étape qui consiste à configurer le fichier teos.toml dans le répertoire utilisateur de teos. Le fichier doit être placé dans un dossier appelé .teos (attention au point) sous votre dossier personnel. Par exemple, /home/<votre-nom-d'utilisateur>/.teos pour Linux. Une fois que vous avez trouvé l'emplacement, créez un fichier teos.toml et définissez ces options correspondant aux choses que nous avons modifiées sur bitcoind.

```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <votre-utilisateur>
btc_rpc_password = <votre-mot-de-passe>
```

Notez que le nom d'utilisateur et le mot de passe doivent être écrits entre guillemets, c'est-à-dire, pour le même exemple qu'auparavant :

```
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```

Une fois que vous avez fait cela, vous devriez être prêt à exécuter la tour. Étant donné que nous fonctionnons sur regtest, il est probable qu'aucun bloc ne soit extrait dans notre réseau de test bitcoin la première fois que la tour s'y connecte (si des blocs sont extraits, quelque chose ne va certainement pas). La tour construit un cache interne des 100 derniers blocs de bitcoind, donc lors de la première exécution, nous pouvons obtenir l'erreur suivante :

> ERREUR [teosd] Pas assez de blocs pour démarrer la tour (nécessaire : 100). Minez au moins 100 de plus.

Étant donné que nous fonctionnons sur regtest, nous pouvons extraire un bloc en émettant une commande RPC, sans avoir besoin d'attendre les 10 minutes de temps médian que nous voyons habituellement dans d'autres réseaux (comme mainnet ou testnet). Consultez l'aide de bitcoin-cli et recherchez comment extraire des blocs. Si vous avez besoin d'aide, vous pouvez consulter cet article.

![image](assets/2.webp)

C'est tout, vous avez réussi à exécuter la tour. Félicitations. 🎉

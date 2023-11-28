---
name: Noeud Bitcoin Core (mac & windows)
description: Installer Bitcoin Core sur Mac ou Windows
---

Installer Bitcoin Core sur votre ordinateur habituel est possible, mais ce n'est pas idéal. Si vous ne dérange pas de laisser votre ordinateur allumé 24h/24 et 7j/7, cela fonctionnera bien. Si vous avez besoin d'éteindre l'ordinateur, il est ennuyeux d'attendre que le logiciel se synchronise à chaque fois que vous le rallumez.

Ces instructions sont destinées aux utilisateurs de Mac ou de Windows. Les utilisateurs de Linux n'auront probablement pas besoin de mon aide, mais les instructions pour Linux sont très similaires à celles de Mac.

## Commencer avec un ordinateur propre

Idéalement, vous voulez utiliser un ordinateur propre, sans logiciel malveillant. Même si vous utilisez un portefeuille matériel, un logiciel malveillant peut vous tromper et vous faire perdre vos bitcoins.

Vous pouvez soit nettoyer un ancien ordinateur et l'utiliser comme un ordinateur dédié à Bitcoin, soit acheter un ordinateur/portable dédié.

## Le disque dur

Bitcoin Core occupera environ 400 gigaoctets de données sur votre disque dur et continuera à croître. Vous pouvez utiliser votre disque dur interne, mais vous pouvez également connecter un disque dur externe. Je vais expliquer les deux options. Idéalement, vous devriez utiliser un disque dur à semi-conducteurs. Si vous avez un vieil ordinateur, il n'en a probablement pas un intégré. Achetez simplement un SSD externe de 1 ou 2 téraoctets et utilisez-le. Le disque dur classique fonctionnera probablement, mais vous pourriez rencontrer des problèmes et il sera beaucoup plus lent.

![image](assets/1.png)

## Télécharger Bitcoin Core

Allez sur bitcoin.org (assurez-vous de ne pas aller sur bitcoin.com, qui est un site de shitcoin détenu par Roger Ver, qui trompe les gens pour qu'ils achètent Bitcoin Cash au lieu de Bitcoin)

Une fois là-bas, il n'est étrangement pas évident où obtenir le logiciel. Allez dans le menu des ressources et cliquez sur "Bitcoin Core", comme indiqué ci-dessous :

![image](assets/2.png)

Cela vous amènera à la page de téléchargement :

![image](assets/3.png)

Cliquez sur le bouton orange "Télécharger Bitcoin Core" :

![image](assets/4.png)

Il y a plusieurs options à choisir, en fonction de votre ordinateur. Les deux premières sont pertinentes pour ce guide ; choisissez Windows ou Mac dans la barre de gauche. Le téléchargement commencera après avoir cliqué dessus, probablement dans votre répertoire Téléchargements.

## Vérifier le téléchargement (partie 1)

Vous avez besoin du fichier qui contient les hachages des différentes versions. Ce fichier était autrefois sur la page de téléchargement de bitcoin.org, mais il a maintenant été déplacé vers bitcoincore.org/en/download :

![image](assets/5.png)

Vous avez besoin du fichier de hachages binaires SHA256. Ce fichier contient les hachages SHA256 des différents packages de téléchargement de Bitcoin Core.

Ensuite, nous devons hacher le téléchargement de Bitcoin Core et le comparer à ce que le fichier dit que le hachage devrait être. Ainsi, nous saurons que le téléchargement est identique à ce qui est attendu, selon bitcoincore.org.

Accédez à nouveau au répertoire Téléchargements et exécutez cette commande (remplacez les X par le nom exact du fichier de téléchargement du nœud complet Bitcoin) :

```
POUR MAC —–> shasum -a 256 XXXXXXXXXXXX
POUR WINDOWS —–> certutil -hashfile XXXXXXXXXXX SHA256
```

Vous obtiendrez un résultat de hachage. Prenez note de celui-ci et comparez-le au hachage contenu dans le fichier SHA256SUMS.
Si les sorties sont identiques, alors vous avez vérifié qu'aucun bit de données n'a été altéré... presque. Nous devons encore nous assurer que le fichier SHA256SUMS n'est pas malveillant.
Pour passer à l'étape suivante, nous devons avoir gpg installé sur notre ordinateur.

Pour cela, consultez mon guide SHA256/gpg, et faites défiler jusqu'à la section "Télécharger gpg", puis recherchez le sous-titre de votre système d'exploitation. Ensuite, revenez ici.

## Obtenir la clé publique

De retour sur la page de téléchargement, obtenez le fichier de signatures de hachage SHA256

![image](assets/6.png)

Cliquez dessus et enregistrez le fichier sur le disque, de préférence dans le répertoire Téléchargements.

Ce fichier contient des signatures de différentes personnes, du fichier SHA256SUMS.

Nous voulons la clé publique du développeur principal, Wladimir J. van der Laan, dans le trousseau de clés de notre ordinateur. Son identifiant de clé publique est :
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Copiez ce texte dans la commande suivante :

```
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```

Par curiosité, à tout moment, vous pouvez voir quelles clés sont dans le trousseau de clés de l'ordinateur avec cette commande :

```
gpg --list-keys
```

## Vérifier le téléchargement (partie 2)

Nous avons la clé publique, nous pouvons maintenant vérifier le fichier SHA256SUMS qui contient les hachages du téléchargement de Bitcoin Core, ainsi que la signature de ces hachages.

Ouvrez à nouveau le Terminal ou CMD, et assurez-vous d'être dans le répertoire Téléchargements. À partir de là, exécutez cette commande :

```
gpg –verify SHA256SUMS.asc SHA256SUMS
```

Le premier fichier répertorié est l'orthographe exacte du fichier de signature. Le deuxième fichier répertorié devrait être l'orthographe exacte du fichier texte contenant les hachages. Les deux fichiers doivent être dans le même répertoire et vous devez être dans le répertoire des fichiers, sinon vous devez saisir le chemin complet pour chaque fichier.

Voici la sortie que vous devriez obtenir

![image](assets/7.png)

Il est sûr d'ignorer le message d'avertissement - cela vous rappelle simplement que vous n'avez pas rencontré Wladimir à une étape clé et lui avez personnellement demandé quelle était sa clé publique, puis avez dit à votre ordinateur de faire entièrement confiance à cette clé.

Si vous avez reçu ce message, vous savez maintenant que le fichier SHA256SUMS.asc n'a pas été altéré après que Wladimir l'ait signé.

## Installer Bitcoin Core

Vous ne devriez pas avoir besoin d'instructions détaillées sur la façon d'installer le programme.

![image](assets/8.png)

## Exécuter Bitcoin Core

Sur un Mac, vous pourriez obtenir un avertissement (Apple est toujours anti-Bitcoin)

![image](assets/9.png)

Cliquez sur OK, puis ouvrez vos Préférences Système

![image](assets/10.png)

Cliquez sur l'icône Sécurité et confidentialité :

![image](assets/11.png)

Ensuite, cliquez sur "ouvrir quand même" :

![image](assets/12.png)

L'erreur apparaîtra à nouveau, mais cette fois-ci vous aurez un bouton OUVRIR disponible. Cliquez dessus.

![image](assets/13.png)

Bitcoin Core devrait se charger et vous serez présenté avec quelques options :

![image](assets/14.png)

Ici, vous pouvez choisir d'utiliser le chemin d'accès par défaut pour le téléchargement de la blockchain, ou vous pouvez choisir votre disque externe. Je recommande de ne pas modifier le chemin d'accès par défaut si vous utilisez le disque interne, cela facilite la configuration lorsque vous installez d'autres logiciels pour communiquer avec Bitcoin Core.
Vous pouvez choisir d'exécuter un nœud élagué, cela permet d'économiser de l'espace, mais limite ce que vous pouvez faire avec votre nœud. De toute façon, vous téléchargerez l'intégralité de la blockchain et la vérifierez, donc si vous avez de l'espace, conservez ce que vous avez téléchargé et ne l'élaguez pas si vous pouvez l'éviter.

Une fois que vous confirmez, le téléchargement de la blockchain commencera. Cela prendra plusieurs jours.

![image](assets/15.png)

Vous pouvez éteindre l'ordinateur et revenir pour télécharger si vous le souhaitez, cela ne causera aucun dommage.

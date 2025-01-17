---
name: GnuPG
description: Comment vérifier l'intégrité et l'authenticité d'un logiciel ?
---
![cover](assets/cover.webp)

Lorsqu'on télécharge un logiciel, il est très important de s'assurer qu'il n'a pas été altéré et qu'il provient bien de la source officielle. C'est particulièrement vrai pour les logiciels liés à Bitcoin, comme les logiciels de portefeuille, qui vous permettent de sécuriser les clés donnant accès à vos fonds. Dans ce tutoriel, nous allons voir comment vérifier l'intégrité et l'authenticité d'un logiciel avant de l'installer. Nous allons prendre pour exemple Sparrow Wallet, un des logiciels de portefeuille préféré des bitcoiners, mais la marche à suivre sera la même pour n'importe quel autre logiciel.

La vérification de l'intégrité consiste à s'assurer que le fichier téléchargé n'a pas été modifié en comparant son empreinte numérique (c'est-à-dire son hachage) avec celle fournie par le développeur officiel. Si les deux correspondent, cela signifie que le fichier est identique à l'original et n'a pas été corrompu ou modifié par un attaquant.

La vérification de l'authenticité, quant à elle, garantit que le fichier provient bien du développeur officiel et non d'un imposteur. Cela se fait par la vérification d'une signature numérique. Cette signature prouve que le logiciel a été signé avec la clé privée du développeur légitime.

Si ces vérifications ne sont pas effectuées, on court le risque d'installer un logiciel malveillant qui pourrait contenir un code modifié. Ce code pourrait permettre soit de voler des informations comme vos clés privées, soit de bloquer l'accès à vos fichiers. Ce type d'attaque est assez fréquent, notamment dans le cadre des logiciels open-source où des versions contrefaites peuvent être distribuées.

Pour effectuer cette vérification, nous allons utiliser deux outils : les fonctions de hachage pour vérifier l'intégrité, et GnuPG, un outil open-source qui implémente le protocole PGP, pour vérifier l'authenticité.

## Prérequis

Si vous êtes sous **Linux**, GPG est préinstallé sur la plupart des distributions. Si ce n'est pas le cas, vous pouvez l'installer avec la commande suivante :

```bash
sudo apt install gnupg
```

Pour **macOS**, si vous n'avez pas déjà installé le gestionnaire de paquets Homebrew, faites-le avec les commandes suivantes :

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Puis installez GPG avec cette commande :

```bash
brew install gnupg
```

Pour **Windows**, si vous n'avez pas GPG, vous pouvez installer le logiciel [Gpg4win](https://www.gpg4win.org/).

![GnuPG](assets/notext/01.webp)

## Téléchargement des documents

Pour commencer, nous allons avoir besoin de différents documents. Rendez-vous sur le site officiel de [Sparrow Wallet dans la section "*Download*"](https://sparrowwallet.com/download/). Si vous souhaitez vérifier un autre logiciel, rendez-vous sur le site de ce logiciel.

![GnuPG](assets/notext/02.webp)

Vous pouvez également aller [sur le dépôt GitHub du projet](https://github.com/sparrowwallet/sparrow/releases).

![GnuPG](assets/notext/03.webp)

Téléchargez l'installateur du logiciel correspondant à votre système d'exploitation.

![GnuPG](assets/notext/04.webp)

Vous allez également avoir besoin du hash du fichier, souvent appelé "*SHA256SUMS*" ou "*MANIFEST*".

![GnuPG](assets/notext/05.webp)

Téléchargez aussi la signature PGP du fichier. C'est le document en `.asc`.

![GnuPG](assets/notext/06.webp)

Assurez-vous de placer tous ces fichiers dans un même dossier pour les étapes suivantes.

Enfin, vous allez avoir besoin de la clé publique du développeur, que l'on va utiliser pour vérifier la signature PGP. Cette clé est souvent disponible soit sur le site web du logiciel, soit sur le dépôt GitHub du projet, parfois sur les réseaux sociaux du développeur, ou encore sur des sites spécialisés comme Keybase. Dans le cas de Sparrow Wallet, vous pouvez retrouver la clé publique du développeur [Craig Raw sur Keybase](https://keybase.io/craigraw). Pour la télécharger directement depuis le terminal, exécutez la commande :

```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```

![GnuPG](assets/notext/07.webp)

## Vérification de la signature

Le processus de vérification de la signature est le même sur **Windows**, **macOS** et **Linux**. Normalement, vous avez déjà importé la clé publique durant l'étape précédente, mais si ce n'est pas le cas, faites-le avec la commande :

```bash
gpg --import [key path]
```

Remplacez `[key path]` par l'emplacement du fichier de la clé publique du développeur.

![GnuPG](assets/notext/08.webp)

Vérifiez la signature avec la commande suivante :

```bash
gpg --verify [file.asc]
```

Remplacez `[file.asc]` par le chemin du fichier de la signature. Dans le cas de Sparrow, ce fichier s'appelle "*sparrow-2.0.0-manifest.txt.asc*" pour la version 2.0.0.

![GnuPG](assets/notext/09.webp)

Si la signature est valide, GPG va vous l'indiquer. Vous pouvez donc passer à l'étape suivante, car cela confirme l'authenticité du fichier.

![GnuPG](assets/notext/10.webp)

## Vérification du hash

Maintenant que l'authenticité du logiciel est confirmée, il faut vérifier également son intégrité. Nous allons comparer le hachage du logiciel avec le hachage fourni par le développeur. Si les deux correspondent, cela garantit que le code du logiciel n'a pas été altéré.

Sur **Windows**, ouvrez un terminal et exécutez la commande suivante :

```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```

Remplacez `[file path]` par l'emplacement de l'installateur.

![GnuPG](assets/notext/11.webp)

Le terminal vous renvoie le hachage du logiciel téléchargé.

![GnuPG](assets/notext/12.webp)

Attention, pour certains logiciels, il peut être nécessaire d'utiliser une fonction de hachage différente de SHA256. Dans ce cas, remplacez simplement le nom de la fonction de hachage dans la commande.

Comparez ensuite le résultat avec la valeur correspondante dans le fichier "*sparrow-2.0.0-manifest.txt*".

![GnuPG](assets/notext/13.webp)

Dans mon cas, on voit que les deux hachages correspondent parfaitement.

Sous **macOS** et **Linux**, le processus de vérification des hachages est automatisé. Il n'est pas nécessaire de vérifier manuellement la correspondance entre les deux hachages comme sur Windows.

Exécutez simplement cette commande sous **macOS** :

```bash
shasum --check [file name] --ignore-missing
```

Remplacez `[file name]` par le nom de l'installateur. Par exemple pour Sparrow Wallet :

```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```

Si les hachages correspondent, vous devriez avoir en sortie :

```bash
Sparrow-2.0.0.dmg: OK
```

Sous **Linux**, la commande est similaire :

```bash
sha256sum --check [file name] --ignore-missing
```

Et si les hachages correspondent, vous devriez avoir en sortie :

```bash
sparrow_2.0.0-1_amd64.deb: OK
```

Vous êtes maintenant assuré que le logiciel que vous avez téléchargé est à la fois authentique et intègre. Vous pouvez procéder à son installation sur votre machine.

Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !

Je vous conseille également de découvrir cet autre tutoriel sur VeraCrypt, un logiciel qui vous permet de chiffrer et de déchiffrer des supports de stockage.

https://planb.network/tutorials/others/general/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5

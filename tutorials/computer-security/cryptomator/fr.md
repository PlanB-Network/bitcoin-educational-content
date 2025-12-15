---
name: Cryptomator
description: Chiffrez vos fichiers dans le cloud
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Florian BURNEL publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont pu être apportées au texte original.*

___

## I. Présentation

Dans ce tutoriel, nous allons utiliser l'application Cryptomator pour chiffrer les données stockées dans le Cloud, que ce soit sur Microsoft OneDrive, Google Drive, Dropbox, Box ou encore iCloud. 

Chiffrer les données que l'on stocke sur les solutions de stockage en ligne de type Drive, c'est le meilleur moyen de protéger ses fichiers et de protéger sa vie privée. Grâce au chiffrement, vous êtes le seul à pouvoir déchiffrer et lire vos données même si elles sont stockées sur un serveur aux États-Unis ou dans un autre pays du monde.

Dans cette démonstration, une machine Windows 11 22H2 avec OneDrive sera utilisée, mais la procédure est identique sur les autres versions de Windows et les autres services de stockage. Ce dont vous avez besoin, c'est d'installer le client de synchronisation et d'ajouter votre compte. Ceci permettra à Cryptomator de stocker ses données dans le coffre.

![Image](assets/fr/020.webp)

Cryptomator est une alternative à d'autres applications, notamment Picocrypt présenté dans un autre article, qui se présente différemment, mais qui est également simple à utiliser. Cryptomator est également **open source**, conforme RGPD, et va permettre de **chiffrer les données avec l'algorithme de chiffrement AES-256 bits**. A contrario, Picocrypt s'appuie sur l'algorithme XChaCha20 (256 bits aussi) qui est plus rapide.

https://planb.academy/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

L'application Cryptomator est disponible sur **Windows** (exe / msi), **Linux**, **macOS,** mais aussi **Android** et **iOS**. D'ailleurs, toutes les applications sont gratuites, à part l'application Android que vous devez payer (14.99 euros).

Sur votre machine, **Cryptomator va créer un dossier au sein duquel il va créer un coffre-fort**. Au sein du coffre-fort, qui peut être stocké sur votre OneDrive, Google Drive, ou autre, vos données seront chiffrées. Ainsi, si vous stockez toutes vos données dans le coffre hébergé sur votre espace de stockage Drive, elles seront protégées (car chiffrées).

**Note** : dans cet article, les services de stockage en ligne sont pris comme exemple, mais Cryptomator peut être utilisé pour chiffrer les données sur un disque local, un disque externe ou encore sur un NAS. Il n'y a pas de restriction, en fait.

## II. Installer Cryptomator

Pour commencer, vous devez **télécharger** et **installer** **Cryptomator**. Une fois le téléchargement effectué, quelques clics suffisent pour effectuer l'installation. Comme [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), Cryptomator s'appuiera sur WinFsp pour **monter un lecteur virtuel sur votre machine Windows**.

* [Télécharger Cryptomator depuis le site officiel](https://cryptomator.org/downloads/)

![Image](assets/fr/025.webp)

## III. Utiliser Cryptomator sous Windows

### A. Créer un nouveau coffre

Afin de pouvoir créer un nouveau coffre, cliquez sur le bouton "**Ajouter**" et choisissez "**Nouveau coffre...**". Vos coffres existants et connus sur cette machine apparaîtront ensuite dans l'interface, sur la gauche. **Le coffre créé depuis une machine A peut être ouvert et modifié à partir d'une machine B**, à condition qu'elle soit équipée de Cryptomator (et de connaître la clé de chiffrement).

![Image](assets/fr/015.webp)

Commencez par donner un nom au coffre, par exemple "**IT-Connect**". Ceci aura pour effet de créer un répertoire nommé "**IT-Connect**" dans mon OneDrive.

![Image](assets/fr/011.webp)

À l'étape suivante, Cryptomator est susceptible de **détecter les "Drive"** présents sur votre machine : Google Drive, OneDrive, Dropbox, etc.... Pour vous permettre de sélectionner directement le fournisseur. J'ai fait l'essai sur deux machines Windows 11 différentes, avec plusieurs Drive, et ce n'était pas détecté. Ce n'est pas gênant, il suffit de définir un "**Emplacement personnalisé**" et de sélectionner la racine de son espace de stockage. Par exemple : **C:\Users\<Nom utilisateur>\OneDrive**.

![Image](assets/fr/018.webp)

Ensuite, vous avez la possibilité d'ajuster une option sous les paramètres experts.

![Image](assets/fr/021.webp)

Puis, vous devez définir **un mot de passe qui correspond à la clé de chiffrement**. C'est grâce à ce mot de passe que vous serez en mesure de **déverrouiller votre coffre Cryptomator** afin d'accéder à ses données. **Si vous le perdez, vous perdez accès à vos données**. Enfin, vous avez tout de même la possibilité de **créer une clé de secours** en cochant l'option "**Oui, mieux vaut prévenir que guérir**", un peu dans le même esprit que la clé de récupération [BitLocker](https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). C'est conseillé, mais ne stockez pas cette clé de secours à la racine de votre OneDrive !

Cliquez sur "**Créer un coffre**".

![Image](assets/fr/019.webp)

Copiez la clé de récupération afin de la stocker dans votre gestionnaire de mots de passe préféré. Cliquez sur "**Suivant**".

![Image](assets/fr/013.webp)

Voilà, votre nouveau coffre est créé et prêt à l'emploi !

![Image](assets/fr/014.webp)

### B. Accéder aux données chiffrées

Pour accéder à un coffre, ainsi qu'à ses données, soit pour **lire les données existantes ou ajouter de nouvelles données**, vous devez le **déverrouiller**. Cryptomator liste les coffres connus : le coffre IT-Connect apparaît, donc il suffit de le sélectionner et de cliquer sur "**Déverrouiller**".

![Image](assets/fr/016.webp)

Vous devez saisir votre mot de passe pour déverrouiller le coffre. Ensuite, cliquez sur "**Révéler le lecteur**".

![Image](assets/fr/022.webp)

**Votre coffre est monté sur la machine Windows en tant que lecteur virtuel.** Ce lecteur, qui hérite ici de la lettre E, vous permet d'accéder à vos données (en clair, car le coffre est déverrouillé).

![Image](assets/fr/017.webp)

Du côté de OneDrive, nous ne pouvons par parcourir directement le coffre de Cryptomator. Nous ne pouvons pas voir les données (pas plus le nom des fichiers que leur contenu). Ceci signifie que vous ne devez pas ajouter de données dans votre coffre Cryptomator via le raccourci OneDrive habituel. **Vous devez ajouter vos données en utilisant le lecteur virtuel de Cryptomator.**

![Image](assets/fr/012.webp)

### C. Options du coffre

Les paramètres du coffre sont accessibles via le bouton "**Options du volume chiffré**" (quand il est verrouillé) et vont permettre d'activer le verrouillage automatique en cas d'inactivité, comme on peut le faire avec son coffre-fort de mots de passe. L'option "**Déverrouiller le volume chiffré au démarrage**" permet, comme son nom l'indique, de déverrouiller le lecteur sans intervention de votre part et de monter le lecteur virtuel. Pour des raisons de sécurité, il vaut mieux éviter d'activer cette option.

Via l'onglet "**Montage**" vous pouvez aussi décider de le monter en lecture seule ou assigner une lettre spécifique.

![Image](assets/fr/024.webp)

Par ailleurs, dans les paramètres de Cryptomator en lui-même, vous pouvez **activer le démarrage automatique de l'application**.

## IV. Conclusion

Avec **Cryptomator**, vous pouvez **créer un coffre chiffré** en quelques minutes afin de protéger les données que vous souhaitez stocker sur OneDrive et consorts. Il est très facile à utiliser lorsqu'il s'agit de le "coupler" avec un Drive : pour cet usage, il a ma préférence en comparaison de Picocrypt.

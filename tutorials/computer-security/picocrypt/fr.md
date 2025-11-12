---
name: Picocrypt
description: Un outil open source pour chiffrer vos données
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Florian BURNEL publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont été apportées au contenu original.*

___

***Note importante :** Depuis le 8 août 2025, le dépôt GitHub de Picocrypt a été archivé, ce qui signifie que le logiciel ne bénéficie plus d’aucune maintenance. Picocrypt reste entièrement fonctionnel, stable et sécurisé en l’état. Toutefois, un successeur de Picocrypt, développé par la communauté, est disponible et s’appelle [Picocrypt NG](https://github.com/Picocrypt-NG/Picocrypt-NG).*

## I. Présentation

Dans ce tutoriel, nous allons découvrir Picocrypt, un logiciel de chiffrement simple, léger et efficace pour chiffrer des données avec un haut niveau de sécurité.

Adapté pour **chiffrer des fichiers**, vous pouvez l'utiliser pour protéger **les données présentes sur votre ordinateur, sur une clé USB**, mais également celles stockées dans le Cloud. Par exemple, vous pouvez chiffrer des données et les stocker sur **Microsoft OneDrive, Google Drive, iCloud ou encore Dropbox**, même si pour cet usage je lui préfère un autre logiciel qui sera présenté dans un prochain article.

Vous pouvez aussi l'utiliser lorsque vous avez besoin de **partager des données avec un tiers** : grâce à Picocrypt et la clé de déchiffrement, il pourra déchiffrer les données sur sa machine. Ainsi, en cas de compromission de votre compte ou de votre ordinateur, les données sont protégées.

Pour suivre le projet Picocrypt, il y a une seule et unique adresse :

* [Picocrypt sur GitHub](https://github.com/Picocrypt/Picocrypt)

Totalement **gratuit et open source**, PicoCrypt est disponible pour **Windows,** **Linux** et **macOS**. Sur Windows, vous pouvez l'installer sur votre machine ou utiliser la version portable.

## II. Picocrypt, un logiciel de chiffrement open source

Le **logiciel de chiffrement Picocrypt** se présente comme **une alternative** à d'autres solutions connues comme **VeraCrypt** et **Cryptomator** (*conçu pour chiffrer les données sur les environnements Cloud*), ou encore **AxCrypt**. D'ailleurs, sur le GitHub officiel de Picocrypt, vous pouvez trouver un comparatif avec certains concurrents :

|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Source : [Github.com](https://github.com/Picocrypt/Picocrypt)

Picocrypt est **très léger** puisqu'il pèse seulement **3 Mo** et il n'a pas besoin d'être installé : c'est une **application portable** qui présente l'avantage de ne pas demander les droits administrateur ! Pour autant, il ne néglige pas la sécurité puisqu'il s'appuie sur des **algorithmes robustes et fiables** :

**Algorithme de chiffrement XChaCha20**
**Fonction de dérivation de clé** Argon2

Au-delà des avantages qui viennent d'être cités, ce qui plait énormément, c'est **sa facilité d'utilisation** !

Il ne lui manque qu'une chose : **un audit du code**, mais c'est planifié comme le montre le tableau comparatif ci-dessus (dernière ligne). Mais bon, comme il est open source, rien ne vous empêche de jeter un coup d'œil à son code source.

Même s'il est comparé à BitLocker dans le tableau ci-dessus, **à mon sens BitLocker et Picocrypt sont destinés à des usages différents** : BitLocker pour chiffrer un volume complet (celui de Windows, par exemple) et Picocrypt pour chiffrer une arborescence ou un espace de stockage type "Drive".

## III. Utilisation de Picocrypt

Pour cette démonstration, une machine sous Windows 11 sera utilisée.

### A. Chiffrer des données avec Picocrypt

Tout d'abord, vous devez télécharger Picocrypt.exe sur le GitHub officiel ([voir cette page](https://github.com/Picocrypt/Picocrypt/releases)).

Ouvrez l'application afin d'afficher son interface minimaliste à l'écran. Pour chiffrer des données, que ce soit **un fichier, plusieurs fichiers ou un dossier**, effectuez simplement **un glisser-déposer vers l'interface de Picocrypt**. Ceci aura pour effet de sélectionner les données à chiffrer.

![Image](assets/fr/020.webp)

Ensuite, pour le chiffrement des données, vous avez accès à plusieurs options, notamment pour la clé de chiffrement. Il peut s'agir d'**un mot de passe robuste** ou d'**une clé de chiffrement qui prend la forme d'un fichier de clé**, ou **les deux**. Si l'on prend l'exemple d'un mot de passe, vous avez le choix entre, créer votre propre mot de passe, ou générer un mot de passe avec Picocrypt.

Ce mot de passe doit être robuste, car il permet de déchiffrer les données. Indiquez-le sous "**Password**" et "**Confirm Password**", puis cliquez sur "**Encrypt**" pour chiffrer les données ! Avant cela, vous pouvez cliquer sur le bouton "**Change**" à côté de "**Save output as**" pour spécifier le répertoire de sortie.

**Note** : pour utiliser une clé au format fichier, vous devez cliquer sur "**Create**" à droite de "**Keyfiles**" afin de créer une clé. Ensuite, elle doit être sélectionnée en cliquant sur "**Edit**" puis en faisant un glisser-déposer du fichier de clé sur la zone prévue à cet effet.

![Image](assets/fr/019.webp)

Les deux fichiers sélectionnés sont **chiffrés et regroupés** dans le fichier "**Encrypted.zip.pcv**" puisque **PCV** est l'extension utilisée par Picocrypt. Ce fichier ZIP est illisible grâce au chiffrement. Pour éviter que les fichiers sélectionnés soient regroupés dans un seul fichier ZIP chiffré, vous devez cocher l'option "**Recursively**" afin qu'il y ait autant de fichiers chiffrés que de fichiers à chiffrer.

Pour accéder à nos données, nous devons les déchiffrer à l'aide de Picocrypt.

![Image](assets/fr/023.webp)

Avant de parler du déchiffrement des données, voici des informations sur quelques-unes des options disponibles :

**Paranoid mode** ou **Mode paranoïaque** : utiliser le niveau de sécurité le plus élevé proposé par Picocrypt. L'outil va utiliser plusieurs algorithmes de chiffrement en cascade (XChaCha20 et Serpent) et HMAC-SHA3 à la place de BLAKE2b pour l'authentification des données.
* **Reed-Solomon** : implémenter des codes de correction d'erreur *Reed-Solomon* pour faciliter la correction d'erreurs sur des données corrompues. Ceci permet de supporter un niveau de corruption d'environ 3% de votre fichier.
**Split into chunks** ou **diviser en plusieurs parties** : si vous chiffrez un fichier volumineux, vous pouvez demander à Picocrypt de le découper en plusieurs parties. Ceci pourra faciliter le transfert du fichier.
* **Compress Files** ou **Compresser les fichiers** : compresser les fichiers pour réduire la taille des fichiers chiffrés.
* **Deleted files** ou **Fichiers supprimés** : supprimer les fichiers sources afin de garder uniquement la version chiffrée

### B. Déchiffrer des données avec Picocrypt

Si vous avez besoin de déchiffrer les données, ce n'est pas plus compliqué que pour les chiffrer. Il suffit d'ouvrir Picocrypt et de **glisser-déposer le fichier PCV à déchiffrer**. Ensuite, indiquez le mot de passe et/ou sélectionnez le fichier de clé avant de cliquer sur "**Decrypt**".

![Image](assets/fr/021.webp)

Voilà, l'archive ZIP "Encrypted.zip" dans sa version non chiffrée me permet de récupérer mes deux fichiers en clair !

![Image](assets/fr/022.webp)

## IV. Conclusion

**Vous étiez prévenu : Picocrypt est très simple à utiliser et il est efficace ! Bien que l'interface soit minimaliste, elle intègre des options très utiles pour personnaliser le chiffrement ! Puisqu'il est disponible en version portable, vous pouvez l'emporter avec vous partout afin de pouvoir déchiffrer vos données à coup sûr.**

Veillez à utiliser des mots de passe robuste pour protéger les données, et si vous utilisez un fichier de clé vous devez penser à le sauvegarder sous peine de ne plus pouvoir déchiffrer le conteneur PCV généré par Picocrypt. Enfin, sachez qu'il existe aussi [une version CLI](https://github.com/Picocrypt/CLI) (avec moins de fonctionnalités) qui permet d'exploiter Picocrypt en ligne de commande : là encore, Picocrypt ouvre la porte à de nouvelles possibilités.

https://planb.academy/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5
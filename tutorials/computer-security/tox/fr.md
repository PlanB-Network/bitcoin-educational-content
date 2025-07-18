---
name: Tox
description: Conversez sans intermédiaires sur le protocol decentralisé Tox
---
![cover](assets/cover.webp)

Le chiffrement de bout en bout est un service offert par de nombreuses applications de messagerie telles que WhatsApp et Telegram. Le chiffrement, ici, signifie qu'avant que le message ne soit envoyé par l'expéditeur, il est sécurisé par un verrou cryptographique dont seul le destinataire à la clé. Aujourd'hui nous partons à la découverte d'une application de messagerie totalement décentralisée et chiffrée de bout en bout, reposant sur des principes similaires à la blockchain, pour proposer une communication sécurisée, chiffrée de bout en bout sans intermédiaire : Tox Chat.

| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Chiffrement de bout en bout.*

## Qu'est-ce que Tox ?

Tox est un protocole de communication libre (open source) et décentralisé qui utilise la technologie *Networking and Cryptography Library* (NaCl) en plus des combinaisons d'algorithmes de chiffrement pour assurer la sécurité et la confidentialité de ses utilisateurs. Tox vous permet d'échanger des messages textuels, d'effectuer les appels audios et vidéos, de partager des fichiers et de partager votre écran avec vos amis de façon sécurisée, décentralisée et sans intermédiaire.

La technologie que le protocole Tox utilise est similaire aux réseau pair-à-pair comme les blockchains ce qui favorise la décentralisation de l'infrastructure du protocole. Contrairement aux réseaux sociaux et applications de messagerie cryptée de bout en bout, l'application Tox Chat est construite sur un protocole décentralisé qui n'a pas de serveur central. Tous les utilisateurs communiquent dans un réseau pair-à-pair sans intermédiaire et résistant à la censure. Pour communiquer, chaque utilisateur est identifié par un unique ID (ToxID) qui est dérivé de sa clé publique qui est stockée dans une table de Hash distribuée.

## Rejoindre Tox

Vous pouvez utiliser le protocole Tox au travers d'un client de messagerie instantané que vous pouvez télécharger sur le [site Tox Chat](https://tox.chat).

![download](assets/fr/01.webp)

Selon votre système d'exploitation, vous pouvez télécharger puis installer un client Tox qui correspond :

- aTox : [aTox](https://github.com/evilcorpltd/aTox), un client Tox écrit en Kotlin disponible uniquement sur Android

![aTox](assets/fr/02.webp)

- qTox : Un client Tox de [source libre](https://github.com/TokTok/qTox) basé sur le Framework Qt (C++) disponible sur Windows, Linux, MacOs.

![qTox](assets/fr/03.webp)

- Toxic : [Toxic](https://github.com/JFreegman/toxic) est un client Tox écrit en C fonctionnant sur les systèmes ayant les interfaces en lignes de commandes.

![Toxic](assets/fr/04.webp)

Dans ce tutoriel, nous utiliserons les clients qTox sur Windows et aTox pour communiquer.

## Débuter avec qTox

Une fois téléchargé, procédez à l'installation de votre client Tox puis créer votre profil.

![qTox-acount](assets/fr/05.webp)

Félicitations, vous venez de rejoindre le protocole Tox. Sur le logiciel qTox, vous pouvez retrouver les informations de votre profil en cliquant sur votre nom d'utilisateur.

![profil](assets/fr/06.webp)

Vous retrouverez notamment votre Tox ID que vous pouvez sauvegarder comme un QR code et partager avec des personnes qui veulent entrer en contact avec vous.

Exportez le fichier de votre profil Tox afin d'avoir une sauvegarde des informations de votre profil et de vos contacts que vous pourrez utiliser pour effectuer une restauration. Cliquez sur le bouton **Export** puis choisissez le chemin de votre fichier de sauvegarde.

![export](assets/fr/07.webp)

A partir du menu **Plus**, ajoutez des amis, importez des contacts puis gérez les demandes d'amis que vous recevez.

![friends](assets/fr/08.webp)

Vous pouvez me joindre via ce Tox ID par exemple : EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F

Une fois la demande d'amis envoyée, le destinataire devra accepter ou rejeter votre demande avant que vous ne puissiez communiquer avec lui.

![request](assets/fr/09.webp)

Vous retrouvez sur votre client Tox toutes les options que vous proposent les applications de messageries instantanées : 

- Les appels vidéo

- Les appels vocaux

- Le partage de fichiers 

- les emojis

![chat](assets/fr/10.webp)

### Des groupes pair à pair

Vos clients Tox vous permettent également de communiquer avec un groupe de personnes tout en étant totalement décentralisée : il s'agit des conférences. Dans le menu **Groupes**, créez une nouvelle conférence ou consultez la liste des invitations à rejoindre des conférences que vous avez reçu.

![conferences](assets/fr/11.webp)

Une fois la conférence créée, vous pouvez inviter vos amis à rejoindre la conférence sur votre client Tox. Dans la liste de vos amis, faites un clic droit sur le nom d'utilisateur de celui que vous souhaitez inviter. Cliquez sur l'option **Inviter à la conférence** puis sélectionnez le nom de la conférence que vous avez créé. Vous pouvez également inviter un ami en créant implicitement une conférence avec l'option **Créer une nouvelle conférence**.

⚠️ Les clients Tox sont en cours de développement, vous pourriez rencontrer des erreurs lors de certaines interactions avec le logiciel. Les fonctionnalités de conférences et d'appels vidéo ne sont pas encore disponible sur le client Tox Android (aTox).

![invite](assets/fr/12.webp)

### Transferts de fichiers 

Dans le menu **Transferts de fichiers**, vous retrouverez l'historique des fichiers que vous avez envoyés et ceux que vous avez reçus de vos contacts.

![files](assets/fr/13.webp)

Vous pouvez également personnaliser vos configurations de partages de fichiers pour chaque discussion que vous avez. Faites un clic droit sur le nom d'utilisateur de votre destinataire puis sélectionnez "Afficher plus de détails".

![details](assets/fr/14.webp)

Vous pouvez gérer à partir de l'interface des détails, les autorisations que vous accordez à votre destinataire en ce qui concerne les :

- Acceptations automatiques des invitations à des conférences.

- Acceptations automatiques des fichiers.

- Chemins de sauvegarde des fichiers de vos discussions.

![permissions](assets/fr/15.webp)

### Plus de paramètres

Dans le menu **Paramètres**, vous pouvez personnaliser les configurations de votre client Tox.

- Dans la section **Générale**, modifiez la langue de base de votre client Tox, définissez les chemins de sauvegardes des fichiers et la taille maximale des fichiers à accepter automatiquement.

![general](assets/fr/16.webp)

- Dans la section **Interface utilisateur**, modifiez les polices d'écriture et les tailles de vos messages. Vous avez également la possibilité de modifier le thème de votre client Tox.

![ui](assets/fr/17.webp)

- L'onglet **Confidentialité** vous permet de définir les messages éphémères en décochant la case "Garder l'historique des discussions". Vous pouvez également modifier votre code Nospam lorsque vous remarquez que vous vous faites spammés par des demandes d'amis en cliquant sur le bouton "Générer un code NoSpam aléatoire".

![privacy](assets/fr/18.webp)

### Qu'est ce qui garantit la confidentialité sur Tox ?

Le protocole Tox utilise la table de Hash Distribuée (Distributed Hash Table) pour créer un réseau de nœuds décentralisés. Chaque client Tox fait partie du réseau DHT et stocke les informations sur d'autres nœuds. Dans le cas de Tox, la DHT stocke les adresses IP comme valeurs associées aux clés publiques Tox (Tox ID). Cela permet de facilement rechercher un appareil Tox Client sans avoir à requérir à un serveur central.

Imaginez vous écrire à notre utilisateur `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F` que nous nommerons **user B**. Votre client Tox se chargera de localiser cet identifiant dans la table de Hash Distribuée et de récupérer l'adresse IP associée. Une fois l'adresse IP trouvée, votre client Tox créera un canal de communication directe et chiffrée avec la machine de notre **user B** ou utilisera d'autres nœuds comme relais pour atteindre **User B**. Les algorithmes de chiffrement assurent indépendamment du canal de communication que seul le destinataire **User B** sera en mesure de lire le contenu de votre message.

Si vous avez aimé découvrir Tox et que vous avez pu comprendre en quoi il est utile pour renforcer votre confidentialité, n'hésitez pas à laisser un pouce à ce tutoriel. Nous vous recommandons notre tutoriel sur Simple Login, un outil qui vous permet de recevoir et d'envoyer des emails de façon anonyme.

https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41
---
name: Horodatage des certificats et diplômes du Plan ₿ Network
description: Comprendre comment Plan ₿ Network délivre une preuve vérifiable pour votre certificat et diplômes
---

![cover](assets/cover.webp)

Si vous lisez ceci, il y a une forte probabilité pour que vous receviez soit un Certificat Bitcoin, soit un diplôme de fin de cours de l'un des cours que vous avez suivi sur Plan ₿ Network, alors félicitations pour cette réalisation !

Dans ce tutoriel, nous allons voir comment Plan ₿ Network délivre une preuve vérifiable pour votre Certificat Bitcoin ou tout Diplôme de Fin de Cours. Puis, dans une seconde partie, nous verrons comment vérifier l'authenticité de ces preuves.

# Mécanisme de preuve par Plan ₿ Network

Chez Plan ₿ Network, nous vous offrons un certificat et des diplômes qui sont cryptographiquement signés par nous, et horodatés sur la Timechain (c'est-à-dire, la blockchain Bitcoin). Pour atteindre cet objectif, nous avons dû concevoir un mécanisme de preuve qui repose sur 2 opérations cryptographiques :

1. Une signature GPG sur un fichier texte qui synthétise vos réalisations
2. L'horodatage de ce fichier signé via [opentimestamps](https://opentimestamps.org/).

Fondamentalement, la première opération vous permet de vérifier qui a émis le certificat (ou diplôme) tandis que la seconde vous permet de vérifier quand il a été émis.
Nous croyons que ce mécanisme de preuve simple nous permet de délivrer des certificats et diplômes avec des preuves indéniables que n'importe qui peut vérifier par lui-même.

![image](./assets/proof-mechanism.webp)

Notez que grâce à ce mécanisme de preuve, toute tentative de modifier même le moindre détail de votre certificat ou diplôme créera un hash sha256 complètement différent du fichier signé, ce qui révélerait instantanément une falsification car la signature et l'horodatage ne seraient plus valides. De plus, si quelqu'un tente de forger malicieusement des certificats ou diplômes au nom de Plan ₿ Network, une simple vérification de la signature révélerait la fraude.

## Comment fonctionne la signature GPG ?

La signature GPG est obtenue avec l'utilisation d'un logiciel open-source nommé GNU Private Guard. Ce logiciel permet à quiconque de créer facilement des clés privées, de signer et vérifier des signatures et également de chiffrer et déchiffrer des fichiers. Pour ce tutoriel, sachez que le Plan ₿ Network utilise GPG pour créer sa clé privée/publique et pour signer tout Certificat Bitcoin ou Diplôme de Fin de Cours.

D'autre part, si quelqu'un souhaite vérifier l'authenticité d'un fichier signé, il peut utiliser GPG pour importer la clé publique de l'émetteur et vérifier. Dans la seconde partie du tutoriel, nous verrons comment faire cela avec un terminal.

Pour ceux qui sont curieux et souhaitent en savoir plus sur ce fantastique logiciel, vous pouvez vous référer à ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## Comment fonctionne l'horodatage ?

N'importe qui peut utiliser OpenTimestamps pour horodater un fichier, et obtenir une preuve vérifiable de l'existence du fichier. En d'autres termes, cela ne vous fournit pas une preuve de quand le fichier a été créé mais une preuve d'existence au plus tard à un certain moment.
OpenTimestamps est capable d'offrir ce service gratuitement grâce à une manière très efficace de stocker une telle preuve dans la Blockchain Bitcoin. Il utilise le hash sha256 du fichier comme identifiant unique de votre fichier et construit un arbre de Merkle avec d'autres hashes de fichiers soumis par d'autres utilisateurs et ancre seulement le hash de la structure de l'arbre de Merkle dans une Transaction OpReturn.
Une fois cette transaction incluse dans un bloc, quiconque possédant le fichier initial et le fichier `.ots` qui lui est associé peut vérifier l'authenticité de l'horodatage. Dans la seconde partie du tutoriel, nous verrons comment vérifier votre Certificat Bitcoin ou tout Diplôme de Fin de Cours avec un terminal et avec une interface graphique via le site web d'OpenTimestamps.

# Comment vérifier un Certificat ou un Diplôme de Plan ₿ Network

## Étape 1. Téléchargez votre Certificat ou Diplôme

Connectez-vous à votre tableau de bord sur la plateform ₿ Network.

![image](./assets/login.webp)

Accédez à la page des Credentials en cliquant sur le menu latéral gauche, et sélectionnez votre session d'examen ou votre Diplôme de Fin de Cours.

![image](./assets/credential.webp)

Téléchargez le fichier zip.

![image](./assets/download.webp)

Extrayez le contenu en cliquant droit sur le fichier `.zip` et en sélectionnant "Extraire". Vous trouverez trois fichiers différents à l'intérieur :

- Fichier texte signé (par exemple, certificate.txt)
- Fichier Open timestamp (OTS) (par exemple, certificate.txt.ots)
- Certificat PDF (par exemple, certificate.pdf)

## Étape 2 : Vérification de la Signature du Fichier Texte

Ouvrez d'abord un terminal dans le dossier où se trouvent les fichiers (en cliquant droit sur la fenêtre du dossier et cliquez sur "Ouvrir dans le Terminal"). Puis suivez les instructions ci-dessous

1. Importez la clé publique PGP de Plan ₿ Network avec la commande suivante :

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

Vous devriez voir un message comme le suivant si vous avez importé la clé PGP avec succès

```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

NOTE : si vous voyez qu'une clé est traitée et 0 importée, il est probable que vous avez déjà importé la même clé précédemment et c'est bon.

2. Vérifiez la signature du certificat ou du diplôme avec la commande suivante :

```bash
gpg --verify certificate.txt
```

Cette commande devrait vous montrer des détails sur la signature, incluant :

- Qui l'a signée (Plan ₿ Network)
- Quand elle a été signée
- Si la signature est valide

Voici un exemple du résultat :

```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```

Si vous voyez un message comme "BAD signature", cela signifie que le fichier a été altéré.

## Étape 3 : Vérification de l'Open Timestamp

### Vérification via une Interface Graphique

1. Visitez le site web d'OpenTimestamps : https://opentimestamps.org/
2. Cliquez sur l'onglet "Stamp & Verify".
3. Glissez et déposez le fichier OTS (par exemple, `certificate.txt.ots`) dans la zone désignée.
4. Glissez et déposez le fichier horodaté (par exemple, `certificate.txt`) dans la zone désignée.
5. Le site web vérifiera automatiquement l'open timestamp et affichera le résultat.

Si vous voyez un message comme le suivant, votre horodatage est valide :
![couverture](assets/opentimestamp_wegui_verified.webp)

### Méthode CLI

NOTE : cette procédure **nécessitera l'exécution d'un nœud Bitcoin local**

1. Installez le client OpenTimestamps depuis le dépôt officiel : https://github.com/opentimestamps/opentimestamps-client en exécutant la commande suivante :

```
pip install opentimestamps-client
```

2. Naviguez jusqu'au répertoire contenant les fichiers de certificat extraits.

3. Exécutez la commande suivante pour vérifier le timestamp ouvert :

```
ots verify certificate.txt.ots
```

Cette commande va :

- Vérifier le timestamp contre la blockchain de Bitcoin
- Vous montrer quand exactement le fichier a été timestampé
- Confirmer l'authenticité du timestamp

### Résultats finaux

Notez que la vérification est réussie si **les deux** messages suivants sont affichés :

1. La signature GPG est signalée comme **"Bonne signature de Plan ₿ Network"**
2. La vérification OpenTimestamps montre un timestamp spécifique de bloc Bitcoin et rapporte **"Succès ! Le bloc Bitcoin [hauteur du bloc] atteste que les données existaient en date du [timestamp]"**

Maintenant que vous savez comment Plan ₿ Network émet une preuve vérifiable pour tout Certificat Bitcoin et Diplôme de Fin de Cours, vous pouvez facilement vérifier l'intégrité de celui-ci.

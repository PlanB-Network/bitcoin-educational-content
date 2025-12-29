---
name: Horodatage des diplômes de Plan ₿ Academy
description: Comprendre comment Plan ₿ Academy émet une preuve vérifiable pour vos certificats et diplômes
---

![cover](assets/cover.webp)

Si vous lisez ceci, il y a de fortes chances pour que vous receviez soit un certificat de test ₿-CERT, soit un diplôme final de l'un des cours que vous avez suivis sur Plan ₿ Academy, alors félicitations pour cette accomplissement !

Dans ce tutoriel, nous allons voir comment Plan ₿ Academy émet des preuves vérifiables pour votre certificat de test ₿-CERT ou tout diplôme de fin de cours. Dans une seconde partie, nous verrons comment vérifier l'authenticité de ces preuves.


# Mécanisme de preuve de Plan ₿ Academy


Chez Plan ₿ Academy, nous vous délivrons des certificats et des diplômes que nous signons cryptographiquement et horodatons sur la Timechain (c'est-à-dire, la blockchain Bitcoin). Pour atteindre cet objectif, nous avons dû concevoir un mécanisme de preuve qui repose sur 2 opérations cryptographiques :

1. Une signature GPG sur un fichier texte qui synthétise vos réalisations ;
2. L'horodatage de ce fichier signé via [opentimestamps](https://opentimestamps.org/).

La première opération vous permet de vérifier l'émetteur du certificat (ou diplôme), tandis que la seconde vous permet de vérifier sa date d'émission.
Nous pensons que ce mécanisme de preuve simple nous permet de délivrer des certificats et diplômes avec des preuves indéniables que n'importe qui peut vérifier par lui-même.

![image](./assets/proof-mechanism.webp)

Grâce à ce mécanisme de preuve, toute tentative de modification, même du moindre détail, de votre certificat ou diplôme créera un hachage SHA-256 complètement différent du fichier signé, ce qui révélerait instantanément une falsification car la signature et l'horodatage ne seraient plus valides. De plus, si quelqu'un tente de falsifier malicieusement des certificats ou diplômes au nom de Plan ₿ Academy, une simple vérification de la signature révélerait la fraude.

## Comment fonctionne la signature GPG ?

La signature GPG est obtenue avec l'utilisation d'un logiciel open source nommé GNU Private Guard. Ce logiciel permet à quiconque de créer facilement des clés privées, de signer et vérifier des signatures, ainsi que de chiffrer et déchiffrer des fichiers. Pour ce tutoriel, sachez que Plan ₿ Academy utilise GPG pour créer ses clés privées/publiques et pour signer tout certificat de test ₿-CERT ou diplôme de fin de cours.

D'autre part, si quelqu'un souhaite vérifier l'authenticité d'un fichier signé, il peut utiliser GPG pour importer la clé publique de l'émetteur et la vérifier. Dans la seconde partie du tutoriel, nous verrons comment faire cela avec un terminal.

Pour ceux qui sont curieux et souhaitent en savoir plus sur ce fantastique logiciel, vous pouvez vous référer à ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html).

## Comment fonctionne l'horodatage ?

N'importe qui peut utiliser OpenTimestamps pour horodater un fichier et obtenir une preuve vérifiable de son existence. En d'autres termes, cela ne vous fournit pas une preuve de quand le fichier a été créé, mais seulement qu'il existait au plus tard à un moment donné.

OpenTimestamps fournit ce service gratuitement grâce à une méthode très efficace pour stocker une telle preuve dans la blockchain Bitcoin. Il utilise le hachage SHA-256 du fichier comme identifiant unique de celui-ci et construit un arbre de Merkle avec d'autres hachages de fichiers soumis par d'autres utilisateurs. Seul le hachage de la structure de l'arbre de Merkle est ancré dans une transaction OpReturn.

Une fois cette transaction incluse dans un bloc, quiconque possédant le fichier initial et le fichier `.ots` qui lui est associé peut vérifier l'authenticité de l'horodatage. Dans la seconde partie de ce tutoriel, nous verrons comment vérifier votre certificat de test ₿-CERT ou tout diplôme de fin de cours avec un terminal et avec une interface graphique via le site web d'OpenTimestamps.

## Étape 1 : Téléchargez votre certificat ou diplôme

Connectez-vous à votre tableau de bord sur [Plan ₿ Acadmy](https://planb.academy/fr/certifications/certificates).

![image](./assets/login.webp)

Accédez à la page des "Certifications" en cliquant sur le menu latéral gauche, et sélectionnez votre certificat ou votre diplôme.

![image](./assets/credential.webp)

Téléchargez le fichier zip.

![image](./assets/download.webp)

Extrayez le contenu en cliquant droit sur le fichier `.zip` et en sélectionnant "Extraire". Vous trouverez trois fichiers différents à l'intérieur :

- Un fichier texte signé (par exemple, certificate.txt) ;
- Un fichier OpenTimestamps (OTS) (par exemple, certificate.txt.ots) ;
- Un certificat en PDF (par exemple, certificate.pdf).

## Étape 2 : Vérification de la signature du fichier texte

Ouvrez d'abord un terminal dans le dossier où se trouvent les fichiers en cliquant droit sur la fenêtre du dossier et cliquez sur "Ouvrir dans le Terminal". Puis suivez les instructions ci-dessous :

1. Importez la clé publique PGP de Plan ₿ Academy avec la commande suivante :

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/Plan ₿ Academy-pk.asc | gpg --import
```

Vous devriez voir un message comme le suivant si vous avez importé la clé PGP avec succès.

```
gpg: key 8F12D0C63B1A606E: public key "Plan ₿ Academy (used for Plan ₿ Academy platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

**NOTE** : Si vous voyez qu'une clé a été traitée mais que 0 clés ont été importées, il est probable que vous avez déjà importé cette même clé précédemment, ce qui est tout à fait normal.

2. Vérifiez la signature du certificat ou du diplôme avec la commande suivante :

```bash
gpg --verify certificate.txt
```

Cette commande devrait vous afficher des détails sur la signature, incluant :

- Qui l'a signée (Plan ₿ Academy) ;
- Quand elle a été signée ;
- Si la signature est valide.

Voici un exemple du résultat :

```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "Plan ₿ Academy (used for Plan ₿ Academy platform) <admin@planb.network>" [unknown]
```

Si vous voyez un message comme "BAD signature", cela signifie que le fichier a été altéré.

## Étape 3 : Vérification de l'Open Timestamp

### Vérification via une interface graphique

1. Visitez le site web d'OpenTimestamps : https://opentimestamps.org/.
2. Cliquez sur l'onglet "Stamp & Verify".
3. Glissez et déposez le fichier OTS (par exemple, `certificate.txt.ots`) dans la zone désignée.
4. Glissez et déposez le fichier horodaté (par exemple, `certificate.txt`) dans la zone désignée.
5. Le site web vérifiera automatiquement l'open timestamp et affichera le résultat.

Si vous voyez un message comme le suivant, votre horodatage est valide : 

![couverture](assets/opentimestamp_wegui_verified.webp)

### Méthode CLI

**NOTE : cette procédure nécessite l'exécution d'un nœud Bitcoin local**

1. Installez le client OpenTimestamps depuis [le dépôt officiel](https://github.com/opentimestamps/opentimestamps-client) en exécutant la commande suivante :

```
pip install opentimestamps-client
```

2. Naviguez jusqu'au répertoire contenant les fichiers de certificat extraits.

3. Exécutez la commande suivante pour vérifier l'OpenTimestamps :

```
ots verify certificate.txt.ots
```

Cette commande va :

- Vérifier l'horodatage par rapport à la blockchain de Bitcoin ;
- Vous montrer quand le fichier a exactement été horodaté ;
- Confirmer l'authenticité de l'horodatage.

### Résultats finaux

La vérification est considérée comme réussie si **les deux** messages suivants sont affichés :

1. La signature GPG est signalée comme **"Bonne signature de Plan ₿ Academy"**
2. La vérification OpenTimestamps montre un horodatage précis dans un bloc Bitcoin et indique **"Succès ! Le bloc Bitcoin [hauteur du bloc] atteste que les données existaient en date du [horodatage]"**

Maintenant que vous savez comment Plan ₿ Academy émet une preuve vérifiable pour tout certificat ₿-CERT et diplôme de fin de cours, vous pouvez facilement en vérifier l'intégrité.

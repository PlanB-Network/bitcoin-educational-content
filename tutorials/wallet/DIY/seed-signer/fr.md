---
name: Ledger Nano S

builder: ledger

tag:
  - wallet
---

# seed signer

materiel:

1. Raspberry Pi Zéro (version 1.3)

Raspberry Pi Zéro

Pour une solution complètement isolée, assurez-vous d'utiliser la version 1.3 sans capacité WiFi ou Bluetooth, mais n'importe quel modèle Raspberry Pi 2/3/4 ou Zero fonctionnera.

Remarque : Raspberry Pi que ceux-ci ne sont généralement pas livrés avec des broches attachées ; les broches devront soit être soudées, soit quelque chose appelé "GPIO Hammer" peut être utilisé.
Marteau GPIO

Si votre soudure n'est pas tout à fait à la hauteur, ou si vous ne possédez pas encore de fer à souder, vous pouvez utiliser "GPIO Hammer" comme alternative à la soudure.

2. Chapeau LCD WaveShare 1,3 pouces avec écran 240 × 240 pixels

Chapeau LCD WaveShare

Écran LCD Waveshare 1,3″ 240 × 240 pixels

Remarque : Choisissez l'écran Waveshare avec soin ; assurez-vous d'acheter le modèle qui a une résolution de 240 × 240 pixels.

3. Module de caméra compatible Pi Zero

Caméra Raspberry Pi

Aokin / AuviPal 5MP 1080p avec module de caméra vidéo à capteur OV5647 ; d'autres marques avec le module de capteur OV5647 devraient également fonctionner, mais peuvent ne pas être compatibles avec le boîtier Orange Pill.

Remarque : Vous aurez besoin d'un câble ruban de caméra spécifiquement compatible avec Raspberry Pi Zero.

4. Carte MicroSD avec au moins 4 Go de capacité

extensive ressources : https://seedsigner.com/explainers/

## Software:

Installation du logiciel

1. Téléchargez le dernier fichier "seedsigner_x_x_x.img.zip"
   dernière version

2. Décompressez le fichier "seedsigner_x_x_x.img.zip"

3. Utilisez Balena Etcher ou un outil similaire pour écrire le fichier image .img décompressé sur une carte microsd
   GRAVEUR DE BALENA

4. Installez la carte microsd dans SeedSigner.
   Clé publique SeedSigner GPG
   seedsigner_pubkey.gpg

## tutoriel video

tuto seed signer: https://www.youtube.com/watch?v=XLrXLVCdDbs

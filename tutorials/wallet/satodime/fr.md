---
name: Satodime
description: Découvrez comment utiliser le Satodime avec l'application mobile
---
![cover](assets/cover.webp)

Ce guide vous accompagne dans l’installation, la configuration et l’utilisation de l’application mobile Satodime. Vous apprendrez à prendre possession de votre carte, créer des coffres-forts, ajouter des fonds, desceller et récupérer vos clés privées. Des annexes fournissent des ressources, bonnes pratiques et explications techniques.

## Introduction

**Satodime**, développé par **[Satochip](https://satochip.io/fr/)**, est une carte au porteur sécurisée pour stocker du Bitcoin de manière tangible et simple. Elle agit comme un hardware wallet self-custodial, où vous contrôlez entièrement vos clés privées sans dépendre d’un tiers. Open-source et certifiée EAL6+, elle supporte jusqu’à trois coffres-forts indépendants.

### Contexte du produit

Satodime, une **carte au porteur, appartient à celui qui la possède physiquement**, sans besoin d'enregistrement ou d'identification préalable. Elle répond au besoin de stockage sécurisé et portable des bitcoins, permettant à quiconque détient la carte de l'utiliser ou de transférer ses bitcoins en la scannant via l'application mobile pour en prendre possession ou desceller les coffres-forts. Contrairement à un billet papier, elle utilise une puce sécurisée pour sceller les clés privées, qui ne sont révélées qu’après descellement, rendant la carte similaire à de l'argent liquide où la propriété est déterminée par la possession physique. Idéale pour offrir des bitcoins en cadeau, elle facilite le transfert des bitcoins de main en main en toute sécurité, tandis que l’application mobile exploite la NFC pour une interaction accessible sur smartphone.

- **Sécurité** : Clés privées générées et stockées dans la puce inviolable ; état visible (scellé, descellé, vide).
- **Fonctionnalités** : Achetez des bitcoins directement via l’app (partenaire Paybis) ; gérez Mainnet et Testnet.
- **Open-source** : Code sous licence AGPLv3, vérifiable sur GitHub.

### Évolution continue

L’application évolue régulièrement. Vérifiez les mises à jour sur le site Satochip ou les stores. Par exemple, de nouvelles blockchains ou fonctionnalités d’achat pourraient être ajoutées. Consultez le [GitHub de Satochip](https://github.com/Toporin/Satodime-Applet) pour les développements en cours.

## 1. Prérequis

Avant de commencer avec **Satodime**, assurez-vous de disposer des éléments suivants :

* **Smartphone compatible** : Un appareil Android ou iOS avec NFC activé.
* **Carte Satodime** : Neuve ou non initialisée.
* **Connexion internet** : Pour télécharger l’app.
* **Connaissances de base** : Comprendre les clés privées/publiques et les risques de perte (irréversible).
* **Support sécurisé** : Un endroit sûr pour noter les clés privées une fois descellées (papier, métal ; jamais numérique).

## 2. Installation

- **Téléchargez l’application** :
	- **[App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
	- **[Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
	- Vérifiez le développeur (Satochip) pour éviter les fraudes.
	- Satodime est **open-source**. Code source : [GitHub de Satochip](https://github.com/Toporin/Satodime-Applet).

- **Installez et lancez l’application** : Activez le NFC sur votre téléphone si nécessaire.

![image](assets/fr/01.webp)

## 3. Configuration initiale

### 3.1 Lancer l’application et scanner

Ouvrez l’app et suivez l’assistant. Apposez la carte Satodime sur le lecteur NFC de votre téléphone (généralement au dos). Maintenez-la pendant toute l’opération pour une connexion stable.

- Si le NFC ne fonctionne pas, vérifiez les paramètres de votre téléphone.
- Un toast confirme la réussite : "Lecture réussie".

![image](assets/fr/02.webp)

De façon générale, **toutes les opérations suivantes demanderont une confirmation via le scan de la carte Satodime.**

### 3.2 Prendre possession de la carte (*Ownership*)

Pour la première utilisation, devenez propriétaire de la carte pour la sécuriser :

- Cliquez sur "*Take Ownership*" dans l’app.
- Confirmez l’opération : cela génère une clé de propriétaire unique.
- Scannez à nouveau la carte pour appliquer les changements.
- **Avertissement** : Cette étape est irréversible. Référez-vous à [l’article sur l’*ownership*](https://satochip.io/satodime-ownership-explained/).

![image](assets/fr/03.webp)


## 4. Créer un coffre-fort

Satodime supporte jusqu’à 3 coffres-forts. Créez-en un pour stocker du bitcoin :

- Sélectionnez un coffre vide (ex. : Coffre 01).
- Choisissez la blockchain (Bitcoin).
- Cliquez sur "*Créer & Sceller*".
- Scannez la carte pour générer et sceller la clé privée (inconnue jusqu’au descellement).
- **Félicitations** : Votre coffre-fort est désormais scellé et prêt à recevoir des fonds.

![image](assets/fr/04.webp)

![image](assets/fr/05.webp)

## 5. Ajouter des fonds

Une fois scellé, chargez le coffre-fort avec des bitcoins :

- Sélectionnez le coffre-fort.
- Cliquez sur "*Ajouter des fonds*".
- Copiez l’adresse publique ou scannez le QR code.
- Envoyez des fonds depuis un autre wallet.
- Vérifiez le solde après confirmation sur la blockchain.
- Option d’achat : Cliquez sur "*Acheter*" pour acheter directement via Paybis (Visa, Mastercard, etc.). Frais applicables.

![image](assets/fr/06.webp)

## 6. Descellez un coffre-fort

Pour accéder à la clé privée et transférer les fonds ailleurs, descellez le coffre-fort :

- Sélectionnez le coffre-fort scellé.
- Cliquez sur "Desceller".
- Confirmez l’avertissement : cette opération est irréversible.
- Scannez la carte pour desceller.
- Le coffre-fort passe en état "*Unsealed*" ; la clé privée est maintenant affichable / exportable.
- **Avertissement** : Une fois descellée, la clé privée est accessible. Si quelqu'un prend possession de votre smartphone, il peut avoir accès à cette clef, et donc récupérer les fonds présents sur votre coffre (irréversible).

![image](assets/fr/07.webp)

## 7. Récupérer la clé privée

Après descellement, exportez la clé pour l’utiliser dans un autre wallet :

- Assurez-vous d'être dans un environnement sécurisé.
- Cliquez sur "*Afficher la clef privée*".
- Choisissez le format : Legacy, SegWit, WIF, etc.
- Copiez la clef ou scannez le QR code.
- **Sécurité** : Ne partagez jamais la clé privée. Stockez-la hors ligne.
- Importez-la dans un logiciel/wallet compatible pour gérer les fonds (Sparrow Wallet ou Electrum par exemple).
 
![image](assets/fr/08.webp)



## 8. Réinitialiser le coffre

La réinitialisation du coffre supprime irréversiblement la clef privée associée. Autrement dit, si vous n'avez pas sécurisé une copie de votre clef privée, ou si vous ne l'avez pas importée dans un autre wallet, la réinitialisation du coffre provoquera la perte irréversible des fonds qui s'y trouvent.

![image](assets/fr/09.webp)

La réinitialisation du coffre rend le slot vide et prêt pour un nouveau coffre.

## 9. Transférer la propriété

Pour, par exemple, offrir des bitcoins grâce à Satodime, vous devez : 
- Prendre la propriété de la carte,
- Créer un coffre Bitcoin,
- Y transférer des sats,
- Transférer la propriété de la carte : le prochain à scanner la carte deviendra propriétaire,
- Donner la carte Satodime à la personne de votre choix, et l'inviter à télécharger l'application puis à scanner la carte pour en prendre la propriété, et donc accéder aux bitcoins qui y sont 'stockés'.

![image](assets/fr/10.webp)


## ANNEXES

### A1. Bonnes pratiques

Pour utiliser **Satodime** de manière sécurisée :

* **Sécurisez la carte** : Traitez-la comme de l’argent liquide ; perte = fonds perdus si non propriétaire.
* **Backup des clés** : Après descellement, notez les clés privées sur support physique sécurisé. Jamais numérique.
* **Vérifiez l’état** : Toujours scanner pour confirmer que vous avez bien la propriété de la carte, et l'état scellé/descellé des coffres.
* **Confidentialité** : Utilisez de nouvelles adresses ; évitez les échanges centralisés pour les transferts.
* **Mises à jour** : Gardez l’app à jour via les stores.
* **Récupération** : Si la carte est perdue mais propriétaire, les fonds sont sur la blockchain ; utilisez la clé privée si descellée.

### A2. Ressources supplémentaires

Spécifiques pour Satodime :
- [Produit Satodime](https://satochip.io/fr/product/satodime/)
- [Guide mobile](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)

[Plan ₿ Academy](https://planb.academy/) pour tutoriels sur la self-custody, les clés privées, etc.

**Sauvegarder sa phrase de récupération** :

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tutoriel sur le Satochip (premier produit de la marque) :**

https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Tutoriels sur le Seedkeeper :**

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. À propos de Satochip

**Liens officiels** :
- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Support : info@satochip.io

**Satochip** est une entreprise belge qui développe des solutions matérielles et logicielles pour la gestion et la conservation de bitcoins et d'autres cryptomonnaies. Son produit phare, le portefeuille matériel Satochip, est une carte NFC équipée d’un élément sécurisé certifié EAL6+. Complété par le Seedkeeper, un gestionnaire de phrases mnémoniques et de secrets, et le Satodime, une carte au porteur, Satochip offre une gamme complète adaptée aux besoins des utilisateurs. Ses appareils, alimentés par des logiciels open source, visent à démocratiser la sécurité sur Bitcoin.

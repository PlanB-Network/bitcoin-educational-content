---
term: BIP0093
definition: Standard Codex32 permettant de sauvegarder une graine en la divisant en plusieurs parts via le partage de secret de Shamir.
---

BIP informationnel qui suggère un standard pour sauvegarder et restaurer la graine d’un portefeuille déterministe hiérarchique (selon le BIP32) en utilisant le Partage de clé secrète de Shamir. Ce protocole définit le format « codex32 », qui s’inspire du format bech32, en introduisant une chaîne structurée composée d’un préfixe, d’un paramètre de seuil, d’un identifiant, d’un index de partage, d’une charge utile et d’une checksum (BCH). La méthode permet de scinder la graine en jusqu’à 31 parts, dont un seuil défini (entre 1 et 9) est requis pour la récupération complète de la graine.

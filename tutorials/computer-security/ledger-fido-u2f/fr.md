---
name: Ledger U2F & FIDO2
description: Renforcer sa sécurité en ligne avec Ledger
---
![cover](assets/cover.webp)

Les dispositifs Ledger sont des hardware wallets initialement conçu pour sécuriser un portefeuille Bitcoin, mais ils disposent également d'options avancées pour réaliser de l'authentification forte sur le web. Grâce à leur compatibilité avec les protocoles **U2F** et **FIDO2**, ils permettent de sécuriser l’accès à vos comptes en ligne en paramétrant un second facteur d'authentification.

Le protocole U2F (Universal 2nd Factor) a été introduit par Google et Yubico en 2014, puis standardisé par la FIDO Alliance. Il permet d’ajouter un second facteur d’authentification physique (2FA) lors d’une connexion. Une fois activé, en plus du mot de passe classique, l’utilisateur doit approuver chaque tentative de connexion à son compte en pressant un bouton sur sa Ledger. Dans ce contexte, la Ledger fonctionne de manière similaire à une Yubikey. U2F constitue en réalité une sous-composante du standard FIDO2, qui l’englobe tout en apportant des améliorations significatives, notamment le support natif des navigateurs modernes et une plus grande souplesse dans la gestion des clés d’authentification.

Ces méthodes reposent sur la cryptographie asymétrique : aucune donnée secrète n’est transmise, ce qui rend les attaques par hameçonnage ou interception inefficaces. U2F et FIDO2 sont aujourd’hui pris en charge par de nombreux services en ligne.

Dans ce tutoriel nous allons découvrir comment activer U2F et FIDO2 pour l’authentification à deux facteurs avec votre Ledger.

**Remarque :** U2F et FIDO2 sont pris en charge sur tous les appareils Ledger équipés des firmwares récents : à partir de la version 2.1.0 pour les Nano X et Nano S classique, et à partir de la version 1.1.0 pour la Nano S Plus. Pour les modèles Stax et Flex, la compatibilité est assurée nativement.

## Installer l'application Ledger Security Key

Si vous utilisez un appareil Ledger, vous savez probablement que le firmware ne contient pas, à lui seul, toutes les fonctionnalités nécessaires à la gestion de portefeuilles crypto. Par exemple, pour utiliser un portefeuille Bitcoin, il faut installer l’application "*Bitcoin*". De la même manière, pour gérer les clés utilisées dans le cadre du MFA, vous devrez installer l’application "*Security Key*".

Avant de commencer, assurez-vous d'avoir configuré votre portefeuille Bitcoin sur votre Ledger. Il est important de sauvegarder correctement votre phrase mnémonique, car les clés utilisées pour le 2FA sont dérivées de cette phrase. En cas de perte ou de dommage de votre Ledger, vous pourrez récupérer l'accès à vos clés en saisissant votre phrase mnémonique sur un autre appareil Ledger (pour le moment, les identifiants FIDO2 en mode "*passwordless*" ne sont pas encore pris en charge sur les Ledger, il n'y a donc pas d'identifiants résidents).

Branchez votre Ledger à votre ordinateur et déverrouillez-la.

![Image](assets/fr/01.webp)

Pour installer l’application, ouvrez le logiciel [Ledger Live](https://www.ledger.com/ledger-live), puis rendez-vous dans l’onglet "*My Ledger*". Recherchez l’application "*Security Key*" et installez-la sur votre appareil.

![Image](assets/fr/02.webp)

L’application "*Security Key*" devrait maintenant apparaître aux côtés des autres applications installées sur votre Ledger.

![Image](assets/fr/03.webp)

Cliquez sur l’application pour la laisser ouverte en vue des prochaines étapes du tutoriel.

![Image](assets/fr/04.webp)

## Utiliser U2F/FIDO2 pour du 2FA avec une Ledger

Accédez au compte que vous souhaitez sécuriser avec une authentification à deux facteurs. Par exemple, je vais utiliser un compte Bitwarden. Vous trouverez généralement l'option du 2FA dans les paramètres du service, sous les onglets "*authentification*", "*sécurité*", "*connexion*" ou bien "*mot de passe*".

![Image](assets/fr/05.webp)

Dans la section dédiée à l'authentification à deux facteurs, sélectionnez l'option "*Passkey*" (le terme peut varier selon le site que vous utilisez).

![Image](assets/fr/06.webp)

Il vous sera souvent demandé de confirmer votre mot de passe actuel.

![Image](assets/fr/07.webp)

Donnez un nom à votre clé de sécurité pour pouvoir la reconnaître facilement, puis cliquez sur "*Read Key*".

![Image](assets/fr/08.webp)

Les détails de votre compte s’afficheront sur l’écran de la Ledger. Appuyez sur le bouton "*Register*" pour confirmer (ou sur les deux boutons simultanément, selon le modèle que vous utilisez).

![Image](assets/fr/09.webp)

La clé d'accès a bien été enregistrée.

![Image](assets/fr/10.webp)

Enregistrez cette clé de sécurité.

![Image](assets/fr/11.webp)

Désormais, lorsque vous voudrez vous connecter à votre compte, en plus de votre mot de passe habituel, on vous demandera de connecter votre Ledger.

![Image](assets/fr/12.webp)

Vous pourrez alors appuyer sur le bouton "*Log in*" affiché sur l’écran de votre Ledger pour valider l’authentification (ou sur les deux boutons simultanément, selon le modèle que vous utilisez).

![Image](assets/fr/13.webp)

L'utilisation d'un hardware wallet Ledger pour l'authentification à deux facteurs présente l'avantage de pouvoir récupérer facilement vos clés grâce à la phrase mnémonique. En plus de cette sauvegarde de base, vous pouvez aussi utiliser un code d'urgence fourni par chaque service où vous avez activé le 2FA. Ce code d'urgence vous permet de vous connecter à votre compte en cas de perte de votre clé de sécurité. Il remplace donc le 2FA pour une connexion si nécessaire.

Par exemple, sur Bitwarden, vous pouvez accéder à ce code en cliquant sur "*View recovery code*".

![Image](assets/fr/14.webp)

Je vous recommande de conserver ce code dans un endroit différent de celui où vous stockez votre mot de passe principal, afin d'éviter qu'ils ne soient volés ensemble. Par exemple, si votre mot de passe est sauvegardé dans un gestionnaire de mots de passe, gardez votre code d'urgence du 2FA sur papier, séparément.

Cette approche vous offre deux niveaux de sauvegarde en cas de perte de votre Ledger pour l'authentification 2FA : une première sauvegarde grâce à la phrase mnémonique pour tous vos comptes et une seconde spécifique à chaque compte avec les codes d'urgence. Toutefois, il est important de **ne pas confondre le rôle de la phrase mnémonique et celui du code d'urgence** :
- La phrase mnémonique de 12 ou 24 mots vous donne accès non seulement aux clés utilisées pour le 2FA sur tous vos comptes, mais aussi à vos bitcoins sécurisés avec votre Ledger ;
- Le code d'urgence vous permet de contourner temporairement la demande de 2FA uniquement sur le compte concerné (dans cet exemple, uniquement sur Bitwarden).

Félicitations, vous êtes maintenant au point sur l'utilisation de votre Ledger pour le MFA ! Si vous avez trouvé ce tutoriel utile, je vous serais très reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager ce tutoriel sur vos réseaux sociaux. Merci beaucoup !

Je vous conseille également de découvrir cet autre tutoriel dans lequel nous abordons une autre solution pour l'authentification U2F et FIDO2 :

https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

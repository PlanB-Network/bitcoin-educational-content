---
name: AUTHY 2FA
description: Comment utiliser une application de 2FA ?
---
![cover](assets/cover.webp)

De nos jours, l'authentification à deux facteurs (2FA) est devenue indispensable pour renforcer la sécurité des comptes en ligne face aux accès non autorisés. Avec l'augmentation des attaques informatiques, se reposer uniquement sur un mot de passe pour sécuriser vos comptes est parfois insuffisant. Le 2FA introduit une couche de sécurité supplémentaire en requérant une seconde forme d'authentification en plus du mot de passe. Cette vérification peut prendre plusieurs formes, comme un code envoyé par SMS, un code dynamique généré par une application dédiée, ou encore l'utilisation d'une clé de sécurité physique. L'utilisation du 2FA diminue grandement les risques de compromission de vos comptes, même en cas de vol de votre mot de passe.

## Le 2FA par application d'authentification

Nous découvrirons d'autres solutions comme les clés de sécurité physique dans d'autres tutoriels, mais dans celui-ci, je vous propose de parler spécifiquement des applications de 2FA. Le fonctionnement de ces applications est assez simple : lorsque le 2FA est activé sur un compte, à chaque connexion, il vous sera demandé non seulement votre mot de passe habituel, mais aussi un code à 6 chiffres. Ce code est généré par votre application de 2FA. Une caractéristique importante de ce code à 6 chiffres est qu'il n'est pas statique ; un nouveau code est généré par l'application toutes les 30 secondes.

01

Le renouvellement du code toutes les 30 secondes rend très difficile pour un attaquant d'accéder à votre compte. Ce système empêche les attaquants de réutiliser un code volé ou intercepté, car celui-ci expire rapidement. Ainsi, même si un attaquant parvient à obtenir le code, il ne pourra l'utiliser que durant une très courte fenêtre de temps avant qu'un nouveau code ne soit requis. De plus, le fait que le code change si fréquemment réduit considérablement le temps disponible pour un pirate qui tenterait de deviner le code par brute force.

Le 2FA via des applications d'authentification représente donc une méthode facile à utiliser et gratuite pour améliorer significativement la sécurité de vos comptes en ligne.

Il existe de nombreuses applications pour configurer le 2FA, parmi lesquelles Google Authenticator et Microsoft Authenticator sont les plus connues. Toutefois, dans ce tutoriel, je souhaite vous présenter une autre solution moins connue nommée Authy. Toutes ces applications fonctionnent grâce au même protocole TOTP (*Time based One Time Password*), ce qui rend leur utilisation assez similaire.

Authy offre toutefois plusieurs avantages par rapport aux autres solutions des géants de l'informatique. Tout d'abord, elle vous permet de synchroniser vos tokens 2FA sur plusieurs appareils, ce qui peut être utile en cas de perte ou de changement de téléphone. Authy vous permet également de générer une sauvegarde chiffrée et de la stocker en ligne, ce qui vous assure de ne jamais perdre l'accès à vos tokens, même en cas de perte de votre appareil principal. Sur le plan de l'interface utilisateur, je trouve personnellement que Authy propose également une expérience plus agréable et intuitive que ses alternatives.

## Comment installer et configurer Authy ?

Sur votre appareil mobile, rendez-vous sur le magasin d'application (Google Play Store ou Apple Store), et recherchez "Twilio Authy Authenticator".

02









## Comment mettre en place le 2FA sur un compte ?











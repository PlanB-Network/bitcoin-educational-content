---
name: SMS4Sats
description: Recevoir et envoyer des SMS anonymement en payant en Bitcoin Lightning
---

![cover](assets/cover.webp)

La vérification par SMS est devenue un passage obligé pour accéder à de nombreux services en ligne. Que ce soit pour créer un compte sur une plateforme, valider une inscription ou confirmer une identité, les sites web exigent quasi-systématiquement un numéro de téléphone. Cette pratique généralisée pose un problème majeur pour quiconque souhaite préserver sa vie privée : votre numéro personnel devient un identifiant permanent, reliant vos différentes activités numériques à votre identité réelle et ouvrant la porte aux sollicitations commerciales indésirables.

**SMS4Sats** répond à cette problématique en proposant des numéros de téléphone temporaires pour recevoir et envoyer des SMS. Le service se distingue par son modèle sans inscription et son paiement exclusif en Bitcoin via le Lightning Network. Contre quelques satoshis, vous obtenez un numéro jetable permettant de valider une inscription sans jamais révéler votre numéro personnel.

Ce tutoriel vous guide dans l'utilisation des trois fonctionnalités de SMS4Sats : recevoir un SMS de vérification, envoyer un SMS anonyme, et louer un numéro temporaire pour plusieurs heures.

## Qu'est-ce que SMS4Sats ?

SMS4Sats est un service en ligne accessible sur [sms4sats.com](https://sms4sats.com) permettant de gérer des SMS de manière anonyme grâce au paiement en Bitcoin Lightning. Le service propose trois fonctionnalités distinctes : la réception de codes de vérification à usage unique, l'envoi de SMS vers n'importe quel numéro, et la location de numéros temporaires pour plusieurs heures.

### Philosophie et modèle de fonctionnement

Le projet s'inscrit dans une logique de confidentialité maximale et de souveraineté financière. En n'exigeant aucune création de compte et en acceptant uniquement les paiements Bitcoin Lightning, SMS4Sats élimine complètement le besoin de fournir des données personnelles. Aucune adresse email, aucune carte bancaire, aucune information nominative n'est requise. Seul le paiement Lightning suffit pour accéder aux services.

Le service supporte plus de 400 sites et applications dans environ 120 pays, couvrant la majorité des besoins de vérification courants. Cette couverture géographique étendue permet de valider des inscriptions sur des plateformes variées, des réseaux sociaux aux services de messagerie.

### Modèle de paiement conditionnel

Pour la fonctionnalité de réception de SMS, SMS4Sats utilise des factures Lightning conditionnelles (hodl invoices). Ce mécanisme garantit que vous n'êtes débité que si le SMS est effectivement reçu. Si aucun message n'arrive dans le délai imparti (20 minutes maximum), le paiement est automatiquement annulé et les satoshis retournent dans votre portefeuille. Cette garantie ne s'applique pas aux fonctionnalités d'envoi et de location, qui sont non remboursables.

## Les trois fonctionnalités de SMS4Sats

L'interface de SMS4Sats s'organise autour de trois onglets correspondant à trois usages distincts : **RECEIVE** pour recevoir des codes de vérification, **SEND** pour envoyer des SMS anonymes, et **RENT** pour louer un numéro temporaire.

### Recevoir un SMS

La fonctionnalité principale permet d'obtenir un numéro temporaire pour recevoir un code de vérification unique. Une fois le code reçu et utilisé, le numéro est définitivement désactivé.

### Envoyer un SMS

Cette fonctionnalité permet d'envoyer un SMS vers n'importe quel numéro de téléphone sans révéler votre identité. Le destinataire recevra le message depuis un numéro anonyme.

### Louer un numéro

Pour les utilisateurs ayant besoin de recevoir plusieurs SMS sur un même numéro, SMS4Sats propose une option de location temporaire. Cette option permet de recevoir et d'envoyer plusieurs messages pendant la durée de location.

**Note sur les tarifs** : Les prix affichés dans ce tutoriel sont donnés à titre indicatif. Ils varient selon le pays du numéro, le service cible et la demande du moment. À titre d'exemple, un SMS pour Telegram France peut coûter entre 1500 et 5000 satoshis selon les conditions. Vérifiez toujours le montant exact de la facture Lightning avant de payer.

## Recevoir un SMS de vérification

Voyons en détail comment utiliser SMS4Sats pour recevoir un code de vérification, illustré par la création d'un compte Telegram.

### Étape 1 : Sélectionner le pays et le service

Rendez-vous sur [sms4sats.com](https://sms4sats.com) et restez sur l'onglet **RECEIVE**. Sélectionnez le pays du numéro souhaité dans le menu déroulant. Si le service cible de votre inscription figure dans la liste, sélectionnez-le pour optimiser les chances de réception.

![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)

Dans cet exemple, nous sélectionnons la France comme pays et Telegram comme service cible. Cliquez sur **NEXT** pour passer à l'étape suivante.

### Étape 2 : Payer la facture Lightning

Une facture Lightning s'affiche sous forme de QR code. Le montant varie selon le pays et le service sélectionnés. Scannez le QR code avec votre portefeuille Lightning ou copiez l'invoice pour la payer manuellement.

![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)

Notez le message important : "No SMS Code = No Payment". Si vous ne recevez pas de SMS, votre paiement sera automatiquement annulé et remboursé dans un délai maximum de 20 minutes.

### Étape 3 : Obtenir le numéro temporaire

Une fois le paiement confirmé, le numéro de téléphone temporaire s'affiche immédiatement. Un compteur indique le temps restant pour recevoir le SMS.

![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)

Copiez ce numéro (ici +33 7 74 70 09 66) pour l'utiliser sur le service où vous souhaitez vous inscrire.

### Étape 4 : Utiliser le numéro sur le service cible

Indiquez le numéro temporaire sur l'application ou le site où vous créez votre compte. Dans notre exemple avec Telegram, entrez le numéro, confirmez-le, puis attendez le code de vérification.

![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)

Le processus est identique à une inscription classique : vous entrez le numéro, Telegram envoie un code de vérification par SMS, puis vous finalisez la création du compte.

### Étape 5 : Récupérer le code de vérification

Retournez sur l'interface SMS4Sats. Dès que le SMS est reçu, le code d'activation s'affiche automatiquement. Cliquez sur **COPY CODE** pour le copier facilement.

![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)

Entrez ce code sur le service cible pour finaliser votre inscription. Le numéro temporaire est ensuite désactivé définitivement.

## Envoyer un SMS anonyme

SMS4Sats permet également d'envoyer des SMS vers n'importe quel numéro sans révéler votre identité.

### Étape 1 : Rédiger le message

Cliquez sur l'onglet **SEND**. Entrez le numéro de téléphone destinataire avec son indicatif international et rédigez votre message (maximum 1600 caractères).

![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)

Cliquez sur **NEXT** pour procéder au paiement.

### Étape 2 : Payer et envoyer

Payez la facture Lightning affichée. Une fois le paiement confirmé, le SMS est envoyé immédiatement au destinataire.

![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)

Un code de confirmation s'affiche pour attester que le message a bien été transmis. Le destinataire recevra le SMS depuis un numéro anonyme.

## Louer un numéro temporaire

Pour les usages nécessitant plusieurs SMS sur un même numéro, la fonctionnalité RENT permet de louer un numéro pendant plusieurs heures.

### Configuration de la location

Cliquez sur l'onglet **RENT**. Sélectionnez le pays et la durée souhaitée.

![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)

**Points importants à noter :**
- Le prix varie selon le pays et la durée choisie
- **Les locations ne sont pas remboursables**, contrairement aux SMS à usage unique
- Les numéros loués ne fonctionnent généralement pas avec Telegram
- Cette option est adaptée pour s'inscrire à plusieurs services successivement

Après avoir cliqué sur **NEXT** et payé la facture Lightning, vous obtenez un numéro utilisable pendant toute la durée de location pour recevoir et envoyer des SMS.

## Avantages et limitations

### Points forts

**Aucune donnée personnelle requise** : Le modèle sans inscription garantit qu'aucune information nominative n'est collectée.

**Trois fonctionnalités complémentaires** : Réception, envoi et location couvrent la plupart des besoins.

**Paiement en Bitcoin uniquement** : Le Lightning Network permet des transactions instantanées et pseudonymes.

**Remboursement automatique** : Pour la réception de SMS, le système de hodl invoices garantit que vous ne payez que si le SMS arrive.

### Contraintes à considérer

**Sécurité relative du canal SMS** : Les codes par SMS ne constituent pas une méthode d'authentification robuste et ne doivent pas servir pour des comptes sensibles.

**Compatibilité variable** : De nombreux sites détectent et bloquent les numéros virtuels. Plusieurs tentatives peuvent être nécessaires.

**Numéros non réutilisables** : Après usage unique, le numéro est recyclé et ne peut pas être récupéré.

**Locations non remboursables** : Contrairement aux SMS uniques, les locations ne bénéficient pas de la garantie de remboursement.

## Bonnes pratiques

### Utilisez Tor pour plus de confidentialité

SMS4Sats est accessible via [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). Cette configuration masque votre adresse IP lors de l'accès au service.

### Évitez les comptes critiques

N'utilisez jamais un numéro jetable pour vos comptes importants (banque, email principal). Si ces plateformes exigent de revalider votre numéro ultérieurement, vous perdrez l'accès au compte.

### Cloisonnez vos identités numériques

Pour les comptes pseudonymes, combinez le numéro temporaire avec une adresse email jetable et un navigateur isolé de votre usage habituel.

### Privilégiez une 2FA robuste

Dès que votre compte est créé, activez des solutions d'authentification plus solides : application TOTP (Aegis, Ente Auth) ou clé de sécurité physique FIDO2.

## Conclusion

SMS4Sats représente une solution complète pour gérer ses SMS de manière confidentielle. Que ce soit pour recevoir un code de vérification, envoyer un message anonyme ou louer un numéro temporaire, le service répond à différents besoins de confidentialité grâce au paiement en Bitcoin Lightning.

Gardez néanmoins à l'esprit ses limitations : le service ne garantit pas un anonymat absolu et n'est pas adapté aux comptes sensibles ou de longue durée. Utilisé à bon escient et en connaissance de ses limites, SMS4Sats constitue un outil pratique pour reprendre le contrôle sur vos communications téléphoniques.

## Ressources

- [Site officiel SMS4Sats](https://sms4sats.com)
- [FAQ du service](https://sms4sats.com/faq)
- [Adresse Tor](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)

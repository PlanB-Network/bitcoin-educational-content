---
name: BitcoinVoucherBot P2P
description: Comment acheter et vendre des Bitcoin P2P avec BitcoinVoucherBot
---

![image](assets/cover.webp)



On entend encore parler de BitcoinVoucherBot, un bot Telegram créé pour acheter Bitcoin sans [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) par virement bancaire SEPA. Malheureusement, depuis novembre 2025, le BitcoinVoucherBot sous sa forme centralisée n'est plus disponible en tant que service sans KYC.



Dans ce guide, nous verrons comment fonctionne la nouvelle implémentation qui permet aux utilisateurs d'acheter et de vendre du Bitcoin directement sur la nouvelle place de marché P2P (Peer-To-Peer), donc sans KYC. Pour contrer les nouvelles restrictions qui menacent de plus en plus la liberté numérique et la vie privée, les développeurs ont créé cette extension, donnant aux utilisateurs la possibilité d'acheter et de vendre des Bitcoin avec un haut degré d'anonymat à travers P2P (Peer-To-Peer). Voyons ensemble comment fonctionne cette nouvelle méthode d'échange.



Pour utiliser le service, vous devrez effectuer des transferts via Lightning Network. Assurez-vous donc d'avoir un wallet qui supporte ce protocole et vous permet d'utiliser un "LNURL" ou un "Lightning Address" pour recevoir et envoyer des fonds.



Parmi les portefeuilles pris en charge, nous pouvons trouver :





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Garde)
- [Wallet de Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Dépositaire avec échange contre non-dépositaire)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Ou tout wallet qui a un "Lightning Address" et génère une facture Bolt11. Les portefeuilles qui generate une facture Bolt12 ne sont pas actuellement pris en charge. Pour plus d'informations, voir la définition de [Bolt](https://planb.academy/resources/glossary/bolt).



Pour ce tutoriel, compte tenu de sa facilité d'utilisation immédiate, nous utiliserons Wallet of Satoshi.



**Attention** : Wallet of Satoshi, bien que populaire parmi les débutants, est dépositaire, avec un contrôle limité sur les fonds ; ne l'utilisez que de manière transitoire, en transférant immédiatement à un non-dépositaire pour une souveraineté totale. À partir d'octobre 2025, il comprend un mode stable d'autodétention dans le monde entier sur iOS/Android (mettre à jour l'application), avec des clés privées autonomes, le passage d'un mode à l'autre, des adresses Lightning personnalisées et la sauvegarde seed en 12 mots. Cependant, elle reste une solution provisoire jusqu'à la consolidation, préférant wallet non custodial mature pour la gestion à long terme.



C'est très bien ! Nous pouvons maintenant commencer notre voyage, qui vous guidera pas à pas dans la création de votre compte, la gestion des correspondances d'achat et de vente, et l'utilisation de votre espace réservé.



## Wallet et inscription



Tout d'abord, si vous ne l'avez pas encore installé sur votre smartphone, téléchargez Wallet of Satoshi.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Si vous n'avez jamais utilisé Wallet of Satoshi et que vous souhaitez comprendre son fonctionnement, je vous suggère de suivre ce tutoriel afin de l'activer correctement et de le sauvegarder en toute sécurité.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Maintenant que votre wallet est prête, vous pouvez commencer à envoyer une petite quantité de sats. Gardez à l'esprit que, pour compléter votre inscription à la plateforme P2P (Peer-To-Peer), il vous sera demandé d'envoyer 1000 sats comme mesure de contrôle : ceci afin de créer une barrière contre toute attaque de type "phantom match" (escroquerie), empêchant quiconque de s'inscrire sans filtre anti-spam.



![image](assets/it/02.webp)



Nous pouvons maintenant ouvrir la plateforme P2P (Peer-To-Peer) pour procéder à l'inscription. Vous pouvez vous connecter à partir d'un ordinateur de bureau ou d'un navigateur sur smartphone, via le BitcoinVoucherBot Telegram ou via des liens .onion pour garantir un niveau de confidentialité encore plus élevé.



si vous choisissez d'utiliser le lien Tor .onion, je vous recommande également "Tor Browser". Si vous ne le connaissez pas encore, vous pouvez en savoir plus sur ce lien :



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Choisissez maintenant la manière dont vous souhaitez atteindre la plate-forme.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Browser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Vous serez redirigé vers la page principale.



appuyez sur "Get Starter" pour démarrer immédiatement



![image](assets/it/03.webp)



Sur l'écran suivant, vous devez choisir un mot de passe et le saisir (case A), puis le répéter (case B). Je vous recommande d'enregistrer immédiatement ce mot de passe sur un support de sauvegarde, qui peut être un dispositif numérique sécurisé tel que le "Bitwarden" :



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

ou sauvegarder votre mot de passe sur un support papier (**avertissement** : ce n'est pas une bonne solution, mais elle est acceptable si elle est conçue comme une solution temporaire).



Cochez la case de vérification dans laquelle vous déclarez que vous n'êtes pas un robot (case C). Remarque N'activez pas le cryptage RSA si vous ne savez pas exactement de quoi il s'agit et comment il fonctionne. Vous ne devez rien faire à ce stade. Cliquez sur "Générer un avatar" ("Generate Avatar") (case D).



![image](assets/it/04.webp)



Vous devez maintenant payer les 1000 sats pour compléter l'inscription.



1. En commençant par le haut, vous verrez d'abord votre "Avatar ID", généré de manière aléatoire et extrêmement important Sauvegardez-le soigneusement, comme je vous ai conseillé de le faire avec le mot de passe.


2. Vous devez ensuite saisir votre "Lightning Address" dans le champ ci-dessous. Cela vous permettra de recevoir des paiements si vous achetez Bitcoin, ou d'obtenir des remboursements. Si vous utilisez Wallet ou Satoshi, vous pourrez copier votre Address en cliquant sur recevoir.


3. Cochez la case de vérification dans laquelle vous indiquez que vous n'êtes pas un robot.


4. Effectuez le paiement de 1000 sats pour obtenir l'accès à votre zone réservée. Si vous ne pouvez pas l'encadrer, cliquez dessus avec votre souris (sur PC) ou tapez dessus avec votre doigt (sur les navigateurs/smartphones Telegram) pour copier l'adresse que vous devez coller dans Wallet of Satoshi et compléter le paiement de la facture.



![image](assets/it/05.webp)



Il s'agit de votre LNURL Address.



![image](assets/it/06.webp)



Félicitations !!! Vous avez créé votre avatar de manière permanente et vous pouvez consulter le résumé ici. Une fois de plus, je vous recommande de sauvegarder soigneusement votre avatar et votre mot de passe, comme je l'ai déjà suggéré.



Cliquez sur "I've saved my credentials, continue" (traduit par : "J'ai sauvegardé mes informations d'identification, continuez")



![image](assets/it/07.webp)



Vous êtes maintenant au cœur de la plateforme, où vous pouvez voir toutes les correspondances avec leurs détails. Pour une vision plus claire, vous trouverez ci-dessous les images inhérentes au site web à partir d'un ordinateur de bureau.





- "Le "type" ("type") définit s'il s'agit d'une vente ("sell") ou d'un achat ("buy")
- "Montant" ("Amount") : indique combien de sats l'utilisateur vend si la correspondance est de type "Vendre", ou combien de Bitcoin l'utilisateur est prêt à acheter si la correspondance est de type "Acheter".
- "BTC Price with Margin" ("Prix BTC avec marge") : indique le prix en tenant compte de la marge appliquée au-dessus de la valeur marquée.
- la "marge" ("Margin") est le pourcentage appliqué au prix du marché. Avec un signe moins (-), vous obtenez une réduction sur le prix du marché, avec un signe plus (+), une prime est appliquée au prix du marché.
- "Méthode" ("Method") indique la méthode par laquelle l'utilisateur préfère être payé.
- le "créateur" est l'avatar unique utilisé par l'utilisateur sur la plateforme.
- "Rep" (réputation) Le niveau de réputation de l'utilisateur va de -5 peu fiable à +5 extrêmement fiable.
- "Statut" ("Status") : indique le statut de l'appariement. Dans l'exemple de la capture d'écran, toutes les correspondances semblent être "ouvertes" ("Open").
- "Expiration" ("Expiration") : indique le temps restant avant que le match n'expire et ne soit annulé s'il n'a été choisi par personne.



![image](assets/it/08.webp)



En haut à droite, cliquez sur votre avatar pour accéder à votre profil.



![image](assets/it/09.webp)



Vous pouvez y voir votre nom d'avatar, votre ID utilisateur, votre date de création et votre réputation, qui influencera positivement ou négativement votre comportement lors des négociations.



![image](assets/it/10.webp)



Dans la section Paramètres, vous pouvez consulter votre "Lightning Address", saisi lors de l'enregistrement, et le modifier si nécessaire. Vous avez également la possibilité de créer une clé publique, qui, comme nous l'avons dit, ne doit être configurée que si vous avez les compétences nécessaires. Elle est utilisée pour crypter les messages que vous échangerez avec votre homologue directement à partir de votre ordinateur.



La fonction Telegram Notification est fortement recommandée. En l'activant, un code QR apparaîtra pour que vous puissiez le cadrer avec l'application Telegram : de cette façon, vous recevrez des notifications en temps réel sur toutes les actions liées à vos matchs, directement dans le chat bot sur Telegram.



![image](assets/it/11.webp)



Enfin, vous trouverez votre section de parrainage, avec les gains générés par les utilisateurs que vous avez invités. À partir de là, vous pouvez utiliser le bouton pour partager votre lien ou votre code QR et, un peu plus bas, afficher une liste de correspondances pour suivre votre réputation ainsi que le score correspondant.



![image](assets/it/12.webp)



## Créer une commande pour acheter Bitcoin



Accédez à la place de marché : dans la barre de navigation principale, cliquez sur le symbole du panier "Place de marché" ("Place de marché") pour ouvrir le carnet de commandes. Commencez ensuite une nouvelle commande : appuyez sur le bouton "Nouvelle commande" ("Nouvelle commande") pour lancer le processus.



![image](assets/it/13.webp)





- Définir les détails de la commande :
- Sélectionnez l'option "Acheter Bitcoin" ("Acheter Bitcoin").
- Saisissez le montant de sats que vous souhaitez.
- Définir la marge de prix (entre -20% et +20% par rapport à la valeur du marché).
- Choisissez le mode de paiement (Instant SEPA, etc.).
- Indique la devise préférée.
- Confirmer la commande : cliquer sur "Créer la commande" ("Confirmer la commande") pour passer à l'étape du dépôt.



![image](assets/it/14.webp)



Acompte requis : un acompte égal à 10 % du montant total, plus des frais de service, est requis pour activer la commande.




- Paiement d'un acompte : lorsque la commande est créée, le système génère automatiquement une facture Lightning. Le dépôt n'est que temporaire et est remboursé lorsque la commande est terminée.
- Caractéristiques principales :
- Dépôt de garantie : 10% de la valeur de la commande.
- Frais de service : coût de l'utilisation de la plateforme.
- Délai : Vous avez 5 minutes pour effectuer le paiement, sinon la transaction expire.



![image](assets/it/15.webp)



Une fois le paiement effectué, l'ordre apparaîtra dans le carnet et sera visible par tous les utilisateurs, qui pourront le choisir et l'accepter. Pour créer un ordre de vente, il vous suffit de cliquer sur "Vendre Bitcoin" ("Sell Bitcoin"), d'entrer la quantité de satoshi que vous souhaitez vendre, de fixer la marge, de sélectionner le mode de paiement et la devise, puis de procéder au dépôt de 10 % à titre de garantie. Une fois l'opération terminée, votre correspondance sera visible dans la liste.



![image](assets/it/16.webp)



## Comment accepter une commande



1. Les vendeurs peuvent consulter la liste de toutes les commandes disponibles dans le livre.


2. Vérifier les détails : chaque commande comporte des informations telles que




  - Quantité de Bitcoin,
  - Marge sur le prix,
  - Mode de paiement,
  - Réputation de l'utilisateur.



![image](assets/it/17.webp)



3. Cliquez sur la commande pour ouvrir la fiche complète avec toutes les informations.


4. Cliquez sur "Sell Bitcoin" ("Vendre Bitcoin") pour accepter la proposition.



![image](assets/it/18.webp)



## Dépôt de garantie exigé par le vendeur



Lorsque la commande est acceptée, le système génère une facture à payer. Le dépôt comprend



- Le montant total de la commande,



- la commission de service.



Le paiement de l'acompte doit être effectué dans le délai imparti, faute de quoi la transaction ne sera pas confirmée.



![image](assets/it/19.webp)



## Envoi d'instructions de paiement



Une fois le dépôt effectué, la transaction apparaît sur le tableau de bord personnel du vendeur, qui doit fournir les détails à l'acheteur pour effectuer le paiement en monnaie fiduciaire.



1. Le vendeur affiche la transaction active dans son tableau de bord.


2. Cliquez sur "Soumettre les instructions de paiement"


3. Saisissez toutes les informations nécessaires au paiement en monnaie fiduciaire (IBAN, destinataire, adresse, motif du paiement, etc.).


4. Cliquez sur "Send Message" ("Envoyer un message") pour transmettre les données à l'acheteur.



![image](assets/it/20.webp)



## Procédure de paiement



L'acheteur reçoit, dans le cadre du chat de la plateforme, un message contenant toutes les données nécessaires pour effectuer le paiement en monnaie fiduciaire :




- Coordonnées bancaires : IBAN avec nom et adresse du titulaire du compte du vendeur.
- Montant exact : montant exact en fiats à transférer.
- Causal/description : texte à inclure dans la transaction.
- Délai : date limite à laquelle le paiement doit être effectué.



Le transfert a lieu en dehors du système P2P et doit être effectué par l'intermédiaire de l'institution bancaire.



⚠️ **Note importante:** la confirmation sur la plateforme ne doit être faite qu'après avoir organisé le transfert ou le paiement en monnaie fiduciaire par l'intermédiaire de votre banque.



![image](assets/it/21.webp)



## Confirmation du paiement fiat



Cette étape est cruciale pour l'acheteur et ne doit être effectuée qu'après avoir vérifié que le paiement a bien été envoyé.



1. Données de réception : l'acheteur a reçu des instructions de paiement de la part du vendeur.


2. Exécution du paiement : le virement en monnaie fiduciaire est effectué à partir du compte bancaire de l'utilisateur.


3. Vérification : vérifier que l'opération a été traitée correctement.


4. Confirmer sur la plateforme : cliquer sur "Confirm fiat payment" ("Confirmer le paiement fiat") sur la page de transaction.


Le bouton "Confirmer le paiement fiat" apparaît dans la section des transactions et ne doit être utilisé qu'après avoir vérifié que le paiement a bien été envoyé.



![image](assets/it/22.webp)



La dernière étape du processus consiste pour le vendeur à confirmer la réception du paiement en fiats, après quoi les sats sont remis à l'acheteur.



![image](assets/it/23.webp)



## Conclusion



En espérant que ce tutoriel vous aidera à utiliser une nouvelle méthode pour échanger des bitcoins ou même simplement les acheter, que ce soit pour votre propre réserve de valeur ou pour commencer à donner vie aux paiements quotidiens. Il n'en reste pas moins qu'il s'agit d'une porte à explorer pour faire face à ce qui est sur le point de se produire dans notre monde numérique.



L'étau des organismes qui nous contrôlent se resserre pour donner naissance à un Internet de plus en plus contrôlé. En achetant P2P, vous conserverez vos achats dans l'anonymat le plus total, sans laisser de trace et sans répercussion de la part de tiers.
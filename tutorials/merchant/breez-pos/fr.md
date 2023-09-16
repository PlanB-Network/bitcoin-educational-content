---
name: Breez point de vente

description: Guide pour commencer à accepter des bitcoins en utilisant Breez POS
---

![cover](assets/cover.jpeg)

## Qu'est-ce que Breez POS ?

**Breez** est une application Lightning complète et non dépositaire. Explorons cela en détail :

- **Lightning** est un réseau de paiement bitcoin qui réduit les temps de transaction de minutes à millisecondes et les frais de transaction de plusieurs dollars à quelques centimes ou moins. Lightning transforme le bitcoin de l'or numérique en monnaie numérique tout en préservant tous les avantages qui font du bitcoin une excellente monnaie.
- **Non dépositaire** signifie que Breez ne prend pas possession de l'argent des utilisateurs. De nombreuses applications Lightning prennent en charge l'argent de leurs utilisateurs. Elles sont essentiellement des banques bitcoin. Avec une application non dépositaire comme Breez, tous les utilisateurs sont leur propre banque.
- **Complet** signifie que Breez s'occupe automatiquement et en arrière-plan de presque toutes les opérations techniques. Des choses comme la création de canaux, la liquidité entrante et l'acheminement restent sous le capot. (Mais Breez est également open source, donc ceux qui souhaitent auditer la technologie sont les bienvenus !)

**Breez POS** est l'abréviation de notre mode point de vente. En d'autres termes, Breez fonctionne comme une caisse enregistreuse numérique pour les entreprises et les commerçants qui souhaitent accepter des paiements Lightning (en plus de son mode "standard", qui est comme la version numérique d'un portefeuille en cuir pour le bitcoin, et un lecteur de podcast de nouvelle génération). Voyons maintenant comment configurer Breez en tant que caisse enregistreuse Lightning pour votre entreprise.

## Comment commencer avec Breez ?

1. La première étape consiste à télécharger l'application. Elle est disponible pour Android et iOS (installez TestFlight et cliquez sur le lien depuis votre appareil).
2. Breez peut se sauvegarder automatiquement sur Google Drive, iCloud ou n'importe quel serveur WebDav.
   > Notez que chaque appareil exécute son propre nœud Lightning. Vous pouvez exécuter le mode POS sur autant d'appareils que vous le souhaitez, mais les soldes resteront séparés.
3. Avec l'application ouverte, cliquez sur l'icône en haut à gauche pour accéder au mode Point de Vente.

## Configuration du POS

1. Cliquez sur cette icône en haut à gauche, puis sur Point de Vente > Paramètres POS.

### Le mot de passe du gestionnaire

Dans les paramètres POS, vous avez la possibilité de créer un mot de passe de gestionnaire. Le mot de passe du gestionnaire rend impossible l'envoi de paiements sortants depuis l'application Breez sans autorisation. Le personnel de vente ne pourra recevoir que des paiements depuis l'appareil. Notez que si vous utilisez cette option, vous voudrez peut-être également empêcher l'accès à la sauvegarde de Breez, il est donc recommandé d'utiliser un compte WebDav externe (par exemple, Nextcloud) pour ce cas d'utilisation.

### La liste des articles

La liste des articles est un catalogue d'articles à vendre et de leurs prix. Il existe deux façons d'ajouter des articles à la liste :

- Pour saisir les articles un par un, cliquez sur Articles en haut de la vue principale du POS, puis sur le signe "+" en bas à droite. Ici, vous pouvez saisir le nom d'un seul type d'article, le prix (affiché dans l'équivalent de la devise de votre choix) et le SKU (un identifiant interne unique pour ce type d'article ; il est facultatif).
- Pour entrer plusieurs articles en même temps, cliquez sur l'icône calculatrice en haut à gauche, puis Point de vente > Préférences > Paramètres du POS, puis cliquez sur les trois points à droite de la liste des articles, puis sur Importer depuis un fichier CSV. Cela vous permettra d'importer un fichier CSV que vous avez préparé à l'avance contenant les noms, les prix et les SKUs de vos articles.

### Affichage en Fiat

Breez envoie et reçoit uniquement des bitcoins, et pour la plupart des transactions sur Lightning, qui ont tendance à être de petits montants, la somme est généralement affichée en Satoshis, également appelés sats (1 BTC = 100 000 000 sats). Cependant, de nombreux commerçants trouvent pratique de pouvoir voir (et indiquer aux clients) la valeur de l'achat affichée dans la devise fiat locale.

Dans la vue principale du POS, la devise actuellement affichée est visible sur le côté droit (la valeur par défaut est SAT). Il y a également une liste déroulante d'autres devises disponibles à afficher. Pour ajouter ou supprimer des devises de cette liste déroulante, cliquez sur Point de vente > Préférences > Devises Fiat. Ensuite, cochez simplement les devises que vous souhaitez avoir dans votre menu déroulant et décochez celles que vous souhaitez exclure.

Les valeurs affichées proviennent de yadio, une source respectée de données de taux de change, et elles sont mises à jour en quasi temps réel. Mais n'oubliez pas : quelle que soit la valeur de la devise actuellement affichée, le paiement lui-même est en bitcoin.

### Facturation d'une commande

Pour composer la commande, ajoutez des articles à partir de la liste des articles ou saisissez simplement une somme sur le clavier. Ensuite, cliquez sur Facturer en haut de la vue principale du POS. Vous verrez alors un code QR que le client peut scanner avec son application Lightning, que vous pouvez partager directement depuis une autre application sur votre appareil, ou que vous pouvez copier et coller si nécessaire.

En scannant ce code ou en cliquant sur la facture partagée/collée, le client verra la facture dans son application Lightning et aura la possibilité de la payer et de régler la transaction immédiatement.

Une fois que vous voyez l'animation Paiement approuvé ! dans l'application Breez sur l'appareil du commerçant, vous pouvez cliquer sur l'icône de l'imprimante pour générer un reçu pour le client. Pour utiliser une imprimante de reçus sous Android, essayez d'utiliser ce pilote. Notez que vous pouvez également imprimer des transactions passées via l'écran Transactions.

### Rapport de ventes

Pour consulter un rapport quotidien/hebdomadaire/mensuel de vos ventes (à des fins comptables ou autres), cliquez sur l'icône en haut à gauche, puis cliquez sur Transactions. Cliquez sur l'icône Rapport pour afficher le rapport et sur l'icône Calendrier pour modifier la plage de dates sélectionnée.

### Exportation des transactions

Pour afficher une liste des paiements reçus dans Breez, cliquez sur l'icône en haut à gauche, puis cliquez sur Transactions. Cliquez sur les trois points en haut à droite, puis sur Exporter pour exporter une liste de paiements entrants au format CSV. Pour limiter la liste à une certaine période, cliquez sur l'icône du calendrier pour définir une plage de dates.

### Impression des reçus

Pour imprimer un reçu de vente, cliquez sur l'icône d'impression en haut à droite de la boîte de dialogue de confirmation de paiement. Alternativement, cliquez sur l'icône en haut à gauche, puis cliquez sur Transactions. Localisez la vente à imprimer, ouvrez-la et cliquez sur l'icône d'impression en haut à droite.

> Note : utilisez ce pilote pour imprimer sur une imprimante thermique portable Bluetooth/USB de 58 mm/80 mm.

## Je veux en savoir plus

- Pour plus d'informations sur Lightning et Breez, consultez notre [blog](https://breez.technology/blog).
- Pour plus de conseils techniques sur la façon de tirer le meilleur parti de l'application et d'effectuer des opérations courantes, consultez notre [documentation](https://breez.technology/documentation).
- Si vous êtes bloqué et que vous ne trouvez pas la réponse dans nos documents d'aide, vous pouvez nous trouver sur [Telegram](https://t.me/breez_labs) ou nous envoyer un [email](mailto:support@breez.technology).
- Si vous souhaitez voir des vidéos de démonstration du mode Breez POS en action réalisées par nos fans et utilisateurs, [ici](https://www.youtube.com/watch?v=xxxx) en voici une courte et [ici](https://www.youtube.com/watch?v=xxxx) en voici une plus longue et plus détaillée.

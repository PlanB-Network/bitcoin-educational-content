---
name: Updating BTCPay Server
description: Apply a security update to your BTCPay Server instance and rotate the credentials that matter
---

![cover](assets/cover.webp)

Faire tourner son propre processeur de paiement, c'est aussi être sa propre équipe de sécurité. Quand les mainteneurs de BTCPay Server publient une version de sécurité, personne ne va patcher votre instance à votre place : la mise à jour, sa vérification et la rotation des identifiants qui suit sont votre responsabilité.

Ce tutoriel déroule toute la procédure, quel que soit votre mode de déploiement : vérifier la version en cours d'exécution, appliquer la mise à jour selon votre type d'installation, contrôler qu'elle a bien été prise en compte, puis renouveler les secrets qu'un attaquant a pu capturer pendant que votre instance était vulnérable.

Si vous n'avez pas encore déployé BTCPay Server, commencez par le guide d'installation :

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## La vulnérabilité critique d'août 2026

⚠️ **Alerte de sécurité critique (7 août 2026) :** une vulnérabilité critique affectant BTCPay Server est activement exploitée et peut entraîner une perte de fonds. Mettez immédiatement votre instance à jour en **version 2.4.2** via `Admin Dashboard > Server > Maintenance > Update`, puis vérifiez que le pied de page affiche bien `2.4.2`. Si vous ne pouvez pas mettre à jour tout de suite, éteignez votre BTCPay Server. Une fois la mise à jour effectuée, vous devez également régénérer complètement vos macaroons ainsi que votre `macaroons.db`, régénérer complètement les chaînes d'authentification de tout autre backend Lightning et, si vous avez généré un portefeuille on-chain chaud dans BTCPay Server, déplacer ces fonds et recréer le portefeuille. Les intégrateurs doivent également mettre à jour NBXplorer en version 2.6.10. Source : [notes de version de BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

La version 2.4.2 a été publiée le 7 août 2026. Les notes de version indiquent qu'elle corrige une vulnérabilité critique déjà exploitée, signalée par `brunoerg` et `benthecarman` dans le cadre de l'effort Bitcoin Red Team. Cette même version corrige aussi un contournement de l'authentification à deux facteurs TOTP via l'authentification Basic de l'API Greenfield, et désactive par défaut cette authentification Basic cinq minutes après la création d'un compte.

« Activement exploitée » entraîne deux conséquences :

- **La mise à jour n'est pas optionnelle et ne se planifie pas pour la semaine prochaine.** Une instance non corrigée et accessible depuis internet doit être soit mise à jour, soit éteinte.
- **La mise à jour ne suffit pas à elle seule.** Si votre instance a été compromise avant que vous ne la patchiez, l'attaquant détient peut-être déjà une copie de vos identifiants Lightning et du matériel cryptographique de tout portefeuille chaud généré pour vous par BTCPay Server. Ces secrets restent valides après la mise à jour tant que vous ne les renouvelez pas. La section sur la rotation ci-dessous est celle que l'on saute le plus souvent, et c'est précisément celle qui protège réellement vos fonds.

## Étape 1 — Identifier votre version

Connectez-vous à votre BTCPay Server et regardez le **pied de page de n'importe quelle page** : la version y est affichée. Vous pouvez aussi ouvrir `Admin Dashboard > Server > Maintenance`, qui affiche la version courante et les commandes de mise à jour.

Si votre instance expose l'API Greenfield, `GET /api/v1/server/info` renvoie également la version.

Toute version inférieure à `2.4.2` est vulnérable.

## Étape 2 — Mettre à jour

### Déploiement Docker auto-hébergé (l'installation standard)

Cela couvre le déploiement Docker officiel, c'est-à-dire celui de la documentation BTCPay Server, celui du lanceur en un clic de LunaNode, et la plupart des installations sur VPS.

Le chemin le plus simple passe par l'interface web :

1. Rendez-vous dans `Admin Dashboard > Server > Maintenance`.
2. Cliquez sur **Update**.
3. Attendez que les conteneurs soient téléchargés et redémarrés. L'interface sera indisponible quelques minutes.

Si l'interface web est injoignable, ou si vous préférez suivre les logs, passez par SSH :

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Sur une installation par défaut, `$BTCPAY_BASE_DIRECTORY` vaut `/root`, donc le répertoire est `/root/btcpayserver-docker`. Le script récupère les dernières images, recrée les conteneurs et affiche les versions obtenues.

Le déploiement Docker embarque NBXplorer aux côtés de BTCPay Server : une mise à jour standard porte donc aussi NBXplorer en `2.6.10`, la version recommandée. Si vous faites tourner NBXplorer séparément — cas typique des intégrateurs et des stacks sur mesure — mettez-le à jour explicitement.

### Umbrel

Ouvrez le tableau de bord Umbrel, allez dans l'**App Store**, trouvez BTCPay Server et appliquez la mise à jour si elle est proposée.

⚠️ **Important :** les paquets de l'app store sont reconditionnés par l'équipe Umbrel et peuvent avoir plusieurs heures, voire plusieurs jours de retard sur l'amont. Vérifiez la version dans le pied de page de BTCPay Server après la mise à jour. Si elle est toujours inférieure à `2.4.2`, **arrêtez l'application** depuis le tableau de bord Umbrel et attendez la publication du paquet plutôt que de laisser tourner une instance vulnérable.

Le guide dédié couvre l'application elle-même :

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Même logique : mettez BTCPay Server à jour depuis la marketplace StartOS, puis vérifiez la version dans le pied de page. Si la version packagée n'est pas encore `2.4.2`, arrêtez le service en attendant.

### Hébergement géré ou tiers

Si quelqu'un d'autre exploite votre instance (un hébergeur, une association, le serveur d'un ami), vous avez quand même besoin de la confirmation. Demandez à l'opérateur la version affichée dans le pied de page, et demandez explicitement si la rotation des identifiants décrite ci-dessous a été effectuée. « On a mis à jour » n'est pas la même réponse que « on a régénéré vos macaroons ».

## Étape 3 — Vérifier que la mise à jour a bien été appliquée

Rechargez l'interface de BTCPay Server et lisez la version dans le pied de page. Elle doit afficher `2.4.2` ou une version supérieure.

Ne vous fiez pas au simple fait que la commande de mise à jour se termine sans erreur : sur une machine contrainte, un téléchargement d'image peut échouer silencieusement et laisser tourner le conteneur précédent. Lisez la version, à chaque fois.

## Étape 4 — Renouveler vos identifiants

C'est l'étape qui fait passer de « patché » à « en sécurité ». Comme la vulnérabilité était exploitée avant la publication du correctif, considérez que tous les secrets détenus par votre instance sont potentiellement connus d'un attaquant.

### Lightning : LND

Régénérez les macaroons **et** le fichier `macaroons.db`. Supprimer uniquement les fichiers de macaroons ne suffit pas : LND dérive les macaroons à partir de la clé racine stockée dans `macaroons.db`, donc un attaquant détenant une copie d'un ancien macaroon conserve son accès tant que cette base n'est pas recréée.

La procédure est la suivante : arrêter LND, supprimer `macaroons.db` et les fichiers `*.macaroon` du répertoire réseau (pour mainnet, `data/chain/bitcoin/mainnet/` dans le répertoire de données de LND), puis redémarrer et déverrouiller LND, qui les recrée. Sauvegardez le répertoire au préalable, et réappairez toutes les applications qui utilisaient les anciens macaroons — BTCPay Server lui-même, Zeus, Thunderhub, RTL, Alby, et le moindre script que vous avez écrit.

Si vous exposez également LND sur internet, profitez-en pour revoir son certificat TLS et les identifiants présents dans `lnd.conf`.

### Lightning : autres backends

Tout ce qui s'authentifie auprès de votre nœud avec une chaîne de caractères doit en recevoir une nouvelle :

- **Core Lightning** : régénérez la rune ou les identifiants d'accès utilisés par la connexion.
- **Phoenixd** : changez le mot de passe HTTP.
- **LNbits et équivalents** : révoquez et réémettez les clés admin et invoice.
- **Chaînes de connexion à un nœud distant** stockées dans les paramètres de boutique de BTCPay Server : réécrivez-les avec les nouveaux secrets.

### Portefeuille on-chain chaud généré dans BTCPay Server

Si vous avez laissé BTCPay Server vous générer un portefeuille on-chain — par opposition à la connexion d'un portefeuille matériel ou à l'import d'un xpub dont les clés n'ont jamais touché le serveur — cette seed a vécu sur la machine.

Considérez-la comme brûlée :

1. Créez un nouveau portefeuille, idéalement avec un portefeuille matériel pour que les clés ne se retrouvent plus jamais sur le serveur.
2. Balayez les fonds de l'ancien portefeuille vers le nouveau.
3. Remplacez le schéma de dérivation dans les paramètres de la boutique par celui du nouveau portefeuille.
4. Ne réutilisez jamais l'ancienne seed.

Les configurations en lecture seule (xpub ou portefeuille matériel) n'ont pas besoin de cette étape : les clés privées n'ont jamais été sur le serveur. C'est exactement pour cette raison que le guide d'installation les recommande.

### Comptes et clés d'API BTCPay Server

Tant que vous y êtes :

- Changez les mots de passe de tous les comptes utilisateurs de l'instance.
- Révoquez et réémettez toutes les **clés d'API** Greenfield.
- Réenrôlez l'authentification à deux facteurs, puisque la 2.4.2 corrige un contournement de la 2FA.
- Ouvrez `Admin Dashboard > Server > Users` et vérifiez qu'aucun compte inattendu n'existe.
- Passez en revue les **payouts**, **pull payments** et **remboursements** récents à la recherche d'entrées que vous n'avez pas créées.
- Vérifiez vos webhooks et leurs secrets.

## Étape 5 — Se tenir informé pour la prochaine fois

Une version de sécurité ne protège que les opérateurs qui en entendent parler :

- Surveillez les [releases de BTCPay Server sur GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub peut vous envoyer un e-mail à chaque nouvelle publication d'un dépôt.
- Suivez les canaux d'annonce du projet et le [blog officiel](https://blog.btcpayserver.org/).
- Gardez votre instance sur une version que vous savez mettre à jour rapidement : plus vous accumulez de retard, plus une mise à jour d'urgence devient douloureuse.

L'auto-hébergement vous donne la souveraineté sur vos paiements. Le prix de cette souveraineté, c'est exactement cela : lire les notes de version et être celui qui patche.

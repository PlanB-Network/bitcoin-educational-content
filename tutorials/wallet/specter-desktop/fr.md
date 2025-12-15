---
name: Specter Desktop
description: Gérez vos portefeuilles Bitcoin multisignatures en toute souveraineté avec votre propre nœud
---

![cover](assets/cover.webp)

Specter Desktop est une application open source (licence MIT) développée par Cryptoadvance depuis 2019 qui facilite la gestion de portefeuilles Bitcoin avec vos hardware wallets (Ledger, Trezor, Coldcard, BitBox02, Passport, etc.) et votre propre infrastructure Bitcoin (nœud Bitcoin Core ou serveur Electrum). L'application excelle particulièrement dans les configurations multisignatures, permettant de sécuriser des montants importants en répartissant le pouvoir de signature entre plusieurs hardware wallets indépendants.

**Dans ce tutoriel, vous apprendrez à :**
- Installer et configurer Specter Desktop sur votre ordinateur (Windows, macOS ou Linux)
- Connecter Specter à un serveur Electrum (nous utiliserons Umbrel dans cet exemple)
- Créer un portefeuille simple avec un hardware wallet (Coldcard)
- Recevoir et envoyer des bitcoins en toute souveraineté
- Configurer un portefeuille multisignature 2-sur-3 avec plusieurs hardware wallets
- Installer Specter sur un serveur Umbrel (bonus avancé)

Toutes vos transactions seront validées localement via votre propre infrastructure, sans transmettre d'informations à des serveurs externes, garantissant ainsi votre confidentialité et votre souveraineté financière. Vérifiez toujours les transactions sur l'écran de votre hardware wallet avant de signer.

## Téléchargement et installation

Rendez-vous sur le site officiel de Specter Desktop pour télécharger l'application.

![Page d'accueil Specter](assets/fr/01.webp)

Sur la page de téléchargement, choisissez la version correspondant à votre système d'exploitation : macOS, Windows ou Linux.

![Téléchargement selon l'OS](assets/fr/02.webp)

Une fois téléchargé, installez l'application selon les instructions habituelles de votre système d'exploitation. Pour macOS, glissez l'icône dans Applications. Pour Windows, exécutez l'installeur. Pour Linux, suivez les instructions du package.

## Configuration initiale

Au premier lancement, Specter Desktop vous demande de choisir votre type de connexion. Vous pouvez vous connecter à un serveur Electrum ou à votre propre nœud Bitcoin Core.

![Choix du type de connexion](assets/fr/03.webp)

Dans cet exemple, nous utiliserons une connexion à un serveur Electrum tournant sur Umbrel. 

N'hésitez pas à vous référer à notre tutoriel Umbrel si vous souhaitez avoir plus d'information à ce sujet : 

https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Cette option offre une synchronisation plus rapide qu'avec Bitcoin Core. Si vous préférez, vous pouvez sélectionner "Bitcoin Core" et configurer la connexion à votre nœud local. Les étapes suivantes restent identiques quel que soit votre choix.

Sélectionnez "Electrum Connection" puis choisissez "Enter my own" pour configurer votre propre serveur Electrum.

![Configuration Electrum](assets/fr/04.webp)

Renseignez l'adresse de votre serveur Electrum. Dans notre cas avec Umbrel, l'adresse sera `umbrel.local` avec le port `50001`. Cliquez sur "Connect" pour établir la connexion.

Une fois connecté, l'écran de bienvenue s'affiche avec une checklist pour démarrer. Vous devez maintenant ajouter vos hardware wallets.

![Écran d'accueil](assets/fr/05.webp)

## Ajout d'un hardware wallet

Dans le menu de gauche, cliquez sur "Add device" pour ajouter votre hardware wallet.

Specter Desktop supporte de nombreux hardware wallets : Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault, et bien d'autres.

N’hésitez pas à consulter nos tutoriels dédiés aux différents hardware wallets si vous souhaitez en apprendre davantage.

![Sélection du type de hardware wallet](assets/fr/06.webp)

Sélectionnez votre hardware wallet. Dans cet exemple, nous utilisons un Coldcard MK4. 

Vous trouverez ci-dessous notre tutoriel concernant ce hardware wallet : 

https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Pour un Coldcard, vous devez exporter les clés publiques depuis le hardware wallet soit avec une connexion USB soit via une carte microSD.

![Import des clés du Coldcard](assets/fr/07.webp)

Suivez les instructions affichées pour exporter les clés depuis votre Coldcard. Donnez un nom à votre hardware wallet (ici "MK4 Tuto"). Une fois les clés importées, vous pouvez créer un portefeuille avec une seule clé ou ajouter d'autres hardware wallets pour un portefeuille multisignature.

![Dispositif ajouté](assets/fr/08.webp)

## Création d'un portefeuille

Après avoir ajouté votre hardware wallet, cliquez sur "Create single key wallet" pour créer un portefeuille à signature unique.

Donnez un nom à votre portefeuille (par exemple "Wallet for tuto") et choisissez le type d'adresses. Sélectionnez "Segwit" pour utiliser des adresses bech32 natives qui optimisent les frais de transaction.

![Configuration du portefeuille](assets/fr/09.webp)

Une fois le portefeuille créé, Specter vous propose de sauvegarder un fichier PDF de backup contenant toutes les informations publiques nécessaires pour restaurer votre portefeuille (descripteurs, clés publiques étendues). Ce fichier ne contient pas vos clés privées.

![Sauvegarde du portefeuille](assets/fr/10.webp)

## Recevoir des bitcoins

Pour recevoir des bitcoins, sélectionnez votre portefeuille dans le menu de gauche, puis cliquez sur l'onglet "Receive".

Specter génère automatiquement une nouvelle adresse de réception avec un QR code.

![Génération d'une adresse de réception](assets/fr/11.webp)

Vous pouvez copier l'adresse ou scanner le QR code. Vérifiez toujours l'adresse sur l'écran de votre hardware wallet avant de la communiquer à quelqu'un.

## Consulter l'historique et les adresses

Une fois que vous avez reçu des bitcoins, vous pouvez consulter vos transactions dans l'onglet "Transactions".

![Historique des transactions](assets/fr/12.webp)

L'onglet "Addresses" vous permet de voir toutes les adresses générées par votre portefeuille, avec leur statut d'utilisation et les montants associés.

![Liste des adresses](assets/fr/13.webp)

## Envoyer des bitcoins

Pour envoyer des bitcoins, cliquez sur l'onglet "Send". Renseignez l'adresse du destinataire, le montant à envoyer, et vérifiez les options avancées si vous souhaitez sélectionner manuellement les UTXOs (coin control).

![Création d'une transaction](assets/fr/14.webp)

Cliquez sur "Create Unsigned Transaction" pour construire la transaction. Specter va ensuite vous demander de signer la transaction avec votre hardware wallet.

![Signature de la transaction](assets/fr/15.webp)

Si vous utilisez un Coldcard, vous aurez le choix entre signer via USB ou utiliser la carte microSD (air-gapped). Confirmez la transaction sur l'écran de votre hardware wallet en vérifiant soigneusement l'adresse de destination et le montant.

Une fois la transaction signée, vous pouvez la diffuser sur le réseau Bitcoin.

![Options de diffusion](assets/fr/16.webp)

Cliquez sur "Send transaction" pour diffuser la transaction. Specter confirmera que votre transaction a été envoyée et vous pourrez suivre son statut dans l'onglet Transactions.

![Diffusion de la transaction](assets/fr/17.webp)

## Création et usage d'un portefeuille multisignature

L'un des atouts majeurs de Specter Desktop réside dans sa capacité à simplifier la gestion des portefeuilles multisignatures. Un portefeuille multisig nécessite plusieurs signatures pour autoriser une transaction, éliminant ainsi le point de défaillance unique. Une configuration 2-sur-3, par exemple, exige deux signatures parmi trois hardware wallets distincts pour valider toute dépense.

Pour créer un portefeuille multisig, commencez par ajouter tous les hardware wallets signataires via "Add device". Dans cet exemple, nous utiliserons trois hardware wallets différents : un Coldcard MK4 (déjà ajouté précédemment), un Passport et un Ledger. Cette diversification des fabricants renforce la sécurité en évitant de dépendre d'une seule chaîne d'approvisionnement ou d'un seul firmware.

Voici les liens des tutoriels concernant le Ledger et le Passport : 

https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Ajoutez le Passport en nommant le hardware wallet (par exemple "Passport multi") et en important ses clés via carte microSD ou QR code. Puis cliquez sur "Continue" pour passer à la suite.

![Ajout du Passport](assets/fr/23.webp)

Ajoutez ensuite le Ledger en le connectant via USB et en ouvrant l'application Bitcoin sur le hardware wallet. Nommez-le (par exemple "ledger multi") et cliquez sur "Get via USB" puis "Continue" pour importer ses clés publiques.

![Ajout du Ledger](assets/fr/24.webp)

Une fois vos trois hardware wallets enregistrés dans Specter, cliquez sur "Add wallet" et sélectionnez l'option "Multiple Signature" pour créer un portefeuille multisignature.

![Choix du type de wallet](assets/fr/25.webp)

Sélectionnez les trois hardware wallets que vous souhaitez inclure dans votre quorum multisignature : MK4 Tuto, Passport multi et ledger multi. Cliquez sur "Continue" pour passer à l'étape suivante.

![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)

Choisissez votre configuration multisignature. Sélectionnez "Segwit" comme type d'adresse pour bénéficier des frais optimisés. Le paramètre "Required Signatures to Authorize Transactions (m of 3)" vous permet de définir le seuil : pour une configuration 2-sur-3, il faudra 2 signatures. Chaque hardware wallet affiche sa clé multisig correspondante. Cliquez sur "Create wallet" pour finaliser la création.

![Configuration 2-sur-3 Segwit](assets/fr/27.webp)

Votre portefeuille multisignature "Multi tuto" est maintenant créé. Specter vous recommande immédiatement de sauvegarder le fichier PDF de backup contenant le descripteur du portefeuille. Cliquez sur "Save Backup PDF" pour télécharger ce fichier critique.

![Wallet multisig créé](assets/fr/28.webp)

Specter vous propose également d'exporter les informations du wallet vers chacun de vos hardware wallets via QR code ou fichier. Cela permet à certains hardware wallets (comme Coldcard ou Passport) de stocker la configuration multisig directement dans leur mémoire.

Pour le Passport, déverrouillez votre appareil puis allez dans "Manage Account" > "Connect Wallet" > "Specter" > "Multisig" > "QR Code", puis scannez le QR code généré par Specter. Votre Passport vous demandera alors de scanner une adresse de réception de votre portefeuille pour valider la configuration du multisig. 

Pour le MK4, branchez-le à votre PC et déverrouillez-le. Ensuite vous pouvez cliquer sur "Save MK4 Tuto file" et enregistrer le fichier dans votre MK4. Lors de la prochaine signature avec votre hardware wallet, le MK4 utilisera ce fichier pour finir la configuration du multisig. 

![Export vers les hardware wallets](assets/fr/29.webp)

Pour information, vous pouvez accéder à tout moment aux backups depuis l'onglet "Settings" de votre portefeuille, puis "Export" :

![Accès au backup PDF](assets/fr/30.webp)

L'utilisation quotidienne reste similaire à un portefeuille simple : vous générez des adresses de réception normalement. Pour envoyer des bitcoins, accédez à l'onglet "Send", renseignez l'adresse du destinataire et le montant, puis cliquez sur "Create Unsigned Transaction".

![Création d'une transaction multisig](assets/fr/31.webp)

Specter construit une PSBT (Partially Signed Bitcoin Transaction) et affiche "Acquired 0 of 2 signatures". Vous devez maintenant signer avec au moins deux de vos trois hardware wallets. Cliquez sur le premier hardware wallet (par exemple "MK4 Tuto") pour signer avec votre Coldcard, puis sur le second (par exemple "Passport multi") pour obtenir la deuxième signature requise.

![Signature de la transaction](assets/fr/32.webp)

Une fois que vous avez obtenu les 2 signatures requises (l'interface affiche "Acquired 2 of 2 signatures" et "Transaction is ready to send"), cliquez sur "Send Transaction" pour diffuser la transaction sur le réseau Bitcoin.

![Transaction prête à être diffusée](assets/fr/33.webp)

Cette approche multisignature convient particulièrement aux entreprises (plusieurs dirigeants doivent approuver les dépenses), aux familles (protection d'un héritage multigénérationnel), ou aux particuliers gérant des montants importants (distribution géographique des hardware wallets pour résister aux catastrophes localisées).

### L'importance critique des backups multisignature

**Attention** : la sauvegarde d'un portefeuille multisignature diffère fondamentalement d'un portefeuille simple. Vos phrases de récupération (seed phrases) ne suffisent pas à elles seules pour restaurer un portefeuille multisig. Vous devez impérativement sauvegarder le **descripteur de sortie** (output descriptor), qui contient les informations de configuration de votre portefeuille multisignature.

Le descripteur de sortie inclut des données essentielles : les clés publiques étendues (xpubs) de chaque cosignataire, le seuil de signatures (2-sur-3 dans notre exemple), le type de script utilisé (Segwit natif, nested ou legacy), et les chemins de dérivation pour chaque hardware wallet. Sans ce descripteur, même si vous possédez deux de vos trois phrases de récupération, vous ne pourrez pas reconstruire votre portefeuille ni accéder à vos bitcoins. Le descripteur permet à votre logiciel de savoir comment combiner les clés publiques pour générer les adresses Bitcoin correspondant à vos fonds.

Specter Desktop génère automatiquement un fichier PDF de backup lors de la création de votre portefeuille multisig. Ce PDF contient le descripteur complet, les fingerprints de chaque hardware wallet, et toutes les informations publiques nécessaires à la restauration. **Ce fichier ne contient pas vos clés privées** et ne permet donc pas à lui seul de dépenser vos bitcoins, mais il permet à quiconque y accède de voir l'historique complet de vos transactions et votre solde.

Pour sauvegarder correctement votre configuration multisignature, suivez cette procédure : après avoir créé votre portefeuille, cliquez sur l'onglet "Settings" puis "Export" et sélectionnez "Save Backup PDF". Créez plusieurs copies de ce PDF : imprimez-en au moins deux exemplaires sur papier, et conservez également une copie numérique chiffrée. Stockez une copie du PDF avec chacune de vos phrases de récupération, dans des endroits géographiquement distincts.

Gravez vos phrases de récupération sur des plaques métalliques résistantes au feu et à l'eau pour garantir leur pérennité. Ne sous-estimez jamais l'importance de ces backups : si vous perdez le dossier `~/.specter` de votre ordinateur ET que vous perdez un de vos hardware wallets sans backup du descripteur, tous vos fonds seront irrémédiablement perdus, même avec une configuration 2-sur-3. La redondance multisignature protège contre la perte d'un hardware wallet, mais uniquement si vous avez correctement sauvegardé le descripteur de votre portefeuille.

## Avantages et limitations de Specter Desktop

**Avantages** : Confidentialité optimale avec validation locale complète sans serveurs tiers. Flexibilité multisignature rendant accessibles des configurations avancées (entreprises, familles, particuliers). Support étendu des hardware wallets avec interopérabilité totale (USB et air-gapped).

**Limitations** : Courbe d'apprentissage significative sur les concepts Bitcoin avancés (UTXOs, descripteurs, chemins de dérivation).

## Bonnes pratiques

Vérifiez toujours adresses et montants sur l'écran de vos hardware wallets avant validation pour vous protéger contre les malwares.

Conservez les sauvegardes PDF séparément de vos seeds. Ces descripteurs publics peuvent être stockés dans un coffre bancaire ou dans un cloud chiffré, facilitant la récupération sans exposer vos clés privées.

Testez la récupération sur des montants symboliques avant d'utiliser vos portefeuilles avec des fonds importants. Créez, testez, effacez et restaurez pour valider vos procédures.

Maintenez Specter et vos firmwares à jour. Distribuez géographiquement vos cosignataires multisignatures (domicile/bureau/proche) pour résister aux catastrophes localisées. Utilisez des étiquettes descriptives pour faciliter comptabilité et déclarations fiscales.

## Bonus : Installation sur un serveur Bitcoin (Umbrel, RaspiBlitz, Start9)

Si vous possédez déjà un serveur Bitcoin comme Umbrel, RaspiBlitz, MyNode ou Start9, vous pouvez installer Specter Desktop directement depuis leur boutique d'applications. Cette approche offre plusieurs avantages significatifs : l'application se configure automatiquement avec votre nœud Bitcoin Core local, elle reste accessible 24/7 via une interface web depuis n'importe quel appareil de votre réseau, et vous pouvez même y accéder à distance de manière sécurisée via Tor. Toute votre infrastructure Bitcoin est centralisée sur un seul serveur dédié, simplifiant la gestion et renforçant votre souveraineté.

### Installation depuis l'App Store Umbrel

Depuis l'interface de votre Umbrel, accédez à l'App Store et recherchez Specter Desktop. Cliquez sur "Install" pour lancer l'installation.

![App Store Umbrel - Specter Desktop](assets/fr/18.webp)

Une fois l'installation terminée, ouvrez Specter Desktop sur votre Umbrel. L'écran de bienvenue vous propose de choisir votre type de connexion. Si vous utilisez Specter sur Umbrel, cliquez sur "Update settings" pour configurer la connexion.

![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)

Sélectionnez "Remote Specter USB connection" pour permettre l'utilisation de hardware wallets USB connectés à votre ordinateur local tout en utilisant Specter sur le serveur Umbrel distant.

![Configuration Remote Specter USB](assets/fr/20.webp)

Suivez les instructions affichées pour configurer le HWI Bridge. Vous devez accéder aux paramètres du device bridge et ajouter le domaine `http://umbrel.local:25441` à la liste blanche (whitelist). Cliquez sur "Update" pour enregistrer la configuration.

![HWI Bridge Settings](assets/fr/21.webp)

Si vous souhaitez également utiliser vos hardware wallets USB depuis votre ordinateur local, téléchargez l'application Specter Desktop sur votre machine et configurez-la en mode "Yes, I run Specter remotely". Cliquez sur "Save" pour finaliser la configuration.

![Configuration connexion remote dans l'app](assets/fr/22.webp)

## Conclusion

Specter Desktop démocratise les configurations Bitcoin avancées en rendant le multisignature accessible sans sacrifier ni votre souveraineté ni votre confidentialité. Pour les utilisateurs gérant des montants significatifs, il transforme des pratiques institutionnelles en solutions déployables par des particuliers.

Bien que l'application exige un investissement initial en infrastructure et en apprentissage, elle offre une souveraineté complète : contrôle de l'infrastructure de validation, détention physique des clés, et transactions libres de toute surveillance tierce. Que vous soyez un particulier sécurisant son épargne, une famille créant un coffre multigénérationnel, ou une entreprise gérant une trésorerie, Specter Desktop constitue l'outil de référence pour concilier sécurité maximale et souveraineté absolue.

## Ressources

### Documentation officielle
- [Site officiel Specter Desktop](https://specter.solutions/desktop/)
- [Code source GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Documentation complète](https://docs.specter.solutions/)

### Communauté et support
- [Groupe Telegram Specter Community](https://t.me/spectersupport)
- [Forum de discussion Reddit](https://reddit.com/r/specterdesktop/)
- [Signalement de bugs GitHub](https://github.com/cryptoadvance/specter-desktop/issues)
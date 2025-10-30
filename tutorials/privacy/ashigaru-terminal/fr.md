---
name: Ashigaru Terminal
description: Utiliser Ashigaru sur desktop pour faire des coinjoins
---

![cover](assets/cover.webp)

Ashigaru Terminal est l'adaptation de Sparrow Server par les équipes d'Ashigaru qui implémente le protocole de coinjoin Whirlpool. Ce logiciel s’inscrit dans la continuité du travail amorcé par Samourai Wallet, notamment sur Whirlpool GUI, dont il reprend les principes fondamentaux : la self-custody et la préservation de la confidentialité. 

Ce logiciel est donc un fork de Sparrow Server, modifié et optimisé pour une intégration complète avec l’écosystème Whirlpool, le protocole de coinjoin ZeroLink initialement développé par les équipes de Samourai.

Ashigaru Terminal fonctionne depuis une interface TUI minimaliste et peut être déployé sur un ordinateur personnel ou sur un serveur dédié. Il permet d’interagir directement avec Whirlpool pour initier des "*Tx0*", gérer les comptes "*Deposit*", "*Premix*", "*Postmix*" et "*Badbank*", et effectuer des remixages automatiques afin de renforcer la confidentialité de vos pièces.

En résumé, Ashigaru Terminal vous sera particulièrement utile si vous souhaitez réaliser des coinjoins via Whirlpool.

Dans ce premier tutoriel, je vais vous accompagner dans l’installation et la prise en main d’Ashigaru Terminal. Un second tutoriel, plus avancé, sera ensuite consacré à la réalisation concrète de coinjoins.

## 1. Installer Ashigaru Terminal

Pour installer Ashigaru Terminal, vous aurez besoin de Tor Browser, car les binaires ne sont distribués que via le réseau Tor. Si ce n’est pas déjà fait, [installez-le sur votre machine](https://www.torproject.org/download/).

### 1.1. Télécharger Ashigaru Terminal

Depuis Tor Browser, rendez-vous sur [la page des releases de leur dépôt Git](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) afin de télécharger la dernière version d’Ashigaru Terminal correspondant à votre système d’exploitation.

```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```

![Image](assets/fr/01.webp)

Téléchargez les 2 fichiers suivants correspondant à votre système d’exploitation :
- Le binaire (`ashigaru_terminal_v1.0.0_amd64.deb` pour Debian/Ubuntu, `.dmg` pour macOS ou `.zip` pour Windows) ;
- Le fichier des hachages signés : `ashigaru_terminal_v1.0.0_signed_hashes.txt`.

### 1.2. Vérifier Ashigaru Terminal

Avant d’exécuter le logiciel sur votre appareil, il faut vérifier son authenticité et son intégrité. Cette étape est importante, car elle permet d'éviter d’installer une version frauduleuse susceptible de compromettre vos bitcoins ou d’infecter votre machine.

Ouvrez un nouvel onglet dans un navigateur et accédez à [l’outil de vérification Keybase](https://keybase.io/verify). Collez dans le champ prévu le contenu du fichier `.txt` que vous venez de télécharger, puis cliquez sur le bouton `Verify`.

![Image](assets/fr/02.webp)

Pour diversifier vos sources de vérification, vous pouvez également comparer le message avec celui disponible sur le site clearnet [ashigaru.rs](https://ashigaru.rs/download/), dans la section `/download`.

![Image](assets/fr/03.webp)

Si la signature est valide, Keybase affichera un message confirmant que le fichier a bien été signé par les développeurs d’Ashigaru.

![Image](assets/fr/04.webp)

Vous pouvez aussi cliquer sur le profil `ashigarudev` affiché par Keybase et vérifier que l’empreinte de leur clé correspond exactement à : `A138 06B1 FA2A 676B`.

![Image](assets/fr/05.webp)

Si une erreur apparaît à cette étape, cela signifie que la signature n’est pas valide. Dans ce cas, **n’installez surtout pas le logiciel téléchargé**. Reprenez la procédure depuis le début ou demandez de l’aide à la communauté avant de continuer.

Keybase vous a fourni le hachage authentifié de l’application. Nous allons maintenant vérifier que le hachage du fichier `.deb`, `.zip` ou `.dmg` que vous avez téléchargé correspond bien à celui validé sur Keybase. Pour cela, rendez-vous sur le site [HASH FILE ONLINE](https://hash-file.online/).

Cliquez sur le bouton `BROWSE...` et sélectionnez le fichier `.deb`, `.zip` ou `.dmg` téléchargé à l’étape 1.1. Choisissez ensuite la fonction de hachage `SHA-256`, puis cliquez sur `CALCULATE HASH` pour générer le hachage de votre fichier.

![Image](assets/fr/06.webp)

Le site affichera alors le hachage du logiciel. Comparez-le à celui que vous avez vérifié sur Keybase.io. Si les deux correspondent parfaitement, la vérification d’authenticité et d’intégrité est réussie. Vous pouvez alors utiliser ce logiciel.

![Image](assets/fr/07.webp)

### 1.3 Lancer Ashigaru Terminal

- **Debian / Ubuntu**

Pour installer le logiciel, exécutez la commande :

```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```

Modifiez la commande en fonction de la version téléchargée.

Vérifiez ensuite l’installation :

```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```

Puis lancez le logiciel :

```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```

- **Windows**

Faites un clic droit sur le fichier `.zip` que vous avez téléchargé et vérifié, puis sélectionnez `Extract All...` pour extraire son contenu.

Une fois l’extraction terminée, double-cliquez sur le fichier `Ashigaru-terminal.exe` afin de lancer le logiciel.

![Image](assets/fr/08.webp)

## 2. Prendre en main Ashigaru Terminal

Ashigaru Terminal est un logiciel en TUI (*Text-based User Interface*), c’est-à-dire une interface minimaliste fonctionnant directement dans le terminal. Vous y interagissez à l’aide de menus et de raccourcis clavier, mais sans véritable environnement graphique classique.

![Image](assets/fr/09.webp)

Son utilisation est assez simple : utilisez les flèches directionnelles de votre clavier pour naviguer dans les menus, et appuyez sur la touche `Enter` pour valider une action ou confirmer un choix.

## 3. Connecter son nœud à Ashigaru Terminal

Par défaut, Ashigaru Terminal se connecte à un serveur Electrum public. Cela présente évidemment des risques en matière de confidentialité et de souveraineté. Nous allons donc le configurer pour qu’il se connecte directement à votre propre Electrum Server.

Pour ce faire, ouvrez le menu `Preferences > Server`.

![Image](assets/fr/10.webp)

Cliquez sur le bouton `< Edit >`.

![Image](assets/fr/11.webp)

Sélectionnez `Private Electrum Server`, puis cliquez sur `<Continue>`.

![Image](assets/fr/12.webp)

Saisissez l’URL et le port de votre serveur. Vous pouvez indiquer une adresse Tor en `.onion`. Cliquez ensuite sur `< Test >` pour vérifier la connexion.

![Image](assets/fr/13.webp)

Si la connexion est réussie, le message `Success` apparaîtra, accompagné des détails de votre serveur.

![Image](assets/fr/14.webp)

Si vous n'avez pas encore de nœud Bitcoin, je vous conseille de suivre cette formation :

https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*Dans mon cas, pour ce tutoriel, je vais me déconnecter de mon serveur Electrs car je travaille sur testnet. Le fonctionnement reste néanmoins strictement identique sur mainnet.*

## 4. Créer un portefeuille sur Ashigaru Terminal

Maintenant que le logiciel est correctement configuré, nous allons pouvoir y ajouter un portefeuille Bitcoin.

Deux possibilités s’offrent à vous :
- Vous pouvez créer un nouveau portefeuille à partir de zéro et l’utiliser exclusivement sur Ashigaru Terminal. Dans ce cas, vous devrez ouvrir ce logiciel à chaque fois que vous souhaitez interagir avec votre portefeuille ;
- Ou bien, vous pouvez importer directement votre portefeuille Ashigaru existant depuis votre téléphone vers Ashigaru Terminal. L’inconvénient de cette méthode est qu’elle réduit légèrement la sécurité de votre configuration, car votre portefeuille est alors exposé à deux environnements à risque au lieu d’un seul. En revanche, elle offre l’avantage de pouvoir laisser Ashigaru Terminal fonctionner en continu pour mixer vos pièces, tout en vous permettant de les dépenser à distance via l’application mobile Ashigaru.

Dans ce tutoriel, nous allons opter pour la seconde méthode. Toutefois, si vous préférez créer un portefeuille entièrement nouveau, la procédure reste identique : la seule différence interviendra lors de la création, où vous devrez sauvegarder votre nouvelle phrase mnémonique et votre nouvelle passphrase.

Notez également qu’Ashigaru Terminal ne permet pas de dépenser directement vos bitcoins. Vous pouvez soit synchroniser le même portefeuille sur Ashigaru Terminal et sur l’application Ashigaru (ce que je vais faire dans ce tutoriel), soit utiliser l’option `Mix to` (que nous verrons dans le prochain tutoriel) afin d’envoyer automatiquement vos fonds vers un hardware wallet après un nombre défini de cycles de mixage.

Si vous n’avez pas encore de portefeuille sur l’application Ashigaru, vous pouvez suivre le tutoriel dédié :

https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Rendez-vous dans le menu `Wallets`.

![Image](assets/fr/15.webp)

Sélectionnez ensuite `Create / restore wallet...`. L’option `Open Wallet...` vous permettra d’accéder ultérieurement à un portefeuille déjà enregistré dans Ashigaru Terminal.

![Image](assets/fr/16.webp)

Attribuez un nom à votre portefeuille.

![Image](assets/fr/17.webp)

Choisissez ensuite le type de portefeuille `Hot Wallet`.

*Remarque* : l’option `Watch-only` permet d’enregistrer la `xpub` d’un hardware wallet afin d’utiliser ultérieurement la fonction `Mix to`. Toutefois, ce type de portefeuille ne peut évidemment pas participer à des coinjoins. Nous reviendrons en détail sur cette fonctionnalité dans le prochain tutoriel.

![Image](assets/fr/18.webp)

C’est à cette étape que la procédure diffère en fonction de votre choix initial :
- Si vous souhaitez créer un nouveau portefeuille à partir de zéro, cliquez sur `<Generate New Wallet>`, définissez une passphrase BIP39, puis sauvegardez soigneusement votre phrase mnémonique et votre passphrase sur un support physique ;

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

- Si vous souhaitez utiliser le même portefeuille que votre application Ashigaru, saisissez directement les 12 mots de votre phrase mnémonique ainsi que votre passphrase BIP39 dans les champs correspondants. Écrivez les mots en minuscules, entiers, dans l'ordre, séparés par un espace, sans chiffre ni caractère supplémentaire.

Une fois cette étape terminée, cliquez sur `< Next >`.

*Remarque* : Si vous ne parvenez pas à cliquer sur ce bouton, cela signifie que votre phrase mnémonique est invalide. Vérifiez attentivement qu’aucun mot n’est incorrect ou mal orthographié.

![Image](assets/fr/19.webp)

Vous devrez ensuite définir un mot de passe. Celui-ci servira à déverrouiller votre portefeuille sur Ashigaru Terminal et à le protéger contre tout accès physique non autorisé. Il n’intervient pas dans la dérivation cryptographique de vos clés : autrement dit, même sans ce mot de passe, toute personne disposant de votre phrase mnémonique et de votre passphrase pourra restaurer votre portefeuille et accéder à vos bitcoins.

Choisissez un mot de passe long, complexe et aléatoire. Conservez-en une copie en lieu sûr : idéalement sur un support physique ou dans un gestionnaire de mots de passe sécurisé.

Cliquez sur `< OK >` lorsque vous avez terminé.

![Image](assets/fr/20.webp)

## 5. Utiliser le portefeuille

Vous pouvez ensuite choisir quel compte consulter. Pour l’instant, nous n’avons encore initié aucun mix, nous allons donc accéder au compte `Deposit`.

![Image](assets/fr/21.webp)

Le fonctionnement est ensuite identique à celui de Sparrow, puisque Ashigaru Terminal est un fork de Sparrow Server. Vous retrouverez donc les mêmes menus :

![Image](assets/fr/22.webp)

- `Transactions` : permet de consulter l’historique des transactions liées à ce compte. Dans mon cas, certaines apparaissent déjà, car j’en avais effectuées avec l’application Ashigaru sur ce même portefeuille.

![Image](assets/fr/23.webp)

- `Receive` : génère une nouvelle adresse de réception vierge pour mettre des sats sur le compte de dépôt.

![Image](assets/fr/24.webp)

- `Addresses` : affiche la liste de toutes vos adresses, qu’elles appartiennent à la chaîne interne ou externe de votre compte.

![Image](assets/fr/25.webp)

- `UTXOs` : répertorie l’ensemble de vos UTXOs disponibles.

![Image](assets/fr/26.webp)

- `Settings` : donne accès au *descriptor* de votre portefeuille. Vous pouvez également y consulter votre seed, ajuster le *Gap Limit* ou encore modifier la date de création de votre portefeuille.

![Image](assets/fr/27.webp)

Vous savez désormais comment installer et prendre en main Ashigaru Terminal. Dans le prochain tutoriel, nous verrons comment réaliser des coinjoins avec ce logiciel et comment gérer les fonds en "*Postmix*", soit via l’application Ashigaru, soit grâce à l’option `Mix to`.


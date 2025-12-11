---
name: Jade - Electrum
description: Comment utiliser votre Jade ou Jade Plus avec Electrum (bureau)
---

![cover](assets/cover.webp)



ce guide est extrait d'une [leçon des ateliers Bitcoin] (https://officinebitcoin.it/lezioni/jadeele/index.html)



Le tutoriel est réalisé avec Jade Classic, mais les opérations sont également valables pour ceux qui ont Jade Plus.



Après avoir initialisé Jade, vous pouvez commencer à l'utiliser et, pour ce faire, choisir un écran wallet.



Jade est un appareil qui peut être utilisé avec plusieurs wallet, ou applications compagnons, comme Blockstream le précise sur son site.



Dans ce tutoriel, vous verrez les étapes d'utilisation du Electrum Wallet, via une connexion par câble USB.



## Transfert de la clé publique



Prenez et allumez votre Jade initialisée. Dès que vous l'allumez, il ressemble à ceci :




![img](assets/en/32.webp)



Si vous sélectionnez _Déverrouiller Jade_, vous obtiendrez un menu dans lequel vous devrez choisir comment connecter votre appareil à l'application compagnon.



Avec le Electrum, vous ne pouvez connecter Jade que par USB, choisissez donc cette méthode.



Lancer Electrum, qui s'ouvrira en proposant par défaut d'ouvrir le dernier wallet utilisé.



Si c'est la première fois que vous connectez Jade à Electrum, sélectionnez _Create New Wallet_ (Créer un nouveau portefeuille) puis _Finish_ (Terminer).



![img](assets/en/34.webp)



Nom wallet.



![img](assets/en/35.webp)



Sélectionnez la norme Wallet.



![img](assets/en/36.webp)



Lors du choix du keystore, il est essentiel de sélectionner _Use a hardware device_.



![img](assets/en/37.webp)



Le Electrum commence à rechercher le dispositif matériel.



![img](assets/en/38.webp)



En connectant le port USB à l'ordinateur (déjà connecté du côté USB C à Jade), le matériel wallet apparaît en mode verrouillage. Jade se déverrouille en entrant le code PIN à six chiffres défini lors de la configuration.




![img](assets/en/39.webp)



Dispositif matériel déverrouillé, Electrum détecte Jade. Continuez en cliquant sur _Suivant_.



![img](assets/en/40.webp)



A ce stade, Electrum vous demande de définir le script de politique : choisissez _Native Segwit_.



![img](assets/en/41.webp)



La phase de transfert de la clé publique de wallet de Jade à l'affichage de Electrum commence.



Lorsque l'exportation de la clé publique est terminée, le processus est achevé.



La montre seule est prête et Electrum vous avertit de l'achèvement de l'opération en affichant l'écran suivant.



![img](assets/en/42.webp)



wallet est effectivement créé et vous pouvez commencer à l'explorer : vous pouvez voir les _adresses_, les _informations sur le portefeuille_ et, surtout, vous pouvez voir dans le coin inférieur droit l'indication qu'il s'agit du dispositif de Blockstream. Le point vert à côté du logo Blockstream indique que l'appareil est allumé et correctement connecté au réseau local.



![img](assets/en/43.webp)



## Recevoir et dépenser des transactions



Dans le menu _Receive_ de Electrum, generate une `scriptPubKey` (adresse) pour recevoir des fonds. Commencez toujours par un petit montant et faites un test de réception et de dépense.



![img](assets/en/44.webp)



Après avoir reçu des sats, vous pouvez vérifier leur arrivée dans le menu _Histoire_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Une fois la transaction confirmée, vous pouvez dépenser cette UTXO et terminer le test.



La dépense consiste à utiliser Jade pour signer.



Allez dans le menu _Send_ de Electrum, collez un scriptPubKey, et vérifiez-le bien.



![img](assets/en/47.webp)



Lorsque vous avez terminé, appuyez sur _Pay_.



La fenêtre de transaction s'ouvre, dans laquelle il est important de définir les frais de transaction corrects. Lorsque vous avez terminé tous les réglages, cliquez sur _Preview_ dans le coin inférieur droit.



![img](assets/en/48.webp)



La fenêtre de transaction affiche quelques détails importants, en premier lieu le statut : `Unsigned`.



À ce stade, vous pouvez également voir la commande _Sign_, sur laquelle vous devez cliquer pour apposer la signature avec Jade.



![img](assets/en/49.webp)



Commence alors une phase de communication entre l'afficheur wallet et le dispositif matériel, au cours de laquelle Electrum vous avertit de suivre les instructions sur le dispositif matériel, allumé et prêt à signer.



![img](assets/en/50.webp)



**Mais avant tout, il est préférable de vérifier ce que vous signez : tous les paramètres de la transaction que vous venez d'établir apparaissent également sur Jade** et vous pouvez tous les vérifier.



![img](assets/en/51.webp)



Pour continuer, veillez à toujours placer le curseur sur la flèche `→` qui mène aux étapes suivantes et jamais sur le ``X` sauf si vous voulez terminer l'opération sans l'avoir achevée.



La partie vérification se termine par l'affichage de la redevance. À ce stade, la confirmation équivaut à l'apposition de votre signature.



![img](assets/en/52.webp)



Pendant un court instant, Jade traite l'opération, puis, une fois celle-ci terminée, revient au menu d'accueil.



![img](assets/en/53.webp)



Sur Electrum, vous pouvez voir le statut de la transaction, qui est passé de "Non signé" à "Signé" et il vous est maintenant possible de la propager en cliquant sur "Diffusion".



![img](assets/en/54.webp)



wallet, ainsi testé, peut être utilisé pour recevoir UTXO destiné à être stocké en toute sécurité.



![img](assets/en/55.webp)



Ce guide est un exemple d'utilisation de votre Jade, connecté via USB, à une montre wallet. La Electrum est un exemple classique, mais vous pouvez préférer d'autres logiciels wallet. Jade exporte la clé publique vers de nombreux autres portefeuilles : retrouvez les fonctions similaires que vous avez lues dans ce tutoriel, pour vous guider et trouver comment l'employer dans votre application companio préférée.
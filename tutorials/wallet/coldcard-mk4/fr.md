---
name: COLDCARD Mk4
description: Guide d'installation et d'utilisation d'un COLDCARD Mk4 avec un Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**Les wallet matériels** sont des dispositifs physiques conçus pour stocker la clé privée de Bitcoin en toute sécurité. Ils stockent les clés privées hors ligne, ce qui signifie que les pirates ne peuvent pas les atteindre via Internet. Alors que les **software wallet** sont principalement utilisés pour les transactions quotidiennes, les **hardware wallet** sont souvent utilisés pour stocker de plus grandes quantités de bitcoins en toute sécurité pendant une longue période. Lorsqu'une transaction Bitcoin est effectuée à l'aide d'un **hardware wallet**, le wallet peut signer les transactions à l'intérieur de l'appareil, de sorte que la clé privée n'est jamais exposée à des environnements connectés à l'internet.


Dans ce tutoriel, nous allons explorer l'un des wallet les plus populaires produits par Coinkite, la Coldcard Mk4. Nous verrons comment configurer et utiliser ce matériel wallet pour effectuer des transactions Bitcoin.


## Aperçu de la Coldcard Mk4


Coldcard Mk4 est un matériel Bitcoin-only wallet fabriqué par Coinkite. Cet appareil est équipé d'un écran, d'un clavier numérique et d'un couvercle protecteur coulissant. En outre, l'appareil offre plusieurs façons de se connecter et d'interagir, notamment l'USB-C, le fonctionnement sous air à l'aide d'une carte MicroSD, le NFC et un mode de disque virtuel. Le Mk4 comprend également des fonctions de sécurité avancées telles que le BIP39 passphrase et les codes PIN d'astuce, offrant aux utilisateurs un meilleur contrôle et une meilleure protection de leur Bitcoin.


## Configuration initiale : PIN et mots anti-hameçonnage


Pour commencer, la Coldcard Mk4 peut être achetée directement sur le [site web de Coinkite] (https://store.coinkite.com/store). Les acheteurs peuvent également choisir de payer en monnaie fiduciaire ou en Bitcoin. En outre, vous aurez également besoin d'une carte MicroSD (4 Go suffisent) et d'une source d'alimentation pouvant être connectée via un câble USB-C (la Coldcard Mk4 dispose uniquement d'un port d'entrée d'alimentation USB-C). Notez que la Mk4 n'ayant pas de batterie intégrée, elle doit être connectée à la source d'alimentation en permanence pendant son utilisation.


Vous recevrez votre Mk4 dans un sac inviolable. Veuillez vous assurer que le sac n'a pas été compromis. Si vous constatez un problème, tel qu'un dommage ou une déchirure sur le sac, vous pouvez en informer Coinkite en envoyant un courriel à support@coinkite.com. En outre, vous pouvez également trouver un numéro à 12 chiffres sur le sac d'inviolabilité, que nous appellerons le numéro de sac du Mk4. Ce numéro de sac sera utilisé ultérieurement pour vérifier que l'appareil n'a pas été altéré pendant le transport et qu'il provient directement de Coinkite. Le numéro de sac est stocké en toute sécurité dans le secure element de la Coldcard à l'aide de la mémoire flash OTP (One-Time-Programmable), ce qui signifie qu'il ne peut pas être modifié une fois qu'il a été programmé. Lorsque vous allumez l'appareil pour la première fois, le numéro affiché à l'écran doit correspondre à celui du sac. Cela permet de s'assurer que le Mk4 que vous avez reçu est l'appareil original provenant de l'usine et qu'il n'a pas été remplacé ou modifié. Bien que cette vérification ne confirme l'intégrité de l'appareil qu'au moment de la première mise sous tension, le secure element continue de protéger vos clés privées, votre code PIN et votre passphrase, ce qui rend extrêmement difficile toute manipulation susceptible de compromettre votre Bitcoin. En outre, de bonnes pratiques, telles que la sécurisation adéquate des données liées à la wallet, contribueront à la sécurité globale de la Coldcard elle-même. Pour plus d'informations, vous pouvez consulter cet [article] (https://blog.coinkite.com/understanding-mk4-security-model/) qui décrit le modèle de sécurité de la Coldcard.


Le clavier se compose de 10 touches numériques, d'une touche OK (`✓`) et d'une touche d'annulation (`✕`). Certains boutons numériques peuvent également être utilisés pour la navigation : `5` pour naviguer vers le haut (`^`), `7` pour naviguer vers la gauche (`<`), `8` pour naviguer vers le bas `˅`, et `9` pour naviguer vers la droite (`>`).


![01](assets/en/01.webp)


Si l'emballage ne pose aucun problème, vous pouvez l'ouvrir. Le Mk4 est livré avec une carte de sauvegarde wallet qui peut être utilisée pour stocker des informations concernant le code PIN de l'appareil, les mots anti-phishing et la seedphrase. Suivez les étapes suivantes pour l'initialisation :


1. Préparez une feuille de papier et un stylo.

2. Connectez le Mk4 à une source d'alimentation (câble USB-C) et insérez la carte MicroSD.

3. Lorsque l'appareil est mis sous tension pour la première fois, l'écran affiche un message concernant les conditions de vente et d'utilisation de Coldcard. Naviguez vers le bas, puis appuyez sur `✓` pour continuer.

4. Ensuite, un numéro à 12 chiffres s'affiche à l'écran. Vérifier ce numéro par rapport à celui qui figure sur le sachet d'inviolabilité et à la copie supplémentaire du numéro du sachet qui était incluse dans le sachet d'inviolabilité pour s'assurer que l'appareil n'a pas été altéré. Si les numéros ne correspondent pas, contactez immédiatement le service d'assistance Coinkite avant de continuer. Sinon, appuyez sur `✓` pour continuer.


![02](assets/en/02.webp)


5. Sélectionnez `Choose PIN Code`.

6. Naviguez vers le bas en lisant les instructions pour passer à l'étape suivante.


![03](assets/en/03.webp)


7. Sur le Mk4, créez et saisissez le préfixe PIN (qui doit comporter de 2 à 6 caractères) et notez-le, puis appuyez sur `✓` pour continuer.

8. Notez les deux mots affichés à l'écran. Ce sont les mots anti-phishing. Appuyez sur `✓` pour continuer.


![04](assets/en/04.webp)


9. Créez et saisissez le suffixe du code PIN (ou le reste du code PIN, qui doit comporter de 2 à 6 caractères) et notez-le. Appuyez sur `✓` pour continuer.

10. Saisissez à nouveau votre code PIN. Appuyez sur `✓` pour continuer.


![05](assets/en/05.webp)


11. Vérifiez si les mots anti-phishing sont les mêmes que ceux que vous avez écrits à l'étape 8. Appuyez sur `✓` pour continuer.

12. Saisissez à nouveau le suffixe de votre code PIN (ou le reste du code PIN). Appuyez sur `✓` pour continuer.


![06](assets/en/06.webp)


13. Le code PIN et les mots anti-phishing de votre Mk4 sont maintenant créés et stockés avec succès par l'appareil.


![07](assets/en/07.webp)


Notez que la Mk4 vous demandera toujours de saisir votre code PIN à chaque fois que vous allumerez votre appareil. Sans ce code PIN, vous ne pourrez pas accéder à votre Coldcard Mk4. Veillez donc à créer une sauvegarde suffisante du code PIN et des mots anti-phishing.


## Installation de votre Wallet


L'étape suivante consiste à configurer votre wallet. Il y a trois façons de le faire :


- Création d'une nouvelle wallet (standard)
- Création d'un nouveau wallet avec des jets de dés
- Importation d'une wallet


### Création d'une nouvelle wallet (standard)


Pour créer une nouvelle wallet, il suffit de suivre les étapes suivantes.


1. Sélectionnez `New Wallet` (ou `New Seed Words`) > Sélectionnez `12 Word` ou `24 Word (default)` selon votre préférence.


![08](assets/en/08.webp)


2. L'appareil génère 12 ou 24 mots en tant que seedphrase, selon votre choix. Naviguez vers le bas en écrivant soigneusement chaque mot dans le bon ordre. Appuyez ensuite sur `✓` pour continuer.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. L'appareil vous demandera de vérifier votre seedphrase en posant les questions dans un ordre aléatoire (par exemple, "Le mot 1 est...", puis "Le mot 5 est...", puis "Le mot 12 est...", et ainsi de suite) et il y aura trois choix de mots pour chaque question. Reportez-vous à la note de l'étape 2 et choisissez les mots correctement (en appuyant sur `1`, `2` ou `3`, selon ce qui correspond au mot correct) pour compléter la création wallet.


![09](assets/en/09.webp)


4. Le Mk4 vous demandera alors si vous souhaitez activer le NFC/Tap ou non. Pour l'instant, sélectionnez `✕` pour cette option. Cette option pourra être modifiée à l'avenir dans les réglages.

5. Enfin, le Mk4 vous demandera également si vous souhaitez désactiver le port USB (qui peut être utilisé pour le transfert de données sans airgapped). Pour l'instant, sélectionnez `✓` pour cette option. Ceci peut être modifié dans les paramètres à l'avenir.

6. L'écran affiche maintenant le menu principal avec "Prêt à signer" en haut. Ceci marque la fin du processus de création de la wallet.


![10](assets/en/10.webp)


### Création d'un nouveau wallet avec jet de dés


Vous pouvez également choisir de générer la nouvelle seedphrase avec de l'entropie. Faites-le si vous ne faites pas confiance à la seedphrase fraîchement générée par Mk4.


La procédure sur la Coldcard Mk4 est la suivante :


1. Sélectionnez "New Wallet" (ou "New Seed Words") > Sélectionnez "12 Word Dice Roll" ou "24 Word Dice Roll" selon votre préférence.

2. Il vous sera demandé d'entrer les résultats de vos jets de dés. Chaque jet de dés ajoute un caractère aléatoire au processus de création de la wallet, garantissant que votre seedphrase est générée de manière totalement sécurisée et imprévisible. Le nombre minimum de lancers est de 50 pour une seedphrase de 12 mots et de 99 pour une seedphrase de 24 mots. Appuyez sur `✓` après avoir saisi au moins 99 valeurs de jet de dés.


![11](assets/en/11.webp)


3. L'appareil génère 12 ou 24 mots en tant que seedphrase, selon votre choix. Naviguez vers le bas en écrivant soigneusement chaque mot dans le bon ordre. Appuyez ensuite sur `✓` pour continuer.

4. L'appareil vous demandera de vérifier votre seedphrase en posant les questions dans un ordre aléatoire (par exemple, "Le mot 1 est...", puis "Le mot 5 est...", puis "Le mot 12 est...", et ainsi de suite) et il y aura trois choix de mots pour chaque question. Reportez-vous à la note de l'étape 3 et choisissez les mots correctement (en appuyant sur `1`, `2` ou `3`, selon ce qui correspond au mot correct) pour compléter la création wallet.


![12](assets/en/12.webp)


5. Le Mk4 vous demandera alors si vous souhaitez activer le NFC/Tap ou non. Pour l'instant, sélectionnez `✕` pour cette option. Cette option pourra être modifiée à l'avenir dans les réglages.

6. Enfin, le Mk4 vous demandera également si vous souhaitez désactiver le port USB (qui peut être utilisé pour le transfert de données sans airgapped). Pour l'instant, sélectionnez `✓` pour cette option. Ceci peut être modifié dans les paramètres à l'avenir.

7. L'écran affiche maintenant le menu principal avec "Prêt à signer" en haut. Ceci marque la fin du processus de création de la wallet.


![13](assets/en/13.webp)


### Importation d'un wallet


La dernière option consiste à importer un wallet. Vous pouvez le faire si vous souhaitez récupérer un wallet à partir d'un seedphrase que vous possédez déjà. Vous pouvez suivre les étapes suivantes :


1. Sélectionnez `Import Existing`.

2. Sélectionnez "24 mots", "18 mots" ou "12 mots", en fonction du nombre de mots de votre seedphrase.


![14](assets/en/14.webp)


3. Coldcard Mk4 vous demandera alors ce qu'est chaque mot dans l'ordre consécutif. Pour chaque mot, naviguez vers le bas ou vers le haut jusqu'à ce que vous trouviez le préfixe écrit pour chaque mot. L'appareil réduira les possibilités jusqu'à ce que vous trouviez le mot correct. Procédez de la même manière pour les autres mots.

4. Pour le mot final, Coldcard Mk4 n'affichera qu'un nombre limité de mots possibles. S'il n'y a pas de correspondance, il se peut que vous ayez mal saisi les mots. Dans le cas contraire, sélectionnez le mot qui correspond à celui de votre seedphrase.


![15](assets/en/15.webp)


5. Le Mk4 vous demandera alors si vous souhaitez activer le NFC/Tap ou non. Pour l'instant, sélectionnez `✕` pour cette option. Cette option pourra être modifiée à l'avenir dans les réglages.

6. Enfin, le Mk4 vous demandera également si vous souhaitez désactiver le port USB (qui peut être utilisé pour le transfert de données sans airgapped). Pour l'instant, sélectionnez `✓` pour cette option. Ceci peut être modifié dans les paramètres à l'avenir.

7. L'écran affiche maintenant le menu principal avec "Prêt à signer" en haut. Ceci marque la fin du processus de création de la wallet.


![16](assets/en/16.webp)


Notez que le seedphrase est le seul accès pour récupérer votre wallet. Créez une copie de sauvegarde de votre seedphrase et conservez-la dans un endroit sûr. **Pas vos clés, pas vos pièces**, celui qui a votre seedphrase a accès à vos bitcoins !


## Installation de votre passphrase


L'une des meilleures pratiques en matière de Bitcoin consiste à utiliser une passphrase. La passphrase joue le rôle de 13e ou 25e mot en plus de la seedphrase. Ce qui la différencie, c'est que vous pouvez choisir la phrase que vous voulez, alors que la seedphrase est sélectionnée à partir d'une liste prédéterminée de 2048 mots. Par défaut, après avoir configuré votre wallet, vous commencerez par une wallet avec une passphrase vierge. Pour configurer une passphrase non vierge, il suffit de suivre les étapes suivantes :


1. Allez à `Passphrase`.

2. Naviguez vers le bas pour lire la description de passphrase, puis appuyez sur `✓` pour continuer.

3. Sélectionnez `Editer Phrase`.


![17](assets/en/17.webp)


4. Saisissez votre passphrase :


   - Appuyez sur `1` (lettres), `2` (chiffres) ou `3` (symboles) pour sélectionner le type de caractère.
   - Appuyez sur `4` pour passer des minuscules aux majuscules (utilisable uniquement lors de la saisie de lettres).
   - Naviguez en utilisant `^` ou `˅` pour sélectionner le personnage de votre passphrase.
   - Naviguez en utilisant `<` ou `>` pour passer d'un caractère à l'autre. Vous pouvez également utiliser `>` pour ajouter des espaces.
   - Appuyez sur `✕` pour supprimer les caractères.
   - Appuyez sur `✓` lorsque vous avez fini d'éditer le passphrase.

5. En outre, les autres options présentent les fonctionnalités suivantes :


   - Les fonctions "Ajouter un mot" ou "Ajouter des chiffres" peuvent être utilisées pour ajouter des lettres ou des chiffres à la passphrase que vous êtes en train d'éditer.
   - Appuyez sur "Clear ALL" pour réinitialiser le passphrase que vous êtes en train d'éditer.
   - Appuyez sur `CANCEL` pour revenir au menu principal.

6. Notez votre passphrase en guise de sauvegarde.

7. Appuyez sur `APPLY` pour accéder au wallet avec le passphrase que vous venez de régler.

8. Mk4 affichera alors une empreinte de clé maîtresse de 8 caractères. Ceci peut être considéré comme l'"ID" du wallet. Notez cette empreinte et appuyez sur `✓` pour continuer.


![18](assets/en/18.webp)


9. Le wallet affiche alors le menu principal du wallet avec le passphrase que vous avez saisi.

10. Il est important de noter qu'une wallet ne vous indiquera pas que vous avez saisi une passphrase incorrecte, car chaque passphrase correspond à sa propre wallet avec une identité unique (empreinte digitale de la clé principale). Par conséquent, il est conseillé de saisir à nouveau la même passphrase et de vérifier si elle produit la même empreinte wallet, afin de s'assurer que vous l'avez saisie correctement. Pour ce faire, effectuez les étapes 11 à 14.

11. Dans le menu principal, sélectionnez `Restore Master`, puis appuyez sur `✓`. Vous êtes maintenant de retour dans le menu principal du wallet avec le passphrase vierge.


![19](assets/en/19.webp)


12. Passez à nouveau à `Passphrase`, puis appuyez sur `✓` pour continuer.

13. Réintroduisez la passphrase que vous avez notée à l'étape 6, puis appuyez sur `APPLY`.

14. Comparez l'empreinte de la clé principale à 8 caractères avec celle que vous avez notée à l'étape 8. Si les deux empreintes ne correspondent pas, il se peut que vous ayez tapé des caractères erronés. Vous pouvez sélectionner un nouveau passphrase et répéter le processus à partir de l'étape 1. Mais si les deux empreintes digitales correspondent, cela signifie que vous avez saisi la passphrase correctement.

15. Le wallet avec le passphrase que vous avez choisi est prêt à être utilisé.


## Exportation du Wallet vers le Sparrow


Comme les autres wallet matériels, la Coldcard Mk4 ne peut pas être utilisée seule. Elle doit être connectée à un logiciel wallet qui sert d'interface. Le logiciel wallet vous permet de consulter votre solde, de créer des transactions et de gérer des adresses, tandis que la Coldcard signe ces transactions en toute sécurité sans jamais exposer vos clés privées.


Dans ce tutoriel, nous utiliserons l'interface Sparrow Wallet. La procédure d'exportation de la wallet est la suivante :


1. Assurez-vous qu'une carte MicroSD est insérée dans le Mk4.

2. Effectuez les étapes de la "Configuration de votre passphrase" sur la wallet avec la passphrase que vous voulez exporter. Si vous voulez exporter la wallet avec la passphrase vierge, vous pouvez sauter cette étape.

3. Allez dans `Avancé/Outils` > Choisissez `Exporter Wallet` > Sélectionnez `Générique JSON` > Faites défiler vers le bas en lisant les instructions, puis appuyez sur `✓`.


![20](assets/en/20.webp)


4. Mk4 a maintenant créé un fichier au format `.json` sur la carte MicroSD.


![21](assets/en/21.webp)


5. Retirez la carte MicroSD de la carte Cold et insérez-la dans l'appareil où le Sparrow Wallet est installé.

6. Ouvrir Sparrow Wallet.

7. Cliquez sur `Fichier`


![22](assets/en/22.webp)


Ensuite, cliquez sur "Nouveau Wallet"


![23](assets/en/23.webp)


Ensuite, saisissez le nom du wallet


![24](assets/en/24.webp)


Ensuite, cliquez sur `Create Wallet`


![25](assets/en/25.webp)


8. Sélectionnez le `Type de script`.


![26](assets/en/26.webp)


9. Dans la section Keystore, sélectionnez `Airgapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Recherchez Coldcard et cliquez sur `Import File...`.


![28](assets/en/28.webp)


11. Sélectionnez le fichier créé à l'étape 4 (celui avec le format `.json`).


![29](assets/en/29.webp)


12. Sur le Mk4, retournez au menu principal et naviguez vers "Avancé/Outils" > "Voir l'identité". Assurez-vous que l'empreinte digitale affichée sur l'écran du Mk4 correspond à celle du Sparrow Wallet (l'empreinte digitale principale dans la section Keystore)

13. Cliquez sur le bouton "Appliquer" en bas à droite.


![30](assets/en/30.webp)


14. En option, vous pouvez également ajouter un mot de passe pour la wallet exportée. Ce mot de passe est requis chaque fois que vous ouvrez l'application Sparrow Wallet pour accéder à la wallet. Si vous oubliez le mot de passe à l'avenir, il vous suffit de répéter les étapes 1 à 13 et de choisir un nouveau mot de passe.


![31](assets/en/31.webp)


15. Le wallet est maintenant exporté avec succès et prêt à être utilisé.


![32](assets/en/32.webp)


## Recevoir des bitcoins


Ensuite, nous allons apprendre à recevoir Bitcoin à l'aide du Mk4. Ce processus est assez simple car vous n'avez pas besoin d'utiliser l'appareil Mk4 lui-même. Si vous avez déjà exporté votre wallet vers le Sparrow, vous pouvez recevoir des Bitcoin directement via le Sparrow Wallet. Suivez les étapes suivantes pour recevoir des bitcoins avec Mk4 :


1. Ouvrir Sparrow Wallet.

2. Sélectionnez `Open Wallet` > Choisissez le fichier wallet dans lequel vous voulez recevoir des bitcoins > Entrez le mot de passe associé à ce wallet.


![33](assets/en/33.webp)


3. Sur l'interface de Sparrow, cliquez sur l'onglet `Receive` sur le côté gauche de l'interface.


![34](assets/en/34.webp)


4. Une adresse ainsi qu'un code QR apparaîtront en haut. Vous pouvez copier et coller l'adresse ou scanner le code QR à l'aide du wallet que vous utiliserez pour envoyer des bitcoins au Sparrow Wallet. En option, vous pouvez saisir une étiquette pour les bitcoins que vous recevez.


![35](assets/en/35.webp)


5. Après avoir envoyé les bitcoins, sur l'interface de Sparrow, cliquez sur l'onglet "Transactions" sur le côté gauche de l'interface. Vous verrez une nouvelle entrée en haut de l'historique des transactions, qui correspond à la transaction que vous venez de faire.


![36](assets/en/36.webp)


6. Vous pouvez également naviguer sur l'onglet `UTXOs` sur le côté gauche de l'interface pour voir les bitcoins que vous venez de recevoir.


![37](assets/en/37.webp)


## Envoi de bitcoins


Contrairement à la réception de bitcoins, la dépense des bitcoins associés à votre Coldcard nécessite l'utilisation de la Coldcard pour la signature des transactions. La procédure d'envoi de bitcoins avec Mk4 est la suivante :


1. Insérez la carte MicroSD dans l'appareil où votre Sparrow Wallet est installé.

2. Ouvrir Sparrow Wallet.

3. Sélectionnez `Open Wallet` > Choisissez le fichier wallet que vous voulez utiliser pour envoyer des bitcoins > Entrez le mot de passe associé à ce wallet.


![38](assets/en/38.webp)


4. Sur l'interface de Sparrow, cliquez sur l'onglet "Envoyer" sur le côté gauche de l'interface.


![39](assets/en/39.webp)


5. Dans l'onglet "Payer à", entrez l'adresse à laquelle vous voulez envoyer les bitcoins.

6. Ajouter un libellé pour la transaction.

7. Saisissez le montant de bitcoins que vous souhaitez envoyer.

8. Saisissez le montant de la redevance en basculant la "fourchette" ou entrez directement un chiffre dans la partie "redevance".


![40](assets/en/40.webp)


9. Dans le coin inférieur droit, cliquez sur "Créer une transaction".


![41](assets/en/41.webp)


10. Vous serez amené dans un nouvel onglet de transaction dont le nom est l'étiquette que vous avez saisie à l'étape 6. Cliquez sur "Finaliser la transaction pour signature".


![42](assets/en/42.webp)


11. Cliquez sur "Sauvegarder la transaction" et enregistrez la transaction sur la carte MicroSD. Renommez le fichier si nécessaire. Cette étape permet d'enregistrer la transaction sous la forme d'un fichier PSBT.


![43](assets/en/43.webp)


12. Retirez la carte MicroSD et insérez-la dans votre Coldcard Mk4.

13. Allumez votre Mk4 en le connectant à une source d'alimentation.

14. Saisissez votre code PIN.

15. Allez dans `Passphrase` et entrez la passphrase de la wallet que vous voulez utiliser pour envoyer les bitcoins. Si vous voulez utiliser la wallet avec la passphrase vierge, sautez cette étape.

16. Assurez-vous que l'empreinte de la clé principale est la même que celle de votre Sparrow Wallet. Vous pouvez le vérifier dans l'onglet "Réglages" de Sparrow Wallet sur le côté gauche de l'interface. Ensuite, appuyez sur `✓` sur votre Mk4 pour continuer. Cela vous amènera au menu principal.

17. Dans le menu principal de Mk4, sélectionnez "Prêt à signer". L'écran affichera le message "OK POUR ENVOYER". Assurez-vous que le montant des bitcoins que vous voulez envoyer et l'adresse de réception sont tous corrects. Appuyez sur `✓` pour confirmer ou `✕` pour annuler.

18. S'il y a plusieurs fichiers PSBT à choisir, Mk4 affichera le message "Choisir le fichier PSBT à signer". Appuyez sur `✓` pour continuer. Ensuite, sélectionnez le fichier PSBT que vous voulez signer en naviguant vers le bas ou vers le haut. Effectuez l'étape 17 pour cette transaction.


![44](assets/en/44.webp)


19. Mk4 affiche alors le message "PSBT Signed" ainsi que le nom du fichier du PSBT signé. Appuyez sur `✓` pour continuer.

20. Retirez la carte MicroSD de la carte Cold et insérez-la dans l'appareil où la carte Sparrow Wallet est installée.

21. Sur Sparrow Wallet, cliquez sur "Charger la transaction".


![45](assets/en/45.webp)


22. Sélectionnez le fichier portant le même nom que celui créé à l'étape 19.


![46](assets/en/46.webp)


23. Cliquez sur "Transaction diffusée".


![47](assets/en/47.webp)


24. Votre transaction a été diffusée et est en cours de traitement. Vous pouvez aller dans l'onglet "Transactions" pour voir le statut de confirmation de votre transaction.


![48](assets/en/48.webp)


## Mise à jour du micrologiciel


### Vérification de la version du micrologiciel


Le micrologiciel du Coldcard Mk4 peut toujours être mis à jour. Pour vérifier si votre Mk4 a été mis à jour vers la dernière version ou non, effectuez les étapes suivantes :

1. Allumez votre Mk4 en le connectant à une source d'alimentation.

2. Saisissez votre code PIN.

3. Allez dans `Avancé/Outils` > Sélectionnez `Mise à jour du firmware` > Sélectionnez `Afficher la version`.


![49](assets/en/49.webp)


Vérifiez la version affichée sur l'écran du Mk4 par rapport à celle qui figure sur le [site web de Coinkite] (https://coldcard.com/downloads). Si la version est différente, vous pouvez mettre à jour le micrologiciel vers la version la plus récente.


![50](assets/en/50.webp)


### Mise à jour du micrologiciel


Si vous souhaitez mettre à jour le micrologiciel vers la dernière version, procédez comme suit :


1. Insérez la carte MicroSD dans votre ordinateur portable/PC.

2. Allez sur [Coinkite's website] (https://coldcard.com/downloads) et téléchargez le dernier firmware sur votre carte MicroSD (Le bouton rouge à droite de l'image Mk4 avec le numéro de version dessus).


![51](assets/en/51.webp)


Vous pouvez également télécharger d'autres versions en cliquant sur "All Files on Mk4" et en explorant la version que vous souhaitez télécharger. Le fichier téléchargé sera au format `.dfu`.


![52](assets/en/52.webp)


3. Retirez la carte MicroSD et insérez-la dans votre Mk4.

4. Allumez votre Mk4 en le connectant à une source d'alimentation.

5. Saisissez votre code PIN.

6. Allez dans `Advanced/Tools` > Sélectionnez `Upgrade Firmware` > Sélectionnez `From MicroSD` > Faites défiler vers le bas en lisant les instructions puis appuyez sur `✓`.


![53](assets/en/53.webp)


7. Sélectionnez le fichier `.dfu` que vous avez téléchargé à l'étape 2.

8. La Coldcard Mk4 affichera un message "Installer ce nouveau firmware". Faites défiler vers le bas en lisant les instructions puis appuyez sur `✓`.


![54](assets/en/54.webp)


9. Attendez que le Mk4 ait fini d'installer le nouveau micrologiciel. Ne débranchez pas la source d'alimentation pendant l'installation.

10. Une fois cette opération terminée, la Mk4 redémarre d'elle-même. Vous pouvez saisir votre code PIN et suivre les étapes de "Vérification de la version du micrologiciel" pour vérifier si le micrologiciel a été mis à jour ou non.


## Fonctionnalités avancées


### Modifier votre code PIN


Si vous souhaitez modifier votre code PIN de connexion, procédez comme suit :


1. Préparez un stylo et une feuille de papier.

2. Allumez votre Mk4 en le connectant à une source d'alimentation.

3. Saisissez votre code PIN.

4. Allez dans `Settings` > Sélectionnez `Login Settings` > Sélectionnez `Change Main PIN`

5. Naviguez vers le bas en lisant le message, puis appuyez sur `✓` pour continuer.


![55](assets/en/55.webp)


6. Saisissez votre ancien code PIN.

7. Saisissez votre nouveau code PIN (de 2 à 6 caractères) et notez-le.

8. Mk4 va maintenant afficher deux nouveaux mots anti-phishing, notez-les, puis appuyez sur `✓` pour continuer.

9. Saisissez votre nouveau suffixe PIN (ou le reste du PIN, qui doit comporter de 2 à 6 caractères) et notez-le.


![56](assets/en/56.webp)


10. Saisissez à nouveau votre nouveau code PIN.

11. Vérifiez si les mots anti-phishing correspondent à ceux que vous avez écrits à l'étape 8.

12. Saisissez à nouveau le suffixe de votre nouveau code PIN (ou le reste du code PIN).


![57](assets/en/57.webp)


13. Votre code PIN a été modifié avec succès.


### NIP des tours - Ajouter un nouveau tour


Un code PIN piège est un code PIN alternatif distinct de celui que vous utilisez pour configurer votre Coldcard Mk4 pour la toute première fois. Lorsque vous allumez votre Mk4, vous pouvez saisir le(s) code(s) secret(s) au lieu de votre code principal pour déclencher certaines actions. Pour configurer le PIN astuce dans la Mk4, vous pouvez suivre les étapes suivantes :


1. Préparez un stylo et une feuille de papier.

2. Allumez votre Mk4 en le connectant à une source d'alimentation.

3. Saisissez votre code PIN.

4. Allez dans `Settings` > Sélectionnez `Login Settings` > Sélectionnez `Trick PINs` > Sélectionnez `Add New Trick`.


![58](assets/en/58.webp)


5. Saisissez le préfixe de votre code PIN (de 2 à 6 caractères) et notez-le.

6. Mk4 va maintenant afficher deux nouveaux mots anti-phishing, notez-les, puis appuyez sur `✓` pour continuer.

7. Saisissez le suffixe de votre code PIN (ou le reste du code PIN, qui doit comporter de 2 à 6 caractères) et notez-le.


![59](assets/en/59.webp)


8. Naviguez vers le bas ou vers le haut pour sélectionner l'action que vous souhaitez associer au code PIN astuce que vous venez de créer. La liste des actions est la suivante :


    - si cette option est sélectionnée, les puces de votre Mk4 seront détruites après la saisie du code PIN, ce qui rendra votre Mk4 inutilisable de façon permanente.
    - `Wipe Seed`, vous pouvez choisir entre les actions suivantes :
      - `Wipe & Reboot` : Le seed est effacé et la carte Cold redémarre après la saisie du code PIN.
      - effacement silencieux : Le seed est effacé silencieusement, mais la carte Cold agira comme si le code PIN avait été saisi de manière incorrecte.
      - `Wipe -> Wallet` : Le seed est effacé silencieusement, et la carte Cold vous emmène dans une situation de contrainte wallet.
    - si vous sélectionnez l'option "Contrainte Wallet", votre Mk4 conduira à une contrainte wallet après la saisie du code PIN.
    - `Compte à rebours de connexion`, vous pouvez choisir entre les actions suivantes :
      - `Wipe & Countdown` (effacement et compte à rebours) : Le seed est immédiatement effacé, puis le Mk4 commence à afficher un compte à rebours.
      - compte à rebours et brique : Le compte à rebours commence et le Mk4 se brique lui-même une fois le temps écoulé.
      - `Just Countdown` (Compte à rebours) : Le Mk4 commencera le compte à rebours et se réinitialisera une fois le temps écoulé.
    - lorsque cette option est sélectionnée, après la saisie du code PIN, la carte Cold agit comme si la carte seedphrase avait été effacée, alors qu'elle est en fait toujours en mémoire.
    - `Just Reboot`, lorsque cette option est sélectionnée, la Coldcard se redémarrera d'elle-même après la saisie du code PIN.
    - cette fonction avancée est destinée aux utilisateurs expérimentés et est conçue pour protéger contre les menaces sérieuses, telles que la coercition par quelqu'un ayant des connaissances d'initié. Lorsque le mode Delta est activé, la COLDCARD semble ouvrir la véritable wallet, ce qui permet à l'attaquant de naviguer et de confirmer son authenticité. Cependant, elle bloque secrètement toute signature de transaction, de sorte qu'aucun bitcoin ne peut être envoyé. Il désactive également l'accès à la phrase seed, et toute tentative de la visualiser l'effacera complètement. Pour rendre le faux wallet plus convaincant, le code PIN astucieux utilisé pour le mode Delta doit commencer par les mêmes chiffres que le vrai code PIN (afin d'afficher les mêmes mots anti-phishing), mais se terminer différemment.
    - `Policy Unlock` (déverrouillage de la politique), lorsque cette option est sélectionnée, la politique de dépense à signature unique (SSSP) sera désactivée après la saisie du code PIN de l'astuce.
    - `Policy Unlock & Wipe`, lorsqu'il est sélectionné, il prétend désactiver SSSP mais il efface le seedphrase dans le processus.

9. Après avoir sélectionné l'action que vous souhaitez associer au PIN astuce, confirmez votre choix en appuyant sur `✓`. Votre PIN astuce est configuré avec succès.

10. Dans `Settings` > `Login Settings` > `Trick PINs`, vous pouvez voir la liste des trick PINs que vous avez créés et les actions qui y sont associées. Vous pouvez choisir de reconfigurer les codes PIN pièges et les actions qui leur sont associées. Vous pouvez également le cacher ou le supprimer en sélectionnant le PIN, puis en sélectionnant "Cacher l'astuce" ou "Supprimer l'astuce".


![60](assets/en/60.webp)


### NIP pièges - Ajouter en cas d'erreur


Vous pouvez également ajouter une action `Add If Wrong` qui sera déclenchée après la saisie d'un certain nombre de fois d'un code PIN incorrect. Vous pouvez configurer cette action en suivant les étapes suivantes :


1. Allumez votre Mk4 en le connectant à une source d'alimentation.

2. Saisissez votre code PIN.

3. Allez dans `Paramètres` > Sélectionnez `Paramètres de connexion` > Sélectionnez `Pinces pièges` > Sélectionnez `Ajouter en cas d'erreur`.


![61](assets/en/61.webp)


4. Mk4 affichera un message concernant ce réglage. Naviguez vers le bas en lisant l'explication, puis appuyez sur `✓` pour continuer.

5. Saisissez le nombre de tentatives erronées nécessaires pour déclencher l'action. Note : Le nombre maximum de tentatives est de `12`. En effet, le Mk4 est conçu de telle sorte que lorsque le code PIN incorrect est saisi `13` fois, l'appareil se brique lui-même, ce qui le rend inutilisable de façon permanente. Après avoir saisi le numéro, appuyez sur `✓` pour continuer.

6. Naviguez vers le haut ou vers le bas pour sélectionner l'action. Les actions disponibles sont les suivantes :


   - `Wipe, Stop` : Le seedphrase est effacé et l'appareil affiche "Seed is wiped, Stop"
   - `Wipe & Reboot` : Le seedphrase est effacé et l'appareil redémarre sans aucun message.
   - `Silent Wipe` (effacement silencieux) : Le seedphrase est effacé sans bruit et l'appareil se comporte comme s'il s'agissait d'une tentative d'erreur de PIN (pas de message d'effacement évident).
   - `Brick Self` : L'appareil est désactivé de façon permanente et n'affiche que "Bricked"
   - dernière chance : Le seedphrase est effacé mais vous avez droit à une dernière tentative de saisie du code PIN ; saisissez à nouveau un code PIN erroné et l'appareil sera bloqué.
   - `Just Reboot` (Redémarrer simplement) : L'appareil redémarre simplement et rien d'autre ne change.

Choisissez l'action que vous voulez appliquer et appuyez sur `✓` pour continuer


![62](assets/en/62.webp)


7. Vous serez ramené au répertoire `Settings > Login Settings > Trick PINs`. Sous la rubrique "Trick PINs :", vous trouverez la liste des codes secrets avec l'action "WRONG PIN" (code secret erroné). Vous pouvez également le cacher ou le supprimer en sélectionnant le PIN, puis en sélectionnant "Hide Trick" ou "Delete Trick".


![63](assets/en/63.webp)



## Conclusion


Ce tutoriel explique comment configurer Mk4, comment effectuer des transactions Bitcoin avec Mk4 et comment utiliser certaines fonctionnalités avancées de Mk4. Il offre des moyens sûrs et flexibles de stocker et de gérer vos bitcoins. Sa conception garantit que les clés privées ne quittent jamais l'appareil, tandis que des fonctionnalités telles que les passphrase, les codes PIN et les transactions à l'air libre permettent aux utilisateurs de contrôler entièrement leur configuration de sécurité. Il peut être associé au Sparrow Wallet pour une expérience conviviale de création, de signature et de gestion des transactions Bitcoin sans compromettre la confidentialité ou la sécurité.


Si vous souhaitez explorer d'autres fonctionnalités, vous pouvez consulter la documentation sur le site web de Coinkite [ici] (https://coldcard.com/docs/). J'espère que ce tutoriel vous sera utile lorsque vous utiliserez votre Coldcard Mk4. Merci et à la prochaine !
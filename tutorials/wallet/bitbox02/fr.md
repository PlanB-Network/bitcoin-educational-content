---
name: BitBox02

description: Configuration et utilisation d'un BitBox02
---

# Bitbox02

![cover](assets/cover.jpeg)

Le BitBox02 (https://bitbox.swiss/) est un portefeuille physique fabriqué en Suisse spécialement conçu pour sécuriser vos Bitcoins. Parmi ses principales caractéristiques, on retrouve une sauvegarde et une restauration faciles à l'aide d'une carte microSD, un design minimaliste et discret, ainsi qu'une prise en charge complète de Bitcoin.

![device](assets/1.png)

Il offre une sécurité de pointe conçue par des experts, avec une conception à double puce comprenant une puce sécurisée. Son code source a été entièrement audité par des chercheurs en sécurité et est entièrement open-source. Le BitBox02 est livré avec une application BitBoxApp simple mais puissante, qui assure une gestion sécurisée de vos Bitcoins. Il prend en charge un nœud complet pour Bitcoin et garantit une communication chiffrée de bout en bout entre l'application et l'appareil. Fabriqué en Suisse, le BitBox02 a acquis une réputation positive auprès de ses utilisateurs.

![video](https://youtu.be/sB4b2PbYaj0)

> Spécifications
>
> - Connectivité : USB-C
> - Compatibilité : Windows 7 et versions ultérieures, macOS 10.13 et versions ultérieures, Linux, Android
> - Entrée : Capteurs tactiles capacitifs
> - Microcontrôleur : ATSAMD51J20A ; 120 Mhz 32-bit Cortex-M4F ; Générateur de nombres aléatoires véritable
> - Puce sécurisée : ATECC608B ; Générateur de nombres aléatoires véritable (NIST SP 800-90A/B/C)
> - Écran : OLED blanc 128 x 64 px
> - Matériau : Polycarbonate
> - Taille : 54,5 x 25,4 x 9,6 mm, y compris la prise USB-C
> - Poids : Appareil 12g ; avec emballage et accessoires 160g

Téléchargez les fiches techniques sur leur site web https://bitbox.swiss/bitbox02/

## Comment utiliser le portefeuille matériel BitBox02

### Configuration du BitBox02

Le BitBox02 dispose d'une connexion USB-C attachée à la coque. Si votre ordinateur utilise le port USB standard, vous devrez utiliser l'adaptateur fourni avec l'appareil.

Connectez-le à votre ordinateur et l'appareil s'allumera (ne le faites pas encore).

Il dispose de capteurs au-dessus et en dessous, et il vous demandera de toucher le haut ou le bas pour orienter l'écran comme vous le souhaitez.

![image](assets/2.png)

### Téléchargez l'application BitBox02

Rendez-vous sur https://shiftcrypto.ch/ et cliquez sur le lien "App" en haut pour accéder à la page de téléchargement :

![image](assets/3.png)

Cliquez sur le bouton bleu "Télécharger" :

![image](assets/4.png)

Pour vérifier le téléchargement (cela ajoute de la complexité, mais c'est recommandé, surtout si vous stockez beaucoup de bitcoins), voir l'Annexe A.

Après le téléchargement, vous pouvez décompresser le fichier. Sur un Mac, double-cliquez simplement sur le fichier téléchargé, et une icône BitBox App apparaîtra dans votre répertoire de téléchargements. Vous pouvez la faire glisser sur votre bureau (ou n'importe où) pour un accès facile.

Double-cliquez sur l'application pour la lancer (elle ne s'installe pas).

Sur Mac, votre ordinateur vous donnera un avertissement. Ignorez-le simplement et cliquez sur "Ouvrir" :

![image](assets/5.png)

Vous verrez ensuite ceci :

![image](assets/6.png)

Connectez maintenant l'appareil à l'ordinateur.
Il vous montrera un code d'appariement. Vérifiez qu'ils correspondent, puis touchez le capteur pour sélectionner la coche. Ensuite, revenez à l'écran, le bouton "Continuer" sera disponible pour vous.
![image](assets/7.png)

Vous aurez ensuite la possibilité de créer une nouvelle graine ou de restaurer une graine. Je vais vous montrer comment créer une nouvelle graine (Il est également important de restaurer la graine que vous avez créée pour tester la qualité de votre sauvegarde, avant de charger des bitcoins sur le portefeuille).

![image](assets/8.png)

L'appareil est livré avec une carte microSD. Insérez-la si vous ne l'avez pas déjà fait.

![image](assets/9.png)

Nommez votre appareil et cliquez sur "Continuer", puis confirmez sur l'appareil.

![image](assets/10.png)

Vous serez ensuite invité à définir un mot de passe pour l'appareil. Ce n'est pas une partie de votre graine. Ce n'est pas non plus une phrase secrète (c'est une partie de votre graine). Il s'agit simplement d'un mot de passe pour verrouiller l'appareil. Lorsque vous allumez l'appareil, on vous demandera d'entrer ce mot de passe à chaque fois. Vous avez droit à 10 échecs consécutifs avant que l'appareil ne s'efface de toute sa mémoire, alors faites attention. L'animation à l'écran vous apprendra comment utiliser les commandes de l'appareil pour définir le mot de passe.

![image](assets/11.png)

Lisez l'écran suivant, cochez chaque case, puis continuez.

![image](assets/12.png)
![image](assets/13.png)
![image](assets/14.png)

Et voici à quoi ressemble le portefeuille une fois qu'il est prêt à être utilisé.

![image](assets/15.png)

### PAS SI VITE !!

C'est assez étrange, mais le BitBox02 nous dit que nous sommes prêts à utiliser l'appareil, mais il ne nous a pas demandé d'écrire les mots de la graine ! La SEULE sauvegarde que nous avons est le fichier enregistré sur la carte microSD. C'est insuffisant. Ces dispositifs de stockage ne durent pas éternellement (en raison de la "dégradation des bits"). Nous avons besoin d'une sauvegarde papier, et de duplicatas, conservés dans un coffre-fort (comme expliqué dans le guide général sur l'utilisation des portefeuilles matériels).

Pour obtenir notre phrase de la graine et l'écrire, allez dans l'onglet "Gérer l'appareil" à gauche, puis cliquez sur "Afficher les mots de récupération".

![image](assets/16.png)

Vous pouvez ensuite passer par la confirmation, et l'appareil vous présentera les mots. Écrivez-les soigneusement et ne laissez jamais personne les voir.

![image](assets/17.png)

Après cela, vous pouvez cliquer sur l'onglet Bitcoin à gauche pour obtenir vos adresses de réception.

![image](assets/18.png)

Il en affiche une à la fois, mais au moins il vous permet de choisir quelle adresse utiliser parmi les 20 premières :

![image](assets/19.png)

En cliquant sur le bouton bleu, l'adresse complète s'affiche, et vous serez invité à vérifier que l'adresse correspond à l'affichage à l'écran. C'est une bonne pratique pour confirmer qu'aucun logiciel malveillant sur votre ordinateur ne vous trompe en vous incitant à envoyer des bitcoins à une adresse d'attaquant.

![image](assets/20.png)

Pour envoyer des bitcoins vers ce portefeuille, vous pouvez copier l'adresse et la coller dans la page de retrait de l'échange où se trouvent vos pièces. Je vous recommande d'envoyer d'abord une petite quantité de test, puis de pratiquer les dépenses, soit en les renvoyant à l'échange, soit à la deuxième adresse de votre portefeuille.

Pour des montants plus importants, je vous suggère de créer une phrase secrète (voir ci-dessous). Le portefeuille d'origine (sans phrase secrète) peut être utilisé comme votre portefeuille leurre (il devra contenir une somme raisonnable pour être crédible).

### Se connecter à un nœud

Le BitBox02 se connectera automatiquement à un nœud. Voyons où il se connecte. Cliquez sur l'onglet "Paramètres" à gauche, puis sur "connectez votre propre nœud complet".

![image](assets/21.png)

Et ici, nous pouvons voir qu'il se connecte au nœud de shiftcrypto. Pas génial. Nous avons trahi toutes nos adresses bitcoin en les leur donnant, ainsi que notre adresse IP (pas la graine bien sûr ; ils peuvent voir nos adresses/soldes, mais ne peuvent pas les dépenser). Nous pouvons entrer les détails de notre propre nœud sur cette page (au-delà de la portée de ce guide particulier), ou nous pouvons utiliser un meilleur logiciel comme Sparrow Bitcoin Wallet, Electrum Desktop Wallet ou Specter Desktop. Je vais vous montrer plus tard dans le guide comment utiliser Sparrow Bitcoin Wallet.

![image](assets/22.png)

Ajoutez une phrase secrète

Maintenant que nous avons configuré l'appareil avec l'application BitBox02 (et révélé nos adresses, inévitable avec ce portefeuille matériel particulier), nous pouvons ajouter une phrase secrète à notre graine. Cela nous permettra de créer un nouveau portefeuille en utilisant la même graine, et ShiftCrypto ne verra jamais nos nouvelles adresses. Nous connecterons ce portefeuille uniquement à notre propre logiciel.

### Activer la phrase secrète

Allez-y maintenant et "activez" la fonction de phrase secrète (mais nous ne définissons pas encore de phrase secrète). Allez dans l'onglet "Gérer l'appareil" et cliquez sur "Activer la phrase secrète" (cercle rouge ci-dessous).

![image](assets/23.png)

Lisez les étapes...

![image](assets/24.png)
![image](assets/25.png)
![image](assets/26.png)

Déconnectez maintenant l'appareil et fermez l'application BitBox02.

FIN de la section BitBox02 par Parman.

Votre appareil est maintenant entièrement opérationnel pour être utilisé sur n'importe quelle solution de bureau telle que Specter, Sparrow et en utilisant l'interface BitBox.

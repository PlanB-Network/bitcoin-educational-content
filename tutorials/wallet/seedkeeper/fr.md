---
name: Seedkeeper
description: Comment sauvegarder votre wallet Bitcoin avec la carte à puce Seedkeeper ?
---

![cover](assets/cover.webp)

Le Seedkeeper est une carte à puce développée par Satochip, une entreprise belge spécialisée dans les solutions matérielles pour la gestion et la protection des secrets numériques. Reconnue pour sa gamme de smartcards destinées à l’écosystème Bitcoin, Satochip a conçu le Seedkeeper comme une alternative aux méthodes traditionnelles de conservation de phrases mnémoniques.

Concrètement, le Seedkeeper prend la forme d’une carte à puce multifonctionnelle, certifiée EAL6, dotée d’un processeur sécurisé et d’une mémoire inviolable (c'est donc ce que l'on appelle un "*Secure Element*"). Comme son nom l'indique, son rôle est de stocker de manière chiffrée et protégée des phrases mnémoniques de portefeuilles Bitcoin ainsi que des mots de passe. Avec le Seedkeeper, vous pouvez générer, importer, organiser et sauvegarder vos secrets directement dans le composant sécurisé de la carte.

Le Seedkeeper répond donc selon moi à deux cas d’utilisation principaux que nous étudierons en 2 tutoriels distincs :
- **La conservation de phrases mnémoniques Bitcoin** : au lieu de noter vos 12 ou 24 mots sur un support papier, vous pouvez les importer dans la smartcard et les protéger par un code PIN.
- **La gestion de mots de passe** : vous pouvez générer des mots de passe forts via l’application Seedkeeper et les stocker directement dans la smartcard, ce qui donne un gestionnaire de mots de passe sécurisé hors ligne pratique et facile à utiliser.

Sur le plan technique, le Seedkeeper offre une capacité de 8192 octets, ce qui permet de stocker au minimum 50 secrets distincts (le nombre exact dépendra de leur taille et des métadonnées associées à chacun). L’accès au Seedkeeper se fait soit [par lecteur de carte à puce relié](https://satochip.io/accessories/) à un ordinateur, soit via l’application mobile avec connexion NFC. Le tout fonctionne en mode hors ligne, sans connexion Internet, ce qui garantit une surface d’attaque limitée.

![Image](assets/fr/001.webp)

Une fonctionnalité particulièrement intéressante est la possibilité de dupliquer le contenu d’un Seedkeeper vers un autre afin de créer une sauvegarde. Nous allons voir dans ce tutoriel comment faire cette manipulation.

Le Seedkeeper est également très intéressant lorsqu’il est associé à un hardware wallet stateless comme le SeedSigner ou le Specter DIY. Dans ce cas, il n’est pas nécessaire d’utiliser le client de Satochip sur ordinateur ou mobile. Le Seedkeeper conserve la seed dans son élément sécurisé et peut être utilisé directement avec le périphérique de signature, ce qui évite d’avoir recours à un QR code papier. Je ne développerai pas ce cas d’usage particulier dans ce tutoriel, puisqu’il fait l’objet d’un autre tutoriel dédié :

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Quel cas d'usage pour le Seedkeeper ?

Ici, je traite uniquement des cas d’usage liés à Bitcoin, car c’est le sujet de ce tutoriel. Nous n’aborderons donc pas la fonctionnalité de gestion des mots de passe, qui fera l’objet d’un autre tutoriel.

Comparé à une simple sauvegarde papier de la phrase mnémonique, l’utilisation d’un Seedkeeper présente plusieurs avantages :

- **Résistance au vol :** la seed de votre portefeuille n’est pas accessible en clair. Pour l’extraire, il faut connaître le PIN du Seedkeeper. Un voleur qui s’emparerait de l’appareil ne pourra rien en faire sans ce code.

- **Diffusion du risque sur deux facteurs :** vous pouvez répartir la sécurité entre un facteur numérique et un facteur physique. Par exemple, si vous stockez le PIN du Seedkeeper dans votre gestionnaire de mots de passe, il faudra à la fois accéder à ce gestionnaire et posséder la smartcard physiquement pour obtenir la seed (une probabilité d’attaque nettement réduite).

- **Gestion centralisée :** le Seedkeeper facilite la gestion de plusieurs seeds de différents portefeuilles.

- **Sauvegardes faciles :** il permet de dupliquer simplement des sauvegardes chiffrées vers d’autres SeedKeepers.

Cependant, certains inconvénients méritent d’être soulignés par rapport à une simple sauvegarde papier de votre seed :

- **Le prix :** bien que modeste (environ 25 €), il reste supérieur à celui d’une feuille de papier.

- **La dépendance à un appareil informatique généraliste :** la saisie et la gestion de la seed nécessitent un ordinateur ou un smartphone, ce qui implique que votre phrase mnémonique transite par une machine avec une surface d’attaque bien plus large qu’un hardware wallet. Cela peut représenter un risque en cas de compromission du poste. C’est pourquoi je déconseille l’usage du Seedkeeper pour stocker la seed d’un hardware wallet (sauf dans un usage stateless sans ordinateur, comme avec le SeedSigner). Le rôle du hardware wallet est précisément de conserver la seed dans un environnement minimaliste et hautement sécurisé. En saisissant manuellement votre seed sur votre ordinateur habituel, elle n’est plus confinée au hardware wallet : elle se retrouve également sur une machine généraliste, exposée à de multiples vecteurs d’attaque. Il vaut donc mieux utiliser le Seedkeeper pour un portefeuille chaud plutôt que pour un portefeuille froid (sauf SeedSigner / stateless hardware wallet).

- **Le risque de perte lié au PIN :** l’inaccessibilité directe de la seed, contrairement à une sauvegarde papier, constitue effectivement une protection face aux vols physiques. Mais comme toujours, la sécurité repose sur un équilibre entre risque de vol et risque de perte. Si votre sauvegarde nécessite un PIN, la perte de ce code rendra impossible la récupération de votre phrase mnémonique, et donc l’accès à vos bitcoins.

Au regard de ces avantages et inconvénients, je considère que les meilleures utilisations du Seedkeeper (en dehors de sa fonction de gestionnaire de mots de passe) sont, d’une part, le stockage des seeds de vos **portefeuilles logiciels**, puisqu’elles résident déjà sur votre téléphone ou votre ordinateur, ou bien de vos hardware wallet sans écran comme le Satochip, et d’autre part, l’usage en combinaison avec un hardware wallet stateless comme le SeedSigner, où il prend tout son sens.

Un autre cas d’utilisation particulièrement intéressant du Seedkeeper est la possibilité de sauvegarder de façon sécurisée et fiable les *Descriptors* de vos portefeuilles.

## 2. Comment obtenir un Seedkeeper ?

Il existe principalement deux façons d’obtenir votre Seedkeeper. Vous pouvez l’[acheter directement sur la boutique officielle](https://satochip.io/product/seedkeeper/) de Satochip ou auprès d’un revendeur agréé. Mais puisque [l’applet du Seedkeeper est open-source](https://github.com/Toporin/Seedkeeper-Applet), vous avez également la possibilité de l’installer vous-même sur [une carte à puce vierge](https://satochip.io/product/blank-javacard-for-diy-project/).

Si vous souhaitez utiliser la fonctionnalité de sauvegarde du Seedkeeper, il vous faudra évidemment acquérir deux smartcards.

## 3. Installer le client Seedkeeper

Dans ce tutoriel, nous allons sauvegarder la seed de notre portefeuille sur notre Seedkeeper. La première étape consiste à installer le logiciel sur votre ordinateur ou votre smartphone. Sur PC, vous devrez [télécharger la dernière version de Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Sur mobile, l’application Seedkeeper est disponible sur le [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) ainsi que sur l’[App Store Apple](https://apps.apple.com/be/app/seedkeeper/id6502836060).

![Image](assets/fr/002.webp)

## 4. Initialisation du Seedkeeper

Lancez l’application et cliquez sur le bouton "*Click & Scan*".

![Image](assets/fr/003.webp)

Un code PIN vous est demandé pour votre Seedkeeper. Comme il s’agit d’une nouvelle carte, aucun PIN n’a encore été défini. Entrez donc un code quelconque pour passer cette étape, puis cliquez sur "*Suivant*".

![Image](assets/fr/004.webp)

Placez ensuite la carte à l’arrière de votre smartphone. L’application détectera que le Seedkeeper n’est pas encore initialisé et vous invitera à définir le code PIN de votre carte à puce, compris entre 4 et 16 caractères. Pour une sécurité optimale, choisissez un mot de passe robuste, le plus long possible, aléatoire et composé d’une grande diversité de caractères. Ce code PIN constitue la seule barrière de protection contre un accès physique à votre phrase de récupération.

**Pensez également à sauvegarder ce code PIN dès maintenant**, par exemple dans un gestionnaire de mots de passe, ou bien sur un support physique distinct. Dans ce dernier cas, ne conservez jamais le support contenant le PIN au même endroit que votre Seedkeeper, sans quoi cette sécurité deviendrait inutile. Il est important de disposer d’une sauvegarde fiable : sans ce code PIN, il vous sera impossible de récupérer les secrets enregistrés sur votre Seedkeeper.

![Image](assets/fr/005.webp)

Confirmez votre code PIN une seconde fois.

![Image](assets/fr/006.webp)

Votre Seedkeeper est désormais initialisé. Vous pouvez le déverrouiller en entrant le code PIN que vous venez de définir.

![Image](assets/fr/007.webp)

Vous accédez maintenant à la page de gestion de votre carte à puce.

![Image](assets/fr/008.webp)

## 5. Enregistrer une seed sur le Seedkeeper

Une fois votre Seedkeeper déverrouillé, cliquez sur le bouton "*+*".

![Image](assets/fr/009.webp)

Sélectionnez "*Importer un secret*". L’option "*Générer un secret*" permet quant à elle de créer une nouvelle phrase mnémonique directement depuis l’application.

![Image](assets/fr/010.webp)

Dans notre cas, nous voulons sauvegarder la seed de notre portefeuille. Cliquez donc sur "*Mnémonique*".

![Image](assets/fr/011.webp)

Attribuez un "*Label*" à ce secret afin de l’identifier facilement si vous enregistrez plusieurs informations dans votre Seedkeeper.

![Image](assets/fr/012.webp)

Saisissez ensuite votre phrase de récupération dans le champ prévu à cet effet. Vous pouvez également, si vous le souhaitez, ajouter une passphrase BIP39 ou vos *Descriptors*. Cliquez ensuite sur "*Importer*".

![Image](assets/fr/013.webp)

*La phrase mnémonique affichée sur cette image est fictive, elle n’appartient à personne. Il s’agit uniquement d’un exemple. Ne révélez jamais votre propre phrase à quiconque, sous peine de vous faire voler vos bitcoins.*

Placez votre Seedkeeper à l’arrière de votre smartphone.

![Image](assets/fr/014.webp)

Votre seed a bien été enregistrée.

![Image](assets/fr/015.webp)

## 6. Accéder à votre seed sur le Seedkeeper

Si vous souhaitez consulter votre phrase mnémonique, prenez votre Seedkeeper et cliquez sur le bouton "*Click & Scan*".

![Image](assets/fr/016.webp)

Saisissez votre code PIN puis appuyez sur "*Suivant*".

![Image](assets/fr/017.webp)

Placez votre Seedkeeper à l’arrière du smartphone.

![Image](assets/fr/018.webp)

Vous accédez alors à la liste de tous vos secrets enregistrés. Dans cet exemple, je veux afficher la seed de mon portefeuille "*Blockstream App*", je clique donc dessus.

![Image](assets/fr/019.webp)

Appuyez sur le bouton "*Révéler*".

![Image](assets/fr/020.webp)

Scannez de nouveau votre Seedkeeper.

![Image](assets/fr/021.webp)

Votre phrase mnémonique précédemment enregistrée s’affiche désormais à l’écran.

![Image](assets/fr/022.webp)

## 7. Faire une sauvegarde du Seedkeeper

Nous allons maintenant réaliser une sauvegarde de mon Seedkeeper sur un second Seedkeeper afin d’en avoir deux exemplaires. Cette redondance peut faire partie d’une stratégie de sécurisation de vos bitcoins : par exemple, stocker votre phrase à deux endroits distincts pour limiter les risques physiques, ou encore en confier une copie à un proche de confiance dans le cadre d’un plan d’héritage.

Pour cela, munissez-vous de votre second Seedkeeper (pensez à identifier l’un des deux avec une marque dessus pour éviter toute confusion). Commencez par l’initialiser en reproduisant le processus de l’étape 4 de ce tutoriel. Choisissez une nouvelle fois un mot de passe fort. Selon votre stratégie, vous pouvez opter pour un mot de passe différent ou conserver le même.

![Image](assets/fr/023.webp)

Ouvrez l’application, cliquez sur "*Click & Scan*", saisissez le mot de passe de votre Seedkeeper n°1 (source), puis scannez-le.

![Image](assets/fr/024.webp)

Vous accédez à sa page d’accueil avec la liste de vos secrets. Cliquez sur les trois petits points en haut à droite de l'interface.

![Image](assets/fr/025.webp)

Sélectionnez "*Faire une sauvegarde*", puis appuyez sur "*Start*".

![Image](assets/fr/026.webp)

Saisissez le code PIN de votre carte de sauvegarde (Seedkeeper n°2).

![Image](assets/fr/027.webp)

Scannez ensuite cette carte.

![Image](assets/fr/028.webp)

Faites de même avec la carte principale (Seedkeeper n°1), puis cliquez sur "*Faire une sauvegarde*".

![Image](assets/fr/029.webp)

Votre Seedkeeper n°2 contient désormais l’intégralité des secrets enregistrés sur le Seedkeeper n°1.

![Image](assets/fr/030.webp)

Vous pouvez scanner votre Seedkeeper n°2 pour vérifier que les secrets ont bien été copiés.

![Image](assets/fr/031.webp)

Voilà ! Vous savez désormais comment utiliser le Seedkeeper pour sauvegarder la phrase mnémonique d’un portefeuille Bitcoin. Dans un prochain tutoriel, nous verrons comment utiliser le Seedkeeper pour stocker vos mots de passe. Je vous invite également à découvrir son usage combiné avec le SeedSigner :

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

Dans ce tutoriel, nous avons mentionné à plusieurs reprises les ***Descriptors*** de votre portefeuille Bitcoin. Vous ne savez pas de quoi il s’agit ? Dans ce cas, je vous recommande de suivre notre formation gratuite CYP 201, qui détaille en profondeur tous les mécanismes de fonctionnement des portefeuilles HD !

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


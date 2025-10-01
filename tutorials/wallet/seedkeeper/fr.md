---
name: Seedkeeper
description: Comment sauvegarder votre wallet Bitcoin avec la carte à puce Seedkeeper ?
---

![cover](assets/cover.webp)

Le Seedkeeper est une carte à puce développée par Satochip, une entreprise belge spécialisée dans les solutions matérielles pour la gestion et la protection des secrets numériques. Reconnue pour sa gamme de smartcards destinées à l’écosystème Bitcoin, Satochip a conçu le Seedkeeper comme une alternative aux méthodes traditionnelles de conservation de phrases mnémoniques.

Concrètement, le Seedkeeper prend la forme d’une carte à puce multifonctionnelle, certifiée EAL6, dotée d’un processeur sécurisé et d’une mémoire inviolable (c'est donc ce que l'on appelle un "*Secure Element*"). Comme son nom l'indique, son rôle est de stocker de manière chiffrée et protégée des phrases mnémoniques de portefeuilles Bitcoin ainsi que des mots de passe. Avec le Seedkeeper, vous pouvez générer, importer, organiser et sauvegarder vos secrets directement dans le composant sécurisé de la carte.

Le Seedkeeper répond donc selon moi à deux cas d’utilisation principaux que nous étudierons en 2 tutoriels distincs :
- **La conservation de phrases mnémoniques Bitcoin** : au lieu de noter vos 12 ou 24 mots sur un support papier, vous pouvez les importer dans la smartcard et les protéger par un code PIN.
- **La gestion de mots de passe** : vous pouvez générer des mots de passe forts via l’application Seedkeeper et les stocker directement dans la smartcard, ce qui donne un gestionnaire de mot de passe sécurisé hors ligne pratique et facile à utiliser.

Sur le plan technique, le Seedkeeper offre une capacité de 8192 octets, ce qui permet de stocker au minimum 50 secrets distincts (le nombre exact dépendra de leur taille et des métadonnées associées à chacun). L’accès au Seedkeeper se fait soit [par lecteur de carte à puce relié](https://satochip.io/accessories/) à un ordinateur, soit via l’application mobile avec connexion NFC. Le tout fonctionne en mode hors ligne, sans connexion Internet, ce qui garantit une surface d’attaque limitée.

Une fonctionnalité particulièrement intéressante est la possibilité de dupliquer le contenu d’un Seedkeeper vers un autre afin de créer une sauvegarde. Nous allons voir dans ce tutoriel comment faire cette manipulation.

Le SeedKeeper est également très intéressant lorsqu’il est associé à un hardware wallet stateless comme le SeedSigner ou le Specter DIY. Dans ce cas, il n’est pas nécessaire d’utiliser le client de Satochip sur ordinateur ou mobile. Le Seedkeeper conserve la seed dans son élément sécurisé et peut être utilisé directement avec le périphérique de signature, ce qui évite d’avoir recours à un QR code papier. Je ne développerai pas ce cas d’usage particulier dans ce tutoriel, puisqu’il fait l’objet d’un autre tutoriel dédié :

https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## Quel cas d'usage pour le Seedkeeper ?

Ici, je traite uniquement des cas d’usage liés à Bitcoin, car c’est le sujet de ce tutoriel. Nous n’aborderons donc pas la fonctionnalité de gestion des mots de passe, qui fera l’objet d’un autre tutoriel.

Comparé à une simple sauvegarde papier de la phrase mnémonique, l’utilisation d’un Seedkeeper présente plusieurs avantages :

- **Résistance au vol :** la seed de votre portefeuille n’est pas accessible en clair. Pour l’extraire, il faut connaître le PIN du Seedkeeper. Un voleur qui s’emparerait de l’appareil ne pourra rien en faire sans ce code.

- **Diffusion du risque sur deux facteurs :** vous pouvez répartir la sécurité entre un facteur numérique et un facteur physique. Par exemple, si vous stockez le PIN du SeedKeeper dans votre gestionnaire de mots de passe, il faudra à la fois accéder à ce gestionnaire et posséder la smartcard physiquement pour obtenir la seed (une probabilité d’attaque nettement réduite).

- **Gestion centralisée :** le SeedKeeper facilite la gestion de plusieurs seeds de différents portefeuilles.

- **Sauvegardes faciles :** il permet de dupliquer simplement des sauvegardes chiffrées vers d’autres SeedKeepers.

Cependant, certains inconvénients méritent d’être soulignés par rapport à une simple sauvegarde papier de votre seed :

- **Le prix :** bien que modeste (environ 25 €), il reste supérieur à celui d’une feuille de papier.

- **La dépendance à un appareil informatique généraliste :** la saisie et la gestion de la seed nécessitent un ordinateur ou un smartphone, ce qui implique que votre phrase mnémonique transite par une machine avec une surface d’attaque bien plus large qu’un hardware wallet. Cela peut représenter un risque en cas de compromission du poste. C’est pourquoi je déconseille l’usage du SeedKeeper pour stocker la seed d’un hardware wallet (sauf dans un usage stateless sans ordinateur, comme avec le SeedSigner). Le rôle du hardware wallet est précisément de conserver la seed dans un environnement minimaliste et hautement sécurisé. En saisissant manuellement votre seed sur votre ordinateur habituel, elle n’est plus confinée au hardware wallet : elle se retrouve également sur une machine généraliste, exposée à de multiples vecteurs d’attaque. Il vaut donc mieux utiliser le Seedkeeper pour un portefeuille chaud plutôt que pour un portefeuille froid (sauf SeedSigner / stateless hardware wallet).

- **Le risque de perte lié au PIN :** l’inaccessibilité directe de la seed, contrairement à une sauvegarde papier, constitue effectivement une protection face aux vols physiques. Mais comme toujours, la sécurité repose sur un équilibre entre risque de vol et risque de perte. Si votre sauvegarde nécessite un PIN, la perte de ce code rendra impossible la récupération de votre phrase mnémonique, et donc l’accès à vos bitcoins.

Au regard de ces avantages et inconvénients, je considère que les meilleures utilisations du SeedKeeper (en dehors de sa fonction de gestionnaire de mots de passe) sont, d’une part, le stockage des seeds de vos **portefeuilles logiciels**, puisqu’elles résident déjà sur votre téléphone ou votre ordinateur, et d’autre part, l’usage en combinaison avec un hardware wallet stateless comme le SeedSigner, où il prend tout son sens.

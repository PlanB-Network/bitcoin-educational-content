---
term: PHRASE DE RÉCUPÉRATION
---

Une phrase de récupération, également parfois nommée mnémonique, seed phrase, ou phrase secrète, est une séquence composée habituellement de 12 ou de 24 mots, qui est générée de manière pseudo-aléatoire à partir d'une source d'entropie. La séquence pseudo-aléatoire est toujours complétée d'une somme de contrôle (checksum). La phrase mnémonique, conjointement avec une passphrase optionnelle, est utilisée pour dériver de façon déterministe l'intégralité des clés associées à un portefeuille HD (déterministe et hiérarchique). Cela signifie qu’à partir de cette phrase, il est possible de générer et de recréer déterministiquement l'ensemble des clés privées et publiques du portefeuille Bitcoin, et par conséquent d'accéder aux fonds qui y sont associés. La raison d'être de la phrase de récupération est de fournir un moyen de sauvegarde et de récupération des bitcoins qui est à la fois sécurisé et facile à utiliser.

Il est important de conserver cette phrase en lieu sûr et de manière sécurisée, car toute personne en possession de la mnémonique aurait accès aux fonds du portefeuille correspondant. Si elle est utilisée dans le cadre d’un portefeuille classique, et sans passphrase optionnelle, elle constitue souvent un SPOF (point de défaillance unique). La phrase de récupération est donc un encodage de la séquence pseudo-aléatoire et de la checksum dans des mots du quotidien afin de faciliter sa notation et sa lisibilité par l’Homme. Elle est construite en fonction du standard BIP39, qui défini et ordonne une liste de 2048 mots utilisés pour cet encodage.

> ► *La liste de 2048 mots du BIP39 est disponible dans plusieurs langues, toutefois, il est conseillé d'utiliser uniquement la version anglaise, car c'est la version la plus largement prise en charge par les logiciels de portefeuille.*


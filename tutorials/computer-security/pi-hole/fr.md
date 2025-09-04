---
name: Pi-Hole
description: Un bloqueur de pubs pour tout votre réseau
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Florian Duchemin publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont pu être apportées au texte original.*

___

## I. Présentation

On a tous fait cela dès le démarrage de notre navigateur favori : installer un **adblocker** (bloqueur de pubs). Par contre, en utilisant le navigateur de la télé ou un appareil Android, etc... C’est un peu plus galère de trouver quelque chose de correct. Et puis, s’il y a plusieurs appareils dans la maison, ben il faut recommencer l’opération et ce, pour chaque navigateur !

Dans ce tutoriel, nous allons donc résoudre une problématique simple **: fournir un bloqueur de publicité à l'ensemble des machines de notre réseau et le gérer de manière centralisée.**

Pour cela, nous allons utiliser un outil développé pour cet usage : **Pi-Hole**

Pi-Hole est un DNS « sinkhole », comprendre « entonnoir ». Il va utiliser les requêtes DNS faites par vos appareils pour valider ou non le trafic et ainsi vous mettre à l’abri des adresses et domaines connus comme diffusant de la pub, des malwares, etc.

Pour rappel, DNS veut dire *Domain Name System*, soit système de noms de domaine. Alors qu’est-ce qu’un nom de domaine me direz-vous? Et bien par exemple, « it-connect.fr » en est un exemple. Un nom de domaine est un identifiant unique pour une ou plusieurs ressources, généralement administrées par une seule entité.

Le nom de la machine plus le nom de domaine est appelé FQDN pour *Fully Qualified Domain Name* ou nom de domaine pleinement qualifié. Il permet d’atteindre une machine précise juste en « l’appelant ». Par exemple, lorsque vous tapez « www.trucmachin.com », vous appelez en faite la machine « www » qui appartient au domaine « trucmachin.com ».

Sauf que nos ordinateurs eux ne comprennent pas le langage des humains, tout ce qu’ils comprennent c’est le binaire et il ont donc besoin d’une adresse IP, qui est l’équivalent d’un numéro de téléphone, pour joindre le site Internet.

Donc, à chaque fois que vous entrez le nom d’un site Internet dans votre navigateur, ou que vos cliquez sur un lien, votre ordinateur commence par demander à un serveur DNS l’adresse IP qui correspond à ce nom.

**Pi-Hole va donc inspecter ces demandes (il y en a des centaines par jour!) et automatiquement bloquer celles connues pour héberger des publicités ou même des fichiers malveillants.**

## II. Installation de Pi-Hole

Avec un nom comme Pi-Hole, on peut à juste titre supposer qu’il faut avoir un Raspberry-Pi... Mais ce n’est pas tout à fait vrai. **Pi-Hole peut être installé sur n’importe quel ordinateur Linux (Debian, Fedora, Rocky, Ubuntu, etc.).**

Par contre, il faut garder en tête que **cet appareil devra tourner 24h/24 pour une raison simple : pas de DNS, pas d’Internet !** Le Raspberry est donc une bonne idée puisqu’il ne consomme presque rien en terme d’énergie.

Pour l’installation, rien de plus simple, il suffit de se connecter en SSH à votre machine Linux puis de rentrer la commande suivante en tant que "*root*" :

```
curl -sSL https://install.pi-hole.net | bash
```

> **Note** : en temps normal, il est déconseillé de « piper » un script sans savoir ce qu’il fait au préalable. Si vous n’êtes pas sûr, rendez-vous sur la page avec un navigateur ou téléchargez le contenu dans un fichier.
>
> **Note bis** : sur les version minimales de Debian 11, Curl n'est pas installé, il faut donc le faire manuellement avec la commande **apt-get install curl** avant de taper la commande ci-dessus.

Une fois le script lancé, une série de test sera fait, l'installation en elle-même se fera toute seule :

![Image](assets/fr/019.webp)

Installation de Pi-Hole

Une fois l’installation terminée, vous arriverez à cet écran :

![Image](assets/fr/020.webp)

Écran de démarrage Pi-Hole

> **Note**: si vous êtes en DHCP au niveau de votre machine, vous aurez un message d'avertissement à ce propos. Bien entendu, pour une utilisation dans les règles, il est plus que conseillé d'assigner une IP fixe à votre machine.

Suite à cet écran, vous aurez quelques messages d'informations puis vous arriverez à l'assistant de configuration qui vous demandera dans un premier temps à quel serveur DNS Pi-Hole transmettra les demandes qui transiterons par lui. Pour ma part, je choisi Quad9 qui dispose d'un charte pour le respect de la vie privée des utilisateurs.

![Image](assets/fr/021.webp)

Choix du DNS - Pi-Hole

> **Note** : si vous êtes en entreprise, il y a de fortes chances que le serveur DNS actuel soit le contrôleur de domaine Active Directory. Pas de soucis avec cela, il sera possible par la suite de spécifier à Pi-Hole un redirecteur conditionnel pour un domaine de son choix. Typiquement, vous pourrez rediriger toute demande concernant votre domaine local vers votre serveur DNS.

Vous remarquerez que certains choix disposent d'une option DNSSEC. De base, le protocole DNS n'est pas sécurisé (il n'as pas été conçu avec cette volonté à l'époque), DNSSEC viens résoudre ce problème en apportant une couche de sécurité par le chiffrement et la signature des échanges, vous trouverez toutes les explications sur l'article correspondant : [Sécurité DNS](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)

Un bloqueur de publicité quel qu'il soit se base sur une ou des listes pour faire son travail. De base, Pi-Hole est fourni avec une seule liste, sélectionnez là; vous pourrez en rajouter par la suite.

![Image](assets/fr/022.webp)

Viens la question à propos de l’interface web, son installation est facultative, l'outil disposant de sa propre ligne de commande pour le management et la visualisation. Mais cette interface étant plutôt agréable et bien faite, je vous conseille de l'installer en même temps :

![Image](assets/fr/023.webp)

Si vous installez Pi-Hole sur une machine disposant déjà d'un serveur Web, il est possible de répondre "non" à la question suivante. Attention toutefois, il est nécessaire de disposer de PHP et de plusieurs modules pour que cela soit fonctionnel. Dans le cas contraire, **lighttpd sera installé avec tous les modules nécessaires**.

![Image](assets/fr/024.webp)

On vous demande ensuite si vous souhaitez enregistrer les demandes DNS, là c'est à vous de voir. **Si vous souhaitez garder un historique, alors mettez oui, sinon, le contraire mais vous perdrez une partie des fonctionnalités** (voir écran suivant).

![Image](assets/fr/025.webp)

Pour son interface web, Pi-Hole utilise une fonction de son cru nommée FTLDNS qui fourni une API et génère des statistiques à partir des requêtes DNS. Cette fonction peut inclure un mode "vie privée" qui masquera les domaines demandés, les clients à l'origine de cette demande, ou les deux. Pratique si on veut faire du monitoring sans pour autant empiéter sur la vie privée des personnes ou tout simplement si on veut respecter les règlements en la matière dans le cas de l'utilisation pour un réseau public.

![Image](assets/fr/026.webp)

Choix du niveau de vie privée

Une fois cette dernière question répondue, le script va faire ce qu'il doit, à savoir télécharger les dépôts GitHub et configurer Pi-Hole. Au terme de l'installation, un écran récapitulatif s'affichera avec les infos importantes :

![Image](assets/fr/027.webp)

Écran récapitulatif de l'installation

Notez bien le mot de passe pour l'interface web ainsi que les informations réseau. Il faut désormais configurer le service DHCP de l'endroit où nous nous trouvons.

## III. Configuration du DHCP

Pour fonctionner, Pi-Hole a donc besoin de "résoudre" les requêtes DNS des clients, il faut donc que ces derniers puisse savoir que c'est à lui qu'il faut les envoyer. Pour cela, plusieurs solutions :

* Modifier les paramètres DNS dans le serveur DHCP en fonction chez vous (par exemple : votre Box)
* Désactiver ce serveur et utiliser celui fourni par Pi-Hole
* Modifier manuellement chaque appareil pour qu'il utilise Pi-Hole en tant que DNS

Je choisis personnellement la première solution. En effet, **il y a de fortes chances que vous disposiez d'un serveur DHCP là où vous vous trouvez** (généralement, votre box). Inutile donc de s'embêter plus que ça.

Comme il existe un grand nombre de possibilités, entre les différentes box opérateur (que je ne connais pas toutes) et ceux qui ont un routeur perso, je ne vais pas mettre de capture d'écran pour ces modifications. Dans tous les cas, il faudra vous rendre dans les paramètres du DHCP et modifier le paramètre "DNS" pour y mettre l'adresse IP de votre Pi-Hole.

Une fois ceci fait, s'il y a des appareils qui ont été allumés avant, ils auront gardé les anciens paramètres, il faudra donc relancer la demande de configuration.

Sur les postes Windows, avec une invite de commandes :

```
ipconfig /renew
```

Sur un poste Linux :

```
dhclient
```

Pour tout autre appareil, il faudra les éteindre et les rallumer.

Ils devraient donc obtenir les bon paramètres, pour le vérifier :

```
ipconfig /all
```

Vous devriez avoir dans le champ DNS l'adresse de votre Pi-Hole, pour moi 192.168.1.42 :

![Image](assets/fr/029.webp)

## IV. Utilisation de l'interface web Pi-Hole

Pour faciliter son administration, **Pi-Hole** bénéficie d'une interface web plutôt bien faite. Conviviale et accessible, elle vous permet de :

* Visualiser en temps réel le nombre de requêtes, celles qui sont bloquées, etc.
* Gérer votre Whitelist et Blacklist
* Ajouter des entrées statiques, des alias, etc.
* Ajouter des listes
* Et bien d'autres fonctions!

Pour ma part, je vais ajouter une liste de blocage. Comme on l'a vu plus haut, une seule liste a été installée en même temps que le soft. Il existe beaucoup de listes pour les sites de pubs mais il est préférable d'en choisir au moins une spécifique au pays dans lequel on vit. Une des listes les plus connue est **EasyList** et l'une d'entre elle est spécifique à la France : [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)

Pour l'ajouter, il faut tout d'abord se connecter à l'interface admin : **http://<ip_du_PiHole>/admin**

Le mot de passe administrateur a été généré auparavant (voir capture de fin d'installation), il suffit donc de le renseigner pour accéder à l'interface :

![Image](assets/fr/030.webp)

Interface de Pi-Hole

On voit par exemple qu'il y a deux clients connectés au Pi-Hole, que celui-ci a traité 442 demandes et que 8 d'entre elles ont été bloquées. Ces graphiques peuvent être une bonne source d'information, surtout dans un cadre professionnel.

Pour ajouter notre liste, direction le menu "**Group Management**" et "**Adlists**" :

![Image](assets/fr/031.webp)

On voit bien notre première liste "**StevenBlack**", pour ajouter la notre, copiez le lien que je vous ai donné plus haut et insérez-le dans le champ "**Address**", pour la description, je choisis de mettre le nom de la liste :

![Image](assets/fr/032.webp)

Ajouter une liste dans Pi-Hole

Il nous reste plus qu'a cliquer sur "**Add**" pour l'ajouter. Afin de l'activer, il est nécessaire de réaliser une étape supplémentaire pour "avertir" Pi-Hole de prendre en charge cette liste. Pour cela :

* Soit vous utilisez la ligne de commande intégrée
* Soit l'interface web

Je choisis personnellement la deuxième car si vous avez bien observé, le lien vers le script PHP qui réalise la mise à jour est directement sur la page où nous sommes (le mot "online"). Il suffit donc de cliquer dessus, ce qui vous amènera sur une page où seul une option s'offrira à vous :

![Image](assets/fr/033.webp)

La page affichera le résultat du script une fois terminé, ce qui signifiera que la liste a été prise en compte (sauf message d'erreur bien entendu).

Comme annoncé en début de tuto, Pi-Hole permet aussi de **bloquer les domaines connus pour distribuer des malwares, pour renforcer cette fonctionnalité, je vous propose d'ajouter également la  liste de domaine distribuée par Abuse.ch** qui est régulièrement mise à jour, cela renforcera significativement la sécurité de votre réseau, elle est disponible à [cette adresse](https://urlhaus.abuse.ch/downloads/hostfile/).

Vous pouvez bien entendu ajouter toute liste qui vous paraîtrait pertinente ou gérer directement votre Blacklist manuellement dans le menu correspondant.

## V. Tests de Pi-Hole

Maintenant que tout est en place, il suffit de tester la solution pour s'assurer qu'elle fonctionne correctement.

Je vais par exemple tenter de joindre le domaine *http://admin.gentbcn.org/* qui est sur la liste de Abuse.ch car connu comme hébergeant des malwares :

![Image](assets/fr/034.webp)

Visiblement, j'ai été bloqué quelque part, pour s'assurer que c'est bien le Pi-Hole qui a fait le job, nous pouvons consulter le journal de requêtes dans l’interface web "Query Log" pour voir que c'est bien un blocage issu d'une entrée de liste :

![Image](assets/fr/035.webp)

## VI. Conclusion

Nous avons vu dans ce tuto comment mettre en place de manière simple non seulement un serveur DNS qui va éliminer la plupart des publicités pour le confort de navigation, mais aussi ajouter **une couche de sécurité en bloquant les domaines de phishing ou diffusant des malwares**.

Le tout gratuitement et de manière économique si installé sur un Raspberry-Pi (d'un point de vue consommation électrique).

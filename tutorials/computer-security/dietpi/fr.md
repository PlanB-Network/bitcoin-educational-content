---
name: DietPi
description: Système d'exploitation léger optimisé pour les machines peu performantes. Avec une préférence pour l'auto-hébergement
---

![cover](assets/cover.webp)



Dans les cercles non techniques, des marques comme `Odroid`, `Raspberry Pi`, `Orange Pi` ou `Radxa`, sont peu connues. Mais il suffit de se tourner vers les milieux technologiques pour constater que les ordinateurs **SBC** - construits sur une seule carte mère, d'une taille souvent microscopique par rapport aux ordinateurs couramment utilisés - sont devenus indispensables, en tant que support pour tout projet personnel.



Il s'agit d'ordinateurs produits dans une grande variété de modèles. Ils accueillent de préférence des distributions Linux, souvent adaptées pour fonctionner sans problème sur ces machines peu puissantes.



**DietPi ne fait pas exception** : c'est un système d'exploitation basé sur Debian, optimisé pour être aussi léger que possible et rendre très rapide même les `SBC` les moins performants. Passé de Debian12 Bookworm à Debian13 Trixie juste au moment de l'écriture de ce tutoriel, il supporte maintenant aussi les SBC à base de processeurs `RISC-V` open source. DietPi est une découverte agréable qui mérite d'être étudiée plus en détail.



## Points forts



Il ne s'agit pas de la "copie habituelle" de Debian pour les petites cartes de type Raspberry. C'est DietPi :




- Optimisé pour la vitesse et la légèreté** : une [comparaison avec d'autres distributions Debian pour SBC] (https://dietpi.com/blog/?p=888), DietPi est plus léger en tout. L'image ISO de DietPi pèse moins de 1 Go, de loin la plus petite parmi celles dédiées aux anciens modèles de Raspberry ou Orange PI (par exemple). La demande en ressources RAM et CPU est très faible, de sorte qu'il tire toujours le meilleur parti des cartes, même les plus anciennes.
- Automatismes et installateurs intégrés** : Une suite de commandes dédiées aide les utilisateurs à surveiller les ressources du système et à automatiser les tâches d'installation et de lancement des programmes, de mise à jour des versions, de sauvegarde et de vérification de tous les journaux.
- Une communauté forte, orientée vers l'expérimentation** : les [tutoriels] (https://dietpi.com/forum/c/community-tutorials/8) et les projets de la communauté DietPi sont idéaux pour s'inspirer des logiciels que vous pouvez installer en un clic grâce à DietPi.



**Il n'a jamais été aussi facile de tirer le maximum de votre SBC**.



## Automatisations pour l'auto-hébergement


Vous voulez expérimenter avec votre propre serveur pour exécuter des solutions réseau avancées, ou des outils pour développer votre expertise Bitcoin ? DietPi est peut-être la solution que vous recherchez. Bien que de nombreuses personnes sachent comment gérer leur propre infrastructure et faire fonctionner des serveurs parfaitement configurés et protégés, DietPi est une étape appropriée pour ceux qui veulent partir de zéro.



Au lieu d'effectuer manuellement toutes les tâches complexes qu'une telle tâche requiert, DietPi vous permet de les construire avec un `wizard` et sa propre ligne de commande. Ici, vous pouvez expérimenter votre propre nuage personnel, la gestion des appareils _smart home_, les sauvegardes automatisées et la crontab, ainsi que des solutions plus avancées.



![img](assets/en/01.webp)



## Installation



### Télécharger



DietPi propose un grand nombre d'images ISO, pour graver le système d'exploitation sur de nombreux périphériques différents. Certaines ne sont que supportées : l'ISO pour Raspberry PI5 est encore en test, par exemple, mais vous pouvez certainement trouver celle qui convient à votre carte.



Pour ce guide, j'ai choisi de l'installer sur un client léger, donc le choix s'est porté sur _PC/VM_ puis sur _Native PC_. Il existe deux images ISO pour ces périphériques, qui diffèrent par la génération du bootloader. La machine utilisée dans le tutoriel étant assez ancienne, le choix s'est porté sur la version _BIOS/CSM_. Si vous avez une machine plus récente, la version correcte pourrait être l'`UEFI`.



![img](assets/en/02.webp)



Vous arriverez sur la page qui contient l'`image de l'installateur`, le `sha256` et les `Signatures`.



![img](assets/en/03.webp)



Préparez un répertoire dans le `home` de votre ordinateur quotidien, afin de pouvoir télécharger les fichiers nécessaires, avec `wget`.



![img](assets/en/04.webp)



La clé publique du développeur a nécessité un minimum de recherche, mais vous pouvez la trouver à ce lien : https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Vérifiez le contenu du répertoire avec `ls -la` et importez la clé MichaIng dans votre trousseau, avec `gpg --import`.



### Vérification et flash



Enfin, la partie que je recommande le plus : vérifiez l'authenticité du système d'exploitation que vous avez téléchargé et que vous êtes sur le point d'installer sur votre SBC.



![img](assets/en/06.webp)



Si vous avez également obtenu le résultat `Good signature` et le même contrôle Hash avec la commande sha256sum, vous pouvez procéder au flashage de l'ISO sur une clé USB. Utilisez des applications comme Whale Etcher pour le faire.



![img](assets/en/07.webp)



## Installation de DietPi



![img](assets/en/09.webp)



Transférez la clé USB sur l'appareil qui hébergera DietPi et commencez l'installation du système d'exploitation lime Green. Dans cet exercice, nous utilisons un client léger avec 16 Go de RAM, un SSD de 128 Go pour le système d'exploitation et un second disque de données de 1 To. L'installation a pris moins de 30 minutes, mais si vous utilisez un Raspberry, par exemple, les ressources peuvent être moindres et prendre plus de temps. La progression de l'installation est affichée pendant l'installation.



![img](assets/en/08.webp)



Conçu pour les Raspberries et autres, la vraie nature de DietPi est l'installation dite "headless", sans environnement graphique et avec un accès natif à `shsh'. Dans le guide, vous verrez plutôt un environnement graphique, LXDE pour être précis.



Au cours de cette étape, il vous sera également demandé de choisir le navigateur web que vous souhaitez utiliser par défaut, entre Chromium et Firefox. Les deux fonctionnent bien ; il n'y a pas de contre-indication particulière à l'un ou à l'autre, si ce n'est votre préférence personnelle.



Vers la fin, le programme d'installation peut vous demander si vous souhaitez déjà installer des programmes, mais ici **je vous conseille de ne rien précharger**. Vous devez savoir qu'après cette étape, il vous sera demandé de changer les mots de passe par défaut des deux utilisateurs, pour des raisons de sécurité. Plus important encore, il vous sera demandé de **définir le `mot de passe logiciel global (GSP)`**, qui garantira l'accès aux différents logiciels de manière contrôlée. **Si vous téléchargez un logiciel pendant l'installation du système d'exploitation, sans avoir défini le "GSP", il restera virtuellement inaccessible**. Vous devrez les désinstaller et les réinstaller à nouveau après avoir défini le `Global Software Password` : par conséquent, **ne mettez rien afin d'éviter un double travail**. (L'inconvénient est probable, mais pas certain à 100 %).



L'installation se termine par une demande d'activation de DietPi-Survey, un service automatisé de collecte de données utilisé pour soutenir le développement du système d'exploitation. Selon le site web, la collecte de données est activée lorsque vous téléchargez l'un des logiciels de l'automatisation fournie par DietPi, ou lorsque vous passez à la version suivante. Chacun a la possibilité d'accepter (_Opt IN_) ou de refuser (_Opt OUT_).



![img](assets/en/23.webp)



Une fois l'installation terminée et le redémarrage effectué, le DietPi apparaît à l'écran tel que vous l'avez configuré. Pour le tutoriel, j'ai choisi l'environnement graphique `LXDE`. Sur le bureau, j'ai trouvé le raccourci pour lancer `htop` et le terminal ouvert.



![img](assets/en/10.webp)



### "Outils" du système d'exploitation



Oubliez la plupart des programmes que vous utilisez sur votre distribution Linux - DietPi est tellement optimisé que vous en avez oublié beaucoup. En fait, vous devriez installer manuellement un grand nombre de commandes, mais si vous ne faites qu'essayer, résistez à la tentation et mettez les automatismes de DietPi à l'épreuve.



C'est certainement le terminal qui est le premier outil utile pour commencer à utiliser votre nouveau système d'exploitation, et il s'ouvre automatiquement chaque fois que vous l'allumez.



![img](assets/en/11.webp)



Sur l'écran du terminal, vous trouverez une série de commandes précédées de `dietpi-` représentant les [outils] (https://dietpi.com/docs/dietpi_tools/) de ce système d'exploitation :




- `dietpi-launcher` : pour accéder au système d'exploitation, au gestionnaire de fichiers, etc
- `dietpi-Software` : qui représente l'outil avec lequel vous pouvez installer tous les logiciels déjà disponibles dans la suite
- `dietpi-config` : pour accéder aux configurations du système, même les plus avancées.



![img](assets/en/14.webp)



### Sauvegarde



La sauvegarde d'un serveur est une routine que l'administrateur système doit prévoir dès le premier démarrage.



Avec DietPi, il y a la commande `dietpi-Backup`, que je vous recommande d'explorer pour trouver la solution idéale : elle vous permet de mettre en place une sauvegarde régulière, incrémentale ou non selon les applications utilisées, et toutes les options pour personnaliser la routine.



![img](assets/en/22.webp)



Sélectionnez la destination de la sauvegarde, par exemple un autre disque, en lançant `dietpi-Drive_Manager` pour monter le lecteur de destination et l'utiliser pour cette fonction.



## Configuration



L'auto-hébergement est une expérience conseillée à tous, qu'ils soient curieux ou simplement enthousiastes. Cependant, la mise en place et la configuration d'un serveur impliquent des défis technologiques non négligeables. C'est là qu'intervient **la simplicité de DietPi** qui vous permet de configurer un système adapté à vos besoins en quelques étapes simples.



![img](assets/en/24.webp)



Réglages de base et avancés, tous à portée de main dans le seul Interface disponible avec la commande :



``dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-software


```
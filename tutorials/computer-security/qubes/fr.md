---
name: Qubes
description: Un système d'exploitation raisonnablement sûr.
---

![cover](assets/cover.webp)

Qubes OS est un système d’exploitation gratuit et open source pensé pour les utilisateurs qui placent la sécurité au centre de leurs priorités. Sa particularité repose sur une idée simple mais radicale : au lieu de considérer l’ordinateur comme un tout, il découpe son utilisation en compartiments indépendants appelés **_qubes_**.

Chaque qube fonctionne comme un **environnement virtuel isolé**, avec un niveau de confiance et une fonction spécifique. Ainsi, même si une application est compromise, l’attaque reste confinée dans son qube sans affecter le reste du système.

> Si vous êtes sérieux au sujet de la sécurité, Qubes OS est le meilleur système d'exploitation disponible aujourd'hui. - **Edward Snowden**.

L’installation de Qubes OS demande cependant plus de préparation que celle d’un système d’exploitation classique. Elle implique de vérifier certains prérequis matériels, de comprendre les bases de la virtualisation et d’accepter une expérience différente, où chaque tâche du quotidien est pensée dans une logique de séparation. Mais une fois en place, Qubes OS offre un cadre robuste qui redéfinit la manière d’interagir avec son ordinateur au quotidien. Dans ce tutoriel, nous vous expliquons comment fonctionne Qubes OS et comment l'installer facilement sur votre système.

## Comment fonctionne Qubes OS ?

Qubes OS repose sur le principe de la compartimentation. Plutôt que d'utiliser un système unique, il s'appuie sur l'hyperviseur **Xen** pour créer des machines virtuelles isolées, appelées qubes. Chaque qube est dédié à une tâche spécifique ou à un niveau de confiance précis (travail, navigation personnelle, opérations bancaires, etc.). Cette séparation garantit qu'une éventuelle compromission dans un qube ne peut pas se propager aux autres, agissant comme plusieurs ordinateurs indépendants au sein d'une seule machine.

L'interface utilisateur est gérée par un domaine central et sécurisé nommé **dom0**. Ce domaine est totalement isolé d'Internet, ce qui en fait le cœur du système. Bien que les fenêtres et les menus soient affichés par dom0, l'exécution réelle des applications se fait dans leurs qubes respectifs.

## Les différents types de qubes

Autour de dom0 gravitent différents types de qubes, qui assurent chacun un rôle bien précis.

- Les **AppVM** sont utilisées pour exécuter les applications du quotidien: l’utilisateur peut ainsi séparer ses courriels professionnels de sa navigation web ou de ses activités bancaires, chaque environnement restant totalement indépendant des autres.

- Ces AppVM reposent elles-mêmes sur des **TemplateVM**, qui servent de modèles centralisés pour installer et mettre à jour les logiciels, ce qui évite d’avoir à gérer chaque qube séparément.

Qubes OS intègre également des machines virtuelles spécialisées dans les **services système**.

- Les **NetVM** gèrent directement les **périphériques réseau** et assurent la connexion à Internet. Elles sont souvent associées à des **FirewallVM**, qui s’interposent pour **filtrer le trafic** et limiter l’exposition des autres qubes.

- Les **ServiceVM** jouent un rôle similaire, par exemple pour la gestion des périphériques USB, toujours avec la même logique : isoler les composants les plus risqués afin de réduire la surface d’attaque.

Enfin, pour les tâches ponctuelles ou risquées, Qubes OS propose des **DisposableVM**. Ces qubes éphémères sont créés à la volée pour **ouvrir un document suspect** ou **visiter un site douteux**, puis disparaissent complètement à leur fermeture, effaçant toutes les traces et empêchant toute attaque persistante.

### Le mécanisme de copie sécurisée (qrexec)

Les échanges entre qubes s’appuient sur **qrexec**, un système de communication inter-VM conçu pour la sécurité. Au lieu de laisser les qubes dialoguer librement, qrexec impose des **politiques précises** : un fichier copié d’une AppVM vers une autre, ou du texte transféré via le presse-papier, passe toujours par un canal surveillé et validé par le système. Ainsi, même le simple fait de copier-coller est encadré pour éviter la propagation de logiciels malveillants.

### Gestion des disques

Qubes OS utilise un système ingénieux pour la gestion du stockage. Les TemplateVM contiennent la base logicielle commune, tandis que les AppVM n’ajoutent que leurs données personnelles et leurs fichiers spécifiques. Cela permet de réduire l’espace disque utilisé et de faciliter les mises à jour globales. Les DisposableVM, quant à elles, utilisent des volumes temporaires qui disparaissent complètement à leur fermeture. Ce modèle garantit non seulement une meilleure sécurité, mais aussi une gestion efficace des ressources.

## Pourquoi choisir Qubes OS ?

Les avantages de Qubes OS reposent avant tout sur son modèle de sécurité unique. Au cœur de cette approche se trouve la compartimentation, qui protège l’utilisateur en isolant chaque tâche dans des machines virtuelles distinctes. Concrètement, un e-mail infecté ou un site web malveillant ne peut compromettre qu’un seul qube, laissant le reste du système et vos données personnelles totalement protégés. Cette architecture limite considérablement les attaques complexes qui, sur un système classique, pourraient se propager librement.

Qubes OS offre également une transparence et un contrôle total sur votre environnement numérique. Vous savez exactement quel logiciel a accès à quelle ressource, qu’il s’agisse du réseau, d’un périphérique USB ou d’autres composants sensibles. Le système intègre par défaut des fonctionnalités de sécurité avancées, telles que le chiffrement complet du disque, et facilite l’utilisation de services d’anonymat comme sur le système d'exploitation Whonix.

https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Plutôt que de chercher à créer un système impénétrable, Qubes OS mise sur la résilience : il encapsule les dommages en cas de compromission, réduisant les risques pour le reste du système. Cette approche pragmatique fait de Qubes OS, un choix privilégié pour les utilisateurs ayant des besoins de sécurité élevés ou souhaitant garder un contrôle maximal sur leur vie numérique.

## Installation de Qubes OS 

Avant d’installer Qubes OS, il est essentiel de s’assurer que votre matériel répond aux exigences minimales, car le système repose sur la virtualisation pour isoler les qubes. Les composants principaux à vérifier sont :
- Le **Processeur** : Un processeur 64 bits compatible avec la virtualisation matérielle (Intel VT-x ou AMD-V).
- La **mémoire vive (RAM)** : un minimum de 8 Go est requis, mais nous vous recommandons une RAM de 16 Go ou plus pour faire tourner simultanément plusieurs qubes.
- L’**espace de stockage** : de 36 Go minimum et idéalement de 128 Go sur un disque SSD pour des performances optimales.

Pour installer Qubes OS,  téléchargez l’image ISO officielle depuis le [site officiel](https://www.qubes-os.org/downloads/) de Qubes OS. Il est essentiel de vérifier l’intégrité de l’ISO à l’aide des signatures GPG fournies, afin de s’assurer que le fichier n’a pas été altéré et que le téléchargement est sécurisé.

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)

Une fois l’ISO vérifiée, vous devez créer un support d’installation bootable, généralement une clé USB. Pour cela, téléchargez et installez un logiciel comme **Rufus** sous Windows ou **Etcher** sur Windows, Linux ou macOS. Ces outils permettent de copier correctement l’ISO sur la clé USB pour qu’elle soit amorçable.

Avant de lancer l’installation, il est nécessaire de configurer le **BIOS ou l’UEFI** de votre ordinateur pour **activer la virtualisation** et permettre le boot depuis USB. Selon le modèle de votre machine, il peut être nécessaire de **désactiver le Secure Boot**, car Qubes OS risque de ne pas démarrer avec cette option activée.

![0_02](assets/fr/02.webp)

Une fois ces conditions remplies, redémarrez votre ordinateur et accédez au BIOS/UEFI en appuyant immédiatement sur **Esc**, **Del**, **F9**, **F10**, **F11** ou **F12** (selon le fabricant). Dans le menu de démarrage, sélectionnez la clé USB comme périphérique de démarrage pour lancer l’installation de Qubes OS.

**Écran de démarrage**  
Au démarrage depuis la clé USB, vous arrivez directement sur le menu **GRUB**, qui vous permet de choisir l’action à effectuer. À l’aide des touches directionnelles de votre clavier, sélectionnez "Installer Qubes OS" et validez avec la touche "Entrée".

![0_03](assets/fr/03.webp)

**Choix de la langue** :

Lorsque l’installation démarre, la première étape consiste à **choisir la langue** et la **variante régionale** adaptée à votre configuration. Cela permet d’afficher correctement le système et les options d’installation dans votre langue préférée.

![0_04](assets/fr/04.webp)

**Configuration des paramètres** :

À cette étape, vous devez configurer différents éléments avant de lancer l’installation sur votre machine.

![0_05](assets/fr/05.webp)

**Disposition du clavier** :

Cliquez sur l’option **Clavier**, puis sélectionnez la **disposition adaptée** à votre ordinateur. Une fois votre choix effectué, cliquez sur **Terminé** pour passer à l’étape suivante.

**Choix de la destination** :

Sélectionnez l’option "Destination de l’installation" pour choisir le disque sur lequel vous souhaitez installer Qubes OS. Par défaut, le partitionnement se fait automatiquement, ce qui permet de supprimer toutes les données du disque et d’installer le système dessus. Vous pouvez cependant choisir l’option **Personnalisé** ou **Personnalisation avancée** pour effectuer un partitionnement sur mesure. Cliquez ensuite sur "Terminé". Le système vous demandera de définir un **mot de passe**, qui sert de couche de sécurité pour chiffrer vos données. Veillez à choisir un mot de passe complexe et unique.

![0_06](assets/fr/06.webp)

![0_07](assets/fr/07.webp)

**Choix du format de la date et de l’heure** :
Cliquez sur l’option Heure et date, puis sélectionnez votre zone géographique. Vous pouvez également choisir le format de l’heure : 24h ou 12h selon votre préférence.

![0_08](assets/fr/08.webp)

**Création du compte utilisateur** :
Cliquez sur **Création d’utilisateur** pour créer votre **premier compte**, qui vous permettra de vous connecter à Qubes OS. 

![0_09](assets/fr/09.webp)

**Activation du compte root** :
Vous pouvez également **activer le compte root** en définissant un mot de passe séparé pour l’administration.

![0_10](assets/fr/10.webp)

Une fois ces différents réglages effectués, cliquez sur **Démarrer l’installation** pour lancer le processus. 

![0_11](assets/fr/11.webp)

Patientez jusqu’à la **fin de l’installation**, puis cliquez sur **Redémarrer le système** pour finaliser l’installation et démarrer Qubes OS.

![0_12](assets/fr/12.webp)

**Configuration supplémentaire** :
Après le redémarrage, Qubes OS vous propose de finaliser la **configuration des templates et des qubes par défaut**. Entrez le mot de passe défini pour chiffrer le disque.

![0_13](assets/fr/13.webp)

Ensuite, commencez par sélectionner les **TemplateVM** que vous souhaitez installer. Les options courantes incluent **Debian 12 Xfce**, **Fedora 41 Xfce** et **Whonix 17**, la dernière étant recommandée pour les usages nécessitant **l’anonymat et la sécurité réseau**. Vous pouvez également définir le **template par défaut**, qui servira de base pour la création de nouvelles **AppVM**.

![0_14](assets/fr/14.webp)

Dans la section **Configuration principale**, vous pouvez choisir de créer automatiquement les qubes système essentiels comme **sys-net**, **sys-firewall** et **default DisposableVM**. Il est conseillé d’activer l’option pour rendre **sys-firewall et sys-usb jetables**, afin de limiter l’exposition des périphériques et du réseau en cas de compromis. Vous pouvez également créer les **AppVM par défaut**, comme **personal**, **work**, **untrusted** et **vault**, pour organiser vos activités selon leur niveau de confiance.

![0_15](assets/fr/15.webp)

Qubes OS propose en outre de créer un **qube dédié aux périphériques USB** (sys-usb) et de configurer **Whonix Gateway et Workstation qubes** pour sécuriser vos communications via le réseau Tor. Pour les utilisateurs avancés, la section **Configuration avancée** permet de créer un **pool LVM thin** pour gérer efficacement l’espace disque entre les qubes.

Une fois toutes ces options configurées, cliquez sur **Terminé**, puis sur **Finir la configuration**. Patientez pendant que le système applique ces réglages. Vous serez ensuite invité à vous **connecter à votre compte utilisateur**, et votre environnement Qubes OS sera prêt à l’usage, sécurisé et correctement isolé pour vos différentes activités.

![0_17](assets/fr/17.webp)

Votre système d'exploitation est maintenant installé et prêt à être utilisé.

![0_18](assets/fr/18.webp)

## Créez un qube sur votre système 

Pour créer un qube, le processus est géré par l'outil **Qube Manager**, accessible depuis le menu Démarrer. Dans la fenêtre de cet outil, il vous suffit de cliquer sur l'icône **Créer un qube** pour ouvrir une nouvelle fenêtre de configuration. Vous y renseignerez d'abord un nom pour votre qube, comme "perso-web" ou "travail", pour identifier son usage. 

Ensuite, vous sélectionnerez son **Type**, généralement **AppVM** pour les tâches courantes, ou **DisposableVM** pour une utilisation temporaire. Il est crucial de choisir le **Template** sur lequel votre qube sera basé, comme "fedora-39" ou "debian-12", car c'est lui qui fournira le système d'exploitation et les logiciels. Vous désignerez également la **NetVM**, qui est la qube responsable de l'accès à Internet, par défaut **sys-firewall**. 

Enfin, après avoir ajusté la taille du stockage et la mémoire vive si nécessaire, un simple clic sur **OK** lancera la création. Une fois le processus terminé, votre nouveau qube sera visible dans la liste et prêt à l'emploi.

En conclusion, Qubes OS n'est pas un système d'exploitation ordinaire, mais une solution de sécurité de pointe qui repense l'architecture d'un ordinateur personnel. Son approche basée sur la compartimentation et l'isolation par la virtualisation offre une protection inégalée contre les menaces les plus sophistiquées. En segmentant l'environnement de travail en qubes spécialisés pour chaque tâche, il garantit qu'un logiciel malveillant ne peut pas se propager et mettre en danger l'ensemble du système.

Que ce soit pour naviguer sur Internet de façon sécurisée, protéger vos informations sensibles ou travailler avec différents niveaux de confiance, Qubes OS fournit un cadre résilient et transparent. En adoptant de bonnes pratiques et en exploitant pleinement ses fonctionnalités, vous disposerez d’une **forteresse numérique** adaptée aux menaces modernes. Découvrez notre cursus sur la protection de ses données et de sa confidentialité.

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1




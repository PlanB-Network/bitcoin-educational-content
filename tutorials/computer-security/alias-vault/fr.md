---
name: Alias Vault
description: Outil puissant pour gérer les mots de passe, l'authentification à deux facteurs et les alias (avec serveur de messagerie intégré) - Egalement auto-hébergé !
---

![cover](assets/cover.webp)



La protection de la vie privée et la sécurité en ligne est un sujet auquel toute personne, quelle que soit son activité, doit prêter attention.



Ces questions s'inscrivent en outre dans un monde en constante ébullition : de plus en plus de développeurs participent au sujet, apportant des implémentations à des solutions établies et à de nouveaux produits.



C'est le cas de **Leendert de Borst** et de son `Alias Vault`, un outil révolutionnaire (le premier du genre) qui vous permet de gérer et de stocker des mots de passe, d'utiliser des enregistrements de mots de passe pour s'authentifier à des services web, d'administrer l'authentification à deux facteurs, mais surtout generate de véritables _aliases_, le tout dans un seul Interface.



**Mais Alias Vault ne s'arrête pas là**.



## Caractéristiques principales



Alias Vault fonctionne dans le cloud sur les serveurs du développeur ou en auto-hébergement dans sa propre infrastructure, une option pour laquelle des fichiers et une image Docker sont disponibles pour être installés avec un scipt. En plus du Interface web, des extensions sont disponibles pour tous les navigateurs populaires, ainsi que des applications mobiles pour iOS et Android ; ces dernières peuvent également être téléchargées à partir de F-Droid, en contournant le magasin officiel de Google.



Dans une Interface Alias Vault est :




- Libre et gratuit**
- Password Manager**, pour stocker tous les mots de passe complexes. En utilisant l'extension du navigateur, le gestionnaire de mots de passe complète les connexions aux sites web
- 2FA**, pour prendre en charge l'authentification à deux facteurs
- Gestionnaire d'alias avec serveur de messagerie intégré** : Alias Vault ne crée pas d'alias qui transfèrent les courriels vers la boîte aux lettres d'un utilisateur ; il crée plutôt de véritables alter-egos, avec prénom, nom, sexe, nom d'utilisateur, mot de passe et date d'anniversaire (si ces informations sont requises).



Une documentation complète et détaillée fait partie du paquet, qui accompagnera les nouveaux venus dans la découverte de cet outil puissant.



## Pas de données personnelles !



Tout commence, comme toujours, par le site web [aliasvault.net](aliasvault.net). Comme indiqué, Alias Vault peut être utilisé sur son propre serveur ou à partir du nuage du développeur pour se familiariser avec lui avant de passer à la solution auto-hébergée.



Le site présente des graphismes très attrayants et bien entretenus, mais les bonnes choses viennent lorsque vous commencez à mettre la main à la pâte : **créer votre compte**.



![img](assets/en/01.webp)



À votre grande surprise, vous constaterez qu'Alias Vault ne demande pas d'informations personnelles : tout ce dont vous avez besoin pour créer le compte est un surnom quelconque, un mot qui vous est familier, pour autant qu'il soit disponible. Acceptez les conditions d'utilisation, choisissez le mot et continuez.



![img](assets/en/02.webp)



Définissez maintenant le **mot de passe principal**, qui est l'information la plus importante de tout votre nouveau système. Avec ce mot de passe, en fait, vous serez le seul à pouvoir accéder au compte ou à le récupérer, car il gardera votre `vault` crypté sur le serveur qui hébergera vos informations.



![img](assets/en/03.webp)



Fait : Vous avez créé votre propre gestionnaire de mots de passe et d'alias, mais sans donner votre propre adresse électronique privée Address.



![img](assets/en/04.webp)



Alias Vault vous souhaite la bienvenue dans un espace sûr, nouveau, personnel mais aussi vide. Et maintenant, nous commençons à le peupler un peu.



Si vous disposez déjà d'un gestionnaire de mots de passe, vous pouvez importer le fichier de celui que vous utilisez, afin d'évaluer les différences avec d'autres fournisseurs, ou peut-être éliminer le gestionnaire d'alias afin de tout gérer dans une seule application.



![img](assets/en/05.webp)



Alias Vault est extrêmement simple : vous avez une page principale, qui est le `Home`, avec deux menus :




- `Credentials` : qui vous permet de créer et de gérer des identités et des alias
- `Email` : une boîte de réception où vous pouvez vérifier les messages entrants pour les alias que vous avez générés.



![img](assets/en/06.webp)



C'est la création d'un premier `alias` qui nous intéresse, donc allez en haut à droite de la page et cliquez sur _+Nouvel Alias_.



![img](assets/en/07.webp)



Au départ, le menu semble minimal, conformément à la philosophie d'Alias Vault. Pour découvrir les fonctionnalités de cette fonction, cliquez sur _Create via advanced mode_.



![img](assets/en/08.webp)



La partie supérieure du premier écran vous permet d'importer les mots de passe que vous utilisez déjà pour les services auxquels vous êtes abonné ou que vous utilisez le plus souvent en ligne.



Si vous avez activé l'authentification à deux facteurs sur l'un des services ci-dessus (ou sur tous), Alias Vault vous permet également de gérer ce Layer de sécurité supplémentaire en important la "clé secrète". Alias Vault créera le `TOTP` requis pour l'accès.



![img](assets/en/09.webp)



**Attention** : Dans l'espace réservé à l'email Address, Alias Vault propose par défaut son propre domaine ; afin d'utiliser le bon Address avec lequel vous avez précédemment créé des comptes, cliquez sur _Enter custom domain_, afin de pouvoir définir le bon domaine après `@`.



![img](assets/en/14.webp)



La partie inférieure de cet écran est la plus amusante. Cliquez sur _Generate Random Alias_ et Alias Vault créera pour vous des identités distinctes pour différents besoins, chacune avec sa propre boîte aux lettres, des mots de passe de niveau très robuste, complétés par d'autres détails tels que le sexe, la date de naissance et un surnom approprié.



![img](assets/en/10.webp)



À partir d'un menu approprié, vous pouvez modifier les paramètres qui affectent la génération du mot de passe, par exemple en choisissant uniquement des lettres minuscules et en éliminant les caractères qui peuvent être ambigus.



![img](assets/en/11.webp)



Vous pouvez utiliser l'alias suggéré par Alias Vault, ou changer de domaine en cliquant sur le menu déroulant correspondant.



![img](assets/en/12.webp)



Avant d'utiliser ce courrier électronique pour un service de connexion, vous pouvez tester sa fonctionnalité en envoyant un message à partir d'un Address de votre choix vers la boîte aux lettres nouvellement créée.



![img](assets/en/13.webp)



**⚠️ ATTENTION** : La réception d'e-mails est possible grâce au serveur intégré d'Alias Vault, mais cela ne vous permet que de recevoir des e-mails et non d'y répondre, ou d'utiliser la boîte aux lettres électronique avec les fonctions "conventionnelles" d'un service `alias`. Il est donc très différent de Simple Login, Addy et d'autres plateformes dédiées exclusivement à ce type de service. Pour l'exemple de Simple Login, vous pouvez consulter le tutoriel dédié :



https://planb.academy/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Pour supprimer un alias que vous avez créé à titre de test, il vous suffit de vous connecter à votre `Home`, puis à `Credentials` et de cliquer sur l'identité que vous souhaitez supprimer. La commande _Delete_ apparaîtra dans le coin supérieur droit pour que vous puissiez procéder.



![img](assets/en/16.webp)



## Extension de navigateur



En fonction de vos besoins, vous pouvez recourir à l'extension de navigateur, que l'on trouve sur les navigateurs les plus répandus.



![img](assets/en/15.webp)



Il s'installe comme vous l'avez déjà fait avec toutes les autres extensions, je ne m'attarderai donc pas sur ce détail.



L'extension du navigateur est là pour faciliter la connexion aux services en ligne ou pour créer de nouveaux alias si nécessaire : si le service est stocké dans vos enregistrements Alias Vault, le remplissage automatique fait ce qu'il faut.



![img](assets/en/17.webp)



La seule précaution à prendre est de vérifier qu'Alias Vault est actif. En effet, l'application dispose d'un paramètre par défaut qui lui permet de se mettre en pause après une période d'inactivité. Il s'agit d'une fonction très utile **lorsque vous devez vous éloigner de votre ordinateur, par exemple, et empêcher quelqu'un d'autre d'accéder à vos comptes**. Une procédure simplifiée vous permettra de vous connecter à nouveau en saisissant le "mot de passe principal", si la session précédente est encore dans le cache. Le temps de déconnexion est l'un des paramètres que vous pouvez personnaliser, en le raccourcissant ou en l'allongeant selon vos préférences.



## Application mobile



Comme toute application de ce type qui se respecte, Alias Vault dispose d'une version pour appareils mobiles, tant pour Android que pour iOS. Pour Android, vous pouvez télécharger l'application à partir de [F-Droid] (https://f-droid.org/packages/net.aliasvault.app/).



Au moment où nous écrivons ces lignes (fin août 2025), l'application mobile considère le "remplissage automatique" comme une fonction expérimentale, qui ne fonctionne qu'avec un très petit nombre de sites. Jusqu'à ce qu'elle soit entièrement mise en œuvre, l'utilisation d'Alias Vault sur mobile nécessite un copier/coller des données.



Une fois que vous avez téléchargé l'application depuis le magasin, pour vous connecter, il vous suffit d'entrer l'utilisateur et le "mot de passe principal" créés sur l'application web.



![img](assets/en/18.webp)



Lors de l'ouverture de votre `vault`, il vous sera demandé si vous souhaitez activer l'accès contrôlé par biométrie, un Layer de sécurité supplémentaire pour empêcher quelqu'un d'autre d'accéder à vos mots de passe s'il se trouve en possession de votre téléphone.



![img](assets/en/19.webp)



Si vous décidez de configurer le contrôle biométrique, allez-y. Si vous sautez l'étape et changez d'avis, vous pouvez également le configurer plus tard à partir du menu _Réglages_.



Une fois que vous avez terminé de vous connecter, les données que vous avez déjà créées sont à nouveau synchronisées.



![img](assets/en/20.webp)



L'application mobile peut être acheminée vers le lien vers le "coffre-fort" hébergé sur son propre serveur.



![img](assets/en/22.webp)



Et c'est précisément la version auto-hébergée que nous allons Address, brièvement, dans la section suivante.



## Auto-hébergement : contrôle total de vos données



Alias Vault, pour être juste, n'est pas le premier "gestionnaire de mots de passe" qui vous permet de déployer le service sur votre infrastructure. Il en existe d'autres, mais certains ont des limitations ou sont partiellement fermés.



L'opportunité est unique : **Ne plus dépendre de fournisseurs de services externes ou de nuages, mais utiliser votre propre serveur local pour garder et gérer les mots de passe, les alias et les informations extrêmement sensibles qui y sont associées**. Avec Alias Vault, vous pouvez également faire pointer le service de messagerie vers votre propre serveur de messagerie pour plus de confidentialité.



Il est temps de se tourner vers la [documentation] (https://docs.aliasvault.net/installation/), pour savoir comment procéder à l'auto-hébergement d'Alias Vault.



![img](assets/en/23.webp)



Alias Vault fonctionne sur Docker Compose, une expérience minimale de Linux et de Docker est donc requise. Vous pouvez commencer par l'installation de base, puis compléter avec des solutions plus avancées.



Votre serveur doit fonctionner sur une machine 64 bits, avec une distribution Linux, 1 Go de RAM et au moins 16 Go d'espace de stockage ; la version de Docker (CE) doit être au moins 20.10 ou supérieure, tandis que Docker Compose nécessite une version à partir de 2.0.



J'ai décidé d'essayer Alias Vault avec un client léger, sur lequel DietPi est installé en tant que distribution, une base Debian Bookworm, optimisée à l'essentiel et faisant déjà tourner `Docker` et `Docker Compose`.



Tout d'abord, afin de mettre un peu d'ordre, créez un répertoire dans votre home, ouvrez le `terminal` et collez la commande pour lancer le script d'installation.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Une fois l'installation terminée, vous trouverez vos identifiants d'accès :


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Vérifiez le contenu du répertoire après l'installation.



![img](assets/en/29.webp)



Pour lancer Alias Vault, utilisez la commande :



``` Launch-Alias-Vault


./install.sh start


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Considérations sur le cryptage et la sécurité



![img](assets/en/32.webp)



Selon ce que Lanedirt déclare sur le site, dans la documentation et sur Github, avec Alias Vault **toutes les informations (composants) que vous placez sur Alias Vault, restent étroitement liées à l'appareil, cryptées et inaccessibles à quiconque ne connaît pas le `mot de passe principal`**.



Le "mot de passe principal" est donc l'élément fondamental de l'ensemble du "coffre-fort". Après avoir été saisi, il est traité par l'algorithme `Argon2id`, une fonction de dérivation de clé à mémoire Hard, afin d'empêcher le secret de quitter l'appareil.



Tout reste caché, même au gestionnaire du nuage ou du service d'hébergement. En fait, à partir du panneau d'administration, vous ne pouvez pas accéder aux détails de l'utilisateur, vous pouvez seulement savoir s'il a créé des alias, reçu des courriels, et peu d'autres choses.



Tous les contenus stockés sont cryptés et décryptés par des clés cryptographiques dérivées du "mot de passe principal". **Seules les données cryptées sont stockées sur le serveur, rien n'apparaît en texte clair**. Si un utilisateur oublie ou perd son `mot de passe principal`, le compte lié à ce dernier est irréversiblement perdu, car le serveur ne peut pas accéder au contenu en clair.



Pour la version auto-hébergée, il existe un script pour réinitialiser le "mot de passe principal", mais cela n'empêche pas la perte de données.



![img](assets/en/33.webp)



Alias Vault étant en phase _Beta_, il se peut que vous ayez des difficultés à y accéder si vous changez/mettez à jour le mot de passe principal. Je vous suggère de le choisir robuste et complexe dès le départ afin que vous puissiez expérimenter le service et décider éventuellement de l'utiliser. Si vous avez des difficultés à accéder au nuage après la mise à jour du mot de passe, veuillez contacter le service d'assistance d'Alias Vault.



Pour une compréhension complète de l'architecture et de la sécurité adoptées par Alias Vault, je vous recommande vivement de consulter [cette page] (https://docs.aliasvault.net/architecture/), qui contient des détails sur la cryptographie sous-jacente à son fonctionnement.



## Feuille de route


Les développeurs ont l'intention de rendre Alias Vault mature et stable d'ici à la fin de 2025, afin de définir ses futures caractéristiques d'utilisation.



Alias Vault est et restera toujours open source et gratuit, mais probablement pas de manière illimitée comme dans la version bêta. Certaines fonctionnalités payantes sont en cours d'implémentation, comme elles ont déjà été annoncées.



Il existe des plans d'équipe/famille et une prise en charge des clés matérielles, cette dernière pour l'authentification avec FIDO2 ou WebAuth.



## Qui a besoin d'Alias Vault ?



**Un tel outil est idéal pour tous ceux qui accordent la priorité à la protection de la vie privée en ligne**.



Votre identité est, selon toute vraisemblance, au cœur des activités que vous menez en ligne et doit être protégée par tous les moyens pour mettre **ces** données à l'abri des services, entreprises et courtiers prêts à tout pour mettre la main sur votre comportement en ligne.



Alias Vault vous redonne le contrôle total de vos informations d'identification, en atténuant ou en éliminant complètement la nécessité de faire appel à des tiers pour protéger et crypter vos données les plus sensibles.



L'architecture et la facilité cryptographique d'Alias Vault sont idéales pour les particuliers souverains, les petites et moyennes entreprises, les équipes de développement et tous les amateurs d'applications **open source**. Si vous appartenez à l'une de ces catégories : amusez-vous à découvrir Alias Vault.
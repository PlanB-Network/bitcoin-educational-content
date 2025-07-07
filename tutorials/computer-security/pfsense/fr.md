---
name: pfSense
description: Installation de Pfsense
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Florian BURNEL publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications majeures ont été apportées au texte original de l'auteur pour actualiser son tutoriel.*

___

![Image](assets/fr/027.webp)

## I. Présentation

pfSense est un système d'exploitation libre et open source qui transforme n'importe quel ordinateur, serveur dédié ou appliance matérielle en un routeur et pare-feu performant et hautement configurable. Basé sur FreeBSD, reconnu pour sa stabilité et la robustesse de son architecture réseau, pfSense s'est imposé depuis plus de quinze ans comme une référence dans le domaine des pare-feu open source pour les entreprises, les collectivités comme pour les particuliers exigeants.

Ses fonctionnalités principales ont considérablement évolué et se sont enrichies au fil des versions. À ce jour, pfSense propose notamment :

- Administration complète et centralisée via une interface web moderne, intuitive et sécurisée.
- Pare-feu stateful performant, avec prise en charge avancée du NAT (y compris NAT-T) et gestion granulaire des règles.
- Support natif du multi-WAN, permettant l'agrégation ou la redondance de connexions Internet.
- Serveur DHCP et relais DHCP intégrés.
- Haute disponibilité grâce au protocole CARP pour le failover et la possibilité de configurer des clusters pfSense.
- Répartition de charge (load balancing) entre plusieurs connexions ou serveurs.
- Prise en charge complète de VPN : IPsec, OpenVPN et WireGuard (remplaçant de L2TP, aujourd'hui obsolète).
- Portail captif configurable pour le contrôle d'accès invité, notamment dans les environnements publics ou hôteliers.

pfSense dispose également d'un système de packages extensible qui permet d'ajouter facilement des fonctionnalités avancées, telles qu'un proxy transparent (Squid), un filtrage d'URL ou encore un IDS/IPS (Snort ou Suricata) directement depuis l'interface web.

pfSense est distribué pour plateformes 64 bits uniquement, conformément aux recommandations actuelles de FreeBSD. Il peut être installé sur du matériel standard (PC, serveurs rack) ou sur des plateformes embarquées basse consommation comme les appliances Netgate ou certains boîtiers x86 à faible encombrement, bien plus puissants que les anciens boîtiers Alix.

Enfin, il convient de rappeler que pfSense requiert au minimum deux interfaces réseau physiques : une dédiée à la zone externe (WAN) et une dédiée au réseau interne (LAN). Selon la complexité de votre infrastructure (DMZ, VLAN, multiples WAN), plusieurs interfaces supplémentaires peuvent être nécessaires pour bénéficier pleinement de ses capacités.

## II. Télécharger l'image

La dernière version stable de pfSense, à la date de rédaction de ce tutoriel, est la 2.8 (publiée en juin 2025). Vous pouvez télécharger l'image ISO ou le fichier d'installation adapté à votre environnement matériel directement depuis le site officiel :

* [Télécharger pfSense](https://www.pfsense.org/download/)

Le portail de téléchargement vous permettra de sélectionner :

- L'architecture (généralement **AMD64** pour tout matériel moderne).
- Le type d'image (**Installer USB Memstick** pour une installation via clé USB, **ISO Installer** pour une gravure ou un montage virtuel).
- Le miroir de téléchargement le plus proche géographiquement, pour optimiser la vitesse de transfert.

Pour ceux qui souhaitent déployer pfSense dans un environnement virtualisé (Proxmox, VMware ESXi, VirtualBox...), une image **OVA** est également disponible. Cette machine virtuelle prête à l'emploi simplifie grandement l'installation et la configuration initiale. Veillez simplement à ajuster les ressources allouées (CPU, RAM, interfaces réseau) en fonction de la charge attendue et de votre topologie réseau.

Avant toute installation, il est recommandé de vérifier l'intégrité du fichier téléchargé en contrôlant le **SHA256** fourni sur la page de téléchargement officielle. Cela garantit que l'image n’a pas été altérée ou corrompue.

## III. Installation

Dans cet exemple, l'installation est réalisée sur une machine virtuelle sous VirtualBox. La procédure reste strictement identique sur une machine physique ou tout autre hyperviseur, hormis la gestion des périphériques virtuels.

### 1. Configuration matérielle minimale

Pour un déploiement standard, il est recommandé de prévoir :

- **1 Go de RAM** au minimum (2 Go ou plus sont conseillés pour activer le système de paquets supplémentaires ou le support ZFS).
- **8 Go d’espace disque** (20 Go ou plus sont préférables pour les configurations plus évoluées, notamment si vous installez un proxy cache, un IDS/IPS ou des logs détaillés).
- **Au moins deux interfaces réseau virtuelles** (une pour le WAN, une pour le LAN). Dans VirtualBox, ajoutez-les dans les paramètres de la VM avant le démarrage.

### 2. Démarrage de l’installateur

Montez l’image ISO téléchargée comme lecteur optique virtuel dans VirtualBox ou insérez la clé USB si vous installez sur une machine physique. Au démarrage, un menu de boot s'affiche :

Si vous ne sélectionnez aucune option, pfSense démarrera automatiquement avec les options par défaut après quelques secondes. Appuyez sur la touche "**Enter**" pour lancer le démarrage normal.

![Image](assets/fr/027.webp)

Lorsque le menu principal apparaît, appuyez rapidement sur la touche "**I**" pour initier l'installation.

![Image](assets/fr/001.webp)

### 3. Paramètres initiaux de l’installateur

Le premier écran permet de définir quelques paramètres régionaux comme la police d’affichage et l’encodage des caractères. Ces réglages sont utiles dans des cas spécifiques (claviers non standard, écrans série, langues orientales). Pour la majorité des installations, conservez les valeurs par défaut et sélectionnez "**Accept these Settings**".

![Image](assets/fr/002.webp)

### 4. Choix du mode d’installation

Sélectionnez "**Quick/Easy Install**" pour lancer une installation automatisée avec les options recommandées. Cette méthode efface le disque sélectionné et configure pfSense avec le partitionnement par défaut.

![Image](assets/fr/003.webp)

Un avertissement apparaît pour signaler que toutes les données présentes sur le disque seront supprimées. Confirmez avec "**OK**".

L’installateur copie ensuite les fichiers nécessaires sur le disque. Selon votre matériel, cette étape peut prendre de quelques secondes à quelques minutes.

### 5. Sélection du noyau

Lorsque l’installateur vous invite à choisir le type de noyau, laissez "**Standard Kernel**" sélectionné. Ce noyau générique est parfaitement adapté pour les déploiements classiques, que ce soit sur un PC, un serveur ou une VM.

### 6. Fin de l’installation et redémarrage

Une fois l'installation terminée, choisissez "**Reboot**" pour redémarrer votre machine sur votre nouvelle instance pfSense.

**Remarque importante** : retirez l'image ISO ou déconnectez la clé USB d’installation avant de redémarrer, afin d'éviter de relancer le programme d’installation au prochain boot.

## IV. Premier démarrage de pfSense

Lors du premier démarrage, pfSense doit être configuré pour reconnaître et affecter correctement ses interfaces réseau (WAN, LAN, DMZ, VLANs, etc.). Une identification rigoureuse de vos cartes réseau est indispensable pour éviter toute erreur de configuration qui vous priverait d'accès à l'interface web ou rendrait votre pare-feu inopérant.

Au lancement, pfSense détecte et liste automatiquement toutes les interfaces réseau disponibles, en indiquant pour chacune son adresse MAC. Cela permet de les distinguer clairement.

### 1. VLANs

La première question concerne la configuration de VLANs. À ce stade, pour une configuration de base, nous n’activerons pas de VLANs. Appuyez donc sur la touche "**N**" pour ignorer cette étape.

![Image](assets/fr/004.webp)

### 2. Attribution des interfaces WAN et LAN

pfSense vous invite ensuite à définir quelle interface sera utilisée pour le WAN (accès Internet). Vous avez le choix entre :

- Saisir le nom de l'interface manuellement (méthode recommandée en environnement virtuel).
- Utiliser la détection automatique en appuyant sur "**A**". Cette option est utile sur un hôte physique, à condition que vos câbles réseau soient branchés et que les liens soient actifs.

![Image](assets/fr/005.webp)

Dans cet exemple, nous configurons manuellement le WAN. Saisissez le nom exact de l’interface. Pour une carte Intel, le nom sera souvent "**em0**" sous FreeBSD, mais il peut varier selon le matériel. Par exemple, une carte Realtek s'affichera souvent comme "**re0**".

![Image](assets/fr/006.webp)

Répétez la même opération pour définir l’interface LAN. Ici, nous utilisons "**em1**".

pfSense vous confirme que l’interface LAN active à la fois le pare-feu et le NAT pour protéger votre réseau interne et gérer la translation d'adresses.

Si vous disposez d’autres interfaces physiques, vous pouvez à ce stade configurer des interfaces supplémentaires (DMZ, Wi-Fi, VLANs spécifiques). Chaque interface logique nécessite une carte réseau ou une interface virtuelle correspondante. Pour une configuration initiale, nous nous limiterons au WAN et au LAN.

Une fois les attributions terminées, pfSense affiche un récapitulatif clair des correspondances entre interfaces physiques et rôles attribués. Validez avec "**Y**".

### 3. Console de pfSense

Lorsque cette étape est achevée, le menu principal de la console pfSense apparaît. Il offre plusieurs options utiles pour l’administration directe, comme la réinitialisation du mot de passe web, le redémarrage, le rechargement de la configuration ou la réattribution des interfaces.

![Image](assets/fr/007.webp)

Vous verrez également un résumé des paramètres réseau actuels, notamment l’adresse IP par défaut de l’interface LAN, en général **192.168.1.1**. C’est cette adresse qu’il faudra saisir dans votre navigateur pour accéder à l’interface web d’administration.

**Remarque** : Si votre réseau interne utilise une plage d’adresses différente, sélectionnez l’option "**2)** Set interface(s) IP address" dans le menu pour attribuer une adresse IP adaptée à votre environnement.

Par défaut, si votre interface WAN est connectée à une box ou à un modem configuré en DHCP, pfSense récupérera automatiquement une adresse IP publique. Vous devriez donc bénéficier d’un accès Internet immédiat en branchant un client sur l’interface LAN de pfSense.

## V. Premier accès à l’interface web

Une fois le premier démarrage terminé et les interfaces réseau configurées, vous pouvez accéder à l’interface web de pfSense pour finaliser et affiner votre configuration.

### 1. Connexion initiale

Branchez un ordinateur sur le port LAN (ou l’interface virtuelle LAN dans votre hyperviseur) et attribuez-lui une adresse IP dans la même plage si nécessaire (par défaut, pfSense distribue automatiquement une adresse par DHCP sur le LAN).

Dans votre navigateur, rendez-vous à l’adresse indiquée par la console (par défaut `https://192.168.1.1`). Notez bien que pfSense impose l’utilisation de HTTPS même pour la première connexion — attendez-vous donc à un avertissement de certificat auto-signé, que vous pouvez ignorer en ajoutant une exception.

L’écran de connexion s’affiche. Les identifiants par défaut sont :
- **Nom d’utilisateur :** `admin`
- **Mot de passe :** `pfsense`

Ces identifiants seront modifiés lors de l’assistant de configuration initial.

## VI. Assistant de configuration (Setup Wizard)

Dès la première connexion, pfSense vous invite à suivre son **Setup Wizard**. Il est fortement recommandé de l’utiliser pour s’assurer que tous les paramètres essentiels sont correctement définis.

### 1. Paramètres généraux

Vous pourrez :
- Spécifier un nom d’hôte et un domaine local (exemple : `pfsense` et `lan.local`).
- Définir les serveurs DNS et choisir si pfSense doit utiliser le DNS de votre FAI ou un service externe (Cloudflare, OpenDNS, Quad9...).

### 2. Fuseau horaire

Indiquez le fuseau horaire de votre site pour que les journaux et planifications soient cohérents (`Europe/Paris` par exemple).

### 3. Configuration WAN

Configurez la connexion WAN :
- Par défaut en **DHCP** (suffisant si vous êtes derrière une box).
- Si vous disposez d’une IP fixe, entrez manuellement les paramètres (IP statique, masque, passerelle, DNS).
- Définissez si nécessaire un VLAN ou une authentification PPPoE (courant chez certains ISP).

### 4. Configuration LAN

L’assistant propose de modifier le sous-réseau LAN par défaut. Si vous avez un plan d’adressage spécifique, c’est le moment de l’adapter.

### 5. Changement du mot de passe administrateur

Sécurisez votre pfSense en définissant immédiatement un mot de passe fort pour l’utilisateur `admin`.

## VII. Vérification et mises à jour

Avant de déployer votre pare-feu, vérifiez que vous disposez de la dernière version :

- Rendez-vous dans **System > Update**.
- Sélectionnez le canal de mise à jour (habituellement **Stable**).
- Lancez la vérification des mises à jour et appliquez-les.

Il est conseillé d’activer l’envoi des notifications de mise à jour pour être averti des correctifs de sécurité.

## VIII. Sauvegarde de la configuration

Avant toute modification majeure, mettez en place une politique de sauvegarde :

- Allez dans **Diagnostics > Backup & Restore**.
- Téléchargez une copie de la configuration actuelle (`config.xml`).
- Conservez-la en lieu sûr (support externe chiffré).

Pour les environnements critiques, envisagez de sauvegarder automatiquement la configuration sur un serveur externe ou via un script programmé.

## IX. Bonnes pratiques après installation

Pour terminer votre déploiement sereinement :

- **Modifier les règles du pare-feu** : par défaut, pfSense autorise tout le trafic sortant sur le LAN et bloque le trafic entrant sur le WAN. Ajustez ces règles selon vos besoins.
- **Configurer un accès distant sécurisé** : si nécessaire, activez l’accès à l’interface web depuis le WAN uniquement via VPN ou avec des restrictions IP.
- **Activer les notifications** : configurez un serveur SMTP pour recevoir des alertes (pannes, mises à jour, erreurs).
- **Installer des extensions utiles** : par exemple, un IDS/IPS (Snort, Suricata), un proxy (Squid), un filtrage DNS (pfBlockerNG).

Votre pare-feu pfSense est désormais opérationnel et prêt à protéger votre réseau. Grâce à sa flexibilité et à sa communauté active, vous disposez d’un outil puissant et évolutif qui pourra s’adapter à vos futurs besoins (multi-WAN, VLAN, VPN site-à-site, portail captif, etc.).

Consultez régulièrement la documentation officielle ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) pour découvrir de nouvelles fonctionnalités et vous assurer de maintenir votre configuration à jour et sécurisée.

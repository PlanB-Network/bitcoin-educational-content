---
name: Angry IP Scanner
description: Une façon simple de scanner son réseau
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Florian BURNEL publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont pu être apportées au texte original.*

___

## I. Présentation

Sous Windows, comment scanner un réseau à la recherche des machines connectées de façon simple et rapide ? La réponse s'appelle Angry IP Scanner. Ce projet open source permet de scanner un réseau facilement, à l'aide d'une interface graphique facile à prendre en main.

Cet outil peut être utilisé par un particulier pour **scanner son réseau local**, mais aussi un professionnel de l'informatique dans le même but. Preuve que **cet outil est très pratique**, il a déjà été utilisé par **certains groupes de cybercriminels** pour scanner le réseau des entreprises (au même titre que Nmap). Nous pouvons citer l'exemple du [groupe de ransomware RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Pour autant, c'est un logiciel sain, mais comment d'autres outils orientés réseau et sécurité, son utilisation peut être détournée.

Ici, nous l'utiliserons sur **Windows 11**, mais il est tout à fait possible de l'utiliser sur les autres versions de **Windows**, ainsi que sur **Linux** et **macOS**.

Moins complet que Nmap, **Angry IP** Scanner reste intéressant pour effectuer une analyse rapide et basique d'un réseau, mais aussi parce qu'il est à la portée de tout le monde. Il va permettre de **détecter les hôtes connectés au réseau** et identifier les **noms d'hôtes** et les **ports ouverts**.

Si vous souhaitez aller plus loin, retrouvez le tutoriel sur Nmap :

https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Prise en main d'Angry IP Scanner

### A. Télécharger et installer Angry IP Scanner

Vous pouvez télécharger la dernière version d'Angry IP Scanner à partir du site officiel de l'application ou depuis GitHub. Nous partirons sur cette seconde option. Cliquez sur le lien ci-dessous et téléchargez la version EXE, à savoir ici : "**ipscan-3.9.1-setup.exe**".

* [GitHub d'Angry IP Scanner](https://github.com/angryip/ipscan/releases/latest)

![Image](assets/fr/016.webp)

Lancez l'exécutable afin de procéder à l'installation. Il n'y a rien à effectuer de spécial lors de cette installation.

![Image](assets/fr/013.webp)

### B. Lancer un premier scan du réseau

Au premier lancement, prenez le temps de lire les instructions de la fenêtre "**Getting Started**" pour en savoir plus sur le fonctionnement de l'outil. D'ailleurs, il y a plusieurs termes à prendre en considération :

* **Feeder** : module chargé de générer les listes d'adresse IP à scanner, à partir d'une plage IP, de façon aléatoire ou un fichier avec une liste d'IP.
* **Fetcher** : ensemble de modules pour récupérer des informations sur les hôtes présents sur le réseau. Il y a, par exemple, des fetchers pour détecter les adresses MAC, scanners les ports, détecter le nom d'hôte ou encore envoyer une requête HTTP.

![Image](assets/fr/018.webp)

Pour scanner un sous-réseau IP, indiquez simplement l'**adresse IP de début** et l'**adresse IP de fin**, au niveau du champ "**Plage IP**" (sinon, changez le type sur la droite). Ensuite, cliquez sur le bouton "**Démarrer**".

![Image](assets/fr/019.webp)

Quelques dizaines de secondes plus tard, le résultat sera visible dans l'interface du logiciel. **Pour chaque adresse IP de la plage analysée, vous saurez si Angry IP Scanner a détecté un hôte ou non.** Un résumé s'affiche aussi à l'écran pour indiquer le nombre d'hôtes actifs, ici 6, et le nombre d'hôtes avec des ports ouverts.

![Image](assets/fr/020.webp)

Ici, nous pouvons constater la présence d'un hôte nommé "**OPNsense.local.domain**", associé à l'adresse IP "**192.168.10.1**" et accessibles sur les **ports 80** et **443** (HTTP et HTTPS). Un clic droit sur l'hôte donne accès à des commandes supplémentaires, telles que la possibilité de refaire un ping, un trace route, ou d'ouvrir un navigateur via cette adresse IP.

![Image](assets/fr/012.webp)

### C. Ajouter des ports à scanner

Par défaut, **Angry IP Scanner** va scanner 3 ports : **80** (HTTP), **443** (HTTPS) et **8080**. Vous pouvez ajouter des ports à scanner à partir des préférences de l'application. Cliquez sur le menu "**Outils**" puis sur l'onglet "**Ports**".

Ici, vous pouvez modifier la liste des ports via l'option "**Choix des ports**". Vous pouvez **indiquer des numéros de ports précis séparés par une virgule ou des plages de ports**. L'exemple ci-dessous permet d'ajouter deux ports : **445** (SMB) et **389** (LDAP). Pour scanner les ports de 1 à 1000, indiquez à "**1-1000**". Il n'est pas précisé si les scans de ports sont effectués en TCP, en UDP ou les deux.

![Image](assets/fr/021.webp)

Si vous relancez l'analyse, vous êtes susceptible d'obtenir de nouvelles informations. Dans l'exemple ci-dessous, Angry IP Scanner m'indique que les ports 389 et 445 sont ouverts sur les hôtes "**SRV-ADDS-01**" et "**SRV-ADDS-02**", grâce à la nouvelle configuration des ports à scanner.

![Image](assets/fr/022.webp)

**Remarque** : à partir du menu "**Scanner**", vous pouvez exporter les résultats du scan dans un fichier texte.

Si vous souhaitez approfondir le scan, cliquez sur le menu "**Outils**" puis cliquez sur "**Fetchers**". Ceci permet d'ajouter des "capacités" au scan. Il suffit de sélectionner un fetcher et de le passer à gauche pour l'activer. Cela va ajouter une colonne supplémentaire au résultat du scan.

![Image](assets/fr/014.webp)

L'exemple ci-dessous montre les fetchers "**Info NetBIOS**" et "**Détection Web**". Le premier permet d'avoir des informations en plus comme l'adresse MAC et le nom de domaine de la machine, tandis que le second affiche l'intitulé de la page Web (ce qui peut donner des indications sur le type de serveur web ou d'application).

![Image](assets/fr/011.webp)

Enfin, à partir des préférences, vous pouvez aussi changer la méthode utilisée pour le "**ping**", c'est-à-dire pour considérer si un hôte actif ou non. Étant donné que certains hôtes ne répondent pas aux pings, cela permet de tenter d'autres méthodes (paquet UDP, TCP port probe, ARP, combinaison UDP + TCP, etc.).

## III. Conclusion

Simple et efficace : Angry IP Scanner permet de détecter les hôtes connectés à un réseau, tout en permettant de configurer les scans de ports. Au niveau des options, ce n'est pas aussi flexible qu'un Nmap et ça ne va pas aussi loin, mais c'est déjà un bon début pour effectuer un scan rapidement.

Si vous souhaitez utiliser **Nmap** avec une interface graphique, vous pouvez utiliser **l'application Zenmap** (aperçu ci-dessous).

![Image](assets/fr/015.webp)

https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d
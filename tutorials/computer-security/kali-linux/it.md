---
name: Kali
description: Installazione di Kali Linux su VirtualBox, come chiavetta USB avviabile o come dual boot, passo dopo passo.
---

![cover-kali](assets/cover.webp)



## Introduzione



### Perché Kali Linux?



**Kali Linux** è una distribuzione Linux specializzata nella sicurezza informatica.


Ecco perché usiamo Kali Linux:





- È preconfigurato con un'ampia gamma di strumenti di pentesting (test di sicurezza di sistema e di rete).
- È **open source e gratuito**, quindi si può usare e modificare liberamente.
- È **affidabile e sicuro**, ideale per imparare la sicurezza informatica.
- Permette di imparare a usare Linux in un ambiente pronto per i test.
- Può essere installato in diversi modi: **VirtualBox**, **chiave USB avviabile** o **avvio doppio**.



## Installazione e configurazione



### 1. Prerequisiti



**Attrezzatura richiesta:**





- processore a 64 bit** (Intel o AMD).
- 8 GB di RAM minimo** (4 GB possono essere sufficienti per un'installazione leggera o una macchina virtuale).
- 50 GB di spazio libero su disco** per installare Kali Linux.
- Connessione a Internet** per scaricare l'immagine ISO e gli aggiornamenti.
- Una chiavetta USB** da almeno 8 GB per creare un supporto avviabile (se volete installare Kali su un PC o testarlo su Live USB).



È importante eseguire il backup dei dati prima dell'installazione su un PC esistente.



### 2. Scaricare





- Andare a [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Selezionate l'immagine ISO per la vostra applicazione:
  - Immagine di installazione** : per l'installazione su PC.
  - Immagine virtuale**: per installare Kali su VirtualBox o VMware.
- Scaricare l'immagine ISO.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Creare una chiave USB avviabile



È possibile utilizzare diversi strumenti, come Balena Etcher :





- Scaricare e installare [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Aprire Balena Etcher, quindi selezionare l'immagine ISO di Kali.
- Selezionare la chiave USB come supporto di destinazione.
- Fare clic su Flash e attendere il completamento del processo.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Installazione e sicurezza di Kali Linux



#### 4.1 Avvio dalla chiave USB





- Spegnere il computer.
- Inserite la chiave USB (contenente Kali Linux).
- Accendere il computer. Sui PC recenti, il sistema dovrebbe riconoscere automaticamente la chiave di avvio USB. In caso contrario, riavviare tenendo premuto il tasto di accesso al BIOS/UEFI (di solito F2, F12 o Canc, a seconda della marca).
  - Nel menu BIOS/UEFI, selezionare la chiave USB come dispositivo di avvio.
  - Salvare e riavviare.



#### 4.2 Avvio dell'installazione



##### Schermata di avvio



Quando si avvia dalla chiavetta USB, dovrebbe apparire la schermata di avvio di Kali Linux. Scegliete tra **installazione grafica** e **installazione testuale**. In questo esempio, abbiamo scelto l'installazione grafica.



![capture](assets/fr/06.webp)



Se si usa l'immagine **Live**, si vedrà un'altra modalità, **Live**, che è anche l'opzione di avvio predefinita.



![Mode Live](assets/fr/07.webp)



##### Selezione della lingua



Scegliere la lingua preferita per l'installazione e il sistema.



![Sélection de la langue](assets/fr/08.webp)



Si prega di specificare la propria posizione geografica.



![Options d'accessibilité](assets/fr/09.webp)



##### Configurazione della tastiera



Selezionare il layout della tastiera. È disponibile un campo di prova per verificare che i tasti corrispondano alla propria configurazione.



![Configuration du clavier](assets/fr/10.webp)



##### Connessione di rete



A questo punto l'installazione scansionerà le interfacce di rete, cercherà un servizio DHCP e chiederà di inserire un nome host per il sistema. Nell'esempio seguente, abbiamo inserito **"kali "** come nome host.



![Configuration réseau](assets/fr/11.webp)



È possibile fornire facoltativamente un nome di dominio predefinito che il sistema utilizzerà (i valori possono essere recuperati da DHCP o se esiste un sistema operativo preesistente).



![Choix du type d'installation](assets/fr/12.webp)



##### Account utente



Quindi, creare l'account utente per il sistema (nome completo, nome utente e una password forte).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Fuso orario



Selezionare la propria area geografica per impostare l'ora del sistema.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Tipo di suddivisione



Il programma di installazione esegue quindi una scansione dei dischi e visualizza diverse opzioni a seconda della configurazione.



In questa guida, si parte da un **disco vuoto**, che offre **quattro possibili scelte**.


Selezioneremo **Guidato - usa l'intero disco**, poiché stiamo eseguendo un'installazione unica di Kali Linux (avvio singolo). Ciò significa che nessun altro sistema operativo verrà mantenuto e che l'intero disco potrà essere cancellato.



Se il disco contiene già dei dati, è possibile che venga visualizzata un'opzione aggiuntiva **Guidato - utilizza lo spazio libero contiguo più grande**.



Questa alternativa consente di installare Kali Linux senza cancellare i dati esistenti, rendendolo ideale per il dual boot con un altro sistema.



Nel nostro caso, il disco è vuoto, quindi questa opzione non appare.



![Choix du partitionnement](assets/fr/17.webp)



Selezionare il disco da partizionare.



![capture](assets/fr/18.webp)



A seconda delle esigenze, si può scegliere di tenere tutti i file in un'unica partizione (comportamento predefinito) o di avere partizioni separate per una o più directory di primo livello.



Se non si è sicuri di ciò che si desidera, scegliere l'opzione **Tutti i file in un'unica partizione**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Avrete quindi un'ultima possibilità di controllare la configurazione del disco prima che il programma di installazione apporti modifiche irreversibili. Dopo aver fatto clic su _Continua_, il programma di installazione si avvierà e l'installazione sarà quasi completata.



![capture](assets/fr/21.webp)



##### LVM crittografato



Se questa opzione è stata attivata nel passaggio precedente, Kali Linux eseguirà una cancellazione sicura del disco rigido prima di chiedere la password LVM.



Si prega di utilizzare una password forte, altrimenti verrà visualizzato un avviso di passphrase debole.



##### Informazioni sul proxy



Kali Linux utilizza i repository per distribuire le applicazioni. Dovrete inserire le informazioni necessarie sul proxy se il vostro ambiente ne utilizza uno.



Se non si è **sicuri** di usare un proxy, **lasciare vuoto**. L'inserimento di informazioni false impedirà la connessione ai repository.



![capture](assets/fr/22.webp)



##### Metapiedi



Se l'accesso alla rete non è stato configurato, è necessario effettuare una **ulteriore configurazione** quando viene richiesto.



Se si utilizza l'immagine **Live**, il passaggio successivo non verrà visualizzato.



È quindi possibile selezionare i [metapacchetti](https://www.kali.org/docs/general-use/metapackages/) che si desidera installare. Le opzioni predefinite installeranno un sistema Kali Linux standard, quindi non sarà necessario modificare nulla.



![capture](assets/fr/23.webp)



#### Informazioni sull'avvio



Confermare quindi l'installazione del boot loader GRUB.



![capture](assets/fr/24.webp)



##### Riavvio



Infine, fare clic su Continua per riavviare la nuova installazione di Kali Linux.



![capture](assets/fr/25.webp)



#### 4.3 Aggiornamento e configurazione di Kali Linux dopo l'installazione



L'aggiornamento del sistema è una fase importante dopo una nuova installazione. Sono disponibili due opzioni:



##### Opzione 1: Tramite interfaccia grafica (GUI)



Kali, come Debian/Ubuntu, offre un gestore di aggiornamenti grafico integrato.



1. Fare clic sul **menu principale** (in alto a sinistra o in basso a seconda del desktop).


2. Aprire **"Software Updater "**.


3. Lo strumento :




    - Controllare i pacchetti da aggiornare.
    - Verrà visualizzato un elenco (con dimensioni e versioni).
    - Consente di avviare l'aggiornamento con un solo clic.


4. Quando viene richiesto, inserire la password di amministratore (`sudo`).


5. Lasciare che si installi e riavviare se necessario.



##### Opzione 2: via terminale



Aprite un terminale ed eseguite :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Non è consigliabile utilizzare l'account **root** per il lavoro quotidiano; creare invece un utente non root.



Nel terminale, digitate questi comandi:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Uscire e rientrare con il nuovo utente.



Riassumiamo alcuni compiti di base di Kali Linux in una tabella.



### Attività di base sotto Kali Linux



| **Catégorie**              | **Tâche de base**                      | **Description / Objectif**                                 | **Méthode principale**                                       |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Navigation système**     | Ouvrir le terminal                     | Accéder à la ligne de commande principale de Kali          | Cliquez sur l’icône du terminal ou utilisez `Ctrl + Alt + T` |
|                            | Parcourir les dossiers                 | Se déplacer dans l’arborescence du système                 | `cd /chemin/du/dossier`, `ls` pour lister les fichiers       |
|                            | Créer / supprimer un dossier           | Organiser les fichiers                                     | `mkdir nom_dossier`, `rm -r nom_dossier`                     |
| **Gestion des fichiers**   | Copier / déplacer un fichier           | Manipuler des fichiers dans le terminal                    | `cp fichier destination`, `mv fichier destination`           |
|                            | Supprimer un fichier                   | Libérer de l’espace disque                                 | `rm nom_du_fichier`                                          |
|                            | Afficher le contenu d’un fichier texte | Lire rapidement un fichier                                 | `cat fichier.txt`, `less fichier.txt`                        |
| **Gestion du système**     | Mettre à jour Kali Linux               | Installer les dernières versions et correctifs de sécurité | `sudo apt update && sudo apt full-upgrade -y`                |
|                            | Installer un logiciel                  | Ajouter un nouvel outil ou utilitaire                      | `sudo apt install nom_du_paquet`                             |
|                            | Supprimer un logiciel                  | Nettoyer le système                                        | `sudo apt remove nom_du_paquet`                              |
|                            | Nettoyer les dépendances inutiles      | Gagner de l’espace disque                                  | `sudo apt autoremove`                                        |
| **Réseau et Internet**     | Vérifier la connexion réseau           | Tester l’accès à Internet                                  | `ping google.com`                                            |
|                            | Identifier l’adresse IP                | Connaître sa configuration réseau                          | `ip a` ou `ifconfig`                                         |
|                            | Changer de réseau Wi-Fi                | Se connecter à un autre point d’accès                      | Icône réseau → Sélectionner le Wi-Fi voulu                   |
| **Comptes et permissions** | Exécuter une commande administrateur   | Obtenir les droits root temporairement                     | `sudo commande`                                              |
|                            | Créer un nouvel utilisateur            | Ajouter un compte local                                    | `sudo adduser nom_utilisateur`                               |
|                            | Modifier un mot de passe               | Sécuriser un compte                                        | `passwd`                                                     |
| **Apparence et confort**   | Changer le fond d’écran                | Personnaliser le bureau                                    | Clic droit sur le bureau → **Paramètres du bureau**          |
|                            | Modifier le thème / icônes             | Améliorer la lisibilité et l’esthétique                    | Paramètres → Apparence / Thèmes                              |
| **Outils Kali**            | Ouvrir le menu des outils              | Explorer les outils de test et de sécurité                 | Menu **Applications → Kali Linux**                           |
|                            | Lancer un outil (ex : nmap, wireshark) | Découverte pratique des utilitaires de sécurité            | `sudo nmap`, `wireshark`, etc.                               |
| **Aide et documentation**  | Obtenir de l’aide sur une commande     | Comprendre une commande avant de l’utiliser                | `man commande` ou `commande --help`                          |

## Conclusione



L'installazione di Kali Linux è solo il primo passo per scoprire questo potente ambiente dedicato alla sicurezza informatica. Padroneggiando le attività di base e la gestione del sistema, tutti possono iniziare a esplorare gli strumenti integrati e a comprendere il funzionamento interno di un sistema Linux. Kali offre un'eccellente piattaforma di apprendimento, sia per rafforzare le competenze tecniche che per sviluppare una vera e propria cultura della sicurezza informatica.
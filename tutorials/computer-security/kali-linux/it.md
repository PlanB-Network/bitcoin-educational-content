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




| **Categoria** | **Attività di base** | **Descrizione / Obiettivo** | **Metodo principale** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Navigazione di sistema** | Aprire il terminale | Accedere alla riga di comando principale di Kali | Cliccare sull'icona del terminale o usare `Ctrl + Alt + T` |
| | Sfogliare le cartelle | Spostarsi nell'albero del sistema | `cd /percorso/della/cartella`, `ls` per elencare i file |
| | Creare / eliminare una cartella | Organizzare i file | `mkdir nome_cartella`, `rm -r nome_cartella` |
| **Gestione dei file** | Copiare / spostare un file | Manipolare i file nel terminale | `cp file destinazione`, `mv file destinazione` |
| | Eliminare un file | Liberare spazio su disco | `rm nome_del_file` |
| | Visualizzare il contenuto di un file di testo | Leggere rapidamente un file | `cat file.txt`, `less file.txt` |
| **Gestione del sistema** | Aggiornare Kali Linux | Installare le ultime versioni e patch di sicurezza | `sudo apt update && sudo apt full-upgrade -y` |
| | Installare un software | Aggiungere un nuovo strumento o utility | `sudo apt install nome_del_pacchetto` |
| | Eliminare un software | Pulire il sistema | `sudo apt remove nome_del_pacchetto` |
| | Pulire le dipendenze inutili | Guadagnare spazio su disco | `sudo apt autoremove` |
| **Rete e Internet** | Verificare la connessione di rete | Testare l'accesso a Internet | `ping google.com` |
| | Identificare l'indirizzo IP | Conoscere la propria configurazione di rete | `ip a` o `ifconfig` |
| | Cambiare rete Wi-Fi | Connettersi a un altro punto di accesso | Icona di rete → Selezionare il Wi-Fi desiderato |
| **Account e permessi** | Eseguire un comando amministratore | Ottenere temporaneamente i diritti di root | `sudo comando` |
| | Creare un nuovo utente | Aggiungere un account locale | `sudo adduser nome_utente` |
| | Modificare una password | Mettere in sicurezza un account | `passwd` |
| **Aspetto e comfort** | Cambiare lo sfondo | Personalizzare il desktop | Tasto destro sul desktop → **Impostazioni della scrivania** |
| | Modificare il tema / icone | Migliorare la leggibilità e l'estetica | Impostazioni → Aspetto / Temi |
| **Strumenti Kali** | Aprire il menu degli strumenti | Esplorare gli strumenti di test e sicurezza | Menu **Applicazioni → Kali Linux** |
| | Avviare uno strumento (es: nmap, wireshark) | Scoperta pratica delle utility di sicurezza | `sudo nmap`, `wireshark`, ecc. |
| **Aiuto e documentazione** | Ottenere aiuto su un comando | Comprendere un comando prima di usarlo | `man comando` o `comando --help` |

## Conclusione



L'installazione di Kali Linux è solo il primo passo per scoprire questo potente ambiente dedicato alla sicurezza informatica. Padroneggiando le attività di base e la gestione del sistema, tutti possono iniziare a esplorare gli strumenti integrati e a comprendere il funzionamento interno di un sistema Linux. Kali offre un'eccellente piattaforma di apprendimento, sia per rafforzare le competenze tecniche che per sviluppare una vera e propria cultura della sicurezza informatica.
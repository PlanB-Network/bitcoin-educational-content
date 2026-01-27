---
name: Pop!_OS
description: Guida all'installazione di Pop!_OS, una distribuzione Linux
---

![cover](assets/cover.webp)



## Introduzione



Pop!OS è un sistema operativo basato su Linux sviluppato da **System76**, un produttore americano specializzato in macchine per sviluppatori, designer e utenti avanzati.



Progettato per offrire un ambiente moderno, stabile e ad alte prestazioni, Pop!OS si distingue per un'esperienza semplice, strumenti potenti e una forte attenzione alla produttività.



### Chi è System76?



System76 è un'azienda americana fondata nel 2005 con sede a Denver, specializzata nella produzione di notebook, desktop e server progettati specificamente per Linux.



A differenza dei produttori tradizionali, System76 sviluppa macchine progettate per essere aperte, riparabili e orientate alla libertà del software.



System76 non produce solo computer.



L'azienda sviluppa anche :




- Pop!OS**, il proprio sistema operativo basato su Linux;
- COSMIC**, il moderno ambiente desktop ad alte prestazioni utilizzato da Pop!OS ;
- Open Firmware**, un firmware open-source basato su Coreboot ;
- strumenti per sviluppatori e designer.



L'obiettivo è offrire un'integrazione hardware e software di alta qualità, paragonabile all'ecosistema Apple, ma totalmente aperta e incentrata su Linux.



## Un sistema moderno, stabile e accessibile



Pop!OS si basa sulle fondamenta di Ubuntu, conferendogli un'eccellente stabilità, un'ampia compatibilità hardware e l'accesso a un vasto ecosistema software.


Offre un'interfaccia elegante, il desktop COSMIC, progettato per essere fluido, intuitivo e personalizzabile, anche per i nuovi utenti.



## La scelta ideale per sviluppatori, progettisti e utenti esigenti



Pop!OS è particolarmente apprezzato da :





- sviluppatori (strumenti preinstallati, gestione avanzata delle piastrelle),
- utenti con schede grafiche Nvidia o AMD,
- studenti e professionisti alla ricerca di un sistema affidabile,
- utenti di Windows che desiderano effettuare una semplice transizione.



Include la piastrellatura automatica, un centro software chiaro e strumenti di produttività integrati per facilitare l'uso quotidiano.



## Punti salienti di Pop!OS





- Prestazioni ottimizzate** grazie agli aggiornamenti regolari.
- Sono disponibili due versioni ISO**: standard e ottimizzata per Nvidia.
- Maggiore sicurezza** (crittografia LUKS disponibile all'installazione).
- Interface COSMIC** ergonomico e moderno.
- Altamente compatibile** con il software Ubuntu e Flatpak.



## Scarica POP!OS in modo sicuro



### 1. Prerequisiti



Prima di scaricare e installare POP!OS, sono necessarie alcune operazioni per preparare correttamente l'ambiente di installazione.



### Attrezzatura necessaria





- Un computer compatibile**: Processore Intel o AMD, GPU Intel / AMD / Nvidia.
- Almeno 4 GB di RAM** (8 GB consigliati per un uso confortevole).
- 20 GB di spazio libero minimo** (consigliati 40 GB o più).
- Una chiave USB** da almeno 4 GB per creare il supporto di installazione.



### Connessione a Internet



Una connessione stabile è utile per :





- scaricare l'immagine ISO,
- installare gli aggiornamenti dopo l'installazione.



Pop!OS può funzionare anche senza connessione, ma l'installazione è molto più fluida su Internet.



### Backup dei dati



Se Pop!OS deve sostituire o coesistere con un altro sistema (Windows, Ubuntu, ecc.), è consigliabile eseguire un backup dei file importanti prima di procedere.



### Verificare la presenza di una GPU Nvidia (se applicabile)



Per i computer dotati di scheda grafica Nvidia, è necessario scaricare l'immagine ISO speciale che include i driver Nvidia.


Questo controllo è molto semplice:





- consultando le specifiche del PC,
- o cercando il modello della scheda grafica nelle impostazioni del sistema.



### Scarica dal sito ufficiale



L'immagine ISO di Pop!OS deve essere scaricata direttamente dalla pagina ufficiale di System76: [system76.com/pop](https://system76.com/pop/).



Questa pagina offre sempre la versione più recente, adatta al vostro hardware.



![capture](assets/fr/03.webp)



### Scegliere la versione: Standard o Nvidia, o Raspberry Pi (ARM64)



Pop!OS è disponibile in tre varianti:



### Versione standard



Consigliato per i computer che utilizzano :





- processore intel o AMD;
- una GPU integrata Intel o AMD;
- una scheda grafica AMD Radeon.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Versione Nvidia



Consigliato per i computer dotati di schede grafiche Nvidia.


Questa immagine include già i driver Nvidia, semplificando l'installazione e riducendo i problemi di grafica.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Versione Raspberry Pi (ARM64)



Per Raspberry Pi 4 e 400 (processore ARM).


Adattata all'architettura ARM, questa è una versione specifica per questi mini-computer.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Creare una chiave USB avviabile



È possibile utilizzare diversi strumenti, come Balena Etcher :





- Scaricare e installare [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Aprire Balena Etcher, quindi selezionare l'immagine ISO di Pop!OS.
- Selezionare la chiave USB come supporto di destinazione.
- Fare clic su Flash e attendere il completamento del processo.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Installazione e protezione di Pop!OS



### Avvio da chiave USB





- Spegnere il computer.
- Inserite la chiave USB (contenente Pop!OS).
- Accendere il computer. Sui PC recenti, il sistema dovrebbe riconoscere automaticamente la chiave di avvio USB. In caso contrario, riavviare tenendo premuto il tasto di accesso al BIOS/UEFI (di solito F2, F12 o Canc, a seconda della marca).
  - Nel menu BIOS/UEFI, selezionare la chiave USB come dispositivo di avvio.
  - Salvare e riavviare.



### Avvio dell'installazione



Una volta selezionata la chiave USB avviabile come dispositivo di avvio, il computer si avvia in un ambiente Pop!OS Live.



Selezionare la lingua.



![Capture](assets/fr/10.webp)



Selezionare una località.



![Capture](assets/fr/11.webp)



Selezionare una lingua per l'input da tastiera.



![Capture](assets/fr/12.webp)



Selezionare un layout di tastiera.



![Capture](assets/fr/13.webp)



Scegliere l'opzione "Installazione pulita" per un'installazione standard. Questa è l'opzione migliore per i nuovi utenti di Linux, ma bisogna tenere presente che cancellerà tutto il contenuto dell'unità di destinazione. In alternativa, è possibile selezionare l'opzione "Prova modalità demo" per continuare a testare Pop!OS nell'ambiente live.



![Capture](assets/fr/14.webp)



Selezionare `Personalizzato (avanzato)` per accedere a GParted. Questo strumento consente di configurare funzioni avanzate come il doppio avvio, la creazione di una partizione `/home` separata o il posizionamento della partizione `/tmp` su un'altra unità.



Fare clic su "Cancella e installa" per installare Pop!OS sull'unità selezionata.



![Capture](assets/fr/15.webp)



### Configurazione dell'account utente



La sezione successiva del programma di installazione vi guiderà nella creazione di un account utente per poter accedere al nuovo sistema operativo.



Fornite un nome completo (che può includere qualsiasi testo a vostra scelta, maiuscolo o minuscolo) e un nome utente (che deve essere in minuscolo):



![Capture](assets/fr/16.webp)



Una volta creato l'account, verrà richiesto di impostare una nuova password.



![Capture](assets/fr/17.webp)



### Crittografia dell'intero disco



La crittografia del disco di sistema non è necessaria, ma garantisce la sicurezza dei dati dell'utente in caso di accesso fisico non autorizzato al dispositivo.



L'unità può essere crittografata utilizzando la password di accesso selezionando `La password di crittografia è uguale alla password dell'account utente`. È anche possibile deselezionare questa casella e selezionare `Imposta password` in basso. Selezionare "Non crittografare" per ignorare il processo di crittografia del disco.



![Capture](assets/fr/18.webp)



Se si è scelto il pulsante `Imposta password`, verrà visualizzato un ulteriore prompt per impostare la password di crittografia.



Procedete al passo successivo del programma di installazione. Pop!OS inizierà l'installazione sul disco.



![Capture](assets/fr/19.webp)



Una volta completata l'installazione, riavviare il computer e accedere per completare il processo di configurazione dell'account utente.



Se è stato modificato l'ordine di avvio per dare priorità alla chiave USB Live all'avvio, spegnere completamente il computer e rimuovere la chiave USB di installazione. Se si è in modalità dual-boot, premere i tasti appropriati per accedere alla configurazione e selezionare l'unità contenente l'installazione di Pop!OS.



![Capture](assets/fr/20.webp)



### Grafica NVIDIA



Se è stata eseguita l'installazione dalla ISO Intel/AMD e il sistema dispone di una scheda grafica NVIDIA discreta, o se ne è stata aggiunta una in un secondo momento, è necessario installare manualmente i driver della scheda per ottenere prestazioni ottimali. Eseguire il seguente comando in un terminale di comando per installare il driver:



```bash
sudo apt install system76-driver-nvidia
```



È inoltre possibile installare i driver grafici NVIDIA dal Pop!_Shop.



![Capture](assets/fr/20.webp)



## Installazione degli strumenti essenziali



Pop!OS offre un'ampia gamma di software tramite il Pop!Shop, ma molti strumenti essenziali possono essere installati anche tramite il terminale con `apt` o `flatpak`. Ecco come installare gli strumenti chiave per un ambiente di lavoro completo.



### Installazione dei terminali




| Strumento | Descrizione | Comando di installazione |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox | Browser web libero e popolare | `sudo apt install firefox` |
| Brave | Browser web focalizzato sulla privacy | Installazione tramite Pop!_Shop o sito ufficiale |
| Visual Studio Code (VS Code) | Potente editor di codice per sviluppatori | `flatpak install flathub com.visualstudio.code` |
| Git | Gestore di versioni | `sudo apt install git` |
| Flatpak | Gestore di pacchetti alternativo | `sudo apt install flatpak` |
| VLC | Lettore multimediale versatile | `sudo apt install vlc` |
| GNOME Terminal | Terminale predefinito | Preinstallato su Pop!OS |
| Curl | Strumento di trasferimento dati online | `sudo apt install curl` |
| Wget | Download di file via HTTP/FTP | `sudo apt install wget` |
| Docker | Containerizzazione di applicazioni | Installazione tramite script ufficiale o `apt` |
| Node.js | Ambiente JavaScript lato server | Installazione tramite `apt` o NodeSource |
| Python3 | Linguaggio di programmazione | `sudo apt install python3 python3-pip` |
| GIMP | Editor di immagini avanzato | `sudo apt install gimp` |
| Thunderbird | Client email | `sudo apt install thunderbird` |
| Transmission | Client BitTorrent leggero | `sudo apt install transmission-gtk` |
| Htop | Monitor di sistema interattivo | `sudo apt install htop` |

### Installazione tramite Pop! Shop (interfaccia grafica)





- Aprire **Pop!_Shop** dal menu principale.
- Utilizzate la barra di ricerca per trovare le applicazioni desiderate (ad esempio, "Brave").
- Fare clic su **Installa** per ogni applicazione.
- Pop!_Shop gestisce automaticamente le dipendenze e gli aggiornamenti.



## Aggiornamento del sistema



### Opzione 1: Tramite interfaccia grafica (GUI)



Pop!OS dispone di un gestore di aggiornamenti grafico semplice e intuitivo.



1. Fare clic sul **menu principale** (icona in basso a sinistra).


2. Aprire **"Pop!_Shop "**.


3. Nel Pop!_Shop, fare clic sulla scheda **"Aggiornamenti "**.


4. Il sistema controllerà automaticamente gli aggiornamenti disponibili.


5. Fare clic su **"Aggiorna tutto "** per avviare l'installazione degli aggiornamenti.


6. Se richiesto, inserire la password.


7. Lasciare terminare il processo, quindi riavviare se necessario.



### Opzione 2: via terminale



Aprite un terminale e digitate :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Gestione degli utenti



Si consiglia di utilizzare un account utente standard con diritti sudo per le operazioni quotidiane.



Per creare un nuovo utente :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Uscire, quindi accedere nuovamente con questo nuovo utente.



### Gestione dei driver grafici





- Per le schede Nvidia, verificare che siano installati i driver proprietari:



```bash
sudo apt install system76-driver-nvidia
```





- Per AMD/Intel, i driver sono generalmente inclusi di default.



### Attivare il firewall (UFW)



Pop!OS non blocca il traffico di rete per impostazione predefinita. Attivate UFW per migliorare la sicurezza:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Configurare gli aggiornamenti automatici



Per mantenere il sistema aggiornato senza interventi manuali:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Personalizzare l'aspetto e il comportamento





- Aprire **Impostazioni di sistema** → **Apparenza** per scegliere un tema chiaro o scuro.
- Configurare gli angoli attivi, le animazioni e le estensioni tramite il manager COSMIC.
- Regolate il layout del desktop per ottimizzare il flusso di lavoro.



### Configurare il backup automatico



Pop!OS integra strumenti come Deja Dup per il backup:





- Avviare **Backup** dal menu.
- Scegliere un'unità esterna o una posizione di rete.
- Programmare backup regolari.



### Installazione di utili estensioni di GNOME/COSMIC



Ecco alcune estensioni consigliate per migliorare l'esperienza dell'utente:





- Dash to Dock**: barra delle applicazioni sempre visibile.
- GSConnect**: sincronizzazione con Android.
- Indicatore Appunti**: gestione avanzata degli Appunti.



Installarli tramite :



```bash
sudo apt install gnome-shell-extensions
```



Quindi attivarli nelle impostazioni.



### Ottimizzazione della gestione della memoria e dello swap



Controllare lo stato di scambio:



```bash
swapon --show
```



Se necessario, aumentare la dimensione dello swap o configurare un file di swap:



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Aggiungerlo al file `/etc/fstab` per il montaggio automatico.



## Gestione di pacchetti e repository



### Comprendere le fonti dei pacchetti



Pop!OS, basato su Ubuntu, utilizza principalmente :





- Repository ufficiali Ubuntu**: per la maggior parte del software stabile.
- Repository System76**: per driver, firmware e strumenti specifici.
- Flatpak**: accesso a un'ampia gamma di applicazioni in sandbox.
- Snap** (opzionale): un altro formato di pacchetto universale.



---

### Aggiungere e gestire i repository PPA



Per installare software frequentemente aggiornato, è possibile aggiungere alcuni PPA (Personal Package Archives):



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Conclusione



Pop!OS è una distribuzione Linux moderna e stabile, adatta sia ai principianti che agli utenti avanzati.



Grazie all'intuitiva interfaccia COSMIC e agli strumenti integrati, offre un'esperienza fluida e produttiva, sia per lo sviluppo, la creazione o l'uso quotidiano.



Questo tutorial copre le fasi principali: preparazione, download, installazione, impostazioni iniziali e strumenti essenziali.



Sentitevi liberi di esplorare ulteriormente Pop!OS e di personalizzare il vostro ambiente per ottenere il massimo da esso.
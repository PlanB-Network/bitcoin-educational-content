---
name: Elementary OS
description: Il sostituto ideale per Windows e MacOS
---

![cover](assets/cover.webp)

Elementary OS è un sistema operativo basato su Ubuntu, progettato per essere semplice, veloce e stabile per molti usi quotidiani. Rappresenta un'equilibrata alternativa Linux a MacOS e Windows. La sua grafica fluida, intuitiva e priva di fronzoli lo rende facile da imparare, anche per i principianti. Inoltre, si concentra sull'ergonomia, la sicurezza e le prestazioni.

https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5


## Perché scegliere Elementary OS

- **Semplicità e facilità d'uso**: la grafica dell'interfaccia di Elementary OS è a metà strada tra quelle di MacOs e Windows. Questa familiarità lo rende facile da adottare, anche per gli utenti meno esperti.
- **Sicurezza**: come la maggior parte delle distribuzioni Linux, Elementary OS beneficia di un elevato livello di sicurezza. Aggiornamenti regolari, gestione dei diritti e assenza di virus comuni ne fanno un sistema affidabile.
- **Velocità**: Elementary OS è una distribuzione leggera. Richiede poche risorse, il che la rende veloce e adatta a computer con configurazioni modeste.
- **Gratuito**: il sistema è completamente gratuito. Tuttavia, quando lo si scarica, è possibile effettuare una donazione per sostenere gli sviluppatori.
- **Comunità attiva**: la comunità intorno a Elementary OS è varia e reattiva. In caso di difficoltà, è facile trovare aiuto nei forum o nei social network.


## Installazione e configurazione

### Prerequisiti hardware

Prima di iniziare l'installazione, accertarsi di disporre delle seguenti apparecchiature:

- Una **chiave USB** da almeno 12 GB
- **Memoria RAM** di almeno 4 GB
- Un disco rigido **da 20 GB** o più per un uso confortevole


## Scarica l'immagine ISO

Vai sul sito ufficiale del sistema operativo [ElementaryOS](https://elementary.io/) e scegli un importo per sostenere il progetto. Questo passo è facoltativo.

Se desideri scaricare gratuitamente l'immagine ISO, inserisci '0' nel campo **"Altro "** e avvia il download dell'immagine ISO del sistema.

![0_01](assets/fr/01.webp)


## Creare una chiave USB avviabile

Una volta scaricata l'immagine ISO, è necessario renderla avviabile su una chiavetta USB per procedere con l'installazione.

Scarica un software come [Balena Etcher](https://etcher.balena.io/) o uno strumento simile, quindi avvia il software.

Seleziona l'immagine ISO di **Elementary OS** scaricata in precedenza e imposta la chiave USB come destinazione.

Fai clic sul pulsante **flash** per avviare il processo e attendere il completamento del processo prima di rimuovere la chiave USB.

![0_02](assets/fr/02.webp)


## Avvio con chiave e accesso al BIOS

Spegni il computer su cui desideri installare Elementary OS, quindi inserisci la chiave USB.

All'avvio del computer, accedi al BIOS (`ESC`, `F9` o `F11` a seconda della marca) e selezionare la chiave USB come dispositivo di avvio, quindi premere `Invio` per avviare il processo di avvio.


## Installazione di Elementary OS

L'installazione si avvia automaticamente se la chiave USB è configurata correttamente.

### Selezione della lingua

Seleziona la lingua in cui desideri installare il sistema. È possibile scegliere anche il tuo linguaggio preferito.

![0_03](assets/fr/03.webp)

![0_04](assets/fr/04.webp)

### Layout della tastiera

Seleziona il layout corrispondente alla tua tastiera. È previsto un campo per verificare che i tasti producano i caratteri corretti.

![0_05](assets/fr/05.webp)

![0_06](assets/fr/06.webp)

### Modalità test

Elementary OS consente di testare il sistema prima di installarlo. Questa modalità consente di esplorare l'interfaccia senza modificare nulla del disco rigido.

### Avvio dell'installazione

- Fai clic su "**Cancella disco e installa**" per installarla direttamente sull'intero disco.
- Fai clic su "**Installazione personalizzata**" se si desidera gestire manualmente le partizioni.

![0_07](assets/fr/07.webp)

### Selezione del disco

Seleziona il disco su cui installare Elementary OS, quindi fai clic sul pulsante "Continua".

![0_08](assets/fr/08.webp)

### Crittografia del disco

Un'opzione consente di crittografare il disco per **proteggere i dati**. Per attivare questa protezione è necessario impostare una password forte. Tuttavia, è opzionale.

![0_09](assets/fr/09.webp)

![0_10](assets/fr/10.webp)

### Avvio dell'installazione

Prima di avviare l'installazione, è possibile autorizzare l'installazione automatica di driver hardware aggiuntivi, a seconda della compatibilità della macchina.

- Fai clic su "Cancella e installa" per avviare l'installazione.
- Attendi il completamento del processo.

![0_11](assets/fr/11.webp)

![0_12](assets/fr/12.webp)

### Riavvio

Al termine, fai clic sul pulsante **enter** per riavviare, quindi rimuovi la chiave USB al momento opportuno per evitare di riavviare l'installazione.

![0_13](assets/fr/13.webp)

## Configurazione dopo l'installazione

Dopo il riavvio, sono necessari alcuni passaggi aggiuntivi.

![0_14](assets/fr/14.webp)

### Selezione della lingua

Conferma o modifica la lingua del sistema al momento del login.

![0_15](assets/fr/15.webp)

### Layout della tastiera

Assicurati che il layout della tastiera sia quello desiderato.

![0_16](assets/fr/05.webp)

### Creazione di un account utente

Associa un account utente al sistema operativo definendo un nome utente e proteggendo l'accesso ai dati con una password alfanumerica di almeno 20 caratteri e simboli.

![0_17](assets/fr/17.webp)

### Prima connessione

Al primo accesso, Elementary OS consente di personalizzare l'ambiente con alcune impostazioni di base.

![0_18](assets/fr/18.webp)

![0_19](assets/fr/19.webp)


## Aggiornamento del sistema

Prima di un uso prolungato, è importante aggiornare il sistema con le patch più recenti.

### Opzione 1: Aggiornamento tramite interfaccia grafica

Accedi all'**AppCenter** e fai clic sull'icona degli aggiornamenti nell'angolo in alto a destra. Attendi l'elenco degli aggiornamenti, quindi fai clic su "**Aggiorna tutto**" per avviare l'installazione.

![0_20](assets/fr/20.webp)

![0_21](assets/fr/21.webp)

### Opzione 2: Aggiornamento tramite terminale

È anche possibile eseguire l'aggiornamento da riga di comando tramite il terminale: un'opzione consigliata per la sua precisione.

```shell
sudo apt update
```

```shell
sudo apt full-upgrade
```

Per i primi aggiornamenti, il sistema operativo richiede la password utente e la conferma per aggiornare i pacchetti software, anche nel kernel di Elementary OS.


## Configurazione dell'ambiente di lavoro

Elementary OS include solo gli strumenti essenziali. Per adattare l'ambiente alle tue esigenze, soprattutto se sei uno sviluppatore, ti consigliamo di installare strumenti aggiuntivi.

- È possibile aggiungere le dipendenze utili con il seguente comando (da adattare alle tue esigenze):

```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```

Questo comando installa **Git**, **Python 3**, **pip**, **strumenti del compilatore**, **wget**, **curl**, **zsh**, **make**, **snapd** e **vscode** per preparare un ambiente di sviluppo di base.

Elementary OS è ora attivo e funzionante sul tuo computer. La sua filosofia di semplicità, leggerezza ed eleganza lo rende una scelta eccellente per l'uso personale e professionale. Avrete un sistema stabile, fluido e ordinato, pronto per essere personalizzato secondo le tue preferenze. Che si tratti di sviluppo, uso in ufficio o navigazione quotidiana, tutto è al suo posto per costruire un ambiente di lavoro efficiente, intuitivo e piacevole. Date un'occhiata anche al nostro tutorial su Fedora, una distribuzione Linux altrettanto semplice, robusta e modulare.

https://planb.academy/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

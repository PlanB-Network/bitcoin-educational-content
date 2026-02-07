---
name: Manjaro
description: Rendere più accessibile la potenza di Arch Linux
---
![cover](assets/cover.webp)

Arch Linux è un sistema operativo molto diffuso in molti settori, grazie alla sua robustezza e stabilità. Tuttavia, può essere difficile da usare per gli utenti inesperti. È proprio per risolvere questo problema che è stato creato **Manjaro**: offrire la potenza di Arch Linux, ma con un'esperienza più semplice e accessibile, basata su un'interfaccia intuitiva e facile da imparare.


## Come iniziare con Manjaro

Uno dei maggiori punti di forza di Manjaro è il suo **sistema di aggiornamento semplice ed efficiente**. Non c'è bisogno di gestire gli aggiornamneti manualmente: Manjaro se ne occupa per te! Un'icona nell'area di notifica (la posizione varia a seconda dell'edizione) ti avvisa quando è disponibile un aggiornamento. Tutto quello che devi fare è seguire le istruzioni e il processo è veloce e senza sforzo.

Manjaro offre anche un **vasto catalogo di applicazioni**. Poiché Manjaro è basato su Arch Linux, beneficia dell'accesso diretto ai suoi repository ufficiali, ricchi di una varietà di software, comprese le applicazioni proprietarie. Manjaro ritarda leggermente alcuni aggiornamenti di Arch Linux per ulteriori test; questo migliora la stabilità al costo di un leggero ritardo nelle nuove versioni. E se questa scelta non ti basta, puoi anche accedere all'**AUR (*Arch User Repository*)**, un'enorme libreria gestita dalla comunità. Se un programma non esiste nei repository ufficiali, è probabile che sia disponibile in AUR.

Un altro vantaggio di Manjaro è che è **molto meno avido di risorse** rispetto a sistemi come Windows o macOS. Consuma meno RAM e potenza di calcolo, rendendolo una scelta ideale per i computer più vecchi o meno potenti: la macchina guadagna in fluidità e velocità, riacquistando una seconda giovinezza.

Inoltre, Manjaro è **completamente gratuito**. A differenza di Windows o macOS, non è necessario pagare nulla per installarlo e sfruttarlo al meglio. Infine, offre una **maggiore sicurezza** grazie ad aggiornamenti regolari e rapidi, che limitano l'esposizione alle vulnerabilità. La sua comunità attiva garantisce inoltre la rapida correzione di eventuali problemi e la proposta di soluzioni efficaci.


## Scoprire Manjaro OS

Prima di iniziare l'installazione di Manjaro, è importante sapere che questa distribuzione è disponibile in diverse edizioni. Ognuna di queste edizioni offre un ambiente desktop unico che influenza sia il flusso di lavoro che il consumo delle risorse di sistema. Esistono tre edizioni ufficiali principali di Manjaro.

![0_01](assets/fr/01.webp)

- L'edizione **KDE Plasma** è la più personalizzabile. Se siete alla ricerca di un sistema visivamente elegante e ad alte prestazioni, KDE Plasma è una scelta eccellente. Questo ambiente desktop stabile è ideale per gli utenti che desiderano un controllo totale e un'esperienza personalizzata.

- Per le macchine con risorse più limitate, l'edizione **Xfce** è la soluzione ideale. La sua interfaccia è leggera e intuitiva e garantisce un funzionamento fluido anche sui computer più vecchi. Inoltre, il suo layout ricorda quello di Windows, rendendo più facile la transizione a Linux per i nuovi utenti.

- Infine, l'edizione **GNOME** offre un approccio completamente diverso. Il suo design snello enfatizza la produttività e l'organizzazione attraverso spazi di lavoro virtuali. Questo flusso di lavoro incentrato sulle attività è particolarmente interessante per gli utenti che hanno già familiarità con Linux e che cercano un ambiente minimalista e altamente efficiente.

### Altre edizioni di Manjaro

![0_02](assets/fr/02.webp)

Oltre alle edizioni ufficiali, la comunità di Manjaro offre anche altre versioni. Queste edizioni alternative sono progettate per soddisfare esigenze specifiche e offrono una varietà di ambienti desktop.

L'edizione **Cinnamon** è una scelta eccellente per chi è agli inizi e cerca un'interfaccia familiare. È stata progettata per essere facile da usare, pur mantenendo le classiche convenzioni degli ambienti d'ufficio tradizionali.

Per gli utenti più avanzati, esistono edizioni come **i3 Window Manager** o **Sway**. Molto più leggere e veloci, richiedono comunque una buona padronanza della riga di comando per essere configurate e sfruttate appieno. Questi ambienti sono ideali per coloro che desiderano un controllo totale sul proprio sistema e che pongono l'efficienza al di sopra di tutto.


## Requisiti tecnici

Affinché Manjaro funzioni in modo ottimale, il computer deve soddisfare alcuni requisiti minimi. Si consiglia di avere almeno il formato:
- Processore a 64 bit (x86_64)
- **4 GB di RAM consigliati (minimo 2 GB)** (vedi sotto)
- 30 GB di spazio su disco (di più se si crea una partizione `/home` dedicata)


## Installazione di Manjaro

Per scaricarlo, vai sul [sito ufficiale di Manjaro](https://manjaro.org/) e scegli l'edizione più adatta alle tue esigenze. Una volta scaricato il file, è necessario creare una chiave USB avviabile con l'immagine ISO di Manjaro.

Quindi vai sul sito web del software [Rufus](https://rufus.ie/it/) e scaricalo. Esegui il programma, inserisci la chiave USB, seleziona l'immagine ISO di Manjaro e avvia il flashing. Attendi il termine del processo prima di rimuovere la chiave. Quindi ora puoi riavviare il computer.

![0_03](assets/fr/03.webp)

Per installare Manjaro sul tuo computer, prima spegnilo completamente. Quindi inserisci la chiave USB, riaccendi il computer e accedi al menu di avvio o al firmware UEFI/BIOS premendo **F2, F10, F12, Escape** o **Delete** (a seconda del produttore).

Scegli quindi la chiave USB come dispositivo di avvio per avviare il processo di installazione del sistema operativo.

### Schermata di avvio

La prima volta che avvii Manjaro dalla chiavetta USB, vieni portato direttamente al menu di installazione. Prima di avviare l'installazione, è possibile cambiare il layout della tastiera o la lingua del sistema.

Seleziona quindi l'opzione **Boot with open source drivers** per avviare l'installazione di Manjaro. Questi driver open source sono compatibili con la maggior parte dell'hardware e sono sufficienti nella maggior parte dei casi. Se disponi di una scheda grafica NVIDIA, ad esempio, o richiedi prestazioni grafiche superiori, è possibile scegliere **Boot with proprietary drivers**, che utilizza driver proprietari.

![0_04](assets/fr/04.webp)

Il sistema verrà avviato in **modalità live predefinita**. Questo ti permette di testare le funzionalità di Manjaro per vedere se è adatto alle tue esigenze prima di installarlo definitivamente. Una volta pronto, fai clic sull'opzione **Installa Manjaro Linux**.

Seleziona la lingua desiderata per l'installazione, quindi fai clic su **Avanti**.

![0_06](assets/fr/06.webp)

Scegli quindi la tua località per impostare il fuso orario corretto. In questa fase è possibile modificare anche la lingua e il formato della data.

![0_07](assets/fr/07.webp)

Seleziona il layout della tastiera. È disponibile un campo di prova per verificare che i tasti digitati corrispondano ai caratteri previsti.

![0_08](assets/fr/08.webp)

### Partizionamento del disco

Per il partizionamento del disco sono disponibili due opzioni.

- Il primo, il più semplice, è cancellare l'intero disco e installarci sopra Manjaro.
- Il secondo consente una **partizione manuale**.

![0_09](assets/fr/09.webp)

Per un'installazione pulita, ti consiglio di creare almeno tre partizioni:
- Una prima partizione di **516 MB** (primaria) per l'**avvio**.
- Una seconda partizione da **2 GB** (logica) per **swap**.
- Una terza partizione per i **dati personali**.

Se desideri installare un altro sistema in parallelo, è necessario dividere quest'ultima partizione e assegnarne solo una parte a Manjaro (almeno **15 GB** per garantire il corretto funzionamento del sistema).

### Creazione di un account utente

Crea un account utente sul sistema compilando le informazioni richieste. Infine, imposta la password dell'amministratore (**root**). L'amministratore è un **super-utente** con pieni diritti sul sistema e la possibilità di eseguire comandi avanzati.

![0_10](assets/fr/10.webp)

### Scegliere la giusta suite per ufficio

Manjaro consente di scegliere tra **FreeOffice** e **LibreOffice**.

- **LibreOffice** è più completo, con una gamma più ampia di software e funzioni avanzate.
- **FreeOffice**, invece, è più leggero e include solo l'essenziale: **TextMaker**, **PlanMaker** e **Presentazioni**.

![0_11](assets/fr/11.webp)

### Riepilogo della configurazione

Una schermata di riepilogo mostra tutti i parametri impostati. Se necessario, è possibile tornare indietro per apportare modifiche, senza influire sulle impostazioni già effettuate.

Quindi fai clic su **Install** e conferma per avviare l'installazione vera e propria.

![0_12](assets/fr/12.webp)

![0_13](assets/fr/13.webp)

### Fine dell'installazione

Alla fine del processo, seleziona la casella **Restart now**, quindi fai clic su **Done**. Il sistema si riavvierà e **Manjaro sarà pronto all'uso**.

![0_13](assets/fr/14.webp)


## Primi passi con Manjaro

L'installazione di Manjaro è solo il primo passo. Per ottenere il massimo dal tuo sistema, ecco alcune cose utili da sapere.

### Aggiornare il sistema

Manjaro semplifica notevolmente gli aggiornamenti. Per aggiornare i pacchetti:

```shell
sudo pacman -Syu
```

Questo comando scarica e installa le ultime versioni disponibili. Si consiglia di eseguirlo regolarmente per mantenere il sistema **sicuro e stabile**.

### Configurazione di un ambiente di sviluppo

Per sviluppare applicazioni Web su Manjaro, installa gli strumenti essenziali con un solo comando:

```shell
sudo pacman -S nodejs npm git yarn
```

Questo comando installa Node.js e npm per eseguire e gestire i progetti JavaScript e TypeScript, Git per la gestione delle versioni e Yarn come gestore di pacchetti alternativo.

### Installazione di un Bitcoin Wallet

Per gestire i tuoi bitcoin su Manjaro, puoi installare **Electrum**, un Wallet leggero e sicuro:

```shell
sudo pacman -S electrum  # Installa Electrum
```

Electrum consente di **ricevere e inviare bitcoin** con facilità, offrendo al contempo funzioni avanzate come la gestione di più Wallet e la passphrase come ulteriore protezione. Per una guida completa all'uso di Electrum, consulta il nostro tutorial dedicato che spiega come creare un Wallet, proteggere i tuoi fondi ed effettua transazioni.

https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


## Proteggere il sistema Manjaro

La sicurezza è un aspetto cruciale di qualsiasi installazione Linux. È importante proteggere la riservatezza e l'integrità dei dati.

### Configurazione del firewall

Manjaro include UFW (*Uncomplicated Firewall*), un programma per la gestione dei filtri firewall di rete, ma bisogna attivarlo manualmente:

```bash
# Installation if not present
sudo pacman -S ufw

# Firewall activation
sudo systemctl enable ufw.enable

sudo ufw enable

# Allow SSH connections (optional)
sudo ufw allow ssh

# Check the status
sudo ufw status verbose
```

![verbose](assets/fr/15.webp)

### Gestione delle autorizzazioni degli utenti

1. **Creare un utente non privilegiato**

```shell
sudo useradd -m username
sudo passwd username
```

2. **Configurazione del file Sudoers**

```shell
sudo EDITOR=nano visudo
```

Ora sei pronto a utilizzare Manjaro Linux sulla tua macchina. Grazie alla sua **semplice installazione**, ai **facili aggiornamenti** e alla **flessibilità**, avrai un sistema potente e performante, adatto allo sviluppo, all'uso quotidiano e alla gestione dei bitcoin con strumenti come Electrum.

Manjaro combina **stabilità, velocità e sicurezza**, rimanendo **completamente gratuito**, il che lo rende una scelta ideale sia per i principianti che per gli utenti avanzati. Prenditi il tempo necessario per esplorare le sue varie caratteristiche e personalizzare il tuo ambiente in base alle tue esigenze. Se vuoi saperne di più e scoprire il sistema Arch Linux, ti consigliamo il nostro tutorial.


https://planb.academy/tutorials/computer-security/operating-system/arch-linux-7a3dc8a8-629b-4971-bb0d-4eab94f93973

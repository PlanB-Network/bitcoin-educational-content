---
name: Qubes
description: Un sistema operativo ragionevolmente sicuro.
---

![cover](assets/cover.webp)



Qubes OS è un sistema operativo libero e open-source progettato per gli utenti che mettono la sicurezza in cima alle loro priorità. La sua particolarità si basa su un'idea semplice ma radicale: invece di considerare il computer come un tutt'uno, ne divide l'uso in compartimenti indipendenti chiamati **_qubes_**.



Ogni qube funziona come un **ambiente virtuale isolato**, con un livello di fiducia e una funzione specifici. Pertanto, anche se un'applicazione viene compromessa, l'attacco rimane confinato al suo qube senza influenzare il resto del sistema.



> Se avete a cuore la sicurezza, Qubes OS è il miglior sistema operativo oggi disponibile. - **Edward Snowden**.

Tuttavia, l'installazione di Qubes OS richiede una preparazione maggiore rispetto all'installazione di un sistema operativo tradizionale. Bisogna verificare alcuni prerequisiti hardware, comprendere le basi della virtualizzazione e accettare un'esperienza diversa, in cui ogni attività quotidiana è pensata in termini di separazione. Ma una volta installato, Qubes OS offre una struttura robusta che ridefinisce il modo in cui si interagisce con il computer ogni giorno. In questa guida vi spiegheremo come funziona Qubes OS e come installarlo facilmente sul vostro sistema.



## Come funziona Qubes OS?



Qubes OS si basa sul principio della compartimentazione. Invece di utilizzare un unico sistema, si basa sull'hypervisor **Xen** per creare macchine virtuali isolate, chiamate qube. Ogni qube è dedicata a un compito specifico o a un livello di fiducia (lavoro, navigazione personale, operazioni bancarie ecc.). Questa separazione garantisce che qualsiasi compromissione in una qube non possa diffondersi alle altre, agendo come diversi computer indipendenti all'interno di un'unica macchina.



L'utente Interface è gestito da un dominio centrale e sicuro chiamato **dom0**. Questo dominio è totalmente isolato da Internet e rappresenta il cuore del sistema. Sebbene le finestre e i menu siano visualizzati dal dom0, l'esecuzione effettiva delle applicazioni avviene nelle rispettive qubes.



## I diversi tipi di qubes



Intorno al dom0 ruotano diversi tipi di qubes, ognuno con un ruolo molto specifico da svolgere.





- Le **AppVM** sono utilizzate per eseguire le applicazioni di tutti i giorni: l'utente può così separare la sua posta elettronica professionale dalla navigazione sul Web o dalle attività bancarie, con ogni ambiente che rimane totalmente indipendente dagli altri.





- Queste AppVM sono a loro volta basate su **TemplateVM**, che fungono da modelli centralizzati per l'installazione e l'aggiornamento del software, eliminando la necessità di gestire ogni qube separatamente.



Qubes OS integra anche macchine virtuali specializzate in **servizi di sistema**.





- La **NetVM** gestisce direttamente i **dispositivi di rete** e assicura la connessione a Internet. Spesso sono associate alle **FirewallVM**, che intervengono per **filtrare il traffico** e limitare l'esposizione di altre qubes.





- Le ServiceVM svolgono un ruolo simile, ad esempio nella gestione dei dispositivi USB, sempre con la stessa logica: isolare i componenti più rischiosi per ridurre la superficie di attacco.



Infine, per le attività occasionali o rischiose, Qubes OS offre **DisposableVM**. Queste qubes effimere vengono create al volo per **aprire un documento sospetto** o **visitare un sito dubbio**, quindi scompaiono completamente quando vengono chiuse, cancellando tutte le tracce e impedendo qualsiasi attacco persistente.



### Il meccanismo di copia sicura (qrexec)



Gli scambi tra le qubes si basano su **qrexec**, un sistema di comunicazione inter-VM progettato per la sicurezza. Invece di lasciare che le qubes comunichino liberamente, qrexec impone **politiche specifiche**: un file copiato da una AppVM all'altra, o un testo trasferito tramite gli appunti, passa sempre attraverso un canale monitorato e convalidato dal sistema. In questo modo, anche il semplice atto di copiare e incollare viene controllato per prevenire la diffusione di malware.



### Gestione del disco



Qubes OS utilizza un sistema ingegnoso per la gestione dello storage. Le TemplateVM contengono il software di base comune, mentre le AppVM aggiungono solo i dati personali e i file specifici. Questo riduce l'utilizzo dello spazio su disco e facilita gli aggiornamenti globali. Le DisposableVM, invece, utilizzano volumi temporanei che scompaiono completamente alla chiusura. Questo modello non solo garantisce una maggiore sicurezza, ma anche una gestione efficiente delle risorse.



## Perché scegliere Qubes OS?



I vantaggi di Qubes OS risiedono soprattutto nel suo modello di sicurezza unico. Il cuore di questo approccio è la compartimentazione, che protegge l'utente isolando ogni attività in macchine virtuali separate. In pratica, un'e-mail infetta o un sito web dannoso possono compromettere solo una singola qube, lasciando il resto del sistema e i dati personali completamente protetti. Questa architettura limita notevolmente gli attacchi complessi che, su un sistema convenzionale, potrebbero propagarsi liberamente.



Qubes OS offre anche una trasparenza e un controllo totali sull'ambiente digitale. Sapete esattamente quale software ha accesso a quale risorsa, sia essa la rete, un dispositivo USB o altri componenti sensibili. Il sistema integra di default funzioni di sicurezza avanzate, come la crittografia completa del disco, e facilita l'uso di servizi di anonimizzazione come il sistema operativo Whonix.



https://planb.academy/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Piuttosto che cercare di creare un sistema impenetrabile, Qubes OS si concentra sulla resilienza: incapsula i danni in caso di compromissione, riducendo il rischio per il resto del sistema. Questo approccio pragmatico rende Qubes OS una scelta preferenziale per gli utenti con esigenze di sicurezza elevate o che desiderano mantenere il massimo controllo sulla propria vita digitale.



## Installazione del sistema operativo Qubes



Prima di installare Qubes OS, è essenziale assicurarsi che l'hardware soddisfi i requisiti minimi, poiché il sistema si basa sulla virtualizzazione per isolare i computer. I componenti principali da controllare sono :




- Il **Processore**: Un processore a 64 bit compatibile con la virtualizzazione hardware (Intel VT-x o AMD-V).
- RAM: è necessario un minimo di 8 GB, ma si consiglia una RAM di 16 GB o più per eseguire più qube contemporaneamente.
- **Spazio di archiviazione**: minimo 36 GB, idealmente 128 GB su un'unità SSD per ottimizzare le prestazioni.



Per installare Qubes OS, scaricare l'immagine ISO ufficiale dal sito Qubes OS [sito ufficiale](https://www.qubes-os.org/downloads/). È essenziale verificare l'integrità dell'ISO utilizzando le firme GPG fornite, per assicurarsi che il file non sia stato manomesso e che il download sia sicuro.



https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Una volta verificata la ISO, è necessario creare un supporto di installazione avviabile, di solito una chiavetta USB. A tale scopo, scaricare e installare software come **Rufus** su Windows o **Etcher** su Windows, Linux o macOS. Questi strumenti consentono di copiare l'ISO sulla chiavetta USB in modo che sia avviabile.



Prima di iniziare l'installazione, è necessario configurare il **BIOS o UEFI** del computer per **abilitare la virtualizzazione** e consentire l'avvio da USB. A seconda del modello di macchina, potrebbe essere necessario **disabilitare Secure Boot**, poiché Qubes OS potrebbe non avviarsi con questa opzione abilitata.



![0_02](assets/fr/02.webp)



Una volta soddisfatte queste condizioni, riavviare il computer e accedere al BIOS/UEFI premendo immediatamente **Esc**, **Del**, **F9**, **F10**, **F11** o **F12** (a seconda del produttore). Nel menu di avvio, selezionare la chiave USB come dispositivo di avvio per lanciare l'installazione del sistema operativo Qubes.



**Schermo di avvio**


All'avvio dalla chiavetta USB, si accede direttamente al menu **GRUB**, dove è possibile scegliere l'azione da eseguire. Utilizzando i tasti freccia della tastiera, selezionare "Install Qubes OS" e premere "Invio".



![0_03](assets/fr/03.webp)



**Scelta della lingua** :



All'avvio dell'installazione, il primo passo è quello di **scegliere la lingua** e la **variante regionale** adatte alla propria configurazione. In questo modo si garantisce che le opzioni del sistema e dell'installazione vengano visualizzate correttamente nella lingua preferita.



![0_04](assets/fr/04.webp)



**Configurazione parametri** :



A questo punto, dovrete configurare una serie di Elements prima di lanciare l'installazione sul vostro computer.



![0_05](assets/fr/05.webp)



**Disposizione della tastiera** :



Fare clic sull'opzione **Tastiera**, quindi selezionare il **display** appropriato per il proprio computer. Una volta effettuata la scelta, fare clic su **Terminato** per passare alla fase successiva.



**Scelta della destinazione** :



Selezionare l'opzione "Destinazione installazione" per scegliere il disco su cui installare Qubes OS. Per impostazione predefinita, il partizionamento avviene automaticamente, consentendo di rimuovere tutti i dati dal disco e di installare il sistema su di esso. È tuttavia possibile scegliere **Personalizzato** o **Personalizzazione avanzata** per eseguire un partizionamento personalizzato. Fare quindi clic su "Fatto". Il sistema chiederà di impostare una **password**, che funge da Layer di sicurezza per crittografare i dati. Assicurarsi di scegliere una password complessa e unica.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Selezionare il formato della data e dell'ora** :


Fare clic sull'opzione Ora e data, quindi selezionare il proprio fuso orario. È inoltre possibile scegliere il formato orario preferito: 24h o 12h.



![0_08](assets/fr/08.webp)



**Creazione dell'account utente** :


Cliccate su **Crea utente** per creare il vostro **primo account**, che vi permetterà di accedere a Qubes OS.



![0_09](assets/fr/09.webp)



**Attivare l'account di root** :


È anche possibile **abilitare l'account root** impostando una password separata per l'amministrazione.



![0_10](assets/fr/10.webp)



Una volta effettuate queste impostazioni, fare clic su **Avvia installazione** per avviare il processo.



![0_11](assets/fr/11.webp)



Attendere il **termine dell'installazione**, quindi fare clic su **riavvia il sistema** per completare l'installazione e avviare Qubes OS.



![0_12](assets/fr/12.webp)



**Configurazione aggiuntiva** :


Dopo il riavvio, Qubes OS chiede di finalizzare i **modelli predefiniti e la configurazione di qubes**. Inserire la password definita per criptare il disco.



![0_13](assets/fr/13.webp)



Quindi, iniziate a selezionare il **TemplateVM** che desiderate installare. Le opzioni più comuni includono **Debian 12 Xfce**, **Fedora 41 Xfce** e **Whonix 17**, quest'ultimo consigliato per gli usi che richiedono **anonimato e sicurezza di rete**. È anche possibile definire il **modello predefinito**, che servirà come base per la creazione di nuove **AppVM**.



![0_14](assets/fr/14.webp)



Nella sezione **Configurazione principale**, si può scegliere di creare automaticamente le qubes essenziali del sistema, come **sys-net**, **sys-firewall** e **default DisposableVM**. È consigliabile attivare l'opzione per rendere **sys-firewall e sys-usb usa e getta**, per limitare l'esposizione del dispositivo e della rete in caso di compromissione. È inoltre possibile creare **AppVM** predefinite, come **personal**, **work**, **untrusted** e **vault**, per organizzare le attività in base al loro livello di fiducia.



![0_15](assets/fr/15.webp)



Qubes OS consente anche di creare un **qube dedicato ai dispositivi USB** (sys-usb) e di configurare i **qube Whonix Gateway e Workstation** per proteggere le comunicazioni attraverso la rete Tor. Per gli utenti avanzati, la sezione **Configurazione avanzata** consente di creare un **LVM thin pool** per gestire in modo efficiente lo spazio su disco tra le qube.



Una volta configurate tutte le opzioni, fare clic su **Complete**, quindi su **Finish configuration**. Attendere che il sistema applichi queste impostazioni. Verrà quindi richiesto di **fare il login al proprio account utente** e l'ambiente Qubes OS sarà pronto per l'uso, sicuro e correttamente isolato per le varie attività.



![0_17](assets/fr/17.webp)



Il sistema operativo è ora installato e pronto all'uso.



![0_18](assets/fr/18.webp)



## Creare un qube sul sistema



Per creare un qube, il processo è gestito dallo strumento **Qube Manager**, accessibile dal menu Start. Nella finestra dello strumento, è sufficiente fare clic sull'icona **Create qube** per aprire una nuova finestra di configurazione. Per prima cosa, inserire un nome per il qube, ad esempio "perso-web" o "work", per identificarne l'uso.



Successivamente, si selezionerà il suo **Tipo**, di solito **AppVM** per le attività di routine, o **DisposableVM** per un uso temporaneo. È fondamentale scegliere il **Template** su cui si baserà la qube, ad esempio "fedora-39" o "debian-12", poiché questo fornirà il sistema operativo e il software. Si designerà anche la **NetVM**, che è la qube responsabile dell'accesso a Internet, di default **sys-firewall**.



Infine, dopo aver regolato le dimensioni della memoria e la RAM, se necessario, un semplice clic su **OK** avvierà il processo di creazione. Una volta completato il processo, la nuova qube sarà visibile nell'elenco e pronta all'uso.



In conclusione, Qubes OS non è un normale sistema operativo, ma una soluzione di sicurezza all'avanguardia che ripensa l'architettura del personal computer. Il suo approccio, basato sulla compartimentazione e sull'isolamento attraverso la virtualizzazione, offre una protezione senza pari contro le minacce più sofisticate. Segmentando l'ambiente di lavoro in quadre specializzate per ogni attività, garantisce che il malware non possa diffondersi e mettere in pericolo l'intero sistema.



Se avete bisogno di navigare sul web in modo sicuro, di proteggere informazioni sensibili o di lavorare con diversi livelli di fiducia, Qubes OS fornisce un quadro resiliente e trasparente. Adottando buone pratiche e sfruttando appieno le sue funzionalità, avrete una **fortezza digitale** adatta alle minacce moderne. Per saperne di più sulla protezione dei dati e della privacy.



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
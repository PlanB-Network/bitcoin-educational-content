---
name: VirtualBox
description: Installare VirtualBox su Windows 11 e creare la prima macchina virtuale
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Florian Burnel pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale



___




## I. Presentazione



In questa esercitazione, impareremo a installare VirtualBox su Windows 11 per creare macchine virtuali, sia per eseguire Windows 10, Windows 11, Windows Server o una distribuzione Linux (Debian, Ubuntu, Kali Linux, ecc.).



Questo tutorial introduttivo a VirtualBox vi aiuterà a iniziare a utilizzare questa soluzione di virtualizzazione open source sviluppata da Oracle, che è completamente gratuita. In seguito, verranno messe online altre esercitazioni per approfondire l'argomento.



Quando si tratta di virtualizzare una workstation, sia a scopo di test nell'ambito di un progetto che durante gli studi di informatica, VirtualBox è chiaramente una buona soluzione. È anche un'alternativa ad altre soluzioni come Hyper-V, integrato in Windows 10 e Windows 11 (oltre che in Windows Server), e VMware Workstation (a pagamento) / VMware Workstation Player (gratuito per uso personale).



La mia configurazione: **una workstation Windows 11 dove installerò VirtualBox**, ma è possibile installare VirtualBox su Windows 10 (o una versione precedente), così come su Linux. Per quanto riguarda le macchine virtuali, VirtualBox supporta un'ampia gamma di sistemi, tra cui Windows (ad esempio Windows 10, Windows 11, Windows Server 2022, ecc.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, ecc.), BSD (PfSense) e macOS.



## II. Scaricare VirtualBox per Windows 11



Per scaricare VirtualBox per l'installazione su una macchina Windows, c'è solo un buon Address: il [sito ufficiale di VirtualBox](https://www.virtualbox.org/wiki/Downloads) nella sezione "**Downloads**". Basta fare clic su "Windows hosts" per avviare il download dell'eseguibile, che ha una dimensione di poco superiore a 100 MB.



![Image](assets/fr/025.webp)



## III. Installazione di VirtualBox su Windows 11



### A. Installazione di VirtualBox



L'installazione di VirtualBox** è semplice e la procedura è la stessa per tutte le versioni di Windows. Iniziare lanciando l'eseguibile di VirtualBox appena scaricato, quindi fare clic su "**Avanti**".



![Image](assets/fr/026.webp)



Questa installazione è personalizzabile, ma vi consiglio di installare tutte le funzioni: è il caso della selezione predefinita. Nell'immagine sottostante, si possono vedere vari Elements, tra cui:





- VirtualBox USB Support** per consentire a VirtualBox di supportare i dispositivi USB
- VirtualBox Bridged Network** per integrare il supporto di rete in modalità "Bridge" (la macchina virtuale può connettersi direttamente alla rete locale)
- VirtualBox Host-Only Network** per integrare il supporto di rete in modalità "Host-Only" (in questa modalità la macchina virtuale può comunicare solo con l'host fisico Windows 11 e con altre macchine virtuali)



Fare clic su "**Avanti**" per continuare.



![Image](assets/fr/001.webp)



Fare clic su "**Sì**", tenendo presente che **la rete sarà interrotta per un momento sulla macchina Windows 11**, mentre VirtualBox esegue le modifiche alla rete per supportare diversi tipi di rete, compresa la modalità Bridge.



![Image](assets/fr/002.webp)



Una volta confermata, l'installazione inizierà... Apparirà una notifica "**Vuoi installare il software di questo dispositivo?**". Spuntare l'opzione "**Sempre fiducia nel software di Oracle Corporation**" e fare clic su "**Installa**". VirtualBox deve installare diversi driver sul computer.



![Image](assets/fr/003.webp)



L'installazione è ora completa! Selezionare l'opzione "**Avvia Oracle VM VirtualBox 6.1.34 dopo l'installazione**" e fare clic su "**Clicca**" per avviare il software.



![Image](assets/fr/004.webp)



### B. Aggiungere il pacchetto di estensioni



Sempre sul sito ufficiale di VirtualBox (vedi link precedente), è possibile scaricare un pacchetto di estensione ufficiale, accessibile nella sezione "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" facendo clic sul link "**Tutte le piattaforme supportate**". Questo pacchetto consente di aggiungere ulteriori funzionalità a VirtualBox: non è obbligatorio aggiungerlo, ma può essere utile! Ad esempio, include il supporto per l'USB 3.0 nelle macchine virtuali, il supporto per la webcam e la crittografia del disco.



Aprire VirtualBox, fare clic su "**File**" e poi su "**Impostazioni**" nel menu.



![Image](assets/fr/005.webp)



Fare clic su "**Estensioni**" a sinistra (1), quindi sul pulsante "**+**" a destra (2) per **caricare il pacchetto di estensioni di VirtualBox** appena scaricato (3).



![Image](assets/fr/006.webp)



Confermare facendo clic sul pulsante "**Installazione**".



![Image](assets/fr/007.webp)



Fare clic su "**OK**": il pacchetto di estensioni ufficiale è ora installato sull'istanza di VirtualBox!



![Image](assets/fr/008.webp)



Passiamo alla creazione della nostra prima macchina virtuale.



## IV. Creare la prima macchina virtuale VirtualBox



Per creare una nuova macchina virtuale su VirtualBox, è sufficiente fare clic sul pulsante "**Nuovo**" per avviare la creazione guidata della macchina virtuale. Poiché è la prima volta che si avvia VirtualBox, vorrei fornire qualche dettaglio in più su Interface e sugli altri pulsanti.





- Impostazioni**: configurazione generale di VirtualBox (cartella VM predefinita, gestione degli aggiornamenti, lingua, reti NAT, estensioni, ecc.)
- Importazione**: importa un dispositivo virtuale in formato OVF
- Esporta**: esporta una macchina virtuale esistente in formato OVF per creare un dispositivo virtuale
- Aggiungi**: aggiunge una macchina virtuale esistente all'inventario di VirtualBox, in formato standard VirtualBox (.vbox) o in formato XML



A sinistra, la sezione "**Strumenti**" dà accesso a **funzioni avanzate, in particolare per la gestione della rete virtuale, ma anche per la gestione dello storage delle macchine virtuali**. Sotto la voce "**Strumenti**" verranno aggiunte in seguito le macchine virtuali.



![Image](assets/fr/009.webp)



### A. Processo di creazione della macchina virtuale



**Come promemoria, VirtualBox supporta una moltitudine di sistemi operativi, tra cui Windows, Linux e BSD. In questo esempio, creerò una macchina virtuale per Windows 11. È necessario compilare diversi campi:





- Nome**: nome della macchina virtuale (è il nome che verrà visualizzato in VirtualBox)
- Cartella macchina**: dove memorizzare la macchina virtuale, sapendo che in questa posizione verrà creata una sottocartella con il nome della macchina virtuale
- Tipo**: il tipo di sistema operativo, a seconda del sistema operativo che si desidera installare
- Versione**: la versione del sistema che si desidera installare, in questo caso Windows 11, quindi "**Windows11_64**"



Fare clic su "**Avanti**" per continuare.



![Image](assets/fr/010.webp)



A seconda del sistema operativo selezionato nel passaggio precedente, **VirtualBox fornisce raccomandazioni sulle risorse da allocare alla macchina virtuale**. In questo caso, si tratta della RAM che si desidera allocare alla macchina virtuale. Assumiamo 4 GB, perché questo è effettivamente consigliato per Windows 11, ma se siete a corto di risorse, specificate invece 2 GB. **Continua



**Nota**: le risorse assegnate alla macchina virtuale possono essere modificate in seguito.



![Image](assets/fr/011.webp)



Per quanto riguarda il disco virtuale Hard, stiamo partendo da zero, quindi dobbiamo scegliere "**Create virtual Hard disk now**" in modo che la macchina virtuale abbia spazio di archiviazione per installare il sistema operativo e memorizzare i dati. Fare clic su "**Crea**".



![Image](assets/fr/012.webp)



VirtualBox supporta tre diversi formati per i dischi virtuali Hard, il che rappresenta una differenza sostanziale rispetto ad altre soluzioni come VMware e Hyper-V. È possibile scegliere tra tre formati:





- VDI**, il formato ufficiale di VirtualBox
- VHD**, che è il formato ufficiale di Hyper-V, anche se il nuovo formato VHDX viene utilizzato più spesso in questi giorni
- VMDX** è il formato ufficiale di VMware per VMware Workstation e VMware ESXi



Per creare una macchina virtuale che verrà utilizzata solo su questa istanza di VirtualBox, scegliere "**VDI**". D'altra parte, se il disco virtuale Hard deve essere collegato a un host Hyper-V in un secondo momento, può essere una buona idea iniziare con il formato VHD per evitare di doverlo convertire. Fare clic su "**Avanti**".



![Image](assets/fr/013.webp)



**Il disco virtuale può essere di dimensioni dinamiche o fisse**. Quando è dinamico, il file che rappresenta **il disco virtuale (qui un file .vdi) cresce man mano che i dati vengono scritti sul disco** fino a raggiungere la dimensione massima, ma non si riduce se i dati vengono cancellati. Al contrario, quando è di dimensioni fisse, **lo spazio di archiviazione totale viene allocato immediatamente (e quindi riservato)**, il che consente prestazioni leggermente superiori, ma richiede più tempo alla prima creazione del disco virtuale.



Personalmente, per le macchine virtuali di prova con VirtualBox, considero sufficiente la modalità "**Dynamically allocated**".



![Image](assets/fr/014.webp)



**Il passo successivo consiste nello specificare le dimensioni del disco virtuale**, tenendo presente che per impostazione predefinita il disco verrà memorizzato nella directory della macchina virtuale (che può essere modificata in questa fase). Ho indicato una dimensione di 64 GB per soddisfare i requisiti di Windows 11, ma anche in questo caso è possibile assegnare una dimensione inferiore. Fate clic su "**Crea**" per creare la macchina virtuale!



![Image](assets/fr/015.webp)



A questo punto, la macchina virtuale è nel nostro inventario, è configurata, ma il sistema operativo non è installato. Dobbiamo finalizzare la configurazione della macchina virtuale prima di avviarla.



### B. Assegnazione di un'immagine ISO a una macchina virtuale VirtualBox



Per installare Windows 11, o qualsiasi altro sistema, abbiamo bisogno di sorgenti di installazione. Nella maggior parte dei casi, per installare un sistema operativo si utilizza un'immagine disco in formato ISO. **È necessario caricare l'immagine ISO di Windows 11 nell'unità DVD virtuale della nostra macchina virtuale



Fare clic sulla macchina virtuale nell'inventario di VirtualBox (1), quindi sul pulsante "**Configurazione**" (2), che dà accesso alla configurazione generale di questa macchina virtuale. Questo menu serve per gestire le risorse (ad es. aumentare la RAM, configurare la CPU, ecc.). Fare clic su "**Storage**" a sinistra (3), sull'unità DVD dove per il momento è scritto "**Empty**" (4), quindi fare clic sull'icona a forma di DVD (5) e su "**Choose a disk file**".



![Image](assets/fr/016.webp)



Selezionare l'immagine ISO del sistema operativo che si desidera installare, quindi fare clic su OK. Questo è il risultato:



![Image](assets/fr/017.webp)



Rimanete nella sezione "**Configurazione**" della VM, ho ancora alcune cose da spiegare.



### C. Connessione di rete della macchina virtuale



Andare alla sezione "**Rete**" a sinistra. Questa sezione consente di gestire la rete della macchina virtuale: numero di interfacce di rete virtuali (fino a 4 per VM), MAC Address e modalità di accesso alla rete (NAT, bridge access, rete interna, ecc.). **Se si desidera che la macchina virtuale abbia accesso a Internet, selezionare "NAT" o "Bridge Access "**, ma questa seconda modalità richiede che un server DHCP sia attivo sulla rete, altrimenti si dovrà configurare un IP Address manualmente.



Nota: tornerò sulla parte relativa alla rete in modo più dettagliato in un articolo dedicato.



![Image](assets/fr/018.webp)



### D. Il numero di processori virtuali



Come un computer fisico, una macchina virtuale ha bisogno di RAM, di un disco Hard e di un processore per funzionare. Quando abbiamo creato la macchina virtuale, avrete notato che la procedura guidata non includeva la configurazione del processore. Tuttavia, questa può essere configurata in qualsiasi momento tramite la scheda "**System**", quindi "**Processor**", dove è possibile scegliere il numero di processori virtuali.



Nota: l'opzione "**Abilita VT-x/AMD-v nested**" è necessaria per la virtualizzazione nidificata.



Nel mio caso, la macchina virtuale ha 2 processori virtuali:



![Image](assets/fr/019.webp)



**Non esitate a dare un'occhiata alle altre sezioni del menu di configurazione.



### E. Primo avvio e installazione del sistema operativo



Per avviare una macchina virtuale, è sufficiente selezionarla nell'inventario e fare clic sul pulsante "**Avvia**". Si aprirà una seconda finestra che fornirà una panoramica visiva della macchina virtuale.



![Image](assets/fr/020.webp)



Ricevo un brutto errore e la mia macchina virtuale non si avvia! L'errore è "Login failed for virtual machine..." con i seguenti dettagli:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



In realtà, questo è normale perché **la funzione di virtualizzazione non è abilitata sul mio computer**! Per risolvere questo problema, è necessario riavviare il computer per accedere al BIOS e abilitare la virtualizzazione.



![Image](assets/fr/021.webp)



Senza aspettare, riavvio il computer e **premo il tasto "SUPPR" per accedere al BIOS** (il tasto può variare a seconda della macchina e potrebbe essere F2, ad esempio) della mia scheda madre ASUS. Per attivare la virtualizzazione, nel mio caso è necessario attivare la "Modalità SVM". Anche in questo caso, da una scheda madre all'altra, da un produttore all'altro, il nome può cambiare. Cercate una funzione che faccia riferimento a **AMD-V** (per una CPU AMD) o **Intel VT-x** (per una CPU Intel).



![Image](assets/fr/022.webp)



Una volta fatto questo, salvare la modifica e riavviare la macchina fisica... Questa volta, **VirtualBox può avviare la macchina virtuale** e caricare l'immagine ISO di Windows per installare il sistema operativo! 🙂



![Image](assets/fr/023.webp)



Sul nostro host fisico Windows 11, dove è installato VirtualBox, possiamo vedere che la cartella della macchina virtuale Windows 11 contiene vari file.





- Il file VBOX** (in formato XML) corrispondente alla configurazione della macchina virtuale (RAM, CPU, ecc.)
- Il file VBOX-PREV** è un backup della configurazione precedente
- Il file VDI** corrisponde al disco virtuale Hard in modalità dinamica, quindi attualmente è di soli 13 GB, mentre la sua dimensione massima è di 64 GB
- Il file NVRAM** contiene lo stato del BIOS della macchina virtuale, equivalente alla memoria non volatile di una macchina fisica



![Image](assets/fr/024.webp)



## V. Conclusioni



**VirtualBox è ora attivo e funzionante sulla nostra macchina fisica con Windows 11! Non resta che approfittarne e creare macchine virtuali! ** Tornerò sull'installazione di Windows 11 in una macchina virtuale VirtualBox in un altro articolo. Per Windows 10, Windows Server o una distribuzione Linux (Ubuntu, Debian, ecc.), lasciatevi guidare da noi!
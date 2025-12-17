---
name: Start9

description: Esercitazione sulla configurazione di un server privato Start9

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Ecco un video tutorial di Southern Bitcoiner, una video guida che mostra come configurare e utilizzare un server personale Start9 / StartOS, e come gestire un nodo bitcoin.*


## 1️⃣ Introduzione


### Che cos'è esattamente Start9?


Start9 è una società fondata nel 2020, nota soprattutto per aver sviluppato [**StartOS**,](https://github.com/Start9Labs/start-os) un sistema operativo basato su Linux progettato per i server personali. Consente agli utenti di auto-ospitare facilmente un'ampia gamma di servizi software, come i nodi Bitcoin e Lightning, le app di messaggistica o i gestori di password, mantenendo il pieno controllo sui propri dati ed eliminando la dipendenza da piattaforme tecnologiche centralizzate. StartOS presenta un'interfaccia intuitiva basata su browser, un Marketplace curato per l'installazione di servizi e strumenti integrati per la privacy come l'integrazione di Tor e la crittografia HTTPS a livello di sistema. Start9 fornisce anche dispositivi hardware precaricati con il sistema operativo, anche se il software può essere installato su hardware compatibile o macchine virtuali (VM).


### Quali sono le opzioni disponibili?


Start9 offre opzioni di implementazione sia precostituite che fai-da-te. Il [**Server One**](https://store.start9.com/collections/servers/products/server-one) e il [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) sono dispositivi hardware ufficiali con componenti ad alte prestazioni: il Server One utilizza un processore **AMD Ryzen 7 5825U** con RAM configurabile (16GB-64GB) e storage (2TB-4TB NVMe SSD), mentre il Server Pure è dotato di un **Intel i7-10710U**, anch'esso con opzioni di RAM e storage configurabili. Entrambi includono **assistenza tecnica a vita** se acquistati direttamente da Start9. Per gli utenti che preferiscono la flessibilità, StartOS può essere installato gratuitamente su un'ampia gamma di hardware esistente, tra cui laptop, desktop, mini PC e computer single-board, o all'interno di macchine virtuali.


![image](assets/en/01.webp)


### Quali sono le differenze con Umbrel?


StartOS e Umbrel semplificano entrambi l'installazione di servizi self-hosted, ma differiscono per architettura e caratteristiche. Umbrel funziona come un livello applicativo su sistemi Debian/Ubuntu o macchine virtuali, mentre Start9 è un sistema operativo dedicato che richiede l'installazione diretta su hardware o macchine virtuali. Umbrel presenta un'interfaccia raffinata, ispirata a macOS, mentre Start9 privilegia un design funzionale e minimale. Umbrel offre una maggiore [selezione di applicazioni](https://apps.umbrel.com/), mentre il [Marketplace di Start9](https://marketplace.start9.com/) compensa con funzionalità tecniche avanzate. Start9 semplifica l'accesso alle impostazioni avanzate attraverso moduli UI convalidati, riducendo la necessità di interazione con la riga di comando. Eccelle anche nella gestione dei backup con backup di sistema criptati in un solo clic, una caratteristica che Umbrel non possiede in modo nativo. StartOS fornisce strumenti di monitoraggio integrati e applica la crittografia HTTPS per l'accesso alla rete locale, migliorando la sicurezza. Umbrel utilizza HTTP non criptato a livello locale, anche se entrambe le piattaforme supportano l'accesso remoto sicuro tramite Tor. Umbrel è adatto agli utenti che danno priorità a un ricco ecosistema di app e a un'interfaccia utente raffinata. Start9 è una scelta forte per chi apprezza la sicurezza, la configurabilità, l'affidabilità del backup e la gestione avanzata dei servizi senza richiedere competenze a riga di comando. Per saperne di più su Umbrel e sulle differenze con Start9, visitate questo corso:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ Prerequisiti per il fai-da-te: Specifiche minime e consigliate


Per un uso di base con servizi minimi, le **specifiche minime** sono: **1 core vCPU (2.0GHz+ boost), 4GB di RAM, 64GB di storage** e una porta Ethernet. Detto questo, consiglio di andare ben oltre, soprattutto se si sta eseguendo un nodo Bitcoin. Personalmente, ho iniziato con 1TB e ho esaurito rapidamente lo spazio. È meglio puntare a **almeno 2TB di spazio di archiviazione**, insieme a una CPU **quad-core (2,5GHz+)** e **8GB+ di RAM**. Fanno un'enorme differenza in termini di prestazioni e longevità. Se volete approfondire, ecco un thread aggiornato della comunità su [Hardware in grado di eseguire StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Download e flashing del firmware


Per iniziare la configurazione, utilizzare un computer separato per visitare il [sito web di Start9](https://start9.com/) e navigare nella sezione della documentazione facendo clic su `DOCS`. Da qui, accedere alle `Guide di flashing` per trovare la versione appropriata di StartOS. Sono disponibili due opzioni:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Questa esercitazione tratta l'opzione `x86/ARM`.


L'ultima versione del sistema operativo può essere scaricata dalla [pagina di rilascio di Github](https://github.com/Start9Labs/start-os/releases/latest). sono disponibili anche versioni [pre-release](https://github.com/Start9Labs/start-os/releases) per gli utenti che desiderano testare le nuove funzionalità. In fondo alla pagina, alla voce `Assets`, scaricare il file `x86_64` o `x86_64-nonfree.iso`.  L'immagine `x86_64-nonfree.iso` contiene software non libero (closed-source) necessario per il Server One e per la maggior parte dell'hardware fai-da-te, in particolare per la grafica e il supporto dei dispositivi di rete.


Si consiglia di verificare l'integrità del file confrontando il suo hash SHA256 con quello elencato su GitHub. Per Linux si può usare il comando `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso`, mentre per altri sistemi operativi si rimanda alla documentazione.


Dopo aver scaricato e verificato l'immagine di StartOS, è necessario eseguire il flashing su un'unità USB. il software consigliato per questa operazione è `BalenaEtcher`. Si tratta di uno strumento gratuito e open-source per la scrittura di file immagine del sistema operativo su unità USB e schede SD, disponibile per Windows, macOS e Linux. Scaricare la versione appropriata dal sito ufficiale [Balena Etcher](https://www.balena.io/etcher/) ed eseguire il programma di installazione. Collegare l'unità USB o la scheda SD di destinazione, aprire Balena Etcher e fare clic su "Flash from file" per selezionare l'immagine del sistema operativo scaricata. Etcher rileverà automaticamente le unità collegate; selezionare la destinazione corretta se sono presenti più unità. Fare clic su `Flash!` per iniziare a scrivere l'immagine. Etcher convalida automaticamente il processo di scrittura al termine. Al termine, rimuovere in modo sicuro l'unità e utilizzarla per avviare il dispositivo.


![image](assets/en/19.webp)


## 4️⃣ Impostazione iniziale


Per la configurazione iniziale, consultare la pagina Start9 [documentazione](https://docs.start9.com/0.3.5.x/) alla voce `USER MANUAL` seguita da `Getting Started - Initial Setup`.  Questa guida ufficiale deve essere consultata per ottenere le informazioni più aggiornate.


Vengono presentate due opzioni:



- Ricominciare da capo
- Opzioni di recupero


Per un'installazione di un nuovo server, selezionare `Start Fresh`. Per prima cosa, collegare il server all'alimentazione e a un cavo Ethernet. Assicurarsi che il computer utilizzato per l'installazione sia sulla stessa rete locale. Rimuovere l'unità USB appena flashata dal computer e inserirla nel server.


È possibile controllare il server in remoto da qualsiasi computer della stessa rete. Aprire un browser Web e navigare su `http://start.local`.


**Nota**: Se si verificano problemi di connessione con questo indirizzo, spesso ciò è dovuto alle reti domestiche che non risolvono i nomi di dominio `.local`. Il problema può essere risolto accedendo direttamente al server tramite il suo indirizzo IP. L'IP può essere trovato accedendo all'interfaccia di amministrazione del router (in genere a `192.168.1.1` o a un indirizzo simile) e individuando il dispositivo nell'elenco dei client DHCP o della mappa di rete. Quindi, inserire l'indirizzo IP completo (ad esempio, `http://192.168.1.105`) nel browser. In questo modo si evita la risoluzione DNS. Se i problemi persistono, consultare la pagina [Problemi comuni](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) o [contattare l'assistenza](https://start9.com/contact/)


Viene visualizzata la schermata di impostazione di StartOS. Fare clic su `Start Fresh` per iniziare la configurazione del nuovo server.


![image](assets/en/03.webp)


Il passo successivo consiste nel selezionare l'unità di memoria in cui verranno memorizzati i dati di StartOS.


![image](assets/en/04.webp)


Impostare una `Password` forte per il server. Registrarla come consigliato da Start9, quindi fare clic su `FINISH`.


![image](assets/en/05.webp)


Una schermata mostrerà che StartOS sta inizializzando e impostando il server. Il passo successivo è quello di "scaricare le informazioni sull'indirizzo", poiché l'indirizzo `start.local` serve solo per l'impostazione e non funzionerà più.


![image](assets/en/06.webp)


Il file di configurazione contiene due indirizzi di accesso critici: uno per la `rete locale (LAN)` e un altro per l'accesso sicuro tramite `Tor`. Entrambi gli indirizzi devono essere salvati in un gestore di password sicuro. Il passo successivo è quello di `affidarsi alla Root CA`. Aprire una nuova scheda del browser e seguire le istruzioni per fidarsi della Root CA e accedere. Il certificato della CA radice può anche essere scaricato facendo clic su `Download certificate` nel file scaricato.


## 5️⃣ Fiducia nella CA radice


Dopo aver scaricato il certificato, la `Root CA` del server deve essere attendibile dal sistema operativo. Fare clic su `Vedi istruzioni` e trovare le linee guida per il sistema operativo specifico.


![image](assets/en/07.webp)


Per un sistema Linux, si utilizzano i seguenti comandi. Per prima cosa, aprire un Terminale e installare i pacchetti necessari:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Navigare nella directory in cui è stato scaricato il certificato, in genere `~/Downloads`. Eseguire questi comandi per aggiungere il certificato all'archivio di fiducia del sistema operativo. Passare alla cartella dei download con `cd ~/Downloads`. Creare la directory necessaria con `sudo mkdir -p /usr/share/ca-certificates/start9`. Copiare il file del certificato, sostituendo `nome-tuo.crt` con il nome effettivo del file, usando `sudo cp "nome-tuo.crt" /usr/share/ca-certificates/start9/`. Registrare il certificato in modo permanente aggiungendo il suo percorso alla configurazione del sistema con `sudo bash -c "echo 'start9/nome-filtro.crt' >> /etc/ca-certificates.conf"`. Infine, ricostruire il trust store con `sudo update-ca-certificates`. È fondamentale utilizzare il nome effettivo del certificato e verificare tutti i percorsi prima di eseguire questi comandi. Questo processo stabilisce una fiducia permanente per le connessioni HTTPS del server Start9.


Un'installazione riuscita sarà indicata da un output che dice `1 aggiunto`. La maggior parte delle applicazioni sarà quindi in grado di connettersi in modo sicuro tramite `https`. Se si usa Firefox, è necessario un ulteriore [passo finale](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). Per Chrome o Brave, è necessario un altro [passo finale] (https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) per configurare il browser in modo che rispetti la Root CA. Verificare la connessione aggiornando la pagina. Se il problema persiste, uscire e riaprire il browser prima di rivisitare la pagina.


![image](assets/en/08.webp)


## 6️⃣ Come iniziare con StartOS


A questo punto dovrebbe essere possibile accedere utilizzando una connessione sicura HTTPS. Inserire la `Password` per accedere alla `Welcome Screen`.


![image](assets/en/09.webp)


Questa schermata fornisce utili scorciatoie per iniziare. La barra laterale sinistra contiene le voci di menu principali per la navigazione.


## sistema 7️⃣


La scheda Sistemi di StartOS consente di accedere alle funzioni principali del sistema per la gestione del server personale. Offre strumenti per la manutenzione, la sicurezza, la diagnostica e la configurazione del sistema senza richiedere competenze a livello di riga di comando.


La sezione `Backup` consente di creare backup completi del sistema, compresi servizi, configurazioni e dati, che possono essere ripristinati in seguito. Ciò è essenziale per il ripristino di emergenza o per la migrazione a un nuovo hardware. I backup possono essere archiviati su unità esterne e sono crittografati con la password principale.


La sezione "Gestione" nella scheda Sistemi consente di controllare le funzioni chiave del sistema. Gli utenti possono verificare e applicare manualmente gli aggiornamenti di StartOS, mantenendo il controllo sul processo di aggiornamento del sistema. È possibile caricare in sideload servizi personalizzati o di terze parti non disponibili sul mercato ufficiale. Se il server non è collegato via Ethernet, le impostazioni Wi-Fi possono essere configurate da questa sezione. Gli utenti avanzati possono abilitare l'accesso SSH per la gestione del sistema a livello di terminale.


![image](assets/en/10.webp)


La sezione `Insights` fornisce un monitoraggio in tempo reale delle prestazioni e dello stato di salute del server, mostrando l'utilizzo della CPU, della RAM e del disco tramite grafici. Mostra anche la temperatura del sistema, utile per i dispositivi come il Raspberry Pi che non hanno un raffreddamento attivo. Le metriche del tempo di attività e della media del carico aiutano a valutare la stabilità del sistema, mentre i registri in tempo reale sono disponibili per la risoluzione di problemi di servizio o di sistema.


La sezione `Supporto` offre accesso alle FAQ integrate, alla documentazione ufficiale e ai canali di supporto della comunità. I registri di debug possono essere scaricati da questa sezione per essere condivisi con l'assistenza Start9 per una più rapida risoluzione dei problemi.


![image](assets/en/11.webp)


## 8️⃣ Marketplace


Il `Mercato` è utilizzato per scoprire, installare e gestire i servizi sul server personale. Fornisce accesso a software come Bitcoin Core, BTCPay Server ed electrs. StartOS supporta diversi marketplace, tra cui il registro ufficiale di Start9 e i registri gestiti dalla comunità. Questi possono essere aggiunti facendo clic su "Cambia" e passando al "Registro della comunità", che fornisce l'accesso a una gamma più ampia di servizi.


![image](assets/en/12.webp)


## 9️⃣ Installazione di un nodo completo Bitcoin


L'installazione di un Bitcoin full node su StartOS offre la piena sovranità sull'esperienza Bitcoin. Consente la convalida delle transazioni e migliora la privacy e la sicurezza eliminando la dipendenza da servizi esterni che possono registrare le attività. Si ottiene il pieno controllo sulle transazioni, consentendo loro di essere trasmesse direttamente alla rete. L'opzione predefinita è `Bitcoin Core`, che si integra in modo nativo con StartOS e consente la connessione con portafogli come Specter, Sparrow o Electrum per una configurazione di auto-custodia. Un'alternativa, `Bitcoin Knots`, è disponibile anche attraverso il Community Registry.


Per installare Bitcoin Core, visitate il Marketplace. Nel registro di default, trovare e installare il servizio Bitcoin Core. Dopo l'installazione, apparirà un prompt `Needs Config`, che richiede il completamento delle impostazioni prima che il servizio possa funzionare. Questo si verifica in genere dopo gli aggiornamenti o le nuove installazioni e richiede una revisione delle `impostazioni RPC`. Procedere con la configurazione predefinita e fare clic su "Salva".


![image](assets/en/13.webp)


Una volta completamente sincronizzato, il nodo può fungere da backend privato per portafogli come Sparrow, garantendo una maggiore privacy e la convalida delle transazioni. Tuttavia, per gli utenti che immagazzinano quantità significative, è fondamentale comprendere i compromessi di sicurezza di questa connessione diretta. Quando un wallet si connette direttamente al Bitcoin Core, può esporre dati sensibili, poiché il Bitcoin Core memorizza le chiavi pubbliche (xpub) e i saldi del wallet in modo non criptato sul computer host. Un sistema compromesso potrebbe consentire a un aggressore di scoprire le vostre partecipazioni e di prendervi di mira.


Per mitigare questo rischio e ottenere un modello di sicurezza più robusto, è possibile impostare un Electrum Server privato. Questo server agisce da intermediario, indicizzando la blockchain senza memorizzare alcuna informazione specifica del wallet. Collegando il wallet al proprio server Electrum invece che direttamente al Bitcoin Core, si impedisce al wallet di accedere ai dati sensibili del nodo.


![image](assets/en/14.webp)


## 🔟 Impostare gli elettori


electrs (Electrum Rust Server) è un indicizzatore veloce ed efficiente che si collega al vostro nodo Bitcoin Core e consente ai portafogli compatibili con Electrum di interrogare la cronologia delle transazioni e i saldi in tempo reale. Eseguendo electrs su StartOS, si elimina la dipendenza dai server Electrum di terze parti, migliorando in modo significativo la privacy e la sicurezza: le query wallet vengono inviate direttamente al proprio nodo self-hosted.


Per configurarlo, installare innanzitutto il servizio electrs dal Marketplace di StartOS. Il sistema richiede che Bitcoin Core sia completamente sincronizzato prima di procedere. Dopo l'installazione, confermare le impostazioni di `Needs Config` con i valori predefiniti raccomandati e electrs inizierà l'indicizzazione della blockchain, che può richiedere fino a un giorno a seconda dell'hardware.


![image](assets/en/15.webp)


Una volta completato, è possibile collegare portafogli come Sparrow o Specter. Una connessione riuscita permette al wallet di sincronizzarsi direttamente con il vostro nodo, fornendo un'esperienza sicura, privata e autogestita del Bitcoin.


## 1️⃣1️⃣ Connect Sparrow Wallet


Per collegare il `Sparrow Wallet` al nodo StartOS utilizzando l'implementazione electrs, assicurarsi innanzitutto che Bitcoin Core sia completamente sincronizzato e che electrs sia installato e funzionante. Aprire Sparrow Wallet sul dispositivo e navigare in `File` -> `Impostazioni` -> `Server`. Scegliere quindi `Privato Electrum Server`. Nel campo URL, inserire il `nome host Tor` e la `porta` di electrs, che si trovano in StartOS in `Services` -> `electrs` -> `Properties` (di solito terminano con `.onion:50001`).


![image](assets/en/16.webp)


Quindi, attivare Tor selezionando `Use Proxy`, impostando l'indirizzo del proxy su `127.0.0.1` e la porta su `9050`. Fare clic su `Test Connection` e attendere qualche istante. In caso di connessione riuscita, verrà visualizzato un messaggio di conferma del tipo `Connected to electrs`. Una volta verificata la connessione, chiudere le impostazioni e procedere alla creazione o al ripristino del wallet. Questa impostazione garantisce che il wallet interroghi il proprio nodo tramite electrs, garantendo la massima riservatezza e un funzionamento privo di fiducia.


![image](assets/en/17.webp)


## 🎯 Conclusione


StartOS di Start9 è una piattaforma facile da usare e incentrata sulla privacy, progettata per ospitare autonomamente servizi essenziali come nodi Bitcoin e Lightning, portafogli e applicazioni personali. Elimina la necessità di competenze a riga di comando offrendo un'interfaccia grafica pulita, backup automatici, monitoraggio della salute e accesso sicuro a Tor, rendendola ideale per gli utenti non tecnici. La sua architettura modulare supporta la perfetta integrazione con strumenti come electrs o Sparrow, offrendo il pieno controllo della propria sovranità finanziaria e digitale. Con una forte attenzione alla trasparenza, al controllo locale e all'estensibilità, StartOS consente agli utenti di rivendicare la proprietà delle piattaforme centralizzate e di gestire la propria infrastruttura privata e resiliente.
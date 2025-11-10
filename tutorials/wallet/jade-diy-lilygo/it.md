---
name: Giada fai da te
description: Trasformate una scheda di sviluppo da 15 dollari in un hardware Bitcoin completamente funzionante wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Costruzione per principianti


**Target:** Costruttori curiosi con poca o nessuna esperienza nel settore embedded.


**Durata:** 2 ore (flessibile)


**Risultati: ** Alla fine, gli studenti sapranno:



- Riconoscere il modello di sicurezza dei portafogli hardware fai da te rispetto ai dispositivi commerciali.
- Assemblare un dispositivo di firma basato su microcontrollore.
- Flashare il firmware open-source e verificare il checksum della build.
- Firmare e trasmettere una transazione mainnet utilizzando il nuovo dispositivo.


---

## Astratto


Questo workshop di 2 ore insegna ai principianti a costruire un hardware Bitcoin funzionale wallet flashando il firmware open-source Jade su una scheda LilyGO T-Display da 15 dollari. Gli studenti trasformano un generico hardware di sviluppo in un dispositivo di firma paragonabile ai portafogli commerciali che costano 150 dollari, imparando i fondamenti della sicurezza attraverso l'esperienza pratica piuttosto che la sola teoria.


### Filosofia


Costruire il proprio dispositivo di firma non significa solo risparmiare, ma anche capire la tecnologia che protegge il proprio Bitcoin. Questo workshop privilegia la "sicurezza attraverso la comprensione" rispetto alla fiducia nella scatola nera. Procurandosi i componenti, flashando il firmware open-source e generando entropia da soli, gli studenti riducono il rischio della catena di fornitura e imparano a valutare criticamente le richieste di sicurezza. L'obiettivo è l'autonomia informata: gli studenti devono comprendere sia la potenza che i limiti del loro dispositivo fai-da-te rispetto alle alternative commerciali rinforzate.


---

## Primer concettuale (15 min)


### Che cos'è l'autocustodia e perché è importante?


Il Bitcoin è stato creato per eliminare dal nostro sistema monetario la necessità di terze parti fidate, come banche e aziende. Invece di usare la fiducia, il bitcoin usa la matematica, la fisica e la crittografia per consentire a chiunque di possedere e controllare il proprio denaro senza bisogno del permesso di nessuno.


Il modo in cui funziona è che il bitcoin esiste su un libro mastro digitale globale chiamato blockchain, alias bitcoin timechain, che è un libro mastro pubblico e trasparente gestito da computer, invece di un libro mastro centralizzato come un conto bancario.


La cosa importante da capire è che per spostare bitcoin da un luogo a un altro, è necessario firmare la transazione con la cosiddetta chiave privata. Pensate a come sbloccare un caveau con una password e spostare il bitcoin nel caveau di qualcun altro. Il Bitcoin vi dà il potere di possedere le chiavi di quel caveau, invece di affidarvi a una banca per spostare il vostro denaro.


Da un grande potere derivano grandi responsabilità: se si perdono le chiavi, i fondi sono perduti per sempre. In questo modo, si può pensare alle chiavi del caveau come al denaro stesso. Anche se le chiavi non sono la stessa cosa del bitcoin, sono il meccanismo per spostare i vostri fondi e sono quindi estremamente importanti da proteggere. Ecco perché diciamo "non le vostre chiavi, non le vostre monete".


Il termine "autodeposito" può sembrare confuso, ma significa solo che si possiedono le proprie chiavi private e si controlla il proprio bitcoin. Se non siete voi a detenere la chiave, vi affidate a qualcun altro che la detenga per voi. Se il vostro bitcoin è in un ETF o in una borsa (Mt. Gox, FTX, Coinbase, Binance, ecc.), non possedete il bitcoin, ma un diritto sul bitcoin. Questo comporta rischi di ogni tipo, come l'hackeraggio degli exchange e la perdita dei bitcoin, oppure il fatto che le società prestino i vostri soldi e ve ne diano solo una parte come riserva. Inoltre, terze parti fidate avrebbero il pieno controllo del vostro denaro e potrebbero limitare o bloccare i prelievi.


![image](assets/fr/01.webp)


Con l'autodeposito si elimina la fiducia dall'equazione. Nessuno può bloccare i vostri fondi o negare una transazione, potete inviare denaro oltre confine, a chiunque, in qualsiasi momento, e non avete bisogno di un conto bancario, di un documento d'identità o dell'approvazione di nessuno. Nessuno può fermarvi, censurarvi o derubarvi, sbloccando la piena potenza del bitcoin come moneta della libertà. Ecco perché diciamo che con il bitcoin potete essere la vostra banca.


Il Bitcoin è stato creato per risolvere il problema della manipolazione della fiducia e del denaro, un'uscita dal nostro sistema attuale, ma l'uscita funziona solo se si prendono le chiavi. Ecco perché l'autocustodia è così importante.


### Che cos'è un Wallet?


Il termine wallet è un po' un termine improprio e quindi può creare confusione. È vero che un wallet bitcoin, come un wallet fisico, immagazzina valore. Ma la differenza principale è che i portafogli di bitcoin non conservano effettivamente alcun bitcoin.


Il Bitcoin esiste solo come voce del libro mastro sulla blockchain pubblica, o all'interno del metaforico caveau nel cyberspazio. Ricordate che per spostare i bitcoin dovete usare le vostre chiavi per sbloccare il caveau e spostare le monete da qualche altra parte; le chiavi private sono quelle utilizzate per spendere i bitcoin. Quando si effettua una transazione con il proprio wallet, in realtà si utilizzano solo le proprie chiavi per firmare la transazione. In questo modo si dimostra di possedere il denaro e di avere il diritto di spendere le monete.


I portafogli Bitcoin in realtà memorizzano solo le chiavi private, quindi sarebbe più corretto chiamarli portachiavi.


### Portafogli Hot vs Cold


Un hot wallet è un'applicazione software sul telefono o sul computer. È collegato a Internet, quindi è più facile da usare e più veloce nel firmare le transazioni, ma questo significa anche che è più esposto agli hacker, al malware e al phishing. Si chiama "caldo" perché è connesso a Internet, è collegato e acceso. Un esempio potrebbe essere un telefono wallet o un browser wallet.


D'altra parte, un wallet freddo, o hardware wallet, è un dispositivo che crea e memorizza la chiave offline. In questo modo si elimina la possibilità di hackerare i fondi ed è molto più sicuro per i risparmi a lungo termine, ma è un dispositivo che deve essere firmato per ogni transazione e può essere meno conveniente.


### Modello di minaccia Hardware Wallet


I portafogli hardware esistono per risolvere un problema fondamentale: come firmare le transazioni Bitcoin senza esporre le proprie chiavi private a un computer connesso a Internet che potrebbe essere compromesso da malware o da aggressori remoti? Il modello di minaccia principale presuppone che il laptop o il telefono di tutti i giorni siano potenzialmente ostili. Un wallet hardware crea un ambiente isolato in cui le chiavi private non lasciano mai il dispositivo e la firma delle transazioni avviene in un secure element o in un microcontrollore che comunica solo la firma al computer host, non la chiave stessa. Anche se il computer è completamente compromesso, un aggressore non può rubare il Bitcoin senza accedere fisicamente al dispositivo e al PIN.


Tuttavia, i portafogli hardware presentano delle minacce proprie. Bisogna fidarsi che il produttore non abbia introdotto backdoor, che la catena di fornitura non sia stata manomessa e che la generazione di numeri casuali sia veramente casuale. Gli aggressori fisici potrebbero estrarre le chiavi attraverso attacchi side-channel o manipolazione del chip, e qualcuno con accesso temporaneo potrebbe modificare il dispositivo. Costruire il proprio hardware wallet aiuta a capire questi compromessi: si decideranno gli elementi sicuri rispetto ai microcontrollori generici, come verificare le transazioni su un display e come proteggersi dalle minacce fisiche e remote. L'obiettivo non è la sicurezza perfetta, ma capire da quali minacce ci si sta proteggendo e quali rimangono.


### Concetti chiave



- Entropia e frasi seed:** Il vostro wallet è sicuro quanto la casualità che lo genera. Mescoleremo il generatore di numeri casuali del dispositivo con trucchi di facile utilizzo per l'uomo, come i lanci di dadi, convertiremo l'entropia in una [frase BIP39] di 12 o 24 parole (https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) e lasceremo la stanza con un backup scritto o in metallo di cui vi fidate.
- Igiene delle frasi dei semi:** Trattate i seed come le chiavi principali dei vostri risparmi. Non digitate mai le parole su un telefono o un computer: i keylogger, gli screenshot e i backup su cloud possono farle trapelare per sempre. Conservate la frase offline, memorizzatela in un luogo accessibile solo a voi e fate pratica nel rileggerla ad alta voce prima di partire.
- Elemento sicuro + microcontrollore:** Considerate il secure element come la cassaforte e il microcontrollore come il cervello. Il secure element custodisce le chiavi private con resistenza alle manomissioni, mentre il microcontrollore gestisce lo schermo, i pulsanti e la logica del firmware. Si noti che i portafogli hardware che stiamo costruendo oggi non dispongono di un secure element. Questo non significa che sia un problema di sicurezza. Questo non significa che sia insicuro, ma solo che ha un livello di protezione in meno.
- Fiducia nel firmware:** Il firmware è il sistema operativo invisibile del wallet. Scaricare sempre da release etichettate, controllare l'hash pubblicato e comprendere che le build riproducibili consentono a più persone di compilare lo stesso codice e di ottenere lo stesso identico binario. Se il checksum non corrisponde, non si firma.


---

## Cosa stiamo costruendo?


Stiamo prendendo un hardware generico, il LilyGo T-Display, e ci stiamo flashando sopra il firmware Jade SDK. Il [Jade Plus](https://blockstream.com/jade/jade-plus/) è un wallet open-source, che di solito costa 150 dollari:


![image](assets/fr/02.webp)


Oggi, invece, flasheremo il loro firmware su un hardware da 15 dollari.


### Cosa comprare


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB con guscio, modello K164)** - [Ordinare direttamente da LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) per circa 15 dollari. Questa scheda ESP32 fornisce il display, i pulsanti e l'interfaccia USB che rispecchiano il Jade Plus di Blockstream. L'ESP32 include anche le radio Wi-Fi e Bluetooth; verrà fornito un firmware che le mantiene disattivate, ma esse costituiscono un modello di minaccia perché un codice maligno potrebbe riattivarle.
- Cavo USB-C** - Portate con voi un cavo compatibile con i dati, in modo da poter flashare il firmware e alimentare la scheda direttamente dal vostro laptop (va benissimo per l'uso in classe).


### Perché costruire il proprio Hardware Wallet?



- Risparmiate circa 135 dollari rispetto all'acquisto di un dispositivo commerciale.
- Costruire il comfort con il flashing del firmware, gli elementi sicuri e l'igiene wallet.
- Attivate altri dispositivi di firma per distribuire i risparmi su più portafogli.
- Riducete i rischi della catena di fornitura acquistando e assemblando voi stessi ogni componente.
- Tenete a mente il mantra di Lopp: sovranità e convenienza sono sempre in contrasto.


## Set up fisico


### Preparare il caso


Per alloggiare la scheda LilyGO T-Display sono disponibili due opzioni: una custodia stampata in 3D o la custodia ufficiale LilyGO. La custodia stampata può essere trovata e stampata da [questo modello](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Offre un involucro leggero e personalizzabile per il dispositivo.


![image](assets/fr/04.webp)


In alternativa, è possibile utilizzare la custodia ufficiale LilyGO, che offre una vestibilità e una finitura leggermente diverse, offrendo una protezione più robusta e un look raffinato.


![image](assets/fr/05.webp)


Si noti che le custodie stampate e ufficiali differiscono leggermente nel design e nell'assemblaggio. Qualunque sia l'opzione scelta, assicurarsi che la scheda sia correttamente inserita nella custodia per evitare connessioni allentate o danni.


### Ispezione della scheda


Prima di procedere, ispezionare attentamente la scheda LilyGO T-Display per verificare che non vi siano difetti o residui visibili. Verificare che il display, i pulsanti e la porta USB-C siano puliti e privi di polvere o schizzi di saldatura. Maneggiare la scheda con cura e rispettare la sicurezza contro le scariche elettrostatiche (ESD) collegandosi a terra o utilizzando un braccialetto ESD per evitare di danneggiare i componenti sensibili.


### Collegamento al computer portatile


Utilizzando un cavo USB-C compatibile con i dati, collegare la scheda LilyGO al computer portatile. Questa connessione fornirà l'alimentazione e consentirà di eseguire il flash del firmware.


All'avvio, viene visualizzata la seguente schermata:


![image](assets/fr/06.webp)



All'accensione, LilyGO visualizza una schermata di prova a colori che passa attraverso i colori solidi. Questo conferma che il display e la scheda funzionano correttamente prima di flashare il firmware.


Una volta completato il test del colore, lo schermo si posiziona su uno stato predefinito, indicando che la scheda è pronta per le fasi successive del processo di costruzione.


![image](assets/fr/07.webp)


## La via facile o la via Hard


Esistono due approcci principali per il flashing del firmware dell'hardware wallet: il modo semplice e il modo difficile. Il metodo semplice utilizza strumenti preconfigurati o flasher basati sul Web che caricano automaticamente il firmware sul dispositivo con un input minimo. Questo metodo è ideale per i principianti che desiderano una vittoria rapida o preferiscono evitare le complessità del debug e delle interazioni da riga di comando. Semplifica il processo e consente di essere operativi più rapidamente, rendendolo accessibile anche a chi è nuovo allo sviluppo embedded o ai portafogli hardware.


La via più difficile, invece, prevede l'utilizzo manuale di strumenti a riga di comando per il flashing del firmware. Questo approccio richiede la verifica delle firme e delle checksum del firmware per garantirne l'autenticità e l'integrità, consentendo una comprensione più approfondita del processo di flashing e del modo in cui il firmware interagisce con l'hardware. Sebbene richieda un maggiore impegno e una maggiore familiarità con i comandi da terminale, offre un maggiore controllo, trasparenza e fiducia nella sicurezza del dispositivo.


Ogni metodo ha dei compromessi: il metodo facile sacrifica un certo grado di fiducia e comprensione per la velocità e la convenienza, mentre il metodo difficile richiede più tempo e competenze tecniche, ma ricompensa con la flessibilità e una maggiore comprensione della tecnologia sottostante. Gli istruttori dovrebbero incoraggiare gli studenti a scegliere il percorso che meglio si adatta al loro livello di comfort e alla loro curiosità, promuovendo sia la fiducia che l'esplorazione.


## Il modo più semplice


Il modo più semplice per flashare un ESP32



- Vai al Github ufficiale di Blockstream: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- È possibile scaricare il file sorgente ed eseguire il sito web in locale, ma GitHub lo ospita già su [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub fornisce l'HTML, il CSS, il JavaScript e così via direttamente al browser, in modo da poter eseguire il flash del dispositivo senza installare strumenti per gli sviluppatori.


![image](assets/fr/09.webp)



- Aprite il menu a tendina (probabilmente è impostato su `M5Stack Core2`) e selezionate la vostra scheda di sviluppo: per questa classe, scegliete `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Quando si fa clic su flash, appare questo. Per sapere quale dispositivo è il LILYGO, scollegare il lilygo e ricollegarlo. La porta COM del lilygo apparirà e scomparirà. Fare clic sulla porta COM a cui è collegato il Jade


![image](assets/fr/11.webp)



- A questo punto dovrebbe apparire una barra di avanzamento e, una volta terminato, si è pronti a configurare il sistema


## Impostazione del Jade Wallet


Una volta che il firmware è stato flashato con successo, il display LilyGO T è ora un wallet hardware Jade completamente funzionale. Questa sezione vi guiderà attraverso il processo di configurazione iniziale, dalla generazione della frase seed alla connessione del dispositivo con il software wallet come il Sparrow o l'applicazione mobile Blockstream Green.


### Avvio iniziale e configurazione del dispositivo



- Accendere il dispositivo:** Con LilyGO ancora collegato al laptop tramite USB-C, il firmware Jade dovrebbe avviarsi automaticamente. Sul display apparirà il logo Jade.



- Entrare in modalità di configurazione:** Il dispositivo presenterà un menu iniziale. Per navigare, utilizzare i due pulsanti fisici della scheda:
 - Pulsante sinistro: ** Sposta su/indietro
 - Tasto destro:** Spostamento in basso/avanti
 - Entrambi i pulsanti contemporaneamente:** Seleziona/conferma



- Selezionare "Setup":** Navigare fino all'opzione Setup e premere entrambi i pulsanti per confermare. Il dispositivo vi guiderà attraverso il processo di configurazione iniziale.


### Creazione del Wallet



- Scegliere "Begin Setup":** Il dispositivo chiederà di iniziare il processo di creazione del wallet. Confermare la selezione.



- Selezionare "Crea nuovo Wallet":** Verranno presentate due opzioni:
 - Crea un nuovo Wallet:** Genera una nuova frase seed (scegliere questa per il workshop)
 - Ripristinare Wallet:** Recuperare un wallet esistente da una frase seed (per utenti avanzati)



- Selezionare "Crea nuovo Wallet" e confermare.



- Generazione di entropia:** Il dispositivo utilizza il suo generatore di numeri casuali per creare entropia crittografica. Questo processo richiede alcuni secondi perché il dispositivo raccoglie la casualità da più fonti.


### Registrazione della frase-seme



- Scrivere la frase seed:** Il dispositivo visualizzerà ora una frase BIP39 seed di 12 parole, una parola alla volta. Questa è la fase più critica dell'intero processo.


**Pratiche di sicurezza importanti


- Scrivete ogni parola in modo chiaro su carta (utilizzate le schede di frasi seed in dotazione, se disponibili)
- Ricontrollate ogni parola mentre la scrivete
- Non fotografate mai la frase seed con il vostro telefono
- Non digitate mai le parole in nessun computer o telefono
- Mantenete la vostra frase seed privata, non condividete lo schermo e non mostratela ad altri



- Verifica della frase seed:** Dopo aver scritto tutte le 12 parole, il dispositivo chiederà di confermare alcune parole della frase per assicurarsi che siano state registrate correttamente. Utilizzare i pulsanti per selezionare la parola corretta per ogni richiesta.


**Prima di procedere, esercitatevi a rileggere la vostra frase seed ad alta voce (a bassa voce, in modo che gli altri non sentano). Questo aiuta a individuare eventuali errori di scrittura o ambiguità.


### Metodo di connessione



- Scegliere il tipo di connessione:** Il firmware Jade supporta due metodi di connessione:
 - USB:** Connessione cablata tramite cavo USB-C (consigliato per questo workshop)
 - Bluetooth:** Connessione wireless ai dispositivi mobili



- Selezionare **USB** per il momento, in quanto è l'opzione più semplice per il software desktop wallet e non introduce vettori di attacco wireless.



- Denominazione del dispositivo:** Il dispositivo Jade visualizzerà un identificatore unico come "Connect Jade A7D924". Questo identificatore aiuta a distinguere tra più portafogli hardware se si finisce per costruirne più di uno. Se lo si desidera, prendere nota di questo identificatore.


### Collegamento al software Wallet


Ora avete due opzioni principali per interfacciarvi con l'hardware wallet appena creato: l'applicazione mobile Blockstream Green (per l'uso in movimento) o Sparrow Wallet (per l'uso desktop con funzioni più avanzate). In questo workshop ci concentreremo sul Sparrow Wallet, in quanto offre una migliore visibilità sui dettagli tecnici delle transazioni Bitcoin.


#### Opzione 1: App mobile Blockstream Green (avvio rapido)


Se volete testare rapidamente il vostro dispositivo con un dispositivo mobile:



- Scaricare l'applicazione **Blockstream Green** dall'App Store (iOS) o da Google Play (Android)
- Aprire l'applicazione e selezionare "Connetti Hardware Wallet"
- Scegliere "Jade" dall'elenco dei dispositivi supportati
- Collegate il vostro Jade al telefono utilizzando un cavo da USB-C a USB-C (o un adattatore da USB-C a Lightning per iPhone 15+)
- Seguire le indicazioni sullo schermo per connettersi e creare il primo wallet


**Nota su Liquid:** L'applicazione Blockstream Green supporta sia Bitcoin che Liquid (una catena laterale Bitcoin). Se si utilizzano le funzioni del Liquid, è possibile che venga richiesto di "Esportare la chiave master blinding": ciò consente all'applicazione di vedere gli importi delle transazioni sulla rete Liquid, che sono altrimenti riservati. Per questo workshop, è possibile ignorare le funzioni Liquid e concentrarsi sulle transazioni Bitcoin standard.


#### Opzione 2: Sparrow Wallet (consigliato per l'officina)


Sparrow Wallet è una potente applicazione desktop che offre un controllo granulare sulle transazioni Bitcoin e si connette perfettamente con l'hardware Jade wallet.


**Installazione:**



- Scaricare Sparrow Wallet dal sito ufficiale: [sparrowwallet.com](https://sparrowwallet.com)
- Verificare la firma del download (per maggiori dettagli, consultare la documentazione di Sparrow)
- Installare e lanciare l'applicazione


**Collegare la vostra Giada a Sparrow:**



- In Sparrow, andare su **File → Nuovo Wallet**
- Assegnate un nome al vostro wallet (ad esempio, "Il mio Jade Wallet")
- Fare clic su **Connesso Hardware Wallet**
- Il Sparrow dovrebbe rilevare automaticamente il dispositivo Jade inserito
- Se richiesto, confermare la connessione sul display di Jade premendo entrambi i tasti
- Selezionare il tipo di script desiderato:
 - Native Segwit (P2WPKH):** Raccomandato per i principianti: tariffe più basse, massima compatibilità con i portafogli moderni
 - Segwit annidato (P2SH-P2WPKH):** Per la compatibilità con i servizi più vecchi
 - Taproot (P2TR):** Più avanzato, offre la migliore privacy e le tariffe più basse, ma richiede un supporto wallet all'avanguardia
- Fare clic su **Import Keystore** per completare la connessione


**Configurazione della connessione al server del Sparrow:**


Prima di poter vedere il proprio saldo o trasmettere le transazioni, il Sparrow deve connettersi a un nodo Bitcoin per recuperare i dati della blockchain. Sono disponibili diverse opzioni, ognuna con diversi compromessi tra convenienza, privacy e fiducia:



- Electrum Server pubblico (più facile, meno privato):** Si collega a un server pubblico gestito da terzi. È veloce da configurare, ma il server può vedere gli indirizzi del wallet e potenzialmente collegarli al vostro indirizzo IP. Ottimo per i test su testnet.
 - In Sparrow, andare su **Strumenti → Preferenze → Server**
 - Selezionare **Server pubblico** e scegliere un server dall'elenco
 - Fare clic su **Test Connection** per verificare



- Nodo Bitcoin Core o Knots (più privato, più funzionante):** Gestisci il tuo nodo Bitcoin completo. Questo è il gold standard per la privacy e la verifica, poiché convalidate ogni transazione da soli e non vi fidate del server di nessun altro. Tuttavia, richiede il download dell'intera blockchain (~600GB) e la sincronizzazione del nodo.
 - Installare e sincronizzare il nucleo o i nodi Bitcoin
 - In Sparrow, andare su **Strumenti → Preferenze → Server**
 - Selezionare **Bitcoin Core o Knots** e inserire i dettagli di connessione del nodo



- Electrum Server privato (buon equilibrio):** Ospita il tuo server Electrum (come Fulcrum o Electrs) collegato al tuo nodo Bitcoin Core o Knots. Offre la massima privacy senza dover eseguire Sparrow sulla stessa macchina del nodo.
 - Configurare un server Electrum che punta al nodo Bitcoin Core o Knots
 - Nel Sparrow, andare a **Strumenti → Preferenze → Server**
 - Selezionare **Privato Electrum** e immettere l'URL del proprio server


Per questo workshop, l'utilizzo di un **Public Electrum Server** va benissimo per le transazioni di testnet. In un ambiente di produzione con fondi reali, si dovrebbe prendere in considerazione la possibilità di gestire un proprio nodo o di utilizzare un server privato fidato per ottenere la massima privacy.


#### Opzione 3: App desktop Blockstream Green (avvio rapido)


Blockstream Green è il software per terminare l'impostazione di JadeDIY e deve essere presente nella versione desktop



- Procuratevi l'applicazione ufficiale di Blockstream - questo è il link dal loro sito web. Una volta arrivati, fate clic su [Download now] (https://blockstream.com/app/).


![image](assets/fr/12.webp)



- A seconda della posizione dei download, molto probabilmente il file si trova nella cartella Download. Controllare e fare doppio clic sul file eseguibile per installare il software.


![image](assets/fr/13.webp)



- Potrebbe essere necessario concedere i diritti di amministratore per eseguire il programma di installazione. Una volta fatto, si aprirà una finestra che dovrebbe assomigliare alla seguente immagine: fare clic su **Avanti**.


![image](assets/fr/14.webp)



- Scegliete dove volete che risieda l'applicazione installata (una posizione con gli altri programmi o un luogo facile da trovare), quindi fate clic su **Avanti**.


![image](assets/fr/15.webp)



- Il programma di installazione chiederà un nome per il collegamento. Inseritene uno o mantenete quello predefinito, quindi fate clic su **Avanti**.


![image](assets/fr/16.webp)



- Se si desidera un collegamento al desktop, selezionare la casella; altrimenti fare clic su **Avanti**.


![image](assets/fr/17.webp)



- Infine, fare clic su **Install** e attendere qualche minuto per il completamento dell'installazione.


![image](assets/fr/18.webp)



- La barra di avanzamento dovrebbe riempirsi fino alla fine.


![image](assets/fr/19.webp)



- Al termine, apparirà una nuova pagina: fare clic su **Finish**.


![image](assets/fr/20.webp)



- Individuare l'applicazione Blockstream appena installata (esempio mostrato nel menu Start di Windows 11).


![image](assets/fr/21.webp)



- Una volta trovato, fate clic per avviarlo: dovrebbe apparire una schermata iniziale.


### Verifica della configurazione


Una volta collegati al Sparrow (o a un'altra applicazione wallet):



- Controllare gli indirizzi:** Il Sparrow visualizza gli indirizzi di ricezione derivati dalla frase del seed. È possibile verificare un indirizzo sul dispositivo Jade accedendo alla scheda "Ricezione" del Sparrow e facendo clic su "Visualizza Address": l'indirizzo dovrebbe apparire sia sullo schermo del computer che sul display di Jade.



- Generare un indirizzo di ricezione:** fare clic sulla scheda **Ricezione** in Sparrow e copiare il primo indirizzo di ricezione Bitcoin.



- Pronti per le transazioni:** Il vostro hardware wallet è ora completamente configurato e pronto a ricevere e firmare le transazioni Bitcoin. Passare alla sezione successiva per esercitarsi a firmare una transazione testnet.



---

### Lista di controllo per la configurazione rapida



- Il firmware Jade si avvia con successo
- Nuovo wallet creato con una frase di 12 parole del seed
- Frase del seme scritta in modo chiaro e verificata
- Modalità di connessione USB selezionata
- Software Wallet (Sparrow) installato e collegato
- Connessione al server configurata (Electrum pubblico per mainnet)
- Primo indirizzo di ricezione generato e verificato sul dispositivo



---

**Licenza MIT**


**Copyright (c) 2025 La Rete Bitcoin NYC**


Con la presente si concede il permesso, a titolo gratuito, a chiunque ottenga una copia di questo software e dei file di documentazione associati (il "Software"), di trattare il Software senza alcuna restrizione, compresi, senza limitazione, i diritti di utilizzare, copiare, modificare, unire, pubblicare, distribuire, concedere in sublicenza e/o vendere copie del Software, e di permettere alle persone a cui il Software viene fornito di farlo, alle seguenti condizioni:


La suddetta nota di copyright e la presente nota di autorizzazione devono essere incluse in tutte le copie o parti sostanziali del Software.


IL SOFTWARE VIENE FORNITO "COSÌ COM'È", SENZA ALCUN TIPO DI GARANZIA, ESPLICITA O IMPLICITA, INCLUSE, A TITOLO ESEMPLIFICATIVO, LE GARANZIE DI COMMERCIABILITÀ, IDONEITÀ A UNO SCOPO PARTICOLARE E NON VIOLAZIONE. IN NESSUN CASO GLI AUTORI O I DETENTORI DEI DIRITTI D'AUTORE SARANNO RESPONSABILI PER QUALSIASI RECLAMO, DANNO O ALTRA RESPONSABILITÀ, SIA IN UN'AZIONE CONTRATTUALE, CHE IN UN'AZIONE ILLECITA O ALTRO, DERIVANTE DA, DA O IN RELAZIONE AL SOFTWARE O ALL'USO O AD ALTRI RAPPORTI CON IL SOFTWARE.


---
---
name: Attakaï

description: trasformazione di un S9 in un sistema di riscaldamento per la casa
---

![cover](assets/cover.png)

# Attakai - il mining domestico reso possibile e accessibile!

L'iniziativa "Attakaï" esplora il mining di Bitcoin utilizzando il calore generato. La guida propone soluzioni per rendere i minatori adatti all'uso come radiatori nelle abitazioni, offrendo così maggiore comfort ed efficienza energetica. Bitcoin regola automaticamente la difficoltà del mining e ricompensa i minatori per il loro lavoro. Tuttavia, la concentrazione dell'hashrate può rappresentare rischi per la neutralità della rete. "Attakaï" offre una guida pratica per il retrofitting dei minatori in modo economico, consentendo ai partecipanti di ridurre la bolletta elettrica e di essere ricompensati con sats senza KYC.

## Introduzione

"Attakaï", che significa "la temperatura ideale" in giapponese, è il nome dell'iniziativa che mira a scoprire il mining di bitcoin attraverso il riutilizzo del calore lanciato da @ajelexBTC e @BlobOnChain con Découvre Bitcoin. Questa guida per il retrofitting di un ASIC servirà come base per imparare di più sul mining, il suo funzionamento, la sua storia recente e l'economia sottostante.

### Perché riutilizzare il calore di un ASIC?

È importante comprendere la relazione tra energia e produzione di calore in un sistema elettrico.

Per un investimento di 1 kW di energia elettrica, un radiatore elettrico produce 1 kW di calore, né più né meno. I nuovi radiatori non sono più efficienti dei radiatori tradizionali. Il loro vantaggio risiede nella loro capacità di diffondere il calore in modo continuo e uniforme in una stanza, offrendo quindi maggiore comfort rispetto ai radiatori tradizionali che alternano tra una potenza di riscaldamento elevata e l'assenza di riscaldamento, generando così variazioni di temperatura regolari e disagio.

Un computer, o più in generale una scheda elettronica, non consuma energia per effettuare calcoli, ha semplicemente bisogno che l'energia circoli nei suoi componenti per funzionare. Il consumo di energia è dovuto alla resistenza elettrica dei componenti che produce perdite, generando così calore, questo è ciò che viene chiamato effetto Joule.
Alcune aziende hanno avuto l'idea di condividere le esigenze di potenza di calcolo e di riscaldamento attraverso radiatori/server. L'idea è quella di distribuire i server di un'azienda in piccole unità che potrebbero essere collocate in abitazioni o uffici. Tuttavia, questa idea incontra diversi problemi. Le esigenze dei server non sono legate alle esigenze di riscaldamento e le aziende non possono utilizzare in modo flessibile le capacità di calcolo dei loro server. Esistono anche limiti alla larghezza di banda che i privati possono possedere. Tutti questi vincoli impediscono all'azienda di rendere redditizie queste costose installazioni e di fornire un'offerta stabile di server online senza avere centri dati in grado di prendere il sopravvento quando non c'è bisogno di riscaldamento.

> "Il calore del tuo computer non viene sprecato se devi riscaldare la tua casa. Se usi un riscaldamento elettrico dove vivi, allora il calore del tuo computer non è uno spreco. Costa lo stesso se generi questo calore con il tuo computer. Se hai un altro sistema di riscaldamento più economico dell'elettrico, allora lo spreco è solo nella differenza di costo. Se è estate e usi l'aria condizionata, allora è il doppio.
> La creazione di bitcoin dovrebbe avvenire dove è meno costoso. Forse sarà dove il clima è freddo e dove il riscaldamento è elettrico, dove il mining diventerebbe gratuito."
> Satoshi Nakamoto - 8 agosto 2010

Il Bitcoin e la sua prova del lavoro si distinguono perché regolano automaticamente la difficoltà del mining in base alla quantità di calcolo effettuato dall'intera rete, questa quantità è chiamata hashrate ed è espressa in hash al secondo. Oggi si stima che sia di 280 Exahash al secondo, ovvero 280 miliardi di miliardi di hash al secondo. Questo hashrate rappresenta lavoro e quindi una quantità di energia spesa. Più alto è l'hashrate, maggiore è la difficoltà e viceversa. In questo modo, è possibile attivare o disattivare un minatore Bitcoin in qualsiasi momento senza conseguenze per la rete, a differenza dei radiatori/server che dovrebbero rimanere stabili per offrire il loro servizio. Il minatore viene ricompensato per il lavoro svolto in relazione al lavoro degli altri, per quanto piccola possa essere questa partecipazione.

In sintesi, un radiatore elettrico e un minatore Bitcoin producono entrambi 1 kW di calore per 1 kW di elettricità consumata. Tuttavia, il minatore riceve anche bitcoin come ricompensa. Indipendentemente dal prezzo dell'elettricità, dal prezzo del bitcoin o dalla concorrenza dell'attività di mining sulla rete Bitcoin, è economicamente più vantaggioso riscaldarsi con un minatore piuttosto che con un radiatore elettrico.

![Video presentazione](https://youtu.be/gKoh44UCSnE)

### Il valore aggiunto per Bitcoin

Non entreremo nei dettagli di come funziona il mining (le risorse sono disponibili in accademia se ne avete bisogno). Ciò che è importante capire è il modo in cui il mining contribuisce alla decentralizzazione di Bitcoin: una serie di tecnologie esistenti sono state ingegnosamente combinate per dare vita al consenso di Nakamoto. Questo consenso permette ai giocatori onesti di essere ricompensati economicamente per la loro partecipazione al funzionamento della rete Bitcoin, scoraggiando invece i giocatori disonesti. Questo è uno dei punti chiave che permette alla rete di esistere a lungo termine.

I giocatori onesti, quelli che effettuano il mining secondo le regole, sono in competizione tra loro per ottenere la quota maggiore possibile della ricompensa per la produzione di nuovi blocchi. Questo incentivo economico porta naturalmente a una forma di centralizzazione, in quanto le aziende scelgono di specializzarsi in questa attività lucrativa riducendo i costi grazie alle economie di scala. Questi attori industriali si trovano in una posizione vantaggiosa per quanto riguarda l'acquisto e la manutenzione dei macchinari, nonché per la negoziazione delle tariffe elettriche all'ingrosso.

> Inizialmente, la maggior parte degli utenti avrebbe gestito i nodi della rete, ma man mano che la rete sarebbe cresciuta oltre un certo punto, sarebbe stata affidata sempre più agli specialisti con server farm di hardware specializzato. Una server farm avrebbe bisogno di un solo nodo sulla rete e il resto della LAN si connetterebbe a quel nodo". - Satoshi Nakamoto - 2 novembre 2008

Alcune entità detengono una percentuale considerevole dell'hashrate totale in grandi parchi minerari. Si può notare la recente ondata di freddo negli Stati Uniti, dove una parte significativa dell'hashrate è stata messa offline per consentire di reindirizzare l'energia alle case che avevano un bisogno eccezionale di elettricità. Per diversi giorni, i minatori hanno avuto un incentivo economico a spegnere le loro farm e questo tempo eccezionale è visibile sulla curva dell'hashrate di Bitcoin.

Questo problema potrebbe diventare problematico e rappresentare un rischio significativo per la neutralità della rete. Un operatore con più del 51% dell'hashrate potrebbe più facilmente censurare le transazioni se lo desiderasse. Per questo motivo è importante distribuire l'hashrate tra più soggetti piuttosto che in entità centralizzate che potrebbero essere più facilmente sequestrate da un governo, ad esempio.

**Se i minatori sono distribuiti in migliaia o addirittura milioni di case in tutto il mondo, diventa molto complicato per uno Stato prenderne il controllo.**

\*\*Alla sua uscita dalla fabbrica, un minatore non è adatto per essere utilizzato come radiatore in una casa, a causa di due problemi principali: un rumore eccessivo e l'assenza di regolazione. Tuttavia, questi problemi possono essere facilmente risolti attraverso semplici modifiche hardware e software, consentendo di ottenere un minatore molto più silenzioso e che può essere programmato e automatizzato come i moderni riscaldamenti elettrici.

**Attakaï è un'iniziativa educativa che ti insegna come effettuare un retrofitting dell'Antminer S9 nel modo più economico possibile.**

È un'ottima opportunità per imparare facendo pratica. Oltre a ridurre la tua bolletta elettrica, sarai ricompensato per la tua partecipazione con sats KYC gratuiti.

## Capitolo 1: Guida all'acquisto di un ASIC usato

In questa sezione vedremo le buone pratiche per acquistare un Bitmain Antminer S9 usato, la macchina su cui si basa questo tutorial di retrofitting come radiatore. Questa guida funziona anche per altri modelli di ASIC in quanto si tratta di una guida all'acquisto generale per hardware di mining usato.

L'Antminer S9 è un dispositivo offerto da Bitmain dal maggio 2016. Consuma 1323W di elettricità e produce 13,5 TH/s. Nonostante sia considerato vecchio, rimane un'ottima opzione per iniziare il mining. Dato che è stato prodotto in grande quantità, è facile trovare pezzi di ricambio in abbondanza in molte regioni del mondo. Di solito è possibile acquistarlo direttamente da privati su siti come Ebay o LeBonCoin, poiché i rivenditori rivolti ai professionisti non lo offrono più a causa della sua minore competitività rispetto a macchine più recenti. È meno efficiente rispetto ad ASIC come l'Antminer S19, offerto dal marzo 2020, ma questo lo rende un hardware usato conveniente e più adatto alle modifiche che effettueremo.

L'Antminer S9 è disponibile in diverse varianti (i, j) che apportano modifiche minori all'hardware di prima generazione. Non riteniamo che questo elemento debba influenzare la tua decisione di acquisto e questa guida funzionerà per tutte queste varianti.

Il prezzo degli ASIC varia in base a molti fattori come il prezzo del bitcoin, la difficoltà della rete, l'efficienza della macchina e il costo dell'elettricità. È quindi difficile dare una stima precisa per l'acquisto di una macchina usata. A febbraio 2023, il prezzo atteso in Francia si aggira generalmente tra 100€ e 200€, ma questi prezzi possono cambiare molto rapidamente.

![image](assets/guide-achat/1.webp)

L'Antminer S9 è composto dalle seguenti parti:

- 3 schede hash dove si trovano i chip che producono l'hashing

![image](assets/guide-achat/2.webp)'

- Una scheda di controllo che include uno slot per una scheda SD, una porta Ethernet e connettori per le hashboard e i ventilatori. È il cervello del tuo ASIC.

![image](assets/guide-achat/3.webp)

- 3 cavi dati che collegano le hashboard alla scheda di controllo

![image](assets/guide-achat/4.webp)

- L'alimentatore che funziona a 220V e può quindi essere collegato come un elettrodomestico tradizionale

![image](assets/guide-achat/5.webp)

- 2 ventilatori da 120mm

![image](assets/guide-achat/6.webp)

- Un cavo maschio C13

![image](assets/guide-achat/7.webp)

Quando acquisti una macchina usata, è importante verificare che tutte le parti siano incluse e funzionanti. Durante lo scambio, dovresti chiedere al venditore di accendere la macchina per verificare il suo corretto funzionamento. È importante verificare che l'apparecchio si accenda correttamente, quindi verificare la connettività a Internet collegando un cavo Ethernet e accedendo all'interfaccia di connessione di Bitmain tramite un browser Internet sulla stessa rete locale. Puoi trovare questo indirizzo IP collegandoti all'interfaccia del tuo router Internet e cercando i dispositivi connessi. Questo indirizzo dovrebbe avere il seguente formato: 192.168.x.x

![image](assets/guide-achat/8.webp)

Verifica anche che le credenziali predefinite funzionino (nome utente: root, password: root). Se le credenziali predefinite non funzionano, sarà necessario eseguire un reset della macchina.

![image](assets/guide-achat/9.webp)

Una volta connesso, dovresti essere in grado di vedere lo stato di ogni hashboard sulla dashboard. Se il minatore è collegato a un pool, dovresti vedere tutte le hashboard funzionare. È importante notare che i minatori fanno molto rumore, è normale. Assicurati anche che i ventilatori funzionino correttamente.

Successivamente, puoi rimuovere il pool di mining del vecchio proprietario per configurare il tuo in seguito. Se lo desideri, puoi anche ispezionare le hashboard smontando la macchina. Tuttavia, questa operazione è più complessa e richiede più tempo e alcuni strumenti. Se desideri procedere con lo smontaggio, puoi fare riferimento alla parte successiva di questo tutorial che spiega come farlo. È importante notare che i minatori accumulano molta polvere e richiedono una manutenzione regolare. È questa accumulazione di polvere e la qualità della manutenzione che potrai osservare smontando la macchina.
Dopo aver esaminato tutti questi punti, puoi acquistare la tua macchina con il massimo grado di fiducia. In caso di dubbi, rivolgiti alla comunità e se hai bisogno di attrezzature per completare questo tutorial, non esitare a inviarci un messaggio.

Per sintetizzare questa guida in una frase: **"Non fidarti, verifica"**.

## Capitolo 2: Guida all'acquisto di componenti per modifiche

![image](assets/piece/1.webp)

### Come trasformare il tuo Antminer S9 in un riscaldamento silenzioso e connesso?

Se sei proprietario di un Antminer S9, probabilmente sai quanto questo dispositivo possa essere rumoroso e ingombrante. Tuttavia, è possibile trasformarlo in un riscaldamento silenzioso e connesso seguendo alcuni semplici passaggi. In questo articolo ti presenteremo gli strumenti necessari per effettuare le modifiche, mentre un articolo successivo spiegherà nel dettaglio i passaggi da seguire per apportare tali cambiamenti.

### 1. Sostituire le ventole

Le ventole originali dell'Antminer S9 sono troppo rumorose per utilizzare il tuo Antminer come riscaldamento. La soluzione è sostituirle con ventole più silenziose. Il nostro team ha testato diversi modelli del marchio Noctua e ha selezionato il Noctua NF-A14 iPPC-2000 PWM come miglior compromesso, assicurandoti di scegliere la versione a 12V delle ventole. Questa ventola da 140mm può produrre fino a 1300W di calore mantenendo un livello teorico di rumore di 31 dB. Per poter montare queste ventole da 140mm, dovrai utilizzare un adattatore da 140mm a 120mm che puoi trovare nel negozio di DécouvreBitcoin. Aggiungeremo anche delle griglie di protezione da 140mm.

![image](assets/piece/1.webp)
![image](assets/piece/2.webp)
![image](assets/piece/3.webp)

Anche la ventola dell'alimentatore è abbastanza rumorosa e deve essere sostituita. Consigliamo il Noctua NF-A6x25 PWM. Nota che i connettori delle ventole Noctua non sono gli stessi di quelli originali, quindi avrai bisogno di un adattatore per collegarli, ne bastano 2. Anche qui, assicurati di scegliere la versione a 12V della ventola.

![image](assets/piece/4.webp)
![image](assets/piece/5.webp)

### 2. Aggiungere un bridge WIFI/Ethernet

Invece di utilizzare un cavo Ethernet, puoi connettere il tuo Antminer tramite WIFI aggiungendo un bridge WIFI/Ethernet. Abbiamo selezionato il vonets vap11g-300 perché consente di recuperare facilmente il segnale WIFI del tuo router e trasmetterlo al tuo Antminer tramite Ethernet senza creare una sottorete. Se hai competenze elettriche, puoi alimentarlo direttamente con l'alimentatore dell'Antminer senza bisogno di aggiungere un caricatore USB, per questo avrai bisogno di un jack femmina da 5,5mmx2,1mm.

![image](assets/piece/6.webp)
![image](assets/piece/7.webp)

### 3. Opzionale: aggiungere una presa connessa

Se desideri accendere/spegnere il tuo Antminer dal tuo smartphone e monitorarne il consumo energetico, puoi aggiungere una presa smart. Abbiamo testato la presa ANTELA nella versione 16A compatibile con l'applicazione smartlife. Questa presa smart consente di consultare il consumo giornaliero e mensile e si connette direttamente al tuo router Internet tramite Wi-Fi.
![image](assets/piece/8.webp)

> Elenco del materiale e link
>
> - 2X adattatore 3D da 140mm a 120mm
> - 2X NF-A14 iPPC-2000 PWM [link](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)
> - 2X Griglie per ventilatori da 140mm [link](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
> - Noctua NF-A6x25 PWM [link](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
> - Morsetto elettrico da 2,5mm2 [link](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
> - Vonets vap11g-300 [link](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1> - Optionnel prise connectée ANTELA [link](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

## Capitolo 3 - TUTORIAL: Come si trasforma un minatore in un riscaldatore?

![immagine](assets/hardware/0.webp)

Se siete esperti del fai-da-te e volete trasformare un miner in un riscaldatore, questo tutorial fa per voi. Vorremmo avvertirvi che le modifiche alle apparecchiature elettroniche possono presentare rischi elettrici e di incendio. È quindi essenziale prendere tutte le precauzioni necessarie per evitare danni o lesioni.
Quando esce dalla fabbrica, un minatore non può essere utilizzato come radiatore in casa, perché è troppo rumoroso e non può essere regolato. Tuttavia, è possibile apportare semplici modifiche per risolvere questi problemi.

> AVVERTENZA: è essenziale che Braiins OS+ sia installato prima sul vostro minore, o qualsiasi altro software in grado di ridurre le prestazioni della vostra macchina. Questo è fondamentale perché, per ridurre il rumore, installeremo ventole meno potenti, in grado di dissipare meno calore.

### Materiali richiesti

- 2 pezzi di adattatore 3D da 140 mm a 120 mm
- 2 ventole Noctua NF-A14 iPPC-2000 PWM
- 2 griglie per ventole da 140 mm
- 1 ventola Noctua NF-A6x25 PWM
- Zucchero da elettricista da 2,5 mm2
- Vonets VAP11G-300
- Opzionale: presa collegata ANTELA

### Sostituzione delle ventole

Inizieremo sostituendo la ventola dell'alimentatore.

> ATTENZIONE: Prima di tutto, prima di iniziare, assicuratevi di aver staccato la spina del vostro minore per evitare qualsiasi rischio di folgorazione.

![immagine](assets/hardware/1.webp)

Inizieremo sostituendo la ventola dell'alimentatore.

Per prima cosa, rimuovere le 6 viti sul lato del case che lo tengono chiuso. Una volta rimosse le viti, aprire con attenzione il case per rimuovere la plastica che copre i componenti.

![image](assets/hardware/2.webp)
![image](assets/hardware/3.webp)'

Ensuite, è il momento di rimuovere la ventola originale facendo attenzione a non danneggiare gli altri componenti. Per farlo, rimuovi le viti che la tengono in posizione e stacca delicatamente la colla bianca che circonda il connettore. È importante procedere con delicatezza per evitare di danneggiare i fili o i connettori.

![image](assets/hardware/4.webp)

Una volta rimossa la ventola originale, noterai che i connettori della nuova ventola Noctua non corrispondono a quelli della ventola originale. Infatti, la nuova ventola ha 3 fili, di cui uno giallo che permette di controllare la velocità. Tuttavia, questo filo non verrà utilizzato in questo caso specifico. Per collegare la nuova ventola, è quindi consigliabile utilizzare un adattatore speciale. È importante notare che questo adattatore può talvolta essere difficile da trovare.

![image](assets/hardware/5.webp)

Se non hai questo adattatore, puoi comunque procedere al collegamento della nuova ventola utilizzando un morsetto per elettricisti. Per farlo, dovrai tagliare i cavi della vecchia e della nuova ventola.

![image](assets/hardware/6.webp)
![image](assets/hardware/7.webp)

Sulla nuova ventola, usa un cutter e taglia delicatamente i contorni del rivestimento principale a 1 cm senza tagliare i rivestimenti dei cavi sottostanti.

![image](assets/hardware/8.webp)

Poi, tirando verso il basso il rivestimento principale, taglia i rivestimenti dei cavi rossi e neri nello stesso modo di prima. E taglia il cavo giallo a filo.

![image](assets/hardware/9.webp)

Sulla vecchia ventola è più delicato tagliare il rivestimento principale senza danneggiare i rivestimenti dei cavi rossi e neri. Per farlo, abbiamo usato un ago che abbiamo infilato tra il rivestimento principale e i fili rossi e neri.

![image](assets/hardware/10.webp)
![image](assets/hardware/11.webp)

Una volta liberati i fili rossi e neri, taglia delicatamente i rivestimenti per non danneggiare i fili elettrici.

![image](assets/hardware/12.webp)

Poi collega i cavi con un morsetto, il filo nero con il nero e il filo rosso con il rosso. Puoi anche aggiungere del nastro isolante per elettricisti.

![image](assets/hardware/13.webp)
![image](assets/hardware/14.webp)

Una volta effettuato il collegamento, è il momento di posizionare la nuova ventola Noctua con la griglia e le vecchie viti, le nuove viti che si trovano nella scatola verranno riutilizzate in seguito. Assicurati di posizionarla nella giusta orientazione. Noterai una freccia su uno dei lati della ventola, che indica la direzione del flusso d'aria. È importante posizionare la ventola in modo che questa freccia punti verso l'interno del case. Poi ricollega la ventola.
![image](assets/hardware/15.webp)![image](assets/hardware/16.webp)

> Opzionale: Se sei competente in elettricità, puoi aggiungere direttamente all'uscita di alimentazione 12V un connettore jack da 5,5 mm femmina che permetterà di alimentare direttamente il bridge Wi-Fi Vonet. Tuttavia, se non sei sicuro delle tue competenze in elettricità, è meglio utilizzare il connettore USB con un caricatore di tipo smartphone per evitare qualsiasi rischio di cortocircuito o danni elettrici.

![image](assets/hardware/17.webp)

Una volta effettuati i collegamenti, rimetti bene la plastica del coperchio sopra la plastica del case e non all'interno.

![image](assets/hardware/18.webp)

Infine, rimetti il coperchio del case al suo posto e riavvita le 6 viti sui lati per mantenere tutto ben fermo. Ecco fatto, la tua alimentazione è ora dotata di una nuova ventola.

### Sostituzione delle 2 ventole principali

1. Prima di tutto, scollega le ventole e svitale.
   ![image](assets/hardware/19.webp)

2. I connettori delle nuove ventole Noctua non corrispondono a quelli originali, ma niente panico! Prendi il tuo cutter e taglia delicatamente le piccole linguette di plastica in modo che i connettori si adattino perfettamente al tuo miner.

![image](assets/hardware/20.webp)
![image](assets/hardware/21.webp)

3. È ora di installare le parti in 3D!
   Fissale su entrambi i lati del miner utilizzando le viti che hai rimosso dalle ventole. Avvita fino a quando la testa della vite si infila nella parte in 3D e questa viene mantenuta saldamente in posizione. Attenzione a non stringere troppo, potresti deformare la parte e una delle viti potrebbe toccare un condensatore! Poi taglia delicatamente le piccole linguette di plastica in modo che i connettori si adattino perfettamente al tuo miner.

![image](assets/hardware/22.webp)

4. Passiamo ora alle ventole.
   Fissale sulle parti in 3D utilizzando le viti fornite nella confezione. Presta attenzione alla direzione del flusso d'aria, le frecce sui lati delle ventole ti indicheranno la direzione da seguire. Vai dal lato della porta Ethernet all'altro lato. Vedi foto qui sotto

![image](assets/hardware/23.webp)
![image](assets/hardware/24.webp)
![image](assets/hardware/25.webp)

5. Ultimo passaggio: collega le ventole e fissa le griglie sopra con le viti che non sono state utilizzate nella confezione della ventola dell'alimentazione. Ne hai solo 4, ma 2 per griglia negli angoli opposti saranno sufficienti. Se necessario, puoi cercare altre viti simili in un negozio di ferramenta.

![image](assets/hardware/26.webp)
'![image](assets/hardware/27.webp)

In attesa di poter offrire un case più sexy al tuo nuovo riscaldamento, puoi collegare il case e l'alimentazione insieme con fascette da elettricista.

![image](assets/hardware/28.webp)

E per il tocco finale, collega il bridge Vonet alla porta Ethernet con il suo alimentatore. Se non l'hai ancora fatto, puoi seguire questo tutorial per configurare il tuo bridge.

![image](assets/hardware/29.webp)

Ecco fatto, bravo! Hai appena sostituito l'intera parte meccanica del tuo minatore. Ora dovresti sentire molto meno rumore.

## Capitolo 4 - Modifica del software - Ripristinare un Antminer S9

**Serie di articoli proposta da BlobOnChain & Ajelex - 15/02/2023**

### Ripristino tramite il pulsante "Reset"

Questo metodo può essere applicato entro 10 minuti dall'avvio del minatore.

Dopo aver acceso il minatore per 2 minuti, premi il pulsante "Reset" per 5 secondi, quindi rilascialo. Il minatore verrà ripristinato alle impostazioni di fabbrica entro 4 minuti e si riavvierà automaticamente (non è necessario spegnerlo).

![image](assets/software/1.webp)

Ripristino tramite il lato web

Accedi all'interfaccia utente del tuo minatore, clicca su "Upgrade" >> "Effettua un ripristino", quindi clicca su "OK" nella finestra pop-up.

### Sistema operativo originale

Per questa parte, supporremo che la macchina funzioni, sia accesa e che il suo sistema operativo originale sia installato. Vedremo brevemente l'interfaccia del sistema operativo originale proposta da Bitmain.

Innanzitutto, accedi alla tua macchina tramite la tua rete locale:

![image](assets/software/2.webp)

Una volta sulla pagina di accesso, dovrai accedere all'ASIC utilizzando le credenziali predefinite:

- username: root
- password: root

(Come ripristinare se la password predefinita non funziona?)

Il sistema operativo principale è relativamente semplice. Con le 4 schede: Sistema, Configurazione del minatore, Stato del minatore, Rete. Nella scheda Configurazione del minatore puoi configurare fino a 3 pool di mining.

![image](assets/software/3.webp)

Nella scheda Stato del minatore puoi osservare diverse informazioni sul funzionamento dell'ASIC in tempo reale. L'hashrate espresso in GH/s, informazioni più precise sul pool e dettagli sullo stato di ogni hashboard e sulla velocità delle ventole in rotazioni al minuto.

![image](assets/software/4.webp)

### Braiins OS+'

Vediamo ora il software Braiins OS+ ASIC (https://braiins.com/os/plus). Il software è sviluppato da Braiins (https://braiins.com/), la società madre di Braiins Pool (https://braiins.com/pool). Al momento in cui scriviamo, questo pool di mining detiene il 4,39% dell'hashrate globale (https://mempool.space/fr/mining/pool/slushpool). La società con sede a Praga era precedentemente nota come Slushpool ed è stata la prima mining pool a essere lanciata nel novembre 2010. Oggi l'azienda, che ha un'ampia gamma di attività, offre strumenti di studio della redditività per il mining (https://insights.braiins.com/en), soluzioni per la gestione delle farm di mining insieme all'attività del pool e software di ottimizzazione per gli ASIC. Offre inoltre il mining con il nuovo protocollo Stratum V2 (https://braiins.com/bitcoin-mining-stack-upgrade).

Vediamo quindi da vicino come funzionano i dispositivi di Bitmain, che attualmente sono gli unici modelli compatibili:

- S19, S19 Pro, S19j, S19j Pro, T19,

- 17, S17 Pro, S17+, S17e, T17, T17+, T17e e S9 [i, j]

Il software Braiins OS può essere installato in modo semplice su tutte le macchine sopra elencate. Permette un controllo più preciso della macchina, consentendo l'overclock o l'underclock. Inoltre, consente di regolare con precisione la frequenza di ciascun chip grazie a una funzione di ottimizzazione automatica chiamata autotuning. Poiché ogni chip hash è leggermente diverso a causa del processo di produzione, il software verifica la frequenza ottimale per ciascuno di essi per ottenere la massima efficienza (W/TH). Il software sostiene che le prestazioni possono essere superiori fino al 25% rispetto all'originale. Secondo le nostre misurazioni, è possibile raggiungere queste cifre.

## Installazione di Braiins OS+

Esistono diversi modi per installare Braiins OS+ su un ASIC. Potete fare riferimento a questa guida, ma anche alla documentazione ufficiale di Braiins e ai video tutorial.
Installazione di Braiins OS+ direttamente sulla memoria di Antminer

Scoprite come installare facilmente Braiins OS+ direttamente sulla memoria del vostro Antminer con BOS toolbox, sostituendo così il sistema operativo originale, utilizzando i passaggi descritti di seguito. Se si desidera mantenere il sistema operativo originale in parallelo, è possibile installare Braiins OS+ su una scheda SD.

1. Accendete il vostro Antimner e collegatelo alla vostra Internet Box.
2. Télécharger BOS toolbox Windows / Linux
3. Decomprimi il file scaricato e apri il file bos-toolbox.bat, seleziona la lingua e dopo qualche istante vedrai questa finestra:
   ![image](assets/software/5.webp)

4. Bos toolbox ti permetterà di trovare facilmente l'indirizzo IP del tuo Antminer e installare Braiins OS+. Se conosci già l'indirizzo IP della tua macchina, puoi passare al passaggio 8. Altrimenti, vai alla scheda di scansione.

![image](assets/software/6.webp)

5. Di solito, negli home network, l'intervallo di indirizzi IP si trova tra 192.168.1.1 e 192.168.1.255, quindi inserisci "192.168.1.0/24" nel campo IP range. Se la tua rete è diversa, modifica questi indirizzi. Poi clicca su "Start".

6. Attenzione, se l'Antminer ha una password, la rilevazione non funzionerà. In tal caso, il modo più semplice è eseguire un reset di fabbrica.

7. Dovresti vedere tutti gli Antminer sulla tua rete, qui l'indirizzo IP è 192.168.1.37.

![image](assets/software/7.webp)

8. Clicca su "Back" e poi sulla scheda "install", inserisci l'indirizzo IP trovato in precedenza nel campo Miner(s) e "admin" (o "root") nel campo Password, che è la password predefinita, quindi clicca su "Start".
   Se l'installazione non funziona né con "admin" né con "root" come password, potrebbe essere necessario eseguire un reset di fabbrica e riprovare.

![image](assets/software/8.webp)

9. Dopo qualche istante, il tuo Antminer si riavvierà e potrai accedere all'interfaccia di Braiins OS+ all'indirizzo IP indicato, qui 192.168.1.37, da inserire direttamente nella barra degli indirizzi del tuo browser. L'username predefinito è "root" e non c'è password predefinita.
   Installazione di Braiins OS+ su una scheda SD

![image](assets/software/9.webp)

![image](assets/software/10.webp)

Il secondo metodo utilizza l'interfaccia originale del tuo Antminer. Questo metodo funziona per le macchine con un sistema operativo precedente al 2019.

### Interfaccia Antminer

1. Scarica il nuovo sistema operativo da installare qui.
2. Come nella sezione precedente, connettiti alla tua macchina tramite la rete locale.
3. Vai alla scheda "System" e poi "Upgrade".
4. Carica il file che hai scaricato e flasha l'immagine.

![image](assets/software/11.webp)

### Scheda micro SD

Un secondo metodo ti consente di utilizzare una scheda micro SD. Questo metodo funziona solo per le macchine con un sistema operativo successivo al 2019.

1. Scarica il nuovo sistema operativo da installare qui.

2. Flasha l'immagine scaricata su una scheda micro SD. Per farlo, puoi utilizzare Etcher. Semplicemente copiare il file nella scheda micro SD non funzionerà.
3. Se possiedi un Antminer S9 e le sue varianti (S9i, S9j), dovrai regolare dei "jumper" per forzare il tuo ASIC a avviarsi dal file contenuto nella scheda micro SD anziché dalla NAND. Se hai un altro modello, puoi passare alla parte 4. I jumper si trovano sulla scheda di controllo nella parte superiore dell'ASIC, vicino alla porta Ethernet. Dovrai rimuoverla facendola scorrere all'indietro. Una volta modificata la posizione del jumper come mostrato nelle immagini qui sotto BOOT FROM SD, puoi reinserire la scheda di controllo e ricollegare l'S9.

![image](assets/software/12.webp)

![image](assets/software/13.webp)

4. Inserisci la scheda micro SD nell'ASIC.
5. Avvia l'ASIC. Se è stata utilizzata la versione di installazione automatica, il nuovo sistema operativo verrà installato automaticamente. L'installazione è completata quando entrambi i LED si accendono contemporaneamente. Puoi riavviare l'ASIC e rimuovere la scheda micro SD. Se è stata scaricata un'altra versione, dovrai lasciare la scheda micro SD all'interno dell'ASIC.

Per ulteriori informazioni sull'installazione, puoi visitare questa sezione del sito di Braiins.

## L'interfaccia

Dovrai connetterti al tuo ASIC in modo simile, utilizzando l'indirizzo IP locale del tuo dispositivo sulla tua rete tramite un browser.

Le credenziali predefinite sono le stesse del sistema operativo originale.

- username: root
- password: root

Verrai quindi accolto dal Dashboard di Brains OS+.

### Dashboard

![image](assets/software/14.webp)

In questa prima pagina potrai osservare le prestazioni della tua macchina in tempo reale.

- Tre grafici in tempo reale che mostrano la temperatura, l'hashrate e lo stato complessivo della tua macchina.
- A destra l'hashrate effettivo, la temperatura media dei chip, l'efficienza stimata in W/THs e il consumo energetico.
- Sotto la velocità di rotazione delle ventole in percentuale rispetto alla velocità massima e il numero di rotazioni al minuto.

![image](assets/software/15.webp)

- Più in basso troverai una vista dettagliata di ogni hashboard. La temperatura media della scheda e dei chip che la compongono, la tensione e la frequenza.
- Un dettaglio sui pool di mining attivi in Pools.
- Lo stato dell'autotuning in Tuner Status.
- A destra i dettagli sulle parti trasmesse al pool.

### Configurazione

![image](assets/software/16.webp)

### Sistema

![image](assets/software/17.webp)

### Azioni rapide

![image](assets/software/18.webp)

Configurazione di un pool

Un pool minerario può essere considerato come una cooperativa agricola. Gli agricoltori mettono in comune la loro produzione per ridurre la varianza della domanda e dell'offerta e ottenere così un reddito più stabile per la loro azienda agricola. Un mining pool funziona allo stesso modo, ma le materie prime messe in comune sono gli hash. La scoperta di un singolo hash valido consente di creare un blocco e di ottenere la ricompensa di 6,25 BTC più le commissioni di transazione incluse nel blocco. Se si effettua il mining da soli, si viene ricompensati solo quando si trova un blocco. Competendo contro tutti gli altri minatori del pianeta, avreste pochissime possibilità di vincere questa grande lotteria e dovreste comunque pagare le commissioni associate all'utilizzo del vostro miner, senza alcuna garanzia di successo. I pool di mining risolvono questo problema mettendo in comune la potenza di calcolo di diversi (migliaia) minatori e dividendo le ricompense tra loro in base alla percentuale di hashrate del pool che viene raggiunta quando viene trovato un blocco. È possibile utilizzare questo strumento per vedere le proprie possibilità di estrarre un singolo blocco. Se si inseriscono le informazioni per un Antminer S9, si può vedere che le probabilità di trovare un hash che consenta la creazione di un blocco sono 1/24.777.849 per ogni blocco, o 1/ 172.068 al giorno. In media (con un hashrate e una difficoltà costanti) ci vorrebbero 471 anni per trovare un blocco.

Tuttavia, poiché il Bitcoin è una questione di probabilità, i minatori solitari sono talvolta ricompensati per aver corso tali rischi: Solo Bitcoin Miner risolve il blocco con un tasso di hash di soli 10 TH/s, battendo probabilità estremamente improbabili - Decrypt

Se vi piace il gioco, potete provarci, ma la nostra guida non andrà in quella direzione. Ci concentreremo invece sul pool di mining più adatto alle nostre esigenze.

Le considerazioni da tenere in considerazione nella scelta di un pool di mining sono il funzionamento delle ricompense del pool, che possono essere diverse, così come l'importo minimo prima di poter prelevare le ricompense su un indirizzo. Ad esempio, Braiins, che propone il software di cui stiamo parlando qui, propone anche un pool. Questo pool ha un sistema di ricompensa chiamato "Score" che incoraggia i minatori a minare per lunghi periodi. La partecipazione include un fattore di tempo di attività che viene espresso con un "scoring hashrate". Nel nostro caso, in cui desideriamo un sistema di riscaldamento che può essere acceso solo per pochi minuti, questo non è il sistema di ricompensa ideale. Preferiamo invece un sistema di ricompensa che ci dia una ricompensa uguale per ogni partecipazione. Inoltre, l'importo minimo di prelievo per Braiins Pool è di 100.000 sats e On-Chain. Quindi perdiamo alcuni sats in commissioni di transazione e una parte della nostra ricompensa può essere bloccata se non miniamo abbastanza durante l'inverno.

Il modello di ricompensa che ci interessa è il PPS, che significa "pay-per-share". Questo significa che il minatore riceverà una ricompensa per ogni azione valida. Esiste anche una variante di questo sistema, il FPPS (Full Pay Per Share), che divide non solo la ricompensa della coinbase, ma anche le commissioni di transazione incluse nel blocco. I pool di mining che consigliamo per collegare la tua attività di mining/riscaldamento sono Linecoin Pool (FPPS) e Nicehash (PPS).

- Nicehash: Il vantaggio di Nicehash è che il prelievo può essere effettuato utilizzando Lightning con commissioni minime. Inoltre, l'importo minimo di prelievo è di 2000 sats. Lo svantaggio è che Nicehash utilizza il suo hashrate per la blockchain più redditizia, senza dare realmente il controllo all'utente e quindi potrebbe non partecipare al hashrate di Bitcoin.

- Lincoin: Il vantaggio di Linecoin è il numero di funzionalità offerte, come un pannello di controllo dettagliato, la possibilità di effettuare prelievi con un Paynym (BIP 47) per una maggiore protezione della privacy e l'integrazione di un bot Telegram e automazioni direttamente configurabili nell'applicazione mobile. Questo pool mina solo blocchi Bitcoin, ma l'importo minimo per il prelievo rimane elevato a 100.000 sats. Esamineremo più in dettaglio l'interfaccia di uno di questi pool in un prossimo articolo.

Per configurare un pool in Braiins 0S+, sarà necessario creare un account in uno dei pool di tua scelta. Qui prenderemo ad esempio Lincoin:

![image](assets/software/19.webp)

Una volta creato il tuo account, fai clic su "Connect To Pool"

Successivamente, copia l'indirizzo Stratum e il tuo nome utente:

![image](assets/software/20.webp)

Ora puoi tornare all'interfaccia di Braiins OS+ per inserire queste credenziali. Per la password, puoi lasciare il campo vuoto.

![image](assets/software/21.webp)

### Overclocking e Underclocking

L'**overclocking** e l'autotuning consistono entrambi nell'aggiustare le frequenze delle schede di hashing per migliorare le prestazioni dell'ASIC. La differenza tra i due risiede nella complessità di queste impostazioni di frequenza.

L'overclocking è un semplice aggiustamento che consiste nell'aumentare la frequenza delle schede di hashing per aumentare il tasso di hashing della macchina. L'underclocking, invece, consiste nel diminuire la frequenza di clock di un circuito integrato al di sotto della sua frequenza nominale. Riducendo la frequenza di clock di un ASIC tramite l'underclocking, si riduce anche il calore generato dall'hardware. Ciò consente di ridurre la velocità dei ventilatori necessari per raffreddare l'ASIC, poiché non devono lavorare così duramente per mantenere una temperatura adeguata. Riducendo la velocità dei ventilatori, si riduce anche il rumore generato dall'ASIC. Ciò può essere particolarmente utile per gli utenti che utilizzano ASIC a casa e cercano di minimizzare le interferenze sonore causate dall'hardware di mining.

È importante notare che l'underclocking può comportare una riduzione delle prestazioni dell'ASIC, quindi è importante trovare un buon equilibrio tra le prestazioni e il rumore.

Braiins OS+ supporta l'overclocking, l'underclocking degli ASIC e l'autotuning. Consente agli utenti di regolare in modo flessibile la frequenza di clock del proprio hardware per massimizzare le prestazioni o risparmiare energia secondo le proprie preferenze.

### Autotuning

Prima del 2018, i minatori avevano due modi per ottenere un vantaggio nella loro attività: trovare elettricità a un costo ragionevole e acquistare hardware più efficiente. Tuttavia, nel 2018, è stata scoperta una nuova avanzata nel campo del software e del firmware di mining, chiamata AsicBoost. Questa tecnica consente ai minatori di ridurre i loro costi di circa il 13% modificando il firmware eseguito sui loro dispositivi.
Aujourd'hui, esiste un nuovo sviluppo nel settore del software e del firmware minerario chiamato autoritimazione (o autotuning) che offre un vantaggio ancora più significativo rispetto ad AsicBoost. Gli ASIC sono composti da numerosi piccoli chip informatici che eseguono l'hashing. Questi chip sono fatti di silicio, lo stesso elemento ampiamente utilizzato nei semiconduttori e in altri componenti microelettronici. La chiave di comprensione qui è che tutti i chip di silicio non sono identici - ognuno può variare leggermente nelle sue proprietà elettriche. I produttori di hardware lo sanno e pubblicano le specifiche di prestazione delle loro macchine minerarie in base al limite inferiore delle loro tolleranze. In altre parole, i produttori conoscono la frequenza che funziona meglio per i chip medi e utilizzano questa frequenza in modo uniforme per tutti i chip della macchina.

Ciò pone un limite superiore alla velocità di hashing che una macchina può avere. L'autoritimazione è un processo in cui gli algoritmi valutano le frequenze ottimali per l'hashing chip per chip, invece di trattare l'intera macchina come un'unica unità. Ciò significa che un chip di migliore qualità che può eseguire più hash al secondo otterrà una frequenza più alta, mentre un chip di qualità inferiore che può eseguire relativamente meno otterrà una frequenza più bassa. L'autotuning del chip è essenzialmente un modo per ottimizzare le prestazioni di un ASIC tramite il software e il firmware eseguiti su di esso.

Il risultato finale è una velocità di hashing più elevata per watt di elettricità, il che significa margini di profitto più elevati per i minatori. Il motivo per cui le macchine non vengono distribuite con questo tipo di software è che la varianza per macchina non è desiderabile, poiché i clienti vogliono sapere esattamente cosa stanno ottenendo ed è quindi una cattiva idea per i produttori vendere un prodotto che non ha prestazioni costanti e prevedibili da una macchina all'altra. Inoltre, l'autotuning del chip richiede considerevoli risorse di sviluppo, poiché è complesso da implementare. I produttori già spendono molte risorse per sviluppare i propri firmware. Esistono soluzioni software che consentono di implementare l'autotuning, come Braiins OS+. Oltre a migliorare le prestazioni dell'ASIC fino al 20%.

> Guida creata da DecouvreBitcoin, più informazioni su MINAGE 201 - credito a Jim e Ajelex.

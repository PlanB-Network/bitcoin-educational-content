---
name: Valet Bitcoin
description: Valet porta il nodo Lightning non custodiale nella vostra tasca
---

![cover_valet](assets/cover.webp)



## Introduzione


Valet è un sistema leggero, autocustode, Bitcoin e Lightning wallet che offre un processo di onboarding facile e conveniente per i principianti. È stato creato appositamente per servire le comunità Bitcoin e le economie circolari, soprattutto nelle aree remote.


Si tratta di un fork del **Semplice Bitcoin Wallet (SBW)**, con una funzione avanzata di canale Hosted Lightning chiamata **Fiat Channels**, progettata per consentire a chiunque di accettare pagamenti Lightning senza rischi di volatilità.


Valet è attualmente disponibile solo per i dispositivi Android e può essere scaricato e installato da diversi app store aperti. Tuttavia, Valet non è ospitato sul **Google Play Store** a causa di problemi di privacy e KYC degli sviluppatori.



## Scaricare e installare Valet


Valet può essere scaricato come file APK dalla pagina GitHub di Standard Sats. [Standard Sats](https://standardsats.github.io/) è la società che ha sviluppato Valet.


👉 Per scaricare Valet, visitate la pagina Standard Sats [GitHub](https://github.com/standardsats/valet/releases) e individuate l'ultima versione (spesso è quella più in alto).


👉 Andate su **Assets** e cliccate sul file con estensione **.apk**. Il download si avvierà automaticamente.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 Una volta completato il download, andate nel **Gestore file** del vostro dispositivo > **Downloads** e selezionate il file apk di Valet.


![Select_valet_apk](assets/en/002.webp)


👉 Installatela e in pochi secondi l'applicazione sarà pronta e apparirà sulla schermata iniziale.


![valet_icon_on_homescreen](assets/en/003.webp)


In alternativa, è possibile scaricare Valet dall'app store **F-Droid**. Se non avete l'app F-Droid sul vostro dispositivo, potete scaricarla e installarla [qui] (https://f-droid.org/en/).


👉 Nella schermata iniziale, aprire F-Droid e cercare **Valet**. Selezionare la prima opzione con un'icona **viola e bianca** tra le due opzioni visualizzate e fare clic su **Download**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 Dopo il download, fare clic su **Installa** e seguire le istruzioni sullo schermo. Al termine dell'installazione, è possibile avviare Valet da F-Droid facendo clic su **Apri**, oppure avviarlo dalla schermata iniziale del dispositivo.



## Creazione di un Bitcoin Wallet


È possibile configurare un Bitcoin wallet su Valet in due semplici passaggi.


👉 Avviare Valet dalla schermata iniziale del dispositivo o dall'app F-Droid. Verrà visualizzata una schermata di impostazione del wallet con due opzioni: **Crea nuovo Wallet** e **Ripristina Wallet**.


👉 Selezionare **Crea nuovo Wallet** e immediatamente verrà creato un nuovo wallet e si verrà reindirizzati alla pagina iniziale.


![set_up_a\_new_wallet](assets/en/006.webp)



## Backup della frase di partenza


👉 Nella pagina iniziale del wallet, fare clic sulla scheda **Green** con la scritta **"Toccare per salvare la frase di recupero del wallet in caso di perdita o sostituzione del dispositivo "**


![seed_phrase_green_card](assets/en/007.webp)


👉 Verrà visualizzata una serie di 12 parole inglesi. Scrivetele su carta, nell'ordine da 1 a 12, e conservatele.


![the_seed_phrase](assets/en/008.webp)


### Prestare attenzione ⚠️:


Prestate attenzione ai seguenti elementi:


- Come già sapete, Valet è un wallet autocustode, quindi la vostra frase seed è l'unico accesso per recuperare il vostro Wallet.
- Se si perde la frase seed, non si avrà mai accesso al wallet.
- Se qualcuno si impossessa della frase seed, può rubare irrimediabilmente tutti i Bitcoin.


Pertanto, dovrete scrivere la vostra frase seed di 12 parole e conservarla in un luogo sicuro. Non dovete mai fare uno screenshot, salvarla come bozza nella vostra e-mail o salvarla su qualsiasi dispositivo elettronico che sia mai stato connesso a Internet.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Ricezione e invio di Bitcoin su Valet


Valet è un wallet autocustodito con capacità on-chain e Bitcoin Lightning. Ciò significa che è possibile ricevere e inviare Bitcoin da Valet sia tramite un **On-chain** che tramite un **Lightning Network**.


Tuttavia, per poter ricevere o inviare Bitcoin tramite Lightning, è necessario creare un canale Lightning utilizzando i on-chain Bitcoin come Liquidity. In alternativa, è possibile acquistare la liquidità del canale Lightning dai venditori.



## Generazione di una catena Bitcoin Address


Per ricevere il Bitcoin attraverso il on-chain, è necessario generare un indirizzo Bitcoin.


👉 Nella pagina iniziale del wallet sono presenti una scheda **arancione** e una **viola**, rispettivamente etichettate come **Bitcoin** e **Lightning**.


👉 Fare clic sulla scheda arancione con l'etichetta **Bitcoin**. Verrete reindirizzati a una schermata che mostra un indirizzo Bitcoin.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Potete **copiare** l'indirizzo e inviarlo alla persona che vi sta inviando i Bitcoin, oppure fare clic sul pulsante **condividi** per inviare il codice QR alla persona tramite i social media o altri canali di comunicazione.


👉 È inoltre possibile fare clic sul pulsante **Modifica** per impostare la quantità di Bitcoin da inviare a quell'indirizzo.


**Attenzione: ** Come per le fatture, la funzione di modifica è utile negli scenari in cui si desidera ricevere una quantità specifica di Bitcoin a un indirizzo in un determinato momento; tuttavia, ciò non significa che l'indirizzo non possa ricevere quantità superiori o inferiori.


👉 Fare clic su **Altri indirizzi freschi**, per generare nuovi indirizzi casuali.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 È anche possibile generare un indirizzo on-chain Bitcoin facendo clic sul pulsante **Ricevi** in fondo alla pagina iniziale del wallet. Selezionate quindi **Ricevi all'indirizzo bitcoin** e continuate con la stessa procedura di cui sopra.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Invio del Bitcoin tramite catena di continuità


L'invio del Bitcoin dal Valet wallet tramite il on-chain è un'operazione semplice.


👉 Nella parte inferiore della pagina iniziale del wallet, fare clic sul pulsante **Invia**, inserire l'indirizzo del Bitcoin o fare clic su **Scansione**, per scansionare il codice QR dell'indirizzo, quindi fare clic su **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Inserire l'importo Bitcoin che si desidera inviare. È possibile inserire manualmente un importo in termini di Sats o in termini di valuta Fiat, oppure fare clic su **Max** per utilizzare tutto il saldo on-chain.


è inoltre possibile regolare le commissioni da pagare per la transazione facendo clic sul piccolo riquadro verde con l'etichetta **fee** e facendo scorrere il punto bianco a destra o a sinistra per aumentare o diminuire le commissioni, rispettivamente. Fare clic su **Ok** per inviare la transazione.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Impostazione di un canale Lightning Network


Come già detto, Valet è un Bitcoin e un Lightning wallet autocustodi; quindi, per poter inviare e ricevere Bitcoin attraverso la rete Lightning, dovrete prima configurare un canale Lightning, seguendo questi passaggi:


👉 Nella schermata iniziale, fare clic sulla **carta viola** con l'etichetta **Lightning**. Verrà visualizzata una pagina con le seguenti opzioni:



- Scansione del nodo QR
- Acquistare su LNBIG.COM
- Acquista su BITREFILL.COM
- Richiesta di risincronizzazione del grafico LN.


Selezionando **Acquista da lnbig.com** o **Acquista da bitrefill.com**, si verrà reindirizzati ai siti web di queste aziende, dove è possibile acquistare una liquidità in entrata di diverse capacità. Ignorate l'ultima opzione **Richiesta di risincronizzazione del grafico LN** per il momento.


La nostra scelta è quindi quella di **scansionare un QR del nodo**. A questo punto, dovete aver deciso e ottenuto il **codice QR** del nodo verso cui volete aprire un canale. Potete aprire canali verso qualsiasi nodo pubblico di vostra scelta. Consultate [1ML](https://1ml.com/) o [Amboss](https://amboss.space/), selezionate un nodo pubblico a vostra scelta e scansionate il codice QR associato al nodo scelto.


![channel_opening_options](assets/en/016.webp)


👉 Verrete automaticamente reindirizzati alla pagina successiva, dove dovrete finanziare il vostro canale. Anche in questo caso, l'utilizzo della rete Lightning in autocustodia richiede l'utilizzo dei Bitcoin per finanziare un canale. Ciò significa che dovete avere dei Bitcoin nel vostro on-chain wallet con cui finanziare il canale Lightning. Per ulteriori informazioni sulla rete Lightning, consultare questo articolo di [Hacken](https://hacken.io/discover/lightning-network/).


![fund_channel](assets/en/017.webp)


👉 Immettere la **quota** di Bitcoin con cui si desidera finanziare il canale, oppure fare clic su **Max** per utilizzare tutto il saldo on-chain Bitcoin. È possibile regolare la **tassa**, oppure lasciare l'impostazione predefinita e fare clic su **Ok**.


**Attenzione: l'importo con cui si finanzia il canale sarà la capacità del nuovo canale (cioè il volume totale di Sats che può essere transato da e verso quel canale)


È inoltre importante utilizzare più di **100.000 Sats** come importo di finanziamento quando si apre un canale. Questo perché molti nodi Lightning richiedono una capacità minima di 100.000 Sats per aprire un canale. Quindi, per evitare di incorrere in tentativi ed errori, è sufficiente utilizzare importi superiori a tale intervallo.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


a questo punto, quando si controlla la pagina iniziale del wallet, si vedrà che l'importo del finanziamento è stato spostato dalla carta **Bitcoin** alla carta **Lightning**. Nella cronologia delle transazioni, si vedrà che la transazione di finanziamento è in corso di elaborazione.


![channel_funding_processing](assets/en/020.webp)


👉 Se si fa clic sulla carta Lightning, si vedranno le informazioni che indicano l'apertura del canale Lightning. Verrà inoltre visualizzata la **transazione di finanziamento del canale** nell'elenco delle transazioni. Attendete la conferma della transazione di finanziamento sul blockchain e il vostro canale Lightning sarà pronto.


![channel_opening](assets/en/021.webp)


👉 Non appena la transazione di finanziamento viene confermata, fate clic sulla **Carta Lightning** nella vostra home page e vedrete le informazioni sul vostro canale Lightning come segue:



- SET DI NUMERI CASUALI SEPARATI DA PUNTI:** Sono gli indirizzi IP dei nodi. (rispettivamente IPV4 e IPV6)
- CAPACITÀ: ** È il volume totale di Sats che può essere inviato e ricevuto attraverso questo canale
- POSSIBILE INVIARE:** Questa è la quantità di Sats che è possibile inviare in questo momento. Noterete che è quasi la stessa cifra della **Capacità**. Questo perché non avete inviato alcun pagamento attraverso il canale.
- PUO' RICEVERE:** Questo è il numero di Sats che si possono ricevere su questo canale al momento. (A questo punto il numero di Sats che si possono ricevere è minimo o nullo, perché per poterli ricevere si devono prima inviare dei Sats per creare un Liquid in entrata)
- RIMBORSABILE:** Indica l'importo che viene restituito all'indirizzo on-chain quando si chiude il canale. Si tratta anche del **bilancio locale del canale**. Notate che è leggermente inferiore alla capacità del canale, e questo perché quando si chiude un canale, si deve pagare una tassa per pubblicare la transazione di chiusura sul blockchain, proprio come si è fatto durante il finanziamento del canale. Il sistema ha quindi dedotto l'importo più basso che pagherete)
- VALORE IN VOLO:** Quando qualcuno invia del sats al vostro canale, o quando cercate di inviare del sats a qualcuno e, per qualsiasi motivo, la transazione viene ritardata, spesso viene mostrato in questo campo.


![channel_info](assets/en/022.webp)


## Invio di Sats attraverso il vostro canale


L'invio del Sats attraverso il Lightning Network è un'operazione semplice.


👉 In fondo alla pagina iniziale, cliccate su **Invia** e **incollate** la fattura Lightning (dovete averla copiata) nell'apposito campo, oppure cliccate su **Scansiona** per scansionare il codice QR della fattura Lightning.


![click_send_or_scan](assets/en/023.webp)


La maggior parte delle fatture Lightning sono dotate di un importo da pagare preimpostato. In alcuni casi, però, può trattarsi di una fattura aperta in cui è necessario inserire l'importo.


👉 Inserire l'importo in **dollari** o **Sats**, oppure fare clic su **Max**, per utilizzare tutto il saldo del canale Lightning, quindi fare clic su **Ok**. Non appena viene trovato un buon percorso, il pagamento verrà inviato e completato in pochi secondi. Tenete d'occhio la pagina iniziale per vedere se il pagamento è stato completato. Quando il pagamento è stato completato, viene visualizzato un segno di spunta verde.


![enter_the_amount](assets/en/024.webp)


## Ricevere il Sats attraverso il proprio canale


La ricezione di pagamenti sul vostro canale Lightning dipende in larga misura dal fatto che abbiate o meno una Liquidity in entrata. Dopo aver aperto un canale, non sarete in grado di ricevere pagamenti finché non avrete inviato almeno un po' di Sats per **creare liquidità in entrata** dall'altra parte della connessione del canale. Per verificare se potete ricevere Sats e la quantità di Sats che potete ricevere, controllate il campo **Può ricevere** nelle informazioni del vostro canale. Questo vi mostrerà quanti Sats ricevete in ogni momento.


Ora, supponiamo che abbiate inviato alcuni Sats dal vostro canale, che abbiate ora liquidità in entrata e che possiate ricevere Sats.


Per ricevere sul canale Lightning, è necessario generare una fattura. A differenza del Bitcoin on-chain, che utilizza gli indirizzi, la rete Lightning utilizza le fatture. Esistono due percorsi per generare una fattura su Valet.


#### OPZIONE 1


👉 In fondo alla pagina iniziale, fare clic su **Ricevi**, selezionare **Ricevi a fattura Lightning**. Compilare l'importo da ricevere nella fattura e fare clic su **Ok**. Copiare la fattura o condividere il codice QR con il pagatore.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### OPZIONE 2


👉 Fare clic sulla scheda viola Lightning sulla pagina iniziale di wallet. Toccate un punto qualsiasi del vostro canale e apparirà un elenco di opzioni. Selezionare **Ricevi sul canale** e inserire l'importo che si sta ricevendo (in Sats o in dollari). Verrà inoltre visualizzato il numero di Sats che si possono ricevere (capacità in entrata) quando si compila la fattura. Fare clic su **Ok** e copiare la fattura o condividere il codice QR con il pagatore.


![receive_to_channel](assets/en/028.webp)


**Attenzione: ** La prima opzione è un'opzione universale, il che significa che se avete più di un canale attivo e utilizzate la prima opzione, il sistema selezionerà automaticamente uno dei vostri canali per la ricezione del Sats.


Quindi, in questo scenario, la seconda opzione è la migliore da utilizzare se si desidera ricevere Sats su un canale particolare.


### Le opzioni di pop-up del vostro canale spiegate


Quando si tocca il proprio canale, vengono visualizzati i seguenti campi di opzione:


![channel_pop_ups](assets/en/029.webp)


**Questo consente di condividere i dettagli del canale, come l'ID del peer remoto, l'ID del canale locale, la transazione di finanziamento, la data di creazione, ecc.


**È possibile chiudere il proprio canale di illuminazione ogni volta che si desidera. Per chiudere il canale, il sistema controlla il saldo Bitcoin che avete sul vostro lato del canale (ricordate il campo **"Can Send "**, noto anche come saldo locale) e ve lo rimanda. In Valet, potete scegliere dove volete che il Bitcoin venga inviato quando il canale viene chiuso. Quindi, **Chiudi canale a wallet** è una delle due opzioni.


👉 Fare clic su questa opzione e selezionare **Bitcoin**. La chiusura del canale avrà inizio e il saldo del canale Bitcoin verrà rinviato all'indirizzo on-chain del wallet.


![close_channel_to_wallet](assets/en/030.webp)


**Chiudere il canale a ADDRESS:** Questa è la seconda opzione per chiudere un canale. Quando si sceglie questa opzione, viene richiesto di inserire un indirizzo wallet a cui inviare il saldo Bitcoin del canale. Si noti che in questa opzione è possibile scansionare solo il codice QR dell'indirizzo Bitcoin a cui si vuole chiudere il canale. Al momento non esiste un'opzione per incollare manualmente l'indirizzo.


👉 Fare clic su questa opzione, scansionare l'indirizzo del Bitcoin e fare clic su **Ok**. La chiusura del canale avrà inizio e il saldo del Lightning Bitcoin verrà inviato all'indirizzo scansionato.


![scan_address_and_Ok](assets/en/031.webp)


**RICEVI A CANALE:** È la stessa cosa che generare una fattura, ma in alcuni casi si può avere più di un canale, compresi i canali Fiat (un tipo unico di canale Lightning ottenibile nel Valet wallet). Quindi, se si hanno più canali aperti, questa opzione garantisce la possibilità di ricevere il pagamento su un canale specifico.


**Questa opzione consente di ricaricare un canale da altri canali esistenti. Ad esempio, se avete due diversi canali Lightning (A e B) e il saldo del Bitcoin sul canale A si è esaurito, con questa opzione potete facilmente e automaticamente ricaricare il saldo del canale A dal canale B.


**Anche questa è un'opzione per generare una fattura per ricevere il pagamento, ma quando si utilizza questa opzione, il mittente paga direttamente. Ciò significa che il pagamento non passa attraverso diversi nodi prima di arrivare all'utente, come avviene per un normale pagamento Lightning. In sostanza, il mittente sa che è stato pagato da voi, conosce il vostro ID canale, ecc. Questa opzione può essere utilizzata quando si riceve un pagamento da una fonte di cui ci si fida e non è necessario mantenere la privacy.


## Canali Hosted e Fiat


Come molti altri Bitcoin wallet, Valet è un Bitcoin e Lightning wallet semplice e leggero. Ma ha un'esclusiva caratteristica Lightning che lo differenzia dalla maggior parte degli altri Bitcoin wallet. Questa funzione si chiama **Canali ospitati e Fiat**.


I canali Fiat sono un tipo di implementazione Lightning che consente un facile onboarding e utilizzo della rete Lightning. Si tratta di una soluzione di custodia che consente il pieno anonimato, proprio come un normale canale Lightning. La tecnologia dei canali Fiat consente anche la creazione di derivati Bitcoin sulla rete Lightning. Con i canali Fiat, ad esempio, i commercianti possono accettare pagamenti Bitcoin di valore stabile senza preoccuparsi della volatilità del Bitcoin.


L'attuale implementazione dei canali Fiat su Valet consente di creare valute Fiat sintetiche stabili sostenute da Sats. Utilizza una relazione Host-Client in cui l'Host è un qualsiasi nodo Lightning che offre questo servizio e il cliente è l'utente di Valet. Si tratta di una soluzione di custodia perché tutti i Sats si trovano sul lato dell'host; tuttavia, la generazione delle fatture, l'instradamento dei tor e la generazione delle preimmagini avvengono ancora sul lato del cliente come in un normale canale Lightning.


L'apertura di un canale Fiat avviene con la stessa procedura dell'apertura di un canale Lightning. L'unica differenza significativa è che in questo caso il cliente (utente Valet) non deve impegnare alcuna liquidità on-chain per creare la capacità del canale. L'host imposta la capacità del canale e gestisce tutti i pagamenti per il cliente.


👉 Per aprire un canale Fiat, fare clic sulla scheda viola **Lightning** nella pagina iniziale del wallet. Selezionare **Scan Node QR** (a questo punto, è necessario aver identificato un Host verso cui si desidera aprire un canale e aver ottenuto il QR del nodo. Un esempio di nodo host verso cui è possibile aprire un canale Fiat è il nodo SATM dello Standard Sats)


**Attenzione:** È importante notare che chiunque può essere un Host. È sufficiente gestire un nodo Lightning con il plugin **Fiat channel** e un servizio **Hedging**. I canali Fiat sono un progetto open-source di *Standard Sats*. Per saperne di più [qui] (https://github.com/standardsats/fiat-channels-rfc) e [qui] (https://standardsats.github.io/).


Nodo SATM QR sotto:


![SATM_node_QR](assets/en/032.webp)


👉 Una volta scansionato il QR del nodo, cliccate su **Richiesta canale fiat USD** o **Richiesta canali fiat EUR** (questa è la denominazione fiat in cui saranno quotati i vostri saldi Fiat). Per ora, scegliete USD e cliccate su **OK**. Il canale verrà aperto automaticamente e potrete iniziare a ricevere il Sats immediatamente. Vedete, è così semplice!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Andate alla pagina iniziale del vostro wallet, vedrete una scheda **verde chiaro** etichettata **USD**, che è il vostro **canale Fiat**.


![fiat_channel_card](assets/en/035.webp)


**Attenzione:** Quando si riceve il Sats su un canale Fiat, il valore fiat del Sats ricevuto viene bloccato come saldo stabile, mentre il volume del Sats fluttua con il prezzo del Bitcoin. Questa soluzione è stata pensata soprattutto per i commercianti che vogliono accettare il Sats per i pagamenti ma non vogliono affrontare le sfide della volatilità del Bitcoin. Ciò consente loro di mantenere un valore stabile in ogni momento, pur potendo effettuare transazioni sulla rete Lightning, godendo della portata globale e della rapidità di regolamento del Bitcoin come mezzo di scambio sul Lightning Network.


Quando viene creato il canale Fiat, vengono visualizzati i seguenti campi Valore e il significato di ciascuno di essi:


![fiat_channel_info](assets/en/036.webp)



- SET DI NUMERI CASUALI SEPARATI DA PUNTI:** Sono gli indirizzi IP dei nodi. (rispettivamente IPV4 e IPV6)
- TASSO SERVER:** Questo è il prezzo di mercato Bitcoin a cui l'Host offre i servizi all'utente. Spesso sarà leggermente diverso dal prezzo di mercato predominante, perché un Host può aggiungere un piccolo premio. Spetta esclusivamente all'host decidere questa tariffa, che quindi può variare da host a host.
- SALDO FIAT: ** È il valore fiat stabile bloccato di ogni sat ricevuto su questo canale. Come spiegato in precedenza, ogni volta che si riceve Sats sul proprio canale Fiat, il valore fiat del Sats al momento della ricezione viene immediatamente bloccato come valore fiat sintetico stabile in questo campo. Il valore del vostro **saldo fiat** non fluttua con il prezzo di mercato del Bitcoin. Ogni volta che si desidera effettuare pagamenti da questo canale, è possibile inviare solo l'equivalente in Sats di questo saldo Fiat. Consideratelo quindi come una moneta fiat digitale sostenuta dal Sats.
- CAPACITÀ:** È il volume totale di Sats che può essere inviato e ricevuto attraverso questo canale. (Anche questo è impostato dall'host. A differenza di un normale canale Lightning, questa capacità può essere regolata dall'host a seconda dei casi)
- POSSIBILE INVIO:** Questo è il volume di Sats che si può inviare in ogni punto in base al proprio saldo fiat. Si tratta di un valore completamente diverso da quello che si ha in un normale canale Lightning, perché questo valore fluttua con il prezzo del Bitcoin. Quindi, quello che vedete qui è il valore Sats del vostro saldo Fiat in qualsiasi momento, basato sul **Tasso del server**.
- PUO' RICEVERE:** È il numero di Sats che si possono ricevere al momento su questo canale. Dopo aver creato il canale, questo valore dovrebbe essere uguale alla capacità del canale.
- VALORE IN VOLO:** Quando qualcuno invia un sats al vostro canale o quando cercate di inviare un sats a qualcuno e, per qualsiasi motivo, la transazione viene ritardata, questo campo viene spesso visualizzato.


Ecco alcune cose importanti da notare sui canali Fiat:



- A differenza di un normale canale Lightning, quando si apre un canale fiat, si può iniziare immediatamente a ricevere Sats, ma non si può inviare. È possibile inviare Sats solo dopo aver ricevuto Sats.
- In ogni momento, l'attività che viene inviata da e verso è il Sats. Il *bilancio Fiat* è solo una rappresentazione IOU sintetica di un valore Bitcoin ricevuto in qualsiasi momento. Non si tratta quindi di una creazione di token o di una nuova criptovaluta.
- Il canale Fiat è utile soprattutto ai commercianti/imprese che sono scettici nell'accettare pagamenti in Bitcoin a causa delle preoccupazioni sulla volatilità. Può essere utile anche alle aziende che vogliono pagare gli stipendi dei propri dipendenti in Bitcoin senza subire le conseguenze della volatilità del Bitcoin, che può rendere instabile il capitale salariale. Può essere utile anche per gli individui che vivono in un'area con un uso predominante del Bitcoin, ma che hanno costi di vita fissi.
- Si noti che non c'è un campo con l'etichetta **REFUNDABLE**. Questo perché, tecnicamente, non è possibile chiudere un canale Fiat. Si può smettere di usare un canale Fiat solo scaricando il suo saldo nel normale canale Fulmine.


### Le opzioni del Pop-Up del canale Fiat spiegate


Quando si tocca il proprio canale Fiat Lightning, vengono visualizzati i seguenti campi:


![fiat_channel_pop_up](assets/en/037.webp)


**Questo consente di condividere i dettagli del canale Fiat, come l'ID del peer remoto, l'ID del canale locale, la data di creazione, ecc.


**Questo permette di esportare lo stato di un canale in qualsiasi momento. Questo è solitamente utile per correggere gli errori del canale e un host può chiedere di condividerlo se è necessario.


**Come già detto, non è possibile chiudere tecnicamente un canale Fiat, ma è possibile scaricare il saldo del canale nel canale Lightning normale esistente. Questo sposta automaticamente l'equivalente Sat del saldo Fiat nel canale Fulmine normale.


**RICEVI A CANALE:** È la stessa cosa che generare una fattura, ma in alcuni casi un utente può avere più di un canale Fiat con host diversi, compresi i normali canali Lightning. Pertanto, se un utente ha più canali aperti, questa opzione garantisce che possa ricevere il pagamento su un canale specifico.


**Questa opzione è una funzione che permette all'utente di riempire un canale da altri canali esistenti. Quindi, con questa opzione, è possibile ricaricare il proprio canale Fiat da un canale normale o da altri canali Fiat esistenti, proprio come si potrebbe fare con il drenaggio.


**Anche questa è un'opzione per generare una fattura per ricevere il pagamento, ma quando si utilizza questa opzione, il mittente paga direttamente. Ciò significa che il pagamento non passa attraverso diversi nodi prima di arrivare all'utente. In sostanza, il mittente sa che è stato pagato da voi, conosce il vostro ID canale, ecc. Questa opzione può essere utilizzata spesso quando si riceve un pagamento da una fonte di cui ci si fida e non si ha bisogno di mantenere la propria privacy.


## Impostazioni del valet:


Come ogni altra applicazione, anche Valet ha delle impostazioni che possono essere regolate in base ai propri gusti. È possibile accedere alla pagina delle impostazioni dalla schermata iniziale.


👉 Nella schermata iniziale, fare clic sull'icona **Gear** situata nell'angolo superiore destro dello schermo per accedere alle impostazioni. Di seguito sono riportati i componenti della sezione impostazioni.


![settings_icon](assets/en/038.webp)


**Se questa opzione è altrimenti **Disabilitata,** è necessario abilitarla perché è l'unico modo per recuperare i canali Lightning normali in caso di disinstallazione e reinstallazione di Valet. Lo spiegheremo più avanti. Fare quindi clic su questo pulsante e dare a Valet il permesso di accedere al **magazzino multimediale**, perché è lì che viene salvato il file di backup.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**Dove archiviare il backup locale:** Se avete dato a Valet l'autorizzazione per l'archiviazione, questo campo sarà automaticamente impostato per archiviare i backup locali nella cartella **Downloads**. Ma è possibile modificarlo facendo clic qui e selezionando una cartella a scelta.


**Gestire i portafogli a catena** Si tratta di un'operazione un po' tecnica, di cui non è necessario occuparsi a meno che non si sia abbastanza esperti. L'impostazione predefinita va bene.


**Non ci si deve preoccupare di questo aspetto, a meno che non si disponga di un hardware wallet da collegare e monitorare. Con questa impostazione, è possibile scansionare e collegare il proprio hardware wallet, come la carta Trezor o Cold, e monitorarne le attività. Si tratta di una funzione di sola osservazione, il che significa che non è possibile eseguire transazioni sull'hardware wallet da qui. È possibile solo osservare e monitorare le attività del wallet, i saldi, ecc.


**Impostazione del nodo ELECTRUM personalizzato:** Anche questo è un aspetto tecnico e, a meno che non siate abbastanza esperti, non dovreste preoccuparvene. L'impostazione predefinita è sufficiente.


**UNITA' DI BITCOIN:** Questo è il modo in cui si desidera che venga visualizzato il saldo Bitcoin. La prima opzione visualizza il saldo in termini Satoshi, ad esempio 1.000.000 Sats, mentre la seconda opzione lo visualizza in punti decimali BTC, ad esempio 0,01BTC


**Se si seleziona questa casella, si dovrà impostare un PIN o un'impronta digitale da inserire per accedere al wallet e autenticare le transazioni.


**Se si seleziona questa casella, le transazioni saranno instradate attraverso la rete Tor. Questo aggiunge un ulteriore livello di privacy, ma può causare un ritardo nei pagamenti, soprattutto per i pagamenti Lightning.


**VIEW BIP39 RECOVERY PHRASE:** Qui è possibile accedere alla frase di 12 parole seed per il backup. Se non l'avete scritta prima o non riuscite a trovare dove l'avete scritta, se avete ancora accesso al vostro Wallet, potete copiarla da qui.


**STATISTICHE DI UTILIZZO: ** mostra un riepilogo di tutte le transazioni e le attività effettuate dopo la creazione del wallet


![usage_stats](assets/en/041.webp)


## Recupero Wallet


Valet è un wallet non custodiale, quindi se si perde il dispositivo o si disinstalla l'app wallet, è necessario eseguire un recupero del wallet per recuperare i canali Bitcoin e Lightning. All'inizio di questa esercitazione, abbiamo menzionato l'importanza di annotare la **frase seed di 12 parole** perché è la chiave per recuperare il wallet. Non ci sono rappresentanti dell'assistenza clienti che possano aiutarvi a rientrare nel vostro wallet.


Per recuperare il proprio wallet Valet sono necessari due strumenti importanti, a seconda che l'utente avesse o meno un canale Lightning attivo. Per gli utenti che non avevano un normale canale Lightning attivo, tutto ciò di cui hanno bisogno è la loro frase seed di **12 parole**, seguendo i semplici passaggi riportati di seguito:


👉 Installare una nuova applicazione Valet e avviare l'applicazione.


👉 Selezionare **Ripristino del Wallet** esistente


![restore_existing_wallet](assets/en/042.webp)


👉 Selezionare **Solo frase di recupero**.


![select_recovery_phrase](assets/en/043.webp)


👉 Inserite la vostra frase di recupero di 12 parole e fate clic su **OK**.


![input_12_words](assets/en/044.webp)


Il wallet verrà recuperato. In questo caso, verrà ripristinato solo il saldo del on-chain Bitcoin.


Tuttavia, se avete un canale normale di Fulmine attivo e recuperate il vostro wallet solo con la frase di recupero, il vostro canale di Fulmine verrà chiuso forzatamente e l'eventuale saldo del Bitcoin verrà automaticamente inviato al vostro saldo del on-chain.


L'altro modo per recuperare il wallet di Valet, soprattutto se prima di disinstallare Valet era aperto un canale Lightning normale, è quello di **utilizzare il file di backup locale salvato sul dispositivo, insieme alla frase seed di 12 parole**. Se si utilizzano queste due parole, lo stato del canale Lightning verrà ripristinato e quindi il canale Lightning non verrà chiuso forzatamente.


Ecco i passaggi:


👉 Installare una nuova applicazione Valet e avviare l'applicazione.


👉 Selezionare **Ripristino del Wallet esistente**.


👉 Selezionate la frase **Backup + Recovery**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Selezionare il file di backup dal file manager del telefono. (Per impostazione predefinita è sempre memorizzato nella cartella **Downloads**)


![local_backup_file_in_download_folder](assets/en/046.webp)


Una volta selezionato il file di backup corretto, verrà visualizzato un messaggio di conferma della presenza di un **"file di backup "** e verrà richiesto di inserire la frase seed di 12 parole.


![enter_12_words](assets/en/047.webp)


👉 Immettere la frase di recupero di 12 parole e fare clic su **OK**. Verrà visualizzata la pagina iniziale del wallet.


👉 Attendere che la sincronizzazione della rete Bitcoin (**SYNC**) e la sincronizzazione del nodo Lightning (**LN Sync**) siano completate e il wallet sarà completamente ripristinato, compresi i canali Lightning.


![LN_sync](assets/en/048.webp)


## Conclusione


Valet è un'interessante soluzione wallet, con caratteristiche che la rendono adatta all'onboarding di nuovi utenti. Dispone inoltre di un canale Fiat, una tecnologia non nuova che garantisce l'integrazione delle aziende gestite con moneta unica sullo standard Bitcoin.


Scaricate Valet oggi stesso e provatelo!!! 🧡
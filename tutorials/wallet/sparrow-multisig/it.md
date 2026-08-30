---
name: Sparrow Wallet - Multisig
description: Creare un portafoglio multi-firma su Sparrow
---
![cover](assets/cover.webp)


Un portafoglio multi-firma (spesso chiamato "*Multisig*") è una struttura di portafoglio Bitcoin che richiede diverse firme crittografiche, provenienti da chiavi diverse, per autorizzare una spesa. A differenza di un portafoglio convenzionale ("*singlesig*"), in cui una sola chiave privata è sufficiente per sbloccare un UTXO, il Multisig si basa su un modello **m-di-n**: delle _n_ chiavi associate al portafoglio, _m_ devono imperativamente co-firmare ogni transazione.


Questo meccanismo consente di condividere il controllo di un portafoglio tra più entità o dispositivi. Ad esempio, in una configurazione 2-di-3, vengono generati tre set di chiavi indipendenti, ma ne bastano due per liberare i fondi. Questa architettura riduce drasticamente i rischi legati alla compromissione o alla perdita di una chiave: un ladro con accesso a una sola chiave non può svuotare il portafoglio, e un utente che ne perde una può comunque accedere ai propri fondi con le due rimanenti.


![Image](assets/fr/01.webp)


Tuttavia, questa maggiore sicurezza comporta una maggiore complessità. Configurare un portafoglio Multisig richiede di mettere in sicurezza diverse frasi Mnemonic (una per ogni fattore di firma) e chiavi pubbliche estese ("*xpub*"). Infatti, se usi un portafoglio Multisig 2-di-3, per recuperare il portafoglio devi avere tutte e tre le frasi Mnemonic, oppure almeno due delle tre. Ma se hai solo due delle tre frasi, ti serve anche l'accesso ai tre *xpub*, senza i quali sarà impossibile recuperare le chiavi pubbliche necessarie per accedere ai bitcoin che proteggono.


Per riassumere, per recuperare un portafoglio Multisig, devi:


- Accedere a tutte le frasi Mnemonic associate a ciascun fattore di firma;
- Oppure disporre del numero minimo di frasi Mnemonic richiesto dalla soglia per poter firmare, e avere anche accesso agli xpub di tutti i fattori per poter recuperare le chiavi pubbliche necessarie.


![Image](assets/fr/02.webp)


Questa gestione dei backup del portafoglio Multisig è facilitata dai *Descrittori di script di output*, che raggruppano tutti i dati pubblici necessari per accedere ai fondi. Tuttavia, questa funzionalità non è ancora implementata in tutti i software di gestione dei portafogli.


Il Multisig è particolarmente adatto ai bitcoiner che cercano una sicurezza rafforzata o una gestione collettiva dei fondi: aziende, associazioni, famiglie o singoli utenti che detengono una quantità significativa di bitcoin. Può essere usato per creare schemi di governance decentralizzata, ad esempio per distribuire l'autorità di firma tra più manager o membri di un team.


In questo tutorial impareremo a creare e usare un classico portafoglio multi-firma con **Sparrow Wallet**. Se vuoi creare un portafoglio multi-firma personalizzato con timelock, ti consiglio di usare invece Liana:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prerequisiti


Per questo tutorial, ti mostrerò come creare un Multisig con il [software di gestione dei portafogli Sparrow Wallet](https://sparrowwallet.com/download/). Se non hai ancora installato questo software, fallo adesso. Se hai bisogno di aiuto, abbiamo anche un tutorial dettagliato sulla configurazione di Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Per configurare un portafoglio multi-firma, ti servono diversi Hardware Wallet. Per un Multisig 2-di-3, ad esempio, potresti usare:


- Un Trezor Model One;
- Ledger Flex;
- Un Passport Core.


![Image](assets/fr/03.webp)


È buona norma usare marche diverse di Hardware Wallet nella tua configurazione Multisig. Questo garantisce che, se un modello specifico presenta un problema grave, ciò non comprometta la sicurezza complessiva del tuo Multisig. Inoltre, ti permette di beneficiare dei vantaggi specifici di ciascun dispositivo. Ad esempio, nella mia configurazione:



- Il Trezor Model One è completamente open-source, il che consente di verificare la generazione del seed. Tuttavia, non essendo dotato di un Secure Element, rimane vulnerabile agli attacchi fisici;



- Il Ledger Flex, invece, beneficia di un firmware proprietario non verificabile, ma integra un Secure Element che offre un'eccellente protezione fisica;



- Il Passport Core combina un firmware completamente open-source, un Secure Element e scambi air-gapped tramite codice QR. È un terzo firmatario indipendente in grado di verificare gli indirizzi e firmare PSBT senza connessione dati USB.


Prima di configurare il tuo portafoglio Multisig, assicurati che ogni Hardware Wallet sia configurato correttamente (generazione e salvataggio della frase Mnemonic, definizione del PIN). Per istruzioni dettagliate, puoi consultare i nostri tutorial per ogni Hardware Wallet, ad esempio:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Come vedremo più avanti in questo tutorial, è anche possibile integrare nella tua configurazione Multisig un fattore non associato a un Hardware Wallet, ma le cui chiavi private sono conservate sul tuo PC. Questo metodo è ovviamente meno sicuro dell'uso esclusivo di portafogli hardware, ma può essere rilevante in certi casi. Ad esempio, per un Multisig 2-di-3, potresti optare per due portafogli hardware e un Software Wallet.

> ⚠️ **Avviso di sicurezza Coldcard MK3:** non creare un nuovo seed su un MK3 con firmware precedente alla versione 4.2.0. I seed generati con firmware precedenti devono essere sostituiti e i fondi trasferiti. Questo tutorial usa quindi Passport Core come firmatario di riferimento air-gapped.


## Creare un portafoglio Multisig


Apri Sparrow Wallet, clicca sulla scheda "*File*", poi seleziona "*New Wallet*".


![Image](assets/fr/04.webp)


Assegna un nome al tuo portafoglio multi-firma, poi clicca su "*Create Wallet*" per confermare.


![Image](assets/fr/05.webp)


Nel menu a tendina "*Policy Type*", seleziona l'opzione "*Multi Signature*".


![Image](assets/fr/06.webp)


In alto a destra, puoi ora definire il numero totale di chiavi del tuo Multisig, così come il numero di co-firmatari richiesti per autorizzare una spesa. Nel mio esempio, si tratta di uno schema 2-di-3.


![Image](assets/fr/07.webp)


In fondo alla finestra, Sparrow Wallet mostra tre "*Keystore*". Ciascuno rappresenta un set di chiavi. Qui uso tre portafogli hardware, quindi ogni "*Keystore*" corrisponde a uno di essi. Ora li configureremo.


Inizio con il Passport Core. Nella scheda "*Keystore 1*", scelgo l'opzione "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Sul Passport, apri l'account che vuoi usare, poi seleziona "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Il Passport mostra un codice QR animato contenente le informazioni della sua chiave pubblica.

Su Sparrow, seleziona "*Scan...*" accanto a "*Passport*" e scansiona quel codice QR animato con la webcam del tuo computer. Controlla che l'impronta digitale della chiave master mostrata da Sparrow corrisponda a quella mostrata dal Passport, poi importa il keystore.

Il tuo xpub del Passport è ora stato importato. Ripeti la procedura appropriata per il Ledger Flex e il Trezor Model One.


Per il Ledger Flex, seleziono "*Keystore 2*", poi clicco su "*Connected Hardware Wallet*". Assicurati che il Ledger sia collegato al computer, sbloccato, e che l'applicazione Bitcoin sia aperta.


![Image](assets/fr/15.webp)


Poi clicca sul pulsante "*Scan...*".


![Image](assets/fr/16.webp)


Accanto al nome del tuo portafoglio hardware, clicca su "*Import Keystore*".


![Image](assets/fr/17.webp)


Il secondo firmatario è ora correttamente registrato in Sparrow Wallet.


![Image](assets/fr/18.webp)


Ripeto esattamente la stessa procedura con il Trezor One per finalizzare la configurazione del Multisig.


![Image](assets/fr/19.webp)


Nella mia configurazione non trattiamo questo caso, ma se vuoi includere una firma tramite un portafoglio software in Sparrow (hot wallet) all'interno del tuo Multisig, ti basta cliccare sul pulsante "*New or Imported Software Wallet*".


Ora che tutti i tuoi dispositivi di firma sono importati in Sparrow Wallet, puoi finalizzare la creazione del Multisig cliccando su "*Apply*".


![Image](assets/fr/20.webp)


Scegli una password robusta per proteggere l'accesso al tuo portafoglio Sparrow Wallet. Questa password protegge le tue chiavi pubbliche, indirizzi, etichette e cronologia delle transazioni da accessi non autorizzati.


Ricordati di salvare questa password in un luogo sicuro, come un gestore di password, per evitare di perderla.


![Image](assets/fr/21.webp)


## Eseguire il backup di un portafoglio Multisig


Ora salveremo il *Descrittore di script di output* su un supporto indipendente e ne conserveremo diverse copie.


Il *Descrittore* contiene tutti gli xpub del tuo portafoglio Multisig, così come i percorsi di derivazione usati per generare le chiavi. Ricorda quanto visto nella prima parte: per ripristinare un portafoglio Multisig, devi avere **tutte** le frasi Mnemonic, oppure solo il numero minimo richiesto per raggiungere la soglia di firma. Tuttavia, in quest'ultimo caso, è anche essenziale avere **gli xpub** dei firmatari mancanti. Il *Descrittore* contiene tutti gli xpub del tuo Multisig.


Se questo non è chiaro, ricorda semplicemente questo: per recuperare un Multisig, ti servono il numero minimo di frasi Mnemonic per ciascun Hardware Wallet usato, in base alla soglia (nel mio caso: 2 frasi), oltre al *Descrittore*.


Questo *Descrittore* non contiene chiavi private, solo pubbliche. Ciò significa che non dà accesso ai fondi. Non è quindi critico quanto le frasi Mnemonic, che danno pieno accesso ai tuoi bitcoin. Il rischio legato al *Descrittore* riguarda solo la riservatezza: in caso di compromissione, una terza parte potrebbe osservare tutte le tue transazioni, ma non potrebbe spendere i tuoi fondi.


Ti consiglio vivamente di creare diverse copie di questo *Descrittore*, e di conservarle insieme a ciascun dispositivo di firma del tuo Multisig. Ad esempio, nel mio caso, stampo il *Descrittore* su carta e conservo una copia con il Passport, un'altra con il Trezor e una con il Ledger. Salvo anche questo *Descrittore* come file PDF su tre chiavette USB, ciascuna conservata insieme a uno dei portafogli hardware. In questo modo, massimizzo le possibilità di non perdere mai questo *Descrittore*, e sono sicuro di avere due copie (una fisica e una digitale) con ciascun dispositivo.


Una volta creato il tuo portafoglio Multisig, Sparrow ti fornisce automaticamente questo *Descrittore*. Clicca sul pulsante "*Save PDF...*" per salvarlo sia come testo sia come codice QR.


![Image](assets/fr/22.webp)


Puoi poi stampare questo PDF e copiarlo sulle tue chiavette USB.


![Image](assets/fr/23.webp)


Il Passport usa la configurazione multisig importata da Sparrow per mostrare e verificare le informazioni sulle chiavi rilevanti durante il flusso di pairing e firma via QR. Conserva il *Descrittore* in modo indipendente: resta essenziale per recuperare il portafoglio se un firmatario non è disponibile.


Oltre a salvare il *Descrittore*, non dimenticare di prestare particolare attenzione al salvataggio delle frasi Mnemonic di ciascuno dei tuoi dispositivi di firma. Se sei alle prime armi, ti consiglio vivamente di consultare quest'altro tutorial per imparare a salvarle e gestirle correttamente:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Prima di ricevere i tuoi primi bitcoin sul tuo Multisig, **ti consiglio vivamente di eseguire un test di recupero a vuoto**. Annota alcune informazioni di riferimento, come il primo indirizzo di ricezione, poi resetta i tuoi portafogli hardware mentre il portafoglio è ancora vuoto. Successivamente, prova a ripristinare il tuo portafoglio Multisig sui portafogli hardware usando i backup cartacei delle tue frasi Mnemonic, poi su Sparrow usando il *Descrittore*. Controlla che il primo indirizzo generato dopo il ripristino corrisponda a quello che avevi originariamente annotato. Se è così, puoi stare tranquillo che i tuoi backup cartacei sono affidabili.


Per saperne di più su come eseguire un test di recupero, ti suggerisco di consultare quest'altro tutorial:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Ricevere bitcoin sul tuo Multisig


Il tuo portafoglio è ora pronto per ricevere bitcoin. In Sparrow, clicca sulla scheda "*Receive*".


![Image](assets/fr/30.webp)


Prima di usare l'indirizzo generato da Sparrow Wallet, prenditi il tempo di verificarlo direttamente sullo schermo dei tuoi portafogli hardware. Questo garantirà che l'indirizzo non sia stato alterato, e che i tuoi dispositivi possiedano le chiavi private necessarie per spendere i fondi associati. Questo ti aiuta a proteggerti da diversi vettori di attacco.


Per farlo, clicca su "*Display Address*" per mostrare l'indirizzo sul tuo Trezor o Ledger, quando collegati via cavo.


![Image](assets/fr/31.webp)


Con il Passport, seleziona l'account multisig e scegli "*Verify Address*". Scansiona il codice QR dell'indirizzo di ricezione mostrato da Sparrow. Il Passport conferma sul suo schermo se l'indirizzo appartiene al portafoglio multisig.


Controlla che l'indirizzo mostrato su ciascun portafoglio hardware corrisponda esattamente a quello in Sparrow Wallet. È consigliabile farlo appena prima di condividere l'indirizzo con chi effettua il pagamento, per essere sicuri della sua integrità.


Puoi poi assegnare un'"*Label*" a questo indirizzo, per indicare l'origine dei bitcoin ricevuti. È un buon modo per organizzare la gestione dei tuoi UTXO.


![Image](assets/fr/34.webp)


Una volta verificato questo, puoi usare l'indirizzo per ricevere bitcoin.


![Image](assets/fr/35.webp)


## Inviare bitcoin con il tuo Multisig


Ora che hai ricevuto i tuoi primi satoshi sul tuo portafoglio Multisig, puoi anche spenderli! In Sparrow, vai alla scheda "*Send*" per creare una nuova transazione.


![Image](assets/fr/36.webp)


Se desideri usare il *Coin Control*, cioè selezionare manualmente gli UTXO che vuoi spendere, vai alla scheda "*UTXOs*". Scegli gli UTXO che vuoi spendere, poi clicca su "*Send Selected*". Sarai automaticamente reindirizzato alla scheda "*Send*", con gli UTXO già precompilati.


![Image](assets/fr/37.webp)


Inserisci l'indirizzo di destinazione. È possibile aggiungere più indirizzi cliccando su "*+ Add*".


![Image](assets/fr/38.webp)


Aggiungi un'"*Label*" per descrivere lo scopo di questa spesa, per facilitare il tracciamento delle tue transazioni.


![Image](assets/fr/39.webp)


Inserisci l'importo da inviare all'indirizzo selezionato.


![Image](assets/fr/40.webp)


Regola la tariffa in base alle condizioni attuali della rete. Ad esempio, consulta [Mempool.space](https://Mempool.space/) per selezionare un livello di tariffa adeguato.


Dopo aver verificato tutti i parametri della transazione, clicca su "*Create Transaction*".


![Image](assets/fr/41.webp)


Se sei soddisfatto di tutto, clicca su "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


In fondo allo schermo, vedrai che Sparrow è in attesa di 2 firme. Questo è normale: il portafoglio usato qui è un Multisig 2-di-3.


![Image](assets/fr/43.webp)


Inizio a firmare con il mio Passport. In Sparrow, clicca su "*Show QR*" per mostrare la PSBT (*Partially Signed Bitcoin Transaction*) come codici QR animati. Sul Passport, seleziona l'account multisig e scegli "*Sign with QR Code*", poi scansiona il codice QR mostrato da Sparrow.


Sullo schermo del tuo Hardware Wallet, controlla attentamente i parametri della transazione: l'indirizzo del destinatario, l'importo inviato e le commissioni. Una volta confermata la transazione, convalida per procedere alla firma.


Dopo aver approvato la transazione, il Passport mostra la PSBT firmata come codici QR animati. In Sparrow, clicca su "*Scan QR*" e scansiona quei codici con la tua webcam. La firma del Passport viene quindi aggiunta. Ora uso il Ledger per la seconda firma richiesta: lo collego e lo sblocco, poi clicco su "*Sign*" in Sparrow.


![Image](assets/fr/48.webp)


Clicca su "*Sign*" accanto al nome del tuo Hardware Wallet.


![Image](assets/fr/49.webp)


La prima volta che usi il tuo Ledger con questo Multisig, Sparrow ti chiederà di verificare le chiavi pubbliche estese (xpub) dei co-firmatari. Come con il Passport, questo passaggio ti impedisce di firmare alla cieca più avanti. Per convalidare queste informazioni, confronta l'xpub mostrato sullo schermo del Ledger con quelli forniti direttamente dai tuoi altri portafogli hardware.


![Image](assets/fr/50.webp)


Controlla l'indirizzo del destinatario, l'importo trasferito e la commissione di transazione, poi firma la transazione.


![Image](assets/fr/51.webp)


Premi lo schermo per firmare.


![Image](assets/fr/52.webp)


Sparrow ora dispone delle due firme necessarie per liberare i fondi dal portafoglio Multisig. Controlla la transazione un'ultima volta e, se tutto va bene, clicca su "*Broadcast Transaction*" per trasmetterla sulla rete.


![Image](assets/fr/53.webp)


Troverai questa transazione nella scheda "*Transactions*" di Sparrow Wallet.


![Image](assets/fr/54.webp)


Complimenti, ora sai come configurare e usare un portafoglio multi-firma su Sparrow. Se questo tutorial ti è stato utile, ti sarei grato se lasciassi un pollice verde qui sotto. Sentiti libero di condividere questo articolo sui tuoi social network. Grazie per la condivisione!


Per approfondire, ti consiglio di consultare questo tutorial su un altro metodo per aumentare la sicurezza del tuo portafoglio Bitcoin, la passphrase BIP39:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
</content>

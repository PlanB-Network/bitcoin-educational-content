---
name: BIP47 - PayNym

description: Come funzionano i PayNym
---
***ATTENZIONE:** In seguito all'arresto dei fondatori di Samourai Wallet e al sequestro dei loro server il 24 aprile, l'applicazione non può più essere utilizzata dagli utenti che non dispongono del proprio Dojo. BIP47 rimane utilizzabile su Sparrow Wallet per tutti gli utenti e **su Samourai Wallet solo per gli utenti che dispongono di un Dojo**.*

_Stiamo seguendo da vicino l'evoluzione di questo caso così come gli sviluppi relativi agli strumenti associati. Siate certi che aggiorneremo questo tutorial non appena saranno disponibili nuove informazioni._

_Questo tutorial è fornito solo a scopo educativo e informativo. Non approviamo né incoraggiamo l'uso di questi strumenti per scopi criminali. È responsabilità di ogni utente rispettare le leggi vigenti nella propria giurisdizione._

---

> "È troppo grande", dicevano tutti, e il tacchino che era nato con gli speroni e si credeva un imperatore, si gonfiò come una nave a tutto vapore e si avvicinò a lui furioso e rosso fino agli occhi. Il povero anatroccolo non sapeva se fermarsi o continuare a camminare: era molto triste di essere deriso da tutti gli anatroccoli della corte.

![BIP47, il brutto anatroccolo illustrazione](assets/1.webp)

Uno dei problemi più importanti nel protocollo Bitcoin è il riutilizzo degli indirizzi. La trasparenza e la distribuzione della rete rendono questa pratica pericolosa per la privacy dell'utente. Per evitare problemi legati a questo, si consiglia di utilizzare un nuovo indirizzo di ricezione per ogni nuovo pagamento in entrata verso un portafoglio, il che può essere complicato in alcuni casi.

Questo compromesso è vecchio come il White Paper. Satoshi ci ha avvertito di questo rischio nel suo lavoro pubblicato alla fine del 2008:

> "Come ulteriore misura di sicurezza, una nuova coppia di chiavi potrebbe essere utilizzata per ogni transazione per mantenerle non collegate a un proprietario comune."

Esistono molte soluzioni per ricevere pagamenti multipli senza riutilizzare gli indirizzi. Ognuna di esse ha i suoi compromessi e svantaggi. Tra tutte queste soluzioni c'è [BIP47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki), una proposta sviluppata da Justus Ranvier e pubblicata nel 2015 che consente di generare codici di pagamento riutilizzabili. Il loro obiettivo è quello di poter effettuare più transazioni verso la stessa persona senza riutilizzare gli indirizzi.

Inizialmente, questa proposta è stata accolta con disprezzo da parte di una parte della comunità e non è mai stata aggiunta a Bitcoin Core. Tuttavia, alcuni software hanno scelto di implementarla comunque. Ad esempio, Samourai Wallet ha sviluppato la propria implementazione di BIP47: PayNym. Oggi, questa implementazione è ovviamente disponibile su Samourai Wallet per smartphone, ma anche su [Sparrow Wallet](https://sparrowwallet.com/) per Desktop.

Nel tempo, Samourai ha programmato nuove funzionalità direttamente legate a PayNym. Ora esiste un intero ecosistema di strumenti per ottimizzare la privacy dell'utente basati su PayNym e BIP47.
In questo articolo, scoprirai il principio di BIP47 e PayNym, i meccanismi di questi protocolli e le applicazioni pratiche che ne derivano. Affronterò solo la prima versione di BIP47, quella attualmente utilizzata per PayNym, ma le versioni 2, 3 e 4 funzionano praticamente allo stesso modo.

> L'unica differenza principale si trova nel livello di notifica della transazione. La versione 1 utilizza un indirizzo semplice con OP_RETURN per la notifica, la versione 2 utilizza uno script multisig (bloom-multisig) con OP_RETURN e la versione 3 e 4 utilizzano semplicemente uno script multisig (cfilter-multisig). I meccanismi menzionati in questo articolo, in particolare i metodi crittografici studiati, sono quindi applicabili alle quattro versioni. Attualmente, l'implementazione di PayNym su Samourai Wallet e Sparrow utilizza la prima versione di BIP47.

## Sommario:

1- Il problema del riutilizzo dell'indirizzo.

2- Principi di BIP47 e PayNym.

3- Tutorial: utilizzo di PayNym.

- Costruire una transazione BIP47 con Samourai Wallet.

- Costruire una transazione BIP47 con Sparrow Wallet.

4- I meccanismi di BIP47.

- Il codice di pagamento riutilizzabile.
- Il metodo crittografico: lo scambio di chiavi Diffie-Hellman stabilito sulle curve ellittiche (ECDH).

- La transazione di notifica.
- Costruzione della transazione di notifica.
- Ricezione della transazione di notifica.
- La transazione di pagamento BIP47.
- Ricezione del pagamento BIP47 e derivazione della chiave privata.
- Rimborso del pagamento BIP47.

5- Utilizzi derivati di PayNym.

6- La mia opinione personale su BIP47.

## Il problema del riutilizzo dell'indirizzo.

Un indirizzo di ricezione viene utilizzato per ricevere bitcoin. Viene generato a partire da una chiave pubblica, calcolato l'hash di essa e applicando un formato specifico. In questo modo, viene creata una nuova condizione di spesa su un UTXO per modificarne il proprietario.

> Per saperne di più sulla generazione di un indirizzo di ricezione, ti consiglio di leggere l'ultima parte di questo articolo: Il portafoglio Bitcoin - estratto [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).

Inoltre, avrai sicuramente sentito da un esperto di bitcoin che gli indirizzi di ricezione sono ad uso unico e che è necessario generarne uno nuovo per ogni nuovo pagamento in entrata verso il tuo portafoglio. Ma perché?
Fondamentalmente, il riutilizzo degli indirizzi non mette direttamente a rischio i tuoi fondi. L'utilizzo della crittografia sulle curve ellittiche consente di dimostrare alla rete di essere in possesso di una chiave privata senza rivelarla. Puoi quindi bloccare diversi UTXO su uno stesso indirizzo e spenderli in momenti diversi. Se non riveli la chiave privata associata a quell'indirizzo, nessuno potrà accedere ai tuoi fondi. Il problema della riutilizzazione degli indirizzi riguarda piuttosto la privacy.

Come accennato in precedenza, la trasparenza e la distribuzione della rete Bitcoin fanno sì che qualsiasi utente, purché abbia accesso ad un nodo, sia in grado di osservare tutte le transazioni. Di conseguenza, può vedere i saldi di tutti gli indirizzi a lui noti. Satoshi Nakamoto ha quindi menzionato la possibilità di generare nuove coppie di chiavi e quindi nuovi indirizzi per ogni nuovo pagamento in entrata verso un portafoglio. L'obiettivo sarebbe quello di avere un ulteriore livello di protezione nel caso in cui si associ l'identità dell'utente a una delle sue coppie di chiavi.

Oggi, con la presenza di società di analisi della blockchain e lo sviluppo del KYC, l'utilizzo di indirizzi nuovi non è più un ulteriore livello di protezione, ma un obbligo per chiunque si preoccupi anche solo minimamente della propria privacy.

La ricerca ed il mantenimento della privacy non sono solo un lusso o una fantasia dei bitcoiner massimalisti. Rappresentano parametri specifici che riguardano direttamente la tua sicurezza personale e la protezione dei tuoi fondi. Per farti capire meglio, ecco un esempio molto concreto:

- Bob compra bitcoin in DCA (Dollars Cost Average), cioè acquista una piccola quantità di bitcoin a intervalli regolari per ammortizzare il prezzo di ingresso. Bob invia sistematicamente i fondi acquistati allo stesso indirizzo di ricezione. Acquista 0,01 bitcoin ogni settimana e li invia a questo stesso indirizzo. Dopo due anni, Bob ha accumulato un intero bitcoin su questo indirizzo.

- Il panettiere nella sua strada accetta pagamenti in bitcoin. Felice di poter spendere bitcoin, Bob va a comprare la sua baguette in satoshi. Per pagare, utilizza i fondi bloccati con il suo indirizzo. Il suo panettiere ora sa che possiede un bitcoin. Questa somma importante potrebbe suscitare invidia e Bob potrebbe potenzialmente subire un attacco fisico in seguito.

È per questo motivo che la maggior parte dei software di portafoglio Bitcoin genera automaticamente un nuovo indirizzo di ricezione quando si fa clic sul pulsante "Ricevi". Per l'utente normale, l'abitudine di utilizzare indirizzi vuoti non è quindi un grande inconveniente. Tuttavia, per un'attività online, una exchange o una campagna di donazione, questo vincolo può diventare rapidamente ingestibile.
Esistono molte soluzioni per queste organizzazioni. Ognuna di esse ha i suoi vantaggi e svantaggi, ma fino ad oggi, come vedremo più avanti, il BIP47 si differenzia davvero dagli altri.

Questo problema del riutilizzo degli indirizzi è tutt'altro che trascurabile su Bitcoin. Come si può vedere dal grafico tratto dal sito oxt.me, il tasso globale di riutilizzo degli indirizzi da parte degli utenti di Bitcoin è attualmente del 52%:
Grafico OXT.me sull'evoluzione del tasso globale di riutilizzo degli indirizzi nella rete Bitcoin.

![image](assets/2.webp)

Crediti: OXT

La maggior parte di questi riutilizzi proviene dagli exchange che, per motivi di efficienza e facilità, riutilizzano lo stesso indirizzo molte volte. Fino ad oggi, il BIP47 rappresenterebbe la migliore soluzione per arginare questo fenomeno negli exchange. Ciò consentirebbe di ridurre il tasso globale di riutilizzo degli indirizzi, senza causare troppi attriti a queste entità.

Questa misura globale sull'intera rete è un dato particolarmente coerente in questo caso. Infatti, il riutilizzo degli indirizzi non è solo un problema per la persona che pratica questo tipo di pratica, ma anche per chiunque effettui transazioni con essa. La perdita di privacy su Bitcoin agisce come un virus e si diffonde da utente a utente. Studiare una misura globale su tutte le transazioni della rete ci consente di prendere coscienza dell'entità di questo fenomeno.

## Principi di BIP47 e PayNym.

BIP47 mira a offrire un modo semplice per ricevere numerosi pagamenti senza riutilizzare gli indirizzi. Il suo funzionamento si basa sull'uso di un codice di pagamento riutilizzabile.

In questo modo, più mittenti possono inviare più pagamenti ad un unico codice di pagamento riutilizzabile di un altro utente, senza che il destinatario debba fornire un nuovo indirizzo vuoto per ogni nuova transazione.

Un utente può quindi comunicare liberamente il suo codice di pagamento (su social media, sul suo sito web...) senza rischi di perdita di privacy, a differenza di un indirizzo di ricezione tradizionale o di una chiave pubblica.
Per effettuare uno scambio, entrambi gli utenti devono avere un portafoglio Bitcoin con un'implementazione del BIP47, come PayNym su Samourai Wallet o Sparrow Wallet. L'associazione dei codici di pagamento dei due utenti permetterà di stabilire un canale segreto tra di loro. Per stabilire correttamente questo canale, l'emittente dovrà effettuare una transazione sulla blockchain di Bitcoin: la transazione di notifica (ne parlerò un po' più avanti).
L'associazione dei codici di pagamento dei due utenti genera segreti condivisi che a loro volta generano un gran numero di indirizzi di ricezione Bitcoin unici (esattamente 2^32). Quindi, in realtà, il pagamento con BIP47 non viene inviato al codice di pagamento, ma agli indirizzi di ricezione Bitcoin del tutto normali, derivati dai codici di pagamento dei protagonisti.

Il codice di pagamento agisce quindi come un identificatore virtuale, derivato dal seed del portafoglio. Nella struttura di derivazione del portafoglio HD, il codice di pagamento si trova a profondità 3, al livello dei conti del portafoglio.

Il suo scopo di derivazione è indicato come 47' (0x8000002F) in riferimento al BIP47. Un percorso di derivazione per un codice di pagamento riutilizzabile potrebbe essere ad esempio:

> m/47'/0'/0'/

Per darvi un'idea di come sia un codice di pagamento, ecco il mio:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Questo può anche essere codificato in un QR code per facilitarne la comunicazione:

![image](assets/4.webp)

Per quanto riguarda i PayNym Bots, questi robot che si vedono su Twitter sono semplicemente rappresentazioni visive del vostro codice di pagamento, realizzate da Samourai Wallet. Sono creati utilizzando una funzione di hash, il che li rende quasi unici. Ecco il mio con il suo identificatore:

> +throbbingpond8B1

![image](assets/5.webp)

Questi Bots non hanno una vera utilità tecnica. Invece, facilitano le interazioni tra gli utenti creando un'identità visiva virtuale.

Per l'utente, il processo di pagamento BIP47 con l'implementazione di PayNym è estremamente semplice. Immaginiamo che Alice voglia inviare pagamenti a Bob:

1. Bob diffonde il suo QR code, o direttamente il suo codice di pagamento riutilizzabile. Può metterlo sul suo sito web, sui suoi vari social media pubblici o inviarlo ad Alice tramite un altro mezzo di comunicazione.
2. Alice apre Samourai o Sparrow e scansiona o incolla il codice di pagamento di Bob.
3. Alice segue il PayNym di Bob ("Follow" in inglese). Questa operazione avviene al di fuori della blockchain e rimane completamente gratuita.

4. Alice collega il suo PayNym a quello di Bob ("Connect" in inglese). Questa operazione avviene "on chain". Alice deve pagare le commissioni di mining della transazione e una commissione fissa di 15.000 sats per il servizio su Samourai. Le commissioni di servizio sono offerte su Sparrow. Questo passaggio è ciò che viene chiamata la transazione di notifica.

5. Una volta confermata la transazione di notifica, Alice può creare una transazione di pagamento BIP47 verso Bob. Il suo portafoglio genererà automaticamente un nuovo indirizzo di ricezione vuoto per il quale solo Bob ha la chiave privata.

Effettuare la transazione di notifica, cioè collegare il proprio PayNym, è un passaggio preliminare obbligatorio per effettuare pagamenti BIP47. Tuttavia, una volta completato questo passaggio, il mittente potrà effettuare molteplici pagamenti al destinatario (esattamente 2^32), senza dover effettuare nuovamente una transazione di notifica.

Avrete potuto notare che ci sono due operazioni diverse che consentono di collegare i PayNym tra loro: seguire e connettere. Seguire ("follow") corrisponde alla transazione di notifica del BIP47 che è semplicemente una transazione Bitcoin con alcune informazioni trasmesse tramite un output OP_RETURN. In questo modo, aiuta a stabilire una comunicazione crittografata tra i due utenti al fine di produrre i segreti condivisi necessari per generare nuovi indirizzi di ricezione vuoti.

D'altra parte, l'operazione di collegamento ("Connect") consente di stabilire un collegamento su Soroban, un protocollo di comunicazione crittografato basato su Tor, sviluppato appositamente dal team di Samourai.

Per riassumere:

- Il collegamento di due PayNym ("follow") è completamente gratuito. Questo aiuta a stabilire comunicazioni crittografate "off chain", in particolare per utilizzare gli strumenti di transazioni collaborative di Samourai (Stowaway o StonewallX2). Questa operazione è specifica di PayNym. Non è descritta nel BIP47.

- La connessione ("Conncect") di due PayNym è a pagamento. Questo implica l'esecuzione della transazione di notifica al fine di avviare la connessione. Il costo è costituito da eventuali commissioni di servizio, commissioni di mining della transazione e 546 sats inviati all'indirizzo di notifica del destinatario per avvisarlo dell'apertura del tunnel. Questa operazione è legata al BIP47. Una volta completata, il mittente può effettuare più pagamenti BIP47 al destinatario.

Per poter connettere due PayNym, devono già essere collegati.

## Tutorial: utilizzo di PayNym.

Ora che abbiamo visto la teoria, esaminiamo insieme la pratica. L'idea dei tutorial qui di seguito è quella di collegare il mio PayNym sul mio portafoglio Sparrow con il mio PayNym sul mio portafoglio Samourai. Il primo tutorial ti mostra come effettuare una transazione utilizzando il codice di pagamento riutilizzabile da Samourai a Sparrow, mentre il secondo tutorial descrive lo stesso meccanismo da Sparrow a Samourai.

> Ho eseguito questi tutorial su Testnet. Non si tratta di veri bitcoin.

### Costruire una transazione BIP47 con Samourai Wallet.

Per iniziare, ovviamente avrai bisogno dell'applicazione Samourai Wallet. Puoi scaricarla direttamente dal Google Play Store o con il file APK disponibile sul sito ufficiale di Samourai, in quest'ultimo caso assicurati di verificare la firma dello sviluppatore e l'integrità del software scaricato prima di installarlo sul tuo telefono.


Una volta che il portafoglio è stato inizializzato, se non l'hai già fatto, richiedi il tuo PayNym facendo clic sul segno più (+) in basso a destra, quindi su "PayNym".

Il primo passo per effettuare un pagamento BIP47 sarà quello di ottenere il codice di pagamento riutilizzabile del nostro destinatario. Successivamente, potremo collegarci a lui e successivamente connetterci:

![video](assets/6.mp4)

Una volta confermata la transazione di notifica, posso inviare più pagamenti al mio destinatario. Ogni transazione verrà automaticamente effettuata con un nuovo indirizzo vuoto per il quale il destinatario possiede le chiavi. Quest'ultimo non deve compiere alcuna azione, tutto viene calcolato dal mio lato.

Ecco come effettuare una transazione BIP47 su Samourai Wallet:

![video](assets/7.mp4)

### Costruire una transazione BIP47 con Sparrow Wallet.

Allo stesso modo di Samourai, ovviamente devi avere il software Sparrow. Questo è disponibile per computer. Puoi scaricarlo dal [sito web ufficiale](https://sparrowwallet.com/).

Assicurati di verificare la firma dello sviluppatore e l'integrità del software scaricato prima di installarlo sul tuo computer.

Crea un portafoglio e richiedi il tuo PayNym facendo clic su "Show PayNym" dal menu "Tool" nella barra superiore:

![image](assets/8.webp)

Successivamente, dovrai collegare e connettere il tuo PayNym con quello del tuo destinatario. Per farlo, inserisci il suo codice di pagamento riutilizzabile nella finestra "Find Contact", segui il percorso e quindi effettua la transazione di notifica facendo clic su "Link Contact":

![image](assets/9.webp)

Una volta confermata la transazione di notifica, è possibile inviare pagamenti al codice di pagamento riutilizzabile. Ecco come procedere:

![video](assets/10.mp4)

Ora che abbiamo esaminato l'aspetto pratico dell'implementazione PayNym di BIP47, vediamo insieme come funzionano tutti questi meccanismi e quali sono i metodi crittografici utilizzati.

## I meccanismi di BIP47.

Per studiare i meccanismi del BIP47, è essenziale comprendere la struttura del portafoglio deterministico gerarchico (HD), i meccanismi di derivazione delle coppie di chiavi figlie ed i principi della crittografia sulle curve ellittiche. Fortunatamente, puoi trovare tutte queste informazioni necessarie per comprendere questa parte sul mio blog:

- [Comprendere i percorsi di derivazione di un portafoglio Bitcoin](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-bitcoin)

- [Il portafoglio Bitcoin - estratto dall'ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2)

### Il codice di pagamento riutilizzabile.

Come spiegato nella seconda parte di questo documento, il codice di pagamento riutilizzabile si trova a una profondità di tre nel portafoglio HD. È in qualche modo assimilabile ad un xpub, sia per la sua posizione e struttura che per il suo ruolo.

Ecco le diverse parti che compongono un codice di pagamento di 80 byte:

- Byte 0: La versione. Se si utilizza la prima versione del BIP47, questo byte sarà uguale a 0x01.

- Byte 1: Il campo dei bit. Questo spazio è riservato per fornire indicazioni aggiuntive in caso di utilizzo specifico. Se si utilizza semplicemente PayNym, questo byte sarà uguale a 0x00.

- Byte 2: La parità di y. Questo byte indica 0x02 o 0x03 a seconda della parità (numero pari o numero dispari) del valore dell'ordinata della nostra chiave pubblica. Per ulteriori informazioni su questa pratica, si prega di leggere il passaggio 1 della sezione "derivazione di un indirizzo" di questo articolo.

- Dai byte 3 al byte 34: Il valore di x. Questi byte indicano l'ascissa della nostra chiave pubblica. La concatenazione di x e della parità di y ci dà la nostra chiave pubblica compressa.

- Dai byte 35 al byte 66: Il codice di catena. Questo spazio è riservato per il codice di catena associato alla chiave pubblica sopra menzionata.

- Dai byte 67 al byte 79: Il padding. Questo spazio è riservato a possibili future evoluzioni. Per la versione 1, vengono semplicemente inseriti zeri per riempire fino a 80 byte, che è la dimensione dei dati di un'uscita OP_RETURN.

Ecco la rappresentazione esadecimale del mio codice di pagamento riutilizzabile, mostrato precedentemente, con i colori corrispondenti ai byte sopra presentati:
Successivamente, è necessario aggiungere l'ottetto del prefisso "P" che permette di identificare immediatamente che si tratta di un codice di pagamento. Questo ottetto è 0x47.

> 0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000

Infine, calcoliamo il checksum di questo codice di pagamento con HASH256, ovvero un doppio hash con la funzione SHA256. Prendiamo i primi quattro ottetti di questo condensato e li concateniamo alla fine (in rosa).

> 0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000567080c4

Il codice di pagamento è pronto, non resta che convertirlo in Base 58:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Come si può notare, questa costruzione assomiglia molto alla struttura di una chiave pubblica estesa di tipo "xpub".

Durante questo processo che porta al nostro codice di pagamento, abbiamo utilizzato una chiave pubblica compressa e un codice di catena ("Chain Code"). Questi due elementi sono il risultato di una derivazione deterministica e gerarchica, dalla radice del portafoglio, seguendo il percorso di derivazione seguente: m/47'/0'/0'/
Concretamente, per ottenere la chiave pubblica e il codice di catena del codice di pagamento riutilizzabile, calcoleremo la chiave privata principale del seed, quindi deriviamo una coppia figlia con l'indice 47 + 2^31 (derivazione rinforzata). Successivamente, deriviamo due coppie figlie con l'indice 2^31 (derivazione rinforzata).

> Se desideri saperne di più sulla derivazione di coppie di chiavi figlie all'interno di un portafoglio deterministico gerarchico Bitcoin, ti consiglio di seguire CRYPTO301.

### Il metodo crittografico: lo scambio di chiavi Diffie-Hellman basato sulle curve ellittiche (ECDH).

Il metodo crittografico utilizzato come base per il BIP47 è l'ECDH (Elliptic-Curve Diffie-Hellman = Scambio di chiavi Diffie-Hellman basato sulle curve ellittiche). Questo protocollo è una variante dello scambio di chiavi Diffie-Hellman classico.

Diffie-Hellman, nella sua prima versione, è un protocollo di accordo sulle chiavi presentato nel 1976 che consente a due persone, utilizzando due coppie di chiavi (chiavi pubbliche e chiavi private), di determinare un segreto condiviso scambiandosi su un canale di comunicazione non sicuro.

![image](assets/11.webp)

Questo segreto condiviso (la chiave rossa) può quindi essere utilizzato per eseguire altre operazioni. Tipicamente, questo segreto condiviso può essere utilizzato per crittografare e decrittografare una comunicazione su una rete non sicura:

![image](assets/12.webp)

Per riuscire in questo scambio, Diffie-Hellman utilizza l'aritmetica modulare per calcolare il segreto comune. Ecco come funziona in modo semplificato:

- Alice e Bob scelgono un colore comune, in questo caso il giallo. Questo colore è noto a tutti. È un dato pubblico.

- Alice sceglie un colore segreto, in questo caso il rosso. Mescola i due colori ottenendo l'arancione.

- Bob sceglie un colore segreto, in questo caso il blu petrolio. Mescola i due colori ottenendo il celeste.

- Alice e Bob possono scambiarsi i colori ottenuti: l'arancione e il celeste. Questo scambio può avvenire su una rete non sicura e può essere osservato da attaccanti.

- Alice mescola il colore celeste ricevuto da Bob con il suo colore segreto (rosso). Ottiene il marrone.

- Bob mescola il colore arancione ricevuto da Alice con il suo colore segreto (blu petrolio). Ottiene lo stesso colore marrone.

![image](assets/13.webp)

> Credito: Idea originale: A.J. Han Vinck Versione vettoriale: Flugaal Traduzione: Dereckson, Public domain, via Wikimedia Commons. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg

In questa semplificazione, il colore marrone rappresenta il segreto condiviso tra Alice e Bob. Bisogna immaginare che in realtà sia impossibile per l'attaccante separare i colori arancione e celeste, al fine di scoprire i segreti di Alice o Bob.

Ora, studiamo il suo funzionamento reale. A prima vista, Diffie-Hellman sembra complesso da comprendere. In realtà, il principio di funzionamento è quasi elementare. Prima di dettagliare i suoi meccanismi, vi ricordo brevemente due concetti matematici di cui avremo bisogno (e che, incidentalmente, sono anche utilizzati in numerosi altri metodi crittografici).

1. Un numero primo è un numero naturale che ha solo due divisori: 1 e se stesso. Ad esempio, il numero 7 è primo, perché può essere diviso solo per 1 e 7 (se stesso). Al contrario, il numero 8 non è primo, perché può essere diviso per 1, 2, 4 e 8. Quindi non ha solo due divisori, ma quattro divisori interi e positivi.

2. Il "modulo" (indicato come "mod" o "%") è un'operazione matematica che consente di restituire il resto della divisione euclidea del primo numero per il secondo numero. Ad esempio, 16 mod 5 è uguale a 1.

Lo scambio di chiavi Diffie-Hellman tra Alice e Bob funziona nel seguente modo:

- Alice e Bob scelgono due numeri comuni: p e g. p è un numero primo. Più grande è questo numero p, più sicuro sarà Diffie-Hellman. g è una radice primitiva di p. Questi due numeri possono essere comunicati in chiaro su una rete non sicura, sono equivalenti al colore giallo nella semplificazione sopra. Alice e Bob devono semplicemente avere gli stessi valori di p e g.

- Una volta scelti i parametri, Alice e Bob determinano ciascuno un numero casuale segreto. Il numero casuale ottenuto da Alice è chiamato *a* (equivalente al colore rosso) e il numero casuale ottenuto da Bob è chiamato *b* (equivalente al colore blu petrolio). Questi due numeri devono rimanere segreti.

- Invece di scambiare questi numeri a e b, ogni parte calcolerà A (maiuscolo) e B (maiuscolo) come segue:

> A è uguale a g elevato alla potenza a modulo p:
> A = g^a % p

> B è uguale a g elevato alla potenza b modulo p:
> B = g^b % p

- Questi numeri A (equivalente al colore arancione) e B (equivalente al colore celeste) saranno scambiati tra le due parti. Lo scambio può avvenire in chiaro su una rete non sicura.

- Alice, che ora conosce B, calcolerà il valore di z come segue:

> z è uguale a B elevato alla potenza a modulo p:
> z = B^a % p

- Come ricordo, B = g^b % p. Quindi abbiamo:

  > z = B^a % p
  > z = (g^b)^a % p
  >
  > In conformità alle regole di calcolo delle potenze:
  >
  > (x^n)^m = x^nm
  >
  > Quindi abbiamo:
  >
  > z = g^ba % p

- Bob, che ora conosce A, calcolerà anche il valore di z come segue:

> z è uguale ad A elevato alla b modulo p:
>
> z = A^b % p
>
> Quindi abbiamo:
>
> z = (g^a)^b % p
> z = g^ab % p
> z = g^ba % p

Grazie alla distributività dell'operatore modulo, Alice e Bob trovano esattamente lo stesso valore di z. Questo numero rappresenta il loro segreto comune, cioè l'equivalente del colore marrone nella spiegazione precedente. Possono utilizzare questo segreto comune per crittografare una comunicazione tra di loro su una rete non sicura.

![Schema del funzionamento tecnico di Diffie-Hellman](assets/14.webp)

Un attaccante in possesso di p, g, A e B sarà impossibilitato a calcolare a, b o z. Effettuare questa operazione significherebbe invertire l'esponenziazione. Questo calcolo è impossibile da eseguire se non provando tutte le combinazioni una per una, poiché si sta lavorando su un campo finito. Ciò equivale a calcolare il logaritmo discreto, cioè l'inverso dell'esponenziale in un gruppo ciclico finito.

Pertanto, fintanto che si scelgono a, b e p sufficientemente grandi, Diffie-Hellman è sicuro. Tipicamente, con parametri di 2.048 bit (un numero di 600 cifre in decimale), testare tutte le possibilità per a e b sarebbe una chimera. Ad oggi, con numeri di questa dimensione, l'algoritmo è considerato sicuro.

È proprio a questo livello che risiede il principale svantaggio del protocollo Diffie-Hellman. Per essere sicuro, l'algoritmo deve utilizzare numeri di grandi dimensioni. Di conseguenza, oggi si preferisce utilizzare l'algoritmo ECDH, una variante di Diffie-Hellman che utilizza una curva algebrica, e in particolare una curva ellittica. Ciò ci consente di lavorare con numeri molto più piccoli pur mantenendo una sicurezza equivalente, riducendo così le risorse necessarie per il calcolo e lo storage.

Il principio generale dell'algoritmo rimane lo stesso. Ma invece di utilizzare un numero casuale *a* e un numero A calcolato da *a* con l'esponenziazione modulare, utilizzeremo una coppia di chiavi stabilite su una curva ellittica. Invece di fare affidamento sulla distributività dell'operatore modulo, qui utilizzeremo la legge di gruppo sulle curve ellittiche, e più precisamente la proprietà associativa di questa legge.
Se non hai alcuna conoscenza sul funzionamento delle chiavi private e pubbliche su una curva ellittica, spiegherò le basi di questo metodo nelle prime sei parti di questo articolo.

In breve, una chiave privata è un numero casuale compreso tra 1 e n-1 (dove n è l'ordine della curva), e una chiave pubblica è un punto unico sulla curva determinato dalla chiave privata tramite l'addizione e il raddoppio di punti dal punto generatore come segue:

> K = k·G

Dove K è la chiave pubblica, k è la chiave privata e G è il punto generatore.

Una delle proprietà di questa coppia di chiavi è che è molto facile determinare K conoscendo k e G, ma è attualmente impossibile determinare k conoscendo K e G. È una funzione unidirezionale.

In altre parole, è possibile calcolare facilmente la chiave pubblica conoscendo la chiave privata, ma è impossibile calcolare la chiave privata conoscendo la chiave pubblica. Questa sicurezza si basa ancora una volta sull'impossibilità di calcolare il logaritmo discreto.

Quindi useremo questa proprietà per adattare il nostro algoritmo Diffie-Hellman. Pertanto, il principio di funzionamento di ECDH è il seguente:

- Alice e Bob concordano insieme su una curva ellittica crittograficamente sicura e sui suoi parametri. Queste informazioni sono pubbliche.

- Alice genera un numero casuale ka che sarà la sua chiave privata. Questa chiave privata deve rimanere segreta. Determina la sua chiave pubblica Ka tramite l'addizione e il raddoppio di punti sulla curva ellittica scelta.

> Ka = ka·G

- Bob genera anche un numero casuale che sarà la sua chiave privata kb. E calcola la chiave pubblica associata Kb.

> Kb = kb·G

- Alice e Bob scambiano le loro chiavi pubbliche Ka e Kb su una rete pubblica non sicura.

- Alice calcola un punto (x,y) sulla curva applicando la sua chiave privata ka dalla chiave pubblica di Bob Kb.

> (x,y) = ka·Kb

- Bob calcola un punto (x,y) sulla curva applicando la sua chiave privata kb dalla chiave pubblica di Alice Ka.

> (x,y) = kb·Ka

- Alice e Bob ottengono lo stesso punto sulla curva ellittica. Il segreto condiviso sarà l'ascissa x di questo punto.

Ottengono lo stesso segreto condiviso perché:

> (x,y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka

Un potenziale attaccante che osserva la rete pubblica non sicura può ottenere solo le chiavi pubbliche di entrambi e i parametri della curva scelta. Come spiegato in precedenza, queste due informazioni da sole non consentono di determinare le chiavi private e quindi l'attaccante non può accedere al segreto.
ECDH è quindi un algoritmo che consente lo scambio di chiavi. Spesso viene utilizzato insieme ad altri metodi crittografici per definire un protocollo. Ad esempio, ECDH è utilizzato nel cuore di TLS (Transport Layer Security), un protocollo di crittografia ed autenticazione utilizzato per il livello di trasporto di Internet. TLS utilizza ECDHE per lo scambio di chiavi, una variante di ECDH in cui le chiavi sono effimere per garantire la riservatezza persistente. Oltre a quest'ultimo, TLS utilizza anche un algoritmo di autenticazione come ECDSA, un algoritmo di crittografia come AES e una funzione di hash come SHA256.
TLS definisce in particolare la "s" in "https", così come il lucchetto che si vede nel browser in alto a sinistra, i quali garantiscono la crittografia della comunicazione. Quindi, state utilizzando ECDH leggendo questo articolo e probabilmente lo utilizzate quotidianamente senza accorgervene.

### La transazione di notifica.

Come abbiamo scoperto nella parte precedente, ECDH è una variante dello scambio di Diffie-Hellman che coinvolge coppie di chiavi basate su una curva ellittica. Per fortuna, abbiamo molte coppie di chiavi che rispettano questo standard nei nostri portafogli Bitcoin!

L'idea è quindi quella di utilizzare le coppie di chiavi dei portafogli deterministici gerarchici Bitcoin delle due parti per stabilire segreti condivisi ed effimeri tra di loro. All'interno del BIP47, viene utilizzato ECDHE (Elliptic Curve Diffie-Hellman Ephemeral).

ECDHE viene utilizzato per la prima volta nel BIP47 per trasmettere il codice di pagamento dal mittente al destinatario. Questa è la famosa transazione di notifica. Infatti, affinché il BIP47 possa essere utilizzato, entrambe le parti (il mittente che invia pagamenti e il destinatario che riceve pagamenti) devono essere a conoscenza del codice di pagamento dell'altra parte. Questo sarà necessario per derivare le chiavi pubbliche effimere e quindi gli indirizzi di ricezione dedicati.

Prima di questo scambio, il mittente è logicamente già a conoscenza del codice di pagamento del destinatario, poiché è stato in grado di recuperarlo off-chain, ad esempio, dal suo sito web o dai suoi social media. Al contrario, il destinatario potrebbe non essere a conoscenza del codice di pagamento del mittente. Sarà quindi necessario trasmetterglielo, altrimenti non sarà in grado di derivare le sue chiavi effimere e quindi non sarà in grado di sapere dove si trovano i suoi bitcoin e di sbloccare i suoi fondi. Potremmo trasmetterglielo off-chain, con un altro sistema di comunicazione, ma ciò comporterebbe un problema in caso di recupero del portafoglio dal seed.
Infatti, come ho già menzionato, gli indirizzi BIP47 non sono derivati dal seed del destinatario (altrimenti si potrebbe utilizzare direttamente uno dei suoi xpub), ma sono il risultato di un calcolo che coinvolge i due codici di pagamento: quello del destinatario e quello del mittente. Pertanto, se il destinatario perde il suo portafoglio e cerca di recuperarlo dal seed, dovrà necessariamente disporre di tutti i codici di pagamento delle persone che gli hanno inviato bitcoin tramite BIP47.
Quindi, potremmo facilmente utilizzare BIP47 senza questa transazione di notifica, ma ogni utente dovrebbe fare un backup dei codici di pagamento dei suoi contatti. Questa situazione rimarrà ingestibile finché non troveremo un modo semplice e resiliente per creare, archiviare e aggiornare questi backup. La transazione di notifica è quindi praticamente obbligatoria nello stato attuale delle cose.

Oltre a questa funzione di backup dei codici di pagamento, come suggerisce il nome stesso, questa transazione svolge anche un ruolo di notifica per il destinatario. Segnala al suo client che è stato aperto un tunnel.

Prima di spiegare più in dettaglio il funzionamento tecnico della transazione di notifica, vorrei parlare un po' del modello di privacy. Infatti, il modello di BIP47 giustificherà alcune precauzioni prese durante la costruzione di questa transazione iniziale.

Il codice di pagamento in sé non costituisce direttamente un rischio per la privacy. A differenza del modello classico di Bitcoin che consente di interrompere il flusso di informazioni tra l'identità dell'utente e le transazioni, mantenendo anonime le chiavi pubbliche, il codice di pagamento può essere associato direttamente a un'identità. Questo ovviamente non è un obbligo, ma questo collegamento non è pericoloso.

Infatti, il codice di pagamento non deriva direttamente gli indirizzi utilizzati per ricevere pagamenti BIP47. Invece, gli indirizzi vengono ottenuti applicando ECDHE tra le chiavi figlie dei codici di pagamento delle due parti.

Quindi, un singolo codice di pagamento non costituisce un rischio diretto per la perdita di privacy poiché si deriva solo l'indirizzo di notifica da esso. Si possono ottenere alcune informazioni, ma normalmente non si saprà con chi si effettuano transazioni.

È quindi essenziale mantenere una rigorosa separazione tra i codici di pagamento degli utenti. A tal fine, la fase di comunicazione iniziale del codice è un momento critico per la privacy del pagamento, eppure è obbligatoria per il corretto funzionamento del protocollo. Se uno dei due codici di pagamento può essere recuperato pubblicamente (ad esempio, su un sito web), il secondo codice, cioè quello del mittente, non deve essere associato al primo.

Ad esempio, immaginiamo che io voglia fare una donazione con BIP47 a un movimento di protesta pacifica in Canada:

- Questa organizzazione ha pubblicato il suo codice di pagamento direttamente sul suo sito web o sui suoi social media.
- Questo codice è quindi associato al movimento.
- Recupero questo codice di pagamento.
- Prima di poter inviare loro una transazione, devo assicurarmi che siano a conoscenza del mio codice di pagamento personale, che è anche associato alla mia identità poiché lo uso per ricevere transazioni dai miei social media.
  Come posso trasmetterlo loro? Se lo invio con un mezzo di comunicazione tradizionale, le informazioni rischiano di trapelare e rischio di essere etichettato come una persona che sostiene movimenti pacifici.
  La transazione di notifica non è certamente l'unico modo per trasmettere segretamente il codice di pagamento del mittente, ma al momento svolge perfettamente questo ruolo applicando diverse strati di sicurezza.
  Nello schema qui sotto, le linee rosse rappresentano il momento in cui il flusso di informazioni deve essere interrotto, e le frecce nere rappresentano i collegamenti indiscutibili che possono essere fatti da un osservatore esterno:
  ![Schema modello di privacy codice di pagamento riutilizzabile](assets/15.webp)
  In realtà, per il modello di privacy classico di Bitcoin, è spesso difficile interrompere completamente il flusso di informazioni tra la coppia di chiavi e l'utente, specialmente quando si effettuano transazioni a distanza. Ad esempio, nel caso di una campagna di donazione, il destinatario sarà costretto a rivelare un indirizzo o una chiave pubblica sul suo sito web o sui suoi social media. L'uso corretto di BIP47, cioè con la transazione di notifica, risolve questo problema grazie a ECDHE e allo strato di crittografia che studieremo.
  Ovviamente, il modello di privacy classico di Bitcoin si osserva sempre a livello delle chiavi pubbliche effimere derivate dall'associazione dei due codici di pagamento. I due modelli sono interdipendenti. Voglio semplicemente mettere in evidenza qui che, a differenza dell'uso classico di una chiave pubblica per ricevere bitcoin, il codice di pagamento può essere associato ad un'identità, poiché l'informazione "Bob effettua una transazione con Alice" viene interrotta in un altro momento. Il codice di pagamento viene utilizzato per generare gli indirizzi di pagamento, ma osservando solo la blockchain, è impossibile associare una transazione di pagamento BIP47 ai codici di pagamento utilizzati per effettuarla.
  Costruzione della transazione di notifica.
  Ora vediamo come funziona questa transazione di notifica. Immaginiamo che Alice voglia inviare fondi a Bob con BIP47. Nel mio esempio, Alice agisce come mittente e Bob come destinatario. Quest'ultimo ha pubblicato il suo codice di pagamento sul suo sito web. Alice è quindi già a conoscenza del codice di pagamento di Bob.
  Alice calcola un segreto condiviso con ECDH:
- Alice combina i testi cifrati ottenuti per formare il codice finale  cifrato di pagamento. Concatena il testo cifrato dell'ascissa della chiave pubblica (x') con il testo cifrato del suo codice stringa (c').

> codice di pagamento criptato = x' || c'

- Alice invia il codice di pagamento criptato a Bob.

4. Bob riceve il codice di pagamento criptato di Alice.

5. Bob utilizza la sua chiave privata “b” per decifrare il codice di pagamento criptato; separa poi il codice di pagamento decifrato in due parti: l'ascissa della chiave pubblica (x) e il codice stringa (c).

> x = x' XOR f1
>
> c = c' XOR f2

6. Bob utilizza l'ascissa della chiave pubblica (x) per verificare se il codice di pagamento è valido.

7. Se il codice di pagamento è valido, Bob può utilizzare la stringa (c) per eseguire operazioni specifiche dalla sua applicazione.

- Alice sostituisce i valori reali dell'ascissa della chiave pubblica (x) e della stringa (c) nel suo codice di pagamento con i valori cifrati (x') e (c').

Prima di continuare la descrizione tecnica di questa transazione di notifica, fermiamoci un attimo su questa operazione XOR. XOR è un operatore logico a livello di bit basato sull'algebra di Boole. A partire da due operandi in bit, restituisce 1 se i bit dello stesso rango sono diversi e restituisce 0 se i bit dello stesso rango sono uguali. Ecco la tabella di verità di XOR in base ai valori degli operandi D ed E:

| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Ad esempio:

> 0110 XOR 1110 = 1000

O ancora:

> 010011 XOR 110110 = 100101

Con ECDH, l'uso di XOR come livello di crittografia è particolarmente coerente. Innanzitutto, grazie a questo operatore, la crittografia è simmetrica. Ciò consentirà al destinatario di decifrare il codice di pagamento con la stessa chiave utilizzata per la crittografia. La chiave di crittografia e decrittografia viene calcolata a partire dal segreto condiviso tramite ECDH.

Questa simmetria è resa possibile dalla proprietà commutativa ed associativa dell'operatore XOR:

- Altre proprietà:
  -> D ⊕ D = 0
  -> D ⊕ 0 = D

- Commutatività:
  D ⊕ E = E ⊕ D

- Associatività:
  D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z

- Simmetria:
  Se: D ⊕ E = L
  Allora: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E
  -> D ⊕ L = E
  Successivamente, questo metodo di crittografia assomiglia molto al cifrario di Vernam (One-Time Pad), l'unico algoritmo di crittografia conosciuto fino ad oggi che ha una sicurezza incondizionata (o assoluta). Affinché il cifrario di Vernam abbia questa caratteristica, la chiave di crittografia deve essere perfettamente casuale, deve essere della stessa lunghezza del messaggio e deve essere utilizzata solo una volta. Nel metodo di crittografia utilizzato qui per il BIP47, la chiave è della stessa lunghezza del messaggio, il fattore di offuscamento ha esattamente la stessa lunghezza della concatenazione dell'ascissa della chiave pubblica con il codice di stringa del codice di pagamento. Questa chiave di crittografia viene utilizzata solo una volta. Tuttavia, non viene creata da un generatore casuale perfetto, poiché è un HMAC. È piuttosto pseudo-casuale. Quindi non è un cifrario di Vernam, ma il metodo ci si avvicina.
  Torniamo alla costruzione della transazione di notifica:

4. Alice ha attualmente il suo codice di pagamento con un payload crittografato. Costruirà e diffonderà una transazione che coinvolge la sua chiave pubblica "A" come input, un output destinato all'indirizzo di notifica di Bob e un output OP_RETURN costituito dal suo codice di pagamento con il payload crittografato. Questa transazione è la transazione di notifica.

OP_RETURN è un Opcode, cioè uno script, che consente di contrassegnare un output di transazione Bitcoin come non valido. Oggi viene utilizzato per diffondere o ancorare informazioni sulla blockchain di Bitcoin. È possibile memorizzare fino a 80 byte di dati che vengono registrati sulla catena e quindi visibili a tutti gli altri utenti.

Come abbiamo visto nella parte precedente, Diffie-Hellman viene utilizzato per generare un segreto condiviso tra due utenti che comunicano su una rete non sicura e potenzialmente osservata da attaccanti. Nel BIP47, ECDH viene utilizzato per poter comunicare sulla rete Bitcoin, che per sua natura è una rete di comunicazione trasparente e osservata da numerosi attaccanti. Il segreto condiviso calcolato tramite lo scambio di chiavi Diffie-Hellman sulla curva ellittica viene quindi utilizzato per crittografare le informazioni segrete da trasmettere: il codice di pagamento del mittente (Alice).

Ecco uno schema tratto dal BIP47 che illustra quanto appena descritto:

![Schema Alice invia il suo codice di pagamento mascherato all'indirizzo di notifica di Bob](assets/16.webp)

Credito: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Se confrontiamo questo schema con ciò che ho descritto in precedenza:

- "Wallet Priv-Key" dal lato di Alice corrisponde a: a.

- "Child Pub-Key 0" dal lato di Bob corrisponde a: B.
- "Notification Shared Secret" corrisponde a: f.
- "Masked Payment Code" corrisponde al codice di pagamento mascherato, cioè con il payload cifrato: x' e c'.

- "Notification Transaction" è la transazione che contiene l'OP_RETURN.

Riassumo i passaggi che abbiamo appena visto per effettuare una transazione di notifica:

- Alice ottiene il codice di pagamento e l'indirizzo di notifica di Bob.

- Alice seleziona un UTXO che le appartiene nel suo portafoglio HD con la corrispondente coppia di chiavi.

- Calcola un punto segreto sulla curva ellittica tramite ECDH.

- Utilizza questo punto segreto per calcolare un HMAC che è il fattore di cecità ("Blinding factor").

- Utilizza questo fattore di cecità per crittografare il payload del suo codice di pagamento personale.

- Utilizza un output di transazione OP_RETURN per trasferire il codice di pagamento mascherato a Bob.


Per comprendere più in dettaglio il suo funzionamento, in particolare l'utilizzo di OP_RETURN, studiamo insieme una vera transazione di notifica. Ho effettuato una transazione di questo tipo su Testnet che puoi trovare cliccando qui:

https://mempool.space/fr/testnet/tx/0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e

TXID:

> 0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e

![Transazione di notifica BIP47](assets/17.webp)

Credito: https://blockstream.info/

Osservando questa transazione, possiamo già vedere che ha un solo input e 4 output:

- Il primo output è l'OP_RETURN che contiene il mio codice di pagamento mascherato.

- Il secondo output di 546 sats punta all'indirizzo di notifica del mio destinatario.

- Il terzo output di 15.000 sats rappresenta le commissioni di servizio, poiché ho utilizzato Samourai Wallet per costruire questa transazione.

- Il quarto output di due milioni di sats rappresenta il resto, cioè la differenza rimanente del mio input che torna a un altro mio indirizzo.

La cosa più interessante da studiare è ovviamente l'output 0 che utilizza l'OP_RETURN. Esaminiamo più da vicino cosa contiene:

![Output OP_RETURN della transazione di notifica BIP47](assets/18.webp)

Credito: https://blockstream.info/

Qui scopriamo lo script dell'output in formato esadecimale:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

In questo script possiamo analizzare diverse parti:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000>
> Gli opcodes:
>
> 6a4c
>
> Un byte che indica la dimensione del payload (80 byte):
>
> 50
>
> I metadati del mio codice di pagamento in chiaro:
>
> 010002
>
> L'ascissa cifrata della chiave pubblica del mio codice di pagamento:
>
> b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164
>
> Il codice di stringa cifrato del mio codice di pagamento:
> 927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d8
>
> Riempimento per raggiungere 80 byte:
> 00000000000000000000000000

Tra gli opcodes, possiamo riconoscere 0x6a che indica l'OP_RETURN e 0x4c che indica l'OP_PUSHDATA1. Il byte successivo a quest'ultimo opcode indica la dimensione del payload che segue. Indica 0x50, ovvero 80 byte.

Successivamente viene il codice di pagamento con il payload cifrato.

Ecco il mio codice di pagamento in chiaro utilizzato in questa transazione:

> In base 58:
>
> PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU
>
> In base 16 (HEX):
> 4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db

Se confrontiamo il mio codice di pagamento in chiaro con l'OP_RETURN, possiamo vedere che l'HRP (in marrone) e il checksum (in rosa) non vengono trasmessi. È normale, queste informazioni sono destinate agli esseri umani.
Successivamente, è possibile riconoscere (in verde) la versione (0x01), il campo di bit (0x00) e la parità della chiave pubblica (0x02). E, alla fine del codice di pagamento, i byte vuoti in nero (0x00) che servono per riempire fino a raggiungere un totale di 80 byte. Tutti questi metadati vengono trasmessi in chiaro (non crittografati).
Infine, si può osservare che l'ascissa della chiave pubblica (in blu) e il codice di stringa (in rosso) sono stati crittografati. Questo costituisce il payload del codice di pagamento.

### Ricezione della transazione di notifica.

Ora che Alice ha inviato la transazione di notifica a Bob, vediamo come quest'ultimo la interpreta.

Ricordiamo che, Bob deve essere in grado di accedere al codice di pagamento di Alice. Senza questa informazione, come vedremo nella parte successiva, non sarà in grado di derivare le coppie di chiavi create da Alice e quindi non potrà accedere ai suoi bitcoin ricevuti con BIP47. Al momento, il payload del codice di pagamento di Alice è crittografato. Vediamo insieme come Bob lo decifra.

1. Bob monitora le transazioni che creano output con il suo indirizzo di notifica.

2. Quando una transazione ha un output sul suo indirizzo di notifica, Bob la analizza per vedere se contiene un output OP_RETURN che rispetta lo standard BIP47.

3. Se il primo byte del payload di OP_RETURN è 0x01, Bob inizia la ricerca di un eventuale segreto condiviso con ECDH:

- Bob seleziona la chiave pubblica in input della transazione. Cioè la chiave pubblica di Alice chiamata "A" con:

> A = a·G

- Bob seleziona la chiave privata "b" associata al suo indirizzo di notifica personale:

> b

- Bob calcola il punto segreto "S" (segreto condiviso ECDH) sulla curva ellittica mediante l'addizione e il raddoppio dei punti applicando la sua chiave privata "b" alla chiave pubblica di Alice "A":

> S = b·A

- Bob determina il punto segreto "f" che consentirà di decifrare il payload del codice di pagamento di Alice. Allo stesso modo in cui Alice lo aveva calcolato in precedenza, Bob troverà "f" applicando HMAC-SHA512 su (x) il valore dell'ascissa del punto segreto "S" e su (o) l'UTXO consumato in input a questa transazione di notifica:

> f = HMAC-SHA512(o, x)

4. Bob interpreta i dati di OP_RETURN nella transazione di notifica come un codice di pagamento. Semplicemente decifrerà il payload di questo potenziale codice di pagamento utilizzando il fattore di cieco "f":

- Bob divide il punto segreto "f" in due parti: i primi 32 byte di "f" saranno "f1" e gli ultimi 32 byte saranno "f2".
- Bob decifra il valore dell'ascissa cifrata (x') della chiave pubblica del codice di pagamento di Alice:

> x = x' XOR f1

- Bob decifra il valore del codice di stringa cifrato (c') del codice di pagamento di Alice:

> c = c' XOR f2

5. Bob verifica se il valore della chiave pubblica del codice di pagamento di Alice fa parte del gruppo secp256k1. Se è così, lo interpreta come un codice di pagamento valido. Altrimenti, ignora questa transazione.

Ora che Bob conosce il codice di pagamento di Alice, lei può inviargli fino a 2^32 pagamenti senza dover mai fare più una transazione di notifica di questo tipo.

Perché funziona? Come fa Bob a determinare lo stesso punto segreto di Alice e quindi a decifrare il suo codice di pagamento? Esaminiamo più nel dettaglio l'azione di ECDH in ciò che abbiamo appena descritto.

Innanzitutto, stiamo affrontando una crittografia simmetrica. Ciò significa che la chiave di cifratura e la chiave di decifratura sono lo stesso valore. Questa chiave nella transazione di notifica è il punto segreto (f = f1 || f2). Quindi Alice e Bob devono ottenere lo stesso valore per f, senza trasmetterlo direttamente poiché un attaccante potrebbe sottrarlo e decifrare l'informazione segreta.

Questo fattore cieco viene ottenuto applicando HMAC-SHA512 a due valori: l'ascissa di un punto segreto e l'UTXO consumato come input della transazione. Quindi Bob deve avere queste due informazioni per decifrare il payload del codice di pagamento di Alice.

Per l'UTXO in input, Bob può semplicemente recuperarlo osservando la transazione di notifica. Per il punto segreto, Bob dovrà utilizzare ECDH.

Come visto nella parte su Diffie-Hellman, semplicemente scambiando le rispettive chiavi pubbliche e applicando segretamente le loro chiavi private alla chiave pubblica dell'altro, Alice e Bob possono trovare un punto preciso e segreto sulla curva ellittica. La transazione di notifica si basa su questo meccanismo:

> La coppia di chiavi di Bob:
>
> B = b·G
>
> La coppia di chiavi di Alice:
>
> A = a·G
>
> Per un punto segreto S (x,y):
>
> S = a·B = a·b·G = b·a·G = b·A

![Schema generazione di un segreto condiviso con ECDHE](assets/19.webp)
Ora che Bob conosce il codice di pagamento di Alice, sarà in grado di rilevare i pagamenti BIP47 da parte di Alice e potrà derivare le chiavi private che bloccano i bitcoin ricevuti.
![Bob interpreta la transazione di notifica di Alice](assets/20.webp)

Crediti: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Se confrontiamo questo schema con ciò che ho descritto in precedenza:

- "Wallet Pub-Key" da parte di Alice corrisponde a: A.

- "Child Priv-Key 0" da parte di Bob corrisponde a: b.

- "Notification Shared Secret" corrisponde a: f.

- "Masked Payment Code" corrisponde al codice di pagamento di Alice mascherato, cioè con il payload crittografato: x' e c'.

- "Notification Transaction" è la transazione che contiene l'OP_RETURN.

Riassumo i passaggi che abbiamo appena visto insieme per ricevere e interpretare una transazione di notifica:

- Bob monitora le transazioni in uscita verso il suo indirizzo di notifica.

- Quando ne rileva una, recupera le informazioni contenute nell'OP_RETURN.

- Bob seleziona la chiave pubblica in input e calcola un punto segreto tramite ECDH.

- Utilizza questo punto segreto per calcolare un HMAC che è il fattore di cecità.

- Utilizza questo fattore di cecità per decifrare il payload del codice di pagamento di Alice contenuto nell'OP_RETURN.

### La transazione di pagamento BIP47.

Studiamo ora insieme il processo di pagamento con BIP47. Per ricordarvi la situazione attuale:

- Alice conosce il codice di pagamento di Bob che ha semplicemente recuperato dal suo sito web.

- Bob conosce il codice di pagamento di Alice grazie alla transazione di notifica.

- Alice effettuerà un primo pagamento a Bob. Potrà effettuarne molti altri allo stesso modo.

Prima di spiegarvi questo processo, penso sia importante ricordare su quali indici stiamo lavorando attualmente:

Descriviamo il percorso di derivazione di un codice di pagamento come segue: m/47'/0'/0'/.

- La prima coppia di figli normali (non rinforzati) è quella utilizzata per generare l'indirizzo di notifica di cui abbiamo parlato nella parte precedente: m/47'/0'/0'/0/.

- Le coppie di chiavi figlie normali vengono utilizzate all'interno di ECDH per generare gli indirizzi di ricezione dei pagamenti BIP47 come vedremo in questa parte: m/47'/0'/0'/ da 0 a 2 147 483 647/.

- Le coppie di chiavi figlie rinforzate sono codici di pagamento effimeri: m/47'/0'/0'/ da 0' a 2 147 483 647'/.
  Ogni volta che Alice desidera inviare un pagamento a Bob, genera un nuovo indirizzo univoco vuoto utilizzando nuovamente il protocollo ECDH:
- Alice seleziona la prima chiave privata derivata dal suo codice di pagamento riutilizzabile personale:

> a

- Alice seleziona la prima chiave pubblica non utilizzata derivata dal codice di pagamento di Bob. Questa chiave pubblica, chiamata "B", è associata alla chiave privata "b" di cui solo Bob è a conoscenza.

> B = b·G

- Alice calcola un punto segreto "S" sulla curva ellittica mediante l'addizione e il raddoppio dei punti applicando la sua chiave privata "a" alla chiave pubblica di Bob "B":

> S = a·B

- Da questo punto segreto, Alice calcola il segreto condiviso "s" (minuscolo). Per farlo, seleziona l'ascissa del punto segreto "S" chiamata "Sx" e passa questo valore alla funzione di hash SHA256.

> s = SHA256(Sx)

Non fidarti. Verifica! Se desideri comprendere i principi di base di una funzione di hash, troverai tutto ciò che ti serve in questo articolo. E se non ti fidi del NIST (hai ragione) e desideri comprendere in dettaglio il funzionamento di SHA256, ti spiego tutto in questo articolo in francese.

- Alice utilizza questo segreto condiviso "s" per calcolare un indirizzo di ricezione dei pagamenti Bitcoin. Inizialmente, verifica che "s" sia contenuto nell'ordine della curva secp256k1. Se non è così, incrementa l'indice della chiave pubblica di Bob per derivare un altro segreto condiviso.

- Successivamente, calcola una chiave pubblica "K0" aggiungendo sulla curva ellittica i punti "B" e "s·G". In altre parole, Alice somma la chiave pubblica derivata dal codice di pagamento di Bob "B" con un altro punto calcolato sulla curva ellittica mediante l'addizione e il raddoppio dei punti con il segreto condiviso "s" dal punto generatore della curva secp256k1 "G". Questo nuovo punto rappresenta una chiave pubblica, che chiamiamo "K0":

> K0 = B + s·G

- Utilizzando questa chiave pubblica "K0", Alice può derivare un indirizzo di ricezione vuoto in modo standard (ad esempio, SegWit V0 in Bech32).

Una volta che Alice ha questo indirizzo di ricezione "K0" appartenente a Bob, può creare una transazione Bitcoin classica, selezionando un UTXO che le appartiene su un altro ramo del suo portafoglio HD e inviandolo all'indirizzo "K0" di Bob.

![Alice invia bitcoin a Bob con BIP47](assets/21.webp)

Crediti: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
Se corrispondiamo questo schema a quanto vi ho descritto in precedenza:

- "Child Priv-Key" da parte di Alice corrisponde a: a.
- "Child Pub-Key 0" da parte di Bob corrisponde a: B.
- "Payment Secret 0" corrisponde a: s.
- "Payment Pub-Key 0" corrisponde a: K0.

Riassumo i passaggi che abbiamo appena visto insieme per inviare un pagamento BIP47:

- Alice seleziona la prima chiave privata figlia derivata dal suo codice di pagamento personale.
- Calcola un punto segreto sulla curva ellittica utilizzando ECDH dalla prima chiave pubblica figlia non utilizzata derivata dal codice di pagamento di Bob.
- Utilizza questo punto segreto per calcolare un segreto condiviso con SHA256.
- Utilizza questo segreto condiviso per calcolare un nuovo punto segreto sulla curva ellittica.
- Aggiunge questo nuovo punto segreto alla chiave pubblica di Bob.
- Ottiene una nuova chiave pubblica effimera di cui solo Bob ha la chiave privata associata.
- Alice può inviare una transazione classica a Bob con l'indirizzo di ricezione effimero derivato.

Se desidera effettuare un secondo pagamento, ripeterà i passaggi sopra descritti, ad eccezione del fatto che selezionerà la seconda chiave pubblica derivata dal codice di pagamento di Bob. Cioè la prossima chiave non utilizzata. Avrà quindi un secondo indirizzo di ricezione appartenente a Bob "K1".

![Alice deriva tre indirizzi di ricezione BIP47 per Bob](assets/22.webp)

Credito: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Può continuare in questo modo e derivare fino a 2^32 indirizzi vuoti appartenenti a Bob.

Da un punto di vista esterno, osservando la blockchain di Bitcoin, teoricamente è impossibile distinguere un pagamento BIP47 da un pagamento classico. Ecco un esempio di una transazione di pagamento BIP47 sul Testnet:

https://blockstream.info/testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

TXID:

> 94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

Sembra una transazione classica con un input consumato, un output di pagamento di 210.000 sats e un resto:

![Transazione di pagamento Bitcoin con BIP47](assets/23.webp)

Credito: https://blockstream.info/

### Ricezione del pagamento BIP47 e derivazione della chiave privata.

Alice ha appena effettuato il suo primo pagamento verso un indirizzo BIP47 vuoto di Bob. Ora vediamo insieme come Bob riceve questo pagamento. Vedremo anche perché Alice non ha accesso alla chiave privata dell'indirizzo che ha appena generato e come Bob trova questa chiave per poter spendere i bitcoin appena ricevuti.
Appena Bob riceve la transazione di notifica da parte di Alice, deriva la chiave pubblica BIP47 "K0" prima ancora che la corrispondente transazione di pagamento venga inviata. Quindi osserva tutti i pagamenti verso l'indirizzo associato. In realtà, deriva immediatamente più indirizzi che osserverà (K0, K1, K2, K3...). Ecco come deriva questa chiave pubblica "K0":

- Bob seleziona la prima chiave privata figlia derivata dal suo codice di pagamento. Questa chiave privata è chiamata "b". È associata alla chiave pubblica "B" con cui Alice ha effettuato i calcoli nella fase precedente:

> b

- Bob seleziona la prima chiave pubblica di Alice derivata dal suo codice di pagamento. Questa chiave è chiamata "A". È associata alla chiave privata "a" con cui Alice ha effettuato i calcoli e di cui solo Alice è a conoscenza. Bob può effettuare questo processo perché conosce il codice di pagamento di Alice che gli è stato trasmesso con la transazione di notifica.

> A = a·G

- Bob calcola il punto segreto "S", attraverso l'addizione e il raddoppio dei punti sulla curva ellittica, applicando la sua chiave privata "b" alla chiave pubblica di Alice "A". Qui viene utilizzato l'ECDH che ci garantisce che questo punto "S" sarà lo stesso per Bob e per Alice.

> S = b·A

- Allo stesso modo di Alice, Bob isola l'ascissa di questo punto "S". Abbiamo chiamato questo valore "Sx". Passa questo valore alla funzione SHA256 per trovare il segreto condiviso "s" (minuscolo).

> s = SHA256(Sx)

- Sempre nello stesso modo di Alice, Bob calcola il punto "s·G" sulla curva ellittica. Poi, aggiunge questo punto segreto alla sua chiave pubblica "B". Ottiene così un nuovo punto sulla curva ellittica che interpreta come una chiave pubblica "K0":

> K0 = B + s·G

Una volta che Bob ha questa chiave pubblica "K0", può derivare la chiave privata associata per poter spendere i suoi bitcoin. È l'unico in grado di generare questo numero.

- Bob aggiunge la sua chiave privata figlia "b" derivata dal suo codice di pagamento personale. È l'unico in grado di ottenere il valore di "b". Poi, aggiunge "b" al segreto condiviso "s" per ottenere k0, la chiave privata di K0:

> k0 = b + s
> Grazie alla legge di gruppo della curva ellittica, Bob ottiene esattamente la chiave privata corrispondente alla chiave pubblica utilizzata da Alice. Quindi abbiamo:
> K0 = k0·G

![Bob genera i suoi indirizzi di ricezione BIP47](assets/24.webp)

Crediti: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Se corrispondiamo questo schema a quanto vi ho descritto in precedenza:

- "Child Priv-Key 0" da parte di Bob corrisponde a: b.

- "Child Pub-Key 0" da parte di Alice corrisponde a: A.

- "Payment Secret 0" corrisponde a: s.

- "Payment Pub-Key 0" corrisponde a: K0.

- "Payment Priv-Key 0" corrisponde a: k0.

Riassumo i passaggi che abbiamo appena visto insieme per ricevere un pagamento BIP47 e calcolare la corrispondente chiave privata:

- Bob seleziona la prima chiave privata figlia derivata dal suo codice di pagamento personale.

- Calcola un punto segreto sulla curva ellittica tramite ECDH utilizzando la prima chiave pubblica figlia derivata dal codice di catena di Alice.

- Utilizza questo punto segreto per calcolare un segreto condiviso con SHA256.

- Utilizza questo segreto condiviso per calcolare un nuovo punto segreto sulla curva ellittica.

- Aggiunge questo nuovo punto segreto alla sua chiave pubblica personale.

- Ottiene una nuova chiave pubblica effimera, a cui Alice invierà il suo primo pagamento.

- Bob calcola la chiave privata associata a questa chiave pubblica effimera aggiungendo la sua chiave privata figlia derivata dal suo codice di pagamento e il segreto condiviso.

Poiché Alice non può ottenere "b", la chiave privata di Bob, non è in grado di determinare k0, la chiave privata associata all'indirizzo di ricezione BIP47 di Bob.

Schematicamente, possiamo rappresentare il calcolo del segreto condiviso "S" come segue:

![Calcolo del segreto condiviso con ECDHE](assets/25.webp)

Una volta trovato il segreto condiviso con ECDH, Alice e Bob calcolano la chiave pubblica di pagamento BIP47 "K0", e Bob calcola anche la chiave privata associata "k0":

![Derivazione dell'indirizzo di ricezione BIP47 dal segreto condiviso](assets/26.webp)

### Rimborso del pagamento BIP47.

Poiché Bob conosce già il codice di pagamento riutilizzabile di Alice, dispone già di tutte le informazioni necessarie per inviarle un rimborso. Non avrà bisogno di contattare nuovamente Alice per chiederle alcuna informazione. Dovrà semplicemente notificarla con una transazione di notifica, in particolare affinché possa recuperare i suoi indirizzi BIP47 con il suo seed, e poi potrà anche inviarle fino a 2^32 pagamenti.
Bob può quindi rimborsare Alice nello stesso modo in cui lei gli ha inviato i pagamenti. I ruoli si invertano:

![Bob invia un rimborso ad Alice con BIP47](assets/27.webp)

Crediti: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Ora conoscete tutti i dettagli di questa magnifica soluzione che è il BIP47.

## Utilizzi derivati di PayNym.

L'implementazione di questo BIP47 su Samourai Wallet ha dato origine a PayNym, identificatori calcolati dai codici di pagamento degli utenti. Oggi, la loro utilità va ben oltre l'uso del BIP47.

Il team di Samourai sta gradualmente sviluppando un intero ecosistema di strumenti e servizi basati sul PayNym dell'utente. Tra questi, ci sono ovviamente tutti gli strumenti di spesa che consentono di ottimizzare la privacy dell'utente aggiungendo entropia a una transazione e quindi aggiungendo del deniability.

L'uso combinato di Soroban, la rete di comunicazione crittografata basata su Tor, e PayNym ha notevolmente migliorato l'esperienza dell'utente nella costruzione di transazioni collaborative, mantenendo un buon livello di sicurezza. Pertanto, è possibile effettuare facilmente transazioni Stowaway (PayJoin) e StonewallX2 senza dover effettuare manualmente numerosi scambi di transazioni non firmate necessarie per configurare una transazione collaborativa di questo tipo.

A differenza dell'uso di BIP47, poiché queste transazioni collaborative non richiedono una transazione di notifica, è sufficiente collegare i PayNym per utilizzare questi strumenti. Non è necessario connetterli.

Se desiderate saperne di più sulle transazioni collaborative e, più in generale, su tutti gli strumenti di spesa di Samourai Wallet, potete leggere la sezione "Gli strumenti di spesa" in questo articolo. Troverete una spiegazione tecnica e un tutorial dettagliato per ogni strumento.

Oltre a queste transazioni collaborative, di recente si è osservato che il team di Samourai sta lavorando su un protocollo di autenticazione legato a PayNym: Auth47. Questo strumento è già implementato e consente, ad esempio, di autenticarsi su un sito web che accetta questo metodo tramite un PayNym. In futuro, penso che oltre a questa possibilità di autenticazione sul web, Auth47 si inserirà in un progetto più ampio legato all'ecosistema BIP47/PayNym/Samourai. Forse questo protocollo verrà utilizzato per ottimizzare ulteriormente l'esperienza dell'utente del portafoglio Samourai Wallet, in particolare nell'uso degli strumenti di spesa. Da seguire...

## La mia opinione personale su BIP47.

Ovviamente, il principale svantaggio del BIP47 è la transazione di notifica. Questo porta l'utente a dover pagare una commissione per il suo mining, il che può essere fastidioso per alcuni. D'altra parte, l'argomento dello "spam" sulla blockchain di Bitcoin è assolutamente inaccettabile. Chiunque paghi una commissione per la sua transazione deve essere in grado di registrarla nel registro, indipendentemente dal suo scopo. Affermare il contrario significa schierarsi a favore della censura.
È possibile che in futuro vengano trovate altre soluzioni meno costose per comunicare il codice di pagamento del mittente al destinatario e per consentire a quest'ultimo di conservarlo in modo sicuro. Ma, per il momento, la transazione di notifica rimane la soluzione con il minor numero di compromessi.

Questo svantaggio rimane trascurabile se si considerano tutti i benefici del BIP47. Tra tutte le proposte esistenti per risolvere il problema del riutilizzo degli indirizzi, secondo me questa appare come la migliore soluzione.

Come spiegato in precedenza, la maggior parte dei riutilizzi degli indirizzi proviene dagli exchange. Il BIP47 è l'unico modo ragionevole per risolvere effettivamente questo problema alla fonte. Qualsiasi proposta volta a ridurre il numero di riutilizzi degli indirizzi dovrebbe considerare questo aspetto e adattare la soluzione alla fonte principale del problema.

In termini di utilizzo, anche se i suoi meccanismi sono piuttosto complessi, la procedura di pagamento BIP47 è molto semplice. I codici di pagamento riutilizzabili possono quindi essere adottati facilmente, anche da utenti inesperti.

In termini di privacy, il BIP47 è molto interessante. Come ho spiegato nella parte sulla transazione di notifica, il codice di pagamento non rivela alcuna informazione sugli indirizzi effimeri derivati. Ciò consente di interrompere il flusso di informazioni tra la transazione Bitcoin e l'identificatore del destinatario, a differenza dell'uso tradizionale di un indirizzo di ricezione.

E soprattutto, l'implementazione PayNym del BIP47 funziona! È disponibile su Samourai Wallet dal 2016 e su Sparrow Wallet dall'inizio di quest'anno. Non si tratta di un progetto scientifico, ma di una soluzione testata ieri e completamente funzionante oggi.

Speriamo che in futuro questi codici di pagamento riutilizzabili saranno adottati dagli attori dell'ecosistema, implementati nei software dei portafogli e utilizzati dai bitcoiner.

Qualsiasi soluzione veramente positiva per la privacy dell'utente deve essere discussa, promossa e difesa, affinché Bitcoin non diventi il terreno di gioco delle agenzie di intelligence e lo strumento di sorveglianza dei governi.
*Stava pensando al modo in cui era stato perseguitato e insultato ovunque, e ora sentiva tutti dire che era il più bello di tutti quegli splendidi uccelli! E persino il sambuco piegava i suoi rami verso di lui, e il sole diffondeva una luce così calda e benefica! Allora le sue piume si gonfiarono, il suo collo slanciato si erse, e gridò con tutto il cuore: "Come avrei potuto sognare tanta felicità quando ero solo un brutto anatroccolo."*

## Per andare oltre:

- Comprendere e utilizzare il CoinJoin su Bitcoin.

- Comprendere i percorsi di derivazione di un portafoglio Bitcoin.

- Installare e utilizzare il proprio nodo Bitcoin RoninDojo.

### Risorse esterne e ringraziamenti:

Grazie a LaurentMT e Théo Pantamis per i numerosi concetti che mi hanno spiegato ed utilizzati in questo articolo. Spero di essere riuscito a trasmetterli con precisione.

Grazie a Fanis Michalakis per la revisione di questo testo e i suoi consigli da esperto.

- https://bitcoiner.guide/paynym/
- https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols

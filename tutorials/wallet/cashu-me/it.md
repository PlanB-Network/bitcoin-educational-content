---
name: Cashu.me
description: Guida di Cashu.me all'utilizzo di ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Ecco un video tutorial di BTC Sessions, una video guida che vi spiega come configurare e utilizzare Cashu.me Bitcoin Wallet, che vi dà accesso a transazioni Bitcoin semplici, economiche e private - senza bisogno di un app store!


In questo tutorial esploreremo Cashu.me, un Wallet basato su browser per pagamenti privati in Bitcoin utilizzando Chaumian ecash. Prima di tuffarci, facciamo una breve introduzione all'ecash e al suo funzionamento.


## Introduzione a ecash


Immaginate di avere in tasca del contante digitale che funziona esattamente come le banconote fisiche: privato, istantaneo e utilizzabile da pari a pari senza intermediari. Questo è ciò che consente ecash: un approccio al pagamento digitale che riporta la privacy del contante fisico nel mondo digitale. A differenza di onchain-Bitcoin, che registra ogni transazione su un Ledger pubblico visibile a chiunque, ecash crea token privati che rappresentano il valore reale del Bitcoin, mantenendo riservate le vostre abitudini di spesa.


Pensate agli ecash come a strumenti digitali al portatore memorizzati sul vostro dispositivo: se li possedete, li possedete, proprio come i contanti fisici. Questi token sono emessi da servizi fidati chiamati `Mints` che detengono le riserve Bitcoin sottostanti. Quando si usa ecash, non si trasmettono le transazioni all'intera rete. Al contrario, si scambiano token privati direttamente con altri, creando un'esperienza di pagamento che assomiglia più a una consegna di contanti che a un pagamento digitale tradizionale.


Cashu è un protocollo Chaumian ecash gratuito e open-source, costruito per Bitcoin. La tecnologia si basa sulla ricerca crittografica pionieristica di David Chaum degli anni '80, utilizzando le "firme cieche" per garantire la privacy. Quando si ricevono i gettoni ecash, la zecca li firma senza sapere dove verranno spesi successivamente: una caratteristica fondamentale che impedisce il tracciamento delle transazioni. È importante notare che ecash non sostituisce il Bitcoin, ma lo integra risolvendo alcuni problemi critici legati ai requisiti dell'architettura del Bitcoin. Fornisce la privacy che il contante fisico offre. Fornisce la privacy offerta dal contante fisico (che manca al trasparente Ledger del Bitcoin) e consente microtransazioni istantanee senza le commissioni del Blockchain o i ritardi di conferma.


Ecash si integra perfettamente con il Lightning Network. Si usa Lightning per depositare il Bitcoin in una zecca (convertendo il valore del Bitcoin in gettoni ecash) e per prelevare successivamente (riconvertendo i gettoni in un saldo spendibile di Lightning). Insieme, formano una potente combinazione: Bitcoin fornisce il regolamento sicuro Layer, Lightning consente transazioni veloci e l'interoperabilità della rete ed ecash aggiunge la privacy Layer che rende i pagamenti digitali nuovamente privati.


## Cashu.me


Cashu.me è una `Progressive Web App (PWA)` che implementa il protocollo Cashu - un'implementazione specifica di Chaumian ecash progettata per Bitcoin. In quanto PWA, funziona direttamente nel browser senza richiedere l'installazione negli app store, anche se è possibile "installarla" sul proprio dispositivo per facilitarne l'accesso. Questo approccio basato sul web garantisce un'ampia compatibilità tra i sistemi operativi, mantenendo la sicurezza attraverso protocolli crittografici piuttosto che restrizioni di piattaforma.


## 🎉 Caratteristiche principali


Scopriamo le caratteristiche ed esploriamo ciò che Cashu.me ha da offrire:



- Chaumian ecash su Lightning**: Utilizza firme cieche in modo che le zecche non possano tracciare i saldi degli utenti o la cronologia delle transazioni
- Autocustodia dei gettoni**: Il controllo dei gettoni ecash avviene localmente con la propria frase seed
- Backup della frase seed**: frase di recupero di 12 parole per il ripristino del Wallet
- Indipendenza dalle zecche**: Funziona con più zecche indipendenti: non siete vincolati a un unico fornitore
- Transazioni istantanee e gratuite**: All'interno della stessa menta, i pagamenti vengono finalizzati in pochi secondi con zero commissioni
- Architettura a tutela della privacy**: Le zecche non possono vedere chi compie transazioni con chi
- Ecash offline**: Inviare/ricevere gettoni attraverso un protocollo di trasmissione locale, come NFC, codice QR, Bluetooth, ecc. senza connessione a Internet
- Scoprire le zecche di ecash tramite Nostr**: Trovare e verificare zecche affidabili attraverso il protocollo Nostr
- Scambio di ecash tra zecche**: Tutte le zecche parlano Lightning, il che significa che è possibile trasferire il valore tra di esse.
- Controllate a distanza il vostro Wallet con Nostr Wallet Connect (NWC)**: Connettersi ad altre applicazioni come Nostr Client e iniziare a fare zapping tramite NWC


Il compromesso critico è la "fiducia": mentre si controllano i gettoni stessi, bisogna fidarsi delle zecche per custodire le riserve di Bitcoin sottostanti. Come afferma la documentazione di Cashu:


> ... la zecca gestisce l'infrastruttura di Lightning e custodisce i satoshi per gli utenti di ecash della zecca. Gli utenti devono affidare alla zecca il Redeem dei loro ecash una volta che vogliono passare a Lightning.

- Documentazione Cashu, [Domande generali sulla sicurezza e sulla privacy](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Questo rende ecash una soluzione di custodia per il Bitcoin stesso, pur mantenendo il pieno controllo dei gettoni.


## 1️⃣ Impostazione iniziale


① Iniziate visitando [Wallet.cashu.me](https://Wallet.cashu.me) nel vostro browser. Poiché Cashu.me è una `PWA`, non è necessario scaricarla dagli app store, ma è sufficiente aprire il sito direttamente nel browser. Per facilitare l'accesso, è possibile installarlo nella schermata iniziale del dispositivo.


per installare la PWA, toccare il pulsante del menu ⋮ nel browser e selezionare "Aggiungi alla schermata iniziale". Una volta installata, chiudere la scheda del browser e lanciare Cashu.me dalla schermata iniziale del dispositivo. Nella schermata di benvenuto, toccare "Avanti" per continuare.


③ La sicurezza è fondamentale. Conservare la frase seed in modo sicuro in un gestore di password o, meglio ancora, scriverla su carta. Questa frase di recupero di 12 parole è l'unico modo per recuperare i fondi se si perde l'accesso al dispositivo. Toccare l'icona 👁️ per rivelare la frase seed, scrivere attentamente tutte le 12 parole in ordine, quindi selezionare la casella contrassegnata da "L'ho scritta". Toccare "Avanti" per continuare e selezionare la casella per confermare l'accettazione dei "termini" nella schermata successiva.


![image](assets/en/01.webp)


Dopo aver completato la configurazione, è necessario collegarsi a una "menta". Toccare `ADD MINT` seguito da `DISCOVER MINTS` per visualizzare le zecche raccomandate dalla comunità Nostr. Per ulteriori verifiche, è possibile esaminare le valutazioni delle zecche su [bitcoinmints.com](bitcoinmints.com).


Toccare quindi "Clicca per sfogliare le mentine" per visualizzare l'elenco completo. Selezionate una menta copiando il suo URL, incollandolo nel campo URL e assegnandole un nome riconoscibile. Per questo esempio, useremo:


URL: `https://mint.minibits.cash/Bitcoin`

Nome: `Minibits`


![image](assets/en/02.webp)


Toccare `ADD MINT` per completare il processo. Nella schermata di conferma, verificare che ci si fidi dell'operatore di questa zecca, quindi toccare nuovamente `ADD MINT`. La zecca Minibits apparirà ora sulla schermata principale. Una volta configurato il Wallet, è necessario finanziarlo prima di effettuare transazioni.


![image](assets/en/03.webp)


## 2️⃣ Finanziamento del Wallet


Cashu.me offre due metodi distinti per finanziare il proprio Wallet. Quando si tocca "Ricevi" nella schermata principale, si vedranno le opzioni per ricevere i fondi tramite "contanti" o "illuminazione".


![image](assets/en/04.webp)


### Finanziamento tramite LIGHTNING


La prima opzione è quella di finanziare il Wallet tramite il Lightning Invoice. selezionare una zecca se sono state aggiunte diverse zecche e definire l'importo (Sats) che si desidera ricevere. A questo punto viene visualizzato un codice QR che può essere scansionato con un altro Lightning Wallet oppure si può semplicemente "copiare" il Invoice e incollarlo in un altro Wallet per pagare e finanziare il Wallet di cashu.me.


![image](assets/en/05.webp)


### Ricevere ecash


Il metodo ecash consente di ricevere gettoni direttamente da un altro Wallet ecash. Iniziare toccando il pulsante `Ricevi` e selezionare l'opzione `ECASH`. Si potrà scegliere tra "Incolla", "Scansiona" o "NFC" per inviare un token Cashu da un altro Wallet. Se si sceglie di incollare, inserire la stringa token copiata da un altro Wallet, l'"Importo" e la "Zecca" verranno visualizzati automaticamente. Toccare `RICEVI` per completare la transazione e il Sats apparirà nel Wallet. Si noti che il saldo è ora distribuito su più zecche. Ad esempio, si potrebbero avere 1.000 Sats nella `Mint` di Minibits e altri 1.000 Sats in una `Mint` di Coinos. Questa separazione tra le diverse zecche è un aspetto importante dell'architettura di Cashu.


![image](assets/en/06.webp)


### Scambio di mentine


Se non vi fidate più di una particolare zecca che avete aggiunto, cashu.me offre una funzione per "scambiare" i fondi da una zecca all'altra. Navigate nella scheda delle zecche e scorrete verso il basso fino a vedere la voce `Scambio di zecche`. Selezionare la zecca `FROM` e `TO` dai menu a discesa e inserire l'importo che si desidera trasferire. Toccare `SWAP` per spostare i gettoni tra le zecche. Questa operazione sarà eseguita tramite una transazione Lightning, quindi è necessario lasciare spazio per le potenziali commissioni Lightning. Nel mio esempio, 1 sat è stato sufficiente.


![image](assets/en/07.webp)


## 3️⃣ Invio di fondi


Per inviare Sats, Cashu.me offre due opzioni. Inviare tramite `ecash` o tramite `lampo`. Diamo un'occhiata a entrambe le opzioni.


### Invio tramite Lightning


Per inviare tramite Lightning, procedere come segue:


1. Toccare "INVIA" nella schermata principale e selezionare "Fulmine"

2. L'applicazione chiederà di inserire un `Lightning Invoice` o un `Address`. È possibile incollare direttamente il Invoice/Address o utilizzare l'opzione di scansione del codice QR per catturarlo visivamente, quindi confermare con `INVIO`

3. Selezionare la zecca da cui si desidera pagare utilizzando il campo a discesa e toccare `PAY` per confermare. **Nota**: esiste anche un'opzione per utilizzare `Multinut` sotto `Impostazioni` -> `Sperimentale` che consente di pagare le fatture da più zecche contemporaneamente.

4. Una volta completato con successo, vedrete la conferma del pagamento e l'importo detratto dal vostro saldo.


![image](assets/en/08.webp)


### Invio tramite ecash


L'invio di ecash è altrettanto semplice.


1. Toccate `Invio` e questa volta selezionate l'opzione `ECASH`.

2. selezionare una zecca" e inserire l'"Importo" che si desidera inviare in Sats e toccare "Invia" per confermare

3. In questo modo si crea un `Codice QR animato` che può essere personalizzato regolando i parametri Velocità e Dimensione. Chiunque può eseguire la scansione di questo codice QR per ottenere immediatamente il Sats, oppure è possibile toccare COPIA per inviare la stringa token a qualcun altro attraverso canali alternativi come Bluetooth, NFC o messaggistica standard.

4. Apro un altro Wallet. Incollare dagli appunti e selezionare `Ricevi ecash` nell'altro Wallet.


![image](assets/en/09.webp)


## 4️⃣ Caratteristiche aggiuntive


Oltre alle funzionalità di base di invio e ricezione, Cashu.me offre potenti funzioni aggiuntive che migliorano l'esperienza del Bitcoin all'interno dell'ecosistema Nostr.


### Collegamento Nostr Wallet


Nostr Wallet Connect (`NWC`) trasforma il modo in cui si interagisce con le applicazioni Nostr creando una connessione perfetta tra il Wallet e le applicazioni sociali. Questo protocollo consente ad applicazioni come [Damus](https://damus.io/) o [Primal](https://primal.net/home) di richiedere pagamenti direttamente attraverso i relay Nostr senza richiedere l'uscita dall'app.


Per impostare `NWC` in Cashu.me:


1. Andare a "Impostazioni" nel menu Hamburger in alto a sinistra

2. Scorrere fino alla sezione `NOSTR Wallet CONNECT` e toccare il pulsante `Enable`

3. In seguito, si imposterà un'indennità per stabilire l'importo massimo che le applicazioni possono spendere dal proprio Wallet.

4. Una volta configurata, è possibile copiare la stringa di connessione e incollarla in qualsiasi client Nostr che supporti `NWC`, abilitando la funzionalità di zapping e tipping istantaneo.


![image](assets/en/10.webp)


### Fulmine Address via npub.cash


Cashu.me si integra con [npub.cash](https://npub.cash/) per fornire un Lightning Address che funziona perfettamente con il protocollo Nostr. Qui è possibile registrarsi e richiedere il proprio nome utente fornendo la propria `nsec` Nostr, che costa 5.000 Sats e supporta il progetto npub.cash, oppure è possibile utilizzare qualsiasi chiave pubblica Nostr (`npub`) senza registrazione.


Per prima cosa, andare su `Impostazioni` e toccare `Abilita` Lightning Address con npub.cash. In questo modo generate un npub.cash Address utilizzerà una stringa `npub` derivata dalla frase Wallet seed predefinita.


In alternativa, visitate [questa pagina web](https://npub.cash/username) per richiedere un nome utente personalizzato utilizzando il vostro Nostr `nsec`, ottenendo un Lightning Address personalizzato come username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Conclusione


Cashu.me offre pagamenti privati Bitcoin che funzionano come i contanti fisici - istantaneamente e peer-to-peer senza esporre la cronologia delle transazioni. Personalmente apprezzo la sua architettura PWA perché opera senza limitazioni di app store. Combinando la sicurezza del Bitcoin, la velocità di Lightning e la privacy dell'ecash, il Wallet offre casi d'uso che potrebbero migliorare l'adozione quotidiana del Bitcoin.


Sebbene si abbia il pieno controllo dei propri gettoni ecash attraverso l'autodeposito, si ricordi che le zecche agiscono come terze parti fidate che detengono le riserve Bitcoin sottostanti. La possibilità di utilizzare più zecche e di passare da una all'altra offre flessibilità, pur mantenendo la privacy.


Grazie a funzionalità come gli indirizzi NWC e npub.cash, Cashu.me è un'opzione Wallet interessante per i clienti sociali che apprezzano la privacy e la sovranità rispetto alle restrizioni delle politiche delle grandi tecnologie.


## 📚 Risorse


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)
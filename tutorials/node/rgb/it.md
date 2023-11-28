---
name: RGB
description: Introduzione e creazione di asset su RGB
---

![RGB vs Ethereum](assets/0.png)

## Introduzione

Il 3 gennaio 2009 Satoshi Nakamoto ha lanciato il primo nodo Bitcoin, da quel momento nuovi nodi si sono uniti e Bitcoin ha iniziato a comportarsi come se fosse una nuova forma di vita, una forma di vita che non ha smesso di evolversi, pian piano è diventata la rete più sicura al mondo grazie al suo design unico, molto ben pensato da Satoshi, che attraverso incentivi economici attira gli utenti comunemente chiamati minatori a investire in energia e potenza di calcolo, contribuendo così alla sicurezza della rete.

Man mano che Bitcoin continua a crescere e ad essere adottato, affronta problemi di scalabilità, la rete Bitcoin consente di estrarre un nuovo blocco con transazioni in un tempo approssimativo di 10 minuti, supponendo che abbiamo 144 blocchi in un giorno con valori massimi di 2700 transazioni per blocco, Bitcoin consentirebbe solo 4,5 transazioni al secondo, Satoshi era consapevole di questa limitazione, possiamo vederlo in una email1 inviata a Mike Hearn nel marzo 2011 in cui spiega come funziona ciò che oggi conosciamo come un canale di pagamento. micropagamenti in modo rapido e sicuro senza dover attendere conferme. È qui che entrano in gioco i protocolli off-chain.

Secondo Christian Decker2, i protocolli off-chain sono di solito sistemi in cui gli utenti utilizzano dati da una blockchain e li gestiscono senza toccare la blockchain stessa fino all'ultimo minuto. Basandosi su questo concetto, è nata la Lightning Network, una rete che utilizza protocolli off-chain per consentire pagamenti Bitcoin quasi istantanei e poiché non tutte queste operazioni vengono scritte sulla blockchain, consente migliaia di transazioni al secondo e scala Bitcoin.

La ricerca e lo sviluppo nell'ambito dei protocolli off-chain su Bitcoin hanno aperto una scatola di Pandora, oggi sappiamo che possiamo ottenere molto di più che il trasferimento di valore in modo decentralizzato, la non-profit LNP/BP Standards Association si concentra sullo sviluppo di protocolli di livello 2 e 3 su Bitcoin e sulla Lightning Network, tra questi progetti spicca RGB.

## Cos'è RGB?

RGB è emerso dalla ricerca di Peter Todd3 su sigilli monouso e convalida lato client, che è stato coniato nel 2016-2019 da Giacomo Zucco e dalla comunità in un protocollo di asset migliore per Bitcoin e la rete Lightning. L'ulteriore evoluzione di queste idee ha portato allo sviluppo di RGB in un sistema di smart contract completo da parte di Maxim Orlovsky, che ne guida l'implementazione dal 2019 con la partecipazione della comunità.

Possiamo definire RGB come un insieme di protocolli open source che ci permette di eseguire smart contract complessi in modo scalabile e confidenziale. Non è una rete particolare (come Bitcoin o Lightning); ogni smart contract è semplicemente un insieme di partecipanti al contratto che possono interagire utilizzando diversi canali di comunicazione (con predefinizione sulla rete Lightning). RGB utilizza la blockchain di Bitcoin come livello di impegno dello stato e mantiene il codice dello smart contract e i dati off-chain, il che lo rende scalabile, sfruttando le transazioni di Bitcoin (e Script) come sistema di controllo della proprietà per gli smart contract; mentre l'evoluzione dello smart contract è definita da uno schema off-chain, infine è importante notare che tutto viene convalidato lato client.

In termini semplici, RGB è un sistema che consente all'utente di verificare, eseguire e auditare un contratto intelligente individualmente in qualsiasi momento senza costi aggiuntivi, poiché non utilizza una blockchain come fanno i sistemi "tradizionali". I complessi sistemi di contratti intelligenti sono stati introdotti da Ethereum, ma a causa della necessità per l'utente di spendere quantità significative di gas per ogni operazione, non hanno mai raggiunto la scalabilità promessa e di conseguenza non sono mai stati un'opzione per i soggetti esclusi dal sistema finanziario attuale.

Attualmente, l'industria delle blockchain promuove che sia il codice dei contratti intelligenti che i dati debbano essere memorizzati nella blockchain ed eseguiti da ogni nodo della rete, indipendentemente dall'aumento eccessivo delle dimensioni o dall'abuso delle risorse computazionali. Lo schema proposto da RGB è molto più intelligente ed efficiente poiché rompe il paradigma della blockchain separando i contratti intelligenti e i dati dalla blockchain, evitando così la saturazione della rete riscontrata in altre piattaforme e non obbligando ogni nodo ad eseguire ogni contratto, ma solo le parti coinvolte, il che aggiunge un livello di riservatezza mai visto prima.

![RGB vs Ethereum](assets/1.png)

## Contratti intelligenti in RGB

In RGB, lo sviluppatore di contratti intelligenti definisce uno schema che specifica le regole secondo cui il contratto si evolve nel tempo. Lo schema è lo standard per la costruzione di contratti intelligenti in RGB e sia un emittente che definisce un contratto per l'emissione, sia un portafoglio o uno scambio devono conformarsi a uno schema particolare contro cui devono convalidare il contratto. Solo se la convalida è corretta, ogni parte può accettare le richieste e lavorare con l'asset.

Un contratto intelligente in RGB è un grafo aciclico diretto (DAG) di cambiamenti di stato, in cui solo una parte del grafo è sempre nota e non vi è accesso al resto. Lo schema RGB è un insieme di regole fondamentali per l'evoluzione di questo grafo con cui inizia il contratto intelligente. Ogni partecipante al contratto può aggiungere a queste regole (se consentito dallo schema) e il grafo risultante viene costruito dall'applicazione iterativa di tali regole.

## Asset fungibili

Gli asset fungibili in RGB seguono la specifica LNPBP RGB-20, quando viene definito un RGB-20, i dati dell'asset noti come "dati di genesi" vengono distribuiti attraverso la rete Lightning, che contiene ciò che è necessario per utilizzare l'asset. La forma più basilare degli asset non consente l'emissione secondaria, la distruzione dei token, la rinominazione o la sostituzione.

A volte l'emittente avrà bisogno di emettere più token in futuro, ad esempio stablecoin come USDT, che mantiene il valore di ogni token legato al valore di una valuta inflazionistica come il dollaro statunitense. Per raggiungere questo obiettivo, esistono schemi RGB-20 più complessi, che oltre ai dati di genesi richiedono all'emittente di produrre spedizioni, che circoleranno anche nella rete Lightning; con queste informazioni possiamo conoscere l'offerta circolante totale dell'asset. Lo stesso vale per gli asset distrutti o per il cambio di nome.

Le informazioni relative all'asset possono essere pubbliche o private: se l'emittente richiede riservatezza, può scegliere di non condividere informazioni sul token e svolgere operazioni in assoluta privacy, ma abbiamo anche il caso opposto in cui l'emittente e i detentori hanno bisogno che l'intero processo sia trasparente. Questo viene realizzato condividendo i dati del token.

## Procedure RGB-20

La procedura di distruzione disabilita i token, i token distrutti non possono più essere utilizzati.

La procedura di sostituzione si verifica quando i token vengono distrutti e viene creato un nuovo importo dello stesso token. Ciò aiuta a ridurre le dimensioni dei dati storici dell'asset, il che è importante per mantenere la velocità dell'asset.

Per supportare il caso d'uso in cui è possibile distruggere asset senza doverli sostituire, viene utilizzato un sottoschema di RGB-20 che consente solo la distruzione degli asset.

## Asset non fungibili

Gli asset non fungibili in RGB seguono la specifica LNPBP RGB-21, quando lavoriamo con NFT abbiamo anche uno schema principale e uno schema secondario. Questi schemi hanno una procedura di incisione, che ci permette di allegare dati personalizzati da parte del proprietario del token, l'esempio più comune che vediamo oggi nei NFT è l'arte digitale collegata al token. L'emittente del token può vietare questa incisione dati utilizzando lo schema secondario RGB-21. A differenza di altri sistemi blockchain NFT, RGB permette di distribuire dati di token di media di grandi dimensioni in modo completamente decentralizzato e resistente alla censura, utilizzando un'estensione alla rete P2P Lightning chiamata Bifrost, che viene utilizzata anche per costruire molte altre forme di funzionalità di contratti intelligenti specifici di RGB.

Oltre agli asset fungibili e agli NFT, RGB e Bifrost possono essere utilizzati per produrre altre forme di contratti intelligenti, inclusi DEX, pool di liquidità, stablecoin algoritmiche, ecc., che tratteremo in futuri articoli.

## NFT da RGB vs NFT da altre piattaforme

- Non c'è bisogno di costosi spazi di archiviazione blockchain
- Non c'è bisogno di IPFS, viene utilizzata invece un'estensione della rete Lightning (chiamata Bifrost) (ed è completamente crittografata end-to-end)
- Non c'è bisogno di una soluzione speciale di gestione dei dati, ancora una volta Bifrost svolge quel ruolo
- Non c'è bisogno di fidarsi dei siti web per mantenere i dati per i token NFT o sugli asset / ABI dei contratti
- Crittografia DRM integrata e gestione della proprietà
- Infrastruttura per i backup utilizzando la rete Lightning (Bifrost)
- Modo per monetizzare i contenuti (non solo vendendo l'NFT stesso, ma l'accesso ai contenuti, più volte)

## Conclusioni

Dalla nascita di Bitcoin, quasi 13 anni fa, ci sono state molte ricerche e sperimentazioni in questo campo, sia i successi che gli errori ci hanno permesso di capire un po' di più come si comportano i sistemi decentralizzati nella pratica, cosa li rende veramente decentralizzati e quali azioni tendono a portarli verso la centralizzazione, tutto ciò ci ha portato a concludere che la vera decentralizzazione è un fenomeno raro e difficile da raggiungere, la vera decentralizzazione è stata raggiunta solo da Bitcoin ed è per questo motivo che concentriamo i nostri sforzi per costruire sopra di esso.

RGB ha la sua tana del coniglio all'interno della tana del coniglio di Bitcoin, mentre sto cadendo attraverso di loro pubblicherò ciò che ho imparato, nel prossimo articolo avremo un'introduzione ai nodi LNP e RGB e come utilizzarli.

- 1 https://plan99.net/~mike/satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md

# Tutorial di RGB-node

## Introduzione

In questo tutorial spieghiamo come utilizzare RGB-node per creare un token fungibile e come trasferirlo, questo documento si basa sulla demo di RGB-node e si differenzia perché questo tutorial utilizza dati reali di testnet e per questo motivo dobbiamo costruire la nostra transazione Bitcoin parzialmente firmata, psbt da ora in poi.

## Requisiti

L'uso di una distribuzione Linux è consigliato, questo tutorial è stato scritto utilizzando Pop!/\_OS, che si basa su Ubuntu e avrai bisogno di:

- cargo
- Bitcoin core
- git

Nota: Questo tutorial mostra l'esecuzione di comandi in un terminale Linux, per differenziare ciò che l'utente scrive e la risposta che riceve nel terminale, includiamo il simbolo $ che simboleggia il prompt bash.

Dovrai installare alcune dipendenze:

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

Compila ed Esegui

RGB-node è un lavoro in corso (WIP), ecco perché dobbiamo posizionarci in un commit specifico (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) per poterlo compilare e utilizzare correttamente, per questo eseguiamo i seguenti comandi.

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

Ora lo compiliamo, non dimenticare di utilizzare l'opzione --locked perché è stata introdotta una modifica importante in una versione di clap.

```
$ cargo install --path . --all-features --locked

....
....
    Finished release [optimized] target(s) in 2m 14s
  Installing /home/user/.cargo/bin/fungibled
  Installing /home/user/.cargo/bin/rgb-cli
  Installing /home/user/.cargo/bin/rgbd
  Installing /home/user/.cargo/bin/stashd
   Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```

Come ci indica il compilatore Rust, i binari sono stati copiati nella directory $HOME/.cargo/bin, se il tuo compilatore li ha copiati in un'altra posizione, assicurati che quella directory sia inclusa in $PATH.

Tra i binari installati possiamo vedere tre daemon o servizi (i file che terminano con d) e una cli (interfaccia a riga di comando), la cli ci permette di interagire con il main daemon rgbd. Poiché in questo tutorial eseguiremo due nodi, avremo bisogno anche di due client, ognuno dei quali deve connettersi al proprio nodo, per questo creiamo due alias.

```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

Possiamo semplicemente eseguire gli alias o aggiungerli alla fine del file $HOME/.bashrc e eseguire source $HOME/.bashrc.
Premessa

RGB-node non gestisce alcun tipo di funzionalità legata al portafoglio, esegue solo compiti specifici di RGB sui dati che verranno forniti da un portafoglio esterno come bitcoin core. In particolare, per dimostrare un flusso di lavoro di base con emissione e trasferimento, avremo bisogno di:

- Un issuance_utxo a cui rgb-node-0 assocerà il nuovo asset emesso
- Un receive_utxo in cui rgb-node-1 riceve l'asset
- Un change_utxo in cui rgb-node-0 riceve il resto dell'asset
- Una transazione bitcoin parzialmente firmata (tx.psbt), la cui chiave pubblica di output verrà modificata per includere un impegno al trasferimento.
  Utilizzeremo il bitcoin core cli, dobbiamo avere il daemon bitcoind in esecuzione su testnet, questo ci darà interoperabilità e alla fine saremo in grado di inviare i nostri asset personali ad altri utenti RGB che hanno seguito questo tutorial.
  Per semplicità, aggiungeremo questo alias alla fine del nostro file ~/.bashrc.

```
alias bcli="bitcoin-cli -testnet"
```

Elenchiamo le nostre transazioni di output non spese e ne selezioniamo due, una sarà l'issuance_utxo e l'altra change_utxo, non importa quale sia quale, l'importante è che l'emittente abbia il controllo di questi due UTXO.

```
$ bcli listunspent
[
  {
    "txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
    "vout": 1,
    "address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
    "label": "",
    "scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
    "amount": 0.01703963,
    "confirmations": 62432,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
    "safe": true
  },
  {
    "txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
    "vout": 1,
    "address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
    "scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
    "amount": 0.02877504,
    "confirmations": 189184,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
    "safe": true
  }
]
```

Prima di andare avanti, dobbiamo parlare degli outpoints, una singola transazione può includere più output, l'outpoint include sia un TXID di 32 byte che un numero di indice di output di 4 byte (vout) per fare riferimento a un output specifico separato da due punti :. Nella nostra lista di output non spesi possiamo trovare due UTXO, su ognuno possiamo vedere txid e vout, quelli sono gli outpoints issuance_utxo e change_utxo.
receive_utxo è un UTXO controllato dal destinatario, in questo caso useremo e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 che è un outpoint da un altro portafoglio.

- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Ora creeremo una transazione parzialmente firmata (tx.psbt) il cui output verrà modificato per includere un impegno di trasferimento, ricordati di sostituire il txid e il vout con i tuoi, l'indirizzo di destinazione non importa davvero, può essere il tuo o può essere di un'altra persona, non importa dove vanno quei satoshi, ciò che importa è che usiamo issuance_utxo.

```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
  "psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
  "fee": 0.00000280,
  "changepos": 0'
'}

```

L'output ci ha fornito un psbt in codifica base64 che useremo per creare tx.psbt.

```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```

Creiamo una nuova directory chiamata rgbdata in cui vengono memorizzate le directory dei dati di ogni nodo.

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

Già posizionati in $HOME/rgbdata avviamo ogni nodo in terminali diversi, dove ~/.cargo/bin è la directory in cui cargo ha copiato tutti i binari dopo l'installazione di rgb-node.

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

## Emissione

Per emettere un asset eseguiamo rgb0-cli con i sottocomandi di emissione fungibile, quindi gli argomenti, il ticker USDT, il nome "USD Tether" e nell'allocazione utilizzeremo l'importo di emissione e l'issuance_utxo come vediamo di seguito:

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

Asset emesso con successo. Utilizza queste informazioni per la condivisione:
Informazioni sull'asset:

```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    amount: 1000
    origin: ~
knownInflation: {}
knownAllocations:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    index: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    revealedAmount:
      value: 1000
      blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```

Otteniamo l'assetId, ne abbiamo bisogno per trasferire l'asset.

```
$ rgb0-cli fungible list

- name: USD Tether
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```

## Genera UTXO oscurato

Per poter ricevere i nuovi USDT, rgb-node-1 deve generare un UTXO oscurato corrispondente a receive_utxo per contenere l'asset.

```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Outpoint oscurato: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Segreto di oscuramento dell'outpoint: 1679197189805229975
```

Per poter accettare trasferimenti relativi a questo UTXO, avremo bisogno del receive_utxo originale e del blinding_factor.

## Trasferimento

Per trasferire una certa quantità dell'asset a rgb-node-1, dobbiamo inviarlo all'UTXO oscurato, rgb-node-0 deve creare una consignment e una disclosure, e commetterle in una transazione bitcoin. Successivamente avremo bisogno di un psbt che modificheremo per includere il commit. Inoltre, le opzioni -i e -a ci consentono di fornire un outpoint di input che sarà l'origine dell'asset e un'allocazione in cui riceveremo il resto, dobbiamo indicarlo nel seguente modo @<change_utxo>.

```
'$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
Il trasferimento è riuscito, le spedizioni e la divulgazione sono scritte in "consignment.rgb" e "disclosure.rgb", la transazione del testimone parzialmente firmata in "witness.psbt"'
Dati di spedizione da condividere: consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e'
```

Questo scriverà tre nuovi file, consignment, disclosure e il psbt incluso il tweak, questo psbt è chiamato transazione dei testimoni, la consignment viene inviata a rgb-node-1.

## Testimoni

La transazione dei testimoni dovrebbe essere firmata e trasmessa, per questo dobbiamo codificarla nuovamente in base64.

```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

Firmalo con il sottocomando walletprocesspsbt.

```
`$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="{'`

`$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="{'`
'"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",  "complete": true
}
```

Ora finalizzalo e ottieni l'hex.

```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{
  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}
```

## Trasmissione

Trasmettilo utilizzando il sottocomando sendrawtransaction per confermarlo nella blockchain.

## Accettare

Per accettare un trasferimento in entrata, rgb-node-1 deve aver ricevuto il file di consegna da rgb-node-0, avere l'utxo di ricezione e il corrispondente blinding_factor generato durante la generazione dell'utxo di occultamento.

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975
```

Trasferimento dell'asset accettato con successo.

Ora possiamo vedere (nel campo knownAllocations) la nuova allocazione di 100 unità di asset in <receive_utxo> eseguendo:

```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT'
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
  amount: 1000
  origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
  index: 0
  outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
  revealedAmount:
    value: 1000
    blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
  index: 1
  outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
  revealedAmount:
    value: 100
    blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```

Since receive_utxo was blinded when the transfer was made, the payer rgb-node-0 has no information about where the 100 USDT was sent, so the location is not shown in knownAllocations.

```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0'
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6  ticker: USDT
  name: USD Tether
  description: ~
  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```

Ma come puoi vedere, rgb-node-0 non può vedere il cambio di 900 asset che abbiamo fornito al comando di trasferimento con l'argomento -a. Per registrare il cambio, rgb-node-0 deve accettare la divulgazione.

```
$ rgb0-cli fungible enclose disclosure.rgb

Dati di divulgazione chiusi con successo.
```

Se rgb-node-0 ha avuto successo, puoi vedere il cambio elencando l'asset.

```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
  name: USD Tether'
descrizione: ~  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
    - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      index: 0
      outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
      revealedAmount:
        value: 900
        blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```

## Conclusioni

Siamo stati in grado di creare un asset fungibile e spostarlo da una transazione all'altra in modo privato, se controlliamo la transazione confermata in un esploratore di blocchi non troveremmo nulla di diverso da una transazione normale, questo grazie al fatto che RGB utilizza sigilli monouso per modificare le transazioni. In questo post, faccio un'introduzione su come funziona RGB.

Questo post potrebbe contenere errori, se ne trovi qualcosa per favore fammelo sapere per migliorare questa guida, suggerimenti e critiche sono anche benvenuti, buon hacking! 🖖

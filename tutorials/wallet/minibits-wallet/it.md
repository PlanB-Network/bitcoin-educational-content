---
name: Minibits Wallet
description: Guida per Minibit Wallet
---

![cover](assets/cover.webp)


In questo tutorial vi guiderò nella configurazione di Minibits Wallet per l'utilizzo di ecash. Una potente tecnologia di pagamento incentrata sulla privacy che funziona insieme a Bitcoin. Minibits è un Wallet ecash e Lightning che consente trasferimenti di valore istantanei, economici e privati, rendendolo ideale per le transazioni quotidiane in cui la privacy è importante.


Prima di immergerci nei Minibit, cerchiamo di capire bene cosa sia e cosa non sia l'ecash. Molte persone confondono l'ecash con la tecnologia Bitcoin o Blockchain, ma si tratta di concetti fondamentalmente diversi.


Ecash NON è Bitcoin. Non sostituisce il vostro Bitcoin Wallet autocustodito, ma lo integra. Ecash non è un Blockchain e non vive in nessun Ledger pubblico. È interessante notare che l'ecash non è una nuova tecnologia: in realtà è precedente al web mondiale, con concetti sviluppati negli anni Ottanta e Novanta.


Che cos'è l'ecash: incredibilmente privato (le transazioni non lasciano traccia), peer-to-peer (trasferimenti diretti senza intermediari) e funziona come uno strumento digitale al portatore (se lo si possiede, lo si controlla). Un vantaggio fondamentale è che l'ecash può essere utilizzato offline: sia il mittente che il destinatario possono essere disconnessi da Internet durante le transazioni. Ecash può essere coniato da un singolo soggetto o da una federazione di entità fidate ed è una tecnologia perfettamente complementare al Bitcoin, in quanto gestisce transazioni piccole e frequenti mentre il Bitcoin funge da Layer di regolamento.


Si prega di notare che questa configurazione di Minibits rappresenta una `soluzione depositaria`, il che significa che vi state affidando all'operatore di Mint per gestire i vostri fondi. Ciò introduce rischi specifici che è necessario comprendere prima di procedere.


Il progetto riporta questo importante disclaimer:


- Questo Wallet deve essere utilizzato solo a scopo di ricerca.
- Il Wallet è una versione beta con funzionalità incomplete e bug noti e sconosciuti.
- Non utilizzatelo con grandi quantità di ecash.
- L'ecash immagazzinato nel Wallet viene emesso dalla zecca
- si confida nel fatto che la zecca la rifornisca di Bitcoin fino a quando non si trasferiscono i propri averi su un altro Bitcoin che illumina il Wallet.
- Il protocollo Cashu che il Wallet implementa non è ancora stato sottoposto a revisione o test approfonditi.


Trattate i Minibit come un Wallet di tutti i giorni, non come un conto di risparmio, e non conservate mai un valore significativo.


## 1️⃣ Impostazione del Wallet


Per iniziare, visitate il [Sito web di Minibits](https://www.minibits.cash/) dove troverete le opzioni di download per tutte le principali piattaforme. Gli utenti iOS possono scaricare da [App Store](https://testflight.apple.com/join/defJQgTD), mentre gli utenti iOS UE hanno l'ulteriore possibilità di installare da [Freedom Store](https://freedomstore.io/). Gli utenti Android possono ottenere l'applicazione da [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) o scaricare il file APK direttamente dalla pagina [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases).


Durante l'installazione di Minibit, vengono visualizzate delle schermate introduttive che spiegano i concetti di base: potete leggerle o saltarle se avete già familiarità con la tecnologia. Una volta completati questi passaggi iniziali, vi verrà chiesto di scegliere tra:


- `Capito, portami al Wallet` per i nuovi utenti o
- ripristina Wallet persi" se si sta ripristinando da un backup.


![image](assets/en/01.webp)

Dopo aver completato l'impostazione iniziale, si accede alla schermata iniziale, che presenta alcune importanti Elements indicazioni. ① L'icona del profilo nell'angolo in alto vi porta alla pagina del vostro profilo, dove potete accedere ai vostri Minibit Wallet Address e selezionare le opzioni di "ricezione in batch". ② Al centro dello schermo sono visualizzate le mentine che è possibile utilizzare, con la mentina Minibits selezionata per impostazione predefinita. ③ La riga di azione sottostante offre le opzioni per inviare pagamenti in ecash o lightning, scansionare un codice QR e ricevere pagamenti. infine, la barra di navigazione inferiore contiene collegamenti alla schermata iniziale, alla cronologia delle transazioni, ai contatti e alle impostazioni.


![image](assets/en/02.webp)


## 2️⃣ Gestire le mentine


Per impostazione predefinita, all'avvio dell'applicazione è abilitata la zecca Minibits. Tuttavia, uno dei punti di forza di ecash è la possibilità di utilizzare più zecche per aumentare la decentralizzazione e la sicurezza. Per aggiungere un'altra zecca, andare su `Impostazioni`, quindi selezionare `Gestione zecche` e infine toccare `Aggiungi zecca`.


[Bitcoinmints.com] (Bitcoinmints.com) fornisce un elenco completo delle zecche disponibili con le valutazioni degli utenti per aiutarvi a scegliere opzioni affidabili. L'utilizzo di più zecche riduce il rischio. Se una zecca ha problemi, i vostri fondi sulle altre zecche rimangono accessibili.


![image](assets/en/04.webp)


## 3️⃣ Creazione di un backup


Il backup è probabilmente la fase più critica dell'intero processo di configurazione. Per accedere alle opzioni di backup, andare su `Impostazioni`-> `Backup` Qui si trovano due opzioni essenziali:

1. la `sua frase seed`, che contiene `12 parole`, consente di recuperare il saldo di ecash in caso di perdita del dispositivo. Questa frase seed è la chiave principale per tutti gli ecash di tutte le zecche aggiunte. Scrivetela su un supporto fisico (carta o metallo) e conservatela in modo sicuro in più luoghi. Non conservate mai la frase seed in formato digitale, dove potrebbe essere compromessa. Visitate questo [tutorial](https://planb.network/en/tutorials/Wallet/backup/backup-Mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) per conoscere le migliori pratiche per la salvaguardia del vostro Wallet.

2. `Wallet backup` che contiene una lunga stringa di backup.


**Attenzione**: Quando si utilizza questo backup per ripristinare il Wallet, è comunque necessario disporre della frase del seed.


![image](assets/en/05.webp)


## 4️⃣ Creare minibit Wallet Address


Successivamente, andare su `Contatti` in basso e personalizzare il proprio `Minibits Wallet Address` toccando `Cambia` -> `Cambia Wallet Address`. Inserire il Address preferito e verificare la disponibilità.


![image](assets/en/07.webp)


Dopo aver impostato il proprio Address, verrà richiesta una piccola "donazione" per sostenere il progetto. Sebbene sia facoltativa, consiglio vivamente di prenderla in considerazione se si intende utilizzare il servizio regolarmente. I progetti open-source come Minibits si basano sul supporto della comunità per continuare lo sviluppo e la manutenzione. Anche un piccolo contributo aiuta a garantire la longevità del progetto.


![image](assets/en/08.webp)


## 5️⃣ Configurazione di Nostr


Se si desidera lasciare una mancia a chi si segue su Nostr, è possibile "aggiungere la chiave npub" selezionando "Contatti" e poi "Pubblico". In questo modo si collega il proprio Minibits Wallet alla rete sociale Nostr, consentendo di dare mance senza problemi.


Si può anche scegliere di "utilizzare il proprio profilo" andando su "Impostazioni" e poi su "Privacy" per importare il proprio Address e la propria chiave Nostr. Tuttavia, si tenga presente che in questo modo si impedisce al proprio Wallet di comunicare con i server Nostr e LNURL Address di minibits.cash, il che disabilita le funzioni lightning Address per la ricezione di zap e pagamenti.


![image](assets/en/09.webp)


## 6️⃣ Ricevere fondi


Per ricevere inizialmente i fondi, è necessario ricaricare il Wallet tramite un Invoice lightning. Il processo è semplice: toccare "Ricarica", inserire l'"Importo" che si desidera aggiungere, aggiungere facoltativamente un "Promemoria" e quindi toccare "Crea Invoice". Dovrete poi pagare questo Invoice utilizzando un altro Wallet Lightning, che converte i pagamenti Bitcoin Lightning in gettoni ecash all'interno del vostro Wallet Minibits.


![image](assets/en/10.webp)


## 7️⃣ Inviare fondi


Ora che avete finanziato il vostro Wallet, potete inviare fondi in due modi diversi.


### Inviare ecash


La prima opzione è quella di inviare direttamente ecash. Toccare "Invia", quindi selezionare "Invia ecash", inserire l'"Importo" e toccare "Crea token" per ottenere un codice QR da condividere con il destinatario o da far scansionare direttamente con il proprio dispositivo. Il destinatario vedrà apparire i gettoni nel suo Wallet quasi istantaneamente, senza spese Blockchain o ritardi di conferma.


![image](assets/en/11.webp)


### Pagare con Lightning


La seconda opzione è pagare con Lightning. Toccare "Invia", quindi selezionare "Paga con Lightning". È possibile scegliere tra i `contatti` di Nostr (se si è collegato il proprio npub), oppure inserire/incollare un codice di pagamento Lightning Address, Invoice o LNURL utilizzando l'opzione `Incolla` o `scansiona`. Dopo aver `confermato` il destinatario, vi verrà richiesto di inserire l'importo da pagare, di aggiungere un promemoria e di toccare `Conferma` seguito da `Paga ora` per completare la transazione Lightning.


![image](assets/en/12.webp)


## 8️⃣ Creare una connessione NWC


Un'altra potente caratteristica di Minibits è la possibilità di creare connessioni `Nostr Wallet Connect (NWC)`, che consentono ad altre applicazioni di richiedere pagamenti dal vostro Wallet senza esporre le vostre chiavi private.


Per impostarlo, andare su `Impostazioni`, quindi selezionare `Nostr Wallet Connect` e toccare `Aggiungi connessione`. Assegnate alla connessione un nome descrittivo che identifichi sia l'applicazione che l'account utente associato. Impostare un limite massimo giornaliero ragionevole per controllare quanto si può spendere attraverso questa connessione, quindi toccare `Salva` per completare l'impostazione.


Questa funzione è particolarmente utile per servizi come Nostr Clients, dove si desidera attivare la mancia automatica senza approvare manualmente ogni transazione.


![image](assets/en/12.webp)


## 🎯 Conclusione


Minibits rappresenta un punto di ingresso accessibile nel mondo dell'ecash, offrendo pagamenti incentrati sulla privacy che completano le vostre disponibilità di Bitcoin. Ricordate di mantenere sempre un backup adeguato, di considerare l'uso di più zecche per la ridondanza e di conservare solo quantità adeguate in questa soluzione di custodia.


Per ulteriori risorse, consultate il repository GitHub di Minibits, il sito web ufficiale e il loro canale Telegram, dove la comunità discute attivamente gli sviluppi e risolve i problemi


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Sito web](https://www.minibits.cash/)
- [Telegramma](https://t.me/MinibitsWallet)


L'ecosistema dell'ecash è ancora in evoluzione, ma strumenti come Minibits stanno rendendo questa potente tecnologia della privacy sempre più accessibile agli utenti comuni.
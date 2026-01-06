---
name: Bull Bitcoin Wallet
description: Scopri come utilizzare il Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Questo video tutorial di BTC Sessions illustra il processo di impostazione e utilizzo di Bull Bitcoin Wallet!


Questa guida illustra l'installazione, la configurazione e l'utilizzo di Bull Bitcoin Wallet. Imparerete a inviare e ricevere fondi sulle reti Bitcoin On-Chain, Liquid e Lightning, nonché a spostare il Bitcoin da una rete all'altra. Le numerose funzioni del wallet lo rendono uno strumento potente e completo per la gestione del vostro Bitcoin. Iniziamo.


## Introduzione


Bull Bitcoin Wallet, sviluppato da [Bull Bitcoin](https://www.bullbitcoin.com/), è un Bitcoin wallet **autocustode**, il che significa che avete il pieno controllo delle vostre chiavi private e quindi dei vostri fondi, senza dipendere da terzi. Open-source e radicato nella filosofia Cypherpunk, questo Wallet combina semplicità, riservatezza e funzionalità avanzate come gli swap tra reti e il supporto PayJoin. Consente di gestire i bitcoin su tre reti: **Bitcoin onchain**, **Liquid** e **Lightning**, ognuna adattata a usi specifici. Su [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), è possibile controllare gli argomenti attuali e i prossimi sviluppi. Poiché il progetto è al 100% open-source e "costruito in pubblico", è possibile inviare i propri suggerimenti e qualsiasi bug riscontrato. Mentre alcuni portafogli ora supportano più reti, il Bull Bitcoin Wallet si distingue per l'integrazione profonda delle funzioni di privacy in tutte le reti, che lo rende uno strumento potente per la gestione del Bitcoin in tutte le principali reti


## 1️⃣ Prerequisiti


Prima di iniziare a utilizzare il **Bull Bitcoin Wallet**, accertarsi di disporre dei seguenti elementi:



- Smartphone compatibile**: Un dispositivo **iOS** (iPhone o iPad) o **Android**
- Connessione a Internet
- Supporti di backup sicuri**: Scrivete la vostra **frase di recupero** (12 parole) su carta o metallo e conservatela in un luogo sicuro.
- Conoscenze di base**: È utile una conoscenza minima dei concetti di Bitcoin (indirizzi, transazioni, tariffe), anche se questo tutorial spiega ogni passaggio per i principianti.


## 2️⃣ Installazione


È possibile installare l'applicazione tramite:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(per dispositivi iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (per dispositivi Android)


Anche gli utenti Android hanno a disposizione opzioni alternative:



- Scaricare l'APK direttamente dalla pagina [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) oppure
- Installare tramite [Zapstore] compatibile con Nostr(https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Dopo aver installato l'applicazione, seguite la schermata di benvenuto per configurare il vostro account.


## 3️⃣ Configurazione iniziale


All'apertura, vengono richieste le seguenti opzioni:



- crea nuovo Wallet
- recupero Wallet" e
- opzioni avanzate


Cominciamo toccando "Opzioni avanzate".


Qui è possibile configurare le impostazioni avanzate prima di creare o ripristinare un wallet:


1. Abilitare il `proxy Tor` per instradare il traffico sulla rete Tor.

1. [Orbot app](https://orbot.app/en/) deve essere installata e funzionante prima di abilitare l'applicazione

2. Tor Proxy si applica solo al Bitcoin (non al Liquid) e può comportare una connessione più lenta.

2. Impostare un "Electrum Server personalizzato", oppure

3. Regolare le impostazioni di `Recover Bull`. In seguito, si approfondirà l'argomento [Recover Bull](https://recoverbull.com/).


Dopo aver effettuato tutte le regolazioni opzionali, toccare "Fatto". Se si desidera riutilizzare un Wallet esistente, fare clic su "Recupera Wallet" e inserire le 12 parole della frase di recupero.


Altrimenti, fare clic su "Crea un nuovo Wallet".


![image](assets/en/01.webp)


## 4️⃣ Schermata iniziale


Prima di approfondire, diamo un'occhiata alla "schermata iniziale" per orientarci:



- il menu "Panoramica delle transazioni" e "Impostazioni" si trova in alto.
- Il `bilancio disponibile` ha un'opzione di privacy che può essere `attivata o disattivata`.
- Accedere al `Bitcoin Bull Exchange` per `acquistare, vendere o pagare` (questo dipende dalla giurisdizione e può richiedere il KYC).
- trasferimento di fondi tra portafogli
- `Secure Bitcoin` equivale a Onchain Bitcoin Wallet
- pagamenti istantanei tramite Lightning / Liquid Network *(Nota: il Bull Bitcoin Wallet consente di effettuare e ricevere pagamenti tramite Lightning. I fondi ricevuti tramite Lightning sono memorizzati sulla [*rete Liquid](https://liquid.net/) (nei pagamenti istantanei Wallet) grazie a uno scambio automatico tramite [*scambio Boltz](https://boltz.exchange/). In questo modo è possibile interagire con Lightning senza dover gestire canali di liquidità, rimanendo in autodeposito.)*
- invio e ricezione di fondi


![image](assets/en/02.webp)


Per prima cosa, effettuiamo alcune configurazioni importanti e iniziamo con il `Backup`.


## 5️⃣ Backup


Per iniziare il processo di backup, toccare l'icona "ingranaggio" (⚙)` nell'angolo in alto a destra dell'applicazione e selezionare "Wallet Backup". Verranno presentati due metodi per proteggere il wallet: "Vault crittografato" e "Backup fisico". Esploriamo ciascuno di essi.


![image](assets/en/03.webp)


### Backup fisico


Toccate "Backup fisico" per visualizzare un elenco di 12 parole che rappresentano la vostra frase di recupero o seed . Considerate quanto segue:



- Scrivete la vostra "frase di recupero" con la massima cura. Scrivetela su carta o metallo e conservatela in un luogo sicuro (cassetta di sicurezza, luogo offline). Questa frase è l'unico mezzo per accedere ai bitcoin in caso di perdita del dispositivo o di cancellazione dell'applicazione.
- È anche importante notare che chiunque abbia questa frase può rubare tutti i vostri bitcoin. Non conservateli mai in formato digitale:
- Nessuna schermata
- Nessun backup su cloud, e-mail o messaggistica
- Nessun copia/incolla (rischio di salvare negli appunti)


![image](assets/en/25.webp)


Nella schermata successiva dovrete mettere le parole nell'ordine giusto per assicurarvi di aver azzeccato la frase seed. Al termine del test, si riceverà una conferma di successo.


! **Questo punto è fondamentale**. Per ulteriore assistenza :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Camera blindata criptata


Esiste anche l'opzione di un backup anonimo e crittografato nel cloud. Ma non abbiamo detto nell'ultimo paragrafo che i backup nel cloud sono rischiosi e dovrebbero essere evitati? Tuttavia, il team di Bull Bitcoin ha sviluppato un modo intelligente per rendere il processo sicuro. Ecco come funziona:


`Recoverbull` è un protocollo di backup che semplifica la protezione del Bitcoin wallet dividendo il backup in due parti. In primo luogo, il file di backup del wallet viene crittografato sul dispositivo utilizzando una chiave di crittografia forte. È possibile salvare questo file crittografato ovunque si desideri, ad esempio su Google Drive o sul proprio dispositivo. In secondo luogo, la chiave di crittografia necessaria per sbloccare il file è memorizzata dal Recoverbull Key Server. Per recuperare il vostro wallet, avete bisogno sia del file di backup crittografato che della chiave, a cui accedete con il vostro PIN o password. Questo design garantisce che il vostro backup nel cloud sia inutile da solo e che il server delle chiavi sia inutile senza il vostro file di backup specifico. In questo modo i vostri fondi sono al sicuro anche se una parte è compromessa.


Pensate a una cassetta di sicurezza. Il file di backup crittografato è la *scatola*, che potete archiviare ovunque (come Google Drive). Il PIN di recupero è la *chiave*, che viene memorizzata separatamente dal server delle chiavi di Recoverbull. Un ladro dovrebbe ottenere sia la vostra scatola specifica che la vostra chiave specifica per aprirla. Questo design assicura che anche se qualcuno ottiene il vostro file di backup, esso è inutile senza la chiave del server, e la chiave del server è inutile senza il vostro file di backup unico.


Per saperne di più sul protocollo di backup wallet di `Recoverbull` [qui](https://recoverbull.com/).


Toccare `Vault crittografato` e poi `Continua` per confermare l'utilizzo del server predefinito. La connessione sarà instradata attraverso la rete `Tor` per garantire la privacy e l'anonimato.


**Comprendere i PIN**



- pIN di sblocco dell'app**:** Il PIN opzionale impostato in `Impostazioni > PIN di sicurezza` per bloccare l'app sul telefono.
- pIN di ripristino**:** Il PIN obbligatorio creato durante il processo di backup del `Vault crittografato', utilizzato per decifrare il file di backup durante il ripristino.


Si tratta di due PIN distinti. Non dimenticate il PIN di ripristino, perché è essenziale per ripristinare il vostro wallet"


**Impostazione del PIN di recupero



- È necessario creare un PIN o una password per recuperare l'accesso al proprio wallet.
- Il PIN/Password deve essere di almeno 6 cifre (ad esempio, evitare sequenze semplici come 123456, che non sono accettate).
- Senza questo PIN, il recupero del wallet è impossibile.


Quindi, selezionare un provider di vault:



- google Drive" o
- una "posizione personalizzata" (ad esempio il proprio dispositivo)


![image](assets/en/04.webp)


A questo punto, salvare il "file di backup". Quindi, toccare `Test Recovery`, selezionare il file di backup o il vault salvato, quindi toccare `Decrypt Vault`. Immettere il `PIN` o la `Password`. Se tutto ha funzionato, apparirà la schermata `Test completato con successo`.


### Etichette di importazione/esportazione


Ora che abbiamo creato il nostro backup, diamo un'occhiata alle "etichette".  Il Bull Bitcoin wallet migliora la privacy e l'organizzazione consentendo agli utenti di creare etichette personalizzate per gli indirizzi di ricezione e le transazioni. Queste etichette aiutano a classificare i fondi, poiché le transazioni inviate a un indirizzo etichettato erediteranno quell'etichetta, e si possono anche etichettare le transazioni in uscita per tenere traccia dei loro cambiamenti. Il wallet supporta pienamente lo standard [BIP-329](https://bip329.org/), il che significa che potete esportare tutte le vostre etichette in un file e importarle in un altro wallet. Questa funzione consente di eseguire il backup della cronologia delle transazioni e delle categorizzazioni o di migrarle tra diverse istanze del wallet senza perdere l'organizzazione personalizzata.


![image](assets/en/05.webp)


## 6️⃣ Impostazioni


Dopo aver messo al sicuro il backup primario, esploriamo le altre funzioni disponibili nelle impostazioni.


### A - Protezione dell'accesso


Per proteggere l'applicazione, andare su "Impostazioni" e scegliere "PIN di sicurezza" per selezionare il codice PIN. Creare un PIN forte per bloccare l'accesso al proprio wallet. Anche se questo passaggio è facoltativo, è altamente raccomandato per evitare accessi non autorizzati se qualcun altro usa il telefono.


![image](assets/en/06.webp)


### B - Connessione a un nodo personale (opzionale)


Il Wallet BullBitcoin si connette di default ai server Electrum: il primo gestito da Bull Bitcoin e un server secondario di Blockstream, entrambi considerati privi di registri, riducendo il rischio di tracciamento.


Per maggiore riservatezza, è possibile collegare l'applicazione al proprio nodo Bitcoin tramite un server Electrum. A tale scopo, toccare `Impostazioni` > `Impostazioni Bitcoin` > `Impostazioni Electrum Server`, quindi toccare `+ Aggiungi server personalizzato` per inserire l'indirizzo e le credenziali del server.


![image](assets/en/07.webp)


### C - Valuta


Il saldo disponibile viene visualizzato nella schermata principale sia in `sats` che in `USD`. Per modificarlo, andare su `Impostazioni` > `Valuta`. Qui è possibile passare da `sats/BTC` e selezionare la `valuta predefinita`.


![image](assets/en/08.webp)


### D - Impostazioni Bitcoin


Il menu `Impostazioni Bitcoin` offre un accesso approfondito alle configurazioni e ai dati principali del vostro wallet. Qui è possibile esaminare i dettagli fondamentali dei portafogli `Secure Bitcoin` e `Instant payments`, offrendo trasparenza e controllo completi. Le caratteristiche principali di questo menu includono:



- Dettagli Wallet:** Navigare al vostro Bitcoin sicuro o wallet con pagamento immediato per visualizzare le informazioni specifiche.
- Impronta digitale Wallet:** Un identificativo unico per il wallet.
- Chiave pubblica (Pubkey):** La chiave utilizzata per gli indirizzi di ricezione generate del vostro Bitcoin .
- Descriptor:** Un riassunto tecnico della struttura del vostro wallet.
- Percorso di derivazione:** Il percorso specifico utilizzato per generate tutti gli indirizzi dalla chiave privata principale.
- Vista Address:** Accesso all'elenco degli indirizzi di ricezione non utilizzati e modifica degli indirizzi (in arrivo)


Inoltre, avete la possibilità di:



- le impostazioni di `Abilitazione del trasferimento automatico` consentono di impostare un saldo massimo istantaneo wallet, che verrà poi trasferito automaticamente al wallet sicuro in bitcoin.
- Importazione di portafogli generici tramite la frase `Mnemonic` o l'importazione di `watch-only`
- Collegare "portafogli hardware": i dispositivi attualmente supportati sono ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade e Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Direttamente dal wallet, si ha accesso alla [borsa Bull Bitcoin](https://www.bullbitcoin.com/), che consente di acquistare, vendere e pagare il Bitcoin senza lasciare l'app. Questa integrazione offre una soluzione comoda per gestire le proprie esigenze di Bitcoin. Si prega di notare che l'accesso alla borsa e ai suoi servizi potrebbe essere limitato in base alla propria giurisdizione e che potrebbe essere necessario completare la verifica Know Your Customer (KYC) per conformarsi agli standard normativi e utilizzare tutte le funzionalità della piattaforma.


Per iniziare, toccare `Exchange` nell'angolo in basso a destra, quindi `Sign up` o `Login` al proprio account.


La borsa offre le seguenti [caratteristiche](https://www.bullbitcoin.com/):



- Acquistate il Bitcoin con l'autotutela dal vostro conto corrente bancario
- Non detentivo
- Persone fisiche o giuridiche
- Prelievo immediato
- Nessun costo nascosto
- Lightning Network disponibile
- Nessun limite alle transazioni
- Opzioni di acquisto ricorrenti


![image](assets/en/09.webp)


Per saperne di più, visitate questo tutorial:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Ricezione di fondi


La ricezione di fondi con **Bull Bitcoin Wallet** è semplice e flessibile e supporta tre reti distinte, adatte a diversi casi d'uso:



- La rete `Bitcoin (onchain)` per lo stoccaggio sicuro a lungo termine.
- La rete `Liquid` per transazioni veloci e più riservate.
- La rete `Lightning` per pagamenti istantanei e a basso costo.


L'applicazione genera automaticamente l'indirizzo o la fattura appropriati in base alla rete selezionata. Ecco come procedere per ogni rete.


### Ricezione tramite Onchain (rete Bitcoin)


Per ricevere i fondi on-chain, è possibile selezionare `Secure Bitcoin Wallet` dalla schermata principale e toccare `Receive`, oppure toccare il pulsante principale `Receive` e quindi scegliere la `rete Bitcoin`.


Esistono due modalità principali per generare un indirizzo di ricezione:


**Modalità predefinita (URI con parametri di input aggiuntivi)


Per impostazione predefinita, il wallet genera un [BIP21 URI](https://bips.dev/21/). Si tratta di un formato standardizzato che contiene più informazioni di un semplice indirizzo, tra cui un importo, una nota personale e parametri PayJoin per migliorare la privacy. Questo URI completo viene codificato in un codice QR e reso disponibile per la copia. Il formato è il seguente: `bitcoin:<indirizzo>?<parametro1>=<valore1>&<parametro2>=<valore2>`.



- Parametri di ingresso aggiuntivi:**
    - Importo:** Specificare l'importo richiesto in BTC, sats o una valuta fiat.
    - Messaggio:** Aggiungere una nota personale che sarà visibile al mittente.
    - PayJoin:** Abilitare questa opzione per migliorare la privacy combinando i dati del mittente e del destinatario nella transazione.


Esempio di URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Nota importante: si prega di non inviare fondi agli indirizzi di questo tutorial, il wallet verrà cancellato.*


![image](assets/en/10.webp)


**Opzione di copia o scansione solo Address attivata


Con l'opzione "Copia o scansione solo Address" abilitata, l'applicazione genera un semplice indirizzo Bitcoin in formato SegWit (bech32).


Esempio:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Anche se si inserisce un importo o una nota, questi non saranno inclusi nel codice QR o nell'indirizzo copiato.


![image](assets/en/11.webp)


### Ricezione tramite il Liquid Network


È possibile ricevere un pagamento sul Liquid Network. Nella schermata "Ricezione" sono disponibili le stesse due opzioni per generare una richiesta di pagamento:


**1. Address semplice:** Copiare l'indirizzo standard `Liquid`. Si tratta di un identificativo unico per il vostro wallet sulla rete Liquid e non include alcun importo o messaggio specifico.


Esempio Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Richiesta di pagamento dettagliata (URI):** Per una richiesta più strutturata, è possibile specificare un importo e una nota personale. Queste informazioni vengono automaticamente codificate in un URI condivisibile e nel codice QR corrispondente.



- Importo:** È possibile impostare l'importo in Bitcoin (BTC), Satoshi (Sats) o una valuta fiat.
- Nota: ** Aggiungere un messaggio personale per identificare la transazione.


**Esempio di URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Per completare la transazione, fornire al mittente l'"indirizzo" o l'"URL". È possibile farlo copiandolo negli appunti o facendo scansionare il codice QR direttamente dallo schermo.


![image](assets/en/12.webp)


### Ricezione tramite Lightning



Il Bull Bitcoin Wallet consente inoltre di inviare e ricevere pagamenti tramite il Lightning Network. Una caratteristica fondamentale è che i fondi ricevuti tramite Lightning vengono automaticamente scambiati e memorizzati sul `Liquid Network` all'interno del vostro `Instant Payments Wallet`. Questo servizio è alimentato dal `Boltz`. Questo design consente di usufruire della velocità e del basso costo di Lightning senza la complessità della gestione dei canali di liquidità, mantenendo la piena autocustodia dei fondi. Sebbene questo approccio ibrido sia autodepositante ed eviti la complessità della gestione dei canali, introduce un servizio di terze parti (Boltz), una piccola commissione di swap e la dipendenza dalla federazione di funzionari del Liquid Network come keyholder, che è diversa da quella di un Lightning wallet tradizionale, non depositario, in cui si gestiscono i propri canali. Per saperne di più sul Liquid e sul suo modello di governance, cliccate qui:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Limiti:**
    - Importo minimo:** È richiesto un importo minimo per la fattura. Controllare l'app per conoscere il limite attuale
    - Commissioni:** Il destinatario è responsabile di una piccola commissione di scambio. Questa commissione viene detratta dall'importo trasferito dal mittente ed è soggetta a modifiche
- Vantaggi:**
    - Autotutela:** I vostri fondi sono sempre sotto il vostro controllo, protetti dalla rete Liquid.
    - Evitare le alte commissioni On-Chain:** Utilizzando Lightning e archiviando su Liquid, si evitano le commissioni on-chain associate all'apertura di un canale Lightning tradizionale. È possibile scegliere di spostare i fondi in un canale on-chain in un secondo momento, quando l'importo accumulato giustifica la spesa.
    - Suggerimento:** Per la transazione più conveniente tra due utenti Bull Bitcoin, utilizzare direttamente la rete **Liquid** per evitare completamente le spese di scambio Lightning.


Per ricevere un pagamento, è necessario emettere una `fattura lampo`:


1. inserire un importo**:** Specificare l'importo che si desidera ricevere in Bitcoin (BTC), Satoshi (Sats) o una valuta fiat.

2. aggiungere una nota" **(Opzionale):** Includere un promemoria o una nota. Questa sarà incorporata nella fattura e visualizzata nella cronologia delle transazioni una volta completato il pagamento, rendendone più facile l'identificazione.

3. validità`**:** La fattura Lightning è sensibile al tempo e scade dopo **12 ore**. Se non viene pagata entro questo periodo, non è più valida e sarà necessario crearne una nuova.


Fornite al mittente la fattura copiandola negli appunti o facendo scansionare il codice QR visualizzato sullo schermo.


![image](assets/en/13.webp)


## 9️⃣ Invio di fondi


È possibile accedere alla schermata di invio direttamente dalla pagina iniziale o da qualsiasi portafoglio. Il Bull Bitcoin Wallet semplifica il processo rilevando automaticamente la rete di destinazione - `Bitcoin`, `Liquid` o `Lightning` - in base all'indirizzo o alla fattura inseriti, incollati o scansionati tramite codice QR.


### Trasmissione On-Chain tramite la rete Bitcoin


L'invio di fondi on-chain significa che la transazione viene registrata direttamente sulla blockchain Bitcoin. Questo metodo è migliore per i trasferimenti di grandi dimensioni o per quelli non sensibili ai tempi. Per iniziare, è possibile toccare il "pulsante di invio" in basso a destra e scansionare o inserire un "indirizzo Bitcoin standard".


Se l'indirizzo fornito non include un importo specifico, nella schermata di invio verrà richiesto di inserire i dettagli. È possibile specificare l'importo nell'unità di misura preferita, ad esempio BTC, satoshi o un equivalente fiat. È inoltre possibile aggiungere una nota personale, ovvero un promemoria privato per il proprio riferimento, che vi aiuterà a identificare la transazione in un secondo momento. Questa nota non viene condivisa con il destinatario.


Al contrario, se la richiesta di pagamento scansionata o incollata contiene già tutti i dettagli necessari, come ad esempio un URI BIP21 con un importo predefinito, il wallet ignorerà la schermata di inserimento dati e porterà direttamente alla schermata di conferma per autorizzare il pagamento.


![image](assets/en/14.webp)


Prima che la transazione venga trasmessa, vi verrà presentata una schermata di conferma. È fondamentale soffermarsi a esaminare attentamente ogni parametro, prestando particolare attenzione all'indirizzo del destinatario, all'importo inviato e alle commissioni di rete. Questa schermata fornisce anche potenti strumenti per personalizzare la transazione.


È possibile controllare le tariffe in due modi principali. Il primo metodo consiste nel selezionare la velocità di transazione desiderata, ad esempio bassa, media o alta, e il wallet calcolerà automaticamente la tariffa appropriata. Il secondo metodo permette un controllo più preciso, consentendo di impostare una tariffa specifica, sia come totale assoluto in satoshi che come tariffa relativa per byte, che fornisce poi un tempo di conferma stimato.


Per gli utenti avanzati, il wallet offre diverse impostazioni per regolare con precisione la transazione. il `Replace-by-Fee` (RBF) è abilitato per impostazione predefinita, una funzione preziosa che consente di accelerare una transazione se rimane bloccata nella mempool, ritrasmettendola con una tariffa più alta. È anche possibile selezionare manualmente gli `Usciti di transazione non spesi` (UTXO) da cui spendere. Si tratta di un potente strumento per il consolidamento UTXO, una strategia che consiste nel combinare più ingressi di piccole dimensioni in un unico ingresso più grande. Sebbene questo possa costare di più in termini di commissioni per la transazione corrente, può ridurre significativamente le commissioni sulle transazioni future, soprattutto se si prevede un aumento delle commissioni di rete.


![image](assets/en/15.webp)


PayJoin viene tentato automaticamente quando si scansiona una richiesta di pagamento del destinatario (un URI BIP21) che include un parametro `pj=`. Se si incolla semplicemente un indirizzo semplice senza parametri aggiuntivi, questa funzione non verrà attivata. Questo metodo collaborativo migliora la privacy combinando gli input sia del mittente che del destinatario, rompendo l'euristica della proprietà comune degli input e consentendo, in alcune circostanze, una migliore scalabilità e un risparmio sulle tariffe.


### Invio al Liquid Network


Il `Liquid Network` è progettato per transazioni rapide e riservate con commissioni minime. Quando si inviano fondi tramite Liquid, questi vengono prelevati dal proprio `Pagamenti istantanei Wallet`. Il processo è semplice: è sufficiente inserire o scansionare l'indirizzo `Liquid` del destinatario.


Se l'indirizzo non specifica un importo, vi verrà chiesto di fornirne uno nella schermata di invio. È possibile inserire l'importo in BTC, satoshis o fiat. Un vantaggio fondamentale di Liquid è la sua bassa soglia minima. Come per le transazioni on-chain, è possibile aggiungere una nota personale opzionale per i propri dati. Se la richiesta di pagamento include già un importo, il wallet passerà direttamente alla schermata di conferma.


Nella schermata di conferma di una transazione Liquid, è possibile esaminare i dettagli. Le commissioni sono notevolmente basse e vengono calcolate in base alla complessità della transazione. In genere si aggirano intorno a 0,1 sat/vB, che per una transazione semplice equivalgono a soli 20-40 satoshis (ad esempio, 26 satoshis al 21 dicembre 2025).


![image](assets/en/16.webp)


### Invio al Lightning Network


È possibile scansionare una Address Lightning (ad esempio `runningbitcoin@rizful.com`) che consente di impostare l'importo e una nota opzionale per il destinatario, oppure scansionare una fattura con un importo predefinito, che porta direttamente alla schermata di conferma.


*Si noti che si applicano importi minimi e commissioni.*


Il Bull Bitcoin Wallet invia pagamenti Lightning prelevando i fondi dal vostro `Pagamenti istantanei Wallet` (sul Liquid) e scambiandoli tramite il `Boltz`. Questo approccio ibrido è completamente autonomo ed evita le elevate spese di gestione di un canale Lightning dedicato da parte del on-chain, ma richiede il pagamento di una "commissione di scambio". Per ottenere il costo più basso, inviate direttamente all'indirizzo Liquid di un destinatario che utilizza anche un Bull Bitcoin wallet.


## 🔟 Trasferimento di fondi tra i portafogli


Il Bull Bitcoin consente di spostare il proprio Bitcoin tra il proprio `Secure Bitcoin` wallet e il proprio `Instant Payments Wallet` sul Liquid Network o su un `Wallet` esterno. Per eseguire un trasferimento, è sufficiente navigare nella sezione `Trasferimento`, selezionare i portafogli di origine e di destinazione, inserire l'importo che si desidera spostare e confermare la transazione.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Recupero del Bull Bitcoin Wallet


Questa sezione spiega come recuperare l'accesso ai fondi del Bull Bitcoin Wallet in caso di smarrimento del dispositivo, disinstallazione dell'applicazione o semplicemente per passare a un nuovo dispositivo. Come già spiegato, esistono due metodi principali per il recupero: il metodo unico `Recoverbull` e la frase standard `BIP39 seed`.


### Metodo 1: Recoverbull


Riconoscimento: I backup di Wallet sono crittografati localmente. Il file crittografato può essere archiviato nel cloud storage o su un altro dispositivo. La chiave di crittografia è memorizzata dal server chiave di Recoverbull. Entrambi sono tenuti separati e devono essere combinati per recuperare un wallet.


Per iniziare, cancellerò il Wallet con tutti i fondi presenti e reinstallerò il wallet. Arriveremo di nuovo alla "schermata di benvenuto". Questa volta, selezionare l'opzione `Recover Wallet`. Quindi, passare al metodo `Vault crittografato`, confermare l'uso del `Server chiave predefinito` e selezionare la posizione o il `Vault provider` in cui è stato memorizzato il file di backup.


![image](assets/en/18.webp)


Il messaggio indica che il vault è stato importato con successo. Toccare il pulsante `Decrypt Vault` e inserire il `PIN`. La schermata successiva mostrerà i "saldi" e il "numero di transazioni" recuperate.


![image](assets/en/19.webp)


### Metodo 2: Frase seme


Questo metodo utilizza la frase di recupero principale del wallet, un elenco standard di 12 parole che funge da backup definitivo per i fondi. È il metodo più universale per recuperare un Bitcoin wallet, poiché non è legato a nessun servizio o server specifico. Finché si dispone di questa frase, è possibile ripristinare il proprio wallet su qualsiasi dispositivo compatibile, anche senza accesso al server delle chiavi Bull Bitcoin.


Dalla schermata di benvenuto, selezionare `Recover Wallet`. Questa volta, scegliere il metodo "Backup fisico". L'applicazione presenterà una griglia di parole. Selezionare attentamente ogni parola della frase seed di 12 parole nell'ordine corretto. Siate meticolosi, perché un solo errore darà luogo a un wallet errato.


## 1️⃣2️⃣ Collegamento di un Hardware Wallet


Per ottenere il massimo livello di sicurezza, molti utenti del Bitcoin scelgono di conservare i propri fondi in un "deposito a freddo". Ciò significa conservare le "chiavi private" che controllano il Bitcoin su un dispositivo che non è mai connesso a Internet. Un `hardware wallet` (o dispositivo di firma) è un dispositivo fisico specializzato progettato proprio per questo scopo. Agisce come una cassaforte digitale per le chiavi, assicurando che non siano mai esposte alle potenziali minacce di un computer o di uno smartphone online.


Collegando un wallet hardware all'applicazione Bull Bitcoin, si ottiene il meglio di entrambi i mondi: la sicurezza senza compromessi dell'archiviazione a freddo per le chiavi private, combinata con le potenti funzioni e l'interfaccia intuitiva del Bull Bitcoin wallet per la visualizzazione dei saldi e la gestione delle transazioni. In questo capitolo finale, vi mostreremo come collegare un wallet hardware, come ad esempio una [Coldcard Q](https://coldcard.com/q), al vostro Bull Bitcoin wallet. Questa esercitazione non tratterà in modo approfondito l'impostazione di una Coldcard Q, che può essere approfondita qui:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Importazione di un Wallet


![image](assets/en/26.webp)


Per prima cosa, dal menu principale della Coldcard Q, selezionare `Esporta Wallet`, quindi scegliere `Bull Wallet`. La vostra Coldcard generate sarà dotata di un codice QR.


![image](assets/en/20.webp)


Aprire il Bull Bitcoin Wallet e navigare in `Impostazioni` > `Impostazioni Bitcoin` > `Importa wallet` e selezionare `Coldcard Q` sul telefono e toccare `Aprire la fotocamera` per scansionare questo codice QR per importare le chiavi pubbliche del wallet hardware.


![image](assets/en/21.webp)


### Ricezione con Coldcard Q


Per ricevere il Bitcoin utilizzando la Coldcard Q collegata, non è necessario che il dispositivo sia fisicamente connesso al telefono. Il Bull Bitcoin Wallet ha già importato le chiavi pubbliche necessarie, consentendogli di ricevere gli indirizzi generate da solo.


1. Toccare il dispositivo di firma Coldcard Q importato e selezionare "Ricevi".

2. L'applicazione visualizzerà automaticamente un indirizzo Bitcoin fresco dal wallet della Coldcard.

3. Utilizzare questo indirizzo per ricevere i fondi. Il Bitcoin sarà assicurato direttamente alle chiavi dell'hardware wallet, anche se il dispositivo era offline durante il processo.


![image](assets/en/22.webp)


### Invio con Coldcard Q


L'invio della Bitcoin con la Coldcard Q richiede una conferma fisica per autorizzare qualsiasi transazione. Mentre l'applicazione Bull Wallet viene utilizzata per creare la transazione, la firma finale può essere creata solo sull'hardware wallet stesso.


Per iniziare, aprire la `Coldcard Q` wallet e toccare `Invia`. Quindi, "aprire la fotocamera" per scansionare il codice QR dell'indirizzo del destinatario. Dopo la scansione, inserire l'"importo" che si desidera inviare e regolare la "priorità della tassa" come necessario.


Per ulteriori opzioni, è possibile consultare la sezione Impostazioni avanzate. Qui si trova l'opzione "Sostituisci per tassa" (RBF), che è attivata per impostazione predefinita e consente di velocizzare una transazione bloccata in un secondo momento. È inoltre disponibile l'opzione `Coin Control`, che consente di selezionare manualmente gli UTXO specifici che si desidera spendere.


Dopo aver esaminato tutti i dettagli, toccare "Mostra PSBT" per preparare la transazione.


![image](assets/en/23.webp)


Toccate il pulsante `Scan` sulla vostra Coldcard Q e utilizzate la sua fotocamera per scansionare il codice QR visualizzato sul vostro telefono. Sullo schermo della Coldcard vengono visualizzati tutti i dettagli della transazione. Verificate attentamente l'importo, l'indirizzo del destinatario e il vostro indirizzo di cambio. Se tutto è corretto, premete il pulsante `Enter` sulla Coldcard Q per firmare la transazione. Successivamente, sullo schermo apparirà un codice QR della transazione firmata.


![image](assets/en/24.webp)


Sul Bull wallet, toccare `Ho finito`, quindi toccare il pulsante `Camera` per scansionare il codice QR della `transazione firmata` dalla Coldcard Q. Il Bull Wallet visualizzerà ora una schermata di riepilogo della transazione firmata. Esaminarla un'ultima volta, quindi toccare "Trasmetti transazione". Questa operazione conclude il processo di invio della transazione alla rete Bitcoin e i fondi saranno in viaggio.


## 🎯 Conclusione


Il viaggio attraverso il Bull Bitcoin Wallet è terminato. L'applicazione mette a portata di mano potenti strumenti per la privacy e la sicurezza, rendendo le funzioni avanzate semplici da usare. Vi aiuta a mantenere la privacy grazie a funzioni come `PayJoin`, che nasconde le vostre transazioni sulla blockchain, e `Tor integration`, che maschera la vostra attività di rete da occhi indiscreti. Per chi desidera il massimo controllo, è possibile connettersi al proprio "nodo Bitcoin personale" per non affidarsi più a server di terze parti e utilizzare un "wallet hardware" per mantenere le chiavi private completamente offline e al sicuro. Grazie alle opzioni di backup intelligenti e al supporto continuo per Bitcoin, Liquid e Lightning, il Bull Bitcoin Wallet è una scelta forte e completa per chiunque voglia mantenere i propri fondi privati, sicuri e sotto il proprio controllo.


## 📚 Risorse del Toro Wallet


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Sito web ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)
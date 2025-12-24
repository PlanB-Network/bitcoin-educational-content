---
name: Mostro
description: Piattaforma di scambio Bitcoin P2P esente da KYC tramite Lightning e Nostr
---

![cover](assets/cover.webp)



Come acquistare o vendere bitcoin senza compromettere la propria sovranità finanziaria? Le piattaforme centralizzate impongono procedure KYC invasive che espongono i vostri dati personali, con la possibilità di congelamento arbitrario del conto o di sorveglianza statale.



**Mostro P2P** offre un'alternativa decentralizzata che combina Lightning Network, il protocollo Nostr e le fatture di deposito. La sua principale innovazione: un sistema di deposito a garanzia automatizzato in cui i bitcoin rimangono sotto il vostro controllo per tutta la durata dello scambio, eliminando il rischio di furto, bancarotta o confisca arbitraria.



## Che cos'è il Mostro P2P?



Mostro P2P è un protocollo di scambio Bitcoin open source creato da **grunch**, sviluppatore del popolare bot Telegram **lnp2pbot** lanciato nel 2021. Sebbene lnp2pbot avesse già abilitato gli scambi P2P senza KYC tramite Lightning, presentava una grave vulnerabilità: **Telegram costituisce un punto di fallimento centralizzato** suscettibile di censura da parte dei governi.



Mostro rappresenta l'evoluzione **decentralizzata** di questo concetto: sostituendo Telegram con il protocollo **Nostr** (una rete incensurabile di relè distribuiti), Mostro elimina questo rischio sistemico. Il protocollo combina Lightning Network per le transazioni istantanee, Nostr per le comunicazioni resistenti alla censura e **hold invoices** per creare un vero e proprio deposito automatico non custodiale.



### Architettura tecnica



Mostro opera attraverso tre componenti:




- Daemon Mostrod**: coordina gli scambi tra gli utenti e il Lightning Network
- Nodo Lightning**: crea fatture di attesa (deposito crittografico di ~24 ore)
- Clienti Mostro**: interfacce utente (CLI, Mobile, Web)



Gli ordini vengono pubblicati su Nostr come eventi pubblici (tipo 38383), mentre le transazioni private vengono trasmesse tramite messaggi criptati end-to-end (NIP-59, NIP-44). Ogni istanza di Mostro definisce le proprie commissioni (generalmente tra lo 0,3% e l'1%) e i limiti di transazione (da poche migliaia a diverse centinaia di migliaia di sats, a seconda dell'istanza).



### Vantaggi decisivi



**Resistente alla censura**: Nessun governo può bloccare Mostro finché esistono relè Nostr da qualche parte nel mondo. A differenza del vulnerabile lnp2pbot via Telegram, Mostro consente scambi a prova di **censura**.



**Escrow non-custodial**: Le fatture Lightning hold bloccano i vostri bitcoin senza trasferirli in modo permanente. I vostri fondi rimangono sotto il vostro controllo e vi vengono automaticamente restituiti in caso di problemi (~24h).



**Confidenzialità per design**: Due modalità disponibili per soddisfare le vostre esigenze. La modalità Reputazione** collega la vostra reputazione alla vostra chiave Nostr per creare una fiducia duratura. La modalità Privata** favorisce l'anonimato assoluto con chiavi effimere monouso.



## Caratteristiche principali



**Comunicazione decentralizzata**: Tutti gli ordini sono pubblicati su Nostr tramite eventi firmati crittograficamente. Le trattative private sono trasmesse tramite messaggi crittografati end-to-end, che garantiscono l'assoluta riservatezza.



**Sistema di valutazione**: valutazione a 5 stelle con calcolo iterativo memorizzata in modo permanente su Nostr. Permette di costruirsi gradualmente una reputazione di trader affidabile.



**Arbitrato decentralizzato**: In caso di controversia, un arbitro imparziale esamina le prove e prende una decisione basata su criteri trasparenti. Ogni controversia genera un token unico per la tracciabilità.



**Flessibilità di pagamento**: Supporto per molte valute fiat tramite il servizio di cambio yadio.io. Accetta bonifici SEPA, PayPal, Revolut, contanti e qualsiasi metodo concordato tra le parti.



## Clienti Mostro disponibili



Mostro offre due principali client operativi per gli scambi P2P.



### Mostro CLI - Client a riga di comando



Il **Mostro CLI** è il client più maturo e funzionale. Scritto in Rust, offre l'intera gamma di funzioni di Mostro tramite un'interfaccia a riga di comando. È compatibile con macOS, Linux e Windows.



**Controlli principali** :




- `elenco ordini`: Visualizza tutti gli ordini disponibili
- `neworder` : Crea un nuovo ordine di acquisto o di vendita
- `takesell` / `takebuy`: Prendere un ordine di acquisto o di vendita
- `fiatsent`: Conferma l'invio del pagamento fiat
- `rilascio`: Rilascia l'escrow e finalizza lo scambio
- `getdm`: Visualizza i messaggi diretti
- `rate` : valutare la controparte dopo uno scambio



Ideale per utenti tecnici, automazione e ambienti che richiedono la massima sicurezza.



### Mostro Mobile - Applicazione per smartphone



L'applicazione **mobile** in versione alpha consente di fare trading con il P2P direttamente dal proprio smartphone. Interface grafica intuitiva con navigazione a schede, visualizzazione degli ordini, filtri avanzati e chat integrata per comunicare con le controparti.



Disponibile per **Android** (tramite APK su GitHub), è la scelta ottimale per gli utenti che privilegiano la semplicità e il trading occasionale in mobilità.



### Mostro-web - Interface web (in fase di sviluppo)



Applicazione web JavaScript avanzata Interface in fase di sviluppo attivo. Progettata per offrire un'esperienza utente completa con ampie funzionalità di trading e gestione del portafoglio. Accesso tramite browser senza necessità di installazione.



## Installazione e configurazione



Questa esercitazione vi guiderà nell'installazione e nell'uso dei due principali client Mostro: CLI e l'applicazione mobile.



### Prerequisiti essenziali



Prima di iniziare, è necessario :





- Un Lightning Network** wallet funzionante con liquidità sufficiente (o compatibile con Lightning)
 - Consigliato: Phoenix, Breez, Wallet o Satoshi...
 - Minimo 1000 satoshis di liquidità da testare



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Una chiave privata Nostr** (formato `nsec1...`)
 - Creare una chiave di trading dedicata su [nostrkeygen.com](https://nostrkeygen.com/)
 - Importante**: Non utilizzare mai la chiave Nostr personale principale
 - Conservate la vostra chiave privata in un luogo sicuro (gestore di password)





- Opzionale ma consigliato**: Connessione VPN o Tor per mascherare il proprio indirizzo IP



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Installazione di Mostro CLI



#### Su macOS



**Fase 1: controllo Rust**



Verificare che Rust sia installato (è richiesta la versione 1.64+):



```bash
rustc --version
```



Se il Rust non è installato :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Fase 2: clonazione del repository**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Fase 3: Configurazione**



Copiare e modificare il file :



```bash
cp .env-sample .env
```



Aprire `.env` e configurare le impostazioni:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Importante per la sincronizzazione CLI/Mobile**: Per accedere agli stessi ordini sul CLI e sull'app mobile, è necessario utilizzare la **stessa Mostro Pubkey** e gli **stessi relè Nostr** in entrambi i client. Controllare queste impostazioni nelle Impostazioni dell'app mobile.



![Configuration .env](assets/fr/02.webp)



**Fase 4: Installazione**



Compilare e installare il programma CLI :



```bash
cargo install --path .
```



La compilazione richiede 1-2 minuti. L'eseguibile `mostro-cli' sarà installato in `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Fase 5: Controllo**



Verificare che tutto funzioni:



```bash
mostro-cli --help
```



Dovrebbe essere visualizzato l'elenco completo degli ordini.



![Vérification avec --help](assets/fr/04.webp)



#### Su Linux (Ubuntu/Debian)



Installazione identica a quella di macOS, con l'aggiunta di :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Seguire quindi i passaggi 3 e 4 della sezione macOS.



#### Su Windows



Installare prima Rust tramite [rustup.rs](https://rustup.rs/), quindi utilizzare PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Configurazione identica: copiare `.env-sample` in `.env` e inserire i propri parametri.



### Installazione di Mostro Mobile



#### Su Android



**Passo 1**: Andare alla pagina [GitHub releases](https://github.com/MostroP2P/mobile/releases) e scaricare il file **app-release.apk** (circa 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Fase 2: una volta scaricato, aprire il file APK dai download. Android chiederà di autorizzare l'installazione da questa fonte.



![Téléchargement et installation APK](assets/fr/11.webp)



**Fase 3**: Seguire le schermate di onboarding, che presentano le funzionalità:




- Negoziare liberamente Bitcoin - senza KYC** : Commercio senza verifica dell'identità grazie a Nostr
- Privacy di default**: Scegliere tra la modalità Reputazione e la modalità Privacy completa
- Sicurezza ad ogni passo**: Protezione con le fatture di trattenuta non detentive



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Passo 4**: Continuare l'onboarding per scoprire :




- Chat completamente crittografata**: Comunicazione crittografata end-to-end
- Accettare un'offerta**: Sfogliare il portafoglio ordini e scegliere un'offerta
- Non trovate quello che vi serve? ** : Create il vostro ordine personalizzato



![Suite onboarding](assets/fr/13.webp)



**Fase 5: una volta completata l'iscrizione, l'app genera automaticamente una coppia di chiavi Nostr. Andate nel menu (☰) e poi in **Account** per salvare le vostre **Secret Words** (frasi di recupero). In questa schermata è inoltre possibile modificare la modalità di privacy già menzionata.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Importante**: Annotate la vostra frase di recupero in un luogo sicuro (password manager, cassaforte di carta).



### Configurazione iniziale della sicurezza



Qualunque sia la piattaforma utilizzata :





- Chiave dedicata**: Utilizzare un'identità Nostr separata per il trading
- Piccoli importi**: Iniziare con meno di sats 10.000 per iniziare
- Relè multipli**: Configurazione di 3-5 relè geograficamente diversi
- Protezione della rete**: Attivare VPN o Tor per nascondere il proprio indirizzo IP
- Wallet secure**: Attivazione del blocco automatico del wallet Lightning



## Utilizzare con CLI



In questa sezione viene illustrato l'acquisto di bitcoin tramite Mostro CLI in base a un caso d'uso reale.



### Fase 1: Elenco degli ordini disponibili



Il comando `elenco ordini` visualizza tutti gli ordini attivi:



```bash
mostro-cli listorders
```



Verrà visualizzata una tabella con i dettagli di ciascun ordine: ID, tipo (acquisto/vendita), importo, valuta, metodo di pagamento.



![Liste des ordres disponibles](assets/fr/05.webp)



In questo esempio, è visibile un ordine di vendita di 5 euro tramite Revolut (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Fase 2: presa in carico dell'ordine



Per acquistare questi bitcoin, prendere l'ordine con `takesell`:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro chiederà all'utente di fornire una **fattura luminosa** per ricevere il BTC. L'importo esatto in satoshi è indicato (qui: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Passo 3: Fornire la fattura Lightning



Generare una fattura Lightning dal wallet (Phoenix, Breez, ecc.) per l'importo esatto, quindi inviarla :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Il sistema conferma la spedizione e vi dice di aspettare che il venditore paghi la fattura di attesa prima di attivare l'escrow.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Fase 4: contattare il venditore



Una volta attivato il deposito a garanzia, utilizzare `dmtouser` per richiedere i dettagli del pagamento al venditore:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Fase 5: Recuperare la risposta



Controllate i messaggi diretti per vedere la risposta del venditore:



```bash
mostro-cli getdm
```



Il venditore vi fornisce il suo ID di pagamento (qui il suo Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Fase 6: Effettuare il pagamento in fiat



Inviare il pagamento tramite il metodo concordato (Revolut in questo esempio) ai recapiti forniti. **Conservate tutti i documenti di supporto** (screenshot, riferimenti alle transazioni).



### Fase 7: Conferma dell'invio del pagamento



Una volta effettuato il pagamento, informare Mostro :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Fase 8: Ricezione dei bitcoin



Non appena il venditore conferma la ricezione del fiat e rilascia l'escrow con il comando `release`, si ricevono immediatamente i bitcoin sulla fattura Lightning fornita.



### Fase 9: Valutazione



Valutare il venditore per contribuire alla reputazione decentralizzata:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Comandi utili



**Annullare un ordine** (prima che venga preso) :


```bash
mostro-cli cancel -o <order-id>
```



**Creare un nuovo ordine di vendita** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Aprire una controversia** :


```bash
mostro-cli dispute -o <order-id>
```



## Utilizzo con l'applicazione mobile



Questa sezione illustra la vendita di bitcoin tramite Mostro Mobile seguendo un caso d'uso reale.



### Interface principale



L'applicazione presenta 3 schede principali:





- Libro degli ordini**: Sfoglia gli ordini di acquisto (BUY BTC) e di vendita (SELL BTC) disponibili
- Le mie operazioni**: Visualizzare gli ordini attivi e storici
- Chat**: Comunicare con le controparti utilizzando le cifre



![Interface principale](assets/fr/14.webp)



### Configurazione consigliata



Prima di fare trading, configurare alcune impostazioni tramite il menu (☰) > **Impostazioni** :





- Lampo Address** (opzionale): Per ricevere direttamente i pagamenti
- Relè**: Aggiungere diversi relay Nostr per la resilienza (ad esempio `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Controllare la chiave pubblica dell'istanza di Mostro che si sta utilizzando



![Paramètres de l'application](assets/fr/16.webp)



**Importante per la sincronizzazione CLI/Mobile**: Se si utilizzano sia il CLI che l'applicazione mobile, configurare **esattamente gli stessi relè Nostr e la stessa Mostro Pubkey** in entrambi i client. Senza questa configurazione identica, non si vedranno gli stessi ordini disponibili su entrambe le interfacce. I relè e la Mostro Pubkey visibili in Impostazioni (schermata precedente) devono corrispondere a quelli presenti nel file `.env' del CLI.



### Passo 1: creare un ordine di vendita



Premere il pulsante verde **"+"** in basso a destra, quindi selezionare **VENDITA** (pulsante rosso).



![Boutons de création d'ordre](assets/fr/17.webp)



Compilare il modulo di creazione:



1. **Valuta**: Selezionare la valuta che si desidera ricevere (EUR, USD, ecc.)


2. **Importo** : Inserire l'importo in valuta (ad es. da 1 a 3 EUR)


3. **Metodi di pagamento** : Scegliere il metodo (ad es. "Revolut")


4. **Tipo di prezzo**: Selezionare "Prezzo di mercato"


5. **Premio**: Regola il premio (cursore da -10% a +10%, consigliato: 0% per vendere rapidamente)



Premere **Invio** per pubblicare l'ordine.



### Fase 2: conferma della pubblicazione



Il vostro ordine è stato pubblicato! Sarà disponibile per 24 ore. È possibile annullarlo in qualsiasi momento, prima che un acquirente lo prenda, eseguendo il comando `cancel`.



![Ordre publié](assets/fr/18.webp)



L'ordine appare nella scheda **My Trades** con lo stato "Pending" e il badge "Created by you".



### Fase 3: Un acquirente prende in carico l'ordine



Quando un acquirente accetta il tuo ordine, ricevi una notifica. Vedere i dettagli in **Le mie compravendite**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Istruzione importante**: Ora è necessario **pagare la fattura di attesa** visualizzata per bloccare i bitcoin (qui 4674 sats per 1-5 EUR) nel deposito a garanzia. Avete **15 minuti al massimo** altrimenti lo scambio sarà annullato.



Copiare la fattura di attesa e pagarla dal proprio wallet Lightning (Phoenix, Breez, ecc.).



### Fase 4: Comunicare con l'acquirente



Una volta attivato l'escrow, premere **CONTATTO** per aprire la chat criptata con l'acquirente.



L'acquirente (qui "anonymous-gloriaZhao") ti contatterà per chiederti i dettagli del pagamento. Ti preghiamo di rispondere con i tuoi dati (Revtag, IBAN, ecc.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Fase 5: ricezione del pagamento in fiat



Attendete di ricevere il pagamento in fiati sul vostro conto Revolut (o altro metodo concordato). **Controllate attentamente**:




- L'importo esatto
- Il mittente
- Il riferimento, se richiesto



L'acquirente vi informerà via chat di aver inviato il pagamento. Mostro visualizzerà anche un messaggio di conferma dell'invio del fiat.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Fase 6: svincolo del deposito a garanzia



Una volta **confermata la ricezione** del pagamento in fiati sul proprio conto, premere il pulsante verde **RELEASE** e confermare per inviare il satss all'acquirente.



![Libération de l'escrow](assets/fr/20.webp)



I Bitcoin vengono trasferiti istantaneamente all'acquirente tramite la sua fattura Lightning.



### Fase 7: valutare la considerazione



Dopo il rilascio, premere **VALUTAZIONE** per valutare l'acquirente. Selezionare da 1 a 5 stelle (qui 5/5) e premere **Invia valutazione**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Lo scambio è finito!



### Acquistare bitcoin con l'app mobile



Il processo per **acquistare** bitcoin è simile, ma invertito:



1. Sfogliare la scheda **Order Book** > **BUY BTC** per visualizzare gli ordini di vendita


2. Fare clic su un ordine interessante per visualizzare i dettagli


3. Premere **Prendi ordine**


4. Fornite la vostra fattura Lightning (generata dal vostro wallet)


5. Attendere che il venditore attivi l'escrow


6. Contattare il venditore tramite **CONTATTO** per i dettagli del pagamento


7. Inviare il pagamento in fiat (conservare la prova)


8. Il venditore rilascia l'escrow dopo la verifica


9. Ricevere bitcoin istantaneamente sulla vostra fattura Lightning


10. Valuta il venditore (1-5 stelle)



### Gestione dei problemi



**Annullare un ordine**: In **My Trades**, premere l'ordine e poi il pulsante **CANCEL** (disponibile solo prima che venga eseguito).



**Aprire una controversia**: In caso di disaccordo, premere **DISPUTE** nei dettagli dell'ordine. Allegare tutte le prove (screenshot della chat, riferimenti alle transazioni bancarie).



## Vantaggi e limiti



### Vantaggi



**Sovranità finanziaria**: I vostri bitcoin non lasciano mai il vostro controllo diretto grazie al meccanismo di hold invoice, eliminando il rischio di bancarotta o di pirateria.



**Resistente alla censura**: Nessuna autorità può bloccare la rete o censurare i vostri ordini. Il sistema funziona finché i relè Nostr sono operativi.



**Anonimato di default**: Solo una chiave Nostr pseudonima vi identifica, senza KYC o dati personali. Comunicazioni crittografate end-to-end.



**Flessibilità di pagamento**: È possibile utilizzare qualsiasi metodo di pagamento reciprocamente accettato (bonifici, applicazioni mobili, contanti, baratto).



### Limitazioni



**Sviluppo iniziale**: Sono necessarie interfacce rudimentali e una curva di apprendimento tecnico.



**Limitata liquidità**: Numero limitato di ordini, in particolare per importi elevati o valute rare.



**Requisiti tecnici**: È richiesta una conoscenza di base di Lightning e Nostr.



**Responsabilità individuale**: Nessun supporto centralizzato in caso di problemi, è richiesta cautela.



## Conclusione



Mostro P2P rappresenta una promettente alternativa alle borse centralizzate, combinando Lightning Network, Nostr e escrow automatizzato per un trading realmente decentralizzato. Nonostante lo sviluppo iniziale e la liquidità limitata, la piattaforma offre già sovranità finanziaria, resistenza alla censura e anonimato di default.



Per i bitcoiners che preferiscono l'autonomia e la riservatezza, Mostro è un'opzione valida che merita di essere esplorata progressivamente. La sua architettura decentralizzata garantisce un'evoluzione comunitaria piuttosto che commerciale, aprendo la strada a un futuro di scambi Bitcoin veramente liberi.



## Risorse



### Documentazione ufficiale




- [Sito ufficiale di Mostro](https://mostro.network)
- [Documentazione tecnica](https://mostro.network/docs-english/index.html)
- [Fondazione Mostro](https://mostro.foundation)



### Codice sorgente e sviluppo




- [Repository GitHub principale](https://github.com/MostroP2P/mostro)
- [client web](https://github.com/MostroP2P/mostro-web)
- [Cliente CLI](https://github.com/MostroP2P/mostro-cli)



### Comunità




- [Protocollo Nostr](https://nostr.com)
- [Guide Lightning Network](https://lightning.network)
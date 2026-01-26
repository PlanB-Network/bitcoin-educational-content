---
name: KaleidoSwap
description: Guida avanzata al trading di asset RGB su Lightning Network con KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap è una sofisticata applicazione desktop open-source che colma il divario tra il Protocollo RGB e il Lightning Network. Si tratta di un'interfaccia completa per la gestione dei nodi RGB Lightning, l'interazione con i fornitori di servizi RGB Lightning (LSP) tramite la specifica LSPS1 e l'esecuzione di swap atomici di asset RGB.


In quanto soluzione non custodiale, KaleidoSwap consente agli utenti di mantenere il pieno controllo sulle proprie chiavi e sui propri dati. Sfruttando il paradigma di convalida lato client di RGB, consente di creare contratti intelligenti privati e scalabili in cima a Bitcoin. Questo tutorial si addentra nelle caratteristiche avanzate di KaleidoSwap, guidandovi attraverso le complessità della gestione del UTXO "colorato", della liquidità del canale per asset specifici e del modello di trading taker-maker, assicurandovi di poter utilizzare appieno questo potente protocollo di scambio decentralizzato.


## Installazione


KaleidoSwap fornisce binari precostituiti per i principali sistemi operativi, ma per gli utenti avanzati la creazione da sorgente garantisce l'esecuzione del codice più recente con le proprie configurazioni specifiche.


### Scaricare i binari


È possibile scaricare l'ultima versione per il proprio sistema operativo dal [sito web ufficiale](https://kaleidoswap.com/) o dalla [pagina dei rilasci di GitHub](https://github.com/kaleidoswap/desktop-app/releases).


### Metodi di installazione


1.  **Windows**: Scaricare il programma di installazione `.exe` ed eseguirlo.

2.  **macOS**: Scaricare il file `.dmg`, aprirlo e trascinare KaleidoSwap nella cartella Applicazioni.

3.  **Linux**: Scaricare il file `.AppImage` o `.deb` e installarlo/eseguirlo.



## Opzioni di impostazione del nodo


Quando si avvia KaleidoSwap per la prima volta, viene presentata la **Schermata di connessione**. Questo è il primo passo per la configurazione dell'ambiente.


![Node Selection Screen](assets/en/01.webp)


È necessario scegliere come collegarsi al RGB Lightning Network. Questa scelta influisce sul livello di controllo e di privacy dell'utente.


### Opzione 1: Nodo locale (consigliato per l'autocustodia)


**Per un controllo completo e una maggiore privacy**, eseguite un nodo direttamente sul vostro computer; vedete i vantaggi che ne derivano:


- Autodeterminazione**: Siete voi a detenere le chiavi. Nessun terzo può bloccare i vostri fondi o censurare le vostre transazioni.
- Privacy**: I vostri dati rimangono sul vostro dispositivo.
- Indipendenza**: Nessuna dipendenza da fornitori di servizi esterni.


Se si seleziona **Nodo locale**, si accede alla schermata di impostazione in cui è possibile creare un nuovo wallet o ripristinarne uno esistente.


![Local Node Setup Screen](assets/en/02.webp)


### Opzione 2: Nodo remoto


Connettersi a un RGB Lightning Node remoto (in hosting su un VPS o su un provider in hosting).


- Vantaggi**: Nessun utilizzo di risorse locali, disponibilità 24/7.
- Scambio**: Richiede la fiducia nell'host o la gestione di un server remoto.


![Remote Node Setup Screen](assets/en/03.webp)


**Per sfruttare appieno le proprietà di resistenza alla censura di Bitcoin e RGB, consigliamo vivamente di gestire il proprio nodo, sia localmente (opzione 1) che in self-hosting su un nodo remoto.


## Creazione di un Wallet


KaleidoSwap gestisce sia le attività Bitcoin che RGB. Il processo di creazione del wallet inizializza un keystore che protegge i fondi on-chain e gli stati del canale Lightning.


Ecco il procedimento dettagliato:

1. Aprire KaleidoSwap e selezionare **Nodo locale**.

2. Fare clic su **Crea nuovo Wallet**.

3. **Impostazione account**: Immettere un **Nome account** e selezionare la **Rete** (ad esempio, Bitcoin Mainnet, Testnet, Signet).

4. **Configurazione avanzata** (opzionale): Se si è un utente esperto, è possibile configurare endpoint RPC personalizzati, URL dell'indicizzatore o impostazioni del proxy in "Impostazioni avanzate".

5. Fare clic su **Continua**.

6. **Password**: Impostare una password forte per crittografare il file wallet localmente.

7. **Frase di recupero**: Annotare la frase seed e conservarla in modo sicuro.


    - Critico**: Questa frase è necessaria per recuperare i fondi on-chain e l'identità del nodo.
    - Attenzione**: **Gli stati dei canali Lightning non possono essere recuperati completamente solo dal seed**. È necessario mantenere anche i backup statici dei canali (SCB) per recuperare i fondi bloccati nei canali.


![Wallet Creation Screen](assets/en/04.webp)



## Panoramica del cruscotto


Una volta creato il vostro wallet, sarete indirizzati al **Dashboard** principale.


![KaleidoSwap Dashboard](assets/en/05.webp)


nota: la schermata qui sopra mostra un wallet già finanziato e con canali attivi. Un nuovo wallet mostrerà saldi pari a zero e nessun canale attivo fino a quando non lo si finanzierà._


## Finanziamento del Wallet


Per operare con gli asset RGB, è necessario finanziare il proprio wallet. KaleidoSwap supporta il deposito di attività Bitcoin e RGB tramite transazioni on-chain o Lightning Network.


### Deposito del Bitcoin


1. Fare clic su **Deposito** nel menu Azioni rapide.

2. Selezionare **BTC** dall'elenco delle attività.


![Select BTC Asset](assets/en/06.webp)


3. Scegliete il vostro metodo di deposito: **Su catena** o **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- A catena**: Scannerizzare il codice QR o copiare l'indirizzo per inviare il Bitcoin da un altro wallet.
- Fulmine**: Generare una fattura per l'importo desiderato.


![BTC On-chain Deposit](assets/en/08.webp)


### Deposito di Attività RGB e UTXO colorati


Per ricevere asset RGB (come USDT), è necessario disporre di UTXO specifici da "colorare" (assegnare un asset).


1. Cliccare su **Deposito** e selezionare l'asset RGB (ad esempio, USDT). **Importante: Se è la **prima volta** che il vostro nodo riceve questo specifico asset, **lasciate vuoto il campo ID asset**. Se si inserisce un ID per una risorsa sconosciuta, il nodo restituirà un errore perché non la riconosce ancora.

2. Scegliere **Su catena** o **Lightning**.


![USDT Deposit Options](assets/en/09.webp)


#### Modalità di ricezione a catena: Testimone vs. Accecato


Quando si ricevono le risorse RGB on-chain, sono disponibili due modalità di privacy:



- Ricezione accecata (consigliata per la privacy)**: Si fornisce al mittente un UTXO "blinded". Si chiede al mittente di inviare risorse a un UTXO esistente di cui si è proprietari, ma si nasconde l'identificativo del UTXO effettivo. Questo offre una migliore privacy.
- Ricezione del testimone**: Si fornisce un indirizzo Bitcoin standard. Chiedete al mittente di creare un *nuovo* UTXO per voi inviando le attività a quell'indirizzo. In questo modo le attività del RGB possono essere collegate direttamente al nuovo UTXO creato dalla transazione.


#### Deposito lampo


Per i depositi Lightning, è sufficiente generate una fattura. La risorsa RGB vi sarà inoltrata attraverso i vostri canali aperti.


![USDT Lightning Invoice](assets/en/10.webp)



## Apertura di canali con le attività RGB


Per instradare le attività del RGB sul Lightning Network, è necessario disporre di un canale con liquidità e allocazione delle attività sufficienti. Il modo più semplice per iniziare è quello di **acquistare un canale** da un LSP (Lightning Service Provider).


### Acquisto di un canale da Kaleido LSP


1. Andare alla scheda **Canali**. Verranno visualizzate le opzioni "Aprire canale" (manuale) o "Acquistare canale" (LSP).

2. Fare clic su **Canale di acquisto**.


![Channels Dashboard](assets/en/11.webp)


3. **Collegamento all'LSP**: L'applicazione si connette all'LSP predefinito di Kaleido. Questo provider offre liquidità in entrata e supporta l'instradamento delle attività RGB.


![Connect to LSP](assets/en/12.webp)


4. **Configura canale**:


    - Capacità**: Selezionare la capacità totale Bitcoin per il canale.
    - Allocazione RGB**: Scegliere l'asset RGB (ad esempio, USDT) che si desidera ricevere o inviare. L'LSP si assicurerà che il canale sia configurato per supportare questa risorsa.


![Configure Channel](assets/en/13.webp)



    - Allocazione RGB**: Scegliere l'asset RGB (ad esempio, USDT) che si desidera ricevere o inviare. L'LSP si assicurerà che il canale sia configurato per supportare questa risorsa.


![RGB Allocation](assets/en/14.webp)


5.  **Pagamento**: È necessario pagare una commissione all'LSP per l'apertura del canale e la fornitura di liquidità. È possibile pagare utilizzando il **Lightning** o il **On-chain** Bitcoin. Il pagamento può essere effettuato dal proprio wallet interno a KaleidoSwap o da un wallet esterno.


![Complete Payment](assets/en/15.webp)


6. Una volta confermato il pagamento, l'LSP avvierà la transazione di apertura del canale. Verrà visualizzata la schermata **Ordine completato**.


![Order Completed](assets/en/16.webp)


7. Dopo la conferma sulla blockchain, il canale sarà attivo e pronto per i trasferimenti RGB.



## Trading: Modello Taker-Maker


Il motore di trading di KaleidoSwap opera su un modello **Taker-Maker**. È possibile scambiare asset manualmente con un peer o utilizzare un Market Maker (LSP).


### Scambiare con un Market Maker (LSP)


Questo è il modo più comune di fare trading. L'utente agisce come **Taker**, eseguendo gli ordini a fronte della liquidità disponibile fornita dal LSP (**Maker**).


1. Passare alla scheda **Trade** e selezionare **Market Maker**.

2. **Inserire l'importo**: Inserire l'importo di Bitcoin che si desidera inviare (o l'attività che si desidera ricevere). L'interfaccia mostrerà il tasso di cambio stimato e le commissioni.


![Market Maker Swap](assets/en/17.webp)


3. **Conferma lo scambio**: Esaminate i dettagli, compreso il tasso di cambio e l'importo esatto che riceverete. Fare clic su **Conferma scambio**.


![Confirm Swap](assets/en/18.webp)


4. **Elaborazione**: Lo scambio viene eseguito atomicamente sul Lightning Network. Viene visualizzata una schermata di stato che indica che lo scambio è in corso.


![Swap Pending](assets/en/19.webp)


5. **Successo**: Una volta regolate le HTLC, lo swap è completo e le attività sono nel vostro canale.


![Swap Success](assets/en/20.webp)



## Sviluppatore API


Per gli sviluppatori che costruiscono sopra KaleidoSwap, l'applicazione espone un API che supporta:



- RGB LSPS1**: Per i servizi di liquidità automatizzati.
- Swap API**: Per il programmatic trading e il market making.
- WebSocket**: Per la sottoscrizione di dati di mercato in tempo reale.


Consultare la [Documentazione API](https://docs.kaleidoswap.com/api/introduction) per i punti finali e le specifiche complete.


## Conclusione


KaleidoSwap vi permette di sfruttare la privacy e la scalabilità delle attività del RGB sul Lightning Network. Comprendendo le UTXO colorate e l'allocazione delle risorse del canale, è possibile utilizzare appieno questo potente protocollo di scambio decentralizzato.
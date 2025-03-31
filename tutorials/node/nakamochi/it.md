---
name: Nakamochi
description: Esecuzione del nodo semplificata - Come impostare e utilizzare il nodo Nakamochi Bitcoin e Lightning.
---
Gestire un proprio nodo Bitcoin e Lightning non deve più essere un compito complesso limitato agli esperti tecnici. Tradizionalmente, la creazione e la gestione dei nodi richiedeva una conoscenza approfondita della crittografia, delle reti e dello sviluppo di software. Nakamochi cambia questa situazione rendendo i nodi accessibili a tutti, indipendentemente dal background tecnico.

Con Nakamochi, chiunque può creare e gestire un nodo da casa, consentendo una totale privacy e indipendenza finanziaria. La gestione di un nodo completo non solo protegge le proprie transazioni, ma contribuisce anche alla forza della rete Bitcoin. Una rete Bitcoin decentralizzata e resiliente si basa su un'ampia distribuzione di nodi per garantire la sua sicurezza e indipendenza.

### Indice dei contenuti


- Che cos'è il Nakamochi e come funziona?
- Impostazione di Nakamochi
- Informazioni sulla rete Lightning
- Aprire canali ed effettuare transazioni nella rete Lightning

## Che cos'è il Nakamochi e come funziona?

Nakamochi è un nodo completo di soli Bitcoin che supporta sia la rete Bitcoin che quella Lightning. Include un portafoglio Bitcoin e Lightning integrato, che consente agli utenti di gestire un nodo Bitcoin sicuro e autosufficiente, beneficiando al contempo della velocità e dei bassi costi di transazione della rete Lightning.

Il vostro nodo Nakamochi è gestito tramite un'applicazione mobile, [BitBanana (Android)](https://bitbanana.app) e [Zeus (iOS)](https://bitbanana.app), che vi permette di controllarlo comodamente da qualsiasi luogo. Queste app fungono da controllo remoto per il vostro nodo, consentendovi di pagare direttamente con Bitcoin o Lightning, di gestire le transazioni, di aprire o chiudere i canali, di controllare i saldi e di monitorare le prestazioni del vostro nodo, il tutto con estrema facilità.

## La configurazione di Nakamochi richiede solo 5 minuti

### Passo 1: Collegarsi e iniziare

1. Collegare Nakamochi all'alimentazione e al Wi-Fi.

2. Cliccate su **"Setup New Wallet "** e memorizzate in modo sicuro la vostra frase di recupero di 24 parole.

3. Utilizzare un'applicazione di gestione dei nodi (Zeus o BitBanana) per connettersi al proprio Nakamochi:

4. Aprire l'applicazione e scansionare il codice QR visualizzato sul Nakamochi.

5. Per maggiore sicurezza, impostare un codice PIN sul dispositivo.

![image](assets/en/01.webp)

collegatevi all'alimentazione e scrivete la vostra frase-seme di 24 parole

![image](assets/en/02.webp)

aspettate che la Blockchain si metta al passo con i tempi

![image](assets/en/03.webp)

imposta un nuovo portafoglio nella scheda Lightning

![image](assets/en/04.webp)

scansione del codice QR con l'app di gestione dei nodi

![image](asset/en/05.webp)

per una maggiore sicurezza, impostare un codice PIN

**Nota:** _Permettere al nodo Nakamochi di sincronizzarsi con la blockchain. Questo processo potrebbe richiedere un po' di tempo a seconda della connessione a Internet

## Informazioni sulla rete Lightning

La Bitcoin Lightning Network rivoluziona le transazioni in Bitcoin rendendole più veloci, più economiche e più efficienti. È perfetta per l'uso quotidiano, in quanto consente pagamenti quasi istantanei con commissioni minime, ideali per le microtransazioni come l'acquisto di un caffè o la gestione di piccoli acquisti frequenti.

Operando fuori dalla catena, Lightning è progettato per scalare, supportando migliaia di transazioni al secondo senza sovraccaricare la blockchain principale di Bitcoin. Questo lo rende un elemento chiave nell'evoluzione di Bitcoin in un sistema di pagamento pratico e globale.

Un altro vantaggio è la privacy, poiché le transazioni su Lightning vengono instradate attraverso canali di pagamento privati anziché essere registrate direttamente sulla blockchain. Ciò garantisce un modo più discreto di effettuare transazioni, pur mantenendo la solida sicurezza di Bitcoin.

#### I canali di pagamento spiegati

La rete Lightning opera attraverso canali di pagamento, che sono connessioni tra due parti che consentono transazioni multiple senza interagire direttamente con la blockchain. Quando un canale è aperto, il saldo tra le due parti viene aggiornato su questa soluzione Lightning di secondo livello per ogni transazione, garantendo pagamenti veloci e a basso costo. Solo l'apertura e la chiusura del canale vengono registrate sulla catena, riducendo la congestione della blockchain Bitcoin. Questo design garantisce scalabilità e privacy, poiché le singole transazioni non vengono registrate sul libro mastro pubblico.

**Esempio:** Alice e Bob aprono un canale impegnandovi Bitcoin. Alice invia Bitcoin a Bob e i loro saldi fuori dalla catena si aggiornano istantaneamente senza che vi sia una registrazione sulla catena. Se Alice paga Charlie e Alice non ha un canale diretto con Charlie, il pagamento può essere instradato attraverso il canale di Bob per raggiungere Charlie. L'instradamento attraverso i nodi intermediari garantisce i pagamenti anche in assenza di connessioni dirette, rendendo la rete altamente efficiente.

## Aprire canali ed effettuare transazioni nella rete Lightning

Una volta che il vostro Nakamochi è stato configurato e collegato a un'app di gestione dei nodi, potete iniziare a utilizzare la rete Lightning aprendo canali ed effettuando transazioni.

### Apertura dei canali su Zeus (iOS):

1. Andare alla scheda **"Canali "** (menu inferiore).

2. Fare clic sul simbolo **"+"** per aprire un nuovo canale.

3. Eseguire la scansione o inserire la pubkey del nodo con cui ci si vuole connettere.

4. Immettere l'importo bloccato (scegliere con il peer o utilizzare l'importo minimo fisso per i nodi noti).

5. Fare clic su **"Aprire un canale "**.

![image](asset/en/06.webp)

schermata ZEUS

Per maggiori informazioni: [Canali | Documentazione Zeus](https://docs.zeusln.app/)

### Apertura dei canali su BitBanana (Android):

1. Aprire il menu hamburger (a sinistra).

2. Andare a **"Canali "**.

3. Fare clic sul simbolo **"+"** per aggiungere/aprire un nuovo canale.

4. Scansionare o incollare la pubkey.

5. Immettere l'importo bloccato (scegliere con il peer o utilizzare l'importo minimo fisso per i nodi noti).

![image](asset/en/07.webp)

schermata di Bitbanana

Per maggiori informazioni: [BitBanana](https://bitbanana.com)

Una volta che il vostro canale è aperto, i pagamenti possono essere inoltrati attraverso di esso ad altri partecipanti alla rete. I saldi si regolano fuori dalla catena, garantendo transazioni quasi istantanee e commissioni minime.

Se non avete più bisogno di un canale, potete chiuderlo. Questa azione regola il saldo finale tra voi e il vostro pari e lo registra sulla catena. Idealmente entrambe le parti sono d'accordo e sono online per una "chiusura cooperativa" (più veloce e con meno spese rispetto a una "chiusura forzata" con un peer non rispondente/offline).

In generale, si consiglia di lasciare aperti i canali per ridurre i costi e aumentare l'affidabilità e l'efficienza della rete. Mantenendo aperti i canali, si riducono al minimo le commissioni sulle transazioni on-chain, si evitano i tempi di inattività per la riconnessione dei canali e si mantiene una capacità di instradamento stabile per un'elaborazione dei pagamenti senza interruzioni. Questo approccio favorisce una rete robusta e resiliente, migliorando l'esperienza complessiva degli utenti e riducendo i costi operativi.

### Link utili


- [Su Nakamochi](https://nakamochi.io/)
- [Iscriviti alla newsletter di Nakamochi](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)
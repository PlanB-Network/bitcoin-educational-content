---
name: Zeus Swap
description: Servizio di scambio non-custodial tra bitcoin on-chain e Lightning Network
---

![cover](assets/cover.webp)

L'ecosistema Bitcoin presenta una dualità: la rete principale (on-chain) offre la massima sicurezza, mentre Lightning Network permette transazioni istantanee. Questa architettura a due livelli (chiamati "layer") crea una sfida pratica: come trasferire fondi in modo efficiente tra questi due livelli senza intermediari centralizzati?

Il problema è concreto: ricevi un pagamento Lightning ma vuoi conservarlo in Cold storage, oppure hai bitcoin on-chain ma hai bisogno di liquidità su Lightning. Le soluzioni tradizionali prevedono l'apertura/chiusura manuale dei canali Lightning (costosa e tecnica) o l'uso di piattaforme centralizzate che richiedono KYC (identificazione "Know Your Customer").

Zeus Swap risolve questo problema con un servizio di scambio automatico e non-custodial. Sviluppato da Zeus LSP, consente di passare bitcoin da on-chain su Lightning e viceversa, senza affidare i fondi a un intermediario. Il processo utilizza gli [Hash Time Locked Contracts (HTLC)](https://planb.academy/en/resources/glossary/htlc) che garantiscono che lo scambio si completi o venga annullato.

L'innovazione sta nella semplicità: pochi clic per uno scambio che preserva la tua sovranità finanziaria, senza registrazione o KYC (Know Your Customer).

## Cos'è Zeus Swap?

Zeus Swap è un servizio di scambio di liquidità sviluppato da Zeus LSP che consente swap atomici tra il layer Bitcoin principale e Lightning Network. È un'infrastruttura tecnica che utilizza i "submarine swap" e i "reverse swap" per facilitare la conversione bidirezionale tra BTC on-chain e satoshi Lightning, mantenendo la natura non-custodial dell'operazione.

### Architettura tecnica

Zeus Swap utilizza la tecnologia open-source di Boltz per gli atomic swap Bitcoin/Lightning. Il protocollo si basa su Hash Time Locked Contracts (HTLC): contratti che bloccano fondi con due condizioni di rilascio (rivelazione di un segreto crittografico o scadenza temporale).

Per un submarine swap (on-chain → Lightning), l'utente invia bitcoin a un indirizzo che incorpora l'hash di una invoice Lightning. Zeus LSP sblocca questi fondi solo pagando la invoice corrispondente, rivelando la pre-image che sblocca automaticamente i bitcoin. Questo meccanismo garantisce l'atomicità.

Per un reverse swap (Lightning → on-chain), l'utente paga una invoice Lightning di Zeus LSP, rivelando una pre-image che permette il rilascio di una transazione Bitcoin già pronta verso l'indirizzo di destinazione.

Per maggiori dettagli sul funzionamento della Lightning Network, consulta il nostro corso dedicato:

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Modello di business

Zeus LSP agisce come market maker, mantenendo liquidità on-chain e Lightning per onorare gli swap. Per ogni swap, Zeus applica una commissione variabile (tipicamente 0,1% - 0,5% a seconda della direzione e delle condizioni) più la fee di mining di Bitcoin, mostrata in modo trasparente prima della conferma.

Come Lightning Service Provider, Zeus ottimizza i costi grazie alla sua esperienza nell'apertura di canali on-demand, routing efficiente e soluzioni di liquidità personalizzate.

### Integrazione

Zeus Wallet integra nativamente il servizio, permettendo gli swap senza uscire dall'interfaccia Bitcoin/Lightning. Questo elimina l'attrito del copia-incolla tra applicazioni.

L'interfaccia web indipendente rimane accessibile a tutti i wallet, garantendo la massima flessibilità d'uso.

## Caratteristiche principali

### Swap bidirezionali

Zeus Swap offre due tipi di swap:

**Submarine swaps (on-chain → Lightning)**: immette liquidità Lightning partendo dai bitcoin on-chain. Utile per alimentare un wallet mobile o un nodo Lightning senza aprire canali manualmente.

**Reverse swaps (Lightning → on-chain)**: converte satoshi da Lightning verso il layer uno per mantenere bitcoin a lungo termine, evitando costose chiusure di canale.

### Interfacce utente

**Interfaccia web** (swaps.zeuslsp.com): esperienza semplificata senza registrazione, processo guidato con visualizzazione in tempo reale di commissioni e stato.

**Integrazione Zeus Wallet**: swap diretti dall'applicazione, gestione automatica di invoice e indirizzi, eliminando errori di gestione.

### Sicurezza e recupero

Ogni swap genera un contratto unico con parametri immutabili: hash Lightning, timeout, indirizzo di rimborso. In caso di fallimento, recupero automatico tramite l'indirizzo fornito, indipendentemente da Zeus LSP.

**Zeus Swaps Rescue Key**: durante uno swap on-chain → Lightning, Zeus genera automaticamente una chiave di recupero universale (Rescue Key) che sostituisce i vecchi file di rimborso individuali. Questa chiave funziona su qualsiasi dispositivo e per tutti gli swap creati con essa. Scaricala e conservala in un luogo sicuro per poter recuperare i fondi in caso di errore nello swap.

### Ottimizzazione della rete

Zeus Swap regola automaticamente i tempi di scadenza e le commissioni di mining in base alle condizioni della rete. Gli utenti Zeus possono scegliere LSP, scadenze personalizzate e compatibilità con altri servizi (Boltz).

## Installazione e utilizzo

### Metodi di accesso

**Interfaccia web** (swaps.zeuslsp.com): soluzione universale compatibile con tutti i wallet, senza installazione, ideale per un uso occasionale.

**App Zeus** (iOS/Android): esperienza integrata che combina wallet e swap, adatta agli utenti regolari.

Consulta il nostro tutorial Zeus per conoscere meglio questo wallet:

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Configurazione web

**On-chain → Lightning**: inizia configurando lo swap sull'interfaccia web di Zeus Swap. Usa la freccia tra i campi on-chain e Lightning per invertire la direzione dello swap.

![Interface de création de swap](assets/fr/01.webp)

*Interfaccia Zeus Swap: seleziona importo (Sats 50.000 → Sats 49.648 dopo le commissioni) con visualizzazione trasparente delle fee di rete (Sats 302) e del servizio Zeus (Sats 50).*

Durante il processo, Zeus ti propone di scaricare la Rescue Key:

![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)

*Finestra di download della Zeus Swaps Rescue Key - Rescue Key che sostituisce i vecchi file di rimborso.*

Se possiedi già una chiave, Zeus permette di verificarla:

![Vérification de la clé existante](assets/fr/03.webp)

*Interfaccia per controllare la validità della Zeus Swaps Rescue Key esistente.*

Una volta configurato, Zeus genera l'indirizzo di ricezione Bitcoin e mostra le istruzioni:

![Adresse de dépôt et instructions](assets/fr/04.webp)

*Pagina di completamento swap: QR code e indirizzo Bitcoin per inviare 50.000 Sats, con promemoria della scadenza di 24 ore.*

Lo swap attende la conferma Bitcoin:

![Attente de confirmation](assets/fr/05.webp)

*Stato "Transaction in Mempool" ("Transazione in Mempool") - in attesa della conferma Bitcoin per completare lo swap.*

Una volta confermato, lo swap si completa automaticamente:

![Swap réussi](assets/fr/06.webp)

*Conferma di successo: 49.648 Sats ricevuti su Lightning dopo la detrazione delle commissioni di rete e servizio.*

### Uso dell'app Zeus

**Lightning → On-chain**: l'app Zeus offre un'esperienza integrata per il reverse swap (Lightning → Bitcoin).

![Navigation vers les swaps dans Zeus](assets/fr/07.webp)

*Schermata principale Zeus con bilanci Lightning (69.851 Sats) e on-chain (38.018 Sats), accesso agli swap dal menu laterale.*

![Configuration du swap reverse](assets/fr/08.webp)

*Creazione reverse swap: 50.000 Sats Lightning → 49.220 Sats on-chain, con commissioni di rete (530 Sats) e servizio (250 Sats) chiaramente indicate. Inserisci manualmente un indirizzo Bitcoin o genera uno automaticamente dal Wallet Zeus con il pulsante "generate on-chain Address" ("genera indirizzo on-chain").*

![Finalisation du swap mobile](assets/fr/09.webp)

*Schermate di completamento: pagamento invoice Lightning con "PAY THIS INVOICE" ("Paga questa invoice"), conferma pagamento Lightning in 9,96 secondi e bilancio con 49.162 Sats in attesa di conferma.*

### Monitoraggio e sicurezza

Ogni swap ha un identificatore unico con tracciamento in tempo reale. Visualizzazione completa dello stato, avvisi automatici per scadenze, suggerimenti sulle fee secondo le condizioni della rete.

## Vantaggi e limiti

### Vantaggi

- **Semplicità**: scambia con pochi clic invece di gestire manualmente i canali
- **Non-custodial**: niente KYC (identificazione "Know Your Customer"), niente account, fondi sempre sotto il tuo controllo
- **Trasparenza**: commissioni visualizzate prima della conferma (0,1%-0,5% + mining, da verificare le fee attuali)
- **Integrazione mobile**: esperienza nativa in Zeus Wallet

### Limiti

- **Tempi di scadenza**: massimo 24-48h, fallimento se la transazione Bitcoin non è confermata in tempo
- **Limiti di importo**: minimo 25.000 Sats, liquidità Zeus LSP variabile
- **Tracce lasciate on-chain**: script HTLC potenzialmente identificabili dalla blockchain analysis
- **Conferma necessaria**: minimo 10 minuti per la validazione dei blocchi su Bitcoin

## Buone pratiche

### Tempi e costi

- Controlla Mempool.space per cercare i periodi di bassa congestione della rete
- Fai swap durante i weekend e le ore non di punta per ridurre le fee di mining
- Valuta i costi: importi piccoli vs apertura diretta di canali

### Sicurezza

- Controlla attentamente gli indirizzi Bitcoin (consigliato copia-incolla)
- Salva la Zeus Swaps Rescue Key in un luogo sicuro
- Salva le informazioni: ID del contratto, indirizzo di rimborso, data di scadenza
- Usa fee di mining adeguate per avere una conferma tempestiva

### Strategia d'uso

- Bilancia liquidità On-chain/Lightning secondo le necessità
- Usa Zeus Swap per aggiustamenti occasionali, canali diretti per necessità permanenti

## Confronto con altri servizi di swap

### Zeus Swap vs Boltz Exchange

Zeus Swap utilizza la tecnologia backend di Boltz, ma con miglioramenti chiave:

**Vantaggi di Zeus Swap**:

- **Interfaccia unificata**: integrazione nativa in Zeus Wallet vs interfaccia web di Boltz
- **WebSocket API**: aggiornamenti in tempo reale vs polling manuale
- **Gestione automatica**: creazione automatica di invoice e indirizzi
- **Supporto mobile**: smartphone vs ottimizzazione solo su desktop
- **Documentazione Swagger**: REST API completa per gli sviluppatori

**Boltz** resta vantaggioso per avere una completa indipendenza e per l'utilizzo con qualsiasi setup Bitcoin/Lightning.

Zeus Swap trasforma la tecnologia comprovata di Boltz in un'esperienza utente mainstream, come succede con la differenza tra protocollo per developer e applicazioni user-friendly.

### Zeus Swap vs Phoenix/Breez (swap integrati)

Phoenix e Breez integrano swap trasparenti che nascondono la complessità tecnica dello stesso. Phoenix usa un sistema automatico swap-in/swap-out dove l'utente "manda a un indirizzo Bitcoin" e l'app gestisce lo swap in background.

Questo approccio ultra-semplificato è adatto ai principianti, ma limita comprensione e controllo. Zeus Swap adotta una filosofia educativa: l'utente capisce che sta scambiando tra due livelli distinti, sviluppando gradualmente la conoscenza dell'ecosistema Bitcoin a due livelli.

## Confronto dettagliato di commissioni e limiti (2024)

⚠️ **Attenzione**: le fee possono variare nel tempo secondo le condizioni di mercato e gli aggiornamenti del servizio. Controlla sempre le fee mostrate nell'interfaccia prima di confermare uno swap.


| Servizio | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Importo minimo |
| ------------- | ----------------------- | --------------------- | --------------- |
| **Zeus Swap** | ~0.1% + commissioni minerarie | 0.5% + commissioni minerarie | 25.000 sats |
| **Boltz** | 0.2% + commissioni minerarie | 0.5% + commissioni minerarie | 50.000 sats |
| **Phoenix** | Solo commissioni minerarie | 0.4% fisso | 10.000 sats |
| **Breez** | 0.25% + commissioni di rete | 0.5% + commissioni minerarie | 50.000 sats |

Zeus Swap offre equilibrio tra facilità d'uso e controllo tecnico: più accessibile di Boltz, più flessibile di Phoenix/Breez, con approccio rigorosamente non-custodial.

## Conclusione

Zeus Swap rappresenta un'innovazione significativa nell'ecosistema Bitcoin, risolvendo elegantemente la sfida dell'interoperabilità tra rete principale e Lightning Network. Combinando la robustezza crittografica degli atomic swap con un'esperienza utente accessibile, democratizza la gestione a due livelli di Bitcoin senza compromettere la sovranità finanziaria.

L'architettura non-custodial di Zeus Swap, ereditata dalla tecnologia comprovata di Boltz, garantisce che i fondi restino sotto il tuo esclusivo controllo durante tutto il processo. Trasparenza dei prezzi e assenza di KYC (pratiche "Know Your Customer") rafforzano questa proposta di valore unica.

Per l'utente moderno, Zeus Swap è uno strumento strategico per ottimizzare la distribuzione della liquidità: on-chain per risparmio a lungo termine, Lightning per spese quotidiane e micropagamenti. Questa flessibilità trasforma la gestione del Bitcoin da vincolo tecnico a vantaggio competitivo.

L'evoluzione futura di Zeus Swap, supportata dal team esperto di Zeus LSP e dalla comunità open-source Boltz, promette miglioramenti in costi, tempi di elaborazione ed esperienza utente. Il servizio si inserisce nella tendenza alla maturazione dell'infrastruttura Bitcoin, dove la sofisticazione tecnica diventa trasparente per l'utente finale.

## Risorse

### Documentazione ufficiale

- [Zeus Swap - Portale web](https://swaps.zeuslsp.com)
- [Zeus Wallet - App mobile](https://zeusln.app)
- [Blog Zeus - Annunci e tutorial](https://blog.zeusln.com)
- [Documentazione tecnica Zeus](https://docs.zeusln.app)

### Comunità e supporto

- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)

---
name: Scambio di Zeus
description: Servizio non custodiale Exchange tra On-Chain e Lightning Network bitcoin
---

![cover](assets/cover.webp)



L'ecosistema Bitcoin presenta una dualità: la rete principale (On-Chain) offre la massima sicurezza, mentre la Lightning Network consente transazioni istantanee. Questa architettura a due Layer crea una sfida pratica: come trasferire in modo efficiente i fondi tra questi due livelli senza intermediari centralizzati?



Il problema è concreto: si riceve un pagamento Lightning ma si desidera conservarlo in un deposito Cold o, viceversa, si dispone di bitcoin On-Chain ma si ha bisogno di liquidità Lightning. Le soluzioni tradizionali prevedono l'apertura/chiusura manuale dei canali Lightning (costosa e tecnica) o piattaforme centralizzate che richiedono il KYC.



Zeus Swap risolve questo problema con un servizio Exchange automatizzato e non depositario. Sviluppato da Zeus LSP, consente di convertire i bitcoin On-Chain in satoshi Lightning in modo bidirezionale, senza affidare i propri fondi a un intermediario. Il processo utilizza contratti atomici (HTLC) che garantiscono il completamento o l'annullamento della Exchange.



L'innovazione sta nella sua semplicità: pochi clic per un Exchange che preserva la vostra sovranità finanziaria, senza bisogno di registrazione o KYC.



## Che cos'è Zeus Swap?



Zeus Swap è un servizio di liquidità Exchange sviluppato da Zeus LSP che permette di effettuare swap atomici tra la rete principale Bitcoin e Lightning Network. Si tratta di un'infrastruttura tecnica che utilizza swap sottomarini e reverse swap per facilitare la conversione bidirezionale tra BTC On-Chain e satoshi Lightning, preservando la natura non custodiale dell'operazione.



### Architettura tecnica



Zeus Swap utilizza la tecnologia open-source Bitcoin/Lightning atomic swap di Boltz. Il protocollo utilizza i Hash Time Locked Contracts (HTLC): contratti che bloccano i fondi con due condizioni di rilascio (rivelazione di un segreto crittografico o scadenza del tempo).



Per uno swap sottomarino (On-Chain → Lightning), l'utente invia bitcoin a un Address che incorpora il Hash di un Invoice Lightning. Zeus LSP sblocca questi fondi solo pagando il Invoice corrispondente, rivelando la pre-immagine che sblocca automaticamente i bitcoin. Questo meccanismo garantisce l'atomicità.



Per un reverse swap (Lightning → On-Chain), l'utente paga un Lightning Invoice da Zeus LSP, rivelando una pre-immagine che consente il rilascio di una transazione Bitcoin preparata al Address di destinazione.



Per maggiori dettagli sul funzionamento del Lightning Network, consultate il nostro corso dedicato:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Modello di business



Zeus LSP agisce come market maker, mantenendo la liquidità di On-Chain e Lightning per onorare gli swap. Per gli swap, Zeus applica una commissione variabile (in genere dallo 0,1% allo 0,5% a seconda della direzione e delle condizioni) più la commissione Mining del Bitcoin, visualizzata in modo trasparente prima della convalida.



In qualità di Lightning Service Provider, Zeus ottimizza i costi grazie alla sua esperienza nell'apertura di canali on-demand, nel routing efficiente e nelle soluzioni di liquidità personalizzate.



### Integrazione



Zeus Wallet integra il servizio in modo nativo, consentendo lo scambio senza lasciare Interface Bitcoin/Lightning. Questo elimina l'attrito del copia e incolla tra le applicazioni.



Il web indipendente Interface rimane accessibile a tutti i portafogli, garantendo la massima flessibilità di utilizzo.



## Caratteristiche principali



### Scambi bidirezionali



Zeus Swap offre due tipi di Exchange:



**Submarine swaps (On-Chain → Lightning)**: inietta liquidità Lightning dalle riserve Bitcoin, utile per alimentare un nodo mobile Wallet o Lightning senza aprire manualmente i canali.



**Scambi inversi (Lightning → On-Chain)**: convertire i satoshi Lightning in bitcoin On-Chain da conservare a lungo termine, evitando costose chiusure di canali.



### Interfacce utente



**Interface web** (swaps.zeuslsp.com): esperienza semplificata senza registrazione, processo guidato con visualizzazione in tempo reale delle spese e dello stato.



**Integrazione con Zeus Wallet**: scambi diretti dall'applicazione, gestione automatica di fatture e indirizzi, eliminazione degli errori di gestione.



### Sicurezza e recupero



Ogni swap genera un Contract unico con parametri immutabili: Hash Lightning, timeout, rimborso Address. In caso di guasto, recupero automatico tramite il Address fornito, indipendentemente da Zeus LSP.



**Zeus Swaps Rescue Key**: durante uno scambio On-Chain → Lightning, Zeus genera automaticamente una chiave di recupero universale che sostituisce i vecchi file di rimborso individuali. Questa chiave unica funziona su qualsiasi dispositivo e per tutti gli swap creati con essa. È fondamentale scaricare e salvare questa chiave in un luogo sicuro per poter recuperare i fondi in caso di fallimento dello swap.



### Ottimizzazione della rete



Zeus Swap regola automaticamente i tempi di scadenza e le tariffe Mining in base alle condizioni della rete. Gli utenti di Zeus beneficiano di opzioni avanzate: scelta del LSP, ritardi personalizzati, compatibilità con altri servizi (Boltz).



## Installazione e utilizzo



### Metodi di accesso



**Interface web** (swaps.zeuslsp.com): soluzione universale compatibile con tutti i portafogli, non richiede installazione, ideale per un uso occasionale.



**Zeus app** (iOS/Android): esperienza integrata che combina Wallet e swap, adatta agli utenti abituali.



Consultate il nostro tutorial su Zeus per saperne di più su questo Wallet completo:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Configurazione web



**On-Chain → Fulmine**: Il processo inizia configurando lo scambio sul web Zeus Swap del Interface. L'utente può utilizzare la freccia tra i campi On-Chain e Lightning per invertire la direzione dello scambio.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: selezione dell'importo (Sats 50.000 → Sats 49.648 dopo le spese) con visualizzazione trasparente delle spese di rete (Sats 302) e del servizio Zeus (Sats 50)*



Durante il processo, Zeus offre la possibilità di scaricare la chiave di recupero universale:



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Dialogo per il download della Zeus Swaps Rescue Key - una chiave universale che sostituisce i vecchi file di rimborso individuali*



Se si dispone già di una chiave, Zeus consente di verificarla:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface per verificare la validità di una chiave di salvataggio Zeus Swaps esistente*



Una volta configurato, Zeus genera il deposito Bitcoin Address e visualizza le istruzioni :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Pagina di completamento dello scambio: Codice QR e Bitcoin Address per l'invio di 50.000 Satss, con promemoria della data di scadenza di 24 ore*



Lo scambio attende quindi la conferma del Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Stato "Transazione in Mempool" - in attesa della conferma del Bitcoin per finalizzare lo scambio*



Una volta confermato, lo scambio viene completato automaticamente:



![Swap réussi](assets/fr/06.webp)



*Conferma del successo: 49.648 Sats ricevuti su Lightning dopo aver dedotto le spese di rete e di servizio*



### Utilizzo dell'applicazione Zeus



**Lightning → On-Chain**: L'applicazione Zeus offre un'esperienza integrata per i reverse swap (da Lightning a Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Schermata principale di Zeus che mostra i saldi di Lightning (69.851 Sats) e On-Chain (38.018 Sats), accesso agli scambi tramite il menu laterale*



![Configuration du swap reverse](assets/fr/08.webp)



*Creazione reverse swap Interface: 50.000 Sats Lightning → 49.220 Sats On-Chain, con i costi di rete (530 Sats) e di servizio (250 Sats) chiaramente indicati. Gli utenti possono inserire manualmente un Bitcoin ricevendo un Address, oppure un generate automaticamente dal Wallet Zeus tramite il pulsante "generate On-Chain Address"*



![Finalisation du swap mobile](assets/fr/09.webp)



*Schermate di finalizzazione: Schermata di pagamento Lightning Invoice con "PAGA QUESTO Invoice", conferma del successo del pagamento Lightning in 9,96 secondi, ed estratto conto del saldo con i 49.162 Sats in attesa di conferma*



### Sorveglianza e sicurezza



Ogni swap ha un identificativo unico con tracciamento in tempo reale. Visualizzazione completa dello stato di avanzamento, avvisi automatici per le date di scadenza. Raccomandazioni di ricarica automatica in base alle condizioni della rete.



## Vantaggi e limiti



### Vantaggi





- Semplicità**: Scambio in pochi click rispetto alla manipolazione manuale dei canali
- Non-custodiale**: nessun KYC, nessun conto, i fondi non vengono mai affidati a terzi
- Trasparenza**: le commissioni vengono visualizzate esplicitamente prima della convalida (da 0,1% a 0,5% + minime a seconda dei test degli utenti - verificare le commissioni correnti ad ogni swap)
- Integrazione mobile**: esperienza nativa in Zeus Wallet



### Limitazioni





- Tempi di scadenza**: 24-48h al massimo, fallimento se Bitcoin non viene confermato in tempo
- Limiti d'importo**: minimo 25.000 Sats, liquidità Zeus LSP variabile a seconda delle condizioni
- Tracce On-Chain**: Script HTLC potenzialmente identificabili dall'analisi Blockchain
- Conferma richiesta**: minimo 10 minuti per la convalida di Bitcoin



## Le migliori pratiche



### Tempi e costi





- Osservare Mempool.space per i periodi di bassa congestione
- Preferite i fine settimana e le ore non di punta per ridurre i costi di Mining
- Calcolo della redditività: piccoli importi vs. apertura diretta del canale



### Sicurezza





- Controllare attentamente gli indirizzi Bitcoin (si consiglia il copia-incolla)
- Backup della chiave di recupero di Zeus Swaps**: scaricare e conservare la chiave di recupero in un luogo sicuro
- Documento: ID Contract, rimborso Address, data di scadenza
- Utilizzare le tariffe Mining appropriate per una conferma tempestiva



### Strategia d'uso





- Bilanciamento On-Chain/Lightning liquidity in base alle proprie esigenze
- Zeus Swap per adeguamenti una tantum, canali diretti per esigenze permanenti



## Confronto con altri servizi di swap



### Zeus Swap vs Boltz Exchange



Zeus Swap utilizza la tecnologia backend di Boltz, ma apporta alcuni miglioramenti fondamentali:



**Benefici dello scambio di Zeus** :




- Interface unificato**: integrazione nativa in Zeus Wallet vs Interface tecnica web Boltz
- API WebSocket**: aggiornamenti in tempo reale rispetto al polling manuale
- Gestione automatizzata**: fatturazione automatica e gestione del Address
- Supporto mobile**: ottimizzazione solo per smartphone e desktop
- Documentazione Swagger**: API REST completa per gli sviluppatori



**Boltz rimane vantaggioso** per la totale indipendenza e l'utilizzo con qualsiasi configurazione Bitcoin/Lightning.



Zeus Swap trasforma la collaudata tecnologia Boltz in un'esperienza utente mainstream, paragonabile alla differenza tra un protocollo grezzo e un'applicazione di facile utilizzo.



### Zeus Swap vs Phoenix/Breez (scambi integrati)



Phoenix e Breez integrano funzionalità di swap trasparenti che nascondono la complessità tecnica all'utente finale. Phoenix utilizza un sistema automatico di swap-in/swap-out in cui l'utente non distingue esplicitamente tra i livelli Bitcoin: "invia a un Bitcoin Address" e l'applicazione gestisce lo scambio in background.



Questo approccio ultra-semplificato è perfettamente adatto ai principianti, ma limita la comprensione e il controllo delle operazioni. Zeus Swap adotta una filosofia più educativa: gli utenti capiscono che stanno scambiando tra due livelli distinti, sviluppando gradualmente la loro comprensione dell'ecosistema Layer Bitcoin.



## Confronto dettagliato delle tariffe e dei limiti (2024)



⚠️ **Attenzione**: Le tariffe possono variare nel tempo a seconda delle condizioni di mercato e degli aggiornamenti del servizio. Controllare sempre le tariffe visualizzate nel Interface prima di convalidare uno scambio.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

Zeus Swap offre un equilibrio tra facilità d'uso e controllo tecnico: più accessibile di Boltz, più flessibile di Phoenix/Breez, con un approccio rigoroso e non custodiale.



## Conclusione



Zeus Swap rappresenta un'innovazione significativa nell'ecosistema Bitcoin, risolvendo in modo elegante la sfida dell'interoperabilità tra la rete principale e il Lightning Network. Combinando la solidità crittografica degli swap atomici con un'esperienza utente accessibile, questo servizio democratizza la gestione del Bitcoin dual-Layer senza compromettere i principi della sovranità finanziaria.



L'architettura non custodiale di Zeus Swap, ereditata dalla collaudata tecnologia Boltz, garantisce che i vostri fondi rimangano sotto il vostro esclusivo controllo durante l'intero processo di swap. Questo approccio rispetta lo spirito del Bitcoin, offrendo al contempo la convenienza per l'utente necessaria per l'adozione mainstream. La trasparenza dei prezzi e l'assenza di processi KYC rafforzano questa proposta di valore unica.



Per l'utente moderno di Bitcoin, Zeus Swap è uno strumento strategico per ottimizzare la distribuzione della liquidità in base alle esigenze: On-Chain deposito sicuro per i risparmi a lungo termine, disponibilità lightning per le spese quotidiane e le microtransazioni. Questa flessibilità trasforma la gestione del Bitcoin da vincolo tecnico a vantaggio competitivo.



L'evoluzione futura di Zeus Swap, supportata dal team esperto di Zeus LSP e dalla comunità open-source di Boltz, promette continui miglioramenti in termini di costi, tempi di elaborazione ed esperienza utente. Questo servizio fa parte della più ampia tendenza alla maturazione dell'infrastruttura Bitcoin, in cui la sofisticazione tecnica diventa trasparente per l'utente finale.



## Risorse



### Documentazione ufficiale




- [Zeus Swap - Portale web](https://swaps.zeuslsp.com)
- [Zeus Wallet - Applicazione mobile](https://zeusln.app)
- [Blog Zeus - Annunci e tutorial](https://blog.zeusln.com)
- [Documentazione tecnica Zeus](https://docs.zeusln.app)



### Comunità e supporto




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegramma Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)
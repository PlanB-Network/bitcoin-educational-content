---
name: Soluzione di acquisto-vendita Bitcoin peer-to-peer
goal: Esplorare le soluzioni di acquisto e vendita di Bitcoin non-KYC
objectives:
  - Comprendere i diversi tipi di KYC, i loro rischi e benefici
  - Comprendere i vantaggi di un acquisto peer-to-peer
  - Implementare la soluzione che corrisponde alle proprie esigenze
  - Migliorare la gestione dei propri UTXO (KYC e non-KYC)
---

# Un viaggio nel mondo del non-KYC

Pierre ci propone questo corso che ci introduce alle diverse soluzioni esistenti per acquistare e vendere Bitcoin peer-to-peer. L'acquisto peer-to-peer è completamente legale e consente di avere maggiore anonimato, infatti queste soluzioni non sono KYC. Il KYC (Know Your Customer) è una regola dei regolatori di mercato (AMF) che consiste nel richiedere un documento d'identità al cliente che desidera acquistare o vendere Bitcoin. Queste regole hanno lo scopo di prevenire il riciclaggio di denaro, il finanziamento del terrorismo e l'evasione fiscale. A rischio di importanti conseguenze per l'utente, il KYC ha l'obiettivo di difendere e proteggere l'utente, anche se molto spesso si osserva l'effetto contrario.

Esploreremo quindi i diversi tipi di KYC (full KYC tipo Francia, KYC Light tipo Svizzera e non-KYC tipo peer-to-peer). Pierre ci presenterà più di 6 soluzioni, quindi avrete tutte le carte in mano per scoprire quella che fa per voi. Se desiderate una soluzione KYC, sappiate che sono presenti nella formazione BTC 102.

+++

# Introduzione

## Spiegazione e tipo di KYC

Il KYC, per "Know Your Customer" (Conosci il tuo cliente), è una norma regolamentare che richiede la raccolta di informazioni private dei clienti, come il loro indirizzo fisico, il documento d'identità o i loro estratti conto bancari. Questa pratica è comune sulle piattaforme di intermediazione, che possono richiedere un KYC completo, comprendente informazioni dettagliate come un documento d'identità, una foto, una prova di residenza, schede di stipendio, ecc.

L'obiettivo principale del KYC è combattere il riciclaggio di denaro, il finanziamento del terrorismo e l'evasione fiscale. Si tratta di una legge introdotta dall'AMF (Autorità dei mercati finanziari), l'organo di regolamentazione del mercato francese. Tuttavia, l'applicazione del KYC comporta la centralizzazione di basi di dati molto sensibili contenenti informazioni personali degli utenti. Queste informazioni, avendo un certo valore, possono essere vendute a entità malintenzionate.

Inoltre, le piattaforme di scambio spesso richiedono una quantità eccessiva di informazioni personali, mettendo così gli utenti in pericolo e aumentando i costi di conformità. Questi costi regolamentari possono scoraggiare le imprese francesi e danneggiare la loro competitività a livello internazionale.
Esistono tre tipi di KYC, tra cui il full KYC che richiede una raccolta completa e regolamentata di informazioni per accedere al servizio. In Svizzera, un'alternativa chiamata "KYC light" consente l'acquisto e la vendita di bitcoin senza fornire un documento d'identità, purché l'importo di acquisto non superi i 1000 euro al giorno. Soluzioni come Relay consentono di utilizzare questo metodo.

In questo contesto, le autorità svizzere possono accedere alle informazioni bancarie per indagare sulle persone considerate a rischio. Gli indirizzi di consegna dei bitcoin sono anche tracciabili tramite il sistema bancario. Il KYC light è generalmente considerato più semplice e meno costoso del sistema francese.

In Francia, l'acquisto di bitcoin online richiede l'invio di denaro a un terzo, tramite bonifico SEPA o Paypal. Per coloro che preferiscono l'anonimato, la sicurezza e la privacy, sono disponibili anche soluzioni per l'acquisto di bitcoin in contanti. Per volumi bassi, l'acquisto di bitcoin in contanti è un'opzione semplice e legale.

Per poter vendere quotidianamente PLT di 100 euro di bitcoin a chiunque, è necessaria una regolamentazione da parte dell'AMF (Autorité des Marchés Financiers). In Francia, questa regolamentazione si applica principalmente ai privati che effettuano volumi elevati di transazioni. Le altre due modalità di acquisto di bitcoin includono l'uso di sportelli automatici (ATM) e gli scambi tra amici. Gli ATM sono regolamentati e richiedono un documento d'identità per transazioni superiori a 500 euro. Lo scambio tra amici, invece, offre un'esposizione al bitcoin in modo più discreto.

Queste misure regolatorie sono in atto per contrastare il finanziamento del terrorismo, l'evasione fiscale e il riciclaggio di denaro. Il bitcoin, come database completamente tracciabile, rende il riciclaggio di denaro particolarmente difficile. L'uso di Bitcoin da parte dei criminali può essere rintracciato, il che rende il Bitcoin uno strumento poco efficace per il riciclaggio di denaro.

È importante notare che questa formazione presenta diverse alternative, nonché strumenti che possono essere utilizzati per scopi malintenzionati o meno. Inoltre, offre spiegazioni sul funzionamento degli order book tra i makers (fornitori di ordini) e i takers (prenditori di ordini).
È anche importante notare che le informazioni presentate qui non sostengono alcuna soluzione in particolare. Si tratta semplicemente di presentare le opzioni disponibili per una migliore comprensione dell'argomento. Per ulteriori domande sul Bitcoin, non esitate a consultare risorse online come www.découvrebitcoin.com.

## Confronto delle soluzioni di acquisto-vendita peer-to-peer

Soluzioni P2P per l'acquisto di Bitcoin: Bisq, RoboSat, LNP2PBot, Peach e HodlHodl

L'acquisto di Bitcoin peer-to-peer (P2P) è un'opzione preferita dagli investitori che desiderano evitare le piattaforme di scambio centralizzate. Questa parte del corso esamina diverse soluzioni P2P disponibili, tra cui Bisq, RoboSat, LNP2PBot, Peach e HodlHodl.
Confronto dei vantaggi e degli svantaggi delle diverse soluzioni

Ogni soluzione P2P ha i propri vantaggi e svantaggi. Qui di seguito forniamo una panoramica delle caratteristiche chiave di ogni soluzione.

### Bisq

[Bisq](https://bisq.network/) è una soluzione P2P non custodiale che dispone di un sistema DAO (Organizzazione Autonoma Decentralizzata) e utilizza il multisign per la gestione delle controversie. Il suo codice è open source, il che contribuisce alla sua robustezza e alla protezione della privacy degli utenti.

| Vantaggi                                        | Svantaggi                                                                                     |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------- |
| - Soluzione P2P, non custodiale, multisign, DAO | - L'applicazione è abbastanza pesante e non molto user-friendly, disponibile solo su computer |
| - Robusta e sicura                              | - I limiti di acquisto e vendita e la gestione degli account con firme sono a doppio taglio.  |
| - Open source                                   |                                                                                               |

### RoboSat

[RoboSat](https://learn.robosats.com/) è una soluzione facile da usare, veloce, che funziona su TOR e non richiede un account. È open source e utilizza il Lightning Network per consentire transazioni veloci.

| Vantaggi                                               | Svantaggi                                                                 |
| ------------------------------------------------------ | ------------------------------------------------------------------------- |
| - Facile da usare                                      | - Il protocollo è fragile con un solo coordinatore                        |
| - Commissioni di transazione basse                     | - Richiede conoscenze tecniche e una comprensione della privacy           |
| - Utilizza il Lightning Network per transazioni veloci | - L'applicazione Umbrell consente di gestire la propria istanza di client |
| - Open source                                          |                                                                           |

### LNP2PBot

[LNP2PBot](https://lnp2pbot.com/) è accessibile tramite Telegram per l'acquisto di Bitcoin senza KYC. Offre transazioni veloci grazie al Lightning Network e commissioni basse.

| Vantaggi                                                    | Svantaggi                                                   |
| ----------------------------------------------------------- | ----------------------------------------------------------- |
| - Accessibile tramite Telegram                              | - Meno robusto e sicuro rispetto alle altre soluzioni       |
| - Velocità grazie al Lightning Network                      | - Meno veloce e meno user-friendly di Robosat               |
| - Commissioni di transazione basse                          | - Può essere collegato all'identità Telegram dell'utente    |
| - Gestione delle controversie internamente                  | - Mancanza di liquidità e fragilità dell'applicazione       |
| Proposte comunitarie per limitare il problema della fiducia | LNP2Pbot deve essere affidabile per gestire le controversie |

### Peach

[Peach](https://peachbitcoin.com/) è un'applicazione mobile dedicata al trading di Bitcoin. Si distingue per la sua semplicità, non richiedendo la creazione di un account per operare. Gli scambi sono veloci, anche in assenza di Lightning Network. Inoltre, le notifiche sui telefoni accelerano il processo di transazione.

| Vantaggi                                                              | Svantaggi                                                                                                                  |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| - Utilizzo semplificato: non è necessaria la creazione di un account. | - Sicurezza e robustezza: essendo legata a un'azienda, Peach presenta potenziali debolezze in termini di sicurezza.        |
| - Velocità di transazione: gli scambi sono rapidi.                    | - Assenza di Lightning Network: questa tecnologia, che consente transazioni Bitcoin più veloci, non è utilizzata da Peach. |
| - Notifiche: accelerano il processo di transazione.                   |                                                                                                                            |

### HodlHodl

[HodlHodl](https://hodlhodl.com/) è una soluzione non custodiale per lo scambio di Bitcoin. Offre numerosi vantaggi come una forte liquidità, la possibilità di scambi privati, un sistema di referral, nonché account con cronologia degli scambi e un sistema di valutazione. Tuttavia, gli scambi sono legati all'indirizzo email e all'identità digitale dell'utente, memorizzati presso HodlHodl. Inoltre, il codice sorgente di HodlHodl non è aperto al pubblico e l'applicazione non può essere utilizzata con Tor.

| Vantaggi                                                                                                                          | Svantaggi                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| - Non custodiale: l'utente rimane in possesso delle sue chiavi private.                                                           | - Memorizzazione delle informazioni personali: l'indirizzo email e l'identità digitale dell'utente sono memorizzati da HodlHodl.  |
| - Liquidità: HodlHodl offre una vasta gamma di possibilità di scambio.                                                            | - Codice sorgente chiuso: il codice di HodlHodl non è aperto al pubblico.                                                         |
| - Possibilità di scambi privati: l'utente può scegliere con chi scambiare.                                                        | - Incompatibilità con Tor: HodlHodl non può essere utilizzato con questa rete incentrata sulla privacy.                           |
| - Sistema di referral: HodlHodl premia il passaparola.                                                                            | - Possibilità di KYC forzato: in alcune situazioni, HodlHodl può richiedere informazioni di identificazione per recuperare fondi. |
| - Cronologia degli scambi e sistema di valutazione: queste funzionalità consentono di valutare l'affidabilità degli altri utenti. |                                                                                                                                   |

## Conclusioni sulle soluzioni P2P

In sintesi, ogni soluzione P2P ha i suoi vantaggi e svantaggi. Bisq è considerata la più robusta e sicura, ma meno facile da utilizzare. RoboSat è open source ma meno robusta di Bisq. LNP2PBot è meno robusta e sicura rispetto alle altre soluzioni, meno veloce e meno user-friendly di RoboSat, ma più di Bisq. Peach è l'applicazione più facile e veloce per acquistare Bitcoin senza KYC, ma c'è un'azienda dietro, quindi ci sono debolezze in termini di sicurezza e robustezza. HodlHodl è un protocollo gestito da un'azienda e chiuso, quindi ci sono debolezze in termini di sicurezza e robustezza, ed è un po' più complicato di Peach.

Il buon vecchio contante di persona rimane sempre una soluzione per piccole somme.

Oltre alle soluzioni P2P, ci sono altre opzioni per lo scambio di criptovalute. kycnot.me offre servizi come VPN, VPS, SMS, ecc. Bitrefil consente di acquistare carte regalo. Ogni soluzione su [kycnotme](https://kycnot.me/) è presentata con i suoi punti positivi e negativi.

# Tutorial sulle soluzioni di acquisto/vendita P2P

## Robosats

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/) è un progetto open source sviluppato da Reckless Satoshi per scambiare in modo privato Bitcoin con valute nazionali. Semplifica l'esperienza peer-to-peer e utilizza fatture Lightning per ridurre al minimo le esigenze di custodia e fiducia. Per utilizzarlo, avremo bisogno di Tor, una rete di comunicazione anonima.

La prima cosa da fare è scaricare Tor. Puoi trovarlo su GitHub o direttamente sul sito ufficiale all'indirizzo: tor.org/download.
Una volta scaricato e installato Tor:

- Premi "Connect" per stabilire la connessione.
- Vai all'[indirizzo onion di robosats](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/).
- Copia il token per salvare la tua identità.

Ecco i passaggi per l'acquisto di Bitcoin con Robosats:

- Consulta il libro degli ordini, puoi filtrare per valuta e metodo di pagamento - ad esempio, acquistare Bitcoin in euro con Revolut.
- Prima di acquistare, verifica la scadenza dell'offerta, il prezzo in euro e il premio (puoi anche filtrare le offerte per premio)
- Preferibilmente, scegli un'offerta con un utente attivo e con un premio inferiore alla media.
- Verifica il riepilogo dell'ordine con l'importo, il metodo di pagamento, il premio, l'ID dell'ordine e la scadenza.
- È possibile ottenere i tuoi satoshi su un indirizzo bitcoin con una tassa di swap-out (da LN a BTC-onchain) dell'ordine del 1% (puoi modificare le tasse di mining on-chain).- In alternativa, crea una fattura con un portafoglio LN tra quelli presenti in questa [lista](https://learn.robosats.com/docs/wallets/) e copia la fattura su Robosats.
- Contatta il venditore tramite chat cifrata per discutere del pagamento in fiat.

Vediamo ora i passaggi per la vendita di bitcoin su Robosats:

- Personalizza la tua offerta scegliendo il metodo di pagamento, il premio, la durata di scadenza, ecc.
- La Fidelity Bond Size è l'equivalente del deposito cauzionale su BISC. Metti il 15% o il 10% di deposito cauzionale per incoraggiare l'altra parte a giocare pulito.
- Blocca i satoshi per confermare la creazione dell'ordine ed evitare lo spam.
- Se qualcuno accetta la tua offerta di vendita, discuti con il tuo partner per procedere al pagamento in fiat. Una volta effettuato il pagamento, lo scambio è completato e i satoshi sono venduti!

## BISQ: soluzione di acquisto peer to peer

[Bisq](https://bisq.network/) è una piattaforma di scambio decentralizzata per asset digitali, principalmente Bitcoin. Consente transazioni dirette, sicure e private tra utenti di tutto il mondo senza la necessità di un intermediario.

🚨 Si prega di fare attenzione quando si utilizza Bisq, poiché si tratta di una soluzione avanzata. Potrebbe non essere adatta per gli utenti principianti. Assicurati di avere una certa esperienza e comprensione prima di iniziare. 🚨

Esaminiamo in dettaglio questa soluzione, ecco i video tutorial:

![parte 1](https://tube.nuagelibre.fr/videos/watch/b3885ea9-23e9-4b58-aa3f-401348da85a1)

![parte 2](https://tube.nuagelibre.fr/videos/watch/53276305-70d6-4c7f-9df9-e100a82eee16)

Per i più esperti, ecco una guida sintetica che riassume rapidamente i passaggi essenziali:

1. Scarica e Installa: Visita il sito web di Bisq e scarica l'applicazione. Installala sul tuo sistema.
2. Configura la Modalità di Pagamento: Apri l'applicazione e vai su "Account". Aggiungi i dettagli del tuo metodo di pagamento.
3. Alimenta il tuo Portafoglio Bisq: Clicca su "Fondi" e "Ricevi Fondi" per ottenere il tuo indirizzo Bisq. Invia Bitcoin a questo indirizzo.
4. Effettua una Transazione: Clicca su "Acquista/Vendi" e scegli la transazione desiderata. Segui le istruzioni per completare la transazione.
5. Conferma la Ricezione: Una volta ricevuto il pagamento, confermalo nell'applicazione Bisq. Questo libera i Bitcoin dal deposito cauzionale.
   Ricorda sempre di verificare tutti i dettagli delle tue transazioni e di trattare solo con parti di fiducia.

Ecco una guida completa che ti guiderà attraverso tutti i passaggi per utilizzare Bisq.

BISQ è una rete decentralizzata e sicura che rispetta la tua proprietà privata. Infatti, è non custodiale, il che significa che possiedi sempre i tuoi fondi. Inoltre, BISQ utilizza un token, il BSQ, che ti consente di pagare commissioni di transazione più basse e stimola la tua partecipazione alla DAO (Organizzazione Autonoma Decentralizzata). Per proteggere i venditori durante le transazioni Bitcoin-fiat, BISQ ha introdotto un sistema di firme e limiti di conto. Come acquirente, dovrai ottenere un account firmato per aumentare il tuo limite di acquisto. La firma è anche un modo per verificare la storia dei trader, garantendo così la sicurezza delle transazioni.

Per installare Bisq e salvare i tuoi dati, segui questi semplici passaggi:

- Vai al sito bisc.network per scaricare il software (Screenshot della pagina di download)
- Verifica l'integrità del software utilizzando strumenti come quelli proposti da Loïc Morel per gli utenti Windows.
- Una volta verificato l'installatore, avvia BISQ, concedi le autorizzazioni necessarie e accetta i termini di utilizzo. (Screenshot dei termini di utilizzo)
- BISQ si connetterà alla rete Bitcoin e a se stesso tramite Tor, ciò potrebbe richiedere del tempo.
- Configura il tuo account di pagamento e fai il backup del tuo SID (Secure Identifier) del tuo portafoglio per prevenire eventuali perdite o furti. (Screenshot della pagina di configurazione dell'account)
- Imposta anche una password per crittografare le tue informazioni.

A seconda del tuo sistema operativo, i dati BISQ verranno memorizzati in posizioni diverse. Puoi trovarli nella cartella "Directory dei dati". Attenzione, se elimini questa cartella, tutti i tuoi dati BISQ saranno persi.
Per recuperare i tuoi dati tramite un backup:

- Copia la cartella di backup nella posizione 'utente/supporto applicazioni/BISQ'.
- Rinomina la cartella di backup in 'BISQ'.
- Riavvia BISQ e tutti i tuoi dati dovrebbero essere ripristinati.

Prima di iniziare a comprare o vendere Bitcoin su BISQ, è cruciale configurare il tuo account di pagamento. Puoi ad esempio configurare un account nella tua valuta nazionale, come un conto SEPA, un conto REVOLUT o un conto PAYPAL.
Per configurare il tuo conto REVOLUT:

- Aggiungi un conto e seleziona REVOLUT dall'elenco delle opzioni. (Screenshot dell'elenco delle opzioni di conto)
- Puoi scegliere diverse valute: euro, sterlina britannica, dollaro americano o franco svizzero.
- La durata massima della transazione è di un giorno e il limite di acquisto è di 0,25 Bitcoin.
- Utilizza il tuo nome di account personale REVOLUT per evitare confusione.
- Assicurati di firmare i tuoi account e di stabilire limiti di acquisto per maggiore sicurezza.

Per acquistare Bitcoin su BISQ:

- Accedi alla sezione "Acquista" dove puoi scegliere diversi mercati. (Screenshot della sezione "Acquista")
- Per beneficiare di commissioni ridotte, ti consigliamo di acquistare BSQ, che puoi acquistare con Bitcoin.
- Puoi scegliere tra diverse offerte in base al prezzo, alla quantità, al metodo di pagamento, ecc.
- Per acquistare BSQ, deposita prima Bitcoin nel tuo portafoglio.
- Scegli un'offerta con un basso premio e una bassa quantità per l'acquisto di BSQ.
- BISQ verifica la validità dell'offerta e la connessione del peer.
- Se il venditore non è connesso, scegline un altro.
- Verifica l'offerta e accetta un premio del 5%.
- Conferma le commissioni e lo scambio di BSQ, quindi attendi la conferma della transazione per acquistare Bitcoin con BSQ.

Per vendere Bitcoin su BISQ:

- Crea una nuova offerta nella scheda "Vendi". (Screenshot della scheda "Vendi")
- Puoi scegliere di fissare il numero di Bitcoin da vendere o l'importo in euro che desideri ricevere.
- Puoi impostare un premio in percentuale sopra il prezzo di mercato.
- Puoi creare un intervallo di vendita o lasciare la scelta all'acquirente.
- Puoi anche impostare un prezzo per fermare l'offerta.
- Scegli l'importo minimo del deposito e le commissioni di transazione.
- Finanzia l'ordine depositando i Bitcoin da vendere, l'importo del deposito cauzionale e le commissioni.
- Una volta creata l'offerta, attendi che un acquirente si presenti.

Una volta che l'acquirente ha effettuato il deposito della transazione su BISQ, i Bitcoin vengono automaticamente inviati all'acquirente e tu ricevi i soldi. L'account viene verificato e firmato dopo una transazione con un account firmato.

## LNP2PBOT

![Tutorial LNp2pbot](https://tube.nuagelibre.fr/videos/watch/57ed232d-6149-4267-be38-92b0f32800f7)

[Telegram](https://telegram.org/) è una piattaforma di messaggistica che, con l'aiuto del bot [Lnp2pbot](https://lnp2pbot.com/), ti consente di acquistare e vendere Bitcoin in modo rapido e facile. Ecco come fare:

Per acquistare Bitcoin tramite il Bot LNP2PBOT su Telegram, segui i seguenti passaggi:

- Iniziate accedendo all'account Twitter del bot Lnp2pbot e cliccate sul link presente nella bio. (Screenshot dell'account Twitter del bot e del link nella bio)
- In Telegram, utilizzate i comandi "/buy" o "/sell" per pubblicare ordini di acquisto o vendita. (Screenshot dell'utilizzo dei comandi "/buy" o "/sell")
- Accedete al canale P2P Lightning per trovare offerte di acquisto e vendita in base ai vostri criteri. (Screenshot del canale P2P Lightning)
- Create un'offerta di acquisto utilizzando il bot Lnp2pbot e il comando "/buy".
- Selezionate la valuta di vostra scelta, indicate l'importo, il prezzo (con un premio se desiderato) e scegliete il vostro metodo di pagamento.
- Attendete che un potenziale venditore vi contatti.

Per vendere Bitcoin tramite Revolut, ecco cosa dovete fare:

- Cliccate su 'vendre Satoshi' per aprire una notifica su LNP2PBot. (Screenshot dell'opzione 'vendre Satoshi')
- Ricevete una fattura Lightning da pagare per vendere i Satoshis. (Screenshot della fattura Lightning)
- Attendete che l'acquirente invii una fattura con i satoshi per ricevere i pagamenti.
- Stabilite un contatto diretto con l'acquirente tramite Telegram per concordare il metodo di pagamento e scambiare le informazioni necessarie.
- Confermate la transazione con una nota.

Se desiderate acquistare Bitcoin inviando una fattura LN, seguite questi passaggi:

- Copiate la fattura e inviatela al bot per acquistare i Satoshi.
- Mettetevi in contatto con il venditore per finalizzare l'acquisto dei Bitcoin.
- In caso di problemi, proponete di aspettare o di tentare una cancellazione.
- Annullate l'offerta e cercatene una nuova se necessario.
- Scegliete un'offerta che accetti CPA istantanei per l'acquisto di Satoshi.
- Inviatela fattura e attendete la conferma di pagamento del venditore.
- Una volta effettuato il pagamento, inviate la conferma al bot.
- Attendete la conferma di ricezione degli euro e l'invio dei satoshi da parte del venditore.

Utilizzando questi metodi, potete acquistare e vendere Bitcoin su Telegram in modo sicuro.

## Peach Bitcoin

sito: https://peachbitcoin.com/

Esamineremo in dettaglio questa soluzione in BTC 205 offerto da @pivi\_, ecco i video tutorial:

[Peach](https://peachbitcoin.com/) è un'applicazione mobile svizzera che consente di acquistare e vendere Bitcoin peer-to-peer. Questa soluzione facile da usare offre un'interfaccia intuitiva, ideale per le transazioni in criptovalute.

L'interfaccia dell'applicazione Peach è composta da quattro schede: acquista, vendi, cronologia e impostazioni. (Screenshot dell'interfaccia dell'applicazione)
L'acquisto di bitcoin su Peach è semplificato. Per iniziare, è necessario creare un'offerta. Ciò è possibile accedendo alla scheda "acquista". (Screenshot della scheda "acquista") Successivamente, scorri le offerte disponibili fino a trovare quella che fa per te. I metodi di pagamento accettati sono vari, tra cui il bonifico bancario, l'online wallet, la gift card e l'opzione locale. (Screenshot dei metodi di pagamento disponibili)
Una volta scelta un'offerta, è possibile chattare con il venditore tramite la chat integrata nell'applicazione. (Screenshot della chat dell'applicazione)
Dopo il pagamento, confermato dal venditore, la transazione è completa. I bitcoin vengono quindi inviati all'acquirente, che riceve una notifica confermando la ricezione dei fondi. (Screenshot della notifica di ricezione dei bitcoin)

Peach è un'applicazione non custodiale, il che significa che i bitcoin rimangono in tuo possesso durante tutto il processo. Tuttavia, eventuali controversie sono gestite in modo centralizzato. Pertanto, è fondamentale salvare le informazioni relative alla transazione e le tue informazioni personali utilizzando la funzionalità Backup. (Screenshot della funzionalità Backup)
Poiché Peach è ancora in versione beta, potrebbero verificarsi alcuni bug. Si consiglia di verificare tutte le informazioni prima di concludere una transazione.
In sintesi, l'applicazione mobile Peach offre una soluzione accessibile per acquistare e vendere bitcoin peer-to-peer. L'utilizzo sicuro e ottimale di Peach è la chiave per il successo delle tue transazioni.

## Hold Hodl

[HodlHodl](https://hodlhodl.com/) è un mercato decentralizzato di Bitcoin che dà la priorità al controllo e alla sicurezza degli utenti. A differenza delle borse tradizionali, funziona secondo un modello peer-to-peer, consentendo scambi diretti tra gli utenti. Grazie al suo sistema di escrow multi-firma, Hodl Hodl garantisce la sicurezza dei fondi durante le transazioni. La piattaforma supporta anche diversi metodi di pagamento e offre opzioni di trading come i contratti per differenza (CFD).

In questo tutorial, ti spieghiamo come acquistare e vendere bitcoin peer-to-peer sulla piattaforma HodlHodl.

Prima di iniziare a utilizzare la piattaforma HodlHodl, sono necessari alcuni passaggi di preparazione:

- Apri il sito web di HodlHodl.
- Crea un account utilizzando un indirizzo email per tenere traccia delle tue transazioni.
- Leggi attentamente la guida alla sicurezza prima di iniziare a fare trading.
- Nota che la piattaforma non è open source e conserva alcune delle tue informazioni personali.

Ecco il processo da seguire per effettuare un acquisto sulla piattaforma HodlHodl:

- Utilizza la funzione di filtro per trovare le offerte che ti interessano.
- Clicca sull'offerta che ti interessa.
- Compilare i campi necessari per accettare il contratto.- Nell'esempio, abbiamo utilizzato Revolut come metodo di pagamento.

La configurazione del contratto multisig per la transazione avviene come segue su HodlHodl:

- Una volta accettata l'offerta, effettuare il pagamento tramite il metodo scelto (Revolut nel nostro caso).
- Creare un contratto multisig generando una password.
- Attendere il deposito dei bitcoin all'indirizzo multisig.
- Scegliere il numero di conferme per il contratto.
- Effettuare il pagamento dell'importo concordato al venditore e confermarlo su HodlHodl.
- Essere pazienti poiché la durata del deposito può essere lunga, a seconda della banca utilizzata.
- Attendere la conferma del venditore prima di rilasciare i bitcoin dopo l'acquisto.

La creazione di un'offerta di acquisto o vendita di bitcoin su HodlHodl avviene come segue:

- Sul sito HodlHodl, indicare l'indirizzo di rilascio per le offerte di acquisto.
- Inserire l'importo, il prezzo e il metodo di pagamento.
- È anche possibile aggiungere opzioni facoltative come limiti di transazione o un titolo per l'offerta.
- Una volta creata l'offerta, è possibile visualizzarla, modificarla, duplicarla o eliminarla a piacimento.

## Bonus: Side Shift.AI

Ecco un breve tutorial sull'utilizzo di [SideShift AI](https://sideshift.ai/), uno strumento molto utile per convertire shitcoin in bitcoin. È lo strumento ideale per coloro che hanno chiuso tutti i loro exchange personali. Non è necessario alcun sistema di ordine e sono disponibili liquidità. Tuttavia, si prega di notare che ci sono commissioni del 2,5% per transazione.

Se hai acquistato criptovalute in modo KYC, è consigliabile utilizzare Monero per convertire queste criptovalute in bitcoin. Monero offre una maggiore privacy rispetto a Bitcoin. Per una maggiore sicurezza, è anche consigliata l'operazione di CoinJoin. CoinJoin mescola le tue transazioni con quelle di altri utenti per complicare la tracciabilità delle tue transazioni.

Vorrei anche presentarti uno strumento open source per l'acquisto e la vendita di bitcoin. Questo strumento ti consente di scegliere tra molte blockchain. Basta inserire il tuo indirizzo Bitcoin e selezionare la quantità che desideri inviare. Non è necessario creare un account o collegare il tuo portafoglio allo strumento. Puoi utilizzare un tasso fisso per inviare o ricevere una quantità specifica. Inoltre, questo strumento consente anche la vendita di bitcoin in cambio di USDC.

### Sostienici

Questo corso, insieme a tutto il contenuto presente su questa università, ti è stato offerto gratuitamente dalla nostra comunità. Per supportarci, puoi condividerlo con chi ti sta intorno, diventare membro dell'università e persino contribuire al suo sviluppo tramite GitHub. A nome di tutto il team, grazie!

### Nota sulla formazione

Un sistema di valutazione per la formazione sarà presto integrato in questa nuova piattaforma di E-learning! Nel frattempo, grazie mille per aver seguito il corso e se ti è piaciuto, pensa di condividerlo con chi ti sta intorno.

# Per andare oltre

## Intervista a Steph di Peach Bitcoin

Ecco un riassunto dell'intervista:

Peach Bitcoin è un'applicazione mobile non custodiale che consente l'acquisto e la vendita di Bitcoin peer-to-peer. Attualmente, il team di Peach Bitcoin, con sede in Svizzera, è composto da otto membri e sta lavorando per far evolvere l'applicazione in modo che funga anche da portafoglio. Il modello unico di Peach Bitcoin si basa su una struttura aziendale centralizzata, pur mantenendo un libro degli ordini decentralizzato. Inoltre, l'applicazione offre un'opzione per le transazioni in contanti durante gli incontri di persona.

Uno dei principali vantaggi di Peach Bitcoin è il livello di sicurezza che offre agli utenti. Il sistema deskrow con multisignature e time lock è progettato per gestire i conflitti e garantire la sicurezza delle transazioni. Inoltre, Peach Bitcoin ha accesso prioritario ai fondi della multisignature, il che le consente di trasferire i bitcoin all'acquirente in caso di comportamento fraudolento da parte del venditore. L'azienda ha in programma di integrare tutte le valute europee e altri metodi di pagamento al momento del lancio in open beta a gennaio.

L'idea di Peach Bitcoin è nata dall'esperienza personale della sua fondatrice nell'industria del Bitcoin. Dopo aver scoperto Bitcoin nel 2017 e aver partecipato a diversi meetup e conferenze, è diventata una massimalista di Bitcoin e ha visto l'opportunità di creare una piattaforma che consentisse ai Bitcoiners di incontrarsi e fare transazioni in contanti. Inoltre, l'applicazione include una chat crittografata per comunicare con altri utenti, preservando così l'anonimato degli utenti.

Attualmente, Peach Bitcoin sta sviluppando diverse funzionalità per facilitare il lavoro dei venditori, tra cui la creazione di un'API per i venditori, una piattaforma per i grandi venditori e l'integrazione di BTC Pay Server per automatizzare i trasferimenti. L'applicazione sarà lanciata in open beta a gennaio 2023.

In conclusione, la fondatrice di Peach Bitcoin sottolinea l'importanza della concorrenza nell'ecosistema Bitcoin, poiché ciò che è buono per Bitcoin è benefico per tutti. Inoltre, incoraggia la diversità e l'inclusione nell'industria del Bitcoin e oltre.

## Intervista a Pierre

Ecco un riassunto dell'intervista: Questa intervista conclude la formazione Bitcoin 205 che tratta delle soluzioni di acquisto peer-to-peer di Bitcoin. Organizzata da Pierre, questa formazione ha lo scopo di educare il pubblico francofono sulle soluzioni tecniche di acquisto peer-to-peer di Bitcoin, un campo fino ad ora trascurato. Grazie ai progressi compiuti, è ora possibile acquistare e utilizzare Bitcoin preservando la propria privacy, anche con un semplice telefono e l'applicazione Telegram.

Uno dei metodi evidenziati è l'uso di CoinJoin con Samouraï per rafforzare la sicurezza. Questa soluzione consente di minimizzare i rischi legati alle entità centralizzate che detengono informazioni personali sugli utenti di Bitcoin. Si consiglia di acquistare Bitcoin in non-kyc, un metodo che consente di rafforzare l'anonimato. Inoltre, alcune piattaforme di scambio come Kraken offrono commissioni di prelievo più basse rispetto ad altre, il che va nella direzione dei principi di Bitcoin.

Bisq, Robosat e Peach sono presentati come soluzioni democratiche per il commercio di Bitcoin. In particolare, Peach è evidenziato per la sua facilità di accesso come applicazione mobile. Tuttavia, ci sono sfide da affrontare, tra cui la regolamentazione delle criptovalute e la necessità di rispettare determinati limiti per evitare una regolamentazione eccessiva.

Viene anche affrontato l'uso dei distributori automatici di Bitcoin ATM, che rappresentano un metodo economico per ottenere Bitcoin non-KYC. A seconda della regolamentazione locale, questi distributori possono essere installati a casa o in luoghi pubblici e possono essere utilizzati per offrire Bitcoin ai propri cari o per i pagamenti nei bar.

La formazione sottolinea l'importanza del ruolo dell'educazione nella comprensione di Bitcoin. Si suggerisce che Bitcoin può offrire una soluzione in caso di recessione o iperinflazione ed è importante sensibilizzare le persone al suo potenziale prima che sia troppo tardi. Inoltre, si sottolinea che la separazione dello Stato e della moneta è tanto essenziale quanto la separazione dello Stato e della religione.

In conclusione, Bitcoin è presentato come una valuta decentralizzata che richiede un'educazione pubblica e una mente aperta per essere pienamente compresa e utilizzata. La formazione mira ad aiutare i partecipanti a comprendere le varie soluzioni di acquisto peer-to-peer e a utilizzare questi strumenti per rafforzare la loro anonimato e sicurezza durante l'utilizzo di Bitcoin.

## Articolo bonus sulla privacy

Un super [articolo](https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/) di Loïc Morel sul KYC e l'identificazione.
Questo articolo approfondisce gli sfide e le soluzioni per preservare la privacy durante l'acquisizione e l'uso di bitcoin. Loïc smonta alcune idee preconcette sull'identificazione KYC (Know Your Customer), dettaglia i rischi associati a questo processo e offre tecniche per mantenere l'anonimato delle transazioni. È una lettura imprescindibile per coloro che cercano di comprendere le sfumature della privacy nel mondo del Bitcoin e imparare come utilizzare strumenti come CoinJoin, Stonewall e PayJoin per offuscare il tracciamento delle transazioni e proteggere così la loro privacy.

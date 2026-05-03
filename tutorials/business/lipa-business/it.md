---
name: Lipa for Business
description: Soluzioni di pagamento Bitcoin e Lightning per gli esercenti
---

![cover](assets/cover.webp)

Gli esercenti sono ora sempre più interessati ad accettare pagamenti Bitcoin tramite Lightning Network. A differenza dei pagamenti tradizionali con carta di credito, che comportano commissioni elevate e lunghi tempi di regolamento, le transazioni Lightning sono praticamente istantanee, non sono soggette a chargeback e preservano la riservatezza del cliente.

Affinché un'azienda possa adottare facilmente Bitcoin, la soluzione di pagamento deve rimanere semplice con una intuitiva interfaccia del registratore di cassa, offrire funzioni multi-utente e, idealmente, offrire la conversione automatica in valuta locale per mitigare la volatilità.

**Lipa for Business** è la risposta perfetta a queste esigenze. Si tratta di una soluzione svizzera sviluppata da Lightning Payment Services AG, progettata per consentire agli esercenti di accettare pagamenti Bitcoin Lightning in modo semplice ed efficiente, rimanendo al tempo stesso non vincolati.

*Nota: le schermate utilizzate in questo tutorial sono tratte dal sito ufficiale di Lipa for Business (lipa.swiss/it/for-business) e sono utilizzate a scopo didattico*


## Presentazione di Lipa per le aziende

Lipa for Business è un'applicazione mobile che funziona come un registratore di cassa Bitcoin e Lightning. Offre un'interfaccia semplificata per raccogliere i pagamenti in sats e integra funzioni professionali: accesso ai dipendenti, esportazioni contabili, dashboard web, il tutto senza mai entrare in possesso dei tuoi fondi.

### Caratteristiche principali

**Pagamenti istantanei Lightning**: le invoice Bitcoin Lightning vengono generate in pochi secondi, garantendo transazioni praticamente istantanee senza intermediari bancari. Le commissioni sono basse e trasparenti rispetto alle soluzioni tradizionali.

**Interfaccia POS intuitiva**: l'applicazione fornisce un'interfaccia del POS chiara, progettata per un facile utilizzo in negozio. Inserendo l'importo in valuta locale, l'app visualizza immediatamente l'importo in BTC e un codice QR per il pagamento. Compatibile con tutti i wallet Lightning presenti sul mercato.

**Gestione di più dipendenti**: tutti i dipendenti possono utilizzare l'applicazione per incassare, senza avere accesso ai fondi. Il proprietario mantiene il pieno controllo, mentre la sincronizzazione nel cloud assicura che nessuna transazione vada persa. Ogni dipendente riceve un accesso separato tramite invito con codice QR.

**Conversione automatica in CHF**: per i commercianti svizzeri, Lipa offre la conversione istantanea delle vendite in franchi svizzeri sul conto bancario. Questa opzione è facoltativa: è possibile mantenere i pagamenti in bitcoin (gratuitamente) o convertirli in CHF/EUR con una commissione dello 0,98%.

**Web Dashboard**: pannello di amministrazione dell'interfaccia accessibile tramite dashboard.lipa.swiss, che consente di visualizzare tutte le transazioni, filtrare per periodo o dipendente ed esportare i dati contabili in formato CSV. La dashboard può essere utilizzata anche per emettere invoice web generate con codici QR direttamente dall'interfaccia.


## Creare un account

⚠️ **Importante**: l'installazione dell'applicazione richiede la residenza in Svizzera. Questa restrizione geografica si applica per motivi di conformità normativa.

Per utilizzare Lipa for Business, occorre innanzitutto creare un conto commerciale dedicato:
- Vai su lipa.swiss/for-business e scarica l'applicazione per la tua piattaforma (Android o iOS).
- Installa "lipa Wallet for business" da Google Play o dall'App Store.
- Al primo avvio, inserisci i dati dell'azienda: nome dell'azienda, e-mail di contatto, telefono e indirizzo.
- L'e-mail è l'identificativo principale per accedere alla web dashboard.

Una volta inviato il modulo, Lipa crea il tuo spazio commerciale. Prima dell'attivazione definitiva può essere effettuato un breve controllo manuale (processo KYC semplificato). L'attivazione avviene solitamente entro 24 ore, ma i tempi possono variare.

**Importante**: non è necessario un collegamento al conto bancario per iniziare a incassare dei bitcoin. Le coordinate bancarie sono necessarie solo se si sceglie la conversione automatica in CHF.


## Installazione e interfaccia

**Applicazione mobile**: disponibile per smartphone e tablet Android/iOS. L'interfaccia è stata progettata per essere utilizzato nel punto vendita, con elementi di facile lettura e interazioni limitate allo stretto necessario. Un pulsante "Incassa un pagamento" consente di accedere alla schermata di inserimento dell'importo.

**Requisiti tecnici**: è necessaria una connessione Internet stabile (minimo 3G) per elaborare i pagamenti Lightning in tempo reale.

**Cruscotto web**: cruscotto gratuito accessibile tramite dashboard.lipa.swiss. Connessione e-mail sicura (link magico senza password). Interfaccia mostra tutte le transazioni con tutti i dettagli: data, importo BTC/fiat, tasso Exchange, dipendente, ecc. Esportazione CSV per l'integrazione contabile.

![Dashboard Lipa Business](assets/fr/02.webp)

Il cruscotto può essere utilizzato anche per emettere invoice web generate con codici QR direttamente dall'interfaccia:

![Génération factures web](assets/fr/03.webp)

**Multi-terminale**: supporto nativo per più terminali all'interno di un'azienda. Aggiungi nuovi dispositivi creando dipendenti tramite invito con codice QR. Ogni terminale è collegato allo stesso wallet dell'esercente, mantenendo la tracciabilità per cassiere.


## Accettare un pagamento

Il processo di raccolta è simile a quello di una transazione convenzionale:

![Processus de paiement Lipa](assets/fr/01.webp)

- **Inserire l'importo**: nella schermata di pagamento, inserire l'importo in valuta locale (CHF o EUR). Esempio: per un caffè a 4,50 CHF, inserire 4,50.
- **Generazione dell'invoice**: l'applicazione converte istantaneamente l'importo in satoshi al tasso corrente e genera un invoice Lightning sotto forma di codice QR
- **Pagamento del cliente**: il cliente scansiona il codice QR con il suo Wallet Lightning e convalida il pagamento.
- **Conferma**: il pagamento viene confermato in pochi secondi, con visualizzazione del successo.


## Strumenti professionali

**Cronologia e statistiche**: ogni pagamento viene registrato con tutti i dettagli. La dashboard offre una panoramica con filtri per periodo o dipendente, paragonabile a un classico sistema di cassa.

**Esportazioni contabili**: esportazione dei dati in formato CSV/Excel con tutte le informazioni necessarie (tasso Exchange, transaction ID) per l'integrazione nel software di contabilità.

**Gestione dei dipendenti**: aggiunta/rimozione di utenti autorizzati tramite dashboard. Ogni dipendente riceve un accesso separato con tracciabilità delle transazioni. Possibilità di revoca in qualsiasi momento.

**Backup**: conto commerciale non custodial con recovery phrase di 24 parole da conservare. Solo il proprietario del Wallet principale deve gestire questo backup, i dipendenti non possono accedervi.


## Conversione automatica in CHF

**Disponibilità**: servizio disponibile per gli esercenti svizzeri con pagamento in CHF (EUR soggetto a disponibilità).

**Configurazione**: scelta tra ricezione in bitcoin (gratuita) o conversione in fiat tramite partner finanziario. In caso di conversione in CHF, inserire un IBAN per i trasferimenti.

**Commissioni**: 0,98% commissione sugli importi convertiti (rispetto allo 0% per i pagamenti in BTC). Nessun'altra commissione nascosta o abbonamento.

**Come funziona**: l'importo ricevuto viene immediatamente venduto al tasso di mercato e trasferito sul tuo conto bancario. Il trasferimento avviene secondo le scadenze bancarie standard della tua banca.

**Flessibilità**: opzione reversibile in qualsiasi momento nei parametri. Permette di testare in modalità "conversione fiat", per poi passare al 100% BTC una volta che ci si sente a proprio agio.


## Sicurezza e riservatezza

**Non custodial**: l'utente mantiene il controllo permanente sui fondi ricevuti. Durante la configurazione viene generata una coppia di chiavi private/pubbliche (da qui la frase di 24 parole). Lipa non memorizza le chiavi private.

**Sicurezza dei dipendenti**: i dipendenti possono solo creare invoice, non spendere fondi. In caso di problemi al terminale, i fondi restano al sicuro e l'utente può revocare l'accesso.

**Riservatezza del cliente**: pagamenti fulminei pseudonimi senza dati personali allegati. In contrasto con i pagamenti con carta che passano attraverso reti centralizzate.

**Autenticazione**: dashboard accessibile tramite e-mail con link magico. Applicazione mobile protetta da PIN o biometria.

## Casi d'uso consigliati

- **Ristorazione**: bar, ristoranti, caffè accettano aggiunte in bitcoin con gestione delle mance.
- **Commercio al dettaglio**: negozi di alimentari, panetterie per l'espansione dei metodi di pagamento senza spese fisse.
- **Venditori itineranti**: food truck, mercati, festival con il solo smartphone.
- **Eventi** : stand temporanei con soluzioni pronte all'uso.
- **Servizi**: consulenti, artigiani per la fatturazione una tantum in bitcoin.


## Vantaggi e limiti

### Vantaggi

- Interfaccia semplice, senza necessità di competenze tecniche.
- Soluzione non custodial con controllo totale dei fondi.
- Gestione di più dipendenti con tracciabilità.
- Esportazione contabile e dashboard web inclusi.
- Opzione di conversione automatica in CHF per i rivenditori svizzeri.
- Commissioni trasparenti: 0% Bitcoin, 0,98% conversione fiat.
- Posizionamento come azienda innovativa nell'ecosistema Bitcoin.
- Protezione contro l'inflazione e la svalutazione monetaria.
- Sistema di pagamento decentralizzato e resistente alla censura.

### Limiti

- Solo supporto per Lightning Network (no Bitcoin On-Chain).
- La conversione Fiat è attualmente limitata alla Svizzera.
- I clienti devono disporre di un Wallet Lightning compatibile.
- I codici QR statici non sono attualmente disponibili.
- Per tutte le transazioni è necessaria una connessione a Internet.


## Conclusione

Lipa for Business si propone come soluzione completa per l'accettazione dei bitcoin in negozio. Non sono necessarie infrastrutture costose (basta un semplice smartphone), i costi sono bassi e fissi e l'integrazione nei processi esistenti è semplice.

La sua natura non custodial e rispettosa della privacy, unita a strumenti di gestione professionali, lo rende una scelta interessante per gli esercenti che desiderano adottare Bitcoin mantenendo semplicità e sicurezza.


## Risorse

- [Sito ufficiale di Lipa for Business](https://lipa.swiss/en/for-business)
- [Cruscotto web](https://dashboard.lipa.swiss)
- [Sostegno alle imprese Lipa](https://help.lipa.swiss/business)
- [Supporto generale Lipa](https://help.lipa.swiss/Wallet)
- [LinkedIn Lipa](https://www.linkedin.com/company/getlipa)
- [Twitter @lipa_btc](https://twitter.com/lipa_btc)

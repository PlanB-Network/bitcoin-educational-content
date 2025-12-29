---
name: LN Markets
description: Piattaforma di trading Bitcoin su Lightning Network
---

![cover](assets/cover.webp)



LN Markets è la prima piattaforma di trading Bitcoin veramente Lightning-nativa, che consente di negoziare derivati Bitcoin con leva finanziaria direttamente dal proprio wallet Lightning, senza KYC, regolamenti istantanei e custodia minima. Lanciata nel 2020, elimina gli attriti delle borse tradizionali: nessuna verifica dell'identità, nessun deposito bloccato, nessuna attesa per le conferme della blockchain. Il vostro wallet Lightning diventa il vostro conto di trading.



## Che cos'è il LN Markets?



LN Markets offre **Futures** (contratti perpetui con leva fino a 100×) e **Options** (Call/Put con rischio limitato al premio pagato). La piattaforma funziona come un livello di aggregazione della liquidità che consolida più sedi di negoziazione per un'esecuzione ottimale a zero slittamento. I vostri fondi sono bloccati solo per l'esatta durata delle vostre posizioni attive, non per giorni o settimane come in un conto deposito tradizionale.



### Prodotti di trading disponibili



**Futures (Contratti perpetui)**



I contratti perpetui sono futures senza data di scadenza, che consentono di speculare sull'andamento del prezzo del Bitcoin con una leva finanziaria. Il LN Markets offre due modalità di gestione del margine:



**Modalità isolata**: Ogni posizione ha un proprio margine dedicato. Solo i fondi assegnati a questa specifica posizione sono a rischio. Se la posizione raggiunge il prezzo di liquidazione, **solo questa posizione viene liquidata**, mentre le altre posizioni e il saldo rimanente non vengono toccati. Ideale per limitare rigorosamente il rischio per ogni operazione.



**Modalità incrociata (Cross Margin)** : Il margine è condiviso tra tutte le posizioni aperte. Il saldo totale del conto funge da garanzia per tutte le posizioni. Se una posizione va male, il sistema attinge all'intero saldo disponibile per evitare la liquidazione. **Rischio**: se il saldo totale si esaurisce, tutte le posizioni possono essere liquidate contemporaneamente. Consigliato solo a trader esperti che desiderano massimizzare l'efficienza del capitale.



**Gestione della posizione** :





- Posizione lunga**: si scommette sul rialzo di BTC/USD. Se il prezzo sale, si vince; se scende, si perde. **Esempio**: Bitcoin a $100.000, aprite un Long con 10.000 sats e leva 10×. Se il Bitcoin sale a 105.000 dollari (+5%), la vostra posizione guadagna il 50% (5% × 10), ossia ~5.000 sats di profitto. Se il Bitcoin scende a 95.000 dollari (-5%), perdete il 50%, ossia una perdita di ~5.000 sats.





- Posizione corta**: si scommette sul calo di BTC/USD. Se il prezzo scende, si vince; se sale, si perde. **Esempio**: Bitcoin a $100.000, aprite una posizione corta con 10.000 sats e leva 10×. Se il Bitcoin scende a 95.000 dollari (-5%), vincete il 50%, ossia ~5.000 sats. Se il Bitcoin sale a 105.000 dollari (+5%), perdete il 50%.



La leva finanziaria (fino a 100×) amplifica proporzionalmente i guadagni e le perdite. Un meccanismo di **funding rate** (addebiti periodici ogni 8 ore) bilancia le posizioni lunghe e corte. È possibile gestire fino a 100 posizioni sui futures contemporaneamente.



**Opzioni**



Un'opzione è come un **biglietto della lotteria con data di scadenza**. Si paga un premio per scommettere sulla direzione del prezzo del Bitcoin. **Il vantaggio principale è che non si può mai perdere più del premio pagato, non è possibile alcuna liquidazione.





- Opzione Call (scommessa rialzista)**: Scommettete che il Bitcoin salirà al di sopra dello strike prima della scadenza. Si vince se il prezzo sale, la perdita è limitata al premio se il prezzo scende.





- Opzione Put (scommessa ribassista)**: Scommettete che il Bitcoin scenderà al di sotto dello strike. Si vince se il prezzo scende, la perdita è limitata al premio se il prezzo sale.





- Straddle (scommessa sulla volatilità)**: Si acquista contemporaneamente una Call e una Put. Si vince se il Bitcoin fa un grande movimento in qualsiasi direzione, si perdono entrambi i premi se il prezzo rimane stabile.



Limite: 50 posizioni simultanee. Ideale per iniziare a fare trading con leva finanziaria senza temere la liquidazione.



**sats ↔ sUSD**: Convertire istantaneamente i satoshi in dollari sintetici (sUSD) per proteggersi dalla volatilità, o viceversa per recuperare l'esposizione al Bitcoin.



## Accesso alla piattaforma e creazione di un account



### Vai a LN Markets



Andate su [lnmarkets.com](https://lnmarkets.com) e cliccate su "Open App".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Crea il tuo account



La schermata di benvenuto offre diversi metodi di connessione:



![Méthodes de connexion](assets/fr/02.webp)



**Opzioni disponibili** :


1. **Registrarsi con un Lightning wallet** (consigliato) : LNURL-auth con Phoenix, Breez, Zeus o BlueWallet


2. **Registrarsi con l'email**: account classico (limita l'esperienza Lightning)


3. **Alby** o **Ledger**: estensioni del browser



### Connessione tramite Lightning (LNURL-auth)



Fare clic su "Registrazione con un Lightning wallet". Scansionare il codice QR con il proprio Lightning wallet:



![QR code LNURL-auth](assets/fr/03.webp)



Il vostro wallet firma automaticamente una richiesta crittografica e il vostro account viene creato istantaneamente, senza e-mail o password. Forte sicurezza e totale anonimato.



### Configurazione iniziale



![Configuration post-connexion](assets/fr/04.webp)



**Parametri disponibili** :




- Nome utente**: personalizzare il proprio nome utente
- Prelievi automatici**: attivare i prelievi automatici sul proprio wallet dopo la chiusura dell'operazione
- Autenticazione a due fattori**: maggiore sicurezza con 2FA
- Documentazione**: accesso alle risorse ufficiali



## Tour Interface



L'interfaccia del LN Markets è organizzata in diverse sezioni accessibili dal menu laterale:



### Cruscotto



![Dashboard](assets/fr/06.webp)



Visualizza la vostra performance per tipo di prodotto (Futures Cross, Futures Isolati, Opzioni) con P&L, volumi scambiati e il vostro Address Lightning personale (ad es. `pivi@lnmarkets.com`).



### Profilo



![Profil trader](assets/fr/07.webp)



Statistiche dettagliate: numero di operazioni, tipo di trader (SCALPER, ecc.), durata mediana della posizione, ripartizione Long/Short, tasso di vincita, medie (quantità, margine, leva) e struttura progressiva delle commissioni in base al volume.



### Commercio



![Historique des trades](assets/fr/08.webp)



La scheda Operazioni visualizza una cronologia completa delle posizioni, con tutte le metriche più importanti: data di creazione, direzione (Long/Short), dimensione della posizione (quantità), margine impegnato, prezzo di entrata e di uscita, profitto/perdita realizzato (P&L) e commissioni di trading. È possibile filtrare per tipo di prodotto (futures/opzioni) ed esportare i dati per analisi esterne o per la contabilità.



### Impostazioni



![Paramètres de la plateforme](assets/fr/05.webp)



La scheda Impostazioni offre due schede: **Account** e **Interface**.



*scheda *Account**:



Gestione dei conti con campi modificabili :




- Nome utente**: modificare il nome utente (ad esempio "pivi") con il pulsante "Aggiorna"
- Email**: aggiungere/modificare il proprio indirizzo email
- Indirizzo bitcoin di deposito**: l'indirizzo bitcoin che si può utilizzare per depositare i fondi on-chain.



**Tre opzioni di configurazione** :




- Apparire nelle classifiche**: scegliere se apparire o meno nelle classifiche pubbliche
- Utilizzare indirizzi Taproot**: utilizzare indirizzi Bitcoin Taproot per depositi/prelievi on-chain
- Abilita i prelievi automatici**: attiva i prelievi automatici sul tuo wallet Lightning dopo la chiusura dell'operazione



**Migrazione dell'account**: Sezione che consente di migrare l'account Lightning alla classica autenticazione e-mail/password.



**Gestione Session**: pulsante "Cancella sessione e dati locali" per disconnettere e pulire i dati locali del browser.



*scheda *Interface**:



Personalizzate l'esperienza dell'utente con sette levette:




- Salta la conferma dell'ordine**: disattiva la modalità di conferma prima dell'esecuzione dell'operazione (trading veloce)
- Mostra i tooltip**: visualizza i tooltip quando si passa il mouse su un elemento
- Modalità privata (maschera i dati sensibili)**: maschera gli importi e i dati sensibili nell'interfaccia (modalità privacy)
- Mostra PL nel profilo**: mostra il profitto/la perdita netta nel profilo pubblico
- Usa le icone delle unità**: visualizza le icone delle unità monetarie (sats, $)
- Abilita le notifiche sonore**: attiva le notifiche sonore per gli eventi di trading
- Abilita le notifiche sul desktop**: attiva le notifiche sul desktop del sistema operativo



### Wallet



![Wallet](assets/fr/09.webp)



Saldi Bitcoin e USD sintetici con storico di depositi, prelievi, trasferimenti incrociati, swap, finanziamenti e gestione degli indirizzi on chain.



### API



![API V3](assets/fr/10.webp)



LN Markets offre un API REST completo (V2 e V3) per automatizzare completamente il trading tramite script o bot. È possibile creare chiavi API con autorizzazioni personalizzabili (sola lettura, trading, prelievi) direttamente dall'interfaccia. Per una facile integrazione sono disponibili gli SDK ufficiali TypeScript e Python. La documentazione completa del API V3 è disponibile all'indirizzo [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).



## Primo deposito di fondi



Cliccate su "Deposito". Sono disponibili tre metodi:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: scansionare il codice QR con il wallet Lightning


2. **Invoice**: inserire un importo e scansionare la fattura Lightning


3. **On-Chain**: deposito Bitcoin on chain



## Il trading in pratica



### Trade Futures Long: puntare sul rialzo



Dal cruscotto, cliccate su "Futures" e poi su "Isolati". Cliccare su **"Acquista "** per aprire una posizione lunga.



![Interface Futures Long](assets/fr/12.webp)



Fare clic sull'icona **calcolatore** accanto al pulsante "Acquista" per visualizzare il calcolatore di posizione:



![Calculateur de position Long](assets/fr/13.webp)



**Esempio concreto** :




- Quantità**: $100 (dimensione della posizione)
- Margine commerciale**: 12.336 sats (margine impegnato)
- Leva**: 7.73× (ogni variazione dell'1% di BTC = 7,73% sul vostro capitale)
- Prezzo di ingresso** : $104,863.5
- Liquidazione**: 92.852 dollari (prezzo critico di liquidazione automatica)
- Prezzo di uscita**: $110.000 (per il calcolo del profitto)
- PL** : 4.492 sats (profitto in caso di uscita a 110.000 dollari)



**Scenari** :




- Aumento +4,9%** (110.000 dollari) : +4.492 sats di profitto (+36,4%)
- Neutrale** ($104.863) : -185 sats (solo tasse)
- -11,5%** (92.852 dollari): liquidazione totale (-100%)



Fare clic sul pulsante "Acquista" per confermare l'operazione. **Due casi possibili** :





- Se la liquidità** sul conto è sufficiente, viene visualizzata direttamente una maschera di conferma (immagine sotto). Cliccate su "Sì" per eseguire immediatamente l'operazione.



![Confirmation trade Long](assets/fr/14.webp)





- Se non avete abbastanza contanti**: viene visualizzato un codice QR Lightning. Scansionatelo con il vostro wallet Lightning per pagare il margine richiesto. L'operazione si apre automaticamente al ricevimento del pagamento



### Trade Futures Short: scommettere sul ribasso



Cliccare su **"Sell "** per aprire una posizione corta (si vince se il prezzo scende). Aprire la calcolatrice con l'icona della calcolatrice per impostare la posizione:



![Calculateur de position Short](assets/fr/15.webp)



Cliccare su "Vendi" per confermare. Per quanto riguarda il Long, **due casi possibili**:





- Se si dispone di denaro sufficiente**: modalità di conferma diretta, fare clic su "Sì"
- Se non si dispone di contanti sufficienti**: viene visualizzato un codice QR Lightning (immagine sotto). Scansionatelo con il vostro wallet Lightning per pagare il margine richiesto:



![Paiement Lightning pour Short](assets/fr/16.webp)



Una volta ricevuto il pagamento Lightning, la posizione Short si apre automaticamente. È quindi possibile gestirla dall'interfaccia di trading.



#### Chiusura di una posizione



Per chiudere la posizione (Long o Short), cliccare sulla **croce piccola nell'angolo in basso a destra** dell'interfaccia di gestione:



![Interface de clôture](assets/fr/17.webp)



Viene visualizzata una finestra di dialogo di conferma per confermare la chiusura dell'operazione:



![Confirmation clôture](assets/fr/18.webp)



La finestra di dialogo visualizza il conto economico corrente (profitto o perdita). Fare clic su "Sì" per chiudere. Il saldo viene immediatamente aggiunto (profitto) o detratto (perdita) dal Wallet tramite Lightning.



### Trading Opzioni Call: diritto condizionato all'acquisto



Le opzioni offrono un **rischio limitato** al premio pagato, senza possibilità di liquidazione. Una Call dà il diritto (non l'obbligo) di acquistare il Bitcoin al prezzo di esercizio prima della scadenza. A differenza dei futures, non potrete mai perdere più del premio investito.



Dalla Dashboard, fare clic su "Opzioni", quindi selezionare la scheda "Chiamata".



![Interface Options Call](assets/fr/19.webp)



Configurare l'operazione con i seguenti parametri:




- Quantità**: $100 (dimensione del contratto)
- Scadenza** : 2025-11-15 (data di scadenza)
- Sciopero**: 96.000 dollari (prezzo obiettivo)



Gli altri campi vengono calcolati automaticamente:




- Margine**: 1.045 sats (premio da pagare, il vostro investimento)
- Breakeven**: $96.923 (prezzo per recuperare la propria quota)
- Delta**: 40 (sensibilità al prezzo del Bitcoin)



**Come calcolare la vincita?



Il vostro profitto dipende dal prezzo del Bitcoin alla scadenza. Formula: **(prezzo BTC - Strike) × dimensione Contract - Premio pagato**.



**Esempi concreti** :





- Bitcoin a $96.000** (prezzo attuale) : Valore intrinseco = $0. **Perdita: -1,045 sats** (si perde il premio)





- Bitcoin a 97.000 dollari**: Valore intrinseco = (97.000 - 96.000) × 0,00105 BTC = 1,05 dollari. Convertito in sats ≈ 2,175 sats. **Profitto: 2,175 - 1,045 = +1,130 sats** (+108% di guadagno)





- Bitcoin a 98.000 dollari**: valore intrinseco = 2.000 dollari ≈ 3.224 sats. **Profitto: +2.179 sats** (+208% di guadagno)





- Bitcoin a 100.000 dollari**: valore intrinseco = 4.000 dollari ≈ 5.263 sats. **Profitto: +4.218 sats** (+403% di guadagno)





- Bitcoin sotto i 96.000 dollari**: L'opzione scade senza valore. **Perdita limitata: -1.045 sats**, nessuna liquidazione possibile



Cliccare su "Acquista Call". Viene visualizzata una finestra di dialogo di conferma:



![Confirmation Call option](assets/fr/20.webp)



Cliccare nuovamente su "Acquista Call" per confermare. L'opzione appare in "Running Options". Alla scadenza, LN Markets calcola automaticamente il valore intrinseco e adegua il profitto/perdita.



**Nota sulle opzioni Put** : Il funzionamento è identico a quello di una call, ma al contrario. Con una Put, si scommette sul fatto che il prezzo del Bitcoin scenda **in basso**. Se il Bitcoin scende al di sotto del vostro strike, vincete; se rimane al di sopra, perdete solo il premio pagato. Il calcolo dei guadagni segue la stessa logica: **(Strike - prezzo BTC) × dimensione Contract - premio pagato**.



### Ritiro fulmineo del fondo



Fare clic su "Ritiro":



![Modal de retrait](assets/fr/21.webp)



**Metodi** : LNURL, Invoice, Lightning Address, On-Chain.



**Procedura Invoice** :


1. Generazione di una fattura Lightning dal wallet


2. Copiare la fattura (inizia con `lnbc...`)


3. Incollarlo nel campo LN Markets


4. Confermare il ritiro


5. Il wallet viene accreditato in 1-3 secondi



Nessuna commissione di prelievo Lightning, solo costi di routing minimi (<0,1% in pratica).



## Rischi e buone pratiche



**Rischi principali** :




- Liquidazione totale**: un'elevata leva finanziaria può cancellare il 100% del margine in pochi minuti
- Servizio sperimentale**: fase alfa, incertezze tecnologiche
- Rischio di controparte**: la piattaforma rimane una controparte unica



**Best practices** :



1. **Gestione del capitale**: adottare una strategia di gestione del rischio adatta al proprio profilo. Ad esempio: destinare il 5% del proprio patrimonio totale al trading con leva finanziaria, quindi rischiare al massimo l'1% di questo capitale per ogni operazione (ad esempio: 1 asset BTC → 5M sats da negoziare → 50k sats rischio massimo per posizione)



2. **Stop-loss sistematico**: configurate gli stop-loss per limitare le perdite per ogni operazione. Con una regola di rischio dell'1%, ad esempio, anche 10 operazioni consecutive perdenti rappresentano solo il 10% del vostro capitale di trading



3. **Iniziare in piccolo**: fare prima un test con qualche migliaio di satss per capire i meccanismi prima di applicare la strategia di gestione del capitale



4. **Ritiro regolare dei profitti**: assicurate i vostri profitti sul vostro wallet principale, lasciando sulla piattaforma solo il capitale di trading attivo



5. **Attenzione alla leva finanziaria**: evitate una leva finanziaria >20× a meno che non siate pienamente consapevoli dei rischi di liquidazione



**Costi**: nessuna commissione di deposito/prelievo Lightning, spread ~0,1% per operazione (che scende allo 0,06% in base al volume).



## Vantaggi e limiti



**Vantaggi** :




- Non custodiale (controllo totale esclusi i periodi di negoziazione)
- Senza KYC (anonimato tramite Lightning/Nostr)
- Pagamenti istantanei (depositi/prelievi in pochi secondi)
- Esecuzione a zero slittamento con aggregazione della liquidità
- Supporto pubblico API e Nostr



**Limitazioni** :




- Servizio alfa (possibili evoluzioni)
- Liquidità inferiore a Binance/Deribit
- Vietato ai residenti negli Stati Uniti



## Conclusione



LN Markets rappresenta un'importante evoluzione del trading Bitcoin, integrando in modo nativo Lightning Network per restituire il controllo agli utenti. Per gli esperti di bitcoiners che desiderano speculare senza compromettere la propria sovranità, si tratta di un'alternativa unica alle tradizionali borse centralizzate.



La piattaforma continua ad evolversi con i futures lineari USDT e il trading non custodiale tramite i Discreet Log Contracts (DLC) in fase di sviluppo. Applicando buone pratiche di gestione del rischio (piccoli importi, stop-loss, prelievi regolari), LN Markets diventa un potente strumento per esplorare la leva finanziaria Bitcoin in modo responsabile.



Iniziate in piccolo, testate con qualche migliaio di satss ed esplorate gradualmente questa nuova frontiera del Lightning Network . Buon trading sovrano ⚡️!



## Risorse





- [Sito ufficiale del LN Markets](https://lnmarkets.com)
- [Documentazione](https://docs.lnmarkets.com)
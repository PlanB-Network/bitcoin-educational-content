---
name: SwapMarket
description: Aggregatore di servizi di swap Bitcoin e Lightning
---

![cover](assets/cover.webp)



Il trasferimento di fondi tra Bitcoin on-chain e Lightning Network richiede generalmente l'apertura manuale di canali Lightning (tecnica e costosa), oppure l'uso di piattaforme di swap centralizzate con KYC. SwapMarket offre un'alternativa: swap atomici senza fiducia tramite fornitori competitivi, senza KYC.



Innovazione: sebbene i provider siano degli intermediari, i HTLC (*Contratti Time Locked Hash*) garantiscono matematicamente che i vostri fondi rimangano sotto il vostro controllo. L'aggregazione di diversi fornitori (Boltz, ZEUS Swaps, Eldamar, Middle Way) crea una concorrenza sui prezzi. Interface web open-source auto-ostabile.



## Che cos'è SwapMarket?



Aggregatore open-source lanciato nel 2024, SwapMarket funziona come un comparatore di fornitori di swap Bitcoin/Lightning. L'utente confronta immediatamente le condizioni (commissioni, liquidità, limiti) e seleziona il fornitore ottimale.



### Architettura tecnica



**Frontend lato client**: applicazione 100% lato client (fork Boltz Web App) ospitata su GitHub Pages. Il codice viene eseguito nel browser senza server backend. Cronologia memorizzata localmente (cookie/cache). Codice sorgente pubblico e verificabile.



**Rilevamento dei provider** : Elenco hardcoded in `src/configs/mainnet.ts`. Aggiunta di nuovi fornitori tramite richiesta di pull o email.



**Backend indipendenti**: Ogni fornitore gestisce il proprio backend Boltz. L'interfaccia interroga le API in tempo reale per confrontare istantaneamente le quotazioni.



**HTLC Swap atomici**: I contratti Hash Time Locked garantiscono l'atomicità: o lo swap viene eseguito, o ciascuna parte recupera i propri fondi. Il rischio di controparte è matematicamente eliminato.



### Filosofia



SwapMarket riduce la centralizzazione creando una concorrenza tra i fornitori per le commissioni e la liquidità. Nessun KYC, codice open-source auto-ostabile, moltiplicazione degli operatori indipendenti per evitare singoli punti di fallimento.



## Caratteristiche principali



### Mercato dei fornitori



L'interfaccia visualizza tutti i provider attivi: nome del provider, commissioni applicate (percentuali e/o fisse), importi minimi/massimi disponibili e tipi di swap supportati. L'applicazione interroga direttamente le API di ciascun provider indicato nel file di configurazione per recuperare le quotazioni in tempo reale. La concorrenza tra i provider garantisce tassi ottimali, generalmente intorno allo 0,5% per gli swap standard.



### Scambi bidirezionali



**Swap-in (on-chain → Lightning)**: Converte i BTC on-chain in satoshi Lightning. Caso d'uso: alimentare un wallet Lightning mobile, ottenere capacità in entrata su un nodo o avere liquidità istantanea.



**Swap-out (Lightning → on-chain)**: Converte i satoshi Lightning in BTC on-chain. Caso d'uso: svuotare un Lightning wallet in un deposito freddo o riequilibrare la liquidità tra i livelli.



### Sicurezza e recupero



**Trustless scambi atomici**: Le HTLC garantiscono che lo scambio sia completato per intero o che ciascuna parte recuperi la propria quota. Il rischio di controparte è matematicamente eliminato.



**Meccanismo di pagamento**: Ogni swap ha un blocco temporale. Se lo swap fallisce, i fondi sono automaticamente rimborsabili dopo la scadenza. L'utente conserva sempre la possibilità di recuperare i suoi bitcoin.



**Chiavi di recupero**: SwapMarket consente di esportare chiavi di recupero per gli swap in corso. In caso di problemi, queste chiavi possono essere utilizzate per finalizzare o annullare uno scambio da qualsiasi dispositivo.



## Installazione e accesso



### Interface web



SwapMarket non richiede alcuna installazione. L'accesso avviene tramite browser visitando https://swapmarket.github.io. Per la massima riservatezza, utilizzare Brave, Firefox con estensioni anti-tracciamento o LibreWolf. Tor Browser è consigliato per l'anonimato in rete.



Non è richiesta alcuna registrazione, e-mail o verifica dell'identità.



### Self-hosting (opzionale)



Per gli utenti tecnici che desiderano eliminare qualsiasi dipendenza dal dominio ufficiale di GitHub Pages, SwapMarket può essere eseguito localmente:



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Via Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



L'applicazione sarà accessibile all'indirizzo `http://localhost:3000`. Il self-hosting garantisce il controllo totale dell'interfaccia, elimina il rischio di censura del dominio ufficiale e consente di verificare il codice sorgente prima dell'esecuzione.



### Configurazione iniziale



**Wallet Lightning**: Assicurarsi di avere un wallet Lightning operativo (Phoenix, Zeus, BlueWallet, ecc.). Per gli swap-in, si riceverà una fattura generate Lightning. Per gli swap-out, si pagherà una fattura Lightning.



**Wallet on-chain**: Per gli swap-in, è necessario un wallet Bitcoin on-chain per inviare fondi. Per gli swap-out, preparare un indirizzo Bitcoin per la ricezione.



**Configurazione opzionale**: SwapMarket memorizza la cronologia degli scambi e le preferenze nei cookie del browser. Non è richiesta la creazione di un account.



## Accesso alle impostazioni e alla chiave di soccorso



Prima di effettuare i primi scambi, si consiglia vivamente di scaricare la **Rescue Key**. Questa chiave di emergenza consente di recuperare i fondi in caso di problemi tecnici o di perdita di accesso al dispositivo.



### Parametri di accesso



Dalla pagina principale di SwapMarket, cliccate sull'icona dell'ingranaggio (⚙️) in alto a destra dell'interfaccia, accanto al modulo di scambio.



![Accès aux paramètres](assets/fr/01.webp)



### Impostazioni della pagina



Si apre la pagina Impostazioni, che mostra diverse opzioni di configurazione:





- Denominazione**: A scelta tra BTC o sats
- Separatore decimale**: Separatore decimale (, o .)
- Notifiche audio e del browser**: Notifiche audio e del browser
- Chiave di ripristino** : Scarica la chiave di ripristino
- Registri**: Visualizzare, scaricare o eliminare i registri



![Page Settings](assets/fr/02.webp)



### Scaricare Rescue Key



Fare clic sul pulsante **Download** accanto a "Rescue Key".



**Punti importanti** :




- La Rescue Key è una **chiave d'emergenza unica** che funziona per tutti i vostri scambi futuri
- Conservate questa chiave in un luogo **sicuro e permanente** (gestore di password, cassaforte digitale)
- In caso di problemi di swap (timeout, guasto tecnico), questa chiave consente di recuperare i fondi



## Creare uno swap passo dopo passo



### Scambio: Fulmine → Bitcoin



Questo primo esempio mostra come convertire i satoshis Lightning in bitcoin on-chain.



**Fase 1: scambiare la configurazione



Dalla pagina principale, selezionare il modulo di scambio :




- LIGHTNING** (campo superiore): Inserire l'importo che si desidera inviare in sats Lightning (esempio: 30.000 sats)
- BITCOIN** (campo inferiore): L'importo che riceverete viene visualizzato automaticamente dopo la detrazione delle spese (esempio: 29.320 sats)



Nel campo inferiore, incollate il vostro **indirizzo di ricezione Bitcoin** dove desiderate ricevere i fondi. Controllare attentamente questo indirizzo.



Il fornitore predefinito è solitamente Boltz Exchange. Le tariffe di rete e le tariffe del fornitore sono chiaramente indicate.



![Configuration swap-out](assets/fr/03.webp)



**Fase 2: selezione del fornitore**



Fare clic sul menu a discesa del fornitore (predefinito: "Boltz Exchange") per visualizzare tutti i fornitori di liquidità disponibili.



Si apre una finestra modale che visualizza una tabella di confronto:




- Stato**: Indicatore Green se il fornitore è attivo
- Alias**: Nome del fornitore (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Tassa**: Spese applicate dal fornitore (generalmente tra lo 0,49% e lo 0,5%)
- Max Swap**: Importo massimo accettato per uno swap



Confrontate le tariffe e gli importi massimi, quindi selezionate il fornitore di vostra scelta.



**Nota bene**: L'interfaccia di selezione del fornitore non visualizza gli **importi minimi** per ciascun fornitore. Queste informazioni vengono visualizzate solo nell'interfaccia di creazione degli swap, dopo la selezione del fornitore. Gli importi minimi e massimi possono variare da fornitore a fornitore e possono cambiare nel tempo. **Verificate sempre questi limiti al momento dello swap**: se l'importo che desiderate scambiare non rientra nei limiti di un provider, potete selezionarne un altro più adatto alla vostra transazione.



![Sélection du provider](assets/fr/04.webp)



**Fase 3: Creazione dello swap e pagamento Lightning**



Fare clic sul pulsante giallo **"CREA SCAMBIO ATOMICO "**. SwapMarket invierà una **fattura Lightning** (BOLT11) da pagare dal proprio wallet Lightning.



La pagina visualizza :




- ID swap**: Identificatore swap univoco (esempio: J4ymFIMVR6Hm)
- Stato**: "swap.created" (swap creato, in attesa di pagamento)
- Codice QR**: Scannerizzatelo con il vostro wallet Lightning
- Invoice Lightning**: Stringa di caratteri che inizia con "lnbc" (esempio: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Pagare questa fattura dal proprio wallet Lightning (Phoenix, Zeus, BlueWallet, ecc.). Viene visualizzato l'importo esatto da pagare (esempio: 30.000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Fase 4: Conferma e accettazione**



Una volta confermato il pagamento Lightning, SwapMarket riceve istantaneamente il pagamento e il provider trasmette la transazione Bitcoin al vostro indirizzo.



Lo stato cambia in **"invoice.settled "** (fattura pagata) e viene visualizzato un messaggio di conferma.



I bitcoin on-chain saranno disponibili non appena la transazione sarà confermata (di solito da pochi minuti a qualche ora, a seconda delle commissioni mining scelte dal provider).



![Confirmation swap-out](assets/fr/06.webp)



È possibile fare clic su **"OPEN CLAIM TRANSACTION "** per visualizzare la transazione Bitcoin su un browser blockchain.



### Scambio: Bitcoin → Fulmine



Questo secondo esempio mostra come convertire i bitcoin on-chain in satoshi Lightning.



**Fase 1: scambiare la configurazione



Dalla pagina principale, selezionare il modulo di scambio :




- BITCOIN** (campo superiore): Immettere l'importo che si desidera inviare in sats Bitcoin (esempio: 63.400 sats)
- LUCE** (campo inferiore): L'importo che riceverete viene visualizzato automaticamente dopo la detrazione delle spese (esempio: 62 884 sats)



Nel campo inferiore, incollare una fattura Lightning** (BOLT11) generata dal wallet Lightning, oppure utilizzare l'indirizzo LNURL se il wallet lo supporta.



![Configuration swap-in](assets/fr/07.webp)



**Fase 2: Controllo della chiave di salvataggio**



Dopo aver fatto clic su **"CREATE ATOMIC SWAP "**, appare una finestra modale che chiede di verificare la Rescue Key.



![Modal Rescue Key](assets/fr/08.webp)



**Chiave di recupero Boltz**: Poiché la chiave di ripristino è già stata caricata durante la configurazione iniziale (vedere la sezione precedente), fare clic sul pulsante **"VERIFICA CHIAVE ESISTENTE "** per importare la chiave salvata.



Selezionare il file della Rescue Key scaricato in precedenza. Dopo l'esito positivo della verifica, l'interfaccia passa automaticamente alla fase successiva.



**Passo 3: indirizzo di deposito Bitcoin**



SwapMarket genera ora un **indirizzo unico Bitcoin** contenente il contratto HTLC collegato alla fattura Lightning.



La pagina visualizza :




- ID di scambio**: Identificatore univoco (esempio: 1kGmB6JyGqU4)
- Stato**: "invoice.set" (fattura impostata, in attesa di pagamento Bitcoin)
- Codice QR**: Indirizzo del deposito Bitcoin
- Indirizzo Bitcoin**: Di solito inizia con "bc1p..." (esempio: bc1p5mvtwxapjkds...9d4n9f)
- Avviso in giallo** : "Assicurati che la tua transazione venga confermata entro ~24 ore dalla creazione di questo swap!"



Questo periodo di ~24 ore è il **timeout** del contratto HTLC. Se la transazione Bitcoin non viene confermata entro questo lasso di tempo, lo swap fallirà e sarà necessario utilizzare la Rescue Key per recuperare i fondi.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



È possibile copiare l'indirizzo facendo clic sul pulsante **"INDIRIZZO "** oppure scansionare il codice QR direttamente dal wallet on-chain.



**Fase 4: invio di bitcoin**



Dal vostro wallet Bitcoin on-chain, inviate **esattamente** l'importo indicato (ad esempio 63.400 sats) all'indirizzo generato.



**Importante**: Utilizzare le tariffe mining appropriate per garantire una conferma rapida. Se la tariffa è troppo bassa e la transazione rimane nella mempool oltre il timeout (~24h), lo swap fallirà.



Una volta inviata la transazione, SwapMarket rileva che si trova nella mempool e visualizza :




- Stato** : "transaction.mempool
- Messaggio**: "La transazione è in mempool - In attesa di conferma per completare lo scambio"



![Transaction en mempool](assets/fr/10.webp)



**Fase 5: Conferma e ricezione del lampo**



Non appena la transazione Bitcoin riceve la prima conferma, il fornitore paga automaticamente la vostra fattura Lightning. Il cliente riceve immediatamente i satoshi sul suo wallet Lightning.



Lo stato cambia in **"transaction.claim.pending "**, quindi viene visualizzato un messaggio di conferma:



![Confirmation swap-in](assets/fr/11.webp)



I satoshis Lightning sono immediatamente disponibili nel wallet.



## Vantaggi e limiti



### Vantaggi



**Concorrenza tariffaria**: L'aggregazione dei fornitori crea una concorrenza naturale che fa scendere le tariffe (dallo 0,49% allo 0,5%).



**Confidenzialità**: Nessun KYC, interfaccia 100% lato client (nessuna trasmissione di dati personali), compatibile con Tor Browser.



**Non detentivo**: HTLC garantisce matematicamente il controllo esclusivo dei vostri fondi. O lo scambio va a buon fine, o si riavranno i propri bitcoin.



**Open-source self-hostable**: codice pubblico verificabile, distribuibile localmente per la massima resistenza alla censura.



### Limitazioni



**Limitata liquidità**: Numero limitato di fornitori attivi (Boltz, Eldamar, MiddleWay a seconda del periodo). Gli importi massimi possono essere limitati.



**Tempo di scadenza**: Timeout da 24 a 48 ore. Se la transazione on-chain non viene confermata prima della scadenza, è necessario un recupero manuale.



**Centralizzazione Interface**: Sebbene sia auto-ostabile, l'interfaccia ufficiale è ospitata su GitHub Pages. Se GitHub censura il repo, l'accesso tramite swapmarket.github.io sarà bloccato (soluzione: self-hosting).



**Tracce on-chain**: Gli script HTLC sono potenzialmente identificabili dall'analisi avanzata della blockchain.



## Le migliori pratiche



### Configurazione sicura



**Scaricare la chiave di soccorso**: Prima del primo swap, scaricare la chiave di salvataggio dalle Impostazioni (vedere la sezione dedicata sopra). Questa chiave unica funzionerà per tutti gli scambi futuri, consentendo di recuperare i fondi in caso di problemi.



**Utilizzare il browser Tor**: Per la massima riservatezza, accedi a SwapMarket tramite il browser Tor per nascondere il tuo indirizzo IP.



**Considerare il self-hosting**: Per gli utenti tecnici, gestire la propria istanza di SwapMarket elimina la dipendenza dal dominio ufficiale di GitHub Pages.



### Ottimizzazione dello scambio



**Tenere d'occhio la mempool**: Controllare mempool.space prima di uno swap-in. Scegliere orari di bassa attività per ridurre al minimo i costi di mining.



**Controllare gli indirizzi: Per gli scambi, controllare meticolosamente l'indirizzo di ricezione. Utilizzate il copia e incolla e controllate i primi 5 e gli ultimi 5 caratteri.



**Provare con piccole quantità**: Iniziate con il minimo consentito (da 25.000 a 50.000 sats). Aumentare gradualmente una volta acquisita la padronanza del processo.



**Documentare gli swap**: Annotate l'ID di ogni swap, l'indirizzo di riscatto e la data di scadenza. Queste informazioni facilitano la tracciabilità e il recupero in caso di problemi tecnici.



### Strategia d'uso



**Bilanciate il vostro flusso di cassa**: Utilizzate SwapMarket per regolare la vostra allocazione tra on-chain (risparmi, sicurezza a lungo termine) e Lightning (spese quotidiane, pagamenti immediati) in base alle vostre reali esigenze.



**Calcolare la redditività**: Per le esigenze di liquidità permanente di Lightning, confrontate il costo cumulativo di ripetuti swap rispetto all'apertura diretta di un canale Lightning. SwapMarket eccelle per gli aggiustamenti una tantum, non necessariamente per i grandi flussi regolari.



## SwapMarket vs Boltz: Qual è la differenza?



### Boltz: Tecnologia e servizio



**Boltz è la tecnologia open-source** (`boltz-backend` su GitHub) che implementa scambi atomici tramite HTLC tra Bitcoin, Lightning e Liquid.



**Punto critico**: Tutti i fornitori di SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) utilizzano la propria istanza del backend di Boltz. La tecnologia sottostante è quindi identica. Una vulnerabilità nel backend di Boltz potrebbe colpire tutti i provider, ma la natura open-source del sistema consente un controllo da parte della comunità.



**Boltz Exchange** è un singolo servizio gestito dal team Boltz, mentre **SwapMarket** riunisce diversi fornitori che utilizzano tutti la tecnologia Boltz, creando un ambiente di prezzi competitivi.



Per maggiori dettagli, consultate le nostre esercitazioni sullo scambio di Boltz e Zeus:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Differenze chiave



| Aspetto      | Boltz Exchange       | SwapMarket                           |
| ------------ | -------------------- | ------------------------------------ |
| Natura        | Servizio unico       | Aggregatore multi-provider           |
| Fornitori     | Solo Boltz           | Boltz, ZEUS, Eldamar, Middle Way     |
| Concorrenza   | Tariffe fisse        | Concorrenza libera                   |
| Interfaccia   | boltz.exchange       | swapmarket.github.io (auto-ospitabile) |
| Sicurezza     | Non-custodial (HTLC) | Non-custodial (HTLC)                 |

*vantaggi di *SwapMarket**: Concorrenza sui prezzi, diversificazione delle istanze backend, confronto in tempo reale.



**Alternative tecnologiche** (non compatibili con SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Queste soluzioni utilizzano le proprie implementazioni di swap sottomarino.



**Raccomandazione**: Utilizzare Boltz Exchange per semplicità o SwapMarket per ottimizzare i costi attraverso la concorrenza. Entrambi sono equivalenti in termini di sicurezza (HTLC non custodiale).



## Conclusione



SwapMarket facilita gli scambi Bitcoin/Lightning aggregando più fornitori in un'unica interfaccia. L'architettura HTLC garantisce la natura non custodiale degli scambi, l'assenza di KYC preserva la riservatezza e il codice open-source auto-ostabile rafforza la resistenza alla censura.



La concorrenza tra i fornitori migliora i tassi e moltiplica le fonti di liquidità. Per ottimizzare la gestione a due livelli (risparmi on-chain, spese Lightning), SwapMarket è uno strumento pratico che preserva la sovranità finanziaria e la riservatezza.



## Risorse



### Documentazione ufficiale




- [SwapMarket - Applicazione web](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Documentazione tecnica](https://docs.boltz.exchange/)
- [Guida self-hosting](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Progetti correlati




- [Boltz Exchange](https://boltz.exchange) - Servizio di scambio atomico originale
- [ZEUS Swaps](https://zeusln.com) - Fornitore di swap fulminei
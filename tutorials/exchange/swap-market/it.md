---
name: SwapMarket
description: Aggregatore di servizi di swap Bitcoin e Lightning
---

![cover](assets/cover.webp)



Il trasferimento di fondi tra Bitcoin On-Chain e Lightning Network richiede generalmente l'apertura manuale di canali Lightning (tecnica e costosa), oppure l'uso di piattaforme di swap centralizzate con KYC. SwapMarket offre un'alternativa: Swap atomici Trustless tramite fornitori competitivi, senza KYC.



Innovazione: sebbene i provider siano intermediari, HTLC (*Contratti Time Locked Hash*) garantisce matematicamente che i vostri fondi rimangano sotto il vostro controllo. L'aggregazione di diversi fornitori (Boltz, ZEUS Swaps, Eldamar, Middle Way) crea una concorrenza sui prezzi. Interface web open-source auto-ostabile.



## Che cos'è SwapMarket?



Aggregatore open-source lanciato nel 2024, SwapMarket funziona come un comparatore di fornitori di swap Bitcoin/Lightning. L'utente confronta immediatamente le condizioni (commissioni, liquidità, limiti) e seleziona il fornitore ottimale.



### Architettura tecnica



**Frontend lato client**: applicazione 100% lato client (Fork Boltz Web App) ospitata su GitHub Pages. Il codice viene eseguito nel browser senza server backend. Cronologia memorizzata localmente (cookie/cache). Codice sorgente pubblico e verificabile.



**Rilevamento del provider** : Elenco codificato Hard in `src/configs/Mainnet.ts`. Aggiunta di nuovi fornitori tramite richiesta di pull o email.



**Backend indipendenti**: Ogni fornitore gestisce il proprio backend Boltz. Interface interroga le API in tempo reale per confrontare istantaneamente i preventivi.



**HTLC Swap atomici**: I contratti Hash Time Locked garantiscono l'atomicità: o lo swap viene eseguito, o ciascuna parte recupera i propri fondi. Il rischio di controparte è matematicamente eliminato.



### Filosofia



SwapMarket riduce la centralizzazione creando una concorrenza tra i fornitori per le commissioni e la liquidità. Nessun KYC, codice open-source auto-ostabile, moltiplicazione degli operatori indipendenti per evitare singoli punti di fallimento.



## Caratteristiche principali



### Mercato dei fornitori



Interface visualizza tutti i provider attivi: nome del provider, commissioni applicate (percentuali e/o fisse), importi minimi/massimi disponibili e tipi di swap supportati. L'applicazione interroga direttamente le API di ciascun provider indicato nel file di configurazione per recuperare le quotazioni in tempo reale. La concorrenza tra i provider garantisce tassi ottimali, generalmente intorno allo 0,5% per gli swap standard.



### Scambi bidirezionali



**Swap-in (On-Chain → Lightning)**: Converte i BTC On-Chain in satoshi Lightning. Caso d'uso: alimentare un Wallet Lightning mobile, ottenere capacità in entrata su un nodo o avere liquidità istantanea.



**Scambio (Lightning → On-Chain)**: Converte i satoshi Lightning in BTC On-Chain. Caso d'uso: scaricare i Lightning Wallet in depositi Cold o riequilibrare la liquidità tra i livelli.



### Sicurezza e recupero



**Trustless Scambi atomici: Il HTLC garantisce che il Exchange sia completato per intero o che ciascuna parte recuperi la propria quota. Il rischio di controparte è matematicamente eliminato.



**Meccanismo di riscatto**: Ogni swap ha una data di scadenza (TIMELOCK). Se lo swap fallisce, i fondi sono automaticamente rimborsabili dopo la scadenza. L'utente conserva sempre la possibilità di recuperare i suoi bitcoin.



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



L'applicazione sarà accessibile all'indirizzo `http://localhost:3000`. Il self-hosting garantisce un controllo totale su Interface, elimina il rischio di censura del dominio ufficiale e consente di verificare il codice sorgente prima dell'esecuzione.



### Configurazione iniziale



**Wallet Lightning**: Assicurarsi di avere un Wallet Lightning operativo (Phoenix, Zeus, BlueWallet, ecc.). Per gli swap-in, si pagherà un Invoice Lightning. Per gli swap-out, si pagherà un Lightning Invoice.



**Wallet On-Chain**: Per gli swap-in, è necessario un Wallet Bitcoin On-Chain per inviare fondi. Per gli swap-out, preparare un Bitcoin che riceve un Address.



**Configurazione opzionale**: SwapMarket memorizza la cronologia degli scambi e le preferenze nei cookie del browser. Non è richiesta la creazione di un account.



## Accesso alle impostazioni e alla chiave di soccorso



Prima di effettuare i primi scambi, si consiglia vivamente di scaricare la **Rescue Key**. Questa chiave di emergenza consente di recuperare i fondi in caso di problemi tecnici o di perdita di accesso al dispositivo.



### Parametri di accesso



Dalla pagina principale di SwapMarket, fare clic sull'icona dell'ingranaggio (⚙️) in alto a destra della Interface, accanto al modulo di scambio.



![Accès aux paramètres](assets/fr/01.webp)



### Impostazioni della pagina



Si apre la pagina Impostazioni, che mostra diverse opzioni di configurazione:





- Denominazione**: A scelta tra BTC o Sats
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



Questo primo esempio mostra come convertire i satoshi Lightning in bitcoin On-Chain.



**Fase 1: scambiare la configurazione



Dalla pagina principale, selezionare il modulo di scambio :




- LIGHTNING** (campo superiore): Inserire l'importo che si desidera inviare in Sats Lightning (esempio: 30.000 Sats)
- Bitcoin** (campo inferiore): L'importo che riceverete viene visualizzato automaticamente dopo la detrazione delle spese (esempio: Sats 29.320)



Nel campo in basso, incollate il vostro **Bitcoin Address** dove desiderate ricevere i fondi. Controllare attentamente il Address.



Il fornitore predefinito è generalmente Boltz Exchange. Le tariffe di rete e le tariffe del fornitore sono chiaramente indicate.



![Configuration swap-out](assets/fr/03.webp)



**Fase 2: selezione del fornitore**



Fare clic sul menu a discesa del fornitore (predefinito: "Boltz Exchange") per visualizzare tutti i fornitori di liquidità disponibili.



Si apre una finestra modale che visualizza una tabella di confronto:




- Stato**: Indicatore Green se il fornitore è attivo
- Alias**: Nome del fornitore (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Tassa**: Spese applicate dal fornitore (generalmente tra lo 0,49% e lo 0,5%)
- Max Swap**: Importo massimo accettato per uno swap



Confrontate le tariffe e gli importi massimi, quindi selezionate il fornitore di vostra scelta.



**Nota bene**: Il Interface di selezione del fornitore non visualizza gli **importi minimi** per ciascun fornitore. Queste informazioni vengono visualizzate solo nella Interface di creazione dello swap, dopo che è stato selezionato un fornitore. Gli importi minimi e massimi possono variare da fornitore a fornitore e possono cambiare nel tempo. **Controllate sempre questi limiti al momento dello swap**: se l'importo che desiderate scambiare non rientra nei limiti di un provider, potete selezionarne un altro più adatto alla vostra transazione.



![Sélection du provider](assets/fr/04.webp)



**Fase 3: Creazione dello swap e pagamento Lightning**



Fare clic sul pulsante giallo **"CREA SCAMBIO ATOMICO "**. SwapMarket invierà a generate un **Lightning Invoice** (BOLT11) da pagare dal proprio Wallet Lightning.



La pagina visualizza :




- ID swap**: Identificatore swap univoco (esempio: J4ymFIMVR6Hm)
- Stato**: "swap.created" (swap creato, in attesa di pagamento)
- Codice QR**: Scansionatelo con il vostro Wallet Lightning
- Lampo Invoice**: Stringa di caratteri che inizia con "lnbc" (esempio: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Pagare questo Invoice dal proprio Wallet Lightning (Phoenix, Zeus, BlueWallet, ecc.). L'importo esatto da pagare viene visualizzato (esempio: 30.000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Fase 4: Conferma e accettazione**



Una volta confermato il pagamento Lightning, SwapMarket riceve istantaneamente il pagamento e il provider trasmette la transazione Bitcoin sul vostro Address.



Lo stato cambia in **"Invoice.settled "** (Invoice pagato) e viene visualizzato un messaggio di conferma.



I bitcoin On-Chain saranno disponibili non appena la transazione sarà confermata (di solito da pochi minuti a poche ore, a seconda delle tariffe Mining scelte dal provider).



![Confirmation swap-out](assets/fr/06.webp)



È possibile fare clic su **"OPEN CLAIM TRANSACTION "** per visualizzare la transazione Bitcoin su Blockchain explorer.



### Scambio: Bitcoin → Fulmine



Questo secondo esempio mostra come convertire i bitcoin On-Chain in satoshi Lightning.



**Fase 1: scambiare la configurazione



Dalla pagina principale, selezionare il modulo di scambio :




- Bitcoin** (campo superiore): Inserire l'importo che si desidera inviare in Sats Bitcoin (esempio: 63.400 Sats)
- LUCE** (campo inferiore): L'importo che riceverete viene visualizzato automaticamente dopo la deduzione delle spese (esempio: 62 884 Sats)



Nel campo inferiore, incollare un Lightning** Invoice (BOLT11) generato dal Lightning Wallet, oppure utilizzare il LNURL Address se il Wallet lo supporta.



![Configuration swap-in](assets/fr/07.webp)



**Fase 2: Controllo della chiave di salvataggio**



Dopo aver fatto clic su **"CREATE ATOMIC SWAP "**, appare una finestra modale che chiede di verificare la Rescue Key.



![Modal Rescue Key](assets/fr/08.webp)



**Chiave di recupero Boltz**: Poiché la chiave di ripristino è già stata caricata durante la configurazione iniziale (vedere la sezione precedente), fare clic sul pulsante **"VERIFICA CHIAVE ESISTENTE "** per importare la chiave salvata.



Selezionare il file Rescue Key scaricato in precedenza. Dopo la verifica, il Interface passa automaticamente alla fase successiva.



**Fase 3: Bitcoin** deposito Address



SwapMarket ora genera un **unico Bitcoin Address** contenente il HTLC Contract collegato al vostro Lightning Invoice.



La pagina visualizza :




- ID di scambio**: Identificatore univoco (esempio: 1kGmB6JyGqU4)
- Stato** : "Invoice.set" (Invoice impostato, in attesa di pagamento Bitcoin)
- Codice QR**: Deposito Bitcoin Address
- Bitcoin** Address: di solito inizia con "bc1p..." (esempio: bc1p5mvtwxapjkds...9d4n9f)
- Avviso in giallo** : "Assicurati che la tua transazione venga confermata entro ~24 ore dalla creazione di questo swap!"



Questo periodo di ~24 ore è il **timeout** di HTLC Contract. Se la transazione Bitcoin non viene confermata entro questo lasso di tempo, lo scambio fallirà e sarà necessario utilizzare la Rescue Key per recuperare i fondi.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



È possibile copiare il Address facendo clic sul pulsante **"Address"** o scansionare il codice QR direttamente dal proprio Wallet On-Chain.



**Fase 4: invio di bitcoin**



Dal vostro Wallet Bitcoin On-Chain, inviate **esattamente** l'importo indicato (ad esempio, 63.400 Sats) al Address generato.



**Importante**: Utilizzare tariffe Mining adeguate per garantire una conferma rapida. Se la tariffa è troppo bassa e la transazione rimane in Mempool oltre il timeout (~24h), lo scambio fallirà.



Una volta inviata la transazione, SwapMarket rileva che è in Mempool e visualizza :




- Stato** : "transazione.Mempool"
- Messaggio**: "La transazione è in Mempool - In attesa di conferma per completare lo scambio"



![Transaction en mempool](assets/fr/10.webp)



**Fase 5: Conferma e ricezione del lampo**



Non appena la transazione Bitcoin riceve la prima conferma, il fornitore paga automaticamente il vostro Invoice Lightning. Il cliente riceve immediatamente i satoshi sul suo Wallet Lightning.



Lo stato cambia in **"transaction.claim.pending "**, quindi viene visualizzato un messaggio di conferma:



![Confirmation swap-in](assets/fr/11.webp)



I satoshi Lightning sono immediatamente disponibili nel Wallet.



## Vantaggi e limiti



### Vantaggi



**Concorrenza tariffaria**: L'aggregazione dei fornitori crea una concorrenza naturale che fa scendere le tariffe (dallo 0,49% allo 0,5%).



**Confidenzialità**: Nessun KYC, Interface 100% lato client (nessuna trasmissione di dati personali), compatibile con Tor Browser.



**Non detentivo**: HTLC garantisce matematicamente il controllo esclusivo dei vostri fondi. O lo scambio va a buon fine, o si riavranno i propri bitcoin.



**Open-source self-hostable**: codice pubblico verificabile, distribuibile localmente per la massima resistenza alla censura.



### Limitazioni



**Limitata liquidità**: Numero limitato di fornitori attivi (Boltz, Eldamar, MiddleWay a seconda del periodo). Gli importi massimi possono essere limitati.



**Tempo di scadenza**: Timeout da 24 a 48 ore. Se la transazione On-Chain non viene confermata prima della scadenza, è necessario un recupero manuale.



**Centralizzazione del Interface**: Sebbene sia auto-ostabile, il Interface ufficiale è ospitato su GitHub Pages. Se GitHub censura il repo, l'accesso tramite swapmarket.github.io sarà bloccato (soluzione: auto-ospedizione).



**Tracce On-Chain**: Gli script HTLC sono potenzialmente identificabili con l'analisi avanzata di Blockchain.



## Le migliori pratiche



### Configurazione sicura



**Scaricare la chiave di soccorso**: Prima del primo swap, scaricare la chiave di salvataggio dalle Impostazioni (vedere la sezione dedicata sopra). Questa chiave unica funzionerà per tutti gli scambi futuri, consentendo di recuperare i fondi in caso di problemi.



**Utilizzare il browser Tor**: Per la massima riservatezza, accedere a SwapMarket tramite il browser Tor per nascondere il proprio IP Address.



**Considerare il self-hosting**: Per gli utenti tecnici, gestire la propria istanza di SwapMarket elimina la dipendenza dal dominio ufficiale di GitHub Pages.



### Ottimizzazione dello scambio



**Tenere d'occhio Mempool**: Controllare Mempool.space prima di uno swap-in. Scegliere orari di bassa attività per ridurre al minimo i costi di Mining.



**Controllare gli indirizzi**: Per le sostituzioni, controllare meticolosamente il Address ricevuto. Utilizzare il copia e incolla e controllare i primi 5 e gli ultimi 5 caratteri.



**Provare con piccole quantità**: Iniziare con il minimo consentito (da 25.000 a 50.000 Sats). Aumentare gradualmente una volta acquisita la padronanza del processo.



**Documentare gli swap**: Annotate l'ID di ogni swap, il Address di rimborso e la data di scadenza. Queste informazioni facilitano la tracciabilità e il recupero in caso di problemi tecnici.



### Strategia d'uso



**Bilanciate il vostro flusso di cassa**: Utilizzate SwapMarket per regolare la vostra allocazione tra On-Chain (risparmi, sicurezza a lungo termine) e Lightning (spese quotidiane, pagamenti immediati) in base alle vostre reali esigenze.



**Calcolare la redditività**: Per le esigenze di liquidità permanente di Lightning, confrontate il costo cumulativo di ripetuti swap rispetto all'apertura diretta di un canale Lightning. SwapMarket eccelle per gli aggiustamenti una tantum, non necessariamente per i grandi flussi regolari.



## SwapMarket vs Boltz: Qual è la differenza?



### Boltz: Tecnologia e servizio



**Boltz è la tecnologia open-source** (`boltz-backend` su GitHub) che implementa scambi atomici tramite HTLC tra Bitcoin, Lightning e Liquid.



**Punto critico**: Tutti i fornitori di SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) utilizzano la propria istanza del backend di Boltz. La tecnologia sottostante è quindi identica. Una vulnerabilità nel backend di Boltz potrebbe colpire tutti i provider, ma la natura open-source del sistema consente un controllo da parte della comunità.



**Boltz Exchange** è un singolo servizio gestito dal team Boltz, mentre **SwapMarket** riunisce diversi fornitori che utilizzano tutti la tecnologia Boltz, creando un ambiente di prezzi competitivi.



Per maggiori dettagli, consultate le nostre esercitazioni sullo scambio di Boltz e Zeus:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Differenze chiave



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

*vantaggi di *SwapMarket**: Concorrenza sui prezzi, diversificazione delle istanze backend, confronto in tempo reale.



**Alternative tecnologiche** (non compatibili con SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Queste soluzioni utilizzano le proprie implementazioni di swap sottomarino.



**Raccomandazione**: Utilizzare Boltz Exchange per semplicità o SwapMarket per ottimizzare i costi attraverso la concorrenza. Entrambi sono equivalenti in termini di sicurezza (il HTLC non è custodiale).



## Conclusione



SwapMarket facilita gli scambi Bitcoin/Lightning aggregando più provider in un unico Interface. L'architettura HTLC garantisce la natura non custodiale degli swap, l'assenza di KYC preserva la riservatezza e il codice open-source auto-ostabile rafforza la resistenza alla censura.



La concorrenza tra i fornitori migliora i tassi e moltiplica le fonti di liquidità. Per ottimizzare la gestione dei due Layer (risparmi On-Chain, spese Lightning), SwapMarket è uno strumento pratico che preserva la sovranità finanziaria e la riservatezza.



## Risorse



### Documentazione ufficiale




- [SwapMarket - Applicazione web](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Documentazione tecnica](https://docs.boltz.Exchange/)
- [Guida self-hosting](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Progetti correlati




- [Boltz Exchange](https://boltz.Exchange) - Servizio di scambio atomico originale
- [ZEUS Swaps](https://zeusln.com) - Fornitore di Lightning swaps
---
name: ArkadeOS
description: Guida completa al portafoglio Arkade e al Protocollo Ark
---

![cover](assets/cover.webp)



La rete Bitcoin deve affrontare una sfida importante: la scalabilità. Sebbene il livello principale (livello 1) offra sicurezza e decentralizzazione senza pari, può gestire solo un numero limitato di transazioni al secondo. Lightning Network è emerso come una promettente soluzione di secondo livello (livello 2), che consente pagamenti veloci e a basso costo. Tuttavia, Lightning impone i suoi vincoli: la gestione dei canali, la necessità di liquidità in entrata e una complessità tecnica che potrebbe scoraggiare i nuovi utenti.



Questo è il contesto di **Ark**, un nuovo protocollo di livello 2 progettato per offrire un'esperienza utente semplificata senza sacrificare la sovranità. **ArkadeOS** (o Arkade) è la prima grande implementazione di questo protocollo, che offre un portafoglio Bitcoin di nuova generazione.



Questo tutorial vi guiderà nel mondo di Arkade. Esploreremo come funziona il protocollo Ark, come installare e configurare il wallet Arkade e come utilizzarlo per inviare e ricevere bitcoin istantaneamente, in modo riservato e senza i soliti attriti del Lightning Network.



## Comprendere il protocollo Ark



Prima di immergersi nell'uso di Arkade, è essenziale comprendere i concetti chiave del protocollo Ark che lo guida. Ark non è una blockchain separata, ma un meccanismo di coordinamento intelligente in cima a Bitcoin.



### Il concetto VTXO


Il cuore di Ark è il **VTXO** (Virtual UTXO). Un VTXO è un UTXO non ancora pubblicato sulla blockchain Bitcoin: esiste al di fuori della catena principale (off-chain) ma è supportato da transazioni pre-firmate sulla blockchain.



A differenza di un saldo su una borsa centralizzata, un VTXO appartiene davvero a voi. Siete in possesso di una prova crittografica che vi permette, in qualsiasi momento, di rivendicare i bitcoin reali corrispondenti sulla blockchain, anche se il server Ark scompare. I VTXO consentono di trasferire istantaneamente il valore tra gli utenti senza attendere le conferme dei blocchi.



### Il ruolo dell'ASP (Ark Service Provider)


Il protocollo Ark opera su un modello client-server. Il server è chiamato **ASP** (Ark Service Provider). L'ASP svolge il ruolo di conduttore:




- Fornisce la liquidità necessaria alla rete.
- Coordina le transazioni tra gli utenti.
- Organizza "round" di regolamento sulla blockchain.



È fondamentale notare che ASP è **non custode**. Non detiene mai le vostre chiavi private, né può rubare i vostri fondi. Il suo ruolo è puramente tecnico e logistico. Se un ASP censura le vostre transazioni o va in tilt, potete sempre recuperare i vostri fondi attraverso una procedura di uscita unilaterale.



### Giri e privacy


Le transazioni su Ark sono finalizzate in lotti chiamati **Round**. Periodicamente (ad esempio, ogni pochi secondi), l'ASP raccoglie tutte le transazioni in sospeso e le fissa sulla blockchain Bitcoin in un'unica transazione ottimizzata.


Questo meccanismo offre due vantaggi principali:




- Scalabilità**: Una singola transazione on-chain può convalidare migliaia di pagamenti off-chain, riducendo drasticamente i costi per gli utenti.
- Riservatezza**: Ogni round agisce come un **CoinJoin**. I fondi di tutti i partecipanti vengono mescolati in un pool comune prima di essere ridistribuiti sotto forma di nuovi VTXO. In questo modo si interrompe il legame tra mittente e destinatario, rendendo estremamente difficile, se non impossibile, per un osservatore esterno rintracciare i pagamenti.



## Presentazione di ArkadeOS



ArkadeOS è l'applicazione concreta che rende disponibile il protocollo Ark al grande pubblico. Sviluppato da Ark Labs, è un ecosistema completo che comprende un portafoglio (Wallet), un server (Operator) e strumenti per gli sviluppatori.



Per l'utente finale, Arkade assume la forma di una wallet (PWA - Progressive Web App) elegante e intuitiva. Nasconde la complessità crittografica dei VTXO e dei round dietro un'interfaccia familiare. Con Arkade, avete un indirizzo per ricevere, un pulsante per inviare e una cronologia delle transazioni, proprio come un classico wallet, ma con la potenza dell'immediatezza e della riservatezza di Ark.



## Installazione e configurazione



Poiché Arkade è una Progressive Web App, è particolarmente facile da installare e non richiede necessariamente l'utilizzo di application store tradizionali.



### Accesso e installazione


È possibile accedere ad Arkade direttamente da qualsiasi browser web moderno (Chrome, Safari, Brave) su computer o cellulare.





- Visitate il sito web ufficiale dell'applicazione: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Sarete accolti da una serie di schermate introduttive che vi presenteranno i concetti chiave di Arkade: un nuovo ecosistema per il Bitcoin, l'importanza dell'autocustodia e i vantaggi delle transazioni in batch.



![arkade onboarding](assets/fr/02.webp)





- Su Android (Chrome/Brave)** : Premere il menu del browser (tre punti) e selezionare "Installa applicazione" o "Aggiungi alla schermata iniziale".
- Su iOS (Safari)**: Premere il pulsante di condivisione (quadrato con una freccia verso l'alto) e scegliere "Sulla schermata iniziale".



Una volta installato, Arkade si avvia come un'applicazione nativa, a schermo intero e senza barra degli indirizzi.



### Creazione del portafoglio


Al primo avvio, vi verrà chiesto di configurare il vostro portafoglio.





- Fare clic su **"Crea nuovo Wallet"**.



![create wallet](assets/fr/03.webp)





- Il wallet viene creato istantaneamente. A differenza dei portafogli Bitcoin tradizionali, **Arkade non utilizza una frase di recupero di 12 o 24 parole**. Al contrario, Arkade genera automaticamente una **chiave privata** in formato Nostr (nsec), che sarà utilizzata per eseguire il backup e il ripristino del wallet. Ricordarsi di salvare immediatamente questa chiave (vedere la sezione successiva).





- Verrà visualizzata la schermata "Il vostro nuovo wallet è attivo!", che conferma che il wallet è pronto all'uso. Fare clic su **"VAI AL PORTAFOGLIO "** per accedere all'interfaccia principale.



Una volta entrati nel wallet, si accede all'interfaccia principale di Arkade. Qui troverete il vostro saldo, i pulsanti per l'invio e la ricezione di fondi e una scheda "Apps" che dà accesso ad applicazioni integrate come Boltz (scambio di fulmini), LendaSat e LendaSwap (servizi di prestito) e Fuji Money (attività sintetiche).



![wallet interface](assets/fr/04.webp)



### Connessione ad ASP


Per impostazione predefinita, il portfolio è configurato automaticamente per connettersi all'ASP ufficiale di Arkade Labs. È possibile verificare a quale server si è connessi andando su **Impostazioni** > **About**, dove è riportato l'indirizzo del server (attualmente `https://arkade.computer`).



Nella versione attuale di Arkade (Beta), non è possibile modificare manualmente il server ASP. L'applicazione si connette automaticamente all'ASP ufficiale di Arkade Labs. In futuro, gli utenti potranno scegliere tra diversi ASP in base alle loro preferenze, ma questa funzione non è ancora disponibile.



### Backup della chiave privata


**Arkade utilizza una chiave privata in formato Nostr (nsec) come metodo di backup e ripristino. Per eseguire il backup della chiave privata :





- Andare a **Impostazioni** dalla schermata principale.
- Selezionare **"Backup e privacy "**.
- Vedrete la vostra **chiave privata** visualizzata nel formato `nsec...`. Questa lunga stringa di caratteri è l'unico mezzo per ripristinare il proprio wallet.
- Premere **"COPY NSEC TO CLIPBOARD "** per copiare la chiave privata.
- Conservate questa chiave in un luogo sicuro**: scrivetela su carta, memorizzatela in un gestore di password sicuro o utilizzate qualsiasi altro metodo di backup che vi sia congeniale.
- Arkade offre anche l'opzione **"Abilita backup Nostr "**. Questa funzione utilizza il protocollo Nostr (una rete decentralizzata) per eseguire automaticamente il backup di alcuni dati del wallet in forma crittografata sui relè Nostr. Questo facilita la sincronizzazione tra più dispositivi e offre un più semplice recupero dello stato del wallet.



**Importante**: I backup di Nostr sono solo una funzione di **comodità**. Non sostituiscono il backup della chiave nsec. I relè Nostr non garantiscono la conservazione permanente dei dati. La chiave privata nsec rimane l'unico mezzo garantito per recuperare i fondi.



![backup private key](assets/fr/05.webp)




## Utilizzo di Arkade



Una volta configurato il wallet, si è pronti a esplorare le funzionalità di Arkade. L'interfaccia è stata progettata per unificare i diversi tipi di pagamenti del Bitcoin (On-chain, Lightning, Ark) senza soluzione di continuità.



### Ricezione di fondi



Per finanziare il portafoglio, premere **"Ricevi "**. Arkade offre tre metodi di ricezione:





- Pagamento con Ark**: Se il mittente utilizza anche Arkade, condividete il vostro indirizzo Ark per un trasferimento istantaneo, riservato e praticamente gratuito.
- Deposito a catena (Imbarco)**: Utilizzare l'indirizzo Bitcoin (`bc1p...`) per ricevere da un wallet classico o da uno scambio. Attendere la conferma (~10 min) prima che i fondi vengano convertiti in VTXO.
- Scambio Lightning**: Generate una fattura Lightning e pagatela da un wallet Lightning esterno. I fondi arrivano immediatamente tramite uno scambio automatico.



![receive amount](assets/fr/06.webp)



La schermata della ricevuta visualizza tutte le opzioni disponibili: Codice QR, indirizzo Ark, indirizzo Bitcoin (BIP21) e fattura Lightning. Per i pagamenti Lightning, mantenere l'applicazione aperta durante la transazione.



![receive confirmation](assets/fr/07.webp)



### Invio di fondi



Per inviare fondi, premere **"Invia "** e incollare l'indirizzo del destinatario o scansionare il codice QR. Arkade rileva automaticamente il tipo di pagamento richiesto:





- Pagamento Ark**: A un indirizzo Ark, il trasferimento è istantaneo, privato e praticamente gratuito (0 commissioni SATS). Non è necessario che il destinatario sia online.
- Pagamento Lightning**: Scansionate una fattura Lightning (`lnbc...`) e Arkade esegue automaticamente uno scambio. L'ASP paga la fattura per voi e addebita il vostro saldo Arkade.
- Pagamento in catena**: Verso un indirizzo classico del Bitcoin (`bc1q...` o `bc1p...`), Arkade avvia un "Output collaborativo" che sarà incluso nel prossimo round del on-chain.



Controllare i dettagli nella schermata "Firma transazione", quindi confermare con **"TAP TO SIGN "**.



![send payment](assets/fr/08.webp)



**Limitazione attuale (Beta)**: I VTXO creati da meno di 24 ore non possono essere utilizzati per le uscite on-chain. Se si verifica un errore, attendere che i VTXO siano "maturi".



**Confidenzialità dell'output on-chain**: L'esempio seguente mostra una [transazione di output Ark su mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Osserviamo un ingresso distribuito a 4 uscite diverse, come in un CoinJoin. Per un osservatore esterno è impossibile determinare quale quantità appartiene a quale utente.



![transaction ark mempool](assets/fr/11.webp)



## Caratteristiche avanzate



### Gestione delle scadenze VTXO


Una caratteristica tecnica del protocollo Ark è che i VTXO hanno una **vita limitata**. Questo vincolo temporale è insito nella progettazione del protocollo. Il tempo di scadenza è configurabile da ogni server ASP; sull'ASP ufficiale di Arkade Labs, questo periodo è di circa **4 settimane (≈30 giorni)**.



**Questa limitazione consente al server Ark di gestire in modo efficiente la liquidità e di ripulire i VTXO degli utenti inattivi. Dopo la scadenza, il server Ark può tecnicamente rivendicare i fondi rimanenti nell'albero VTXO.



**Per mantenere attivi i VTXO, è necessario "rinfrescarli" prima della loro scadenza. Il refresh consiste nel partecipare a un nuovo "round" in cui i VTXO prossimi alla scadenza vengono scambiati con nuovi VTXO con un nuovo periodo di validità completa (≈30 giorni su Arkade Labs ASP).



Il portafoglio Arkade gestisce questo processo in modo automatico: l'applicazione monitora costantemente lo stato dei vostri VTXO e li aggiorna automaticamente qualche giorno prima della loro scadenza. Se aprite regolarmente l'applicazione (almeno una volta alla settimana), i vostri VTXO saranno automaticamente mantenuti attivi.



**Se non si apre il portafoglio per più di 4 settimane, i VTXO scadono. Tuttavia, non perdete i vostri fondi: avete la possibilità di recuperarli attraverso una **uscita unilaterale** (vedi sezione successiva). Questa procedura è più costosa e più lenta, ma garantisce la possibilità di recuperare i fondi.



La necessità di aprire regolarmente l'applicazione rende Arkade un **"Hot Wallet"** progettato per la spesa quotidiana, non una cassaforte per i risparmi a lungo termine. Per conservare i bitcoin senza utilizzarli per lunghi periodi, preferire un hardware freddo wallet.



**Controllare lo stato dei VTXO**: È possibile monitorare lo stato dei VTXO in **Impostazioni** > **Avanzate**. Vedere "Prossimo rinnovo" per vedere quando avverrà il prossimo rinnovo automatico e "Monete virtuali" per vedere un elenco dettagliato di tutti i VTXO con la relativa data di scadenza.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (Uscita Unilaterale)



L'uscita unilaterale è una **garanzia crittografica fondamentale** del protocollo Ark che vi assicura di riavere i vostri fondi, anche se l'ASP scompare, censura le vostre transazioni o si rifiuta di collaborare. Tecnicamente, i vostri VTXO sono **transazioni Bitcoin pre-firmate** di vostra proprietà. In caso di emergenza assoluta, potete trasmettere queste transazioni sulla blockchain Bitcoin per recuperare i vostri fondi senza l'autorizzazione di nessuno.



**Come funziona? Il processo si svolge in due fasi. In primo luogo, lo **Sgombero**: si trasmettono in sequenza le transazioni pre-firmate che compongono i VTXO nell'albero delle transazioni. Poi la **Finalizzazione**: una volta scaduti i timelock (di solito 24 ore), si raccolgono i bitcoin da un indirizzo standard.



**Stato attuale di Arkade**: Nella versione Beta, non esiste ancora un pulsante o una semplice interfaccia utente per l'output unilaterale. Questa funzionalità richiede attualmente l'uso dell'SDK Arkade e conoscenze tecniche di programmazione TypeScript.



**Anche se la procedura non è accessibile premendo un pulsante, la garanzia crittografica è presente. I vostri VTXO contengono transazioni pre-firmate che vi appartengono legittimamente. È questa garanzia tecnica che rende Arca un protocollo **non custodiale**: anche nel peggiore dei casi, i vostri fondi restano tecnicamente recuperabili. Nelle versioni future di Arkade verrà probabilmente aggiunta un'interfaccia semplificata.



## Vantaggi e limiti



Per collocare Arkade nel giusto contesto, riassumiamo i suoi attuali punti di forza e di debolezza.



### Punti salienti




- Esperienza utente (UX)**: Nessuna gestione dei canali, capacità in entrata o backup complessi dei canali come con Lightning. Basta installare e utilizzare.
- Privacy** : L'architettura predefinita CoinJoin offre un livello di anonimato molto più elevato rispetto alle transazioni standard on-chain o Lightning.
- Interoperabilità**: Pagate qualsiasi codice QR Bitcoin (On-chain o Lightning) da un'unica interfaccia.



### Vincoli




- Protocollo giovani**: Ark è una tecnologia molto recente. Possono esistere bug. Si consiglia di non utilizzare Ark per memorizzare somme la cui perdita sarebbe critica.
- Dipendenza da ASP**: Sebbene non sia vincolante, il sistema si basa sulla disponibilità dell'ASP per garantire la fluidità. Se l'ASP è offline, non è più possibile effettuare transazioni istantanee (solo l'uscita dei fondi on-chain).
- Solo Hot Wallet** : La necessità di aprire regolarmente l'applicazione per aggiornare i VTXO non è adatta alla conservazione a freddo (conservazione Cold).



## Confronto: Arkade vs Lightning vs Cashu



Per capire meglio il posizionamento di Arkade, confrontiamolo con le altre due principali soluzioni di scalabilità.




| Criterio | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modello** | UTXO condiviso coordinato da server (ASP) | Rete P2P di canali di pagamento | Token ciechi emessi da una banca (Mint) |
| **Custodia** | **Non-custodial** (hai le chiavi) | **Non-custodial** (hai le chiavi) | **Custodial** (il Mint ha i fondi) |
| **Privacy** | **Elevata** (CoinJoin nativo, cieco per il pubblico) | **Media** (Onion routing, ma canali visibili) | **Molto Elevata** (Cieco anche per il Mint) |
| **Scalabilità** | Eccellente (Batching massivo on-chain) | Eccellente (Transazioni infinite off-chain) | Eccellente (Semplici firme del server) |
| **Esperienza** | Semplice (simile a un wallet on-chain) | Complessa (gestione canali, liquidità) | Molto semplice (come contante digitale) |
| **Rischio principale** | Disponibilità dell'ASP ed espirazione | Gestione dei canali e backup | Fiducia nel Mint (rischio di furto) |

**Arkade** è il compromesso ideale: la semplicità e la riservatezza di Cashu, ma con la sovranità (non detentiva) di Lightning.



## Supporto e assistenza



In caso di problemi o domande durante l'utilizzo di Arkade, l'applicazione offre diverse opzioni di supporto:





- Andare a **Impostazioni** > **Assistenza**.
- Troverete diverse opzioni:
  - Assistenza clienti**: Chiedete aiuto per il vostro portafoglio, segnalate bug o ponete domande.
  - Chat sicura**: Le conversazioni sono sicure e private e la cronologia viene mantenuta tra le sessioni.
  - Segnalazioni di bug**: Segnalate qualsiasi problema riscontrato, compresi i passaggi per riprodurlo.
  - Monitoraggio dei progressi**: Tenete sempre sotto controllo i vostri ticket di assistenza e le conversazioni.



![support](assets/fr/10.webp)



Il team di Arkade è attivo anche su Telegram tramite il canale @arkade_os per il supporto e le opportunità di integrazione.



## Nota importante: l'applicazione è in versione beta



**⚠️ Arkade è attualmente in Beta pubblica sul mainnet Bitcoin**. Sebbene l'applicazione funzioni con bitcoin reali, è importante prendere alcune precauzioni.



### Raccomandazioni per l'uso




- Utilizzare piccole quantità**: Evitate di conservare grandi somme su Arkade. Utilizzate questo wallet per le spese quotidiane e conservate i vostri risparmi su un hardware wallet freddo.
- Possibili bug e limitazioni**: Come ogni applicazione in fase di sviluppo attivo, Arkade può presentare bug o comportamenti inaspettati. Segnalare eventuali problemi tramite il supporto integrato.
- Rapida evoluzione** : L'applicazione e il protocollo vengono costantemente migliorati. Alcune caratteristiche potrebbero cambiare o essere aggiunte nelle versioni future.



### Limitazioni attuali conosciute




- ritardo di 24 ore sui VTXO** : I VTXO appena creati non possono essere utilizzati immediatamente per le uscite on-chain.
- ASP unico**: Non è ancora possibile cambiare il server ASP nell'applicazione.
- Uscita unilaterale tecnica**: Non esiste ancora un'interfaccia semplificata per l'uscita unilaterale (richiede l'SDK).



Il team di Arkade Labs sta lavorando attivamente per ridurre queste limitazioni nelle versioni future.



## Conclusione



ArkadeOS rappresenta una svolta importante nell'ecosistema Bitcoin. Implementando il protocollo Ark, dimostra che è possibile conciliare la semplicità d'uso con i principi fondamentali del Bitcoin: non fidarsi, verificare.



Sebbene sia ancora agli inizi, Arkade offre un affascinante scorcio di quello che potrebbe essere il futuro dei pagamenti Bitcoin: istantaneo, privato e accessibile a tutti senza prerequisiti tecnici. È lo strumento perfetto per le vostre spese quotidiane, a complemento della vostra soluzione di risparmio sicuro (Cold Wallet).



Vi invitiamo a testare Arkade con piccole quantità per scoprire personalmente questo nuovo protocollo. L'ecosistema si sta evolvendo rapidamente e Arkade è all'avanguardia in questa innovazione.



## Risorse



Per saperne di più, consultate le risorse ufficiali:





- Sito web di Arkade**: [arkadeos.com](https://arkadeos.com)
- Documentazione**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Protocollo Ark**: [ark-protocol.org](https://ark-protocol.org)
- Codice sorgente** : [GitHub Arkade](https://github.com/arkade-os)
---
name: Zenzero Wallet
description: Software Bitcoin Wallet, Fork da Wasabi Wallet, che integra Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet è un portafoglio Bitcoin open source, non custodiale, incentrato sulla riservatezza e sulla privacy. È nato come Fork da Wasabi Wallet (dopo la versione 2.0.7.2 - licenza MIT).



Ginger Wallet mantiene l'architettura tecnica di Wasabi, aggiungendo alcune caratteristiche specifiche. Secondo la [documentazione di Ginger Wallet](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet), Wasabi enfatizza **autonomia e controllo**, mentre Ginger si concentra su **facilità d'uso, sicurezza e un'esperienza semplificata**, rendendolo accessibile a chi ha meno familiarità con gli aspetti tecnici.



Ginger Wallet è un software Wallet solo per computer (nessuna applicazione mobile).



## Che cos'è il CoinJoin?



Il CoinJoin** è un particolare tipo di struttura di transazione Bitcoin che riunisce diversi partecipanti in un'unica transazione collaborativa. Questo meccanismo mescola le voci di diversi utenti in una transazione comune, rendendo estremamente difficile - se non spesso impossibile, se fatto correttamente - la tracciabilità dei fondi. Di conseguenza, diventa quasi impossibile per un osservatore esterno identificare con certezza l'origine e la destinazione dei bitcoin coinvolti, a differenza di quanto avviene nelle transazioni Bitcoin convenzionali.



Per l'utente, il CoinJoin aiuta a preservare la sua riservatezza. Ad esempio, se ricevete una donazione di 10.000 Sats su un Bitcoin Address, il mittente può tracciare questi fondi e, in alcuni casi, dedurre che possedete una quantità maggiore di bitcoin o osservare le vostre attività. Effettuando un CoinJoin dopo questa donazione di 10.000 Sats, interrompete la tracciabilità: il mittente non sarà più in grado di ricavare alcuna informazione su di voi da questo pagamento.



Chaumian CoinJoin offre un elevato livello di sicurezza, poiché i fondi rimangono sempre sotto il controllo esclusivo dell'utente. Nemmeno gli operatori dei server di coordinamento possono deviare i bitcoin dei partecipanti in nessun caso. Né gli utenti né i coordinatori devono fidarsi l'uno dell'altro: ognuno mantiene il controllo delle proprie chiavi private e rimane l'unico autorizzato a convalidare le transazioni. Nessuna terza parte può quindi appropriarsi dei vostri bitcoin durante una CoinJoin, né stabilire un collegamento diretto tra le vostre entrate e le vostre uscite.



Per saperne di più sul CoinJoin, consultate il corso BTC 204 della Plan ₿ Academy:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Installare Ginger Wallet



Per installare Ginger Wallet, visitare il sito web [Ginger Wallet](https://gingerwallet.io).



Premete **Download** per scaricare la versione giusta per il vostro computer (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Un'altra opzione è quella di andare su [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) per scaricare il progetto.



![screen](assets/fr/04.webp)



Eseguire quindi il programma di installazione.



![screen](assets/fr/05.webp)




## Impostazioni dei parametri



### Configurazioni preliminari



Aprire Ginger Wallet, scegliere la lingua preferita.



![screen](assets/fr/06.webp)



Fin dall'inizio, Ginger ricorda i costi che comporta il processo CoinJoin.



![screen](assets/fr/07.webp)



Premere quindi **Avvio**, poi **Nuovo** per creare un nuovo portafoglio.



![screen](assets/fr/08.webp)



Quindi, salvare e confermare il seedphrase.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Per una maggiore sicurezza, Ginger Wallet offre la possibilità di aggiungere un passphrase.



![screen](assets/fr/11.webp)



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Questo passphrase, una volta aggiunto, verrà richiesto ogni volta che si cercherà di accedere al portafoglio.



![screen](assets/fr/12.webp)



Ginger attiva automaticamente il **CoinJoin** predefinito quando si crea il portafoglio. L'utente viene informato di ciò e può quindi personalizzare l'impostazione in base alle proprie esigenze.



![screen](assets/fr/13.webp)




### Impostazioni generali



Dopo aver creato il vostro primo portfolio, verrete portati al Interface Wallet di Ginger.



![screen](assets/fr/14.webp)



Attivare la modalità **Discreta**, se si desidera nascondere i saldi dei portafogli.



![screen](assets/fr/15.webp)



Su Ginger Wallet è possibile creare più portafogli. Basta cliccare su **Aggiungi un portafoglio**.



![screen](assets/fr/16.webp)



Ginger supporta l'uso di portafogli hardware tramite lo standard Bitcoin core Interface, anche se l'integrazione diretta da o verso un portafoglio hardware non è ancora disponibile.



I portafogli hardware compatibili includono (ma non sono limitati a) :




- BLOCKSTREAM Giada
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Modello T
- Trezor Safe 3
- ecc.



Cliccare ora su **Impostazioni**.



![screen](assets/fr/17.webp)



Queste impostazioni sono quelle dell'applicazione in generale e le configurazioni effettuate si applicano a tutti i portafogli.



In **Impostazioni** sono presenti le schede :





- Generale**



![screen](assets/fr/18.webp)





- Aspetto



In questa scheda è possibile modificare, tra l'altro, la lingua, la valuta e l'unità di visualizzazione delle tariffe (BTC/Satoshi).



![screen](assets/fr/19.webp)





- Bitcoin**



Questa scheda consente di abilitare l'esecuzione del Bitcoin Knots all'avvio dell'applicazione, di scegliere la rete (Main/RegTest) e il fornitore di tariffe (Mempool Space/BLOCKSTREAM info/Full node), ecc.



![screen](assets/fr/20.webp)





- Caratteristiche di sicurezza**



Nella scheda Sicurezza è possibile abilitare l'autenticazione a due fattori, attivare o disattivare Tor e persino disabilitarlo una volta chiusa l'applicazione Ginger.



![screen](assets/fr/21.webp)



**NB** :




- Per l'autenticazione a due fattori, assicurarsi che l'applicazione di autenticazione supporti il protocollo SHA256 e i codici a 8 cifre. Ginger Wallet richiede un codice 2FA a 8 cifre per una maggiore sicurezza. Questo formato più lungo rende il codice molto più difficile da indovinare o da compromettere, offrendo una maggiore protezione contro gli accessi non autorizzati.
- Per impostazione predefinita, tutto il traffico di rete di Ginger passa attraverso Tor, eliminando la necessità di una configurazione manuale. Se Tor è già attivo sul sistema, Ginger gli darà automaticamente la priorità.



Ma una volta disattivato Tor nelle impostazioni, la privacy rimane generalmente preservata, tranne in due situazioni:




- durante un CoinJoin, il coordinatore potrebbe collegare gli ingressi e le uscite al Address IP;
- quando si trasmette una transazione, un nodo malintenzionato a cui ci si connette potrebbe associare la transazione al proprio IP.



Non dimenticare di premere ogni volta **Fatto** (in basso a destra Coin) per salvare le impostazioni. Alcune impostazioni richiedono il riavvio di Ginger Wallet per avere effetto.



Inoltre, la barra di ricerca nella parte superiore dei portafogli consente di cercare e accedere a qualsiasi parametro, ecc...



![screen](assets/fr/22.webp)




### Configurazione del portafoglio



Nell'applicazione è possibile creare diversi portafogli, in modo da poterli configurare in base alle proprie esigenze. A tale scopo, fare clic sui **tre puntini** davanti al nome del portafoglio, quindi su **Impostazioni del portafoglio**.



![screen](assets/fr/23.webp)



Come potete vedere, oltre al parametro Wallet, potrete vedere i vostri UTXO (elenco dei token che possedete), le statistiche e le informazioni Wallet (la chiave pubblica estesa, ad esempio).



Per tornare alla configurazione del portafoglio, una volta cliccato su Parametri del portafoglio, si accede alle schede seguenti:




- Generale** (dove è possibile modificare il nome del portafoglio) ;



![screen](assets/fr/24.webp)





- CoinJoin** (dove è possibile personalizzare le impostazioni CoinJoin di questo portafoglio) ;



![screen](assets/fr/25.webp)





- Strumenti** (dove è possibile controllare il seedphrase, sincronizzare nuovamente il portafoglio o eliminarlo).



![screen](assets/fr/26.webp)




## Ricevere bitcoin



Per ricevere bitcoin nel proprio Wallet su Ginger Wallet :




- premere **Ricevi** ;



![screen](assets/fr/27.webp)





- Inserire il nome della fonte a cui si desidera associare il Address. Si tratta di un'etichetta per tenere traccia dei pagamenti. Non ha alcuna implicazione per il On-Chain; è semplicemente un'informazione di tracciabilità memorizzata localmente nell'applicazione;



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- fare clic sulla piccola freccia a sinistra di **generate** per scegliere il formato Address (**SegWit** /**Taproot**), quindi fare clic su **generate**, per generate e Address e codice QR.



![screen](assets/fr/29.webp)



Questo codice Address o QR sarà utilizzato dal mittente per inviare i bitcoin.



![screen](assets/fr/30.webp)




## Inviare bitcoin



Video tutorial su come inviare tramite Ginger Wallet.



![Vidéo](https://youtu.be/2nf5aAimfhg)



Per fare questo :




- Premere il tasto **Invio**;
- inserire il Address del destinatario, l'importo da inviare e un'etichetta;
- controllare la panoramica della transazione e confermare l'invio.



![screen](assets/fr/31.webp)




## Spendere bitcoin



È facile comprare e vendere Bitcoin con Ginger Wallet. In pochi passi è possibile spendere i propri bitcoin.



### Acquistare bitcoin



Gli utenti di Ginger Wallet possono acquistare bitcoin.





- Premere il pulsante **Acquista**. Questo pulsante rimane visibile anche se il Wallet è vuoto.



![screen](assets/fr/32.webp)





- Prima di procedere all'acquisto di un Bitcoin, è necessario selezionare il proprio Paese o anche il proprio Stato (in alcune regioni, come il Canada). Infatti, quando si fa clic per la prima volta sulla funzione **Acquista**, è necessario specificare anche la propria regione.



![screen](assets/fr/33.webp)



Premere **Continua** per avanzare nel processo di acquisto.





- Inserite quindi l'importo di bitcoin che desiderate acquistare nel campo dedicato. È inoltre possibile scegliere la valuta della transazione.



![screen](assets/fr/34.webp)



Ogni valuta ha un limite minimo e massimo di acquisto. Ad esempio, in USD, il limite massimo è di 30.000 dollari.



Se si è già effettuato un acquisto, è possibile visualizzare la cronologia delle transazioni facendo clic sul pulsante **Ordini precedenti**. Verrà visualizzato un elenco delle transazioni passate e del loro stato.





- Scegliete l'offerta che fa per voi.



A questo punto, viene visualizzato un elenco di tutte le offerte disponibili. Per ogni offerta, avete :




 - nome del fornitore (1) ;
 - il numero di bitcoin equivalente all'importo precedentemente inserito, il metodo di pagamento e la commissione di acquisto (2) ;
 - il pulsante **Accetta** (3).



![screen](assets/fr/35.webp)



Le tariffe indicate nell'offerta non costituiscono un costo aggiuntivo. Sono già incluse nell'importo totale dell'offerta.



La Coin in alto a destra dello schermo con l'etichetta **Tutti** consente di filtrare le offerte in base al metodo di pagamento. Il metodo di pagamento selezionato viene impostato come predefinito, ma può essere modificato in qualsiasi momento.



![screen](assets/fr/36.webp)



Se trovate un'offerta adeguata, fate clic sul pulsante **Accetta** per procedere all'acquisto. Verrete quindi reindirizzati alla pagina del venditore, dove potrete concludere la transazione.



### Vendere bitcoin



Gli utenti di Ginger Wallet possono vendere Bitcoin. Il pulsante **Vendi** è visibile solo quando ci sono fondi disponibili nel portafoglio.





- Fare clic su **Vendita**.



![screen](assets/fr/37.webp)





- Come per l'opzione **Acquista**, quando si utilizza la funzione Vendi per la prima volta, è necessario selezionare il proprio Paese prima di procedere con una vendita di Bitcoin.





- Successivamente, è necessario inserire la quantità di Bitcoin che si desidera vendere. L'importo può essere espresso in BTC o in una valuta fiat, come il dollaro USA (USD).





- Una volta fatto ciò, verrà visualizzato un elenco di offerte disponibili. Scegliete l'offerta di vendita che fa per voi, quindi fate clic su **Accetta** per continuare.





- Ora è necessario finalizzare la transazione:
 - Una volta accettata un'offerta, verrete reindirizzati alla pagina del fornitore;
 - Seguire le istruzioni riportate nella pagina del fornitore;
 - A un certo punto, riceverete un Address del destinatario e l'importo esatto da inviare;
 - Tornare quindi a Ginger Wallet per continuare il processo;
 - Una volta tornati a Ginger Wallet, apparirà una finestra di dialogo che consentirà di continuare facendo clic su **Invia**.



Si aprirà la schermata **Invio** con il Address e l'importo del destinatario precompilati. È anche possibile utilizzare il pulsante **Invia** nella schermata iniziale. Anche se è possibile inviare la transazione manualmente, si consiglia di completarla tramite la finestra di dialogo per ottimizzare il processo.



## Realizzare un CoinJoin su Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Proteggete la riservatezza dei vostri bitcoin con **CoinJoin**, integrato direttamente in Ginger Wallet. Il Wallet utilizza **WABISABI**, un protocollo Chaumian CoinJoin progettato per facilitare coinjoin più accessibili ed efficienti.



Sta a voi scegliere la strategia CoinJoin (automatica o manuale) più adatta a voi.



Ginger CoinJoin è pronto all'uso non appena viene scaricato (non sono necessari ulteriori passaggi). Ginger CoinJoin viene eseguito automaticamente in background per proteggere la vostra privacy a ogni transazione. In pratica, il lettore CoinJoin appare ogni volta che si ha un saldo che può essere anonimizzato.



Per quanto riguarda l'avvio manuale di CoinJoin, è sufficiente un clic. Avviate il round e attendete che la transazione CoinJoin venga creata e confermata. Vedrete il punteggio di anonimizzazione in Interface.



È possibile eseguire diversi mix fino a raggiungere il livello di anonimato desiderato. È anche possibile escludere alcune parti dal mix.



Per impostazione predefinita, Ginger utilizza il proprio coordinatore con tutti i parametri preconfigurati e le commissioni garantite. Le Coinjoin di token di valore superiore a 0,03 BTC comportano una commissione del coordinatore dello 0,3% oltre alla commissione Mining. Gli ingressi di valore pari o inferiore a 0,03 BTC, così come i remix, sono esenti da commissioni di coordinamento, anche dopo una singola transazione. Pertanto, un pagamento effettuato con fondi CoinJoin consente sia al mittente che al destinatario di rimescolare le proprie monete senza incorrere nelle commissioni di coordinamento.



Ginger preferisce coinjoin con più partecipanti a round più piccoli e veloci. Le coinjoin più grandi offrono maggiore anonimato, costi più bassi e una maggiore efficienza dello spazio BLOCK.




## Sicurezza e buone pratiche



Il desiderio di decentralizzazione e la salvaguardia della privacy richiedono l'adozione di diverse best practice:




- Conservare sempre il seedphrase in un luogo sicuro e non in linea;
- In caso di smarrimento del computer o di sospetto di accesso non autorizzato, creare immediatamente un nuovo Wallet. Trasferite i fondi in questo nuovo portafoglio e cancellate quello vecchio;
- Utilizzare un Address diverso per ogni ricezione per evitare di riutilizzare gli indirizzi;
- Scaricate sempre le applicazioni del vostro portfolio esclusivamente dall'account ufficiale GitHub o dal sito web ufficiale.



Ora avete familiarità con l'utilizzo dell'applicazione Ginger Wallet per inviare, ricevere e spendere i vostri bitcoin.



Se questa esercitazione vi è stata utile, lasciatemi un pollice Green qui sotto. Sentitevi liberi di condividere questo articolo attraverso le vostre piattaforme di social media. Grazie mille!



Vi suggerisco anche di dare un'occhiata a questo tutorial su come utilizzare l'applicazione informatica Liana per inviare e ricevere bitcoin, nonché per implementare un piano patrimoniale automatizzato.



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
---
name: Zeus Embedded
description: Come utilizzare il Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS è inizialmente un'applicazione mobile per la gestione remota dei nodi lightning, che consente di controllare il nodo installato su un server remoto


Ma l'applicazione presenta anche un "nodo incorporato".



**È questo aspetto dell'applicazione che esploreremo in questo tutorial.** Questo permette a chiunque di avere il proprio nodo lightning su cellulare, senza la necessità di un server dedicato, allo stesso modo in cui ACINQ offre il suo incredibile Wallet lightning Phoenix.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Come promemoria, Lightning è una rete che opera in parallelo con Bitcoin, consentendo di scambiare bitcoin senza dover effettuare sistematicamente transazioni On-Chain. Il risultato è una transazione quasi istantanea, senza dover attendere 10 minuti per la convalida del blocco. Il risultato è una transazione quasi istantanea, senza dover attendere 10 minuti per la convalida di un blocco. Questo è particolarmente utile quando si paga un commerciante nel mondo fisico. Inoltre, Lightning offre un notevole livello di **confidenzialità** che la rete Bitcoin non possiede in modo nativo*.



**Zeus "Integrated "** si rivolge ai Bitcoiners che vogliono massimizzare la propria privacy e autonomia.


In breve, è **potenzialmente** il Wallet mobile dei sogni dei cypherpunks. Anche se è ancora in fase embrionale (versione alfa) e soggetto a qualche bug, le sue caratteristiche sono numerose e non c'è dubbio che farà la gioia dei più intrepidi tra noi, che vogliono il massimo controllo e la massima opzionalità.



D'altra parte, non credo che al momento sia adatto ai principianti che non hanno familiarità con il Bitcoin e vogliono semplicemente un modo semplice per inviare/ricevere satoshis. Anche se questo potrebbe cambiare in futuro, dato che è in fase di implementazione una funzione di custodia tramite il protocollo Cashu (chaumian Ecash) per i principianti...



## Installare l'applicazione



Andate su [il sito web del progetto](https://zeusln.com/) per scaricare l'applicazione per il sistema operativo del vostro smartphone:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Creazione del portafoglio



Una volta avviata l'applicazione, fare clic sul pulsante "Quick Start" (Avvio rapido) per iniziare a creare il Wallet.



![image](assets/fr/03.webp)





Apparirà quindi una serie di schermate di inizializzazione. Attendere qualche istante, quindi attendere qualche minuto finché il nodo non sarà sincronizzato al 100% tramite Neutrino.



Questa operazione potrebbe richiedere alcuni minuti. A titolo informativo, il neutrino è un modo per i portafogli mobili di accedere alle informazioni Blockchain Bitcoin, senza dover eseguire un Full node.



![image](assets/fr/04.webp)





Dopo qualche istante, siete pronti a partire.



![image](assets/fr/05.webp)




## Configurazione dell'applicazione



Pronti, beh, non proprio, perché è ovvio che un utente Zeus degno di questo nome naviga con classe e stile sulla sua Wallet. Quindi dovremo cambiare il suo avatar.



Cliccate sul vostro avatar nell'angolo in alto a destra dello schermo:



![image](assets/fr/06.webp)





Fare clic sulla ruota dentata, quindi sul più "+" :



![image](assets/fr/07.webp)





Selezionate la foto più bella di Zeus per rappresentare questo Wallet e cliccate su "SCEGLI IMMAGINE" in fondo allo schermo, poi tornate indietro cliccando sulla freccia in alto a destra.



![image](assets/fr/08.webp)





Infine, assegnare al Wallet un soprannome e fare clic su "SAVE Wallet CONFIG" per rendere effettiva la modifica. Infine, fare clic sulla freccia indietro nell'angolo in alto a sinistra per tornare alla schermata iniziale.



![image](assets/fr/09.webp)





Questa volta possiamo davvero iniziare.



![image](assets/fr/10.webp)



### Biometria



Per proteggere l'accesso al Wallet, è possibile aggiungere un PIN/una password e attivare la biometria.



Per farlo, accedere al menu principale di Wallet facendo clic sui trattini orizzontali in alto a sinistra.



![image](assets/fr/11.webp)





Selezionare "Impostazioni", quindi "Sicurezza" e infine "Imposta/modifica PIN".



![image](assets/fr/12.webp)





Creare il PIN, confermarlo e attivare la biometria premendo il pulsante corrispondente "Biometria".  Tornare al menu principale utilizzando la freccia in alto a sinistra.



![image](assets/fr/13.webp)




### Salva la frase Mnemonic



Una volta tornati al menu principale, cliccate su "Backup di Wallet", quindi leggete il testo di avvertimento che vi informa che perdere le 24 parole che state per ricevere equivale a perdere l'accesso ai vostri fondi, e che chiunque abbia queste parole oltre a voi può accedere ai vostri fondi. Non datele mai a nessuno.



Selezionare "Ho capito" nella parte inferiore dello schermo. Fare quindi clic su ciascuna delle 24 parole per visualizzarle e annotarle con attenzione.



Potete scriverlo su carta o, per maggiore sicurezza, inciderlo su acciaio inossidabile per proteggerlo da incendi, inondazioni o crolli. La scelta del supporto per il vostro Mnemonic dipenderà dalla vostra strategia di sicurezza, ma se utilizzate Zeus come portafoglio spese contenente importi moderati, la carta dovrebbe essere sufficiente.



Per ulteriori informazioni sul modo corretto di salvare e gestire la frase Mnemonic, vi consiglio di seguire quest'altra guida, soprattutto se siete principianti:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Una volta terminato, cliccate su "HO FATTO IL BACKUP DELLE MIE 24 PAROLE" nella parte inferiore dello schermo e torniamo alla schermata iniziale, pronti a ricevere i nostri primi bitcoin.




## Opzione 1 - Ricevere bitcoin On-Chain e aprire un canale Lightning



**Zeus Embedded** è stato progettato principalmente come nodo fulmineo incorporato, ma può essere utilizzato anche come Wallet On-Chain.



Per ricevere i bitcoin On-Chain, cliccare sul pulsante "On-Chain" e poi su "Ricevi".


Infine, scansionare il codice QR o copiare il codice Bitcoin Address per depositare i fondi.



![image](assets/fr/15.webp)





Una volta che i fondi sono stati confermati e accreditati sul vostro Wallet, potete usarli per aprire un **canale Lightning**. Il vostro canale Lightning è la vostra porta d'accesso al Lightning Network, che vi consentirà di effettuare Exchange bitcoin in modo molto più riservato e rapido.





- A tal fine, fare clic su "SPOSTARE FONDI On-Chain SU LIGHTNING"



Nella schermata successiva, viene chiesto di aprire un canale in collaborazione con **"Olympus by Zeus "**, l'LSP (Lightning Service Provider) preferito da Wallet.


Per questa esercitazione, sceglieremo questa opzione per semplicità, ma è perfettamente possibile aprire canali con qualsiasi nodo della rete.


È anche possibile aprire più canali in un'unica transazione, selezionando "APRI CANALE AGGIUNTIVO". *Ma di questo ci occuperemo in una versione "avanzata" del tutorial di **Zeus Embedded***.





- Quindi selezionare l'importo che si desidera dedicare a questo canale. Nel nostro caso, verranno utilizzati tutti i nostri fondi On-Chain, quindi attiviamo il pulsante "Usa tutti i fondi possibili".





- Infine, selezionare il pulsante "APRI CANALE" nella parte inferiore dello schermo.



![image](assets/fr/16.webp)





In pochi secondi, il canale viene stabilito e siamo pronti a effettuare le nostre prime transazioni Lightning. Nella schermata iniziale, possiamo vedere un piccolo orologio accanto al nostro saldo Wallet. Questo perché dobbiamo ancora aspettare 3 conferme On-Chain prima che il canale sia veramente operativo. Questo perché dobbiamo ancora attendere 3 conferme On-Chain prima che il canale sia veramente funzionante.



![image](assets/fr/17.webp)





Dopo le 3 conferme, notiamo che il nostro saldo è ora accreditato sull'inserto Lightning.



![image](assets/fr/18.webp)



Un piccolo dettaglio: quando facciamo clic sul menu in fondo allo schermo per visualizzare lo stato dei nostri canali lightning, vediamo che una piccola parte del nostro saldo non è disponibile per la spesa: possiamo spendere solo 208253 satoshis invece dei 210370 che abbiamo effettivamente. Questo è normale, perché è specifico del protocollo lightning.



Infine, va notato che il nostro partner Olympus si riserva il diritto di chiudere il canale a sua discrezione, ad esempio se non viene utilizzato. Per garantire il mantenimento del nostro canale, dovremo pagare l'LSP (Lightning Service Provider), come vedremo nel prossimo paragrafo, attraverso la seconda modalità di apertura del canale.





## Inviare bitcoin tramite Lightning



Ora che il nostro canale è attivo e funzionante, vediamo come utilizzarlo per pagare un fulmine Invoice (Invoice).



A tal fine, fare clic sul pulsante "Lampo", quindi su "Invia".



![image](assets/fr/19.webp)





Nella schermata successiva, copiate il vostro Invoice nel campo dedicato, oppure scansionatelo cliccando sull'icona in alto a destra. Infine, far scorrere il pulsante "Slide to Pay" verso destra per pagare.



![image](assets/fr/20.webp)






Aspettate qualche secondo e il Invoice sarà pagato e i vostri satoshi avranno viaggiato alla velocità della luce.



![image](assets/fr/21.webp)





Zeus consente poi di aggiungere una nota per denominare il pagamento o di visualizzare il percorso dei satoshi prima di raggiungere la destinazione (e le tariffe applicate da tutti i nodi intermedi). Questo è il tipo di funzionalità che amiamo di Wallet.



![image](assets/fr/22.webp)



Si noti che, a differenza di un Wallet come [Phoenix]([Plan ₿ Network - Phoenix](https://planb.network/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), con Zeus il percorso viene calcolato localmente e non delegato a terzi (ACINQ nel caso di Phoenix). Quindi siete gli unici a conoscere il destinatario del pagamento. Perdiamo un po' di efficienza (i pagamenti richiedono un po' più di tempo per essere completati, ma guadagniamo molto in termini di privacy).





Facendo clic sulla piccola freccia in fondo alla schermata iniziale, è possibile visualizzare anche la cronologia dei pagamenti. Qui vediamo in Green i 212.121 Sats ricevuti per il On-Chain, poi in rosso rispettivamente i 211.756 Sats usati per aprire il nostro canale, quindi i 121.212 satoshi usati per pagare il nostro fulmine Invoice.



![image](assets/fr/23.webp)





## Opzione 2 - Ricevere bitcoin direttamente su Lightning



Anziché aprire manualmente un canale, come abbiamo appena visto, è possibile ricevere fondi direttamente tramite Lightning, anche senza un canale preesistente, utilizzando Olympus, il LSP di Zeus.




- A tal fine, fare clic sul pulsante "Fulmine" nella schermata iniziale, quindi su "Ricezione".
- Scegliete quindi l'importo che desiderate ricevere nella casella "Importo" e selezionate il pulsante "CREA Invoice" in fondo alla schermata.



![image](assets/fr/24.webp)





La schermata successiva mostra i Invoice da pagare per ricevere i satoshi. Ci viene detto che l'LSP tratterrà 10.000 Sats se il pagamento viene effettuato tramite Lightning. Vedremo più avanti come si giustificano queste spese di apertura del canale.



Pagate il Invoice o fatelo pagare a qualcun altro e il canale verrà aperto automaticamente, ma detraendo i 10.000 Sats come concordato.



![image](assets/fr/25.webp)





Siamo ora a capo di 2 canali luminosi, il cui stato può essere controllato facendo clic sul pulsante indicato dalla freccia bianca nella parte inferiore della schermata iniziale.



Possiamo notare che, a differenza del canale aperto dalla nostra scala On-Chain, quello aperto direttamente dal fulmine non mostra alcun avviso.


Dal momento che avete pagato per la creazione di questo canale, il Lightning Service Provider (LSP) si impegna a mantenere il canale per 3 mesi e vi offre "liquidità in entrata". Sul canale inferiore, si può notare che la capacità di ricezione è di 96383 satoshis. L'LSP ha quindi vincolato un capitale per consentirvi di ricevere pagamenti direttamente dopo l'apertura del canale.



Quindi i 10.000 Satoshi di tasse pagate coprono: il costo dell'apertura del canale (transazione Bitcoin On-Chain, la garanzia di manutenzione del canale per 3 mesi e il blocco del capitale).



![image](assets/fr/26.webp)





Congratulazioni, ora siete pronti a utilizzare Zeus Embedded, il sistema di illuminazione mobile Wallet con le caratteristiche più avanzate del mercato.





Per saperne di più sul funzionamento tecnico del Lightning Network, potete trovare l'eccellente formazione gratuita sul Plan ₿ Network di Fanis Michalakis:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
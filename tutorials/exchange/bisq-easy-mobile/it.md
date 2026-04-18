---
name: Bisq Easy Mobile
description: Un protocollo di trading peer-to-peer per i nuovi utenti di bitcoin - nessun intermediario, nessun KYC.
---
![cover](assets/cover.webp)


## Introduzione


Il protocollo commerciale [Bisq Easy](https://bisq.network/bisq-easy/) è progettato per [Bisq 2](https://github.com/bisq-network/bisq2), il successore di [Bisq v1](https://github.com/bisq-network/bisq). Il Bisq 2 supporterà più protocolli di scambio, reti di privacy e identità. Facilita l'acquisto di Bitcoin con zero commissioni di scambio e nessun requisito di deposito cauzionale. Si rivolge ai nuovi acquirenti di Bitcoin che cercano un'opzione senza KYC e che desiderano essere avviati in modo efficiente da venditori esperti e competenti che hanno familiarità con la piattaforma Bisq.


Attualmente, Bisq Easy è l'unico protocollo commerciale per Bisq 2. In futuro sono previsti altri protocolli commerciali. Per saperne di più sul Bisq 2, consultare questo tutorial:


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

Questa breve guida è un complemento al tutorial precedente sull'acquisto del Bitcoin utilizzando l'applicazione [Bisq Easy Mobile](https://github.com/bisq-network/bisq-mobile) e Lightning.


## 1️⃣ Per iniziare


Per iniziare, scaricare Bisq Easy Mobile dalla [pagina di download] (https://bisq.network/downloads/). Si consiglia di verificare il download. Le istruzioni per la verifica sono disponibili anche sulla [pagina di download](https://bisq.network/downloads/). Dopo l'installazione, è necessario accettare l'"Accordo con l'utente". Quindi, creare un profilo pubblico composto da un `nickname` e da un avatar (rappresentato da un'icona `bot`). Con Bisq Easy è possibile creare più profili utente all'interno di un unico client. Dopo una breve inizializzazione, si arriva alla "schermata iniziale". L'applicazione mette in evidenza il materiale didattico direttamente sulla pagina principale. Toccare `Apri la guida al commercio` per familiarizzare con le informazioni più recenti.


![image](assets/en/01.webp)


La guida al commercio spiega tutto ciò che è importante in semplici passi:



- Come fare trading su Bisq Easy
- Come funziona il processo commerciale
- Cosa devo sapere sulle regole commerciali.


Un'altra sezione importante è **"Quanto è sicuro fare trading su Bisq Easy? "**


![image](assets/en/08.webp)


Selezionare la casella "Ho letto e compreso" e toccare "Fine".


![image](assets/en/02.webp)


## 2️⃣ Backup dei dati


Prima di iniziare, è necessario eseguire alcune operazioni di pulizia e creare un "backup" del file di salvataggio dei dati. Andate su `Più` > `Backup & Restore` per salvare il vostro profilo e la cronologia delle compravendite. Se si perde il dispositivo senza un backup, la reputazione e le operazioni in corso sono irrecuperabili. Fornire una `Password` per criptare il backup.


![image](assets/en/11.webp)


## 3️⃣ Offerte


Dalla `Schermata iniziale`, ci sono due modi per navigare verso le offerte. Toccare "Esplora offerte" al centro dello schermo o "Offerte" nel menu in basso. Da qui, selezionare la `valuta` in cui si desidera operare.


![image](assets/en/03.webp)


A differenza di [Bisq 1](https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04), che richiede una garanzia, Bisq Easy si affida esclusivamente alla reputazione del venditore come garanzia. Se da un lato questo approccio consente agli acquirenti di acquistare Bitcoin per la prima volta senza esserne precedentemente proprietari, dall'altro pone un elevato grado di fiducia nella capacità del venditore di consegnare Bitcoin dopo aver ricevuto i pagamenti in fiat. Pertanto, il modello di sicurezza Bisq Easy è ottimizzato solo per piccole quantità di scambi e le transazioni sono limitate a 600 USD equivalenti per transazione per minimizzare il rischio. Nella sezione "Libro delle offerte", selezionare i filtri per i metodi di pagamento e il regolamento in Lightning o Bitcoin (on-chain).


![image](assets/en/04.webp)


Dopo aver applicato i "filtri", selezionare un'offerta adeguata da un partner commerciale affidabile. Verranno visualizzati il metodo di pagamento e il tipo di transazione prescelti dal venditore (`Lightning` o `on-chain`). Assicurarsi che questi corrispondano alle proprie preferenze prima di procedere. Qui selezioniamo l'opzione Lightning ⚡.


![image](assets/en/05.webp)


Rivedere e confermare i dettagli dell'operazione toccando "Conferma accettazione offerta". Una schermata popup confermerà che l'offerta è stata accettata con successo. Toccare Mostra compravendita in "Compravendite aperte". Nella sezione Compravendite aperte, incollate la vostra "fattura Lightning" e toccate "Invia al venditore" per condividerla. Attendere ora i dati del conto di pagamento del venditore. I venditori potrebbero impiegare del tempo per rispondere. Controllate periodicamente gli aggiornamenti nella finestra di chat.


![image](assets/en/06.webp)


Inviate un breve saluto nella chat. Il venditore condividerà i dettagli del pagamento quando sarà online


![image](assets/en/09.webp)


Una volta ricevuti i dati necessari per il pagamento dal venditore, procedere con il completamento del pagamento. Successivamente, toccare il pulsante "Conferma di aver effettuato il pagamento" e attendere pazientemente la conferma della ricezione. ️ ⌛️


Infine, quando il venditore conferma la ricezione del pagamento, è necessario confermare anche la ricezione del Bitcoin. Questo completa l'acquisto del Bisq in modalità Easy. Congratulazioni! Ora è possibile toccare il pulsante "Chiudi lo scambio".


![image](assets/en/10.webp)


## 4️⃣ Risoluzione delle controversie su Bisq Easy


Se qualcosa va storto nella compravendita, sia gli acquirenti che i venditori possono richiedere un supporto di mediazione.


**Cosa possono fare i mediatori

- Contribuire a facilitare il completamento del commercio

- Verifica dei pagamenti in fiat, altcoin e Bitcoin

- Annullare le operazioni quando necessario

- Segnalare ai moderatori gravi violazioni delle regole per un potenziale divieto di utilizzo


**Conseguenze per i venditori fraudolenti:**

A seconda del tipo di reputazione:



- Reputazione del BSQ Bond**: La DAO può confiscare il BSQ vincolato
- Cipolla Address Reputazione**: Il loro indirizzo Bisq 1 cipolla può essere bandito


**Nota importante:** Poiché la reputazione è legata al profilo dell'utente, un ban disabilita completamente la reputazione.


## 5️⃣ Create la vostra offerta


Invece di accettare le offerte esistenti, potete creare la vostra offerta di acquisto e lasciare che i venditori vengano da voi. Questa è l'opzione giusta se non si trovano offerte con il giusto premio o metodi di pagamento nel mercato in cui si desidera effettuare la compravendita, anche se bisognerà aspettare che un venditore accetti.


Nella schermata "Offerte", toccare l'icona verde "+" nell'angolo in basso a destra. Selezionare quindi `Acquista Bitcoin` e scegliere la valuta fiat.


Impostate i vostri parametri di trading:



- Importo fisso o importo a scelta**: Scegliere l'importo che si desidera spendere.
- Metodo di pagamento**: Selezionare una delle opzioni disponibili
- Insediamento**: Scegliere Lampo ⚡ o ₿ on-chain


Rivedere i dettagli e toccare "Crea offerta". L'offerta viene ora visualizzata nel "Libro delle offerte".


![image](assets/en/07.webp)


*Nota: come acquirente su Bisq Easy, non è necessaria la reputazione: questo è il vantaggio principale. I venditori si fanno carico dei requisiti di reputazione e del rischio, ed è per questo che applicano dei premi. La tua offerta deve semplicemente avere un prezzo sufficientemente interessante da essere presa in considerazione dai venditori rispettabili*


Una volta pubblicata, attendete nella sezione "Libro delle offerte". Quando un venditore accetta la vostra offerta, riceverete una notifica. Aprire la compravendita in `Open Trades`, dove il venditore e voi potrete scambiarvi i dettagli di pagamento. Inviare al venditore il proprio indirizzo Bitcoin o la fattura Lightning. Dopo l'invio, confermare il pagamento. Quando il venditore confermerà la ricezione, rilascerà il Bitcoin per completare lo scambio.


## 🎯 Conclusione


Bisq Easy consente di acquistare Bitcoin senza garanzie, risolvendo il classico problema dell'uovo e della gallina per i nuovi acquirenti. Il compromesso è chiaro: per la sicurezza ci si affida alla reputazione del venditore invece che ai fondi bloccati. Questo approccio basato sulla fiducia spiega il premio tipico del 5-15%, che compensa i venditori affidabili per il loro investimento nel creare fiducia e fornire supporto. Sebbene il sistema limiti le transazioni a piccole somme per contenere le perdite potenziali, è bene attenersi sempre a venditori con una solida reputazione. Per i nuovi arrivati disposti ad accettare queste condizioni, Bisq Easy offre un facile punto d'ingresso a Bitcoin.


## 📚 Bisq Risorse mobili semplici


[Github](https://github.com/bisq-network/bisq-mobile) | [Sito web ](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)
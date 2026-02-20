---
name: SMS4Sats
description: Ricevere e inviare SMS in modo anonimo pagando in Bitcoin Lightning
---

![cover](assets/cover.webp)

La verifica tramite SMS è diventata un must per molti servizi online. Che si tratti di creare un account su una piattaforma, convalidare una registrazione o confermare un'identità, i siti web richiedono quasi sistematicamente un numero di telefono. Questa pratica diffusa pone un grave problema a chiunque voglia preservare la propria privacy: il numero personale diventa un identificativo permanente, che collega le varie attività digitali alla tua identità reale e apre la porta a sollecitazioni commerciali indesiderate.

**SMS4Sats** risponde a questo problema offrendo numeri telefonici temporanei per ricevere e inviare SMS. Il servizio si distingue per il suo modello senza registrazione e per l'esclusivo pagamento in bitcoin tramite Lightning Network. Per pochi satoshi, si ottiene un numero usa e getta che consente di convalidare una registrazione senza mai rivelare il proprio numero personale.

Questo tutorial ti guida attraverso le tre funzioni di SMS4Sats: ricevere un SMS di verifica, inviare un SMS anonimo e noleggiare un numero temporaneo per alcune ore.


## Che cos'è SMS4Sats?

SMS4Sats è un servizio online accessibile all'indirizzo [sms4sats.com](https://sms4sats.com), che consente la gestione anonima degli SMS tramite pagamento in bitcoin su Lightning. Il servizio offre tre funzionalità distinte: ricezione di codici di verifica monouso, invio di SMS a qualsiasi numero e noleggio di numeri temporanei per diverse ore.

### Filosofia e modello operativo

Il progetto è stato concepito per garantire la massima riservatezza e sovranità finanziaria. Non richiedendo la creazione di un account e accettando solo pagamenti in bitcoin su Lightning, SMS4Sats elimina completamente la necessità di fornire dati personali. Non è richiesto nessun indirizzo e-mail, nessuna carta di credito, nessuna informazione personale. Per accedere ai servizi è necessario solo il pagamento Lightning.

Il servizio supporta oltre 400 siti e applicazioni in circa 120 Paesi, coprendo la maggior parte delle esigenze di verifica più comuni. Questa ampia copertura geografica consente di convalidare le registrazioni su diverse piattaforme, dai social network ai servizi di messaggistica.

### Modello di pagamento condizionato

SMS4Sats utilizza le invoice condizionate Lightning (invoice hodl) per la sua funzionalità di ricezione degli SMS. Questo meccanismo garantisce che l'addebito avvenga solo se l'SMS viene effettivamente ricevuto. Se non arriva alcun messaggio entro il tempo previsto (20 minuti al massimo), il pagamento viene automaticamente annullato e i satoshi vengono restituiti al tuo wallet. Questa garanzia non si applica alle funzioni di invio e noleggio, che non sono rimborsabili.


## Le tre funzionalità di SMS4Sats

L'interfaccia di SMS4Sats è organizzata in tre schede che corrispondono a tre usi distinti: **RECEIVE** per ricevere codici di verifica, **SEND** per inviare SMS anonimi e **RENT** per noleggiare un numero temporaneo.

### Ricevere un SMS

La funzione principale consente di ottenere un numero temporaneo per ricevere un codice di verifica unico. Una volta ricevuto e utilizzato il codice, il numero viene disattivato in modo permanente.

### Inviare un SMS

Questa funzione consente di inviare un SMS a qualsiasi numero di telefono senza rivelare la propria identità. Il destinatario riceverà il messaggio da un numero anonimo.

### Affittare un numero

Per gli utenti che hanno bisogno di ricevere più messaggi SMS su un unico numero, SMS4Sats offre un'opzione di noleggio temporaneo. Questa opzione consente di ricevere e inviare diversi messaggi durante il periodo di noleggio.

**Nota sui prezzi**: i prezzi indicati in questa guida sono indicativi. Variano a seconda del paese del numero, del servizio di destinazione e della domanda attuale. Ad esempio, un SMS verso Telegram Francia può costare da 1.500 a 5.000 satoshi, a seconda delle condizioni. Verifica sempre l'importo esatto dell'invoice Lightning prima di pagare.


## Ricevere un SMS di verifica

Vediamo in dettaglio come utilizzare SMS4Sats per ricevere un codice di verifica, illustrando la creazione di un account Telegram.

### Passo 1: Selezionare il paese e il servizio

Vai su [sms4sats.com](https://sms4sats.com) e rimani sulla scheda **RECEIVE**. Seleziona il paese del numero desiderato dal menu a discesa. Se il servizio di destinazione del tuo abbonamento è elencato, selezionalo per ottimizzare le possibilità di ricezione.

![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)

In questo esempio, selezioniamo la Francia come Paese e Telegram come servizio di destinazione. Fai clic su **NEXT** per passare alla fase successiva.

### Passo 2: pagare l'invoice Lightning

L'invoice Lightning viene visualizzata sotto forma di codice QR. L'importo varia a seconda del Paese e del servizio selezionato. Scansiona il codice QR con il tuo Lightning wallet o copia l'invoice per pagarla manualmente.

![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)

Nota il messaggio importante: "Nessun codice SMS = Nessun pagamento". Se non ricevi un SMS, il pagamento verrà automaticamente annullato e rimborsato entro un massimo di 20 minuti.

### Fase 3: ottenere il numero temporaneo

Una volta confermato il pagamento, viene immediatamente visualizzato il numero di telefono temporaneo. Un contatore indica il tempo rimanente per ricevere l'SMS.

![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)

Copia questo numero (qui +33 7 74 70 09 66) per utilizzarlo sul servizio per il quale desideri registrarti.

### Passo 4: utilizzare il numero sul servizio di destinazione

Immetti il numero temporaneo sull'applicazione o sul sito Web in cui è stato creato l'account. Nel nostro esempio Telegram, inserisci il numero, confermalo e attendi il codice di verifica.

![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)

Il processo è identico a quello della registrazione tradizionale: si inserisce il numero, Telegram invia un codice di verifica via SMS e poi si conclude la creazione dell'account.

### Passo 5: Recuperare il codice di verifica

Torna all'interfaccia di SMS4Sats. Non appena viene ricevuto l'SMS, viene visualizzato automaticamente il codice di attivazione. Clicca su **COPIA DEL CODICE** per copiarlo facilmente.

![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)

Immetti questo codice sul servizio di destinazione per completare la registrazione. Il numero temporaneo viene quindi disattivato in modo permanente.


## Inviare un SMS anonimo

SMS4Sats consente inoltre di inviare messaggi SMS a qualsiasi numero senza rivelare la propria identità.

### Fase 1: scrivere il messaggio

Fai clic sulla scheda **Invio**. Inserisci il numero di telefono di destinazione con il prefisso internazionale e scrivi il messaggio (massimo 1600 caratteri).

![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)

Fai clic su **NEXT** per procedere al pagamento.

### Passo 2: pagare e inviare

Paga l'invoice Lightning visualizzata. Una volta confermato il pagamento, l'SMS viene inviato immediatamente al destinatario.

![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)

Viene visualizzato un codice di conferma per confermare l'invio del messaggio. Il destinatario riceverà l'SMS da un numero anonimo.


## Noleggiare un numero temporaneo

Per gli usi che richiedono diversi messaggi SMS sullo stesso numero, la funzione NOLEGGIO consente di affittare un numero per diverse ore.

### Configurazione del noleggio

Fai clic sulla scheda **NOLEGGIO**. Seleziona il paese e la durata.

![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)

**Punti importanti da notare:**
- I prezzi variano a seconda del paese e della durata del noleggio.
- **I noleggi non sono rimborsabili**, a differenza degli SMS monouso.
- I numeri affittati in genere non funzionano con Telegram.
- Questa opzione è adatta per abbonarsi a più servizi in successione.

Una volta cliccato su **NEXT** e pagata l'invoice Lightning, otterrai un numero che puoi utilizzare per la durata del periodo di noleggio per ricevere e inviare messaggi SMS.


## Vantaggi e limiti

### Punti salienti

- **Non sono richiesti dati personali**: il modello senza registrazione garantisce che non vengano raccolti dati personali.

- **Tre funzioni aggiuntive**: ricezione, invio e noleggio coprono la maggior parte delle esigenze.

- **Pagamento solo in bitcoin**: Lightning Network consente transazioni istantanee e pseudonime.

- **Rimborso automatico**: quando si ricevono messaggi SMS, il sistema di invoice hodl garantisce il pagamento solo se l'SMS arriva.

### Vincoli da considerare

- **Sicurezza del canale SMS**: i codici SMS non sono un metodo di autenticazione solido e non dovrebbero essere utilizzati per gli account sensibili.

- **Compatibilità variabile**: molti siti rilevano e bloccano i numeri virtuali. Potrebbero essere necessari diversi tentativi.

- **Numeri non riutilizzabili**: dopo un singolo utilizzo, il numero viene riciclato e non può essere recuperato.

- **Noleggio non rimborsabile**: a differenza dei messaggi SMS una tantum, il noleggio non prevede una garanzia di rimborso.


## Le migliori pratiche

### Utilizzare Tor per una maggiore privacy

SMS4Sats è accessibile tramite [Tor](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). Questa configurazione maschera il tuo indirizzo IP quando accedi al servizio.

### Evitare gli account critici

Non utilizzare mai un numero usa e getta per i tuoi account importanti (banca, e-mail principale). Se queste piattaforme richiedono di riconfermare il numero in un secondo momento, perderai l'accesso all'account.

### Separa le tue identità digitali

Per gli account pseudonimi, combina il numero temporaneo con un indirizzo e-mail usa e getta e un browser isolato dal tuo uso abituale.

### Scegliere un 2FA robusto

Una volta creato l'account, attiva le soluzioni di autenticazione più forti: Applicazione TOTP (Aegis, Ente Auth) o chiave di sicurezza fisica FIDO2.


## Conclusione

SMS4Sats è una soluzione completa per la gestione degli SMS riservati. Che si voglia ricevere un codice di verifica, inviare un messaggio anonimo o affittare un numero temporaneo, il servizio soddisfa un'ampia gamma di esigenze di riservatezza, grazie al pagamento in bitcoin Lightning.

Tieni però presente i suoi limiti: il servizio non garantisce l'anonimato assoluto e non è adatto a conti sensibili o a lungo termine. Utilizzato con saggezza e consapevolezza dei suoi limiti, SMS4Sats è uno strumento pratico per riprendere il controllo delle tue comunicazioni telefoniche.


## Risorse

- [Sito ufficiale di SMS4Sats](https://sms4sats.com)
- [FAQ sul servizio](https://sms4sats.com/faq)
- [indirizzo Tor](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)

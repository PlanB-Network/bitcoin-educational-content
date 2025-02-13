---
name: Pesca
description: Guida completa all'utilizzo di Peach e allo scambio di bitcoin P2P
---
![cover](assets/cover.webp)

![peach](https://youtu.be/ziwhv9KqVkM)

## Introduzione

Gli scambi peer-to-peer (P2P) senza KYC sono essenziali per preservare la riservatezza e l'autonomia finanziaria degli utenti. Permettono di effettuare transazioni dirette tra individui senza la necessità di verificare l'identità, il che è fondamentale per coloro che tengono alla privacy. Per una comprensione più approfondita dei concetti teorici, date un'occhiata al corso BTC204:

https://planb.network/courses/btc204
### 1. Che cos'è la pesca?

Peach è una piattaforma di scambio P2P che consente agli utenti di acquistare e vendere bitcoin senza KYC. Offre un'interfaccia intuitiva e funzioni di sicurezza avanzate. Rispetto ad altre soluzioni come Bisq, HodlHodl e Robosat, Peach si distingue per la facilità d'uso e le basse commissioni.

### 2. Privacy e raccolta dati

**Quali informazioni raccoglie Peach?

Peach si impegna a memorizzare il minimo indispensabile di dati sui propri utenti. Ecco una panoramica dei dati memorizzati sui suoi server:


- Un hash dell'identificativo univoco della vostra applicazione (AdID)
- Un hash dei dati di pagamento
- Le vostre conversazioni criptate
- Dati sulle transazioni per garantire che gli utenti anonimi non superino il limite di trading (tipi di metodi di pagamento utilizzati, importi di acquisto e vendita)
- Indirizzi utilizzati per inviare e ricevere dal conto fiduciario
- Dati di utilizzo (Firebase & Google Analytics), solo con il vostro consenso

Come promemoria, un hash è un dato reso irriconoscibile, simile alla crittografia. Gli stessi dati produrranno sempre lo stesso hash, rendendo possibile l'individuazione di duplicati senza conoscere i dati originali.

*Per ulteriori informazioni sull'hashing, è possibile seguire questo corso:*

https://planb.network/courses/cyp201
**Chi può vedere i miei dati di pagamento?


- Solo la controparte può vedere i dettagli del pagamento
- I dati vengono trasmessi tramite i server Peach, ma sono completamente criptati da un capo all'altro
- In caso di controversia, i dati di pagamento e la cronologia delle conversazioni saranno visibili al mediatore Peach assegnato

## Installazione e configurazione

### 1. Installare l'applicazione Peach

![Installation de Peach](assets/fr/01.webp)


- Scaricate l'applicazione da [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/).
- Seguire le istruzioni di installazione del dispositivo.
- Durante l'installazione, vi verrà chiesto di scegliere se desiderate condividere alcuni dati per migliorare l'applicazione Peach (immagine 1)
- Nella schermata successiva (immagine 2), sono disponibili due opzioni:
 - Se siete un nuovo utente, cliccate su "Nuovo utente" per creare un nuovo profilo
 - Se si dispone già di un account, utilizzare "Ripristina" per ripristinare il profilo esistente
- Se avete un codice di riferimento, potete inserirlo qui.
- Per ripristinare un account esistente (immagine 3), è necessario :
 - Il file di backup
 - La password per decifrare il file

### 2. Panoramica delle schermate principali

L'applicazione Peach è organizzata in quattro schermate principali accessibili dalla barra di navigazione inferiore:

![Navigation dans l'application](assets/fr/02.webp)


- Home** : La schermata principale per l'acquisto e la vendita di bitcoin. Qui è possibile creare nuove transazioni e accedere alle offerte disponibili.
- Portafoglio**: Il vostro portafoglio bitcoin integrato che vi permette di :
 - Controllare il saldo
 - Ricevere bitcoin
 - Inviare bitcoin
 - Visualizzare la cronologia delle transazioni
- Commerci** : Il vostro centro di gestione del commercio dove troverete :
 - Le vostre transazioni correnti
 - Una storia completa dei vostri scambi
 - Lo stato di ogni transazione
- Impostazioni** : L'hub di configurazione dell'account per :
 - Gestire i metodi di pagamento
 - Configurare i backup
 - Personalizzare le preferenze
 - Accesso all'assistenza e al supporto

### 3. Configurare i metodi di pagamento

![Accès aux paramètres de paiement](assets/fr/03.webp)

Accedete ai metodi di pagamento tramite la scheda Impostazioni (immagine 8)

**Pagamenti online

![Configuration des paiements en ligne](assets/fr/04.webp)


- Fare clic sul pulsante per aggiungere un nuovo metodo di pagamento
- Scegliete la vostra valuta
- Selezionare il metodo di pagamento preferito

*Tipi di metodi di pagamento disponibili:*

***Trasferimenti bancari disponibili: ***


- SEPA (standard o istantaneo)
- Inserite le vostre coordinate bancarie SEPA

***Portafogli online accettati :***


- Sono disponibili diverse opzioni a seconda del paese (Revolut, Paypal, Wise, Strike, ecc.)
- Seguire le istruzioni per aggiungere i dati di accesso

***La carta regalo che può essere utilizzata :***


- Amazon
- Inserire il paese di emissione della carta e le altre informazioni necessarie

***Opzioni di pagamento nazionali:***

Sistemi di pagamento specifici per ogni paese :


- Satispay (Italia)
- MB Way (Portogallo)
- Bizum (Spagna)
- Pagamenti più rapidi (Regno Unito)

***Pagamenti di persona:***

![Configuration des paiements en personne](assets/fr/05.webp)


- Selezionare "Incontri
- Quindi selezionare il proprio incontro dall'elenco

### Istruzioni per l'uso


- È possibile impostare più metodi di pagamento contemporaneamente
- Più metodi si aggiungono, più ampia sarà la gamma di offerte a cui si avrà accesso
- Prima di registrarsi, verificare che i dati siano corretti
- È possibile modificare o eliminare i metodi di pagamento in qualsiasi momento

**Nota sulla sicurezza**: Le informazioni di pagamento sono criptate e condivise solo con il partner di scambio durante la transazione.

### 4. Come proteggere il vostro portafoglio

**Comprendere il proprio conto Peach

Un account Peach non è un account tradizionale con login e password. È un file memorizzato localmente sul vostro telefono, il che significa che Peach non ha bisogno di memorizzare i vostri dati o di conoscere la vostra identità: siete voi a controllarlo. Questo file contiene tutti i vostri dati, dalle chiavi del vostro portafoglio bitcoin ai dettagli dei vostri pagamenti.

Questo approccio garantisce una maggiore riservatezza, ma implica anche una maggiore responsabilità. Perdere il telefono senza un backup significa perdere l'accesso al conto Peach e ai fondi. È quindi fondamentale eseguire il backup di questo file e proteggerlo con una password forte.

**Creare i backup**

![Accéder aux sauvegardes](assets/fr/13.webp)


- Accedere alle impostazioni dalla scheda in basso a destra della schermata iniziale
- Selezionare l'opzione "backup" nel menu delle impostazioni

![Processus de sauvegarde](assets/fr/06.webp)

Sono disponibili due tipi di backup:

**Salvare il file del conto (immagine 14)**


- Fare clic su "Crea nuovo backup"
- Creare una password forte per crittografare il file di backup
- Conservare questo file in un luogo sicuro

Il backup dei file ripristina l'intero account Peach, compresi i file :


- Il vostro portafoglio
- I vostri metodi di pagamento
- Storia della conversazione
- Dati di pagamento
- Storico delle transazioni con i dettagli della controparte

**Salvataggio della frase di recupero (immagine 15)**


- Seguire le istruzioni per visualizzare la frase di recupero
- Scrivete con attenzione le parole nell'ordine corretto
- Conservare questo backup in un luogo sicuro, possibilmente diverso dal file dell'account

La frase di recupero recupera solo :


- Accesso al proprio account
- I vostri fondi bitcoin

Perderete :


- Storia della conversazione
- Dati di pagamento
- Informazioni sulla controparte nella cronologia delle transazioni

Per una sicurezza ottimale, si consiglia di eseguire entrambi i tipi di backup.

## Comprare e vendere Bitcoin

### 1. Come acquistare i Bitcoin

![Création et vue des offres](assets/fr/07.webp)


- Nella schermata iniziale, fare clic sul pulsante "Acquista" (immagine 16)
- Configurare l'acquisto in base alle proprie preferenze (immagine 17)
- Sfogliare l'elenco delle offerte disponibili (immagine 18)

![Sélection et confirmation d'achat](assets/fr/08.webp)


- Selezionate l'offerta che fa per voi (immagine 19)
- Effettuare il pagamento con il metodo concordato
- Confermare il pagamento nell'applicazione e valutare la transazione (immagine 20)

![Réception des bitcoins](assets/fr/09.webp)


- Tracciare lo stato della transazione
- Controllare la conferma di ricezione dei bitcoin
- I fondi saranno disponibili nel vostro portafoglio Peach

### 2. Come vendere Bitcoin

![Création d'un ordre de vente](assets/fr/10.webp)


- Configurare l'offerta di vendita (immagine 24)
- Finanziare la transazione inviando i bitcoin all'indirizzo fornito (immagine 25)
- Attendere la conferma della transazione (immagine 26)
- La vostra offerta è ora visibile agli acquirenti (immagine 27)

![Attente du paiement](assets/fr/11.webp)


- Monitorare lo stato della vostra offerta
- Attendere la conferma del pagamento da parte dell'acquirente
- Controllare i dettagli della transazione

![Finalisation de la vente](assets/fr/12.webp)


- Controllare lo stato dei pagamenti
- Confermare la ricezione del pagamento
- Valutare la transazione
- I bitcoin vengono rilasciati automaticamente all'acquirente

**Consigli per una transazione di successo**


- Rispondere rapidamente ai messaggi della controparte
- Controllare attentamente i dettagli del pagamento
- Non esitate a ricorrere al servizio di mediazione in caso di problemi

**Nota di sicurezza**: Non confermate mai la ricezione di un pagamento prima di averne verificato la ricezione sul vostro conto.

## Vantaggi e svantaggi

### Benefici della pesca


- Non è richiesto il KYC**: Preserva la riservatezza dell'utente.
- Nessun accesso ai dati bancari**: Peach non ha accesso alle vostre coordinate bancarie o alla vostra identità.
- Interfaccia intuitiva**: Facile da usare per gli utenti intermedi.
- Open Source** : Il codice sorgente è pubblico e verificabile dalla comunità.

### Svantaggi della pesca


- Liquidità limitata**: Volume di trading inferiore rispetto alle piattaforme più consolidate.
- Rischio normativo** : L'applicazione è gestita da una società svizzera. È quindi soggetta alle normative svizzere, che potrebbero evolvere e potenzialmente censurare l'applicazione.

## Risorse utili


- Video esplicativo in francese: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Guida rapida: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
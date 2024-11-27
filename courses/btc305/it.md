---
name: Bitcoin and BTC Pay Server
goal: Installare BTC Pay Server per la tua attività
objectives:
  - Capire cos'è btcpayserver.
  - Self-hostare e configurare BTC Pay Server.
  - Utilizzare btcpayserver nella tua attività quotidiana.
---

# Bitcoin e BTCPay Server

Questo è un corso introduttivo su BTCPay Server Operator scritto da Alekos e Bas, che è stato adattato nel formato del corso Plan ₿ da melontwist e asi0.

UNA STORIA NON FINITA

"Questo è falso, la mia fiducia in te è infranta, ti renderò obsoleto".

Prodotto dalla BTCPay Server Foundation

+++

# Introduzione

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Critiche entusiastiche per Bitcoin e BTCPay Server degli autori

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

Iniziamo con cosa è BTCPay Server e da dove provien. Valorizziamo la trasparenza e certi standard per formare fiducia nello spazio Bitcoin.
Un progetto in questo spazio ha infranto questi valori. Il lead developer di BTCPay Server, Nicolas Dorier, ha preso questa cosa personalmente e ha fatto la promessa di renderli obsoleti. Eccoci molti anni dopo, lavorando verso questo futuro, completamente open-source, ogni giorno.

> Questo è falso, la mia fiducia in te è infranta, ti renderò obsoleto.
> Nicolas Dorier

Dopo le parole pronunciate da Nicolas, era il momento di iniziare a costruire. È stato dedicato molto lavoro a quello che ora chiamiamo BTCPay Server. Più persone volevano supportare questa iniziativa. I più noti sono r0ckstardev, MrKukks, Pavlenex e il primo commerciante ad utilizzare il software, astupidmoose.

Cosa significa open source e cosa comporta un tale progetto?

FOSS sta per Free & Open-Source Software. Il primo termine si riferisce a condizioni che permettono a chiunque di copiare, modificare e persino distribuire versioni (anche a scopo di lucro) del software. Il secondo termine si riferisce alla condivisione aperta del codice sorgente, incoraggiando il pubblico a contribuire e migliorarlo.
Questo attira utenti esperti entusiasti di contribuire al software che già utilizzano e da cui traggono valore, dimostrando nel tempo di prevalere nell'adozione rispetto al software proprietario. È coerente con l'etica di Bitcoin secondo cui "le informazioni aspirano ad essere libere". Riunisce persone appassionate che formano una comunità ed è semplicemente più divertente. Come Bitcoin, il FOSS è inevitabile.

### Prima di iniziare

Questo corso è composto da più parti. Molte saranno gestite dal tuo insegnante in aula, ambienti demo a cui avrai accesso, un server ospitato per te stesso e, possibilmente, un nome di dominio. Se completi questo corso in modo indipendente, tieni presente che gli ambienti contrassegnati come DEMO non saranno disponibili per te.
NB. Se segui questo corso in aula, i nomi dei server potrebbero differire a seconda della configurazione della tua aula. Le variabili nei nomi dei server potrebbero essere diverse per questo motivo.

### Struttura del corso

Ogni capitolo ha obiettivi e valutazioni delle conoscenze. Copriremo ognuno di questi e avremo un riassunto delle caratteristiche chiave in ogni blocco di lezione (ad es. capitolo). Le illustrazioni sono presentate per fornire un feedback visivo e rafforzare i concetti chiave. Gli obiettivi sono stabiliti all'inizio di ogni blocco di lezione. Questi obiettivi vanno oltre una semplice lista di controllo. Ti forniscono una guida per acquisire un nuovo insieme di competenze. Le valutazioni delle conoscenze diventano progressivamente più sfidanti nella configurazione del tuo BTCPay Server.

### Cosa ricevono gli studenti con il corso?

Con il Corso su BTCPay Server, uno studente può comprendere i principi di base, sia tecnici che non, di Bitcoin. La formazione estensiva sull'uso di Bitcoin tramite BTCPay Server permetterà agli studenti di gestire la propria infrastruttura Bitcoin.

### Indirizzi Web importanti o opportunità di contatto

La Fondazione BTCPay Server, che ha permesso ad Alekos e Bas di scrivere questo corso, si trova a Tokyo, Giappone. È possibile contattare la Fondazione BTCPay Server tramite il sito web elencato;

- https://foundation.btcpayserver.org
- unisciti ai canali di chat ufficiali: https://chat.btcpayserver.org

## Introduzione a Bitcoin

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Comprendere Bitcoin tramite esercizi in classe

Questo è un esercizio in classe quindi, se segui questo corso da solo, non puoi eseguirlo ma puoi comunque approfondire questo esercizio. Per completare questo compito, il numero minimo di persone è tra 9 e 11.

L'esercizio inizia dopo aver guardato l'introduzione "Come funzionano Bitcoin e la blockchain" della BBC.

![come funzionano bitcoin e la blockchain](https://youtu.be/mhE_vvwAiRc)

Questo esercizio richiede la partecipazione di almeno nove persone. L'intento dell'esercizio è di ottenere fisicamente un'idea di come funziona Bitcoin. Interpretando ciascun ruolo nella rete, apprenderai in modo interattivo e divertente. Questo esercizio non coinvolge Lightning Network.

### Esempio; Richiede 9 / 11 persone

I ruoli sono:

- 1 Cliente
- 1 Commerciante
- 7 a 9 nodi Bitcoin

**La configurazione è la seguente:**

Il cliente acquista un prodotto dal negozio con Bitcoin.

**Scenario 1 - Sistema Bancario Tradizionale**

- Configurazione:
  - Vedi diagrammi/spiegazioni nell'allegato Figjam - [Schema dell'Attività](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Fai partecipare tre studenti volontari nei ruoli di Cliente (Alice), Commerciante (Bob) e Banca.
- Queata la sequenza degli eventi:
  - Cliente- naviga nel negozio online e trova un articolo per $25 che desidera, e informa il Commerciante che vorrebbe acquistarlo
  - Commerciante- chiede il pagamento.
  - Cliente- invia le informazioni della carta al Commerciante
  - Commerciante- inoltra le informazioni alla Banca (identificando sia la propria identità che quella del cliente) richiedendo il pagamento di
  - La Banca raccoglie informazioni sul Cliente e sul Commerciante (Alice e Bob) e verifica che il saldo del cliente sia sufficiente.
  - Deduce \$25 dal conto di Alice, aggiunge \$24 al conto di Bob, prende \$1 per il servizio
  - Il Commerciante riceve il via libera dalla Banca e spedisce l'articolo al cliente.
- Commenti:
  - Bob e Alice devono avere una relazione con una banca.
  - La banca raccoglie informazioni su entrambi, Bob e Alice.
  - La banca prende una percentuale.
  - La banca deve essere fidata in ogni momento per la custodia del denaro di ciascun partecipante.

**Scenario 2 - Sistema Bitcoin**

- Configurazione:
  - Vedi diagrammi/spiegazioni nell'allegato Figjam - [Schema dell'Attività](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
- Sostituire la Banca con nove studenti che interpreteranno il ruolo di un Computer (Nodi/Minatori di Bitcoin) in una rete per sostituire la Banca.
- Ognuno dei 9 Computer possiede un registro storico completo di tutte le transazioni passate (quindi saldi accurati senza falsificazioni), così come un insieme di regole:
  - Verificare che la transazione sia firmata correttamente (la chiave apre la serratura)
  - Trasmettere e ricevere transazioni valide ai pari nella rete, scartare quelle non valide (incluso qualsiasi tentativo di spendere gli stessi fondi due volte)
- Aggiornare/Aggiungere periodicamente i record con nuove transazioni ricevute da un computer "casuale" a patto che tutti i contenuti siano validi (nota: stiamo ignorando, per ora, la componente del Proof of Work, esclusivamente per semplicità), altrimenti rifiutare queste e continuare come prima fino a quando il prossimo computer "casuale" invia un aggiornamento
  - La quantità appropriata è stata inviata se i contenuti erano validi.
- Rappresentare la sequenza degli eventi:
  - Cliente- naviga nel negozio online e trova un articolo a $25 che desidera, e informa il Commerciante che vorrebbe acquistarlo
  - Commerciante- chiede il pagamento inviando al cliente una fattura/indirizzo dal proprio portafoglio.
  - Cliente- costruisce una transazione (inviando $25 in BTC a un indirizzo fornito dal Commerciante) e la trasmette alla Rete Bitcoin.
- Computer- ricevono la transazione e verificano:
  - Che ci sia almeno $25 di BTC nell'indirizzo da cui viene inviato
  - Che la transazione sia firmata correttamente (“sbloccata” dal cliente)
  - Se non è così, allora la transazione non verrà propagata attraverso la rete, diversamente verrà propagata e messa in attesa.
  - I commercianti possono controllare che la transazione sia in sospeso e in attesa.
- Un computer viene "casualmente" scelto per proporre di finalizzare la transazione proposta trasmettendo "un blocco" che la contiene; se risulta corretto, riceveranno una ricompensa in BTC.
  - OPZIONALE/AVANZATO - invece di selezionare casualmente un Computer, simulare il mining facendo lanciare ai Computer dei dadi fino a quando non si verifica un risultato predeterminato (ad es., il primo che ottiene un doppio sei viene selezionato)
  - Può anche rappresentare cosa succederebbe se due Computer vincono approssimativamente contemporaneamente, risultando in una divisione della catena.
  - I Computer controllano la validità, aggiornano/aggiungono record ai loro registri se le regole sono soddisfatte e trasmettono il blocco ai pari.
  - Il computer casualmente scelto riceve una ricompensa per aver proposto un blocco valido.
  - Il Commerciante controlla che la transazione sia stata finalizzata; quindi, i fondi sono stati ricevuti e l'articolo è stato inviato al cliente.
- Commenti:
  - Si noti che non è stata necessaria una preesistente relazione bancaria.
  - Non è necessario un terzo per facilitare; sostituito da codice/incentivi.
  - Nessuna raccolta di dati da parte di nessuno al di fuori dello scambio diretto e solo la quantità necessaria scambiata tra i partecipanti (ad es., indirizzo di spedizione).
  - Non è richiesta fiducia tra le persone (sennochè l'invio dell'articolo da parte Commerciante).
  - Il denaro è gestito e detenuto direttamente dagli individui.
  - Il registro di Bitcoin è rappresentato in dollari per semplicità, ma in realtà è in BTC.
  - Simuliamo una singola transazione trasmessa, ma in realtà, sono in sospeso nella rete molteplici transazioni, e i blocchi includono migliaia di transazioni contemporaneamente. I nodi controllano anche che non ci siano transazioni di doppia spesa in sospeso (scarterei tutte tranne una se fosse il caso).
- Scenari di imbroglio:
  - Cosa succede se il cliente non avesse $25 in BTC?
    - Non sarebbe in grado di creare la transazione perché “sbloccare” e “proprietà” sono la stessa cosa, e i computer controllano che la transazione sia firmata correttamente; altrimenti, la rifiutano.
- Cosa succede se il computer scelto casualmente tenta di "modificare il registro"?
  - Il blocco verrebbe rifiutato, poiché ogni altro computer ha una storia completa e noterebbe il cambiamento, violando una delle loro regole.
  - Il Computer Casuale non riceverebbe una ricompensa e nessuna transazione del loro blocco verrebbe finalizzata.

## Valutazione della conoscenza

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### Discussione in classe KA

Discutere alcune semplificazioni fatte nell'esercizio in classe sotto il secondo scenario e descrivere cosa fa effettivamente il sistema Bitcoin in modo più dettagliato.

### Revisione del vocabolario KA

Definire i seguenti termini chiave introdotti nella sezione precedente:

- Nodo
- Mempool
- Obiettivo di Difficoltà
- Blocco

**Discutere il significato di alcuni termini aggiuntivi come gruppo:**

Blockchain, Transazione, Doppia Spesa, Problema dei Generali Bizantini, Mining, Proof of Work (PoW), Funzione di Hash, Ricompensa del Blocco, Blockchain, Chain più Lunga, Attacco del 51%, Output, Blocco dell'Output, Cambio, Satoshis, Chiave Pubblica/Privata, Indirizzo, Crittografia a Chiave Pubblica, Firma Digitale, Portafoglio

# Introduzione a BTCPay Server

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## Comprensione della schermata di login di BTCPay Server

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Lavorare con BTCPay Server

L'obiettivo di questo blocco del corso sarà acquisire una comprensione generale del software BTCPay Server. In un ambiente condiviso, si raccomanda di seguire la dimostrazione dell'istruttore e seguire insieme il Manuale del Corso BTCPay Server. Imparerai come creare un portafoglio attraverso diversi metodi. Gli esempi includono configurazioni di portafogli caldi e portafogli hardware collegati tramite BTCPay Server Vault. Questi obiettivi verranno perseguiti in un ambiente Demo, a cui il tuo istruttore ti dara accesso.
Se segui questo corso da solo, puoi trovare un elenco di host di terze parti per scopi dimostrativi su https://directory.btcpayserver.org/filter/hosts. Sconsigliamo vivamente l'uso di queste opzioni di terze parti come ambienti di produzione, ma servono agli scopi giusti per un'introduzione all'uso di Bitcoin e BTCPay Server.

Come tirocinante rockstar di BTCPay Server, potresti avere esperienza precedente nella configurazione di un nodo Bitcoin. Questo corso si riferisce specificamente allo stack software di BTCPay Server.

Molte delle opzioni in BTCPay Server esistono in una forma o nell'altra in altri software relativi ai portafogli Bitcoin.

### Schermata di login di BTCPay Server

Quando vieni accolto nell'ambiente Demo, ti viene chiesto di 'Accedere' o 'Creare il tuo account'. Gli amministratori del server potrebbero disattivare la funzionalità di creazione di nuovi account per motivi di sicurezza. I loghi e i colori dei pulsanti di BTCPay Server possono essere modificati perché BTCPay Server è un software open source. Un host di terze parti può applicare il White-label al software e cambiare l'intero aspetto.

![immagine](assets/en/0.webp)

### Finestra di creazione di un account

La creazione di account su BTCPay Server richiede stringhe di indirizzi Email validi; example@email.com sarebbe una stringa valida per l'Email.

La password deve essere lunga almeno 8 caratteri, includendo lettere, numeri e caratteri. Dopo aver impostato la password, dovrai digitarla nuovamente per assicurarti che sia uguale a quella inserita la prima volta. 
Quando sia i campi Email che Password sono compilati correttamente, clicca sul pulsante "Crea Account". Questo salverà l'Email e la password sull'istanza del BTCPay Server dell'istruttore.
![image](assets/en/1.webp)

**!Nota!**

Se segui questo corso da solo, creare questo account potrebbe essere qualcosa che potresti fare su un host di terze parti; quindi, ancora una volta, menzioniamo di non usare questi come ambienti di produzione ma solo a scopo di formazione.

### Creazione Account da parte dell'Amministratore di BTCPay Server

L'Amministratore dell'Istanza di BTCPay Server può anche creare account per BTCPay Server. L'Amministratore dell'istanza di BTCPay Server può cliccare su "Impostazioni Server" (1), cliccare sulla scheda "Utenti" (2), e cliccare sul pulsante "+ Aggiungi Utente" (3) in alto a destra della scheda Utenti. Nell'Obiettivo (4.3), imparerai di più sul controllo degli account da parte dell'amministratore.

![image](assets/en/2.webp)

Come amministratore, avrai bisogno dell'indirizzo Email dell'utente per impostare una password standard. Si consiglia come Amministratore di informare l'utente che, per motivi di sicurezza, dovrebbe cambiare questa password prima di utilizzare l'account . Se l'Amministratore NON imposta una Password e SMTP è stato configurato sul server, l'utente riceverà un'email con un link di invito per creare il proprio account e impostare la password da solo.

### Esempio

Quando segui il corso con un istruttore, segui il link fornito dall'istruttore e crea il tuo account sull'ambiente Demo fornito. Assicurati che il tuo indirizzo email e la password siano salvati in modo sicuro; avrai bisogno di queste credenziali di accesso per il resto degli obiettivi dimostrativi in questo corso.

Il tuo istruttore potrebbe aver raccolto in anticipo l'indirizzo email e inviato un link di invito prima di questo esercizio. Se istruito, controlla la tua Email.

Quando segui il corso senza un istruttore, crea il tuo account utilizzando l'ambiente demo di BTCPay Server; vai su

https://mainnet.demo.btcpayserver.org/login.

Questo account dovrebbe essere utilizzato solo a scopo dimostrativo/formativo e mai per affari.

### Riepilogo delle Competenze

In questa sezione, hai imparato quanto segue:

- Come creare un account su un server ospitato tramite l'interfaccia.
- Come un amministratore del server può aggiungere manualmente utenti nelle impostazioni del server.

### Valutazione della Conoscenza

#### Revisione Concettuale KA

Fornisci motivi per cui utilizzare un Server Demo è una cattiva idea per scopi di produzione.

## Gestione dell'account utente

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Gestione Account su BTCPay Server

Dopo che un commerciante ha creato il proprio account, può gestirlo in Basso a Sinistra dell'interfaccia utente di BTCPay Server. Sotto il pulsante Account, ci sono diverse impostazioni di livello superiore.

- Modalità Scuro/Chiaro.
- Nascondi le Informazioni Sensibili.
- Gestisci Account.

![image](assets/en/3.webp)

### Modalità Scuro e Chiaro

Gli utenti di BTCPay Server possono scegliere tra una versione dell'interfaccia utente in Modalità Scuro o Chiaro. Le pagine rivolte ai clienti non cambieranno. Usano le impostazioni preferite dal cliente riguardo la modalità scuro o chiaro.

### Nascondi le Informazioni Sensibili

Il pulsante nascondi informazioni sensibili offre un semplice strato di sicurezza. Ogni volta che devi operare sul tuo BTCPay Server, ma potrebbero esserci persone che guardano oltre la tua spalla in uno spazio pubblico, attiva Nascondi Informazioni Sensibili, e tutti i valori in BTCPay Server saranno nascosti. Qualcuno potrebbe essere in grado di guardare oltre la tua spalla ma non potrà più vedere i valori con cui stai lavorando.

### Gestisci Account

Una volta che l'account utente è stato creato, qui è dove gestire le password, 2fa, o le chiavi API.

### Gestione Account - Account

Facoltativamente è possibile aggiornare  il proprio account con un indirizzo email diverso. Per assicurarsi che l'indirizzo email sia corretto, BTCPay Server consente di inviare un'email di verifica. Cliccare su salva se l'utente imposta un nuovo indirizzo email e conferma che la verifica ha avuto successo. Il nome utente rimane lo stesso dell'Email precedente.

Un utente può decidere di eliminare il proprio account. Ciò può essere fatto cliccando sul pulsante elimina nella scheda Account.

![immagine](assets/en/4.webp)

**!Nota!**

Dopo aver cambiato l'Email, il nome utente per l'account non cambierà. L'indirizzo Email precedentemente fornito rimarrà il nome per l'accesso.

### Gestione Account - Password

Uno studente potrebbe voler cambiare la sua password. Può farlo andando nella scheda Password. Qui è richiesto di digitare la sua vecchia password e può cambiarla con una nuova.

![immagine](assets/en/5.webp)

### Autenticazione a Due Fattori (2fa)

Per limitare le conseguenze di una password rubata, è possibile utilizzare l'autenticazione a due fattori (2fa), un metodo di sicurezza relativamente nuovo. È possibile attivare l'autenticazione a due fattori tramite la gestione account e la scheda per l'autenticazione a due fattori. È necessario completare un secondo passaggio dopo aver effettuato l'accesso con il proprio nome utente e password.

BTCPay Server consente due modi per abilitare il 2FA, 2FA basato su App (Authy, Google, Microsoft authenticators) o tramite dispositivi di sicurezza (FIDO2 o LNURL Auth).

### Autenticazione a Due Fattori - Basata su App

In base al sistema operativo del telefono cellulare (Android o iOS), gli utenti possono scegliere tra le seguenti app;

1. Scaricare un'autenticatore a due fattori;
   - Authy per [Android](https://play.google.com/store/apps/details?id=com.authy.authy) o [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator per [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) o [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator per [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) o [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. Dopo aver scaricato e installato l'App Authenticator.
   - Scansionare il QR Code fornito da BTCPay Server
   - Oppure inserire manualmente nella tua app Authenticator la chiave generata da BTCPay Server.
3. L'app Authenticator fornirà un codice unico. Inserire il codice unico in BTCPay Server per verificare l'impostazione e cliccare su verifica per completare il processo.

![immagine](assets/en/6.webp)

### Riepilogo delle Competenze

In questa sezione, hai appreso quanto segue:

- Opzioni di gestione dell'account e i vari modi per gestire un account su un'istanza di BTCPay Server.
- Come configurare il 2FA basato su app.

### Valutazione della Conoscenza

#### Revisione Concettuale KA

Descrivi come il 2FA basato su app aiuta a proteggere il tuo account

## Creazione di un nuovo negozio

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>

### Crea la tua procedura guidata per il negozio

Quando un nuovo utente accede a BTCPay Server, l'ambiente è vuoto e necessita di un primo negozio. La procedura guidata di introduzione di BTCPay Server offrirà all'utente l'opzione di "Creare il tuo negozio" (1). Un Negozio può essere visto come una Casa per le tue necessità in Bitcoin. Un nuovo Nodo BTCPay Server inizierà con la Sincronizzazione della Blockchain di Bitcoin (2). A seconda dell'infrastruttura su cui esegui BTCPay Server, ciò può richiedere dalle poche ore a qualche giorno. La versione corrente dell'istanza è mostrata nell'angolo in basso a destra della tua interfaccia utente BTCPay Server. Questo è utile come riferimento quando si riscontrano problemi.

![immagine](assets/en/7.webp)

### Procedura guidata per creare il tuo negozio

Questo corso inizierà con una schermata leggermente diversa rispetto alla pagina precedente. Poiché il tuo istruttore ha preparato l'ambiente Demo, la blockchain di Bitcoin è stata sincronizzata in precedenza e, quindi, non vedrai lo stato di sincronizzazione dei nodi.

Un utente può decidere di eliminare l'intero account. Questo può essere fatto cliccando sul pulsante di eliminazione nella scheda Account.

![immagine](assets/en/8.webp)

**!Nota!**

Gli account di BTCPay Server possono creare un numero illimitato di negozi. Ogni negozio è un portafoglio o "casa".

### Esempio

Inizia cliccando su "Crea il tuo negozio".

![immagine](assets/en/9.webp)

Questo creerà la tua prima Casa e dashboard per utilizzare BTCPay Server.

(1) Dopo aver cliccato su "Crea il tuo negozio", BTCPay Server richiederà di nominare il negozio; questo può essere qualsiasi cosa utile per te.

![immagine](assets/en/10.webp)

(2) Successivamente, deve essere impostata una valuta predefinita per il negozio, sia una valuta fiat sia denominata in uno standard Bitcoin / Sats. Per l'ambiente demo, la imposteremo in USD.

![immagine](assets/en/11.webp)

(3) Come ultimo parametro nella configurazione del negozio, BTCPay Server richiede di impostare una "Fonte di prezzo preferita" per confrontare il prezzo di Bitcoin con il prezzo fiat corrente in modo che il tuo negozio mostri il corretto tasso di cambio tra Bitcoin e la valuta fiat impostata per il negozio. Nell'esempio Demo, ci atteniamo all'impostazione predefinita e la impostiamo sull'exchange Kraken. BTCPay Server utilizza l'API di Kraken per controllare i tassi di cambio.

![immagine](assets/en/12.webp)

(4) Ora che questi parametri del negozio sono stati impostati, clicca sul pulsante Crea, e BTCPay Server creerà la dashboard del tuo primo negozio, dove la procedura guidata continuerà.

![immagine](assets/en/13.webp)

Congratulazioni, hai creato il tuo primo negozio, e questo conclude questo esercizio.

![immagine](assets/en/14.webp)

### Riepilogo delle competenze

In questa sezione, hai imparato:

- Creazione del negozio e configurazione di una valuta predefinita combinata con le preferenze della fonte di prezzo.
- Ogni "Negozio" è una nuova casa separata dagli altri negozi su questa installazione di BTCPay Server.

# Introduzione alla Sicurezza delle Chiavi Bitcoin

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Comprensione della Generazione delle Chiavi Bitcoin

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### Cosa comporta la generazione delle chiavi bitcoin?

Quando vengono creati, i portafogli Bitcoin generano un cosiddetto "seed". Nell'ultimo obiettivo, hai creato un "seed", Le serie di parole generate in precedenza sono note anche come frasi mnemoniche. Il seed è utilizzato per derivare le singole Chiavi Bitcoin da esso. Le frasi seed non dovrebbero mai essere condivise con terze parti o peer non fidati.
La generazione del seed avviene secondo lo standard industriale noto come framework "Hierarchical Deterministic" (HD).
![image](assets/en/15.webp)

### Indirizzi

BTCPay Server è stato costruito per generare un nuovo Indirizzo. Questo allevia il problema del riutilizzo dell'indirizzo pubblico o dell'Indirizzo. Usare la stessa chiave pubblica rende molto facile tracciare l'intera cronologia dei pagamenti. Pensare alle chiavi come a buoni monouso migliorerebbe significativamente la tua privacy. Usiamo anche gli Indirizzi Bitcoin, non confonderli con le chiavi pubbliche.

Un Indirizzo viene derivato dalla chiave pubblica attraverso un "algoritmo di hashing". La maggior parte dei portafogli e delle transazioni, tuttavia, mostrerà gli Indirizzi piuttosto che quelle chiavi pubbliche. Gli Indirizzi sono, in generale, più corti delle chiavi pubbliche e di solito iniziano con `1`, `3`, o `bc1`, mentre le chiavi pubbliche iniziano con `02`, `03`, o `04`.

- Gli indirizzi che iniziano con `1.....` sono ancora indirizzi molto comuni. Come menzionato nel capitolo Creazione di un nuovo negozio, questi sono indirizzi legacy. Questo tipo di indirizzo è destinato alle transazioni P2PKH. P2Pkh utilizza la codifica Base58, che rende l'indirizzo sensibile al maiuscolo/minuscolo. La sua struttura si basa sulla chiave pubblica con un ulteriore cifra come identificatore.

- Gli indirizzi che iniziano con `bc1...` stanno lentamente diventando indirizzi molto comuni. Sono noti come indirizzi SegWit (nativi). Offrono una struttura di commissioni migliore rispetto agli altri indirizzi menzionati. Gli indirizzi SegWit nativi utilizzano la codifica Bech32 e consentono solo lettere minuscole.

- Gli indirizzi che iniziano con `3...` sono comunemente ancora utilizzati dagli exchange per gli indirizzi di deposito. Questi indirizzi sono menzionati nel capitolo Creazione di un nuovo negozio, indirizzi SegWit avvolti o nidificati. Tuttavia, potrebbero anche funzionare come "Indirizzo Multisig". Quando utilizzati come indirizzo SegWit, si risparmia nuovamente sulle commissioni di transazione, anche se meno rispetto a SegWit nativo. Gli indirizzi P2SH utilizzano la codifica Base58. Ciò li rende sensibili al maiuscolo/minuscolo, come l'indirizzo legacy.

- Gli indirizzi che iniziano con `2...` sono indirizzi Testnet. Sono destinati a ricevere bitcoin testnet (tBTC). Non dovresti mai confonderli e inviare Bitcoin a questi indirizzi. Per scopi di sviluppo, puoi generare un portafoglio testnet. Ci sono molteplici faucet online per ottenere Bitcoin testnet. Non acquistare mai Bitcoin testnet. I Bitcoin testnet sono minati. Questo potrebbe essere un motivo per uno sviluppatore di utilizzare Regtest invece. Si tratta di un ambiente di gioco per sviluppatori, privo di alcuni componenti di rete. Bitcoin è, tuttavia, molto utile per scopi di sviluppo.

### Chiavi Pubbliche

Le chiavi pubbliche sono meno utilizzate nella pratica oggi. Nel tempo, gli utenti di bitcoin le hanno sostituite con gli Indirizzi. Esistono ancora e vengono ancora utilizzate occasionalmente. Le chiavi pubbliche sono, in generale, stringhe molto più lunghe degli indirizzi. Come con gli indirizzi, iniziano con un identificatore specifico.

- Prima di tutto, `02...` e `03...` sono identificatori di chiavi pubbliche molto standard codificati in formato SEC. Questi possono essere elaborati e trasformati in indirizzi per ricevere, utilizzati per creare indirizzi multi-sig o per verificare una firma. Le transazioni Bitcoin dei primi giorni utilizzavano chiavi pubbliche come parte delle transazioni P2PK.

- Tuttavia, i portafogli HD utilizzano una struttura diversa. `xpub...`, `ypub...` o `zpub...` sono chiamate chiavi pubbliche estese, meglio note come xpubs. Queste chiavi vengono utilizzate per derivare molte chiavi pubbliche poiché fanno parte del portafoglio HD. Poiché la tuo xpub contiene la cronologia di tutte le transazioni, passate e future, non condividerla mai con parti non fidate.

### Riepilogo delle Competenze

In questa sezione, hai imparato quanto segue:

- Le differenze tra indirizzi e tipi di dati di chiavi pubbliche e i vantaggi dell'uso degli indirizzi rispetto alle chiavi pubbliche.

### Valutazione della conoscenza

Descrivere il vantaggio dell'utilizzo di indirizzi nuovi per ogni transazione rispetto al riutilizzo degli indirizzi o ai metodi basati su chiavi pubbliche

## Proteggere le chiavi con un portafoglio hardware

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Conservazione delle Chiavi Bitcoin

Il seed, l'elenco di 12 - 24 parole generato, richiede backup adeguati e sicurezza, poiché queste parole sono l'unico modo per recuperare l'accesso a un portafoglio. La Tutti i tuoi indirizzi creati verranno salvati usando questa unica lista di parole mnemoniche che rappresentano la tua frase seed o frase di recupero.

Mantieni la tua frase di recupero al sicuro. Se accessibile da qualcuno, specificamente con intenti malevoli, possono spostare i tuoi fondi. Mantenere il seed sicuro e protetto ma anche ricordarlo è reciproco. Ci sono diversi metodi per conservare le chiavi private Bitcoin, ognuno con vantaggi e svantaggi, sia in termini di sicurezza, privacy, comodità o mezzi fisici. Data l'importanza delle chiavi private, gli utenti Bitcoin tendono a conservare e mantenere al sicuro queste chiavi in "autocustodia" piuttosto che usare servizi "custodial" come le banche. A seconda dell'utente e delle esigenze è possibile utilizzare o una soluzione di Cold storage oppure un Hot wallet.

### Conservazione Hot e Cold delle chiavi Bitcoin

Di solito, i portafogli Bitcoin sono denominati in Hot Wallet o Cold Wallet. La maggior parte dei compromessi si trova nella comodità, facilità d'uso e rischi per la sicurezza. Ognuno di questi metodi può anche essere visto come una soluzione custodial. Tuttavia, i compromessi qui sono per lo più basati su sicurezza e privacy e vanno oltre l'ambito di questo corso.

### Hot wallet

Gli Hot wallet sono il modo più comodo di interagire con Bitcoin tramite mobile, web o software desktop. Il portafoglio è sempre connesso a Internet, permettendo agli utenti di inviare o ricevere Bitcoin. Questo, tuttavia, è anche la sua debolezza, il portafoglio, essendo sempre online, è ora più vulnerabile agli attacchi di hacker o malware sul tuo dispositivo. In BTCPay Server, gli hot wallet conservano le chiavi private sull'istanza. Chiunque acceda al tuo negozio BTCPay Server potrebbe rubare fondi da questo indirizzo se malintenzionato. Quando BTCPay Server è eseguito in un ambiente ospitato, dovresti sempre considerare questo nel tuo profilo di sicurezza e preferibilmente non usare un Hot-wallet in tal caso. Quando BTCPay Server è installato su hardware di proprietà, protetto e fidato da te, il profilo di rischio si abbassa significativamente, ma non scompare mai!

### Cold Wallet

Le persone spostano i loro Bitcoin in un cold wallet perché può isolare le chiavi private da Internet. Rimuovere la connessione internet dall'equazione riduce il rischio di malware, spyware e SIM swap. Si ritiene che la conservazione a freddo sia superiore alla conservazione a caldo per sicurezza e autonomia, purché vengano prese precauzioni adeguate per evitare la perdita delle chiavi private Bitcoin. La conservazione a freddo è più adatta per grandi quantità di Bitcoin, che non sono destinate a essere spese spesso a causa della complessità dell'installazione del portafoglio.

Ci sono vari metodi su come conservare le chiavi Bitcoin in cold storage, da portafogli di carta a portafogli cerebrali, portafogli hardware o, fin dall'inizio, un file del portafoglio. La maggior parte dei portafogli utilizza BIP 39 per generare il seed. Tuttavia, all'interno del software Bitcoin core, non è ancora stato raggiunto un consenso sull'uso di esso. Il software Bitcoin Core genererà comunque un file Wallet.dat che devi conservare in una posizione sicura offline.

### Riepilogo delle Competenze

In questa sezione, hai imparato:

- Le differenze tra hot e cold wallet in termini di funzionalità e i loro compromessi.

### Valutazione della conoscenza Revisione Concettuale

- Cos'è un portafoglio?
- Qual è la differenza tra portafogli caldi e freddi?

- Descrivi cosa si intende per "generare un portafoglio"?

## Utilizzando le tue chiavi Bitcoin

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### Portafoglio BTCPay Server

BTCPay Server comprende le seguenti funzionalità standard del portafoglio:

- Transazioni
- Invia
- Ricevi
- Rescan
- Pagamenti Pull
- Pagamenti
- PSBT
- Impostazioni generali

### Transazioni

Gli amministratori possono vedere le transazioni in entrata e in uscita per il portafoglio on-chain collegato a questo specifico negozio nella vista delle transazioni. Ogni transazione ha una distinzione tra ricevute e inviate. Le transazioni ricevute saranno verdi e le transazioni in uscita saranno rosse. All'interno della vista delle transazioni di BTCPay Server, gli amministratori vedranno anche un insieme di etichette standard.

| Tipo di Transazione | Descrizione                                                        |
| ------------------- | ------------------------------------------------------------------ |
| App                 | Il pagamento è stato ricevuto tramite una fattura creata dall'app  |
| invoice             | Il pagamento è stato ricevuto tramite una fattura                  |
| payjoin             | Non pagato, il timer della fattura non è ancora scaduto            |
| payjoin-exposed     | UTXO è stato esposto tramite una proposta di payjoin della fattura |
| payment-request     | Il pagamento è stato ricevuto tramite una richiesta di pagamento   |
| payout              | Il pagamento è stato inviato tramite un pagamento o un rimborso    |

### Come Inviare

La funzione di invio del server BTCPay invia transazioni dal tuo portafoglio on-chain BTCPay Server. BTCPay Server consente di firmare le tue transazioni per spendere fondi in più modi . Una transazione può essere firmata con;

- Portafoglio Hardware
- Portafogli che supportano PSBT
- Chiave privata HD o seed di recupero.
- Portafoglio Caldo

#### Portafoglio hardware

BTCPay Server ha un supporto integrato per portafoglio hardware che ti consente di utilizzare il tuo portafoglio hardware con BTCPay Vault senza divulgare informazioni a app o server di terze parti. L'integrazione del portafoglio hardware all'interno di BTCPay Server ti consente di importare il tuo portafoglio hardware e spendere i fondi in entrata con una semplice conferma sul tuo dispositivo. Le tue chiavi private non lasciano mai il dispositivo, e tutti i fondi vengono validati contro il tuo nodo completo, quindi non c'è perdita di dati.

#### Firmando con un portafoglio che supporta PSBT

PSBT (Partially Signed Bitcoin transactions) è un formato di interscambio per transazioni Bitcoin che devono ancora essere completamente firmate. PSBT è supportato in BTCPay Server e può essere firmato con portafogli hardware e software compatibili.

La costruzione di una transazione Bitcoin firmata completamente prevede i seguenti passaggi:

- Viene costruita una PSBT con input e output specifici ma senza firme
- La PSBT esportata può essere importatasu un portafoglio che supporta questo formato
- I dati della transazione possono essere ispezionati e firmati utilizzando il portafoglio
- Il file PSBT firmato viene esportato dal portafoglio e importato su BTCPay Server
- BTCPay Server produce la transazione Bitcoin finale
- Verifichi il risultato e lo trasmetti alla rete

#### Firmando con chiave privata HD o seed
Se hai creato un portafoglio in precedenza utilizzando BTCPay Server, puoi spendere i fondi inserendo la tua chiave privata in un campo appropriato. Imposta un "AccountKeyPath" appropriato in impostazioni del portafoglio; altrimenti, non puoi spendere.

#### Firmando con un portafoglio caldo

Se hai creato un nuovo portafoglio durante la configurazione del tuo negozio e lo hai abilitato come un portafoglio caldo, utilizzerà automaticamente il seed memorizzato su un server per firmare.

### RBF (Replace-By-Fee)

Replace-By-Fee (RBF) è una funzionalità del protocollo Bitcoin che consente di sostituire una transazione precedentemente trasmessa (se non confermata). Questo permette di randomizzare l'impronta della transazione del tuo portafoglio o di sostituirla con una tariffa più alta per spostare la transazione più in alto nella coda di priorità di conferma (mining). Questo sostituirà efficacemente la transazione originale poiché la tariffa più alta sarà prioritaria e, una volta confermata, invaliderà quella originale (senza doppia spesa).
Premi il pulsante "Impostazioni Avanzate" per visualizzare le opzioni RBF;

![immagine](assets/en/16.webp)

- Randomizza per maggiore privacy, consente alla transazione di essere sostituita automaticamente per la randomizzazione dell'impronta della transazione.
- Sì, contrassegna la transazione per RBF e può essere esplicitamente sostituita (Non sostituita di default, solo su input)
- No, non permettere che la transazione sia sostituita.

### Selezione Moneta

La selezione moneta è una funzionalità avanzata che aumenta la privacy e consente di selezionare gli utxo che si desidera spendere quando si crea una transazione. Ad esempio, pagare con utxo freschi di conjoin.

La selezione moneta funziona nativamente con la funzionalità di etichettatura del portafoglio. Questo ti consente di etichettare i fondi in entrata per una gestione e spesa UTXO più fluida.

BTCpay Server supporta anche BIP-329 per la gestione delle etichette. BIP-329 consente di applicare etichette; se trasferisci da un portafoglio che supporta questo particolare BIP e imposti etichette, BTCPay Server le riconoscerà e le importerà. Quando si migrano server, queste informazioni possono anche essere esportate e importate nel nuovo ambiente.

### Come Ricevere

Quando si fa clic sul pulsante di ricezione in BTCPay Server, viene generato un indirizzo inutilizzato per ricevere pagamenti. Gli amministratori possono anche generare un nuovo indirizzo generando una nuova "Fattura".

BTCPay Server chiederà sempre di generare l'indirizzo BTC disponibile successivo per evitare il riutilizzo degli indirizzi. Dopo aver cliccato su "Genera il prossimo indirizzo BTC disponibile", BTCPay Server ha generato un nuovo indirizzo e QR. Consente anche di impostare direttamente un'Etichetta all'indirizzo per una migliore gestione dei tuoi indirizzi.

![immagine](assets/en/17.webp)

![immagine](assets/en/18.webp)

#### Ri-scansione

La funzionalità di Ri-scansione si basa su "Scantxoutset" di Bitcoin Core 0.17.0 per scandire lo stato attuale della blockchain (chiamato Set UTXO) alla ricerca di monete appartenenti allo schema di derivazione configurato. La ri-scansione del portafoglio risolve due problemi che gli utenti di BTCPay Server sperimentano.

1. Problema del limite di gap - La maggior parte dei portafogli di terze parti sono portafogli leggeri che condividono un nodo tra molti utenti. I portafogli che dipendono da nodi leggeri e completi limitano la quantità (tipicamente 20) di indirizzi senza saldo che tengono traccia sulla blockchain per evitare problemi di prestazioni. BTCPay Server genera un nuovo indirizzo per ogni fattura. Tenendo presente quanto sopra, dopo che BTCPay Server genera 20 fatture consecutive non pagate, il portafoglio esterno smette di recuperare le transazioni, assumendo che non si siano verificate nuove transazioni. Il tuo portafoglio esterno non le mostrerà una volta che le fatture vengono pagate sulla 21ª, 22ª, ecc. D'altra parte, internamente, il portafoglio BTCPay Server tiene traccia di qualsiasi indirizzo che genera insieme a un limite -gap- molto più grande. Non si affida a terzi e può sempre mostrare il saldo corretto.
2. La soluzione del limite di gap - Se il tuo [portafoglio esterno/esistente](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) consente la configurazione del limite di gap, la soluzione più semplice è aumentarlo. Tuttavia, la maggior parte dei portafogli non permette questa configurazione. Gli unici portafogli che conosciamo e che permettono la configurazione del limite di gap sono Electrum, Wasabi e Sparrow Wallet. Sfortunatamente, è probabile che tu incontri problemi con molti altri portafogli. Per la migliore esperienza utente e privacy, considera di abbandonare i portafogli esterni e di utilizzare il portafoglio interno di BTCPay Server.

#### BTCPay Server utilizza "mempoolfullrbf=1"

BTCPay Server utilizza "mempoolfullrbf=1"; abbiamo aggiunto questo come impostazione predefinita nel tuo setup di BTCPay Server. Tuttavia, è sempre possibile disabilitarlo manualmente. Senza "mempoolfullrbf=1", se un cliente effettua un doppio pagamento con una transazione che non segnala RBF, il commerciante lo saprebbe solo dopo la conferma.

Un amministratore potrebbe voler escludere questa impostazione. Con la seguente stringa, puoi cambiare l'impostazione predefinita.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### Impostazioni del portafoglio BTCPay Server

Le impostazioni del portafoglio all'interno di BTCPay Server offrono una panoramica chiara e veloce delle impostazioni generali del tuo portafoglio. Tutte queste impostazioni sono precompilate se il portafoglio è stato creato con BTCPay Server.

![immagine](assets/en/19.webp)

Le impostazioni del portafoglio all'interno di BTCPay Server offrono una panoramica chiara e veloce delle impostazioni generali del tuo portafoglio. Tutte queste impostazioni sono precompilate se il portafoglio è stato creato con BTCPay Server. Le impostazioni del portafoglio di BTCPay Server iniziano con lo stato del portafoglio. È un portafoglio solo visualizzazione o un portafoglio attivo? A seconda del tipo di portafoglio, le azioni possono variare dalla riesecuzione della scansione del portafoglio per le transazioni mancanti, dalla pulizia delle vecchie transazioni dalla cronologia, dalla registrazione del portafoglio per i link di pagamento, o dalla sostituzione e cancellazione del portafoglio corrente associato al negozio. Nelle impostazioni del portafoglio di BTCPay Server, gli amministratori possono impostare un'etichetta per il portafoglio per una migliore gestione. Qui l'amministratore sarà anche in grado di vedere lo Schema di Derivazione, la chiave dell'account (xpub), l'Impronta digitale e il Percorso chiave. Le impostazioni dei pagamenti nel portafoglio hanno solo 2 impostazioni principali. Il pagamento è invalido se la transazione non viene confermata entro (minuti impostati) dopo la scadenza della fattura. Considera la fattura confermata quando la transazione di pagamento ha X numero di conferme. Gli amministratori possono anche impostare un interruttore per mostrare le commissioni consigliate ai pagamenti o impostare un obiettivo di conferma manuale nel numero di blocchi.

![immagine](assets/en/20.webp)

**!Nota!**

Se segui questo corso da solo, creare questo account potrebbe essere qualcosa che potresti fare su un host di terze parti, quindi ancora una volta menzioniamo di non utilizzare questi come ambienti di produzione, ma solo a scopo di formazione.

### Esempio

#### Configurare un portafoglio Bitcoin in BTCPay Server

BTCPay Serverdu configurare un portafoglio in due modi. Il primo è importare un portafoglio Bitcoin già esistente. L'importazione può essere fatta collegando un portafoglio hardware, importando un file del portafoglio, inserendo una chiave pubblica estesa, scansionando il codice QR di un portafoglio, o, meno consigliato, inserendo a mano un seed di recupero del portafoglio precedentemente creato. In BTCPay Server, è anche possibile creare un nuovo portafoglio. Ci sono due modi possibili per configurare BTCPay Server quando si genera un nuovo portafoglio.
L'opzione di portafoglio caldo (hot wallet) in BTCPay Server consente funzionalità come 'Payjoin' o 'Liquid'. Tuttavia, c'è uno svantaggio: il seed di recupero generato per questo portafoglio sarà memorizzato sul server, dove chiunque abbia il controllo da Amministratore potrebbe recuperare il seed di recupero. Poiché la tua chiave privata deriva dal tuo seed di recupero, un attore malevolo potrebbe ottenere accesso ai tuoi fondi attuali e futuri!
Per mitigare tale rischio in BTCPay Server, un Amministratore può impostare in Impostazioni Server > Politiche > "Consenti ai non-amministratori di creare portafogli caldi per i loro negozi" su no, come è per impostazione predefinita. Per migliorare la sicurezza di questi portafogli caldi, l'amministratore del server dovrebbe abilitare l'autenticazione 2FA sugli account autorizzati ad avere portafogli caldi. Conservare le chiavi private su un server pubblico è pericoloso e comporta dei rischi. Alcuni sono simili ai rischi della Rete Lightning (vedi il capitolo successivo per i rischi della Rete Lightning).

La seconda opzione che BTCPay Server offre per generare un nuovo portafoglio è creando un portafoglio Solo-Visualizzazione (Watch-Only wallet). BTCPay Server genererà le tue chiavi private una sola volta. Dopo che l'utente conferma di aver annotato il proprio Seed, BTCPay Server cancellerà le chiavi private dal server. Di conseguenza, il tuo negozio ora ha un portafoglio Solo-Visualizzazione collegato ad esso. Per spendere i fondi ricevuti sul tuo portafoglio Solo-Visualizzazione, vedi il capitolo Come Inviare, sia utilizzando BTCPay Server Vault, PSBT (transazione bitcoin parzialmente firmata), o, meno raccomandato, inserendo manualmente il tuo seed.

Hai creato un nuovo 'Negozio' nell'ultima parte. La procedura guidata di installazione continuerà chiedendo di "Impostare un portafoglio" o "Impostare un nodo Lightning". In questo esempio, seguirai la procedura guidata "Impostare un portafoglio" (1).

![immagine](assets/en/21.webp)

Dopo aver cliccato su "Impostare un portafoglio", la procedura guidata continuerà chiedendo come vuoi procedere; BTCPay Server ora offre l'opzione di collegare un portafoglio Bitcoin esistente al tuo nuovo negozio. Se non hai un portafoglio, BTCPay Server propone di crearne uno nuovo. Questo esempio seguirà i passaggi per "creare un nuovo portafoglio" (2). Segui i passaggi per imparare come "Collegare un portafoglio esistente (1).

![immagine](assets/en/22.webp)

**!Nota!**

Se segui questo corso in aula, l'esempio attuale e il seed che abbiamo generato sono solo a scopo didattico. Non dovrebbe mai esserci alcuna somma sostanziale, se non quella richiesta durante gli esercizi, su questi indirizzi.

(1) Continua la procedura guidata del "Nuovo portafoglio" cliccando sul pulsante "Crea un nuovo portafoglio".

![immagine](assets/en/23.webp)

(2) Dopo aver cliccato su “Crea un nuovo portafoglio”, la finestra successiva della procedura guidata darà le opzioni “Portafoglio caldo” e “Portafoglio Solo-Visualizzazione”. Se segui insieme a un istruttore, il tuo ambiente è una Demo condivisa, e puoi solo creare un Portafoglio Solo-Visualizzazione. Nota la differenza tra le due figure qui sotto. Poiché sei nell'ambiente Demo seguendo insieme all'istruttore, crea un "Portafoglio Solo-Visualizzazione" e continua con la procedura guidata del "Nuovo Portafoglio".

![immagine](assets/en/24.webp)

![immagine](assets/en/25.webp)

(3) Continuando la procedura guidata del nuovo portafoglio, ora ti trovi nella sezione Crea portafoglio BTC Solo-Visualizzazione. Qui abbiamo la possibilità di impostare il tipo di indirizzo del portafoglio "Tipo di indirizzo". BTCPay Server consente di scegliere il tipo di indirizzo preferito; al momento della scrittura di questo corso, è ancora consigliato utilizzare gli indirizzi bech32. Scopri più dettagli sugli indirizzi nel primo capitolo di questa parte.

- Segwit (bech32)
- Gli indirizzi Native SegWit iniziano con `bc1q`.
  - Esempio: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Gli indirizzi Legacy iniziano con il numero `1`.
  - Esempio: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (Per utenti avanzati)
  - Gli indirizzi Taproot iniziano con `bc1p`.
  - Esempio: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- Segwit wrapped
  - Gli indirizzi Segwit wrapped iniziano con `3`.
  - Esempio: `37BBXXXXXXXXXXXXXXX`

Scegli segwit (raccomandato) come tipo di indirizzo del portafoglio preferito.

![immagine](assets/en/26.webp)

(4) Quando si imposta il parametro per il Wallet, BTCPay Server consente agli utenti di impostare una passphrase opzionale tramite BIP39, assicurati di confermare la tua password.

![immagine](assets/en/27.webp)

(5) Dopo aver impostato il tipo di indirizzo del Wallet e, eventualmente, alcune opzioni avanzate, clicca su Crea, e BTCPay Server genererà il tuo nuovo Wallet. Nota che questo è l'ultimo passo prima di generare il seed. Assicurati di fare ciò in un ambiente in cui nessuno possa rubare il seed guardando il tuo schermo.

![immagine](assets/en/28.webp)

(6) Nella schermata successiva della procedura guidata, BTCPay Server ti mostra il seed per il tuo Wallet appena generato; queste sono le chiavi per recuperare il tuo Wallet e firmare le transazioni. BTCPay Server genera un seed di 12 parole. Queste parole verranno cancellate dal server dopo questa schermata di configurazione. Questo Wallet è specificamente un portafoglio di visualizzazione. Si consiglia di non memorizzare questa il seed digitalmente o tramite immagine fotografica. Gli utenti possono proseguire solo se riconoscono attivamente di aver annotato il loro seed.

![immagine](assets/en/29.webp)

(7) Dopo aver cliccato su Fatto e aver assicurato il seed, BTCPay Server aggiornerà il tuo negozio con il nuovo Wallet allegato ed è pronto a ricevere pagamenti. Nell'interfaccia utente, nel menu di navigazione a sinistra, nota come Bitcoin sia ora evidenziato e attivato sotto Wallet.

![immagine](assets/en/30.webp)

### Esempio: Annotare un seed

Questo è un metodo molto sicuro di usare Bitcoin. Come detto prima, solo tu dovresti avere accesso o conoscenza del tuo seed.  Questo dovrebbe essere utilizzato eslusicamente per questo corso. Troppi fattori, occhi indiscreti dei compagni di classe, sistemi non sicuri e molti altri rendono queste chiavi solo educative e non affidabili. Tuttavia, le chiavi generate devono comunque essere conservate per i successivi esempi del corso.

Il primo metodo che utilizzeremo nella situazione attuale, anche il meno sicuro, è annotare la frase seme nell'ordine corretto. Una cartoncino per annotare il seed viene forntiro nel materiale del corso allo studente o, in alternativa è disponibile su gitHub di BTCPay Server. Utilizzeremo questa carta per annotare le parole generate nel passaggio precedente. Assicurati di scriverle nell'ordine corretto. Dopo averle scritte, controllale rispetto a quanto fornito dal software per assicurarti di averle scritte nell'ordine corretto. Una volta scritte, clicca sulla casella che indica di aver annotato correttamente il tuo seed.

### Esempio: Conservare il seed su un Hardware Wallet

In questo corso, analizziamo come conservare il seed su un hardware wallet. L'istruttore del corso potrebbe non avere un dispositivo hardware. Nella guida del corso, però, sono elencati i portafogli hardware che si adatterebbero a questo esercizio.
In questo esempio useremo BTCPay Server Vault e il portafoglio hardware Blockstream Jade.
Puoi anche seguire un video di riferimento per collegare un portafoglio hardware.
![BTCPay Server - Come collegare il tuo portafoglio hardware con BTCPay Vault.](https://youtu.be/s4qbGxef43A)

Scarica BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Assicurati di scaricare i file corretti per il tuo sistema. Gli utenti Windows dovrebbero scaricare il pacchetto [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), gli utenti Mac scaricano [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), e gli utenti Linux dovrebbero scaricare [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

Dopo aver installato BTCPay Server Vault, avvia il software facendo clic sull'icona sul tuo Desktop. Quando BTCPay Server Vault è correttamente installato e avviato per la prima volta, chiederà il permesso di essere utilizzato con le applicazioni Web. Richiederà inoltre l'accesso allo specifico BTCPay Server con cui lavori. Accetta queste condizioni. BTCPay Server Vault ora cercherà il dispositivo Hardware. Una volta trovato, BTCPay Server riconoscerà che Vault è in esecuzione e ha recuperato il tuo dispositivo.

**!Nota!**

Non dare le tue chiavi SSH o l'account amministratore del server a nessun altro tranne che agli amministratori quando utilizzi un portafoglio caldo. Chiunque abbia accesso a questi account avrà accesso ai fondi nel Hot Wallet.

### Riepilogo delle Competenze

In questa sezione, hai appreso quanto segue:

- La vista delle transazioni del portafoglio Bitcoin e le sue varie categorizzazioni.
- Le varie opzioni quando si invia da un portafoglio Bitcoin, dai portafogli hardware ai portafogli caldi.
- Il problema del limite di gap affrontato quando si utilizzano la maggior parte dei portafogli e come correggerlo.
- Come generare un nuovo portafoglio Bitcoin all'interno di BTCPay Server, inclusa la memorizzazione delle chiavi in un portafoglio hardware e il backup della frase di recupero.

In questa sezione, hai imparato come generare un nuovo portafoglio Bitcoin all'interno di BTCPay Server. Non abbiamo ancora affrontato come assicurare o utilizzare quelle chiavi. In una rapida panoramica di questo obiettivo, hai imparato come configurare il primo negozio. Hai imparato come generare una frase di recupero Bitcoin.

### Valutazione della Conoscenza Revisione Pratica

Descrivi un metodo per generare chiavi e uno schema per assicurarle, insieme ai compromessi/rischi dello schema di sicurezza.

## BTCPay Server Lightning Wallet

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Quando un amministratore del server provvede a configurare una nuova istanza di BTCPay Server, può impostare un'implementazione della rete Lightning, LND, Core Lightning o Eclair; vedi Parte Configurazione di BTCPay Server per istruzioni di installazione più dettagliate.
Collegare un nodo Lightning al proprio BTCPay Server funziona tramite un nodo personalizzato. Un utente che non è un amministratore del server su BTCPay Server non sarà in grado di utilizzare il nodo Lightning interno per impostazione predefinita. Ciò serve a proteggere il proprietario del server dalla perdita dei suoi fondi. Gli amministratori del server possono installare un Plugin per dare accesso al loro nodo Lightning tramite LNBank; ciò è al di fuori dell'ambito di questo corso; per maggiori informazioni su LNBank, consultare la pagina ufficiale del plugin.

### Collegare il nodo interno (amministratore del server)

L'amministratore del server può utilizzare il nodo Lightning interno di BTCPay Server. Indipendentemente dall'implementazione di Lightning, il collegamento al nodo Lightning interno è lo stesso.

Andare in un negozio configurato in precedenza e cliccare sul portafoglio "Lightning" nel menu a sinistra. BTCPay Server offre due possibilità di configurazione, utilizzando il nodo interno (solo amministratore del server per impostazione predefinita) o un nodo personalizzato (collegamento esterno). Gli amministratori del server possono cliccare sull'opzione "Usa nodo interno". Non è richiesta ulteriore configurazione. Cliccare sul pulsante "salva"  e controllare la notifica che indica "Nodo Lightning BTC aggiornato". Il negozio ha ora ottenuto con successo le capacità alla rete Lightning.

### Collegare il nodo esterno (utente del server/proprietario del negozio)

Ai proprietari dei negozi non è in genere permesso utilizzare il nodo Lightning dell'amministratore del server per impostazione predefinita. È necessario effettuare il collegamento a un nodo esterno, sia un nodo del proprietario del negozio prima della configurazione di BTCPay Server, un plugin LNBank se reso disponibile dall'amministratore del server, o una soluzione di custodia come Alby.

Andare in un negozio configurato in precedenza e cliccare su "Lightning" sotto i portafogli nel menu a sinistra. Poiché ai proprietari dei negozi non è permesso utilizzare il nodo interno per impostazione predefinita, questa opzione è disabilitata. Utilizzare un nodo personalizzato è l'unica opzione disponibile.

BTCPay Server richiede informazioni di connessione; le soluzioni precedenti (o di custodia) forniranno queste informazioni specifiche per implementare Lightning. All'interno di BTCPay Server, i proprietari dei negozi possono utilizzare le seguenti connessioni:

- C-lightning tramite connessione TCP o Unix domain socket.
- Lightning Charge tramite HTTPS
- Eclair tramite HTTPS
- LND tramite il proxy REST
- LNDhub tramite l'API REST

![immagine](assets/en/31.webp)

Cliccare su "testa connessione" per assicurarsi di aver inserito correttamente i dettagli della connessione. Dopo che la connessione risulta essere buona, cliccare su salva, e BTCPay Server mostra che il negozio è aggiornato con un Nodo Lightning.

### Gestione del nodo Lightning interno LND (Amministratore del server)

Dopo aver collegato il nodo Lightning interno, gli amministratori del server noteranno nuove tessere sulla Dashboard specificamente per le informazioni Lightning.

- Saldo Lightning
- BTC nei canali
  - BTC nei canali in apertura
  - BTC saldo locale
  - BTC saldo remoto
  - BTC nei canali in chiusura
- BTC On-chain
  - BTC confermati
  - BTC non confermati
  - BTC riservati
- Servizi Lightning
  - Ride the Lightning (RTL).

Cliccando sia sul logo di Ride the Lightning nella tessera "Servizi Lightning" sia su "Lightning" sotto i portafogli nel menu a sinistra, gli amministratori del server possono accedere a RTL per la gestione del nodo Lightning.

**Nota!**

Se il collegamento al nodo Lightning interno fallisce - Se la connessione interna fallisce, confermare:

1. Che il nodo Bitcoin on-chain sia completamente sincronizzato
2. Che il nodo Lightning interno sia "Abilitato" in "Lightning" > "Impostazioni" > "Impostazioni Lightning BTC"
   Se non riesci a connetterti al tuo nodo Lightning, prova a riavviare il server o leggi maggiori dettagli sulla documentazione ufficiale di BTCPay Server; https://docs.btcpayserver.org/Troubleshooting/ . Non potrai accettare pagamenti Lightning nel tuo negozio fino a quando il tuo nodo Lightning non risulterà "Online". Prova a testare la tua connessione Lightning cliccando sul link "Informazioni Nodo Pubblico".

### Portafoglio Lightning

Nell'opzione Portafoglio Lightning presente nella barra del menu a sinistra, gli amministratori del server troveranno un facile accesso a RTL, alle loro Informazioni Nodo Pubblico e alle impostazioni Lightning specifiche per il loro negozio BTCPay Server.

#### Informazioni nodo interno

Gli amministratori del server possono cliccare sulle informazioni del nodo interno e dare un'occhiata allo stato del loro server (Online/Offline) e alla stringa di connessione per Clearnet o Tor.

![immagine](assets/en/32.webp)

#### Cambiare connessione

 Accanto alle informazioni del Nodo Pubblico del negozio, i proprietari possono trovare questa opzione. Ciò porterà alla configurazione iniziale per la connessione del nodo lightning esterno, compilare le nuove informazioni del nodo Lightning, cliccare su salva e aggiornare il negozio con le nuove informazioni del nodo.

![immagine](assets/en/33.webp)

#### Servizi

Se l'amministratore del server decide di installare più servizi per l'implementazione Lightning, questi saranno elencati qui. Con un'implementazione LND standard, gli amministratori avranno Ride The Lightning (RTL) come strumento standard per la gestione del nodo.

#### Impostazioni portafoglio BTC Lightning

Dopo aver aggiunto il nodo Lightning al negozio in una fase precedente, all'interno delle impostazioni del portafoglio Lightning, i proprietari del negozio possono ancora scegliere di disattivarlo per il loro negozio utilizzando l'interruttore in alto nelle impostazioni Lightning.

![immagine](assets/en/34.webp)

#### Opzioni di pagamento Lightning

I proprietari dei negozi possono impostare parametri per migliorare l'esperienza Lightning per i loro clienti.

- Mostrare gli importi dei pagamenti Lightning in Satoshi.
- Aggiungere suggerimenti di hop per canali privati alla fattura Lightning.
- Unificare URL/QR code di pagamento on-chain e Lightning al checkout.
- Impostare un modello di descrizione per le fatture Lightning.

#### LNURL

I proprietari dei negozi possono scegliere di utilizzare o meno LNURL. Un URL della Rete Lightning, o LNURL, è uno standard proposto per le interazioni tra colui che paga ed il beneficiario. In breve, un LNURL è un URL codificato bech32 prefissato con lnurl. Si prevede che il portafoglio Lightning decodifichi l'URL, contatti l'URL e attenda un file JSON con ulteriori istruzioni, in particolare un tag che definisce il comportamento dell'LNURL.

- Abilitare LNURL
- Modalità LNURL Classica
  - Per compatibilità del portafoglio, codificato Bech32 (classico) vs URL in chiaro (prossimo)
- Consentire al beneficiario di inserire un commento.

### Esempio 1

#### Connettersi a Lightning con il nodo interno (Amministratore)

Questa opzione è disponibile solo se sei l'Amministratore di questa istanza o se l'Amministratore ha modificato le impostazioni predefinite dove gli utenti possono utilizzare il nodo lightning interno.

Come amministratore, clicca su Portafoglio Lightning nella barra del menu a sinistra. BTCPay Server chiederà di utilizzare una delle due opzioni per connettere un Nodo Lightning, un nodo interno o un nodo esterno personalizzato. Clicca su Usa nodo interno e clicca su salva.

#### Gestire il tuo nodo Lightning (RTL)

Dopo essersi connessi al nodo lightning interno, BTCPay Server si aggiornerà e mostrerà una notifica "Nodo Lightning BTC aggiornato", confermando che ora hai collegato Lightning al tuo negozio.

Gestire il nodo lightning è un compito per l'Amministratore del server. Questo comporta:

- Gestire le transazioni
- Gestire la liquidità
  - Liquidità in entrata
  - Liquidità in uscita
- Gestire utenti (peer) e canali
  - Utenti (peer) connessi
  - Tariffe dei canali
  - Stato dei canali
- Effettuare backup frequenti dei stati del canale.
- Controllare i rapporti di routing.
- In alternativa, utilizzare servizi come Loop.

Tutta la gestione dei nodi Lightning viene effettuata da standard con RTL (assumendo che si utilizzi un'implementazione LND). Gli amministratori possono cliccare sul loro Lightning Wallet in BTCPay Server e trovare un pulsante per aprire RTL. La Dashboard principale di BTCPay Server è ora aggiornata con le caselle di Lightning Network, inclusi accessi rapidi a RTL.

### Esempio 2

#### Connettersi a Lightning con Alby

Quando ci si connette con ad una soluzione custodial come Alby, i proprietari di ciascun negozoi dovrebbero prima creare un account, visitando: https://getalby.com/

![immagine](assets/en/35.webp)

Dopo aver creato l'account Alby, vai al tuo negozio BTCPay Server.

Passo 1: Clicca su 'Imposta un nodo Lightning' sulla Dashboard o su 'Lightning' sotto portafogli.

![immagine](assets/en/36.webp)

Passo 2: Inserisci le credenziali di connessione del tuo portafoglio fornite da Alby. Nella Dashboard di Alby, clicca su Portafoglio. Qui troverai "Credenziali di Connessione del Portafoglio". Copia queste credenziali. Incolla le credenziali di Alby nel campo di configurazione della connessione in BTCPay Server.

![immagine](assets/en/37.webp)

Passo 3: Dopo aver fornito a BTCPay Server i dettagli della connessione, clicca sul pulsante "Testa Connessione" per assicurarti che la connessione funzioni correttamente. Nota il messaggio "Connessione al nodo Lightning riuscita" nella parte superiore dello schermo. Questo conferma che tutto funziona correttamente.

![immagine](assets/en/38.webp)

Passo 4: Clicca su salva, e il tuo negozio è ora connesso con un nodo Lightning tramite Alby.

![immagine](assets/en/39.webp)

**!Nota!**

Non affidare mai ad una soluzione Lightning custodital più di quanto sei disposto a perdere.

### Riassunto delle Competenze

In questa sezione hai imparato:

- Come connettere un nodo Lightning interno o esterno
- I contenuti e la funzione delle varie caselle relative a Lightning nella Dashboard
- Come configurare il portafoglio Lightning utilizzando Voltage Surge o Alby

### Valutazione della Conoscenza Revisione Pratica

Descrivi alcune delle varie opzioni per connettere un portafoglio Lightning al tuo negozio.

# Interfaccia BTCPay Server

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Panoramica della Dashboard

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server è un pacchetto software modulare. Tuttavia, ci sono standard che ogni istanza di BTCPay Server avrà e con cui interagiranno l'Amministratore/gli utenti. Iniziando dalla Dashboard. Il principale punto di ingresso di ogni BTCPay Server dopo aver effettuato l'accesso. La Dashboard offre una panoramica delle prestazioni del tuo negozio, del saldo attuale del portafoglio e delle ultime transazioni negli ultimi 7 giorni. Avendo una vista modulare, i Plugin possono utilizzare questa vista a loro vantaggio e creare le loro caselle sulla Dashboard. Per questa parte di corso, parleremo solo dei plugin/app standard e delle loro rispettive viste in tutto BTCPay Server.

### Caselle della Dashboard

All'interno della vista principale della dashboard di BTCPay Server ci sono alcune caselle standard disponibili. Queste caselle sono destinate al proprietario del negozio o all'Amministratore per gestire rapidamente il suo negozio in una panoramica.

- Saldo del portafogliolighti
- Attività delle transazioni
- Saldo Lightning (se Lightning è abilitato sul negozio)
- Servizi Lightning (se Lightning è abilitato sul negozio)
- Transazioni recenti.
- Fatture recenti
- Crowdfunding attivi correnti
- Prestazioni del negozio / articoli più venduti.
  La tessera Saldo Portafoglio offre una rapida panoramica dei fondi e delle prestazioni del tuo portafoglio. Può essere visualizzata sia in BTC che in valuta Fiat in un grafico settimanale, mensile o annuale.
  ![immagine](assets/en/40.webp)

### Attività delle transazioni

Accanto alla tessera Saldo Portafoglio, BTCPay Server mostra una rapida panoramica dei Pagamenti in sospeso, la quantità di Transazioni negli ultimi 7 giorni e se il tuo negozio ha emesso dei rimborsi. Cliccando sul pulsante Gestisci si accede alla gestione dei pagamenti in sospeso (per saperne di più sui pagamenti in BTCPay Server - capitolo Pagamenti).

![immagine](assets/en/41.webp)

### Saldo Lightning

Questo è visibile solo quando Lightning è attivato.

Quando l'Amministratore ha consentito l'accesso alla rete Lightning, la dashboard di BTCPay Server ora ha una nuova tessera con le informazioni del tuo nodo Lightning. Quanto BTC è nei canali, come questo è bilanciato localmente o in remoto (liquidità in entrata o in uscita), se i canali si stanno chiudendo o aprendo e quanto bitcoin è detenuto on-chain sul nodo lightning.

![immagine](assets/en/42.webp)

### Servizi Lightning

Questo è visibile solo quando lightning è attivo.

Oltre a vedere il tuo saldo Lightning sulla dashboard di BTCPay Server, gli amministratori vedranno anche la tessera per i Servizi Lightning. Qui gli amministratori possono trovare pulsanti rapidi per gli strumenti che usano per gestire il loro nodo Lightning; per esempio, Ride the Lightning è uno degli strumenti standard con BTCPay Server per la gestione del nodo Lightning.

![immagine](assets/en/43.webp)

### Transazioni recenti

La tessera delle transazioni recenti mostrerà le transazioni più recenti del tuo negozio. Con un clic, l'Amministratore dell'istanza di BTCPay Server può ora vedere l'ultima transazione e vedere se è necessaria attenzione verso di essa.

![immagine](assets/en/44.webp)

### Fatture recenti

La tessera delle fatture recenti mostra le 6 ultime fatture generate dal tuo BTCPay Server, incluse Stato e importo della fattura. La tessera include anche un pulsante "Visualizza tutto" per accedere facilmente alla panoramica completa delle fatture.

![immagine](assets/en/45.webp)

### Punto Vendita e Crowdfunding

Poiché BTCPay Server offre un insieme di plugin o app standard, Punto Vendita e Crowdfunding sono i due principali plugin di BTCPay Server. Con ogni negozio e portafoglio, un utente di BTCPay Server può generare quanti Punti Vendita o Crowdfunding desidera. Ognuno creerà una nuova tessera sulla dashboard mostrando le prestazioni dei plugin.

![immagine](assets/en/46.webp)

Nota la leggera differenza tra una tessera Punto Vendita e una tessera Crowdfunding. L'Amministratore vede gli articoli più venduti nella tessera Punto Vendita. Nella tessera Crowdfunding, questo diventa Perk principale. Entrambe le tessere hanno pulsanti rapidi per gestire la rispettiva app e visualizzare le fatture recenti create dagli articoli principali o dai perk principali.

![immagine](assets/en/47.webp)

**!?Nota!?**

I grafici del saldo e le transazioni recenti sono disponibili solo per un metodo di pagamento on-chain. Le informazioni sui saldi e le transazioni di Lightning Network sono in fase di elaborazione. A partire dalla Versione 1.6.0 di BTCPay Server, sono disponibili i saldi base di Lightning Network.

### Riepilogo delle competenze

In questa sezione, hai appreso quanto segue:

- La disposizione principale delle tessere sulla pagina principale è nota come Dashboard.
- Una comprensione di base dei contenuti di ogni tessera.

### Revisione della valutazione delle conoscenze

Elenca quante più tessere ricordi dalla Dashboard.

## BTCPay Server - Impostazioni del negozio

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>

All'interno del software BTCPay Server, conosciamo 2 tipi di impostazioni. Le impostazioni specifiche del BTCPay Server Store, trovate nel pulsante delle impostazioni nella barra del menu a sinistra sotto la Dashboard, e le impostazioni del BTCPay Server, trovate in fondo alla barra del menu, proprio sopra Account. Le impostazioni specifiche del BTCPay Server Server possono essere visualizzate solo dagli amministratori del server.
Le impostazioni del negozio si suddividono in molte schede per categorizzare ogni insieme di impostazioni.

- Generale
- Tariffe
- Aspetto del Checkout
- Token di Accesso
- Utenti
- Ruoli
- Webhook
- Processori di Pagamento
- Email
- Moduli

### Generale

Nella scheda delle Impostazioni Generali, i proprietari dei negozi impostano il loro branding e i predefiniti di pagamento. Durante la configurazione iniziale del negozio, è stato dato un nome al negozio; questo sarà ripreso nelle impostazioni Generali sotto Nome Negozio. Qui il proprietario del negozio può anche impostare il proprio sito web per abbinare il branding e un ID Negozio affinché l'Amministratore possa riconoscerlo nel database.

#### Branding

Poiché BTCPay Server è FOSS, un proprietario di negozio può personalizzare il branding per abbinarlo al suo negozio. Imposta il colore del brand, archivia i loghi del tuo brand e aggiungi CSS personalizzati per le pagine pubbliche/rivolte al cliente (Fatture, Richieste di Pagamento, Pagamenti Pull)

#### Pagamento

Nelle impostazioni dei pagamenti, i proprietari dei negozi impostano la valuta predefinita del loro negozio (sia in Bitcoin che in qualsiasi valuta fiat).

#### Permetti a chiunque di creare fatture

Questa impostazione è pensata per gli sviluppatori o coloro i quali implementano nuove funzionalità su BTCPay Server. Con questa impostazione attivata per il tuo negozio, il mondo esterno può creare fatture sulla tua istanza di BTCPay Server.

#### Aggiungi una tariffa aggiuntiva (tariffa di rete) alle fatture

Una funzionalità all'interno di BTCPay per proteggere i commercianti da attacchi di dust o clienti che generano un alto costo in commissioni. Ad esempio, il cliente ha creato una fattura per 20$ e l'ha pagata parzialmente, pagando 1$ 20 volte fino a quando la fattura è stata completamente pagata. Ora il commerciante ha una transazione più grande, aumentando il costo di mining nel caso in cui decida di spostare quei fondi più tardi. Per impostazione predefinita, BTCPay applica una commissione di rete aggiuntiva all'importo totale della fattura per coprire quella spesa per il commerciante quando la fattura viene pagata in più transazioni. BTCPay offre diverse opzioni per personalizzare questa funzionalità di protezione. Puoi applicare una tariffa di rete:

- Solo se il cliente effettua più di un pagamento per la fattura (Nell'esempio sopra, se il cliente ha creato una fattura per 20\$ e ha pagato 1\$, l'importo totale dovuto ora è 19\$ + la tariffa di rete. La tariffa di rete viene applicata dopo il primo pagamento)
- Su ogni pagamento (incluso il primo pagamento, nel nostro esempio, il totale sarà 20\$ + tariffa di rete immediata, anche sul primo pagamento)
- Non aggiungere mai la tariffa di rete (disabilita completamente la tariffa di rete)

Sebbene protegga dalle transazioni dust, può anche riflettersi negativamente sulle attività commerciali se non comunicato correttamente. I clienti potrebbero avere domande aggiuntive e pensare che li stiate facendo pagare troppo.

#### La fattura scade se l'intero importo non è stato pagato dopo?

Il timer della fattura è impostato di default a 15 minuti. Il timer è un meccanismo di protezione contro la volatilità poiché blocca l'importo in Bitcoin secondo i tassi di cambio Bitcoin a fiat. Se il cliente non paga la fattura entro il periodo definito, la fattura è considerata scaduta. La fattura è considerata "pagata" non appena la transazione è visibile sulla blockchain (0-conferme) ma considerata "completa" quando raggiunge il numero di conferme definito dal commerciante (solitamente, 1-6). Il timer è personalizzabile in minuti.

#### Considera la fattura pagata anche se l'importo pagato è inferiore dell'X% rispetto al previsto?

Quando un cliente utilizza direttamente un exchange per pagare una fattura, questo applica una piccola commissione. Questo significa che tale fattura non è considerata interamente completata. La fattura ottiene lo stato "pagata parzialmente". È possibile impostare la percentuale qui se un commerciante desidera accettare fatture pagate in modo insufficiente.

### Tariffe

In BTCPay Server, quando viene generata una fattura, è sempre necessario il prezzo Bitcoin/fiat più aggiornato e preciso. Quando si crea un nuovo negozio in BTCPay Server, agli amministratori viene chiesto di impostare la loro fonte di prezzo preferita; dopo che il negozio è stato configurato, i proprietari del negozio possono sempre cambiare la loro fonte di prezzo in questa scheda.

#### Script avanzati per le regole sulle tariffe

Utilizzato principalmente dagli utenti esperti. Se attivato, i proprietari dei negozi possono creare script relativi alle fluttuazioni di prezzo e come addebitare ai loro clienti.

#### Test

Un luogo rapido per testare le tue coppie di valute preferite. Include anche una funzione per controllare le coppie di valute predefinite tramite query REST.

### Aspetto del Checkout

La scheda Aspetto del Checkout inizia con le impostazioni specifiche della fattura e un metodo di pagamento predefinito e abilita metodi di pagamento specifici quando sono soddisfatti i requisiti impostati.

#### Impostazioni della fattura

Metodi di pagamento predefiniti. BTCPay Server in una configurazione standard ha tre opzioni.

- BTC (on-chain)
- BTC (LNURL-pay)
- BTC (Off-chain & Lightning)

Possiamo impostare parametri per il nostro negozio, dove un cliente interagirà solo con Lightning quando il prezzo è inferiore a un certo importo e viceversa per le transazioni On-chain quando X è maggiore di Y presentare sempre l'opzione di pagamento On-chain.

![immagine](assets/en/48.webp)

#### Checkout

A partire dalla versione 1.7 di BTCPay Server, è stata introdotta una nuova interfaccia di Checkout, chiamata Checkout V2. Dalla 1.9 è stato standardizzato, gli amministratori e i proprietari dei negozi possono ancora impostare il checkout alla versione precedente. Utilizzando l'interruttore "Usa il checkout classico", un proprietario di negozio può riportare il negozio all'esperienza di checkout precedente. BTCPay Server ha anche un insieme selezionato di preset per il commercio online o un'esperienza in negozio.

![immagine](assets/en/49.webp)

Quando un cliente interagisce con il negozio e genera una fattura, c'è un tempo di scadenza per la fattura. Per impostazione predefinita, BTCPay Server imposta questo a 5 minuti, e l'Amministratore può impostarlo come ritiene più appropriato. La pagina di checkout può essere ulteriormente personalizzata controllando i seguenti parametri:

- Celebrare il pagamento mostrando coriandoli
- Mostrare l'intestazione del negozio (Nome e logo)
- Mostrare il pulsante "Paga nel portafoglio"
- Unificare gli URL/QR dei pagamenti on-chain e off-chain
- Mostrare gli importi dei pagamenti Lightning in Satoshi
- Rilevamento automatico della lingua al checkout

![immagine](assets/en/50.webp)

Quando il rilevamento automatico della lingua non è impostato, BTCPay Server, per impostazione predefinita, visualizzerà l'inglese. Un proprietario di negozio può cambiare questa impostazione predefinita nella sua lingua preferita.

![immagine](assets/en/51.webp)

Cliccando sul menu a tendina, i proprietari dei negozi possono impostare un titolo HTML personalizzato da visualizzare sulla pagina di checkout.

![immagine](assets/en/52.webp)

Per assicurarsi che il cliente conosca il suo metodo di pagamento, un proprietario di negozio può impostare esplicitamente il suo checkout per richiedere sempre agli utenti di scegliere il loro metodo di pagamento preferito. Quando la fattura viene pagata, BTCPay Server consente al cliente di tornare al negozio online. I proprietari dei negozi possono impostare questo reindirizzamento automatico dopo che il cliente ha pagato.

![immagine](assets/en/53.webp)

#### Ricevuta pubblica

Nelle impostazioni della ricevuta pubblica, un proprietario di negozio può impostare le pagine delle ricevute come pubbliche e mostrare l'elenco dei pagamenti sulla pagina della ricevuta e il codice QR della ricevuta stessa affinché il cliente possa accedervi digitalmente con facilità.

### Token di Accesso

I token di accesso sono utilizzati per l'abbinamento a certe integrazioni di e-commerce o integrazioni personalizzate.

### Utenti

Gli utenti del negozio sono coloro che il proprietario del negozio può gestire, inclusi i membri del personale, i loro account e l'accesso al negozio. Dopo che i membri del personale hanno creato i loro account, il proprietario del negozio può aggiungere utenti specifici al negozio come Utenti Ospiti o proprietari. Per definire ulteriormente il ruolo dello staff, fare riferimento alla sezione successiva su "Impostazioni del negozio BTCPay Server - Ruoli".

### Ruoli

Un proprietario di negozio potrebbe non trovare significativi i ruoli standard degli utenti. Nelle impostazioni dei ruoli personalizzati, un proprietario di negozio può definire le esigenze esatte per ogni ruolo nella sua attività.

(1) Per creare un nuovo ruolo, cliccare sul pulsante "+ Aggiungi ruolo".

(2) Inserire un nome per il ruolo, ad esempio, "Cassiere".

(3) Configurare i singoli permessi per il ruolo.

- Modificare i tuoi negozi.
- Gestire i conti di scambio collegati ai tuoi negozi.
  - Visualizzare i conti di scambio collegati ai tuoi negozi.
- Gestire i tuoi pagamenti pull.
- Creare pagamenti pull.
  - Creare pagamenti pull non approvati.
- Modificare le fatture.
  - Visualizzare le fatture.
  - Creare una fattura.
  - Creare fatture dai nodi lightning associati ai tuoi negozi.
- Visualizzare i tuoi negozi.
  - Visualizzare le fatture.
  - Visualizzare le tue richieste di pagamento.
  - Modificare i webhook dei negozi.
- Modificare le tue richieste di pagamento.
  - Visualizzare le tue richieste di pagamento.
- Utilizzare i nodi lightning associati ai tuoi negozi.
  - Visualizzare le fatture lightning associate ai tuoi negozi.
  - Creare fatture dai nodi lightning associati ai tuoi negozi.
- Depositare fondi sui conti di scambio collegati ai tuoi negozi.
- Ritirare fondi dai conti di scambio al tuo negozio.
- Commerciare fondi sui conti di scambio del tuo negozio.

Quando il ruolo viene creato, il nome è fissato e non può essere cambiato.

### Webhook

All'interno di BTCPay Server, è abbastanza semplice creare un nuovo "Webhook". Nella scheda Impostazioni del negozio BTCPay Server - Webhook, un proprietario di negozio può facilmente creare un nuovo webhook cliccando su "+ Crea Webhook". I Webhook permettono a BTCPay Server di inviare eventi HTTP relativi al tuo negozio ad altri server o integrazioni di e-commerce.

Ora ti trovi nella vista per creare un Webhook. Assicurati di conoscere il tuo Payload URL e incollalo nel tuo BTCPay Server. Mentre hai incollato l'URL del payload, sotto di esso viene mostrato il segreto del webhook. Copia il segreto del webhook e forniscilo all'endpoint. Quando tutto è stato impostato, puoi attivare in BTCPay Server la Riconsegna Automatica. Cercheremo di riconsegnare ciascuna consegna fallita dopo 10 secondi, 1 minuto e fino a 6 volte dopo 10 minuti. Puoi alternare tra ogni evento o specificare gli eventi secondo le tue necessità. Assicurati di abilitare il webhook e premi Aggiungi webhook per salvarlo.

I Webhook non sono destinati ad essere compatibili con l'API di Bitpay. Ci sono due IPN separati (in termini di BitPay: "Notifiche di Pagamento Istantaneo") in BTCPay Server.

- Webhook
- Notifiche

Utilizza solo l'URL di Notifica quando crei fatture tramite l'api di Bitpay.

### Gestori di Pagamento

I gestori di pagamento lavorano in sinergia con il concetto di Pagamenti in BTCPay Server, aggregando i pagamenti per raggruppare più transazioni e inviarle in una volta sola. Con i gestori di pagamento, un proprietario di negozio può automatizzare i pagamenti. BTCPay Server offre due metodi di pagamenti automatizzati, On-chain e Off-chain (LN).
Il proprietario del negozio può cliccare e configurare separatamente entrambi i gestori di pagamento. Un proprietario di negozio potrebbe voler eseguire il gestore on-chain solo una volta ogni X ore, mentre quello off-chain potrebbe essere eseguito ad intervalli di pochi minuti. On-chain, è possibile anche impostare un obiettivo per il blocco in cui dovrebbe essere incluso. Per default, questo è impostato a 1 (o al prossimo blocco disponibile). Si noti che impostando il processore di pagamento Off-chain  si ha solo il timer dell'intervallo e nessun obiettivo di blocco. I pagamenti Lightning sono infatti istantanei.

I proprietari di negozio possono configurare il gestore on-chain solo se hanno un Hot-wallet collegato al loro negozio.

Dopo aver impostato un gestore di pagamento, è possibile rimuoverlo o modificarlo rapidamente tornando alla scheda del gestore di pagamento nelle impostazioni del negozio BTCPay Server.

**Nota**

Gestore di pagamento on-chain - Il gestore di pagamenti on-chain può funzionare solo su un negozio configurato con un Hot wallet collegato. Se non c'è un hot wallet collegato, BTCPay Server non detiene le chiavi del portafoglio e non sarà in grado di elaborare automaticamente i pagamenti.

### Email

BTCPay Server può utilizzare le Email per le Notifiche o, se impostato correttamente, per recuperare account creati sull'istanza, poiché da standard BTCPay Server non invia un'email quando, ad esempio viene persa la password.

Prima che un proprietario di negozio possa impostare regole Email, dobbiamo configurare alcune impostazioni email di base. BTCPay Server ha bisogno di queste impostazioni per inviare email per eventi basati sul tuo negozio o per il reset della password.

BTCPay Server ha semplificato la compilazione di queste informazioni utilizzando l'opzione "Compilazione Rapida":

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

Utilizzando l'opzione di compilazione rapida, BTCPay Server pre-compilerà i campi per il server SMTP e la porta; ora, il proprietario del negozio deve solo inserire le sue credenziali in un indirizzo Email, Login (che di solito corrisponde al tuo indirizzo email) e la tua password. L'opzione avanzata che BTCPay Server offre nelle impostazioni email è quella di Disabilitare i controlli di sicurezza del Certificato TLS; per default, questo è Abilitato.

Con le regole Email, un proprietario di negozio può impostare eventi specifici per attivare email a indirizzi email specifici.

- Fattura Creata
- Fattura Ha Ricevuto Pagamento
- Fattura in Elaborazione
- Fattura Scaduta
- Fattura Risolta
- Fattura Invalida
- Pagamento della Fattura Risolto

Se il cliente ha fornito un indirizzo Email, questi trigger possono anche inviare le informazioni al cliente. I proprietari di negozio possono pre-compilare l'oggetto per specificare la ragione di invio della Email e quale trigger l'ha causata.

### Moduli

Poiché BTCPay Server non raccoglie alcun dato, un proprietario di negozio potrebbe voler aggiungere un modulo personalizzato alla loro esperienza di checkout; in questo modo, il proprietario del negozio può raccogliere informazioni aggiuntive dal suo cliente. Il costruttore di moduli di BTCPay Server è composto da due parti, una visuale e una vista del codice più avanzata dei moduli.
Quando si crea un nuovo modulo, BTCPay Server apre una nuova finestra richiedendo informazioni di base su ciò che si desidera che il nuovo modulo richieda. Inizialmente, il proprietario del negozio deve dare un nome chiaro al suo nuovo modulo, questo nome NON può essere cambiato dopo averlo impostato.
![image](assets/en/68.webp)

Dopo che il proprietario del negozio ha dato un nome al modulo, è possibile anche attivare l'interruttore per "Consenti modulo per uso pubblico" su ON, diventerà verde. Ciò affinché il modulo venga utilizzato in ogni luogo visibile al cliente. Ad esempio, se un proprietario di negozio crea 1 fattura separata non attraverso il suo Punto Vendita, potrebbe comunque voler raccogliere le informazioni dal cliente; questo interruttore su ON consente di raccogliere tali informazioni.

![image](assets/en/69.webp)

Ogni modulo inizia con almeno 1 nuovo campo modulo. Il proprietario del negozio può scegliere quale tipo di campo dovrebbe essere;

- Testo
- Numero
- Password
- Email
- URL
- Numeri di telefono
- Data
- Campi nascosti
- Fieldset
- Un'area di testo per commenti aperti.
- Selettore di opzioni

Ogni tipo viene fornito con i suoi parametri da compilare. Il proprietario del negozio può impostarlo secondo le sue preferenze. Sotto il primo campo creato, i proprietari di negozi possono continuare ad aggiungere nuovi campi a questo modulo.

![image](assets/en/70.webp)

#### Moduli personalizzati avanzati

BTCPay Server consente anche di costruire moduli in codice. JSON, in particolare. Invece di guardare l'editor, i proprietari di negozi possono cliccare sul pulsante CODICE accanto all'editor, accedendo al codice. In una definizione di campo, possono essere impostati solo i seguenti campi; i valori dei campi sono memorizzati nei metadati della fattura:

| Campo                 | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | Se vero, il .value deve essere impostato nella definizione del modulo, e l'utente non sarà in grado di cambiare il valore del campo. (esempio: la versione della definizione del modulo)                                                                                                                                                                                                                                                                                                                                 |
| .fields.type          | Il tipo di input HTML testo, radio, checkbox, password, nascosto, pulsante, colore, data, datetime-local, mese, settimana, tempo, email, numero, intervallo, ricerca, url, selezione, tel                                                                                                                                                                                                                                                                                                                                |
| .fields.options       | Se .fields.type è select, l'elenco dei valori selezionabili                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.options.text  | Il testo visualizzato per questa opzione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | Il valore del campo se questa opzione è selezionata                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| .fields.type=fieldset | Crea un fieldset HTML intorno ai .fields.fields figli (vedi sotto)                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| .fields.name          | Il nome della proprietà JSON del campo come apparirà nei metadati della fattura                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| .fields.value         | Il valore predefinito del campo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| .fields.required      | se vero, il campo sarà obbligatorio                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| .fields.label         | L'etichetta del campo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.helpText      | Testo aggiuntivo per fornire una spiegazione per il campo.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| .fields.fields        | È possibile organizzare i propri campi gerarchicamente, consentendo ai campi figli di essere annidati all'interno dei metadati della fattura. Questa struttura può aiutarti a organizzare e gestire meglio le informazioni raccolte, rendendone più facile l'accesso e la consultazione. Ad esempio, se hai un modulo che raccoglie informazioni sui clienti, puoi raggruppare i campi sotto un campo padre chiamato cliente. All'interno di questo campo padre, potresti avere campi figli come nome, Email e indirizzo. |

Il nome del campo rappresenta il nome della proprietà JSON che memorizza il valore fornito dall'utente nei metadati della fattura. Alcuni nomi ben noti possono essere interpretati e modificare le impostazioni della fattura.

| Nome del campo   | Descrizione             |
| ---------------- | ----------------------- |
| invoice_amount   | L'importo della fattura |
| invoice_currency | La valuta della fattura |

È possibile precompilare i campi di una fattura automaticamente aggiungendo stringhe di query all'URL del modulo, come "?your_field=value".

Ecco alcuni casi d'uso per questa funzionalità:

- Assistenza nell'inserimento dei dati: Precompilare i campi con informazioni note sul cliente per facilitarne la compilazione del modulo. Ad esempio, se conosci già l'indirizzo email di un cliente, puoi precompilare il campo email per risparmiargli tempo.
- Personalizzazione: Personalizzare il modulo in base alle preferenze o alla segmentazione dei clienti. Ad esempio, se hai diversi livelli di clienti, puoi precompilare il modulo con dati pertinenti, come il loro livello di adesione oppure offerte specifiche.
- Tracciamento: Tracciare la fonte delle visite dei clienti utilizzando campi nascosti e valori precompilati. Ad esempio, puoi creare link con valori utm_media precompilati per ogni canale di marketing (es. Twitter, Facebook, Email). Questo ti aiuta ad analizzare l'efficacia delle tue iniziative di marketing.
- Test A/B: Precompilare i campi con valori diversi per testare differenti versioni del modulo, consentendoti di ottimizzare l'esperienza utente e i tassi di conversione.

### Riepilogo delle competenze

In questa sezione, hai appreso quanto segue:

- La disposizione e le funzioni delle schede nelle Impostazioni del Negozio
- Una moltitudine di opzioni per regolare con precisione il trattamento dei tassi di cambio sottostanti, pagamenti parziali e altro ancora.
- Personalizzare l'aspetto del checkout, inclusa l'abilitazione della chain princiape rispetto a Lightning in base al prezzo delle fatture.
- Gestire livelli di accesso al negozio e permessi attraverso i ruoli.
- Configurare email automatiche e trigger
- Creare moduli personalizzati per raccogliere ulteriori informazioni sui clienti al momento del checkout.

### Valutazioni delle conoscenze

#### Revisione KA

Qual è la differenza tra Impostazioni del Negozio e Impostazioni del Server?

#### Ipotesi KA

Descrivi alcune opzioni che potresti selezionare in Aspetto del Checkout > Impostazioni Fattura, e perché.

## BTCPay Server - Impostazioni del server

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay Server consiste in due diverse viste delle impostazioni. Una è dedicata alle Impostazioni del Negozio e l'altra alle Impostazioni del Server. Quest'ultima è disponibile solo se sei un amministratore del server e non per i proprietari dei negozi. Gli amministratori del server possono aggiungere utenti, creare ruoli personalizzati, configurare il server email, impostare politiche, eseguire compiti di manutenzione, controllare tutti i servizi collegati a BTCPay Server, caricare file sul server o controllare i Log.

### Utenti

Come menzionato nella parte precedente, gli Amministratori del Server possono invitare utenti al loro server aggiungendoli alla scheda Utenti.

### Ruoli personalizzati su tutto il server

BTCPay Server prevede due tipi di ruoli personalizzati, quelli specifici del negozio e i Ruoli personalizzati su tutto il server nelle impostazioni di BTCPay Server. Entrambi hanno un insieme simile di permessi; tuttavia, se impostati tramite la scheda Impostazioni di BTCPay Server - Ruoli, il ruolo applicato sarà su tutto il server e si applicherà a più negozi. Notare un'etichetta "Su tutto il server" ai ruoli personalizzati nelle impostazioni del server.

### Ruoli personalizzati su tutto il server

Set di permessi per ruoli personalizzati su tutto il server:

- Modifica i tuoi negozi.
- Gestisci gli exchange collegati ai tuoi negozi.
  - Visualizza gli exchange collegati ai tuoi negozi.
- Gestisci i tuoi pagamenti pull.
- Crea pagamenti pull.
  - Crea pagamenti pull non approvati.
- Modifica fatture.
  - Visualizza fatture.
  - Crea una fattura.
  - Crea fatture dai nodi lightning associati ai tuoi negozi.
- Visualizza i tuoi negozi.
  - Visualizza fatture.
  - Visualizza le tue richieste di pagamento.
  - Modifica i webhook dei negozi.
- Modifica le tue richieste di pagamento.
  - Visualizza le tue richieste di pagamento.
- Usa i nodi lightning associati ai tuoi negozi.
  - Visualizza le fatture lightning associate ai tuoi negozi.
  - Crea fatture dai nodi lightning associati ai tuoi negozi.
- Deposita fondi negli exchange collegati ai tuoi negozi.
- Preleva fondi dagli exchange verso il tuo negozio.
- Commercia fondi sugli exchange.

**!?Nota!?**

Quando il ruolo viene creato, il nome è fisso e non può essere cambiato.

### Email

Le impostazioni Email su tutto il server sono simili a quelle specifiche per negozio. Tuttavia, questa configurazione gestisce non solo i trigger per i negozi o i log degli amministratori. Questa configurazione Email rende anche disponibile il recupero della password su BTCPay Server al Login. Funziona in modo simile alle impostazioni specifiche per negozio; gli amministratori possono inserire rapidamente i parametri Email e inserire le credenziali email, e il server può ora inviare email.

### Politiche

Gli amministratori delle politiche di BTCPay Server possono impostare alcune configurazioni su argomenti come Impostazioni Utenti Esistenti, Impostazioni Nuovi Utenti, Impostazioni Notifiche e Impostazioni Manutenzione. Queste sono destinate a registrare nuovi utenti come amministratori o utenti normali o anche a nascondere BTCPay Server dai motori di ricerca aggiungendo al tuo header del server.

#### Impostazioni utenti esistenti

Le opzioni disponibili qui sono separate dai ruoli personalizzati. Questi permessi extra potrebbero rendere un negozio o il proprietario del negozio vulnerabile agli attacchi. Politiche che possono essere aggiunte agli utenti esistenti:

- Consenti ai non amministratori di usare il nodo Lightning interno nei loro negozi.
  - Questo permetterebbe ai proprietari dei negozi di usare il nodo Lightning dell'amministratore del server e, quindi, i suoi fondi! Attenzione, questa non è una soluzione per dare accesso a Lightning.
- Consenti ai non amministratori di creare portafogli caldi per i loro negozi.
  - Questo permetterebbe a chiunque abbia un account sulla tua istanza di BTCPay Server di creare Portafogli caldi e memorizzare il loro seed di recupero sul server dell'Amministratore. Questo potrebbe rendere l'Amministratore responsabile della custodia dei fondi di terzi!
- Consenti ai non amministratori di importare portafogli caldi per i loro negozi.
  - Simile al precedente argomento sulla creazione di Portafogli caldi, questa politica consente di importare un portafoglio caldo, con gli stessi pericoli menzionati nella sezione di creazione dei portafogli caldi.

#### Impostazioni nuovi utenti

Possiamo impostare alcune opzioni importanti per gestire i nuovi utenti che arrivano sul server. Possiamo impostare un'email di conferma per le nuove registrazioni, disabilitare la creazione di nuovi utenti attraverso la schermata di login e limitare l'accesso dei non amministratori alla creazione di utenti tramite l'API.

- Richiedi un'email di conferma per la registrazione.
  - L'amministratore del server deve avere configurato un server Email!
- Disabilita la registrazione di nuovi utenti sul server
- Disabilita l'accesso dei non amministratori all'endpoint API di creazione utente.

Per impostazione predefinita, BTCPay Server ha disabilitato la registrazione di nuovi utenti e disattivato l'accesso dei non amministratori all'endpoint API di creazione utente. Questo è dovuto a un aspetto di sicurezza per la quale viene inibita la possibilità di creare account nel caso qualcuno trovi il Login BTCPay del tuo server.

#### Impostazioni Notifiche

![image](assets/en/76.webp)

#### Impostazioni Manutenzione

BTCPay Server è un progetto Open Source che vive su GitHub. Ogni volta che BTCPay Server rilascia una nuova versione, gli Amministratori possono essere notificati. Gli amministratori possono anche voler scoraggiare i motori di ricerca (google, yahoo, duckduckgo) dall'indicizzare il dominio di BTCPay Server. Poiché BTCPay Server è FOSS, sviluppatori in tutto il mondo potrebbero voler creare nuove funzionalità; BTCPay Server ha una funzionalità sperimentale che, quando attivata, permette all'amministratore di utilizzare funzionalità non destinate alla produzione, puramente a scopo di test.

- Controlla le release su GitHub e notifica quando è disponibile una nuova versione di BTCPay Server.
- Scoraggia i motori di ricerca dall'indicizzare questo sito
- Abilita le funzionalità sperimentali.

![image](assets/en/77.webp)

#### Plugin

BTCPay Server può aggiungere Plugin ed espandere il suo set di funzionalità. I plugin, di default, sono caricati dalla repository plugin-builder di BTCPay Server. Un amministratore, tuttavia, può scegliere di vedere i plugin in stato di Pre-release, e se lo sviluppatore del plugin lo consente, l'amministratore del server può ora installare versioni beta dei plugin.

![image](assets/en/78.webp)

##### Impostazioni Personalizzazione

Una distribuzione standard di BTCPay Server sarà raggiungibile tramite il dominio impostato durante l'installazione. Tuttavia, un amministratore del server può rimappare il dominio e visualizzare una delle app create da un negozio specifico. L'Amministratore del Server può anche mappare domini specifici a app specifiche.

- Visualizza l'app sulla radice del sito web
  - Mostra l'elenco delle possibili app da mostrare sul dominio radice.

![image](assets/en/79.webp)

- Mappa domini specifici a app specifiche.
  - Quando clicchi per impostare un dominio specifico per app specifiche, l'Amministratore può impostare quanti domini puntare verso app specifiche come necessario.

![image](assets/en/80.webp)

#### Esploratori di Blocchi

BTCPay Server, come standard, viene fornito con mempool.space come suo esploratore di blocchi per le transazioni. Quando BTCPay Server genera una nuova fattura, e c'è una transazione ad essa legata, il proprietario del negozio può cliccare per aprire la transazione; BTCPay Server punterà da standard verso mempool.space come esploratore di blocchi; un amministratore del server può cambiarlo secondo le sue preferenze.

![image](assets/en/81.webp)

### Servizi

La scheda impostazioni di BTCPay Server: Servizi offre una panoramica dei componenti utilizzati dal tuo BTCPay Server. I servizi esposti dal tuo BTCPay Server possono variare a seconda del metodo di distribuzione.

Un Amministratore di BTCPay Server può cliccare su "Vedi informazioni" dietro ogni servizio per aprirlo e impostare specifiche configurazioni.

![image](assets/en/82.webp)

#### LND (gRPC)

BTCPay espone il servizio gRPC di LND per il consumo esterno; qui troverai le informazioni di connessione in questo specifico menu delle impostazioni; qui sono elencati i portafogli compatibili. BTCPay Server fornisce anche un codice QR per la connessione da scansionare e applicare nel portafoglio mobile.

Gli amministratori del server possono aprire più dettagli per vedere;

- Dettagli dell'host
- Uso di SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- GRPC SSL Cipher suite (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay espone il servizio REST di LND per il consumo esterno; qui troverai le informazioni di connessione; qui sono elencati i portafogli compatibili. Tra i portafogli compatibili ci sono Joule, Alby e ZeusLN. BTCPay Server fornisce un codice QR per la connessione, da scansionare e applicare nel portafoglio compatibile.

- REST Uri
- Macaroon
- AdminMacaroon - InvoiceMacaroon
- ReadonlyMacaroon

#### Backup del Seed LND

Il backup del seed LND è utile per recuperare i fondi dal tuo portafoglio LND in caso di corruzione del Server. Poiché il nodo Lightning è un Hot-wallet, puoi trovare le informazioni del seed su questa pagina.

LND documenta il processo di recupero. Vedi https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md per la documentazione.

#### Ride The Lightning

Ride the Lightning è uno strumento di gestione dei nodi Lightning costruito come software Open Source. BTCPay Server utilizza RTL come componente di gestione del nodo Lightning nel suo stack. Gli amministratori di BTCPay Server possono accedere a RTL tramite le impostazioni del Server - scheda Servizi o cliccando sul portafoglio Lightning.

#### Nodo completo P2P

Gli amministratori del server potrebbero voler collegare il loro nodo Bitcoin a un portafoglio mobile. Questa pagina espone informazioni per connettersi da remoto al tuo nodo completo tramite il protocollo P2P. Al momento, BTCPay Server elenca Blockstream Green e Wasabi wallet come portafogli compatibili. BTCPay Server fornisce un codice QR per la connessione, da scansionare e applicare nel portafoglio compatibile.

#### Nodo completo RPC

Questa pagina espone informazioni per connettersi da remoto al tuo nodo completo tramite il protocollo RPC.

#### SSH

SSH è utilizzato per scopi di manutenzione. BTCPay Server mostra il comando di connessione iniziale per raggiungere il tuo Server e le chiavi pubbliche SSH autorizzate a connettersi al tuo Server. Gli amministratori del Server potrebbero voler disattivare le modifiche SSH tramite l'interfaccia utente di BTCPay Server.

#### DNS Dinamico

Il DNS dinamico ti consente di avere un nome DNS stabile che punta al tuo Server, anche se il tuo indirizzo IP cambia regolarmente. Questo è consigliato se ospiti BTCPay Server a casa e desideri avere un dominio clearnet per accedere al tuo Server.

Nota che devi configurare correttamente il tuo NAT e l'installazione di BTCPay Server per ottenere il certificato HTTPS.

### Tema

BTCPay Server, da standard, viene fornito con due temi: modalità Chiara e Scuro. È possibile passare da uno all'altro cliccando su Account in basso a sinistra e alternando tra tema Scuro o tema Chiaro. Gli amministratori di BTCPay Server possono aggiungere il loro tema fornendo un tema CSS personalizzato.

Gli amministratori possono estendere il tema Chiaro/Scuro aggiungendo il proprio CSS personalizzato o impostando il loro tema personalizzato come completo.

![immagine](assets/en/83.webp)

#### Branding del Server

Gli amministratori del server possono cambiare il branding di BTCPay Server impostando un branding aziendale su tutto il server. Poiché BTCPay Server è FOSS, gli amministratori del server possono etichettare il software con il proprio marchio e cambiare l'aspetto per adattarlo alla loro attività.

![immagine](assets/en/84.webp)

### Manutenzione

Come amministratore del server, i tuoi utenti si aspettano che tu ti prenda cura del Server. All'interno della scheda Manutenzione di BTCPay Server, l'amministratore può eseguire manutenzioni essenziali. Impostare il nome di dominio per l'istanza di BTCPay Server, Riavviare o pulire il Server. Forse più importante, eseguire aggiornamenti.

BTCPay Server è un progetto Open Source e si aggiorna frequentemente. Ogni nuova release viene annunciata sia con le tue notifiche di BTCPay Server sia sui canali ufficiali attraverso i quali BTCPay Server comunica.

![immagine](assets/en/85.webp)

#### Nome del dominio

Dopo aver configurato BTCPay Server, un amministratore potrebbe voler cambiare il suo Dominio originale. All'interno della scheda Manutenzione, l'amministratore può cambiare il Dominio. Dopo aver cliccato conferma e impostato i corretti record DNS sul Dominio, BTCPay Server si aggiorna e riavvia per tornare al nuovo Dominio.

![immagine](assets/en/86.webp)

#### Riavvia

Riavvia BTCPay Server e i servizi correlati.

![immagine](assets/en/87.webp)

#### Pulisci

BTCPay Server funziona con componenti Docker; con gli aggiornamenti, potrebbero rimanere residui di immagini Docker, file temporanei, ecc. Gli amministratori del server possono pulirli e recuperare spazio nel loro ambiente eseguendo lo script di pulizia.
![image](assets/en/88.webp)

#### Aggiornamento

Probabilmente l'opzione più importante nella scheda Manutenzione. BTCPay Server è costruito dalla comunità e, quindi, i suoi cicli di aggiornamento sono più frequenti rispetto alla maggior parte dei prodotti software. Quando BTCPay Server ha una nuova release, gli amministratori saranno notificati nel centro notifiche. Cliccando sul pulsante di aggiornamento, BTCPay Server controllerà GitHub per l'ultima release, aggiornerà il Server e lo riavvierà. Prima di aggiornare, si consiglia sempre agli amministratori del server di leggere le note di rilascio distribuite attraverso i canali ufficiali di BTCPay Server.

![image](assets/en/89.webp)

### Log

Affrontare un problema non è mai divertente. Questo documento spiega il flusso di lavoro e i passaggi più comuni per identificare efficacemente il tuo problema e risolverlo da solo o con l'aiuto della comunità.

Identificare il problema è cruciale.

#### Riprodurre il problema

Prima di tutto, prova a determinare quando si verifica il problema. Prova a riprodurre il problema. Prova ad aggiornare e riavviare il tuo Server per verificare che tu possa riprodurre il problema. Se descrive meglio il tuo problema, scatta uno screenshot.

##### Aggiornare il server

Controlla la versione di BTCPay Server se è molto più vecchia dell'[ultima versione](https://github.com/btcpayserver/btcpayserver/releases) di BTCPay Server. Aggiornare il tuo Server potrebbe risolvere il problema.

##### Riavviare il server

Riavviare il tuo Server è un modo semplice per risolvere molti dei problemi più comuni di BTCPay Server. Potrebbe essere necessario accedere via SSH al tuo Server per riavviarlo.

##### Riavviare un servizio

Per alcuni problemi, potrebbe essere necessario riavviare solo un particolare servizio nel tuo deployment di BTCPay Server. Ad esempio, riavviare il container lets encrypt per rinnovare il certificato SSL.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Usa docker ps per trovare il nome di un diverso servizio che vorresti riavviare.

#### Esaminare i log

I log possono fornire un pezzo di informazione essenziale. Nei paragrafi seguenti, descriveremo come ottenere le informazioni dei log per varie parti di BTCPay.

##### Log di BTCPay

Dalla versione v1.0.3.8, puoi facilmente accedere ai log di BTCPay Server dall'interfaccia utente. Se sei un amministratore del server, vai su Impostazioni Server > Log e apri il file dei log. Se non sai cosa significa un particolare errore nei log, menzionalo durante la risoluzione dei problemi.

Se desideri log più dettagliati e stai utilizzando un deployment Docker, puoi visualizzare i log di specifici container Docker utilizzando la riga di comando. Vedi queste [istruzioni per accedere via ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) a un'istanza di BTCPay in esecuzione su un VPS.

Nella pagina successiva trovi un elenco generale dei nomi dei container utilizzati per BTCPay Server.

Esegui i comandi qui sotto per stampare i log per nome del container. Sostituisci il nome del container per visualizzare altri log dei container.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Log per      | Nome del Container                |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker

Ci sono diversi modi per accedere ai tuoi log LND quando utilizzi Docker. Prima accedi come root:

```bash
sudo su -
Naviga nella directory corretta:
cd btcpayserver-docker
# Trova il nome del container:
docker ps
Stampa i log per nome del container:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

In alternativa, puoi stampare rapidamente i log utilizzando l'ID del container (sono necessari solo i primi caratteri unici dell'ID, come i primi due a sinistra):

```bash
docker logs 'inserisci qui il tuo ID del container'
```

Se per qualsiasi motivo hai bisogno di più log

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/bitcoin/mainnet/
ls
```

Vedrai qualcosa come

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

Per accedere ai log non compressi di questi log fai `cat lnd.log` o se ne vuoi un altro, usa `cat lnd.log.15`.

Per accedere ai log compressi in `.gzip` usa `gzip -d lnd.log.16.gz` (in questo caso stiamo accedendo a `lnd.log.16.gz`). Questo dovrebbe darti un nuovo file, dove puoi fare `cat lnd.log.16`. Nel caso il sopra non funzioni, potresti aver bisogno di installare prima gzip con `sudo apt-get install gzip`.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Trova l'ID del container c-lightning.
docker logs 'inserisci qui il tuo ID del container'
```

alternativamente, usa questo

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

Puoi anche ottenere informazioni sui log con il comando cli di c-lightning.

```bash
bitcoin-lightning-cli.sh getlog
```

#### Log del Nodo Bitcoin

In aggiunta a [guardare i log](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) del tuo container Bitcoind, puoi anche usare uno qualsiasi dei [comandi bitcoin-cli](https://developer.bitcoin.org/reference/rpc/index.html)

[(apre una nuova finestra)](https://developer.bitcoin.org/reference/rpc/index.html) per ottenere informazioni dal tuo nodo bitcoin. BTCPay include uno script per permetterti di comunicare facilmente con il tuo nodo Bitcoin.

All'interno della cartella btcpayserver-docker, ottieni le informazioni sulla blockchain usando il tuo nodo:

```bash
bitcoin-cli.sh getblockchaininfo
```

BTCPay Server dispone di un file system locale e consente di caricare direttamente sul server gli asset dei prodotti (Store), i loghi e il branding. Il file system del server è accessibile solo agli amministratori del server; i proprietari dei negozi possono caricare i loro loghi/branding a livello di negozio.
Quando l'amministratore del server si trova nella scheda Archiviazione File, è possibile caricare direttamente sul proprio server o cambiare il provider di archiviazione file in un sistema di file locale o in Azure Blob Storage.

![immagine](assets/en/90.webp)

![immagine](assets/en/91.webp)

### Riepilogo delle Competenze

In questa sezione, hai appreso quanto segue:

- La differenza tra le impostazioni di Store e Server, in particolare per quanto riguarda Utenti, Ruoli ed Email
- Impostare politiche a livello di server per l'uso e la creazione di wallet caldi Lightning o Bitcoin on chain, la registrazione di nuovi utenti e le notifiche email.
- Come aggiungere temi personalizzati (invece delle semplici opzioni chiaro/scuro) così come creare loghi personalizzati
- Eseguire semplici compiti di manutenzione del server tramite l'interfaccia grafica fornita
- Risolvere problemi, inclusa la ricerca di dettagli per uno qualsiasi dei contenitori Docker o il proprio nodo
- Gestire l'archiviazione dei file

### Valutazione delle Conoscenze

#### Revisione Concettuale KA

Qual è la differenza nei Ruoli assegnati tramite le Impostazioni del Server rispetto a quelle del Store, e descrivere un possibile uso per l'uno rispetto all'altro?

#### Revisione Pratica KA

Descrivere alcuni possibili casi d'uso abilitati nella scheda Politiche.

#### Revisione Pratica KA

Descrivere alcune azioni che un amministratore potrebbe compiere regolarmente nella scheda Manutenzione.

## BTCPay Server - Pagamenti

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Una fattura è un documento che il venditore emette al compratore per riscuotere il pagamento.

In BTCPay Server, una fattura rappresenta un documento che deve essere pagato entro un intervallo di tempo definito ad un tasso di cambio fisso. Le fatture hanno una scadenza perché bloccano il tasso di cambio entro un determinato lasso di tempo per proteggere il ricevente dalle fluttuazioni di prezzo.

Il nucleo di BTCPay Server è la capacità di agire come un sistema di gestione delle fatture Bitcoin. Una fattura è uno strumento essenziale per tracciare e gestire un pagamento ricevuto.

A meno che non si utilizzi un [Wallet](https://docs.btcpayserver.org/Wallet/) integrato per ricevere pagamenti manualmente, tutti i pagamenti all'interno di un negozio saranno mostrati nella pagina delle Fatture. Questa pagina ordina cumulativamente i pagamenti per data ed è un pezzo centrale per la gestione delle fatture e la risoluzione dei problemi di pagamento.

![immagine](assets/en/92.webp)

### Generale

#### Stati delle fatture

La tabella sottostante elenca e descrive gli stati standard delle fatture in BTCPay e suggerisce azioni comuni. Le azioni sono solo raccomandazioni. Spetta agli utenti definire il miglior corso d'azione per il loro business e casi d'uso.

| Stato della Fattura                 | Descrizione                                                                                                                                           | Azione                                                                                                                                                             |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Nuova                               | Non pagata, il timer della fattura non è ancora scaduto                                                                                               | Nessuna                                                                                                                                                            |
| Nuova (pagataParziale)              | Pagata, non in pieno, il timer della fattura non è ancora scaduto                                                                                     | Nessuna                                                                                                                                                            |
| Scaduta                             | Non pagata, il timer della fattura è scaduto                                                                                                          | Nessuna                                                                                                                                                            |
| Scaduta (pagataParziale) \*\*       | Pagata, non per l'intero importo, e scaduta                                                                                                           | Contattare l'acquirente per organizzare un rimborso o chiedere di saldare il dovuto. Opzionalmente, segnare la fattura come regolata o invalida                    |
| Scaduta (pagataTardi)               | Pagata, per l'intero importo, dopo la scadenza del timer della fattura                                                                                | Contattare l'acquirente per organizzare un rimborso o processare l'ordine se le conferme tardive sono accettabili.                                                 |
| Liquidato (pagato in eccesso)       | Pagato più dell'importo della fattura, liquidato, ricevuto un numero sufficiente di conferme                                                          | Contattare l'acquirente per organizzare un rimborso per l'importo extra, o, facoltativamente, attendere che l'acquirente ti contatti                               |
| In elaborazione                     | Pagato per intero, ma non ha ricevuto un numero sufficiente di conferme specificate nelle impostazioni del negozio                                    | Contattare l'acquirente per organizzare un rimborso per l'importo extra, o, facoltativamente, attendere che l'acquirente ti contatti                               |
| In elaborazione (pagato in eccesso) | Pagato più dell'importo della fattura, non ricevuto un numero sufficiente di conferme                                                                 | Attendere la liquidazione poi contattare l'acquirente per organizzare un rimborso per l'importo extra, o, facoltativamente, attendere che l'acquirente ti contatti |
| Liquidato                           | Pagato, per intero, ricevuto un numero sufficiente di conferme nel negozio                                                                            | Eseguire l'ordine                                                                                                                                                  |
| Liquidato (marcato)                 | Lo stato è stato cambiato manualmente in liquidato da uno stato in elaborazione o non valido                                                          | L'amministratore del negozio ha marcato il pagamento come liquidato                                                                                                |
| Non valido\*                        | Pagato, ma non ha ricevuto un numero sufficiente di conferme entro il tempo specificato nelle impostazioni del negozio                                | Verificare la transazione su un esploratore blockchain, se ha ricevuto conferme sufficienti, marcarlo come liquidato                                               |
| Non valido (marcato)                | Lo stato è stato cambiato manualmente in non valido da uno stato liquidato o scaduto                                                                  | L'amministratore del negozio ha marcato il pagamento come non valido                                                                                               |
| Non valido (pagato in eccesso)      | Pagato più dell'importo della fattura, ma non ha ricevuto un numero sufficiente di conferme entro il tempo specificato nelle impostazioni del negozio | Verificare la transazione su un esploratore blockchain, se ha ricevuto conferme sufficienti, marcarlo come liquidato                                               |

#### Dettagli della fattura

La pagina dei dettagli della fattura contiene tutte le informazioni relative a una fattura.

Le informazioni sulla fattura sono create automaticamente in base allo stato della fattura, al tasso di cambio, ecc. Le informazioni sul prodotto sono create automaticamente se la fattura è stata creata con informazioni sul prodotto, come nell'app Punto Vendita.

#### Filtraggio delle fatture

Le fatture possono essere filtrate tramite i filtri rapidi situati accanto al pulsante di ricerca o i filtri avanzati, che possono essere attivati facendo clic sul link (Aiuto) in alto. Gli utenti possono filtrare le fatture per negozio, ID ordine, ID articolo, stato o data.

#### Esportazione delle fatture

Le fatture BTCPay Server possono essere esportate in formato CSV o JSON. Per maggiori informazioni sull'esportazione delle fatture e sulla contabilità.

#### Rimborsare una fattura

Se, per qualsiasi motivo, desideri emettere un rimborso, puoi facilmente creare un rimborso dalla vista della fattura.

#### Archiviare le fatture

A causa della funzionalità di non riutilizzo dell'indirizzo di BTCPay Server, è comune vedere molte fatture scadute nella pagina delle fatture del tuo negozio. Per nasconderle dalla tua vista, selezionale nell'elenco e contrassegnale come archiviate. Le fatture che sono state contrassegnate come archiviate non vengono eliminate. Il pagamento a una fattura archiviata verrà comunque rilevato dal BTCPay Server (stato pagato in ritardo). Puoi visualizzare le fatture archiviate del negozio in qualsiasi momento selezionando fatture archiviate dal menu a discesa del filtro di ricerca.

#### Valuta predefinita

Valuta predefinita del negozio, questa è stata impostata nella procedura guidata di creazione del negozio

#### Consentire a chiunque di creare una fattura

Dovresti abilitare questa opzione se vuoi permettere al mondo esterno di creare fatture nel tuo negozio. Questa opzione è utile solo se stai utilizzando il pulsante di pagamento o se stai emettendo fatture tramite API o sito web HTML di terze parti. L'app PoS è pre-autorizzata e non ha bisogno di essere abilitata affinché un visitatore casuale possa aprire il tuo negozio PoS e creare una fattura.

#### Aggiungere una tariffa aggiuntiva (tariffa di rete) alla fattura

- Solo se il cliente effettua più di un pagamento per fattura
- Su ogni pagamento
- Non aggiungere mai la tariffa di rete

#### La fattura scade se l'intero importo non è stato pagato dopo .. Minuti.

Il timer della fattura è impostato di default a 15 minuti. Il timer è un meccanismo di protezione contro la volatilità poiché blocca l'importo della criptovaluta secondo i tassi di cambio cripto a fiat. Se il cliente non paga la fattura entro il periodo definito, la fattura è considerata scaduta. La fattura è considerata "pagata" non appena la transazione è visibile sulla blockchain (0-conferme) ma considerata "completa" quando raggiunge il numero di conferme definito dal commerciante (solitamente, da 1 a 6). Il timer è personalizzabile.

#### Considera la fattura pagata anche se l'importo pagato è ..% inferiore al previsto.

In una situazione in cui un cliente utilizza un exchange per pagare direttamente una fattura, questo prende una piccola quantità come commissione. Questo significa che tale fattura non è considerata interamente completata. La fattura ottiene lo stato "pagata parzialmente". Se un commerciante vuole accettare fatture pagate meno di quanto previsto, puoi impostare qui la percentuale.

### Richieste

Le Richieste di Pagamento sono una funzionalità che consente ai proprietari di negozi BTCPay di creare fatture di lunga durata. I fondi sono pagati a una richiesta di pagamento utilizzando il tasso di cambio al momento del pagamento. Questo consente agli utenti di effettuare pagamenti a loro convenienza senza negoziare o verificare i tassi di cambio con il proprietario del negozio al momento del pagamento.

Gli utenti possono pagare con pagamenti parziali. La richiesta di pagamento rimarrà valida fino a quando non sarà pagata per intero o se il proprietario del negozio fissa un tempo di scadenza. Gli indirizzi non vengono mai riutilizzati. Un nuovo indirizzo viene generato ogni volta che l'utente clicca su paga per creare una fattura per la richiesta di pagamento.

I proprietari di negozi possono stampare le richieste di pagamento (o esportare i dati della fattura) per la tenuta dei registri e la contabilità. BTCPay etichetta automaticamente le fatture come Richieste di Pagamento nell'elenco fatture del tuo negozio.

#### Personalizza le Tue Richieste di Pagamento

- Importo della Fattura - Imposta l'Importo del Pagamento Richiesto
- Denominazione - Mostra l'Importo Richiesto in Fiat o Criptovaluta
- Quantità di Pagamento - Consenti solo pagamenti singoli o pagamenti parziali
- Tempo di Scadenza - Consenti pagamenti fino a una data o senza scadenza
- Descrizione - Editor di Testo, Tabelle di Dati, Incorpora Foto & Video
- Aspetto - Colore e Stile con Temi CSS

![immagine](assets/en/93.webp)

#### Crea una Richiesta di Pagamento

Nel menu a sinistra, vai su Richiesta di Pagamento e clicca su "Crea Richiesta di Pagamento".

![immagine](assets/en/94.webp)

Fornisci il Nome della Richiesta, Importo, Denominazione Visualizzata, Negozio Associato, Tempo di Scadenza & Descrizione (Opzionale)

Seleziona l'opzione Consenti al pagante di creare fatture nella loro denominazione se vuoi consentire pagamenti parziali.

Clicca su Salva & Visualizza per rivedere la richiesta di pagamento.

BTCPay crea un URL per la richiesta di pagamento. Condividi questo URL per visualizzare la tua richiesta di pagamento. Hai bisogno di più richieste uguali? Puoi duplicare le richieste di pagamento utilizzando l'opzione Clona nel menu principale.

![immagine](assets/en/95.webp)

**ATTENZIONE**

Le richieste di pagamento dipendono dal negozio, il che significa che durante la creazione ogni richiesta di pagamento è associata a un negozio. Assicurati di avere un portafoglio collegato al tuo negozio a cui appartiene la richiesta di pagamento.

#### Richiesta Pagata

Il pagante e il richiedente possono visualizzare lo stato della richiesta di pagamento dopo aver inviato il pagamento. Lo stato apparirà come Risolto se il pagamento è stato ricevuto per intero. Se sono stati effettuati solo pagamenti parziali, l'Importo Dovuto mostrerà il saldo dovuto.

![immagine](assets/en/96.webp)

#### Personalizza le Richieste di Pagamento

Il contenuto della descrizione può essere modificato utilizzando l'editor di testo della richiesta di pagamento. Entrambe le opzioni sono disponibili se vuoi utilizzare temi di colore aggiuntivi o stili CSS personalizzati.
Gli utenti non tecnici possono utilizzare un [tema bootstrap](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Ulteriori personalizzazioni possono essere effettuate fornendo codice CSS aggiuntivo, come mostrato di seguito.

```css
:root {
  --btcpay-font-family-base: "Source Sans Pro", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --btcpay-primary: #7d4698;
  --btcpay-primary-accent: #59316b;
  --btcpay-body-text: #333a41;
  --btcpay-body-bg: #fff;
  --btcpay-bg-tile: #f8f9fa;
}

#mainNav {
  color: white;
  background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
  color: white;
}
```

### Pagamenti Pull

Tradizionalmente, un ricevente condivide il proprio indirizzo Bitcoin per effettuare un pagamento in Bitcoin, e il mittente invia successivamente denaro a questo indirizzo. Tale sistema è chiamato pagamento Push, poiché il mittente inizia il pagamento mentre il ricevente può essere non disponibile, spingendo il pagamento al ricevente.

Ma che dire di invertire il ruolo?

E se, invece che un mittente che spinge il pagamento, il mittente permettesse al ricevente di prelevare il pagamento nel momento in cui lo ritiene opportuno? Questo è il concetto di pagamento Pull. Ciò permette nuove applicazioni, come:

- Un servizio di abbonamento (dove l'abbonato permette al servizio di prelevare denaro ogni tot tempo)
- Rimborsi (dove il commerciante permette al cliente di prelevare il denaro del rimborso nel suo portafoglio quando lo ritiene opportuno)
- Fatturazione basata sul tempo per i liberi professionisti (dove la persona che assume permette al libero professionista di prelevare denaro nel suo portafoglio man mano che il tempo viene registrato)
- Mecenatismo (dove il mecenate permette al beneficiario di prelevare denaro ogni mese per continuare a sostenere il loro lavoro)
- Vendita automatica (dove un cliente di un exchange permetterebbe all'exchange di prelevare denaro dal loro portafoglio per vendere automaticamente ogni mese)
- Sistema di prelievo del saldo (dove un servizio ad alto volume permette agli utenti di richiedere prelievi dal loro saldo, il servizio può quindi facilmente raggruppare tutti i pagamenti a molti utenti a intervalli fissi)

### Pagamenti

La funzionalità di pagamento è legata ai [Pagamenti Pull](https://docs.btcpayserver.org/PullPayments/). Questa funzionalità ti permette di creare pagamenti all'interno del tuo BTCPay. Questa funzionalità ti permette di processare pagamenti pull (rimborsi, pagamenti di stipendi o prelievi).

#### Esempio 1: Rimborso

Iniziamo con l'esempio del rimborso. Il cliente ha acquistato un articolo nel tuo negozio ma, purtroppo, deve restituire l'articolo. Vuole un rimborso. All'interno di BTCPay, puoi creare un [Rimborso](https://docs.btcpayserver.org/Refund/) e fornire al cliente il link per richiedere i suoi fondi. Non appena il cliente ha fornito il suo indirizzo e richiesto i fondi, verrà mostrato nei Pagamenti.

Il primo stato che assume è In Attesa di Approvazione. I commessi del negozio possono controllare se ce ne sono più di uno in attesa e, dopo aver fatto la selezione, si utilizza il pulsante Azioni.

Opzioni sul pulsante azione

- Approva i pagamenti selezionati
- Approva e invia i pagamenti selezionati
- Annulla i pagamenti selezionati

Il passo successivo è Approvare e inviare i pagamenti selezionati poiché vogliamo rimborsare il cliente. Controlla l'indirizzo del Cliente, mostra l'importo e se vogliamo che le commissioni vengano sottratte dal rimborso o meno. Una volta effettuati i controlli, resta solo da firmare la transazione.
Il cliente ora riceve aggiornamenti sulla pagina di Richiesta. Può seguire la transazione poiché gli viene fornito un link a un esploratore di blocchi e alla sua transazione. Una volta che la transazione è stata confermata e lo stato cambia in Completato.

#### Esempio 2: Stipendio

Ora parliamo del pagamento degli stipendi, poiché questo viene gestito internamente dal negozio e non su richiesta del Cliente. Il principio è lo stesso; si utilizzano i Pagamenti su Richiesta. Ma invece di creare un rimborso, effettueremo un [Pagamento su Richiesta](https://docs.btcpayserver.org/PullPayments/).

Vai alla scheda Pagamenti su Richiesta nel tuo server BTCPay. In alto a destra, clicca sul pulsante Crea Pagamento su Richiesta.

Ora siamo nella creazione del Pagamento, dai un nome e definisci l'importo desiderato nella valuta scelta, compila la Descrizione, così l'impiegato sa di cosa si tratta. La parte successiva è simile ai rimborsi. L'impiegato compila l'indirizzo di Destinazione e l'importo che vuole richiedere da questo Pagamento. Potrebbe decidere di effettuare 2 richieste separate, a indirizzi diversi, o anche di richiedere una parte tramite lightning.

Se ci sono più Pagamenti in attesa, puoi raggrupparli per essere firmati e inviati. Una volta firmati, i pagamenti passano alla scheda In corso e mostrano la Transazione. Quando accettati dalla rete, il pagamento passa alla scheda Completato. La scheda Completato è legata alla consultazione e funge da storico. Contiene i Pagamenti elaborati e la transazione ad essi associata.

### Pagamenti su Richiesta

#### Concetto

Quando un mittente configura un Pagamento su Richiesta, può configurare una serie di proprietà:

- Nome della Richiesta di Pagamento
- Un importo limite
- Un' Unità di conto (come BTC, SAT, USD)
- Metodi di Pagamento
  - BTC On-chain
  - BTC Off-chain
- Descrizione
- CSS personalizzato
- Data di fine (opzionale per Lightning Network BOLT11)

Fatto ciò, il mittente può condividere il pagamento su richiesta usando un link con il destinatario, permettendo al destinatario di creare un pagamento. Il destinatario sceglierà il suo pagamento:

- Quale metodo di pagamento utilizzare
- Dove inviare i soldi

Una volta creato un pagamento, questo verrà conteggiato nel limite del pagamento su richiesta per il periodo corrente. Il mittente approverà quindi il pagamento impostando il tasso al quale il pagamento verrà inviato e procederà con il pagamento.

Per il mittente, forniamo un modo facile da usare per raggruppare il pagamento di diversi pagamenti dal [Portafoglio Interno BTCPay](https://docs.btcpayserver.org/Wallet/).

#### API Greenfield

Il Server BTCPay fornisce un'API completa sia per il mittente che per il destinatario che è documentata nella pagina `/docs` della tua istanza. (o sul sito della documentazione https://docs.btcpayserver.org)

Poiché la nostra API espone la piena capacità dei pagamenti su richiesta, un mittente può automatizzare i pagamenti secondo le sue necessità.

### Riepilogo delle Competenze

In questa sezione, hai appreso quanto segue:

- Comprensione approfondita degli stati delle fatture di BTCPay Server così come le azioni che possono essere eseguite su di esse
- Personalizzare e gestire meccanismi di fattura estesi noti come Richieste.
- Le ulteriori possibilità di pagamento flessibili aperte dalla caratteristica unica di Pagamento su Richiesta di BTCPay Server, in particolare come gestire rimborsi e pagamenti degli stipendi.

### Valutazione della Conoscenza

#### Revisione Concettuale KA

Quali sono alcune differenze tra fatture e richieste di pagamento, e quale potrebbe essere un buon motivo per utilizzare quest'ultime?

#### Revisione Concettuale KA

In che modo i pagamenti su richiesta ampliano ciò che tipicamente può essere fatto on-chain? Descrivi alcuni casi d'uso che abilitano.

## Plugin Predefiniti del Server BTCPay

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Plugin e App Predefinite

Il server BTCPay viene fornito con un insieme standard di Plugin (App) che possono trasformare BTCPay Server in un gateway di pagamento per l'e-commerce. Con l'aggiunta di un Punto Vendita, una piattaforma di Crowdfunding e un semplice pulsante di pagamento, BTCPay Server diventa una soluzione facile da implementare.

### Punto Vendita

Uno dei Plugin standard di BTCPay Server è il Punto Vendita (PoS). Con il plugin PoS, un proprietario di negozio può creare un Webshop direttamente da BTCPay Server, senza la necessità di soluzioni di e-commerce di terze parti per gestire un Webshop. L'app PoS basata sul web consente agli utenti con negozi fisici di accettare facilmente Bitcoin, senza commissioni o coinvolgimento di terze parti, direttamente nel loro portafoglio. Il PoS può essere facilmente visualizzato su tablet o altri dispositivi che supportano la navigazione web. Gli utenti possono facilmente creare una scorciatoia sulla schermata home per accedere rapidamente all'app web.

#### Come creare un nuovo Punto Vendita

BTCPay Server consente ai proprietari di negozi di creare rapidamente un Punto Vendita in più layout. BTCPay Server riconosce che non ogni negozio è e-commerce, e non ogni negozio è un bar o un ristorante, e viene fornito con più configurazioni standard per il tuo PoS.

Quando il proprietario del negozio clicca su "Punto Vendita" nella sua barra del menu a sinistra, BTCPay Server chiederà ora un nome; questo nome sarà visibile nella barra del menu a sinistra. Clicca su Crea per creare il PoS.

![immagine](assets/en/97.webp)

#### Aggiornare il nuovo Punto Vendita creato

Dopo aver creato un nuovo PoS, la schermata successiva sarà per aggiornare il tuo Punto Vendita e aggiungere articoli per il tuo negozio.

##### Nome dell'app

Il nome dato qui al tuo Punto Vendita sarà visibile nel menu principale del BTCPay Server.

##### Titolo visualizzato

Il pubblico vedrà il titolo pubblico o il nome quando visita il tuo negozio. BTCPay Server come nome standard del tuo negozio “Tea shop” Sostituiscilo con il nome del tuo negozio.

![immagine](assets/en/98.webp)

#### Scegliere lo Stile del Punto Vendita

BTCPay Server è in grado di visualizzare il suo Punto Vendita in più modi.

- Lista prodotti
  - Una vista negozio dove i clienti possono acquistare solo 1 prodotto alla volta.
- Lista prodotti con carrello.
  - Una vista negozio dove i clienti possono acquistare più articoli contemporaneamente e ottenere una panoramica del carrello della spesa a destra dello schermo.
- Solo tastierino
  - Nessuna lista prodotti, solo un tastierino per la fatturazione diretta.
- Display stampabile (Lista prodotti stampabile con QR)
  - Se non puoi sempre visualizzare la tua lista prodotti digitalmente, hai bisogno di una soluzione "offline" per i prodotti; BTCPay Server ha una funzione di display stampabile per funzionare come un negozio Offline.

![immagine](assets/en/99.webp)

#### Stile del Punto Vendita - Lista prodotti

![immagine](assets/en/100.webp)

#### Stile del Punto Vendita - Lista prodotti + Carrello

![immagine](assets/en/101.webp)

#### Stile del Punto Vendita - Solo tastierino

![immagine](assets/en/102.webp)

#### Stile del Punto Vendita - Display stampabile

![immagine](assets/en/103.webp)

#### Valuta

Il proprietario del negozio può impostare una valuta diversa per il suo Punto Vendita rispetto alla sua valuta predefinita. La valuta predefinita del negozio popolerà automaticamente questo campo.

#### Descrizione

Racconta al mondo del tuo negozio; cosa stai vendendo e a quanto? Tutto ciò che spiega il tuo negozio va qui.

#### Prodotti

Quando viene creato un Punto Vendita, un server BTCPay standard aggiunge alcuni articoli al negozio come riferimento. Clicca sul pulsante Modifica su uno degli articoli standard per comprendere meglio ogni possibile opzione per un articolo.

Creare un nuovo prodotto nel tuo negozio prevede i seguenti campi:

- Titolo
- Prezzo (fisso, minimo o personalizzato)
- URL dell'immagine
- Descrizione
- Inventario
- ID
- Testo del pulsante di acquisto
- Abilita/Disabilita

Una volta che il proprietario del negozio ha compilato tutti i campi del nuovo prodotto, clicca su salva e noterai che la sezione Prodotti nel Punto Vendita sta iniziando a popolarsi. Assicurati sempre di salvare in alto a destra dello schermo per evitare che i proprietari dei negozi possano perdere i progressi già fatti nell'aggiunta di prodotti.

I proprietari dei negozi possono anche utilizzare l'"Editor Raw" per configurare i loro prodotti. L'editor raw richiede una conoscenza di base delle strutture JSON.

#### Checkout

BTCPay Server consente una piccola personalizzazione del checkout specifica per i PoS. Il proprietario del negozio può impostare il testo "Compra per x" o richiedere dati specifici del cliente aggiungendo moduli.

#### Mance

Non tutti i negozi necessitano dell'opzione per le mance sulle loro vendite. I proprietari dei negozi possono attivarla o disattivarla a seconda delle loro necessità. Se il negozio utilizza le mance, il proprietario del negozio può impostare il testo nel campo per le mance che preferisce. Le mance su BTCPay Server funzionano in base a una percentuale. I proprietari dei negozi possono aggiungere più percentuali con separazione tramite virgola.

#### Sconti

Come proprietario di un negozio, potresti voler offrire al cliente uno sconto personalizzato al momento del pagamento; l'interruttore per gli Sconti diventa disponibile al checkout del tuo negozio. Tuttavia, ciò è molto sconsigliato per i sistemi di self-checkout.

#### Pagamenti Personalizzati

Quando l'opzione Pagamenti Personalizzati è attivata, al cliente viene permesso di inserire il prezzo che ha stabilito, uguale o superiore alla fattura originale generata dal negozio.

#### Opzioni Aggiuntive

Dopo aver impostato tutto per il tuo Punto Vendita, rimangono alcune opzioni extra. I proprietari dei negozi possono facilmente incorporare il loro PoS tramite un Iframe o incorporare un pulsante di pagamento che collega a un articolo specifico del negozio. Per personalizzare il negozio PoS appena creato, i proprietari possono aggiungere CSS personalizzato in fondo alle opzioni aggiuntive.

#### Elimina questa app

Se il proprietario del negozio desidera eliminare completamente il Punto Vendita dal suo server BTCPay, in fondo all'aggiornamento del PoS, i proprietari dei negozi possono cliccare sul pulsante Elimina questa app per distruggere completamente la loro app PoS. Cliccando su "Elimina questa app", BTCPay Server chiederà una conferma digitando `DELETE` e confermando con il clic sul pulsante Elimina. Dopo l'eliminazione, il proprietario del negozio ritorna alla dashboard di BTCPay Server.

### BTCPay Server - Crowdfund

Accanto al plugin Punto Vendita, BTCPay Server offre l'opzione di creare un crowdfund. Proprio come qualsiasi altra piattaforma di Crowdfund, i proprietari dei negozi possono impostare un obiettivo, creare vantaggi per coloro i quali contribuiscono e personalizzarlo secondo le loro necessità.

#### Come impostare un nuovo crowdfund

Clicca sul plugin Crowdfund attraverso il menu principale sulla sinistra del tuo BTCPay Server, sotto la sezione Plugin. BTCPay Server ora richiederà un nome per il Crowdfund; questo nome sarà anche visualizzato nella barra del menu a sinistra.

#### Aggiorna il nuovo Punto Vendita creato

Una volta dato un nome all'App, la prossima schermata sarà per aggiornare l'App.

#### Nome App

Il nome dato al tuo Crowdfund sarà visibile nel menu principale di BTCPay Server.

#### Titolo Visualizzato

Il titolo è dato al Crowdfund per il pubblico.

#### Slogan

Dai al crowdfund uno slogan per riconoscere di cosa tratta la raccolta fondi.

![immagine](assets/en/107.webp)

#### URL Immagine in Evidenza

Ogni crowdfund ha la sua immagine principale, quel banner che riconosci direttamente. Questa immagine può essere memorizzata sul tuo server se hai diritti amministrativi, gli amministratori possono caricarla nelle impostazioni del server BTCPay Server - File. Quando sei un proprietario di negozio, l'immagine deve essere caricata sul web tramite un host di terze parti (ad esempio imgur)

#### Rendi il Crowdfund Pubblico

Questo interruttore rende il tuo Crowdfund pubblico e quindi visibile al mondo esterno. Per scopi di test o per vedere se il tuo tema è applicato correttamente, si potrebbe voler mantenere questa impostazione su OFF per il periodo di creazione del crowdfund.

#### Descrizione

Racconta al mondo del tuo Crowdfund, per cosa stai raccogliendo fondi? Tutto ciò che spiega il tuo crowdfund va qui.

![immagine](assets/en/108.webp)

#### Obiettivo del Crowdfund

Imposta un obiettivo target per quanto la raccolta fondi dovrebbe guadagnare per il progetto e in quale valuta l'obiettivo dovrebbe essere denominato. Assicurati che, se i tuoi obiettivi sono fissati con un orizzonte temporale, includi date di inizio e fine sotto Obiettivi nel crowdfund.

![immagine](assets/en/109.webp)

#### Vantaggi

I vantaggi aiutano molto con il tuo crowdfunding. Questo perché i vantaggi danno alle persone un modo per partecipare alla tua campagna. Si appellano sia alle motivazioni egoistiche che a quelle benevolenti. E ti permettono di accedere alle spese dei tuoi sostenitori, non solo al loro portafoglio filantropico -- puoi indovinare quale è più significativo.

La creazione di un nuovo vantaggio consiste nei seguenti campi;

- Titolo
- Prezzo (fisso, minimo o personalizzato)
- URL Immagine
- Descrizione
- Inventario
- ID
- Testo del Pulsante di Acquisto.
- Abilita/Disabilita

Una volta che il proprietario del negozio ha compilato tutti i campi del nuovo vantaggio da creare, clicca su salva e noterai che la sezione Vantaggi nei crowdfunds viene popolata.

![immagine](assets/en/110.webp)

### BTCPay Server - Punto Vendita

#### Contributi

I proprietari dei negozi possono scegliere come visualizzare i Vantaggi, come sono ordinati o anche classificati rispetto agli altri vantaggi. Tuttavia, una volta raggiunti gli obiettivi del Crowdfund, i proprietari dei negozi potrebbero voler fermare l'afflusso di donazioni verso questa raccolta fondi. Pertanto, può attivare l'opzione "Non permettere ulteriori contributi dopo aver raggiunto l'obiettivo". Questo fermerà il Crowdfund dall'accettare donazioni.

##### Comportamento del Crowdfund

Lo standard del Crowdfund conta solo le fatture create con il Crowdfund verso l'obiettivo. Tuttavia, potrebbero esserci casi in cui il proprietario del negozio vuole che tutte le fatture fatte in questo negozio contino verso il crowdfund.

#### Opzioni Aggiuntive per la personalizzazione

BTCPay Server offre un paio di personalizzazioni extra. Aggiungi suoni, animazioni o persino thread di discussione al Crowdfund. I proprietari dei negozi potrebbero anche cambiare l'aspetto del Crowdfund inserendo il proprio CSS personalizzato.

#### Elimina questa app

Se il proprietario del negozio vuole eliminare completamente il Crowdfund dal suo BTCPay Server, in fondo all'aggiornamento del Crowdfund i proprietari dei negozi possono cliccare sul pulsante "Elimina questa app" per distruggere completamente la loro app Crowdfund. Cliccando su "Elimina questa app", BTCPay Server chiederà conferma digitando `DELETE` e cliccando sul pulsante Elimina. Dopo l'eliminazione, il proprietario del negozio ritorna alla dashboard di BTCPay Server.

### BTCPay Server - Pulsante di Pagamento

I pulsanti di pagamento HTML facilmente integrabili e altamente personalizzabili permettono ai proprietari di negozi di ricevere mance e donazioni. Nella barra del menu a sinistra di BTCPay Server, sotto la sezione Plugins, i proprietari di negozi possono cliccare su "Pay Button" e cliccare su Enable per creare un pulsante di pagamento.

#### Impostazioni Generali

All'interno delle Impostazioni Generali per il Pulsante di Pagamento, i proprietari di negozi possono impostare

- Prezzo standard
- Valuta predefinita
- Metodo di pagamento predefinito
  - Usa il predefinito del negozio
  - BTC on-chain
  - BTC Off-chain (Lightning)
  - BTC Off-chain (LNURL-pay)
- Descrizione del checkout
- ID dell'ordine

#### Opzioni di visualizzazione

Il pulsante di pagamento di BTCPay Server può essere configurato per adattarsi a diversi stili. I pulsanti possono avere un importo fisso o personalizzato, mostrato sia con uno slider sia con i toggle più e meno.

#### Utilizzo del Modale

Quando si crea il pulsante di pagamento, i proprietari di negozi possono defnirne il comportamento quando un cliente lo clicca e mostrarlo in modale o come una nuova pagina.

**!?Nota!?**

Attenzione: Il pulsante di pagamento dovrebbe essere utilizzato solo per mance e donazioni

L'utilizzo del pulsante di pagamento per integrazioni di e-commerce non è raccomandato poiché le informazioni rilevanti per l'ordine possono essere modificate dall'utente. Per l'e-commerce, dovresti usare la nostra API Greenfield. Se questo negozio elabora transazioni commerciali, ti consigliamo di creare un negozio separato prima di utilizzare il pulsante di pagamento.

#### Personalizza il testo del pulsante di pagamento

Per impostazione predefinita, il pulsante di pagamento di BTCPay Server indica "Paga con BTCPay". I proprietari di negozi possono impostare questo testo a loro piacimento e cambiare il logo di BTCPay Server con il proprio. Imposta il testo utilizzando "Pay Button Text" e incolla l'URL dell'immagine sotto "Pay Button Image URL".

##### Dimensione dell'immagine

La dimensione dell'immagine nel pulsante può essere impostata solo su tre valori predefiniti.

- 146x40px
- 168x46px
- 209x57px

#### Tipo di pulsante

BTCPay Server conosce tre stati per il Pulsante di Pagamento.

- Importo Fisso
  - Il prezzo precedentemente impostato si trova nelle impostazioni generali del pulsante.
- Importo Personalizzato
  - Il pulsante di pagamento di BTCPay Server ha i toggle + e - per impostare un prezzo personalizzato.
  - Quando si utilizza l'importo personalizzato, BTCPay Server richiederà un Min, un Max e quanto dovrebbe aumentare gradualmente.
  - I pulsanti possono essere impostati su "Usa stile di input semplice". Questo elimina i toggle +/-.
  - Adatta il pulsante in linea dove pulsante e toggle appaiono in linea.
- Slider
  - Simile all'importo personalizzato, tuttavia, visivamente diverso poiché ha uno slider invece dei toggle +/-.
  - Quando si utilizza lo Slider, BTCPay Server richiederà un Min, un Max e quanto dovrebbe aumentare gradualmente.

**!?Nota!?**

La cancellazione del Pulsante di Pagamento può essere effettuata in alto nella descrizione di avviso.

#### Notifiche di Pagamento

L'IPN del Server (Notifica di Pagamento Istantaneo) è destinata ai webhook e può essere compilata con un URL per postare i dati post-acquisto.

#### Notifiche Email

Ogni volta che avviene un pagamento, BTCPay Server può notificare il proprietario del negozio.

#### Reindirizzamento del browser

Quando il cliente completa l'acquisto, verrà reindirizzato a questo link se impostato dal proprietario del negozio.

#### Opzioni Avanzate del Pulsante di Pagamento

Specifica ulteriori parametri della stringa di query che dovrebbero essere aggiunti alla pagina di checkout una volta creato la fattura. Ad esempio, `lang=da-DK` caricerebbe la pagina di checkout in danese per impostazione predefinita.

#### Utilizza App come Endpoint

Collega direttamente il pulsante di pagamento ad un articolo in una delle app PoS o Crowdfund precedenti.
I proprietari di negozi possono cliccare sul menu a discesa e selezionare l'App desiderata; una volta selezionata l'App, il proprietario del negozio può aggiungere l'articolo che necessita di essere collegato.

#### Codice Generato

Poiché il pulsante di pagamento di BTCPay Server è HTML facilmente incorporabile, BTCPay Server mostra il codice generato da copiare in un sito web in fondo dopo aver configurato il pulsante di pagamento.

I proprietari di negozi possono copiare il codice generato nel loro sito web, e il pulsante di pagamento di BTCPay Server è direttamente attivo sul loro sito web.

#### Notifiche di Pagamento

L'IPN (Instant Payment Notification) del server è destinata ai webhook e può essere compilata con un URL per postare i dati dell'acquisto.

#### Notifiche Email

Ogni volta che avviene un pagamento, BTCPay Server può notificare il proprietario del negozio.

#### Reindirizzamento del Browser

Quando il cliente completa l'acquisto, verrà reindirizzato a questo link se impostato dal proprietario del negozio.

#### Opzioni Avanzate per il Pulsante di Pagamento

Specificare ulteriori parametri della stringa di query che dovrebbero essere aggiunti alla pagina di checkout una volta creata la fattura. Ad esempio, `lang=da-DK` caricerebbe la pagina di checkout in danese per impostazione predefinita.

#### Utilizzare l'App come Endpoint

Collegare direttamente il pulsante di pagamento a un articolo in una delle app PoS o Crowdfund precedentemente. I proprietari di negozi possono cliccare sul menu a discesa e selezionare l'app desiderata, una volta selezionata l'app, il proprietario del negozio può aggiungere l'articolo che necessita collegare.

#### Codice Generato

Poiché il pulsante di pagamento di BTCPay Server è un HTML facilmente incorporabile, BTCPay Server mostra il codice generato da copiare in un sito web in fondo dopo aver configurato il pulsante di pagamento. I proprietari di negozi possono copiare il codice generato nel loro sito web e il pulsante di pagamento di BTCPay Server è direttamente attivo sul loro sito web.

### Riepilogo delle Competenze

In questa sezione hai imparato:

- Come utilizzare il plugin PoS integrato di BTCPay Server per creare facilmente un negozio personalizzato
- Come utilizzare il plugin Crowdfund integrato di BTCPay Server per creare facilmente un'app di crowdfunding personalizzata
- Generare codice per un pulsante di pagamento personalizzato utilizzando il plugin del Pulsante di Pagamento

### Valutazione delle Conoscenze

#### Revisione KA

Quali sono i tre plugin integrati che vengono forniti standard con BTCPay Server? In poche parole, descrivi come ciascuno può essere utilizzato.

# Configurazione di BTCPay Server

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Comprensione di base dell'installazione di BTCPay Server su un ambiente LunaNode

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### Installazione di BTCPay Server su Amb. Hostato (LunaNode)

Questi passaggi forniranno tutte le informazioni necessarie per iniziare a utilizzare BTCPay Server su LunaNode. Ci sono molte opzioni su come distribuire il software.
Puoi trovare tutti i dettagli di BTCPay Server su https://docs.btcpayserver.org.

#### Da dove iniziamo?

In questa parte, familiarizzerai con LunaNode come provider di hosting, farai i primi passi per utilizzare il tuo BTCPay Server e capirai come procedere con Lightning Network. Dopo aver esaminato tutti i passaggi, potrai gestire un negozio online o una piattaforma di crowdfunding che accetta Bitcoin!

Questo è uno dei tanti modi per distribuire BTCPay Server. Leggi la nostra documentazione per maggiori dettagli,

https://docs.btcpayserver.org.

### BTCPay Server - Distribuzione su LunaNode

#### Distribuzione su LunaNode

Prima, vai sul sito di LunaNode.com, dove creeremo un nuovo account. Clicca su "Sign Up" in alto a destra o usa la procedura guidata "Get Started" sulla loro homepage.
![image](assets/en/111.webp)

Dopo aver creato il tuo nuovo account, LunaNode invia una email di verifica. Una volta verificato l'account, a differenza di Voltage, ti viene immediatamente presentata la possibilità di ricaricare il saldo del tuo account. Questo saldo è necessario per pagare lo spazio server e i costi di hosting.

![image](assets/en/112.webp)

#### Aggiungi credito al tuo account LunaNode

Una volta cliccato su "Deposit credit", puoi impostare quanto vuoi ricaricare sul tuo account e come vuoi pagarlo. LunaNode e BTCPay Server costeranno tra 10$USD e 20$USD al mese.
A differenza di Voltage.cloud, ottieni pieno accesso al tuo Virtual Private Server (VPS da qui in poi) e quindi hai più controllo sul tuo server. Dopo aver creato il tuo nuovo account, LunaNode invia una email di verifica.

#### Come distribuire un nuovo server?

In questa guida, procederemo alla configurazione creando un set di chiavi API e utilizzando il lanciatore di BTCPay Server creato da LunaNode.

Nella tua dashboard di LunaNode, clicca su API in alto a destra. Questo aprirà una nuova pagina. Dobbiamo solo impostare un Nome per la chiave API. Il resto sarà gestito da LunaNode e non sarà coperto in questa guida. Clicca sul pulsante "Create API Credential".
Dopo aver creato le credenziali API, riceverai una lunga stringa di lettere e caratteri. Questa è la tua chiave API.

![image](assets/en/113.webp)

#### Come distribuire un nuovo server?

Ci sono 2 parti in queste credenziali, chiave API e ID API; avremo bisogno di entrambi. Prima di passare al punto successivo, apriamo una seconda scheda nel browser e andiamo su https://launchbtcpay.lunanode.com/

Qui ti verrà chiesto di fornire la tua chiave API e ID API. Questo serve per verificare la tua identità per la creazione di questo nuovo server. La chiave API dovrebbe essere ancora aperta nella tua scheda precedente; se scorri in basso nella tabella qui sotto, troverai l'ID API.

Torna alla pagina con il Launcher, compila i campi con la tua chiave API e ID, e clicca su continua.

![image](assets/en/114.webp)

Nel passo successivo, puoi fornire un nome di dominio. Se possiedi già un dominio e vuoi usarlo per BTCPay Server, assicurati di aggiungere anche il record DNS (chiamato record `A`) sul tuo dominio. Se non possiedi un dominio, usa il dominio fornito da LunaNode invece (puoi cambiarlo in seguito nelle impostazioni di BTCPay Server) e clicca su Continua.

Per saperne di più su come impostare o cambiare un record DNS per BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Lancia BTCPay Server su LunaNode

Dopo aver compiuto i passi precedenti, possiamo impostare tutte le opzioni per il nostro nuovo server. Qui selezioneremo Bitcoin (BTC) come valuta supportata; possiamo impostare un'email per ricevere notifiche riguardo al rinnovo dei certificati di crittografia; questo non è obbligatorio.
Questa guida mira a configurare un ambiente Mainnet; tuttavia, LunaNode permette anche di impostare Testnet o Regtest per scopi di sviluppo. Lascieremo l'opzione Mainnet per questa guida.
Scegli la tua implementazione di Lightning. LunaNode offre due diverse implementazioni, LND e Core Lightning. Per questa guida, sceglieremo LND. Ci sono piccole, ma significative differenze tra le implementazioni; per maggiori informazioni su questo, si raccomanda di leggere la documentazione estesa; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![immagine](assets/en/115.webp)

LunaNode offre diversi piani di Macchine Virtuali (VM). Questi variano in fasce di prezzo e specifiche del server. Per questa guida sarà sufficiente un piano m2; tuttavia, se hai selezionato altre valure oltre a Bitcoin, considera di usare almeno un m4.

Accelerare la sincronizzazione iniziale della blockchain; questa è un'opzione facoltativa e dipende dalle tue necessità. Ci sono opzioni avanzate come impostare un Alias Lightning, puntare a una specifica release di GitHub, o impostare chiavi SSH; nessuna di queste sarà trattata in questa guida.

Dopo aver compilato il modulo, devi cliccare su Launch VM, e LunaNode inizierà a creare la tua nuova VM, includendo BTCPay Server installato su di essa. Questo processo richiede un paio di minuti; una volta che il tuo server è pronto, LunaNode ti fornirà il link al tuo nuovo BTCPay Server.

Dopo il processo di creazione, clicca sul link al tuo BTCPay Server; qui, ti verrà chiesto di creare un account Amministratore.

![immagine](assets/en/116.webp)

### Riepilogo delle Competenze

In questa sezione hai imparato:

- Creare e finanziare un account su LunaNode
- Usare il BTCPay Server Launcher per creare il tuo server

### Valutazione delle Conoscenze

#### Revisione Concettuale KA

Descrivi alcune delle differenze tra eseguire un'istanza di BTCPay Server su un VPS rispetto alla creazione di un account su un'istanza ospitata.

## Installazione di BTCPay Server su un ambiente Voltage

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Familiarizzerai con Voltage.cloud come provider di hosting, farai i primi passi per usare il tuo BTCPay Server e capirai come procedere con Lightning Network. Dopo aver seguito tutti i passaggi, potrai gestire un negozio online o una piattaforma di crowdfunding che accetta Bitcoin!

Questo è uno dei tanti modi per distribuire BTCPay Server. Leggi la nostra documentazione per maggiori dettagli,
https://docs.btcpayserver.org.

### Distribuzione di BTCPay Server - Voltage.cloud

Prima di tutto, vai sul sito web Voltage.cloud e registrati per un nuovo account. Quando crei un account puoi iscriverti per una prova gratuita di 7 giorni. Clicca su Sign Up in alto a destra o usa l'opzione "Try a free 7 day trial" sulla loro homepage.

![immagine](assets/en/117.webp)

Dopo aver creato un account, clicca sul pulsante `NODES` sulla tua dashboard. Una volta selezionati i Nodi e creato un nuovo nodo, ci verranno presentate le possibili offerte di nodi da Voltage. Poiché questa guida tratterà anche Lightning Network, su Voltage, dobbiamo prima scegliere la nostra implementazione di Lightning prima di creare un BTCPay Server. Clicca su Lightning Node.

![immagine](assets/en/118.webp)
Qui dovrai selezionare quale tipo di nodo Lightning desideri. Voltage offre una varietà di opzioni per la configurazione di lightning. Questo è diverso quando si effettua il deploy con, ad esempio, LunaNode. Ai fini di questa guida, un Lite Node sarà sufficiente. Leggi di più sulle differenze su Voltage.cloud.
![immagine](assets/en/119.webp)

Dai un Nome al tuo nodo, imposta una password e proteggi questa password. Se questa password viene persa, perderai l'accesso ai tuoi backup e Voltage non può recuperarla. Crea il nodo e Voltage ti mostrerà il progresso. Voltage ha creato il tuo Nodo Lightning. Ora possiamo creare l'istanza di BTCPay Server e accedere direttamente a Lightning Network.

Clicca su Nodi nell'angolo in alto a sinistra del tuo cruscotto. Qui puoi configurare la prossima parte della tua istanza di BTCPay Server. Clicca su "crea nuovo" una volta che sei nella panoramica dei nodi. Ti verrà mostrata una schermata simile a quella precedente. Ora invece di Nodo Lightning, scegliamo BTCPay Server.

Voltage ti mostra la geolocalizzazione del tuo BTCPay Server, Voltage hosta negli Stati Uniti. Qui vedrai anche il costo dell'hosting del server. Clicca su Crea e dai un nome al tuo BTCPay Server. Abilita Lightning e Voltage ti mostra il nodo Lightning creato nel passaggio precedente. Clicca su Crea e Voltage creerà un'istanza di BTCPay Server.

![immagine](assets/en/120.webp)

Dopo aver cliccato su crea, Voltage ti fornisce nome utentee e password predefiniti. Questi sono simili alla password che hai impostato precedentemente in Voltage. Clicca sul pulsante Accedi al Conto per essere reindirizzato al tuo BTCPay Server.

Benvenuto nella tua nuova istanza di BTCPay Server. Poiché abbiamo già configurato Lightning nel processo di creazione, ti mostra che Lightning è già abilitato!

### Riepilogo delle Competenze

In questo capitolo hai imparato:

- Creare un account su Voltage.cloud
- Passaggi per far funzionare BTCPay Server insieme a un nodo Lightning sull'account

### Valutazione delle Conoscenze

#### Revisione Concettuale KA

Quali sono alcune differenze chiave tra le configurazioni di Voltage e LunaNode?

## Installazione di BTCPay Server su un nodo Umbrel

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

Al termine di questi passaggi, puoi accettare pagamenti lightning nel tuo negozio BTCPay sulla tua rete locale. Questo processo si applica anche se gestisci un nodo umbrel in un ristorante o in un'attività commerciale. Se vuoi collegare questo negozio a un sito web pubblico, segui l'esercizio Avanzato per esporre il tuo nodo umbrel al pubblico.

https://umbrel.com/

![immagine](assets/en/121.webp)

### BTCPay Server - Implementazione su Umbrel

Dopo che il tuo nodo Umbrel ha completato la sincronizzazione con la blockchain di Bitcoin, vai all'Umbrel App Store e cerca BTCPay Server sotto Apps.

![immagine](assets/en/122.webp)

Clicca su BTCPay Server per vedere i dettagli dell'App. Quando i dettagli di BTCPay Server sono aperti, in basso a destra mostra i requisiti affinché l'App funzioni correttamente. Indica che richiede il nodo Bitcoin e Lightning. Se non hai installato il Nodo Lightning sul tuo Umbrel, clicca su Installa. Questo processo può richiedere un paio di minuti.

![immagine](assets/en/123.webp)

Dopo aver installato il tuo Nodo Lightning:

1. Clicca su apri nei dettagli dell'app o sull'App nel cruscotto di Umbrel.
2. Clicca su imposta un nuovo nodo; ti verranno mostrate 24 parole per il recupero del tuo nodo lightning.
3. Scrivile.

![immagine](assets/en/124.webp)
Umbrel richiederà la verifica delle parole appena annotate. Dopo aver configurato il nodo Lightning, torna all'App Store di Umbrel e trova BTCPay Server. Clicca sul pulsante di installazione, e Umbrel mostrerà se i componenti richiesti sono installati e che BTCPay Server richiede l'accesso a questi componenti. Dopo l'installazione, clicca su Apri in alto a destra nei dettagli dell'App o apri BTCPay Server tramite la dashboard di Umbrel.
Umbrel richiederà la verifica delle parole appena annotate.

![immagine](assets/en/125.webp)

**!?Nota!?**

Assicurati di conservarle in un luogo appropriato, come precedentemente appreso con la conservazione delle chiavi.

Dopo aver configurato il nodo Lightning, torna all'App Store di Umbrel e trova BTCPay Server. Clicca sul pulsante di installazione, e Umbrel mostrerà se i componenti richiesti sono installati e che BTCPay Server richiede l'accesso a questi componenti.

![immagine](assets/en/126.webp)

Dopo l'installazione, clicca su Apri in alto a destra nei dettagli dell'App o apri BTCPay Server tramite la dashboard di Umbrel.

![immagine](assets/en/127.webp)

### Riepilogo delle Competenze

In questa sezione hai imparato:

- I passaggi per installare BTCPay Server con funzionalità Lightning su un nodo Umbrel

### Valutazione delle Conoscenze

#### Revisione Concettuale KA

In che modo la configurazione su Umbrel differisce dalle precedenti due opzioni ospitate?

# Conclusione

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>



## Valuta il corso
<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>
<isCourseReview>true</isCourseReview>

## Conclusione del Corso

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![immagine](assets/en/128.webp)

Dovresti anche avere una comprensione generale di cosa sia Bitcoin, come funziona e come può scalare attraverso layer aggiuntivi come Lightning Network. In questo corso, abbiamo visto come chiunque possa utilizzare BTCPay Server, dall'installazione iniziale alla creazione di negozi e alla gestione complessa delle fatture, per diventare un individuo o un commerciante finanziariamente sovrano.

Congratulazioni per aver completato questo corso. Speriamo che tu abbia apprezzato i contenuti e continui a utilizzare ed esplorare BTCPay Server, e che tu sia entusiasta del futuro promettente che Bitcoin, la comunità in espansione ed i partecipanti porteranno avanti, cosi come lo siamo noi.

> **FOSS è inevitabile.**

### Glossario

| Termine                                         | Definizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Attacco del 51%                                 | L'atto intenzionale di costruire una nuova blockchain più lunga per sostituire i blocchi nella blockchain. Questo ti consente di sostituire le transazioni che sono state minate nella blockchain. Questo tipo di attacco è più facile da eseguire quando si ha la maggior parte della potenza di mining, motivo per cui è definito come "Attacco della Maggioranza" o "Attacco del 51%".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| AccountKey                                      | La chiave dell'account da ribasare                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PercorsoAccountKey                              | Il percorso dalla radice alla chiave dell'account è prefissato dall'impronta della chiave pubblica principale.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Indirizzo                                       | Gli indirizzi Bitcoin codificano in modo compatto le informazioni necessarie per pagare un destinatario. Un indirizzo moderno consiste in una stringa di lettere e numeri che inizia con bc1 e appare come bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4. Un indirizzo è una forma abbreviata dello script di blocco del destinatario, che può essere utilizzato dal mittente per trasferire fondi al destinatario. La maggior parte degli indirizzi rappresenta o la chiave pubblica del destinatario o una forma di script che definisce condizioni di spesa più complesse. L'esempio precedente è un indirizzo bech32 che codifica un programma di testimoni che blocca i fondi all'hash di una chiave pubblica (Vedi Pay-to-Witness-Public-Key-Hash). Esistono anche formati di indirizzo più vecchi che iniziano con 1 o 3 che utilizzano la codifica degli indirizzi Base58Check per rappresentare hash di chiavi pubbliche o hash di script. |
| Tipo di Indirizzo                               | Un indirizzo può rappresentare diversi script. Gli indirizzi sono codificati e prefissati al fine di trasmettere il loro tipo di script. Gli indirizzi legacy utilizzano Base58, e quando un indirizzo legacy è l'hash di una chiave pubblica, un cosiddetto indirizzo P2PKH, inizia con un ‘1’. Meno frequentemente, un indirizzo legacy è un hash di uno script, in tal caso inizierà con un ‘3’. Attualmente, tutti gli indirizzi SegWit sono codificati in Bech32 e iniziano con il prefisso ‘bc1’.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| App                                             | BTCPay Server ha plugin che potrebbero funzionare come un'applicazione in sé.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| BIP 329                                         | Esporta/importa etichette del portafoglio                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| BIP49                                           | Definisce lo schema di derivazione per i portafogli HD utilizzando il formato di serializzazione P2WPKH-nested-in-P2SH (BIP 141) per le transazioni con testimone segregato.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Indirizzo Bitcoin                               | Stringa alfanumerica dove invii i tuoi bitcoin, quindi ora "vive" lì. È un identificativo, che consiste in una stringa di circa 33 lettere e numeri combinati. In una versione corrente del protocollo, un indirizzo inizia con 1, 3, o b. Avere l'indirizzo di un destinatario è una parte necessaria per avviare una transazione bitcoin. Gli indirizzi Bitcoin sono generati dalle chiavi pubbliche e diversi indirizzi possono essere generati da un insieme di chiavi pubbliche per migliorare la privacy. Gli indirizzi Bitcoin agiscono proprio come gli indirizzi email, se vuoi inviare un messaggio devi sapere dove sta andando, lo stesso vale per i bitcoin. Prima di inviare una transazione bitcoin, devi assicurarti che l'indirizzo del destinatario sia accurato poiché le transazioni bitcoin sono irreversibili e potresti inviare bitcoin a un indirizzo che non appartiene a un destinatario.                              |
| bitcoin versus Bitcoin                          | Bitcoin è la rete monetaria, e bitcoin (minuscolo) è un'unità monetaria sulla rete Bitcoin. Utilizzi la valuta bitcoin o un token per effettuare transazioni sulla rete Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Blocco                                          | Un blocco è una struttura dati nella blockchain di Bitcoin che consiste in un'intestazione e un corpo di transazioni Bitcoin. Il blocco è contrassegnato da un timestamp e si impegna su un specifico predecessore (blocco genitore). Quando viene hashata, l'intestazione del blocco fornisce la prova del lavoro che rende la blockchain probabilisticamente immutabile. I blocchi devono aderire alle regole applicate dal consenso della rete per estendere la blockchain. Quando un blocco viene aggiunto alla blockchain, le transazioni incluse ricevono la prima conferma.                                                                                                                                                                                                                                                                                                                                            |
| Esploratore di Blocchi                          | Uno strumento online che ti consente di cercare informazioni in tempo reale e storiche su una blockchain, inclusi dati relativi a blocchi, transazioni, indirizzi e altro.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Hash del Blocco                                 | L'hash del blocco è l'hash SHA-256 dei dati del blocco, ed è solitamente rappresentato in formato esadecimale. Un hash del blocco può essere interpretato come un numero molto grande. Per soddisfare il requisito della Prova di Lavoro (Proof-of-Work), un hash del blocco deve essere inferiore a una certa soglia. Pertanto, tutti gli hash dei blocchi iniziano con una serie di zeri seguiti da una stringa alfanumerica. Alcuni blocchi hanno fino a venti zeri iniziali, mentre i blocchi più vecchi ne hanno pochi come otto. Il numero di zeri richiesti dimostra approssimativamente la difficoltà di mining al momento della pubblicazione del blocco.                                                                                                                                                                                                                                                                               |
| Altezza del Blocco                              | Ogni blocco è numerato in ordine ascendente, a partire da zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Ricompensa del Blocco                           | Consiste nel sussidio del blocco (bitcoin appena creati) e nella somma di tutte le commissioni sulle transazioni incluse nel blocco.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Dimensione del Blocco                           | Ogni blocco ha una quantità limitata di dati che può contenere. I dati che non rientrano in un determinato blocco verranno registrati in uno dei blocchi successivi. Per quanto riguarda i blocchi bitcoin, inizialmente avevano una dimensione di 1mb, tuttavia, dopo un soft fork, la dimensione del blocco può tecnicamente contenere fino a 4mb di dati.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Sussidio del Blocco                             | La quantità di nuovi bitcoin coniati in ogni blocco. Ogni blocco che viene prodotto e aggiunto alla blockchain permette al creatore del blocco di coniare una certa quantità di nuovi bitcoin. Il sussidio è iniziato con 50 BTC per blocco, ed è dimezzato ogni 210.000 blocchi o circa ogni 4 anni.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Blockchain                                      | Un registro distribuito, o database, di tutte le transazioni Bitcoin. Le transazioni sono raggruppate in aggiornamenti discreti chiamati blocchi, limitati fino a 4 milioni di unità di peso. I blocchi sono prodotti approssimativamente ogni 10 minuti tramite un processo stocastico chiamato mining. Ogni blocco include una "prova di lavoro" computazionalmente intensiva. Il requisito della prova di lavoro è utilizzato per regolare gli intervalli dei blocchi e proteggere la blockchain da attacchi volti a riscrivere la storia: un attaccante avrebbe bisogno di superare la prova di lavoro esistente per sostituire i blocchi già pubblicati, rendendo ogni blocco probabilisticamente immutabile man mano che viene sepolto sotto i blocchi successivi.                                                                                                                                                                         |
| BTCPAY Server Vault                             | Per un equilibrio ottimale tra facilità d'uso, sicurezza e privacy, si raccomanda di utilizzare BTCPay Server Wallet con un hardware wallet. BTCPay Vault è costruito per fare da ponte tra l'Hardware Wallet e BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Problema dei Generali Bizantini                 | Un problema della teoria dei giochi che descrive la difficoltà che hanno le parti decentralizzate nel raggiungere un consenso senza fare affidamento su una parte centrale di fiducia. Il nome deriva dallo scenario di diversi generali che assediano Bisanzio. Hanno circondato la città, ma devono decidere collettivamente quando attaccare. Se tutti i generali attaccano allo stesso tempo, vinceranno, ma se attaccano in momenti diversi, perderanno. I generali non hanno canali di comunicazione sicuri tra loro perché qualsiasi messaggio inviato o ricevuto potrebbe essere stato intercettato o inviato errato dai difensori di Bisanzio. Come possono i generali organizzarsi per attaccare contemporaneamente?                                                                                                                                                                                                          |
| Censura                                         | Controllo su quali informazioni possono essere trasmesse alle masse. Quando si parla di bitcoin, la censura riguarda la capacità di fermare la transazione da parte di terzi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Resto                                           | La parte di UTXO restituita al portafoglio del mittente, tramite un indirizzo diverso. Corrisponde alla somma degli input meno l'importo speso e la commissione sulla transazione.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Child Pays For Parent (CPFP)                    | Una tecnica di aumento della commissione in cui un utente spende un output da una transazione non confermata a bassa tariffa in una transazione figlia con una tariffa alta per incoraggiare i miners a includere entrambe le transazioni in un blocco.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Coinbase Transaction                            | La primissima transazione in ogni blocco che distribuisce la ricompensa del blocco e le commissioni di transazione a chi ha minato il blocco.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Coincidence of Wants                            | Un fenomeno economico dove due parti detengono ciascuna un oggetto che l'altra desidera, quindi scambiano questi oggetti direttamente senza alcun mezzo monetario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Cold Storage                                    | Un modo per gestire dati senza essere connessi a Internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Cold Wallet                                     | Un tipo di portafoglio bitcoin che conserva in modo sicuro le tue chiavi private offline, solitamente su un dispositivo fisico. Conosciuto anche come hardware wallet, protegge i tuoi bitcoin digitali dagli hacker online usando un dispositivo simile a una chiavetta USB che non è connesso a Internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Command Line Interface (CLI)                    | Interazione con un dispositivo o programma computerizzato con comandi da parte di un utente o client, e risposte dal dispositivo o programma, sotto forma di linee di testo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Commitment Transaction                          | Una transazione di impegno è una transazione Bitcoin, firmata da entrambi i partner del canale, che codifica il saldo più recente di un canale. Ogni volta che viene effettuato o inoltrato un nuovo pagamento utilizzando il canale, il saldo del canale si aggiornerà e una nuova transazione di impegno verrà firmata da entrambe le parti. Importante, in un canale tra Alice e Bob, entrambi conservano la loro versione della transazione di impegno, che è anche firmata dall'altra parte. In qualsiasi momento, il canale può essere chiuso da Alice o Bob se presentano la loro transazione di impegno alla blockchain di Bitcoin. Presentare una transazione di impegno più vecchia (datata) è considerato barare (cioè, una violazione del protocollo) su Lightning Network e può essere penalizzato dall'altra parte, reclamando tutti i fondi nel canale per sé stessi, tramite una transazione di penalità.                     |
| Confirmation                                    | Una volta che una transazione è inclusa in un blocco, ha una conferma. Non appena viene estratto un altro blocco sulla blockchain, la transazione ha due conferme, e così via. Sei o più conferme sono considerate una prova sufficiente che una transazione non può essere invertita.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Crowdfund (CF)                                  | Un plugin predefinito di BTCPay Server che consente al proprietario di un negozio di creare facilmente un sito web di crowdfunding tipico. Possono facilmente impostare un obiettivo, creare vantaggi per i contributi e personalizzarlo secondo le loro esigenze.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Cryptography                                    | Un sistema speciale, dove il messaggio originale viene modificato in modo che solo i destinatari previsti possano riceverlo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Dashboard                                       | La pagina principale di BTCPay Server. Fornisce una panoramica di tutta l'attività per un negozio, visualizzata attraverso una serie di riquadri riassuntivi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Demo                                            | Si riferisce all'ambiente virtuale in cui si svolgono le dimostrazioni del software.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Deployment                                      | Il deployment del software comprende tutte le attività che rendono un sistema software disponibile per l'uso. Il processo generale di deployment consiste in diverse attività interrelate con possibili transizioni tra di loro.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Percorso di Derivazione                         | Un pezzo di dati che indica ad un portafoglio Deterministico Gerarchico (HD) come derivare una chiave specifica all'interno di un albero di chiavi. I percorsi di derivazione sono utilizzati come standard Bitcoin e sono stati introdotti con i portafogli HD come parte del BIP 32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Regolazione della Difficoltà                    | Regolazione del target di difficoltà, ogni 2016 blocchi (circa due settimane) per cercare di assicurare che i blocchi vengano minati una volta ogni 10 minuti in media. Crea quindi un tempo consistente tra i blocchi e un'emissione consistente di nuovi bitcoin nella rete (tramite la ricompensa del blocco).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Target di Difficoltà                            | Utilizzato nel mining, è un numero che l'hash di un blocco deve essere inferiore affinché il blocco sia aggiunto alla blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Firma Digitale                                  | Una firma digitale è uno schema matematico per verificare l'autenticità e l'integrità di messaggi o documenti digitali. Può essere vista come un impegno crittografico in cui il messaggio non è nascosto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Divisibile                                      | La proprietà di un bene che può essere suddiviso in quantità minori senza perdere valore. Poiché le transazioni economiche avvengono frequentemente in quantità variabili, una valuta deve essere divisibile per essere utilizzata ampiamente in un'economia.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Docker                                          | Software che impacchetta il software in unità standardizzate chiamate container che hanno tutto ciò che il software necessita per funzionare, inclusi librerie, strumenti di sistema, codice e runtime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Doppia Spesa                                    | La possibilità di spendere gli stessi fondi due volte. Bitcoin protegge dalla doppia spesa verificando che ogni transazione aggiunta alla blockchain aderisca alle regole del consenso; ciò significa controllare che gli input per la transazione non siano stati precedentemente spesi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Durabilità                                      | Proprietà del denaro, in cui la valuta può mantenere il suo stato originale nel tempo e resistere a usi ripetuti. Una valuta duratura deve essere in grado di sopravvivere a danni potenziali.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Electrum                                        | Electrum è uno dei portafogli Bitcoin più popolari, creato nel 2011.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Chiave pubblica estesa (Xpub)                   | Chiave pubblica estesa, nota anche come Xpub, una chiave pubblica che funge da genitore per chiavi derivate dall'Xpub come caratteristica del portafoglio HD. Questa Xpub è uno standard introdotto nel BIP 32. I portafogli la utilizzano dietro le quinte per derivare chiavi pubbliche. La condivisione dell'Xpub non è consigliata, i tuoi fondi non saranno comunque a rischio diretto di essere spostati, l'Xpub non può derivare chiavi private. Il vantaggio della condivisione di un Xpub potrebbe essere per scopi di crowdfunding in BTCPay Server. L'Xpub viene condiviso tramite mezzi online, mentre le chiavi private rimangono offline su un HWW.                                                                                                                                                                                                                                                                                  |
| F.U.D.                                          | Acronimo per Paura, incertezza e dubbio; solitamente evocato intenzionalmente per mettere un concorrente in svantaggio.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Commissione                                     | Nel contesto di Lightning Network, i nodi addebiteranno commissioni di routing per inoltrare i pagamenti di altri utenti. I singoli nodi possono impostare le proprie politiche di commissione che saranno calcolate come la somma di una commissione base fissa e una tariffa che dipende dall'importo del pagamento. Nel contesto di Bitcoin, il mittente di una transazione paga una commissione di transazione ai minatori per includere la transazione in un blocco. Le commissioni di transazione Bitcoin non includono una commissione base e dipendono linearmente dal peso della transazione, ma non dall'importo.                                                                                                                                                                                                                                                                                                                   |
| Fiat                                            | Valuta emessa dal governo che non è supportata da una merce come l'oro.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Finite                                          | Si riferisce alla fornitura limitata di Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Fork                                            | Un cambiamento al protocollo o a un pezzo di codice. I fork sono solitamente introdotti per aggiornare un progetto. Nella comunità open source, i fork esistono perché molte persone scelgono di scaricare ed eseguire lo stesso software in momenti diversi e non aggiornano sempre. Se due utenti scaricano ed eseguono la versione 1 di un software, e solo un utente aggiorna quando viene rilasciata la versione 2, l'utente che ha aggiornato sta eseguendo un fork della versione 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Funding Transaction                             | Transazione utilizzata per aprire un canale di pagamento. Il valore (in bitcoin) della transazione di finanziamento corrisponde esattamente alla capacità del canale di pagamento. L'output della transazione di finanziamento è uno script multisignature 2-di-2 (multisig) dove ogni partner del canale controlla una chiave. Data la sua natura multisig, può essere speso solo di comune accordo tra i partner del canale. Sarà eventualmente speso da una delle transazioni di impegno o dalla transazione di chiusura.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Fungible                                        | Qualcosa (come denaro o una merce) di natura tale che una parte o quantità possa essere sostituita da un'altra parte o quantità uguale nel pagare un debito o regolare un conto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Gap Limit                                       | Si riferisce al numero standard di indirizzi pubblici che vengono controllati per transazioni nella blockchain al fine di calcolare il saldo di un account. Le transazioni ricevute su un indirizzo oltre il limite di gap degli indirizzi non vengono rilevate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Genesis Block                                   | Primo blocco nella blockchain di Bitcoin. Satoshi Nakamoto, il creatore di Bitcoin, ha minato il blocco Genesis il 3 gennaio 2009 e ha incluso il titolo del Financial Times di quel giorno, “Chancellor on brink of second bailout for banks” (Cancelliere sull'orlo del secondo salvataggio per le banche).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Github                                          | Una piattaforma e servizio basato su cloud per lo sviluppo software e il controllo versione usando Git, che consente agli sviluppatori di memorizzare e gestire il loro codice.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Gossip Protocol                                 | I nodi LN inviano e ricevono informazioni sulla topologia di Lightning Network attraverso messaggi di gossip che vengono scambiati con i loro peer. Il protocollo di gossip è principalmente definito in BOLT #7 e definisce il formato dei messaggi node_announcement, channel_announcement e channel_update. Per prevenire lo spam, i messaggi di annuncio dei nodi saranno inoltrati solo se il nodo ha già un canale, e i messaggi di annuncio dei canali saranno inoltrati solo se la transazione di finanziamento del canale è stata confermata dalla rete Bitcoin. Solitamente, i nodi Lightning si connettono con i loro partner di canale, ma è possibile connettersi con qualsiasi altro nodo Lightning per elaborare messaggi di gossip.                                                                                                                                                                                           |
| Gresham's Law                                   | Legge secondo cui “il denaro cattivo scaccia quello buono”. In altre parole, in un'economia dove sono in uso due valute, gli individui spenderanno il denaro cattivo, che si svaluta costantemente, e terranno il denaro buono, che mantiene il suo valore. Così, il denaro cattivo dominerà in termini di circolazione e uso nelle transazioni quotidiane, mentre il denaro buono dominerà in termini di risparmi e investimenti a lungo termine.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Halving                                         | Un evento che dimezza il tasso di emissione di bitcoin ogni 210.000 blocchi (circa ogni quattro anni).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Hard Fork                                       | Una modifica del consenso che non è compatibile con le versioni precedenti. L'incompatibilità con le versioni precedenti si verifica quando un comportamento precedentemente invalido viene reso valido. Per mantenere il consenso attraverso un hard fork, tutti i nodi devono aggiornarsi. Altrimenti, i nodi vecchi rifiuteranno le transazioni o i blocchi come non validi secondo le vecchie regole, mentre i nodi aggiornati li accetteranno come validi. Per questa ragione, i hard fork sono evitati a tutti i costi in Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Hardware Wallet (HWW)                           | Un tipo speciale di portafoglio Bitcoin che memorizza le chiavi private dell'utente in un dispositivo hardware sicuro.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Hash Function                                   | Una funzione hash crittografica è un algoritmo matematico che mappa dati di dimensione arbitraria in una stringa di bit di dimensione fissa (un hash) ed è progettata per essere una funzione unidirezionale, ovvero, una funzione difficile da invertire. L'unico modo per ricreare i dati di input dall'output di una funzione hash crittografica ideale è tentare una ricerca di input possibili per vedere se producono una corrispondenza.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Hash Rate                                       | Una misura di quanti hash i minatori producono cumulativamente al secondo sulla rete Bitcoin. Un singolo hash è un tentativo di creare una Prova di Lavoro per un blocco.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Hot Wallet                                      | Un dispositivo con connessioni esterne, specialmente a internet. Un hot wallet è un portafoglio Bitcoin che si collega a internet. Questi portafogli sono più comodi per le spese quotidiane, ma non sono sicuri come le opzioni di cold storage perché interagiscono con internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Initial Block Download (IBD)                    | Il download iniziale dell'intera blockchain di Bitcoin da zero. Quando un nuovo nodo viene configurato e si unisce alla rete, si collega ad altri nodi e chiede loro i blocchi. Il nuovo nodo elabora questi blocchi e costruisce la blockchain fino a quando non ha raggiunto e sincronizzato con la rete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Invoice                                         | Un documento commerciale emesso da un venditore a un acquirente relativo a una transazione di vendita e che indica i prodotti, le quantità e i prezzi concordati per i prodotti o servizi forniti dal venditore all'acquirente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Know Your Customer (KYC)                        | Leggi intese a prevenire l'uso delle istituzioni finanziarie per trasferimenti di denaro illeciti, imponendo che tutti i conti finanziari siano identificabili a individui o organizzazioni.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Layer 2                                         | Una rete costruita sopra una blockchain, ad esempio, Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Legacy Address                                  | Gli indirizzi legacy usano Base58, e quando un indirizzo legacy è l'hash di una chiave pubblica, un cosiddetto indirizzo P2PKH, inizia con un ‘1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Lightning Network                               | Un protocollo sopra Bitcoin. Crea una rete di canali di pagamento che consente l'inoltro fiduciario dei pagamenti attraverso la rete con l'aiuto di HTLCs e onion routing. Altri componenti di Lightning Network sono il protocollo gossip, lo strato di trasporto e le richieste di pagamento.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Liquidity                                       | Misura di diverse caratteristiche di un particolare asset in un dato mercato. La liquidità è un indicatore di quanto un grande ordine avrà impatto sul prezzo di un asset. Un asset con più liquidità ha una maggiore profondità del libro ordini. Ciò significa che sarà in grado di assorbire più ordini con movimenti di prezzo minori.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Catena più Lunga                                | La catena di blocchi che ha richiesto più sforzo per essere costruita. Viene chiamata così perché intuitivamente una blockchain con più blocchi richiederà più energia per essere costruita rispetto ad una catena con meno blocchi, ma più precisamente è la catena che ha richiesto più lavoro per essere prodotta, quindi un nome migliore potrebbe essere stato "catena più pesante".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Catena Principale                               | Nel contesto di Lightning Network, si riferisce alla Rete Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Mezzo di Scambio                                | Un tipo di bene che facilita lo scambio di altri beni e servizi all'interno di un'economia. Storicamente, oggetti come conchiglie, perline e oro sono stati utilizzati come mezzi di scambio.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Mempool                                         | Abbreviazione di "memory pool", è uno spazio di archiviazione temporaneo per le transazioni che sono state ricevute da un nodo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Miner                                           | Un nodo impegnato nel processo di costruzione della blockchain aggiungendo nuovi blocchi attraverso il processo di hashing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Mining                                          | Processo di costruzione di un blocco a partire dalle transazioni recenti Bitcoin e poi risolvendo un problema computazionale richiesto come prova di lavoro. È il processo attraverso il quale il registro condiviso di bitcoin (cioè, la blockchain) viene aggiornata e attraverso il quale nuove transazioni vengono incluse nel registro. È anche il processo attraverso il quale viene emesso nuovo bitcoin. Ogni volta che viene creato un nuovo blocco, il nodo di mining riceverà nuovo bitcoin creato all'interno della transazione coinbase di quel blocco.                                                                                                                                                                                                                                                                                                                                                                  |
| Multifirma (multisig)                           | Uno script che richiede più di una firma per autorizzare la spesa. I canali di pagamento sono sempre codificati come indirizzi multisig che richiedono una firma da ciascun partner del canale di pagamento. Nel caso standard di un canale di pagamento a due parti, viene utilizzato un indirizzo multisig 2-di-2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Nodo                                            | Un computer che partecipa a una rete. In particolare le reti Bitcoin o Lightning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output                                          | Pacchetto di bitcoin creato in una transazione bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Blocco di Output                                | Un insieme di requisiti posti su un output. Questi requisiti devono essere soddisfatti per poter utilizzare l'output in una transazione. L'esempio più comune è un semplice requisito di avere la chiave privata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Indirizzo P2SH                                  | Gli indirizzi P2SH sono codifiche Base58Check del hash a 20 byte di uno script. Gli indirizzi P2SH iniziano con un "3". Gli indirizzi P2SH nascondono tutta la complessità, in modo che il mittente di un pagamento non veda lo script.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Indirizzo P2WPKH                                | Il formato di indirizzo "native SegWit v0", gli indirizzi P2WPKH sono codificati in bech32 e iniziano con "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Indirizzo P2WSH                                 | Il formato di indirizzo script "native SegWit v0", gli indirizzi P2WSH sono codificati in bech32 e iniziano con "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Transazione Bitcoin Parzialmente Firmata (PSBT) | Uno standard Bitcoin che facilita la portabilità delle transazioni non firmate, permettendo a più parti di firmare facilmente la stessa transazione. Questo è più utile quando più parti desiderano aggiungere input alla stessa transazione. PSBT è stato introdotto da BIP 174 e consente agli utenti di firmare più facilmente le transazioni su un dispositivo di cold storage e poi trasmettere la transazione firmata da un dispositivo connesso a Internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Pathfinding                                     | Il processo di ricerca di un percorso per il pagamento dalla sorgente alla destinazione in Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Pay-to-Public-Key-Hash (P2PKH)                  | P2PKH è un tipo di output che blocca i bitcoin sull'hash di una chiave pubblica. Un output bloccato da uno script P2PKH può essere sbloccato (speso) presentando la chiave pubblica corrispondente all'hash e una firma digitale creata dalla chiave privata corrispondente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Pay-to-Script-Hash (P2SH)                       | P2SH è un tipo di output versatile che consente l'uso di script Bitcoin complessi. Con P2SH, lo script complesso che dettaglia le condizioni per spendere l'output (redeem script) non è presentato nello script di blocco. Invece, il valore è bloccato sull'hash di uno script, che deve essere presentato e soddisfatto per spendere l'output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Pay-to-Taproot (P2TR)                           | Attivato nel novembre 2021, Taproot è un nuovo tipo di output che blocca i bitcoin su un albero di condizioni di spesa, o una singola condizione radice.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Pay-to-Witness-Public-Key-Hash (P2WPKH)         | P2WPKH è l'equivalente SegWit di P2PKH, utilizzando un testimone segregato. La firma per spendere un output P2WPKH è inserita nell'albero dei testimoni invece che nel campo ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Pay-to-Witness-Script-Hash (P2WSH)              | P2WSH è l'equivalente SegWit di P2SH, utilizzando un testimone segregato. La firma e lo script per spendere un output P2WSH sono inseriti nell'albero dei testimoni invece che nel campo ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Payjoin                                         | Un tipo speciale di transazione Bitcoin dove sia il mittente che il destinatario contribuiscono con input al fine di eludere l'euristica di proprietà di input comune, un'assunzione utilizzata per violare la privacy degli utenti bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Payment Channel                                 | Una relazione finanziaria tra due nodi sulla Lightning Network, creata utilizzando una transazione bitcoin che paga un indirizzo multisignature. I partner del canale possono utilizzare il canale per inviare bitcoin avanti e indietro tra loro senza registrare tutte le transazioni sulla blockchain di Bitcoin. In un tipico canale di pagamento, solo due transazioni, la transazione di finanziamento e la transazione di impegno, sono aggiunte alla blockchain. I pagamenti inviati attraverso il canale non sono registrati nella blockchain e si dice che avvengano "off-chain".                                                                                                                                                                                                                                                                                                                                                      |
| Payment Request                                 | Una funzionalità che consente ai proprietari di negozi BTCPay di creare fatture di lunga durata. I fondi pagati a una richiesta di pagamento utilizzano il tasso di cambio al momento del pagamento. Ciò consente agli utenti di effettuare pagamenti a loro convenienza senza dover negoziare o verificare i tassi di cambio con il proprietario del negozio al momento del pagamento.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Payout                                          | La funzionalità di payout è legata ai Pagamenti Pull. Questa funzionalità consente di elaborare pagamenti pull (rimborsi, pagamenti di stipendi o prelievi).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Plugin                                          | Un add-on software che viene installato su un programma, migliorandone le capacità.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Point Of Sale (PoS)                             | Un plugin predefinito di BTCPay Server che consente a un proprietario di negozio di creare un negozio online direttamente da BTCPay Server. Il proprietario del negozio non ha bisogno di soluzioni di ecommerce di terze parti per gestire un negozio online.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Portabilità                                     | Capacità di un bene di essere facilmente trasportato nello spazio. La portabilità è una caratteristica importante del denaro solido; affinché una moneta sia ampiamente adottata, e quindi utilizzabile, deve essere in grado di muoversi attraverso confini, tra individui e su lunghe distanze con relativa facilità.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Proof Of Work (PoW)                             | Dati che richiedono un calcolo significativo per essere trovati e che possono essere facilmente verificati da chiunque per dimostrare la quantità di lavoro che è stata necessaria per produrli. In Bitcoin, i minatori devono trovare una soluzione numerica all'algoritmo SHA-256 che soddisfi un obiettivo condiviso dalla rete, chiamato target di difficoltà.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Pseudonimo                                      | Un nome fittizio utilizzato da individui per proteggere la loro identità o costruire una reputazione separata dalla loro vera identità. Le chiavi pubbliche sono utilizzate per consentire agli utenti di Bitcoin di ricevere bitcoin rimanendo pseudonimi rispetto alla blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Crittografia a Chiave Pubblica                  | Coinvolge una coppia di chiavi nota come chiave pubblica e chiave privata, che sono associate a un'entità che ha bisogno di autenticare la sua identità elettronicamente o di firmare o criptare dati. La chiave pubblica viene pubblicata e la corrispondente chiave privata viene tenuta segreta. I dati criptati con la chiave pubblica possono essere decifrati solo con la corrispondente chiave privata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Chiave Pubblica/Privata                         | Coppia di chiavi utilizzata nella crittografia a chiave pubblica. La chiave pubblica è condivisa con altri apertamente e può essere considerata come un numero di conto, mentre la chiave privata è tenuta segreta e può essere considerata come una password.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Pagamento Pull                                  | Tradizionalmente, per effettuare un pagamento in Bitcoin, il ricevente condivide il proprio indirizzo bitcoin e il mittente invia successivamente denaro a questo indirizzo. Tale sistema è chiamato pagamento push poiché il mittente inizia il pagamento mentre il ricevente può essere non disponibile, di fatto spingendo il pagamento al ricevente. Invece dello scenario tipico di un mittente che "spinge" il pagamento, il mittente consente al ricevente di prelevare il pagamento nel momento in cui lo ritiene opportuno.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Buco del Coniglio                               | Un riferimento a Alice Nel Paese Delle Meraviglie dove l'eroe inizia un'avventura entrando in un buco del coniglio. All'interno di Bitcoin si riferisce agli argomenti apparentemente infiniti che uno esplora e vede sotto una nuova luce una volta che ha iniziato a comprendere Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Ricevere                                        | Il processo di ricevere bitcoin inviati a un indirizzo fornito.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Registrare                                      | Il processo di creazione di un account o di registrazione a un servizio, tipicamente fatto scegliendo un nome utente e una password.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Replace By Fee (RBF)                            | Una transazione Bitcoin può essere designata come RBF al fine di consentire al mittente di sostituire questa transazione con un'altra transazione simile che paga una commissione più alta. Questo meccanismo esiste per consentire agli utenti di rispondere se la rete diventa congestionata e le commissioni aumentano inaspettatamente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Repository                                      | Nei sistemi di controllo versione, un repository è una struttura dati che memorizza i metadati per un insieme di file o una struttura di directory. A seconda che il sistema di controllo versione in uso sia distribuito, come Git o Mercurial, o centralizzato, come Subversion, CVS o Perforce, l'intero insieme di informazioni nel repository può essere duplicato su ogni sistema dell'utente o può essere mantenuto su un singolo server. Alcuni dei metadati che un repository contiene includono, tra le altre cose, un record storico delle modifiche nel repository, un insieme di oggetti commit e un insieme di riferimenti agli oggetti commit, chiamati heads.                                                                                                                                                                                                                                                                    |
| Rescan                                          | Processo di scansione dello stato corrente del set UTXO per monete appartenenti a uno schema di derivazione precedentemente configurato.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Revokation Key                                  | Ogni Revocable Sequence Maturity Contract (RSMC) contiene due chiavi di revoca. Ogni partner del canale conosce una chiave di revoca. Conoscendo entrambe le chiavi di revoca, l'output del RSMC può essere speso entro il timelock predefinito. Durante la negoziazione di un nuovo stato del canale, le vecchie chiavi di revoca vengono condivise, "revocando" così lo stato vecchio. Le chiavi di revoca sono utilizzate per scoraggiare i partner del canale dal trasmettere uno stato del canale vecchio.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Routing                                         | Il processo di utilizzo del percorso della Lightning Network per effettuare pagamenti.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Routing Fees                                    | Nella Lightning Network, le commissioni addebitate per inoltrare i pagamenti di altri utenti. I nodi individuali possono impostare le proprie politiche di commissione che saranno calcolate come la somma di una base_fee fissa e una fee_rate che dipende dall'importo del pagamento.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Salability                                      | La facilità con cui un bene può essere venduto sul mercato ogni volta che il suo detentore lo desidera, con la minima perdita nel suo prezzo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Satoshi (sat)                                   | Un satoshi è la più piccola unità (denominazione) di bitcoin che può essere registrata sulla blockchain. Un satoshi equivale a 1/100 milionesimo (0,00000001) di un bitcoin ed è nominato in onore del creatore di Bitcoin, Satoshi Nakamoto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Satoshi Nakamoto                                | Il nome utilizzato dalla persona o dal gruppo di persone che hanno progettato Bitcoin e creato la sua implementazione di riferimento originale. Come parte dell'implementazione, hanno anche ideato il primo database blockchain. Nel processo, sono stati i primi a risolvere il problema del doppio-spending per la valuta digitale. La loro vera identità rimane sconosciuta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Satoshi Per Byte                                | Un'unità per misurare la priorità della transazione, definita dalla commissione della transazione in satoshi divisa per la dimensione della transazione in byte.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Satoshi Per Verabyte                            | Concetto simile a Satoshi Per Byte, ma per indirizzi più recenti che utilizzano Segwit. Equivale alla dimensione della transazione in unità di peso divisa per 4. Le unità di peso sono calcolate prendendo la dimensione della transazione (senza il testimone) moltiplicata per 3, aggiunta alla dimensione della transazione inclusa il testimone.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Scarcity                                        | Proprietà di un bene che non può essere replicato senza costi. La scarsità non dipende dal numero di unità esistenti di un bene, ma piuttosto dalla costosità della produzione di ulteriori unità.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Script                                          | Bitcoin utilizza un sistema di scripting per le transazioni chiamato Bitcoin Script. Assomigliando al linguaggio di programmazione Forth, è semplice, basato su stack ed elaborato da sinistra a destra. È intenzionalmente Turing-incompleto, senza cicli o ricorsioni.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Seed Phrase                                     | Un elenco di parole che memorizza tutte le informazioni necessarie per recuperare i fondi Bitcoin on-chain. Il software del portafoglio genererà tipicamente una frase seed e istruirà l'utente a scriverla su carta. Se il computer dell'utente si rompe o il suo disco rigido diventa corrotto, possono scaricare nuovamente lo stesso software del portafoglio e utilizzare il backup su carta per recuperare i loro bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Segregated Witness (SegWit)                     | Segregated Witness (SegWit) è un aggiornamento del protocollo Bitcoin introdotto nel 2017 che aggiunge un nuovo campo di testimoni per firme e altre prove di autorizzazione delle transazioni. Questo nuovo campo testimone è esente dal calcolo dell'ID della transazione, il che risolve la maggior parte delle classi di malleabilità delle transazioni da parte di terzi. Segregated Witness è stato implementato come un soft fork ed è un cambiamento che tecnicamente rende le regole del protocollo di Bitcoin più restrittive.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Self-Sovereignty                                | Un modello per la gestione delle identità digitali in cui individui o aziende hanno la piena proprietà e la capacità di controllare i propri account e dati personali.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Send                                            | Il processo di invio di bitcoin a un indirizzo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Sensitivity Mode                                | Attivato tramite un'interruttore nelle impostazioni del negozio, l'attivazione comporta l'oscuramento dei valori numerici (ad es., quantità di bitcoin) in tutte le visualizzazioni.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Server Settings                                 | Impostazioni all'interno di BTCPay Server che si applicano a livello di server (a differenza delle impostazioni del negozio che sono limitate in ambito a un singolo negozio).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SHA-256                                         | Una funzione di hash crittografica. Membro di una famiglia di funzioni di hash chiamate funzioni Secure Hashing Algorithm (SHA).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Shopify                                         | Una multinazionale canadese di e-commerce con sede a Ottawa, Ontario. Shopify è il nome della sua piattaforma di e-commerce proprietaria per negozi online e sistemi di vendita al dettaglio.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| SMTP                                            | Simple Mail Transfer Protocol è uno standard di comunicazione Internet per la trasmissione di posta elettronica.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Soft Fork                                       | Un aggiornamento del protocollo compatibile sia in avanti che indietro, che consente sia ai nodi vecchi che a quelli nuovi di continuare a utilizzare la stessa catena.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Software Stack                                  | In informatica, un software stack o solution stack è un insieme di sottosistemi o componenti software necessari per creare una piattaforma completa tale che nessun software aggiuntivo sia necessario per supportare le applicazioni.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Store                                           | Un negozio all'interno di BTCPay Server può essere visto come una "Casa" per un specifico portafoglio bitcoin, estendendosi con tutte le funzionalità di BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Store Settings                                  | Impostazioni all'interno di BTCPay Server specifiche per un negozio.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Taproot                                         | Aggiornamento di Bitcoin che introdurrebbe diverse nuove funzionalità. L'aggiornamento è descritto nei BIPs 340, 341 e 342, e introduce lo schema di firma Schnorr, Taproot e Tapscript. Insieme, questi aggiornamenti introducono nuovi modi più efficienti, flessibili e privati di trasferire bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Thier's Law                                     | Legge secondo la quale il denaro buono scaccia il denaro cattivo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Third-Party Host                                | Quando un sito web di un individuo o di un'azienda è gestito su server di proprietà e gestiti da un'altra impresa. L'alternativa è avere il proprio sito web ospitato sui propri server nel proprio data center.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Timelock                                        | Un timelock è un tipo di vincolo che limita la spesa di alcuni bitcoin fino a un tempo futuro specificato o all'altezza di un blocco. I timelock sono prominenti in molti contratti Bitcoin, inclusi i canali di pagamento e gli HTLCs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Topologia                                       | La topologia di Lightning Network descrive la forma di Lightning Network come un grafo matematico. I nodi del grafo sono i nodi Lightning (partecipanti alla rete/peer). Gli archi del grafo sono i canali di pagamento. La topologia di Lightning Network viene trasmessa pubblicamente con l'aiuto del protocollo gossip, ad eccezione dei canali non annunciati. Questo significa che Lightning Network potrebbe essere significativamente più grande del numero annunciato di canali e nodi. Conoscere la topologia è di particolare interesse nel processo di routing basato sulla sorgente dei pagamenti in cui il mittente scopre una rotta.                                                                                                                                                                                                                                                                                  |
| Transazione                                     | Le transazioni sono strutture dati utilizzate da Bitcoin per trasferire bitcoin da un indirizzo all'altro. Diverse migliaia di transazioni sono aggregate in un blocco, che viene poi registrato (minato) sulla blockchain. La prima transazione in ogni blocco, chiamata transazione coinbase, genera nuovi bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ID Transazione                                  | Una stringa di lettere e numeri che identifica una specifica transazione sulla blockchain. La stringa è semplicemente il doppio hash SHA-256 di una transazione. Questo hash può essere utilizzato per cercare una transazione su un nodo o un esploratore di blocchi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Autenticazione a Due Fattori (2FA)              | Un metodo di sicurezza per la gestione dell'identità e dell'accesso che richiede due forme di identificazione per accedere a risorse e dati, spesso con un dispositivo secondario in aggiunta alla password di login standard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Non Censurabile                                 | Proprietà per cui nessuna entità ha la capacità di invertire una transazione Bitcoin o mettere in blacklist un portafoglio o un indirizzo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Non Confiscabile                                | Proprietà per cui nessuna entità può prendere bitcoin da un'entità contro la loro volontà.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Output di Transazione Non Spesi (UTXO)          | Output non ancora spesi, quindi disponibili per essere utilizzati in nuove transazioni.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Esperienza Utente (UX)                          | Come un utente interagisce con e sperimenta un prodotto, sistema o servizio. Include le percezioni di una persona sull'utilità, facilità d'uso ed efficienza.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Interfaccia Utente (UI)                         | Il punto di interazione e comunicazione uomo-computer in un dispositivo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Verificabile                                    | Proprietà di un bene che può essere facilmente differenziato da impostori e falsificazioni.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Virtuale                                        | Che esiste o è simulato su un computer o una rete informatica.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Macchina Virtuale (VM)                          | In informatica, una macchina virtuale è la virtualizzazione o emulazione di un sistema informatico. Le macchine virtuali si basano su architetture informatiche e forniscono la funzionalità di un computer fisico. Le loro implementazioni possono coinvolgere hardware specializzato, software, o una combinazione dei due.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Server Privato Virtuale                         | Un server privato virtuale è una macchina virtuale venduta come servizio da un servizio di hosting Internet. Il termine "server dedicato virtuale" ha un significato simile. Un server privato virtuale esegue la propria copia di un sistema operativo, e i clienti possono avere accesso a livello di superutente a quell'istanza del sistema operativo, quindi possono installare quasi qualsiasi software che funziona su quel sistema operativo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Volatilità                                      | Misura del grado di variazione nel prezzo di un asset nel tempo. Gli asset che sperimentano grandi variazioni di prezzo regolarmente sono più volatili, mentre gli asset che hanno un prezzo più stabile sono meno volatili.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Portafoglio                                     | I portafogli Bitcoin contengono le chiavi di un utente, permettendo agli utenti di ricevere bitcoin, firmare transazioni e controllare il saldo del proprio conto. Le chiavi private e pubbliche contenute in un portafoglio Bitcoin svolgono due funzioni distinte, ma sono legate insieme nella creazione. I portafogli Bitcoin contengono le chiavi di un utente, non i loro bitcoin effettivi. Concettualmente, un portafoglio è come un portachiavi nel senso che contiene molte coppie di chiavi private e pubbliche. Queste chiavi sono utilizzate per firmare transazioni, permettendo a un utente di dimostrare di possedere gli output delle transazioni sulla blockchain, ovvero i loro bitcoin. Tutti i bitcoin sono registrati sulla blockchain sotto forma di output di transazioni.                                                                                                                                               |
| Wasabi Wallet                                   | Un portafoglio Bitcoin open-source, non custodial e focalizzato sulla privacy per Desktop che implementa CoinJoin senza fiducia.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Portafoglio Solo-Lettura                        | Portafogli Bitcoin che permettono di tenere traccia dei propri bitcoin in cold storage disabilitando la possibilità di spendere fondi. Questo perché i portafogli solo-lettura non memorizzano o utilizzano chiavi private e, quindi, sono incapaci di autorizzare qualsiasi spesa per conto dell'utente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Balena                                          | Nel contesto di Bitcoin, una balena è qualcuno che detiene una grande quantità di bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| White-Label                                     | Un prodotto white-label è un prodotto o servizio prodotto da un'azienda che altre aziende rimarchiano per farlo apparire come se lo avessero prodotto loro.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Whitepaper                                      | Introduce una nuova idea o argomento per la discussione. Il whitepaper di Bitcoin ha introdotto Bitcoin come un "sistema di contante elettronico peer-to-peer" che "non richiede parti terze di fiducia". Satoshi Nakamoto ha pubblicato il whitepaper il 31 ottobre 2008 su una lista email di crittografi e cypherpunk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Wrapped Segwit                                  | Un'implementazione di design inclusa nell'aggiornamento SegWit pensata per permettere ai portafogli e ad altro software Bitcoin di supportare più facilmente SegWit. Per raggiungere questo obiettivo, i due script nativi di SegWit, P2WPKH e P2WSH, sono utilizzati come "redeemScript" di una transazione P2SH, producendo tipi di script Wrapped SegWit di P2SH-P2WPKH e P2SH-P2WSH rispettivamente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

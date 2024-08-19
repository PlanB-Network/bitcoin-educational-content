---
name: AUTHY 2FA
description: Come utilizzare un'applicazione 2FA?
---
![cover](assets/cover.webp)

Oggi giorno, l'autenticazione a due fattori (2FA) è diventata essenziale per migliorare la sicurezza degli account online contro l'accesso non autorizzato. Con l'aumento degli attacchi informatici, affidarsi esclusivamente a una password per proteggere i propri account è a volte insufficiente. La 2FA introduce un ulteriore livello di sicurezza richiedendo una seconda forma di autenticazione in aggiunta alla password. Questa verifica può assumere diverse forme, come un codice inviato tramite SMS, un codice dinamico generato da un'app dedicata o l'uso di una chiave di sicurezza fisica. Utilizzare la 2FA riduce notevolmente il rischio che i tuoi account vengano compromessi, anche se la tua password viene rubata.

## 2FA tramite App di Autenticazione

Esploreremo altre soluzioni come le chiavi di sicurezza fisiche in altri tutorial, ma in questo propongo di discutere specificamente delle applicazioni 2FA. Il funzionamento di queste applicazioni è piuttosto semplice: quando la 2FA è attivata su un account, ad ogni accesso, ti verrà chiesto non solo la tua solita password ma anche un codice a 6 cifre. Questo codice è generato dalla tua applicazione 2FA. Una caratteristica importante di questo codice a 6 cifre è che non è statico; un nuovo codice viene generato dall'applicazione ogni 30 secondi.
![AUTHY 2FA](assets/notext/01.webp)
Il rinnovo del codice ogni 30 secondi rende molto difficile per un attaccante accedere al tuo account. Questo sistema impedisce agli attaccanti di riutilizzare un codice rubato o intercettato, poiché scade rapidamente. Così, anche se un attaccante riesce a ottenere il codice, può utilizzarlo solo durante una finestra di tempo molto breve prima che sia richiesto un nuovo codice. Inoltre, il fatto che il codice cambi così frequentemente riduce significativamente il tempo a disposizione di un hacker che tenta di indovinare il codice attraverso attacchi di forza bruta.

La 2FA tramite app di autenticazione rappresenta quindi un metodo facile da usare e gratuito per migliorare significativamente la sicurezza dei tuoi account online.

Ci sono molte applicazioni per impostare la 2FA, tra cui Google Authenticator e Microsoft Authenticator sono le più conosciute. Tuttavia, in questo tutorial, desidero presentarvi un'altra soluzione meno nota chiamata Authy. Tutte queste applicazioni operano utilizzando lo stesso protocollo TOTP (*Time based One Time Password*), rendendo il loro uso abbastanza simile.
Authy offre diversi vantaggi rispetto ad altre soluzioni delle grandi aziende tecnologiche. Primo, permette di sincronizzare i tuoi token 2FA su più dispositivi, il che può essere utile in caso di perdita o cambio di telefono. Authy consente anche di generare un backup crittografato e di memorizzarlo online, assicurandoti di non perdere mai l'accesso ai tuoi token, anche se perdi il dispositivo principale. Da un punto di vista dell'interfaccia utente, personalmente trovo che Authy offra anche un'esperienza più piacevole e intuitiva rispetto alle sue alternative.

## Come installare Authy?

Sul tuo smartphone, vai allo store di app (Google Play Store o Apple Store), e cerca "*Twilio Authy Authenticator*".

- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)
![AUTHY 2FA](assets/notext/02.webp)
Quando avvii l'app per la prima volta, dovrai creare un account. Seleziona il prefisso telefonico del tuo paese, così come il tuo numero di telefono, poi clicca su "*Submit*".
![AUTHY 2FA](assets/notext/03.webp)
Inserisci il tuo indirizzo email per il recupero del codice.
![AUTHY 2FA](assets/notext/04.webp)
Un'email verrà inviata per verificare il tuo indirizzo. Inserisci i 6 numeri ricevuti per confermare. ![AUTHY 2FA](assets/notext/05.webp)
Seleziona uno dei due metodi disponibili per verificare il tuo numero di telefono. Se opti per ricevere un SMS, inserisci il codice a 6 cifre ricevuto tramite messaggio per confermare il tuo numero.
![AUTHY 2FA](assets/notext/06.webp)
Congratulazioni, il tuo account Authy è stato creato!
![AUTHY 2FA](assets/notext/07.webp)
## Come configurare Authy?

Per iniziare, vai nelle impostazioni dell'app cliccando sui tre piccoli punti situati in alto a destra dello schermo.
![AUTHY 2FA](assets/notext/08.webp)
Poi clicca su "Impostazioni".
![AUTHY 2FA](assets/notext/09.webp)
Nella scheda "Il Mio Account", hai l'opzione di modificare il tuo account. Ti raccomando di aggiungere un codice PIN all'app selezionando "Protezione App". Questo aggiunge un ulteriore livello di sicurezza per accedere alla tua applicazione.
![AUTHY 2FA](assets/notext/10.webp)
Nella scheda "Account", puoi impostare un backup per i tuoi token. Questo backup permette il recupero dei tuoi codici in caso di problemi. È criptato utilizzando una password che devi definire. È importante che questa password sia forte e conservata in un luogo sicuro. Impostare questo backup non è necessariamente obbligatorio se hai altri metodi di recupero, come un secondo dispositivo con lo stesso account Authy, ad esempio.
![AUTHY 2FA](assets/notext/11.webp)Nella scheda "Dispositivi", puoi vedere tutti i dispositivi sincronizzati con il tuo account Authy. Hai l'opzione di disabilitare l'uso di più dispositivi, che limita l'accesso al tuo account a quel dispositivo soltanto. Se usi solo un dispositivo, questo può aumentare la sicurezza del tuo account, ma assicurati di avere un altro metodo di backup in caso perdessi questo dispositivo.

Se preferisci permettere l'aggiunta di altri dispositivi, ti consiglio di attivare l'opzione che richiede la conferma dai dispositivi attualmente autorizzati sul tuo account Authy prima di aggiungere un nuovo dispositivo.
![AUTHY 2FA](assets/notext/12.webp)
Per aggiungere un nuovo dispositivo, basta ripetere il processo di installazione presentato nella parte precedente utilizzando le stesse credenziali. Ti verrà poi chiesto di confermare questo nuovo accesso dal tuo dispositivo principale.

## Come impostare il 2FA su un account?

Per impostare un codice di autenticazione 2FA tramite un'app come Authy su un account, l'account deve supportare questa funzionalità. Oggi, la maggior parte dei servizi online offre questa opzione 2FA, ma non è sempre il caso. Prendiamo l'esempio dell'account Proton mail che ho presentato in un altro tutorial:

https://planb.network/tutorials/others/proton-mail
![AUTHY 2FA](assets/notext/13.webp)
Generalmente troverai questa opzione 2FA nelle impostazioni del tuo account, spesso sotto la sezione "Password" o "Sicurezza".
![AUTHY 2FA](assets/notext/14.webp)
Quando attivi questa opzione sul tuo account Proton mail, ti viene presentato un codice QR. Devi quindi scansionare questo codice QR con la tua app Authy.
![AUTHY 2FA](assets/notext/15.webp)
Su Authy, clicca sul pulsante "+".
![AUTHY 2FA](assets/notext/16.webp)
Clicca su "Scansiona Codice QR". Poi scansiona il codice QR sul sito web.
Hai anche l'opzione di modificare il tuo nome utente se necessario. Dopo aver apportato le modifiche, clicca sul pulsante "*SALVA*".
Authy mostrerà quindi il tuo codice dinamico specifico di 6 cifre per questo account che si aggiorna ogni 30 secondi.
Inserisci questo codice sul sito web per completare la configurazione del 2FA.
Alcuni siti ti forniranno anche dei codici di recupero dopo aver attivato il 2FA. Questi codici ti permettono di accedere al tuo account se perdi l'accesso alla tua app Authy. Ti consiglio di salvarli in un luogo sicuro.
Il tuo account è ora protetto con l'autenticazione a due fattori tramite l'app Authy.
Ogni volta che effettui l'accesso all'account, dovrai fornire il codice dinamico generato da Authy. Ora puoi proteggere tutti i tuoi account compatibili con questo metodo 2FA. Per aggiungere un nuovo account su Authy, clicca sui tre piccoli punti in alto a destra dell'app.
Poi clicca su "*Aggiungi Account*".
Segui gli stessi passaggi usati per il primo account. I tuoi vari codici dinamici saranno visibili sulla homepage di Authy.
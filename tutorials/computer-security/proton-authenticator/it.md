---
name: Proton Authenticator
description: Come posso utilizzare Proton Authenticator per proteggere i miei account con 2FA?
---
![cover](assets/cover.webp)

L'autenticazione a due fattori (2FA) aggiunge un'ulteriore barriera di sicurezza ai tuoi account richiedendo, oltre alla password, un'ulteriore prova che solo tu ne sarai in possesso. L'attivazione della 2FA riduce drasticamente il rischio di hacking, anche nel caso in cui la password venga compromessa da phishing o da una fuga di dati. Senza il 2FA, un malintenzionato avrebbe bisogno solo della tua password per accedere ai tuoi account; con il 2FA, avrebbe bisogno anche del tuo secondo fattore, vanificando la maggior parte dei tentativi di furto di account.

Esistono vari tipi di 2FA. I codici SMS sono meglio di niente, ma rimangono vulnerabili agli attacchi di SIM swap e alle intercettazioni. Non consigliamo gli SMS come 2FA principale. Le applicazioni di autenticazione (TOTP) generano codici temporanei localmente sul dispositivo, rendendoli molto più difficili da intercettare. Le chiavi di sicurezza fisiche offrono la migliore sicurezza, ma richiedono un hardware dedicato.

Proton Authenticator è un autenticatore TOTP. È la risposta di Proton ai limiti delle applicazioni esistenti: molte sono proprietarie, contengono tracker pubblicitari e non offrono un backup crittografato. Proton Authenticator si distingue perché fornisce un'applicazione open source, priva di pubblicità e tracker, con backup crittografato end-to-end.


## Presentazione di Proton Authenticator

Proton Authenticator è un'applicazione di autenticazione TOTP per cellulari e desktop sviluppata da Proton, nota per i suoi servizi incentrati sulla privacy. Come tutti i prodotti Proton, l'applicazione è open source ed è stata sottoposta a controlli di sicurezza indipendenti. È disponibile gratuitamente su tutte le piattaforme (Android, iOS, Windows, macOS, Linux).

Proton Authenticator offre le seguenti caratteristiche principali:
- Generazione di codici **TOTP** per gli account 2FA, compatibile con la maggior parte dei siti che utilizzano Google Authenticator, Authy, ecc.
- **Backup cloud crittografato opzionale**: è possibile collegare l'applicazione al proprio account Proton per eseguire il backup e la sincronizzazione dei codici con crittografia end-to-end. Se si perde il dispositivo, è sufficiente ricollegarne uno nuovo per ripristinare tutti i codici.
- **Sincronizzazione su più dispositivi**: accedendo a Proton nell'app, i codici 2FA si sincronizzano automaticamente tra più dispositivi tramite crittografia end-to-end. Su iOS, un'alternativa è la sincronizzazione tramite iCloud.
- **Blocco locale tramite password o biometria**: l'applicazione offre il blocco tramite PIN e/o impronte digitali/Face ID. Quindi, anche se qualcuno accede fisicamente al tuo telefono sbloccato, non sarà in grado di aprire Proton Authenticator.
- **Nessuna raccolta di dati o tracker**: Proton si impegna a non raccogliere dati personali tramite l'applicazione. Non c'è pubblicità nascosta o analisi comportamentale.
- **Importazione/esportazione semplice**: uno dei punti di forza di Proton Authenticator è la procedura guidata di importazione degli account esistenti, compatibile con altre applicazioni (Google Authenticator, Authy, Aegis, ecc.). Se necessario, è anche possibile esportare i codici in un file.

In breve, Proton Authenticator vuole essere una soluzione 2FA senza compromessi: sicura, privata e flessibile.


## Installazione

Proton Authenticator è disponibile gratuitamente su tutte le piattaforme. Per scaricare l'applicazione, visita la pagina ufficiale: [https://proton.me/authenticator/download](https://proton.me/authenticator/download)

![PROTON AUTHENTICATOR](assets/fr/01.webp)

_La pagina ufficiale di Proton Authenticator mostra le caratteristiche principali dell'applicazione e dell'interfaccia_

In questa pagina troverai i link per il download per tutti i sistemi operativi: Android, iOS, Windows, macOS e Linux. È sufficiente fare clic sul sistema operativo prescelto e seguire la procedura di installazione standard.

In questa guida ti mostrero come installarla e configurarla su macOS, per poi vedere come installare l'app su iOS e sincronizzare i codici tra i due dispositivi.

### Installazione su macOS

Una volta scaricata e installata l'applicazione, avvia Proton Authenticator. Al primo avvio, l'applicazione guida l'utente attraverso alcune schermate di configurazione iniziale:

![PROTON AUTHENTICATOR](assets/fr/02.webp)

_Schermata di benvenuto di Proton Authenticator con il messaggio "Sicurezza in ogni codice" e il pulsante "Inizia"_

### Importazione iniziale

Se Proton Authenticator rileva che in precedenza si utilizzava un'altra applicazione 2FA, potrebbe apparire una procedura guidata di importazione. Supporta l'importazione diretta da alcune applicazioni (Google Authenticator, 2FAS, Authy, Aegis, ecc.). In alternativa, è possibile saltare questo passaggio e aggiungere gli account manualmente in un secondo momento.

![PROTON AUTHENTICATOR](assets/fr/03.webp)

_Procedura guidata di importazione per il trasferimento di codici da altre applicazioni di autenticazione_

![PROTON AUTHENTICATOR](assets/fr/04.webp)

_Applicazioni di importazione compatibili: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth e Google Authenticator_

### Protezione delle applicazioni locali

Imposta un PIN di sblocco o abilita lo sblocco biometrico (Touch ID), se disponibile. Questo passaggio è fondamentale per evitare che chiunque utilizzi il Mac possa accedere liberamente ai codici 2FA.

![PROTON AUTHENTICATOR](assets/fr/05.webp)

_Schermata di configurazione di Touch ID con messaggio "Proteggi i tuoi dati" e pulsante "Attiva Touch ID "_

### Opzioni di sincronizzazione

L'applicazione consente inoltre di attivare la sincronizzazione iCloud per eseguire il backup dei dati in modo sicuro tra i dispositivi Apple.

![PROTON AUTHENTICATOR](assets/fr/06.webp)

_Opzione di sincronizzazione iCloud con il messaggio "Esegui il backup dei dati in modo sicuro con la sincronizzazione iCloud crittografata"_

Una volta completati questi passaggi, Proton Authenticator è pronto per l'uso.

![PROTON AUTHENTICATOR](assets/fr/07.webp)

_L'iterfaccia principale di Proton Authenticator è ancora vuota con le opzioni "Crea un nuovo codice" e "Importa codici "_


## Aggiungere un account 2FA con ProtonMail

Vediamo ora come aggiungere il primo codice 2FA, utilizzando ProtonMail come esempio. Questo metodo funziona in modo identico per tutti i servizi che supportano l'autenticazione a due fattori.

### Abilitare la 2FA su ProtonMail

Per prima cosa, potete consultare la nostra guida a ProtonMail per maggiori informazioni:


https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Accedi al tuo account ProtonMail e vai alle impostazioni di sicurezza. Cerca l'opzione "Autenticazione a due fattori" e attivala.

![PROTON AUTHENTICATOR](assets/fr/08.webp)

_Pagina delle impostazioni di ProtonMail con l'opzione "Authenticator app" nella sezione "Autenticazione a due fattori*_

Fai clic sul pulsante per attivare l'autenticatore e ProtonMail chiederà di scegliere un'applicazione di autenticazione.

![PROTON AUTHENTICATOR](assets/fr/09.webp)

_Finestra di configurazione di ProtonMail 2FA con i pulsanti "Annulla" e "Avanti "_

ProtonMail visualizzerà quindi un codice QR da scansionare con la propria applicazione di autenticazione.

![PROTON AUTHENTICATOR](assets/fr/10.webp)

_Codice QR ProtonMail da scansionare con la tua applicazione di autenticazione, con l'opzione "Inserisci manualmente la chiave" disponibile_

Se preferisci inserire la chiave manualmente, fai clic su "Enter key manually instead" per visualizzare la chiave segreta.

![PROTON AUTHENTICATOR](assets/fr/11.webp)

_Inserimento manuale delle informazioni 2FA: Chiave, Intervallo (30) e Cifre (6)_

### Scansiona il codice QR con Proton Authenticator

In Proton Authenticator su macOS, fai clic su "Crea un nuovo codice". L'applicazione offre diverse opzioni: **Scansiona un codice QR** o **Inserisci la chiave manualmente**.

Utilizza la fotocamera del Mac per scansionare il codice QR visualizzato sullo schermo di ProtonMail. Una volta scansionato il codice QR, si accede alla schermata di configurazione del nuovo codice.

![PROTON AUTHENTICATOR](assets/fr/12.webp)

_Finestra di creazione di una nuova voce con i campi Titolo (ProtonMail), Segreto, Mittente (Proton), parametri numerici e intervallo_

Proton Authenticator compilerà automaticamente le informazioni. Se lo desideri, è possibile personalizzare il nome, quindi fai clic su "Salva".

![PROTON AUTHENTICATOR](assets/fr/13.webp)

_Codice TOTP generato per ProtonMail (848 812) con visualizzazione del tempo residuo_

### Convalidare la configurazione

ProtonMail chiederà di inserire un codice di 6 cifre generato da Proton Authenticator per confermare il corretto funzionamento della 2FA.

![PROTON AUTHENTICATOR](assets/fr/14.webp)

_Schermata di convalida di ProtonMail che richiede l'inserimento del codice a 6 cifre (848 812)_

Copia il codice dall'applicazione (facendo clic su di esso) e incollalo in ProtonMail per completare l'attivazione.

Una volta convalidato, ProtonMail ti chiederà di scaricare i codici di recupero. È fondamentale salvarli con cura.

![PROTON AUTHENTICATOR](assets/fr/15.webp)

_Schermata dei codici di recupero di ProtonMail con l'elenco dei codici di recupero e il pulsante "Scarica"_

### Codici di emergenza

Quando si aggiunge un account, conserva i codici di recupero forniti dal servizio. La maggior parte dei siti offre codici di recupero statici e monouso da conservare in un luogo sicuro. Conserva questi codici di backup al di fuori di Proton Authenticator, in modo da poter accedere al tuo account se perdi l'accesso all'applicazione 2FA.


## Installazione di IOS e importazione di codice

Ora che avete configurato Proton Authenticator su macOS, potreste volerlo utilizzare anche su iPhone o iPad. Ecco come ottenere i codici 2FA su più dispositivi.

### Scaricare l'applicazione su iOS

Vai sull'App Store e cerca "Proton Authenticator". Scarica e installa l'applicazione sul tuo dispositivo iOS.

![PROTON AUTHENTICATOR](assets/fr/16.webp)

_Processo di installazione su iOS: schermata di benvenuto, procedura guidata di importazione, selezione delle applicazioni compatibili e schermata finale "Importa codici da Proton Authenticator"_

### Metodo 1: Esportazione/importazione tramite file JSON

Se non utilizzi la sincronizzazione automatica (account iCloud o Proton), è necessario trasferire manualmente i codici dal Mac all'iPhone:

**Fase 1 - Esportazione da macOS** :

Sul Mac, apri Proton Authenticator e vai su Impostazioni (icona ingranaggio). Nel menu, fai clic su "Esporta".

![PROTON AUTHENTICATOR](assets/fr/17.webp)

_Menu delle impostazioni di Proton Authenticator su macOS con l'opzione "Esporta" visibile_

![PROTON AUTHENTICATOR](assets/fr/18.webp)

_Finestra di esportazione con nome del file "Proton_Authenticator_backup_2025" e pulsante "Salva "_

Salva il file JSON sul Mac. È possibile inviarlo tramite e-mail sicura o salvarlo in iCloud Drive per accedervi dall'iPhone.

**Fase 2 - Importazione su iOS** :

Sul tuo iPhone, installa Proton Authenticator e, durante la configurazione, scegli di importare i codici. Seleziona "Proton Authenticator" dall'elenco e importa il file JSON.

![PROTON AUTHENTICATOR](assets/fr/19.webp)

_Processo di importazione su iOS: Localizzazione del file JSON, conferma dell'importazione e schermate di configurazione con opzioni Face ID e iCloud_

### Metodo 2: Sincronizzazione automatica

**Via account Proton (per la sincronizzazione multipiattaforma)**:

Se non hai ancora configurato un account Proton e se desideri sincronizzare tra diversi sistemi operativi, l'applicazione chiederà di creare o collegare un account Proton.

![PROTON AUTHENTICATOR](assets/fr/20.webp)

_Schermata di sincronizzazione del dispositivo che chiede di creare un account Proton gratuito o di collegarsi a un account esistente_

**Via iCloud (solo per l'ecosistema Apple)**:

Se si utilizzano solo dispositivi Apple, è possibile scegliere la sincronizzazione iCloud nelle impostazioni dell'applicazione. Questo metodo sincronizza automaticamente e in modo sicuro i codici tra tutti i dispositivi Apple, senza bisogno di un account Proton.


## Backup e ripristino criptati

Una delle caratteristiche principali di Proton Authenticator è il back-up end-to-end dei codici 2FA, ciò garantisce che in caso di perdita o cambio di dispositivo non si debba ricominciare da capo.

### Crittografia end-to-end

Quando si tratta di backup crittografato nel cloud con Proton Authenticator, i segreti TOTP vengono crittografati localmente sul dispositivo prima di essere inviati al server Proton. La decodifica è possibile solo da parte tua, sui dispositivi collegati al tuo account Proton. Proton AG non dispone della chiave per leggere i codici registrati.

Su iOS, se si sceglie iCloud anziché l'account Proton, i dati vengono crittografati secondo gli standard Apple. Il backup locale su Android consente di crittografare il file di backup con una password a scelta.

### Ripristino in caso di perdita

Se il telefono viene smarrito, rubato o si cambia telefono :

- **Con il backup di Proton abilitato**: installa Proton Authenticator sul nuovo dispositivo. Durante la configurazione iniziale, accedi allo stesso account Proton. Immediatamente, l'applicazione sincronizzerà e scaricherà tutti i codici 2FA dal backup criptato.
- **Con il backup di iCloud (iOS)**: collega il nuovo iPhone/iPad con lo stesso ID Apple e assicurarti di attivare il Portachiavi iCloud. Dopo aver installato Proton Authenticator, collegarti a iCloud. I codici dovrebbero sincronizzarsi tramite iCloud e apparire.
- **Nessun backup nel cloud**: dovrai importare i tuoi account manualmente. Se hai esportato un file di backup, utilizza la funzione Importa in Proton Authenticator. Nel peggiore dei casi, se non si dispone di un backup, è necessario utilizzare i codici di backup per ciascun servizio o contattare l'assistenza.

Proton Authenticator consente di esportare gli account in qualsiasi momento, sia come file crittografato che come codice QR multi-account. Queste opzioni offrono una maggiore sicurezza.


## Le migliori pratiche

L'utilizzo di un autenticatore 2FA aumenta notevolmente la sicurezza, ma è necessario osservare alcune best practice:

### Salva i tuoi codici di emergenza

Quando si attiva la 2FA su un servizio, spesso viene fornito un elenco di codici di recupero. Conservateli fuori dal telefono (su carta, in un gestore di password criptato, ecc.). In caso di perdita totale dell'autenticatore, questi codici statici vi salveranno.

### Non confondere le tue password e i codici 2FA

Sarai tentato di utilizzare un gestore di password che memorizzi anche i TOTP. Tuttavia, tenere la password e il codice 2FA nello stesso posto crea un unico punto di errore e indebolisce la doppia autenticazione. Per la massima sicurezza, molti esperti consigliano di separare i due fattori: le password in un gestore sicuro e i codici 2FA in un'applicazione separata come Proton Authenticator. Tuttavia, utilizzare un gestore integrato è sempre meglio che non avere affatto la 2FA.

### Attivare diversi metodi 2FA

Idealmente, utilizza più di un secondo fattore per i tuoi account critici. Non esitare ad aggiungere una chiave di sicurezza fisica se il servizio lo consente. Per maggiori informazioni, consultate il nostro tutorial sulle chiavi fisiche Yubikey:

https://planb.academy/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Allo stesso modo, tieni a portata di mano dei codici di emergenza stampati.

### Discrezione e protezione del dispositivo

Non permettere a nessuno di cercare il tuo telefono sbloccato. Con Proton Authenticator, i codici sono protetti da PIN/biometria: non divulgare questo PIN. Allo stesso modo, fai attenzione al phishing: anche con il 2FA, se fornisci un codice a un sito fraudolento in tempo reale, potrebbe essere utilizzato da un malintenzionato.

### Aggiornamenti e audit

Mantenere Proton Authenticator aggiornato (gli aggiornamenti correggono eventuali difetti). Poiché il codice è aperto, la comunità effettua verifiche informali e Proton pubblica i risultati delle verifiche formali.


## Confronto con altre applicazioni

Come si colloca Proton Authenticator rispetto ad altre applicazioni di autenticazione? Ecco un riepilogo comparativo:
- **Proton Authenticator**: open source, backup in cloud crittografato E2EE opzionale, sincronizzazione su più dispositivi, blocco locale, nessun tracciamento, disponibile su mobile e desktop.
- **Google Authenticator**: proprietario, backup tramite account Google dal 2023 ma senza crittografia end-to-end (le chiavi possono essere viste da Google), sincronizzazione multidispositivo aggiunta nel 2023, nessun blocco delle applicazioni per impostazione predefinita, contiene tracker di Google.
- **Aegis Authenticator**: open source, solo backup locale, nessuna sincronizzazione cloud, codice/blocco biometrico, nessun tracciamento, solo Android.
- **Authy**: proprietario, backup su cloud criptato con password ma codice chiuso, sincronizzazione su più dispositivi, blocco PIN/impronta digitale, raccoglie il numero di telefono, l'applicazione desktop verrà dismessa nel marzo 2024.

Di seguito troverai la nostra guida ad Authy:

https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator è una delle soluzioni più complete e sicure disponibili: open source, sincronizzazione criptata su più dispositivi, nessun tracciamento commerciale.


## Risorse e supporto

### Documentazione ufficiale

- **Sito web ufficiale**: [proton.me/authenticator](https://proton.me/authenticator) - Presentazione del prodotto e download
- **Pagina di download**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Link per tutti i sistemi operativi
- **Supporto Proton**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Guida ufficiale all'attivazione di 2FA
- **Blog di Proton**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Annunci e caratteristiche dettagliate

### Codice sorgente e trasparenza

- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Codice sorgente aperto
- **Audit di sicurezza**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Rapporti di audit indipendenti

### Test di sicurezza consigliati

Dopo la configurazione, testa la configurazione:
- [Have I Been Pwned](https://haveibeenpwned.com/) - Controlla se i tuoi account sono stati compromessi
- [2FA Directory](https://2fa.directory/) - Elenco dei servizi che supportano 2FA

### Comunità e discussioni

- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - La community ufficiale di Proton
- **Forum delle guide sulla privacy**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Discussioni tecniche su questioni di privacy
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Consigli generali sulla privacy.

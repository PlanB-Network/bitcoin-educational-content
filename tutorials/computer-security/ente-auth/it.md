---
name: Ente Auth
description: Un autenticatore 2FA crittografato end-to-end e open-source
---
![cover](assets/cover.webp)



L'autenticazione a due fattori (2FA) è diventata indispensabile per proteggere i nostri account online. Oltre alla password abituale, richiede un codice temporaneo, solitamente generato da un'applicazione dedicata. Questo meccanismo, noto come TOTP (Time-Based One-Time Password), garantisce che, anche se la password viene compromessa, un malintenzionato non sarà in grado di accedere al vostro account senza possedere questo secondo fattore, rinnovato ogni 30 secondi.



Tuttavia, la scelta della giusta applicazione di autenticazione non è banale. Google Authenticator, pur essendo molto diffuso, presenta notevoli limitazioni: codice proprietario impossibile da verificare, sincronizzazione senza crittografia end-to-end e rischio di perdita totale dei codici in caso di problemi con il telefono. Altre soluzioni, come Authy, richiedono un numero di telefono e non garantiscono la totale riservatezza.



**Ente Auth** si propone come alternativa moderna e sicura. Questa applicazione gratuita, open source e multipiattaforma, sviluppata dal team di [Ente Photos](https://ente.io), offre backup cloud crittografati end-to-end e una sincronizzazione perfetta tra tutti i dispositivi. A differenza delle soluzioni proprietarie, Ente Auth offre un controllo totale sui codici di autenticazione senza compromettere la privacy.



In questo tutorial vi mostreremo passo dopo passo come installare e utilizzare Ente Auth e perché questa soluzione si differenzia dagli autenticatori tradizionali.



## Introduzione all'Ente Auth



Ente Auth è stato sviluppato dal team che ha ideato Ente Photos, un servizio di archiviazione di foto crittografato end-to-end e rispettoso della privacy. Fedele alla filosofia Ente ("Ente" significa "miniera" in malayalam, a simboleggiare il controllo sui propri dati), Ente Auth è stato progettato per restituire agli utenti il pieno controllo sui propri codici di autenticazione a due fattori.



### Caratteristiche principali



**Codici TOTP standard**: Ente Auth genera codici temporanei compatibili con la maggior parte dei servizi (GitHub, Google, Binance, ProtonMail, ecc.). È possibile aggiungere tutti gli account 2FA necessari e l'applicazione calcola i codici in base ai segreti forniti.



**Backup crittografato end-to-end nel cloud**: I vostri codici sono archiviati online in modo sicuro. Solo voi potete decifrarli: la chiave di crittografia deriva dalla vostra password ed è nota solo a voi. Ente (il server) non è a conoscenza dei vostri segreti e nemmeno dei titoli dei vostri account, poiché tutto è crittografato sul lato client utilizzando un'architettura a conoscenza zero.



**Sincronizzazione su più dispositivi**: Potete installare Ente Auth su diversi dispositivi (smartphone, tablet, computer) e accedere ai vostri codici su tutti. Qualsiasi modifica viene propagata automaticamente e istantaneamente agli altri dispositivi tramite il cloud crittografato, garantendo una grande flessibilità nel lavoro quotidiano.



**Interface minimalista e intuitivo**: L'applicazione offre un Interface semplificato, facile da imparare anche per gli utenti non tecnici. gli account 2FA vengono visualizzati con il nome del servizio, il login e il codice a 6 cifre, aggiornato in tempo reale. Ente Auth visualizza anche il codice successivo con qualche secondo di anticipo per evitare di essere scoperti dalla scadenza.



**Open source e verificato**: Il codice sorgente di Ente Auth è [pubblico su GitHub](https://github.com/ente-io/auth) con licenza AGPL v3.0. Qualsiasi sviluppatore può verificarlo per controllare eventuali difetti o comportamenti indesiderati. La crittografia implementata è stata oggetto di un [audit esterno indipendente](https://ente.io/blog/cryptography-audit/), a garanzia della serietà della sicurezza dell'applicazione.



### Vantaggi e limiti



**Vantaggi:**




- Privacy by design con la crittografia end-to-end
- Sincronizzazione sicura tra tutti i dispositivi
- Codice sorgente aperto verificabile
- Interface utente chiaro e intuitivo Interface
- Back-up automatico per evitare la perdita di codici
- Disponibile su tutte le piattaforme (mobile e desktop)



**Limiti:**




- Per la sincronizzazione è necessaria una connessione a Internet
- Gli utenti avanzati possono preferire soluzioni 100% offline come Aegis (solo per Android)
- Relativamente recente rispetto alle soluzioni consolidate



## Installazione



Ente Auth è disponibile sulle piattaforme più diffuse. È possibile scaricare l'applicazione da [il sito web ufficiale](https://ente.io/auth) o dagli store ufficiali.



![Installation d'Ente Auth](assets/fr/01.webp)



*Pagina di download di Ente Auth con tutte le piattaforme disponibili



### Android


Avete diverse opzioni:




- Google Play Store**: Cercare "Ente Auth" per l'installazione classica
- F-Droid**: Disponibile dal catalogo di applicazioni open-source di Android, con la garanzia di una costruzione verificata e senza contenuti proprietari
- Installazione manuale** : I file APK possono essere scaricati dalla [pagina GitHub del progetto](https://github.com/ente-io/auth/releases) con notifica integrata delle nuove versioni



### iOS (iPhone/iPad)


Installate Ente Auth direttamente dall'App Store di Apple cercando il nome dell'applicazione. L'applicazione per iOS può essere eseguita anche su Mac dotati di chip Apple Silicon (M1/M2) tramite il Mac App Store.



### Computer (Windows, macOS, Linux)


Ente Auth offre applicazioni desktop native. Visitate [ente.io/download](https://ente.io/download) o la sezione [Releases di GitHub](https://github.com/ente-io/auth/releases):





- Windows**: Viene fornito un programma di installazione EXE
- macOS**: Trascinamento dell'immagine disco DMG in Applicazioni
- Linux** : Sono disponibili diversi formati (AppImage portable, .deb per Debian/Ubuntu, .rpm per Fedora/Red Hat)



**Nota:** Questa esercitazione si basa su Ente Auth v4.4.4 e successive. Le versioni precedenti possono presentare piccole differenze Interface.



### Web Interface


Senza installazione, è possibile accedere ai codici tramite [auth.ente.io](https://auth.ente.io) da qualsiasi browser. Interface web è limitato alla visualizzazione dei codici (utile per la risoluzione dei problemi), poiché l'aggiunta di account richiede l'applicazione mobile o desktop per motivi di sicurezza.



## Prima configurazione



### Creazione di un account



Quando si avvia Ente Auth per la prima volta, si hanno due opzioni:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Schermata iniziale di Ente Auth con opzioni di creazione dell'account*



**Con un account (consigliato)**: Scegliere "Crea account" e inserire il proprio indirizzo e-mail Address e una password. **Importante**: questa password serve come password principale per la crittografia dei dati. Scegliere una password forte e unica, poiché non esiste una procedura di ripristino convenzionale senza perdita di dati. Se la si smarrisce, i dati crittografati saranno irrecuperabili.



**Modalità offline**: Selezionare "Usa senza backup" per utilizzare l'applicazione in locale senza cloud. In questa modalità, i codici rimangono sul dispositivo, ma è necessario esportarli manualmente per evitare di perderli.



![Vérification email et récupération de clé](assets/fr/03.webp)



*Processo di verifica via e-mail e generazione di una chiave di recupero di 24 parole*



Può essere richiesta una verifica via e-mail per convalidare la creazione dell'account e consentire il recupero su un nuovo dispositivo. Ente Auth vi fornirà anche una chiave di recupero di 24 parole (basata sul metodo BIP39). **È assolutamente necessario conservare questa chiave** in un luogo sicuro: è l'unico mezzo per recuperare i dati in caso di dimenticanza della password.



### Sicurezza locale



Consiglio vivamente di attivare la protezione locale tramite codice o biometria. Andate in **Impostazioni → Sicurezza → Schermata di blocco** e configurate :





- Sblocco biometrico**: Face ID, impronta digitale a seconda delle capacità del dispositivo
- PIN/password specifici per l'applicazione**
- Ritardo di blocco automatico**: ad es. "Immediatamente" o dopo 30 secondi di inattività



Questa protezione impedisce l'accesso non autorizzato ai vostri codici se qualcuno accede al vostro telefono sbloccato. Si noti che questo blocco è una barriera aggiuntiva: i dati rimangono crittografati end-to-end anche senza questa protezione.



## Aggiungere account 2FA



### Procedura standard



Per aggiungere un nuovo account 2FA, facciamo l'esempio concreto dell'attivazione di 2FA su Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*Il Interface principale di Ente Auth è pronto ad aggiungere il primo account 2FA*



**Lato servizio (Bull Bitcoin)**: Accedere all'account Bull Bitcoin, andare alle impostazioni di sicurezza e attivare l'autenticazione a due fattori.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* menu impostazioni di sicurezza



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Opzione per abilitare l'autenticazione a due fattori su Bull Bitcoin*



Il servizio visualizzerà quindi un codice QR da scansionare con la propria applicazione di autenticazione:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Codice QR generato da Bull Bitcoin da scansionare con l'autenticatore*



**In Ente Auth**: Fare clic su "Inserisci una chiave di configurazione", quindi scansionare il codice QR visualizzato da Bull Bitcoin. Ente Auth riconoscerà automaticamente l'account e compilerà i campi.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Configurazione dei dettagli del conto Bull Bitcoin in Ente Auth*



È possibile personalizzare il nome del servizio e il proprio login per facilitarne l'individuazione. Le impostazioni avanzate (algoritmo SHA1, periodo di 30s, 6 cifre) sono generalmente corrette per impostazione predefinita.



**Convalida lato servizio**: Tornare al Toro Bitcoin e inserire il codice a 6 cifre generato da Ente Auth per completare l'attivazione.



![Saisie du code 2FA](assets/fr/09.webp)



*Inserire il codice generato da Ente Auth per convalidare l'attivazione di 2FA*



![2FA activée](assets/fr/10.webp)



*Conferma dell'avvenuta attivazione di 2FA su Bull Bitcoin*



**Codici di recupero**: Bull Bitcoin vi fornirà i codici di recupero. **Conservarli in un luogo sicuro, separato dall'autenticatore.



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Opzione per i codici di backup di emergenza generate su Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Elenco dei codici di recupero da conservare in un luogo sicuro*



### Organizzazione e gestione



Ente Auth offre diverse caratteristiche pratiche:



**Copia rapida**: Premere il codice per copiarlo automaticamente negli appunti.



**Azioni sensibili al contesto**: Tenere premuto (o fare clic con il tasto destro del mouse sul desktop) per modificare, eliminare, condividere o appuntare una voce.



**Tag e ricerca**: Organizzate i vostri account con tag (personale/professionale, per categoria di servizio) e utilizzate la barra di ricerca per filtrare rapidamente.



![Création d'un tag](assets/fr/17.webp)



*Processo di creazione dei tag: menu contestuale e finestra di dialogo di creazione*



![Tag appliqué](assets/fr/18.webp)



*Il tag "Bitcoin" è stato applicato con successo al conto Bull Bitcoin*



**Icone automatiche**: Ogni voce può essere illustrata con il logo del servizio, grazie all'integrazione del pacchetto di icone [Simple Icons] (https://simpleicons.org/).



**Condivisione sicura temporanea**: Un'esclusiva funzionalità di Ente Auth, la condivisione sicura consente di trasmettere un codice 2FA a un collega senza rivelare il segreto sottostante. generate un link criptato valido per 2, 5 o 10 minuti al massimo: il destinatario vede il codice in tempo reale, ma non può esportarlo o accedere ai dati dell'account. Questo metodo è ideale per l'assistenza tecnica o la collaborazione temporanea, offrendo un livello di sicurezza impossibile con un semplice screenshot o un messaggio di testo.



![Partage sécurisé](assets/fr/19.webp)



*Interface condivisione temporanea sicura: scegliere la durata (5 min)*



**Esportazione/importazione sicura**: Ente Auth consente di esportare i codici in altre applicazioni o di importarli da Google Authenticator e altre soluzioni. L'esportazione avviene tramite un file criptato o un codice QR, garantendo la portabilità dei dati senza compromettere la sicurezza.



**Chiave di recupero BIP39**: L'applicazione genera automaticamente una frase di recupero di 24 parole secondo lo standard BIP39 (Bitcoin Improvement Proposal), identico a quello dei portafogli di criptovalute. Questa frase è la chiave di recupero definitiva, che consente di ripristinare tutti i codici anche se si dimentica la password principale.



## Configurazione e impostazioni



Ente Auth offre numerose opzioni di personalizzazione accessibili tramite le impostazioni dell'applicazione:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Panoramica dei parametri disponibili in Ente Auth*



### Gestione dei conti e dei dati



![Paramètres de sécurité](assets/fr/14.webp)



*Opzioni di sicurezza avanzate: verifica via e-mail, codice PIN, sessioni attive*



Le impostazioni di sicurezza consentono di :




- Abilita la verifica via e-mail per le nuove connessioni
- Attivare la chiave d'accesso
- Visualizzare le sessioni attive sui vari dispositivi
- Impostazione di un codice PIN o della biometria



### Interface e opzioni di utilizzo



![Paramètres généraux](assets/fr/15.webp)



*Parametri Interface e personalizzazione dell'applicazione*



Le impostazioni generali includono :




- Lingua**: Interface multilingue
- Display**: Icone grandi, modalità compatta
- Privacy**: Nascondere i codici, ricerca rapida
- Telemetria**: Segnalazione degli errori (può essere disattivata)



## Backup e sincronizzazione



### Come funziona la crittografia



Quando si aggiunge un account con un account Ente collegato, l'applicazione cripta immediatamente questi dati sensibili a livello locale utilizzando la chiave master (derivata dalla password). I dati crittografati vengono quindi inviati al server Ente per l'archiviazione.



Grazie a questo meccanismo, è sempre disponibile un backup cloud crittografato end-to-end dei codici. In caso di smarrimento del dispositivo, è sufficiente reinstallare Ente Auth e ricollegarsi: l'applicazione scaricherà e decifrerà automaticamente tutti i codici.



### Sincronizzazione multidispositivo



Se si utilizza Ente Auth sia sullo smartphone che sul computer, qualsiasi aggiunta o modifica su un dispositivo appare in pochi secondi sull'altro. Questa sincronizzazione passa attraverso il cloud di Ente, ma poiché i dati sono crittografati end-to-end, il server vede solo il contenuto crittografato illeggibile.



![Synchronisation mobile](assets/fr/16.webp)



*Demo di sincronizzazione: stesso conto Bull Bitcoin accessibile da mobile e da desktop*



La sincronizzazione è perfetta: installate Ente Auth sul vostro smartphone, accedete con le vostre credenziali e tutti i vostri codici 2FA (qui Bull Bitcoin) appariranno automaticamente. L'esempio qui sopra mostra la perfetta sincronizzazione tra desktop e mobile: lo stesso codice Bull Bitcoin è accessibile su entrambi i dispositivi.



In termini di riservatezza, né Ente né terzi hanno accesso ai vostri segreti 2FA. Anche i metadati (tag, note, nomi di servizi) sono criptati prima di essere inviati. Questa architettura a conoscenza zero garantisce che solo voi possiate decifrare i vostri codici.



### Utilizzo offline



La sincronizzazione richiede Internet, ma Ente Auth funziona perfettamente offline su ogni dispositivo, poiché tutti i dati sono memorizzati localmente. Le modifiche offline vengono accodate e sincronizzate non appena viene ripristinata la connessione.



## Sicurezza e privacy



### Garanzie crittografiche



Ente Auth si basa su una robusta crittografia end-to-end con architettura zero-knowledge. I vostri codici sono crittografati con una chiave di cui siete gli unici detentori, derivata dalla vostra password principale grazie a funzioni avanzate di derivazione della chiave.



**Architettura a conoscenza zero: Ente non può accedere fisicamente ai vostri dati. Anche i metadati (nomi dei servizi, tag, note) vengono crittografati sul lato client prima della trasmissione. Questo approccio garantisce che, in caso di attacco ai vostri server o di richiesta governativa, Ente possa divulgare solo dati criptati che non possono essere letti senza la vostra password.



**Crittografia locale**: Il processo di crittografia avviene interamente sul dispositivo prima di essere inviato al cloud. I server di Ente ricevono e memorizzano solo i dati crittografati, rendendo impossibile l'accesso non autorizzato, anche per gli amministratori del servizio.



### Trasparenza e audit



Poiché il codice è [open source](https://github.com/ente-io/auth), la comunità può verificare l'assenza di backdoor. Ente ha fatto eseguire [molteplici audit esterni](https://ente.io/blog/cryptography-audit/) per convalidare la sicurezza della sua implementazione:





- Cure53** (Germania): Verifica della sicurezza delle applicazioni e della crittografia
- Symbolic Software** (Francia): Competenza specializzata in crittografia
- Fallible** (India): Test di penetrazione e analisi delle vulnerabilità



Questi audit indipendenti, effettuati da società riconosciute, garantiscono che l'implementazione crittografica di Ente Auth è conforme alle migliori pratiche di sicurezza e non presenta difetti critici.



### Informativa sulla privacy



Ente Auth applica una [politica esemplare sulla privacy](https://ente.io/privacy/) basata su una raccolta minima di dati. Vengono conservate solo le informazioni strettamente necessarie al funzionamento del servizio: la vostra e-mail Address per l'autenticazione e il recupero dell'account.



**Nessun tracciamento o telemetria**: A differenza della maggior parte delle applicazioni, Ente Auth non raccoglie metriche di utilizzo, né dati di crash identificativi, né informazioni comportamentali. L'applicazione funziona senza pubblicità invadente o tracker analitici.



**Conformità al RGPD**: Ente è pienamente conforme al Regolamento generale europeo sulla protezione dei dati. Avete il diritto di accedere, correggere o cancellare i vostri dati in qualsiasi momento. L'esportazione dei dati](https://ente.io/take-control/) è a portata di clic e la cancellazione definitiva del vostro account elimina tutti i vostri dati dai server.



**Archiviazione decentralizzata e sicura**: I vostri dati crittografati sono replicati su 3 diversi provider, in 3 diversi Paesi, garantendo una disponibilità ottimale ed evitando la dipendenza da un unico provider cloud.



Il modello di business di Ente si basa sul servizio a pagamento Ente Photos, che ci consente di offrire Ente Auth **gratuitamente e senza limitazioni** senza compromettere la privacy degli utenti attraverso la monetizzazione dei loro dati. Questo approccio garantisce la sostenibilità del servizio senza fare affidamento sulla pubblicità o sulla rivendita di dati personali.



## Confronto con altre soluzioni



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth si distingue come una delle poche soluzioni in grado di combinare tutti i vantaggi: trasparenza del codice sorgente, backup crittografato nel cloud e sincronizzazione multipiattaforma.



## Casi d'uso consigliati



### Utenti individuali



Ente Auth è ideale per le persone attente alla sicurezza che attivano sistematicamente la 2FA. Non dovrete più preoccuparvi di perdere i codici quando cambiate telefono o di dover scegliere tra comodità e sicurezza.



### Utilizzo in famiglia e su più dispositivi



L'applicazione si rivela particolarmente utile se si utilizzano più dispositivi. È possibile salvare i codici su smartphone e tablet o condividere alcuni codici di famiglia (Netflix, family cloud) in modo sincrono e sicuro.



### Uso professionale



Per i team che gestiscono account sensibili, Ente Auth facilita la collaborazione preservando la sicurezza, grazie alle sue funzioni di condivisione avanzate integrate nella sezione "Organizzazione e gestione".



## Le migliori pratiche





- Conservare i codici di emergenza**: Conservare i codici di recupero forniti da ciascun servizio lontano dal telefono.





- Utilizzare una password principale forte**: La password principale di Ente Auth deve essere unica e robusta, in quanto protegge tutti i codici.





- Attivare la protezione locale**: Configurare il PIN o la biometria per impedire l'accesso fisico non autorizzato.





- Non personalizzare eccessivamente**: Evitare modifiche avanzate che potrebbero compromettere la sincronizzazione.





- Mantenere l'applicazione aggiornata**: Gli aggiornamenti correggono i difetti di sicurezza e migliorano la funzionalità.





- Prova di ripristino**: Di tanto in tanto verificare che sia possibile ripristinare i codici su un altro dispositivo.



## Conclusione



Ente Auth rappresenta una soluzione moderna e completa per l'autenticazione a due fattori. Combinando sicurezza, trasparenza e facilità d'uso, questa applicazione open source soddisfa le esigenze degli utenti più esigenti senza sacrificare la convenienza.



A differenza delle soluzioni proprietarie che vi bloccano in un ecosistema opaco, Ente Auth vi restituisce il controllo dei vostri dati di autenticazione proteggendovi da perdite accidentali grazie ai suoi backup criptati.



Sia che si tratti di un individuo che desidera proteggere i propri account personali, sia che si tratti di un team che gestisce gli accessi aziendali, Ente Auth è una scelta intelligente per modernizzare l'approccio alla sicurezza digitale senza compromettere la privacy.



## Risorse e supporto



### Documentazione ufficiale




- Sito web ufficiale**: [ente.io/auth](https://ente.io/auth)
- Centro assistenza**: [help.ente.io/auth](https://help.ente.io/auth)
- Blog tecnico**: [ente.io/blog](https://ente.io/blog)



### Codice sorgente e trasparenza




- GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- Audit sulla crittografia**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Comunità




- Discord**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- Reddit**: [r/enteio](https://reddit.com/r/enteio)
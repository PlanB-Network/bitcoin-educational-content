---
name: Aegis Authenticator
description: Come si può utilizzare Aegis Authenticator per proteggere gli account con la doppia autenticazione?
---

![cover](assets/cover.webp)



Oggi l'autenticazione a due fattori (2FA) è essenziale per proteggere gli account online. Oltre alla password, aggiunge un secondo fattore (spesso un codice a 6 cifre) che scade dopo 30 secondi, rendendo il tutto molto più difficile per gli hacker. L'utilizzo di un'applicazione dedicata TOTP (*Time-based One-Time Password*) è più sicuro degli SMS, che possono essere dirottati da attacchi di SIM swapping.



Tuttavia, non tutte le applicazioni di autenticazione sono uguali. Molte soluzioni proprietarie (Google Authenticator, Authy, ecc.) pongono problemi: sono proprietarie e closed-source (impossibile verificarne la sicurezza), a volte integrano tracker pubblicitari, non offrono un back-up crittografato dei codici e possono persino impedire l'esportazione degli account per bloccarvi nel loro ecosistema.



Aegis Authenticator, invece, si presenta come un'alternativa gratuita ed etica a queste applicazioni. Aegis è un'applicazione gratuita, sicura e open-source per la gestione dei token di verifica in due passaggi su Android. Il suo sviluppo si concentra su caratteristiche essenziali che altre applicazioni non offrono, tra cui una robusta crittografia dei dati locali e la possibilità di effettuare backup sicuri. Nel complesso, Aegis offre una soluzione di doppia autenticazione locale e verificabile, ideale per chi desidera mantenere il controllo totale sui propri codici 2FA.



## Presentazione di Aegis Authenticator



Aegis Authenticator è un'applicazione 2FA open-source per Android, rilasciata sotto licenza GPL v3. Si distingue per la sua filosofia di "privacy by design": l'applicazione funziona interamente offline e non richiede la connessione a un servizio remoto. Di conseguenza, i token rimangono memorizzati localmente sul dispositivo, in una cassaforte sicura di cui solo voi possedete la chiave.



### Caratteristiche principali



**Tutti i codici OTP sono memorizzati in un caveau crittografato AES-256 (modalità GCM), protetto da una password principale definita dall'utente. È possibile sbloccare questo caveau tramite password o dati biometrici (impronte digitali, riconoscimento facciale) per una maggiore comodità. In assenza di una password, i dati non sarebbero criptati, pertanto si consiglia vivamente di impostarne una.**



**Organizzazione avanzata:** Aegis mantiene ben organizzati i vostri numerosi account 2FA. È possibile ordinare le voci in ordine alfabetico o nell'ordine desiderato, raggrupparle per categoria (ad es. personale, lavoro, sociale) per facilitarne il recupero e assegnare a ciascuna voce un'icona personalizzata. È inclusa una barra di ricerca per trovare immediatamente un servizio o un account in base al nome.



**Per non perdere mai l'accesso ai vostri account, Aegis offre backup automatici della vostra cassaforte. Questi sono criptati (tramite una password) e possono essere salvati in una posizione a scelta (memoria interna, cartella cloud, ecc.). L'applicazione può anche esportare manualmente il database degli account, in formato crittografato o non crittografato, a seconda delle esigenze. L'importazione di account da altre applicazioni 2FA è altrettanto semplice (Aegis supporta l'importazione da Authy, Google Authenticator, FreeOTP, andOTP, ecc.)**



**Sicurezza e privacy:** l'applicazione è completamente offline per impostazione predefinita. Non richiede permessi di rete, il che significa che non trasmette dati all'esterno, e non dispone di tracker pubblicitari o moduli di analisi comportamentale. Aegis non visualizza annunci pubblicitari e non richiede un account utente: appena installato, è subito operativo senza registrazione. Poiché il suo codice sorgente è pubblico su GitHub, la comunità può verificarlo liberamente, garantendo l'assenza di funzionalità dannose o nascoste.



**Aegis adotta un design pulito, Material Design, con supporto di temi scuri (inclusa una modalità AMOLED) e persino una vista opzionale a mattonelle per visualizzare i codici come griglie. L'interface è ordinato, senza fronzoli, e impedisce la cattura dello schermo dei codici come misura di sicurezza.**



## Installazione



Poiché Aegis Authenticator è open source, i suoi sviluppatori favoriscono canali di distribuzione rispettosi della privacy. Esistono due modi principali per installarlo:



### Via F-Droid (consigliato)



Il modo più sicuro e semplice è attraverso F-Droid, il negozio alternativo gratuito. Se F-Droid non è ancora installato sul vostro telefono, iniziate a scaricarlo dal sito ufficiale [F-Droid.org](https://f-droid.org). Poi :





- Aprite F-Droid e assicuratevi di aver aggiornato i repository per ottenere l'elenco più recente di applicazioni
- Cercare "Aegis Authenticator" in F-Droid. Dovrebbe apparire l'applicazione ufficiale (editore: Beem Development)
- Avviare l'installazione premendo Installa. Poiché Aegis è una delle applicazioni verificate da F-Droid, potrete beneficiare di un download affidabile e sicuro



L'installazione tramite F-Droid offre il vantaggio di ricevere automaticamente gli aggiornamenti dell'applicazione non appena vengono rilasciati. Inoltre, F-Droid garantisce che l'applicazione sia priva di componenti proprietari indesiderati.



### Via GitHub (APK firmato)



Se preferite installare l'applicazione senza passare per un negozio, potete scaricare l'APK ufficiale direttamente dalla pagina GitHub del progetto. Sul repository di Aegis ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), andate alla sezione Releases, dove sono pubblicate le versioni stabili.





- Scarica l'ultima versione APK
- Prima di installare l'APK, assicurarsi di aver autorizzato l'installazione di applicazioni da fonti sconosciute sul dispositivo (nelle impostazioni di Android)
- L'APK fornito su GitHub è firmato dallo sviluppatore con la stessa chiave di F-Droid



Dopo l'installazione manuale, l'applicazione funzionerà in modo identico. Si noti che gli aggiornamenti non saranno automatici: sarà necessario controllare periodicamente GitHub per le nuove versioni.



### Google Play Store vs F-Droid



Aegis Authenticator è disponibile sia su Google Play Store che su F-Droid, offrendo la possibilità di scegliere il metodo di installazione:



**Google Play Store:**




- ✅ Aggiornamenti automatici integrati nel sistema Android
- ✅ Installazione semplice e familiare
- ✅ Stesso APK firmato come su altri canali



**F-Droid (consigliato) :**




- ✅ Negozio gratuito e open source
- ✅ Costruzione riproducibile e verificabile
- ✅ Non è richiesto il servizio Google
- ✅ Rispetto per la filosofia del software libero



La scelta tra queste due opzioni dipende dalle vostre preferenze riguardo all'ecosistema Google. Se preferite la semplicità, il Play Store è l'ideale. Se si desidera un approccio più rispettoso della privacy, indipendente dai servizi di Google, F-Droid è la scelta migliore.



## Prima configurazione



Quando Aegis viene lanciato per la prima volta, viene proposta una procedura di configurazione iniziale per proteggere il codice 2FA:



![Configuration initiale Aegis](assets/fr/01.webp)



*Processo di configurazione iniziale di Aegis: schermata di benvenuto, scelte di sicurezza, definizione e finalizzazione della master password*



### Impostare una password principale



Aegis chiederà innanzitutto di scegliere una password principale. Questa password verrà utilizzata per criptare tutti i token di autenticazione memorizzati nel vault. Si consiglia vivamente di impostare una password forte e unica che solo voi conoscerete.



**⚠️ Attenzione:** non dimenticate questa password: se la perdete, i codici 2FA criptati diventeranno inaccessibili (non c'è una backdoor). Aegis chiederà di inserire la password due volte per conferma.



### Abilitazione dello sblocco biometrico (opzionale)



Se il vostro dispositivo Android è dotato di un lettore di impronte digitali o di un altro sensore biometrico, Aegis vi chiederà di attivare lo sblocco biometrico. Questa opzione è facoltativa ma molto pratica: consente di sbloccare rapidamente l'applicazione con l'impronta digitale o il volto, anziché digitare ogni volta la password.



Si noti che la biometria è una comodità aggiuntiva: la password principale è comunque richiesta se la biometria viene modificata o il dispositivo viene riavviato.



### Scoprire le impostazioni dell'applicazione



Una volta entrati nell'applicazione (il Interface principale è inizialmente vuoto), familiarizzare con le opzioni di configurazione disponibili. Accedere alle impostazioni tramite il menu a discesa in alto a destra dello schermo (tre punti verticali), quindi selezionare "Impostazioni".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface principale Aegis vuoto all'avvio, accesso al menu dei parametri e panoramica delle opzioni disponibili*



Il menu delle impostazioni di Aegis raggruppa diverse sezioni importanti:





- **Aspetto**: Personalizzazione del tema (chiaro, scuro, AMOLED), della lingua e di altre impostazioni visive
- **Comportamento**: Configurare il comportamento dell'applicazione quando interagisce con l'elenco di voci
- **Pacchetti di icone**: gestione e importazione di pacchetti di icone per personalizzare l'aspetto dei vostri account
- **Sicurezza**: Impostazioni per la crittografia, lo sblocco biometrico, il blocco automatico e altri parametri di sicurezza
- **Backup**: Configurare i backup automatici in una posizione a scelta
- **Importazione ed esportazione**: Importazione di backup da altre applicazioni di autenticazione ed esportazione manuale del caveau Aegis
- **Registro di controllo**: Registro dettagliato di tutti gli eventi significativi dell'applicazione



Questa chiara organizzazione consente di configurare Aegis in base alle proprie preferenze ed esigenze di sicurezza.



## Aggiungere un account 2FA



Dopo aver configurato Aegis, passiamo all'essenziale: aggiungere gli account a due fattori. Il processo è semplice e Aegis offre diversi metodi per integrare i codici di autenticazione.



### I tre metodi di aggiunta disponibili



Dalla schermata principale di Aegis Interface, premere il pulsante **+** in basso a destra per accedere alle opzioni di aggiunta. Sono disponibili tre opzioni:





- **Scansione del codice QR**: Scansiona direttamente il codice QR visualizzato dal servizio web
- **Scansione immagine**: Scansiona un codice QR da un'immagine salvata sul dispositivo
- **Inserire manualmente**: Inserire manualmente le informazioni dell'account 2FA



### Esempio pratico: configurazione di Bitwarden



Facciamo un esempio concreto di attivazione della 2FA su Bitwarden per illustrare il processo:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Esempio di attivazione 2FA su Bitwarden: Interface web con le opzioni di autenticazione e la raccomandazione Aegis*





- **Accesso alle impostazioni**: Accedere al proprio account Bitwarden e accedere alle impostazioni, scheda "Sicurezza"
- **Sezione Provider**: Accedere alla sezione "Provider" e fare clic su "Gestisci" nella sezione "Authenticator app"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Processo completo per l'aggiunta di un account: Codice QR visualizzato dal servizio, chiave segreta visibile e codice di verifica inserito*





- **Eseguire la scansione del codice QR**: Si apre una finestra popup con il codice QR e la chiave segreta
- In **Aegis**: Utilizzare "Scansione del codice QR" per acquisire automaticamente le informazioni
- **Verifica**: Inserire il codice a 6 cifre generato da Aegis nel campo "Codice di verifica"
- **Attivazione**: Fare clic su "Attiva" per finalizzare l'attivazione



### Aggiungere manualmente i dettagli



Se preferite o non potete scansionare il codice QR, utilizzate l'opzione "Inserisci manualmente". Il modulo consente di inserire :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Processo di aggiunta di un nuovo account 2FA: Interface vuoto, aggiunta di opzioni, modulo di inserimento manuale e account aggiunto con successo*





- **Nome**: Nome del servizio (es. Bitwarden, GitHub...)
- **Emittente**: L'emittente (spesso identico al nome)
- **Gruppo**: Opzionale, per organizzare i conti per categoria
- **Nota**: Osservazioni personali su questo racconto
- **Segreto**: La chiave segreta fornita dal servizio (mascherata per impostazione predefinita)
- **Avanzato**: Parametri avanzati (algoritmo, periodo, numero di cifre)



Una volta aggiunto, il conto appare nell'elenco con il suo codice attuale e un indicatore di tempo che mostra il tempo rimanente prima del rinnovo.



### Compatibilità universale



Aegis è compatibile con tutti i servizi che utilizzano gli standard TOTP e HOTP, compresi praticamente tutti i siti che offrono 2FA: social network, banche, gestori di password, piattaforme di criptovaluta, ecc.



### Organizzazione dell'ingresso



Una volta aggiunti diversi conti, si apprezzeranno gli strumenti organizzativi di Aegis:





- **Ordinamento personalizzato:** Per impostazione predefinita, i conti sono elencati in ordine alfabetico, ma è possibile modificare l'ordine manualmente
- **Gruppi e categorie:** Create gruppi per separare i vostri account personali da quelli aziendali, oppure raggruppateli per tipo di servizio (banca, e-mail, social network, ecc.)
- **Icone personalizzate:** Aegis cerca di assegnare automaticamente un'icona appropriata se disponibile, altrimenti è possibile scegliere tra molte icone generiche o importare un'immagine
- **Ricerca rapida:** La barra di ricerca in alto consente di digitare poche lettere per filtrare immediatamente le voci corrispondenti



Toccando una voce, il codice OTP viene visualizzato a grandezza naturale (se era nascosto) ed è possibile copiarlo negli appunti con una pressione prolungata, utile per incollarlo nell'applicazione a cui ci si vuole collegare.



## Sicurezza e backup



Poiché la sicurezza è il cuore di Aegis, è importante capire come vengono protetti i codici 2FA e come assicurarne la persistenza in caso di problemi.



### Architettura di sicurezza



**Crittografia robusta**: Tutti i codici vengono memorizzati in una cassaforte criptata utilizzando l'algoritmo **AES-256 in modalità GCM**, insieme alla password principale. La derivazione delle chiavi è basata su **scrypt**, che offre una maggiore protezione contro gli attacchi di forza bruta.



**Sblocco sicuro** : La password principale è necessaria per decifrare i dati. La biometria (opzionale) utilizza **Android Secure Keystore** e TEE (Trusted Execution Environment) per proteggere la chiave di crittografia.



**Autorizzazioni minime**: Aegis funziona offline per impostazione predefinita, richiedendo solo l'accesso alla fotocamera (scansione QR), alla biometria e al vibratore. Nessun dato viene raccolto o condiviso.



### Opzioni di backup



Aegis offre diverse strategie di backup per soddisfare le diverse esigenze di sicurezza e convenienza:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface completo di account aggiunto, avviso di backup, impostazioni di backup automatico e strategie di backup*



**1. Backup locali automatici**




- Configurare una cartella di destinazione a scelta
- Frequenza personalizzabile (dopo ogni cambio, quotidianamente, ecc.)
- File criptati protetti da password (.aesvault)
- Compatibile con le cartelle sincronizzate (Nextcloud, Dropbox, ecc.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Processo di selezione della cartella di backup: file explorer, cartella di destinazione e autorizzazione di accesso*



**2. Backup cloud di Android**




- Integrazione opzionale con il sistema di backup Android
- Disponibile solo per casseforti criptate (sicurezza preservata)
- Backup trasparente con altri dati Android
- Ripristino automatico al cambio di dispositivo



**3. Esportazioni manuali**




- Esportazione su richiesta tramite **Impostazioni > Importazione ed esportazione**
- Scelta del formato crittografato (consigliato) o in chiaro
- Utile per migrazioni o backup occasionali



### Buone pratiche di sicurezza





- Mantenere diverse versioni di **backup** per prevenire la corruzione
- Testate regolarmente **i vostri backup tentando un ripristino**
- Conservare separatamente i codici di recupero forniti dal servizio di assistenza
- La password principale **è sempre necessaria anche con i backup nel cloud**
- **Proteggere la password principale**: utilizzare una password unica e forte memorizzata in un gestore di password
- Mantenete la vostra applicazione **aggiornata** con le ultime patch di sicurezza
- Attivare il **blocco automatico** nelle impostazioni per proteggere l'accesso all'applicazione
- Disattivare gli **screenshot** (opzione predefinita) per evitare che i codici vengano intercettati
- Usare la biometria con parsimonia: preferire le password per gli accessi critici



## Confronto con altre applicazioni



Come si colloca Aegis rispetto alle altre applicazioni di autenticazione più diffuse?



### Aegis vs. Google Authenticator



**Aegis :**




- ✅ Open source e verificabile
- backup locale criptato
- organizzazione avanzata (gruppi, icone, ricerca)
- ✅ Nessuna raccolta dati
- solo Android



**Google Authenticator :**




- disponibile su Android e iOS
- ✅ Sincronizzazione cloud (dal 2023)
- codice sorgente chiuso
- funzionalità limitata
- ❌ Potenziale raccolta dei dati di Google



### Aegis vs Authy



**Aegis :**




- ✅ Open source
- ✅ Nessun account richiesto
- possibilità di esportazione del codice
- controllo totale dei dati
- ❌ Nessuna sincronizzazione multidispositivo nativa



**Authy :**




- ✅ Sincronizzazione multidispositivo
- disponibile su Android e iOS
- codice sorgente chiuso
- richiede un numero di telefono
- ❌ Impossibile esportare i codici
- ❌ Le applicazioni desktop sono state rimosse nel marzo 2024



Aegis eccelle per gli utenti Android che apprezzano la trasparenza, la sicurezza locale e il controllo completo dei propri dati. Alternative come Authy sono più adatte se avete assolutamente bisogno della sincronizzazione automatica tra più dispositivi.




## Conclusione



Aegis Authenticator è una soluzione eccellente per chi cerca un'applicazione 2FA trasparente, sicura e rispettosa della privacy. Il suo approccio open-source, unito a una robusta crittografia e a un'ordinata Interface, lo rende una scelta di prim'ordine per proteggere i vostri account online.



Sebbene sia limitato ad Android e manchi di sincronizzazione cloud nativa, Aegis compensa ampiamente queste limitazioni con la sua filosofia "privacy by design" e il controllo totale dei dati. Per gli utenti preoccupati della propria privacy digitale, Aegis offre un'alternativa credibile e potente alle soluzioni proprietarie dominanti sul mercato.



La sicurezza dei vostri conti online non deve dipendere dalla buona volontà di aziende commerciali. Con Aegis, mantenete il controllo dei vostri codici di autenticazione, in una cassaforte digitale di cui solo voi possedete la chiave.



## Risorse



### Siti web ufficiali




- **Sito web ufficiale**: [getaegis.app](https://getaegis.app/) - Presentazione e download della candidatura
- **Codice sorgente**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Repository ufficiale GitHub
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Installazione tramite il free store



### Documentazione tecnica




- **Documentazione del Vault**: [Progetto del Vault](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Descrizione tecnica della crittografia e dell'architettura sicura
- **FAQ ufficiali**: [getaegis.app/#faq](https://getaegis.app/#faq) - Risposte alle domande più frequenti
- **Wiki del progetto**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Documentazione utente completa
---
name: LineageOS
description: Sistema operativo Android gratuito e non scollato per gli smartphone
---

![cover](assets/cover.webp)



I sistemi Android convenzionali preinstallati sui nostri smartphone pongono una serie di problemi ben noti: l'integrazione intensiva dei servizi Google che porta a un costante tracciamento dei dati, le applicazioni sponsorizzate indesiderate (bloatware) imposte dai produttori e l'abbandono del tracciamento degli aggiornamenti dopo pochi anni, condannando i dispositivi ancora funzionanti a un'obsolescenza programmata.



LineageOS si presenta come una risposta elegante a questi problemi. Prodotto della comunità open source e diretto successore di CyanogenMod (dismesso alla fine del 2016), LineageOS è un sistema operativo mobile gratuito basato su Android che riporta gli utenti al controllo dei propri smartphone. Lanciato ufficialmente nel dicembre 2016, il progetto vanta oggi oltre 4,4 milioni di installazioni attive in tutto il mondo e supporta centinaia di modelli di telefono di oltre 20 marchi diversi.



![lineageos-homepage](assets/fr/01.webp)



*Il sito ufficiale di LineageOS presenta il progetto e i suoi obiettivi*



## Che cos'è LineageOS?



### Filosofia e obiettivi



LineageOS è un sistema operativo mobile open source basato sull'Android Open Source Project (AOSP), sviluppato da una vasta comunità di collaboratori volontari in tutto il mondo. Il suo motto non ufficiale potrebbe essere "Your device, your rules" (il tuo dispositivo, le tue regole): il progetto mira a prolungare la vita degli smartphone offrendo un'esperienza Android semplificata e rispettosa della privacy.



Il progetto è sorto dalle ceneri di CyanogenMod, una delle ROM Android alternative più popolari della storia. Quando CyanogenMod Inc. ha chiuso i battenti nel dicembre 2016, la comunità si è mobilitata per creare LineageOS, mantenendo lo spirito di innovazione e la filosofia open-source che hanno caratterizzato il suo predecessore.



A differenza delle distribuzioni Android OEM, LineageOS non preinstalla alcuna applicazione Google di default ed elimina completamente il bloatware. Gli utenti iniziano con un sistema minimalista che include solo le applicazioni essenziali (telefono, messaggi, fotocamera, browser) e sono liberi di scegliere cosa aggiungere in seguito.



### Impatto e comunità



Le statistiche ufficiali rivelano la portata del progetto: con oltre 4,4 milioni di installazioni attive in 224 Paesi, LineageOS rappresenta una delle alternative Android più adottate al mondo. Il Brasile è in testa con oltre 2 milioni di utenti, seguito da Cina e Stati Uniti, a dimostrazione del fascino universale di un Android libero e personalizzabile.




## Caratteristiche principali



### Interface e esperienza utente



**Android puro**: LineageOS offre un'autentica esperienza Android vicina ad AOSP, senza sovrapposizioni di produttori o applicazioni superflue. Il Interface rimane familiare agli utenti Android e offre una fluidità ottimale grazie all'assenza di bloatware.



**Senza Google per impostazione predefinita**: Nessun servizio Google è preinstallato, per motivi legali ed etici. Questo approccio "Google-free" garantisce un controllo totale sui vostri dati personali e migliora le prestazioni evitando l'esecuzione di servizi in background.



### Personalizzazione e sicurezza



**Personalizzazione avanzata**: LineageOS sblocca molte opzioni non disponibili su Android stock: riconfigurazione dei pulsanti di navigazione, temi di sistema personalizzabili, profili di utilizzo adattati a diversi contesti (lavoro, personale, gioco).



**Outil Trust**: Funzionalità integrata che monitora lo stato di sicurezza del dispositivo e avvisa di potenziali minacce, fornendo una visibilità in tempo reale della sicurezza del sistema.



**Aggiornamenti estesi**: La comunità di LineageOS si impegna a fornire patch di sicurezza mensili, consentendo ai dispositivi dismessi dai produttori di continuare a ricevere le più recenti patch di sicurezza di Android.



## Dispositivi compatibili



LineageOS supporta centinaia di dispositivi di oltre 20 produttori: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone e molti altri. Questa ampia compatibilità è uno dei principali vantaggi del progetto rispetto ad alternative come GrapheneOS, che sono limitate ai dispositivi Pixel.



![devices-compatibility](assets/fr/02.webp)



*Pagina dei dispositivi compatibili con LineageOS con filtri per produttori*



![google-devices](assets/fr/03.webp)



*Dispositivi Google supportati, compreso il Pixel 4 (nome in codice "flame")*



### Dispositivi popolari



Secondo le statistiche ufficiali, i modelli più utilizzati includono una varietà di dispositivi che coprono diverse fasce di prezzo e di età, dimostrando la capacità di LineageOS di dare nuova vita agli smartphone più vecchi e di ottimizzare quelli più recenti.



### Punti cruciali prima dell'installazione



**Bootloader sbloccabile**: Verificare che il produttore/operatore consenta lo sblocco. Alcuni marchi, come Huawei, hanno eliminato questa possibilità sui modelli più recenti, mentre altri impongono procedure specifiche.



**Modello esatto**: È fondamentale scaricare la ROM che corrisponde esattamente al vostro dispositivo. Due modelli con nomi commerciali simili possono differire dal punto di vista tecnico (Galaxy S10 vs S10 5G ad esempio) e richiedere immagini diverse.



**Supporto scalabile**: I dispositivi più recenti potrebbero non essere supportati immediatamente, poiché il porting richiede uno sviluppatore volontario che se ne occupi. Al contrario, il supporto può cessare se il manutentore di un dispositivo si ritira dal progetto.



## Installazione



### Prerequisiti essenziali



⚠️ **Leggere completamente queste istruzioni prima di iniziare** per evitare qualsiasi problema!



**Ripristino del firmware stock (se necessario) :**




- Strumento Android Flash**: Utilizzare lo strumento ufficiale di Google [flash.android.com] (https://flash.android.com) per ripristinare facilmente il dispositivo Pixel ad Android stock dal browser web (è necessario Chrome/Edge)
- Alternativa**: Immagini di fabbrica manualmente da [developers.google.com/android/images](https://developers.google.com/android/images)



**Test prerequisiti obbligatori:**




- Avviare il dispositivo almeno una volta** con il sistema stock originale
- Test di tutte le funzioni**: SMS, chiamate, Wi-Fi, dati mobili
- Importante**: Verificare che sia possibile inviare/ricevere SMS ed effettuare/ricevere chiamate (anche via WiFi e 4G/5G). Se non funziona con il sistema stock, non funzionerà nemmeno con LineageOS!
- Dispositivi recenti**: Alcuni richiedono l'utilizzo di VoLTE/VoWiFi almeno una volta sul sistema stock per fornire IMS



**Preparazione del sistema




- Rimuovere tutti gli account Google** dal dispositivo per evitare la protezione del ripristino di fabbrica, che potrebbe bloccare l'attivazione
- Backup completo** : Il processo cancella completamente il telefono. Backup di foto, contatti, applicazioni e file importanti



**Strumenti ADB e Fastboot:** Seguire la [guida ufficiale LineageOS] (https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) per installare gli strumenti della piattaforma Android SDK. Verificare l'installazione con `adb version` e `fastboot --version`.



**Configurazione del telefono




- Attivare le **Opzioni sviluppatore**: Impostazioni > Informazioni > toccare 7 volte "Numero di build"



![android-version](assets/fr/06.webp)



*Passare a Impostazioni > Informazioni sul telefono per attivare la modalità sviluppatore*





- Abilitare il **debug USB** nelle opzioni dello sviluppatore
- Attivare **OEM Unlock** (essenziale per sbloccare il bootloader)



![developer-options](assets/fr/07.webp)



*Abilita le Opzioni sviluppatore, il debug USB e lo sblocco OEM*



### Installazione dettagliata



⚠️ **Queste istruzioni sono specifiche per LineageOS 22.2. Seguire con precisione ogni passo. Non andare avanti se qualcosa non funziona!



#### Passo 1: Controllo del firmware



**Richiesta di firmware**: Il dispositivo deve avere installato Android 13 prima di continuare (per Pixel 4). Il firmware si riferisce alle immagini specifiche del dispositivo incluse nel sistema stock.



![pixel4-info](assets/fr/04.webp)



*Pagina ufficiale del Pixel 4 con link per il download e guide per l'installazione*



![downloads-page](assets/fr/05.webp)



*Pagina di download della build di LineageOS e file*



**Download specifici di Pixel 4




- Costruire LineageOS**: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- File richiesti**: Scaricate i 3 file necessari da questa pagina (verranno utilizzati nei passaggi successivi):
  - `lineage-22.2-YYYMMDD-nightly-flame-signed.zip` (ROM principale)
  - dtbo.img` (blob della struttura dei dispositivi di partizione)
  - `boot.img` (LineageOS di ripristino)



⚠️ **Importante**: Controllare la versione di Android, non la versione del sistema operativo del produttore. L'utilizzo di una ROM personalizzata (anche LineageOS) non garantisce che questo requisito sia soddisfatto.



💡 **Tip**: In caso di dubbi sul firmware, tornare al sistema stock prima di continuare!



#### Passo 2: sblocco del bootloader



⚠️ **Questo passaggio cancella tutti i dati!





- Testare la connessione ADB**: Collegare il dispositivo via USB e testare con il comando `adb devices` dal terminale del computer



![adb-devices](assets/fr/08.webp)



*Controllare la connessione ADB con il comando `adb devices`*





- Autorizzare la connessione** sul telefono



![usb-debugging-auth](assets/fr/09.webp)



*Debug USB abilitato con l'impronta digitale RSA del computer*





- Avvio in modalità bootloader** :


```
adb -d reboot bootloader
```


Oppure tenere premuto **Volume giù + Accensione** per spegnere il dispositivo





- Controllare la connessione fastboot**:


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*Comandi Fastboot nel terminale per verificare la connessione*



![bootloader-screen](assets/fr/11.webp)



*Display fastboot del Pixel 4 con informazioni di sistema*





- Sbloccare il bootloader** :


```
fastboot flashing unlock
```


Sul dispositivo, utilizzare i tasti del volume per navigare e premere il tasto **Power** per selezionare "Unlock the bootloader" e confermare l'operazione



![unlock-bootloader](assets/fr/12.webp)



*Conferma dello sblocco del bootloader sul dispositivo*



⚠️ **Il telefono si riavvierà automaticamente** dopo la conferma dello sblocco





- Dopo il riavvio automatico**, riabilitare il debug USB nelle opzioni sviluppatore




#### Passo 3: Flash di partizioni aggiuntive



⚠️ **Richiesta per il corretto funzionamento del recupero**





- Riavviare il bootloader**: Volume giù + alimentazione
- Flash** (sostituire `/path/to/` con la cartella in cui è stato scaricato il file) :


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*Flash delle partizioni dtbo e boot.img via fastboot*



#### Passo 4: Installazione del ripristino di LineageOS





- Flash recovery** (sostituire `/path/to/` con la cartella in cui è stato scaricato il file) :


```
fastboot flash boot /chemin/vers/boot.img
```




- Riavviare in recovery** per verificare



#### Passo 5: Installazione di LineageOS





- Riavviare in recovery**: Volume giù + accensione → modalità di recupero



![recovery-mode](assets/fr/14.webp)



*Interface da LineageOS con il menu principale*





- Reset di fabbrica** : Digitare "Reset di fabbrica" → "Formattazione dati / reset di fabbrica"



![factory-reset](assets/fr/15.webp)



*Procedura di ripristino della fabbrica in LineageOS* recovery





- Ritorno al menu principale**
- Caricamento automatico di LineageOS** :
   - Sul dispositivo: "Applica aggiornamento" → "Applica da ADB"
   - Sul PC: `adb -d sideload /path/to/lineageos.zip`



![apply-update](assets/fr/16.webp)



*Selezionare "Applica aggiornamento" e poi "Applica da ADB" nel ripristino*



![sideload-process](assets/fr/17.webp)



*Installazione di LineageOS in corso tramite sideload*



![sideload-terminal](assets/fr/18.webp)



*Comando Sideload nel terminale con l'avanzamento dell'installazione



💡 **Normale**: Il processo potrebbe arrestarsi al 47% o visualizzare errori di "Successo": questo è normale!



#### Fase 6: primo avvio





- Riavvio**: "Riavvia subito il sistema"
- Primo avvio**: Può richiedere fino a 15 minuti



🎉 **Installazione completata!



### Punti di attenzione



⚠️ **Attenzione**: LineageOS viene fornito "così com'è" senza alcuna garanzia. Sebbene ci impegniamo al massimo per garantire che tutto funzioni, l'installazione avviene a proprio rischio e pericolo!



**Controlli critici




- Compatibilità del firmware**: Assicurarsi di verificare la versione del firmware richiesta nella pagina di download del proprio modello
- Mai ribloccare** il bootloader dopo l'installazione di LineageOS
- Seguire le istruzioni specifiche** per il dispositivo in uso



## Configurazione e applicazioni



### Primo avvio


Interface semplificato, vicino ad Android stock, senza Google. Configurazione semplice: lingua, Wi-Fi, nessun account richiesto.



### Applicazioni alternative



**Sorgenti applicative sicure:**



**F-Droid** : Il negozio di applicazioni open source di riferimento, preinstallato con LineageOS per microG o scaricabile direttamente. F-Droid offre solo software open source verificato e compilato in modo trasparente, garantendo l'assenza di tracker o componenti dannosi.



**Aurora Store**: Client anonimo per accedere al Google Play Store senza un account Google. Aurora prende in prestito gli account anonimi condivisi, consentendo di scaricare le applicazioni più diffuse preservando la propria privacy.



**Applicazioni alternative essenziali





- Navigazione**: Organic Maps (mappe offline basate su OpenStreetMap)
- Comunicazione**: Signal (messaggi crittografati end-to-end), K-9 Mail (client di posta elettronica gratuito)
- Media**: NewPipe (YouTube senza pubblicità e senza tracciamento), VLC (lettore multimediale universale)
- Produttività**: Nextcloud (cloud self-hosting), Simple Calendar (sincronizzazione CalDAV)
- Sicurezza**: Bitwarden (gestore di password), Aegis Authenticator (codici 2FA)



Queste applicazioni, la maggior parte delle quali sono disponibili tramite F-Droid, formano un ecosistema coerente che può sostituire completamente i servizi di Google, offrendo al contempo un'esperienza utente moderna e funzionale.



## Uso e manutenzione



### Esperienza quotidiana



LineageOS trasforma l'esperienza Android, dando priorità alla fluidità e alla reattività. La snella Interface è particolarmente efficace sui dispositivi più vecchi, che ricevono una nuova vita, con prestazioni generalmente superiori alle ROM del produttore grazie all'assenza di pesanti overlay e processi superflui.



Le funzionalità di base (chiamate, SMS, foto, navigazione) funzionano senza problemi, mentre gli strumenti di personalizzazione consentono di adattare il sistema alle preferenze individuali senza comprometterne la stabilità.



### Sistema di aggiornamento OTA



LineageOS dispone di un sistema di aggiornamento Over-The-Air particolarmente semplice da utilizzare. Le nuove versioni vengono proposte automaticamente tramite notifiche e l'installazione richiede solo pochi clic, senza bisogno di complessi interventi tecnici. Il processo preserva completamente i dati e le applicazioni installate.



Questi aggiornamenti regolari sono una risorsa importante, soprattutto per i dispositivi dismessi dai produttori, che possono continuare a beneficiare delle ultime patch di sicurezza Android.



### Migliori pratiche consigliate



**Sicurezza post-installazione:**




- Impostare un PIN o una password forte per lo sblocco
- Verificare che la crittografia dello storage sia abilitata (di solito è un'impostazione predefinita)
- Installare un gestore di password come Bitwarden tramite F-Droid



**Manutenzione preventiva




- Aggiornamenti OTA regolari per la sicurezza
- Limitare l'installazione delle applicazioni a fonti affidabili (F-Droid, Aurora Store)
- Rivedere periodicamente le autorizzazioni concesse alle applicazioni
- I riavvii occasionali ottimizzano le prestazioni e liberano memoria



## Vantaggi e limiti



✅ **Benefici:**




- Privacy predefinita (nessun tracciamento da parte di Google)
- Ampia compatibilità (oltre 300 modelli)
- Prestazioni superiori (nessun bloatware)
- Aggiornamenti estesi sui dispositivi più vecchi



❌ **Limitazioni:**




- Installazione tecnica
- Niente Android Auto/Google Pay
- Le app bancarie possono essere problematiche



## GrapheneOS vs LineageOS: qual è la differenza?



### Approcci distinti



**GrapheneOS** si concentra esclusivamente sulla massima sicurezza e viene eseguito solo sui Google Pixel per sfruttare i loro chip di sicurezza dedicati. Il sistema incorpora numerose mitigazioni avanzate contro gli exploit e rafforza notevolmente il sandboxing delle applicazioni.



**LineageOS** bilancia sicurezza, privacy e convenienza sul maggior numero possibile di dispositivi. L'approccio è più pragmatico e punta a una compatibilità estesa piuttosto che alla sicurezza assoluta.



### Gestione dei servizi Google



**GrapheneOS**: Offre un sistema Google Play sandboxed opzionale. Google Play può essere installato ma viene eseguito in una sandbox rigorosa, senza privilegi speciali di sistema. Questo approccio unico permette di utilizzare l'ecosistema Google mantenendo un controllo di sicurezza rigoroso.



**LineageOS**: Permette all'utente di scegliere se installare i servizi Google (GApps), microG (alternativa gratuita) o se rimanere completamente libero da Google. Massima flessibilità per soddisfare le vostre esigenze.



### Confronto tecnico



| **Aspect** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibilité** | Pixels uniquement | Centaines d'appareils |
| **Sécurité** | Mitigations avancées | Sécurité AOSP standard |
| **Google Play** | Sandboxé optionnel | Installation classique possible |
| **Installation** | Interface web + USB | Procédure manuelle technique |
| **Philosophie** | Sécurité avant tout | Équilibre et liberté de choix |

### Raccomandazioni per l'uso



**Scegliete GrapheneOS** se possedete un Pixel, se la massima sicurezza è la vostra priorità e se accettate vincoli per una maggiore protezione.



**Scegliete LineageOS** se avete un dispositivo non-Pixel, se cercate un buon equilibrio tra privacy e praticità o se volete scegliere il vostro livello di compromesso con l'ecosistema Google.



## Conclusione



LineageOS offre un'alternativa matura per riprendere il controllo del vostro smartphone Android. Esperienza libera, prestazioni ottimali, ampia compatibilità: la scelta ideale per combinare privacy e praticità quotidiana.



## Risorse



### Documentazione ufficiale




- [Sito ufficiale di LineageOS](https://lineageos.org)
- [Wiki LineageOS](https://wiki.lineageos.org) - Guide all'installazione per modello
- [LineageOS per microG](https://lineage.microg.org) - Versione con microG integrato



### Comunità




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Account Mastodon @LineageOS](https://fosstodon.org/@LineageOS)



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
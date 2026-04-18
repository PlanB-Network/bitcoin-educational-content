---
name: White Noise
description: Un'applicazione di messaggistica privata e decentralizzata basata sui protocolli Nostr e MLS
---

![cover](assets/cover.webp)


## Introduzione

>Nel mezzo delle difficoltà si nasconde un'opportunità.

Questa citazione di Albert Einstein ci ricorda che i problemi non sono definitivi, ma contengono al loro interno i semi di nuove soluzioni innovative.

Le motivazioni alla base del lancio della soluzione che presentiamo in questo tutorial lo illustrano perfettamente. Si tratta di **White Noise**, nato dalla necessità.

Secondo le parole del suo fondatore, Max Hillebrand, riportate da *Bitcoin Magazine*: « Abbiamo lanciato questo progetto per mancanza di alternative. » Spiega che « le applicazioni di crittografia esistenti sono inefficienti su larga scala: aggiungere 100 persone a una conversazione di gruppo rallenta notevolmente la crittografia. Le piattaforme decentralizzate, inoltre, non offrono messaggistica privata. Infine, la rete open relay di Nostr permette a tutti di diffondere idee, ma la protezione dei messaggi diretti rimane drammaticamente inadeguata. Ci siamo resi conto che, per proteggere la libertà, dovevamo unire questi sistemi. »


## Che cos'è White Noise?

White Noise è un'applicazione di messaggistica open source sviluppata da un team no-profit. L'applicazione promuove la sicurezza, la privacy e la decentralizzazione. A differenza delle applicazioni convenzionali, non richiede né un numero di telefono né un indirizzo e-mail.

White Noise si distingue per l'integrazione di due protocolli fondamentali - Nostr e MLS - che ne costituiscono la base tecnica.

Nostr (Notes and Other Stuff Transmitted by Relays) è un protocollo decentralizzato e open-source progettato per resistere alla censura.  Il protocollo utilizza relay, coppie di chiavi e client.

https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Con White Noise, è possibile anche scegliere le impostazioni del relay per massimizzare la privacy.

MLS (Messaging Layer Security), invece, è un protocollo di sicurezza che consente la crittografia end-to-end dei messaggi. In altre parole, i messaggi sono accessibili solo agli endpoint, cioè il mittente e il destinatario del messaggio. Ciò significa che i relay coinvolti nell'instradamento dei messaggi non possono accedere al loro contenuto.

Ecco un rapido confronto tra White Noise e alcune delle più note applicazioni di messaggistica.

| Punti di comparaziones        | White Noise | Telegram    | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| ----------------------------- | :---------: | :---------: | :-------------: | :-----: | :------: | :--------------: | :-----: |
| Cifratura E2EE / 1:1          | ✅ Sì       | Facoltativa | ✅ Sì           | ✅ Sì   | ✅ Sì    | ✅ Sì            | ✅ Sì  |
| Cifratura dei gruppi E2EE     | ✅ Sì       | ❌ No       | ✅ Sì           | ✅ Sì   | ✅ Sì    | Facoltativa      | ✅ Sì  |
| Anonimizzazione dell'identità | ✅ Sì       | Facoltativa | ❌ No           | ✅ Sì   | ❌ No    | ❌ No            | ❌ No  |
| Server open source            | ✅ Sì       | ❌ No       | ❌ No           | ✅ Sì   | ❌ No    | ❌ No            | ✅ Sì  |
| Client open source            | ✅ Sì       | ✅ Sì       | ❌ No           | ✅ Sì   | ❌ No    | ❌ No            | ✅ Sì  |
| Server decentralizzati        | ✅ Sì       | ❌ No       | ❌ No           | ✅ Sì   | ❌ No    | ❌ No            | ❌ No  |
| Anno di creazione             | 2025        | 2013        | 2009            | 2025    | 2011     | 2011              | 2014   |


## Come iniziare con White Noise

### Installazione di White Noise

Vai al [sito web White Noise](https://www.whitenoise.chat/), quindi fai clic su **Download**.

![screen](assets/fr/03.webp)

White Noise è attualmente disponibile solo sui dispositivi mobili.

Nella nuova interfaccia visualizzata, premi:
- il pulsante **Zapstore** o **Android APK** se vuoi scaricarlo su Android;
- sul pulsante **iOS TestFlight** se si utilizzi un iPhone.

![screen](assets/fr/04.webp)

Ai fini di questa esercitazione, effettueremo un download da Android.

Se scegli di scaricare tramite **Zapstore**, verrai reindirizzato nello store. Una volta su Zapstore, digita **White Noise** nella barra di ricerca. Procedi quindi al download facendo clic su **Install**.

![screen](assets/fr/05.webp)

![screen](assets/fr/06.webp)

Se  scegli di scaricare il file APK, verrai reindirizzato al repository White Noise di GitHub per scegliere la versione giusta per il tuo smartphone.

I file APK disponibili sono:
- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), adatto ai telefoni recenti con processori a 64 bit;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) adatto ai telefoni più vecchi con processori a 32 bit.

Sono presenti anche file **.sha256**, che sono solo checksum per verificare l'integrità del download.

![screen](assets/fr/07.webp)

Una volta completato il download, installa e apri l'applicazione.

![screen](assets/fr/08.webp)

### Configurazione iniziale dell'account utente

Per la prima connessione a White Noise, premi il pulsante **Registra**.

![screen](assets/fr/09.webp)

Quindi, configura il tuo profilo scegliendo una foto, un nome e aggiungendo una breve descrizione di te stesso. Non è necessario inserire la tua identità reale (nome e foto).

Nota che White Noise sceglie automaticamente un nome (pseudonimo) per l'utente, che può essere mantenuto o modificato. Infine, premi il pulsante **Fine**.

![screen](assets/fr/10.webp)

Verrai reindirizzato alla **schermata iniziale** di White Noise, dove saranno elencate le tue conversazioni. Il tuo account è ora configurato e pronto all'uso. È possibile condividere il tuo profilo o cercare amici per iniziare una chat.

![screen](assets/fr/11.webp)

### Scoprire le interfacce di White Noise

Nell'interfaccia principale, nella parte superiore dello schermo, si trova:

Nell'angolo in alto a sinistra, l'icona del profilo è una miniatura della foto del profilo o la prima lettera del nome del profilo. Fai clic su di essa per accedere alle impostazioni dell'account.

![screen](assets/fr/12.webp)

![screen](assets/fr/13.webp)

Nell'angolo in alto a destra si trova l'icona per iniziare una nuova conversazione.

![screen](assets/fr/14.webp)

![screen](assets/fr/15.webp)


## Impostazioni dell'account utente

Premi l'icona del profilo nell'angolo in alto a sinistra per accedere alle impostazioni.

![screen](assets/fr/16.webp)

Nella parte superiore dell'interfaccia **Impostazioni**, troverai la tua foto e il nome del profilo, seguiti dalla tua chiave pubblica, che potrai condividere utilizzando il codice QR accanto ad essa.

![screen](assets/fr/17.webp)

Appena sotto, si trova il pulsante **Cambia account**, che consente di collegarsi a un altro profilo all'interno dell'applicazione.

![screen](assets/fr/18.webp)

Poi c'è una prima sezione con quattro (4) sottomenu come:

- **Modificare il profilo**

In questo sottomenu è possibile modificare il nome del profilo, l'indirizzo Nostr (NIP-05)... Non dimenticarti di fare clic su **Salva** per salvare le modifiche.

![screen](assets/fr/19.webp)

- **Tasti del profilo**

Qui è possibile accedere alle chiavi pubbliche e private (segrete). Come ricorda White Noise, la chiave privata non deve essere divulgata in nessun caso.

![screen](assets/fr/20.webp)

- **Relay di rete**

In questo sottomenu è possibile aggiungere o rimuovere i **relay generali** (relay definiti per l'uso in tutte le applicazioni Nostr), gli **inbox relay** e i **key pack relay**.

Per farlo, tocca l'icona **cestino** davanti a un relay per eliminarlo o toccare l'icona **+** (più) per aggiungerne uno nuovo.

![screen](assets/fr/21.webp)

- **Disconnessione**

Fai clic su questo sottomenu per scollegare l'account dall'applicazione. Assicurati però di aver salvato le chiavi private offline, altrimenti non sarai in grado di accedere nuovamente in seguito.

![screen](assets/fr/22.webp)

Una seconda sezione offre dei sottomenu:

- **Impostazioni dell'applicazione**

Qui è possibile definire l'aspetto (tema e lingua di visualizzazione) dell'applicazione e persino cancellare i dati se ritieni che siano stati compromessi o se ti senti a rischio.

![screen](assets/fr/23.webp)

- **Donazione a White Noise**

È possibile sostenere il team di White Noise (un'organizzazione senza scopo di lucro) con donazioni tramite il loro indirizzo Lightning o il loro indirizzo Bitcoin silent payment.

![screen](assets/fr/24.webp)

Infine, in fondo, ci sono le **impostazioni dello sviluppatore**.

![screen](assets/fr/25.webp)


## Iniziare una conversazione

Vediamo ora come avviare una conversazione. Al momento in cui scriviamo, White Noise offre tre opzioni di comunicazione. Di seguito analizzeremo le **Conversazioni private** (**Chat 1:1**), cioè tra te e un'altra persona, le **Conversazioni di gruppo** e l'**Invio di file multimediali**.

### Chat 1:1

Dall'interfaccia principale, per aggiungere un nuovo utente, clicca sull'icona per iniziare una nuova conversazione.

Quindi scansiona il codice QR della chiave pubblica (1) o incolla la chiave pubblica (2) del nuovo utente nella barra di ricerca per trovarlo.

![screen](assets/fr/26.webp)

Tocca quindi il pulsante **Avvia conversazione** per iniziare una conversazione con l'utente. È anche possibile **seguire** l'utente o invitarlo a una conversazione di gruppo premendo il pulsante **Aggiungi al gruppo**.

![screen](assets/fr/27.webp)

Il primo messaggio a un nuovo utente è simile a una richiesta di invito. Questa richiesta deve essere accettata dall'utente prima di poter comunicare con lui/lei. Se si rifiuta, non è possibile alcuna conversazione.

![screen](assets/fr/28.webp)

Inoltre, se non accettano il tuo invito, non potranno leggere il contenuto del tuo messaggio iniziale.

Una volta accettato l'invito, l'utente può rispondere e comunicare in modo sicuro e senza interruzioni.

![screen](assets/fr/29.webp)

Inoltre, in una discussione sono disponibili ulteriori funzionalità.

È possibile premere a lungo su un messaggio specifico per visualizzare opzioni quali:
- reagire al messaggio con un emoji (1);
- fare una **citazione diretta** per rispondere al messaggio premendo **Reply** (2);
- copiare il messaggio premendo **Copia** (3).

![screen](assets/fr/30.webp)

- elimina un messaggio con il pulsante **Elimina** solo se proviene da te.

![screen](assets/fr/31.webp)

È possibile effettuare ricerche all'interno di una conversazione.

Fai clic sull'avatar dell'utente nella parte superiore dello schermo per accedere alle "informazioni sulla conversazione" e tocca il pulsante **Cerca nella conversazione**.

![screen](assets/fr/32.webp)

![screen](assets/fr/33.webp)

Nella barra di ricerca visualizzata, digita la parola che desideri cercare e avvia la ricerca. Le parole ricercate saranno evidenziate in **grassetto**.

![screen](assets/fr/34.webp)

### Conversazioni di gruppo

Le conversazioni di gruppo possono essere avviate su White Noise.

A tal fine, tocca l'icona nell'interfaccia di avvio della nuova conversazione, quindi fai clic su **Nuova conversazione di gruppo**. Quindi, nella barra di ricerca, inserisci la chiave pubblica del primo membro che desideri aggiungere al gruppo.

![screen](assets/fr/35.webp)

![screen](assets/fr/36.webp)

Eventualmente, se questa opzione non funziona, dall'interfaccia **Avvia una nuova conversazione**, inserisci nella barra di ricerca la chiave pubblica del primo membro che vuoi aggiungere al gruppo. È anche possibile scansionare il codice QR associato alla sua chiave pubblica.

Questa volta, invece di toccare il pulsante **Avvia conversazione**, fai clic sul pulsante **Aggiungi al gruppo**.

![screen](assets/fr/37.webp)

Nel menu a comparsa che appare, tocca **Nuova conversazione di gruppo**.

![screen](assets/fr/38.webp)

Quindi premi **Continua** (non è necessario inserire nuovamente la chiave pubblica).

![screen](assets/fr/39.webp)

Come creatore del gruppo, ne sei automaticamente l'amministratore. Compila i dettagli del gruppo, come **nome e descrizione del gruppo**, quindi fai clic sul pulsante **Crea gruppo**.

![screen](assets/fr/40.webp)

L'utente aggiunto come primo membro e tutti gli altri aggiunti successivamente ricevono una notifica che li invita a unirsi al gruppo. Devono accettare facendo clic su **Accetta** per unirsi al gruppo.

![screen](assets/fr/41.webp)

È anche possibile aggiungere un nuovo membro con cui si sta già chattando a un gruppo esistente. Per farlo, clicca sull'avatar dell'utente nella parte superiore dello schermo per accedere alle "informazioni sulla conversazione" e tocca il pulsante **Aggiungi al gruppo**.

![screen](assets/fr/42.webp)

Nella nuova interfaccia che appare, **seleziona** il gruppo a cui si desidera aggiungerlo e tocca **Aggiungi al gruppo**. Non resta che attendere che accetti di unirsi al gruppo.

![screen](assets/fr/43.webp)

Nota che solo l'amministratore del gruppo può modificare le informazioni del gruppo e aggiungere o espellere membri. Inoltre, la rotazione delle chiavi impedisce ai membri vietati di decifrare i messaggi futuri.

Per rimuovere un membro, dall'interfaccia principale del gruppo, tocca l'icona del gruppo in alto per accedere all'interfaccia delle informazioni sul gruppo.

![screen](assets/fr/44.webp)

![screen](assets/fr/45.webp)

Quindi fai clic sul nome del membro e su **Rimuovi dal gruppo**. Da questa interfaccia è anche possibile inviargli un messaggio, seguirlo o aggiungerlo a un altro gruppo.

![screen](assets/fr/46.webp)

### Invio di file multimediali

Per il momento, su White Noise è possibile condividere solo foto tra utenti. Sia che si tratti di una conversazione privata o di una chat di gruppo, per farlo è necessario:

- premi il simbolo **più (+)** a sinistra del campo di immissione del messaggio di testo.

![screen](assets/fr/47.webp)

- quindi fai clic sulla casella **Foto** in basso per accedere alla tua galleria.

![screen](assets/fr/48.webp)

- scegli le foto da inviare.

![screen](assets/fr/49.webp)

![screen](assets/fr/50.webp)

![screen](assets/fr/51.webp)


## Punti chiave da ricordare

White Noise offre un buon livello di riservatezza e una sicurezza superiore. D'altra parte, si tratta di un'applicazione molto recente, poco diffusa e ancora agli inizi. Di conseguenza, è ancora troppo presto per trarre conclusioni concrete. È possibile riscontrare alcuni malfunzionamenti durante l'uso.

Attualmente, manca di alcune funzionalità (nessuna chiamata audio o video, nessun invio di file multimediali audio o video) rispetto alle applicazioni di messaggistica più diffuse.

Ciononostante, White Noise rimane un'opzione interessante per le conversazioni in cui la riservatezza è fondamentale (ad esempio con la famiglia, gli amici più stretti o gli attivisti di una causa comune), anche se richiede un po' di impegno per l'installazione (tramite store di applicazioni alternativi o file APK) e l'apprendimento (padroneggiando un po' il concetto di coppie di chiavi, client e relay con il protocollo Nostr).

Ora sai come utilizzare White Noise per comunicare in modo sicuro con i tuoi amici e familiari. Se questa esercitazione ti è stata utile, metti un pollice in su.

Raccomandiamo il nostro tutorial su Tox Chat, un'applicazione che consente di chattare senza intermediari attraverso il protocollo decentralizzato Tox.

https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3

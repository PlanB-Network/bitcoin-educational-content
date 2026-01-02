---
name: Bitchat
description: Messaggistica decentralizzata, senza Internet, per una comunicazione gratuita
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Questo video tutorial di BTC Sessions illustra il processo di impostazione e utilizzo di Bitchat!


Bitchat è nato da uno sforzo di prototipazione rapida in cui [@jack](https://primal.net/jack) ha sviluppato il concetto iniziale durante una sessione di codifica nel fine settimana. [@calle](https://primal.net/calle) si è unito al progetto poco dopo per co-sviluppare l'implementazione Android. Attualmente Jack è a capo dello sviluppo della versione iOS, mentre calle supervisiona la versione Android con il supporto di molti altri collaboratori.


## Introduzione: Chattare liberamente, senza rete


Immaginate di inviare messaggi quando Internet non funziona, durante un disastro naturale o in luoghi in cui le comunicazioni sono limitate. Bitchat lo rende possibile. Si tratta di un'applicazione di messaggistica decentralizzata, peer-to-peer, che salta i server centrali e permette ai dispositivi di parlare direttamente tra loro, completamente offline, utilizzando il Bluetooth e la rete mesh. Progettata tenendo conto della privacy e della resilienza, Bitchat è ideale per l'uso in aree in cui la connettività tradizionale è inaffidabile o non disponibile, ad esempio in caso di catastrofi, in luoghi remoti o per chi vuole evitare la sorveglianza. Il Bitchat utilizza la crittografia per garantire che ogni messaggio sia crittografato end-to-end, verificato e a prova di manomissione.


In questo tutorial vi mostreremo come funziona Bitchat e come potete utilizzarlo per una comunicazione veramente privata e offline.


## 🚀 Caratteristiche principali


Il Bitchat consente la messaggistica offline attraverso queste [funzioni] (https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Compatibilità multipiattaforma**: Piena compatibilità del protocollo tra iOS e Android.
- Rete mesh decentralizzata**: Individuazione automatica dei peer e trasmissione di messaggi multi-hop tramite Bluetooth Low Energy (BLE)
- Crittografia end-to-end**: Scambio di chiavi X25519 + AES-256-GCM per i messaggi privati
- Chat basate su canali**: Messaggistica di gruppo basata su argomenti con protezione opzionale tramite password
- Store & Forward**: Messaggi memorizzati nella cache per i peer offline e consegnati quando si riconnettono
- La privacy prima di tutto**: Nessun account, nessun numero di telefono, nessun identificatore persistente
- Comandi in stile IRC: Interfaccia familiare in stile `/join, /msg, /who`.
- Conservazione dei messaggi**: Salvataggio opzionale dei messaggi a livello di canale, controllato dai proprietari del canale
- Cancellazione di emergenza**: Toccare tre volte il logo per cancellare istantaneamente tutti i dati
- Moderna interfaccia utente Android**: Jetpack Compose con Material Design 3
- Temi scuro/luminoso**: Estetica ispirata ai terminali, in linea con la versione iOS
- Ottimizzazione della batteria**: Scansione e gestione energetica adattive


## 1️⃣ Come funziona il Bitchat - semplicemente


Bitchat consente di inviare messaggi ai telefoni vicini direttamente tramite Bluetooth (`BLE` come segue), senza bisogno di Internet o del segnale cellulare. Quando si avvia una chat, i telefoni eseguono una stretta di mano sicura per creare una chiave di crittografia unica e temporanea per la conversazione. Ogni messaggio è protetto dalla crittografia end-to-end e per ognuno di essi viene utilizzata una nuova chiave per garantire che i messaggi passati rimangano al sicuro anche se il telefono viene compromesso in seguito. Infine, l'applicazione divide i messaggi in piccoli pezzi e li mescola con dati fittizi casuali per nascondere la vostra attività di messaggistica. Per le chat dirette da dispositivo a dispositivo, funziona solo in un raggio d'azione di circa 100 metri. È come passarsi note criptate in una stanza affollata: i dispositivi sussurrano direttamente tra loro, distruggendo le chiavi dopo ogni messaggio.


Bitchat consente anche di unirsi a chat room basate sulla localizzazione utilizzando il protocollo Nostr e `#geohashes`. Un geohash è un codice breve, come `#u33d`, che rappresenta una specifica area geografica, da un singolo quartiere fino a un'intera città o regione. È possibile "teletrasportarsi" in qualsiasi chat room geohash del mondo semplicemente inserendo il suo tag. I messaggi vengono inviati attraverso una rete decentralizzata di relay, che protegge la vostra posizione esatta. Inoltre, ogni volta che ci si unisce a una stanza geohash, si riceve una nuova identità temporanea, che aggiunge un ulteriore livello di privacy alle conversazioni basate sulla posizione.


Per dettagli tecnici più precisi, consultare il [Whitepaper ufficiale](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## installazione e configurazione di 2️⃣


### Dove trovare il Bitchat


È possibile installare il Bitchat attraverso:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (per dispositivi iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (per dispositivi Android)


Anche gli utenti Android hanno a disposizione opzioni alternative:



- Scaricare l'APK direttamente dalla pagina [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) oppure
- Installare tramite [Zapstore] compatibile con Nostr(https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Nota**: questa esercitazione si concentra principalmente sull'implementazione Android. La versione iOS potrebbe essere diversa


### Processo di impostazione


Dopo l'installazione, aprire Bitchat per visualizzare la schermata iniziale dei permessi. Ecco cosa dovete fare:


1. **concedere i permessi richiesti:**


   - Accesso Bluetooth** (per scoprire gli utenti Bitchat nelle vicinanze)
   - Posizione precisa** (Android lo richiede per la funzionalità Bluetooth)
   - Notifiche** (per ricevere avvisi di messaggi privati)

2. **Disattivare l'ottimizzazione della batteria**:


   - In questo modo Bitchat può essere eseguito in background
   - Mantiene costantemente le connessioni della rete mesh


Toccate "Concedi permessi", seguite le "istruzioni" e "Disattiva ottimizzazione batteria" per passare alla schermata successiva.


![image](assets/en/02.webp)


Benvenuti nella schermata principale del Bitchat. Orientiamoci:


### Impostazioni


Prima di tutto. Il menu delle impostazioni si apre toccando il "logo Bitchat".  Sono disponibili le seguenti opzioni:



- Impostare l'aspetto (sistema/luce/scuro).
- abilitare la `prova di lavoro` a geohash per scoraggiare lo spam (opzionale)
- Attivare `Tor` per migliorare la privacy.


![image](assets/en/16.webp)


### Impostare la propria identità


Toccare il campo `bitchat/anonXXXX` in alto per scegliere il proprio nome utente. Questo è il modo in cui gli altri vi vedranno sia in modalità Bluetooth che in modalità Internet. Ad esempio, si può cambiare "anon2022" con un nome utente di propria scelta.


![image](assets/en/03.webp)


### Selezionare i canali di rete


Utilizzare il menu `#canali di localizzazione` (a destra del nome utente) per passare da un tipo di connessione all'altro:



- BLE Mesh***: Modalità Bluetooth predefinita (senza internet, da 10 a 50 metri di portata)
- #geohashes**: Comunità geografiche abilitate a Internet che utilizzano il [protocollo Nostr](https://nostr.com/)


Quando si seleziona la modalità `#geohashes`, Bitchat si integra con il protocollo Nostr per abilitare le comunità geografiche. I messaggi vengono pubblicati su "relay decentralizzati" di Nostr piuttosto che sulla rete peer-to-peer di Bitchat, consentendo conversazioni più ampie ma filtrate dal luogo. In particolare, le vostre chiavi di identità Bitchat firmano crittograficamente tutti gli eventi Nostr per mantenere l'autenticazione, mentre i tag geohash (come `#u4pruyd` per un quartiere) filtrano i messaggi al livello di precisione scelto. Ciò significa che è possibile partecipare alle discussioni locali senza rivelare le coordinate esatte, anche se è necessario l'accesso a Internet.


![image](assets/en/04.webp)


### Monitoraggio dei pari

licenza: CC-BY-SA-V4

Il contatore peer mostra gli utenti:



- Nelle vicinanze (rete BLE) o
- Nella tua zona geohash (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Chat globale e messaggi privati


Il Bitchat offre due modalità di comunicazione distinte per soddisfare le diverse esigenze:



- Canali pubblici:** Per conversare apertamente con gli altri. È possibile connettersi attraverso la rete locale BLE mesh per gli utenti vicini o attraverso un #geohash globale per le comunità basate sulla posizione e abilitate a Internet.
- Messaggi privati:** Per conversazioni sicure a tu per tu. Questi messaggi stabiliscono una connessione diretta e crittografata per mantenere riservati gli scambi.


La comprensione di entrambe le modalità vi aiuterà a orientarvi nelle conversazioni.


### Canali pubblici: Il Community Hub


Il menu `#canali di localizzazione` (in alto a destra) controlla la visibilità pubblica. Selezionando `mesh` ci si connette a tutti gli utenti vicini tramite BLE mesh, in genere dispositivi nel raggio di 10-50 metri. In questo modo si crea un forum aperto in cui i messaggi vengono trasmessi a tutti coloro che si trovano nel raggio d'azione, ideale per annunci di eventi o avvisi locali.


Per una portata geografica più ampia, scegliete un qualsiasi tag `#geohash` per unirvi a comunità alimentate da Internet e filtrate per località. Questi canali utilizzano i relè del protocollo Nostr, consentendo la comunicazione tra città o regioni diverse, pur mantenendo la rilevanza della località. I vostri messaggi appaiono in diretta agli altri utenti dello stesso canale e i nuovi partecipanti vedono automaticamente la cronologia dei messaggi recenti al momento dell'iscrizione.


![image](assets/en/06.webp)


### Conversazioni private: Sicure e crittografate


Per avviare una conversazione privata, toccare direttamente qualsiasi "nome utente" visualizzato nella "Panoramica degli utenti". È inoltre possibile toccare l'icona "stella" per contrassegnare l'utente come preferito, in modo da mantenerlo visibile nell'elenco dei contatti anche quando è offline.


![image](assets/en/07.webp)


Bitchat avvia automaticamente il suo "handshake di sicurezza" quando si avvia una chat privata. I dispositivi si scambiano chiavi effimere per creare un tunnel crittografato specifico per la conversazione. Questo processo garantisce che tutti i messaggi e i file condivisi rimangano riservati grazie alla crittografia end-to-end continua. I messaggi privati supportano la condivisione di testi e file.


![image](assets/en/08.webp)


## 4️⃣ Caratteristiche aggiuntive


È possibile accedere immediatamente al pannello delle azioni digitando `/` in un punto qualsiasi del Bitchat. Questo rivela un menu di comandi per azioni rapide.



- Gestire le connessioni**: bloccare gli utenti" o "Sbloccare i pari"
- Controlli dei canali**: mostra canali" o "Unisci/crea canale"
- Interazioni sociali**: `Abbracciare calorosamente` o `schiaffeggiare con la trota` 🎣
- Manutenzione della chat**: cancella i messaggi della chat
- Strumenti per la privacy**: vedere chi è online" o "Inviare un messaggio privato"


I comandi vengono eseguiti immediatamente, come `/blocca Satoshi` per mettere a tacere i critici o `abbraccia Hal` per diffondere positività 🫂.


![image](assets/en/09.webp)


## 5️⃣ Creare un canale


I canali in Bitchat consentono di organizzare la comunicazione su argomenti, luoghi o comunità. Per creare il vostro canale, seguite questo flusso di lavoro:


### Passo 1: creare un canale


Per creare un canale, digitate `/j` o `/join` seguito dal `nome del canale` in qualsiasi chat (ad esempio, `/j <nome del canale>`). Dopo la creazione appare una nuova `icona ⧉` che indica il nuovo canale. Altri utenti possono unirsi digitando lo stesso comando (ad esempio, `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Passo 2: Configurazione delle impostazioni


Oltre ai comandi predefiniti, all'interno di un canale sono disponibili le seguenti impostazioni:



- `/save` per salvare i messaggi localmente
- `/transfer` per trasferire la proprietà del canale e
- `/pass` per cambiare la password del canale.


Per le comunità private, questo comando abilita la protezione con password, richiedendo ai membri approvati di inserire una password personalizzata prima di unirsi.


## 6️⃣ Modalità Panico


Parliamo ora della modalità `panico`: toccando tre volte il logo `Bitchat` si avvia una cancellazione completa di tutti i messaggi e i dati locali all'interno dell'applicazione. È l'ultima salvaguardia della privacy, perfetta per le situazioni che richiedono una discrezione immediata.


**Promemoria importante:** La modalità panico è permanente. Una volta attivata, i dati non possono essere recuperati. Usare con cautela


![image](assets/en/11.webp)


## 7️⃣ Geohashes


I canali Geohash consentono conversazioni mirate basate sulla "posizione geografica" piuttosto che sulle tradizionali connessioni di rete. Questa funzione trasforma bitchat in uno strumento di comunicazione consapevole della posizione, ideale per il coordinamento locale, la creazione di comunità e le discussioni specifiche del luogo.


### Come funziona `#geohashes


Il sistema divide il mondo in quadrati di griglia utilizzando il [Geohash system](https://en.wikipedia.org/wiki/Geohash), dove ogni carattere dell'hash rappresenta una maggiore precisione:



- Livello 4** (ad esempio, `u33d`): Copre circa 25 km × 25 km - ideale per discussioni a livello cittadino
- Livello 6** (ad esempio, `u33d8z`): Copre circa 1,2 km × 1,2 km - precisione del quartiere
- Livello 8** (ad esempio, `u33d8z1k`): Copre circa 150 m × 150 m - precisione del segmento stradale


La selezione di precisione bilancia la privacy con l'utilità: livelli più alti creano zone più esclusive, ma rivelano la vostra posizione in modo più preciso.


### Unirsi ai canali `#geohash


1. Accedere al menu `#canali di localizzazione`.

2. Selezionare il livello di precisione desiderato e inserire il `#geohash` (ad esempio, #u33d)

3. Toccare il pulsante `Teleport` per unirsi al `canale di localizzazione`.


![image](assets/en/12.webp)


In alternativa, è possibile toccare l'icona `mappa` per utilizzare la vista mappa per determinare il livello di precisione e toccare `seleziona` per unirsi al `canale di localizzazione`.


![image](assets/en/13.webp)


**Promemoria importante**: la funzionalità _#geohash richiede una connessione internet attiva - a differenza del BLE mesh che funziona offline tramite Bluetooth._


## 8️⃣ Heatmaps


Le heatmap sono un modo interessante per scoprire gli eventi e i canali del Bitchat in tutto il mondo. [Bitmap](https://bitmap.lat/) visualizza e tiene traccia dei messaggi anonimi, basati sulla posizione, attraverso la rete Nostr, mostrando gli eventi effimeri della Nostr. Date un'occhiata e partecipate ai canali e alle chat specifiche per ogni luogo.


![image](assets/en/15.webp)


## 🎯 Conclusione


Il Bitchat consente una comunicazione sicura e decentralizzata per gli scenari in cui la messaggistica tradizionale fallisce. È in grado di operare senza infrastrutture internet grazie alla rete mesh BLE, che lo rende adatto a proteste, zone disastrate e aree remote dove la connettività è limitata o censurata. L'applicazione garantisce la privacy grazie alla crittografia a chiave effimera, ai canali di localizzazione basati su geohash e alla cancellazione dei dati in modalità panico.


L'applicazione è ancora nelle prime fasi di sviluppo, ma si sta già dimostrando promettente. Gli utenti devono aspettarsi bug occasionali e segnalare i problemi tramite [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Sono previsti miglioramenti, tra cui l'integrazione di `ecash` per le transazioni private in-app utilizzando il protocollo Cashu.


![image](assets/en/14.webp)


## 📚 Risorse Bitchat


[Github](https://github.com/permissionlesstech) | [Sito web ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)
---
name: Zen Browser
description: Come utilizzare Zen Browser per una navigazione produttiva e riservata?
---

![cover](assets/cover.webp)

Nell'attuale panorama dei browser web, Google Chrome domina con oltre il 65% di quota di mercato, ma questa egemonia solleva importanti questioni sulla privacy e sulla diversità tecnologica. Chrome, come la maggior parte dei browser più diffusi, raccoglie massicciamente dati di navigazione per alimentare gli algoritmi pubblicitari di Google.

![Parts de marché des navigateurs](assets/fr/01.webp)

Di fronte a questa realtà, stanno emergendo nuovi browser con una filosofia diversa: conciliare un'esperienza utente moderna con il rispetto della privacy. Zen Browser, lanciato nel 2024, fa parte di questo approccio, offrendo un'alternativa innovativa basata su Firefox ma riprogettata per gli utenti di oggi.

Zen Browser si distingue per la sua unica interfaccia con schede verticali, spazi di lavoro per organizzare le sessioni e funzioni di produttività come la Split View. Ma al di là di queste innovazioni ergonomiche, è soprattutto il suo impegno nella privacy che lo rende interessante: nessuna telemetria, protezione anti-tracciamento rafforzata e sviluppo trasparente della community.

In questa esercitazione scopriremo come Zen Browser può trasformare il modo di navigare combinando produttività, personalizzazione e privacy.


## Installazione del browser Zen

### Download ufficiale

Zen Browser è disponibile per Windows, macOS e Linux. Visita il sito ufficiale: zen-browser.app/download

![Site officiel Zen Browser](assets/fr/02.webp)

Il sito rileva automaticamente il sistema e propone il link appropriato:

![Page de téléchargement](assets/fr/03.webp)

- **Windows**: programma di installazione .exe per Windows 10/11 (versioni x64 e ARM64)
- **macOS**: immagine disco .dmg compatibile con Intel e Apple Silicon (macOS Monterey e successivi)
- **Linux**: sono disponibili diverse opzioni:
  - **Flatpak** (consigliato): `flatpak install flathub app.zen_browser.Zen`
  - **AppImage**: portatile, direttamente eseguibile
  - **Archivio tar.gz**: da estrarre manualmente
  - **AUR** (Arch Linux): pacchetto Zen-browser.

### Installazione passo-passo

**Su Windows**:
- Scarica il file .exe
- Esegui il programma di installazione (se SmartScreen avvisa, fare clic su "Informazioni aggiuntive" e poi su "Esegui comunque")
- Scegli la directory di installazione
- Lascia selezionata l'opzione "Avvia Zen Browser" per iniziare immediatamente

**Su macOS**:
- Scarica il file .dmg
- Monta l'immagine del disco
- Trascina Zen Browser nella cartella Applicazioni
- Al primo avvio: fai clic con il tasto destro del mouse > "Aprire" per passare a Gatekeeper

**Su Linux**:
- **Flatpak**: installazione automatica tramite il gestore di pacchetti
  - **AppImage**: `chmod +x ZenBrowser.AppImage` quindi fare doppio clic su
  - **tar.gz**: Estrai ed esegui l'eseguibile di zen-browser

### Primo lancio e configurazione iniziale

All'avvio iniziale, Zen Browser guida l'utente attraverso diverse fasi di configurazione:

![Import de données](assets/fr/04.webp)

_Importazione facoltativa dei dati da un altro browser (preferiti, cronologia, password)_

![Configuration initiale](assets/fr/05.webp)

_Scelta del motore di ricerca predefinito e configurazione delle schede_

![Personnalisation visuelle](assets/fr/06.webp)

_Seleziona il colore dell'area di lavoro e convalida l'accesso al browser_

![Page d'accueil Zen Browser](assets/fr/07.webp)

_Pagina iniziale di Zen Browser con la caratteristica barra laterale_


## Presentazione di Zen Browser

**Zen Browser** è un browser web libero e open source derivato da Mozilla Firefox, sviluppato da una community di appassionati volontari dal marzo 2024. A differenza dei browser delle grandi aziende tecnologiche, Zen Browser non è sostenuto da alcuna azienda commerciale ed è finanziato esclusivamente dai contributi della sua comunità.

**Nota importante**: Zen Browser è attualmente in versione **Beta**. Sebbene sia stabile per l'uso quotidiano, aspettatati aggiornamenti frequenti e bug occasionali.

La filosofia del progetto è riassunta dallo slogan: "Welcome to a calmer Internet". Questo approccio si traduce in un browser che si preoccupa della tua esperienza utente piuttosto che dei tuoi dati personali, cercando il perfetto equilibrio tra bellezza, velocità e privacy.

### Un'interfacecia riprogettata per la produttività

Zen Browser rivoluziona l'esperienza di navigazione con diverse innovazioni:
**A differenza dei browser tradizionali, Zen visualizza le schede in una barra laterale verticale anziché orizzontale. Questa scelta ergonomica, ispirata da Arc Browser, massimizza lo spazio di visualizzazione e migliora la navigazione, soprattutto quando si hanno molte schede aperte.**
**Spazi di lavoro**: organizzate le schede per progetto o tema in spazi dedicati. Ad esempio, uno spazio "Lavoro" per le schede professionali, uno spazio "Osservazione" per le schede di lettura e così via. È possibile passare istantaneamente da uno spazio all'altro.
**Split view**: visualizzazione di più siti affiancati in un'unica finestra, ideale per confrontare le informazioni o lavorare su più fonti contemporaneamente.
**Glance**: anteprima di un link in una finestra modale temporanea senza aprire una nuova scheda, perfetta per consultare un riferimento senza perdere il contesto.

### Privacy per impostazione predefinita

Zen Browser integra in modo nativo una forte protezione della privacy:
- **Anti-tracciamento potenziato**: blocco automatico di tracker, cookie di terze parti e script di fingerprinting
- **Telemetria disabilitata**: nessun dato inviato a server esterni
- **DNS su HTTPS**: crittografate le tue richieste DNS per evitare il monitoraggio
- **Riduzione delle dipendenze da Google**: Zen Browser elimina la maggior parte delle connessioni ai servizi di Google, anche se alcune possono rimanere (navigazione sicura, aggiornamenti)

### Personalizzazione avanzata con Zen Mods

Zen offre un ecosistema di personalizzazione unico con **Zen Mods**: una galleria di temi e modifiche creati dalla community per trasformare l'aspetto e il comportamento del browser.

**Mods Zen popolari consigliati**:
- **SuperPins** ⭐: trasforma le schede appuntate in pulsanti stilizzati per un aspetto più professionale dell'interfaccia
- **Coesione**: stile coerente e trasparente che unifica la barra degli URL, la barra laterale e i segnalibri
- **Migliore barra di ricerca**: sposta la barra di ricerca in alto per migliorare l'ergonomia
- **Espansione della barra laterale al passaggio del mouse**: Espansione automatica della barra laterale al passaggio del mouse, per massimizzare lo spazio sullo schermo
- **Migliori schede scaricate**: ottimizza la gestione della memoria con indicatori visivi per le schede inattive
- **Barra URL purificata**: barra dell'interfaccia purificata dell'indirizzo, rimuove gli elementi superflui
- **Zen trasparenze**: eleganti effetti di trasparenza con animazioni fluide.

**Installazione di Zen Mod**:
- Vai alla [galleria ufficiale di Zen Mods](https://zen-browser.app/mods)
- Sfoglia la galleria dei temi disponibili.

![Galerie Zen Mods](assets/fr/12.webp)

- Fai clic su "Installa" per la mod desiderata

![Installation SuperPins](assets/fr/13.webp)

_Esempio: Installazione della famosa mod SuperPins_

- Il tema si applica immediatamente
- È possibile disattivarlo o provarne altri in qualsiasi momento.

Le Zen Mods non si limitano ai temi visivi: alcune modificano il comportamento dell'interfaccia (animazioni, disposizione degli elementi, scorciatoie personalizzate). Questo approccio modulare consente a ciascun utente di creare il proprio ambiente di navigazione ideale.

![Gestion des Zen Mods](assets/fr/16.webp)

_Interfaccia per la gestione parametri dei Mod Zen installati_

**⚠️ Nota importante sulla personalizzazione e sul fingerprinting**:

Più si personalizza Zen Browser (temi, estensioni, mod), più la propria **impronta digitale** diventa unica e quindi rintracciabile. È un compromesso fondamentale:
- **Massima personalizzazione** = esperienza utente ottimale MA impronta unica e facilmente identificabile
- **Configurazione predefinita** = impronta più comune MA esperienza meno personalizzata

Zen Browser ha preferito l'esperienza utente al perfetto anonimato. Se la tua priorità è l'anonimato assoluto, preferisci Tor Browser o Mullvad Browser, che impongono una configurazione uniforme a tutti gli utenti.

Inoltre, essendo basato su Firefox, Zen è compatibile con l'intero ecosistema di estensioni di Firefox.


## Vantaggi e svantaggi

### ✅ Punti salienti

- **Privacy by design**: protezione antitracciamento attiva, telemetria disattivata, nessuna raccolta dati
- **Interfaccia innovativa**: schede verticali, spazi di lavoro, Split View migliorano drasticamente la produttività
- **Aggiornamenti rapidi**: sincronizzazione con Firefox in meno di 72 ore per le patch di sicurezza
- **Personalizzazione avanzata**: temi della community, regolazione fine, compatibilità con le estensioni di Firefox
- **Open source e comunità**: codice trasparente, sviluppo collaborativo, indipendenza dalle Big Tech.

### ❌ Limiti attuali

- **Nessuna versione mobile**: disponibile solo su PC (Windows, macOS, Linux)
- **Incompatibilità DRM**: Netflix, Disney+, Spotify e altri servizi di streaming non funzionano attualmente
- **Progetto giovane**: piccolo team, supporto della comunità, bug occasionali
- **Curva di apprendimento**: interfaccia differente, richiede un adattamento per chi è abituato alle schede orizzontali.


## Configurazione avanzata per la privacy e la sicurezza

Per accedere alle impostazioni del browser Zen:

![Accès aux paramètres](assets/fr/14.webp)

_Fai clic sull'icona del puzzle (estensioni), quindi su "Impostazioni Zen" in basso_

![Interface des paramètres](assets/fr/15.webp)

_Vista generale dei parametri Zen con tutte le schede disponibili_

### Impostazioni predefinite ottimizzate

Fin dall'inizio, Zen Browser applica una configurazione ad alta privacy che supera quella della maggior parte dei browser:
- **Protezione anti-tracciamento rigorosa**: livello "Standard" attivato per impostazione predefinita, che blocca:
  - cookie per il tracciamento dei siti e supercookie
  - script di tracciamento degli annunci (Google Analytics, Facebook Pixel, ecc.)
  - criptominter che utilizzano la tua CPU per mintare criptovalute
  - Impronte digitali tramite Canvas, WebGL e AudioContext
- **Isolamento totale dei cookie**: First Party Isolation impedisce a un sito di leggere i cookie di un altro
- **La telemetria è stata in gran parte disabilitata**: la maggior parte della raccolta dei dati è stata rimossa, anche se alcune connessioni ai servizi di Mozilla/Google potrebbero rimanere e richiedere un'ulteriore configurazione manuale
- **DNS sicuro per impostazione predefinita**: DNS-over-HTTPS abilitato per impedire lo spionaggio delle richieste
- **HTTPS-Only enabled**: forza le connessioni crittografate su tutti i siti.

### Impostazioni di privacy consigliate

**1. Seleziona il livello di protezione anti-tracciamento**:
Impostazioni > Privacy e sicurezza > Protezione avanzata dal tracciamento

![Protection anti-pistage](assets/fr/18.webp)

**Standard (default consigliato)**:
- Equilibrio tra protezione e prestazioni, le pagine si caricano normalmente
- Blocca: social tracker, cookie cross-site, tracciamento dei contenuti in finestre private, cryptomining, fingerprinting
- Include **Total Cookie Protection**: isola i cookie per ogni sito per evitare il tracciamento trasversale.

**Strict (massima protezione)**:
- Maggiore protezione, ma potrebbe interrompere alcuni siti o contenuti
- Blocca: social tracker, cookie cross-site, contenuti di tracciamento in **tutte** le finestre, browser noti e sospetti
- Consigliato agli utenti esperti

**Personalizzato (controllo granulare)**:
- Scegliere con precisione i tracker e gli script da bloccare
- Opzioni separate: Cookie, Contenuto di tracciamento, Cryptomining, Tracker noti/sospetti
- Ideale per la messa a punto in base alle proprie esigenze

**2. Cambia motore di ricerca**
Impostazioni > Ricerca > Motore di ricerca predefinito:

![Configuration moteur de recherche](assets/fr/20.webp)

- **DuckDuckGo**: nessuna profilazione, nessun filtro a bolle, risultati neutrali
- **Startpage**: risultati anonimizzati di Google, con sede nei Paesi Bassi (RGPD)
- **Searx**: Motore di metaricerca decentralizzato, senza log, open source
- **Brave Search**: indicizzatore indipendente, non di Google
- **Evita**: Google, Bing, Yahoo (raccolta massiccia di dati)

**3. Configura il DNS sicuro (DNS su HTTPS)**:

Impostazioni > Privacy e sicurezza > DNS su HTTPS (in fondo alla pagina)

![Configuration DNS sur HTTPS](assets/fr/19.webp)

**Protezione di default**:
- Zen decide automaticamente quando utilizzare il DNS sicuro
- Utilizzare il DNS sicuro nelle regioni in cui è disponibile
- Fallback al DNS predefinito in caso di problemi con il provider sicuro
- Disattivazione automatica con VPN, controlli parentali o politiche aziendali.

**Protezione aumentata (consigliata)**:
- Potete controllare quando utilizzare il DNS sicuro e scegliere il provider
- Utilizza il provider selezionato con fallback al sistema DNS, se necessario
- **Provider predefinito**: Cloudflare (veloce, log anonimizzati)
- **Alternative**: Passare a Quad9, NextDNS secondo disponibilità

**Protezione massima (utenti avanzati)**:
- Zen utilizza **sempre** solo DNS sicuri
- Avvertenza di sicurezza prima di utilizzare il sistema DNS
- **Attenzione**: i siti potrebbero non essere caricati se il DNS sicuro non è disponibile

**4. Abilita solo la modalità HTTPS**:
Impostazioni > Privacy e sicurezza > Solo modalità HTTPS > **Abilitato**

- Forza tutte le connessioni a HTTPS
- Avvisa se un sito supporta solo HTTP

**5. Gestire le autorizzazioni predefinite:**

Impostazioni > Privacy e sicurezza > Autorizzazioni:
- **Posizione**: blocco (eccetto servizi di carte)
- **Telecamera/microfono**: blocco (autorizzare caso per caso)
- **Notifiche**: blocca (impedisce lo spam)
- **Riproduzione automatica**: blocca audio e video

### Estensioni di sicurezza consigliate

**Estensioni essenziali**

- **uBlock Origin**: il più efficace blocco degli annunci e tracker
  - Elenchi consigliati: EasyList, EasyPrivacy, l'elenco dei server di pubblicità e tracciamento di Peter Lowe
  - Modalità avanzata per utenti esperti
- **Cancella URL**: cancella i parametri di tracciamento degli URL (utm_source, fbclid, ecc.)
- **Cookie AutoDelete**: cancella automaticamente i cookie e i dati di navigazione alla chiusura della scheda
- **Decentraleyes**: serve le librerie JS localmente per evitare i CDN di Google/Cloudflare.

**Estensioni avanzate (utenti esperti)**:
- **NoScript**: controllo granulare di JavaScript (può interrompere molti siti)
- **Privacy Badger** (EFF): rilevamento comportamentale dei tracker
- **Contenitori temporanei**: isolare ogni scheda in un contenitore separato.


## Capire l'assenza di DRM in Zen Browser

### Che cos'è il DRM?

I **DRM (Digital Rights Management)** sono tecnologie di protezione che criptano il contenuto digitale per impedirne la copia. Richiedono un modulo proprietario del browser (come **Google Widevine**) per decifrare e leggere i supporti protetti.

**Servizi che richiedono DRM**:
- **Streaming video**: Netflix, Disney+, HBO Max, Amazon Prime Video
- **Musica premium**: Spotify Premium, YouTube Music, Deezer
- **Formazione online**: Udemy, Coursera (video protetti)

### Perché Zen Browser non ha il DRM

**Principali motivi**:
1. **Costi e complessità**: le licenze di Google Widevine non sono gratuite e richiedono un processo di approvazione complesso
2. **Filosofia del progetto**: il DRM è una "scatola nera" proprietaria, incompatibile con l'approccio open source e l'indipendenza da Google
3. **Risorse limitate**: il team si concentra sull'innovazione e sulla riservatezza dell'interfaccia.

### Impatto pratico

**❌ Servizi inaccessibili:**

Netflix, Disney+, Spotify Premium, YouTube Premium, Corsi di formazione a pagamento Udemy/Coursera

![Erreur DRM Prime Video](assets/fr/17.webp)

_Tipico messaggio di errore quando si tenta di riprodurre contenuti protetti da DRM_

**✅ Servizi funzionali:**

YouTube, Twitch, Vimeo, siti di notizie, social network, podcast gratuiti

**Soluzioni di bypass**:
- Utilizzare Firefox/Chrome solo per lo streaming
- Applicazioni native (Netflix, Spotify)
- Scegliere contenuti privi di DRM (YouTube, Twitch, Bandcamp, PeerTube)

**Stato attuale**: il team Zen ha iniziato il processo di ottenimento di una licenza Widevine, ma non è stato fornito alcun calendario. Il processo dipende interamente dall'approvazione di Google.


## Uso quotidiano

### Interfaccia e navigazione

**Barra laterale a schede**:
- Titolo e miniatura per ogni pagina
- pulsante "+" per le nuove schede
- Riorganizzazione con il drag-and-drop
- Azioni sensibili al contesto: clic con il tasto destro del mouse per duplicare, chiudere, spostare

**Aree di lavoro**:
- Selettore nella parte superiore della barra laterale
- Creazione di aree tematiche
- Passaggio rapido da un contesto all'altro
- Schede appuntate disponibili in tutti gli spazi

![Création d'un nouvel espace](assets/fr/11.webp)

_Interfaccia per creare una nuova area di lavoro_

**Caratteristiche avanzate**

- **Split View**: seleziona più schede > fai clic con il pulsante destro del mouse > "Dividi schede"
- **Glance**: Alt + click su un link per l'anteprima

### Scorciatoie utili

- `ctrl+T`: nuova scheda
- `ctrl+spazio`: menu spazio di lavoro
- `ctrl+B`: mostra/nasconde la barra laterale
- `ctrl+Shift+P`: finestra privata
- `alt+click`: Glance (anteprima)

### Le migliori pratiche

- **Organizzare gli spazi**: crea spazi tematici (Lavoro, Da visionare, Personale)
- Utilizza le schede con i **pin**: per i siti più visitati
- **Sfruttare la visualizzazione divisa**: ideale per il multitasking su schermi grandi
- **Mantenersi aggiornati**: controlla regolarmente gli aggiornamenti
- **Esplora Zen Mods**: personalizza l'aspetto in base ai tuoi gusti.


## Conclusione

Zen Browser rappresenta una ventata di aria fresca nell'ecosistema dei browser web. Combinando un'interfaccia innovativa e produttiva con un rigoroso rispetto della privacy, offre un'alternativa credibile ai browser dei giganti della tecnologia.

Le sue schede verticali e gli spazi di lavoro trasformano davvero l'esperienza di navigazione per chi si destreggia tra più progetti. La sua filosofia "no Google" e lo sviluppo della community ne fanno una scelta coerente per gli utenti preoccupati della loro sovranità digitale.

Sebbene abbia ancora alcune limitazioni (assenza di dispositivi mobili, mancanza di DRM), Zen Browser è abbastanza maturo per l'uso quotidiano e sta migliorando rapidamente grazie alla sua attiva comunità.

Per i bitcoiners e gli utenti tecnologici che apprezzano sia la produttività che la privacy, Zen Browser è sicuramente da provare. Potresti adottare questo nuovo modo di navigare, più sereno ed efficiente.


## Risorse

### Link ufficiali

- [Sito ufficiale di Zen Browser](https://zen-browser.app)
- [Documentazione completa](https://docs.zen-browser.app)
- [Codice sorgente GitHub](https://github.com/zen-browser/desktop)
- [Pagina di download](https://zen-browser.app/download)

### Community e supporto

- [Discordia ufficiale](https://discord.gg/zen-browser)
- [Reddit r/zen_browser](https://reddit.com/r/zen_browser)
- [Galleria Mods Zen](https://zen-browser.app/mods)

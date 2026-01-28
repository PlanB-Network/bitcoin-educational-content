---
name: Firefox
description: Come configurare Firefox per proteggere la privacy?
---

![cover](assets/cover.webp)


## Introduzione

Tutti noi trascorriamo ore online, spesso senza renderci conto di ciò che il nostro browser sta rivelando di noi. Ogni clic, ogni ricerca, ogni sito che visitiamo alimenta un'enorme industria di raccolta di dati personali.

![Statistiche navigatori 2024](assets/fr/01.webp)

*Quota di mercato dei browser web: Chrome domina con il 65% del mercato, seguito da Safari ed Edge. Fonte: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*

Come mostra questo grafico, Google Chrome domina in modo massiccio, con oltre il 65% dell'utilizzo mondiale. Questa egemonia significa che la maggior parte degli utenti di Internet affida i propri dati di navigazione a Google, un'azienda il cui modello di business si basa sulla pubblicità mirata. Firefox, con appena il 3% del mercato, rappresenta un'alternativa sviluppata da Mozilla, un'organizzazione no-profit che non ha alcun interesse commerciale a sfruttare i tuoi dati.

Ma scegliere Firefox è solo il primo passo. Per impostazione predefinita, anche Firefox richiede delle regolazioni per massimizzare la protezione. Questa guida ti accompagna passo dopo passo, dai più semplici ai più avanzati, per trasformare Firefox in un vero e proprio scudo contro il tracciamento, preservando al contempo una piacevole esperienza di navigazione.

### Perché Firefox?

- **Libero e open-source** (motore Gecko): codice verificabile e trasparente.
- **Organizzazione non profit**: Fondazione Mozilla, missione di interesse generale.
- **Protezioni native integrate**: protezione avanzata dal tracciamento (ETP), protezione totale dai cookie (TCP), partizionamento dello stato, modalità solo HTTPS, DNS su HTTPS (DoH).
- **Personalizzazione avanzata**: a differenza di Chrome, Firefox consente di modificare il suo comportamento in profondità.

### Principi importanti prima di iniziare

- **Non esiste una ricetta universale**: più modifichi, più rischi di distinguerti (fingerprinting). L'obiettivo è quello di essere più protetti senza distinguersi dalla massa.
- **Progressi passo dopo passo**: modifica un'impostazione, testa i tuoi siti abituali, quindi continua. Non è necessario modificare tutto in una volta.
- **Equilibrio personale**: trova il TUO compromesso tra privacy e facilità d'uso.


## Installazione rapida

![Download Firefox](assets/fr/02.webp)

**Download ufficiale**: vai su [firefox.com/browsers/desktop](https://www.firefox.com/it/browsers/desktop/). In questa pagina, seleziona il tuo sistema operativo (Windows, macOS, Linux) per accedere alla pagina di download appropriata con istruzioni specifiche per l'installazione.

- **Windows**: scarica il programma di installazione `.exe`, fai doppio clic e segui la procedura guidata di installazione.
- **macOS**: scarica il file `.dmg`, aprilo e trascina Firefox nella cartella Applicazioni.
- **Linux**: sono disponibili diverse opzioni - pacchetto `.deb`/`.rpm`, Flatpak (Flathub), Snap, o tramite il gestore di pacchetti (apt, dnf, pacman). Preferisci i sorgenti ufficiali di Mozilla.

**Suggerimento**: Una volta installato, verifica la presenza di aggiornamenti tramite Aiuto → **Informazioni su Firefox** (importanti per le patch di sicurezza).

![Configurazione iniziale Firefox](assets/fr/03.webp)

*Prima schermata all'avvio di Firefox: imposta Firefox come browser predefinito, aggiungilo ai collegamenti, quindi fai clic su "Salva e continua "*

![Crea un account Firefox](assets/fr/04.webp)

*Passo facoltativo: crea o accedi a un account Firefox. È possibile saltare questo passaggio facendo clic su "Non ora" in basso a destra*

![Schermata iniziale Firefox](assets/fr/05.webp)

*Schermata iniziale di Firefox al termine della configurazione. Nota il menu* ☰ *in alto a destra, che dà accesso a Impostazioni ed Estensioni per personalizzare Firefox*


## Protezioni già attivate di default (consigliate)

- **Isolamento dei siti (Fission)**: in distribuzione progressiva. Questa funzione esegue ogni sito in un processo separato per evitare che una scheda dannosa acceda ai dati di un'altra. Controllate il suo stato tramite `about:support` (cercate "Fission"). Se non è abilitata, è possibile attivarla manualmente in `about:config` con `fission.autostart = true`.
- **Protezione totale dei cookie (TCP)**: attiva per impostazione predefinita. I cookie e le altre forme di memorizzazione sono limitati al sito della prima parte (un "barattolo" per sito), il che neutralizza il tracciamento trasversale. Se necessario, vengono effettuate eccezioni temporanee tramite l'API di accesso allo storage (pulsanti di accesso integrati).
- **Protezione dal tracciamento dei "rimbalzi" e dei reindirizzamenti**: Firefox rileva e ripulisce automaticamente i cookie lasciati dai siti di "rimbalzo" (link che reindirizzano l'utente tramite un tracker prima della destinazione), riducendo questo canale di tracciamento senza alcuna azione da parte dell'utente.


## Livello 1 - Essenziale (≤ 10 minuti)

Obiettivo: grandi guadagni in termini di privacy senza interrompere il web. Per il 90% degli utenti.

Per accedere alle impostazioni, fai clic sul menu ☰ in alto a destra, quindi su **"Impostazioni "**:

![Parametri generali](assets/fr/07.webp)

*Pagina delle impostazioni di Firefox - scheda "Generale". Qui è possibile configurare la maggior parte delle opzioni relative alla privacy*

**Protezione di tracciamento (ETP)**

- Passare da **ETP** a **Strict**. Si bloccano più tracker (cookie cross-site, fingerprinting, cryptomining, widget sociali...).
- Se un sito si corrompe (video, pulsante di accesso...), disattiva la protezione solo per quel sito tramite lo scudo 🛡️, quindi aggiorna la scheda.

Ecco i diversi livelli di sicurezza dell'ETP:

- **Standard** (bilanciato, massima compatibilità).
  - Blocca: social tracker, cookie cross-site (tutte le finestre), tracciamento dei contenuti nella navigazione privata, minatori di criptovalute, rilevatori di impronte digitali.
  - Include **Total Cookie Protection** (TCP): un "barattolo" per sito.
- **Strict** (consigliato per la riservatezza)
  - Blocca anche i contenuti di tracciamento in tutte le finestre + impronte digitali note e sospette.
  - Può interrompere alcuni siti; utilizzare lo scudo 🛡️ per un'eccezione locale.
- **Custom** (avanzato)
  - Regolazione fine: cookie, tracciamento dei contenuti, minori, impronte digitali (note/sospette).

![Parametri di protezione contro il monitoraggio](assets/fr/06.webp)

**Cookies e dati del sito**

- Attiva "**Cancella i cookie e i dati del sito alla chiusura**" per riavviare in modo pulito a ogni riavvio.
- Aggiungi **Eccezioni** per 2-3 siti essenziali, se lo desideri (e-mail, banca).

**Inserimento automatico dei dati, suggerimenti e home page**

- Disattiva la **compilazione automatica** (ID, indirizzi, carte). Utilizza invece un gestore di password.
- **Ricerca**: disattiva **"Mostra suggerimenti di ricerca"**.
- **Barra degli indirizzi**: taglia "**Suggerimenti sponsorizzati**" e "**Suggerimenti contestuali**".
- **Home**: disattiva **Pocket** e **contenuti sponsorizzati**.

![Parametri per i cookie e password](assets/fr/08.webp)

**Solo HTTPS**

- Attiva la "**HTTPS modalità esclusiva in tutte le finestre**".

![Configurazione DNS over HTTPS](assets/fr/09.webp)

**Misurazione della telemetria e della pubblicità**

- In "Raccolta dati da parte di Firefox", **deselezionare tutto**.
- Disattiva le "**Misure pubblicitarie a tutela della privacy**" (PPA).
- **Navigazione sicura**: mantieni l'opzione attivata (consigliata). Firefox controlla i siti in base agli elenchi di minacce tramite query con hashtag e controlli locali, proteggendo da phishing e malware con un impatto minimo sulla privacy.

**Controllo globale della privacy (opzionale)**

- Attiva il **GPC** per segnalare il proprio rifiuto di vendere/condividere i dati.

**Motore di ricerca**

- Passa a **DuckDuckGo**, **Startpage**, **Qwant** o **Brave Search** (Impostazioni → Ricerca).

![Configurazione del motore di ricerca DuckDuckGo](assets/fr/11.webp)

**Navigazione privata**

- Finestre private (Ctrl/Cmd+Shift+P) per sessioni una tantum (regali, account secondari...). Evita la modalità "sempre privata": le estensioni potrebbero essere inattive e le eccezioni dei cookie meno utili.

**Estensioni essenziali** (installa dal catalogo ufficiale)

- **uBlock Origin**: blocca gli annunci e il tracciamento continuo, leggero.
- **Privacy Badger**: impara a bloccare ciò che ti controlla; invia Do Not Track / GPC.
- **ClearURLs** (opzionale): Firefox (ETP Strict) e uBO fanno già molta pulizia; tienilo se vedi ancora URL "sporchi" (utm, fbclid).
- **Contenitori multi-account di Firefox**: isola i cookie/sessioni e l'archiviazione per contenitore; account multipli paralleli; meno tracciamento cross-site. Estensione ufficiale: `https://addons.mozilla.org/it/firefox/addon/multi-account-containers/`.

![Estensioni Multi-Account Containers](assets/fr/12.webp)

**Password e 2FA**

- Utilizza un **gestore di password** dedicato (Bitwarden, KeePassXC). **Evita** di memorizzare le password nel browser. **Abilita la 2FA** quando possibile.


## Livello 2 - Rinforzato (compartimentazione e rete)

Obiettivo: compartimentare le attività e ridurre le perdite di rete.

**DNS su HTTPS (DoH)**

- **Stato predefinito**: attivato automaticamente in alcune regioni (USA, Canada, Russia, Ucraina). Nelle altre regioni è necessaria l'attivazione manuale.
- **Configurazione**: Impostazioni → Generale → Impostazioni di rete → **Abilita DoH** → **Cloudflare** o **Quad9** → **Protezione massima**.
- Massima protezione = **solo TRR** (nessun fallback al DNS di sistema). Se una rete aziendale/alberghiera si blocca, torna a **Standard** o disabilita DoH.
- **Ridondanza**: se utilizzi già una VPN affidabile con un proprio DNS sicuro, DoH può essere ridondante.
- **Test di verifica**: `https://www.dnsleaktest.com/` deve visualizzare solo il fornitore DoH scelto.

![Selezione del fonitore DNS Cloudflare](assets/fr/10.webp)

**Compartimentazione con contenitori e profili**

- **Contenitori multi-account**: crea spazi (Personale, Lavoro, Finanza, Reti sociali, Shopping, Usa e getta). Configura "**Apri sempre in questo contenitore**" per i siti ricorrenti. Estensione ufficiale: `https://addons.mozilla.org/it/firefox/addon/multi-account-containers/`.
- Perché usarli?
- **Forte isolamento** di cookie/sessioni/storage di spazio.
- **Meno tracciamento cross-site**: limitare i 'giganti' (Facebook, Google).
- Più **account** simultanei sullo stesso servizio.
- Minore rischio di **CSRF/XSS** tra identità segmentate.
  - Suggerimento: almeno crea i contenitori dedicati per Social Network/Google, Lavoro, Finanza.
- **Facebook Container** (opzionale): una versione semplificata dedicata a FB/Instagram.
- **Profili separati**: tramite `about:profiles` (profilo principale, profilo minimo "ultra-sicuro", profilo di prova). Totale compartimentazione dei dati e delle estensioni.

**Estensioni avanzate** (essere riservato)

- **Cookie AutoDelete**: cancella i cookie di un sito non appena la scheda viene chiusa (utile se Firefox rimane aperto a lungo).
- **LocalCDN**: serve per le librerie correnti a livello locale (riduce le chiamate a Google/Microsoft). Compatibilità parziale.

**Mobile (Android)**

- **Firefox Android + uBlock Origin**: protezione simile anche in mobilità.

## Livello 3 - Esperto (about:config & Arkenfox)

Obiettivo: protezione avanzata con compromessi accettati. Consigliato su un **profilo separato**.

Scegliete solo uno dei due approcci seguenti:

**Approccio A - Modifiche manuali**: Alcuni aggiustamenti mirati tramite `about:config` (controllo più semplice e preciso)

**Approccio B - Arkenfox user.js**: Configurazione completamente automatizzata (più complessa, massima protezione)

➡️ **Arkenfox include già TUTTE le modifiche a about:config menzionate qui sotto** + altre centinaia. Se si sceglie Arkenfox, ignorare la sezione about:config.

### Approccio A: modifiche manuali tramite about:config

Digita `about:config` nella barra Address → Accetta il rischio.

![Avertimenti about:config](assets/fr/13.webp)

![Interfaccia about:config](assets/fr/14.webp)

![Preferenze about:config](assets/fr/15.webp)

- Resistenza al fingerprinting (ereditata da Tor Browser)

```text
privacy.resistFingerprinting = true
```

Effetti: Fuso orario UTC, **letterboxing** (dimensioni standard delle finestre), User-Agent/politiche standardizzate, restrizioni Canvas/WebGL/AudioContext. Maggiore uniformità, ma alcune "stranezze" (orario sfalsato, a volte un po' di inglese).

- Disattiva WebRTC (evita le fughe di dati IP, ma interrompe la visone Web)

```text
media.peerconnection.enabled = false
```

- Referente più compatibile (predefinito)

```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```

Opzione rigorosa (può interrompere i pagamenti/SSO):

```text
network.http.referer.XOriginPolicy = 2
```

- Limita le API e la speculazione

```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```

Regola d'oro: se qualcosa si rompe, tornare all'ultima modifica.

### Approccio B: Arkenfox user.js (configurazione completamente automatizzata)

Il progetto **Arkenfox** fornisce un file `user.js`, gestito dalla comunità, che applica automaticamente centinaia di preferenze di Firefox orientate alla privacy e alla sicurezza. Al riavvio, Firefox legge questo file dal profilo dell'utente e applica queste impostazioni.

- Qual è lo scopo? Partire da una **base consolidata coerente** senza "cliccare ovunque"; ridurre le sviste; risparmiare tempo.
- Cosa cambia (esempi): taglio della telemetria, cookie/cache/referrer/HTTPS rafforzati, **RFP** + letterboxing, **WebRTC disabilitato**, aggiustamenti DoH/TLS, API chat limitate.
- Quando usarlo: se vuoi che Firefox sia temprato in 10 minuti e accetti alcune eccezioni (DRM/streaming, Web Visio, SSO/pagamenti).
- Vantaggi: veloce, coerente, **aggiornato** (allineato alle ESR), molto ben **documentato** (wiki + commenti), **personalizzabile** tramite sovrascritture.
- Limitazioni: compatibilità (alcune applicazioni web), comodità (UTC, dimensioni della finestra) e un promemoria: **Non è Tor** (non c'è anonimato in rete).

Installazione (idealmente su un **profilo dedicato**)

1. Salva profilo/favoriti ed elenca i siti con eccezioni per i cookie.
2. Scarica `user.js` da `https://github.com/arkenfox/user.js` (versione ESR/stabile).
3. Trova la cartella del profilo tramite `circa:profili`:
   - Windows: `%APPDATA%/Mozilla/Firefox/Profili/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Libreria/Application Support/Firefox/Profili/...`
4. Chiudere Firefox e spostare `user.js` nella radice della cartella del profilo.
5. Rilanciare; personalizzare tramite `about:config` o un file di override.

Aggiornamenti

- Segui le release di Arkenfox (allineate alle ESR), sostituire il file `user.js`, rilanciare Firefox; leggere le note di rilascio.

**Personalizzazione attraverso le sovrascritture**

Arkenfox è deliberatamente restrittivo per impostazione predefinita. Per adattare alcune impostazioni alle proprie esigenze (streaming, video, siti specifici), è possibile creare un file `user-overrides.js` nella stessa cartella di `user.js`. Questo file permette di "sovrascrivere" alcune preferenze di Arkenfox senza modificare il file principale.

Creare `user-overrides.js` e aggiungere le proprie personalizzazioni:

```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```

Le migliori pratiche:

- Utilizza un profilo separato "**Arkenfox**" e mantieni un profilo "normale" per comodità.
- Riduci al minimo le estensioni (uBlock Origin OK) per limitare la superficie di attacco e l'unicità.
- Aggiungi eccezioni sito per sito (schermare 🛡️, uBO, NoScript se utilizzato) quando necessario.
- Testa dopo ogni modifica: perdite WebRTC/DNS, copertura delle tracce, CreepJS.


## Le migliori pratiche

- **Aggiornamenti**: Firefox e le estensioni da aggiornare spesso.
- **Estensioni**: ragionevoli e affidabili; attenzione ai rimborsi "controversi".
- **Download**: attenzione; verifica i file sensibili su VirusTotal.
- **Password**: **gestore dedicato** (Bitwarden, KeePassXC); **2FA** abilitato; evita la memorizzazione nel browser.
- **Pulizia**: confina Google/Facebook nei contenitori; chiudi/apri regolarmente per "resettare" il contesto.


## Limiti e alternative

- Un browser protetto ≠ Anonimato di rete: senza **VPN**, il tuo IP rimane visibile; anche con esso, la correlazione rimane possibile.
- Modificare troppo può renderti **unico**. **RFP** standardizza; gli strumenti di randomizzazione (ad esempio Chameleon) possono... differenziarti. Testa, confronta, aggiusta.
- Alternative/complementi:
  - Tor Browser: anonimato in rete tramite Tor; più lento. Consulta la nostra guida completa all'installazione e alla configurazione:
    
https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

  - Browser Mullvad: "Tor senza Tor", da abbinare alla VPN; footprint standardizzato. Scopri come installarlo nel nostro tutorial dedicato:
    
https://planb.academy/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e

- Combinazioni consigliate: Firefox (livello 2) + VPN per l'uso quotidiano; Tor/Mullvad per le attività sensibili; profili separati per la compartimentazione.


## Conclusione

Seguendo questa guida passo passo, hai trasformato Firefox in un vero e proprio baluardo contro la sorveglianza digitale. Dalle impostazioni essenziali di livello 1 alle configurazioni avanzate di Arkenfox, ogni modifica rafforza la tua privacy senza compromettere la tua esperienza di navigazione.

**La tua privacy è ora più protetta**: blocco dei tracker pubblicitari, compartimentazione dei cookie, neutralizzazione delle fughe di dati degli indirizzi IP, disabilitazione della telemetria. Firefox non è più solo un browser, ma uno strumento di resistenza digitale su misura per le tue esigenze.

**Ricordati: la riservatezza non è mai scontata. Verifica regolarmente la tua protezione, aggiorna le impostazioni e non esitare a modificare la configurazione in base al cambiamento delle tue abitudini. L'anonimato online dipende tanto dai tuoi strumenti quanto dalle tue pratiche.**


## Risorse



### Plan ₿ Academy

- SCU 202 - Migliorare la sicurezza digitale personale: Per saperne di più sui concetti di sicurezza digitale trattati in questo tutorial



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Documentazione di Mozilla

- [Protezione avanzata dal tracciamento](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): guida ufficiale alla protezione avanzata dal tracciamento.
- [State Partitioning](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): documentazione tecnica sul partizionamento degli stati.
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security): riferimento completo sulla sicurezza web.

### Arkenfox

- [Wiki e guida all'installazione](https://github.com/arkenfox/user.js/wiki): documentazione completa del progetto Arkenfox.
- [Deposito e rilasci](https://github.com/arkenfox/user.js): scarica il file user.js e tieni traccia degli aggiornamenti.

### Guide e comunità

- [PrivacyGuides - Browser per desktop](https://www.privacyguides.org/it/desktop-browsers/): raccomandazioni e confronti tra browser.
- **Reddit**: r/firefox, r/privacy per feedback e supporto.
- **Forum PrivacyGuides**: discussioni tecniche approfondite.

### Strumenti di test

- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): impronte digitali ed efficacia anti-tracciamento.
- [DNS Leak Test](https://www.dnsleaktest.com/): test sulle fughe di DNS ed efficienza del DoH.
- [BrowserLeaks](https://browserleaks.com/): suite di test completa (WebRTC, Canvas, caratteri, ecc.).
- [BadSSL](https://badssl.com/): test di validazione dei certificati SSL/TLS.
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): analisi avanzata di oltre 50 vettori di impronte digitali.
- [Cloudflare DNS Test](https://1.1.1.1/help): verifica che Cloudflare DoH funzioni correttamente.

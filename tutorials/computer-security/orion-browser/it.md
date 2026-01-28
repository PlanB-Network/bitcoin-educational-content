---
name: Orion Browser
description: Come utilizzare Orion Browser per proteggere la privacy su Mac e iPhone?
---

![cover](assets/cover.webp)


## Introduzione

In un contesto in cui la maggior parte dei browser raccoglie massicciamente i nostri dati personali, la scelta di un browser rispettoso della privacy diventa fondamentale. Chrome domina con il 65% del mercato globale, ma il suo modello di business si basa sullo sfruttamento dei dati di navigazione. Safari, pur essendo integrato nell'ecosistema Apple, manca di funzioni di protezione avanzate e non supporta in modo flessibile le estensioni di terze parti.

![Répartition du marché des navigateurs](assets/fr/01.webp)

_Ripartizione del mercato dei browser web: Chrome domina con oltre il 65% di quota di mercato, seguito da Safari, Edge e Firefox_

**Orion Browser** si presenta come un'alternativa innovativa per gli utenti Apple. Sviluppato da Kagi, questo browser combina la velocità del motore WebKit con la filosofia della telemetria zero. A differenza dei suoi concorrenti, Orion non invia dati a server remoti e blocca in modo nativo il 99,9% degli annunci e dei tracker, compreso YouTube.

La sua caratteristica unica? Orion è l'**unico browser WebKit** a installare nativamente le estensioni di Chrome **e** Firefox, offrendo il meglio di entrambi i mondi. Questa compatibilità, unita al consumo di memoria da 2 a 3 volte inferiore rispetto agli altri browser e alla perfetta integrazione con l'ecosistema Apple (iCloud, Keychain), lo rende la scelta ideale per gli utenti Mac e iPhone attenti alla privacy.


## Perché scegliere Orion Browser?

### Vantaggi principali

**Massima protezione fin dall'inizio**: Orion blocca per impostazione predefinita il 99,9% degli annunci pubblicitari (compreso YouTube) e tutti i tracker proprietari e di terze parti. La sua tecnologia combina l'Intelligent Tracking Prevention di WebKit con gli elenchi di EasyPrivacy per la massima efficienza. Caratteristica unica: Orion blocca gli script di fingerprinting **prima che vengano eseguiti**, rendendo letteralmente impossibile il tracciamento: un approccio più radicale rispetto ad altri browser che tentano solo di "mascherare" i dati.

**Zero telemetria verificabile**: Orion adotta un approccio radicale alla privacy, con una telemetria pari a zero. A differenza di altri browser, che all'avvio effettuano centinaia di richieste di rete  (IP esposto, impronta digitale del browser, informazioni personali), Orion non _"telefona a casa"_. Questa differenza fondamentale elimina completamente il rischio di perdita involontaria di dati.

**Prestazioni eccezionali**: basato su una versione ottimizzata di WebKit, Orion eguaglia o addirittura supera Safari in velocità su Mac. I test dello Speedometer 2.0/2.1 lo collocano costantemente al primo posto sui processori Apple Silicon. Il blocco nativo degli annunci accelera ulteriormente il caricamento delle pagine del 20-40%.

**Supporto universale per le estensioni**: un'importante innovazione, Orion consente di installare estensioni dal Chrome Web Store **e** da Mozilla Add-ons. Il supporto delle estensioni Web è attualmente sperimentale, con l'obiettivo di una compatibilità al 100% al momento del rilascio della beta. È possibile utilizzare molte estensioni popolari come uBlock Origin, Bitwarden, anche su iPhone - una novità assoluta su iOS, anche se alcune di queste potrebbero non funzionare perfettamente.

### Limitazioni da tenere presenti

- **Disponibilità limitata**: attualmente riservato a macOS e iOS/iPadOS. Una versione per Linux sta raggiungendo le tappe di sviluppo (Milestone 2 nel 2025), ma non è disponibile una build pubblica. Windows e Android non sono in fase di sviluppo per mancanza di risorse.
- **Codice sorgente chiuso**: sebbene alcuni componenti siano open-source, Orion rimane prevalentemente proprietario, questo rimane un punto di discussione nella community della privacy.
- **Estensioni sperimentali**: il supporto delle estensioni è ancora in fase beta, con frequenti incompatibilità. Le estensioni possono influire sulle prestazioni e alcune non funzionano affatto.
- **Sicurezza di WebKit**: a differenza di Chromium, WebKit non offre un isolamento così robusto dei processi per sito, il che può comportare rischi per la sicurezza in alcuni scenari.
- **Test di blocco**: Orion si comporta deliberatamente male nei test pubblicitari online (26-35%), poiché Kagi ritiene che questi test siano "fondamentalmente errati". L'efficacia reale nell'uso quotidiano è di gran lunga superiore.


## Installazione di Orion Browser

### Su macOS

![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)

_La homepage di Kagi presenta Orion Browser come "un browser privo di pubblicità con protezione totale della privacy e supporto universale per le estensioni"_

- Vai a [kagi.com/orion](https://kagi.com/orion/)
- Fai clic su "**Scaricare Orion per macOS**"

![Page de téléchargement d'Orion Browser](assets/fr/03.webp)

_La pagina di download di Orion Browser mostra la disponibilità per macOS e iOS, con link all'App Store_

- Apri il file `.dmg` scaricato
- Trascina l'applicazione Orion nella cartella Applicazioni
- Al primo avvio, macOS ti chiederà di confermare l'apertura

**Alternativa Homebrew**:

```bash
brew install --cask orion
```

### Su iPhone/iPad

- Apri l'**App Store**
- Cerca "**Orion Browser by Kagi**"
- Installa l'applicazione gratuita (compatibile con iOS 15+)

### Configurazione iniziale

Al primo avvio, Orion guida l'utente attraverso diverse fasi:

**1. Schermata di benvenuto**

![Écran de bienvenue d'Orion](assets/fr/04.webp)

_La schermata di benvenuto di Orion Browser evidenzia le caratteristiche principali: navigazione più veloce, zero telemetria, blocco degli annunci e supporto delle estensioni_

**2. Personalizzazione dell'interfaccia**

![Options de personnalisation](assets/fr/05.webp)

_La schermata di personalizzazione consente di configurare l'aspetto delle schede e dell'interfaccia in base alle proprie preferenze_

- **Importazione dei dati**: trasferimento facile di preferiti e password da Safari, Chrome o Firefox
- **Sincronizzazione iCloud**: attiva per trovare i tuoi preferiti e le tue schede su tutti i tuoi dispositivi Apple

**3. Installazione su dispositivi mobili**

![Installation sur iOS](assets/fr/06.webp)

_Schermata di installazione su iOS che mostra il codice QR per scaricare rapidamente Orion Browser dall'App Store_

**4. Interfaccia di benvenuto e strumenti essenziali**

![Page d'accueil Orion](assets/fr/07.webp)

_Pagina iniziale dell'interfaccia di Orion Browser: la freccia indica i tre strumenti chiave accessibili direttamente dalla barra degli indirizzi_

Una volta completata la configurazione, si scoprirà la semplificata interfaccia di Orion con i suoi **tre strumenti essenziali** (indicati dalla freccia):
- **Shield 🛡️**: visualizza il rapporto sulla privacy con il numero di elementi bloccati nella pagina corrente
- **Pennello 🖌️**: personalizzazione della visualizzazione delle pagine (tema, font, rimozione di elementi che distraggono)
- **Gear ⚙️**: configura i parametri specifici del sito web (permessi, blocco, ecc.)

Questi strumenti sono sempre disponibili e consentono di controllare l'esperienza di navigazione su base individuale.

**Importante**: Orion è gratuito e non richiede la registrazione o la creazione di un account per funzionare.

![Orion+ dans les préférences](assets/fr/08.webp)

_Schermata di abbonamento a Orion+ nelle preferenze, che offre un abbonamento opzionale per supportare lo sviluppo_

**Orion+ (opzionale)**: per supportare lo sviluppo del progetto, Kagi offre Orion+ ($5/mese, $50/anno o $150 a vita). Questa sottoscrizione volontaria consente di:
- comunicare direttamente con il team di sviluppo
- influenzare l'evoluzione del browser in base alle proprie esigenze
- accesso alle versioni Nightly con le ultime funzionalità sperimentali
- usufruire dell'ultimo motore WebKit
- ottenere un badge distintivo sul forum di feedback

Orion+ garantisce l'indipendenza del progetto: "Il tuo contributo finanziario ci aiuta a rimanere indipendenti e a mantenere la promessa di diventare il miglior browser per i nostri utenti". È questo modello di finanziamento degli utenti che mantiene Orion privo di pubblicità e di telemetria.


## Configurazione per la massima riservatezza

### Parametri essenziali

Accedere alle preferenze tramite **Orion → Preferenze** (o ⌘,):

**1. Ricerca - Motore di ricerca privato**

![Configuration du moteur de recherche](assets/fr/09.webp)

_Configurazione predefinita del motore di ricerca: DuckDuckGo è selezionato per garantire la massima privacy_

- **Motore predefinito**: seleziona **DuckDuckGo**, **Startpage** o **Kagi** per una privacy ottimale (evita Google/Bing)
- **Suggerimenti di ricerca**: disabilitarli per evitare che i tasti premuti vengano trasmessi ai server dei motori di ricerca

**2. Privacy - Protezione generale**

![Content Blocker dans les préférences](assets/fr/12.webp)

_Le impostazioni sulla privacy di Orion mostrano il blocco dei contenuti con 119.156 regole attive, le opzioni di rimozione dei tracker e l'agente utente personalizzato_

**Blocco dei contenuti attivo per impostazione predefinita**:
- **EasyList**: 119k+ regole di blocco degli annunci
- **EasyPrivacy**: protezione contro il tracciamento
- **Gestire gli elenchi di filtri**: ggiunge altri elenchi (consigliato Hagezi)

**Opzioni di privacy**:
- Rimuove i tracker dagli URL: **"solo per la navigazione privata"** pulisce i link copiati
- Condividere i rapporti sugli incidenti: "dopo aver chiesto l'approvazione" rispetta il tuo consenso
- **Agente utente personalizzato**: può essere modificato per aggirare alcuni blocchi

![YouTube avec Privacy Report](assets/fr/10.webp)

_Esempio di YouTube visualizzato con Orion: nessuna pubblicità visibile e Rapporto sulla privacy che mostra i numerosi Elements bloccati_

**3. Impostazioni del sito web - Controllo per sito**

![Website Settings pour YouTube](assets/fr/11.webp)

_Le impostazioni del sito web per YouTube mostrano le opzioni di compatibilità, il blocco dei contenuti e le autorizzazioni specifiche del sito_

**Accesso rapido**: fai clic sull'ingranaggio ⚙️ nella barra degli indirizzi per regolare:
- **Modalità compatibilità**: risolve i problemi di visualizzazione sospendendo le estensioni
- **Blocco dei contenuti**: disattiva il blocco per un sito specifico, se necessario
- **JavaScript/Cookies**: controllo granulare per sito
- **Autorizzazioni**: telecamera, microfono, posizione configurati individualmente

**4. Filtri personalizzati avanzati** (vedi più sotto)

**Crea filtri personalizzati** (Privacy → Gestione elenchi filtri → Filtri personalizzati):

**Sintassi semplificata** (compatibile con Adblock Plus):
- `reddit.com##.promotedlink`: nasconde i post sponsorizzati di Reddit
- `||ads.example.com^`: blocca completamente un dominio pubblicitario
- `@@||sito-utile.com^`: crea un'eccezione per un sito

**Suggerimento: Visita [FilterLists.com](https://filterlists.com) per migliaia di elenchi specializzati pronti all'uso.**

### Estensioni consigliate

Orion supporta nativamente le estensioni per Chrome e Firefox. Installale direttamente dagli store ufficiali:

**Essenziali**:
- **uBlock Origin**: aggiunge un controllo granulare al blocco nativo
- **Bitwarden**: gestore di password open-source
- **Cancella URL**: cancella i parametri di tracciamento degli URL

**Opzionale**:
- **LocalCDN**: serve le librerie condivise localmente
- **Cookie AutoDelete**: cancella automaticamente i cookie dopo la chiusura delle schede
- **NoScript**: controllo totale sull'esecuzione di JavaScript (utenti avanzati)

Per installare un file:
- Visita [chrome.google.com/webstore](https://chrome.google.com/webstore) o [addons.mozilla.org](https://addons.mozilla.org)
- Fai clic su "Aggiungi a Chrome/Firefox"
- Orion intercetterà e installerà automaticamente l'estensione.

**Attenzione**: poiché il supporto delle estensioni è sperimentale, molte di esse potrebbero non funzionare correttamente o influire sulle prestazioni. In caso di problemi (sito non più funzionante, lentezza), disattivare le estensioni una per una per identificare la fonte.

## Uso quotidiano

### Interfacce e caratteristiche uniche

![Outil de personnalisation pinceau](assets/fr/13.webp)

_Menu a pennello di Orion per la personalizzazione della visualizzazione: dimensione dei caratteri, tema (chiaro/scuro), disattivazione delle intestazioni adesive e rimozione di elementi che distraggono_

**Strumento pennello: personalizzazione avanzata**

Lo strumento **brush** di Orion è una caratteristica unica che consente di personalizzare la visualizzazione di ogni sito web:

**Opzioni del tema**:
- Passa da un tema chiaro a uno scuro per ogni sito
- Adattamento automatico alle preferenze del sistema

**Controllo tipografico**:
- **Dimensione del carattere**: regola la leggibilità con i pulsanti A- e A+
- **Stile carattere**: cambia la famiglia di caratteri (predefinita o personalizzata)

**Pulizia interfaccia**:
- **Disabilita le intestazioni bloccate**: rimuove le intestazioni che rimangono bloccate in alto durante lo scorrimento
- **Cancella elementi**: rimuove in modo permanente gli elementi fastidiosi (annunci, pop-up, cookie banner)
  - Clicca su "+ Cancella" e seleziona l'elemento da nascondere
  - Molto utile per i siti con annunci persistenti o tracciamento visivo degli elementi

**Persistenza**: tutte queste impostazioni vengono salvate per dominio e riapplicate automaticamente alla visita successiva.

**Gestione avanzata delle schede**:
- **Schede verticali**: si attivano tramite la barra dei menu (funzione Schede laterali)
- **Schede compatte**: in Preferenze → Schede → Layout "Compatto" per risparmiare spazio
- **Gruppi di schede**: organizza le sessioni per tema
- **Profili multipli**: crea identità separate tramite la barra dei menu (funzione Profili) con dati completamente isolati

**Modalità a basso consumo**: ispirata all'iPhone, questa modalità sospende automaticamente le schede inattive dopo 5 minuti e può ridurre il consumo energetico fino al 90%. Attivala tramite la barra dei menu di Orion su Mac o nelle impostazioni su iOS.

**Strumenti integrati** (menu Modifica e altri):
- **Modifica il testo della pagina**: modifica temporaneamente qualsiasi testo (menu Modifica)
- **Consenti copia e incolla**: supera le restrizioni alla copia (menu Modifica)
- **Copia collegamento pulito**: fai clic con il tasto destro del mouse su un link per rimuovere i parametri di tracciamento
- **Modalità Focus**: navigazione senza distrazioni e a schermo intero
- **Immagine nell'immagine**: guarda i video in una finestra fluttuante
- **Apri in Internet Archive**: accesso diretto alle versioni archiviate
- **Rapporto sulla privacy**: fai clic sullo scudo 🛡️ per visualizzare gli elementi bloccati per pagina.

### Gestione della navigazione privata

La navigazione privata di Orion (⌘⇧N) offre:
- Isolamento completo di cookie e sessioni
- Cancellazione automatica alla chiusura
- Cronologia e disattivazione della cache
- Maggiore protezione contro le impronte digitali

**Suggerimento**: per una compartimentazione avanzata, crea **profili separati** tramite la barra dei menu (funzione Profili). Ogni profilo appare come un'applicazione separata nel Dock, con le proprie impostazioni, estensioni e dati completamente isolati.

### Ottimizzazione delle prestazioni e privacy

Per mantenere Orion veloce e privato:
- **Estensioni**: limitale al minimo indispensabile (può ridurre le prestazioni)
- **Modalità basso consumo**: attiva per le sessioni prolungate (risparmio del 90% possibile)
- **Rapporto sulla privacy**: fai clic sullo scudo 🛡️ per vedere i blocchi in tempo reale
- **Personalizzazione visiva**: utilizzate il pennello 🖌️ per adattare la visualizzazione e rimuovere gli elemnti che distraggono
- **Copia di un link pulito**: fai clic con il tasto destro del mouse per copiare i link senza tracker
- **Profili separati**: utilizza profili dedicati per compartimentare le tue attività
- **Impostazioni del sito web**: fai clic sull'ingranaggio ⚙️ per adattare le autorizzazioni in base al sito
- **Pulizia regolare**: cancella la cache tramite Orion → Cancella i dati di navigazione


## Confronto con le alternative

| Criteri             | Orion            | Safari            | Chrome            | Firefox            | Brave             |
|---------------------|:----------------:|:-----------------:|:-----------------:|:------------------:|:-----------------:|
| **Telemetria**      | Nessuna          | Minimale          | Ampia             | Moderato           | Minimale          |
| **Blocco nativo**   | 99,9% efficacia  | Basico            | Assente           | Parziale           | Completo          |
| **Estensioni**      | Chrome + Firefox | Limitazioni       | Chrome unicamente | Firefox unicamente | Chrome unicamente |
| **Prestazioni Mac** | Eccellente       | Eccellente        | Buone             | Media              | Buona             |
| **Open Source**     | Parziale         | Parziale (WebKit) | Parziale          | Completamente      | Completamente     |
| **Piattaforme**     | Mac/iOS          | Mac/iOS           | Tutte             | Tutte              | Tutte             |

**Rispetto a Safari**: Orion offre una protezione superiore grazie al suo blocco avanzato e al supporto delle estensioni, mantenendo le prestazioni di WebKit.

**Rispetto a Chrome**: privacy impareggiabile senza compromettere la compatibilità, grazie al supporto delle estensioni di Chrome.

**Rispetto a Firefox**: più veloce su Mac, interfaccia più intuitiva, ma meno controllo granulare e non open-source.

**Rispetto a Brave**: Filosofia simile, ma Orion evita le controversie su cripto/BAT e offre una migliore integrazione con Apple.


## Casi d'uso consigliati

**Ideale per**:
- Gli utenti Apple che cercano più privacy di Safari
- Persone che desiderano bloccare tutti gli annunci (compreso YouTube) senza estensioni
- Gli sviluppatori che necessitano di devtools WebKit con protezione della privacy integrata
- Gli utenti iPhone che vogliono estensioni desktop su mobile (innovazione unica)
- Professionisti che hanno bisogno di compartimentare le proprie attività (profili multipli)
- Utenti di telefonia mobile alla ricerca di una migliore gestione della batteria (modalità a basso consumo)

**Evitalo se**:
- Utilizzi principalmente Windows/Linux (nessuna versione disponibile)
- L'open-source completo è essenziale per il tuo modello di minaccia
- Dipendi da estensioni specifiche che potrebbero non funzionare
- È necessaria una sincronizzazione multipiattaforma che vada oltre l'ecosistema Apple
- Preferisci una soluzione stabile e collaudata (in stato di beta permanente dal 2021).


## Punti di attenzione e sicurezza

### Caratteristiche di sicurezza uniche

**Protezione rivoluzionaria anti-fingerprinting**: Orion è l'unico browser che blocca completamente l'esecuzione degli script di fingerprinting prima che questi possano scansionare il sistema. Questo approccio "nessuno script in esecuzione = nessun fingerprinting possibile" supera i tradizionali metodi di mascheramento utilizzati da altri browser.

**Whitelist trasparente**: Orion mantiene un piccolo elenco pubblico di siti (browserbench.org, wizzair.com) in cui il blocco viene automaticamente disabilitato per evitare malfunzionamenti. Questa trasparenza consente agli utenti di capire esattamente quando e perché il blocco viene attenuato.

**Estensioni non verificate**: il supporto per le estensioni di Chrome/Firefox introduce ulteriori rischi, in quanto queste estensioni non sono state progettate per WebKit e non sono specificamente verificate per questo ambiente.

### Manutenzione e aggiornamenti

- **Aggiornamenti automatici**: Orion si aggiorna automaticamente su macOS tramite Sparkle
- **Monitoraggio delle vulnerabilità**: controlla regolarmente le note di rilascio per le patch di sicurezza
- **Segnalazione di bug**: utilizza [orionfeedback.org](https://orionfeedback.org) per segnalare i problemi.


## Conclusione

Orion Browser rappresenta un significativo passo avanti per la privacy su macOS e iOS. Il suo approccio a zero telemetria, combinato con un blocco nativo ultra-efficiente e un supporto unico per le estensioni universali, lo rende una scelta eccellente per gli utenti Apple attenti alla privacy.

**Importante**: Orion rimane in beta permanente dal 2021, con limitazioni di compatibilità delle estensioni e rischi intrinseci di WebKit. Valutare questi compromessi in base al proprio modello di minaccia.

Per l'uso quotidiano su Mac o iPhone, è probabilmente il miglior compromesso tra riservatezza, prestazioni e facilità d'uso disponibile nell'ecosistema Apple, a patto di accettarne i limiti.

Ricordate: la protezione della privacy non dipende solo dal browser. Combinate Orion con le migliori pratiche (password forti, 2FA, VPN se necessario) per una sicurezza online ottimale.


## Risorse e supporto

### Documentazione ufficiale

- **Sito web ufficiale**: [kagi.com/orion](https://kagi.com/orion/)
- **FAQ complete**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- **Forum della comunità**: [community.kagi.com](https://community.kagi.com)
- **Tracciamento di bug**: [orionfeedback.org](https://orionfeedback.org)
- **GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Componenti open-source
- **Blog Kagi**: [blog.kagi.com](https://blog.kagi.com) - Notizie e aggiornamenti

### Test di verifica consigliati

Dopo la configurazione, testa la configurazione:
- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Test delle impronte digitali
- [DNS Leak Test](https://www.dnsleaktest.com/) - Verifica la presenza di perdite DNS
- [BrowserLeaks](https://browserleaks.com/) - Suite completa di test sulla privacy

### Alternative in Plan ₿ Academy

Per la massima protezione, consultate le nostre altre guide:
- [Firefox hardened](https://planb.academy/tutorials/computer-security/communication/firefox-11814cec-3415-4ed9-a06e-f6fda5c9510f) - Configurazione multipiattaforma avanzata
- [Tor Browser](https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb) - Completo anonimato in rete
- [Mullvad Browser](https://planb.academy/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e) - Massima protezione dalle impronte digitali

Se vuoi saperne di più sulla storia e sul funzionamento dei browser, nonché sui principali oggetti digitali della tua vita quotidiana, ti invito a scoprire il nostro nuovo corso di formazione gratuito SCU 202, disponibile su Plan ₿ Academy:

https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

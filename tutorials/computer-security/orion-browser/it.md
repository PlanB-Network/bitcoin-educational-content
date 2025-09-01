---
name: Browser Orion
description: Come utilizzare Orion Browser per proteggere la privacy su Mac e iPhone?
---

![cover](assets/cover.webp)



## Introduzione



In un contesto in cui la maggior parte dei browser raccoglie massicciamente i nostri dati personali, la scelta di un browser rispettoso della privacy diventa fondamentale. Chrome domina con il 65% del mercato globale, ma il suo modello di business si basa sullo sfruttamento dei dati di navigazione. Safari, pur essendo integrato nell'ecosistema Apple, manca di funzioni di protezione avanzate e non supporta in modo flessibile le estensioni di terze parti.



![Répartition du marché des navigateurs](assets/fr/01.webp)


*Ripartizione del mercato dei browser web: Chrome domina con oltre il 65% di quota di mercato, seguito da Safari, Edge e Firefox*



**Orion Browser** si presenta come un'alternativa innovativa per gli utenti Apple. Sviluppato da Kagi, questo browser combina la velocità del motore WebKit con la filosofia della telemetria zero. A differenza dei suoi concorrenti, Orion non invia dati a server remoti e blocca in modo nativo il 99,9% degli annunci e dei tracker, compreso YouTube.



La sua caratteristica unica? Orion è l'**unico browser WebKit** a installare nativamente le estensioni di Chrome **e** Firefox, offrendo il meglio di entrambi i mondi. Questa compatibilità, unita al consumo di memoria da 2 a 3 volte inferiore rispetto agli altri browser e alla perfetta integrazione con l'ecosistema Apple (iCloud, Keychain), lo rende la scelta ideale per gli utenti Mac e iPhone attenti alla privacy.



## Perché scegliere Orion Browser?



### Vantaggi principali



**Massima protezione fin dall'inizio**: Orion blocca per impostazione predefinita il 99,9% degli annunci pubblicitari (compreso YouTube) e tutti i tracker di prima parte e di terze parti. La sua tecnologia combina l'Intelligent Tracking Prevention di WebKit con gli elenchi di EasyPrivacy per la massima efficienza. Caratteristica unica: Orion blocca gli script di fingerprinting **prima che vengano eseguiti**, rendendo letteralmente impossibile il tracciamento: un approccio più radicale rispetto ad altri browser che tentano solo di "mascherare" i dati.



**Zero telemetria verificabile**: Orion adotta un approccio radicale alla privacy, con una telemetria pari a zero. A differenza di altri browser, che all'avvio effettuano centinaia di richieste di rete (esponente IP, impronta digitale del browser, informazioni personali), Orion non "telefona a casa". Questa differenza fondamentale elimina completamente il rischio di perdita involontaria di dati.



**Prestazioni eccezionali**: Basato su una versione ottimizzata di WebKit, Orion eguaglia o addirittura supera Safari in velocità su Mac. I test dello Speedometer 2.0/2.1 lo collocano costantemente al primo posto sui processori Apple Silicon. Il blocco nativo degli annunci accelera ulteriormente il caricamento delle pagine del 20-40%.



**Supporto universale per le estensioni**: Un'importante innovazione: Orion consente di installare estensioni dal Chrome Web Store **e** da Mozilla Add-ons. Il supporto delle estensioni Web è attualmente sperimentale, con l'obiettivo di una compatibilità al 100% al momento del rilascio della beta. È possibile utilizzare molte estensioni popolari come uBlock Origin, Bitwarden, anche su iPhone - una novità assoluta su iOS, anche se alcune potrebbero non funzionare perfettamente.



### Limitazioni da tenere presenti





- Disponibilità limitata**: Attualmente riservato a macOS e iOS/iPadOS. Una versione per Linux sta raggiungendo le tappe di sviluppo (Milestone 2 nel 2025), ma non è disponibile una build pubblica. Windows e Android non sono in fase di sviluppo per mancanza di risorse.
- Codice sorgente chiuso**: Sebbene alcuni componenti siano open-source, Orion rimane prevalentemente proprietario, un punto di discussione nella comunità della privacy.
- Estensioni sperimentali**: Il supporto delle estensioni è ancora in fase beta, con frequenti incompatibilità. Le estensioni possono influire sulle prestazioni e alcune non funzionano affatto.
- Sicurezza di WebKit**: A differenza di Chromium, WebKit non offre un isolamento dei processi per sito così robusto, il che può comportare rischi per la sicurezza in alcuni scenari.
- Test di blocco**: Orion si comporta deliberatamente male nei test pubblicitari online (26-35%), poiché Kagi ritiene che questi test siano "fondamentalmente errati". L'efficacia reale nell'uso quotidiano è di gran lunga superiore.



## Installazione di Orion Browser



### Su macOS



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*La homepage di Kagi presenta Orion Browser come "un browser privo di pubblicità con protezione totale della privacy e supporto universale per le estensioni "*





- Vai a [kagi.com/orion](https://kagi.com/orion/)
- Fare clic su "**Scaricare Orion per macOS**"



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*La pagina di download di Orion Browser mostra la disponibilità per macOS e iOS, con link all'App Store*





- Aprire il file `.dmg` scaricato
- Trascinare l'applicazione Orion nella cartella Applicazioni
- Al primo avvio, macOS vi chiederà di confermare l'apertura di



**Alternativa Homebrew**:


```bash
brew install --cask orion
```



### Su iPhone/iPad





- Aprire l'**App Store**
- Cercare "**Orion Browser by Kagi**"
- Installare l'applicazione gratuita (compatibile con iOS 15+)



### Configurazione iniziale



Al primo avvio, Orion guida l'utente attraverso diverse fasi:



**1. Schermata di benvenuto


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*La schermata di benvenuto di Orion Browser evidenzia le caratteristiche principali: navigazione più veloce, zero telemetria, blocco degli annunci e supporto delle estensioni*



**2. Personalizzazione Interface**


![Options de personnalisation](assets/fr/05.webp)


*La schermata di personalizzazione consente di configurare l'aspetto delle schede e del Interface in base alle proprie preferenze*





- Importazione dei dati**: Trasferimento facile di preferiti e password da Safari, Chrome o Firefox
- Sincronizzazione ICloud**: Attiva per trovare i tuoi preferiti e le tue schede su tutti i tuoi dispositivi Apple



**3. Installazione su dispositivi mobili**


![Installation sur iOS](assets/fr/06.webp)


*Schermata di installazione su iOS che mostra il codice QR per scaricare rapidamente Orion Browser dall'App Store*



**4. Interface benvenuto e strumenti essenziali



![Page d'accueil Orion](assets/fr/07.webp)


*Pagina iniziale di Orion Browser Interface: la freccia indica i tre strumenti chiave accessibili direttamente dalla barra Address*



Una volta completata la configurazione, si scoprirà il semplificato Interface di Orion con i suoi **tre strumenti essenziali** (indicati dalla freccia):





- Shield 🛡️**: Visualizza il rapporto sulla privacy con il numero di elementi bloccati nella pagina corrente
- Pennello 🖌️**: Personalizzazione della visualizzazione delle pagine (tema, font, rimozione di Elements che distraggono)
- Gear ⚙️**: Configurare i parametri specifici del sito web (permessi, blocco, ecc.)



Questi strumenti sono sempre disponibili e consentono di controllare l'esperienza di navigazione su base individuale.



**Importante**: Orion è gratuito e non richiede la registrazione o la creazione di un account per funzionare.



![Orion+ dans les préférences](assets/fr/08.webp)


*Schermata di abbonamento a Orion+ nelle preferenze, che offre un abbonamento opzionale per supportare lo sviluppo*



**Orion+ (opzionale)**: Per supportare lo sviluppo del progetto, Kagi offre Orion+ ($5/mese, $50/anno o $150 a vita). Questa sottoscrizione volontaria consente a:




- Comunicare direttamente con il team di sviluppo
- Influenzare l'evoluzione del browser in base alle proprie esigenze
- Accesso alle versioni Nightly con le ultime funzionalità sperimentali
- Usufruite dell'ultimo motore WebKit
- Ottenere un badge distintivo sul forum di feedback



Orion+ garantisce l'indipendenza del progetto: "Il vostro contributo finanziario ci aiuta a rimanere indipendenti e a mantenere la promessa di diventare il miglior browser per i nostri utenti". È questo modello di finanziamento degli utenti che mantiene Orion privo di pubblicità e di telemetria.



## Configurazione per la massima riservatezza



### Parametri essenziali



Accedere alle preferenze tramite **Orion → Preferenze** (o ⌘,):



**1. Ricerca - Motore di ricerca privato**



![Configuration du moteur de recherche](assets/fr/09.webp)


*Configurazione predefinita del motore di ricerca: DuckDuckGo è selezionato per garantire la massima privacy*





- Motore predefinito**: Selezionare **DuckDuckGo**, **Startpage** o **Kagi** per una privacy ottimale (evitare Google/Bing)
- Suggerimenti di ricerca**: Disabilitarli per evitare che i tasti premuti vengano trasmessi ai server dei motori di ricerca



**2. Privacy - Protezione generale**



![Content Blocker dans les préférences](assets/fr/12.webp)


*Le impostazioni sulla privacy di Orion mostrano il blocco dei contenuti con 119.156 regole attive, le opzioni di rimozione dei tracker e l'agente utente personalizzato*



**Blocco dei contenuti attivo per impostazione predefinita**:




- EasyList**: 119k+ regole di blocco degli annunci
- EasyPrivacy**: Protezione contro il tracciamento
- Gestire gli elenchi di filtri**: Aggiungere altri elenchi (consigliato Hagezi)



**Opzioni di privacy**:




- Rimuove i tracker dagli URL**: "Solo per la navigazione privata" pulisce i link copiati
- Condividere i rapporti sugli incidenti**: "Dopo aver chiesto l'approvazione" rispetta il vostro consenso
- Agente utente personalizzato**: Può essere modificato per aggirare alcuni blocchi



![YouTube avec Privacy Report](assets/fr/10.webp)


*Esempio di YouTube visualizzato con Orion: nessuna pubblicità visibile e Rapporto sulla privacy che mostra i numerosi Elements bloccati*



**3. Impostazioni del sito web - Controllo per sito**



![Website Settings pour YouTube](assets/fr/11.webp)


*Le impostazioni del sito web per YouTube mostrano le opzioni di compatibilità, il blocco dei contenuti e le autorizzazioni specifiche del sito*



**Accesso rapido**: Fare clic sull'ingranaggio ⚙️ nella barra Address per regolare:




- Modalità compatibilità**: Risolve i problemi di visualizzazione sospendendo le estensioni
- Blocco dei contenuti**: Disattivare il blocco per un sito specifico, se necessario
- JavaScript/Cookies**: Controllo granulare per sito
- Autorizzazioni**: Telecamera, microfono, posizione configurati individualmente



**4. Filtri personalizzati avanzati** (vedere sotto)



**Creare filtri personalizzati** (Privacy → Gestione elenchi filtri → Filtri personalizzati):



**Sintassi semplificata** (compatibile con Adblock Plus):




- `reddit.com##.promotedlink`: Nasconde i post sponsorizzati di Reddit
- `||ads.example.com^`: Blocca completamente un dominio pubblicitario
- `@@||sito-utile.com^`: Crea un'eccezione per un sito



**Suggerimento: Visitate [FilterLists.com](https://filterlists.com) per migliaia di elenchi specializzati pronti all'uso.



### Estensioni consigliate



Orion supporta nativamente le estensioni per Chrome e Firefox. Installatele direttamente dagli store ufficiali:



**Essenziali**:




- uBlock Origin**: Aggiunge un controllo granulare al blocco nativo
- Bitwarden**: Gestore di password open-source
- Cancella URL**: Cancella i parametri di tracciamento degli URL



**Opzionale**:




- LocalCDN**: Serve le librerie condivise localmente
- Cookie AutoDelete**: Cancella automaticamente i cookie dopo la chiusura delle schede
- NoScript**: Controllo totale sull'esecuzione di JavaScript (utenti avanzati)



Per installare un file:




- Visitare [chrome.google.com/webstore](https://chrome.google.com/webstore) o [addons.mozilla.org](https://addons.mozilla.org)
- Fare clic su "Aggiungi a Chrome/Firefox"
- Orion intercetterà e installerà automaticamente l'estensione



**Attenzione**: Poiché il supporto delle estensioni è sperimentale, molte di esse potrebbero non funzionare correttamente o influire sulle prestazioni. In caso di problemi (sito non più funzionante, lentezza), disattivare le estensioni una per una per identificare la fonte.



## Uso quotidiano



### Interface e caratteristiche uniche




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Menu a pennello di Orion per la personalizzazione della visualizzazione: dimensione dei caratteri, tema (chiaro/scuro), disattivazione delle intestazioni adesive e rimozione di Elements* che distraggono



**Strumento pennello: personalizzazione avanzata**



Lo strumento **brush** di Orion è una caratteristica unica che consente di personalizzare la visualizzazione di ogni sito web:



**Opzioni del tema**:




- Passare da un tema chiaro a uno scuro per ogni sito
- Adattamento automatico alle preferenze del sistema



**Controllo tipografico**:




- Dimensione del carattere**: Regolare la leggibilità con i pulsanti A- e A+
- Stile carattere**: Cambia la famiglia di caratteri (predefinita o personalizzata)



**Pulizia Interface**:




- Disabilita le intestazioni appiccicose**: Rimuove le intestazioni che rimangono bloccate in alto durante lo scorrimento
- Cancellare Elements**: Rimuove in modo permanente il fastidioso Elements (annunci, pop-up, cookie banner)
  - Cliccate su "+ Cancella" e selezionate l'elemento da nascondere
  - Molto utile per i siti con annunci persistenti o tracciamento visivo Elements



**Persistenza**: Tutte queste impostazioni vengono salvate per dominio e riapplicate automaticamente alla visita successiva.



**Gestione avanzata delle schede**:




- Schede verticali**: Si attivano tramite la barra dei menu (funzione Schede laterali)
- Schede compatte**: In Preferenze → Schede → Layout "Compatto" per risparmiare spazio
- Gruppi di schede**: Organizzare le sessioni per tema
- Profili multipli**: Creare identità separate tramite la barra dei menu (funzione Profili) con dati completamente isolati



**Modalità a basso consumo**: Ispirata all'iPhone, questa modalità sospende automaticamente le schede inattive dopo 5 minuti e può ridurre il consumo energetico fino al 90%. Attivatela tramite la barra dei menu di Orion su Mac o nelle impostazioni su iOS.



**Strumenti integrati** (menu Modifica e altri):




- Modifica il testo della pagina**: modifica temporaneamente qualsiasi testo (menu Modifica)
- Consenti copia e incolla**: Supera le restrizioni alla copia (menu Modifica)
- Copia collegamento pulito**: Fare clic con il tasto destro del mouse su un link per rimuovere i parametri di tracciamento
- Modalità Focus**: navigazione senza distrazioni e a schermo intero
- Immagine nell'immagine**: Guarda i video in una finestra fluttuante
- Aprire in Internet Archive**: Accesso diretto alle versioni archiviate
- Rapporto sulla privacy**: Fare clic sullo scudo 🛡️ per visualizzare gli elementi bloccati per pagina



### Gestione della navigazione privata



La navigazione privata di Orion (⌘⇧N) offre:




- Isolamento completo di cookie e sessioni
- Cancellazione automatica alla chiusura
- Cronologia e disattivazione della cache
- Maggiore protezione contro le impronte digitali



**Suggerimento**: Per una compartimentazione avanzata, creare **profili separati** tramite la barra dei menu (funzione Profili). Ogni profilo appare come un'applicazione separata nel Dock, con le proprie impostazioni, estensioni e dati completamente isolati.



### Ottimizzazione delle prestazioni e privacy



Per mantenere Orion veloce e privato:




- Estensioni**: Limitare al minimo indispensabile (può ridurre le prestazioni)
- Modalità basso consumo**: Attivare per sessioni prolungate (risparmio del 90% possibile)
- Rapporto sulla privacy**: Fare clic sullo scudo 🛡️ per vedere i blocchi in tempo reale
- Personalizzazione visiva**: Utilizzate il pennello 🖌️ per adattare la visualizzazione e rimuovere la Elements che distrae
- Copia di un link pulito**: Fare clic con il tasto destro del mouse per copiare i link senza tracker
- Profili separati**: Utilizzate profili dedicati per compartimentare le vostre attività
- Impostazioni del sito web**: Fare clic sull'ingranaggio ⚙️ per adattare le autorizzazioni in base al sito
- Pulizia regolare**: Cancellare la cache tramite Orion → Cancellare i dati di navigazione



## Confronto con le alternative



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**Rispetto a Safari**: Orion offre una protezione superiore grazie al suo blocco avanzato e al supporto delle estensioni, mantenendo le prestazioni di WebKit.



**Versus Chrome**: privacy impareggiabile senza compromettere la compatibilità, grazie al supporto delle estensioni di Chrome.



**Rispetto a Firefox**: Più veloce su Mac, Interface più intuitivo, ma meno controllo granulare e non open-source.



**Rispetto a Brave**: Filosofia simile, ma Orion evita le controversie su cripto/BAT e offre una migliore integrazione con Apple.



## Casi d'uso consigliati



**Ideale per**:




- Gli utenti Apple cercano più privacy di Safari
- Persone che desiderano bloccare tutti gli annunci (compreso YouTube) senza estensioni
- Gli sviluppatori necessitano di devtools WebKit con protezione della privacy integrata
- Gli utenti iPhone vogliono estensioni desktop su mobile (innovazione unica)
- Professionisti che hanno bisogno di compartimentare le proprie attività (profili multipli)
- Utenti di telefonia mobile alla ricerca di una migliore gestione della batteria (modalità a basso consumo)



**Evitare se**:




- Utilizzate principalmente Windows/Linux (nessuna versione disponibile)
- L'open-source completo è essenziale per il vostro modello di minaccia
- Dipendete da estensioni specifiche che potrebbero non funzionare
- È necessaria una sincronizzazione multipiattaforma che vada oltre l'ecosistema Apple
- Preferite una soluzione stabile e collaudata (in stato di beta permanente dal 2021)



## Punti di attenzione e sicurezza



### Caratteristiche di sicurezza uniche



**Protezione rivoluzionaria anti-fingerprinting**: Orion è l'unico browser che blocca completamente l'esecuzione degli script di fingerprinting prima che questi possano scansionare il sistema. Questo approccio "nessuno script in esecuzione = nessun fingerprinting possibile" supera i tradizionali metodi di mascheramento utilizzati da altri browser.



**Whitelist trasparente**: Orion mantiene un piccolo elenco pubblico di siti (browserbench.org, wizzair.com) in cui il blocco viene automaticamente disabilitato per evitare malfunzionamenti. Questa trasparenza consente agli utenti di capire esattamente quando e perché il blocco viene attenuato.



**Estensioni non verificate**: Il supporto per le estensioni di Chrome/Firefox introduce ulteriori rischi, in quanto queste estensioni non sono state progettate per WebKit e non sono specificamente verificate per questo ambiente.



### Manutenzione e aggiornamenti





- Aggiornamenti automatici**: Orion si aggiorna automaticamente su macOS tramite Sparkle
- Monitoraggio delle vulnerabilità**: Controllare regolarmente le note di rilascio per le patch di sicurezza
- Segnalazione di bug**: Utilizzare [orionfeedback.org](https://orionfeedback.org) per segnalare i problemi




## Conclusione



Orion Browser rappresenta un significativo passo avanti per la privacy su macOS e iOS. Il suo approccio a zero telemetria, combinato con un blocco nativo ultra-efficiente e un supporto unico per le estensioni universali, lo rende una scelta eccellente per gli utenti Apple attenti alla privacy.



**Importante**: Orion rimane in beta permanente dal 2021, con limitazioni di compatibilità delle estensioni e rischi intrinseci di WebKit. Valutare questi compromessi in base al proprio modello di minaccia.



Per l'uso quotidiano su Mac o iPhone, è probabilmente il miglior compromesso tra riservatezza, prestazioni e facilità d'uso disponibile nell'ecosistema Apple, a patto di accettarne i limiti.



Ricordate: la protezione della privacy non dipende solo dal browser. Combinate Orion con le migliori pratiche (password forti, 2FA, VPN se necessario) per una sicurezza online ottimale.



## Risorse e supporto



### Documentazione ufficiale




- Sito web ufficiale**: [kagi.com/orion](https://kagi.com/orion/)
- FAQ complete**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- Forum della comunità**: [community.kagi.com](https://community.kagi.com)
- Tracciamento di bug**: [orionfeedback.org](https://orionfeedback.org)
- GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Componenti open-source
- Blog Kagi**: [blog.kagi.com](https://blog.kagi.com) - Notizie e aggiornamenti



### Test di verifica consigliati



Dopo la configurazione, testare la configurazione:




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Test delle impronte digitali
- [DNS Leak Test](https://www.dnsleaktest.com/) - Verifica la presenza di perdite DNS
- [BrowserLeaks](https://browserleaks.com/) - Suite completa di test sulla privacy



### Alternative al Plan ₿ Network


Per la massima protezione, consultate le nostre altre guide:




- [Firefox hardened](https://planb.network/tutorials/computer-security/firefox) - Configurazione multipiattaforma avanzata
- [Tor Browser](https://planb.network/tutorials/computer-security/tor-browser) - Completo anonimato in rete
- [Mullvad Browser](https://planb.network/tutorials/computer-security/mullvad-browser) - Massima protezione dalle impronte digitali



Se volete saperne di più sulla storia e sul funzionamento dei browser, nonché sui principali oggetti digitali della vostra vita quotidiana, vi invito a scoprire il nostro nuovo corso di formazione gratuito SCU 202, disponibile su Plan ₿ Network:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
---
name: Mullvad Browser
description: Come usare il browser Mullvad per la privacy
---

![cover](assets/cover.webp)



In un mondo in cui la sorveglianza digitale sta diventando onnipresente, proteggere la vostra privacy online non è mai stato così importante. Le aziende utilizzano tecniche sofisticate per tracciarvi:





- **Cookie di terze parti**: piccoli file depositati da siti esterni per seguirvi da un sito all'altro
- **Fingerprinting**: raccoglie le caratteristiche uniche del vostro browser e del vostro dispositivo (risoluzione dello schermo, font installati, plugin, ecc.) per identificarvi senza cookie
- **Script di tracciamento**: codici JavaScript invisibili che analizzano il comportamento di navigazione dell'utente (clic, scorrimento, tempo trascorso)
- **Analisi IP Address**: localizzazione geografica e identificazione del vostro fornitore di servizi Internet



Questi dati vengono poi combinati per creare profili dettagliati del vostro comportamento online e monetizzati, spesso a vostra insaputa. Questa realtà solleva una domanda fondamentale: come si può navigare in Internet mantenendo l'anonimato e la riservatezza?



La risposta sta in gran parte nella scelta del browser web. Questo strumento, che utilizziamo ogni giorno per accedere alle informazioni, fare acquisti o comunicare, svolge un ruolo decisivo nella protezione dei nostri dati personali. Purtroppo, i browser più diffusi, come Google Chrome (che detiene circa il 65% del mercato globale), sono progettati intorno a modelli commerciali basati sulla raccolta massiccia di dati degli utenti.



![MULLVAD BROWSER](assets/fr/01.webp)


*Mullvad Browser si distingue per il blocco dei tracker eccezionalmente efficace, superando di gran lunga i browser consumer*



Di fronte a questa sfida, stanno emergendo nuovi attori con una filosofia diversa: quella di porre la privacy al centro del proprio design. Tra questi, Mullvad Browser si distingue come soluzione innovativa che combina le migliori protezioni della privacy con un'esperienza di navigazione fluida e accessibile.



A differenza dei browser tradizionali che cercano di personalizzare l'esperienza dell'utente raccogliendo i suoi dati, Mullvad Browser adotta l'approccio opposto: fa sì che tutti i suoi utenti appaiano identici ai siti web, rendendo così praticamente impossibile il tracciamento personalizzato.



In questa esercitazione scopriremo insieme come Mullvad Browser può trasformare il vostro modo di navigare in Internet, offrendovi una solida protezione contro la sorveglianza senza sacrificare la facilità d'uso.




## Introduzione al browser Mullvad



**Mullvad Browser** è un browser web incentrato sulla privacy sviluppato in collaborazione con il Progetto Tor e distribuito gratuitamente dalla società svedese Mullvad VPN. Lanciato nell'aprile del 2023, si presenta come un **"Tor Browser senza la rete Tor "**, progettato per ridurre al minimo il tracciamento e l'impronta digitale online, consentendo agli utenti di navigare tramite una VPN affidabile anziché tramite la rete Tor.



Mullvad Browser è un browser gratuito e open-source basato su Firefox ESR (la versione più longeva di Mozilla Firefox) e reso più resistente dagli esperti del Progetto Tor. In concreto, include la maggior parte delle **funzioni di protezione di Tor Browser**, ma **non instrada il traffico attraverso la rete Tor**. Al contrario, gli utenti possono (e dovrebbero) collegarlo a una VPN crittografata affidabile per rendere anonimo il proprio IP Address.



In termini di esperienza d'uso, Mullvad Browser assomiglia a un browser classico, offrendo una navigazione fluida. È disponibile gratuitamente su Windows, macOS e Linux (senza versione mobile). Non è necessario essere abbonati a Mullvad VPN per utilizzarlo; tuttavia, **l'utilizzo di Mullvad Browser senza mascherare il proprio IP non garantisce un completo anonimato**, per cui si consiglia vivamente di utilizzarlo insieme a una VPN affidabile.



### Obiettivi: privacy e anti-tracciamento



Il browser Mullvad è stato progettato con un obiettivo principale: **proteggere la privacy degli utenti** online e contrastare le comuni tecniche di tracciamento e profilazione. I suoi obiettivi principali includono:





- Riducete drasticamente il tracciamento degli annunci e il **tracking** da parte di siti web e agenzie pubblicitarie. Per impostazione predefinita, Mullvad Browser blocca i tracker di terze parti, i cookie di tracciamento e gli script di fingerprinting che potrebbero identificare l'utente.





- Standardizzate l'impronta digitale del vostro browser per **"confondersi con la massa"**. L'impronta digitale è come una "carta d'identità" unica creata combinando tutte le caratteristiche del vostro browser. Mullvad Browser fa in modo che tutti i suoi utenti abbiano esattamente la stessa "carta d'identità", rendendo impossibile distinguerli singolarmente.





- Offre una protezione immediata senza estensioni aggiuntive. Mullvad Browser viene fornito in una configurazione "pronta all'uso": l'utente non deve installare una serie di estensioni o modificare alcuna impostazione per essere protetto.





- Non sacrificate le prestazioni o l'ergonomia più del necessario. In assenza del routing Tor, **Mullvad Browser** offre una navigazione molto più veloce di **Tor Browser**, avvicinandosi alle prestazioni di un browser standard abbinato a una VPN.



### Caratteristiche principali del browser Mullvad



Mullvad Browser include una serie di **funzioni di sicurezza e privacy** direttamente ispirate a Tor Browser:





- **Navigazione privata in ogni momento:** La modalità di navigazione privata è attivata per impostazione predefinita e non può essere disattivata. **Non vengono memorizzati cronologia, cookie o cache da una sessione all'altra**. Non appena si chiude Mullvad Browser, tutti i dati di navigazione vengono eliminati.





- **Protezione avanzata contro il fingerprinting:** Il browser applica impostazioni rigorose per contrastare il fingerprinting digitale. Questo include:
- Standardizzazione dell'**agente utente** e della versione del browser
- Fuso orario impostato su **UTC** per tutti gli utenti
- **Letterboxing**: una tecnica che aggiunge automaticamente margini grigi intorno alle pagine web per standardizzare le dimensioni di visualizzazione e impedire l'identificazione in base alle dimensioni dello schermo
- **Blocco delle API di fingerprinting**: Le tecnologie Canvas (disegno 2D), WebGL (grafica 3D) e AudioContext (elaborazione audio) sono disabilitate perché possono rivelare dettagli unici sull'hardware
- **Font di sistema standardizzati** per evitare l'identificazione da parte dei font installati





- Blocco di tracker e pubblicità: Mullvad Browser integra nativamente l'estensione **uBlock Origin** (preinstallata) con liste di protezione aggiuntive per bloccare **tracker di terze parti, script pubblicitari e altri contenuti dannosi**. Questa protezione è accompagnata dal **First-Party Isolation**: una tecnica che memorizza i cookie in "vasi" separati per ogni sito web, impedendo a un sito di leggere i cookie depositati da un altro.





- **Pulsante di ripristino della sessione:** Come il pulsante "Nuova identità" di Tor Browser, Mullvad Browser offre un pulsante per **riavviare rapidamente il browser con una nuova sessione vuota**.





- **Livelli di sicurezza regolabili:** È possibile regolare il livello di sicurezza (*Normale*, *Più sicuro*, *Sicuro*) nelle impostazioni, proprio come in Tor Browser.



## Estensioni integrate per impostazione predefinita



Mullvad Browser include **tre estensioni preinstallate** che costituiscono il nucleo della sua protezione anti-tracciamento. **È fondamentale non rimuoverle o modificarne le configurazioni**, in quanto ciò vi renderebbe unici tra gli utenti di Mullvad Browser:



### **Blocco Origine**


Questa estensione per il blocco di annunci e tracker è preconfigurata con **elenchi di filtri ottimizzati** per bloccare:




- Pubblicità invasiva
- Tracker di terze parti che raccolgono i vostri dati
- Script dannosi
- Tracciamento comportamentale Elements



uBlock Origin in Mullvad Browser utilizza parametri standardizzati per garantire che tutti gli utenti blocchino esattamente lo stesso Elements, preservando così l'uniformità delle impronte digitali.



### **NoScript**


NoScript viene eseguito in background per gestire i **livelli di sicurezza** del browser. Questo:




- Controlla l'esecuzione di **JavaScript** in base al livello selezionato (normale/massima sicurezza/massima sicurezza)
- Filtra automaticamente gli attacchi **XSS** (Cross-Site Scripting)
- Blocca i contenuti attivi pericolosi su siti non HTTPS
- La sua icona è nascosta per impostazione predefinita, ma può essere visualizzata tramite "Personalizza barra degli strumenti"



### *estensione* **Mullvad Browser**


Questa estensione specifica di Mullvad offre diverse funzionalità a seconda che siate o meno clienti di Mullvad VPN:



#### **Senza l'abbonamento a Mullvad VPN:**




- **Controllo di base della connessione**: visualizza l'IP pubblico attuale e alcune informazioni sulla connessione
- **Raccomandazioni sulla privacy**: suggerimenti per migliorare le impostazioni di sicurezza (DNS, solo HTTPS, motore di ricerca)
- **Controllo WebRTC**: abilitazione/disabilitazione per evitare perdite IP Address
- Può essere eliminato senza **impatto** sulla vostra impronta digitale se non utilizzate Mullvad VPN



#### **Con l'abbonamento a Mullvad VPN:**


L'estensione rivela tutto il suo potenziale con funzioni avanzate:





- **Proxy SOCKS5 integrato**: connessione con un solo clic al server proxy Mullvad VPN
- **IP Address fisso**: a differenza di una VPN, che può cambiare il proprio IP Address, un proxy garantisce sempre lo stesso Address in uscita
- **Interruttore automatico**: se la VPN si disconnette, il traffico del browser viene immediatamente bloccato
- **Supporto IPv6**: Connettività IPv6 anche se la connessione VPN non è abilitata





- **Multihop (doppia VPN)**: possibilità di cambiare la posizione del proxy per creare un tunnel nel tunnel
 - Il traffico passa prima attraverso il server VPN, poi "salta" a un altro server Mullvad
 - Utilizzare una localizzazione diversa solo per il browser





- **Monitoraggio avanzato della connessione**: monitoraggio in tempo reale dello stato della VPN, del server connesso e del rilevamento delle perdite DNS





- **Accesso a Mullvad Leta**: motore di ricerca privato riservato agli abbonati (anche se sconsigliato da Mullvad per motivi di correlazione con il proprio account)



Queste tre estensioni lavorano insieme per creare un ecosistema coerente di protezione, in cui ogni utente beneficia esattamente delle stesse difese senza possibilità di personalizzazione che comprometterebbe l'anonimato collettivo.



## Vantaggi e svantaggi di Mullvad Browser



### Vantaggi





- **Eccellente protezione della privacy per impostazione predefinita:** Mullvad Browser applica fin dall'inizio impostazioni di privacy molto rigorose, senza necessità di configurazione manuale.





- **Prestazioni migliori di Tor Browser:** In assenza di onion routing, Mullvad Browser è **notevolmente più veloce e reattivo** di Tor Browser per la navigazione web classica.





- La familiare semplicità del **Interface**: Mullvad Browser è basato sul Interface di Firefox. Se siete abituati a Firefox o anche a Tor Browser, non vi sentirete fuori posto.





- **Collaborazione fidata e codice verificato:** Mullvad Browser si avvale dell'esperienza del Progetto Tor e tutto il codice sorgente è disponibile per una verifica esterna.



### Svantaggi





- Nessun anonimato di rete senza VPN: Il punto più importante è che **Mullvad Browser non nasconde il vostro IP Address da solo** (come tutti gli altri browser, tranne Tor Browser). Il vostro IP Address è come il vostro "Address postale" su Internet: rivela la vostra posizione e il vostro ISP. Per questo motivo **dipende fortemente da una VPN** (rete privata virtuale) per nascondere queste informazioni cruciali.





- **Nessuna versione mobile:** Ad oggi, Mullvad Browser è disponibile solo su PC (Windows, Mac, Linux).





- Incompatibile con alcune abitudini: La **modalità privata permanente** significa che non è possibile mantenere una sessione da un utilizzo all'altro. È impossibile rimanere connessi a un account Web da una sessione all'altra.





- **Funzioni limitate:** Per preservare l'uniformità delle impronte digitali, Mullvad Browser ha **disabilitato diverse funzioni** presenti in Firefox e non è destinato alla personalizzazione.



## Installazione del browser Mullvad



Mullvad Browser è disponibile gratuitamente per Windows, macOS e Linux. Per installarlo, visitate [il sito ufficiale di Mullvad](https://mullvad.net/browser).



![MULLVAD BROWSER](assets/fr/02.webp)



*Home page ufficiale di Mullvad Browser con il pulsante di download evidenziato.*



![MULLVAD BROWSER](assets/fr/03.webp)



*Selezionate il vostro sistema operativo nella pagina di download di Mullvad Browser.*



Fare clic sul pulsante **"Download "** corrispondente al proprio sistema operativo.



Per Linux, è possibile scegliere tra diversi formati a seconda della distribuzione. Una volta completato il download:



### Su Windows


Eseguire il file `.exe' scaricato e seguire le istruzioni di installazione.



### Su macOS


Aprite il file `.dmg' scaricato e trascinate l'applicazione Mullvad Browser nella cartella Applicazioni.



### Su Linux


Estrarre l'archivio `.tar.xz' nella directory desiderata ed eseguire il file `start-mullvad-browser.desktop'.



## Configurazione e primo utilizzo



Quando si avvia per la prima volta Mullvad Browser, viene visualizzato un Interface molto simile a quello di Tor Browser. Il browser è preconfigurato per la privacy e non richiede modifiche particolari.



![MULLVAD BROWSER](assets/fr/04.webp)



*Interface Pagina iniziale di Mullvad Browser con estensioni, icona della scopa per generare una nuova identità e menu dell'applicazione in alto a destra*



**Importante:** Mullvad Browser non maschera il vostro IP Address per impostazione predefinita. Per una protezione completa, si consiglia vivamente di utilizzare una VPN in parallelo. È possibile utilizzare Mullvad VPN o qualsiasi altro servizio VPN affidabile.



Il browser include anche **DNS-over-HTTPS (DoH)** che utilizza il servizio DNS di Mullvad: questa tecnologia cripta le richieste DNS (traducendo i nomi dei siti in indirizzi IP) per impedire al vostro ISP di monitorare i siti che visitate.



### Impostazioni di sicurezza



È possibile regolare il livello di sicurezza facendo clic sul **menu dell'applicazione** (tre barre orizzontali) in alto a destra, poi su **"Impostazioni "**, quindi sulla scheda **"Privacy e sicurezza "**. Scorrere fino alla sezione **"Sicurezza "**:



![MULLVAD BROWSER](assets/fr/05.webp)



*Scelta dei livelli di sicurezza: le frecce indicano il percorso dal menu dell'applicazione alla scheda "Privacy e sicurezza" alle opzioni di sicurezza*



Mullvad Browser offre tre livelli di sicurezza:





- **Normale** (attuale livello predefinito): Tutte le funzioni del browser e del sito web sono abilitate





- **Più sicuro**: Disabilita le funzioni dei siti web spesso pericolose, che possono comportare una perdita di funzionalità su alcuni siti web:
 - JavaScript è disabilitato per i siti non HTTPS
 - Alcuni font e simboli matematici sono disabilitati
 - Suoni e video (HTML5 media) e WebGL sono "click to play"





- **Il più sicuro**: Consente solo le funzioni del sito web necessarie per i siti statici e i servizi di base:
 - JavaScript è disabilitato per impostazione predefinita per tutti i siti
 - Alcuni font, icone, immagini e simboli matematici sono disabilitati
 - Suoni e video (HTML5 media) e WebGL sono "click to play"



### Pulsante Nuova sessione



Per riavviare una sessione vuota senza chiudere il browser, fare clic sull'icona della scopa o utilizzare il menu dell'applicazione > **"Nuova sessione "**.



![MULLVAD BROWSER](assets/fr/06.webp)



*Ripristina la tua identità" per riavviare il browser con una sessione completamente nuova*



## Uso quotidiano



### Navigazione normale



Mullvad Browser si comporta come un browser classico per la navigazione quotidiana. Tutti i siti web sono accessibili come al solito, con il vantaggio di una maggiore protezione contro il tracciamento.



### Gestione dei cookie e login



A causa della modalità privata permanente, dovrete riconnettervi ai vostri account a ogni accesso. Questo è il prezzo da pagare per la massima riservatezza.



### Estensioni



Mullvad Browser tecnicamente consente di installare estensioni aggiuntive dal catalogo di Firefox, ma **è importante capire le implicazioni**. Ogni estensione aggiunta modifica la vostra impronta digitale e vi distingue dagli altri utenti di Mullvad Browser, il che va contro il principio fondamentale del browser: far apparire tutti gli utenti identici.



Come spiega Mullvad: *"A volte, non avere una difesa specifica è meglio che averne una". Volendo aumentare la privacy online, si installano estensioni che alla fine ci rendono ancora più visibili. "*



Se decidete di installare comunque delle estensioni, sappiate che state creando un'impronta digitale unica che può essere utilizzata per rintracciarvi da un sito all'altro. Per la massima protezione, è meglio attenersi alle tre estensioni preinstallate, che sono identiche per tutti gli utenti.



## Le migliori pratiche con Mullvad Browser



1. **Usate sempre una VPN**: Mullvad Browser non maschera il vostro IP. Una VPN è essenziale per il completo anonimato.



2. **Non personalizzare il browser**: Evitare di modificare le impostazioni o di aggiungere estensioni, in quanto ciò potrebbe rendere l'utente identificabile.



3. **Utilizzare il pulsante di nuova sessione**: Tra un'attività e l'altra, utilizzare la funzione di ripristino per suddividere le sessioni.



4. **Scegliete il livello di sicurezza più adatto alle vostre esigenze**:




- **Normale (consigliato)**: Per la navigazione quotidiana. Offre già un'eccellente protezione, pur mantenendo la funzionalità dei siti web. È il miglior equilibrio per il 95% degli utenti.
- **Più sicuro**: Se si visitano siti sconosciuti o potenzialmente pericolosi, o per una maggiore protezione sulle reti Wi-Fi pubbliche. Alcuni siti potrebbero non funzionare correttamente.
- **Il più sicuro**: Riservato a situazioni ad alto rischio (giornalismo investigativo, comunicazioni sensibili, ambienti ostili). La maggior parte dei siti moderni sarà danneggiata, ma questo è il prezzo della massima sicurezza.



5. **Controllate regolarmente gli aggiornamenti**: Mantenete il vostro browser aggiornato con le ultime patch di sicurezza.



6. **Utilizzare motori di ricerca rispettosi della privacy**: Scegliete DuckDuckGo, Startpage o Searx invece di Google.



7. **Abilitare la modalità solo HTTPS**: Nelle impostazioni, assicurarsi che la modalità "Solo HTTPS" sia abilitata per forzare le connessioni sicure.



8. **NON modificare le impostazioni avanzate**: A differenza di altri browser, Mullvad Browser è progettato in modo che TUTTI gli utenti abbiano esattamente la stessa configurazione. Modificare le impostazioni in `about:config` o cambiare le impostazioni di uBlock Origin/NoScript vi renderebbe unici e annullerebbe completamente l'anonimato del browser.



## Configurazione DNS consigliata



Mullvad Browser integra automaticamente Mullvad DNS-over-HTTPS. Se si utilizza Mullvad VPN, l'estensione consiglia di **disabilitare Mullvad DoH** perché è più veloce utilizzare il server DNS del server VPN. Se non si utilizza Mullvad VPN, mantenere Mullvad DoH abilitato per evitare il monitoraggio DNS da parte dell'ISP.



## Conclusione



Mullvad Browser è una soluzione eccellente per chi cerca una navigazione web rispettosa della privacy senza i limiti di prestazioni della rete Tor. In combinazione con una VPN di qualità, offre una solida protezione contro il tracciamento e la sorveglianza online.



Sebbene presenti alcune limitazioni (assenza di una versione mobile, sessioni non persistenti), Mullvad Browser è uno strumento prezioso nell'arsenale di chiunque desideri riprendere il controllo della propria privacy digitale. La sua facilità d'uso e la configurazione predefinita lo rendono una scelta saggia per gli utenti attenti alla privacy, siano essi principianti o esperti.



## Risorse



### Documentazione ufficiale




- [Sito ufficiale del browser Mullvad](https://mullvad.net/fr/browser)
- [Pagina di download del browser Mullvad](https://mullvad.net/en/download/browser)
- [Specifiche tecniche dettagliate](https://mullvad.net/en/browser/Hard-facts)
- [Estensione del browser Mullvad](https://mullvad.net/en/help/mullvad-browser-extension)



### Guide e spiegazioni




- [Perché la privacy è importante](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor senza Tor: concetto di browser Mullvad](https://mullvad.net/en/browser/tor-without-tor)
- [Come scegliere un browser rispettoso della privacy](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Capire il fingerprinting del browser](https://mullvad.net/en/browser/browser-fingerprinting)



### Assistenza e supporto




- [Centro di aiuto del browser Mullvad](https://mullvad.net/en/help/tag/mullvad-browser)
- [Primi passi per la privacy online](https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Risorse comunitarie




- [Guida al browser Mullvad - Guide alla privacy](https://www.privacyguides.org/en/desktop-browsers/)
- [Discussioni della comunità](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)
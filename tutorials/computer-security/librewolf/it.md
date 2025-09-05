---
name: LibreWolf
description: Come utilizzare il browser per la privacy LibreWolf
---

![cover](assets/cover.webp)



Ogni clic, ogni ricerca, ogni sito visitato: il vostro browser web è diventato un sofisticato informatore che alimenta un sistema di sorveglianza commerciale globale. Google Chrome, utilizzato da oltre 3 miliardi di persone, trasforma la vostra navigazione quotidiana in dati redditizi per i giganti della pubblicità. Anche Firefox, nonostante la sua reputazione di browser "etico", attiva di default meccanismi di telemetria che trasmettono le vostre abitudini di navigazione a Mozilla.



Questa realtà solleva una domanda essenziale: è ancora possibile navigare liberamente su Internet senza essere costantemente spiati e profilati? Fortunatamente la risposta è sì, grazie a progetti comunitari che rimettono l'utente al centro delle loro preoccupazioni.



LibreWolf incarna questa filosofia di resistenza digitale. Nato da una comunità di sviluppatori indipendenti, questo browser trasforma Firefox in un vero e proprio scudo contro la sorveglianza online. Laddove i browser commerciali cercano di monetizzare la vostra attenzione, LibreWolf fa l'opposto: vi rende invisibili ai tracker preservando un'esperienza di navigazione fluida e moderna.



In questa esercitazione scopriremo come LibreWolf può trasformare il modo di navigare sul web, offrendo una solida protezione contro il tracciamento senza sacrificare le prestazioni o la compatibilità con il web.



![LIBREWOLF](assets/fr/01.webp)


*Quota di mercato dei browser web: Chrome domina con il 65% del mercato, seguito da Safari ed Edge. Questo dominio solleva interrogativi sulla diversità del web e sulla privacy*



## Presentazione di LibreWolf



**FreeWolf** è un browser web open-source derivato da Mozilla Firefox, sviluppato e mantenuto da una comunità indipendente di appassionati di software libero. Il suo obiettivo principale è offrire una navigazione incentrata sulla privacy, la sicurezza e la libertà dell'utente.



In concreto, LibreWolf utilizza il motore Gecko di Firefox, ma con una filosofia radicalmente diversa: laddove Firefox deve trovare un equilibrio tra privacy e facilità d'uso, LibreWolf opta per la privacy di default. Il progetto rimuove tutto ciò che potrebbe violare la privacy dell'utente (telemetria, raccolta dati, moduli sponsorizzati), integrando al contempo impostazioni di sicurezza avanzate.



### Obiettivi: privacy e libertà



LibreWolf mira a massimizzare la protezione contro il tracciamento e il fingerprinting, migliorando al contempo la sicurezza del browser. I suoi obiettivi principali includono:





- Eliminare tutta la telemetria e la raccolta dati** in Firefox
- Disabilitare le funzioni che vanno contro la libertà dell'utente**, come i moduli DRM proprietari
- Applicare le impostazioni di privacy/sicurezza** e le patch specifiche fin dall'inizio
- Lo sviluppo comunitario garantisce trasparenza e indipendenza** dagli interessi commerciali



In breve, LibreWolf si presenta come "Firefox come sarebbe stato se la privacy fosse stata una priorità assoluta": un browser che rispetta l'utente per impostazione predefinita, senza bisogno di ulteriori configurazioni.



### Caratteristiche principali



Fin dall'inizio, LibreWolf offre una serie di funzioni orientate alla privacy:



**A differenza di Chrome o Firefox, che inviano determinate statistiche di utilizzo, LibreWolf non raccoglie assolutamente nulla dalla vostra navigazione. Nessun rapporto sugli arresti anomali, nessuno studio sugli utenti, nessun suggerimento sponsorizzato.



**LibreWolf integra in modo nativo l'estensione uBlock Origin, uno dei migliori bloccatori di annunci e tracker sul mercato. Per impostazione predefinita, LibreWolf filtra in modo aggressivo tutto ciò che potrebbe tracciare l'utente online (annunci invadenti, script di tracciamento, criptovalute Mining).



**Motore di ricerca privato per impostazione predefinita:** LibreWolf utilizza per impostazione predefinita DuckDuckGo come motore di ricerca iniziale, che non conserva la cronologia delle query effettuate. Sono disponibili anche altre alternative orientate alla privacy (Searx, Qwant, Whoogle).



**Protezione anti-fingerprint rinforzata:** Il fingerprinting consente di identificare in modo univoco un browser attraverso la sua configurazione, anche senza cookie. Per contrastare questo fenomeno, LibreWolf attiva la tecnologia RFP (Resist Fingerprinting) del progetto Tor, per rendere il browser il più generico possibile. I test dimostrano che un Firefox standard è unico per circa il 90% su strumenti come coveryourtracks.eff.org, mentre LibreWolf lo è solo per circa il 10-20% (queste cifre sono indicative e possono variare in base alla configurazione del software e dell'hardware e alle estensioni installate).



![LIBREWOLF](assets/fr/07.webp)


*Pagina di prova EFF [Cover Your Tracks](https://coveryourtracks.eff.org/) con il pulsante TEST YOUR BROWSER. Questa pagina viene utilizzata per valutare la protezione contro i tracker e le impronte digitali



![LIBREWOLF](assets/fr/08.webp)


*Risultato del test Cover Your Tracks. Viene visualizzato il messaggio "hai una forte protezione contro il tracciamento del Web", che mostra l'efficacia della protezione di LibreWolf.*



**LibreWolf attiva per impostazione predefinita impostazioni di sicurezza rigorose. La Protezione avanzata dal tracciamento di Firefox viene portata al livello severo per bloccare migliaia di tracker, cookie di terze parti e contenuti dannosi. Attiva inoltre l'isolamento dei siti e dei cookie (*Total Cookie Protection*) per suddividere i dati per ogni dominio e limita WebRTC (limitando i *candidati ICE* e l'instradamento tramite proxy quando è presente un proxy) per ridurre il rischio di fuga di dati IP Address.



**Aggiornamenti veloci del motore:** Il progetto segue molto da vicino gli sviluppi di Firefox: LibreWolf è sempre basato sull'ultima versione stabile di Firefox e i manutentori si sforzano di rilasciare una nuova versione entro 24-72 ore da ogni rilascio ufficiale di Firefox.



## Vantaggi e svantaggi



### Vantaggi





- Nessuna telemetria o connessione indesiderata:** LibreWolf non trasmette dati di utilizzo, garantendo il totale rispetto della vostra privacy.





- Open-source e basato sulla comunità:** Il progetto è al 100% open-source e gestito da volontari. Questa indipendenza garantisce che nessun modello pubblicitario possa influenzare lo sviluppo.





- Preconfigurato per la privacy:** LibreWolf vi fa risparmiare tempo prezioso: non c'è bisogno di passare ore a modificare le impostazioni di Firefox, è già tutto pronto.





- Ad blocker/tracker nativo:** uBlock Origin è integrato di serie, quindi non dovrete fare nulla per proteggervi da annunci e bug.





- Eccellente protezione anti-fingerprinting:** Grazie a RFP e alle numerose impostazioni sulla privacy, LibreWolf riduce drasticamente la vostra impronta digitale unica sul web.





- Prestazioni migliorate e leggerezza:** Rimuovendo la telemetria e alcune funzioni non essenziali, LibreWolf può essere leggermente più veloce e meno avido di energia rispetto a Firefox standard.



### Svantaggi e limiti





- Nessun aggiornamento automatico integrato:** LibreWolf non si aggiorna da solo. Spetta all'utente installare le nuove versioni non appena vengono rilasciate, per rimanere al sicuro.





- Compatibilità ridotta con alcuni servizi:** A causa delle sue impostazioni molto rigide, LibreWolf potrebbe incontrare problemi su alcuni siti web. Le piattaforme di streaming Netflix e Disney+ non funzioneranno, poiché LibreWolf disattiva il DRM Widevine per impostazione predefinita.





- Nessuna rete anonima integrata:** a differenza di Tor Browser, LibreWolf non instrada il traffico tramite Tor o una VPN. Se avete bisogno dell'anonimato di rete, dovrete configurare manualmente un proxy/VPN.





- Cookie e sessioni non persistenti (default):** Per motivi di riservatezza, LibreWolf cancella i cookie, la cronologia e i dati del sito ogni volta che si chiude il browser. Sarà necessario accedere nuovamente ai propri account ad ogni accesso.





- Nessuna versione mobile o sincronizzazione cloud:** LibreWolf è disponibile solo su desktop (Windows, Linux, macOS). Non esiste un'applicazione mobile e quindi non è possibile sincronizzare gli account o i segnalibri tramite cloud.



## Installazione di LibreWolf



**Sito ufficiale:** [librewolf.net](https://librewolf.net)



LibreWolf è disponibile per tutti i principali sistemi operativi desktop: Linux, Windows e macOS. Per scaricare LibreWolf, visitate il sito ufficiale:



![LIBREWOLF](assets/fr/02.webp)


*La pagina iniziale di LibreWolf (librewolf.net) mostra il logo del browser, il pulsante blu di installazione e i collegamenti al codice sorgente e alla documentazione. Una grande freccia blu indica il pulsante di installazione*



Fare clic sul pulsante "Installazione" per accedere alle istruzioni dettagliate relative al proprio sistema operativo:



![LIBREWOLF](assets/fr/03.webp)


*Pagina di selezione del sistema operativo per il download di LibreWolf.*



L'installazione varia a seconda del sistema operativo in uso:



### Su Linux


LibreWolf offre build per molte distribuzioni. Su Debian/Ubuntu e derivate è disponibile un repository APT ufficiale. In alternativa, LibreWolf è pubblicato in Flatpak su Flathub:


```
flatpak install flathub io.gitlab.librewolf-community
```



### Su Windows


Scaricare il programma di installazione (.exe) dal sito ufficiale o utilizzare il file:




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`



### Su macOS


LibreWolf è disponibile come pacchetto .dmg per Mac. Scaricate l'immagine del disco dal sito ufficiale e trascinate l'applicazione LibreWolf nella cartella Applicazioni. In alternativa, è possibile installarla tramite Homebrew.




## Configurazione e primo utilizzo



Al primo avvio, noterete la familiare Interface di Firefox, ma più spoglia: la pagina iniziale contiene solo la barra di ricerca e nessun suggerimento sponsorizzato. Nella barra degli strumenti è presente l'icona di uBlock Origin, segno che il blocco è attivo.



![LIBREWOLF](assets/fr/04.webp)


*Pagina iniziale di LibreWolf con estensioni e menu. Una freccia blu in alto a destra indica l'icona del menu (tre barre orizzontali)



LibreWolf carica automaticamente le pagine in modalità "strict" (anti-tracciamento) e il motore di ricerca predefinito sarà DuckDuckGo. Si può provare a visitare un sito di test di tracciamento (ad esempio amiunique.org) per osservare l'impronta esposta: dovrebbe essere molto più generica rispetto a quella di un browser standard.



### Impostazioni sulla privacy



LibreWolf è già configurato in modo ottimale per la privacy. In Menu → Opzioni → Privacy e sicurezza, vedrete che LibreWolf è impostato sulla modalità di protezione dal tracciamento avanzata: Strict. Questa modalità blocca:




- Tracciatori intersito
- Cookie di terze parti
- Contenuti di tracciamento noti
- Cryptomining
- Rilevatori di impronte digitali



![LIBREWOLF](assets/fr/05.webp)


*Pagina della scheda Sicurezza e privacy che mostra le impostazioni di sicurezza di LibreWolf.*



WebRTC è disattivato (per evitare fughe di dati IP) e la Protezione totale dei cookie è attiva. La telemetria e i sondaggi di Firefox sono completamente disattivati.



### Gestione dei cookie e della cronologia



Per impostazione predefinita, LibreWolf cancella i cookie e la memoria locale a ogni chiusura. Se questo comportamento vi infastidisce, potete modificarlo in Privacy e sicurezza → Cookie e dati del sito deselezionando "Elimina cookie e dati del sito alla chiusura di LibreWolf".



![LIBREWOLF](assets/fr/06.webp)


*La stessa pagina un po' più in basso, che mostra l'opzione per cancellare i cookie quando il browser è chiuso*



### Aggiunta di estensioni utili



In linea di principio, LibreWolf scoraggia l'aggiunta di estensioni non necessarie, poiché ogni estensione può essere un vettore di tracciamento. Tuttavia, alcune estensioni affidabili possono migliorare la vostra esperienza:




- Firefox Multi-Account Containers** (di Mozilla) per la navigazione a compartimenti stagni
- Decentraleyes** o **LocalCDN** per servire localmente le librerie comuni



Evitate soprattutto le estensioni "VPN gratuite" o i proxy di dubbia qualità: uBlock Origin copre già il 99% delle vostre esigenze.



## Uso quotidiano



### Navigazione quotidiana sul web


Utilizzate LibreWolf per le vostre attività quotidiane su Internet. La differenza principale rispetto agli altri browser è che si lasciano molte meno tracce pubblicitarie. I banner di "accettazione dei cookie" scompaiono su molti siti, grazie agli elenchi di filtraggio di uBlock.



### Utilizzare le schede private per compartimentare


Anche se LibreWolf cancella tutto al termine della sessione, può essere utile aprire una finestra privata del browser (Ctrl+Maiusc+P) per alcune attività durante la sessione, al fine di separare un'identità specifica.



### Sfruttare i contenitori multi-account


L'installazione dell'estensione Multi-Account Containers può aiutarvi a segmentare le vostre attività in silos a tenuta stagna. Ad esempio, è possibile definire un contenitore "Banking" per i siti bancari, un contenitore "Social Networks" per Facebook/Twitter, ecc. Ogni contenitore ha i suoi cookie, le sue sessioni e la sua memoria isolata. Ogni contenitore ha i suoi cookie, le sue sessioni e la sua memoria isolata.



### Gestione dei permessi ottimizzata per sito


LibreWolf consente di controllare le autorizzazioni concesse ai siti (posizione, fotocamera, microfono, notifiche) caso per caso. Concedete le autorizzazioni solo ai siti di cui vi fidate e dove necessario.



## Le migliori pratiche con LibreWolf



1. **Mantenere LibreWolf aggiornato:** Controllare regolarmente il sito per le nuove versioni, soprattutto dopo il rilascio di Firefox stabile.



2. **Evitare di mescolare identità personale e navigazione privata:** idealmente, non si dovrebbe accedere con i propri account personali nella stessa sessione in cui si sta effettuando una ricerca sensibile.



3. **Non sovraccaricare LibreWolf con estensioni superflue:** ogni estensione installata può introdurre rischi di sicurezza o di fingerprinting.



4. **Utilizzare una VPN o un proxy Tor in aggiunta:** LibreWolf non rende anonimi nei confronti del proprio ISP. Per l'anonimato di rete, è possibile utilizzare LibreWolf dietro una VPN affidabile.



5. **Salvate i vostri dati importanti:** segnalibri, password se memorizzati localmente. Considerate un gestore di password esterno (KeePassXC, Bitwarden) piuttosto che il gestore di password di base del browser.



## Confronto con altri browser



LibreWolf fa parte della "cassetta degli attrezzi" dei browser orientati alla privacy:



**LibreWolf vs. Firefox:** LibreWolf arriva già protetto e senza telemetria. Firefox conserva il vantaggio della sincronizzazione su più dispositivi e una base di utenti molto ampia, ma richiede una configurazione manuale per raggiungere il livello di riservatezza di LibreWolf.



**Brave utilizza il codice di Chrome/Chromium e integra un modello di business attraverso un programma pubblicitario opzionale. LibreWolf, essendo un Fork comunitario per Firefox, mantiene l'ecosistema libero di Mozilla e non ha legami con Google.



**LibreWolf vs Tor Browser:** Tor Browser è insostituibile per l'anonimato di fronte a una potente sorveglianza, ma è lento e scomodo nell'uso quotidiano. LibreWolf, per la navigazione quotidiana sul web classico, è molto più veloce e pratico.



**LibreWolf vs Mullvad Browser:** Mullvad Browser si spinge ancora più avanti nella standardizzazione, ma al costo di una ridotta usabilità (impossibile mantenere un cookie di login). LibreWolf raggiunge un equilibrio: molto privato, ma utilizzabile quotidianamente.



## Conclusione



LibreWolf rappresenta un'ottima soluzione per chi cerca un browser ultra-privato "per tutti i giorni" senza spingersi fino all'estremo anonimato di Tor. È la scelta ideale per attivisti, giornalisti, sviluppatori o power user che desiderano una navigazione web classica (veloce, compatibile con i siti moderni) sfuggendo al tracciamento degli annunci e alle Big Tech.



Sebbene presenti alcune limitazioni (assenza di aggiornamenti automatici, compatibilità ridotta con alcuni servizi), LibreWolf è uno strumento prezioso nell'arsenale di chiunque desideri riprendere il controllo della propria privacy digitale. La sua facilità d'uso e la configurazione predefinita lo rendono una scelta saggia per gli utenti attenti alla privacy.



## Risorse



### Documentazione ufficiale




- [Sito ufficiale di LibreWolf](https://librewolf.net)
- [Codice sorgente su Codeberg](https://codeberg.org/librewolf)
- [FAQ ufficiali](https://librewolf.net/docs/faq)



### Guide e confronti




- [Guide alla privacy](https://www.privacyguides.org/en/desktop-browsers/)
- [Test comparativi sulla privacy](https://privacytests.org)



### Sostegno della comunità




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)
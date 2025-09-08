---
name: Scala della coda
description: Esercitazione avanzata di Tailscale
---
![cover](assets/cover.webp)



## 1. Introduzione



Tailscale è una VPN di nuova generazione che crea una rete mesh crittografata tra i vostri dispositivi. Consente di connettere i computer remoti come se fossero sulla stessa rete locale, senza complesse configurazioni o aperture di porte.



Per il self-hosting, Tailscale assegna a ogni dispositivo un IP privato fisso in una rete virtuale, offrendo un accesso stabile ai vostri servizi anche quando il vostro IP pubblico cambia. Ciò significa che potete gestire i vostri server da remoto, senza esporre i vostri servizi direttamente a Internet.



**Applicazioni principali:**




- Gestire un server personale dall'esterno
- Gestire i nodi Umbrel/Lightning più velocemente di Tor
- Accesso sicuro a un Raspberry Pi o a un NAS
- Connettetevi ai vostri servizi tramite SSH o HTTP senza complesse configurazioni di rete



Questo approccio incentrato sulla semplicità consente ai self-hoster di accedere ai propri servizi in modo sicuro, evitando le insidie delle VPN tradizionali.



## 2. Come funziona Tailscale



A differenza delle VPN tradizionali, che instradano tutto il traffico attraverso un server centrale, Tailscale crea una rete mesh in cui i dispositivi comunicano direttamente tra loro. Il server centrale gestisce solo l'autenticazione e la distribuzione delle chiavi, senza vedere i dati degli utenti.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Figura 1: VPN tradizionale con architettura hub-and-spoke in cui tutto il traffico passa attraverso un server centrale*



Sulla base di WireGuard, ogni dispositivo genera le proprie chiavi crittografiche. Il server di coordinamento distribuisce le chiavi pubbliche ai nodi, che poi stabiliscono direttamente tra loro dei tunnel crittografati end-to-end. Per superare i firewall, Tailscale utilizza il NAT traversal e, come ultima risorsa, i relay DERP che mantengono la crittografia.



![VPN maillé (mesh)](assets/fr/02.webp)


*Figura 2: Rete mesh Tailscale in cui i dispositivi comunicano direttamente tra loro*



Tutte le comunicazioni sono criptate con WireGuard. Tailscale vede solo i metadati (connessioni), ma non il contenuto degli scambi. Per una maggiore sovranità, Headscale consente al server di coordinamento di essere self-hosted.



**Sicurezza e riservatezza:** Grazie a WireGuard, tutte le comunicazioni su Tailscale sono crittografate end-to-end. Tailscale non può leggere il vostro traffico: solo i vostri dispositivi dispongono delle chiavi private necessarie. Il servizio vede solo i metadati: Indirizzi IP, nomi dei dispositivi, timestamp delle connessioni e log delle connessioni peer-to-peer (senza contenuti).



Tuttavia, questa architettura dipende da Tailscale Inc. per il coordinamento della rete. Per eliminare questa dipendenza, Headscale offre un'alternativa open-source che consente di ospitare autonomamente il server di controllo e di utilizzare i client ufficiali di Tailscale, garantendo così la completa sovranità sulla propria infrastruttura di rete, a costo di una configurazione più tecnica.



**Per una spiegazione dettagliata del funzionamento interno di Tailscale, compresa la gestione del piano di controllo, l'attraversamento NAT e i relè DERP, consigliamo l'eccellente articolo [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) sul blog ufficiale. Questo articolo spiega in modo approfondito i concetti tecnici che rendono Tailscale così potente.



## 3. Installazione di Tailscale



Tailscale funziona sui **più comuni** sistemi operativi (Windows, macOS, Linux, iOS, Android). Si dice che l'installazione sia "facile e veloce" su tutte le piattaforme. Iniziamo a dare un'occhiata a Interface e a come creare un account, quindi passiamo alle procedure di installazione per i diversi ambienti.



### 3.1 Creazione di un account Tailscale



Andate su [https://tailscale.com/](https://tailscale.com/) e fate clic sul pulsante "Inizia" in alto a destra della pagina.




![Page d'accueil Tailscale](assets/fr/03.webp)


*La home page di Tailscale spiega il concetto e offre un avvio gratuito*



Per utilizzare Tailscale, è necessario creare un account tramite un provider di identità:



![Page de connexion Tailscale](assets/fr/04.webp)


*Scelta del fornitore di identità da collegare a Tailscale (Google, Microsoft, GitHub, Apple, ecc.)*



Dopo aver effettuato l'accesso, Tailscale vi chiederà alcune informazioni sull'uso che intendete farne:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Modulo per comprendere meglio il vostro caso d'uso (personale o professionale)*



Una volta creato il vostro account, potete installare Tailscale sui vostri dispositivi:



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale consente di installare l'applicazione su diversi sistemi*



### 3.2 Installazione su diverse piattaforme





- Su Windows e macOS:** È sufficiente scaricare l'applicazione grafica dal sito ufficiale di Tailscale e installarla (file .msi su Windows, .dmg su Mac). Una volta installata, l'applicazione lancia un Interface grafico che consente di collegarsi (tramite browser) al proprio account Tailscale per autenticare la macchina.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Collegare un MacBook alla rete di coda*



![Connexion réussie](assets/fr/09.webp)


*Conferma che il dispositivo è collegato alla rete Tailscale*





- Su Linux (Debian, Ubuntu, ecc.):** Avete diverse opzioni. Il metodo più semplice è quello di eseguire lo script di installazione ufficiale: ad esempio, su Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Questo script aggiungerà il repository ufficiale di Tailscale e installerà il pacchetto. È anche possibile [aggiungere manualmente il repository APT](https://pkgs.tailscale.com) o usare i normali pacchetti Snap o apt. Una volta installato, daemon `tailscaled` verrà eseguito in background. Sarà quindi necessario **autenticare il nodo** (vedere Interface CLI vs web più avanti). Su altre distribuzioni (Fedora, Arch...), il pacchetto è disponibile anche tramite i repository standard o lo script di installazione universale. Per un server headless, usare CLI: per esempio `sudo tailscale up --auth-key <key>` se si usa una chiave di autenticazione pre-generata, o semplicemente `tailscale up` per un login interattivo (che fornirà un URL da visitare per autenticare il dispositivo).





- Sui sistemi basati su ARM (Raspberry Pi, ecc.):** Generalmente siamo su Linux, quindi lo stesso approccio di cui sopra (script o pacchetto). Si noti che Tailscale supporta senza problemi l'architettura ARM32/ARM64. Molti utenti installano Tailscale su Raspberry Pi OS tramite apt o su distribuzioni leggere (DietPi, ecc.) per accedere al proprio Pi ovunque.





- Su iOS e Android:** Tailscale fornisce applicazioni mobili **ufficiali**. È sufficiente installare *Tailscale* dall'[App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) o dal [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Come installare Tailscale su iPhone: benvenuto, privacy, notifiche, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Connettersi a tailnet, selezionare l'account e convalidarlo sull'iPhone*



Una volta installata l'app, al primo avvio vi chiederà di autenticarvi tramite il provider scelto (Google, Apple ID, Microsoft, ecc., a seconda di quello che state usando per Tailscale) - è la stessa procedura delle altre piattaforme, di solito un reindirizzamento a una pagina web OAuth. Successivamente, l'app mobile crea la VPN (su iOS è necessario accettare il componente aggiuntivo di configurazione della VPN). L'app può quindi essere eseguita in background, consentendovi di accedere alla vostra tailnet da qualsiasi luogo. *Nota bene:* su mobile, è possibile avere solo **una VPN attiva alla volta** - quindi assicuratevi di non avere un'altra VPN connessa allo stesso tempo, altrimenti Tailscale non sarà in grado di stabilire la propria. Su Android, è possibile impostare un profilo di lavoro separato se si desidera isolare determinati usi (ad esempio, un profilo con Tailscale attivo per una determinata app).



### 3.3 Aggiunta di più dispositivi e convalida



Una volta collegato il primo dispositivo, Tailscale chiede di aggiungere altri dispositivi alla rete:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface mostra il primo dispositivo collegato e in attesa di altri dispositivi*



Una volta aggiunti diversi dispositivi, è possibile verificare che possano comunicare tra loro:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Conferma che i dispositivi possono comunicare tra loro tramite ping*



Tailscale suggerisce quindi ulteriori configurazioni per migliorare la vostra esperienza:



![Suggestions de configuration](assets/fr/14.webp)


*Suggerimenti per l'impostazione del DNS, la condivisione dei dispositivi e la gestione degli accessi*



### 3.4 Cruscotto di amministrazione



La console di amministrazione web consente di visualizzare e gestire tutti i dispositivi collegati:



![Tableau de bord des machines](assets/fr/15.webp)


*Elenco dei dispositivi collegati con le loro caratteristiche e il loro stato*



**Interface Web vs Interface CLI:** Tailscale offre due modi complementari di interagire con la rete: il **Interface web administration** e il **command-line client (CLI)**.





- Interface Web (Admin Console)**: accessibile all'indirizzo [https://login.tailscale.com](https://login.tailscale.com), questa console web è il cruscotto centrale della vostra rete Tailscale. Elenca tutti i dispositivi (*macchine*), il loro stato online/offline, i loro indirizzi IP Tailscale e altro ancora. Qui è possibile **gestire i dispositivi** (rinominare, far scadere le chiavi, autorizzare i percorsi, disabilitare un nodo), **gestire gli utenti** (in un contesto organizzativo) e definire le regole di sicurezza (ACL). Qui si configurano anche opzioni globali come MagicDNS, tag o chiavi di autenticazione (chiavi di autenticazione precedenti al generate per l'aggiunta automatica di dispositivi). Interface web è molto utile per avere una visione d'insieme e applicare le modifiche che verranno propagate a tutti i nodi tramite il server di coordinamento. *Esempio:* L'attivazione di una **rete di sottorete** o di un **nodo di uscita** si effettua con un solo clic nella console, una volta che il nodo in questione si è annunciato come tale.





- Linea di comando Interface (CLI):** Il comando `tailscale` è disponibile in CLI su ogni dispositivo in cui è installato Tailscale. Questo CLI permette di fare tutto localmente: connettersi (`tailscale up`), ispezionare lo stato (`tailscale status` per vedere quali peer sono connessi), eseguire il debug (`tailscale ping <ip>`) e così via. Alcune funzioni sono addirittura **esclusive di CLI** o più avanzate, ad esempio:





  - `tailscale up --advertise-routes=192.168.0.0/24` per pubblicizzare una rotta di sottorete,
  - `tailscale up --advertise-exit-node` per proporre la propria macchina come nodo di uscita,
  - `tailscale set --accept-routes=true` (o `--exit-node=<IP>`) per consumare una rotta o usare un nodo di uscita,
  - `tailscale ip -4` per visualizzare il Tailscale IP del dispositivo,
  - blocco/sblocco della coda (se si usa *tailnet-lock*, funzione di sicurezza avanzata),
  - o `tailscale file send <node>` per usare **Taildrop** (trasferimento di file tra dispositivi).


Il CLI è molto utile sui server senza grafica Interface e per lo scripting di alcune azioni. **Differenze d'uso:** La maggior parte delle configurazioni di base può essere effettuata sia tramite il Web che tramite il CLI. Ad esempio, l'aggiunta di un dispositivo può essere fatta o tramite un prompt dalla console, o eseguendo `tailscale up` sul dispositivo e convalidando via web. Allo stesso modo, la ridenominazione di un dispositivo può essere effettuata tramite la console o con `tailscale set --hostname`. **Riassumendo**, la console web è ideale per l'amministrazione globale della rete (specialmente con più macchine/utenti), mentre il CLI è utile per il controllo a grana fine di una determinata macchina, per gli script di automazione o per l'uso su un sistema senza interfaccia grafica.



## 4. Utilizzo di Tailscale su Umbrel



Umbrel è una popolare piattaforma di self-hosting (utilizzata in particolare per i nodi Bitcoin/Lightning e altri servizi self-hosted, tramite il suo App Store). Per installare e configurare Umbrel, vi consigliamo di seguire il nostro tutorial dedicato:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

L'utilizzo congiunto di Umbrel e Tailscale è un caso d'uso particolarmente interessante, poiché Umbrel integra in modo nativo un modulo Tailscale facile da implementare. Ecco come Tailscale si integra con Umbrel e quali sono i suoi vantaggi:



### 4.1 Installazione e configurazione dell'ombrello





- Installazione di Tailscale su Umbrel:** Umbrel ha un'applicazione ufficiale di Tailscale nel suo App Store. L'installazione non potrebbe essere più semplice:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Pagina dell'applicazione Tailscale nell'Umbrel App Store*



Dall'Umbrel Web Interface, aprire l'App Store, cercare **Tailscale** e fare clic su *Install*. Pochi secondi dopo, l'applicazione viene installata sull'Umbrel. Quando la si apre, Umbrel visualizza una pagina che consente di collegare il nodo a Tailscale.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Schermata di connessione della coda in Interface* di Umbrel



Basta **cliccare su "Log in "**, che vi reindirizzerà alla pagina di autenticazione di Tailscale:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Connettersi a Tailscale tramite un provider di identità*



È possibile autenticarsi tramite il proprio account Tailscale (Google/GitHub/ecc.) o inserire la propria e-mail. In genere, su Umbrel, Interface chiede di visitare [https://login.tailscale.com](https://login.tailscale.com) e di effettuare l'accesso: in questo modo si autentica l'applicazione Umbrel Tailscale.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Conferma che il dispositivo Umbrel è collegato alla rete Tailscale*



Una volta fatto, il vostro Umbrel è "nella" rete Tailscale e appare sulla vostra console con un nome (ad esempio *umbrel*). È quindi possibile fare clic sull'IP Address dei dispositivi per copiarlo, recuperare l'IPv6 Address o il MagicDNS associato al dispositivo.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*La console di amministrazione di Tailscale mostra diversi dispositivi collegati, tra cui Umbrel*




### 4.2 Accesso remoto ai servizi Umbrel



Una volta che Umbrel è connesso a Tailscale, **si può accedere a Interface Umbrel e alle applicazioni in esecuzione su di esso, da qualsiasi luogo, come se si fosse sulla rete locale**. Questo è uno dei principali vantaggi rispetto a Tor.



L'accesso è straordinariamente semplice: invece di usare `umbrel.local` (che funziona solo sulla rete locale), si usa l'IP Tailscale Address di Umbrel (`http://100.x.y.z`) direttamente da qualsiasi dispositivo connesso alla tailnet. Questo funziona indipendentemente dal luogo in cui ci si trova o dalla connessione internet utilizzata (4G, Wi-Fi pubblico, rete aziendale).



**Esempi di applicazioni ospitate da Umbrel e accessibili tramite Tailscale:**





- Interface Umbrel principale**: Accedere al cruscotto di Umbrel digitando semplicemente `http://100.x.y.z` nel browser
- Nodo Bitcoin**: Gestione del nodo Bitcoin senza latenza, visualizzazione della sincronizzazione e delle statistiche
- Nodo Lightning**: Utilizzare ThunderHub, RTL o altre interfacce di gestione Lightning con una risposta immediata
- Mempool**: Visualizza le transazioni Bitcoin e Mempool senza ritardi Tor
- noStrudel**: Accesso ai servizi Nostr ospitati su Umbrel



**Collegare portafogli esterni ai nodi Bitcoin o lightning tramite Tailscale:**



Tailscale consente inoltre ai portafogli Bitcoin e Lightning installati su altri dispositivi di connettersi direttamente al nodo Umbrel:





- Sparrow wallet (Bitcoin)**: Questo Wallet Bitcoin esterno può collegarsi direttamente al server Electrum di Umbrel utilizzando il Address IP di Tailscale:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Configurazione di un server Electrum privato nel Sparrow wallet utilizzando il Tailscale IP Address* di Umbrel



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Elenco degli alias del server Electrum in Sparrow con Umbrel Tailscale IP Address*



Leggete la nostra guida completa alla configurazione del Sparrow wallet con il vostro nodo Bitcoin:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- Zeus (Fulmine)**: Questo Wallet mobile Lightning può connettersi al vostro nodo Lightning su Umbrel. Invece di configurare l'endpoint come `.onion', è sufficiente impostare l'IP Tailscale di Umbrel e la porta API di Lightning. La connessione sarà istantanea rispetto a Tor.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Configurazione di Zeus per la connessione al nodo Lightning tramite l'IP Address di Tailscale*



Per configurare Zeus con il vostro nodo Lightning, consultate il nostro tutorial dettagliato:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Per saperne di più sul Lightning Network e su come funziona su Umbrel, visitate:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Vantaggi rispetto a Tor



Umbrel offre nativamente l'accesso remoto tramite Tor (fornendo indirizzi `.onion' per i suoi servizi web). Sebbene Tor abbia il vantaggio della riservatezza (anonimato) e non richieda alcuna registrazione, molti utenti trovano **Tor lento e instabile** per l'uso quotidiano (pagine caricate lentamente, timeout, ecc.) - *"Umbrel via Tor è così lento "* si lamentano alcuni.



Tailscale offre una connessione generalmente **più veloce e a bassa latenza**, poiché il traffico passa direttamente (o tramite un relay veloce) invece di rimbalzare attraverso 3 nodi Tor. Inoltre, Tailscale offre un'esperienza di "rete locale": vengono utilizzati IP privati e le applicazioni possono essere mappate direttamente (ad esempio, unità di rete SMB su 100.x.y.z).



Detto questo, Tor ha il vantaggio di essere decentralizzato e "out of the box" su Umbrel, mentre Tailscale implica la fiducia in una terza parte (o l'hosting di Headscale). Tor è anche utile per l'accesso senza client (da qualsiasi browser Tor, è possibile consultare l'interfaccia utente di Umbrel, mentre Tailscale richiede il client installato sul dispositivo di accesso).



**Riassumendo**, per un uso interattivo (portafogli Lightning, interfacce web frequenti), Tailscale offre un comfort e una velocità apprezzabili rispetto a Tor, al prezzo di una leggera dipendenza esterna. Molte persone scelgono di utilizzare *entrambi*: Tailscale su base quotidiana e Tor come ripiego o per condividere l'accesso con qualcuno senza invitarlo nella propria VPN.



### 4.4 Sicurezza



Utilizzando Tailscale con Umbrel, si evita di esporre Umbrel a Internet. Il nodo Umbrel è accessibile solo agli altri dispositivi autenticati nella tailnet, riducendo notevolmente la superficie di attacco (nessuna porta aperta agli estranei, nessun rischio di attacco al servizio web via Internet).



Le comunicazioni sono crittografate (WireGuard) in aggiunta a qualsiasi crittografia che i vostri servizi stanno già effettuando (ad esempio, anche l'HTTP interno è nel tunnel). È ancora possibile applicare ACL Tailscale per impedire, ad esempio, a un particolare dispositivo tailnet di accedere a Umbrel, se si desidera suddividere la rete. Umbrel stesso non vede la differenza: pensa di servire la rete locale.



---

Per concludere questa sezione, l'integrazione di Tailscale su Umbrel richiede solo pochi clic e **migliora notevolmente l'accessibilità** del vostro nodo self-hosted. Sarete in grado di amministrare Umbrel e i suoi servizi da qualsiasi luogo, in modo sicuro ed efficiente, proprio come se foste a casa vostra. Si tratta di una soluzione particolarmente utile per le applicazioni in tempo reale (Lightning) che soffrono della latenza di Tor, o più in generale per qualsiasi self-host in cerca di una semplice connessione privata. Il tutto senza esporre una sola porta** sul vostro computer e senza complicate configurazioni di rete.



## 5. Gestione avanzata e casi d'uso



### 5.1 Caratteristiche avanzate di Tailscale



**Gestione della rete:** La console di amministrazione (login.tailscale.com) consente di gestire i dispositivi, visualizzare le connessioni e configurare le regole di accesso.



**MagicDNS:** Risolve automaticamente i nomi dei dispositivi (ad esempio `raspberrypi.tailnet.ts.net`) per evitare di memorizzare gli indirizzi IP.



**Definire con precisione chi può accedere a cosa nella rete tramite regole JSON, ideali per isolare determinati dispositivi o limitare l'accesso a servizi specifici.



**La condivisione dei dispositivi consente di invitare qualcuno ad accedere a un computer specifico senza dargli accesso all'intera rete.



**Router di subnet:** Una macchina Tailscale può fungere da gateway per un'intera subnet, consentendo l'accesso a dispositivi non Tailscale (IoT, stampanti, ecc.) tramite una singola macchina configurata.



**Nodo di uscita:** Utilizza una macchina come gateway Internet per uscire con il suo IP. Utile per il Wi-Fi pubblico o per aggirare le restrizioni geografiche.



**Taildrop:** Un'alternativa sicura ad AirDrop, che consente di trasferire file tra i dispositivi Tailscale, indipendentemente dalla piattaforma o dalla posizione. A differenza di AirDrop, che è limitato all'ecosistema Apple e alla vicinanza fisica, Taildrop funziona tra tutti i vostri dispositivi (Windows, Mac, Linux, Android, iOS), anche se si trovano in paesi diversi. I file vengono trasferiti direttamente tra i dispositivi con crittografia end-to-end, senza passare per un server centrale. A seconda del sistema, è possibile utilizzare la riga di comando `tailscale file cp` oppure l'applicazione grafica Interface.



### 5.2 Confronto con altre soluzioni



**Tailscale è molto più semplice da configurare (nessuna porta da aprire, nessuna gestione dei certificati) ma comporta la dipendenza da un servizio di terze parti. OpenVPN è completamente controllabile, ma richiede maggiori competenze.



**Come concorrente diretto, ZeroTier opera a Layer 2 (Ethernet), consentendo il broadcast/multicast, mentre Tailscale opera a Layer 3 (IP). ZeroTier offre una maggiore flessibilità di rete, mentre Tailscale privilegia la semplicità d'uso.



**Tor offre l'anonimato che Tailscale non offre, ma è molto più lento. Tor è decentralizzato e non richiede un account, mentre Tailscale è più veloce e offre un'esperienza simile a una LAN.



**Tailscale automatizza tutta la gestione delle chiavi e delle connessioni che WireGuard raw richiede di gestire manualmente. È essenzialmente WireGuard + una gestione semplificata Layer.



In conclusione, Tailscale si posiziona come una soluzione moderna e orientata alla semplicità, ideale per l'uso personale e per i piccoli team. Per i puristi del controllo totale, Headscale offre un'alternativa di self-hosting.



## 6. Conclusione



**Vantaggi di Tailscale:** Tailscale offre diversi vantaggi per il self-hosting:





- Semplicità e prestazioni** - Installazione rapida su tutte le piattaforme senza configurazione di rete complessa. Il traffico segue il percorso più diretto tra le macchine (P2P mesh), con le prestazioni del protocollo WireGuard e nessun server centrale a limitare il throughput.
- Sicurezza e flessibilità** - Crittografia end-to-end, superficie di attacco ridotta e funzionalità avanzate (ACL, autenticazione SSO/MFA). Funziona anche dietro i NAT o in movimento, con router di sottorete e nodi di uscita per adattare la rete alle vostre esigenze.



**Limiti:** Tenere presente anche:





- Dipendenza esterna** - Nella sua versione standard, il servizio si basa sull'infrastruttura di Tailscale Inc. Questa dipendenza può essere aggirata tramite Headscale (alternativa self-hosting).
- Altri vincoli** - Codice sorgente parzialmente chiuso, limitazioni della versione gratuita per alcuni usi avanzati, nessun supporto per Layer 2 (broadcast/multicast) e necessità di accesso a Internet per stabilire le connessioni.



**Tailscale è ideale per i singoli self-host e i piccoli team, per gli sviluppatori che hanno bisogno di accedere a risorse disperse, per i principianti delle VPN e per gli utenti mobili. Per le aziende che richiedono un controllo totale, possono essere preferibili altre soluzioni come Headscale o WireGuard.



**Esplorate Headscale per l'hosting autonomo completo, le integrazioni API e DevOps (Terraform), o alternative come Innernet (simile ma completamente autonomo) e Netmaker.



Tailscale è uno strumento essenziale per il self-hosting, grazie alla sua semplicità ed efficienza, che rende la vostra infrastruttura privata accessibile come se fosse nel cloud, mantenendo il controllo a casa.



## 7. Risorse utili



### Documentazione ufficiale





- Centro di documentazione Tailscale**: [docs.tailscale.com](https://docs.tailscale.com) - Documentazione completa in inglese, guide all'installazione, esercitazioni e riferimenti tecnici.
- Come funziona Tailscale**: [Come funziona Tailscale](https://tailscale.com/blog/how-tailscale-works) - Articolo dettagliato che spiega il funzionamento interno di Tailscale.
- Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - Monitoraggio degli aggiornamenti e delle nuove funzionalità.



### Guide pratiche





- Tutorial Homelab**: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Guide specifiche per il self-hosting.
- Configurazione di un nodo di uscita**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Guida dettagliata alla configurazione dei nodi di uscita.
- Utilizzare Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Trasferimento di file tra dispositivi Tailscale.



### Confronti





- Tailscale rispetto ad altre soluzioni**: [tailscale.com/compare](https://tailscale.com/compare) - Confronto dettagliato con altre soluzioni VPN e di rete (ZeroTier, OpenVPN, ecc.).



### Comunità





- Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Discussioni, domande e feedback.
- GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Codice sorgente del cliente, dove seguire lo sviluppo e segnalare i problemi.
- Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Comunità di utenti e sviluppatori.



Tailscale fornisce regolarmente nuovi contenuti e funzionalità. Consultate il loro [blog ufficiale](https://tailscale.com/blog/) per le ultime novità e i casi di studio.
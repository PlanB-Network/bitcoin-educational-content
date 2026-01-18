---
name: pfSense
description: Installazione di pfSense
---
![cover](assets/cover.webp)

___

*Questa esercitazione si basa su un contenuto originale di Florian BURNEL pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Sono state apportate importanti modifiche al testo originale dell'autore per aggiornare il tutorial.*

___

![Image](assets/fr/027.webp)


## I. Presentazione

pfSense è un sistema operativo gratuito e open source che trasforma qualsiasi computer, server dedicato o dispositivo hardware in un router e firewall ad alte prestazioni e altamente configurabile. Basato su FreeBSD e rinomato per la sua architettura di rete stabile e robusta, da oltre quindici anni pfSense definisce lo standard dei firewall open source per aziende, enti locali e utenti domestici esigenti.

Le sue funzioni principali si sono evolute notevolmente nel corso degli anni e sono state migliorate con ogni nuova versione. Ad oggi, pfSense offre:
- Amministrazione completa e centralizzata tramite un'interfaccia web moderna, intuitiva e sicura.
- Firewall stateful ad alte prestazioni con supporto NAT avanzato (incluso NAT-T) e gestione granulare delle regole.
- Supporto nativo multi-WAN, che consente l'aggregazione o la ridondanza delle connessioni Internet.
- Server DHCP e relay integrati.
- Alta disponibilità grazie al protocollo CARP per il failover e alla possibilità di configurare cluster pfSense.
- Bilanciamento del carico tra diverse connessioni o server.
- Supporto VPN completo: IPsec, OpenVPN e WireGuard (che sostituisce L2TP, ormai obsoleto).
- Captive portal configurabile per il controllo degli accessi degli ospiti, soprattutto in ambienti pubblici o alberghieri.

pfSense dispone anche di un sistema di pacchetti estensibili che rende facile l'aggiunta di funzionalità avanzate come un proxy trasparente (Squid), il filtraggio degli URL o IDS/IPS (Snort o Suricata) direttamente dall'interfaccia web.

pfSense è distribuito solo per piattaforme a 64 bit, in linea con le attuali raccomandazioni di FreeBSD. Può essere installato su hardware standard (PC, server rack) o su piattaforme embedded a basso consumo come le appliance Netgate o alcuni box x86 a basso profilo, molto più potenti dei vecchi box Alix.

Infine, è bene ricordare che pfSense richiede almeno due interfacce fisiche di rete: una dedicata alla zona esterna (WAN) e una dedicata alla rete interna (LAN). A seconda della complessità dell'infrastruttura (DMZ, VLAN, WAN multiple), potrebbero essere necessarie diverse interfacce aggiuntive per sfruttare appieno le sue capacità.


## II. Scarica l'immagine

L'ultima versione stabile di pfSense, al momento della stesura di questo tutorial, è la 2.8 (rilasciata nel giugno 2025). È possibile scaricare l'immagine ISO o il file di installazione adatto al proprio ambiente hardware direttamente dal sito ufficiale:
- [Scarica pfSense](https://www.pfsense.org/download/)

Il portale di download consente di selezionare:
- Architettura (generalmente **AMD64** per tutti gli hardware moderni).
- Tipo di immagine (**Installer USB Memstick** per l'installazione tramite chiavetta USB, **ISO Installer** per la masterizzazione o la modifica virtuale).
- Il mirror di download più vicino, per ottimizzare la velocità di trasferimento.

Per chi desidera distribuire pfSense in un ambiente virtualizzato (Proxmox, VMware ESXi, VirtualBox...), è disponibile anche un'immagine **OVA**. Questa macchina virtuale pronta all'uso semplifica notevolmente l'installazione e la configurazione iniziale. È sufficiente assicurarsi di regolare le risorse allocate (CPU, RAM, interfacce di rete) in base al carico previsto e alla topologia di rete.

Prima dell'installazione, si consiglia di controllare l'integrità del file scaricato verificando il **SHA256** fornito nella pagina ufficiale di download. Questo assicura che l'immagine non sia stata alterata o corrotta.


## III. Installazione

In questo esempio, l'installazione viene eseguita su una macchina virtuale con VirtualBox. La procedura rimane strettamente identica su una macchina fisica o su qualsiasi altro hypervisor, ad eccezione della gestione dei dispositivi virtuali.

### 1. Requisiti hardware minimi

Per un'installazione standard, si consiglia di utilizzare il formato:
- 1 GB di RAM **minima** (2 GB o più sono consigliati per abilitare pacchetti aggiuntivi o il supporto ZFS).
- 8 GB di spazio su disco (20 GB o più sono preferibili per le configurazioni più avanzate, soprattutto se si installa una cache proxy, IDS/IPS o registri dettagliati).
- Almeno due interfacce di rete virtuali (una per la WAN e una per la LAN). In VirtualBox, aggiungerle alle impostazioni della macchina virtuale prima dell'avvio.

### 2. Avvio dell'installatore

Montare l'immagine ISO scaricata come unità ottica virtuale in VirtualBox o inserire la chiave USB se si sta installando su una macchina fisica. All'avvio, viene visualizzato un menu di avvio:

Se non si seleziona alcuna opzione, pfSense si avvierà automaticamente con le opzioni predefinite dopo pochi secondi. Premere il tasto "**Enter**" per avviare l'avvio normale.

![Image](assets/fr/027.webp)

Quando appare il menu principale, premere rapidamente il pulsante "**I**" per avviare l'installazione.

![Image](assets/fr/001.webp)

### 3. Impostazioni iniziali del programma di installazione

La prima schermata consente di impostare alcuni parametri regionali, come il carattere di visualizzazione e la codifica dei caratteri. Queste impostazioni sono utili in casi specifici (tastiere non standard, schermi seriali, lingue orientali). Per la maggior parte delle installazioni, mantenere i valori predefiniti e selezionare "**Accetta queste impostazioni**".

![Image](assets/fr/002.webp)

### 4. Scelta della modalità di installazione

Selezionate "**Quick/Easy Install**" per eseguire un'installazione automatica con le opzioni consigliate. Questo metodo cancella il disco selezionato e configura pfSense con il partizionamento predefinito.

![Image](assets/fr/003.webp)

Viene visualizzato un avviso che indica che tutti i dati presenti sul disco verranno cancellati. Confermare con "**OK**".

Il programma di installazione copia quindi i file necessari sul disco. A seconda dell'hardware, questa operazione può richiedere da pochi secondi a qualche minuto.

### 5. Selezione del core

Quando il programma di installazione chiede di scegliere il tipo di kernel, lasciare selezionato "**Kernel standard**". Questo kernel generico è perfettamente adatto alle distribuzioni standard, sia su PC che su server o macchine virtuali.

### 6. Fine dell'installazione e riavvio

Una volta completata l'installazione, selezionare "**Riavvia**" per riavviare la macchina sulla nuova istanza pfSense.

**Nota importante**: rimuovere l'immagine ISO o scollegare la chiave USB di installazione prima di riavviare, per evitare di riavviare il programma di installazione al successivo avvio.


## IV. Avvia pfSense per la prima volta

Al primo avvio, pfSense deve essere configurato per riconoscere e assegnare correttamente le sue interfacce di rete (WAN, LAN, DMZ, VLAN, ecc.). Un'attenta identificazione delle schede di rete è essenziale per evitare errori di configurazione che potrebbero privare l'utente dell'accesso all'interfaccia web o rendere il firewall inoperante.

All'avvio, pfSense rileva ed elenca automaticamente tutte le interfacce di rete disponibili, indicando il MAC Address di ciascuna. In questo modo è facile distinguerle.

### 1. VLAN

La prima domanda riguarda la configurazione delle VLAN. In questa fase, per una configurazione di base, non attiveremo alcuna VLAN. Premere quindi il tasto "**N**" per saltare questo passaggio.

![Image](assets/fr/004.webp)

### 2. Assegnazione interfaccia WAN e LAN

pfSense chiede quindi di definire quale interfaccia sarà utilizzata per la WAN (accesso a Internet). È possibile scegliere tra:
- Inserire manualmente il nome dell'interfaccia (consigliato per gli ambienti virtuali).
- Utilizzare il rilevamento automatico premendo "**A**". Questa opzione è utile su un host fisico, a condizione che i cavi di rete siano collegati e i collegamenti attivi.

![Image](assets/fr/005.webp)

In questo esempio, configuriamo manualmente la WAN. Immetti il nome esatto dell'interfaccia. Per una scheda Intel, il nome sarà spesso "**em0**" in FreeBSD, ma può variare a seconda dell'hardware. Ad esempio, una scheda Realtek viene spesso visualizzata come "**re0**".

![Image](assets/fr/006.webp)

Ripeti la stessa operazione per definire l'interfaccia LAN. In questo caso, utilizziamo "**em1**".

pfSense conferma che l'interfaccia LAN attiva sia il firewall che il NAT per proteggere la rete interna e gestire la traduzione dell'indirizzo.

Se si dispone di altre interfacce fisiche, è possibile configurare altre interfacce (DMZ, Wi-Fi, VLAN specifiche) in questa fase. Ogni interfaccia logico richiede una scheda di rete corrispondente o un'interfaccia virtuale. Per la configurazione iniziale, ci limiteremo a WAN e LAN.

Una volta completate le assegnazioni, pfSense visualizza un chiaro riepilogo delle corrispondenze tra le interfacce fisiche e i ruoli assegnati. Confermare con "**Y**".

### 3. Console PfSense

Al termine di questa fase, appare il menu principale della console pfSense. Offre diverse opzioni utili per l'amministrazione diretta, come la reimpostazione della password web, il riavvio, il ricaricamento della configurazione o la riassegnazione delle interfacce.

![Image](assets/fr/007.webp)

Verrà inoltre visualizzato un riepilogo delle impostazioni di rete correnti, compreso l'indirizzo IP predefinito dell'interfaccia LAN, solitamente **192.168.1.1**. Questo è l'indirizzo che si deve inserire nel browser per accedere al sito web di amministrazione dell'interfaccia.

**Nota**: se la rete interna utilizza un intervallo d'indirizzo diverso, selezionare "**2)** Imposta l'interfaccia d'indirizzo IP" nel menu per assegnare un'indirizzo IP adatto al proprio ambiente.

Per impostazione predefinita, se l'interfaccia WAN è collegato a un box o a un modem configurato per il DHCP, pfSense recupera automaticamente un'indirizzp IP pubblico. È quindi possibile beneficiare di un accesso immediato a Internet collegando un client alla LAN dell'interfaccia di pfSense.


## V. Primo accesso all'iterfaccia web

Una volta completato l'avvio iniziale e configura le interfacce di rete, è possibile accedere all'interfaccia web di pfSense per finalizzare e mettere a punto la configurazione.

### 1. Connessione iniziale

Collegare un computer alla porta LAN (o all'interfaccia LAN virtuale nell'hypervisor) e assegnargli un'indirizzo IP nello stesso intervallo, se necessario (per impostazione predefinita, pfSense distribuisce automaticamente un'indirizzo tramite DHCP sulla LAN).

Nel browser, andare all'indirizzo indicato dalla console (per impostazione predefinita `https://192.168.1.1`). Si noti che pfSense richiede l'HTTPS anche per la prima connessione, quindi ci si aspetta un avviso di certificato autofirmato, che si può ignorare aggiungendo un'eccezione.

Viene visualizzata la schermata di accesso. Le credenziali predefinite sono:
- **Nome utente:** `admin`
- **Password:** `pfsense`

Questi identificatori saranno modificati durante la configurazione guidata iniziale.


## VI. Configurazione guidata

Alla prima connessione, pfSense richiede di seguire la sua **Configurazione guidata**. Si consiglia vivamente di utilizzarla per assicurarsi che tutti i parametri essenziali siano definiti correttamente.

### 1. Parametri generali

È possibile:
- Specificare un nome host e un dominio locale (esempio: `pfsense` e `lan.local`)
- Definire i server DNS e scegliere se pfSense deve utilizzare il DNS del proprio ISP o un servizio esterno (Cloudflare, OpenDNS, Quad9...).

### 2. Fuso orario

Indicare il fuso orario del sito in modo che i log e gli orari siano coerenti (ad esempio, `Europa/Parigi`).

### 3. Configurazione WAN

Configurazione della connessione WAN:
- L'impostazione predefinita è **DHCP** (sufficiente se ci si trova dietro un box).
- Se disponi di un IP fisso, inserire manualmente i parametri (IP statico, maschera, gateway, DNS).
- Se necessario, definisci una VLAN o l'autenticazione PPPoE (comune con alcuni ISP).

### 4. Configurazione LAN

La procedura guidata suggerisce di modificare la sottorete LAN predefinita. Se hai un piano di indirizzamento specifico, è il momento di adottarlo.

### 5. Modifica della password dell'amministratore

Proteggi il tuo pfSense impostando immediatamente una password forte per l'utente `admin`.


## VII. Verifica e aggiornamenti

Prima di distribuire il firewall, assicurati di avere l'ultima versione di:
- Vai al **Sistema > Aggiornamento**.
- Seleziona il canale di aggiornamento (di solito **Stabile**).
- Verifica la presenza di aggiornamenti e applicali.

È buona norma attivare le notifiche di aggiornamento per essere informati sulle patch di sicurezza.


## VIII. Salvataggio della configurazione

Prima di apportare modifiche importanti, implementa una politica di backup:
- Vai a **Diagnostica > Backup e ripristino**.
- Scarica una copia della configurazione corrente (`config.xml`).
- Conservalo in un luogo sicuro (supporto esterno crittografato).

Per gli ambienti 'mission-critical', considera il backup automatico della configurazione su un server esterno o tramite uno script programmato.


## IX. Migliori pratiche dopo l'installazione

Per terminare la tua implementazione con la massima tranquillità:
- **Modifica le regole del firewall**: per impostazione predefinita, pfSense consente tutto il traffico in uscita sulla LAN e blocca il traffico in entrata sulla WAN. Imposta queste regole secondo le necessità.
- **Configura l'accesso remoto sicuro**: se necessario, abilita l'accesso al web dell'interfaccia dalla WAN solo tramite VPN o con restrizioni IP.
- **Abilita le notifiche**: configura un server SMTP per ricevere gli avvisi (guasti, aggiornamenti, errori).
- **Installa estensioni utili**: ad esempio, IDS/IPS (Snort, Suricata), proxy (Squid), filtraggio DNS (pfBlockerNG).

Il tuo firewall pfSense è ora attivo e funzionante, pronto a proteggere la tua rete. Grazie alla sua flessibilità e alla comunità attiva, disponi di uno strumento potente e scalabile, in grado di adattarsi alle tue esigenze future (multi-WAN, VLAN, VPN site-to-site, captive portal, ecc.).

Consulta regolarmente la documentazione ufficiale ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) per scoprire nuove funzionalità e assicurati che la tua configurazione sia aggiornata e sicura.

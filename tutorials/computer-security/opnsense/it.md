---
name: OPNsense
description: Come si installa e si configura un firewall OPNsense?
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Florian BURNEL pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale



___



## I. Presentazione



In questa guida daremo un'occhiata al firewall open source OPNsense. Ne esamineremo le caratteristiche principali, i prerequisiti e come installare questa soluzione basata su FreeBSD.



Prima di iniziare, è bene sapere che **OPNsense e pfSense sono entrambi firewall open source** basati su FreeBSD. Possiamo dire che pfSense è una sorta di fratello maggiore di OPNsense, in quanto quest'ultimo è un Fork creato nel 2015. Infine, è importante sottolineare che dal 2017 **OPNsense è passato a HardenedBSD invece che a FreeBSD**. HardenedBSD è una versione migliorata di FreeBSD, con funzioni di sicurezza avanzate



OPNsense si distingue per il suo Interface più moderno e per la **frequenza degli aggiornamenti**. Infatti, il programma di aggiornamento di OPNsense prevede due major release all'anno, che vengono aggiornate ogni due settimane circa (con conseguenti minor release). Questo follow-up è molto interessante rispetto a pfSense, se guardiamo alle versioni comunitarie di queste soluzioni.



![Image](assets/fr/050.webp)



## II. Caratteristiche di OPNsense



OPNsense è un sistema operativo progettato per agire come firewall e router, anche se le sue funzionalità sono numerose e possono essere estese installando pacchetti aggiuntivi. Adatto all'uso in produzione, è utilizzato principalmente per la sicurezza della rete e la gestione dei flussi.



### A. Caratteristiche principali



Ecco alcune delle caratteristiche principali di OPNsense:





- Firewall e NAT**: OPNsense offre funzionalità avanzate di firewall stateful con filtraggio stateful e funzionalità di traduzione Address della rete (NAT).





- DNS/DHCP**: OPNsense può essere configurato per gestire i servizi DNS e DHCP sulla rete. Può agire come server DHCP, ma può anche essere utilizzato come risolutore DNS per i computer della rete locale. Dnsmasq è integrato di default.





- VPN**: OPNsense supporta diversi protocolli VPN, tra cui IPsec, OpenVPN e WireGuard, consentendo connessioni sicure per l'accesso remoto a postazioni di lavoro mobili o per l'interconnessione di siti.





- Proxy web**: OPNsense include un proxy web per controllare e filtrare l'accesso a Internet. Può essere utilizzato anche per filtrare i contenuti e gestire l'accesso alla rete.





- Gestione della larghezza di banda (QoS)**: OPNsense offre funzioni di gestione della qualità del servizio (QoS) per assegnare priorità al traffico di rete e gestire meglio la larghezza di banda.





- Captive portal**: questa funzione consente di gestire l'accesso degli utenti alla rete tramite una pagina di autenticazione (base locale, voucher, ecc.). È una funzione comunemente utilizzata per le reti Wi-Fi pubbliche.





- IDS/IPS**: OPNsense integra Suricata per offrire funzioni di rilevamento e prevenzione delle intrusioni (IDS/IPS) per proteggere la rete dagli attacchi.





- Alta disponibilità (CARP)**: OPNsense supporta il CARP (*Common Address Redundancy Protocol*) per l'alta disponibilità tra più firewall OPNsense, garantendo che il servizio rimanga attivo anche in caso di guasto hardware.





- Reporting e monitoraggio**: OPNsense fornisce strumenti di reporting e monitoraggio in tempo reale per tracciare le prestazioni della rete (con NetFlow) e individuare potenziali problemi, grazie alla creazione di registri. Sono compresi i grafici. Lo strumento Monit è integrato in OPNsense e consente la supervisione del firewall stesso.



### B. Pacchetti aggiuntivi



Questa è solo una panoramica delle funzionalità offerte da OPNsense. Inoltre, il **catalogo dei pacchetti** accessibile dal Interface di amministrazione di OPNsense consente di **arricchire il firewall con funzionalità aggiuntive**. Queste includono un client ACME, un agente Wazuh, il servizio NTP Chrony e Caddy come reverse proxy.



![Image](assets/fr/051.webp)



## III. Prerequisiti di OPNsense



Prima di tutto, è necessario decidere dove installare OPNsense. Ci sono diverse soluzioni possibili, tra cui l'installazione su :





- Un hypervisor come macchina virtuale, che sia Hyper-V, Proxmox, VMware ESXi, ecc.
- Una macchina come sistema *bare-metal*. Potrebbe essere un mini PC che funge da firewall.



È inoltre possibile acquistare **un apparecchio OPNsense montabile su rack** attraverso il nostro negozio online.



È necessario tenere conto delle risorse hardware necessarie per l'esecuzione di OPNsense. I dettagli sono riportati in [questa pagina di documentazione] (https://docs.opnsense.org/manual/hardware.html).



**Risorse minime e consigliate per la produzione:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Infine, i **requisiti di risorse dipendono soprattutto dal numero di connessioni da gestire**, e quindi dai **requisiti di larghezza di banda**. Inoltre, è necessario **tenere presente i servizi che verranno attivati e utilizzati** (proxy, rilevamento delle intrusioni, ecc.) in quanto possono essere affamati di CPU e/o RAM.



Avrete anche bisogno dell'immagine ISO di installazione di OPNsense, che potete scaricare da [il sito ufficiale](https://opnsense.org/download/). Per l'installazione su una macchina virtuale, selezionate "**dvd**" come tipo di immagine per ottenere un'immagine ISO (e fateci quello che volete...). Per l'installazione tramite una chiave USB avviabile, selezionare l'opzione "**vga**" per ottenere un file "**.img**".



![Image](assets/fr/048.webp)



È inoltre necessario un computer per l'amministrazione e il test di OPNsense.



## IV. Configurazione dell'obiettivo



Il nostro obiettivo è quello di





- Creare una rete virtuale interna (192.168.10.0/24 - LAN)**, che possa accedere a Internet tramite il firewall OPNsense. Per l'uso in produzione, questa potrebbe essere la vostra rete locale, via cavo e/o Wi-Fi.
- Attivare e configurare NAT** in modo che le macchine virtuali della rete virtuale interna possano accedere a Internet
- Attivare e configurare il server DHCP su OPNsense** per distribuire una configurazione IP alle future macchine collegate alla rete virtuale interna
- Configurare il firewall** per consentire solo i flussi in uscita da LAN a WAN in HTTP (80) e HTTPS (443).
- Configurare il firewall** per consentire alla LAN virtuale di utilizzare OPNsense come resolver DNS (53).



Se si utilizza la piattaforma Hyper-V, si otterrà la seguente rappresentazione:



![Image](assets/fr/033.webp)



## V. Installazione del firewall OPNsense



### A. Preparazione della chiave USB avviabile



Il primo passo è preparare il supporto di installazione: **la chiave USB avviabile con OPNsense**. Questa operazione è ovviamente facoltativa se si lavora in un ambiente virtuale, ma in ogni caso è necessario scaricare l'immagine ISO di installazione di OPNsense.



Dopo il download, si ottiene **un archivio contenente un'immagine in formato ".img "**. È possibile **creare una chiavetta USB avviabile** con varie applicazioni, tra cui **balenaEtcher**: ultra-semplice da usare. Inoltre, l'applicazione riconosce l'immagine nell'archivio, quindi non è necessario decomprimerla prima.





- [Scarica balenaEtcher](https://etcher.balena.io/)



Una volta installata l'applicazione, selezionare l'immagine, la chiave USB e fare clic su "Flash! Attendere un momento.



![Image](assets/fr/049.webp)



Ora siete pronti per l'installazione.



### B. Installazione del sistema OPNsense



Avviare la macchina che ospita OPNsense. Dovrebbe apparire una pagina di benvenuto simile a quella qui sotto. Per qualche secondo, la schermata mostrata sarà visibile nella finestra. Lasciate che il processo faccia il suo corso...



![Image](assets/fr/019.webp)



L'immagine OPNsense viene caricata sulla macchina, in modo da poter accedere al sistema in modalità "**live**", cioè temporaneamente memorizzata.



![Image](assets/fr/025.webp)



Si arriverà quindi a un Interface simile a quello qui sotto. Accedere con il login "**installer**" e la password "**opnsense**". Si noti che la tastiera è **QWERTY** al momento. A questo punto, **inizieremo il processo di installazione di OPNsense**.



![Image](assets/fr/026.webp)



Sullo schermo appare una nuova procedura guidata. Il primo passo consiste nel selezionare il layout della tastiera corrispondente alla propria configurazione. Per una tastiera AZERTY, selezionare dall'elenco l'opzione "**Francese (tasti accento)**", quindi fare doppio clic su**.



![Image](assets/fr/027.webp)



Il secondo passo consiste nel selezionare l'operazione da eseguire. In questo caso, eseguiremo un'installazione utilizzando il file system **ZFS**. Posizionarsi sulla riga "**Installazione (ZFS)**" e confermare con **Invio**.



![Image](assets/fr/028.webp)



Nel terzo passaggio, selezionare "**stripe**" poiché la nostra macchina è dotata di **un solo disco**: non c'è ridondanza possibile per proteggere lo storage del firewall e i suoi dati. Questo è particolarmente importante quando si installa su una macchina fisica per proteggere da un guasto hardware di un disco, tramite il principio RAID.



![Image](assets/fr/029.webp)



Nel quarto passaggio, è sufficiente premere **Invio** per confermare.



![Image](assets/fr/030.webp)



Infine, confermare selezionando "**Sì**" e premendo il tasto **Invio**.



![Image](assets/fr/031.webp)



Ora dovrete aspettare che OPNsense venga installato... Questo processo richiede circa 5 minuti.



![Image](assets/fr/032.webp)



Una volta completata l'installazione, è possibile modificare la password "**root**" prima del riavvio. Selezionare "**Password di root**", premere **Invio** e inserire due volte la password "**root**".



![Image](assets/fr/020.webp)



Infine, selezionare "**Completa installazione**" e premere **Invio**. Cogliete l'occasione per **espellere il disco dall'unità DVD della macchina virtuale**. Nelle impostazioni della macchina virtuale è possibile impostare il primo avvio su disco.



![Image](assets/fr/021.webp)



La macchina virtuale si riavvierà e caricherà il sistema OPNsense dal disco, dato che lo abbiamo appena installato. Accedere con l'account "root" nella console e la nuova password (altrimenti la password predefinita è "**opnsense**").



### D. Collegamento delle interfacce di rete



Apparirà la schermata mostrata di seguito. Selezionare "**1**" e premere **Invio** per associare le schede di rete della macchina alle interfacce OPNsense.



![Image](assets/fr/022.webp)



Per prima cosa, la procedura guidata chiede di configurare l'aggregazione dei collegamenti e le VLAN. Specificare "**n**" per rifiutare e convalidare ogni volta la risposta con **Invio**. Successivamente, è necessario assegnare le due interfacce "**hn0**" e "**hn1**" alla **WAN** e alla **LAN**. In linea di massima, "**hn0**" corrisponde alla WAN e l'altra Interface alla LAN.



Ecco come funziona:



![Image](assets/fr/023.webp)



Ora abbiamo :





- La **LAN** Interface associata alla scheda di rete "**hn1**" e all'IP predefinito di OPNsense Address, cioè **192.168.1.1/24**.
- Il Interface **WAN** associato alla scheda di rete "**hn0**" e con un IP Address recuperato tramite **DHCP** sulla rete locale (grazie al nostro switch virtuale esterno).



Per impostazione predefinita, l'amministrazione di OPNsense Interface è accessibile solo dalla LAN Interface, per ovvie ragioni di sicurezza. È quindi necessario collegarsi alla LAN Interface del firewall per eseguire l'amministrazione. Se ciò non fosse possibile, è possibile amministrare temporaneamente OPNsense dalla WAN. Ciò comporta la disabilitazione della funzione firewall.



Per farlo, passare alla modalità shell tramite l'opzione "**8**" ed eseguire il seguente comando:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Accesso al sistema di gestione OPNsense Interface



È possibile accedere all'amministrazione OPNsense Interface tramite HTTPS, utilizzando l'IP Address della LAN** Interface (o della WAN). Il browser vi porterà a una pagina di accesso. Accedere con l'account "root" e la password selezionati in precedenza.



![Image](assets/fr/034.webp)



Attendere qualche secondo... Verrà richiesto di seguire una procedura guidata per eseguire la configurazione di base. Fare clic su "**Avanti**" per continuare.



![Image](assets/fr/036.webp)



Il primo passo consiste nel definire il nome host, il nome di dominio, scegliere la lingua e definire i server DNS da utilizzare per la risoluzione dei nomi. Mantenendo l'opzione "**Abilita resolver**", il firewall potrà essere utilizzato come resolver DNS, il che sarà utile per le macchine della nostra LAN virtuale.



![Image](assets/fr/037.webp)



Passare alla fase successiva. La procedura guidata offre la possibilità di **definire un server NTP per la sincronizzazione della data e dell'ora**, anche se esistono già dei server configurati di default. Inoltre, è essenziale scegliere il fuso orario corrispondente alla propria posizione geografica (a meno che non si abbiano requisiti particolari).



![Image](assets/fr/038.webp)



Segue una fase importante: **configurare il Interface WAN**. Attualmente è configurato in DHCP e rimarrà in questa modalità di configurazione, a meno che non si desideri impostare un IP statico Address.



![Image](assets/fr/039.webp)



Sempre nella pagina di configurazione della WAN di Interface, è necessario deselezionare l'opzione "**Blocca l'accesso a reti private via WAN**" se la rete sul lato WAN utilizza un indirizzamento privato. È probabile che questo sia il caso di un laboratorio e quindi potrebbe impedire l'accesso a Internet.



![Image](assets/fr/040.webp)



Successivamente, è possibile **definire una password di "root "**, ma questo è facoltativo perché lo abbiamo già fatto.



![Image](assets/fr/041.webp)



Continuare fino alla fine per avviare il ricaricamento della configurazione. Se è necessario continuare a prendere il controllo tramite la WAN, riavviare il comando precedente una volta completato il processo.



![Image](assets/fr/042.webp)



Non c'è altro da fare!



![Image](assets/fr/035.webp)



### E. Configurazione DHCP



Il nostro obiettivo è utilizzare il server DHCP di OPNsense per distribuire gli indirizzi IP sulla LAN virtuale. Per farlo, dobbiamo accedere a questo menu:



```
Services > ISC DHCPv4 > [LAN]
```



**Come si può vedere, il DHCP è già abilitato per impostazione predefinita sulla LAN ** Se non si è interessati a questo servizio, è meglio disabilitarlo. Anche se è già abilitato e vogliamo usarlo, è importante rivedere la sua configurazione.



Se necessario, è possibile modificare l'intervallo di indirizzi IP da distribuire: *da *192.168.10.10** a **192.168.10.245**, a seconda delle impostazioni correnti.



![Image](assets/fr/046.webp)



Si può anche notare che i campi "**Server DNS**", "**Gateway**", "**Nome di dominio**", ecc. sono vuoti per impostazione predefinita. In realtà, esiste un'eredità automatica di alcune opzioni e valori predefiniti per questi vari campi. Ad esempio, per il server DNS, verrà distribuito l'IP Address della LAN Interface, consentendo al firewall OPNsense di essere utilizzato come resolver DNS.



Se necessario, salvare la configurazione dopo aver apportato le modifiche.



![Image](assets/fr/047.webp)



Per testare il server DHCP, è necessario collegare una macchina alla rete LAN del firewall.



Questa macchina deve ottenere un IP Address dal server DHCP di OPNsense e la nostra macchina deve avere accesso alla rete. L'accesso a Internet deve funzionare. Si noti che se si è disattivata la funzione firewall per accedere a OPNsense dalla WAN, si disattiverà il NAT, impedendo l'accesso al Web.



**Nota**: i leasing DHCP attualmente emessi sono visibili dal Interface dell'amministrazione di OPNsense. A tale scopo, accedere al seguente percorso: **Servizi > ISC DHCPv4 > Locazioni**.



![Image](assets/fr/045.webp)



### F. Configurazione di regole NAT e firewall



La buona notizia è che ora possiamo accedere all'amministrazione di OPNsense Interface dalla LAN.



```
https://192.168.1.10
```



Dopo aver effettuato l'accesso a OPNsense, scopriamo la configurazione NAT. Andare in questa posizione: **Firewall > NAT > Outbound**. Qui è possibile scegliere tra la creazione automatica (predefinita) e quella manuale delle regole NAT in uscita.



Scegliete la modalità automatica tramite l'opzione "**Generazione automatica delle regole NAT in uscita**" e cliccate su "**Salva**" (in linea di principio, questa configurazione è già quella attiva). In modalità automatica, OPNsense crea autonomamente una regola NAT per ogni rete.



![Image](assets/fr/043.webp)



Per il momento, tutti i computer collegati alla LAN virtuale "**192.168.10.0/24**" possono accedere a Internet senza restrizioni. Tuttavia, il nostro obiettivo è quello di limitare l'accesso alla WAN ai protocolli HTTP e HTTPS, nonché al DNS sulla LAN Interface del firewall.



Dobbiamo quindi creare le regole del firewall... Sfogliare il menu come segue: **Firewall > Regole > LAN**.



**Per impostazione predefinita, ci sono due regole per autorizzare tutto il traffico LAN in uscita, in IPv4 e IPv6**. Disattivare queste due regole facendo clic sulla freccia Green all'estrema sinistra, all'inizio di ogni riga.



Quindi creare tre nuove regole per autorizzare la **rete LAN** (cioè "**rete LAN**") a :





- accedere a tutte le destinazioni utilizzando **HTTP**.
- accedere a tutte le destinazioni con **HTTPS**.
- richiedere **OPNsense** sul suo **Interface LAN** (cioè "**LAN Address**"), tramite il **protocollo DNS** (questo implica l'utilizzo del firewall come DNS), altrimenti autorizzare il proprio DNS resolver tramite il suo IP Address.



Si ottiene così il seguente risultato:



![Image](assets/fr/044.webp)



Non resta che cliccare su "**Applica modifiche**" per passare le nuove regole del firewall alla produzione. **Si noti che tutti i flussi non esplicitamente autorizzati saranno bloccati per impostazione predefinita



La macchina LAN può accedere a Internet, utilizzando HTTP e HTTPS. Tutti gli altri protocolli saranno bloccati.



![Image](assets/fr/018.webp)



## IV. Conclusione



Seguendo questa guida, potrete installare OPNsense e iniziare subito a lavorare. OPNsense offre un'ampia gamma di funzioni per proteggere e gestire in modo efficiente il traffico di rete ed è adatto all'uso in ambienti professionali.



Questa installazione è solo l'inizio: sentitevi liberi di esplorare i menu e di configurare altre funzioni per adattare OPNsense alle vostre esigenze.
---
name: Le reti IP dalla teoria alla pratica
goal: Imparate a conoscere i fondamenti delle reti IP per configurarle e risolverne i problemi.
objectives: 


  - Comprendere l'architettura e il funzionamento del protocollo TCP/IP
  - Spiegare le differenze, i vantaggi e i vincoli di IPv4 e IPv6
  - Identificare e distinguere tra i diversi tipi di IP Address
  - Configurazione e verifica dell'indirizzamento IP su sistemi Unix/Linux
  - Utilizzare i principali strumenti di diagnostica per analizzare e risolvere i problemi di rete


---

# Competenze essenziali per navigare nel mondo della proprietà intellettuale


Immergetevi nel cuore del mondo IP e dotatevi delle conoscenze necessarie per comprendere e gestire in modo efficiente le vostre reti. In questo corso imparerete tutto quello che c'è da sapere sulle reti di computer in modo chiaro e pratico.


Imparerete come funzionano le reti e l'indirizzamento IP, come distinguere tra IPv4 e IPv6, come identificare e utilizzare le diverse categorie Address e come cogliere tutta l'importanza del protocollo TCP/IP e dei collegamenti che crea tra indirizzi IP, indirizzi fisici e nomi DNS.


NET 302 si rivolge soprattutto a studenti, utenti Linux o semplici curiosi che vogliono comprendere le basi del networking e rafforzare la propria autonomia nella gestione, risoluzione dei problemi e ottimizzazione delle infrastrutture.


Unitevi a noi e trasformate le vostre conoscenze in una reale esperienza operativa!


___


Questo corso NET 302 è un adattamento del corso *Le basi della rete: TCP/IP, IPv4 e IPv6*, scritto in francese da Philippe Pierre e pubblicato su [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), sotto licenza Creative Commons Attribution-NonCommercial 4.0 International ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).



Alla versione originale di Loïc Morel sono state apportate sostanziali modifiche: il testo è stato interamente riscritto, ampliato e arricchito per fornire contenuti aggiornati e approfonditi, pur mantenendo lo spirito didattico dell'opera originale di Philippe Pierre. Anche i diagrammi sono stati rivisti.


+++


# Introduzione


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Panoramica del corso


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Questo corso fornisce un'introduzione completa ai fondamenti delle reti IP. È strutturato in quattro sezioni principali, ognuna delle quali copre un aspetto essenziale per la comprensione, la configurazione e la diagnosi di problemi in una rete di computer.


### Protocollo TCP/IP


In questa prima parte, getteremo le basi esplorando il concetto di rete e la storia del protocollo TCP/IP. Studieremo i suoi componenti principali: IP, TCP e un breve sguardo al protocollo IPv5 QoS. Verranno inoltre trattate le primitive di servizio per comprendere meglio la logica dei dati Exchange.


### Indirizzamento IPv4


Passeremo poi a un modulo dedicato all'indirizzamento IPv4. Imparerete come viene utilizzato in pratica l'IPv4, i suoi diversi tipi Address (privato, pubblico, broadcast, ecc.), il ruolo fondamentale del DNS, nonché il funzionamento degli indirizzi Ethernet e del protocollo ARP. Scoprirete anche il NAT (Network Address Translation) e le basi della configurazione di rete.


### Indirizzamento IPv6


La terza parte si concentra sull'indirizzamento IPv6, necessario per superare le limitazioni dell'IPv4. Ne esamineremo gli standard e le definizioni, il Address Assignment all'interno di una rete locale, la gestione dei blocchi Address e la relazione tra IPv6 e DNS.


### Strumenti di diagnostica di rete


Infine, concluderemo con una presentazione dei principali strumenti di diagnostica di rete. Questi vi permetteranno di analizzare, controllare e risolvere i malfunzionamenti. Questa parte sarà strutturata per livelli: Accesso alla rete, Rete, Trasporto e Livelli superiori.


Al termine di questo corso, avrete le conoscenze fondamentali per amministrare in modo efficiente un'infrastruttura di rete e diagnosticare potenziali problemi.


Siete pronti a tuffarvi nel mondo delle reti informatiche? Andiamo!


**NOTA**: Le descrizioni sono basate su un sistema GNU/Linux CentOS 7. Tuttavia, le configurazioni di rete sono in gran parte le stesse quando si confronta un sistema Debian con uno CentOS. Pertanto, non faremo alcuna distinzione. Quando c'è una distinzione, la prefissiamo con un logo specifico.


**N.B.**: Se durante il corso si incontrano termini non familiari, si prega di consultare [il glossario](https://planb.network/resources/glossary) per le definizioni.



# Protocolli TCP/IP


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Che cos'è una rete?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



In questo primo modulo, daremo uno sguardo approfondito al protocollo TCP/IP, la pietra miliare delle moderne comunicazioni digitali. Parleremo delle sue origini, dei suoi principi fondamentali e del sistema di indirizzamento che utilizza, essenziale per garantire il flusso di informazioni tra i dispositivi connessi.


Descriveremo anche i principali componenti che strutturano questo modello e spiegheremo come interagiscono per formare una rete operativa, affidabile e scalabile. Ma prima è essenziale tornare al concetto di rete.


Etimologicamente, una rete si riferisce a un insieme di punti collegati tra loro, che formano una struttura interconnessa. Nelle telecomunicazioni e nell'informatica, questa definizione si traduce in un gruppo di dispositivi (computer, router, switch, access point, ecc.) in grado di scambiare dati attraverso supporti fisici o wireless. Una rete consente quindi un flusso continuo o intermittente di informazioni, a seconda delle esigenze, dei protocolli in uso e della natura dell'architettura implementata.


Nel corso del tempo sono state sviluppate diverse topologie classiche per soddisfare le diverse esigenze di costo, prestazioni, resilienza e facilità di manutenzione. Queste includono:


- rete ad anello,
- rete di alberi,
- rete di autobus,
- rete di stelle,
- rete mesh.



### Rete ad anello


In una topologia ad anello, i dispositivi sono collegati in un anello chiuso: ogni stazione è collegata alla successiva e l'ultima si collega alla prima. In questa configurazione, ogni dispositivo funge da relè, passando i dati al collegamento successivo. A seconda del tipo di rete, le informazioni possono circolare in una sola direzione o in entrambe.


Il vantaggio di questa disposizione risiede nella semplicità del cablaggio e nell'assenza di dipendenza da un'apparecchiatura centrale. Tuttavia, la continuità dell'intera rete dipende dalla salute di ogni singolo elemento: il guasto di una singola stazione può interrompere l'intero sistema di comunicazione. Per questo motivo vengono spesso introdotti meccanismi di ridondanza o di bypass.



![Image](assets/fr/001.webp)



### Rete di alberi


La rete ad albero, o topologia gerarchica, è modellata sulla struttura di un albero genealogico. È costituita da livelli successivi: un nodo radice in cima si collega a diversi nodi di livello inferiore, che possono a loro volta collegarsi ad altri nodi, e così via.


Questa disposizione gerarchica funziona particolarmente bene per le reti di grandi dimensioni che necessitano di una chiara divisione delle responsabilità e di una gestione segmentata. Tuttavia, rende la rete vulnerabile ai guasti dei nodi di livello superiore: la perdita della radice o di un ramo principale può interrompere intere sezioni dell'infrastruttura.



![Image](assets/fr/002.webp)



### Rete di autobus


In una topologia bus, tutti i dispositivi condividono lo stesso mezzo di trasmissione, in genere una linea coassiale o una fibra ottica. Ogni unità è collegata passivamente, cioè non modifica attivamente il segnale, e può inviare o ricevere dati su questo canale condiviso.


Il principale vantaggio della topologia a bus è il basso costo di installazione, grazie alla semplificazione del cablaggio.  Tuttavia, nelle vecchie implementazioni basate su cavi coassiali (Ethernet 10BASE2/10BASE5), la disconnessione o la perdita di una singola stazione potrebbe interrompere o addirittura bloccare tutto il traffico, poiché la continuità elettrica e l'impedenza di terminazione del bus non verrebbero più mantenute. Il fatto di avere un unico mezzo fisico è anche una debolezza critica: qualsiasi interruzione o guasto interrompe la comunicazione per l'intera rete.



![Image](assets/fr/003.webp)



### Rete di stelle


La topologia a stella, nota anche come "hub and spoke", è la più comune oggi, soprattutto nelle reti Ethernet domestiche e d'ufficio. In questo caso, tutti i dispositivi si collegano a un unico dispositivo centrale.


Questa disposizione facilita la gestione e la manutenzione: se un dispositivo periferico si guasta, il resto della rete non ne risente. Lo svantaggio è che il dispositivo centrale è un singolo punto di guasto: se si guasta, la comunicazione si interrompe ovunque. Anche la qualità dei cavi e la lunghezza dei collegamenti devono essere considerate con attenzione per mantenere buone prestazioni.



![Image](assets/fr/004.webp)



**Nota**: esistono ancora reti organizzate con una topologia lineare, simile a un bus, in cui le apparecchiature sono collegate una dopo l'altra. Questa soluzione, benché poco costosa da implementare, presenta l'inconveniente principale che una singola interruzione isola alcuni host, dividendo la rete in sottoinsiemi indipendenti.


### Rete a maglie


La rete mesh è progettata per garantire la massima ridondanza: ogni dispositivo è collegato direttamente a ogni altro dispositivo. Ciò garantisce la continuità del servizio anche in caso di guasto di più collegamenti o dispositivi, poiché il traffico può essere reindirizzato su percorsi alternativi.


Il compromesso è che il numero di connessioni da stabilire aumenta rapidamente con il numero di terminali. Per `N` punti di connessione, sono necessari `N × (N-1) / 2` collegamenti separati, rendendo questa topologia costosa e complessa da implementare. Per questo motivo viene utilizzata principalmente nelle reti critiche che richiedono una disponibilità molto elevata, come alcune parti di Internet o sistemi industriali sensibili.



![Image](assets/fr/005.webp)



Esistono altre varianti, come le reti a griglia o a ipercubo, progettate per esigenze specifiche di calcolo distribuito o di elaborazione parallela.


Su scala globale, Internet è un'enorme interconnessione di reti che utilizzano topologie diverse, unificate da un indirizzamento comune (IPv4 e IPv6) e da un insieme di protocolli standardizzati definiti dall'IETF (*Internet Engineering Task Force*). Questa diversità fa sì che Internet non segua un'unica topologia: la sua struttura è flessibile, scalabile e indipendente dallo schema di indirizzamento logico che la rende utilizzabile.



## Le origini del TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



Le origini del protocollo TCP risalgono all'**ARPA** (*Advanced Research Projects Agency*, ribattezzata "DARPA" nel 1972), che nel 1966 lanciò il progetto **ARPANET**. Il primo segmento ARPANET entrò in funzione nell'ottobre 1969, collegando le università UCLA e Stanford. L'obiettivo era quello di collegare i centri di ricerca attraverso una rete a commutazione di pacchetto in grado di mantenere le comunicazioni anche in caso di guasto parziale dell'infrastruttura.


Nell'ambito di questa dinamica, l'ARPA finanziò l'Università di Berkeley per integrare i primi protocolli TCP/IP nel suo sistema BSD Unix. Questo ha avuto un ruolo fondamentale nella diffusione e standardizzazione del protocollo, prima nel mondo accademico e poi nell'industria.


**Nota**: a quel tempo, gli informatici non avevano ancora Linux (che sarebbe apparso solo all'inizio degli anni '90), né Minix, il sistema didattico progettato da Andrew Tanenbaum.  Le opzioni principali erano Unix o, a volte, mainframe proprietari come OpenVMS. Grazie alla sua flessibilità e apertura, Unix è stato fondamentale per la diffusione dei primi concetti di rete.


In senso stretto, TCP/IP non è un singolo protocollo, ma una suite di protocolli costruiti attorno a TCP e IP. È salito alla ribalta perché ha fornito una Interface di programmazione standardizzata per lo scambio di dati tra macchine sulla stessa rete. Questo Interface, basato su primitive chiamate "socket", ha permesso di creare connessioni affidabili e flessibili, integrando al contempo protocolli applicativi essenziali.


ARPANET è quindi la base storica dell'attuale Internet. Internet è infatti una rete globale basata sul principio della commutazione di pacchetto, in cui le informazioni circolano utilizzando una serie di protocolli standardizzati che garantiscono la compatibilità e l'interoperabilità tra sistemi eterogenei. Questa architettura aperta ha permesso lo sviluppo e la diffusione di innumerevoli servizi e applicazioni, tra cui:


- e-mail,
- il World Wide Web (www),
- trasferimento e condivisione di file...


La governance e l'evoluzione di questi protocolli sono supervisionate dall'***Internet Architecture Board*** (IAB).

Questa organizzazione coordina le direzioni tecniche attraverso due strutture principali:


- IRTF** (_Internet Research Task Force_), che conduce ricerche a lungo termine sull'evoluzione e il miglioramento dei protocolli.
- IETF** (_Internet Engineering Task Force_), che sviluppa, standardizza e documenta i protocolli operativi utilizzati in Internet


La distribuzione delle risorse di rete (intervalli IP Address, numeri di sistemi autonomi, nomi di dominio radice, ecc.) è coordinata a livello internazionale da **IANA/ICANN**. La gestione operativa si basa su: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Europa, Medio Oriente, Asia Centrale), **ARIN**, **APNIC**, **LACNIC** e **AFRINIC**.


Tutte le specifiche del protocollo TCP/IP sono registrate in documenti chiamati **RFC** (_Request For Comments_), che fungono da riferimenti tecnici autorevoli. Le RFC vengono continuamente aggiornate e numerate per riflettere la continua evoluzione della suite di protocolli.


La pila TCP/IP è spesso rappresentata come una pila di quattro livelli funzionali, spesso paragonata al modello a sette Layer **OSI** (_Open Systems Interconnection_) sviluppato dall'**ISO** (_International Standards Organization_), che serve come riferimento concettuale per il networking.


I quattro livelli del modello TCP/IP sono:


- il Layer di ACCESSO ALLA RETE, che fornisce i protocolli di collegamento fisico e di controllo dell'accesso ai media;
- iNTERNET Layer, che gestisce l'instradamento e l'indirizzamento IP;
- il TRANSPORT Layer, che garantisce l'affidabilità e la gestione dei flussi di dati utilizzando protocolli come TCP o UDP ;
- il Layer APPLICAZIONE, che raggruppa protocolli utente e software come HTTP, FTP, SMTP e DNS.



![Image](assets/fr/006.webp)



Oggi la versione di IP più diffusa è l'IPv4, ma il suo spazio Address a 32 bit presenta evidenti limitazioni. Questo ha portato alla creazione dell'IPv6, che utilizza un indirizzamento a 128 bit e offre una capacità virtualmente illimitata: essenziale per supportare la crescita esplosiva dei dispositivi connessi e affrontare le sfide dell'Internet delle cose, della mobilità e della sicurezza.


Ogni Layer dello stack TCP/IP fornisce servizi specifici, rendendo possibile Address diverse esigenze di rete in modo modulare: trasmissione fisica, indirizzamento logico, integrità dei dati e servizi a livello di applicazione.


| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## Protocollo QoS IPv5


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



L'intestazione di un pacchetto IP è una struttura di dati essenziale, suddivisa in diversi campi, ognuno dei quali ha un ruolo specifico per garantire che i pacchetti vengano trasmessi ed elaborati correttamente durante il viaggio attraverso la rete. Questi campi includono l'IP Address di destinazione (necessario per instradare il pacchetto verso il destinatario), la lunghezza dell'intestazione indicata dal campo IHL (*Internet Header Length*), la lunghezza totale del pacchetto registrata nel campo *Total Length*, informazioni di controllo e verifica e altri parametri per la gestione del flusso e della qualità della comunicazione.


Il primo campo dell'intestazione si chiama Versione. Questo valore di 4 bit specifica quale versione del protocollo IP segue il pacchetto. È importante perché indica a ciascun router o dispositivo intermedio come interpretare e gestire i dati incapsulati.


**Nota**: la gestione e l’assegnazione delle versioni dei protocolli IP rientrano nelle competenze dello **IANA**. Un campo a 4 bit consente 16 combinazioni binarie (valori da 0 a 15). Ad oggi, la loro assegnazione è la seguente:



| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Tra questi c'è l'IPv5 che, sebbene sia in gran parte sconosciuto al pubblico, esisteva come ST (_Stream Protocol_). Sviluppato negli anni '80, l'IPv5 è stato progettato per rispondere a un'esigenza sempre più sentita all'epoca: fornire "qualità del servizio" (QoS) a determinati flussi di dati che richiedevano una trasmissione continua e stabile, come il Voice over IP o i flussi multimediali. L'obiettivo era quello di garantire la larghezza di banda e la priorità end-to-end, un concetto simile a quello che oggi offre l'RSVP (_Resource Reservation Protocol_) per riservare dinamicamente le risorse di rete sui router moderni.


Tuttavia, l'IPv5 è rimasto sperimentale ed è stato implementato solo su un numero limitato di dispositivi di rete. La sua limitata adozione, unita alla rapida crescita della necessità di spazio Address, ha indotto i progettisti di Internet a passare direttamente dall'IPv4 all'IPv6. In questo modo si sono evitati sia i limiti del Address dell'IPv4, sia il rischio di confusione o incompatibilità con le specifiche sperimentali dell'IPv5.


Sebbene l'IPv5 non abbia mai avuto un uso diffuso, ha svolto un ruolo importante nel dare forma alle prime idee sulla QoS e sulla gestione del traffico. Oggi è più un indicatore storico che uno standard operativo.


**Un protocollo è un insieme di regole di comunicazione: strutture di dati, algoritmi, formati di pacchetti e convenzioni che consentono a dispositivi diversi di trasmettere informazioni in modo affidabile e comprensibile. Un servizio è l'implementazione concreta di un protocollo attraverso programmi specifici (client, server) che seguono queste regole e rendono disponibili le funzionalità a utenti e applicazioni.


Possiamo ora esaminare più da vicino la struttura e il funzionamento del protocollo IP, la base essenziale di tutte le comunicazioni di rete.



## Il protocollo IP


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Definizioni e informazioni generali


Il protocollo IP, o "***Internet Protocol***", è la spina dorsale del modello TCP/IP. Trasporta i pacchetti di dati da un host all'altro all'interno di una rete, sia essa locale o mondiale. Ha due ruoli chiave: gestire l'indirizzamento logico dei dispositivi e garantire l'instradamento dei pacchetti su reti spesso eterogenee e interconnesse.


A livello fisico, la trasmissione si basa su interfacce hardware per stabilire connessioni punto-punto tra i nodi. Tuttavia, è il protocollo IP che rende possibile la comunicazione end-to-end, fornendo a ciascun pacchetto le informazioni necessarie per navigare attraverso molteplici percorsi possibili verso la destinazione.


Tre configurazioni di rete Elements determinano il modo in cui un pacchetto viene inviato sul suo percorso:


- IP Address**: identifica in modo univoco l'host di destinazione nella rete.
- Maschera di sottorete**: specifica quale parte del Address identifica la rete e quale l'host, consentendo una divisione logica in sottoreti.
- Il gateway**: indica il router intermedio attraverso il quale il pacchetto deve passare per raggiungere una rete esterna o un altro segmento della rete locale.


Su Internet, i dati non scorrono come un unico flusso continuo, ma vengono inviati come **datagrammi**: blocchi di dati indipendenti, ciascuno incapsulato con tutte le informazioni necessarie per la consegna. Questo è il principio del **packet switching**, in cui le informazioni vengono suddivise in unità autonome che possono seguire percorsi diversi per raggiungere lo stesso destinatario.


Oltre al carico utile (*payload*), ogni datagramma IP contiene un'intestazione strutturata con campi quali il Address di destinazione, il Address di origine, il tipo di servizio, il numero di versione del protocollo e altre informazioni di controllo necessarie per gestire la trasmissione.


La dimensione massima teorica di un datagramma IP è di **65.536 ottetti**, un limite fissato dal campo di lunghezza totale dell'intestazione. In pratica, questa dimensione è raramente raggiunta, poiché le reti fisiche che trasportano i pacchetti (Ethernet, Wi-Fi, fibra ottica...) di solito impongono limiti più severi noti come **MTU** (_Maximum Transmission Unit_). Se un datagramma supera l'MTU del collegamento fisico, deve essere suddiviso in pacchetti più piccoli, ciascuno inviato separatamente e riassemblato all'arrivo.


Questa adattabilità rende l'IP un protocollo robusto e flessibile, in grado di operare su un'ampia varietà di tecnologie sottostanti mantenendo la compatibilità universale tra sistemi e reti eterogenee.



### Frammentazione dei datagrammi IP


Quando un datagramma IP deve attraversare una rete la cui capacità di trasmissione è inferiore al datagramma stesso, deve essere **frammentato** per poter viaggiare senza problemi. Questo limite di dimensione fisica è chiamato **MTU** (Maximum Transmission Unit): la dimensione massima del frame che può passare su una determinata rete senza essere frammentato.


Ogni tecnologia di rete impone la propria MTU, determinata dalle caratteristiche dell'hardware e del protocollo. I valori comuni includono:


- ARPANET**: 1000 byte
- Ethernet**: 1500 byte
- FDDI**: 4470 byte


Quando un datagramma supera l'MTU di un segmento di rete che deve attraversare, le apparecchiature di routing lo dividono in **frammenti** più piccoli che rispettano il limite. Questo accade tipicamente quando si passa da una rete ad alta MTU a una con una capacità inferiore. Ad esempio, un datagramma proveniente da una rete FDDI potrebbe dover essere frammentato prima di essere inviato su un segmento Ethernet.



![Image](assets/fr/008.webp)



Il processo di frammentazione funziona in questo modo:


- Il router spezza il datagramma in frammenti non più grandi dell'MTU della rete di destinazione.
- La dimensione di ogni frammento è un multiplo di 8 byte, poiché il protocollo IP utilizza questa unità per codificare l'offset di riassemblaggio.
- Ogni frammento riceve la propria intestazione IP, che contiene le informazioni necessarie al destinatario finale per riassemblarli nell'ordine corretto.


Una volta frammentati, i pezzi viaggiano indipendentemente attraverso la rete. Possono seguire percorsi diversi, a seconda delle tabelle di routing, del carico dei collegamenti o delle interruzioni. Non è garantito che arrivino nell'ordine in cui sono stati inviati.


All'arrivo, la macchina ricevente si occupa del **riassemblaggio**. Utilizzando le informazioni contenute nelle intestazioni (identificatore condiviso, offset e flag di frammentazione), rimette i frammenti nel giusto ordine per ricostruire il datagramma originale prima di trasmetterlo al Layer successivo. Se anche un solo frammento è perso o corrotto, l'intero datagramma viene solitamente scartato: senza ogni frammento, il risultato sarebbe incompleto o inutilizzabile.


Sebbene efficaci, la frammentazione e il riassemblaggio presentano degli svantaggi: un'elaborazione supplementare per router e host e una maggiore probabilità di perdita di pacchetti, che può aumentare le ritrasmissioni. Ecco perché un'attenta gestione dell'MTU e l'ottimizzazione delle dimensioni dei pacchetti sono importanti per una comunicazione IP fluida ed efficiente.



### Incapsulamento dei dati


Per garantire che i dati vengano instradati correttamente attraverso i livelli del modello TCP/IP, il processo di **incapsulamento** svolge un ruolo fondamentale. In ogni fase del viaggio di un messaggio dall'applicazione del mittente al computer del destinatario, vengono aggiunte informazioni supplementari, note come intestazioni. Queste intestazioni forniscono ai dispositivi intermedi e ai livelli software le istruzioni necessarie per elaborare, consegnare e, se necessario, riassemblare i dati.


Quando un messaggio viene inviato, passa attraverso i quattro livelli dello stack TCP/IP. A ogni Layer, viene aggiunta una nuova intestazione davanti ai dati esistenti: ogni intestazione contiene metadati specifici, come indirizzi logici o fisici, porte di comunicazione, numeri di sequenza, flag di controllo degli errori e qualsiasi informazione necessaria per gestire la trasmissione e l'instradamento.


La trasmissione segue quindi un processo strutturato:


- L'applicazione Layer crea il **messaggio** iniziale, contenente i dati grezzi.
- Il Transport Layer lo incapsula in un **segmento**, aggiungendo porte di origine e di destinazione, numeri di sequenza e meccanismi di controllo del flusso.
- Il Layer di Internet aggiunge al segmento un'intestazione IP per formare un **datagramma**, specificando gli indirizzi IP di origine e di destinazione.
- Il Network Access Layer avvolge il datagramma in un **frame**, aggiungendo gli indirizzi MAC e i codici di controllo dell'integrità (CRC).



![Image](assets/fr/009.webp)



Questo processo di incapsulamento garantisce sia l'integrità e la tracciabilità dei dati, sia la loro adattabilità: nel passaggio da una rete all'altra, le intestazioni forniscono ai dispositivi le informazioni necessarie per scegliere il percorso, verificare la validità o eseguire la frammentazione, se necessario.


All'arrivo, il processo è invertito: la macchina ricevente riceve il frame dal Layer di accesso alla rete, che legge e rimuove l'intestazione corrispondente. Il datagramma viene quindi passato al Layer Internet, che legge l'intestazione IP e la rimuove a sua volta per consegnare il segmento al Layer Trasporto. Il Transport Layer elabora le intestazioni di trasporto, controlla l'integrità del flusso e infine consegna il **messaggio** all'applicazione di destinazione nel suo stato originale.



![Image](assets/fr/010.webp)



La trasformazione dei dati in ogni Layer può essere riassunta come segue:


- Messaggio**: blocco di informazioni al Layer dell'applicazione.
- Segmento**: unità di dati dopo l'incapsulamento da parte del Layer di trasporto.
- Datagramma**: forma assunta dopo l'aggiunta dell'intestazione IP da parte del Layer di Internet.
- Frame**: blocco finale pronto per la trasmissione sul mezzo fisico da parte del Layer di accesso alla rete.



![Image](assets/fr/011.webp)



Questo processo, essenziale per l'affidabilità e l'universalità delle comunicazioni Internet, garantisce che ogni dato, per quanto frammentato o complesso, possa essere trasportato da un capo all'altro rimanendo comprensibile e utilizzabile dalla macchina ricevente.



### Indirizzamento IP


Anche con la commutazione dei pacchetti, la frammentazione e l'incapsulamento, una rete non potrebbe funzionare senza un sistema di indirizzamento affidabile. Per garantire che ogni pacchetto di dati raggiunga il destinatario corretto, il Layer di Internet utilizza un identificatore unico: il **IP Address**.

In IPv4, un Address IP è codificato su **32 bit** e scritto come quattro numeri decimali separati da punti, nel noto formato N1.N2.N3.N4 (ad esempio: 192.168.1.12).


Un IP Address è composto da due parti:


- _netid_**: identifica la rete a cui l'host appartiene
- _hostid_**: identifica l'host specifico all'interno della rete

Questa separazione consente di strutturare logicamente l'Internet globale in molte reti interconnesse.


Storicamente, il sistema IPv4 si basava su uno schema basato su classi, etichettate da A a E, che definivano la gamma di Address e il loro uso previsto. Ogni classe assegnava un determinato numero di bit al _netid_ e all'_hostid_, influenzando direttamente il numero possibile di reti e host.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Non tutti i valori possibili possono essere assegnati agli host. Ad esempio, in una **classe C** Address, l'ultimo byte offre 8 bit (256 valori). Ma due di questi sono riservati:


- 0: identifica la rete stessa
- 255: è il **broadcast** Address, usato per inviare un pacchetto a tutti gli host della rete contemporaneamente.

Restano quindi 254 indirizzi utilizzabili per i dispositivi.


Il numero di indirizzi disponibili varia notevolmente da una classe all'altra: dalle grandi reti pubbliche in classe A, alle reti aziendali in classe B, fino alle reti locali più piccole in classe C.



![Image](assets/fr/013.webp)



Alcuni intervalli Address sono riservati per uso privato e non vengono mai instradati direttamente su Internet. Questi sono noti come **indirizzi privati** e sono utilizzati all'interno di organizzazioni, aziende o abitazioni e richiedono la traduzione del Address, in genere NAT (*Network Address Translation*), per raggiungere la rete Internet pubblica. Questi sono:


- Classe A**: da 10.0.0.0 a 10.255.255.255
- Classe B**: da 172.16.0.0 a 172.31.255.255
- Classe C**: da 192.168.0.0 a 192.168.255.255


Quando un dispositivo con un Address privato accede a Internet, un router o un gateway abilitato NAT lo sostituisce con un Address pubblico valido.


Esempio: Se un host ha il Address **192.168.7.5**, si può dedurre:


- 192.168.7.0: rete Address
- 192.168.7.1: spesso il router locale
- 192.168.7.5: l'host stesso


Un altro caso speciale è **127.0.0.1**, noto come "***loopback***".

Sui sistemi Linux, è associato al Interface **lo**. Questo Address consente a una macchina di collegarsi al Address stesso per test o diagnostica locale, senza passare attraverso un Interface fisico. L'intero intervallo **127.0.0.0/8** è riservato a questo scopo.


Per ottimizzare l'uso del Address e progettare reti complesse, la **subnetmask** (_netmask_) è essenziale. Questa maschera binaria separa il _netid_ dall'_hostid_ in un Address IP.

Ogni classe ha una maschera predefinita:


- 255.0,0,0** per la classe A,
- 255.255.0.0** per la classe B,
- 255.255.255.0** per la classe C.


Una buona progettazione di rete segue una regola di base: i dispositivi che devono comunicare direttamente devono trovarsi nella stessa rete o sottorete. Per segmentare una rete, si ricorre al subnetting, che consiste nel dividere una rete in sottoreti più piccole utilizzando una maschera più specifica.


Esempio di subnetting:

Una rete di **classe C**: 192.168.1.0/24 con una maschera predefinita di 255.255.255.0.

Vogliamo 4 sottoreti con un massimo di 60 host ciascuna.


**Fase 1**: Numero di indirizzi necessari per sottorete = 60 + 2 indirizzi riservati (rete + broadcast) = 62.


**Fase 2**: Trovare la più vicina potenza di 2 ≥ 62. -> 2⁶ = 64.


**Fase 3: Regolare la maschera. Mantenere i bit _netid_ e riservare i bit _hostid_ necessari. Otteniamo una maschera binaria che, una volta convertita, dà **255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Fase 4**: Calcolare gli intervalli Address per ciascuna sottorete, variando i bit riservati all'host.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Fase 5**: In questo modo si creano quattro sottoreti, ognuna delle quali supporta fino a 62 macchine, mantenendo efficiente lo schema di indirizzamento complessivo. La parte _hostid_ è divisa in una parte _subnetid_ e una parte host.



![Image](assets/fr/016.webp)



Questo principio fondamentale di subnetting rimane indispensabile nella moderna ingegneria di rete, consentendo un'allocazione IP precisa, un migliore controllo del traffico, un forte isolamento dei segmenti e una gestione scalabile della rete.



### Indirizzamento CIDR


All'inizio degli anni '90, con la rapida diffusione di Internet nelle aziende e nelle organizzazioni, il tradizionale sistema di indirizzamento IP basato sulle classi (A, B, C) ha iniziato a mostrare i suoi limiti.

La sua struttura rigida portava a un notevole spreco di indirizzi IP e rendeva le tabelle di routing sempre più grandi, complesse e difficili da mantenere.

Per risolvere questi problemi, è stato introdotto un metodo più flessibile ed efficiente: **CIDR** (_Classless Inter-Domain Routing_). Il CIDR è diventato gradualmente lo standard, sostituendo in larga misura il vecchio sistema basato sulle classi.


L'idea alla base del CIDR è la capacità di raggruppare diverse reti adiacenti, in particolare blocchi di Classe C, in un'unica unità logica chiamata **supernet** (_supernet_). Con questa aggregazione, una singola voce nella tabella di routing può rappresentare più sottoreti, riducendo il numero di percorsi che i router devono gestire e migliorando le loro prestazioni.


Se inizialmente le reti di Classe C erano quelle che avevano più bisogno di aggregazione a causa della loro minore capacità, il principio è stato applicato anche alle reti di Classe B e, in teoria, anche a quelle di Classe A, anche se queste ultime sono meno interessate grazie alla loro ampia portata Address.


Con CIDR, il concetto di classi fisse scompare. Lo spazio Address viene trattato come un intervallo continuo che può essere diviso o aggregato a seconda delle necessità. I blocchi CIDR sono definiti utilizzando maschere di sottorete che non sono limitate alle classi A, B o C predefinite. Un blocco CIDR può rappresentare una singola rete o un insieme contiguo di sottoreti che condividono lo stesso prefisso.


Un blocco CIDR è scritto nel formato "Address/prefix", dove il numero dopo la barra indica quanti bit compongono la parte di rete. Ad esempio, /17 significa che i primi 17 bit identificano la rete, mentre i restanti 15 bit identificano gli host.


Esempio:

Un blocco /17 contiene 2^(32-17) indirizzi, quindi 2^15 = 32.768 indirizzi totali. Sottraendo i due indirizzi riservati (rete e broadcast) rimangono 32.766 indirizzi host utilizzabili. Ciò consente agli amministratori di rete di dimensionare le sottoreti in base alle esigenze reali, evitando inutili sprechi.


Per facilitare la comprensione del dimensionamento CIDR, ecco una tabella dei prefissi più comuni e delle relative maschere di sottorete e indirizzi utilizzabili equivalenti:


| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**NOTA**: Storicamente, l'RFC 950 scoraggiava l'uso della subnet zero, principalmente per evitare confusione nell'instradamento.  Questa restrizione è diventata obsoleta con la RFC 1878, che ne consente pienamente l'uso. La vecchia limitazione era dovuta principalmente all'incompatibilità con l'hardware più vecchio che non poteva gestire correttamente il CIDR. Le apparecchiature moderne non hanno questo problema.


Ad esempio, la sottorete **1.0.0.0** con la maschera di sottorete **255.255.0.0**, un tempo ambigua con l'identificatore di rete di classe A, è ora perfettamente valida e utilizzabile.


**TIP**: per calcolare le sottoreti senza errori e convertire rapidamente gli indirizzi in notazione CIDR, esistono strumenti pratici come ***ipcalc***. Questo "calcolatore di rete" mostra chiaramente le suddivisioni Address, gli intervalli disponibili e le maschere associate, ideale sia per gli amministratori che per gli studenti che stanno imparando il CIDR.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## Il protocollo TCP


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



Il protocollo **TCP** (_Transmission Control Protocol_) svolge un ruolo centrale nel Layer TRANSPORT del modello TCP/IP. Funge da ponte tra le applicazioni e Internet Layer, garantendo il trasferimento affidabile dei dati tra due macchine distanti.

Mentre il protocollo IP si limita a inviare i pacchetti senza garantirne la consegna o l'ordine, il TCP assicura l'integrità e la coerenza del flusso di dati, consegnandoli senza perdite, nell'ordine corretto e senza duplicati.


Le principali responsabilità di TCP comprendono:


- Riordino dei segmenti ricevuti;
- Monitoraggio del flusso di dati per evitare congestioni;
- Suddivisione o riassemblaggio dei blocchi di dati in unità adeguate (segmenti);
- Gestione della creazione e della chiusura delle connessioni tra le due estremità della comunicazione.


Il TCP è un protocollo orientato alla connessione, cioè stabilisce una relazione esplicita e continua tra client e server. A tal fine, utilizza **numeri di sequenza** e **riconoscimenti**: per ogni segmento inviato, viene assegnato un identificatore univoco in modo che la macchina ricevente possa controllare sia l'ordine che l'integrità dei dati. Il destinatario restituisce quindi un segmento di riconoscimento con il flag **ACK** impostato a 1, confermando la ricezione e indicando il prossimo numero di sequenza previsto.



![Image](assets/fr/018.webp)



Per migliorare l'affidabilità, il TCP utilizza un timer: una volta inviato un segmento, inizia un conto alla rovescia. Se non arriva un riscontro entro il periodo di timeout, il mittente ritrasmette automaticamente il segmento, supponendo che sia stato perso durante il transito. Questo meccanismo di ritrasmissione automatica compensa le perdite inerenti alle reti IP, che possono verificarsi in caso di congestione, errori di instradamento o guasti hardware.



![Image](assets/fr/019.webp)



TCP è in grado di rilevare e gestire i duplicati. Se arriva un segmento ritrasmesso ma anche l'originale, il ricevitore utilizza i numeri di sequenza per identificare il duplicato e conserva solo la copia corretta, eliminando ogni ambiguità.


Affinché questo processo funzioni, le due macchine devono avere una comprensione comune dei loro numeri di sequenza iniziali. Ciò viene garantito seguendo una rigorosa procedura di connessione: da un lato, il **server** resta in ascolto su una porta specifica, in attesa di una richiesta in arrivo (modalità passiva); dall'altro, il **cliente** avvia attivamente la connessione inviando una richiesta al server sulla stessa porta di servizio.


**NOTA**: Una "porta" è un identificatore numerico (da 0 a 65.535) assegnato a un'applicazione di rete su un computer. Viene utilizzata per differenziare più servizi in esecuzione simultanea sullo stesso IP Address. Quando un client invia dati, specifica il numero di porta in modo che il sistema operativo del server sappia quale programma deve riceverli (ad esempio, 80 per HTTP, 443 per HTTPS, 25 per SMTP). Le porte agiscono come porte dedicate, indirizzando il traffico in entrata e in uscita, impedendo la confusione tra i servizi e consentendo un controllo dell'accesso a grana fine tramite firewall o regole di filtraggio.


La sincronizzazione della sequenza Exchange si basa sul famoso meccanismo **"*three-way handshake*"**, simile al modo in cui due persone si salutano per stabilire un contatto. Questa fase di inizializzazione, che garantisce l'affidabilità del TCP, si svolge in 3 fasi:

1. **SYN:** Il client invia un segmento di sincronizzazione iniziale (**SYN**) con il flag appropriato impostato e un numero di sequenza iniziale (ad esempio, C);

2. **Il server ricevente risponde con un segmento di conferma (**SYN-ACK**), che conferma il numero di sequenza del client e fornisce il proprio numero di sequenza iniziale;

3. **Il client invia una conferma finale (**ACK**) che conferma la ricezione del numero di sequenza del server, finalizzando la sincronizzazione. Il flag SYN è ora disabilitato e il flag ACK rimane impostato, a indicare che la connessione è stabilita.



![Image](assets/fr/020.webp)



Questo protocollo Exchange assicura che entrambe le parti condividano la stessa base di numerazione prima di trasmettere i dati del carico utile. Una volta completata la sincronizzazione, la sessione viene aperta: i segmenti possono ora viaggiare in entrambe le direzioni, ciascuno riconosciuto alla ricezione, garantendo la massima affidabilità del flusso di dati.


L'handshake a tre vie*** riguarda solo la creazione della connessione. Per la chiusura, il protocollo TCP utilizza un *quadruplo handshake*: FIN → ACK → FIN → ACK, che garantisce che nessun segmento in transito venga perso prima del rilascio completo della connessione.


Sebbene sia stato progettato per garantire robustezza e affidabilità, questo processo ha anche dato origine a vulnerabilità sfruttabili. Ad esempio, attacchi come l'**IP Spoofing** mirano a bypassare o a corrompere questa relazione di fiducia spacciandosi per una macchina autorizzata attraverso numeri di sequenza falsificati, creando una breccia che consente l'intercettazione o la manipolazione del flusso di dati.


Per limitare i rischi di dirottamento della sincronizzazione della sequenza e per gestire il carico della rete, il protocollo TCP utilizza una tecnica di gestione dei flussi nota come "**_Sliding Window_**". Questo sistema regola la quantità di dati che possono essere inviati senza richiedere un riconoscimento immediato per ogni segmento, riducendo così il sovraccarico inutile sulla rete e mantenendo una buona affidabilità.


In termini pratici, la finestra scorrevole definisce un intervallo di numeri di sequenza che possono circolare liberamente tra mittente e destinatario senza che ogni singolo segmento venga riconosciuto. Man mano che il sistema mittente riceve i riconoscimenti, la finestra "scivola": scorre verso destra per lasciare spazio a nuovi segmenti da inviare. La dimensione di questa finestra (fondamentale per ottimizzare il throughput evitando la congestione) è specificata nel campo "*Window*" dell'intestazione TCP.


**Esempio**: se il numero di sequenza iniziale è 3 e la finestra si estende fino alla sequenza 5, i segmenti numerati da 3 a 5 possono essere inviati senza attendere le singole conferme.



![Image](assets/fr/021.webp)



La dimensione della finestra scorrevole non è fissa, ma si adatta dinamicamente alle condizioni della rete e alla capacità di elaborazione del destinatario.  Se il ricevitore è in grado di gestire un volume maggiore di dati, lo segnala attraverso il campo Finestra, inducendo il mittente a espandere la propria finestra. Al contrario, in caso di sovraccarico o di rischio di saturazione, il destinatario può richiedere una riduzione, mentre il mittente aspetterà che la finestra si sposti in avanti per inviare ulteriori segmenti.


Il protocollo prevede una procedura simmetrica per la chiusura di una connessione TCP, in modo da garantire una chiusura pulita e ordinata. Ciascuna macchina può avviare la chiusura inviando un segmento con il flag **FIN** impostato a 1, segnalando l'intenzione di terminare la comunicazione. Quindi attende che tutti i segmenti in transito siano stati ricevuti e ignora qualsiasi altro dato.


Alla ricezione di questo segmento, l'altra macchina invia una conferma di ricezione, anch'essa contrassegnata dal flag FIN. Quindi termina l'invio dei dati rimanenti prima di informare l'applicazione locale che la coonnessione è stata chiusa. Questa doppia conferma assicura una chiusura ordinata e riduce al minimo il rischio di perdita di dati.


Questa gestione precisa, che combina l'instradamento flessibile di IP con il controllo rigoroso di TCP, è spesso illustrata da un diagramma che contrappone la velocità del protocollo IP (che funziona su base **"best effort "**, senza alcuna garanzia di consegna) all'affidabilità del protocollo TCP (che gestisce la trasmissione attraverso riconoscimenti e sequenze negoziate).



![Image](assets/fr/022.webp)



In alcuni casi, tuttavia, l'affidabilità assoluta non è la priorità: lo sono la velocità e la semplicità. Questo vale per applicazioni come lo streaming dal vivo o il VoIP, che possono tollerare una certa perdita di pacchetti senza compromettere seriamente l'esperienza dell'utente. In questi casi, è preferibile il **UDP** (_User Datagram Protocol_).


UDP opera su un principio fondamentalmente diverso da quello del TCP: è **senza connessione**, ovvero non viene stabilita alcuna relazione preliminare tra mittente e destinatario. Quando una macchina invia pacchetti tramite UDP, questi vengono trasmessi a senso unico; il destinatario non invia conferme e il mittente non ha alcuna conferma dell'arrivo del messaggio. L'intestazione UDP è volutamente minima, contiene solo la porta di origine, la porta di destinazione, la lunghezza del segmento e una somma di controllo, senza alcun meccanismo di riconoscimento o di controllo dello stato. Come sempre, gli indirizzi IP sono trasportati dall'intestazione IP sottostante.


Un'analogia comune è che il protocollo TCP è come una **chiamata telefonica**, in cui viene stabilito un circuito, seguito e controllato per tutta la durata della conversazione. Il protocollo UDP, invece, è come un **invio di posta**, in cui il mittente inserisce una lettera in una cassetta postale senza alcuna prova immediata di consegna o feedback sistematico.


Questa complementarità tra TCP e UDP consente alle reti moderne di adattarsi a diverse esigenze, scegliendo la massima affidabilità o privilegiando la velocità, a seconda dell'applicazione.



## Primitive di servizio


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Architettura a strati e organizzazione Exchange


Come abbiamo visto, i **servizi** sono l'implementazione concreta dei protocolli che abbiamo descritto finora. Sebbene il modello TCP/IP differisca dal modello **OSI**, adotta lo stesso approccio a strati: ogni Layer è progettato per svolgere una funzione specifica e per fornire **servizi** al Layer direttamente sopra di esso, dando vita a un'architettura modulare, robusta e facilmente manutenibile.


Ogni Layer si basa sulle capacità di quello sottostante e, a sua volta, fornisce al Layer superiore un Interface coerente per la gestione dei dati. In questa architettura, ogni Layer ha le proprie **strutture dati**, accuratamente definite per garantire la perfetta compatibilità con gli altri livelli. Questa compatibilità è essenziale per una comunicazione fluida, affidabile e chiara da un endpoint all'altro.


Due aspetti fondamentali regolano questi scambi:


- Aspetto verticale**: il rapporto tra un Layer e quello sopra o sotto di esso (da Layer N a Layer N+1 e viceversa).



![Image](assets/fr/023.webp)




- Aspetto orizzontale**: l'interazione tra applicazioni remote, cioè il dialogo tra un **cliente** e un **server**, in entrambe le direzioni.



![Image](assets/fr/024.webp)



L'architettura a strati segue il principio secondo cui ogni Layer elabora solo le informazioni che rientrano nel suo ambito: le strutture dei dati, le intestazioni e i meccanismi di controllo variano da un Layer all'altro, ma insieme formano un sistema coerente, che garantisce il graduale instradamento dei dati verso la loro destinazione finale.


**Ricordo**: Si utilizza una terminologia specifica per descrivere le unità di dati scambiate tra i livelli:


- messaggio** per l'applicazione Layer,
- segmento** per il Layer di trasporto (TCP),
- datagramma** per Internet Layer (IP),
- frame** per l'accesso alla rete Layer.


La tabella seguente riassume i termini dei contesti TCP e UDP:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Primitive di servizio e unità di dati


Al centro di questo sistema ci sono le **primitive di servizio**, che fungono da interfacce di comunicazione. Queste primitive funzionano come sportelli di servizio, in ascolto su **porte** specifiche riservate e consentono ai processi di stabilire, mantenere e terminare le connessioni di rete in modo controllato. Mentre i protocolli organizzano il formato e la trasmissione dei dati attraverso la rete, sono i **servizi e le loro primitive** a fornire il collegamento verticale tra i livelli.


Combinando l'aspetto orizzontale (comunicazione tra applicazioni distribuite) con quello verticale (interazioni interne tra i livelli), il modello TCP/IP offre un'architettura completa e scalabile. La sovrapposizione di queste due prospettive offre una chiara panoramica di come vengono scambiati i dati nella comunicazione di rete strutturata.



![Image](assets/fr/026.webp)



### Riassunto della parte


In questa prima sezione principale abbiamo esplorato l'architettura di base che governa la configurazione e il funzionamento delle attuali reti connesse a Internet. Questa architettura si basa su un **modello a quattro Layer**, ispirato al modello OSI, e costruito attorno alla suite di protocolli **TCP/IP**, la spina dorsale delle comunicazioni moderne. Abbiamo visto che TCP, con il suo approccio orientato alla connessione, garantisce trasferimenti affidabili, mentre UDP, più leggero e veloce, è preferito quando la velocità è più importante dell'affidabilità.


Il corretto funzionamento di questo modello si basa sull'implementazione di protocolli attraverso **primitive di servizio**. Queste garantiscono il collegamento tra i livelli, consentendo di adattare l'elaborazione dei dati ai requisiti specifici di ciascun livello, dal trasporto all'applicazione, compreso l'accesso a Internet e alla rete. Questo approccio modulare rende il sistema flessibile e robusto.


L'indirizzamento IP è un'altra pietra miliare di questa infrastruttura. Ogni dispositivo connesso è identificato da un **unico IP Address**, preso da uno spazio Address organizzato in **classi** (da A a E). Alcuni di questi indirizzi sono riservati per scopi speciali, come il loopback locale o il multicast, mentre altri, noti come "indirizzi privati", non vengono instradati su Internet senza traduzione (NAT). Questa classificazione consente un'organizzazione logica e gerarchica delle reti.


Abbiamo anche esaminato il concetto di **sottoreti**, che consente di dividere i segmenti di una rete per gestire meglio le risorse IP e ottimizzare il flusso di dati. Sebbene la suddivisione manuale tramite maschere di sottorete rimanga un principio importante, è stata ampiamente modernizzata grazie al **CIDR** (_Classless Inter-Domain Routing_). Questo metodo ha trasformato la gestione del Address consentendo un'allocazione più flessibile e razionale degli intervalli IP, riducendo al contempo le dimensioni delle tabelle di routing.


Padroneggiando questi concetti - livelli, protocolli, primitive di servizio, indirizzamento e subnetting - si acquisisce una solida base per comprendere il funzionamento tecnico delle reti moderne e per configurare in modo efficiente un'infrastruttura di rete per soddisfare le esigenze odierne.


Nella prossima sezione esamineremo più da vicino l'indirizzamento IPv4.



# Indirizzamento IPv4


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Utilizzo di IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



In questa sezione approfondiremo il modo in cui gli indirizzi **IPv4** sono effettivamente implementati in una rete reale. Ne analizzeremo il formato, la logica che li sottende e il modo in cui si collegano ad altri Elements chiave della rete, come i **nomi DNS**, gli **indirizzi MAC**, le **sottoreti** e le **tecniche di traduzione**.


Un IP Address è un identificatore numerico univoco assegnato a ciascun **network Interface** di un dispositivo. Consente di individuare il dispositivo all'interno della rete e di raggiungerlo per trasmettere dati. Ad esempio, un router, un server, una workstation, una stampante di rete o persino una telecamera di sorveglianza hanno almeno un proprio IP Address. L'IP Address rende possibile il **routing**, cioè lo spostamento di pacchetti dal punto A al punto B, anche se fisicamente distanti.


Gli indirizzi IP possono essere assegnati in due modi principali:


- Statico**: Impostato manualmente sul dispositivo.
- Dinamico**: Assegnato automaticamente su richiesta da un server DHCP (_Dynamic Host Configuration Protocol_). Il DHCP semplifica la gestione della rete, eliminando la necessità di una configurazione manuale e consentendo un controllo preciso attraverso le prenotazioni e la durata del lease.


*gli indirizzi *IPv4** sono scritti in un formato a **32 bit** suddiviso in **quattro byte**. Ogni byte contiene 8 bit e rappresenta un numero decimale da 0 a 255. I 4 byte sono separati da punti per formare una notazione chiara e leggibile.


esempio: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Ogni bit di un byte ha un valore (o "peso"): il bit di sinistra (il più significativo) vale 128, il successivo 64, poi 32, 16, 8, 4, 2 e 1 per il bit di destra (il meno significativo). In questo modo, la scrittura binaria viene convertita in decimale con la semplice aggiunta dei pesi impostati.


La tabella seguente illustra questa corrispondenza:



| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

Per convertire il binario in decimale, sommare i pesi dei bit impostati a 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

Un IP Address identifica un singolo **network Interface**, non l'intero dispositivo. Un router o un firewall multiporta ha più interfacce, ognuna con il proprio IP Address. Un Interface può anche avere più indirizzi IP (ad esempio, per servire più reti o servizi virtuali).


Ogni pacchetto IP contiene due indirizzi IP nell'intestazione:


- Il Address di origine (**mittente**)
- Il Address di destinazione (**ricevitore**)

I router leggono questi indirizzi per capire quale sia il percorso migliore per inviare il pacchetto fino alla destinazione. Senza regole di indirizzamento rigorose, il traffico di rete non potrebbe essere instradato correttamente e l'interconnessione globale delle reti sarebbe impossibile.


Un Address IPv4 è composto da due parti:


- NetID**: identifica la rete
- HostID**: identifica un dispositivo all'interno della rete

La **maschera di sottorete** determina dove finisce il NetID e dove inizia l'HostID, specificando quanti bit appartengono a ciascuna porzione. Più lungo è il NetID, maggiore è il numero di sottoreti possibili, ma il numero di host per sottorete diminuisce di conseguenza.


Originariamente, le reti IPv4 erano suddivise in cinque **classi**: (A, B, C, D ed E). Ogni classe corrisponde a uno specifico intervallo NetID e definisce una granularità fissa:


- Classe A: reti molto grandi con un gran numero di host
- Classe B: reti di medie dimensioni
- Classe C: reti di piccole dimensioni
- Classe D: indirizzi riservati al multicasting (_multicast_)
- Classe E: indirizzi sperimentali, non utilizzati per l'indirizzamento convenzionale



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Indirizzi speciali:


- Rete Address**: Identifica la rete stessa (utilizzata nelle tabelle di routing).
- Broadcast Address**: Invia i dati a tutti i dispositivi della sottorete contemporaneamente (tutti i bit HostID sono impostati su 1).


I seguenti intervalli sono riservati per uso interno:


- 10.0.0.0/8** (Classe privata A)
- 127.0.0.0/8** (loopback locale o _loopback_)
- 172.da 16.0.0 a 172.31.255.255** (classe B privata)
- 192.168.0.0 a 192.168.255.255** (classe C privata)


L'indirizzo **127.0.0.1** e, più in generale, l'intero intervallo 127.0.0.0/8 è utilizzato per i test interni: qualsiasi richiesta inviata ad esso non lascia mai la macchina. È utile per verificare che un servizio di rete locale funzioni senza coinvolgere la rete più ampia.


Per utilizzare meglio lo spazio Address, gli amministratori spesso dividono le reti in **sottoreti** utilizzando maschere di sottorete o la notazione **CIDR** (_Classless Inter-Domain Routing_). Il CIDR consente una gestione più precisa e aiuta a non sprecare indirizzi. Oggi il CIDR è essenziale per mettere a punto gli intervalli IP e ridurre le dimensioni delle tabelle di routing.


Nelle reti moderne, l'indirizzamento IP è solitamente abbinato ad altri identificatori:



- nome di dominio** registrato in un **DNS** (_Domain Name System_): Associa un IP numerico Address a un nome di facile accesso.
- MAC Address**: un identificatore fisico inciso nella scheda di rete, utilizzato per il trasporto locale (_Ethernet_). Quando un pacchetto IP deve essere trasmesso fisicamente, la tabella ARP abbina il Address IP al Address MAC della destinazione.


Per far fronte alla carenza di IPv4 Address e per aggiungere un Layer di sicurezza, le reti utilizzano spesso la traduzione Address (_NAT_). La NAT consente a molti dispositivi privati di condividere un unico IP pubblico Address quando accedono a Internet.


**Nota**: Gli strumenti online e integrati nel sistema operativo, come il [Grenoble CRIC calculator](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), semplificano notevolmente il calcolo di subnet e maschere.

Queste utility aiutano a pianificare in modo efficiente la suddivisione della rete.


In conclusione, il broadcast Address rimane una funzione pratica per l'invio dello stesso messaggio a tutti i dispositivi connessi a un segmento: ciò si ottiene impostando tutti i bit della parte HostID su 1, in modo che tutti gli host siano indirizzati.



## I diversi tipi di IPv4 Address


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



Gli indirizzi IPv4 si dividono in due categorie principali: indirizzi pubblici, direttamente accessibili su Internet, e indirizzi privati, destinati all'uso interno di una rete locale.


Un IPv4 Address pubblico è unico a livello globale e instradabile su Internet. Viene assegnato dalle autorità ufficiali ed è necessario per i servizi rivolti al pubblico, come siti web, server di posta elettronica o infrastrutture cloud.

L'unicità mondiale di questi indirizzi è essenziale per evitare conflitti o collisioni di routing.


La **IANA** (_Internet Assigned Numbers Authority_), che opera sotto la **ICANN** (_Internet Corporation for Assigned Names and Numbers_), gestisce la distribuzione di questi intervalli IP. In concreto, la IANA divide lo spazio IPv4 in 256 blocchi di dimensione /8, secondo la notazione CIDR. Ogni blocco rappresenta poco più di 16,7 milioni di indirizzi (2³² / 2⁸).


Questi blocchi unicast Address sono affidati dalla IANA ai **Regional Internet Registries** (RIR). Questi RIR sono responsabili della ridistribuzione degli indirizzi a livello regionale, in base alle reali esigenze dei fornitori di accesso, delle aziende o delle amministrazioni. Lo spazio unicast Address si estende dai blocchi **1/8 a 223/8**, con porzioni riservate a usi speciali (ricerca, documentazione, test) o assegnate direttamente a una rete o a un RIR per la ridistribuzione.


Per verificare chi possiede un IP pubblico Address, è possibile consultare i database RIR utilizzando il comando **whois** o le interfacce web fornite da ciascun registro. Questi strumenti possono essere utilizzati per risalire all'organizzazione o al provider che ha dichiarato il Address.


Esistono invece indirizzi IPv4 privati, una risposta pratica alla carenza di indirizzi pubblici. Questi indirizzi, che non sono instradabili su Internet, sono riservati agli ambienti locali: reti aziendali, LAN domestiche, data center o cluster informatici. Non sono unici a livello mondiale: molte reti private possono riutilizzare gli stessi intervalli IP senza interferenze, purché rimangano isolate o utilizzino un dispositivo di traduzione di rete Address per accedere a Internet.


Per consentire a un dispositivo con un IP Address privato di accedere a Internet, le reti utilizzano il NAT (Network Address Translation). Il NAT funziona sostituendo dinamicamente il Address privato con uno pubblico, consentendo a decine (o addirittura centinaia) di dispositivi di condividere un unico IP Address pubblico. Questo metodo ottimizza l'uso dello spazio IPv4 e aggiunge anche un Layer di sicurezza, nascondendo la struttura interna della rete.


Un'altra categoria speciale è quella degli indirizzi **non specificati**. La notazione IPv4 **0.0.0.0** o la sua versione IPv6 **::/128** significa "nessun Address specifico". Tale Address non è valido come destinazione Address di rete, ma può essere utilizzato localmente da un host per indicare "tutte le interfacce" o "nessun Address ancora assegnato". Questo è comune nei Assignment dinamici DHCP o per l'ascolto su tutte le interfacce del server.


IPv6 supporta anche l'indirizzamento privato, ma in generale lo standard raccomanda l'indirizzamento pubblico per evitare di sovrapporre più livelli NAT. Gli **indirizzi locali** (_site-local_) del blocco **fec0::/10** sono stati deprecati dalla **RFC 3879** per motivi di coerenza e sicurezza. Sono stati sostituiti da **Unique Local Addresses** (_ULA_) situati nel blocco **fc00::/7**. Gli ULA consentono la creazione di reti IPv6 private con instradamento interno pulito, utilizzando un identificatore a 40 bit generato casualmente per garantire l'unicità locale.


L'esaurimento dell'IPv4 è stato ufficialmente confermato nel 2011. Per prolungarne la durata, la comunità di Internet ha adottato diverse strategie:


- Migrazione graduale a **IPv6**
- Uso diffuso di **NAT**
- Politiche di allocazione più rigorose da parte delle RIR, che richiedono una precisa giustificazione e gestione delle esigenze di Address
- Recupero dei blocchi Address inutilizzati o restituiti volontariamente dalle aziende


Queste misure dimostrano che l'indirizzamento IP non è solo una sfida tecnica, ma anche una questione di governance globale, centrale per la continua espansione di Internet.



## DNS, una directory Address


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Siamo onesti: gli esseri umani non sono bravi a memorizzare lunghe stringhe di numeri, sia in forma binaria che decimale. Questa sfida diventa ancora più grande con gli indirizzi IP, che possono essere complessi e un singolo IP Address può talvolta mascherare più indirizzi, soprattutto quando sono coinvolte tecniche come NAT o hosting virtuale.


Per facilitare le cose, l'applicazione Layer utilizza un sistema che collega un IP Address a un nome logico leggibile dall'uomo. Questo è il ruolo del **DNS** (*Domain Name System*), una directory massiccia, gerarchica e distribuita che abbina nomi di dominio leggibili a indirizzi IP. Il sistema si basa su una serie di protocolli e servizi. Il software server DNS più utilizzato è **BIND** (_Berkeley Internet Name Domain_), un pacchetto software open-source che fa riferimento a gran parte dell'infrastruttura DNS di Internet.


L'idea alla base del DNS è semplice: per qualsiasi servizio connesso, sia esso un sito web, un server di posta o un altro servizio di rete, esiste un record che mappa un nome di dominio a uno o più indirizzi IP. Questo funziona in due direzioni:


- Risoluzione in avanti: traduzione di un nome in un IP Address.
- Risoluzione inversa: trovare il nome di dominio associato a un determinato IP Address.

Questo rende l'indirizzamento di rete utilizzabile dagli esseri umani, preservando al contempo la precisione di cui i router hanno bisogno per spostare correttamente i dati.


Un nome di dominio è sempre strutturato in modo gerarchico, con ogni livello separato da un punto: il nome completo è chiamato **FQDN** (_Fully Qualified Domain Name_). La parte più a destra è il **TLD** (_Top Level Domain_), come `.com`, `.org` o `.fr`. La parte più a sinistra indica l'host, ossia la macchina o il servizio specifico collegato all'IP Address.


Il sistema DNS è concepito come un **albero di zone**. Una **zona** è una sezione dello spazio dei nomi di dominio gestita da uno specifico server DNS. Una singola zona può contenere più **sottodomini**, che possono a loro volta essere delegati ad altre zone gestite da server diversi. Gli amministratori sono responsabili della manutenzione delle loro zone: gestione degli aggiornamenti, delle deleghe e della gestione generale.


Questa struttura consente non solo di puntare a un dominio principale (ad esempio `example.com`), ma anche di mettere a punto i record per i singoli host (`www`, `mail`, `ftp`, ecc.). Agli albori della rete, questa mappatura veniva gestita con file statici (`/etc/hosts` sui sistemi Unix), ma questo metodo è diventato presto impraticabile per un'Internet in rapida crescita e interconnessione.


È importante capire che un **server DNS** può servire solo un ambito limitato. Ad esempio, il server DNS interno di un'azienda potrebbe non essere direttamente accessibile da Internet. Se questo DNS non è configurato per inoltrare le query o non ha un rapporto di fiducia con altri server, alcune query falliranno: né il nome né l'IP Address possono essere risolti al di fuori della zona definita.


Il DNS svolge anche un ruolo nell'instradamento delle e-mail. Ad esempio, un record **MX** (_Mail Exchange_) specifica i server di posta responsabili della ricezione delle e-mail per un determinato dominio. Questi record definiscono le priorità (fattore di ponderazione) e le soluzioni di failover. Il file di zona di un server DNS deve contenere un record **SOA** (_Start Of Authority_), che designa il server come fonte ufficiale di informazioni per quella zona.


Grazie alla sua struttura gerarchica e distribuita, il DNS rimane una pietra miliare di Internet, consentendo agli utenti di accedere ai servizi attraverso nomi di dominio chiari e memorizzabili invece di indirizzi IP lunghi e tecnici.


Nel prossimo capitolo esploreremo un altro concetto fondamentale: *gli *indirizzi Ethernet**, noti anche come **indirizzi MAC**, che garantiscono la consegna dei dati al Layer fisico delle reti locali.



## Scoprire gli indirizzi Ethernet e ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Definizioni


Affinché il protocollo di instradamento dei dati funzioni in modo affidabile e coerente, è essenziale un componente chiave. Come esseri umani, possiamo facilmente identificare una macchina dal suo IP Address o dal suo nome recuperato tramite DNS. Una macchina, tuttavia, deve essere in grado di riconoscere senza ambiguità il dispositivo di destinazione per consegnare i pacchetti. Per farlo, si affida a un identificatore hardware specifico, utilizzato direttamente dal suo Interface di rete: il MAC Address (_Media Access Control_).


**Nota**: Questo non ha nulla a che vedere con un "Address fisico" nell'architettura della memoria. In informatica, una memoria fisica Address si riferisce a una posizione specifica sul bus di memoria, a differenza di una Address virtuale gestita dal sistema operativo. Un Address MAC, invece, si riferisce esclusivamente all'hardware di rete.


Il MAC Address è assegnato in modo permanente e univoco dal produttore dell'apparecchiatura. Il MAC Address identifica inequivocabilmente la scheda di rete, sia che si tratti di un computer, di uno smartphone, di una stampante o di qualsiasi altro dispositivo collegato. A differenza di un IP Address, che può cambiare dinamicamente (tramite un server DHCP o una configurazione manuale), il MAC Address rimane normalmente lo stesso per tutta la vita del dispositivo, a meno che non venga deliberatamente modificato.


Ogni rete Interface, cablata o wireless, ha il proprio MAC Address. Questo Address viene utilizzato all'interno del data link Layer (Layer 2 del modello OSI) per inserire e gestire l'hardware Address in ogni frame di rete scambiato. Questo è talvolta indicato come _indirizzo Ethernet_ o _UAA_ (_Universally Administered Address_). Standardizzato su una lunghezza di 48 bit, o 6 byte, è scritto in notazione esadecimale, generalmente sotto forma di byte separati da `:` o `-`.


Ad esempio: `5A:BC:17:A2:AF:15`


In questa struttura, i primi tre byte identificano il produttore della scheda di rete: si tratta del cosiddetto **OUI** (*Organisationally Unique Identifier*). Questi prefissi, assegnati dall'IEEE, sono utilizzati anche in altri schemi di indirizzamento hardware, come Bluetooth e LLDP, per garantire l'unicità a livello mondiale.


### Modifica di un MAC Address (MAC Spoofing)


In teoria, il MAC Address è progettato per rimanere fisso, ma esistono modi per modificarlo, in particolare per soddisfare esigenze particolari o per aggirare alcuni vincoli. Questa operazione, spesso definita _spoofing MAC_, consiste nel sostituire il Address hardware originale con un valore diverso, definito a livello software. Alcuni sistemi operativi facilitano questa modifica, in particolare quando il Address Ethernet effettivo non è utilizzato direttamente dal driver.


Le ragioni di una tale modifica sono varie. Può trattarsi della necessità che una determinata applicazione richieda uno specifico Ethernet Address per funzionare correttamente, oppure di risolvere un conflitto di indirizzi identici tra due dispositivi che condividono la stessa rete locale.


La modifica del MAC Address può essere motivata anche da considerazioni di privacy: nascondendo l'identificatore univoco inciso sulla scheda, gli utenti riducono la possibilità che il loro dispositivo venga tracciato da reti o servizi di sorveglianza. Tuttavia, questa pratica non è priva di conseguenze. La modifica di un MAC Address può disturbare alcuni dispositivi di filtraggio o richiedere la riconfigurazione dei firewall per autorizzare il nuovo hardware.


Alcune reti, in particolare quelle Wi-Fi, utilizzano il filtraggio MAC Address per consentire l'accesso solo ai dispositivi con indirizzi approvati. Sebbene questo aggiunga un livello di controllo di base, non è sicuro di per sé. Un aggressore può catturare un MAC Address valido già autorizzato sulla rete e clonarlo per aggirare le restrizioni. Per questo motivo, il filtraggio MAC deve sempre essere combinato con misure di sicurezza più severe.


### Corrispondenza MAC/IP


Affinché una rete locale funzioni in modo efficiente, deve esistere una chiara mappatura tra indirizzi fisici (indirizzi MAC) e indirizzi logici (indirizzi IP). Senza questo collegamento, un computer potrebbe conoscere l'IP Address di una destinazione, ma non saprebbe come inviarle fisicamente i dati sulla rete locale.

Questa mappatura è gestita automaticamente dal protocollo ARP (_Address Resolution Protocol_).


In pratica, quando un utente vuole conoscere il MAC Address corrispondente a uno specifico IP Address, può utilizzare l'utility `arp`. Questo strumento controlla la tabella ARP locale della macchina per visualizzare le corrispondenze note tra gli indirizzi IP e gli indirizzi MAC della rete locale. In questo modo, è possibile verificare rapidamente l'effettivo collegamento tra i livelli logico e fisico.


Esempio pratico: se si desidera verificare quale scheda di rete corrisponde all'IP Address `192.168.1.5`, utilizzare il seguente comando:


```bash
arp –a 192.168.1.5
```


L'output mostrerà il Address fisico associato (MAC), la natura dell'ingresso (statico o dinamico) e il Interface interessato.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


È importante ricordare che il MAC Address e l'IP Address sono due identificatori completamente diversi, ma strettamente complementari. Il MAC Address è inciso in modo univoco su ogni Interface di rete dal produttore e serve a identificare fisicamente il dispositivo sulla rete locale. Il Address IP, invece, è un Address logico assegnato dinamicamente o staticamente, che consente alla macchina di unirsi alla rete IP e ai pacchetti Exchange al di fuori della sua rete locale.



- Esempio visivo di MAC Address:


![Image](assets/fr/032.webp)




- Esempio visivo di un IP Address:


![Image](assets/fr/027.webp)



In un ambiente aziendale, questi due livelli di indirizzamento non possono funzionare separatamente. Ad esempio, quando un server DHCP assegna automaticamente un IP Address, il MAC Address dell'apparecchiatura viene utilizzato come punto di partenza. Il computer invia una richiesta di trasmissione DHCP contenente il suo MAC Address in modo che il server possa assegnare un IP Address disponibile al dispositivo corretto. Senza questa identificazione hardware, il server DHCP non saprebbe a quale dispositivo consegnare il Address.


Il protocollo ARP è quindi fondamentale: fornisce il collegamento tra indirizzi IP e indirizzi fisici, consentendo alle macchine di tradurre una destinazione logica in una destinazione fisica effettiva. Quando un computer deve inviare un pacchetto a una macchina della stessa rete, consulta innanzitutto la sua tabella ARP per verificare se il MAC Address del destinatario è già noto. In caso contrario, trasmette una richiesta ARP a tutti gli host della rete locale. Il computer che riconosce l'IP Address del destinatario in questa richiesta risponde specificando il suo MAC Address. Il mittente scrive quindi questo IP/MW-134 in una tabella ARP. Il mittente scrive quindi questa coppia IP/MAC nella sua cache ARP, per evitare di dover ripetere l'operazione ogni volta che viene inviata la richiesta.


Questa tabella ARP funge da mini directory di mappatura, aggiornata dinamicamente in modo simile a come il DNS associa i nomi di dominio agli indirizzi IP. Senza ARP, non sarebbe possibile alcun Exchange locale, poiché il data link Layer deve conoscere il MAC Address per incapsulare correttamente i frame Ethernet.


Al contrario, il protocollo RARP (_Reverse Address Resolution Protocol_) è stato progettato per la situazione opposta: consentire a una macchina che conosce solo il suo MAC Address di scoprire il suo IP Address. Questo era il caso comune delle vecchie workstation senza un disco Hard locale, che dovevano avviarsi attraverso la rete e richiedere un IP Address. RARP è stato poi sostituito da **BOOTP** e poi da **DHCP**, che sono più flessibili e automatizzati.


Questi protocolli di associazione svolgono un ruolo importante nel routing. Un router è essenzialmente una macchina con più interfacce di rete, che collega segmenti diversi. Quando un router riceve un frame, lo elabora per estrarre il datagramma IP ed esamina l'intestazione IP per determinare la destinazione. Se la destinazione si trova su una rete direttamente collegata, il datagramma viene consegnato direttamente dopo aver aggiornato l'intestazione. Se la destinazione appartiene a un'altra rete, il router consulta la sua tabella di routing per identificare il percorso migliore, o _next hop_, verso la destinazione.


In questo modo il percorso viene suddiviso in segmenti più brevi e gestibili. Ogni router intermedio conosce solo il passo successivo, non necessariamente la destinazione finale.


**Ricorda: ** La consegna diretta avviene quando il mittente e il destinatario si trovano sulla stessa rete fisica. In caso contrario, la consegna è indiretta e passa attraverso uno o più router.


La tabella di routing, gestita manualmente (routing statico) o dinamicamente (routing dinamico), contiene le informazioni necessarie per decidere quale percorso seguire. Nelle piccole reti, una configurazione statica è sufficiente. Nelle infrastrutture più grandi, il routing dinamico è essenziale per adattare automaticamente i percorsi quando la topologia cambia o un collegamento si interrompe.


La tabella di routing funge da tabella di mappatura tra gli indirizzi IP di destinazione e i gateway successivi. Di solito memorizza gli identificatori di rete (_network ID_) anziché ogni singolo host Address, riducendo così notevolmente le sue dimensioni.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Grazie a queste voci, il router può determinare rapidamente attraverso quale Interface e a quale nodo deve essere inviato ogni datagramma. In combinazione con ARP per la risoluzione degli indirizzi MAC corrispondenti, questo assicura un trasferimento efficiente e affidabile dei dati attraverso la rete.


Infine, i protocolli di routing dinamico includono standard come RIP (_Routing Information Protocol_), basato sull'algoritmo della distanza, e OSPF (_Open Shortest Path First_), che calcola i percorsi più brevi in una topologia complessa. Questi protocolli aggiornano costantemente Exchange per ottimizzare i percorsi, ridurre i costi di trasmissione e migliorare la resilienza contro le interruzioni o la congestione.



## NAT: Traduzione Address


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Definizione


Network Address Translation_ (NAT) è una tecnica sviluppata per Address l'esaurimento graduale degli indirizzi IPv4 disponibili. Progettata come soluzione provvisoria prima dell'adozione generalizzata dell'IPv6, la NAT ha permesso ad aziende e privati di continuare a collegare un gran numero di macchine utilizzando solo un insieme limitato di indirizzi IP pubblici.


**Il passaggio da IPv4 a IPv6 risolve teoricamente il problema dell'esaurimento espandendo lo spazio Address da 32 bit a 128 bit, fornendo un numero quasi illimitato di indirizzi (2^128). In pratica, tuttavia, la transizione è ancora incompleta e il NAT rimane ancora oggi ampiamente utilizzato.


Il principio alla base del NAT è semplice ma molto efficace: invece di assegnare un unico IP pubblico Address a ogni dispositivo della rete interna, si utilizza un unico Address instradabile (o un piccolo pool di indirizzi) per tutti i dispositivi privati. Il gateway NAT, spesso integrato nel router o nel firewall, traduce dinamicamente l'IP interno Address insieme alle informazioni necessarie per instradare correttamente il traffico verso l'esterno e garantisce che le risposte vengano restituite al mittente originale.


Questo approccio ha un vantaggio immediato: nasconde completamente l'architettura di rete interna. Per un osservatore esterno, tutte le richieste provenienti da workstation, server o stampanti sembrano provenire dalla stessa identità pubblica. Gli indirizzi privati, solitamente presi da intervalli riservati (ad esempio 192.168.x.x o 10.x.x.x), rimangono invisibili da Internet.


Oltre a risolvere il problema della scarsità di IPv4, il NAT rafforza anche la sicurezza, creando una prima barriera logica tra la rete interna e quella pubblica. Le comunicazioni in entrata non richieste sono naturalmente bloccate, poiché solo le connessioni avviate dall'interno della rete beneficiano della traduzione necessaria per ricevere le risposte.



![Image](assets/fr/035.webp)



### Tipi di traduzione


Il NAT può essere implementato in modi diversi per soddisfare esigenze specifiche. Le due modalità principali di funzionamento sono la traduzione statica e la traduzione dinamica.


*la *traduzione statica** crea una mappatura fissa tra un IP Address privato e un IP Address pubblico. Ogni macchina interna è collegata in modo permanente al suo Address pubblico dedicato. Ad esempio, un dispositivo interno configurato come 192.168.20.1 può essere associato al Address 157.54.130.1 instradabile. Quando un pacchetto in uscita lascia la rete locale, il router sostituisce il Address di origine del pacchetto con il Address pubblico ed esegue l'operazione inversa per il traffico in entrata. Questa traduzione bidirezionale è trasparente per l'utente.


**Attenzione: ** Sebbene questo metodo isoli la rete interna, non risolve la carenza di indirizzi IP pubblici, poiché sono necessari tanti indirizzi pubblici quante sono le macchine da esporre. La traduzione statica è quindi utilizzata principalmente quando alcune risorse interne devono rimanere raggiungibili dall'esterno (server web, server di posta...).


*la *traduzione dinamica**, invece, utilizza un pool di indirizzi IP pubblici. Quando un host interno avvia una connessione, il router assegna temporaneamente uno di questi indirizzi pubblici al Address privato dell'host per la durata della sessione. Il collegamento è 1 a 1, ma temporaneo: una volta terminata la connessione, il Address pubblico diventa disponibile per un altro dispositivo. Il NAT dinamico riduce quindi il numero di indirizzi pubblici necessari quando non tutti i computer sono online contemporaneamente, ma richiede comunque un blocco di indirizzi esterni grande almeno quanto il numero massimo di connessioni simultanee.


*la *traduzione di porta** (PAT), nota anche come *sovraccarico NAT* o *masquerading IP*, fa un ulteriore passo avanti: tutti i dispositivi privati condividono un unico IP pubblico Address (o un numero molto ridotto). Per distinguere le sessioni, il gateway modifica non solo il Address di origine, ma anche la porta di origine. Mantiene una tabella che collega ogni coppia *(Address privato, porta privata)* a una coppia unica *(Address pubblico, porta pubblica)*. Questa forma di NAT è utilizzata in quasi tutti i router domestici e consente a decine di dispositivi (computer, smartphone, oggetti connessi, ecc.) di condividere lo stesso IP pubblico Address, mantenendo una comunicazione fluida.


Il NAT prolunga quindi la durata di vita dell'IPv4, aggiungendo al contempo un prezioso Layer elemento di segmentazione e sicurezza. Tuttavia, con l'aumento dell'adozione dell'IPv6 e la diffusione del suo vasto spazio Address, il ruolo del NAT probabilmente diminuirà, anche se per motivi di compatibilità e controllo sarà ancora utilizzato in alcuni ambienti per segmentare e filtrare il traffico.


### Implementazione NAT


Per garantire il corretto funzionamento della traduzione Address, il router o gateway NAT deve tenere un registro accurato delle mappature stabilite tra ciascun Address privato della rete interna e il Address pubblico utilizzato per comunicare con il mondo esterno. Queste informazioni sono memorizzate nella cosiddetta "tabella di traduzione NAT", che svolge un ruolo centrale nella gestione del traffico di rete.


Ogni voce di questa tabella collega almeno una coppia: l'IP interno Address della macchina che invia e l'IP esterno Address che sarà esposto su Internet. Quando un pacchetto dalla rete privata viene inviato a una destinazione pubblica, il router NAT intercetta il frame, analizza le intestazioni IP e TCP/UDP, quindi sostituisce il Address privato della sorgente con il Address pubblico del gateway. Sul percorso di ritorno, lo stesso gateway cattura il pacchetto in arrivo, controlla la tabella di mappatura ed esegue l'operazione inversa per reindirizzare il flusso al Address interno originale.


Questo principio di traduzione dinamica si basa su una gestione precisa della tabella: ogni voce rimane valida finché c'è traffico attivo che la giustifica. Dopo un periodo configurabile di inattività, la voce viene cancellata e può essere riutilizzata per nuove connessioni.


esempio di tabella di traduzione NAT semplificata


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

In questo esempio, se per la seconda voce non è transitato alcun pacchetto in oltre un'ora (3.600 secondi), essa viene contrassegnata come riutilizzabile. Al contrario, una durata pari a zero indica una comunicazione attiva, con la mappatura bloccata.


Sebbene il NAT funzioni in modo trasparente per la maggior parte degli usi comuni (navigazione web, e-mail, trasferimento di file, ecc.), può creare ulteriori problemi per alcune applicazioni di rete. Alcune tecnologie si basano sullo scambio esplicito di indirizzi IP o porte all'interno del payload dei pacchetti. Dopo il passaggio attraverso un gateway NAT, queste informazioni diventano inconsistenti.


Esempi tipici di limitazioni sono:


- I protocolli peer-to-peer (P2P), che richiedono connessioni dirette tra i dispositivi, sono ostacolati dalla barriera NAT, poiché tutte le macchine interne condividono lo stesso IP esterno Address e non possono essere raggiunte direttamente senza una configurazione specifica (come *port forwarding* o UPnP);
- Il protocollo IPSec, utilizzato per proteggere le comunicazioni di rete, cripta le intestazioni dei pacchetti. Poiché il NAT deve modificare queste intestazioni per sostituire gli indirizzi IP, la crittografia rende impossibile questa operazione senza meccanismi di adattamento come il NAT-T (*NAT Traversal*);
- Il protocollo X Window, che consente la visualizzazione remota di applicazioni grafiche su Unix/Linux, funziona in modo che il server X invii attivamente le connessioni TCP ai client. Questa inversione della direzione abituale delle connessioni può essere bloccata da NAT.


In generale, qualsiasi protocollo che includa esplicitamente il Address IP interno nel payload del pacchetto ne risentirà, poiché tale Address non corrisponderà più al Address reale, visibile su Internet, dopo la traduzione.


**Nota importante:** Per risolvere questi problemi, alcuni router NAT offrono la funzione di _Deep Packet Inspection_ (DPI) o _Protocol Helpers_, che ispezionano il contenuto dei pacchetti per identificare e sostituire dinamicamente gli indirizzi o i numeri di porta all'interno dei dati delle applicazioni. Ciò richiede una conoscenza approfondita del formato del protocollo e può creare vulnerabilità di sicurezza o aumentare l'utilizzo delle risorse.


**Attenzione:** Sebbene la NAT aiuti a nascondere la rete interna e a controllare il traffico in entrata, non sostituisce un firewall dedicato. La traduzione da sola non è una barriera di sicurezza completa: deve sempre essere integrata da chiare regole di filtraggio per bloccare il traffico non richiesto o indesiderato.


per illustrare il funzionamento pratico di questo sistema, si consideri il seguente esempio:{\i}



![Image](assets/fr/037.webp)



In questo scenario, una stazione di lavoro interna può accedere al server Web interno semplicemente chiamando l'URL `http://192.168.1.20:80`. L'indicazione della porta è facoltativa, poiché `80` è la porta HTTP standard. Al contrario, se la richiesta proviene dall'esterno, l'utente inserisce la porta pubblica Address `http://85.152.44.14:80`. Il router NAT riceve la richiesta, consulta la sua tabella di mappatura e traduce automaticamente il Address pubblico in uno privato, reindirizzando la connessione a `http://192.168.1.20:80`.


Lo stesso principio si applica a qualsiasi altro server autorizzato a ricevere connessioni Internet, come il server Extranet (circuito blu nel diagramma).


**Nota pratica:** negli ambienti virtualizzati si usano comunemente interfacce di rete chiamate _virbrX_ (per _Virtual Bridge X_). Questi bridge virtuali, forniti in particolare dalla libreria libvirt o dall'hypervisor Xen, collegano la rete interna virtuale delle macchine guest alla rete fisica applicando il NAT. Sono generalmente configurati tramite script in `/etc/sysconfig/network-scripts/`, come mostrato di seguito per `virbr0`:


```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```


Una volta creato il ponte virtuale, è necessario abilitare il routing IP e configurare la traduzione delle porte con `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Con questa configurazione, il traffico in uscita viene instradato e viene applicata la traduzione NAT, consentendo alle macchine virtuali di comunicare con il mondo esterno senza esporre direttamente i loro indirizzi IP interni.


Nel prossimo capitolo, esamineremo in dettaglio la configurazione dell'IP Address in ambiente Linux, con metodi semplici e avanzati adatti a diversi contesti di amministrazione.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Come si configura la rete con `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Configurazione standard


Dopo aver trattato le basi teoriche del networking e aver capito come funzionano gli indirizzi IP, le maschere, l'instradamento e la traduzione, è il momento di passare alla configurazione pratica. Su GNU/Linux, la configurazione della rete è ora gestita con il comando **`ip`** (pacchetto _iproute2_), che sostituisce il vecchio `ifconfig`.


`ip` consente di assegnare o modificare un IP Address, cambiare una maschera, avviare o arrestare un Interface o controllarne lo stato in qualsiasi momento.


**TIPS:** per visualizzare tutte le interfacce (attive o meno): `ip addr show`


Esempio: assegnazione di un Address statico e attivazione del Interface


Aggiungere Address `192.168.1.2/24` a Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Attivare il Interface:


```shell
ip link set dev eth0 up
```


Disattivare lo stesso Interface:


```shell
ip link set dev eth0 down
```


Visualizza lo stato di un Interface specifico:


```shell
ip addr show dev eth2
```


**Suggerimento pratico:** con `ip`, l'aggiunta di un ulteriore Address a un Interface non richiede più il suffisso `:1`. Basta aggiungere un'altra riga `ip addr add ...`:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Script di attivazione: ifup / ifdown


Le utilità `ifup` e `ifdown` leggono i file di configurazione statica da `/etc/sysconfig/network-scripts/` (su RHEL, CentOS, Rocky Linux, AlmaLinux...) o `/etc/network/interfaces` (su Debian/Ubuntu) per attivare o disattivare le interfacce in modo pulito.


```shell
ifup eth1
ifdown eth2
```


File di configurazione (simile a RHEL):


- /etc/sysconfig/network**: impostazioni globali (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-**: impostazioni specifiche per ogni Interface.


Esempio statico (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


Esempio di DHCP:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Questa struttura modulare è ancora valida e può essere facilmente automatizzata sui sistemi attuali.


### Configurazione avanzata: bonding


Negli ambienti professionali, l'obiettivo è garantire la continuità del servizio e/o aggregare la larghezza di banda. *I meccanismi di bonding* (o *teaming* con _teamd_) soddisfano queste esigenze: diverse interfacce fisiche funzionano come un unico Interface logico, spesso chiamato `bond0` o `team0`.



![Image](assets/fr/039.webp)



Prerequisiti:


- Caricare il modulo `bonding` (o usare `teamd`) ;
- Disporre di almeno due interfacce fisiche.


#### I vari metodi di incollaggio comuni:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Impostazione con `ip link



- Disattivare le interfacce fisiche:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Creare il Interface incollato:


```shell
ip link add bond0 type bond mode balance-alb
```



- Configurare le opzioni dopo la creazione


```shell
ip link set bond0 type bond miimon 100
```



- Assegnare gli indirizzi MAC e IP:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Collegare le interfacce slave:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Riportare tutto su:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Suggerimento: ** per staccare uno slave senza eliminare il legame: `ip link set eth1 nomaster`


#### Configurazione permanente (simile a RHEL)


Creare tre file in `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_


```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```


_ifcfg-eth0_


```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


_ifcfg-eth1_


```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


Allora:


```shell
systemctl restart network
```


#### IP aggiuntivo Address (alias moderno)


Con `ip`, è possibile aggiungere semplicemente un secondo Address allo stesso dispositivo:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Per rendere questo alias persistente dopo un riavvio, aggiungere un secondo blocco `IPADDR2=...` / `PREFIX2=...` a `ifcfg-eth0`, oppure creare una nuova connessione *NetworkManager* tramite `nmcli`.


Grazie a `ip` e ai comandi correlati (`ip link`, `ip addr`, `ip route`), la configurazione della rete è più coerente, scrivibile e chiara. Il bonding è un componente chiave delle architetture ad alta disponibilità e l'assegnazione di più indirizzi a un singolo Interface è diventata molto più semplice.


Nel prossimo capitolo esamineremo le specifiche e l'implementazione dell'indirizzamento IPv6.


# Indirizzamento IPv6


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: standard e definizioni


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Passiamo ora alla prossima generazione di indirizzamento IP: il protocollo IPv6, originariamente noto come IPng (_IP Next Generation_). Progettato per superare le limitazioni strutturali dell'IPv4, questo protocollo introduce un'architettura di indirizzamento notevolmente ampliata, oltre a numerose ottimizzazioni tecniche.


Le motivazioni alla base dell'adozione dell'IPv6 sono varie e Address esigenze critiche per l'evoluzione di Internet. In primo luogo, il ruolo dell'IPv6 è quello di supportare la crescita esponenziale del numero di dispositivi connessi (un obiettivo irraggiungibile con lo spazio limitato del Address IPv4). In secondo luogo, il protocollo mira a ridurre le dimensioni delle tabelle di routing, rendendo gli scambi più efficienti e riducendo il carico di lavoro dei router nel lungo periodo.


IPv6 cerca anche di semplificare alcuni aspetti della gestione dei pacchetti, migliorando il flusso dei datagrammi e ottimizzando la velocità di trasferimento tra le reti. Dal punto di vista della sicurezza, le intestazioni AH/ESP del protocollo *IPsec* sono incluse nella specifica di base e tutti i nodi IPv6 devono essere in grado di supportarle (RFC 6434). Il loro uso, tuttavia, rimane facoltativo: spetta all'amministratore abilitarli a seconda del contesto.


Altri obiettivi sono una gestione più precisa dei tipi di servizio, in particolare per garantire una migliore qualità delle applicazioni in tempo reale (VoIP, videoconferenze, ecc.). L'IPv6 è anche progettato per consentire una gestione più flessibile della mobilità: un dispositivo può cambiare punto di accesso senza modificare il proprio Address in modo visibile ai suoi pari.


Infine, l'IPv6 è stato progettato per coesistere con i protocolli legacy. Sebbene non sia direttamente compatibile a livello binario con l'IPv4, rimane pienamente interoperabile con i protocolli superiori al Layer, come TCP, UDP, ICMPv6 e DNS, nonché con i protocolli di routing come OSPF e BGP, a condizione che vengano apportate alcune modifiche. Per la gestione del multicast, IPv6 utilizza il protocollo MLD (*Multicast Listener Discovery*), che è l'equivalente funzionale di IGMP in ambiente IPv4.


### Regole di notazione


Uno dei cambiamenti più significativi dell'IPv6 è il formato dell'IP Address stesso. Per ovviare alla cronica carenza di indirizzi IPv4, la lunghezza del Address è stata aumentata da 32 a 128 bit, quindi 16 byte. In teoria, questo comporta un possibile spazio Address di:


$$3,4 ´times 10^{38}$$


Questo garantisce una capacità virtualmente illimitata per tutte le apparecchiature attuali e future.


Gli indirizzi IPv6 sono scritti in modo molto diverso dalla nota notazione decimale punteggiata. Un IPv6 Address è composto da otto gruppi di 16 bit, scritti in esadecimale e separati da due punti `:`.


Ad esempio:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Per semplificare la notazione, gli zeri iniziali di ciascun gruppo possono essere omessi. L'esempio precedente diventa quindi:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Inoltre, una singola sequenza continua di gruppi di zero può essere sostituita con::, accorciando ulteriormente il Address:


```
1987:c02:0:84c2::cf2a:9077
```


**Attenzione: ** questa regola è rigida: solo una sequenza di zeri consecutivi può essere sostituita da `::`. Se un Address contiene più sequenze di zeri, solo la più lunga viene condensata. Questo garantisce sia l'unicità che la leggibilità.


**Dettaglio importante:** il carattere `:` usato per separare i blocchi esadecimali può causare ambiguità negli URL, poiché `:` è usato anche per indicare una porta di servizio. Per evitare confusione, gli indirizzi IPv6 negli URL devono essere racchiusi tra parentesi quadre `[ ]`.


Esempio di accesso HTTP a una porta specifica per il Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Quando si rappresenta un Address IPv4 in un contesto IPv6, è possibile utilizzare una notazione mista in forma decimale punteggiata, preceduta da`::`:


```
::192.168.1.5
```


Questa compatibilità facilita la transizione tra i due protocolli consentendo di includere blocchi IPv4 nello spazio IPv6 Address.


**Nota: ** Per standardizzare la scrittura degli indirizzi, la RFC 5952 definisce un formato canonico con regole di abbreviazione per evitare rappresentazioni multiple dello stesso Address. L'osservanza di queste raccomandazioni aiuta a ridurre le interpretazioni errate e garantisce configurazioni di rete coerenti.


### Tipi di IPv6 Address


L'IPv6 si differenzia dal suo predecessore per un'ampia gamma di categorie Address, ognuna delle quali è stata progettata per usi specifici, consentendo al contempo un routing e una gestione della rete flessibili. Come per l'IPv4, gli indirizzi possono essere globali, locali, riservati o specifici per determinati meccanismi di transizione.


Un Address IPv6 non specificato è rappresentato da `::` o, più esplicitamente, `::0.0.0.0`. Questa forma speciale viene utilizzata durante l'acquisizione del Address o come valore predefinito per indicare l'assenza di un Address.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *In una LAN privata, il prefisso `fd00::/8` è preferibile per l'assegnazione di indirizzi interni che non sono instradabili su Internet.*


#### Indirizzi riservati


Alcuni intervalli IPv6 sono esplicitamente riservati e non devono essere utilizzati come indirizzi globali. Hanno scopi tecnici specifici:


- `::/128`**: Address non specificato, mai assegnato in modo permanente a un dispositivo, ma usato come fonte Address da una macchina in attesa di configurazione.
- `::1/128`**: il _loopback_ Address, l'equivalente diretto di `127.0.0.1` in IPv4, che consente a una macchina di collegarsi al Address stesso.
- `64:ff9b::/96`**: Riservato ai traduttori di protocollo per consentire l'interconnessione IPv4/IPv6, come definito in RFC 6052.
- `::ffff:0:0/96`**: blocco di compatibilità per rappresentare un Address IPv4 in una struttura IPv6 specifica, spesso usato internamente dalle applicazioni.


Questi blocchi garantiscono l'interoperabilità e facilitano la migrazione tra le due versioni del protocollo.


#### Indirizzi unicast globali


Gli indirizzi unicast globali costituiscono la maggior parte dello spazio IPv6 pubblicamente instradabile, rappresentando circa 1/8 dello spazio Address. Dal 1999, la IANA ha assegnato questi blocchi, come il prefisso `2001::/16`, in blocchi CIDR (da `/23` a `/12`) ai registri regionali, che poi li ridistribuiscono a provider e organizzazioni.


Alcuni campi hanno usi speciali documentati:


- `2001:2::/48`**: Riservato ai test di prestazione e interoperabilità (RFC 5180).
- `2001:db8::/32`**: Riservato alla documentazione e agli esempi (RFC 3849).
- `2002::/16`**: Utilizzato per il meccanismo 6to4, che consente al traffico IPv6 di viaggiare attraverso un'infrastruttura IPv4 (utile durante la fase di transizione tra i due protocolli).


**Nota:** una gran parte degli indirizzi globali rimane inutilizzata e serve come riserva per la futura crescita di Internet.


#### Indirizzi locali unici (ULA)


Gli indirizzi locali unici (`fc00::/7`) sono l'equivalente IPv6 degli indirizzi privati IPv4 (RFC1918). Consentono di creare reti interne isolate senza rischiare conflitti con l'indirizzamento pubblico. In pratica, il prefisso effettivo è `fd00::/8`, con l'ottavo bit impostato a 1 per indicare l'uso locale. Ogni blocco ULA include un identificatore pseudocasuale a 40 bit, che riduce al minimo le collisioni Address quando si collegano reti private separate.


#### Indirizzi link-local


Gli indirizzi link-local (`fe80::/64`) sono utilizzati esclusivamente per la comunicazione all'interno dello stesso segmento Layer 2 (stessa VLAN o switch). Non vengono mai instradati oltre il collegamento locale. Ogni Interface di rete genera automaticamente un Address link-local, spesso derivato dal suo Address MAC utilizzando lo schema EUI-64.


**Caratteristica speciale**: la stessa macchina può utilizzare lo stesso link-local Address su più interfacce, ma il Interface deve essere specificato quando si comunica per evitare ambiguità.


#### Indirizzi multicast


In IPv6, il broadcast è stato sostituito dal multicast, un modo più efficiente per consegnare i pacchetti a un gruppo definito di destinatari. L'intervallo multicast ha il prefisso `ff00::/8`. Questo include indirizzi come `ff02::1`, che si rivolge a tutti i nodi del collegamento locale. Anche se conveniente, questo Address non è più raccomandato per le applicazioni, in quanto può generare trasmissioni incontrollate generate.


Un uso comune del multicast è il _Neighbor Discovery Protocol_ (NDP), che sostituisce ARP in IPv6. NDP utilizza indirizzi multicast specifici, come `ff02::1:ff00:0/104`, per scoprire automaticamente altri host connessi allo stesso link.


Combinando questi tipi di Address, l'IPv6 offre una serie completa di opzioni per soddisfare le esigenze di routing globale, comunicazioni locali, migrazione IPv4/IPv6 e configurazione automatica dei dispositivi, migliorando al contempo l'efficienza della trasmissione.


### Portata Address


L'ambito di un Address IPv6 definisce il dominio esatto in cui è valido e unico. La comprensione di questo concetto è fondamentale per padroneggiare l'instradamento dei pacchetti e l'organizzazione logica di una rete IPv6. Gli indirizzi IPv6 sono generalmente raggruppati in tre categorie principali in base al loro ambito e utilizzo: unicast, anycast e multicast.


*gli indirizzi *Unicast** sono i più comuni e comprendono diversi sottotipi distinti.

Questi includono il Address _loopback_ (`::1`), il cui ambito è limitato all'host che lo utilizza e che viene usato per testare lo stack di rete internamente senza inviare traffico sulla rete fisica.

Esistono poi gli indirizzi link-local (_link-local_), il cui campo di applicazione è limitato a un singolo segmento di rete: sono utilizzati per le comunicazioni dirette tra dispositivi sullo stesso collegamento fisico o logico (ad esempio, un singolo switch o una VLAN).

Infine, gli indirizzi locali unici (_ULA_, per _Unique Local Addresses_) sono interni a una rete privata. Possono essere instradati tra più segmenti privati, ma non sono mai visibili su Internet.


Concettualmente, gli indirizzi IPv6 sono spesso rappresentati come una struttura binaria in cui la prima metà (i primi 64 bit) identifica il prefisso di rete e la seconda metà (anch'essa di 64 bit) identifica in modo univoco il Interface del dispositivo su quella rete. Questa suddivisione facilita l'autoconfigurazione Address attraverso meccanismi come SLAAC (_Stateless Address Autoconfiguration_), che consentono alle macchine di assegnare automaticamente generate un Address stabile basato sul MAC Address o su un identificatore pseudo-casuale.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

L'architettura IPv6 segue il modello di routing globale gerarchico dell'attuale Internet. Il partizionamento dei prefissi consente ai registri regionali e agli operatori di rete di gestire l'assegnazione dei Address in modo decentralizzato, garantendo al contempo l'unicità globale. In questo contesto, lo stesso host può possedere contemporaneamente un Address unicast globale per le comunicazioni Internet e un Address link-local per le interazioni locali, ad esempio con il vicinato immediato o per i messaggi di scoperta dei router.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Gli indirizzi anycast** rappresentano un concetto intermedio che si basa sul modello unicast ma che in alcuni casi può comportarsi come il multicast. Un Address anycast è, in sostanza, un Address unicast assegnato a più interfacce distribuite su diversi nodi di rete. Quando un pacchetto viene inviato a un Address anycast, il protocollo IPv6 mira a consegnarlo a uno degli host che condividono quel Address, in genere quello più vicino in termini di topologia di routing. Questo approccio ottimizza la velocità di elaborazione delle query e migliora la resilienza dei servizi distribuiti. Un esempio classico sono i server DNS root, dove l'indirizzamento anycast indirizza automaticamente le query al punto di presenza più vicino.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

Nell'IPv6, gli **indirizzi multicast** sostituiscono il meccanismo di broadcast, considerato troppo costoso e inadatto a una rete su scala globale. Un Address multicast identifica un gruppo di interfacce, in genere tra più host, che desiderano ricevere gli stessi pacchetti contemporaneamente.

Ogni multicast Address include uno speciale campo _scope_ a 4 bit, che definisce il limite geografico o logico della trasmissione:


- Uno scope di `1` significa che il pacchetto è solo per il dispositivo locale.
- Uno scope di `2` limita il pacchetto al collegamento locale: tutti i dispositivi sullo stesso segmento fisico o virtuale possono riceverlo.
- Un ambito di `5` estende la portata a un sito, in genere un'intera rete aziendale.
- Un ambito di `8` estende la portata a un'organizzazione, consentendo la consegna in tutte le sottoreti della stessa entità.
- Uno scope di `e` (14 in esadecimale) indica una portata globale, rendendo il gruppo multicast accessibile da qualsiasi punto di Internet se l'infrastruttura di routing lo supporta.


La struttura di un Address multicast IPv6 comprende:


- un campo _Flag_ (4 bit) specifica se il gruppo è permanente o temporaneo,
- un campo _Scope_ (4 bit) definisce l'ambito,
- un campo di identificazione (112 bit) che identifica il numero del gruppo multicast.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Un noto esempio di multicast IPv6 in azione è il _Neighbor Discovery Protocol_ (NDP). Invece di usare ARP come in IPv4, NDP si basa su indirizzi multicast come `ff02::1:ff00:0/104` per trasmettere richieste di neighbor discovery, indirizzate solo agli host rilevanti sullo stesso link.


Definendo in modo così preciso gli ambiti Address, l'IPv6 struttura il modo in cui i flussi di dati vengono inviati, ricevuti e instradati. Questa granularità rende il protocollo più flessibile ed efficiente per la gestione delle comunicazioni locali e globali, evitando gli svantaggi del broadcasting generalizzato.


## Address Assignment in una rete locale


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


In questo capitolo esamineremo uno degli aspetti più pratici dell'implementazione dell'IPv6: l'assegnazione degli indirizzi IP agli host di una rete locale. L'architettura IPv6 è stata progettata per essere flessibile, consentendo a ogni dispositivo di assegnare automaticamente il proprio generate, pur permettendo una configurazione completamente manuale quando necessario.


Una rete locale IPv6 divide sistematicamente il Address in due parti:


- i primi 64 bit rappresentano il prefisso della sottorete, solitamente fornito da un router o da un'autorità Address;
- i restanti 64 bit vengono utilizzati dall'host per identificarsi in modo univoco su quel segmento.

Questo modello semplifica notevolmente l'aggregazione delle rotte e la gestione dei blocchi Address.


Per assegnare gli indirizzi ai dispositivi si utilizzano due approcci principali:


- Configurazione manuale, in cui l'amministratore specifica l'esatto Interface di ogni Address;
- Configurazione automatica, in cui i dispositivi generate o ottengono dinamicamente i propri indirizzi.


Nella configurazione manuale, l'amministratore assegna il Address IPv6 completo a ciascun Interface. Alcuni valori rimangono riservati:


- `::/128`: Address non specificato, mai assegnato in modo permanente ;
- `::1/128`: loopback Address (_loopback_), equivalente IPv4: `127.0.0.1`.


A differenza di IPv4, non esiste il concetto di _broadcast_; le combinazioni "tutti zeri" o "tutti uno" nella parte host non hanno un significato speciale.

La configurazione manuale è ancora utile in ambienti controllati, ma diventa difficile da mantenere in scala.


Per la configurazione automatica esistono diversi metodi:


- Il protocollo **NDP** (_Neighbor Discovery Protocol_), specificato da RFC4862, consente l'autoconfigurazione *stateless*. In questa modalità, l'host riceve un prefisso di rete da un router locale e compila il Address stesso con un identificatore basato sul suo MAC Address. Questo metodo è semplice da implementare e non richiede un server centrale.
- Le implementazioni come quelle di Windows possono generate la parte host in modo pseudo-casuale per migliorare la privacy evitando l'esposizione diretta del MAC Address. La rivelazione del MAC Address nei pacchetti IPv6 può sollevare problemi di privacy, in quanto consente di tracciare un dispositivo su reti diverse.
- Protocollo DHCPv6: Definito in RFC3315 e simile al DHCP utilizzato per IPv4, consente una configurazione più controllata e centralizzata, compresa la gestione dei lease, le opzioni extra (DNS, MTU...) e la registrazione dei database. Il DHCPv6 può funzionare da solo o insieme alla configurazione stateless per fornire parametri aggiuntivi senza assegnare il Address IP stesso.


**Nota importante: ** Nel metodo basato sul MAC, il MAC Address viene convertito in un identificatore a 64 bit utilizzando il formato EUI-64. Questo meccanismo inserisce i byte `FF:FE` al centro del MAC Address originale (in 48 bit) e inverte il 7° bit per indicare l'unicità globale. Il risultato è un identificatore Interface stabile, utilizzato nel Address IPv6 completo.


Ecco un esempio di come trasformare un MAC Address in EUI-64:


![Image](assets/fr/045.webp)



Tuttavia, a causa delle crescenti preoccupazioni sulla tracciabilità dei dispositivi, i sistemi operativi moderni (in particolare Linux, Windows 10+, macOS, Android) ora abilitano le estensioni per la privacy per impostazione predefinita. Queste utilizzano identificatori Interface generati in modo casuale e rinnovati periodicamente per le connessioni in uscita, mantenendo un identificatore stabile per le comunicazioni interne (come DNS o DHCPv6).


Come nel caso del DHCP in IPv4, gli indirizzi IPv6 assegnati automaticamente possono avere due durate, definite dai router o dai server DHCPv6:


- Durata preferita*: dopo questo periodo, il Address rimane valido, ma non viene più utilizzato per avviare nuove connessioni;
- Durata valida*: allo scadere di questo tempo, il Address viene completamente rimosso dalla configurazione del Interface.


Questo sistema consente di gestire dinamicamente i cambiamenti della rete, ad esempio garantendo una transizione senza problemi da un ISP all'altro. Aggiornando il prefisso annunciato dai router e adattando i record DNS in parallelo, la migrazione IPv6 può essere effettuata senza alcuna interruzione del servizio.


**Suggerimento:** L'uso combinato di Address e dei cicli di vita DNS consente di implementare una strategia di transizione graduale, in cui le nuove connessioni passano a una nuova topologia, mentre quelle esistenti continuano fino alla loro fine naturale.


In breve, l'IPv6 offre un'ampia gamma di flessibilità per il Address Assignment: configurazione manuale, autoconfigurazione stateless o stateful, DHCPv6 o generazione casuale. Ogni approccio presenta vantaggi e limiti e può essere adattato in base al livello di controllo richiesto, alle dimensioni della rete o alle esigenze di privacy.


## Assegnazione dei blocchi IPv6 Address


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Distribuzione Address


Lo schema di assegnazione del Address IPv6 è stato strutturato per soddisfare due obiettivi: garantire l'unicità del Address globale e consentire una gerarchia logica che favorisca l'aggregazione e la semplificazione delle tabelle di routing.

Come per l'IPv4, la *Internet Assigned Numbers Authority* (IANA) si trova al vertice di questa gerarchia. Gestisce lo spazio unicast globale Address e delega i blocchi Address ai cinque registri regionali di Internet (_RIR_).


I cinque RIR esistenti sono:


- ARIN (Nord America),
- RIPE NCC (Europa, Medio Oriente, Asia Centrale),
- APNIC (Asia-Pacifico),
- AFRINIC (Africa),
- LACNIC (America Latina e Caraibi).


La IANA assegna a ciascun RIR blocchi IPv6 di dimensioni variabili, generalmente comprese tra /23 e /12. Questo approccio offre flessibilità, garantendo al contempo la scalabilità a lungo termine. I RIR, a loro volta, ridistribuiscono questi blocchi agli Internet Service Provider (ISP), alle grandi aziende e alle istituzioni pubbliche.


Dal 2006, ogni RIR riceve dalla IANA un blocco IPv6 /12, una dimensione fissa pensata per garantire una riserva stabile e sufficientemente ampia per la crescita futura. I RIR di solito li suddividono in blocchi /23, /26 o /29. Gli ISP ricevono più spesso blocchi /32, anche se questa dimensione può variare a seconda delle dimensioni e dell'area geografica dell'ISP. In genere assegnano ai clienti blocchi /48. Ogni /48 fornisce 65.536 sottoreti /64 distinte (una capacità enorme rispetto all'IPv4).


**Nota importante:** un blocco /32 contiene esattamente 65.536 sottoblocchi /48. Ciò significa che ogni ISP può servire decine di migliaia di clienti senza esaurire la propria allocazione. Grazie al suo /48, ogni cliente avrà poi a disposizione una quantità gigantesca di spazio per strutturare la propria rete interna con tutti i segmenti /64 che desidera.


La gerarchia di allocazione tipica è la seguente:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Con questa abbondanza di indirizzi, il NAT (*Network Address Translation*), un tempo essenziale in IPv4 per far fronte alla carenza di Address, non è più necessario. Ogni host può avere un Address pubblico unico e instradabile a livello globale, semplificando la connettività end-to-end e rendendo più facile l'uso di protocolli come IPSec, VoIP o connessioni in entrata.


Per verificare a quale organizzazione appartiene un IPv6 Address, è possibile utilizzare il comando `whois` per interrogare i database RIR pubblici. Questa trasparenza consente di identificare l'organizzazione che possiede un prefisso, il che può essere utile per scopi di rete, analisi o sicurezza.


### Indirizzamento PA vs PI


In origine, il modello di allocazione dell'IPv6 era basato esclusivamente su blocchi PA (*Provider Aggregatable*), ovvero legati all'ISP. In questo modello, un'organizzazione riceve il proprio prefisso dal proprio ISP, il che significa che cambiare provider richiede la rinumerazione dell'intera infrastruttura.


Sebbene le funzioni di autoconfigurazione dell'IPv6 e i tempi di vita del Address rendano più semplice la rinumerazione, questa rimane scomoda per le organizzazioni con infrastrutture critiche o connessioni a più provider per esigenze di ridondanza.


Dal 2009, le politiche di allocazione consentono i blocchi PI (*Provider Independent*). Questi blocchi (generalmente di dimensioni /48) sono assegnati direttamente a un'azienda o a un'istituzione da un RIR, indipendentemente da qualsiasi ISP. Questo modello è particolarmente adatto alle organizzazioni che praticano il *multihoming* (cioè che si collegano a più operatori contemporaneamente). In Europa, ad esempio, il RIPE-512 definisce la politica di assegnazione delle PI.


### Notazione della maschera di sottorete


Come nell'IPv4, l'IPv6 utilizza il CIDR (*Classless Inter-Domain Routing*). Consiste nell'indicare il numero di bit che compongono il prefisso dopo il Address, utilizzando il carattere `/`.


Prendiamo il seguente esempio:


```
2001:db8:1:1a0::/59
```


Ciò significa che i primi 59 bit sono fissi e identificano la rete. Tutti i bit rimanenti (qui 69 bit) possono essere utilizzati per identificare sottoreti o host.


Pertanto, questa notazione copre gli indirizzi da `2001:db8:1:1a0:0:0:0` a `2001:db8:1:1bf:ffff:ffff:ffff`.


Questo blocco copre quindi un insieme di 8 sottoreti /64, ciascuna in grado di ospitare un numero enorme di dispositivi.


La notazione CIDR consente una pianificazione precisa dello spazio Address, dalle reti su larga scala alle configurazioni domestiche e agli ambienti virtualizzati, e incoraggia l'aggregazione delle rotte, riducendo il carico dei router e migliorando la scalabilità.


### Pacchetti e intestazioni IPv6


Il formato dei pacchetti IPv6 si differenzia da quello IPv4 per essere più semplice e più estensibile. Un datagramma IPv6 inizia sempre con un'intestazione di 40 byte di dimensioni fisse, contenente tutte le informazioni di routing essenziali. Questo approccio semplificato, rispetto alla lunghezza variabile dell'intestazione di IPv4 (da 20 a 60 byte), consente un'elaborazione più rapida ed efficiente dei pacchetti da parte dei router.


Tuttavia, IPv6 non elimina le funzionalità: invece di integrare numerosi campi opzionali nell'intestazione principale, introduce un sistema di intestazioni di estensione, collocate immediatamente dopo l'intestazione di base. Queste intestazioni opzionali consentono di aggiungere dati o istruzioni specifiche per determinate funzioni, senza appesantire inutilmente i pacchetti ordinari.


Alcune intestazioni di estensione seguono una struttura fissa, mentre altre possono contenere un numero variabile di opzioni. In Queste opzioni sono codificate come triplette `{Type, Length, Value}`:


- Il campo "Tipo" (1 byte) indica la natura dell'opzione;
- I primi due bit del "Tipo" specificano cosa devono fare i router se l'opzione non viene riconosciuta:
 - Ignorare l'opzione e continuare il trattamento,
 - Abbandona il datagramma,
 - Drop e invio di un errore ICMP all'origine.
 - Eliminare il datagramma senza notifica (nel caso di pacchetti multicast).
- Il campo "Lunghezza" (1 byte) specifica la dimensione del campo "Valore", da 0 a 255 byte;
- Il campo "Valore" contiene i dati associati all'opzione.


Ecco una panoramica dei diversi tipi di intestazioni di estensione definiti da IPv6.


#### Intestazione Hop-by-Hop


Questa intestazione, se presente, è sempre collocata subito dopo l'intestazione di base. Contiene informazioni che devono essere elaborate da ogni router lungo il percorso del pacchetto, a differenza della maggior parte delle altre intestazioni, che di solito sono gestite solo dal nodo di destinazione. Gli usi tipici includono la segnalazione di parametri globali o la richiesta di specifiche fasi di elaborazione durante il percorso del pacchetto.


![Image](assets/fr/047.webp)


#### Intestazione di routing


L'intestazione di instradamento specifica un elenco di indirizzi intermedi attraverso cui il pacchetto deve passare. Esistono due modalità di instradamento principali:


- Strict routing: il percorso esatto è predefinito
- Routing libero: vengono specificati solo alcuni passaggi obbligatori.


I primi quattro campi di questa intestazione di rooting sono:


- Intestazione successiva**: identifica il tipo di intestazione successiva;
- Tipo di instradamento**: definisce il metodo di instradamento (di solito `0`);
- Segmenti rimasti**: numero di segmenti ancora da attraversare ;
- Address[n]**: elenco degli indirizzi intermedi.


Il campo "Segmenti rimasti" inizia con il numero totale di segmenti rimanenti e viene decrementato di uno a ogni hop.


![Image](assets/fr/048.webp)


#### Intestazione di frammentazione


In IPv6, solo l'host sorgente è autorizzato a frammentare un datagramma, a differenza di IPv4 dove anche i router potevano farlo. Tutti i nodi IPv6 devono essere in grado di gestire pacchetti di almeno 1280 byte. Se un router incontra un pacchetto più grande dell'MTU del collegamento successivo, invia un messaggio *ICMPv6 Packet Too Big* all'origine, che quindi adatta le dimensioni delle sue trasmissioni.


L'intestazione di frammentazione contiene i seguenti campi:


- Identificazione**: identificatore unico del datagramma per il riassemblaggio.
- Fragment Offset**: posizione del frammento all'interno del datagramma originale.
- Flag M**: indica se seguono altri frammenti.


![Image](assets/fr/049.webp)


#### Intestazione di autenticazione (AH)


Questa intestazione è progettata per proteggere le comunicazioni verificando sia l'autenticità del mittente che l'integrità dei dati. È comunemente utilizzata con il protocollo IPsec. Utilizzando un codice di autenticazione, il destinatario può confermare che il messaggio proviene veramente dal mittente previsto e che non è stato alterato durante il transito.


In caso di tentativo di modifica fraudolenta, il codice di autenticazione non corrisponderà più e il datagramma potrà essere rifiutato. Questo meccanismo protegge anche dagli attacchi di replay, rilevando le duplicazioni non autorizzate.


![Image](assets/fr/050.webp)


#### Intestazione delle opzioni di destinazione


Questa intestazione è destinata solo al destinatario finale del datagramma. Può essere utilizzata per aggiungere opzioni o metadati specifici dell'applicazione, senza che i router intermedi ne tengano conto.


Inizialmente, il protocollo non prevedeva alcuna opzione di questo tipo. Tuttavia, questa intestazione è stata introdotta durante la progettazione di IPv6, per consentire l'aggiunta di future estensioni senza modificare la struttura complessiva del pacchetto. L'opzione null, ad esempio, viene utilizzata solo per riempire l'intestazione con un multiplo di 8 byte per l'allineamento della memoria.


![Image](assets/fr/051.webp)


La progettazione dei pacchetti IPv6 si basa su una netta separazione tra un'intestazione di base minima e intestazioni di estensione modulari. Questa architettura garantisce sia prestazioni di elaborazione standard sia la flessibilità necessaria per far evolvere il protocollo e integrare meccanismi di sicurezza, di routing complesso o di qualità del servizio, mantenendo la compatibilità con le infrastrutture future.


## Relazione tra IPv6 e DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


Nelle reti moderne, il DNS (*Domain Name System*) traduce i nomi di dominio in indirizzi IP utilizzabili dalle macchine. Con l'introduzione dell'IPv6, il DNS ha dovuto adattarsi per supportare gli indirizzi a 128 bit mantenendo la retrocompatibilità con l'IPv4. Questa coesistenza è particolarmente importante negli ambienti dual-stack, dove entrambe le versioni IP operano contemporaneamente.


### Record DNS specifici per IPv6


Per associare un nome di dominio a un Address IPv6, il DNS utilizza un record AAAA (*quad-A*), analogo al record "A" per gli indirizzi IPv4. Il record AAAA mappa esplicitamente un nome di dominio a un Address IPv6.

Esempio:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Questo record indica che il dominio `ipv6.mydmn.org` si risolve al Address IPv6 `2001:66c:2a8:22::c100:68b`. È possibile, e persino consigliato per la massima compatibilità, associare lo stesso nome di dominio a diversi indirizzi IP, sia IPv4 (tramite un record A) che IPv6 (tramite un record AAAA). Ciò consente ai clienti compatibili con l'IPv6 di preferire l'IPv6, garantendo al contempo il supporto dei client solo IPv4.


Inoltre, il DNS supporta la risoluzione inversa, ovvero può cercare il nome di dominio associato a un determinato IP Address. Nel caso di IPv6, questa operazione utilizza i record PTR collocati nella zona `ip6.arpa`. Questa zona è riservata specificamente alla risoluzione inversa di IPv6. Per IPv4, è la zona `in-addr.arpa`.


### Risoluzione inversa


La risoluzione inversa di un IPv6 Address segue un processo rigoroso:

1) Espandere il Address in notazione esadecimale completa (16 byte, cioè 32 cifre esadecimali).

Esempio:


```shell
2001:66c:2a8:22::c100:68b
```


Diventa:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Invertire l'ordine di ogni cifra esadecimale (nibble), separarli con dei punti e aggiungere `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Questa struttura garantisce ricerche inverse standardizzate e uniche nello spazio IPv6 Address.


**Nota bene**: Le query DNS possono viaggiare sia su IPv4 che su IPv6. Il protocollo di trasporto utilizzato non ha alcun effetto sul tipo di record restituiti.

Ad esempio:


- Un client connesso tramite IPv6 può richiedere un record IPv4.
- Un client connesso tramite IPv4 può richiedere un record IPv6.

Il server DNS risponde semplicemente con i record che possiede, indipendentemente dal protocollo di trasporto della query.


Quando un nome host è mappato sia su IPv4 che su IPv6, la scelta di quale Address utilizzare è regolata dalla RFC 6724, che definisce un algoritmo di selezione Address basato su fattori quali la preferenza del prefisso, l'ambito e la raggiungibilità. Per impostazione predefinita, IPv6 è generalmente preferito, a meno che non venga sovrascritto dalla configurazione del sistema o della rete.


**Ricordo importante**: quando si inserisce un Address IPv6 in un URL (*Uniform Resource Locator*), questo deve essere racchiuso tra parentesi quadre (`[]`). In questo modo si evita la confusione tra i due punti (`:`) all'interno del Address IPv6 e i due punti che separano il nome dell'host dalla porta nell'URL.


Esempio valido:


```shell
http://[2001:db8::1]:8080
```


Questo assicura che l'URL venga elaborato correttamente sia dai browser che dai server web.


L'integrazione dell'IPv6 nel sistema DNS richiede quindi nuovi tipi di record, un metodo rigoroso per la risoluzione inversa e regole precise di selezione e formattazione per garantire la compatibilità e la coerenza del routing.


### Riassunto della parte


In questa sezione abbiamo esplorato i principi fondamentali dell'indirizzamento IPv6. Abbiamo iniziato esaminando la struttura di IPv6 Address: la sua lunghezza di 128 bit, la notazione esadecimale e le regole di semplificazione utilizzate per abbreviare le sequenze ripetitive di zeri. Questa struttura consente a IPv6 di superare le limitazioni dello spazio Address di IPv4, garantendo al contempo scalabilità e gerarchia efficiente.


Abbiamo quindi esaminato le diverse categorie di indirizzi IPv6: unicast, anycast e multicast, descrivendone in dettaglio la portata, l'uso tipico e la rappresentazione nello spazio Address.


Successivamente, sono stati esaminati i metodi di assegnazione degli indirizzi IPv6 all'interno di una rete locale, sia tramite configurazione manuale, sia tramite il protocollo DHCPv6, sia tramite meccanismi di autoconfigurazione stateless come quelli offerti da NDP. Questi approcci consentono ai dispositivi di assegnare automaticamente il proprio Address a partire dal prefisso fornito e dal proprio MAC Address (tramite EUI-64), offrendo al contempo flessibilità in termini di gestione del tempo di vita e di privacy.


Abbiamo anche descritto in dettaglio come vengono assegnati i blocchi Address, a partire dalla IANA, che li distribuisce ai cinque RIR (*Registered Internet Regions*), e poi agli ISP, che li ridistribuiscono ai loro clienti come sottoreti (spesso in /48, consentendo 65536 sottoreti /64). La distinzione tra blocchi _Provider Aggregatable_ (PA) e _Provider Independent_ (PI) aiuta a gestire gli scenari di _multihoming_ o di cambio di provider.


Abbiamo visto che il DNS si è adattato all'IPv6 con l'introduzione del record AAAA e che i meccanismi di risoluzione inversa si basano ora sulla zona `ip6.arpa`. È importante notare che il DNS rimane indipendente dal protocollo di trasporto utilizzato (IPv4 o IPv6), garantendo una perfetta interoperabilità in un ambiente dual-stack.


L'IPv6 non è quindi solo un miglioramento incrementale rispetto all'IPv4, ma una riprogettazione completa del sistema di indirizzamento, costruita per rispondere alle sfide attuali e future dell'Internet globale.


Nella parte finale di questo corso NET 302, passeremo alla pratica e ci concentreremo sugli strumenti di diagnostica di rete.



# Strumenti di diagnostica di rete


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Strumenti di accesso alla rete Layer


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


In questo primo capitolo della sezione finale sulla diagnostica di rete, ci concentriamo sugli strumenti per analizzare l'accesso alla rete Layer del modello TCP/IP. Questo Layer è responsabile della comunicazione diretta tra i dispositivi sulla stessa rete fisica, in particolare attraverso l'uso di indirizzi MAC e interfacce di rete fisiche come le schede Ethernet o le interfacce Wi-Fi.


L'obiettivo è fornire agli amministratori strumenti pratici per ispezionare, testare e ottimizzare questa essenziale Layer connettività di basso livello. Questi strumenti possono essere utilizzati per verificare il corretto funzionamento delle interfacce, risolvere i problemi di configurazione delle schede di rete o rilevare anomalie come collisioni, perdita di pacchetti o errori di collegamento.


### Utilità di quartiere IP/MAC


#### strumento `Arp


Uno degli strumenti diagnostici più vecchi del Network Access Layer è il comando `arp'. Sebbene sia sempre più spesso sostituito da alternative moderne come `ip neigh` (che scopriremo a breve). `Arp` è ancora presente su molti sistemi per visualizzare o manipolare la cache ARP (*Address Resolution Protocol*). Questa cache memorizza le mappature tra gli indirizzi IP e gli indirizzi MAC conosciuti localmente su una macchina. In altre parole, consente di determinare quale Address fisico (MAC) corrisponde a un determinato Address IP sulla rete locale.


In pratica, quando un host vuole inviare un pacchetto a un IP Address all'interno della stessa sottorete, deve prima conoscere il MAC Address della macchina di destinazione. Questa mappatura è gestita da ARP, che trasmette una richiesta sulla rete locale e riceve una risposta contenente il MAC Address corrispondente. Il risultato viene poi memorizzato temporaneamente in una tabella locale chiamata "ARP cache", per evitare di ripetere le richieste per ogni nuovo pacchetto.


Per visualizzare il contenuto di questa cache e controllare le voci attualmente note alla macchina, utilizzare:


```bash
arp -a
```


Questo comando elenca tutte le mappature IP/MAC registrate localmente, su tutte le interfacce. Ogni riga fornisce il nome dell'host (se risolvibile), il Address IP, il Address MAC corrispondente e il Interface in cui è stata osservata la mappatura.


Per filtrare la visualizzazione su un IP Address specifico, è sufficiente specificarlo:


```bash
arp -a 192.168.1.5
```


In questo modo è facile verificare se un particolare IP Address è presente nella cache, il che può aiutare a diagnosticare errori di comunicazione tra due host sulla stessa rete.


Allo stesso modo, per visualizzare solo le voci ARP associate a una specifica rete Interface (ad esempio una scheda Ethernet denominata `eth0`), è possibile utilizzare:


```bash
arp -a -i eth0
```


Ciò è particolarmente utile negli ambienti multi-Interface (cablati, wireless, VPN, ecc.), dove un host può avere diversi adattatori di rete.


Il comando `arp` non è limitato all'uso in sola lettura. Può anche essere usato per modificare manualmente la cache ARP, una funzione preziosa in alcuni scenari avanzati di risoluzione dei problemi o quando si simulano condizioni specifiche. Ad esempio, è possibile aggiungere manualmente una mappatura IP/MAC:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Questo comando crea una voce statica nella tabella ARP locale, associando l'IP Address `192.168.1.7` al MAC Address `00:17:BC:56:4F:25` sul Interface `eth2`.Se non viene specificato alcun Interface, il sistema utilizza automaticamente il primo applicabile.


È anche possibile rimuovere una voce dalla cache ARP, sia per correggere un errore sia per forzare una riscoperta:


```bash
arp -d 192.168.1.7
```


Questa operazione cancella la voce, assicurando che il successivo tentativo di comunicazione attivi una nuova richiesta ARP.


**NOTA**: L'opzione di cancellazione accetta anche un nome Interface, consentendo di indirizzare in modo più preciso la rimozione di una voce specifica.


In sintesi, lo strumento `arp` fornisce una diagnostica di basso livello, particolarmente utile nelle reti locali dove i problemi di connettività possono spesso essere ricondotti a una risoluzione Address errata o obsoleta. Tuttavia, nei sistemi recenti, in particolare nelle moderne distribuzioni Linux, questo strumento viene sempre più spesso sostituito dal comando `ip neigh`, del set di strumenti `iproute2`, che offre funzionalità simili in un quadro più unificato.


#### strumento `Ip neighbor


Nei sistemi moderni, in particolare nelle recenti distribuzioni di Linux, il comando `ip neigh` è lo strumento principale per ispezionare e gestire le mappature tra indirizzi IP e MAC. Questo comando fa parte della suite `iproute2`, che sta gradualmente sostituendo strumenti più vecchi come `arp`, fornendo un quadro più coerente e flessibile per la diagnostica del data link Layer.


Il comando `ip neigh` interroga la cache dei vicini IP locali, che è equivalente alla cache ARP per IPv4 e alla cache NDP (_Neighbor Discovery Protocol_) per IPv6. Questa cache memorizza le associazioni note tra indirizzi IP (v4 o v6) e indirizzi MAC, insieme al loro stato (valido, in attesa, scaduto...).


Il comando di base per visualizzare la cache è:


```bash
ip neigh
```


Questo produce un elenco di voci, che mostra l'IP di destinazione Address, la rete pertinente Interface, il MAC Address associato (se disponibile) e lo stato della voce (ad esempio, `REACHABLE', `STALE', `DELAY', `FAILED'...).


Esempio di uscita:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Questa riga indica che la macchina conosce una mappatura valida tra l'IP Address `192.168.1.5` e il MAC Address `00:17:BC:56:4F:25` tramite il Interface `eth0`.


È anche possibile filtrare le voci in base a criteri quali IP Address, Interface o stato. Ad esempio, per interrogare solo il Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


Oppure per visualizzare tutte le voci per Interface `eth1`:


```bash
ip neigh show dev eth1
```


Oltre alla consultazione, `ip neigh` può essere usato anche per modificare manualmente la cache. Ad esempio, per aggiungere una voce statica:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Associa in modo permanente l'IP Address `192.168.1.7` al MAC Address specificato sul Interface `eth1`. L'opzione `nud permanent` (per _Neighbor Unreachability Detection_) assicura che la voce non venga automaticamente invalidata.


Al contrario, per eliminare una voce della cache:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Questo costringe il sistema a risolvere nuovamente la mappatura la volta successiva che comunica con quel Address.


**NOTA**: Lo strumento `ip neigh` funziona sia per IPv4 che per IPv6. Per IPv4, si interfaccia con ARP; per IPv6, interagisce con NDP. Questo fornisce un approccio unificato e coerente alla gestione delle relazioni IP/MAC in tutte le famiglie di protocolli, rendendo `ip neigh` il moderno standard per la gestione dei vicini sui sistemi Linux.


### Strumenti di analisi del pacchetto


Per analizzare a fondo ciò che accade in una rete di computer, gli amministratori hanno bisogno di strumenti in grado di catturare i pacchetti scambiati tra le macchine. Due utility spiccano come punti di riferimento: `tcpdump` e `Wireshark`. Questi strumenti sono essenziali per diagnosticare comportamenti anomali, verificare gli scambi di protocollo o studiare la sicurezza della rete ispezionando il contenuto dei frame.


#### `ttcpdump`: analisi a riga di comando


`tcpdump` è uno strumento a riga di comando molto potente, progettato per catturare e visualizzare i pacchetti che viaggiano attraverso una rete Interface . Opera in tempo reale e, grazie alla sua struttura leggera, può essere utilizzato su sistemi privi di grafica Interface o con risorse limitate. Si basa sulla libreria `libpcap`, che fornisce funzioni di cattura a basso livello indipendenti dall'hardware.


Un uso comune di `tcpdump` è quello di monitorare l'attività di rete di una macchina o di un segmento di rete, filtrando i pacchetti in base a criteri specifici. I risultati possono essere reindirizzati a un file, consentendo di archiviare il traffico per un'analisi successiva o di riprodurlo con un altro strumento, come Wireshark.


La sintassi generale del comando è la seguente:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` scrive i pacchetti catturati in un file in formato `libpcap` (estensione `.cap` o `.pcap`);
- `-i` specifica la rete Interface da monitorare (ad esempio, `eth0`, `wlan0`);
- `-s` imposta la quantità massima di dati catturati per pacchetto. Specificando `0` si catturano tutti i pacchetti;
- `-n` disabilita la risoluzione dei nomi DNS e dei servizi, migliorando le prestazioni.


I filtri di espressione alla fine del comando consentono di limitare le catture a un sottoinsieme di traffico. È possibile combinare le parole chiave `host`, `port`, `src`, `dst`, ecc. per affinare la selezione.


Esempio: catturare pacchetti HTTP (porta 80) da o verso il server `192.168.25.24` e salvarli in un file `fichier.cap`:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Il file risultante può essere successivamente analizzato con uno strumento grafico o riprodotto su un altro sistema.


#### Wireshark: analisi visiva avanzata


Wireshark, precedentemente noto come *Ethereal*, è un programma completo di analisi di rete con un Interface grafico. A differenza di `tcpdump`, fornisce una visualizzazione strutturata e dettagliata dei pacchetti, compresa la dissezione dei protocolli, i grafici di flusso, le statistiche sul traffico e i filtri interattivi. Si basa inoltre su `libpcap`, il che significa che può aprire ed elaborare i file di acquisizione generati da `tcpdump`.


Wireshark è disponibile su molti sistemi operativi, compresi Linux e Windows. L'installazione richiede i privilegi di amministratore per accedere alle interfacce di acquisizione. Una volta avviato, è possibile selezionare una rete Interface dal menu *Capture*. Facendo clic su *Avvio* si avvia la registrazione dei pacchetti in tempo reale. Il display è diviso in tre riquadri:


- l'elenco dei fotogrammi catturati ;
- dettagli decodificati dal protocollo,
- dati esadecimali grezzi.



![Image](assets/fr/052.webp)



Wireshark eccelle negli scenari in cui è necessario osservare il comportamento di protocolli complessi, ricostruire le finestre di dialogo delle applicazioni (come una sessione HTTP o DNS) o studiare i tempi di risposta dei servizi. Supporta anche filtri di visualizzazione altamente specifici utilizzando la sua sintassi dedicata (diversa da quella di `tcpdump`) per concentrarsi solo sui pacchetti rilevanti.


#### Strumenti complementari


È importante notare che `tcpdump` e Wireshark non sono intercambiabili: ognuno ha i suoi punti di forza. `tcpdump` è più adatto agli ambienti a riga di comando, agli script automatici e agli interventi sui server remoti, mentre Wireshark è ideale per l'analisi dettagliata, interattiva e didattica del traffico.


I due strumenti possono essere combinati: è possibile effettuare una cattura su un sistema remoto con `tcpdump`, quindi trasferire il file `.cap` per analizzarlo con Wireshark su una macchina locale. Questo approccio è ampiamente utilizzato nella pratica.


### Strumenti di analisi Interface


Nel Network Access Layer è spesso necessario interrogare e configurare le interfacce fisiche di rete per diagnosticare malfunzionamenti, ottimizzare le prestazioni o verificare l'integrità della connessione. Uno degli strumenti più potenti disponibili in Linux a questo scopo è `ethtool`, un'utilità a riga di comando che non solo fornisce informazioni tecniche dettagliate su un Ethernet Interface, ma consente anche di regolare alcuni dei suoi parametri in tempo reale.


#### Visualizza le specifiche del Interface


Una caratteristica fondamentale di `ethtool` è la capacità di interrogare un Interface e di visualizzarne le caratteristiche attuali. Ciò consente di verificare:


- velocità del collegamento (ad esempio 100 Mbit/s, 1 Gbit/s o 10 Gbit/s) ;
- modalità di negoziazione (half duplex o full duplex) ;
- se l'autonegoziazione è abilitata;
- il tipo di porta (rame, fibra, ecc.) ;
- stato del collegamento (attivo o meno) ;
- supporto di funzioni avanzate come il *Wake-on-LAN*.


Queste informazioni sono particolarmente utili per diagnosticare problemi legati alla connettività fisica o alle impostazioni di negoziazione non corrispondenti tra la scheda di rete dell'host e l'apparecchiatura a cui si collega (switch, router, ecc.).


Per ottenere queste informazioni, è sufficiente eseguire:


```bash
ethtool enp0s3
```


Questo comando produce un rapporto dettagliato su `enp0s3` Interface, una convenzione di denominazione comune sui sistemi basati su CentOS o RHEL.



![Image](assets/fr/053.webp)



#### Modificare dinamicamente i parametri del Interface


`ethtool` non si limita all'osservazione: consente anche di regolare alcuni parametri del Interface senza riavviare la macchina. Ciò consente, ad esempio, di forzare una velocità di collegamento specifica o di attivare funzioni in base alle esigenze della rete locale.


L'opzione `-s` viene utilizzata per configurare dinamicamente parametri quali:


- velocità del collegamento (`speed`), impostata esplicitamente (ad es. 1000 per 1 Gbit/s) ;
- modalità duplex (`duplex`), `mezzo` o `pieno` ;
- abilitare o disabilitare l'autonegoziazione (`autoneg`) ;
- abilitazione di *Wake-on-LAN* (`wol`) ;
- tipo di porta.


Esempio 1: abilitare l'autonegoziazione su un Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Esempio 2: attivare la funzione *Wake-on-LAN* (per consentire alla macchina di svegliarsi da remoto tramite un pacchetto magico):


```bash
ethtool -s enp0s3 wol p
```


In questo esempio, l'opzione `p` specifica che il risveglio avverrà non appena viene rilevato un pacchetto *Wake-on-LAN*. Questa configurazione è spesso usata in ambienti aziendali per eseguire aggiornamenti notturni o manutenzione remota.


#### Installazione degli strumenti


È importante notare che `ethtool` non è sempre installato per default. Sulle distribuzioni Red Hat/CentOS, può essere installato con il comando:


```bash
yum install -y ethtool
```


Su Debian e Ubuntu, il comando equivalente è:


```bash
sudo apt install ethtool
```


**ATTENZIONE**: in tutti i comandi `ethtool`, il nome della rete Interface deve essere specificato subito dopo l'opzione (come `-s`). Qualsiasi errore di sintassi nella collocazione dei parametri renderà il comando non valido o inefficace.



## Strumenti di rete Layer


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Strumenti di analisi del traffico


Nella diagnostica di rete, il comando `ping` rimane uno degli strumenti più semplici ma più potenti per testare la connettività tra due macchine. Controlla se un host remoto è raggiungibile in un determinato momento, fornendo anche informazioni sulla latenza, sulla stabilità del collegamento e sulla risoluzione DNS.


Il comando `ping` si basa sul protocollo ICMP (*Internet Control Message Protocol*). Quando un utente invia una richiesta `ping`, il sistema invia un pacchetto ICMP "Echo Request" a un Address IP o a un nome host. Se il computer di destinazione è online e il percorso di rete è valido, risponde con un pacchetto ICMP "Echo Reply". Questo semplice meccanismo può essere utilizzato per misurare la latenza e rilevare problemi di connettività o di risoluzione dei nomi.


Esempio di comando classico:


```bash
ping 172.17.18.19
```


Risposta tipica:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


In questo esempio, la risoluzione del nome è stata eseguita automaticamente: il dominio `mydmn.org` è associato all'IP Address `172.17.18.19`, confermando che la risoluzione DNS funziona correttamente. Il comando fornisce anche dettagli tecnici quali:


- numero di sequenza iCMP (`icmp_seq`), utile per controllare l'ordine delle risposte;
- TTL (*Time-To-Live*), che indica il numero di hop rimanenti prima che il pacchetto venga scartato;
- tempo/ritardo di andata e ritorno (`time`), espresso in millisecondi, che fornisce una stima della latenza del collegamento.


#### Analisi più dettagliata dei parametri ICMP


Il TTL è un campo critico del protocollo IP. Ogni datagramma viene inizializzato con un valore TTL dal mittente (spesso 64, 128 o 255). Ogni router lungo il percorso decrementa questo valore di 1. Se il TTL raggiunge lo 0 prima di arrivare a destinazione, il pacchetto viene scartato e al mittente viene restituito un errore ICMP. Questo meccanismo previene i loop di instradamento infiniti.


Il tempo di propagazione (*round-trip delay/time*) misura il ritardo con cui un pacchetto lascia il mittente, raggiunge la destinazione e ritorna. In pratica, un ritardo inferiore a 200 ms è considerato accettabile per un collegamento stabile. Ritardi anormalmente elevati possono indicare una congestione della rete, un instradamento inefficiente o una scarsa qualità del collegamento.


#### Uso avanzato di `ping


`ping` fornisce opzioni per affinare i test e osservare comportamenti specifici della rete.


Per inviare richieste in broadcast, si può usare l'opzione `-b' per indirizzare tutti gli host di una sottorete:

```bash
ping -b 192.168.1.255
```


Questo è utile sulle reti locali per individuare rapidamente gli host attivi o per testare come la rete gestisce le richieste di broadcast. Tuttavia, in molte configurazioni, i router e i firewall bloccano i ping broadcast per evitare attacchi di amplificazione.


È anche possibile specificare un intervallo personalizzato tra le richieste con l'opzione `-i` (valore predefinito: 1 secondo):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Invia 10 richieste ICMP a intervalli di 0,2 secondi. Questo tipo di test è utile per rilevare le fluttuazioni della latenza su un breve periodo o per sollecitare leggermente un collegamento per valutarne la stabilità.


### Strumenti di analisi delle tabelle di routing


Il comando `ip route`, parte della suite `iproute2`, è lo strumento raccomandato e standard nei moderni sistemi Linux per ispezionare e gestire la tabella di routing IP del kernel. Sostituisce l'obsoleto comando `route`, offrendo una sintassi più chiara, una maggiore coerenza e un supporto esteso alle caratteristiche moderne (IPv6, tabelle multiple, spazi dei nomi, ecc.).


#### Visualizzazione della tabella di routing


Per visualizzare la tabella di routing corrente:


```bash
ip route show
```


Questo output elenca tutte le rotte conosciute dal kernel, cioè i percorsi dei pacchetti in uscita a seconda della loro destinazione.


Esempio di uscita:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Ogni riga rappresenta un percorso. I campi chiave includono:


- default**: la rotta predefinita, utilizzata quando non esiste una rotta più specifica.
- via**: il gateway utilizzato per raggiungere la destinazione.
- dev**: la rete Interface utilizzata.
- proto**: come è stata creata la rotta (manuale, DHCP, kernel, ecc.).
- metric**: costo del percorso, usato per dare priorità a più percorsi possibili.
- scope**: ambito della rotta (ad esempio, `link` per una rotta direttamente collegata).
- src**: l'IP di origine Address utilizzato per i pacchetti in uscita su questo Interface.


#### Aggiunta e cancellazione di percorsi


È anche possibile modificare la tabella di routing in modo dinamico, ad esempio aggiungendo o rimuovendo rotte statiche.


Aggiunta di un percorso statico:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Questo configura un percorso verso la rete `192.168.1.0/24`, attraverso il gateway `192.168.1.1` sul Interface `eth0`.


Rimuovere questo percorso:


```bash
ip route del 192.168.1.0/24
```


Questo comando elimina la rotta definita in precedenza.


#### Comandi utili


Ecco alcune varianti utili per l'analisi o lo scripting:


- `ip -4 route`: visualizza solo le rotte IPv4;
- `ip -6 route`: visualizza solo i percorsi IPv6;
- `ip route list table main`: visualizza la tabella di routing principale (valore predefinito) ;
- `ip route get <Address>`: mostra quale Interface e quale gateway utilizzerebbe un pacchetto diretto al Address indicato.


Esempio:


```bash
ip route get 8.8.8.8
```


Questo mostra il percorso esatto che un pacchetto farebbe per raggiungere `8.8.8.8`.


### Strumenti di tracciamento


Uno degli strumenti più efficaci per analizzare il percorso seguito dai pacchetti IP tra un host sorgente e una destinazione è il comando `traceroute`. Esso mostra, passo dopo passo, il percorso seguito dai pacchetti e identifica i router intermedi che essi attraversano. In caso di malfunzionamento di un collegamento di rete o di un'interruzione del servizio, `traceroute` aiuta a localizzare con precisione il problema.


Come per il comando `ping`, la destinazione può essere specificata con il suo nome di dominio completamente qualificato (FQDN) o con il suo IP Address . Ad esempio:


```bash
traceroute mydmn.org
```


#### Principio di funzionamento


il `traceroute` si basa sul campo TTL (*Time To Live*) nell'intestazione dei pacchetti IP. Come spiegato in precedenza, questo campo è un contatore decrementato da ogni router lungo il percorso. Quando il TTL raggiunge lo zero, il pacchetto viene scartato e il router restituisce al mittente un messaggio ICMP "Time Exceeded". Questo meccanismo previene i loop infiniti in caso di errato instradamento.


`traceroute` sfrutta questo comportamento per mappare i router tra il mittente e il destinatario:


- Prima invia una serie di pacchetti UDP (di solito tre), con un TTL di 1. Il primo router trova un TTL di 0, quindi scarta il pacchetto e risponde con un messaggio ICMP, rivelando il suo IP Address e il tempo di risposta.
- Successivamente, invia un'altra serie di pacchetti con un TTL di 2, rivelando il secondo router.
- Il processo si ripete finché non viene raggiunta la destinazione, a quel punto l'host risponde con un messaggio ICMP Port Unreachable, indicando che l'endpoint è stato raggiunto.


Per impostazione predefinita, `traceroute` utilizza pacchetti UDP inviati a porte non utilizzate (tipicamente a partire dalla 33434), ma può anche essere configurato per utilizzare ICMP (come `ping`) o persino TCP, a seconda dei sistemi o delle varianti di comando.


Esempio di uscita:


```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```


Ogni riga corrisponde a un router attraversato, con un massimo di tre misure temporali (in millisecondi) che indicano la latenza del viaggio di andata e ritorno verso quel router. Questi valori aiutano a valutare le prestazioni di ciascun segmento di rete.


#### Interpretazione dei risultati


Se un router non risponde o filtra i messaggi ICMP, vengono visualizzati degli asterischi `*` al posto del tempo di risposta. Questo può indicare:


- un firewall che blocca le risposte ICMP,
- un dispositivo configurato per non rispondere, oppure
- un problema temporaneo di connettività lungo il percorso.


Pertanto, il `traceroute` non solo identifica il percorso seguito, ma evidenzia anche i punti di latenza anomala o le interruzioni.


Su alcuni sistemi è possibile utilizzare il comando equivalente `tracepath`, che non richiede i privilegi di root. Per IPv6, utilizzare `traceroute6` o `tracepath6`.


Esempio di tracciamento IPv6:


```bash
traceroute6 ipv6.google.com
```


### Strumenti per il controllo delle connessioni attive


Per diagnosticare le connessioni di rete attive e monitorare l'attività di rete su un sistema Linux, il comando `ss` (abbreviazione di _socket statistics_) è lo strumento di riferimento moderno. Parte della suite `iproute2`, sostituisce l'ormai obsoleto `netstat`, offrendo prestazioni migliori e risultati più accurati.


`ss` visualizza le connessioni TCP e UDP attive, le porte in ascolto, gli indirizzi locali e remoti, gli stati delle connessioni e i processi associati.


#### Uso generale


Quando viene eseguito senza opzioni, il comando `ss` visualizza le connessioni TCP attive. Sintassi di base:


```bash
ss [options]
```


Alcune opzioni comuni per affinare l'analisi:


- `-t`: mostra solo le connessioni TCP;
- `-u`: mostra solo le connessioni UDP;
- `-l`: mostra solo i socket in ascolto;
- `-n`: disabilita la risoluzione dei nomi (IP grezzi e numeri di porta) ;
- `-p`: visualizza i processi associati a ciascun socket (PID e nome del programma),
- `-a`: mostra tutte le connessioni, comprese quelle inattive,
- `-s`: visualizza statistiche di alto livello sui socket.


#### Casi di studio


Per visualizzare tutte le connessioni attive che utilizzano la porta TCP 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Mostra le connessioni TCP attive che coinvolgono la porta 80. Stati come `LISTEN', `ESTABLISHED', `TIME-WAIT' indicano lo stato attuale di ciascun Exchange.


Esempio di uscita:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Per visualizzare tutte le connessioni di rete con i processi associati:


```bash
ss -tulnp
```


Per ottenere un riepilogo complessivo dell'uso dei socket:

```bash
ss -s
```


Per filtrare solo le connessioni UDP:

```bash
ss -unp
```


Questi comandi sono particolarmente utili per rilevare connessioni sospette, porte di ascolto inaspettate o per monitorare l'attività di un servizio specifico.


## Trasporto e trasporto degli strumenti Layer


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Strumenti di interrogazione DNS


Nei livelli superiori del modello TCP/IP, in particolare nell'Application Layer, è importante capire come funziona la risoluzione dei nomi. Gli strumenti di interrogazione DNS consentono di verificare se un nome di dominio è correttamente associato a un IP Address e aiutano anche a diagnosticare i problemi del server DNS, come la configurazione errata, i ritardi di propagazione o la mancata disponibilità. Questi strumenti sono essenziali per qualsiasi amministratore di rete o per qualsiasi utente che desideri una comprensione più approfondita degli scambi DNS in un ambiente IP.


#### Il comando `nslookup


Lo strumento di interrogazione DNS più semplice è `nslookup`. Invia una richiesta a un server DNS e restituisce l'IP Address associato a un nome di dominio (o viceversa). Per impostazione predefinita, interroga il server DNS configurato del sistema, ma è anche possibile specificare un server direttamente nel comando.


Esempio di ricerca diretta:

```bash
nslookup mydmn.org
```


Interrogazione di un server DNS specifico:

```bash
nslookup mydmn.org 192.6.23.4
```


La richiesta chiede al server DNS di `192.6.23.4` di risolvere il nome `mydmn.org`. È particolarmente utile per verificare se un determinato server DNS riconosce un nome di dominio o per verificare che il server funzioni correttamente.


#### Il comando `dig


`dig` (*Domain Information Groper*) è uno strumento più moderno, completo e flessibile di `nslookup`. Supporta query complesse e fornisce informazioni dettagliate sul processo di risoluzione, sulla gerarchia dei server coinvolti, sul tipo di record restituito (A, AAAA, MX, TXT, ecc.) e sugli eventuali errori riscontrati.


Esempio di query di base:

```bash
dig mydmn.org
```


Interrogazione di un server DNS specifico:

```bash
dig @192.6.23.4 mydmn.org
```


Questo comando verifica la disponibilità di un record DNS su un determinato server.

Uno dei vantaggi principali di `dig` è che mostra i dettagli della risposta DNS, il che lo rende molto utile per diagnosticare gli errori di configurazione.


#### Configurazione manuale dei risolutori DNS


A volte è necessario sovrascrivere i server DNS utilizzati localmente, ad esempio in ambienti di test o per forzare l'uso di server specifici. Questo può essere fatto modificando il file `/etc/resolv.conf', che definisce le impostazioni di risoluzione DNS del sistema.


Esempio di configurazione:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Il campo `search` specifica un dominio da aggiungere automaticamente durante la risoluzione dei nomi brevi.
- Le voci `nameserver` definiscono i server DNS da utilizzare, in ordine di priorità.


In molte distribuzioni moderne (specialmente quelle che usano `systemd-resolved`), le modifiche a `/etc/resolv.conf` sono temporanee e possono essere sovrascritte al riavvio o alla riconnessione alla rete. Metodi più permanenti includono l'uso di `resolvconf`, `systemd-resolved` o la modifica delle configurazioni di *NetworkManager*.


#### Il comando `host


Un altro strumento DNS semplice ma efficace è `host`. Risolve i nomi di dominio in indirizzi IP (o l'inverso) e può aiutare a diagnosticare guasti o errate configurazioni DNS su una rete Interface.


Esempi:

```bash
host mydmn.org
```


Ricerca inversa:

```bash
host 192.6.23.4
```


`host` è particolarmente utile per i controlli rapidi, soprattutto se usato negli script a riga di comando.


Le interrogazioni ripetute o intensive a server DNS di terze parti senza autorizzazione possono essere interpretate come tentativi di intrusione o attività dannose. Se usati in modo improprio o contro reti non controllate, questi comandi possono assomigliare a scansioni di ricognizione, che spesso sono il primo passo di un attacco. Limitate sempre il loro uso agli ambienti che amministrate o per i quali disponete di un'autorizzazione esplicita.


### Strumenti di scansione della rete


Quando si monitora o si mette in sicurezza una rete locale o di grandi dimensioni, è fondamentale identificare i dispositivi attivi e i servizi che espongono. Questo è esattamente ciò che fa lo strumento `nmap` (*Network Mapper*).


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Introduzione a `nmap


`nmap` consente la scansione mirata di uno o più host per rilevare le porte aperte, i servizi disponibili (HTTP, SSH, DNS, ecc.) e talvolta anche il tipo di sistema operativo in uso. Grazie alle sue numerose opzioni, `nmap` fornisce una panoramica precisa della superficie di esposizione di una rete, essenziale durante le fasi di auditing o di hardening della gestione dell'infrastruttura.


Proprio come il comando `host`, `nmap` non deve mai essere usato su reti o infrastrutture non proprie o senza un'autorizzazione esplicita. Le scansioni delle porte non autorizzate possono essere segnalate come tentativi di ricognizione malevoli, sono spesso rilevate dai sistemi di sicurezza (firewall, IDS/IPS) e possono persino portare a conseguenze legali.


#### Uso di base


Per scansionare un host specifico e visualizzare le sue porte aperte:

```bash
nmap 192.168.0.1
```


Questo comando esegue la scansione delle 1000 porte più comuni sull'host `192.168.0.1` e visualizza i servizi a cui si accede e i protocolli utilizzati. Se la risoluzione DNS è configurata, è possibile utilizzare anche il nome dell'host invece dell'IP Address.


#### Scansione completa della rete


Uno dei vantaggi di `nmap` è la capacità di scansionare un intero intervallo di indirizzi con un solo comando. In questo modo è facile, ad esempio, inventariare rapidamente tutte le macchine attive su una rete:


```bash
nmap 192.168.0.0/24
```


In questo caso, verranno interrogati tutti gli host nell'intervallo da `192.168.0.0` a `192.168.0.255`. Per ogni IP Address, i risultati elencano le porte aperte, il loro stato (aperte, filtrate, ecc.) e, quando possibile, il nome del servizio corrispondente.



![Image](assets/fr/055.webp)



Un amministratore può affidarsi a `nmap` per diversi compiti:


- Rilevare gli host attivi**: identificare quali macchine rispondono all'interno di una sottorete;
- Inventario dei servizi**: garantire l'accesso solo alle porte necessarie (principio del minimo privilegio);
- Controllo di conformità**: confronta le porte aperte con la politica di sicurezza dell'organizzazione;
- Prevenzione delle vulnerabilità**: individuare servizi insicuri o non aggiornati in esecuzione su macchine critiche.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Strumenti di interrogazione dei processi


Per un'analisi approfondita dei processi attivi e dei file aperti, soprattutto in un contesto di rete, gli amministratori di Linux si rivolgono spesso al comando `lsof` (*List Open Files*). Nonostante il nome, `lsof` non si limita ai file tradizionali: nei sistemi UNIX, tutto è considerato un file, compresi i socket di rete, i dispositivi e i canali di comunicazione.


Questo strumento fornisce quindi una visione trasversale del sistema correlando i processi attivi, le porte di rete aperte, i file accessibili e gli utenti coinvolti.


#### Analisi di rete con `lsof


L'opzione `-i' limita l'output alle connessioni di rete (TCP, UDP, IPv4 o IPv6). In questo modo è facile vedere quali processi stanno comunicando sulla rete:


```bash
lsof -i
```


Questo comando elenca tutti i processi in esecuzione che utilizzano un socket di rete, mostrando la porta in uso, il protocollo (TCP/UDP), lo stato della connessione, nonché il PID e l'utente associato.


#### Filtraggio per IP Address o per porta


È possibile affinare le ricerche specificando un IP Address e una porta, isolando un particolare flusso di rete. Ad esempio, per controllare una sessione SMTP (porta 25) con un host specifico:


```bash
lsof -n -i @192.168.2.1:25
```


Questo visualizzerà solo le connessioni di rete attive con l'host `192.168.2.1` sulla porta 25, utile per diagnosticare attività sospette o problemi di flusso SMTP.


#### Tracciamento dell'accesso al dispositivo


Un altro punto di forza di `lsof` è il monitoraggio di file speciali come le partizioni del disco. Ad esempio, per verificare quali processi hanno aperto file su `/dev/sda1`:


```bash
lsof /dev/sda1
```


Questo è utile quando un tentativo di smontaggio fallisce perché il dispositivo è ancora in uso, oppure quando si indaga su quali applicazioni stanno accedendo a una partizione.


#### Analisi incrociata: processo e rete


Le opzioni possono essere combinate per ottenere informazioni precise. Ad esempio, per visualizzare tutte le porte di rete aperte da un processo con PID 1521:


```bash
lsof -i -a -p 1521
```


L'opzione `-a' interseca i criteri (`-i' e `-p'), limitando l'output alle sole connessioni di rete di quel processo.


#### Tracciamento multiutente


`lsof` può anche essere usato per analizzare l'attività di utenti specifici, elencando tutti i file che hanno aperto, opzionalmente filtrati per PID:


```bash
lsof -p 1521 -u 500,phil
```


Questo mostra i file o le connessioni di rete utilizzate dall'utente `phil` o UID 500, limitatamente al processo 1521.


### Riassunto della sezione


In questa sezione finale abbiamo esplorato un'ampia gamma di strumenti indispensabili per la diagnosi, l'analisi e l'amministrazione delle reti di computer. Strutturato intorno ai livelli del modello TCP/IP, questo studio non solo chiarisce il funzionamento delle comunicazioni di rete, ma stabilisce anche una metodologia rigorosa per identificare, isolare e risolvere i potenziali problemi.


Questi strumenti offrono agli amministratori un insieme coerente di leve tecniche per monitorare lo stato di salute della rete, analizzare il traffico, verificare le connessioni e intervenire rapidamente su apparecchiature o servizi difettosi.


#### Accesso alla rete Layer


Strumenti che forniscono visibilità diretta su interfacce e frame:


- arp / ip neigh**: ispeziona e modifica la cache ARP/NDP per controllare o correggere le associazioni IP-MAC;
- tcpdump**: cattura dei pacchetti a riga di comando, filtrabile ed esportabile;
- Wireshark**: analisi grafica dei pacchetti con decodifica profonda dei protocolli;
- ethtool**: interroga e regola i parametri fisici della scheda Ethernet (velocità, duplex, WoL, ecc.).


#### Rete Layer


Strumenti per la valutazione della connettività IP, del routing e del traffico di pacchetti:


- ping**: verifica la raggiungibilità e misura la latenza con ICMP;
- ip route**: ispeziona e modifica la tabella di routing per controllare i percorsi dei pacchetti;
- traceroute**: identificazione hop-by-hop dei router lungo il percorso verso una destinazione;
- ss**: inventario dettagliato dei socket TCP/UDP e dei processi associati (successore di netstat).


#### Livelli di trasporto e applicazione


Strumenti per la diagnosi di servizi e processi:


- nslookup / dig / host**: Query DNS per convalidare la risoluzione dei nomi e analizzare i record;
- nmap**: esplora le porte aperte e i servizi esposti per valutare la superficie di attacco;
- lsof**: elenca i file e i socket aperti dai processi, correlando l'attività del sistema e della rete.


La padronanza di questi strumenti, ciascuno allineato a una fase specifica del modello TCP/IP, consente un approccio metodico: a partire dal Layer fisico, passando per il routing e fino ai servizi applicativi. Questa catena di competenze consente agli amministratori di diagnosticare, proteggere e ottimizzare l'infrastruttura, garantendo le prestazioni e la disponibilità della rete.


# Parte finale


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Recensioni e valutazioni


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Esame finale


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Conclusione


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>
---
name: Nmap
description: Master Nmap per la mappatura della rete e la scansione delle vulnerabilità
---

![cover](assets/cover.webp)



*Questa esercitazione si basa su un contenuto originale di Mickael Dorigny pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Sono state apportate modifiche al testo originale



___



Benvenuti in questo tutorial introduttivo a Nmap, pensato per tutti coloro che desiderano padroneggiare questo potente strumento di scansione di rete. L'obiettivo è quello di fornire le conoscenze fondamentali necessarie per utilizzare Nmap in modo efficace ogni giorno.



Nmap è uno strumento versatile, ampiamente utilizzato dai professionisti dell'IT, delle reti e della cybersecurity per la diagnostica, la scoperta della rete e l'auditing della sicurezza. Questa esercitazione è rivolta a coloro che sono alle prime armi in questi campi e desiderano apprendere le basi di Nmap. Si raccomanda una conoscenza di base dell'amministrazione di sistema e di rete.



Imparerete le basi di Nmap, come eseguire scansioni di porte, identificare gli host attivi su una rete, rilevare versioni di servizi e sistemi operativi, eseguire scansioni di vulnerabilità e molto altro ancora. Ogni sezione comprende spiegazioni dettagliate ed esempi pratici per aiutarvi a padroneggiare l'uso di Nmap in una varietà di contesti.



Alla fine di questa esercitazione, avrete una solida conoscenza di Nmap e sarete in grado di utilizzarlo efficacemente per migliorare la sicurezza e la gestione delle vostre reti. Buona lettura.



## 1 - Introduzione a Nmap: Che cos'è Nmap?



### I. Presentazione



In questa prima sezione, daremo un'occhiata allo strumento di scansione di rete Nmap. Esamineremo i principali Elements da conoscere su questo strumento e il suo funzionamento in generale. Questo ci aiuterà a capire meglio il resto del tutorial.



### II. Introduzione allo strumento Nmap



Nmap, per _Network Mapper_, è uno strumento gratuito e open-source utilizzato per la **scoperta delle reti, la mappatura e la verifica della sicurezza**. Può essere utilizzato anche per altre attività come **inventario di rete, diagnostica o supervisione**.



Può determinare se gli host di una rete mirata sono attivi e raggiungibili, quali servizi di rete sono esposti, quali versioni e tecnologie sono in uso e altre utili informazioni di analisi. Nmap può essere utilizzato per eseguire la scansione di un singolo servizio su una macchina specifica o su un'ampia porzione di rete, fino all'intera Internet.



I punti di forza di Nmap sono molti:





- Potente e flessibile**: Nmap può eseguire la scansione di reti di grandi dimensioni e utilizzare tecniche di rilevamento avanzate. Supporta UDP, TCP, ICMP, IPv4 e IPv6 e può eseguire il rilevamento di versioni, scansioni di vulnerabilità o interazioni specifiche per i protocolli. La sua architettura è modulare, in particolare grazie agli script NSE (Nmap Scripting Engine), che vedremo più avanti in questo tutorial.
- Facilità d'uso**: la documentazione ufficiale è abbondante e di ottima qualità. Sono inoltre disponibili numerose risorse della comunità per aiutarvi a iniziare.
- Popolarità e longevità**: Nmap è un punto di riferimento nel suo campo dal 1998. La versione attuale, al momento del presente aggiornamento, è la 7.95. Sebbene esistano altri strumenti per compiti specifici, Nmap rimane un must per la mappatura e l'analisi delle reti.



**Nmap al cinema**



Nmap è uno dei pochi strumenti di sicurezza ad aver acquisito una certa notorietà presso il grande pubblico. Appare nel film _Matrix Reloaded_, in una scena emblematica in cui Trinity lo usa per hackerare un sistema:



![nmap-image](assets/fr/01.webp)



matrice: Scena Reloaded con Nmap



Appare anche in altre opere cinematografiche.



**Risposta



In qualità di amministratore di sistema e poi di auditor e pentester di cybersecurity, **utilizzo Nmap quasi quotidianamente** e lo **consiglio regolarmente** agli amministratori di sistema che desiderano rafforzare la loro padronanza delle reti e migliorare le loro capacità diagnostiche.



### III. Funzionamento ad alto livello



Nmap è disponibile per Linux, Windows e macOS. È scritto principalmente in C, C++ e Lua (per gli script NSE). Si usa principalmente alla riga di comando, anche se sono disponibili anche interfacce grafiche come Zenmap. Tuttavia, si consiglia vivamente di iniziare con la riga di comando per capire meglio il suo funzionamento.



Un semplice esempio:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Questo comando verrà spiegato in dettaglio più avanti. In questa guida utilizzeremo Nmap su Linux, ma i suoi usi sono simili su altri sistemi. In Windows, Nmap si basa sulla libreria **Npcap** (che sostituisce l'ormai obsoleto WinPcap) per catturare e iniettare i pacchetti di rete.



Nmap viene utilizzato come un binario convenzionale, come `ls` o `ip`. Alcune funzioni avanzate possono richiedere diritti elevati, poiché lo strumento a volte manipola i pacchetti in modi non convenzionali per provocare reazioni specifiche sui sistemi di destinazione (in particolare per il rilevamento di servizi o vulnerabilità).



### IV. Impatto dell'utilizzo di Nmap



Prima di utilizzare Nmap, è essenziale essere consapevoli del suo potenziale impatto su reti e sistemi:





- Può inviare **migliaia o addirittura milioni di pacchetti** in un breve lasso di tempo, il che può saturare alcune infrastrutture di rete.
- È in grado di inviare a generate pacchetti **malformati o non standard**, in grado di disturbare alcune apparecchiature (in particolare i sistemi industriali).
- Può produrre un **comportamento simile a quello di un attacco**, che può innescare allarmi nei sistemi di sicurezza (firewall, IDS/IPS, ecc.).



In generale, **Nmap è uno strumento molto loquace**, in quanto genera molto traffico per estrarre quante più informazioni possibili. È quindi consigliabile comprendere appieno il suo funzionamento prima di utilizzarlo in ambienti sensibili o di produzione.



### V. Conclusioni



Questa sezione introduce Nmap e le sue caratteristiche principali. Abbiamo visto che si tratta di uno strumento essenziale, potente e flessibile per la mappatura delle reti. Abbiamo anche discusso il suo funzionamento e le precauzioni da prendere quando lo si usa, per preparare la scena per le parti successive del tutorial.



## 2 - Perché usare Nmap?



### I. Presentazione



In questa sezione daremo un'occhiata agli usi principali dello strumento di scansione di rete Nmap. Vedremo che si tratta di uno strumento ampiamente utilizzato in molti contesti e professioni e che averlo nella propria cassetta degli attrezzi e saperlo padroneggiare è sicuramente un'abilità utile.



### II. Utilizzo di Nmap per la diagnostica e la supervisione



Nmap può essere utilizzato per la diagnostica di rete e, più in generale, per il monitoraggio. Così come un ping può essere usato per determinare se due host stanno comunicando, Nmap può essere usato per determinare rapidamente se un host è attivo o se un particolare servizio è operativo. Grazie a [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap"), è possibile ottenere dati precisi sul tempo di risposta di un host, sul percorso effettuato dai pacchetti, sulla risposta fornita da un servizio specifico, ecc.



Il comando e il risultato seguenti possono essere utilizzati, ad esempio, per scoprire rapidamente se un server web sull'host **192.168.1.18** è attivo e risponde correttamente:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Usare Nmap per recuperare lo stato del servizio web da un server remoto.*



Quindi, l'uso di Nmap va oltre il famoso "test ping" durante le fasi di debug o diagnostica. Vedremo più avanti che ci sono diversi metodi utilizzati da Nmap per identificare quale servizio è in ascolto su una determinata porta, compresa la sua versione.



### III. Utilizzo di Nmap per la mappatura della rete



Come _Network Mapper_, la mappatura delle reti è l'obiettivo principale di questo strumento. Può essere utilizzato all'interno di una rete locale o su più reti, sottoreti e VLAN, per elencare tutti gli host e i servizi raggiungibili. Nmap rende questo compito molto più veloce ed efficiente di qualsiasi metodo manuale.



Ad esempio, il comando seguente può essere usato per identificare rapidamente gli host attivi sulla rete **192.168.1.0/24**:



```
nmap -sn 192.168.1.0/24
```



*Nota: l'opzione `-sP` è obsoleta ed è stata sostituita da `-sn`.*



![nmap-image](assets/fr/03.webp)



*Utilizzo di Nmap per scoprire gli host raggiungibili su una rete*



Vedremo più avanti che ci sono diversi metodi utilizzati da Nmap per determinare se un host può essere considerato "attivo", anche se non espone a priori alcun servizio.



### IV. Utilizzo di Nmap per valutare una politica di filtraggio



Nmap ha il vantaggio di essere fattuale: i suoi risultati consentono di stabilire conclusioni concrete, a differenza di qualsiasi documento di architettura o politica di filtraggio. È uno strumento fondamentale per valutare l'efficacia della compartimentazione del sistema informativo, in quanto consente di **verificare se la politica di filtraggio viene effettivamente applicata**.



In una rete aziendale, le migliori prassi impongono di segmentare i sistemi in base al loro ruolo, alla loro criticità o alla loro ubicazione. Le regole di filtraggio (spesso implementate tramite firewall) devono limitare le comunicazioni tra le zone. Ma queste configurazioni sono spesso complesse e soggette a errori.



Per verificare che la politica sia stata rispettata, non c'è niente di meglio di un test concreto. Ad esempio, si può verificare che i servizi di amministrazione sensibili (SSH, WinRM, MSSQL, MySQL, ecc.) non siano accessibili da una zona utente.



L'uso di **Nmap per testare il criterio di filtraggio** dovrebbe essere sistematico prima che tale criterio venga messo in produzione. Purtroppo, questo controllo viene spesso trascurato.



Secondo la mia esperienza, molti errori di configurazione passano inosservati in assenza di test di convalida. Un semplice errore in un intervallo IP o nella svista di una regola può rendere vulnerabile una zona apparentemente isolata.



### V. Utilizzo di Nmap per l'auditing della sicurezza e i test di penetrazione



Nmap ha **molte funzioni utili per la valutazione della sicurezza**, per i test di penetrazione (pentest) e purtroppo anche per gli aggressori.



Le funzioni di scoperta della rete sono fondamentali per un attaccante, che ha bisogno di capire la topologia della rete dopo una compromissione iniziale. Ma Nmap offre molto di più: integra un motore di scripting, **molti dei quali sono dedicati al rilevamento delle vulnerabilità**.



Ad esempio, questo comando può essere usato per verificare se un servizio FTP consente una connessione anonima, senza doversi connettere manualmente:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Utilizzo di uno script NSE per verificare l'autenticazione FTP anonima tramite Nmap.*



Il rilevamento delle vulnerabilità di Nmap è una delle prime fasi di un audit o di un test di penetrazione. Consente di identificare rapidamente alcuni punti deboli e di ottimizzare gli sforzi di analisi.



Ma attenzione: **Gli strumenti di scansione della vulnerabilità hanno i loro limiti**. Nmap copre solo una parte delle minacce e non garantisce che un sistema sia sicuro se non vengono rilevati problemi. È quindi essenziale **comprendere il funzionamento degli script utilizzati** e non affidarsi esclusivamente al loro verdetto.



### VI. Conclusione



Abbiamo visto che la padronanza di Nmap può coprire un'ampia gamma di casi d'uso, dalla diagnostica e dal monitoraggio alla mappatura, alla valutazione dei criteri di sicurezza e alla scansione delle vulnerabilità. Nella prossima sezione entreremo nel vivo dell'installazione di Nmap.




## 3 - Installazione e configurazione di Nmap



### I. Presentazione



In questa sezione impareremo a installare lo strumento di scansione di rete Nmap sui sistemi operativi Linux e Windows. Alla fine di questa sezione, avremo tutto il necessario per iniziare a usare Nmap per i moduli futuri. Infine, vedremo quali privilegi può richiedere quando viene utilizzato e perché.



### II. Installazione di Nmap in Linux



Nmap è stato originariamente progettato per funzionare su sistemi operativi GNU/Linux. Di conseguenza, grazie alla sua longevità e popolarità, lo troverete in tutti i repository ufficiali delle principali distribuzioni Unix. In questo tutorial, utilizzerò un sistema operativo basato su Debian [Kali Linux] (https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Ma potete usarlo esattamente nello stesso modo da una classica Debian, CentOS, Red Hat o altro!



In Debian, per verificare che Nmap sia presente nei repository correnti, si può usare il seguente comando:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



La risposta indica chiaramente che il pacchetto "nmap" esiste nei repository (qui, quelli di Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). D'ora in poi, potrete installare Nmap tramite i soliti comandi di installazione, niente di disarmante per il momento 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Per verificare che Nmap sia installato correttamente, visualizzeremo la sua versione:



```
nmap --version
```



Ecco il risultato atteso:



![nmap-image](assets/fr/05.webp)



risultato della visualizzazione della versione attuale di Nmap._



Si noti la presenza in questa visualizzazione della libreria "libpcap" (_Packet Capture Library_) e della sua versione. Utilizzata anche da Wireshark, "libpcap" è usata da Nmap per creare e manipolare i pacchetti e ascoltare il traffico di rete.



### III Installazione di Nmap su Windows



Per installarlo su un sistema operativo Windows, iniziate scaricando il binario dal sito ufficiale (e da nessun altro!):





- Pagina di download di Nmap sul sito ufficiale: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




È quindi necessario scaricare il file binario denominato `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



pagina di download del binario di installazione di nmap per Windows



Una volta che il binario è presente sul sistema, è sufficiente eseguirlo per installare Nmap. L'installazione è semplice e si possono lasciare tutte le opzioni come predefinite.



Il mio riflesso è quello di deselezionare la casella "zenmap (GUI Frontend)". Si tratta di un Interface grafico per Nmap che non uso e che non sarà trattato in questo tutorial, ma provatelo pure una volta che avrete imparato a usare lo strumento a riga di comando di Nmap!



![nmap-image](assets/fr/07.webp)



deselezione opzionale di Zenmap durante l'installazione di Nmap su Windows



Al termine dell'installazione di Nmap, viene proposta una seconda installazione: quella della libreria "Npcap":



![nmap-image](assets/fr/08.webp)



installazione della libreria "Npcap" durante l'installazione di Nmap in Windows



È la libreria su cui si basa Nmap per gestire le comunicazioni di rete, ossia la creazione, l'invio e la ricezione di pacchetti di rete. Probabilmente vi siete già imbattuti in questa libreria se utilizzate Wireshark su Windows, poiché anch'essa la utilizza e ne richiede l'installazione.



Come per Linux, è possibile verificare che Nmap sia installato aprendo un Prompt dei comandi o un terminale [Powershell] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") e digitando il seguente comando:



```
nmap --version
```



Ecco il risultato atteso:



![nmap-image](assets/fr/09.webp)



risultato della visualizzazione della versione corrente di Nmap._



Nmap è ora installato su Windows. È possibile utilizzarlo esattamente come su Linux, seguendo questa guida.



### IV. Privilegi locali necessari per utilizzare Nmap



Ma a proposito, quando si usa Nmap, **è necessario avere privilegi locali elevati sul sistema? ** La risposta è: *dipende**: **dipende**.



Nella sua forma più elementare, cioè senza utilizzare le sue opzioni, Nmap non richiede necessariamente diritti privilegiati. Tuttavia, vi renderete presto conto che è meglio usare Nmap in un contesto privilegiato ("root" in Linux, "amministratore" o equivalente in Windows) per poterlo utilizzare al massimo delle sue potenzialità, con il rischio di ricevere un messaggio di errore come questo:



![nmap-image](assets/fr/10.webp)



messaggio di errore in Linux quando le opzioni di Nmap richiedono i diritti di root



Sia su Linux che su Windows, ci sono molti casi in cui Nmap vi chiederà un accesso privilegiato. I motivi principali sono i seguenti (elenco non esaustivo):





- Costruzione di pacchetti di rete "grezzi "**: Nmap è in grado di eseguire un'ampia gamma di metodi di scansione, compresa la manipolazione e la costruzione di pacchetti avanzati. È il caso, ad esempio, di eseguire scansioni TCP SYN, che non rispettano il classico _Three-way handshake_ degli scambi TCP. Per fare questo, Nmap ha bisogno di utilizzare funzioni diverse da quelle native dei sistemi operativi, che sanno solo rispettare le buone pratiche nelle comunicazioni di rete (fa appello alle librerie "Npcap" e "libcap" viste sopra). È perché Nmap non fa le cose in modo "standard" che è in grado di dedurre alcune informazioni sui sistemi operativi, sui servizi e su alcune vulnerabilità.





- Ascoltare il traffico di rete**: alcune opzioni di Nmap richiedono l'ascolto della rete per recuperare determinate informazioni. Questa azione è considerata sensibile nei sistemi operativi, poiché consente anche di ascoltare le comunicazioni di altre applicazioni sul sistema. Proprio come Wireshark, Nmap ha bisogno di privilegi specifici per farlo, che sono più facili da ottenere se ci si trova direttamente in una sessione privilegiata.





- Ascolto su porte privilegiate**: nei sistemi operativi, le porte da 0 a 1024 (TCP e UDP) sono dette privilegiate, cioè riservate a usi molto specifici e quindi protette. Anche se oggi questo è un motivo un po' obsoleto, è ancora necessario avere determinati privilegi per ascoltare su queste porte, cosa che Nmap potrebbe dover fare a seconda dell'uso che ne verrà fatto.





- Invio di pacchetti UDP:** Analogamente, l'ascolto di un'applicazione di rete sulle porte UDP (un protocollo stateless) richiede diritti privilegiati sui sistemi operativi. Sarà quindi necessaria una sessione privilegiata se si desidera eseguire una scansione UDP, per la quale Nmap dovrà ascoltare una risposta al fine di analizzare le risposte alle sue scansioni.




Per essere più precisi, è possibile, almeno in Linux, eseguire Nmap con tutte le sue funzioni e opzioni senza essere root. Ciò si ottiene concedendo le giuste _capacità_ al binario. Tuttavia, questo richiede una manipolazione avanzata e potrebbe non essere così pratico come eseguire Nmap direttamente con i privilegi. Inoltre, questo approccio è meno comune e può creare problemi di sicurezza se configurato male.



Tuttavia, questo si discosta un po' dal nostro tutorial su Nmap, quindi per ora ne faremo a meno.



Per il resto di questa guida, si presuppone che Nmap sia sempre eseguito come "root" (da una shell come "root" o tramite il comando "sudo"), o in un terminale amministratore in Windows, anche se ciò non è indicato. In caso contrario, si potrebbero riscontrare differenze sottili ma evidenti rispetto al tutorial.



### V. Conclusioni



Ecco fatto! Nmap è ora installato sul nostro sistema operativo e pronto all'uso, senza bisogno di ulteriori configurazioni. Questa sezione conclude l'introduzione e la presentazione di Nmap. Spero che vi abbia fatto venire l'acquolina in bocca e che siate ansiosi di iniziare a fare pratica.



Su una nota più seria, ora abbiamo un'idea più precisa di cosa sia lo strumento di mappatura Nmap e di quali siano i suoi usi più comuni, nonché i suoi limiti. Andiamo avanti!




## 4 - Scansione delle porte TCP e UDP con Nmap



### I. Presentazione



In questa sezione impareremo a eseguire le prime scansioni delle porte utilizzando lo strumento di scansione di rete Nmap. Vedremo come utilizzarlo per compilare un elenco dei servizi di rete esposti su un host, sia che utilizzino i protocolli TCP che UDP.



D'ora in poi, ricordatevi di scansionare solo gli host in un ambiente controllato per i quali disponete di un'autorizzazione esplicita.





- Come promemoria: [Codice penale: Capo III: Attacchi a sistemi automatizzati di elaborazione dati](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Se non ne avete uno a portata di mano**, vi consiglio le seguenti soluzioni gratuite, che fanno al caso vostro!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Piattaforma di addestramento all'hacking, Hack The Box mette costantemente a disposizione sistemi vulnerabili da attaccare come meglio credete. Sono disponibili diverse centinaia di sistemi, ma un pool rinnovato di 20 macchine è offerto gratuitamente tutto l'anno, con accesso tramite una VPN OpenVPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Questa piattaforma offre numerosi sistemi intenzionalmente vulnerabili da scaricare, che possono essere utilizzati tramite VirtualBox (anch'essa una soluzione gratuita) o altri mezzi. Una volta scaricati, non c'è bisogno di una VPN: tutto è locale.




Inoltre, siete liberi di **creare una macchina virtuale** sul vostro sistema operativo preferito e installarvi vari servizi come target di test. Il vantaggio sarà che sarete in grado di vedere cosa succede sul lato server durante una scansione, soprattutto con Wireshark, e di intervenire sul firewall locale quando faremo test più avanzati.



Facciamo un po' di pratica!



### II. Scansione delle porte TCP di un host tramite Nmap



#### A. Prima scansione della porta TCP con Nmap



Ora eseguiamo le prime scansioni con Nmap. Il nostro obiettivo è semplice: vogliamo scoprire quali servizi sono esposti dal server web che abbiamo appena implementato, per vedere se c'è qualcosa di inaspettato, come un servizio di amministrazione che non dovrebbe essere accessibile o l'esposizione di una porta di un'applicazione che pensavamo fosse stata disattivata.



Nel mio esempio, l'host da scansionare ha l'IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Ecco un possibile risultato. Vediamo un classico ritorno di Nmap con molte informazioni:



![nmap-image](assets/fr/11.webp)



risultati di una semplice scansione TCP eseguita con Nmap



Dando una rapida occhiata a questo risultato, si capisce che le porte TCP/22 e TCP/80 sono accessibili su questo host.



Per impostazione predefinita, e se non glielo si dice, Nmap scansiona solo le porte TCP.



#### B. Comprendere i risultati di una semplice scansione Nmap



Ma andiamo oltre, per capire questo output: ogni riga è importante, in primo luogo per sapere cosa è stato appena fatto e in secondo luogo per interpretare correttamente i risultati della scansione stessa.



La prima riga è essenzialmente un promemoria della versione e della data della scansione (utile per la registrazione e l'archiviazione!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



La seconda riga mostra i risultati dell'avvio della scansione per l'host "debian.home (192.168.1.19)". Queste informazioni saranno utili quando si avvierà la scansione di più host contemporaneamente:



```
Nmap scan report for debian.home (192.168.1.19)
```



La terza riga ci dice che l'host in questione è "Up", cioè attivo:



```
Host is up (0.00022s latency).
```



Infine, Nmap ci informa che 998 porte TCP identificate come chiuse non vengono visualizzate nel file:



```
Not shown: 998 closed tcp ports (conn-refused)
```



In questo modo si risparmiano quasi 1.000 righe di output che assomigliano a:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Grazie a lui per averci risparmiato questo!



Perché 998 porte "chiuse"? Aggiungendo le 2 porte aperte si arriva a 1000, e questo è il numero di porte che Nmap scansionerà nella sua configurazione predefinita, non le 65535 porte TCP esistenti! Vedremo più avanti che questa configurazione è interamente e facilmente personalizzabile. Ma se l'host preso di mira ha un servizio in ascolto su una porta piuttosto esotica, questa scansione "predefinita" non lo scoprirà.



Dopo queste informazioni, troviamo ciò che è più interessante: una tabella organizzata secondo le tre colonne "PORT - STATE - SERVICE":





- La prima colonna "PORT" indica semplicemente la porta/protocollo di destinazione ed è importante verificare se si tratta di una porta TCP (`<port>/tcp`) o UDP (`<port>/udp`).





- La colonna "STATE" indica lo stato del servizio di rete scoperto su questa porta e determinato da Nmap in base alla risposta ottenuta. Può essere "aperto", "chiuso", "filtrato" o "sconosciuto". Vedremo più avanti come Nmap distingue questi diversi stati.





- La colonna "SERVICE" indica il servizio esposto sulla porta in questione. Si noti, tuttavia, che in questo caso non sono state utilizzate opzioni di scoperta attiva dei servizi. Nmap si basa su un riferimento locale tra una porta/protocollo e il servizio presumibilmente assegnato: il file "/etc/services"




Se si consulta il file "/etc/services" di un sistema Linux, si troverà un collegamento "port/protocol - service" simile a quello visualizzato da Nmap:



![nmap-image](assets/fr/12.webp)



estrae il contenuto del file "/etc/services" in Linux



È importante capire che, per il momento, Nmap non ha eseguito alcun rilevamento attivo dei servizi. Ad esempio, non sarebbe stato in grado di identificare il servizio SSH dietro una porta TCP/80 se questo fosse stato il caso. Da qui l'importanza di sapere come usare le opzioni giuste: presto arriverà!



Sapere come interpretare l'output di Nmap è una parte importante della padronanza dello strumento. La buona notizia è che l'output sarà in gran parte lo stesso, indipendentemente dalle opzioni utilizzate.



#### C. Sotto il cofano: analisi della rete tramite Wireshark



Se si osserva attentamente ciò che accade sulla rete Interface dell'host che esegue la scansione del server o su quella del server stesso, le azioni di Nmap saranno molto più chiare. È quello che faremo qui.



Quello che posso mostrarvi qui è solo una parte di ciò che è visibile in Wireshark. Se volete andare oltre, potete eseguire voi stessi una cattura della rete durante una scansione e poi sfogliare ciò che è stato catturato.



In questo test, l'host di scansione (192.168.1.18) e l'host di destinazione (192.168.1.19) si trovano sulla stessa rete locale.



Nmap inizia scoprendo se l'host di destinazione è attivo sulla rete locale inviando una richiesta ARP. Se riceve una risposta, sa che l'host è attivo e inizia la scansione della rete:



![nmap-image](assets/fr/13.webp)



richiesta ARP emessa da Nmap per determinare se un host di destinazione è presente sulla rete locale



Se l'host da scansionare si trova su una rete remota, Nmap inizia inviando una richiesta di ping e cerca di raggiungere alcune delle porte più frequentemente esposte (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



richiesta di ping emessa da Nmap per determinare se un host di destinazione è raggiungibile su una rete remota



Se ottiene una risposta a uno qualsiasi di questi test, considera il bersaglio attivo.



Una volta che Nmap ha determinato che il suo obiettivo è attivo, cercherà di risolvere il suo nome di dominio con il server DNS configurato sulla scheda di rete:



![nmap-image](assets/fr/15.webp)



risoluzione dNS sul target di scansione Nmap



Ora che Nmap ha identificato l'obiettivo e sa che è attivo, inizia la scansione della porta TCP:



![nmap-image](assets/fr/16.webp)



tCP Trasmissione di pacchetti SYN e ricezione di RST/ACK durante la scansione Nmap



A tal fine, su ogni porta TCP nel suo intervallo predefinito, **invia pacchetti TCP SYN e attende una risposta**. Nella schermata qui sopra, riceve pacchetti TCP RST/ACK dal server scansionato, il che significa "vai avanti, non c'è niente da vedere qui" - in altre parole, queste porte sono chiuse. Come abbiamo visto nel risultato, questo sarà il caso della maggior parte delle porte scansionate. Con due eccezioni:



![nmap-image](assets/fr/17.webp)



risposta a un pacchetto TCP SYN inviato sulla porta 22, attivo sulla destinazione della scansione



Nell'immagine qui sopra, vediamo un pacchetto TCP SYN/ACK inviato dall'host di destinazione**. La porta è attiva ed espone un servizio. Nmap conferma la ricezione della risposta, quindi termina la connessione (TCP RST/ACK). **In questo modo ha saputo che la porta TCP/22 era attiva**.



Abbiamo visto che Nmap rispetta il "Three Way Handshake" durante la scansione di una rete TCP. Per motivi di prestazioni, è possibile chiedergli di non rispondere al ritorno del server, risparmiando così diverse migliaia di pacchetti durante la scansione di una rete di grandi dimensioni. Ma vedremo queste opzioni e ottimizzazioni più avanti nel corso del tutorial.



Ora abbiamo un'idea più precisa di come eseguire una scansione TCP e di cosa succede effettivamente quando viene eseguita. Abbiamo anche visto che, per impostazione predefinita, Nmap esegue una scansione della porta TCP su un numero limitato di porte.



### III. Scansione delle porte UDP con Nmap



#### A. Prima scansione della porta UDP con Nmap



Vediamo ora come analizzare le porte UDP di un host. Come abbiamo visto, per impostazione predefinita Nmap scansiona sempre le porte TCP. Questo può significare perdere molte informazioni se non ne siamo consapevoli.



Come promemoria, ai fini di questo test, il mio host di scansione (192.168.1.18) e il mio host di destinazione (192.168.1.19) si trovano sulla stessa rete locale.



```
nmap -sU 192.168.1.19
```



In questo caso, il ritorno ottenuto ha lo stesso formato di una scansione TCP, ma i servizi attivi visualizzati sono in `<porta>/UDP`, come richiesto!



![nmap-image](assets/fr/18.webp)



risultato di una semplice scansione UDP eseguita con Nmap



L'opzione "-sU" viene utilizzata per indicare a Nmap che si desidera lavorare su UDP, anziché su TCP, come avviene di default.



A proposito, avrete probabilmente notato che Nmap richiede i diritti di "root" per le scansioni UDP, come menzionato in precedenza nel tutorial.



nota: a partire dalle ultime versioni di Nmap, si raccomanda sempre di eseguire le scansioni UDP con i privilegi di amministratore per garantire risultati affidabili, poiché alcune funzioni richiedono l'accesso non vincolato ai socket di rete



Le scansioni UDP possono richiedere molto tempo (1100 secondi per scansionare 1000 porte nel mio esempio), a causa dell'assenza del "Three Way Handshake" in UDP, il che significa che Nmap attenderà un ritorno per ogni pacchetto UDP inviato e determinerà la porta come "chiusa" solo se non vi è alcun ritorno dopo un certo tempo (timeout). La risposta degli host sottoposti a scansione non è sistematica e spesso è limitata in termini di numero di risposte al secondo, per evitare alcuni attacchi di amplificazione. Ciò è in contrasto con il TCP, dove la risposta dell'host scansionato è immediata, sia che la porta sia aperta o chiusa. Vedremo più avanti come ottimizzare questo aspetto.



Una seconda difficoltà con UDP è **che i servizi non rispondono sempre ai pacchetti in arrivo**, semplicemente perché questo non è sempre necessario ed è il principio di UDP. Quando questo è il caso e non viene ricevuto alcun ICMP "port unreachable", il servizio viene contrassegnato come "open|filtered" da Nmap, come mostrato nella schermata precedente.



#### B. Sotto il cofano: analisi della rete tramite Wireshark



Come per la scansione TCP, diamo un'occhiata più da vicino a ciò che accade a livello di rete durante una scansione UDP utilizzando un'analisi Wireshark. Il comportamento di Nmap nel determinare se un host è attivo è lo stesso.



L'unica vera differenza nella scansione di UDP è che Nmap non attende un "Three Way Handshake", poiché questo meccanismo non esiste in UDP (protocollo stateless):



![nmap-image](assets/fr/19.webp)



trasmissione di pacchetti uDP e ricezione ICMP (porta irraggiungibile) durante la scansione Nmap



Nella schermata precedente si può notare che Nmap invia un gran numero di pacchetti UDP e riceve in risposta un pacchetto ICMP "Destination unreachable (Port unreachable)". Questo è normale, poiché è la risposta appropriata definita da [RFC 1122] (https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") quando una porta UDP non è raggiungibile:



![nmap-image](assets/fr/20.webp)



estratto da RFC 1122._



Diamo un'occhiata più da vicino a questa acquisizione di Wireshark, che mostra **i tre possibili scenari** in UDP:



![nmap-image](assets/fr/21.webp)



cattura della rete durante una scansione UDP su diverse porte con Nmap._



I tre casi sono i seguenti:





- Il primo Exchange è composto dai pacchetti no. 3, 4 e 8, 9. Nmap invia pacchetti UDP sulla porta SNMP classica e quindi **costruisce in anticipo i pacchetti conformi al protocollo**. Quindi ottiene una risposta dal server (pacchetti n. 8 e 9). Risultato: Nmap ha ricevuto una risposta, il servizio è "aperto".





- Il secondo Exchange è costituito dai pacchetti 6 e 7. Nmap invia un pacchetto UDP "vuoto" (senza struttura di protocollo) alla porta UDP/165 e riceve in risposta un pacchetto ICMP: "Destinazione non raggiungibile (Porta non raggiungibile)". Risultato: Nmap ha ricevuto una risposta (negativa), l'host è attivo, ma il servizio che ha cercato di raggiungere non è operativo su questa porta, che sarà contrassegnata come "chiusa".





- L'ultimo Exchange è costituito dal pacchetto n. 12: Nmap invia un pacchetto UDP "vuoto" alla porta UDP/1235. Non c'è risposta, nemmeno un rifiuto esplicito da parte dell'host scansionato. Risultato: Nmap contrassegna la porta come "aperta|filtrata", poiché non è in grado di stabilire se ciò sia dovuto alla presenza di un firewall, configurato per non rispondere, o a un servizio UDP attivo che non restituisce comunque alcuna risposta (non obbligatorio in UDP).




Ecco il risultato visualizzato da Nmap in questi tre casi:



![nmap-image](assets/fr/22.webp)



i possibili risultati di una scansione UDP eseguita tramite Nmap._



Ora abbiamo un'idea più precisa di come eseguire una scansione UDP e di cosa succede effettivamente quando viene eseguita. Finora abbiamo usato Nmap in modo molto semplice, senza decidere quali porte scansionare, ma le cose stanno per cambiare!



### IV. Messa a punto della scansione delle porte con Nmap



#### A. Promemoria del comportamento predefinito di Nmap



Come abbiamo visto, Nmap sceglie da solo il numero e le porte da scansionare se non si specifica alcuna opzione. Questa è la configurazione "predefinita" utilizzata da Nmap quando non gli si dice esattamente cosa fare. Queste opzioni predefinite sono pensate per dare un'idea delle principali porte esposte, che vengono selezionate in base alla frequenza di esposizione (porte più comuni o frequenti) piuttosto che in ordine numerico (porta 1, 2, 3, ecc.) e anche per evitare di avviare una scansione delle 65535 porte possibili se non si specificano le opzioni appropriate, che sarebbero troppo lunghe e prolisse per un caso d'uso "predefinito".



**Come vengono scelte queste porte?



Le 1000 porte scansionate nella modalità predefinita sono scelte in base alla loro frequenza. Queste statistiche sono mantenute da Nmap e aggiornate allo stesso modo del binario stesso e dei suoi script (moduli). È possibile visualizzare queste statistiche nel file "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



estratto dal file "/usr/shares/nmap/nmap-services"._



Qui, nella terza colonna, vediamo quelle che sembrano probabilità (tra 0 e 1) o una distribuzione percentuale. Si tratta della frequenza di occorrenza di ciascuna coppia porta/protocollo. Possiamo notare che le porte più conosciute (FTP, SSH, TELNET e SMTP in questo estratto) hanno un valore molto più alto rispetto alle altre.



#### B. Specificare con precisione le porte di destinazione per una scansione Nmap



Tuttavia, nel mondo reale, potrebbe essere necessario scansionare solo una porta specifica, o più porte, o un intervallo specifico di porte. Con Nmap è facile fare proprio questo, in modo uniforme per le scansioni UDP e TCP.



**Scansione di una porta specifica tramite Nmap**



Se si desidera eseguire la scansione di una singola porta, e non di 1000, è possibile specificare questa porta tramite l'opzione "-p" o "--port" di Nmap:



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Di conseguenza, la scansione sarà naturalmente molto più veloce e Nmap emetterà solo i pacchetti necessari per rilevare se l'host è attivo e se la porta specificata è raggiungibile. Ciò consente di risparmiare tempo se si desidera eseguire un test rapido per verificare se il servizio Web del sito della vetrina è ancora attivo.



**Scansione di più porte tramite Nmap**



Allo stesso modo, possiamo specificare più porte a Nmap, utilizzando la stessa opzione e concatenando le porte specificate con una virgola:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Indipendentemente dall'ordine, Nmap controllerà tutte queste porte e solo quelle sull'host preso di mira. Nell'output di Nmap si noterà che **dice esplicitamente tutte le porte e il loro stato**, anche se sono "chiuse". A differenza del comportamento predefinito, in cui questo output completo avrebbe occupato troppo spazio:



![nmap-image](assets/fr/24.webp)



*Risultato di una scansione Nmap TCP sulle porte indicate



**Scansione di una serie di porte



Se il numero di porte da scansionare è troppo grande, è possibile specificarle per intervallo, ad esempio:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Naturalmente, è possibile mescolare e abbinare a piacimento, ad esempio:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**Scansione delle porte TCP e UDP



È anche possibile eseguire scansioni UDP e TCP contemporaneamente, su porte selezionate:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



In quest'ultimo esempio si nota la presenza di "U:" per indicare una porta UDP e "T:" per indicare una porta TCP. Ecco un possibile risultato di questo tipo di scansione:



![nmap-image](assets/fr/25.webp)



*Risultato della scansione delle porte TCP e UDP con Nmap.*



Questo è un modo interessante per personalizzare le scansioni!



**Scansione di tutte le porte



Infine, è possibile specificare a Nmap intervalli più o meno ampi. Abbiamo visto che l'elenco predefinito selezionato da Nmap contiene 1000 porte. Possiamo anche chiedere le prime 100 porte più frequenti, o le prime 200, usando l'opzione "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Infine, possiamo chiedere di scansionare tutte le porte possibili (tutte le 65535), usando la notazione "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Quest'ultima operazione richiederà più tempo, soprattutto con UDP, ma sarete sicuri di non perdere nessuna porta aperta.



*Nota: L'opzione "-p-" è il metodo consigliato per la scansione di tutte le porte TCP. Per le scansioni UDP, è consigliabile limitare il numero di porte per motivi di prestazioni, poiché le scansioni complete di tutte le porte UDP possono richiedere tempi molto lunghi.*



Più avanti nel corso dell'esercitazione, vedremo come ottimizzare la velocità delle scansioni di Nmap in base alle nostre esigenze, il che sarà particolarmente utile per le scansioni su tutte le porte TCP e UDP.



### V. Conclusioni



In questa sezione abbiamo finalmente fatto un po' di pratica e ora sappiamo **come usare Nmap in modo elementare per scansionare le porte TCP e UDP di un host**. Abbiamo anche analizzato in dettaglio cosa succede a livello di rete e **come Nmap determina se una porta TCP o UDP è attiva o meno**. Infine, sappiamo come selezionare finemente le porte che vogliamo scansionare e **cosa fanno effettivamente le opzioni predefinite di Nmap**. Nel seguito, riutilizzeremo queste conoscenze e le applicheremo alla scansione di un'intera rete, compresa la mappatura globale e la scoperta della rete.




## 5 - Mappatura e scoperta della rete con Nmap



### I. Presentazione



In questa sezione impareremo a utilizzare lo strumento di scansione di rete Nmap per mappare la rete. Vedremo come può essere efficace in questo compito, attraverso le sue varie opzioni. Infine, esamineremo diversi modi per specificare gli obiettivi delle nostre scansioni a Nmap.



In particolare, utilizzeremo quanto appreso nella sezione precedente su come Nmap determina se un host è attivo e raggiungibile.



Come accennato nell'introduzione a Nmap, si tratta di un Network Mapper. Come tale, è lo strumento perfetto per stilare un elenco di host accessibili su una rete, sia locale che remota.



**Ritorno dell'autore:**



In effetti, come auditor e pentester di cybersecurity, utilizzo sistematicamente Nmap quando eseguo test di penetrazione interni per scoprire dove mi trovo, chi sono i miei vicini sulla rete locale e quali altre reti sono accessibili, nonché i sistemi che vi si trovano. Il mio obiettivo è semplice: mappare la rete, determinare le dimensioni del sistema informativo e, in particolare, delineare la sua superficie di attacco.



La mappatura della rete può essere utile anche nel contesto della diagnostica di rete, della supervisione, della mappatura degli asset (siete davvero sicuri che il vostro IS sia costituito solo da ciò che è presente nell'Active Directory o nell'inventario GLPI/OCS? Può anche essere utilizzata per rilevare la presenza di Shadow IT nel vostro sistema informativo.



### II. Utilizzo di Nmap per la scansione di una rete



#### A. Scoprire una rete con una scansione Nmap



Ora vorremmo fare un passo avanti e analizzare l'intera rete locale. Nulla di più semplice: basta riutilizzare i comandi visti nella sezione precedente, ma specificando un CIDR invece di un semplice IP Address.



Un CIDR (**Classless Inter Domain Routing**) è la notazione "classica" per specificare un intervallo di rete e la sua estensione (utilizzando la maschera). Ad esempio, "192.168.0.0/24" è una "traduzione" della notazione della maschera decimale "255.255.255.0".



Per utilizzare Nmap specificando un CIDR, si può procedere come segue:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



È anche possibile, come per le porte nella sezione precedente, specificare più host, più reti o un intervallo:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Ecco un esempio dei risultati che si possono ottenere eseguendo una scansione su una rete:



![nmap-image](assets/fr/26.webp)



risultati di una scansione Nmap per mappare diverse reti



In particolare, si vedono diversi host attivi e ogni sezione di host inizia con una riga come questa:



```
Nmap scan report for <name> (<IP>)
```



Questo ci permette di vedere chiaramente a quale host si riferiscono i risultati seguenti. Anche l'ultima riga è importante:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Sappiamo che, sulle reti scansionate, Nmap ha scoperto 5 host attivi.



#### B. Sotto il cofano: analisi della rete tramite Wireshark



Ora analizzeremo più da vicino ciò che accade a livello di rete durante un rilevamento di rete eseguito tramite Nmap.



Come abbiamo visto nella sezione precedente, per impostazione predefinita Nmap utilizza il protocollo ARP per rilevare la presenza di host sulla rete locale:



![nmap-image](assets/fr/27.webp)



pacchetti aRP acquisiti durante la scansione di una rete locale con Nmap e le sue opzioni predefinite



È quindi in grado di rilevare praticamente tutti gli host della rete locale, poiché la risposta a una richiesta ARP è generalmente fornita da tutti gli host attivi sulla rete e non appare in alcun modo sospetta.



Per le reti remote, Nmap utilizza una combinazione di tecniche:



![nmap-image](assets/fr/28.webp)



iCMP e i pacchetti TCP catturati durante la scansione di una rete remota con Nmap e le sue opzioni predefinite



Per essere più precisi, Nmap utilizza un pacchetto ICMP echo (il caso classico di ping) e un pacchetto ICMP Timestamp, solitamente utilizzato per calcolare i tempi di transito dei pacchetti. Spera di ottenere una risposta da host su reti remote.



Ma c'è di più. Nell'acquisizione di Wireshark qui sopra si può notare che i pacchetti **TCP SYN** vengono sistematicamente inviati sulle porte TCP/443 di ogni potenziale host delle reti da scansionare, così come i pacchetti **TCP ACK** sulla porta TCP/80.



**Perché inviare pacchetti TCP alle porte come parte della scoperta della rete?



L'invio di un pacchetto SYN a una determinata porta consente a Nmap di **determinare se un servizio è in ascolto su quella porta**. Se un host risponde a un pacchetto SYN con un pacchetto SYN/ACK, ciò indica che è attivo e che un servizio è in ascolto su quella porta. Nmap tenta quindi la fortuna su questo servizio, **anche se non si ottiene alcuna risposta al ping**.



L'invio di un pacchetto ACK a una determinata porta consente a Nmap di **determinare se un firewall è presente su quell'host**. Se un host risponde a un pacchetto ACK con un pacchetto RST (Reset), ciò indica che probabilmente su quell'host è presente un firewall che blocca il traffico non richiesto. L'host tradisce così la sua presenza sulla rete, anche se non ha risposto ad altre richieste.



È importante notare, tuttavia, che il rilevamento del firewall con questa tecnica potrebbe non essere perfettamente affidabile in tutti i casi. Alcuni host possono ricevere risposte RST generate per motivi diversi dalla presenza di un firewall, come ad esempio una configurazione specifica del servizio o del sistema operativo. Inoltre, i moderni firewall possono essere configurati per non rispondere ai tentativi di rilevamento di questo tipo.



Ora abbiamo fatto molta strada e siamo in grado di eseguire la scoperta di base della rete. Ora esamineremo alcune altre opzioni che ci daranno un maggiore controllo sul comportamento di Nmap.



### III. Individuazione della rete senza scansione delle porte con Nmap



Come avrete notato, per impostazione predefinita Nmap **esegue una scansione delle porte in seguito alla scoperta di un host attivo**, il che comporta un'enorme quantità di pacchetti e di attesa per le risposte alla nostra scansione. Se avete 5 host sulla vostra rete, Nmap cercherà di controllare lo stato di circa 5.000 porte, il che richiederà più tempo.



Tuttavia, è possibile utilizzare le opzioni di Nmap per eseguire **solo una scoperta degli host attivi** su una rete, senza scoprire i loro servizi.



Se si vuole solo sapere quali host sono raggiungibili, senza alcuna informazione sui servizi e sulle porte che espongono, si può usare l'opzione "-sn" per eseguire **solo una scansione utilizzando richieste ICMP Echo (ping) e ARP**. In altre parole, disabilitare del tutto la scansione delle porte:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Ecco il risultato di una ricerca di rete Nmap eseguita senza scansione delle porte:



![nmap-image](assets/fr/29.webp)



Risultato di una ricerca di rete senza scansione delle porte con Nmap.



Abbiamo già accennato alle possibili limitazioni dell'uso del solo ICMP per la scoperta degli host (per le reti remote). Ecco perché Nmap utilizza anche alcuni trucchi che possono tradire la presenza di un firewall o di un servizio specifico sugli host. Con l'aiuto delle opzioni, possiamo riutilizzare questi trucchi e persino estenderli, senza dover ricominciare con una scansione completa delle porte di ogni host scoperto.



A tale scopo, utilizzeremo le opzioni "-PS" (TCP SYN) e "-PA" (TCP ACK), che ci permetteranno di specificare le porte che desideriamo unire come parte della nostra scoperta di host, nonché l'opzione "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Questa scansione garantisce già una scoperta dell'host un po' più completa rispetto alle opzioni predefinite.



Stiamo iniziando a ottenere comandi piuttosto completi, utilizzando più opzioni. Questo perché conosciamo il funzionamento di Nmap e le limitazioni delle sue opzioni "predefinite", che a volte ci fanno perdere tempo o non ci fanno scoprire Elements importanti. È proprio questo il motivo per cui bisogna dedicare del tempo alla sua padronanza!



Per dettagliare le opzioni del nostro ultimo ordine:





- "`-sn`: disabilita la scansione delle porte per ogni host attivo scoperto da Nmap.





- "`-PP`: abilita l'eco ICMP (ping scan) per la scoperta degli host.





- "`-PS <PORT>`": invia un pacchetto TCP SYN sulla/e porta/e indicata/e per rilevare qualsiasi servizio attivo che tradisca la presenza di un host che non ha risposto al ping.





- "`-PA <PORT>`": invia un pacchetto TCP ACK sulla/e porta/e indicata/e per rilevare eventuali firewall attivi che tradiscono la presenza di un host che non ha risposto al ping.




Nell'esempio precedente, per l'opzione "-PS" ho specificato le porte che considero più frequentemente esposte nei miei contesti Nmap. Queste diverse porte saranno poi testate su ogni host, non per vedere se il servizio che ospitano è realmente attivo, ma per vedere se questo ci permette di scoprire un host che non ha risposto al nostro ICMP Echo pur essendo ancora attivo (tramite una risposta dal servizio o dal firewall dell'host).



Ecco cosa si può vedere in un'acquisizione di rete effettuata al momento di una scansione di questo tipo, in questo caso un estratto su un singolo host di destinazione:



![nmap-image](assets/fr/30.webp)



pacchetti inviati da Nmap durante l'esplorazione avanzata della rete, senza scansione delle porte



Troviamo i pacchetti TCP SYN, TCP ACK sulla porta TCP/80 e ICMP echo. Nmap eseguirà tutti questi test per ogni host preso di mira dalla nostra scansione di rilevamento della rete.



### IV. Utilizzo di un file di risorse per il target con Nmap



Specificare i target può rivelarsi rapidamente complesso nei sistemi informatici reali, che a volte possono essere costituiti da decine o centinaia di reti, sottoreti e VLAN. Per questo motivo è più facile utilizzare un file come fonte per Nmap piuttosto che specificarli uno per uno sulla riga di comando.



Per iniziare, creare un semplice file contenente una voce per riga:



![nmap-image](assets/fr/31.webp)



contenente un target (host o rete) per riga



Quindi, possiamo utilizzare tutte le opzioni di Nmap viste finora e specificare l'opzione "-iL <percorso/file>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap includerà quindi nella sua scansione tutti gli obiettivi contenuti nel nostro file.



Se si vuole essere sicuri che tutti gli obiettivi vengano presi in considerazione, è possibile utilizzare l'opzione "-sL -n". Nmap interpreterà solo i CIDR e gli host presenti nel file e li visualizzerà, senza inviare alcun pacchetto sulla rete:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



In questo modo si garantisce che l'elenco degli host da scansionare sia accurato.



Un ultimo importante suggerimento che vorrei condividere con voi riguarda l'**esclusione di un host o di una rete nell'ambito di una scansione**. La necessità di escludere un host può essere necessaria in diversi casi, in particolare se vogliamo essere sicuri che **un componente sensibile del sistema informatico non venga disturbato o interrotto dalle nostre scansioni**.



Esempi frequenti di tali esigenze si hanno quando un'azienda possiede apparecchiature industriali (PLC) o sanitarie. Tali apparecchiature sono talvolta mal progettate e non sono affatto destinate a ricevere pacchetti mal formattati o troppo numerosi. Per ovvie ragioni di disponibilità o di rischio aziendale/umano, è preferibile escluderle dai test.



Per escludere indirizzi IP o reti dalla nostra scansione, possiamo usare l'opzione "--exclude" di Nmap, ad esempio:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



In questo esempio, sto eseguendo la scansione della rete "192.168.1.0/24" ma escludendo l'host "192.168.1.140" che si trova lì. Nessun pacchetto verrà inviato da Nmap a questo host. Un altro esempio di esclusione di sottorete:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Allo stesso modo, eseguo la scansione della rete grande "10.0.0.0/16", ma la rete "10.0.100.0/24" non viene scansionata. Anche in questo caso, consiglio di utilizzare l'opzione "-sL -n" per avere una visione molto chiara di quali host verranno scansionati e quali esclusi dalla scansione, soprattutto se si opera in un contesto sensibile.



### V. Individuazione della rete e scansione delle porte



Ora possiamo combinare quanto appreso in questa sezione con quanto appreso nella sezione precedente sulle opzioni di scansione delle porte. Per impostazione predefinita, abbiamo visto che Nmap scansiona le 1000 porte più frequenti su ogni host attivo che scopre. Abbiamo visto come impedire questo comportamento se non lo vogliamo, ma possiamo controllarlo completamente e persino estenderlo se lo desideriamo.



Ad esempio, il comando seguente verifica la presenza di un servizio in ascolto sulla porta TCP/22 su ogni host scansionato:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap esegue innanzitutto un'individuazione della rete per elencare gli host attivi e, per ciascuno di essi, controlla che sia presente un servizio sulla porta TCP/22.



Allo stesso modo, possiamo eseguire una scansione completa di tutte le porte TCP su ogni host individuato sulla rete "192.168.0.0/24", escludendo ad esempio l'host "192.168.0.4":



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Siete liberi di combinare tutte le opzioni che abbiamo imparato finora per soddisfare le vostre esigenze.



### VI. Conclusione



In questa sezione abbiamo visto come utilizzare Nmap per mappare la rete utilizzando varie opzioni. Ora abbiamo una conoscenza approfondita degli obiettivi delle nostre scansioni, nonché del comportamento di Nmap nella scansione delle porte e del metodo di rilevamento degli host. E soprattutto sappiamo quali sono i comportamenti e i limiti predefiniti di Nmap e come utilizzare le sue opzioni principali per andare oltre.



Nella prossima sezione, esamineremo i meccanismi e le opzioni per scoprire le versioni dei servizi e dei sistemi operativi scansionati da Nmap.




## 6 - Rilevare le versioni dei servizi e del sistema operativo con Nmap



### I. Presentazione



In questa sezione impareremo a utilizzare Nmap per scoprire e rilevare con precisione le versioni dei servizi e dei sistemi operativi utilizzati dagli host sottoposti a scansione. Verrà dato uno sguardo dettagliato a come Nmap svolge questo compito e alle limitazioni dello strumento per comprendere e interpretare meglio i suoi risultati.



Come abbiamo visto nelle sezioni precedenti di questa guida, per impostazione predefinita, Nmap non controlla quale servizio è esposto sulle porte che scansiona e considera aperte. Quindi, se si sta ascoltando un servizio web sulla porta TCP/22, Nmap continuerà a segnalarlo come aperto, ma come un servizio `SSH'. Questo perché utilizza un [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) locale al vostro sistema per cercare una relazione tra una porta/protocollo e il nome di un servizio (il file `/etc/services/`).



Nella maggior parte dei casi, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) fornirà le informazioni corrette, poiché in un ambiente di produzione è raro trovare casi del genere. Tuttavia, i casi rimanenti sono situazioni in cui un servizio classico ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, ecc.) è esposto su una porta non classica (ad esempio 2022 per un servizio SSH), nel qual caso Nmap non troverà una corrispondenza nel suo database locale, o una che non corrisponde alla realtà, e si perderanno informazioni importanti.



Fortunatamente, Nmap offre opzioni e meccanismi molto precisi per scoprire quale servizio esatto si nasconde dietro una porta aperta. Dispone persino di un database di query e firme per identificare le tecnologie e le versioni esatte. Oltre ai servizi, Nmap può anche identificare la tecnologia utilizzata e la sua versione.



Questo è ciò che vedremo in questa sezione.



### II. Come rilevare una tecnologia o una versione



#### A. Promemoria su come identificare una tecnologia o una versione



L'identificazione di una tecnologia e di una versione comporta il recupero del nome del servizio, del CMS, dell'applicazione o del software in ascolto sulla porta in questione. Ad esempio, una pagina web è gestita da un CMS (`WordPress`), eseguita da un servizio web (`Apache`, IIS, Nginx) e ospitata da un server (Linux o Windows). Ma come si fa a sapere quale servizio web è in esecuzione?



La metodologia classica per trovare queste informazioni è il _banner grabbing_, che consiste semplicemente nel localizzare il punto in cui il servizio in questione visualizza queste informazioni e leggere i dati. Molto spesso, nella loro configurazione o elaborazione predefinita, i servizi mostrano il loro nome e persino la loro versione come prima risposta dopo una connessione.



![nmap-image](assets/fr/32.webp)



visualizzare una versione non appena viene stabilita una connessione TCP da un servizio FTP



Qui vediamo che una semplice connessione TCP a questo servizio tramite `telnet` produce un pacchetto TCP contenente la sua tecnologia e la sua versione.



Una volta che ci si è fatti un'idea del tipo di servizio con cui si ha a che fare, si possono anche inviare comandi o richieste specifiche a quel servizio per estrarne informazioni. Queste richieste/comandi possono anche essere inviati alla cieca (senza essere sicuri che si tratti del tipo di servizio giusto), nella speranza che uno di essi provochi una risposta dal servizio in questione.



In altri casi, più avanzati, è necessario inviare pacchetti specifici per provocare una reazione, ad esempio un errore, che fornirà informazioni dettagliate sulla versione o sulla tecnologia utilizzata.



Come si può immaginare, Nmap utilizzerà tutte queste tecniche per cercare di identificare il tipo esatto di servizio ospitato su una porta, nonché il nome della sua tecnologia e la versione.



#### B. Comprendere le sonde e le corrispondenze di Nmap



Per effettuare tutti questi controlli su ogni porta scansionata, Nmap utilizza un database locale che viene aggiornato frequentemente (proprio come il binario o i suoi moduli). Si tratta di un file di testo di diverse migliaia di righe: `/usr/share/nmap/nmap-service-probes`.



Questo file è composto da numerose voci, tutte organizzate intorno a due linee guida principali:





- La `Sonda`: è la definizione del pacchetto che Nmap invierà nel tentativo di provocare una reazione dal servizio da identificare. Pensate a un tentativo alla cieca come _Hello? Guten Tag? Pronto? Um... Buenos Dias forse? Non appena il servizio bersaglio riceve una sonda che comprende (cioè che parla il protocollo corretto), risponderà a Nmap, che avrà così la conferma del tipo di servizio.





- Match": si tratta di espressioni regolari che Nmap applica alla risposta ottenuta. Se l'invio di una richiesta HTTP GET ha provocato una risposta da parte del servizio, Nmap applicherà decine di espressioni regolari a questa risposta per identificare la presenza, ad esempio, delle parole `Apache`, `Nginx`, `Microsoft IIS`, ecc.




Esistono altre direttive per casi specifici, ma le principali per capire come funziona Nmap e personalizzarne l'uso sono queste. Per rendere più concreta questa parte teorica, ecco un esempio:



![nmap-image](assets/fr/33.webp)



esempio di sonda nel file `/usr/share/nmap/nmap-service-probes' di Nmap



Nella prima riga di questo esempio, vediamo una sonda di facile comprensione chiamata `GetRequest`. Si tratta di un pacchetto TCP contenente una richiesta HTTP GET vuota alla radice del servizio web utilizzando HTTP/1.0, seguita da un feed di riga e da una riga vuota.



La riga `port` indica a Nmap per quale porta inviare la sonda. Ciò consente di dare priorità ai test e di risparmiare tempo.



Infine, abbiamo due esempi di `match`. Il primo, ad esempio, categorizzerà il servizio web scansionato come `ajp13` se l'espressione regolare contenuta in questa riga corrisponde alla risposta del servizio ricevuta.



Per aiutarvi a capire come possono essere le sonde, ecco un elenco di alcune delle sonde che troverete in questo file (al momento della stesura di questa guida ce ne sono 188 in tutto).



![nmap-image](assets/fr/34.webp)



esempio di diverse sonde utilizzate da Nmap e presenti nel file `/usr/share/nmap/nmap-service-probes`._



I primi due (chiamati `NULL` e `GenericLines`) sono di particolare interesse, poiché inviano semplicemente un pacchetto TCP vuoto o contenente un'interruzione di riga. I servizi del server spesso si annunciano proprio non appena viene ricevuta una connessione, senza alcuna azione, comando o richiesta specifica da parte del client.



Ecco il caso di un _match_ leggermente più complesso:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



L'espressione regolare esatta è contenuta qui tra la `m|` e la `|`, che delimita qualsiasi espressione regolare in questo file. Si consiglia di leggere l'intero esempio. Si noterà una selezione nell'espressione regolare: `([\d.]+)`, usata per isolare una versione. Questo esempio definisce anche altri Elements come il nome del prodotto `p/nginx/`, la versione recuperata `v/$1/` e il CPE con la versione `cpe:/a:igor_sysoev:nginx:$1/`.



Un CPE (Common Platform Enumeration) è un sistema di notazione standardizzato utilizzato per identificare e descrivere software e hardware. Questo formato consente una gestione più efficiente delle vulnerabilità e delle configurazioni di sicurezza, e soprattutto un modo unificato di rappresentarle, indipendentemente dal prodotto in questione. Ecco due esempi di CPE: `cpe:/o:microsoft:windows_8.1:r1` e `cpe:/a:apache:http_server:2.4.35`



Qui identifichiamo chiaramente i loro tipi `o` per il sistema operativo, `a` per l'applicazione, il fornitore, il prodotto e le versioni.



Quindi, in caso di _match_ con una di queste espressioni regolari, recupereremo non solo il nome del servizio, ma anche la sua versione e l'esatto CPE, rendendo più facile trovare le CVE che hanno un impatto su questa versione. Troverete queste informazioni nell'output standard di Nmap e vedrete che sono molto utili per altri scopi che tratteremo in alcune sezioni.



La sintassi esatta di _matches_ e, più in generale, delle direttive del file `/usr/share/nmap/nmap-service-probes' non si ferma qui e può sembrare piuttosto complessa se non si è abituati a manipolare Nmap e i suoi risultati. Tuttavia, dovreste almeno tenere a mente la sua esistenza e il suo funzionamento generale, che vi tornerà utile in seguito quando vorrete capire o eseguire il debug di un risultato, personalizzare una scansione o persino contribuire allo sviluppo di Nmap.



### III. Uso di Nmap per rilevare le versioni



Ora useremo tutti questi complessi meccanismi di _Probe_ e _Match_ tramite una semplice opzione: `-sV`. Questa opzione dice semplicemente a Nmap: cerca di scoprire esattamente quali servizi e versioni delle porte sono state impostate come aperte.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Ecco un esempio completo del risultato di tale comando:



![nmap-image](assets/fr/35.webp)



i risultati del rilevamento della versione di Nmap delle applicazioni esposte in rete



Qui possiamo vedere che Nmap è riuscito a identificare tutte le versioni dei servizi di rete esposti da questo obiettivo e visualizza queste informazioni in una nuova colonna `VERSION`. È possibile visualizzare informazioni piuttosto precise, anche sul sistema operativo, se queste informazioni fanno parte della firma recuperata.



Per capire in dettaglio cosa succede durante una scansione di vulnerabilità, si può usare l'opzione `--version-trace`. Questa opzione fornisce una visualizzazione in modalità debug, mostrando la _Probe_ che ha portato al rilevamento:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Di conseguenza, avremo molte informazioni da selezionare. Cercare di identificare le righe che iniziano con `Service scan Hard match`. Si vedranno quindi righe come queste:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Possiamo vedere chiaramente quali _Probes_ sono state utilizzate per rilevare la tecnologia e la versione (in questo caso le _Probes_ `NULL` e `GetRequest`), così come le informazioni recuperate.



### IV. Test di padronanza e accuratezza del rilevamento



Ora torneremo a una direttiva del file `/usr/share/nmap/nmap-service-probes' che non abbiamo esaminato in precedenza:



![nmap-image](assets/fr/36.webp)



direttiva `rarità` delle sonde nel file `/usr/share/nmap/nmap-service-probes`._



Questa direttiva viene utilizzata per indicare la rarità (cioè la priorità/probabilità) associata a una _Sonda_. Questa notazione da 1 a 9 consente di controllare la completezza dell'analisi eseguita da Nmap quando invia le _Sonde_. Nel sistema di "notazione" di Nmap, una rarità di 1 fornisce informazioni nella stragrande maggioranza dei casi, mentre una rarità di 8 o 9 rappresenta un caso molto particolare, specifico di una configurazione o di un servizio raramente presente.



Per essere più chiari, in un caso predefinito, Nmap invierà a ciascun servizio da identificare le _Sonde_ che hanno una rarità da 1 a 7. Per dare un'idea della distribuzione delle _Sonde_ per _rarità_, ecco il loro numero:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Può sembrare controintuitivo, ma ci sono più sonde di `rarità' 8 e 9 rispetto alle altre. Questo è dovuto al fatto che le sonde di rarità 1 sono generiche e funzionano nella maggior parte dei casi, indipendentemente dal servizio (ricordate la sonda `NULL` che invia semplicemente un pacchetto TCP vuoto). Mentre le Sonde più complesse sono quasi uniche per ogni servizio.



Se si desidera gestire manualmente le sonde da usare nella scansione delle versioni, si può usare l'opzione `--version-intensity`. Ecco due esempi:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Per concludere l'argomento, ecco un esempio di _Probe_ 9 e 8:



![nmap-image](assets/fr/37.webp)



esempi di sonda a rarità 8 e 9 nel file `/usr/share/nmap/nmap-service-probes`._



Queste due _Sonde_ rilevano i server di Quake1 e Quake2 (il videogioco). Interessanti per i nostalgici, ma difficilmente utili nella vita di tutti i giorni.



A seconda delle vostre esigenze di precisione o velocità, ricordate che questo principio di "rarità" esiste e può influenzare il risultato.



### V. Uso di Nmap per rilevare i sistemi operativi



Vediamo ora come Nmap può aiutarci a rilevare i sistemi operativi degli host scansionati e rilevati su una rete. A tale scopo, utilizzare l'opzione `-O` (per `OS Scan`) di Nmap.



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Ecco un esempio dei risultati. In questo caso, Nmap ci dice che probabilmente si tratta di un sistema operativo Linux e ci offre varie statistiche sulla sua versione esatta.



![nmap-image](assets/fr/38.webp)



rilevamento della probabilità di identificazione di un sistema operativo da parte di Nmap



Per raggiungere questo obiettivo, Nmap utilizzerà una moltitudine di tecniche che funzionano in modo molto simile a _Probes_ e _Matches_ per il rilevamento di tecnologie e versioni. La differenza principale è che Nmap utilizzerà parametri di "basso livello" di ICMP, TCP, UDP e altri protocolli. Ecco due esempi di test per il rilevamento di un sistema operativo Microsoft Windows 11:



![nmap-image](assets/fr/39.webp)



esempi di test eseguiti da Nmap per rilevare un sistema operativo Windows 11



Ammettiamolo, questi test sono molto difficili da interpretare e non cercheremo di capirli a fondo nel contesto di un tutorial introduttivo su Nmap. Se volete approfondire l'argomento, il file contenente queste informazioni è `/usr/share/nmap/nmap-os-db`.



Tuttavia, è necessario sapere che il rilevamento del sistema operativo è più una probabilità stabilita da Nmap che una certezza.



### VI. Conclusione



In questa sezione abbiamo imparato a utilizzare le opzioni di Nmap per rilevare le tecnologie, le versioni e i sistemi operativi degli host e dei servizi scansionati. Ora abbiamo una buona comprensione del modo in cui Nmap ottiene queste informazioni da remoto. Abbiamo anche esaminato le opzioni per gestire la verbosità e l'accuratezza dei test, nonché le limitazioni dello strumento su questi argomenti.



Nella prossima sezione impareremo a utilizzare gli script NSE di Nmap per eseguire un'analisi di sicurezza del nostro sistema informatico. Se necessario, rileggete le ultime sezioni e non esitate a esercitarvi e a scavare nelle viscere dello strumento per padroneggiare meglio ciò che abbiamo imparato finora.




## 7 - Analisi della sicurezza: individuare le vulnerabilità



### I. Presentazione



In questa sezione impareremo a utilizzare lo strumento di scansione di rete Nmap per rilevare e analizzare le vulnerabilità sugli obiettivi delle nostre scansioni. In particolare, esamineremo le varie opzioni disponibili per svolgere questo compito e studieremo i limiti delle capacità dello strumento per comprendere e interpretare meglio i suoi risultati.



In questa prima sezione, daremo un'occhiata allo scanner di vulnerabilità di Nmap e vedremo come utilizzare le opzioni di base per il rilevamento delle vulnerabilità. Nelle sezioni successive, vedremo più da vicino come funziona questa funzione e come può essere personalizzata.



### II. Uso di Nmap per rilevare le vulnerabilità



Ora vogliamo utilizzare lo scanner di rete Nmap per rilevare le vulnerabilità nei servizi e nei sistemi del nostro sistema informatico. Ciò significa che oltre a scoprire gli host attivi, enumerare i servizi esposti e rilevare versioni e tecnologie, Nmap cercherà le vulnerabilità.



Per raggiungere questo obiettivo, Nmap si affida agli script NSE (_Nmap Scripting Engine_), che possono essere considerati come moduli che consentono un approccio granulare ai test.



Con le giuste opzioni, chiederemo a Nmap di utilizzare i suoi vari script NSE su ogni servizio scoperto, permettendoci di scoprire:





- Errori di configurazione ;





- Ulteriori e più avanzate scoperte di versioni e sistemi operativi ;





- Vulnerabilità note (CVE) ;





- Identificatori deboli ;





- Elements caratteristico di un'infezione da malware ;





- Possibilità di negazione del servizio ;





- Ecc.




Come si può vedere, gli script NSE estendono in modo significativo le capacità di Nmap in termini di operazioni di rete che può eseguire. E questo per eseguire operazioni molto più avanzate che in passato. La buona notizia è che, come al solito, queste funzioni possono essere utilizzate semplicemente tramite un'opzione e in un contesto predefinito. Questo è ciò che vedremo in seguito.



### III. Esempio di scansione delle vulnerabilità



Gli script NSE possono essere utilizzati quando si usa Nmap per scansionare una singola porta su un host, tutti i servizi su quell'host o tutti i servizi rilevati su più reti. Possiamo quindi utilizzare le opzioni che vedremo in tutti i contesti che abbiamo studiato finora.



Per abilitare la scansione delle vulnerabilità tramite una scansione Nmap, è necessario utilizzare l'opzione `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Ricordate che per impostazione predefinita, se non si specifica nulla, Nmap scansiona solo le 1000 porte più comuni. Non rileverà le vulnerabilità sulle porte più esotiche che gli obiettivi potrebbero esporre.



Prima di utilizzare questa funzionalità in un sistema informativo di produzione, vi invito a continuare a leggere il tutorial. Nelle sezioni successive, vedremo come controllare meglio l'impatto e i tipi di test che verranno eseguiti.



Riutilizzando ciò che abbiamo imparato in precedenza, possiamo, ad esempio, essere più completi e scansionare tutte le porte TCP di un obiettivo:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Ecco il risultato di una scansione Nmap utilizzando gli script NSE:



![nmap-image](assets/fr/40.webp)



esempio dei risultati di una scansione di vulnerabilità su un host tramite Nmap._



Qui vediamo la visualizzazione di informazioni aggiuntive di interesse nel contesto di un'analisi di vulnerabilità:





- Il servizio FTP è accessibile in modo anonimo e non è protetto da autenticazione. Lo script NSE incaricato di questa verifica ce lo dice e mostra anche parte della struttura ad albero del servizio FTP. Qui vediamo che abbiamo accesso alla directory `C` del sistema Windows!





- Lo script NSE incaricato di recuperare i servizi Web avanzati visualizza il titolo della pagina, dando un'idea più precisa del servizio Web ospitato.





- Abbiamo anche una mini analisi della configurazione del servizio SMB (script `smb2-time`, `smb-security-mode` e `smb2-security-mode`). Le informazioni sono visualizzate in modo leggermente diverso, dopo il risultato della scansione della rete, per facilitarne la lettura. In particolare, queste informazioni indicano l'assenza di firme SMB Exchange. Questa debolezza della configurazione consente al bersaglio di essere controllato. Questa debolezza della configurazione consente di utilizzare l'obiettivo in un attacco SMB Relay, una notevole falla di sicurezza spesso sfruttata nei test di intrusione/cyber-attacco.




Naturalmente, questo è solo un esempio. Nmap dispone di script NSE per molti servizi, mirati a un'ampia gamma di vulnerabilità. Nella prossima sezione esamineremo più da vicino queste possibilità.



Per concludere questa introduzione alla scansione delle vulnerabilità, ecco un comando completo per la scoperta della rete, la scansione delle porte TCP, il rilevamento delle versioni e delle vulnerabilità:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Ecco un comando che inizia ad assomigliare a casi d'uso più realistici di Nmap!



### IV. Comprendere i limiti di Nmap nella scansione delle vulnerabilità



Sia chiaro: Nmap non è in grado di effettuare un test di penetrazione completo del vostro sistema informatico, né di simulare un'operazione di Red Team. Ha diverse limitazioni di cui dovete essere consapevoli se non volete avere un falso senso di sicurezza:





- Copertura limitata**: sebbene gli script NSE di Nmap siano potenti, la loro copertura di test può essere limitata rispetto ad altri strumenti specializzati nella scoperta delle vulnerabilità. Alcune vulnerabilità potrebbero non essere coperte dagli script NSE disponibili, come le vulnerabilità di Active Directory, l'esposizione di dati sensibili o i casi più avanzati di applicazioni web vulnerabili.





- Complessità della vulnerabilità**: alcuni tipi di vulnerabilità possono essere difficili da rilevare con gli script NSE a causa della loro complessità. Ad esempio, le vulnerabilità che richiedono un'interazione complessa con un servizio remoto potrebbero non essere rilevate efficacemente da Nmap (come nel caso di permessi eccessivi in una condivisione di file o di una falla nel controllo dei permessi in un'applicazione web).





- Rilevamento passivo**: Nmap si concentra principalmente sulle scansioni attive per rilevare le vulnerabilità, il che significa che potrebbe non rilevare efficacemente le potenziali vulnerabilità senza stabilire una connessione attiva con gli host di destinazione. Le vulnerabilità che non si manifestano durante una scansione attiva possono quindi non essere rilevate (come nel caso di un'iniezione di codice in un'applicazione web).





- Dipendenza dagli aggiornamenti**: Il [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) degli script NSE di Nmap è in continua evoluzione, ma può esserci un ritardo tra la scoperta di una nuova vulnerabilità e l'aggiunta di uno script corrispondente a Nmap. Di conseguenza, Nmap potrebbe non essere sempre aggiornato con le ultime vulnerabilità.





- Falsi positivi e falsi negativi**: come ogni strumento di sicurezza, gli script NSE di Nmap possono produrre falsi positivi (falsi avvisi di vulnerabilità) o falsi negativi (vulnerabilità reali non rilevate). È un aspetto da tenere presente quando si analizzano i risultati di Nmap.




È quindi importante capire cosa fa e cosa non fa Nmap e, allo stesso modo, sapere come interpretare i suoi risultati. In particolare, nel corso di questo tutorial abbiamo visto che le opzioni predefinite possono farci perdere importanti Elements che possono essere scoperti con un uso attento.



Che siate un amministratore di sistema di rete, un ingegnere della sicurezza o addirittura un CISO, l'uso di Nmap vi offre una panoramica dello stato di sicurezza di un sistema informatico. Si tratta di un primo passo importante per la sicurezza di un sistema, che può essere eseguito regolarmente dal team IT. Tuttavia, non dovrebbe sostituire l'intervento e la consulenza di esperti di [cybersecurity] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), che saranno in grado di scoprire i punti deboli in modo molto più completo di Nmap.



### V. Conclusione



In questa prima sezione del Modulo 3 abbiamo introdotto la scansione delle vulnerabilità tramite Nmap. Ora sappiamo come utilizzare l'opzione principale per eseguire questo compito, ma conosciamo anche i limiti dell'esercizio. Nella prossima sezione esamineremo più da vicino questa funzionalità, utilizzando gli script NSE per decuplicare la potenza di Nmap.



## 8 - Utilizzo degli script NSE di Nmap



### I. Presentazione



In questa sezione, daremo uno sguardo approfondito agli script NSE (_Nmap Scripting Engine_). In particolare, vedremo perché sono uno dei grandi punti di forza di questo strumento, come funzionano e come sfogliare e utilizzare i numerosi script esistenti.



Questa sezione fa seguito alla precedente esercitazione, in cui abbiamo imparato a utilizzare le funzioni di scansione delle vulnerabilità di Nmap in modo elementare. Ora vedremo più da vicino come funziona [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/), in modo da poter effettuare ancora una volta scansioni più precise e controllate.



### II. Il concetto di script NSE di Nmap



Gli script NSE di Nmap consentono di estendere le sue funzionalità in modo estremamente flessibile. Sono scritti in LUA, un linguaggio di scripting più facile da gestire e da accedere rispetto al C o al C# utilizzati da Nmap. Il vantaggio di utilizzare uno script LUA con Nmap piuttosto che uno strumento autonomo è che ci permette di sfruttare la velocità di esecuzione e le funzionalità standard di Nmap (rilevamento di host, porte e versioni, ecc.).



Gli script sono organizzati per categoria e uno stesso script può appartenere a più di una categoria:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Tecnicamente, le categorie a cui appartiene uno script sono indicate direttamente nel suo codice.



![nmap-image](assets/fr/41.webp)



categorie di script nSE `ftp-anon`._



Questo esempio mostra parte del codice dello script NSE `ftp-anon.nse`, la cui esecuzione è stata vista nella sezione precedente.



### III. Elenco degli script NSE esistenti



Per impostazione predefinita, gli script NSE di Nmap si trovano nella directory `/usr/share/nmap/scripts/`, senza una specifica struttura ad albero o gerarchia. Ecco una panoramica dei contenuti di questa directory:



![nmap-image](assets/fr/42.webp)



estrae il contenuto della directory `/usr/share/nmap/scripts/` contenente gli script NSE._



Questa directory contiene oltre 5.000 script NSE. Nella maggior parte dei casi, la prima parte del nome dello script contiene il protocollo o la categoria a cui appartiene. Questo ci permette di ordinare l'elenco, ad esempio se vogliamo elencare tutti gli script che si rivolgono al servizio FTP:



![nmap-image](assets/fr/43.webp)



elenco degli script NSE Nmap con nomi che iniziano con `ftp-`._



Nmap non offre un'opzione per sfogliare ed elencare gli script NSE; si può usare il comando `-script-help` seguito dal nome di una categoria o da una parola:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Tuttavia, il risultato sarà il nome di ogni script e la sua descrizione, il che non è ottimale se la ricerca porta a diverse decine di script:



![nmap-image](assets/fr/44.webp)



risultato dell'utilizzo del comando `-script-help' di Nmap



A mio parere, il metodo più efficace è quello di usare i classici comandi Linux nella directory `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Sentitevi liberi di sfogliare il codice dei moduli che vi interessano, per capire meglio come funziona uno script NSE.



### IV. Utilizzo degli script NSE di Nmap



Ora impareremo a eseguire scansioni di vulnerabilità selezionando attentamente gli script NSE che ci interessano.



#### A. Selezionare gli script per categoria



Per cominciare, si può scegliere di eseguire tutti gli script appartenenti a una categoria specifica. Dobbiamo indicare questa o queste categorie a Nmap con l'argomento `-script <categoria>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Questo primo comando è l'equivalente del comando `nmap -sC`. Per impostazione predefinita, Nmap selezionerà gli script della categoria `default`, ma questo è solo a titolo indicativo. Il comando successivo, ad esempio, utilizzerà tutti gli script della categoria `discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Come abbiamo visto, alcune categorie ci permettono di identificare rapidamente cosa fanno i relativi script NSE (`discovery`, `vuln`, `exploit`), mentre altre definiscono il livello di rischio, rilevamento o stabilità del test eseguito. Se ci troviamo in un contesto delicato e non abbiamo una buona conoscenza delle diverse azioni eseguite dalla nostra selezione di script, possiamo scegliere di combinare le selezioni per scegliere solo gli script che rientrano nelle categorie `discovery` e `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Se si vuole escludere in modo assoluto ed esplicito gli script dalle categorie `dos` e `intrusivo`, si può usare la seguente notazione:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Si noti che, specificando le condizioni di esclusione come sopra, si otterrà l'uso di tutte le altre categorie non esplicitamente escluse. Per essere più corretti, si potrebbe specificare, ad esempio:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Ecco alcuni esempi di come gestire gli script NSE per categoria, soprattutto quando si utilizza Nmap per l'analisi delle vulnerabilità in contesti reali.



#### B. Selezionare i copioni come unità



Si può anche scegliere di eseguire un singolo test specifico durante un'analisi, un test corrispondente a uno script NSE. Per farlo, è necessario specificare il nome dello script nel parametro `script <nome>`. Prendiamo come esempio lo script `ftp-anon.nse`:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Abbiamo quindi un risultato molto preciso:



![nmap-image](assets/fr/45.webp)



risultato dell'utilizzo dello script NSE `ftp-anon` su una porta FTP via Nmap._



Vediamo il risultato dell'esecuzione dello script `ftp-anon` sulla porta 21 e su nessun'altra porta, perché abbiamo specificato l'opzione `-p 21`. Avremmo anche potuto eseguire una scansione di base delle porte, eseguendo lo script NSE `ftp-anon` solo sui servizi FTP rilevati:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Pertanto, Nmap avrebbe eseguito questo test di connessione anonima anche se avesse trovato un servizio FTP su un'altra porta.



Per una breve descrizione di ciò che fa uno script NSE, si può usare l'opzione `-script-help' di cui sopra:



![nmap-image](assets/fr/46.webp)



aiutare a visualizzare i risultati per lo script NSE `sshv1`._



In breve, ancora una volta possiamo riutilizzare tutte le opzioni di scoperta della rete, i servizi, le versioni e le tecnologie che abbiamo usato finora!



#### C. Gestione degli argomenti degli script



Nel corso dell'utilizzo di Nmap, ci si imbatte in alcuni script NSE che richiedono argomenti di input per funzionare correttamente. Vediamo ora come passare gli argomenti a questi script tramite le opzioni di Nmap.



Come esempio, prendiamo lo script `ssh-brute`, che consente di eseguire un attacco di forza bruta al servizio SSH.



Un classico attacco di forza bruta consiste nel testare diverse password (a volte milioni) nel tentativo di autenticarsi a un account specifico. Tentando un numero così elevato di password, l'attaccante scommette sulla probabilità che l'utente abbia utilizzato una password debole del dizionario di password utilizzato per l'attacco.



Questo script ha opzioni "predefinite", che possiamo personalizzare per adattarle al nostro contesto. Nel contesto di questo attacco, ad esempio, possiamo fornire a Nmap l'elenco degli utenti e il dizionario delle password da utilizzare. Per quanto ne so, non è possibile elencare facilmente gli argomenti richiesti per uno script, quindi il modo più affidabile è visitare il sito ufficiale di Nmap. Un link diretto alla documentazione di uno script NSE può essere ottenuto in risposta all'opzione `-script-help':



![nmap-image](assets/fr/47.webp)



risultato della visualizzazione dell'aiuto per lo script NSE `ssh-brute` con un link a nmap.org._



Cliccando sul link indicato, si arriva a questa pagina web del sito [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



elenco di argomenti che possono essere passati allo script NSE `ssh-brute` di Nmap



Qui abbiamo una chiara visione degli argomenti che possono essere usati, i principali nel nostro contesto sono `passdb` (file contenente un elenco di password) e `userdb` (file contenente un elenco di utenti). La documentazione si riferisce alle librerie interne di Nmap, in quanto questi meccanismi di forza bruta e le opzioni associate sono mutualizzati per essere usati in modo uniforme in diversi script (`ssh-brute`, `mysql-brute`, `mssql-brute`, ecc.) e quindi avranno più o meno gli stessi argomenti:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Come si può vedere in quest'ultimo comando, è possibile specificare gli argomenti necessari a uno script Nmap utilizzando l'opzione `-scripts-args key=value,key=value`. Ecco un possibile risultato dell'output di Nmap quando si esegue un brute force SSH tramite lo script NSE `ssh-brute`:



![nmap-image](assets/fr/49.webp)



risultato di un'esecuzione bruteforce di SSH tramite Nmap._



Come si può notare, le informazioni generate dagli script NSE sono precedute da `NSE: [nome dello script]` nell'output interattivo (output del terminale), rendendole più facili da trovare. Nella visualizzazione abituale dei risultati di Nmap, abbiamo semplicemente un riepilogo che indica se sono stati scoperti o meno identificatori deboli (comprese le password, ricordate).



Per fare un ulteriore passo avanti e per ricordare che tutto questo può essere usato in aggiunta a tutte le opzioni che abbiamo già esaminato, ecco un comando che scoprirà la rete `10.10.10.0/24`, scansionerà le 2000 porte TCP più frequenti ed eseguirà una ricerca di accesso anonimo sui servizi FTP e una campagna di forza bruta sui servizi SSH:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Questo è solo un esempio dei molti script disponibili e delle loro opzioni. Ma ora abbiamo un'idea più precisa di come utilizzare gli script NSE, se richiedono argomenti e come passarli a Nmap.



### V. Conclusioni



In questa sezione abbiamo imparato a utilizzare gli script NSE di Nmap per eseguire varie operazioni. Vi invito a scoprire le diverse categorie di script e gli script stessi, per vedere quanti test possono automatizzare.



Per diverse sezioni abbiamo accumulato opzioni di scoperta, scansione ed enumerazione più o meno avanzate. Ormai dovreste essere consapevoli che l'output e la visualizzazione dei risultati di Nmap iniziano a diventare piuttosto estesi, a volte persino troppo prolissi per il nostro terminale. Nella prossima sezione impareremo a gestire questo output, in particolare memorizzandolo in file di vari formati.






## 9 - Gestione dei dati di output di Nmap




### I. Presentazione



In questa sezione esamineremo l'output prodotto da Nmap e in particolare le varie opzioni di formattazione. Vedremo che Nmap può produrre diversi formati di output per soddisfare le diverse esigenze e che anche questo è uno dei grandi punti di forza di questo strumento.



Per impostazione predefinita, Nmap offre una vista dettagliata dei risultati delle scansioni e dei test eseguiti. Sono inclusi gli host e i servizi scansionati, quelli rilevati come accessibili, le specifiche delle porte aperte, il loro stato e la loro versione. Inoltre, i dettagli degli script NSE sono disponibili anche nell'output del terminale. Tuttavia, questo output può diventare rapidamente voluminoso, anche con una chiara formattazione delle informazioni, il che può rendere difficile trovare informazioni precise nei risultati.



### II. Padroneggiare i formati di output di Nmap



#### A. Salvare i risultati della scansione in un file di testo



Per semplificare le cose, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) consente di salvare facilmente i risultati in un file di testo. Questo può essere utile per l'archiviazione, il confronto con altri test, ma anche per sfogliare l'output con strumenti di videoscrittura o linguaggi di scripting specializzati, come Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, ecc. Per memorizzare l'output standard di Nmap in un file di testo, si può usare l'opzione `-oN <nome file>` (la "N" in "normale"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Non c'è da sorprendersi, perché Nmap visualizzerà il suo solito output standard nel nostro terminale, ma anche nel file specificato.



#### B. Output di generate Nmap in formato condensato



Esiste anche un secondo formato di output nello stile "testo" che può essere facilmente interpretato da un essere umano: il formato "greppable".



Questo formato è stato creato per fornire una visione "condensata" dell'output di Nmap, strutturato in modo tale da facilitarne l'elaborazione da parte di strumenti come `grep`. Vediamo un esempio di questo tipo di output:



![nmap-image](assets/fr/50.webp)



scansione della rete nmap e output in formato "greppable"



In questo caso, ho eseguito un rilevamento della rete, una scansione delle porte e un'analisi delle tecnologie e delle versioni su una rete /24, quindi ho memorizzato l'output in un file in formato "greppable". Alla fine ho ottenuto un file contenente 2 righe per ogni host attivo:





- La prima riga mi dice che il tal host è _Up_;





- Una seconda riga mi dice quali porte sono state scansionate, il loro stato e le informazioni sulla tecnologia e sulla versione recuperate in un formato molto specifico: `<porta>/<stato/<protocollo>/<servizio>/<versione>/,`




Questa formattazione con un delimitatore fisso consente una rapida elaborazione con strumenti di elaborazione testi come `grep`, o con linguaggi di scripting e programmazione. Il comando seguente, ad esempio, mi permette di recuperare facilmente le informazioni sull'host `10.10.10.5` nel caso di un'enorme scansione eseguita da Nmap il cui output sarebbe difficile da consultare:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Al contrario, posso anche elencare facilmente tutti gli host che hanno la porta 21 aperta, dato che le porte e l'IP sono sulla stessa riga:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Per ottenere questo tipo di output, è necessario utilizzare l'opzione `-oG <filename>.gnmap` (la "G" di "grep"). Per abitudine, io uso l'estensione `.gnmap' per questo tipo di file, ma potete usare quello che preferite:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Questo formato può essere utilizzato per diversi scopi ed è particolarmente utile per lo scripting/sorting rapido. Tuttavia, tende a essere abbandonato in favore del formato che vedremo in seguito.



nota: il formato greppable `-oG` è stato ufficialmente deprecato da Nmap 7.90. Può ancora essere usato per compatibilità. Può ancora essere usato per motivi di compatibilità, ma si raccomanda di usare il formato XML o normale per qualsiasi sviluppo o parsing automatizzato



#### C. Formato XML per l'output di Nmap



L'ultimo formato che vale la pena menzionare in questa guida è XML. A differenza dei due formati precedenti, questo non è progettato per essere letto dall'uomo, ma da altri strumenti o script.



XML (_eXtensible Markup Language_) è un linguaggio di markup utilizzato per memorizzare e trasportare dati, offrendo una struttura gerarchica tramite tag personalizzati.



All'interno di Nmap, il formato XML viene utilizzato per generate rapporti dettagliati sulle scansioni eseguite, comprese le informazioni su host, porte e vulnerabilità rilevate, nonché informazioni aggiuntive non visualizzate nell'output standard di Nmap.



Per ottenere un file di output in formato XML, è necessario utilizzare l'opzione `-oX` ("O" da "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Il risultato è l'output standard di Nmap nel terminale e un file in formato XML nella directory corrente.



Naturalmente, il formato XML non è progettato per essere letto e interpretato dall'uomo. Tuttavia, se si desidera eseguire scripting o analisi automatizzate su questo formato di output di Nmap, è comunque necessario avere un'idea dei tag e della struttura utilizzata. Ad esempio, ecco una parte del contenuto del file XML creato da Nmap, che mostra i risultati della scansione di 1 host:



![nmap-image](assets/fr/51.webp)



esempio di un record XML per 1 host durante una scansione Nmap



Ci sono molte informazioni e siamo particolarmente interessati alle due porte aperte:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Questo formato facilita l'analisi automatica dei risultati, in quanto ogni informazione è ordinata in un tag o attributo dedicato e denominato. In particolare, troviamo un'informazione che non abbiamo mai incontrato prima: il CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Abbiamo accennato brevemente alla CPE nella sezione 2 del modulo 2 e questa informazione viene determinata nelle corrispondenze durante il rilevamento della versione. Nmap utilizza i suoi meccanismi di rilevamento dei servizi, delle tecnologie e delle versioni per trovare il CPE associato.



Questo ci permette di riutilizzare queste informazioni con i database e le applicazioni che le utilizzano. Mi riferisco in particolare al database NVD, che fa riferimento ai CVE. Per ogni CVE, contiene le CPE interessate dalla vulnerabilità. Ecco un esempio di CVE relativo a `a:microsoft:internet_information_services:7.5` dal database NVD:



![nmap-image](assets/fr/52.webp)



presenza di un CPE nei dettagli di un CVE nel database NVD



Ora abbiamo una migliore comprensione dei vantaggi di questo formato, che offre una struttura molto chiara delle informazioni e contiene tutti i dati raccolti o elaborati da Nmap.



Per riflesso, salvo sistematicamente le mie scansioni Nmap in tutti e tre i formati contemporaneamente. Ciò è reso possibile dall'opzione `-oA <nome>` ("A" per "Tutti"), che crea un file `<nome>.nmap`, un file `<nome>.xml` e un file `<nome>.gnmap`. In questo modo sono sicuro che non mancherà nulla quando avrò bisogno di rivedere i risultati.



Con questi tre formati, si dovrebbe avere tutto ciò che serve per salvare ed eventualmente elaborare i risultati di Nmap in modo automatizzato. Utilizzeremo nuovamente il formato XML nella prossima sezione, quando esamineremo l'utilizzo di Nmap con altri strumenti di sicurezza.



#### III. Generazione di un rapporto HTML da una scansione Nmap



Il formato XML offre molte possibilità, non ultima quella di servire come base per la generazione di un report in formato HTML, che sarà più piacevole da consultare.



Per trasformare un file Nmap in formato XML in una pagina web, utilizzeremo lo strumento `xsltproc`, che dovremo prima installare:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Una volta installato questo strumento, è sufficiente fornirgli il file XML da convertire e il nome del report HTML da generare:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Di conseguenza, avremo la nostra intera scansione ben strutturata, con persino alcuni colori e link cliccabili nell'indice!



![nmap-image](assets/fr/53.webp)



estratto da un rapporto di scansione Nmap in formato HTML generato da xsltproc._



In generale, il file XML salvato da Nmap contiene un riferimento a un altro file in formato XSL:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



La conversione in HTML è quindi una funzione fornita e facilitata da Nmap, essendo `xsltproc` uno strumento comune e riconosciuto per eseguire questo compito (che non fa parte della suite di strumenti di Nmap).



XSLT (_Extensible Stylesheet Language Transformations_) è un sottoinsieme di XSL che consente di visualizzare i dati XML su una pagina web e di "trasformarli", parallelamente agli stili XSL, in informazioni leggibili e formattate in formato HTML.



fonte: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Il livello di informazione del report è equivalente a quello del formato XML di Nmap e superiore a quello dell'output standard del terminale (_interactive output_).



### IV. Gestione del livello di verbosità di Nmap



Vediamo ora alcune opzioni per Debugger Nmap o per seguirne i progressi.



La prima opzione da menzionare è l'opzione `-v`, che aumenta la verbosità di Nmap. Ecco un esempio:



![nmap-image](assets/fr/54.webp)



l'output verboso di nmap utilizzando l'opzione `-v`._



In una scansione che ha come obiettivo molti host e porte, l'output del terminale diventerà difficile da sfruttare a causa della quantità di informazioni visualizzate. Per questo motivo, questa opzione dovrebbe essere usata in combinazione con le opzioni viste in precedenza, che consentono di memorizzare l'output standard di Nmap in un file. Le informazioni relative all'uso della verbosità non saranno incluse in questo file di output. Come si può vedere dall'esempio precedente, questa verbosità consente di seguire le azioni e le scoperte di Nmap in modo chiaro e diretto. Per le scansioni più lunghe, in cui la visualizzazione dei dati può essere lenta, questo evita di non vedere l'attività corrente di Nmap e di sapere che le cose stanno procedendo e a quale ritmo. Per aumentare la verbosità di un ulteriore livello, è possibile utilizzare l'opzione `-vv`.



Per seguire ulteriormente l'attività di Nmap durante la scansione, è possibile utilizzare l'opzione `-packet-trace'. Con l'opzione `-v`, si ottiene un log in tempo reale di tutte le porte aperte scoperte da Nmap, mentre con questa opzione si ottiene una riga di log per ogni pacchetto inviato a una porta. Questo produce naturalmente un output molto prolisso, ma consente un monitoraggio dettagliato dell'attività di Nmap; ecco un esempio:



![nmap-image](assets/fr/55.webp)



monitoraggio dettagliato dell'attività di Nmap tramite `-packet-trace`



Anche in questo caso, queste informazioni non verranno registrate nel file di output prodotto da Nmap se vengono utilizzate le opzioni `-oN`, `-oG`, `-oX` o `-oA`.



Infine, Nmap offre anche due opzioni di debug: `-d` e `-dd`. Queste opzioni si comportano in modo simile all'opzione di verbosità `-v`, ma aggiungono ulteriori informazioni tecniche, come un riepilogo dei parametri tecnici all'inizio della scansione:



![nmap-image](assets/fr/56.webp)



le opzioni di temporizzazione sono visualizzate nella vista di debug di Nmap



Nelle prossime sezioni vedremo quali sono le opzioni di "Temporizzazione" e perché è utile conoscerle.



Infine, se si vuole avere solo una panoramica di base e sintetica dell'andamento della scansione di Nmap, si può usare l'opzione `--stats-every 5s`. Il termine "5s" indica 5 secondi e può essere modificato in base alle proprie esigenze. Questa è la frequenza con cui riceveremo un feedback da Nmap sui suoi progressi:



![nmap-image](assets/fr/57.webp)



informazioni visualizzate dall'opzione `--stats-every` di Nmap



In particolare, è possibile ottenere una percentuale di avanzamento, nonché un'indicazione della fase in cui si trova: fase di scoperta dell'host tramite [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), fase di scoperta delle porte TCP esposte, ecc. Queste informazioni possono essere ottenute anche nell'output del terminale premendo "Invio" durante una scansione.



Tuttavia, Nmap non è molto bravo a stimare il tempo necessario per un'operazione, anche perché non sa in anticipo quanti host e servizi dovrà analizzare.



### V. Conclusione



In questa sezione abbiamo esaminato una serie di opzioni per salvare i risultati della scansione Nmap in diversi formati di file. Ciò si rivelerà molto utile, poiché in contesti realistici i risultati delle scansioni possono occupare centinaia o addirittura migliaia di righe! Abbiamo anche visto come aumentare il livello di verbosità di Nmap per scopi di debug o per ottenere un rapporto sull'avanzamento della scansione.



Il formato XML sarà particolarmente utile nella prossima sezione, dove esamineremo alcuni strumenti che possono lavorare con i risultati di Nmap.




## 10 - Utilizzo di Nmap con altri strumenti di sicurezza



### I. Presentazione



In questa sezione, daremo un'occhiata ad alcuni degli usi classici di Nmap con altri strumenti di sicurezza gratuiti e open source. In particolare, utilizzeremo quanto appreso nelle sezioni precedenti per migliorare ulteriormente la potenza e l'efficienza di Nmap.



La possibilità di salvare i risultati delle scansioni Nmap in XML rende i dati compatibili con una serie di altri strumenti. Poiché oggi quasi tutti i linguaggi di programmazione e scripting dispongono di librerie in grado di analizzare l'XML, l'elaborazione di questi dati risulta molto più semplice. Diversi strumenti, in particolare quelli orientati alla sicurezza offensiva, dispongono di funzioni per l'elaborazione del formato XML generato da Nmap. Diamo un'occhiata più da vicino.



Citerò alcuni strumenti offensivi senza descriverne nel dettaglio l'uso e il funzionamento. Presumo che il lettore abbia familiarità con il loro uso di base e che siano già operativi. Questa sezione sarà di particolare interesse per i professionisti della [cybersecurity] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), per le persone in formazione o per coloro che hanno deciso di approfondire l'argomento.



### II. Importare i risultati di Nmap in Metasploit



Il primo strumento che esamineremo per riutilizzare i dati di Nmap nella ricerca offensiva di sicurezza e vulnerabilità è Metasploit.



Metasploit è un framework per exploit e attacchi. È una soluzione gratuita e uno strumento riconosciuto che contiene un gran numero di moduli scritti in Ruby o Python. Questi permettono di sfruttare le vulnerabilità, di eseguire attacchi, di generare backdoor, di gestire callback (funzioni C&C o di comunicazione e controllo) e di utilizzare tutto in modo uniforme.



In particolare, questo noto e diffuso framework operativo può lavorare con un [database] postgreSQL(https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) in cui sono memorizzati host, porte, servizi, informazioni di autenticazione e altro ancora.





- Documentazione ufficiale di Metasploit: [https://docs.metasploit.com/](https://docs.metasploit.com/)




È qui che entrano in gioco Nmap e il suo output, poiché il formato XML dell'output di Nmap può essere facilmente importato nel database di Metasploit per popolare il suo database di host e servizi, che possono quindi essere rapidamente designati come bersagli per questo o quell'attacco.



Una volta entrato nella mia shell interattiva di Metasploit, inizio a creare uno spazio di lavoro, una sorta di spazio specifico per il mio ambiente del giorno:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Una volta creato il mio spazio di lavoro, dobbiamo verificare che la comunicazione con il database sia operativa:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Infine, possiamo usare il comando `db_import` di Metasploit per importare la nostra scansione Nmap in formato XML:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Ecco il risultato dell'esecuzione di tutti questi comandi:



![nmap-image](assets/fr/58.webp)



importare una scansione Nmap in formato XML nel database di Metasploit



Qui si può vedere che ogni host è importato, insieme ai suoi servizi. Questi dati possono essere visualizzati tramite il comando `services` o `services -p <port>` per un servizio specifico:



![nmap-image](assets/fr/59.webp)



elenco dei servizi importati dal file XML nel database di Metasploit



Infine, possiamo riutilizzare rapidamente e facilmente questi dati in un modulo grazie all'opzione `-R`, che "convertirà" l'elenco dei servizi ottenuti come input per la direttiva `RHOSTS`, utilizzata per specificare gli obiettivi dell'attacco da effettuare. Ecco un esempio con il modulo `ssh_login`, che permette di effettuare un attacco brute force ai servizi [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



utilizzare l'opzione `services -R` per importare i servizi specificati come obiettivo dell'attacco



Questo è solo un piccolo esempio di ciò che si può fare con i dati di Nmap in Metasploit, ma dà una piccola idea di quanto velocemente e facilmente queste informazioni possano essere riutilizzate come parte di un test di penetrazione, di una scansione di vulnerabilità o di un attacco informatico. Vale anche la pena ricordare che Nmap può essere eseguito direttamente da Metasploit per importare i risultati nel database (comando `db_nmap`), un altro argomento interessante da trattare!



### III. Utilizzo di Nmap con lo scanner web Aquatone



Il secondo strumento che vorrei presentare in questa sezione sul riutilizzo dei risultati di Nmap per l'analisi offensiva della sicurezza e delle vulnerabilità è Aquatone.



Aquatone è uno scanner web progettato per esplorare in modo efficiente le applicazioni web su una rete. Offre funzioni avanzate per la scoperta di servizi web, l'identificazione di sottodomini, l'analisi delle porte e il fingerprinting delle applicazioni web. Il tutto presentato in modo chiaro e conciso in rapporti HTML, JSON e di testo per una facile analisi della sicurezza web.



Come Metasploit, Aquatone può elaborare direttamente il formato XML di Nmap e utilizzarlo come obiettivo per la scansione. In particolare, può estrarre solo gli host e i servizi di interesse (servizi web) da tutti i dati che un rapporto Nmap può contenere.





- Link allo strumento: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Per utilizzare l'output XML di Nmap con Aquatone, è sufficiente inviare il file XML in una pipe che verrà consumata da Aquatone. Ecco un esempio:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Se normalmente Aquatone esegue il port discovery sugli host per trovare i servizi web, in questo contesto si affiderà esclusivamente ai risultati di Nmap, che ha già eseguito questa operazione, risparmiando così tempo:



![nmap-image](assets/fr/61.webp)



utilizzando i risultati di Nmap in formato XML con `aquatone`._



Per vostra informazione, ecco un estratto del rapporto prodotto da Aquatone:



![nmap-image](assets/fr/62.webp)



esempio di un rapporto `aquatone



Personalmente, utilizzo spesso Aquatone per avere una rapida panoramica dei tipi di siti web presenti sulla rete, grazie soprattutto alla sua funzionalità di screenshot.



Anche in questo caso, avere un rapporto Nmap completo in formato XML consente di risparmiare tempo e di riutilizzarlo facilmente in un altro strumento.



### IV. Conclusione



Questi due esempi mostrano chiaramente che il formato XML di Nmap facilita l'utilizzo dei risultati da parte di altri strumenti, in quanto si tratta di un formato di dati strutturato e facile da usare. Esistono molti altri strumenti in grado di elaborare questi risultati, come strumenti di reporting automatico, rappresentazioni grafiche o scanner di vulnerabilità proprietari più complessi.



Naturalmente, potete anche sviluppare i vostri script e strumenti in Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) o qualsiasi altro linguaggio con una libreria di parsing XML per manipolare e riutilizzare i dati dei risultati di Nmap come meglio credete.



Questa sezione ci porta alla fine del modulo di esercitazione sull'uso più avanzato di Nmap, in particolare per la scansione delle vulnerabilità attraverso gli script NSE.



La prossima sezione dell'esercitazione si concentrerà, tra l'altro, su alcune ulteriori best practice più tecniche e su suggerimenti sulle scansioni specifiche che Nmap può eseguire. Verranno inoltre illustrate le opzioni di ottimizzazione delle prestazioni delle scansioni, particolarmente utili quando si eseguono scansioni di reti di grandi dimensioni.




## 11 - Migliorare le prestazioni della scansione di rete



### I. Presentazione



In questo capitolo impareremo a ottimizzare la velocità delle scansioni di rete eseguite con Nmap utilizzando varie opzioni specifiche. In particolare, impareremo a conoscere il funzionamento interno di Nmap, dalla gestione del _timeout_ alle configurazioni pre-salvate dello strumento.



Dopo aver dato un'occhiata alle caratteristiche di Nmap, vediamo di capire meglio la sua potenza. Se avete mai usato questo strumento su reti di grandi dimensioni, avrete probabilmente notato che alcune scansioni possono richiedere molto tempo, nonostante la potenza dello strumento. E per una buona ragione: un semplice comando `nmap`, con poche opzioni, può far passare milioni di pacchetti che mirano a centinaia di migliaia di potenziali sistemi e servizi.



Inoltre, alcune configurazioni delle apparecchiature di rete possono imporre intenzionalmente una velocità inferiore (numero di pacchetti al secondo), con il rischio di rifiutare i pacchetti o di vietare l'IP Address per motivi di sicurezza.



A seconda del contesto, può essere utile cercare di ottimizzare tutto questo, come vedremo in questo capitolo.



In ogni caso, è possibile controllare i valori predefiniti dei parametri che stiamo per esaminare, nonché se le opzioni che si intende utilizzare sono state prese in considerazione correttamente, tramite il debug di Nmap (opzione `-d` vista in un capitolo precedente):



![nmap-image](assets/fr/63.webp)



visualizzare le opzioni di temporizzazione tramite l'opzione `-d` di Nmap



### II. Gestione della velocità delle scansioni Nmap



#### A. Gestione della parallelizzazione



Per impostazione predefinita, Nmap utilizza la parallelizzazione nelle sue scansioni per ottimizzarle e tutti i parametri che utilizza possono essere modificati tramite varie opzioni. Tuttavia, i casi in cui è effettivamente necessario modificare questi parametri sono piuttosto rari, quindi non li esamineremo in dettaglio in questa guida:





- `--min-hostgroup/max-hostgroup <size>`: dimensione dei gruppi di scansione degli host paralleli.





- `--min-parallelismo/max-parallelismo <numprobes>`: parallelizzazione delle sonde.





- `--scan-delay/--max-scan-delay <time>`: regola il ritardo tra le sonde.




Sappiate che esistono e che possono essere utilizzati.



#### B. Gestione del numero di pacchetti al secondo



Per impostazione predefinita, Nmap regola il numero di pacchetti al secondo che invia in base alla risposta della rete. Tuttavia, è possibile forzare questa impostazione definendo il valore massimo e/o minimo da seguire in termini di numero di pacchetti al secondo. Questa impostazione viene effettuata utilizzando le opzioni `--min-rate <numero>` e `--max-rate <numero>` dove `numero` rappresenta un numero di pacchetti al secondo. Esempio:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Queste opzioni consentono di regolare la velocità delle scansioni in base alle proprie esigenze specifiche, sia per accelerare il processo che per limitare la larghezza di banda utilizzata. Quest'ultimo caso (limitare la velocità delle scansioni) è quello che più probabilmente vi condurrà a queste opzioni, soprattutto se si verifica una latenza di rete quando si usa Nmap (cosa piuttosto rara).



### III. Gestione delle interruzioni di connessione e dei timeout



Un altro parametro con cui possiamo giocare per ottimizzare la velocità delle scansioni di Nmap (o garantire una maggiore precisione) riguarda _timeout_ e _retry_.



Per _timeout_, si tratta del **timeout di mancata risposta** dopo il quale Nmap smetterà di attendere una risposta e considererà il servizio o l'host non raggiungibile. Per _retry_, questo è il **numero di tentativi successivi di un'operazione** che Nmap eseguirà prima di passare oltre.



Come per la parallelizzazione, la gestione del _timeout_ e del _retry_ può essere applicata alle fasi di scoperta dell'host o del servizio:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: specifica il tempo di andata e ritorno di un Exchange. Anche questo parametro viene calcolato e adattato al volo durante la scansione. Anche in questo caso, questo parametro viene calcolato e adattato al volo durante la scansione. È improbabile che sia necessario usarlo, poiché Nmap calcola questo tempo al volo in base alla reazione della rete.





- `--max-retries <number>`: limita il numero di ritrasmissioni di un pacchetto durante la scansione della porta. Per impostazione predefinita, Nmap può arrivare a 10 ritentativi per un singolo servizio, soprattutto se trova latenze o perdite a livello di rete, ma nella maggior parte dei casi ne viene eseguito solo uno.





- `--host-timeout <time>`: specifica il tempo massimo che Nmap trascorrerà su un host per tutte le sue operazioni, compresa la scansione delle porte, il rilevamento dei servizi e qualsiasi altra operazione relativa a quell'host. Se questo intervallo di tempo viene superato senza alcuna risposta o **completamento delle operazioni**, Nmap abbandonerà l'host senza visualizzare alcun risultato e passerà al successivo nell'elenco. Ciò consente di controllare il tempo massimo che Nmap trascorre su un determinato host, evitando di rimanere bloccati su host recalcitranti e ottimizzando il tempo complessivo di scansione.




Nel mio lavoro quotidiano, utilizzo le opzioni `--max-retries` e `--host-timeout` per ottimizzare le mie scansioni:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Questi parametri offrono una maggiore flessibilità per adattare il comportamento della scansione alle esigenze specifiche e alle condizioni della rete. Tuttavia, è necessario essere consapevoli delle loro implicazioni in termini di carico sugli host scansionati e di potenziale perdita di precisione.



### IV. Uso delle configurazioni preparate



Le varie opzioni che abbiamo visto in questo capitolo possono essere utilizzate singolarmente o come parte delle configurazioni già pronte offerte da Nmap. L'opzione che permette di utilizzare questi _templates_ (modelli di configurazione) è `-T <numero>` o `-T <nome>`. Ci sono 5 livelli di _templates_ utilizzabili:



```
-T<0-5>: Set timing template (higher is faster)
```



Per impostazione predefinita, Nmap utilizza _template_ 3 (_normale_), che in genere è sufficiente.



Da parte mia, in genere opero in contesti in cui devo essere abbastanza veloce (pur rimanendo il più completo possibile) e uso spesso l'opzione `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Ecco cosa mostrano le informazioni di debug di questa scansione:



![nmap-image](assets/fr/64.webp)



uso dell'impostazione `-T4` durante una scansione Nmap



### V. Conclusione



In questo capitolo abbiamo esaminato varie tecniche e opzioni che possono essere utilizzate per gestire la potenza, l'aggressività e le prestazioni di Nmap. Queste opzioni sono particolarmente utili per la scansione di reti di grandi dimensioni e, più raramente, per scopi stealth.



Nel prossimo capitolo vedremo alcune best practice per l'utilizzo di Nmap e per garantirne la sicurezza.




## 12 - Sicurezza e riservatezza dei dati quando si utilizza Nmap



### I. Presentazione



In questo capitolo esamineremo una serie di buone pratiche da adottare per quanto riguarda la sicurezza e, soprattutto, la riservatezza dei dati prodotti, elaborati e archiviati da Nmap.



L'uso di Nmap all'interno di un sistema informatico può essere rapidamente classificato come un'azione offensiva. Di conseguenza, è necessario prendere una serie di precauzioni per agire all'interno di un quadro legale, garantendo al contempo la sicurezza degli obiettivi previsti, dei dati raccolti e del sistema utilizzato per la scansione.



### II. Ottenere le autorizzazioni necessarie



Prima di eseguire la scansione di una rete o di un sistema, accertarsi di aver ottenuto le autorizzazioni appropriate. La scansione dei sistemi alla ricerca di vulnerabilità (`NSE scripts`) senza autorizzazione può essere illegale e può avere conseguenze legali, soprattutto se la sicurezza dei sistemi informativi non rientra nei vostri compiti ufficiali.





- Come promemoria: [Codice penale: Capo III: Attacchi a sistemi automatizzati di elaborazione dati](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Protezione dei dati sensibili



I risultati prodotti da Nmap possono essere considerati sensibili, in particolare quando contengono informazioni sulle debolezze del sistema informativo che potrebbero essere sfruttate da un aggressore. Ma anche quando riguardano sistemi non accessibili a tutti (ad esempio, sistemi informativi sensibili, industriali, sanitari o di backup (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Abbiamo anche visto che, a seconda degli script NSE utilizzati, i risultati della scansione NSE di [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) possono contenere anche identificatori.



In questo modo, un malintenzionato che riesca ad accedere ai risultati di queste scansioni avrà a disposizione una mappa del sistema informatico e un'infinità di informazioni tecniche, senza aver eseguito personalmente queste azioni, con il rischio di essere individuato.



È quindi importante fare attenzione a non raccogliere o memorizzare in modo inappropriato informazioni sensibili quando si utilizza Nmap, tra cui, ma non solo, le seguenti:





- Crittografia dei dati di output: se è necessario memorizzare o trasmettere i risultati delle scansioni di Nmap, assicurarsi di crittografarli per proteggere la riservatezza dei dati. In questo modo si impedisce l'intercettazione non autorizzata di informazioni sensibili. Idealmente, i dati dovrebbero essere crittografati non appena lasciano il sistema utilizzato per eseguire la scansione (un archivio ZIP crittografato con una password forte è un ottimo inizio).





- Impostare i controlli di accesso: assicurarsi che solo le persone autorizzate abbiano accesso ai risultati delle scansioni Nmap, dove saranno archiviati. Impostate controlli di accesso appropriati per proteggere le informazioni sensibili da accessi non autorizzati.





- Vigilanza nella gestione dei dati: durante il transito, la copia o l'elaborazione dei dati di scansione, assicurarsi di tenere sotto stretto controllo la sicurezza dei dati. Ciò significa: non lasciarli in giro nella directory `Download` di una postazione di lavoro connessa a Internet, non farli transitare attraverso l'applicazione interna HTTP file Exchange, non lasciare il Blocco note aperto senza bloccare la postazione di lavoro durante la pausa pranzo, ecc.




### IV. Gestione delle scansioni aggressive



Come abbiamo visto in questo tutorial, Nmap può essere molto prolisso a livello di rete. Può anche inviare pacchetti non correttamente formattati e che non rispettano rigorosamente la struttura del protocollo nei frame e nei pacchetti di rete che genera. Tutte queste azioni possono avere un impatto su alcuni sistemi e servizi, a volte fino a causare malfunzionamenti o saturazione delle risorse di sistema e di rete.



Per evitare incidenti, è necessario padroneggiare il comportamento di Nmap e sapere come adattarlo al contesto in cui viene utilizzato, mediante le varie opzioni discusse in questa esercitazione. Non necessariamente utilizzeremo Nmap allo stesso modo in un sistema informatico contenente [hardware] industriale (https://www.it-connect.fr/actualites/actu-materiel/) e in una rete utente composta da sistemi Windows protetti da un firewall locale o in un nucleo di rete.



Si spera che le varie lezioni di questo tutorial vi abbiano insegnato a padroneggiare e analizzare il comportamento di Nmap, ma il modo migliore per imparare è fare. Assicuratevi quindi di conoscere bene le opzioni di Nmap che utilizzerete.



### V. Protezione del sistema di scansione



Nel primo capitolo abbiamo visto che nella maggior parte dei casi Nmap deve essere eseguito come `root` o amministratore locale. Questo perché esegue operazioni di rete, a volte a un livello piuttosto basso, attraverso librerie di rete, che richiedono autorizzazioni elevate e rischiose dal punto di vista della stabilità del sistema o della riservatezza di altre applicazioni.



Di conseguenza, Nmap può essere considerato un componente sensibile del sistema su cui è installato. Assicuratevi di utilizzare la versione più recente di Nmap, poiché le versioni precedenti possono contenere vulnerabilità di sicurezza note. Utilizzando una versione aggiornata, è possibile ridurre al minimo i rischi associati all'uso dello strumento.



Se si è scelto di utilizzare Nmap non attraverso una sessione come `root`, ma concedendo privilegi specifici a un utente privilegiato in modo che abbia tutto ciò che serve per utilizzare Nmap (`sudo` o _capabilities_), si tenga presente che Nmap può essere utilizzato come parte di un'elevazione completa dei privilegi:



![nmap-image](assets/fr/65.webp)



elevazione dei privilegi di Nmap tramite `sudo`



In questo caso, sto usando il comando Nmap attraverso `sudo`, ma questo mi permette di ottenere una shell interattiva come `root` sul sistema, che non era l'obiettivo originale.



È inoltre altamente sconsigliato installare Nmap su sistemi non progettati per eseguire scansioni di rete. Mi riferisco in particolare ai server o alle workstation. Da un lato, questo aggiungerebbe un potenziale vettore per l'elevazione dei privilegi, ma soprattutto darebbe all'attaccante un accesso senza sforzo a uno strumento offensivo.



Infine, la sicurezza del sistema utilizzato per la scansione deve essere garantita in modo più ampio, affinché non diventi esso stesso un vettore di intrusione o di fuga di informazioni. Come amministratore di sistema, è meglio utilizzare un sistema dedicato, idealmente con una durata di vita limitata, piuttosto che la propria workstation.



### VI. Conclusione



In conclusione, assicuratevi di aver acquisito la giusta padronanza di Nmap prima di utilizzarlo in condizioni reali o di produzione, e siate vigili quando elaborate e gestite i suoi risultati. Sarebbe un peccato causare danni, fughe di dati o facilitare una compromissione, quando l'approccio iniziale è volto a migliorare la sicurezza dell'azienda.



## 13 - Scansione delle porte via TCP: SYN, Connect e FIN



### I. Presentazione



In questo capitolo e nel prossimo, esamineremo più da vicino i diversi tipi di scansione TCP disponibili in Nmap, a partire da quelli più comunemente utilizzati: Scansioni SYN, Connect e FIN.



Come avrete notato, Nmap offre diverse opzioni per le scansioni TCP:



![nmap-image](assets/fr/66.webp)



tecniche di scansione disponibili in Nmap



L'idea è quella di spiegare alcuni di questi metodi, per aiutarvi a capire le loro differenze, i loro vantaggi e i loro limiti. Vedrete che, a seconda del contesto o di ciò che volete sapere, è meglio optare per un'opzione o per un'altra.



### II. Scansione TCP SYN o "Half Open scan



Il primo tipo di scansione TCP che esamineremo è la `scansione TCP SYN`, nota anche come `scansione mezza aperta`. Se ricordate le scansioni di rete che abbiamo fatto dopo le prime scansioni delle porte, questo è il tipo di scansione usato di default da [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) quando viene eseguito con i diritti di root.



La traduzione vi aiuterà a capire come funziona questa scansione. In effetti, una scansione TCP SYN invierà un pacchetto TCP SYN a ciascuna porta mirata, che è il primo pacchetto inviato da un client (quello che richiede di stabilire una connessione) come parte del famoso _Three way handshake_ TCP. Normalmente, se la porta è aperta sul server di destinazione, con un servizio in esecuzione dietro di essa, il server invia un pacchetto TCP SYN/ACK per convalidare il SYN del client e inizializzare la connessione TCP. Questa risposta assume la forma di un pacchetto TCP con i flag SYN e ACK impostati a 1, che ci permette di confermare che la porta è aperta e conduce a un servizio.



D'altra parte, se la porta è chiusa, il server invierà un pacchetto `TCP` con i flag RST e ACK impostati a 1 per terminare la richiesta di connessione, così sapremo che nessun servizio sembra essere attivo dietro questa porta:



![nmap-image](assets/fr/67.webp)



diagramma di comportamento della scansione SYN di tCP per porte aperte e chiuse



Per avere una visione più concreta del `TCP SYN Scan`, ho eseguito una scansione della porta TCP/80 verso un host che aveva un server web attivo su questa porta. Eseguendo una scansione di rete con Wireshark, si può vedere il seguente flusso (origine della scansione: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



acquisizione della rete durante una scansione TCP SYN per una porta aperta



Nella prima riga si vede che la sorgente della scansione sta inviando un pacchetto TCP all'host `10.10.10.203` sulla porta TCP/80. In questo pacchetto TCP, il flag SYN è impostato su 1 per indicare che si tratta di una richiesta di inizializzazione della connessione TCP.



Poi, sulla seconda riga, vediamo che il target risponde con un `TCP SYN/ACK`, il che significa che accetta di inizializzare una connessione e quindi di ricevere flussi sulla porta TCP/80. Possiamo quindi dedurre che la porta TCP/80 è aperta e che sul server scansionato è presente un server web.



Il nostro host invia quindi un pacchetto RST per chiudere la connessione, consentendo all'host sottoposto a scansione di non mantenere una connessione TCP aperta in attesa di una risposta. Nel caso di una scansione su molte porte, la mancata chiusura delle connessioni TCP potrebbe portare a un denial of service, saturando il numero di connessioni in attesa di risposta che il server può mantenere (vedere [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



In Wireshark è possibile vedere lo stato dei flag TCP per ogni test eseguito. Questo mostra se il pacchetto è un pacchetto SYN, SYN/ACK, ACK, ecc:



![nmap-image](assets/fr/69.webp)



visualizzare i flag TCP di un pacchetto in Wireshark (TCP SYN qui)



Al contrario, ho eseguito lo stesso test tra le due macchine, ma questa volta eseguendo la scansione di una porta TCP/81 su cui non è attivo alcun servizio (origine della scansione: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



acquisizione della rete durante una scansione TCP SYN per una porta chiusa



L'host scansionato restituisce un `TCP RST/ACK` in risposta al mio `TCP SYN` quando la porta non è aperta.



Come già detto, quando si esegue Nmap da un terminale privilegiato, la scansione TCP SYN è la modalità predefinita e può essere forzata tramite l'opzione `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




La scansione `TCP SYN' è quella più comunemente utilizzata per motivi di velocità. D'altra parte, la mancata finalizzazione del _Three Way Handshake_ da parte di un client (cioè il mancato invio dell'ACK dopo il SYN/ACK del server) può sembrare sospetta se osservata troppe volte su un server o dalla stessa fonte sulla rete. In effetti, il comportamento normale di un client dopo la ricezione di un pacchetto TCP SYN/ACK in risposta a un TCP SYN è quello di inviare un `riconoscimento` (ACK) e quindi avviare il Exchange.



Tuttavia, fornisce una scansione leggermente più veloce, poiché non si preoccupa di inviare un ACK per ogni risposta positiva. Il vantaggio di SYN Scan è la sua velocità, poiché viene inviato un solo pacchetto per ogni porta da scansionare, a scapito di una maggiore possibilità di rilevamento.



Inoltre, la scansione TCP SYN è in grado di rilevare se una porta è filtrata (protetta) da un firewall. Infatti, un firewall di fronte all'host di destinazione può essere individuato dal modo in cui si comporta quando riceve un pacchetto TCP SYN su una porta che dovrebbe proteggere. Semplicemente non risponde. Tuttavia, come abbiamo visto, in entrambi i casi (porta aperta o chiusa), l'host risponde. Questo terzo comportamento rivela la presenza di un firewall tra l'host scansionato e la macchina che esegue la scansione. Ecco il risultato che Nmap può restituire quando una porta scansionata è filtrata da un firewall:



![nmap-image](assets/fr/71.webp)



visualizzazione di nmap durante la scansione di una porta filtrata



Quando si esegue un'acquisizione di rete al momento della scansione, si può notare che non viene fornita alcuna risposta:



![nmap-image](assets/fr/72.webp)



acquisizione della rete durante una scansione TCP SYN per una porta filtrata da un firewall



La differenza tra una porta chiusa e una porta filtrata è la seguente: una porta filtrata è una porta protetta da un firewall, mentre una porta chiusa è una porta su cui non è in esecuzione alcun servizio e che quindi non è in grado di elaborare i nostri pacchetti TCP. Alcuni tipi di scansione TCP, come la scansione TCP SYN, sono in grado di rilevare se una porta è filtrata, mentre altri tipi di scansione non lo sono.



### III. Scansione TCP Connect o scansione Full Open



Il secondo tipo di scansione TCP è la scansione `TCP Connect`, nota anche come _Full Open Scan_. Funziona allo stesso modo della scansione TCP SYN, ma questa volta restituisce un `TCP ACK` dopo una risposta positiva dal server (un SYN/ACK). Per questo motivo si chiama `Full Open', in quanto la connessione viene completamente aperta e avviata su ogni porta aperta durante la scansione, rispettando così il TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



diagramma di comportamento di tCP Connect Scan per le porte aperte e chiuse



Ecco cosa si vede transitare sulla rete durante una scansione `TCP Connect` mirata a una porta aperta:



![nmap-image](assets/fr/74.webp)



sniffing di rete durante una scansione TCP Connect per una porta aperta



Possiamo vedere che il primo pacchetto TCP inviato è un `TCP SYN` inviato dal client, e il server risponderà con un `TCP SYN/ACK`, indicando che la porta è aperta e ospita un servizio attivo. Per simulare un client legittimo, Nmap invia un `TCP ACK` al server. Al contrario, quando si scansiona una porta chiusa:



![nmap-image](assets/fr/75.webp)



acquisizione di rete durante una scansione TCP Connect per una porta chiusa



Si noti che la risposta del server al nostro pacchetto `SYN` è ancora una volta un pacchetto `TCP RST/ACK`, quindi si può dedurre che la porta è chiusa e che nessun servizio è in esecuzione su di essa.



Quando si utilizza Nmap, l'opzione `-sT` (`scan Connect`) viene utilizzata per eseguire una scansione TCP Connect. Si noti che quando Nmap viene utilizzato da una sessione non privilegiata, questa è la modalità di scansione TCP predefinita:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



La scansione `TCP Connect` simula una richiesta di connessione più legittima, con un comportamento più simile a quello di un client lambda, quindi è più difficile individuare una scansione su un numero ridotto di porte. È tuttavia più lenta, poiché inizializza completamente ogni connessione TCP sulle porte aperte del computer sottoposto a scansione.



Una scansione Nmap di 10.000 porte sarà comunque facilmente rilevabile se sono installati servizi di rilevamento e protezione dalle intrusioni di rete (IDS, IPS, EDR). Quando un aggressore vuole mantenere un basso profilo, tenderà a concentrarsi su un piccolo numero di porte scelte strategicamente, come la 445 (SMB) o la 80 (HTTP), che sono spesso aperte sui server e presentano vulnerabilità comuni.



Poiché TCP Connect Scan si aspetta una risposta in entrambi i casi, può anche rilevare la presenza di un firewall che potrebbe filtrare le porte sull'host di destinazione.



### IV. Scansione TCP FIN o "Stealth Scan



La scansione `TCP FIN`, nota anche come _Stealth Scan_, utilizza il comportamento di un client che termina una connessione TCP per rilevare una porta aperta.



In TCP, per fine sessione si intende l'invio di un pacchetto TCP con il flag FIN impostato a 1. In un normale Exchange, il server cessa ogni comunicazione con il client (nessuna risposta). Se il server non ha una connessione TCP attiva con il client, invia un `RST/ACK`. È quindi possibile distinguere tra porte aperte e chiuse inviando pacchetti `TCP FIN` a un insieme di porte:



![nmap-image](assets/fr/76.webp)



diagramma di comportamento della scansione tCP FIN per porte aperte e chiuse



Ho nuovamente catturato la rete durante una scansione _Stealth_ e questo è ciò che si vede quando la porta scansionata è aperta:



![nmap-image](assets/fr/77.webp)



acquisizione della rete durante una scansione TCP FIN per una porta aperta



Possiamo vedere che il client invia uno o due pacchetti per terminare una connessione TCP e che il server non risponde. Accetta semplicemente la fine della connessione e smette di comunicare.



Ecco cosa si vede ora quando si scansiona una porta chiusa:



![nmap-image](assets/fr/78.webp)



acquisizione di rete durante una scansione TCP FIN per una porta chiusa



Vediamo che il server restituisce un pacchetto `TCP RST/ACK`, quindi c'è una differenza di comportamento tra una porta aperta e una chiusa, e siamo in grado di elencare le porte aperte su un server inviando un pacchetto TCP FIN. Con Nmap, l'opzione `-sF` (`scan FIN`) viene utilizzata per eseguire una scansione TCP FIN:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan non funziona sugli host Windows, perché il sistema operativo tende a ignorare i pacchetti TCP FIN quando vengono inviati a porte non aperte. Pertanto, se si esegue una scansione TCP FIN su un host Windows, si avrà l'impressione che tutte le porte siano chiuse.



Per questo motivo è importante conoscere i diversi metodi di scansione e capire la differenza tra di essi.



Poiché in entrambi i casi il TCP FIN non attende una risposta, non è in grado di rilevare la presenza di un firewall tra l'host di destinazione e l'origine della scansione.



Ecco un esempio del risultato della scansione TCP FIN di Nmap:



![nmap-image](assets/fr/79.webp)



risultati di una scansione TCP FIN da parte di Nmap



Infatti, una mancata risposta da parte dell'host su una determinata porta può significare che la porta è filtrata, ma anche che è aperta e attiva.



Questa scansione viene definita "stealth", in quanto non genera molto traffico e generalmente non provoca registrazioni nei sistemi interessati. Può essere utilizzata per scoprire in modo discreto le porte di una rete senza suscitare alcun allarme. Tuttavia, come già detto, la sua efficacia può variare a seconda del sistema di destinazione, così come la sua discrezionalità a seconda della configurazione delle apparecchiature di sicurezza.



### V. Conclusioni



Questo è il primo di due capitoli sui diversi tipi di scansione TCP offerti da Nmap! Nel prossimo capitolo esamineremo i tipi di scansione TCP XMAS, Null e ACK, che operano in modi diversi per rilevare le porte aperte su un host.





## 14 - Scansione delle porte via TCP: XMAS, Null e ACK



### I. Presentazione



In questa sezione continueremo a esplorare i vari metodi di scansione TCP offerti da Nmap. Verranno esaminati i metodi `XMAS`, `Null` e `ACK`, che utilizzano caratteristiche specifiche di TCP per recuperare informazioni sulle porte e sui servizi aperti su un determinato obiettivo.



### II. Scansione TCP XMAS



XMAS Scan TCP è un po' insolito, in quanto non simula affatto il normale comportamento di utenti o macchine su una rete. Infatti, XMAS Scan invia pacchetti TCP con i flag `URG` (Urgent), `PSH` (Push) e `FIN` (Finish) impostati su 1, al fine di aggirare alcuni firewall o meccanismi di filtraggio.



Il nome XMAS deriva dal fatto che vedere questi flag attivi è insolito. Quando tutti e tre i flag sono impostati simultaneamente in un pacchetto TCP, l'aspetto è quello di un albero di Natale illuminato:



![nmap-image](assets/fr/80.webp)



flag tCP utilizzati nella scansione XMAS



Senza entrare nel dettaglio del ruolo di questi flag, è importante sapere che quando si invia un pacchetto con questi tre flag abilitati, un servizio attivo dietro la porta di destinazione non restituirà alcun pacchetto. Se invece la porta è chiusa, riceveremo un pacchetto TCP RST/ACK. Ora saremo in grado di distinguere tra il comportamento di una porta aperta e di una chiusa quando elenchiamo le porte di una macchina:



![nmap-image](assets/fr/81.webp)



diagramma di comportamento di tCP XMAS Scan per porte aperte e chiuse



Sempre seguendo la stessa logica, una scansione di rete sulla porta TCP/80 di un host con un server Web attivo mostra il seguente comportamento quando rileva una porta aperta (origine della scansione `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



acquisizione della rete durante una scansione TCP XMAS per una porta aperta



Si può notare che l'origine della scansione invia due pacchetti TCP XMAS (con i flag `FIN`, `PSH` e `URG` impostati a 1) all'host `10.10.10.203` e che non c'è alcun ritorno dalla destinazione, a indicare che la porta è aperta. Al contrario, quando si esegue una `scansione TCP XMAS' su una porta chiusa, si osserva il seguente risultato:



![nmap-image](assets/fr/83.webp)



cattura della rete durante una scansione TCP XMAS per una porta chiusa



La risposta al nostro pacchetto TCP è quindi un `TCP RST/ACK`, che indica che la porta è chiusa. Per utilizzare questa tecnica con Nmap, l'opzione `-sX` (`scan XMAS`) consente di eseguire una scansione TCP XMAS:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



È importante notare che la scansione TCP XMAS non è in grado di rilevare i firewall che possono trovarsi tra il computer di destinazione e quello di scansione, a differenza di altri tipi di scansione come TCP SYN o Connect. Infatti, un firewall attivo tra i due host garantirà che non venga effettuato alcun ritorno TCP se la porta di destinazione è filtrata (cioè protetta dal firewall). In caso di mancata risposta, è quindi impossibile sapere se la porta è protetta dal firewall o se è aperta e attiva. Occorre inoltre tenere presente che, come la scansione TCP FIN, alcune applicazioni o sistemi operativi come Windows possono falsare i risultati di questo tipo di scansione.



nota: il supporto per le scansioni XMAS/FIN/NULL sulle versioni recenti di Windows rimane limitato e i risultati potrebbero essere incoerenti su questo tipo di target. (Aggiornamento 2025)_



### III. Scansione TCP nulla



A differenza della scansione TCP XMAS, la scansione TCP Null invia pacchetti di scansione TCP con tutti i flag impostati su 0. Anche questo è un comportamento che non si riscontrerà mai in un normale Exchange tra macchine, poiché l'invio di un pacchetto TCP senza flag non è specificato nell'RFC che descrive il protocollo TCP. Per questo motivo può essere individuato più facilmente.



Come la scansione TCP XMAS, questa scansione può interferire con alcuni firewall o moduli di filtraggio, consentendo il passaggio dei pacchetti:



![nmap-image](assets/fr/84.webp)



diagramma di comportamento di tCP Null Scan per porte aperte e chiuse



Ecco cosa si vede sulla rete durante una scansione TCP Null su una porta aperta:



![nmap-image](assets/fr/85.webp)



acquisizione della rete durante una scansione TCP Null per una porta aperta



La macchina di scansione invia un pacchetto senza flag (`[<None>]` in Wireshark) senza alcuna risposta dal server. Al contrario, quando la porta di destinazione è chiusa:



![nmap-image](assets/fr/86.webp)



acquisizione di rete durante una scansione TCP Null per una porta chiusa



Per eseguire una scansione TCP Null con Nmap, è sufficiente utilizzare l'opzione `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Poiché la risposta quando una porta è aperta e quando un firewall è attivo (nessun feedback del server in entrambi i casi) è identica, TCP Null scan non è in grado di rilevare la presenza di un firewall. Inoltre, il firewall può addirittura falsare il risultato suggerendo che una porta è aperta, poiché non risponde ai pacchetti TCP senza flag, anche se la porta è filtrata. Si tratta di un'informazione importante da tenere presente quando si utilizzano scansioni che non sono in grado di distinguere tra una porta aperta e una filtrata (protetta da firewall), come le scansioni `TCP Null`, `XMAS` o `FIN`, al fine di rimanere coerenti nell'interpretazione dei risultati ottenuti.



### IV. Scansione TCP ACK



La scansione TCP ACK viene utilizzata per rilevare la presenza di un firewall sull'host di destinazione o tra la destinazione e l'origine della scansione.



A differenza di altre scansioni, la scansione TCP ACK non cerca di identificare quali porte sono aperte sull'host, ma piuttosto se è attivo un sistema di filtraggio, rispondendo per ogni porta con `filtered` o `unfiltered`. Alcune scansioni TCP, come `TCP SYN` o `TCP Connect`, possono fare entrambe le cose contemporaneamente, mentre altre, come `TCP FIN` o `TCP XMAS`, non sono in grado di determinare la presenza di un filtraggio. Per questo motivo può essere utile la scansione TCP ACK:



![nmap-image](assets/fr/87.webp)



diagramma di comportamento della scansione ACK tCP per porte filtrate e non filtrate



Per eseguire questo tipo di scansione utilizzeremo l'opzione `-sA` di Nmap. Ecco il risultato di una scansione TCP ACK se la porta è filtrata, cioè bloccata e protetta da un firewall:



![nmap-image](assets/fr/88.webp)



visualizzazione di nmap durante la scansione TCP ACK



Esempio di risultato per un host con firewall e uno senza. Nmap restituisce `filtro` sulle porte TCP/80 e TCP/81 dell'host `10.10.10.203`. In un'analisi di rete tramite Wireshark, il comportamento è il seguente:



![nmap-image](assets/fr/89.webp)



acquisizione di rete durante una scansione TCP ACK per una porta non filtrata da un firewall



Il computer di destinazione non restituisce nulla se è presente un firewall.



Per lanciare questa scansione con Nmap, utilizzare l'opzione `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Conclusioni



Abbiamo esaminato tre diversi metodi di scansione via TCP, oltre a quelli già presentati. Questi diversi metodi devono essere utilizzati in condizioni e contesti molto specifici, in particolare nell'ambito di test di penetrazione o di operazioni di Red Team, durante le quali sono presenti nozioni di discrezione.



## 15 - CheatSheet di Nmap - Riepilogo dei comandi dell'esercitazione



### I. Presentazione



Ecco un breve riassunto dei numerosi comandi e casi d'uso di Nmap, in modo da poterli trovare e riutilizzare rapidamente nell'uso quotidiano.



### II. Nmap: CheatSheet IT-Connect



Ecco un cheatsheet dei comandi presentati. Questa pagina facilita la ricerca degli usi più comuni di Nmap.





- Scansione della porta




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Scoprire gli host attivi




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



nota: L'opzione `-sP` è obsoleta da diversi anni e dovrebbe essere sostituita da `-sn`. (Aggiornamento 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Rilevamento della versione




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- Script NSE: alla ricerca di vulnerabilità




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Gestione dell'output di Nmap




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Ottimizzazione delle prestazioni




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Tipi di scansione TCP




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Spero che questi comandi vi siano utili. Non dimenticate di adattare l'obiettivo delle scansioni al vostro contesto e di fare riferimento alla documentazione ufficiale per padroneggiare appieno i test eseguiti.



### III. Conclusione



L'esercitazione su Nmap è terminata. Ora avete le basi necessarie per utilizzare questo strumento completo e potente. Si consiglia vivamente di fare pratica su ambienti controllati (Hack The Box, VulnHub, macchine virtuali) prima di utilizzarlo in produzione.



Rimane ancora molto da esplorare sul funzionamento interno dello strumento e sulle sue funzioni avanzate. Tuttavia, la padronanza dei comandi e dei concetti qui presentati vi consentirà di utilizzare Nmap con sicurezza e pertinenza.
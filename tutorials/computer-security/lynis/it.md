---
name: Lynis
description: Eseguire un controllo di sicurezza di una macchina Linux con Lynis
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Fares CHELLOUG pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale



___



## I. Presentazione



**In questo tutorial impareremo ad eseguire un controllo di sicurezza su una macchina Linux utilizzando Lynis! Per coloro che non conoscono **Lynis,** è una piccola utility a riga di comando che analizza la configurazione del vostro server e fornisce raccomandazioni per **migliorare la sicurezza della vostra macchina.**



Lynis è uno strumento open source di CISOFY, un'azienda specializzata in **system auditing e hardening**. Se volete fare progressi nell'hardening di Linux e dei servizi più diffusi (SSH, Apache2, ecc.), Lynis è il vostro alleato! Lynis non solo vi dice cosa sta andando storto, ma fornisce anche raccomandazioni per indirizzarvi nella giusta direzione (e farvi risparmiare tempo).



**Lynis** funziona con la maggior parte delle distribuzioni Linux, tra cui: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis si rivolge agli utenti Linux / UNIX, ma è anche compatibile con **macOS**. L'installazione è molto rapida e non prevede la gestione delle dipendenze a livello di pacchetto.



Viene utilizzato per diversi scopi:





- Audit di sicurezza
- Test di conformità (PCI, HIPAA e SOX)
- Configurazioni di sistema più difficili
- Rilevamento delle vulnerabilità



Lo strumento è ampiamente utilizzato da una vasta gamma di utenti, tra cui amministratori di sistema, auditor IT e pentester. Per le analisi, lo strumento si basa su standard quali **CIS Benchmark, NIST, NSA, OpenSCAP** e sulle raccomandazioni ufficiali di **Debian, Gentoo, Red Hat**.



Il progetto è disponibile a questo Address su **Github**:





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Scarica Lynis da CISOFY](https://cisofy.com/lynis/#download)



In questa guida passo-passo, **utilizzerò un VPS con Debian 12** e mi concentrerò sulla parte SSH, in quanto vorrei verificare la sua configurazione e migliorarla.



## II. Download e installazione



Esistono diversi modi per scaricare e installare Lynis. Scegliete quello che preferite dall'elenco che segue.



### A. Installazione dai repository Debian



Questa modalità di installazione consente di utilizzare il comando **lynis** da qualsiasi punto del sistema, a differenza dell'installazione da sorgente, dove è necessario trovarsi nella directory.



Collegarsi al server tramite SSH e inserire i seguenti comandi per installare Lynis:



```
sudo apt-get update
sudo apt-get install lynis -y
```



Ecco cosa si ottiene:



![Image](assets/fr/024.webp)



### B. Scaricare dal sito web ufficiale



È anche possibile scaricarlo dal sito web di Cisofy:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Ecco cosa si ottiene:



![Image](assets/fr/032.webp)



Successivamente, scompattiamo l'archivio con il seguente comando:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Ecco cosa si ottiene:



![Image](assets/fr/020.webp)



Passiamo alla cartella **lynis**:



```
cd lynis
```



È possibile verificare la presenza di aggiornamenti con il seguente comando:



```
./lynis update info
```



Ecco cosa si ottiene:



![Image](assets/fr/023.webp)



### C. Scaricare da GitHub



Scaricheremo **Lynis** dal repository ufficiale di GitHub, usando il seguente comando (*git* deve essere presente sul vostro computer):



```
git clone https://github.com/CISOfy/lynis.git
```



Ecco cosa si ottiene:



![Image](assets/fr/060.webp)



## III. Utilizzo di Lynis



Lynis è presente sulla nostra macchina, quindi impariamo a usarlo!



### A. Controlli e opzioni principali



Per visualizzare i comandi disponibili, basta inserire il seguente comando:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



Ecco cosa si ottiene:



![Image](assets/fr/039.webp)



Inoltre, sono disponibili le seguenti opzioni:



![Image](assets/fr/040.webp)



Per visualizzare tutti i comandi disponibili, digitate il seguente comando:



```
sudo lynis show
```



Ecco cosa si ottiene:



![Image](assets/fr/022.webp)



Se si desidera visualizzare tutte le opzioni, è necessario immettere:



```
sudo lynis show options
```



Ecco cosa si ottiene:



![Image](assets/fr/021.webp)



Nel resto dell'articolo, impareremo a utilizzare alcune opzioni.



### B. Esecuzione dell'audit del sistema



Chiederemo a **Lynis** di verificare il nostro sistema, evidenziando ciò che è configurato correttamente e ciò che potrebbe essere migliorato. Per farlo, inserire il seguente comando:



```
sudo lynis audit system
# ou
./lynis audit system
```



Per impostazione predefinita, se non si è connessi come root quando si esegue questo comando, lo strumento verrà eseguito con i privilegi dell'utente attualmente connesso. Alcuni test non verranno eseguiti in questo contesto:



![Image](assets/fr/052.webp)



Ecco i test che non verranno eseguiti in questa modalità:



![Image](assets/fr/051.webp)



Una volta eseguito il comando, inizia l'analisi. È sufficiente attendere un attimo.



Alla fine della verifica, si ottiene questo (possiamo vedere che **Lynis** ha identificato correttamente il sistema **Debian 12** e userà il **Pintage Debian** per l'analisi):



![Image](assets/fr/017.webp)



Successivamente, Lynis elencherà una serie di punti corrispondenti a tutto ciò che ha controllato nel nostro sistema. Come vedremo, l'elenco è organizzato per categorie. Vale la pena notare che viene utilizzato un codice colore per evidenziare le raccomandazioni:





- Rosso** per Elements critico o best practice non rispettate (un pacchetto mancante, per esempio), cioè il vostro server non rispetta questo punto
- Giallo** per suggerimenti o parziale conformità alla raccomandazione (diciamo che è un vantaggio conformarsi a un punto evidenziato con questo colore (non prioritario))
- Green** per i punti in cui la configurazione del server è conforme
- Bianco**, se neutro



Qui possiamo vedere che Lynis raccomanda di installare **fail2ban**:



![Image](assets/fr/057.webp)



Nella sezione "**Boot e servizi**", vediamo che la protezione dei servizi tramite *systemd* potrebbe essere migliorata. Il lato positivo è che Grub2 è presente e non ci sono problemi di permessi su:



![Image](assets/fr/029.webp)



Poi ci sono le sezioni "**Kernel**" e "**Memoria e processi**":



![Image](assets/fr/037.webp)



Quindi, la sezione "**Utenti, gruppi e autenticazione**". Lo strumento ci informa di un avviso sui permessi della directory "**/etc/sudoers.d**". Per il momento non sappiamo altro, ma alla fine dell'analisi potremo vedere quali sono le raccomandazioni.



![Image](assets/fr/049.webp)



Ecco cosa si può trovare nelle sezioni "**Shells", "Files Systems" e "USB Devices "**. Tra le altre cose, possiamo vedere che ci sono suggerimenti sui punti di montaggio e che i dispositivi USB sono attualmente consentiti su questa macchina.



![Image](assets/fr/048.webp)



Poi, le sezioni: "Indica che i pacchetti non più in uso possono essere eliminati e che non esiste un'utilità in grado di gestire gli aggiornamenti automatici.



![Image](assets/fr/058.webp)



Possiamo vedere che il firewall è attivato (e sì, c'è iptables!). Inoltre, possiamo vedere che ha trovato regole inutilizzate e che è installato un server web Apache.



![Image](assets/fr/055.webp)



Segue un'analisi del server web stesso, dal momento che il servizio è stato identificato.



Possiamo vedere che ha trovato i file di configurazione di **Nginx** e che per la parte SSL/TLS, i **ciferi** sono configurati con l'uso di un protocollo che non sarebbe sicuro. D'altra parte, secondo Lynis, la gestione dei log è corretta.



![Image](assets/fr/038.webp)



Il servizio SSH è presente sul mio server VPS. La sua configurazione è analizzata da Lynis. Va detto che la sicurezza di SSH può essere facilmente migliorata! Torneremo su quest'area in dettaglio una volta ottenute le raccomandazioni.



![Image](assets/fr/026.webp)



Ecco le sezioni **"Supporto SNMP", "Database", "PHP", "Supporto Squid", "Servizi LDAP", "Registrazione e file "**.



C'è un suggerimento molto importante sulla gestione dei log: si raccomanda vivamente di non memorizzare i log solo localmente sulla macchina. Se la macchina fosse corrotta da un aggressore, è probabile che questi cerchi di cancellare le sue tracce... Quindi è necessario esternalizzare i log.



![Image](assets/fr/050.webp)



Qui, abbiamo la verifica dei servizi vulnerabili, la gestione degli account, le attività pianificate e la sincronizzazione NTP.È indicato che il livello è basso sul banner e sulla parte di identificazione: questo è comprensibile, se si visualizza la versione del sistema, si dà un'indicazione a un potenziale attaccante. Questa è l'impostazione predefinita.



Sarebbe interessante attivare **auditd** per avere i log in caso di analisi **forense**. Viene controllato anche il **NTP**, perché per cercare i log in modo efficiente, è preferibile avere i sistemi in orario, il che semplifica la ricerca.



![Image](assets/fr/036.webp)



Lynis esamina poi il Elements crittografico, la virtualizzazione, i container e i framework di sicurezza. Alcune sezioni sono vuote perché non c'è corrispondenza con la macchina analizzata. Tuttavia, possiamo vedere che ho due certificati SSL scaduti e non ho attivato **SELinux**.



![Image](assets/fr/027.webp)



Anche in questo caso ci sono margini di miglioramento: non c'è uno scanner antivirus o antimalware e ci sono suggerimenti sui permessi dei file.



![Image](assets/fr/028.webp)



Successivamente, Lynis si concentra sulla configurazione del kernel Linux (comprese le regole per lo stack IPv4) e sulla gestione delle directory "Home" della macchina Linux.



![Image](assets/fr/035.webp)



Siamo arrivati alla fine dell'analisi... Quest'ultimo punto dimostra che avremmo tutto da guadagnare dall'avere ClamAV su questa macchina.



![Image](assets/fr/030.webp)



## IV. Raccomandazioni



Dopo la verifica, è il momento di leggere e analizzare le raccomandazioni. Qui si trovano le raccomandazioni e le spiegazioni per ciascuno dei test effettuati da Lynis.



Prendiamo ad esempio le raccomandazioni per SSH. **Per ogni suggerimento, troverete il parametro consigliato e un link che spiegherà il punto di sicurezza ** Sta a voi decidere, a seconda del contesto e dell'utilizzo.



Vediamo alcuni esempi di raccomandazioni che riprendono direttamente i punti evidenziati nell'audit...



### A. Esempi di raccomandazioni





- Come abbiamo visto in precedenza, l'NTP è importante per la marcatura temporale dei registri:



![Image](assets/fr/043.webp)





- Lynis suggerisce anche di installare il pacchetto **apt-listbugs** per ottenere informazioni sui bug critici durante l'installazione dei pacchetti tramite **apt.**



![Image](assets/fr/041.webp)





- Lo strumento suggerisce di installare **needrestart per poter** vedere quali processi utilizzano una vecchia versione della libreria e devono essere riavviati.



![Image](assets/fr/054.webp)





- Questo suggerimento suggerisce di installare **fail2ban** per bloccare automaticamente gli host che non riescono ad autenticarsi (in particolare con la forza bruta).



![Image](assets/fr/044.webp)





- Per rendere più rigidi i servizi di sistema, l'autore consiglia di eseguire il comando blu per ogni servizio della macchina.



![Image](assets/fr/056.webp)





- Suggerisce di impostare date di scadenza per tutte le password degli account protetti.



![Image](assets/fr/031.webp)





- Questo suggerimento suggerisce di impostare valori minimi e massimi per l'età di una password. In questo modo si garantisce, tra l'altro, che le password vengano cambiate regolarmente.



![Image](assets/fr/042.webp)





- Si consiglia di utilizzare partizioni separate, per limitare l'impatto di problemi di spazio su disco in una partizione.



![Image](assets/fr/047.webp)





- Questa raccomandazione suggerisce di disabilitare l'archiviazione USB e firewire per evitare la perdita di dati



![Image](assets/fr/033.webp)





- Per soddisfare questa raccomandazione, è sufficiente installare e configurare **unnatended-upgrade**, ad esempio.



![Image](assets/fr/053.webp)



### B. Installazione dei pacchetti consigliati



Per migliorare la configurazione del sistema, installeremo alcuni pacchetti sulla macchina: alcuni raccomandati da Lynis, altri che consiglio personalmente.



Avrete una buona base su cui lavorare, purché dedichiate un po' di tempo alla loro configurazione. A tale scopo, consultate il sito IT-Connect, altri articoli sul Web e la documentazione dello strumento.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Alcune informazioni sui pacchetti installati:





- Clamav** è un antivirus.
- unattend-upgrades** vi consentirà di gestire automaticamente gli aggiornamenti e persino di riavviare la macchina o di eliminare automaticamente i vecchi pacchetti, è completamente configurabile.
- rkhunter** è un anti-rootkit che analizza il file system.
- Fail2ban** si baserà sui vostri file di log in base a ciò che gli darete da leggere e funzionerà con **iptables**, ad esempio per bandire gli indirizzi IP che cercano di "forzare" il vostro server in SSH.



### C. Raccomandazioni per SSH



Diamo un'occhiata alle raccomandazioni SSH. Sono elencate di seguito. Non preoccupatevi, vi spiegheremo subito come migliorare la configurazione.



![Image](assets/fr/034.webp)



Diamo un'occhiata più da vicino alla mia attuale configurazione **SSH** in:**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



La configurazione suggerita di seguito può ancora essere ottimizzata, ma fornisce una buona base. *Si noti che ho rimosso alcuni commenti per una maggiore leggibilità*.



Noi:





- Cambiare la porta di connessione SSH (dimenticare la 22 predefinita)
- Aumentare il livello di verbosità dei log, da **INFO a VERBOSE**
- Impostare **LoginGraceTime** a **2 minuti**



Se non vengono immesse informazioni sulla connessione entro due minuti, la connessione viene interrotta.





- Attivare **Modalità di restrizione**



Specifica se "sshd" deve controllare le modalità e il proprietario dei file dell'utente e la sua home directory prima di convalidare una connessione. Questo è normalmente auspicabile, perché a volte i novizi lasciano accidentalmente la loro directory o i loro file completamente accessibili a tutti. L'impostazione predefinita è "sì".





- Impostare **MaxAuthtries** su 3



Rappresenta il numero di tentativi di autenticazione falliti prima che la comunicazione venga chiusa.





- Impostare **MaxSessions** su 2



Rappresenta il numero massimo di sessioni simultanee.





- Abilitare l'autenticazione a chiave pubblica



```
PubkeyAuthentication yes
```





- Mantenere l'autenticazione con password:



```
PasswordAuthentication yes
```



Vietate le password vuote e l'autenticazione **Kerberos**, così come l'autenticazione **diretta di root**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Assicurarsi di avere "**PermitRootLogin no", se è uguale a "yes", è il "male assoluto "**.





- Vietare il reindirizzamento delle connessioni TCP



```
AllowTcpForwarding no
```



Indica se i reindirizzamenti TCP sono consentiti, con "sì" come impostazione predefinita. Attenzione: la disabilitazione dei reindirizzamenti TCP non aumenta la sicurezza se gli utenti hanno accesso a una shell, poiché possono comunque impostare i propri strumenti di reindirizzamento.





- Vietare il reindirizzamento X11



```
X11Forwarding no
```



Indica se i reindirizzamenti X11 sono accettati, con "no" come impostazione predefinita. Attenzione: anche se i reindirizzamenti X11 sono disabilitati, ciò non aumenta la sicurezza, poiché gli utenti possono comunque impostare i propri reindirizzatori. Il reindirizzamento X11 è automaticamente disabilitato se si seleziona **UseLogin**.





- Impostare il timeout di comunicazione tra il client e sshd



```
ClientAliveInterval  300
```



Definisce un timeout in secondi, dopo il quale, se non vengono ricevuti dati dal client, il servizio sshd invia un messaggio di richiesta di risposta dal client. Per impostazione predefinita, questa opzione è impostata su "0", il che significa che questi messaggi non vengono inviati al client. Solo la versione 2 del protocollo SSH supporta questa opzione.



```
ClientAliveCountMax 0
```



Secondo la [documentazione (*pagina uomo*) per sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), ecco cosa significa questa opzione: "Imposta il numero di messaggi di attesa (vedi sopra) da inviare senza risposta dal client per **sshd**. Se questa soglia viene raggiunta mentre i messaggi di attesa sono stati inviati, **sshd** disconnette il client e termina la sessione. È importante notare che questi messaggi di attesa sono molto diversi dall'opzione **KeepAlive** (sotto). I messaggi di attesa della connessione vengono inviati attraverso il tunnel crittografato e non sono quindi falsificabili. Il mantenimento della connessione a livello TCP abilitato da **KeepAlive** è falsificabile. Il meccanismo di mantenimento della connessione è interessante quando il client o il server devono sapere se la connessione è inattiva"





- Prevenire la divulgazione di informazioni disabilitando **motd, banner, lastlog**



```
PrintMotd no
```



Specifica se sshd deve mostrare il contenuto del file "/etc/motd" quando un utente si collega in modalità interattiva. Su alcuni sistemi, questo contenuto può essere visualizzato anche dalla shell, tramite /etc/profile o un file simile. Il valore predefinito è "yes".



```
Banner none
```



Si noti che in alcune giurisdizioni l'invio di un messaggio prima dell'autenticazione può essere un prerequisito per la protezione legale. Il contenuto del file specificato viene trasmesso all'utente remoto prima che venga concessa l'autorizzazione alla connessione. Questa opzione deve essere configurata, poiché per impostazione predefinita non viene visualizzato alcun messaggio.



In immagini, questo dà:



![Image](assets/fr/019.webp)



### D. Punteggio dell'audit



Infine, non dimentichiamo di controllare il **punteggio di audit di Lynis**! Vediamo che il **punteggio di Hardening è 63** e che il file di report può essere visualizzato in "**/var/log/lynis-report.dat**". C'è anche il file "**/var/log/lynis.log**".



**In altre parole, più alto è il punteggio, meglio è! È quindi necessario lavorare sulla configurazione per ottenere il punteggio più alto possibile, consentendo al contempo alla macchina e ai servizi ospitati di funzionare normalmente (il che significa eseguire test funzionali).



![Image](assets/fr/046.webp)



Diamo un'occhiata ai risultati sul mio secondo server, dove ho dedicato un po' più di tempo all'hardening! Quindi è normale che il punteggio sia più alto (**76**).



![Image](assets/fr/045.webp)



## V. Pianificazione automatizzata Lynis



**Lynis** offre anche la possibilità di eseguire i controlli tramite un'attività pianificata. Esiste infatti l'opzione **"--cronjob "**, che esegue tutti i test di Lynis senza bisogno di convalida o azione da parte dell'utente. È quindi possibile creare molto semplicemente uno script che esegua **Lynis** e metta l'output in un file con data e ora del nome del server in questione. Ecco un file di questo tipo da inserire nella cartella */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



La variabile **"AUDITOR_NAME "** è semplicemente una variabile che verrà impostata nell'opzione **"--auditor "** di **Lynis** in modo che questo nome venga visualizzato nel report:



![Image](assets/fr/059.webp)



Creeremo anche alcune variabili contestuali che ci aiuteranno a organizzarci meglio, come il nome dell'host e la data per assegnare il nome al report e la marcatura temporale, e il percorso della cartella in cui vogliamo inserire i nostri report.



## VI. Conclusione



Lynis è uno strumento molto pratico che vi aiuterà a risparmiare tempo e a essere più efficienti quando vorrete saperne di più sullo stato della configurazione di un server Linux, soprattutto in termini di sicurezza. Tuttavia, non dimenticate che ogni modifica deve essere testata prima di essere applicata in produzione, tenendo conto del vostro utilizzo e del vostro contesto.



Probabilmente non si applicherà la stessa configurazione per un VPS esposto alla Rete, dove è necessaria una sola connessione SSH (perché si è l'unica persona a connettersi), a differenza di una **bastion** o di uno **scheduler** che avranno bisogno di moltiplicare le connessioni **SSH.**



Una volta ottenuta una configurazione adeguata in termini di hardening, è consigliabile adottare uno strumento di automazione, in modo da non dover ripetere manualmente le operazioni, che richiederebbero molto tempo e sarebbero soggette a errori. Ad esempio, è possibile utilizzare **: Puppet, Chef, Ansible, ecc...**



Non dimenticate di comunicare con i vostri team prima dell'implementazione: dovete far capire loro perché state facendo questi cambiamenti, non solo dirgli che li state facendo. Alla fine, l'obiettivo sarà quello di trasmettere le buone pratiche, aumentando così le possibilità di successo.



Infine, è possibile confrontare **Lynis** con altri strumenti, che sono numerosi. Se volete orientarvi verso una gestione centralizzata pur rimanendo open source, vi consiglio lo strumento [Wazuh] (https://wazuh.com/).



**Questo tutorial è terminato, divertitevi con Lynis!
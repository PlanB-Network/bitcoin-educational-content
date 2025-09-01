---
name: Ntopng
description: Monitorare la rete con ntopng
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Florian Duchemin pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale



___



## I. Presentazione



**Che si tratti di controllare la fluidità della rete, di ottenere un quadro chiaro dell'utilizzo o di statistiche sulle prestazioni, il monitoraggio del flusso di rete è una parte importante di una rete aziendale**. Aiuta ad anticipare le modifiche all'infrastruttura e a garantire la qualità d'uso per gli utenti (nota anche come QoE per *Quality of Experience*, in contrapposizione a QoS).



A tal fine, sono disponibili numerose tecniche e software/protocolli. Netflow, ad esempio, sviluppato da Cisco, può essere utilizzato per recuperare le statistiche dei flussi IP da un Interface, ma il suo uso è limitato alle apparecchiature compatibili.



Ecco perché in questo tutorial vi presenterò **Ntop** e vi mostrerò come utilizzarlo nella vostra infrastruttura per tenere sotto controllo l'utilizzo della rete.



Ntop è un software open source che può essere installato su qualsiasi macchina Linux. È gratuito e può raccogliere i seguenti dati:





- Utilizzo della larghezza di banda
- Principali clienti
- Destinazioni principali
- Protocolli utilizzati
- Applicazioni utilizzate
- Porte utilizzate
- Ecc.



Ora ribattezzata **Ntopng (New Generation)**, offre gratuitamente molte funzioni di base. È disponibile anche una versione commerciale che consente di esportare gli avvisi configurati in software di tipo SIEM o di filtrare il traffico con regole definite direttamente dalla sonda.



## II. Prerequisiti



L'installazione di una sonda Ntop varia a seconda dell'apparecchiatura e dell'ambiente. Pertanto, non vi fornirò una guida passo-passo, ma vi illustrerò le varie possibilità.



### A. Modalità di bordo



Se avete un firewall pfSense, OPNSense o Endian in produzione, o anche una workstation Linux con NFTables, buone notizie! Potete installare direttamente Ntopng e iniziare a monitorare le vostre interfacce.



Il vantaggio di questa tecnica è che non richiede hardware aggiuntivo. D'altra parte, aumenta l'utilizzo delle risorse, quindi assicuratevi di avere un hardware adeguato o una macchina virtuale di dimensioni sufficienti (minimo 2 core e 2BG di RAM).



### B. Modalità TAP / SPAN



Un **tap** è **un dispositivo di rete che duplica il traffico che lo attraversa e lo invia a un altro dispositivo.** Il vantaggio di questo dispositivo è che non richiede alcuna modifica all'infrastruttura esistente e può essere collocato ovunque per monitorare sezioni specifiche della rete, o tra lo switch core e il router edge per analizzare il traffico da/verso Internet.



Il grande svantaggio di questo tipo di apparecchiatura è il suo costo. Nelle reti Gigabit di oggi, un tap passivo non è in grado di catturare correttamente il traffico di rete, quindi è necessario un dispositivo attivo dal costo di circa 200 euro (minimo).



La modalità **SPAN**, nota anche come **port mirroring**, viene utilizzata da uno switch per inoltrare il traffico da una porta all'altra. È di gran lunga il metodo che preferisco, in quanto è semplice da configurare e, come il tap, consente di monitorare una parte della rete o l'intera rete a piacimento. Tuttavia, ci sono due svantaggi: lo switch deve integrare questa funzione e il suo utilizzo può aumentare il carico del processore sullo switch.



### C. Modalità router



È perfettamente possibile montare un router sotto Linux e installarvi ntopng. L'unico inconveniente di questo metodo è che modificherà la rete, sia il suo indirizzamento interno, sia l'indirizzamento tra il router "reale" e quello che si sta aggiungendo.



Nota: per i lettori dell'articolo [Creare un router Wifi con Raspberry Pi e RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) è perfettamente possibile installare ntopng sul proprio Rpi per ottenere statistiche accurate!



### D. Modalità ponte



Un'alternativa interessante è l'uso di **una macchina Linux in modalità bridge.** Collocata tra due apparecchiature, permette di catturare tutto il traffico senza dover intervenire nella configurazione dell'infrastruttura o delle sue apparecchiature. Poiché una vecchia macchina può fare il lavoro, il costo di questo metodo può anche essere interessante. Si noti che per essere ottimale, il dispositivo dovrebbe avere tre schede di rete, due in modalità bridge, una per accedere a Interface e SSH. È possibile utilizzare solo due schede, ma in questo caso verrà catturato anche il traffico di amministrazione del dispositivo...



Quindi è **quest'ultima modalità che utilizzerò**. Per motivi pratici, utilizzerò macchine virtuali per la dimostrazione, ma il metodo rimane lo stesso per l'uso su macchine fisiche.



## III. Preparazione della sonda con ponte Interface



Per la sonda, ho scelto una macchina **Debian 11** con installazione minima.



Primo passo, sempre lo stesso, aggiornare il file:



```
apt-get update && apt-get upgrade
```



Installare quindi il pacchetto **bridge-utils**, che ci permetterà di creare il nostro ponte:



```
apt-get install bridge-utils
```



Una volta installata, la prima cosa da notare è il nome attuale delle nostre schede di rete. In Debian, questo nome può assumere diverse forme e ci servirà per la configurazione.



Un semplice comando **ip add** restituirà un output con queste informazioni:



![Image](assets/fr/016.webp)



Qui vedo 3 interfacce:





- Lo**: è il Interface di loopback; è un Interface virtuale che "fa il giro" sull'apparecchiatura. In pratica, questo Interface, il cui Address è 127.0.0.1 (anche se qualsiasi Address in 127.0.0.0/8 va bene, poiché questo intervallo è riservato a questo scopo) viene utilizzato per contattare l'apparecchiatura stessa. Se avete installato un sito web sulla vostra workstation (usando WAMPP, per esempio), probabilmente avete usato il Address "*localhost*" Address per visualizzare il sito ospitato sulla propria macchina. Questo nome di host è associato al Address 127.0.0.1 e quindi al loopback del Interface.
- ens33**: questo è il mio primo Interface, che ha ricevuto un Address qui dal mio DHCP
- ens36**: il mio secondo Interface



Ora che ho tutte le informazioni, posso modificare il file */etc/network/interfaces* per creare il mio bridge. Ecco come appare attualmente (può variare):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



La prima parte riguarda il mio Interface di loopback, che non toccherò, seguito dal Interface ens33. Le modifiche riguardano l'aggiunta del mio secondo Interface (ens36) e la configurazione del bridge con queste due interfacce:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Ecco alcune spiegazioni di questi primi cambiamenti:





- auto *Interface***: "avvia" automaticamente Interface all'avvio del sistema
- iface *Interface* inet manual**: per usare il Interface senza alcun IP Address. Come la parola chiave "static" per definire un IP Address statico o "dhcp" per utilizzare un indirizzamento dinamico



Le modifiche continuano:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Anche qui, alcune spiegazioni:





- iface br0 inet static**: qui ho definito il mio bridge Interface (*br0*) con un Address statico.
- Address, netmask, gateway**: informazioni sull'indirizzamento della scheda
- bridge_ports**: interfacce da includere nel bridge
- bridge_stp**: il protocollo Spanning Tree viene utilizzato quando si interconnettono gli switch per rilevare i collegamenti ridondanti ed evitare i loop. Poiché un ponte può essere inserito tra due percorsi di rete, può essere la fonte di un loop, da cui la possibilità di abilitare questo protocollo. Non ne ho bisogno qui, quindi lo disabilito.



Salvare le modifiche e riavviare la rete:



```
systemctl restart networking
```



Per verificare le modifiche, visualizzare nuovamente il risultato del comando **ip** add:



![Image](assets/fr/021.webp)


Si può vedere chiaramente **il mio nuovo Interface "*br0*" con l'IP Address che gli ho assegnato.** Per inciso, si può anche vedere che le mie due interfacce fisiche sono effettivamente "UP", ma non hanno alcun IP Address.



## IV. Installazione di NtopNG



Ora che la nostra sonda è in grado di sniffare il traffico tra la mia rete e il router, non resta che installare ntopng. Per farlo, modificate prima il file */etc/apt/sources.list* e aggiungete **contrib** alla fine di ogni riga che inizia con **deb** o **deb-src**.



Per impostazione predefinita, i sorgenti dei pacchetti contengono solo pacchetti conformi alle DFSG (*Debian Free Sotftware Guidelines*), identificati dalla parola chiave **main**. È possibile aggiungere anche queste fonti:





- contrib**: pacchetti contenenti software conforme a DFSG, ma che utilizzano dipendenze che non fanno parte del ramo **main**
- non-free**: contiene pacchetti che non sono conformi a DFSG



Esempio di riga in /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Quindi aggiungerò la parola **contributo** a righe come queste.



Il resto dei passaggi è elencato nel sito [NtopNG] (https://packages.ntop.org/apt/) dove, per Debian 11, è necessario aggiungere i sorgenti di Ntop per una futura installazione. Questa aggiunta è automatizzata utilizzando un file:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Poi si passa alla fase di installazione vera e propria:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Il primo comando cancella la cache del gestore di pacchetti apt. Il secondo aggiorna l'elenco dei pacchetti e il terzo installa NtopNG.



Dopo l'installazione, il software **NtopNG è direttamente disponibile sulla porta 3000 della macchina Debian**. Quindi per me è `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



Pagina iniziale di NtopNG



Vengono mostrati il login e la password predefiniti, quindi non resta che inserirli!



## V. Utilizzo di NtopNG



Quando si accede per la prima volta, la prima cosa che viene chiesta è di cambiare la password di amministrazione e la lingua predefinite. Purtroppo il francese non è tra queste.



Si arriva quindi al cruscotto:



![Image](assets/fr/023.webp)



Cruscotto NtopNG



Non abituatevi a questo! Se notate il riquadro giallo nella parte superiore dello schermo, vedrete la frase: "*La licenza scade alle 04:57*". Per impostazione predefinita, l'installazione lancia una prova della versione completa di NtopNG, ma per un tempo (molto) limitato. Una volta raggiunto questo "conto alla rovescia", viene attivata la versione *comunitaria* e il cruscotto cambia:



![Image](assets/fr/024.webp)



Nuovo cruscotto della comunità NtopNG



La prima cosa da fare è **verificare che il Interface corretto sia in ascolto**. Nell'angolo in alto a sinistra, un elenco a discesa delle interfacce disponibili consente di selezionare il Interface che ci interessa: br0



![Image](assets/fr/025.webp)



Selezione Interface



La nuova finestra mostra i "Top Flaw Talkers", cioè i dispositivi che comunicano di più. In questo caso compaiono solo due stazioni:



![Image](assets/fr/026.webp)



**Gli host sorgente appaiono a sinistra, le destinazioni a destra ** Questo permette di visualizzare l'uso della larghezza di banda totale da parte di ciascun host e di avere una visione complessiva del traffico di rete. Non è male, ma possiamo andare oltre...



Se clicco su "*Hosts*", ad esempio, ottengo un grafico che mostra il consumo di energia in invio e in ricezione di ciascun host della mia rete. Qui, ad esempio, posso vedere che 192.168.1.37 rappresenta da solo l'80% del mio traffico:



![Image](assets/fr/027.webp)



Se faccio clic sull'IP Address dell'host in questione, vengo reindirizzato a una pagina di riepilogo:



![Image](assets/fr/028.webp)



Posso vedere, ad esempio, che si tratta di una macchina VMWare (riconoscendo il SI del mio MAC Address), che si chiama DESKTOP-GHEBGV1 (quindi sicuramente un host Windows) E ho **statistiche sui pacchetti ricevuti e inviati, oltre alla quantità di dati**.



Noterete anche un nuovo menu nella parte superiore di questo riepilogo. Vi suggerisco di fare clic su "**Apps**" per vedere cosa sta generando così tanto traffico:



![Image](assets/fr/017.webp)


Sembra che abbiamo una risposta! Nel grafico a sinistra, **vediamo che il 76,6% del traffico proviene da ... Windows Update**, quindi questo host sta scaricando aggiornamenti!



NtopNG utilizza una tecnologia chiamata DPI per *Deep Packet Inspection*, che consente di classificare ogni flusso di rete e di definire l'applicazione (o la famiglia di applicazioni) che si trova dietro di esso.



Per dimostrarlo, lancio un video di YouTube sul mio host:



![Image](assets/fr/018.webp)



**Il traffico è stato immediatamente riconosciuto e categorizzato!



Nota: per ovvie ragioni, questo tipo di software può sollevare problemi di privacy, quindi fate attenzione a usarlo nelle giuste condizioni. Si noti inoltre che è possibile **anonimizzare i risultati**; l'opzione si trova in **Impostazioni > Preferenze > Varie** e si chiama "**Maschera IP Host Address**".



## VI. Rilevamenti e avvisi



NtopNG è anche in grado di emettere avvisi di sicurezza su determinati feed. Questi si trovano nel menu **Avvisi**, nel banner di sinistra. Qui, ad esempio, ho un totale di 2851 avvisi, suddivisi in diverse gravità: Avviso, Avvertenza ed Errore.



![Image](assets/fr/019.webp)



Diamo un'occhiata agli avvisi di alta criticità, ne ho 17!



Facendo clic su questa figura vengono visualizzati i dettagli degli avvisi. Non c'è nulla di allarmante, si tratta di un falso positivo: il download degli aggiornamenti viene classificato come un trasferimento di file binari in un flusso HTTP, il che potrebbe significare un attacco.



![Image](assets/fr/020.webp)



Tuttavia, poiché sto usando la versione gratuita, non posso escludere i domini o gli host che sono la fonte degli avvisi, quindi dovrete tenerli d'occhio per evitare di perdere qualcosa di molto più preoccupante. NtopNG invierà generate avvisi in caso di:





- Download di file binari su HTTP
- Traffico DNS sospetto
- Utilizzo di una porta non standard
- Rilevamento dell'iniezione SQL
- Cross-Site Scripting (XSS)
- Ecc.



## VII. Conclusione



In questa esercitazione abbiamo visto **come impostare una sonda con NtopNG** che ci permette di **analizzare il nostro traffico di rete** per visualizzare l'utilizzo dei protocolli e l'occupazione di ogni host, ma anche di rilevare il traffico sospetto.



Purtroppo, in questo articolo non posso descrivere tutte le caratteristiche e le possibilità, ma sentitevi liberi di esplorarle!



Questa soluzione può essere implementata in modo permanente all'interno di un'infrastruttura aziendale. NtopNG può anche esportare i risultati in un database InfluxDB, consentendo di creare dashboard personalizzati con uno strumento di terze parti come Graphana.
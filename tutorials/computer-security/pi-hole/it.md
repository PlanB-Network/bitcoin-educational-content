---
name: Pi-Hole
description: Un blocco degli annunci per l'intera rete
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Florian Duchemin pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale



___



## I. Presentazione



Lo abbiamo fatto tutti non appena abbiamo avviato il nostro browser preferito: installare un **adblocker** (blocco degli annunci). Tuttavia, quando si utilizza il browser della TV o un dispositivo Android, ecc... È un po' più difficile trovare qualcosa che funzioni. E se in casa c'è più di un dispositivo, bisogna ripetere l'operazione per ogni browser!



In questo tutorial, risolveremo un problema semplice**: fornire un ad blocker a tutte le macchine della nostra rete e gestirlo in modo centralizzato **



Per farlo, utilizzeremo uno strumento sviluppato a questo scopo: **Pi-Hole**



Pi-Hole è un sinkhole DNS. Utilizzerà le richieste DNS effettuate dai vostri dispositivi per convalidare o negare il traffico, proteggendovi così da indirizzi e domini noti per la distribuzione di pubblicità, malware e così via.



DNS è l'acronimo di Domain Name System (sistema di nomi di dominio). Che cos'è un nome di dominio? Beh, "it-connect.fr" è solo un esempio. Un nome di dominio è un identificativo univoco per una o più risorse, solitamente amministrate da un'unica entità.



Il nome del computer più il nome del dominio è chiamato FQDN, ovvero *Fully Qualified Domain Name*. Consente di raggiungere un computer specifico semplicemente "chiamandolo". Ad esempio, quando si digita "www.trucmachin.com", si chiama la macchina "www", che appartiene al dominio "trucmachin.com".



Solo che i nostri computer non capiscono il linguaggio umano, ma solo quello binario, quindi hanno bisogno di un IP Address, che è l'equivalente di un numero di telefono, per raggiungere il sito web.



Quindi, ogni volta che si inserisce il nome di un sito web nel browser o si fa clic su un link, il computer chiede a un server DNS il Address IP corrispondente a quel nome.



**Pi-Hole ispezionerà quindi queste richieste (ce ne sono centinaia ogni giorno!) e bloccherà automaticamente quelle note per ospitare pubblicità o addirittura file dannosi



## II. Installazione di Pi-Hole



Con un nome come Pi-Hole, si potrebbe giustamente pensare che sia necessario un Raspberry-Pi... Ma questo non è del tutto vero. **Pi-Hole può essere installato su qualsiasi computer Linux (Debian, Fedora, Rocky, Ubuntu, ecc.)



D'altra parte, è necessario tenere presente che **questo dispositivo dovrà funzionare 24 ore su 24 per un semplice motivo: senza DNS, niente Internet!** Il Raspberry è quindi una buona idea, poiché consuma quasi zero energia.



Per l'installazione, è sufficiente collegarsi al computer Linux tramite SSH e inserire il seguente comando come "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Nota**: in circostanze normali, non è consigliabile "hackerare" uno script senza prima sapere cosa fa. Se non siete sicuri, visitate la pagina con un browser o scaricate il contenuto come file.
>


> **Nota: nelle versioni minimali di Debian 11, Curl non è installato, quindi è necessario installarlo manualmente con il comando **apt-get install curl** prima di digitare il comando precedente.

Una volta eseguito lo script, verrà eseguita una serie di test e l'installazione stessa si prenderà cura di sé:



![Image](assets/fr/019.webp)



Installazione di Pi-Hole



Una volta completata l'installazione, si aprirà questa schermata:



![Image](assets/fr/020.webp)



Schermata iniziale di Pi-Hole



> **Nota**: se si utilizza il protocollo DHCP sulla macchina, verrà visualizzato un messaggio di avviso. Naturalmente, per un uso corretto, si consiglia vivamente di assegnare un IP fisso alla macchina.

Dopo questa schermata, si riceveranno alcuni messaggi informativi e poi si accederà alla configurazione guidata, che chiederà innanzitutto a quale server DNS Pi-Hole dovrà inoltrare le richieste. Per quanto mi riguarda, ho scelto Quad9, che ha una carta della privacy per gli utenti.



![Image](assets/fr/021.webp)



Selezione DNS - Pi-Hole



> **Nota: se siete in un'azienda, è probabile che il vostro server DNS attuale sia il controller di dominio di Active Directory. Ma non preoccupatevi, in seguito potrete specificare un reindirizzatore condizionale per un dominio di vostra scelta. In genere, sarete in grado di reindirizzare qualsiasi richiesta relativa al vostro dominio locale al vostro server DNS.

Si noterà che alcune scelte includono un'opzione DNSSEC. Fondamentalmente, il protocollo DNS non è sicuro (all'epoca non era stato progettato con questo obiettivo). Il protocollo DNSSEC risolve questo problema aggiungendo un Layer di sicurezza attraverso la crittografia e la firma degli scambi, come spiegato nell'articolo corrispondente: [Sicurezza DNS](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Qualsiasi blocco degli annunci si basa su uno o più elenchi per svolgere il proprio lavoro. Pi-Hole viene fornito di serie con un solo elenco, che può essere selezionato e aggiunto in seguito.



![Image](assets/fr/022.webp)



Per quanto riguarda la domanda su Interface web, la sua installazione è facoltativa, in quanto lo strumento ha una propria riga di comando per la gestione e la visualizzazione. Ma questo Interface è piuttosto piacevole e ben fatto, quindi vi consiglio di installarlo contemporaneamente:



![Image](assets/fr/023.webp)



Se state installando Pi-Hole su una macchina che ha già un server Web, potete rispondere "no" alla seguente domanda. Si noti, tuttavia, che per funzionare sono necessari PHP e diversi moduli. Altrimenti, **lighttpd verrà installato con tutti i moduli necessari**.



![Image](assets/fr/024.webp)



Viene quindi chiesto se si desidera registrare le richieste DNS. **Se desiderate mantenere una cronologia, impostate su sì; altrimenti impostate su no, ma perderete alcune funzionalità** (vedi schermata successiva).



![Image](assets/fr/025.webp)



Per il suo web Interface, Pi-Hole utilizza una funzione propria chiamata FTLDNS, che fornisce un'API e genera statistiche dalle richieste DNS. Questa funzione può includere una modalità "privacy" che maschera i domini richiesti, i clienti dietro la richiesta o entrambi. È utile se si desidera effettuare un monitoraggio senza violare la privacy delle persone o semplicemente se si desidera rispettare le normative vigenti in caso di utilizzo su una rete pubblica.



![Image](assets/fr/026.webp)



Scelta di uno stile di vita privato



Una volta risposto a quest'ultima domanda, lo script farà ciò che deve fare: scaricare i repository GitHub e configurare Pi-Hole. Al termine dell'installazione, verrà visualizzata una schermata di riepilogo con le informazioni più importanti:



![Image](assets/fr/027.webp)



Schermata di riepilogo dell'installazione



Annotare la password web del Interface e le informazioni sulla rete. Ora è il momento di configurare il servizio DHCP nella nostra sede attuale.



## III. Configurazione DHCP



Per funzionare, Pi-Hole ha bisogno di "risolvere" le richieste DNS dei client, che devono sapere che è il sito a cui inviarle. Esistono diversi modi per farlo:





- Modificare le impostazioni DNS del server DHCP (ad esempio, la propria casella)
- Disabilitare questo server e utilizzare quello fornito da Pi-Hole
- Modificare manualmente ogni dispositivo per utilizzare Pi-Hole come DNS



Personalmente scelgo la prima soluzione. È probabile che **siate in possesso di un server DHCP nel luogo in cui vi trovate** (di solito la vostra casella). Quindi non c'è bisogno di preoccuparsi.



Poiché ci sono molte possibilità, tra le scatole dei diversi operatori (che non conosco tutti) e chi ha il proprio router, non fornirò uno screenshot per queste modifiche. In ogni caso, dovrete andare nelle impostazioni DHCP e modificare il parametro "DNS" per includere l'IP Address del vostro Pi-Hole.



Una volta effettuata questa operazione, se i dispositivi sono stati accesi in precedenza, avranno mantenuto le vecchie impostazioni, quindi sarà necessario riavviare la richiesta di configurazione.



Sulle stazioni di lavoro Windows, con un prompt dei comandi:



```
ipconfig /renew
```



Su una workstation Linux:



```
dhclient
```



Per tutti gli altri dispositivi, è necessario spegnerli e riaccenderli.



Quindi dovrebbero ottenere i parametri giusti, da controllare:



```
ipconfig /all
```



Nel campo DNS dovrebbe esserci il Address del vostro Pi-Hole, nel mio caso 192.168.1.42:



![Image](assets/fr/029.webp)



## IV. Utilizzo del web Pi-Hole Interface



Per facilitare l'amministrazione, **Pi-Hole** beneficia di un Interface web ben progettato. Facile da usare e accessibile, consente di:





- Visualizzare il numero di richieste, le richieste bloccate, ecc. in tempo reale.
- Gestione di Whitelist e Blacklist
- Aggiungere voci statiche, alias, ecc.
- Aggiungi elenchi
- E molte altre funzioni!



Da parte mia, aggiungerò un elenco di blocco. Come già detto, è stato installato solo un elenco contemporaneamente a Soft. Esistono molti elenchi per i siti di annunci, ma è meglio sceglierne almeno uno specifico per il paese in cui si vive. Uno degli elenchi più noti è **EasyList**, e uno di questi è specifico per la Francia: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Per aggiungerlo, collegarsi prima all'amministratore del Interface: **http://<ip_du_PiHole>/admin**



La password di amministratore è già stata generata (si veda la schermata di fine installazione), quindi è sufficiente inserirla per accedere a Interface:



![Image](assets/fr/030.webp)



Interface da Pi-Hole



Possiamo vedere, ad esempio, che ci sono due clienti connessi al Pi-Hole, che ha elaborato 442 richieste e che 8 di queste sono state bloccate. Questi grafici possono essere una buona fonte di informazioni, soprattutto in un contesto professionale.



Per aggiungere la nostra lista, accedere ai menu "**Gestione dei gruppi**" e "**Liste**":



![Image](assets/fr/031.webp)



Possiamo vedere la nostra prima lista "**StevenBlack**", per aggiungere la nostra, copiate il link che vi ho dato sopra e inseritelo nel campo "**Address**", per la descrizione, ho scelto di mettere il nome della lista:



![Image](assets/fr/032.webp)



Aggiunta di un elenco in Pi-Hole



Non resta che fare clic su "**Aggiungi**" per aggiungerlo. Per attivarlo, è necessario eseguire un ulteriore passaggio per "avvertire" Pi-Hole di occuparsi di questo elenco. Per fare questo:





- Utilizzare la riga di comando integrata
- O il web Interface



Personalmente ho scelto la seconda, perché se avete guardato bene, il link allo script PHP che esegue l'aggiornamento si trova direttamente nella pagina in cui ci troviamo (la parola "online"). Quindi basta cliccarci sopra per accedere a una pagina con una sola opzione:



![Image](assets/fr/033.webp)



La pagina visualizzerà il risultato dello script una volta completato, il che significa che l'elenco è stato preso in considerazione (a meno che non venga visualizzato un messaggio di errore, ovviamente).



Come annunciato all'inizio di questo tutorial, Pi-Hole consente anche di **bloccare i domini noti per la distribuzione di malware. Per rafforzare questa funzione, vi suggerisco di aggiungere anche l'elenco dei domini regolarmente aggiornato distribuito da Abuse.ch**, che rafforzerà in modo significativo la sicurezza della vostra rete, disponibile all'indirizzo [questo Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Naturalmente, è possibile aggiungere qualsiasi elenco che si ritiene rilevante o gestire manualmente la propria blacklist tramite il menu blacklist.



## V. Test Pi-Hole



Ora che tutto è pronto, non resta che testare la soluzione per assicurarsi che funzioni correttamente.



Ad esempio, cercherò di raggiungere il dominio *http://admin.gentbcn.org/* che si trova nell'elenco di Abuse.ch perché è noto per ospitare malware:



![Image](assets/fr/034.webp)



Ovviamente sono stato bloccato da qualche parte. Per essere sicuri che sia stato il Pi-Hole a fare il lavoro, possiamo controllare il registro delle query nella pagina web di Interface "Query Log" per vedere se si tratta di un blocco da una voce dell'elenco:



![Image](assets/fr/035.webp)



## VI. Conclusione



In questo tutorial vi abbiamo mostrato come impostare un server DNS che non solo elimina la maggior parte degli annunci per il vostro comfort di navigazione, ma aggiunge anche **un Layer di sicurezza bloccando i domini di phishing e di diffusione di malware**.



Tutti gratuiti ed economici se installati su un Raspberry-Pi (in termini di consumo energetico).
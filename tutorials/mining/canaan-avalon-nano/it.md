---
name: Canaan Avalon Nano 3S
description: Configurazione del ASIC Avalon per il solomining o il pooling Miner
---

![cover](assets/cover.webp)



In questo tutorial vedremo come configurare il Canaan Avalon Nano 3S, per un facile uso domestico della Miner.



Fino ad oggi, le macchine ASIC (*Application Specific Integrated Circuit*) progettate specificamente per svolgere un determinato compito - in questo caso, il calcolo Hash (SHA-256) per Miner di Bitcoin - erano particolarmente inadatte all'uso domestico. Il fastidio del rumore, il calore generato e la necessità di adattare l'impianto elettrico per supportare l'enorme potenza di questi dispositivi hanno impedito alla maggior parte di noi di partecipare.



Oggi Canaan, uno dei principali produttori di macchine ASIC, ha deciso di affrontare il mercato dei privati che desiderano il Miner a casa, offrendo una gamma di prodotti relativamente silenziosi e molto facili da installare (plug & play).



Questi dispositivi sono commercializzati come riscaldatori ausiliari, nel caso dell'**Avalon Nano 3S (140W)**, o come mini-radiatori con una potenza di **800W** nel caso dell'**Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Si noti che la differenza di prezzo con i riscaldatori tradizionali di potenza equivalente non consente, nella stragrande maggioranza dei casi, di ottenere un profitto finanziario. I satoshi generati dall'attività del Mining non compenseranno mai questa differenza di prezzo, a meno che non si abbia accesso a elettricità gratuita (in eccesso) o molto economica.



A mio parere, questi dispositivi dovrebbero essere visti più come un modo semplice per fare Miner a casa per coloro che desiderano farlo per motivi personali: *ottenere un Satss non KYC / giocare alla "lotteria" con la solominazione / partecipare alla decentralizzazione del Hashrate ecc.*, beneficiando **come bonus** del calore generato per riscaldare la propria stanza in inverno. Ma non come un modo per risparmiare denaro, almeno nella maggior parte dei casi (paesi occidentali).



## Unboxing e caratteristiche



Per prima cosa, vediamo cosa c'è all'interno della scatola di Avalon Nano 3S.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Una volta aperta la confezione, troverete un involucro di cartone contenente un ricevitore WIFI che, come vedremo in seguito, dovrete collegare alla porta USB del dispositivo per consentirgli di connettersi alla rete locale. Sono inclusi anche il manuale di istruzioni e un perno metallico per ripristinare le impostazioni di fabbrica del dispositivo, se necessario.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Una volta tolto tutto dalla scatola, ecco cosa c'è in dotazione: la macchina stessa, ovviamente, il manuale d'uso, il ricevitore WIFI, il già citato puntale metallico e l'alimentatore Supply del dispositivo. La carta di credito in dotazione non è degna di nota, a nostro avviso.



![image](assets/fr/05.webp)



Di seguito è riportata una tabella che riassume le specifiche tecniche generali del Nano 3S:



| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## Accensione e connessione alla rete locale



Una volta disimballato, posizionare Avalon Nano 3 S possibilmente in un'area relativamente aperta per consentire al calore di circolare. Quindi iniziare a inserire il piccolo modulo ricevitore WIFI come mostrato di seguito:



![image](assets/fr/06.webp)


Quindi collegare la spina USB-C del Supply alla porta USB-C del dispositivo per alimentarlo.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Il dispositivo si avvia e sullo schermo appare il logo di Avalon Nano, seguito da un logo "cellulare" con la scritta "Configurare la rete con l'applicazione Avalon Family".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



A tal fine, accedere al negozio di applicazioni mobili, cercare e scaricare l'applicazione **Avalon Family**.



![image](assets/fr/11.webp)


Una volta installato, apritelo facendo clic su "Skip" nell'angolo in alto a destra, poi sul pulsante "Add" e infine su "Search". Assicuratevi che il Bluetooth sia abilitato sul vostro smartphone, in modo che il rilevamento del dispositivo avvenga senza problemi.



![image](assets/fr/12.webp)


Una volta che il dispositivo è stato rilevato dall'applicazione, fare clic su di esso e scegliere "Connetti". Verrà quindi visualizzata la schermata in cui inserire i dettagli della connessione WIFI.


![image](assets/fr/13.webp)


Una volta che il dispositivo è collegato alla rete locale, la schermata si presenterà come segue:



![image](assets/fr/14.webp)



Mostra un Hashrate "fittizio", poiché non è stato ancora configurato alcun pool, e l'ora, la data, l'alimentazione e l'IP del dispositivo Address - molto utile se si desidera accedere al Interface del dispositivo tramite un PC e un browser (per saperne di più in seguito).



![image](assets/fr/15.webp)




## Collegamento a un Mining pool



**Questa parte è comune ai modelli Nano 3 e Mini 3, poiché i processi sono strettamente identici**.



Sia che si voglia "solominare", sia che si voglia "mettere in comune" il Miner, ci si dovrà connettere a un Mining pool. In effetti, il nostro dispositivo non è altro che un creatore di Hash senza alcuna conoscenza della rete Bitcoin. La connessione a un pool gli dà accesso alla rete Bitcoin e gli consente di ricevere modelli di blocco su cui lavorare.



### Utilizzo dell'applicazione per la connessione a un Mining pool



Nell'applicazione Avalon Family, selezionare il dispositivo come mostrato di seguito. Verrà chiesto automaticamente di modificare la password di amministratore della macchina. Fare clic su "OK" se si desidera farlo, oppure su annulla per lasciare la password di accesso predefinita "admin".


![image](assets/fr/16.webp)


Selezionare quindi "Impostazioni", poi "Configurazione pool" e inserire i parametri per i 3 pool richiesti.


I pool #2 e #3 fungeranno da backup nel caso in cui uno di essi si guasti, in modo che il Miner non funzioni per niente. Per impostazione predefinita, il Hashrate sarà puntato al pool #1



Nel nostro caso abbiamo scelto:




- 1 - Piscina pubblica,
- 2 - CkPool,
- 3 - Oceano.



![image](assets/fr/17.webp)



Per ulteriori dettagli sulla connessione a un Mining pool, consultare queste esercitazioni:



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Per riassumere, abbiamo bisogno di





- il pool Address, di solito **stratum+tcp://xxxxxxxx:port**.





- il nome del "lavoratore" composto dal *vostro Bitcoin Address* e dallo *pseudo* che avete scelto per il vostro dispositivo, separando i due con un *punto*, ad esempio:**bc1qxxxxxxxxxxxxx.MonAvalonNano3S**





- la password, che di solito è sempre "**x**"



Una volta inserite le informazioni sulla piscina, cliccare su "Salva".



![image](assets/fr/18.webp)


Riavviare il dispositivo come indicato e attendere qualche minuto finché il Hashrate non sarà puntato sulla piscina preferita (#1).



### Utilizzo del browser per collegarsi a un Mining pool



È inoltre possibile collegarsi a un Mining pool e, più in generale, accedere al sistema di gestione Interface del dispositivo tramite il proprio browser preferito.



Per farlo, digitate nella barra di ricerca del browser l'IP Address del dispositivo mostrato nella schermata sottostante, nel nostro esempio **192.168.144.6**



![image](assets/fr/15.webp)



Viene visualizzata la seguente pagina, che chiede di aprire l'applicazione Avalon Family e di scansionare il codice QR visualizzato con l'applicazione.



![image](assets/fr/20.webp)



Aprire l'applicazione e fare clic sui 3 trattini in alto a destra, quindi su scansione. Scansionare il codice QR del browser, quindi inserire la password di amministratore dell'applicazione e fare clic su OK.



![image](assets/fr/21.webp)



Qui si trova la pagina web che consente di interagire con Avalon. È più un cruscotto per visualizzare le metriche della macchina che un mezzo per configurarla.



Le impostazioni del pool sono comunque accessibili in questo modo, facendo clic su **"Pool Config "** nell'angolo in basso a destra.



![image](assets/fr/22.webp)



Come per l'applicazione mobile, qui è possibile inserire i parametri della piscina.



![image](assets/fr/23.webp)



## Controllo del dispositivo tramite l'app Avalon Family



Ora abbiamo collegato il nostro Miner alla rete locale e abbiamo puntato il nostro Hashrate verso le piscine di Mining. Ora scopriamo le caratteristiche essenziali della nostra macchina attraverso l'applicazione Avalon Family.



Nell'applicazione della famiglia Avalon, fare clic sull'icona corrispondente ad Avalon Nano 3S.


vengono presentati 3 menu: "Modalità lavoro", "Controllo luce" e "Impostazioni". Per prima cosa, fare clic su "Modalità di lavoro". Verranno proposte 3 modalità di alimentazione della macchina.



**Basso**: porta circa 3 Th/s di Hashrate per 70W di consumo energetico


**Medium**: consente di ottenere circa 4,5 Th/s di Hashrate per 100W di consumo energetico


**Alto**: fornisce circa 6 Th/s di Hashrate con un consumo massimo di 140W



![image](assets/fr/31.webp)


Facciamo un passo indietro ed esploriamo il menu "Controllo luce". Si tratta di una funzione puramente estetica. Sono disponibili numerose opzioni per variare il colore, l'intensità, il calore, per spegnere i LED del dispositivo durante la notte, ecc. È facile scoprirlo da soli.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Infine, l'ultimo menu disponibile è il menu "Impostazioni", già visto per la connessione alle vasche Mining. Qui è possibile gestire le vasche, cambiare la password dell'amministratore e osservare varie metriche come la data di scadenza della garanzia, la pulizia dei filtri o come contattare l'assistenza in caso di guasto. Qui è possibile gestire i pool, modificare la password di amministratore del dispositivo e osservare varie metriche come la data di scadenza della garanzia, la pulizia del filtro o come contattare l'assistenza in caso di guasto.



![image](assets/fr/35.webp)


Per la manutenzione e per mantenere il filtro il più pulito possibile, si consiglia di utilizzare un aspirapolvere e di aspirare regolarmente le entrate e le uscite dell'aria per evitare intasamenti.



Siamo giunti alla fine di questa esercitazione, che ci ha insegnato come collegare il nostro Avalon Nano 3 S alla rete locale, come puntare il nostro Hashrate alle piscine Mining e come navigare tra le opzioni e le impostazioni utilizzando l'applicazione Avalon Family.



Per saperne di più, date un'occhiata al nostro tutorial sulla versione superiore dell'Avalon: il Mini 3.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7
---
name: Canaan Avalon Mini 3
description: Configurazione del ASIC Avalon per il solomining o il pooling Miner
---

![cover](assets/cover.webp)



In questa guida vedremo come configurare il Canaan Avalon Mini 3, per un facile utilizzo domestico del Miner.



Fino ad oggi, le macchine ASIC (*Application Specific Integrated Circuit*) progettate specificamente per svolgere un determinato compito - in questo caso, il calcolo Hash (SHA-256) per Miner di Bitcoin - erano particolarmente inadatte all'uso domestico. Il fastidio del rumore, il calore generato e la necessità di adattare l'impianto elettrico per supportare l'enorme potenza di questi dispositivi hanno impedito alla maggior parte di noi di partecipare.



Oggi Canaan, uno dei principali produttori di macchine ASIC, ha deciso di affrontare il mercato dei privati che desiderano il Miner a casa, offrendo una gamma di prodotti relativamente silenziosi e molto facili da installare (plug & play).



Questi dispositivi sono commercializzati come riscaldatori ausiliari, nel caso dell'**Avalon Nano 3S (140W)**, o come mini-radiatori con una potenza di **800W** nel caso dell'**Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Si noti che la differenza di prezzo con i riscaldatori tradizionali di potenza equivalente non consente, nella stragrande maggioranza dei casi, di ottenere un profitto finanziario. I satoshi generati dall'attività del Mining non compenseranno mai questa differenza di prezzo, a meno che non si abbia accesso a elettricità gratuita (in eccesso) o molto economica.



A mio parere, questi dispositivi dovrebbero essere visti più come un modo semplice per fare Miner a casa per coloro che desiderano farlo per motivi personali: *ottenere un Satss non KYC / giocare alla "lotteria" con la solominazione / partecipare alla decentralizzazione del Hashrate ecc.*, beneficiando **come bonus** del calore generato per riscaldare la propria stanza in inverno. Ma non come un modo per risparmiare denaro, almeno nella maggior parte dei casi (paesi occidentali).



## Unboxing e caratteristiche



### Avalon Nano 3S



Per prima cosa, vediamo cosa c'è all'interno della scatola di Avalon Mini 3.



![image](assets/fr/24.webp)



Quando si apre la scatola, le istruzioni per l'uso sono direttamente di fronte a voi, ma soprattutto il modulo ricevitore WIFI è nascosto sotto l'adesivo bianco rotondo a sinistra delle istruzioni per l'uso. Ne avrete bisogno in seguito.



![image](assets/fr/25.webp)



Sotto il blocco di schiuma si trova il dispositivo e, una volta rimosso dalla scatola, l'unità Supply di potenza.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Accensione e connessione alla rete locale



Una volta disimballato, posizionare Avalon Mini 3 in un'area relativamente aperta, se possibile, per consentire al calore di circolare correttamente. Quindi iniziare a inserire il piccolo modulo ricevitore WIFI nella porta USB sul lato inferiore del dispositivo, collegare l'alimentazione Supply e assicurarsi che il pulsante di accensione sia in posizione "1".



![image](assets/fr/28.webp)



Una volta completati questi passaggi, il display a LED del dispositivo si accende e mostra il simbolo "Bluetooth", a indicare che il dispositivo è pronto per essere collegato alla rete locale tramite l'applicazione Avalon Family.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



A tal fine, accedere al negozio di applicazioni mobili, cercare e scaricare l'applicazione **Avalon Family**.



![image](assets/fr/11.webp)


Una volta installato, apritelo facendo clic su "Skip" nell'angolo in alto a destra, poi sul pulsante "Add" e infine su "Search". Assicuratevi che il Bluetooth sia abilitato sul vostro smartphone, in modo che il rilevamento del dispositivo avvenga senza problemi.



![image](assets/fr/12.webp)


Una volta che il dispositivo è stato rilevato dall'applicazione, fare clic su di esso e scegliere "Connetti". Verrà quindi visualizzata la schermata in cui inserire i dettagli della connessione WIFI.


![image](assets/fr/13.webp)


Una volta collegato alla rete locale, il Mini 3 visualizzerà informazioni quali IP Address, ora, Hashrate e potenza elettrica.



Di seguito viene riportata una tabella riassuntiva delle specifiche tecniche generali del Mini 3:




| Caratteristica                                      | Valore                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consumo di energia                              | 800 W                                                     |
| Rumore                                                | 35-55 dB                                                  |
| Temperatura aria in uscita                       | 60-70°C (a temperatura ambiente 25°C)                  |
| Requisiti di temperatura ambiente per l'uso | -5° C - 40°C                                              |
| Intervallo di tensione di ingresso del dispositivo                         | 110V-240V AC 50/60Hz                                      |
| Dimensioni della macchina                                 | Lunghezza: 760 mm / Profondità: 104 mm / Altezza: 214.5 mm |
| Peso della macchina                                  |  8.35 kg                                                  |

## Collegamento a un Mining pool



**Questa parte è comune ai dispositivi Nano 3 e Mini 3, in quanto i processi sono strettamente identici**



Sia che si voglia "solominare" sia che si voglia "mettere in comune" il Miner, è necessario collegarsi a un Mining pool. In effetti, il nostro dispositivo non è altro che un Hash-maker che non conosce la rete Bitcoin. La connessione a un pool gli dà accesso alla rete Bitcoin e gli consente di ricevere modelli di blocco su cui lavorare.



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



Per maggiori dettagli su come collegarsi a un Mining pool, consultare queste esercitazioni:



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



Nel menu principale dell'applicazione della famiglia Avalon, fare clic sull'icona corrispondente all'Avalon Mini 3. Si accede direttamente al menu per la gestione delle modalità operative.



sono disponibili 3 opzioni: modalità "Riscaldamento", "Mining" o "Notte".





- In modalità "Riscaldamento" sono disponibili 2 livelli di potenza "Eco" o "Super".


Il livello "Eco" corrisponde a una potenza di riscaldamento di 500 W per un Hashrate di circa 25 Th/s e 40 dB per il livello sonoro.


Il livello "Super" corrisponde a una potenza di uscita di 650 W a circa 30Th/s e 45 dB. Questa modalità consente di impostare una temperatura ambiente massima oltre la quale l'unità smette di funzionare.



![image](assets/fr/36.webp)




- In modalità "Mining", l'unità funziona alla massima velocità, senza la possibilità di impostare una temperatura target (a parte il limite di surriscaldamento incorporato, ovviamente). L'obiettivo è sfruttare al massimo le prestazioni del Miner. In questo caso, la potenza di uscita si avvicina a 800 W a circa 37,5 Th/s e un livello di rumore di 50-55 dB.



![image](assets/fr/37.webp)


Infine, in modalità "Night", il Mini 3 funziona alla velocità più bassa possibile con un rumore minimo. 400 W, 20 Th/s e circa 33 dB.



Anche in questo caso è possibile impostare una temperatura target al di sopra della quale l'unità passa in modalità inattiva e interrompe la Miner. Se la temperatura scende, l'unità si riavvia e riprende il riscaldamento e il Miner. In questa modalità, i LED del display sono spenti per impostazione predefinita, ma si può scegliere di accenderli se necessario per illuminare la stanza al buio, come una luce notturna (vedi foto sotto).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Infine, è possibile giocare con i LED dell'Avalon tramite il menu "Display". Si può scegliere di scorrere le informazioni operative pertinenti, di visualizzare l'ora o persino un'immagine personalizzata (pixelata).



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Come nel caso di Avalon Nano 3S, il menu "Impostazioni" consente di modificare la password dell'amministratore, le impostazioni della piscina, controllare l'ostruzione del filtro (situato sul lato inferiore del dispositivo), contattare l'assistenza o visualizzare i registri del dispositivo.



![image](assets/fr/42.webp)



Anche in questo caso, il filtro sul fondo dell'unità può essere pulito con un aspirapolvere, più regolarmente è meglio è.



Siamo giunti alla fine di questa esercitazione, che ci ha insegnato come collegare il nostro Avalon Mini 3 alla rete locale, come puntare il nostro Hashrate alle piscine Mining e come navigare tra le opzioni e le impostazioni utilizzando l'applicazione Avalon Family.



Per saperne di più, date un'occhiata al nostro tutorial sulla versione più piccola dell'Avalon: il Nano 3S.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6
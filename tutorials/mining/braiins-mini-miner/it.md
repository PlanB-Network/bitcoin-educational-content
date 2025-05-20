---
name: Mini Miner Braiins
description: Fare mining facilmente da casa.
---
![cover](assets/cover.webp)

### Introduzione

Il Mini Miner braiins BMM 100 è un prodotto creato dalla mining pool Braiins. Questo dispositivo ha un design accattivante ed è silenziosissimo. Produce 1,1 Th/s di potenza di calcolo e consuma circa 40 watt. A differenza di altri dispositivi non è open source, ma è veramente facile da installare, bastano veramente pochi click! Il Mini Miner BMM 100 è la prima versione uscita. Ora è in produzione la versione 2, chiamata BMM 101, che differisce dalla prima per il display più grosso e la presenza del Wi-Fi, ma le procedure di installazione sono le stesse.

Potete anche trovare molte altre informazioni importanti consultando la guida completa direttamente sul [sito del produttore](https://braiins.com/hardware/mini-miner-bmm-100).

### Panoramica del BMM 100

il dispositivo si presenta come un parallelepipedo con un display sulla parte anteriore

![image](assets/en/01.webp)

una ventola sul lato superiore

![image](assets/en/02.webp)

mentre sul lato posteriore abbiamo: il foro per la corrente, lo spazio per una scheda SD (che potrebbe servire per eventuali aggiornamenti), un tastino con scritto `IP REPORT` che permette di sapere l’indirizzo IP del mini miner, il quale indirizzo è necessario per accedere alla dashboard del dispositivo. Una volta premuto il tasto, l'indirizzo IP è visualizzato per circa 5 secondi, poi scompare e riappare la schermata impostata. Se però avete la necessità di cambiare alcune impostazioni, basta schiacciare nuovamente il tastino in questione per far comparire nuovamente a schermo l'indirizzo IP. Continuando con la lista troviamo una porta ethernet ed un accesso per eseguire il reset del dispositivo, per il quale sarà necessario prendere una spilletta e tenere premuto per 10 secondi al fine di azzerare tutte le impostazioni del mini miner. Infine troviamo due spie, una verde e una rossa che ci indicano lo stato del miner.

![image](assets/en/03.webp)

### Collegare il Mini Miner

Sarà necessario collegare il dispositivo ad internet via ethernet, da notare che con la nuova versione (BMM 101) questo non è piu necessario. Tornano a questo mini miner, una volta individuata la posizione dovremo collegarlo prima alla linea internet e poi alla corrente elettrica: il dispositivo si accenderà automaticamente e mostrerà sullo schermo il proprio indirizzo IP.

### Configurazione

Noi dobbiamo aprire un browser e inserire l’indirizzo IP che ci mostra il mini miner nella barra di ricerca. Vi ricordo che per trovare il dispositivo in rete dovrete essere in locale, quindi dovrete avere il computer che state utilizzando collegato alla stessa rete del mini miner. una volta inserito l’indirizzo IP premiamo invio e ci comparirà a schermo la pagina del login al sistema operativo del mini miner, che è Braiins OS.

![image](assets/en/06.webp)

Per poter accedere dovrete inserire come username `root`, mentre la password potete lasciarla vuota. Cliccate su login e vi comparirà la dashboard del vostro mini miner.

![image](assets/en/07.webp)

### Impostazioni generali

Andiamo su System

![image](assets/en/24.webp)

all'interno dei settings troviamo alcune impostazioni generali come il tema (chiaro o scuro), la lingua, il fuso orario e il cambio della password. 

![image](assets/en/25.webp)

Se andiamo in "Mini Miner Screen" invece abbiamo le impostazioni del nostro mini miner, come la visualizzazione dello schermo. Possiamo scegliere se mostrare l’ora, oppure il prezzo di bitcoin, o la schermata con le informazioni sullo stato della macchina come hashrare prodotto, temperatura, watt consumati, eccetera. Qui sta a voi scegliere cosa volete vedere a schermo; possiamo inoltre modificare la luminosità dello schermo, impostare la modalità notte e visualizzare l’orario con il formato a 12 ore o a 24 ore. 

![image](assets/en/26.webp)

Una volta effettuati dei cambiamenti, cliccate su `Save Changes` e vedrete le modifiche sul vostro schermo del dispositivo

![image](assets/en/27.webp)

### Collegamento alla mining pool

Ora non siamo ancora operativi, perché dobbiamo collegarci ad una pool per poter iniziare a minare, quindi dobbiamo andare in “Configuration”

![image](assets/en/08.webp)

e la prima voce è proprio `Pools`.

![image](assets/en/09.webp)

Qui dovremo decidere che pool utilizzare. In questo tutorial vi mostrerò due opzioni. La prima è collegarci alla mining pool Braiins che è utilizzata anche dai miners professionali, come si vede da questa guida:

https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

La seconda opzione è collegarci ad una mining pool che mina in solo, come Public Pool, segui questa guida per farlo:

https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

#### Braiins pool

Per collegarsi a questa pool è necessario creare un account. questa pool effettua anche pagamenti utilizzando il Lightning Network, quindi potremo ricevere qualche sats al giorno. Per farlo dobbiamo impostare un lightning address sul quale ricevere le ricompense. Se non sai come creare un account su braiins pool o come impostare il tuo lightning address puoi seguire questa guida:

https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Una volta fatto ci troviamo nella dashboard di Braiins pool. Quello che dobbiamo fare noi e dire alla pool che ci vogliamo connettere con un nostro miner, quindi sulla sinistra dello schermo trovate una serie di voci. Noi dobbiamo andare su “workers”:

![image](assets/en/04.webp)

e dobbiamo cliccare sul bottone viola sulla destra con scritto “Connect workers”.

![image](assets/en/05.webp)

Ecco che si apre la finestra con le informazioni che ci servono per connettere il nostro mini miner alla pool. Qui l’unica modifica che possiamo fare è quella di scegliere Stratum V2. Per sapere che cosa sia Stratum v2 consulta questa voce del [glossario](https://planb.network/en/resources/glossary/stratum-v2).

![image](assets/en/10.webp)

Ora noi dobbiamo copiare questa stringa che inizia per stratumv2. Clicchiamo quindi sul simbolino “copia”, poi andiamo sulla dashboard del nostro mini miner che avevamo lasciato in configurazione e pools. Clicchiamo su add new pool

![image](assets/en/11.webp)

e incolliamo la stringa che abbiamo copiato nello spazio sotto a Pool URL.

![image](assets/en/12.webp)

Ora dobbiamo aggiungere username e password. Torniamo nella dashboad della pool. Sotto abbiamo anche un userID e una password. Lo userID e il nostro username, quello che abbiamo dato in fase di creazione dell’account, più il nome del miner che vogliamo inserire. si può decidere se dare un nome oppure no al dispositivo che state collegando alla pool, è opzionale, ma è consigliabile metterlo, cosi se si collegano più dispositivi sarà più facile identificarli subito. Se invece non si vuole mettere niente si può lasciare `workerName`. 

![image](assets/en/13.webp)

Andiamo quindi sul nostro mini miner e inseriamo lo username. Qui inseriremo nel mio caso “finalstepbitcoin” che è il mio userID, punto miniminer. Questo è il nome che ho deciso di dare al dispositivo. Se non lo si vuole nominare basta scrivere userid punto workername. Nel mio caso sarebbe stato finalstepbitcoin.workername. Una volta inserito lo username si può scegliete una password e scriverla nel campo vuoto. Si può anche mettere anithing123, che è quella riportata anche nella schermata della pool, ma vuole semplicemente indicare che si può mettere la password che si vuole. 

Una volta inseriti tutti i dati bisogna premere sul tasto salva sulla destra (quello a forma di floppy disk) e in questo modo sono stati configurati i dati della pool nel mini miner. 

![image](assets/en/14.webp)

Ora bisogna tornare sulla dashboard della pool e cliccare su "Connected! Go back".

![image](assets/en/15.webp)

Abbiamo collegato il nostro mini miner alla pool di braiins! Ora è possibile vederlo nella lista dei workers. Se non si dovesse vedere basta fare un refresh e attendere qualche istante. Una volta comparso, verificare che abbia lo status "OK" con la spunta verde.

![image](assets/en/17.webp)

se si torna sulla dashboard si dovrebbe cominciare a vedere del movimento sul grafico e vedere l’hashrate del nostro dispositivo. Questo significa che la pool sta ricevendo il nostro lavoro e quindi stiamo a tutti gli effetti minando.

![image](assets/en/16.webp)

#### Public Pool

Attraverso questa pool si può tentare la fortuna e minare in solo, appoggiandosi ad una pool. In questo caso non riceveremo reward, ma riceveremo l’intera ricompensa se mai riusciremo a minare un blocco. Ci collegheremo quindi a public pool, una pool per solo mining completamente open source. Apriamo una nuova finestra sul browser e andiamo su [web.public-pool.io](https://web.public-pool.io/#/).

![image](assets/en/18.webp)

ecco che si apre una pagina con tutte le informazioni di cui abbiamo bisogno. Ci copiamo quindi l’indirizzo stratum

![image](assets/en/19.webp)

poi torniamo sulla dashboard del nostro mini miner, andiamo su configuration e su pools, clicchiamo su add new pool (stesso procedimento visto in precedenza) e incolliamo l’ indirizzo stratum sotto a pool url.

![image](assets/en/20.webp)

Ora torniamo sulla pagina della pool e vediamo che come username dobbiamo inserire un indirizzo bitcoin, che sarà quello sulla quale riceveremo la reward nel caso minassimo un blocco, poi un punto e poi il nome del nostro dispositivo, come abbiamo fatto in precedenza con Braiins Pool, mentre la password possiamo sceglierla noi.

![image](assets/en/21.webp)

Torniamo sul mini miner e sotto username incolliamo un indirizzo bitcoin seguito da punto e il nome, io metto `miniminer`. Nella password invece io metterò test, voi inserite quella che volete. 

![image](assets/en/22.webp)

Ora salviamo le impostazioni e disabilitiamo la pool di Braiins. 

![image](assets/en/23.webp)

Bene! Ora stiamo minando su public pool!

![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)

---
name: Electrum Airgap
description: Un primo passo verso la sicurezza, un cold wallet con Electrum
---
![cover](assets/cover.webp)

## Cold Wallet

In questo tutorial ti spiegherò come realizzare il tuo primo dispositivo di firma airgap, disconnesso dalla rete Internet, anche senza avere un hardware wallet dedicato. Tutto ciò che ti serve è avere a disposizione due computer:
- un vecchio dispositivo a cui impedire per sempre la connessione a Internet;
- il tuo computer di uso quotidiano.

Questa configurazione permette di ottenere un grado di sicurezza maggiore rispetto al classico `hot wallet`: il vecchio computer - senza connessione alla rete - è il custode delle tue chiavi private, che non sono mai esposte su internet, ma conservate offline ("airgap" o "cold").

Sul tuo computer quotidiano installerai invece un wallet di visualizzazione ("watch-only"), connesso alla rete e con cui potrai, ad esempio, controllare il saldo e preparare le transazioni di ricezione.

## Wallet Airgap: Cosa e Come

Eseguendo i passi di questa guida, installeremo due software wallet Electrum sui due diversi computer e, infine, creeremo due wallet con keystore differenti: il wallet airgap userà tutta la gerarchia del wallet HD, mentre il wallet di visualizzazione sarà generato con la chiave pubblica master.

Questi due wallet saranno, in tutto e per tutto, molto diversi tra loro. L'unica cosa che avranno in comune, come vedremo, sono gli indirizzi:
- il wallet sul computer airgap può solo firmare ma, disconnesso dalla rete, non conosce il saldo e gli indirizzi usati;
- il wallet sul computer quotidiano potrà solo preparare e propagare le transazioni, senza poterne disporre la spesa, in mancanza delle chiavi private.

## Preparazione Preliminare

Per scaricare Electrum, ti consiglio di seguire i primi passi di questo tutorial:

https://planb.network/it/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Dopo il download verifica sempre la release prima di installarla, poi procedi alla configurazione "One Server", come troverai nella sezione della guida, al capitolo `Inizia con un wallet fittizio`.

L'operazione di configurazione "One Server" è necessaria solo per il wallet installato sul computer quotidiano, in quanto l'altro computer sarà sempre offline.

Le operazioni che seguono prevedono di praticare su due computer (e wallet) diversi, pertanto - per praticità e messa a fuoco - ho scelto di impostare il wallet airgap con il tema chiaro, mentre il wallet di visualizzazione ha il tema scuro.

## Creazione Wallet Airgap

Dopo aver scaricato e verificato il download di Electrum, prendi una copia dell'eseguibile e portala sul computer offline. Quindi lancialo e installa Electrum.

Con il doppio click fai partire Electrum: il computer dove userai questo wallet è offline, ignora le impostazioni di rete e vai alla creazione del wallet che, in questa guida, chiameremo `airgap`.

![image](assets/en/01.webp)

Scegliere _Standard wallet_.

![image](assets/en/02.webp)

E selezionare poi _Create a new seed_ per fare generare la mnemonica dal software.

![image](assets/en/03.webp)

Trascrivi accuratamente le 12 parole generate da Electrum su un supporto di carta e procedi con la fase di verifica, reimmettendo le parole in ordine, quando Electrum lo richiede.

![image](assets/en/04.webp)

![image](assets/en/05.webp)

Al termine della creazione del wallet, imposta una password complessa (`Strong`) per cifrare il file del wallet sul dispositivo airgap. Questo passaggio è molto delicato e importante, in quanto la password scelta adesso, impedisce l'accesso al wallet che ha facoltà dispositiva, potendo spendere i fondi firmare le transazioni.

![image](assets/en/06.webp)

Cliccando _Finish_ il wallet è definito ed appare sullo schermo. Naturalmente l'indicatore della connessione di rete, ovvero il pallino colorato in basso a destra, è di colore rosso, in quanto il computer è disconnesso e non permette al wallet di esporre le chiavi online.

![image](assets/en/07.webp)

## Creazione Wallet di Visualizzazione

Ora che il tuo wallet ha le chiavi private offline, devi predisporre un wallet di visualizzazione, o `watch-only`, che ti permetterà di visualizzare il saldo, così come preparare transazioni di ricezione per continuare ad accumulare sats in sicurezza.

Dal wallet che si trova sul dispositivo offline, scegli il menu _Wallet_ -> _Information_

![image](assets/en/08.webp)

Apparirà la finestra che contiene tutte le informazioni del tuo wallet, dove potrai controllare `derivation path` e `master fingerprint`, ad esempio per segnarle vicino alle parole della frase mnemonica (fortemente consigliato).

![image](assets/en/09.webp)

Ricorda che prelevi questo dato da un computer non connesso, quindi dovrai copiare/incollare la `zpub` su un file di testo e salvarlo su una chiavetta usb. 

Ora puoi spostarti sul computer connesso a internet, per lanciare Electrum e creare un nuovo wallet.

Dal menu _File_ scegli _New/Restore_.

![image](assets/en/10.webp)

Il nuovo wallet è di sola visualizzazione, per questa guida lo chiameremo `watch-only`.

![image](assets/en/12.webp)

Nella schermata successiva scegli _Standard wallet_ e procedi cliccando _Next_.

![image](assets/en/13.webp)

Nella scelta del `Keystore` fai attenzione: per creare il wallet di visualizzazione seleziona _Use a master key_. Procedi poi con _Next_.

![image](assets/en/14.webp)

Incolla qui la `zpub` copiata dal wallet offline e che hai portato su questo computer tramite supporto usb.

![image](assets/en/15.webp)

Concludi impostando una password robusta anche per questo wallet, possibilmente diversa da quella scelta per il suo corrispondente cold.

Ti comparirà il wallet di visualizzazione, con un warning. Il messaggio ti ricorda che questo è un wallet di sola visualizzazione e che non è possibile, con esso, spendere i fondi associati.

**Nota Bene**: **sarà pertanto necessario possedere sempre le chiavi private per disporre degli UTXO di questo wallet**. Con un buon sistema di backup, non ti sarà difficile rimanere nel pieno possesso dei tuoi bitcoin.

![image](assets/en/16.webp)

Questo warning apparirà ogni singola volta che apri questo wallet. Clicca su _Ok_ e passiamo alla fase di verifica.

## Verifica dei Due Wallet

Come abbiamo imparato all'inizio di questa guida, un wallet airgap e il suo wallet di visualizzazione sono due portafogli che hanno facoltà diverse, ma che **condividono gli stessi indirizzi**.

Se guardiamo i due wallet, uno accanto all'altro, visivamente notiamo che nel wallet airgap è presente il simbolo del "seed", mentre nel watch-only no. Anche questo particolare ti aiuterà a ricordare che il wallet di visualizzazione non ha le chiavi private.

![image](assets/en/17.webp)

Per fare una prima verifica accurata, però, seleziona in entrambi i wallet il menu `Addresses`: condividendo gli stessi indirizzi, la lista di questi ultimi deve essere identica per entrambi.

![image](assets/en/18.webp)

⚠️ **ATTENZIONE**: **non ci possono essere vie di mezzo, gli indirizzi devono essere gli stessi. In caso fossero diversi, è necessario eliminare tutto il lavoro fin qui fatto e ricominciare da capo**.

Ora si può procedere a fare due verifiche differenti. Prima di tutto, provare a cancellare i due wallet e ripristinarli da capo, ognuno sul computer apposito. In caso si proceda a fare questa verifica, per il wallet di visualizzazione le procedure sono identiche a quelle esposte in precedenza.

Per il wallet airgap, invece, nella schermata del `keystore` dovrai scegliere _I already have a seed_ e immettere le parole copiandole dal tuo backup cartaceo.

Finita la prova "a vuoto", puoi provare a fare una transazione di un importo piccolo e spenderla immediatamente. 

## Transazioni di Ricezione e Spesa

Per iniziare ad usare il tuo Electrum airgap, puoi fare una transazione di ricezione con un piccolo importo, per poi spenderla verso un tuo indirizzo. Potrai così familiarizzare con la procedura, verificando di avere il pieno controllo dei fondi.

**Nota**: ti sconsiglio di depositare sul wallet un ingente quantitativo di fondi, prima di avere la certezza di poter svolgere tutte le operazioni agevolmente.

Le operazioni spiegate di seguito possono, a prima vista, sembrarti complicate. Non farti abbattere: quando avrai fatto la prima prova, scoprirai che richiedono solo pochissimi minuti per essere completate.

Per ricevere fondi, devi necessariamente utilizzare il wallet di visualizzazione che si trova sul tuo computer connesso alla rete Internet. Dal menu `Receive` clicca su _Create request_ per far generare ad Electrum il primo indirizzo disponibile e usalo per mandarci pochi sats.

![image](assets/en/19.webp)

![image](assets/en/20.webp)

Una volta propagata la transazione puoi già notare che - come è naturale che sia - la stessa è visibile solo sul wallet di visualizzazione e non sul wallet airgap.

![image](assets/en/21.webp)

Dopo che la tua transazione ha ricevuto qualche conferma, puoi preparare la spesa e provare così la procedura di firma dal wallet fuori rete. Prepara quindi la transazione sul watch-only e premi _Preview_ per controllarla

![image](assets/en/22.webp)

Ti compare la finestra di transazione avanzata dove puoi notare che:
- la transazione non è firmata (`Status: Unsigned);
- i comandi `Sign` e `Broadcast` sono inibiti.

L'unica cosa che puoi fare è esportare la transazione così com'è, per portarla sul wallet airgap e firmarla.

Introduci una chiavetta USB nel tuo computer e, dal menu in basso a sinistra, scegli _Share_.

![image](assets/en/23.webp)

Dopodiché seleziona _Save to file_.

![image](assets/en/24.webp)

Salva la transazione sulla chiavetta usb.

Noterai che Electrum da al file un nome che riporta le prime cifre del transaction ID e l'estensione del file è `.psbt`, che significa `Partially Signed Bitcoin Transaction`.

Estrai il supporto con il file `.psbt` e collegalo al computer offline.

Dal wallet airgap, scegli ora il menu _Tools_, poi _Load transaction_ e di seguito From file_.

![image](assets/en/25.webp)

Con il file manager scegli il `.psbt` dalla sua posizione.

![image](assets/en/29.webp)

Il software del computer fuori rete aprirà in automatico la finestra di transazione avanzata, del tutto identica a come l'hai vista sul wallet di visualizzazione. Lo status è `Unsigned`, ma la differenza è che il comando `Sign` qui è attivo. Ed è precisamente quello che dovrai eseguire.

![image](assets/en/26.webp)

![image](assets/en/27.webp)

Ora che la transazione è firmata, ricordati che il tuo wallet è su una macchina offline. Pertanto - anche se vedi attivo il comando `Broadcast` - il tuo wallet non sarà in grado di propagare la transazione verso la rete Bitcoin.

Quello che devi fare ora è ripetere l'operazione di esportazione della transazione firmata sulla chiavetta usb, in modo da importarla su un computer connesso a internet e propagarla.

Dal menu in basso a sinistra, scegli di nuovo _Share_  e poi _Save to file_.

![image](assets/en/28.webp)

Ora il file ha un'altra estensione: **anziché `.psbt` ora la transazione ha estensione `.txn`. D'ora in avanti è così che Electrum ti farà riconoscere le transazioni firmate da quelle non firmate**.

![image](assets/en/30.webp)

Per la definitiva propagazione della transazione, estrai la chiavetta usb dal computer fuori rete e inseriscila nel computer connesso a Internet.

Dal watch-only, ripeti la procedura di importazione, ovvero dal menu _Tools_ seleziona _Load transaction_ e infine _From file_.

![image](assets/en/31.webp)

Electrum ti aprirà la finestra di transazione, decisamente diversa da quella mostrata in precedenza su questo wallet, in quanto ora è firmata (`Status: Signed`) e il comando `Broadcast` accessibile.

L'ultima operazione che devi fare è proprio questa:

![image](assets/en/32.webp)

## Conclusioni

I tuoi test sono ora terminati. Se hai seguito la guida e hai ottenuto gli stessi risultati, hai creato un wallet cold con Electrum, su due computer differenti, che potrai usare in maniera airgap per conservare i tuoi bitcoin.

Le uniche cose a cui dovrai prestare la massima attenzione sono due:
1) **non usare mai il wallet airgap per generare indirizzi di ricezione**. Essendo offline, ti proporrà sempre il primo indirizzo, che coincide con quello che hai appena usato per fare la transazione di test;

![image](assets/en/33.webp)

_Come puoi notare dall'immagine sopra, il wallet offline non conosce la storia dei propri indirizzi. È totalmente cieco da questo punto di vista. **L'unico compito che può svolgere per te, è conservare le chiavi offline e firmare le tue transazioni**_.

2) Usare una chiavetta USB dedicata solo a questo scopo, **non utilizzare un supporto che usi frequentemente**. Gli strumenti di uso quotidiano hanno più probabilità di subire un attacco informatico e, non volendo, potresti attaccare anche il computer che stai tenendo scollegato dalla rete. Una chiavetta USB che usi solo per questo scopo ha pochissime occasioni per entrare in contatto con il tuo PC online, specie se sei un hodler che non deve spendere, riducendo così la probabilità di ricevere e poi trasmettere virus, malware ecc.

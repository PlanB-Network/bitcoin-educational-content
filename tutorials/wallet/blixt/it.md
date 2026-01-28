---
name: Blixt Wallet
description: Come iniziare a utilizzare un potente nodo LN sul cellulare?
---
![cover](assets/cover.webp)


Questa guida è dedicata a tutti i nuovi utenti che desiderano iniziare a utilizzare Bitcoin Lightning Network (LN) in modo GRATUITO, OPEN SOURCE e COMPLETAMENTE NON COSTOSO.


Utilizzando [Blixt Wallet](https://blixtwallet.com/), un nodo LN completo sul vostro cellulare, ovunque voi siate.


Se non avete mai usato il Bitcoin Lightning Network, prima di iniziare [leggete questa semplice spiegazione analogica sul Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## ASPETTI IMPORTANTI:



- Blixt è un nodo privato, NON un nodo di routing! Tenetelo a mente: ciò significa che tutti i canali LN in Blixt non saranno annunciati al grafico LN (i cosiddetti canali privati). Ciò significa che questo nodo non effettuerà l'instradamento di altri pagamenti attraverso il nodo Blixt. Questo nodo Blixt NON è per il routing, ripeto. Serve principalmente per poter gestire i propri canali LN ed effettuare i pagamenti LN privatamente, ogni volta che se ne ha bisogno. Questo nodo Blixt deve essere online e sincronizzato SOLO PRIMA di effettuare le transazioni. Ecco perché vedrete un'icona in alto che indica lo stato di sincronizzazione. Ci vogliono solo pochi istanti, a seconda del tempo in cui lo si è tenuto offline.



- Blixt utilizza LND (aezeed) come backend Wallet, quindi non cercare di importare altri tipi di portafogli Bitcoin in esso. [Qui sono spiegati i tipi di semi Wallet Mnemonic](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Ed ecco [un elenco più esteso di tutti i tipi di portafogli](https://walletsrecovery.org/). Quindi, se in precedenza avevate un nodo LND, potete importare il seed e i canali di backup in Blixt, [come spiegato in questa guida](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Alla fine di questa guida troverete una sezione speciale con ["consigli e trucchi"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- I link più importanti sono riportati alla fine di questa guida e vanno inseriti tra i preferiti.


---

## Blixt - Primo contatto


Quindi... la mamma di Darth ha deciso di iniziare a usare il LN con Blixt. Una decisione da Hard, ma saggia. Blixt è solo per le persone intelligenti e per coloro che vogliono davvero imparare di più, l'uso profondo di LN.


![blixt](assets/en/01.webp)


Darth avverte sua madre:


"*Mamma, se inizi a usare il nodo Blixt LN, devi prima sapere cos'è il Lightning Network e come funziona, almeno a livello di base. [Qui ho messo insieme un semplice elenco di risorse sul Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Si prega di leggerle prima.*"


La mamma di Darth ha letto le risorse e ha fatto il suo primo passo: installare Blixt sul suo nuovo dispositivo Android. Blixt è disponibile anche per iOS e macOS (desktop). Tuttavia, si consiglia di utilizzare una versione più recente di Android, almeno la 9 o la 10, per una migliore compatibilità ed esperienza. L'esecuzione di un nodo LN completo su un dispositivo mobile non è un compito facile e potrebbe richiedere un po' di spazio (almeno 600 MB) e di memoria.


Una volta aperto Blixt, la schermata di "benvenuto" vi darà alcune opzioni:


![blixt](assets/en/02.webp)


Nell'angolo in alto a destra sono presenti 3 puntini che attivano un menu con:



- "enable Tor" - l'utente può iniziare con la rete Tor, in particolare se vuole ripristinare un vecchio nodo LND che funzionava solo con peer Tor.
- "Imposta nodo Bitcoin": se l'utente desidera connettersi direttamente al proprio nodo, per sincronizzare i blocchi attraverso Neutrino, può farlo direttamente dalla schermata di benvenuto. Questa opzione è utile anche nel caso in cui la connessione a Internet o a Tor non sia stabile per connettersi al nodo Bitcoin predefinito (node.blixtwallet.com).
- Presto verrà aggiunta la lingua, in modo che l'utente possa iniziare subito con la lingua che gli è più congeniale. Se volete contribuire a questo progetto open source con traduzioni in altre lingue, [unitevi qui](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### OPZIONE A - Creare un nuovo Wallet


Se si sceglie di "creare un nuovo Wallet", si verrà reindirizzati direttamente alla schermata principale del Blixt Wallet.


Questo è il vostro "cockpit" ed è anche il "Main LN Wallet", quindi sappiate che vi mostrerà solo l'equilibrio del vostro LN Wallet. Il Wallet di riserva viene visualizzato separatamente (vedere C).


![blixt](assets/en/03.webp)


A - Icona dell'indicatore di sincronizzazione dei blocchi Blixt. È la cosa più importante per un nodo LN: essere sincronizzato con la rete. Se l'icona è ancora attiva, significa che il nodo non è pronto! Quindi abbiate pazienza, soprattutto per la prima sincronizzazione iniziale. Potrebbero essere necessari fino a 6-8 minuti, a seconda del dispositivo e della connessione a Internet.


È possibile fare clic su di esso e vedere lo stato della sincronizzazione:


![blixt](assets/en/04.webp)


È inoltre possibile fare clic sul pulsante "Mostra registro LND" (A) se si desidera visualizzare e leggere ulteriori dettagli tecnici del registro LND, in tempo reale. È molto utile per il debug e per imparare meglio il funzionamento del LN.


B - Qui è possibile accedere a tutte le impostazioni di Blixt, e sono molte! Blixt offre molte funzioni e opzioni per gestire il vostro nodo LN come un professionista. Tutte queste opzioni sono spiegate in dettaglio nella sezione "[Blixt Features Page](https://blixtwallet.github.io/features#blixt-options) - Options Menu".


C - Qui c'è il menu "Magic Drawer", [spiegato in dettaglio anche qui](https://blixtwallet.github.io/features#blixt-drawer). Qui si trovano i canali "Onchain Wallet" (B), Lightning Channels (C), Contatti, icona di stato dei canali (A), Keysend (D).


![blixt](assets/en/05.webp)


D - È il menu di aiuto, con collegamenti alla pagina delle FAQ/Guide, al contatto con lo sviluppatore, alla pagina Github e al gruppo di supporto Telegram.


E - Indica il tuo primo BTC Address, dove puoi depositare il tuo primo test Sats. QUESTO È FACOLTATIVO! Se si deposita direttamente in quel Address, si apre un canale LN verso il nodo Blixt. Ciò significa che vedrete il vostro Sats depositato andare in un'altra transazione onchain (tx), per aprire quel canale LN. È possibile verificarlo nella catena Blixt onchain Wallet (vedi punto C), cliccando sul menu TX in alto a destra.


![blixt](assets/en/06.webp)


Come si può vedere nel registro delle transazioni di Onchain, i passaggi sono molto dettagliati e indicano la destinazione dei Sats (deposito, apertura, chiusura del canale).


RACCOMANDAZIONE:


Dopo aver testato diverse situazioni, siamo arrivati alla conclusione che è molto più efficiente aprire canali tra 1 e 5 M Sats. I canali più piccoli tendono a esaurirsi rapidamente e a pagare una percentuale più alta di canoni rispetto ai canali più grandi.


F - Indica il saldo principale del Lightning Wallet. Questo NON è il saldo totale del Wallet di Blixt, ma rappresenta solo il Sats che avete nei canali Lightning, disponibile per l'invio. Come indicato in precedenza, il Wallet Onchain è separato. Tenete presente questo aspetto. Il Wallet onchain è separato per un motivo importante: è usato principalmente per aprire/chiudere i canali LN.


Ok, ora la mamma di Darth ha depositato un po' di Sats nella Address onchain visualizzata nella schermata principale. Si raccomanda di mantenere l'applicazione Blixt online e attiva per un po' di tempo, fino a quando i minatori non avranno prelevato il BTC nel primo blocco.


Dopo di che potrebbero volerci fino a 20-30 minuti prima che il canale sia completamente confermato e aperto e lo vedrete nel Magic Drawer - Lightning Channels come attivo. Anche il piccolo punto colorato in cima al cassetto, se si tratta di Green, indicherà che il vostro canale LN è online e pronto per essere usato per inviare Sats su LN.


Il Address e il messaggio di benvenuto visualizzato scompariranno. Non è più necessario aprire un canale automatico. È possibile disattivare l'opzione nel menu Impostazioni.


È il momento di andare avanti, testando altre funzioni e opzioni per aprire i canali LN.


Ora, apriamo un altro canale con un altro nodo peer. La comunità di Blixt ha messo insieme [un elenco di buoni nodi da iniziare a usare con Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Procedura per aprire un canale LN in Blixt**


Si tratta di un'operazione molto semplice, che richiede solo alcuni passaggi e un po' di pazienza:



- Inserito nell'elenco dei pari della [Blixt Community](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- Selezionare un nodo e fare clic sul link del titolo del nome, per aprire la pagina di Amboss
- Fare clic per visualizzare il codice QR per il nodo URI Address


![blixt](assets/en/07.webp)


Aprite Blixt e andate nel cassetto superiore - Canali Lightning e fate clic sul pulsante "+"


![blixt](assets/en/08.webp)


A questo punto, fare clic sulla telecamera (A) per scansionare il codice QR dalla pagina di Amboss e i dettagli del nodo verranno compilati. Aggiungere l'importo del Sats per il canale desiderato e selezionare la tariffa per la trasmissione. È possibile lasciare il valore automatico (B) per una conferma più rapida o regolarlo manualmente facendo scorrere il pulsante. È anche possibile premere a lungo il numero e modificarlo a piacimento.


Non mettere meno di 1 sat/vbyte! Di solito è meglio consultare le [Tariffe Mempool](https://Mempool.space/) prima di aprire un canale e selezionare una tariffa conveniente.


Fatto, ora basta cliccare sul pulsante "apri canale" e attendere 3 conferme, che di solito richiedono 30 minuti (1 blocco circa ogni 10 minuti).


Una volta confermato, il canale sarà attivo nella sezione "Canali Lightning".


---

## Blixt - Secondo contatto


Ok, ora abbiamo un canale LN con solo liquidità OUTBOUND. Ciò significa che possiamo solo INVIARE, non possiamo ancora RICEVERE Sats su LN.


![blixt](assets/en/09.webp)


Perché? Avete letto le guide indicate all'inizio? No? Tornate indietro e leggetele. È molto importante capire come funzionano i canali LN.


![blixt](assets/en/10.webp)


Come si può vedere in questo esempio, il canale aperto con il primo deposito non ha troppa liquidità INBOUND ("Può ricevere") ma ha molta liquidità OUTBOUND ("Può inviare").


Quali opzioni avete quindi se volete ricevere più Sats che LN?



- Spendere un po' di Sats dal canale esistente. Sì, LN è una rete di pagamento di Bitcoin, utilizzata principalmente per spendere il proprio Sats in modo più veloce, economico, privato e semplice. Il LN NON è un modo per fare hodling, per quello c'è il Wallet onchain.



- Scambiate un po' di Sats con il vostro Wallet onchain, utilizzando un servizio di scambio sottomarino. In questo modo non si spende il proprio Sats, ma lo si restituisce al proprio Wallet onchain. Qui potete vedere in dettaglio alcuni metodi, nella [Pagina delle guide Blixt](https://blixtwallet.github.io/guides).



- Aprire un canale INBOUND da qualsiasi provider LSP. Ecco un video dimostrativo su come utilizzare LNBig LSP per aprire un canale inbound. Ciò significa che pagherete una piccola tassa per un canale VUOTO (da parte vostra) e potrete ricevere più Sats in quel canale. Se siete un commerciante che riceve più di quanto spende, questa è una buona opzione. Inoltre, se state acquistando Sats su LN, utilizzando Robosats o qualsiasi altro LN Exchange.



- Aprite un canale Dunder, con il nodo Blixt o qualsiasi altro fornitore di LSP Dunder. Un canale Dunder è un modo semplice per ottenere un po' di liquidità INBOUND, ma allo stesso tempo per depositare un po' di Sats in quel canale. È anche buono perché aprirà il canale con un [UTXO](https://en.Bitcoin.it/wiki/UTXO) che non proviene dal tuo Wallet Blixt. Questo aggiunge un po' di privacy. È anche buono perché, se non avete Sats in un Wallet onchain, per aprire un normale canale LN, ma li avete in un altro LN Wallet, potete semplicemente pagare da quell'altro Wallet attraverso LN l'apertura e il deposito (da parte vostra) di quel canale Dunder. [Maggiori dettagli su come funziona Dunder e su come gestire il proprio server qui](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Ecco i passaggi per attivare l'apertura di un canale Dunder:



- Andare in Impostazioni, nella sezione "Esperimenti" attivare la casella "Abilita Dunder LSP".
- Una volta fatto questo, tornate alla sezione "Lightning Network" e vedrete che è apparsa l'opzione "Imposta server LSP Dunder". Lì, per impostazione predefinita, è impostato "https://dunder.blixtwallet.com", ma è possibile cambiarlo con qualsiasi altro provider Dunder LSP Address. [Ecco un elenco della comunità Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) con i nodi che possono fornire canali LSP Dudner per il vostro Blixt.
- A questo punto è possibile accedere alla schermata principale e fare clic sul pulsante "Ricevi". Seguite quindi questa procedura [spiegata in questa guida](https://blixtwallet.github.io/guides#guide-lsp).


OK, quindi dopo la conferma del canale Dunder (ci vorranno alcuni minuti) vi ritroverete con 2 canali LN: uno aperto inizialmente con l'autopilota (canale A) e uno con più liquidità in entrata, aperto con Dunder (canale B).


![blixt](assets/en/12.webp)


Bene, ora siete pronti per inviare e ricevere abbastanza Sats su LN!


FELICE FULMINE Bitcoin!


---

## Blixt - Terzo contatto


Ricordate che nel primo capitolo "Primo contatto" c'erano due opzioni nella schermata di benvenuto:


- [Opzione A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Creare un nuovo Wallet
- Opzione B - Ripristino del Wallet


Ora parliamo di come ripristinare un nodo Blixt Wallet o qualsiasi altro nodo LND in crash. Si tratta di un'operazione un po' più tecnica, ma prestate attenzione. Non è che Hard.


### OPZIONE B - Ripristino del Wallet


In passato ho scritto una guida dedicata a [come ripristinare un nodo Umbrel in crash](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), in cui ho menzionato anche il metodo di utilizzo di Blixt come processo di ripristino rapido, utilizzando il file seed + channel.backup di Umbrel.


Ho anche scritto una guida su come ripristinare il vostro nodo Blixt o migrare il vostro Blixt su un altro dispositivo, [qui](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Ma spieghiamo in modo semplice questo processo. Come si può vedere nell'immagine qui sopra, ci sono due cose da fare per ripristinare il nodo Blixt/LND precedente:



- il riquadro in alto deve essere riempito con tutte le 24 parole del seed (nodo vecchio/morto)
- in basso ci sono due opzioni di pulsanti per inserire/caricare il file channel.backup, precedentemente salvato dal vecchio nodo Blixt/LND. Può trattarsi di un file locale (caricato in precedenza sul dispositivo) o di una posizione remota di Google Drive / iCloud. Blixt dispone di un'opzione per salvare il backup dei canali direttamente in un'unità Google / iCloud. Per maggiori dettagli, consultare la pagina [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).


Tuttavia, se in precedenza non avevate alcun canale LN aperto, non è necessario caricare alcun file channels.backup. È sufficiente inserire le 24 parole seed e premere il pulsante di ripristino.


Non dimenticare di attivare Tor, dal menu a 3 punti in alto, come abbiamo spiegato nella sezione Opzione A. Questo è il caso in cui si hanno SOLO peer Tor e non si può essere contattati tramite clearnet (dominio/IP). Altrimenti non è necessario.


Un'altra funzione utile è quella di impostare uno specifico nodo Bitcoin dal menu superiore. Per impostazione predefinita sincronizza i blocchi da node.blixtwallet.com (modalità neutrino), ma è possibile impostare qualsiasi altro nodo Bitcoin che fornisca la sincronizzazione neutrino.


Una volta compilate queste opzioni e premuto il pulsante di ripristino, Blixt inizierà a sincronizzare i blocchi attraverso Neutrino, come abbiamo spiegato nel capitolo Primo contatto. Quindi, siate pazienti e osservate il processo di ripristino nella schermata principale, facendo clic sull'icona di sincronizzazione.


![blixt](assets/en/14.webp)


Come si può vedere in questo esempio, mostra che i blocchi Bitcoin sono sincronizzati al 100% (A) e il processo di recupero è in corso (B). Ciò significa che i canali LN che avevate in precedenza verranno chiusi e i fondi ripristinati nella vostra Blixt onchain Wallet.


Questo processo richiede tempo! Quindi, siate pazienti e cercate di mantenere il vostro Blixt attivo e online. La sincronizzazione iniziale potrebbe richiedere fino a 6-8 minuti e la chiusura dei canali potrebbe richiedere fino a 10-15 minuti. Quindi è meglio che il dispositivo sia ben carico.


Una volta avviato questo processo, si può controllare nel Magic Drawer - Lightning Channels lo stato di ciascuno dei canali precedenti, mostrando che sono in stato di "pending to close". Una volta chiuso ogni canale, si può vedere il tx di chiusura nel Wallet onchain (vedere Magic Drawer - Onchain) e aprire il registro del menu tx.


![blixt](assets/en/15.webp)


Inoltre, è bene controllare e aggiungere, se non ci sono, i peer precedentemente presenti nel vecchio nodo LN. Andate quindi al menu Impostazioni, scendete a "Lightning Network" e inserite l'opzione "Mostra peer fulminei".


![blixt](assets/en/16.webp)


All'interno della sezione verranno visualizzati i peer a cui si è connessi in quel momento e se ne possono aggiungere altri, meglio aggiungere quelli che avevano canali in precedenza. Basta andare su [Amboss page](https://amboss.space/), cercare gli alias o il nodeID dei vostri nodi peer e scansionare il loro URI.


![blixt](assets/en/17.webp)


Come si può vedere nell'immagine qui sopra, ci sono 3 aspetti:


A - rappresenta l'URI del nodo clearnet Address (dominio/IP)


B - rappresenta il nodo Tor onion Address URI (.onion)


C - è il codice QR da scansionare con la fotocamera Blixt o il pulsante di copia.


Questo nodo Address URI deve essere aggiunto all'elenco dei peer. Quindi non è sufficiente il nome dell'alias del nodo o il nodeID.


Ora si può andare su Magic Drawer (menu in alto a sinistra) - Lightning Channels, e si può vedere a quale altezza di blocco di scadenza i fondi verranno restituiti nella propria onchain Address.


![blixt](assets/en/18.webp)


Il blocco numero 764272 è il momento in cui i fondi saranno utilizzabili nella vostra Bitcoin sulla catena Address. E potrebbero essere necessari fino a 144 blocchi dal primo blocco di conferma fino al rilascio. [Quindi verificatelo nel Mempool](https://Mempool.space/).


E questo è tutto. Aspettate pazientemente che tutti i canali vengano chiusi e che i fondi tornino nel vostro Wallet onchain.


👉 **Metodo di ripristino segreto :**


Esiste un altro metodo per ripristinare il nodo Blixt LND senza nemmeno chiudere i canali. Ma è nascosto ai soliti utenti noob, perché questo metodo è SOLO per coloro che sanno cosa stanno facendo.


Nel caso in cui sia necessario migrare il nodo Blixt esistente (funzionante) su un altro nuovo dispositivo, senza chiudere i canali LN esistenti, è necessario eseguire i seguenti passaggi:



- Supponiamo che abbiate già salvato il Blixt Wallet seed (24 parole aezeed)
- Sul vecchio dispositivo, andare su "Impostazioni" - sezione debug - "Compatta database LND". Questo passaggio è facoltativo, ma consigliato se si desidera ridurre le dimensioni del file channel.db. Di solito è piuttosto grande, a seconda dell'attività del nodo. In questo modo si riavvia Blixt e si compatta la dimensione del file db.
- Una volta riavviato, andare su "Impostazioni" e cambiare il nome del proprio alias normale in "Hampus". In questo modo si attiveranno le opzioni nascoste, riservate agli utenti avanzati.
- Scendete fino alla sezione "Debug" e vedrete una nuova opzione "Esporta file channel.db". ATTENZIONE! Una volta effettuata questa esportazione, il nodo Blixt LN esistente verrà disattivato su questo vecchio dispositivo e verrà esportato l'intero database del nodo (channel.db) pronto per essere importato in un nuovo dispositivo.
- Questo file db verrà salvato in una cartella designata sul vecchio dispositivo (Documenti o Download) e da lì dovrà essere spostato così com'è sul nuovo dispositivo. È possibile utilizzare ad esempio [LocalSend FOSS app](https://github.com/localsend/localsend) per trasferire il file direttamente tra i dispositivi.
- In questo momento il vecchio Blixt DEVE rimanere spento. NON RIAPRIRLO!
- Una volta trasferito il file channel.db sul nuovo dispositivo, avviare la nuova installazione di Blixt e scegliere "Ripristina Wallet" nella prima schermata.
- Sul pulsante dove è scritto "Seleziona file SCB" premere a lungo (NON fare semplicemente clic!) e poi verrà visualizzata l'opzione per selezionare un file channel.db da salvare localmente nel nuovo dispositivo. Se si preme semplicemente quel pulsante, per impostazione predefinita verrà utilizzato un file SCB (con i canali in chiusura), mentre non funziona per i canali live con backup completo.
- Inserite le 24 parole seed e fate clic su "Ripristina"
- Vedrete che Blixt inizierà a sincronizzarsi con Neutrino. È possibile osservare anche i log di sincronizzazione.
- TENERE A MENTE! Cercate di tenere Blixt sempre aperto in questa fase! Non lasciare che vada in sospensione o che chiuda la schermata dell'app. Ciò potrebbe interrompere la sincronizzazione iniziale e doverla ripetere. Attendere pazientemente, non ci vogliono più di pochi minuti.
- Una volta terminata la sincronizzazione dei blocchi iniziali, verrà effettuata una rapida scansione degli indirizzi Wallet precedenti e i canali saranno nuovamente online, vivi e vegeti.
- Purtroppo non è ancora possibile ripristinare la cronologia dei pagamenti e i contatti precedenti. Ma questo non è così importante.


E FATTO! Ora avete un nodo Blixt LN completamente ripristinato. Potrebbe funzionare anche con altri backup di LND (Umbrel, Raspiblitz, ecc.) se si è salvato correttamente il file channel.db. Quindi Blixt può letteralmente salvare qualsiasi nodo LND morto.


---

## Blixt - Quarto contatto


Questo capitolo riguarda la personalizzazione e la conoscenza del nodo Blixt. Non descriverò tutte le funzionalità disponibili, sono troppe e sono già state spiegate nella [Blixt Features Page](https://blixtwallet.github.io/features).


Ma vi indicherò alcuni di quelli necessari per procedere con l'utilizzo di Blixt e avere una grande esperienza.


### A - Nome (NameDesc)


![blixt](assets/en/19.webp)


[Il NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) è uno standard per trasmettere il "nome del ricevitore" nelle fatture BOLT11.


Il nome può essere qualsiasi e può essere cambiato in qualsiasi momento.


Questa opzione è molto utile in vari casi, quando si desidera inviare un nome insieme alla descrizione del Invoice, in modo che il destinatario possa avere un'idea di chi ha ricevuto il Sats. Questa opzione è del tutto facoltativa e anche nella schermata di pagamento l'utente deve spuntare la casella che indica l'invio del nome alias.


Ecco un esempio di come appare quando si utilizza [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Questo è un altro esempio di invio a un'altra applicazione Wallet che supporta NameDesc:


![blixt](assets/en/21.webp)


### B - Scatola dei fulmini


A partire dalla nuova versione v0.6.9-420 [recentemente annunciata](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), Blixt ha introdotto una nuova potente funzione per Lightning Address in Blixt.


Questa nuova funzione è facoltativa e non è attiva di default!


Per il momento la casella LN predefinita è gestita dal server Blixt e offre un LN Address @blixtwallet.com. Ma CHIUNQUE abbia un nodo pubblico LND può gestire il server Lightning Box e offrire un LN Address per il proprio dominio, in autocustodia.


In questo momento, il server Blixt inoltra i pagamenti inviati agli indirizzi LN @blixtwallet.com solo agli utenti Blixt che hanno impostato il loro LN Address. Gli utenti devono mettere il loro nodo Blixt Wallet in "modalità persistente" per poter ricevere questi pagamenti ai loro indirizzi LN @blixtwallet.com.


Nelle note di rilascio è presente un video dimostrativo su come configurare il LN Address in Blixt.


Questo LN Address implementato nell'applicazione Blixt Wallet è come una chat su LN, istantanea e divertente, che supporta anche [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (aggiunta di un nome alias a un pagamento). È possibile aggiungere all'elenco dei contatti tutti gli indirizzi LN che si utilizzano di frequente e averli a portata di mano per chattare. Ora Blixt può essere considerata un'applicazione di chat LN completa 😂😂.


Un'altra caratteristica utile è il pieno supporto a LUD-18 (che anche [Stacker.News](https://stacker.news/r/DarthCoin) e altri supportano).


![blixt](assets/en/22.webp)


Come si può vedere nello screenshot qui sopra, inviando da un account Stacker News, è stato visualizzato il logo + LN Address + il messaggio. Lo stesso modo funziona per l'invio da Blixt: è possibile allegare il proprio LN Address Blixt o semplicemente aggiungere il nome dell'alias (precedentemente impostato nelle impostazioni di Blixt) o anche entrambi.


Questa opzione della LUD-18 potrebbe essere utile anche per i servizi di sottoscrizione, dove l'utente può inviare uno specifico alias (che NON è l'alias del proprio nodo o il proprio nome reale!) e in base a questo può essere registrato o ricevere un messaggio specifico o altro. Allegare un nome alias ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ un commento ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) a un pagamento LN può avere molteplici utilizzi!


Ecco il codice per [Lightning Box](https://github.com/hsjoberg/lightning-box) se lo eseguite per voi stessi, per la vostra famiglia e i vostri amici, sul vostro nodo.


Qui è anche possibile eseguire il [LSP Dunder server](https://github.com/hsjoberg/dunder-lsp) per i nodi mobili Blixt e offrire liquidità agli utenti Blixt se si dispone di un buon nodo pubblico LN (funziona solo con LND).


### C - Backup dei canali LN e delle parole seed


Si tratta di una funzione molto importante!


Dopo aver aperto o chiuso un canale LN è necessario eseguire un backup. Può essere fatto manualmente salvando un piccolo file sul dispositivo locale (di solito la cartella dei download) o utilizzando un account Google Drive o iCloud.


![blixt](assets/en/23.webp)


Andare alla sezione Impostazioni Blixt - Wallet. Qui sono disponibili le opzioni per salvare tutti i dati importanti del Blixt Wallet:



- "Mostra Mnemonic": visualizza le 24 parole seed per scriverle
- "Rimuovi Mnemonic dal dispositivo": questa opzione è facoltativa e va utilizzata solo se si desidera veramente rimuovere le parole seed dal dispositivo. Questo NON cancellerà il Wallet, ma solo il seed. Ma attenzione! Non c'è modo di recuperarle se non le si è annotate prima.
- "Esportazione del canale di backup": questa opzione salva un piccolo file sul dispositivo locale, di solito nella cartella "downloads", da cui è possibile prenderlo e spostarlo al di fuori del dispositivo, per conservarlo in modo sicuro.
- "Verifica il backup del canale": è una buona opzione se si utilizza Google Drive o iCloud per verificare l'integrità del backup eseguito in remoto.
- " Backup del canale di Google drive": salverà il file di backup nel vostro drive personale di Google. Il file è crittografato e viene memorizzato in un repository separato dai soliti file di Google. Quindi non ci sono preoccupazioni che possano essere lette da chiunque. In ogni caso, il file è totalmente inutile senza le parole seed, quindi nessuno può prendere i vostri fondi solo da quel file.


Per questa sezione raccomando quanto segue:



- utilizzare un gestore di password per memorizzare in modo sicuro il file seed e il file di backup. KeePass o Bitwarden sono ottimi per questo scopo e possono essere utilizzati su più piattaforme e in modalità self hosted o offline.
- Fare il BACKUP OGNI VOLTA che si apre o si chiude un canale. Il file viene aggiornato con le informazioni sui canali. Non è necessario farlo dopo ogni transazione effettuata su LN. Il backup del canale non memorizza tali informazioni, ma solo lo stato del canale.


![blixt](assets/en/24.webp)


---

## Blixt - Suggerimenti e trucchi


### CASO 1 - PROBLEMI DI SINCRONIZZAZIONE


"Il mio Blixt non si sincronizza... Il mio Blixt non mostra il saldo... Il mio Blixt non può aprire i canali... Ho provato a ripristinarlo in un altro dispositivo... ecc_"


Tutti questi problemi iniziano perché il vostro dispositivo non si sincronizza correttamente. Vi preghiamo di comprendere questo aspetto importante: Blixt è un nodo mobile LND che utilizza Neutrino per la sincronizzazione/lettura dei blocchi.



- Ecco una spiegazione meno tecnica tratta da [Bitcoin Magazine](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Ecco altre risorse tecniche di [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Ecco come è possibile attivare Neutrino sul proprio nodo domestico e servire filtri di blocco per il nodo mobile, da [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


RICORDA: L'utilizzo di Neutrino su clearnet è totalmente sicuro, il vostro IP o xpub non vengono divulgati. State solo leggendo i blocchi da un nodo remoto con Neutrino. Tutto qui. Tutto il resto viene fatto sul vostro dispositivo locale.


Quindi non è necessario utilizzarlo con Tor. Tor aggiungerà un'enorme latenza al processo di sincronizzazione e renderà Blixt molto instabile. Se volete davvero utilizzare Tor, assicuratevi di sapere cosa state facendo e di avere una buona connessione e pazienza. Lo stesso vale per l'utilizzo di una VPN. Fate attenzione alla latenza che vi viene fornita dalla VPN.


È possibile testare la latenza di un server neutrino semplicemente effettuando un ping, da un PC o da un cellulare.


![blixt](assets/en/25.webp)


Questo è il solito ping verso il server neutrino europe.blixtwallet.com, che mostra che la connessione è molto buona con un tempo di risposta di 50 ms in media e un TTL di 51. Il tempo di risposta può variare ma non troppo. Il TTL deve essere stabile.


Se questi valori sono superiori a 100-150 ms, il processo di sincronizzazione si interromperà o, peggio ancora, potrebbe causare la chiusura dei canali da parte dei peer! Non ignorate questo aspetto.


Senza una sincronizzazione adeguata, non è possibile vedere il bilanciamento corretto o i canali del LN non saranno online e operativi. Non importa quanti giga ultra terra mbps abbiate la velocità di download, non importa. È importante il tempo di risposta e il TTL (time to live).


Questo è un caso generale per gli utenti LATAM. Non so cosa sia successo laggiù, ma voi avete una connessione terribile con ping di oltre 200 ms che possono interrompere qualsiasi sincronizzazione.


Qual è dunque la soluzione per questi utenti disperati?



- smettere di usare Blixt con Tor. È totalmente inutile
- potete utilizzare una VPN, ma sceglietela con saggezza e monitorate costantemente il ping. Utilizzatene una più vicina alla vostra posizione geografica. La distanza significa un tempo di risposta maggiore, ricordate.
- scegliete saggiamente i vostri peer di neutrino, ecco un elenco di server di neutrino pubblici ben noti:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Un altro modo è quello di selezionare uno da questo elenco di nodi che annuncia i "filtri compatti" (BIP157 / neutrino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Scegliete quello più vicino alla vostra posizione geografica.


Un altro modo (il migliore) è quello di collegarsi a un nodo della comunità locale, gestito da un amico o da un gruppo che si conosce e che offre una connessione a neutrini. [Qui le istruzioni per farlo](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Il loro nodo non sarà influenzato in alcun modo, hanno solo bisogno di una connessione stabile e pubblica.


C'è bisogno di più server neutrino nella regione LATAM, per una sincronizzazione migliore e veloce. Quindi, per favore, organizzatevi con la vostra comunità locale di Bitcoin e decidete chi e dove gestisce un Bitcoin Core + Neutrino per il vostro uso personale. È sufficiente un IP pubblico. Se non avete accesso a un IP pubblico, potete utilizzare un IP VPS e creare un tunnel wireguard verso il vostro nodo domestico. In questo modo si reindirizza tutto il traffico al proprio IP VPS locale, senza rivelare alcuna informazione privata sul proprio nodo domestico.


### CASO 2 - NON TERMINA MAI LA SINCRONIZZAZIONE


"_Il mio Blixt ha una buona connessione con il server neutrino ma è bloccato nella sincronizzazione._"


#### Server del tempo


A volte le persone utilizzano dispositivi vecchi o non sono correttamente collegati a un server orario. Neutrino si sincronizza bene fino a quando non raggiunge i blocchi effettivi che non corrispondono all'ora locale reale. Nei log di Blixt LND si vedrà un errore che dice che "l'ora del blocco è lontana dal futuro" o qualcosa di simile a "l'intestazione non passa il controllo di correttezza".


Soluzione rapida: impostare la data e l'ora corrette per il dispositivo e riavviare Blixt.


#### Spazio ridotto sul dispositivo


A volte, utilizzando un vecchio dispositivo, con poco spazio, può raggiungere una soglia limite e bloccarsi. Infatti, se si utilizza questo nodo mobile LND, i file dei neutrini diventano più grandi e anche il file channel.db.


Correzione rapida: Andare in Opzioni Blixt - Sezione Debug - Selezionare "arresta LND e cancella i file di neutrini". L'applicazione verrà riavviata e inizierà una nuova sincronizzazione. A volte questa soluzione rapida può riparare anche i dati danneggiati. Tenere presente che ci vorrà un po' di tempo, tra 1 e 3 minuti, per una risincronizzazione completa. NON cancella i fondi o i canali esistenti, ma sì, dopo la risincronizzazione potrebbe attivarsi una nuova scansione degli indirizzi del Bitcoin e ciò potrebbe richiedere più tempo.


Il passo successivo è verificare la quantità di dati ancora occupati. È possibile vedere questo dato in Info app Android - Dati. Se è ancora più grande di 400-500 MB, è possibile compattare i file LND. Andare quindi in Opzioni Blixt - Sezione Debug - Selezionare "Compatta DB LND". Riavviare l'applicazione Blixt se non viene eseguita automaticamente. La compattazione avviene all'avvio e solo una volta. Ora si vedrà che i dati di Blixt sono più o meno occupati.


#### Modalità persistente


A volte le persone non aprono Blixt per molto tempo, quindi la sincronizzazione è troppo vecchia. Ma si aspettano di essere sincronizzati istantaneamente quando lo aprono.


Abbiate pazienza e guardate la ruota che gira in alto. Opzionalmente si può andare su Opzioni - Vedi informazioni sul nodo e vedere se la sincronizzazione con la catena e la sincronizzazione con il grafico sono contrassegnate come "vero". Senza questa dicitura "true" non è possibile utilizzare correttamente Blixt, non è possibile vedere correttamente il saldo, non è possibile vedere i canali LN online, non è possibile effettuare pagamenti.


Correzione rapida: Esiste una potente opzione per "mantenere in vita" il nodo Blixt. Andate in Opzioni - Esperimenti - Selezionate "Attiva modalità persistente". Questo riavvierà Blixt e metterà il servizio LND in modalità persistente, ovvero sarà sempre attivo e manterrà online la sincronizzazione, anche se si passa a un'altra applicazione o semplicemente si chiude Blixt (non si chiude forzatamente o si uccide l'attività). È possibile mantenere questa modalità per tutto il giorno se si dispone di una connessione stabile e si ha bisogno di utilizzare Blixt più volte. Non consumerà troppo la batteria.


### CASO 3 - VOGLIO MIGRARE SU UN ALTRO DISPOSITIVO


Su questo scenario ho scritto una guida esauriente nella [pagina delle FAQ](https://blixtwallet.github.io/faq#blixt-restore): con due opzioni, veloce (chiusura cooperativa dei canali prima della migrazione) e lenta (chiusura forzata dei canali perché il vecchio dispositivo è morto).


Ma voglio ribadire qui alcuni aspetti importanti e aggiungere una nuova procedura "segreta".


RICORDA:



- Eseguite sempre un backup dello stato dei vostri canali (SCB) DOPO ogni apertura o chiusura di un canale. Bastano pochi secondi per farlo.
- Non conservate i vecchi file SCB, per non confondervi e ripristinarli. Sono del tutto inutili e potrebbero innescare una procedura di sanzione se li si usa. Utilizzate sempre l'ultima versione del file SCB se procedete al ripristino.
- Salvare il file SCB (è un testo crittografato con estensione .bin) fuori dal dispositivo, in un luogo sicuro. È possibile utilizzare [LocalSend](https://github.com/localsend/localsend) per spostare questo file su un PC o un altro dispositivo.
- Conservare anche il seed del Blixt Wallet in un luogo sicuro, ad esempio un gestore di password offline o una USB crittografata.


Metodo segreto: Come migrare il nodo Blixt senza chiudere i canali esistenti. Per questo è necessario leggere attentamente la sezione precedente "Terzo contatto" di questa guida sul "Ripristino di Wallet".


Questa procedura NON È PER NOOBS, è solo per utenti avanzati! Per questo motivo non è molto diffusa e consiglio di eseguirla solo con l'assistenza degli sviluppatori di Blixt o del mio supporto. Non ignorate questo consiglio.


### CASO 4 - QUALI PEER UTILIZZARE PER APRIRE I CANALI?


Come ho scritto nella [pagina delle guide Blixt](https://blixtwallet.github.io/guides), ci sono molti modi per aprire canali con questo nodo mobile LND. Ma vorrei ricordare alcuni aspetti importanti:



- aperto con nodi LSP ben noti e con peer garantiti dalla comunità. [Vedi qui un elenco](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- non aprire con nodi casuali solo Tor. Sono inutili e avrete solo problemi di impossibilità di effettuare pagamenti. Non importa quanto sia bravo il vostro amico "il corridore di nodi" con un nodo Tor scadente in una giungla, non vi darà mai i migliori percorsi per un nodo privato mobile. Non si aprono canali con qualcuno perché è tuo amico. Questo non è Facebook! Si apre un canale per: buone rotte, piccole tariffe, disponibilità.
- non è necessario aprire una tonnellata di canali piccoli, 2-3 o al massimo 4, ma con una buona quantità di Sats. Non aprite canali piccoli, sono totalmente inutili. Più piccoli di 200k per un cellulare non servono a molto.
- tenete presente i LSP che offrono canali in entrata e canali JIT (just in time). Questi sono molto utili perché non è necessario utilizzare nessuno dei vostri UTXO, potete pagare il canale di apertura con i fondi che avete già in altri portafogli LN, impilandoli e preparandoli per l'apertura di un canale più grande. Dovreste usare questi canali JIT a vostro favore. [Ho spiegato in questa guida](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) più opzioni per i peer per i nodi privati come Blixt. Inoltre [in questa guida pubblicata su SN](https://stacker.news/items/679242/r/DarthCoin) ho spiegato come gestire la liquidità dei nodi mobili privati.


---

## Conclusione


OK, ci sono molte altre caratteristiche sorprendenti che Blixt offre, ve le farò scoprire una per una e divertitevi.


Questa applicazione è davvero sottovalutata, soprattutto perché non è sostenuta da alcun finanziamento VC, è guidata dalla comunità, costruita con amore e passione per Bitcoin e Lightning Network.


Questo nodo mobile LN, Blixt, è uno strumento molto potente nelle mani di molti utenti, se sanno come usarlo bene. Immaginate di girare per il mondo con un nodo LN in tasca e che nessuno lo sappia.


E non parliamo di tutte le altre ricche funzioni che vengono fornite, che poche o nessuna altra applicazione Wallet può offrire.


Nel frattempo, ecco tutti i link su questo incredibile nodo Bitcoin Lightning:



- [Pagina web ufficiale di Blixt](https://blixtwallet.com/)
- [Pagina Github di Blixt](https://github.com/hsjoberg/blixt-Wallet/)
- [Pagina delle caratteristiche di Blixt](https://blixtwallet.github.io/features) - che spiega una per una ogni caratteristica e funzionalità.
- [Pagina delle FAQ di Blixt](https://blixtwallet.github.io/faq) - Elenco di domande e risposte e risoluzione dei problemi di Blixt
- [Pagina delle guide Blixt](https://blixtwallet.github.io/guides) - demo, video tutorial, guide extra e casi d'uso per Blixt
- Download: [Play Store Android](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [Download diretto APK](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Gruppo Telegram per il supporto diretto](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Pagina di crowdfunding di Geyser](https://geyser.fund/project/blixt) - dona Sats a tuo piacimento per sostenere il progetto
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - chat anonima LN
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Calendario delle ragazze Blixt](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - video promozionale (è possibile testare il primo utilizzo di LN)
- [Volantino stampabile in formato A4 con i primi passi da compiere con Blixt, in varie lingue](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt offre anche una demo funzionale completa](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) direttamente sul suo sito web o su una versione web dedicata, per avere un'esperienza di prova completa, prima di iniziare a usarla nel mondo reale.


---
**DISCLAIMER:**


*Non sono pagato o supportato in alcun modo dagli sviluppatori di questa applicazione. Ho scritto questa guida perché ho visto che l'interesse per questa applicazione Wallet sta aumentando e i nuovi utenti non capiscono ancora come iniziare. Anche per aiutare Hampus (lo sviluppatore principale) con la documentazione sull'utilizzo di questo nodo Wallet.*


*Non ho alcun interesse a promuovere questa applicazione LN, se non quello di promuovere l'adozione di Bitcoin e LN. Questo è l'unico modo!*


---
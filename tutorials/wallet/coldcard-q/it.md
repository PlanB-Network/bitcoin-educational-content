---
name: COLDCARD Q
description: Impostazione e utilizzo di una COLDCARD Q
---
![cover](assets/cover.webp)

Un portafoglio hardware è un dispositivo elettronico dedicato alla gestione e alla protezione delle chiavi private di un portafoglio Bitcoin. A differenza dei portafogli software (o hot wallet) installati su macchine generiche spesso connesse a Internet, i portafogli hardware consentono di isolare fisicamente le chiavi private, riducendo il rischio di pirateria e furto.

L'obiettivo principale di un portafoglio hardware è quello di ridurre il più possibile le funzionalità del dispositivo per minimizzare la superficie di attacco. Una minore superficie di attacco significa anche un minor numero di potenziali vettori di attacco, ossia un minor numero di punti deboli del sistema che gli aggressori potrebbero sfruttare per ottenere l'accesso ai bitcoin.

È consigliabile utilizzare un portafoglio hardware per proteggere i bitcoin, soprattutto se se ne possiedono grandi quantità, sia in valore assoluto che in proporzione al patrimonio totale.

I portafogli hardware sono utilizzati insieme al software di gestione del portafoglio su un computer o uno smartphone. Quest'ultimo gestisce la creazione delle transazioni, ma la firma crittografica necessaria a renderle valide viene eseguita esclusivamente all'interno del portafoglio hardware. Ciò significa che le chiavi private non sono mai esposte a un ambiente potenzialmente vulnerabile.

I portafogli hardware offrono una doppia protezione all'utente: da un lato, proteggono i bitcoin da attacchi remoti mantenendo le chiavi private offline, dall'altro, offrono generalmente una maggiore resistenza fisica ai tentativi di estrazione delle chiavi. È proprio in base a questi due criteri di sicurezza che possiamo giudicare e classificare i diversi modelli presenti sul mercato.

In questo tutorial vorrei presentarvi una di queste soluzioni: la **COLDCARD Q**.

---
Poiché la COLDCARD Q offre una moltitudine di funzioni, propongo di suddividere il suo utilizzo in 2 esercitazioni. In questo primo tutorial, esamineremo la configurazione iniziale e le funzioni di base del dispositivo. Poi, in un secondo tutorial, vedremo come sfruttare tutte le opzioni avanzate della COLDCARD.

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
---
## Introduzione alla COLDCARD Q

La COLDCARD Q è un portafoglio hardware per soli Bitcoin sviluppato dalla società canadese Coinkite, nota per i precedenti modelli MK. La Q rappresenta il prodotto più avanzato fino ad oggi e si posiziona come il portafoglio hardware Bitcoin definitivo.

In termini di hardware, la COLDCARD Q è dotata di tutte le caratteristiche necessarie per un'esperienza d'uso ottimale:


- Un ampio display LCD semplifica la navigazione e il funzionamento;
- Una tastiera QWERTY completa;
- Fotocamera integrata per la scansione dei codici QR;
- Due slot per schede microSD ;
- Un'opzione di alimentazione completamente isolata tramite tre batterie AAA (non incluse) o tramite un cavo USB-C;
- Due Secure Elements di due produttori diversi per una maggiore sicurezza;
- La capacità di comunicare tramite NFC.

A mio parere, la COLDCARD Q presenta solo due inconvenienti. In primo luogo, a causa delle sue numerose funzioni, è piuttosto ingombrante, misurando quasi 13 cm di lunghezza e 8 cm di larghezza, ovvero quasi le dimensioni di un piccolo smartphone. È anche piuttosto spesso a causa del vano batteria. Se siete alla ricerca di un portafoglio hardware più piccolo e più mobile, l'MK4, molto più compatto, potrebbe essere un'opzione migliore. Il secondo svantaggio è ovviamente il costo del dispositivo, che sul sito ufficiale ha un prezzo di 239,99 dollari**, ovvero 72 dollari in più rispetto all'MK4, il che mette il Q in diretta concorrenza con portafogli hardware di qualità superiore come il Ledger Flex o il Passport di Foundation.

![CCQ](assets/fr/001.webp)

Dal punto di vista del software, la COLDCARD Q è ben equipaggiata come gli altri dispositivi Coinkite, con una serie di funzioni avanzate:


- Tiro di dadi per generare la propria frase di recupero;
- Codice PIN ;
- Conto alla rovescia per il blocco definitivo del PIN ;
- BIP39 passphrase ;
- PIN di chiusura finale ;
- Conto alla rovescia della connessione ;
- SeedXOR;
- BIP85...

In breve, la COLDCARD Q offre un'esperienza d'uso migliorata rispetto alla MK4 e può essere ideale per gli utenti di livello intermedio o avanzato che desiderano una maggiore facilità d'uso.

La COLDCARD Q è in vendita [sul sito ufficiale di Coinkite](https://store.coinkite.com/store/coldcard). Può anche essere acquistata presso un rivenditore.

## Preparazione dell'esercitazione

Una volta ricevuta la COLDCARD, il primo passo è ispezionare la confezione per assicurarsi che non sia stata aperta. Se la confezione è danneggiata, ciò potrebbe indicare che il portafoglio hardware è stato compromesso e potrebbe non essere autentico.

![CCQ](assets/fr/002.webp)

Quando si apre la scatola, si trovano i seguenti elementi:


- La COLDCARD Q è contenuta in una busta sigillata;
- Una scheda per registrare la frase mnemonica.

![CCQ](assets/fr/003.webp)

Assicuratevi che il sacchetto non sia stato sigillato o danneggiato. Verificate inoltre che il numero riportato sul sacchetto corrisponda a quello riportato sulla carta all'interno del sacchetto. Conservate questo numero per un riferimento futuro.

![CCQ](assets/fr/004.webp)

Se si preferisce alimentare la COLDCARD senza collegarla a un computer (air-gap), inserire tre batterie AAA nella parte posteriore del dispositivo. In alternativa, è possibile collegarla al computer tramite un cavo USB-C.

![CCQ](assets/fr/005.webp)

Per questa esercitazione, è necessario anche Sparrow Wallet per gestire il portafoglio Bitcoin sul computer. Scaricate [Sparrow Wallet](https://sparrowwallet.com/download/) dal sito ufficiale. Vi consiglio vivamente di verificarne l'autenticità (con GnuPG) e l'integrità (tramite hash) prima di procedere all'installazione. Se non sapete come fare, seguite questo tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
## Selezione del codice PIN

Ora è possibile accendere la COLDCARD premendo il pulsante nell'angolo in alto a sinistra.

![CCQ](assets/fr/006.webp)

Premere il pulsante "*INVIO*" per accettare le condizioni di utilizzo.

![CCQ](assets/fr/007.webp)

La COLDCARD Q visualizzerà un numero nella parte superiore dello schermo. Assicuratevi che questo numero corrisponda a quello riportato sulla busta sigillata e sul pezzo di plastica all'interno della busta. In questo modo si garantisce che la confezione non sia stata aperta tra il momento in cui è stata confezionata da Coinkite e quello in cui è stata aperta. Premere "*INVIO*" per continuare.

![CCQ](assets/fr/008.webp)

Passare al menu "*Scegliere il codice PIN*" e confermare con il tasto "*INVIO*".

![CCQ](assets/fr/009.webp)

Questo codice PIN viene utilizzato per sbloccare la COLDCARD. È quindi una protezione contro l'accesso fisico non autorizzato. Questo codice PIN non partecipa alla creazione delle chiavi crittografiche del vostro portafoglio. Pertanto, anche senza accesso a questo codice PIN, il possesso della frase mnemonica vi permetterà di riavere accesso ai vostri bitcoin.

I codici PIN della COLDCARD sono divisi in due parti: un prefisso e un suffisso, ciascuno dei quali può contenere da 2 a 6 cifre, per un totale di 4-12 cifre. Quando sbloccate la vostra COLDCARD, dovrete innanzitutto inserire il prefisso, dopodiché il dispositivo vi mostrerà 2 parole. Quindi inserire il suffisso. Queste due parole vengono fornite durante questa fase di configurazione e devono essere salvate con cura, poiché serviranno ogni volta che si sblocca la COLDCARD. Se le due parole visualizzate durante lo sblocco corrispondono a quelle salvate durante la configurazione, ciò conferma che il dispositivo non è stato compromesso dall'ultimo utilizzo.

Cliccate nuovamente su "*Scegliere il PIN*"

![CCQ](assets/fr/010.webp)

Confermare di aver letto le avvertenze.

![CCQ](assets/fr/011.webp)

A questo punto si sceglierà il codice PIN. Si consiglia un codice PIN lungo e casuale. Assicuratevi di conservare questo codice in un luogo diverso da quello in cui è conservata la COLDCARD. Per registrare questo codice si può utilizzare la scheda fornita nel pacco.

Inserire il prefisso desiderato, quindi premere il tasto "*INVIO*" per confermare la prima parte del codice PIN.

![CCQ](assets/fr/012.webp)

Sullo schermo appariranno le due parole anti-phishing. Conservatele con cura per riferimento futuro. Per annotarle, potete utilizzare la scheda inclusa nella confezione.

![CCQ](assets/fr/013.webp)

Inserire quindi la seconda parte del codice PIN e premere "*INVIO*".

![CCQ](assets/fr/014.webp)

Confermate il PIN inserendolo una seconda volta, controllando che le due parole anti-phishing corrispondano a quelle salvate in precedenza.

![CCQ](assets/fr/015.webp)

D'ora in poi, ogni volta che sbloccherete la vostra COLDCARD, ricordatevi di controllare la validità delle due parole anti-phishing che appaiono sullo schermo dopo aver inserito il prefisso del codice PIN.

## Aggiornamento del firmware

Quando si utilizza il dispositivo per la prima volta, è importante controllare e aggiornare il firmware. A tale scopo, accedere al menu "*Avanzate/Strumenti*".

![CCQ](assets/fr/016.webp)

**Importante:** Se si intende aggiornare il firmware e non è la prima volta che si utilizza COLDCARD (cioè si dispone già di un portafoglio creato su COLDCARD), assicurarsi di disporre della frase mnemonica e che sia funzionante (nonché della passphrase opzionale, se applicabile). Questo è importante per evitare di perdere i bitcoin in caso di problemi durante l'aggiornamento del dispositivo.

Selezionare "*Aggiornamento del firmware*".

![CCQ](assets/fr/017.webp)

Selezionare "*Mostra versione*".

![CCQ](assets/fr/018.webp)

È possibile verificare la versione attuale del firmware della COLDCARD. Ad esempio, nel mio caso la versione è "*1.2.3Q*".

![CCQ](assets/fr/019.webp)

Controllare [sul sito ufficiale della COLDCARD](https://coldcard.com/downloads) se è disponibile una versione più recente. Fare clic su "*Download*" per scaricare il nuovo firmware.

![CCQ](assets/fr/020.webp)

A questo punto, si consiglia vivamente di verificare l'integrità e l'autenticità del firmware scaricato. A tal fine, scaricare [il documento contenente gli hash di tutte le versioni, firmato dagli sviluppatori](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), verificare la firma con [la chiave pubblica dello sviluppatore](https://keybase.io/dochex) e assicurarsi che l'hash indicato nel documento firmato corrisponda a quello del firmware scaricato dal sito. Se tutto è corretto, si può procedere con l'aggiornamento.

Se non avete familiarità con questo processo di verifica, vi consiglio di seguire questa guida:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Prendete una scheda microSD e trasferiteci il file del firmware (documento in `.dfu`). Inserire la scheda microSD in una delle porte della COLDCARD.

![CCQ](assets/fr/021.webp)

Quindi, nel menu di aggiornamento del firmware, selezionare "*Da MicroSD*".

![CCQ](assets/fr/022.webp)

Selezionare il file corrispondente al firmware.

![CCQ](assets/fr/023.webp)

Confermare la selezione premendo il tasto "*ENTER*".

![CCQ](assets/fr/024.webp)

Attendere l'aggiornamento del firmware.

![CCQ](assets/fr/025.webp)

Una volta completato l'aggiornamento, inserire il codice PIN per sbloccare il dispositivo.

![CCQ](assets/fr/026.webp)

Il firmware è ora aggiornato.

## Parametri COLDCARD Q

Se lo desiderate, potete esplorare le impostazioni della vostra COLDCARD accedendo al menu "*Impostazioni*".

![CCQ](assets/fr/027.webp)

In questo menu si trovano varie opzioni di personalizzazione, come l'impostazione della luminosità dello schermo o la selezione dell'unità di misura predefinita.

![CCQ](assets/fr/028.webp)

Nel prossimo tutorial vedremo altre impostazioni avanzate:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
## Creare un portafoglio Bitcoin

Ora è il momento di generare un nuovo portafoglio Bitcoin! Per farlo, è necessario creare una frase mnemonica. Su Coldcard, avete tre metodi per generare questa frase:


- Utilizzare solo il generatore di numeri casuali interno (TRNG);
- Utilizzare una combinazione di TRNG e lancio di dadi per aggiungere entropia;
- Utilizzare solo i tiri di dado.

**Per i principianti e gli utenti intermedi, si consiglia di utilizzare solo il generatore di numeri casuali interno alla COLDCARD**

Non raccomando l'opzione del solo dado, perché una cattiva esecuzione può portare a una frase con un'entropia insufficiente, mettendo a rischio la sicurezza del vostro portafoglio.

Tuttavia, l'opzione migliore è sicuramente la seconda, che combina l'uso del TRNG con una fonte di entropia esterna. Questo metodo garantisce un'entropia minima equivalente a quella del solo TRNG e aggiunge un ulteriore livello di sicurezza nel caso di un eventuale fallimento del generatore interno (volontario o meno). Scegliendo questa opzione, che combina TRNG e lancio di dadi, beneficiate di un maggiore controllo sulla generazione della frase, senza aumentare i rischi in caso di cattiva esecuzione da parte vostra.

Fare clic su "*Nuove parole seme*".

![CCQ](assets/fr/029.webp)

Potete scegliere la lunghezza della frase. Vi consiglio di optare per una frase di 12 parole, perché è meno complessa da gestire e non offre meno sicurezza di portafoglio rispetto a una frase di 24 parole.

![CCQ](assets/fr/030.webp)

La COLDCARD visualizzerà quindi la frase di recupero generata dal TRNG. Se si desidera aggiungere ulteriore entropia esterna, premere il tasto "*4*".

![CCQ](assets/fr/031.webp)

Si accede così a una pagina in cui è possibile aggiungere entropia lanciando i dadi. Effettuate il maggior numero possibile di lanci (si consiglia un minimo di 50, ma un numero inferiore non è un problema, poiché state già beneficiando dell'entropia del TRNG) e registrate i risultati con i tasti da "*1*" a "*6*". Al termine, premere "*INVIO*" per confermare.

![CCQ](assets/fr/032.webp)

Verrà visualizzata una nuova frase mnemonica, basata sull'entropia appena fornita e su quella del TRNG.

**Attenzione: Questo mnemonico dà accesso completo e illimitato a tutti i vostri bitcoin**. Chiunque sia in possesso di questa frase può rubare i vostri fondi, anche senza accedere fisicamente alla vostra COLDCARD. La frase di 12 parole ripristina l'accesso ai vostri bitcoin in caso di perdita, furto o rottura della COLDCARD. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.

Potete scriverlo sul cartoncino fornito con la vostra COLDCARD oppure, per maggiore sicurezza, vi consiglio di inciderlo su un supporto in acciaio inox per proteggerlo dal rischio di incendi, alluvioni o crolli. In ogni caso, non salvatela mai su un supporto digitale, altrimenti potreste perdere i vostri bitcoin.

Scrivete le parole fornite sullo schermo su un supporto fisico di vostra scelta. A seconda della vostra strategia di sicurezza, potete pensare di fare diverse copie fisiche complete della frase (ma soprattutto non dividetela). È importante che le parole siano numerate e in ordine sequenziale.

Ovviamente, **non dovete mai condividere queste parole** su Internet, a differenza di quanto avviene in questa esercitazione. Questo portfolio di esempio sarà utilizzato solo su Testnet e sarà cancellato alla fine dell'esercitazione.

Dopo aver scritto le parole, premere "*INVIO*".

![CCQ](assets/fr/033.webp)

Per assicurarsi che la frase sia stata salvata correttamente, il sistema chiederà di confermare alcune parole. Selezionare il numero corrispondente a ciascuna parola sulla tastiera.

![CCQ](assets/fr/034.webp)

Il vostro portafoglio è stato creato! Nell'angolo in alto a destra dello schermo è visibile l'impronta digitale della chiave privata principale. Premete "*INVIO*".

![CCQ](assets/fr/035.webp)

Ora si accede al menu principale della COLDCARD.

![CCQ](assets/fr/036.webp)

## Impostazione di un nuovo portafoglio su Sparrow

Esistono diverse opzioni per stabilire la comunicazione tra il software Sparrow Wallet e la COLDCARD. La più semplice consiste nell'utilizzare un cavo USB-C. Tuttavia, per impostazione predefinita, le comunicazioni via cavo e NFC della COLDCARD sono disattivate. Per riattivarle, accedere a "*Impostazioni*", quindi a "*Hardware On/Off*" e attivare l'opzione di comunicazione desiderata.

![CCQ](assets/fr/037.webp)

Se preferite mantenere la vostra COLDCARD totalmente isolata dal computer, potete optare per una comunicazione indiretta "air-gap", utilizzando codici QR o una scheda microSD. Questo è il metodo che utilizzeremo in questa esercitazione.

Andare a "*Avanzate/Strumenti*".

![CCQ](assets/fr/038.webp)

Selezionare "*Esporta portafoglio*".

![CCQ](assets/fr/039.webp)

Quindi selezionare "*Portafoglio*".

![CCQ](assets/fr/040.webp)

Premere "*INVIO*" per generare il file di configurazione.

![CCQ](assets/fr/041.webp)

Scegliere quindi come inviare il file a Sparrow. In questo esempio, ho inserito una microSD nello slot "*A*", quindi selezionerò il pulsante "*1*". È anche possibile visualizzare le informazioni come codice QR sullo schermo della COLDCARD premendo il pulsante "*QR*" e scansionare il codice QR con la webcam del computer.

![CCQ](assets/fr/042.webp)

Avviare Sparrow Wallet e saltare le pagine introduttive per raggiungere la schermata principale. Assicuratevi di essere correttamente connessi a un nodo controllando l'interruttore in basso a destra dello schermo.

![CCQ](assets/fr/043.webp)

Si raccomanda vivamente di utilizzare il proprio nodo Bitcoin. Per questo tutorial, sto usando un nodo pubblico (giallo), dato che sono sulla testnet, ma per l'uso in produzione, è meglio usare Bitcoin Core localmente (verde) o un server Electrum su un nodo remoto (blu).

Accedere al menu "*File*" e selezionare "*Nuovo portafoglio*".

![CCQ](assets/fr/044.webp)

Date un nome al vostro portafoglio e cliccate su "*Crea portafoglio*".

![CCQ](assets/fr/045.webp)

Nel menu a discesa "*Tipo di script*", scegliere il tipo di script che proteggerà i bitcoin.

![CCQ](assets/fr/046.webp)

Fare clic su "*Portafoglio hardware sospeso*".

![CCQ](assets/fr/047.webp)

Nella scheda "*Coldcard*", fare clic su "*Scansione...*" se si intende scansionare il codice QR visualizzato sulla COLDCARD, oppure su "*Importa file...*" per importare il file dalla microSD (si tratta del file `.json`).

![CCQ](assets/fr/048.webp)

Dopo l'importazione, verificare che la "*impronta master*" visualizzata su Sparrow corrisponda a quella visualizzata sulla COLDCARD. Confermare la creazione cliccando su "*Apply*".

![CCQ](assets/fr/049.webp)

Impostate una password forte per proteggere l'accesso al vostro Sparrow Wallet. Questa password proteggerà le chiavi pubbliche, gli indirizzi, i tag e la cronologia delle transazioni da accessi non autorizzati.

È buona norma salvare questa password per non dimenticarla (ad esempio, in un gestore di password).

![CCQ](assets/fr/050.webp)

Il vostro portafoglio è ora impostato su Sparrow Wallet.

![CCQ](assets/fr/051.webp)

Prima di ricevere i primi bitcoin nel portafoglio, **vi consiglio vivamente di eseguire un test di ripristino a vuoto**. Annotate alcune informazioni di riferimento, come il vostro xpub, quindi resettate la vostra COLDCARD Q mentre il portafoglio è ancora vuoto. Quindi provare a ripristinare il portafoglio sulla COLDCARD utilizzando i backup cartacei. Verificare che l'xpub generato dopo il ripristino corrisponda a quello annotato in origine. Se così fosse, si può essere certi che i backup cartacei sono affidabili.

Per saperne di più su come eseguire un test di ripristino, vi suggerisco di consultare quest'altra guida:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Ricevere bitcoin

Per ricevere i primi bitcoin, iniziate accendendo e sbloccando la vostra COLDCARD.

![CCQ](assets/fr/052.webp)

Su Sparrow Wallet, fare clic sulla scheda "*Receive*".

![CCQ](assets/fr/053.webp)

Prima di utilizzare l'indirizzo proposto da Sparrow Wallet, verificarlo sullo schermo della COLDCARD. Questa pratica consente di confermare che l'indirizzo visualizzato su Sparrow non è fraudolento e che il portafoglio hardware possiede effettivamente la chiave privata necessaria per spendere successivamente i bitcoin garantiti da questo indirizzo. Ciò consente di evitare diversi tipi di attacco.

Per eseguire questo controllo, fare clic sul menu "*Address Explorer*" della COLDCARD.

![CCQ](assets/fr/054.webp)

Selezionare il tipo di script che si sta utilizzando su Sparrow. Nel mio caso, si tratta di Segwit P2WPKH. Faccio clic su di esso.

![CCQ](assets/fr/055.webp)

È quindi possibile visualizzare in ordine i diversi indirizzi derivati.

![CCQ](assets/fr/056.webp)

Verificare con Sparrow che l'indirizzo corrisponda. Nel mio caso, l'indirizzo con percorso di derivazione `m/84'/1'/0'/0/0` è effettivamente `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` sia su Sparrow che su COLDCARD.

![CCQ](assets/fr/057.webp)

Un altro modo per verificare la proprietà di questo indirizzo è scansionare il suo codice QR direttamente su Sparrow dalla COLDCARD. Dalla schermata iniziale della COLDCARD, selezionare "*Scansiona qualsiasi codice QR*". È anche possibile utilizzare il tasto "*QR*" sulla tastiera.

![CCQ](assets/fr/058.webp)

Scansionare il codice QR dell'indirizzo visualizzato su Sparrow Wallet.

![CCQ](assets/fr/059.webp)

Assicurarsi che l'indirizzo visualizzato sulla COLDCARD corrisponda a quello visualizzato su Sparrow. Quindi premere il pulsante "*1*".

![CCQ](assets/fr/060.webp)

L'indirizzo è quindi confermato con successo.

![CCQ](assets/fr/061.webp)

È ora possibile aggiungere un "*Label*" per descrivere la fonte dei bitcoin che saranno assicurati con questo indirizzo. Questa è una buona pratica che consente di gestire meglio gli UTXO.

![CCQ](assets/fr/062.webp)

Per ulteriori informazioni sull'etichettatura, consiglio anche quest'altro tutorial:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52
È quindi possibile utilizzare questo indirizzo per ricevere bitcoin.

![CCQ](assets/fr/063.webp)

## Inviare bitcoin

Ora che avete ricevuto le prime sature nel vostro portafoglio protetto da COLDCARD, potete anche spenderle!

Come sempre, iniziate accendendo e sbloccando la vostra COLDCARD Q, quindi aprite Sparrow Wallet e passate alla scheda "*Invio*" per preparare una nuova transazione.

![CCQ](assets/fr/064.webp)

Se si desidera "controllare le monete", ossia scegliere specificamente quali UTXO consumare nella transazione, andare alla scheda "*UTXO*". Selezionare gli UTXO che si desidera spendere, quindi fare clic su "*Invia selezionati*". Si verrà reindirizzati alla stessa schermata della scheda "*Invio*", ma con gli UTXO già selezionati per la transazione.

![CCQ](assets/fr/065.webp)

Inserire l'indirizzo di destinazione. È possibile inserire più indirizzi facendo clic sul pulsante "*+ Aggiungi*".

![CCQ](assets/fr/066.webp)

Scrivete una "*Etichetta*" per ricordare lo scopo di questa spesa.

![CCQ](assets/fr/067.webp)

Selezionare l'importo da inviare a questo indirizzo.

![CCQ](assets/fr/068.webp)

Adattare il tasso di commissione della transazione in base al mercato attuale.

![CCQ](assets/fr/069.webp)

Assicurarsi che tutti i parametri della transazione siano corretti, quindi fare clic su "*Crea transazione*".

![CCQ](assets/fr/070.webp)

Se tutto è di vostro gradimento, cliccate su "*Finalizza la transazione per la firma*".

![CCQ](assets/fr/071.webp)

Una volta creata la transazione in Sparrow, è il momento di firmarla con la COLDCARD. Per trasmettere la PSBT (transazione non firmata) al dispositivo, sono disponibili diverse opzioni. Se la trasmissione dati via cavo è abilitata, è possibile inviare la transazione direttamente tramite una connessione USB-C, proprio come si farebbe con qualsiasi altro portafoglio hardware. In questo caso, su Sparrow, dovrete fare clic sul pulsante "*Sign*" nell'angolo in basso a destra. Nel mio esempio, questo pulsante è bloccato perché la COLDCARD non è collegata via cavo.

![CCQ](assets/fr/072.webp)

Se si preferisce mantenere una connessione "air-gap" senza contatto diretto tra il portafoglio hardware e il computer, si hanno due opzioni. La prima, più complessa, consiste nell'utilizzare una scheda microSD. Inserite la scheda microSD nel computer, registrate la transazione tramite il pulsante "*Save Transaction*" su Sparrow, quindi trasferite la scheda in una porta della vostra COLDCARD.

![CCQ](assets/fr/073.webp)

Accedere quindi al menu "*Pronto a firmare*".

![CCQ](assets/fr/074.webp)

Esaminate i dettagli della transazione sulla vostra COLDCARD, compreso l'indirizzo del destinatario, l'importo inviato e la commissione della transazione.

![CCQ](assets/fr/075.webp)

Se tutto è corretto, premere il pulsante "*INVIO*" per firmare la transazione.

![CCQ](assets/fr/076.webp)

Quindi rimettete la microSD nel computer e su Sparrow fate clic su "*Carica transazione*" per caricare la transazione firmata dalla microSD. Sarà quindi possibile eseguire un controllo finale prima di caricarla sulla rete Bitcoin.

![CCQ](assets/fr/077.webp)

Il secondo metodo di firma con la COLDCARD in Air-Gap, molto più semplice di quello con la microSD, consiste nello scansionare il PSBT direttamente tramite la fotocamera del dispositivo. Su Sparrow, selezionare "*Mostra QR*".

![CCQ](assets/fr/078.webp)

Sulla COLDCARD, selezionare "*Scansione di qualsiasi codice QR*". È anche possibile utilizzare il tasto "*QR*" sulla tastiera.

![CCQ](assets/fr/079.webp)

Utilizzate la fotocamera della COLDCARD per scansionare il codice QR visualizzato su Sparrow.

![CCQ](assets/fr/080.webp)

I dettagli della transazione appariranno di nuovo per la verifica. Premere "*INVIO*" per firmare se tutto è di vostro gradimento.

![CCQ](assets/fr/081.webp)

La COLDCARD visualizzerà quindi la transazione firmata come codice QR. Utilizzate la webcam del vostro computer per scansionare questo codice QR selezionando "*Scan QR*" su Sparrow.

![CCQ](assets/fr/082.webp)

La transazione firmata è ora visibile su Sparrow. Controllate un'ultima volta che tutto sia corretto, quindi fate clic su "*Transazione trasmessa*" per trasmettere la transazione sulla rete Bitcoin.

![CCQ](assets/fr/083.webp)

È possibile seguire la transazione nella scheda "*Transazioni*" di Sparrow Wallet.

![CCQ](assets/fr/084.webp)

Congratulazioni, ora siete al corrente dell'uso di base di COLDCARD Q con Sparrow Wallet!

Se avete trovato utile questo tutorial, vi sarei molto grato se lasciaste un pollice verde qui sotto. Non esitate a condividere questo tutorial sui vostri social network. Grazie mille!

Vi consiglio anche di dare un'occhiata a quest'altra esercitazione in cui si parla delle opzioni avanzate della COLDCARD Q :

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
---
name: Jade Plus - Green
description: Configura facilmente Jade Plus con Green
---
![cover](assets/cover.webp)

Jade Plus è un Hardware wallet specifico per bitcoin progettato da Blockstream. È il successore del classico Jade, con miglioramenti del software, più opzioni e un'ergonomia ridisegnata per un uso più intuitivo. Questa nuova versione vanta un magnifico schermo LCD da 1,9 pollici, con una gamma di colori più ampia rispetto al suo predecessore. Anche i pulsanti e la navigazione nei menù sono stati ottimizzati.

Jade Plus può essere utilizzato in diversi modi: tramite una connessione cablata USB-C, in modalità "*Air-Gap*" con una scheda micro SD (è necessario un adattatore), tramite Bluetooth o anche scambiando [codici QR](https://planb.network/resources/glossary/qr-code) grazie alla fotocamera integrata. Questo Hardware wallet è alimentato a batteria.

È disponibile a partire da 149,99 dollari nella versione nera di base, e il prezzo può salire fino a 20 dollari per le versioni "*Genesis Grey*" o "*Lunar Silver*". Jade Plus è quindi una scelta interessante, con funzionalità avanzate paragonabili a quelle degli Hardware wallet di fascia alta come Coldcard Q o Passport V2, ma ad un prezzo piuttosto basso, vicino ai modelli di fascia media.

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus è compatibile con la maggior parte dei software di gestione dei wallet. Ecco un riepilogo della compatibilità al momento della stesura del presente documento (gennaio 2025):

| Management Software  | Desktop | Mobile | USB | Bluetooth   | QR  | JadeLink |
| -------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green    | 🟢      | 🟢     | 🟢  | 🟢 (Mobile) | 🟢  | 🔴       |
| Liana                | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Sparrow              | 🟢      | 🔴     | 🟢  | 🔴          | 🟢  | 🟢       |
| Nunchuk              | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Specter              | 🟢      | 🔴     | 🔴  | 🔴          | 🟢  | 🟢       |
| Bluewallet           | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Electrum             | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Keeper               | 🔴      | 🟢     | 🔴  | 🔴          | 🟢  | 🔴       |

In questo tutorial, configuriamo e utilizziamo Jade Plus con l'applicazione mobile Green wallet di Blockstream tramite una connessione Bluetooth. Questa configurazione è ideale per i principianti. Se sei alla ricerca di un approccio più avanzato, ti consiglio di dare un'occhiata a quest'altro tutorial in cui utilizziamo Jade Plus con Sparrow mediante Codice QR:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Il modello di sicurezza Jade Plus

Jade Plus utilizza un modello di sicurezza basato su un "elemento di sicurezza virtuale", reso concreto da un "blind oracle". In pratica, questo meccanismo combina il PIN scelto dall'utente, un segreto ospitato sul dispositivo Jade e un segreto detenuto dall'oracle (un server gestito da Blockstream), per creare una chiave AES-256 distribuita su due entità. Durante l'avvio, uno scambio [ECDH](https://planb.network/resources/glossary/ecdh) protegge la comunicazione con l'oracle e cripta la [frase mnemonica](https://planb.network/resources/glossary/recovery-phrase) sull'Hardware wallet. In termini pratici, quando si vuole accedere al seed per firmare le transazioni, è necessario accedere a:


- Dispositivo Jade Plus stesso;
- PIN per sbloccare il dispositivo;
- segreto dell'oracle.

Il vantaggio principale di questo approccio è l'assenza di un singolo punto di fallimento a livello Hardware, poiché se un aggressore riesce ad accedere al tuo Jade, per estrarre le chiavi è necessario compromettere contemporaneamente il Jade e l'oracle. Questo modello significa anche che Jade Plus è interamente open-source, evitando i vincoli associati all'uso di veri e propri elementi fisici sicuri, come quelli utilizzati su Ledger, ad esempio.

Lo svantaggio di questo sistema è che l'uso di Jade Plus dipende dall'oracle gestito da Blockstream. Se questo oracle diventa inaccessibile, non è più possibile utilizzare l'Hardware wallet direttamente con il PIN. Tuttavia, questo non significa che i bitcoin siano persi, poiché possono ancora essere recuperati utilizzando la frase mnemonica, che puoi inserire in Jade Plus in modalità "*stateless*". Per aggirare questa dipendenza, puoi anche configurare e gestire il tuo server oracle.

## Unboxing di Jade Plus

Quando ricevi Jade Plus, verifica che la scatola e il sigillo siano in buone condizioni per assicurarti che la confezione non sia stata aperta.

![JADE-PLUS-GREEN](assets/fr/02.webp)

Nella confezione trovi:


- Jade Plus;
- Cavo USB-C;
- Schede per registrare la frase mnemonica come parole o come "*CompactSeedQR*";
- Alcune istruzioni per l'uso;
- Alcuni adesivi.

![JADE-PLUS-GREEN](assets/fr/03.webp)

Il dispositivo dispone di 4 pulsanti di navigazione:


- Il pulsante in basso a destra accende Jade;
- Il pulsante grande sulla parte anteriore del dispositivo serve a selezionare una voce di menù;
- I due piccoli pulsanti in alto consentono di navigare a destra e a sinistra;
- Puoi selezionare un elemento anche facendo clic contemporaneamente sui due pulsanti nella parte superiore del dispositivo.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Impostazione di un nuovo wallet

Fai clic sul pulsante di avvio.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Fai clic su "*Setup Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Scegli "*Begin Setup*". L'opzione "*Advanced Setup*" fa la stessa cosa, ma con accesso alle impostazioni avanzate.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Clicca quindi su "*Create a New wallet*" per generare un nuovo seed.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Fai clic sul pulsante "*Continue*" per visualizzare la nuova frase mnemonica.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Jade Plus ti mostra la frase mnemonica di 12 parole. **Questa frase mnemonica fornisce accesso completo e illimitato a tutti i tuoi bitcoin.** Chiunque sia in possesso di questa frase può rubare i tuoi fondi, anche senza accedere fisicamente al tuo Jade Plus. La frase di 12 parole ripristina l'accesso ai bitcoin in caso di perdita, furto o rottura del Jade. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.

Puoi scriverlo sul cartoncino fornito nella scatola, oppure, per maggiore sicurezza, ti consiglio di inciderlo su una base in acciaio inossidabile per proteggerlo da incendi, allagamenti o crolli.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Per ulteriori informazioni sul modo corretto di salvare e gestire la frase mnemonica, ti consiglio di seguire quest'altro tutorial, soprattutto se sei un principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Ovviamente, non devi mai condividere queste parole su Internet, come faccio io in questo tutorial. Questo wallet di esempio sarà utilizzato solo su Testnet e sarà cancellato alla fine del tutorial***

Fai clic sulla freccia a destra dello schermo per visualizzare le seguenti parole.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Una volta che hai salvato la frase, Jade Plus chiede di confermarla. Seleziona la parola corretta in base all'ordine utilizzando i pulsanti nella parte superiore del dispositivo e fai clic sul pulsante centrale per passare alla parola successiva.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Collegamento di Jade Plus a Green

In questo tutorial, utilizzeremo l'applicazione Green per gestire il wallet inserito su Jade Plus. Questo metodo è particolarmente adatto per i principianti. Se desideri gestire il tuo wallet Bitcoin in modo più dettagliato, puoi anche utilizzare Sparrow, che tratteremo in un tutorial separato:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Per le istruzioni sull'installazione e la configurazione dell'applicazione Blockstream Green, consulta la prima parte di quest'altro tutorial:

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Una volta entrato su Green, clicca sul pulsante "*Configure a new wallet*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Seleziona "*On Hardware wallet*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Attiva il Bluetooth sullo smartphone, quindi fai clic sul pulsante "*Connect your Jade*".

![JADE-PLUS-GREEN](assets/fr/15.webp)

Autorizza l'applicazione Green ad accedere alle connessioni Bluetooth.

![JADE-PLUS-GREEN](assets/fr/16.webp)

L'applicazione sta cercando il tuo Jade Plus.

![JADE-PLUS-GREEN](assets/fr/17.webp)

Su Jade Plus, fai clic sul menù "*Bluetooth*".

![JADE-PLUS-GREEN](assets/fr/18.webp)

Seleziona il tuo dispositivo su Green.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Conferma il codice di accoppiamento su Jade Plus.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green offre un test per verificare che il tuo Jade sia autentico. Clicca sul pulsante per farlo.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Conferma su Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Il colore verde conferma che il dispositivo è autentico.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Impostazione del codice PIN

Fai clic sul pulsante "*Continue*" per scegliere il codice PIN di Jade.

![JADE-PLUS-GREEN](assets/fr/24.webp)

Il codice PIN sblocca il tuo Jade. È quindi una protezione contro l'accesso fisico non autorizzato. Il codice PIN non è necessario per la creazione delle chiavi crittografiche del wallet. Pertanto, anche senza accesso a questo codice PIN, il possesso della frase mnemonica di 12 parole ti permetterà di riavere accesso ai tuoi bitcoin. Ti consiglio di scegliere un codice PIN il più possibile casuale. E assicurati di salvare questo codice in un luogo separato da quello in cui conservi il tuo Jade (ad esempio, in un gestore di password).

Scegli il codice PIN a 6 cifre sul tuo Jade, utilizzando i pulsanti destro e sinistro per scorrere le cifre e il pulsante centrale per confermare l'inserimento di una cifra.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Conferma il PIN una seconda volta.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Il tuo wallet è stato creato.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Creare un account Bitcoin

A questo punto è necessario creare un account all'interno del tuo wallet. Fai clic sul pulsante "*Create an account*".

![JADE-PLUS-GREEN](assets/fr/28.webp)

Scegli "*Standard*" se desideri creare un wallet classico a firma singola.

![JADE-PLUS-GREEN](assets/fr/29.webp)

Per ulteriori informazioni sull'opzione "*2FA*", puoi seguire quest'altra guida:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Il tuo account è stato creato.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Se desideri personalizzare il tuo Green wallet, clicca sui tre puntini in alto a destra.

![JADE-PLUS-GREEN](assets/fr/31.webp)

L'opzione "*Name*" consente di personalizzare il nome del wallet, particolarmente utile se gestisci diversi wallet sulla stessa applicazione. Il menù "*Unit*" consente di modificare l'unità di base del wallet. Ad esempio, puoi scegliere di visualizzarlo in satoshi anziché in bitcoin. Infine, il menù "*Parameters*" consente di accedere ad altre opzioni. Qui, ad esempio, trovi la tua chiave pubblica estesa e il suo descriptor, utile se intendi creare un wallet di sola lettura sul tuo Jade.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Per ricollegarti a Jade dopo averlo spento, premi il pulsante di accensione/spegnimento nella parte inferiore del dispositivo. Sull'applicazione Green, seleziona il dispositivo dalla pagina iniziale:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Inserisci quindi il codice PIN sul tuo Jade e sarai nuovamente connesso.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Il tuo Jade viene sbloccato tramite il "virtual secure element" di Blockstream (vedi la prima sezione di questo tutorial). Ciò richiede una connessione Bluetooth con l'applicazione Green. Se incontri difficoltà con la connessione Bluetooth durante lo sblocco, prova a dissociare e riassociare i due dispositivi. Se il problema persiste, puoi comunque sbloccare il tuo Jade selezionando l'opzione "*QR Scan*" e seguendo le istruzioni disponibili [sul sito web di Blockstream](https://jadefw.blockstream.com/pinqr/index.html).

Prima di ricevere i primi bitcoin nel wallet, **ti consiglio vivamente di eseguire un test di ripristino con il wallet ancora vuoto**. Annota alcune informazioni di riferimento, come il tuo indirizzo xpub o il primo indirizzo di ricezione, quindi cancella il tuo wallet sull'app Green e su Jade Plus mentre è ancora vuoto (`Opzioni -> Dispositivo -> Ripristino dati di fabbrica`). A questo punto prova a ripristinare il wallet utilizzando i backup cartacei della frase mnemonica. Verifica che le informazioni del cookie generate dopo il ripristino corrispondano a quelle annotate in origine. Se è così, puoi esser certo che i tuoi backup cartacei sono affidabili. Per saperne di più su come effettuare un ripristino di prova, consulta quest'altro tutorial:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Ricevere bitcoin

Ora che il tuo wallet Bitcoin è stato configurato, sei pronto a ricevere i tuoi primi satoshi! Basta cliccare sul pulsante "*Receive*" nell'applicazione Green.

![JADE-PLUS-GREEN](assets/fr/35.webp)

Green visualizza un indirizzo di ricezione, ma prima di utilizzarlo è essenziale verificarlo su Jade per confermare che appartenga effettivamente al tuo wallet. A tal fine, fai clic sul pulsante "*Verify on device*".

![JADE-PLUS-GREEN](assets/fr/36.webp)

Verifica su Jade che l'indirizzo sia lo stesso di Green, quindi fai clic sul pulsante per confermare.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Ora puoi condividere l'indirizzo con il destinatario per ricevere bitcoin nel tuo wallet. Quando la transazione viene trasmessa alla rete, appare nel tuo wallet. Aspetta di ricevere un numero sufficiente di conferme per considerare la transazione confermata.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Inviare bitcoin

Con i bitcoin nel tuo wallet, ora puoi anche inviare bitcoin. Per farlo, clicca su "*Send*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

Nella pagina successiva, inserisci l'indirizzo del destinatario. È possibile inserirlo manualmente o scansionare un codice QR.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Scegli l'importo del pagamento.

![JADE-PLUS-GREEN](assets/fr/41.webp)

Nella parte inferiore della schermata puoi selezionare la fee per questa transazione. Puoi scegliere se seguire le raccomandazioni dell'applicazione o personalizzare la fee. Più alta è la fee rispetto alle altre transazioni in corso, più veloce sarà l'elaborazione della transazione. Per informazioni sull'andamento delle commissioni, visita [Mempool.space](https://mempool.space/) nella sezione "*Transaction Fees*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Clicca su "*Avanti*" per accedere alla schermata di riepilogo della transazione. Verifica che l'indirizzo, l'importo e la fee siano corretti.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Se tutto va bene, fai scorrere verso destra il pulsante verde in fondo allo schermo per firmare e trasmettere la transazione sulla rete Bitcoin.

![JADE-PLUS-GREEN](assets/fr/44.webp)

A questo punto ti verrà chiesto di confermare la transazione su Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Assicurati che l'indirizzo del destinatario sia corretto. Fai clic sul segno di spunta per confermare.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Verifica che l'importo dell'addebito sia corretto, quindi conferma.

![JADE-PLUS-GREEN](assets/fr/47.webp)

La transazione è stata firmata e trasmessa da Green.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Congratulazioni, ora sai come configurare e utilizzare Jade Plus con l'applicazione mobile Blockstream Green, tramite connessione Bluetooth. Se questa guida è stata utile, ti sarei grato se lasciassi un pollice verde qui sotto. Sentiti libero di condividere questo articolo sui tuoi social network. Grazie per la condivisione!

Per fare un ulteriore passo avanti, ti consiglio questo tutorial su Jade Plus, in cui lo configuriamo con il software Sparrow usando il codice QR. Imparerai anche ad utilizzare le impostazioni avanzate del tuo Hardware wallet:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262


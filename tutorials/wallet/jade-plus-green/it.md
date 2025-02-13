---
name: Giada Plus - Verde
description: Configurare facilmente Jade Plus con Green
---
![cover](assets/cover.webp)

Jade Plus è un portafoglio hardware per soli Bitcoin progettato da Blockstream. È il successore del classico Jade, con miglioramenti del software, più opzioni e un'ergonomia ridisegnata per un uso più intuitivo. Questa nuova versione vanta un magnifico schermo LCD da 1,9 pollici, con una gamma di colori più ampia rispetto al suo predecessore. Anche i pulsanti e la navigazione nei menu sono stati ottimizzati.

Jade Plus può essere utilizzato in diversi modi: tramite una connessione cablata USB-C, in modalità "*Air-Gap*" con una scheda micro SD (è necessario un adattatore), tramite Bluetooth o anche scambiando codici QR grazie alla fotocamera integrata. Questo portafoglio hardware è alimentato a batteria.

È disponibile a partire da 149,99 dollari nella versione nera di base, e il prezzo può salire fino a 20 dollari per le versioni "*Genesis Grey*" o "*Lunar Silver*". Il Jade Plus è quindi una scelta interessante, con funzionalità avanzate paragonabili a quelle dei portafogli hardware di fascia alta come Coldcard Q o Passport V2, ma a un prezzo piuttosto basso, vicino ai modelli di fascia media.

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus è compatibile con la maggior parte dei software di gestione del portafoglio. Ecco un riepilogo della compatibilità al momento della stesura del presente documento (gennaio 2025):

| Desktop | Mobile | USB | Bluetooth | QR | JadeLink | Software di gestione

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

passero | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢

nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 |

specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢

blueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴

custode | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 |

In questo tutorial, configureremo e utilizzeremo Jade Plus con l'applicazione mobile Green Wallet di Blockstream tramite una connessione Bluetooth. Questa configurazione è ideale per i principianti. Se siete alla ricerca di un approccio più avanzato, vi consiglio di dare un'occhiata a questo tutorial in cui utilizziamo Jade Plus con Sparrow Wallet in modalità codici QR:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
## Il modello di sicurezza Jade Plus

Jade Plus utilizza un modello di sicurezza basato su un "elemento sicuro virtuale", materializzato da un "oracolo cieco". In concreto, questo meccanismo combina il PIN scelto dall'utente, un segreto ospitato sul Jade e un segreto detenuto dall'oracolo (un server gestito da Blockstream), per creare una chiave AES-256 distribuita su due entità. Durante l'avvio, uno scambio ECDH protegge la comunicazione con l'oracolo e cripta la frase di recupero sul portafoglio hardware. In termini pratici, quando si vuole accedere al seed per firmare le transazioni, è necessario accedere a :


- Al dispositivo Jade Plus stesso;
- PIN per sbloccare il dispositivo ;
- E al segreto dell'oracolo.

Il vantaggio principale di questo approccio è l'assenza di un singolo punto di guasto a livello hardware, poiché se un aggressore riesce ad accedere al vostro Jade, per estrarre le chiavi è necessario compromettere contemporaneamente il Jade e l'oracolo. Questo modello significa anche che Jade Plus è interamente open-source, evitando i vincoli associati all'uso di veri e propri elementi fisici sicuri, come quelli utilizzati su Ledger, ad esempio.

Lo svantaggio di questo sistema è che l'uso di Jade Plus dipende dall'oracolo gestito da Blockstream. Se questo oracolo diventa inaccessibile, non è più possibile utilizzare il portafoglio hardware direttamente con il PIN. Tuttavia, questo non significa che i bitcoin siano persi, poiché possono ancora essere recuperati utilizzando la frase di recupero, che è possibile inserire in Jade Plus in modalità "*stateless*". Per aggirare questa dipendenza, è anche possibile configurare e gestire il proprio server oracle.

## Unboxing del Jade Plus

Quando si riceve Jade Plus, verificare che la scatola e il sigillo siano in buone condizioni per assicurarsi che la confezione non sia stata aperta.

![JADE-PLUS-GREEN](assets/fr/02.webp)

Nella confezione troverete :


- Le Jade Plus;
- Cavo USB-C;
- Schede per registrare la frase mnemonica come parole o come "*CompactSeedQR*";
- Alcune istruzioni per l'uso ;
- Una corda;
- Alcuni adesivi.

![JADE-PLUS-GREEN](assets/fr/03.webp)

Il dispositivo dispone di 4 pulsanti di navigazione:


- Il pulsante in basso a destra accende il Jade;
- Il pulsante grande sulla parte anteriore del dispositivo serve a selezionare una voce;
- I due piccoli pulsanti in alto consentono di navigare a destra e a sinistra;
- È possibile selezionare un elemento anche facendo clic contemporaneamente sui due pulsanti nella parte superiore del dispositivo.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Impostazione di un nuovo portafoglio Bitcoin

Fare clic sul pulsante di avvio.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Fare clic su "*Impostazione di Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Scegliere "Iniziare la configurazione". L'opzione "*Configurazione avanzata*" fa la stessa cosa, ma con accesso alle impostazioni avanzate.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Cliccare quindi su "*Crea un nuovo portafoglio*" per generare un nuovo seme.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Fare clic sul pulsante "*Continua*" per visualizzare la nuova frase di recupero.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Jade Plus visualizza la frase mnemonica di 12 parole. **Questa frase mnemonica vi dà accesso completo e illimitato a tutti i vostri bitcoin. Chiunque sia in possesso di questa frase può rubare i vostri fondi, anche senza accedere fisicamente al vostro Jade Plus. La frase di 12 parole ripristina l'accesso ai bitcoin in caso di perdita, furto o rottura del Jade. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.

Potete scriverlo sul cartoncino fornito nella scatola, oppure, per maggiore sicurezza, vi consiglio di inciderlo su una base in acciaio inossidabile per proteggerlo da incendi, allagamenti o crolli.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Per ulteriori informazioni sul modo corretto di salvare e gestire la frase mnemonica, vi consiglio di seguire quest'altro tutorial, soprattutto se siete principianti:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
***Ovviamente, non dovete mai condividere queste parole su Internet, come faccio io in questo tutorial. Questo portfolio di esempio sarà utilizzato solo su Testnet e sarà cancellato alla fine del tutorial

Fate clic sulla freccia a destra dello schermo per visualizzare le seguenti parole.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Una volta salvata la frase, Jade Plus chiede di confermarla. Selezionare la parola corretta in base all'ordine utilizzando i pulsanti nella parte superiore del dispositivo e fare clic sul pulsante centrale per passare alla parola successiva.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Collegamento di Jade Plus a Green Wallet

In questa esercitazione, utilizzeremo l'applicazione Green Wallet per gestire il portafoglio ospitato su Jade Plus. Questo metodo è particolarmente adatto ai principianti. Se desiderate gestire il vostro portafoglio Bitcoin in modo più dettagliato, potete anche utilizzare Sparrow Wallet, che tratteremo in un tutorial separato:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
Per le istruzioni sull'installazione e la configurazione dell'applicazione Blockstream Green, consultare la prima parte di quest'altro tutorial:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
Una volta entrati nell'applicazione Blockstream Green, cliccate sul pulsante "*Configura un nuovo portafoglio*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Selezionare "*Sul portafoglio hardware*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Attivare il Bluetooth sullo smartphone, quindi fare clic sul pulsante "*Connetti il tuo Jade*".

![JADE-PLUS-GREEN](assets/fr/15.webp)

Autorizzare l'applicazione Green ad accedere alle connessioni Bluetooth.

![JADE-PLUS-GREEN](assets/fr/16.webp)

L'applicazione sta cercando il vostro Jade Plus.

![JADE-PLUS-GREEN](assets/fr/17.webp)

Su Jade Plus, fare clic sul menu "*Bluetooth*".

![JADE-PLUS-GREEN](assets/fr/18.webp)

Selezionate il vostro dispositivo nell'applicazione Verde.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Confermare il codice di accoppiamento su Jade Plus.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green vi offre un test per verificare che la vostra Giada sia autentica. Cliccate sul pulsante per farlo.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Confermare sulla Giada.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Il colore verde conferma che il dispositivo è autentico.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Impostazione del codice PIN

Fare clic sul pulsante "*Continua*" per scegliere il codice PIN di Jade.

![JADE-PLUS-GREEN](assets/fr/24.webp)

Il codice PIN sblocca il vostro Jade. È quindi una protezione contro l'accesso fisico non autorizzato. Il codice PIN non partecipa alla creazione delle chiavi crittografiche del portafoglio. Pertanto, anche senza accesso a questo codice PIN, il possesso della frase mnemonica di 12 parole vi permetterà di riavere accesso ai vostri bitcoin. Si consiglia di scegliere un codice PIN il più possibile casuale. E assicuratevi di salvare questo codice in un luogo separato da quello in cui è memorizzato il vostro Jade (ad esempio, in un gestore di password).

Scegliete il codice PIN a 6 cifre sul vostro Jade, utilizzando i pulsanti destro e sinistro per scorrere le cifre e il pulsante centrale per confermare l'inserimento di una cifra.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Confermare il PIN una seconda volta.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Il vostro portafoglio bitcoin è stato creato.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Creare un conto Bitcoin

A questo punto è necessario creare un account all'interno del proprio portafoglio. Fare clic sul pulsante "*Crea un account*".

![JADE-PLUS-GREEN](assets/fr/28.webp)

Scegliere "*Standard*" se si desidera creare un portafoglio classico a sigla singola.

![JADE-PLUS-GREEN](assets/fr/29.webp)

Per ulteriori informazioni sull'opzione "*2FA*", potete seguire quest'altra guida:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2FA-37397d5c-5c27-44ad-a27a-c9ceac8c9df9
Il vostro account è stato creato.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Se desiderate personalizzare il vostro portafoglio verde, cliccate sui tre puntini in alto a destra.

![JADE-PLUS-GREEN](assets/fr/31.webp)

L'opzione "*Nome*" consente di personalizzare il nome del portafoglio, particolarmente utile se si gestiscono diversi portafogli sulla stessa applicazione. Il menu "*Unità*" consente di modificare l'unità di base del portafoglio. Ad esempio, si può scegliere di visualizzarlo in satoshi anziché in bitcoin. Infine, il menu "*Parametri*" consente di accedere ad altre opzioni. Qui, ad esempio, troverete la vostra chiave pubblica estesa e il suo descrittore, utile se intendete creare un portafoglio di soli orologi dal vostro Jade.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Per ricollegarsi a Jade dopo averlo spento, premere il pulsante di accensione/spegnimento nella parte inferiore del dispositivo. Nell'applicazione Green, selezionare il dispositivo dalla pagina iniziale:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Inserite quindi il codice PIN sul vostro Jade e sarete nuovamente connessi.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Il vostro Jade viene sbloccato tramite il "virtual secure element" di Blockstream (vedere la prima sezione di questa guida). Ciò richiede una connessione Bluetooth con l'applicazione Green. Se si incontrano difficoltà con la connessione Bluetooth durante lo sblocco, provare a dissociare e riassociare i due dispositivi. Se il problema persiste, potete comunque sbloccare il vostro Jade selezionando l'opzione "*QR Scan*" e seguendo le istruzioni disponibili [sul sito web di Blockstream](https://jadefw.blockstream.com/pinqr/index.html).

Prima di ricevere i primi bitcoin nel portafoglio, **consiglio vivamente di eseguire un test di ripristino a vuoto**. Annotate alcune informazioni di riferimento, come il vostro indirizzo xpub o il primo indirizzo di ricezione, quindi cancellate il vostro portafoglio sull'app Green e su Jade Plus mentre è ancora vuoto (`Opzioni -> Dispositivo -> Ripristino dati di fabbrica`). Quindi provare a ripristinare il portafoglio utilizzando i backup cartacei della frase mnemonica. Verificare che le informazioni del cookie generate dopo il ripristino corrispondano a quelle annotate in origine. Se è così, potete essere certi che i vostri backup cartacei sono affidabili. Per saperne di più su come effettuare un ripristino di prova, consultate quest'altro tutorial:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Ricevere bitcoin

Ora che il vostro portafoglio Bitcoin è stato configurato, siete pronti a ricevere i vostri primi satelliti! Basta cliccare sul pulsante "*Ricevi*" nell'applicazione Green.

![JADE-PLUS-GREEN](assets/fr/35.webp)

Il verde visualizza un indirizzo di ricezione, ma prima di utilizzarlo è essenziale verificarlo su Jade per confermare che appartenga effettivamente al nostro portafoglio. A tal fine, fare clic sul pulsante "*Verifica sul dispositivo*".

![JADE-PLUS-GREEN](assets/fr/36.webp)

Verificare su Jade che l'indirizzo sia lo stesso di Green, quindi fare clic sul pulsante per confermare.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Ora è possibile condividere l'indirizzo con l'ordinante per ricevere bitcoin nel proprio portafoglio. Quando la transazione viene trasmessa alla rete, appare nel vostro portafoglio. Aspettate di ricevere un numero sufficiente di conferme per considerare la transazione definitiva.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Inviare bitcoin

Con i bitcoin nel vostro portafoglio, ora potete anche inviare bitcoin. Cliccate su "*Invio*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

Nella pagina successiva, inserire l'indirizzo del destinatario. È possibile inserirlo manualmente o scansionare un codice QR.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Scegliere l'importo del pagamento.

![JADE-PLUS-GREEN](assets/fr/41.webp)

Nella parte inferiore della schermata è possibile selezionare la tariffa per questa transazione. È possibile scegliere se seguire le raccomandazioni dell'applicazione o personalizzare le commissioni. Più alta è la tariffa rispetto alle altre transazioni in corso, più veloce sarà l'elaborazione della transazione. Per informazioni sul mercato delle commissioni, visitare [Mempool.space](https://mempool.space/) nella sezione "*Transaction Fees*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Cliccare su "*Avanti*" per accedere alla schermata di riepilogo della transazione. Verificare che l'indirizzo, l'importo e le spese siano corretti.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Se tutto va bene, fate scorrere verso destra il pulsante verde in fondo allo schermo per firmare e trasmettere la transazione sulla rete Bitcoin.

![JADE-PLUS-GREEN](assets/fr/44.webp)

A questo punto vi verrà chiesto di confermare la transazione su Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Assicurarsi che l'indirizzo del destinatario sia corretto. Fare clic sul segno di spunta per confermare.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Verificare che l'importo dell'addebito sia corretto, quindi convalidare.

![JADE-PLUS-GREEN](assets/fr/47.webp)

La transazione è stata firmata e trasmessa da Green.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Congratulazioni, ora sapete come configurare e utilizzare Jade Plus con l'applicazione mobile Blockstream Green, tramite connessione Bluetooth. Se questa guida vi è stata utile, vi sarei grato se lasciaste un pollice verde qui sotto. Sentitevi liberi di condividere questo articolo sui vostri social network. Grazie per la condivisione!

Per fare un ulteriore passo avanti, vi consiglio questo tutorial su Jade Plus, in cui lo configuriamo con il software Sparrow Wallet in modalità QR. Imparerete anche a utilizzare le impostazioni avanzate del vostro portafoglio hardware:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
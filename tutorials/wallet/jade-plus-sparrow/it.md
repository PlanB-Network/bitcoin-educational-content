---
name: Jade Plus - Passero
description: Configurazione avanzata di Jade Plus con Sparrow Wallet
---
![cover](assets/cover.webp)

Jade Plus è un portafoglio hardware per soli Bitcoin progettato da Blockstream. È il successore del classico Jade, con miglioramenti del software, più opzioni e un'ergonomia ridisegnata per un uso più intuitivo. Questa nuova versione vanta un magnifico schermo LCD da 1,9 pollici, con una gamma di colori più ampia rispetto al suo predecessore. Anche i pulsanti e la navigazione nei menu sono stati ottimizzati.

Jade Plus può essere utilizzato in diversi modi: tramite una connessione cablata USB-C, in modalità "*Air-Gap*" con una scheda micro SD (è necessario un adattatore), tramite Bluetooth o anche scambiando codici QR grazie alla fotocamera integrata. Questo portafoglio hardware è alimentato a batteria.

È disponibile a partire da 149,99 dollari nella versione nera di base, e il prezzo può salire fino a 20 dollari per le versioni "*Genesis Grey*" o "*Lunar Silver*". Il Jade Plus è quindi una scelta interessante, con funzionalità avanzate paragonabili a quelle dei portafogli hardware di fascia alta come Coldcard Q o Passport V2, ma a un prezzo piuttosto basso, vicino ai modelli di fascia media.

![JADE-PLUS-SPARROW](assets/fr/01.webp)

Jade Plus è compatibile con la maggior parte dei software di gestione del portafoglio. Ecco un riepilogo della compatibilità al momento della stesura del presente documento (gennaio 2025):

| Desktop | Mobile | USB | Bluetooth | QR | JadeLink | Software di gestione

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

passero | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢

nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢

specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢

blueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴

custode | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 |

In questa esercitazione, imposteremo una configurazione avanzata di Jade Plus con il software desktop Sparrow Wallet in modalità codici QR. Questa configurazione è ideale per utenti intermedi o esperti. Se cercate un approccio più semplice per i principianti, vi consiglio di dare un'occhiata a questa esercitazione in cui utilizziamo Jade Plus con Green Wallet tramite una connessione Bluetooth:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0
## Il modello di sicurezza Jade Plus

Jade Plus utilizza un modello di sicurezza basato su un "elemento sicuro virtuale", materializzato da un "oracolo cieco". In concreto, questo meccanismo combina il PIN scelto dall'utente, un segreto ospitato sul Jade e un segreto detenuto dall'oracolo (un server gestito da Blockstream), per creare una chiave AES-256 distribuita su due entità. Durante l'avvio, uno scambio ECDH protegge la comunicazione con l'oracolo e cripta la frase di recupero sul portafoglio hardware. In termini pratici, quando si vuole accedere al seed per firmare le transazioni, è necessario accedere a :


- Il dispositivo Jade Plus stesso;
- PIN per sbloccare il dispositivo ;
- E al segreto dell'oracolo.

Il vantaggio principale di questo approccio è l'assenza di un singolo punto di guasto a livello hardware, poiché se un aggressore riesce ad accedere al vostro Jade, per estrarre le chiavi è necessario compromettere contemporaneamente il Jade e l'oracolo. Questo modello significa anche che Jade Plus è interamente open-source, evitando i vincoli associati all'uso di veri e propri elementi fisici sicuri, come quelli utilizzati su Ledger, ad esempio.

Lo svantaggio di questo sistema è che l'uso di Jade Plus dipende dall'oracolo gestito da Blockstream. Se questo oracolo diventa inaccessibile, non è più possibile utilizzare il portafoglio hardware direttamente con il PIN. Tuttavia, questo non significa che i bitcoin siano persi, poiché possono ancora essere recuperati utilizzando la frase di recupero, che è possibile inserire in Jade Plus in modalità "*stateless*". Per aggirare questa dipendenza, è anche possibile configurare e gestire il proprio server oracle.

Un'altra opzione per gestire i semi è semplicemente quella di non registrarli su Jade Plus. In questo caso, il Jade diventa solo un dispositivo di firma. Durante l'inizializzazione, oltre al consueto salvataggio della frase di recupero sotto forma di parole, la si salverà anche come codice QR generato a mano. In questo modo, ogni volta che si utilizza il portafoglio, è possibile importare il seme utilizzando la fotocamera del Jade. Questa può essere un'opzione interessante per gli utenti avanzati, a seconda della vostra strategia di sicurezza, ma dovete fare attenzione sia a salvare il seme che a proteggerlo, perché anche come codice QR permetterebbe a chiunque di rubare i vostri fondi. In questo tutorial esamineremo questa opzione, ma non è obbligatoria.

## Unboxing del Jade Plus

Quando si riceve Jade Plus, verificare che la scatola e il sigillo siano in buone condizioni per assicurarsi che la confezione non sia stata aperta.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

Nella confezione troverete :


- Le Jade Plus;
- Cavo USB-C;
- Schede per registrare la frase mnemonica come parole o come "*CompactSeedQR*";
- Alcune istruzioni per l'uso ;
- Una corda;
- Alcuni adesivi.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

Il dispositivo dispone di 4 pulsanti di navigazione:


- Il pulsante in basso a destra accende il Jade;
- Il pulsante grande sulla parte anteriore del dispositivo serve a selezionare una voce;
- I due piccoli pulsanti in alto consentono di navigare a destra e a sinistra;
- È possibile selezionare un elemento anche facendo clic contemporaneamente sui due pulsanti nella parte superiore del dispositivo.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Impostazione di un nuovo portafoglio Bitcoin

Fare clic sul pulsante di avvio.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Fare clic su "*Impostazione di Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Selezionare "Impostazione avanzata*".

![Image](assets/fr/07.webp)

Cliccate quindi su "*Crea un nuovo portafoglio*" per generare un nuovo seme. È possibile scegliere tra una frase mnemonica di 12 o 24 parole. La sicurezza del vostro portafoglio rimane equivalente con entrambe le opzioni, quindi potrebbe essere più conveniente scegliere l'opzione più semplice da salvare, cioè 12 parole.

![Image](assets/fr/08.webp)

Fare clic sul pulsante "*Continua*" per visualizzare la nuova frase di recupero.

![Image](assets/fr/09.webp)

Jade Plus visualizza la frase mnemonica di 12 parole. **Questa frase mnemonica vi dà accesso completo e illimitato a tutti i vostri bitcoin. Chiunque sia in possesso di questa frase può rubare i vostri fondi, anche senza accedere fisicamente al vostro Jade Plus. La frase di 12 parole ripristina l'accesso ai bitcoin in caso di perdita, furto o rottura del Jade. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.

Potete scriverlo sul cartoncino fornito nella scatola, oppure, per maggiore sicurezza, vi consiglio di inciderlo su una base in acciaio inossidabile per proteggerlo da incendi, allagamenti o crolli.

![Image](assets/fr/10.webp)

Per ulteriori informazioni sul modo corretto di salvare e gestire la frase mnemonica, vi consiglio di seguire quest'altro tutorial, soprattutto se siete principianti:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
naturalmente, non dovete mai condividere queste parole su Internet, come sto facendo io in questa esercitazione. Questo portfolio di esempio sarà utilizzato solo su Testnet e sarà cancellato alla fine del tutorial.**_

Fate clic sulla freccia a destra dello schermo per visualizzare le seguenti parole.

![Image](assets/fr/11.webp)

Una volta salvata la frase, Jade Plus chiede di confermarla. Selezionare la parola corretta in base all'ordine utilizzando i pulsanti nella parte superiore del dispositivo e fare clic sul pulsante centrale per passare alla parola successiva.

![Image](assets/fr/12.webp)

A questo punto avete due opzioni. Come spiegato nell'introduzione, potete scegliere di salvare il vostro seme direttamente sul dispositivo e utilizzare il sistema di protezione "*Virtual Secure Element*" di Blockstream per accedere al vostro portafoglio (opzione 1), oppure salvare il vostro seme come codice QR e scansionarlo ogni volta che lo utilizzate (opzione 2).

Per l'opzione 1, selezionare "*No*" e per l'opzione 2, selezionare "*Sì*".

![Image](assets/fr/13.webp)

### Opzione 1: Sblocco con PIN QR

Se si è scelta l'opzione 1 (CompactSeedQR: "*No*"), si passa direttamente alla selezione del metodo di connessione. In questa esercitazione, vogliamo utilizzare il dispositivo in modalità Air-Gap tramite lo scambio di codici QR, quindi selezioniamo "*QR*".

![Image](assets/fr/27.webp)

Fare clic su "*Continua*".

![Image](assets/fr/28.webp)

Il codice PIN viene utilizzato per sbloccare il vostro Jade e offre protezione contro l'accesso fisico non autorizzato. Il codice PIN non partecipa alla creazione delle chiavi crittografiche del portafoglio. Pertanto, anche senza accesso a questo codice PIN, il possesso della frase mnemonica di 12 parole vi permetterà di riavere accesso ai vostri bitcoin. Si consiglia di scegliere un codice PIN il più possibile casuale. Inoltre, assicuratevi di salvare questo codice in un luogo separato da quello in cui è memorizzato il vostro Jade, ad esempio in un gestore di password.

Scegliere un codice PIN a 6 cifre su Jade, utilizzando i pulsanti sinistro e destro per scorrere le cifre e il pulsante centrale per confermare ogni cifra.

![Image](assets/fr/29.webp)

Confermare il PIN una seconda volta.

![Image](assets/fr/30.webp)

Come spiegato nell'introduzione, il seme viene memorizzato in modo criptato su Jade Plus. Per decifrarlo, è necessario fornire :


- Il codice PIN valido (che abbiamo appena impostato) ;
- Il segreto dell'oracolo gestito da Blockstream.

In questa esercitazione avanzata, utilizzeremo Sparrow Wallet per gestire il nostro portafoglio Bitcoin. Tuttavia, a differenza del software Green Wallet di Blockstream, Sparrow non ha accesso all'oracolo sui server di Blockstream. Pertanto, utilizzeremo il sito web di Blockstream per recuperare il segreto dell'oracolo ogni volta che sbloccheremo Jade Plus.

Visitate https://jadefw.blockstream.com/pinqr/index.html

Fare clic su "*Avvia sblocco QR*".

![Image](assets/fr/31.webp)

Fare clic su "*Fatto*", poiché il PIN è già stato scelto su Jade Plus.

![Image](assets/fr/32.webp)

Utilizzare la fotocamera del computer per scansionare i codici QR visualizzati sullo schermo di Jade.

![Image](assets/fr/33.webp)

Confermate sul vostro Jade per accedere alla schermata successiva.

![Image](assets/fr/34.webp)

Scansionate il codice QR ora visibile sul sito web per recuperare il segreto dell'oracolo.

![Image](assets/fr/35.webp)

Ora che il portafoglio è stato creato, si può procedere con le fasi successive e saltare la sottosezione "*Opzione 2: CompactSeedQR*".

![Image](assets/fr/36.webp)

A ogni avvio, fare clic su "*Modalità QR*".

![Image](assets/fr/37.webp)

Selezionare "*Sblocco PIN QR*".

![Image](assets/fr/38.webp)

Inserire il codice PIN.

![Image](assets/fr/39.webp)

Poi andate su [il sito web di Blockstream](https://jadefw.blockstream.com/pinqr/qrpin.html) per scambiare i codici QR con l'oracolo.

![Image](assets/fr/40.webp)

La vostra Giada è ora sbloccata.

![Image](assets/fr/41.webp)

### Opzione 2: CompactSeedQR

Se si è scelta l'opzione 2 (CompactSeedQR: "*Sì*"), cliccare nuovamente su "*Sì*".

![Image](assets/fr/14.webp)

Fare clic su "*Avvio*".

![Image](assets/fr/15.webp)

È possibile utilizzare la base per codice QR fornita nella confezione di Jade Plus. Selezionare la casella appropriata a seconda che si sia optato per una frase di 12 o 24 parole. È anche possibile [stampare il modello dal sito web di Blockstream](https://help.blockstream.com/hc/article_attachments/41928319071769).

Jade Plus visualizzerà ogni zona del codice QR.

![Image](assets/fr/16.webp)

Utilizzare una penna per colorare i quadrati e riprodurre il seme come codice QR. Siate precisi per garantire che la fotocamera di Jade Plus possa scansionarlo in seguito. Utilizzare la freccia per passare all'area successiva.

![Image](assets/fr/17.webp)

Al termine, fare clic su "*Fatto*".

![Image](assets/fr/18.webp)

Scansionare il codice QR fatto a mano con Jade Plus per verificarne la validità.

![Image](assets/fr/19.webp)

Se il backup della carta è corretto, fare clic su "*Continua*".

![Image](assets/fr/20.webp)

In questa esercitazione, utilizzeremo una modalità di connessione basata esclusivamente sulla scansione dei codici QR, quindi selezionate "*QR*".

![Image](assets/fr/21.webp)

Si può anche scegliere di aggiungere un PIN oltre al backup del CompactSeedQR, come nell'opzione 1. Questo offre due modi di accedere al portafoglio: tramite il PIN e il sistema "Virtual Secure Element" di Blockstream, oppure tramite il CompactSeedQR. In questo modo è possibile accedere al portafoglio in due modi: tramite il PIN e il sistema "Virtual Secure Element" di Blockstream, oppure tramite il CompactSeedQR.

Se si sceglie l'opzione del doppio PIN, selezionare "*PIN*" e seguire la stessa procedura dell'opzione 1 per impostare il codice PIN.

Se si preferisce continuare solo con CompactSeedQR, selezionare "*SeedQR*".

![Image](assets/fr/22.webp)

Ora che il vostro portafoglio è stato creato, potete passare alle fasi successive.

![Image](assets/fr/23.webp)

Ad ogni avvio, fare clic sul pulsante "*Modalità QR*", quindi su "*Scan SeedQR*".

![Image](assets/fr/24.webp)

Utilizzare la fotocamera del dispositivo per scansionare il seme salvato come codice QR.

![Image](assets/fr/25.webp)

La vostra Giada è ora sbloccata.

![Image](assets/fr/26.webp)

## Aggiungere una passphrase BIP39

La passphrase BIP39 è una password opzionale che si può scegliere liberamente e che viene aggiunta alla frase mnemonica per rafforzare la sicurezza del portafoglio. Con questa funzione abilitata, l'accesso al portafoglio Bitcoin richiede sia la frase mnemonica che la passphrase. Senza di esse, sarebbe impossibile recuperare il portafoglio.

Prima di configurare questa opzione su Jade Plus, si consiglia vivamente di leggere questo articolo per comprendere appieno il funzionamento teorico della passphrase ed evitare errori che potrebbero portare alla perdita dei bitcoin:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Con Jade ancora bloccato (la passphrase può essere inserita solo quando il dispositivo non è sbloccato), accedere al menu "*Opzioni*".

![Image](assets/fr/42.webp)

Selezionare "*BIP39 Passphrase*".

![Image](assets/fr/43.webp)

Nell'opzione "*Frequenza*", è possibile scegliere se Jade Plus chiederà di inserire la passphrase a ogni avvio:


- "*Disabilitato*" disabilita l'uso di una passphrase;
- l'opzione "*Solo al prossimo accesso*" richiederà di tornare a questo menu per attivare la richiesta della passphrase al prossimo avvio. Questa opzione consente di non rivelarne l'uso;
- l'opzione "Chiedi sempre" fa sì che Jade chieda sistematicamente la passphrase a ogni avvio, rivelando così che il portafoglio è protetto da una passphrase.

Scegliete l'opzione in base alla vostra strategia di sicurezza. Personalmente, seleziono "*Chiedere sempre*" per l'esempio.

![Image](assets/fr/44.webp)

È quindi possibile scegliere tra due metodi di inserimento della passphrase:


- "*Manuale*: Una tastiera virtuale consente di inserire lettere (maiuscole e minuscole), numeri e simboli, carattere per carattere. Questo è il metodo standard per tutti i portafogli hardware;
- "*Elenco di parole*": Metodo specifico progettato da Blockstream per Jade, che velocizza l'inserimento della passphrase e ne aumenta l'entropia. Durante l'inserimento, il sistema suggerisce le parole dell'elenco BIP39, facilitando lo sblocco. Questo metodo genera automaticamente una frase concatenando le parole scelte, separate da spazi (esempio: `abandon ability able`).

Personalmente, vi consiglio di utilizzare il primo metodo, poiché è lo standard che troverete su tutti gli altri supporti di portafoglio.

![Image](assets/fr/45.webp)

È quindi possibile tornare alla schermata iniziale e sbloccare il portafoglio come di consueto, utilizzando il codice PIN o il CompactSeedQR (come visto sopra). Verrà quindi richiesto di inserire la passphrase.

![Image](assets/fr/46.webp)

Inseritela sulla tastiera di Jade e assicuratevi di fare uno o più backup su supporti fisici (carta o metallo). Per l'esempio, sto usando una passphrase molto debole, ma è necessario scegliere una passphrase forte e casuale che includa tutti i tipi di caratteri e sia sufficientemente lunga (come una password forte).

![Image](assets/fr/47.webp)

Se la passphrase è valida, confermare.

![Image](assets/fr/48.webp)

Si noti che le passphrase BIP39 sono sensibili alle maiuscole e alle minuscole. Se si inserisce una passphrase leggermente diversa da quella configurata inizialmente, Jade non segnalerà un errore ma ricaverà un'altra serie di chiavi crittografiche che non saranno quelle del portafoglio iniziale.

È quindi importante, durante la configurazione, prendere nota dell'impronta digitale della chiave master, che si trova nell'angolo in basso a destra dello schermo. Ad esempio, con la mia passphrase `PBN`, l'impronta digitale della mia chiave master è `3AD1AE65`.

![Image](assets/fr/49.webp)

Ogni volta che si sblocca Jade con la passphrase, verificare che l'impronta digitale sia la stessa inserita durante la configurazione. Se è così, la passphrase è corretta e si sta accedendo al portafoglio Bitcoin giusto. In caso contrario, il portafoglio è sbagliato e occorre riprovare, facendo attenzione a non commettere errori di immissione.

Prima di ricevere i primi bitcoin nel portafoglio, **consiglio vivamente di eseguire un test di ripristino a vuoto**. Prendete nota di alcune informazioni di riferimento, come il vostro indirizzo xpub o il primo indirizzo di ricezione, quindi cancellate il vostro portafoglio sul Jade Plus mentre è ancora vuoto (`Opzioni -> Dispositivo -> Ripristino dati di fabbrica`). Quindi provare a ripristinare il portafoglio utilizzando i backup cartacei della frase mnemonica e di qualsiasi passphrase. Verificate che le informazioni del cookie generate dopo il ripristino corrispondano a quelle annotate in origine. Se è così, potete essere certi che i vostri backup cartacei sono affidabili. Per saperne di più su come eseguire un ripristino di prova, date un'occhiata a quest'altro tutorial:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Configurazione del portafoglio su Sparrow Wallet

In questa esercitazione presento un uso avanzato di Jade Plus utilizzando Sparrow Wallet. Tuttavia, questo portafoglio hardware è compatibile con molti altri programmi, come Liana, Nunchuk, Specter, Green e Keeper. Queste compatibilità variano in termini di connessioni: USB, Bluetooth o codice QR (per i dettagli, vedere la tabella nell'introduzione).

Iniziate scaricando e installando Sparrow Wallet [dal sito ufficiale](https://sparrowwallet.com/) sul vostro computer, se non l'avete ancora fatto.

![Image](assets/fr/50.webp)

Assicuratevi di verificare l'autenticità e l'integrità del software prima dell'installazione. Se non sapete come fare, consultate questa guida:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Una volta aperto Sparrow Wallet, fare clic sulla scheda "*File*", quindi su "*Nuovo portafoglio*".

![Image](assets/fr/51.webp)

Assegnate un nome al vostro portafoglio, quindi cliccate su "*Crea portafoglio*".

![Image](assets/fr/52.webp)

Selezionate "*Portafoglio hardware sospeso*".

![Image](assets/fr/53.webp)

Fare clic su "*Scansione...*" accanto all'opzione "*Giada*".

![Image](assets/fr/54.webp)

Sbloccate il vostro Jade Plus e, se ne state usando uno, inserite la vostra passphrase. Quindi accedere al menu "*Opzioni*", selezionare "*Portafoglio*" e fare clic su "*Esporta Xpub*".

![Image](assets/fr/55.webp)

Il vostro Jade visualizzerà il vostro Keystore tramite diversi codici QR. Eseguite la scansione sul vostro computer utilizzando Sparrow.

![Image](assets/fr/56.webp)

A questo punto dovrebbero essere visualizzati il vostro xpub e l'impronta digitale della vostra chiave master, che dovrebbe corrispondere a quella del vostro Jade Plus. Fare clic su "*Applica*".

![Image](assets/fr/57.webp)

Impostate una password forte per proteggere l'accesso al vostro Sparrow Wallet. Questa password proteggerà le chiavi pubbliche, gli indirizzi, le etichette e la cronologia delle transazioni da accessi non autorizzati. È buona norma salvare questa password in un gestore di password, in modo da non dimenticarla.

![Image](assets/fr/58.webp)

Il vostro portafoglio è ora configurato correttamente su Sparrow.

![Image](assets/fr/59.webp)

## Ricevere bitcoin

Ora che il vostro Jade Plus è configurato, siete pronti a ricevere le prime sature sul vostro nuovo portafoglio Bitcoin. Per farlo, su Sparrow, fare clic sul menu "*Receive*".

![Image](assets/fr/60.webp)

Sparrow visualizzerà il primo indirizzo di ricezione vuoto del portafoglio.

![Image](assets/fr/61.webp)

Prima di utilizzarlo, controlliamolo sullo schermo di Jade Plus per assicurarci che appartenga al nostro portafoglio Bitcoin. Su Jade, fare clic su "*Scan QR*", quindi scansionare il codice QR dell'indirizzo visualizzato su Sparrow.

![Image](assets/fr/62.webp)

Verificare che l'indirizzo visualizzato sullo schermo di Jade corrisponda a quello visualizzato su Sparrow Wallet. In caso affermativo, fare clic sul segno di spunta per continuare.

![Image](assets/fr/63.webp)

Il vostro portafoglio hardware confermerà quindi che questo indirizzo fa parte del vostro portafoglio e che detiene la chiave privata associata.

![Image](assets/fr/64.webp)

Se l'indirizzo viene convalidato da Jade, è possibile utilizzarlo per ricevere bitcoin. Quando la transazione viene trasmessa alla rete, appare su Sparrow. Aspettate di ricevere un numero sufficiente di conferme per considerare la transazione definitiva.

![Image](assets/fr/65.webp)

## Inviare bitcoin

Ora che avete qualche saturazione nel vostro portafoglio, potete anche inviarne qualcuna. Per farlo, cliccate sul menu "*UTXO*".

![Image](assets/fr/66.webp)

Selezionare gli UTXO che si desidera utilizzare come input per questa transazione, quindi fare clic su "*Invia selezionati*".

![Image](assets/fr/67.webp)

Inserite l'indirizzo del destinatario, un'etichetta che ricordi lo scopo della transazione e l'importo che desiderate inviare a questo indirizzo.

![Image](assets/fr/68.webp)

Regolare il tasso di commissione in base alle attuali condizioni di mercato, quindi fare clic su "*Crea transazione*".

![Image](assets/fr/69.webp)

Verificare che tutti i parametri della transazione siano corretti, quindi fare clic su "*Finalizza transazione per la firma*".

![Image](assets/fr/70.webp)

Fare clic su "*Mostra QR*" per visualizzare la PSBT (*Transazione Bitcoin parzialmente firmata*). Sparrow ha creato la transazione, ma mancano ancora le firme per sbloccare i bitcoin utilizzati nell'input. Queste firme possono essere eseguite solo da Jade Plus, che ospita il vostro seme dando accesso alle chiavi private necessarie per firmare la transazione.

![Image](assets/fr/71.webp)

Su Jade Plus, fare clic su "*Scan QR*" per scansionare il PSBT visualizzato su Sparrow.

![Image](assets/fr/72.webp)

Confermare che l'indirizzo di consegna e l'importo inviato siano corretti, quindi fare clic sulla freccia per convalidare.

![Image](assets/fr/73.webp)

Assicuratevi che l'importo della tassa sia quello scelto, quindi fate clic sull'icona del segno di spunta nell'angolo in alto a sinistra dell'interfaccia per firmare la transazione.

![Image](assets/fr/74.webp)

Su Sparrow Wallet, cliccate su "*Scan QR*" e scansionate il codice QR visualizzato sul vostro Jade.

![Image](assets/fr/75.webp)

La transazione firmata è ora pronta per essere trasmessa alla rete Bitcoin e inserita in un blocco da un miner. Se tutto è corretto, fare clic su "*Transazione trasmessa*".

![Image](assets/fr/76.webp)

La transazione è stata trasmessa ed è in attesa di conferma.

![Image](assets/fr/77.webp)

Congratulazioni, ora sapete come impostare e utilizzare Jade Plus in modalità QR. Se questa esercitazione vi è stata utile, vi sarei grato se lasciaste un pollice verde qui sotto. Sentitevi liberi di condividere questo articolo sui vostri social network. Grazie per la condivisione!

Per approfondire, vi consiglio quest'altro tutorial su Jade Plus, in cui lo configuriamo via Bluetooth con l'applicazione mobile Green:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0
---
name: Passaporto - Fondazione
description: Configurazione e utilizzo del portafoglio hardware Passport in modalità manuale
---
![cover](assets/cover.webp)

Il Passport è un portafoglio hardware per soli Bitcoin, progettato da Foundation Devices, un'azienda americana fondata nell'aprile 2020 a Boston.

Il Passport "*Batch 2*" che presentiamo in questa guida è il successore della "*Founder's Edition*". Presenta un design premium, uno schermo a colori ad alta definizione e una tastiera fisica ergonomica. Funziona in modalità "*Air-Gap*", assicurando che le chiavi private del portafoglio rimangano totalmente isolate, con scambi possibili tramite scheda MicroSD o codici QR. Il dispositivo include una batteria rimovibile da 1200 mAh.

Per quanto riguarda la connettività, il Passport è dotato di una porta MicroSD, una porta USB-C per la ricarica e una fotocamera posteriore per la scansione dei codici QR.

In termini di sicurezza, il Passport incorpora un elemento sicuro e il codice sorgente del dispositivo è interamente open-source. Offre tutte le caratteristiche che ci si aspetta da un buon portafoglio hardware Bitcoin. Si noti che il Passport non supporta ancora miniscript, ma questa funzione è prevista per il secondo trimestre del 2025.

Al prezzo di 199 dollari, il Passport si posiziona come portafoglio hardware di fascia alta, in concorrenza con Coldcard Q, Jade Plus, Tezor Safe 5 e i modelli top di gamma di Ledger.

![Image](assets/fr/01.webp)

Per gestire il vostro portafoglio sicuro su un Passport, avete diverse opzioni. Questo portafoglio hardware è compatibile con la maggior parte dei software di gestione dei portafogli presenti sul mercato, tra cui Sparrow Wallet, Specter Desktop, Nunchuk, Keeper e altri. In questa guida impareremo a usarlo con Sparrow Wallet.

Se siete principianti, l'opzione più semplice è utilizzare il Passport con l'applicazione nativa Envoy, sviluppata da Foundation. Per sapere come utilizzare Envoy con il Passport, consultate quest'altra guida:

https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb
## Unboxing del Passaporto

Quando si riceve il Passport, assicurarsi che la scatola e il sigillo sul cartone siano intatti per confermare che la confezione non è stata aperta. Al momento della configurazione, verrà inoltre effettuata una verifica software dell'autenticità e dell'integrità del dispositivo.

![Image](assets/fr/02.webp)

Il contenuto della scatola comprende :


- Passaporto;
- Un pezzo di cartone per scrivere la frase mnemonica;
- Un cavo USB-C per la ricarica;
- Scheda MicroSD ;
- Due adattatori da MicroSD a Lightning o USB-C ;
- Adesivi.

Sul dispositivo è presente :


- Una tastiera (1) ;
- Porta USB-C (2);
- Un pulsante di cancellazione (3);
- Un pulsante di ritorno (4) ;
- Un pulsante di conferma (5);
- Cuscinetto direzionale (6);
- Pulsante di accensione/spegnimento (7);
- Un indicatore di stato (8);
- Porta MicroSD (9) ;
- Un pulsante per cambiare modalità aA1 (10) ;
- Una fotocamera posteriore.

![Image](assets/fr/03.webp)

## Passaporto di partenza

Premere il pulsante di accensione/spegnimento sul lato dell'unità per avviarla.

![Image](assets/fr/04.webp)

Premere il pulsante di conferma per accedere al menu successivo.

![Image](assets/fr/05.webp)

In questa esercitazione, utilizzeremo Sparrow Wallet per gestire il portafoglio protetto da passaporto. Selezionare "*Impostazione manuale*".

![Image](assets/fr/06.webp)

Accettare quindi le condizioni d'uso.

![Image](assets/fr/07.webp)

Il passo successivo è il controllo del dispositivo. Questa operazione conferma l'autenticità del Passaporto e garantisce che non sia stato manomesso durante il trasporto. Vi verrà chiesto di scansionare un codice QR.

![Image](assets/fr/08.webp)

Andate su [il sito ufficiale di verifica](https://validate.foundationdevices.com/) e selezionate "*Passaporto*".

![Image](assets/fr/09.webp)

Utilizzare la fotocamera del Passport per scansionare il codice QR visualizzato sul sito.

![Image](assets/fr/10.webp)

Il dispositivo visualizzerà quindi 4 parole.

![Image](assets/fr/11.webp)

Inserite queste parole sul sito web per confermare l'autenticità del vostro passaporto e cliccate su "*Validate*".

![Image](assets/fr/12.webp)

Se appare il messaggio "*Passato*", il portafoglio hardware è autentico. Ora è possibile utilizzarlo per proteggere un portafoglio Bitcoin.

![Image](assets/fr/13.webp)

Confermare il risultato del test sul Passaporto.

![Image](assets/fr/14.webp)

## Impostazione del codice PIN

Segue la fase del codice PIN. Il codice PIN sblocca il Passaporto. Pertanto, protegge dall'accesso fisico non autorizzato. Il codice PIN non partecipa alla creazione delle chiavi crittografiche del portafoglio. Quindi, anche senza accesso al codice PIN, il possesso della frase mnemonica di 12 o 24 parole vi permetterà di riavere accesso ai vostri bitcoin.

![Image](assets/fr/15.webp)

Si consiglia di scegliere un codice PIN il più possibile casuale. Inoltre, assicuratevi di salvare questo codice in un luogo separato da quello in cui è memorizzato il vostro Passport (ad esempio, in un gestore di password).

È possibile scegliere un codice PIN tra 6 e 12 cifre. Vi consiglio di farlo il più lungo possibile.

Utilizzare la tastiera per inserire i numeri PIN. Al termine, fare clic sul pulsante di conferma.

![Image](assets/fr/16.webp)

Confermare il PIN una seconda volta.

![Image](assets/fr/17.webp)

Il codice PIN è stato registrato.

![Image](assets/fr/18.webp)

## Aggiornamento del firmware del Passport

Il portafoglio hardware suggerisce di aggiornare il firmware. Vi consiglio di aggiornarlo immediatamente per beneficiare dei miglioramenti e delle correzioni apportate dalle ultime versioni. Per continuare, fare clic sul pulsante di conferma a destra.

![Image](assets/fr/19.webp)

Il Passport è pronto a ricevere il nuovo firmware tramite una scheda MicroSD.

![Image](assets/fr/20.webp)

A tal fine, utilizzare la scheda MicroSD inclusa nella confezione del Passport (o un'altra) e inserirla nel computer. Scaricare l'ultima versione del firmware da [il sito di documentazione della Fondazione](https://docs.foundation.xyz/firmware-updates/passport/) o [il loro repository GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Prima di installarlo sul vostro dispositivo, vi consigliamo vivamente di verificare l'autenticità e l'integrità del firmware scaricato. Se avete bisogno di aiuto, consultate questo tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Dopo aver controllato il file `.bin', collocarlo sulla MicroSD e inserirlo nel Passport. Si aprirà l'esploratore di file del Passport. Selezionare il file `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Fare clic su "*Selezione*".

![Image](assets/fr/23.webp)

Confermare quindi l'installazione del firmware.

![Image](assets/fr/24.webp)

Attendere il completamento dell'aggiornamento.

![Image](assets/fr/25.webp)

Una volta completato l'aggiornamento, inserire il codice PIN per sbloccare il dispositivo e continuare la configurazione.

![Image](assets/fr/26.webp)

## Creare un nuovo portafoglio Bitcoin

Ora è il momento di creare un nuovo portafoglio Bitcoin. Fare clic sul pulsante di conferma.

![Image](assets/fr/27.webp)

Per creare un nuovo portafoglio, cliccare su "*Crea nuovo seme*".

![Image](assets/fr/28.webp)

È possibile scegliere tra una frase mnemonica di 12 o 24 parole. La sicurezza offerta da entrambe le opzioni è simile, quindi potete optare per quella più facile da salvare, cioè 12 parole.

![Image](assets/fr/29.webp)

Fare clic su "*Continua*".

![Image](assets/fr/30.webp)

Il Passport genererà ora il "*Codice di backup*". Si tratta di una serie di numeri che possono essere utilizzati per decriptare un backup del portafoglio memorizzato su una MicroSD. Questo sistema di backup, specifico per i dispositivi Foundation, costituisce un ulteriore backup della vostra frase mnemonica, ma non è compatibile con altri software Bitcoin.

Se decidete di utilizzare questo "*Codice di backup*", assicuratevi di conservarlo in una posizione diversa dalla MicroSD contenente il backup crittografato del vostro portafoglio. Potete tuttavia scegliere di non utilizzare questo sistema se ritenete che un buon backup della vostra frase mnemonica sia sufficiente.

![Image](assets/fr/31.webp)

Inserire il "*Codice di backup*" per confermare il corretto salvataggio.

![Image](assets/fr/32.webp)

Se è stata inserita una MicroSD, il backup crittografato del portafoglio è stato salvato lì.

![Image](assets/fr/33.webp)

Sul passaporto verrà visualizzata la frase mnemonica di 12 parole. Questa frase mnemonica vi dà accesso completo e illimitato a tutti i vostri bitcoin. Chiunque sia in possesso di questa frase può rubare i vostri fondi, anche senza accedere fisicamente al vostro Passaporto.

La frase di 12 parole ripristina l'accesso ai bitcoin in caso di perdita, furto o rottura del Passaporto. È quindi molto importante salvarlo con cura e conservarlo in un luogo sicuro.

Potete scriverlo sul cartoncino fornito nella scatola, oppure, per maggiore sicurezza, vi consiglio di inciderlo su una base in acciaio inossidabile per proteggerlo da incendi, allagamenti o crolli.

Cliccate sul pulsante di conferma per visualizzare la vostra frase mnemonica.

![Image](assets/fr/34.webp)

Per ulteriori informazioni sul modo corretto di salvare e gestire la frase mnemonica, vi consiglio di seguire quest'altro tutorial, soprattutto se siete principianti:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
naturalmente, non dovete mai condividere queste parole su Internet, come sto facendo io in questa esercitazione. Questo portfolio di esempio sarà utilizzato solo su Testnet e sarà cancellato alla fine del tutorial.**_

Eseguite un backup fisico di questa frase.

![Image](assets/fr/35.webp)

Il Passport è stato configurato con successo. Fare clic sul pulsante di conferma per continuare.

![Image](assets/fr/36.webp)

## Scoperta del menu

L'interfaccia del Passport presenta tre menu principali:


- "*Account*";
- "*Più*";
- "*Impostazioni*".

Per spostarsi tra questi menu, utilizzare le frecce sinistra e destra del pad direzionale.

### *Menu "Conto*

Nel menu "*Account*" si trovano le funzioni principali del portafoglio Bitcoin. È possibile firmare una transazione tramite la fotocamera o la porta MicroSD.

![Image](assets/fr/37.webp)

Il sottomenu "*Strumenti account*" offre opzioni quali la verifica di un indirizzo, la firma di un messaggio o la consultazione degli indirizzi in portafoglio.

![Image](assets/fr/38.webp)

Nel sottomenu "*Gestione del conto*" è possibile collegare il proprio portafoglio Bitcoin a un software di gestione del portafoglio (di cui parleremo nei prossimi passi di questo tutorial), oppure visualizzare e rinominare il proprio conto.

![Image](assets/fr/39.webp)

### Menu "Altro

Nel menu "*Più*" è possibile creare un nuovo account nel proprio portafoglio, collegato alla stessa frase mnemonica.

![Image](assets/fr/40.webp)

È inoltre possibile inserire una passphrase BIP39 (vedere la sezione successiva) o utilizzare un seed temporaneo.

![Image](assets/fr/41.webp)

### Menu "Impostazioni

Nel menu "*Impostazioni*" si trovano tutte le impostazioni del portafoglio e del dispositivo.

![Image](assets/fr/42.webp)

Il sottomenu "*Dispositivo*" offre opzioni per personalizzare la luminosità dello schermo, impostare il ritardo prima del blocco automatico, modificare il codice PIN o rinominare il dispositivo.

![Image](assets/fr/43.webp)

Il sottomenu "*Backup*" consente di esportare il backup criptato del portafoglio, di verificare la validità di un backup esistente o di ricercare nuovamente il "*Codice di backup*".

![Image](assets/fr/44.webp)

Il sottomenu "*Firmware*" consente di aggiornare il firmware del Passport. Si consiglia di eseguire regolarmente questi aggiornamenti per usufruire delle correzioni e delle funzioni più recenti.

![Image](assets/fr/45.webp)

Il sottomenu "*Bitcoin*" consente di cambiare l'unità di misura visualizzata (BTC o satoshis), di gestire un eventuale portafoglio Multisig o di passare alla modalità "*Testnet*".

![Image](assets/fr/46.webp)

In "*Avanzate*", è possibile visualizzare le parole della frase mnemonica, eseguire azioni sulla MicroSD inserita, ripristinare le impostazioni di fabbrica del Passport o eseguire un controllo di autenticità, come eseguito in precedenza.

![Image](assets/fr/47.webp)

È possibile attivare "*Parole di sicurezza*", una funzione che aggiunge un livello di sicurezza visualizzando due parole specifiche quando si sblocca il dispositivo dopo aver inserito le prime quattro cifre del codice PIN. Queste parole, da salvare durante la configurazione, garantiscono che il Passport non sia stato sostituito o manomesso. In caso di discrepanze successive, si consiglia di non utilizzare il dispositivo. Si consiglia di attivare questa opzione per evitare la maggior parte dei rischi di compromissione fisica del dispositivo.

![Image](assets/fr/48.webp)

Infine, il sottomenu "*Estensioni*" consente di attivare funzioni specifiche per determinati usi dell'apparecchio, come il protocollo coinjoin di Whirlpool.

![Image](assets/fr/49.webp)

## Aggiungere una passphrase BIP39

Prima di continuare, se lo desiderate, potete aggiungere una passphrase BIP39. La passphrase BIP39 è una password opzionale che si può scegliere liberamente e che viene aggiunta alla frase mnemonica per rafforzare la sicurezza del portafoglio. Con questa funzione abilitata, l'accesso al portafoglio Bitcoin richiede sia la frase mnemonica che la passphrase. Senza di esse, sarebbe impossibile recuperare il portafoglio.

Prima di configurare questa opzione sul Passport, si consiglia vivamente di leggere questo articolo per comprendere appieno il funzionamento teorico della passphrase ed evitare errori che potrebbero portare alla perdita dei bitcoin:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Per attivarla, andate nel menu "*Altre*" e fate clic su "*Inserisci passphrase*".

![Image](assets/fr/50.webp)

Inserire la passphrase utilizzando la tastiera aA1 e assicurarsi di salvarla una o più volte su un supporto fisico (carta o metallo). Per l'esempio, sto usando una passphrase molto debole, ma dovreste scegliere una passphrase forte e casuale, che includa tutti i tipi di caratteri e sia sufficientemente lunga (come una password forte).

![Image](assets/fr/51.webp)

Si noti che le passphrase BIP39 sono sensibili alle maiuscole e alle minuscole. Se si inserisce una passphrase leggermente diversa da quella inizialmente configurata, Passport non segnalerà un errore, ma ricaverà un'altra serie di chiavi crittografiche che non saranno quelle del portafoglio iniziale.

È quindi importante, durante la configurazione, annotare da qualche parte l'impronta digitale della chiave master che verrà fornita nel passaggio successivo. Ad esempio, con la mia passphrase `Plan B Network`, la mia master key fingerprint è `745D526B`.

![Image](assets/fr/52.webp)

Ogni volta che si sblocca il Passport, è necessario tornare a questo menu per inserire la passphrase e applicarla al portafoglio. Passport non salva la passphrase.

Ogni volta che si sblocca, dopo aver scritto la passphrase, verificare in questa schermata di conferma che l'impronta digitale indicata sia la stessa di quella scritta durante la configurazione. Se è così, la passphrase è corretta e si sta accedendo al portafoglio Bitcoin corretto. In caso contrario, il portafoglio è sbagliato e occorre riprovare, facendo attenzione a non commettere errori di immissione.

Prima di ricevere i primi bitcoin sul vostro portafoglio, **vi consiglio vivamente di eseguire un test di recupero vuoto**. Prendete nota di alcune informazioni di riferimento, come il vostro indirizzo xpub o il primo indirizzo di ricezione, quindi cancellate il vostro portafoglio sul Passport mentre è ancora vuoto (`Impostazioni -> Avanzate -> Cancella Passport`). Quindi provare a ripristinare il portafoglio utilizzando i backup cartacei della frase mnemonica e dell'eventuale passphrase. Verificate che le informazioni del cookie generate dopo il ripristino corrispondano a quelle annotate in origine. Se è così, potete essere certi che i vostri backup cartacei sono affidabili. Per saperne di più su come eseguire un ripristino di prova, consultare quest'altra esercitazione:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
![Image](assets/fr/53.webp)

## Configurazione del portafoglio su Sparrow Wallet

In questa esercitazione vi mostrerò un uso avanzato di Passport con Sparrow Wallet. Tuttavia, questo portafoglio hardware è compatibile anche con Envoy (l'applicazione Foundation), Keeper, BlueWallet, Nunchuk, Specter e molti altri...

Iniziate scaricando e installando Sparrow Wallet [dal sito ufficiale](https://sparrowwallet.com/) sul vostro computer, se non l'avete ancora fatto.

![Image](assets/fr/54.webp)

Assicuratevi di verificare l'autenticità e l'integrità del software prima dell'installazione. Se non sapete come fare, consultate questa guida:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Una volta aperto Sparrow Wallet, fare clic sulla scheda "*File*", quindi su "*Nuovo portafoglio*".

![Image](assets/fr/55.webp)

Assegnate un nome al vostro portafoglio, quindi cliccate su "*Crea portafoglio*".

![Image](assets/fr/56.webp)

Selezionate "*Portafoglio hardware sospeso*".

![Image](assets/fr/57.webp)

Fate clic su "*Scansione...*" accanto all'opzione "*Passaporto*". In questo modo si aprirà la webcam.

![Image](assets/fr/58.webp)

Sul portafoglio hardware, accedere al menu "*Account*", selezionare il sottomenu "*Manage Account*" e fare clic su "*Connect Wallet*".

![Image](assets/fr/59.webp)

Nell'elenco a discesa visualizzato, scegliere "*Sparrow*".

![Image](assets/fr/60.webp)

Selezionare quindi "*Single-sig*" per una configurazione normale, senza multisig.

![Image](assets/fr/61.webp)

Selezionare l'opzione "*Codice QR*".

![Image](assets/fr/62.webp)

Il Passport genererà quindi codici QR dinamici. Utilizzate la webcam del vostro computer per scansionarli nel software Sparrow.

![Image](assets/fr/63.webp)

A questo punto si dovrebbe vedere il proprio xpub e l'impronta digitale della chiave master, che dovrebbe corrispondere a quella visualizzata sul Passport quando si inserisce la passphrase. Fare clic sul pulsante "*Applica*".

![Image](assets/fr/64.webp)

Impostate una password forte per proteggere l'accesso al vostro Sparrow Wallet. Questa password proteggerà le chiavi pubbliche, gli indirizzi, le etichette e la cronologia delle transazioni da accessi non autorizzati. È buona norma salvare questa password in un gestore di password, in modo da non dimenticarla.

![Image](assets/fr/65.webp)

Il Passport richiede quindi di scansionare l'indirizzo di prima ricezione per confermare che l'importazione è andata a buon fine.

![Image](assets/fr/66.webp)

In Sparrow, andare alla scheda "*Ricevi*" e scansionare il codice QR del primo indirizzo.

![Image](assets/fr/67.webp)

Se l'operazione ha esito positivo, il Passaporto visualizza "*Verificato*".

![Image](assets/fr/68.webp)

Questo conferma che l'importazione è avvenuta con successo.

![Image](assets/fr/69.webp)

## Ricevere bitcoin

Ora che il Passport è stato configurato, siete pronti a ricevere le prime sature sul vostro nuovo portafoglio Bitcoin. Per farlo, su Sparrow, cliccate sul menu "*Receive*".

![Image](assets/fr/70.webp)

Sparrow visualizzerà il primo indirizzo di ricevuta vuoto del portafoglio. È possibile aggiungere un'etichetta.

![Image](assets/fr/71.webp)

Prima di utilizzarlo, controlleremo l'indirizzo sulla schermata di Passport per assicurarci che appartenga al nostro portafoglio Bitcoin. Su Sparrow, se necessario, è possibile ingrandire il codice QR dell'indirizzo facendo clic su di esso. Nel menu "*Account*" del Passport, selezionare "*Strumenti account*".

![Image](assets/fr/72.webp)

Cliccate su "*Verifica indirizzo*", quindi scansionate il codice QR visualizzato su Sparrow Wallet.

![Image](assets/fr/73.webp)

Assicuratevi che l'indirizzo visualizzato sul Passaporto corrisponda esattamente a quello visualizzato su Sparrow e che appaia la dicitura "*Verificato*".

![Image](assets/fr/74.webp)

Ora è possibile utilizzarlo per ricevere bitcoin. Quando la transazione viene trasmessa sulla rete, appare su Sparrow. Aspettate di ricevere un numero sufficiente di conferme per considerare la transazione definitiva.

![Image](assets/fr/75.webp)

## Inviare bitcoin

Ora che avete qualche saturazione nel vostro portafoglio, potete anche inviarne qualcuna. Per farlo, cliccate sul menu "*UTXO*".

![Image](assets/fr/76.webp)

Selezionare gli UTXO che si desidera utilizzare come input per questa transazione, quindi fare clic su "*Invia selezionati*".

![Image](assets/fr/77.webp)

Inserite l'indirizzo del destinatario, un'etichetta che ricordi lo scopo della transazione e l'importo che desiderate inviare a questo indirizzo.

![Image](assets/fr/78.webp)

Regolare il tasso di commissione in base alle attuali condizioni di mercato, quindi fare clic su "*Crea transazione*".

![Image](assets/fr/79.webp)

Verificare che tutti i parametri della transazione siano corretti, quindi fare clic su "*Finalizza transazione per la firma*".

![Image](assets/fr/80.webp)

Fare clic su "*Mostra QR*" per visualizzare la PSBT (*Transazione Bitcoin parzialmente firmata*). Sparrow ha creato la transazione, ma mancano ancora le firme per sbloccare i bitcoin utilizzati nell'input. Queste firme possono essere eseguite solo da Passport, che ospita il seme e dà accesso alle chiavi private necessarie per firmare la transazione.

![Image](assets/fr/81.webp)

Sul Passport, accedere al menu "*Account*" e fare clic su "*Firma con codice QR*".

![Image](assets/fr/82.webp)

Scansionare il PSBT (*Transazione Bitcoin parzialmente firmata*) visualizzato su Sparrow Wallet.

![Image](assets/fr/83.webp)

Confermare che l'indirizzo del destinatario e l'importo inviato siano corretti, quindi premere il pulsante di conferma.

![Image](assets/fr/84.webp)

Controllare l'indirizzo di scambio. Nel mio esempio non c'è, in quanto la transazione include una sola uscita.

![Image](assets/fr/85.webp)

Assicuratevi che la tariffa sia quella che avete scelto.

![Image](assets/fr/86.webp)

Se tutte le informazioni sono corrette, fare clic sul pulsante di conferma per firmare la transazione.

![Image](assets/fr/87.webp)

Su Sparrow Wallet, cliccate su "*Scan QR*" e scansionate il codice QR visualizzato sul vostro Passaporto.

![Image](assets/fr/88.webp)

La transazione firmata è ora pronta per essere trasmessa alla rete Bitcoin e inserita in un blocco da un miner. Se tutto è corretto, fare clic su "*Transazione trasmessa*".

![Image](assets/fr/89.webp)

La transazione è stata trasmessa ed è in attesa di conferma.

![Image](assets/fr/90.webp)

Congratulazioni, ora sapete come configurare e utilizzare Passport. Se questa guida vi è stata utile, vi sarei grato se lasciaste un pollice verde qui sotto. Sentitevi liberi di condividere questo articolo sui vostri social network. Grazie per la condivisione!

Per ulteriori informazioni, consultare il nostro tutorial sul software Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
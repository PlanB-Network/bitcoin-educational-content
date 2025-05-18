---
name: Trezor Modello Uno
description: Impostazione e utilizzo del Hardware Wallet Model One
---
![cover](assets/cover.webp)



*Credito immagine: [Trezor.io](https://trezor.io/)*



Il Trezor Model One è il primo Hardware Wallet mai realizzato, lanciato nel 2014 da SatoshiLabs. Dopo oltre dieci anni di vita, rimane una scelta interessante, soprattutto per gli utenti che cercano un Hardware Wallet accessibile sia dal punto di vista tecnico che del budget. Infatti, il prezzo è di 49 euro sul sito ufficiale di Trezor. È uno degli unici portafogli hardware in questa fascia di prezzo. Si colloca a metà strada tra i dispositivi entry-level a circa 20 euro, come il Tapsigner, che spesso non dispongono di uno schermo, e i dispositivi di fascia media a circa 80 euro, come il Ledger Nano S Plus o il Trezor Safe 3.



Il Model One è dotato di un display OLED monocromatico da 0,96 pollici e di due pulsanti fisici. Funziona senza batteria e utilizza solo una connessione micro-USB per l'alimentazione e il trasferimento dei dati.



![Image](assets/fr/01.webp)



Lo svantaggio principale del Model One è la mancanza del Secure Element, che lo rende vulnerabile a una serie di attacchi fisici, alcuni dei quali sono relativamente semplici da eseguire. Questi attacchi possono includere l'analisi dei canali ausiliari per determinare il PIN del dispositivo o tecniche più avanzate per estrarre il seed crittografato e forzarlo in seguito. Si noti che questi attacchi richiedono l'accesso fisico al dispositivo. Tuttavia, questa vulnerabilità può essere notevolmente ridotta utilizzando un solido passphrase BIP39. Se si opta per questo Hardware Wallet, si consiglia vivamente di configurare un passphrase.



Il Model One offre due importanti vantaggi:




- Si basa su un'architettura completamente open-source. A differenza dei modelli più recenti con Secure Element, tutti i componenti hardware e software del Model One sono verificabili;
- È dotato di uno schermo. Per quanto ne so, questo è l'unico Hardware Wallet sul mercato in questa fascia di prezzo con un display. Si tratta di una caratteristica molto importante, in quanto consente di verificare le informazioni firmate e gli indirizzi di ricezione, prevenendo così molti attacchi digitali.



Il Trezor Model One può quindi rappresentare una scelta saggia per i principianti e gli utenti intermedi con un budget limitato. Tuttavia, è importante essere consapevoli dei suoi limiti in termini di protezione fisica, a causa dell'assenza di Secure Element. Se il vostro budget è limitato, questa è una buona opzione, ma se potete permettervi di optare per un modello superiore, come il Trezor Safe 3 a 79 euro, è preferibile, in quanto include un Secure Element.



## Unboxing del Trezor Model One



Quando si riceve il Model One, verificare che la scatola e il Seal siano intatti per confermare che la confezione non è stata aperta. In seguito, al momento della configurazione, verrà effettuata una verifica software dell'autenticità e dell'integrità del dispositivo.



Il contenuto della scatola comprende :




- Il Trezor Model One;
- Cartoncino per registrare la frase Mnemonic, adesivi e istruzioni;
- Cavo da USB-A a micro-USB.



![Image](assets/fr/02.webp)



La navigazione del dispositivo è molto semplice:




- Fare clic con il tasto destro del mouse per confermare e procedere con le fasi successive;
- Utilizzare il tasto sinistro per tornare indietro.



## Prerequisiti



In questa esercitazione vi mostrerò come utilizzare il Trezor Model One con [Sparrow Wallet portfolio management software](https://sparrowwallet.com/download/). Se non avete ancora installato questo software, fatelo subito. Se avete bisogno di aiuto, abbiamo anche un tutorial dettagliato sulla configurazione di Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

È inoltre necessario il software Trezor Suite per configurare il Model One, verificarne l'autenticità e installare il firmware. Utilizzeremo questo software solo per questo, e in seguito sarà necessario solo per gli aggiornamenti del firmware. Per la gestione quotidiana del Wallet, utilizzeremo esclusivamente Sparrow Wallet, in quanto è ottimizzato per il Bitcoin e facile da usare, anche per i principianti (Sparrow supporta solo il Bitcoin, non le altcoin).



[Scarica Trezor Suite dal sito ufficiale](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Per entrambi i programmi, vi consiglio vivamente di verificarne l'autenticità (con GnuPG) e l'integrità (tramite Hash) prima di installarli sul vostro computer. Se non sapete come fare, potete seguire quest'altro tutorial:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Avvio del Trezor Model One



Collegare il Model One al computer in cui sono già installati Trezor Suite e Sparrow Wallet.



![Image](assets/fr/04.webp)



Aprire Trezor Suite, quindi fare clic su "*Impostare il mio Trezor*".



![Image](assets/fr/05.webp)



Selezionare "*Firmware solo Bitcoin*", quindi fare clic su "*Installa Bitcoin*".



![Image](assets/fr/06.webp)



Trezor Suite installerà quindi il firmware sul Model One. Attendere durante l'installazione.



![Image](assets/fr/07.webp)



Fare clic su "*Continua*".



![Image](assets/fr/08.webp)



## Creare un portafoglio Bitcoin



Su Trezor Suite, fare clic sul pulsante "*Crea nuovo Wallet*".



![Image](assets/fr/09.webp)



Accettare le condizioni di utilizzo del Hardware Wallet.



![Image](assets/fr/10.webp)



In Trezor Suite, fare clic su "*Continua il backup*".



![Image](assets/fr/11.webp)



Il software fornisce istruzioni su come gestire la frase Mnemonic.



Questo Mnemonic vi dà accesso completo e illimitato a tutti i vostri bitcoin. Chiunque sia in possesso di questa frase può rubare i vostri fondi, anche senza avere accesso fisico al vostro Trezor Model One.



La frase di 24 parole ripristina l'accesso ai bitcoin in caso di smarrimento, furto o rottura del Hardware Wallet. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.



Potete scriverlo sul cartoncino fornito nella scatola, oppure, per maggiore sicurezza, vi consiglio di inciderlo su una base in acciaio inossidabile per proteggerlo da incendi, allagamenti o crolli.



Confermare le istruzioni, quindi fare clic sul pulsante "*Crea backup Wallet*".



![Image](assets/fr/12.webp)



Il Model One creerà la frase Mnemonic utilizzando il suo generatore di numeri casuali. Assicuratevi di non essere osservati durante questa operazione. Scrivete le parole fornite sullo schermo su un supporto fisico di vostra scelta. A seconda della vostra strategia di sicurezza, potete pensare di fare diverse copie fisiche complete della frase (ma soprattutto non dividetela). È importante che le parole siano numerate e in ordine sequenziale.



***Ovviamente, non dovete mai condividere queste parole su Internet, come faccio io in questo tutorial. Questo esempio di Wallet sarà usato solo sul Testnet e sarà cancellato alla fine del tutorial



Per maggiori informazioni sul modo corretto di salvare e gestire la frase Mnemonic, vi consiglio di seguire quest'altra guida, soprattutto se siete principianti:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Per passare alle parole successive, fare clic con il tasto destro del mouse. Una volta scritte tutte le parole, fare nuovamente clic sul pulsante destro per passare alla fase successiva.



![Image](assets/fr/13.webp)



Il vostro Hardware Wallet vi mostra di nuovo tutte le parole. Controllate di averle scritte tutte.



![Image](assets/fr/14.webp)



## Impostazione del codice PIN



Poi si passa alla fase del codice PIN. Il codice PIN sblocca il Trezor. Pertanto, fornisce una protezione contro l'accesso fisico non autorizzato. Il codice PIN non partecipa alla creazione delle chiavi crittografiche del Wallet. Pertanto, anche senza accedere al codice PIN, il possesso della frase di 12 parole del Mnemonic consentirà di ottenere una protezione contro l'accesso fisico non autorizzato. Quindi, anche senza accesso al codice PIN, il possesso della frase Mnemonic di 12 parole vi permetterà di riavere accesso ai vostri bitcoin.



Su Trezor Suite, fare clic su "*Continua a PIN*", quindi sul pulsante "*Imposta PIN*".



![Image](assets/fr/15.webp)



Confermare il Modello Uno.



![Image](assets/fr/16.webp)



Si consiglia di scegliere un codice PIN il più possibile casuale. Assicurarsi di salvare questo codice in un luogo diverso da quello in cui è memorizzato il Trezor (ad esempio, in un gestore di password). È possibile definire un codice PIN di un numero compreso tra 8 e 50 cifre. Si consiglia di scegliere un codice PIN il più lungo possibile per aumentare la sicurezza.



Il codice PIN deve essere inserito in Trezor Suite sul computer facendo clic sui punti corrispondenti alle cifre, secondo la configurazione della tastiera visualizzata su Trezor Model One.



Questo metodo specifico di inserimento del PIN è richiesto ogni volta che si sblocca il Trezor Model One, sia tramite Trezor Suite che tramite Sparrow Wallet.



![Image](assets/fr/17.webp)



Al termine, fare clic sul pulsante "*Inserisci il PIN*".



![Image](assets/fr/18.webp)



Per confermare, digitare nuovamente il PIN.



![Image](assets/fr/19.webp)



Su Trezor Suite, fare clic sul pulsante "*Completa la configurazione*".



![Image](assets/fr/20.webp)



La configurazione del Model One è ora completa. Se si desidera, è possibile modificare il nome e la pagina iniziale del Hardware Wallet.



![Image](assets/fr/21.webp)



Non avremo più bisogno del software Trezor Suite, se non per effettuare gli aggiornamenti regolari del firmware del Hardware Wallet o per eseguire un test di ripristino. Ora utilizzeremo Sparrow per gestire il portafoglio, in quanto questo software è perfettamente adatto all'uso esclusivo del Bitcoin.



## Impostazione del portafoglio su Sparrow Wallet



Iniziate scaricando e installando Sparrow Wallet [dal sito ufficiale](https://sparrowwallet.com/) sul vostro computer, se non l'avete ancora fatto.



Una volta aperto Sparrow Wallet, assicuratevi che il software sia collegato a un nodo Bitcoin, indicato dal segno di spunta nell'angolo in basso a destra di Interface. Se avete problemi a collegare Sparrow, vi consiglio di consultare l'inizio di questa guida:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Fare clic sulla scheda "*File*", quindi su "*Nuovo Wallet*".



![Image](assets/fr/22.webp)



Assegnare un nome al portafoglio, quindi fare clic su "*Crea Wallet*".



![Image](assets/fr/23.webp)



Nel menu a discesa "*Tipo di script*", selezionare il tipo di script che verrà utilizzato per proteggere i bitcoin. Io consiglio "*Taproot*" o, in mancanza, "*Native SegWit*".



![Image](assets/fr/24.webp)



Fare clic sul pulsante "*Connected Hardware Wallet*". Naturalmente il Model One deve essere collegato al computer.



![Image](assets/fr/25.webp)



Fare clic sul pulsante "*Scan*". Dovrebbe apparire il vostro Modello Uno.



Quando si collega il Model One a un computer con Sparrow Wallet aperto, verrà richiesto di inserire un passphrase BIP39 su Sparrow. Questa opzione avanzata sarà trattata in una prossima esercitazione. Per il momento, è sufficiente selezionare "*Disattiva passphrase*" per evitare che il Trezor richieda l'immissione di un passphrase a ogni avvio.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Fare clic su "*Importa Keystore*".



![Image](assets/fr/27.webp)



Ora è possibile vedere i dettagli del proprio Wallet, compresa la chiave pubblica estesa del primo account. Fare clic sul pulsante "*Apply*" per finalizzare la creazione del Wallet.



![Image](assets/fr/28.webp)



Scegliere una password forte per proteggere l'accesso a Sparrow Wallet. Questa password garantirà un accesso sicuro ai dati di Sparrow Wallet, proteggendo le chiavi pubbliche, gli indirizzi, le etichette e la cronologia delle transazioni da accessi non autorizzati.



Vi consiglio di salvare questa password in un gestore di password per non dimenticarla.



![Image](assets/fr/29.webp)



E ora il vostro portafoglio è stato importato in Sparrow Wallet!



![Image](assets/fr/30.webp)



Prima di ricevere i primi bitcoin nel Wallet, **vi consiglio vivamente di eseguire un test di ripristino a vuoto**. Annotare alcune informazioni di riferimento, ad esempio il proprio xpub, quindi resettare il Trezor Model One mentre il Wallet è ancora vuoto. Quindi provare a ripristinare il Wallet sul Trezor utilizzando i backup cartacei. Verificare che l'xpub generato dopo il ripristino corrisponda a quello scritto in origine. Se così fosse, si può essere certi che i backup cartacei sono affidabili.



Per saperne di più su come eseguire un test di ripristino, vi suggerisco di consultare quest'altra guida:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Come ricevere bitcoin con il Trezor Model One?



Su Sparrow, fare clic sulla scheda "*Receive*".



![Image](assets/fr/31.webp)



Prima di utilizzare il Address proposto da Sparrow Wallet, verificatelo sullo schermo del vostro Trezor. Questa pratica consente di confermare che il Address visualizzato su Sparrow non è fraudolento e che il Hardware Wallet detiene effettivamente la chiave privata necessaria per spendere successivamente i bitcoin assicurati con questo Address. Ciò consente di evitare diversi tipi di attacco.



Per eseguire questo controllo, fare clic sul pulsante "*Visualizza Address*".



![Image](assets/fr/32.webp)



Verificare che il Address visualizzato sul Trezor corrisponda a quello del Wallet di Sparrow. È consigliabile effettuare questo controllo anche prima di comunicare il Address al mittente, per essere sicuri della sua validità. È possibile premere il tasto destro per confermare.



![Image](assets/fr/33.webp)



Si può anche aggiungere un "*Label*" per descrivere l'origine dei bitcoin che saranno protetti con questo Address. Questa è una buona pratica che consente di gestire meglio gli UTXO.



![Image](assets/fr/34.webp)



È quindi possibile utilizzare questo Address per ricevere bitcoin.



![Image](assets/fr/35.webp)



## Come inviare bitcoin con il Trezor Model One?



Ora che avete ricevuto i primi Satss nel vostro Model One-secured Wallet, potete anche spenderli! Collegate il vostro Trezor al computer, lanciate Sparrow Wallet, quindi andate alla scheda "*Invio*" per creare una nuova transazione.



![Image](assets/fr/36.webp)



Se si desidera *controllare le monete*, ossia scegliere specificamente quali UTXO consumare nella transazione, andare alla scheda "*UTXO*". Selezionare gli UTXO che si desidera spendere, quindi fare clic su "*Invia selezionati*". Si verrà reindirizzati alla stessa schermata della scheda "*Invio*", ma con gli UTXO già selezionati per la transazione.



![Image](assets/fr/37.webp)



Inserire la destinazione Address. È possibile inserire più indirizzi facendo clic sul pulsante "*+ Aggiungi*".



![Image](assets/fr/38.webp)



Scrivete una "*Etichetta*" per ricordare lo scopo di questa spesa.



![Image](assets/fr/39.webp)



Selezionare l'importo da inviare a questo Address.



![Image](assets/fr/40.webp)



Regolate il tasso di commissione della vostra transazione in base al mercato attuale. Ad esempio, è possibile utilizzare [Mempool.space](https://Mempool.space/) per scegliere una tariffa adeguata.



Assicurarsi che tutti i parametri della transazione siano corretti, quindi fare clic su "*Crea transazione*".



![Image](assets/fr/41.webp)



Se tutto è di vostro gradimento, cliccate su "*Finalizza la transazione per la firma*".



![Image](assets/fr/42.webp)



Fare clic su "*Firma*".



![Image](assets/fr/43.webp)



Fare clic su "*Sign*" accanto al proprio Trezor Model One.



![Image](assets/fr/44.webp)



Controllare i parametri della transazione sulla schermata del Hardware Wallet, tra cui il Address ricevente del destinatario, l'importo inviato e la tariffa. Una volta verificata la transazione su Trezor, fare clic con il tasto destro del mouse per firmarla.



![Image](assets/fr/45.webp)



La transazione è ora firmata. Controllare un'ultima volta che tutto sia a posto, quindi fare clic su "*Diffusione della transazione*" per trasmettere la transazione sulla rete Bitcoin.



![Image](assets/fr/46.webp)



È possibile trovarlo nella scheda "*Transazioni*" di Sparrow Wallet.



![Image](assets/fr/47.webp)



Congratulazioni, ora siete al corrente dell'uso di base del Trezor Model One con lo Sparrow Wallet! Per fare un ulteriore passo avanti, vi consiglio questo tutorial completo sull'uso di un Trezor Hardware Wallet con un BIP39 passphrase per rafforzare la vostra sicurezza:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Se questa esercitazione vi è stata utile, vi sarei grato se lasciaste un pollice Green qui sotto. Sentitevi liberi di condividere questo articolo sui vostri social network. Grazie mille!
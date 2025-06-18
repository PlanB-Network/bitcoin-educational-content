---
name: Trezor Safe 3
description: Configurazione e utilizzo di Hardware Wallet Safe 3
---
![cover](assets/cover.webp)



*Credito immagine: [Trezor.io](https://trezor.io/)*



Il Trezor Safe 3 è un Hardware Wallet progettato da SatoshiLabs e creato nel 2023. È un modello molto compatto e leggero (14 grammi) progettato sia per i principianti che per gli utenti intermedi. È il successore del famoso Model One, con aggiunte significative, pur mantenendo l'approccio open-source del marchio che lo distingue dal suo principale concorrente, il Ledger. Il Safe 3 ha un prezzo di 79 euro. Si posiziona quindi nel segmento medio del Hardware Wallet, in diretta concorrenza con il Ledger Nano S Plus.



Il Safe 3 non ha una batteria e funziona esclusivamente tramite una connessione USB-C, utilizzata sia per l'alimentazione che per la comunicazione. È dotato di un piccolo display OLED monocromatico da 0,96 pollici e di due pulsanti fisici.



![Image](assets/fr/01.webp)



Safe 3 offre tutte le caratteristiche essenziali che ci si aspetta da un buon Hardware Wallet, compresa un'eccellente integrazione del passphrase BIP39. Tuttavia, non supporta ancora Miniscript.



Questo modello è particolarmente adatto ai principianti e potrebbe addirittura essere il Hardware Wallet che consiglierei a un nuovo utente. È adatto anche agli utenti intermedi. D'altra parte, potrebbe non soddisfare tutte le aspettative degli utenti avanzati che cercano funzioni più specifiche, disponibili su dispositivi come la Coldcard. Tuttavia, se non avete bisogno di queste opzioni avanzate, il Trezor Safe 3 può essere una scelta eccellente.



## Il modello di sicurezza Trezor Safe 3



Il Trezor Safe 3 è ora dotato di un **Secure Element** certificato EAL6+, un progresso significativo rispetto ai modelli precedenti come il Model One e il Model T. Si tratta del chip OPTIGA Trust M V3, che non memorizza direttamente il seed, ma agisce come componente crittografico per proteggerne l'accesso. Il Secure Element conserva un segreto a cui si può accedere solo dopo che l'utente ha inserito correttamente il PIN. Questo segreto viene quindi utilizzato per decifrare il seed, che viene memorizzato in modo criptato nella memoria principale del dispositivo.



Questo sistema di sicurezza ibrido offre una migliore protezione fisica, in particolare contro gli attacchi di estrazione o di analisi invasiva, problemi a cui il Model One era soggetto, in particolare nella gestione dei PIN. Queste vulnerabilità sono ora aggirate grazie all'utilizzo del Secure Element. Questo modello mantiene inoltre un'architettura software open-source: il codice che gestisce la generazione e l'utilizzo delle chiavi private rimane completamente accessibile e verificabile. Il chip OPTIGA gestisce soltanto il codice PIN, un elemento esterno alla gestione delle chiavi Bitcoin Wallet. Rilascia solo un segreto che può essere utilizzato per decifrare il seed. Inoltre, il chip OPTIGA Trust M V3 beneficia di una licenza relativamente libera, che autorizza SatoshiLabs a pubblicare liberamente le potenziali vulnerabilità.



Questo modello di sicurezza rappresenta, a mio avviso, uno dei migliori compromessi disponibili oggi sul mercato. Combina i vantaggi di un Secure Element con la gestione del software open-source. In precedenza, gli utenti dovevano scegliere tra una maggiore sicurezza fisica con un chip e la trasparenza con l'open-source; con Trezor Safe 3, è possibile beneficiare di entrambi.



In questa guida vi mostreremo come configurare e utilizzare il vostro Trezor Safe 3 in modo sicuro.



## Unboxing del Trezor Safe 3



Quando si riceve il Safe 3, assicurarsi che la scatola e il Seal siano intatti per confermare che la confezione non è stata aperta. In seguito, al momento della configurazione, verrà effettuata una verifica software dell'autenticità e dell'integrità del dispositivo.



Il contenuto della scatola comprende :




- Trezor Safe 3;
- Un astuccio contenente cartoncini per registrare la frase Mnemonic, adesivi e istruzioni;
- Cavo da USB-C a USB-C.



![Image](assets/fr/02.webp)



Una volta aperto, il Trezor Safe 3 dovrebbe essere protetto da una plastica protettiva e la porta USB-C dovrebbe essere protetta da un Seal olografico. Assicurarsi che sia presente.



![Image](assets/fr/03.webp)



La navigazione sul dispositivo è semplice: utilizzare il pulsante destro per scorrere verso destra e il pulsante sinistro per scorrere verso sinistra. Premere entrambi i pulsanti contemporaneamente per confermare un'azione.



![Image](assets/fr/04.webp)



## Prerequisiti



In questa esercitazione vi mostrerò come utilizzare Trezor Safe 3 con [Sparrow Wallet portfolio management software](https://sparrowwallet.com/download/). Se non avete ancora installato questo software, fatelo subito. Se avete bisogno di aiuto, abbiamo anche un tutorial dettagliato sulla configurazione di Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

È inoltre necessario il software Trezor Suite per configurare il Safe 3, verificarne l'autenticità e installare il firmware. Utilizzeremo questo software solo per questo, e in seguito sarà necessario solo per gli aggiornamenti del firmware. Per la gestione quotidiana del Wallet, utilizzeremo esclusivamente Sparrow Wallet, in quanto è ottimizzato per il Bitcoin e facile da usare, anche per i principianti (Sparrow supporta solo il Bitcoin, non le altcoin).



[Scarica Trezor Suite dal sito ufficiale](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Per entrambi i programmi, consiglio vivamente di verificarne l'autenticità (con GnuPG) e l'integrità (tramite Hash) prima di installarli sul computer. Se non sapete come fare, potete seguire quest'altra guida:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Avvio di Trezor Safe 3



Collegare il Safe 3 al computer dove sono già installati Trezor Suite e Sparrow Wallet.



![Image](assets/fr/06.webp)



Aprire Trezor Suite, quindi fare clic su "*Impostare il mio Trezor*".



![Image](assets/fr/07.webp)



Selezionare "*Firmware solo Bitcoin*", quindi fare clic su "*Installa Bitcoin*".



![Image](assets/fr/08.webp)



Trezor Suite installerà quindi il firmware sul Safe 3. Attendere durante l'installazione.



![Image](assets/fr/09.webp)



Fare clic su "*Continua*".



![Image](assets/fr/10.webp)



Procedere quindi al test di autenticità per assicurarsi che il Hardware Wallet non sia falso o compromesso.



![Image](assets/fr/11.webp)



Sul Safe 3, premere il pulsante destro per confermare.



![Image](assets/fr/12.webp)



Se il Trezor è autentico, in Trezor Suite apparirà un messaggio di conferma.



![Image](assets/fr/13.webp)



È quindi possibile saltare le finestre con le istruzioni operative di base.



![Image](assets/fr/14.webp)



## Creare un portafoglio Bitcoin



Su Trezor Suite, fare clic sul pulsante "*Crea nuovo Wallet*".



![Image](assets/fr/15.webp)



Per un portafoglio standard, si può optare per il tipo di backup predefinito. In questo modo si crea un portafoglio classico a sigla singola con una frase Mnemonic di 12 parole. Fare clic su "*Crea Wallet*".



Se volete saperne di più sulle altre opzioni di backup disponibili su Trezor, tra cui *Multi-share Backup*, vi consiglio di consultare anche questo tutorial:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Accettare le condizioni di utilizzo del Hardware Wallet.



![Image](assets/fr/17.webp)



Premere nuovamente il pulsante destro per creare un nuovo portafoglio.



![Image](assets/fr/18.webp)



In Trezor Suite, fare clic su "*Continua il backup*".



![Image](assets/fr/19.webp)



Il software fornisce istruzioni su come gestire la frase Mnemonic.



Questo Mnemonic vi dà accesso completo e illimitato a tutti i vostri bitcoin. Chiunque sia in possesso di questa frase può rubare i vostri fondi, anche senza avere accesso fisico alla vostra Trezor Safe 3.



La frase di 12 parole ripristina l'accesso ai vostri bitcoin in caso di smarrimento, furto o rottura del vostro Hardware Wallet. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.



Potete scriverlo sul cartoncino fornito nella scatola, oppure, per maggiore sicurezza, vi consiglio di inciderlo su una base in acciaio inossidabile per proteggerlo da incendi, allagamenti o crolli.



Confermare le istruzioni, quindi fare clic sul pulsante "*Crea backup Wallet*".



![Image](assets/fr/20.webp)



Safe 3 creerà la vostra frase Mnemonic utilizzando il suo generatore di numeri casuali. Assicuratevi di non essere osservati durante questa operazione. Scrivete le parole fornite sullo schermo su un supporto fisico di vostra scelta. A seconda della vostra strategia di sicurezza, potete pensare di fare diverse copie fisiche complete della frase (ma soprattutto non dividetela). È importante che le parole siano numerate e in ordine sequenziale.



***Ovviamente, non dovete mai condividere queste parole su Internet, come faccio io in questa esercitazione. Questo esempio di Wallet sarà utilizzato solo sul Testnet e sarà cancellato alla fine del tutorial



Per ulteriori informazioni sul modo corretto di salvare e gestire la frase Mnemonic, vi consiglio di seguire quest'altra guida, soprattutto se siete principianti:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Per passare alle parole successive, fare clic con il tasto destro del mouse. È possibile andare indietro facendo clic sul pulsante sinistro. Una volta scritte tutte le parole, tenere premuto il tasto destro per passare alla fase successiva.



![Image](assets/fr/22.webp)



Selezionare le parole della frase Mnemonic in base al loro ordine per confermare che sono state scritte correttamente. Utilizzare i pulsanti destro e sinistro per spostarsi tra le proposte, quindi selezionare la parola corretta facendo clic contemporaneamente sui due pulsanti.



![Image](assets/fr/23.webp)



Una volta completata la procedura di verifica, fare clic sul pulsante a destra.



![Image](assets/fr/24.webp)



## Impostazione del codice PIN



Poi si passa alla fase del codice PIN. Il codice PIN sblocca il Trezor. Pertanto, fornisce una protezione contro l'accesso fisico non autorizzato. Il codice PIN non partecipa alla creazione delle chiavi crittografiche del Wallet. Pertanto, anche in assenza di accesso al codice PIN, il possesso della frase Mnemonic di 12 parole consentirà al Trezor di accedere al dispositivo. Quindi, anche senza accesso al codice PIN, il possesso della frase Mnemonic di 12 parole vi permetterà di riavere accesso ai vostri bitcoin.



Su Trezor Suite, fare clic su "*Continua a PIN*", quindi sul pulsante "*Imposta PIN*".



![Image](assets/fr/25.webp)



Confermare con Safe 3.



![Image](assets/fr/26.webp)



Si consiglia di scegliere un codice PIN il più possibile casuale. Assicurarsi di salvare questo codice in un luogo diverso da quello in cui è memorizzato il Trezor (ad esempio, in un gestore di password). È possibile definire un codice PIN di un numero compreso tra 8 e 50 cifre. Si consiglia di scegliere un codice PIN il più lungo possibile per aumentare la sicurezza.



Utilizzare i pulsanti destro e sinistro per selezionare ogni cifra. Per confermare la scelta e passare alla cifra successiva, premere entrambi i pulsanti contemporaneamente.



![Image](assets/fr/27.webp)



Al termine, fare clic sul segno di spunta "*INVIO*" all'inizio delle cifre, quindi confermare il PIN una seconda volta.



![Image](assets/fr/28.webp)



Il codice PIN è stato registrato.



![Image](assets/fr/29.webp)



Su Trezor Suite, fare clic sul pulsante "*Completa la configurazione*".



![Image](assets/fr/30.webp)



La configurazione del Safe 3 è ora completa. Se lo si desidera, è possibile modificare il nome e la pagina iniziale del Hardware Wallet.



![Image](assets/fr/31.webp)



Non avremo più bisogno del software Trezor Suite, se non per eseguire gli aggiornamenti regolari del firmware sul Hardware Wallet o per eseguire un test di ripristino. Ora utilizzeremo Sparrow per gestire il portafoglio, poiché questo software è perfettamente adatto all'uso esclusivo del Bitcoin.



## Impostazione del portafoglio su Sparrow Wallet



Iniziate scaricando e installando Sparrow Wallet [dal sito ufficiale](https://sparrowwallet.com/) sul vostro computer, se non l'avete ancora fatto.



Una volta aperto Sparrow Wallet, assicuratevi che il software sia collegato a un nodo Bitcoin, indicato dal segno di spunta nell'angolo in basso a destra del Interface. Se avete problemi a collegare Sparrow, vi consiglio di leggere l'inizio di questa guida:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Fare clic sulla scheda "*File*", quindi su "*Nuovo Wallet*".



![Image](assets/fr/32.webp)



Assegnare un nome al portafoglio, quindi fare clic su "*Crea Wallet*".



![Image](assets/fr/33.webp)



Nel menu a discesa "*Tipo di script*", selezionare il tipo di script che verrà utilizzato per proteggere i bitcoin. Io consiglio "*Taproot*" o, in mancanza, "*Native SegWit*".



![Image](assets/fr/34.webp)



Fare clic sul pulsante "*Connected Hardware Wallet*". Il Safe 3 deve ovviamente essere collegato al computer e sbloccato.



![Image](assets/fr/35.webp)



Fare clic sul pulsante "*Scan*". Dovrebbe apparire il vostro Safe 3. Fare clic su "*Importa Keystore*".



![Image](assets/fr/36.webp)



Ora è possibile visualizzare i dettagli del proprio Wallet, compresa la chiave pubblica estesa del primo account. Fare clic sul pulsante "*Apply*" per completare la creazione del Wallet.



![Image](assets/fr/37.webp)



Scegliete una password forte per proteggere l'accesso a Sparrow Wallet. Questa password garantirà un accesso sicuro ai dati di Sparrow Wallet, proteggendo le chiavi pubbliche, gli indirizzi, le etichette e la cronologia delle transazioni da accessi non autorizzati.



Vi consiglio di salvare questa password in un gestore di password per non dimenticarla.



![Image](assets/fr/38.webp)



E ora il vostro portafoglio è stato importato in Sparrow Wallet!



![Image](assets/fr/39.webp)



Prima di ricevere i primi bitcoin nel Wallet, **consiglio vivamente di eseguire un test di ripristino a vuoto**. Annota alcune informazioni di riferimento, come il tuo xpub, quindi resetta il tuo Trezor Safe 3 mentre il Wallet è ancora vuoto. Quindi provare a ripristinare il Wallet sul Trezor utilizzando i backup cartacei. Verificare che l'xpub generato dopo il ripristino corrisponda a quello scritto in origine. Se così fosse, si può essere certi che i backup cartacei sono affidabili.



Per saperne di più su come eseguire un test di ripristino, vi suggerisco di consultare quest'altra guida:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Come posso ricevere bitcoin con Trezor Safe 3?



Su Sparrow, fare clic sulla scheda "*Receive*".



![Image](assets/fr/40.webp)



Prima di utilizzare il Address proposto da Sparrow Wallet, verificatelo sullo schermo del vostro Trezor. Questa pratica consente di confermare che il Address visualizzato su Sparrow non è fraudolento e che il Hardware Wallet contiene effettivamente la chiave privata necessaria per spendere successivamente i bitcoin garantiti con questo Address. Ciò consente di evitare diversi tipi di attacco.



Per eseguire questo controllo, fare clic sul pulsante "*Visualizza Address*".



![Image](assets/fr/41.webp)



Verificare che il Address visualizzato sul Trezor corrisponda a quello del Wallet di Sparrow. È consigliabile effettuare questo controllo anche prima di comunicare il Address al mittente, per essere sicuri della sua validità. È possibile utilizzare i pulsanti per confermare.



![Image](assets/fr/42.webp)



È quindi possibile aggiungere una "*Etichetta*" per descrivere la fonte di bitcoin che verrà assicurata con questo Address. Questa è una buona pratica che consente di gestire meglio gli UTXO.



![Image](assets/fr/43.webp)



È quindi possibile utilizzare questo Address per ricevere bitcoin.



![Image](assets/fr/44.webp)



## Come si inviano i bitcoin con Trezor Safe 3?



Ora che avete ricevuto i vostri primi Satss sul vostro Safe 3-secured Wallet, potete anche spenderli! Collegate il vostro Trezor al computer, sbloccatelo con il codice PIN, lanciate Sparrow Wallet, quindi andate alla scheda "*Invio*" per creare una nuova transazione.



![Image](assets/fr/45.webp)



Se si desidera *controllare le monete*, ossia scegliere specificamente quali UTXO consumare nella transazione, andare alla scheda "*UTXO*". Selezionare gli UTXO che si desidera spendere, quindi fare clic su "*Invia selezionati*". Si verrà reindirizzati alla stessa schermata della scheda "*Invio*", ma con gli UTXO già selezionati per la transazione.



![Image](assets/fr/46.webp)



Inserire la destinazione Address. È possibile inserire più indirizzi facendo clic sul pulsante "*+ Aggiungi*".



![Image](assets/fr/47.webp)



Scrivete una "*Etichetta*" per ricordare lo scopo di questa spesa.



![Image](assets/fr/48.webp)



Selezionare l'importo da inviare a questo Address.



![Image](assets/fr/49.webp)



Regolate il tasso di commissione della vostra transazione in base al mercato attuale. Ad esempio, è possibile utilizzare [Mempool.space](https://Mempool.space/) per scegliere una tariffa adeguata.



Assicurarsi che tutti i parametri della transazione siano corretti, quindi fare clic su "*Crea transazione*".



![Image](assets/fr/50.webp)



Se tutto è di vostro gradimento, cliccate su "*Finalizza la transazione per la firma*".



![Image](assets/fr/51.webp)



Fare clic su "*Firma*".



![Image](assets/fr/52.webp)



Fare clic su "*Sign*" accanto al proprio Trezor Safe 3.



![Image](assets/fr/53.webp)



Controllare i parametri della transazione sullo schermo del Hardware Wallet, compresi il Address ricevente del destinatario, l'importo inviato e l'addebito. Una volta verificata la transazione sul Trezor, fare clic su entrambi i pulsanti contemporaneamente per firmarla.



![Image](assets/fr/54.webp)



La transazione è ora firmata. Verificate un'ultima volta che tutto sia a posto, quindi fate clic su "*Diffusione della transazione*" per trasmetterla sulla rete Bitcoin.



![Image](assets/fr/55.webp)



Si trova nella scheda "*Transazioni*" di Sparrow Wallet.



![Image](assets/fr/56.webp)



Congratulazioni, ora siete al corrente dell'uso di base del Trezor Safe 3 con Sparrow Wallet! Per fare un ulteriore passo avanti, vi consiglio questo tutorial completo sull'uso di un Trezor Hardware Wallet con un BIP39 passphrase per aumentare la vostra sicurezza:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Se questa esercitazione vi è stata utile, vi sarei grato se lasciaste un pollice Green qui sotto. Sentitevi liberi di condividere questo articolo sui vostri social network. Grazie mille!
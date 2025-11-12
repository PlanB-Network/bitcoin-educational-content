---
name: Seedkeeper x SeedSigner
description: Come posso utilizzare Seedkeeper con il mio SeedSigner?
---

![cover](assets/cover.webp)



*Grazie al team di [Satochip](https://satochip.io/) per aver accettato di riutilizzare i [loro video](https://www.youtube.com/@satochip/videos) in questa guida. Grazie anche a [Crypto Guide](https://www.youtube.com/@CryptoGuide/) per il suo fork del firmware di SeedSigner, che consente il supporto delle smartcard



---

Il SeedSigner è un hardware wallet che si assembla da solo a partire da hardware standard, di solito intorno a un Raspberry Pi Zero. Questo wallet è definito "*stateless*": a differenza della maggior parte degli altri modelli presenti sul mercato (Coldcard, Trezor, Ledger, ecc.), non memorizza alcun dato nella memoria permanente e opera solo in diretta dalla RAM. Di conseguenza, il seed del vostro portafoglio non viene mai memorizzato sul SeedSigner. Ogni volta che si riavvia, è necessario inserirlo per consentire al dispositivo di firmare le transazioni. Il metodo più comune è quello di salvare il seed come codice QR, da scansionare ogni volta che lo si utilizza (*SeedQR*).



Questo approccio presenta tuttavia un rischio significativo: il seed deve rimanere accessibile in chiaro per poter essere scansionato. In caso di furto o intrusione, un aggressore potrebbe facilmente impossessarsene e rubare i bitcoin.



Per superare questa debolezza, SeedSigner può essere combinato con [**Seedkeeper**](https://satochip.io/product/seedkeeper/), una smart card sviluppata da Satochip. Ciò consente di memorizzare frasi mnemoniche (o altri segreti) in una secure element protetta da un codice PIN. L'applet Seedkeeper è open-source e il suo secure element è certificato EAL6+. Utilizzata insieme a SeedSigner, offre una caratteristica di sicurezza molto interessante: le chiavi rimangono gestite interamente off-line, si firmano le transazioni su uno schermo affidabile e il seed è fisicamente protetto in una smartcard resistente agli attacchi fisici.



Per completare l'installazione sono necessari i seguenti elementi:




- L'attrezzatura necessaria per un SeedSigner classico è la solita: un Raspberry Pi Zero, uno schermo Waveshare da 1,3 pollici, una fotocamera compatibile e una scheda microSD (troverete maggiori dettagli nel tutorial SeedSigner qui sotto);
- Il kit di estensione SeedSigner, disponibile [sul negozio ufficiale Satochip](https://satochip.io/product/seedsigner-extension-kit/), che consente di leggere e scrivere sulla smartcard direttamente dal SeedSigner. Un'altra opzione è quella di utilizzare un lettore di smartcard esterno, che può essere collegato via cavo a una porta Micro-USB del Raspberry Pi. Tuttavia, non ho testato personalmente questa soluzione;
- Un Seedkeeper, o in alternativa una smartcard vuota su cui installare l'applet Seedkeeper (il kit di estensione venduto da Satochip include già una smartcard vuota).



![Image](assets/fr/01.webp)



Questa esercitazione copre due scenari:




- Se si dispone già di un portafoglio Bitcoin gestito tramite SeedSigner, è sufficiente installare il nuovo firmware. Potete quindi continuare a utilizzare il vostro wallet esistente, questa volta utilizzando Seedkeeper per una maggiore sicurezza.
- Se non si dispone ancora di un Bitcoin wallet associato al SeedSigner, è necessario seguire i passaggi **5** e **6** dell'esercitazione riportata di seguito. Queste sezioni spiegano come generate una frase mnemonica con il SeedSigner, salvarla tramite un *SeedQR* e quindi collegare questo wallet al Sparrow Wallet per gestirlo. Non mi soffermerò su queste procedure e **presumo che abbiate già un Bitcoin wallet funzionante, configurato con il Sparrow e il vostro SeedSigner**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Installare il firmware



Per utilizzare SeedSigner con un Seedkeeper, è necessario installare un firmware alternativo, diverso da quello del SeedSigner originale, per supportare la lettura delle smart card. A tale scopo, [consiglio di utilizzare il fork di "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Scaricare [l'ultima versione dell'immagine](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) corrispondente al modello di Raspberry Pi in uso.



![Image](assets/fr/02.webp)



Se non lo si possiede già, scaricare il software [Balena Etcher] (https://etcher.balena.io/), quindi procedere come segue:




- Inserire la scheda microSD nel computer;
- Avvio di Etcher ;
- Selezionare il file `.zip' appena scaricato;
- Selezionare la scheda microSD come destinazione;
- Fare clic su `Flash!`.



![Image](assets/fr/03.webp)



Attendere il completamento del processo: la microSD è pronta per l'uso. Ora si può passare all'assemblaggio del dispositivo.



Per maggiori dettagli sull'installazione del firmware e sulla verifica del software (un'operazione che vi consiglio vivamente di fare), consultate la seguente guida:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Montaggio del lettore di smartcard



![video](https://youtu.be/jqE8HDMCImA)



Iniziare a installare la fotocamera sul Raspberry Pi Zero, inserendola con attenzione nel perno della fotocamera e bloccandola con la linguetta nera. Quindi posizionate il Pi sul fondo del case, assicurandovi di allineare le porte con le aperture corrispondenti.



![Image](assets/fr/04.webp)



Quindi collegare il lettore di smart card ai pin GPIO del Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Far scorrere il coperchio di plastica sul lettore di smart card fino a posizionarlo correttamente.



![Image](assets/fr/06.webp)



Quindi aggiungere lo schermo ai pin GPIO dell'estensione.



![Image](assets/fr/07.webp)



Infine, inserire la scheda microSD contenente il firmware nella porta laterale del Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Ora è possibile collegare SeedSigner tramite la porta Micro-USB di Raspberry Pi Zero o tramite la porta USB-C dell'estensione. Entrambe le opzioni funzionano. Attendete qualche secondo per l'avvio e poi vedrete apparire la schermata di benvenuto.



![Image](assets/fr/09.webp)



Per maggiori dettagli sulla configurazione iniziale di SeedSigner, vi consiglio di consultare il seguente tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flashare una smartcard con l'applet Seedkeeper (opzionale)



![video](https://youtu.be/NF4HemyEcOY)



Se possedete già un Seedkeeper, potete saltare questo passaggio e passare direttamente al punto 4. In questa sezione vedremo come installare l'applet Seedkeeper su una smartcard vuota (metodo fai da te).



Per iniziare, aprire il menu `Strumenti > Strumenti Smartcard` su SeedSigner.



![Image](assets/fr/10.webp)



Quindi selezionare `Strumenti fai da te > Installa applet`.



![Image](assets/fr/11.webp)



Inserire la smartcard nel lettore SeedSigner, con il chip rivolto verso il basso, quindi scegliere l'applet `SeedKeeper`.



![Image](assets/fr/12.webp)



Si prega di avere pazienza durante l'installazione: il processo potrebbe richiedere alcune decine di secondi.



![Image](assets/fr/13.webp)



Una volta che l'applet è stata installata con successo, si può procedere al punto 4.



![Image](assets/fr/14.webp)



## 4. Salvare un SeedQR esistente su Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Ora che il Seedkeeper è operativo, è possibile salvare il mnemonico Bitcoin wallet sulla smartcard. Per iniziare, accendere il SeedSigner come di consueto, quindi scansionare il *SeedQR* del wallet per caricarlo nel dispositivo. Una volta importato il seed, è sufficiente selezionare "Fatto".



![Image](assets/fr/15.webp)



Quando il seed è caricato, accedere al menu `Backup Seed`.



![Image](assets/fr/16.webp)



Inserire quindi il Seedkeeper nell'unità SeedSigner e selezionare l'opzione "A SeedKeeper".



![Image](assets/fr/17.webp)



Il SeedSigner vi chiederà quindi di inserire un codice PIN per il vostro Seedkeeper. Poiché si tratta di una carta vuota, non è ancora stato definito alcun codice. Immettere un codice qualsiasi per saltare questo passaggio, quindi convalidare.



![Image](assets/fr/18.webp)



SeedSigner rileva che Seedkeeper non è ancora stato inizializzato (cioè non è stata impostata alcuna password). Fare clic su "Ho capito" per continuare.



![Image](assets/fr/19.webp)



Ora scegliete il nuovo codice PIN del vostro Seedkeeper, compreso tra 4 e 16 caratteri. Per maggiore sicurezza, scegliete un codice lungo e casuale: è l'unica barriera che protegge l'accesso fisico alla vostra frase mnemonica.



Ricordate di salvare il PIN appena creato, in un gestore di password affidabile o su un supporto fisico separato, a seconda della vostra strategia. In quest'ultimo caso, assicuratevi di non tenere mai il supporto contenente il PIN nello stesso posto del vostro Seedkeeper, altrimenti la protezione diventerà inefficace. È importante avere una copia di backup: **Senza questo PIN, non sarà possibile accedere al proprio seed e i bitcoin andranno persi**.



![Image](assets/fr/20.webp)



È quindi possibile definire una `etichetta` associata alla frase mnemonica. Questa etichetta è utile se si memorizzano diversi segreti su Seedkeeper, in modo da poterli identificare facilmente.



![Image](assets/fr/21.webp)



La frase mnemonica è ora salvata sulla smartcard.



![Image](assets/fr/22.webp)



In termini di strategia di sicurezza, sono possibili diversi approcci, a seconda delle esigenze e del livello di esposizione al rischio. Personalmente, consiglio di conservare almeno 2 copie del proprio seed:




- Si tratta di una novità assoluta per le smartcard, che si possono tenere facilmente accessibili per le operazioni quotidiane, come la verifica degli indirizzi o la firma delle transazioni. Questo metodo è pratico (come vedremo nella parte 5) e rimane sicuro grazie alla protezione offerta dal codice PIN, per cui è possibile tenerla accessibile senza grossi rischi;
- Una seconda copia della frase mnemonica non criptata, che funge da backup definitivo del portafoglio, da utilizzare solo in caso di perdita o furto del Seedkeeper. Poiché questa versione non è criptata, deve essere conservata in un luogo separato e più sicuro, per evitare la compromissione simultanea dei due backup.



A seconda della vostra strategia di protezione e del vostro profilo di rischio, potete anche duplicare il seed su diversi Seedkeeper o creare diverse copie fisiche del mnemonico. Per saperne di più su queste pratiche, consultate il seguente tutorial:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Caricamento di un seed da Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Ora è possibile utilizzare il Seedkeeper per caricare la frase mnemonica nel SeedSigner all'avvio, e firmare così le transazioni Bitcoin. Per iniziare, accendere il SeedSigner collegandolo alla presa di corrente, quindi aprire il menu "Seeds".



![Image](assets/fr/23.webp)



Quindi selezionare l'opzione "Da SeedKeeper".



![Image](assets/fr/24.webp)



Inserire il Seedkeeper nel lettore di smart card, quindi inserire il codice PIN per sbloccarlo. Confermare l'immissione premendo il pulsante di conferma in basso a destra, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper può contenere diversi segreti, quindi SeedSigner chiede di scegliere quello che si desidera caricare. L'etichetta visualizzata corrisponde al nome definito al punto 4. Se, come nel mio caso, avete registrato un solo seed, sarà disponibile una sola opzione.



![Image](assets/fr/26.webp)



Il seed è ora caricato. Verificare che si tratti del wallet corretto confrontando l'impronta digitale visualizzata sullo schermo con quella specificata nelle impostazioni del Sparrow e del Wallet. Questa impronta digitale è stata fornita anche al momento della prima creazione del wallet.



Se si utilizza un passphrase, è possibile applicarlo in questa fase (vedere la parte 6 di questa guida). Altrimenti, fare semplicemente clic su "Fatto".



![Image](assets/fr/27.webp)



Potete quindi utilizzare il vostro wallet come al solito: controllare gli indirizzi di consegna e firmare le transazioni, proprio come con un SeedSigner classico. Per saperne di più su come utilizzarlo, consultate il tutorial dedicato:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Utilizzo di Seedkeeper con un passphrase BIP39



State utilizzando un passphrase per proteggere il vostro portafoglio Bitcoin? Potete registrarlo nel Seedkeeper, insieme al seed. Questa soluzione vi consentirà di caricare rapidamente il vostro wallet sul SeedSigner, senza dover inserire manualmente il passphrase sulla piccola tastiera ogni volta che lo utilizzate.



Trovo questo metodo particolarmente interessante, in quanto consente di beneficiare dei vantaggi di sicurezza del passphrase, eliminando al contempo i vincoli associati al suo utilizzo quotidiano. Ecco un esempio di configurazione che consiglio:




- Conservate i vostri seed e passphrase in un Seedkeeper, protetto da un codice PIN forte (questo è importante). Questo backup vi consentirà di utilizzare facilmente il vostro wallet su base giornaliera. Se lo si desidera, è possibile duplicare queste informazioni su un secondo Seedkeeper;
- Conservate anche una copia chiara del vostro mnemonico e del passphrase, su carta o metallo. Si tratta di un backup di ultima istanza se si perde il Seedkeeper o il suo PIN. Assicuratevi di conservare queste copie in luoghi separati, in modo che non possano essere compromesse contemporaneamente.



In questa configurazione, se qualcuno mette le mani sul vostro mnemonico in chiaro, non sarà in grado di rubare nulla senza conoscere il passphrase (a condizione, naturalmente, che sia abbastanza forte da resistere a un attacco di forza bruta). Al contrario, se qualcuno scopre il vostro passphrase in chiaro, questo rimarrà inutilizzabile senza la frase mnemonica corrispondente.



Infine, se qualcuno riesce ad accedere fisicamente al vostro Seedkeeper contenente il seed e il passphrase, non sarà in grado di estrarre nulla senza conoscere il codice PIN. A differenza del passphrase, questo codice non può essere forzato, poiché la smartcard si blocca automaticamente dopo 5 tentativi non validi.



La sicurezza di questa configurazione si basa quindi su due punti essenziali:




- Un **passphrase forte**: deve essere lungo, casuale e contenere un'ampia varietà di caratteri. La sua complessità non è un problema per voi, poiché dovrete inserirlo solo una volta sulla tastiera durante l'inizializzazione; in seguito, sarà trasmesso da Seedkeeper ;
- Un **codice PIN** per Seedkeeper: anch'esso casuale e composto da 16 caratteri.



Per impostare questa configurazione, iniziare a caricare il passphrase nel SeedSigner nel modo consueto. È possibile seguire la procedura descritta in questo tutorial:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Una volta che il portafoglio con il passphrase è stato caricato correttamente sul SeedSigner, aprire il menu `Seeds` e selezionare l'impronta corrispondente a questo portafoglio. Si noti che questa impronta differisce da quella del portafoglio senza passphrase.



![Image](assets/fr/28.webp)



Quindi fare clic su `Backup Seed`, inserire il Seedkeeper nell'unità e selezionare `To SeedKeeper`.



![Image](assets/fr/29.webp)



Inserire il PIN per sbloccare Seedkeeper, quindi assegnare un'etichetta a questo segreto. Si può lasciare l'impronta digitale come etichetta per mantenere una forma di negazione plausibile, oppure dichiarare esplicitamente `Passphrase Wallet`, ad esempio.



![Image](assets/fr/30.webp)



Il vostro portafoglio passphrase è ora registrato su Seedkeeper.



![Image](assets/fr/31.webp)



All'avvio successivo, inserire il Seedkeeper nell'unità, quindi navigare in `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Inserire il PIN per sbloccare la smartcard, quindi selezionare il wallet corrispondente al passphrase.



![Image](assets/fr/33.webp)



Controllare l'impronta del passphrase e del wallet, quindi confermare.



![Image](assets/fr/34.webp)



Ora potete accedere al vostro portafoglio con passphrase e firmare le vostre transazioni come fareste normalmente con SeedSigner.



## 7. Opzioni aggiuntive



Nel menu `Strumenti > Strumenti Smartcard` sono disponibili diverse opzioni per la gestione di Seedkeeper:





- Nel menu `Strumenti comuni` è possibile :
 - Controllare l'autenticità della carta;
 - Modifica del codice PIN ;
 - Modificare le etichette associate ai segreti;
 - Disattivare la funzione NFC (consigliato se si usa solo il lettore di chip) ;
 - Eseguire un reset di fabbrica.





- Nel menu `Funzioni SeedKeeper` è possibile :
 - Consultare l'elenco dei segreti registrati ;
 - Salvare un nuovo segreto ;
 - Cancellare un segreto esistente ;
 - Salvare o caricare i descrittori (funzione utile per i portafogli multi-sig).





- Nel menu `Strumenti fai da te`, è possibile :
 - Compilazione dell'applet Seedkeeper ;
 - Installare l'applet su una scheda vuota ;
 - Eliminare un'applet Seedkeeper per resettarla e renderla nuovamente vuota.



Ora sapete come utilizzare Seedkeeper per eseguire il backup del vostro portafoglio in modo sicuro in combinazione con SeedSigner.



Se questa impostazione vi ha convinto, non esitate a sostenere i progetti che la rendono possibile:




- Acquistando direttamente l'apparecchiatura [sul sito web di Satochip](https://satochip.io/shop/);
- Facendo [una donazione al progetto SeedSigner](https://seedsigner.com/donate/);
- Iscrivendosi al canale YouTube di [Crypto Guide] (https://www.youtube.com/@CryptoGuide/), gestito dalla persona che gestisce il repository GitHub che ospita il firmware modificato.
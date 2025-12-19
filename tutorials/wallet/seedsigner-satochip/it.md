---
name: Satochip x SeedSigner
description: Come utilizzare un Satochip con il vostro SeedSigner?
---

![cover](assets/cover.webp)



*Si ringrazia [Crypto Guide](https://www.youtube.com/@CryptoGuide/) per il suo fork del firmware di SeedSigner per il supporto delle smartcard, che utilizzeremo in questo tutorial



---

Satochip è un hardware in formato smart card wallet con un elemento di sicurezza certificato EAL6+, uno dei più alti standard di sicurezza. È progettato e prodotto dall'omonima azienda belga: Satochip.



Al prezzo di circa 25 euro, Satochip si distingue dalla concorrenza per l'eccellente rapporto qualità-prezzo. Grazie al suo chip sicuro, offre resistenza agli attacchi fisici. Inoltre, il codice sorgente dell'applet è interamente open-source, con licenza *AGPLv3*.



D'altra parte, il suo formato impone alcune limitazioni funzionali. Il principale inconveniente di Satochip è l'assenza di uno schermo integrato: gli utenti devono quindi firmare le transazioni alla cieca, affidandosi esclusivamente al display del computer.



Per ovviare a questa debolezza, una configurazione particolarmente interessante è quella di utilizzarlo insieme a un SeedSigner. In questa configurazione, la comunicazione non avviene più direttamente tra il computer e lo Satochip, ma attraverso lo scambio di codici QR tra il computer e il SeedSigner. Il SeedSigner funge quindi da schermo fiduciario: visualizza le informazioni da firmare, mentre la firma stessa viene eseguita dal Satochip. A differenza dell'uso convenzionale del SeedSigner (o anche dell'uso in combinazione con Seedkeeper), il seed non viene mai caricato nel SeedSigner. Il SeedSigner diventa quindi lo schermo dello Satochip, eliminando i rischi associati alla firma cieca.



Se consideriamo il problema dal punto di vista opposto, l'uso del SeedSigner con uno Satochip colma un'importante lacuna del SeedSigner: la possibilità di memorizzare e utilizzare il seed all'interno di un secure element.



A mio avviso, questa configurazione offre diversi vantaggi rispetto ai portafogli hardware tradizionali:




- Il Satochip costa circa 25 euro e, poiché l'applet è open-source, è possibile installarlo da soli su una smartcard vuota. Occorre poi aggiungere il costo dei componenti di SeedSigner e dell'estensione per la lettura delle smartcard: a seconda di dove si acquista l'hardware, il totale dovrebbe essere compreso tra 70 e 100 euro.
- Tutto il software coinvolto nella configurazione è open-source: il firmware SeedSigner e l'applet Satochip.
- Beneficiate di un elemento di sicurezza certificato.
- La configurazione può essere effettuata interamente in modo fai-da-te, senza ricorrere a hardware esplicitamente destinato all'uso del Bitcoin, il che può fornire una forma di negazione plausibile e di resistenza ad alcune minacce esterne (tra cui, a seconda del paese, la pressione dello Stato). Questa è anche una soluzione interessante se l'accesso ai portafogli hardware commerciali è limitato o impossibile nella vostra regione.




## 1. Materiali necessari



Per eseguire questa configurazione, sono necessari i seguenti elementi:




- L'attrezzatura abituale di un SeedSigner classico:
 - un Raspberry Pi Zero con pin GPIO,
 - 1.schermo Waveshare da 3",
 - una fotocamera compatibile,
 - una scheda microSD.



![Image](assets/fr/01.webp)





- Il kit di estensione SeedSigner, disponibile [presso il negozio ufficiale Satochip](https://satochip.io/product/seedsigner-extension-kit/), che consente di leggere e scrivere su una smartcard direttamente dal SeedSigner. Un'altra opzione è quella di utilizzare [un lettore di smartcard esterno](https://satochip.io/product/chip-card-reader/), che può essere collegato via cavo a una porta Micro-USB del Raspberry Pi. Tuttavia, non ho testato personalmente questa soluzione;
- [A Satochip](https://satochip.io/product/satochip/), o in alternativa una [smartcard vuota](https://satochip.io/product/card-for-diy-project/) su cui installare l'applet Satochip (il kit di estensione venduto da Satochip include già una smartcard vuota). Il kit di estensione di Satochip supporta anche il formato [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). È quindi possibile optare per questo formato, se si preferisce.



![Image](assets/fr/02.webp)



Per maggiori dettagli sull'attrezzatura necessaria per assemblare un SeedSigner, consultare la Parte 1 di questo altro tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Installare il firmware



Per utilizzare il SeedSigner con un Satochip, è necessario installare un firmware alternativo, diverso da quello del SeedSigner originale, per supportare la lettura delle smart card. A tale scopo, [consiglio di utilizzare il fork di "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Scaricare [l'ultima versione dell'immagine](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) corrispondente al modello di Raspberry Pi in uso.



![Image](assets/fr/03.webp)



Se non lo si possiede già, scaricare il software [Balena Etcher] (https://etcher.balena.io/), quindi procedere come segue:




- Inserire la scheda microSD nel computer;
- Avvio di Etcher ;
- Selezionare il file `.zip' appena scaricato;
- Selezionare la scheda microSD come destinazione;
- Fare clic su `Flash!`.



![Image](assets/fr/04.webp)



Attendere il completamento del processo: la microSD è pronta per l'uso. Ora si può passare all'assemblaggio del dispositivo.



Per maggiori dettagli sull'installazione del firmware e sulla verifica del software (un'operazione che vi consiglio vivamente di fare), consultate la seguente guida:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Montaggio del lettore di smartcard



Iniziare a installare la fotocamera sul Raspberry Pi Zero, inserendola con attenzione nel perno della fotocamera e bloccandola con la linguetta nera. Quindi posizionate il Pi sul fondo del case, assicurandovi di allineare le porte con le aperture corrispondenti.



![Image](assets/fr/05.webp)



Quindi collegare il lettore di smart card ai pin GPIO del Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Far scorrere il coperchio di plastica sul lettore di smart card fino a posizionarlo correttamente.



![Image](assets/fr/07.webp)



Quindi aggiungere lo schermo ai pin GPIO dell'estensione.



![Image](assets/fr/08.webp)



Infine, inserire la scheda microSD contenente il firmware nella porta laterale del Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Ora è possibile collegare SeedSigner tramite la porta Micro-USB di Raspberry Pi Zero o tramite la porta USB-C dell'estensione. Entrambe le opzioni funzionano. Attendete qualche secondo per l'avvio e poi vedrete apparire la schermata di benvenuto.



![Image](assets/fr/10.webp)



Per maggiori dettagli sulla configurazione iniziale di SeedSigner, si consiglia di consultare la parte 4 del seguente tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flashare una smartcard con l'applet Satochip (opzionale)



Se si possiede già un Satochip, si può saltare questo passaggio e andare direttamente al punto 4. In questa sezione vedremo come installare l'applet Satochip su una smartcard vuota (metodo fai da te). L'applet è semplicemente un piccolo programma in esecuzione sulla smartcard che consente di gestire funzioni specifiche.



Per iniziare, aprire il menu `Strumenti > Strumenti Smartcard` su SeedSigner.



![Image](assets/fr/11.webp)



Quindi selezionare `Strumenti fai da te > Installa applet`.



![Image](assets/fr/12.webp)



Inserire la smartcard nel lettore SeedSigner, con il chip rivolto verso il basso, e selezionare l'applet `Satochip`.



![Image](assets/fr/13.webp)



Si prega di avere pazienza durante l'installazione: il processo potrebbe richiedere alcune decine di secondi.



![Image](assets/fr/14.webp)



Una volta che l'applet è stata installata con successo, si può procedere al punto 4.



![Image](assets/fr/15.webp)




## 5. Creare e salvare seed



### 5.1. Generare seed



Ora che l'hardware e il software funzionano correttamente, si può procedere alla creazione del portafoglio Bitcoin. Per farlo, si collega il SeedSigner, quindi il generate del seed come con un SeedSigner tradizionale. A tale scopo, collegate il vostro SeedSigner, quindi generate il vostro seed come con un SeedSigner convenzionale, lanciando i dadi o scattando una foto:




- Andare al menu `Strumenti > Telecamera / Tiri di dado`;
- Seguire quindi il processo di generazione dell'entropia secondo il metodo scelto;
- Infine, eseguire il backup del seed su un supporto fisico e controllare attentamente il backup.



![Image](assets/fr/16.webp)



Se volete vedere i dettagli di questa procedura, seguite la parte 5 di questa guida:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Salvataggio del seed su un Seedkeeper



Una volta generato il seed, questo è l'unico momento in cui risiede nella RAM del SeedSigner. Nel mio caso, voglio salvarlo su un [Seedkeeper](https://satochip.io/product/seedkeeper/), un altro prodotto Satochip progettato per memorizzare i segreti. Utilizzerò questo dispositivo come ultima risorsa, in caso di perdita del mio Satochip.



La strategia di backup scelta dipende dalle vostre preferenze, ma è indispensabile avere almeno una copia della vostra frase mnemonica, sia su supporto fisico (carta o metallo) sia, come in questo caso, in un Seedkeeper. È inoltre possibile moltiplicare il numero di backup a seconda delle esigenze. Per ulteriori informazioni sulle strategie di backup del portafoglio, vi suggerisco di leggere questo tutorial:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Per eseguire il backup del seed su un Seedkeeper, andare direttamente al menu `Backup Seed`.



![Image](assets/fr/17.webp)



Inserire quindi il Seedkeeper nel lettore di smart card e selezionare "A SeedKeeper".



![Image](assets/fr/18.webp)



Immettere il PIN per sbloccarlo.



![Image](assets/fr/19.webp)



Scegliere una `etichetta` per identificare facilmente i diversi segreti memorizzati su Seedkeeper. È possibile, ad esempio, mantenere semplicemente l'impronta wallet o indicare esplicitamente `Seed`. La scelta dipende dalle vostre preferenze e dai vostri rischi.



![Image](assets/fr/20.webp)



Se la vostra strategia di backup si basa esclusivamente su questo Seedkeeper, vi consiglio vivamente di eseguire subito un test di ripristino vuoto, quindi di confrontare le impronte digitali per verificare che il backup funzioni.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Il codice PIN di Seedkeeper deve essere il più lungo e casuale possibile, per evitare tentativi di forza bruta in caso di compromissione fisica della carta. È inoltre necessario conservare una copia di backup di questo codice PIN, memorizzata in un luogo separato da Seedkeeper. Senza questo PIN, non sarà possibile accedere alla mnemonica memorizzata in Seedkeeper e i bitcoin andranno definitivamente persi.



### 5.3. Risparmiare seed sul Satochip



Ora che il portafoglio è stato generato, salvato e verificato, lo trasferiremo a Satochip. A tale scopo, assicurarsi che il seed sia caricato nella RAM del SeedSigner. Quindi andare su `Strumenti > Strumenti Smartcard > Funzioni Satochip`.



![Image](assets/fr/21.webp)



Inserire lo Satochip nel lettore di smart card, quindi selezionare "Inizializza con Seed".



![Image](assets/fr/22.webp)



Il dispositivo chiede di inserire il codice PIN di Satochip; poiché la scheda è nuova e non inizializzata, non esiste ancora un PIN. Immettere un codice qualsiasi per saltare questo passaggio (non è bloccante).



![Image](assets/fr/23.webp)



Il SeedSigner rileva che il vostro Satochip non è stato inizializzato. Fare clic su "Ho capito" per confermare.



![Image](assets/fr/24.webp)



È quindi possibile impostare il codice PIN Satochip, da 4 a 16 caratteri. Per rafforzare la sicurezza del wallet, scegliete un codice lungo e casuale: è l'unica protezione contro l'accesso fisico alla vostra frase mnemonica.



Ricordate di salvare il PIN appena creato, in un gestore di password sicuro o su un supporto fisico, a seconda della vostra strategia personale. In quest'ultimo caso, assicuratevi di non conservare mai il supporto contenente il PIN nello stesso luogo in cui si trova il vostro Satochip, altrimenti la protezione diventerà inutile. È importante avere una copia di backup: **Senza questo PIN, non sarà possibile accedere al proprio seed e i bitcoin saranno persi per sempre**.



![Image](assets/fr/25.webp)



SeedSigner chiede quindi quale seed importare in Satochip. Selezionare quello la cui impronta digitale corrisponde al portafoglio appena creato.



![Image](assets/fr/26.webp)



Il vostro seed è ora importato nello Satochip.



![Image](assets/fr/27.webp)



Ora potete spegnere il vostro SeedSigner.



Se si desidera utilizzare un passphrase BIP39 per migliorare la sicurezza del wallet, consultare la parte 6 di questa guida:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Importare il wallet nel Sparrow



Ora che il vostro portafoglio è attivo e funzionante, importeremo le sue informazioni pubbliche (il "*keystore*") in Sparrow Wallet o in un altro software di gestione del portafoglio. Questo software verrà utilizzato per creare, distribuire e monitorare le transazioni. Tuttavia, non sarà in grado di firmarle, poiché solo Satochip (ed eventuali backup) detiene le chiavi private necessarie per questa operazione.



### 6.1 Preparazione di SeedSigner e Satochip



Inserire la scheda microSD contenente il sistema operativo, quindi accendere il SeedSigner. Per il momento non può fare nulla, perché non conosce ancora il seed. Dovrete iniziare inserendo lo Satochip nel lettore di smart card, in quanto è quello che contiene il seed.



Dalla schermata principale, accedere al menu `Strumenti > Strumenti Smartcard > Funzioni Satochip`.



![Image](assets/fr/28.webp)



Quindi fare clic su "Esporta Xpub".



![Image](assets/fr/29.webp)



Selezionare il tipo di portafoglio. Nel nostro caso, si tratta di un portafoglio singolo: selezionare `Singolo Sig`.



![Image](assets/fr/30.webp)



Si passa poi alla scelta dello standard di scripting. Scegliere l'ultimo: `Native SegWit`.



![Image](assets/fr/31.webp)



Infine, selezionare il `Coordinatore`, cioè il software di gestione del portafoglio che si desidera utilizzare. In questo caso, utilizzeremo Sparrow Wallet.



![Image](assets/fr/32.webp)



Appare un messaggio di avvertimento: questo è perfettamente normale. La chiave pubblica estesa (`xpub`) consente di visualizzare tutti gli indirizzi derivati dalla propria seed (sul primo conto). Non dà però accesso ai vostri fondi: la sua divulgazione comprometterebbe la vostra privacy, ma non la sicurezza dei vostri bitcoin. In altre parole, vi permette di osservare i vostri saldi, ma non di spenderli.



Fare clic su "Ho capito".



![Image](assets/fr/33.webp)



Inserire quindi il codice PIN di Satochip per sbloccarlo. Si tratta del codice definito e salvato al punto 5.



![Image](assets/fr/34.webp)



Infine, fare clic su `Esporta Xpub` se si è soddisfatti delle informazioni visualizzate.



![Image](assets/fr/35.webp)



Il SeedSigner genera quindi il vostro xpub sotto forma di codice QR dinamico, contenente tutti i dati necessari per gestire il vostro portafoglio in Sparrow Wallet. È possibile regolare la luminosità dello schermo utilizzando il joystick per facilitare la scansione del codice QR.



### 6.2 Importazione di un nuovo portafoglio in Sparrow Wallet



Assicurarsi che il software Sparrow Wallet sia installato sul computer. Se non sapete come scaricarlo, verificarne l'autenticità e installarlo correttamente, consultate il nostro tutorial completo sull'argomento:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Sul computer, aprire il Sparrow Wallet, quindi nella barra dei menu fare clic su `File → Importa Wallet`.



![Image](assets/fr/36.webp)



Scorrere fino a `SeedSigner`, quindi selezionare `Scansione...`. La vostra webcam si attiverà: scansionate il codice QR dinamico visualizzato sullo schermo di SeedSigner.



![Image](assets/fr/37.webp)



Assegnare un nome al portafoglio, quindi fare clic su "Crea Wallet". Il Sparrow chiederà quindi di impostare una password per bloccare l'accesso locale a questo wallet. Scegliete una password forte: protegge i vostri dati nel Sparrow (chiavi pubbliche, indirizzi, etichette e cronologia delle transazioni). Tuttavia, questa password non è necessaria per ripristinare il wallet in futuro: lo sarà solo la vostra frase mnemonica (ed eventualmente il vostro passphrase).



Vi consiglio di salvare questa password in un gestore di password, per evitare di perderla.



![Image](assets/fr/38.webp)



Il keystore è stato importato con successo.



![Image](assets/fr/39.webp)



Verificare ora che l'impronta digitale `Master` visualizzata in Sparrow Wallet corrisponda a quella precedentemente rilevata sul SeedSigner.



SeedSigner vi chiederà quindi di scansionare un indirizzo di ricezione casuale dal vostro Sparrow wallet per confermare la validità dell'importazione.



![Image](assets/fr/40.webp)



Satochip (tramite SeedSigner) e Sparrow Wallet sono ora collegati in modo sicuro. Il Sparrow funge da interfaccia di gestione completa, mentre lo Satochip rimane l'unico dispositivo in grado di firmare le transazioni. Ora siete pronti a ricevere e inviare bitcoin in una configurazione totalmente air-gapped.



![Image](assets/fr/41.webp)



## 7. Ricevere e inviare bitcoin



Satochip e Sparrow Wallet sono ora configurati per lavorare insieme. In questa sezione spiegheremo passo dopo passo come ricevere e inviare bitcoin in questa modalità.



### 7.1 Ricevere bitcoin



#### 7.1.1 Generazione di un indirizzo di ricezione



Sul computer, aprire il Sparrow Wallet e sbloccare il `Satochip-SeedSigner` wallet utilizzando la password. Verificare che il software sia collegato a un server (indicatore in basso a destra). Quindi, nella barra laterale, fare clic su "Ricevi".



![Image](assets/fr/42.webp)



Appare un nuovo indirizzo Bitcoin. Troverete :




- L'indirizzo in formato testo (che inizia con `bc1q...` se si utilizza il P2WPKH, come in questo esempio) ;
- Il codice QR associato ;
- Un campo `Label`, utile per tracciare le transazioni.



Consiglio vivamente di aggiungere un'etichetta a ogni ricevuta di bitcoin nel wallet. Questo vi aiuterà a identificare facilmente la provenienza di ogni UTXO e a gestire meglio la vostra privacy. Per saperne di più su questo importante argomento, consultate la formazione dedicata su Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Per aggiungere un'etichetta, è sufficiente inserire un nome nel campo "Etichetta" e confermare.



Ad esempio:



```txt
Label : Sale of the Raspberry Pi Zero
```



Il vostro indirizzo è ora associato a questa etichetta in tutte le sezioni del Sparrow.



![Image](assets/fr/43.webp)



#### 7.1.2 Verifica del Address sul SeedSigner



Prima di comunicare l'indirizzo di ricezione all'ordinante, è importante verificare che appartenga al proprio seed. Questo passo garantisce che il Satochip sia in grado di firmare le transazioni associate a questo indirizzo. Questo passaggio garantisce che Satochip sia in grado di firmare le transazioni associate a questo indirizzo. Inoltre, previene potenziali attacchi in cui il Sparrow visualizzerebbe un indirizzo fraudolento. Tenete presente che Sparrow funziona su un ambiente insicuro (il vostro computer), la cui superficie di attacco è di gran lunga superiore a quella del vostro Satochip, che è totalmente isolato. Per questo motivo non ci si deve mai fidare ciecamente degli indirizzi visualizzati in Sparrow prima di verificarli sull'hardware wallet.



In Sparrow, fare clic sul codice QR dell'indirizzo per ingrandirlo: verrà quindi visualizzato a schermo intero.



![Image](assets/fr/44.webp)



Sul SeedSigner, inserire il Satochip nel lettore, quindi dal menu principale selezionare "Scansione". Eseguire la scansione del codice QR visualizzato sul computer, quindi selezionare `Usa carta Satochip`.



![Image](assets/fr/45.webp)



Confermare quindi il tipo di script utilizzato (in questo caso, `Native SegWit`), inserire il codice PIN Satochip per sbloccarlo e convalidare le informazioni `xpub`.



![Image](assets/fr/46.webp)



Se l'indirizzo scansionato corrisponde a quello ricavato dal seed, il SeedSigner visualizzerà il messaggio: `Address verificato`.



![Image](assets/fr/47.webp)



In questo modo si può essere certi che l'indirizzo appartenga al proprio portafoglio.



#### 7.1.3 Ricezione dei fondi



A questo punto è possibile trasmettere questo indirizzo in forma di testo o tramite il codice QR alla persona o al reparto che deve inviare i satss. Una volta che la transazione è stata trasmessa in rete, apparirà nella scheda "Transazioni" di Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Inviare bitcoin



L'invio di bitcoin con la configurazione Satochip-SeedSigner prevede 3 fasi:




- Creazione di transazioni in Sparrow ;
- Firma della transazione sul Satochip, tramite il SeedSigner ;
- Infine, la transazione viene trasmessa in rete da Sparrow.



Tutti gli scambi tra i due dispositivi avvengono esclusivamente tramite codici QR.



#### 7.2.1 Creazione della transazione in Sparrow



In Sparrow Wallet, è possibile creare una transazione facendo clic sulla scheda `Invio` nella barra laterale sinistra. Tuttavia, preferisco utilizzare la scheda `UTXOs`, che consente di praticare il *Controllo Coin*. Questo metodo offre un controllo preciso sugli UTXO spesi, per limitare le informazioni rivelate durante le transazioni.



Nella scheda `UTXOs`, selezionare le monete che si desidera spendere, quindi fare clic su `Invia selezionati`.



![Image](assets/fr/49.webp)



Compilare quindi i campi della transazione:




- In `Pagare a`, incollare l'indirizzo del destinatario o scansionare il suo codice QR utilizzando l'icona della fotocamera;
- In `Etichetta`, aggiungere un'etichetta per tracciare questa spesa;
- In "Importo", inserire l'importo da inviare;
- Infine, scegliere la velocità di carica in base alle condizioni attuali della rete (le stime sono disponibili su [mempool.space](https://mempool.space/)).



Una volta completati tutti i campi, controllare attentamente le informazioni, quindi fare clic su "Crea transazione >>".



![Image](assets/fr/50.webp)



Controllare un'ultima volta i dettagli della transazione per verificarne l'accuratezza, quindi fare clic su "Finalizza transazione per la firma".



![Image](assets/fr/51.webp)



La transazione è pronta, ma non è ancora stata firmata. Per visualizzare il [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) come codice QR, fare clic su `Mostra QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Firma della transazione con Satochip



Accendere SeedSigner e inserire Satochip come di consueto. Dalla schermata iniziale, selezionare "Scansione", quindi eseguire la scansione del codice QR visualizzato sul Sparrow.



![Image](assets/fr/53.webp)



Selezionare l'opzione "Usa scheda Satochip".



![Image](assets/fr/54.webp)



Inserire il codice PIN per sbloccare la smartcard.



![Image](assets/fr/55.webp)



SeedSigner rileva che si tratta di un PSBT e visualizza un riepilogo della transazione:




   - L'importo inviato,
   - Indirizzi di destinazione,
   - Costi di transazione associati.



Cliccate su "Rivedi i dettagli" e controllate tutte le informazioni direttamente sulla schermata di SeedSigner. I punti più importanti da controllare sono gli importi inviati, gli indirizzi di destinazione e le spese di transazione.



![Image](assets/fr/56.webp)



Se tutto è in ordine, selezionare `Approva PSBT` per firmare la transazione utilizzando lo Satochip.



![Image](assets/fr/57.webp)



Una volta completata la firma, SeedSigner genera un nuovo codice QR contenente la transazione firmata, pronto per essere scansionato da Sparrow.



#### 7.2.3 Trasmissione della transazione dal Sparrow



Ora che la transazione è firmata e convalidata, non resta che trasmetterla sulla rete Bitcoin in modo che un minatore possa includerla in un blocco. In Sparrow, fare clic su "Scansione QR".



![Image](assets/fr/58.webp)



Presentare il codice QR visualizzato sul SeedSigner (quello contenente la transazione firmata) alla webcam. Il Sparrow visualizzerà tutti i dettagli della transazione. Controllare che tutte le informazioni siano corrette, quindi fare clic su "Trasmetti transazione" per trasmetterla sulla rete Bitcoin.



![Image](assets/fr/59.webp)



La transazione viene ora trasmessa alla rete. È possibile seguirne la conferma nella scheda `Transazioni` di Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Recuperate il vostro wallet



Come abbiamo visto nelle sezioni precedenti, a seconda della strategia di sicurezza, esistono diversi modi per eseguire il backup della frase di ripristino oltre che di Satochip :




- Utilizzo di un classico *SeedQR* con il SeedSigner ;
- Registrando la frase mnemonica su un supporto fisico;
- Oppure memorizzandola su un Seedkeeper, come spiegato nella sezione 5.2.



In ogni caso, ci sono due situazioni principali in cui è necessario intervenire: la perdita dello Satochip o la perdita del SeedSigner. Vediamo come reagire in ciascuno di questi scenari.



### 8.1. Recuperare il wallet con Satochip



Se avete ancora il vostro Satochip ma il vostro SeedSigner è rotto o perso, la situazione è abbastanza semplice da gestire, poiché il vostro wallet è ancora nel Satochip.



L'opzione migliore è raccomandare i componenti necessari e ricostruire un nuovo SeedSigner da zero. Trattandosi di un dispositivo "stateless", non importa se si utilizza lo stesso SeedSigner o un altro: finché si riesce a inserire il Satochip, tutto funzionerà normalmente.



Se non volete ricostruirne uno, potete anche utilizzare il vostro Satochip nel modo classico, cioè direttamente dal vostro computer, senza passare per il SeedSigner. Questo metodo funziona perfettamente, ma riduce notevolmente la sicurezza del vostro Bitcoin wallet: perdete l'isolamento "*air-gapped*" e dovete firmare alla cieca, poiché il SeedSigner fungeva da schermo affidabile. Tuttavia, questa può essere una soluzione temporanea in caso di emergenza o se non si è in grado di ricostruire un SeedSigner.



A tale scopo, è necessario un lettore di smart card o NFC USB. Aprite il wallet che volete ripristinare nel Sparrow, quindi andate alla scheda "Impostazioni" e fate clic su "Sostituisci".



![Image](assets/fr/61.webp)



Inserire il Satochip nel lettore di smart card collegato al computer, quindi fare clic su "Importa" accanto a "Satochip".



![Image](assets/fr/62.webp)



Infine, inserire il PIN della smartcard per sbloccarla. A questo punto potrete accedere al vostro wallet, creare transazioni e firmarle direttamente con lo Satochip collegato.



### 8.2. Recuperare il portafoglio con SeedSigner



L'altro scenario, più delicato, si verifica quando si perde l'accesso al proprio Satochip contenente il seed: che sia rotto, perso, rubato o che si sia dimenticato il codice PIN. Se il vostro Satochip è stato rubato o smarrito, vi consigliamo vivamente, una volta ripristinato l'accesso ai vostri fondi, di trasferire immediatamente i vostri bitcoin su un wallet nuovo di zecca, generato con un seed diverso. In questo modo si garantisce che un potenziale aggressore non possa mai avere accesso ai vostri satss.



Per riottenere l'accesso al portafoglio e spostare i fondi, è sufficiente caricare il seed in SeedSigner. A seconda del supporto di backup utilizzato, sono disponibili diverse opzioni:





- Inserire manualmente la frase mnemonica nel menu `Seeds > Enter 12-word seed`.



![Image](assets/fr/63.webp)





- Eseguite la scansione del vostro *SeedQR* facendo clic sul pulsante "Scansione" nella pagina iniziale.



![Image](assets/fr/64.webp)





- Oppure caricare il seed da un Seedkeeper, tramite il menu `Seeds > From SeedKeeper` (questo è il metodo che sto usando in questa guida). È sufficiente inserire il PIN del Seedkeeper e selezionare il segreto da utilizzare come seed sul SeedSigner.



![Image](assets/fr/65.webp)



Una volta caricato il seed nel SeedSigner, qualunque sia il metodo utilizzato, sarà possibile firmare una o più transazioni di scansione per spostare i bitcoin su un nuovo wallet non compromesso. Per sapere come fare, consultare la parte 7.2 del seguente tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Ora sapete come utilizzare Satochip per gestire in modo sicuro il vostro portafoglio Bitcoin in combinazione con SeedSigner.



Se questa impostazione vi ha convinto, non esitate a sostenere i progetti che la rendono possibile:




- Acquistando direttamente l'apparecchiatura [sul sito web di Satochip](https://satochip.io/shop/);
- Facendo [una donazione al progetto SeedSigner](https://seedsigner.com/donate/);
- Iscrivendosi al canale YouTube di [Crypto Guide] (https://www.youtube.com/@CryptoGuide/), gestito dalla persona che gestisce il repository GitHub che ospita il firmware modificato utilizzato in questa esercitazione.
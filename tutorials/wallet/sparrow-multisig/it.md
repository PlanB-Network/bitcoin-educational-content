---
Name: Sparrow - Multisig
Description: Creare un wallet multi-firma su Sparrow
---
![cover](assets/cover.webp)



Un wallet multi-firma (spesso chiamato "*Multisig*") è un contratto Bitcoin che richiede più firme crittografiche, da chiavi diverse, per autorizzare una spesa. A differenza di un wallet convenzionale ("*singlesig*"), dove una singola chiave privata è sufficiente per sbloccare un UTXO, il Multisig si basa su un modello **m-di-n**: delle _n_ chiavi associate al wallet, _m_ devono imperativamente co-firmare ogni transazione.



Questo meccanismo consente di condividere il controllo di un wallet tra più entità o dispositivi. Ad esempio, in una configurazione 2 su 3, vengono generate tre serie di chiavi indipendenti, ma solo due sono necessarie per sbloccare i fondi. Questa architettura riduce drasticamente i rischi associati alla compromissione o alla perdita di una chiave: un ladro che ha accesso a una sola chiave non può svuotare il wallet, e un utente che ne perde una può comunque accedere ai suoi fondi con le altre due.



![Image](assets/fr/01.webp)



Tuttavia, questa maggiore sicurezza comporta una maggiore complessità. La configurazione di un Multisig wallet richiede la protezione di diverse frasi Mnemonic (una per fattore di firma) e di chiavi pubbliche estese ("*xpub*"). Infatti, se si utilizza un wallet Multisig 2-di-3, per recuperare il wallet è necessario disporre di tutte e tre le frasi Mnemonic o di almeno due delle tre frasi. Ma se si dispone solo di due delle tre frasi, è necessario accedere anche alle tre *xpub*, senza le quali sarà impossibile recuperare le chiavi pubbliche necessarie per accedere ai bitcoin che proteggono.



In sintesi, per recuperare un wallet Multisig, è necessario :




- Accedere a tutte le frasi Mnemonic associate a ciascun fattore di firma;
- Oppure avere il numero minimo di frasi Mnemonic richiesto dalla soglia per poter firmare, e anche avere accesso alle xpub di tutti gli intestatari del wallet per recuperare le chiavi pubbliche necessarie.



![Image](assets/fr/02.webp)



La gestione dei backup del wallet Multisig è facilitata da *[Output Script Descriptors](https://planb.network/resources/glossary/output-script-descriptors)*, che raggruppano tutti i dati pubblici necessari per accedere ai fondi. Tuttavia, questa funzionalità non è ancora implementata in tutti i software di gestione del wallet.



Un wallet Multisig è particolarmente adatto ai bitcoiners che cercano una maggiore sicurezza o una gestione collettiva dei fondi: aziende, associazioni, famiglie o singoli utenti che detengono una quantità significativa di bitcoin. Può essere utilizzato per creare schemi di governance decentralizzati, ad esempio per distribuire l'autorità di firma tra diversi manager o membri del team.



In questa esercitazione imparerai a creare e utilizzare un classico wallet a più firme con **Sparrow**. Se desideri creare un wallet multi-firma personalizzato con [timelocks](https://planb.network/resources/glossary/timelock), ti consiglio di utilizzare Liana:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prerequisiti



In questa esercitazione ti mostrerò come creare un Multisig con [Sparrow](https://sparrowwallet.com/download/). Se non hai ancora installato questo software, fallo subito. Se hai bisogno di aiuto, abbiamo anche un tutorial dettagliato sulla configurazione di Sparrow:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Per configurare un wallet multi-firma, sono necessari diversi hardware wallet. Per un Multisig 2-di-3, ad esempio, si possono utilizzare:




- Un Trezor modello 1;
- Un Ledger Flex;
- Un Coldcard MK3.



![Image](assets/fr/03.webp)



È una buona idea utilizzare diverse marche di Hardware Wallet nella configurazione Multisig. In questo modo si garantisce che se un modello specifico presenta un problema grave, questo non influisce sulla sicurezza complessiva del Multisig. Inoltre, ciò consente di beneficiare dei vantaggi specifici di ciascun dispositivo. Ad esempio, nella mia configurazione:





- Trezor Model One è completamente open-source, il che rende possibile la verifica della generazione seed. Tuttavia, non essendo dotato di un Secure Element (chip fatto apposta per resistere ad attacchi fisici e informatici), rimane vulnerabile agli attacchi fisici;





- Ledger Flex, invece, beneficia di un firmware proprietario non verificabile, ma incorpora un Secure Element che offre un'eccellente protezione fisica;





- Coldcard è dotato di un Secure Element e il suo codice è rintracciabile. È una scelta interessante per la nostra configurazione, in quanto offre funzioni di verifica non disponibili su altri modelli.



Prima di configurare il Multisig Wallet, assicurati che ogni Hardware Wallet sia configurato correttamente (generazione e salvataggio delle frasi Mnemonic, definizione del PIN). Per istruzioni dettagliate, puoi consultare i nostri tutorial per ogni Hardware Wallet, ad esempio :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Come vedrai più avanti in questo tutorial, è anche possibile integrare nella configurazione del Multisig un fattore che non è associato a un Hardware Wallet, ma le cui chiavi private sono memorizzate sul tuo PC. Questo metodo è ovviamente meno sicuro dell'uso esclusivo con Hardware Wallet, ma può essere rilevante in alcuni casi. Ad esempio, per un Multisig 2-di-3, si potrebbe optare per due Hardware Wallet e un Software Wallet.



## Creare un portafoglio Multisig



Apri Sparrow, fai clic sulla scheda "*File*", quindi seleziona "*New Wallet*".



![Image](assets/fr/04.webp)



Assegna un nome al wallet multisig, quindi clicca su "*Create Wallet*" per confermare.



![Image](assets/fr/05.webp)



Nel menu a discesa "*Policy Type*", seleziona l'opzione "*Multi Signature*".



![Image](assets/fr/06.webp)



Nell'angolo in alto a destra è possibile definire il numero totale di chiavi nel Multisig e il numero di cofirmatari necessari per autorizzare una transazione. Nel mio esempio, si tratta di uno schema 2 di 3.



![Image](assets/fr/07.webp)



Nella parte inferiore della finestra, Sparrow visualizza tre "*Keystore*". Ognuno di essi rappresenta un set di chiavi. Qui sto usando tre Hardware Wallet, quindi ogni "*Keystore*" corrisponde a uno di essi. Ora li configureremo.



Inizio con la Coldcard. Nella scheda "*Keystore 1*", scelgo l'opzione "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Sul Coldcard, una volta sbloccato il dispositivo, vado al menu "*Settings*", quindi a "*Multisig Wallets*".



![Image](assets/fr/09.webp)



Questo menù consente di gestire i Multisig Wallet in cui partecipa Coldcard. Se voglio crearne uno nuovo, seleziono "*Esport XPUB*".



![Image](assets/fr/10.webp)



Per il campo "*Account Number*", se si gestisce un solo conto, è possibile lasciarlo vuoto e convalidare direttamente premendo il pulsante di conferma.



![Image](assets/fr/11.webp)



La scheda Coldcard ti mostra quindi un file contenente la tua xpub appena generata, salvata sulla scheda Micro SD.



![Image](assets/fr/12.webp)



Inserisci la Micro SD nel computer. Su Sparrow, fai clic sul pulsante "*Import file...*" accanto a "*Coldcard Multisig*", quindi seleziona il file creato dal Coldcard sulla scheda.



![Image](assets/fr/13.webp)



Il tuo xpub è stato importato con successo. Ora ripeti la procedura con gli altri due Hardware Wallet.



![Image](assets/fr/14.webp)



Per il Ledger Flex, seleziona "*Keystore 2*", quindi fai clic su "*Connected Hardware Wallet*". Assicurati che il Ledger sia collegato al computer, sbloccato e che l'applicazione Bitcoin sia aperta.



![Image](assets/fr/15.webp)



Quindi fai clic sul pulsante "*Scan...*".



![Image](assets/fr/16.webp)



Accanto al nome dell'Hardware Wallet, fai clic su "*Import Keystore*".



![Image](assets/fr/17.webp)



Il secondo firmatario è ora correttamente registrato su Sparrow.



![Image](assets/fr/18.webp)



Ripeti esattamente la stessa procedura con il Trezor One per finalizzare la configurazione del Multisig.



![Image](assets/fr/19.webp)



Nella mia configurazione non è contemplato questo caso, ma se desideri includere una firma tramite un Software Wallet in Sparrow (Hot Wallet) all'interno del proprio Multisig, è sufficiente fare clic sul pulsante "*New or Imported Software Wallet*".



Ora che tutti i dispositivi di firma sono stati importati su Sparrow, è possibile finalizzare la creazione di Multisig facendo clic su "*Apply*".



![Image](assets/fr/20.webp)



Scegli una password forte per proteggere l'accesso al proprio Sparrow. Questa password protegge le chiavi pubbliche, gli indirizzi, le etichette e la cronologia delle transazioni da accessi non autorizzati.



Ricorda di salvare la password in un luogo sicuro, ad esempio in un gestore di password, per evitare di perderla.



![Image](assets/fr/21.webp)



## Backup di un Multisig Wallet



Ora salva il tuo *Output Script Descriptors* sul Coldcard (questo vale solo per gli utenti che hanno un Coldcard nel loro Multisig) e, soprattutto, tieni una copia di backup su un supporto indipendente.



Il *Descriptor* contiene tutte le xpub del Multisig Wallet, nonché i percorsi di derivazione utilizzati per generate le chiavi. Ricorda quanto visto nella Parte 1: per ripristinare un Multisig Wallet, è necessario avere **tutte** le frasi Mnemonic, oppure solo il numero minimo richiesto per raggiungere la soglia di firma. Tuttavia, in quest'ultimo caso, è essenziale avere anche **gli xpub** dei firmatari mancanti. Il *Descriptor* contiene tutte le xpub del Multisig.



Se non è chiaro, ricorda solo questo: per recuperare un Multisig, è necessario il numero minimo di frasi Mnemonic per ogni Hardware Wallet utilizzato, a seconda della soglia (nel mio caso: 2 frasi), oltre al *Descriptor*.



Questo *Descriptor* non contiene chiavi private, ma solo chiavi pubbliche. Ciò significa che non dà accesso ai fondi. Non è quindi critico come le frasi Mnemonic, che danno pieno accesso ai bitcoin. Il rischio del *Descriptor* è legato esclusivamente alla riservatezza: in caso di compromissione, una terza parte potrebbe osservare tutte le tue transazioni, ma non potrebbe spendere i tuoi fondi.



Consiglio vivamente di creare diverse copie di questo *Descriptor* e di conservarle con ciascun dispositivo di firma del Multisig. Ad esempio, nel mio caso, stampo il *Descriptor* su carta e ne conservo una copia nello stesso luogo dove riponi il Coldcard, un'altra insieme al Trezor e una insieme al Ledger. Inoltre, salvo questo *Descriptor* in formato PDF su tre chiavette USB, ognuna delle quali viene conservata con uno degli Hardware Wallet. In questo modo, massimizzo le possibilità di non perdere mai questo *Descrittore* e sono sicuro di avere due copie (una fisica e una digitale) con ogni dispositivo.



Una volta creato il Multisig Wallet, Sparrow fornisce automaticamente questo *Descriptor*. Fai clic sul pulsante "*SavePDF...*" per salvarlo sia come testo che come codice QR.



![Image](assets/fr/22.webp)



È quindi possibile stampare il PDF e copiarlo sulle chiavette USB.



![Image](assets/fr/23.webp)



Registreremo anche questo *Descrittore* sul Coldcard (se ne usate uno nella vostra configurazione). Ciò consentirà al Coldcard di verificare che ogni transazione firmata in seguito corrisponda al Wallet originale: xpub corretto, formato Address corretto, percorso di derivazione corretto... Senza questo *Descrittore* importato, Coldcard non può confermare che gli indirizzi Exchange non siano stati dirottati o che il PSBT non sia stato manomesso.



Questo è ciò che rende Coldcard così interessante in un Multisig: offre controlli aggiuntivi contro alcuni attacchi sofisticati, che altri Hardware Wallet non consentono (a condizione, ovviamente, che lo si usi per firmare).



In Sparrow, accedere al menu "*Settings*", quindi fare clic su "*Export...*".



![Image](assets/fr/24.webp)



Accanto all'opzione "*Coldcard Multisig*", fare clic su "*Export file...*" e salvare il file di testo sulla scheda Micro SD.



![Image](assets/fr/25.webp)



Inserire quindi la scheda nel Coldcard. Andare al menu "*Settings*", quindi "*Multisig Wallet*" e selezionare "*Import from SD*".



![Image](assets/fr/26.webp)



Selezionare il file appropriato e confermare l'importazione.



![Image](assets/fr/27.webp)



Fare clic sul nome del nuovo Multisig importato.



![Image](assets/fr/28.webp)



Controllare i parametri di configurazione del Multisig, quindi confermare la registrazione.



![Image](assets/fr/29.webp)



Il Multisig è ora correttamente salvato sul Coldcard. Se si dispone di più Coldcard nello stesso Multisig, ripetere questa procedura per ciascuna di esse.



Oltre a salvare il *Descrittore*, non dimenticate di prestare particolare attenzione al salvataggio delle frasi Mnemonic per ciascuno dei vostri dispositivi di firma. Se siete alle prime armi, vi consiglio di consultare quest'altra guida per imparare a salvarle e gestirle correttamente:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Prima di ricevere i primi Bitcoin sul Multisig, **vi consiglio vivamente di eseguire un test di ripristino a vuoto**. Annotare alcune informazioni di riferimento, come la prima ricezione dell'Address, quindi ripristinare gli Hardware Wallet mentre il Wallet è ancora vuoto. Successivamente, provare a ripristinare il Multisig Wallet sui portafogli Hardware utilizzando i backup cartacei della frase Mnemonic, mentre su Sparrow utilizzando il *Descrittore*. Verificare che il primo Address generato dopo il ripristino corrisponda a quello scritto originariamente. Se così fosse, si può essere certi che i backup cartacei sono affidabili.



Per saperne di più su come eseguire un test di ripristino, vi suggerisco di consultare quest'altra guida:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Ricevere Bitcoin sul vostro Multisig



Il vostro Wallet è ora pronto a ricevere Bitcoin. In Sparrow, fare clic sulla scheda "*Receive*".



![Image](assets/fr/30.webp)



Prima di utilizzare l'Address generato da Sparrow Wallet, prendetevi il tempo di verificarlo direttamente sullo schermo dei vostri Hardware Wallet. In questo modo vi assicurerete che l'Address non sia stato alterato e che i vostri dispositivi possiedano le chiavi private necessarie per spendere i fondi associati. Questo aiuta a proteggersi da una serie di vettori di attacco.



A tal fine, fare clic su "*Display Address*" per visualizzare l'Address sul Trezor o sul Ledger, se collegato via cavo.



![Image](assets/fr/31.webp)



Con Coldcard, questa verifica può essere effettuata senza alcuna interazione con Sparrow. È sufficiente aprire il menu "*Address Explorer*" e selezionare il proprio Multisig in basso.



![Image](assets/fr/32.webp)



Si vedranno quindi gli indirizzi di ricezione generati dal Multisig.



![Image](assets/fr/33.webp)



Verificare che l'Address visualizzato su ogni Hardware Wallet corrisponda esattamente a quello del Wallet di Sparrow. È consigliabile eseguire questa operazione appena prima di condividere l'Address con il pagatore, per essere sicuri della sua integrità.



È quindi possibile assegnare un "Label" (etichetta) a questo Address, per indicare l'origine dei Bitcoin ricevuti. Questo è un buon modo per organizzare la gestione dei vostri UTXO.



![Image](assets/fr/34.webp)



Una volta verificato, è possibile utilizzare l'Address per ricevere Bitcoin.



![Image](assets/fr/35.webp)



## Inviare Bitcoin con il vostro Multisig



Ora che avete ricevuto i primi Sats sul vostro Multisig Wallet, potete anche spenderli! In Sparrow, vai alla scheda "*Send*" per creare una nuova transazione.



![Image](assets/fr/36.webp)



Se si desidera utilizzare il *Coin Control*, ossia la selezione manualmente gli UTXO da spendere, andare alla scheda "*UTXO*". Scegliete gli UTXO che desiderate spendere, quindi cliccate su "*Send Selected*". Si verrà automaticamente reindirizzati alla scheda "*Send*", con gli UTXO già precompilati.



![Image](assets/fr/37.webp)



Inserire la destinazione dell'Address. È possibile aggiungere più indirizzi facendo clic su "*+ Aggiungi*".



![Image](assets/fr/38.webp)



Aggiungere una "*Label*" (Etichetta) per descrivere lo scopo di questa spesa, così da facilitare la tracciabilità delle transazioni.



![Image](assets/fr/39.webp)



Inserire l'importo da inviare all'Address selezionato.



![Image](assets/fr/40.webp)



Regolare la quantità di fees in base alle condizioni attuali della rete. Ad esempio, consultare [Mempool.space](https://Mempool.space/) per selezionare una fee adeguata.



Dopo aver controllato tutti i parametri della transazione, fare clic su "*Create Transaction*".



![Image](assets/fr/41.webp)



Se siete soddisfatti di tutto, fate clic su "*Finalize Transaction for Signing*".



![Image](assets/fr/42.webp)



Nella parte inferiore dello schermo, vedrete che Sparrow è in attesa di 2 firme. Questo è normale: il Wallet usato qui è un Multisig 2-di-3.



![Image](assets/fr/43.webp)



Inizio a firmare con il mio Coldcard. A tal fine, inserisco una scheda Micro SD nel computer, quindi faccio clic su "*Save Transaction*".



![Image](assets/fr/44.webp)



Esistono 3 modi per trasmettere la transazione dal firmare all'Hardware Wallet e poi recuperarla da Sparrow. Il primo è utilizzare una scheda Micro SD, come faremo qui per Coldcard. Il secondo è tramite una connessione via cavo, che utilizzeremo per la seconda firma (Ledger e Trezor). Infine, è possibile utilizzare la comunicazione tramite codice QR, per i dispositivi dotati di fotocamera come Coldcard Q, Jade Plus o Passport V2.



Una volta salvato il PSBT (*Partially Signed Bitcoin Transaction*) sulla Micro SD, lo inserisco nel Coldcard MK3, quindi seleziono il menu "*Ready To Sign*".



![Image](assets/fr/45.webp)



Sullo schermo dell'Hardware Wallet, controllare attentamente i parametri della transazione: l'Address del destinatario, l'importo inviato e le spese. Una volta confermata la transazione, convalidare per procedere alla firma.



![Image](assets/fr/46.webp)



Riportare quindi la Micro SD sul computer e fare clic su "*Load Transaction*" su Sparrow. Selezionate il PSBT firmato su Coldcard dai vostri file.



![Image](assets/fr/47.webp)



Si può notare che la firma Coldcard è stata aggiunta. Ora utilizzerò un secondo dispositivo, in questo caso il Ledger, per eseguire la seconda firma richiesta. Lo collego, lo sblocco e poi faccio clic su "*Sign*" su Sparrow.



![Image](assets/fr/48.webp)



Fare clic su "*Sign*" accanto al nome del proprio Hardware Wallet.



![Image](assets/fr/49.webp)



La prima volta che si utilizza Ledger con questo Multisig, Sparrow chiederà di verificare le chiavi pubbliche estese (xpub) dei cofirmatari. Come nel caso di Coldcard, questo passaggio impedisce di firmare alla cieca in seguito. Per convalidare queste informazioni, confrontare le xpub visualizzate sullo schermo del Ledger con quelle fornite direttamente dagli altri Hardware Wallet.



![Image](assets/fr/50.webp)



Controllare l'Address del destinatario, l'importo trasferito e la tariffa della transazione, quindi firmare la transazione.



![Image](assets/fr/51.webp)



Toccare sullo schermo per firmare.



![Image](assets/fr/52.webp)



Sparrow dispone ora delle due firme necessarie per rilasciare i fondi dal portafoglio Multisig. Controllate la transazione un'ultima volta e, se tutto va bene, fate clic su "*Broadcast Transaction*" per trasmetterla in rete.



![Image](assets/fr/53.webp)



Questa transazione si trova nella scheda "*Transactions*" di Sparrow Wallet.



![Image](assets/fr/54.webp)



Congratulazioni, ora sapete come impostare e utilizzare un Wallet a firma multipla su Sparrow. Se avete trovato utile questa guida, vi sarei grato se lasciaste un pollice verde qui sotto. Non esitate a condividere questo articolo sui vostri social network. Grazie per la condivisione!



Per andare oltre, vi consiglio di consultare questo tutorial su un altro metodo per aumentare la sicurezza del vostro Bitcoin Wallet, il passphrase BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

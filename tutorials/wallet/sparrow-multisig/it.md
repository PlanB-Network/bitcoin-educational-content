---
name: Sparrow - multisig
description: Creare un wallet multi-firma su Sparrow
---
![cover](assets/cover.webp)



Un wallet multi-firma (spesso chiamato "*multisig*") è un contratto Bitcoin che richiede più firme crittografiche, da chiavi diverse, per autorizzare una spesa. A differenza di un wallet convenzionale ("*singlesig*"), dove una singola chiave privata è sufficiente per sbloccare un [UTXO](https://planb.network/resources/glossary/utxo), il multisig si basa su un modello **m-di-n**: delle _n_ chiavi associate al wallet, _m_ devono imperativamente co-firmare ogni transazione.



Questo meccanismo consente di suddividere il controllo di un wallet tra più entità o dispositivi. Ad esempio, in una configurazione 2 su 3, vengono generate tre serie di chiavi indipendenti, ma solo due sono necessarie per sbloccare i fondi. Questa architettura riduce drasticamente i rischi associati alla compromissione o alla perdita di una chiave: un ladro che ha accesso a una sola chiave non può svuotare il wallet, e un utente che ne perde una può comunque accedere ai suoi fondi con le altre due.



![Image](assets/fr/01.webp)



Tuttavia, questa maggiore sicurezza comporta una maggiore complessità. La configurazione di un multisig wallet richiede la protezione di diverse frasi mnemoniche (una per fattore di firma) e di chiavi pubbliche estese ("*xpub*"). Infatti, se si utilizza un wallet multisig 2-di-3, per recuperare il wallet è necessario disporre di tutte e tre le frasi mnemoniche o di almeno due delle tre frasi. Ma se si dispone solo di due delle tre frasi, è necessario accedere anche alle tre *xpub*, senza le quali sarà impossibile recuperare le chiavi pubbliche necessarie per accedere ai bitcoin che proteggono.



In sintesi, per recuperare un wallet multisig, è necessario:




- Accedere a tutte le frasi mnemoniche associate a ciascun fattore di firma;
- Oppure avere il numero minimo di frasi mnemoniche richiesto dalla soglia per poter firmare, e anche avere accesso alle xpub di tutti gli intestatari del wallet per recuperare le chiavi pubbliche necessarie.



![Image](assets/fr/02.webp)



La gestione dei backup del wallet multisig è facilitata dagli *[Output Script Descriptors](https://planb.network/resources/glossary/output-script-descriptors)*, che raggruppano tutti i dati pubblici necessari per accedere ai fondi. Tuttavia, questa funzionalità non è ancora implementata in tutti i software di gestione del wallet.



Un wallet multisig è particolarmente adatto ai bitcoiners che cercano una maggiore sicurezza o una gestione collettiva dei fondi: aziende, associazioni, famiglie o singoli utenti che detengono una quantità significativa di bitcoin. Può essere utilizzato per creare schemi di governance decentralizzati, ad esempio per distribuire l'autorità di firma tra diversi manager o membri del team.



In questa esercitazione imparerai a creare e utilizzare un classico wallet a più firme con **Sparrow**. Se desideri creare un wallet multi-firma personalizzato con [timelocks](https://planb.network/resources/glossary/timelock), ti consiglio di utilizzare Liana:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prerequisiti



In questa esercitazione ti mostrerò come creare un multisig con [Sparrow](https://sparrowwallet.com/download/). Se non l'hai ancora installato e ti serve aiuto, abbiamo anche un tutorial dettagliato sulla configurazione di Sparrow:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Per configurare un wallet multi-firma, sono necessari diversi hardware wallet. Per un multisig 2-di-3, ad esempio, si possono utilizzare:




- Un Trezor modello 1;
- Un Ledger Flex;
- Un Coldcard MK3.



![Image](assets/fr/03.webp)



È una buona idea utilizzare diverse marche di Hardware wallet nella configurazione multisig. In questo modo hai la garanzia che se un modello specifico presenta un problema grave, questo non influisce sulla sicurezza complessiva del multisig. Inoltre, ciò ti consente di beneficiare dei vantaggi specifici di ciascun dispositivo. Ad esempio, nella mia configurazione:





- Trezor Model One è completamente open-source, il che rende possibile la verifica della generazione seed. Tuttavia, non essendo dotato di un Secure Element (chip fatto apposta per resistere ad attacchi fisici e informatici), rimane vulnerabile agli attacchi fisici;





- Ledger Flex, invece, beneficia di un firmware proprietario non verificabile, ma incorpora un Secure Element che offre un'eccellente protezione fisica;





- Coldcard è dotato di un Secure Element e il suo codice è rintracciabile. È una scelta interessante per la nostra configurazione, in quanto offre funzioni di verifica non disponibili su altri modelli.



Prima di configurare il multisig wallet, assicurati che ogni Hardware wallet sia configurato correttamente (generazione e salvataggio delle frasi mnemonichehe, definizione del PIN). Per istruzioni dettagliate, puoi consultare i nostri tutorial per ogni Hardware wallet, ad esempio:



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Come vedrai più avanti in questo tutorial, è anche possibile integrare nella configurazione del multisig un fattore che non è associato a un Hardware wallet, ma le cui chiavi private sono memorizzate sul tuo PC. Questo metodo è ovviamente meno sicuro dell'uso esclusivo con Hardware wallet, ma può essere rilevante in alcuni casi. Ad esempio, per un multisig 2-di-3, si potrebbe optare per due Hardware wallet e un Software wallet.



## Creare un portafoglio multisig



Apri Sparrow, fai clic sulla scheda "*File*", quindi seleziona "*New wallet*".



![Image](assets/fr/04.webp)



Assegna un nome al wallet multisig, quindi clicca su "*Create wallet*" per confermare.



![Image](assets/fr/05.webp)



Nel menu a discesa "*Policy Type*", seleziona l'opzione "*Multi Signature*".



![Image](assets/fr/06.webp)



Nell'angolo in alto a destra puoi definire il numero totale di chiavi nel multisig e il numero di cofirmatari necessari per autorizzare una transazione. Nel mio esempio, si tratta di uno schema 2 di 3.



![Image](assets/fr/07.webp)



Nella parte inferiore della finestra, Sparrow visualizza tre "*Keystore*". Ognuno di essi rappresenta un set di chiavi. Qui sto usando tre Hardware wallet, quindi ogni "*Keystore*" corrisponde a uno di essi. Ora li configureremo.



Inizio con il Coldcard. Nella scheda "*Keystore 1*", scelgo l'opzione "*Airgapped Hardware wallet*".



![Image](assets/fr/08.webp)



Sul Coldcard, una volta sbloccato il dispositivo, vado al menu "*Settings*", quindi a "*multisig wallets*".



![Image](assets/fr/09.webp)



Questo menù consente di gestire i multisig wallet in cui partecipa Coldcard. Se voglio crearne uno nuovo, seleziono "*Esport XPUB*".



![Image](assets/fr/10.webp)



Per il campo "*Account Number*", se si gestisce un solo conto, è possibile lasciarlo vuoto e convalidare direttamente premendo il pulsante di conferma.



![Image](assets/fr/11.webp)



La scheda Coldcard ti mostra quindi un file contenente la tua xpub appena generata, salvata sulla scheda Micro SD.



![Image](assets/fr/12.webp)



Inserisci la Micro SD nel computer. Su Sparrow, fai clic sul pulsante "*Import file...*" accanto a "*Coldcard multisig*", quindi seleziona il file creato dal Coldcard sulla scheda.



![Image](assets/fr/13.webp)



Il tuo xpub è stato importato con successo. Ora ripeti la procedura con gli altri due Hardware wallet.



![Image](assets/fr/14.webp)



Per il Ledger Flex, seleziona "*Keystore 2*", quindi fai clic su "*Connected Hardware wallet*". Assicurati che il Ledger sia collegato al computer, che sia sbloccato, e che l'applicazione Bitcoin sia aperta.



![Image](assets/fr/15.webp)



Quindi fai clic sul pulsante "*Scan...*".



![Image](assets/fr/16.webp)



Accanto al nome dell'Hardware wallet, fai clic su "*Import Keystore*".



![Image](assets/fr/17.webp)



Il secondo firmatario è ora correttamente registrato su Sparrow.



![Image](assets/fr/18.webp)



Ripeti esattamente la stessa procedura con il Trezor One per finalizzare la configurazione del multisig.



![Image](assets/fr/19.webp)



Nella mia configurazione non è contemplato questo caso, ma se desideri includere una firma tramite un Software wallet in Sparrow (Hot wallet) all'interno del proprio multisig, è sufficiente fare clic sul pulsante "*New or Imported Software wallet*".



Ora che tutti i dispositivi di firma sono stati importati su Sparrow, è possibile finalizzare la creazione di multisig facendo clic su "*Apply*".



![Image](assets/fr/20.webp)



Scegli una password forte per proteggere l'accesso al proprio Sparrow. Questa password protegge le chiavi pubbliche, gli indirizzi, le etichette e la cronologia delle transazioni da accessi non autorizzati.



Ricorda di salvare la password in un luogo sicuro, ad esempio in un gestore di password, per evitare di perderla.



![Image](assets/fr/21.webp)



## Backup di un multisig wallet



Ora salva il tuo *Output Script Descriptors* sul Coldcard (questo vale solo per gli utenti che hanno un Coldcard nel loro multisig) e, soprattutto, tieni una copia di backup su un supporto indipendente.



Il *Descriptor* contiene tutte le xpub del multisig wallet, nonché i percorsi di derivazione utilizzati per generate le chiavi. Ricorda quanto visto nella Parte 1: per ripristinare un multisig wallet, è necessario avere **tutte** le frasi mnemoniche, oppure solo il numero minimo richiesto per raggiungere la soglia di firma. Tuttavia, in quest'ultimo caso, è essenziale avere anche **le xpub** dei firmatari mancanti. Il *Descriptor* contiene tutte le xpub del multisig.



Se non è chiaro, ricorda solo questo: per recuperare un multisig, è necessario il numero minimo di frasi mnemoniche per ogni Hardware wallet utilizzato, a seconda della soglia (nel mio caso: 2 frasi), oltre al *Descriptor*.



Questo *Descriptor* non contiene chiavi private, ma solo chiavi pubbliche. Ciò significa che non dà accesso ai fondi. Non è quindi critico come le frasi mnemoniche, che danno pieno accesso ai bitcoin. Il rischio del *Descriptor* è legato esclusivamente alla riservatezza: in caso di compromissione, una terza parte potrebbe osservare tutte le tue transazioni, ma non potrebbe spendere i tuoi fondi.



Ti consiglio vivamente di creare diverse copie di questo *Descriptor* e di conservarle con ciascun dispositivo di firma del multisig. Ad esempio, nel mio caso, stampo il *Descriptor* su carta e ne conservo una copia nello stesso luogo dove ripongo il Coldcard, un'altra insieme al Trezor e una insieme al Ledger. Inoltre, salvo questo *Descriptor* in formato PDF su tre chiavette USB, ognuna delle quali viene conservata con uno degli Hardware wallet. In questo modo, massimizzo le possibilità di non perdere mai questo *Descriptor* e sono sicuro di avere due copie (una fisica e una digitale) con ogni dispositivo.



Una volta creato il multisig wallet, Sparrow fornisce automaticamente questo *Descriptor*. Fai clic sul pulsante "*SavePDF...*" per salvarlo sia come testo che come codice QR.



![Image](assets/fr/22.webp)



È quindi possibile stampare il PDF e copiarlo sulla tua chiavetta USB.



![Image](assets/fr/23.webp)



Registra anche questo *Descriptor* sul Coldcard (se ne usi uno nella tua configurazione). Ciò consentirà al Coldcard di verificare che ogni transazione firmata in seguito corrisponda al wallet originale: xpub corretto, formato di indirizzo corretto, percorso di derivazione corretto... Se non viene importato il *Descriptor*, Coldcard non può confermare che non sia avvenuta la manomissione degli indirizzi di cambio o della PSBT (Partially Signed Bitcoin Transaction).


Questo è ciò che rende Coldcard così interessante nella creazione di un multisig: offre controlli aggiuntivi contro alcuni attacchi sofisticati, che altri Hardware wallet non offrono (a condizione, ovviamente, che lo si usi per firmare).



In Sparrow, accedi al menu "*Settings*", quindi fai clic su "*Export...*".



![Image](assets/fr/24.webp)



Accanto all'opzione "*Coldcard multisig*", fai clic su "*Export file...*" e salva il file di testo sulla scheda Micro SD.



![Image](assets/fr/25.webp)



Inserisci quindi la scheda nel Coldcard. Vai al menu "*Settings*", quindi "*multisig wallet*" e seleziona "*Import from SD*".



![Image](assets/fr/26.webp)



Seleziona il file appropriato e conferma l'importazione.



![Image](assets/fr/27.webp)



Fai clic sul nome del nuovo multisig importato.



![Image](assets/fr/28.webp)



Controlla i parametri di configurazione del multisig, quindi conferma la registrazione.



![Image](assets/fr/29.webp)



Il multisig è ora correttamente salvato sul Coldcard. Se disponi di più Coldcard nello stesso multisig, ripeti questa procedura per ciascuna di esse.



Oltre a salvare il *Descriptor*, non dimenticare di prestare particolare attenzione al salvataggio delle frasi mnemoniche per ciascuno dei tuoi dispositivi di firma. Se sei alle prime armi, ti consiglio di consultare quest'altra guida per imparare a salvarle e gestirle correttamente:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Quando ancora non hai ricevuto fondi sul multisig, **ti consiglio vivamente di eseguire un test di ripristino con il wallet vuoto**. Annota alcune informazioni di riferimento, come il primo indirizzo di ricezione, quindi ripristina gli Hardware wallet mentre il wallet è ancora vuoto. Successivamente, prova a ripristinare il multisig sugli Hardware wallet utilizzando i backup cartacei della frasi mnemoniche, mentre su Sparrow fai la stessa cosa utilizzando il *Descriptor*. Verifica che il primo indirizzo di ricezione generato dopo il ripristino corrisponda a quello scritto originariamente. Se così fosse, puoi essere certo che i backup cartacei sono affidabili.



Per saperne di più su come eseguire un test di ripristino, ti suggerisco di consultare quest'altra guida:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Ricevere bitcoin sul tuo multisig



Il tuo wallet è ora pronto a ricevere bitcoin. In Sparrow, fai clic sulla scheda "*Receive*".



![Image](assets/fr/30.webp)



Prima di utilizzare l'indirizzo di ricezione generato da Sparrow wallet, prenditi del tempo per verificarlo direttamente sullo schermo dei tuoi Hardware wallet. Questo ti assicurerà che l'indirizzo non sia stato alterato e che i tuoi dispositivi possiedano le chiavi private necessarie per spendere i fondi associati. Questo aiuta a proteggerti da una serie di vettori di attacco.



A tal fine, fai clic su "*Display address*" per visualizzare l'indirizzo sul Trezor o sul Ledger, se collegato via cavo.



![Image](assets/fr/31.webp)



Con Coldcard, questa verifica può essere effettuata senza alcuna interazione con Sparrow. Puoi semplicemente aprire il menu "*address Explorer*" e selezionare il tuo multisig in basso.



![Image](assets/fr/32.webp)



Vedrai quindi gli indirizzi di ricezione generati dal multisig.



![Image](assets/fr/33.webp)



Verifica che l'indirizzo visualizzato su ogni Hardware wallet corrisponda esattamente a quello del wallet di Sparrow. Ti consiglio di eseguire questa operazione prima di condividere l'indirizzo con il pagatore, per essere sicuro della sua integrità.



Puoi quindi assegnare una "Etichetta"  a questo indirizzo, per indicare l'origine dei bitcoin ricevuti. Questo è un buon modo per organizzare e gestire i tuoi UTXO.



![Image](assets/fr/34.webp)



Una volta verificato, puoi utilizzare l'indirizzo per ricevere bitcoin.



![Image](assets/fr/35.webp)



## Inviare bitcoin con il tuo multisig



Ora che hai ricevuto i primi Sats sul tuo multisig wallet, puoi anche spenderli! Su Sparrow, vai alla scheda "*Send*" per creare una nuova transazione.



![Image](assets/fr/36.webp)



Se vuoi utilizzare il *Coin Control*, ossia la selezione manuale degli UTXO da spendere, vai sulla scheda "*UTXO*". Scegli gli UTXO che desideri spendere, quindi clicca su "*Send Selected*". Verrai automaticamente reindirizzato sulla scheda "*Send*", con gli UTXO già selezionati.



![Image](assets/fr/37.webp)



Inserisci l'indirizzo di destinazione. Puoi aggiungere più indirizzi facendo clic su "*+ Aggiungi*".



![Image](assets/fr/38.webp)



Aggiungi una "*Etichetta*" per descrivere lo scopo di questa transazione, così da facilitarne la tracciabilità.



![Image](assets/fr/39.webp)



Inserisci l'importo da inviare all'indirizzo selezionato.



![Image](assets/fr/40.webp)



Regola la quantità di fee in base alle condizioni attuali della rete. Ad esempio, consulta [Mempool.space](https://Mempool.space/) per selezionare una fee adeguata.



Dopo aver controllato tutti i parametri della transazione, fai clic su "*Create Transaction*".



![Image](assets/fr/41.webp)



Se sei soddisfatto di tutto, fai clic su "*Finalize Transaction for Signing*".



![Image](assets/fr/42.webp)



Nella parte inferiore dello schermo, vedrai che Sparrow è in attesa di 2 firme. Questo è normale: il wallet usato qui è un multisig 2-di-3.



![Image](assets/fr/43.webp)



Inizia a firmare con il tuo Coldcard. A tal fine, inserisci una scheda Micro SD nel computer, quindi fai clic su "*Save Transaction*".



![Image](assets/fr/44.webp)



Esistono 3 modi per trasmettere la transazione da firmare all'Hardware wallet e poi recuperarla da Sparrow. Il primo è utilizzare una scheda Micro SD, come vedrai qui con Coldcard. Il secondo è tramite una connessione via cavo, che utilizzerai per la seconda firma (Ledger e Trezor). Infine, puoi utilizzare la comunicazione tramite codice QR, per i dispositivi dotati di fotocamera come Coldcard Q, Jade Plus o Passport V2.



Una volta che hai salvato il PSBT (*Partially Signed Bitcoin Transaction*) sulla Micro SD, inseriscilo nel Coldcard MK3, quindi seleziona il menu "*Ready To Sign*".



![Image](assets/fr/45.webp)



Sullo schermo dell'Hardware wallet, controlla attentamente i parametri della transazione: l'indirizzo del destinatario, l'importo inviato e le fee. Una volta confermata la transazione, convalida per procedere alla firma.



![Image](assets/fr/46.webp)



Quindi torna al tuo computer con la Micro SD e su Sparrow clicca su "*Load Transaction*". Seleziona il PSBT firmato su Coldcard dai tuoi file.



![Image](assets/fr/47.webp)



Puoi vedere che la firma Coldcard è stata aggiunta. Devi ora usare un secondo dispositivo, in questo esempio il Ledger, per eseguire la seconda firma richiesta. Collegalo, sbloccalo e poi fai clic su "*Sign*" su Sparrow.



![Image](assets/fr/48.webp)



Fai clic su "*Sign*" accanto al nome del proprio Hardware wallet.



![Image](assets/fr/49.webp)



La prima volta che usi Ledger con questo multisig, Sparrow chiederà di verificare le chiavi pubbliche estese (xpub) dei cofirmatari. Come nel caso di Coldcard, questo passaggio impedisce di firmare alla cieca in seguito. Per convalidare queste informazioni, confronta le xpub visualizzate sullo schermo del Ledger con quelle fornite direttamente dagli altri Hardware wallet.



![Image](assets/fr/50.webp)



Controlla l'indirizzo del destinatario, l'importo trasferito e la fee della transazione, quindi firma la transazione.



![Image](assets/fr/51.webp)



Tocca sullo schermo per firmare.



![Image](assets/fr/52.webp)



Sparrow dispone ora delle due firme necessarie per rilasciare i fondi dal portafoglio multisig. Controlla la transazione un'ultima volta e, se tutto va bene, fai clic su "*Broadcast Transaction*" per trasmetterla in rete.



![Image](assets/fr/53.webp)



Questa transazione si trova nella scheda "*Transactions*" di Sparrow wallet.



![Image](assets/fr/54.webp)



Congratulazioni, ora sai come impostare e utilizzare un wallet a firma multipla su Sparrow. Se hai trovato utile questa guida, ti sarei grato se lasciassi un pollice verde qui sotto. Non esitare a condividere questo articolo sui tuoi social network. Grazie per la condivisione!



Per andare avanti, ti consiglio di consultare questo tutorial su un altro metodo per aumentare la sicurezza del tuo Bitcoin wallet tramite l'uso della passphrase BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

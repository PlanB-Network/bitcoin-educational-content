---
name: COLDCARD Q - Key Teleport
description: Cos'è il Key Teleport e come si usa?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Qual è la funzione **Key Teleport** offerta da Coinkite con il suo dispositivo di punta ColdCardQ?



**Key Teleport** consente di trasferire in modo sicuro dati riservati tra 2 ColdCardQ. Il canale di trasmissione non deve essere criptato e può essere pubblico.



Questo può essere utilizzato per trasferire:





- frasi **gW-0** (il master seed di ColdCard Q o i segreti conservati nel [seed Vault] di ColdCardQ(https://coldcard.com/docs/temporary-seeds/#seed-vault).
- note e password riservate: può essere un segreto qualsiasi o l'intera directory [Secure Notes & Passwords](https://coldcard.com/docs/secure_notes/) della vostra ColdCardQ.
- un backup dell'intero **ColdCardQ**: il ColdCardQ che riceve questo backup non deve avere un seed Master per funzionare.
- gW-3 (**Transazioni Bitcoin parzialmente firmate**) come parte di uno schema multi-firma.



Ciò richiede l'aggiornamento del [firmware del dispositivo alla versione v1.3.2Q](https://coldcard.com/docs/upgrade/) o superiore.



## Come si usa il Teletrasporto delle chiavi?



### 1- Per trasferire qualsiasi tipo di dati



In questa sede ci occuperemo del trasferimento di frasi seed, note, password o dell'intero trasferimento di un backup ColdCardQ. Il caso dei trasferimenti PSBT per le transazioni con più firme sarà trattato più avanti.



#### Preparare il dispositivo a ricevere i segreti



Nel menu **"Avanzate / Strumenti**" della ColdCardQ, selezionare **"Teletrasporto chiave (avvio) "**.


Nella schermata successiva, viene proposta una password di 8 cifre, qui "20420219". È necessario comunicare questa password al mittente. Per inviare la password si possono usare gli sms, ad esempio, oppure il sistema di messaggistica sicura preferito, o ancora una chiamata vocale.



Cliccare quindi sul pulsante **"Enter**" della ColdCardQ per passare alla fase successiva.




![CCQ-key-teleport](assets/fr/01.webp)




Sullo schermo viene generato un codice QR. Ancora una volta, dovrete comunicare questo codice QR al "mittente" ColdCardQ. Il modo più semplice per farlo è una videochiamata.



**NON INVIATE QUESTO CODICE QR ATTRAVERSO LO STESSO CANALE DI TRASMISSIONE UTILIZZATO PER INVIARE LA PRECEDENTE PASSWORD A 8 CIFRE**.



![CCQ-key-teleport](assets/fr/02.webp)



*Per coloro che sono interessati, cerchiamo di capire il meccanismo sottostante che permette di trasferire segreti su canali non protetti*



*Quello che stiamo facendo in realtà è avviare un trasferimento di segreti tramite il metodo Diffie-Hellman, trattato nel corso BTC204 che ho incluso qui sotto*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Attualmente abbiamo:*




- ha generato una coppia di chiavi effimere (pubblica/privata rispettivamente Ka e ka con Ka=G.ka, G è il punto di generazione ECDH) e una password di 8 cifre.
- ha utilizzato questa password per criptare la chiave pubblica (Ka) tramite AES-256-CTR, quindi ha trasmesso questa password tramite il canale di comunicazione A alla ColdCardQ "mittente".
- infine, abbiamo trasmesso il pacchetto criptato al mittente tramite il codice QR di cui sopra, utilizzando un secondo canale di comunicazione B diverso dal primo.



#### Preparare il dispositivo che invierà i segreti



Dal dispositivo di invio, fare clic sul pulsante **"QR "** per scansionare il codice QR inviato dal dispositivo di ricezione, quindi inserire la password a 8 cifre comunicata nel passaggio precedente tramite un canale separato. Ora siamo pronti per iniziare l'invio dei dati dal dispositivo "mittente".



**Non inserire la password a 8 cifre in modo errato, perché non verrà visualizzato alcun messaggio di errore e il processo continuerà. Tuttavia, il trasferimento finale dei dati fallirà e si dovrà ricominciare da capo**.



![CCQ-key-teleport](assets/fr/03.webp)



*Per i più curiosi, diamo un'altra occhiata a ciò che stiamo facendo in termini di crittografia e di trasferimento di segreti:*




- abbiamo importato i dati criptati scansionando il codice QR sul dispositivo ricevente.
- poi li abbiamo decifrati utilizzando la password a 8 cifre trasmessaci attraverso un canale secondario.
- siamo quindi in possesso della chiave pubblica (Ka) generata inizialmente dal destinatario.
- Quindi generate una nuova coppia di chiavi effimere (Kb/kb, con Kb=G.kb) sul dispositivo di invio, che utilizziamo per applicare ECDH a Ka. Eseguiamo quindi l'operazione kb.Ka=Ks , dove Ks è chiamata **"chiave di sessione "**




Ora vi viene chiesto di scegliere la natura dei segreti da trasmettere tra le 2 ColdCardQ (note riservate, password, backup completo, semi contenuti nel vostro caveau, master del dispositivo seed).



![CCQ-key-teleport](assets/fr/04.webp)



Il nostro segreto sarà un breve messaggio scegliendo **"Quick Text Message "**. Digitare il messaggio (per noi "Rocce di rete PlanB") e premere **"INVIO "**.


Il dispositivo genera quindi una nuova password casuale denominata **"Teleport Password "** , nell'esempio "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Premere **"INVIO "** e verrà presentato un nuovo codice QR. Farlo scansionare dal dispositivo ricevente. Su un altro canale di comunicazione, trasmettere la **"Password di teletrasporto "** al dispositivo ricevente.



![CCQ-key-teleport](assets/fr/06.webp)



*Di nuovo, per i curiosi, durante questa fase:*




- dopo aver selezionato i segreti da trasmettere, generate una nuova password casuale chiamata **"Teleport Password"**.
- quindi criptare i segreti tramite AES-256-CTR utilizzando la **"Session Key"**, "Ks", generata nel passo precedente.
- al pacchetto già crittografato con la **"Session Key "** aggiungiamo la nostra chiave pubblica Kb, quindi aggiungiamo un ulteriore Layer di crittografia AES-256-CTR con la **"Teleport Password "**. Il tutto viene quindi codificato come un codice QR




#### Finalizzare il trasferimento dei segreti al dispositivo ricevente



Premere il pulsante **"QR "** per scansionare il codice QR presentato dal dispositivo di invio attraverso il canale visio. Verrà richiesto di inserire la **"Password di teletrasporto "** per noi "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





I dati vengono quindi decifrati e resi intelligibili al dispositivo ricevente. Il messaggio ricevuto è effettivamente "PlanB Network rocks". Tutto qui.



![CCQ-key-teleport](assets/fr/08.webp)



*Cosa è successo effettivamente durante quest'ultima fase :*?




- abbiamo decifrato i dati trasmessi dal mittente utilizzando la **"Teleport Password "**
- abbiamo quindi la chiave pubblica Kb e il nostro messaggio segreto criptato dalla **"Session Key "**, "Ks". Ma come possiamo fare questo dal momento che, come ricevente, non conosciamo Ks, che è stata creata dal mittente?
- Dobbiamo applicare la nostra chiave privata "ka" dal passaggio iniziale **"Preparare il dispositivo che riceverà i dati"** alla chiave pubblica Kb.
- Infatti, calcolando ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks, troviamo Ks. Che viene infine utilizzato per decifrare il messaggio segreto.



### 2- Trasferimento del PSBT al Multisig (avanzato)



Ciò presuppone che il vostro Wallet Multisig sia già stato creato e che il vostro dispositivo ColdCardQ sia già stato preimpostato per poter eseguire transazioni multi-firma. In caso contrario, le spiegazioni sono disponibili [qui] (https://coldcard.com/docs/Multisig/) sul sito web di Coinkite.



Un breve promemoria su cosa sia un Wallet (Multisig) a firma multipla.



Di solito, per spendere i fondi Wallet, è necessaria una sola chiave privata per sbloccare gli UTXO associati ai vostri indirizzi.


Nel caso di un Wallet Multisig, possono essere necessarie fino a 15 chiavi private e quindi 15 firme per spendere i fondi. Questo è noto come portafoglio "M su N", con N compreso tra 1 e 15 e M il numero di firme necessarie affinché i fondi siano spendibili. Ad esempio, un portafoglio Wallet Multisig 3 su 5 richiederà almeno 3 firme su 5 possibili.



La sfida consiste quindi nel coordinarsi tra i firmatari per firmare un "PSBT" per "Partially Signed Bitcoin Transaction" a turno. In questo contesto, "**Key Teleport**" può essere utilizzato per trasmettere il PSBT tra i cofirmatari in modo semplice e riservato. Una semplice videochiamata tra i cofirmatari è sufficiente.



Ecco come si fa su un Multisig 3 su 4.



**Firmatario 1:**



Il firmatario 1 importa e firma il PSBT. Infine, fa clic su **"T "** per utilizzare **"Key Teleport "** per trasmettere il PSBT al firmatario 2.



![CCQ-key-teleport](assets/fr/09.webp)




Dopo aver selezionato il firmatario 2 cliccando su **"INVIO "**, viene fornita una "PASSWORD TELEPORT" (qui JJ YC AB 6A), che deve essere trasmessa al firmatario 2 tramite un altro canale di comunicazione. Ad esempio, un SMS o una chiamata vocale, ma non una videochiamata.



Premere nuovamente **"ENTER "** e apparirà un codice QR che rappresenta il PSBT firmato da 1 e poi criptato dalla "PASSWORD TELEPORT".



![CCQ-key-teleport](assets/fr/10.webp)



**Firmatario 2:**



Il firmatario 2 esegue la scansione del codice QR presentatogli dal firmatario 1. Quindi inserisce la "PASSWORD TELEPORT" trasmessa sul canale di comunicazione secondario per decifrare i dati trasmessi.



Il firmatario 2 firma la transazione e poi clicca su **"T "** per trasmettere il PSBT al firmatario 3 tramite "Key Teleport".


È evidente che sono già state apposte 2 firme. Manca solo quella del firmatario 3 perché la transazione sia valida. Selezionare il firmatario 3 facendo clic su **"INVIO "**.



![CCQ-key-teleport](assets/fr/11.webp)



Viene creata una nuova "PASSWORD TELEPORT", seguita da un codice QR che codifica il PSBT firmato da 1 e 2 e poi criptato da questa nuova "PASSWORD TELEPORT" (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Firmatario 3:**



Ripetere lo stesso passaggio di cui sopra.


Il firmatario 3 scansiona il codice QR che gli viene presentato dal firmatario 2. Quindi inserisce la "PASSWORD TELEPORT" trasmessa dal canale di comunicazione secondario.



Il firmatario 3 firma la transazione e questa volta, poiché sono state apposte 3 firme su 4, la transazione viene indicata come finalizzata ed è pronta per essere distribuita tramite vari supporti (SD Card, NFC, QR ecc.).



![CCQ-key-teleport](assets/fr/13.webp)



Se la funzione "Push Tx" della ColdCardQ è attivata, è sufficiente applicare la ColdCardQ sul retro di un qualsiasi dispositivo connesso a Internet (smartphone/tablet) abilitato alla tecnologia NFC per trasmettere la transazione attraverso la rete Bitcoin.



![CCQ-key-teleport](assets/fr/14.webp)



*Per il trasferimento del PSBT da un firmatario all'altro, si utilizza semplicemente il "Teleport Key" tramite una "Teleport Password" in ogni fase, che cripta il PSBT mentre viene trasferito da un firmatario all'altro. Poiché i dati trasmessi non possono essere utilizzati per rubare fondi, non è necessario un Diffie-Hellman come nel caso dell'invio di segreti altamente confidenziali (seed, password ecc...)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Fonte: [sito ufficiale di ColdCard](https://coldcard.com/)*
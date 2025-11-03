---
name: COLDCARD - Co-firma
description: Scoprite la funzione Co-Sign e utilizzatela sulla vostra COLDCARD
---

![cover](assets/cover.webp)


*NB: Questo tutorial è rivolto a persone che hanno già una certa esperienza con i portafogli multi-firma, con i dispositivi Coinkite e con software come il Sparrow wallet o il Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Perché ColdCard Co-Sign?



Questa funzione vi permette di aggiungere **condizioni di spesa** al vostro dispositivo ColdCard (Q o Mk4) come un modulo di sicurezza hardware (HSM), per proteggere i vostri fondi mantenendo una notevole flessibilità e controllo su di essi.



Le condizioni di spesa possono essere, ad esempio:





- Limiti di grandezza**: limitano la quantità di bitcoin che si possono spendere in una singola transazione.
- Limiti di velocità:** decidono quante transazioni si possono effettuare per unità di tempo (per ora, giorno, settimana, ecc.), richiedendo un numero minimo di blocchi tra di esse.
- Indirizzi pre-approvati:** Consente l'invio di bitcoin solo a indirizzi pre-approvati.
- Autenticazione a due fattori:** Richiede la conferma da parte di un'applicazione mobile 2FA di terze parti (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) su uno smartphone/tablet abilitato NFC con accesso a Internet.



**Come funziona



Aggiungendo un secondo seed al dispositivo ColdCard Mk4 o Q, chiamato "Spending Policy Key", che in questo tutorial chiameremo "C Key".


Oltre a questo seed aggiuntivo, vi verrà chiesto di Supply almeno una chiave aggiuntiva (XPUB), che chiameremo "chiave di backup", per creare un Wallet Multisig 2-on-N.



In sintesi, creeremo un Wallet Multisig, e il vostro dispositivo ColdCard conterrà 2 delle chiavi private necessarie per spendere i fondi, il master seed del dispositivo e la "Spending Policy Key".



Ogni volta che alla "C Key" viene chiesto di firmare, si applicano le condizioni di spesa specificate e la ColdCard firmerà solo se la transazione è conforme a tali condizioni.



Se si desidera rinunciare a queste condizioni di spesa, è possibile farlo:




- firmando con una delle chiavi di riserva e la mano del seed, oppure con 2 chiavi di riserva a seconda delle dimensioni del vostro Multisig.
- inserendo la "Chiave della politica di spesa" o la "Chiave C" nel menu "Co-Firma". **Quest'ultimo non può essere consultato direttamente sul dispositivo, altrimenti chiunque potrebbe annullare le condizioni di spesa configurate




## Configurazione della ColdCard Co-Sign



![video](https://youtu.be/MjMPDUWWegw)



### 1- Attivare la funzionalità



Prima di tutto, assicuratevi che il vostro dispositivo abbia almeno l'ultima versione del firmware:




- Mk4: v5.4.2
- Q: v1.3.2Q




Sulla vostra Mk4 o ColdCardQ, andate su *Strumenti avanzati > Co-firma ColdCard*.



![Co-Sign](assets/fr/01.webp)



*Nel seguente tutorial, le schermate saranno prese su una ColdCardQ per comodità, ma i passaggi e i menu sono identici tra la Mk4 e la Q.*



Viene visualizzato un riepilogo delle funzionalità.


La terminologia usata per designare le chiavi, che useremo di nuovo nel Wallet multi-firma 2 contro 3 che stiamo per creare, è la seguente:



Chiave A = Coldcard master seed


Chiave B = Chiave di backup


Chiave C = Chiave della politica di spesa



Fare clic su **"INVIO "**.



![Co-Sign](assets/fr/02.webp)



Il passo successivo consiste nel decidere quale chiave privata fungerà da "chiave della politica di spesa" o "chiave C".



Possiamo vedere che abbiamo diverse opzioni a disposizione:





- Oppure premere **"ENTER "** per creare una nuova frase seed di 12 parole.





- Fare clic su **"(1) "** per importare un seed esistente di 12 parole, oppure scegliere **"(2) "** per importare un seed esistente di 24 parole.





- Oppure premere **"(6) "** per importare un seed dal caveau del dispositivo.



Ai fini di questa esercitazione, abbiamo deciso di importare un seed a 12 parole esistente premendo **"(1) "**. Può trattarsi di un qualsiasi seed BIP39 che già possedete e di cui ovviamente disponete di un backup.



Utilizzare la tastiera per inserire le 12 parole del proprio seed. Per questo esempio, sceglieremo la frase valida per il seed: beef x 12. Quindi premere **"INVIO "**.


*NB: se non si dispone di un backup di questo seed, non sarà più possibile modificare le impostazioni di "Co-Sign" sul dispositivo, per cambiare le condizioni di spesa*



La funzione "Co-Sign" è ora attivata sul dispositivo. Successivamente dovremo scegliere le nostre condizioni di spesa, quindi completare la creazione del Wallet a firma multipla.



![Co-Sign](assets/fr/03.webp)



### 2- Scegliere le condizioni di spesa o "*politiche di spesa*"



Qui si specificano le condizioni di spesa che devono essere soddisfatte quando la **"Chiave C "** o la **"Chiave politica di spesa**" firmano una transazione.



Nel menu **"Co-firma "**, fare clic su **"Politica di spesa**".



È quindi possibile scegliere l'entità massima, ossia il numero massimo di satoshi che possono essere spesi in una singola transazione.



Per questo esempio, sceglieremo una magnitudine massima di **21212** satoshis. Fare clic su **"INVIO "** per confermare.




![Co-Sign](assets/fr/04.webp)



Si sceglie poi di impostare la velocità massima, cioè il numero di transazioni che il dispositivo sarà in grado di firmare per unità di tempo. Per questa esercitazione, sceglieremo la velocità illimitata, cioè nessun limite al numero di transazioni.




![Co-Sign](assets/fr/05.webp)



### 3- Creare Wallet Multisig 2-su-N



Dobbiamo ancora scegliere la terza chiave per il nostro Wallet Multisig, cioè la **"Chiave di backup "** (Chiave B), oltre al **master seed** del dispositivo (Chiave A) e alla **"Chiave della politica di spesa "** (Chiave C).



La nostra "chiave B" dovrà essere importata tramite scheda SD o tramite codice QR nel caso di ColdCardQ.


Per fare questo, avremo bisogno di un secondo dispositivo ColdCard Mk4 o Q, sul quale verrà utilizzata la nostra "Chiave B".



Su questo secondo dispositivo contenente la **"Chiave di backup "**, ad esempio una ColdCard Mk4, andare dal menu principale a **"Impostazioni "**, quindi a **"Multisig Wallet"** e infine a **"Esporta Xpub "**.


(Se il vostro secondo dispositivo è un ColdCardQ, avrete la possibilità di esportare il vostro Xpub tramite codice QR, naturalmente).





![Co-Sign](assets/fr/06.webp)





Nella schermata successiva, inserire una scheda SD e fare clic sul pulsante **"convalida "** in basso a destra. Quindi fare clic su **"(1) "** per salvare il file sulla scheda SD.



Il file conterrà l'impronta digitale della chiave pubblica (*fingerprint*) nel nome e avrà la forma `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Inserire quindi la scheda SD nella ColdCardQ "iniziale" per importare la nostra "chiave di backup" (chiave B).


Nel menu "ColdCard Co-Signing", scegliere "Build 2-of-N", quindi nella schermata successiva fare clic su **"ENTER "**, poi ancora **"ENTER "** per importare la "Backup Key" dalla scheda SD.



![Co-Sign](assets/fr/08.webp)



Nella schermata successiva, lasciate in bianco "Numero di conto" (a meno che non sappiate esattamente cosa state facendo) e cliccate nuovamente su **"INVIO "**.



![Co-Sign](assets/fr/09.webp)



Finalmente siamo pronti a utilizzare il nostro nuovo Wallet Multisig 2-sur-3, così composto:



Chiave A= scheda fredda Q master seed


Chiave B= Chiave di backup (appena importata da un secondo dispositivo Coldcard)


Chiave C= Chiave di politica di spesa (se usata per firmare, impone condizioni di spesa predefinite)



## Co-firmare con Sparrow wallet



Se necessario, consultare le esercitazioni riportate di seguito per familiarizzare con il software Sparrow wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Esportazione Wallet Multisig 2-sur-3 a Sparrow wallet



Ora dobbiamo esportare il nostro Wallet Multisig in Sparrow, in modo da potervi collocare i primi satoshi.



Dal menu principale della ColdCardQ, selezionare **"Impostazioni "**, quindi **"Portafogli Multisig"**.


L'insieme dei portafogli Multisig noti alla vostra ColdCard viene ora visualizzato, con il numero di chiavi coinvolte "2/3" (2-sur3). Scegliere il Multisig **"ColdCard Co-Sign "** appena creato, quindi cliccare su **"ColdCard Export "**.



![Co-Sign](assets/fr/10.webp)




Infine, scegliete il metodo che vi permetterà di esportare il Wallet nel Sparrow. Nel nostro caso, sceglieremo la scheda SD e quindi clicchiamo su **"(1) "** dopo aver inserito una scheda SD nello slot A del dispositivo.



![Co-Sign](assets/fr/11.webp)



Quindi, in Sparrow wallet, selezionare "Importa Wallet".



![Co-Sign](assets/fr/12.webp)



Quindi fare clic su **"Importa file "**. Scegliere quindi il file **"export-Coldcard_Co-sign.txt "** sulla scheda SD.



![Co-Sign](assets/fr/13.webp)



Assegnare al Wallet un nome come apparirà nel Sparrow e scegliere una password per criptare il Wallet (o meno).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Ora siamo pronti a ricevere i nostri primi satoshi e a testare le condizioni di spesa che abbiamo applicato al nostro Wallet.



![Co-Sign](assets/fr/16.webp)



### 2- Verifica delle politiche di spesa predefinite



Come promemoria, per il nostro Wallet Multisig avevamo deciso un importo massimo di 21212 satoshis. Ciò significa che ogni volta che la Spending Policiy Key (Chiave C) firmava una transazione, questa sarebbe stata valida solo se l'importo speso fosse stato inferiore o uguale a 21212 satoshis.



Mettiamolo alla prova.


Per prima cosa, facciamo clic sulla scheda "Ricezione" in Sparrow e lasciamo cadere alcuni Satss su Wallet, che utilizzeremo in questa esercitazione.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Proviamo allora a spendere più dei 21212 satoshi consentiti simulando una transazione di 50.000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Dopo aver scansionato il codice QR che rappresenta la transazione *non firmata* con la nostra ColdCardQ per importare la transazione, ecco cosa ci viene mostrato sullo schermo. Un messaggio di avvertimento ci dice che le condizioni di spesa non sono state soddisfatte. Se firmiamo comunque la transazione, solo una delle due chiavi (la master seed sul dispositivo, ma non la "chiave C") firmerà.




![Co-Sign](assets/fr/23.webp)



Qui, dopo aver importato la nostra transazione in Sparrow, possiamo vedere che solo una delle firme è stata applicata alla transazione.



![Co-Sign](assets/fr/24.webp)




Ora ripetiamo l'esperimento, ma per una transazione di 21.000 satoshi, cioè inferiore alla magnitudine massima (21212 Sats) che abbiamo stabilito per questo Wallet.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Proviamo a firmare questa transazione con la nostra ColdCardQ.



Questa volta non ci sono problemi, non appare alcun messaggio di avviso e quando importiamo la transazione firmata in Sparrow wallet, questa volta le due firme sono state applicate, rendendo la transazione valida e pronta per la distribuzione.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Co-firma con il Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA e indirizzi whitelistati



In questo paragrafo, utilizzeremo il nostro Wallet Multisig Co-Sign con Nunchuk e sfrutteremo l'opportunità di applicare nuove condizioni di spesa per vedere come va.



Andate su *Strumenti avanzati > Cofirma della ColdCard*.


Ci viene chiesto di inserire la nostra "Spending Policy Key", per accedere al menu che ci permette di modificare le condizioni di spesa. Nel nostro caso, inseriamo 12 x "manzo".



Abbiamo deciso di mantenere una grandezza di 21212 Sats e una "Velocità limite" massima per ragioni pratiche legate a questo tutorial. D'altra parte, useremo il menu **"Whitelist Addresses "** per imporre gli indirizzi su cui i nostri fondi possono essere spesi.




![Co-Sign](assets/fr/31.webp)




Scansionare i codici QR associati agli indirizzi (ne sceglieremo 2) che si desidera aggiungere alla whitelist, quindi fare clic su **"INVIO "**. Dopo aver convalidato gli indirizzi premendo successivamente **"INVIO "**, vediamo che sono stati applicati i limiti agli indirizzi Magnitude e beneficiari.



![Co-Sign](assets/fr/32.webp)



Infine, per avere un quadro completo delle possibilità offerte da "Co-Sign", attiviamo l'opzione "Web 2FA".


Questa funzione consente di utilizzare un'applicazione conforme a TOTP RFC-6238, come Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / o Aegis Authenticator, per aggiungere un ulteriore Layer di sicurezza.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

In concreto, prima di firmare una transazione, dovrete avvicinare il vostro dispositivo abilitato NFC e connesso a Internet alla vostra Coldcard. In questo modo si accederà automaticamente alla pagina web coldcard.com, dove verrà chiesto di inserire il codice a 6 cifre della propria applicazione. Se inserite il codice giusto, la pagina web vi mostrerà un codice QR da scansionare per la ColdCardQ, oppure un codice a 8 cifre da inserire sul vostro Mk4, per autorizzare il vostro dispositivo a firmare.





![Co-Sign](assets/fr/33.webp)



Dopo aver scansionato il codice QR visualizzato nell'applicazione di doppia autenticazione e aver aggiunto il vostro account ColdCard Co-Sign (CCC), vi verrà chiesto di verificare che tutto sia in ordine inserendo il vostro codice 2FA.



Digitare la ColdCard sul retro del dispositivo NFC.



![Co-Sign](assets/fr/34.webp)



Nella pagina web che si apre, inserite il codice 2FA della vostra applicazione preferita. Poi scansionate il codice QR visualizzato con la vostra ColdCardQ (o inserite il codice a 8 cifre visualizzato nel vostro Mk4).



![Co-Sign](assets/fr/35.webp)




Ora abbiamo imposto un limite alla grandezza (21212 Sats), agli indirizzi di destinazione e alla doppia autenticazione.



![Co-Sign](assets/fr/36.webp)



### 2- Esportazione Wallet Multisig 2 contro 3 a Nunchuk



Esportiamo Wallet Multisig 2 contro 3 nel Nunchuk questa volta, come abbiamo fatto con Sparrow in precedenza.


Andare su *Impostazioni > Portafogli Multisig > 2/3: ColdCard Co-sign > Esportazione ColdCard*.



![Co-Sign](assets/fr/10.webp)



Questa volta scegliere l'opzione NFC per l'esportazione facendo clic sull'omonimo pulsante di ColdcardQ **"NFC "**.



![Co-Sign](assets/fr/37.webp)



Nel Nunchuk, se si apre l'applicazione per la prima volta, fare clic su **"Recupera Wallet esistente "**.



![Co-Sign](assets/fr/38.webp)



Se nell'applicazione è già presente un Wallet, fare clic su **"+"** in alto a destra, quindi su **"Recupera Wallet esistente "**.



![Co-Sign](assets/fr/39.webp)




Scegliere quindi **"Recupero Wallet da COLDCARD "** e **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Infine, toccare il retro dello smartphone sullo schermo della ColdCardQ per importare il Wallet tramite NFC.



![Co-Sign](assets/fr/41.webp)



Il nostro conto e i satoshi precedentemente depositati tramite Sparrow wallet sono tornati.



![Co-Sign](assets/fr/42.webp)



### 3- Verifica delle politiche di spesa predefinite



Proviamo ora a effettuare una transazione che violi le 2 condizioni di spesa impostate. **Cercheremo di spendere più di 21212 Sats a un Address che non è stato approvato.** Proviamo a inviare 22 222 Sats a un Address a caso.



![Co-Sign](assets/fr/43.webp)



Una volta creata la transazione, cliccate sui 3 puntini in alto a destra per esportarla nella vostra ColdCard.



![Co-Sign](assets/fr/44.webp)



Scegliere quindi **"Esportazione tramite BBQR "** e scansionare il codice QR visualizzato con la ColdCardQ.



![Co-Sign](assets/fr/45.webp)



La ColdcardQ visualizza quindi un avviso che, scorrendo verso il fondo dello schermo, chiarisce che la transazione viola le condizioni di spesa, come previsto.



**Si noti che il dispositivo non ci dice quali sono le condizioni di spesa, per evitare che un potenziale aggressore cerchi di aggirare le restrizioni




![Co-Sign](assets/fr/46.webp)



Se si convalida ancora premendo **"INVIO "**, appare il codice QR che rappresenta la transazione firmata. Se lo si importa sul Nunchuk, si può notare che è stata applicata una sola firma.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Eseguiamo esattamente la stessa operazione, ma questa volta con una transazione che rispetta il limite di grandezza (21212 Sats) e spende i satoshi in uno dei 2 indirizzi che abbiamo preconfigurato.



Inviamo il Nunchuk 12121 Sats a uno dei nostri 2 indirizzi. Poi esportiamo la transazione nella nostra ColdCard come fatto in precedenza.



![Co-Sign](assets/fr/49.webp)




Dopo aver importato la transazione non firmata nella nostra ColdCardQ, vediamo cosa ci viene mostrato questa volta.



Un avviso è sempre presente, ma questa volta, scorrendo in fondo allo schermo, vediamo che si tratta di convalidare la transazione tramite 2FA. Il dispositivo ci chiede di avvicinare la ColdcardQ al nostro terminale NFC connesso a Internet (smartphone o tablet), cosa che facciamo.



![Co-Sign](assets/fr/50.webp)



Sul nostro smartphone si apre una pagina web che ci chiede di inserire il nostro codice 2FA, cosa che facciamo grazie a Proton Authenticator.



![Co-Sign](assets/fr/51.webp)





Poi scansionate il codice QR che appare sulla pagina web, per autorizzare la vostra ColdCard a firmare la transazione.


La transazione è ora firmata dalle due chiavi e quindi valida.



Se la funzione "Push Tx" è abilitata sulla vostra ColdCardQ, potete trasmettere la transazione direttamente alla rete con un semplice tocco sul retro del vostro smartphone.



![Co-Sign](assets/fr/52.webp)




Se non avete attivato il "Push tx", premete il pulsante "QR" sulla vostra ColdCardQ per visualizzare la transazione firmata come codice QR e importarla sul Nunchuk, come nell'esempio precedente.



![Co-Sign](assets/fr/53.webp)



Questa volta notiamo che sono state applicate 2 firme, per cui la transazione è pronta per essere trasmessa sulla rete Bitcoin.



![Co-Sign](assets/fr/54.webp)




Siamo giunti alla fine di questo tutorial, che vi darà una panoramica delle possibilità offerte dalla funzionalità Co-Sign integrata nei dispositivi ColdCardQ e Mk4 di Coinkite, nonché del suo utilizzo attraverso portafogli come Sparrow e Nunchuk.
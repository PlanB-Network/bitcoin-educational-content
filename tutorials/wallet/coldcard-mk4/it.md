---
name: COLDCARD Mk4
description: Guida all'impostazione e all'utilizzo di un COLDCARD Mk4 con Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


*gli *Hardware wallet** sono dispositivi fisici realizzati solo per memorizzare la chiave privata del Bitcoin in modo sicuro. Conservano le chiavi private offline, il che significa che gli hacker non possono raggiungerle attraverso Internet. Mentre i **software wallet** sono usati principalmente per le transazioni di tutti i giorni, gli **hardware wallet** sono spesso usati per conservare grandi quantità di bitcoin in modo sicuro per lungo tempo. Quando si effettua una transazione Bitcoin utilizzando i **hardware wallet**, il wallet può firmare le transazioni all'interno del dispositivo, in modo che la chiave privata non sia mai esposta ad ambienti connessi a Internet.


In questa esercitazione esploreremo una delle wallet hardware più popolari prodotte da Coinkite, la Coldcard Mk4. Vedremo come impostare e utilizzare questo wallet hardware per eseguire le transazioni Bitcoin.


## Panoramica della Coldcard Mk4


Coldcard Mk4 è un hardware wallet prodotto da Coinkite. Questo dispositivo è dotato di uno schermo, di un tastierino numerico e di una cover protettiva scorrevole. Inoltre, il dispositivo offre diversi modi per connettersi e interagire, tra cui USB-C, funzionamento in aria utilizzando una scheda MicroSD, NFC e una modalità disco virtuale. L'Mk4 include anche funzioni di sicurezza avanzate, come il BIP39 passphrase e i PIN a sorpresa, che offrono agli utenti un maggiore controllo e una maggiore protezione del proprio Bitcoin.


## Configurazione iniziale: PIN e parole anti-phishing


Per iniziare, la Coldcard Mk4 può essere acquistata direttamente dal [sito web di Coinkite](https://store.coinkite.com/store). Gli acquirenti possono anche scegliere di pagare con valuta fiat o con Bitcoin. Inoltre, è necessaria una scheda MicroSD (4 GB sono sufficienti) e una fonte di alimentazione che può essere collegata tramite cavo USB-C (la Coldcard Mk4 ha solo una porta di alimentazione USB-C). Poiché la Mk4 non dispone di una batteria integrata, deve essere sempre collegata alla fonte di alimentazione durante l'utilizzo.


L'Mk4 viene consegnato in una busta con chiusura a prova di manomissione. Assicurarsi che la borsa non sia stata compromessa. Se notate qualcosa che potrebbe costituire un problema, come danni o strappi sulla borsa, potete informare Coinkite inviando un'e-mail a support@coinkite.com. Inoltre, sulla busta antimanomissione è presente un numero di 12 cifre, a cui ci riferiremo come numero di busta dell'Mk4. Questo numero di busta verrà utilizzato in seguito per verificare che il dispositivo non sia stato manomesso durante la spedizione e che provenga direttamente da Coinkite. Il numero di busta è memorizzato in modo sicuro nel secure element della scheda Cold tramite una memoria flash OTP (One-Time-Programmable), il che significa che non può essere modificato una volta programmato. Quando si accende il dispositivo per la prima volta, il numero visualizzato sullo schermo deve corrispondere a quello della borsa. In questo modo si garantisce che l'Mk4 ricevuto è l'apparecchio originale uscito dalla fabbrica e non è stato sostituito o modificato. Sebbene questa verifica confermi l'integrità del dispositivo solo al momento della prima accensione, il secure element continua a proteggere le chiavi private, il PIN e il passphrase, rendendo estremamente difficile la compromissione del Bitcoin da parte di eventuali manomissioni. Inoltre, le buone pratiche, come la corretta protezione dei dati relativi al wallet, contribuiranno alla sicurezza generale della scheda Cold stessa. Per ulteriori informazioni, è possibile consultare questo [articolo](https://blog.coinkite.com/understanding-mk4-security-model/) che illustra il modello di sicurezza della Coldcard.


La tastiera è composta da 10 pulsanti numerici, un pulsante OK (`✓`) e un pulsante Annulla (`✕`). Alcuni pulsanti numerici possono essere utilizzati anche per la navigazione: `5` per navigare verso l'alto (`^`), `7` per navigare verso sinistra (`<`), `8` per navigare verso il basso (`˅`) e `9` per navigare verso destra (`>`).


![01](assets/en/01.webp)


Se l'imballaggio non presenta problemi, è possibile aprire la busta. L'Mk4 viene fornito con una scheda di backup wallet che può essere utilizzata per memorizzare le informazioni relative al PIN del dispositivo, alle parole anti-phishing e al seedphrase. Seguire i seguenti passaggi per l'inizializzazione:


1. Preparate un foglio di carta e una penna.

2. Collegare l'Mk4 a una fonte di alimentazione (cavo USB-C) e inserire la scheda MicroSD.

3. Una volta acceso il dispositivo per la prima volta, sullo schermo verrà visualizzato un messaggio relativo alle Condizioni di vendita e di utilizzo di Coldcard. Spostarsi verso il basso, quindi premere `✓` per continuare.

4. Sullo schermo viene quindi visualizzato un numero di 12 cifre. Controllare questo numero con quello riportato sulla busta antimanomissione e con la copia aggiuntiva del numero della busta inclusa nella busta antimanomissione per verificare che il dispositivo non sia stato manomesso. Se i numeri non corrispondono, contattare immediatamente l'assistenza Coinkite prima di procedere. Altrimenti, premere `✓` per continuare.


![02](assets/en/02.webp)


5. Selezionare "Scegliere il codice PIN".

6. Navigare verso il basso mentre si leggono le istruzioni per passare alla fase successiva.


![03](assets/en/03.webp)


7. Sull'Mk4, creare e inserire il prefisso PIN (deve essere lungo da 2 a 6 caratteri) e annotarlo, quindi premere `✓` per continuare.

8. Scrivete le due parole visualizzate sullo schermo. Sono le parole anti-phishing. Premere `✓` per continuare.


![04](assets/en/04.webp)


9. Creare e inserire il suffisso del PIN (o il resto del PIN, deve essere lungo da 2 a 6 caratteri) e annotarlo. Premere `✓` per continuare.

10. Reinserire il prefisso PIN. Premere `✓` per continuare.


![05](assets/en/05.webp)


11. Verificate se le parole anti-phishing sono uguali a quelle scritte al punto 8. Premere `✓` per continuare.

12. Reinserire il suffisso del PIN (o il resto del PIN). Premere `✓` per continuare.


![06](assets/en/06.webp)


13. Il PIN e le parole anti-phishing del vostro Mk4 sono state create e memorizzate con successo dal dispositivo.


![07](assets/en/07.webp)


Si noti che l'Mk4 chiederà sempre di inserire il PIN ogni volta che si accende il dispositivo. Senza questo PIN, non è possibile accedere al Coldcard Mk4. Assicuratevi quindi di creare un backup sufficiente del PIN e delle parole anti-phishing.


## Impostazione del Wallet


Il passo successivo consiste nell'impostare il wallet. Esistono tre modi per farlo:


- Creazione di un nuovo wallet (standard)
- Creare un nuovo wallet con i tiri di dado
- Importazione di un wallet


### Creazione di un nuovo wallet (standard)


Per creare un nuovo wallet, è sufficiente eseguire le seguenti operazioni.


1. Selezionare `New Wallet` (o `New Seed Words`) > Selezionare `12 Word` o `24 Word (default)` a seconda delle preferenze.


![08](assets/en/08.webp)


2. Il dispositivo genererà 12 o 24 parole come seedphrase in base alla vostra scelta. Navigare verso il basso scrivendo attentamente ogni parola nell'ordine corretto. Quindi, premere `✓` per continuare.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Il dispositivo vi chiederà di verificare il vostro seedphrase ponendo domande in ordine casuale (ad esempio, `Parola 1 è?`, poi `Parola 5 è?`, poi `Parola 12 è?`, e così via) e ci saranno tre scelte di parole per ogni domanda. Fate riferimento alla nota della fase 2 e scegliete le parole in modo corretto (premendo `1`, `2` o `3`, a seconda di quale corrisponda alla parola corretta) per completare la creazione del wallet.


![09](assets/en/09.webp)


4. L'Mk4 chiederà quindi se si desidera abilitare l'NFC/Tap o meno. Per ora, selezionare `✕` per questa opzione. In futuro, questa opzione potrà essere modificata nelle impostazioni.

5. Infine, l'Mk4 vi chiederà anche se volete disabilitare la porta USB (che può essere usata per il trasferimento di dati senza aria). Per ora, selezionare `✓` per questa opzione. In futuro, questa opzione potrà essere modificata nelle impostazioni.

6. Sullo schermo viene visualizzato il menu principale con la dicitura "Pronto per la firma" in alto. Questo segna il completamento del processo di creazione del wallet.


![10](assets/en/10.webp)


### Creare un nuovo wallet con lancio di dadi


In alternativa, si può anche scegliere di generare il nuovo seedphrase con l'entropia. Fatelo se non vi fidate del seedphrase appena generato da Mk4.


La procedura per la Coldcard Mk4 è la seguente:


1. Selezionare `New Wallet` (o `New Seed Words`) > Selezionare `12 Word Dice Roll` o `24 Word Dice Roll` a seconda delle preferenze.

2. Vi verrà chiesto di inserire i risultati dei vostri lanci di dadi. Ogni lancio di dadi aggiunge casualità al processo di creazione del wallet, assicurando che il vostro seedphrase sia generato in modo del tutto sicuro e imprevedibile. Il numero minimo di lanci è 50 per un seedphrase di 12 parole e 99 per un seedphrase di 24 parole. Premere `✓` dopo aver inserito almeno 99 valori di lancio dei dadi.


![11](assets/en/11.webp)


3. Il dispositivo genererà 12 o 24 parole come seedphrase in base alla vostra scelta. Navigare verso il basso scrivendo attentamente ogni parola nell'ordine corretto. Quindi, premere `✓` per continuare.

4. Il dispositivo vi chiederà di verificare il vostro seedphrase ponendo domande in ordine casuale (ad esempio, `Parola 1 è?`, poi `Parola 5 è?`, poi `Parola 12 è?`, e così via) e ci saranno tre scelte di parole per ogni domanda. Fare riferimento alla nota del passaggio 3 e scegliere correttamente le parole (premendo `1`, `2` o `3`, a seconda di quale corrisponda alla parola corretta) per completare la creazione del wallet.


![12](assets/en/12.webp)


5. L'Mk4 chiederà quindi se si desidera abilitare l'NFC/Tap o meno. Per ora, selezionare `✕` per questa opzione. In futuro, questa opzione potrà essere modificata nelle impostazioni.

6. Infine, l'Mk4 vi chiederà anche se volete disabilitare la porta USB (che può essere usata per il trasferimento di dati senza aria). Per ora, selezionare `✓` per questa opzione. In futuro, questa opzione potrà essere modificata nelle impostazioni.

7. Sullo schermo apparirà il menu principale con la dicitura "Pronto a firmare" in alto. Questo segna il completamento del processo di creazione del wallet.


![13](assets/en/13.webp)


### Importazione di un wallet


L'ultima opzione prevede l'importazione di un wallet. È possibile farlo se si desidera recuperare un wallet da un seedphrase già in possesso. Seguite i seguenti passaggi:


1. Selezionare "Importazione esistente".

2. Selezionare `24 Parole`, `18 Parole` o `12 Parole`, a seconda del numero di parole del vostro seedphrase.


![14](assets/en/14.webp)


3. Coldcard Mk4 vi chiederà quindi il significato di ciascuna parola in ordine consecutivo. Per ogni parola, navigare verso il basso o verso l'alto fino a trovare il prefisso di scrittura per ogni parola. Il dispositivo restringe le possibilità fino a trovare la parola corretta. Procedete in questo modo per le altre parole.

4. Per la parola finale, Coldcard Mk4 visualizzerà solo un numero limitato di parole possibili. Se non ci sono corrispondenze, è possibile che le parole siano state inserite in modo errato. In caso contrario, selezionare la parola che corrisponde a quella presente sulla seedphrase.


![15](assets/en/15.webp)


5. L'Mk4 chiederà quindi se si desidera abilitare l'NFC/Tap o meno. Per ora, selezionare `✕` per questa opzione. In futuro, questa opzione potrà essere modificata nelle impostazioni.

6. Infine, l'Mk4 vi chiederà anche se volete disabilitare la porta USB (che può essere usata per il trasferimento di dati senza aria). Per ora, selezionare `✓` per questa opzione. In futuro, questa opzione potrà essere modificata nelle impostazioni.

7. Sullo schermo verrà visualizzato il menu principale con la dicitura "Pronto per la firma" in alto. Questo segna il completamento della procedura di creazione del wallet.


![16](assets/en/16.webp)


Tenere presente che il seedphrase è l'unico accesso per recuperare il wallet. Create un backup del vostro seedphrase e conservatelo in un luogo sicuro. **Non le vostre chiavi, non le vostre monete**, chiunque abbia il vostro seedphrase ha accesso ai vostri bitcoin!


## Impostazione del passphrase


Una delle migliori pratiche del Bitcoin consiste nell'utilizzare un passphrase. Il passphrase funge da 13° o 25° parola in aggiunta al seedphrase. La differenza sta nel fatto che si può scegliere la frase che si desidera, mentre il seedphrase viene selezionato da un elenco predeterminato di 2048 parole. Per impostazione predefinita, dopo aver impostato il wallet, si inizierà con un wallet con un passphrase vuoto. Per impostare un passphrase non vuoto, è sufficiente eseguire le seguenti operazioni:


1. Andare su `Passphrase`.

2. Navigare verso il basso per leggere la descrizione di passphrase, quindi premere `✓` per procedere.

3. Selezionare "Modifica frase".


![17](assets/en/17.webp)


4. Inserite il vostro passphrase:


   - Premere `1` (lettere), `2` (numeri) o `3` (simboli) per selezionare il tipo di carattere.
   - Premere `4` per passare dalle lettere minuscole a quelle maiuscole (può essere utilizzato solo durante l'immissione delle lettere).
   - Navigare utilizzando `^` o `˅` per selezionare il personaggio per il proprio passphrase.
   - Navigare usando `<` o `>` per spostarsi tra i caratteri. Si può anche usare `>` per aggiungere spazi.
   - Premere `✕` per eliminare i caratteri.
   - Premere `✓` al termine della modifica del passphrase.

5. Inoltre, le altre opzioni hanno le seguenti funzionalità:


   - Le funzioni `Aggiungi parola` o `Aggiungi numeri` possono essere utilizzate per aggiungere lettere/numeri al passphrase che si sta modificando.
   - Premere `Clear ALL` per resettare il passphrase che si sta modificando.
   - Premere `CANCEL` per tornare al menu principale.

6. Annotare il passphrase come backup.

7. Premere `APPLY` per accedere al wallet con il passphrase appena impostato.

8. L'Mk4 visualizzerà quindi un'impronta digitale della chiave master lunga 8 caratteri. Questo può essere considerato l'"ID" del wallet. Annotare questa impronta digitale e premere `✓` per procedere.


![18](assets/en/18.webp)


9. A questo punto, il wallet visualizzerà il menu principale del wallet con il passphrase inserito.

10. È importante notare che un wallet non vi dirà che avete inserito un passphrase errato, perché ogni passphrase corrisponde a un wallet con un'identità unica (impronta digitale della chiave master). Pertanto, è buona norma inserire nuovamente lo stesso passphrase e verificare se produce la stessa impronta digitale del wallet, assicurandosi di averla inserita correttamente. A tal fine, eseguire i passaggi da 11 a 14.

11. Nel menu principale, selezionare `Ripristina master`, quindi premere `✓`. Ora si torna al menu principale del wallet con il passphrase vuoto.


![19](assets/en/19.webp)


12. Passare nuovamente a `Passphrase`, quindi premere `✓` per procedere.

13. Reinserire il passphrase scritto al punto 6, quindi premere `APPLY`.

14. Controllare l'impronta digitale della chiave master lunga 8 caratteri con quella annotata al passaggio 8. Se le due impronte non corrispondono, è possibile che siano state digitate in modo errato. Se le due impronte non corrispondono, è possibile che siano stati digitati caratteri non corrispondenti. È possibile selezionare una nuova passphrase e ripetere la procedura dal passaggio 1. Se invece entrambe le impronte corrispondono, è possibile che siano state digitate in modo errato. Se invece le due impronte corrispondono, significa che il passphrase è stato immesso correttamente.

15. Il wallet con il passphrase scelto è pronto per essere utilizzato.


## Esportazione del Wallet in Sparrow


Come altri wallet hardware, la Coldcard Mk4 non può essere utilizzata da sola. Deve essere collegata a un software wallet che funge da interfaccia. Il software wallet consente di visualizzare il saldo, creare transazioni e gestire gli indirizzi, mentre la Coldcard firma in modo sicuro le transazioni senza esporre le chiavi private.


In questa esercitazione, utilizzeremo il Sparrow Wallet come interfaccia. La procedura per esportare il wallet è la seguente:


1. Assicurarsi di avere una scheda MicroSD inserita nella Mk4.

2. Eseguire i passaggi "Impostazione del passphrase" sul wallet con il passphrase che si desidera esportare. Se si desidera esportare il wallet con il passphrase vuoto, è possibile saltare questo passaggio.

3. Andare in `Avanzate/Strumenti` > Scegliere `Esporta Wallet` > Selezionare `Generico JSON` > Scorrere verso il basso leggendo le istruzioni, quindi premere `✓`.


![20](assets/en/20.webp)


4. Mk4 ha creato un file in formato `.json` nella scheda MicroSD.


![21](assets/en/21.webp)


5. Rimuovere la scheda MicroSD dalla scheda Cold e inserirla nel dispositivo in cui è installato il Sparrow Wallet.

6. Aprire Sparrow Wallet.

7. Fare clic su "File"


![22](assets/en/22.webp)


Quindi, fare clic su "Nuovo Wallet"


![23](assets/en/23.webp)


Quindi, inserire il nome del wallet


![24](assets/en/24.webp)


Successivamente, fare clic su "Crea Wallet"


![25](assets/en/25.webp)


8. Selezionare il `tipo di script`.


![26](assets/en/26.webp)


9. Nella sezione Keystore, selezionare `Airgapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Cercare Coldcard e fare clic su `Importa file...`.


![28](assets/en/28.webp)


11. Selezionare il file creato nel passaggio 4 (quello con il formato `.json`).


![29](assets/en/29.webp)


12. Sull'Mk4, tornare al menu principale e spostarsi su `Avanzate/Strumenti` > `Visualizza identità`. Assicurarsi che l'impronta digitale visualizzata sullo schermo dell'Mk4 corrisponda a quella del Sparrow Wallet (l'impronta digitale Master nella sezione Keystore)

13. Fare clic sul pulsante "Applica" nell'angolo in basso a destra.


![30](assets/en/30.webp)


14. È possibile aggiungere una password per il wallet esportato. Questa password è necessaria ogni volta che si apre l'applicazione Sparrow Wallet per accedere al wallet. Se in futuro si dimentica la password, è sufficiente ripetere i passaggi da 1 a 13 e scegliere una nuova password.


![31](assets/en/31.webp)


15. Il wallet è stato esportato con successo ed è pronto per essere utilizzato.


![32](assets/en/32.webp)


## Ricevere bitcoin


Successivamente, impareremo a ricevere il Bitcoin utilizzando l'Mk4. Questo processo è abbastanza semplice perché non è necessario utilizzare il dispositivo Mk4. Se avete già esportato il vostro wallet in Sparrow, potete ricevere Bitcoin direttamente tramite Sparrow Wallet. Seguite questi passaggi per ricevere bitcoin con Mk4:


1. Aprire Sparrow Wallet.

2. Selezionare `Aprire Wallet` > Scegliere il file wallet in cui si desidera ricevere bitcoin > Inserire la password associata a quel wallet.


![33](assets/en/33.webp)


3. Nell'interfaccia del Sparrow, fare clic sulla scheda "Ricezione" sul lato sinistro dell'interfaccia.


![34](assets/en/34.webp)


4. In alto apparirà un indirizzo e un codice QR. È possibile copiare e incollare l'indirizzo o scansionare il codice QR utilizzando il wallet che si utilizzerà per inviare bitcoin al Sparrow Wallet. Opzionalmente, è possibile digitare un'etichetta per i bitcoin ricevuti.


![35](assets/en/35.webp)


5. Dopo aver inviato i bitcoin, nell'interfaccia del Sparrow, fare clic sulla scheda "Transazioni" sul lato sinistro dell'interfaccia. Vedrete una nuova voce in cima alla cronologia delle transazioni, che corrisponde alla transazione appena effettuata.


![36](assets/en/36.webp)


6. È anche possibile navigare sulla scheda `UTXOs` sul lato sinistro dell'interfaccia per vedere i bitcoin appena ricevuti.


![37](assets/en/37.webp)


## Invio di bitcoin


A differenza della ricezione di bitcoin, per spendere i bitcoin associati alla propria Coldcard è necessario utilizzare la Coldcard per firmare le transazioni. La procedura di invio di bitcoin con Mk4 è la seguente:


1. Inserire la scheda MicroSD nel dispositivo in cui è installato il Sparrow Wallet.

2. Aprire Sparrow Wallet.

3. Selezionare `Aprire Wallet` > Scegliere il file wallet che si desidera utilizzare per inviare bitcoin > Inserire la password associata a quel wallet.


![38](assets/en/38.webp)


4. Nell'interfaccia del Sparrow, fare clic sulla scheda "Invio" sul lato sinistro dell'interfaccia.


![39](assets/en/39.webp)


5. Nella scheda `Pagare a`, inserire l'indirizzo a cui si desidera inviare i bitcoin.

6. Aggiungere un'etichetta per la transazione.

7. Inserire l'importo di bitcoin che si desidera inviare.

8. Immettere la tariffa selezionando l'opzione "Intervallo" o inserire direttamente un numero nella parte "Tariffa".


![40](assets/en/40.webp)


9. Nell'angolo in basso a destra, fare clic su "Crea transazione".


![41](assets/en/41.webp)


10. Verrà visualizzata una nuova scheda di transazione il cui nome è l'etichetta inserita al punto 6. Fare clic su "Finalizza transazione per la firma".


![42](assets/en/42.webp)


11. Fare clic su "Salva transazione" e salvare la transazione nella scheda MicroSD. Rinominare il file se necessario. Questo passaggio salverà la transazione come file PSBT.


![43](assets/en/43.webp)


12. Rimuovere la scheda MicroSD e inserirla nella Coldcard Mk4.

13. Accendere l'Mk4 collegandolo a una fonte di alimentazione.

14. Immettere il PIN.

15. Andare su `Passphrase` e inserire il passphrase del wallet che si vuole usare per inviare i bitcoin. Se si desidera utilizzare il wallet con il passphrase vuoto, saltare questo passaggio.

16. Assicurarsi che l'impronta digitale della chiave master sia la stessa di quella del Sparrow Wallet. È possibile verificarlo nella scheda "Impostazioni" del Sparrow Wallet sul lato sinistro dell'interfaccia. Quindi, premere `✓` sul proprio Mk4 per procedere. Si accede così al menu principale.

17. Nel menu principale dell'Mk4, selezionare "Pronto a firmare". Sullo schermo apparirà il messaggio `OCCORRE INVIARE? Assicurarsi che l'importo dei bitcoin che si desidera inviare e l'indirizzo del destinatario siano tutti corretti. Premere `✓` per confermare o `✕` per annullare.

18. Se ci sono più file PSBT tra cui scegliere, l'Mk4 visualizzerà il messaggio "Scegli il file PSBT da firmare". Premere `✓` per continuare. Quindi, selezionare il file PSBT che si desidera firmare navigando verso il basso o verso l'alto. Eseguire il passaggio 17 per quella transazione.


![44](assets/en/44.webp)


19. L'Mk4 visualizzerà il messaggio `PSBT Signed` insieme al nome del file del PSBT firmato. Premere `✓` per continuare.

20. Rimuovere la scheda MicroSD dalla scheda Cold e inserirla nel dispositivo in cui è installato il Sparrow Wallet.

21. Su Sparrow Wallet, fare clic su "Carica transazione".


![45](assets/en/45.webp)


22. Selezionate il file con lo stesso nome di quello creato al punto 19.


![46](assets/en/46.webp)


23. Fare clic su "Trasmissione di una transazione".


![47](assets/en/47.webp)


24. La transazione è stata trasmessa ed è in fase di elaborazione. È possibile accedere alla scheda `Transazioni` per visualizzare lo stato di conferma della transazione.


![48](assets/en/48.webp)


## Aggiornamento del firmware


### Verifica della versione del firmware


Il firmware di Coldcard Mk4 può sempre essere aggiornato a una versione più recente. Per verificare se l'Mk4 è stato aggiornato all'ultima versione o meno, eseguire i seguenti passaggi:

1. Accendere l'Mk4 collegandolo a una fonte di alimentazione.

2. Immettere il PIN.

3. Andare in `Avanzate/Strumenti` > Selezionare `Aggiornamento firmware` > Selezionare `Mostra versione`.


![49](assets/en/49.webp)


Verificare la versione visualizzata sullo schermo dell'Mk4 rispetto a quella presente sul sito web [Coinkite] (https://coldcard.com/downloads). Se la versione è diversa, è possibile aggiornare il firmware alla versione più recente.


![50](assets/en/50.webp)


### Aggiornamento del firmware


Se si desidera aggiornare il firmware alla versione più recente, procedere come segue:


1. Inserire la scheda MicroSD nel computer portatile/PC.

2. Andare sul sito [Coinkite] (https://coldcard.com/downloads) e scaricare il firmware più recente sulla scheda MicroSD (il pulsante rosso a destra dell'immagine Mk4 con il numero di versione).


![51](assets/en/51.webp)


È possibile scaricare anche altre versioni facendo clic su `Tutti i file su Mk4` ed esplorando la versione che si desidera scaricare. Il file scaricato sarà in formato `.dfu`.


![52](assets/en/52.webp)


3. Rimuovere la scheda MicroSD e inserirla nella Mk4.

4. Accendere l'Mk4 collegandolo a una fonte di alimentazione.

5. Immettere il PIN.

6. Andare su `Avanzate/Strumenti` > Selezionare `Aggiornamento firmware` > Selezionare `Da microSD` > Scorrere verso il basso leggendo le istruzioni e premere `✓`.


![53](assets/en/53.webp)


7. Selezionare il file `.dfu` scaricato al punto 2.

8. La Coldcard Mk4 visualizzerà il messaggio `Installare questo nuovo firmware? Scorrere verso il basso leggendo le istruzioni e premere `✓`.


![54](assets/en/54.webp)


9. Attendere che l'Mk4 termini l'installazione del nuovo firmware. Non scollegare l'alimentazione durante l'installazione.

10. Al termine, l'Mk4 si riavvia da solo. È possibile inserire il PIN ed eseguire la procedura "Controllo della versione del firmware" per verificare se il firmware è stato aggiornato o meno.


## Caratteristiche avanzate


### Modifica del PIN


Se si desidera modificare il PIN di accesso, è sufficiente eseguire i seguenti passaggi:


1. Preparate una penna e un foglio di carta.

2. Accendere l'Mk4 collegandolo a una fonte di alimentazione.

3. Immettere il PIN.

4. Andare a `Impostazioni` > selezionare `Impostazioni di accesso` > selezionare `Modifica del PIN principale`

5. Navigare verso il basso mentre si legge il messaggio, quindi premere `✓` per procedere.


![55](assets/en/55.webp)


6. Immettere il vecchio PIN.

7. Inserite il nuovo prefisso PIN (deve essere lungo da 2 a 6 caratteri) e annotatelo.

8. A questo punto Mk4 visualizzerà due nuove parole anti-phishing; annotatele, quindi premete `✓` per procedere.

9. Inserite il nuovo suffisso del PIN (o il resto del PIN, deve essere lungo da 2 a 6 caratteri) e annotatelo.


![56](assets/en/56.webp)


10. Reinserire il nuovo prefisso PIN.

11. Verificate se le parole anti-phishing corrispondono a quelle scritte al punto 8.

12. Reinserire il nuovo suffisso del PIN (o il resto del PIN).


![57](assets/en/57.webp)


13. Il PIN è stato modificato con successo.


### PIN dei trucchi - Aggiungi un nuovo trucco


Il PIN di sicurezza è un codice PIN alternativo, diverso da quello utilizzato per la prima configurazione della Coldcard Mk4. Quando si accende l'Mk4, è possibile inserire il PIN truffa al posto del PIN principale per attivare determinate azioni. Per configurare il PIN di sicurezza nell'Mk4, procedere come segue:


1. Preparate una penna e un foglio di carta.

2. Accendere l'Mk4 collegandolo a una fonte di alimentazione.

3. Immettere il PIN.

4. Andare in `Impostazioni` > selezionare `Impostazioni di accesso` > selezionare `PIN truccato` > selezionare `Aggiungi nuovo trucco`.


![58](assets/en/58.webp)


5. Inserite il vostro prefisso PIN (deve essere lungo da 2 a 6 caratteri) e annotatelo.

6. A questo punto Mk4 visualizzerà due nuove parole anti-phishing; annotatele, quindi premete `✓` per procedere.

7. Inserite il suffisso del vostro PIN truccato (o il resto del PIN, che deve essere lungo da 2 a 6 caratteri) e annotatelo.


![59](assets/en/59.webp)


8. Spostarsi verso il basso o verso l'alto per selezionare l'azione che si desidera associare al PIN truccato appena creato. L'elenco delle azioni è il seguente:


    - se si seleziona `Brick Self`, i chip della Mk4 verranno distrutti dopo l'inserimento del PIN, rendendo la Mk4 inutilizzabile in modo permanente.
    - `Cancellare il seme`, è possibile scegliere tra le seguenti azioni:
      - cancella e riavvia": Il seed viene cancellato e la scheda Cold si riavvia dopo l'inserimento del PIN.
      - cancellazione silenziosa: Il seed viene cancellato silenziosamente, ma la scheda Cold si comporterà come se il PIN fosse stato inserito in modo errato.
      - `Cancellare -> Wallet`: Il seed viene cancellato silenziosamente e la scheda Cold vi porterà in un wallet a rischio.
    - se selezionato, il vostro Mk4 porterà a un wallet dopo l'inserimento del PIN.
    - nel `conto alla rovescia`, è possibile scegliere tra le seguenti azioni:
      - cancella e conto alla rovescia": Il seed viene immediatamente cancellato, quindi l'Mk4 inizia a visualizzare un conto alla rovescia.
      - conto alla rovescia e mattone": Il conto alla rovescia ha inizio e l'Mk4 si blocca allo scadere del tempo.
      - conto alla rovescia": L'Mk4 inizierà il conto alla rovescia e si riavvierà da solo allo scadere del tempo.
    - se si seleziona "Look Blank", dopo l'inserimento del PIN, la scheda Cold si comporta come se il seedphrase fosse stato cancellato, ma in realtà è ancora in memoria.
    - se si seleziona `Just Reboot`, la scheda Cold si riavvia da sola dopo l'inserimento del PIN di sicurezza.
    - modalità Delta", questa funzione avanzata è destinata agli utenti esperti ed è progettata per proteggere da minacce gravi, come la coercizione da parte di qualcuno con conoscenze interne. Quando la modalità Delta è attivata, la COLDCARD sembra aprire il vero wallet, consentendo all'aggressore di navigare e confermare l'aspetto autentico. Tuttavia, blocca segretamente la firma delle transazioni, per cui non è possibile inviare bitcoin. Inoltre, disabilita l'accesso alla frase seed e qualsiasi tentativo di visualizzarla la cancellerà completamente. Per rendere il falso wallet più convincente, il Trick PIN utilizzato per la Modalità Delta deve iniziare con gli stessi numeri del PIN reale (in modo da mostrare le stesse parole anti-phishing) ma terminare in modo diverso.
    - se si seleziona `Sblocco della politica`, la politica di spesa del firmatario unico (SSSP) verrà disattivata dopo l'inserimento del PIN di sicurezza.
    - quando viene selezionata, questa opzione finge di disabilitare l'SSSP, ma nel frattempo cancella il seedphrase.

9. Dopo aver selezionato l'azione che si desidera associare al PIN truccato, confermare la scelta premendo `✓`. Il PIN truccato è stato configurato con successo.

10. In `Impostazioni` > `Impostazioni di login` > `NIP truccati`, è possibile visualizzare l'elenco dei PIN truccati creati e le azioni ad essi abbinate. È possibile scegliere di riconfigurare i PIN truccati e le azioni ad essi abbinate. È anche possibile nasconderlo o eliminarlo selezionando il PIN e poi scegliendo `Nascondi trucco` o `Elimina trucco`.


![60](assets/en/60.webp)


### PIN truccati - Aggiungere se sbagliato


In alternativa, è possibile aggiungere un'azione "Aggiungi se sbagliato" che verrà attivata dopo l'inserimento di un PIN errato per un certo numero di volte. È possibile configurare questa azione eseguendo i seguenti passaggi:


1. Accendere l'Mk4 collegandolo a una fonte di alimentazione.

2. Immettere il PIN.

3. Andare in `Impostazioni` > selezionare `Impostazioni di accesso` > selezionare `PIN truccati` > selezionare `Aggiungi se sbagliato`.


![61](assets/en/61.webp)


4. L'Mk4 visualizzerà un messaggio relativo a questa impostazione. Navigare verso il basso leggendo la spiegazione, quindi premere `✓` per procedere.

5. Immettere il numero di tentativi errati necessari per attivare l'azione. Nota: il numero massimo di tentativi è `12`. Questo perché l'Mk4 è progettato in modo tale che quando il PIN errato viene inserito `13` volte, il dispositivo si blocca, rendendolo inutilizzabile in modo permanente. Dopo aver inserito il numero, premere `✓` per continuare.

6. Spostarsi verso l'alto o verso il basso per selezionare l'azione. Le azioni disponibili sono le seguenti:


   - cancella, Stop": Il seedphrase viene cancellato e il dispositivo mostra "Seed is wiped, Stop"
   - cancella e riavvia": Il seedphrase viene cancellato e il dispositivo si riavvia senza alcun messaggio.
   - cancellazione silenziosa: Il seedphrase viene cancellato silenziosamente e il dispositivo si comporta come un tentativo di PIN errato (nessun messaggio di cancellazione evidente).
   - `Brick Self`: Il dispositivo è permanentemente disabilitato e mostra solo "Bricked"
   - ultima possibilità: Il seedphrase viene cancellato, ma è possibile effettuare un ultimo tentativo di inserimento del PIN; se si inserisce nuovamente il PIN sbagliato, il dispositivo viene bloccato.
   - riavvio semplice": Il dispositivo si riavvia semplicemente e non cambia nulla.

Scegliere l'azione che si desidera applicare e premere `✓` per procedere


![62](assets/en/62.webp)


7. Verrà visualizzata la directory `Impostazioni > Impostazioni di accesso > PIN truccati`. Sotto la voce `PIN truccati`, si trova l'elenco dei PIN truccati con l'azione `PIN SBAGLIATO`. È anche possibile nasconderlo o eliminarlo selezionando il PIN e poi scegliendo `Nascondi trucco` o `Elimina trucco`.


![63](assets/en/63.webp)



## Conclusione


Questo tutorial spiega come configurare Mk4, come effettuare transazioni Bitcoin con Mk4 e come utilizzare alcune funzioni avanzate di Mk4. Mk4 offre un modo sicuro e flessibile per conservare e gestire i bitcoin. Il suo design fa sì che le chiavi private non lascino mai il dispositivo, mentre funzioni come i passphrase, i PIN a trabocchetto e le transazioni air-gapped offrono agli utenti il pieno controllo della loro configurazione di sicurezza. Può essere accoppiato con Sparrow Wallet per un'esperienza semplice di creazione, firma e gestione delle transazioni Bitcoin senza compromettere la privacy o la sicurezza.


Se desiderate esplorare altre funzionalità, potete consultare la documentazione sul sito Web di Coinkite [qui] (https://coldcard.com/docs/). Spero che questa guida vi sia utile per l'utilizzo della vostra Coldcard Mk4. Grazie e alla prossima volta!
---
name: Ashigaru - Stowaway
description: Come si effettua una transazione Payjoin su Ashigaru?
---
![cover](assets/cover.webp)



> *Costringere le spie della blockchain a ripensare a tutto ciò che pensano di sapere*

Payjoin è una struttura di transazione Bitcoin progettata per migliorare la riservatezza dell'utente attraverso la collaborazione diretta con il destinatario del pagamento. Esistono diverse implementazioni per facilitarne la realizzazione e automatizzare il processo. La più nota è senza dubbio Stowaway, sviluppata inizialmente dal team di Samurai Wallet e ora integrata nel suo fork Ashigaru.



## Come funziona Stowaway?



Come già detto, Ashigaru integra uno strumento PayJoin chiamato `Stowaway`. Questo strumento è disponibile nell'applicazione Ashigaru su Android. Per effettuare un Payjoin, il destinatario (che assume anche il ruolo di collaboratore) deve utilizzare un software compatibile con Stowaway, quindi per il momento solo Ashigaru.



Stowaway si basa su una categoria di transazioni che Samurai ha definito "Cahoots". Una Cahoot è una transazione collaborativa tra più utenti, che comporta uno scambio di informazioni al di fuori della blockchain Bitcoin. Ashigaru offre attualmente due strumenti Cahoots: Stowaway (Payjoins) e StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Le transazioni Cahoots richiedono lo scambio di transazioni parzialmente firmate tra gli utenti. Questo processo può essere lungo e noioso, soprattutto se effettuato in remoto. Tuttavia, è ancora possibile farlo manualmente, se i collaboratori si trovano nello stesso luogo. In concreto, si tratta di scansionare cinque codici QR in successione, scambiati tra i due partecipanti.



A distanza, questo metodo diventa troppo complesso. Per ovviare a questo problema, Samourai ha sviluppato un protocollo di comunicazione criptato basato su Tor chiamato "Soroban*". Grazie a Soroban, gli scambi necessari per un Payjoin sono automatizzati e avvengono in background.



Queste comunicazioni criptate richiedono una connessione e un'autenticazione tra i partecipanti a Cahoot. Per questo motivo Soroban si affida alle Paynym degli utenti. Se non conoscete ancora il funzionamento di Paynyms, date un'occhiata a questo tutorial dedicato per saperne di più:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

In poche parole, un Paynym è un identificativo unico associato al vostro wallet, che vi permette di attivare diverse funzioni, tra cui gli scambi criptati. Ha la forma di un identificativo accompagnato da un'illustrazione. Ecco, per esempio, quello che utilizzo sul Testnet:



![Image](assets/fr/01.webp)



**Per riassumere:**





- payjoin" = Struttura di transazione collaborativa specifica;





- `Stowaway` = Implementazione Payjoin disponibile su Ashigaru ;





- `Cahoots` = Nome dato dai Samourai a tutti i loro tipi di transazioni collaborative, in particolare il Payjoin `Stowaway`, ripreso oggi su Ashigaru;





- soroban = Protocollo di comunicazione criptato stabilito su Tor che consente la collaborazione con altri utenti in una transazione `Cahoots`;





- paynym" = Identificatore unico wallet utilizzato per stabilire una comunicazione con un altro utente su "Soroban", al fine di effettuare una transazione "Chahoots".



Per uno sguardo più approfondito su come funzionano i Payjoin e sulla loro utilità per la privacy onchain, vi consiglio quest'altro tutorial:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Come si stabilisce una connessione tra Paynyms?



Per iniziare, è ovviamente necessario installare Ashigaru e creare un file :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Per effettuare una transazione remota Cahoots, compreso un PayJoin (*Stowaway*) tramite Ashigaru, è necessario innanzitutto "seguire" l'utente con cui si desidera collaborare, utilizzando il suo Paynym. Nel caso di uno Stowaway, ciò significa seguire la persona a cui si desidera inviare bitcoin. Se non sapete ancora come seguire un altro Paynym, troverete la procedura dettagliata in questo tutorial:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Come faccio a fare un Payjoin su Ashigaru?



Per effettuare una transazione Stowaway, cliccate sull'immagine del vostro Paynym nell'angolo in alto a sinistra dello schermo, quindi aprite il menu "Collabora". La persona che partecipa alla transazione con voi deve fare lo stesso, a meno che non vi scambiate i codici QR di persona.



![Image](assets/fr/02.webp)



Sono disponibili due opzioni: selezionare `Inizia` se si è il mittente del pagamento, oppure `Partecipa` se si è il beneficiario di questo payjoin.



![Image](assets/fr/03.webp)



Se siete il destinatario, la procedura è molto semplice. Per la collaborazione a distanza tramite la rete Soroban, cliccate su `Partecipa`, scegliete il conto che desiderate utilizzare, quindi premete `ASCOLTA RICHIESTE CAUSE` per attendere la richiesta inviata dal pagatore.



![Image](assets/fr/04.webp)



D'altra parte, per la collaborazione di persona tramite la scansione del codice QR, andate sulla home page del vostro wallet, premete l'icona del codice QR nella parte superiore dello schermo, quindi scansionate il codice QR fornito dal pagatore che avvia la transazione.



![Image](assets/fr/05.webp)



Se si ricopre il ruolo di pagatore, cioè di colui che avvia la transazione, andare al menu `Collaborare` e selezionare `Inizia`.



![Image](assets/fr/06.webp)



Per il tipo di transazione, dato che si vuole effettuare un Payjoin Stowaway, scegliere questa opzione.



![Image](assets/fr/07.webp)



È possibile scegliere tra la collaborazione online (*Cahoots* tramite *Soroban*) e la collaborazione faccia a faccia, con scambio di codici QR.



![Image](assets/fr/08.webp)



### Cahoots online



Se avete scelto l'opzione `Online`, selezionate il destinatario tra i Paynyms che state seguendo.



![Image](assets/fr/09.webp)



Cliccare su "Imposta transazione", quindi scegliere il conto dal quale si desidera effettuare la spesa.



![Image](assets/fr/10.webp)



Nella pagina successiva, inserire i dettagli della transazione: l'importo da inviare al destinatario e la tariffa di addebito. Non è necessario inserire un indirizzo di ricezione, poiché il destinatario lo trasmetterà da solo durante gli scambi PSBT.



Quindi fare clic su "Verifica dell'impostazione della transazione".



![Image](assets/fr/11.webp)



Controllate attentamente le informazioni, assicuratevi che il vostro collaboratore ascolti le richieste di *Cahoots*, quindi cliccate sul pulsante verde `BEGIN TRANSACTION` per avviare lo scambio di PSBT tramite Soroban.



![Image](assets/fr/12.webp)



Attendere che entrambi i partecipanti abbiano firmato la transazione, quindi trasmetterla sulla rete Bitcoin.



![Image](assets/fr/13.webp)



### Discussioni faccia a faccia



Se si desidera effettuare il cambio di persona, selezionare il tipo di transazione `STONEWALL X2`, quindi scegliere l'opzione `Di persona/manuale`.



![Image](assets/fr/14.webp)



Cliccare su "Imposta transazione", quindi scegliere il conto dal quale si desidera effettuare la spesa.



![Image](assets/fr/15.webp)



Nella pagina successiva, inserire i dettagli della transazione: l'importo da inviare al destinatario e la tariffa di addebito. Non è necessario inserire un indirizzo di ricezione, poiché il destinatario lo trasmetterà lui stesso durante gli scambi PSBT.



Quindi fare clic su "Verifica dell'impostazione della transazione".



![Image](assets/fr/16.webp)



Controllare i dettagli, quindi premere il pulsante verde "INIZIA LA TRANSAZIONE" per avviare lo scambio di PSBT tramite la scansione del codice QR.



![Image](assets/fr/17.webp)



Lo scambio avviene alternando la scansione con il collaboratore: fate clic su "MOSTRA CODICE QR" per mostrare il vostro codice QR al collaboratore, che lo scansionerà. Egli farà quindi clic su "MOSTRA CODICE QR" per visualizzare il suo, e voi lo scansionerete con "LANCIA QR Scanner". Ripetete questa procedura fino a completare tutte e cinque le fasi dello scambio.



![Image](assets/fr/18.webp)



Una volta completati tutti gli scambi, controllare i dettagli della transazione, quindi rilasciarla trascinando la freccia verde nella parte inferiore dello schermo.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). La sua struttura è la seguente:



![Image](assets/fr/20.webp)



*Credito: [mempool.space](https://mempool.space/)*



Se analizziamo questa transazione, vediamo il mio UTXO di `164.211 sats` sul lato di ingresso, così come il UTXO di `190.002 sats` appartenente all'effettivo destinatario del pagamento. In uscita, ricevo un UTXO di `63.995 sats`, mentre il beneficiario riceve un UTXO di `290.002 sats`. Confrontando le entrate e le uscite, possiamo vedere che il destinatario ha effettivamente guadagnato `100.000 sats`, che corrisponde all'importo del mio pagamento effettivo, e che io ho perso `100.000 sats`, a cui ho aggiunto i costi del mining.



Ovviamente, posso descrivere questa struttura perché ho costruito io stesso la transazione. Ma per un osservatore esterno è generalmente impossibile determinare quali UTXO appartengono a quale partecipante, sia in ingresso che in uscita.



Per approfondire la conoscenza della gestione della privacy onchain su Bitcoin, vi consiglio di seguire il mio corso BTC 204 su Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
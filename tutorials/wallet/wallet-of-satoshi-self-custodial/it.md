---
name: Wallet of Satoshi - Autocustodia
description: Scopri come configurare la modalità di autocustodia di un portafoglio Wallet of Satoshi
---

![cover](assets/cover.webp)



***Non le tue chiavi, non le tue monete* è più di un modo di dire, è un principio fondamentale del Bitcoin, il che significa che se non controlli le **chiavi private** che sbloccano i tuoi bitcoin, non li possiedi veramente.



Molti utenti iniziano generalmente con un wallet **custodiale**, per poi migrare a un wallet **autocustodiale**, dove controllano autonomamente le proprie chiavi private.


In questa esercitazione non vi presenteremo un nuovo wallet autocustode. Vi presenteremo invece una nuova caratteristica dei wallet ***Wallet of Satoshi***: **la modalità autocustodiale**.



L'obiettivo di questa nuova integrazione è quello di consentire agli utenti di mantenere il controllo delle proprie chiavi private, beneficiando al contempo di semplicità e di un'esperienza d'uso fluida.



Prima di entrare nel vivo della questione, esaminiamo per un attimo la speciale modalità di autocustodia offerta da Wallet of Satoshi (WoS).



## La particolarità della modalità di autocustodia



La semplicità e la fluidità della modalità di autocustodia di WoS elimina la complessità di aprire canali Lightning, amministrare nodi... Ma come è possibile?



La modalità di autocustodia del Wallet of Satoshi è alimentata da **Spark**. Si tratta di una soluzione Layer 2 per Bitcoin, creata da Lightspark, che utilizza la tecnologia **statechains**.



Di conseguenza, le transazioni non vengono eseguite direttamente sul Lightning Network. Le interazioni tra la rete **LN** e **Spark** avvengono tramite **scambi atomici**.



Ad esempio, Bob desidera pagare una fattura Lightning utilizzando WoS. Trasferisce i suoi satoshi, ma in background questi vengono indirizzati a uno **Spark Service Provider (SSP)** su Spark, che a sua volta esegue il pagamento sulla rete Lightning.



Al contrario, Alice desidera ottenere fondi direttamente dal suo portafoglio WoS. In questo caso, il **SSP** riceve sats tramite LN e accredita immediatamente il portafoglio di Alice.



Quindi, è importante notare che per beneficiare della semplicità e della fluidità di WoS, è necessario dipendere dai server di Spark. Tuttavia, in termini di sicurezza, se una SSP diventa dannosa o non disponibile, si dispone del meccanismo di **uscita unilaterale**, una misura di sicurezza che consente di recuperare i propri fondi su Bitcoin on-chain (anche se questo può essere lento e costoso), garantendo un'esperienza di auto-custodia paragonabile a quella di un nodo Lightning privato.



Tenendo conto di tutti questi parametri, si può decidere quanto sats si vuole tenere nella propria autocustodia WoS.



Se siete nuovi utenti del Wallet of Satoshi, dovrete naturalmente scaricare l'applicazione mobile wallet. Tuttavia, se la state già utilizzando e volete sapere come usare la **modalità di autocustodia**, andate direttamente alla sezione **Configurazione della modalità di autocustodia** di questa guida.



## Come iniziare con il Wallet of Satoshi



Andate nel vostro negozio di applicazioni e scaricate WoS.



![screen](assets/fr/03.webp)



Una volta completato il download, aprire l'applicazione e premere **Avvio**.



![screen](assets/fr/04.webp)



Verrete reindirizzati all'interfaccia principale dell'applicazione. In realtà, quando si accede a WoS per la prima volta, il portafoglio è già funzionante e si apre sistematicamente in modalità di custodia per impostazione predefinita.



![screen](assets/fr/05.webp)



Anche se non si desidera utilizzare WoS in modalità di custodia, si consiglia di configurarlo prima. Per farlo, consultare questo tutorial.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Passiamo alla configurazione del nostro WoS in autocustodia.



## Configurazione della modalità di autocustodia



Fare clic sul menu hamburger (icona a 3 barre) nell'angolo superiore destro dell'interfaccia principale.



![screen](assets/fr/06.webp)



Quindi, nel menu visualizzato, fare clic sul sottomenu **Aprire l'autotutela Wallet**.



![screen](assets/fr/07.webp)



WoS ti dice immediatamente che *la modalità di autocustodia è accompagnata da una frase di recupero. Inoltre, sei l'unico responsabile della sicurezza dei tuoi fondi*.



![screen](assets/fr/08.webp)



Selezionate il pulsante "**Comprendo**" (1), quindi premete il pulsante **Aprire l'autotutela Wallet** (2), che appare in giallo brillante.



![screen](assets/fr/09.webp)



### Creare un portafoglio di autotutela



Dopo aver fatto clic sul pulsante **Aprire il Wallet di autocustodia**, fare clic sul pulsante **Creare un nuovo Wallet**.



![screen](assets/fr/10.webp)



WoS creerà quindi un portafoglio di autotutela per voi, sempre all'interno della stessa applicazione. Potrete passare dalla modalità **custodiale** (disponibile in alcune regioni) alla modalità **autocustodia** a vostro piacimento e in qualsiasi momento.



![screen](assets/fr/11.webp)



Una volta creato, sarete reindirizzati all'interfaccia principale di WoS self-custody. Noterete che non ci sono differenze tra la panoramica generale e le interfacce di un portafoglio di custodia WoS e quelle di un portafoglio di autodeposito WoS.



### Salvataggio della frase mnemonica



Toccare l'icona **Keychain + Backup Wallet** situata nella parte superiore dello schermo tra il nome del Wallet of Satoshi e il menu hamburger.



![screen](assets/fr/12.webp)



WoS offre due modi diversi per salvare le 12 parole (frase mnemonica): **backup tramite Google Drive** e **backup manuale**.



Anche se suggeriamo il backup manuale, che è il più sicuro, vi mostreremo anche come eseguire il backup tramite Google Drive.



#### Backup tramite Google Drive



Fare clic sul pulsante **Google Drive Backup**.



![screen](assets/fr/13.webp)



Se si opta per il backup con Google Drive, c'è un rischio elevato che il proprio account Google venga compromesso. Un malintenzionato avrebbe accesso al file contenente le vostre 12 parole e potrebbe così ottenere l'accesso al vostro wallet.



L'aggiunta di una password per criptare il file contenente le 12 parole è sicuramente un buon modo per aggiungere un ulteriore livello di sicurezza.



Attivate quindi il pulsante **Cripta con una password** nelle opzioni avanzate.



![screen](assets/fr/14.webp)



Nella nuova interfaccia visualizzata, impostare una password forte e confermarla nuovamente.



![screen](assets/fr/15.webp)



È importante ricordare che una volta scelta la password, non dovete dimenticarla o perdere il supporto su cui l'avete scritta. Se la dimenticate o la perdete, non potrete più accedere alle vostre 12 parole e quindi ai vostri fondi.



Dopo aver scelto la password, selezionare un account Google per il backup, quindi concedere gli accessi richiesti da WoS.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Aspettate qualche secondo. Bingo! Il backup è stato completato con successo.



![screen](assets/fr/18.webp)



È sempre possibile eseguire un backup aggiuntivo scegliendo il secondo metodo di backup: il backup manuale.


#### Backup manuale



Se si opta per il backup manuale, si consiglia vivamente di consultare questo tutorial, che esplora le migliori pratiche per eseguire il backup della frase mnemonica in modo sicuro, in modo da non perdere l'accesso ai propri bitcoin.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Premere il pulsante **Backup manuale**.



![screen](assets/fr/19.webp)



Nell'interfaccia seguente, WoS ricorda alcune precauzioni di sicurezza da prendere in considerazione prima di procedere con il backup manuale.



Attivare il pulsante **Comprendo** e premere il pulsante **Avanti**.



![screen](assets/fr/20.webp)



A questo punto vi verranno presentate le vostre 12 parole. Salvatele, quindi fate clic sul pulsante **Avanti**.



![screen](assets/fr/21.webp)



Su questa nuova interfaccia, premete le parole nell'ordine giusto.



![screen](assets/fr/22.webp)



Infine, fare clic sul pulsante **Avanti**. Congratulazioni! Il backup è ora completo.



![screen](assets/fr/23.webp)



## Ripristino del portafoglio in autocustodia



Quando si desidera recuperare o ripristinare il wallet di autocustodia WoS in seguito a un cambio di telefono o per qualsiasi altro motivo, ecco i passaggi da seguire.



Per aprire il portafoglio WoS, fare clic sul menu ad hamburger nell'angolo superiore destro dell'interfaccia principale.


Nel menu visualizzato, fare clic sul sottomenu **Aprire l'autotutela Wallet**.


Nella nuova interfaccia visualizzata, premere il pulsante **Ripristina Wallet** esistente.



![screen](assets/fr/24.webp)



Scegliete un metodo di ripristino e passate al passo successivo.



![screen](assets/fr/25.webp)



### Ripristino tramite Google Drive



1. Premere il pulsante **Ripristina da Google Drive**.


2. Selezionate un account Google e lasciate che WoS recuperi i dati salvati su Google Drive.


3. Inserite quindi la password di crittografia (se l'avete definita in precedenza, ovviamente) dal file contenente le 12 parole.


4. Attendete qualche istante affinché il ripristino abbia effetto e sarete in grado di accedere nuovamente al vostro portafoglio.



### Restauro manuale



1. Premere il pulsante **Ripristino manuale**.


2. Inserite quindi le 12 parole della vostra frase mnemonica, scrivendo ogni parola davanti al numero iniziale.


3. Attendete qualche istante affinché il ripristino abbia effetto e sarete in grado di accedere nuovamente al vostro portafoglio.




### Trasferimento di bitcoin tra la custodia e l'autodeposito di WoS



Quando avete bitcoin (sats) nel vostro deposito WoS wallet e create un WoS self-custody wallet, non perderete i vostri fondi. Meglio ancora, potete trasferirli al vostro portafoglio di autodeposito e viceversa.



Per fare ciò :


È possibile copiare l'indirizzo di autocustodia WoS lightning o una fattura creata da voi.



![screen](assets/fr/26.webp)



Ora aprite la vostra custodia wallet e premete il pulsante **Envoyer**.



Quindi incollare l'indirizzo o la fattura. Premere **Envoyer** una seconda volta.



Tornate al vostro portafoglio di autocustodia e vedrete che avete effettivamente ricevuto i fondi.



![screen](assets/fr/27.webp)



## Inviare e ricevere bitcoin



Per quanto riguarda l'invio e la ricezione di bitcoin in modalità self-custody, proprio come la panoramica generale e le interfacce, non sono diversi dall'invio e dalla ricezione di bitcoin attraverso un WoS custody wallet.



Consultare il tutorial di base sull'uso del Wallet of Satoshi sulla rete Plan₿.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Ora è possibile configurare e far funzionare Wallet of Satoshi da soli in modalità di autocustodia.



Se questo tutorial vi è stato utile, lasciatemi un pollice verde qui sotto. Grazie mille!
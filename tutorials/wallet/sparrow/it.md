---
name: Sparrow Wallet
description: Installazione, configurazione e utilizzo di Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet è un software di gestione del portafoglio Bitcoin autocustodito sviluppato da Craig Raw. Questo software open-source è apprezzato dai bitcoiners per le sue numerose funzioni e per l'intuitività dell'interfaccia.

Esistono due modi per utilizzare Sparrow:


- Come un Hot Wallet, dove le chiavi private sono memorizzate sul PC.
- Come gestore di un Cold Wallet, in cui le chiavi private sono conservate in un Hardware Wallet. In questa modalità, Sparrow gestisce solo le informazioni pubbliche del Wallet, tiene traccia dei fondi, genera indirizzi e crea transazioni, ma la firma dell'Hardware Wallet è necessaria per rendere valide queste transazioni. Può quindi sostituire applicazioni come Ledger Live o Trezor Suite.

Sparrow supporta Wallet a firma singola e multipla e consente una gestione fluida di più Wallet. Ad esempio, è possibile controllare simultaneamente un Wallet collegato a un Ledger, un altro a un Trezor e anche un Hot Wallet.

Il software offre anche funzioni avanzate di controllo delle monete, consentendo di scegliere con precisione quali UTXO utilizzare nelle transazioni per ottimizzare la riservatezza.

In termini di connessione, Sparrow consente di collegarsi al proprio nodo Bitcoin, sia in remoto tramite un server Electrum, sia con Bitcoin Core. È anche possibile utilizzare un nodo pubblico se non hai ancora il proprio. Le connessioni remote vengono effettuate tramite Tor.

## Installare Sparrow Wallet

Vai sulla [pagina ufficiale per il download di Sparrow Wallet](https://sparrowwallet.com/download/) e scegli la versione del software corrispondente al tuo sistema operativo.

![Image](assets/fr/01.webp)

È importante verificare l'integrità e l'autenticità del software prima di installarlo. Se non sai come fare, qui trovi un tutorial completo:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Una volta installato Sparrow, puoi saltare le schermate esplicative iniziali e passare direttamente alla schermata di gestione della connessione.

![Image](assets/fr/02.webp)

## Collegamento alla rete Bitcoin

Per interagire con la rete Bitcoin e trasmettere le tue transazioni, Sparrow deve essere connesso a un nodo Bitcoin. Esistono tre modi principali per stabilire questa connessione:


- 🟡 Utilizzando un nodo pubblico, cioè collegandosi a un nodo di terze parti che consente tali connessioni. Se non disponi di un tuo nodo Bitcoin, questa opzione consente di iniziare rapidamente a utilizzare Sparrow. Tuttavia, il nodo a cui ti connetti vedrà tutte le tue transazioni, il che potrebbe compromettere la tua riservatezza. Avere il controllo sulle tue chiavi è essenziale, ma avere un tuo nodo è ancora meglio. Utilizza quindi questa opzione solo se sei agli inizi, consapevole dei rischi per la tua privacy.
- 🟢 Connessione a un nodo Bitcoin Core. Se disponi di un nodo Bitcoin Core, puoi collegarlo a Sparrow Wallet, sia localmente se Bitcoin Core è installato sulla stessa macchina, sia in remoto.
- 🔵 Connessione tramite un server Electrum. Se il nodo Bitcoin è dotato di Electrum, come nel caso di soluzioni node-in-a-box come Umbrel o Start9, è possibile collegarsi ad esso in remoto da Sparrow.

**È preferibile utilizzare una connessione tramite Electrs o Bitcoin Core sul tuo nodo per ridurre la necessità di affidarsi a terzi e migliorare la tua privacy**

### Connettersi ad un nodo pubblico 🟡

La connessione a un nodo pubblico è molto semplice. Fai clic sulla scheda "*Public Server*".

![Image](assets/fr/03.webp)

Seleziona un nodo dall'elenco a discesa.

![Image](assets/fr/04.webp)

Quindi fai clic su "*Test Connection*".

![Image](assets/fr/05.webp)

Una volta collegato, Sparrow Wallet ti mostrerà un segno di spunta giallo nell'angolo inferiore destro dell'interfaccia per indicare che sei connesso a un nodo pubblico.

![Image](assets/fr/06.webp)

### Collegamento a Bitcoin Core 🟢

Il secondo metodo di connessione a un nodo Bitcoin consiste nel collegare Sparrow a un Bitcoin Core. Se Bitcoin Core è installato sulla stessa macchina, l'autenticazione avverrà tramite il file cookie. Se Bitcoin Core si trova su una macchina remota, dovrai utilizzare la password definita nel file `Bitcoin.conf`.

Nota che se utilizzi un nodo Bitcoin Core Light (con installazione parziale), non potrai ripristinare un Wallet contenente transazioni precedenti ai blocchi memorizzati localmente. Tuttavia, per un nuovo Wallet creato su Sparrow, questo non sarà un problema: le nuove transazioni saranno visibili, anche se il nodo è Light.

Per configurare un nodo Bitcoin Core, puoi consultare una delle seguenti esercitazioni, a seconda del sistema operativo in uso:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Su Sparrow, vai alla scheda "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Con Bitcoin Core locale:**

Se sul computer è installato Bitcoin Core, individuare il file `Bitcoin.conf` tra i file del software. Se questo file non esiste, è possibile crearlo. Aprilo con un editor di testo e inserisci la seguente riga:

```ini
server=1
```

Quindi salva le modifiche.

Puoi farlo anche tramite l'interfaccia grafica di Bitcoin-QT, andando su "*Settings*" > "*Options...*" e attivando l'opzione "*Enable RPC server*".

Non dimentica di riavviare il software dopo aver apportato queste modifiche.

![Image](assets/fr/08.webp)

Torna quindi su Sparrow e inserisci il percorso del file cookie, solitamente situato nella stessa cartella di `Bitcoin.conf`, a seconda del sistema operativo:

| **macOS** | ~/Libreria/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Lascia gli altri parametri come predefiniti, URL `127.0.0.1` e porta `8332`, quindi fai clic su "*Test Connection*".

![Image](assets/fr/10.webp)

La connessione è stabilita. Nell'angolo in basso a destra apparirà un segno di spunta verde per indicare che sei connesso a un nodo Bitcoin Core.

![Image](assets/fr/11.webp)

**Con Bitcoin Core remoto:**

Se Bitcoin Core è installato su un'altra macchina collegata alla stessa rete, individua innanzitutto il file `Bitcoin.conf` tra i file del software. Se questo file non esiste ancora, puoi crearlo. Apri questo file con un editor di testo e aggiungere la seguente riga:

```ini
server=1
```

Dopo aver modificato il file, assicurati di salvarlo nella cartella appropriata per il tuo sistema operativo:

| **macOS** | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

Questa operazione può essere eseguita anche tramite l'interfaccia grafica Bitcoin-QT. Accedi al menu "*Settings*", poi "*Options...*" e attiva l'opzione "*Enable RPC server*" selezionando la casella corrispondente. Se il file `Bitcoin.conf` non esiste, puoi crearlo direttamente da questa schermata facendo clic su "*Apri file di configurazione*".

![Image](assets/fr/12.webp)

Trova l'IP Address della macchina che ospita Bitcoin Core sulla rete locale. Per farlo, puoi usare uno strumento come [Angry IP Scanner](https://angryip.org/). Supponiamo, per esempio, che l'IP Address del tuo nodo sia `192.168.1.18`.

Nel file `Bitcoin.conf`, aggiungi le seguenti righe, impostando `rpcbind=192.168.1.18` in modo che corrisponda all'IP Address del nodo.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

Nel file `Bitcoin.conf`, aggiungi un nome utente e una password per le connessioni remote. Assicurati di sostituire `loic` con il tuo nome utente e `my_password` con una password forte:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Dopo aver modificato e salvato il file, riavvia il software Bitcoin-QT.

Ora puoi tornare a Sparrow Wallet. Vai sulla scheda "*User / Pass*". Inserisci il nome utente e la password configurati nel file `Bitcoin.conf`. Lascia gli altri parametri come predefiniti, ossia l'URL `127.0.0.1` e la porta `8332`. Quindi fai clic su "*Test Connection*".

![Image](assets/fr/15.webp)

La connessione è stabilita. Nell'angolo in basso a destra apparirà un segno di spunta verde per indicare che sei connesso a un nodo Bitcoin Core.

![Image](assets/fr/16.webp)

### Connettersi a un server Electrum 🔵

L'ultima opzione di connessione è l'utilizzo di un server Electrum remoto. Questo metodo consente di connettersi al proprio nodo via Tor da un altro dispositivo e di sfruttare un indicizzatore per sfogliare più rapidamente i portafogli su Sparrow. È particolarmente indicato se disponi di una soluzione node-in-a-box come Umbrel o Start9, che consentono di installare Electrum con un solo clic.

Per farlo, procurati il Tor `.onion' Address del tuo server Electrum. Con Umbrel, ad esempio, lo trovi nell'applicazione Electrs.

![Image](assets/fr/17.webp)

Su Sparrow Wallet, accedi alla scheda "*Private Electrum*".

![Image](assets/fr/18.webp)

Inserisci il tuo indirizzo Tor nell'apposito spazio. Le altre impostazioni possono rimanere predefinite. Quindi fai clic su "*Test Connection*".

![Image](assets/fr/19.webp)

La connessione è confermata. Se chiudi questa finestra, nell'angolo in basso a destra appare un segno di spunta blu che indica che sei connesso a un server Electrum.

![Image](assets/fr/20.webp)

## Creare un Hot Wallet

Ora che Sparrow Wallet è configurato per comunicare con la rete Bitcoin, sei pronto a creare il tuo primo Wallet. Questa sezione ti guida nella creazione di un Hot Wallet, ovvero un Wallet le cui chiavi private sono memorizzate sul tuo computer. Poiché il computer è una macchina complessa connessa a Internet, presenta una superficie di attacco molto ampia. Di conseguenza, un Hot Wallet dovrebbe essere utilizzato solo per quantità limitate di bitcoin. Per conservare quantità maggiori, opta per un Wallet sicuro con un Hardware Wallet. Se questo è ciò che stai cercando, puoi passare alla sezione successiva.

Per creare un Hot Wallet, dalla schermata iniziale di Sparrow Wallet, fai clic sulla scheda "*File*" e quindi su "*New Wallet*".

![Image](assets/fr/21.webp)

Inserisci un nome per il portafoglio e clicca su "*Create Wallet*".

![Image](assets/fr/22.webp)

Nella parte superiore della schermata puoi scegliere se creare un portafoglio "*Single Signature*" o "*Multi Signature*". Subito sotto, seleziona il tipo di script per bloccare i tuoi UTXO. Ti consiglio di utilizzare lo standard più recente: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Quindi fai clic su "*New or Imported Software Wallet*".

![Image](assets/fr/24.webp)

Scegli lo standard BIP39, in quanto è supportato da quasi tutti i software del portafoglio Bitcoin. Scegli quindi la lunghezza della frase di recupero. Attualmente è sufficiente una frase di 12 parole, poiché entrambe offrono una sicurezza simile, ma la frase di 12 parole è più semplice da salvare.

![Image](assets/fr/25.webp)

Fai clic sul pulsante "*generate New*" per inserire la frase generata del proprio Wallet. Questa frase dà accesso completo e illimitato a tutti i tuoi bitcoin. Chiunque sia in possesso di questa frase può rubare i tuoi fondi, anche senza accedere fisicamente al tuo computer.

La frase di 12 parole ripristina l'accesso ai bitcoin in caso di perdita, furto o rottura del computer. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.

È possibile inciderlo su carta o, per maggiore sicurezza, inciderlo su acciaio inossidabile per proteggerlo da incendi, inondazioni o crolli. La scelta del supporto per la frase Mnemonic dipenderà dalla tua strategia di sicurezza, ma se stai usando Sparrow come Wallet per le spese quotidiane con quantità moderate di bitcoin, la carta dovrebbe essere sufficiente.

Per ulteriori informazioni sul modo corretto di salvare e gestire la frase Mnemonic, ti consiglio di seguire quest'altra guida, soprattutto se sei principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
![Image](assets/fr/26.webp)

**Ovviamente, non devi mai condividere queste parole su Internet, come faccio io in questa esercitazione. Questo esempio di Wallet sarà utilizzato solo sul Testnet e sarà cancellato alla fine del tutorial.**

Puoi anche scegliere di aggiungere una passphrase BIP39 facendo clic sulla casella "*Use passphrase*". Attenzione: l'uso di una passphrase può essere molto utile, ma se non si capisce come funziona, può essere molto rischioso. Per questo motivo ti consiglio vivamente di leggere questo breve articolo teorico sull'argomento:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Dopo aver salvato la frase Mnemonic e qualsiasi passphrase su un supporto fisico, fai clic su "*Confirm Backup*".

![Image](assets/fr/27.webp)

Reinserisci le 12 parole per confermare che sono state salvate correttamente, quindi fai clic su "*Create Keystore*".

![Image](assets/fr/28.webp)

Quindi fai clic su "*Import Keystore*" per importare le chiavi del portafoglio dalla frase Mnemonic.

![Image](assets/fr/29.webp)

Clicca su "*Apply*" per finalizzare la creazione del wallet.

![Image](assets/fr/30.webp)

Imposta una password forte per proteggere l'accesso al tuo wallet Sparrow. È buona norma conservare questa password in un gestore di password, in modo da non dimenticarla. Nota che questa password non deriva dalle tue chiavi private. Viene utilizzata solo per accedere al tuo Wallet tramite Sparrow Wallet. Quindi, anche senza questa password, la frase Mnemonic sarà sufficiente per accedere ai bitcoin da qualsiasi applicazione compatibile con BIP39.

![Image](assets/fr/31.webp)

Il tuo Hot Wallet è ora creato. Puoi passare alla sezione *Receiving Bitcoins* di questa esercitazione se non intendi utilizzare un Hardware Wallet con Sparrow.

## Gestione di un Cold Wallet

Il secondo modo di utilizzare Sparrow Wallet è di configurarlo come gestore di un wallet con un Hardware Wallet. In questa configurazione, le chiavi private del Wallet Bitcoin rimangono esclusivamente sull'Hardware Wallet, mentre Sparrow accede solo alle informazioni pubbliche. Questo approccio offre un livello di sicurezza più elevato rispetto agli Hot Wallet discussi in precedenza. Questo perchè le chiavi private sono conservate su un dispositivo specializzato, spesso dotato di un chip sicuro (Secure Element), che non è connesso a Internet e presenta quindi una superficie di attacco molto più ridotta rispetto a un computer tradizionale.

Esistono due modi principali per collegare l'Hardware Wallet a Sparrow:


- Con cavo, comunemente utilizzato con modelli entry-level come Trezor Safe 3 o Ledger Nano S Plus;
- In modalità Air-Gap, cioè senza una connessione diretta via cavo, tramite una scheda MicroSD o il codice QR.

Sparrow supporta tutti questi metodi di comunicazione ed è compatibile con la maggior parte degli Hardware Wallet presenti sul mercato.

Per questa esercitazione, utilizzerò un Ledger Nano S con cavo, ma la procedura è simile in modalità Air-Gap, ovvero senza cavo. Trovi i dettagli specifici per il tuo Hardware Wallet nel tutorial dedicato al Plan ₿ Network.

Prima di iniziare, accertati che il Wallet sia già configurato sull'Hardware Wallet. Se utilizzi una connessione via cavo, collegalo al computer tramite il cavo.

Per importare il cosiddetto "*Keystore*" (le informazioni pubbliche necessarie per gestire il Wallet) in Sparrow Wallet, fai clic sulla scheda "*File*", quindi su "*New Wallet*".

![Image](assets/fr/32.webp)

Assegna un nome al Wallet e fai clic su "*Create Wallet*". Ti consiglio di inserire il nome del tuo Hardware Wallet per identificarlo facilmente in seguito.

![Image](assets/fr/33.webp)

Nella parte superiore della schermata, scegli tra un Wallet "*Single Signature*" o "*Multi Signature*". Per il nostro esempio, configureremo un portafoglio a firma singola.

In basso, seleziona il tipo di script per bloccare gli UTXO. Se il tuo Hardware Wallet lo supporta, ti suggerisco di scegliere "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

Successivamente, la procedura varia a seconda del metodo di connessione utilizzato. Se utilizzi un metodo Air-Gap, seleziona "*Airgapped Hardware Wallet*". Segui quindi le istruzioni specifiche del dispositivo.

![Image](assets/fr/35.webp)

Se utilizzi una connessione via cavo, come nel mio caso, scegli "*Connected Hardware Wallet*".

![Image](assets/fr/36.webp)

Fai clic su "*Scan*" per far rilevare a Sparrow il tuo dispositivo. Assicurati che sia collegato e sbloccato. Per alcuni modelli, come il Ledger, è necessario aprire l'applicazione "*Bitcoin*" per abilitare il rilevamento.

![Image](assets/fr/37.webp)

Seleziona "*Import Keystore*".

![Image](assets/fr/38.webp)

Clicca su "*Apply*" per finalizzare la creazione del wallet.

![Image](assets/fr/39.webp)

Imposta una password forte per proteggere l'accesso al tuo Sparrow. Questa password proteggerà le chiavi pubbliche, gli indirizzi e la cronologia delle transazioni. Ti consiglio di salvarla in un gestore di password. Nota che questa password non deriva dalle chiavi private. Anche senza di essa, puoi recuperare l'accesso ai bitcoin con frase Mnemonic tramite qualsiasi software compatibile con BIP39.

![Image](assets/fr/40.webp)

Il Wallet di gestione è ora configurato su Sparrow.

![Image](assets/fr/41.webp)

## Ricevere Bitcoin

Ora che il Wallet è impostato su Sparrow, puoi ricevere bitcoin. È sufficiente accedere al menu "*Receive*".

![Image](assets/fr/42.webp)

Sparrow visualizzerà il primo Address inutilizzato nel tuo Wallet. Puoi aggiungere una "*Etichetta*" (Label) a questo Address per ricordare l'origine di questi satoshi in futuro.

![Image](assets/fr/43.webp)

Se utilizzi un Hot Wallet, l'Address visualizzato può essere utilizzato immediatamente, copiandolo o scansionando il codice QR associato.

Se utilizzi un Hardware Wallet, è molto importante controllare l'Address sullo schermo del dispositivo prima di utilizzarlo. Per i dispositivi cablati, collega e sblocca l'Hardware Wallet, quindi su Sparrow clicca su "*Display Address*". Assicurati che l'Address visualizzato sull'Hardware Wallet corrisponda a quello visualizzato su Sparrow.

![Image](assets/fr/44.webp)

Per gli utenti di Hardware Wallet Air-Gap, la verifica dell'Address varia a seconda del tipo di modello del dispositivo. Per istruzioni precise, consulta l'esercitazione dedicata al Plan ₿ Network.

Una volta che la transazione è stata trasmessa dal pagatore, la si vedrà apparire nella scheda "*Transactions*". Puoi fare clic su di essa per ottenere ulteriori dettagli, ad esempio il txid.

![Image](assets/fr/45.webp)

Nella scheda "*Addresses*" trovi un elenco di tutti gli indirizzi della posta in arrivo. Puoi vedere se sono già stati utilizzati e se è stata aggiunta un'etichetta. "*Gli indirizzi di ricezione*" sono quelli che Sparrow mostra quando fai clic su "*Receive*" e sono destinati ai pagamenti in arrivo. Gli indirizzi "*Change*" sono utilizzati per i resti nelle transazioni, cioè per recuperare la parte inutilizzata dei tuoi UTXO in entrata.

![Image](assets/fr/46.webp)

La scheda "*UTXOs*" mostra tutti i tuoi UTXOs, cioè i frammenti bitcoin in tuo possesso. Puoi vedere la quantità di ogni UTXO e l'etichetta associata.

![Image](assets/fr/47.webp)

## Inviare bitcoin

Ora che hai qualche satoshi nel tuo Wallet, hai anche la possibilità di inviarne qualcuno. Anche se ci sono diversi modi per farlo, ti consiglio di usare il menu "*UTXOs*" per avere un controllo più preciso sulle monete spese (*coin control*), piuttosto che andare direttamente al menu "*Send*" (anche se quest'ultimo può essere sufficiente se sei principianti).

![Image](assets/fr/48.webp)

Seleziona gli UTXO che desideri utilizzare come input per questa transazione, quindi fai clic su "*Send Selected*". Questo approccio consente di selezionare le fonti più appropriate tra gli UTXO, in base alle spese e alle etichette applicate al momento della ricezione, al fine di ottimizzare la riservatezza dei pagamenti. Assicurati che la somma degli UTXO selezionati sia superiore all'importo che desideri inviare.

![Image](assets/fr/49.webp)

Inserisci l'Address del destinatario nel campo "*Pay to*". Puoi anche scansionare l'Address con la webcam facendo clic sull'icona della fotocamera. Il pulsante "*+Add*" consente di pagare più indirizzi in un'unica transazione.

![Image](assets/fr/50.webp)

Aggiungi un'etichetta alla tua transazione per ricordarti da dove proviene. Questa etichetta sarà anche associata al tuo eventuale resto.

![Image](assets/fr/51.webp)

Inserisci l'importo da inviare a questo Address.

![Image](assets/fr/52.webp)

Regola la fee in base alle attuali condizioni di mercato. Puoi farlo inserendo un valore assoluto della fee o regolando la fee con il cursore.

![Image](assets/fr/53.webp)

Nella parte inferiore della schermata puoi scegliere tra "*Efficiency*" e "*Privacy*". Nel mio caso, l'opzione "*Privacy*" non è disponibile, poiché ho solo un UTXO in questo wallet. "*Efficiency*" corrisponde a una transazione classica, mentre "*Privacy*" è una transazione di tipo Stonewall: una struttura di transazione che rafforza la tua riservatezza simulando un mini-[CoinJoin](https://planb.network/resources/glossary/coinjoin), il che rende più complessa l'analisi della catena.

![Image](assets/fr/54.webp)

Sparrow ti mostra un diagramma riassuntivo che evidenzia gli input, gli output e le commissioni di transazione (nota che le commissioni non sono in realtà un output, contrariamente a quanto suggerisce il diagramma). Se sei soddisfatti di tutto, fai clic su "*Create Transaction*".

![Image](assets/fr/55.webp)

In questo modo accedi a una pagina con tutti i dettagli della transazione. Verifica che tutte le informazioni siano corrette, quindi fai clic su "*Finalize Transaction for Signing*".

![Image](assets/fr/56.webp)

È importante mantenere il Sighash di default. Per capire perché, dai un'occhiata a questo corso di formazione, in cui ti spiego tutto quello che c'è da sapere su Sighash:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Nella schermata successiva, le opzioni variano a seconda del tipo di Wallet in uso:


- Per un Hardware Wallet Air-Gap, fai clic su "*Show QR*" per visualizzare un PSBT che è possibile firmare con il tuo dispositivo, quindi carica il PSBT firmato su Sparrow utilizzando "*Scan QR*". L'opzione "*Save transaction*" funziona in modo simile, ma con scambi su microSD;
- Per un Hot Wallet, è sufficiente fare clic su "*Sign*" e inserire la password del Wallet per firmare;
- Per un Hardware Wallet cablato, fai clic anche su "*Sign*" per inviare la transazione non firmata al dispositivo.

![Image](assets/fr/57.webp)

Sul proprio Hardware Wallet, controlla l'Address del destinatario, l'importo inviato e le fees. Se tutto è corretto, procedi con la firma.

Una volta firmata, la transazione riapparirà su Sparrow, pronta per essere trasmessa sulla rete Bitcoin e successivamente inserita in un blocco. Se tutto è corretto, fai clic su "*Broadcast Transaction*".

![Image](assets/fr/58.webp)

La transazione è ora trasmessa e in attesa di conferma.

![Image](assets/fr/59.webp)

## Gestione e configurazione dei Wallet su Sparrow

Nella scheda "*Settings*" si trovano informazioni dettagliate sul Wallet, come :


- Tipo di Wallet (single-sig o multi-sig);
- Tipo di script utilizzato;
- Il nome assegnato al Wallet;
- Impronta della chiave master;
- Il percorso di bypass;
- La chiave pubblica estesa dell'account.

![Image](assets/fr/60.webp)

Il pulsante "*Export*" consente di esportare le informazioni del Wallet in modo da poterle utilizzare in altri software mantenendo le informazioni impostate in Sparrow.

Il pulsante "*Add account*" consente di aggiungere un altro account al Wallet. Un account corrisponde a un insieme separato di indirizzi di posta elettronica. Questa funzione può essere utile, ad esempio, se desideri separare un account personale da uno aziendale, con una singola frase Mnemonic.

Il pulsante "*Advanced*" consente di accedere alle impostazioni avanzate, come la personalizzazione della ricerca Address di Sparrow e la modifica della password del Wallet.

![Image](assets/fr/61.webp)

Quando chiudi Sparrow, il Wallet si blocca automaticamente. Alla successiva apertura del software, una finestra chiederà di sbloccare il Wallet con la password.

![Image](assets/fr/62.webp)

Se questa finestra non si apre o se desideri aprire un altro Wallet su Sparrow, fai clic sulla scheda "*File*" e seleziona "*Open Wallet*".

![Image](assets/fr/63.webp)

In questo modo si aprirà il File Manager nella cartella in cui Sparrow memorizza i Wallet. È sufficiente selezionare il Wallet che desideri aprire e inserire la password per sbloccarlo.

![Image](assets/fr/64.webp)

Nel menu "*File*", alla voce "*Settings*", si trovano i parametri di connessione alla rete Bitcoin già esplorati nelle sezioni precedenti. Puoi inoltre regolare vari parametri come l'unità di misura utilizzata, la valuta fiat per le conversioni e le fonti di informazione.

![Image](assets/fr/65.webp)

La scheda "*View*" offre opzioni di personalizzazione e l'accesso ad alcuni comandi utili, come "*Refresh Wallet*", che aggiorna la ricerca delle transazioni per il Wallet.

![Image](assets/fr/66.webp)

La scheda "*Tools*" raggruppa diversi strumenti avanzati, tra cui :


- "*Sign/Verify message*" consente di dimostrare il possesso di un Address ricevente o di verificare una firma.
- "*Send To Many*" offre una interfaccia semplificata per l'esecuzione di transazioni a più indirizzi di ricezione contemporaneamente, comodo per le spese in batch.
- "*Sweep Private Key*" consente di recuperare i bitcoin protetti da una semplice chiave privata e di trasferirli al proprio Sparrow. Questo può essere particolarmente utile per chi possiede bitcoin risalenti ai primi anni 2010, prima dell'era dei portafogli HD.
- "Verify Download" verifica l'integrità e l'autenticità del software scaricato prima di installarlo sul dispositivo.
- "*Restart In*" consente di passare ai Wallet sulle reti Testnet o Signet. Questo può essere utile se desideri accedere a reti di prova con monete di nessun valore reale.

![Image](assets/fr/67.webp)

Ora sai tutto sul software Sparrow, uno strumento eccellente per la gestione quotidiana dei Wallet Bitcoin.

Se questa esercitazione è stata utile, ti sarei molto grato se lasciassi un pollice verde qui sotto. Sentiteti libero di condividerlo sui tuoi social network. Grazie mille!

Ti consiglio anche quest'altro tutorial in cui spiego come configurare l'Hardware Walle COLDCARD Q con Sparrow:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

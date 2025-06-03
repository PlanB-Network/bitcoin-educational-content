---
name: Passero Wallet
description: Installazione, configurazione e utilizzo di Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet è un software di gestione del portafoglio Bitcoin autocustodito sviluppato da Craig Raw. Questo software open-source è apprezzato dai bitcoiners per le sue numerose funzioni e per l'intuitività del Interface.

Esistono due modi per utilizzare Sparrow:


- Come un Hot Wallet, dove le chiavi private sono memorizzate sul PC.
- Come gestore di Cold Wallet, in cui le chiavi private sono conservate in un Hardware Wallet. In questa modalità, Sparrow manipola solo le informazioni pubbliche Wallet, tiene traccia dei fondi, genera indirizzi e crea transazioni, ma la firma Hardware Wallet è necessaria per rendere valide queste transazioni. Può quindi sostituire applicazioni come Ledger Live o Trezor Suite.

Sparrow supporta portafogli a firma singola e multipla e consente una gestione fluida di più portafogli. Ad esempio, è possibile controllare simultaneamente un Wallet collegato a un Ledger, un altro a un Trezor e anche un Hot Wallet.

Il software offre anche funzioni avanzate di controllo delle monete, consentendo di scegliere con precisione quali UTXO utilizzare nelle transazioni per ottimizzare la riservatezza.

In termini di connessione, Sparrow consente di collegarsi al proprio nodo Bitcoin, sia in remoto tramite un server Electrum, sia con Bitcoin Core. È anche possibile utilizzare un nodo pubblico se non si ha ancora il proprio. Le connessioni remote vengono effettuate tramite Tor.

## Installare Sparrow Wallet

Andare alla [pagina ufficiale di download di Sparrow Wallet] (https://sparrowwallet.com/download/) e scegliere la versione del software corrispondente al proprio sistema operativo.

![Image](assets/fr/01.webp)

È importante verificare l'integrità e l'autenticità del software prima di installarlo. Se non sapete come fare, qui troverete un tutorial completo:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Una volta installato Sparrow, è possibile saltare le schermate esplicative iniziali e passare direttamente alla schermata di gestione della connessione.

![Image](assets/fr/02.webp)

## Collegamento alla rete Bitcoin

Per interagire con la rete Bitcoin e trasmettere le proprie transazioni, Sparrow deve essere connesso a un nodo Bitcoin. Esistono tre modi principali per stabilire questa connessione:


- 🟡 Utilizzando un nodo pubblico, cioè collegandosi a un nodo di terze parti che consente tali connessioni. Se non si dispone di un proprio nodo Bitcoin, questa opzione consente di iniziare rapidamente a utilizzare Sparrow. Tuttavia, il nodo a cui vi connettete vedrà tutte le vostre transazioni, il che potrebbe compromettere la vostra riservatezza. Avere il controllo sulle proprie chiavi è essenziale, ma avere un proprio nodo è ancora meglio. Utilizzate quindi questa opzione solo se siete agli inizi, consapevoli dei rischi per la vostra privacy.
- 🟢 Connessione a un nodo Bitcoin Core. Se si dispone di un nodo Bitcoin Core, è possibile collegarlo a Sparrow Wallet, sia localmente se Bitcoin Core è installato sulla stessa macchina, sia in remoto.
- 🔵 Connessione tramite un server Electrum. Se il nodo Bitcoin è dotato di Electrum, come nel caso di soluzioni node-in-a-box come Umbrel o Start9, è possibile collegarsi ad esso in remoto da Sparrow.

**È preferibile utilizzare una connessione tramite Electrs o Bitcoin Core sul proprio nodo per ridurre la necessità di affidarsi a terzi e ottimizzare la propria riservatezza**

### Connettersi ad un nodo pubblico 🟡

La connessione a un nodo pubblico è molto semplice. Fare clic sulla scheda "*Server pubblico*".

![Image](assets/fr/03.webp)

Selezionare un nodo dall'elenco a discesa.

![Image](assets/fr/04.webp)

Quindi fare clic su "*Test Connection*".

![Image](assets/fr/05.webp)

Una volta collegato, Sparrow Wallet visualizzerà un segno di spunta giallo nell'angolo inferiore destro di Interface per indicare che si è connessi a un nodo pubblico.

![Image](assets/fr/06.webp)

### Collegamento a un nucleo Bitcoin 🟢

Il secondo metodo di connessione a un nodo Bitcoin consiste nel collegare Sparrow a un Bitcoin Core. Se il Bitcoin Core è installato sulla stessa macchina, l'autenticazione avverrà tramite il file cookie. Se Bitcoin Core si trova su una macchina remota, è necessario utilizzare la password definita nel file `Bitcoin.conf`.

Si noti che se si utilizza un nodo Bitcoin Core potato, non sarà possibile ripristinare un Wallet contenente transazioni precedenti ai blocchi memorizzati localmente. Tuttavia, per un nuovo Wallet creato su Sparrow, questo non sarà un problema: le nuove transazioni saranno visibili, anche se il nodo è stato tagliato.

Per configurare un nodo Bitcoin Core, è possibile consultare una delle seguenti esercitazioni, a seconda del sistema operativo in uso:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Su Sparrow, andare alla scheda "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Con Bitcoin Core locale:**

Se sul computer è installato Bitcoin Core, individuare il file `Bitcoin.conf` tra i file del software. Se questo file non esiste, è possibile crearlo. Aprirlo con un editor di testo e inserire la seguente riga:

```ini
server=1
```

Quindi salvare le modifiche.

È possibile farlo anche tramite la grafica Interface di Bitcoin-QT, andando su "*Impostazioni*" > "*Opzioni...*" e attivando l'opzione "*Abilita server RPC*" > "*Opzioni...*" e attivando l'opzione "*Abilita server RPC*".

Non dimenticate di riavviare il software dopo aver apportato queste modifiche.

![Image](assets/fr/08.webp)

Tornare quindi a Sparrow Wallet e inserire il percorso del file cookie, solitamente situato nella stessa cartella di `Bitcoin.conf`, a seconda del sistema operativo:

| **macOS** | ~/Libreria/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Lasciare gli altri parametri come predefiniti, URL `127.0.0.1` e porta `8332`, quindi fare clic su "*Test Connection*".

![Image](assets/fr/10.webp)

La connessione è stabilita. Nell'angolo in basso a destra apparirà un segno di spunta Green per indicare che si è connessi a un nodo Bitcoin Core.

![Image](assets/fr/11.webp)

**Con il nucleo Bitcoin remoto:**

Se Bitcoin Core è installato su un'altra macchina collegata alla stessa rete, individuare innanzitutto il file `Bitcoin.conf` tra i file del software. Se questo file non esiste ancora, è possibile crearlo. Aprire questo file con un editor di testo e aggiungere la seguente riga:

```ini
server=1
```

Dopo aver modificato il file, assicuratevi di salvarlo nella cartella appropriata per il vostro sistema operativo:

| **macOS** | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

Questa operazione può essere eseguita anche tramite il Bitcoin-QT Interface grafico. Accedere al menu "*Impostazioni*", poi "*Opzioni...*" e attivare l'opzione "*Abilita server RPC*" selezionando la casella corrispondente. Se il file `Bitcoin.conf` non esiste, è possibile crearlo direttamente da questo Interface facendo clic su "*Apri file di configurazione*".

![Image](assets/fr/12.webp)

Trovare l'IP Address della macchina che ospita Bitcoin Core sulla rete locale. Per farlo, si può usare uno strumento come [Angry IP Scanner](https://angryip.org/). Supponiamo, per amor di discussione, che l'IP Address del vostro nodo sia `192.168.1.18`.

Nel file `Bitcoin.conf`, aggiungere le seguenti righe, impostando `rpcbind=192.168.1.18` in modo che corrisponda all'IP Address del nodo.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

Nel file `Bitcoin.conf`, aggiungere un nome utente e una password per le connessioni remote. Assicurarsi di sostituire `loic` con il proprio nome utente e `my_password` con una password forte:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Dopo aver modificato e salvato il file, riavviare il software Bitcoin-QT.

Ora è possibile tornare a Sparrow Wallet. Andare alla scheda "*User / Pass*". Inserire il nome utente e la password configurati nel file `Bitcoin.conf`. Lasciare gli altri parametri come predefiniti, ossia l'URL `127.0.0.1` e la porta `8332`. Quindi fare clic su "*Test Connection*".

![Image](assets/fr/15.webp)

La connessione è stabilita. Nell'angolo in basso a destra apparirà un segno di spunta Green per indicare che si è connessi a un nodo Bitcoin Core.

![Image](assets/fr/16.webp)

### Connettersi a un server Electrum 🔵

L'ultima opzione di connessione è l'utilizzo di un server Electrum remoto. Questo metodo consente di connettersi al proprio nodo via Tor da un altro dispositivo e di sfruttare un indicizzatore per sfogliare più rapidamente i portafogli su Sparrow. È particolarmente indicato se si dispone di una soluzione node-in-a-box come Umbrel o Start9, che consentono di installare Electrum con un solo clic.

Per farlo, procuratevi il Tor `.onion' Address del vostro server Electrum. Con Umbrel, ad esempio, lo troverete nell'applicazione Electrs.

![Image](assets/fr/17.webp)

Su Sparrow Wallet, accedere alla scheda "*Elettro privato*".

![Image](assets/fr/18.webp)

Inserire il proprio Tor Address nell'apposito spazio. Le altre impostazioni possono rimanere predefinite. Quindi fare clic su "*Test Connection*".

![Image](assets/fr/19.webp)

La connessione è confermata. Se si chiude questa finestra, nell'angolo in basso a destra appare un segno di spunta blu che indica che si è connessi a un server Electrum.

![Image](assets/fr/20.webp)

## Creare un portafoglio caldo

Ora che Sparrow Wallet è configurato per comunicare con la rete Bitcoin, siete pronti a creare il vostro primo Wallet. Questa sezione vi guida nella creazione di un Hot Wallet, ovvero un Wallet le cui chiavi private sono memorizzate sul vostro computer. Poiché il computer è una macchina complessa connessa a Internet, presenta una superficie di attacco molto ampia. Di conseguenza, un Hot Wallet dovrebbe essere utilizzato solo per quantità limitate di bitcoin. Per conservare quantità maggiori, optate per un Wallet sicuro con un Hardware Wallet. Se questo è ciò che state cercando, potete passare alla sezione successiva.

Per creare un Hot Wallet, dalla schermata iniziale di Sparrow Wallet, fare clic sulla scheda "*File*" e quindi su "*New Wallet*".

![Image](assets/fr/21.webp)

Inserire un nome per il portafoglio e cliccare su "*Crea Wallet*".

![Image](assets/fr/22.webp)

Nella parte superiore del Interface è possibile scegliere se creare un portafoglio "*Single Signature*" o "*Multi Signature*". Subito sotto, selezionate il tipo di script per bloccare i vostri UTXO. Vi consiglio di utilizzare lo standard più recente: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Quindi fare clic su "*Nuovo o importato Software Wallet*".

![Image](assets/fr/24.webp)

Scegliete lo standard BIP39, in quanto è supportato da quasi tutti i software del portafoglio Bitcoin. Scegliere quindi la lunghezza della frase di recupero. Attualmente è sufficiente una frase di 12 parole, poiché entrambe offrono una sicurezza simile, ma la frase di 12 parole è più semplice da salvare.

![Image](assets/fr/25.webp)

Fare clic sul pulsante "*generate New*" per inserire la frase generate del proprio Wallet. Questa frase dà accesso completo e illimitato a tutti i vostri bitcoin. Chiunque sia in possesso di questa frase può rubare i vostri fondi, anche senza accedere fisicamente al vostro computer.

La frase di 12 parole ripristina l'accesso ai bitcoin in caso di perdita, furto o rottura del computer. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.

È possibile inciderlo su carta o, per maggiore sicurezza, inciderlo su acciaio inossidabile per proteggerlo da incendi, inondazioni o crolli. La scelta del supporto per il vostro Mnemonic dipenderà dalla vostra strategia di sicurezza, ma se state usando Sparrow come Wallet a spesa calda contenente quantità moderate, la carta dovrebbe essere sufficiente.

Per ulteriori informazioni sul modo corretto di salvare e gestire la frase del Mnemonic, vi consiglio di seguire quest'altra guida, soprattutto se siete principianti:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Ovviamente, non dovete mai condividere queste parole su Internet, come faccio io in questa esercitazione. Questo esempio di Wallet sarà utilizzato solo sul Testnet e sarà cancellato alla fine del tutorial.**

Si può anche scegliere di aggiungere un passphrase BIP39 facendo clic sulla casella "*Usa passphrase*". Attenzione: l'uso di un passphrase può essere molto utile, ma se non si capisce come funziona, può essere molto rischioso. Per questo motivo vi consiglio vivamente di leggere questo breve articolo teorico sull'argomento:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Dopo aver salvato il Mnemonic e qualsiasi passphrase su un supporto fisico, fare clic su "*Conferma backup*".

![Image](assets/fr/27.webp)

Reinserire le 12 parole per confermare che sono state salvate correttamente, quindi fare clic su "*Create Keystore*".

![Image](assets/fr/28.webp)

Quindi fare clic su "*Import Keystore*" per importare le chiavi del portafoglio dal Mnemonic.

![Image](assets/fr/29.webp)

Cliccare su "*Apply*" per finalizzare la creazione del portafoglio.

![Image](assets/fr/30.webp)

Impostate una password forte per proteggere l'accesso al vostro portafoglio Sparrow. È buona norma conservare questa password in un gestore di password, in modo da non dimenticarla. Si noti che questa password non ha alcun ruolo nella derivazione delle chiavi. Viene utilizzata solo per accedere al proprio Wallet tramite Sparrow Wallet. Quindi, anche senza questa password, la frase Mnemonic sarà sufficiente per accedere ai bitcoin da qualsiasi applicazione compatibile con BIP39.

![Image](assets/fr/31.webp)

Il vostro Hot Wallet è ora creato. Potete passare alla sezione *Ricezione di Bitcoin* di questa esercitazione se non intendete utilizzare un Hardware Wallet con Sparrow.

## Gestione di un portafoglio Cold

Il secondo modo di utilizzare Sparrow Wallet è di configurarlo come gestore di portafoglio con un Hardware Wallet. In questa configurazione, le chiavi private del Bitcoin Wallet rimangono esclusivamente sul Hardware Wallet, mentre Sparrow accede solo alle informazioni pubbliche. Questo approccio offre un livello di sicurezza più elevato rispetto ai portafogli Hot discussi in precedenza, in quanto le chiavi private sono conservate su un dispositivo specializzato, spesso dotato di un chip sicuro, che non è connesso a Internet e presenta quindi una superficie di attacco molto più ridotta rispetto a un computer tradizionale.

Esistono due modi principali per collegare il Hardware Wallet a Sparrow:


- Con cavo, comunemente utilizzato con modelli entry-level come Trezor Safe 3 o Ledger Nano S Plus ;
- In modalità Air-Gap, cioè senza una connessione diretta via cavo, tramite una scheda MicroSD o il codice QR Exchange.

Sparrow supporta tutti questi metodi di comunicazione ed è compatibile con la maggior parte dei portafogli hardware presenti sul mercato.

Per questa esercitazione, utilizzerò un Ledger Nano S con cavo, ma la procedura è simile in modalità Air-Gap. Troverete i dettagli specifici per il vostro Hardware Wallet nel tutorial dedicato al Plan ₿ Network.

Prima di iniziare, accertarsi che il Wallet sia già configurato sul Hardware Wallet. Se si utilizza una connessione via cavo, collegarlo al computer tramite il cavo.

Per importare il cosiddetto "*Keystore*" (le informazioni pubbliche necessarie per gestire il portafoglio) in Sparrow Wallet, fare clic sulla scheda "*File*", quindi su "*New Wallet*".

![Image](assets/fr/32.webp)

Assegnare un nome al portafoglio e fare clic su "*Crea Wallet*". Vi consiglio di inserire il nome del vostro Hardware Wallet per identificarlo facilmente in seguito.

![Image](assets/fr/33.webp)

Nella parte superiore del Interface, scegliere tra un portafoglio "*Single Signature*" o "*Multi Signature*". Per il nostro esempio, configureremo un portafoglio a firma singola.

In basso, selezionare il tipo di script per bloccare gli UTXO. Se il vostro Hardware Wallet lo supporta, vi suggerisco di scegliere "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

Successivamente, la procedura varia a seconda del metodo di connessione utilizzato. Se si utilizza un metodo Air-Gap, selezionare "*Airgapped Hardware Wallet*". Seguire quindi le istruzioni specifiche del dispositivo.

![Image](assets/fr/35.webp)

Se si utilizza una connessione via cavo, come nel mio caso, scegliere "*Connesso Hardware Wallet*".

![Image](assets/fr/36.webp)

Fate clic su "*Scan*" per far rilevare a Sparrow il vostro dispositivo. Assicurarsi che sia collegato e sbloccato. Per alcuni modelli, come il Ledger, è necessario aprire l'applicazione "*Bitcoin*" per abilitare il rilevamento.

![Image](assets/fr/37.webp)

Selezionare "*Importa deposito chiavi*".

![Image](assets/fr/38.webp)

Cliccare su "*Apply*" per finalizzare la creazione del portafoglio.

![Image](assets/fr/39.webp)

Impostate una password forte per proteggere l'accesso al vostro Sparrow Wallet. Questa password proteggerà le chiavi pubbliche, gli indirizzi e la cronologia delle transazioni. Si consiglia di salvarla in un gestore di password. Si noti che questa password non ha alcun ruolo nella derivazione delle chiavi. Anche senza di essa, è possibile recuperare l'accesso ai bitcoin con il Mnemonic tramite qualsiasi software compatibile con BIP39.

![Image](assets/fr/40.webp)

Il portafoglio di gestione è ora configurato su Sparrow.

![Image](assets/fr/41.webp)

## Ricevere bitcoin

Ora che il Wallet è impostato su Sparrow, è possibile ricevere bitcoin. È sufficiente accedere al menu "*Ricevi*".

![Image](assets/fr/42.webp)

Sparrow visualizzerà il primo Address inutilizzato nel vostro Wallet. È possibile aggiungere una "*Etichetta*" a questo Address per ricordare l'origine di questi satoshi in futuro.

![Image](assets/fr/43.webp)

Se si utilizza un Hot Wallet, il Address visualizzato può essere utilizzato immediatamente, copiandolo o scansionando il codice QR associato.

Se si utilizza un Hardware Wallet, è molto importante controllare il Address sullo schermo del dispositivo prima di utilizzarlo. Per i dispositivi cablati, collegare e sbloccare il Hardware Wallet, quindi in Sparrow fare clic su "*Visualizza Address*". Assicurarsi che il Address visualizzato sul Hardware Wallet corrisponda a quello visualizzato su Sparrow.

![Image](assets/fr/44.webp)

Per gli utenti di Hardware Wallet Air-Gap, la verifica Address varia a seconda del modello di dispositivo. Per istruzioni precise, consultare l'esercitazione dedicata al Plan ₿ Network.

Una volta che la transazione è stata trasmessa dal pagatore, la si vedrà apparire nella scheda "*Transazioni*". È possibile fare clic su di essa per ottenere ulteriori dettagli, ad esempio il txid.

![Image](assets/fr/45.webp)

Nella scheda "*Indirizzi*" si trova un elenco di tutti gli indirizzi della posta in arrivo. È possibile vedere se sono già stati utilizzati e se è stata aggiunta un'etichetta. *Gli indirizzi "Receive*" sono quelli che Sparrow mostra quando si fa clic su "*Receive*" e sono destinati ai pagamenti in arrivo. Gli indirizzi "*Change*" sono utilizzati per il Exchange nelle transazioni, cioè per recuperare la parte inutilizzata dei vostri UTXO in entrata.

![Image](assets/fr/46.webp)

La scheda "*UTXOs*" mostra tutti i vostri UTXOs, cioè i frammenti Bitcoin in vostro possesso. È possibile vedere la quantità di ogni UTXO e l'etichetta associata.

![Image](assets/fr/47.webp)

## Inviare bitcoin

Ora che avete qualche satoshis nel vostro Wallet, avete anche la possibilità di inviarne qualcuno. Anche se ci sono diversi modi per farlo, vi consiglio di usare il menu "*UTXOs*" per avere un controllo più preciso sulle monete spese (*coin control*), piuttosto che andare direttamente al menu "*Send*" (anche se quest'ultimo può essere sufficiente se siete principianti).

![Image](assets/fr/48.webp)

Selezionare gli UTXO che si desidera utilizzare come input per questa transazione, quindi fare clic su "*Invia selezionati*". Questo approccio consente di selezionare le fonti più appropriate tra gli UTXO, in base alle spese e alle etichette applicate al momento della ricezione, al fine di ottimizzare la riservatezza dei pagamenti. Assicuratevi che la somma degli UTXO selezionati sia superiore all'importo che desiderate inviare.

![Image](assets/fr/49.webp)

Inserire il Address del destinatario nel campo "*Pagare a*". È anche possibile scansionare il Address con la webcam facendo clic sull'icona della fotocamera. Il pulsante "*+Aggiungi*" consente di pagare più indirizzi in un'unica transazione.

![Image](assets/fr/50.webp)

Aggiungete un'etichetta alla vostra transazione per ricordarvi il suo scopo. Questa etichetta sarà anche associata al vostro eventuale Exchange.

![Image](assets/fr/51.webp)

Inserire l'importo da inviare a questo Address.

![Image](assets/fr/52.webp)

Regolare la tariffa in base alle attuali condizioni di mercato. È possibile farlo inserendo un valore assoluto della tariffa o regolando la tariffa con il cursore.

![Image](assets/fr/53.webp)

Nella parte inferiore del Interface è possibile scegliere tra "*Efficienza*" e "*Privacy*". Nel mio caso, l'opzione "*Privacy*" non è disponibile, poiché ho solo un UTXO in questo portafoglio. "*Efficienza*" corrisponde a una transazione classica, mentre "*Privacy*" è una transazione di tipo Stonewall, una struttura di transazione che rafforza la vostra riservatezza simulando un mini-CoinJoin, il che rende più complessa l'analisi della catena.

![Image](assets/fr/54.webp)

Sparrow visualizza un diagramma riassuntivo che mostra gli input, gli output e le commissioni di transazione (si noti che le commissioni non sono in realtà un output, contrariamente a quanto suggerisce il diagramma). Se siete soddisfatti di tutto, fate clic su "*Crea transazione*".

![Image](assets/fr/55.webp)

In questo modo si accede a una pagina con i dettagli del Elements della transazione. Verificare che tutte le informazioni siano corrette, quindi fare clic su "*Finalizza transazione per la firma*".

![Image](assets/fr/56.webp)

È importante mantenere il default di Sighash. Per capire perché, date un'occhiata a questo corso di formazione, in cui vi spiego tutto quello che c'è da sapere su Sighash:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Nella schermata successiva, le opzioni variano a seconda del tipo di Wallet in uso:


- Per un Hardware Wallet Air-Gap, fare clic su "*Mostra QR*" per visualizzare un PSBT che è possibile firmare con il proprio dispositivo, quindi caricare il PSBT firmato in Sparrow utilizzando "*Scansiona QR*". L'opzione "*Salva transazione*" funziona in modo simile, ma con scambi su microSD;
- Per un Hot Wallet, è sufficiente fare clic su "*Firma*" e inserire la password del Wallet per firmare;
- Per un Hardware Wallet cablato, fare clic anche su "*Sign*" per inviare la transazione non firmata al dispositivo.

![Image](assets/fr/57.webp)

Sul proprio Hardware Wallet, controllare il Address del destinatario, l'importo inviato e le spese. Se tutto è corretto, procedere con la firma.

Una volta firmata, la transazione riapparirà in Sparrow, pronta per essere trasmessa sulla rete Bitcoin e successivamente inserita in un blocco. Se tutto è corretto, fare clic su "*Transazione trasmessa*".

![Image](assets/fr/58.webp)

La transazione è ora trasmessa e in attesa di conferma.

![Image](assets/fr/59.webp)

## Gestione e configurazione dei portafogli su Sparrow

Nella scheda "*Impostazioni*" si trovano informazioni dettagliate sul portafoglio, come :


- Tipo di portafoglio (single-sig o multi-sig) ;
- Tipo di script utilizzato ;
- Il nome assegnato al portafoglio ;
- Impronta della chiave master;
- Il percorso di bypass ;
- La chiave pubblica estesa dell'account.

![Image](assets/fr/60.webp)

Il pulsante "*Esporta*" consente di esportare le informazioni del portafoglio in modo da poterle utilizzare in altri software mantenendo le informazioni impostate in Sparrow.

Il pulsante "*Aggiungi account*" consente di aggiungere un altro account al portafoglio. Un account corrisponde a un insieme separato di indirizzi di posta elettronica. Questa funzione può essere utile, ad esempio, se si desidera separare un account personale da uno aziendale, con una singola frase Mnemonic.

Il pulsante "*Avanzate*" consente di accedere alle impostazioni avanzate, come la personalizzazione della ricerca Address di Sparrow e la modifica della password del portafoglio.

![Image](assets/fr/61.webp)

Quando si chiude Sparrow Wallet, il Wallet si blocca automaticamente. Alla successiva apertura del software, una finestra chiederà di sbloccare il Wallet con la password.

![Image](assets/fr/62.webp)

Se questa finestra non si apre o se si desidera aprire un altro portafoglio su Sparrow, fare clic sulla scheda "*File*" e selezionare "*Apri Wallet*".

![Image](assets/fr/63.webp)

In questo modo si aprirà il File Manager nella cartella in cui Sparrow memorizza i portafogli. È sufficiente selezionare il Wallet che si desidera aprire e inserire la password per sbloccarlo.

![Image](assets/fr/64.webp)

Nel menu "*File*", alla voce "*Impostazioni*", si trovano i parametri di connessione alla rete Bitcoin già esplorati nelle sezioni precedenti. È inoltre possibile regolare vari parametri come l'unità di misura utilizzata, la valuta fiat per le conversioni e le fonti di informazione.

![Image](assets/fr/65.webp)

La scheda "*Vista*" offre opzioni di personalizzazione e l'accesso ad alcuni comandi utili, come "*Refresh Wallet*", che aggiorna la ricerca delle transazioni per il portafoglio.

![Image](assets/fr/66.webp)

La scheda "*Strumenti*" raggruppa diversi strumenti avanzati, tra cui :


- "*Firma/Verifica messaggio*" consente di dimostrare il possesso di un Address ricevente o di verificare una firma.
- "*Invia a molti*" offre un Interface semplificato per l'esecuzione di transazioni a più indirizzi di ricezione contemporaneamente, comodo per le spese in batch.
- "*Sweep Private Key*" consente di recuperare i bitcoin protetti da una semplice chiave privata e di trasferirli al proprio Sparrow Wallet. Questo può essere particolarmente utile per chi possiede bitcoin risalenti ai primi anni 2010, prima dell'era dei portafogli HD.
- "Verify Download" verifica l'integrità e l'autenticità del software scaricato prima di installarlo sul dispositivo.
- "*Restart In*" consente di passare ai portafogli sulle reti Testnet o Signet. Questo può essere utile se si desidera accedere a reti di prova con monete di nessun valore reale.

![Image](assets/fr/67.webp)

Ora sapete tutto sul software Sparrow Wallet, uno strumento eccellente per la gestione quotidiana dei portafogli Bitcoin.

Se questa esercitazione vi è stata utile, vi sarei molto grato se lasciaste un pollice Green qui sotto. Sentitevi liberi di condividerlo sui vostri social network. Grazie mille!

Vi consiglio anche quest'altro tutorial in cui spiego come configurare la COLDCARD Q Hardware Wallet con Sparrow Wallet :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
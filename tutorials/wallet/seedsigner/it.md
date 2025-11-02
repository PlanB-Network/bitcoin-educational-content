---
name: SeedSigner
description: Un Hardware Wallet fai-da-te, senza stato, economico e con una copertura aerea completa
---

![cover](assets/cover.webp)



Il SeedSigner è un Hardware Wallet Bitcoin open-source che chiunque può costruire da sé utilizzando componenti elettronici economici e generici. A differenza di prodotti commerciali come il Ledger, la Coldcard o il Trezor, non si tratta di un dispositivo pronto all'uso prodotto da un'azienda: è un progetto comunitario che consente a tutti di creare il proprio dispositivo, controllandone ogni fase.



Il SeedSigner è progettato per essere al 100% ***air-gapped***: non si connette mai a Internet, non ha Wi-Fi o Bluetooth (nel caso del Raspberry Pi Zero v1.3) e non è mai connesso a un computer per i dati Exchange. La comunicazione avviene esclusivamente tramite un sistema Exchange con codice QR. Concretamente, il vostro software di gestione del portafoglio (come il Sparrow wallet) visualizza la transazione da firmare sotto forma di codici QR; voi li scansionate con la fotocamera del SeedSigner, quindi il dispositivo firma la transazione utilizzando le vostre chiavi private temporaneamente memorizzate nella sua RAM. Infine, il dispositivo genera codici QR contenenti la transazione firmata, che l'utente scansiona con il proprio software per inviarla alla rete Bitcoin.



![Image](assets/fr/001.webp)



SeedSigner è anche ***stateless***. In altre parole, non salva il seed o le chiavi private in modo permanente, a differenza di altri portafogli hardware. Ogni volta che si riavvia, la sua memoria è completamente vuota, a meno che non si configuri il dispositivo per salvare le impostazioni su una scheda microSD. È quindi necessario reinserire il proprio seed ogni volta che lo si utilizza; il metodo più pratico è quello di memorizzarlo sotto forma di codice QR, da scansionare all'avvio con la fotocamera di SeedSigner. Questa modalità di funzionamento riduce notevolmente la superficie di attacco: anche se un ladro ruba il dispositivo, non vi troverà alcuna informazione, poiché è sempre vuoto per impostazione predefinita.



Un'altra opzione per memorizzare il seed e utilizzarlo con SeedSigner è quella di utilizzare una smart card *SeedKeeper* insieme a un lettore compatibile. In questo modo si ottiene un *secure element* molto robusto per memorizzare il seed, mentre si utilizza lo schermo di SeedSigner per firmare le transazioni. Ma questa particolare configurazione è oggetto di un'altra esercitazione dedicata. Qui ci concentreremo sull'uso di base di SeedSigner:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Il progetto SeedSigner occupa un posto importante nell'ecosistema Bitcoin, poiché offre a tutti, ovunque nel mondo, la possibilità di beneficiare di una sicurezza avanzata per proteggere i propri bitcoin. Il suo principale vantaggio risiede nella sua accessibilità: l'hardware necessario può essere acquistato per meno di 50 dollari. Inoltre, consente alle persone che vivono in Paesi con restrizioni di costruire il proprio Hardware Wallet a partire da componenti informatici standard, facili da reperire e meno soggetti a vincoli normativi.



Ma anche al di fuori di questi contesti particolari, SeedSigner può essere un'opzione interessante: è open-source, funziona in modo stateless e airgapped, e riduce i vettori di attacco legati alla catena Supply del vostro Hardware Wallet.



## 1. Attrezzatura necessaria



Per costruire SeedSigner, sono necessari i seguenti componenti:





- Raspberry Pi Zero
    - Si consiglia la versione 1.3, che non dispone né di Wi-Fi né di Bluetooth, garantendo un isolamento completo.
 - Anche le versioni W e v2 sono compatibili, ma incorporano un chip Wi-Fi/Bluetooth. È quindi consigliabile disattivarlo fisicamente rimuovendo il modulo radio dalla scheda. L'operazione è relativamente semplice, ma richiede precisione (per la Zero W sono sufficienti delle pinze sottili, mentre per la v2 è necessaria una penna Hot per rimuovere la piastra metallica che nasconde il modulo). Non entrerò nei dettagli in questo tutorial, ma troverete tutte le istruzioni in questo documento: *[Disabilitazione WiFi/Bluetooth via hardware] (https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Attenzione: alcuni modelli di Raspberry Pi Zero vengono venduti senza pin GPIO pre-saldati. È possibile acquistare una versione con pin integrati direttamente (soluzione più semplice), oppure acquistare i pin separatamente e saldarli da soli (soluzione più complessa).
 - Non dimenticare di includere un alimentatore micro-USB Supply.



![Image](assets/fr/002.webp)





- Schermo Waveshare da 1,3" (240×240 px)** (in francese)
    - È essenziale scegliere questo particolare modello: esistono altri schermi simili, ma con una risoluzione diversa. Senza la definizione di 240×240 px, il display sarà inutilizzabile.
    - Il display incorpora tre pulsanti e un mini-joystick che funge da Interface per l'utente.



![Image](assets/fr/003.webp)





- Fotocamera compatibile con Raspberry Pi Zero**
    - Opzione 1: la fotocamera standard con un ampio tappetino dorato (verificare la compatibilità con la custodia).
    - Opzione 2: la fotocamera più compatta "*Zero*", progettata appositamente per il Pi Zero.



![Image](assets/fr/004.webp)





- Scheda MicroSD**
    - Capacità consigliata: tra 4 e 32 GB.





- Alloggiamento (opzionale, ma consigliato)** (opzionale, ma consigliato)** (opzionale, ma consigliato)** (opzionale, ma consigliato)** (consigliato)
    - Protegge il dispositivo e lo rende facile da usare.
    - Il modello più popolare è il "*Caso della pillola arancione*", per il quale sono disponibili [file STL open-source per la stampa 3D](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Le scatole sono disponibili anche presso [rivenditori indipendenti legati al progetto](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



È possibile acquistare questi componenti separatamente o, per maggiore semplicità, optare per pacchetti già pronti che includono tutto l'hardware necessario. Personalmente, ho ordinato il mio pacchetto [da questo sito francese](https://bitcoinbazar.fr/), ma troverete anche un elenco di fornitori per ogni regione del mondo sulla [pagina hardware del progetto SeedSigner](https://seedsigner.com/hardware/). Se preferite acquistare i componenti singolarmente, sono disponibili sulle principali piattaforme di e-commerce o nei negozi specializzati.



## 2. Preparazione del software



Una volta che l'hardware è stato assemblato, è necessario preparare la scheda microSD installandovi il sistema SeedSigner. Per fare ciò, andate sul vostro computer di tutti i giorni e inserite la microSD destinata a SeedSigner.



### 2.1. Scaricare



Andare su [repository GitHub ufficiale del progetto](https://github.com/SeedSigner/seedsigner/releases). Per la versione più recente del software, scaricare :




- L'immagine `.img' corrispondente al modello di Pi.
- Il file `.sha256.txt`.
- Il file `.sha256.txt.sig'.



![Image](assets/fr/006.webp)



Prima di iniziare l'installazione, controlliamo il software.



### 2.2 Verifica in Linux e macOS



Iniziate importando la chiave pubblica ufficiale del progetto SeedSigner direttamente da Keybase:



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Il terminale dovrebbe indicare che una chiave è stata importata o aggiornata. Quindi, eseguire il comando di verifica sul file di firma (ricordarsi di modificare il comando in base alla propria versione, qui `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Se tutto è corretto, l'output dovrebbe essere `Buona firma`. Ciò significa che il file `.sha256.txt` è stato firmato dalla chiave appena importata e che la firma è valida. Ignorate il messaggio di avvertimento `WARNING: This key is not certified with a trusted signature`: è normale, perché ora sta a voi verificare che la chiave utilizzata appartenga al progetto SeedSigner.



A tal fine, confrontare gli ultimi 16 caratteri dell'impronta digitale visualizzata con quelli disponibili su [Keybase.io/SeedSigner](https://keybase.io/seedsigner), sul loro [Twitter ufficiale](https://twitter.com/SeedSigner/status/1530555252373704707) o nel file pubblicato su [SeedSigner.com](https://seedsigner.com/keybase.txt). Se questi identificatori corrispondono esattamente, si può essere certi che la chiave sia effettivamente quella del progetto. In caso di dubbio, fermatevi immediatamente e chiedete aiuto alla comunità di SeedSigner (Telegram, X, GitHub...).



Quando la chiave è stata convalidata, si può verificare che l'immagine scaricata non sia stata modificata (ricordarsi di modificare il comando in base alla propria versione, qui `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- In Linux, questo comando è integrato.
- Attenzione: le versioni di macOS precedenti a `Big Sur (11)` non riconoscono l'opzione `--ignore-missing`. In questo caso, rimuoverla e ignorare gli avvisi sui file mancanti.



Il risultato atteso è un `OK` accanto al file `.img`. Questo conferma che l'immagine caricata è identica a quella pubblicata dal progetto e non è stata modificata.



### 2.3 Verifica di Windows



Su Windows, la procedura è simile ma i comandi sono diversi. Iniziare installando [Gpg4win] (https://www.gpg4win.org/) e aprire l'applicazione *Kleopatra*. Importare la chiave pubblica del progetto SeedSigner dall'URL Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Quindi, aprire PowerShell nella cartella in cui si trovano i file scaricati (`Shift` + clic destro > `Apri PowerShell qui`). Eseguite il seguente comando per verificare la firma del manifest (ricordate di modificare il comando in base alla vostra versione, qui `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Se tutto è corretto, l'output dovrebbe essere `Buona firma`. Ciò significa che il file `.sha256.txt` è stato firmato dalla chiave appena importata e che la firma è valida. Ignorate il messaggio di avvertimento `WARNING: This key is not certified with a trusted signature`: è normale, perché ora sta a voi verificare che la chiave utilizzata appartenga al progetto SeedSigner.



A tal fine, confrontare gli ultimi 16 caratteri dell'impronta digitale visualizzata con quelli disponibili su [Keybase.io/SeedSigner](https://keybase.io/seedsigner), sul loro [Twitter ufficiale](https://twitter.com/SeedSigner/status/1530555252373704707) o nel file pubblicato su [SeedSigner.com](https://seedsigner.com/keybase.txt). Se questi identificatori corrispondono esattamente, si può essere certi che la chiave sia effettivamente quella del progetto. In caso di dubbio, fermatevi immediatamente e chiedete aiuto alla comunità di SeedSigner (Telegram, X, GitHub...).



Una volta convalidata la chiave, è necessario verificare che il file immagine non sia stato danneggiato. A tale scopo, utilizzate il seguente comando in PowerShell :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Esempio per un Raspberry Pi Zero 2 (ricordarsi di modificare il comando in base alla propria versione, qui `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell calcola quindi il Hash SHA256 del file immagine. Confrontate questo Hash con il valore corrispondente in `seedsigner.0.8.6.sha256.txt`.




- Se i due valori sono strettamente identici, la verifica ha esito positivo e si può continuare.
- Se differiscono, il file è danneggiato o corrotto. Non utilizzarlo e ricominciare il download.



![Image](assets/fr/013.webp)



L'esito positivo della verifica garantisce che il file `.img' è autentico (firmato da SeedSigner) e inalterato (non modificato). Si può quindi passare tranquillamente al passo successivo.



### 2.4. Flash dell'immagine



Se non lo si possiede già, scaricare il software [Balena Etcher] (https://etcher.balena.io/), quindi :




- Inserire la scheda microSD nel computer.
- Avviare Etcher.
- Selezionare il file `.img' scaricato e verificato.
- Selezionare la scheda microSD come destinazione.
- Fare clic su `Flash!`.



![Image](assets/fr/014.webp)



Attendere il completamento del processo: la microSD è pronta per l'uso. Ora è il momento del montaggio!



## 3. Assemblaggio di SeedSigner



Dopo aver preparato la scheda microSD e averla flashata con il software SeedSigner, si può procedere all'assemblaggio finale. Prendete tempo, perché alcune parti sono fragili (in particolare la tovaglia, la fotocamera e i pin GPIO).



### 3.1 Preparazione dell'alloggiamento



Prima di tutto, aprire il case. Controllate che sia pulito e che non ci siano residui di plastica della stampa 3D che intralcino le chiusure interne. Cercare :




- Posizione della telecamera (piccolo foro circolare nella parte anteriore).
- L'apertura per lo schermo.
- Le aperture per le porte micro-USB e lo slot microSD del Raspberry Pi Zero.



### 3.2 Installazione della telecamera



Individuare il connettore a nastro della fotocamera sul Raspberry Pi Zero: è una sottile striscia nera sul lato della scheda, che può essere sollevata leggermente per aprirla. Sollevarla con cautela, senza forzarla: dovrebbe inclinarsi semplicemente di qualche millimetro.



![Image](assets/fr/015.webp)



Inserire il coperchio della fotocamera. La parte marrone/rame deve essere rivolta verso il basso. Assicurarsi che sia saldamente inserito nel connettore, senza che venga ruotato.



![Image](assets/fr/016.webp)



Chiudere la barra nera per bloccare la tovaglia (si sentirà un leggero scatto). Controllare delicatamente che rimanga in posizione e non si muova.



![Image](assets/fr/017.webp)



Posizionare quindi il modulo della telecamera nell'apposito foro dell'alloggiamento. A seconda del modello, può inserirsi direttamente o richiedere una piccola striscia adesiva per tenerlo in posizione. L'obiettivo deve essere perfettamente allineato, rivolto verso l'esterno.



### 3.3 Installazione del Raspberry Pi Zero



Se si utilizza una custodia, inserire la scheda Raspberry Pi Zero all'interno. Allineare con cura le porte con le aperture previste.



Posizionare quindi il display Waveshare sopra il Raspberry Pi Zero. I pin GPIO del Pi devono essere perfettamente allineati con il connettore femmina del display. Premere lentamente il display sui pin, esercitando una pressione uniforme su ciascun lato per evitare di piegarli.



![Image](assets/fr/018.webp)



Se si dispone di una custodia, completare l'assemblaggio aggiungendo il pannello frontale e il joystick.



Infine, inserire la scheda microSD contenente il software flashato nello slot montato sul bordo del Raspberry Pi Zero. Assicuratevi che scatti in posizione.



### 3.4 Primo avvio



Collegare un cavo di alimentazione micro-USB alla porta dedicata. Attendere circa un minuto. Dovrebbe apparire il logo di SeedSigner, seguito dalla schermata iniziale.



![Image](assets/fr/019.webp)



Per cominciare, verificate che i vari componenti funzionino correttamente accedendo al menu `Impostazioni > Test I/O'.



![Image](assets/fr/020.webp)



Testare tutti i pulsanti e verificare che rispondano correttamente. Quindi fare clic sul pulsante `KEY1` per verificare che la fotocamera funzioni come previsto. Verrà scattata una foto.



![Image](assets/fr/021.webp)



### 3.5 Regolazione della telecamera



A seconda di come è stato montato SeedSigner, la fotocamera potrebbe visualizzare un'immagine invertita. Per correggere questo problema, andare su `Impostazioni > Avanzate > Rotazione fotocamera` e selezionare una rotazione di 180°, se necessario.



![Image](assets/fr/022.webp)



Se si è cambiato l'orientamento della fotocamera o si desidera modificare altre impostazioni (come la lingua Interface) in un secondo momento, è necessario abilitare la persistenza delle impostazioni sulla microSD. In caso contrario, le impostazioni torneranno a essere quelle predefinite a ogni riavvio, poiché il Raspberry Pi Zero non dispone di memoria persistente.



Per farlo, aprire il menu `Impostazioni > Impostazioni persistenti', quindi selezionare `Abilitato'.



![Image](assets/fr/023.webp)



Se tutto è funzionante, il vostro SeedSigner è pronto per l'uso!



## 4. Impostazioni di SeedSigner



Prima di creare il Bitcoin Wallet, configuriamo il SeedSigner. Poiché funziona su un Raspberry Pi Zero senza memoria persistente, le sue impostazioni non vengono salvate automaticamente, a meno che non le si salvi sulla scheda microSD. Assicuratevi quindi di aver abilitato questa opzione, altrimenti le impostazioni andranno perse al riavvio (vedi punto 3.5).



### 4.1 Accesso al menu dei parametri



Avviare SeedSigner e attendere che venga visualizzata la schermata iniziale. Utilizzando il joystick, navigare fino all'opzione `Impostazioni`, quindi convalidare premendo il pulsante centrale. A questo punto si accede al menu principale delle impostazioni.



![Image](assets/fr/024.webp)



### 4.2 Scelta del software di gestione del portafoglio



Accedere quindi al menu "Software coordinatore".



![Image](assets/fr/025.webp)



Il `Coordinatore` si riferisce al software di gestione del portafoglio con cui il vostro SeedSigner comunicherà tramite codici QR. Questo software viene installato sul computer o sullo smartphone. Vi permetterà di gestire i vostri bitcoin, ma senza avere accesso alle vostre chiavi private. Il SeedSigner rimane l'unico dispositivo in grado di firmare le transazioni.



La versione attuale del firmware supporta diversi pacchetti software: Sparrow, Specter, BlueWallet, Nunchuk e Keeper. Nel mio caso, utilizzo **Sparrow wallet**, che raccomando particolarmente per la sua semplicità e ricchezza di funzionalità.



Se non sapete come installarlo, potete seguire questa guida:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

È sufficiente selezionare il software desiderato dal menu.



![Image](assets/fr/026.webp)



### 4.3 Visualizzazione delle unità e dell'importo



Nel menu `Denomination Display` è possibile scegliere l'unità di misura in cui vengono visualizzati gli importi:




- `BTC`
- mBTC` (milli-Bitcoin, o 0,001 BTC)
- gW-20 (satoshis, o 1/100.000.000 BTC)



L'unità **Sats** è generalmente la più pratica per piccole quantità.



![Image](assets/fr/027.webp)



### 4.4 Impostazioni avanzate



Andate ora al menu `Avanzate`. Qui troverete diverse opzioni utili:




- gW-22 network`: da modificare solo se si desidera utilizzare il SeedSigner su Testnet.
- densità codice QR`: regola la quantità di informazioni contenute in ogni codice QR. Potete lasciare il valore predefinito, a meno che non troviate difficile la lettura durante la scansione.
- `Xpub export`: abilita o disabilita l'esportazione della chiave pubblica estesa (`xpub`, `ypub`, `zpub`) al software di gestione del portafoglio tramite codice QR (una funzione che useremo in seguito, quindi lasciatela abilitata per ora).
- tipi di script": definisce i tipi di script consentiti per bloccare i bitcoin. Non è necessario modificare questo parametro, in quanto il tipo di script sarà impostato direttamente su Sparrow. Qui sono interessati solo gli script che il SeedSigner è autorizzato a manipolare.



### 4.5 Selezione della lingua



Infine, nel menu `Lingua` è possibile cambiare la lingua del Interface in base alle proprie preferenze.



![Image](assets/fr/028.webp)



## 5. Creazione e salvataggio del seed



La frase seed (o Mnemonic) costituisce la base del vostro portafoglio Bitcoin. Viene utilizzata per ricavare le chiavi private e gli indirizzi e fornisce l'accesso ai fondi. SeedSigner offre diversi metodi per generarla, che analizzeremo in questa sezione.



Prima di iniziare, alcuni promemoria essenziali:




- Chiunque sia in possesso di questa frase può rubare i vostri fondi, anche senza avere accesso fisico al vostro SeedSigner ;
- Di solito, per ripristinare un Wallet in caso di smarrimento o furto di un Hardware Wallet si utilizza una frase di 12 parole. Ma poiché il SeedSigner è un dispositivo *senza stato*, non registra mai il seed. Quindi i backup fisici non sono solo copie di sicurezza, ma **l'unico modo per utilizzare il Wallet. Pertanto, i backup fisici non sono solo copie di sicurezza, ma **l'unico modo per utilizzare il Wallet**. Se perdete questi backup, i vostri bitcoin andranno definitivamente persi. Quindi eseguite il backup con attenzione, su diversi supporti e in luoghi sicuri;
- Se siete agli inizi, vi consiglio vivamente di leggere questo tutorial per comprendere nel dettaglio i rischi legati alla gestione di una frase Mnemonic :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Accedere allo strumento di creazione seed



Dalla schermata iniziale di SeedSigner, andare al menu "Strumenti".



![Image](assets/fr/029.webp)



Ora il generate è il vostro seed. Un seed è semplicemente un grande numero casuale. Più è generato in modo casuale, più è sicuro. SeedSigner offre due modi per farlo:




- fotocamera": seed è generato dal rumore visivo di una fotografia. Si prende un'immagine di un ambiente casuale (oggetto, paesaggio, volto, ecc.) le cui variazioni di pixel vengono utilizzate per generare generate entropia. È un metodo veloce, ma non riproducibile.
- lanci di dadi": si tirano i dadi per creare l'entropia necessaria. È un metodo che richiede più tempo, ma è riproducibile e quindi verificabile. Se si opta per questo metodo, seguire i consigli di questo tutorial (non è necessario calcolare il checksum, se ne occupa SeedSigner):



https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Creazione del seed con la foto



Se si sceglie il metodo fotografico, cliccare su `New seed` (con l'icona della macchina fotografica), scattare una foto e convalidare. Selezionare quindi la lunghezza della frase (12 o 24 parole), che apparirà sullo schermo per essere salvata. Le fasi successive sono identiche a quelle della parte 5.3.



### 5.3 Creare seed con i dadi



In questa esercitazione, utilizzeremo il metodo dei **tiri di dado**. Cliccare su `New seed` (con l'icona del dado).



![Image](assets/fr/030.webp)



Scegliete quindi la lunghezza della vostra frase Mnemonic. 12 parole offrono già un livello di sicurezza sufficiente, quindi questa è la scelta che consiglio.



![Image](assets/fr/031.webp)



Lanciare i dadi e inserire i numeri risultanti utilizzando il cursore. Premere il pulsante centrale per convalidare ogni immissione. Se si commette un errore, si può tornare indietro. Utilizzare più dadi diversi per ridurre l'influenza di eventuali dadi sbilanciati. Assicuratevi di non essere osservati durante questa operazione.



![Image](assets/fr/032.webp)



Una volta inseriti i 50 lanci, SeedSigner genera la frase. **Seguite attentamente le istruzioni di questo tutorial se siete alle prime armi:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Visualizzazione e salvataggio del seed



Scrivete con cura le parole della vostra frase Mnemonic su un supporto fisico adeguato (carta o metallo).



![Image](assets/fr/033.webp)



### 5.5 Verifica del backup



Per evitare errori di backup, SeedSigner chiede di verificare il backup. Fare clic su "Verifica".



![Image](assets/fr/034.webp)



Inserite quindi la parola richiesta in base al suo ordine nella frase. Ad esempio, qui devo scegliere la terza parola della frase.



![Image](assets/fr/035.webp)



In caso di errore, il SeedSigner vi informerà e dovrete ricominciare da capo, assicurandovi di annotare la frase Mnemonic quando vi viene fornita. Questa fase di verifica assicura che il backup sia corretto e completo. Una volta convalidato, sullo schermo verrà visualizzato "Backup verificato".



![Image](assets/fr/036.webp)



Per un test di ripristino più completo, seguire questa esercitazione:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Comprendere il concetto di "dispositivo stateless



Il SeedSigner è un dispositivo senza memoria permanente. Ciò significa che il vostro seed non viene mai memorizzato all'interno del dispositivo (a differenza di un Ledger, di un Trezor o di una Coldcard, per esempio). Non appena si spegne il dispositivo, il seed scompare completamente dalla sua RAM. Quando SeedSigner si riavvia, ritorna allo stato di vuoto: per firmare le vostre transazioni dovrete fornirgli nuovamente il vostro seed.



Questo fornisce una protezione essenziale. A differenza di altri portafogli hardware, SeedSigner si basa su un Raspberry Pi Zero senza alcuna protezione fisica, compreso il *secure element*. Ma poiché non vengono memorizzati dati sensibili, anche un dispositivo fisicamente compromesso non permetterebbe a un aggressore di estrarre le chiavi private o di spendere i bitcoin.



D'altra parte, questa architettura implica un'ulteriore responsabilità: senza un backup, i vostri fondi sono definitivamente persi. Ecco perché consiglio un **doppio backup**. Avete già la vostra frase di ripristino: si tratta del vostro backup principale a lungo termine, da conservare in un luogo sicuro. Ora creeremo una copia di questa frase sotto forma di **codice QR**.



Ogni volta che si utilizza SeedSigner, si scansiona questo codice QR con la fotocamera del dispositivo, in modo da caricare temporaneamente i seed nella sua memoria mentre si firmano le transazioni. Anche questo secondo backup, destinato all'uso quotidiano, deve essere conservato con la massima cura: chiunque sia in possesso di questo codice QR ha pieno accesso ai vostri bitcoin.


Vi consiglio inoltre di conservare il codice QR e la frase Mnemonic in due luoghi separati, per evitare di perdere tutto in caso di sinistro.



Infine, un'alternativa più avanzata e sicura consiste nell'utilizzare il SeedSigner con un **SeedKeeper**, che memorizza il seed in un secure element. Per saperne di più, consultate questo tutorial:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Scrittura dell'impronta digitale della chiave master



Una volta completata la verifica, SeedSigner visualizza l'impronta digitale della chiave master del Wallet. Questa impronta digitale identifica il vostro Wallet e vi garantisce di utilizzare la frase di recupero corretta in futuro. Non rivela alcuna informazione sulle vostre chiavi private, quindi potete conservarla in modo sicuro su un supporto digitale. Assicuratevi di conservarne una copia accessibile e di non perderla mai.



![Image](assets/fr/037.webp)



In questa fase è anche possibile aggiungere un **passphrase BIP39** per rafforzare la sicurezza del Wallet. Questa opzione può essere utile, a seconda della vostra strategia di backup, ma comporta anche dei rischi: se perdete il passphrase, l'accesso ai vostri bitcoin sarà definitivamente perso.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Se non conoscete ancora il concetto di passphrase, vi invito a leggere questo tutorial completo sull'argomento:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Salvataggio del seed in formato QR (*SeedQR*)



SeedSigner consente di convertire il seed in un codice QR cartaceo, chiamato *SeedQR*. Questo metodo semplifica la ricarica del Wallet, in quanto evita di riscrivere manualmente ogni parola.



A tale scopo, è necessario un codice QR di carta o di metallo vuoto, corrispondente alla lunghezza della frase Mnemonic. Se avete acquistato un pacchetto completo per il vostro SeedSigner, i modelli sono solitamente inclusi. In caso contrario, è possibile scaricarli e stamparli (o riprodurli a mano) qui:




- [formato 12 parole](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [formato 24 parole](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Formato compatto 12 parole](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Formato compatto 24 parole](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Dalla schermata del seed, selezionare "Backup seed".



![Image](assets/fr/039.webp)



Quindi scegliere "Esporta come SeedQR".



![Image](assets/fr/040.webp)



Selezionare quindi il formato desiderato (normale o compatto) in base al modello di carta disponibile.



![Image](assets/fr/041.webp)



Fare clic su "Inizia" per avviare la creazione del *SeedQR*. SeedSigner visualizzerà una serie di griglie (A1, A2, B1, ecc.), ciascuna corrispondente a una parte del codice.



![Image](assets/fr/042.webp)



Riproducete con cura ogni punto nero sul foglio di salvataggio, quindi utilizzate il joystick per passare al BLOCK successivo. Prendete tempo: un semplice disallineamento può rendere inutilizzabile il codice QR.



Alcuni suggerimenti:




- Iniziate con una matita per poter correggere eventuali errori, poi tornate a usare una penna nera fine una volta terminato;
- È sufficiente un punto ben centrato al centro del quadrato, non è necessario riempirlo completamente.



![Image](assets/fr/043.webp)



Quindi fare clic su "Conferma SeedQR" e scansionare il codice QR per verificare che funzioni correttamente.



![Image](assets/fr/044.webp)



Se viene visualizzato il messaggio `Successo', il vostro *SeedQR* è valido: potete procedere al passo successivo.



![Image](assets/fr/045.webp)



**Conservate questo foglio come la vostra frase di recupero. Chiunque sia in possesso di questo codice QR può ricostruire le vostre chiavi private e rubare i vostri bitcoin.**



Congratulazioni, il vostro portafoglio Bitcoin è ora attivo e funzionante! Ora importeremo i suoi componenti pubblici in **Sparrow wallet** per gestirlo facilmente.



## 6. Importare Wallet in Sparrow



Una volta impostato SeedSigner e generato e salvato correttamente il seed, il passo successivo consiste nel collegare questo portafoglio al software di gestione, come il Sparrow wallet. Il vostro seed rimarrà sempre offline, in quanto solo la parte pubblica del vostro portafoglio sarà trasmessa al Sparrow. Ciò consentirà al software di visualizzare gli indirizzi, le transazioni e di creare nuove transazioni, senza poter spendere i bitcoin. Per spendere i bitcoin, il SeedSigner dovrà sempre firmare la transazione preparata da Sparrow.



### 6.1 Preparazione del SeedSigner



Inserire la microSD contenente il sistema operativo, accendere il SeedSigner e caricare il seed appena creato dal codice QR di backup. Nella schermata iniziale, selezionare "Scansione", quindi eseguire la scansione del SeedQR con il SeedSigner.



![Image](assets/fr/046.webp)



Verificare che l'impronta digitale della chiave master corrisponda all'impronta digitale del Wallet. Se si utilizza un passphrase, inserirlo in questa fase.



![Image](assets/fr/047.webp)



Si accede così al menu del proprio portfolio, nel mio caso denominato `d4149b27`. Se siete tornati alla schermata iniziale, selezionate `Seeds`, quindi scegliete la stampa corrispondente al vostro portfolio. Quindi fare clic su `Esporta Xpub`.



![Image](assets/fr/048.webp)



Selezionare il tipo di portafoglio. Nel nostro caso, si tratta di un portafoglio singolo: selezionare `Singolo Sig`.



![Image](assets/fr/049.webp)



Poi viene la scelta dello standard di scripting. Il più recente ed economico in termini di costi di transazione è il `Taproot`. Vi consiglio quindi di scegliere questo standard.



![Image](assets/fr/050.webp)



Apparirà un messaggio di avvertimento. È normale: questa chiave pubblica estesa (`xpub`) consente di visualizzare tutti gli indirizzi derivati dal proprio seed (sul primo conto). Non permette di spendere i fondi, ma rivela la struttura del portafoglio. Se mai dovesse trapelare, sarebbe un problema per la vostra privacy, ma non per la sicurezza dei vostri bitcoin: vi permette di vederli, ma non di spenderli.



Fare clic su `Ho capito`, quindi su `Esporta Xpub` se si è soddisfatti delle informazioni visualizzate.



Il SeedSigner genera quindi il vostro xpub sotto forma di codice QR dinamico contenente tutti i dati necessari per gestire il vostro portafoglio in Sparrow wallet.



![Image](assets/fr/051.webp)



Con il joystick è possibile regolare la luminosità dello schermo per facilitare la scansione del codice QR.



### 6.2 Importazione di un nuovo portafoglio in Sparrow wallet



Assicuratevi di aver installato il software Sparrow wallet sul vostro computer. Se non sapete come scaricarlo, controllarlo e installarlo correttamente, consultate il nostro tutorial completo sull'argomento:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Sul computer, aprire il Sparrow wallet, quindi nella barra dei menu fare clic su `File → Importa Wallet`.



![Image](assets/fr/052.webp)



Scorrere fino a `SeedSigner`, quindi selezionare `Scansione...`. Si aprirà la webcam: scansionare il codice QR dinamico visualizzato sullo schermo di SeedSigner.



![Image](assets/fr/053.webp)



Assegnare un nome al portafoglio, quindi fare clic su "Crea Wallet". Il Sparrow chiederà quindi di impostare una password per bloccare l'accesso locale a questo Wallet. Scegliete una password forte: protegge l'accesso ai dati del vostro portafoglio nel Sparrow (chiavi pubbliche, indirizzi, etichette e cronologia delle transazioni). Questa password non è necessaria per ripristinare il portafoglio in un secondo momento: a questo scopo è necessaria solo la frase del Mnemonic (ed eventualmente del passphrase).



Vi consiglio di salvare questa password in un gestore di password per evitare di perderla.



![Image](assets/fr/054.webp)



Il keystore è stato importato con successo.



![Image](assets/fr/055.webp)



Verificare quindi che l'impronta digitale "Master" visualizzata in Sparrow corrisponda a quella precedentemente annotata in SeedSigner.



Il SeedSigner e il Sparrow wallet sono ora collegati in modo sicuro. Il Sparrow funge da gestione completa del Interface, mentre il SeedSigner rimane l'unico dispositivo in grado di firmare le transazioni. Ora siete pronti a ricevere e inviare bitcoin in una configurazione totalmente air-gapped.



## 7. Ricevere e inviare bitcoin



SeedSigner e Sparrow wallet sono ora configurati per lavorare insieme. In questa sezione finale, vedremo come ricevere e inviare bitcoin utilizzando questa configurazione.



### 7.1 Ricevere bitcoin



#### 7.1.1 Generazione di una ricezione Address



Sul computer, aprire Sparrow wallet e sbloccare SeedSigner Wallet utilizzando la password. Assicurarsi che il software sia collegato a un server (tacca in basso a destra). Nella barra laterale, fare clic su "Ricezione".



![Image](assets/fr/056.webp)



Viene visualizzato un nuovo Bitcoin Address. Viene visualizzato :




- Il testo Address (che inizia con `bc1p...` se si usa P2TR come me),
- Il codice QR corrispondente,
- Un campo `Label` per tracciare le transazioni.



Vi consiglio vivamente di aggiungere un'etichetta a ogni ricevuta del Bitcoin sul vostro Wallet. Questo vi permetterà di identificare facilmente la provenienza di ogni UTXO e di migliorare la gestione della privacy. Per approfondire questo importante argomento, potete consultare la formazione dedicata su Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Per aggiungere un'etichetta, è sufficiente inserire un nome nel campo "Etichetta" e confermare.



Ad esempio:



```txt
Label : Sale of the Raspberry Pi Zero
```



Il vostro Address è ora associato a questa etichetta in tutte le sezioni del Sparrow.



![Image](assets/fr/057.webp)



#### 7.1.2 Verifica del Address sul SeedSigner



Prima di condividere il Address ricevuto, è molto importante verificare che esso appartenga al seed. Questo passaggio garantisce che il SeedSigner sia in grado di firmare le transazioni associate a questo Address. Inoltre, protegge da possibili attacchi in cui il Sparrow mostra un Address fraudolento. Ricordate che Sparrow viene eseguito in un ambiente non sicuro (il vostro computer), che ha una superficie di attacco molto più ampia rispetto al vostro SeedSigner, che è totalmente isolato. Per questo motivo, non si dovrebbe mai credere ciecamente a un destinatario Address visualizzato sul Sparrow finché non lo si è verificato con il proprio Hardware Wallet.



Sul Sparrow, fare clic sul codice QR del Address per ingrandirlo: verrà quindi visualizzato a schermo intero.



![Image](assets/fr/058.webp)



Nel SeedSigner, dal menu principale, selezionare "Scansione". Scansionare il codice QR visualizzato sullo schermo del computer, quindi scegliere il seed corrispondente al Wallet (nel mio caso, l'impronta digitale `d4149b27`).



![Image](assets/fr/059.webp)



Se il Address scansionato corrisponde a quello derivato dal seed, la schermata di SeedSigner visualizzerà il messaggio: `Address verificato`.



![Image](assets/fr/060.webp)



Questo conferma che il Address appartiene al vostro Wallet e che potete ricevere bitcoin con sicurezza.



#### 7.1.3 Ricezione dei fondi



A questo punto è possibile comunicare questo Address (in forma di testo o di codice QR) alla persona o al reparto che deve inviare il Satss. Una volta che la transazione è stata trasmessa in rete, apparirà nella scheda "Transazioni" del Sparrow wallet.



![Image](assets/fr/061.webp)



### 7.2 Inviare bitcoin



L'invio di bitcoin con un SeedSigner avviene in 3 fasi:




- Creazione di transazioni in Sparrow ;
- Firma della transazione sul SeedSigner ;
- Distribuzione finale della transazione tramite Sparrow.



Tutti gli scambi tra i due dispositivi avvengono esclusivamente tramite codici QR.



#### 7.2.1 Creazione della transazione in Sparrow



In Sparrow wallet, è possibile fare clic sulla scheda `Invio` nella barra laterale sinistra. Tuttavia, preferisco utilizzare la scheda `UTXOs`, che consente di praticare il "*Controllo Coin*". Questo metodo consente di controllare con precisione gli UTXO utilizzati, in modo da poter controllare le informazioni rivelate durante la transazione.



Nella scheda `UTXOs`, selezionare le monete che si desidera spendere, quindi fare clic su `Invia selezionati`.



![Image](assets/fr/062.webp)



Compilare quindi i campi della transazione:




- In `Pagare a`, incollare il Address del destinatario o fare clic sull'icona della fotocamera per scansionare il codice QR;
- In `Etichetta`, aggiungere un'etichetta per tracciare questa spesa;
- In "Importo", inserire l'importo da inviare;
- Infine, selezionare la tariffa in base alle attuali condizioni di mercato (le stime sono disponibili su [Mempool.space](https://Mempool.space/)).



Una volta completati i campi, controllare attentamente le informazioni, quindi fare clic su `Crea transazione >>.



![Image](assets/fr/063.webp)



Controllare i dettagli della transazione per verificare che tutto sia corretto, quindi fare clic su "Finalizza transazione per la firma".



![Image](assets/fr/064.webp)



La transazione è pronta, ma non ancora firmata. Per visualizzare il [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/PSBT) come codice QR, fare clic su `Mostra QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Firma della transazione con il SeedSigner



Accendere il SeedSigner e scansionare il SeedQR per accedere al portafoglio, come di consueto. Dalla schermata iniziale, selezionare "Scansione", quindi scansionare il codice QR visualizzato sul Sparrow.



![Image](assets/fr/066.webp)



Scegliete quindi il modello seed in base al vostro portafoglio.



![Image](assets/fr/067.webp)



SeedSigner rileva automaticamente che si tratta di un PSBT e visualizza un riepilogo della transazione:




   - L'importo inviato,
   - Indirizzi di uscita,
   - Costi di transazione associati.



Fare clic su "Rivedi dettagli" e controllare attentamente tutte le informazioni direttamente sulla schermata di SeedSigner. Gli elementi più importanti da controllare sono l'importo inviato, il Address del destinatario e l'importo delle spese applicate.



![Image](assets/fr/068.webp)



Se tutto è corretto, selezionare `Approva PSBT` per firmare la transazione utilizzando le chiavi private corrispondenti.



![Image](assets/fr/069.webp)



Una volta firmato, il SeedSigner genera un nuovo codice QR contenente la transazione firmata, pronto per essere scansionato da Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Trasmissione della transazione da Sparrow



Ora che la transazione è valida, deve essere trasmessa sulla rete Bitcoin, in modo che raggiunga un Miner che la aggiungerà a un BLOCK.



Sul Sparrow, fare clic su "Scansione QR".



![Image](assets/fr/071.webp)



Presentare il codice QR visualizzato dal SeedSigner (quello della transazione firmata) alla webcam. Il Sparrow decodificherà la firma e visualizzerà i dettagli completi della transazione. Verificare che tutte le informazioni siano corrette, quindi fare clic su Trasmetti transazione per trasmetterla alla rete Bitcoin.



![Image](assets/fr/072.webp)



La transazione è stata inviata alla rete Bitcoin. È possibile seguirne l'andamento nella scheda "Transazioni" del Sparrow wallet.



![Image](assets/fr/073.webp)



Ora avete imparato a conoscere le basi dell'uso di SeedSigner. Per approfondire le vostre conoscenze ed esplorare usi più avanzati, vi invito a consultare il seguente tutorial:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Puoi anche sostenere lo sviluppo del progetto open-source SeedSigner facendo una donazione in bitcoin!](https://seedsigner.com/donate/)**



*Crediti: alcune immagini di questo tutorial provengono dal [sito ufficiale del progetto SeedSigner](https://seedsigner.com/) e dal [repository GitHub](https://github.com/SeedSigner/seedsigner).*
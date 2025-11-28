---
name: Specter fai da te
description: Guida all'installazione di Specter DIY
---

![cover](assets/cover.webp)


## Specter-DIY


> I cypherpunk scrivono codice. Sappiamo che qualcuno deve scrivere software per difendere la privacy e, poiché non possiamo ottenere la privacy se non lo facciamo tutti, lo scriveremo.

*Il manifesto di Cypherpunk - Eric Hughes - 9 marzo 1993*


L'idea del progetto è quella di costruire un wallet hardware a partire da componenti di serie.

Anche se disponiamo di una scheda di estensione che racchiude tutto in un bel formato e consente di evitare le saldature, continueremo a supportare e mantenere la compatibilità con i componenti standard.


![image](assets/fr/01.webp)


Vogliamo anche mantenere il progetto flessibile, in modo che possa funzionare su qualsiasi altro insieme di componenti con modifiche minime. Forse volete realizzare un wallet su un'architettura diversa (RISC-V?), con un modem audio come canale di comunicazione - dovreste essere in grado di farlo. Dovrebbe essere facile aggiungere o modificare le funzionalità di Specter e noi cerchiamo di astrarre i moduli logici il più possibile.


I codici QR sono un modo predefinito per Specter di comunicare con l'host. I codici QR sono piuttosto comodi e consentono all'utente di controllare la trasmissione dei dati: ogni codice QR ha una capacità molto limitata e la comunicazione avviene in modo unidirezionale. Inoltre, la comunicazione avviene in modalità airgapped: non è necessario collegare il wallet al computer in qualsiasi momento.


Per la memorizzazione dei segreti supportiamo la modalità agnostica (il wallet dimentica tutti i segreti quando viene spento), la modalità spericolata (memorizza i segreti nella flash del microcontrollore dell'applicazione) e l'integrazione del secure element è in arrivo.


Il nostro obiettivo principale è la configurazione di più firme con altri portafogli hardware, ma wallet può funzionare anche come firmatario singolo. Cerchiamo di renderlo compatibile con Bitcoin Core dove possibile - PSBT per le transazioni non firmate, descrittori wallet per importare/esportare portafogli multisigla. Per comunicare più facilmente con Bitcoin Core stiamo anche lavorando a [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - un piccolo server python flask che parla con il vostro nodo Bitcoin Core.


La maggior parte del firmware è scritta in MicroPython, il che rende il codice facile da controllare e modificare. Utilizziamo la libreria [secp256k1](https://github.com/bitcoin-core/secp256k1) di Bitcoin Core per i calcoli delle curve ellittiche e la libreria [LittlevGL](https://lvgl.io/) per l'interfaccia grafica.


## Esclusione di responsabilità


Il progetto è maturato in modo significativo, tanto che il livello di sicurezza di Specter-DIY è ora paragonabile ai portafogli hardware commerciali presenti sul mercato. Abbiamo implementato un bootloader sicuro che verifica gli aggiornamenti del firmware, in modo da garantire che solo il firmware firmato possa essere caricato sul dispositivo dopo la configurazione iniziale. Tuttavia, a differenza dei dispositivi di firma commerciali, il bootloader deve essere installato manualmente dall'utente e non è impostato in fabbrica dal fornitore del dispositivo. Pertanto, è necessario prestare particolare attenzione durante l'installazione iniziale del firmware e assicurarsi di aver verificato le firme PGP e di flashare il firmware da un computer sicuro.


Se qualcosa non funziona, aprite un problema qui o fate una domanda nel nostro [gruppo Telegram](https://t.me/+VEinVSYkW5TUl5Ai).


## Lista della spesa per Specter-DIY


Qui descriviamo cosa acquistare e nella parte successiva spieghiamo come assemblarlo e alcune note sulla scheda: ponticelli di alimentazione, porte USB ecc.


### Scheda di scoperta


La parte principale del dispositivo è la scheda di sviluppo:



- Scheda sviluppatore STM32F469I-DISCO (ad es. da [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) o [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Cavo mini**USB
- Cavo MicroUSB standard per comunicare tramite USB


Facoltativo ma consigliato:


- [Scanner per codici QR Waveshare](https://www.waveshare.com/barcode-scanner-module.htm) con intestazioni a pin lunghe come [queste](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) o [queste](https://www.amazon.com/gp/product/B015KA0RRU/) per collegare lo scanner alla scheda (sono necessarie 4 intestazioni a pin).


Attualmente stiamo lavorando a una scheda di estensione che include uno slot per smartcard, uno scanner di codici QR, una batteria e una custodia stampata in 3d, ma non include la parte principale - la scheda di scoperta che deve essere ordinata separatamente. In questo modo l'attacco alla catena di approvvigionamento non è ancora un problema, poiché i componenti critici per la sicurezza vengono acquistati in un negozio di elettronica a caso.


È possibile iniziare a utilizzare Specter anche senza alcun componente aggiuntivo, ma sarà possibile comunicare con lui tramite USB o lo slot per schede SD integrato. L'utilizzo di Specter tramite USB significa che non è collegato all'aria e quindi si perde un'importante proprietà di sicurezza.


### Scanner QR


Per lo scanner di codici QR sono disponibili diverse opzioni.


**Opzione 1. Raccomandato.** Scanner molto buono da Waveshare (40$)


[Scanner Waveshare](https://www.waveshare.com/barcode-scanner-module.htm) - è necessario trovare un modo per montarlo bene, magari utilizzando una sorta di shield Arduino Prototype e del nastro adesivo.


Non è necessario saldare, ma se avete abilità nella saldatura potete rendere il wallet molto più bello ;)


**Opzione 2.** Scanner molto bello di Mikroe ma piuttosto costoso (150$):


[Codice a barre a scatto](https://www.mikroe.com/barcode-click) + [Adattatore](https://www.mikroe.com/arduino-uno-click-shield)


**Opzione 3.** Qualsiasi altro scanner QR


È possibile trovare alcuni scanner economici in Cina. La loro qualità spesso non è eccelsa, ma si può correre il rischio. Forse anche ESPcamera potrebbe fare al caso vostro. È sufficiente collegare l'alimentazione, l'UART (pin D0 e D1) e il trigger a D5.


**Opzione 4.** Nessun scanner.


Quindi è possibile utilizzare Specter solo con USB / SD Card.


A meno che non si costruisca un proprio modulo di comunicazione che utilizzi qualcos'altro al posto dei codici QR: audiomodem, bluetooth o altro. Non appena è possibile attivarlo e inviare i dati via seriale, si può fare quello che si vuole.


### Componenti opzionali


Se si aggiunge un piccolo powerbank o un caricabatterie/booster, il wallet diventa completamente autonomo ;)



## Assemblaggio di Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Collegamento dello scanner di codici a barre Waveshare


Il firmware del wallet configura lo scanner al primo avvio, quindi non è necessaria alcuna preconfigurazione manuale.


Ecco come collegare lo scanner alla scheda:


![image](assets/fr/02.webp)


Per comodità si può acquistare uno shield Arduino Protype e saldare e montare tutto su di esso (ad esempio [questo](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Gestione dell'alimentazione


Sul lato superiore della scheda è presente un ponticello che definisce il punto di alimentazione. È possibile cambiare la posizione del ponticello e selezionare la fonte di alimentazione da una delle porte USB o dal pin VIN e collegarvi una batteria esterna (dovrebbe essere a 5 V).


### Custodia per il fai-da-te


Consultate la cartella [allegati](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Siate creativi!


Assemblate il vostro Specter-DIY e inviateci le immagini (fate una richiesta di pull o contattateci).


Date un'occhiata alla [Gallery](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) con gli Specter assemblati dalla comunità!




## Installazione del codice compilato


Con il bootloader sicuro l'installazione iniziale del firmware è leggermente diversa. Gli aggiornamenti sono più semplici e non richiedono il collegamento dell'hardware wallet al computer.


![video](https://youtu.be/eF4cgK_L6T4)


### Flashing del firmware iniziale


**Nota** Se non volete usare i binari dei rilasci, consultate la [documentazione del bootloader](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) che spiega come compilarlo e configurarlo per usare le vostre chiavi pubbliche invece delle nostre.



- Se si effettua l'aggiornamento da versioni inferiori a `1.4.0` o si carica il firmware per la prima volta, utilizzare il file `initial_firmware_<version>.bin` dalla pagina [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Verificare la firma del file `sha256.signed.txt` con [la chiave PGP di Stepan](https://stepansnigirev.com/ss-specter-release.asc)
 - Verificare l'hash del file `initial_firmware_<version>.bin` con l'hash memorizzato nel file `sha256.signed.txt`
- Se si sta eseguendo l'aggiornamento da un bootloader vuoto o se viene visualizzato il messaggio di errore del bootloader che indica che il firmware non è valido, consultare la sezione successiva - Flashing del firmware Specter firmato.
- Accertarsi che il ponticello di alimentazione della scheda di rilevamento sia in posizione STLK
- Collegare la scheda di rilevamento al computer tramite il cavo **miniUSB** posto sulla parte superiore della scheda.
    - La scheda dovrebbe apparire come un disco rimovibile chiamato `DIS_F469NI`.
- Copiare il file `initial_firmware_<version>.bin` nella root del filesystem `DIS_F469NI`.
- Una volta terminato il flashing del firmware, la scheda si resetta e si riavvia al bootloader. Il bootloader controllerà il firmware e si avvierà al firmware principale. Se viene visualizzato un messaggio di errore che indica che non è stato trovato alcun firmware, seguire le istruzioni di aggiornamento e caricare il firmware tramite scheda SD.
- A questo punto, è possibile commutare il ponticello di alimentazione nella posizione desiderata e alimentare la scheda dalla powerbank o dalla batteria.


Il flashing del firmware iniziale tramite copia-incolla del file `.bin` a volte non riesce, spesso a causa del cavo o se si collega il dispositivo tramite un hub USB. In questo caso è possibile provare ancora un paio di volte (di solito funziona in 2-3 tentativi).


Se fallisce sempre, potete usare lo strumento open-source [stlink](https://github.com/stlink-org/stlink/releases/latest). Installatelo e digitate nel vostro terminale: `st-flash write <path/to/initial_firmare.bin> 0x8000000`. Di solito funziona in modo molto più affidabile.


### Aggiornamento del firmware



- Scaricare il file `specter_upgrade_<versione>.bin` dal sito [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Copiare questo file binario nella root della scheda SD (formattata in FAT, 32 GB al massimo)
 - Assicurarsi che nella directory principale sia presente un solo file `specter_upgrade***.bin
- Inserire la scheda SD nello slot SD della scheda di rilevamento e accendere la scheda
- Il bootloader eseguirà il flash del firmware e vi avviserà al termine dell'operazione.
- Riavviare la scheda: ora verrà visualizzata l'interfaccia di Specter-DIY, che suggerirà di selezionare il codice PIN


Ogni volta che viene rilasciata una nuova versione è sufficiente scaricare il file `specter_upgrade_<versione>.bin dalle release, scaricarlo sulla scheda SD e aggiornare il dispositivo come nel passaggio precedente. Il bootloader si assicurerà che solo il firmware firmato possa essere caricato sulla scheda.


### Come scoprire la versione del firmware


Accedere al menu `Impostazioni del dispositivo`, che mostrerà il numero di versione sotto il titolo della schermata.


## Utilizzare Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Sicurezza di Specter-DIY


### Hardware


Il display è controllato dall'MCU dell'applicazione.


L'integrazione dell'elemento sicuro non è ancora arrivata: al momento i segreti sono memorizzati anche sull'MCU principale. Tuttavia, è possibile utilizzare il wallet senza memorizzare il segreto: è necessario inserire ogni volta la frase di recupero. Perché ricordare a lungo il passphrase se si può ricordare l'intero mnemonico?


Il dispositivo utilizza una flash esterna per memorizzare alcuni file (QSPI), ma tutti i file utente sono firmati dal wallet e controllati al momento del caricamento.


La funzionalità di scansione QR è su un microcontrollore separato, quindi tutta l'elaborazione delle immagini avviene al di fuori dell'MCU critico per la sicurezza. Al momento l'USB e la scheda SD sono ancora gestite dall'MCU principale, quindi non utilizzate la scheda SD e l'USB se volete ridurre la superficie di attacco.


### Protezione PIN (autenticazione dell'utente)


Durante il primo avvio viene generato un segreto unico sulla MCU principale. Questo segreto consente di verificare che il dispositivo non sia stato sostituito da un dispositivo dannoso: quando si immette il codice PIN, viene visualizzato un elenco di parole che rimarranno invariate finché il segreto è presente.


Il codice PIN e il segreto univoco vengono utilizzati per ottenere una chiave di decrittografia per le chiavi Bitcoin (se memorizzate). Pertanto, se l'aggressore è in grado di bypassare la schermata del PIN, la decrittografia fallirà comunque.


Se si è bloccato il firmware (TODO: aggiungere qui il link alle istruzioni), si blocca anche il segreto, quindi se l'aggressore inserisce un firmware diverso nella scheda, il segreto viene cancellato e sarà possibile riconoscerlo quando si inizia a inserire il codice PIN: la sequenza di parole sarà diversa.


### Generazione della frase di recupero


Questa è una delle parti più importanti del wallet - per generate la chiave in modo sicuro. Per farlo bene, utilizziamo più fonti di entropia:



- TRNG del microcontrollore. Proprietario, certificato e probabilmente buono, ma non ci fidiamo
- Touchscreen. Ogni volta che si tocca lo schermo si misura la posizione e il momento in cui è avvenuto il tocco (in ticchettii del microcontrollore a 180 MHz).
- Microfoni integrati: non ancora. La scheda è dotata di due microfoni, in modo che l'hardware wallet possa ascoltare l'utente e aggiungere questi dati al pool di entropia.


Tutta questa entropia viene sottoposta a hashing e convertita nella vostra frase di recupero. L'entropia risultante è sempre migliore di quella delle singole fonti.


### Logica di alto livello - portafogli


Specter opera come deposito di chiavi. Contiene le chiavi private dell'HD che possono essere coinvolte nei portafogli. I portafogli sono definiti dai loro descrittori. Supportiamo anche i miniscritti.


Ogni wallet appartiene a una particolare rete. Ciò significa che se si è importato un wallet su `testnet` non sarà disponibile su `mainnet` o `regtest`; è necessario passare a questa rete e importare il wallet separatamente.


### Verifica delle transazioni


Le seguenti regole si applicano alle transazioni che il wallet firmerà:



- se vengono trovati input misti provenienti da portafogli diversi, l'utente viene avvertito ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- le uscite di modifica mostrano il nome del wallet a cui sono inviate
- per utilizzare un multisig o un miniscript è necessario importare il wallet aggiungendo il descrittore wallet (tramite QR, USB o scheda SD)


## Supporto dei descrittori


Tutti i normali descrittori di Bitcoin funzionano. A parte questo, abbiamo alcune estensioni:


### Rami multipli nei descrittori


Per risparmiare spazio nei codici QR, è possibile aggiungere descrittori con più rami in una sola volta. Se si desidera utilizzare `wpkh(xpub/0/*)` per gli indirizzi di ricezione e `wpkh(xpub/1/*)` per gli indirizzi di modifica, è possibile combinarli in un unico descrittore: `wpkh(xpub/{0,1}/*)` - il wallet tratterà il primo indice della parte di insieme `{}` come ramo per gli indirizzi di ricezione e il secondo come indirizzi di modifica.


È inoltre possibile specificare più di due rami e gli indici dei rami possono essere diversi per i diversi firmatari, quindi questo descrittore è molto strano ma assolutamente valido:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


In questo caso, per ricevere l'indirizzo numero 17 il wallet utilizzerà lo script di `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


L'unico requisito è che il numero di indici in tutti gli insiemi sia lo stesso (3 nel caso precedente).


### Derivazioni predefinite


Se il descrittore contiene chiavi pubbliche master ma non contiene derivazioni jolly, la derivazione predefinita `/{0,1}/*` verrà aggiunta a tutte le chiavi estese del descrittore. Se almeno una delle xpub ha una derivazione jolly, il descrittore non verrà modificato.


Il descrittore `wpkh(xpub)` sarà convertito in `wpkh(xpub/{0,1}/*)`.


### Miniscritto


Specter supporta i miniscript, ma non supporta la compilazione da policy a miniscript (perché è troppo costosa). Eseguiamo alcuni controlli sul miniscript, per cui solo gli script `B` sono ammessi al livello superiore e tutti gli argomenti nei sub-miniscript devono avere proprietà conformi a [spec](http://bitcoin.sipa.be/miniscript/).


È possibile utilizzare [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) per generate un descrittore da una politica e quindi importarlo nel wallet.


Ad esempio, una polizza "Posso spendere ora o tra 100 giorni mia moglie" può essere convertita in wallet in questo modo:


Politica: `o(9@pk(xpubA),and(older(14400),pk(B)))` (la mia chiave è 9 volte più probabile)


Miniscript: `or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Poiché qui non abbiamo derivazioni con caratteri jolly, le derivazioni predefinite di `/{0,1}/*` saranno aggiunte alle xpub.



---

Licenza MIT


Copyright (c) 2019 cryptoadvance


---
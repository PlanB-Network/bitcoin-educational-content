---
name: Nerdminer
description: Inizia a minare bitcoin con una probabilità di vincita vicina allo 0
---

![cover](assets/cover.jpeg)

> Configurazione del tuo NerdMiner_v2

In questo tutorial, ti guideremo attraverso i passaggi necessari per configurare un NerdMiner_v2, che è un dispositivo hardware (un ESP-32 S3) dedicato al mining di bitcoin.
Ovviamente la potenza di calcolo di un dispositivo del genere non può competere con gli ASIC dei minatori amatoriali o professionisti. Tuttavia, il NerdMiner è uno strumento didattico perfetto per rendere il mining di bitcoin concreto. E chissà, con (molta molta) fortuna, potresti trovare un blocco e la relativa ricompensa. Per i curiosi, vedremo nella sezione [Stima della probabilità di vincita](#stima-della-probabilita-di-vincita). In termini di consumo energetico, un NerdMiner consuma 0,5W; a titolo di confronto, una lampada a LED consuma in media 20 volte di più.

Prima di passare in rassegna i vari passaggi, elenchiamo l'hardware necessario per realizzarlo:

- un [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- un [alimentatore USB-C](https://amzn.eu/d/gIOot90)
- una custodia 3D: se hai una stampante 3D, puoi scaricare il [file 3D](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons), altrimenti puoi acquistarne uno sul [negozio online di Silexperience](https://silexperience.company.site/NerdMiner_V2-p544379757).
- un PC con Chrome Browser installato
- una connessione internet
- un indirizzo bitcoin

Puoi anche acquistare un kit NerdMiner già pre-assemblato da diversi rivenditori come:

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

Inizialmente, vedremo come flashare il software sull'ESP-32 S3, poi vedremo come riavviarlo per cambiare rete wifi. Questi passaggi sono destinati agli utenti Windows, se stai utilizzando un sistema operativo Linux, esegui le [preliminary steps](#preliminary-steps-for-linux-users) per consentire al tuo sistema di riconoscere l'ESP-32 S3.

# Installazione del software NerdMiner_v2

L'installazione del software è notevolmente semplificata grazie all'uso del webflasher.

## Passaggio 1: Preparazione del webflasher

Innanzitutto, devi accedere al [flasher NM2 online](https://bitmaker-hub.github.io/diyflasher/).

Quindi seleziona il firmware corrispondente al tuo ESP-32. Nella maggior parte dei casi è quello predefinito: il T-Display S3. Quindi clicca su "Flash".

> ⚠️ È importante che tu utilizzi il browser Chrome, poiché questo permette l'uso di flasher e l'accesso alle porte USB per impostazione predefinita.

![](assets/webflasher.png)

## Passo 2: Collegamento dell'ESP-32

Una volta avviato il webflasher, si aprirà una finestra popup che mostra le diverse porte USB riconosciute dal browser.
A questo punto, puoi collegare il tuo ESP-32 e verrà visualizzata una nuova porta (in questo caso, è la porta ttyACM0). Devi quindi selezionarla e fare clic su "connect".

![](assets/flasher-port-serial.png)

Il software verrà quindi scaricato sul tuo ESP32 in pochi secondi.

![](assets/NM2-sucessfully-installed.png)

## Passo 3: Configurazione del NerdMiner

La configurazione del tuo NerdMiner verrà effettuata tramite uno smartphone o un computer.
Attiva il WiFi e connettiti alla rete locale NerdMinerAP. Se stai utilizzando uno smartphone, verrà aperto automaticamente il portale di configurazione, altrimenti digita l'indirizzo 192.168.4.1 nel browser.
Quindi seleziona "Configure WiFi".

Ora puoi configurare il tuo Nerdminer.
Innanzitutto, connettiti alla tua rete WiFi, selezionando il nome della rete e inserendo la password associata.

Successivamente, puoi scegliere il pool di mining a cui desideri partecipare. Infatti, è comune nell'industria del mining di Bitcoin condividere la potenza di calcolo per aumentare le possibilità di trovare un blocco in cambio della condivisione della ricompensa proporzionalmente all'hashrate fornito.
Per i NerdMiner, puoi scegliere di connetterti a uno di questi pool:

| Pool URL          | Porta | URL                        | Stato                                         |
| ----------------- | ----- | -------------------------- | --------------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Pool di mining solo e open-source predefinito |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Mantenuto da CHMEX                            |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Mantenuto da djerfy                           |

Una volta scelto il tuo pool, devi inserire il tuo indirizzo Bitcoin per poter ricevere la ricompensa in caso (eccezionale) di un blocco trovato.

Seleziona anche il tuo fuso orario in modo che il NerdMiner possa mostrarti correttamente l'ora.
Ora puoi fare clic su "save".

![](assets/wifi-configuration.jpg)

Congratulazioni, ora fai parte della rete di mining di Bitcoin!

## Utilizzo del NerdMiner

Il software NerdMinerv2 ha 3 schermate diverse, alle quali puoi accedere facendo clic sul pulsante in alto a destra dello schermo:

- La schermata principale fornisce accesso alle statistiche del tuo NerdMiner.
- La seconda schermata fornisce accesso all'ora, all'hashrate, al prezzo del Bitcoin e all'altezza del blocco.
- Il terzo schermo fornisce accesso alle statistiche della rete mondiale di mining di bitcoin
  ![](assets/NM2-screens.png)

Se desideri riavviare il tuo NerdMiner, ad esempio per cambiare la rete WiFi, devi premere il pulsante superiore per 5 secondi.

Se premi una volta il pulsante inferiore, spegni il tuo NerdMiner. Premere due volte permette di invertire l'orientamento dello schermo.

### Passaggi preliminari per gli utenti Linux

Ecco i passaggi affinché Chrome possa rilevare la tua porta seriale su Linux.

1. Identifica la porta associata:

- Collega il tuo ESP-32 al tuo computer
- Apri un terminale
- Inserisci il seguente comando per elencare tutte le porte:
  - `dmesg | grep tty`
  - o `ls /dev/tty*`
- Per essere sicuri della porta, puoi procedere per eliminazione ripetendo il comando senza che l'ESP-32 sia collegato

2. Cambia i permessi della porta associata:

- Di default, l'accesso alle porte seriali potrebbe richiedere i permessi di root, quindi li renderemo disponibili aggiungendo il tuo utente al gruppo `dialout`
  - `sudo usermod -a -G dialout TUO_NOME_UTENTE`, sostituisci `TUO_NOME_UTENTE` con il tuo nome utente.
  - quindi disconnettiti e riconnettiti con questo utente, o riavvia il sistema per assicurarti che le modifiche al gruppo abbiano effetto.

Ora che il tuo ESP-32 è riconosciuto dal sistema, puoi tornare al [primo passaggio](#etape-1-preparation-du-webflasher) per l'installazione del software.

## Conclusioni

Ecco fatto! Il tuo NerdMiner_v2 è ora configurato e pronto per l'uso.

Buon mining e che la fortuna sia con te!

### Stima della probabilità di vincita

Divertiamoci a stimare la probabilità di vincere una ricompensa di blocco. Questa stima sarà approssimativa e mira solo a ottenere l'ordine di grandezza della probabilità.
Le pool a cui un NerdMiner può connettersi sono solo "pool di mining individuale", il che significa che la pool non mutualizza la potenza di hash di tutti i minatori connessi, ma agisce semplicemente come coordinatore.
Supponiamo ora che il nostro NerdMiner abbia una potenza di hash di circa 45kH/s.

Sapendo che la potenza di hash totale è di circa 450 EH/s (o $4.5 x 10^20$ hash al secondo), possiamo considerare che la probabilità di trovare il prossimo blocco sia di 1 su 100 milioni di miliardi, il che è molto molto molto improbabile che accada. Quindi, oltre ad essere uno strumento educativo e oggetto di curiosità, un NerdMiner può fungere da biglietto della lotteria nel mining di bitcoin a un costo elettrico marginale di 0,5 W - anche se, come abbiamo appena visto, la probabilità di vincita è ridicolmente bassa. Eppure, perché non sfidare la fortuna?

### Informazioni aggiuntive

Ecco alcuni link se desideri approfondire l'argomento:

- [Pagina del progetto NerdMiner_v2](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Documentazione completa di NerdMiners](https://docs.bitwater.ch/nerd-miner-v2/)

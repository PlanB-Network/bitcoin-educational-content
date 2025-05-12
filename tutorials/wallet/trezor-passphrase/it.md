---
name: passphrase BIP39 Trezor
description: Come faccio ad aggiungere un passphrase al mio portafoglio Trezor?
---
![cover](assets/cover.webp)



Un passphrase BIP39 è una password opzionale che, combinata con la frase Mnemonic, fornisce un ulteriore Layer di sicurezza per i portafogli Bitcoin deterministici e gerarchici. In questa esercitazione scopriremo insieme come impostare un passphrase sul vostro Bitcoin sicuro Wallet su un Trezor (Safe 3, Safe 5 e Model One).



![Image](assets/fr/01.webp)



Prima di iniziare questo tutorial, se non conoscete il concetto di passphrase, il suo funzionamento e le sue implicazioni per il vostro Bitcoin Wallet, vi consiglio vivamente di consultare quest'altro articolo teorico in cui spiego tutto (questo è molto importante, in quanto l'utilizzo di un passphrase senza averne compreso appieno il funzionamento può mettere a rischio i vostri bitcoin):



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Il passphrase su Trezor viene gestito nel modo classico se si è optato per lo standard BIP39 durante la configurazione (cosa che consiglio se non si ha bisogno di *Multi-share Backup*). La particolarità di Trezor è che è possibile inserire il passphrase direttamente sul Hardware Wallet, oppure tramite la tastiera del computer utilizzando il software Trezor Suite. Questa seconda opzione è notevolmente meno sicura, poiché il computer ha una superficie di attacco immensamente più ampia rispetto al Hardware Wallet. Tuttavia, la digitazione di un passphrase complesso è un'operazione che può essere eseguita in modo semplice e veloce. Tuttavia, la digitazione di un passphrase complesso può essere più veloce su una tastiera convenzionale che sul Hardware Wallet, il che potrebbe incoraggiare l'uso di passphrase forti. Quindi è sempre meglio usare un passphrase, anche se deve essere digitato, piuttosto che non usarlo affatto. È importante, tuttavia, rimanere consapevoli dell'aumento del rischio di attacchi numerici che ciò comporta.



Queste opzioni non sono disponibili su tutti i software di gestione del portafoglio compatibili con Trezor. Ad esempio, per il Modello Uno, il passphrase può essere inserito tramite la tastiera su Sparrow Wallet. Per i modelli Model T, Safe 3 e Safe 5, è necessario utilizzare Trezor Suite o inserire il passphrase direttamente su Hardware Wallet, poiché l'opzione di inserimento tramite Sparrow è stata disattivata da HWI alcuni anni fa.



![Image](assets/fr/02.webp)



In Trezor Suite, sono disponibili due modi diversi per gestire la domanda di passphrase. È possibile attivare l'opzione "*passphrase*" nella scheda "*Device*". Se attivata, Trezor Suite e tutti gli altri software di gestione del portafoglio chiederanno sistematicamente di inserire il passphrase a ogni avvio. Se si preferisce un approccio più discreto all'uso del passphrase, è possibile mantenere l'impostazione su "*Standard*". In questo caso, dovrete accedere manualmente al menu del vostro Hardware Wallet nell'angolo in alto a sinistra e fare clic sul pulsante "*+ passphrase*" ogni volta che lo avviate.



Prima di iniziare questa esercitazione, assicuratevi di aver già inizializzato il vostro Trezor e di aver generato la frase Mnemonic. Se non l'avete fatto e il vostro Trezor è nuovo, seguite l'esercitazione specifica per il modello Plan ₿ Network. Se non l'avete fatto e il vostro Trezor è nuovo, seguite l'esercitazione specifica per il modello disponibile sul sito Plan ₿ Network. Una volta completata questa fase, è possibile tornare a questa guida.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Aggiunta di un passphrase a un Safe 3 o Safe 5



Dopo aver creato il Wallet, salvato il Mnemonic e impostato un PIN, si accede al menu iniziale di Trezor Suite. Nell'angolo in alto a sinistra dovrebbe apparire una finestra che invita ad attivare il passphrase BIP39.



![Image](assets/fr/03.webp)



Se questa finestra non appare, è necessario attivare manualmente l'opzione "*passphrase*" nella scheda delle impostazioni "*Device*".



![Image](assets/fr/04.webp)



In questa finestra viene richiesto di inserire il proprio passphrase. Scegliete un passphrase forte e fate immediatamente un backup fisico, su un supporto come carta o metallo. In questo esempio, ho scelto il passphrase: `fH3&kL@9mP#2sD5qR!82`. Questo è un esempio; tuttavia, vi consiglio di scegliere un passphrase leggermente più lungo. Tra i 30 e i 40 caratteri sarebbe l'ideale (come una buona password).



naturalmente, non si deve mai condividere il proprio passphrase su Internet, come faccio io in questa esercitazione. Questo esempio di Wallet sarà usato solo sul Testnet e sarà cancellato alla fine del tutorial.**_



Per consigli più specifici sulla scelta del passphrase, vi invito ancora una volta a consultare quest'altro articolo:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Se si desidera inserire il proprio passphrase tramite la tastiera del computer, inserirlo nell'apposito campo, quindi fare clic su "*Accesso passphrase Wallet*".



![Image](assets/fr/05.webp)



Il Hardware Wallet visualizzerà quindi il passphrase. Assicurarsi che corrisponda al backup fisico (cartaceo o metallico) prima di fare clic sullo schermo per continuare.



![Image](assets/fr/06.webp)



In questo modo si potrà accedere al proprio portafoglio protetto da passphrase.



![Image](assets/fr/07.webp)



Se si preferisce aumentare la sicurezza inserendo il passphrase solo sul Trezor, quando viene richiesto, fare clic su "*Inserisci passphrase su Trezor*".



![Image](assets/fr/08.webp)



Sul Trezor apparirà una tastiera T9 che permetterà di inserire il passphrase. Una volta completata l'immissione, fare clic sul segno di spunta Green per applicare il passphrase al proprio Wallet.



![Image](assets/fr/09.webp)



A questo punto sarà possibile accedere al passphrase sicuro Wallet.



![Image](assets/fr/10.webp)



Per utilizzare Sparrow Wallet, la procedura è simile, ma per i modelli T, Safe 3 e Safe 5, il passphrase deve essere inserito sul Hardware Wallet e non tramite la tastiera del computer.



Ogni volta che Sparrow Wallet richiede l'accesso al vostro Trezor e passphrase non è ancora stato applicato dall'ultimo avvio, dovrete inserirlo utilizzando la tastiera T9.



![Image](assets/fr/11.webp)



## Aggiunta di un passphrase a un Modello Uno



Sul Model One, l'uso di un passphrase BIP39 è quasi indispensabile. Poiché questo dispositivo non incorpora un elemento sicuro, è relativamente facile estrarre informazioni sensibili. Non è quindi resistente agli attacchi fisici. Tuttavia, poiché il passphrase non rimane sul dispositivo dopo che è stato spento, l'uso di un passphrase forte (non bruteable) può proteggere dalla maggior parte degli attacchi fisici noti su questo modello.



Sul Model One, non è possibile inserire il passphrase direttamente sul Hardware Wallet. È necessario inserirlo tramite la tastiera del computer.



Dopo aver creato il Wallet, salvato il Mnemonic e impostato un PIN, si accede al menu iniziale di Trezor Suite. Nell'angolo in alto a sinistra dovrebbe apparire una finestra che invita ad attivare il passphrase BIP39.



![Image](assets/fr/12.webp)



Se questa finestra non appare, è necessario attivare l'opzione "*passphrase*" nella scheda "*Device*" delle impostazioni.



![Image](assets/fr/13.webp)



In questa finestra viene richiesto di inserire il proprio passphrase. Scegliete un passphrase forte e fate immediatamente un backup fisico, su un supporto come carta o metallo. In questo esempio, ho scelto il passphrase: `fH3&kL@9mP#2sD5qR!82`. Questo è solo un esempio; tuttavia, vi consiglio di scegliere un passphrase leggermente più lungo. L'ideale sarebbe una lunghezza compresa tra 30 e 40 caratteri (come una buona password).



Per consigli più specifici sulla scelta del passphrase, vi invito ancora una volta a consultare quest'altro articolo:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Immettere il proprio passphrase nell'apposito campo, quindi fare clic sul pulsante "*Accesso passphrase Wallet*".



![Image](assets/fr/14.webp)



Il Hardware Wallet visualizzerà il passphrase. Assicuratevi che corrisponda al vostro backup fisico (cartaceo o metallico), quindi fate clic sul pulsante di destra per continuare.



![Image](assets/fr/15.webp)



In questo modo si accede al portafoglio protetto da passphrase.



![Image](assets/fr/16.webp)



Per utilizzare Sparrow Wallet in seguito, la procedura rimane la stessa. Ogni volta che Sparrow richiede l'accesso al Hardware Wallet e il passphrase non è stato inserito dall'ultimo avvio del dispositivo, sarà necessario inserirlo.



![Image](assets/fr/17.webp)



Congratulazioni, ora siete aggiornati sull'uso del passphrase BIP39 sui portafogli hardware Trezor. Se volete fare un ulteriore passo avanti nella sicurezza del Wallet, date un'occhiata a questo tutorial sui sistemi di backup *multi-share* di Trezor (*sistema di condivisione segreta di Shamir*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Se avete trovato utile questa esercitazione, vi sarei grato se lasciaste un pollice Green qui sotto. Sentitevi liberi di condividere questo articolo sui vostri social network. Grazie mille!
---
name: BIP-39 passphrase SeedSigner
description: Come posso aggiungere un passphrase al mio portafoglio SeedSigner?
---

![cover](assets/cover.webp)



Un passphrase BIP39 è una password opzionale che, combinata con la frase Mnemonic, fornisce un ulteriore Layer di sicurezza per i portafogli Bitcoin deterministici e gerarchici. In questa esercitazione scopriremo insieme come impostare un passphrase sul vostro Bitcoin Wallet utilizzato con un SeedSigner.



![Image](assets/fr/01.webp)



## Prerequisiti prima di aggiungere un passphrase



Prima di iniziare questo tutorial, se non conoscete il concetto di passphrase, il suo funzionamento e le sue implicazioni per il vostro Bitcoin Wallet, vi consiglio vivamente di consultare quest'altro articolo teorico in cui spiego tutto (questo è molto importante, in quanto l'utilizzo di un passphrase senza averne compreso appieno il funzionamento può mettere a rischio i vostri bitcoin):



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Prima di iniziare questa esercitazione, assicuratevi di aver già inizializzato il vostro SeedSigner e di aver generato la frase Mnemonic. Se non l'avete fatto e il vostro SeedSigner è nuovo, seguite l'esercitazione su Plan ₿ Academy. Se non l'avete fatto e il vostro SeedSigner è nuovo di zecca, seguite il tutorial su Plan ₿ Academy. Una volta completata questa fase, si può tornare a questo tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Come si aggiunge un passphrase al SeedSigner?



L'aggiunta di un passphrase al portafoglio gestito tramite SeedSigner crea un portafoglio completamente nuovo, generando un set di chiavi completamente separato. Di conseguenza, se si dispone già di un portafoglio contenente Satss, non sarà più possibile accedervi con il passphrase, poiché genera un portafoglio completamente diverso.



Per applicare un passphrase al SeedSigner, accendere il dispositivo e scansionare il SeedQR come di consueto. Il SeedSigner visualizzerà l'impronta digitale del Wallet attuale, corrispondente a quello **senza passphrase**. Il Wallet con passphrase avrà un'impronta digitale diversa.



Fare clic sul pulsante "BIP-39 passphrase".



![Image](assets/fr/02.webp)



Inserite quindi il passphrase di vostra scelta nell'apposito campo, utilizzando la tastiera a schermo. Assicuratevi di effettuare uno o più backup fisici (cartacei o metallici): la perdita di questo passphrase comporterà la perdita permanente dell'accesso ai vostri bitcoin. **Per ripristinare un Wallet, sono indispensabili sia il Mnemonic che il passphrase ** Se uno dei due viene perso, i bitcoin saranno irrimediabilmente bloccati.



Una volta completata l'iscrizione, convalidarla premendo il pulsante `KEY3` in basso a destra di SeedSigner.



![Image](assets/fr/03.webp)



*In questo esempio, ho usato il passphrase `pba`. Tuttavia, nel vostro caso, assicuratevi di scegliere un passphrase robusto. Per sapere come definire un passphrase ottimale, consultate quest'altro articolo:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner visualizza quindi la nuova impronta digitale del passphrase Wallet. Fare diverse copie di questa impronta digitale: è importante quando si utilizza un Wallet con il passphrase, in quanto consente di verificare, ogni volta che si inserisce il passphrase, che non si siano commessi errori di battitura e che si stia accedendo al Wallet giusto.



Ad esempio, se nel mio caso scrivo erroneamente il passphrase `Pba` quando avvio il SeedSigner invece di `pba`, questo semplice cambiamento da minuscolo a maiuscolo porterà alla creazione di un portafoglio completamente diverso da quello a cui desidero accedere.



Questa impronta digitale non comporta alcun rischio per la sicurezza o la riservatezza del Wallet. Non rivela alcuna informazione, pubblica o privata, sulle chiavi. A differenza del Mnemonic e del passphrase, è possibile salvare l'impronta digitale su un supporto digitale. Si consiglia di conservarne una copia in diversi luoghi: su carta, in un gestore di password, ecc.



Una volta salvata l'impronta digitale, fare clic su "Fatto".



![Image](assets/fr/04.webp)



In questo modo avrete accesso a tutte le funzioni del vostro portafoglio, proprio come su un SeedSigner classico.



![Image](assets/fr/05.webp)



Ora è possibile importare il keystore nel Sparrow wallet e utilizzare il Wallet come di consueto. Ogni volta che si riavvia, è necessario eseguire la scansione del SeedQR e inserire nuovamente il passphrase con la tastiera, come abbiamo fatto qui.



Prima di utilizzare effettivamente il Wallet con il passphrase, si consiglia vivamente di eseguire un test di ripristino completo e vuoto. Ciò consentirà di confermare la validità della frase Mnemonic e dei backup passphrase. Per sapere come eseguire questo controllo, consultare la seguente esercitazione:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
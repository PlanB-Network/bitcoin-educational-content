---
name: BIP-39 Passphrase SeedSigner
description: Come posso aggiungere un passphrase al mio portafoglio SeedSigner?
---

![cover](assets/cover.webp)



Il passphrase BIP39 è una password opzionale che, insieme alla frase mnemonica, fornisce un ulteriore livello di sicurezza per i portafogli Bitcoin deterministici e gerarchici. In questo tutorial scopriremo insieme come impostare un passphrase sul vostro Bitcoin wallet utilizzato con un SeedSigner.



![Image](assets/fr/01.webp)



## Prerequisiti prima di aggiungere una passphrase



Prima di iniziare questo tutorial, se non conoscete il concetto di passphrase, il suo funzionamento e le sue implicazioni per il vostro Bitcoin wallet, vi consiglio vivamente di consultare quest'altro articolo teorico in cui spiego tutto (questo è molto importante, in quanto l'utilizzo di un passphrase senza averne compreso appieno il funzionamento può mettere a rischio i vostri bitcoin):



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Prima di iniziare questo tutorial, assicuratevi di aver già inizializzato il vostro SeedSigner e di aver generato la vostra frase mnemonica. Se non l'avete fatto e il vostro SeedSigner è nuovo, seguite il tutorial su Plan ₿ Academy. Una volta completata questa fase, si può tornare a questo tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Come si aggiunge un passphrase al SeedSigner?



L'aggiunta di un passphrase al vostro portafoglio gestito tramite SeedSigner crea un portafoglio completamente nuovo, generando un insieme di chiavi completamente separato. Di conseguenza, se si dispone già di un portafoglio contenente satss, non sarà più possibile accedervi con il passphrase, poiché genera un portafoglio completamente diverso.



Per applicare un passphrase al SeedSigner, accendere il dispositivo e scansionare il SeedQR come di consueto. Il SeedSigner visualizzerà l'impronta digitale del wallet attuale, corrispondente a quello **senza passphrase**. Il wallet con passphrase avrà un'impronta digitale diversa.



Fare clic sul pulsante `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



Inserite quindi il passphrase di vostra scelta nell'apposito campo, utilizzando la tastiera a schermo. Assicuratevi di effettuare uno o più backup fisici (cartacei o metallici): la perdita di questo passphrase comporterà la perdita permanente dell'accesso ai vostri bitcoin. **Per ripristinare un wallet, sia il mnemonico che il passphrase sono essenziali ** Se uno dei due viene perso, i bitcoin saranno irrimediabilmente bloccati.



Una volta completata l'iscrizione, convalidarla premendo il pulsante `KEY3` in basso a destra di SeedSigner.



![Image](assets/fr/03.webp)



*In questo esempio, ho usato il passphrase `pba`. Tuttavia, nel vostro caso, assicuratevi di scegliere un passphrase robusto. Per sapere come definire un passphrase ottimale, consultate quest'altro articolo:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Il SeedSigner visualizza quindi la nuova impronta digitale del passphrase wallet. Fare diverse copie di questa impronta digitale: è importante quando si utilizza un wallet con il passphrase, in quanto consente di verificare, ogni volta che si inserisce il passphrase, che non si siano commessi errori di battitura e che si stia accedendo al wallet giusto.



Ad esempio, se nel mio caso scrivo erroneamente il passphrase `Pba` quando avvio il SeedSigner invece di `pba`, questo semplice cambiamento da minuscolo a maiuscolo porterà alla creazione di un portafoglio completamente diverso da quello a cui voglio accedere.



Questa impronta digitale non comporta alcun rischio per la sicurezza o la riservatezza del wallet. Non rivela alcuna informazione, pubblica o privata, sulle chiavi. Quindi, a differenza del mnemonico e del passphrase, è possibile salvare l'impronta digitale su un supporto digitale. Vi consiglio di conservarne una copia in diversi luoghi: su un foglio di carta, in un gestore di password, ecc.



Una volta salvata l'impronta digitale, fare clic su "Fatto".



![Image](assets/fr/04.webp)



In questo modo avrete accesso a tutte le funzioni del vostro portafoglio, proprio come su un SeedSigner classico.



![Image](assets/fr/05.webp)



Ora è possibile importare il keystore nel Sparrow Wallet e utilizzare il wallet come di consueto. Ogni volta che si riavvia, è necessario eseguire la scansione del SeedQR e reinserire il passphrase con la tastiera, come abbiamo fatto qui.



Prima di utilizzare il wallet con il passphrase, consiglio vivamente di eseguire un test di ripristino completo e vuoto. In questo modo si potrà confermare che i backup della frase mnemonica e del passphrase sono validi. Per sapere come eseguire questo controllo, consultate la seguente esercitazione:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
---
name: Blockstream Green - Mobile
description: Impostazione di un software wallet mobile
---
![cover](assets/cover.webp)

Un software wallet è un'applicazione installata su un computer, uno smartphone o un altro dispositivo connesso a Internet, che consente di gestire e proteggere le chiavi del wallet Bitcoin. A differenza degli hardware wallet, che isolano le chiavi private, i wallet "hot" operano in un ambiente potenzialmente esposto agli attacchi informatici, aumentando il rischio di pirateria e furto.

Questo tipo di wallet dovrebbe essere utilizzato per gestire quantità ragionevoli di bitcoin, soprattutto per le transazioni quotidiane. Possono anche essere un'opzione interessante per le persone con un patrimonio limitato di bitcoin, per le quali l'investimento in un hardware wallet può sembrare sproporzionato. La loro costante esposizione a Internet li rende tuttavia meno sicuri per la conservazione di risparmi a lungo termine o di grandi fondi. Per questi ultimi è meglio optare per soluzioni più protette, come gli hardware wallet.

In questo tutorial, vorrei presentarti una delle migliori soluzioni di software wallet per dispositivi mobili: **Blockstream Green**.

![GREEN](assets/fr/01.webp)

Se desideri scoprire come utilizzare Blockstream Green sul tuo computer, consulta quest'altra guida:

https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

## Introduzione a Blockstream Green

Blockstream Green è un wallet disponibile per mobile e desktop. Precedentemente noto come _Green Address_, questo wallet è diventato un progetto di Blockstream in seguito alla sua acquisizione nel 2016.

Green è un'applicazione particolarmente facile da usare, il che la rende interessante per i principianti. Offre tutte le caratteristiche essenziali che deve avere un buon wallet Bitcoin, tra cui RBF (_Replace-by-Fee_), l'opzione per connettersi tramite Tor, la possibilità di collegare il proprio nodo, SPV (_Simple Payment Verification_), etichettatura degli UTXO e coin control.

Blockstream Green supporta anche la rete Liquid, una sidechain di Bitcoin sviluppata da Blockstream per transazioni veloci e riservate, che avvengono al di fuori della blockchain principale. Questo tutorial si concentra esclusivamente sul funzionamento di Green nella rete Bitcoin, uno successivo tratterà l'uso con Liquid.

## Installazione e configurazione di Blockstream Green

Il primo passo è ovviamente quello di scaricare l'applicazione Green. Vai nel tuo store per scaricarlo

- [Per Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Per Apple](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).
![GREEN](assets/fr/02.webp)

Per gli utenti Android, è possibile installare l'applicazione anche tramite il file `.apk` [disponibile su GitHub di Blockstream](https://github.com/Blockstream/green_android/releases).

![GREEN](assets/fr/03.webp)

Avvia l'applicazione, quindi seleziona la casella "_Accetto le condizioni..._".

![GREEN](assets/fr/04.webp)

Quando si apre Green per la prima volta, la schermata iniziale appare senza un wallet configurato. In seguito, se si creano o importano wallet, appariranno in questa interfaccia. Prima di procedere alla creazione di un wallet, ti consiglio di cominciare dalle impostazioni dell'applicazione, in base alle tue esigenze. Clicca su "App Settings".

![GREEN](assets/fr/05.webp)

L'opzione "Enhanced Privacy", disponibile solo su Android, migliora la privacy disabilitando gli screenshot e nascondendo le anteprime delle applicazioni. Inoltre, blocca automaticamente l'accesso alle applicazioni non appena il telefono si blocca, rendendo più difficile l'esposizione dei dati.

![GREEN](assets/fr/06.webp)

Per coloro che desiderano migliorare la propria privacy, Green offre la possibilità di instradare il traffico tramite Tor, una rete che cripta tutte le connessioni e rende le attività difficili da rintracciare. Sebbene questa opzione possa rallentare leggermente il funzionamento dell'applicazione, è altamente consigliata per proteggere la tua privacy, soprattutto se non utilizzi un tuo nodo.

![GREEN](assets/fr/07.webp)

Per gli utenti che dispongono di un proprio full node, Green Wallet offre la possibilità di collegarsi ad esso tramite un server Electrum, garantendo il controllo totale sulle informazioni della rete Bitcoin e sulla propagazione delle transazioni.

![GREEN](assets/fr/08.webp)

<<<<<<< Updated upstream
Un'altra funzione alternativa è l'opzione "_SPV Verification_", che consente di verificare direttamente alcuni dati della blockchain e quindi ridurre la necessità di fidarsi del nodo predefinito di Blockstream, anche se questo metodo non fornisce tutte le garanzie di un full node.

![GREEN](assets/fr/09.webp)

Dopo aver regolato le impostazioni in base alle tue esigenze, fai clic sul pulsante "_Save_" e riavvia l'applicazione.
=======
Un'altra funzione alternativa è l'opzione "*SPV Verification*", che consente di verificare direttamente alcuni dati della blockchain e quindi ridurre la necessità di fidarsi del nodo predefinito di Blockstream, anche se questo metodo non fornisce tutte le garanzie di un full node.

![GREEN](assets/fr/09.webp)

Dopo aver regolato le impostazioni in base alle tue esigenze, fai clic sul pulsante "*Save" e riavvia l'applicazione.
>>>>>>> Stashed changes

![GREEN](assets/fr/10.webp)

## Creare un wallet Bitcoin con Blockstream Green

<<<<<<< Updated upstream
Ora sei pronto a creare un wallet Bitcoin. Fai clic sul pulsante "_Get Started_".

![GREEN](assets/fr/11.webp)

Puoi scegliere tra la creazione di un software wallet locale o la gestione di un wallet cold tramite un dispositivo hardware. Per questo tutorial ci concentreremo sulla creazione di un wallet hot, quindi dovrai selezionare l'opzione "On This Device". In una prossima guida ti mostrerò come utilizzare l'altra opzione.
=======
Ora sei pronto a creare un wallet Bitcoin. Fare clic sul pulsante "*Get Started*".

![GREEN](assets/fr/11.webp)

Puoiscegliere tra la creazione di un software wallet locale o la gestione di un wallet cold tramite un dispositivo hardware. Per questo tutorial ci concentreremo sulla creazione di un wallet hot, quindi dovrai selezionare l'opzione "On This Device". In una prossima guida ti mostrerò come utilizzare l'altra opzione.
>>>>>>> Stashed changes

L'opzione "_Watch-only_", invece, consente di importare una chiave pubblica estesa (`xpub`) per visualizzare le transazioni di un wallet senza poter spendere i fondi associati, il che è utile per monitorare un wallet su un dispositivo hardware, ad esempio.

![GREEN](assets/fr/12.webp)

Si può quindi scegliere di ripristinare un wallet esistente o di crearne uno nuovo. Ai fini di questa guida, creeremo un nuovo wallet. Tuttavia, se hai bisogno di ripristinare un wallet Bitcoin esistente dalla sua frase mnemonica, ad esempio in seguito alla perdita del dispositivo hardware, dovrai scegliere la seconda opzione.

![GREEN](assets/fr/13.webp)

È possibile scegliere tra una mnemonica di 12 o 24 parole. Questa ti permetterà di recuperare l'accesso al wallet da qualsiasi software compatibile in caso di problemi con il tuo telefono. Attualmente, la scelta di una mnemonica di 24 parole non offre maggiore sicurezza di una di 12 parole. Ti consiglio quindi di scegliere una frase mnemonica di 12 parole.

<<<<<<< Updated upstream
Green ti mostrerà la frase mnemonica. Prima di continuare, assicurati di non essere osservato. Clicca su "_Show Recovery Phrase_" per visualizzarla sullo schermo.

![GREEN](assets/fr/14.webp)

**Questa mnemonica dà accesso completo e illimitato a tutti i tuoi bitcoin**. Chiunque sia in possesso di queste parole può rubare i tuoi fondi, anche senza accedere fisicamente al tuo dispositivo.

Le parole consentono l'accesso ai bitcoin in caso di perdita, furto o rottura del telefono. È quindi molto importante eseguire un backup accurato **su un supporto fisico (non digitale)** e conservarlo in un luogo sicuro. Puoi scriverlo su un foglio di carta o, per maggiore sicurezza, se si tratta di un wallet di grandi dimensioni, ti consiglio di incidere le parole su un supporto in acciaio inossidabile, per proteggerlo dal rischio di incendi, allagamento o crolli (per un wallet hot progettato per proteggere una piccola quantità di bitcoin, un semplice backup cartaceo è probabilmente sufficiente).
=======
Green ti mostrerà la frase mnemonica. Prima di continuare, assicurateti di non essere osservato. Clicca su "_Show Recovery Phrase_" per visualizzarla sullo schermo.

![GREEN](assets/fr/14.webp)

**Questa mnemonica dà accesso completo e illimitato a tutti i tuoi bitcoin **. Chiunque sia in possesso di queste parole, può rubare i tuoi fondi, anche senza accedere fisicamente al tuo dispositivo.

Le parole consentono l'accesso ai bitcoin in caso di perdita, furto o rottura del telefono. È quindi molto importante eseguire un backup accurato **su un supporto fisico (non digitale)** e conservarlo in un luogo sicuro. Puoi scriverlo su un foglio di carta o, per maggiore sicurezza, se si tratta di un portafoglio di grandi dimensioni, ti consiglio di incidere le parole su un supporto in acciaio inossidabile, per proteggerlo dal rischio di incendi,o allagamento o crolli (per un wallet hot progettato per proteggere una piccola quantità di bitcoin, un semplice backup cartaceo è probabilmente sufficiente).
>>>>>>> Stashed changes

_Ovviamente, non devi mai condividere queste parole su Internet, come faccio io in questo tutorial. Questo wallet di esempio sarà utilizzato solo su Testnet e sarà cancellato alla fine del tutorial._

![GREEN](assets/fr/15.webp)

<<<<<<< Updated upstream
Dopo aver scritto correttamente la frase mnemonica su un supporto fisico, clicca su su "_Continue_". Green Wallet ti chiederà di confermare alcune parole della mnemonica per assicurarsi che siano state trascritte correttamente. Riempi gli spazi vuoti con le parole mancanti.
=======
Dopo aver scritto correttamente la frase mnemonica su un supporto fisico, clicca su su _Continue_". Green Wallet ti chiederà di confermare alcune parole della mnemonica per assicurarsi che siano state trascritte correttamente. Riempi gli spazi vuoti con le parole mancanti.
>>>>>>> Stashed changes

![GREEN](assets/fr/16.webp)

Scegli un PIN a sei cifre per il dispositivo, che verrà utilizzato per sbloccare Green. Si tratta di una protezione contro l'accesso fisico non autorizzato. Il PIN non concorre alla creazione delle chiavi crittografiche del wallet. Anche senza questo PIN, il possesso della frase mnemonica di 12 o 24 parole ti permetterà di riavere accesso ai fondi associati ad esso.

<<<<<<< Updated upstream
Ti consiglio di scegliere un PIN di 6 cifre che sia il più casuale possibile. Assicurati di salvare questo PIN per non dimenticarlo, altrimenti sarai costretto a recuperare il wallet dalla mnemonica. È possibile aggiungere un'opzione per il blocco biometrico, per evitare di dover inserire il PIN ogni volta che lo si utilizza. In generale, il biometrico è molto meno sicuro del PIN stesso. Pertanto, per impostazione predefinita, ti consiglio di non usare questa opzione per lo sblocco.
=======
Ti consiglio di scegliere un PIN di 6 cifre che sia il più casuale possibile. Assicurati di salvare questo PIN per non dimenticarlo, altrimenti sarai costretto a recuperare il wallet dalla mnemonica. È possibile aggiungere un'opzione per il blocco biometrico, per evitare di dover inserire il PIN ogni volta che lo si utilizza. In generale, lil biometrico è molto meno sicuro del PIN stesso. Pertanto, per impostazione predefinita, ti consiglio di non impostare questa opzione per lo sblocco.
>>>>>>> Stashed changes

![GREEN](assets/fr/17.webp)

Immetti il PIN una seconda volta per confermarlo.

![GREEN](assets/fr/18.webp)

<<<<<<< Updated upstream
Attendi la creazione del wallet, quindi fai clic sul pulsante "_Create an account_".

![GREEN](assets/fr/19.webp)

Adesso puoi scegliere tra un wallet standard singlesig, che utilizzeremo in questo tutorial, o un wallet protetto da autenticazione a due fattori (2FA).

![GREEN](assets/fr/20.webp)

L'opzione 2FA su Green crea un wallet multifirma 2di2, con una chiave detenuta da Blockstream. Ciò significa che per effettuare una transazione sono necessarie entrambe le chiavi: una chiave locale protetta dal codice PIN sul telefono e una chiave remota protetta dall'autenticazione 2FA sui server di Blockstream. In caso di perdita dell'accesso all'autenticazione 2FA o di indisponibilità dei servizi di Blockstream, i meccanismi di recupero basati su script time-lock, garantiscono il recupero autonomo dei fondi. Sebbene questa configurazione riduca notevolmente il rischio di furto dei tuoi bitcoin, è più complessa da gestire e dipende in parte da Blockstream. Per questo tutorial, opteremo per un wallet classico singlesig, con le chiavi memorizzate localmente sul telefono.
=======
Attendi la creazione del wallet, quindi fare clic sul pulsante "_Create an account_".

![GREEN](assets/fr/19.webp)

Adesso puoi scegliere tra un wallet standard a singlesig, che utilizzeremo in questo tutorial, o un wallet protetto da autenticazione a due fattori (2FA).

![GREEN](assets/fr/20.webp)

L'opzione 2FA su Green crea un wallet multifirma 2di2, con una chiave detenuta da Blockstream. Ciò significa che per effettuare una transazione sono necessarie entrambe le chiavi: una chiave locale protetta dal codice PIN sul telefono e una chiave remota protetta dall'autenticazione 2FA sui server di Blockstream. In caso di perdita dell'accesso all'autenticazione 2FA o di indisponibilità dei servizi di Blockstream, i meccanismi di recupero basati su time-loc script, garantiscono il recupero autonomo dei fondi. Sebbene questa configurazione riduca notevolmente il rischio di furto dei tuoi bitcoin, è più complessa da gestire e dipende in parte da Blockstream. Per questo tutorial, opteremo per un wallet classico singlesig, con le chiavi memorizzate localmente sul telefono.
>>>>>>> Stashed changes

Il tuo wallet è stato creato con l'applicazione Green!

![GREEN](assets/fr/21.webp)

<<<<<<< Updated upstream
Prima di ricevere i primi bitcoin nel tuo wallet, **ti consiglio vivamente di eseguire un test di recupero finché è vuoto**. Prendi nota di alcune informazioni di riferimento, come la xpub o il primo indirizzo di ricezione, quindi cancella il wallet dall'app Green, mentre è ancora vuoto. In seguito prova a ripristinare il wallet su Green utilizzando il backup cartaceo. Verifica che le informazioni del cookie generate dopo il ripristino corrispondano a quelle annotate in origine. Se è così, puoi essere certo che il tuo backup cartaceo è affidabile. Per saperne di più su come effettuare un ripristino di prova, consulta quest'altro tutorial:
=======
Prima di ricevere i primi bitcoin nel tuo wallet, **ti consiglio vivamente di eseguire un test di recupero finché è vuoto**. Prendi nota di alcune informazioni di riferimento, come la xpub o il primo indirizzo di ricezione, quindi cancella il wallet dall'app Green, mentre è ancora vuoto. Quindi prova a ripristinare il wallet su Green utilizzando il backup cartaceo. Verifica che le informazioni del cookie generate dopo il ripristino corrispondano a quelle annotate in origine. Se è così, puoi essere certo che il tuo backup cartaceo è affidabile. Per saperne di più su come effettuare un ripristino di prova, consulta quest'altro tutorial:
>>>>>>> Stashed changes

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Impostazione del wallet su Blockstream Green

Se desideri personalizzare il tuo wallet, clicca sui tre puntini in alto a destra.

![GREEN](assets/fr/22.webp)

L'opzione "_Rename_" consente di personalizzare il nome del wallet, particolarmente utile se si gestiscono diversi wallet sulla stessa applicazione.

![GREEN](assets/fr/23.webp)

<<<<<<< Updated upstream
Il menu "_Unit_" consente di modificare l'unità di base del wallet. Si può scegliere di visualizzarlo in satoshi oppure in bitcoin.
=======
Il menu "*Unit*" consente di modificare l'unità di base del wallet. Si può scegliere di visualizzarlo in satoshi oppure in bitcoin.
>>>>>>> Stashed changes

![GREEN](assets/fr/24.webp)

Il menu "_Settings_" consente di accedere alle varie opzioni del wallet Bitcoin.

![GREEN](assets/fr/25.webp)

Qui, ad esempio, si trova la chiave pubblica estesa e il suo _descriptor_, utile se si intende impostare un wallet in modalità watch-only.

![GREEN](assets/fr/26.webp)

È inoltre possibile modificare il PIN del wallet e attivare l'accesso con il biometrico.

![GREEN](assets/fr/27.webp)

## Usare Blockstream Green

Ora che il tuo wallet è stato configurato, sei pronto a ricevere i tuoi primi sats! Basta cliccare sul pulsante "_Receive_".

![GREEN](assets/fr/28.webp)

<<<<<<< Updated upstream
Green visualizzerà quindi il primo indirizzo di ricezione vuoto del wallet. È possibile scansionare il QR code associato o copiare direttamente l'indirizzo per ricevere bitcoin. Questo tipo di indirizzo non specifica l'importo che il mittente deve inviare. È tuttavia possibile generare un indirizzo che richieda un importo specifico, facendo clic sui tre puntini in alto a destra, quindi su "_Request Amount_" e inserendo l'importo desiderato.
=======
Green visualizzerà quindi il primo indirizzo di ricezione vuoto del wallet. È possibile scansionare il QR code associato o copiare direttamente l'indirizzo per inviare bitcoin. Questo tipo di indirizzo non specifica l'importo che il mittente deve inviare. È tuttavia possibile generare un indirizzo che richieda un importo specifico, facendo clic sui tre puntini in alto a destra, quindi su "_Request Amount_" e inserendo l'importo desiderato.
>>>>>>> Stashed changes

Poiché stai usando un account Segwit v0 (BIP84), il tuo indirizzo inizierà con `bc1q...`. Nel mio esempio, sto usando un wallet Testnet, quindi il prefisso è leggermente diverso.

![GREEN](assets/fr/29.webp)

Quando la transazione viene propagata alla rete, appare nel tuo wallet.

![GREEN](assets/fr/30.webp)

Aspetta di aver ricevuto un numero sufficiente di conferme per considerare la transazione definitiva.

![GREEN](assets/fr/31.webp)

Con i bitcoin nel tuo wallet, ora puoi anche spendere. Clicca su "_Send_".

![GREEN](assets/fr/32.webp)

Nella pagina successiva, inserisci l'indirizzo del destinatario. È possibile inserirlo manualmente o scansionando un QR code.

![GREEN](assets/fr/33.webp)

Imposta l'importo del pagamento.

![GREEN](assets/fr/34.webp)

<<<<<<< Updated upstream
La parte inferiore della schermata è dedicata all'impostazione delle fee. È possibile scegliere se seguire le raccomandazioni dell'applicazione o personalizzare l'importo. Più alte sono le fee rispetto alle altre transazioni in attesa, più veloce sarà l'elaborazione della transazione. Per informazioni sul funzionamento delle fee, visita [Mempool.space](https://mempool.space/) nella sezione "_Transaction Fees_".
=======
Nella parte inferiore della schermata è possibile selezionare lle fee per questa transazione. È possibile scegliere se seguire le raccomandazioni dell'applicazione o personalizzare le fee. Più alte sono le fee rispetto alle altre transazioni in attesa, più veloce sarà l'elaborazione della transazione. Per informazioni sul funzionamento delle fee, visita [Mempool.space](https://mempool.space/) nella sezione "_Transaction Fees_".
>>>>>>> Stashed changes

![GREEN](assets/fr/35.webp)

Clicca su "_Next_" per accedere alla schermata di riepilogo della transazione. Verifica che l'indirizzo, l'importo e le fee siano corretti.

![GREEN](assets/fr/36.webp)

Se tutto va bene, muovi verso destra il pulsante verde in fondo allo schermo per firmare e propagare la transazione sulla rete Bitcoin.

![GREEN](assets/fr/37.webp)

La transazione apparirà ora sulla dashboard del tuo wallet, in attesa di conferma.

![GREEN](assets/fr/38.webp)

<<<<<<< Updated upstream
_Questo tutorial si basa su [una versione originale appartenente a Bitstack](https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet) scritta da Loïc Morel. Bitstack è una neo-banca Bitcoin francese, che offre la possibilità di risparmiare in bitcoin, sia in DCA (Dollar Cost Averaging), sia attraverso un sistema di arrotondamento automatico per le spese giornaliere._
=======
_Questo tutorial si basa su [una versione originale appartenente a Bitstack](https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet) scritta da Loïc Morel. Bitstack è una neo-banca Bitcoin francese, che offre la possibilità di risparmiare in bitcoin, sia in DCA (Dollar Cost Averaging), sia attraverso un sistema di arrotondamento automatico per le spese giornaliere._
>>>>>>> Stashed changes

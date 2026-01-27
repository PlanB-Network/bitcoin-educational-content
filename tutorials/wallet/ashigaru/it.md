---
name: Ashigaru
description: Il fork di Samourai Wallet per proteggere, gestire e miscelare i bitcoin
---

![cover](assets/cover.webp)



Ashigaru è un'applicazione Bitcoin mobile wallet che segue il progetto Samourai Wallet, ma in una nuova forma. Questo software è nato in un contesto particolare: nell'aprile 2024, i fondatori di Samourai Wallet sono stati arrestati dalle autorità americane e i loro server sono stati sequestrati. Sebbene l'applicazione Samurai sia rimasta utilizzabile, attualmente non viene più mantenuta. Ashigaru è una versione gratuita per fork di Samurai Wallet, mantenuta da un team anonimo per garantire la continuità delle funzionalità di Samurai e salvaguardare la sua filosofia originaria: difendere la privacy e la sovranità degli utenti di Bitcoin.



Ashigaru riprende molto del DNA di Samourai: un'interfaccia simile, un approccio ovviamente autocustodiale, l'open source e l'attenzione alla privacy. Il codice è distribuito sotto la licenza GNU GPLv3, che garantisce che chiunque possa controllare, modificare o ridistribuire il software.



L'applicazione Ashigaru integra una serie di strumenti avanzati per la riservatezza e la gestione dei vostri UTXO:




- Whirlpool**, un protocollo di coinjoin basato su Zerolink, che consente di interrompere i legami deterministici tra le entrate e le uscite delle transazioni, senza perdere la sovranità sui propri fondi.
- PayNym**, che implementa codici di pagamento riutilizzabili (BIP47), ora rappresentati tramite un sistema di avatar "*Pepehash*".
- Ricochet**, una funzione che aggiunge salti intermedi alle transazioni per renderle più difficili da tracciare.
- E naturalmente ***Coin Control*** per selezionare, congelare ed etichettare con precisione gli UTXO.
- Batch Spending***, per ridurre i costi raggruppando diversi pagamenti in un'unica transazione.
- La modalità **Stealth**, che nasconde l'applicazione sul cellulare dietro un launcher fittizio per passare inosservata durante un'ispezione fisica del telefono.
- Strumenti di spesa avanzati per ottimizzare la vostra riservatezza (payjoin, stonewall...).
- Un sistema di recupero ottimizzato che utilizza la passphrase BIP39.
- Un sistema per ottimizzare automaticamente la scelta delle commissioni di transazione.



![Image](assets/fr/01.webp)



Ashigaru si rivolge quindi agli utenti consapevoli delle problematiche legate alla tracciabilità delle transazioni su Bitcoin. Che siate utenti attenti alla privacy, bitcoiner esperti impegnati nell'autocustodia o individui esposti ai rischi di una maggiore sorveglianza, questa applicazione per il wallet vi fornisce gli strumenti necessari per riprendere il controllo della vostra attività sul Bitcoin.



Ashigaru è disponibile in versione mobile tramite la sua applicazione, che esploreremo in questo tutorial. Ma può essere utilizzato anche sul PC con ***Ashigaru Terminal***, che presenteremo in un prossimo tutorial.



![Image](assets/fr/02.webp)



In questo tutorial, vorrei introdurvi all'uso di base di Ashigaru: installazione, connessione al Dojo, backup, ricezione e invio di bitcoin. Gli strumenti avanzati saranno presentati in altri tutorial dedicati.



## 1. Prerequisiti per Ashigaru



L'applicazione richiede alcuni prerequisiti per funzionare correttamente. Innanzitutto, non è un'applicazione disponibile sui classici store come Google Play Store o App Store. Si installa manualmente sul telefono solo dal suo file `.apk`, scaricabile tramite la rete Tor. Pertanto, se si utilizza un iPhone, questo metodo non funziona: è necessario un dispositivo Android.



Per scaricare il file `.apk` tramite Tor, è necessario un browser in grado di accedere ai siti `.onion`. Il modo più semplice è installare l'applicazione Tor Browser sul proprio telefono, disponibile sul [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) o direttamente [tramite il suo `.apk`](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



La maggior parte degli smartphone recenti blocca per impostazione predefinita l'installazione di applicazioni provenienti da fonti sconosciute. È necessario attivare temporaneamente questa opzione per Tor Browser nelle impostazioni del dispositivo per consentirne l'installazione. Una volta installata l'applicazione, ricordatevi di disattivare questa funzione per rafforzare la sicurezza del vostro telefono.



Un altro prerequisito essenziale per l'utilizzo di Ashigaru è un nodo Bitcoin Dojo. Per motivi di sicurezza e sovranità, il team di Ashigaru non gestisce un server centralizzato a cui collegare la vostra applicazione. Dovrete quindi gestire la vostra istanza di Dojo o collegarvi a una istanza fidata.



Il Dojo consente all'applicazione Ashigaru di consultare le informazioni della blockchain, visualizzare i saldi degli indirizzi e trasmettere le transazioni sulla rete Bitcoin.



Per saperne di più su Dojo e imparare a installarlo, vi invito a seguire questo tutorial dedicato:



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Se proprio non potete permettervi di gestire un vostro Dojo, potete trovare persone disposte a condividere gratuitamente la loro istanza su [dojobay.pw](https://www.dojobay.pw/mainnet/). Questa può essere una soluzione temporanea, ma a lungo termine vi consiglio di usare il vostro Dojo per garantire la vostra sovranità e riservatezza.



## 2. Controllare e installare l'applicazione Ashigaru



### 2.1. Scaricare l'applicazione Ashigaru



Sul telefono, aprire Tor Browser e andare su [il sito ufficiale di Ashigaru](https://ashigaru.rs/download/), nella sezione `Download`. Quindi fare clic sul pulsante `Download for Android` per scaricare il file di installazione.



![Image](assets/fr/04.webp)



Prima di installare l'applicazione sul dispositivo, ne verificheremo l'autenticità e l'integrità. Si tratta di un passaggio molto importante, soprattutto quando si installa un'applicazione direttamente da un file `.apk'.



### 2.2. Controllare l'applicazione Ashigaru



Tornare al [sito ufficiale di Ashigaru](https://ashigaru.rs/download/) nella sezione `Download`, quindi copiare il messaggio visualizzato sotto il titolo `SHA-256 Hash del file APK`. Copiare l'intero blocco, da `BEGIN PGP SIGNED MESSAGE` a `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Sempre dal telefono, aprite una nuova scheda in Tor Browser e andate a [lo strumento di verifica di Keybase](https://keybase.io/verify). Incollate il messaggio appena copiato nell'apposito campo, quindi fate clic sul pulsante "Verifica".



![Image](assets/fr/06.webp)



Se la firma è autentica, Keybase visualizzerà un messaggio che conferma che il file è stato firmato dagli sviluppatori di Ashigaru. È inoltre possibile fare clic sul profilo `ashigarudev` indicato da Keybase e verificare che l'impronta digitale della chiave corrisponda esattamente a : `A138 06B1 FA2A 676B`.



Tuttavia, se in questa fase compare un errore, significa che la firma non è valida. In questo caso, **non installare l'APK**. Ricominciare dall'inizio o chiedere aiuto alla comunità prima di continuare.



![Image](assets/fr/07.webp)



Keybase vi ha fornito l'hash dell'applicazione. Verifichiamo ora che l'hash del file `.apk' scaricato corrisponda a quello verificato su Keybase. Per farlo, andate su [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Fate clic sul pulsante `BROWSE...` e selezionate il file `.apk` scaricato al punto 2.1.


Scegliere quindi la funzione hash `SHA-256` e fare clic su `CALCOLA HASH` per calcolare l'hash del file.



![Image](assets/fr/09.webp)



Il sito visualizzerà l'hash del vostro file `.apk`. Confrontatelo con l'hash verificato su Keybase.io. Se i due hash sono identici, la verifica dell'autenticità e dell'integrità ha avuto successo. A questo punto è possibile procedere all'installazione dell'applicazione.



![Image](assets/fr/10.webp)



### 2.3. installare l'applicazione Ashigaru



Per installare l'applicazione, aprire il file manager del telefono e andare alla cartella dei download. Quindi fare clic sul file `.apk` appena controllato e confermare l'installazione quando richiesto.



![Image](assets/fr/11.webp)



Ashigaru è ora installato sul vostro telefono.



## 3. Inizializzare l'applicazione e creare un portafoglio Bitcoin



Quando si avvia l'applicazione per la prima volta, selezionare `MAINNET`.



![Image](assets/fr/12.webp)



Quindi fare clic su "Inizia".



![Image](assets/fr/13.webp)



Ora creeremo un nuovo portafoglio Bitcoin. Premere il pulsante "Crea un nuovo wallet".



![Image](assets/fr/14.webp)



### 3.1. creare un portafoglio Bitcoin



Ashigaru richiede un passphrase BIP39. Scegliete il vostro passphrase e inseritelo nei campi appropriati. Deve essere il più lungo e casuale possibile per resistere a un attacco di forza bruta.



Eseguire immediatamente un backup fisico di questo passphrase. Si tratta di un passo molto importante: in caso di smarrimento del telefono, **se non si dispone più di questo passphrase, non sarà più possibile accedere ai bitcoin** memorizzati con il wallet Ashigaru. Questo stesso passphrase viene utilizzato anche per crittografare il file di recupero del wallet.



Se non sapete cos'è un passphrase o non ne comprendete appieno il funzionamento, vi consiglio vivamente di leggere questo ulteriore tutorial. È importante, perché il passphrase è un elemento critico della vostra sicurezza: un'incomprensione del suo utilizzo potrebbe comportare la perdita permanente dei vostri fondi.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Una volta inserito il passphrase, fare clic su `NEXT`.



![Image](assets/fr/15.webp)



Scegliere quindi un codice PIN. Questo codice verrà utilizzato per sbloccare il wallet Ashigaru, proteggendolo dall'accesso fisico non autorizzato. Non partecipa alla derivazione crittografica delle chiavi del wallet. Ciò significa che, anche senza conoscere il codice PIN, chiunque abbia la vostra frase mnemonica e il passphrase sarà in grado di riavere accesso ai vostri bitcoin.



Optate per un codice PIN lungo e casuale. Ricordate di tenere una copia di backup in un luogo separato dal telefono, per evitare che vengano compromessi contemporaneamente.



![Image](assets/fr/16.webp)



Una volta creato il codice PIN, Ashigaru visualizza la frase mnemonica del wallet. Attenzione: questa frase, combinata con il passphrase, dà pieno accesso ai bitcoin. Chiunque ne sia in possesso può impossessarsi dei vostri fondi, anche se non ha accesso al vostro telefono. Questa sequenza di 12 parole può essere utilizzata per ripristinare il wallet in caso di perdita, furto o rottura del telefono. È quindi importante conservarla con la massima cura su un supporto fisico (carta o metallo).



Non salvate mai questa frase in forma digitale, altrimenti rischiate di esporre i vostri fondi al furto. A seconda della vostra strategia di sicurezza, potete creare diverse copie fisiche, ma non dividetele mai. Mantenete le parole nell'ordine esatto e assicuratevi che siano numerate.



Infine, non conservare mai il mnemonico e il passphrase nello stesso posto. Se entrambi venissero compromessi contemporaneamente, un malintenzionato potrebbe accedere al wallet.



![Image](assets/fr/17.webp)



Per saperne di più su come proteggere la vostra frase mnemonica, consultate questo tutorial complementare:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru chiede quindi di riconfermare il proprio passphrase. Cogliete l'occasione per verificare che il vostro backup fisico sia corretto.



![Image](assets/fr/18.webp)



### 3.2. collegare un dojo



Successivamente, si passa alla fase di connessione al Dojo. Come spiegato nell'introduzione, per interagire con la rete Bitcoin, l'Ashigaru deve essere collegato a un Dojo.



Accedere allo "Strumento di manutenzione" del proprio Dojo e aprire il menu "APPUNTAMENTI".



![Image](assets/fr/19.webp)



Su Ashigaru, premere il pulsante "Scansione QR", quindi scansionare il codice QR di connessione visualizzato dal DMT. Quindi fare clic su "Continua" per confermare.



![Image](assets/fr/20.webp)



Immettere il codice PIN per sbloccare il wallet. Si accede così alla pagina di sincronizzazione. È normale che in questa fase vengano visualizzati errori *PayNym*, poiché il wallet è nuovo. Fare semplicemente clic su "Continua".



![Image](assets/fr/21.webp)



Verrà quindi visualizzata la pagina iniziale del portafoglio.



![Image](assets/fr/22.webp)



Prima di proseguire, vi consiglio di effettuare un ripristino di prova quando il wallet non contiene ancora bitcoin. In questo modo si potrà verificare che i backup cartacei funzionino correttamente. Per sapere come fare, seguite questo tutorial:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Impostazione dell'applicazione Ashigaru



Per accedere alle impostazioni dell'applicazione, cliccate sull'immagine del vostro *PayNym* nell'angolo in alto a sinistra, quindi selezionate "Impostazioni".



![Image](assets/fr/23.webp)



Qui troverete diverse opzioni per adattare il funzionamento di Ashigaru alle vostre esigenze. Tuttavia, vi consiglio vivamente di attivare fin dall'inizio due parametri importanti.



Iniziate aprendo il menu `Sicurezza > Modalità Stealth`, quindi attivate questa funzione se ne avete bisogno. Questa funzione nasconde l'applicazione Ashigaru dietro il nome, il logo e l'interfaccia di una normale applicazione installata sul telefono. Lo scopo è quello di impedire a chiunque di identificare Ashigaru in caso di ispezione fisica del telefono.



![Image](assets/fr/24.webp)



Ogni applicazione falsa offerta ha un metodo specifico per sbloccare la vera interfaccia Ashigaru. Ad esempio, se si sceglie la calcolatrice, l'applicazione Ashigaru scompare dalla schermata iniziale e viene sostituita da una finta calcolatrice. Quando la si apre, si vede la classica interfaccia di una calcolatrice funzionante, ma per accedere ad Ashigaru è sufficiente toccare cinque volte velocemente il simbolo `=`.



Il secondo parametro importante da attivare è [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Questa opzione consente di aumentare il costo di una transazione se questa rimane bloccata nei mempool perché il costo è troppo basso. È possibile attivarla tramite il menu `Transazioni > Spendi usando RBF`.



![Image](assets/fr/25.webp)



Suggerimento: è possibile cambiare l'unità di visualizzazione del portafoglio da `BTC` a `sat` semplicemente facendo clic sul saldo totale visualizzato nella pagina iniziale.



## 5. Ricevere bitcoin su Ashigaru



Ora che il portafoglio è operativo, è possibile ricevere i satss. Per farlo, premere il pulsante `+` in basso a destra dell'interfaccia, quindi il pulsante verde `Ricevi`.



![Image](assets/fr/26.webp)



Ashigaru vi mostra quindi il primo indirizzo di ricezione inutilizzato nel vostro wallet, per evitare il riutilizzo dell'indirizzo (il riutilizzo dell'indirizzo è una pratica molto negativa per la vostra privacy). È quindi possibile inoltrare questo indirizzo alla persona o al servizio che deve inviare bitcoin.



![Image](assets/fr/27.webp)



Una volta trasmessa in rete, la transazione apparirà automaticamente sulla pagina iniziale dell'applicazione.



![Image](assets/fr/28.webp)



## 6. Inviare bitcoin con Ashigaru



Ora che avete dei bitcoin nella vostra Ashigaru wallet, potete anche inviarli. Per farlo, premere il pulsante `+` in basso a destra, quindi selezionare il pulsante rosso `Invia`.



![Image](assets/fr/29.webp)



Scegliere quindi il conto dal quale si desidera effettuare la spesa. Per il momento non abbiamo ancora affrontato il conto `Postmix`, riservato alle coinjoin, di cui ci occuperemo in un prossimo tutorial. Invieremo quindi i fondi dal conto di deposito principale.



![Image](assets/fr/30.webp)



Inserire i dettagli della transazione: l'importo da inviare e l'indirizzo Bitcoin del destinatario.



![Image](assets/fr/31.webp)



Facendo clic sui tre puntini nell'angolo in alto a destra e poi su "Mostra uscite non spese", si può anche scegliere con precisione quali UTXO si desidera spendere, per migliorare la propria privacy.



![Image](assets/fr/32.webp)



Una volta compilati tutti i dettagli, fare clic sulla freccia bianca in fondo all'interfaccia per continuare.



Si accede quindi a una pagina di riepilogo che mostra tutti i dettagli della transazione. Vengono visualizzati diversi elementi importanti:




- Nel blocco `Destinazione`, verificare un'ultima volta che l'indirizzo del destinatario e l'importo inviato siano corretti;
- Nel blocco `Tasse`, è possibile visualizzare la tariffa selezionata automaticamente da Ashigaru e, se necessario, modificarla cliccando su `MANAGE`;
- Il blocco `Transaction` indica il tipo di transazione che si sta per eseguire. In questo caso, parliamo di una transazione semplice, ma Ashigaru supporta anche altri tipi di transazioni ottimizzate per la privacy, di cui parleremo in dettaglio in un prossimo tutorial;
- Il blocco rosso "Allarme transazione" avverte l'utente se la transazione mostra schemi che possono essere riconosciuti dagli strumenti di analisi della catena e che potrebbero compromettere la sua privacy. Facendo clic su di esso, è possibile visualizzare i dettagli. Ad esempio, nel mio caso, Ashigaru mi dice che l'importo inviato è rotondo (`3000 sats`), permettendomi di dedurre quale uscita corrisponde alla spesa e quale allo scambio. Per saperne di più su queste euristiche di analisi della catena, vi invito a seguire la mia formazione su BTC 204 su Plan ₿ Academy ;
- Infine, è possibile aggiungere un'etichetta alla transazione per tenere traccia del suo scopo.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Dopo aver controllato tutte le informazioni, utilizzare la freccia verde per inviare i bitcoin. Tenere premuta la freccia, quindi trascinarla verso destra per confermare il caricamento.



![Image](assets/fr/33.webp)



La vostra transazione è stata trasmessa sulla rete Bitcoin.



![Image](assets/fr/34.webp)



## 7. Recupero dell'Ashigaru wallet



Il recupero di un Ashigaru wallet differisce leggermente da quello di un Bitcoin wallet classico, poiché l'applicazione utilizza gli stessi metodi del Samurai Wallet. Se si perde l'accesso al wallet (perché si è dimenticato il PIN, si è disinstallato o si è perso il telefono), ci sono diversi modi per recuperare i bitcoin.



Se avete ancora accesso al vostro telefono o se avete fatto una copia di backup di questo file, il metodo più semplice è usare il file di backup `ashigaru.txt`. Questo file contiene tutte le informazioni necessarie per ripristinare il portafoglio su una nuova istanza di Ashigaru (o su Sparrow Wallet), ma è criptato con il passphrase definito al punto 3.1 di questo tutorial. È quindi necessario disporre sia del file `ashigaru.txt` che del passphrase per utilizzare questo metodo.



Con questi due elementi è possibile, ad esempio, ripristinare il portafoglio su Sparrow Wallet.



![Image](assets/fr/35.webp)



Se non avete accesso al file `ashigaru.txt`, potete comunque recuperare l'accesso ai vostri fondi usando la vostra frase mnemonica del passphrase, proprio come fareste per qualsiasi altro portafoglio del Bitcoin. Vi consiglio di eseguire questo ripristino su una nuova istanza Ashigaru o direttamente sul Sparrow Wallet, per recuperare facilmente i percorsi di bypass dal Whirlpool se lo stavate utilizzando. In alternativa, è possibile importare queste informazioni in qualsiasi altro software compatibile con BIP39 inserendo manualmente i percorsi di derivazione.



Per ulteriori informazioni su questa procedura, consultare il tutorial completo che ho scritto sul recupero di un Wallet Samurai wallet. Poiché l'Ashigaru è un fork, la procedura è identica:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Come si può notare, qualunque sia il metodo di ripristino utilizzato, il passphrase è indispensabile. Assicuratevi quindi di eseguire un backup accurato. È anche possibile creare diverse copie, a seconda della propria strategia di sicurezza.



## 8. Aggiornamento dell'applicazione



Per aggiornare l'app Ashigaru, dato che l'avete installata da un file `.apk` e non tramite il Play Store come una normale app, dovrete scaricare il nuovo file `.apk` corrispondente alla versione aggiornata, quindi installarlo manualmente.



Ripetete i passaggi descritti nella sezione 2 di questa guida, ma quando fate clic sul file `.apk` per avviare l'installazione, **il vostro telefono Android dovrebbe offrirvi l'opzione `Aggiornamento` e non `Installazione`**.



![Image](assets/fr/41.webp)



Questo è un punto molto importante: se Android visualizza `Install` invece di `Update`, probabilmente si sta installando una versione fraudolenta. In questo caso, interrompete immediatamente la procedura di installazione.



Come per la prima installazione, verificare l'autenticità e l'integrità del file `.apk` prima di procedere con l'aggiornamento.



Per sapere quando è disponibile una nuova versione, controllate di tanto in tanto il sito ufficiale di Ashigaru. Siate certi che Ashigaru è un'applicazione stabile e matura, ereditata da Samourai Wallet, e gli aggiornamenti sono relativamente poco frequenti rispetto ai software più recenti.



## 9. Donazione al progetto Ashigaru



Ashigaru è un progetto open-source. Se volete sostenere il suo sviluppo, potete fare una donazione direttamente dall'applicazione tramite PayNym.



Per farlo, cliccare sul proprio PayNym in alto a destra dell'interfaccia, quindi selezionare il codice di pagamento che inizia con `PM...`.



![Image](assets/fr/36.webp)



Quindi premere il pulsante `+` in basso a destra dello schermo.



![Image](assets/fr/37.webp)



Selezionate `Ashigaru Open Source Project` come destinatario.



![Image](assets/fr/38.webp)



Fare clic sul pulsante `CONNECT` per stabilire il canale di comunicazione BIP47 (ulteriori informazioni su questo protocollo sono riportate nel tutorial sottostante).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Una volta confermata la transazione di notifica, è possibile inviare le donazioni al progetto facendo clic sulla piccola freccia bianca nell'angolo in alto a destra dell'interfaccia.



![Image](assets/fr/40.webp)



Ora sapete come utilizzare le funzioni di base dell'applicazione Ashigaru. Nelle prossime esercitazioni vedremo come sfruttare le transazioni di spesa avanzate, oltre a Whirlpool, l'implementazione del coinjoin ereditata da Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

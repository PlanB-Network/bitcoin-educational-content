---
name: Terminale Ashigaru
description: Usa Ashigaru sul desktop per creare coinjoin
---

![cover](assets/cover.webp)



Ashigaru Terminal è l'adattamento del team Ashigaru del Sparrow Server, che implementa il protocollo Whirlpool coinjoin. Questo software è la continuazione del lavoro iniziato da Samourai Wallet, in particolare sulla GUI di Whirlpool, di cui adotta i principi fondamentali: autocustodia e conservazione della riservatezza.



Questo software è un fork del Sparrow Server, modificato e ottimizzato per la piena integrazione con l'ecosistema Whirlpool, il protocollo di coinjoin ZeroLink originariamente sviluppato dai team di Samourai.



Ashigaru Terminal opera da un'interfaccia TUI minimalista e può essere distribuito su un personal computer o su un server dedicato. Consente di interagire direttamente con Whirlpool per avviare "*Tx0*", gestire i conti "*Deposit*", "*Premix*", "*Postmix*" e "*Badbank*" ed eseguire rimescolamenti automatici per rafforzare la riservatezza dei vostri pezzi.



In breve, Ashigaru Terminal sarà particolarmente utile se si desidera creare coinjoin usando Whirlpool.



In questo primo tutorial, vi illustrerò l'installazione e il funzionamento di Ashigaru Terminal. Un secondo tutorial più avanzato sarà dedicato alla creazione di coinjoin.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Installare il terminale Ashigaru



Per installare Ashigaru Terminal, è necessario Tor Browser, poiché i file binari sono distribuiti solo attraverso la rete Tor. Se non l'avete ancora fatto, [installatelo sulla vostra macchina](https://www.torproject.org/download/).



### 1.1. scaricare Ashigaru Terminal



Da Tor Browser, andare a [la pagina dei rilasci del loro repository Git](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) per scaricare l'ultima versione di Ashigaru Terminal per il vostro sistema operativo.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Scaricate i 2 file seguenti per il vostro sistema operativo:




- Il binario (`ashigaru_terminal_v1.0.0_amd64.deb` per Debian/Ubuntu, `.dmg` per macOS o `.zip` per Windows) ;
- Il file hashs firmato: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Controllare il terminale Ashigaru



Prima di eseguire il software sul proprio dispositivo, è necessario verificarne l'autenticità e l'integrità. Si tratta di un passaggio importante, in quanto impedisce di installare una versione fraudolenta che potrebbe compromettere i bitcoin o infettare il computer.



Aprite una nuova scheda del browser e andate su [Keybase verification tool] (https://keybase.io/verify). Incollate il contenuto del file `.txt` appena scaricato nell'apposito campo, quindi fate clic sul pulsante `Verifica`.



![Image](assets/fr/02.webp)



Per diversificare le vostre fonti di verifica, potete anche confrontare il messaggio con quello disponibile sul sito clearnet [ashigaru.rs](https://ashigaru.rs/download/), nella sezione `/download`.



![Image](assets/fr/03.webp)



Se la firma è valida, Keybase visualizzerà un messaggio che conferma che il file è stato firmato dagli sviluppatori di Ashigaru.



![Image](assets/fr/04.webp)



È inoltre possibile fare clic sul profilo di `ashigarudev` visualizzato da Keybase e verificare che l'impronta digitale della chiave corrisponda esattamente a: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Se in questa fase compare un errore, la firma non è valida. In questo caso, **non installare il software scaricato**. Ricominciare dall'inizio o chiedere aiuto alla comunità prima di continuare.



Keybase vi ha fornito l'hash autenticato dell'applicazione. Verifichiamo ora che l'hash del file `.deb', `.zip' o `.dmg' scaricato corrisponda a quello convalidato su Keybase. Per farlo, andate su [HASH FILE ONLINE](https://hash-file.online/).



Fare clic sul pulsante `BROWSE...` e selezionare il file `.deb`, `.zip` o `.dmg` scaricato al punto 1.1. Scegliere quindi la funzione di hash `SHA-256` e fare clic su `CALCOLA HASH` per generate l'hash del file.



![Image](assets/fr/06.webp)



Il sito visualizzerà quindi l'hash del software. Confrontatelo con l'hash verificato su Keybase.io. Se i due corrispondono perfettamente, la verifica dell'autenticità e dell'integrità ha avuto successo. È quindi possibile utilizzare il software.



![Image](assets/fr/07.webp)



### 1.3 Avvio del terminale Ashigaru





- Debian / Ubuntu



Per installare il software, eseguire il comando :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Modificare l'ordine in base alla versione scaricata.



Quindi verificare l'installazione:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Avviare quindi il software:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Finestre**



Fare clic con il pulsante destro del mouse sul file `.zip' scaricato e controllato, quindi selezionare `Estrai tutto...` per estrarre il contenuto.



Una volta completata l'estrazione, fare doppio clic sul file `Ashigaru-terminal.exe` per avviare il software.



![Image](assets/fr/08.webp)



## 2. Come iniziare con il terminale Ashigaru



Ashigaru Terminal è un programma TUI (*Text-based User Interface*), cioè un'interfaccia minimalista che gira direttamente nel terminale. Si interagisce con essa utilizzando menu e scorciatoie da tastiera, ma senza un vero e proprio ambiente grafico classico.



![Image](assets/fr/09.webp)



È facile da usare: utilizzate i tasti freccia della tastiera per navigare nei menu e premete il tasto "Invio" per convalidare un'azione o confermare una scelta.



## 3. Collegamento del nodo al terminale Ashigaru



Per impostazione predefinita, Ashigaru Terminal si connette a un server Electrum pubblico. Questo comporta ovviamente dei rischi in termini di riservatezza e sovranità. Quindi lo configureremo per connettersi direttamente al proprio Electrum Server.



Per farlo, aprire il menu `Preferenze > Server`.



![Image](assets/fr/10.webp)



Fare clic sul pulsante `<Modifica >`.



![Image](assets/fr/11.webp)



Selezionare "Electrum Server privato", quindi fare clic su "Continua".



![Image](assets/fr/12.webp)



Inserire l'URL e la porta del proprio server. È possibile specificare un indirizzo Tor in `.onion`. Cliccare quindi su `<Test >` per verificare la connessione.



![Image](assets/fr/13.webp)



Se la connessione ha successo, apparirà il messaggio `Successo', insieme ai dettagli del vostro server.



![Image](assets/fr/14.webp)



Se non avete ancora un nodo Bitcoin, vi consiglio di seguire questo corso:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*Nel mio caso, per questa esercitazione, mi disconnetterò dal mio server Electrs perché sto lavorando su testnet. Tuttavia, l'operazione rimane rigorosamente identica su mainnet.*



## 4. Creare un portafoglio su Ashigaru Terminal



Ora che il software è configurato correttamente, è possibile aggiungere un portafoglio Bitcoin.



Avete due opzioni:




- È possibile creare un nuovo wallet da zero e utilizzarlo esclusivamente su Ashigaru Terminal. In questo caso, sarà necessario aprire questo software ogni volta che si desidera interagire con il proprio wallet;
- In alternativa, è possibile importare il wallet Ashigaru esistente direttamente dal telefono ad Ashigaru Terminal. Lo svantaggio di questo metodo è che riduce leggermente la sicurezza della vostra configurazione, poiché il vostro wallet è esposto a due ambienti rischiosi invece che a uno. D'altra parte, offre il vantaggio di poter lasciare Ashigaru Terminal sempre in funzione per miscelare le monete, consentendo al contempo di spenderle in remoto tramite l'applicazione mobile Ashigaru.



In questa esercitazione, opteremo per il secondo metodo. Tuttavia, se preferite creare un portafoglio completamente nuovo, la procedura rimane la stessa: l'unica differenza sarà durante la creazione, quando dovrete salvare la vostra nuova frase mnemonica e il vostro nuovo passphrase.



Nota anche che Ashigaru Terminal non consente di spendere direttamente i tuoi bitcoin. Puoi sincronizzare lo stesso portafoglio su Ashigaru Terminal e sull’app Ashigaru (come farò in questo tutorial), oppure su Sparrow Wallet.



Se non avete ancora un wallet sull'applicazione Ashigaru, potete seguire il tutorial dedicato:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Andare al menu `Portafogli`.



![Image](assets/fr/15.webp)



Quindi selezionare `Crea/ripristina wallet...`. L'opzione `Apri Wallet...` consente di accedere in un secondo momento a un portafoglio già salvato nel Terminale Ashigaru.



![Image](assets/fr/16.webp)



Date un nome al vostro portafoglio.



![Image](assets/fr/17.webp)



Scegliere quindi il tipo di portafoglio "Hot Wallet".






![Image](assets/fr/18.webp)



È in questa fase che la procedura si differenzia a seconda della scelta iniziale:




- Se si desidera creare un nuovo portafoglio da zero, fare clic su `<Generare un nuovo Wallet>`, definire un passphrase BIP39, quindi salvare accuratamente la frase mnemonica e il passphrase su un supporto fisico;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Se si desidera utilizzare lo stesso wallet dell'applicazione Ashigaru, inserire le 12 parole della frase mnemonica e il passphrase BIP39 direttamente nei campi corrispondenti. Scrivete le parole in minuscolo, intere, in ordine, separate da uno spazio, senza numeri o caratteri aggiuntivi.



Una volta completato questo passaggio, fare clic su `<Avanti >`.



*Nota*: Se non è possibile fare clic su questo pulsante, la frase mnemonica non è valida. Controllate attentamente che nessuna parola sia errata o scritta male.



![Image](assets/fr/19.webp)



Sarà quindi necessario impostare una password. Questa verrà utilizzata per sbloccare il terminale Ashigaru wallet e proteggerlo da accessi fisici non autorizzati. Non è coinvolta nella derivazione crittografica delle chiavi: in altre parole, anche senza questa password, chiunque abbia la frase mnemonica e il passphrase sarà in grado di ripristinare il wallet e accedere ai bitcoin.



Scegliete una password lunga, complessa e casuale. Conservatene una copia in un luogo sicuro: idealmente su un supporto fisico o in un gestore di password sicuro.



Al termine, fare clic su `< OK >`.



![Image](assets/fr/20.webp)



## 5. Utilizzo del portafoglio



Si può quindi scegliere a quale conto accedere. Per il momento non abbiamo avviato alcun mix, quindi accediamo al conto `Deposit`.



![Image](assets/fr/21.webp)



Il funzionamento è quindi identico a quello del Sparrow, poiché Ashigaru Terminal è un fork del Sparrow Server. Troverete gli stessi menu:



![Image](assets/fr/22.webp)





- transazioni": consente di consultare la cronologia delle transazioni collegate a questo conto. Nel mio caso, alcune di esse appaiono già, poiché ne avevo effettuate alcune con l'applicazione Ashigaru su questo stesso wallet.



![Image](assets/fr/23.webp)





- receive`: genera un nuovo indirizzo di ricevuta vuoto per l'inserimento dei satss nel conto di deposito.



![Image](assets/fr/24.webp)





- indirizzi`: visualizza un elenco di tutti i vostri indirizzi, che appartengono alla catena interna o esterna del vostro account.



![Image](assets/fr/25.webp)





- `UTXOs`: elenca tutti gli UTXO disponibili.



![Image](assets/fr/26.webp)





- impostazioni": consente di accedere al *descrittore* del portafoglio. È inoltre possibile consultare il proprio seed, regolare il *Limite di Gap* o modificare la data di creazione del portafoglio.



![Image](assets/fr/27.webp)



Ora sai come installare e utilizzare Ashigaru Terminal. Nel prossimo tutorial vedremo come eseguire coinjoin con questo software e come gestire i fondi in "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

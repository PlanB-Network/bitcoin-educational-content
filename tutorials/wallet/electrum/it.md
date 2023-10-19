---
name: Electrum

description: Guida completa a Electrum, da zero all'eroe
---

![cover](assets/cover.png)

Descrizione di Electrum

https://twitter.com/ElectrumWallet
https://electrum.org/
https://electrum.readthedocs.io/

> "Devo dire che quando ho trovato questa guida sono rimasto scioccato. Congratulazioni ad Arman the Parman per questo. Sarebbe stato un peccato non ospitarlo qui e tradurlo in quante più lingue possibili. Onestamente, consigli per quel tipo." Rogzy

![Portafoglio desktop Electrum (Mac / Linux) - download, verifica, connessione al tuo nodo.](https://youtu.be/wHmQNcRWdHM)

![Effettuare una transazione Bitcoin con Electrum](https://youtu.be/-d_Zd7VcAfQ)

## Perché Electrum?

Questa è una guida dettagliata su come utilizzare il portafoglio Bitcoin Electrum, con soluzioni per tutte le sue insidie e particolarità, qualcosa che ho sviluppato dopo diversi anni di utilizzo e insegnamento agli studenti sulla sicurezza/privacy di Bitcoin. Electrum non è il miglior portafoglio Bitcoin per chi vuole mantenere tutto il più semplice possibile e preferisce rimanere a livello principiante. Invece, è per chi è o aspira ad essere un utente "esperto".

Per il nuovo utente di Bitcoin, è eccellente solo se sotto la supervisione di un utente esperto che gli mostri la strada. Se si impara ad usarlo da soli, sarebbe sicuro a patto che si prenda il proprio tempo e lo si utilizzi in un ambiente di test con solo un piccolo numero di satoshi all'inizio. Questa guida supporta tale sforzo, ma è anche un buon punto di riferimento per chiunque altro.

> Avviso: questa guida è grande. Non cercare di fare tutto questo in un solo giorno. È meglio salvare la guida e procedere gradualmente nel tempo.

## Scaricare Electrum

Idealmente, utilizzare un computer dedicato a Bitcoin per le proprie transazioni Bitcoin (la mia guida per questo https://armantheparman.com/mint/) _(DISPONIBILE anche nella sezione sulla privacy)_. Va bene esercitarsi con piccole quantità su un computer "sporco" quando si sta imparando (chissà quanti malware nascosti il tuo computer regolare ha accumulato nel corso degli anni - non vuoi esporre i tuoi portafogli Bitcoin ad essi).

Ottieni Electrum da https://electrum.org/.

Clicca sulla scheda Download in alto.

Clicca sul link di download corrispondente al tuo computer. Qualsiasi computer Linux o Mac può utilizzare il link Python (cerchio rosso). Un computer Linux con un chip Intel o AMD può utilizzare l'Appimage (cerchio verde; è simile a un file eseguibile di Windows). Un dispositivo Raspberry Pi ha un microprocessore ARM e può utilizzare solo la versione Python (cerchio rosso), non l'Appimage, anche se i Pi eseguono Linux. Il cerchio blu è per Windows e il cerchio nero è per Mac.

![image](assets/1.png)

## Verifica di Electrum

Lo scopo della "verifica" del download è assicurarsi che nemmeno un singolo bit di dati sia stato manomesso. Ciò impedisce di utilizzare una versione "hackerata" e dannosa del software. Va bene saltare questa fase a patto che si utilizzi la copia scaricata solo per esercitarsi, ovvero non utilizzare portafogli che contengono denaro serio. Quindi, una volta pronti a utilizzare Electrum per i propri fondi reali, è necessario eliminare la propria copia e ricominciare, questa volta verificando il download.

Per fare ciò, utilizziamo strumenti di crittografia a chiave pubblica/privata - gpg, di cui abbiamo scritto una guida qui (https://armantheparman.com/gpg/). Lo strumento gpg viene fornito con tutti i sistemi operativi Linux. Per Mac e Windows, consulta il link gpg per le istruzioni di download.
Oltre al download del software Electrum, per motivi di sicurezza, è necessaria anche la FIRMA digitale del software. Si tratta di una stringa di testo (in realtà un numero codificato usando il testo) che lo sviluppatore ha prodotto con la sua chiave gpg PRIVATA. Utilizzando il programma gpg, possiamo quindi "testare" la FIRMA rispetto alla sua chiave PUBBLICA (creata dalla chiave privata dello sviluppatore) a cui tutti hanno accesso, rispetto al FILE di download.

In altre parole, con i tre input (firma, chiave pubblica e file di dati), otteniamo un output vero o falso per confermare che il file non è stato manomesso.

Per ottenere la firma, fai clic sul link corrispondente al file scaricato (vedi frecce colorate):

![image](assets/2.png)

Cliccando sul link potrebbe scaricare automaticamente il file nella cartella dei download, oppure potrebbe aprirsi nel browser. Se si apre nel browser, è necessario salvare il file. È possibile fare clic con il pulsante destro del mouse e selezionare "Salva con nome". A seconda del sistema operativo o del browser, potrebbe essere necessario fare clic con il pulsante destro del mouse nell'area dello spazio bianco, non sul testo.

Di seguito è riportato il testo scaricato. Puoi vedere che ci sono più firme, queste sono firme di persone diverse. Puoi verificare ognuna di esse. Ti mostrerò come verificare solo quella dello sviluppatore.

![image](assets/3.png)

Successivamente, è necessario ottenere la chiave pubblica di ThomasV, che è il principale sviluppatore. Puoi ottenerla direttamente da lui, dal suo account Keybase, da Github o da qualcun altro, da un keyserver o dal sito web di Electrum.

Ottenerla dal sito web di Electrum è in realtà il modo meno sicuro, perché se questo sito web è malintenzionato (proprio ciò che stiamo verificando), perché dovremmo ottenere una chiave pubblica da esso (la chiave pubblica potrebbe essere falsa)?

Per tenerlo semplice per ora, ti mostrerò come ottenerla comunque dal sito web, ma tieni presente questo. Ecco la copia (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc) su GitHub con cui puoi confrontarla.

Scorri un po' verso il basso nella pagina per trovare il link alla chiave pubblica di ThomasV (cerchio rosso sotto). Fai clic su di esso e scaricalo, o se si apre del testo in un browser, fai clic con il pulsante destro del mouse per salvarlo.

![image](assets/4.png)

Ora hai 3 nuovi file, probabilmente tutti nella cartella dei download. Non importa dove si trovano, ma rende il processo più semplice se li metti tutti nella stessa cartella.

I tre file:

1. Il download di Electrum
2. Il file di firma (di solito ha lo stesso nome del download di Electrum con l'aggiunta di ".asc")
3. La chiave pubblica di ThomasV.

Apri un terminale su Mac o Linux, o il prompt dei comandi (CMD) su Windows.

Vai alla directory dei download (o ovunque tu abbia messo i tre file). Se non hai idea di cosa significhi, impara da questo breve video per Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) e questo per Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Ricorda che sui computer Linux, i nomi delle directory sono sensibili alle maiuscole.
Nel terminale, digita questo per importare la chiave pubblica di ThomasV nel "portachiavi" del tuo computer (il portachiavi è un concetto astratto - in realtà è solo un file sul tuo computer):

```
gpg --import ThomasV.asc
```

Assicurati che il nome del file corrisponda a quello che hai scaricato. Inoltre, nota che ci sono due trattini, non uno solo. Inoltre, nota che c'è uno spazio prima e dopo "--import". Poi premi <enter>.

Il file dovrebbe essere importato. Se ricevi un errore, controlla di essere nella directory in cui il file effettivamente si trova. Per verificare in quale directory ti trovi (su Mac o Linux), digita pwd. Per vedere quali file sono nella directory in cui ti trovi (su Mac o Linux), digita ls. Dovresti vedere elencato il file di testo "ThomasV.asc", eventualmente tra gli altri file.

Poi esegui il comando per verificare la firma.

```
gpg –verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Nota che ci sono 4 "elementi" qui, separati da uno spazio. Ho messo in grassetto il testo alternativamente per aiutarti a vedere. I quattro elementi sono:

1. il programma gpg
2. l'opzione --verify
3. il nome del file della firma
4. il nome del programma

A volte puoi omettere il quarto elemento e il computer indovina cosa intendi. Non sono sicuro, ma credo che funzioni solo se i nomi dei file differiscono solo per "asc" alla fine.

Non copiare semplicemente i nomi dei file che ho mostrato qui - assicurati che corrispondano al nome del file che hai sul tuo sistema.

Premi <enter> per eseguire il comando. Dovresti vedere una "buona firma da ThomasV" per indicare il successo. Ci saranno alcuni errori perché non abbiamo le chiavi pubbliche per le firme delle altre persone che sono contenute nel file di firma (questo sistema di combinare le firme in un unico file potrebbe cambiare nelle versioni successive). Inoltre, c'è un avviso in fondo che possiamo ignorare (questo ci avvisa che non abbiamo esplicitamente detto al computer di fidarci della chiave pubblica di ThomasV).

Ora abbiamo una copia verificata di Electrum che è sicura da usare.

## Esecuzione di Electrum

### Esecuzione di Electrum se si utilizza Python

Se hai scaricato la versione di Python, ecco come farla funzionare. Vedrai sulla pagina di download questo:

![image](assets/5.png)

Per Linux, è una buona idea prima aggiornare il sistema:

```
sudo apt-get update
sudo apt-get upgrade
```

Copia il testo giallo evidenziato, incollalo nel terminale e premi <enter>. Ti verrà chiesta la password, eventualmente una conferma per continuare, e poi installerà quei file ("dipendenze").

Dovrai anche estrarre il file zippato in una directory a tua scelta. Puoi farlo con l'interfaccia utente grafica o dalla riga di comando (comando evidenziato in rosa) - ricorda che i nomi dei tuoi file potrebbero essere diversi. (Nota che quando abbiamo verificato il download nella sezione precedente, abbiamo verificato il file zip, non la directory estratta.)

C'è un'opzione per "installare" usando il programma PIP, ma questo è superfluo e aggiunge passaggi extra e l'installazione di file. Esegui semplicemente il programma utilizzando il terminale per evitare tutto ciò.

I passaggi (Linux) sono:

1. vai alla directory in cui sono estratti i file
2. digita: ./run_electrum

Su un Mac, i passaggi sono gli stessi ma potrebbe essere necessario installare prima Python3 e utilizzare questo comando per eseguire:

````
```python3 ./run_electrum```
````

Una volta che Electrum è in esecuzione, la finestra del terminale rimarrà aperta. Se la chiudi, terminerà il programma Electrum. Riducila al minimo mentre usi Electrum.

### Esecuzione di Electrum con l'Appimage

Questo è un po' più semplice, ma non così facile come un file eseguibile di Windows. A seconda della versione di Linux che stai utilizzando, di default i file Appimage potrebbero avere attributi impostati in modo che l'esecuzione sia vietata dal sistema. Dobbiamo cambiarlo. Se il tuo Appimage funziona, puoi saltare questo passaggio. Vai alla posizione del file, utilizzando il terminale, quindi esegui questo comando:

```
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

"sudo" fornisce privilegi di superutente; "chmod" è un comando per cambiare la modalità, modificando chi può leggere, scrivere o eseguire; "ug+x" significa che stiamo modificando l'utente e il gruppo per consentire l'esecuzione.

Modifica il nome del file per corrispondere alla tua versione.

Quindi, Electrum verrà eseguito facendo doppio clic sull'icona dell'Appimage.

### Esecuzione di Electrum con Mac

Basta fare doppio clic sul file scaricato (è un "drive"). Si aprirà una finestra. Trascina l'icona di Electrum nella finestra sul desktop o ovunque tu voglia conservare il programma. Puoi quindi "espellere" il drive e cancellare il drive (file scaricato).

Per eseguire il programma, basta fare doppio clic su di esso. Potresti ricevere alcuni errori "nanny" specifici di Mac che devono essere bypassati.

### Esecuzione di Electrum con Windows

Nonostante il fatto che odio Windows più di tutto, questo è il metodo più semplice. Basta fare doppio clic sul file eseguibile per avviarlo.

## Inizia con un portafoglio fittizio

Quando carichi per la prima volta Electrum, si aprirà una finestra come questa:

![image](assets/6.png)

Successivamente, seleziona manualmente il tuo server, ma per ora lascia le impostazioni predefinite e connessione automatica.

Successivamente, crea un portafoglio fittizio: non mettere mai fondi in questo portafoglio. Lo scopo di questo portafoglio fittizio è quello di procedere attraverso il software e assicurarsi che tutto funzioni correttamente prima di caricare il tuo vero portafoglio. Stiamo cercando di evitare di rivelare accidentalmente la privacy con un portafoglio reale. Se stai solo facendo pratica, il portafoglio che crei può essere considerato comunque un portafoglio fittizio.

Puoi lasciare il nome come "default_wallet" o cambiarlo a tuo piacimento e fare clic su Avanti. In seguito, se hai più portafogli, puoi trovarli e aprirli in questa fase facendo clic prima su "Scegli..."

![image](assets/7.png)

Scegli "Portafoglio standard" e <Avanti>:

![image](assets/8.png)

Quindi, seleziona "Ho già una frase di recupero". Non voglio che tu prenda l'abitudine di creare una frase di recupero di Electrum, poiché utilizza il proprio protocollo che non è compatibile con altri portafogli: ecco perché non clicchiamo su "nuova frase di recupero".

![image](assets/9.png)

Vai su https://iancoleman.io/bip39/ e crea una frase di recupero fittizia. Prima, cambia il numero di parole a 12 (che è una pratica comune), quindi fai clic su "genera" e copia le parole nella casella negli appunti.

![image](assets/10.png)

Quindi incolla le parole in Electrum. Ecco un esempio:

![image](assets/11.png)

Electrum cercherà parole che corrispondano al suo proprio protocollo. Dobbiamo bypassare questo. Fai clic su Opzioni e seleziona Frase di recupero BIP39:

![image](assets/12.png)

Il seme diventa quindi valido. (Prima di fare ciò, Electrum si aspettava un seme di Electrum, quindi questo seme era considerato non valido). Prima di fare clic su Avanti, notare il testo che dice "Checksum OK". È importante (per il portafoglio reale che potresti utilizzare in seguito) vedere questo prima di procedere, poiché conferma la validità del seme inserito. L'avvertimento in fondo può essere ignorato, è solo una lamentela dello sviluppatore di Electrum riguardo a BIP39 e alle loro affermazioni "FUD" che la loro versione (che non è compatibile con altri portafogli) è superiore.

> Una breve deviazione per un avvertimento importante. Lo scopo del checksum è assicurarsi di aver inserito il seme senza errori di battitura. Il checksum è la parte finale del seme (la 12ª parola diventa la parola di checksum) che viene determinata matematicamente dalla prima parte del seme (11 parole). Se si dovesse digitare qualcosa di sbagliato all'inizio, la parola di checksum non corrisponderà matematicamente e il software del portafoglio ti avviserà con un avvertimento. Ciò non significa che il seme non possa essere utilizzato per creare un portafoglio Bitcoin funzionale. Immagina di creare un portafoglio con un errore di battitura, caricare il portafoglio con bitcoin e poi un giorno potresti aver bisogno di ripristinare il portafoglio, ma quando lo fai, non ricreerai l'errore di battitura: ripristinerai il portafoglio sbagliato! È piuttosto pericoloso che Electrum ti permetta di procedere con la creazione di un portafoglio se il checksum non è valido, quindi fai attenzione, è tua responsabilità assicurarti. Altri portafogli non ti permetteranno di procedere, il che è molto più sicuro. Questo è uno dei motivi per cui dico che Electrum è sicuro da usare, una volta che impari ad usarlo correttamente (gli sviluppatori di Electrum dovrebbero risolvere questo problema).

Nota che se desideri aggiungere una passphrase, la possibilità di selezionarla si trova in questa finestra delle opzioni, proprio in alto.

Dopo aver fatto clic su OK, verrai riportato alla schermata in cui hai digitato la frase del seme. Se hai selezionato un'opzione di passphrase, NON la inserisci insieme alle parole del seme (la richiesta per quella arriva dopo).

Se non hai richiesto una passphrase, vedrai questa schermata successiva: ulteriori opzioni per il tipo di script del tuo portafoglio e il percorso di derivazione, che puoi imparare qui (https://armantheparman.com/public-and-private-keys/), ma lascia semplicemente i valori predefiniti e procedi.

![image](assets/13.png)

> Per ulteriori informazioni: la prima opzione ti consente di scegliere tra legacy (indirizzi che iniziano con "1"), pay-to-script-hash (indirizzi che iniziano con "3") o bech32/native segwit (indirizzi che iniziano con "bc1q"). Al momento della stesura, Electrum non supporta ancora taproot (indirizzi che iniziano con "bc1p"). La seconda opzione in questa finestra ti consente di modificare il percorso di derivazione. Ti consiglio di non modificarlo mai, soprattutto prima di capire cosa significa. Le persone sottolineeranno l'importanza di scrivere il percorso di derivazione in modo da poter recuperare il tuo portafoglio se necessario, ma se lo lasci come predefinito, probabilmente andrà tutto bene, quindi non preoccuparti, ma è comunque una buona pratica scrivere il percorso di derivazione.

Successivamente, ti verrà data la possibilità di aggiungere una PASSWORD. Questa non deve essere confusa con "PASSPHRASE". Una password blocca il file sul tuo computer. Una passphrase fa parte della composizione della chiave privata. Poiché si tratta di un portafoglio fittizio, puoi lasciare la password vuota e procedere.

![image](assets/14.png)

Riceverai una finestra pop-up riguardo alle notifiche delle nuove versioni (ti consiglio di selezionare no). Il portafoglio si genererà quindi da solo e sarà pronto all'uso (ma ricorda, questo portafoglio è destinato ad essere eliminato, è solo un portafoglio fittizio).

![image](assets/15.png)

Ci sono alcune cose che ti suggerisco di fare per configurare l'ambiente software (richiesto solo una volta):

### Cambia le unità in BTC

Vai al menu in alto, strumenti -> preferenze di Electrum, e lì nella scheda generale, troverai l'opzione per cambiare l'"unità di base" in BTC.
Abilita la scheda Indirizzi e Monete

Vai al menu in alto, visualizza, e seleziona "mostra indirizzi". Poi torna a visualizza e seleziona "mostra monete".

### Abilita Oneserver

Di default, Electrum si connette a un nodo casuale. Si connette anche a molti altri nodi secondari. Non sono sicuro di quali dati vengano scambiati con questi nodi secondari, ma non vogliamo che ciò accada, per motivi di privacy. Anche se specifici un nodo, ad esempio il tuo nodo personale, questi molti altri nodi saranno comunque connessi, e non sono sicuro di quali informazioni vengano condivise. Tuttavia, è facile prevenirlo. Prima di mostrarti come specificare il tuo nodo personale, forzeremo Electrum a connettersi solo a un server alla volta.

> C'è un modo per farlo specificando "oneserver" dalla riga di comando, ma non raccomando questa modalità. Mostrerò un'alternativa che ritengo più semplice a lungo termine e meno probabile di farti connettere accidentalmente ad altri nodi.

Il motivo per cui stiamo usando un portafoglio fittizio è che se avessimo caricato il nostro vero portafoglio, con i nostri veri bitcoin, avremmo già involontariamente stabilito una connessione con un nodo casuale (anche se abbiamo selezionato "imposta server manualmente" all'inizio, si connette comunque a questi altri nodi secondari per qualche motivo (ehi sviluppatori di Electrum, dovreste risolvere questo problema). Se il nostro portafoglio fosse privato, sarebbe un disastro.

Inoltre, non possiamo eseguire i passaggi che ti mostrerò di seguito senza prima caricare un qualche tipo di portafoglio. (Stiamo per modificare un file di configurazione che viene popolato e pronto per la modifica solo una volta caricato un portafoglio).

**Chiudi Electrum (IMPORTANTE, se non lo fai, le modifiche che apporterai verranno cancellate).**

### File di configurazione LINUX/MAC

Apri il terminale in Linux o Mac (istruzioni per Windows in seguito):

Dovresti trovarsi automaticamente nella cartella home. Da lì, vai alla cartella delle impostazioni nascoste di Electrum (questa è diversa rispetto alla posizione dell'applicazione).

```
cd .electrum
```

Nota il punto prima di "electrum" che indica che si tratta di una cartella nascosta.

Un altro modo per arrivarci è digitare:

```
cd ~/.electrum
```

dove "~" rappresenta il percorso della tua cartella home. Puoi vedere il percorso completo della tua directory corrente con il comando "pwd".

Una volta nella directory ".electrum", digita "nano config" e premi <invio>.

Si aprirà un editor di testo (chiamato nano) con il file di configurazione aperto. Il mouse non funziona molto qui. Usa i tasti freccia per arrivare alla riga che dice:

```
"oneserver": false,
```

Cambia "false" in "true"; e non disturbare la sintassi (non eliminare la virgola o il punto e virgola).

Premi <ctrl> x, per uscire, poi "y" per salvare, poi <invio> per confermare la modifica senza modificare il nome del file.
Ora esegui di nuovo Electrum. Quindi clicca sul cerchio in basso a destra, che apre le impostazioni di rete. Poi, nella scheda panoramica in alto, vedrai "connesso a 1 nodo" - questo indica il successo.
Appena sotto, vedrai un campo di testo e l'indirizzo del server è lì. Attualmente sei connesso a quel nodo casuale. Maggiori informazioni sulla connessione a un nodo nella prossima sezione.

### File di configurazione di Windows

Il file di configurazione di Windows è un po' più difficile da trovare. La directory è:

```
C:/Users/Parman/AppData/Roaming/Electrum
```

Ovviamente, devi cambiare "Parman" con il tuo nome utente per il computer.

In quella cartella troverai il file di configurazione. Aprilo con un editor di testo e modifica la riga:

```
"oneserver": false,
```

Cambia "false" in "true"; non disturbare la sintassi (non eliminare la virgola o il punto e virgola).

Salva quindi il file ed esci.

## Connetti Electrum a un nodo

Successivamente, vogliamo connettere il nostro portafoglio fittizio a un nodo a nostra scelta. Se non sei pronto per eseguire un nodo, puoi fare una delle seguenti cose:

1. Connetti a un nodo personale di un amico (richiede Tor)
2. Connetti a un nodo di un'azienda affidabile
3. Connetti a un nodo casuale (non consigliato).

A proposito, ecco le istruzioni per eseguire il tuo nodo e queste sono le ragioni per cui dovresti farlo (tutti i tutorial nella sezione Nodo o nei nostri corsi gratuiti).

### Connetti al nodo di un amico tramite Tor (Guida in arrivo.)

### Connetti a un nodo di un'azienda affidabile

L'unico motivo per farlo sarebbe se devi accedere alla blockchain e non hai a disposizione il tuo nodo (o quello di un amico).

Connettiamoci al nodo di Bitaroo - Ci dicono che non raccolgono dati. Sono uno scambio solo Bitcoin, gestito da un appassionato di Bitcoin. Connettersi a loro richiede un po' di fiducia, ma è meglio che connettersi a un nodo casuale, che potrebbe essere una società di sorveglianza.

Accedi alle impostazioni di rete cliccando sul cerchio nella parte inferiore destra della finestra del portafoglio (il rosso indica non connesso, il verde indica connesso e il blu indica connesso tramite Tor).

![image](assets/16.png)

Una volta cliccato sull'icona del cerchio, apparirà una finestra popup: Il tuo portafoglio mostrerà "connesso a 1 nodo" poiché l'abbiamo forzato in precedenza.

Deseleziona la casella "seleziona server automaticamente" e quindi nel campo Server, digita i dettagli di Bitaroo come mostrato:

![image](assets/17.png)

Chiudi la finestra e ora dovremmo essere connessi al nodo di Bitaroo. Per confermare, il cerchio dovrebbe essere verde. Cliccaci di nuovo e controlla che i dettagli del server non siano tornati a un nodo casuale.

### Connetti al tuo nodo

Se hai il tuo nodo è fantastico. Se hai solo Bitcoin Core e non anche un SERVER Electrum, non sarai ancora in grado di connettere un PORTAFOGLIO Electrum al tuo nodo.

> Nota: Electrum Server e Electrum Wallet sono cose diverse. Il server è un software necessario affinché il portafoglio Electrum possa comunicare con la blockchain di Bitcoin - Non so perché sia stato progettato in questo modo - forse per velocità, ma potrei sbagliarmi.
>
> Se esegui un pacchetto software di nodo come MyNode (quello che consiglio alle persone di iniziare), Raspiblitz (consigliato quando diventi più esperto) o Umbrel (personalmente non lo consiglio ancora perché ho riscontrato troppi problemi), allora sarai in grado di connettere il tuo portafoglio semplicemente inserendo l'indirizzo IP del computer (Raspberry Pi) su cui viene eseguito il nodo, seguito da due punti e 50002, come mostrato nell'immagine nella sezione precedente. (Più avanti ti mostrerò come trovare l'indirizzo IP del tuo nodo).

Apri le impostazioni di rete (clicca sul cerchio verde o rosso in basso a destra). Deseleziona la casella "seleziona server automaticamente", quindi inserisci il tuo indirizzo IP come ho fatto io, il tuo sarà diverso, ma i due punti e "50002" dovrebbero essere gli stessi.

![image](assets/18.png)

Chiudi la finestra e ora dovremmo essere connessi al tuo nodo. Per confermare, clicca nuovamente sul cerchio e verifica che i dettagli del server non siano tornati a essere un nodo casuale.

A volte, nonostante si faccia tutto correttamente, sembra rifiutarsi di connettersi. Ecco alcune cose da provare...

- Aggiorna a una versione più recente di Electrum e del tuo software di nodo
- Prova a eliminare la cartella della cache nella directory ".electrum"
- Prova a cambiare la porta da 50002 a 50001 nelle impostazioni di rete
- Utilizza questa guida per connetterti utilizzando Tor come alternativa (https://armantheparman.com/tor/)
- Reinstalla il server Electrum sul nodo

## TROVARE L'INDIRIZZO IP DEL TUO NODO

Un indirizzo IP non è qualcosa che un utente comune sa come cercare e utilizzare. Ho aiutato molte persone a eseguire un nodo e poi a connettere i loro portafogli al nodo - un ostacolo spesso sembra essere la ricerca del suo indirizzo IP.

Per MyNode, puoi digitare nella finestra del browser:

```
mynode.local
```

A volte, "mynode.local" non funziona (assicurati di non digitarlo nella barra di ricerca di Google). Per far sì che la barra di navigazione riconosca il tuo testo come un indirizzo e non come una ricerca, precedi il testo con http://

così:

```
http://mynode.local
```

se ciò non funziona, prova con una "s", così:

```
https://mynode.local
```

In questo modo accederai al dispositivo e potrai fare clic sul collegamento delle impostazioni (vedi il mio "cerchio" blu sotto) per mostrare questa schermata in cui è presente l'indirizzo IP:

![image](assets/19.png)

Questa pagina si caricherà e vedrai l'IP del nodo (cerchio blu).

![image](assets/20.png)

Quindi, in futuro, puoi digitare 192.168.0.150 o http://192.168.0.150 nel tuo browser.

Per il Raspiblitz (quando non si è collegati a uno schermo), è necessario un metodo diverso (che funziona anche per MyNode):

Accedi alla pagina web del tuo router: qui troveremo l'indirizzo IP di tutti i dispositivi connessi. La pagina web del router sarà un indirizzo IP che inserisci in un browser web. Il mio aspetto è:

> http://192.168.0.1

Per ottenere le credenziali di accesso al router, puoi trovarle nel manuale utente o talvolta persino su un adesivo sul router stesso. Cerca il nome utente e la password. Se non riesci a trovarli, prova con Utente: "admin" Password: "password"
Se sei in grado di effettuare l'accesso, vedrai i tuoi dispositivi connessi e dai loro nomi potrebbe essere chiaro quale sia il tuo nodo. L'indirizzo IP sarà presente.

### Se i primi due metodi falliscono, l'ultimo funzionerà ma è noioso:

Prima di tutto, trova l'indirizzo IP di qualsiasi dispositivo sulla tua rete (il computer attuale va bene).

Su un Mac, lo troverai nelle preferenze di Rete:

![image](assets/21.png)

Siamo interessati ai primi 4 elementi (192.168.0), non al 4° elemento, il "166" che vedi nell'immagine (il tuo sarà diverso).

Per Linux, usa la riga di comando:

```
ifconfig | grep inet
```

Quella linea verticale è il simbolo "pipe" e lo troverai sotto il tasto <delete>. Vedrai un output e un indirizzo IP. (Ignora 127.0.0.1, non è quello, e ignora la netmask)

Per Windows, apri il prompt dei comandi (cmd) e digita:

```
ipconfig/all
```

e premi Invio. L'indirizzo IP si trova nell'output.

Quella era la parte facile. La parte difficile è ora trovare l'indirizzo IP del tuo nodo: dobbiamo fare una supposizione forzata. Supponiamo ad esempio che l'indirizzo IP del tuo computer inizi con 192.168.0.xxx, quindi per il tuo nodo, nel browser, prova:

```
https://192.168.0.2
```

Il numero più piccolo possibile è 2 (0 significa qualsiasi dispositivo e 1 appartiene al router) e il più alto, credo sia 255 (questo corrisponde a 11111111 in binario, il numero più grande rappresentabile da 1 byte).

Uno per uno, procedi verso l'alto fino a 255. Alla fine, ti fermerai al numero corretto che carica la tua pagina MyNode (o la pagina RaspiBlitz). Allora saprai quale numero inserire nelle impostazioni di rete di Electrum per connetterti al tuo nodo.

Avrà un aspetto simile a questo (assicurati di includere i due punti e il numero successivo):

![image](assets/22.png)

> È utile sapere che questi indirizzi IP sono INTERNI alla tua rete domestica. Nessuno all'esterno può vederli e non sono sensibili. Sono un po' come le estensioni telefoniche in un'organizzazione grande che ti indirizzano a telefoni diversi.

## Elimina il portafoglio fittizio

Ora ci siamo collegati con successo a un solo nodo. Questo è come Electrum si caricherà di default da ora in poi. Dovresti ora eliminare il portafoglio fittizio (Menu: file -> elimina), nel caso in cui invii accidentalmente fondi a questo portafoglio non sicuro (non è sicuro perché non l'abbiamo creato in modo sicuro).

## Crea un portafoglio di pratica

Dopo aver eliminato il portafoglio fittizio, ricomincia e ne crea uno nuovo, allo stesso modo, solo che questa volta, annota le parole del seed e tienile abbastanza al sicuro.

È una buona idea imparare come Electrum funziona con questo portafoglio di pratica, senza l'ingombrante portafoglio hardware (necessario per una sicurezza elevata). Metti solo una piccola quantità di bitcoin in questo portafoglio - Supponi che perderai questi soldi. Una volta diventato esperto, impara ad usare Electrum con un portafoglio hardware.

Nel nuovo portafoglio che hai creato, vedrai un elenco di indirizzi. Quelli verdi sono chiamati "indirizzi di ricezione". Sono il prodotto di 3 cose:

- La frase del seed
- La passphrase
- Il percorso di derivazione

Il tuo nuovo portafoglio ha un insieme di indirizzi di ricezione che possono essere creati in modo matematico e riproducibile da qualsiasi portafoglio software che abbia il seed, la passphrase e il percorso di derivazione. Ce ne sono 4,3 miliardi! Più di quanti ne avrai bisogno. Electrum ti mostra solo i primi 20, e poi di più man mano che li utilizzi.
Ulteriori informazioni sulle chiavi private di Bitcoin possono essere trovate in questa guida.

![image](assets/23.png)

Questo è molto diverso da alcuni altri portafogli che presentano solo un indirizzo alla volta.

Poiché hai inserito la frase seed nella creazione di questo portafoglio, Electrum ha la chiave privata per ciascuno degli indirizzi e la spesa da questi indirizzi è possibile.

Nota anche che ci sono indirizzi gialli, chiamati "indirizzi di cambio" - Questi sono solo un altro insieme di indirizzi di un diverso ramo matematico (ne esistono altri 4,3 miliardi). Sono utilizzati dal portafoglio per inviare automaticamente i fondi in eccesso nel portafoglio come resto. Ad esempio, se prendi 1,5 bitcoin e ne spendi 0,5 a un commerciante, il resto di 1,0 deve andare da qualche parte. Il tuo portafoglio lo spenderà all'indirizzo di cambio giallo vuoto successivo, altrimenti andrà al minatore! Per ulteriori informazioni su questo (UTXOs) consulta questa guida. (https://armantheparman.com/utxo/)

Successivamente, torna al sito delle chiavi private di Ian Colman e inserisci il seed (anziché generarne uno). Vedrai che le informazioni sulla chiave privata e pubblica cambiano; tutto ciò che segue dipende dalle cose sopra nella pagina.

> Ricorda, non dovresti "mai" inserire il seed su un computer per il tuo vero portafoglio Bitcoin - il malware può rubarlo. Stiamo solo usando un portafoglio di pratica, per scopi di apprendimento, quindi va bene per ora.

Scorri verso il basso e cambia il percorso di derivazione in BIP84 (segwit) per abbinarlo al tuo portafoglio Electrum cliccando sulla scheda BIP84.

![image](assets/24.png)

Sotto, vedrai la chiave privata estesa dell'account e la chiave pubblica estesa dell'account:

![image](assets/25.png)

Vai su Electrum e confronta che corrispondano. C'è un menu in alto, portafoglio -> informazioni:

![image](assets/26.png)

Questo compare:

![image](assets/27.png)

Nota che le due chiavi pubbliche corrispondono.

Successivamente, confronta gli indirizzi. Torna al sito di Ian Coleman e scorri fino in fondo:

![image](assets/28.png)

Nota che corrispondono agli indirizzi in Electrum.

Ora verificheremo gli indirizzi di cambio. Scorri un po' verso l'alto fino al percorso di derivazione e cambia l'ultimo 0 in un 1:

![image](assets/29.png)

Ora scorri verso il basso e confronta che gli indirizzi corrispondano agli indirizzi gialli in Electrum.

Perché abbiamo fatto tutto questo?

Abbiamo preso le parole seed e le abbiamo inserite in due diversi programmi software indipendenti per assicurarci che ci stessero dando le stesse informazioni. Questo riduce significativamente il rischio che un codice malintenzionato si nasconda all'interno e ci dia false chiavi private o pubbliche, o indirizzi.

La prossima cosa da fare è ricevere un piccolo test e spenderlo all'interno del portafoglio da un indirizzo a un altro.

## Testare il portafoglio (Impara ad usarlo)

Qui ti mostrerò come ricevere un UTXO nel tuo portafoglio e poi spostarlo (spenderlo) in un altro indirizzo all'interno del portafoglio. Si tratta di una quantità molto piccola che non ci dispiacerebbe rischiare di perdere.

Questo ha diversi scopi.

- Dimostrerà che hai il potere di spendere monete nel nuovo portafoglio.
- Dimostrerà come utilizzare il software Electrum per effettuare una spesa (e alcune funzionalità), prima di aggiungere ulteriori complessità per la sicurezza (utilizzando un portafoglio hardware o un computer air-gapped).
- Rinforzerà l'idea che hai molteplici indirizzi tra cui scegliere per ricevere e spendere, all'interno dello stesso portafoglio.

Apri il tuo test Electrum Wallet e clicca sulla scheda Indirizzi, quindi fai clic con il pulsante destro del mouse sul primo indirizzo e seleziona Copia -> Indirizzo:

![image](assets/30.png)

L'indirizzo è ora nella memoria del tuo computer.

Ora vai su un exchange dove hai alcuni bitcoin e preleva una piccola quantità su questo indirizzo, diciamo 50.000 sats. Userò Coinbase come esempio perché è l'exchange più comunemente utilizzato, anche se sono nemici di Bitcoin e mi disgusta accedere a un vecchio account abbandonato per questo scopo.

Accedi e fai clic sul pulsante Invia/Ricevi, che oggi si trova nell'angolo in alto a destra della pagina web.

![image](assets/31.png)

Ovviamente non ho fondi su Coinbase, ma immagina solo che ci siano fondi qui e segui il procedimento: Incolla l'indirizzo da Electrum nel campo "A" come ho fatto io. Dovrai anche selezionare una quantità (suggerisco circa 50.000 sats). Non inserire un "messaggio opzionale" - Coinbase sta già raccogliendo abbastanza dei tuoi dati (e li sta vendendo), non c'è bisogno di aiutarli. Infine, fai clic su "Continua". Dopo di ciò, non so quali altre finestre popup potresti ricevere, sei da solo, ma il metodo è simile per tutti gli exchange.

![image](assets/32.png)

A seconda dell'exchange, potresti vedere i sats nel tuo portafoglio immediatamente o potrebbe esserci un ritardo di ore/giorni.

Nota che Electrum ti mostrerà le monete ricevute anche se non sono state confermate sulla blockchain. Le monete che hai vengono lette dalla lista di attesa di un nodo Bitcoin, o "mempool". Quando viene inserito in un blocco, vedrai i fondi come confermati.

Ora che abbiamo un UTXO nel nostro portafoglio, dovremmo etichettarlo. Solo noi possiamo vedere questa etichetta, non ha nulla a che fare con il registro pubblico. Tutte le nostre etichette Electrum sono visibili solo sul computer che stiamo utilizzando. Possiamo effettivamente salvare un file e usarlo per ripristinare tutte le nostre etichette su un computer diverso che esegue lo stesso portafoglio.

### Crea un'etichetta per un UTXO

Avevo bisogno di una donazione per questo portafoglio di prova, grazie a @Sathoarder per avermi fornito un UTXO attivo (10.000 sats), e un'altra persona (anonima) ha donato allo stesso indirizzo (5000 sats). Nota che ci sono 15.000 sats nel saldo del primo indirizzo e un totale di 2 transazioni (colonna di destra). In fondo, il saldo è di 10.000 sats confermati e altri 5.000 sats sono non confermati (ancora nella mempool).

![image](assets/33.png)

Ora, se andiamo alla scheda Monete, possiamo vedere due "monete ricevute" o UTXO. Sono entrambi nello stesso indirizzo.

![image](assets/34.png)

Tornando alla scheda Indirizzi, se fai doppio clic sull'area "etichette" accanto all'indirizzo, potrai inserire del testo e premere <invio> per salvare:

![image](assets/35.png)
Questa è una buona pratica per tenere traccia di dove provengono le tue monete, se sono KYC-free o meno e quanto costa ogni UTXO (nel caso in cui tu abbia bisogno di venderle e calcolare le tasse che ti verranno sottratte dal governo).

Idealmente, dovresti evitare di accumulare più monete nello stesso indirizzo. Se decidi di farlo (non farlo), puoi etichettare ogni moneta invece di tutte con la stessa etichetta utilizzando il metodo dell'indirizzo. Non puoi effettivamente andare alla scheda "monete" ed editare le etichette lì (no, sarebbe troppo intuitivo!). Devi andare alla scheda Cronologia, trovare la transazione, etichettarla e poi vedrai le etichette nella sezione delle monete. Le etichette che vedi nella sezione delle monete provengono dalle etichette degli indirizzi O dalle etichette della cronologia, ma qualsiasi etichetta della cronologia sovrascrive qualsiasi etichetta dell'indirizzo. Per fare il backup delle tue etichette su un file, puoi esportarle dal menu in alto, portafoglio -> etichette -> esporta.

Successivamente, spendiamo le monete dal primo indirizzo al secondo indirizzo. Fai clic con il pulsante destro del mouse sul primo indirizzo e seleziona "spendere da" (in realtà non è necessario in questo scenario, ma immagina di avere molte monete in molti indirizzi; utilizzando questa funzione, possiamo forzare il portafoglio a spendere solo le monete che vogliamo. Se vogliamo selezionare più monete in più indirizzi, possiamo selezionare gli indirizzi con un clic del mouse sinistro tenendo premuto il tasto comando, quindi fare clic con il pulsante destro del mouse e selezionare "spendere da"):

![image](assets/36.png)

Una volta fatto ciò, ci sarà una barra verde in fondo alla finestra del portafoglio che indica il numero di monete che hai selezionato e il totale disponibile da spendere.

Puoi anche spendere monete singole all'interno di un indirizzo ed escluderne altre nello stesso indirizzo, ma questo è sconsigliato perché stai lasciando monete in un indirizzo che è stato indebolito criptograficamente a causa della spesa di una delle monete (un'altra ragione per non mettere più monete in un unico indirizzo, oltre alle ragioni di privacy, è che dato che dovresti spenderle tutte se ne spendi una, questo diventa costoso inutilmente). Ecco come selezionare una singola moneta da un indirizzo condiviso, ma non farlo:

![image](assets/37.png)

Ora, abbiamo selezionato le due monete da spendere. Successivamente, decidiamo dove spenderle. Inviamole al secondo indirizzo. Dovremo copiare l'indirizzo in questo modo:

![image](assets/38.png)

Quindi vai alla scheda "Invia" e incolla il secondo indirizzo nel campo "pagare a". Non è necessario aggiungere una descrizione; potresti farlo, ma puoi farlo in seguito modificando le etichette. Per l'importo, seleziona "Max" per spendere tutte le monete che abbiamo selezionato. Quindi clicca su "Paga" e poi clicca sul pulsante "avanzate" nella finestra popup che appare.

![image](assets/39.png)

Clicca sempre su "avanzate" in questa fase in modo da poter avere un controllo preciso e verificare esattamente cosa c'è nella transazione. Ecco la transazione:

![image](assets/40.png)

Vediamo due finestre/box bianche interne. Quella superiore è la finestra degli input (quali monete vengono spese) e quella inferiore è gli output (dove vanno le monete).
Nota, lo stato (in alto a sinistra) è "non firmato" per ora. L'"Importo inviato" è 0 perché le monete vengono trasferite all'interno del portafoglio. La commissione è di 481 sats. Nota che se fossero stati 480 sats, lo zero finale sarebbe stato omesso, come questo, 0.0000048 e per l'occhio stanco, questo può sembrare 48 sats - fai attenzione (qualcosa che gli sviluppatori di Electrum dovrebbero correggere).
La dimensione della transazione si riferisce alla dimensione dei dati in byte, non all'importo di bitcoin. Il "sostituisci con commissione" è attivo per impostazione predefinita e ti consente di inviare nuovamente la transazione con una commissione più alta se necessario. Il LockTime ti consente di regolare quando la transazione è valida - non ho ancora giocato con quello, ma consiglio di non usarlo a meno che non comprendi appieno cosa stai facendo e hai avuto un po' di pratica con piccole quantità.

In fondo, abbiamo alcuni strumenti di regolazione delle commissioni di mining di fantasia. Tutto ciò che devi fare per i trasferimenti interni è impostarlo alla commissione minima di 1 sat/byte. Digita manualmente il numero nel campo della commissione target. Per verificare una commissione appropriata per un pagamento esterno, puoi consultare https://mempool.space per vedere quanto è occupato il mempool e vengono visualizzate alcune commissioni suggerite.

![image](assets/41.png)

Ho selezionato 1 sat/byte.

Nella finestra di input, vediamo due voci. La prima è la donazione di 5000 sat. Vediamo a sinistra il suo hash di transazione (che possiamo cercare sulla blockchain). Accanto ad esso, c'è un "21" - questo indica che è l'output etichettato come 21 in quella transazione (in realtà è il 22° output perché il primo è etichettato come zero).

Qualcosa da notare qui: gli UTXO esistono solo all'interno di una transazione. Per spendere un UTXO dobbiamo fare riferimento ad esso e mettere quel riferimento nell'input di una nuova transazione. Gli output diventano quindi nuovi UTXO e il vecchio UTXO diventa uno STXO (output di transazione speso).

La seconda riga è la donazione di 10.000 sat. Ha un "0" accanto all'hash di transazione da cui proviene perché è il primo (e forse unico) output per quella transazione.

Nella finestra inferiore, vediamo il nostro indirizzo. Nota che il totale di bitcoin degli input non corrisponde esattamente al totale degli output. La differenza va al minatore. Il minatore osserva la discrepanza in tutte le transazioni nel blocco che sta cercando di minare e aggiunge quel numero alla sua ricompensa. (Le commissioni di mining in questo modo sono completamente slegate dalla catena di transazioni e iniziano una nuova vita).

Se regoliamo la commissione di mining, il valore dell'output cambierà automaticamente.

> Vale la pena sottolineare qui: nota il colore degli indirizzi nella finestra di transazione. Ricorda che gli indirizzi verdi sono elencati nella scheda degli indirizzi. Se un indirizzo è evidenziato in verde (o giallo) in una finestra di transazione, allora Electrum ha riconosciuto l'indirizzo come uno dei suoi. Se l'indirizzo non ha evidenziazione, allora è un indirizzo esterno (esterno al portafoglio attualmente aperto) e dovresti controllarlo con particolare attenzione.

Una volta che hai controllato tutto nella transazione e sei sicuro di essere soddisfatto delle monete che stai spendendo e di dove stanno andando, puoi fare clic su "finalizza".

![image](assets/42.png)

Dopo aver cliccato su "finalizza", non è più possibile apportare modifiche: se ne hai bisogno, devi chiudere questa finestra e ricominciare da capo. Nota che il pulsante "finalizza" è cambiato in "esporta" e sono comparsi nuovi pulsanti: "salva", "combina", "firma" e "trasmetti". Il pulsante "trasmetti" è disattivato perché la transazione non è firmata e quindi non valida in questa fase.
Una volta che hai cliccato su "firma", se hai una password per il portafoglio, ti verrà richiesta e lo stato (in alto a destra) passerà da "non firmata" a "firmata". A questo punto, il pulsante "trasmetti" sarà disponibile.

Dopo aver trasmesso, puoi chiudere la finestra della transazione. Se vai alla scheda degli indirizzi, vedrai che il primo indirizzo è vuoto e il secondo indirizzo ha 1 UTXO.

Nota: Vedrai tutti questi cambiamenti anche prima che la transazione venga inserita in un blocco o "confermata". Questo perché Electrum aggiorna i saldi/le transazioni non solo in base ai dati della blockchain, ma anche ai dati della mempool. Non tutti i portafogli fanno questo.

Qualcosa da sottolineare è che invece di trasmettere, possiamo salvare la transazione per dopo. Può essere salvata sia nello stato non firmato che in quello firmato.

Clicca sul pulsante "esporta" (paradossalmente, NON cliccare sul pulsante "salva") e vedrai una serie di opzioni. La transazione è codificata con del testo e quindi può essere salvata in diversi modi.

![image](assets/43.png)

Salvare in un codice QR è molto interessante. Se scegli questa opzione, apparirà un codice QR:

![image](assets/44.png)

Puoi quindi fare una foto del codice QR. Ci sono diverse cose che puoi fare con questo, ma per ora diciamo solo che lo stai caricando di nuovo nel portafoglio in seguito. Puoi chiudere Electrum, caricare di nuovo il portafoglio e andare al menu Strumenti:

![image](assets/45.png)

Questo aprirà la fotocamera del tuo computer. Mostra quindi alla fotocamera la foto del codice QR sul tuo telefono e la transazione verrà caricata di nuovo, esattamente come l'hai lasciata.

Non è intuitivo come caricare transazioni salvate, quindi fai attenzione. Caricare una transazione non è uno "strumento", ma l'opzione è nascosta nel menu Strumenti (un'altra cosa che gli sviluppatori di Electrum dovrebbero sistemare).

Un processo simile è possibile con una transazione salvata come file. Prova a esercitarti con uno dei due metodi, all'interno dello stesso portafoglio. Non lo spiegherò qui, ma puoi utilizzare questa funzione per passare una transazione tra lo stesso portafoglio su computer diversi, tra portafogli multi-firma e da e verso portafogli hardware. Ecco alcune istruzioni.

Ora, tornando al pulsante "salva": questo non serve a salvare il testo della transazione. In realtà, dice al portafoglio Electrum di riconoscere questa transazione sul computer locale come un pagamento effettuato. Se lo fai per errore, vedrai la transazione con un'icona di un computer. Puoi fare clic destro e cancellare la transazione: non preoccuparti, non puoi cancellare i bitcoin in questo modo. Electrum dimenticherà quindi che questa transazione è mai avvenuta e "rimborserà" i satoshi e li mostrerà nella posizione corretta in cui si trovano effettivamente.

### Indirizzi di cambio

Gli indirizzi di cambio sono interessanti. Devi capire gli UTXO per comprendere questa spiegazione. Se stai spendendo verso un indirizzo una quantità inferiore all'UTXO, allora i bitcoin rimanenti andranno al minatore a meno che non venga specificato un output di cambio.
Potresti avere un UTXO di 6,15 bitcoin e desiderare di spendere 0,15 bitcoin per donare a dei manifestanti oppressi da un governo "democratico" tirannico in qualche parte del mondo. Prenderesti quindi i 6,15 bitcoin (utilizzando la funzione "spend from" in Electrum) e li inseriresti in una transazione.

Incolleresti l'indirizzo dei manifestanti nel campo "pay to", forse inseriresti "EndTheFed & WEF" nel campo "description" e per l'importo inseriresti 0,15 bitcoin e cliccheresti su "pay", quindi su "advanced".

Nella schermata della transazione, nella finestra di input, vedresti il 6,15 bitcoin UTXO. Nella finestra di output, vedresti un indirizzo senza evidenziazione (questo è l'indirizzo dei manifestanti) con accanto 0,15 bitcoin. Vedresti anche un indirizzo giallo con leggermente meno di 6,0 bitcoin. Questo è l'indirizzo di cambio selezionato automaticamente dal portafoglio da uno dei suoi stessi indirizzi di cambio gialli. Lo scopo dell'indirizzo di cambio è consentire al portafoglio di mettere monete di cambio al suo interno senza compromettere la disponibilità degli indirizzi di ricezione che potresti avere in programma o per cui hai inviato fatture. Se ad esempio verranno utilizzati successivamente dai clienti, non vuoi che il tuo portafoglio li utilizzi automaticamente e li riempia. È disordinato e dannoso per la privacy.

Nota che, mentre regoli la tassa di mining, l'importo dell'output di cambio si regolerà automaticamente, non l'importo del pagamento.

### Cambio manuale o pagamento a molti

Questa è una caratteristica davvero interessante di Electrum. Puoi accedervi in questo modo.

![image](assets/46.png)

Puoi quindi inserire più destinazioni per il saldo UTXO che stai spendendo, come questo:

![image](assets/47.png)

Incolla l'indirizzo, digita una virgola, quindi uno spazio, quindi l'importo, quindi <invio>, quindi fallo di nuovo. NON INSERIRE GLI IMPORTI NELLE FINESTRE "AMOUNT" - Electrum popolerà il totale qui mentre digiti gli importi singoli nella finestra "Pay to".

Ciò ti consente di determinare manualmente dove va il cambio (ad esempio un indirizzo specifico nel tuo portafoglio o un altro portafoglio), oppure puoi pagare molte persone contemporaneamente. Se il tuo totale non è sufficientemente alto per corrispondere alla dimensione dell'UTXO, Electrum creerà comunque un output di cambio aggiuntivo per te.

La funzione Pay to Many consente anche la possibilità di creare i tuoi "PayJoins" o "CoinJoins" - al di fuori dello scopo di questo articolo, ma ho una guida qui. (https://armantheparman.com/cj/)

## Portafogli

Voglio dimostrare un portafoglio Solo Visualizzazione utilizzando Electrum. Per farlo, devo prima definire "portafoglio". Ci sono due modi in cui "portafoglio" viene utilizzato in Bitcoin:

- Tipo A, "portafoglio" - si riferisce al software che mostra gli indirizzi e i saldi, ad esempio Electrum, Blue Wallet, Sparrow Wallet, ecc.

- Tipo B, "portafoglio" - si riferisce alla collezione unica di indirizzi associati alla combinazione del nostro seed_phrase/passphrase/derivation_path. Ci sono 8,6 miliardi di indirizzi in ogni portafoglio (4,3 miliardi di indirizzi di ricezione e 4,3 miliardi di indirizzi di cambio). Se cambi qualcosa nel seed phrase, passphrase o derivation path, ottieni un nuovo portafoglio inutilizzato con nuovi e tutti unici 8,6 miliardi di indirizzi vuoti.

Quale tipo si sta riferendo quando si utilizza la parola "portafoglio" è ovvio nel contesto.

## Portafoglio Solo Visualizzazione - un esercizio

Non è del tutto ovvio a cosa serve un portafoglio di osservazione, ma inizierò spiegando cos'è, come crearne uno di prova e poi torneremo al suo scopo più avanti quando spiegherò di più sui portafogli hardware. (Per una recensione approfondita su come utilizzare un portafoglio hardware e varie marche specifiche, vedi qui.)
Creeremo un portafoglio regolare fittizio (questa volta aggiungendo un po' più di complessità con una frase segreta) e poi il corrispondente portafoglio di osservazione. Se vuoi, puoi copiare esattamente quello che ho fatto io o crearne uno tuo: questo portafoglio deve essere scartato, non utilizzarlo effettivamente. Inizia generando un seme di 12 parole utilizzando il sito di Ian Coleman.

Osserva le 12 parole casuali nella schermata sottostante e che ho inserito una frase segreta nel campo della frase segreta:

FRASE SEGRETA: "Craig Wright è un bugiardo e un truffatore e dovrebbe essere in prigione. Inoltre, Ross Ulbricht dovrebbe essere rilasciato immediatamente dal carcere."

La frase segreta può essere lunga fino a 100 caratteri e idealmente dovrebbe essere inequivocabile e non troppo breve. Quella che ho usato io è solo per divertimento. In generale, suggerisco di evitare lettere maiuscole e simboli solo per ridurre lo stress nel tentativo di combinazioni se hai mai avuto problemi a ricordare la tua frase segreta.

![image](assets/48.png)

Successivamente, in Electrum, vai al menu file->nuovo/ripristina. Digita un nome univoco per creare un nuovo portafoglio e clicca su "avanti".

![image](assets/49.png)

I passaggi successivi dovresti conoscerli ormai, quindi li elencherò senza immagini:

- Portafoglio standard
- Ho già un seme
- Copia e incolla le 12 parole nella casella o inseriscile manualmente.
- Clicca su "opzioni" e seleziona BIP39, e clicca anche sulla spunta della frase segreta ("estendi questo seme con parole personalizzate")
- Inserisci la tua frase segreta esattamente come hai fatto sulla pagina di Ian Coleman
- Lascia le impostazioni predefinite per il semantica dello script e il percorso di derivazione
- Non è necessario aggiungere una password (blocca il portafoglio)

Ora torna al sito di Ian Coleman, nella sezione "percorso di derivazione", e clicca sulla scheda "BIP 84" per selezionare la stessa semantica dello script predefinita in Electrum (Native Segwit).

![image](assets/50.png)

Le chiavi private e pubbliche estese sono appena sotto e cambiano quando apporti modifiche al percorso di derivazione (o qualsiasi altra cosa più in alto nella pagina).

![image](assets/51.png)

Vedrai anche le chiavi private/pubbliche estese BIP32: per ora, ignorale.

La chiave privata estesa dell'account può essere utilizzata per rigenerare completamente il tuo portafoglio. La chiave pubblica estesa dell'account, tuttavia, può solo produrre una versione limitata dello stesso portafoglio (portafoglio di osservazione): se inserisci questa chiave in Electrum, produrrà comunque tutti gli 8,6 miliardi di indirizzi che avrebbe il seme o la chiave privata estesa, ma Electrum non avrà a disposizione chiavi private, quindi non sarà possibile effettuare transazioni. Facciamolo ora per dimostrare il punto:

Copia la "chiave pubblica estesa dell'account" negli appunti.

Quindi vai su Electrum, lascia aperto il portafoglio che abbiamo creato in precedenza e vai su file->nuovo/ripristina. Il processo per creare il portafoglio è leggermente diverso rispetto a prima:

- Portafoglio standard
- Utilizza una chiave principale
- Incolla la chiave pubblica estesa nella casella e procedi
- Non è necessario inserire una frase segreta; fa già parte della chiave pubblica estesa
- Non è necessario inserire la semantica dello script e il percorso di derivazione
- Non è necessario aggiungere una password (blocca il portafoglio)
  Quando il portafoglio si carica, dovresti notare che vengono caricati esattamente gli stessi indirizzi di prima quando è stato inserito il seed. Dovresti anche notare in alto nella barra del titolo che dice "watching wallet". Questo portafoglio può mostrarti i tuoi indirizzi e i tuoi saldi (controllando i saldi tramite un nodo), ma non sei in grado di FIRMARE transazioni (perché il portafoglio di osservazione non ha chiavi private).
  Allora qual è il punto?

Una ragione, e non la principale, è che potenzialmente puoi osservare il tuo portafoglio e il suo saldo su un computer senza esporre le tue chiavi private a malware sul computer.

Un'altra ragione è che è RICHIESTO per effettuare pagamenti se scegli di tenere le tue chiavi private fuori dal computer; spiegherò:

> I portafogli hardware (HWW) sono stati creati in modo che un dispositivo possa conservare le tue chiavi private in modo sicuro (bloccate con un PIN), non esporre mai le chiavi a un computer (anche quando collegato a un computer tramite un cavo) e non essere in grado di connettersi a Internet. Un dispositivo del genere non può effettuare transazioni da solo perché tutte le transazioni Bitcoin iniziano facendo riferimento a un UTXO (o più UTXO) sulla blockchain (che si trova su un nodo). Un portafoglio deve specificare l'ID della transazione in cui si trova l'UTXO e quale output della transazione deve essere speso. Solo dopo aver specificato l'input può essere creata una nuova transazione in primo luogo, figuriamoci firmarla. I portafogli hardware non possono creare transazioni perché non hanno accesso a nessun UTXO: non sono collegati a nulla! Di solito viene estratta una chiave pubblica estesa dall'HWW e gli indirizzi vengono quindi visualizzati su un computer: molte persone saranno familiari con il software Ledger o Trezor Suite che mostra indirizzi e saldi sul loro computer - questo è un portafoglio di osservazione. Questi programmi possono creare transazioni, ma non possono firmarle. Possono solo far firmare le transazioni da HWW che sono collegati a loro. L'HWW prende la transazione appena generata dal portafoglio di osservazione, la firma e poi la invia di nuovo al computer per la trasmissione a un nodo. L'HWW non può trasmettere da solo, lo fa il portafoglio di osservazione associato. In questo modo, i due portafogli (portafoglio con chiave pubblica sul computer e portafoglio con chiave privata nell'HWW) collaborano per generare, firmare e trasmettere, assicurandosi che le chiavi private rimangano isolate e lontane da un dispositivo connesso a Internet.

## Transazioni Bitcoin parzialmente firmate (PSBT)

È possibile creare una transazione e salvarla su un file, successivamente ricaricarla, firmarla, salvarla, ricaricarla e infine trasmetterla - non sto dicendo che qualcuno debba farlo; è solo qualcosa che è possibile.

Ora considera un portafoglio multisignature 3 su 5: 5 chiavi private creano un portafoglio e ne servono 3 per firmare completamente una transazione (vedi qui per saperne di più sulle chiavi dei portafogli multisignature). È possibile avere 5 diversi computer, ognuno con una delle cinque chiavi private.

Il computer uno potrebbe generare una transazione e firmarla. Potrebbe quindi salvarla su un file e inviarla via email al computer due. Il computer due può quindi firmarla e potenzialmente salvare il file in un codice QR e trasmettere il QR tramite una chiamata Zoom al computer tre dall'altra parte del mondo. Il computer tre può catturare il QR, caricare la transazione in Electrum e firmare la transazione. Dopo le prime 2 firme, la transazione era una PSBT (transazione Bitcoin parzialmente firmata). Dopo la terza firma, la transazione diventa completamente firmata e valida, pronta per la trasmissione.
Per saperne di più su PSBTS, consulta questa guida. (https://armantheparman.com/psbt/)

## Utilizzare portafogli hardware con Electrum

Ho una guida sull'utilizzo dei portafogli hardware in generale, che penso sia importante per le persone che sono nuove ai portafogli hardware, da leggere. (https://armantheparman.com/using-hwws/)

Ci sono anche guide su varie marche di portafogli hardware che si collegano a Sparrow Bitcoin Wallet, che puoi trovare qui. (https://armantheparman.com/hwws/)

Questa sarà la mia prima guida su come utilizzare un portafoglio hardware con Electrum - userò il portafoglio hardware ColdCard come esempio. Questo non è un manuale dettagliato sul ColdCard specificamente, quella guida si trova qui. Sto solo mostrando punti specifici di Electrum. (https://armantheparman.com/cc/)

### Connessione tramite scheda micro SD (air-gapped)

Prima di connettere il tuo vero portafoglio tramite ColdCard, spero tu abbia seguito i passaggi precedenti per caricare un portafoglio fittizio di Electrum e impostare i parametri di rete.

Quindi, sul ColdCard, inserisci la scheda SD. Sto assumendo che tu abbia già creato il tuo seed. Se stai accedendo al portafoglio con una passphrase, applicala ora. Scorri verso il basso e seleziona il menu Avanzate/Strumenti -> Esporta Portafoglio -> Portafoglio Electrum.

Puoi scorrere verso il basso e leggere il messaggio. Ti offre sempre di selezionare "1" per inserire un numero di conto diverso da zero (parte del percorso di derivazione), ma se hai seguito il mio consiglio, non hai modificato i percorsi di derivazione predefiniti, quindi non vorrai un numero di conto diverso da zero; premi semplicemente il segno di spunta per continuare.

Quindi seleziona la semantica dello script. La maggior parte delle persone selezionerà "Native Segwit".

Dirà "File del portafoglio Electrum scritto" e visualizzerà il nome del file. Fai un appunto mentale.

Quindi togli la scheda micro SD e inseriscila nel computer con Electrum.

Alcuni sistemi operativi apriranno automaticamente l'esplora file quando inserisci la microSD. Molte persone vedranno il nuovo file del portafoglio e lo apriranno facendo doppio clic su di esso, e si chiederanno perché non funziona. Non è un ottimo design. In realtà, devi ignorare l'esplora file (chiudilo) e aprire il file del portafoglio utilizzando Electrum:

Apri Electrum. Se è già aperto con un altro portafoglio, seleziona file -> nuovo. Stiamo cercando questa finestra:

![image](assets/52.png)

Ecco il trucco, non è intuitivo. Fai clic su "scegli". Quindi naviga nel sistema di file sulla scheda microSD e trova il file del portafoglio e aprilo.

Ora hai aperto il portafoglio di osservazione corrispondente al tuo portafoglio hardware. Ottimo.

### Connessione tramite cavo USB.

Questo modo dovrebbe essere più facile, ma per i computer Linux è molto più difficile. È necessario aggiornare qualcosa chiamata "Regole Udev". Ecco come (guida dettagliata https://armantheparman.com/gpg-articles/ ), e brevemente:

È una buona idea assicurarsi che il sistema sia aggiornato. Quindi:

```
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

poi...

```
python3 -m pip install ckcc-protocol
```

Se si verifica un errore, assicurati che pip sia installato. Puoi verificare con (pip --version), e puoi installarlo con (sudo apt install pythron3-pip)

Crea o modifica, se esiste già, il file /etc/udev/rules.d/

Come questo:

```
sudo nano /etc/udev/rules.d
```

Un editor di testo si aprirà. Copia il testo da qui e incollalo nel file rules.d, salva ed esci.
![image](assets/53.png)

Quindi esegui questi comandi uno dopo l'altro:

```
sudo groupadd plugdev

sudo usermod -aG plugdev $(whoami)

sudo udevadm control –reload-rules && sudo udevadm trigger
```

Se ricevi un messaggio "group plugdev" già esistente, va bene, procedi. Dopo il secondo comando, non riceverai alcun feedback o risposta, procedi semplicemente al terzo comando.

Potrebbe essere necessario scollegare e ricollegare il ColdCard al computer.

Se non riesci ancora a connettere il ColdCard nonostante tutto ciò, ti consiglierei di provare ad aggiornare il firmware (guida disponibile a breve, ma per ora puoi trovare istruzioni sul sito del produttore).

Successivamente, crea un nuovo portafoglio:

- Portafoglio standard
- Utilizza un dispositivo hardware
- Verrà eseguita una scansione per rilevare il tuo ColdCard. Procedi.
- Seleziona la semantica dello script e il percorso di derivazione
- Decidi se il file del portafoglio deve essere crittografato (consigliato)

### Transazioni utilizzando il ColdCard

Con il cavo collegato, le transazioni sono facili. La firma delle transazioni sarà senza soluzione di continuità.

Se utilizzi il dispositivo in modo isolato, dovrai passare manualmente la transazione salvata tra i dispositivi utilizzando la scheda microSD. Ci sono alcuni trucchi.

Dopo aver creato una transazione e finalizzata, devi fare clic sul pulsante di esportazione nell'angolo in basso a sinistra. Vedrai "salva su file" che, in modo controintuitivo, non è ciò che vogliamo. In realtà, devi prima andare all'ultima opzione di menu che dice "per portafogli hardware" e quindi, all'interno di quella selezione, trovare l'altro "salva su file" e selezionarlo. Quindi salva il file sulla microSD, togli la scheda e inseriscila nel ColdCard. Ricorda che potresti dover applicare una passphrase per selezionare il portafoglio corretto. Lo schermo indicherà "pronto per la firma". Fai clic sul segno di spunta, controlla la transazione e procedi confermando con il segno di spunta. Una volta fatto, togli la scheda e reinseriscila nel computer.

Quindi dobbiamo aprire la transazione utilizzando Electrum. La funzione è nascosta nel menu Strumenti -> Carica transazione. Naviga nel file system e trova il file. Ogni volta che firmi, ci saranno tre file. Il file originale salvato che ha creato il portafoglio di osservazione e due file creati dal ColdCard (non so perché lo faccia). Uno dirà "firmato" e uno dirà "finale". Non è intuitivo, ma quello "firmato" non è utile, dobbiamo aprire la transazione "finale".

Una volta caricata quella, puoi fare clic su "trasmetti" e il pagamento verrà effettuato.

## Aggiornamento di Electrum e della directory nascosta ".electrum"

Electrum risiede sul tuo computer in due posizioni. C'è l'applicazione stessa e c'è una cartella di configurazione nascosta. Questa cartella si trova in posizioni diverse a seconda del sistema operativo:

Windows:

> C:/Users/il_tuo_nome_utente/AppData/Roaming/Electrum

Mac:

> /Users/il_tuo_nome_utente/.electrum

Linux:

> /home/il_tuo_nome_utente/.electrum

Nota il "." prima di "electrum" in Linux e Mac: indica che la cartella è nascosta. Inoltre, nota che questa directory viene creata (automaticamente) solo dopo aver eseguito Electrum per la prima volta. La directory contiene il file di configurazione di Electrum e anche la directory che contiene eventuali portafogli salvati.
Se elimini il programma Electrum dal tuo computer, la cartella nascosta rimarrà, a meno che tu non la elimini attivamente anche tu.
Per aggiornare Electrum, segui la stessa procedura che ho descritto all'inizio per scaricare e verificare. Avrai quindi due copie del programma sul tuo computer e potrai eseguire entrambe: ogni programma accederà alla stessa cartella nascosta di Electrum per la sua configurazione e l'accesso al portafoglio. Tutto ciò che abbiamo salvato, come l'unità di base, il nodo predefinito a cui connettersi, altre preferenze e l'accesso ai portafogli, rimarrà perché tutto ciò è salvato in quella cartella.

### Spostare Electrum e i portafogli su un altro computer

Per fare ciò, puoi copiare i file del programma su una chiavetta USB e copiare anche la cartella .electrum. Quindi copiali o spostali sul nuovo computer. Non è necessario verificare nuovamente il programma. Assicurati di copiare la cartella .electrum nella posizione predefinita (ricorda di copiarla PRIMA di eseguire Electrum per la prima volta su quel computer, altrimenti verrà creata una cartella .electrum predefinita vuota e potresti confonderti).

## Etichette

Come ho spiegato in precedenza, nella scheda degli indirizzi c'è una colonna delle etichette. Puoi fare doppio clic lì e inserire note per te stesso (sono solo sul tuo computer, non pubbliche e non sulla blockchain).

![image](assets/54.png)

Quando sposti il tuo portafoglio Electrum su un altro computer, potresti voler conservare tutte queste note. Puoi eseguire il backup su un file utilizzando il menu, portafoglio -> etichette -> esporta, e quindi sul nuovo computer utilizzare portafoglio -> etichette -> importa.

## Suggerimenti:

Se trovi utile questa risorsa e desideri supportare ciò che faccio per Bitcoin, puoi donare alcuni satoshi qui:

Indirizzo Lightning statico: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/

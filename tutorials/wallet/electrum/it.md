---
name: Electrum

description: Guida completa a Electrum, da zero a cento
---

![cover](assets/cover.webp)

Descrizione di Electrum

https://twitter.com/ElectrumWallet
https://electrum.org/
https://electrum.readthedocs.io/

> "Devo dire che quando ho trovato questo tutorial sono rimasto scioccato. Congratulazioni ad Arman the Parman. Sarebbe stato un peccato non pubblicare qui il tutorial e tradurlo in quante più lingue possibili. Quel ragazzo è un grande." - Rogzy

![Portafoglio desktop Electrum (Mac / Linux) - download, verifica, connessione al tuo nodo.](https://youtu.be/wHmQNcRWdHM)

![Effettuare una transazione Bitcoin con Electrum](https://youtu.be/-d_Zd7VcAfQ)

## Perché Electrum?

Questa è una guida dettagliata su come utilizzare Electrum, con soluzioni per scovare tutte le sue insidie e particolarità. Ho raggiunto questo livello di conoscenza dopo diversi anni di utilizzo e insegnamento agli studenti rigurdo a temi di sicurezza/privacy su Bitcoin. Electrum non è il miglior wallet Bitcoin per chi vuole mantenere tutto il più semplice possibile e preferisce rimanere a livello principiante. Al contrario, è rivolto agli utenti esperti, o chi aspira ad esserlo.

Per un utilizzatore principiante di Bitcoin, diventa eccellente solo se sotto la supervisione di un utente esperto che gli mostri la strada. Se si impara ad usarlo da soli, all'inizio sarebbe meglio prendersi il proprio tempo e utilizzarlo in un ambiente di test inviando pochi satoshi. Questa guida ti aiuta a imparare come usare questo strumento, ma è anche un buon punto di riferimento per chiunque altro.

> Avviso: questo tutorial è alquanto lungo, per cui non cercare di replicare tutti i passaggi in un solo giorno. È meglio salvare la guida e procedere gradualmente.

## Scaricare Electrum

L'ideale è utilizzare un computer dedicato a Bitcoin per le proprie transazioni (la mia guida a riguardo è qui: https://armantheparman.com/mint/) _(DISPONIBILE anche nella sezione sulla privacy)_. Va bene esercitarsi con pochi satoshi su un computer "sporco" quando si sta imparando (chissà quanti malware nascosti il tuo computer ha accumulato nel corso degli anni - non vuoi esporre i tuoi wallet ad questi software malevoli).

Scarica Electrum da https://electrum.org/.

Clicca sulla scheda 'Download' in alto.

Clicca sul link di download corrispondente al tuo sistema operativo. Qualsiasi computer Linux o Mac può utilizzare il link Python (pallino rosso). Un computer Linux con un chip Intel o AMD può utilizzare l'Appimage (pallino verde; è simile a un file eseguibile di Windows). Un dispositivo Raspberry Pi ha un microprocessore ARM e può utilizzare solo la versione Python (pallino rosso), non l'Appimage, anche se i Pi eseguono Linux. Il pallino blu è il link per Windows, e il pallino nero è quello per Mac.

![image](assets/1.webp)

## Verifica di Electrum

Lo scopo della "verifica" del download è assicurarsi che nemmeno un singolo bit di dati sia stato manomesso. Ciò impedisce di utilizzare una versione "hackerata" e dannosa del software. Puoi saltare questa fase solo se utilizzi una versione scaricata solo per esercitarti, ovvero senza transare fondi reali tramite il wallet. Al contrario, una volta che sei pronto a utilizzare Electrum con fondi veri, dovrai eliminare questa versione e ricominciare, questa volta verificando il download di Electrum.

Per farlo, utilizziamo strumenti di crittografia a chiave pubblica/privata - gpg, su cui abbiamo scritto una guida qui (https://armantheparman.com/gpg/). Lo strumento gpg è inserito in tutti i sistemi operativi Linux. Per Mac e Windows, consulta il link gpg di cui sopra per le istruzioni di download.
Oltre a scaricare Electrum è necessario ottenere anche la FIRMA digitale del software per motivi di sicurezza. Si tratta di una stringa di testo (in realtà un numero codificato usando il formato del testo) che lo sviluppatore ha prodotto con la sua chiave gpg PRIVATA. Utilizzando il programma gpg, possiamo quindi "verificare" la FIRMA confrontandola con la sua chiave PUBBLICA (creata a partire dalla chiave privata dello sviluppatore), rispetto al FILE di download. È bene sapere che chiunque ha accesso alla chiave pubblica in questione.

In altre parole, con i tre input (firma, chiave pubblica e file del software), otteniamo un output (vero o falso) per confermare che il file non sia stato manomesso.

Per ottenere la firma, clicca sul link corrispondente al file scaricato (vedi frecce colorate):

![image](assets/2.webp)

Cliccando sul link si potrebbe scaricare automaticamente il file nella cartella download, oppure potrebbe aprirsi nel browser. In questo secondo caso, è necessario salvare il file. Clicca con il tasto destro del mouse e seleziona "Save as" (Salva con nome). A seconda del sistema operativo o del browser, potrebbe essere necessario cliccare con il tasto destro sullo spazio bianco, non sul testo.

Nell'immagine di seguito è riportato il testo scaricato. Puoi vedere che ci sono più firme, che sono di persone diverse. Sappi che puoi verificare ognuna di esse, anche se in questo tutorial ti mostrerò come verificare solo quella dello sviluppatore.

![image](assets/3.webp)

Successivamente, è necessario scaricare la chiave pubblica di ThomasV, che è il principale sviluppatore. Puoi prenderla direttamente da lui, dal suo account Keybase, da Github o da qualcun altro, da un keyserver o dal sito web di Electrum.

In realtà, scaricarla dal sito web di Electrum è il modo meno sicuro, perché se il sito è stato hackerato (proprio ciò che stiamo verificando), per quale motivo dovremmo ottenere una chiave pubblica da lì (la chiave pubblica potrebbe essere falsa)?

Semplificando, ti mostrerò come ottenere la chiave pubblica di ThomasV dal sito web di Electrum. Tuttavia, ricorda quello che ho scritto sopra. Ecco la copia (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc) su GitHub con cui puoi confrontarla.

Scorri un po' verso il basso nella pagina per trovare il link alla chiave pubblica di ThomasV (pallino rosso nell'immagine sotto). Cliccaci su e scaricalo. Se si apre come testo sul browser, clicca con il tasto destro del mouse per salvarlo.

![image](assets/4.webp)

Ora hai 3 nuovi file, probabilmente tutti nella cartella dei download. Non importa dove si trovino, ma metterli tutti nella stessa cartella rende il processo più semplice.

I tre file:

1. Il download di Electrum
2. La firma (di solito ha lo stesso nome del download di Electrum con l'aggiunta di ".asc")
3. La chiave pubblica di ThomasV.

Apri un terminale su Mac o Linux, o il prompt dei comandi (CMD) su Windows.

Vai alla directory dei download (o ovunque tu abbia messo i tre file). Se non hai idea di cosa significhi, puoi guardare questo breve video per Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) e questo per Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Ricorda che i nomi delle directory sono sensibili alle maiuscole sui computer Linux.
Apri un terminale e digita il comando di seguito per importare la chiave pubblica di ThomasV nel "portachiavi" del tuo computer (sto usando "portachiavi" come concetto astratto - in realtà è solo un file sul tuo computer):

```
gpg --import ThomasV.asc
```

Assicurati che il nome del file corrisponda a quello che hai scaricato. Inoltre, ti faccio notare che ci sono due trattini, non uno solo. Fai anche attenzione a inserire uno spazio prima e dopo "--import". Poi premi <enter> (invio).

Il file dovrebbe essere importato. Se ti viene mostrato un messaggio di errore, controlla di essere nella directory in cui il file si trova effettivamente. Per verificare in quale directory ti trovi (su Mac o Linux), digita `pwd`. Per vedere quali file sono nella directory in cui ti trovi (su Mac o Linux), digita `ls`. Dovresti vedere elencato il file di testo "ThomasV.asc", insieme ad altri file.

Poi esegui il comando per verificare la firma.

```
gpg –verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Nota che ci sono 4 "elementi" qui, separati da uno spazio:

1. il programma gpg
2. l'opzione --verify
3. il nome del file della firma
4. il nome del programma

A volte puoi omettere il quarto elemento e il computer capisce lo stesso cosa intendi. Non sono sicuro, ma credo che funzioni solo se i nomi dei file differiscono solo per "asc" alla fine.

Non copiare semplicemente i nomi dei file che ho mostrato qui - assicurati che corrispondano al nome del file che hai sul tuo sistema.

Premi <enter> (invio) per eseguire il comando. Ti dovrebbe apparire il messaggio "buona firma da ThomasV" per indicare che il processo di verifica è andato a buon fine. Ci saranno alcuni errori perché non abbiamo le chiavi pubbliche per le firme delle altre persone. Queste chiavi sono contenute nel file di firma (questo sistema di combinare le firme in un unico file potrebbe cambiare nelle versioni successive). Inoltre, c'è un avviso in fondo che possiamo ignorare (questo ci avvisa che non abbiamo esplicitamente detto al sistema di fidarci della chiave pubblica di ThomasV).

Ora abbiamo una copia verificata di Electrum sicura da usare.

## Esecuzione di Electrum

### Esecuzione di Electrum se si utilizza Python

Se hai scaricato la versione di Python, ecco come farla funzionare. Vedrai questo sulla pagina di download:

![image](assets/5.webp)

Per Linux, è una buona idea prima aggiornare il sistema:

```
sudo apt-get update
sudo apt-get upgrade
```

Copia il testo giallo evidenziato, incollalo nel terminale e premi <enter> (invio). Ti verrà chiesta la password, eventualmente una conferma per continuare, e poi verranno installati dei file conosciuti come "dipendenze" su Linux.

Dovrai anche estrarre il file zip in una directory a tua scelta. Puoi farlo tramite l'interfaccia grafica o dalla riga di comando (comando evidenziato in rosa) - ricorda che i nomi dei tuoi file potrebbero essere diversi (quando abbiamo verificato il download nella sezione precedente, abbiamo verificato il file zip, non la directory estratta).

C'è un'opzione per "installare" usando il programma PIP, ma ciò è superfluo e aggiunge passaggi extra, come l'installazione di altri file. Esegui semplicemente il programma utilizzando il terminale per evitare tutto ciò.

I passaggi (su Linux) sono:

1. vai alla directory in cui sono estratti i file
2. digita: ./run_electrum

I passaggi sono gli stessi su Mac, ma potrebbe essere necessario installare prima Python3 e utilizzare questo comando per eseguire il programma:

````
```python3 ./run_electrum```
````

Una volta che Electrum è in esecuzione, la finestra del terminale rimarrà aperta. Se la chiudi, terminerà Electrum. Riducila al minimo mentre usi il programma.

### Esecuzione di Electrum con l'Appimage

Questo metodo è un po' più semplice, ma non così facile come usare un file eseguibile su Windows. A seconda della versione di Linux che stai utilizzando, i file Appimage potrebbero avere attributi impostati in modo che l'esecuzione sia vietata dal sistema di default. Dobbiamo cambiare questa cosa. Se il tuo Appimage funziona, puoi saltare questo passaggio. Altrimenti, vai alla directory dove si trova il file, utilizzando il terminale, quindi esegui questo comando:

```
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

"sudo" fornisce privilegi di superutente; "chmod" è un comando per cambiare la modalità di accesso al file, modificando chi può leggere, scrivere o eseguire lo stesso; "ug+x" significa che stiamo consentendo all'utente e al gruppo di attivare il programma.

Modifica il nome del file in modo che corrisponda alla tua versione.

A questo punto, Electrum verrà eseguito facendo doppio clic sull'icona dell'Appimage.

### Esecuzione di Electrum con Mac

Basta fare doppio clic sul file scaricato (è un "drive"). Si aprirà una finestra. Trascina l'icona di Electrum nella finestra sul desktop, o ovunque tu voglia conservare il programma. Puoi quindi "espellere" il drive e cancellarlo (si tratta del file scaricato).

Per eseguire il programma, basta fare doppio clic su di esso. Potresti ricevere alcuni errori "nanny" specifici di Mac che devono essere bypassati.

### Esecuzione di Electrum con Windows

Nonostante il fatto che odio Windows più di tutto, questo è il metodo più semplice. Basta fare doppio clic sul file eseguibile per avviarlo.

## Inizia con un wallet fittizio

Quando carichi per la prima volta Electrum, si aprirà una finestra come questa:

![image](assets/6.webp)

In futuro, selezionerai manualmente il tuo server, ma, per ora, lascia le impostazioni predefinite e la connessione automatica.

Successivamente, crea un wallet fittizio: non mettere mai fondi reali in questo wallet. Lo scopo di questo wallet fittizio è quello di imparare ad usare il software e assicurarsi che tutto funzioni correttamente prima di caricare il tuo vero wallet. Stiamo cercando di evitare che venga accidentalmente violata la privacy del wallet reale. Se stai solo facendo pratica, il wallet che crei può essere considerato comunque un wallet fittizio.

Puoi lasciare il nome "default_wallet" o cambiarlo a tuo piacimento, e quindi cliccare su 'Next' (Avanti). In seguito, se creerai più wallet, puoi trovarli e aprirli in questa fase cliccando prima su "Choose..." (Scegli...)

![image](assets/7.webp)

Scegli "Standard wallet" e <Next> (Avanti):

![image](assets/8.webp)

Quindi, seleziona "I already have a seed" (Possiedo già un seed). Non voglio che tu prenda l'abitudine di creare la seedphrase con Electrum, poiché utilizza il proprio protocollo che non è compatibile con altri wallet: ecco perché non clicchiamo su "new seed" (nuovo seed).

![image](assets/9.webp)

Vai su https://iancoleman.io/bip39/ e crea una seedphrase di test. Prima di tutto, cambia il numero di parole a 12 (che è la versione di seedphrase più utilizzata), quindi clicca su "generate" e copia le parole nella casella negli appunti.

![image](assets/10.webp)

Quindi incolla le parole in Electrum. Ecco un esempio:

![image](assets/11.webp)

Electrum cercherà parole che corrispondano al suo protocollo. Dobbiamo ignorare questo passaggio; clicca su "options" (opzioni) e seleziona seedphrase BIP39:

![image](assets/12.webp)

la seedphrase diventa quindi valida (prima di inserirla, Electrum si aspettava una seedphrase di Electrum, per questo la seedphrase che abbiamo inserito era considerata non valida). Prima di cliccare su "next" (avanti), nota il messaggio che dice "Checksum OK". È importante (per il wallet reale che potresti utilizzare in seguito) prestare attenzione a questo aspetto prima di procedere, poiché conferma la validità della seedphrase inserita. L'avvertimento in fondo può essere ignorato. Si tratta soltanto della lamentela dello sviluppatore di Electrum riguardo a BIP39 e alle loro affermazioni "FUD" (Fear, Uncertainty, and Doubt = Paura, Incertezza e Dubbio) che asseriscono che la loro versione (non compatibile con altri wallet) sia superiore.

**Piccolo approfondimento importante.** Lo scopo del [checksum](https://planb.network/resources/glossary/checksum) è assicurarsi di aver inserito la seedphrase senza errori di battitura. Il checksum è la parte finale della seedphrase (la 12ª parola diventa il checksum) che viene determinata matematicamente a partire dalla prima parte della seedphrase (le 11 parole). Se si dovesse digitare qualcosa di sbagliato all'inizio, la parola di checksum non corrisponderà matematicamente, e il software del wallet ti mostrerà con un avvertimento. Ciò non significa che la seedphrase non possa essere utilizzata per creare un wallet Bitcoin funzionante. Immagina di creare un wallet facendo un errore di battitura e inviarci dei bitcoin. Un giorno potresti aver bisogno di ripristinare il wallet, ma quando lo fai, non ricreerai l'errore di battitura: ripristinerai il wallet sbagliato! 

È piuttosto pericoloso che Electrum ti permetta di procedere con la creazione di un wallet se il checksum non è valido, quindi fai attenzione: è tua responsabilità assicurarti che il Checksum si corretto. Altri wallet non ti permetteranno di procedere, il che è molto più sicuro. Questo è uno dei motivi per cui dico che Electrum è sicuro da usare, una volta che impari ad usarlo correttamente (gli sviluppatori di Electrum dovrebbero risolvere questo problema).

Nota che se desideri aggiungere una passphrase, la possibilità di selezionarla si trova in alto nel menù opzioni.

Dopo aver cliccato su OK, verrai riportato alla schermata in cui hai digitato la seedphrase. Se hai selezionato l'opzione passphrase, questa NON la inserisci insieme alla seedphrase ma in seguito.

Se non hai richiesto la [passphrase](https://planb.network/resources/glossary/passphrase-bip39), vedrai questa schermata successiva contenente ulteriori opzioni per il tipo di script e il derivation path del tuo wallet. Trovi maggiori approfondimenti qui (https://armantheparman.com/public-and-private-keys/). Ad ogni modo, puoi lasciare semplicemente i valori predefiniti e procedere.

![image](assets/13.webp)

Ulteriori informazioni sulla schermata che vedi sopra: la prima opzione ti consente di scegliere tra legacy (indirizzi che iniziano con "1"), pay-to-script-hash (indirizzi che iniziano con "3") o bech32/native segwit (indirizzi che iniziano con "bc1q"). Al momento della stesura di questo tutorial, Electrum non supporta ancora taproot (indirizzi che iniziano con "bc1p"). 
La seconda opzione ti consente di modificare il [derivation path](https://planb.network/resources/glossary/derivation-path). Ti consiglio di non modificarlo mai, soprattutto se non sai cosa stai facendo. Molti affermano l'importanza di scrivere il derivation path in modo da poter recuperare il tuo wallet se necessario. Ma se lo lasci come predefinito, probabilmente andrà tutto bene, quindi non preoccuparti. Ad ogni modo, è consigliato appuntarsi il derivation path.

Successivamente, ti verrà data la possibilità di aggiungere una "PASSWORD". Questa non deve essere confusa con la "PASSPHRASE". 
- Una password blocca il file sul tuo computer. 
- Una passphrase fa parte della chiave privata.
Poiché si tratta di un wallet fittizio, puoi lasciare la password vuota e procedere.

![image](assets/14.webp)

Ti verrà mostrata una finestra pop-up per ricevere le notifiche riguardo alle nuove versioni (ti consiglio di selezionare no). Il wallet si genererà quindi da solo e sarà pronto all'uso (ma ricorda, questo wallet è destinato ad essere eliminato, è solo un wallet fittizio).

![image](assets/15.webp)

Ci sono alcuni setting che ti consiglio di fare per configurare al meglio Electrum (da fare solo una volta):

### Cambia le unità in BTC

Vai al menù in alto, tool (strumenti) -> electrum preferences (preferenze di Electrum), e lì nella scheda general (generale), troverai l'opzione per cambiare la "base unit" (l'unità di base) in BTC.
Abilita la scheda "Addresses and Coins" (Indirizzi e Monete).

Vai al menù "View" (Visualizza), in alto, e seleziona "show addresses" (mostra indirizzi). Poi torna su "View" (Visualizza) e seleziona "show coins" (mostra monete).

### Abilita Oneserver

Di default, Electrum si connette a un nodo casuale, e si connette anche a molti altri nodi secondari. Non sono sicuro di quali dati vengano scambiati con questi nodi secondari, ma, per tutelare la nostra privacy, non vogliamo che questo accada. Anche se inserisci le informazioni di un nodo, ad esempio il tuo nodo personale, molti altri nodi saranno comunque connessi, e non sono sicuro di quali informazioni vengano condivise. Tuttavia, è facile prevenirlo. Prima di mostrarti come inserire le informationi del tuo nodo, forzeremo Electrum a connettersi solo ad un server alla volta.

Puoi farlo specificando "oneserver" dalla riga di comando, ma non raccomando questa modalità. Mostrerò un'alternativa che ritengo più semplice a lungo termine e con meno probabilità di farti connettere accidentalmente ad altri nodi.

Il motivo per cui stiamo usando un wallet fittizio è che se avessimo caricato il nostro vero wallet, con i nostri veri bitcoin, avremmo già involontariamente stabilito una connessione con un nodo casuale. Questo accade anche se all'inizio abbiamo selezionato "set server manually" (imposta server manualmente) (ehi sviluppatori di Electrum, dovreste risolvere questo problema). Se il nostro wallet fosse privato, sarebbe un disastro.

Inoltre, non possiamo eseguire i passaggi che ti mostrerò di seguito senza prima caricare un qualche tipo di wallet (stiamo per modificare un file di configurazione che viene riempito con i dati e si può modificare solo una volta caricato un wallet).

**Chiudi Electrum (IMPORTANTE: se non lo fai, le modifiche che apporterai verranno cancellate).**

### File di configurazione LINUX/MAC

Apri un terminale su Linux o Mac (istruzioni per Windows in seguito).

Dovresti trovarti automaticamente nella cartella home. Da quì, vai alla cartella delle impostazioni nascoste di Electrum (che può cambiare a seconda di dove sia stato salvato Electrum nel tuo computer).

```
cd `.electrum`
```

Nota il punto prima di "electrum" che indica che si tratta di una cartella nascosta.

Un altro modo per arrivarci è digitare:

```
cd ~/`.electrum`
```

dove "~" rappresenta il percorso della tua cartella home. Puoi vedere il percorso completo della tua directory corrente con il comando `pwd`.

Una volta nella directory "`.electrum`", digita "nano config" e premi <invio>.

Si aprirà un editor di testo (chiamato nano) con il file di configurazione aperto. Il mouse non funziona qui. Devi usare i tasti con le freccie per arrivare alla riga che dice:

```
"oneserver": false,
```

Cambia "false" in "true"; e non modificare la sintassi (non eliminare la virgola o il punto e virgola).

Premi <ctrl> "x", per uscire, poi "y" per salvare, poi <invio> per confermare la modifica senza modificare il nome del file.
Ora esegui di nuovo Electrum. Quindi clicca sul pallino in basso a destra per aprire le impostazioni di rete. Poi, nella scheda in alto, vedrai "connected to 1 node" (connesso a 1 nodo) - questo indica che tutto è andato a buon fine.
Sotto, vedrai un campo di testo: l'indirizzo del server è lì. Attualmente sei connesso a quel nodo scelto casualmente dal software. Trovi maggiori informazioni sulla connessione ad un nodo nella prossima sezione.

### File di configurazione di Windows

Il file di configurazione Windows è un po' più difficile da trovare. La directory è:

```
C:/Users/Parman/AppData/Roaming/Electrum
```

Ovviamente, devi cambiare "Parman" con il nome utente del tuo computer.

In quella cartella troverai il file di configurazione. Aprilo con un editor di testo e modifica la riga:

```
"oneserver": false,
```

Cambia "false" in "true"; non modificare la sintassi (non eliminare la virgola o il punto e virgola).

Salva quindi il file, ed esci.

## Connetti Electrum a un nodo

Successivamente, è bene connettere il nostro wallet fittizio a un nodo a nostra scelta. Se non sei pronto per creare un nodo personale, puoi fare una delle seguenti cose:

1. Connetterti al nodo di un amico (richiede Tor)
2. Connetterti al nodo di un'azienda affidabile
3. Connetterti ad un nodo scelto in maniera casuale (non consigliato).

A proposito, trovi tutte le istruzioni per lanciare il tuo nodo personale e le ragioni per cui dovresti farlo nei nostri tutorial nella sezione "Nodo", o nei nostri corsi gratuiti.

### Connettiti al nodo di un amico tramite Tor (Guida in arrivo)

### Connettiti a un nodo di un'azienda affidabile

L'unico motivo per connettersi al nodo di un'azienda sarebbe quello di accedere alla blockchain quando non hai a disposizione il tuo nodo (o quello di un amico).

Connettiamoci al nodo di Bitaroo - ci dicono che non raccolgono dati. Sono un Exchange Bitcoin-only, gestito da un appassionato di Bitcoin. Connettersi al loro nodo richiede un po' di fiducia, ma è meglio che connettersi a un nodo a caso, che potrebbe rivelarsi di una società di sorveglianza.

Accedi alle impostazioni di rete cliccando sul pallino nella parte inferiore destra della finestra di Electrum (il rosso indica "non connesso", il verde indica "connesso", e il blu indica "connesso tramite Tor").

![image](assets/16.webp)

Una volta cliccato sull'icona del pallino, apparirà una finestra popup: il tuo wallet mostrerà "connected to 1 node " (connesso a 1 nodo) poiché l'abbiamo forzato in precedenza.

Deseleziona la casella "select server automatically" (seleziona server automaticamente) e quindi nel campo Server, digita i dettagli di Bitaroo come mostrato:

![image](assets/17.webp)

Chiudi la finestra: ora dovremmo essere connessi al nodo di Bitaroo. Per confermare, il pallino dovrebbe essere verde. Cliccaci di nuovo e controlla che i dettagli del server non siano tornati a un nodo casuale.

### Connetti al tuo nodo

Se hai il tuo nodo è fantastico. Se hai Bitcoin Core, ma non un SERVER Electrum, non sarai ancora in grado di connettere Electrum al tuo nodo.

> **Nota:** Electrum Server e Electrum Wallet sono cose diverse. Il server è un software necessario affinché il wallet Electrum possa comunicare con la blockchain di Bitcoin (non so perché sia stato progettato in questo modo, forse per velocità, ma potrei sbagliarmi).
>
> Se esegui un pacchetto software di un nodo come MyNode (quello che consiglio alle persone di iniziare), Raspiblitz (consigliato quando diventi più esperto) o Umbrel (personalmente non lo consiglio ancora, perché ho riscontrato troppi problemi), allora sarai in grado di connettere Electrum semplicemente inserendo l'indirizzo IP del computer (Raspberry Pi) su cui viene eseguito il nodo, seguito da due punti e da 50002, come mostrato nell'immagine nella sezione precedente (più avanti ti mostrerò come trovare l'indirizzo IP del tuo nodo).

Apri le impostazioni di rete (clicca sul pallino verde o rosso in basso a destra). Deseleziona la casella "select server automatically" (seleziona server automaticamente), quindi inserisci il tuo indirizzo IP come ho fatto io. Il tuo sarà diverso, ma i due punti e "50002" dovrebbero essere gli stessi.

![image](assets/18.webp)

Chiudi la finestra: ora dovresti essere connesso al tuo nodo. Per confermare, clicca nuovamente sul pallino e verifica che i dettagli del server non siano tornati al un nodo casuale.

A volte, nonostante si faccia tutto correttamente, il software si rifiuta di connettersi. In questi casi, ecco alcune cose da provare...

- Aggiorna Electrum e il software che gestisce il tuo nodo
- Prova ad eliminare la cartella della cache nella directory "`.electrum`"
- Prova a cambiare la porta da 50002 a 50001 nelle impostazioni di rete
- Utilizza questa guida per connetterti utilizzando Tor come alternativa: https://armantheparman.com/tor/
- Reinstalla il server Electrum sul tuo nodo

## TROVARE L'INDIRIZZO IP DEL TUO NODO

Un indirizzo IP non è qualcosa che un utente comune sa come cercare e utilizzare. Ho aiutato molte persone a eseguire un nodo e poi a connetterci Electrum. Per fare questo, ho notato che la ricerca dell'indirizzo IP del nodo, a volte, è un ostacolo.

Per MyNode, puoi digitare nella finestra del browser:

```
mynode.local
```

A volte, "mynode.local" non funziona (assicurati di non digitarlo nella barra di ricerca di Google). Per far sì che la barra di navigazione riconosca il tuo testo come un indirizzo e non come una ricerca, inserisci prima http://

così:

```
http://mynode.local
```

se ciò non funziona, prova con una "s", così:

```
https://mynode.local
```

In questo modo accederai al dispositivo e potrai cliccare sul collegamento delle impostazioni (vedi il mio "pallino" blu sotto) per mostrare questa schermata in cui è presente l'indirizzo IP:

![image](assets/19.webp)

Questa pagina si caricherà e vedrai l'IP del nodo (pallino blu).

![image](assets/20.webp)

Quindi, in futuro, puoi digitare 192.168.0.150 o http://192.168.0.150 nel tuo browser.

Per Raspiblitz (quando non è collegato a uno schermo), è necessario usare un metodo diverso (che funziona anche per MyNode):

Accedi alla pagina web del tuo router: qui troveremo l'indirizzo IP di tutti i dispositivi connessi. La pagina web del router sarà un indirizzo IP che inserisci in un browser web. Il mio ha questo aspetto:

```
http://192.168.0.1
```

Per capire quali sono le credenziali di accesso al router, puoi cercarle nel manuale utente o talvolta persino su un adesivo attaccato al router stesso. Cerca il nome utente e la password. Se non riesci a trovarli, prova con Utente: "admin" Password: "password"
Se sei in grado di effettuare l'accesso, vedrai i tuoi dispositivi connessi e dai loro nomi potrebbe essere chiaro quale sia il tuo nodo. Trovato il nodo, troverai anche l'indirizzo IP ad esso associato.

### Se i primi due metodi falliscono, l'ultimo funzionerà, ma è noioso!

Prima di tutto, trova l'indirizzo IP di un qualsiasi dispositivo sulla tua rete (il computer che stai usando va bene).

Su Mac, lo troverai nelle preferenze di Rete:

![image](assets/21.webp)

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

Il numero più piccolo possibile è 2 (0 significa "qualsiasi dispositivo" e 1 appartiene al router) e il più alto, credo sia 255 (questo corrisponde a 11111111 in binario, il numero più grande rappresentabile da 1 byte).

Uno per uno, procedi verso l'alto fino a 255. Alla fine, ti fermerai al numero corretto che carica la tua pagina MyNode (o la pagina RaspiBlitz). Allora saprai quale numero inserire nelle impostazioni di rete di Electrum per connetterti al tuo nodo.

Avrà un aspetto simile a questo (assicurati di includere i due punti e il numero successivo):

![image](assets/22.webp)

È utile sapere che questi indirizzi IP sono INTERNI alla tua rete domestica. Nessuno all'esterno può vederli. Quindi non sono dati sensibili. Puoi considerarli come le estensioni telefoniche di una grande azienda che ti indirizzano a telefoni diversi.

## Elimina il wallet fittizio

Ora ci siamo collegati con successo a un solo nodo: Electrum si caricherà così di default, da ora in poi. Dovresti ora eliminare il wallet fittizio ( Menu: file –> delete. In italiano Menù: file -> elimina), nel caso in cui invii accidentalmente fondi a questo wallet non sicuro (non è sicuro perché non l'abbiamo creato in modo sicuro).

## Crea un wallet di esercitazione

Dopo aver eliminato il wallet fittizio, ricomincia e creane uno nuovo allo stesso modo. Questa volta, annota le parole della seedphrase e tienile al sicuro.

È una buona idea imparare come funziona Electrum con questo wallet di esercitazione, senza la scomodità di usare un hardware wallet (tuttavia necessario per una sicurezza elevata). Metti solo una piccola quantità di bitcoin in questo wallet - facendo finta che perderai questi soldi. Una volta diventato esperto, imparerai ad usare Electrum con un hardware wallet.

Nel nuovo wallet che hai creato, vedrai un elenco di indirizzi. Quelli verdi sono chiamati "indirizzi di ricezione". Sono il prodotto di 3 cose:

- La seedphrase
- La passphrase
- Il derivation path

Il tuo nuovo wallet ha un insieme di indirizzi di ricezione che possono essere creati in modo matematico e riproducibile da qualsiasi software wallet che contenga la seedphrase, la passphrase e il derivation path. Ce ne sono 4,3 miliardi! Più di quanti ne avrai bisogno. Electrum ti mostra solo i primi 20, e poi ne carica di più man mano che li utilizzi.
Ulteriori informazioni sulle chiavi private di Bitcoin possono essere trovate [in questa guida](https://armantheparman.com/public-and-private-keys/).

![image](assets/23.webp)

Electrum è molto diverso da altri wallet che presentano solo un indirizzo alla volta.

Dato che hai inserito la seedphrase durante la creazione di questo wallet, Electrum ha la chiave privata per ciascuno degli indirizzi. Dunque, puoi usare questi indirizzi per fare transazioni.

Nota anche che ci sono indirizzi colorati di giallo, chiamati "indirizzi di resto": si tratta di un altro insieme di indirizzi di un diverso ramo matematico (ne esistono altri 4,3 miliardi). Sono utilizzati da Electrum per inviare automaticamente i fondi in eccesso nel wallet come resto. Ad esempio, se prendi 1,5 bitcoin e ne invii 0,5 a un commerciante, il resto di 1,0 deve andare da qualche parte. Il tuo wallet lo collegherà all'indirizzo di resto giallo successivo (vuoto), altrimenti andrà al miner! Per ulteriori informazioni su questo (UTXOs) consulta questa guida: https://armantheparman.com/utxo/.

Successivamente, torna al sito di Ian Colman per verificare le chiavi private e inserisci la seedphrase (anziché generarne una). Vedrai che le informazioni sulla chiave privata e pubblica cambiano; tutto ciò che segue dipende da come hai svolto la procedura fin ora.

**Ricorda:** non dovresti "mai" inserire la seedphrase di accesso al tuo vero wallet Bitcoin su un computer - un malware può rubarlo. Stiamo solo usando un wallet di esercitazione, per scopi di apprendimento, quindi per ora va bene lo stesso.

Sempre su quel sito, scorri verso il basso e cambia il derivation path in BIP84 (segwit) perchè sia uguale al tuo Electrum, cliccando sulla scheda BIP84.

![image](assets/24.webp)

Sotto, vedrai la chiave privata estesa e la chiave pubblica estesa dell'account:

![image](assets/25.webp)

Vai su Electrum e assicurati che corrispondano. C'è un menù in alto, wallet -> information (portafogli -> informazioni):

![image](assets/26.webp)

Vedrai questo:

![image](assets/27.webp)

Verifica che le due chiavi pubbliche corrispondano.

Successivamente, confronta gli indirizzi. Torna al sito di Ian Coleman e scorri fino in fondo:

![image](assets/28.webp)

Anche qui, verifica che corrispondano agli indirizzi in Electrum.

Ora verificheremo gli indirizzi di resto. Scorri un po' verso l'alto fino al derivation path e cambia l'ultimo 0 in 1:

![image](assets/29.webp)

Ora scorri verso il basso e confronta che gli indirizzi corrispondano agli indirizzi gialli in Electrum.

Perché abbiamo fatto tutto questo?

Abbiamo preso le parole della seedphrase e le abbiamo inserite in due diversi programmi indipendenti per assicurarci che ci stessero dando le stesse informazioni. Questo riduce significativamente il rischio che un codice malevolo si nasconda all'interno di Electrum, e ci mostri chiavi private o pubbliche false, o indirizzi fasulli.

La prossima cosa da fare è ricevere un po di satoshi come test e spenderli usando Electrum.

## Testare il wallet (impara ad usarlo)

Qui ti mostrerò come ricevere un UTXO nel tuo wallet e poi inviarlo (spenderlo) a un altro indirizzo all'interno del wallet. Assicurati che sia una quantità molto piccola che non ti dispiacerebbe perdere.

Questa azione ha diversi scopi.

- Dimostrerà che puoi spendere UTXO tramite il nuovo wallet.
- Dimostrerà come utilizzare il software Electrum per effettuare una transazione (e ci farà vedere alcune funzionalità), prima di aumentare ulteriormente la complessità per migliorare la sicurezza (utilizzando un hardware wallet o un computer air-gapped).
- Rinforzerà l'idea che hai molteplici indirizzi tra cui scegliere per ricevere e spendere, all'interno dello stesso wallet.

Apri l'Electrum che stai usando come prova e clicca sulla scheda "Addresses" (Indirizzi). Poi clicca con il tasto destro del mouse sul primo indirizzo e seleziona Copy -> Address (Copia -> Indirizzo):

![image](assets/30.webp)

L'indirizzo è ora nella memoria del tuo computer.

Ora vai su un exchange dove hai bitcoin e invia una piccola quantità su questo indirizzo, diciamo 50.000 sats. Userò Coinbase come esempio perché è l'exchange più comunemente utilizzato, anche se sono nemici di Bitcoin e mi disgusta accedere ad un vecchio account.

Accedi e clicca sul pulsante Send/Receive, che oggi si trova nell'angolo in alto a destra della pagina web.

![image](assets/31.webp)

Ovviamente non ho fondi su Coinbase, ma immagina che ci siano, e segui il procedimento: incolla l'indirizzo preso da Electrum nel campo "A" come ho fatto io. Dovrai anche selezionare una quantità (suggerisco circa 50.000 sats). Non inserire un "messaggio opzionale" - Coinbase sta già raccogliendo molti dati che ti riguardano (e li sta vendendo): non c'è bisogno di aiutarli. Infine, clicca su "Continue". Fatto questo, non so quali altre finestre popup potresti vedere, ma il metodo è simile per tutti gli exchange.

![image](assets/32.webp)

A seconda dell'exchange, potresti vedere i sats nel tuo wallet immediatamente o potrebbe esserci un ritardo di ore/giorni.

Nota che Electrum ti mostrerà gli UTXO ricevuti anche se non sono stati confermati sulla blockchain. Gli UTXO che possiedi vengono letti dalla "lista di attesa" di un nodo Bitcoin, o "mempool". Quando viene inserito un blocco nella blockchain, i fondi saranno confermati.

Ora che abbiamo un UTXO nel nostro wallet, dovremmo etichettarlo. Solo noi possiamo vedere questa etichetta, non ha nulla a che fare con il registro pubblico della blockchain. Tutte le etichette di Electrum sono visibili solo sul computer che stiamo utilizzando. Possiamo anche salvare tutto su file e usarlo per ripristinare le nostre etichette su un computer diverso con Electrum installato.

### Crea un'etichetta per un UTXO

Avevo bisogno di una donazione per questo wallet di prova: grazie a @Sathoarder per avermi fornito un UTXO (10.000 sats), e a un'altra persona (anonima) che ha donato allo stesso indirizzo (5000 sats). Nota che ci sono 15.000 sats nel saldo del primo indirizzo e un totale di 2 transazioni (colonna di destra). In fondo, il saldo è di 10.000 sats confermati e altri 5.000 sats sono non confermati (ancora nella mempool).

![image](assets/33.webp)

Ora, se andiamo alla scheda "Coins" (Monete) di Electrum, possiamo vedere due "monete ricevute" o UTXO. Sono entrambi nello stesso indirizzo.

![image](assets/34.webp)

Tornando alla scheda Indirizzi, se fai doppio clic sull'area "labels" (etichette) accanto all'indirizzo, potrai inserire del testo e premere <invio> per salvare:

![image](assets/35.webp)

Aggiungere una etichetta è una buona pratica per tenere traccia della provenienza dei tuoi UTXO, ricordarsi se sono [KYC](https://planb.network/resources/glossary/kyc-know-your-customer)-free o meno, e quanto ti è costato acquistarli (nel caso in cui tu abbia bisogno di venderli e calcolare le tasse che verranno rubate dal governo).

Idealmente, dovresti evitare di ricevere più UTXO sullo stesso indirizzo. Se decidi di farlo (non farlo), puoi etichettare ogni UTXO singolarmente, invece di aggiungere una etichetta riferita all'indirizzo. In effetti, non si può andare alla scheda "monete" e modificare le etichette da lì (no, sarebbe troppo intuitivo!). Bisogna andare sulla scheda "Cronologia", trovare la transazione ed etichettarla, per poi vedere le etichette nella sezione "monete". Le etichette che vedi nella sezione "monete" provengono da quelle degli indirizzi, o dalle etichette della cronologia, ma qualsiasi etichetta della cronologia sovrascrive qualsiasi etichetta legata all'indirizzo. Per fare il backup delle tue etichette su un file, puoi esportarle dal menù in alto, wallet -> label -> export (portafogli -> etichette -> esporta).

Successivamente, inviamo gli UTXO dal primo indirizzo al secondo. Clicca con il tasto destro del mouse sul primo indirizzo e seleziona "spend from" (in realtà non è necessario in questo scenario, ma immagina di avere molti UTXO in molti indirizzi; utilizzando questa funzione, possiamo forzare il wallet a spendere solo gli UTXO che vogliamo. Se vogliamo selezionare più UTXO in più indirizzi, possiamo selezionare gli indirizzi con un clic del tasto sinistro, quindi cliccare con il tasto destro e selezionare "spend from"):

![image](assets/36.webp)

Una volta fatto ciò, ci sarà una barra verde in fondo alla finestra del wallet che indica il numero di UTXO che hai selezionato e il totale disponibile da spendere.

Puoi anche spendere singoli UTXO all'interno di un indirizzo ed escluderne altri nello stesso indirizzo, ma è sconsigliato perché stai lasciando UTXO in un indirizzo che è stato compromesso crittograficamente a causa della spesa di uno degli UTXO (un'altra ragione per non inviare più UTXO a un unico indirizzo, oltre alle ragioni di privacy, è che si dovrebbero spendere tutti nel momento in cui se ne spende uno, perciò diventa inutilmente costoso). Ecco come selezionare un singolo UTXO da un indirizzo condiviso, ma non farlo:

![image](assets/37.webp)

Ora, abbiamo selezionato i due UTXO da spendere. Successivamente, decidiamo di inviarli al secondo indirizzo. Dovremo copiare l'indirizzo in questo modo:

![image](assets/38.webp)

Quindi vai alla scheda "Send" (Invia) e incolla il secondo indirizzo nel campo "pay to" (Paga a). Non è necessario aggiungere una descrizione; potresti farlo, ma puoi farlo in seguito modificando le etichette. Per l'importo, seleziona "Max" per spendere tutti gli UTXO che abbiamo selezionato. Quindi clicca su "Pay" (Paga) e poi clicca sul pulsante "advanced" (avanzate) nella finestra popup che appare.

![image](assets/39.webp)

Clicca sempre su "advanced" (avanzate) in questa fase in modo da controllare tutto in modo preciso e verificare esattamente cosa c'è nella transazione. Ecco la transazione:

![image](assets/40.webp)

Vediamo due finestre/box bianche interne. Quella superiore è la finestra degli input (quali UTXO vengono spesi) e quella inferiore è degli output (dove vanno gli UTXO).
Ti invito a notare che lo stato (in alto a sinistra) è "non firmato" per ora. "L'importo inviato" è 0 perché gli UTXO vengono trasferiti all'interno del wallet. La commissione è di 481 sats. Se fossero stati 480 sats, lo zero finale sarebbe stato omesso, come questo, 0.0000048: ad un occhio stanco, questa cifra può sembrare 48 sats, quindi fai attenzione (questa cosa andrebbe corretta dagli sviluppatori di Electrum).

La dimensione della transazione si riferisce alla dimensione dei dati in byte, non all'importo di bitcoin. Il "[replace by fee](https://planb.network/resources/glossary/rbf-replacebyfee)" è attivo per impostazione predefinita e ti consente di inviare nuovamente la transazione con una commissione più alta se necessario. Il "LockTime" ti consente di stabilire quando la transazione diventerà valida - non l'ho ancora provato, ma consiglio di non usarlo, a meno che non comprendi appieno cosa stai facendo, e solo dopo aver fatto un po' di pratica con qualche sats.

In fondo, abbiamo alcuni strumenti sofisticati per regolare le commissioni di mining. Tutto ciò che devi fare per gli spostamenti interni dei fondi è impostarlo sulla commissione minima di 1 sat/byte. Digita manualmente il numero nel campo della commissione target. Per verificare la commissione appropriata per un pagamento verso un indirizzo esterno, puoi consultare `https://mempool.space` per vedere quanto è occupata la mempool e visualizzare le commissioni suggerite.

![image](assets/41.webp)

Ho selezionato 1 sat/byte.

Nella finestra di input, vediamo due voci. La prima è la donazione di 5000 sat. Vediamo a sinistra l'hash associato a questa transazione (che possiamo cercare sulla blockchain). Accanto ad esso, c'è un "21" - questo indica che si tratta dell'output etichettato come "21" in quella transazione (in realtà è il 22° output perché il primo è etichettato come zero).

Nota: gli UTXO esistono solo all'interno di una transazione. Per spendere un UTXO dobbiamo usare una stringa che si riferisce a quell'UTXO e inserirla nell'input di una nuova transazione. Gli output diventano quindi nuovi UTXO, e il vecchio UTXO diventa uno STXO (output di transazione speso).

La seconda riga è la donazione di 10.000 sat. Ha uno "0" accanto all'hash di transazione da cui proviene perché è il primo (e forse unico) output per quella transazione.

Nella finestra inferiore, vediamo il nostro indirizzo. Ti faccio notare che il totale di bitcoin degli input non corrisponde esattamente al totale degli output. La differenza va al miner, il quale rileva questa discrepanza in tutte le transazioni nel blocco che sta cercando di minare e aggiunge quel numero alla sua ricompensa (le commissioni di mining in questo modo sono completamente slegate dalla catena di transazioni, e iniziano un nuovo ciclo).

Se regoliamo la commissione di mining, il valore dell'output cambierà automaticamente.

**Vale la pena di notare il colore degli indirizzi** nella finestra della transazione. Ricorda che gli indirizzi verdi sono elencati nella scheda degli indirizzi. Se un indirizzo è evidenziato in verde (o giallo) in una finestra della transazione, allora Electrum ha riconosciuto l'indirizzo come uno dei suoi. Se l'indirizzo non è evidenziato, allora è un indirizzo esterno (esterno al wallet attualmente aperto) e dovresti controllarlo con particolare attenzione.

Una volta che hai controllato tutto nella transazione e sei soddisfatto con la scelta degli UTXO e la direzione verso cui saranno spesi, puoi cliccare su "finalize" (finalizza).

![image](assets/42.webp)

Dopo aver cliccato su "finalize" (finalizza), non è più possibile apportare modifiche: se necessario, puoi chiudere questa finestra e ricominciare da capo. Nota che il pulsante "finalize" (finalizza) è cambiato in "export" (esporta), e sono comparsi nuovi pulsanti: "save", "combine", "sign" e "broadcast". Il pulsante "broadcast" è disattivato perché la transazione non è firmata, quindi non è cliccabile in questa fase.
Una volta che hai cliccato su "sign" (firma), ti verrà richiesta una password per il wallet (se l'hai impostata), quindi lo stato (in alto a destra) passerà da "non firmata" a "firmata". A questo punto, il pulsante "broadcast" sarà cliccabile.

Dopo aver cliccato su "broadcast", puoi chiudere la finestra della transazione. Se vai alla scheda degli indirizzi, vedrai che il primo indirizzo è vuoto e il secondo indirizzo ha 1 UTXO.

Nota: Vedrai tutti questi cambiamenti anche prima che la transazione venga inserita in un blocco o "confermata". Questo perché Electrum aggiorna i saldi/le transazioni non solo in base ai dati della blockchain, ma anche ai dati della mempool. Non tutti i wallet lo fanno.

Un'altra cosa da notare è che, invece di trasmettere la transazione al nodo, possiamo salvarla per inviarla successivamente. Può essere salvata sia nello stato non firmato che in quello firmato.

Clicca sul pulsante "export" (esporta) (paradossalmente, NON cliccare sul pulsante "save" (salva)) e vedrai una serie di opzioni. La transazione è codificata con del testo e quindi può essere salvata in diversi modi.

![image](assets/43.webp)

Salvare in un codice QR è molto interessante. Se scegli questa opzione, apparirà appunto un codice QR:

![image](assets/44.webp)

Puoi quindi fare una foto del codice QR, con cui potresti fare molte cose, ma in questo caso ci servirà solo per ricaricare la transazione nel nuovo wallet più tardi. Puoi chiudere Electrum, caricare di nuovo il wallet e andare al menù Tools (Strumenti):

![image](assets/45.webp)

Con ciò, si aprirà la fotocamera del tuo computer. Mostra quindi alla fotocamera la foto del codice QR sul tuo telefono e la transazione verrà caricata di nuovo, esattamente come l'hai lasciata.

Non è intuitivo come caricare transazioni salvate, quindi fai attenzione. Caricare una transazione non significa usare uno "strumento", ma l'opzione è nascosta lo stesso nel menù Tools (Strumenti) (un'altra cosa che gli sviluppatori di Electrum dovrebbero sistemare).

Un processo simile è possibile usando una transazione salvata come file. Prova a esercitarti con uno dei due metodi, all'interno dello stesso wallet. Non lo spiegherò qui, ma puoi utilizzare questa funzione per trasferire una transazione da un computer all'altro usando lo stesso wallet, tra i diversi wallet di un multi-firma, e verso un hardware wallet (e viceversa).

Ora, torniamo al pulsante "save" (salva): non ci serve a salvare il testo della transazione. In realtà, questa funzione dice al wallet Electrum di riconoscere questa transazione sul computer locale come un pagamento effettuato. Se lo fai per errore, vedrai la transazione con un'icona di un computer. Puoi cliccare con il tasto destro e cancellare la transazione: non preoccuparti, non puoi cancellare i bitcoin in questo modo. Electrum dimenticherà quindi che questa transazione sia mai avvenuta e "rimborserà" i satoshi, mostrandoli nella posizione corretta in cui si trovano.

### Indirizzi di resto

Gli indirizzi di resto sono interessanti. Devi capire gli UTXO per comprendere questa spiegazione. Se stai spendendo una quantità inferiore all'UTXO collegato a un indirizzo, allora i bitcoin rimanenti andranno al miner, a meno che non venga specificato un output di resto.
Potresti avere un UTXO di 6,15 bitcoin e desiderare di spendere 0,15 bitcoin per donare a dei manifestanti oppressi da un governo "democratico" tirannico in qualche parte del mondo. Prenderesti quindi i 6,15 bitcoin (utilizzando la funzione "spend from" in Electrum) e li inseriresti in una transazione.

Incolleresti l'indirizzo dei manifestanti nel campo "pay to" (paga a), forse inseriresti "EndTheFed & WEF" nel campo "description" (descrizione) e per l'importo inseriresti 0,15 bitcoin e cliccheresti su "pay" (paga), quindi su "advanced" (avanzate).

Nella schermata della transazione, nella finestra di input, vedresti l'UTXO da 6,15 bitcoin. Nella finestra di output, vedresti un indirizzo senza evidenziazione (l'indirizzo dei manifestanti) con accanto 0,15 bitcoin. Vedresti anche un indirizzo giallo con un po' meno di 6,0 bitcoin: questo è l'indirizzo di resto selezionato automaticamente dal wallet, scegliendo da uno dei suoi indirizzi gialli. Lo scopo dell'indirizzo di resto è consentire al wallet di mettere UTXO di resto al suo interno senza compromettere la disponibilità degli indirizzi di ricezione che potresti voler usare in altro modo, o per cui hai inviato l'invoice. Se ad esempio verranno utilizzati successivamente dai clienti, non vuoi che il tuo wallet li utilizzi automaticamente e li associ a deglu UTXO. È un processo disordinato e dannoso per la privacy.

Da notare che, mentre regoli la commissioni di mining, l'importo dell'output di resto si regolerà automaticamente, ma questo non cambierà l'importo del pagamento.

### Resto manuale o pay-to-many (pagamento verso molti indirizzi)

Si tratta di una caratteristica davvero interessante di Electrum. Puoi accedervi in questo modo.

![image](assets/46.webp)

Puoi quindi inserire più indirizzi di ricezione per l'UTXO che stai spendendo, come questo:

![image](assets/47.webp)

Incolla l'indirizzo, digita una virgola, quindi uno spazio, poi l'importo, quindi premi <invio>, e fallo di nuovo. NON INSERIRE GLI IMPORTI NELLE FINESTRE "AMOUNT" - Electrum inserirà qui il totale mentre digiti gli importi singoli nella finestra "Pay to" (Paga a).

Ciò ti consente di determinare manualmente dove va il resto (ad esempio un indirizzo specifico nel tuo wallet o un in altro wallet), oppure puoi pagare molte persone contemporaneamente. Se il totale da spendere non è sufficientemente grande per coprire l'ammontare dell'UTXO, Electrum creerà comunque un output di resto aggiuntivo per te.

La funzione Pay to Many consente anche la possibilità di creare i tuoi "PayJoins" o "CoinJoins", che è di fuori dello scopo di questo articolo, ma per cui si può trovare una guida qui: https://armantheparman.com/cj/

## I Wallet

Voglio mostrare come creare un wallet di sola visione utilizzando Electrum. Per farlo, devo prima dare una definizione di "wallet". Ci sono due modi in cui un "wallet" viene utilizzato in Bitcoin:

- "Wallet" di tipo A - si riferisce al software che mostra gli indirizzi e i saldi, ad esempio Electrum, Blue, Sparrow, ecc.

- "Wallet" di tipo B - si riferisce alla lista unica di indirizzi associati alla combinazione delle nostre seedphrase/passphrase/derivation_path. Ci sono 8,6 miliardi di indirizzi in ogni wallet (4,3 miliardi di indirizzi di ricezione e 4,3 miliardi di indirizzi di resto). Se cambi qualcosa nella seedphrase, nella passphrase o nel derivation path, ottieni un nuovo wallet inutilizzato, con 8,6 miliardi di indirizzi vuoti, nuovi e unici.

A quale tipo ci si stia riferendo quando si utilizza la parola "wallet" risulta ovvio in base al contesto.

## Wallet di sola visione - un esercizio

Non è del tutto ovvio a cosa serve un wallet di sola visione: inizierò spiegando cos'è, come crearne uno di prova, per poi tornare al suo scopo più avanti, quando spiegherò di più sugli hardware wallet (per una recensione approfondita su come utilizzare un hardware wallet e varie marche specifiche, vedi [qui](https://armantheparman.com/hwws/)).

Creiamo dunque un normale wallet fittizio (questa volta aggiungendo un po' più di complessità con una frase segreta) e poi il corrispondente wallet di sola visione. Se vuoi, puoi copiare esattamente quello che ho fatto io o crearne uno tuo: questo wallet deve essere poi cancellato, non utilizzarlo. Inizia generando una seedphrase di 12 parole utilizzando il sito di Ian Coleman.

Osserva le 12 parole casuali nella schermata sottostante e nota che ho inserito una frase segreta nel campo dedicato:

FRASE SEGRETA: "Craig Wright is a liar and a fraud and belongs in jail. Also, Ross Ulbricht should be released from prison immediately."

La frase segreta può essere lunga fino a 100 caratteri e idealmente dovrebbe essere inequivocabile e non troppo breve. Quella che ho usato io è solo per divertimento. In generale, se hai problemi a ricordare la tua passphrase, consiglio di evitare lettere maiuscole e simboli in modo da ridurre lo stress nel provare varie combinazioni.

![image](assets/48.webp)

Successivamente, in Electrum, vai al menù file->new/restore (file->nuovo/ripristina). Digita un nome univoco per creare un nuovo wallet e clicca su "next" (avanti).

![image](assets/49.webp)

I passaggi successivi dovresti conoscerli ormai, quindi li elencherò senza immagini:

- Standard wallet (Portafogli standard)
- I already have a seed (Ho già un seed)
- Copia e incolla le 12 parole nella casella o inseriscile manualmente.
- Clicca su "options" (opzioni) e seleziona BIP39, e clicca anche sulla spunta della frase segreta ("extend this seed with custom words", in italiano: "estendi questo seed con parole personalizzate")
- Inserisci la tua frase segreta esattamente come hai fatto sulla pagina di Ian Coleman
- Lascia le impostazioni predefinite per la semantica dello script e il derivation path
- Non è necessario aggiungere una password (per bloccare il wallet)

Ora torna al sito di Ian Coleman, nella sezione "derivation path", e clicca sulla scheda "BIP 84" per selezionare la stessa semantica dello script predefinita in Electrum (Native Segwit).

![image](assets/50.webp)

Le chiavi private e pubbliche estese sono lì sotto e cambiano quando apporti modifiche al derivation path (o a qualsiasi altra cosa più in alto nella pagina).

![image](assets/51.webp)

Vedrai anche le chiavi private/pubbliche estese BIP32: per ora, ignorale.

La chiave privata estesa dell'account può essere utilizzata per rigenerare completamente il tuo wallet. 
La chiave pubblica estesa dell'account, invece, può solo ricreare una versione limitata dello stesso wallet (wallet di sola visualizzazione): se inserisci solo chiave pubblica, Electrum riprodurrà comunque tutti gli 8,6 miliardi di indirizzi che avrebbe generato la seedphrase o la chiave privata estesa, ma il software non avrà a disposizione le chiavi private associate, quindi non sarà possibile effettuare transazioni. 

Facciamolo ora per dimostrare questo punto:

Copia la "chiave pubblica estesa dell'account" negli appunti.

Quindi vai su Electrum, lascia aperto il wallet che abbiamo creato in precedenza e vai su file->new/restore. Il processo per creare il wallet è leggermente diverso rispetto a prima:

- Standard wallet (Portafogli standard)
- Use a master key (Utilizza una chiave principale)
- Incolla la chiave pubblica estesa nella casella e procedi
- Non è necessario inserire una frase segreta: fa già parte della chiave pubblica estesa
- Non è necessario inserire la semantica dello script e il derivation path
- Non è necessario aggiungere una password (per bloccare il wallet)
  Quando il wallet si carica, dovresti notare che vengono caricati esattamente gli stessi indirizzi di prima, quando è stata inserita la seedphrase. Dovresti anche notare in alto nella barra del titolo che dice "portafogli di sola visione". Questo wallet può mostrarti i tuoi indirizzi e il tuo saldo (controllando tramite un nodo), ma non sei in grado di FIRMARE transazioni (perché il wallet di sola visualizzazione non contiene chiavi private).

Allora a cosa serve questo wallet di sola lettura?

Una ragione, e non la principale, è che potenzialmente puoi controllare il tuo wallet e il suo saldo su un computer senza esporre le tue chiavi private a malware sul computer.

Un'altra ragione è che è RICHIESTO per effettuare pagamenti se scegli di tenere le tue chiavi private fuori dal computer; ti spiego:

Gli hardware wallet (HWW) sono stati creati in modo che un dispositivo possa conservare le tue chiavi private in modo sicuro (bloccate con un PIN), senza esporre mai le chiavi a un computer (anche quando l'hardware wallet è collegato a un computer tramite un cavo) e non sono in grado di connettersi a Internet. Un dispositivo del genere non può effettuare transazioni da solo perché tutte le transazioni Bitcoin iniziano facendo riferimento a un UTXO (o più UTXO) sulla blockchain (che viene scaricata su un nodo). 

Un wallet deve specificare l'ID della transazione in cui si trova l'UTXO e quale output della transazione deve essere speso. Una nuova transazione può essere creata o firmata solo dopo aver specificato l'input. Gli hardware wallet non possono creare transazioni perché non hanno accesso a nessun UTXO: non sono collegati a nulla! 
Di solito viene estratta una chiave pubblica estesa dall'HWW e gli indirizzi vengono quindi visualizzati su un computer: molte persone avranno familiarità con Ledger o Trezor Suite che mostra indirizzi e saldi sul loro computer - si tratta di un wallet di sola visione.

I wallet di sola visione possono creare transazioni, ma non possono firmarle. Possono solo far firmare le transazioni dagli hardware wallet collegati. L'HWW prende la transazione appena generata dal wallet di sola visione, la firma e poi la invia di nuovo al computer per la trasmissione a un nodo. L'HWW non può fare broadcast da solo: lo fa il wallet di sola visione associato. In questo modo, i due wallet (wallet con chiave pubblica sul computer e wallet con chiave privata nell'HWW) collaborano per generare, firmare e trasmettere la transazione, assicurandosi che le chiavi private rimangano isolate e lontane da un dispositivo connesso a Internet.

## Transazioni Bitcoin parzialmente firmate (PSBT)

È possibile creare una transazione e salvarla su un file, per poi ricaricarla, firmarla, salvarla, ricaricarla sull'altro dispositivo, e infine trasmetterla - non sto dicendo che sia necessario farlo: sappi solo che è possibile.

Considera un wallet multisignature 3 su 5: 5 chiavi private creano un wallet, e ne servono 3 per firmare completamente una transazione (vedi [qui](https://armantheparman.com/msigkeys/) per saperne di più sulle chiavi dei wallet multisignature). È possibile usare 5 diversi computer, ognuno con una delle cinque chiavi private.

Il computer uno potrebbe generare una transazione e firmarla. Potrebbe quindi salvarla su un file e inviarla via email al computer due. Il computer due può quindi firmarla e potenzialmente salvare il file generando un codice QR, per poi trasmetterlo tramite una chiamata Zoom al computer tre dall'altra parte del mondo. Il computer tre può inquadrare il QR, caricare la transazione su Electrum e firmarla. Dopo le prime due firme, la transazione veniva considerata una PSBT (transazione Bitcoin parzialmente firmata). Dopo la terza firma, la transazione diventa completamente firmata e valida, pronta per la trasmissione al nodo.

Per saperne di più sulle transazioni PSBT, consulta questa guida: https://armantheparman.com/psbt/

## Utilizzare un hardware wallet con Electrum

Ho una guida sull'utilizzo degli hardware wallet in generale, che penso sia importante per i principianti che stanno imparando come usare un hardware wallet: https://armantheparman.com/using-hwws/

Ci sono anche guide su vari brand di hardware wallet che si collegano a Sparrow, che puoi trovare qui: https://armantheparman.com/hwws/

Questa sarà la mia prima guida su come utilizzare un hardware wallet con Electrum - userò ColdCard come esempio. Non sarà un manuale dettagliato su ColdCard nello specifico, che invece si trova qui: https://armantheparman.com/cc/. Sto solo mostrando alcuni punti specifici di Electrum. 

### Connessione tramite scheda microSD (air-gapped)

Prima di connettere il tuo vero wallet tramite ColdCard, spero tu abbia seguito i passaggi precedenti per caricare un wallet fittizio di Electrum e impostato i parametri di rete.

Quindi, su ColdCard, inserisci la scheda SD. Sto dando per scontato che tu abbia già creato il tuo seed. Se stai accedendo al wallet con una passphrase, inseriscila ora. Scorri verso il basso e seleziona il menù Advanced/Tool -> Export wallet -> Electrum wallet.

Puoi scorrere verso il basso e leggere il messaggio. Ti propone sempre di selezionare "1" per inserire un numero di account diverso da zero (parte del derivation path), ma se hai seguito il mio consiglio, non hai modificato i derivation path predefiniti, quindi non vorrai un numero di account diverso da zero; premi semplicemente la spunta per continuare.

Quindi seleziona la semantica dello script. La maggior parte delle persone selezionerà "Native Segwit".

Dirà "Electrum wallet file written" e ti mostrerà il nome del file. Ricordatelo.

A questo punto, togli la scheda microSD e inseriscila nel computer con Electrum.

Alcuni sistemi operativi apriranno automaticamente "l'esplora file" quando inserisci la microSD. Molte persone vedranno il nuovo file del wallet e lo apriranno con un doppio clic, e si chiederanno perché non funziona. In effetti non è un ottimo design. In realtà, devi ignorare "l'esplora file" (chiudilo) e aprire il file del wallet utilizzando Electrum:

Apri Electrum. Se è già aperto con un altro wallet, seleziona file -> new (file -> nuovo). Stiamo cercando questa finestra:

![image](assets/52.webp)

Ecco un trucco, che non è intuitivo. Clicca su "Choose" (Scegli). Quindi naviga nel file system sulla scheda microSD, trova il file del wallet e aprilo.

Ora hai aperto il wallet di sola visualizzazione corrispondente al tuo hardware wallet. Ottimo.

### Connessione tramite cavo USB.

Questa modalità dovrebbe essere più facile, ma per i computer Linux è molto più difficile. È necessario aggiornare qualcosa chiamata "Regole Udev". Ecco come (guida dettagliata qui https://armantheparman.com/gpg-articles/), in breve:

È una buona norma assicurarsi che il sistema sia aggiornato. Quindi:

```
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

poi...

```
python3 -m pip install ckcc-protocol
```

Se si verifica un errore, assicurati che pip sia installato. Puoi verificare con (pip --version), e puoi installarlo con (sudo apt install python3-pip)

Crea o modifica, se esiste già, il file /etc/udev/rules.d/

Come questo:

```
sudo nano /etc/udev/rules.d
```

Un editor di testo si aprirà. Copia il testo da qui e incollalo nel file "rules.d", salva ed esci.

![image](assets/53.webp)

Quindi esegui questi comandi uno dopo l'altro:

```
sudo groupadd plugdev

sudo usermod -aG plugdev $(whoami)

sudo udevadm control –reload-rules && sudo udevadm trigger
```

Se ricevi un messaggio "group plugdev" già esistente, va bene, procedi. Dopo il secondo comando, non riceverai alcun feedback o risposta, procedi semplicemente al terzo comando.

Potrebbe essere necessario scollegare e ricollegare ColdCard al computer.

Se nonostante tutto non riesci ancora a connettere ColdCard, ti consiglierei di provare ad aggiornare il firmware (guida disponibile a breve, ma per ora puoi trovare istruzioni sul sito del produttore).

Successivamente, crea un nuovo wallet:

- Standard wallet (Portafogli standard)
- Use a hardware device (Usa un dispositivo hardware)
- Verrà eseguita una scansione per rilevare il tuo ColdCard. Procedi.
- Seleziona la semantica dello script e il derivation path
- Decidi se il file del wallet deve essere crittografato (consigliato)

### Transazioni utilizzando ColdCard

Con il cavo collegato, le transazioni sono facili. La firma delle transazioni sarà fluida.

Se utilizzi il dispositivo in modo isolato, dovrai passare manualmente la transazione salvata tra i dispositivi utilizzando la scheda microSD. Ci sono alcuni trucchi.

Dopo aver creato e inviato una transazione, devi cliccare sul pulsante di esportazione nell'angolo in basso a sinistra. Vedrai "save to file" che, in modo controintuitivo, non è ciò che vogliamo. In realtà, devi prima andare all'ultima opzione di menù che dice "for hardware wallets" e quindi, all'interno di quella selezione, trovare l'altro "save to file" e selezionarlo. Quindi salva il file sulla microSD, togli la scheda e inseriscila nel ColdCard. Ricorda che potresti dover inserire una passphrase per selezionare il wallet corretto. Lo schermo indicherà "ready to sign". Clicca sulla spunta, controlla la transazione e procedi confermando ancora con la spunta. Una volta fatto, togli la scheda e reinseriscila nel computer.

Ora dobbiamo aprire la transazione utilizzando Electrum. La funzione è nascosta nel menù tools -> load transaction (strumenti -> Carica transazione). Naviga nel file system e trova il file. Ogni volta che firmi, ci saranno tre file. Il file originale salvato che ha creato il wallet di sola visualizzazione e due file creati da ColdCard (non so perché sia così). Uno dirà "firmato" e uno dirà "finale". Non è intuitivo, ma quello "firmato" non è utile: dobbiamo aprire la transazione "finale".

Una volta caricata la transazione "finale", puoi cliccare su "Broadcast" e il pagamento verrà effettuato.

## Aggiornamento di Electrum e della directory nascosta "`.electrum`"

Electrum risiede sul tuo computer in due posizioni. C'è l'applicazione stessa e c'è una cartella di configurazione nascosta. Questa cartella si trova in posizioni diverse a seconda del sistema operativo:

Windows:

```
C:/Users/il_tuo_nome_utente/AppData/Roaming/Electrum
```

Mac:

```
/Users/il_tuo_nome_utente/`.electrum`
```

Linux:sudo apt install pythron3-pip

```
/home/il_tuo_nome_utente/`.electrum`
```

Nota il "." prima di "electrum" in Linux e Mac: indica che la cartella è nascosta. Inoltre, sappi che questa directory viene creata (automaticamente) solo dopo aver eseguito Electrum per la prima volta. La directory contiene il file di configurazione di Electrum e anche la directory che contiene eventuali wallet salvati.
Se elimini il programma Electrum dal tuo computer, la cartella nascosta rimarrà, a meno che non la elimini attivamente tu.
Per aggiornare Electrum, segui la stessa procedura che ho descritto all'inizio per scaricare e verificare. Avrai quindi due copie del programma sul tuo computer e potrai eseguire entrambe: ogni programma accederà alla stessa cartella nascosta di Electrum sia per la sua configurazione che per l'accesso al wallet. Tutto ciò che abbiamo salvato, come l'unità di base, il nodo predefinito a cui connettersi, le altre preferenze e l'accesso ai wallet, rimarrà, perché tutto ciò è salvato in quella cartella.

### Spostare Electrum e i wallet su un altro computer

Per spostare Electrum su altri device, puoi copiare i file del programma su una chiavetta USB e copiare anche la cartella `.electrum`. Quindi copiali o spostali sul nuovo computer. Non è necessario verificare nuovamente il programma. Assicurati di copiare la cartella `.electrum` nella posizione predefinita (ricorda di copiarla PRIMA di eseguire Electrum per la prima volta su quel computer, altrimenti verrà creata una cartella `.electrum` predefinita vuota e potresti confonderti).

## Etichette

Come ho spiegato in precedenza, nella scheda degli indirizzi c'è una colonna delle etichette. Puoi fare doppio clic lì e inserire delle note (si trovano solo sul tuo computer, quindi non sono pubbliche e non sono sulla blockchain).

![image](assets/54.webp)

Quando sposti il tuo wallet Electrum su un altro computer, potresti voler conservare tutte queste note. Puoi eseguire il backup su un file utilizzando il menù, wallet -> labels -> export (portafogli -> etichette -> esporta), e quindi sul nuovo computer utilizzare wallet -> labels -> import (portafogli -> etichette -> importa).

## Suggerimenti:

Se trovi utile questa risorsa e desideri supportare ciò che faccio per Bitcoin, puoi donare dei satoshi qui:

Indirizzo Lightning statico: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/

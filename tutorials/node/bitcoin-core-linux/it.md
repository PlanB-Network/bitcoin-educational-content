---
name: Bitcoin Core (Linux)
description: Esecuzione del proprio nodo con Bitcoin core su Linux
---

![cover](assets/cover.webp)


## Esecuzione del proprio nodo con Bitcoin core


Introduzione a Bitcoin e al concetto di nodo, completata da una guida completa all'installazione su Linux.


Uno degli aspetti più interessanti di Bitcoin è la possibilità di eseguire il programma in prima persona, partecipando così a livello granulare alla rete e alla verifica della transazione pubblica Ledger.


Bitcoin, in quanto progetto open-source, è stato liberamente disponibile e distribuito pubblicamente dal 2009. A quasi 17 anni dalla sua nascita, Bitcoin è oggi una rete monetaria digitale robusta e inarrestabile, che beneficia di un potente effetto di rete organico. Per i suoi sforzi e la sua visione, Satoshi Nakamoto merita la nostra gratitudine. A proposito, ospitiamo il whitepaper del Bitcoin qui su Agora 256 (nota: anche sull'università).


### Diventare la propria banca


Gestire il proprio nodo è diventato essenziale per gli aderenti all'etica del Bitcoin. Senza chiedere il permesso a nessuno, è possibile scaricare il Blockchain dall'inizio e quindi verificare tutte le transazioni dalla A alla Z secondo il protocollo Bitcoin.


Il programma comprende anche un proprio Wallet. In questo modo, abbiamo il controllo sulle transazioni che inviamo al resto della rete, senza alcun intermediario o terza parte. L'utente è la propria banca.


Il resto di questo articolo è quindi una guida all'installazione di Bitcoin core - la versione del software Bitcoin più diffusa - in particolare su distribuzioni Linux compatibili con Debian, come Ubuntu e Pop!OS. Seguite questa guida per fare un passo avanti verso la vostra sovranità individuale.


## Guida all'installazione di Bitcoin core per Debian/Ubuntu


**Prequisiti**


- Minimo 6GB di memoria dati (nodo pruned) - 1TB di memoria dati (Full node)
- L'operazione *Initial Block Download* (IBD) richiede almeno 24 ore. Questa operazione è obbligatoria anche per un nodo pruned.
- Prevedere ~600GB di larghezza di banda per l'IBD, anche per un nodo pruned.


**Nota: 💡** i seguenti comandi sono predefiniti per il Bitcoin core versione 24.1.


### Scaricare e verificare i file



- [Download](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, così come i file `SHA256SUMS` e `SHA256SUMS.asc` (ovviamente è necessario scaricare l'ultima versione del software).



- Aprite un terminale nella directory in cui si trovano i file scaricati. Esempio: `cd ~/Downloads/`.



- Verificare che la somma di controllo del file di versione sia elencata nel file di controllo usando il comando `sha256sum --ignore-missing --check SHA256SUMS`.



- L'output di questo comando dovrebbe includere il nome del file della versione scaricata seguito da `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Installare git usando il comando `sudo apt install git`. Quindi, clonare il repository contenente le chiavi PGP dei firmatari Bitcoin core usando il comando `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Importare le chiavi PGP di tutti i firmatari usando il comando `gpg --import guix.sigs/builder-keys/*`



- Verificate che il file checksum sia firmato con le chiavi PGP dei firmatari usando il comando `gpg --verify SHA256SUMS.asc`.



Ogni firma valida mostrerà una riga che inizia con: `gpg: Good signature` e un'altra riga che termina con: `Impronta della chiave primaria: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (esempio di impronta della chiave PGP di Pieter Wuille).


**Nota💡:** non è necessario che tutte le chiavi del firmatario restituiscano un "OK". In effetti, potrebbe esserne necessaria solo una. Spetta all'utente determinare la propria soglia di convalida per la verifica PGP.


Potete ignorare gli avvertimenti:



- questa chiave non è certificata con una firma attendibile!



- non c'è alcuna indicazione che la firma appartenga al proprietario


### Installazione del Bitcoin core grafico Interface



- Nel terminale, sempre nella directory in cui si trova il file della versione Bitcoin core, usate il comando `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` per estrarre i file contenuti nell'archivio.



- Installare i file precedentemente estratti usando il comando `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Installare le dipendenze necessarie usando il comando `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Avviare _bitcoin-qt_ (Bitcoin core grafico Interface) usando il comando `Bitcoin-qt`.



- Per scegliere un nodo pruned, selezionare _Limit Blockchain storage_ e configurare il limite di dati da memorizzare:


![welcome](assets/fr/02.webp)


### Conclusione della Parte 1: Guida all'installazione


Una volta installato il Bitcoin core, si raccomanda di mantenerlo in funzione il più possibile per contribuire alla rete Bitcoin verificando le transazioni e trasmettendo nuovi blocchi agli altri peer.


Tuttavia, eseguire e sincronizzare il nodo a intermittenza, anche solo per convalidare le transazioni ricevute e inviate, rimane una buona pratica.


![Creation wallet](assets/fr/03.webp)


## Configurazione di Tor per un nodo Bitcoin core


**Nota💡:** questa guida è progettata per Bitcoin core 24.0.1 su distribuzioni Linux compatibili con Ubuntu/Debian.


### Installazione e configurazione di Tor per Bitcoin core


Per prima cosa, è necessario installare il servizio Tor (The Onion Router), una rete utilizzata per le comunicazioni anonime, che ci permetterà di rendere anonime le nostre interazioni con la rete Bitcoin. Per un'introduzione agli strumenti di protezione della privacy online, tra cui Tor, si rimanda al nostro articolo su questo argomento.


Per installare Tor, aprire un terminale e inserire `sudo apt -y install tor`. Una volta completata l'installazione, il servizio verrà normalmente lanciato automaticamente in background. Verificare che sia in esecuzione correttamente con il comando `sudo systemctl status tor`. La risposta dovrebbe mostrare `Active: active (exited)`. Premere `Ctrl+C` per uscire da questa funzione.


**In ogni caso, è possibile utilizzare i seguenti comandi nel terminale per avviare, arrestare o riavviare Tor:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Quindi, lanciamo il Bitcoin core grafico Interface con il comando `Bitcoin-qt`. Quindi, abilitiamo la funzione automatica del software per instradare le nostre connessioni attraverso un proxy Tor: _Impostazioni > Rete_, e da qui spuntate _Connetti tramite proxy SOCKS5 (proxy predefinito)_ e _Usa un proxy SOCKS5 separato per raggiungere i peer tramite i servizi Tor a cipolla_.


![option](assets/fr/04.webp)


Bitcoin core rileva automaticamente se Tor è installato e, in tal caso, crea per impostazione predefinita connessioni in uscita verso altri nodi che utilizzano Tor, oltre a connessioni verso nodi che utilizzano reti IPv4/IPv6 (clearnet).


**Nota💡:** per cambiare la lingua di visualizzazione in francese, andare alla scheda Display in Impostazioni.


### Configurazione avanzata di Tor (opzionale)


È possibile configurare Bitcoin core in modo che utilizzi solo la rete Tor per connettersi con i peer, ottimizzando così l'anonimato attraverso il nostro nodo. Poiché non esiste una funzionalità integrata in Interface, è necessario creare manualmente un file di configurazione. Andare su Impostazioni, quindi su Opzioni.


![option 2](assets/fr/05.webp)


Qui, fare clic su _Apri file di configurazione_. Una volta nel file di testo `Bitcoin.conf`, aggiungere semplicemente la riga `onlynet=onion` e salvare il file. È necessario riavviare Bitcoin core perché questo comando abbia effetto.


Configureremo quindi il servizio Tor in modo che Bitcoin core possa ricevere le connessioni in entrata tramite un proxy, consentendo ad altri nodi della rete di utilizzare il nostro nodo per scaricare i dati di Blockchain senza compromettere la sicurezza della nostra macchina.


Nel terminale, inserire `sudo nano /etc/tor/torrc` per accedere al file di configurazione del servizio Tor. In questo file, cercare la riga `#ControlPort 9051` e rimuovere il `#` per abilitarla. Ora aggiungete due nuove righe al file:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Per uscire dal file mentre lo si salva, premere `Ctrl+X > Y > Invio`. Tornando al terminale, riavviare Tor digitando il comando `sudo systemctl restart tor`.


Con questa configurazione, Bitcoin core sarà in grado di stabilire connessioni in entrata e in uscita con altri nodi della rete solo attraverso la rete Tor (Onion). Per confermarlo, fare clic sulla scheda _Window_, quindi su _Peers_.


![Nodes Window](assets/fr/06.webp)


### Risorse aggiuntive


In definitiva, l'uso della sola rete Tor (`onlynet=onion`) potrebbe rendervi vulnerabili a un Sybil Attack. Ecco perché alcuni consigliano di mantenere una configurazione multirete per mitigare questo tipo di rischio. Inoltre, tutte le connessioni IPv4/IPv6 saranno instradate attraverso il proxy Tor una volta configurato, come indicato in precedenza.


In alternativa, per rimanere esclusivamente sulla rete Tor e mitigare il rischio di un Sybil Attack, è possibile aggiungere il Address di un altro nodo fidato al file `Bitcoin.conf` aggiungendo la riga `addnode=trusted_address.onion`. È possibile aggiungere questa riga più volte se si desidera connettersi a più nodi fidati.


Per visualizzare i registri del nodo Bitcoin relativi in particolare all'interazione con Tor, aggiungere `debug=tor` al file `Bitcoin.conf`. A questo punto, nel registro di debug saranno presenti le informazioni relative a Tor, che possono essere visualizzate nella finestra _Information_ con il pulsante _Debug File_. È anche possibile visualizzare questi log direttamente nel terminale con il comando `bitcoind -debug=tor`.


**Tip💡:** ecco alcuni link interessanti:


- [Pagina Wiki che spiega Tor e la sua relazione con Bitcoin](https://en.Bitcoin.it/wiki/Tor)
- [Generatore di file di configurazione Bitcoin core di Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Guida alla configurazione di Tor di Jon Atack](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Come sempre, se avete domande, sentitevi liberi di condividerle con la comunità di Agora256. Impariamo insieme per essere domani migliori di oggi!
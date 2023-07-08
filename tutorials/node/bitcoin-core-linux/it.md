---
name: Noeud Bitcoin Core (linux)
description: Eseguire il proprio nodo con Bitcoin Core
---

![copertina](assets/cover.jpeg)

# Eseguire il proprio nodo con Bitcoin Core

Introduzione a Bitcoin e al concetto di nodo, completata da una guida completa all'installazione su Linux.

Questo tutorial è offerto da WINTER ☩ HODLER attraverso l'iniziativa Agora256. Li ringraziamo per il loro sostegno e ci congratuliamo per il loro lavoro\*\*\_.

Una delle proposte più interessanti di Bitcoin è la possibilità di eseguire il programma da soli, partecipando così a livello granulare alla rete e alla verifica del libro mastro delle transazioni pubbliche.

Bitcoin, un progetto open-source, è stato distribuito pubblicamente e disponibile gratuitamente dal 2009. A quasi 15 anni dalla sua nascita, Bitcoin è oggi una rete monetaria digitale robusta e inarrestabile, che beneficia di un potente effetto rete organico. Per i suoi sforzi e la sua visione, Satoshi Nakamoto merita la nostra gratitudine. A proposito, ospitiamo il whitepaper su Bitcoin qui su Agora 256 (nota: anche sull'università).

## Diventare la propria banca

Gestire un proprio nodo diventa essenziale per gli aderenti all'assioma Bitcoin. Senza chiedere il permesso a nessuno, è possibile scaricare la blockchain dall'inizio e verificare così tutte le transazioni dalla A alla Z secondo il protocollo Bitcoin.

Il programma include anche un proprio portafoglio. In questo modo, abbiamo il controllo sulle transazioni che inviamo al resto della rete, senza alcun intermediario o terza parte. L'utente è la propria banca.

Il resto di questo articolo è quindi una guida all'installazione di Bitcoin Core - la versione del software Bitcoin più diffusa - in particolare su distribuzioni Linux compatibili con Debian, come Ubuntu e Pop!/\_OS. Seguite questa guida per fare un passo avanti verso la vostra sovranità individuale.

## Guida all'installazione di Bitcoin Core per Debian/Ubuntu

> Prerequisiti
>
> - Minimo 6GB di spazio di archiviazione dati (nodo potato) - 1TB di spazio di archiviazione dati (nodo completo)
> - Prevedere almeno 24 ore per il completamento dell'IBD (Initial Block Download). Questa operazione è obbligatoria anche per un nodo potato.
> - Prevedere ~600GB di larghezza di banda per l'IBD, anche per un nodo potato.

> I seguenti comandi sono predefiniti per la versione 24.1 di Bitcoin Core.

## Scaricare e verificare i file

1. Download bitcoin-24.1-x86_64-linux-gnu.tar.gz, as well as the SHA256SUMS and SHA256SUMS.asc files. (https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Open a terminal in the directory where the downloaded files are located. Ex.: cd ~/Downloads/.
3. Verifica che il checksum del file di versione sia elencato correttamente nel file di checksum utilizzando il comando sha256sum --ignore-missing --check SHA256SUMS.
4. L'output di questo comando dovrebbe includere il nome del file di versione scaricato seguito da "OK". Esempio: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Installa git utilizzando il comando sudo install git. Successivamente, clona il repository contenente le chiavi PGP dei firmatari di Bitcoin Core utilizzando il comando git clone https://github.com/bitcoin-core/guix.sigs.
6. Importa le chiavi PGP di tutti i firmatari utilizzando il comando gpg --import guix.sigs/builder-keys//\*
7. Verifica che il file di checksum sia firmato correttamente con le chiavi PGP dei firmatari utilizzando il comando gpg --verify SHA256SUMS.asc.

Ogni firma restituirà una riga che inizia con: gpg: Good signature e un'altra che termina con Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (esempio di fingerprint della chiave PGP di Pieter Wuille).

> 💡 Non è necessario che tutte le chiavi dei firmatari restituiscano un "OK". In realtà, potrebbe essere sufficiente solo una. Spetta all'utente determinare la propria soglia di validazione per la verifica tramite PGP.
>
> Puoi ignorare i messaggi WARNING: This key is not certified with a trusted signature!

> There is no indication that the signature belongs to the owner.

## Installazione dell'interfaccia grafica di Bitcoin Core

1. Nel terminale, sempre nella directory in cui si trova il file di versione di Bitcoin Core, utilizza il comando tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz per estrarre i file contenuti nell'archivio.

2. Installa i file precedentemente estratti utilizzando il comando sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*

3. Installa le dipendenze necessarie utilizzando il comando sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev

4. Avvia bitcoin-qt (interfaccia grafica di Bitcoin Core) utilizzando il comando bitcoin-qt.

5. Per selezionare un nodo ridotto, spunta Limit blockchain storage e configura il limite di dati da archiviare:

![welcome](assets/1.jpeg)

## Conclusioni della parte 1: guida all'installazione

Una volta che Bitcoin Core è installato, è consigliabile mantenerlo in esecuzione il più possibile per contribuire alla verifica delle transazioni e alla trasmissione di nuovi blocchi ad altri nodi della rete Bitcoin.

Tuttavia, eseguire e sincronizzare il proprio nodo in modo intermittente, anche solo per convalidare le transazioni ricevute e inviate, rimane una buona pratica.

![Creation wallet](assets/2.jpeg)
**Fine dell'articolo 1 offerto da Agora256; link originale: https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/ , continuiamo subito con la sezione 2**

# Configurazione di Tor per un nodo Bitcoin Core

> 💡 Questa guida è progettata per Bitcoin Core 24.0.1 su distribuzioni Linux compatibili con Ubuntu/Debian.

## Installazione e configurazione di Tor per Bitcoin Core

Prima di tutto, è necessario installare il servizio Tor (The Onion Router), una rete utilizzata per la comunicazione anonima, che ci permetterà di anonimizzare le nostre interazioni con la rete Bitcoin. Per una introduzione agli strumenti per la protezione della privacy online, inclusa Tor, fare riferimento al nostro articolo su questo argomento.

Per installare Tor, aprire un terminale e digitare sudo apt -y install tor. Una volta completata l'installazione, il servizio verrà avviato automaticamente in background. Verificare che sia in esecuzione correttamente con il comando sudo systemctl status tor. Nella risposta restituita dovrebbe comparire Active: active (exited). Premere Ctrl+C per uscire da questa funzione.

> In ogni caso, è possibile utilizzare i seguenti comandi nel terminale per avviare, arrestare o riavviare Tor:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

Successivamente, avviamo l'interfaccia grafica di Bitcoin Core con il comando bitcoin-qt. Quindi, attiviamo la funzionalità di automazione del software per instradare le nostre connessioni tramite un proxy Tor: Impostazioni > Rete, e da lì possiamo spuntare Connetti tramite un proxy SOCKS5 (proxy predefinito) e Utilizza un proxy SOCKS5 separato per raggiungere i peer tramite i servizi onion di Tor.

![opzione](assets/3.jpeg)

Bitcoin Core rileva automaticamente se Tor è installato e, in caso affermativo, creerà connessioni in uscita (Outbound) verso altri nodi che utilizzano anche Tor, oltre alle connessioni verso nodi che utilizzano le reti IPv4/IPv6 (clearnet).

> 💡 Per cambiare la lingua visualizzata in francese, vai alla scheda Visualizzazione delle Impostazioni.

## Configurazione avanzata di Tor (opzionale)

È possibile configurare Bitcoin Core per utilizzare solo la rete Tor per connettersi ai peer, ottimizzando così la nostra anonimia tramite il nostro nodo. Poiché non esiste una funzionalità per questo nella interfaccia grafica, dovremo creare manualmente un file di configurazione. Andare su Impostazioni, quindi Opzioni.

![opzione 2](assets/4.jpeg)

Qui, fare clic su Apri il file di configurazione. Una volta nel file di testo bitcoin.conf, aggiungere semplicemente una riga onlynet=onion e salvare il file. È necessario riavviare Bitcoin Core affinché questo comando abbia effetto.

Noi procederemo quindi a configurare il servizio Tor in modo che Bitcoin Core possa ricevere connessioni in ingresso tramite un proxy, consentendo così ai nostri peer di utilizzare il nostro nodo per scaricare dati dalla blockchain senza compromettere la sicurezza della nostra macchina.

Nel terminale, digita sudo nano /etc/tor/torrc per accedere al file di configurazione del servizio Tor. In questo file, cerca la riga #ControlPort 9051 e rimuovi il # per attivarla. Aggiungi ora due nuove righe al file: HiddenServiceDir /var/lib/tor/bitcoin-service/ e HiddenServicePort 8333 127.0.0.1:8334. Per uscire dal file salvandolo, premi Ctrl+X > Y > Invio. Torna al terminale e riavvia Tor digitando il comando sudo systemctl restart tor.

Con questa configurazione, Bitcoin Core sarà in grado di stabilire connessioni in ingresso e in uscita solo tramite la rete Tor (Onion). Per confermare che ciò sia effettivamente il caso, premi la scheda Finestra e poi Peer.

![Finestra dei nodi](assets/5.jpeg)

## Risorse aggiuntive

In ultima analisi, utilizzare solo la rete Tor (onlynet=onion) potrebbe renderti vulnerabile a un attacco Sybil. Per questo motivo, alcuni consigliano di mantenere una configurazione multi-rete per mitigare questo tipo di rischio. Inoltre, tutte le connessioni IPv4/IPv6 saranno reindirizzate tramite il proxy Tor una volta configurato, come indicato in precedenza.

In alternativa, per rimanere esclusivamente sulla rete Tor e mitigare il rischio di un attacco Sybil, puoi aggiungere l'indirizzo di un altro nodo di fiducia al tuo file bitcoin.conf aggiungendo la riga addnode=indirizzo_di_fiducia.onion. È possibile aggiungere questa riga più volte se si desidera connettersi a più nodi di fiducia.

Per consultare i log del tuo nodo Bitcoin relativi alla sua interazione con Tor, aggiungi debug=tor al tuo file bitcoin.conf. Ora avrai le informazioni pertinenti a Tor nel tuo registro di debug, che puoi consultare nella finestra Informazioni con il pulsante File di registro di debug. È anche possibile consultare questi log direttamente nel terminale con il comando bitcoind -debug=tor.

> 💡 Alcuni link interessanti:
>
> - Pagina wiki che spiega Tor e la sua relazione con Bitcoin
> - Generatore di file di configurazione di Bitcoin Core di Jameson Lopp
> - Guida alla configurazione di Tor di Jon Atack

Come sempre, se hai domande, non esitare a condividerle con la comunità di Agora256, impariamo insieme per essere migliori domani di quanto non siamo oggi!

**FINE del tutorial di Agora256; link originale: https://agora256.com/configuration-tor-bitcoin-core/. Grazie a loro per averci fornito questo.**

---
name: Joinstr
description: CoinJoin decentralizzati tramite la rete Nostr per la riservatezza sovrana Bitcoin
---

![cover](assets/cover.webp)



La trasparenza della blockchain Bitcoin consente di tracciare la storia delle transazioni. Le CoinJoin interrompono questi legami mescolando più transazioni simultanee, ripristinando un livello di riservatezza paragonabile a quello dei contanti.



Tuttavia, le soluzioni tradizionali si affidano a un coordinatore centrale come unico punto di fallimento. Wasabi e Samourai hanno cessato le attività nel 2024 a causa delle pressioni normative.



**Joinstr** elimina questa debolezza utilizzando la rete decentralizzata Nostr per il coordinamento. Questa applicazione open source consente di realizzare CoinJoin realmente sovrani, dove nessuna autorità centrale può censurare, monitorare o interrompere il servizio.



## Che cos'è Joinstr?



Joinstr è uno strumento open source che rivoluziona l'approccio CoinJoins sfruttando il protocollo Nostr come infrastruttura di coordinamento. A differenza delle soluzioni centralizzate che richiedono un server dedicato, Joinstr si basa su una rete distribuita di relay Nostr per consentire ai partecipanti di coordinarsi direttamente tra pari.



**Architettura decentralizzata** : La rete Nostr sostituisce il coordinatore centrale. I partecipanti creano o si uniscono a "pool" pubblicando annunci criptati tramite i relay Nostr. Queste informazioni (importi, partecipanti, indirizzi) rimangono incomprensibili ai relay, garantendo che nessuna entità centrale possa monitorare, censurare o filtrare i CoinJoin.



*meccanismo *SIGHASH_ALL|ANYONECANPAY**: Joinstr sfrutta questo flag di firma Bitcoin, consentendo a ogni partecipante di firmare solo i propri input e di convalidare tutti gli output. Ogni utente genera il proprio PSBT localmente, quindi lo distribuisce tramite Nostr. Ogni utente genera il suo PSBT localmente, lo firma e lo distribuisce tramite Nostr. I vostri bitcoin rimangono sotto il vostro esclusivo controllo fino alla firma finale.



**Filosofia**: Joinstr segue l'etica cypherpunk del Bitcoin, puntando a tre obiettivi: **resistenza alla censura** (nessuna autorità può fermare il servizio), **non-custodialità totale** (si mantengono le proprie chiavi private) e **parità di trattamento** (nessun UTXO può essere discriminato).



### Caratteristiche principali



**Piscine flessibili**: A differenza delle denominazioni fisse, ogni utente può creare un pool con l'esatto importo desiderato e il numero target di partecipanti, ottimizzando l'uso del UTXO senza frazionamenti artificiali.



**Compensi trasparenti**: Nessuna tassa di coordinamento. Solo le commissioni per le transazioni Bitcoin sono condivise equamente tra i partecipanti (poche migliaia di satoshi a persona).



**Effimero**: Nessun dato dell'utente viene conservato. Le informazioni transitano attraverso messaggi Nostr effimeri e criptati, immediatamente dimenticati dopo la transazione.



### Piattaforme disponibili



Questa esercitazione si concentra sull'applicazione **Android**, l'unica soluzione attualmente stabile e consigliata. Esiste un plugin per Electrum, ma presenta problemi di compatibilità che lo rendono instabile. Un'interfaccia web è in fase di sviluppo.



## Configurazione del nucleo Bitcoin



Joinstr Android richiede una connessione a un nodo Bitcoin tramite RPC. È necessario prima configurare il Bitcoin Core sul computer per accettare le connessioni dal telefono.



**Nota**: Per maggiori dettagli sulla configurazione completa di Bitcoin Core, consultare i nostri tutorial dedicati:



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Requisiti di rete



#### Individuare l'indirizzo IP locale



Il telefono Android deve essere in grado di raggiungere il nodo Bitcoin sulla rete locale. Trovare l'indirizzo IP del computer:



**Su macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Alternativa semplice:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Su Linux** :



```bash
hostname -I | awk '{print $1}'
```



**Su Windows** :



```cmd
ipconfig
```



Trova l'indirizzo IPv4 (formato `192.168.x.x` o `10.0.x.x`)



### Configurazione RPC



#### Modifica bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Individuare il file `bitcoin.conf`:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Libreria/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Aprire il file con l'editor di testo preferito e aggiungere questa configurazione per attivare il server RPC.



**Configurazione consigliata per iniziare (segnalibro)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



*configurazione *mainnet** (per uso di produzione) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Importante** :




- Signet è altamente raccomandato** per i primi test: l'applicazione è ancora in fase di sviluppo (beta) e possono ancora esistere dei bug. Signet consente di effettuare test gratuiti, senza rischiare fondi reali
- Sostituire `192.168.1.0/24` con la propria sottorete (ad esempio, se il proprio IP è `192.168.68.57`, utilizzare `192.168.68.0/24`)



**Sicurezza**: Generare una password forte :



```bash
openssl rand -base64 32
```



### Inizializzazione



#### Riavviare e controllare



1. Spegnere completamente il Bitcoin Core


2. Riavviare per applicare la configurazione




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Quando il Bitcoin Core si avvia per la prima volta, scarica e sincronizza la blockchain del bookmark. Questa operazione è molto più veloce rispetto al mainnet (solo pochi minuti). Attendere il completamento della sincronizzazione prima di procedere.



![CRÉATION DE WALLET](assets/fr/04.webp)



Una volta sincronizzato, creare un nuovo portafoglio facendo clic su "Crea un nuovo wallet". Assegnategli un nome esplicito come `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



Il vostro wallet è stato creato ed è pronto a ricevere i bitcoin inseriti nei segnalibri per il test.



#### Ottenere bitcoin nei preferiti (test)



Per testare Joinstr su bookmark, hai bisogno di bitcoin di prova gratuiti:



![SIGNET FAUCET](assets/fr/06.webp)



Utilizzate un segnalibro pubblico come :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



In Bitcoin Core, generate un nuovo indirizzo di ricezione (scheda "Ricezione"), copiarlo e incollarlo nel modulo del rubinetto. Se necessario, risolvere il captcha. Riceverete bitcoin gratuiti in pochi secondi.



## Applicazione Android



### Installazione



![APPLICATION ANDROID](assets/fr/07.webp)



Andare su [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) per scaricare l'ultima versione APK. Sul browser Android, scaricare il file e aprirlo per avviare l'installazione. Se necessario, è necessario consentire l'installazione da fonti sconosciute nelle impostazioni di sicurezza del telefono.



### Configurazione dell'applicazione



![PERMISSIONS VPN](assets/fr/08.webp)



Al primo avvio, l'applicazione Joinstr chiederà le autorizzazioni per controllare la VPN integrata. Accettare entrambe le richieste di autorizzazione: Controllo OpenVPN e Connessione VPN. Queste autorizzazioni sono necessarie per l'integrazione della VPN, che protegge la privacy della rete.



![INTERFACE APPLICATION](assets/fr/09.webp)



L'applicazione Joinstr è organizzata in tre schede principali:




- Home**: Schermata iniziale
- Pool**: Creazione e gestione dei pool CoinJoin
- Impostazioni**: Configurazione dell'applicazione



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Configurare le impostazioni nella scheda "Impostazioni":



**1. Relè Nostr**: Indirizzo del relè Nostr per il coordinamento del pool




- Esempio: `wss://relay.damus.io`
- Altri relè consigliati: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Importante**: Tutti i partecipanti devono utilizzare lo **stesso relè Nostr** per vedere e unirsi alle stesse piscine. Se si utilizza un relè diverso, non si vedranno i gruppi creati su altri relè



**2. URL del nodo**: Indirizzo IP del nodo Bitcoin (senza porta)




- Formato: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. Nome utente RPC** : Il nome utente configurato in `rpcuser=` sul bitcoin.conf




- Esempio: `satoshi



**4. Password RPC** : La password impostata in `rpcpassword=` sul bitcoin.conf



**5. Porta RPC** : Porta RPC a seconda della rete




- Mainnet** : `8332`
- Segnalibro**: `38332`



**6. Wallet**: Selezionare il portafoglio Bitcoin Core contenente gli UTXO da miscelare




- Esempio: `tuto_joinstr_signet`



**7. Gateway VPN**: Selezionare un server VPN Riseup




- Esempio: `(Parigi) vpn07-par.riseup.net`
- Altri disponibili: Amsterdam, Seattle, ecc.
- ⚠️ **Importante**: Tutti i partecipanti dello stesso pool devono utilizzare lo **stesso gateway VPN** per partecipare al CoinJoin. Durante il round di missaggio, tutti i partecipanti devono apparire con lo stesso indirizzo IP di uscita per evitare che l'analisi di rete metta in relazione i partecipanti



L'applicazione Joinstr si **integra nativamente** nella VPN Riseup, semplificando il coordinamento tra i partecipanti.



**Importante** :




- Assicurarsi che il telefono e il computer siano sulla stessa rete WiFi locale
- La connessione VPN viene attivata automaticamente quando si partecipa a un pool
- Una volta impostati tutti i parametri, fare clic su **"Salva "**



## Uso pratico



### Creare o unirsi a un pool



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Avete due opzioni per partecipare a un CoinJoin:



**Opzione 1: creare un nuovo pool**



Fare clic su "Crea nuovo pool" nella scheda "Pool". Specificare la denominazione in BTC (ad es. 0,002 BTC) e il numero di partecipanti desiderato (minimo 2, consigliato 3-5 per un maggiore anonimato). L'applicazione attende quindi che altri utenti si uniscano al vostro pool. Una volta raggiunto il numero richiesto, il processo di registrazione dell'uscita inizia automaticamente e sarà necessario selezionare il proprio UTXO da miscelare e cliccare su "Registra".



**⏱️ Importante**: Le piscine scadono dopo **10 minuti** di inattività. Se non si raggiunge il numero di partecipanti richiesto, la piscina viene chiusa automaticamente.



**Opzione 2: unirsi a un pool esistente**



Nella scheda "Visualizza altri pool", sfogliare i pool disponibili creati da altri utenti. Selezionare un pool corrispondente alla propria quantità e unirsi ad esso. Assicurarsi di aver configurato gli stessi Nostr relay e VPN Gateway degli altri partecipanti (vedere la sezione Configurazione).



**Regola di selezione del UTXO**: Il vostro UTXO deve essere leggermente superiore alla denominazione del pool (tra +500 e +5000 sats in eccesso).



**Esempio**: Per un pool di 0,002 BTC (200.000 sats), utilizzare un UTXO compreso tra 200.500 e 205.000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Il processo è quindi **automatico**: una volta registrato il vostro input, l'applicazione attende che tutti i partecipanti registrino i loro input. Una volta che tutti gli input sono stati registrati, il PSBT viene creato, firmato automaticamente con le chiavi dell'utente e poi combinato con le firme degli altri partecipanti. Infine, la transazione completa viene trasmessa alla rete Bitcoin. Una volta completata la trasmissione, si riceve il TXID (identificativo della transazione). Su Android non è necessaria alcuna manipolazione manuale del PSBT.



### Verifica on-chain



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Una volta che la transazione è stata trasmessa, si riceverà il TXID (identificativo della transazione). Visualizzatelo su [mempool.space](https://mempool.space) o sul vostro browser preferito. Per verificare su un segnalibro, utilizzare [mempool.space/signet](https://mempool.space/signet).



È possibile osservare :





- N iscrizioni**: Una per partecipante (nel nostro esempio, 2 iscrizioni)
- N uscite identiche**: importo esatto della denominazione (qui, 2 uscite di 0,00199800 BTC ciascuna)
- Diagramma di flusso**: mempool.space mostra visivamente il mix di ingressi e uscite
- Caratteristiche** : La transazione può essere identificata come SegWit, Taproot, RBF, ecc.



Poiché tutte le uscite principali hanno la stessa quantità, è **impossibile determinare quale appartiene a chi**. Questo è il principio fondamentale del CoinJoin: l'indistinguibilità delle uscite.



**Esempio di transazione firmata** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Nota bene**: Se i vostri UTXO erano più grandi della denominazione del pool, avrete delle uscite in valuta estera (eccedenze). Questi UTXO in valuta rimangono tracciabili e devono essere gestiti separatamente dalle uscite anonime. Non combinateli mai con le vostre uscite miste.



## Pacchetti di qualità e anonimato CoinJoin



L'efficienza di un CoinJoin si misura in base alla sua **anonset**: il numero di uscite di valore identico prodotte dalla transazione. Più alto è questo numero, più è difficile determinare quale input corrisponde a quale output.



Joinstr genera attualmente pool di **2-5 partecipanti** in media. Queste cifre sono inferiori rispetto ai tradizionali coordinatori centralizzati come Wasabi (50-100 partecipanti) o Whirlpool (5-10 partecipanti), ma questo è il prezzo della decentralizzazione.



💡 **Per comprendere gli insiemi di anonimi e il loro calcolo in dettaglio**, consultare il nostro corso completo: [Insiemi di anonimi](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. altri CoinJoin




| Aspetto | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Partecipanti per pool** | 50-100 | 5-10 | Variabile (P2P) | **2-5** |
| **Coordinatore** | Centralizzato (chiuso 2024) | Centralizzato (attivo) | P2P maker/taker | **Nessuno (Nostr)** |
| **Resistenza alla censura** | Debole | Media | Molto alta | **Molto alta** |
| **Commissioni di coordinamento** | Percentuale | Commissione di ingresso | Pagato ai creatori | **Nessuno** |
| **Discriminazione UTXO** | Sì (liste nere) | No | No | **No** |

💡 **Altre soluzioni attive CoinJoin** :




- Ashigaru**: Implementazione open-source del protocollo Whirlpool con coordinatore centralizzato ma distribuibile in modo decentralizzato. Continua a funzionare dopo il sequestro di Samourai Wallet nel 2024.
- JoinMarket**: Soluzione P2P decentralizzata senza coordinatore centrale, basata su un modello di business maker/taker in cui i "maker" forniscono liquidità e sono remunerati dai "taker".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Il compromesso fondamentale**: Joinstr e JoinMarket sono le uniche due soluzioni senza un coordinatore centrale. JoinMarket utilizza un modello di business P2P con incentivi finanziari, mentre Joinstr utilizza Nostr per un coordinamento senza costi. Joinstr sacrifica l'anonimato immediato su larga scala a favore della semplicità (nessuna gestione di maker/taker) e della totale assenza di costi di coordinamento.



**Raccomandazione pratica**: Per compensare i pool più piccoli, eseguite più turni successivi di CoinJoin con partecipanti diversi. Distanziate i turni e cambiate le staffette Nostr tra un turno e l'altro per massimizzare la riservatezza.



Per ulteriori informazioni su questo argomento, consultate il nostro corso completo sulla privacy dei bitcoin:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Vantaggi e limiti



### Punti salienti



**Privacy migliorata**: La combinazione tra la crittografia delle comunicazioni Nostr, la VPN condivisa tra i partecipanti e l'uso consigliato di Tor crea una protezione a più livelli difficile da aggirare.



**Trasparente, costi minimi**: Nessun costo di coordinamento, solo i costi di mining sono condivisi equamente tra i partecipanti. Nessuna percentuale prelevata da nessun operatore.



### Vincoli da considerare





- Liquidità variabile**: Pool più piccoli, possono aspettare che i partecipanti si riuniscano
- Progetto in corso**: Applicazione in beta, possibili bug. Testate prima con piccole quantità di segnalibri
- Attacchi sibillini**: Possibilità che un avversario controlli diversi partecipanti alla piscina



## Le migliori pratiche



**Isolamento del UTXO**: Non combinare mai un UTXO miscelato con uno non miscelato. Utilizzare una cartella separata per i risultati anonimizzati.



**È indispensabile fare più turni**: Eseguire un minimo di 3 round successivi con partecipanti diversi. Variare quantità e tempi per evitare schemi. Distanziare i turni di diverse ore l'uno dall'altro.



**Protezione della rete**: Utilizzare sistematicamente Tor in aggiunta alla VPN integrata. Generare chiavi Nostr effimere per ogni sessione importante.



**Progresso cauto**: Iniziare a creare segnalibri con piccole quantità.



## Conclusione



Joinstr rappresenta una soluzione di privacy Bitcoin veramente decentralizzata. Utilizzando Nostr per il coordinamento, elimina la dipendenza da coordinatori centrali, preservando la sovranità degli utenti.



**Per gli utenti che apprezzano la resistenza alla censura e sono disposti a eseguire diversi cicli di CoinJoin per compensare le piscine più piccole.



In un contesto di crescente controllo finanziario, gli strumenti decentralizzati per proteggere la privacy stanno diventando essenziali.



## Risorse



### Documentazione ufficiale




- [Sito ufficiale di Joinstr](https://joinstr.xyz)
- [Documentazione per l'utente](https://docs.joinstr.xyz/users/using-joinstr)
- [Documentazione tecnica](https://docs.joinstr.xyz/overview/how-does-it-work)
- [Codice sorgente GitLab](https://gitlab.com/invincible-privacy/joinstr)
- [Applicazione Android](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Tutorial




- [Tutorial del plugin Electrum](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Guida completa di Uncensored Tech



### Comunità e supporto




- [Gruppo Telegram Joinstr](https://t.me/joinstr) - Supporto alla comunità e angoli per i segnalibri
- [Discussione tecnica su DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Strumenti aggiuntivi




- [Bookmark Faucet](https://signetfaucet.com) - Bitcoin di prova gratuiti
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Alternativa Faucet
- [Mempool.space](https://mempool.space) - Block explorer con analisi della privacy
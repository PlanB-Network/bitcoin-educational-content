---
name: Ombrello
description: Scoprire e installare Umbrel - Il vostro nodo Bitcoin e il vostro server domestico
---

![cover](assets/cover.webp)



## Introduzione



### Che cos'è un nodo Bitcoin?



Un nodo Bitcoin è un computer che partecipa alla rete Bitcoin eseguendo il software Bitcoin Core o un client alternativo. Il suo ruolo è essenziale per il funzionamento e la sicurezza della rete:





- Archiviazione Blockchain**: Mantiene una copia completa e aggiornata del Blockchain Bitcoin
- Verifica delle transazioni**: convalida ogni transazione e blocco in base alle regole del protocollo
- Diffusione delle informazioni**: Condivide le nuove transazioni e i blocchi con gli altri nodi
- Creazione del consenso**: Contribuisce all'applicazione delle regole della rete



Gestire il proprio nodo Bitcoin è un passo fondamentale verso la sovranità finanziaria, che offre diversi vantaggi chiave:





- Riservatezza**: Condividete le vostre transazioni senza rivelare le vostre informazioni a terzi
- Resistenza alla censura**: Nessuno può impedirvi di usare il Bitcoin
- Verifica indipendente**: Non è necessario fidarsi dei nodi altrui per verificare le transazioni
- Creazione del consenso**: Contribuire all'applicazione delle regole della rete Bitcoin
- Supporto alla rete**: Diventare un partecipante attivo nella distribuzione e nel decentramento della rete



### Umbrel: Una soluzione semplice per gestire un nodo Bitcoin



Umbrel è un sistema operativo open source che semplifica l'installazione e la gestione di un nodo Bitcoin. Inoltre, trasforma il vostro computer in un server domestico personale e privato, rendendo facile ospitare :





- Un nodo Bitcoin completo
- Applicazioni essenziali Bitcoin (Electrs, Mempool.space)
- Altri servizi personali (cloud storage, streaming, VPN, ecc.)



Con il suo elegante e intuitivo Interface utente, Umbrel rende i servizi self-hosted accessibili a tutti, mantenendo il controllo totale sui vostri dati.



## Opzioni di installazione dell'ombrello



Umbrel offre due modi principali per utilizzare la propria soluzione: un'opzione chiavi in mano (Umbrel Home) e una versione open source gratuita (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: la soluzione chiavi in mano



Umbrel Home è un server domestico preconfigurato, appositamente progettato per un'esperienza ottimale. Questa soluzione hardware all-in-one comprende:



**Caratteristiche hardware**




- Processore ad alte prestazioni ottimizzato per il self-hosting
- Storage SSD ad alta velocità preinstallato
- Sistema di raffreddamento silenzioso
- Design compatto ed elegante
- Porte USB ed Ethernet integrate



**Benefici esclusivi**




- Installazione plug-and-play: collegare e partire
- Supporto premium con assistenza dedicata
- Aggiornamenti automatici garantiti
- Procedura guidata di migrazione integrata
- Garanzia hardware completa
- Supporto completo per tutte le funzionalità



**Prezzo**: 399 € (il prezzo può variare a seconda della stagione)



### UmbrelOS: la versione open source



UmbrelOS è la versione gratuita e open source del sistema operativo Umbrel. Questa soluzione flessibile consente di utilizzare il proprio hardware e di beneficiare delle funzionalità essenziali di Umbrel.



**Benefici**




- Totalmente gratuito
- Codice sorgente aperto e verificabile
- Libertà di scelta
- Opzioni di personalizzazione avanzate



**Piattaforme supportate**




- Raspberry Pi 5: una soluzione popolare e conveniente
- Sistemi X86: Per PC o server standard
- Macchina virtuale: Per i test o l'utilizzo su un'infrastruttura esistente



**Limitazioni




- Solo il supporto della comunità
- Alcune funzioni avanzate riservate a Umbrel Home
- Configurazione iniziale più tecnica
- Le prestazioni dipendono dall'hardware selezionato



Questa versione è ideale per :




- Utenti tecnici
- Chi possiede già un'apparecchiatura compatibile
- Persone che vogliono imparare e sperimentare
- Sviluppatori che desiderano contribuire al progetto



Link ufficiali per l'installazione :




- [Installazione su Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Installazione su sistemi x86 (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Installazione macchina virtuale](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



In questa guida ci concentreremo sull'installazione di UmbrelOS su un Raspberry Pi 5, ma i principi di base rimangono simili per altre piattaforme.



## Installazione di Umbrel OS su Raspberry Pi 5



### Componenti necessari



Per questa installazione è necessario :





- Raspberry Pi 5 (4 GB o 8 GB di RAM)
- Un alimentatore ufficiale di Raspberry Pi Supply (fondamentale per la stabilità!)
- Scheda MicroSD (minimo 32 GB)
- Un lettore di schede microSD
- Un'unità SSD esterna per l'archiviazione dei dati
- Cavo Ethernet
- Un cavo USB per collegare l'unità SSD



### Fasi di installazione



**Scarica UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Visita il [sito ufficiale](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Scaricare l'ultima versione di UmbrelOS per Raspberry Pi 5



**Installazione di *Balena Etcher



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Scaricate e installate [Balena Etcher](https://www.balena.io/etcher/) sul vostro computer



**Preparazione della scheda microSD**



![Insertion carte microSD](assets/fr/03.webp)




- Inserire la scheda microSD nel lettore di schede del computer



**Immagine lampeggiante**



![Flashage UmbrelOS](assets/fr/04.webp)




- Lancio dell'incisore Balena
- Selezionare l'immagine UmbrelOS scaricata
- Scegliere la scheda microSD come destinazione
- Fare clic su "Flash!" e attendere il completamento del processo
- Espulsione sicura della scheda



**Installazione della scheda microSD



![Installation microSD](assets/fr/05.webp)




- Inserire la scheda microSD nel Raspberry Pi 5



**Collegamento periferico**



![Connexion périphériques](assets/fr/06.webp)




- Collegare l'unità SSD esterna a una porta USB disponibile
- Collegare il cavo Ethernet tra il Pi e il router



**Accensione



![Démarrage du Pi](assets/fr/07.webp)




- Collegare l'alimentazione ufficiale di Raspberry Pi Supply
- Attendere qualche minuto per l'avvio del sistema



**Primo accesso**



![Accès interface web](assets/fr/08.webp)




- Su un dispositivo connesso alla stessa rete, aprire il browser
- Accedere al sito web Interface di Umbrel all'indirizzo: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Se `umbrel.local` non funziona, è necessario trovare l'IP Address del Raspberry Pi sulla rete locale. È possibile:




- Consultare il manuale Interface del router
- Utilizzare uno scanner di rete come nmap
- Utilizzate il comando `arp -a` nel terminale del vostro computer



## Primo passo su Umbrel



Una volta che Umbrel è stato avviato ed è accessibile tramite il browser, seguite i seguenti passaggi per iniziare:



### Configurazione iniziale



**Crea il tuo account**



![Création compte](assets/fr/10.webp)




- Scegliere un nome utente
- Impostare una password sicura
- Per accedere a Umbrel sono necessarie le seguenti credenziali



**Conferma dell'account



![Confirmation compte](assets/fr/11.webp)




- Fare clic su "Avanti" per accedere al cruscotto



**Scoperta del Interface**



![Interface Umbrel](assets/fr/12.webp)




- Accedere all'App Store Umbrel
- Scoprite le numerose applicazioni disponibili
- Iniziamo installando le applicazioni essenziali per il Bitcoin



### Installazione delle applicazioni Bitcoin



**Nodo Bitcoin**



![Bitcoin Node](assets/fr/13.webp)




- Prima applicazione da installare
- Scaricare e controllare l'intero Blockchain Bitcoin



**Elettori**



![Installation Electrs](assets/fr/14.webp)




- Server Electrum per la connessione dei portafogli Bitcoin
- Si sincronizza con il vostro nodo Bitcoin



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Display Interface per Blockchain
- Traccia le transazioni e i blocchi in tempo reale



## Tracciamento di una transazione con Mempool.space



Mempool.space è un esploratore Blockchain open-source che fornisce una visualizzazione in tempo reale della rete Bitcoin. Permette di seguire le transazioni e di capire come si propagano sulla rete.



### Comprendere Mempool e conferme



Il "Mempool" (pool di memoria) è come una sala d'attesa virtuale dove tutte le transazioni Bitcoin non confermate vengono memorizzate prima di essere incluse in un blocco. Ecco come viene elaborata una transazione:



1. **Trasmissione**: Quando si invia una transazione, questa viene prima trasmessa sulla rete Bitcoin


2. **In attesa nel Mempool**: In attesa di essere selezionato da un Miner sulla base dei costi


3. **Prima conferma**: Un minore lo include in un blocco (1a conferma)


4. **Conferme aggiuntive**: Ogni nuovo blocco estratto dopo quello contenente la transazione aggiunge una conferma



Il numero di conferme consigliato dipende dalla quantità :




- Per piccole quantità: 1-2 conferme possono essere sufficienti
- Per importi elevati: 6 conferme sono generalmente considerate molto sicure



### Esplorare Interface da Mempool.space



1. **La pagina iniziale** fornisce una panoramica della rete Bitcoin:




   - Blocchi estratti di recente
   - Stime dei costi per le diverse priorità
   - Lo stato attuale del Mempool



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Cercare una transazione**: Per rintracciare una transazione specifica, incollare il suo identificativo (txid) nella barra di ricerca in cima alla pagina.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analizzare i dettagli della transazione



Una volta trovata la transazione, Mempool.space vi presenta un'analisi completa:



1. **Informazioni essenziali** :




   - Stato (confermato o meno)
   - Spese pagate (in Sats/vB)
   - Tempo di conferma stimato



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Struttura di transazione** :




   - Rappresentazione visiva di ingressi e uscite
   - Elenco dettagliato degli indirizzi coinvolti
   - Importi trasferiti



3. **Dati tecnici** :




   - Peso della transazione
   - Dimensione virtuale
   - Formato e versione utilizzata
   - Altri metadati specifici



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Vantaggi dell'utilizzo di Mempool.space su Umbrel



1. **Confidenzialità**: Le richieste passano attraverso il proprio nodo


2. **Indipendenza**: Non è necessario affidarsi a un servizio di terze parti


3. **Affidabilità**: Accesso ai dati anche quando i browser pubblici sono inattivi



Con questa applicazione è possibile monitorare in modo efficiente le transazioni, capire come le commissioni incidono sulla velocità di conferma e comprendere meglio il funzionamento della rete Bitcoin.



## Collegamento di un Wallet Bitcoin al nodo



### Configurazione degli elettrotecnici



**Collegamento locale



![Connexion locale](assets/fr/18.webp)




- Da utilizzare sulla rete locale
- Più veloce e più facile da configurare



**Connessione remota via Tor**



![Connexion Tor](assets/fr/19.webp)




- Per accedere al nodo da qualsiasi luogo
- Più sicuro e privato



### Collegamento con Sparrow Wallet



**Accesso ai parametri



![Paramètres Sparrow](assets/fr/20.webp)




- Passero aperto Wallet
- Andare in Preferenze > Server
- Cliccate su "Modifica connessione esistente"



**Scelta del tipo di connessione



Sparrow offre tre modalità di connessione:



***Server pubblico***




- Connessione a server pubblici (ad es. blockstream.info, Mempool.space)
- Semplice ma meno privato



***Bitcoin Core***




- Collegamento diretto a un nodo Bitcoin
- Privato ma più lento



***Elettro privato***




- Collegarsi al server Electrs
- Combina riservatezza e prestazioni



**Configurazione degli eletti



Scegliete il tipo di connessione utilizzando le informazioni visualizzate nell'applicazione Electrs che abbiamo visto in precedenza:



In entrambi i casi, lasciare deselezionate le opzioni "Usa SSL" e "Usa proxy".



**Collegamento locale


Host: umbrel.local


Numero di porta: 50001



**Connessione remota (Tor)**


Host : [tuo-Address-onion]


Numero di porta: 50001



La connessione Tor è necessaria se si vuole accedere al nodo al di fuori della rete locale.



![Configuration connexion](assets/fr/21.webp)


Per ulteriori informazioni sul software Sparrow Wallet, abbiamo un tutorial completo:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Conclusione



Il vostro Umbrel è ora pronto all'uso. Partecipate attivamente alla rete Bitcoin mantenendo il pieno controllo dei vostri dati. Sentitevi liberi di esplorare le molte altre applicazioni disponibili nell'App Store di Umbrel per estendere le capacità del vostro server domestico.



## Risorse utili



### Documentazione ufficiale




- [Sito ufficiale Umbrel](https://umbrel.com)
- [Documentazione Umbrel](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Applicazioni Bitcoin




- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Elettori](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Passero Wallet](https://sparrowwallet.com)



### Comunità




- [Forum Umbrel](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)
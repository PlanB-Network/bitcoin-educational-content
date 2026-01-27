---
name: Heritage
description: Un portafoglio Bitcoin con meccanismo di ereditarietà integrato tramite script Taproot
---

![cover](assets/cover.webp)



La trasmissione dei bitcoin in caso di morte o di incapacità rappresenta una sfida importante per i possessori di criptovalute. Senza un adeguato piano di successione, questi beni diventano irrecuperabili per i propri cari.



Heritage fornisce una risposta elegante implementando un meccanismo di commutazione a uomo morto direttamente sulla blockchain Bitcoin. Questo wallet open-source consente di configurare le condizioni di successione del on-chain: se il proprietario non effettua altre transazioni per un periodo definito, le chiavi alternative predesignate possono rilasciare i fondi.



## Che cos'è il patrimonio?



Heritage è un portafoglio Bitcoin che integra in modo nativo un meccanismo di ereditarietà tramite script Taproot. Sviluppato sotto licenza MIT da Jérémie Rodon, questo software open-source garantisce trasparenza e durata.



Heritage utilizza scritture Taproot codificate in indirizzi Bitcoin. Ogni UTXO integra due tipi di condizioni di spesa:





- Percorso primario** : Il proprietario può spendere i suoi bitcoin in qualsiasi momento con la sua chiave primaria
- Percorsi alternativi**: Per ogni erede designato, uno script combina la sua chiave pubblica con un timelock



Ogni transazione del proprietario posticipa automaticamente la data di attivazione delle clausole di successione. In caso di inattività prolungata (morte, incapacità), le condizioni si attivano automaticamente.



## Servizio del patrimonio (facoltativo)



Heritage offre due opzioni di utilizzo:



**Fai da te (gratis)**: La sola applicazione open-source. Si gestisce tutto autonomamente con il proprio nodo. Questa opzione offre accesso integrato al backup, eredità integrata e controllo esclusivo dei vostri bitcoin. Tuttavia, è necessario creare i propri avvisi (calendario, promemoria) per non dimenticare di rinnovare i timelock e non ci sono notifiche automatiche per gli eredi.



**Utilizzare il servizio (0,05% all'anno)** : Il servizio btc-heritage.com aggiunge funzioni per semplificare la gestione:




- Promemoria automatici prima della scadenza delle scadenze
- Notifiche automatiche agli eredi per guidarli nel processo di recupero
- Assistenza prioritaria
- Gestione semplificata dei descrittori



Commissione: 0,05% dell'importo gestito all'anno, minimo 0,5 mBTC/anno. Primo anno gratuito.



Il servizio rimane non custodiale: le chiavi private non lasciano mai il vostro dispositivo. Heritage non può accedere ai vostri fondi.



## Patrimonio CLI



Per gli utenti avanzati che preferiscono il terminale, Heritage offre uno strumento a riga di comando (CLI) per un controllo granulare e per il funzionamento della macchina con il sistema air-gapped.



![Page Heritage CLI](assets/fr/03.webp)



La documentazione completa sul CLI è disponibile all'indirizzo [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Qui troverete le istruzioni per il download, la connessione al servizio, la creazione di portafogli (con chiavi Ledger o locali), la gestione degli eredi e delle transazioni.



Questa esercitazione si concentra sull'applicazione Desktop, più accessibile alla maggior parte degli utenti.



## Desktop del patrimonio



Heritage Desktop è un'applicazione grafica con un'interfaccia intuitiva che guida l'utente in ogni fase del processo di configurazione.



### Scaricare



Andate su [btc-heritage.com](https://btc-heritage.com) e cliccate su "Download application".



![Page d'accueil Heritage](assets/fr/01.webp)



Scegliete la versione corrispondente al vostro sistema operativo (Linux 64bits o Windows 64bits). I binari non sono firmati digitalmente, il che potrebbe causare avvisi di sicurezza.



![Page de téléchargement](assets/fr/02.webp)



### Installazione su Linux



Su Linux, l'applicazione è distribuita in formato AppImage. Prima di poterla eseguire, è necessario installare la dipendenza `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Quindi rendere il file eseguibile ed eseguirlo:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Primo lancio



Al primo avvio, la procedura guidata di onboarding offre tre scelte:



![Onboarding initial](assets/fr/05.webp)





- Impostare un Wallet del patrimonio culturale**: Creare un nuovo wallet con piano del patrimonio
- Ereditare bitcoin**: Recuperare bitcoin come erede
- Esplorare da solo**: Esplorare le funzioni senza assistenza



Selezionare "Setup an Heritage Wallet" per creare il primo wallet.



### Connessione di rete Bitcoin



Scegliere la modalità di connessione alla rete Bitcoin:



![Choix connexion](assets/fr/06.webp)





- Utilizzare il Servizio Patrimonio**: Infrastruttura gestita, più semplice per gli eredi
- Utilizzo del mio nodo**: Collegarsi al proprio nodo Bitcoin Core o Electrum



Per questa esercitazione, utilizzeremo il nostro nodo.



### Gestione delle chiavi private



Selezionare la modalità di gestione delle chiavi private:



![Gestion des clés](assets/fr/07.webp)





- Con un dispositivo hardware Ledger** : Massima sicurezza con hardware wallet (consigliato)
- Archiviazione locale con password**: Chiavi memorizzate localmente con protezione tramite password
- Ripristino di un wallet esistente** : Ripristino da un seed esistente



### Configurazione del nodo



Se si utilizza il proprio nodo, l'applicazione guida l'utente nella configurazione. Assicurarsi che il nodo Bitcoin o Electrum sia :




- Installato e funzionante
- Sincronizzato con la rete Bitcoin
- Configurato per accettare connessioni RPC (per Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Fare clic su "Il mio nodo Bitcoin è attivo e funzionante" quando il nodo è pronto.



### Pannello di stato



Fare clic su "Stato" nell'angolo in alto a destra, quindi su "Apri configurazione" per accedere ai parametri di connessione.



![Panneau Status](assets/fr/09.webp)



Impostare l'URL del server Electrum (ad esempio, `umbrel.local:50001` se si utilizza Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Creazione del wallet



Una volta stabilita la connessione, fare clic su "Crea Wallet" nella scheda WALLETS.



![Créer wallet](assets/fr/11.webp)



Un popup spiega l'architettura divisa di Heritage :



![Architecture split](assets/fr/12.webp)



1. **Fornitore di chiavi (offline)**: Gestisce le chiavi private e firma le transazioni. Può essere un software Ledger o wallet.


2. **Wallet online**: Gestisce la sincronizzazione con la rete Bitcoin, la creazione di indirizzi e la trasmissione di transazioni.



Compilare il modulo di creazione:



![Formulaire création wallet](assets/fr/13.webp)





- Nome Wallet**: Un nome unico per identificare il wallet
- Provider di chiavi**: Per questa esercitazione, scegliere l'archiviazione locale delle chiavi
- Nuovo/Ripristino**: Selezionare "Nuovo" per creare un nuovo seed
- Conteggio parole**: 24 parole consigliate per la massima sicurezza



Inserire una password forte e scegliere le opzioni per il Wallet online:



![Options Online Wallet](assets/fr/14.webp)





- Nodo locale**: Utilizza il proprio nodo Electrum o Bitcoin Core
- Servizio Heritage**: Utilizza il servizio Heritage (consigliato per le funzioni di notifica)



Fare clic su "Crea Wallet" per finalizzare la creazione.



### Interface da wallet



Il wallet è stato creato. L'interfaccia visualizza :



![Interface wallet](assets/fr/15.webp)





- Equilibrio
- Pulsanti di invio e ricezione
- Storia delle transazioni
- Storia della configurazione del patrimonio
- Indirizzi wallet



### Creazione di eredi



Andare alla scheda "EROI" per creare gli eredi.



![Page Heirs](assets/fr/16.webp)



Il popup informativo spiega:




- Gli eredi sono chiavi pubbliche Bitcoin associate a singoli individui
- Ogni erede ha una propria frase mnemonica
- Il primo erede dovrebbe essere un "backup" per voi stessi (in caso di perdita del vostro wallet principale)



#### Creazione dell'erede di backup



Fare clic su "Crea erede" e denominarlo "Backup".



![Création héritier Backup](assets/fr/17.webp)



Il popup spiega perché una frase di 12 parole senza passphrase è sicura per gli eredi:


1. **Nessun accesso immediato**: Le chiavi degli eredi non possono accedere ai fondi fino alla scadenza del blocco temporale


2. **Rilevamento delle compromissioni**: Se qualcuno accede alla frase, è possibile aggiornare la configurazione del Patrimonio


3. **Accessibilità a lungo termine**: Un passphrase potrebbe essere dimenticato dopo molti anni



Configurare l'erede :



![Configuration héritier](assets/fr/18.webp)





- Fornitore di chiavi** : Memorizzazione della chiave locale
- Nuovo**: Generare un nuovo seed
- Conteggio parole**: 12 parole



Finalizzare la creazione :



![Finalisation héritier](assets/fr/19.webp)





- Tipo di erede**: Chiave pubblica estesa
- Esportazione al servizio**: Opzionale, consente la notifica automatica agli eredi



L'erede di backup è stato creato:



![Héritier créé](assets/fr/20.webp)



#### Salvataggio della frase mnemonica dell'erede



Fare clic sull'erede di Backup e poi su "Mostra Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**IMPORTANTE: annotate queste 12 parole e conservatele in un luogo sicuro. Questa è la chiave per recuperare i fondi.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Rimozione del seed dall'applicazione



Una volta scritta la frase, accedere ai parametri dell'erede (icona della ruota dentata):



![Paramètres héritier](assets/fr/23.webp)



Utilizzare "Strip Heir Seed" per rimuovere la chiave privata dall'applicazione. Confermare il salvataggio della frase.



![Strip Heir Seed](assets/fr/24.webp)



Si tratta di una misura di sicurezza: solo la chiave pubblica rimane nell'applicazione, sufficiente per configurare l'ereditarietà.



#### Creazione di un secondo erede



Ripetere la procedura per creare un secondo erede (ad esempio, "Satoshi"). A questo punto si avranno due eredi:



![Deux héritiers](assets/fr/25.webp)





- Backup**: La chiave di emergenza personale
- Satoshi**: Un erede designato



### Configurazione del patrimonio



Tornare al wallet e fare clic sull'icona Impostazioni:



![Paramètres wallet](assets/fr/26.webp)



Nella sezione "Configurazione del patrimonio", fare clic su "Crea":



![Heritage Configuration](assets/fr/27.webp)



Stabilite dei limiti di tempo per ogni erede:



![Configuration délais](assets/fr/28.webp)





- Backup**: 180 giorni (6 mesi) - Data di scadenza: 2026-06-18
- Satoshi**: 455 giorni (15 mesi) - Data di scadenza: 2027-03-20



**Importante**: Ogni erede deve avere un ritardo maggiore rispetto al precedente. Il primo erede (Backup) avrà accesso ai fondi per primo.



Configurare anche :



![Configuration finale](assets/fr/29.webp)





- Data di riferimento**: Data di inizio per il calcolo dei tempi di consegna
- Ritardo minimo di maturazione**: Ritardo minimo dopo una transazione (si consigliano 10 giorni)



Fare clic su "Crea" per convalidare la configurazione.



La configurazione del patrimonio è ora attiva:



![Configuration active](assets/fr/30.webp)



Visualizza entrambi gli eredi con le rispettive scadenze e date di scadenza.



### Salvataggio dei descrittori



**Importante**: Conservare i descrittori wallet. Senza di essi, anche con la frase mnemonica, il recupero dei fondi è impossibile.



Fare clic su "Descrittori di backup" :



![Bouton Backup](assets/fr/31.webp)



Salvare il file JSON contenente i descrittori Bitcoin:



![Backup descripteurs](assets/fr/32.webp)



Questo file deve essere trasmesso agli eredi, insieme alle rispettive frasi mnemoniche.



### Ricevere bitcoin



Fare clic su "RICEVIMENTO" per generate un indirizzo di ricezione:



![Recevoir bitcoins](assets/fr/33.webp)



Congratulazioni! Il vostro Heritage Wallet è pronto a ricevere bitcoin. Ogni indirizzo generato incorpora automaticamente le condizioni di Heritage.



Dopo aver ricevuto una transazione, il saldo viene aggiornato:



![Solde mis à jour](assets/fr/34.webp)



La cronologia visualizza la transazione e la configurazione del patrimonio associata.



---

## Recupero da parte di un erede



Una volta trascorso il tempo stabilito, l'erede può reclamare i fondi.



### Prerequisiti



L'erede ha bisogno di :


1. La sua frase mnemonica di 12 parole


2. Il file di backup del descrittore wallet originale (JSON)



### Creazione di un erede Wallet



Nella scheda "Eredità", un popup ricorda questi prerequisiti:



![Page Heir Wallets](assets/fr/35.webp)



**Nota bene**: Senza il file di backup del descrittore, l'accesso ai fondi è IMPOSSIBILE, anche con la frase mnemonica corretta.



Cliccare su "Crea erede Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Compilare il modulo:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Nome dell'erede Wallet**: Un nome per identificare questo erede wallet
- Fornitore di chiavi** : Memorizzazione della chiave locale
- Ripristina**: Selezionare questa opzione per inserire una frase esistente



Inserire le 12 parole della frase mnemonica dell'erede e configurare il Provider Heritage:



![Entrée mnemonic](assets/fr/38.webp)





- Provider del patrimonio**: "Locale" per utilizzare il proprio nodo con il file di backup



Caricare il file di backup JSON e fare clic su "Crea erede Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Erede Wallet



Viene creato l'Erede Wallet . Inizialmente, se il blocco temporale non è ancora scaduto, non è disponibile alcuna eredità:



![Pas d'héritage disponible](assets/fr/40.webp)



Una volta trascorso il ritardo e sincronizzati con la rete Bitcoin, i fondi appaiono nell'elenco delle eredità:



![Héritage disponible](assets/fr/41.webp)



L'interfaccia visualizza :




- Tipo di chiave e impronta digitale
- Totale fondi ereditari
- Importo spendibile attuale (0 sat se il timelock non è ancora scaduto)
- Scadenze e date di scadenza



Al raggiungimento della data di scadenza, il pulsante "Spend" trasferisce i bitcoin su un wallet personale.



---

## Le migliori pratiche



### Salvataggio dei descrittori



I descrittori wallet sono essenziali per ricostruire gli indirizzi del vostro Patrimonio. **Senza i descrittori, anche con la vostra frase mnemonica, non sarete in grado di trovare i vostri fondi.



### Sicurezza delle chiavi





- Utilizzare un Ledger per la chiave principale, se possibile
- Non conservate mai le sentenze degli eredi nello stesso luogo in cui sono conservate le vostre
- Diffondere le informazioni su più media e in più luoghi



### Documentazione per i vostri cari



Scrivete istruzioni chiare che spieghino ogni fase del processo di recupero. I vostri eredi potrebbero non avere familiarità con il Bitcoin nel momento critico.



## Alternative



Esistono altre soluzioni per gestire la trasmissione dei bitcoin, tra cui Liana e Bitcoin Keeper. Troverete i nostri tutorial qui sotto:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Conclusione



Heritage consente di pianificare la successione del Bitcoin in modo sovrano attraverso l'applicazione Desktop. L'implementazione richiede un'attenta considerazione dei tempi appropriati e della protezione dei segreti. Non dimenticate di passare il testimone ai vostri eredi:




- La loro frase mnemonica di 12 parole
- Il file di backup del descrittore
- Istruzioni per il recupero



## Risorse





- [Sito ufficiale del patrimonio](https://btc-heritage.com)
- [Documentazione CLI](https://btc-heritage.com/heritage-cli)
- [Patrimonio GitHub CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)
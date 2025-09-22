---
name: Blockstream App - Desktop
description: Come utilizzare il Hardware Wallet con l'applicazione Blockstream su un computer?
---
![cover](assets/cover.webp)



## 1. Introduzione



### 1.1 Obiettivo del tutorial





- Questa esercitazione spiega come utilizzare l'applicazione **Blockstream** su un computer per gestire un Bitcoin **onchain** Wallet con un **Hardware Wallet**, consentendo transazioni sicure registrate sul Blockchain Bitcoin principale.
- Copre l'installazione, la configurazione iniziale, la connessione di un Hardware Wallet e la ricezione e l'invio di bitcoin onchain.
- Nota: altre esercitazioni nelle appendici riguardano Liquid, Watch-Only e l'applicazione mobile.



### 1.2 Pubblico di riferimento





- **Principianti**: Utenti che desiderano gestire i propri bitcoin con un software desktop sicuro e un Hardware Wallet.
- **Utenti intermedi**: Persone che vogliono capire come utilizzare un Hardware Wallet per le transazioni onchain e le opzioni di privacy come Tor o SPV.



### 1.3. Informazioni sui portafogli hardware





- **Hardware Wallet**, **Cold Wallet**: Un dispositivo fisico che memorizza le chiavi private offline, offrendo un elevato livello di sicurezza contro gli attacchi informatici, a differenza dei portafogli **Hot** (portafogli software su dispositivi connessi).
- **Uso consigliato**:
    - Ideale per garantire grandi importi o risparmi a lungo termine.
    - È adatto agli utenti attenti alla sicurezza che desiderano proteggere i propri fondi dai rischi associati ai dispositivi connessi.
- **Limitazioni**: Richiede un software come Blockstream App per visualizzare i saldi, gli indirizzi generate e trasmettere le transazioni con firma Hardware Wallet.



## 2. Presentazione dell'applicazione Blockstream





- **Blockstream App** è un'applicazione mobile (iOS, Android) e desktop per la gestione dei portafogli e degli asset Bitcoin sul Liquid Network. Acquisita da Blockstream nel 2016, si chiamava *GreenAddress*, è stata rinominata *Blockstream Green* (2019) e ora si chiama *Blockstream app* (2025).
- **Caratteristiche principali**:
- **Transazioni Onchain** su Blockchain Bitcoin.
    - Transazioni sulla rete **Liquid** (Sidechain per scambi veloci e riservati).
- **Portafogli di sola osservazione** per il monitoraggio dei fondi senza accesso alle chiavi.
    - Opzioni di privacy: connessione tramite **Tor**, connessione a un **nodo personale** tramite Electrum o verifica **SPV** per ridurre la dipendenza da nodi di terze parti.
    - Funzioni **Replace-by-fee (RBF)** per accelerare le transazioni non confermate.
- **Compatibilità**: Integra portafogli hardware come **Blockstream Jade**.
- **Interface**: Intuitivo per i principianti, con opzioni avanzate per gli esperti.
- **Nota**: Questa guida si concentra sull'uso di onchain con un Hardware Wallet sulla versione desktop. Le altre esercitazioni fornite come appendici riguardano l'uso su applicazioni mobili, per le funzioni onchain, Liquid e Watch-Only.



## 3. Installazione e configurazione di Blockstream App Desktop



### 3.1. scaricare





- Accedere al [sito ufficiale](https://blockstream.com/app/) e fare clic su "_Download Now_". Scaricare la versione corrispondente al proprio sistema operativo (Windows, macOS, Linux).
- **Nota**: Assicurarsi di scaricare dalla fonte ufficiale per evitare software fraudolento.



### 3.2. configurazione iniziale





- **Schermata iniziale**: Alla prima apertura, l'applicazione visualizza una schermata senza un Wallet configurato. I portafogli creati o importati appariranno qui in seguito.



![image](assets/fr/02.webp)





- **Personalizzazione delle impostazioni**: Fare clic sull'icona delle impostazioni in basso a sinistra, regolare le opzioni sottostanti, quindi uscire da Interface per continuare.



![image](assets/fr/03.webp)



#### 3.2.1. Parametri generali





- Nel menu Impostazioni, fare clic su "**Generale**".
- **Funzione**: Modificare la lingua del software e attivare funzioni sperimentali, se necessario.



![image](assets/fr/04.webp)



#### 3.2.2. Connessione via Tor





- Nel menu Impostazioni, fare clic su "**Rete**".
- **Funzione**: Instradare il traffico di rete tramite **Tor**, una rete anonima che cripta le connessioni.
- Perché? Nascondere il proprio IP Address e proteggere la propria privacy, ideale se non ci si fida della propria rete (Wi-Fi pubblico, ad esempio).
- **Svantaggi**: Può rallentare l'applicazione a causa della crittografia.
- **Raccomandazione**: Attivare Tor se la riservatezza è una priorità, ma verificare la velocità della connessione.



![image](assets/fr/05.webp)



#### 3.2.3. Connessione a un nodo personale





- Nel menu Impostazioni, fare clic su "**Server e convalida personalizzati**".
- **Funzione**: Collega l'applicazione al proprio **nodo Bitcoin completo** tramite un **server Electrum**.
- Perché? Fornisce un controllo totale sui dati Blockchain, eliminando la dipendenza dai server Blockstream.
- **Prerequisito**: Un nodo Bitcoin configurato.
- **Raccomandazione**: Utenti avanzati che desiderano la massima sovranità.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. Verifica dell'SPV





- Nel menu Impostazioni, fare clic su "**Server e convalida personalizzati**".
- **Funzione**: Utilizza la **verifica semplificata dei pagamenti (SPV)** che scarica le intestazioni dei blocchi e verifica le transazioni in base alla prova di inclusione (Merkle), senza memorizzare il Blockchain completo.
- Perché? Riduce la dipendenza dal nodo predefinito di Blockstream, pur rimanendo leggero per i dispositivi.
- **Svantaggi**: Meno sicuro di un Full node, poiché si basa su nodi di terze parti per alcune informazioni.
- **Raccomandazione**: Attivare SPV se non si può usare un nodo personale, ma si preferisce un Full node per una sicurezza ottimale.



![image](assets/fr/07.webp)



## 4. Collegamento di un Hardware Wallet all'app Blockstream



### 4.1. Considerazioni preliminari



#### 4.1.1. Per gli utenti del Ledger





- Il Blockstream Green supporta solo l'applicazione **Bitcoin Legacy** sui dispositivi Ledger (Nano S, Nano X).
- Passi da seguire in **Ledger Live** prima di collegare il dispositivo :


1. Accedere a **"Impostazioni "** → **"Funzioni sperimentali "** e attivare la **modalità sviluppatore**.


2. Accedere a **"Il mio Ledger"** → **"Catalogo applicazioni "**, quindi installare l'applicazione **Bitcoin Legacy**


3. Aprire l'applicazione **Bitcoin Legacy** sul Ledger prima di avviare il Blockstream Green per stabilire la connessione.




- **Nota**: Assicurarsi che il Ledger sia sbloccato con il codice PIN e che l'applicazione Bitcoin Legacy sia attiva al momento della connessione.



#### 4.1.2 Inizializzazione di un Hardware Wallet





- Se il Hardware Wallet (Ledger, Trezor o Blockstream Jade) non è mai stato utilizzato (né con il Blockstream Green, né con altri software come il Ledger Live), è necessario innanzitutto inizializzarlo. Questa fase comporta, in un ambiente sicuro, l'assenza di telecamere o osservatori:


1. **seed generazione di frasi / Mnemonic frase** (12, 18 o 24 parole): Scrivetela con cura su un foglio di carta.


2. **Verifica della frase seed**: Verifica dell'importazione del Wallet dalle parole annotate, ad esempio verificando la chiave pubblica estesa. Da eseguire prima dell'invio di fondi al Wallet e della messa in sicurezza permanente della frase seed.


3. **Protezione della frase seed**: Conservare la frase su un supporto fisico (carta o metallo) e in un luogo sicuro. Non conservatela mai in formato digitale (niente screenshot, cloud o e-mail).




- **Importante**: La frase seed è l'unico mezzo per recuperare i fondi in caso di smarrimento o malfunzionamento del dispositivo. Chiunque abbia accesso può rubare i vostri bitcoin.
- **Risorse** per il backup e il controllo della frase seed :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Configurazione per questa esercitazione :





- Supponiamo che il Hardware Wallet sia già stato inizializzato con una frase seed e un codice PIN di chiusura.
- Si presume che il Hardware Wallet non sia mai stato collegato a Blockstream App, il che richiede la creazione di un nuovo account. Se il Hardware Wallet è già stato utilizzato con Blockstream App, l'account apparirà automaticamente all'apertura dell'applicazione.



### 4.2. Avviare la connessione





- Dalla schermata iniziale, fare clic su "**Setup a New Wallet**", quindi convalidare i termini e le condizioni e fare clic su "**Get Started**":



![image](assets/fr/08.webp)





- Selezionare l'opzione "**Su Hardware Wallet**":



![image](assets/fr/09.webp)





- Se si utilizza un **Blockstream Jade**, fare clic sul pulsante corrispondente. Altrimenti, selezionare "**Collega un dispositivo hardware diverso**":



![image](assets/fr/10.webp)





- Collegare il Hardware Wallet al computer tramite USB e selezionarlo nell'applicazione Blockstream:



![image](assets/fr/22.webp)





- Attendere mentre Blockstream App importa le informazioni sul portafoglio:



![image](assets/fr/23.webp)



### 4.3. Creare un account





- Se il vostro Hardware Wallet è già stato utilizzato con Blockstream App, il vostro account apparirà automaticamente nel Interface dopo l'importazione. In caso contrario, creare un account facendo clic su "**Crea account**":



![image](assets/fr/24.webp)





- Scegliere "**Standard**" per configurare un portafoglio Bitcoin classico:



![image](assets/fr/25.webp)





- Una volta creato l'account, è possibile accedere al portafoglio Interface principale:



![image](assets/fr/26.webp)





## 5. Utilizzo del Wallet onchain con un Hardware Wallet



### 5.1. Ricevere bitcoin





- Dalla schermata principale del portafoglio, cliccare su "**Ricevi**" :



![image](assets/fr/27.webp)





- L'applicazione visualizza un Address di ricezione **vuoto**. L'utilizzo di un nuovo Address per ogni ricezione migliora la riservatezza. Fare clic su "**Copia Address**" per copiare il Address, oppure lasciare che il mittente scansioni il codice QR visualizzato:



![image](assets/fr/12.webp)



**Opzioni** :




- (1) Fare clic sulle frecce per creare un nuovo generate collegato al portafoglio.
- (2) Per richiedere un importo specifico, fare clic su "**Altre opzioni**" e poi su "**Richiesta importo**". Il QR verrà aggiornato e il Address verrà sostituito da un URI di pagamento Bitcoin come: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Per riutilizzare un Address precedente, cliccare su "**Altre opzioni**" e poi su "**Elenco degli indirizzi**" :



![image](assets/fr/14.webp)





- **Verifica**: Verificare attentamente il Address condiviso per evitare errori o attacchi (ad esempio, malware che modificano gli appunti).
- Una volta che la transazione è stata trasmessa in rete, apparirà nel vostro Wallet. Attendere da 1 a 6 conferme per considerare la transazione non modificabile.



![image](assets/fr/28.webp)



### 5.2. inviare bitcoin





- Dalla schermata principale del portafoglio, fare clic su "**Invio**".



![image](assets/fr/29.webp)





- Inserire i dettagli:
    - (1) Verificare che l'asset selezionato sia **Bitcoin** (onchain).
    - (2) Inserire il **Address del destinatario** incollandolo o scansionando un codice QR con la webcam.
    - (3) Indicare l'**importo** da inviare (in BTC, satoshi o altre unità).




![image](assets/fr/16.webp)





- Selezionare **tasse di transazione** (opzionale) :
 - Scegliete tra le opzioni proposte (veloce, media, lenta) in base all'urgenza, con un tempo di conferma stimato.
 - Per tariffe personalizzate, regolare manualmente il numero di satoshis per vbyte. Questi sono visualizzati nella schermata iniziale. Vedere anche [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **Selezione manuale degli UTXO** (opzionale): Fare clic su "**Selezione manuale Coin**" per scegliere gli UTXO specifici da utilizzare nella transazione.



![image](assets/fr/18.webp)





- **Verifica preliminare**: Controllare il Address, l'importo e le commissioni nella schermata di riepilogo, quindi fare clic su "**Conferma transazione**". In realtà, la transazione non sarà rilasciata alla rete fino a quando non sarà stata firmata con il proprio Hardware Wallet, che è l'unico a possedere le chiavi segrete associate agli indirizzi su cui verranno addebitati gli UTXO (satoshi).



![image](assets/fr/19.webp)





- **Controllo finale e firma**: Assicurarsi che tutti i parametri della transazione siano corretti **sulla schermata del Hardware Wallet**, quindi firmare la transazione utilizzando quest'ultimo. Un errore del Address può comportare una perdita irreversibile di fondi.





- **Trasmissione**: Una volta firmata, Blockstream App trasmette automaticamente la transazione sulla rete Bitcoin.



![image](assets/fr/20.webp)





- **Follow-up**:
 - La transazione viene visualizzata nella schermata iniziale di Wallet come "in attesa" fino alla conferma.
 - Finché la transazione non è stata confermata, è possibile utilizzare la funzione **Replace-by-fee (RBF)** per accelerare la conferma aumentando la tariffa (vedere Appendice).



![image](assets/fr/21.webp)



## Appendici



### A1. Altri tutorial Blockstream





- Utilizzo del Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Importazione e monitoraggio di un portafoglio in "Watch-Only" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Utilizzo dell'app Blockstream sui telefoni cellulari (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Spiegazione di Replace-by-fee (RBF)





- **Definizione**: Replace-by-fee (RBF) è una caratteristica della rete Bitcoin che consente al mittente di accelerare la conferma di una transazione **onchain** aumentando la tariffa.
- **Limiti**:
    - Il RBF non è disponibile per le transazioni Liquid o Lightning.
    - La transazione iniziale deve essere contrassegnata come compatibile con il RBF, cosa che Blockstream App fa automaticamente.
- Per maggiori informazioni, vedere [il nostro glossario](https://planb.network/resources/glossary/rbf-replacebyfee).



### A3. Le migliori pratiche





- **Proteggete la vostra frase di recupero**:
    - Conservare la frase Hardware Wallet e Mnemonic su un supporto fisico (carta, metallo) in un luogo sicuro.
    - Non conservatelo mai in formato digitale (cloud, e-mail, screenshot).
    - Esercitazione: salvare la frase Mnemonic :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Proteggere la privacy**:





    - generate un nuovo Address per ogni ricezione onchain.
    - Attivare **Tor** o **SPV** per limitare il tracciamento.
    - Collegatevi al vostro nodo Bitcoin tramite Electrum per ottenere la massima sovranità.
- **Controllare sempre gli indirizzi di spedizione**:





    - Controllare il Address sullo schermo del Hardware Wallet prima di firmare.
    - Utilizzare il copia/incolla o un codice QR per evitare errori manuali.
- **Ottimizzare i costi**:





    - Adattare le tariffe in base all'urgenza e alla congestione della rete (vedere [Mempool.space](https://Mempool.space/)).
    - Utilizzate Liquid o Lightning per transazioni veloci e a basso costo che non richiedono la sicurezza onchain.
- **Aggiornare il software**:





    - Mantenete l'App Blockstream e il firmware del Hardware Wallet aggiornati con le ultime funzioni e patch di sicurezza.



### A4. Risorse aggiuntive





- **Link ufficiali**:
    - [Sito ufficiale](https://blockstream.com/)
    - [Supporto per l'applicazione Blockstream](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): documentazione e chat
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Esploratori di blocchi**:
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Informazioni sul flusso di blocchi](https://blockstream.info/Liquid)
    - Fulmine : [1ML (Lightning Network)](https://1ml.com/)





- **Protezione della frase di recupero:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Glossario](https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Glossario](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
---
name: App Blockstream - Solo per guardare
description: Come si configura un Watch-only wallet su Blockstream App?
---

![cover](assets/cover.webp)


## 1. Introduzione


### 1.1 Obiettivo del tutorial





- Questa esercitazione spiega come impostare e utilizzare la funzione **Watch-Only** dell'applicazione mobile **Blockstream App** per monitorare un Bitcoin Wallet senza accedere alle sue chiavi private.
- L'articolo tratta dell'installazione, della configurazione iniziale, dell'importazione di una chiave pubblica estesa e del suo utilizzo per tenere traccia dei saldi e degli indirizzi di ricezione generate.
- Nota: altre esercitazioni, fornite in appendice, riguardano Onchain, Liquid e la versione desktop.



### 1.2. Pubblico di riferimento





- Principianti**: Utenti che desiderano monitorare un portafoglio Bitcoin (spesso associato a un Hardware Wallet) tramite un'applicazione mobile intuitiva.
- Utenti intermedi**: Persone che desiderano gestire portafogli di sola lettura utilizzando opzioni di privacy come Tor o SPV.
- Proprietari di Hardware Wallet**: Per controllare i propri saldi e gli indirizzi generate senza collegare il proprio dispositivo.
- Aziende e negozi** :
 - Tracciate le vostre transazioni a fini contabili senza esporre le vostre chiavi private.
 - Verificare le transazioni ricevute senza inserire le chiavi private nei sistemi di pagamento online.
 - Consentite ai dipendenti di generate nuovi indirizzi di ricezione senza avere accesso alle chiavi private.
- Organizzazioni e crowdfunding**: Mostrare il bilancio in modo trasparente ai donatori senza consentire l'accesso ai fondi.



### 1.3. Introduzione del Watch-Only



Un **Watch-Only** Wallet consente di monitorare le transazioni e il saldo di un Bitcoin Wallet senza avere accesso alle chiavi private. A differenza di un Wallet convenzionale, memorizza solo dati pubblici, come la **chiave pubblica estesa** (che ha dato origine a "**xpub**", poi "zpub", "ypub", ecc.), che gli consente di ottenere gli indirizzi dei destinatari e di tenere traccia della cronologia delle transazioni sul Blockchain Bitcoin. L'assenza di chiavi private rende impossibile erogare fondi dall'applicazione, garantendo una maggiore sicurezza.



![image](assets/fr/10.webp)



**Perché usare un Watch-only wallet?





- Sicurezza**: Ideale per monitorare un portafoglio protetto da un **Hardware Wallet** senza esporre le chiavi private su un dispositivo collegato.
- Comodità**: Consente di controllare il saldo e i nuovi indirizzi dei destinatari generate senza collegare il Hardware Wallet.
- Riservatezza**: Compatibile con opzioni quali **Tor** o **SPV** per limitare la dipendenza da server di terze parti.
- Casi d'uso**: Tracciamento di fondi in movimento, generazione di indirizzi per ricevere pagamenti o verifica di transazioni senza rischiare chiavi private.



![image](assets/fr/01.webp)



### 1.4. Chiavi pubbliche estese



Una **chiave pubblica estesa** (xpub, ypub, zpub, ecc.) è un dato derivato da un Bitcoin Wallet che genera tutte le chiavi pubbliche figlie e i loro indirizzi di ricezione associati, senza dare accesso alle chiavi private.





- Come funziona** : La chiave pubblica estesa viene generata dalla frase seed tramite un processo deterministico (BIP-32). Si crea un albero gerarchico di chiavi pubbliche figlie, ognuna delle quali può essere convertita in una Address di ricezione. Utilizzando lo stesso percorso di derivazione (ad esempio, `m/44'/0'/0'`) della Wallet osservata, la Watch-only wallet genera gli stessi indirizzi, consentendo la tracciabilità dei fondi e la creazione di nuovi indirizzi di ricezione.



![image](assets/fr/11.webp)





- Tipi di chiavi pubbliche estese
 - xpub**: Utilizzato per i portafogli Legacy (indirizzi che iniziano con "1", BIP-44) e per i portafogli Taproot (indirizzi che iniziano con "bc1p", BIP-86).
 - ypub**: Progettato per i portafogli SegWit compatibili (indirizzi che iniziano con "3", BIP-49).
 - zpub**: Associato ai portafogli SegWit nativi (indirizzi che iniziano con "bc1q", BIP-84).
 - Altri (tpub, upub, vpub, ecc.)**: Utilizzato per reti alternative (come la Testnet) o standard specifici. Ad esempio, tpub è per la rete Testnet.





- Distinzione** : La scelta tra xpub, ypub o zpub dipende dal tipo di Address (legacy, SegWit, Taproot o SegWit annidato) e dallo standard BIP utilizzato dal Wallet. Verificare il formato richiesto dal portafoglio sorgente per garantire la compatibilità con Blockstream App.





- Sicurezza e riservatezza** : La chiave pubblica estesa non è sensibile in termini di sicurezza, poiché non consente di spendere i fondi (nessun accesso alle chiavi private). Tuttavia, è sensibile in termini di riservatezza, in quanto rivela tutti gli indirizzi pubblici e la cronologia delle transazioni associate.



**Raccomandazione**: Proteggere la propria chiave pubblica estesa come informazione sensibile.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet promemoria





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: tutti i nomi di un'applicazione installata su smartphone, computer o qualsiasi dispositivo connesso a Internet, che consente di gestire e proteggere le chiavi private di un Bitcoin Wallet.
- A differenza degli **hardware wallet**, noti anche come **Cold wallet**, che isolano le chiavi offline, i software wallet operano in un ambiente connesso, rendendoli più vulnerabili agli attacchi informatici.





- Uso consigliato** :
    - Ideale per gestire quantità moderate di Bitcoin, soprattutto per le transazioni quotidiane.
    - Adatto ai principianti o agli utenti con risorse limitate, per i quali un Hardware Wallet può sembrare superfluo.





- Limitazioni**: Meno sicuro per la conservazione di grandi fondi o di risparmi a lungo termine. In questo caso, scegliete un Hardware Wallet.




## 2. Presentazione dell'applicazione Blockstream





- Blockstream App** è un'applicazione mobile (iOS, Android) e desktop per la gestione dei portafogli Bitcoin e delle attività sul Liquid Network. Acquisita da [Blockstream](https://blockstream.com/) nel 2016, era precedentemente denominata *Green Address* e poi *Blockstream Green*.
- Caratteristiche principali** :
    - Transazioni Onchain** su Blockchain Bitcoin.
    - Transazioni sulla rete **Liquid** (Sidechain per scambi veloci e riservati).
    - Portafogli di sola sorveglianza** per il monitoraggio dei fondi senza accesso alle chiavi.
    - Opzioni di privacy: connessione tramite **Tor**, connessione a un **nodo personale** tramite Electrum o verifica **SPV** per ridurre la dipendenza da nodi di terze parti.
    - Funzioni **Replace-by-fee (RBF)** per accelerare le transazioni non confermate.
- Compatibilità**: Integra portafogli hardware come **Blockstream Jade**.
- Interface**: Intuitivo per i principianti, con opzioni avanzate per gli esperti.
- Nota**: Questa guida si concentra sull'uso di Onchain. Altre esercitazioni nelle appendici riguardano Onchain, Watch-Only e la versione desktop.




## 3. Installazione e configurazione dell'applicazione Blockstream



### 3.1. scaricare





- Per Android** :
    - Scaricare [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) dal Google Play Store.
    - Alternativa: Installare tramite il file APK disponibile su [GitHub ufficiale di Blockstream](https://github.com/Blockstream/green_android).
- Per iOS** :
    - Scaricare [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) dall'App Store.
- Nota**: Assicurarsi di scaricare da fonti ufficiali per evitare applicazioni fraudolente.



### 3.2. configurazione iniziale





- Schermata iniziale**: Alla prima apertura, l'applicazione visualizza una schermata senza una Wallet configurata. I portafogli creati o importati appariranno qui in seguito.



![image](assets/fr/02.webp)





- Personalizzare le impostazioni**: Cliccare su "Impostazioni dell'applicazione", regolare le opzioni sottostanti, cliccare su "Salva", riavviare l'applicazione e creare il portafoglio.



![image](assets/fr/03.webp)



#### 3.2.1. Privacy migliorata (solo Android)





- Funzione**: Disattiva gli screenshot, nasconde le anteprime delle applicazioni nel task manager e blocca l'accesso quando il telefono è bloccato.
- Perché? ** : Protegge i dati da accessi fisici non autorizzati o da malware che catturano lo schermo.



#### 3.2.2. Connessione via Tor





- Funzione**: Instradare il traffico di rete tramite **Tor**, una rete anonima che cripta le connessioni.
- Perché? Nascondere il proprio IP Address e proteggere la propria privacy, ideale se non ci si fida della rete (ad esempio, Wi-Fi pubblico).
- Svantaggi**: Può rallentare l'applicazione a causa della crittografia.
- Raccomandazione**: Attivare Tor se la riservatezza è una priorità, ma verificare la velocità della connessione.



#### 3.2.3. Connessione a un nodo personale





- Funzione**: Collega l'applicazione al proprio **nodo Bitcoin completo** tramite un **server Electrum**.
- Perché? Fornisce un controllo totale sui dati Blockchain, eliminando la dipendenza dai server Blockstream.
- Prerequisito**: Un nodo Bitcoin configurato.
- Raccomandazione**: Utenti avanzati che desiderano la massima sovranità.



#### 3.2.4. Verifica dell'SPV





- Funzione**: Utilizza la **verifica semplificata del pagamento (SPV)** per verificare direttamente alcuni dati del Blockchain senza scaricare l'intera catena.
- Perché? Riduce la dipendenza dal nodo predefinito di Blockstream, pur rimanendo leggero per i dispositivi mobili.
- Svantaggi**: Meno sicuro di un Full node, poiché si affida a nodi di terze parti per alcune informazioni.
- Raccomandazione**: Attivare l'SPV se non si può usare un nodo personale, ma si preferisce un Full node per una sicurezza ottimale.





## 4. Creazione di un portafoglio Bitcoin "Solo osservazione



### 4.1. Recuperare la chiave pubblica estesa



Per configurare un Watch-only wallet, occorre innanzitutto ottenere la chiave pubblica estesa (xpub, ypub, zpub, ecc.) del Wallet da monitorare. Queste informazioni sono generalmente disponibili nelle impostazioni o nella sezione "Informazioni sul Wallet" del software o del Hardware Wallet.





- Esempio con l'applicazione Blockstream: Dalla schermata iniziale del Wallet, andare su "Impostazioni", quindi su "Dettagli Wallet" e copiare il file zpub :



![image](assets/fr/09.webp)





- Alternativa 1: generate un codice QR contenente la chiave pubblica estesa da scansionare nella fase successiva.
- Alternativa 2: utilizzare un output descriptor se il Wallet lo prevede.



### 4.2. importare il Wallet Solo orologio





- Attenzione**: Preparate il vostro portfolio in un ambiente privato, senza telecamere o osservatori.
- Dalla schermata iniziale, fare clic su "Imposta un nuovo portafoglio" e poi su "Inizia":



![image](assets/fr/04.webp)





- Viene visualizzata la schermata successiva:



![image](assets/fr/06.webp)






- (1) **"Configurazione del Wallet mobile "** : Creare un nuovo Hot Wallet. Vedere l'esercitazione "Blockstream App - Onchain" nell'appendice.
- (2) **"Ripristino da backup "**: Importa un portafoglio esistente utilizzando una frase Mnemonic (12 o 24 parole). Attenzione: Non importare la frase da un Cold Wallet, poiché verrà esposta su un dispositivo collegato, invalidandone la sicurezza.
- (3) **"Watch-Only "**: l'opzione che ci interessa per questa esercitazione.





- Quindi selezionare "**Firma singola**" e la rete "**Bitcoin**":



![image](assets/fr/12.webp)





- Incollare la chiave pubblica estesa (xpub, ypub, zpub, ecc.), eseguire la scansione del codice QR corrispondente o immettere un output descriptor. Anche se l'applicazione specifica "xpub", sono autorizzate anche le chiavi ypub, zpub, ecc. Fare quindi clic su "Connetti":



![image](assets/fr/13.webp)




### 4.3. Utilizzo del Wallet solo orologio



Una volta importato, il Watch-only wallet visualizza il saldo totale e la cronologia delle transazioni degli indirizzi derivati dalla chiave pubblica estesa. Sono visibili solo le transazioni onchain (le transazioni Liquid sono ignorate). Per monitorare un Liquid Wallet, ripetere l'importazione selezionando "Liquid" nel passaggio precedente.





- Visualizzazione del saldo e della cronologia**: dalla schermata iniziale, è possibile visualizzare il saldo totale e la cronologia delle transazioni onchain:



![image](assets/fr/14.webp)





- generate un Address ricevente**: Cliccare su "Transact", quindi su "Receive", per creare un nuovo Address onchain. Condividerlo tramite codice QR o copiarlo per ricevere fondi:



![image](assets/fr/15.webp)





- Inviare fondi**: Cliccare su **"Transact "**, quindi su **"Send "**. È possibile inserire :
 - Il Address del destinatario.
 - L'importo della transazione.
 - Spese di transazione.



Tuttavia, poiché il Watch-only wallet non detiene le chiavi private, non è possibile inviare direttamente i fondi. Per firmare la transazione, collegare i PSBT Hardware Wallet o Exchange scansionando i codici QR (opzione disponibile, ad esempio, sulla Coldcard Q).



![image](assets/fr/16.webp)





- Nota**: Controllare sempre il Address ricevente e i dettagli della transazione per evitare errori. I fondi inviati al Address sbagliato non possono essere recuperati.




## Appendici



### A1. Altri tutorial dell'App Blockstream





- Utilizzo della rete Onchain :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Utilizzo del Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Versione desktop :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Chiavi pubbliche estese





- Glossario :
 - [Chiavi pubbliche estese](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Corso :
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Le migliori pratiche



Per utilizzare **Blockstream App** in modo sicuro ed efficiente, seguire queste raccomandazioni. Esse vi aiuteranno a proteggere i vostri fondi, ottimizzare le vostre transazioni e preservare la vostra riservatezza sulle reti **Bitcoin (onchain)**, **Liquid** e **Lightning**.





- Proteggete la vostra frase di recupero** :
 - Esercitazione: Salvataggio della frase Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Utilizzare l'autenticazione sicura** :
 - Attivare un **PIN forte** o una **autenticazione biometrica** (impronta digitale o riconoscimento facciale) per proteggere l'accesso all'applicazione.
 - Non condividete mai il vostro PIN o i vostri dati biometrici.





- Proteggere la privacy** :
 - generate un nuovo Address per ogni ricezione onchain o Liquid per limitare il tracciamento sul Blockchain.
 - Attivare le funzioni "Enhanced Privacy", "Tor" e "SPV".
 - Per ottenere la massima riservatezza, collegare il Wallet al proprio nodo Bitcoin tramite un server Electrum invece di utilizzare il nodo pubblico





- Scegliete la rete più adatta alle vostre esigenze** :
 - Onchain**: Preferito per la custodia a lungo termine o per le transazioni di grande valore (commissioni trascurabili rispetto all'importo).
 - Liquid**: Da utilizzare per trasferimenti rapidi e a basso costo con una maggiore riservatezza.
 - Lampo**: Scegliete trasferimenti istantanei e a basso costo per piccoli importi.





- Controllare sempre gli indirizzi di spedizione** :
 - Prima di inviare fondi, controllare attentamente il Address. I fondi inviati al Address sbagliato sono persi per sempre. Utilizzare il copia/incolla o la scansione del codice QR, non copiare/modificare mai un Address a mano.





- Ottimizzare i costi** :
 - Per le transazioni onchain, scegliere le tariffe appropriate (lente, medie, veloci) in base all'urgenza e alla congestione della rete.
 - Utilizzare Liquid o Lightning per piccole quantità.





- Mantenere l'applicazione aggiornata




### A4. Risorse aggiuntive





- Link ufficiali di Blockstream:**
 - [Sito ufficiale](https://blockstream.com/)**
 - [Supporto per l'applicazione mobile](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : documentazione e chat
 - [GitHub](https://github.com/Blockstream/green_android)**





- Esploratori di blocchi :**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Fulmine: **[1ML (Lightning Network)](https://1ml.com/)**





 - Apprendimento ed esercitazioni:** **[Plan ₿ Network](https://planb.network/)** :
  - Protezione della frase di recupero



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Glossario](https://planb.network/fr/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Glossario](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

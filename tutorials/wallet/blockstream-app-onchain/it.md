---
name: App Blockstream - Onchain
description: Configurare l'App Blockstream su mobile e gestire le transazioni onchain
---
![cover](assets/cover.webp)


## 1. Introduzione


### 1.1 Obiettivo del tutorial





- Questo tutorial spiega come utilizzare l'applicazione mobile **Blockstream App** per gestire un Bitcoin **onchain** Wallet, ossia le transazioni registrate direttamente sul Blockchain Bitcoin principale.
- Copre l'installazione, la configurazione iniziale, la creazione di un Software Wallet e le operazioni di ricezione e invio di bitcoin.
- Nota: altre esercitazioni nelle appendici riguardano Liquid, Watch-Only e la versione desktop.



![image](assets/fr/01.webp)



### 1.2 Pubblico di riferimento





- Principianti**: Utenti che desiderano gestire i propri bitcoin con un'applicazione mobile intuitiva.
- Utenti intermedi**: Persone che cercano di capire le funzionalità di onchain e le opzioni di privacy come Tor o SPV.



### 1.3. Promemoria sui portafogli Hot





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: tutti i nomi di un'applicazione installata su uno smartphone, un computer o un qualsiasi dispositivo connesso a Internet, che consente di gestire e proteggere le chiavi private di un Bitcoin Wallet.
- A differenza degli **hardware wallet**, noti anche come **Cold wallet**, che isolano le chiavi offline, i software wallet operano in un ambiente connesso, rendendoli più vulnerabili agli attacchi informatici.





- Uso consigliato** :
    - Ideale per gestire quantità moderate di Bitcoin, soprattutto per le transazioni quotidiane.
    - Adatto ai principianti o agli utenti con risorse limitate, per i quali un Hardware Wallet può sembrare superfluo.





- Limitazioni**: Meno sicuro per la conservazione di grandi fondi o di risparmi a lungo termine. In questo caso, scegliete un Hardware Wallet.




## 2. Presentazione dell'applicazione Blockstream





- Blockstream App** è un'applicazione mobile (iOS, Android) e desktop per la gestione dei portafogli e delle attività del Bitcoin sul Liquid Network. Acquisita da [Blockstream](https://blockstream.com/) nel 2016, era precedentemente denominata *Green Address* e poi *Blockstream Green*.
- Caratteristiche principali** :
    - Transazioni Onchain** su Blockchain Bitcoin.
    - Transazioni di rete **Liquid** (Sidechain per scambi veloci e riservati).
    - Portafogli di sola osservazione** per il monitoraggio dei fondi senza accesso alle chiavi.
    - Opzioni di privacy: connessione tramite **Tor**, connessione a un **nodo personale** tramite Electrum o verifica **SPV** per ridurre la dipendenza da nodi di terze parti.
    - Funzioni **Replace-by-fee (RBF)** per accelerare le transazioni non confermate.
- Compatibilità**: Integra portafogli hardware come **Blockstream Jade**.
- Interface**: Intuitivo per i principianti, con opzioni avanzate per gli esperti.
- Nota**: Questa guida si concentra sull'uso di onchain. Altre esercitazioni nelle appendici riguardano Liquid, Watch-Only e la versione desktop.



## 3. Installazione e configurazione dell'applicazione Blockstream



### 3.1. scaricare





- Per Android** :
    - Scaricare [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) dal Google Play Store.
    - Alternativa: Installare tramite il file APK disponibile su [GitHub ufficiale di Blockstream](https://github.com/Blockstream/green_android).
- Per iOS** :
    - Scaricare [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) dall'App Store.
- Nota**: Assicurarsi di scaricare da fonti ufficiali per evitare applicazioni fraudolente.



### 3.2. configurazione iniziale





- Schermata iniziale**: Alla prima apertura, l'applicazione visualizza una schermata senza un Wallet configurato. I portafogli creati o importati appariranno qui in seguito.



![image](assets/fr/02.webp)





- Personalizzare le impostazioni**: Cliccare su "Impostazioni dell'applicazione", regolare le opzioni sottostanti, cliccare su "Salva", riavviare l'applicazione e creare il portafoglio.



![image](assets/fr/03.webp)



#### 3.2.1. Privacy migliorata (solo Android)





- Funzione**: Disattiva gli screenshot, nasconde le anteprime delle applicazioni nel task manager e blocca l'accesso quando il telefono è bloccato.
- Perché? ** : Protegge i dati da accessi fisici non autorizzati o da malware che catturano lo schermo.


#### 3.2.2. Connessione via Tor





- Funzione**: Instradare il traffico di rete tramite **Tor**, una rete anonima che cripta le connessioni.
- Perché? Nascondere il proprio IP Address e proteggere la propria privacy, ideale se non ci si fida della propria rete (Wi-Fi pubblico, ad esempio).
- Svantaggi**: Può rallentare l'applicazione a causa della crittografia.
- Raccomandazione**: Attivare Tor se la riservatezza è una priorità, ma verificare la velocità della connessione.


#### 3.2.3. Connessione a un nodo personale





- Funzione**: Collega l'applicazione al proprio **nodo Bitcoin completo** tramite un server **Electrum**.
- Perché? Fornisce un controllo totale sui dati Blockchain, eliminando la dipendenza dai server Blockstream.
- Prerequisito**: Un nodo Bitcoin configurato.
- Raccomandazione**: Utenti avanzati che cercano la massima sovranità.


#### 3.2.4. Verifica dell'SPV





- Funzione**: Utilizza la **verifica semplificata dei pagamenti (SPV)** per verificare direttamente alcuni dati Blockchain senza scaricare l'intera catena.
- Perché? Riduce la dipendenza dal nodo predefinito di Blockstream, pur rimanendo leggero per i dispositivi mobili.
- Svantaggi**: Meno sicuro di un Full node, poiché si affida a nodi di terze parti per alcune informazioni.
- Raccomandazione**: Attivare SPV se non è possibile utilizzare un nodo personale, ma si preferisce un Full node per una sicurezza ottimale.





## 4. Creare un portafoglio Bitcoin onchain



### 4.1. Avvio della creazione





- Attenzione**: Preparate il vostro portfolio in un ambiente privato, senza telecamere o osservatori.
- Dalla schermata iniziale, fare clic su "Inizia":



![image](assets/fr/04.webp)





- Se si desidera gestire un **Cold Wallet** (Wallet offline): fare clic su **"Connect Jade "** per utilizzare il Hardware Wallet Blockstream Jade o altri portafogli Cold compatibili.



![image](assets/fr/05.webp)





- Viene visualizzata la schermata successiva:



![image](assets/fr/06.webp)





- (1) **"Configurazione del Wallet mobile "** : Creare un nuovo Hot Wallet (Hot Wallet).
- (2) **"Ripristino da backup "**: Importa un portafoglio esistente utilizzando una frase Mnemonic (12 o 24 parole). Attenzione: Non importare una frase Cold Wallet, poiché verrà esposta su un dispositivo collegato, invalidandone la sicurezza.
- (3) **"Watch-Only "**: Importazione di un portafoglio esistente di sola lettura, per visualizzare il saldo (ad esempio del Cold Wallet) senza esporre la frase Mnemonic. Vedere l'esercitazione Watch Only nell'appendice.



**In questa esercitazione**: Fare clic su **"Setup Mobile Wallet"** per creare un Hot Wallet.


Il Wallet viene creato automaticamente e viene visualizzata la pagina iniziale del Wallet, qui chiamata "Il mio Wallet 5":



![image](assets/fr/07.webp)



**Importante**: Blockstream App ha semplificato la creazione di un Wallet evitando di visualizzare automaticamente la frase seed di 12 parole. *Anche se il portafoglio viene ora creato con un solo clic, si rischia di perdere l'accesso ai fondi se non si salva la frase seed*.



### 4.2. Salvare la frase seed





- Nella schermata iniziale del Wallet, fare clic sulla scheda "Sicurezza", quindi sulla richiesta "Backup" o sul menu "Frase di ripristino":



![image](assets/fr/08.webp)



Verrà visualizzata la frase seed di 12 parole da salvare.





- Scrivete la vostra frase di recupero con la massima cura. Scrivetela su carta o metallo e conservatela in un luogo sicuro (luogo sicuro e offline). Questa frase è l'unico mezzo per accedere ai bitcoin in caso di perdita del dispositivo o di cancellazione dell'applicazione.
- È anche importante notare che chiunque abbia questa frase può rubare tutti i vostri bitcoin. Non conservateli mai in formato digitale:
 - Nessuna schermata
 - Nessun backup su cloud, e-mail o messaggistica
 - Nessun copia/incolla (rischio di salvare negli appunti)



**! Questo punto è fondamentale**. Per ulteriori informazioni sul backup :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Confermare la frase seed



Prima di inviare fondi a un Address associato a questa frase seed, è necessario testare il backup delle 12 parole.



Per farlo, scriveremo un riferimento, cancelleremo il Wallet, lo ripristineremo con il backup e verificheremo che il riferimento sia rimasto invariato.





- Nella schermata iniziale del Wallet, fare clic sulla scheda "Impostazioni", quindi su "Dettagli Wallet" e copiare la zPub ([chiave pubblica estesa](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602):



![image](assets/fr/09.webp)



Nota: uno zpub Address può essere importato nell'applicazione Blockstream per la funzione "Watch Only" (vedi Appendice).





- Eliminare l'applicazione, quindi ripristinare il Wallet tramite **"Ripristino da backup "** inserendo la frase Mnemonic e verificare che lo zpub sia invariato. In caso affermativo, il backup è corretto e si possono inviare fondi al Wallet.





- Per saperne di più su come eseguire un test di recupero, ecco un tutorial dedicato:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Protezione dell'accesso all'applicazione



Bloccate l'accesso all'applicazione con un codice PIN forte:




- Dalla schermata iniziale del Wallet, andare su **"Sicurezza "** e cliccare su **"PIN "**
- Inserire e confermare **un codice PIN casuale di 6 cifre**.



**Opzione biometrica**: Disponibile per una maggiore comodità, ma meno sicura di un robusto codice PIN (rischio di accesso non autorizzato, ad es. impronta digitale o scansione del viso durante il sonno).



**Nota**: Il PIN protegge il dispositivo, ma solo la frase seed può essere utilizzata per recuperare i fondi.





## 5. Utilizzo del Wallet onchain



### 5.1. Ricevere bitcoin





- Dalla schermata iniziale del portafoglio, fare clic su "**Transact**" e poi su "Receive "**.



![image](assets/fr/10.webp)





- L'applicazione visualizza un Address di ricezione **vuoto** (formato SegWit v0, che inizia con `bc1q...`). L'utilizzo di un nuovo Address ogni volta che si riceve il Bitcoin migliora la riservatezza.





- Opzioni** :
    - (1) "Bitcoin": fare clic per selezionare una spedizione onchain o Liquid e scegliere l'asset.
    - (2) Fare clic sulle frecce per selezionare un altro nuovo Address collegato a questa frase seed.
    - (3) È anche possibile scegliere un Address tra quelli già utilizzati/visualizzati, facendo clic sui tre punti in alto a destra e poi su "Elenco indirizzi"
    - (4) Per richiedere un importo specifico, fare clic sui tre punti in alto a destra, selezionare "Richiedi importo" e inserire l'importo desiderato. Il QR verrà aggiornato e il Address sarà sostituito da un URI di pagamento Bitcoin.




![image](assets/fr/11.webp)





- Condividere il Address/URI facendo clic su "**Condividi**", copiando il testo o scansionando il codice QR.
- Verifica**: Verificare il più possibile il Address condiviso con il destinatario per evitare errori o attacchi (ad esempio, malware che modificano la clipboard).



### 5.2. inviare bitcoin





- Dalla schermata iniziale del portafoglio, fare clic su "**Transact**" e poi su **"Send "**:



![image](assets/fr/12.webp)





- Inserire i dettagli** :
    - (1) Inserire il **Address del destinatario** incollandolo o scansionando un codice QR.
    - (2) Verificare le attività e il conto da cui vengono inviati i fondi.
    - (3) Indicare l'**importo** da inviare. È possibile scegliere l'unità di misura: BTC, satoshis, USD, ...


L'importo minimo (limite del dush) al 03/08/2025 è di 546 Sats.




    - (4) Selezionare **tasse di transazione** :
        - Scegliete tra le opzioni suggerite (ad esempio, veloce, media, lenta) a seconda dell'urgenza e verrà visualizzato un tempo di trasferimento approssimativo.
        - Per tariffe personalizzate, regolare manualmente il numero di Satoshi per vbyte (vedere [Mempool.space](https://Mempool.space/) per le tariffe di mercato).




![image](assets/fr/13.webp)





- Controllo** :
    - Controllare il Address, l'importo e le spese nella schermata di riepilogo.
    - Un errore Address può causare una perdita irreversibile di fondi. Attenzione alle minacce informatiche che modificano gli appunti.



![image](assets/fr/14.webp)





- Conferma**: Fare scorrere il pulsante "Invia" per firmare e distribuire la transazione.
- Seguito**: Nella scheda "Transazione" del Wallet, la transazione appare come "in attesa" fino alla conferma (da 1 a 6 conferme):



![image](assets/fr/15.webp)





- Finché la transazione non è stata confermata, la funzione "Replace by fee" (vedi Appendice) consente di accelerarne la gestione aumentando le commissioni di transazione:



![image](assets/fr/16.webp)




## Appendici



### A1. Altri tutorial Blockstream



Utilizzo del Liquid Network



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Importazione e tracciamento di un Wallet in modalità "Solo orologio"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Versione desktop



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Spiegazione di Replace-by-fee (RBF)



**Definizione**: Replace-by-fee (RBF) è una caratteristica della rete Bitcoin che consente al mittente di accelerare la conferma di una transazione **onchain** accettando di pagare una tariffa più alta.



**Limiti** :




- Il RBF non è disponibile per le transazioni Liquid o Lightning.
- La transazione iniziale deve essere contrassegnata come compatibile con il RBF al momento della sua creazione, cosa che Blockstream App fa automaticamente.



**Maggiore informazione:**




- [Glossario](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Le migliori pratiche



Per utilizzare **Blockstream App** in modo sicuro ed efficiente, seguire queste raccomandazioni. Esse vi aiuteranno a proteggere i vostri fondi, ottimizzare le vostre transazioni e preservare la vostra riservatezza sulle reti **Bitcoin (onchain)**, **Liquid** e **Lightning**.





- Proteggete la vostra frase di recupero** :
 - Esercitazione: Salvare la frase del Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Utilizzare l'autenticazione sicura** :
 - Attivare un **PIN forte** o una **autenticazione biometrica** (impronta digitale o riconoscimento facciale) per proteggere l'accesso all'applicazione.
 - Non condividete mai il vostro PIN o i vostri dati biometrici.





- Proteggere la privacy** :
 - generate un nuovo Address per ogni ricezione onchain o Liquid per limitare il tracciamento sul Blockchain.
 - Attivare le funzioni "Enhanced Privacy", "Tor" e "SPV".
 - Per la massima riservatezza, collegare il Wallet al proprio nodo Bitcoin tramite un server Electrum invece di utilizzare il nodo pubblico





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





- Link ufficiali:**
 - [Sito ufficiale](https://blockstream.com/)**
 - [Supporto per l'applicazione mobile](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : documentazione e chat
 - [GitHub](https://github.com/Blockstream/green_android)**





- Esploratori di blocchi :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
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
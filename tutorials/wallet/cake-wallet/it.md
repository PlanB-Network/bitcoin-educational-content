---
name: Torta Wallet
description: Tutorial su Cake Wallet e sui pagamenti silenziosi
---

![cover](assets/cover.webp)


Questa guida esplora [**Cake Wallet**](https://cakewallet.com/): un Wallet open-source, non custodiale e incentrato sulla privacy, disponibile per Android, iOS, macOS, Linux e Windows. Ci immergeremo nelle sue caratteristiche di privacy specifiche per il Bitcoin, vedremo come inviare/ricevere Bitcoin tramite **Silent Payments** (un protocollo di privacy migliorato per il On-Chain) e daremo un'occhiata all'implementazione del PayJoin v2 per le transazioni asincrone.


## 🎉 Caratteristiche principali



- [**Pagamenti silenziosi (BIP-352)**](https://BIPs.dev/352/) migliora i precedenti [codici di pagamento BIP 47](https://silentpayments.xyz/docs/comparing-proposals/bip47/) chiamati anche "PayNyms" con indirizzi furtivi riutilizzabili. Quando un mittente utilizza il vostro Address di pagamento silenzioso, il suo Wallet ricava un Address unico utilizzando chiavi diverse che verranno combinate in un Taproot Address unico. I record Blockchain mostrano transazioni non correlate, impedendo il collegamento dei pagamenti in entrata. I pagamenti silenziosi offrono una serie di vantaggi, tra cui:
    - Indirizzi riutilizzabili: Non è necessario creare un nuovo generate per ogni transazione, garantendo una migliore esperienza utente e una maggiore privacy
    - Nessun aumento dei costi: I pagamenti silenziosi non aumentano le dimensioni o i costi delle transazioni.
    - Maggiore anonimato: Gli osservatori esterni non possono collegare le transazioni a un Address Silent Payment.
    - Non è richiesta alcuna interazione tra mittente e destinatario: Le transazioni possono essere effettuate senza alcuna comunicazione tra le parti.
    - Indirizzi unici per ogni pagamento: Eliminazione del rischio di riutilizzo accidentale del Address.
    - Non è necessario un server: I pagamenti silenziosi possono essere effettuati senza bisogno di un server dedicato.
- PayJoin v2** attenua l'analisi del grafico delle transazioni unendo gli input di mittenti e destinatari in un'unica transazione. La torta Wallet implementa due progressi fondamentali:
    - Transazioni asincrone**: Il mittente e il destinatario non devono più essere online contemporaneamente per completare una transazione privata.
    - Comunicazione senza server**: Nessuna delle due parti ha bisogno di gestire un server PayJoin, eliminando un importante ostacolo tecnico.
- Il controllo Coin** consente la selezione manuale del UTXO durante le transazioni. Ciò impedisce il collegamento accidentale degli indirizzi quando si spendono più UTXO con origini diverse.
- Supporto TOR**, che consente agli utenti di instradare il proprio traffico di rete attraverso la rete Tor
- RBF** (Replace-By.Fee) consente di regolare la tariffa dopo l'invio di una transazione.


## 1️⃣ Impostazione del Wallet


Cake Wallet offre un'ampia gamma di piattaforme supportate. È possibile scegliere tra `Android`, `iOS / macOS`, `Linux` e `Windows`.  Per iniziare, visitare il sito https://docs.cakewallet.com/get-started/ e selezionare il sistema operativo.


![image](assets/en/01.webp)


Dopo l'installazione, impostare un `PIN` (4 o 6 cifre). Verrà quindi visualizzato:


1. creare un nuovo Wallet" (per i nuovi utenti)

2. ripristino Wallet` (per i portafogli esistenti)


![image](assets/en/02.webp)


Nella schermata successiva è possibile scegliere tra un'ampia gamma di criptovalute. Selezionare `Bitcoin` e toccare `Next` e fornire un `nome Wallet` per identificare il Wallet. Toccando `Impostazioni avanzate` appare una serie di `Impostazioni sulla privacy`. Apportare queste modifiche:



- Fiat API:** seleziona `Tor Only` (instrada le richieste di prezzo attraverso Tor)
- Scambio:** selezionare `Solo Tor` (anonimizza il traffico Exchange)


Il tipo BIP-39 seed è generato per impostazione predefinita, con l'opzione di passare al tipo Electrum seed. I percorsi di derivazione sono i seguenti:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Se si desidera aggiungere un ulteriore Layer di sicurezza, è possibile impostare un `passphrase`.  Lo scopo principale di un passphrase è quello di fornire una protezione aggiuntiva contro gli attacchi fisici. Anche se un attaccante trova la frase seed, non può accedere al Wallet senza il passphrase corretto. In altre parole, la frase seed da sola rappresenta un Wallet, mentre la frase seed più passphrase crea un Wallet completamente diverso, senza alcun collegamento con l'originale. Questa funzione consente anche di creare "portafogli segreti" protetti dal passphrase e di ottenere una negazione plausibile. In una situazione di coercizione, si potrebbe rivelare la frase seed mantenendo al sicuro i beni più importanti nel Wallet protetto dal passphrase.


Se si gestisce già un proprio nodo, selezionare `Add New Custom Node` e fornire il proprio `Node Address` per convalidare transazioni e blocchi all'interno della propria infrastruttura. Una volta terminato, toccare `Continue` e `Next` per creare il proprio Wallet.


![image](assets/en/03.webp)


Nella schermata successiva, viene visualizzato un disclaimer:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Per imparare le migliori pratiche di salvataggio della frase Mnemonic, consultate questo tutorial:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Toccare `Comprendo. Mostrami il mio seed" e salva queste parole in un luogo sicuro! Quindi toccare `Verifica seed` e dopo la verifica `Apri Wallet`.


## 2️⃣ Impostazioni


Prima di approfondire, diamo un'occhiata alla `Schermata iniziale` e alle `Impostazioni`.


Nella schermata iniziale vengono visualizzati diversi elementi:



- il menu `Hamburger` ci porta alle `impostazioni`
- Saldo disponibile
- Silent Payments Card per avviare la scansione delle transazioni inviate al vostro Silent Payment Address
- Scheda PayJoin per "attivare" il PayJoin come funzione di tutela della privacy e di risparmio di denaro
- in basso ci sono le scorciatoie per `Wallet Overview`, `Receive`, `Swap` tra Bitcoin e altre valute, `Send` e `Buy`


![image](assets/en/11.webp)


Toccando l'icona `Menu hamburger` si apre il menu delle impostazioni. Esaminiamo le opzioni.


![image](assets/en/05.webp)


### A - Connessione e sincronizzazione 🔗


Qui è possibile ricollegare il Wallet, gestire i nodi e collegarsi al proprio nodo (consigliato). La funzione `Scansione pagamenti silenziosi` ci permette di personalizzare la scansione specificando `Scansione dall'altezza del BLOCK` o `Scansione dalla data`.


![image](assets/en/06.webp)


Come caratteristica "alfa" è disponibile anche l'opzione "Attiva Tor integrato" per instradare il traffico attraverso la rete Tor.


### B - Impostazioni per i pagamenti silenziosi 🔈


Per visualizzare questa funzione, è possibile attivare la scheda Pagamenti silenziosi nella schermata principale. L'attivazione della funzione "Scansione continua" consente al Wallet di monitorare continuamente il Blockchain per i pagamenti silenziosi in arrivo. È possibile specificare i parametri di scansione per personalizzare il processo di scansione in base alle proprie esigenze, come descritto in precedenza.


![image](assets/en/07.webp)


### C - Sicurezza e backup 🗝️


Per proteggere il nostro Wallet, possiamo creare un backup seguendo le istruzioni dell'applicazione. In questo modo avremo una copia sicura delle nostre chiavi private, che ci permetterà di recuperare il nostro Wallet in caso di smarrimento o furto. Inoltre, possiamo visualizzare la nostra frase seed e le nostre chiavi private, cambiare il nostro PIN, abilitare l'autenticazione biometrica, firmare/verificare e impostare 2FA per un ulteriore Layer di protezione.


![image](assets/en/08.webp)


**Nota**: A partire da settembre 2025, l'autenticazione biometrica delle impronte digitali sui dispositivi Android deve funzionare con almeno un'implementazione biometrica di Classe 2; per maggiori dettagli, consultare [qui] (https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Tuttavia, questo requisito potrebbe cambiare in futuro.


### D - Impostazioni sulla privacy 🔒


Possiamo anche migliorare la sicurezza del nostro Wallet utilizzando Tor per criptare la nostra connessione a Internet e salvaguardare la nostra privacy quando accediamo a fonti esterne. Inoltre, possiamo impedire gli screenshot per mantenere riservate le informazioni del nostro Wallet, abilitare gli indirizzi autogenerati per crearne di nuovi a ogni transazione e disabilitare le azioni di acquisto/vendita per evitare transazioni non autorizzate. È inoltre possibile "attivare il PayJoin", un'altra funzione di privacy che esamineremo in seguito.


![image](assets/en/09.webp)


### E - Altre impostazioni 🔧


Altre impostazioni ci permettono di gestire la priorità delle commissioni e di impostare il livello di commissione predefinito per le nostre transazioni. Questo ci permette di controllare le commissioni di transazione associate ai nostri Silent Payment, tenendo conto dell'attuale utilizzo della rete.


![image](assets/en/10.webp)


## 3️⃣ Ricevere ₿itcoin con Silent Payments


Sono disponibili diverse opzioni e tipi di Address per la ricezione del Bitcoin. il `SegWit (P2WPKH)` * (che inizia con bc1q....)* è l'opzione predefinita.  In questo esempio selezioniamo `Pagamenti silenziosi`.


Per ricevere un pagamento silenzioso, toccare innanzitutto l'icona `Ricevi` nella torta Wallet. Quindi, inserire l'importo che si prevede di ricevere. Per specificare il tipo di Address, toccare nuovamente `Ricevi` nella parte superiore dello schermo e selezionare `Pagamenti silenziosi` dalle opzioni.


Nella schermata principale verranno visualizzati il codice QR Silent Payment e il Address riutilizzabile. Come previsto, il Address è piuttosto lungo:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Ora, utilizzare un Wallet compatibile con il BIP-352 (ad esempio il Wallet blu) per scansionare questo codice QR e inviare il pagamento. Vedrete che il Wallet ricava una destinazione unica Address dal vostro Address silenzioso.


![image](assets/en/13.webp)


## 4️⃣ Invio di ₿itcoin con Silent Payments


Poiché il Wallet blu può solo "inviare" pagamenti silenziosi, utilizzeremo un altro BIP 352 compatibile come parte ricevente. La procedura è identica a quella di una normale transazione Bitcoin.



- Toccate "Invia" nella schermata principale
- incollando il nostro riutilizzabile `sp1qq...` Address o scansionando il codice QR direttamente all'interno dell'applicazione.
- Selezionare l'importo che si desidera spendere dal proprio saldo disponibile
- Toccare "Invia" nella parte inferiore dello schermo per confermare la transazione


Una volta inserito il `sp1qq...` Address, il Wallet ricava automaticamente un corrispondente `bc1p...` Taproot Address (P2TR) in background, che verrà utilizzato per il pagamento silenzioso.


È possibile scrivere una nota interna per ogni transazione, regolare le impostazioni delle commissioni o selezionare determinati UTXO per la transazione utilizzando la funzione `Coin Control`.


![image](assets/en/14.webp)


passare il dito a destra per confermare la transazione.


Una volta inviata la transazione, vi verrà chiesto se volete aggiungere questo contatto alla vostra rubrica Address.


![image](assets/en/15.webp)


## 6️⃣ PayJoin


Rivediamo cosa è il PayJoin (https://docs.cakewallet.com/cryptos/Bitcoin/#PayJoin):


payjoin v2 è una funzione di Bitcoin che consente al mittente e al destinatario di una transazione di lavorare insieme per creare un'unica transazione. Questa transazione ha input provenienti da *entrambi* i mittenti e i destinatari, il che impedisce le più comuni tecniche di sorveglianza contro Bitcoin e consente di migliorare la scalabilità e di risparmiare sulle commissioni in alcune circostanze._


Per saperne di più su PayJoin, potete anche visitare il seguente tutorial.


https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Per utilizzare il PayJoin entrambe le parti necessitano di un Wallet compatibile con il PayJoin e il destinatario deve avere almeno un Coin o un'uscita nel suo Wallet. Per iniziare, seguire i passaggi indicati di seguito:


1. Toccare il `Menu hamburger` e toccare il pulsante `Privacy`

2. Attivare l'opzione `Usa PayJoin

3.  Toccate "Ricevi" nella schermata iniziale e vi verrà presentato un codice QR PayJoin e un pulsante di copia (quando è selezionato SegWit)


![image](assets/en/16.webp)


## 7️⃣ Altre caratteristiche


Ci sono molte altre funzioni come lo "swap" di più valute, le opzioni di "acquisto e vendita" con connessioni a diversi venditori e programmi specifici per le torte come "Cake Pay", che consente di acquistare carte prepagate o carte regalo.


![image](assets/en/17.webp)


## 🎯 Conclusione


Questa è la nostra recensione di Cake Wallet, che offre una pratica privacy Bitcoin grazie a funzioni quali Silent Payments (BIP-352) e PayJoin v2.


I Pagamenti silenziosi sostituiscono gli indirizzi usa e getta con indirizzi furtivi riutilizzabili per impedire il collegamento On-Chain delle transazioni in entrata. Sebbene i problemi di sincronizzazione delle versioni precedenti siano notevolmente migliorati, i requisiti computazionali per la scansione e il rilevamento dei pagamenti silenziosi sono aumentati e richiedono maggiori risorse e larghezza di banda.


PayJoin v2 stravolge l'analisi della catena unendo gli input del mittente e del destinatario in singole transazioni senza costi aggiuntivi o coordinamento centrale. Questo rompe l'euristica dell'ingresso comune Ownership, il che rappresenta un vantaggio significativo in quanto significa che non si può presumere che tutti gli ingressi appartengano al mittente.


Per gli utenti che danno priorità all'anonimato finanziario, Cake Wallet è un'opzione valida. Incorpora i protocolli di privacy direttamente nella sua funzionalità principale, rendendoli accessibili senza alcuna complessità tecnica. Con l'aumento della sorveglianza sulle blockchain pubbliche, strumenti come questo aiutano a mantenere la privacy delle transazioni dove è più importante. Un'implementazione più ampia di questi standard nel panorama Wallet sarebbe uno sviluppo gradito.


## 📚 Risorse


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://BIPs.dev/352/](https://BIPs.dev/352/)


https://PayJoin.org/
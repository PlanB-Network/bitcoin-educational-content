---
name: Nunchuk
description: Wallet mobile adatto a tutti
---
![cover](assets/cover.webp)

## Un wallet potente
Nunchuk è arrivato a fine 2020 con una filosofia ben precisa: fare del multifirma uno standard. È pertanto stato progettato per svolgere funzioni molto avanzate, con la pregevole scelta di costruire il progetto direttamente su Bitcoin Core, il software di riferimento per l'ecosistema Bitcoin.

Dopo oltre 4 anni di sviluppo ed utilizzo, è pronto per essere provato su scala. Se sei un principiante e non conosci Nunchuk, questa guida ti aiuterà a compiere i primi passi e scoprire questo software, le cui funzioni avanzate potrai conoscere dopo aver superato il primo impatto. Il tutorial in sé è dedicato ad utenti intermedi che possiedono le competenze necessarie a seguirne tutti i passi, ma può essere di ispirazione per tutti per scoprire come aumentare le abilità. Inizieremo con la versione mobile e questa puntualizzazione è necessaria, dato che Nunchuk ha il software per essere eseguito anche su computer.

## Download
Il primo step è sicuramente decidere dove scaricare l'app. Vai sul [sito ufficiale](https://nunchuk.io/) dove puoi trovare un po' di documentazione (non molta ma è un inizio), la presentazione delle caratteristiche nonché, verso fine pagina, tutti i link per il download.

📌 Per questo tutorial ho deciso di mostrarti come scaricare il software wallet dal repository Github e come verificare la release prima di installarla sul tuo cellulare. **La procedura che segue si può fare solo dal computer**, pertanto ti consiglio di fare tutte queste operazioni dal tuo desktop o laptop e - dopo tutte le verifiche - trasferire il file `.apk` sul cellulare.

![image](assets/en/01.webp)

Se le tue competenze non sono molto avanzate, puoi decidere di scaricare l'`.apk` dagli store ufficiali e saltare direttamente alla parte di questo tutorial dedicata alla configurazione. Se invece vuoi fare il salto di qualità, continua a seguire passo dopo passo.

Dal tuo computer desktop clicca dunque _Visit our open source repository_

Il link ti porterà alla pagina Github di Nunchuk, dove troverai una serie di repo. Noi ci focalizzeremo su quello di _nunchuk-android_

![image](assets/en/02.webp)

Nella schermata successiva, individua a destra la sezione dedicata alle _Releases_ e scegli _Latest_

![image](assets/en/03.webp)

Tra gli _Assets_, scarica la release (in questo esempio la 1.67.apk), insieme al file SHA256SUMS e SHA256SUMS.asc.

![image](assets/en/04.webp)

Per trovare la chiave GPG dello sviluppatore torna nella sezione _Releases_ del repository e cerca la 1.9.53 (o precedenti) che riportano il link per ottenere e scaricare la _GPG Key_

![image](assets/en/05.webp)

Procederemo alla verifica tramite un pratico tool offerto da Sparrow wallet, che ha una finestra dedicata a questo scopo e che supporta le firme PGP e i Manifest SHA256.

Lancia quindi Sparrow e dal menu _Tools_ scegli _Verify Download_.

![image](assets/en/06.webp)

Nella finestra che si apre in pop-up, trovi dei campi da "compilare": scegli il tasto _Browse_ a destra e seleziona, per ogni campo, i file corrispondenti che hai hai appena scaricato da Github. Completati tutti i passi, la finestra si presenterà come segue, con le spunte verdi e la conferma dell'hash del manifest.

![image](assets/en/07.webp)
**N.B. lo screenshot è tratto da un PC Windows, la stessa pratica si può usare per qualsiasi sistema operativo del tuo computer, basta avere Sparrow Wallet installato. E verificato!**

Puoi trovare la guida a Sparrow wallet per scaricare questo software wallet
https://planb.network/en/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Puoi quindi trasferire il file `.apk` dal computer al cellulare

![image](assets/en/08.webp)

e installare Nunchuk

![image](assets/en/09.webp)

Prima di lanciare Nunchuk sul cellulare, apri Orbot e inserisci il nuovo arrivato nella lista delle app da instradare sotto Tor.

![image](assets/en/11.webp)

Ora fai partire Nunchuk. Per le caratteristiche del progetto - che non sono oggetto di questo tutorial - Nunchuk, una volta aperto, ti inviterà ad eseguire il login tramite una email o un profilo Google. Finché non avrai intenzione di usufruire dei piani avanzati di Nunchuk Inc, **evita di eseguire il login** e procedi scegliendo l'opzione _Continue as guest_.

![image](assets/en/12.webp)

## Impostazioni
Nunchuk si presenta con una finestra _Home_ di presentazione, dove è facile capirne la filosofia di funzionamento e che approfondiremo tra poco.

In basso puoi trovare i menu e, come primo step, scegli _Profile_ per accedere alle impostazioni.

![image](assets/en/10.webp)

Scegli quindi _Display settings_, continuando ad ignorare l'invito a creare un account.

![image](assets/en/14.webp)

Nella schermata che segue puoi controllare se il wallet è online e puoi collegare il tuo server, facendo bene attenzione alle istruzioni al link che ti viene proposto cliccando su _this guide_.

![image](assets/en/15.webp)

Salva le impostazioni con il comando _Save network settings_, torna nel menu _Profile_ e seleziona _Security settings_.

![image](assets/en/16.webp)

Da questo menu imposti come difendere l'apertura dell'app. Per evitare accessi non voluti puoi proteggere Nunchuk con il biometrico del telefono, e/o aggiungere un PIN di sicurezza.

![image](assets/en/17.webp)

Dai anche un'occhiata al menu _About_, che trovi sempre nella finestra _Profile_

![image](assets/en/18.webp)

che ti consentirà di verificare la versione della app, o per contattare gli sviluppatori in caso di necessità.

![image](assets/en/19.webp)

## Generazione di chiavi e wallet
Come è facile intuire dalla filosofia di Nunchuk, il software si propone come utile strumento per gestire wallet multifirma. Per svolgere questa funzione Nunchuk consente di creare wallet separandoli da quelle che sono le chiavi necessarie per disporre le firme digitali.

Di fatto, il funzionamento ideale di Nunchuk prevede la creazione di wallet che possono essere dei watch-only, dipendenti da chiavi che possono essere "cold".

Nelle schermate precedenti avrai sicuramente notato che c'è in basso un menu denominato _Keys_. Se hai appena scaricato Nunchuk, sia in _Home_ che in _Keys_ ti appare un grosso pulsante che ti invita ad aggiungere una chiave, _Add Key_.

![image](assets/en/20.webp)
![image](assets/en/21.webp)

**Questo è proprio il funzionamento di Nunchuk:** prima si generano/importano le chiavi e poi si crea il wallet, configurando il quale si sceglie quali chiavi autorizzeranno lo sblocco dei fondi conservati su di esso.

Anche in caso di wallet singlesig, si crea prima la chiave e solo in seguito il wallet. Ed è proprio quello che faremo adesso, iniziando da un wallet singlesig per rompere il ghiaccio e scoprire le funzioni di Nunchuk.

Clicca _Add Key_

![image](assets/en/22.webp)

Nunchuk mostra una serie di dispositivi di firma supportati ma, per iniziare, scegli _Software_.

![image](assets/en/23.webp)

Nunchuk genererà una mnemonica che verrà conservata sul dispositivo. È necessario quindi scriversi la sequenza di parole per il backup, creando le condizioni ambientali migliori e assicurandosi di avere il tempo necessario per fare bene e con calma. Il software mostra la mnemonica una sola volta, sia che si scelga di mostrarla subito o in seguito, pertanto scegli _Create and backup now_.

![image](assets/en/24.webp)

Nunchuk genera frasi mnemoniche di 24 parole, le quali compaiono subito nella schermata successiva

![image](assets/en/25.webp)

per poi procedere ad una veloce verifica, chiedendo di selezionare la parola corretta, tra 3 scelte, corrispondente al numero della sequenza mnemonica.
Se hai scritto correttamente la mnemonica, il tasto _Continue_ diventa operativo. Premilo per andare avanti.

![image](assets/en/26.webp) 

Dai un nome alla tua chiave e premi _Continue_.

![image](assets/en/27.webp)

Al termine di queste fasi, ti verrà chiesto se aggiungere alla tua frase mnemonica una [Passphrase](https://planb.network/en/resources/glossary/passphrase-bip39). Se non hai la necessaria consapevolezza di come usare la passphrase, predisporne il backup o di come funziona, ti consiglio di scegliere _I don't need a passphrase_.

![image](assets/en/28.webp)

La chiave è infine creata e ti viene mostrata nel menu:
- Con _Key Spec_ viene indicata la master fingerprint
- Hai delle impostazioni, i tre pallini in alto a destra, dove puoi cancellare la chiave o firmare un messaggio
- Accanto al nome della chiave trovi l'icona di un pennino, cliccando il quale potrai editare il nome della Key, ad esempio per tenere in ordine le tue chiavi in futuro.
- Come ultimo comando, puoi controllare lo stato di salute della chiave: premendo _Run health check_ puoi far controllare all'app se una chiave è compromessa.

Quando sei a posto, clicca _Done_

![image](assets/en/29.webp)

Nel menu _Keys_ vedrai comparire la tua prima chiave.

![image](assets/en/30.webp)

Andando nel menu _Home_ compare la possibilità di creare il wallet. Clicca _Create new wallet_.

![image](assets/en/31.webp)

Nunchuk ti mostra una serie di possibilità che hanno a che fare, per la maggior parte, con i servizi che la società offre e che non sono oggetto di questo tutorial.

In questa guida creeremo un _Hot wallet e un _Custom wallet_ dettagliandone i particolari.
Iniziamo con _Custom wallet_.

![image](assets/en/32.webp)

In maniera semplice, l'app ti chiederà di dare un nome a questo nuovo wallet e scegliere lo script per gli indirizzi. Per il tutorial ho scelto di lasciare l'impostazione predefinita, _Native segwit_. Quando hai finito, scegli _Continue_

![image](assets/en/33.webp)

La configurazione del wallet prosegue chiedendo di impostare con quale chiave verranno sbloccati i fondi di questo wallet. Qualora ci fossero più chiavi, ti verrà mostrato un elenco dal quale scegliere. Noi per il momento ne abbiamo creata solo una, pertanto scegliamo di mettere la spunta su quella. In basso a destra è visibile come Nunchuk ti chiederà di impostare i tuoi futuri wallet multifirma, aumentando il numero di _Required keys_. 

![image](assets/en/34.webp)

Siccome stiamo creando un singlesig, lasciamo `1` e clicchiamo _Continue_.

Per ultimo, compare una schermata di verifica, dove puoi controllare le caratteristiche del wallet:
- il nome
- il tage `1/1 Multisig`, che è il modo in cui Nunchuk nomina i wallet singlesig
- lo script type, `Native segwit`
- la chiave `Keys`, con relativo fingerprint e derivation path

Quando sei soddisfatto, premi _Create wallet_

![image](assets/en/35.webp)

Il wallet è stato creato e puoi scaricare il file [.BSMS](https://github.com/bitcoin/bips/blob/master/bip-0129.mediawiki) come backup. Per tornare al menu principale clicca la freccia in alto a sinistra.

![image](assets/en/36.webp)

Sei in _Home_, dove ti viene mostrato il wallet appena creato che riporta il saldo e lo stato della connessione. Cliccando nello spazio blu, puoi accedere alle funzioni principali del wallet.

![image](assets/en/37.webp)

- L'icona della lente in alto a destra ti permette di fare la ricerca di una transazione;
- `View wallet config` da accesso al menu di configurazione, dove puoi editare il nome del wallet e attivare delle opzioni avanzate, in alto a destra (di cui non è possibile avere screenshot). Qui potrai esportare la configurazione del wallet, le labels, sostituire le keys, cambiare il [gap limit](https://planb.network/en/resources/glossary/gap-limit) ed altro.

## Transazioni con Nunchuk

Premi _Receive_

![image](assets/en/38.webp)

L'app è programmata per mostrare il QR Code dell'indirizzo o copiare/condividere lo scriptPubKey per ricevere fondi onchain.

![image](assets/en/39.webp)

Abbiamo fatto arrivare un UTXO su questo primo indirizzo,

![image](assets/en/40.webp)

ma clicchiamo ancora _Receive_ per riceverne un altro.

![image](assets/en/41.webp)

Lo scopo è farti scoprire che Nunchuk ti segnala questo nuovo indirizzo come _Unused address_ ma ti fa anche vedere che hai degli _Used addresses_ e il relativo conteggio.

### Transazione di spesa con coin control

Quando anche questo secondo UTXO è arrivato, torna nella schermata principale del wallet per controllare lo stato delle due transazioni in arrivo e, soprattutto, clicca sull'opzione _View coins_

![image](assets/en/42.webp)

dove ti saranno mostrati gli UTXO singoli. Qui è possibile scegliere di visualizzarne un in particolare, cliccando la freccina accanto all'importo

![image](assets/en/43.webp)

e controllare quando è arrivato, la descrizione, bloccare l'UTXO in modo che non venga speso ed altro.

![image](assets/en/44.webp)

Ma se torni nel menu _Coins_ cliccando la freccia in alto a destra, puoi attivare il "Coin Control" per spendere i tuoi UTXO in maniera più controllata.

Nell'esempio che segue ho scelto di selezionare l'UTXO di 21.000 sats e poi cliccare il simbolo in basso a sinistra.

![image](assets/en/45.webp)

Nunchuk apre automaticamente la finestra _New transaction_ per spendere questo UTXO. Nella transazione di spesa, per prima cosa, si deve impostare l'importo manualmente o selezionando _Send all selected_ per inviare tutto il saldo del coin control, senza generare resti. Una volta impostato l'importo, scegli _Continue_

![image](assets/en/46.webp)

Ora Nunchuk mostra dove incollare l'indirizzo a cui trasferire questi fondi, dettagliare una descrizione e finalizzare la transazione.

![image](assets/en/47.webp)

Scegliendo _Create transaction_ si delega all'app la gestione automatica delle fee e della transazione. Io ti consiglio di scegliere _Custom transaction_ per un maggiore controllo.

In questa nuova schermata è importante selezionare 
- _Subtract fee from send amount_, per impedire che le fee vengano pagate da un altro UTXO presente nel wallet, spendendolo e generando un resto (che è una perdita di privacy evitabile);
- per poi impostare le fee manualmente, dopo aver controllato sull'explorer.

Fatte tutte queste operazioni, clicca su _Continue_

![image](assets/en/48.webp)

La successiva schermata è il riepilogo completo della transazione. Se è tutto a posto, confermare selezionando _Confirm and create transaction_.

![image](assets/en/49.webp)

Con _Pending signatures_ Nunchuk ti avvisa che la transazionep è in attesa della firma per approvare la spesa, che si appone cliccando _Sign_.

![image](assets/en/50.webp)

Compare in basso il comando _Broadcast_ per propagare la transazione finalizzata e firmata.

![image](assets/en/51.webp)

### Transazione di spesa da menu _Send_

Mentre nella pagina principale del wallet vediamo la transazione in uscita e in attesa di conferma, usiamo il menu _Send_ per simulare una spesa quotidiana.

![image](assets/en/52.webp)

Cliccando _Send_, infatti, compare la schermata per l'invio della transazione, che è uguale a quella appena vista ma senza passare dal coin control.

Anche in questo secondo esempio ho deciso di selezionare _Custom transaction_ e di mandare tutto l'importo, ma avrei potuto impostarlo manualmente. Una volta deciso l'importo da inviare premi _Continue_.

![image](assets/en/53.webp)

Successivamente fare sempre caso se le fee sono sottratte dall'UTXO in questione (in questo esempio la scelta è obbligata, perché ce n'è solo uno), regolare manualmente le fee in base alla situazione del momento in mempool e premere _Continue_.

![image](assets/en/54.webp)

Se la schermata di riepilogo è soddisfacente, scegliere _Confirm and create transaction_.

![image](assets/en/55.webp)

Firmare la transazione con _Sign_

![image](assets/en/56.webp)

e propagarla alla rete.

![image](assets/en/57.webp)

Il wallet si trova a questo punto col saldo a zero e la history in aggiornamento.

![image](assets/en/58.webp)

## Creazione di un "Hot wallet"

Per ultimo e per non tralasciare nulla delle fasi iniziali di Nunchuk mobile, vediamo come questo crea quello che l'app chiama "Hot wallet".

Nel menu _Home_ di Nunchuk, dove compare la lista dei wallet, cliccare il `+` in alto a destra.

![image](assets/en/59.webp)

Scegliere _Hot wallet_ tra le opzioni

![image](assets/en/60.webp)

Nunchuk dispensa qualche consiglio sulla gestione degli hot wallet nella pagina di presentazione, dove selezionerai _Continue_ per procedere.

![image](assets/en/61.webp)

Dopo qualche istante il wallet è creato e compare nella lista in colore marroncino. Questo è il colore con cui Nunchuk avvisa che non hai ancora fatto il backup del wallet.

![image](assets/en/62.webp)

Clicca sul nome del wallet, per accedere alle sue configurazioni e potrai notare un invito ad eseguire subito il backup della frase mnemonica.

![image](assets/en/63.webp)

La procedura è la stessa che abbiamo visto in precedenza, quindi non staremo a ripeterla. Una volta terminata, Nunchuk ti porterà alla pagina della relativa chiave, che potrai editare come quella che hai creato con la procedura _Custom_.

![image](assets/en/64.webp)

Prova anche _Run health check_

![image](assets/en/65.webp)

o a vedere come visualizzare tutti i tuoi wallet nella _Home_ della app.

![image](assets/en/66.webp)

## Da tenere a mente per proseguire in autonomia
Così come c'è un ordine per la creazione, ovvero prima la generazione delle chiavi e poi del wallet, dovrai mantenere l'ordine inverso per la cancellare questi elementi dalla tua app.

Se hai l'esigenza di eliminare una delle chiavi, dovrai prima avere l'accortezza di cancellare il wallet, oppure i wallet, che impiegano una delle chiavi per la firma per le transazioni: prima si cancellano i wallet e solo dopo le chiavi. Se non seguirai quest'ordine, ti ritroverai nell'impossibilità di rimuovere la chiave.

Ora che sai come partire con Nunchuk, puoi continuare a studiare questa app e scoprirne i segreti. In questo tutorial abbiamo soltanto mosso i primi passi, ma ci sono applicazioni più sofisticate ed esigenze evolute che questo software wallet può aiutarti a soddisfare.

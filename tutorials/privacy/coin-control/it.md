---
name: Coin Control
description: Scopri Coin Control, uno strumento fondamentale per proteggere la tua privacy su Bitcoin
---
![cover](assets/cover.webp)

*Questo tutorial è importato da [una lezione di Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*

## Introduzione

La solidità del protocollo Bitcoin è garantita da concetti cardine semplici. Tra questi, spicca la trasparenza: tutte le transazioni Bitcoin sono pubbliche e facilmente verificabili da chiunque. Sebbene questa caratteristica sia una pietra miliare del protocollo, perché previene frodi e garantisce la genuinità dei fondi, può rappresentare anche una sfida per la confidenzialità. **Ti sei domandato se tanta trasparenza può inficiare la tua privacy?**

Dovresti farlo. Se da una parte accumulare satoshi non-kyc è piuttosto semplice, la tua privacy è maggiormente a rischio proprio nella fase si spesa.

### Cosa succede quando spendi un UTXO

Spendere Bitcoin non è semplicemente il trasferimento di valore a qualcun altro. 

Consumando uno dei tuoi UTXO, devi infatti soddisfare le condizioni imposte per la trasparenza del protocollo, perché hai l'obbligo di dimostrare che sei proprietario di quei fondi. Ti fai pertanto carico di :
- esporre la tua chiave pubblica;
- produrre una firma digitale.

Il momento della spesa è dunque il più critico: **spendere bitcoin è un atto da compiere in maniera consapevole e con il maggior controllo possibile**.

## Coin Control

Nel protocollo Bitcoin, elementi come _conto_ o _unità monetarie_ non esistono. Il concetto di UTXO è spiegato egregiamente nel seguente corso che ti consiglio vivamente:

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Con Bitcoin ciò che accumuli e in seguito spenderai, sono piccole o grandi unità di conto misurate in satoshi, rappresentati da `output di transazione non spesi`, gli **UTXO**, detti anche `coins`. Quando si utilizzano UTXO per creare una transazione, questi vengono completamente distrutti e si creano altri UTXO al loro posto.

I software wallet sono sviluppati per fare questa scelta in maniera automatica, utilizzando coins selezionate in maniera "casuale", adottando alcuni algoritmi previsti dal protocollo. L'unico criterio che questi algoritmi soddisfano, è quello di coprire l'importo necessario alla spesa. 

Possono mischiare tra loro UTXO di diversa età, oppure privilegiare la spesa del più recente o più "anziano", a seconda dell'algoritmo scelto dagli sviluppatori. I migliori software wallet, prevedono anche di lasciare all'utente una scelta importante.

Il `Coin Control`manuale, che puoi trovare anche denominato `Coin Selection`, è una funzione caratteristica di alcuni software wallet, che ti permette di **selezionare manualmente gli UTXO da spendere quando costruisci la tua transazione**.

Supponiamo di avere un wallet con 3 UTXO, rispettivamente da 21.000, 42.000 e 63.000 satoshi.

![img](assets/en/01.webp)

Se devi spendere 24.000 sats e lasci fare la selezione automatica a un algoritmo, un buon software wallet potrebbe scegliere di combinare l'UTXO 1 + l'UTXO 2 per pagare i 24k sats e le fee del miner, creando un resto che torna su un indirizzo interno del wallet di partenza.

![img](assets/en/02.webp)

Dopo la transazione la nuova situazione nel wallet, contando solo gli UTXO, si può così riassumere.

![img](assets/en/03.webp)

Con il giusto software e la tua consapevolezza, invece, avresti potuto compiere una scelta diversa, per certi versi più corretta. Ad esempio selezionando solo l'UTXO2 (da 42.000 sats).

![img](assets/en/04.webp)

Con una situazione finale nel tuo wallet, a livello di UTXO, che ha un aspetto differente da prima.

![img](assets/en/05.webp)

## Perché il coin control manuale?

![img](assets/en/06.webp)

Nei due esempi precedenti, il saldo è di fatto lo stesso `108.280 sats`. Dopo la spesa di 24.000 sats, senza selezione manuale avremmo 2 UTXO nel wallet; con il coin control manuale ne abbiamo 3 totali.

La domanda che ci potremmo porre è la seguente: **perché fare tutto questo?** Ci sono, o potrebbero esserci, diversi motivi per cui non abbiamo usato l'`UTXO1` **e sono tutti alla base del perché - in fase di spesa - attivare il coin control manuale è una delle buone pratiche da seguire**.

Selezionare gli UTXO permette di privilegiare alcuni aspetti, rispetto ad altri. La scelta dipende proprio dagli obiettivi che vuoi raggiungere.

### Privacy

Uno dei vantaggi principali, quando si parla di coin control manuale, è una **maggiore privacy per chi spende**. Prendiamo sempre il nostro esempio: la spesa di 24.000 satoshi _senza manual coin selection_. Essendo la blockchain di Bitcoin un registro pubblico, un osservatore esterno può dichiarare, senza ombra di dubbio, che gli input `UTXO1 di 21.000 sats` e `UTXO2 di 42.000 sats`, nonché il resto, l'`UTXO5 da 38.280 sats` **appartengono tutti e tre allo stesso utente**.

Selezionando manualmente l'`UTXO2`, invece, rimane completamente riservato l'`UTXO1`, fermo nell'UTXO set in attesa di essere speso in un momento più appropriato.

L'`UTXO1` potrebbe provenire da una fonte KYC, ad esempio un pagamento ricevuto in cambio di beni e servizi, mentre gli altri UTXO no. Mischiare un UTXO-kyc con altri più riservati, compromette l'anonimity set dei fondi non-kyc.

**I fondi KYC porterebbero inevitabilmente a risalire all'identità del pagante. Se fosse il tuo wallet, vorresti che un osservatore esterno possa risalire alla tua identità con una certezza così assoluta?** 

Prova allora a considerare che i wallet che implementano la selezione manuale degli UTXO, permettono ad esempio la **segregazione di uno o più UTXO**, una funzione da utilizzare quando si presentano situazioni di questo tipo.

Sebbene io sia convinta che fondi KYC dovrebbero essere conservati in un wallet separato rispetto a bitcoin acquistati senza kyc, se questo è il tuo caso la segregazione di alcuni tuoi indirizzi è un aiuto fondamentale, che potresti sfruttare imparando a selezionare manualmente i tuoi input di spesa.

### Risparmio sulle fee

Selezionare l'UTXO corretto per effettuare una spesa, **consente di ottimizzare le fee**. Sempre partendo dal nostro esempio iniziale, il software wallet ha selezionato due UTXO per coprire la spesa da fare. Due UTXO implicano due firme da mostrare alla rete. Ne consegue che la transazione ha un "peso" maggiore in termini di vByte.

Usando il coin control manuale, invece, puoi selezionarne uno solo che sia sufficiente a coprire l'importo, risparmiando fee diminuendo il "peso" della transazione.

In periodi in cui le fee sono alte, ma sei costretto a spendere bitcoin on-chain (ad esempio per aprire un canale Lightning Network), ecco che il coin control si rivela il giusto incentivo economico a cui ricorrere.

### Aggregazione dei resti

Quando si fa un pagamento e si usano Bitcoin on-chain, la possibilità di ricevere un resto diventa quasi sempre una certezza. Ogni resto è di per sé una piccola perdita di privacy, in quanto svela alla rete (e sopratutto al destinatario del pagamento) un tuo indirizzo che si può associare al tuo input di partenza.

Considerando che i migliori wallet HD generano degli indirizzi appositi per i resti, puoi riconoscerli facilmente e "segregare" tutti i resti delle varie transazioni effettuate; quando questi hanno raggiunto un certo importo puoi selezionarli manualmente e consolidarli, o fare swap su Lightning Network (il mio metodo preferito) e trattarli così da riguadagnare la privacy perduta in fase di spesa.

### Spesa da un cold wallet

Il cold wallet è uno strumento con cui si può ragionevolmente ottenere un buon grado di sicurezza, per conservare una qualsiasi quantità di fondi da tenere da parte per un lungo periodo di tempo. Possono però capitare degli imprevisti, per cui si presenta la necessità di mettere mano ai risparmi e far fronte a qualche spesa inaspettata.

Non so quanti possono condividere il mio approccio, ma il mio consiglio è quello di **non effettuare mai la spesa direttamente dal cold wallet, per evitare di ricevere il resto tra gli indirizzi dello stesso**. Impara a selezionare manualmente gli UTXO necessari a coprire la spesa, trasferiscili su un wallet hot e prepara la tua transazione da quest'ultimo. L'eventuale resto, poi, potrai rimandarlo su un indirizzo del cold wallet (se l'importo è adeguato), utilizzarlo per altre spese, oppure ancora segregarlo come abbiamo appena visto.

## Presentazione pratica
Dopo l'introduzione tecnica dei `perché`, vediamo come mettere in pratica il coin control manuale con diversi software, desktop e mobile. Useremo sempre lo stesso wallet BIP39, importato in ognuno degli strumenti scelti, in modo da mostrarti le piccole differenze che ci sono tra di loro.

## Wallet Desktop

### Sparrow

Se usi Sparrow, apri il tuo wallet e seleziona _UTXOs_ dal menu a sinistra. Ti comparirà la lista dei tutti gli UTXO associati al tuo wallet.

Clicca semplicemente con il mouse su uno di loro e poi scegli _Send Selected_. Sparrow ti mostra anche il totale disponibile per la spesa dopo la selezione, proprio accanto al comando. Graficamente Sparrow ti mostra l'UTXO selezionato evidenziandolo in blu.

![img](assets/en/07.webp)

Puoi anche selezionarne più di uno. Aiutati con il tasto _CTRL_ per selezionare UTXO non adiacenti nella lista.

![img](assets/en/08.webp)

Dopo aver selezionato manualmente gli UTXO, puoi iniziare a costruire la transazione e Sparrow ti mostrerà bene, graficamente, come è costituita.

![img](assets/en/09.webp)

#### Segregazione dell'UTXO

Segregare dei fondi significa "bloccarli" all'interno del wallet, affinché non possano essere usati come input di una transazione. Sparrow permette questa funzionalità, cui si accede sempre dal menu _UTXOs_: si posiziona il mouse sull'UTXO da "bloccare" e si clicca il tasto destro del mouse. Tra le funzionalità di questa procedura comparirà  _Freeze UTXO_. È così che potrai segregare le coin con Sparrow Wallet.

![img](assets/en/29.webp)

### Electrum

Se il tuo wallet desktop è Electrum, devi sapere che puoi selezionare manualmente gli UTXO sia dal menu _Addresses_ sia dal menu _Coins_. In entrambi i menu la selezione avviene puntando il mouse sull'UTXO desiderato e scegliendo _Add to coin control_ dopo aver cliccato il tasto destro.

![img](assets/en/10.webp)

Anche con questo software puoi selezionare più di un UTXO, aiutandoti con il tasto _CTRL_ della tastiera se non sono adiacenti tra loro.

![img](assets/en/11.webp)

Graficamente Electrum ti mostrerà la selezione evidenziando in verde gli UTXO selezionati, mentre in basso ti compare una barra, evidenziata dello stesso colore, che mostra il saldo disponibile dopo il coin control.

![img](assets/en/12.webp)

Una volta selezionato l'output, o gli output, puoi costruire la tua transazione come fai solitamente dal menu _Send_.

#### Segregazione dell'UTXO

Electrum mette a disposizione questa funzionalità, andando nel menu _Coins_, dove si andrà a selezionare un determinato UTXO e poi scegliendo _Freeze_ con un click del tasto destro del mouse. Si può "freezare" l'indirizzo anche senza fondi dal menu _Addresses_, oppure la "coin" per non spenderla.

![img](assets/en/28.webp)

### Nunchuk

Nunchuk consente di selezionare manualmente gli UTXO dal menu principale, una volta aperto. Lancia Nunchuk e clicca _View coins_.

![img](assets/en/13.webp)

Si apre la finestra che contiene tutti gli UTXO del tuo wallet, dove puoi selezionarne uno o più, attivando la spunta accanto ad ogni importo. Dopo aver effettuato la selezione, continua con _Create transaction_.

![img](assets/en/14.webp)

Dopodiché potrai inserire l'indirizzo di destinazione e impostare l'importo e le fee.

![img](assets/en/15.webp)

#### Segregazione dell'UTXO

Per completezza, anche Nunchuk permette tra le sue funzionalità, di segregare uno (o più) UTXO e lo fa con due modalità differenti. Accedi al menu _View coins_ e scegli manualmente nell'elenco delle coins. Poi clicca il menu _More_ in basso a destra: ti comparirà un elenco di opzioni, tra cui puoi scegliere _Lock coins_.

![img](assets/en/39.webp)

![img](assets/en/40.webp)

Puoi anche cliccare nello spazio riservato all'UTXO, per accedere alla finestra _Coin details_. Qui compare in alto a destra il comando per bloccare/sbloccare l'UTXO in questione.

![img](assets/en/41.webp)

### Blockstream App

Blockstream App desktop, precedentemente conosciuto come Green, permette di fare coin selection quando si è già iniziata a costruire la transazione. Apri pertanto il tuo wallet e clicca su _Send_.

![img](assets/en/16.webp)

Incolla l'indirizzo di destinazione nel campo apposito e poi seleziona _Manual coin selection_.

![img](assets/en/17.webp)

Si apre la finestra dove puoi selezionare uno o più UTXO. Nell'esempio che segue, abbiamo selezionato due coins. Dopodiché conferma la scelta cliccando su _Confirm Coin Selection_.

![img](assets/en/18.webp)

Imposta l'importo e le fee e poi procedi normalmente con la tua transazione.

![img](assets/en/19.webp)

⚠️ N.B. Nel menu _Coins_ di Green sono presenti le voci _Lock_/_Unlock_ che prefigurano la possibilità di segregare UTXO. Questa funzionalità è attivabile solo negli account cosiddetti multisig; inoltre si attiva solo selezionando UTXO di importo molto piccolo, vicino alla soglia del `Dust`.

## Wallet mobile

Anche da mobile è possibile scegliere wallet che permettono di selezionare manualmente gli UTXO. Vediamo Blue Wallet come primo esempio.

### Blue Wallet

Se sei un utente di questo wallet, aprilo e clicca per entrare nelle schermate dei comandi relativi ad uno dei tuoi wallet. Per accedere al coin control manuale si deve entrare nella fase di spesa, quindi clicca _Send_.

![img](assets/en/21.webp)

Nella successiva schermata scegli i menu segnalati dai tre pallini in alto a destra. Si apre una finestra a tendina con una serie di comandi. Scegli l'ultimo: _Coin Control_.

![img](assets/en/22.webp)

A questo punto Blue Wallet mostra tutti i tuoi UTXO. Oltre che dagli importi, sono differenziati graficamente da colori diversi.

![img](assets/en/27.webp)

Scegli l'UTXO da selezionare dopodiché seleziona _Use Coin_.

![img](assets/en/23.webp)

Blue Wallet ti riporta nella finestra di _Send_ per continuare a costruire la transazione. Aggiusta l'importo e le fee, dopodiché scegli _Next_.

![img](assets/en/24.webp)

A questo punto puoi terminare la transazione, come fai di solito.

#### Segregazione di un UTXO

Anche Blue Wallet permette di segregare gli UTXO, rendendoli non disponibili per la spesa il che non è male come funzione per un wallet da dispositivo mobile. Si accede al coin control con la procedura appena spiegata e, dopo aver selezionato l'UTXO, scegli _Freeze_ al posto di _Use Coin_.

![img](assets/en/26.webp)

### Nunchuk

Anche la versione mobile di Nunchuk prevede la possibilità per l'utente di effettuare il coin control. Se usi questa app da mobile, aprilo e vai nel menu _Wallet_. Da qui scegli _View coins_.

![img](assets/en/30.webp)

Nella finestra dove compare la lista degli UTXO clicca _Select_.

![img](assets/en/38.webp)

Accanto ad ogni UTXO appare la funzione di selezione. Come nella versione desktop, anche su Nunchuk mobile la selezione manuale avviene spuntando il quadratino accanto all'importo. La schermata riporta il numero di UTXO selezionati e l'importo totale a disposizione. Una volta finito, clicca il simbolo ₿ in basso a sinistra, che è il comando per iniziare a costruire la transazione.

![img](assets/en/31.webp)

Ora puoi completare la transazione, scegliendo l'importo e cliccando su _Continue_.

![img](assets/en/32.webp)

Continua come fai sempre, incollando un indirizzo di destinazione, una descrizione e personalizzando le impostazioni delle fee.

#### Segregazione dell'UTXO

Si può segregare gli UTXO anche con Nunchuk mobile. Accedi alla finestra dedicata all'elenco delle coins e seleziona la freccia accanto all'UTXO che vuoi segregare.

![img](assets/en/42.webp)

Ti comparirà lo spazio riservato al _Coin details_, dove puoi selezionare _Lock this coin_.

![img](assets/en/43.webp)

### Bitcoin Keeper

Bitcoin Keeper è l'ultimo wallet che vedremo in questa guida. Vediamo la sua funzionalità applicata al coin control con un wallet single-sig, anche se un tale uso  non è lo scopo di questa app molto particolare. Dopo aver impostato Keeper sul tuo telefono, lancialo e apri un wallet contenente alcuni fondi. Al centro della schermata principale clicca _View All Coins_.

![img](assets/en/34.webp)

Keeper mostra una panoramica degli UTXO. Per accedere alla schermata di selezione clicca _Select To Send_.

![img](assets/en/35.webp)

Puoi selezionare le coins, spuntandole, cliccando sull'apposito comando. Al termine, clicca _Send_.

![img](assets/en/36.webp)

Bitcoin Keeper ti porta direttamente al menu _Send_, dove puoi costruire la transazione con gli UTXO selezionati.

![img](assets/en/37.webp)

## Hardware wallet

Ognuno dei software wallet visti in questa guida può essere l'interfaccia watch-only di un tuo hardware wallet. Significa il coin control per dispositivo di firma offline si esegue con i passaggi visti fin qui.

### Raccomandazioni generali

Il coin control è una pratica molto efficace per selezionare gli input delle tue transazioni. La selezione manuale è ancor più efficiente se, in fase di acquisto/ricezione dei tuoi fondi, hai etichettato bene la provenienza dei tuoi satoshi. Se desideri imparare bene questa tecnica, ti consiglio il seguente tutorial:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Abbiamo parlato in precedenza della `segregazione dei resti`. Se vuoi bloccare i resti per poi trattarli e riguadagnare privacy (swap su layer 2), devi aver cura di "etichettarli" ogni volta che ne ricevi uno. Dei software wallet visti fin qui, solo Electrum colora graficamente gli UTXO di resto per renderli visibili a colpo d'occhio. Altri, come Sparrow, ti indicano la catena nel derivation path del singolo UTXO (`m/84'/0'/0'/1/11`). 

Per applicare efficacemente questa tecnica, ricordati di aggiungere sempre una descrizione sul resto ricevuto: la persona a cui hai mandato i tuoi fondi (un pagamento, un'esercitazione o altro), conosce l'indirizzo associato al resto e sa che appartiene a te, in quanto proviene della transazione fatta insieme!

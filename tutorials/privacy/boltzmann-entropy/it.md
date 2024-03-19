---
name: Boltzmann Calculator
description: Comprendere il concetto di entropia e come utilizzare Boltzmann
---
![cover](assets/cover.jpeg)

Il Boltzmann Calculator è uno strumento per analizzare una transazione Bitcoin misurando il suo livello di entropia insieme ad altre metriche avanzate. Fornisce approfondimenti sulle connessioni tra gli input e gli output di una transazione. Questi indicatori offrono una valutazione quantificata della privacy di una transazione e aiutano a identificare potenziali errori.

Questo strumento Python è stato sviluppato dai team di Samourai Wallet e OXT, ma può essere utilizzato su qualsiasi transazione Bitcoin.

## Come utilizzare il Boltzmann Calculator?
Per utilizzare il Boltzmann Calculator, sono disponibili due opzioni. La prima è installare direttamente sulla propria macchina lo [strumento Python](https://code.samourai.io/oxt/boltzmann). In alternativa, è possibile optare per il sito web [KYCP.org](https://kycp.org/#/) (_Know Your Coin Privacy_), che offre una piattaforma di utilizzo semplificata. Per gli utenti di [RoninDojo](https://planb.network/tutorials/node/ronin-dojo-v2), si noti che questo strumento è già integrato nel vostro nodo.

Utilizzare il sito KYCP è piuttosto semplice: basta inserire l'identificativo della transazione (TXID) che si desidera analizzare nella barra di ricerca e premere `INVIO`.
![KYCP](assets/1.webp)
Si troveranno quindi diverse informazioni sulla transazione, inclusi i collegamenti tra gli input e gli output. Cliccare su `collegamenti deterministici`.
![KYCP](assets/2.webp)
Si arriverà alla pagina dedicata agli indicatori del Boltzmann Calculator.
![KYCP](assets/3.webp)
Per coloro che preferiscono utilizzare lo strumento direttamente dal proprio nodo RoninDojo, è accessibile tramite `RoninCLI > Samourai Toolkit > Boltzmann Calculator`.

Per l'uso locale sul proprio computer, sono disponibili istruzioni specifiche per il proprio sistema a questo indirizzo: [https://code.samourai.io/oxt/boltzmann](https://code.samourai.io/oxt/boltzmann)

Come per il sito KYCP.org, una volta installato lo strumento Python, sarà sufficiente incollare il TXID della transazione che si desidera analizzare.

![KYCP](assets/7.webp)

Quindi, premere il tasto `INVIO` per ottenere i risultati.

![KYCP](assets/8.webp)

## Quali sono gli indicatori del Boltzmann Calculator?
### Combinazioni / Interpretazioni:
Il primo indicatore che il software calcola è il numero totale di combinazioni possibili, indicato sotto `nb combinations` o `interpretations` nello strumento.

Tenendo conto dei valori degli UTXO coinvolti nella transazione, questo indicatore calcola il numero di modi in cui gli input possono essere associati agli output. In altre parole, determina il numero di interpretazioni plausibili che una transazione può suscitare dal punto di vista di un osservatore esterno che la analizza.
Ad esempio, un coinjoin strutturato secondo il modello Whirlpool 5x5 presenta `1.496` combinazioni possibili: ![KYCP](assets/4.webp)
Un coinjoin Whirlpool Surge Cycle 7x7, d'altra parte, presenta `9.934.563` interpretazioni possibili: ![KYCP](assets/5.webp)
Al contrario, una transazione più tradizionale con 1 input e 2 output presenterà una sola interpretazione: ![KYCP](assets/6.webp)

### Entropia:
Il secondo indicatore calcolato è l'entropia di una transazione, designata da `Entropia`.
Nel contesto generale della crittografia e dell'informazione, l'entropia è una misura quantitativa dell'incertezza o dell'imprevedibilità associata a una fonte di dati o a un processo casuale. In altre parole, l'entropia è un modo di misurare quanto sia difficile prevedere o indovinare le informazioni.

Nel contesto specifico dell'analisi delle catene, l'entropia è anche il nome di un indicatore, derivato dall'entropia di Shannon e [inventato da LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), che viene calcolato con lo strumento Boltzmann.

Quando una transazione presenta un alto numero di combinazioni possibili, è spesso più rilevante riferirsi alla sua entropia. Questo indicatore permette di misurare la mancanza di conoscenza degli analisti sulla configurazione esatta della transazione. In altre parole, più alta è l'entropia, più difficile diventa per gli analisti il compito di identificare i movimenti di bitcoin tra input e output.

In pratica, l'entropia rivela se, dal punto di vista di un osservatore esterno, una transazione presenta molteplici interpretazioni possibili, basandosi unicamente sulle quantità di input e output, senza considerare altri schemi e euristiche esterni o interni. Un'alta entropia è quindi sinonimo di maggiore riservatezza per la transazione.

L'entropia è definita come il logaritmo binario del numero di combinazioni possibili. Ecco la formula utilizzata:
```
E: l'entropia della transazione
C: il numero di combinazioni possibili per la transazione

E = log2(C)
```

In matematica, il logaritmo binario (logaritmo in base 2) corrisponde all'operazione inversa dell'elevamento a potenza di 2. In altre parole, il logaritmo binario di `x` è l'esponente al quale `2` deve essere elevato per ottenere `x`. Questo indicatore è quindi espresso in bit.

Prendiamo l'esempio del calcolo dell'entropia per una transazione coinjoin strutturata secondo il modello Whirlpool 5x5, che, come accennato in precedenza, offre un numero di combinazioni possibili di `1,496`:
```
C = 1,496
E = log2(1,496)
E = 10.5469 bit
```
Quindi, questa transazione coinjoin mostra un'entropia di `10.5469 bit`, che è considerata molto soddisfacente. Più alto è questo valore, più diverse interpretazioni ammette la transazione, rafforzando così il suo livello di privacy.
Per una transazione coinjoin 7x7 che presenta `9,934,563` interpretazioni, l'entropia sarebbe:
```
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bit
```

Prendiamo un altro esempio con una transazione più convenzionale, con un input e due output: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) Nel caso di questa transazione, l'unica interpretazione possibile è: `(In.0) > (Out.0 ; Out.1)`. Di conseguenza, la sua entropia è stabilita a `0`:
```
C = 1
E = log2(1)
E = 0 bit
```

### Efficienza:
Il terzo indicatore fornito dal Calcolatore Boltzmann è denominato `Efficienza del Portafoglio`. Questo indicatore valuta l'efficienza della transazione confrontandola con la transazione ottimale concepibile in una configurazione identica.
Questo ci porta a discutere il concetto di entropia massima, che corrisponde all'entropia più alta che una specifica struttura di transazione potrebbe teoricamente raggiungere. L'efficienza della transazione viene quindi calcolata confrontando questa entropia massima con l'entropia effettiva della transazione analizzata.
La formula utilizzata è la seguente:
```
ER: l'entropia effettiva della transazione espressa in bit
EM: l'entropia massima possibile per una data struttura di transazione espressa in bit
Ef: l'efficienza della transazione in bit

Ef = ER - EM
```

Per esempio, per una struttura di coinjoin di tipo Whirlpool 5x5, l'entropia massima è impostata a `10.5469`:
```
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bit
```

Questo indicatore è espresso anche in percentuale, la cui formula è quindi:
```
CR: il numero effettivo di combinazioni possibili
CM: il numero massimo di combinazioni possibili con la stessa struttura
Ef: l'efficienza espressa in percentuale

Ef = CR / CM
Ef = 1.496 / 1.496
Ef = 100%
```

Un'efficienza del `100%` indica quindi che la transazione massimizza il suo potenziale di privacy secondo la sua struttura.

### Densità di Entropia:
Il quarto indicatore è la densità di entropia, indicata nello strumento come `Densità di Entropia`. Fornisce una prospettiva sull'entropia relativa a ciascun input o output della transazione. Questo indicatore si rivela utile per valutare e confrontare l'efficienza di transazioni di dimensioni diverse. Per calcolarlo, basta dividere l'entropia totale della transazione per il numero totale di input e output coinvolti:
```
ED: la densità di entropia espressa in bit
E: l'entropia della transazione espressa in bit
T: il numero totale di input e output nella transazione

ED = E / T
```

Prendiamo l'esempio di un coinjoin Whirlpool 5x5:
```
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bit
```

Calcoliamo anche la densità di entropia per un coinjoin Whirlpool 7x7:
```
T = 7 + 7 = 14
E = 23.244
ED = 23.244 / 14 = 1.66 bit
```

### Punteggio di Boltzmann:
Il quinto elemento di informazione fornito dal Calcolatore di Boltzmann è la tabella delle probabilità di corrispondenza tra gli input e gli output. Questa tabella indica, attraverso il punteggio di Boltzmann, la probabilità condizionale che un specifico input sia correlato a un dato output.

Si tratta quindi di una misura quantitativa della probabilità condizionale che un'associazione tra un input e un output in una transazione si verifichi, basata sul rapporto tra il numero di occorrenze favorevoli di questo evento e il numero totale di occorrenze possibili, in un insieme di interpretazioni.

Prendendo di nuovo l'esempio di un coinjoin Whirlpool, la tabella delle probabilità condizionali evidenzierebbe le possibilità di collegamento tra ciascun input e output, fornendo una misura quantitativa dell'ambiguità delle associazioni nella transazione:

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
Qui, possiamo chiaramente vedere che ogni input ha la stessa probabilità di essere associato a qualsiasi output, il che aumenta la confidenzialità della transazione.
Il calcolo del punteggio di Boltzmann prevede la divisione del numero di interpretazioni in cui si verifica un certo evento per il numero totale di interpretazioni disponibili. Pertanto, per determinare il punteggio che associa l'input numero 0 all'output numero 3 (`512` interpretazioni), si utilizza la seguente procedura:
```
Interpretazioni (IN.0 > OUT.3) = 512
Interpretazioni Totali = 1496
Punteggio = 512 / 1496 = 34%
```

Prendendo l'esempio di un coinjoin Whirlpool 7x7 (ciclo di surge), la tabella di Boltzmann sarebbe così:

|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Tuttavia, nel caso di una semplice transazione con un singolo input e due output, la situazione è diversa:

| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |
Qui, si osserva che la probabilità che ciascun output provenga dall'input n. 0 è del `100%`. Una probabilità inferiore si traduce quindi in una maggiore privacy, diluendo i collegamenti diretti tra input e output.

### Collegamenti Deterministici:
La sesta informazione fornita è il numero di collegamenti deterministici, completato dal rapporto di questi collegamenti. Questo indicatore rivela quanti collegamenti tra gli input e gli output nella transazione analizzata sono indiscutibili, con una probabilità del `100%`. Il rapporto, d'altra parte, offre una prospettiva sul peso di questi collegamenti deterministici all'interno dell'intero insieme di collegamenti della transazione.
Per esempio, una transazione di tipo Whirlpool coinjoin non ha collegamenti deterministici e, quindi, mostra un indicatore e un rapporto del `0%`. Al contrario, nella nostra seconda semplice transazione esaminata (con un input e due output), l'indicatore è impostato a `2` e il rapporto raggiunge il `100%`. Così, un indicatore nullo segnala un'eccellente confidenzialità a causa dell'assenza di collegamenti diretti e indiscutibili tra input e output.

**Risorse Esterne:**

- [Codice Boltzmann su Samourai](https://code.samourai.io/oxt/boltzmann) 
- [Transazioni Bitcoin & Privacy (Parte I) di Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Transazioni Bitcoin & Privacy (Parte II) di Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Transazioni Bitcoin & Privacy (Parte III) di Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- [Sito Web KYCP](https://kycp.org/#/)
- [Articolo su Medium sull'Introduzione allo Script Boltzmann di Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
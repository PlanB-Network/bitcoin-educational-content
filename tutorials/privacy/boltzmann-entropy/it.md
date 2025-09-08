---
name: Boltzmann Calculator
description: Comprendere il concetto di entropia utilizzando il Boltzmann Calculator.
---
![cover](assets/cover.webp)

***ATTENZIONE:** In seguito all'arresto dei fondatori di Samourai Wallet e al sequestro dei relativi server, avvenuto il 24 aprile 2024, il sito web KYCP.org non è attualmente accessibile. Anche il repository GitLab che ospitava il codice del Boltzmann Calculator in Python è stato sequestrato. Al momento, non è più possibile scaricare lo strumento. Tuttavia, è probabile che il codice venga ripubblicato da altri prossimamente.
Nel frattempo, puoi comunque trarre beneficio da questo tutorial per comprendere il funzionamento del Boltzmann Calculator. Gli indicatori forniti dallo strumento sono applicabili a qualsiasi transazione Bitcoin e possono anche essere calcolati manualmente. Tutti i passaggi necessari sono illustrati in questo tutorial. Se hai già scaricato lo strumento Python sul tuo computer, o se utilizzi un nodo RoninDojo, puoi continuare a usarlo normalmente seguendo le istruzioni contenute qui.*

_Stiamo seguendo da vicino l'evoluzione di questo caso così come gli sviluppi relativi agli strumenti associati. Siate certi che aggiorneremo questo tutorial non appena saranno disponibili nuove informazioni._

_Questo materiale è fornito esclusivamente a scopo educativo e informativo. Non approviamo né incoraggiamo l’uso di questi strumenti per finalità illecite. È responsabilità di ciascun utente rispettare le leggi vigenti nella propria giurisdizione._

---

Il **Boltzmann Calculator** è uno strumento pensato per analizzare una transazione Bitcoin, misurandone il livello di **entropia** e altre metriche avanzate.  
Fornisce una panoramica dettagliata delle connessioni tra input e output, offrendo una valutazione quantitativa del livello di **privacy** della transazione ed evidenziando eventuali errori di struttura.

Sviluppato dal team di Samourai Wallet e OXT, questo strumento Python può essere utilizzato per analizzare qualsiasi transazione Bitcoin, indipendentemente dal wallet utilizzato.

## Come utilizzare il Boltzmann Calculator?
Per utilizzare il Boltzmann Calculator sono disponibili due opzioni. La prima consiste nell’installarlo direttamente sul proprio dispositivo locale. In alternativa, è possibile utilizzare il sito web KYCP.org (_Know Your Coin Privacy_), che offre una piattaforma di utilizzo semplificata. Per gli utenti di RoninDojo, questo strumento è già integrato nel nodo.

Utilizzare il sito KYCP.org è piuttosto semplice: basta inserire l’identificativo della transazione (TXID) che si desidera analizzare nella barra di ricerca e premere `INVIO`.
![KYCP](assets/1.webp)
Verranno visualizzate diverse informazioni sulla transazione, inclusi i collegamenti tra input e output. Clicca su `deterministic links`.
![KYCP](assets/2.webp)
Si aprirà la pagina dedicata agli indicatori del Boltzmann Calculator.
![KYCP](assets/3.webp)
Chi preferisce usare lo strumento direttamente dal proprio nodo RoninDojo può trovarlo in RoninCLI > Samourai Toolkit > Boltzmann Calculator. Così come sul sito KYCP.org, dopo aver installato lo strumento Python sarà sufficiente incollare il TXID della transazione da analizzare.

![KYCP](assets/7.webp)
Quindi, premere il tasto `INVIO` per ottenere i risultati.

![KYCP](assets/8.webp)

## Quali sono gli indicatori del Boltzmann Calculator?
### Combinazioni / Interpretazioni:
Il primo indicatore calcolato dal software è il numero totale di combinazioni possibili, mostrato come `nb combinations` o `interpretations`.

Questo valore considera gli importi degli UTXO coinvolti nella transazione e indica in quanti modi gli input possono essere collegati agli output. In pratica, rappresenta il numero di interpretazioni plausibili che un osservatore esterno può fare analizzando la transazione.

Ad esempio, un coinjoin strutturato secondo il modello Whirlpool 5x5 mostra `1.496` combinazioni possibili:  
![KYCP](assets/4.webp)

Un coinjoin Whirlpool Surge Cycle 8x8, invece, presenta `9.934.563` interpretazioni possibili:  
![KYCP](assets/5.webp)

Al contrario, una transazione tradizionale con 1 input e 2 output ha una sola interpretazione possibile:  
![KYCP](assets/6.webp)

### Entropia:
Il secondo indicatore calcolato è l'entropia di una transazione, designata da `Entropy`.
Nel contesto generale della crittografia e dell'informazione, l'entropia è una misura quantitativa dell'incertezza o dell'imprevedibilità associata a una fonte di dati o a un processo casuale. In altre parole, l'entropia misura quanto sia difficile prevedere o indovinare informazioni.
Nel contesto specifico di chain analysis, l'entropia è anche il nome di un indicatore, derivato dall'entropia di Shannon e [inventato da LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), che viene calcolato con lo strumento di Boltzmann.

Quando una transazione presenta un alto numero di possibili combinazioni, si fa riferimento alla sua entropia. Questo indicatore permette di misurare la mancanza di conoscenza degli analisti sulla configurazione esatta della transazione. In altre parole, più alta è l'entropia, più è difficile identificare i movimenti di bitcoin tra input e output.

L’entropia misura dunque, quanto è difficile, per un osservatore esterno, comprendere la struttura reale di una transazione guardando solo il numero e l’importo degli input e degli output, senza usare euristiche o supposizioni aggiuntive.
Una transazione con alta entropia lascia spazio a più interpretazioni possibili e, di conseguenza, garantisce un livello più elevato di privacy.

L'entropia è definita come il logaritmo binario del numero di combinazioni possibili. Ecco la formula utilizzata:
```plaintext
E: l'entropia della transazione
C: il numero di combinazioni possibili per la transazione

E = log2(C)
```

In matematica, il logaritmo binario (logaritmo in base 2) corrisponde all'operazione inversa dell'elevamento a potenza di 2. In altre parole, il logaritmo binario di `x` è l'esponente al quale `2` deve essere elevato per ottenere `x`. Questo indicatore è espresso in bit.

Prendiamo l'esempio del calcolo dell'entropia per una transazione coinjoin strutturata secondo il modello Whirlpool 5x5, che, come accennato in precedenza, offre un numero di combinazioni possibili di `1,496`:
```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bit
```
Quindi, questa transazione coinjoin mostra un'entropia di `10.5469 bit`, che è considerata molto soddisfacente. Più alto è questo valore, maggiori sono le interpretazioni plausibili per la transazione, rafforzando così il suo livello di privacy.
Per una transazione coinjoin 8x8 che presenta `9,934,563` interpretazioni, l'entropia sarebbe:
```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bit
```

Prendiamo un altro esempio con una transazione più convenzionale, con un input e due output: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) 

In questo caso, l'unica interpretazione possibile è: `(In.0) > (Out.0 ; Out.1)`. Di conseguenza, la sua entropia è stabilita a `0`:
```plaintext
C = 1
E = log2(1)
E = 0 bit
```

### Efficienza:
Il terzo indicatore fornito dal Calcolatore Boltzmann è denominato `Wallet Efficiency`. Questo indicatore valuta l'efficienza della transazione confrontandola con la transazione ottimale concepibile in una configurazione identica.
Questo ci porta a discutere il concetto di entropia massima, che corrisponde all'entropia più alta che una specifica struttura di transazione potrebbe teoricamente raggiungere. L'efficienza della transazione viene così calcolata confrontando questa entropia massima con l'entropia effettiva della transazione analizzata.
La formula utilizzata è la seguente:
```plaintext
ER: l'entropia effettiva della transazione espressa in bit
EM: l'entropia massima possibile per una data struttura di transazione espressa in bit
Ef: l'efficienza della transazione in bit

Ef = ER - EM
```

Per esempio, per una struttura di coinjoin di tipo Whirlpool 5x5, l'entropia massima è impostata a `10.5469`:
```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bit
```

Questo indicatore è espresso anche in percentuale, la cui formula è quindi:
```plaintext
CR: il numero effettivo di combinazioni possibili
CM: il numero massimo di combinazioni possibili con la stessa struttura
Ef: l'efficienza espressa in percentuale

Ef = CR / CM
Ef = 1.496 / 1.496
Ef = 100%
```

Un’efficienza del 100% indica che la transazione raggiunge il massimo livello di privacy consentito dalla sua struttura. 

### Densità di Entropia:
Il quarto indicatore è, come indicato nello strumento, la `Entropy Density`. Essa fornisce una prospettiva sull'entropia relativa a ciascun input o output della transazione ed è utile per valutare e confrontare l'efficienza di transazioni di dimensioni diverse. Per calcolarlo, basta dividere l'entropia totale della transazione per il numero totale di input e output coinvolti:
```plaintext
ED: la densità di entropia espressa in bit
E: l'entropia della transazione espressa in bit
T: il numero totale di input e output nella transazione

ED = E / T
```

Prendiamo l'esempio di un coinjoin Whirlpool 5x5:
```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bit
```

Calcoliamo anche la densità di entropia per un coinjoin Whirlpool 8x8:
```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```

### Punteggio di Boltzmann:
Il quinto elemento fornito dal Boltzmann Calculator è la tabella delle probabilità di corrispondenza tra gli input e gli output. Questa tabella indica, attraverso un punteggio, la probabilità condizionale che uno specifico input sia correlato ad un dato output.
Si tratta quindi di una misura quantitativa della possibilità che un'associazione tra un input e un output in una transazione si verifichi, basata sul rapporto tra il numero di casi favorevoli di questo evento e il numero totale di casi possibili, in un insieme di interpretazioni.

Prendendo nuovamente come esempio un coinjoin Whirlpool, la tabella delle probabilità condizionali evidenzia le possibili associazioni tra ciascun input e ciascun output, fornendo una misura quantitativa dell’ambiguità nelle associazioni all’interno della transazione.

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |


Qui, possiamo chiaramente notare che ogni input ha la stessa probabilità di essere associato a qualsiasi output, il che aumenta la privacy della transazione.

Il calcolo del punteggio Boltzmann si basa sul rapporto tra il numero di interpretazioni in cui un determinato evento si verifica e il numero totale di interpretazioni possibili.
Ad esempio, per determinare il punteggio che associa l’input 0 all’output 3, se tale associazione compare in 512 interpretazioni su un totale di 1.496, la procedura sarà la seguente:
```plaintext
Interpretazioni (IN.0 > OUT.3) = 512
Interpretazioni Totali = 1496
Punteggio = 512 / 1496 = 34%
```

Prendendo l'esempio di un coinjoin Whirlpool 8x8 (Surge cycle), la tabella del punteggio Boltzmann sarebbe così:

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


Qui, si osserva che la probabilità che ciascun output provenga dall'input n. 0 è del `100%`. Una probabilità inferiore si traduce quindi in una maggiore privacy, rendendo meno evidenti i collegamenti diretti tra input e output.

### Collegamenti Deterministici:
La sesta informazione fornita è il numero di collegamenti deterministici, accompagnato dal relativo rapporto.
Questo indicatore mostra quanti collegamenti tra input e output nella transazione analizzata sono certi con una probabilità del 100%.
Il rapporto indica invece quale peso questi collegamenti deterministici hanno rispetto al totale dei collegamenti presenti nella transazione.
Ad esempio, una transazione di tipo Whirlpool coinjoin non presenta collegamenti deterministici e quindi mostra un indicatore e un rapporto pari a 0%.
Al contrario, nella nostra seconda transazione semplice esaminata (con un input e due output), l’indicatore è pari a 2 e il rapporto raggiunge il 100%.
Un valore nullo di questo indicatore significa dunque un’elevata privacy, dovuta all’assenza di collegamenti diretti e indiscutibili tra input e output.

**Risorse Esterne:**

- Codice Boltzmann su Samourai
- [Transazioni Bitcoin & Privacy (Parte I) di Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Transazioni Bitcoin & Privacy (Parte II) di Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Transazioni Bitcoin & Privacy (Parte III) di Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- Sito Web KYCP
- [Articolo su Medium sull'Introduzione allo Script Boltzmann di Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)

---
name: Approfondire Simplicity
goal: Padroneggiare la filosofia di design, il sistema di tipi e l'intero ciclo di vita di Simplicity
objectives:
  - Comprendere i tre metodi fondamentali di composizione e i nove combinatori che formano un linguaggio completo
  - Costruire logica booleana, aritmetica e SHA-256 a partire dal sistema di tipi minimale di Simplicity
  - Cogliere come gli effetti collaterali Failure e Reader abilitano l'interazione reale con la blockchain
  - Imparare come i programmi Simplicity diventano indirizzi Taproot e vengono riscattati con dati di witness
---

# Approfondire Simplicity

Un'immersione profonda nella teoria e nelle decisioni di design dietro il linguaggio Simplicity, basata sulla serie completa di cinque articoli ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) di [Dr. Russell O'Connor](https://r6.ca/), il creatore di Simplicity presso Blockstream Research. Questo corso spiega *perché* Simplicity è stato progettato nel modo in cui è stato progettato, non come scriverlo.

Il corso segue gli articoli del Dr. O'Connor attraverso i tre modi fondamentali di combinare computazioni, il sistema di tipi minimale e il suo teorema di completezza, la costruzione di tipi di dati pratici e dell'aritmetica a partire da principi primi, l'accurata introduzione di effetti collaterali per l'interazione con la blockchain, e infine come i programmi vengono impegnati (committed) in indirizzi e riscattati on-chain.

+++

# Introduzione

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Panoramica del corso

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Benvenuti a SCR403 — Approfondire Simplicity!

Questo corso si basa sulla serie di articoli **"Delving Simplicity"** scritta da [Dr. Russell O'Connor](https://r6.ca/), Infrastructure Tech Developer presso [Blockstream](https://blockstream.com/) e creatore di Simplicity. Gli articoli originali sono stati pubblicati sul forum [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) e costituiscono il materiale sorgente principale per questo corso. Siamo grati per il suo lavoro pionieristico, che ha reso possibile questo contenuto educativo.

### Cosa imparerai

Questo corso esplora la filosofia di design e i fondamenti matematici dietro Simplicity, il linguaggio di scripting di nuova generazione attivato sulla [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) nel luglio 2025. Segue la serie completa di cinque articoli ed è strutturato in due sezioni principali di contenuto:

1. **Fondamenta di Simplicity** — Perché la computazione blockchain richiede un linguaggio fondamentalmente diverso, i tre modi per combinare operazioni (sequenziale, parallelo, condizionale) e i nove combinatori fondamentali che formano un linguaggio matematicamente completo
2. **Dai tipi di dati ai programmi** — Costruire logica booleana, aritmetica e SHA-256 a partire da principi primi; comprendere gli effetti collaterali Failure e Reader che abilitano l'interazione con la blockchain; e imparare come i programmi vengono impegnati in indirizzi Taproot tramite Commitment Merkle Root e riscattati con dati di witness

### Prerequisiti

Questo è un corso di livello **esperto** (circa 10 ore). Dovresti avere familiarità con:
- Concetti di base dello scripting Bitcoin (cosa fa la validazione delle transazioni)
- Concetti di programmazione fondamentali (tipi, funzioni, composizione)
- Una certa familiarità con la notazione matematica è utile ma non richiesta. Introduciamo tutto man mano che procediamo

### Risorse chiave

- **Articoli originali**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) del Dr. Russell O'Connor su Delving Bitcoin
- **Repository di Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — codice sorgente e prove formali in Rocq
- **Sito ufficiale**: [simplicity-lang.org](https://simplicity-lang.org/) — documentazione e riferimento SimplicityHL
- **Blog di Blockstream**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — panoramica tecnica

Pronti a immergervi in una delle opere di ingegneria Bitcoin più eleganti? Iniziamo!

## Cos'è Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Se arrivi a questo corso senza un background su Simplicity, questo capitolo ti orienterà prima di tuffarci nel profondo.

### Simplicity in breve

Simplicity è un **linguaggio per smart contract nativo di Bitcoin**, attivo oggi sulla Liquid Network. Immaginato per la prima volta dal Dr. Russell O'Connor intorno al 2012 e descritto in dettaglio nel suo paper del 2017 *Simplicity: A New Language for Blockchains*, è stato attivato sulla Liquid Network nel luglio 2025 dopo anni di verifica formale e sviluppo.

A differenza di Solidity di Ethereum, che è un linguaggio per contratti Turing-completo e ad alto livello, Simplicity è intenzionalmente minimale. Ha:
- **Tre costruttori di tipo** (unit, sum, product)
- **Nove combinatori** (operazioni di base e regole di composizione)
- **Nessun ciclo, nessuna ricorsione, nessuna memoria dinamica**

A partire da queste sole primitive, puoi costruire qualsiasi computazione ti serva per la validazione delle transazioni, dalla logica booleana all'hashing SHA-256 completo.

### Cosa puoi fare con Simplicity oggi?

Simplicity sta già alimentando applicazioni reali sulla Liquid Network. La più nota è il [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), un marketplace di opzioni senza oracoli dove gli utenti scambiano opzioni call su L-BTC usando USDt come collaterale (il contratto sottostante supporta anche le put). Altri progetti Simplicity attivi includono [Swaption](https://swaption.io/) di SideSwap (opzioni) e l'open-source [Deadcat](https://github.com/Resolvr-io/deadcat) di Resolvr (mercati predittivi). Oltre alla DeFi, Simplicity abilita condizioni di spesa avanzate come vault, covenant e schemi multisig complessi che sarebbero impossibili o non sicuri in Bitcoin Script.

### Cos'è questo corso — e cosa non è

Questo **non** è un tutorial di coding pratico. Qui non scriverai programmi Simplicity. Se stai cercando quello, dai un'occhiata a:
- [simplicity-lang.org](https://simplicity-lang.org/) — documentazione ufficiale e il linguaggio ad alto livello SimplicityHL
- Il [repository GitHub di Simplicity](https://github.com/BlockstreamResearch/simplicity) — implementazione di riferimento, esempi e prove Rocq
- Il [post sul blog di Blockstream](https://blog.blockstream.com/en-simplicity-github/) per iniziare

Ciò di cui questo corso **si occupa**: le **scelte filosofiche e tecniche** dietro il design di Simplicity. Perché questo linguaggio è stato creato in questo modo? Perché solo nove combinatori? Perché nessuna ricorsione? Perché è importante che il sistema di tipi si colleghi al calcolo dei sequenti di Gentzen?

Pensatelo come capire **perché il motore è stato costruito in questo modo** piuttosto che imparare a guidare l'auto.

### A chi è rivolto?

Questo corso è ideale per:
- **Sviluppatori di protocollo** che vogliono comprendere le fondamenta di Simplicity prima di scrivere codice
- **Ricercatori Bitcoin** interessati all'approccio di verifica formale e teoria dei tipi
- **Informatici** curiosi della connessione tra calcolo dei sequenti e computazione blockchain
- **Bitcoiner avanzati** che vogliono andare oltre una comprensione superficiale delle capacità di scripting di Liquid

Se termini come "sum type", "combinatori" o "calcolo dei sequenti" sono del tutto nuovi per te, non preoccuparti, spieghiamo tutto da zero. Ma preparati per un viaggio denso e matematico.

### Dagli articoli al corso

La serie originale "Delving Simplicity" del Dr. O'Connor è strutturata in cinque articoli tecnici. Questo corso riorganizza e annota quel materiale in un percorso di apprendimento progressivo con quiz per verificare la tua comprensione lungo il cammino. Le idee, le definizioni e le dimostrazioni sono sue, e noi abbiamo adattato il formato per un'educazione strutturata.

# Fondamenta di Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Modi fondamentali di combinare computazioni

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Ora che Simplicity è stata attivata sulla Liquid Network, vorrei fare un'immersione approfondita nella filosofia e nel design del linguaggio Simplicity.

La validazione delle transazioni di Bitcoin è un'applicazione significativamente diversa dal normale design di linguaggi di programmazione. Lo spazio nei blocchi ha un costo elevato, quindi i programmi devono essere compatti. I programmi nelle transazioni Bitcoin vengono eseguiti solo su un singolo input e tutti eseguono il programma sullo stesso input. Inoltre, l'agente che autorizza la transazione conosce già in anticipo l'esito della computazione: che la transazione è valida.

Tipicamente l'agente che autorizza eseguirà computazioni molto più costose per derivare i dati di witness che attestano la validità della transazione, mentre i programmi eseguiti sulla blockchain devono verificare la validità dei dati di witness. Verificare la validità è spesso molto più economico che dimostrarla.

Abbiamo progettato Simplicity tenendo a mente questo tipo di sfide uniche nel design del linguaggio. Ad esempio, Simplicity richiede che i rami non eseguiti vengano potati (pruned) in modo che non appaiano sulla blockchain. I passaggi di preprocessing sono progettati con cura per esibire una complessità temporale (quasi) lineare rispetto alla dimensione del programma Simplicity. L'analisi statica viene usata al posto del "gas", che non può essere calcolato senza eseguire il codice in un modo prescritto, in modo che i dettagli del modello di esecuzione non diventino critici per il consenso. Nessuna allocazione dinamica di memoria durante l'esecuzione. E così via.

Prima di addentrarmi nei dettagli di design di Simplicity, voglio iniziare questa serie con un po' di filosofia della programmazione riguardo ai modi generali di combinare blocchi costitutivi di base per creare nuove funzionalità.

### Composizione

Supponiamo che si stia progettando un linguaggio per transazioni programmabili per una blockchain come Bitcoin. In particolare, i programmi hanno accesso solo ai dati della transazione e ai dati UTXO degli input, e l'esecuzione determina solo la validità della transazione (il che permette di mettere in cache il risultato dell'esecuzione). Diciamo che si parte da un insieme di operazioni di base che possono svolgere vari compiti come computazioni elementari, lettura e/o elaborazione di dati dalla transazione, e verifica delle firme. Ogni operazione consuma un tipo di input (eventualmente vuoto) e restituisce un tipo di output. Quali sono i modi in cui possiamo combinare queste operazioni di base in operazioni più complesse?

### Composizione sequenziale

![Sequential Composition](assets/en/001.webp)

Il metodo di composizione più fondamentale è la composizione sequenziale. Se abbiamo due operazioni di base, una il cui tipo di dato in output corrisponde al tipo di dato in input dell'altra, allora possiamo combinare queste due operazioni in una nuova operazione composta. Questa nuova operazione esegue le due operazioni di base in sequenza, prendendo come input l'input della prima operazione, passando l'output di quella prima operazione all'input della seconda operazione, e infine restituendo l'output di quella seconda operazione.

Naturalmente, non dobbiamo limitarci a combinare solo operazioni di base. Ora che abbiamo alcune operazioni composte, possiamo combinarle anch'esse usando la composizione funzionale.

In matematica, questa composizione sequenziale viene spesso chiamata semplicemente "composizione", e si potrebbe pensare che questo sia l'unico modo di comporre le cose. Tuttavia, abbiamo altri modi di comporre le operazioni.

### Composizione parallela

![Parallel Composition](assets/en/002.webp)

Supponiamo di avere due operazioni, che possono essere di base o complesse, ed entrambe prendono lo stesso tipo di input. Un secondo modo fondamentale di comporre queste due operazioni è eseguirle entrambe sullo stesso input. Questo viene chiamato composizione parallela, e il tipo dell'output è il "prodotto" dei tipi degli output delle operazioni originali e contiene la coppia dei due output.

Sebbene si chiami composizione "parallela", e le due operazioni potrebbero in linea di principio essere eseguite in parallelo, l'esecuzione parallela non è un requisito operativo. Possiamo implementare la composizione parallela "sequenzialmente" eseguendo prima un'operazione e poi la seconda. Non ci interessano i dettagli di come venga implementata la composizione parallela, purché l'output sia lo stesso.

### Composizione condizionale

![Conditional Composition](assets/en/003.webp)

La composizione condizionale è il duale della composizione parallela. In questo caso abbiamo due operazioni che producono lo stesso output, e le componiamo scegliendo quale delle due eseguire. L'input di questa operazione composta è la "somma" o "unione taggata" dei tipi degli input delle operazioni originali. In questo caso il tag, "Left" o "Right", è un singolo bit nei dati dell'input che determina quale tipo di dato viene trasportato, e quindi quale delle due operazioni può essere eseguita.

La composizione condizionale opera nello stesso modo anche quando l'input è la somma di due tipi identici. Il tipo somma contiene comunque un tag, e il valore di quel tag determina quale delle due operazioni va eseguita.

### Composizione in Bitcoin Script

Ci sono molti modi di realizzare questi tre tipi di composizione in vari linguaggi di programmazione. In Bitcoin Script, la composizione sequenziale è realizzata (approssimativamente) dalla concatenazione di due routine (questo è il motivo per cui Bitcoin Script è chiamato un linguaggio di programmazione concatenativo) poiché l'output di una routine viene lasciato sullo stack per essere consumato dalla routine successiva. La composizione parallela si ottiene tramite l'uso di operazioni di duplicazione e scambio per manipolare lo stack in modo che due routine possano essere eseguite sullo stesso input. Le cose non sono del tutto semplici poiché ciò che chiamiamo "prodotto" dei tipi viene tipicamente realizzato utilizzando più elementi dello stack. Speriamo che l'idea generale sia chiara.

La composizione condizionale è, naturalmente, realizzata da `OP_IF` che si dirama in base al valore sullo stack. In questo caso l'elemento in cima allo stack svolge il ruolo di tag, e di solito il successivo elemento o elementi sullo stack sono di "tipi" diversi che dipendono dal valore del tag. Per ogni caso i tipi degli elementi dello stack potrebbero essere adatti all'elaborazione solo da uno dei rami dell'`OP_IF`. Tuttavia, dopo aver raggiunto `OP_ENDIF` gli elementi dello stack devono essere di "tipo" coerente in modo che lo script rimanente sia in grado di procedere indipendentemente da quale ramo sia stato preso in precedenza.

### Composizione in Simplicity

Abbiamo progettato Simplicity con combinatori che implementano direttamente queste tre forme di composizione. Insieme a qualche combinatore in più per supportare altre operazioni di base relative ai tipi prodotto e somma, il linguaggio Simplicity di base finisce per consistere in nove combinatori che sono sufficienti a esprimere qualsiasi computazione finita. Ne discuteremo in maggior dettaglio nel prossimo capitolo.

### Un quarto tipo di composizione

Prima di concludere dovremmo menzionare che esiste almeno un altro tipo di composizione presente nell'informatica, che è la "composizione ricorsiva". Nella composizione ricorsiva un'operazione viene iterata più volte.

Nota che Bitcoin Script non supporta la composizione ricorsiva, e allo stesso modo, abbiamo esplicitamente escluso la ricorsione illimitata dal design di Simplicity. La nostra tesi è che la computazione iterativa illimitata sia meglio implementata usando covenant ricorsivi che calcolano attraverso più transazioni. Questo permette agli utenti di evitare i vincoli di spazio nei blocchi e di standardness, e di prevedere meglio i costi delle transazioni.

Detto ciò, ci sono modi di abusare della funzionalità di delega di Simplicity per fornire qualcosa che assomiglia a una composizione ricorsiva illimitata, cosa che potremmo discutere più avanti in questa serie.

### Conclusione

Abbiamo esaminato le tre forme principali di composizione per trasformare operazioni di base in operazioni complesse:

- composizione sequenziale
- composizione parallela
- composizione condizionale

Abbiamo discusso come queste forme di composizione siano realizzate in Bitcoin Script, e accennato a come abbiano influenzato il design del linguaggio Simplicity. Abbiamo notato che il quarto tipo di composizione, la composizione ricorsiva, è specificamente esclusa sia da Simplicity che da Bitcoin Script.

Nel prossimo capitolo descriveremo i nove combinatori che costituiscono il nucleo del linguaggio Simplicity, come servano a realizzare direttamente queste tre forme di composizione, e come questo formi un linguaggio completo per descrivere qualsiasi computazione finita.

## Completezza combinatoria di Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

In questo capitolo introduciamo il linguaggio Simplicity di base e mostriamo che il linguaggio è completo, ovvero che qualsiasi computazione finita può essere espressa al suo interno.

### Tipi di Simplicity

Simplicity supporta tre costruttori di tipo fondamentali. Il tipo prodotto `A × B` rappresenta gli output della composizione parallela, mentre il tipo somma `A + B` (unione taggata) gestisce gli input della composizione condizionale. Il terzo tipo è il tipo unit.

### Tipo Unit

Il tipo unit, indicato con `𝟙` o `ONE`, contiene esattamente un valore: la tupla vuota `⟨⟩` o `()`. Questo tipo di dato a zero bit non trasporta alcuna informazione.

### Tipo Sum

Un tipo somma `A + B` combina due tipi con tag che indicano "sinistra" o "destra". I valori sono scritti come `σᴸ(a)` o `inl(a)` per i valori taggati a sinistra e `σᴿ(b)` o `inr(b)` per i valori taggati a destra. I tag rimangono distinti anche quando si combinano tipi identici.

#### Tipo Booleano

Il tipo `𝟙 + 𝟙`, indicato con `𝟚` o `TWO`, rappresenta un tipo a un bit con due valori. Per convenzione, `σᴸ⟨⟩` rappresenta falso/zero, mentre `σᴿ⟨⟩` rappresenta vero/uno.

### Tipo Prodotto

I tipi prodotto `A × B` contengono coppie di valori scritte come `⟨a, b⟩` o `(a, b)`. Il tipo `𝟚 × 𝟚` ha quattro valori, distinti dai quattro valori in `𝟚 + 𝟚`.

### Espressioni Simplicity di base

Le operazioni sono indicate come `f : A ⊢ B`, il che significa tipo di input `A` e tipo di output `B`. Simplicity è "del primo ordine" — non possiede tipi funzione.

### Due operazioni di base

Il linguaggio di base fornisce due operazioni di base:

**Identità (`iden`).** L'operazione identità fa passare il proprio input inalterato:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** L'operazione unit scarta il proprio input e restituisce la tupla vuota:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Queste formano famiglie con un'operazione per tipo.

### Tre combinatori di composizione

La composizione sequenziale usa `comp f g` (scritto `f ⨾ g` o `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

La composizione parallela usa `pair f g` (scritto `f ▵ g` o `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

La composizione condizionale usa `case f g : (A + B) × C ⊢ D`, fornendo ai rami accesso a un ambiente condiviso `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Perché la composizione condizionale assume questa forma — una somma accoppiata con un ambiente condiviso `C` — anziché un più semplice `copair f g : A + B ⊢ C` che si limita a scegliere un ramo? Perché un `copair` nudo non può esprimere la **distribuzione**: la funzione `dist : (A + B) × C ⊢ A × C + B × C` che spinge un input condiviso nel ramo che viene preso. Costruendo l'ambiente `C` direttamente dentro `case`, Simplicity ottiene la composizione condizionale *e* la distribuzione da un singolo combinatore — una delle decisioni di design chiave che mantiene il linguaggio di base a nove combinatori.

### Altri quattro combinatori

Il consumo di prodotti usa `take` e `drop`:

**take** estrae l'elemento sinistro:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** estrae l'elemento destro:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

La produzione di somme usa `injl` e `injr`:

**injl** avvolge con un tag sinistro:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** avvolge con un tag destro:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### I nove combinatori fondamentali

In totale, Simplicity ha esattamente nove combinatori fondamentali:

| Combinator | Purpose |
|---|---|
| `iden` | Pass input through |
| `unit` | Discard input |
| `comp` | Sequential composition |
| `pair` | Parallel composition |
| `case` | Conditional composition |
| `take` | Extract left from product |
| `drop` | Extract right from product |
| `injl` | Inject into left of sum |
| `injr` | Inject into right of sum |

### Simplicity e il calcolo dei sequenti

Il design di Simplicity deriva dal frammento congiuntivo-disgiuntivo del calcolo dei sequenti di Gentzen. Più precisamente, è una variante dell'*interpretazione funzionale* del calcolo dei sequenti, che è a sua volta analoga alla corrispondenza di Curry-Howard tra deduzione naturale e calcolo lambda. Le regole dei combinatori esibiscono "tipi più piccoli nelle premesse rispetto alle conclusioni", permettendo alla Bit Machine — l'interprete a macchina a stack astratto di Simplicity — di minimizzare la copia di dati durante l'esecuzione.

### I valori non sono espressioni

Le espressioni Simplicity denotano operazioni, non valori. La notazione `scribe b : A ⊢ B` rappresenta un'unica espressione che restituisce sempre il valore `b`, e serve come comodità notazionale piuttosto che come combinatore. Questo rispecchia Bitcoin Script, dove operazioni come `OP_1` spingono valori piuttosto che esprimerli direttamente.

### Il teorema di completezza di Simplicity

Con tutti e nove i combinatori a disposizione, come facciamo a sapere di non star trascurando qualcosa — che questi nove siano davvero sufficienti? Il teorema di completezza di Simplicity risponde a questa domanda: per qualsiasi funzione tra tipi Simplicity (finiti), esiste un'espressione Simplicity che la denota. La dimostrazione è costruttiva — mostra come costruire l'espressione:

1. **Decomporre l'input**: usando espressioni `case` annidate, decomporre completamente qualsiasi input di qualsiasi tipo nei suoi bit costituenti
2. **Costruire una tabella di lookup**: per ogni possibile input, usare `scribe` per produrre l'output corrispondente
3. **Assemblare**: i `case` annidati e gli `scribe` insieme formano una gigantesca tabella di lookup che implementa la funzione

Questo teorema è formalmente verificato nell'assistente di dimostrazione Rocq (precedentemente Coq). La dimostrazione fa parte del repository ufficiale di Simplicity ed è stata verificata meccanicamente per la sua correttezza.

Sebbene il teorema di completezza garantisca che i nove combinatori di Simplicity possano esprimere qualsiasi funzione tra tipi Simplicity (finiti), le espressioni risultanti dalla costruzione a tabella di lookup sono impraticabilmente grandi. Una funzione su input a 256 bit richiederebbe una tabella di lookup con 2²⁵⁶ voci. Questo è il motivo per cui i prossimi capitoli si concentrano sulla costruzione di espressioni efficienti che sfruttano la struttura delle computazioni, piuttosto che forzare tutto tramite tabelle di lookup.

### Conclusione

Il linguaggio di base di Simplicity include un sistema di tipi e combinatori che abilitano qualsiasi computazione finita. Sebbene il teorema di completezza garantisca l'espressività, le espressioni risultanti dalla costruzione generica sono impraticabilmente grandi. Lo sviluppo pratico in Simplicity comporta lo sfruttamento della struttura computazionale per espressioni concise. I prossimi capitoli esplorano strutture dati, interazioni con le transazioni e combinatori aggiuntivi.
</content>

# Dai tipi di dati ai programmi

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Costruire tipi di dati

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

Nei capitoli precedenti, abbiamo mostrato come l'insieme di combinatori di base di Simplicity sia sufficiente per implementare qualsiasi computazione pura finita. Questo capitolo mostra come costruire strutture dati e computazioni pratiche a partire da queste primitive — allo stesso modo in cui i computer sono costruiti a partire da porte logiche.

### Logica booleana

Il tipo Booleano, indicato con `𝟚`, equivale a `𝟙 + 𝟙` e ha due valori: `σᴸ⟨⟩` (falso) e `σᴿ⟨⟩` (vero). Usando i combinatori di base, si possono costruire gli operatori della logica booleana.

#### Operazione And

L'operazione logica `and : 𝟚 × 𝟚 ⊢ 𝟚` prende due bit e restituisce un bit. L'implementazione si dirama sul primo bit: se falso, restituisce falso; altrimenti, restituisce il secondo bit.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Verifica con `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Verifica con `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Altre operazioni logiche

L'operazione `not` richiede un combinatore ausiliario:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

L'iniziale `iden ▵ unit : A ⊢ A × 𝟙` aggiunge un "ambiente" vuoto all'input, permettendo l'applicazione del combinatore `case`. L'uso di `take` nei due rami scarta questo ambiente vuoto per eseguire `f` o `g`.

Altre operazioni logiche booleane:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Sommatori di bit

Un "half-adder" (semi-sommatore) prende due bit e li somma, producendo un output a due bit: un bit di riporto e un bit di somma.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

Un "full-adder" (sommatore completo) somma tre bit, producendo un output a due bit. L'input usa la tupla annidata `(𝟚 × 𝟚) × 𝟚`.

Per le tuple annidate, viene usata una notazione compatta:

- `O f` indica `take f`
- `I f` indica `drop f`
- `H` indica `iden`

Ad esempio, `I O H` significa `drop (take iden) : A × (B × C) ⊢ B`, estraendo il valore centrale. La notazione evoca cifre binarie: pensando alle tuple annidate come alberi binari, la notazione rappresenta le cifre binarie invertite delle posizioni nell'albero. Queste espressioni formano indici di De Bruijn per Simplicity.

**Nota:** la notazione `I`, `O` e `H` si applica solo a sottoespressioni composte esclusivamente da `take`, `drop` e `iden`.

Il full-adder compone due half-adder, prendendo l'`or` logico dei bit di riporto:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

Nella prima riga, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` esegue l'half-adder sui primi due bit, conservando l'ultimo bit.

Nella seconda riga, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` conserva il primo bit (il riporto in uscita del primo half-adder) ed esegue l'half-adder sugli ultimi due bit.

Nell'ultima riga, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` prende l'OR logico dei primi due bit (i riporti in uscita di entrambi gli half-adder) e restituisce il bit di somma in uscita del secondo half-adder.

Questo dimostra la programmazione in Simplicity: usare la notazione `I`, `O` e `H` per riferirsi ai bit di dati, formando "ambienti" adatti per chiamare altre funzioni tramite composizione sequenziale.

Gli utenti non definiscono operazioni di basso livello direttamente. Più avanti in questa serie si discuteranno i jet della libreria standard che implementano funzioni comuni. Gli utenti finali non devono programmare direttamente in Simplicity, in modo simile a Bitcoin Script. Invece, linguaggi di livello superiore come SimplicityHL generano codice Simplicity, gestendo gli "ambienti" delle sottoespressioni e traducendo le variabili con nome in sequenze appropriate di `take` e `drop`.

### Vettori

I vettori a lunghezza fissa sono definiti formando prodotti iterati del tipo `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Questi possono essere scritti come `A^2`, `A^4`, `A^8`, ecc.

I vettori sono definiti solo per lunghezze che sono potenze di due. Altre potenze richiederebbero la scelta di convenzioni di raggruppamento.

Data l'espressione `f : A ⊢ B`, l'accoppiamento ripetuto "mappa" essa sui vettori a lunghezza fissa:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Data la funzione `f : A × B ⊢ B`, l'iterazione o "folding" sui vettori a lunghezza fissa:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Esistono molte varianti. Data `f : A × B ⊢ C`, "zip" su vettori accoppiati con `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Data `f : (A × B) × C ⊢ C`, fold su vettori accoppiati con `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Combinando `map` e `fold-right` si creano combinatori accumulanti: `f : A × C ⊢ C × B` produce `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Sono possibili molte più varianti.

#### Parole multi-bit

Un vettore di bit produce interi multi-bit. Ad esempio, `𝟚³²` è un tipo parola a 32 bit. `𝟚²⁵⁶` è un tipo parola a 256 bit, adatto per hash e operazioni crittografiche.

Usando il full-adder, una variante delle operazioni sui vettori definisce un "sommatore a riporto propagato" (ripple carry adder) su parole multi-bit:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` prende due numeri binari a n bit e un bit di riporto in ingresso, restituendo un flag di riporto in uscita a un bit e una somma a n bit.

#### SHA-256

Definendo ricorsivamente operazioni aritmetiche su parole multi-bit — sottrazione, moltiplicazione, divisione — e operazioni logiche bit a bit come AND, OR, XOR logici, e combinando ripetutamente queste, si può costruire persino la funzione di compressione a blocchi di SHA-256:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

La compressione SHA-256 è formalmente definita usando Simplicity all'interno dell'assistente di dimostrazione Rocq (precedentemente Coq), con una dimostrazione formale che l'implementazione di `sha256-hash-block` è corretta.

La compressione gira troppo lentamente come Simplicity grezzo. I jet eseguono nativamente funzioni comuni come la compressione SHA-256. Le implementazioni Simplicity pure servono come specifiche formali per i jet.

### Tipi Option

I tipi Option risultano dal prendere una somma con il tipo unit:

```
Option A ≔ 𝟙 + A
```

Il tipo `Option A` può essere scritto come `A?` o `𝕊 A` (dove `𝕊` significa "successore"). Le funzioni mappano sui tipi option:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Combinatori monadici come bind possono essere definiti:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffer a lunghezza variabile

I "buffer" sono tipi per vettori parzialmente riempiti:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Il tipo `Xᑉ⁸` si espande a `(1 + X⁴) × ((1 + X²) × (1 + X))`. Trattandolo come un polinomio ed espandendolo si ottiene `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Interpretato come tipo, rappresenta la somma di tutte le possibili tuple di X fino a 7, inclusa la tupla vuota. Questo è esattamente il tipo delle liste di lunghezza strettamente minore di 8.

Come per i vettori, si possono definire operazioni di mappatura e folding sui buffer. Le operazioni di stack includono `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` e `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` aggiunge un elemento al buffer, restituendo un vettore completo in caso di overflow. `pop-<n` rimuove un elemento, restituendo il buffer più piccolo e l'elemento rimosso, restituendo opzionalmente nulla se il buffer originale era vuoto.

La definizione di `push-<n`, ricorsivamente:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Simplicity grezzo diventa difficile da seguire oltre certi livelli di complessità. Gli utenti finali utilizzano linguaggi di livello superiore come SimplicityHL che generano queste espressioni idiomatiche.

### Conclusione

Questo capitolo ha mostrato come costruire operazioni logiche a partire dai bit. Da queste, è emersa l'aritmetica a livello di bit, permettendo di ragionare sull'esecuzione. Sono stati sviluppati tipi vettore, dimostrando l'iterazione su parole multi-bit per la definizione dell'aritmetica. Proseguendo, operazioni crittografiche come SHA-256 e la validazione delle firme Schnorr possono essere definite usando solo combinatori Simplicity — tutte effettivamente definite usando Simplicity.

Questo capitolo non è una guida esaustiva a tutti i possibili tipi di dati e operazioni costruibili in Simplicity, ma illustra come ottenere funzionalità pratiche entro i vincoli di Simplicity. Nonostante i tipi finitamente limitati, si possono definire vettori utili, tipi buffer e operazioni che iterano su queste strutture.

Le effettive specifiche delle operazioni della libreria standard differiscono leggermente dalle definizioni qui riportate. Ad esempio, il full-adder effettivo usa una funzione XOR a 3 vie e una logica di "maggioranza" invece di due half-adder.

In pratica, i programmi Simplicity usano jet per le operazioni aritmetiche e crittografiche. Tuttavia, i jet sostituiscono solo espressioni. I combinatori che iterano su buffer e vettori non possono essere sostituiti da jet, e compaiono nei programmi Simplicity effettivi. Sebbene, piuttosto che usare direttamente questi, gli utenti finali impiegano linguaggi di livello superiore come SimplicityHL che generano tali espressioni.

I combinatori definiti ricorsivamente sembrano crescere esponenzialmente in dimensione dell'espressione. Questo non è un problema. Durante la serializzazione, le espressioni sono codificate come DAG (grafi diretti aciclici) piuttosto che come alberi. La rappresentazione effettiva cresce solo linearmente.

Finora, sono state considerate solo computazioni pure. L'interazione con i dati delle transazioni per compiti come la firma delle transazioni richiede un modo per far fallire i programmi se le firme non sono valide. Il prossimo capitolo discute gli effetti collaterali in Simplicity.

## Due effetti collaterali

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

Nei capitoli precedenti, abbiamo mostrato come costruire alcune strutture dati e computazioni usando l'insieme di combinatori di base di Simplicity. Come abbiamo notato, i combinatori di base sono sufficienti per implementare qualsiasi computazione pura finita. Questo solleva una domanda: cos'altro si può ottenere? Possiamo aggiungere effetti collaterali aggiuntivi alle nostre espressioni.

Esistono vari tipi di possibili effetti collaterali per le espressioni: aggiornamento di stato, scrittura su un log, lancio di un'eccezione, lettura da un ambiente, chiamata a una continuazione, ecc. Gli effetti collaterali disponibili in Simplicity dipendono dall'applicazione.

Per le applicazioni Bitcoin e Liquid, attualmente abbiamo due effetti collaterali: l'effetto Failure, che è un effetto di eccezione dove l'eccezione ha tipo `𝟙`, e l'effetto Reader che permette di accedere ai dati dall'ambiente della transazione. I nostri combinatori di base sono "puri"; non hanno effetti collaterali. Tuttavia, i jet possono introdurre nuove primitive che hanno effetti collaterali.

### Jet con effetti

Parleremo di più dei jet più avanti in questo corso, ma qui introduciamo alcuni jet di esempio per illustrare i loro effetti collaterali.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` è un jet per un'espressione che prende una chiave pubblica x-only, un messaggio a 256 bit e una firma Schnorr, e non restituisce nulla! Secondo il suo tipo, dovrebbe comportarsi come `unit`. La differenza sta nell'effetto collaterale del jet: se la verifica della firma fallisce, l'intera computazione viene interrotta lanciando un'eccezione (di tipo unit). Questo è l'effetto Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` è un jet minimale per esprimere l'effetto Failure. Se l'input di `verify` è `false`, l'intera computazione viene interrotta, lanciando un'eccezione. Se l'input è `true`, non viene restituito nulla, ma la computazione può continuare.

#### Hash delle transazioni

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` sembra essere una funzione costante, poiché c'è un solo possibile valore di input: la tupla vuota. Tuttavia, questo jet legge dall'ambiente della transazione e produce un hash dei dati della transazione analogo al message digest `SIGHASH_ALL` usato nella verifica delle firme di Bitcoin Script. Questo è un esempio dell'effetto Reader: il valore restituito dipende dall'ambiente della transazione all'interno del quale il jet viene eseguito. Esistono diversi altri jet di hashing che effettuano l'hash di vari sottoinsiemi dei dati dell'ambiente della transazione per aiutare a costruire message digest personalizzati per le firme.

#### Jet di introspezione

`input-sequence : 𝟚³² ⊢ 𝟚³²?` è una funzione che prende un indice di input e restituisce il numero di sequenza della transazione per quell'input, restituendo opzionalmente nulla se l'indice è fuori limite. Anche qui, il valore di output non è una funzione pura dell'indice di input, ma piuttosto l'operazione usa l'effetto Reader per accedere all'ambiente della transazione al fine di determinare il valore di output. Esistono diversi altri jet di introspezione che restituiscono vari frammenti dei dati dell'ambiente della transazione.

### Classificare gli effetti

Non tutti gli effetti collaterali sono uguali. Alcuni effetti collaterali si comportano meglio di altri. Possiamo classificare gli effetti in base a quanto sono suscettibili di trasformazioni del programma.

#### Effetti commutativi

Un effetto commutativo è uno in cui, se si scambiano gli output di due espressioni, si possono scambiare in sicurezza anche le espressioni stesse senza modificare l'effetto dell'espressione. Considera `swap = I H ▵ O H : A × B ⊢ B × A`. Se `f ▵ g ⨾ swap = g ▵ f` per ogni espressione `f` e `g` con effetti collaterali, allora gli effetti sono commutativi.

Leggere dati della transazione dall'ambiente è un effetto commutativo perché il risultato della lettura dall'ambiente è lo stesso, indipendentemente dall'ordine in cui eseguiamo la lettura.

In generale, lanciare un'eccezione non è un effetto commutativo. Se `f` lancia un'eccezione `e₁` e `g` lancia un'altra eccezione `e₂`, allora quale eccezione viene lanciata dalla coppia di `f` e `g` dipende dall'ordine in cui vengono eseguite.

Tuttavia, nel caso speciale dell'effetto Failure, in cui può essere lanciata solo un'eccezione di tipo unit, l'effetto è commutativo. Indipendentemente da quale tra `f` o `g` lanci un'eccezione, l'eccezione risultante sarà la stessa, perché esiste un solo possibile valore di eccezione.

#### Effetti idempotenti

Un effetto idempotente è uno in cui, se si duplica l'output di un'espressione, si può duplicare in sicurezza anche l'espressione stessa senza modificare l'effetto dell'espressione. Considera `dup = iden ▵ iden : A ⊢ A × A`. Se `f ⨾ dup = dup ⨾ f ▵ f` per ogni `f` con effetti collaterali, allora gli effetti sono idempotenti.

Leggere dati della transazione dall'ambiente è un effetto idempotente. Anche lanciare un'eccezione è un effetto idempotente. Anche se solo una delle due espressioni duplicate verrà eseguita, qualsiasi eccezione lanciata da `dup ⨾ f ▵ f` sarà la stessa lanciata da `f ⨾ dup`.

Tuttavia, scrivere su un log potrebbe non essere idempotente, poiché duplicare l'effetto farebbe apparire il messaggio di log due volte. Tuttavia, se il log consiste in un _insieme_ di messaggi invece che in una _lista_ di messaggi, allora l'effetto sarebbe idempotente (e commutativo) perché l'inserimento in un insieme è a sua volta un'operazione idempotente.

#### Effetti unitari

Un effetto unitario è uno in cui, se si scarta l'output di un'espressione, si può scartare in sicurezza anche l'espressione stessa senza modificare gli effetti dell'espressione. Se vale sempre che `f ⨾ unit = unit` per ogni `f` con effetti collaterali, allora i tuoi effetti sono unitari.

Leggere dati dall'ambiente è uno dei pochi tipi di effetti unitari. Se il risultato della lettura dei dati della transazione dall'ambiente viene scartato, l'intera espressione che esegue la lettura può essere scartata.

L'effetto Failure non è unitario. Se `f` lancia un'eccezione, allora lo farà anche `f ⨾ unit`; l'esecuzione non arriverà nemmeno al combinatore `unit` prima che la computazione venga interrotta. D'altra parte, `unit` ovviamente non lancerebbe alcuna eccezione, quindi gli effetti di `f ⨾ unit` e di `unit` sarebbero diversi.

Per riassumere, ecco come gli effetti discussi sopra si comportano rispetto a queste tre proprietà:

| Effect | Commutative | Idempotent | Unitary |
| --- | :---: | :---: | :---: |
| Reader (transaction environment) | ✓ | ✓ | ✓ |
| Failure (unit-typed exception) | ✓ | ✓ | ✗ |
| Writer (log as a set) | ✓ | ✓ | ✗ |
| General exceptions (arbitrary type) | ✗ | ✓ | ✗ |

### Effetti consentiti in Simplicity

Più proprietà ben educate ha un tipo di effetto, più margine ha un ottimizzatore Simplicity per trasformare i programmi che usano quegli effetti. Idealmente vorremmo consentire solo effetti che hanno tutte e tre le proprietà: commutativi, idempotenti e unitari. Questo permetterebbe a un ottimizzatore di eseguire qualsiasi tipo di trasformazione del programma desideri. Tuttavia, la lettura da un ambiente è l'unico effetto che soddisfa tutte e tre le proprietà.

Invece richiediamo che gli effetti di Simplicity siano commutativi e idempotenti. Entrambi gli effetti che usiamo in Simplicity, l'effetto Failure e l'effetto Reader, sono commutativi e idempotenti. Questo permette di eseguire una vasta classe di ottimizzazioni sul codice Simplicity.

Tuttavia, la trasformazione di "scarto" descritta sopra, il tentativo di sostituire `f ⨾ unit` con `unit`, o qualsiasi trasformazione simile, non è consentita se `f` può produrre un effetto Failure. Infatti, immagina se `f` contenesse un'asserzione `bip0340-verify`. Sarebbe disastroso tentare di ottimizzare via quel controllo.

### Perché consentire effetti collaterali?

Perché Simplicity dovrebbe consentire effetti collaterali? Non sarebbe meglio se ogni programma prendesse l'intera transazione come input e restituisse un output Booleano che decide se una transazione è valida o meno?

#### Verifica in batch

Uno dei motivi per cui abbiamo l'effetto Failure è supportare la [verifica in batch](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) delle firme Schnorr. Nella verifica in batch, molte verifiche individuali di firme Schnorr vengono raggruppate in modo tale che, se una singola verifica di firma fallisce, l'intero batch fallisce.

Questa procedura di batching migliora l'efficienza rispetto alla verifica individuale di ogni firma. Lo svantaggio è che se la verifica in batch fallisce, non veniamo a sapere quale specifica verifica di firma o verifiche siano fallite.

Usando l'effetto collaterale Failure, `bip0340-verify` garantisce che se una verifica di firma fallisce, l'intera transazione fallisce. Se `bip0340-verify` restituisse invece `𝟚`, un tipo Booleano, per successo o fallimento, allora una verifica di firma fallita potrebbe comunque portare a un ramo in cui lo script ha successo. In tal caso avremmo bisogno di sapere se la particolare firma è valida o meno, e quindi non potremmo sfruttare la verifica in batch.

#### Dati di transazione precalcolati

Un problema nei primi tempi di Bitcoin Script era che la funzione di hashing usata per creare i message digest per le firme era lineare rispetto alla dimensione della transazione. Tipicamente ogni input crea almeno un message digest per la verifica della firma, quindi complessivamente la quantità di hashing era quadratica rispetto alla dimensione della transazione.

Questo problema è stato risolto in Segwit e nelle iterazioni successive di Bitcoin Script ridefinendo i message digest in modo che potessero essere calcolati in tempo costante per ogni verifica di firma. Questo si basa sull'avere `PrecomputedTransactionData`, che precalcola gli hash dei dati della transazione una sola volta e viene poi condiviso da tutte le computazioni sighash di ciascun input. I jet di hashing delle transazioni di Simplicity si basano sullo stesso tipo di dati di transazione precalcolati per garantire che i jet vengano eseguiti in tempo costante.

Supponiamo che `sig-all-hash` non usasse l'effetto Reader. Supponiamo di essere riusciti in qualche modo a costruire un tipo Simplicity per l'ambiente della transazione. Chiamiamolo `TxEnv`, in modo che `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` fosse il tipo del jet. Una tale definizione richiederebbe che il jet `sig-all-hash` fosse in grado di calcolare l'hash di qualsiasi transazione, non solo della transazione con cui è coinvolto. I programmi Simplicity potrebbero copiare il `TxEnv` fornito e passare una copia modificata di esso a `sig-all-hash`. In tal caso `sig-all-hash` non potrebbe fare affidamento su `PrecomputedTransactionData`, e torneremmo a richiedere tempo lineare rispetto a qualunque dato di transazione venisse passato a questa versione di `sig-all-hash`.

Poiché `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` usa l'effetto Reader per accedere ai dati della transazione, ottiene accesso _solo_ a un ambiente di transazione fisso. Per questo motivo, l'implementazione del jet può usare in sicurezza `PrecomputedTransactionData` e operare in tempo costante.

### Aggregazione di firme cross-input

Sebbene né Liquid né Bitcoin supportino attualmente l'[aggregazione di firme cross-input](https://hrf.org/latest/cisa-research-paper/), vorremmo verificare che Simplicity possa essere compatibile con essa quando arriverà il momento.

Sebbene i dettagli non siano stati definiti, immaginiamo che la mezza-aggregazione (half-aggregation) venga implementata usando un effetto Writer. Cioè, un nuovo jet con un tipo come `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` prenderebbe una chiave pubblica, un message digest e la componente `r` di una firma Schnorr (una firma Schnorr consiste in una componente `r` e una componente `s`) e li scriverebbe su un log della transazione prima di continuare l'esecuzione. Poi, altrove nella transazione o con la transazione, verrebbe fornita una componente `s` aggregata per tutte le firme Schnorr semi-aggregate. La transazione sarebbe valida solo quando tale componente `s` aggregata viene fornita per tutte le chiavi, i messaggi e le componenti `r` registrati.

Per soddisfare i requisiti di Simplicity, questo effetto Writer deve essere idempotente e commutativo. Questo può essere garantito trattando il log del writer come un insieme di tuple chiave, messaggio, componente `r`. Questo funziona perché le operazioni sugli insiemi sono idempotenti e commutative. Trattare il log come un insieme di valori sarebbe compatibile con l'algoritmo di verifica della semi-aggregazione.

### Conclusione

In questo capitolo abbiamo esaminato l'aggiunta di effetti collaterali alle computazioni che Simplicity può svolgere. Abbiamo classificato vari tipi di effetti in base a quanto siano ben educati rispetto a vari tipi di trasformazione del programma. Abbiamo deciso di limitare gli effetti di Simplicity a quelli commutativi e idempotenti.

I due effetti che usiamo per le applicazioni Bitcoin e Liquid sono l'effetto Reader, per accedere all'ambiente della transazione, e l'effetto Failure, per interrompere e far fallire il programma. Alcuni jet fanno uso di operazioni primitive dove questi tipi di effetti collaterali possono verificarsi.

L'effetto Failure determina l'output di un programma Simplicity: il programma o fallisce, rendendo la transazione non valida, oppure il programma ha successo. L'effetto Reader fornisce un tipo di input a un programma Simplicity: l'ambiente contenente i dati della transazione. Ma dobbiamo anche fornire altri input, come le firme digitali, ai programmi Simplicity.

Nel prossimo capitolo esamineremo cosa sono i programmi Simplicity, come vengono trasformati in indirizzi, e come aggiungiamo altri input, come le firme, ai programmi Simplicity.

## Programmi e indirizzi

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

Nel capitolo precedente abbiamo descritto due effetti collaterali usati in Simplicity: l'effetto Failure, che determina il successo o il fallimento di un programma, e l'effetto Reader, che fornisce accesso all'ambiente della transazione. Ora ci rivolgiamo alla domanda pratica: cos'è esattamente un programma Simplicity, e come diventa un indirizzo sulla blockchain?

### Programmi Simplicity

Un programma Simplicity è definito come un'espressione Simplicity di tipo `𝟙 ⊢ 𝟙`. Questa firma di tipo significa che il programma non prende un input significativo (solo il valore unit) e non produce un output significativo (solo il valore unit). L'effetto Reader cattura l'input dell'ambiente della transazione, mentre l'effetto Failure indica successo o fallimento. Questi effetti gestiscono l'I/O piuttosto che i tipi Simplicity stessi.

### Commitment Merkle Root

Anziché memorizzare programmi completi on-chain, Bitcoin impiega commitment — una pratica che si estende da Pay-to-Script-Hash (P2SH). Simplicity usa un Commitment Merkle Root (CMR).

Ogni combinatore riceve un tag SHA-256 derivato dal pattern: `Simplicity␟Commitment␟[identifier]`, dove `␟` rappresenta il codice ASCII 31 (l'unit separator).

Ogni tag è l'hash SHA-256 della corrispondente stringa pre-immagine elencata di seguito:

| Combinator | Tag pre-image (ASCII string) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Un'espressione Simplicity viene poi sottoposta ricorsivamente a hash in un CMR a 256 bit calcolando un midstate SHA-256 taggato per ciascun combinatore insieme ai CMR dei suoi argomenti (scriviamo `#ᶜ(e)` per il CMR dell'espressione `e`, e `∥` per la concatenazione di byte):

| Combinator | CMR rule |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

I combinatori binari (`comp`, `pair`, `case`) concatenano i CMR di entrambi i figli; i combinatori unari (`take`, `drop`, `injl`, `injr`) concatenano il CMR del loro unico figlio dopo un padding di 32 byte a `0x00`; e le foglie nullarie (`iden`, `unit`) fanno l'hash del loro solo tag. Due convenzioni mantengono questo economico da calcolare: si usano midstate SHA-256 in modo che **ogni espressione richieda al massimo una chiamata alla funzione di compressione SHA-256** (assumendo che il midstate fino ai tag costanti sia precalcolato), e i costruttori a un argomento prefissano il loro argomento con 32 byte di padding `0x00`, il che consente un po' di precalcolo extra per le implementazioni che lo desiderano.

Per il combinatore `unit` — un costruttore nullario senza sotto-espressioni argomento — questa regola si specializza in `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, dove `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (il tag viene fornito due volte). Il CMR risultante per il programma banale `unit` è:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

È fondamentale notare che il CMR non si impegna sui tipi delle espressioni Simplicity, basandosi invece sull'inferenza di tipo durante il riscatto.

### Indirizzi

Gli indirizzi impiegano il meccanismo Taproot di BIP-0341 con i CMR impegnati sotto la versione TapLeaf `0xbe`. Il processo prevede:

1. Calcolare un hash taggato TapLeaf combinando il byte di versione, la lunghezza del CMR e il CMR stesso
2. Modificare (tweak) una chiave pubblica interna (usando un punto NUMS quando non si desidera un percorso di spesa tramite chiave)
3. Convertire in formato bech32m
4. Aggiungere i checksum appropriati

Quando non si desidera un percorso di spesa tramite chiave, la chiave pubblica interna viene impostata su un punto **NUMS** ("Nothing-Up-My-Sleeve"): un punto della curva scelto deliberatamente in modo che nessuno ne conosca il logaritmo discreto — in altre parole, un punto senza una corrispondente chiave privata. Poiché nessuno può mai produrre una firma per esso, il percorso di spesa tramite chiave è dimostrabilmente inutilizzabile, e l'output può essere speso *solo* attraverso il percorso dello script Simplicity impegnato. In un'applicazione reale, questo punto NUMS dovrebbe essere randomizzato come raccomandato da BIP-0341, in modo che gli output senza percorso di spesa tramite chiave siano indistinguibili dagli output Taproot ordinari (un beneficio per la privacy).

#### Da Simplicity a indirizzo

Percorriamo l'intera derivazione per il programma più semplice possibile: `unit : 𝟙 ⊢ 𝟙`, un no-op che ha sempre successo.

**1. Tag del combinatore.** Prima calcoliamo il tag `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Forniamo il tag due volte per ottenere il CMR del programma:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. Hash TapLeaf.** Prefissiamo il CMR con la versione TapLeaf di Simplicity `0xbe` e la lunghezza del CMR `0x20` (32 byte), quindi calcoliamo l'hash taggato TapLeaf di Elements (un hash taggato è `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Con questa unica foglia non ci sono TapBranch, quindi questo hash è già la radice del TapTree.

**4. TapTweak.** Poiché vogliamo nessun percorso di spesa tramite chiave, usiamo il punto NUMS di BIP-0341 come chiave interna e lo modifichiamo con la radice del TapTree:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Chiave di output.** Modifichiamo la chiave interna sulla curva, `output_pk = lift_x(internal_pk) ⊕ t·G` (l'aritmetica sulla curva ellittica è qui riassunta), ottenendo la chiave di output x-only `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Indirizzo Bech32m.** Codifichiamo la chiave di output x-only, prefissiamo una `p` (il carattere di versione witness SegWit v1), aggiungiamo il prefisso leggibile Liquid-testnet `tex1`, e aggiungiamo il checksum Bech32m. L'indirizzo finale è:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

È stato un bel lavoro — ma gran parte è imposta da Taproot stesso, non da Simplicity.

### Espressioni Witness

Un nuovo tipo di combinatore risolve l'assenza di input ai programmi Simplicity: l'espressione witness. Il combinatore `witness` permette l'integrazione di dati di firma e altro materiale witness nei programmi.

```
      w : B
-----------------
witness w : A ⊢ B
```

La semantica dell'espressione witness è semplice: ignora il proprio input e restituisce semplicemente il valore `w` (che può essere di qualsiasi tipo Simplicity), cioè `⟦witness w⟧(a) = w`. Questo non aggiunge **nessuna nuova espressività** — dal teorema di completezza, Simplicity può già costruire qualsiasi funzione costante di questo tipo (ricordiamo la macro `scribe` dei capitoli precedenti). Il senso del combinatore `witness` sta interamente nel suo **CMR**: il valore `w` è **escluso** dal CMR dell'espressione, quindi l'indirizzo può essere calcolato prima che `w` sia noto, e `w` viene fornito al momento del riscatto.

Questa scelta di design supporta la potatura (pruning) — i rami condizionali non eseguiti non devono essere rivelati on-chain, incluse le loro espressioni witness associate. Quando un ramo viene potato, il verificatore ha bisogno solo del CMR del sottoalbero potato, non del suo contenuto effettivo.

### Valori Witness

Potrebbe sembrare una limitazione che un'espressione witness possa contenere solo un *valore*, e non un'espressione Simplicity più generale. Ma i programmi per blockchain basate su UTXO vengono eseguiti una sola volta. Non c'è bisogno di passare un'intera sotto-espressione a un nodo witness: l'utente può semplicemente eseguire quella sotto-espressione da solo, off-chain, e trascriverne l'output nel valore witness per ottenere lo stesso identico risultato.

(Più avanti in questo corso incontreremo il combinatore `disconnect`, che si comporta molto come un'espressione witness che *prende* un'intera espressione Simplicity come proprio argomento.)

Un design alternativo alimenterebbe tutti i dati witness come argomento al programma Simplicity di livello superiore. Le espressioni witness sono preferite per due motivi. Primo, la **potatura**: i rami non eseguiti delle espressioni `case` non vengono mai rivelati on-chain, e qualsiasi espressione witness al loro interno viene potata insieme a essi. Secondo, la **località**: le espressioni witness ci permettono di collocare ogni valore witness esattamente dove viene usato, invece di farlo passare dall'input di livello superiore del programma.

### Inferenza di tipo

Poiché i CMR non si impegnano sui tipi, il sistema di tipi viene ricostruito durante il riscatto. L'algoritmo di inferenza di tipo di Simplicity determina i tipi minimi per ciascuna sotto-espressione in base alla struttura del combinatore. Più precisamente, l'inferenza calcola il tipo *principale* (più generale) di ogni sotto-espressione; qualsiasi variabile di tipo che rimane libera viene poi istanziata al tipo unit `𝟙`, il che produce un tipo unico e minimo per il programma.

### Conclusione

In questo capitolo abbiamo stabilito che i programmi Simplicity sono espressioni di tipo `𝟙 ⊢ 𝟙`, spiegato come vengono costruiti i Commitment Merkle Root a partire da hash SHA-256 taggati di ciascun combinatore, e mostrato come i CMR vengono trasformati in indirizzi on-chain tramite Taproot BIP-0341. Abbiamo introdotto le espressioni witness come meccanismo per fornire dati di firma e altri input al momento della spesa senza impegnarsi sui loro valori al momento della creazione dell'indirizzo.

# Sezione finale

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Recensioni e valutazioni

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Esame finale

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusione

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>

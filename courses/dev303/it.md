---
name: Impara Rust con Bitcoin
goal: Migliorare le competenze di sviluppo Rust attraverso la codifica di Bitcoin
objectives: 

  - Studiare il linguaggio Rust
  - Capire perché usare Rust per sviluppare Bitcoin
  - Imparare le basi di Lightning SDK

---

# Un viaggio nel linguaggio Rust per i developer Bitcoin



In questo corso pratico, filmato durante un seminario organizzato da Fulgur' Ventures nell'ottobre 2023, svilupperete le vostre competenze Rust costruendo componenti e mini-progetti reali incentrati su Bitcoin. Verranno trattati i fondamenti di Rust, i motivi per cui Rust viene utilizzato per lo sviluppo di Bitcoin (sicurezza della memoria, prestazioni e concorrenza sicura) e come iniziare a utilizzare l'SDK Lightning per creare funzionalità di pagamento.


Nel corso dei capitoli, si farà pratica con i modelli fondamentali del Rust (proprietà, tempi di vita, tratti, async), si lavorerà con le primitive di Bitcoin (chiavi, transazioni, scripting) e si integreranno progressivamente i concetti di Lightning (nodi, canali, fatture).


Non è richiesto alcuno sviluppo precedente di Rust o Bitcoin, anche se la familiarità con la programmazione di base è utile. Il corso è adatto ai principianti, ma sufficientemente pratico per gli ingegneri che passano al Bitcoin.


+++

# Introduzione

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Panoramica del corso

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Introduzione**


Benvenuti a questo corso di programmazione per principianti sugli SDK. In questo corso imparerete le basi del Rust, poi vi concentrerete sul Rust applicato alla programmazione di Bitcoin e concluderete con alcuni casi d'uso degli SDK.


I video della formazione saranno per ora disponibili solo in inglese e facevano parte di un seminario dal vivo organizzato lo scorso ottobre in Toscana da Fulgure Venture. Questa formazione si concentrerà solo sulla prima settimana. La seconda parte era rivolta al RGB e può essere consultata nel corso RGB.


https://planb.academy/en/courses/rgb-programming-3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Questo corso offre l'opportunità di sviluppare le proprie capacità di programmazione sul Lightning Network utilizzando Rust e vari SDK. È pensato per gli sviluppatori con un solido background di programmazione che desiderano immergersi nello sviluppo specifico per il Lightning Network. Imparerete le basi del Rust, i motivi per cui è adatto allo sviluppo di Bitcoin, per poi passare all'implementazione pratica utilizzando gli SDK specializzati.


**Sezione 2: Imparare a codificare con Rust**

In questa sezione scoprirete i fondamenti del Rust attraverso una serie di capitoli progressivi. Imparerete a scrivere codice Rust, a comprenderne le specificità e a padroneggiarne le caratteristiche essenziali in sette parti dettagliate. Questo modulo è essenziale per comprendere perché Rust è il linguaggio preferito per lo sviluppo di Bitcoin.


**Sezione 3: Rust e Bitcoin**

In questa sede, esploreremo in modo approfondito perché Rust è una scelta importante per lo sviluppo di Bitcoin. Imparerete a conoscere il suo modello di errore, lo strumento UniFFI e i tratti asincroni, tutti elementi chiave per la costruzione di software robusto e sicuro.


**Sezione 4: Sviluppo di LNP/BP con SDK**

Imparerete a sviluppare i nodi LN utilizzando vari SDK come l'SDK Breez e Greenlight per Lipa. Vedrete come implementare le applicazioni Lightning Network utilizzando le librerie progettate per semplificare lo sviluppo di Bitcoin e Lightning.


Siete pronti a far crescere le vostre abilità nel Lightning Network con Rust? Andiamo!

# Imparare a codificare con il libro rust

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Introduzione al Rust

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Installazione e gestione di Rust con Rustup


Quando si inizia il viaggio con Rust, il primo passo è la creazione di un ambiente di sviluppo adeguato. L'approccio più consigliato per l'installazione di Rust è Rustup, un sistema di gestione della toolchain che gestisce l'installazione e gli aggiornamenti su diversi progetti e piattaforme.


Rustup non è un semplice programma di installazione, ma uno strumento di gestione completo per l'ambiente di sviluppo Rust. Con Rustup è possibile installare facilmente target di compilazione aggiuntivi per piattaforme diverse, come ARM64 per lo sviluppo di Android o altre architetture da supportare. Lo strumento gestisce anche gli aggiornamenti di Rust senza problemi, il che è particolarmente prezioso dato che Rust rilascia una nuova versione stabile ogni sei settimane circa. Quando è necessario aggiornare all'ultima versione, un semplice comando `rustup update` gestisce tutto automaticamente.


Quando si installa Rustup, vale la pena di capire il modello di sicurezza coinvolto. Il processo di installazione scarica ed esegue uno script dal sito ufficiale di Rust tramite HTTPS, che fornisce una sicurezza crittografica a livello di trasporto. I pacchetti scaricati da Rustup e Cargo provengono da fonti affidabili (crates.io e l'infrastruttura ufficiale di Rust) e beneficiano della crittografia HTTPS. Sebbene questo approccio sia sicuro per la maggior parte degli scenari di sviluppo, alcune organizzazioni con politiche di sicurezza rigorose potrebbero preferire l'installazione di Rust attraverso il gestore di pacchetti della loro distribuzione Linux, che fornisce un ulteriore livello di fiducia attraverso l'infrastruttura di firma dei pacchetti della distribuzione stessa. Per l'apprendimento e lo sviluppo in generale, Rustup è uno strumento ben consolidato e ampiamente affidabile nell'ecosistema Rust.


Per la maggior parte degli scenari di sviluppo, potete installare Rustup eseguendo lo script di installazione fornito sul sito ufficiale di Rust. Il programma di installazione vi chiederà di scegliere tra diverse opzioni di toolchain, con la scelta consigliata dalla maggior parte degli utenti. Il programma di installazione vi chiederà di scegliere tra diverse opzioni di toolchain, con la toolchain stabile che è la scelta consigliata per la maggior parte degli utenti. L'installazione avviene nella vostra home directory, non richiede privilegi di amministratore e imposta tutte le variabili d'ambiente necessarie per un uso immediato.


### Comprendere le catene di strumenti e i componenti del Rust


L'ecosistema di sviluppo di Rust è costituito da diversi componenti chiave che lavorano insieme per fornire un ambiente di programmazione completo. La comprensione di questi componenti aiuta a navigare nel processo di sviluppo del Rust in modo più efficace e a risolvere i problemi che si presentano.


Il compilatore Rust, noto come `rustc`, costituisce il nucleo della catena di strumenti Rust. Anche se in teoria si potrebbe usare direttamente `rustc` per compilare i programmi Rust, la maggior parte del lavoro di sviluppo si affida a Cargo, il gestore di pacchetti e il sistema di compilazione di Rust. Cargo funziona in modo simile a npm nell'ecosistema JavaScript, gestendo le dipendenze, coordinando le compilazioni e fornendo comodi comandi per le attività di sviluppo più comuni. Quando si eseguono comandi come `cargo build` o `cargo run`, Cargo orchestra il processo di compilazione, gestisce la risoluzione delle dipendenze e gestisce la struttura complessiva del progetto.


Clippy è un linter che analizza il codice e fornisce suggerimenti per migliorarlo. A differenza dei controllori di sintassi di base, Clippy comprende gli idiomi del Rust e può consigliare modi più idiomatici per svolgere compiti specifici. Questo strumento aiuta ad apprendere le migliori pratiche di Rust e a scrivere codice più manutenibile.


La toolchain Rust include anche strumenti di documentazione completi e la documentazione della libreria standard, accessibile attraverso il sito web ufficiale della documentazione Rust. Questa documentazione è un riferimento indispensabile durante lo sviluppo e fornisce informazioni dettagliate su funzioni, tipi e moduli della libreria standard. La documentazione comprende esempi e spiegazioni esaurienti che aiutano a capire non solo cosa fanno le funzioni, ma anche come usarle efficacemente nei programmi.


Rust supporta diversi canali di rilascio: stabile, beta e nightly. Il canale stabile fornisce versioni accuratamente testate e adatte all'uso in produzione. Il canale beta offre un'anteprima della prossima versione stabile, utilizzata principalmente per i test finali prima del rilascio ufficiale. Il canale nightly include funzionalità sperimentali in fase di sviluppo attivo, che possono essere utili per provare nuove funzionalità di Rust, anche se queste funzionalità potrebbero cambiare o essere rimosse nelle versioni future.


### Creazione e gestione di progetti Rust con Cargo


Lo sviluppo moderno di Rust è incentrato su Cargo, che semplifica la creazione di progetti, la gestione delle dipendenze e il processo di compilazione. Invece di creare manualmente directory e file, Cargo fornisce il comando `cargo new` per generate una struttura di progetto completa con valori predefiniti ragionevoli.


Quando si crea un nuovo progetto con `cargo new project_name`, Cargo stabilisce una struttura di directory standard, crea un file `main.rs` di base con un programma "Hello, world!", inizializza un repository Git e genera un file `Cargo.toml` per la configurazione del progetto. Il file `Cargo.toml` serve come punto centrale di configurazione del progetto, contenendo metadati sul progetto ed elencando tutte le dipendenze richieste dal codice.


Cargo fornisce diversi comandi essenziali per il lavoro di sviluppo quotidiano. Il comando `cargo build` compila il progetto e le sue dipendenze, creando file eseguibili nella directory `target`. Per una rapida iterazione durante lo sviluppo, `cargo run` combina la compilazione e l'esecuzione in un unico passaggio. Il comando `cargo check` esegue tutti i controlli di compilazione senza generare l'eseguibile finale, rendendolo significativamente più veloce di una compilazione completa quando si vuole semplicemente verificare che il codice venga compilato correttamente.


Quando si prepara il codice per la distribuzione in produzione, il flag `--release` abilita le ottimizzazioni e rimuove le asserzioni di debug. I build di rilascio vengono eseguiti più velocemente e producono eseguibili più piccoli, ma richiedono più tempo per la compilazione e rimuovono le informazioni utili per il debug. Il compilatore applica varie ottimizzazioni durante i build di rilascio e disabilita i controlli di runtime, come il rilevamento degli overflow dei numeri interi, migliorando le prestazioni ma eliminando alcune garanzie di sicurezza presenti nei build di debug.


### Variabili, mutabilità e filosofia di sicurezza di Rust


Rust adotta un approccio diverso alla gestione delle variabili rispetto alla maggior parte dei linguaggi. Per impostazione predefinita, tutte le variabili in Rust sono immutabili, il che significa che i loro valori non possono essere modificati dopo l'assegnazione iniziale. Questa scelta progettuale ha lo scopo di prevenire i comuni errori di programmazione che derivano da cambiamenti di stato inaspettati.


Quando si dichiara una variabile con `let x = 5`, questa diventa immutabile per impostazione predefinita. Qualsiasi tentativo di modificare il suo valore in seguito risulterà in un errore di compilazione. Questo requisito di immutabilità costringe gli sviluppatori a riflettere attentamente su quando i cambiamenti di stato sono veramente necessari e rende il comportamento del codice più prevedibile. Molti bug di programmazione derivano da variabili che cambiano inaspettatamente, e l'immutabilità predefinita di Rust aiuta a prevenire questi problemi.


Quando si ha realmente bisogno di modificare il valore di una variabile, Rust richiede una dichiarazione esplicita di mutabilità utilizzando la parola chiave `mut`: `let mut x = 5`. Questa dichiarazione esplicita serve a segnalare chiaramente al compilatore e agli altri sviluppatori che il valore di questa variabile può cambiare durante l'esecuzione del programma. L'obbligo di dichiarare esplicitamente la mutabilità incoraggia a valutare attentamente se la mutabilità è veramente necessaria per ogni variabile.


Rust supporta anche lo shadowing, che consente di dichiarare una nuova variabile con lo stesso nome di una variabile precedente. A differenza della mutazione, l'ombreggiatura crea una variabile completamente nuova che ha lo stesso nome, nascondendo di fatto la variabile precedente. Questa tecnica si rivela particolarmente utile quando si trasformano i dati attraverso più passaggi, come ad esempio il parsing di una stringa in un numero e la successiva elaborazione di tale numero. Con l'ombreggiatura, è possibile mantenere un nome di variabile coerente per tutto il processo di trasformazione, pur cambiando il tipo di variabile a ogni passaggio.


La distinzione tra ombreggiatura e mutazione diventa importante quando si considerano i cambiamenti di tipo. Con l'ombreggiatura si possono cambiare sia il valore che il tipo di una variabile, perché si sta creando una nuova variabile. Con la mutazione, invece, si può cambiare solo il valore mantenendo lo stesso tipo, poiché si sta modificando una variabile esistente anziché crearne una nuova.


```rust
// Shadowing: creating new variables with the same name
let amount = "100000";           // amount is a &str (string slice)
let amount = amount.parse::<u64>().unwrap();  // amount is now u64
let amount = amount * 100;       // amount is still u64, new value

// Mutation: modifying the same variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: same type, different value
// balance = "empty";            // ERROR: cannot change type with mutation

// Practical example: processing a Bitcoin amount input
let user_input = "  0.001 ";                    // &str with whitespace
let user_input = user_input.trim();            // &str, whitespace removed
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Amount in satoshis: {}", satoshis);  // 100000
```


### Tipi di dati e fondamenti del sistema dei tipi


Rust implementa un sistema di tipi forte e statico, in cui ogni valore deve avere un tipo ben definito conosciuto al momento della compilazione. Sebbene ciò possa sembrare restrittivo rispetto ai linguaggi a tipizzazione dinamica, le capacità di inferenza dei tipi di Rust consentono di specificare raramente i tipi in modo esplicito. Il compilatore è in grado di determinare il tipo appropriato in base all'uso che si fa del valore.


Tuttavia, alcune situazioni richiedono annotazioni esplicite sul tipo. Quando si usano funzioni generiche come `parse()`, che possono convertire stringhe in vari tipi numerici, il compilatore deve sapere quale tipo specifico si desidera. In questi casi, si forniscono annotazioni sul tipo usando la sintassi dei due punti: `indovina: u32 = "42".parse().expect("Non è un numero!")`.


I tipi scalari di Rust includono numeri interi, numeri in virgola mobile, booleani e caratteri. Il sistema di tipi interi fornisce un controllo preciso sull'utilizzo della memoria e sulle caratteristiche delle prestazioni. I tipi di interi sono denominati sistematicamente: `i8`, `i16`, `i32`, `i64` e `i128` per i numeri interi firmati e `u8`, `u16`, `u32`, `u64` e `u128` per i numeri interi senza segno. I numeri indicano l'ampiezza dei bit, rendendo immediatamente chiaro l'utilizzo della memoria e gli intervalli di valori.


I tipi `isize` e `usize` meritano un'attenzione particolare, poiché si adattano all'architettura di destinazione. Sui sistemi a 64 bit, questi tipi sono larghi 64 bit, mentre sui sistemi a 32 bit sono larghi 32 bit. Questi tipi sono comunemente usati per l'indicizzazione degli array e gli offset di memoria, perché corrispondono alla dimensione naturale delle parole dell'architettura di destinazione, consentendo un'aritmetica efficiente dei puntatori e delle operazioni di memoria.


Rust offre diversi modi per scrivere i letterali interi, compresi i formati decimale, esadecimale (`0x`), ottale (`0o`) e binario (`0b`). È inoltre possibile utilizzare i trattini bassi in qualsiasi punto dei letterali numerici per migliorare la leggibilità, ad esempio scrivendo `1_000_000` invece di `1000000`. I trattini bassi non hanno alcun effetto sul valore, ma possono rendere più leggibili i numeri grandi.


I tipi in virgola mobile in Rust sono semplici: `f32` per i numeri in virgola mobile a singola precisione e `f64` per i numeri in virgola mobile a doppia precisione. Il tipo `f64` è generalmente preferito per la sua maggiore precisione e per il fatto che i moderni processori possono spesso gestire le operazioni a virgola mobile a 64 bit con la stessa efficienza di quelle a 32 bit.


### Tipi composti e organizzazione dei dati


Oltre ai tipi scalari, Rust offre tipi composti che raggruppano più valori. Le tuple consentono di combinare valori di tipo diverso in un unico valore composto. Si creano tuple usando le parentesi e si può specificare il tipo di ogni elemento: `let tup: (i32, f64, u8) = (500, 6.4, 1)`.


Le tuple supportano la destrutturazione, che consente di estrarre i singoli valori: `let (x, y, z) = tup`. Questa sintassi crea tre variabili separate dai componenti della tupla. In alternativa, si può accedere direttamente agli elementi della tupla usando la notazione a punti con l'indice dell'elemento: `tup.0`, `tup.1`, `tup.2`.


```rust
// Creating a tuple with different types
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Destructuring: extract all values at once
let (txid, amount, confirmed) = transaction;
println!("Transaction {} for {} sats", txid, amount);

// Dot notation: access individual elements by index
println!("Confirmed: {}", transaction.2);  // true

// Practical example: function returning multiple values
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Returns (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```


Gli array in Rust differiscono in modo significativo dagli array o dalle liste in molti altri linguaggi perché hanno una dimensione fissa che diventa parte del loro tipo. Un array di cinque interi ha il tipo `[i32; 5]`, dove il punto e virgola separa il tipo di elemento dalla lunghezza dell'array. Queste informazioni sulla dimensione a livello di tipo consentono al compilatore di eseguire il controllo dei limiti e assicurano che le funzioni che ricevono gli array sappiano esattamente quanti elementi aspettarsi.


È possibile inizializzare gli array elencando esplicitamente tutti gli elementi: `[1, 2, 3, 4, 5]`, oppure utilizzando una sintassi abbreviata per gli array con valori ripetuti: `[3; 5]` crea una matrice di cinque elementi, tutti con il valore 3. Questa stenografia è utile per inizializzare i buffer o per creare array con valori predefiniti.


L'accesso agli array utilizza la notazione delle parentesi quadre come la maggior parte dei linguaggi, ma Rust fornisce un controllo dei limiti sia in fase di compilazione che di esecuzione. Quando si accede a un array con un indice costante che il compilatore è in grado di verificare, il compilatore cattura gli accessi fuori limite in tempo di compilazione. Per gli indici dinamici determinati in fase di esecuzione, Rust inserisce controlli sui limiti che causano il panico del programma se si tenta di accedere a un indice non valido, prevenendo le violazioni della sicurezza della memoria.



## Ownership e sicurezza della memoria in Rust

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Capire l'approccio unico di Rust alla gestione della memoria


Questo capitolo tratta uno dei concetti più importanti del Rust. Mentre i concetti precedenti possono sembrare familiari ai programmatori che provengono da altri linguaggi, la proprietà è l'approccio di Rust per risolvere la sicurezza della memoria senza garbage collection.


Rust è stato progettato con l'obiettivo fondamentale di prevenire i bug legati alla memoria che affliggono i linguaggi di basso livello come C e C++. Questi problemi includono i bug use-after-free, in cui si accede alla memoria dopo che è stata rilasciata, e i buffer overflow, in cui i programmi scrivono al di fuori dei confini della memoria allocata. Le soluzioni tradizionali a questi problemi hanno comportato compromessi che Rust cerca di eliminare. I linguaggi di livello superiore come Java e Go risolvono la sicurezza della memoria attraverso la garbage collection, in cui un processo automatico identifica e libera periodicamente la memoria inutilizzata. Tuttavia, i garbage collector introducono un sovraccarico di prestazioni e possono causare pause imprevedibili durante l'esecuzione del programma, rendendoli inadatti alla programmazione di sistemi in cui le prestazioni costanti sono fondamentali.


Rust ottiene la sicurezza della memoria principalmente attraverso l'analisi statica eseguita in fase di compilazione. Il compilatore esamina il codice sorgente e può determinare se la maggior parte delle operazioni di memoria sono sicure senza richiedere la garbage collection. Per i casi che non possono essere verificati staticamente, come ad esempio l'accesso ad array con indici calcolati in tempo reale, Rust inserisce controlli sui limiti che mettono in panico piuttosto che consentire un comportamento non definito. Questo approccio differisce fondamentalmente dagli analizzatori statici disponibili per C e C++, che sono stati adattati a linguaggi non originariamente progettati per un'analisi statica completa. La sintassi e le regole del linguaggio di Rust sono state create da zero per consentire un'ampia verifica in tempo di compilazione, assicurando che, una volta compilato con successo un programma, questo venga eseguito in modo sicuro o vada in panico in modo prevedibile, anziché presentare un comportamento non definito.


### Il sistema Ownership: Regole e principi


La pietra angolare delle garanzie di sicurezza della memoria di Rust è il sistema di proprietà, che regola la gestione della memoria durante l'esecuzione di un programma. Ownership si basa su tre regole fondamentali che il compilatore applica in ogni momento:


1. Ogni valore in Rust ha un proprietario (una variabile che contiene il valore)

2. Può esserci un solo proprietario alla volta

3. Quando il proprietario esce dall'ambito, il valore viene eliminato


Gli scope in Rust sono tipicamente definiti da parentesi graffe, sia nei corpi delle funzioni, sia nei blocchi condizionali, sia nei blocchi di scope creati esplicitamente. Quando una variabile viene dichiarata all'interno di un ambito, quell'ambito diventa il proprietario del valore della variabile. La variabile rimane accessibile e valida per tutta la durata dell'ambito, ma non appena l'esecuzione lascia l'ambito, tutte le variabili possedute vengono automaticamente ripulite attraverso un processo chiamato dropping.


Questa pulizia automatica è implementata attraverso il meccanismo di drop di Rust, in cui il linguaggio chiama implicitamente una funzione di drop sulle variabili che escono dallo scope. Per i tipi di base, questo significa semplicemente che la memoria viene contrassegnata come disponibile per il riutilizzo. Per i tipi più complessi che gestiscono risorse, le implementazioni personalizzate di drop possono eseguire ulteriori operazioni di pulizia, come la chiusura di handle di file o il rilascio di connessioni di rete. Questo modello, mutuato dal RAII (Resource Acquisition Is Initialization) del C++, garantisce che le risorse siano sempre rilasciate correttamente, senza richiedere un codice di pulizia esplicito da parte del programmatore.


### Spostamento del Ownership e layout di memoria


Per comprendere il modo in cui la proprietà viene trasferita tra le variabili è necessario esaminare la differenza tra i tipi semplici e i tipi complessi in termini di layout della memoria e di comportamento di copia. I tipi semplici, come gli interi, i booleani e i numeri a virgola mobile, hanno una dimensione fissa e nota al momento della compilazione e possono essere copiati in modo efficiente. Quando si assegna una variabile intera a un'altra, Rust crea una copia completa e indipendente del valore, consentendo a entrambe le variabili di esistere contemporaneamente senza problemi di proprietà.


I tipi complessi come le stringhe rappresentano una sfida diversa perché gestiscono la memoria allocata dinamicamente. Una stringa in Rust consiste in tre componenti memorizzati sullo stack: un puntatore ai dati dei caratteri allocati nell'heap, la lunghezza corrente della stringa e la capacità totale del buffer allocato. Questa struttura consente alle stringhe di crescere e ridursi in modo efficiente, mantenendo la conoscenza dei loro confini. Quando si assegna una variabile String a un'altra, Rust si trova di fronte a una scelta: può copiare solo la struttura basata sullo stack (creando due puntatori agli stessi dati dell'heap) o eseguire una copia profonda di tutti i dati dell'heap.


Il comportamento predefinito di Rust è quello di spostare la proprietà piuttosto che copiare, trasferendo i dati dell'heap dalla variabile di origine a quella di destinazione e invalidando l'origine. Questo approccio evita il pericoloso scenario in cui più variabili potrebbero modificare la stessa memoria heap o in cui la stessa memoria potrebbe essere liberata più volte quando le variabili escono dallo scope. L'operazione di spostamento è efficiente perché copia solo la piccola struttura basata sullo stack, non i dati potenzialmente grandi dell'heap, e mantiene la sicurezza della memoria garantendo la proprietà singola.


### Referenze e prestiti


Sebbene gli spostamenti di proprietà forniscano sicurezza, possono essere restrittivi quando è necessario utilizzare un valore in più punti senza trasferire la proprietà. Rust risolve questo problema con il prestito, che consente a funzioni e variabili di accedere temporaneamente ai dati senza assumerne la proprietà. Un riferimento, creato con l'operatore ampersand, consente di accedere in sola lettura a un valore lasciando la proprietà alla variabile originale.


I riferimenti consentono alle funzioni di operare sui dati senza consumarli, rendendo possibile l'utilizzo dello stesso valore più volte in un programma. Quando si passa un riferimento a una funzione, si prestano temporaneamente i dati e la funzione deve restituire il riferimento prima che il proprietario originale possa riprendere il pieno controllo. Questa metafora del prestito riflette la natura temporanea dell'accesso: così come si può prestare un libro a un amico mantenendone la proprietà, i riferimenti consentono un accesso temporaneo, pur conservando la relazione di proprietà originale.


I riferimenti mutabili estendono questo concetto per consentire la modifica di dati presi in prestito, ma con severe restrizioni per mantenere la sicurezza. Rust consente un solo riferimento mutabile a un dato dato in qualsiasi momento, impedendo le corse ai dati in cui più parti di un programma potrebbero modificare simultaneamente la stessa memoria. Inoltre, non è possibile avere contemporaneamente riferimenti mutabili e immutabili agli stessi dati, poiché ciò potrebbe portare a situazioni in cui il codice presume che i dati siano stabili mentre altro codice li sta modificando attivamente. Queste regole vengono applicate in fase di compilazione, eliminando intere classi di bug di concorrenza che affliggono altri linguaggi di programmazione di sistema.


```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Immutable borrow: read the balance
let balance_ref = &wallet_balance;
println!("Current balance: {} sats", balance_ref);
// balance_ref goes out of scope here

// Mutable borrow: update the balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Receive payment
println!("After deposit: {} sats", balance_mut);
// balance_mut goes out of scope here

// Function that borrows immutably
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Function that borrows mutably
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("After fee: {} sats", wallet_balance); // 149,000
}
```


### Tipi di stringhe e fette


Rust distingue tra letterali di stringa e tipo String, che riflettono strategie di gestione della memoria e casi d'uso diversi. I letterali di stringa sono incorporati direttamente nel binario compilato e hanno il tipo &str (string slice), che rappresenta una vista dei dati di stringa immutabili. Questi letterali sono efficienti perché non richiedono l'allocazione in fase di esecuzione, ma non possono essere modificati perché fanno parte del codice del programma.


Il tipo String, invece, gestisce la memoria allocata dinamicamente e può crescere, ridursi ed essere modificato in fase di esecuzione. È possibile creare una String da un letterale utilizzando String::from() o metodi simili, che allocano memoria heap e copiano il contenuto del letterale. Questa distinzione consente a Rust di ottimizzare sia le prestazioni (usando i letterali quando possibile) sia la flessibilità (usando le stringhe quando è necessario modificarle).


Le slice di stringhe (&str) forniscono una potente astrazione per lavorare con porzioni di stringhe senza copiare i dati. Una slice contiene un puntatore all'inizio dei dati della stringa e una lunghezza, consentendo di fare riferimento alle sottostringhe in modo efficiente. La sintassi delle slice utilizza intervalli (ad esempio, &s[0..5]) per specificare a quale porzione della stringa fare riferimento. Poiché le slice sono riferimenti, sono soggette a regole di prestito, che impediscono di modificare la stringa sottostante mentre le slice esistono. Questa applicazione in tempo di compilazione previene bug comuni come l'accesso a memoria non valida dopo che la stringa originale è stata liberata o modificata.


### Array, vettori e fette generiche


Il concetto di slice si estende oltre le stringhe a qualsiasi sequenza di elementi, fornendo un modo unificato di lavorare con array di dimensioni fisse e vettori dinamici. Gli array in Rust hanno la lunghezza codificata nel loro tipo (ad esempio, [i32; 5] per un array di cinque interi a 32 bit), il che li rende adatti a situazioni che richiedono garanzie di dimensione in tempo di compilazione. Le funzioni che accettano array possono imporre requisiti di lunghezza esatti, utili per operazioni come le funzioni crittografiche che richiedono input di dimensioni precise.


Le slice (&[T]) forniscono un'alternativa più flessibile, rappresentando una vista su qualsiasi sequenza contigua di elementi, indipendentemente dalla memorizzazione sottostante. È possibile creare slice da array, vettori o altre slice e la stessa slice può fare riferimento a diverse porzioni di dati durante la sua vita. Questa flessibilità rende le slice ideali per le funzioni che devono elaborare sequenze senza preoccuparsi del meccanismo di memorizzazione specifico o della dimensione esatta.


La relazione tra i tipi posseduti (String, Vec<T>) e le loro controparti a slice (&str, &[T]) segue uno schema coerente in tutto Rust. I tipi posseduti gestiscono la loro memoria e possono essere modificati, mentre le slice forniscono un accesso efficiente e di sola lettura a porzioni di quei dati. Questo design consente di realizzare API flessibili (che accettano vari tipi di input attraverso le fette) ed efficienti (evitando copie non necessarie), mantenendo le garanzie di sicurezza di Rust attraverso il sistema di prestito.



## Strutture, costruzione di tipi di dati complessi

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Le strutture in Rust servono come base per creare tipi di dati complessi, simili alle classi di altri linguaggi di programmazione. Esse consentono di raggruppare dati correlati in un'unica unità coesa che può contenere più campi di tipo diverso. La sintassi per la definizione di una struttura segue uno schema semplice: si usa la parola chiave `struct` seguita dal nome della struttura, quindi si definiscono i campi all'interno di parentesi graffe, usando una sintassi di due punti per specificare il tipo di ogni campo.


Rust segue specifiche convenzioni di denominazione per le strutture, che il compilatore applicherà tramite avvisi. I nomi delle strutture devono usare CamelCase (noto anche come PascalCase), mentre i nomi dei campi all'interno della struttura devono usare snake_case con trattini bassi. Questa convenzione aiuta a mantenere la coerenza tra le basi di codice di Rust e rende il codice più leggibile per gli altri sviluppatori.


La creazione di istanze di strutture richiede di specificare i valori di tutti i campi utilizzando il nome della struttura seguito da parentesi graffe contenenti le assegnazioni dei campi. Una volta ottenuta un'istanza di struttura, è possibile accedere e modificare i singoli campi utilizzando la notazione a punti, a condizione che l'istanza sia dichiarata mutabile. Questa notazione a punti funziona in modo coerente in Rust, a differenza di linguaggi come il C++, dove si possono usare operatori diversi per i puntatori rispetto agli oggetti diretti.


### Funzioni del costruttore e scorciatoie di campo


Rust non dispone di costruttori incorporati come alcuni linguaggi orientati agli oggetti, ma è possibile creare funzioni che restituiscono istanze di strutture con lo stesso scopo. Queste funzioni costruttrici in genere accettano parametri per alcuni o tutti i campi e possono impostare valori predefiniti per altri. Quando si scrivono tali funzioni, Rust fornisce una comoda stenografia: se un parametro ha lo stesso nome di un campo della struttura, si può semplicemente scrivere il nome del campo una volta sola, invece di ripeterlo nel formato `campo: valore'.


Le istanze di struttura possono essere create anche copiando i valori da istanze esistenti, utilizzando la sintassi struct update. Questa funzione consente di creare una nuova istanza specificando solo i campi che si desidera modificare, mentre tutti gli altri campi vengono copiati da un'istanza esistente. Tuttavia, questa operazione segue le regole di proprietà di Rust, il che significa che i tipi non copiati verranno spostati dall'istanza di partenza, rendendo potenzialmente inutilizzabili parti dell'istanza originale. Il compilatore tiene traccia di questi spostamenti parziali in modo intelligente, consentendo di continuare a utilizzare i campi che non sono stati spostati e impedendo l'accesso ai campi spostati.


### Strutture di tuple e strutture di unità


Rust supporta le strutture a tupla, che sono strutture con campi senza nome a cui si accede per indice anziché per nome. Sono utili per i tipi wrapper semplici o quando si ha bisogno di una struttura ma non di campi con nome. Si accede ai campi delle strutture a tupla usando la notazione a punti seguita dall'indice del campo, come `.0` per il primo campo, `.1` per il secondo e così via. Questo approccio funziona bene per le strutture che racchiudono un singolo valore o che contengono solo pochi valori strettamente correlati, per i quali i nomi potrebbero essere ridondanti.


Le strutture unitarie rappresentano la forma più semplice di struttura: non contengono alcun dato. Anche se inizialmente potrebbe sembrare inutile, le strutture unitarie diventano preziose quando si lavora con il sistema di tratti del Rust, in quanto possono implementare comportamenti senza memorizzare alcun dato. Queste strutture vuote servono come marcatori o segnaposto in modelli Rust più avanzati.


### Metodi e funzioni associate


Le strutture ottengono funzionalità aggiuntive quando si aggiungono comportamenti attraverso blocchi di implementazione. Usando la parola chiave `impl` seguita dal nome della struttura, si possono definire metodi che operano sulle istanze della struttura. I metodi sono funzioni che prendono `self` come primo parametro, che può essere un valore posseduto (`self`), un riferimento immutabile (`&self`) o un riferimento mutabile (`&mut self`), a seconda di ciò che il metodo deve fare con l'istanza.


La scelta del tipo di parametro `self` determina il comportamento del metodo rispetto alla proprietà. I metodi che prendono `&self` possono leggere dall'istanza senza assumerne la proprietà, il che li rende adatti a operazioni che non modificano la struttura. I metodi che prendono `&mut self` possono modificare l'istanza, pur consentendo al chiamante di mantenere la proprietà. I metodi che prendono `self` come valore consumano l'istanza, il che è appropriato per operazioni che trasformano la struttura in qualcos'altro o quando il metodo rappresenta l'operazione finale su quell'istanza.


Le funzioni associate sono funzioni definite all'interno di un blocco di implementazione che non prendono `self' come parametro. Sono simili ai metodi statici di altri linguaggi e sono comunemente usate come costruttori o funzioni di utilità relative al tipo. Le funzioni associate si chiamano usando la sintassi dei due punti (`Tipo::nome_funzione()`), che le distingue chiaramente dai metodi chiamati sulle istanze.


```rust
// Define a struct for a Lightning invoice
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}

impl Invoice {
// Associated function (constructor) - no self parameter
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // default 1 hour
}
}

// Method with &self - read-only access
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Method with &mut self - can modify the instance
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Method with self - consumes the instance
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Use associated function to create instance
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats in millisats
"Coffee payment".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // Add 30 minutes

let request = invoice.into_payment_request();
// invoice is now consumed, cannot be used anymore
println!("Payment request: {}", request);
}
```


#### Enumerazioni: Modellare scelte e varianti


Le enumerazioni in Rust hanno maggiori capacità rispetto alle enumerazioni di molti altri linguaggi. Sebbene possano rappresentare semplici insiemi di costanti denominate, gli enum di Rust possono anche contenere dati all'interno di ogni variante, rendendoli adatti a modellare situazioni in cui un valore può essere di diversi tipi o stati. Ogni variante di enum può contenere diversi tipi e quantità di dati, da nessun dato a strutture complesse con campi denominati.


La possibilità di allegare dati alle varianti di enum elimina molti errori di programmazione comuni in altri linguaggi. Invece di mantenere variabili separate per un indicatore di tipo e per i dati associati, che possono facilmente diventare incoerenti, gli enum Rust raggruppano le informazioni sul tipo con i dati stessi. Questa struttura garantisce che i dati corrispondano sempre alla variante, evitando errori di corrispondenza che potrebbero causare errori di esecuzione.


Le varianti di enum possono contenere dati in diverse forme: nessun dato per i semplici flag, dati simili a tuple per i campi senza nome o dati simili a strutture con campi con nome. Si possono anche mescolare questi stili all'interno di un singolo enum, scegliendo la forma più appropriata per ogni variante. Questa flessibilità rende gli enum adatti a modellare concetti di dominio complessi, in cui casi diversi richiedono informazioni diverse.


#### Il tipo di opzione: Gestire le assenze in modo sicuro


Uno degli enum più importanti di Rust è `Option<T>`, che rappresenta valori che possono essere presenti o meno. Questo enum ha due varianti: `Some(T)` che contiene un valore di tipo T e `None` che rappresenta l'assenza di un valore. Il tipo Option è la soluzione di Rust ai problemi dei puntatori nulli che affliggono molti altri linguaggi, costringendo gli sviluppatori a gestire esplicitamente i casi in cui i valori potrebbero mancare.


L'uso dei tipi di opzione rende il codice più robusto, perché il compilatore richiede di gestire sia la presenza che l'assenza di valori. Non è possibile utilizzare accidentalmente un valore potenzialmente mancante senza prima verificare se esiste. Questa gestione esplicita previene le eccezioni relative ai puntatori nulli e simili errori di runtime che sono fonti comuni di bug in altri linguaggi di programmazione.


Il tipo Option si integra con il sistema di pattern matching di Rust, consentendo di gestire entrambi i casi. Metodi come `unwrap_or()` forniscono modi convenienti per estrarre valori con default di ripiego, mentre metodi come `map()` e `and_then()` permettono di utilizzare modelli di programmazione funzionale per lavorare con valori opzionali.


### Corrispondenza dei modelli con le espressioni di corrispondenza


La corrispondenza dei pattern attraverso le espressioni `match` fornisce un modo per lavorare con gli enum e altri tipi di dati. Un'espressione di corrispondenza esamina un valore ed esegue codice diverso in base allo schema a cui il valore corrisponde. Ogni schema può destrutturare il valore corrispondente, legando parti di esso a variabili che possono essere usate nel blocco di codice corrispondente.


Le espressioni di corrispondenza devono essere esaustive, cioè devono gestire tutti i casi possibili per il tipo che viene abbinato. Questo requisito previene i bug che potrebbero verificarsi se alcuni casi fossero accidentalmente non gestiti. Quando non si vuole gestire esplicitamente tutti i casi, si può usare il pattern jolly (`_`) per catturare tutti i casi rimanenti, oppure legare i casi non gestiti a una variabile, se si ha bisogno di accedere al valore.


Il costrutto `if let' fornisce un'alternativa più concisa a match, quando ci si preoccupa solo di un modello specifico. Questa sintassi è particolarmente utile quando si lavora con i tipi Option o quando si vuole eseguire del codice solo se un valore corrisponde a una particolare variante di enum. Il costrutto `if let' può includere una clausola `else' per i casi in cui lo schema non corrisponde, rendendolo un modo semplificato per gestire semplici scenari di corrispondenza di schemi.


#### Collezioni: Gestione di gruppi di dati


La libreria standard di Rust fornisce diversi tipi di collezioni per gestire gruppi di dati correlati. Queste raccolte sono generiche, cioè possono memorizzare elementi di qualsiasi tipo e gestiscono automaticamente la memoria. Le collezioni più utilizzate sono i vettori per gli elenchi ordinati, le mappe hash per le associazioni chiave-valore e le stringhe per i dati di testo.


#### Vettori: Array dinamici


I vettori rappresentano matrici che possono crescere e cambiare dimensione durante l'esecuzione del programma. A differenza degli array a dimensione fissa, i vettori allocano memoria sull'heap e possono espandersi o ridursi secondo le necessità. La creazione di un vettore richiede spesso l'annotazione esplicita del tipo quando si inizia con un vettore vuoto, poiché il compilatore deve sapere quale tipo di elementi conterrà il vettore.


I vettori offrono diversi modi per accedere agli elementi, ciascuno con caratteristiche di sicurezza diverse. La notazione per indici (`vec[0]`) fornisce un accesso diretto, ma va in panico se l'indice è fuori dai limiti. Il metodo `get()` restituisce un'opzione `Option`, consentendo di gestire con grazia l'accesso fuori dai limiti. La scelta tra questi approcci dipende dalla possibilità di garantire la validità dell'indice o dalla necessità di gestire potenziali fallimenti.


Le regole di prestito di Rust si applicano ai vettori, impedendo i comuni problemi di sicurezza della memoria. Se si tiene un riferimento a un elemento del vettore, non si può modificare il vettore finché quel riferimento non esce dall'ambito. In questo modo si evitano situazioni in cui i riferimenti potrebbero puntare a memoria deallocata dopo operazioni vettoriali come l'inserimento di nuovi elementi o la cancellazione del vettore.


#### Mappe Hash: Memorizzazione di valori-chiave


Le mappe Hash forniscono un'efficiente archiviazione chiave-valore, dove è possibile cercare rapidamente i valori in base alle chiavi associate. Sia le chiavi che i valori possono essere di qualsiasi tipo, anche se le chiavi devono implementare i tratti necessari per l'hashing e il confronto di uguaglianza. Le mappe Hash assumono la proprietà dei valori inseriti, a meno che questi non implementino il tratto Copy.


Le mappe Hash offrono diversi metodi per inserire e aggiornare i valori. Il metodo di base `insert()` sovrascrive i valori esistenti, mentre `entry()` fornisce una logica di inserimento più flessibile. Il metodo entry API consente di inserire valori solo se non esistono già, o di aggiornare valori esistenti in base al loro stato attuale. Questo API è utile per schemi come il conteggio delle occorrenze o il mantenimento di totali correnti.


Quando si recuperano valori da mappe hash, il metodo `get()` restituisce una `Option`, poiché la chiave richiesta potrebbe non esistere. Si possono usare metodi come `copied()` per convertire da `Option<&T>` a `Option<T>` per i tipi Copy e `unwrap_or()` per fornire valori predefiniti quando mancano le chiavi.


### Gestione delle stringhe e Unicode


Le stringhe in Rust sono codificate UTF-8, il che fornisce il pieno supporto di Unicode, ma introduce una certa complessità rispetto alle semplici stringhe di ASCII. Il tipo `String` rappresenta i dati di testo posseduti e crescenti, mentre le fette di stringa (`&str`) forniscono viste mutuate dei dati di stringa. È possibile convertire questi tipi a seconda delle necessità; le fette di stringa sono spesso utilizzate per i parametri delle funzioni, per accettare sia stringhe di proprietà che letterali di stringa.


La manipolazione delle stringhe comprende metodi per l'aggiunta di testo, la formattazione di più valori insieme e l'estrazione di sottostringhe. Il metodo `push_str()` aggiunge fette di stringa senza assumerne la proprietà, mentre la macro `format!` fornisce un modo flessibile per costruire stringhe da più componenti. Quando si lavora con gli indici di stringa, bisogna fare attenzione a rispettare i limiti dei caratteri UTF-8 per evitare il panico del runtime.


Per un'elaborazione sicura carattere per carattere, le stringhe forniscono metodi iteratori come `chars()` per i valori scalari Unicode e `bytes()` per l'accesso ai byte grezzi. Questi iteratori gestiscono correttamente la codifica UTF-8, assicurando che non vengano accidentalmente divisi caratteri multi-byte. Questo approccio è più sicuro e affidabile dell'indicizzazione manuale, soprattutto quando si lavora con testi internazionali che possono contenere caratteri Unicode complessi.



## Il sistema di gestione degli errori a due categorie del Rust

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust adotta un approccio fondamentalmente diverso alla gestione degli errori rispetto alla maggior parte dei linguaggi di programmazione. Mentre molti linguaggi si basano principalmente sulle eccezioni, Rust distingue due categorie distinte di errori e fornisce meccanismi specifici per la gestione di ciascun tipo. Questo capitolo esplora il sistema completo di gestione degli errori di Rust, che comprende sia gli errori irrecuperabili, che interrompono l'esecuzione del programma, sia gli errori recuperabili, che consentono ai programmi di continuare a funzionare in modo corretto.


### Errori irrecuperabili e panico


Gli errori irrecuperabili rappresentano situazioni in cui il programma è entrato in uno stato incoerente o inaspettato da cui non può riprendersi in modo sicuro. Si tratta di scenari come l'accesso a un array fuori dai limiti, il tentativo di operazioni che violano la sicurezza della memoria o il verificarsi di condizioni che indicano errori fondamentali nella logica del programma. Quando si verificano questi errori, la risposta appropriata è quella di terminare immediatamente il programma piuttosto che rischiare ulteriori corruzioni o comportamenti non definiti.


In Rust, gli errori irrecuperabili scatenano un panico, che causa l'arresto del programma in modo controllato. Prima di terminare, Rust esegue un processo chiamato unwinding, in cui ripercorre lo stack delle chiamate per fornire una traccia dettagliata dello stack che mostra esattamente dove si è verificato il panico. Questo processo di unwinding aiuta gli sviluppatori a identificare l'origine del problema durante il debug. Per le applicazioni critiche dal punto di vista delle prestazioni o per i sistemi embedded, è possibile disabilitare l'unwinding e configurare Rust in modo che si interrompa immediatamente quando si verifica un panico, anche se in questo modo si sacrificano le informazioni di debug per una terminazione più rapida.


È possibile innescare un panico in modo esplicito utilizzando la macro `panic!` con un messaggio personalizzato. Quando si verifica un panico, viene visualizzato un output che indica quale thread è andato in panico e il messaggio associato. L'impostazione della variabile d'ambiente `RUST_BACKTRACE` fornisce ulteriori informazioni di debug, mostrando lo stack completo delle chiamate che hanno portato al panico. Ad esempio, se si tenta di accedere all'elemento 99 di un vettore contenente solo tre elementi, generate si troverà di fronte a un panico con un messaggio "index out of bounds" (indice fuori dai limiti), insieme a un backtrace che mostra l'esatta sequenza di chiamate di funzione che hanno portato all'errore.


### Errori recuperabili con risultato


Gli errori recuperabili rappresentano condizioni di errore previste che i programmi possono gestire con grazia senza terminare. Esempi sono il tentativo di aprire un file che non esiste, i fallimenti della connessione di rete o l'immissione di dati non validi da parte dell'utente. Per queste situazioni, Rust fornisce l'enum `Result`, che rappresenta esplicitamente le operazioni che potrebbero fallire e costringe gli sviluppatori a gestire sia i casi di successo che quelli di fallimento.


L'enum `Result` è definito con due varianti: `Ok(T)` per le operazioni riuscite che contengono un valore di tipo `T` e `Err(E)` per i fallimenti che contengono un errore di tipo `E`. Questo progetto utilizza il sistema di tipi di Rust per garantire che i potenziali fallimenti non possano essere ignorati. Le funzioni che potrebbero fallire restituiscono un `risultato` e il codice chiamante deve gestire esplicitamente sia il caso di successo che quello di errore, in genere utilizzando la corrispondenza di pattern con le espressioni `match`.


Si consideri la funzione `File::open`, che restituisce un `risultato<File, std::io::Error>`. Quando si apre un file, si riceve un oggetto `File` se l'operazione ha successo o un oggetto `std::io::Error` se l'operazione fallisce. Si può fare un match su questo risultato per gestire ogni caso in modo appropriato. Nel caso di successo, si può procedere con le operazioni sul file, mentre nel caso di errore si può tentare di creare il file, provare un approccio alternativo o propagare l'errore al codice chiamante. Questa gestione esplicita assicura che il programma prenda decisioni consapevoli sul recupero degli errori, invece di bloccarsi inaspettatamente.


### Modelli e scorciatoie per la gestione degli errori


Mentre la corrispondenza esplicita dei pattern fornisce un controllo completo sulla gestione degli errori, Rust offre diversi metodi di convenienza per i più comuni pattern di gestione degli errori. Il metodo `unwrap` estrae il valore di successo da un `Result`, ma va in panico se si verifica un errore, il che lo rende utile per la prototipazione rapida o per situazioni in cui si è sicuri che un'operazione avrà successo. Il metodo `expect` funziona in modo simile, ma consente di fornire un messaggio di panico personalizzato, facilitando il debug quando le cose vanno male.


Per una gestione più flessibile degli errori, metodi come `unwrap_o_else` consentono di fornire una chiusura che viene eseguita quando si verifica un errore, consentendo una logica di recupero personalizzata. È possibile concatenare queste operazioni per gestire scenari complessi, come il tentativo di aprire un file e di crearlo se non esiste, con strategie di gestione degli errori diverse per ogni passaggio.


L'operatore punto interrogativo (`?`) fornisce una sintassi concisa per la propagazione degli errori, che è comune nei programmi Rust. Quando si aggiunge `?` a un `Risultato`, questo operatore scarta automaticamente i valori di successo e restituisce immediatamente gli errori dalla funzione corrente. Questo operatore può essere usato solo nelle funzioni che restituiscono tipi `Result`, assicurando che gli errori possano essere propagati correttamente nello stack delle chiamate. L'operatore `?` rende il codice di gestione degli errori molto più leggibile, eliminando le espressioni di corrispondenza verbose e mantenendo la semantica di propagazione degli errori esplicita.


```rust
use std::fs::File;
use std::io::{self, Read};

// Custom error type for wallet operations
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Function returning Result for recoverable errors
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simulate reading from file
let balance_str = "150000"; // Would normally read from file
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Using the ? operator for clean error propagation
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propagates error if it fails

if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Sent {} sats, remaining: {}", amount, balance - amount))
}

fn main() {
// Handle the Result explicitly
match send_payment(50_000) {
Ok(msg) => println!("Success: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Not enough funds"),
Err(WalletError::FileNotFound) => println!("Error: Wallet file not found"),
Err(WalletError::InvalidFormat) => println!("Error: Corrupted wallet file"),
}

// Or use unwrap_or_else for custom fallback
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```


### Propagazione degli errori e progettazione delle funzioni


La propagazione degli errori è un concetto fondamentale nella gestione degli errori di Rust, che consente alle funzioni di passare gli errori nello stack delle chiamate, anziché gestirli localmente. Quando si progettano funzioni che potrebbero fallire, si dovrebbero restituire tipi `Result` per dare ai chiamanti la flessibilità di decidere come gestire gli errori. Questo approccio promuove la gestione degli errori in modo composito, dove ogni funzione nella catena di chiamate può gestire gli errori localmente o passarli al codice di livello superiore, che ha un contesto più ampio per prendere decisioni di recupero.


L'operatore punto interrogativo semplifica la propagazione degli errori. Invece di scrivere verbose espressioni di corrispondenza per ogni operazione potenzialmente fallimentare, è possibile concatenare le operazioni con gli operatori `?`, creando un codice leggibile che gestisce il percorso di successo mentre propaga automaticamente gli errori che si verificano. Questo schema è così comune che molte funzioni di Rust sono state progettate appositamente per funzionare bene con l'operatore `?`, consentendo una gestione fluida degli errori in tutta la base di codice.


Quando si decide tra il panico e la restituzione di errori, bisogna considerare se il codice chiamante può ragionevolmente recuperare il guasto. Se un fallimento rappresenta un errore di programmazione o uno stato di sistema irrecuperabile, è appropriato il panico. Tuttavia, se il fallimento è una condizione attesa che il codice chiamante potrebbe gestire in modo diverso a seconda del contesto, la restituzione di un `risultato` offre una migliore flessibilità e componibilità.


### Migliori pratiche e considerazioni sulla progettazione


Un'efficace gestione degli errori in Rust richiede un'attenta considerazione di quando è il caso di andare in panico rispetto a quando restituire gli errori. Usate il panico per situazioni che rappresentano errori di programmazione o stati che non dovrebbero mai verificarsi in programmi corretti, come l'accesso a dati codificati in modo rigido che sapete essere validi. Per esempio, l'analisi di una stringa di indirizzi IP codificati in modo rigido, di cui si è verificata la correttezza, può tranquillamente utilizzare `expect` con un messaggio descrittivo che spiega perché l'operazione non dovrebbe mai fallire.


Per gli input controllati dall'utente o per le interazioni con il sistema esterno, si preferisce sempre restituire tipi `Result` piuttosto che andare nel panico. Gli utenti commettono errori, i file vengono cancellati e le connessioni di rete falliscono: sono condizioni normali che i programmi ben progettati dovrebbero gestire con grazia. Restituendo errori per queste situazioni, si permette al codice chiamante di implementare strategie di recupero appropriate, come richiedere all'utente un input diverso, tornare ai valori predefiniti o visualizzare messaggi di errore utili.


Considerare la possibilità di creare tipi personalizzati che impongano la validazione al momento della costruzione, per evitare che gli stati non validi si propaghino nel programma. Ad esempio, se il vostro programma richiede numeri entro un intervallo specifico, create un tipo wrapper che convalidi l'input durante la costruzione e non permetta di creare istanze non valide. Questo approccio utilizza il sistema di tipi di Rust per eliminare intere classi di errori rendendo irrappresentabili gli stati non validi, riducendo la necessità di controllare gli errori in fase di esecuzione in tutta la base di codice.


## Caratteristiche della programmazione funzionale, chiusure e puntatori intelligenti


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Pur non essendo un linguaggio di programmazione funzionale puro, Rust incorpora caratteristiche ispirate ai paradigmi di programmazione funzionale. Queste caratteristiche consentono agli sviluppatori di scrivere codice conciso sfruttando concetti come le chiusure e gli iteratori. Rust include questi elementi funzionali per fornire strumenti flessibili per l'elaborazione dei dati e meccanismi di callback.


Le caratteristiche della programmazione funzionale in Rust mantengono i principi fondamentali del linguaggio, ovvero la sicurezza della memoria e le astrazioni a costo zero. Quando si utilizzano chiusure e iteratori, non si sacrificano le prestazioni per l'espressività: il compilatore di Rust ottimizza questi costrutti per produrre codice macchina efficiente, paragonabile agli approcci tradizionali basati su loop.


### Capire le chiusure


Le chiusure in Rust sono funzioni anonime che possono catturare variabili dall'ambiente circostante. In altri linguaggi di programmazione sono spesso chiamate funzioni lambda. La caratteristica principale delle chiusure è la loro capacità di "chiudere" il loro ambiente, cioè di accedere e utilizzare le variabili che esistono nell'ambito in cui la chiusura è definita.


La sintassi delle chiusure utilizza i caratteri pipe (`|`) invece delle parentesi per definire i parametri. Per una chiusura senza parametri, si scrive `||`, mentre per le chiusure con parametri, li si elenca tra le parentesi come `|x, y|`. Se il corpo della chiusura consiste in una singola espressione, si possono omettere le parentesi graffe, rendendo la sintassi molto concisa.


Consideriamo l'esempio pratico di un'azienda di magliette che regala magliette esclusive in base alle preferenze dei clienti. Se un cliente ha specificato un colore preferito, riceve quel colore; altrimenti, riceve il colore più fornito come predefinito. Utilizzando le chiusure, questa logica diventa: `preferenza_utente.unwrap_o_else(|| self.most_stocked())`. La chiusura `||self.most_stocked()` fornisce il valore predefinito solo quando necessario e può accedere a `self` dal suo ambiente.


### Inferenza del tipo di chiusura e flessibilità


Una delle caratteristiche più comode di Rust con le chiusure è l'inferenza automatica dei tipi. A differenza delle normali funzioni, in cui è necessario specificare esplicitamente i tipi di parametro e di ritorno, le chiusure possono spesso dedurre questi tipi dal contesto. Il compilatore analizza l'uso della chiusura e determina automaticamente i tipi appropriati. Tuttavia, una volta che una chiusura viene chiamata con tipi specifici, tali tipi diventano fissi per quell'istanza di chiusura.


È possibile memorizzare le chiusure nelle variabili come qualsiasi altro valore, rendendole cittadini di prima classe nel linguaggio. Quando si assegna una chiusura a una variabile, è possibile richiamarla in seguito usando le parentesi: `let mia_chiusura = |x| x + 1; let risultato = mia_chiusura(5);`. Questa flessibilità consente di passare le chiusure come argomenti alle funzioni, di restituirle dalle funzioni e di utilizzarle nelle strutture dati.


Se il compilatore non è in grado di dedurre i tipi o se si vuole essere espliciti, si possono annotare i parametri della chiusura e i tipi di ritorno usando una sintassi simile a quella delle funzioni: `|x: i32| -> i32 { x + 1 }`. Questa tipizzazione esplicita è talvolta necessaria in scenari complessi in cui il compilatore ha bisogno di informazioni aggiuntive per risolvere correttamente i tipi.


### Catturare le variabili d'ambiente


Le chiusure possono catturare le variabili dal loro ambiente in tre modi diversi: tramite riferimento immutabile, tramite riferimento mutabile o tramite proprietà. Il compilatore Rust determina automaticamente il metodo di cattura più restrittivo che soddisfa le esigenze della chiusura, seguendo il principio del minimo privilegio.


Quando una chiusura deve solo leggere un valore, lo cattura tramite un riferimento immutabile. Questo permette alla variabile originale di rimanere accessibile anche dopo che la chiusura è stata definita e chiamata. Ad esempio, una chiusura che stampa un elenco prenderà in prestito l'elenco in modo immutabile, consentendo di continuare a utilizzare l'elenco dopo l'esecuzione della chiusura.


Se una chiusura deve modificare una variabile catturata, deve catturarla con un riferimento mutabile. In questo caso, sia la variabile catturata che la chiusura stessa devono essere dichiarate mutabili. La chiusura può quindi modificare la variabile catturata, ma si applicano ancora le regole di prestito: non si possono avere altri riferimenti a quella variabile finché esiste la chiusura mutabile.


Il metodo di cattura più restrittivo è la proprietà, che sposta le variabili catturate nella chiusura. Questo è necessario quando la chiusura potrebbe superare l'ambito in cui le variabili sono state originariamente definite, come nel caso della creazione di thread. Si può forzare la cattura della proprietà usando la parola chiave `move` prima dei parametri della chiusura: `move |x| { /* corpo della chiusura */ }`. Questo è essenziale per la sicurezza dei thread, poiché questi non possono prendere in prestito in modo sicuro da altri thread che potrebbero terminare e far cadere le loro variabili.


### Tratti di chiusura e tipi di funzione


Rust rappresenta le chiusure attraverso un sistema di tratti con tre tratti chiave: `FnOnce`, `FnMut` e `Fn`. Questi tratti formano una gerarchia che descrive come le chiusure possono essere chiamate e cosa possono fare con le variabili catturate.


`FnOnce` è il tratto di base che tutte le chiusure implementano. Rappresenta le chiusure che possono essere chiamate almeno una volta. Alcune chiusure, in particolare quelle che spostano i valori catturati o li consumano in qualche modo, possono essere chiamate solo una volta, perché distruggono o spostano i dati catturati durante l'esecuzione.


`FnMut` rappresenta chiusure che possono essere chiamate più volte e possono mutare l'ambiente catturato. Queste chiusure catturano le variabili con un riferimento mutabile e possono modificarle nel corso di più chiamate. Le regole di prestito assicurano che quando una chiusura `FnMut` è attiva, ha accesso esclusivo e mutabile alle sue variabili catturate.


`Fn` è il tratto più restrittivo, che rappresenta chiusure che possono essere chiamate più volte senza mutare l'ambiente catturato. Queste chiusure catturano solo tramite riferimenti immutabili e possono essere chiamate simultaneamente senza violare le garanzie di sicurezza di Rust. Se una chiusura implementa `Fn`, implementa automaticamente anche `FnMut` e `FnOnce`, poiché essere richiamabile più volte senza mutazione implica essere richiamabile con mutazione ed essere richiamabile una volta.


### Lavorare con gli iteratori


Gli iteratori in Rust forniscono un modo per elaborare sequenze di dati. Sono pigri, cioè non eseguono alcun lavoro fino a quando non vengono consumati chiamando metodi che effettivamente iterano i dati. Questa valutazione pigra consente di concatenare in modo efficiente le operazioni senza creare collezioni intermedie.


Il tratto `Iterator` definisce la funzionalità di base con un tipo associato `Item` che rappresenta ciò che l'iteratore produce e un metodo `next` che restituisce `Option<Self::Item>`. Quando `next` restituisce `None`, l'iteratore è esaurito. Questa struttura consente agli iteratori di rappresentare in modo sicuro sia sequenze finite che potenzialmente infinite.


È possibile creare iteratori da collezioni utilizzando metodi come `iter()` per prendere in prestito l'iterazione, `iter_mut()` per prendere in prestito l'iterazione mutabile e `into_iter()` per consumare l'iterazione. La scelta tra questi metodi dipende dalla necessità di modificare gli elementi e dal fatto che si voglia consumare l'insieme originale.


### Adattatori e consumatori di iteratori


Gli adattatori di iteratori sono metodi che trasformano un iteratore in un altro, consentendo di concatenare le operazioni. Gli adattatori più comuni sono `map` per trasformare ogni elemento, `filter` per selezionare gli elementi in base a un predicato e `enumerate` per aggiungere indici. Questi adattatori sono pigri: non fanno alcun lavoro finché non vengono consumati.


Il metodo `map` applica una chiusura a ogni elemento, trasformandolo in qualcos'altro. Per esempio, `numeri.iter().map(|x| x * 2)` crea un iteratore che raddoppia ogni numero. Il metodo `filtro` mantiene solo gli elementi per i quali la chiusura del predicato risulta vera: `numeri.iter().filtro(|&x| x > 10)` mantiene solo i numeri maggiori di dieci.


I metodi di consumo iterano effettivamente i dati e producono un risultato finale. Il metodo `collect` consuma un iteratore e crea un insieme da esso. Spesso è necessario specificare il tipo di collezione: `let vec: Vec<_> = iteratore.collect()`. Altri consumatori sono `sum` per sommare elementi numerici, `fold` per accumulare valori con un'operazione personalizzata e `for_each` per eseguire effetti collaterali su ogni elemento.


### Modelli avanzati di iteratore


Altre operazioni sugli iteratori sono `zip` per combinare due iteratori in modo elementare, `chain` per concatenare gli iteratori e `filter_map` per combinare filtraggio e mappatura in un'unica operazione. Il metodo `zip` crea coppie di elementi corrispondenti di due iteratori: `a.iter().zip(b.iter())` produce le tuple `(a[0], b[0]), (a[1], b[1]), ...`.


Il metodo `fold` è utile per accumulare valori. Prende un valore iniziale e una chiusura che combina l'accumulatore con ogni elemento: `numeri.iter().fold(0, |acc, x| acc + x)` somma tutti i numeri. Questo schema può implementare molte altre operazioni, come la ricerca di valori massimi, la costruzione di stringhe o la creazione di strutture di dati complesse.


Le catene di iteratori possono esprimere in modo conciso trasformazioni complesse di dati. Ad esempio, l'elaborazione di dati audio potrebbe comportare: `coefficienti.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Questo moltiplica i coefficienti corrispondenti e i valori del buffer, somma i risultati e sposta il valore finale, il tutto in un'unica espressione leggibile.


```rust
fn main() {
// Sample UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Using closures and iterators to process UTXOs

// 1. Filter UTXOs above dust threshold (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calculate total balance with fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Find UTXOs needed to cover a 120,000 sat payment
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Skip dust
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transform to display format using map and collect
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```


### Introduzione ai puntatori intelligenti


I puntatori intelligenti sono strutture di dati che si comportano come i puntatori tradizionali, ma forniscono funzionalità aggiuntive e una gestione automatica della memoria. A differenza dei semplici riferimenti, i puntatori intelligenti sono proprietari dei dati a cui puntano e possono implementare comportamenti personalizzati per l'allocazione, la deallocazione e i modelli di accesso alla memoria. Sono strumenti essenziali per la gestione dei dati allocati nell'heap e per l'implementazione di schemi di proprietà complessi che vanno oltre il sistema di proprietà di base di Rust.


L'aspetto "intelligente" deriva dalla loro capacità di gestire automaticamente attività di gestione della memoria che altrimenti richiederebbero un intervento manuale. Quando un puntatore intelligente esce dall'ambito, può liberare automaticamente la memoria associata, decrementare il conteggio dei riferimenti o eseguire altre operazioni di pulizia. Questa automazione aiuta a prevenire le perdite di memoria e gli errori di use-after-free, offrendo al contempo una maggiore flessibilità rispetto all'allocazione solo in stack.


I puntatori intelligenti di solito implementano due caratteristiche chiave: `Deref` e `Drop`. Il tratto `Deref` consente di utilizzare lo smart pointer come se fosse un riferimento ai dati contenuti. Il tratto `Drop` consente una logica di pulizia personalizzata quando lo smart pointer viene distrutto. Insieme, questi tratti consentono agli smart pointer di gestire automaticamente la memoria.


### Il puntatore intelligente Box


`Box<T>` è il puntatore intelligente più semplice, che fornisce l'allocazione sull'heap per qualsiasi tipo `T`. Quando si crea una `Box`, il valore contenuto viene memorizzato sull'heap anziché sullo stack, mentre la `Box` stessa (che è solo un puntatore) viene memorizzata sullo stack. Questa indirezione è utile quando è necessario memorizzare grandi quantità di dati senza spostarli, quando si ha bisogno di un tipo con dimensioni sconosciute al momento della compilazione o quando si vuole trasferire in modo efficiente la proprietà dei dati dell'heap.


Creare una `Box` è semplice: `let boxed_value = Box::new(42);` alloca un intero sull'heap. La `Box` gestisce automaticamente questa memoria: quando la `Box` esce dallo scope, dealloca automaticamente la memoria dell'heap. Questa pulizia automatica previene le perdite di memoria senza richiedere una gestione manuale della memoria.


Uno dei casi d'uso più importanti di `Box` è l'abilitazione di strutture dati ricorsive. Si consideri un elenco collegato in cui ogni nodo contiene un valore e un puntatore al nodo successivo. Senza `Box`, non è possibile definire una struttura di questo tipo, perché il compilatore non può determinare la dimensione di un tipo che contiene se stesso. Utilizzando `Box<Node>` per il puntatore successivo, si elimina il problema del dimensionamento ricorsivo, perché `Box` ha una dimensione nota e fissa, indipendentemente da ciò che contiene.


### Implementazione del tratto Deref


Il tratto `Deref` permette di dereferenziare un tipo usando l'operatore `*`, facendo sì che gli smart pointer si comportino come riferimenti ai dati in essi contenuti. Quando si implementa `Deref` per uno smart pointer, si abilita la dereferenziazione automatica che rende lo smart pointer trasparente all'uso. Ciò significa che si possono chiamare metodi sul tipo contenuto direttamente attraverso lo smart pointer, senza dereferenziare esplicitamente.


Il tratto `Deref` definisce un tipo associato `Target` che specifica il tipo di riferimento che l'operazione di dereferenziazione deve produrre. Il tratto richiede l'implementazione di un metodo `deref` che restituisca un riferimento al tipo target. Per `Box<T>`, l'implementazione restituisce un riferimento al valore `T` contenuto.


Rust esegue la coercizione automatica di deref, il che significa che il compilatore può inserire automaticamente le chiamate a `deref` quando necessario per rendere i tipi compatibili. Questo è il motivo per cui si può passare una `Stringa` a una funzione che si aspetta una `&str`: il compilatore fa automaticamente una dereferenziazione della `Stringa` per ottenere una fetta di stringa. Questa coercizione può concatenare più livelli, quindi una `Box<String>` può essere automaticamente convertita in una `&str` attraverso più operazioni di deref.


### Implementazione della goccia personalizzata


Il tratto `Drop` consente di specificare il codice di pulizia personalizzato che viene eseguito quando un valore esce dall'ambito. Questo è particolarmente importante per i puntatori intelligenti che gestiscono risorse al di là della semplice memoria, come handle di file, connessioni di rete o conteggi di riferimenti. Il tratto `Drop` ha un singolo metodo, `drop`, che prende un riferimento mutabile a `self` ed esegue la pulizia.


La maggior parte dei tipi non ha bisogno di implementazioni personalizzate di `Drop`, perché Rust gestisce automaticamente l'eliminazione dei loro campi. Tuttavia, i puntatori intelligenti hanno spesso bisogno di una logica personalizzata per ripulire correttamente le risorse che gestiscono. Ad esempio, uno smart pointer conteggio dei riferimenti deve decrementare il conteggio dei riferimenti e potenzialmente deallocare i dati condivisi quando l'ultimo riferimento viene abbandonato.


È anche possibile abbandonare esplicitamente un valore prima che esca dall'ambito, usando `std::mem::drop()`. Questa funzione assume la proprietà di un valore e lo rilascia immediatamente, il che può essere utile per liberare risorse in anticipo o per garantire che la pulizia avvenga in un punto specifico del programma. La funzione esplicita di drop è solo una funzione di identità che si appropria di un valore; il vero lavoro avviene quando il valore viene abbandonato alla fine della funzione.


Questa base di chiusure, iteratori e puntatori intelligenti fornisce agli sviluppatori di Rust gli strumenti per scrivere codice espressivo, sicuro ed efficiente. Queste caratteristiche lavorano insieme per consentire modelli di programmazione comuni, pur mantenendo le garanzie fondamentali di sicurezza della memoria e delle prestazioni di Rust.



## Conteggio dei riferimenti e mutabilità interna

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Conteggio dei riferimenti con RC


Il conteggio dei riferimenti rappresenta un altro tipo fondamentale di puntatore intelligente in Rust, progettato specificamente per consentire scenari di proprietà multipla. A differenza di Box, che segue le tradizionali regole di proprietà singola in cui un'entità possiede i dati, RC (Reference Counter) consente a più parti del codice di condividere la proprietà degli stessi dati contemporaneamente. Questo modello di proprietà condivisa funziona attraverso un meccanismo di conteggio che tiene traccia di quanti riferimenti esistono a un particolare pezzo di dati.


Il sistema di conteggio dei riferimenti funziona mantenendo un contatore interno che si incrementa ogni volta che si clona un RC e si decrementa quando un RC viene abbandonato. La memoria viene liberata solo quando questo contatore raggiunge lo zero, garantendo che i dati rimangano validi finché esiste un riferimento. Questo approccio previene la deallocazione prematura, consentendo al contempo modelli flessibili di condivisione dei dati che sarebbero impossibili con la semplice proprietà della casella.


Un esempio pratico in cui RC è utile riguarda la creazione di strutture di dati condivise, come gli elenchi collegati, in cui più elenchi possono fare riferimento alla stessa porzione di coda. Si consideri il tentativo di creare due elenchi separati che fanno entrambi riferimento a una sottosequenza comune. Con la proprietà Box, questo diventa impossibile perché lo spostamento della porzione condivisa nel primo elenco trasferisce la proprietà, impedendone l'uso nel secondo elenco. RC risolve questo problema consentendo di clonare il riferimento piuttosto che i dati sottostanti, rendendo possibile la struttura condivisa e mantenendo la sicurezza della memoria.


Quando si clona un RC, non si duplicano i dati interni, indipendentemente dalla loro dimensione o complessità. Al contrario, si crea un altro riferimento alla stessa posizione di memoria e si incrementa il contatore di riferimento. Questo rende efficiente la clonazione di istanze di RC anche per strutture di dati di grandi dimensioni, poiché viene copiato solo il riferimento stesso, mentre i dati sottostanti rimangono al loro posto.


### Mutabilità interna con RefCell


RefCell introduce la mutabilità interna, che consente di mutare i dati anche quando si dispone solo di un riferimento immutabile ad essi. Questa funzionalità cambia radicalmente il modo in cui vengono applicate le regole di prestito di Rust, spostando i controlli dal tempo di compilazione al tempo di esecuzione. Mentre i riferimenti normali si affidano al compilatore per verificare la sicurezza del prestito, RefCell esegue questi controlli durante l'esecuzione del programma, offrendo una maggiore flessibilità al costo di potenziali panici in fase di esecuzione.


Il principio fondamentale di RefCell consiste nel mantenere le stesse regole di prestito che Rust applica normalmente in fase di compilazione, ma verificandole dinamicamente. In qualsiasi momento, è possibile avere un riferimento mutabile o un numero qualsiasi di riferimenti immutabili ai dati all'interno di una RefCell. Se il codice tenta di violare queste regole creando contemporaneamente riferimenti in conflitto, il programma va in panico anziché produrre un comportamento non definito.


Questo controllo a tempo di esecuzione consente di creare alcuni modelli di programmazione che il compilatore potrebbe rifiutare anche quando sono effettivamente sicuri. L'analisi statica del compilatore non è sempre in grado di dimostrare la correttezza di schemi di prestito complessi, il che lo porta a scegliere la strada della cautela. RefCell consente di ignorare queste restrizioni conservative quando si è sicuri della correttezza del codice, ma questa fiducia comporta la responsabilità di garantire un uso corretto per evitare crash di runtime.


Un caso d'uso comune di RefCell riguarda gli oggetti mock negli scenari di test. Quando si implementa un tratto che fornisce solo l'accesso immutabile al sé, ma l'implementazione del mock ha bisogno di tracciare i cambiamenti di stato internamente, RefCell consente questo schema. È possibile avvolgere lo stato interno in una RefCell, consentendo al mock di mutare i suoi dati di tracciamento anche attraverso un'interfaccia immutabile.


### Combinazione di RC e RefCell per uno stato mutabile condiviso


La combinazione di RC e RefCell crea un modello di stato mutabile condiviso, in cui più proprietari possono modificare gli stessi dati. RC fornisce la capacità di proprietà condivisa, mentre RefCell consente la mutazione attraverso riferimenti immutabili. Questa combinazione è utile in scenari come le strutture a grafo, le cache o qualsiasi situazione in cui più parti del programma hanno bisogno di accedere sia in lettura che in scrittura a dati condivisi.


Quando si avvolge una RefCell all'interno di un RC, si crea una struttura che può essere clonata e distribuita in tutto il programma, con ogni clone che fornisce accesso agli stessi dati mutabili sottostanti. Tutti i proprietari possono potenzialmente modificare i dati usando il metodo borrow_mut di RefCell, ma devono comunque rispettare le regole di prestito in fase di esecuzione. Questo modello consente di realizzare scenari complessi di condivisione dei dati, mantenendo le garanzie di sicurezza di Rust attraverso i controlli di runtime.


Tuttavia, questa flessibilità è accompagnata da importanti avvertenze riguardanti le perdite di memoria e i cicli di riferimento. Quando si usa RC con RefCell, è possibile creare accidentalmente riferimenti circolari in cui le strutture di dati fanno riferimento a se stesse, direttamente o attraverso una catena di riferimenti. Questi cicli impediscono che il conteggio dei riferimenti raggiunga mai lo zero, causando perdite di memoria perché i dati sembrano avere sempre riferimenti attivi anche quando non sono più accessibili dal resto del programma.


La soluzione ai cicli di riferimento prevede l'uso di riferimenti deboli, che non contribuiscono al conteggio dei riferimenti utilizzato per le decisioni sulla gestione della memoria. I riferimenti deboli consentono di mantenere le connessioni tra le strutture di dati senza mantenerle in vita, interrompendo i potenziali cicli e preservando la possibilità di accedere ai dati correlati quando sono ancora presenti.


```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simulating a channel state that multiple components need to access and modify
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> allows multiple owners with interior mutability
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clone Rc to share ownership (cheap - only increments counter)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// Reference count is now 3
println!("Reference count: {}", Rc::strong_count(&channel));

// UI component reads the state (immutable borrow)
{
let state = channel_for_ui.borrow();
println!("UI shows balance: {} msats", state.local_balance_msat);
} // borrow ends here

// Router updates the state after a payment (mutable borrow)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // Sent 100k sats
state.remote_balance_msat += 100_000_000;
println!("Router updated balances");
} // mutable borrow ends here

// Original reference can still read the updated state
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// WARNING: This would panic at runtime!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PANIC: already borrowed
}
```


### Sicurezza dei thread e fondamenti di concorrenza


L'approccio di Rust alla concorrenza è incentrato sulla prevenzione dei data race e dei problemi di sicurezza della memoria in fase di compilazione. Il sistema di tipi applica la sicurezza dei thread attraverso tratti come `Send` e `Sync`, che contrassegnano i tipi come sicuri per il trasferimento tra thread o sicuri per l'accesso concorrente. Questa verifica in fase di compilazione permette di individuare molti bug di concorrenza che in altri linguaggi di programmazione di sistema apparirebbero solo in fase di esecuzione.


La creazione di thread in Rust segue uno schema semplice utilizzando thread::spawn, che accetta una chiusura da eseguire nel nuovo thread e restituisce un handle per gestire il ciclo di vita del thread. Il thread generato viene eseguito in concomitanza con il thread principale e si può usare il metodo join sull'handle per attendere il completamento. Senza un'unione esplicita, i thread generati possono essere terminati quando il thread principale esce, interrompendo potenzialmente il lavoro incompleto.


La parola chiave move diventa cruciale quando si lavora con i thread, perché le chiusure passate ai thread generati hanno spesso bisogno di possedere i loro dati piuttosto che prenderli in prestito. Poiché i thread generati possono sopravvivere all'ambito che li ha creati, il prestito dall'ambito padre crea potenziali violazioni della durata. Lo spostamento dei dati nella chiusura del thread trasferisce la proprietà, assicurando che i dati rimangano validi per l'intera durata del thread e impedendo l'accesso dall'ambito originale.


Il passaggio di messaggi fornisce un'alternativa alla concorrenza a stati condivisi attraverso canali che consentono ai thread di comunicare inviando dati piuttosto che condividendo la memoria. La libreria standard di Rust fornisce canali Multiple Producer Single Consumer (MPSC), in cui più thread possono inviare messaggi a un singolo thread ricevente. Questo modello elimina molti problemi di sincronizzazione, evitando di condividere completamente lo stato mutabile e affidandosi invece allo scambio di messaggi per la coordinazione.


### Concorrenza dello stato condiviso con Mutex e Arc


Quando il passaggio di messaggi non è adatto, Rust offre la tradizionale concorrenza a stati condivisi tramite Mutex (mutua esclusione) combinato con Arc (Atomic Reference Counter). Mutex assicura che solo un thread possa accedere ai dati protetti alla volta, richiedendo ai thread di acquisire un blocco prima di accedere ai dati. Il blocco viene rilasciato automaticamente quando l'oggetto di guardia restituito dall'operazione di blocco esce dall'ambito, evitando i comuni scenari di deadlock causati da sblocchi dimenticati.


Arc è l'equivalente thread-safe di RC, che utilizza operazioni atomiche per gestire il conteggio dei riferimenti in modo sicuro su più thread. Mentre RC funziona perfettamente per scenari a thread singolo, il suo conteggio dei riferimenti non atomico crea condizioni di gara quando si accede da più thread. I contatori atomici di Arc garantiscono che le modifiche al conteggio dei riferimenti avvengano in modo sicuro anche in caso di accesso concorrente, rendendolo adatto alla condivisione dei dati attraverso i confini dei thread.


La combinazione di Arc e Mutex crea un modello per lo stato mutabile condiviso nei programmi concorrenti. Avvolgendo un Mutex in un Arc, è possibile clonare l'Arc per distribuire l'accesso allo stesso mutex tra più thread, con ogni thread in grado di acquisire il blocco e modificare i dati protetti in modo sicuro. Questo modello offre la flessibilità dello stato condiviso, mantenendo le garanzie di sicurezza di Rust attraverso la verifica a tempo di compilazione e il blocco a tempo di esecuzione.


I tratti Send e Sync lavorano dietro le quinte per garantire la sicurezza dei thread in fase di compilazione. Send indica che un tipo può essere trasferito in modo sicuro a un altro thread, mentre Sync indica che i riferimenti a un tipo possono essere condivisi in modo sicuro tra i thread. La maggior parte dei tipi implementa automaticamente questi tratti quando i loro componenti sono thread-safe, ma alcuni tipi, come RC e RefCell, non li implementano esplicitamente perché non sono progettati per l'accesso concorrente. L'implementazione automatica di questi tratti previene l'introduzione accidentale di violazioni della sicurezza dei thread, consentendo al contempo ai tipi sicuri di lavorare senza problemi in contesti concorrenti.


## Comprendere le macro Rust

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Introduzione alle macro in Rust


Le macro in Rust sono una funzione di metaprogrammazione che consente agli sviluppatori di scrivere codice che genera altro codice in fase di compilazione. A differenza delle funzioni, che vengono richiamate in fase di esecuzione, le macro vengono espanse all'inizio del processo di compilazione, prima del controllo dei tipi e delle fasi successive. Questa distinzione fondamentale rende le macro particolarmente utili per ridurre la ripetizione del codice e creare linguaggi specifici per il dominio all'interno dei programmi Rust.


L'indicatore più riconoscibile di una chiamata macro è il punto esclamativo (!) che segue il nome della macro. Per esempio, quando si usa `println!("Hello, world!")`, non si sta chiamando una funzione ma una macro. Questa macro si espande in un codice più complesso che gestisce le operazioni di formattazione e di output. Il punto esclamativo serve a indicare agli sviluppatori che si sta generando codice a tempo di compilazione piuttosto che una chiamata di funzione standard.


Rust fornisce tre tipi distinti di macro, ognuno dei quali serve a scopi diversi nell'ecosistema del linguaggio:



- Macro simili a funzioni**: Assomigliano a chiamate di funzione ma operano in tempo di compilazione (ad esempio, `vec!`, `println!`)
- Macro derivate**: Implementa automaticamente i tratti per i tipi (ad esempio, `#[derive(Debug, Clone)]`)
- Macro simili ad attributi**: Modificano il comportamento degli elementi di codice a cui sono applicate (ad esempio, `#[test]`, `#[tokio::main]`)


La comprensione di questi diversi tipi di macro è essenziale per un'efficace programmazione Rust, in quanto ciascuno di essi si rivolge a casi d'uso e modelli di programmazione specifici.


### Tipi di macro e loro applicazioni


Le macro simili a funzioni rappresentano il tipo di macro più comunemente incontrato nella programmazione Rust. Queste macro utilizzano una sintassi simile a quella delle chiamate di funzione, ma eseguono una corrispondenza di pattern sull'input per ottenere il codice appropriato per generate. La macro `vec!` è un esempio comune di questa categoria, che consente agli sviluppatori di creare e inizializzare vettori con una sintassi concisa. Quando si scrive `vec![1, 2, 3, 4]`, la macro lo espande in codice che crea un nuovo vettore, spinge ogni elemento individualmente e restituisce il vettore completato.


Le macro di derivazione forniscono implementazioni automatiche dei tratti per i tipi personalizzati, riducendo in modo significativo il codice boilerplate. Quando si aggiunge `#[derive(Debug)]` a una definizione di struct o enum, si istruisce il compilatore a creare un'implementazione completa del tratto Debug per quel tipo. Questa implementazione generata gestisce la logica di formattazione necessaria per visualizzare il contenuto del tipo in un formato leggibile dall'uomo. Il meccanismo di derivazione supporta numerosi tratti di libreria standard, tra cui Clone e PartialEq, rendendolo uno strumento comunemente usato per ridurre il boilerplate.


Le macro di tipo attributo modificano il comportamento degli elementi di codice che annotano, fornendo un modo per aggiungere metadati o alterare il comportamento di compilazione. Queste macro appaiono come attributi posti sopra definizioni di tipi, funzioni o altri costrutti di codice. Ad esempio, l'attributo `#[non_exhaustive]` su un enum indica che nelle versioni future potrebbero essere aggiunte ulteriori varianti, richiedendo alle espressioni di corrispondenza di includere un caso predefinito. Questo meccanismo assicura la compatibilità con il futuro, fornendo al contempo una chiara documentazione del potenziale evolutivo del tipo.


### Creazione di macro simili a funzioni personalizzate


La scrittura di macro simili a funzioni personalizzate richiede la comprensione della sintassi di corrispondenza dei modelli di Rust per le definizioni di macro. La definizione di macro utilizza un approccio dichiarativo in cui si specificano i pattern che corrispondono a diversi moduli di input e ai corrispondenti modelli di generazione del codice. Ogni macro può contenere più rami, in modo da poter gestire vari modelli di input e generate il codice appropriato per ogni caso.


Si consideri la creazione di una macro vettoriale personalizzata che dimostri i principi fondamentali della costruzione delle macro. La definizione della macro inizia con `macro_regole!` seguita dal nome della macro e da una serie di rami di corrispondenza dei modelli. Ogni ramo consiste in un modello che corrisponde a una specifica sintassi di input e in un modello di codice che genera il codice Rust corrispondente. Per esempio, un ramo semplice potrebbe corrispondere alle parentesi vuote `[]` e al codice generate per creare un vettore vuoto, mentre un altro ramo corrisponde a una singola espressione e genera codice per creare un vettore con un elemento.


Le macro diventano particolarmente utili quando si implementano modelli di argomenti variabili utilizzando la sintassi della ripetizione. Lo schema `$($x:expr),*` corrisponde a zero o più espressioni separate da virgole, consentendo alla macro di gestire un numero arbitrario di argomenti. Il corrispondente modello di generazione del codice usa `$(vec.push($x);)*` per iterare su tutte le espressioni abbinate e generate dichiarazioni push individuali per ciascuna di esse. Questo meccanismo di ripetizione consente alle macro di generate scrivere codice che sarebbe impossibile o estremamente prolisso scrivere manualmente.


```rust
// A macro to create a HashMap with Bitcoin-related data
macro_rules! btc_map {
// Empty case
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// A macro for logging with context (simulating a derive-like pattern)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Using the btc_map! macro
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Fee rates: {:?}", fee_rates);

// Using the log_payment! macro
log_payment!(info, "Sending {} sats to {}", 100_000, "bc1q...");
log_payment!(warn, "Fee rate {} sats/vB is above average", 75);
log_payment!(error, "Payment failed: insufficient funds");

// Standard vec! macro usage comparison
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```


Il processo di compilazione trasforma le chiamate macro in codice espanso prima che avvengano il controllo dei tipi e l'ottimizzazione. Quando il compilatore incontra un'invocazione macro, confronta l'input con gli schemi definiti e sostituisce la chiamata macro con il codice generato. Il codice espanso viene quindi sottoposto ai normali processi di compilazione, compresi il controllo dei tipi e l'ottimizzazione. Strumenti come `cargo expand` consentono agli sviluppatori di ispezionare il codice generato, fornendo preziose funzionalità di debug durante lo sviluppo di macro complesse.


### Concetti avanzati di macro e debug


Lo sviluppo di macro richiede la comprensione della distinzione tra esecuzione a tempo di compilazione e a tempo di esecuzione. Le macro vengono eseguite in fase di compilazione, generando codice che verrà eseguito in fase di esecuzione. Questa separazione temporale significa che la logica delle macro non può dipendere dai valori di runtime, ma consente anche di ottimizzare i calcoli complessi che possono essere eseguiti una sola volta durante la compilazione anziché ripetutamente durante l'esecuzione.


Il sistema di corrispondenza dei pattern nelle macro supporta vari specificatori di frammenti che definiscono il tipo di elementi di codice che possono essere abbinati. Lo specificatore `expr` corrisponde alle espressioni, `ty` corrisponde ai tipi, `ident` corrisponde agli identificatori e molti altri forniscono un controllo a grana fine sulla validazione dell'input. Questi specificatori assicurano che le macro ricevano input sintatticamente validi e forniscono chiari messaggi di errore quando viene incontrata una sintassi non valida.


Il debug delle macro presenta sfide uniche a causa della loro natura a tempo di compilazione. Il comando `cargo expand` è utile per lo sviluppo delle macro, in quanto visualizza il codice completamente espanso generato dalle invocazioni delle macro. Questo strumento consente agli sviluppatori di verificare che le loro macro generate il codice previsto e di identificare i problemi nella logica di espansione. Quando il codice generato dalle macro contiene errori, l'output espanso aiuta a capire se il problema risiede nella definizione della macro o nella struttura del codice generato.


Le macro complesse possono implementare schemi ricorsivi, in cui una macro richiama se stessa con argomenti modificati per gestire la generazione di codice nidificato o iterativo. Tuttavia, le macro ricorsive richiedono un'attenta progettazione per evitare l'espansione infinita e problemi di prestazioni di compilazione. La natura compile-time dell'espansione delle macro significa che anche le implementazioni inefficienti delle macro influiscono solo sulla velocità di compilazione e non sulle prestazioni di runtime, ma macro troppo complesse possono rallentare significativamente il processo di compilazione.



# Rust E Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Perché Rust per lo sviluppo di Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


La scelta del Rust per lo sviluppo di Bitcoin e del Lightning non è casuale. Lo sviluppo di Bitcoin comporta responsabilità uniche che lo distinguono dal tipico sviluppo software. Quando lavorano con Bitcoin, gli sviluppatori si trovano spesso a gestire i fondi degli utenti in un ambiente in cui gli errori possono essere irreversibili. A differenza dei sistemi finanziari tradizionali con protezioni normative e meccanismi di chargeback, la natura decentralizzata di Bitcoin significa che una volta trasmessa una transazione, non c'è un'autorità a cui appellarsi per recuperare i fondi. Questa realtà richiede un livello superiore di responsabilità e precisione nello sviluppo del software.


La filosofia del "muoviti velocemente e rompi le cose" che funziona in molti settori tecnologici semplicemente non si applica allo sviluppo di Bitcoin. L'ecosistema richiede invece linguaggi e strumenti che aiutino gli sviluppatori a creare software robusto e sicuro, in cui i guasti siano evitati o gestiti con grazia. Questo è il motivo per cui molti progetti Bitcoin di spicco si sono orientati verso Rust, tra cui Bitcoin Development Kit (BDK), il Lightning Development Kit (LDK) e il BreezSDK.


Rust offre tre proprietà essenziali che lo rendono particolarmente adatto allo sviluppo di Bitcoin: un sistema statico di tipi forti, una ricca strumentazione moderna e la compatibilità multipiattaforma. Ognuna di queste caratteristiche contribuisce alla capacità del linguaggio di aiutare gli sviluppatori a scrivere codice più sicuro e affidabile per gestire le operazioni con le criptovalute.


### Sistema di tipo statico forte del Rust


Il sistema di tipi di Rust offre caratteristiche di tipizzazione sia statiche che forti, che lavorano insieme per catturare gli errori prima che possano influenzare gli utenti. La natura statica significa che il controllo dei tipi avviene in fase di compilazione, richiedendo agli sviluppatori di risolvere i disallineamenti tra i tipi prima ancora che il programma possa essere costruito. Ciò contrasta con i linguaggi tipizzati dinamicamente, dove gli errori di tipo emergono solo in fase di esecuzione, potenzialmente dopo che il software è stato distribuito e sta gestendo fondi reali degli utenti.


La forza del sistema di tipi di Rust si riferisce alla sua espressività e al suo rigore nella modellazione dei problemi. A differenza dei linguaggi con sistemi di tipi più deboli, come il C, in cui gli sviluppatori sono limitati a tipi di base come numeri e strutture, Rust consente una modellazione ricca di tipi, in grado di rappresentare con precisione concetti di dominio complessi. Ad esempio, è possibile creare tipi che distinguono tra diversi tipi di elenchi o imporre che determinate operazioni siano eseguite solo su tipi di oggetti specifici.


Ciò che rende il sistema di tipi di Rust rilevante per lo sviluppo di Bitcoin è il suo approccio alla sicurezza della memoria. Lo stesso sistema di tipi che modella la logica aziendale gestisce anche la proprietà della memoria e il controllo degli accessi condivisi. Questa doppia responsabilità significa che le classi comuni di vulnerabilità, come le perdite di memoria, gli errori double-free e le condizioni di gara, vengono eliminate completamente dal compilatore. Il sistema di tipi applica queste garanzie di sicurezza attraverso concetti come proprietà, prestito e conteggio dei riferimenti, rendendo estremamente difficile l'introduzione di bug legati alla memoria che potrebbero compromettere la sicurezza o la stabilità.


```rust
// Example: Type-safe Bitcoin amount handling
// Using newtypes to prevent mixing up satoshis and other values

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats per vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calculate fee given tx size - type system ensures we can't mix up values
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// This would NOT compile - type safety prevents mixing values:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: expected FeeRate, found Satoshis
}
```


### Tooling moderno e supporto multipiattaforma


L'ecosistema di strumenti di Rust fornisce agli sviluppatori strumenti che aiutano la produttività e la qualità del codice. Lo stesso compilatore Rust è stato progettato non solo per tradurre il codice in forma binaria, ma anche come strumento educativo che aiuta gli sviluppatori a imparare e migliorare. Quando si verificano errori di compilazione, il compilatore fornisce spiegazioni dettagliate su cosa è andato storto e spesso suggerisce soluzioni specifiche. Questo approccio è particolarmente prezioso per gli sviluppatori alle prime armi con Rust, in quanto il compilatore insegna efficacemente le buone pratiche e aiuta a prevenire gli errori più comuni.


Il linguaggio include Cargo, un gestore di pacchetti unificato che gestisce la gestione delle dipendenze, la costruzione, i test e la generazione della documentazione. Questa standardizzazione elimina la frammentazione che si riscontra nei vecchi linguaggi come il C++, dove più strumenti concorrenti creano incoerenza tra i progetti. Cargo supporta anche estensioni come rustfmt per la formattazione del codice e Clippy per l'analisi statica, assicurando che il codice segua linee guida di stile coerenti e catturi potenziali problemi prima che diventino tali.


Le capacità multipiattaforma di Rust si estendono oltre i sistemi operativi tradizionali per includere piattaforme mobili come Android e iOS, nonché WebAssembly per le applicazioni basate su browser. Questo supporto multipiattaforma è utile per le applicazioni Bitcoin che devono essere eseguite in ambienti diversi. Ad esempio, progetti come Mutiny Wallet sfruttano la compilazione WebAssembly di Rust per creare portafogli Lightning che vengono eseguiti direttamente nei browser web, cosa che sarebbe impraticabile con le sole tecnologie web tradizionali.


### Comprendere i tipi di errore e le loro implicazioni


Una gestione efficace degli errori inizia con la comprensione delle diverse categorie di errori che possono verificarsi durante l'esecuzione del programma. Consideriamo una semplice applicazione di routing che calcola i percorsi tra punti geografici. Questo esempio illustra tre tipi fondamentali di errori che gli sviluppatori devono affrontare: errori di input non validi, errori di risorse di runtime ed errori logici.


Gli errori di input non validi si verificano quando una funzione riceve parametri che non soddisfano i suoi requisiti. Ad esempio, se un sistema di coordinate geografiche utilizza numeri interi firmati per la longitudine, ma riceve un valore negativo quando sono validi solo i valori positivi, la funzione non può procedere in modo significativo. Questi errori rappresentano una violazione del contratto tra il chiamante e la funzione e la risposta appropriata è in genere quella di rifiutare l'input e restituire un'indicazione di errore.


Gli errori delle risorse di runtime si verificano quando le dipendenze esterne non sono disponibili o non sono accessibili. La lettura di un file di mappa può fallire perché il file non esiste, l'applicazione non ha i permessi adeguati o il dispositivo di memorizzazione non è disponibile. Questi errori sono esterni alla logica del programma e spesso richiedono correzioni ambientali piuttosto che modifiche al codice. Tuttavia, le applicazioni robuste devono prevedere e gestire questi scenari con grazia.


Gli errori logici rappresentano bug nell'implementazione del programma o incomprensioni sul modo in cui i componenti interagiscono. Se un algoritmo di routing restituisce un percorso vuoto quando vengono forniti punti di partenza e di arrivo validi, ciò indica un difetto logico che deve essere corretto nel codice stesso. A differenza degli altri tipi di errore, gli errori logici richiedono in genere il debug e la modifica del codice per essere risolti.


### Strategie per una gestione robusta degli errori


La costruzione di un software affidabile richiede strategie proattive che riducano al minimo le opportunità di errore e gestiscano con grazia gli errori inevitabili. La prima strategia consiste nel limitare i possibili errori attraverso un'attenta progettazione dei tipi. Scegliendo tipi che possono rappresentare solo valori validi, gli sviluppatori possono eliminare intere classi di errori di input non validi. Ad esempio, l'uso di numeri interi senza segno per valori che non possono essere negativi previene gli errori di valore negativo in fase di compilazione.


Le asserzioni forniscono un ulteriore livello di protezione, verificando esplicitamente che le condizioni previste siano vere durante l'esecuzione del programma. Questi controlli hanno molteplici scopi: catturano i bug durante i test, fanno sì che i programmi falliscano precocemente quando si verificano i problemi (facilitando il debug) e servono come documentazione eseguibile che descrive le ipotesi del programmatore. Quando un'asserzione fallisce, indica che è stato violato un presupposto fondamentale sullo stato del programma, indicando in genere un errore logico che deve essere indagato.


Il principio delle astrazioni a livelli aiuta a gestire la complessità, assicurando che gli errori siano gestiti ai livelli appropriati del sistema. I dettagli dell'implementazione interna, compresi i tipi di errore specifici delle librerie di livello inferiore, non devono propagarsi oltre i confini del sottosistema. Invece, ogni livello deve tradurre gli errori in termini significativi per quel livello di astrazione. Ad esempio, un'applicazione wallet che utilizza una libreria Bitcoin deve tradurre gli errori di parsing dei descrittori di basso livello in messaggi di livello superiore, come "configurazione wallet non valida", che forniscano informazioni utili agli utenti o al codice chiamante.


Questo approccio alla gestione degli errori, combinato con il sistema di tipi e gli strumenti di Rust, aiuta a individuare potenziali problemi nelle prime fasi del processo di sviluppo, prima che possano influenzare gli utenti o compromettere la sicurezza delle applicazioni di Bitcoin.



## Modello di errore

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust fornisce un approccio completo alla gestione degli errori che bilancia sicurezza e praticità. Mentre i concetti generali del modello di errore si applicano a tutti i linguaggi di programmazione, Rust offre strumenti e modelli specifici che rendono la gestione degli errori esplicita e gestibile. La comprensione di questi meccanismi è fondamentale per scrivere applicazioni Rust robuste, in grado di gestire con grazia le situazioni impreviste, mantenendo le prestazioni e la sicurezza.


### Il panico e i suoi usi appropriati


Il meccanismo di panico di Rust rappresenta il modo più diretto per gestire gli errori irrecuperabili. Quando si chiama la macro `panic!`, il programma interrompe immediatamente l'esecuzione, interrompendola o svolgendola, a seconda della configurazione. La macro panic accetta un messaggio stringa che descrive cosa è andato storto, fornendo un contesto per il debug. Inoltre, metodi come `unwrap()` e `expect()` sui tipi Result e Option servono come scorciatoie per andare in panico quando questi tipi contengono rispettivamente valori di errore o None. Il metodo `expect()` consente di fornire un messaggio personalizzato, rendendolo leggermente più informativo di `unwrap()` durante il debug dei fallimenti.


Nonostante la sua semplicità, il panico deve essere usato con giudizio nel codice di produzione. Ci sono diversi scenari in cui il panico non è solo accettabile, ma consigliato. Quando si scrivono esempi o prototipi, il panico fornisce un modo pulito per concentrarsi sulla funzionalità principale, senza ingombrare il codice con una gestione completa degli errori. Negli ambienti di test, il panico è spesso il comportamento desiderato quando le asserzioni falliscono, perché indica chiaramente che si è verificato qualcosa di inaspettato. La comunità Rust riconosce anche le situazioni in cui gli sviluppatori hanno maggiori conoscenze rispetto al compilatore, come ad esempio quando si analizzano indirizzi IP codificati in modo rigido che sono noti per essere validi.


Tuttavia, l'apparente sicurezza dei panici "verificati dal compilatore" può essere ingannevole. Si consideri uno scenario in cui si codifica un indirizzo IP e si usa `expect()` perché si sa che è valido. Nel corso del tempo, con l'evoluzione del codice, quel valore codificato in modo rigido potrebbe essere trasformato in una costante, che in seguito potrebbe essere cambiata in qualcosa come "localhost" per migliorare l'esperienza dell'utente. Improvvisamente, il panico "sicuro" diventa un errore di runtime. Questa evoluzione dimostra perché in genere è meglio evitare il panico nel codice di produzione e restituire invece tipi di errore appropriati che possono essere gestiti con grazia.


Un'eccezione notevole alla regola "evitare il panico" riguarda le operazioni con i mutex. Quando si chiama `lock()` su un mutex, viene restituito un Risultato perché il blocco può fallire se un altro thread è andato in panico mentre teneva il mutex. Questo crea una situazione di confusione in cui il codice locale riceve un errore per qualcosa che è accaduto in un contesto completamente diverso. Poiché non si può ragionevolmente gestire un errore originato dal panico di un altro thread, molti sviluppatori considerano accettabile l'unwrap dei blocchi mutex, soprattutto se si mantiene una base di codice priva di panico altrove.


### Lavorare con i tipi di risultato e di opzione


Il tipo Result costituisce la spina dorsale del sistema di gestione degli errori di Rust. Essendo un enum che può contenere un `Ok(valore)` o un `Err(errore)`, Result costringe a riconoscere esplicitamente che le operazioni possono fallire. Il tipo Option ha uno scopo simile per i casi in cui un valore potrebbe essere semplicemente assente, contenendo o `Some(value)` o `None`. Sebbene Option non fornisca informazioni dettagliate sugli errori, è perfetto per le situazioni in cui l'assenza di un valore è significativa e attesa.


Sia Result che Option forniscono diversi metodi di utilità che rendono più ergonomica la gestione degli errori. Il metodo `unwrap_or()` restituisce il valore contenuto, se presente, o un valore predefinito, se c'è un errore o None. Questo schema è particolarmente utile quando si ha un ripiego ragionevole, come l'analisi dell'input dell'utente con un valore predefinito ragionevole quando l'analisi fallisce. Il metodo `unwrap_o_default()` funziona in modo simile, ma utilizza il valore predefinito del tipo, invece di richiedere di specificarne uno. Sebbene questi metodi non gestiscano tecnicamente gli errori nel senso tradizionale del termine, forniscono un modo per degradare con grazia la funzionalità quando si verificano dei problemi.


L'operatore punto interrogativo (`?`) è una sintassi concisa per la propagazione degli errori. Quando viene applicato a un risultato o a un'opzione, estrae il valore di successo, se presente, o restituisce immediatamente l'errore dalla funzione corrente, se c'è un problema. Questo operatore elimina i verbosi schemi di controllo degli errori comuni in linguaggi come Go, dove è necessario controllare e restituire manualmente gli errori a ogni passo. L'operatore punto interrogativo fornisce essenzialmente zucchero sintattico per i ritorni anticipati, consentendo di scrivere codice pulito e lineare che si concentra sul percorso felice, gestendo automaticamente la propagazione degli errori.


### Modelli avanzati di gestione degli errori


Il metodo `map()` sui tipi Result e Option consente una gestione degli errori di tipo funzionale, che può rendere il codice più espressivo e composito. Quando si chiama `map()` su un Result, la funzione fornita viene applicata al valore di successo, se presente, mentre gli errori vengono automaticamente propagati senza modifiche. Questo schema è utile quando si concatenano le operazioni, perché ci si può concentrare sulla trasformazione dei valori senza gestire ripetutamente i casi di errore. Il metodo `map_err()` fornisce la funzionalità inversa, consentendo di trasformare i tipi di errore lasciando invariati i valori di successo.


La trasformazione degli errori diventa cruciale quando si costruiscono applicazioni stratificate in cui componenti diversi necessitano di tipi di errore diversi. Si consideri una funzione che analizza l'input dell'utente e deve convertire gli errori di parsing di basso livello in errori specifici del dominio. Usando `map_err()`, si può facilmente tradurre un errore generico "formato numero non valido" in un errore più contestuale "età non valida", che abbia senso nel dominio dell'applicazione. Questa trasformazione avviene proprio nel punto in cui si verifica l'errore, rendendo il codice più leggibile e manutenibile rispetto ai tradizionali blocchi try-catch, dove la gestione degli errori è separata dalle operazioni che possono fallire.


La combinazione dell'operatore punto interrogativo con la mappatura degli errori crea schemi concisi di gestione degli errori. È possibile concatenare le operazioni, trasformare gli errori come necessario e propagarli nello stack delle chiamate con un minimo di boilerplate. Questo approccio mantiene la gestione degli errori vicino alle operazioni che possono fallire, pur mantenendo una separazione netta tra i percorsi di successo e di errore.


```rust
use std::fmt;

// Layered error types for a wallet application
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implement Display for user-friendly messages
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convert from lower-level error to domain error
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Simulated network call
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Higher-level function using ? with automatic error conversion
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError auto-converts to WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // User-friendly message
}
}
```


### Librerie esterne ed ecosistemi di gestione degli errori


L'ecosistema Rust comprende diverse librerie popolari che estendono le capacità di gestione degli errori della libreria standard. La libreria `anyhow` fornisce un approccio semplificato alla gestione degli errori, offrendo un tipo di errore universale che può convertire automaticamente qualsiasi tipo di errore che implementi il tratto standard Error. Questa conversione automatica consente di utilizzare l'operatore punto interrogativo con diversi tipi di errore senza conversione manuale, rendendola particolarmente utile per le applicazioni in cui non è necessario distinguere programmaticamente tra diversi tipi di errore.


Mentre `anyhow` eccelle nel semplificare la gestione degli errori per le applicazioni in cui gli errori sono principalmente visualizzati agli utenti, ha dei limiti nello sviluppo delle librerie. Poiché `anyhow` converte essenzialmente tutti gli errori in messaggi di stringa, gli utenti della libreria non possono facilmente rispondere in modo programmatico alle diverse condizioni di errore. Questa limitazione rende `anyhow` più adatto alle applicazioni degli utenti finali che alle librerie che devono fornire informazioni strutturate sugli errori ai loro utenti.


Approcci più avanzati alla gestione degli errori comportano la creazione di tipi di errore personalizzati che modellano le modalità di errore specifiche dell'applicazione o della libreria. Un modello di errore ben progettato potrebbe distinguere tra input non validi (che il chiamante può correggere), errori di runtime (che possono essere ritentati) e fallimenti permanenti (che indicano bug o condizioni irrecuperabili). Questo approccio strutturato consente agli utenti del codice di prendere decisioni intelligenti su come rispondere ai diversi tipi di errore, sia che si tratti di riprovare le operazioni, di richiedere agli utenti un input diverso o di segnalare i bug agli sviluppatori.


## UniFFI, collegamento delle librerie Rust a più linguaggi


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Introduzione a UniFFI e allo sviluppo multipiattaforma


UniFFI è uno strumento per rendere accessibili le librerie Rust in diversi linguaggi di programmazione e piattaforme. Sviluppato da Mozilla, questo strumento affronta una sfida fondamentale nello sviluppo del software moderno: come sfruttare i vantaggi in termini di prestazioni e sicurezza di Rust mantenendo la compatibilità con diversi ecosistemi di sviluppo. Lo strumento genera automaticamente i binding linguistici per le librerie Rust, eliminando la necessità per gli sviluppatori di creare manualmente il codice di interfaccia per ogni linguaggio di destinazione.


Il problema principale che UniFFI risolve deriva dalla natura di Rust come linguaggio compilato. Quando il codice Rust viene compilato, produce un output binario con una Foreign Function Interface (FFI) che presenta un'interfaccia di basso livello che può essere difficile da usare direttamente da linguaggi di livello superiore come Python, Swift o Kotlin. Tradizionalmente, ogni sviluppatore di librerie dovrebbe scrivere un codice di binding personalizzato per ogni linguaggio di destinazione, creando una barriera significativa all'adozione multipiattaforma. UniFFI elimina questa ridondanza fornendo un approccio standardizzato per generare automaticamente questi binding.


La filosofia di progettazione dello strumento è incentrata sulla possibilità per gli sviluppatori di Rust di concentrarsi sulla logica aziendale principale, rendendo al contempo accessibili le loro librerie agli sviluppatori che lavorano in altri linguaggi. Uno sviluppatore iOS che utilizza Swift, ad esempio, può consumare una libreria Rust attraverso i bindings generati da UniFFI che presentano un'interfaccia Swift completamente nativa, senza alcuna indicazione che l'implementazione sottostante sia scritta in Rust. Questa perfetta integrazione consente ai team di sfruttare i vantaggi di Rust in termini di prestazioni senza richiedere a tutti i membri del team di imparare Rust.


### Comprendere l'architettura e il flusso di lavoro di UniFFI


UniFFI opera attraverso un flusso di lavoro ben definito che trasforma le librerie Rust in pacchetti compatibili con più lingue. Il processo inizia con la creazione di un file UDL (Unified Definition Language), che serve come specifica di interfaccia per descrivere quali parti della libreria Rust devono essere esposte ad altre lingue. Questo file UDL funge da contratto tra l'implementazione di Rust e i binding linguistici generati.


L'architettura segue una chiara separazione delle preoccupazioni. Gli sviluppatori mantengono la loro libreria Rust con idiomi e modelli standard Rust, quindi creano un file UDL separato che mappa l'interfaccia pubblica nel sistema di tipi di UniFFI. Il generatore di binding UniFFI elabora sia la libreria Rust che le specifiche UDL per produrre binding in lingua nativa per le piattaforme di destinazione richieste. Questi binding generati gestiscono tutte le complesse operazioni di marshalling e unmarshaling dei dati tra il runtime in lingua straniera e il codice Rust.


In fase di runtime, l'architettura crea un approccio a strati in cui il codice dell'applicazione scritto nel linguaggio di destinazione (come Kotlin per Android) interagisce con il codice di binding generato che appare completamente nativo di quel linguaggio. Questo livello di binding gestisce la traduzione tra tipi specifici delil linguaggio e tipi Rust, gestisce la memoria in modo sicuro attraverso i confini delil linguaggio e fornisce una gestione degli errori che segue le convenzioni delil linguaggio di destinazione. La logica aziendale Rust sottostante rimane invariata e non è consapevole delle interfacce linguistiche multiple costruite sopra di essa.


### Lavorare con l'UDL: definizione e mappatura dei tipi Interface


L'Unified Definition Language è la pietra miliare della funzionalità di UniFFI e fornisce un modo dichiarativo per specificare quali parti di una libreria Rust devono essere esposte e come devono essere presentate nei linguaggi di destinazione. I file UDL devono contenere almeno uno spazio dei nomi, che funge da contenitore per le funzioni che possono essere richiamate direttamente senza richiedere l'istanziazione degli oggetti. Queste funzioni dello spazio dei nomi in genere gestiscono operazioni semplici che prendono valori come parametri e restituiscono risultati.


UDL supporta un insieme completo di tipi incorporati che si adattano in modo naturale ai corrispondenti tipi Rust. I tipi di base includono primitive standard come booleani, numeri interi di varie dimensioni (u8, u32, ecc.), numeri in virgola mobile e stringhe. I tipi più complessi includono vettori, mappe hash e concetti specifici di Rust come i tipi Option (rappresentati con la sintassi del punto interrogativo) e Result per la gestione degli errori. Il sistema di tipi supporta anche le enumerazioni, sia quelle semplici basate sui valori sia quelle complesse che contengono dati associati, consentendo una modellazione dei dati che si traduce attraverso i confini linguistici.


Le strutture in Rust si traducono in dizionari in UDL, mantenendo una corrispondenza quasi uno a uno e adattandosi alle convenzioni sintattiche di UDL. Quando le strutture Rust hanno metodi associati, possono essere esposte come interfacce in UDL, che generate come classi con metodi in linguaggi di destinazione orientati agli oggetti come Kotlin o Swift. Questa mappatura preserva i modelli di progettazione orientati agli oggetti che gli sviluppatori si aspettano in questi linguaggi, pur mantenendo la struttura e il comportamento dell'implementazione Rust sottostante.


```
// Example UDL file for a Bitcoin wallet library (wallet.udl)
namespace wallet {
// Namespace functions - called directly without object
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Dictionary (struct) - becomes data class in Kotlin, struct in Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interface (class with methods) - becomes class with methods
interface Wallet {
// Constructor
constructor(string mnemonic);

// Methods
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enum with data - maps to sealed class (Kotlin) or enum with associated values (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Error enum for Result types
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Function that can fail - throws in target language
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```


L'implementazione Rust corrispondente definirebbe questi tipi e implementerebbe l'attributo `uniffi::export` nei binding generate per Kotlin, Swift, Python e altri linguaggi supportati.


### Gestione degli errori e funzioni avanzate


UniFFI fornisce una gestione degli errori che preserva il modello di errore basato sui risultati di Rust, traducendolo in modo appropriato per le lingue di destinazione. Le funzioni che restituiscono tipi di risultato in Rust possono essere contrassegnate con la parola chiave "throws" in UDL, specificando quali tipi di errore possono produrre. Questi errori devono essere definiti come enum di errore nel file UDL e devono implementare il tratto Error standard di Rust nel codice Rust sottostante. Il crate thiserror fornisce una comoda macro per implementare questo tratto, riducendo in modo significativo il codice boilerplate.


La traduzione della gestione degli errori dimostra l'approccio di UniFFI consapevole del linguaggio. In Kotlin, le funzioni contrassegnate come lancianti nell'UDL generate sono metodi che lanciano eccezioni secondo le convenzioni Java/Kotlin. I binding Python utilizzano in modo analogo il modello di eccezioni di Python. Questa traduzione garantisce che la gestione degli errori sia naturale e idiomatica in ogni lingua di destinazione, preservando al contempo il significato semantico dei tipi di errore Rust originali.


Le interfacce di callback rappresentano un'altra caratteristica avanzata che consente la comunicazione bidirezionale tra le librerie Rust e le applicazioni che le utilizzano. Quando una libreria Rust ha bisogno di richiamare il codice dell'applicazione, gli sviluppatori possono definire dei tratti in Rust e contrassegnarli come interfacce di callback in UDL. L'applicazione utilizzatrice implementa queste interfacce nel proprio linguaggio nativo e UniFFI gestisce il complesso marshalling necessario per invocare questi callback dal codice Rust. Questo schema richiede un'attenta considerazione della sicurezza dei thread, poiché le callback possono attraversare i confini dei thread, rendendo necessari i limiti di Send e Sync sul lato Rust.


### Applicazioni nel mondo reale e limitazioni attuali


UniFFI è stato adottato dalla comunità di sviluppo di criptovalute e blockchain, con progetti importanti come BDK (Bitcoin Development Kit), LDK (Lightning Development Kit) e varie implementazioni di wallet che lo utilizzano per fornire SDK mobili. Questi progetti dimostrano l'utilizzo di UniFFI in ambienti di produzione.


L'esame dei file UDL reali di questi progetti rivela i modelli e le migliori pratiche emerse dall'uso pratico. Il file UDL di BDK, ad esempio, mostra come modelli di dominio complessi con più enum, struct e interfacce possano essere mappati efficacemente per creare SDK mobili completi. La coerenza della sintassi UDL tra i diversi progetti significa che gli sviluppatori che hanno familiarità con una libreria compatibile con UniFFI possono capire e lavorare rapidamente con le altre, creando un effetto di rete che va a vantaggio dell'intero ecosistema.


Tuttavia, UniFFI presenta notevoli limitazioni che gli sviluppatori devono considerare. La più significativa è la mancanza di supporto per le interfacce asincrone. Tutti i binding generati sono sincroni, il che richiede agli sviluppatori di gestire le operazioni asincrone all'interno del loro codice Rust e di presentare interfacce sincrone alle applicazioni di consumo. Inoltre, il posizionamento della documentazione rappresenta una sfida: la documentazione scritta nel codice Rust non viene trasferita ai binding generati, mentre la documentazione nei file UDL non è disponibile per i consumatori diretti della libreria Rust. Sebbene siano in corso sforzi per risolvere queste limitazioni attraverso il parsing e la generazione automatica, rimangono considerazioni per le implementazioni attuali. Infine, UniFFI genera i bindings del linguaggio ma non gestisce il packaging e la distribuzione specifici per la piattaforma, lasciando agli sviluppatori la gestione delle fasi finali di creazione dei pacchetti distribuibili per ogni piattaforma di destinazione.


# Sviluppare LNP/BP con SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## Nodo LN su SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### Comprendere l'architettura modulare di LDK


Il kit di sviluppo Lightning (LDK) adotta un approccio diverso all'implementazione di Lightning Network rispetto al software per nodi tradizionali come CLightning o LND. Mentre i nodi Lightning tradizionali funzionano come applicazioni daemon complete in esecuzione continua su una macchina, LDK funziona come una libreria Rust modulare che fornisce componenti primitivi per la costruzione di soluzioni Lightning personalizzate. Questa distinzione architettonica rende LDK flessibile, consentendo agli sviluppatori di assemblare le funzionalità di Lightning in modo da soddisfare i requisiti specifici del progetto.


La filosofia alla base di LDK è incentrata sulla modularità e sull'adattabilità. Invece di fornire una soluzione monolitica, LDK offre singoli componenti che possono essere combinati, personalizzati o sostituiti completamente. Ogni componente è dotato di implementazioni predefinite che funzionano immediatamente, ma gli sviluppatori hanno la libertà di sostituire le proprie implementazioni quando necessario. Ad esempio, LDK include implementazioni predefinite per il monitoraggio della blockchain, la firma delle transazioni e la comunicazione di rete, ma ognuna di queste può essere sostituita con soluzioni personalizzate adatte a casi d'uso o ambienti specifici.


Questo design modulare consente a LDK di funzionare su diverse piattaforme e scenari che sarebbero difficili da gestire per i nodi Lightning tradizionali. Le applicazioni mobili, i browser web, i dispositivi embedded e l'hardware specializzato possono tutti sfruttare i componenti di LDK in modo da soddisfare i propri vincoli e requisiti. L'architettura della libreria garantisce che gli sviluppatori possano creare applicazioni abilitate a Lightning senza essere vincolati a schemi operativi predeterminati o a dipendenze di sistema.


### Casi d'uso di LDK e flessibilità della piattaforma


La flessibilità architettonica di LDK apre numerosi casi d'uso che vanno ben oltre le tradizionali implementazioni di nodi Lightning. Lo sviluppo mobile di wallet rappresenta una delle applicazioni più interessanti, in cui LDK consente la creazione di portafogli Lightning non custodiali simili a Phoenix wallet. Queste implementazioni mobili possono mantenere il controllo dell'utente sulle chiavi private mentre si sincronizzano con i fornitori di servizi Lightning (LSP) quando si connettono, consentendo la ricezione dei pagamenti e la gestione dei canali senza soluzione di continuità anche in caso di connettività intermittente.


L'integrazione del modulo di sicurezza hardware (HSM) illustra un altro potente caso d'uso di LDK. Estraendo solo i componenti di firma e verifica delle transazioni, gli sviluppatori possono creare dispositivi di firma Lightning-aware che comprendono il contesto e le implicazioni delle transazioni Lightning. Questa capacità va oltre la semplice firma delle transazioni e include un'analisi intelligente dell'inoltro dei pagamenti, delle operazioni sui canali e delle decisioni critiche per la sicurezza. L'HSM può valutare se una transazione rappresenta un pagamento legittimo, un'operazione di instradamento o un tentativo potenzialmente dannoso, fornendo agli utenti informazioni significative sulla sicurezza.


Le applicazioni Lightning basate sul Web traggono notevoli vantaggi dalla filosofia di progettazione senza chiamate di sistema di LDK. Poiché gli ambienti WebAssembly non hanno accesso diretto a risorse di sistema come file system, socket di rete o fonti di entropia, l'approccio puro di LDK consente alle funzionalità di Lightning di operare senza problemi negli ambienti browser. Gli sviluppatori possono implementare livelli di rete personalizzati utilizzando WebSocket e fornire fonti di persistenza e casualità compatibili con i browser, mantenendo la piena conformità al protocollo Lightning.


### Componenti principali e architettura guidata dagli eventi


L'architettura interna di LDK ruota attorno a diversi componenti chiave che lavorano insieme attraverso un sistema guidato dagli eventi. Il sistema di gestione dei peer gestisce tutte le comunicazioni con altri nodi Lightning, implementando il protocollo noise per la crittografia e gestendo le strutture dei messaggi per la conformità al protocollo Lightning. Questo componente opera indipendentemente dal meccanismo di trasporto sottostante, consentendo agli sviluppatori di implementare il networking su socket TCP, WebSocket, connessioni seriali USB o qualsiasi altro canale di comunicazione bidirezionale.


Il channel manager funge da coordinatore centrale per le operazioni del canale Lightning, lavorando a stretto contatto con il peer manager per eseguire le operazioni di apertura, chiusura e pagamento del canale. Quando uno sviluppatore avvia l'apertura di un canale, il channel manager crea i messaggi di protocollo necessari e si coordina con il peer manager per gestire il processo di negoziazione in più fasi. Questa separazione delle preoccupazioni consente un'astrazione pulita tra la logica del protocollo Lightning e i dettagli della comunicazione di rete.


Il sistema di eventi di LDK fornisce notifiche asincrone per tutte le operazioni significative e i cambiamenti di stato. Gli eventi coprono l'intero spettro delle operazioni di Lightning, dalle connessioni e disconnessioni dei peer ai successi e ai fallimenti dei pagamenti, ai cambiamenti di stato dei canali e alle conferme della blockchain. Questo approccio guidato dagli eventi consente alle applicazioni di rispondere in modo appropriato all'attività della rete Lightning, mantenendo al contempo una separazione netta tra la funzionalità di base di LDK e la logica specifica dell'applicazione. Gli sviluppatori possono implementare gestori di eventi personalizzati che aggiornano le interfacce utente, attivano le notifiche o avviano azioni successive in base agli eventi della rete Lightning.


### Blockchain Integrazione e gestione dei dati


L'integrazione dei dati Blockchain rappresenta uno dei livelli di astrazione di LDK, progettato per ospitare qualsiasi cosa, dai nodi Bitcoin completi ai client mobili leggeri. LDK supporta due modalità primarie di interazione con la blockchain, ciascuna ottimizzata per diversi vincoli di risorse e requisiti operativi. La modalità a blocco completo consente alle applicazioni con accesso ai dati completi della blockchain di passare interi blocchi a LDK, consentendo un monitoraggio completo delle transazioni e una risposta immediata agli eventi rilevanti della blockchain.


Per gli ambienti con risorse limitate, LDK offre un approccio basato sul filtraggio che riduce i requisiti di larghezza di banda e di archiviazione. In questa modalità, LDK comunica i suoi interessi di monitoraggio attraverso interfacce astratte, richiedendo la sorveglianza di specifici ID di transazione, UTXO o modelli di script. Il livello applicativo può quindi implementare il monitoraggio utilizzando i server Electrum, i block explorer o altre fonti di dati blockchain leggere. Questo approccio consente ai portafogli mobili e alle applicazioni web di mantenere la funzionalità Lightning senza richiedere la sincronizzazione completa della blockchain.


Il livello di persistenza di LDK segue gli stessi principi di astrazione, fornendo alle applicazioni blob di dati binari che devono essere memorizzati e recuperati in modo affidabile. LDK gestisce tutta la complessità della serializzazione e della deserializzazione degli stati dei canali Lightning, dei dati di gossip della rete e di altre informazioni critiche. Le applicazioni devono semplicemente implementare meccanismi di archiviazione affidabili, utilizzando file system locali, servizi di archiviazione cloud o sistemi di database specializzati. Questo design garantisce che la gestione degli stati di Lightning rimanga solida, consentendo alle applicazioni di scegliere soluzioni di archiviazione che soddisfino i loro requisiti operativi e i loro modelli di sicurezza.


### Funzionalità avanzate e modelli di integrazione


Le capacità di LDK si estendono alle funzionalità del Lightning Network, come i pagamenti multipercorso, l'ottimizzazione dei percorsi e la gestione del gossip di rete. Il sistema di routing mantiene una visione completa della topologia del Lightning Network attraverso la partecipazione al protocollo gossip, consentendo di trovare percorsi intelligenti per i pagamenti. Le applicazioni possono influenzare le decisioni di routing attraverso i parametri di configurazione e possono persino implementare una logica di routing personalizzata per casi d'uso specifici.


Il sistema di binding linguistico della libreria consente l'integrazione di LDK in diversi ambienti di programmazione, supportando Java, Kotlin, Swift, TypeScript, JavaScript e C++. Questa compatibilità multipiattaforma consente alle applicazioni mobili scritte in linguaggi nativi di incorporare le funzionalità di Lightning mantenendo caratteristiche di performance ottimali. Il sistema di binding preserva l'architettura event-driven e il design modulare di LDK in tutti i linguaggi supportati, garantendo agli sviluppatori un'esperienza coerente indipendentemente dalla piattaforma di destinazione.


La stima delle commissioni e la trasmissione delle transazioni rappresentano ulteriori aree in cui LDK offre flessibilità. Le applicazioni possono implementare strategie di stima delle tariffe personalizzate che tengano conto dei loro specifici modelli operativi e dei requisiti degli utenti. Allo stesso modo, la trasmissione delle transazioni può essere personalizzata per funzionare con varie interfacce di rete Bitcoin, dalle connessioni dirette full node ai servizi di trasmissione di terze parti. Questa flessibilità garantisce che le applicazioni basate su LDK possano ottimizzare le interazioni con la blockchain per i loro casi d'uso specifici, mantenendo la conformità al protocollo Lightning e gli standard di sicurezza.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### La sfida dello sviluppo dei fulmini


Lo sviluppo di applicazioni che integrano i pagamenti Lightning rappresenta una barriera significativa per la maggior parte degli sviluppatori. Per creare un'applicazione con funzionalità di pagamento Lightning, gli sviluppatori devono essenzialmente diventare esperti di Lightning, comprendendo concetti complessi come la gestione dei canali, il bilanciamento della liquidità e la topologia della rete. Questo requisito di competenza crea un problema fondamentale per l'adozione di Lightning: mentre la rete Lightning in sé è operativa e i pagamenti sono affidabili, la complessità tecnica impedisce un'integrazione diffusa nelle applicazioni di tutti i giorni.


La sfida principale risiede nel divario tra ciò di cui gli sviluppatori hanno bisogno e ciò che vogliono fornire. Gli sviluppatori lavorano in genere con scadenze strette e preferiscono soluzioni semplici che consentano loro di concentrarsi sulle funzionalità principali dell'applicazione piuttosto che diventare esperti di infrastrutture di pagamento. Quando l'integrazione di Lightning è difficile, gli sviluppatori gravitano naturalmente verso le soluzioni di custodia, perché offrono il percorso di minor resistenza. Tuttavia, questa tendenza verso i servizi di deposito mina la proposta di valore fondamentale di Bitcoin, ovvero la sovranità finanziaria non depositaria.


### La visione di Breez, fulmini ovunque


Breez è nata da una visione semplice ma ambiziosa: far sì che tutti si connettano alla rete Lightning attraverso interfacce intuitive per l'economia Lightning. L'approccio dell'azienda riconosce che la rete Lightning, pur funzionando bene dal punto di vista tecnico, ha un disperato bisogno di essere adottata dagli utenti per raggiungere il suo pieno potenziale. La sfida dell'adozione va oltre i singoli utenti e comprende l'intero ecosistema di applicazioni e servizi che potrebbero beneficiare dell'integrazione di Lightning.


L'applicazione originale Breez ha dimostrato questa visione fornendo agli utenti un nodo Lightning non custodiale in esecuzione direttamente sui loro telefoni cellulari. L'applicazione ha messo in mostra funzionalità di Lightning come lo streaming di micropagamenti per i podcaster e la funzionalità di punto vendita. Tuttavia, l'applicazione Breez ha anche rivelato un limite architettonico critico: l'ecosistema delle applicazioni mobili non facilita la comunicazione tra le applicazioni, costringendo gli sviluppatori a costruire tutte le funzionalità legate a Lightning in un'unica applicazione piuttosto che consentire alle applicazioni specializzate di sfruttare l'infrastruttura Lightning condivisa.


Gli insegnamenti tratti dall'applicazione Breez hanno portato a un'intuizione cruciale: il futuro dell'adozione di Lightning dipende dalla conquista degli sviluppatori. Se l'integrazione di Lightning senza custodia diventa l'opzione più semplice per gli sviluppatori, diventerà la scelta predefinita. Questo approccio offre anche vantaggi normativi, in quanto il software non custodiale deve affrontare meno ostacoli normativi rispetto ai servizi di custodia, rendendo più facile per gli sviluppatori spedire le loro applicazioni a livello globale.


### L'architettura dell'SDK Breez


L'SDK Breez offre un approccio alternativo all'integrazione delle funzionalità di Lightning nelle applicazioni. Invece di richiedere che ogni applicazione esegua il proprio nodo Lightning, l'SDK fornisce un'architettura che mantiene i principi di non-custodia, semplificando al contempo l'esperienza degli sviluppatori. Nel suo nucleo, l'SDK fornisce a ogni utente finale il proprio nodo Lightning personale che gira sull'infrastruttura Greenlight, il servizio di hosting di nodi Lightning basato sul cloud di Blockstream.


Questa architettura risolve contemporaneamente diversi problemi critici. Gli utenti non devono preoccuparsi della gestione dei database, dei tempi di attività dei server o della manutenzione dell'infrastruttura, preoccupazioni che sarebbero eccessive per i consumatori tipici. Tuttavia, a differenza delle soluzioni di custodia tradizionali, Greenlight non ha mai accesso alle chiavi degli utenti. Il nodo Lightning nel cloud non può eseguire alcuna operazione senza un'applicazione attivamente connessa che possa firmare transazioni e messaggi. Questo design mantiene i vantaggi di sicurezza dell'autocustodia, eliminando al contempo la complessità operativa.


L'SDK supporta anche l'interoperabilità. Più applicazioni possono connettersi al nodo Lightning dello stesso utente utilizzando la stessa frase seed, consentendo agli utenti di mantenere un unico saldo Lightning in diverse applicazioni specializzate. Ad esempio, un utente potrebbe avere un'applicazione Lightning wallet generale e un'applicazione specializzata in podcasting, entrambe con accesso agli stessi fondi e canali Lightning. Questa architettura consente lo sviluppo di applicazioni specializzate e mirate, mantenendo un'infrastruttura finanziaria unificata.


### Fornitori di servizi lightning e liquidità just-in-time


Una componente fondamentale dell'SDK Breez è l'integrazione con i Lightning Service Provider (LSP), che funzionano in modo analogo agli Internet Service Provider ma per la rete Lightning. Gli LSP risolvono una delle sfide più complesse di Lightning: la gestione della liquidità. Nei canali Lightning, i fondi possono fluire solo nelle direzioni in cui esiste la liquidità, come le perline di un abaco che possono muoversi solo dove c'è spazio.


L'SDK implementa canali "just-in-time" attraverso gli LSP, gestendo automaticamente la liquidità senza l'intervento dell'utente. Quando un utente ha bisogno di ricevere un pagamento ma non ha sufficiente liquidità in entrata, l'LSP apre automaticamente un nuovo canale Lightning nel momento in cui arriva il pagamento. Questo processo avviene senza soluzione di continuità in background, assicurando che gli utenti possano sempre ricevere i pagamenti senza dover comprendere le meccaniche dei canali sottostanti.


L'integrazione con gli LSP va oltre la semplice gestione della liquidità. L'SDK include tutte le funzionalità di Lightning: servizi di watchtower integrati per la sicurezza, interoperabilità on-chain tramite swap sottomarini, accesso ai fiat tramite servizi come MoonPay e supporto per i protocolli LNURL. Il sistema fornisce inoltre backup e ripristino senza soluzione di continuità, assicurando che gli utenti non perdano mai l'accesso ai loro fondi anche se i fornitori di infrastrutture cambiano o diventano indisponibili.


### Esperienza di implementazione e di sviluppo


L'SDK Breez dà la priorità all'esperienza dello sviluppatore grazie al suo approccio completo e integrato nelle batterie. L'SDK fornisce binding per diversi linguaggi di programmazione, tra cui Rust, Swift, Kotlin, Python, Go, React Native, Flutter e C#, consentendo agli sviluppatori di integrare i pagamenti Lightning utilizzando gli strumenti di sviluppo preferiti. L'architettura astrae dalla complessità di Lightning attraverso le API, mantenendo la sicurezza della rete Lightning.


I componenti chiave lavorano insieme per fornire questa esperienza semplificata. Il parser di input gestisce automaticamente i diversi formati di pagamento, determinando se una stringa rappresenta una fattura, un LNURL o un altro metodo di pagamento e indirizzandola alla funzione di gestione appropriata. Il firmatore integrato gestisce tutte le operazioni crittografiche in background, mentre lo swapper gestisce le interazioni on-chain in modo trasparente. Questo design consente agli sviluppatori di concentrarsi sulla proposta di valore unica della loro applicazione, anziché diventare esperti dell'infrastruttura Lightning.


L'architettura trustless dell'SDK garantisce che Greenlight possa osservare gli stati dei canali e le informazioni di routing, ma non possa accedere ai fondi degli utenti o eseguire operazioni non autorizzate. Gli utenti mantengono il controllo completo sulle loro chiavi private, che non lasciano mai i loro dispositivi. Questo approccio rappresenta un compromesso attentamente considerato tra semplicità operativa e privacy, fornendo un percorso pratico per l'adozione di Lightning a livello mainstream e preservando al contempo i principi fondamentali di sovranità finanziaria di Bitcoin.


## LDK vs Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Comprendere le limitazioni di Lightning Development Kit (LDK)


Il Lightning Development Kit è una raccolta di librerie Rust progettata per fornire agli sviluppatori flessibilità nella creazione di applicazioni Lightning Network . Tuttavia, questa flessibilità è accompagnata da significative sfide di implementazione che sono emerse durante lo sviluppo reale del Lipa . La natura di basso livello dell'LDK significa che gli sviluppatori devono gestire in modo indipendente numerose attività complesse, dalla sincronizzazione del grafo di rete all'ottimizzazione dell'instradamento dei pagamenti. Se da un lato questo approccio offre un controllo completo sull'implementazione di Lightning, dall'altro richiede notevoli risorse di sviluppo e una profonda competenza tecnica per ottenere un'affidabilità pronta per la produzione.


Una delle caratteristiche più critiche mancanti in LDK era il supporto per LNURL, uno standard ampiamente adottato che semplifica le interazioni Lightning Network per gli utenti finali. Inoltre, l'assenza di uscite di ancoraggio poneva seri problemi operativi, in particolare negli ambienti con tariffe elevate. Le uscite Anchor risolvono un problema fondamentale delle chiusure forzate dei canali Lightning: quando le tariffe di rete aumentano drasticamente, i canali con tariffe predefinite possono diventare impossibili da chiudere unilateralmente perché la tariffa preimpostata diventa insufficiente per la conferma della transazione. Questa limitazione si è rivelata particolarmente problematica per le applicazioni mobili wallet, dove gli utenti potrebbero abbandonare il wallet senza coordinare la chiusura cooperativa dei canali, lasciando i fondi potenzialmente bloccati durante i picchi delle tariffe.


La relativa immaturità dell'LDK si è manifestata anche nell'inaffidabilità dell'instradamento dei pagamenti, un problema critico per qualsiasi applicazione Lightning. Nonostante si tratti di un'implementazione tecnicamente valida, l'ampia portata dell'LDK come soluzione generica ha reso difficile risolvere rapidamente problemi specifici. Il team di sviluppo si è trovato a passare molto tempo a risolvere problemi di routing e a implementare funzionalità che idealmente dovrebbero essere gestite a livello di libreria, con un impatto finale sulla velocità di sviluppo e sulla qualità dell'esperienza utente.


### Scoprire i vantaggi dell'SDK Breez e di Greenlight


Il passaggio all'SDK Breez ha rappresentato un cambiamento nell'approccio architettonico, passando da un nodo Lightning autogestito a una soluzione basata sul cloud e alimentata dal servizio Greenlight di Blockstream. Questo cambiamento ha risolto immediatamente diversi punti critici riscontrati con l'implementazione di LDK. Il miglioramento più significativo ha riguardato l'affidabilità dei pagamenti, soprattutto grazie alla capacità di Greenlight di mantenere un grafico di rete sempre aggiornato. A differenza delle tradizionali implementazioni di Lightning mobile che devono sincronizzare le informazioni di rete all'avvio dell'applicazione, i nodi di Greenlight funzionano continuamente nel cloud, mantenendo la consapevolezza della rete in tempo reale e fornendo istantaneamente i dati completi del grafo quando gli utenti si connettono.


Questa architettura sfrutta l'implementazione Core Lightning (CLN), collaudata in battaglia, che per anni ha instradato con successo i pagamenti come una delle implementazioni originali del Lightning Network. L'esperienza accumulata e la comprovata affidabilità di CLN hanno fornito miglioramenti immediati in termini di stabilità rispetto al più giovane progetto LDK. Quando gli utenti attivano il loro wallet alimentato da Greenlight, ereditano immediatamente la conoscenza della rete e le capacità di instradamento di un nodo Lightning in continuo funzionamento, eliminando i ritardi di sincronizzazione e le incertezze di instradamento che affliggevano l'implementazione precedente.


La filosofia di progettazione del Breez SDK è stata utile per lo sviluppo del wallet. Invece di fornire un toolkit Lightning generico, il Breez si concentra specificamente sulle applicazioni wallet per gli utenti finali, consentendo al team di sviluppo di concentrare i propri sforzi sulla creazione di soluzioni complete per questo caso d'uso specifico. Questo approccio mirato ha permesso a Breez di integrare servizi essenziali direttamente nell'SDK, tra cui la funzionalità Lightning Service Provider (LSP) che consente agli utenti di ricevere pagamenti immediatamente dopo l'installazione di wallet, senza richiedere procedure manuali di apertura dei canali.


### Funzionalità complete e miglioramenti dell'esperienza utente


L'approccio integrato del Breez SDK va oltre le funzionalità di base di Lightning, incorporando caratteristiche che migliorano l'esperienza dell'utente. L'integrazione LSP integrata elimina la barriera tradizionale che impone agli utenti di comprendere la gestione dei canali, consentendo la ricezione immediata dei pagamenti per le nuove installazioni di wallet. Questo processo di onboarding contribuisce all'adozione del mainstream, in quanto gli utenti possono iniziare a ricevere i pagamenti Lightning senza alcuna conoscenza tecnica o procedura di configurazione.


La funzionalità di swap on-chain fornisce un ulteriore livello di ottimizzazione dell'esperienza utente, consentendo di presentare agli utenti un bilancio unificato. Invece di costringere gli utenti a comprendere la distinzione tra Lightning e on-chain Bitcoin, il servizio di swap consente la conversione automatica tra questi livelli, a seconda delle necessità. Quando gli utenti hanno bisogno di effettuare pagamenti on-chain, il sistema può scambiare senza problemi i fondi Lightning in on-chain Bitcoin dietro le quinte, mantenendo l'illusione di un unico saldo liquido e gestendo la complessità tecnica internamente.


Il supporto dell'SDK per le riserve a canale zero risolve un problema significativo dell'esperienza utente nelle implementazioni tradizionali di Lightning. Le riserve di canale di solito impediscono agli utenti di spendere l'intero saldo visualizzato, creando confusione quando i pagamenti falliscono nonostante i fondi apparentemente sufficienti. Eliminando queste riserve, Breez consente agli utenti di spendere l'intero saldo visualizzato, anche se ciò richiede al LSP di accettare un rischio aggiuntivo. Questo compromesso esemplifica l'approccio incentrato sull'utente di Breez, in cui la complessità tecnica e il rischio sono assorbiti dai fornitori di servizi per creare esperienze intuitive per gli utenti.


Caratteristiche aggiuntive come il supporto LNURL, i servizi di cambio e la sincronizzazione multidispositivo dimostrano ulteriormente l'approccio completo dell'SDK allo sviluppo wallet. L'architettura basata su cloud consente agli utenti di accedere al proprio nodo Lightning da più dispositivi o applicazioni, con Breez che gestisce la sincronizzazione dello stato tra questi diversi punti di accesso. I punti della roadmap futura includono la funzionalità spendi-tutto per il drenaggio completo del wallet, lo splicing per la gestione dinamica dei canali e un mercato di LSP concorrenti per introdurre una sana concorrenza nella fornitura di servizi.


### Valutazione dei compromessi e dei problemi di centralizzazione


Il passaggio all'SDK Breez e a Greenlight introduce importanti compromessi di centralizzazione che devono essere attentamente considerati nel contesto dei principi di decentralizzazione di Bitcoin. L'architettura basata sul cloud significa che i nodi Lightning degli utenti operano sull'infrastruttura di Blockstream, creando dipendenze sia dal funzionamento continuo di Greenlight sia dallo sviluppo continuo di Breez. Questa centralizzazione va al di là della mera convenienza, in quanto può avere un impatto sulla capacità degli utenti di recuperare i fondi in caso di indisponibilità dei servizi o di censura.


Gli scenari di recupero presentano sfide particolari in questa architettura. Sebbene gli utenti mantengano il controllo delle loro chiavi private, l'accesso ai fondi senza l'infrastruttura di Greenlight richiederebbe competenze tecniche per avviare nodi Core Lightning indipendenti e ripristinare gli stati dei canali. Per i singoli utenti, questo processo di recupero si rivelerebbe probabilmente proibitivo, e anche i fornitori di wallet si troverebbero ad affrontare sfide significative per migrare intere basi di utenti verso un'infrastruttura alternativa se i servizi di Greenlight venissero interrotti.


Anche le considerazioni sulla privacy cambiano con questo cambiamento architettonico. L'instradamento basato sul cloud significa che Greenlight può potenzialmente ottenere visibilità sulle destinazioni dei pagamenti, mentre le precedenti architetture basate solo su LSP limitavano la fuga di informazioni agli importi e ai tempi dei pagamenti. La generazione di Invoice nel cloud espande ulteriormente la potenziale esposizione delle informazioni, in quanto le fatture inutilizzate che prima rimanevano private sui dispositivi degli utenti ora passano attraverso l'infrastruttura di Blockstream.


Nonostante questi problemi di centralizzazione, i vantaggi pratici superano spesso i rischi teorici per molti casi d'uso. L'affidabilità migliorata, il set completo di funzionalità e l'esperienza utente superiore consentono agli sviluppatori wallet di concentrarsi sulle innovazioni del livello applicativo piuttosto che sulla gestione dell'infrastruttura Lightning. Questa divisione del lavoro riflette la maturazione di un ecosistema in cui fornitori di servizi specializzati gestiscono sfide tecniche complesse, consentendo agli sviluppatori di applicazioni di concentrarsi sull'esperienza utente e sulla logica aziendale. La chiave sta nel comprendere chiaramente questi compromessi e nel prendere decisioni informate in base ai requisiti dei casi d'uso specifici e ai livelli di tolleranza del rischio.




# Sezione finale

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Recensioni e valutazioni

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusione

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>
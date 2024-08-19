---
name: Introduzione alla crittografia formale
goal: Un'introduzione approfondita alla scienza e alla pratica della crittografia.
objectives:
  - Esplorare i cifrari di Beale e i metodi crittografici moderni per comprendere i concetti di base e storici della crittografia.
  - Approfondire la teoria dei numeri, i gruppi e i campi per padroneggiare i concetti matematici chiave che stanno alla base della crittografia.
  - Studiare il cifrario a flusso RC4 e l'AES con chiave a 128 bit per apprendere sugli algoritmi crittografici simmetrici.
  - Investigare il criptosistema RSA, la distribuzione delle chiavi e le funzioni hash per esplorare la crittografia asimmetrica.

---

# Approfondimento nella crittografia

È difficile trovare molti materiali che offrano un buon compromesso nell'educazione crittografica.

Da un lato, ci sono trattati formali e lunghi, accessibili davvero solo a coloro che hanno una solida formazione in matematica, logica o qualche altra disciplina formale. Dall'altro lato, ci sono introduzioni molto generali che nascondono troppi dettagli per chiunque sia almeno un po' curioso.

Questa introduzione alla crittografia cerca di catturare il compromesso. Sebbene debba essere relativamente impegnativa e dettagliata per chiunque sia nuovo alla crittografia, non è il labirinto di un tipico trattato fondazionale.

+++

# Un'introduzione alla Crittografia
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Breve descrizione
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Questo libro offre un'introduzione approfondita alla scienza e alla pratica della crittografia. Dove possibile, si concentra su una esposizione concettuale, piuttosto che formale, del materiale.

> Questo corso si basa sul [repo di JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Tutti i diritti a lui. Il contenuto non è ancora finito ed è qui solo per mostrare come potremmo integrarlo se JWburger's fosse d'accordo.

### Motivazione e obiettivi

È difficile trovare molti materiali che offrano un buon compromesso nell'educazione crittografica.

Da un lato, ci sono trattati formali e lunghi, accessibili davvero solo a coloro che hanno una solida formazione in matematica, logica o qualche altra disciplina formale. Dall'altro lato, ci sono introduzioni molto generali che nascondono troppi dettagli per chiunque sia almeno un po' curioso.

Questa introduzione alla crittografia cerca di catturare il compromesso. Sebbene debba essere relativamente impegnativa e dettagliata per chiunque sia nuovo alla crittografia, non è il labirinto di un tipico trattato fondazionale.

### Pubblico di destinazione

Dagli sviluppatori ai curiosi intellettualmente, questo libro è utile per chiunque voglia più di una comprensione superficiale della crittografia. Se il tuo obiettivo è padroneggiare il campo della crittografia, allora questo libro è anche un buon punto di partenza.

### Linee guida per la lettura

Il libro attualmente contiene sette capitoli: "Cos'è la Crittografia?" (Capitolo 1), "Fondamenti Matematici della Crittografia I" (Capitolo 2), "Fondamenti Matematici della Crittografia II" (Capitolo 3), "Crittografia Simmetrica" (Capitolo 4), "RC4 e AES" (Capitolo 5), "Crittografia Asimmetrica" (Capitolo 6) e "Il criptosistema RSA" (Capitolo 7). Un capitolo finale, "La Crittografia nella Pratica", sarà ancora aggiunto. Si concentra su varie applicazioni crittografiche, inclusa la sicurezza del livello di trasporto, il routing a cipolla e il sistema di scambio di valore di Bitcoin.
A meno che tu non abbia una solida formazione in matematica, la teoria dei numeri è probabilmente l'argomento più difficile di questo libro. Offro una panoramica di essa nel Capitolo 3, e appare anche nell'esposizione dell'AES nel Capitolo 5 e del criptosistema RSA nel Capitolo 7.
Se stai davvero lottando con i dettagli formali in queste parti del libro, ti consiglio di accontentarti di una lettura ad alto livello di esse la prima volta.

### Ringraziamenti

Il libro più influente nella formazione di questo è stato _Introduction to Modern Cryptography_ di Jonathan Katz e Yehuda Lindell, CRC Press (Boca Raton, FL), 2015. Un corso accompagnatorio è disponibile su Coursera con il nome "Cryptography".

Le principali fonti aggiuntive che sono state utili nella creazione della panoramica in questo libro sono Simon Singh, _The Code Book_, Fourth Estate (Londra, 1999); Christof Paar e Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) e un corso basato sul libro di Paar chiamato "Introduction to Cryptography" (disponibile su https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); e Bruce Schneier, _Applied Cryptography_, 2ª ed., 2015 (Indianapolis, IN: John Wiley & Sons).

Citerò solo informazioni e risultati molto specifici che prendo da queste fonti, ma voglio qui riconoscere il mio debito generale verso di esse.

Per quei lettori che desiderano cercare conoscenze più avanzate sulla crittografia dopo questa introduzione, consiglio vivamente il libro di Katz e Lindell. Il corso di Katz su Coursera è in qualche modo più accessibile del libro.

### Contributi

Si prega di dare un'occhiata al file dei contributi nel repository per alcune linee guida su come supportare il progetto.

# Cos'è la Crittografia?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

Iniziamo la nostra indagine sul campo della crittografia con uno degli episodi più affascinanti e divertenti della sua storia: quello dei cifrari di Beale.

La storia dei cifrari di Beale è, a mio avviso, più probabile che sia finzione piuttosto che realtà. Ma si dice sia avvenuta come segue.

## I cifrari di Beale
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>

Sia nell'inverno del 1820 che nel 1822, un uomo di nome Thomas J. Beale soggiornò in un'osteria di proprietà di Robert Morriss a Lynchburg (Virginia). Alla fine del secondo soggiorno di Beale, egli consegnò a Morriss una scatola di ferro contenente documenti preziosi per la custodia.

Qualche mese dopo, Morriss ricevette una lettera da Beale datata 9 maggio 1822. Essa sottolineava il grande valore del contenuto della scatola di ferro e forniva alcune istruzioni a Morriss: se né Beale né nessuno dei suoi associati fosse mai venuto a reclamare la scatola, avrebbe dovuto aprirla esattamente dieci anni dopo la data della lettera (cioè il 9 maggio 1832). Alcuni dei documenti all'interno sarebbero stati scritti in testo normale. Diversi altri, tuttavia, sarebbero stati “incomprensibili senza l'ausilio di una chiave”. Questa “chiave” sarebbe stata poi consegnata a Morriss da un amico non nominato di Beale nel giugno del 1832.
Nonostante le istruzioni chiare, Morriss non aprì la scatola nel maggio del 1832 e il misterioso amico di Beale non si presentò a giugno di quell'anno. Fu solo nel 1845 che l'oste decise finalmente di aprire la scatola. Al suo interno, Morriss trovò una nota che spiegava come Beale e i suoi associati avessero scoperto oro e argento nel West e lo avessero sepolto, insieme ad alcuni gioielli, per metterlo al sicuro. Inoltre, la scatola conteneva tre **cifrari**: testi scritti in codice che richiedono una **chiave crittografica**, o un segreto, e un algoritmo accompagnatorio per essere decifrati. Questo processo di sblocco di un cifrario è noto come **decrittazione**, mentre il processo di blocco è noto come **crittazione**. (Come spiegato nel Capitolo 3, il termine cifrario può assumere vari significati. Nel nome "cifrari di Beale", è l'abbreviazione di cifrari.)

I tre cifrari che Morriss trovò nella scatola di ferro consistevano ciascuno in una serie di numeri separati da virgole. Secondo la nota di Beale, questi cifrari fornivano separatamente la posizione del tesoro, il contenuto del tesoro e un elenco di nomi con gli eredi legittimi al tesoro e le loro quote (quest'ultima informazione era rilevante nel caso in cui Beale e i suoi associati non venissero mai a reclamare la scatola).

Morris tentò di decifrare i tre cifrari per vent'anni. Questo sarebbe stato facile con la chiave. Ma Morriss non aveva la chiave e non ebbe successo nei suoi tentativi di recuperare i testi originali, o **testi in chiaro** come vengono tipicamente chiamati in crittografia.

Avvicinandosi alla fine della sua vita, Morriss passò la scatola a un amico nel 1862. Questo amico successivamente pubblicò un opuscolo nel 1885, sotto lo pseudonimo di J.B. Ward. Includeva una descrizione della storia (presunta) della scatola, dei tre cifrari e di una soluzione che aveva trovato per il secondo cifrario. (A quanto pare, esiste una chiave per ciascun cifrario, e non una chiave unica che funziona su tutti e tre i cifrari come Beale sembrava aver suggerito originariamente nella sua lettera a Morriss.)

Puoi vedere il secondo cifrario in *Figura 2* qui sotto.<sup>[2](#footnote2)</sup> La chiave per questo cifrario è la Dichiarazione di Indipendenza degli Stati Uniti. La procedura di decrittazione si riduce all'applicazione delle seguenti due regole:

* Per qualsiasi numero n nel cifrario, localizza la n-esima parola nella Dichiarazione di Indipendenza degli Stati Uniti
* Sostituisci il numero n con la prima lettera della parola trovata

*Figura 1: Cifrario di Beale n. 2*

![Figura 1: Cifrario di Beale n. 2](assets/Figure1-1.webp "Figura 1: Cifrario di Beale n. 2")

Ad esempio, il primo numero del secondo cifrario è 115. La 115esima parola della Dichiarazione di Indipendenza è “instituted”, quindi la prima lettera del testo in chiaro è “i”. Il cifrario non indica direttamente gli spazi tra le parole e le maiuscole. Ma dopo aver decifrato le prime parole, si può logicamente dedurre che la prima parola del testo in chiaro era semplicemente “I”. (Il testo in chiaro inizia con la frase “I have deposited in the county of Bedford.”)
Dopo la decifrazione, il secondo messaggio fornisce i dettagli del contenuto del tesoro (oro, argento e gioielli) e suggerisce che è stato sepolto in pentole di ferro e coperto con rocce nella Contea di Bedford (Virginia). Le persone amano un buon mistero, quindi sono stati compiuti grandi sforzi per decifrare gli altri due cifrari di Beale, in particolare quello che descrive la posizione del tesoro. Anche vari criptografi di spicco hanno tentato di decifrarli. Tuttavia, fino ad ora, nessuno è stato in grado di decifrare gli altri due testi cifrati.

## Crittografia moderna
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Storie affascinanti come quella dei cifrari di Beale sono ciò che la maggior parte di noi associa alla crittografia. Eppure, la crittografia moderna si differenzia in almeno quattro modi importanti da questi tipi di esempi storici.

Primo, storicamente la crittografia è stata interessata solo alla **segretezza** (o confidenzialità).<sup>[3](#footnote3)</sup> I testi cifrati venivano creati per garantire che solo certe parti potessero essere a conoscenza delle informazioni nei testi in chiaro, come nel caso dei cifrari di Beale. Affinché uno schema di crittografia servisse bene questo scopo, la decifrazione del testo cifrato dovrebbe essere fattibile solo se si possiede la chiave.

La crittografia moderna si occupa di una gamma più ampia di temi oltre alla semplice segretezza. Questi temi includono principalmente (1) **integrità del messaggio**—cioè, assicurare che un messaggio non sia stato modificato; (2) **autenticità del messaggio**—cioè, assicurare che un messaggio provenga realmente da un determinato mittente; e (3) **non ripudio**—cioè, assicurare che un mittente non possa negare falsamente in seguito di aver inviato un messaggio.<sup>[4](#footnote4)</sup>

Una distinzione importante da tenere a mente è, quindi, tra uno **schema di crittografia** e uno **schema crittografico**. Uno schema di crittografia è solo interessato alla segretezza. Mentre uno schema di crittografia è uno schema crittografico, il contrario non è vero. Uno schema crittografico può anche servire gli altri temi principali della crittografia, inclusi integrità, autenticità e non ripudio.

I temi dell'integrità e dell'autenticità sono altrettanto importanti quanto la segretezza. I nostri sistemi di comunicazione moderni non sarebbero in grado di funzionare senza garanzie riguardo l'integrità e l'autenticità delle comunicazioni. Il non ripudio è anche una preoccupazione importante, come per i contratti digitali, ma meno ubiquamente necessario nelle applicazioni crittografiche rispetto alla segretezza, integrità e autenticità.

Secondo, gli schemi di crittografia classici come i cifrari di Beale coinvolgono sempre una chiave che era condivisa tra tutte le parti rilevanti. Tuttavia, molti schemi crittografici moderni coinvolgono non solo una, ma due chiavi: una **privata** e una **pubblica**. Mentre la prima dovrebbe rimanere privata in qualsiasi applicazione, la seconda è tipicamente di dominio pubblico (da qui i loro rispettivi nomi). Nel regno della crittografia, la chiave pubblica può essere utilizzata per cifrare il messaggio, mentre la chiave privata può essere utilizzata per decifrarlo.

Il ramo della crittografia che si occupa di schemi in cui tutte le parti condividono una chiave è noto come **crittografia simmetrica**. La singola chiave in tale schema è solitamente chiamata **chiave privata** (o chiave segreta). Il ramo della crittografia che si occupa di schemi che richiedono una coppia di chiavi privata-pubblica è noto come **crittografia asimmetrica**. Questi rami sono talvolta anche denominati **crittografia a chiave privata** e **crittografia a chiave pubblica**, rispettivamente (anche se ciò può creare confusione, poiché gli schemi crittografici a chiave pubblica hanno anche chiavi private).
L'avvento della crittografia asimmetrica alla fine degli anni '70 è stato uno degli eventi più importanti nella storia della crittografia. Senza di essa, la maggior parte dei nostri sistemi di comunicazione moderni, inclusi Bitcoin, non sarebbero possibili, o almeno sarebbero molto impraticabili.

Importante, la crittografia moderna non è esclusivamente lo studio degli schemi crittografici a chiave simmetrica e asimmetrica (anche se ciò copre gran parte del campo). Ad esempio, la crittografia si occupa anche di funzioni hash e generatori di numeri pseudocasuali, e si possono costruire applicazioni su questi primitivi che non sono correlati alla crittografia a chiave simmetrica o asimmetrica.

In terzo luogo, gli schemi di cifratura classici, come quelli utilizzati nei cifrari di Beale, erano più arte che scienza. La loro sicurezza percepita era in gran parte basata su intuizioni riguardanti la loro complessità. Tipicamente, venivano corretti quando si apprendeva un nuovo attacco contro di essi, o abbandonati completamente se l'attacco era particolarmente grave. La crittografia moderna, tuttavia, è una scienza rigorosa con un approccio formale e matematico sia nello sviluppo che nell'analisi degli schemi crittografici.

Specificamente, la crittografia moderna si concentra su **prove formali di sicurezza**. Qualsiasi prova di sicurezza per uno schema crittografico procede in tre passaggi:

1. La dichiarazione di una **definizione crittografica di sicurezza**, cioè un insieme di obiettivi di sicurezza e la minaccia posta dall'attaccante.
2. La dichiarazione di eventuali ipotesi matematiche riguardo alla complessità computazionale dello schema. Ad esempio, uno schema crittografico può contenere un generatore di numeri pseudocasuali. Anche se non possiamo dimostrare che questi esistano, possiamo supporre che esistano.
3. L'esposizione di una **prova matematica di sicurezza** dello schema sulla base della nozione formale di sicurezza e di eventuali ipotesi matematiche.

In quarto luogo, mentre storicamente la crittografia era utilizzata principalmente in ambito militare, è venuta a permeare le nostre attività quotidiane nell'era digitale. Che tu stia facendo operazioni bancarie online, postando sui social media, acquistando un prodotto da Amazon con la tua carta di credito, o inviando bitcoin a un amico, la crittografia è il sine qua non della nostra era digitale.

Data queste quattro caratteristiche della crittografia moderna, potremmo caratterizzare la **crittografia** moderna come la scienza che si occupa dello sviluppo formale e dell'analisi degli schemi crittografici per proteggere le informazioni digitali dagli attacchi avversari. La sicurezza qui dovrebbe essere intesa in senso ampio come la prevenzione di attacchi che danneggiano la segretezza, l'integrità, l'autenticazione e/o la non ripudiabilità nelle comunicazioni.

La crittografia è meglio vista come una sottodisciplina della **cybersecurity**, che si occupa di prevenire il furto, il danneggiamento e l'uso improprio dei sistemi informatici. Da notare che molte preoccupazioni sulla cybersecurity hanno poco o solo un parziale collegamento con la crittografia.

Ad esempio, se un'azienda ospita server costosi localmente, potrebbe essere preoccupata di proteggere quest'hardware dal furto e dal danneggiamento. Sebbene questa sia una preoccupazione di cybersecurity, ha poco a che fare con la crittografia.

Per un altro esempio, gli **attacchi phishing** sono un problema comune nella nostra era moderna. Questi attacchi tentano di ingannare le persone tramite un'e-mail o qualche altro mezzo di messaggistica per indurle a rinunciare a informazioni sensibili come password o numeri di carte di credito. Sebbene la crittografia possa aiutare a indirizzare gli attacchi phishing fino a un certo punto, un approccio completo richiede più che semplicemente l'uso di un po' di crittografia.

## Comunicazioni aperte

La crittografia moderna è progettata per fornire garanzie di sicurezza in un ambiente di **comunicazioni aperte**. Se il nostro canale di comunicazione è così ben protetto che gli intercettatori non hanno alcuna possibilità di manipolare o anche solo osservare i nostri messaggi, allora la crittografia è superflua. La maggior parte dei nostri canali di comunicazione, tuttavia, è tutt'altro che così ben sorvegliata.
La spina dorsale della comunicazione nel mondo moderno è una vasta rete di cavi in fibra ottica. Effettuare chiamate telefoniche, guardare la televisione e navigare sul web in una casa moderna dipende generalmente da questa rete di cavi in fibra ottica (una piccola percentuale può dipendere esclusivamente da satelliti). È vero che potresti avere diverse connessioni dati nella tua casa, come il cavo coassiale, la linea digitale asimmetrica per abbonati e il cavo in fibra ottica. Ma, almeno nel mondo sviluppato, questi diversi mezzi di trasmissione dati si uniscono rapidamente fuori dalla tua casa a un nodo in una vasta rete di cavi in fibra ottica che collega l'intero globo. Fanno eccezione alcune aree remote del mondo sviluppato, come negli Stati Uniti e in Australia, dove il traffico dati potrebbe ancora viaggiare anche per lunghe distanze su tradizionali fili di rame telefonici.

Sarebbe impossibile impedire ai potenziali aggressori di accedere fisicamente a questa rete di cavi e alla sua infrastruttura di supporto. Infatti, sappiamo già che la maggior parte dei nostri dati viene intercettata da varie agenzie di intelligence nazionali in punti cruciali di intersezione di Internet. Questo include tutto, dai messaggi di Facebook agli indirizzi dei siti web che visiti.

Mentre sorvegliare i dati su larga scala richiede un avversario potente, come un'agenzia di intelligence nazionale, gli aggressori con poche risorse possono facilmente tentare di intercettare su scala più locale. Anche se ciò può avvenire a livello di intercettazione dei cavi, è molto più facile intercettare le comunicazioni wireless.

La maggior parte dei dati della nostra rete locale—sia nelle nostre case, in ufficio o in un caffè—viaggia ora tramite onde radio verso punti di accesso wireless su router tutto-in-uno, piuttosto che attraverso cavi fisici. Quindi, un aggressore ha bisogno di poche risorse per intercettare qualsiasi traffico locale. Questo è particolarmente preoccupante poiché la maggior parte delle persone fa molto poco per proteggere i dati che viaggiano attraverso le loro reti locali. Inoltre, i potenziali aggressori possono anche prendere di mira le nostre connessioni a banda larga mobile, come 3G, 4G e 5G. Tutte queste comunicazioni wireless sono un bersaglio facile per gli aggressori.

Pertanto, l'idea di mantenere segrete le comunicazioni proteggendo il canale di comunicazione è un'aspirazione irrimediabilmente illusoria per gran parte del mondo moderno. Tutto ciò che sappiamo giustifica una severa paranoia: dovresti sempre presumere che qualcuno stia ascoltando. E la crittografia è il principale strumento che abbiamo per ottenere un qualche tipo di sicurezza in questo ambiente moderno.
[^7]: Vedi, per esempio, Olga Khazan, "La pratica inquietante e di lunga data dell'intercettazione dei cavi sottomarini", *The Atlantic*, 16 luglio 2013 (disponibile su [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)) [^7].

# Fondamenti Matematici della Crittografia I
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

La crittografia si basa sulla matematica. E se vuoi costruire una comprensione della crittografia che vada oltre il superficiale, devi essere a tuo agio con quella matematica.

Questo capitolo introduce la maggior parte delle matematiche di base che incontrerai nell'apprendimento della crittografia. Gli argomenti includono variabili casuali, operazioni modulo, operazioni XOR e pseudocasualità. Dovresti padroneggiare il materiale in queste sezioni per una comprensione non superficiale della crittografia.

Il capitolo successivo tratta la teoria dei numeri, che è molto più impegnativa.

## Variabili casuali
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Una variabile casuale è tipicamente denotata da una lettera maiuscola non in grassetto. Quindi, per esempio, potremmo parlare di una variabile casuale X, una variabile casuale Y o una variabile casuale Z. Questa è la notazione che utilizzerò anche da qui in poi.

Una **variabile casuale** può assumere due o più valori possibili, ognuno con una certa probabilità positiva. I valori possibili sono elencati nel **set di esiti**.

Ogni volta che **campioni** una variabile casuale, estrai un valore particolare dal suo set di esiti secondo le probabilità definite.

Passiamo a un esempio semplice. Supponiamo una variabile X definita come segue:

* X ha il set di esiti {1,2}
* Pr [X = 1] = 0,5
* Pr [X = 2] = 0,5

È facile vedere che X è una variabile casuale. Primo, ci sono due o più valori possibili che X può assumere, cioè 1 e 2. Secondo, ogni valore possibile ha una probabilità positiva di verificarsi ogni volta che campioni X, cioè 0,5.

Tutto ciò che una variabile casuale richiede è un set di esiti con due o più possibilità, dove ogni possibilità ha una probabilità positiva di verificarsi al campionamento. In linea di principio, quindi, una variabile casuale può essere definita astrattamente, priva di qualsiasi contesto. In questo caso, potresti pensare al "campionamento" come all'esecuzione di un esperimento naturale per determinare il valore della variabile casuale.

La variabile X sopra è stata definita astrattamente. Potresti, quindi, pensare di campionare la variabile X sopra come lanciare una moneta equa e assegnare "2" in caso di testa e "1" in caso di croce. Per ogni campione di X, lanci di nuovo la moneta.

In alternativa, potresti anche pensare di campionare X, come lanciare un dado equo e assegnare "2" nel caso in cui il dado mostri 1, 3 o 4, e assegnare "1" nel caso in cui il dado mostri 2, 5 o 6. Ogni volta che campioni X, lanci di nuovo il dado.

Veramente, qualsiasi esperimento naturale che ti permetta di definire le probabilità dei valori possibili di X sopra può essere immaginato rispetto al disegno.
Spesso, tuttavia, le variabili casuali non sono introdotte in modo astratto. Invece, l'insieme dei possibili valori di esito ha un significato esplicito nel mondo reale (piuttosto che essere solo numeri). Inoltre, questi valori di esito potrebbero essere definiti rispetto a un tipo specifico di esperimento (piuttosto che come qualsiasi esperimento naturale con quei valori).
Consideriamo ora un esempio di variabile X che non è definita in modo astratto. X è definita come segue per determinare quale delle due squadre inizia una partita di calcio:

* X ha l'insieme di esiti {calcio d'inizio rosso, calcio d'inizio blu}
* Lancio di una moneta particolare C: croce = "calcio d'inizio rosso"; testa = "calcio d'inizio blu"
* Pr [X = calcio d'inizio rosso] = 0.5
* Pr [X = calcio d'inizio blu] = 0.5

In questo caso, l'insieme di esiti di X è fornito con un significato concreto, ovvero quale squadra inizia in una partita di calcio. Inoltre, i possibili esiti e le loro probabilità associate sono determinati da un esperimento concreto, ovvero il lancio di una moneta particolare C.

Nelle discussioni sulla crittografia, le variabili casuali sono solitamente introdotte rispetto a un insieme di esiti con un significato nel mondo reale. Potrebbe trattarsi dell'insieme di tutti i messaggi che potrebbero essere criptati, noto come spazio dei messaggi, o dell'insieme di tutte le chiavi che le parti che utilizzano la crittografia possono scegliere, noto come spazio delle chiavi.

Le variabili casuali nelle discussioni sulla crittografia, tuttavia, non sono solitamente definite rispetto a un esperimento naturale specifico, ma rispetto a qualsiasi esperimento che potrebbe produrre le giuste distribuzioni di probabilità.

Le variabili casuali possono avere distribuzioni di probabilità discrete o continue. Le variabili casuali con una **distribuzione di probabilità discreta**—cioè, variabili casuali discrete—hanno un numero finito di possibili esiti. La variabile casuale X negli esempi finora forniti era discreta.

Le **variabili casuali continue** possono invece assumere valori in uno o più intervalli. Si potrebbe dire, ad esempio, che una variabile casuale, al campionamento, assumerà qualsiasi valore reale tra 0 e 1, e che ogni numero reale in questo intervallo è ugualmente probabile. All'interno di questo intervallo, ci sono infiniti valori possibili.

Per le discussioni sulla crittografia, sarà necessario comprendere solo le variabili casuali discrete. Qualsiasi discussione sulle variabili casuali da qui in poi dovrebbe, quindi, essere intesa come riferita a variabili casuali discrete, a meno che non sia specificato diversamente.

### Rappresentazione grafica delle variabili casuali

I possibili valori e le probabilità associate per una variabile casuale possono essere facilmente visualizzati attraverso un grafico. Ad esempio, consideriamo la variabile casuale X dalla sezione precedente con un insieme di esiti di {1,2}, e Pr [X = 1] = 0.5 e Pr [X = 2] = 0.5. Tipicamente, visualizzeremmo una tale variabile casuale sotto forma di un grafico a barre come in *Figura 1*.

*Figura 1: Variabile casuale X*

![Figura 1: Variabile casuale X.](assets/Figure2-1.webp)

Le barre larghe in *Figura 1* ovviamente non intendono suggerire che la variabile casuale X sia effettivamente continua. Invece, le barre sono rese larghe per essere più visivamente accattivanti (solo una linea dritta verso l'alto fornisce una visualizzazione meno intuitiva).

### Variabili uniformi

Nell'espressione "variabile casuale", il termine "casuale" significa semplicemente "probabilistico". In altre parole, significa solo che due o più possibili esiti della variabile si verificano con certe probabilità. Questi esiti, tuttavia, non devono necessariamente essere ugualmente probabili (anche se il termine "casuale" può effettivamente avere quel significato in altri contesti).
Una **variabile uniforme** è un caso speciale di variabile casuale. Può assumere due o più valori tutti con la stessa probabilità. La variabile casuale X rappresentata nella *Figura 1* è chiaramente una variabile uniforme, poiché entrambi i possibili risultati si verificano con una probabilità di 0,5. Ci sono, tuttavia, molte variabili casuali che non sono esempi di variabili uniformi.
Considera, per esempio, la variabile casuale Y. Ha un insieme di risultati {1,2,3,8,10} e la seguente distribuzione di probabilità: Pr [Y = 1] = 0,25; Pr [Y = 2] = 0,35; Pr [Y = 3] = 0,1; Pr [Y = 8] = 0,25; Pr [Y = 10] = 0,05.

Sebbene due possibili risultati abbiano effettivamente una probabilità uguale di verificarsi, ovvero 1 e 8, Y può anche assumere certi valori con probabilità diverse da 0,25 durante il campionamento. Pertanto, mentre Y è effettivamente una variabile casuale, non è una variabile uniforme.

Una rappresentazione grafica di Y è fornita nella *Figura 2*.

*Figura 2: Variabile casuale Y*

![Figura 2: Variabile casuale Y.](assets/Figure2-2.webp "Figura 2: Variabile casuale Y")

Per un ultimo esempio, considera la variabile casuale Z. Ha l'insieme di risultati {1,3,7,11,12} e la seguente distribuzione di probabilità: Pr (2) = 0,2; Pr (3) = 0,2; Pr (9) = 0,2; Pr (11) = 0,2; Pr (12) = 0,2. Puoi vederla rappresentata nella Figura 3. La variabile casuale Z, a differenza di Y, è effettivamente una variabile uniforme, poiché tutte le probabilità per i possibili valori durante il campionamento sono uguali.

*Figura 3: Variabile casuale Z*

![Figura 3: Variabile casuale Z.](assets/Figure2-3.webp "Figura 3: Variabile casuale Z")

### Probabilità condizionata

Supponiamo che Bob intenda selezionare uniformemente un giorno dall'ultimo anno solare. Cosa dovremmo concludere essere la probabilità che il giorno selezionato sia in estate?

Finché pensiamo che il processo di Bob sarà davvero uniforme, dovremmo concludere che c'è una probabilità 1/4 che Bob selezioni un giorno d'estate. Questa è la **probabilità incondizionata** che il giorno selezionato casualmente sia in estate.

Supponiamo ora che, invece di estrarre uniformemente un giorno del calendario, Bob selezioni uniformemente solo tra quei giorni in cui la temperatura a mezzogiorno a Crystal Lake (New Jersey) era di 21 gradi Celsius o superiore. Data quest'ulteriore informazione, cosa possiamo concludere sulla probabilità che Bob selezioni un giorno d'estate?

Dovremmo davvero trarre una conclusione diversa da prima, anche senza ulteriori informazioni specifiche (ad esempio, la temperatura a mezzogiorno ogni giorno dell'ultimo anno solare).

Sapendo che Crystal Lake si trova nel New Jersey, certamente non ci aspetteremmo che la temperatura a mezzogiorno sia di 21 gradi Celsius o superiore in inverno. Invece, è molto più probabile che sia un giorno caldo in primavera o autunno, o un giorno in estate. Pertanto, sapendo che la temperatura a mezzogiorno a Crystal Lake nel giorno selezionato era di 21 gradi Celsius o superiore, la probabilità che il giorno selezionato da Bob sia in estate diventa molto più alta. Questa è la **probabilità condizionata** che il giorno selezionato casualmente sia in estate, dato che la temperatura a mezzogiorno a Crystal Lake era di 21 gradi Celsius o superiore.
A differenza dell'esempio precedente, le probabilità di due eventi possono anche essere completamente indipendenti. In tal caso, diciamo che sono **indipendenti**.
Supponiamo, ad esempio, che una certa moneta equa sia atterrata su testa. Dato questo fatto, qual è quindi la probabilità che domani piova? La probabilità condizionata in questo caso dovrebbe essere la stessa della probabilità incondizionata che domani piova, poiché il lancio di una moneta generalmente non ha alcun impatto sul tempo.

Usiamo un simbolo “|” per scrivere le affermazioni di probabilità condizionale. Ad esempio, la probabilità dell'evento A dato che l'evento B si è verificato può essere scritta come segue: Pr[A|B]. Quindi, quando due eventi, A e B, sono indipendenti, allora Pr[A|B] = Pr[A] e Pr[B|A] = Pr[B]. La condizione per l'indipendenza può essere semplificata come segue: Pr[A,B] = Pr[A]*Pr[B].

Un risultato chiave nella teoria della probabilità è noto come **Teorema di Bayes**. Esso afferma sostanzialmente che Pr[A|B] può essere riscritto come segue:

Pr[A|B] = (Pr[B|A] • Pr[A]) / Pr[B]

Invece di usare probabilità condizionali con eventi specifici, possiamo anche guardare alle probabilità condizionali coinvolte con due o più variabili casuali su un insieme di possibili eventi. Supponiamo due variabili casuali, X e Y. Possiamo denotare qualsiasi valore possibile per X con x, e qualsiasi valore possibile per Y con y. Potremmo dire, quindi, che due variabili casuali sono indipendenti se vale la seguente affermazione:

Pr[X = x,Y = y] = Pr[X = x] • Pr[Y = y] per tutti i valori di x e y

Siamo un po' più espliciti su cosa significa questa affermazione.

Supponiamo che gli insiemi di risultati per X e Y siano definiti come segue: **X** = {x<sub>1</sub>,x<sub>2</sub>,…,x<sub>i</sub>,…x<sub>n</sub>} e **Y** = {y<sub>1</sub>,y<sub>2</sub>,…,y<sub>i</sub>,…y<sub>m</sub>}. (È tipico indicare insiemi di valori con lettere maiuscole in grassetto.)

Ora supponiamo che tu campioni Y e osservi y<sub>1</sub>. L'affermazione sopra ci dice che la probabilità di ottenere ora x<sub>1</sub> campionando X è esattamente la stessa come se non avessimo mai osservato y<sub>1</sub>. Questo è vero per qualsiasi y<sub>i</sub> che avremmo potuto estrarre dal nostro campionamento iniziale di Y. Infine, questo vale non solo per x<sub>1</sub>. Per qualsiasi x<sub>i</sub> la probabilità di verificarsi non è influenzata dal risultato di un campionamento di Y. Tutto questo si applica anche al caso in cui X viene campionato per primo.

Concludiamo la nostra discussione su un punto leggermente più filosofico. In qualsiasi situazione reale, la probabilità di un certo evento è sempre valutata rispetto a un particolare insieme di informazioni. Non esiste una "probabilità incondizionata" in nessun senso molto stretto della parola.

Ad esempio, supponiamo che ti chiedessi la probabilità che i maiali voleranno entro il 2030. Anche se non ti do ulteriori informazioni, sai chiaramente molto sul mondo che può influenzare il tuo giudizio. Non hai mai visto maiali volare. Sai che la maggior parte delle persone non si aspetterà che volino. Sai che non sono davvero fatti per volare. E così via.
Quindi, quando parliamo di una "probabilità incondizionata" di un certo evento in un contesto reale, questo termine può davvero avere significato solo se lo interpretiamo come "la probabilità senza ulteriori informazioni esplicite". Qualsiasi comprensione di una "probabilità condizionata" dovrebbe, quindi, essere sempre intesa in relazione a un pezzo specifico di informazione.
Potrei, per esempio, chiedervi la probabilità che i maiali voleranno entro il 2030, dopo avervi fornito prove che alcune capre in Nuova Zelanda hanno imparato a volare dopo alcuni anni di addestramento. In questo caso, probabilmente aggiustereste il vostro giudizio sulla probabilità che i maiali voleranno entro il 2030. Quindi, la probabilità che i maiali voleranno entro il 2030 è condizionata da queste prove riguardanti le capre in Nuova Zelanda.

## L'operazione modulo
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

L'espressione più basilare con l'**operazione modulo** è della seguente forma: x mod y.

La variabile x è chiamata dividendo e la variabile y divisore. Per eseguire un'operazione modulo con un dividendo positivo e un divisore positivo, si determina semplicemente il resto della divisione.

Per esempio, considerate l'espressione 25 mod 4. Il numero 4 entra nel numero 25 un totale di 6 volte. Il resto di quella divisione è 1. Quindi, 25 mod 4 è uguale a 1. In modo simile, possiamo valutare le espressioni sottostanti:

* 29 mod 30 = 29 (poiché 30 entra in 29 un totale di 0 volte e il resto è 29)
* 42 mod 2 = 0 (poiché 2 entra in 42 un totale di 21 volte e il resto è 0)
* 12 mod 5 = 2 (poiché 5 entra in 12 un totale di 2 volte e il resto è 2)
* 20 mod 8 = 4 (poiché 8 entra in 20 un totale di 2 volte e il resto è 4)

Quando il dividendo o il divisore è negativo, le operazioni modulo possono essere gestite diversamente dai linguaggi di programmazione.

Vi imbatterete sicuramente in casi con un dividendo negativo in crittografia. In questi casi, l'approccio tipico è il seguente:

* Prima determinare il valore più vicino *inferiore o uguale* al dividendo in cui il divisore divide con un resto di zero. Chiamiamo quel valore p.
* Se il dividendo è x, allora il risultato dell'operazione modulo è il valore di x – p.

Per esempio, supponiamo che il dividendo sia – 20 e il divisore 3. Il valore più vicino inferiore o uguale a – 20 in cui 3 divide uniformemente è – 21. Il valore di x – p in questo caso è – 20 – – 21. Questo è uguale a 1 e, quindi, – 20 mod 3 è uguale a 1. In modo simile, possiamo valutare le espressioni sottostanti:

* – 8 mod 5 = 2
* – 19 mod 16 = 13
* – 14 mod 6 = 4

Per quanto riguarda la notazione, tipicamente vedrete i seguenti tipi di espressioni: x = [y mod z]. A causa delle parentesi, l'operazione modulo in questo caso si applica solo al lato destro dell'espressione. Se y è uguale a 25 e z è uguale a 4, per esempio, allora x si valuta a 1.
Senza parentesi, l'operazione di modulo agisce su *entrambi i lati* di un'espressione. Supponiamo, per esempio, la seguente espressione: x = y mod z. Se y è uguale a 25 e z è uguale a 4, allora tutto ciò che sappiamo è che x mod 4 si valuta in 1. Questo è coerente con qualsiasi valore di x dall'insieme {….– 7, – 3, 1, 5, 9….}. 
Il ramo della matematica che coinvolge operazioni di modulo su numeri ed espressioni è riferito come **aritmetica modulare**. Puoi pensare a questo ramo come l'aritmetica per casi nei quali la linea numerica non è infinitamente lunga. Anche se tipicamente incontriamo operazioni di modulo per interi (positivi) nella crittografia, puoi anche eseguire operazioni di modulo usando qualsiasi numero reale.

### Il cifrario di Cesare

L'operazione di modulo è frequentemente incontrata nella crittografia. Per illustrare, consideriamo uno degli schemi di cifratura storici più famosi: il cifrario di Cesare.

Definiamolo prima. Supponiamo un dizionario *D* che equipara tutte le lettere dell'alfabeto inglese, in ordine, con l'insieme di numeri {0,1,2…,25}. Assumiamo uno spazio dei messaggi **M**. Il **cifrario di Cesare** è, quindi, uno schema di cifratura definito come segue:

- Seleziona uniformemente una chiave k dallo spazio delle chiavi **K**, dove **K** = {0,1,2,…,25}<sup>[1](#footnote1)</sup>
- Cifra un messaggio m є **M**, come segue:
    - Separa m nelle sue singole lettere m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Converti ogni m<sub>i</sub> in un numero secondo *D*
    - Per ogni m<sub>i</sub>, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Converti ogni c<sub>i</sub> in una lettera secondo *D*
    - Poi combina c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub> per ottenere il testo cifrato c
- Decifra un testo cifrato c come segue:
    -- Converti ogni c<sub>i</sub> in un numero secondo *D*
    -- Per ogni c<sub>i</sub>, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    -- Converti ogni m<sub>i</sub> in una lettera secondo *D*
    -- Poi combina m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub> per ottenere il messaggio originale m

L'operatore modulo nel cifrario di Cesare assicura che le lettere si avvolgano, in modo che tutte le lettere del testo cifrato siano definite. Per illustrare, consideriamo l'applicazione del cifrario di Cesare sulla parola “DOG”.

Supponiamo che tu abbia selezionato uniformemente una chiave con il valore di 17. La lettera “O” equivale a 15. Senza l'operazione di modulo, l'addizione di questo numero di testo in chiaro con la chiave risulterebbe in un numero di testo cifrato di 32. Tuttavia, quel numero di testo cifrato non può essere trasformato in una lettera di testo cifrato, poiché l'alfabeto inglese ha solo 26 lettere. L'operazione di modulo assicura che il numero di testo cifrato sia in realtà 6 (il risultato di 32 mod 26), che equivale alla lettera di testo cifrato “G”.

L'intera cifratura della parola “DOG” con un valore di chiave di 17 è come segue:
* Messaggio = DOG = D,O,G = 3,15,6* c<sub>0</sub> = [(3 + 17) Mod 26] = [(20) Mod 26] = 20 = U
* c<sub>1</sub> = [(15 + 17) Mod 26] = [(32) Mod 26] = 6 = G
* c<sub>2</sub> = [(6 + 17) Mod 26] = [(23) Mod 26] = 23 = X
* c = UGX

Tutti possono intuitivamente comprendere come funziona il cifrario di Cesare e probabilmente usarlo da soli. Tuttavia, per avanzare nella conoscenza della crittografia, è importante iniziare a sentirsi più a proprio agio con la formalizzazione, poiché gli schemi diventeranno molto più complessi. Ecco perché i passaggi per il cifrario di Cesare sono stati formalizzati.

## L'operazione XOR
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Tutti i dati informatici vengono elaborati, memorizzati e inviati attraverso le reti a livello di bit. Anche gli schemi crittografici applicati ai dati informatici operano a livello di bit.

Ad esempio, supponiamo che tu abbia digitato un'e-mail nella tua applicazione di posta elettronica. Qualsiasi crittografia che applichi non avviene direttamente sui caratteri ASCII della tua e-mail. Invece, viene applicata alla rappresentazione in bit delle lettere e degli altri simboli nella tua e-mail.

Un'operazione matematica chiave da comprendere per la crittografia moderna, oltre all'operazione modulo, è quella dell'**operazione XOR**, o operazione di "o esclusivo". Questa operazione prende in input due bit e produce in output un altro bit. L'operazione XOR sarà semplicemente denotata come "XOR". Produce 0 se i due bit sono uguali e 1 se i due bit sono diversi. Puoi vedere le quattro possibilità qui sotto.

* 0 XOR 0 = 0
* 0 XOR 1 = 1
* 1 XOR 0 = 1
* 1 XOR 1 = 0

Puoi eseguire un'operazione XOR su due messaggi più lunghi di un singolo bit allineando i bit di quei due messaggi ed eseguendo l'operazione XOR su ogni coppia individuale di bit.

Per illustrare, supponiamo che tu abbia un messaggio m<sub>1</sub> (01111001) e un messaggio m<sub>2</sub> (01011001). L'operazione XOR di questi due messaggi può essere vista qui sotto.

* m<sub>1</sub> XOR m<sub>2</sub> = 01111001 XOR 01011001 = 00100000

Il processo è semplice. Prima esegui l'XOR dei bit più a sinistra di m<sub>1</sub> e m<sub>2</sub>. In questo caso è 0 XOR 0 = 0. Poi esegui l'XOR della seconda coppia di bit da sinistra. In questo caso è 1 XOR 1 = 0. Continui questo processo fino ad aver eseguito l'operazione XOR sui bit più a destra.
È facile vedere che l'operazione XOR è commutativa, ovvero che m<sub>1</sub> XOR m<sub>2</sub> = m<sub>2</sub> XOR m<sub>1</sub>. Inoltre, l'operazione XOR è anche associativa. Ciò significa che (m<sub>1</sub> XOR m<sub>2</sub>) XOR m<sub>3</sub> = m<sub>1</sub> XOR (m<sub>2</sub> XOR m<sub>3</sub>).
Un'operazione XOR su due stringhe di lunghezze alternative può avere interpretazioni diverse, a seconda del contesto. Qui non ci occuperemo di operazioni XOR su stringhe di lunghezze diverse.

Un'operazione XOR è equivalente al caso speciale di eseguire un'operazione modulo sull'addizione di bit quando il divisore è 2. Puoi vedere l'equivalenza nei seguenti risultati:

* (0 + 0) mod 2 = 0 XOR 0 = 0
* (1 + 0) mod 2 = 1 XOR 0 = 1
* (0 + 1) mod 2 = 0 XOR 1 = 1
* (1 + 1) mod 2 = 1 XOR 1 = 0

## Pseudocasualità
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Nella nostra discussione sulle variabili casuali e uniformi, abbiamo fatto una distinzione specifica tra "casuale" e "uniforme". Questa distinzione è tipicamente mantenuta nella pratica quando si descrivono le variabili casuali. Tuttavia, nel nostro contesto attuale, questa distinzione deve essere abbandonata e "casuale" e "uniforme" vengono usati sinonimamente. Spiegherò il motivo alla fine della sezione.

Per iniziare, possiamo definire una stringa binaria di lunghezza n **casuale** (o **uniforme**), se è stata il risultato del campionamento di una variabile uniforme S che dà a ogni stringa binaria di tale lunghezza n una probabilità uguale di selezione.

Supponiamo, per esempio, l'insieme di tutte le stringhe binarie di lunghezza 8: {0000 0000, 0000 0001,…, 1111 1111}. (È tipico scrivere una stringa di 8 bit in due quartetti, ciascuno chiamato **nibble**.) Chiamiamo questo insieme di stringhe **S<sub>8</sub>**.

Secondo la definizione sopra, possiamo quindi definire una particolare stringa binaria di lunghezza 8 casuale (o uniforme), se è stata il risultato del campionamento di una variabile uniforme S che dà a ogni stringa in **S<sub>8</sub>** una probabilità uguale di selezione. Dato che l'insieme **S<sub>8</sub>** include 2<sup>8</sup> elementi, la probabilità di selezione al campionamento dovrebbe essere 1/2<sup>8</sup> per ogni stringa nell'insieme.

Un aspetto chiave della casualità di una stringa binaria è che è definita in riferimento al processo tramite il quale è stata selezionata. La forma di una particolare stringa binaria di per sé, quindi, non rivela nulla sulla sua casualità nella selezione.

Per esempio, molte persone intuitivamente hanno l'idea che una stringa come 1111 1111 non potrebbe essere stata selezionata casualmente. Ma questo è chiaramente falso.
Definendo una variabile uniforme S su tutte le stringhe binarie di lunghezza 8, la probabilità di selezionare 1111 1111 dal set **S<sub>8</sub>** è la stessa di quella di una stringa come 0111 01001. Quindi, non si può dedurre nulla sulla casualità di una stringa, semplicemente analizzando la stringa stessa.
Possiamo anche parlare di stringhe casuali senza riferirci specificamente a stringhe binarie. Potremmo, per esempio, parlare di una stringa esadecimale casuale AF 02 82. In questo caso, la stringa sarebbe stata selezionata casualmente dal set di tutte le stringhe esadecimali di lunghezza 6. Questo è equivalente a selezionare casualmente una stringa binaria di lunghezza 24, poiché ogni cifra esadecimale rappresenta 4 bit.

Tipicamente l'espressione “una stringa casuale”, senza qualificazioni, si riferisce a una stringa selezionata casualmente dal set di tutte le stringhe della stessa lunghezza. Questo è come l'ho descritto sopra. Una stringa di lunghezza n può, ovviamente, essere anche selezionata casualmente da un set diverso. Uno, per esempio, che costituisce solo un sottoinsieme di tutte le stringhe di lunghezza n, o forse un set che include stringhe di lunghezza variabile. In questi casi, tuttavia, non ci riferiremmo ad essa come a “una stringa casuale”, ma piuttosto “una stringa che è selezionata casualmente da qualche set **S**”.

Un concetto chiave nella crittografia è quello della pseudocasualità. Una **stringa pseudocasuale** di lunghezza n appare *come se* fosse il risultato del campionamento di una variabile uniforme S che dà a ogni stringa in **S<sub>n</sub>** una probabilità uguale di selezione. In realtà, tuttavia, la stringa è il risultato del campionamento di una variabile uniforme S' che definisce solo una distribuzione di probabilità—non necessariamente una con probabilità uguali per tutti i possibili esiti—su un sottoinsieme di **S<sub>n</sub>**. Il punto cruciale qui è che nessuno può realmente distinguere tra campioni da S e S', anche se ne prendi molti.

Supponiamo, per esempio, una variabile casuale S. Il suo set di esiti è **S<sub>256</sub>**, questo è il set di tutte le stringhe binarie di lunghezza 256. Questo set ha 2<sup>256</sup> elementi. Ogni elemento ha una probabilità uguale di selezione, 1/2<sup>256</sup>, al momento del campionamento.

In aggiunta supponiamo una variabile casuale S’. Il suo set di esiti include solo 2<sup>128</sup> stringhe binarie di lunghezza 256. Ha una certa distribuzione di probabilità su quelle stringhe, ma questa distribuzione non è necessariamente uniforme.

Supponiamo che ora abbia preso migliaia di campioni da S e migliaia di campioni da S' e ti abbia dato i due set di esiti. Ti dico a quale variabile casuale è associato ciascun set di esiti. Successivamente, prendo un campione da una delle due variabili casuali. Ma questa volta non ti dico da quale variabile casuale ho preso il campione. Se S' fosse pseudocasuale, allora l'idea è che la tua probabilità di fare la scelta giusta su quale variabile casuale ho campionato è praticamente non migliore di 1/2.

Tipicamente, una stringa pseudocasuale di lunghezza n è prodotta selezionando casualmente una stringa di dimensione n – x, dove x è un intero positivo, e usandola come input per un algoritmo di espansione. Questa stringa casuale di dimensione n – x è nota come il **seme**.
Le stringhe pseudocasuali sono un concetto chiave per rendere la crittografia pratica. Consideriamo, ad esempio, i cifrari a flusso. Con un cifrario a flusso, una chiave selezionata casualmente viene inserita in un algoritmo espansionistico per produrre una stringa pseudocasuale molto più grande. Questa stringa pseudocasuale viene poi combinata con il testo in chiaro tramite un'operazione XOR per produrre un testo cifrato.
Se non fossimo in grado di produrre questo tipo di stringa pseudocasuale per un cifrario a flusso, allora avremmo bisogno di una chiave lunga quanto il messaggio per la sua sicurezza. Questa non è un'opzione molto pratica nella maggior parte dei casi.

La nozione di pseudocasualità discussa in questa sezione può essere definita più formalmente. Si estende anche ad altri contesti. Ma non è necessario approfondire questa discussione qui. Tutto ciò che veramente è necessario comprendere intuitivamente per gran parte della crittografia è la differenza tra una stringa casuale e una pseudocasuale.

Il motivo per cui si abbandona la distinzione tra "casuale" e "uniforme" nella nostra discussione dovrebbe ora essere chiaro. Nella pratica, tutti usano il termine pseudocasuale per indicare una stringa che appare **come se** fosse il risultato del campionamento di una variabile uniforme S. Parlando in modo rigoroso, dovremmo chiamare una tale stringa "pseudo-uniforme", adottando il nostro linguaggio da prima. Poiché il termine "pseudo-uniforme" è sia ingombrante che non utilizzato da nessuno, non lo introdurremo qui per chiarezza. Invece, semplicemente abbandoniamo la distinzione tra "casuale" e "uniforme" nel contesto attuale.

## Note

<chapterId>7cccd92c-15bc-5394-9024-af126988ecd7</chapterId>

[^1]: Possiamo definire esattamente questa affermazione, utilizzando la terminologia della sezione precedente. Lasciate che una variabile uniforme K abbia **K** come insieme di possibili risultati. Quindi Pr [K = 0] = 1/26, Pr [K = 1] = 1/26, e così via. Campionare la variabile uniforme K una volta per ottenere una chiave particolare [^1].

[^2]: Se interessati a un'esposizione più formale su questi argomenti, potete consultare l'*Introduzione alla Crittografia Moderna* di Katz e Lindell, specialmente il capitolo 3 [^2].

# Fondamenti Matematici della Crittografia II
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

Questo capitolo copre un argomento più avanzato sui fondamenti matematici della crittografia: la teoria dei numeri. Sebbene la teoria dei numeri sia importante per la crittografia simmetrica (come nel Cifrario di Rijndael), è particolarmente importante nell'ambito della crittografia a chiave pubblica.

Se trovate i dettagli della teoria dei numeri onerosi, vi consiglierei una lettura ad alto livello la prima volta. Potete sempre tornarci in un secondo momento.

## Cos'è la teoria dei numeri?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>

Potreste caratterizzare la **teoria dei numeri** come lo studio delle proprietà degli interi e delle funzioni matematiche che lavorano con gli interi.

Considerate, ad esempio, che due numeri a e N sono **coprimi** (o **primi relativi**) se il loro massimo comune divisore è uguale a 1. Supponiamo ora un particolare intero N. Quanti interi più piccoli di N sono coprimi con N? Possiamo fare affermazioni generali sulle risposte a questa domanda? Questi sono i tipi tipici di domande che la teoria dei numeri cerca di rispondere.
La teoria dei numeri moderna si basa sugli strumenti dell'algebra astratta. Il campo dell'**algebra astratta** è una sottodisciplina della matematica dove gli oggetti principali di analisi sono oggetti astratti noti come strutture algebriche. Una **struttura algebrica** è un insieme di elementi congiunti con una o più operazioni, che soddisfano certi assiomi. Attraverso le strutture algebriche i matematici possono ottenere intuizioni su specifici problemi matematici, astrattendosi dai loro dettagli.
Il campo dell'algebra astratta è talvolta chiamato anche algebra moderna. Potresti anche incontrare il concetto di **matematica astratta** (o **matematica pura**). Quest'ultimo termine non si riferisce all'algebra astratta, ma significa piuttosto lo studio della matematica per se stessa, e non solo con un occhio alle potenziali applicazioni.

Gli insiemi dell'algebra astratta possono trattare molti tipi di oggetti, dalle trasformazioni che preservano la forma su un triangolo equilatero ai modelli di carta da parati. Per la teoria dei numeri, consideriamo solo insiemi di elementi che contengono interi o funzioni che lavorano con interi.

## Gruppi
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Un concetto di base in matematica è quello di un insieme di elementi. Un insieme è solitamente denotato da segni di parentesi graffe con gli elementi separati da virgole.

Ad esempio, l'insieme di tutti gli interi è {…,-2,-1,0,1,2,…}. Le ellissi qui significano che un certo modello continua in una particolare direzione. Quindi l'insieme di tutti gli interi include anche 3,4,5,6 e così via, così come -3,-4,-5,-6 e così via. Questo insieme di tutti gli interi è tipicamente denotato da ℤ.

Un altro esempio di insieme è ℤ mod 11, o l'insieme di tutti gli interi modulo 11. A differenza dell'intero insieme ℤ, questo insieme contiene solo un numero finito di elementi, cioè {0,1,…,9,10}.

Un errore comune è pensare che l'insieme ℤ mod 11 sia in realtà {-10,-9,…,0,…,9,10}. Ma questo non è il caso, data la definizione dell'operazione modulo data in precedenza. Qualsiasi intero negativo ridotto in modulo 11 si avvolge su {0,1,…,9,10}. Ad esempio, l'espressione -2 mod 11 si avvolge a 9, mentre l'espressione -27 mod 11 si avvolge a 5.

Un altro concetto di base in matematica è quello di un'operazione binaria. Si tratta di qualsiasi operazione che prende due elementi per produrne un terzo. Ad esempio, dall'aritmetica e dall'algebra di base, sareste familiari con quattro operazioni binarie fondamentali: addizione, sottrazione, moltiplicazione e divisione.

Questi due concetti matematici di base, insiemi e operazioni binarie, sono utilizzati per definire la nozione di gruppo, la struttura più essenziale nell'algebra astratta.

Specificamente, supponiamo un'operazione binaria ◌. Inoltre, supponiamo un insieme di elementi **S** equipaggiato con tale operazione. Tutto ciò che "equipaggiato" significa qui è che l'operazione ◌ può essere eseguita tra qualsiasi coppia di elementi nell'insieme **S**.

La combinazione 〈**S**, ◌〉 è, quindi, un **gruppo** se soddisfa quattro condizioni specifiche, note come assiomi di gruppo.

1. Per qualsiasi a e b che sono elementi di **S**, a ◌ b è anche un elemento di **S**. Questo è noto come la **condizione di chiusura**.
2. Per qualsiasi a, b e c che sono elementi di **S**, vale che (a ◌ b) ◌ c = a ◌ (b ◌ c). Questo è noto come la **condizione di associatività**. 3. Esiste un unico elemento e in **S**, tale che per ogni elemento a in **S**, vale la seguente equazione: e ◌ a = a ◌ e = a. Poiché esiste un solo tale elemento e, viene chiamato **elemento neutro**. Questa condizione è nota come la **condizione di identità**.
4. Per ogni elemento a in **S**, esiste un elemento b in **S**, tale che vale la seguente equazione: a ◌ b = b ◌ a = e, dove e è l'elemento neutro. L'elemento b qui è noto come **elemento inverso**, ed è comunemente denotato come a<sup>-1</sup>. Questa condizione è nota come la **condizione di invertibilità**.

Esploriamo ulteriormente i gruppi. Denotiamo l'insieme di tutti gli interi con ℤ. Questo insieme combinato con l'addizione standard, o 〈ℤ, +〉, si adatta chiaramente alla definizione di un gruppo, poiché soddisfa i quattro assiomi sopra menzionati.

1. Per qualsiasi x e y che sono elementi di ℤ, x + y è anche un elemento di ℤ. Quindi 〈ℤ, +〉 soddisfa la condizione di chiusura.
2. Per qualsiasi x, y e z che sono elementi di ℤ, (x + y) + z = x + (y + z). Quindi 〈ℤ, +〉 soddisfa la condizione di associatività.
3. Esiste un elemento neutro in 〈ℤ, +〉, ovvero 0. Per qualsiasi x in ℤ, vale infatti che: 0 + x = x + 0 = x. Quindi 〈ℤ, +〉 soddisfa la condizione di identità.
4. Infine, per ogni elemento x in ℤ, esiste un y tale che x + y = y + x = 0. Se x fosse 10, per esempio, y sarebbe –10 (nel caso in cui x sia 0, anche y è 0). Quindi 〈ℤ, +〉 soddisfa la condizione di invertibilità.

Importante, il fatto che l'insieme degli interi con l'addizione costituisca un gruppo non significa che costituisca un gruppo con la moltiplicazione. Puoi verificarlo testando 〈ℤ, •〉 contro i quattro assiomi di gruppo (dove • indica la moltiplicazione standard).

I primi due assiomi sono ovviamente soddisfatti. Inoltre, sotto la moltiplicazione, l'elemento 1 può servire come elemento neutro. Qualsiasi intero x moltiplicato per 1, produce infatti x. Tuttavia, 〈ℤ, •〉 non soddisfa la condizione di invertibilità. Cioè, non esiste un elemento y unico in ℤ per ogni x in ℤ, tale che x • y = 1.

Per esempio, supponiamo che x = 22. Quale valore di y dell'insieme ℤ moltiplicato per x produrrebbe l'elemento neutro 1? Il valore di 1/22 funzionerebbe, ma questo non è nell'insieme ℤ. Infatti, si incontra questo problema per qualsiasi intero x, ad eccezione dei valori di 1 e -1 (dove y dovrebbe essere rispettivamente 1 e -1).
Se consentissimo l'uso dei numeri reali per il nostro insieme, allora i nostri problemi scomparirebbero in gran parte. Per ogni elemento x nell'insieme, la moltiplicazione per 1/x produce 1. Poiché le frazioni sono incluse nell'insieme dei numeri reali, si può trovare un inverso per ogni numero reale. L'eccezione è lo zero, poiché qualsiasi moltiplicazione con zero non produrrà mai l'elemento identità 1. Pertanto, l'insieme dei numeri reali non-zero dotato di moltiplicazione è effettivamente un gruppo.

Alcuni gruppi soddisfano una quinta condizione generale, nota come **condizione di commutatività**. Questa condizione è la seguente:

* Supponiamo un gruppo G con un insieme **S** e un operatore binario ◌. Supponiamo che a e b siano elementi di **S**. Se risulta che a ◌ b = b ◌ a per qualsiasi coppia di elementi a e b in **S**, allora G soddisfa la condizione di commutatività.

Qualsiasi gruppo che soddisfa la condizione di commutatività è noto come **gruppo commutativo**, o **gruppo Abeliano** (in onore di Niels Henrik Abel). È facile verificare che sia l'insieme dei numeri reali con l'addizione sia l'insieme degli interi con l'addizione sono gruppi Abeliani. L'insieme degli interi con la moltiplicazione non è affatto un gruppo, quindi a fortiori non può essere un gruppo Abeliano. Al contrario, l'insieme dei numeri reali non-zero con la moltiplicazione è anche un gruppo Abeliano.

Dovresti prestare attenzione a due importanti convenzioni sulla notazione. Primo, i segni “+” o “x” saranno frequentemente impiegati per simboleggiare operazioni di gruppo, anche quando gli elementi non sono, di fatto, numeri. In questi casi, non dovresti interpretare questi segni come l'addizione o la moltiplicazione aritmetica standard. Invece, sono operazioni con solo una somiglianza astratta a queste operazioni aritmetiche.

A meno che non ti stia riferendo specificamente all'addizione o alla moltiplicazione aritmetica, è più semplice usare simboli come ◌ e ◊ per le operazioni di gruppo, poiché questi non hanno connotazioni culturalmente radicate.

Secondo, per lo stesso motivo per cui i segni “+” e “x” sono spesso usati per indicare operazioni non aritmetiche, gli elementi identità dei gruppi sono frequentemente simbolizzati da “0” e “1”, anche quando gli elementi in questi gruppi non sono numeri. A meno che non ti stia riferendo all'elemento identità di un gruppo con numeri, è più semplice usare un simbolo più neutro come “e” per indicare l'elemento identità.

Molti insiemi di valori diversi e molto importanti in matematica dotati di certe operazioni binarie sono gruppi. Le applicazioni crittografiche, tuttavia, lavorano solo con insiemi di interi o almeno elementi che sono descritti da interi, ovvero, nel dominio della teoria dei numeri. Pertanto, insiemi con numeri reali diversi dagli interi non sono impiegati nelle applicazioni crittografiche.

Concludiamo fornendo un esempio di elementi che possono essere “descritti da interi”, anche se non sono interi. Un buon esempio sono i punti delle curve ellittiche. Sebbene qualsiasi punto su una curva ellittica non sia chiaramente un intero, tale punto è effettivamente descritto da due interi.

Le curve ellittiche sono, ad esempio, cruciali per Bitcoin. Qualsiasi coppia di chiavi private e pubbliche standard di Bitcoin è selezionata dall'insieme di punti definito dalla seguente curva ellittica: x^3 + 7 = y^2 mod 2^256 – 232 – 29 – 28 – 27 – 26 - 24 - 1 (il più grande numero primo minore di 2^256). La coordinata x è la chiave privata e la coordinata y è la tua chiave pubblica.
Le transazioni in Bitcoin coinvolgono tipicamente il blocco degli output verso una o più chiavi pubbliche in qualche modo. Il valore di queste transazioni può, quindi, essere sbloccato realizzando firme digitali con le corrispondenti chiavi private.

## Gruppi ciclici
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Una distinzione importante che possiamo fare è tra un **gruppo finito** e un **gruppo infinito**. Il primo ha un numero finito di elementi, mentre il secondo ha un numero infinito di elementi. Il numero di elementi in qualsiasi gruppo finito è noto come **ordine del gruppo**. Tutta la crittografia pratica che coinvolge l'uso di gruppi si basa su gruppi finiti (numerico-teorici).

Nella crittografia a chiave pubblica, una certa classe di gruppi abeliani finiti noti come gruppi ciclici sono particolarmente importanti. Per comprendere i gruppi ciclici, dobbiamo prima capire il concetto di esponenziazione degli elementi di un gruppo.

Supponiamo un gruppo G con un'operazione di gruppo ◌, e che a sia un elemento di G. L'espressione a<sup>n</sup> dovrebbe, quindi, essere interpretata come l'elemento a combinato con se stesso un totale di n - 1 volte. Per esempio, a<sup>2</sup> significa a ◌ a, a<sup>3</sup> significa a ◌ a ◌ a, e così via. (Nota che qui l'esponenziazione non è necessariamente l'esponenziazione nel senso aritmetico standard.)

Passiamo a un esempio. Supponiamo che G = 〈ℤ mod 7,+〉, e che il nostro valore per a sia 4. In questo caso, a<sup>2</sup> = [4 + 4 mod 7] = [8 mod 7] = 1 mod 7. Alternativamente, a<sup>4</sup> rappresenterebbe [4 + 4 + 4 + 4 mod 7] = [16 mod 7] = 2 mod 7.

Alcuni gruppi abeliani hanno uno o più elementi, che possono generare tutti gli altri elementi del gruppo attraverso l'esponenziazione continua. Questi elementi sono chiamati **generatori** o **elementi primitivi**.

Una classe importante di tali gruppi è 〈ℤ* mod N, •〉, dove N è un numero primo. La notazione ℤ* qui significa che il gruppo contiene tutti gli interi positivi non-zero minori di N. Un tale gruppo, quindi, ha sempre N - 1 elementi.

Consideriamo, per esempio, G = 〈ℤ* mod 11, •〉. Questo gruppo ha i seguenti elementi: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}. L'ordine di questo gruppo è 10 (che è effettivamente uguale a 11 - 1).

Esploriamo l'esponenziazione dell'elemento 2 da questo gruppo. I calcoli fino a 2<sup>12</sup> sono mostrati di seguito. Nota che sul lato sinistro dell'equazione, l'esponente si riferisce all'esponenziazione degli elementi del gruppo. Nel nostro esempio particolare, questo coinvolge effettivamente l'esponenziazione aritmetica sul lato destro dell'equazione (ma avrebbe potuto coinvolgere, per esempio, l'addizione). Per chiarire, ho scritto l'operazione ripetuta, piuttosto che la forma esponenziale sul lato destro.

* 2<sup>1</sup> = 2 mod 11
* 2<sup>2</sup> = 2 · 2 mod 11 = 4 mod 11
* 2<sup>3</sup> = 2 · 2 · 2 mod 11 = 8 mod 11
* 2<sup>4</sup> = 2 · 2 · 2 · 2 mod 11 = 16 mod 11 = 5 mod 11
* 2<sup>5</sup> = 2 · 2 · 2 · 2 · 2 mod 11 = 32 mod 11 = 10 mod 11
* 2<sup>6</sup> = 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 64 mod 11 = 9 mod 11
* 2<sup>7</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 128 mod 11 = 7 mod 11
* 2<sup>8</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 256 mod 11 = 3 mod 11
* 2<sup>9</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 512 mod 11 = 6 mod 11
* 2<sup>10</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 1024 mod 11 = 1 mod 11
* 2<sup>11</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 2048 mod 11 = 2 mod 11
* 2<sup>12</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 4096 mod 11 = 4 mod 11

Se si osserva attentamente, si può vedere che eseguendo l'elevamento a potenza sull'elemento 2 si cicla attraverso tutti gli elementi di 〈ℤ* mod 11, •〉 nell'ordine seguente: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Dopo 2<sup>10</sup>, l'elevamento a potenza continuato dell'elemento 2 cicla nuovamente attraverso tutti gli elementi e nello stesso ordine. Pertanto, l'elemento 2 è un generatore in 〈ℤ* mod 11, •〉.

Sebbene 〈ℤ* mod 11, •〉 abbia più generatori, non tutti gli elementi di questo gruppo sono generatori. Consideriamo, per esempio, l'elemento 3. Eseguendo le prime 10 potenze, senza mostrare i calcoli complicati, si ottengono i seguenti risultati:

* 3<sup>1</sup> = 3 mod 11
* 3<sup>2</sup> = 9 mod 11
* 3<sup>3</sup> = 5 mod 11
* 3<sup>4</sup> = 4 mod 11
* 3<sup>5</sup> = 1 mod 11
* 3<sup>6</sup> = 3 mod 11
* 3<sup>7</sup> = 9 mod 11
* 3<sup>8</sup> = 5 mod 11
* 3<sup>9</sup> = 4 mod 11
* 3<sup>10</sup> = 1 mod 11

Invece di ciclare attraverso tutti i valori in 〈ℤ* mod 11, •〉, l'esponenziazione dell'elemento 3 porta solo a un sottoinsieme di quei valori: 3, 9, 5, 4 e 1. Dopo la quinta esponenziazione, questi valori iniziano a ripetersi.

Ora possiamo definire un **gruppo ciclico** come qualsiasi gruppo con almeno un generatore. Ovvero, esiste almeno un elemento del gruppo dal quale puoi produrre tutti gli altri elementi del gruppo attraverso l'esponenziazione.

Potresti aver notato nel nostro esempio sopra che sia 2<sup>10</sup> che 3<sup>10</sup> sono uguali a 1 mod 11. Infatti, anche se non eseguiremo i calcoli, l'esponenziazione per 10 di qualsiasi elemento nel gruppo 〈ℤ* mod 11, •〉 produrrà 1 mod 11. Perché è così?

Questa è una domanda importante, ma richiede un po' di lavoro per rispondere.

Per iniziare, supponiamo due interi positivi a e N. Un importante teorema in teoria dei numeri afferma che a ha un inverso moltiplicativo modulo N (cioè, un intero b tale che a • b = 1 mod N) se e solo se il massimo comune divisore tra a e N è uguale a 1. Ovvero, se a e N sono coprimi.

Quindi, per qualsiasi gruppo di interi dotato di moltiplicazione modulo N solo i coprimi più piccoli con N sono inclusi nel set. Possiamo denotare questo insieme con ℤ<sup>c</sup> mod N.

Ad esempio, supponiamo che N sia 10. Solo gli interi 1, 3, 7 e 9 sono coprimi con 10. Quindi l'insieme ℤ<sup>c</sup> mod 10 include solo {1, 3, 7, 9}. Non puoi creare un gruppo con moltiplicazione intera modulo 10 usando altri interi tra 1 e 10. Per questo particolare gruppo, gli inversi sono le coppie 1 e 9, e 3 e 7.

Nel caso in cui N stesso sia primo, tutti gli interi da 1 a N – 1 sono coprimi con N. Un tale gruppo, quindi, ha un ordine di N – 1. Usando la nostra notazione precedente, ℤ<sup>c</sup> mod N è uguale a ℤ* mod N quando N è primo. Il gruppo che abbiamo selezionato per il nostro esempio precedente, 〈ℤ* mod 11, •〉, è un particolare esempio di questa classe di gruppi.

Successivamente, la funzione φ(N) calcola il numero di coprimi fino a un numero N, ed è conosciuta come **Funzione Phi di Eulero**.<sup>[1](#footnote1)</sup> Secondo il **Teorema di Eulero**, ogni volta che due interi a e N sono coprimi, vale quanto segue:

* a<sup>φ(N)</sup> mod N = 1 mod N
Questa ha un'importante implicazione per la classe di gruppi 〈ℤ* mod N, •〉 dove N è primo. Per questi gruppi, l'esponenziazione degli elementi del gruppo rappresenta l'esponenziazione aritmetica. Ovvero, a<sup>φ(N)</sup> mod N rappresenta l'operazione aritmetica a<sup>φ(N)</sup> mod N. Poiché ogni elemento a in questi gruppi moltiplicativi è coprimo con N, significa che a<sup>φ(N)</sup> mod N = a<sup>N – 1</sup> mod N = 1 mod N.
Il teorema di Eulero è un risultato davvero importante. Per iniziare, implica che tutti gli elementi in 〈ℤ* mod N, •〉 possono solo ciclare attraverso un numero di valori tramite esponenziazione che si divide in N – 1. Nel caso di 〈ℤ* mod 11, •〉, ciò significa che ogni elemento può solo ciclare attraverso 2, 5, o 10 elementi. I valori di gruppo attraverso i quali un elemento cicla mediante esponenziazione sono noti come **ordine dell'elemento**. Un elemento con un ordine equivalente all'ordine di un gruppo è un generatore.

Inoltre, il teorema di Eulero implica che possiamo sempre conoscere il risultato di a<sup>N – 1</sup> mod N per qualsiasi gruppo 〈ℤ* mod N, •〉 dove N è primo. Questo vale indipendentemente da quanto possano essere complessi i calcoli effettivi.

Per esempio, supponiamo che il nostro gruppo sia ℤ* mod 160,481,182 (dove 160,481,182 è effettivamente un numero primo). Sappiamo che tutti gli interi da 1 a 160,481,181 devono essere elementi di questo gruppo, e che φ(n) = 160,481,181. Anche se non possiamo eseguire tutti i passaggi nei calcoli, sappiamo che espressioni come 514<sup>160,481,181</sup>, 2,005<sup>160,481,181</sup>, e 256,212<sup>160,481,181</sup> devono tutte valutare a 1 mod 160,481,182.

## Campi
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Un gruppo è la struttura algebrica di base in algebra astratta, ma ce ne sono molte altre. L'unica altra struttura algebrica di cui devi essere a conoscenza è quella di un campo, specificamente quella di un campo finito. Questo tipo di struttura algebrica è frequentemente utilizzato in crittografia, come nello Standard di Crittografia Avanzata. Quest'ultimo è il principale schema di crittografia simmetrica che incontrerai nella pratica.

Un campo deriva dalla nozione di un gruppo. Specificamente, un **campo** è un insieme di elementi **S** dotato di due operatori binari ◌ e ◊, che soddisfa le seguenti condizioni:

1. L'insieme **S** dotato di ◌ è un gruppo Abeliano.
2. L'insieme **S** dotato di ◊ è un gruppo Abeliano per gli elementi "non-zero".
3. L'insieme **S** dotato dei due operatori soddisfa quella che è nota come la condizione distributiva: Supponiamo che a, b e c siano elementi di **S**. Allora **S** dotato dei due operatori soddisfa la proprietà distributiva quando a ◌ (b ◊ c) = a ◌ b ◊ a ◌ c.
Si noti che, come per i gruppi, la definizione di un campo è molto astratta. Non fa affermazioni sui tipi di elementi in **S**, o sulle operazioni ◌ e ◊. Afferma semplicemente che un campo è qualsiasi insieme di elementi con due operazioni per le quali valgono le tre condizioni sopra menzionate. (L'elemento "zero" nel secondo gruppo Abeliano può essere interpretato in modo astratto.)
Quindi, quale potrebbe essere un esempio di campo? Un buon esempio è l'insieme ℤ mod 7, o {0,1,…,7} definito sulla somma standard (al posto di ◌ sopra) e sulla moltiplicazione standard (al posto di ◊ sopra).

Primo, ℤ mod 7 soddisfa la condizione per essere un gruppo Abeliano rispetto all'addizione, e soddisfa la condizione per essere un gruppo Abeliano rispetto alla moltiplicazione se si considerano solo gli elementi non-zero. Secondo, la combinazione dell'insieme con i due operatori soddisfa la condizione distributiva.

È didatticamente utile esplorare queste affermazioni utilizzando alcuni valori particolari. Prendiamo i valori sperimentali 5, 2 e 3, alcuni elementi selezionati casualmente dall'insieme ℤ mod 7, per ispezionare il campo 〈ℤ mod 7, +, •〉. Useremo questi tre valori nell'ordine, come necessario per esplorare condizioni particolari.

Esploriamo prima se ℤ mod 7 equipaggiato con l'addizione è un gruppo Abeliano.

1. Condizione di chiusura: Prendiamo 5 e 2 come nostri valori. In tal caso, [5 + 2] mod 7 = 7 mod 7 = 0. Questo è effettivamente un elemento di ℤ mod 7, quindi il risultato è coerente con la condizione di chiusura.
2. Condizione di associatività: Prendiamo 5, 2 e 3 come nostri valori. In tal caso, [(5 + 2) + 3] mod 7 = [5 + (2 + 3)] mod 7 = 10 mod 7 = 3. Questo è coerente con la condizione di associatività.
3. Condizione di identità: Prendiamo 5 come nostro valore. In tal caso, [5 + 0] mod 7 = [0 + 5] mod 7 = 5. Quindi 0 sembra essere l'elemento identità per l'addizione.
4. Condizione di inverso: Consideriamo l'inverso di 5. Deve essere il caso che [5 + d] mod 7 = 0, per qualche valore di d. In questo caso, l'unico valore da ℤ mod 7 che soddisfa questa condizione è 2.
5. Condizione di commutatività: Prendiamo 5 e 3 come nostri valori. In tal caso, [5 + 3] mod 7 = [3 + 5] mod 7 = 1. Questo è coerente con la condizione di commutatività.

L'insieme ℤ mod 7 equipaggiato con l'addizione appare chiaramente essere un gruppo Abeliano. Esploriamo ora se ℤ mod 7 equipaggiato con la moltiplicazione è un gruppo Abeliano per tutti gli elementi non-zero.

1. Condizione di chiusura: Prendiamo 5 e 2 come nostri valori. In tal caso, [5 • 2] mod 7 = 10 mod 7 = 3. Anche questo è un elemento di ℤ mod 7, quindi il risultato è coerente con la condizione di chiusura.
2. Condizione di associatività: Prendiamo come nostri valori 5, 2 e 3. In questo caso, [(5 • 2) • 3] mod 7 = [5 • (2 • 3)] mod 7 = 30 mod 7 = 2. Questo è coerente con la condizione di associatività.
3. Condizione di identità: Prendiamo 5 come nostro valore. In questo caso, [5 • 1] mod 7 = [1 • 5] mod 7 = 5. Quindi 1 sembra essere l'elemento identità per la moltiplicazione.
4. Condizione di inverso: Consideriamo l'inverso di 5. Deve verificarsi che [5 • d] mod 7 = 1, per qualche valore di d. Il valore unico da ℤ mod 7 che soddisfa questa condizione è 3. Questo è coerente con la condizione di inverso.
5. Condizione di commutatività: Prendiamo 5 e 3 come nostri valori. In questo caso, [5 • 3] mod 7 = [3 • 5] mod 7 = 15 mod 7 = 1. Questo è coerente con la condizione di commutatività.

L'insieme ℤ mod 7 sembra chiaramente soddisfare le regole per essere un gruppo Abeliano quando congiunto sia con l'addizione che con la moltiplicazione sugli elementi non nulli.

Infine, questo insieme combinato con entrambi gli operatori sembra soddisfare la condizione distributiva. Prendiamo come nostri valori 5, 2 e 3. Possiamo vedere che [5 • (2 + 3)] mod 7 = [5 • 2 + 5 • 3] mod 7 = 25 mod 7 = 4.

Abbiamo ora visto che ℤ mod 7 equipaggiato con addizione e moltiplicazione soddisfa gli assiomi per un campo finito quando testato con valori particolari. Naturalmente possiamo anche dimostrare che generalmente, ma non lo faremo qui.

Una distinzione chiave è tra due tipi di campi: campi finiti e campi infiniti.

Un **campo infinito** coinvolge un campo dove l'insieme **S** è infinitamente grande. L'insieme dei numeri reali ℝ equipaggiato con addizione e moltiplicazione è un esempio di campo infinito. Un **campo finito**, noto anche come **campo di Galois**, è un campo dove l'insieme **S** è finito. Il nostro esempio sopra di 〈ℤ mod 7, +, •〉 è un campo finito.

In crittografia, siamo principalmente interessati ai campi finiti. Generalmente, si può dimostrare che un campo finito esiste per qualche insieme di elementi **S** se e solo se ha p<sup>m</sup> elementi, dove p è un numero primo e m un intero positivo maggiore o uguale a uno. In altre parole, se l'ordine di qualche insieme **S** è un numero primo (p<sup>m</sup> dove m = 1) o una potenza di primo (p<sup>m</sup> dove m > 1), allora puoi trovare due operatori ◌ e ◊ tali che le condizioni per un campo siano soddisfatte.

Se qualche campo finito ha un numero primo di elementi, allora è chiamato **campo primo**. Se il numero di elementi nel campo finito è una potenza di primo, allora il campo è chiamato **campo esteso**. In crittografia, siamo interessati sia ai campi primi che ai campi estesi.
I principali campi di interesse in crittografia sono quelli in cui l'insieme di tutti gli interi è modulato da un numero primo, e gli operatori sono l'addizione e la moltiplicazione standard. Questa classe di campi finiti includerebbe ℤ mod 2, ℤ mod 3, ℤ mod 5, ℤ mod 7, ℤ mod 11, ℤ mod 13, e così via. Per qualsiasi campo primo ℤ mod p, l'insieme degli interi del campo è il seguente: {0,1,….,p – 2, p – 1}.
In crittografia siamo anche interessati ai campi di estensione, in particolare a qualsiasi campo con 2<sup>m</sup> elementi dove m > 1. Tali campi finiti sono, ad esempio, utilizzati nel Cifrario Rijndael, che costituisce la base dello Standard di Crittografia Avanzata. Mentre i campi primi sono relativamente intuitivi, questi campi di estensione di base 2 probabilmente non lo sono per chiunque non sia familiare con l'algebra astratta.

Per iniziare, è effettivamente vero che qualsiasi insieme di interi con 2<sup>m</sup> elementi può essere assegnato a due operatori che farebbero della loro combinazione un campo (purché m sia un intero positivo). Tuttavia, il fatto che un campo esista non significa necessariamente che sia facile da scoprire o particolarmente pratico per certe applicazioni.

Si scopre che, in particolare, i campi di estensione applicabili di 2<sup>m</sup> in crittografia sono quelli definiti su particolari insiemi di espressioni polinomiali, piuttosto che su qualche insieme di interi.

Ad esempio, supponiamo che volessimo un campo di estensione con 2<sup>3</sup> (cioè, 8) elementi nell'insieme. Sebbene ci possano essere molti insiemi diversi che possono essere utilizzati per campi di quella dimensione, un tale insieme include tutti i polinomi unici della forma a<sub>2</sub>x<sup>2</sup> + a<sub>1</sub>x + a<sub>0</sub>, dove ogni coefficiente a<sub>i</sub> è o 0 o 1. Pertanto, questo insieme **S** include i seguenti elementi:

1. 0: Il caso in cui a<sub>2</sub> = 0, a<sub>1</sub> = 0, e a<sub>0</sub> = 0.
2. 1: Il caso in cui a<sub>2</sub> = 0, a<sub>1</sub> = 0, e a<sub>0</sub> = 1.
3. x: Il caso in cui a<sub>2</sub> = 0, a<sub>1</sub> = 1, e a<sub>0</sub> = 0.
4. x + 1: Il caso in cui a<sub>2</sub> = 0, a<sub>1</sub> = 1, e a<sub>0</sub> = 1.
5. x<sup>2</sup>: Il caso in cui a<sub>2</sub>= 1, a<sub>1</sub> = 0, e a<sub>0</sub> = 0.
6. x<sup>2</sup> + 1: Il caso in cui a<sub>2</sub> = 1, a<sub>1</sub> = 0, e a<sub>0</sub> = 1.
7. \(x^2 + x\): Il caso in cui \(a_2 = 1\), \(a_1 = 1\) e \(a_0 = 0\). 8. \(x^2 + x + 1\): Il caso in cui \(a_2 = 1\), \(a_1 = 1\) e \(a_0 = 1\).

Quindi **S** sarebbe l'insieme \(\{0,1,x,x + 1, x^2,x^2 + 1, x^2 + x, x^2 + x + 1\}\). Quali due operazioni possono essere definite su questo insieme di elementi per garantire che la loro combinazione sia un campo?

La prima operazione sull'insieme S (◌) può essere definita come l'addizione standard di polinomi modulo 2. Tutto ciò che devi fare è sommare i polinomi come faresti normalmente, e poi applicare il modulo 2 a ciascuno dei coefficienti del polinomio risultante. Ecco alcuni esempi:

* \([(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1\)
* \([(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2\)
* \([(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1\)

La seconda operazione sull'insieme S (◌) necessaria per creare il campo è più complicata. Si tratta di una sorta di moltiplicazione, ma non la moltiplicazione standard dell'aritmetica. Invece, devi vedere ogni elemento come un vettore e comprendere l'operazione come la moltiplicazione di quei due vettori modulo un polinomio irriducibile.

Passiamo ora all'idea di un polinomio irriducibile. Un **polinomio irriducibile** è uno che non può essere fattorizzato (proprio come un numero primo non può essere fattorizzato in componenti diversi da 1 e il numero primo stesso). Ai nostri fini, siamo interessati ai polinomi che sono irriducibili rispetto all'insieme di tutti gli interi. (Nota che potresti essere in grado di fattorizzare certi polinomi, per esempio, con i numeri reali o complessi, anche se non puoi fattorizzarli usando gli interi).

Per esempio, considera il polinomio \(x^2 - 3x + 2\). Questo può essere riscritto come \((x – 1)(x – 2)\). Quindi, questo non è irriducibile. Ora considera il polinomio \(x^2 + 1\). Usando solo interi, non c'è modo di fattorizzare ulteriormente questa espressione. Quindi, questo è un polinomio irriducibile rispetto agli interi.
Ora, passiamo al concetto di moltiplicazione vettoriale. Non esploreremo questo argomento in profondità, è sufficiente che tu comprenda una regola di base: la divisione tra vettori può avvenire purché il dividendo abbia un grado superiore o uguale a quello del divisore. Se il dividendo ha un grado inferiore a quello del divisore, allora non può più essere diviso per il divisore.
Ad esempio, considera l'espressione x<sup>6</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Questa si riduce ulteriormente poiché il grado del dividendo, 6, è superiore al grado del divisore, 5. Ora considera l'espressione x<sup>5</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Anche questa si riduce ulteriormente, poiché il grado del dividendo, 5, e del divisore, 5, sono uguali.

Tuttavia, ora considera l'espressione x<sup>4</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Questa non si riduce ulteriormente, poiché il grado del dividendo, 4, è inferiore al grado del divisore, 5.

Sulla base di queste informazioni, siamo ora pronti a trovare la nostra seconda operazione per l'insieme {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1}.

Ho già detto che la seconda operazione dovrebbe essere intesa come moltiplicazione vettoriale modulo un certo polinomio irriducibile. Questo polinomio irriducibile dovrebbe garantire che la seconda operazione definisca un gruppo Abeliano su **S** ed è coerente con la condizione distributiva. Quindi, quale dovrebbe essere questo polinomio irriducibile?

Poiché tutti i vettori nell'insieme sono di grado 2 o inferiore, il polinomio irriducibile dovrebbe essere di grado 3. Se una qualsiasi moltiplicazione di due vettori nell'insieme produce un polinomio di grado 3 o superiore, sappiamo che il modulo di un polinomio di grado 3 produce sempre un polinomio di grado 2 o inferiore. Questo accade perché qualsiasi polinomio di grado 3 o superiore è sempre divisibile per un polinomio di grado 3. Inoltre, il polinomio che funge da divisore deve essere irriducibile.

Si scopre che ci sono diversi polinomi irriducibili di grado 3 che potremmo usare come nostro divisore. Ognuno di questi polinomi definisce un campo diverso in congiunzione con il nostro insieme S e l'addizione modulo 2. Questo significa che hai molteplici opzioni quando utilizzi i campi di estensione 2<sup>m</sup> in crittografia.

Per il nostro esempio, supponiamo di selezionare il polinomio x<sup>3</sup> + x + 1. Questo è effettivamente irriducibile, perché non puoi fattorizzarlo usando numeri interi. Inoltre, garantirà che qualsiasi moltiplicazione di due elementi produrrà un polinomio di grado 2 o inferiore.
Lavoriamo attraverso un esempio della seconda operazione usando il polinomio x^3 + x + 1 come divisore per illustrare come funziona. Supponiamo che tu moltiplichi gli elementi x^2 + 1 con x^2 + x nel nostro insieme **S**. Dobbiamo quindi calcolare l'espressione [(x^2 + 1) • (x^2 + x)] mod x^3 + x + 1. Questo può essere semplificato come segue:
* [(x^2 + 1) • (x^2 + x)] mod x^3 + x + 1 =
* [x^2 • x^2 + x^2 • x + 1 • x^2 + 1 • x] mod x^3 + x + 1 = 
* [x^4 + x^3 + x^2 + x] mod x^3 + x + 1
    
Sappiamo che [x^4 + x^3 + x^2 + x] mod x^3 + x + 1 può essere ridotto poiché il dividendo ha un grado superiore (4) rispetto al divisore (3).

Per iniziare, puoi vedere che l'espressione x^3 + x + 1 va in x^4 + x^3 + x^2 + x un totale di x volte. Puoi verificarlo moltiplicando x^3 + x + 1 per x, che è x^4 + x^2 + x. Poiché quest'ultimo termine ha lo stesso grado del dividendo, cioè 4, sappiamo che questo funziona. Puoi calcolare il resto di questa divisione per x come segue:

* [(x^4 + x^3 + x^2 + x) – (x^4 + x^2 + x)] mod x^3 + x + 1 = 
* [x^3] mod x^3 + x + 1 =
* x^3

Quindi, dopo aver diviso x^4 + x^3 + x^2 + x per x^3 + x + 1 un totale di x volte, abbiamo un resto di x^3. Questo può essere ulteriormente diviso per x^3 + x + 1?
Intuitivamente, potrebbe sembrare logico dire che \(x^3\) non può più essere diviso per \(x^3 + x + 1\), poiché il secondo termine sembra più grande. Tuttavia, ricordiamo la nostra discussione sulla divisione vettoriale di prima. Finché il dividendo ha un grado maggiore o uguale al divisore, l'espressione può essere ulteriormente ridotta. Specificamente, l'espressione \(x^3 + x + 1\) può entrare in \(x^3\) esattamente 1 volta. Il resto viene calcolato come segue:
\[\left[(x^3) – (x^3 + x + 1)\right] \mod x^3 + x + 1 = 
[x + 1] \mod x^3 + x + 1 = 
x + 1\]

Potresti chiederti perché \((x^3) – (x^3 + x + 1)\) si valuta in \(x + 1\) e non in \(- x – 1\). Ricorda che la prima operazione del nostro campo è definita modulo 2. Pertanto, la sottrazione di due vettori produce esattamente lo stesso risultato dell'addizione di due vettori.

Per riassumere la moltiplicazione di \(x^2 + 1\) e \(x^2 + x\): Quando moltiplichi questi due termini ottieni un polinomio di grado 4, \(x^4 + x^3 + x^2 + x\), che deve essere ridotto modulo \(x^3 + x + 1\). Il polinomio di grado 4 è divisibile per \(x^3 + x + 1\) esattamente \(x + 1\) volte. Il resto dopo aver diviso \(x^4 + x^3 + x^2 + x\) per \(x^3 + x + 1\) esattamente \(x + 1\) volte è \(x + 1\). Questo è effettivamente un elemento nel nostro insieme \(\{0,1,x,x + 1,x^2,x^2 + 1,x^2 + x,x^2 + x + 1\}\).

Perché i campi di estensione con base 2 su insiemi di polinomi, come nell'esempio sopra, sono utili per la crittografia? Il motivo è che puoi considerare i coefficienti nei polinomi di tali insiemi, 0 o 1, come elementi di stringhe binarie di una certa lunghezza. L'insieme **S** nel nostro esempio sopra, ad esempio, potrebbe essere invece visto come un insieme S che include tutte le stringhe binarie di lunghezza 3 (da 000 a 111). Le operazioni su **S**, quindi, possono anche essere utilizzate per eseguire operazioni su queste stringhe binarie e produrre una stringa binaria della stessa lunghezza.

## Algebra astratta nella pratica
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>
Nonostante il linguaggio formale e l'astrattezza della discussione, il concetto di gruppo non dovrebbe essere troppo difficile da comprendere. Si tratta semplicemente di un insieme di elementi insieme a un'operazione binaria, dove l'esecuzione di tale operazione binaria su quegli elementi soddisfa quattro condizioni generali. Un gruppo Abeliano ha semplicemente una condizione in più nota come commutatività. Un gruppo ciclico, a sua volta, è un tipo speciale di gruppo Abeliano, ovvero uno che ha un generatore. Un campo è semplicemente una costruzione più complessa basata sulla nozione di base di gruppo.
Ma se sei una persona praticamente incline, potresti chiederti a questo punto: A chi importa? Sapere che un certo insieme di elementi con un operatore è un gruppo, o addirittura un gruppo Abeliano o ciclico, ha qualche rilevanza nel mondo reale? Sapere che qualcosa è un campo?

Senza addentrarci troppo nei dettagli, la risposta è "sì". I gruppi sono stati creati per la prima volta nel XIX secolo dal matematico francese Evariste Galois. Li ha usati per trarre conclusioni sulla risoluzione delle equazioni polinomiali di grado superiore a cinque.

Da allora il concetto di gruppo ha aiutato a far luce su numerosi problemi in matematica e altrove. Sulla loro base, ad esempio, il fisico Murray-Gellman è stato in grado di prevedere l'esistenza di una particella prima che fosse effettivamente osservata negli esperimenti.<sup>[3](#footnote3)</sup> Per un altro esempio, i chimici utilizzano la teoria dei gruppi per classificare le forme delle molecole. I matematici hanno persino utilizzato il concetto di gruppo per trarre conclusioni su qualcosa di così concreto come la carta da parati!

Essenzialmente, mostrare che un insieme di elementi con un certo operatore è un gruppo, significa che ciò che si sta descrivendo ha una particolare simmetria. Non una simmetria nel senso comune della parola, ma in una forma più astratta. E questo può fornire intuizioni sostanziali su sistemi e problemi particolari. Le nozioni più complesse dell'algebra astratta ci danno semplicemente informazioni aggiuntive.

Più importantemente, vedrai l'importanza dei gruppi e dei campi teorici dei numeri nella pratica attraverso la loro applicazione nella crittografia, in particolare nella crittografia a chiave pubblica. Abbiamo già visto nella nostra discussione sui campi, ad esempio, come i campi di estensione sono impiegati nel Cifrario di Rijndael. Elaboreremo quell'esempio nel *Capitolo 5*.

## Ulteriori esplorazioni
<chapterId>ab51038d-82bd-5c5d-a759-276cfbf7fbce</chapterId>

Per ulteriori discussioni sull'algebra astratta, consiglierei l'eccellente serie di video sull'algebra astratta di Socratica.<sup>[4](#footnote4)</sup> Raccomanderei in particolare i seguenti video: "Cos'è l'algebra astratta?", "Definizione di gruppo (espansa)", "Definizione di anello (espansa)" e "Definizione di campo (espansa)". Questi quattro video ti daranno ulteriori intuizioni su gran parte della discussione sopra. (Non abbiamo discusso degli anelli, ma un campo è solo un tipo speciale di anello.)

Per ulteriori discussioni sulla teoria dei numeri moderna, puoi consultare molte discussioni avanzate sulla crittografia. Come suggerimenti, offrirei l'Introduzione alla Crittografia Moderna di Jonathan Katz e Yehuda Lindell o la Comprensione della Crittografia di Christof Paar e Jan Pelzl per ulteriori discussioni.<sup>[5](#footnote5)</sup>
[^1]: La funzione opera come segue. Ogni intero N può essere fattorizzato in un prodotto di primi. Supponiamo che un particolare N sia fattorizzato come segue: p<sub>1</sub><sup>e1</sup> • p<sub>2</sub><sup>e2</sup> …. • p<sub>m</sub><sup>em</sup> dove tutti i p sono numeri primi e tutti gli e sono interi maggiori o uguali a 1. Allora, φ(N) = Somma<sub>i=1…m</sub>[p<sub>i</sub><sup>ei</sup> – p<sub>i</sub><sup>ei - 1</sup>] [^1].

[^2]: I campi estesi diventano molto controintuitivi. Invece di avere elementi di interi, hanno insiemi di polinomi. Inoltre, qualsiasi operazione viene eseguita modulo qualche polinomio irriducibile [^2].

[^3]: Vedi [Video YouTube](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be) [^3].

[^4]: Socratica, [Algebra Astratta](https://www.socratica.com/subject/abstract-algebra) [^4].

[^5]: Katz e Lindell, *Introduzione alla Crittografia Moderna*, 2ª ed., 2015 (CRC Press: Boca Raton, FL). Paar e Pelzl, *Comprendere la Crittografia*, 2010 (Springer-Verlag: Berlino) [^5].

# Crittografia Simmetrica
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

Una delle due principali branche della crittografia è la crittografia simmetrica. Include schemi di cifratura così come schemi preoccupati con l'autenticazione e l'integrità. Fino agli anni '70, tutta la crittografia avrebbe consistito di schemi di cifratura simmetrica.

La discussione principale inizia esaminando gli schemi di cifratura simmetrica e facendo la distinzione cruciale tra cifrari a flusso e cifrari a blocchi. Successivamente, ci rivolgiamo ai codici di autenticazione dei messaggi, che sono schemi per garantire l'integrità e l'autenticità dei messaggi. Infine, esploriamo come gli schemi di cifratura simmetrica e i codici di autenticazione dei messaggi possono essere combinati per garantire una comunicazione sicura.

Questo capitolo discute varie schemi crittografici simmetrici dalla pratica in modo superficiale. Il prossimo capitolo offre una esposizione dettagliata della cifratura con un cifrario a flusso e un cifrario a blocchi dalla pratica, rispettivamente RC4 e AES.

Prima di iniziare la nostra discussione sulla crittografia simmetrica, voglio brevemente fare alcune osservazioni sulle illustrazioni di Alice e Bob in questo e nei capitoli successivi.

## Alice e Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Nell'illustrare i principi della crittografia, le persone spesso si affidano a esempi che coinvolgono Alice e Bob. Farò lo stesso.

Soprattutto se sei nuovo alla crittografia, è importante rendersi conto che questi esempi di Alice e Bob sono solo intesi come illustrazioni dei principi e delle costruzioni crittografiche in un ambiente semplificato. I principi e le costruzioni, tuttavia, sono applicabili a una gamma molto più ampia di contesti della vita reale.

Ecco cinque punti chiave da tenere a mente sugli esempi che coinvolgono Alice e Bob in crittografia:

1. Possono facilmente essere tradotti in esempi con altri tipi di attori come aziende o organizzazioni governative.
2. Possono facilmente essere estesi per includere tre o più attori.
3. Negli esempi, Bob e Alice sono tipicamente partecipanti attivi nella creazione di ciascun messaggio e nell'applicazione di schemi crittografici su quel messaggio. Ma, in realtà, le comunicazioni elettroniche sono in gran parte automatizzate. Quando visiti un sito web utilizzando la sicurezza del livello di trasporto, ad esempio, la crittografia è tipicamente gestita interamente dal tuo computer e dal server web. 4. Nel contesto della comunicazione elettronica, i "messaggi" che vengono inviati attraverso un canale di comunicazione sono solitamente pacchetti TCP/IP. Questi possono appartenere a un'e-mail, un messaggio di Facebook, una conversazione telefonica, un trasferimento di file, un sito web, un caricamento di software, e così via. Non sono messaggi nel senso tradizionale. Tuttavia, i crittografi spesso semplificano questa realtà affermando che il messaggio è, per esempio, un'e-mail.
5. Gli esempi si concentrano tipicamente sulla comunicazione elettronica, ma possono anche essere estesi a forme tradizionali di comunicazione come le lettere.

## Schemi di crittografia simmetrica

Possiamo definire in modo approssimativo uno **schema di crittografia simmetrica** come qualsiasi schema crittografico con tre algoritmi:

1. Un **algoritmo di generazione della chiave**, che genera una chiave privata.
2. Un **algoritmo di crittografia**, che prende la chiave privata e un testo in chiaro come input e produce un testo cifrato come output.
3. Un **algoritmo di decrittazione**, che prende la chiave privata e il testo cifrato come input e produce il testo in chiaro originale come output.

Tipicamente uno schema di crittografia—sia esso simmetrico o asimmetrico—offre un modello per la crittografia basato su un algoritmo principale, piuttosto che una specifica esatta.

Per esempio, consideriamo Salsa20, uno schema di crittografia simmetrica. Può essere utilizzato sia con lunghezze di chiave di 128 che di 256 bit. La scelta riguardo alla lunghezza della chiave influisce su alcuni dettagli minori dell'algoritmo (il numero di round nell'algoritmo per essere precisi).

Ma non si direbbe che usare Salsa20 con una chiave di 128 bit sia uno schema di crittografia diverso da Salsa20 con una chiave di 256 bit. L'algoritmo principale rimane lo stesso. Solo quando l'algoritmo principale cambia si potrebbe realmente parlare di due schemi di crittografia diversi.

Gli schemi di crittografia simmetrica sono tipicamente utili in due tipi di casi: (1) Quelli in cui due o più agenti comunicano a distanza e vogliono mantenere segreto il contenuto delle loro comunicazioni; e (2) quelli in cui un agente vuole mantenere segreto il contenuto di un messaggio nel tempo.

Puoi vedere una rappresentazione della situazione (1) in *Figura 1* qui sotto. Bob vuole inviare un messaggio M ad Alice a distanza, ma non vuole che altri possano leggere quel messaggio.

Bob prima cifra il messaggio M con la chiave privata K. Poi, invia il testo cifrato C ad Alice. Una volta che Alice ha ricevuto il testo cifrato, può decifrarlo usando la chiave K e leggere il testo in chiaro. Con un buon schema di crittografia, qualsiasi attaccante che intercetti il testo cifrato C non dovrebbe essere in grado di apprendere nulla di realmente significativo riguardo al messaggio M.

Puoi vedere una rappresentazione della situazione (2) in *Figura 2* qui sotto. Bob vuole impedire ad altri di visualizzare certe informazioni. Una situazione tipica potrebbe essere quella in cui Bob è un dipendente che memorizza dati sensibili sul suo computer, che né estranei né i suoi colleghi dovrebbero leggere.
Bob cifra il messaggio M al tempo T<sub>0</sub> con la chiave K per produrre il testo cifrato C. Al tempo T<sub>1</sub> ha nuovamente bisogno del messaggio e decifra il testo cifrato C con la chiave K. Qualsiasi attaccante che potrebbe aver intercettato il testo cifrato C nel frattempo non dovrebbe essere stato in grado di dedurre nulla di significativo su M da esso.
*Figura 1: Segretezza nello spazio*

![Figura 1: Segretezza nello spazio](assets/Figure4-1.webp "Figura 1: Segretezza nello spazio")

*Figura 2: Segretezza nel tempo*

![Figura 2: Segretezza nel tempo](assets/Figure4-2.webp "Figura 2: Segretezza nel tempo")

## Un esempio: Il cifrario di Cesare
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

Nel Capitolo 2, abbiamo incontrato il cifrario di Cesare che è un esempio di un semplicissimo schema di cifratura simmetrica. Vediamolo di nuovo qui.

Supponiamo un dizionario *D* che equipara tutte le lettere dell'alfabeto inglese, in ordine, con l'insieme dei numeri {0,1,2…,25}. Supponiamo un insieme di possibili messaggi **M**. Il cifrario di Cesare è, quindi, uno schema di cifratura definito come segue:

- Selezionare casualmente una chiave k dall'insieme delle possibili chiavi **K**, dove **K** = {0,1,2,…,25}
- Cifrare un messaggio m є **M**, come segue:
    - Separare m nelle sue singole lettere m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Convertire ogni m<sub>i</sub> in un numero secondo *D*
    - Per ogni m<sub>i</sub>, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Convertire ogni c<sub>i</sub> in una lettera secondo *D*
    - Poi combinare c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub> per ottenere il testo cifrato c
- Decifrare un testo cifrato c come segue:
    - Convertire ogni c<sub>i</sub> in un numero secondo *D*
    - Per ogni c<sub>i</sub>, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    - Convertire ogni m<sub>i</sub> in una lettera secondo *D*
    - Poi combinare m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub> per ottenere il messaggio originale m

Ciò che rende il cifrario di Cesare uno schema di cifratura simmetrica è che la stessa chiave viene utilizzata sia per il processo di cifratura che per quello di decifratura. Ad esempio, supponiamo che tu voglia cifrare il messaggio "DOG" usando il cifrario di Cesare, e che tu abbia selezionato casualmente "24" come chiave. Cifrando il messaggio con questa chiave si otterrebbe “BME”. L'unico modo per recuperare il messaggio originale è utilizzare la stessa chiave, "24", per il processo di decifratura.
Il cifrario di Cesare è un esempio di **cifrario a sostituzione monoalfabetica**: uno schema di crittografia in cui l'alfabeto del testo cifrato è fisso (cioè, viene utilizzato solo un alfabeto). Assumendo che l'algoritmo di decrittazione sia deterministico, ogni simbolo nel testo cifrato di sostituzione può al massimo corrispondere a un simbolo nel testo in chiaro.
Fino al 1700, molte applicazioni della crittografia si basavano pesantemente sui cifrari a sostituzione monoalfabetica, anche se spesso questi erano molto più complessi del cifrario di Cesare. Si potrebbe, ad esempio, selezionare casualmente una lettera dell'alfabeto per ogni lettera del testo originale con il vincolo che ogni lettera occorra solo una volta nell'alfabeto del testo cifrato. Ciò significa che avresti avuto fattoriale 26 possibili chiavi private, il che era enorme nell'era preinformatica.

Nota che incontrerai spesso il termine **cifrario** nella crittografia. Sii consapevole che questo termine ha vari significati. Infatti, conosco almeno cinque significati distinti del termine all'interno della crittografia.

In alcuni casi si riferisce a uno schema di crittografia, come nel cifrario di Cesare e nel cifrario a sostituzione monoalfabetica. Tuttavia, il termine può anche riferirsi specificamente all'algoritmo di crittografia, alla chiave privata, o semplicemente al testo cifrato di qualsiasi schema di crittografia.

Infine, il termine cifrario può anche riferirsi a un algoritmo di base da cui è possibile costruire schemi crittografici. Questi possono includere vari algoritmi di crittografia, ma anche altri tipi di schemi crittografici. Questo senso del termine diventa rilevante nel contesto dei cifrari a blocchi (vedi la sezione "Cifrari a blocchi" qui sotto).

Potresti anche incontrare i termini **cifrare** o **decifrare**. Questi termini sono semplicemente sinonimi di crittografia e decrittografia.

## Attacchi di forza bruta e il principio di Kerckhoff
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Il cifrario di Cesare è uno schema di crittografia simmetrica molto insicuro, almeno nel mondo moderno.<sup>[1](#footnote1)</sup> Un attaccante potrebbe semplicemente tentare la decrittazione di qualsiasi testo cifrato con tutte le 26 possibili chiavi per vedere quale risultato ha senso. Questo tipo di attacco, in cui l'attaccante sta semplicemente ciclando attraverso le chiavi per vedere cosa funziona, è noto come **attacco di forza bruta** o **ricerca esaustiva della chiave**.

Perché uno schema di crittografia soddisfi una nozione minima di sicurezza, deve avere un insieme di chiavi possibili, o **spazio delle chiavi**, che sia così grande da rendere gli attacchi di forza bruta impraticabili. Tutti gli schemi di crittografia moderni soddisfano questo standard. È noto come il **principio dello spazio delle chiavi sufficiente**. Un principio simile si applica tipicamente in diversi tipi di schemi crittografici.

Per avere un'idea della grandezza massiva dello spazio delle chiavi negli schemi di crittografia moderni, supponiamo che un file sia stato crittografato con un 128-bit utilizzando lo standard di crittografia avanzata. Ciò significa che un attaccante ha a disposizione un insieme di 2<sup>128</sup> chiavi attraverso le quali deve ciclare per un attacco di forza bruta. Una possibilità di successo dello 0,78% con questa strategia richiederebbe all'attaccante di ciclare attraverso circa 2,65 x 10<sup>36</sup> chiavi.
Supponiamo ottimisticamente che un attaccante possa tentare 10 quadrilioni di chiavi al secondo (ovvero, 10<sup>16</sup> chiavi al secondo). Per testare lo 0,78% di tutte le chiavi nello spazio delle chiavi, il suo attacco dovrebbe durare 2,65 x 10<sup>20</sup> secondi. Questo corrisponde a circa 8,4 trilioni di anni. Quindi, anche un attacco brute force da parte di un avversario assurdamente potente non è realistico con uno schema di crittografia moderno a 128 bit. Questo è il principio dello spazio chiave sufficiente in azione.

La cifratura a traslazione è più sicura se l'attaccante non conosce l'algoritmo di crittografia? Forse, ma non di molto.

In ogni caso, la crittografia moderna assume sempre che la sicurezza di qualsiasi schema di crittografia simmetrica si basi unicamente sul mantenimento segreto della chiave privata. Si presume sempre che l'attaccante conosca tutti gli altri dettagli, inclusi lo spazio dei messaggi, lo spazio delle chiavi, lo spazio del testo cifrato, l'algoritmo di selezione della chiave, l'algoritmo di crittografia e l'algoritmo di decrittazione.

L'idea che la sicurezza di uno schema di crittografia simmetrica possa basarsi solo sul segreto della chiave privata è nota come **principio di Kerckhoffs**.

Come originariamente inteso da Kerckhoffs, il principio si applica solo agli schemi di crittografia simmetrica. Una versione più generale del principio, tuttavia, si applica anche a tutti gli altri tipi di schemi crittografici moderni: il design di qualsiasi schema crittografico non deve essere necessario che sia segreto affinché sia sicuro; il segreto può estendersi solo ad alcune stringhe di informazioni, tipicamente una chiave privata.

Il principio di Kerckhoffs è centrale nella crittografia moderna per quattro motivi.<sup>[2](#footnote2)</sup> Primo, esiste solo un numero limitato di schemi crittografici per tipi particolari di applicazioni. Ad esempio, la maggior parte delle applicazioni di crittografia simmetrica moderna utilizza il cifrario Rijndael. Quindi, il tuo segreto riguardo al design di uno schema è solo molto limitato. C'è, tuttavia, molta più flessibilità nel mantenere segreta qualche chiave privata per il cifrario Rijndael.

Secondo, è più facile sostituire una stringa di informazioni che un intero schema crittografico. Supponiamo che tutti i dipendenti di un'azienda abbiano lo stesso software di crittografia e che ogni due dipendenti abbiano una chiave privata per comunicare confidenzialmente. I compromessi delle chiavi sono un problema in questo scenario, ma almeno l'azienda potrebbe mantenere il software con tali violazioni di sicurezza. Se l'azienda si affidasse al segreto dello schema, allora qualsiasi violazione di quel segreto richiederebbe la sostituzione di tutto il software.

Terzo, il principio di Kerckhoffs consente la standardizzazione e la compatibilità tra gli utenti degli schemi crittografici. Questo ha enormi benefici per l'efficienza. Ad esempio, è difficile immaginare come milioni di persone potrebbero connettersi in modo sicuro ai server web di Google ogni giorno, se quella sicurezza richiedesse di mantenere segreti gli schemi crittografici.

Quarto, il principio di Kerckhoff consente il controllo pubblico degli schemi crittografici. Questo tipo di controllo è assolutamente necessario per ottenere schemi crittografici sicuri. Illustrativamente, l'algoritmo principale nella crittografia simmetrica, il cifrario Rijndael, è stato il risultato di una competizione organizzata dal National Institute of Standards and Technology tra il 1997 e il 2000.

Qualsiasi sistema che tenti di ottenere **sicurezza tramite l'oscurità** è un sistema che si basa sul mantenimento segreto dei dettagli del suo design e/o implementazione. In crittografia, sarebbe specificamente un sistema che si basa sul mantenimento segreto dei dettagli del design dello schema crittografico. Quindi, la sicurezza tramite l'oscurità è in diretto contrasto con il principio di Kerckhoffs.
La capacità dell'apertura di rafforzare la qualità e la sicurezza si estende anche più ampiamente al mondo digitale rispetto alla sola crittografia. Le distribuzioni Linux libere e open source come Debian, ad esempio, hanno generalmente diversi vantaggi rispetto ai loro corrispettivi Windows e MacOS in termini di privacy, stabilità, sicurezza e flessibilità. Sebbene ciò possa avere molteplici cause, il principio più importante è probabilmente, come Eric Raymond ha formulato nel suo famoso saggio "La Cattedrale e il Bazar", che "[d]ato un numero sufficiente di occhi, tutti i bug sono superficiali."<sup>[3](#footnote3)</sup> È questo principio della saggezza della folla che ha dato a Linux il suo successo più significativo.
Non si può mai affermare in modo univoco che uno schema crittografico sia "sicuro" o "insicuro". Invece, esistono varie nozioni di sicurezza per gli schemi crittografici. Ogni **definizione di sicurezza crittografica** deve specificare (1) gli obiettivi di sicurezza, così come (2) le capacità di un attaccante. Analizzare gli schemi crittografici rispetto a una o più nozioni specifiche di sicurezza fornisce intuizioni sulle loro applicazioni e limitazioni.

Sebbene non approfondiremo tutti i dettagli delle varie nozioni di sicurezza crittografica, dovresti sapere che due ipotesi sono ubiquitarie a tutte le moderne nozioni di sicurezza crittografica relative agli schemi simmetrici e asimmetrici (e in qualche forma ad altri primitivi crittografici):

* La conoscenza dell'attaccante riguardo allo schema è conforme al principio di Kerckhoffs.
* L'attaccante non può realisticamente eseguire un attacco a forza bruta sullo schema. In particolare, i modelli di minaccia delle nozioni di sicurezza crittografica tipicamente non consentono nemmeno attacchi a forza bruta, poiché si assume che questi non siano una considerazione rilevante.

## Cifrari a flusso
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Gli schemi di cifratura simmetrica sono standardmente suddivisi in due tipi: cifrari a flusso e cifrari a blocchi. Questa distinzione è tuttavia alquanto problematica, in quanto le persone usano questi termini in modo non coerente. Nelle prossime sezioni, stabilirò la distinzione nel modo che ritengo migliore. Dovresti tuttavia essere consapevole che molte persone useranno questi termini in modo leggermente diverso da come ho stabilito.

Cominciamo dai cifrari a flusso. Un **cifrario a flusso** è uno schema di cifratura simmetrica dove la cifratura consiste di due passaggi.

Primo, viene prodotta una stringa della lunghezza del testo in chiaro tramite una chiave privata. Questa stringa è chiamata **keystream**.

Successivamente, il keystream è combinato matematicamente con il testo in chiaro per produrre un testo cifrato. Questa combinazione è tipicamente un'operazione XOR. Per decifrare, è sufficiente invertire l'operazione. (Nota che A XOR B = B XOR A, nel caso in cui A e B siano stringhe di bit. Quindi, l'ordine di un'operazione XOR in un cifrario a flusso non importa per il risultato. Questa proprietà è nota come commutatività.)

Un tipico cifrario a flusso XOR è rappresentato nella *Figura 3*. Prima si prende una chiave privata K e si usa per generare un keystream. Il keystream è poi combinato con il testo in chiaro tramite un'operazione XOR per produrre il testo cifrato. Qualsiasi agente che riceve il testo cifrato può facilmente decifrarlo se ha la chiave K. Tutto ciò che deve fare è creare un keystream lungo quanto il testo cifrato secondo la procedura specificata dello schema e applicarvi l'XOR con il testo cifrato.

*Figura 3: Un cifrario a flusso XOR*

![Figura 3: Un cifrario a flusso XOR](assets/Figure4-3.webp "Figura 3: Un cifrario a flusso XOR")
Si ricorda che uno schema di crittografia è tipicamente un modello per la crittografia con lo stesso algoritmo di base, piuttosto che una specifica esatta. Di conseguenza, un cifrario a flusso è tipicamente un modello per la crittografia in cui si possono utilizzare chiavi di lunghezze diverse. Anche se la lunghezza della chiave può influenzare alcuni dettagli minori dello schema, non ne influenzerà la forma essenziale.
Il cifrario di Cesare è un esempio di cifrario a flusso molto semplice e insicuro. Utilizzando una singola lettera (la chiave privata), si può produrre una stringa di lettere della lunghezza del messaggio (il flusso di chiavi). Questo flusso di chiavi viene poi combinato con il testo in chiaro tramite un'operazione modulo per produrre un testo cifrato. (Questa operazione modulo può essere semplificata in un'operazione XOR quando si rappresentano le lettere in bit).

Un altro esempio famoso di cifrario a flusso è il **cifrario di Vigenère**, dal nome di Blaise de Vigenère che lo sviluppò completamente alla fine del XVI secolo (anche se altri avevano fatto molto lavoro precedente). È un esempio di **cifrario a sostituzione polialfabetica**: uno schema di crittografia in cui l'alfabeto del testo cifrato per un simbolo del testo in chiaro cambia a seconda della sua posizione nel testo. A differenza di un cifrario a sostituzione monoalfabetica, i simboli del testo cifrato possono essere associati a più di un simbolo del testo in chiaro.

Con la crescente popolarità della crittografia nell'Europa rinascimentale, crebbe anche la **crittoanalisi**—cioè, la decifrazione dei testi cifrati—particolarmente, utilizzando l'**analisi delle frequenze**. Quest'ultima impiega regolarità statistiche nella nostra lingua per decifrare i testi cifrati, ed è stata scoperta dagli studiosi arabi già nel nono secolo. È una tecnica che funziona particolarmente bene con testi lunghi. E anche i cifrari a sostituzione monoalfabetica più sofisticati non erano più sufficienti contro l'analisi delle frequenze entro il 1700 in Europa, particolarmente in ambiti militari e di sicurezza. Poiché il cifrario di Vigenère offriva un significativo avanzamento in termini di sicurezza, divenne popolare in questo periodo e si diffuse ampiamente entro la fine del 1700.

Parlando in termini informali, lo schema di crittografia funziona come segue:

1. Seleziona una parola di più lettere come chiave privata
2. Per qualsiasi messaggio, applica il cifrario di Cesare a ogni lettera del messaggio utilizzando la lettera corrispondente nella parola chiave come spostamento
3. Se hai completato il ciclo attraverso la parola chiave ma non hai ancora cifrato completamente il testo in chiaro, applica nuovamente le lettere della parola chiave come cifrario di Cesare alle lettere corrispondenti nel resto del testo
4. Continua questo processo fino a quando l'intero messaggio è stato cifrato

Per illustrare, supponiamo che la tua chiave privata sia GOLD e tu voglia criptare il messaggio "CRYPTOGRAPHY". In tal caso procederesti come segue secondo il cifrario di Vigenère:

- c<sub>0</sub> = [(2 + 6) Mod 26] = 8 = I
- c<sub>1</sub> = [(17 + 14) Mod 26] = 5 = F
- c<sub>2</sub> = [(24 + 11) Mod 26] = 9 = J
- c<sub>3</sub> = [(15 + 3) Mod 26] = 18 = S
- c<sub>4</sub> = [(19 + 6) Mod 26] = 25 = Z
- c<sub>5</sub> = [(14 + 14) Mod 26] = 2 = C
- c<sub>6</sub> = [(6 + 11) Mod 26] = 17 = R
- c<sub>7</sub> = [(17 + 3) Mod 26] = 20 = U
- c<sub>8</sub> = [(0 + 6) Mod 26] = 6 = G
- c<sub>9</sub> = [(15 + 14) Mod 26] = 3 = D
- c<sub>10</sub> = [(7 + 11) Mod 26] = 18 = S
- c<sub>11</sub> = [(24 + 3) Mod 26] = 1 = B
- c = "IFJSZCRUGDSB"

Un altro famoso esempio di cifrario a flusso è il **one-time pad**. Con il one-time pad, si crea semplicemente una stringa di bit casuali lunga quanto il messaggio in chiaro e si produce il testo cifrato tramite l'operazione XOR. Pertanto, la chiave privata e il flusso di chiavi sono equivalenti con un one-time pad.

Mentre il cifrario di Cesare e i cifrari di Vigenère sono molto insicuri nell'era moderna, il one-time pad è molto sicuro se usato correttamente. Probabilmente, l'applicazione più famosa del one-time pad è stata, almeno fino agli anni '80, per la **linea diretta Washington-Mosca**.

La linea diretta è un collegamento di comunicazione diretto tra Washington e Mosca per questioni urgenti che è stato installato dopo la Crisi dei missili di Cuba. La tecnologia per questa ha subito trasformazioni nel corso degli anni. Attualmente, include un cavo in fibra ottica diretto così come due collegamenti satellitari (per ridondanza), che consentono e-mail e messaggistica testuale. Il collegamento termina in vari luoghi negli Stati Uniti. Il Pentagono, la Casa Bianca e Raven Rock Mountain sono noti punti finali. Contrariamente all'opinione popolare, la linea diretta non ha mai coinvolto telefoni.

In sostanza, il sistema del one-time pad funzionava come segue. Sia Washington che Mosca avrebbero avuto due insiemi di numeri casuali. Un insieme di numeri casuali, creato dai Russi, riguardava la cifratura e decifratura di qualsiasi messaggio in lingua russa. Un insieme di numeri casuali, creato dagli Americani, riguardava la cifratura e decifratura di qualsiasi messaggio in lingua inglese. Di tanto in tanto, ulteriori numeri casuali venivano consegnati all'altra parte tramite corrieri fidati.

Washington e Mosca erano, quindi, in grado di comunicare segretamente utilizzando questi numeri casuali per creare one-time pads. Ogni volta che si doveva comunicare, si utilizzava la porzione successiva di numeri casuali per il proprio messaggio.

Sebbene altamente sicuro, il one-time pad affronta significative limitazioni pratiche: la chiave deve essere lunga quanto il messaggio e nessuna parte di un one-time pad può essere riutilizzata. Questo significa che è necessario tenere traccia di dove ci si trova nel one-time pad, conservare un enorme numero di bit e scambiare bit casuali con i propri controparti di tanto in tanto. Di conseguenza, il one-time pad non è frequentemente utilizzato nella pratica.

Invece, i cifrari a flusso pseudocasuali predominanti utilizzati nella pratica sono **pseudorandom stream ciphers**. Salsa20 e una variante strettamente correlata chiamata ChaCha sono esempi di cifrari a flusso pseudocasuali comunemente utilizzati.

Con questi cifrari a flusso pseudocasuali, si seleziona casualmente una chiave K che è più corta della lunghezza del testo in chiaro. Tale chiave casuale K è solitamente creata dal nostro computer sulla base di dati imprevedibili che raccoglie nel tempo, come il tempo tra i messaggi di rete, i movimenti del mouse e così via.
Questa chiave casuale K viene quindi inserita in un algoritmo di espansione che crea un flusso di chiavi pseudocasuali lungo quanto il messaggio. Puoi specificare esattamente quanto deve essere lungo il flusso di chiavi (ad esempio, 500 bit, 1000 bit, 1200 bit, 29.117 bit, e così via).
Un flusso di chiavi pseudocasuali appare *come se* fosse stato scelto completamente a caso dall'insieme di tutte le stringhe della stessa lunghezza. Di conseguenza, la cifratura con un flusso di chiavi pseudocasuali appare come se fosse stata effettuata con un blocco monouso. Ma ovviamente, non è così.

Poiché la nostra chiave privata è più corta del flusso di chiavi e il nostro algoritmo di espansione deve essere deterministico affinché il processo di cifratura/decifratura funzioni, non ogni flusso di chiavi di quella particolare lunghezza potrebbe risultare come output dalla nostra operazione di espansione.

Supponiamo, ad esempio, che la nostra chiave privata abbia una lunghezza di 128 bit e che possiamo inserirla in un algoritmo di espansione per creare un flusso di chiavi molto più lungo, diciamo di 2.500 bit. Poiché il nostro algoritmo di espansione deve essere deterministico, il nostro algoritmo può al massimo selezionare 1/2<sup>128</sup> stringhe con una lunghezza di 2.500 bit. Quindi, un tale flusso di chiavi non potrebbe mai essere selezionato completamente a caso da tutte le stringhe della stessa lunghezza.

La nostra definizione di cifrario a flusso ha due aspetti: (1) un flusso di chiavi lungo quanto il testo in chiaro viene generato con l'aiuto di una chiave privata; e (2) questo flusso di chiavi viene combinato con il testo in chiaro, tipicamente tramite un'operazione XOR, per produrre il testo cifrato.

A volte le persone definiscono la condizione (1) in modo più rigoroso, affermando che il flusso di chiavi deve specificamente essere pseudocasuale. Ciò significa che né il cifrario a spostamento, né il blocco monouso sarebbero considerati cifrari a flusso.

A mio avviso, definire la condizione (1) in modo più ampio fornisce un modo più semplice per organizzare gli schemi di cifratura. Inoltre, significa che non dobbiamo smettere di chiamare un particolare schema di cifratura un cifrario a flusso solo perché apprendiamo che in realtà non si basa su flussi di chiavi pseudocasuali.

## Cifrari a blocchi
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Il primo modo in cui si comprende comunemente un **cifrario a blocchi** è come qualcosa di più primitivo rispetto a un cifrario a flusso: Un algoritmo principale che esegue una trasformazione che preserva la lunghezza su una stringa di lunghezza adeguata con l'aiuto di una chiave. Questo algoritmo può essere utilizzato per creare schemi di cifratura e forse altri tipi di schemi crittografici.

Frequentemente, un cifrario a blocchi può prendere stringhe di input di lunghezze variabili come 64, 128 o 256 bit, così come chiavi di lunghezze variabili come 128, 192 o 256 bit. Anche se alcuni dettagli dell'algoritmo potrebbero cambiare a seconda di queste variabili, l'algoritmo principale non cambia. Se lo facesse, parleremmo di due cifrari a blocchi differenti. Nota che l'uso della terminologia dell'algoritmo principale qui è lo stesso che per gli schemi di cifratura.

Una rappresentazione di come funziona un cifrario a blocchi può essere vista nella *Figura 4* qui sotto. Un messaggio M di lunghezza L e una chiave K servono come input al cifrario a blocchi. Esso restituisce un messaggio M’ della lunghezza L. La chiave non necessariamente deve essere della stessa lunghezza di M e M’ per la maggior parte dei cifrari a blocchi.

*Figura 4: Un cifrario a blocchi*

![Figura 4: Un cifrario a blocchi](assets/Figure4-4.webp "Figura 4: Un cifrario a blocchi")
Un cifrario a blocchi di per sé non costituisce uno schema di crittografia. Tuttavia, un cifrario a blocchi può essere utilizzato con vari **modi di funzionamento** per produrre diversi schemi di crittografia. Un modo di funzionamento aggiunge semplicemente alcune operazioni aggiuntive esterne al cifrario a blocchi.

Per illustrare come funziona, supponiamo un cifrario a blocchi (BC) che richiede una stringa di input di 128 bit e una chiave privata di 128 bit. La Figura 5 qui sotto mostra come quel cifrario a blocchi può essere utilizzato con il **modo di codice elettronico** (**modalità ECB**) per creare uno schema di crittografia. (Le ellissi sulla destra indicano che è possibile ripetere questo schema tutte le volte che è necessario).

*Figura 5: Un cifrario a blocchi con modalità ECB*

![Figura 5: Un cifrario a blocchi con modalità ECB](assets/Figure4-5.webp "Figura 5: Un cifrario a blocchi con modalità ECB")

Il processo per la crittografia con codice elettronico utilizzando il cifrario a blocchi è il seguente. Verifica se puoi dividere il tuo messaggio in chiaro in blocchi di 128 bit. Se non è possibile, aggiungi del **riempimento** al messaggio, in modo che il risultato possa essere diviso uniformemente per la dimensione del blocco di 128 bit. Questi sono i dati utilizzati per il processo di crittografia.

Ora dividi i dati in blocchi di stringhe di 128 bit (M<sub>1</sub>, M<sub>2</sub>, M<sub>3</sub>, e così via). Fai passare ogni stringa di 128 bit attraverso il cifrario a blocchi con la tua chiave di 128 bit per produrre blocchi di testo cifrato di 128 bit (C<sub>1</sub>, C<sub>2</sub>, C<sub>3</sub>, e così via). Questi blocchi, ricombinati, formano il testo cifrato completo.

La decrittazione è semplicemente il processo inverso, anche se il destinatario ha bisogno di un modo riconoscibile per rimuovere qualsiasi riempimento dai dati decrittati per produrre il messaggio in chiaro originale.

Sebbene relativamente semplice, un cifrario a blocchi con modalità di codice elettronico manca di sicurezza. Questo perché porta a una **crittografia deterministica**. Qualsiasi due stringhe di dati identiche di 128 bit vengono crittografate esattamente nello stesso modo. Questa informazione può essere sfruttata.

Invece, qualsiasi schema di crittografia costruito da un cifrario a blocchi dovrebbe essere **probabilistico**: ovvero, la crittografia di qualsiasi messaggio M, o di qualsiasi specifico blocco di M, dovrebbe generalmente produrre un risultato diverso ogni volta.<sup>[5](#footnote5)</sup>

La **modalità di concatenazione dei blocchi cifrati** (**modalità CBC**) è probabilmente il modo più comune utilizzato con un cifrario a blocchi. La combinazione, se fatta correttamente, produce uno schema di crittografia probabilistico. Puoi vedere una rappresentazione di questa modalità di funzionamento nella Figura 6 qui sotto.

*Figura 6: Un cifrario a blocchi con modalità CBC*

![Figura 6: Un cifrario a blocchi con modalità CBC](assets/Figure4-6.webp "Figura 6: Un cifrario a blocchi con modalità CBC")

Supponiamo che la dimensione del blocco sia di nuovo di 128 bit. Quindi, per iniziare, dovresti nuovamente assicurarti che il tuo messaggio in chiaro originale riceva il necessario riempimento.

Poi, fai lo XOR della prima porzione di 128 bit del tuo testo in chiaro con un **vettore di inizializzazione** di 128 bit. Il risultato viene inserito nel cifrario a blocchi per produrre un testo cifrato per il primo blocco. Per il secondo blocco di 128 bit, fai prima lo XOR del testo in chiaro con il testo cifrato del primo blocco, prima di inserirlo nel cifrario a blocchi. Continui questo processo fino a quando non hai crittografato l'intero messaggio in chiaro.

Quando hai finito, invii il messaggio cifrato insieme al vettore di inizializzazione non cifrato al destinatario. Il destinatario ha bisogno di conoscere il vettore di inizializzazione, altrimenti non può decifrare il testo cifrato.
Questa costruzione è molto più sicura rispetto alla modalità libro codice elettronico quando utilizzata correttamente. Dovresti, prima di tutto, assicurarti che il vettore di inizializzazione sia una stringa casuale o pseudocasuale. Inoltre, dovresti utilizzare un vettore di inizializzazione diverso ogni volta che usi questo schema di crittografia.
In altre parole, il tuo vettore di inizializzazione dovrebbe essere un nonce casuale o pseudocasuale, dove un **nonce** sta per "un numero che viene utilizzato una sola volta". Se mantieni questa pratica, allora la modalità CBC con un cifrario a blocchi garantisce che qualsiasi due blocchi di testo in chiaro identici saranno generalmente criptati in modo diverso ogni volta.

Infine, rivolgiamo la nostra attenzione alla **modalità di feedback di output** (**modalità OFB**). Puoi vedere una rappresentazione di questa modalità in *Figura 7*.

*Figura 7: Un cifrario a blocchi con modalità OFB*

![Figura 7: Un cifrario a blocchi con modalità OFB](assets/Figure4-7.webp "Figura 7: Un cifrario a blocchi con modalità OFB")

Con la modalità OFB selezioni anche un vettore di inizializzazione. Ma qui, per il primo blocco, il vettore di inizializzazione è inserito direttamente nel cifrario a blocchi con la tua chiave. I 128 bit risultanti sono, quindi, trattati come un flusso di chiavi. Questo flusso di chiavi è XORato con il testo in chiaro per produrre il testo cifrato per il blocco. Per i blocchi successivi, utilizzi il flusso di chiavi del blocco precedente come input nel cifrario a blocchi e ripeti i passaggi.

Se osservi attentamente, ciò che è stato effettivamente creato qui dal cifrario a blocchi con modalità OFB è un cifrario a flusso. Generi porzioni di flusso di chiavi di 128 bit fino ad avere la lunghezza del testo in chiaro (scartando i bit che non ti servono dall'ultima porzione di flusso di chiavi di 128 bit). Quindi, XORi il flusso di chiavi con il tuo messaggio in chiaro per ottenere il testo cifrato.

Nella sezione precedente sui cifrari a flusso, ho affermato che produci un flusso di chiavi con l'aiuto di una chiave privata. Per essere precisi, non deve essere creato solo con una chiave privata. Come puoi vedere nella modalità OFB, il flusso di chiavi è prodotto con il supporto sia di una chiave privata che di un vettore di inizializzazione.

Nota che, come con la modalità CBC, è importante selezionare un nonce pseudocasuale o casuale per il vettore di inizializzazione ogni volta che usi un cifrario a blocchi in modalità OFB. Altrimenti, la stessa stringa di messaggi di 128 bit inviata in comunicazioni diverse sarà criptata nello stesso modo. Questo è un modo per creare una crittografia probabilistica con un cifrario a flusso.

Alcuni cifrari a flusso utilizzano solo una chiave privata per creare un flusso di chiavi. Per quei cifrari a flusso, è importante che tu utilizzi un nonce casuale per selezionare la chiave privata per ogni istanza di comunicazione. Altrimenti, i risultati della crittografia con quei cifrari a flusso saranno anche deterministici, portando a problemi di sicurezza.

Il cifrario a blocchi moderno più popolare è il **cifrario Rijndael**. È stato il vincitore tra quindici proposte in un concorso tenuto dal National Institute of Standards and Technology (NIST) tra il 1997 e il 2000 per sostituire uno standard di crittografia più vecchio, lo **standard di crittografia dei dati** (**DES**).
Il cifrario Rijndael può essere utilizzato con diverse specifiche per lunghezze di chiave e dimensioni di blocco, così come in diverse modalità di funzionamento. Il comitato per la competizione NIST ha adottato una versione ristretta del cifrario Rijndael, ovvero una che richiede dimensioni di blocco di 128 bit e lunghezze di chiave di 128 bit, 192 bit o 256 bit, come parte dello **standard avanzato di crittografia** (**AES**). Questo è davvero lo standard principale per le applicazioni di crittografia simmetrica. È così sicuro che persino la NSA sembra disposta ad utilizzarlo con chiavi da 256 bit per documenti top secret.<sup>[6](#footnote6)</sup>
Il cifrario a blocchi AES sarà spiegato in dettaglio nel *Capitolo 5*.

## Chiarimenti sulla confusione
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

La confusione riguardo alla distinzione tra cifrari a blocchi e cifrari a flusso nasce perché a volte le persone interpretano il termine cifrario a blocchi come riferito specificamente a un *cifrario a blocchi con una modalità di crittografia a blocchi*.

Considerate le modalità ECB e CBC nella sezione precedente. Queste richiedono specificamente che i dati per la crittografia siano divisibili per la dimensione del blocco (il che significa che potreste dover utilizzare il padding per il messaggio originale). Inoltre, i dati in queste modalità sono anche operati direttamente dal cifrario a blocchi (e non solo combinati con il risultato di un'operazione di cifrario a blocchi come nella modalità OFB).

Pertanto, alternativamente, potete definire un **cifrario a blocchi** come qualsiasi schema di crittografia, che opera su blocchi di messaggio di lunghezza fissa alla volta (dove ogni blocco deve essere più lungo di un byte, altrimenti si trasforma in un cifrario a flusso). Sia i dati per la crittografia che il testo cifrato devono dividersi uniformemente in questa dimensione del blocco. Tipicamente, la dimensione del blocco è di 64, 128, 192 o 256 bit in lunghezza. Al contrario, un cifrario a flusso può crittografare messaggi in pezzi di un bit o byte alla volta.

Con questa comprensione più specifica del cifrario a blocchi, potete effettivamente affermare che gli schemi di crittografia moderni sono o cifrari a flusso o cifrari a blocchi. Da qui in poi, intenderò il termine cifrario a blocchi nel senso più generale a meno che non sia specificato diversamente.

La discussione sulla modalità OFB nella sezione precedente solleva anche un altro punto interessante. Alcuni cifrari a flusso sono costruiti da cifrari a blocchi, come Rijndael con OFB. Alcuni come Salsa20 e ChaCha non sono creati da cifrari a blocchi. Potreste chiamare questi ultimi **cifrari a flusso primitivi**. (Non esiste davvero un termine standardizzato per riferirsi a tali cifrari a flusso.)

Quando le persone parlano dei vantaggi e degli svantaggi dei cifrari a flusso e dei cifrari a blocchi, stanno tipicamente confrontando cifrari a flusso primitivi con schemi di crittografia basati su cifrari a blocchi.

Mentre potete sempre facilmente costruire un cifrario a flusso da un cifrario a blocchi, è tipicamente molto difficile costruire qualche tipo di costrutto con una modalità di crittografia a blocchi (come con la modalità CBC) da un cifrario a flusso primitivo.

Da questa discussione, dovreste ora comprendere la *Figura 8*. Fornisce una panoramica sugli schemi di crittografia simmetrica. Utilizziamo tre tipi di schemi di crittografia: cifrari a flusso primitivi, cifrari a flusso basati su cifrari a blocchi e cifrari a blocchi in una modalità a blocchi (chiamati anche "cifrari a blocchi" nel diagramma).

*Figura 8: Panoramica degli schemi di crittografia simmetrica*

![Figura 8: Panoramica degli schemi di crittografia simmetrica](assets/Figure4-8.webp "Figura 8: Panoramica degli schemi di crittografia simmetrica")

## Codici di autenticazione dei messaggi
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>
La crittografia si occupa di segretezza. Ma si occupa anche di temi più ampi, come l'integrità del messaggio, l'autenticità e la non ripudiabilità. I cosiddetti **codici di autenticazione dei messaggi** (MAC) sono schemi crittografici a chiave simmetrica che supportano l'autenticità e l'integrità nelle comunicazioni.

Perché è necessario qualcosa oltre alla segretezza nella comunicazione? Supponiamo che Bob invii ad Alice un messaggio utilizzando una crittografia praticamente infrangibile. Qualsiasi attaccante che intercetti questo messaggio non sarà in grado di ottenere informazioni significative riguardo al contenuto. Tuttavia, l'attaccante ha comunque almeno due altri vettori di attacco disponibili:

1. Potrebbe intercettare il testo cifrato, alterarne il contenuto e inviare il testo cifrato modificato ad Alice.
2. Potrebbe bloccare completamente il messaggio di Bob e inviare il proprio testo cifrato creato.

In entrambi questi casi, l'attaccante potrebbe non avere alcuna intuizione sui contenuti dai testi cifrati (1) e (2). Ma potrebbe comunque causare danni significativi in questo modo. Qui diventano importanti i codici di autenticazione dei messaggi.

I codici di autenticazione dei messaggi sono definiti in modo non rigoroso come schemi crittografici simmetrici con tre algoritmi: un algoritmo di generazione della chiave, un algoritmo di generazione del tag e un algoritmo di verifica. Un MAC sicuro garantisce che i tag siano **esistenzialmente infalsificabili** per qualsiasi attaccante, ovvero, non possono creare con successo un tag sul messaggio che verifica, a meno che non abbiano la chiave privata.

Bob e Alice possono combattere la manipolazione di un messaggio particolare usando un MAC. Supponiamo per un momento che a loro non importi della segretezza. Vogliono solo assicurarsi che il messaggio ricevuto da Alice sia effettivamente di Bob e non sia stato modificato in alcun modo.

Il processo è rappresentato nella *Figura 9*. Per utilizzare un MAC, genererebbero prima una chiave privata K condivisa tra loro. Bob crea un tag T per il messaggio utilizzando la chiave privata K. Poi, invia il messaggio così come il tag del messaggio ad Alice. Lei può, quindi, verificare che Bob abbia effettivamente creato il tag, eseguendo la chiave privata, il messaggio e il tag attraverso un algoritmo di verifica.

*Figura 9: Panoramica degli schemi di crittografia simmetrica*

![Figura 9: Panoramica degli schemi di crittografia simmetrica](assets/Figure4-9.webp "Figura 9: Panoramica degli schemi di crittografia simmetrica")

A causa dell'infalsificabilità esistenziale, un attaccante non può alterare il messaggio M in alcun modo o creare un proprio messaggio con un tag valido. Questo è così, anche se l'attaccante osserva i tag di molti messaggi tra Bob e Alice che usano la stessa chiave privata. Al massimo, un attaccante potrebbe impedire ad Alice di ricevere il messaggio M (un problema che la crittografia non può affrontare).

Un MAC garantisce che un messaggio sia stato effettivamente creato da Bob. Questa autenticità implica automaticamente l'integrità del messaggio, ovvero, se Bob ha creato un certo messaggio, allora, di fatto, non è stato alterato in alcun modo da un attaccante. Quindi, d'ora in poi, qualsiasi preoccupazione per l'autenticazione dovrebbe essere automaticamente intesa come una preoccupazione per l'integrità.

Sebbene abbia tracciato una distinzione tra autenticità e integrità del messaggio nella mia discussione, è anche comune usare questi termini come sinonimi. Si riferiscono, quindi, all'idea di messaggi che sono stati sia creati da un mittente particolare che non alterati in alcun modo. In questo spirito, i codici di autenticazione dei messaggi sono spesso chiamati anche **codici di integrità dei messaggi**.

## Crittografia autenticata
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>
Tipicamente, si desidera garantire sia la segretezza che l'autenticità nella comunicazione e, pertanto, gli schemi di crittografia e gli schemi MAC vengono solitamente utilizzati insieme. Uno **schema di crittografia autenticata** è uno schema che combina la crittografia con un MAC in modo altamente sicuro. Specificamente, deve soddisfare gli standard per l'infalsificabilità esistenziale così come una nozione molto forte di segretezza, ovvero una che sia resistente agli **attacchi a testo cifrato scelto**.

Affinché uno schema di crittografia sia resistente agli attacchi a testo cifrato scelto, deve soddisfare gli standard per la **non-malleabilità**: ciò significa che qualsiasi modifica di un testo cifrato da parte di un attaccante dovrebbe produrre o un testo cifrato non valido o uno che, una volta decifrato, non ha alcuna relazione con l'originale.

Poiché uno schema di crittografia autenticata garantisce che un testo cifrato creato da un attaccante sia sempre invalido (poiché il tag non verrà verificato), soddisfa gli standard per la resistenza agli attacchi a testo cifrato scelto. È interessante notare che si può dimostrare che uno schema di crittografia autenticata può sempre essere creato dalla combinazione di un MAC infalsificabile esistenzialmente e uno schema di crittografia che soddisfa una nozione di sicurezza meno forte, nota come sicurezza da **attacchi a testo in chiaro scelto**.

Non entreremo in tutti i dettagli della costruzione degli schemi di crittografia autenticata. Ma è importante conoscere due dettagli della loro costruzione.

Primo, uno schema di crittografia autenticata gestisce prima la crittografia e poi crea un tag del messaggio sul testo cifrato. Si è scoperto che altri approcci, come combinare il testo cifrato con un tag sul testo in chiaro, o creare prima un tag e poi crittografare sia il testo in chiaro che il tag, sono insicuri. Inoltre, entrambe le operazioni hanno la propria chiave privata selezionata casualmente, altrimenti la tua sicurezza è gravemente compromessa.

Il principio sopra menzionato si applica più in generale: *si dovrebbero sempre utilizzare chiavi distinte quando si combinano schemi crittografici di base*.

Uno schema di crittografia autenticata è rappresentato nella *Figura 10*. Bob crea prima un testo cifrato C dal messaggio M utilizzando una chiave K<sub>C</sub> selezionata casualmente. Poi, crea un tag del messaggio T eseguendo il testo cifrato e una diversa chiave K<sub>T</sub> selezionata casualmente attraverso l'algoritmo di generazione del tag. Sia il testo cifrato che il tag del messaggio vengono inviati ad Alice.

Alice ora verifica prima se il tag è valido dato il testo cifrato C e la chiave K<sub>T</sub>. Se valido, può poi decifrare il messaggio usando la chiave K<sub>C</sub>. Non solo le è assicurata una nozione molto forte di segretezza nelle loro comunicazioni, ma sa anche che il messaggio è stato creato da Bob.

*Figura 10: Uno schema di crittografia autenticata*

Come vengono creati i MAC? Sebbene i MAC possano essere creati tramite vari metodi, un modo comune ed efficiente per crearli è tramite funzioni hash crittografiche.

Introdurremo le funzioni hash crittografiche più approfonditamente nel *Capitolo 6*. Per ora, sappi solo che una **funzione hash** è una funzione computazionalmente efficiente che prende input di dimensione arbitraria e produce output di lunghezza fissa. Ad esempio, la popolare funzione hash **SHA-256** (secure hash algorithm 256) genera sempre un output di 256 bit indipendentemente dalla dimensione dell'input. Alcune funzioni hash, come SHA-256, hanno applicazioni utili in crittografia.
Il tipo più comune di tag prodotto con una funzione di hash crittografico è il **codice di autenticazione del messaggio basato su hash** (HMAC). Il processo è illustrato nella *Figura 11*. Una parte produce due chiavi distinte da una chiave privata K, la chiave interna K<sub>1</sub> e la chiave esterna K<sub>2</sub>. Il testo in chiaro M o il testo cifrato C viene quindi hashato insieme alla chiave interna. Il risultato T' viene poi hashato con la chiave esterna per produrre il tag del messaggio T.
Esiste una gamma di funzioni di hash che possono essere utilizzate per creare un HMAC. La funzione di hash più comunemente impiegata è SHA-256.

*Figura 11: HMAC*

![Figura 11: HMAC](assets/Figure4-11.webp "Figura 11: HMAC")

## Sessioni di comunicazione sicure
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Supponiamo che due parti siano in una sessione di comunicazione, quindi inviano più messaggi avanti e indietro.

Uno schema di crittografia autenticata consente al destinatario di un messaggio di verificare che sia stato creato dal suo partner nella sessione di comunicazione (purché la chiave privata non sia stata divulgata). Questo funziona abbastanza bene per un singolo messaggio. Tipicamente, tuttavia, due parti inviano messaggi avanti e indietro in una sessione di comunicazione. E in quel contesto, uno schema di crittografia autenticata semplice, come descritto nella sezione precedente, non è sufficiente a garantire la sicurezza.

Il motivo principale è che uno schema di crittografia autenticata non fornisce alcuna garanzia che il messaggio sia stato effettivamente inviato anche dall'agente che lo ha creato all'interno di una sessione di comunicazione. Considerate i seguenti tre vettori di attacco:

1. **Attacco di replay**: Un attaccante reinvia un testo cifrato e un tag che ha intercettato tra due parti in un momento precedente.
2. **Attacco di riordinamento**: Un attaccante intercetta due messaggi in momenti diversi e li invia al destinatario nell'ordine inverso.
3. **Attacco di riflessione**: Un attaccante osserva un messaggio inviato da A a B e invia anche quel messaggio ad A.

Sebbene l'attaccante non abbia conoscenza del testo cifrato e non possa creare testi cifrati falsificati, gli attacchi sopra menzionati possono comunque causare danni significativi nelle comunicazioni.

Supponiamo, ad esempio, che un particolare messaggio tra le due parti coinvolga il trasferimento di fondi finanziari. Un attacco di replay potrebbe trasferire i fondi una seconda volta. Uno schema di crittografia autenticata semplice non ha difese contro tali attacchi.

Fortunatamente, questi tipi di attacchi possono essere facilmente mitigati in una sessione di comunicazione utilizzando **identificatori** e **indicatori di tempo relativi**.

Gli identificatori possono essere aggiunti al messaggio in chiaro prima della crittografia. Questo impedirebbe qualsiasi attacco di riflessione. Un indicatore di tempo relativo può, ad esempio, essere un numero di sequenza in una particolare sessione di comunicazione. Ogni parte aggiunge un numero di sequenza a un messaggio prima della crittografia, così il destinatario sa in che ordine i messaggi sono stati inviati. Questo elimina la possibilità di attacchi di riordinamento. Elimina anche gli attacchi di replay. Qualsiasi messaggio che un attaccante invia in seguito avrà un numero di sequenza vecchio, e il destinatario saprà di non dover elaborare di nuovo il messaggio.

Per illustrare come funzionano le sessioni di comunicazione sicure, supponiamo ancora una volta Alice e Bob. Inviano un totale di quattro messaggi avanti e indietro. Potete vedere come uno schema di crittografia autenticata con identificatori e numeri di sequenza funzionerebbe di seguito nella *Figura 11*.
La sessione di comunicazione inizia con Bob che invia ad Alice un testo cifrato C<sub>0,B</sub> con un tag del messaggio T<sub>0,B</sub>. Il testo cifrato contiene il messaggio, così come un identificatore (BOB) e un numero di sequenza (0). Il tag T<sub>0,B</sub> è creato sull'intero testo cifrato. Nelle loro comunicazioni successive, Alice e Bob mantengono questo protocollo, aggiornando i campi secondo necessità.
*Figura 12: Una sessione di comunicazione sicura*

![Figura 12: Una sessione di comunicazione sicura](assets/Figure4-12.webp "Figura 12: Una sessione di comunicazione sicura")

## Note
<chapterId>b96d38dd-c9cb-56a7-8764-4af8526bc63f</chapterId>

[^1]: Secondo Svetonio, un cifrario a sostituzione con una chiave costante di valore 3 fu utilizzato da Giulio Cesare nelle sue comunicazioni militari. Quindi A diventava sempre D, B sempre E, C sempre F, e così via. Questa particolare versione del cifrario a sostituzione è, quindi, diventata nota come **Cifrario di Cesare** (anche se non è realmente un cifrario nel senso moderno della parola, poiché il valore della chiave è costante). Il cifrario di Cesare potrebbe essere stato sicuro nel primo secolo a.C., se i nemici di Roma fossero stati molto poco familiari con la crittografia. Ma chiaramente non sarebbe uno schema molto sicuro nei tempi moderni [^1].

[^2]: Jonathan Katz e Yehuda Lindell, *Introduzione alla Crittografia Moderna*, CRC Press (Boca Raton, FL: 2015), p. 7f [^2].

[^3]: Eric Raymond, “La Cattedrale e il Bazar,” il documento è stato presentato al Linux Kongress, Würzburg, Germania (27 Maggio 1997). Ci sono numerose versioni successive disponibili così come un libro. Le mie citazioni provengono dalla pagina 30 del libro: Eric Raymond, *La Cattedrale e il Bazar: Riflessioni su Linux e Open Source da un Rivoluzionario per Caso*, edizione rivista (2001), O’Reilly: Sebastopol, CA [^3].

[^4]: Crypto Museum, "Linea diretta Washington-Mosca," 2013, disponibile su [Crypto Museum](https://www.cryptomuseum.com/crypto/hotline/index.htm) [^4].

[^5]: L'importanza della crittografia probabilistica è stata sottolineata per la prima volta da Shafi Goldwasser e Silvio Micali, “Crittografia probabilistica,” *Journal of Co [^5].

# RC4 e AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

In questo capitolo, discuteremo i dettagli di uno schema di crittografia con un moderno cifrario a flusso primitivo, RC4 (o "cifrario Rivest 4"), e un moderno cifrario a blocchi, AES. Mentre il cifrario RC4 è caduto in disgrazia come metodo di crittografia, AES è lo standard per la crittografia simmetrica moderna. Questi due esempi dovrebbero fornire un'idea migliore di come funziona sotto il cofano la crittografia simmetrica.
Per comprendere il funzionamento dei moderni cifrari a flusso pseudocasuale, mi concentrerò sul cifrario a flusso RC4. Si tratta di un cifrario a flusso pseudocasuale che è stato utilizzato nei protocolli di sicurezza per punti di accesso wireless WEP e WAP, così come in TLS. Poiché RC4 presenta molte debolezze dimostrate, è caduto in disgrazia. Infatti, l'Internet Engineering Task Force ora vieta l'uso delle suite RC4 da parte delle applicazioni client e server in tutte le istanze di TLS.<sup>[3](#footnote3)</sup> Tuttavia, funziona bene come esempio per illustrare come funziona un cifrario a flusso primitivo.
Per iniziare, mostrerò prima come cifrare un messaggio in chiaro con un cifrario RC4 semplificato. Supponiamo che il nostro messaggio in chiaro sia "SOUP". La cifratura con il nostro cifrario RC4 semplificato, quindi, procede in quattro passaggi.

### Passo 1

Prima, definire un array S con S[0] = 0 fino a S[7] = 7. Un array qui significa semplicemente una collezione mutabile di valori organizzati da un indice, chiamato anche lista in alcuni linguaggi di programmazione (ad esempio, Python). In questo caso, l'indice va da 0 a 7, e i valori vanno anch'essi da 0 a 7. Quindi S è come segue:

- S = [0,1,2,3,4,5,6,7]

I valori qui non sono numeri ASCII, ma le rappresentazioni del valore decimale di stringhe di 1 byte. Quindi il valore 2 sarebbe uguale a 0000 0011. La lunghezza dell'array S è, quindi, di 8 byte.

### Passo 2

Secondo, definire un array chiave K di lunghezza di 8 byte scegliendo una chiave tra 1 e 8 byte (senza frazioni di byte permesse). Poiché ogni byte è di 8 bit, è possibile selezionare qualsiasi numero tra 0 e 255 per ogni byte della chiave.

Supponiamo di scegliere la nostra chiave k come [14,48,9], in modo che abbia una lunghezza di 3 byte. Ogni indice del nostro array chiave è, quindi, impostato secondo il valore decimale per quel particolare elemento della chiave, in ordine. Se si esaurisce l'intera chiave, si ricomincia dall'inizio, fino a riempire gli 8 slot dell'array chiave. Quindi, il nostro array chiave è come segue

- K = [14,48,9,14,48,9,14,48]

### Passo 3

Terzo, trasformeremo l'array S utilizzando l'array chiave K, in un processo noto come programmazione della chiave. Il processo è il seguente in pseudocodice:

- Creare le variabili j e i
- Impostare la variabile j = 0
- Per ogni i da 0 a 7:
	- Impostare j = j + S[i] + K[i] mod 8
	- Scambiare S[i] e S[j]

La trasformazione dell'array S è catturata dalla *Tabella 1*.

Per iniziare, si può vedere lo stato iniziale di S come [0,1,2,3,4,5,6,7] con un valore iniziale di 0 per j. Questo sarà trasformato utilizzando l'array chiave [14,48,9,14,48,9,14,48].
Il ciclo for inizia con i = 0. Secondo il nostro pseudocodice sopra, il nuovo valore di j diventa 6 (j = j + S[0] + K[0] mod 8 = 0 + 0 + 14 mod 8 = 6 mod 8). Scambiando S[0] con S[6], lo stato di S dopo 1 round diventa [6,1,2,3,4,5,0,7]. 
Nella riga successiva, i = 1. Passando nuovamente attraverso il ciclo for, j ottiene un valore di 7 (j = j + S[1] + K[1] mod 8 = 6 + 1 + 48 mod 8 = 55 mod 8 = 7 mod 8). Scambiando S[1] con S[7] dallo stato corrente di S, [6,1,2,3,4,5,0,7], si ottiene [6,7,2,3,4,5,0,1] dopo il round 2.

Continuiamo con questo processo fino a produrre la riga finale in fondo per l'array S, [6,4,1,0,3,7,5,2].

*Tabella 1: Tabella di pianificazione delle chiavi*

![Tabella 1: Tabella di pianificazione delle chiavi](assets/Table5-1.webp "Tabella 1: Tabella di pianificazione delle chiavi")

### Passo 4

Come quarto passo, produciamo il keystream. Questa è la stringa pseudocasuale di lunghezza uguale al messaggio che vogliamo inviare. Questo sarà utilizzato per criptare il messaggio originale "SOUP". Poiché il keystream deve essere lungo quanto il messaggio, abbiamo bisogno di uno che abbia 4 byte.

Il keystream è prodotto dal seguente pseudocodice:

- Creare le variabili j, i e t
- Impostare j = 0
- Per ogni i del testo in chiaro, partendo da i = 1 e proseguendo fino a i = 4, ogni byte del keystream è prodotto come segue:
    - j = j + S[i] mod 8
	- Scambiare S[i] con S[j]
	- t = S[i] + S[j] mod 8
	- Il byte i-esimo del keystream = S[t]

Puoi seguire i calcoli nella *Tabella 2*.

Lo stato iniziale di S = S = [6,4,1,0,3,7,5,2]. Impostando i = 1, il valore j diventa 4 (j = j + S[i] mod 8 = 0 + 4 mod 8 = 4). Quindi, scambiamo S[1] con S[4] per produrre la trasformazione di S nella seconda riga, [6,3,1,0,4,7,5,2]. Il valore t è, quindi, 7 (t = S[i] + S[j] mod 8 = 3 + 4 mod 8 = 7). Infine, il byte per il keystream è, quindi, S[7], ovvero 2.

Possiamo, quindi, continuare a produrre gli altri byte fino ad avere i seguenti quattro byte: 2, 6, 3 e 7. Ognuno di questi byte può, quindi, essere utilizzato per criptare ogni lettera del testo in chiaro, "SOUP".
Per iniziare, utilizzando una tabella ASCII, possiamo vedere che "SOUP" codificato dai valori decimali delle stringhe di byte sottostanti è "83 79 85 80". La combinazione con il flusso di chiavi "2 6 3 2" produce "85 85 88 82", che rimane invariato dopo un'operazione modulo 256. In ASCII, il testo cifrato "85 85 88 82" equivale a "UUXR".
Cosa succede se la parola da cifrare fosse più lunga dell'array S? In tal caso, l'array S continua a trasformarsi in questo modo mostrato sopra per ogni byte i del testo in chiaro, fino ad avere un numero di byte nel flusso di chiavi uguale al numero di lettere nel testo in chiaro.

*Tabella 2: Generazione del flusso di chiavi*

![Tabella 2: Generazione del flusso di chiavi](assets/Table5-2.webp "Tabella 2: Generazione del flusso di chiavi")

L'esempio che abbiamo appena discusso è solo una versione semplificata del cifrario a flusso RC4. Il vero cifrario a flusso RC4 ha un array S di 256 byte di lunghezza, non 8 byte, e una chiave che può essere tra 1 e 256 byte, non tra 1 e 8 byte. L'array delle chiavi e i flussi di chiavi sono, quindi, tutti prodotti considerando la lunghezza di 256 byte dell'array S. I calcoli diventano immensamente più complessi, ma i principi rimangono gli stessi. Utilizzando la stessa chiave, [14,48,9], con il cifrario RC4 standard, il messaggio in chiaro "SOUP" viene cifrato come 67 02 ed df in formato esadecimale.

Un cifrario a flusso in cui il flusso di chiavi si aggiorna indipendentemente dal messaggio in chiaro o dal testo cifrato è un **cifrario a flusso sincrono**. Il flusso di chiavi dipende solo dalla chiave. Chiaramente, RC4 è un esempio di cifrario a flusso sincrono, poiché il flusso di chiavi non ha alcuna relazione con il testo in chiaro o con il testo cifrato. Tutti i nostri cifrari a flusso primitivi menzionati nel capitolo precedente, inclusi il cifrario di Cesare, il cifrario di Vigenère e il one-time pad, erano anch'essi di tipo sincrono.

Al contrario, un **cifrario a flusso asincrono** ha un flusso di chiavi che è prodotto sia dalla chiave che dagli elementi precedenti del testo cifrato. Questo tipo di cifrario è anche chiamato **cifrario auto-sincronizzante**.

È importante che il flusso di chiavi prodotto con RC4 sia trattato come un one-time pad, e non è possibile produrre il flusso di chiavi esattamente nello stesso modo la prossima volta. Piuttosto che cambiare la chiave ogni volta, la soluzione pratica è combinare la chiave con un nonce per produrre il flusso di byte.

## AES con una chiave a 128 bit
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Come menzionato nel capitolo precedente, il National Institute of Standards and Technology (NIST) ha tenuto una competizione tra il 1997 e il 2000 per determinare un nuovo standard di cifratura simmetrica. Il cifrario Rijndael si è rivelato essere la proposta vincente. Il nome è un gioco di parole sui nomi dei creatori belgi, Vincent Rijmen en Joan Daemen.

Il cifrario Rijndael è un cifrario a blocchi, il che significa che esiste un algoritmo centrale, che può essere utilizzato con diverse specifiche per lunghezze di chiave e dimensioni di blocco. È possibile, quindi, utilizzarlo con diverse modalità di funzionamento per costruire schemi di cifratura.
Il comitato per la competizione NIST ha adottato una versione ristretta del cifrario Rijndael, ovvero una che richiede dimensioni di blocco di 128 bit e lunghezze della chiave di 128 bit, 192 bit o 256 bit, come parte dello standard di crittografia avanzata. Questa versione ristretta del cifrario Rijndael può anche essere utilizzata in molteplici modalità di funzionamento. La specifica per lo standard è ciò che è noto come lo Standard di Crittografia Avanzato (AES).

Per mostrare come funziona il cifrario Rijndael, il nucleo dell'AES, illustrerò il processo di crittografia con una chiave di 128 bit. La dimensione della chiave ha un impatto sul numero di round tenuti per ogni blocco di crittografia. Per le chiavi di 128 bit, sono richiesti 10 round. Con 192 bit e 256 bit, sarebbero stati rispettivamente 12 e 14 round.

Inoltre, assumerò che l'AES sia utilizzato in modalità ECB. Questo rende l'esposizione leggermente più semplice e non ha importanza per l'algoritmo Rijndael. Per essere sicuri, la modalità ECB non è sicura nella pratica perché porta a una crittografia deterministica. La modalità sicura più comunemente utilizzata con l'AES è CBC.

Chiamiamo la chiave K<sub>0</sub>. La costruzione con i parametri sopra indicati, quindi, appare come in Figura 1, dove M<sub>i</sub> rappresenta una parte del messaggio in chiaro di 128 bit e C<sub>i</sub> una parte del testo cifrato di 128 bit. Un padding viene aggiunto al messaggio in chiaro per l'ultimo blocco, se il messaggio in chiaro non può essere diviso equamente per la dimensione del blocco.

*Figura 1: AES-ECB con una chiave di 128 bit*

![Figura 1: AES-ECB con una chiave di 128 bit](assets/Figure5-1.webp "Figura 1: AES-ECB con una chiave di 128 bit")

Ogni blocco di testo di 128 bit passa attraverso dieci round nello schema di crittografia Rijndael. Questo richiede una chiave di round separata per ogni round (K<sub>1</sub> fino a K<sub>10</sub>). Queste sono prodotte per ogni round dalla chiave originale di 128 bit K<sub>0</sub> utilizzando un algoritmo di espansione della chiave. Quindi, per ogni blocco di testo da crittografare, useremo la chiave originale K<sub>0</sub> così come dieci chiavi di round separate. Nota che queste stesse 11 chiavi sono utilizzate per ogni blocco di 128 bit di testo in chiaro che richiede la crittografia.

L'algoritmo di espansione della chiave è lungo e complesso. Approfondirlo ha pochi benefici didattici. Puoi esaminare l'algoritmo di espansione della chiave per conto tuo, se lo desideri. Una volta che le chiavi di round sono prodotte, il cifrario Rijndael manipolerà il primo blocco di 128 bit del testo in chiaro, M<sub>1</sub>, come visto in Figura 2. Ora passeremo attraverso questi passaggi.

*Figura 2: La manipolazione di M<sub>1</sub> con il cifrario Rijndael*

![Figura 2: AES-ECB con una chiave di 128 bit](assets/Figure5-2.webp "Figura 2: AES-ECB con una chiave di 128 bit")

### Round 0

Il Round 0 del cifrario Rijndael è semplice. Viene prodotto un array S<sub>0</sub> tramite un'operazione XOR tra il testo in chiaro di 128 bit e la chiave privata. Ovvero,

- S<sub>0</sub> = M<sub>1</sub> XOR K<sub>0</sub>
Nel round 1, l'array S<sub>0</sub> viene prima combinato con la chiave di round K<sub>1</sub> utilizzando un'operazione XOR. Questo produce un nuovo stato di S.
In secondo luogo, viene eseguita l'operazione di sostituzione dei byte sullo stato corrente di S. Funziona prendendo ogni byte dell'array S da 16 byte e sostituendolo con un byte di un array chiamato **Rijndael’s S-box**. Ogni byte ha una trasformazione unica, e come risultato viene prodotto un nuovo stato di S. La S-box di Rijndael è mostrata in *Figura 3*.

*Figura 3: S-Box di Rijndael*

![Figura 3: S-Box di Rijndael](assets/Figure5-3.webp "Figura 3: S-Box di Rijndael")

Questa S-Box è uno dei punti in cui l'algebra astratta entra in gioco nel cifrario di Rijndael, specificamente i campi di Galois.

Per iniziare, si definisce ogni possibile elemento byte da 00 a FF come un vettore a 8 bit. Ogni tale vettore è un elemento del campo di Galois GF(2<sup>8</sup>) dove il polinomio irriducibile per l'operazione modulo è x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Il campo di Galois con queste specifiche è chiamato anche Campo Finito di Rijndael.

Successivamente, per ogni possibile elemento nel campo creiamo quello che viene chiamato la **Nyberg S-Box**. In questa box, ogni byte è mappato sul suo inverso moltiplicativo (cioè, in modo che il loro prodotto sia uguale a 1). Mappiamo poi questi valori dalla S-box di Nyberg alla S-Box di Rijndael usando la trasformazione affine.

La terza operazione sull'array S è l'operazione di shift delle righe. Prende lo stato di S e elenca tutti i sedici byte in una matrice. Il riempimento della matrice inizia in alto a sinistra e procede girando dall'alto verso il basso e poi, ogni volta che una colonna è riempita, spostandosi di una colonna a destra e verso l'alto.

Una volta che la matrice di S è stata costruita, le quattro righe vengono spostate. La prima riga rimane uguale. La seconda riga si sposta di uno verso sinistra. La terza si sposta di due verso sinistra. La quarta si sposta di tre verso sinistra. Un esempio del processo è fornito in *Figura 4*. Lo stato originale di S è mostrato in alto, lo stato risultante dopo l'operazione di shift delle righe è mostrato sotto.

*Figura 4: Operazione di shift delle righe*

![Figura 4: Operazione di shift delle righe](assets/Figure5-4.webp "Figura 4: Operazione di shift delle righe")

Nel quarto passaggio, i campi di Galois fanno nuovamente la loro comparsa. Per iniziare, ogni colonna della matrice S viene moltiplicata per la colonna della matrice 4 x 4 vista in *Figura 5*. Ma invece di essere una moltiplicazione di matrici regolare, è una moltiplicazione vettoriale modulo un polinomio irriducibile, x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. I coefficienti vettoriali risultanti rappresentano i bit individuali di un byte.

*Figura 5: Matrice di mix delle colonne*

![Figura 5: Matrice di mix delle colonne](assets/Figure5-5.webp "Figura 5: Matrice di mix delle colonne")

La moltiplicazione della prima colonna della matrice S con la matrice 4 x 4 sopra riportata produce il risultato in *Figura 6*.
*Figura 6: Moltiplicazione della prima colonna*
![Figura 6: Moltiplicazione della prima colonna](assets/Figure5-6.webp "Figura 6: Moltiplicazione della prima colonna")

Come passo successivo, tutti i termini nella matrice devono essere trasformati in polinomi. Per esempio, F1 rappresenta 1 byte e diventerebbe x<sup>7</sup> + x<sup>6</sup> + x<sup>5</sup> + x<sup>4</sup> + 1 e 03 rappresenta 1 byte e diventerebbe x + 1.

Tutte le moltiplicazioni sono quindi eseguite modulo x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Questo risulta nell'aggiunta di quattro polinomi in ciascuna delle quattro celle della colonna. Dopo aver eseguito queste addizioni modulo 2, si otterranno quattro polinomi. Ognuno di questi polinomi rappresenta una stringa di 8 bit, o 1 byte, di S. Non eseguiremo tutti questi calcoli qui sulla matrice nella *Figura 6* poiché sono estensivi.

Una volta che la prima colonna è stata elaborata, le altre tre colonne della matrice S vengono elaborate nello stesso modo. Eventualmente ciò produrrà una matrice con sedici byte che può essere trasformata in un array.

Come passo finale, l'array S viene combinato nuovamente con la chiave di round in un'operazione XOR. Questo produce lo stato S<sub>1</sub>. Ovvero,

- S<sub>1</sub> = S XOR K<sub>0</sub>

### Round dal 2 al 10

I round dal 2 al 9 sono semplicemente una ripetizione del round 1, *mutatis mutandis*. L'ultimo round appare molto simile ai round precedenti, eccetto che il passaggio di mix delle colonne viene eliminato. Ovvero, il round 10 viene eseguito come segue:

- S<sub>9</sub> XOR K<sub>10</sub>
- Sostituzione dei Byte
- Scambio delle Righe
- S<sub>10</sub> = S XOR K<sub>10</sub>

Lo stato S<sub>10</sub> è ora impostato su C<sub>1</sub>, i primi 128 bit del testo cifrato. Procedendo attraverso i rimanenti blocchi di testo in chiaro da 128 bit si ottiene il testo cifrato completo C.

### Le operazioni del cifrario di Rijndael

Qual è il ragionamento dietro le diverse operazioni viste nel cifrario di Rijndael?

Senza entrare nei dettagli, gli schemi di crittografia sono valutati sulla base della misura in cui creano confusione e diffusione. Se lo schema di crittografia ha un alto grado di **confusione**, significa che il testo cifrato appare drasticamente diverso dal testo in chiaro. Se lo schema di crittografia ha un alto grado di **diffusione**, significa che qualsiasi piccola modifica al testo in chiaro produce un testo cifrato drasticamente diverso.

Il ragionamento per le operazioni dietro il cifrario di Rijndael è che producono entrambi un alto grado di confusione e diffusione. La confusione è prodotta dall'operazione di sostituzione dei byte, mentre la diffusione è prodotta dalle operazioni di scambio delle righe e mix delle colonne.

# Crittografia Asimmetrica
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

Come con la crittografia simmetrica, gli schemi asimmetrici possono essere utilizzati per garantire sia la segretezza che l'autenticazione. Tuttavia, a differenza di questi, tali schemi impiegano due chiavi anziché una: una privata e una pubblica.
Iniziamo la nostra indagine con la scoperta della crittografia asimmetrica, in particolare i problemi che l'hanno stimolata. Successivamente, discutiamo come funzionano a livello alto i sistemi asimmetrici per la cifratura e l'autenticazione. Introduciamo poi le funzioni hash, che sono fondamentali per comprendere i sistemi di autenticazione asimmetrici, e hanno anche rilevanza in altri contesti crittografici, come per i codici di autenticazione dei messaggi basati su hash discussi nel Capitolo 4.

## Il problema della distribuzione e gestione delle chiavi
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Supponiamo che Bob voglia comprare un nuovo impermeabile da Jim’s Sporting Goods, un rivenditore di articoli sportivi online con milioni di clienti in Nord America. Questo sarà il suo primo acquisto da loro e vuole usare la sua carta di credito. Quindi, Bob dovrà prima creare un account con Jim’s Sporting Goods, il che richiede l'invio di dettagli personali come il suo indirizzo e le informazioni della carta di credito. Potrà poi procedere con i passaggi necessari per acquistare l'impermeabile.

Bob e Jim’s Sporting Goods vorranno assicurarsi che le loro comunicazioni siano sicure durante questo processo, considerando che Internet è un sistema di comunicazione aperto. Vorrebbero assicurarsi, ad esempio, che nessun potenziale attaccante possa venire a conoscenza dei dettagli della carta di credito e dell'indirizzo di Bob, e che nessun potenziale attaccante possa ripetere i suoi acquisti o crearne di falsi per suo conto.

Un avanzato schema di cifratura autenticata come discusso nel capitolo precedente potrebbe certamente rendere sicure le comunicazioni tra Bob e Jim’s Sporting Goods. Ma ci sono chiaramente ostacoli pratici all'implementazione di tale schema.

Per illustrare questi ostacoli pratici, supponiamo di vivere in un mondo in cui esistono solo gli strumenti della crittografia simmetrica. Cosa potrebbero fare Jim’s Sporting Goods e Bob, quindi, per garantire una comunicazione sicura?

In queste circostanze, si troverebbero di fronte a costi sostanziali per comunicare in modo sicuro. Poiché Internet è un sistema di comunicazione aperto, non possono semplicemente scambiarsi un insieme di chiavi attraverso di esso. Quindi, Bob e un rappresentante di Jim’s Sporting Goods dovrebbero effettuare uno scambio di chiavi di persona.

Una possibilità è che Jim’s Sporting Goods crei delle posizioni speciali per lo scambio di chiavi, dove Bob e altri nuovi clienti possono recuperare un insieme di chiavi per una comunicazione sicura. Questo comporterebbe ovviamente costi organizzativi sostanziali e ridurrebbe notevolmente l'efficienza con cui i nuovi clienti possono effettuare acquisti.

In alternativa, Jim’s Sporting Goods può inviare a Bob una coppia di chiavi tramite un corriere di alta fiducia. Questo è probabilmente più efficiente dell'organizzare luoghi di scambio di chiavi. Ma comporterebbe comunque costi sostanziali, in particolare se molti clienti effettuano solo uno o pochi acquisti.

Inoltre, uno schema simmetrico per la cifratura autenticata costringe anche Jim’s Sporting Goods a conservare set separati di chiavi per tutti i loro clienti. Questa sarebbe una sfida pratica significativa per migliaia di clienti, figuriamoci per milioni.

Per comprendere quest'ultimo punto, supponiamo che Jim’s Sporting Goods fornisca a ogni cliente la stessa coppia di chiavi. Questo permetterebbe a ogni cliente - o a chiunque altro potesse ottenere questa coppia di chiavi - di leggere e persino manipolare tutte le comunicazioni tra Jim’s Sporting Goods e i suoi clienti. Potresti, quindi, anche non usare affatto la crittografia nelle tue comunicazioni.

Anche ripetere un insieme di chiavi solo per alcuni clienti è una pessima pratica di sicurezza. Qualsiasi potenziale attaccante potrebbe tentare di sfruttare questa caratteristica dello schema (ricordiamo che si presume che gli attaccanti sappiano tutto di uno schema tranne le chiavi, in conformità con il principio di Kerckhoffs.)

Quindi, Jim’s Sporting Goods dovrebbe conservare una coppia di chiavi per ogni cliente, indipendentemente da come queste coppie di chiavi vengano distribuite. Questo presenta chiaramente diversi problemi pratici.

- Jim’s Sporting Goods dovrebbe conservare milioni di coppie di chiavi, un insieme per ogni cliente.
- Queste chiavi dovrebbero essere adeguatamente protette, poiché sarebbero un bersaglio certo per gli hacker. Qualsiasi violazione della sicurezza richiederebbe la ripetizione di costosi scambi di chiavi, sia presso apposite sedi di scambio di chiavi sia tramite corriere. - Qualsiasi cliente di Jim’s Sporting Goods dovrebbe conservare con cura una coppia di chiavi a casa. Si verificheranno perdite e furti, richiedendo una ripetizione degli scambi di chiavi. I clienti dovrebbero anche affrontare questo processo per qualsiasi altro negozio online o altri tipi di entità con cui desiderano comunicare e fare transazioni su Internet.

Queste due principali sfide appena descritte erano preoccupazioni molto fondamentali fino alla fine degli anni '70. Erano conosciute come il **problema della distribuzione delle chiavi** e il **problema della gestione delle chiavi**, rispettivamente.

Questi problemi erano sempre esistiti, ovviamente, e spesso causavano grattacapi in passato. Le forze militari, ad esempio, avrebbero dovuto costantemente distribuire libri con chiavi per la comunicazione sicura al personale sul campo a grandi rischi e costi. Ma questi problemi stavano peggiorando poiché il mondo si stava sempre più muovendo verso uno di comunicazione digitale a lunga distanza, in particolare per le entità non governative.

Se questi problemi non fossero stati risolti negli anni '70, lo shopping efficiente e sicuro presso Jim’s Sporting Goods probabilmente non sarebbe esistito. Infatti, gran parte del nostro mondo moderno con e-mail pratiche e sicure, banking online e shopping probabilmente sarebbe stato solo un lontano sogno. Qualcosa che assomiglia anche lontanamente a Bitcoin non avrebbe potuto esistere affatto.

Quindi, cosa è successo negli anni '70? Come è possibile che possiamo fare acquisti online all'istante e navigare in modo sicuro sul World Wide Web? Come è possibile che possiamo inviare istantaneamente Bitcoin in tutto il mondo dai nostri smartphone?

## Nuove direzioni nella crittografia
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

Negli anni '70, i problemi della distribuzione delle chiavi e della gestione delle chiavi avevano attirato l'attenzione di un gruppo di crittografi accademici americani: Whitfield Diffie, Martin Hellman e Ralph Merkle. Di fronte allo scetticismo severo della maggior parte dei loro colleghi, si avventurarono a ideare una soluzione.

Almeno una motivazione primaria per la loro impresa era la previsione che le comunicazioni informatiche aperte avrebbero profondamente influenzato il nostro mondo. Come Diffie e Hellman notano nel 1976,

> Lo sviluppo di reti di comunicazione controllate da computer promette contatti senza sforzo ed economici tra persone o computer su lati opposti del mondo, sostituendo la maggior parte della posta e molte escursioni con le telecomunicazioni. Per molte applicazioni, questi contatti devono essere resi sicuri sia contro l'intercettazione sia contro l'iniezione di messaggi illegittimi. Attualmente, tuttavia, la soluzione dei problemi di sicurezza è ben indietro rispetto ad altre aree della tecnologia delle comunicazioni. *La crittografia contemporanea è incapace di soddisfare i requisiti, in quanto il suo uso imporrebbe tali gravi inconvenienti agli utenti del sistema, da eliminare molti dei benefici della teleelaborazione.*<sup>[1](#footnote1)</sup>

La tenacia di Diffie, Hellman e Merkle ha dato i suoi frutti. La prima pubblicazione dei loro risultati fu un articolo di Diffie e Hellman nel 1976 intitolato “Nuove Direzioni nella Crittografia”. In esso, presentarono due modi originali per affrontare il problema della distribuzione delle chiavi e il problema della gestione delle chiavi.
La prima soluzione che hanno proposto era un *protocollo di scambio chiavi remoto*, ovvero, un insieme di regole per lo scambio di una o più chiavi simmetriche attraverso un canale di comunicazione non sicuro. Questo protocollo è ora conosciuto come *scambio di chiavi Diffie-Hellman* o *scambio di chiavi Diffie-Hellman-Merkle*.<sup>[2](#footnote2)</sup>
Con lo scambio di chiavi Diffie-Hellman, due parti scambiano prima alcune informazioni pubblicamente su un canale insicuro come Internet. Sulla base di queste informazioni, poi, creano indipendentemente una chiave simmetrica (o una coppia di chiavi simmetriche) per la comunicazione sicura. Sebbene entrambe le parti creino le loro chiavi indipendentemente, le informazioni che hanno condiviso pubblicamente assicurano che questo processo di creazione della chiave produca lo stesso risultato per entrambi.

Importante è che, mentre tutti possono osservare le informazioni che vengono scambiate pubblicamente dalle parti sul canale insicuro, solo le due parti coinvolte nello scambio di informazioni possono creare chiavi simmetriche da esse.

Questo, naturalmente, suona completamente controintuitivo. Come possono due parti scambiare alcune informazioni pubblicamente che permetteranno solo a loro di creare chiavi simmetriche da esse? Perché chiunque altro che osserva lo scambio di informazioni non sarebbe in grado di creare le stesse chiavi?

Si basa su alcuni bellissimi concetti matematici, ovviamente. Lo scambio di chiavi Diffie-Hellman funziona tramite una funzione unidirezionale con una botola. Discutiamo il significato di questi due termini a turno.

Supponiamo che ti venga data una funzione f(x) e il risultato f(a) = y, dove a è un valore particolare per x. Diciamo che f(x) è una **funzione unidirezionale** se è facile calcolare il valore y quando sono dati a e f(x), ma è computazionalmente impraticabile calcolare il valore a quando sono dati y e f(x). Il nome funzione unidirezionale, naturalmente, deriva dal fatto che tale funzione è pratica da calcolare solo in una direzione.

Alcune funzioni unidirezionali hanno quello che è noto come una botola. Mentre è praticamente impossibile calcolare a dato solo y e f(x), esiste un certo pezzo di informazione Z che rende il calcolo di a da y computazionalmente fattibile. Questo pezzo di informazione Z è noto come la **botola**. Le funzioni unidirezionali che hanno una botola sono note come **funzioni con botola**.

Non entreremo nei dettagli dello scambio di chiavi Diffie-Hellman qui. Ma essenzialmente ogni partecipante crea alcune informazioni, di cui una parte è condivisa pubblicamente e di cui alcune rimangono segrete. Ogni parte, poi, prende il loro pezzo di informazione segreta e l'informazione pubblica condivisa dall'altra parte per creare una chiave privata. E, in modo alquanto miracoloso, entrambe le parti finiranno per avere la stessa chiave privata.

Qualsiasi parte che osserva solo le informazioni condivise pubblicamente tra le due parti in uno scambio di chiavi Diffie-Hellman è incapace di replicare questi calcoli. Avrebbero bisogno delle informazioni private da una delle due parti per farlo.

Sebbene la versione base dello scambio di chiavi Diffie-Hellman presentata nel documento del 1976 non sia molto sicura, versioni sofisticate del protocollo base sono certamente ancora in uso oggi. Più importantemente, ogni protocollo di scambio chiavi nell'ultima versione del protocollo di sicurezza del livello di trasporto (versione 1.3) è essenzialmente una versione arricchita del protocollo presentato da Diffie e Hellman nel 1976. Il protocollo di sicurezza del livello di trasporto è il protocollo predominante per lo scambio sicuro di informazioni formattate secondo il protocollo di trasferimento ipertestuale (http), lo standard per lo scambio di contenuti Web.
È importante sottolineare che lo scambio di chiavi Diffie-Hellman non è uno schema asimmetrico. Parlando in termini stretti, potrebbe essere considerato appartenente al regno della crittografia a chiave simmetrica. Tuttavia, poiché sia lo scambio di chiavi Diffie-Hellman sia la crittografia asimmetrica si basano su funzioni numerico-teoriche unidirezionali con trappole, di solito vengono discussi insieme.
Il secondo metodo proposto da Diffie e Hellman per affrontare il problema della distribuzione e gestione delle chiavi nel loro articolo del 1976 era, naturalmente, tramite la crittografia asimmetrica.

A differenza della loro presentazione dello scambio di chiavi Diffie-Hellman, hanno fornito solo i contorni generali di come potrebbero essere plausibilmente costruiti schemi crittografici asimmetrici. Non hanno offerto alcuna funzione unidirezionale che potesse specificamente soddisfare le condizioni necessarie per una sicurezza ragionevole in tali schemi.

Tuttavia, l'implementazione pratica di uno schema asimmetrico fu trovata un anno dopo da tre diversi crittografi accademici e matematici: Ronald Rivest, Adi Shamir e Leonard Adleman. Il sistema crittografico che introdussero divenne noto come **sistema crittografico RSA** (dalle loro iniziali).

Le funzioni con trappola utilizzate nella crittografia asimmetrica (e nello scambio di chiavi Diffie-Hellman) sono tutte correlate a due principali **problemi computazionalmente difficili**: la fattorizzazione di numeri primi e il calcolo dei logaritmi discreti.

La **fattorizzazione di numeri primi** richiede, come suggerisce il nome, di scomporre un intero nei suoi fattori primi. Il problema RSA è di gran lunga l'esempio più noto di un sistema crittografico relativo alla fattorizzazione di numeri primi.

Il **problema del logaritmo discreto** è un problema che si verifica nei gruppi ciclici. Dato un generatore in un particolare gruppo ciclico, richiede il calcolo dell'esponente unico necessario per produrre un altro elemento nel gruppo a partire dal generatore.

Gli schemi basati sul logaritmo discreto si affidano a due principali tipi di gruppi ciclici: gruppi moltiplicativi di interi e gruppi che includono i punti sulle curve ellittiche. Lo scambio di chiavi Diffie-Hellman originale, come presentato in "New Directions in Cryptography", funziona con un gruppo moltiplicativo ciclico di interi. L'algoritmo di firma digitale di Bitcoin e il recentemente introdotto schema di firma Schnorr (2021) si basano entrambi sul problema del logaritmo discreto per un particolare gruppo ciclico di curve ellittiche.

Successivamente, passeremo a una panoramica ad alto livello della segretezza e dell'autenticazione nell'ambito asimmetrico. Prima di farlo, tuttavia, dobbiamo fare una breve nota storica.

Ora sembra plausibile che un gruppo di crittografi e matematici britannici che lavoravano per il Government Communications Headquarters (GCHQ) avesse fatto indipendentemente le scoperte sopra menzionate alcuni anni prima. Questo gruppo era composto da James Ellis, Clifford Cocks e Malcolm Williamson.

Secondo i loro racconti e quello del GCHQ, fu James Ellis a ideare per primo il concetto di crittografia a chiave pubblica nel 1969. Presumibilmente, Clifford Cocks scoprì poi il sistema crittografico RSA nel 1973, e Malcolm Williamson il concetto di scambio di chiavi Diffie-Hellman nel 1974. Le loro scoperte, tuttavia, non furono presumibilmente rivelate fino al 1997, data la natura segreta del lavoro svolto al GCHQ.

## Crittografia asimmetrica e autenticazione
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Una panoramica della crittografia asimmetrica con l'aiuto di Bob e Alice è fornita nella *Figura 1*.
Alice crea inizialmente una coppia di chiavi, composta da una chiave pubblica (K<sub>P</sub>) e una chiave privata (K<sub>S</sub>), dove il "P" in K<sub>P</sub> sta per "pubblica" e il "S" in K<sub>S</sub> per "segreta". Successivamente, distribuisce liberamente questa chiave pubblica ad altri. Torneremo sui dettagli di questo processo di distribuzione più avanti. Ma per ora assumiamo che chiunque, inclusa Bob, possa ottenere in modo sicuro la chiave pubblica di Alice K<sub>P</sub>.

In un momento successivo, Bob desidera scrivere un messaggio M ad Alice. Poiché include informazioni sensibili, tuttavia, vuole che il contenuto rimanga segreto per tutti tranne che per Alice. Quindi, Bob cripta il suo messaggio M utilizzando K<sub>P</sub>. Invia poi il testo cifrato risultante C ad Alice, che decifra C con K<sub>S</sub> per produrre il messaggio originale M.

*Figura 1: Crittografia asimmetrica*

![Figura 1: Crittografia asimmetrica](assets/Figure6-1.webp "Figura 1: Crittografia asimmetrica")

Qualsiasi avversario che ascolti la comunicazione tra Bob e Alice può osservare C. Conosce anche K<sub>P</sub> e l'algoritmo di crittografia E(·). Importante, tuttavia, queste informazioni non permettono all'attaccante di decifrare in modo fattibile il testo cifrato C. La decifrazione richiede specificamente K<sub>S</sub>, che l'attaccante non possiede.

I sistemi di crittografia simmetrica generalmente devono essere sicuri contro un attaccante che può criptare validamente messaggi in chiaro (noti come sicurezza contro attacchi con testo cifrato scelto). Non sono progettati, tuttavia, con lo scopo esplicito di permettere la creazione di tali testi cifrati validi da parte di un attaccante o di chiunque altro.

Questo è in netto contrasto con un sistema di crittografia asimmetrica, il cui scopo principale è permettere a chiunque, inclusi gli attaccanti, di produrre testi cifrati validi. I sistemi di crittografia asimmetrica possono, quindi, essere etichettati come **cifrari ad accesso multiplo**.

Per capire meglio cosa sta succedendo, immagina che invece di inviare un messaggio elettronicamente, Bob volesse inviare una lettera fisica in segreto. Un modo per garantire la segretezza sarebbe per Alice inviare un lucchetto sicuro a Bob, ma tenere la chiave per aprirlo. Dopo aver scritto la sua lettera, Bob potrebbe mettere la lettera in una scatola e chiuderla con il lucchetto di Alice. Potrebbe, quindi, inviare la scatola chiusa con il messaggio ad Alice che ha la chiave per aprirla.

Mentre Bob è in grado di chiudere il lucchetto, né lui né nessun'altra persona che intercetti la scatola possono aprire il lucchetto se questo è davvero sicuro. Solo Alice può aprirlo e vedere il contenuto della lettera di Bob perché lei ha la chiave.

Un sistema di crittografia asimmetrica è, grossomodo, una versione digitale di questo processo. Il lucchetto è paragonabile alla chiave pubblica e la chiave del lucchetto è paragonabile alla chiave privata. Poiché il lucchetto è digitale, tuttavia, è molto più facile e meno costoso per Alice distribuirlo a chiunque possa voler inviare messaggi segreti a lei.

Per l'autenticazione nell'ambito asimmetrico, utilizziamo le **firme digitali**. Queste, quindi, hanno la stessa funzione dei codici di autenticazione dei messaggi nell'ambito simmetrico. Una panoramica delle firme digitali è fornita nella *Figura 2*.
Bob crea inizialmente una coppia di chiavi, costituita dalla chiave pubblica (K<sub>P</sub>) e dalla chiave privata (K<sub>S</sub>), e distribuisce la sua chiave pubblica. Quando vuole inviare un messaggio autenticato ad Alice, prende prima il suo messaggio M e la sua chiave privata per creare una firma digitale D. Bob, quindi, invia ad Alice il suo messaggio insieme alla firma digitale. Alice inserisce il messaggio, la chiave pubblica e la firma digitale in un algoritmo di verifica. Questo algoritmo produce o vero per una firma valida, o falso per una firma non valida.
Una firma digitale è, come il nome chiaramente implica, l'equivalente digitale di una firma scritta su lettere, contratti e così via. Infatti, una firma digitale è solitamente molto più sicura. Con un certo sforzo, si può falsificare una firma scritta; un processo reso più facile dal fatto che le firme scritte non sono frequentemente verificate attentamente. Una firma digitale sicura, tuttavia, è, proprio come un codice di autenticazione del messaggio sicuro, **esistenzialmente infalsificabile**: ciò significa che, con uno schema di firma digitale sicuro, nessuno può realisticamente creare una firma per un messaggio che superi la procedura di verifica, a meno che non disponga della chiave privata.

*Figura 2: Autenticazione asimmetrica*

![Figura 2: Autenticazione asimmetrica](assets/Figure6-2.webp "Figura 2: Autenticazione asimmetrica")

Come con la crittografia asimmetrica, vediamo un interessante contrasto tra le firme digitali e i codici di autenticazione dei messaggi. Per questi ultimi, l'algoritmo di verifica può essere impiegato solo da una delle parti a conoscenza della comunicazione sicura. Questo perché richiede una chiave privata. Nell'impostazione asimmetrica, tuttavia, chiunque può verificare una firma digitale S fatta da Bob.

Tutto ciò rende le firme digitali uno strumento estremamente potente. Esse costituiscono la base, ad esempio, per la creazione di firme su contratti che possono essere verificate a fini legali. Se Bob avesse fatto una firma su un contratto nello scambio sopra, Alice può mostrare il messaggio M, il contratto e la firma S a un tribunale. Il tribunale può, quindi, verificare la firma usando la chiave pubblica di Bob.<sup>[5](#footnote5)</sup>

Per un altro esempio, le firme digitali sono un aspetto importante per garantire la sicurezza del software e la distribuzione degli aggiornamenti del software. Questo tipo di verificabilità pubblica non potrebbe mai essere creato usando solo codici di autenticazione dei messaggi.

Come ultimo esempio del potere delle firme digitali, consideriamo Bitcoin. Uno dei malintesi più comuni su Bitcoin, specialmente nei media, è che le transazioni siano criptate: non lo sono. Invece, le transazioni Bitcoin funzionano con firme digitali per garantire la sicurezza.

I Bitcoin esistono in lotti chiamati output di transazione non spesi (o UTXO). Supponiamo di ricevere tre pagamenti su un particolare indirizzo Bitcoin per 2 bitcoin ciascuno. Tecnicamente non hai ora 6 bitcoin su quell'indirizzo. Invece, hai tre lotti di 2 bitcoin che sono bloccati da un problema crittografico associato a quell'indirizzo. Per qualsiasi pagamento che fai, puoi usare uno, due o tutti e tre questi lotti, a seconda di quanto ti serve per la transazione.

La prova di proprietà sugli output di transazione non spesi è solitamente mostrata tramite una o più firme digitali. Bitcoin funziona precisamente perché le firme digitali valide sugli output di transazione non spesi sono computazionalmente infattibili da realizzare, a meno che non si sia in possesso delle informazioni segrete necessarie per farle.
Attualmente, le transazioni Bitcoin includono trasparentemente tutte le informazioni che devono essere verificate dai partecipanti nella rete, come le origini degli output di transazione non spesi utilizzati nella transazione. Anche se è possibile nascondere alcune di queste informazioni e permettere comunque la verifica (come fanno alcune criptovalute alternative come Monero), ciò crea anche particolari rischi per la sicurezza.

A volte si crea confusione tra le firme digitali e le firme scritte catturate digitalmente. In quest'ultimo caso, si cattura un'immagine della propria firma scritta e la si incolla su un documento elettronico, come un contratto di lavoro. Questo, tuttavia, non è una firma digitale nel senso crittografico. Quest'ultima è semplicemente un lungo numero che può essere prodotto solo essendo in possesso di una chiave privata.

Come nell'impostazione della chiave simmetrica, è possibile utilizzare anche schemi di crittografia asimmetrica e di autenticazione insieme. Si applicano principi simili. Prima di tutto, si dovrebbero usare coppie di chiavi private-pubbliche diverse per la crittografia e per fare firme digitali. Inoltre, si dovrebbe prima criptare un messaggio e poi autenticarlo.

Importante, in molte applicazioni la crittografia asimmetrica non viene utilizzata per l'intero processo di comunicazione. Invece, tipicamente sarà usata solo per *scambiare chiavi simmetriche* tra le parti con cui si comunicherà effettivamente.

Questo è il caso, per esempio, quando si acquistano beni online. Conoscendo la chiave pubblica del venditore, lei può inviarti messaggi firmati digitalmente che puoi verificare per la loro autenticità. Su questa base, puoi seguire uno dei molti protocolli per scambiare chiavi simmetriche per comunicare in modo sicuro.

La principale ragione per la frequenza del suddetto approccio è che la crittografia asimmetrica è molto meno efficiente della crittografia simmetrica nel produrre un determinato livello di sicurezza. Questo è uno dei motivi per cui abbiamo ancora bisogno della crittografia a chiave simmetrica accanto alla crittografia pubblica. Inoltre, la crittografia a chiave simmetrica è molto più naturale in applicazioni particolari come un utente di computer che cripta i propri dati.

Quindi, come esattamente le firme digitali e la crittografia a chiave pubblica affrontano i problemi di distribuzione e gestione delle chiavi?

Non c'è una sola risposta qui. La crittografia asimmetrica è uno strumento e non c'è un solo modo per impiegare quello strumento. Ma prendiamo il nostro esempio precedente di Jim’s Sporting Goods per mostrare come i problemi sarebbero tipicamente affrontati in questo esempio.

Per iniziare, Jim’s Sporting Goods probabilmente si rivolgerebbe a un **autorità di certificazione**, un'organizzazione che supporta nella distribuzione della chiave pubblica. L'autorità di certificazione registrerebbe alcuni dettagli su Jim’s Sporting Goods e gli concederebbe una chiave pubblica. Poi, invierebbe a Jim’s Sporting Goods un certificato, noto come **certificato TLS/SSL**, con la chiave pubblica di Jim’s Sporting Goods firmata digitalmente usando la propria chiave pubblica dell'autorità di certificazione. In questo modo, l'autorità di certificazione afferma che una particolare chiave pubblica appartiene davvero a Jim’s Sporting Goods.

La chiave per comprendere questo processo con i certificati TLS/SSL è che, mentre generalmente non avrai la chiave pubblica di Jim’s Sporting Goods memorizzata da nessuna parte sul tuo computer, le chiavi pubbliche delle autorità di certificazione riconosciute sono effettivamente memorizzate nel tuo browser o nel tuo sistema operativo. Queste sono memorizzate in quello che si chiamano **certificati radice**.

Quindi, quando Jim’s Sporting Goods ti fornisce il suo certificato TLS/SSL, puoi verificare la firma digitale dell'autorità di certificazione tramite un certificato radice nel tuo browser o sistema operativo. Se la firma è valida, puoi essere relativamente sicuro che la chiave pubblica sul certificato appartenga davvero a Jim’s Sporting Goods. Su questa base, è facile impostare un protocollo per una comunicazione sicura con Jim’s Sporting Goods.
La distribuzione delle chiavi è ora diventata notevolmente più semplice per Jim’s Sporting Goods. Non è difficile vedere che anche la gestione delle chiavi è diventata molto più semplice. Invece di dover conservare migliaia di chiavi, Jim’s Sporting Goods ha solo bisogno di conservare una chiave privata che gli permette di fare firme per la chiave pubblica sul suo certificato SSL. Ogni volta che un cliente visita il sito di Jim’s Sporting Goods, può stabilire una sessione di comunicazione sicura da questa chiave pubblica. I clienti non hanno bisogno di conservare nessuna informazione (a parte le chiavi pubbliche delle autorità di certificazione riconosciute nel loro sistema operativo e browser).

## Funzioni hash
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Le funzioni hash sono onnipresenti nella crittografia. Non sono né schemi simmetrici né asimmetrici, ma rientrano in una categoria crittografica a sé stante.

Abbiamo già incontrato le funzioni hash nel Capitolo 4 con la creazione di messaggi di autenticazione basati su hash. Sono anche importanti nel contesto delle firme digitali, sebbene per un motivo leggermente diverso: le firme digitali sono tipicamente realizzate sul valore hash di un messaggio (criptato), piuttosto che sul messaggio (criptato) stesso. In questa sezione, offrirò un'introduzione più approfondita alle funzioni hash.

Iniziamo con la definizione di una funzione hash. Una **funzione hash** è qualsiasi funzione facilmente calcolabile che prende input di dimensione arbitraria e produce output di lunghezza fissa.

Una **funzione hash crittografica** è semplicemente una funzione hash che è utile per applicazioni in crittografia. L'output di una funzione hash crittografica è tipicamente chiamato **hash**, **valore hash**, o **digest del messaggio**.

Nel contesto della crittografia, una "funzione hash" si riferisce tipicamente a una funzione hash crittografica. Adotterò questa pratica d'ora in poi.

Un esempio di funzione hash popolare è **SHA-256** (secure hash algorithm 256). Indipendentemente dalla dimensione dell'input (ad esempio, 15 bit, 100 bit o 10.000 bit), questa funzione produrrà un valore hash di 256 bit. Qui sotto puoi vedere alcuni esempi di output della funzione SHA-256.

* “Hello”: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
* “52398”: a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90
* “La crittografia è divertente”: 3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c

Tutti gli output sono esattamente 256 bit scritti in formato esadecimale (ogni cifra esadecimale può essere rappresentata da quattro cifre binarie). Quindi, anche se avessi inserito il libro *Il Signore degli Anelli* di Tolkien nella funzione SHA-256, l'output sarebbe comunque di 256 bit.

Le funzioni hash come SHA-256 sono impiegate per vari scopi nella crittografia. Le proprietà richieste da una funzione hash dipendono davvero dal contesto di una particolare applicazione. Ci sono due proprietà principali generalmente desiderate dalle funzioni hash nella crittografia:

1.	Resistenza alle collisioni
2.	Oscuramento

Si dice che una funzione hash H sia **resistente alle collisioni** se è impraticabile trovare due valori, x e y, tali che x ≠ y, eppure H(x) = H(y).
Le funzioni hash resistenti alle collisioni sono importanti, ad esempio, nella verifica del software. Supponiamo che tu voglia scaricare la versione Windows di Bitcoin Core 0.21.0 (un'applicazione server per elaborare il traffico della rete Bitcoin). I passaggi principali che dovresti compiere per verificare la legittimità del software sono i seguenti:
1. Devi prima scaricare e importare le chiavi pubbliche di uno o più contributori di Bitcoin Core in un software che possa verificare le firme digitali (ad esempio, Kleopetra). Puoi trovare queste chiavi pubbliche [qui](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Si raccomanda di verificare il software Bitcoin Core con le chiavi pubbliche di più contributori.
2. Successivamente, devi verificare le chiavi pubbliche che hai importato. Almeno un passaggio che dovresti compiere è verificare che le chiavi pubbliche trovate siano le stesse pubblicate in varie altre località. Potresti, ad esempio, consultare le pagine web personali, le pagine Twitter o le pagine Github delle persone le cui chiavi pubbliche hai importato. Tipicamente, questo confronto delle chiavi pubbliche viene fatto confrontando un breve hash della chiave pubblica noto come impronta digitale.
3. Successivamente, devi scaricare l'eseguibile per Bitcoin Core dal loro [sito web](www.bitcoincore.org). Saranno disponibili pacchetti per i sistemi operativi Linux, Windows e MAC.
4. Dopo, devi localizzare due file di rilascio. Il primo contiene l'hash SHA-256 ufficiale per l'eseguibile che hai scaricato insieme agli hash di tutti gli altri pacchetti che sono stati rilasciati. Un altro file di rilascio conterrà le firme di vari contributori sul file di rilascio con gli hash dei pacchetti. Entrambi questi file di rilascio dovrebbero essere situati sul sito web di Bitcoin Core.
5. Successivamente, dovresti calcolare l'hash SHA-256 dell'eseguibile che hai scaricato dal sito web di Bitcoin Core sul tuo computer. Poi, confronti questo risultato con quello dell'hash ufficiale del pacchetto per l'eseguibile. Dovrebbero essere uguali.
6. Infine, dovresti verificare che una o più delle firme digitali sul file di rilascio con gli hash ufficiali del pacchetto corrispondano effettivamente a una o più chiavi pubbliche che hai importato (i rilasci di Bitcoin Core non sono sempre firmati da tutti). Puoi fare ciò con un'applicazione come Kleopetra.

Questo processo di verifica del software ha due benefici principali. Primo, assicura che non ci siano stati errori nella trasmissione durante il download dal sito web di Bitcoin Core. Secondo, garantisce che nessun attaccante potrebbe averti fatto scaricare codice modificato e malevolo, sia hackerando il sito web di Bitcoin Core sia intercettando il traffico.

Come esattamente il processo di verifica del software sopra descritto protegge da questi problemi?

Se hai verificato diligentemente le chiavi pubbliche che hai importato, allora puoi essere abbastanza certo che queste chiavi siano effettivamente loro e non siano state compromesse. Dato che le firme digitali hanno l'inforgevolezza esistenziale, sai che solo questi contributori avrebbero potuto fare una firma digitale sugli hash ufficiali del pacchetto sul file di rilascio.

Supponiamo che le firme sul file di rilascio che hai scaricato siano corrette. Ora puoi confrontare il valore hash che hai calcolato localmente per l'eseguibile Windows che hai scaricato con quello incluso nel file di rilascio correttamente firmato. Poiché sai che la funzione hash SHA-256 è resistente alle collisioni, una corrispondenza significa che il tuo eseguibile è esattamente lo stesso dell'eseguibile ufficiale.

Passiamo ora alla seconda proprietà comune delle funzioni hash: l'occultamento. Si dice che una funzione hash H abbia la proprietà di occultamento, se, per un x selezionato casualmente da un intervallo molto ampio, è impraticabile trovare x quando è dato solo H(x).
Di seguito, puoi vedere l'output SHA-256 di un messaggio che ho scritto. Per garantire sufficiente casualità, il messaggio includeva una stringa di caratteri generata casualmente alla fine. Dato che SHA-256 possiede la proprietà di occultamento, nessuno sarebbe in grado di decifrare questo messaggio.
* b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded

Ma non ti lascerò in sospeso fino a quando SHA-256 diventerà più debole. Il messaggio originale che ho scritto era il seguente:

* “Questo è un messaggio molto casuale, o beh, in qualche modo casuale. Questa parte iniziale non lo è, ma terminerò con alcuni caratteri relativamente casuali per garantire un messaggio molto imprevedibile. XLWz4dVG3BxUWm7zQ9qS”.

Un modo comune in cui le funzioni hash con la proprietà di occultamento vengono utilizzate è nella gestione delle password (anche la resistenza alle collisioni è importante per questa applicazione). Qualsiasi servizio online basato su account decente, come Facebook o Google, non memorizzerà direttamente le tue password per gestire l'accesso al tuo account. Invece, memorizzeranno solo un hash di quella password. Ogni volta che inserisci la tua password su un browser, viene prima calcolato un hash. Solo quell'hash viene inviato al server del fornitore di servizi e confrontato con l'hash memorizzato nel database back-end. La proprietà di occultamento può aiutare a garantire che gli aggressori non possano recuperarla dal valore dell'hash.

La gestione delle password tramite hash, ovviamente, funziona solo se gli utenti scelgono effettivamente password difficili. La proprietà di occultamento presume che x sia scelto casualmente da un intervallo molto ampio. Selezionare password come “1234”, “mypassword” o la data del tuo compleanno non fornirà alcuna reale sicurezza. Esistono lunghe liste di password comuni e dei loro hash che gli aggressori possono sfruttare se ottengono l'hash della tua password. Questi tipi di attacchi sono noti come **attacchi dizionario**. Se gli aggressori conoscono alcuni dei tuoi dettagli personali, potrebbero anche tentare alcune ipotesi informate. Pertanto, hai sempre bisogno di password lunghe e sicure (preferibilmente lunghe stringhe casuali da un gestore di password).

A volte un'applicazione potrebbe aver bisogno di una funzione hash che abbia sia resistenza alle collisioni che occultamento. Ma certamente non sempre. Il processo di verifica del software di cui abbiamo discusso, ad esempio, richiede solo che la funzione hash mostri resistenza alle collisioni, l'occultamento non è importante.

Mentre la resistenza alle collisioni e l'occultamento sono le principali proprietà ricercate delle funzioni hash in crittografia, in certe applicazioni potrebbero essere desiderabili anche altri tipi di proprietà.

### Note
[^1]: Whitfield Diffie e Martin Hellman, “Nuove direzioni nella crittografia,” *IEEE Transactions on Information Theory* IT-22 (1976), pp. 644–654, a p. 644 [^1].

[^2]: Ralph Merkle discute anche di un protocollo di scambio di chiavi in “Comunicazioni sicure su canali insicuri”, *Communications of the Association for Computing Machinery*, 21 (1978), 294–99. Sebbene Merkle abbia effettivamente inviato questo articolo prima del documento di Diffie e Hellman, è stato pubblicato più tardi. La soluzione di Merkle non è esponenzialmente sicura, a differenza di quella di Diffie-Hellman [^2].

[^3]: Ron Rivest, Adi Shamir e Leonard Adleman, “Un metodo per ottenere firme digitali e sistemi di crittografia a chiave pubblica”, *Communications of the Association for Computing Machinery*, 21 (1978), pp. 120–26 [^3].

[^4]: Una buona storia di queste scoperte è fornita da Simon Singh, *Il libro dei codici*, Fourth Estate (Londra, 1999), Capitolo 6 [^4].
[^5]: Qualsiasi schema che tenta di raggiungere la non ripudiabilità, l'altro tema discusso nel *Capitolo 1*, dovrà basarsi necessariamente sull'uso delle firme digitali [^5].
[^6]: La terminologia "nascondere" non è un linguaggio comune, ma è presa specificamente da Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller e Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Capitolo 1 [^6].

# Il criptosistema RSA
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

Mentre la crittografia simmetrica è solitamente abbastanza intuitiva per la maggior parte delle persone, questo generalmente non accade con la crittografia asimmetrica. Sebbene tu possa essere a tuo agio con la descrizione ad alto livello offerta nelle sezioni precedenti, probabilmente ti stai chiedendo cosa siano esattamente le funzioni unidirezionali e come vengono utilizzate per costruire schemi asimmetrici.

In questo capitolo, eliminerò parte del mistero che circonda la crittografia asimmetrica, esaminando più da vicino un esempio specifico, ovvero il criptosistema RSA. Nella prima sezione, introdurrò il problema della fattorizzazione su cui si basa il problema RSA. Coprirò quindi una serie di risultati chiave della teoria dei numeri. Nell'ultima sezione, metteremo insieme queste informazioni per spiegare il problema RSA e come questo può essere utilizzato per creare schemi crittografici asimmetrici.

Aggiungere questa profondità alla nostra discussione non è un compito facile. Richiede l'introduzione di un bel numero di teoremi e proposizioni della teoria dei numeri. Ma non lasciare che la matematica ti dissuada. Lavorare su questa discussione migliorerà significativamente la tua comprensione di ciò che sta alla base della crittografia asimmetrica ed è un investimento utile.

Ora passiamo prima al problema della fattorizzazione.

## Il problema della fattorizzazione
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Ogni volta che moltiplichi due numeri, diciamo a e b, ci riferiamo ai numeri a e b come **fattori**, e al risultato come **prodotto**. Tentare di scrivere un numero N come la moltiplicazione di due o più fattori è chiamato **fattorizzazione**.<sup>[1](#footnote1)</sup> Puoi chiamare qualsiasi problema che richiede questo un **problema di fattorizzazione**.

Circa 2.500 anni fa, il matematico greco Euclide di Alessandria scoprì un teorema chiave sulla fattorizzazione degli interi. È comunemente chiamato il **teorema della fattorizzazione unica** e afferma quanto segue:

*Teorema 1*. Ogni intero N maggiore di 1 è o un numero primo, o può essere espresso come un prodotto di fattori primi.

Tutta l'ultima parte di questa affermazione significa che puoi prendere qualsiasi intero non primo N maggiore di 1 e scriverlo come una moltiplicazione di numeri primi. Di seguito sono riportati diversi esempi di interi non primi scritti come il prodotto di fattori primi.

* 18 = 2 • 3 • 3 = 2 • 3<sup>2</sup>
* 84 = 2 • 2 • 3 • 7 = 2<sup>2</sup> • 3 • 7
* 144 = 2 • 2 • 2 • 2 • 3 • 3 = 2<sup>4</sup> • 3<sup>2</sup>
Per tutti e tre gli interi sopra menzionati, calcolare i loro fattori primi è relativamente semplice, anche se si dispone solo di N. Si inizia con il più piccolo numero primo, ovvero 2, e si verifica quante volte l'intero N è divisibile per esso. Si procede poi testando la divisibilità di N per 3, 5, 7 e così via. Si continua questo processo fino a quando il proprio intero N è scritto come prodotto di soli numeri primi.
Prendiamo, ad esempio, l'intero 84. Di seguito potete vedere il processo per determinare i suoi fattori primi. Ad ogni passaggio estraiamo il più piccolo fattore primo rimanente (a sinistra) e determiniamo il termine residuo da fattorizzare. Continuiamo fino a quando il termine residuo è anch'esso un numero primo. Ad ogni passaggio, l'attuale fattorizzazione di 84 è visualizzata sulla destra.

* Fattore primo = 2: termine residuo = 42 (84 = 2 • 42)
* Fattore primo = 2: termine residuo = 21 (84 = 2 • 2 • 21)
* Fattore primo = 3: termine residuo = 7 (84 = 2 • 2 • 3 • 7)
* Poiché 7 è un numero primo, il risultato è 2 • 2 • 3 • 7, o 2<sup>2</sup> • 3 • 7.

Supponiamo ora che N sia molto grande. Quanto sarebbe difficile ridurre N nei suoi fattori primi?

Questo dipende davvero da N. Supponiamo, ad esempio, che N sia 50,450,400. Anche se questo numero sembra intimidatorio, i calcoli non sono così complicati e possono essere facilmente eseguiti a mano. Come sopra, si inizia semplicemente con 2 e si procede. Di seguito, potete vedere il risultato di questo processo in modo simile a quanto sopra.

* 2: 25,225,200 (50,450,400 = 2 • 25,225,200)
* 2: 12,612,600 (50,450,400 = 2<sup>2</sup> • 12,612,600)
* 2: 6,306,300 (50,450,400 = 2<sup>3</sup> • 6,306,300)
* 2: 3,153,150 (50,450,400 = 2<sup>4</sup> • 3,153,150)
* 2: 1,576,575 (50,450,400 = 2<sup>5</sup> • 1,576,575)
* 3: 525,525 (50,450,400 = 2<sup>5</sup> • 3 • 525,525)
* 3: 175,175 (50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 175,175)
* 5: 35,035 (50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5 • 35,035)
* 5: 7,007 (50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7,007)
* 7: 1.001 (50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7 • 1.001) * 7: 143 (50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 143)
* 11: 13 (50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13)
* Poiché 13 è un numero primo, il risultato è 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13.

Risolvere questo problema a mano richiede del tempo. Un computer, ovviamente, potrebbe fare tutto questo in una frazione di secondo. Infatti, un computer può spesso anche fattorizzare interi estremamente grandi in una frazione di secondo.

Ci sono, tuttavia, alcune eccezioni. Supponiamo che per prima cosa selezioniamo casualmente due numeri primi molto grandi. È tipico etichettarli con p e q, e adotterò questa convenzione qui.

Per essere concreti, diciamo che p e q sono entrambi primi di 1024 bit, e che effettivamente richiedono almeno 1024 bit per essere rappresentati (quindi il primo bit deve essere 1). Quindi, ad esempio, 37 non potrebbe essere uno dei numeri primi. Certamente puoi rappresentare 37 con 1024 bit. Ma chiaramente *non hai bisogno* di così tanti bit per rappresentarlo. Puoi rappresentare 37 con una stringa che ha 6 bit o più. (In 6 bit, 37 sarebbe rappresentato come 100101).

È importante apprezzare quanto siano grandi p e q se selezionati secondo le condizioni sopra. Come esempio, ho selezionato un numero primo casuale che necessita di almeno 1024 bit per la rappresentazione qui sotto.

* 14.752.173.874.503.595.484.930.006.383.670.759.559.764.562.721.397.166.747.289.220.945.457.932.666.751.048.198.854.920.097.085.690.793.755.254.946.188.163.753.506.778.089.706.699.671.722.089.715.624.760.049.594.106.189.662.669.156.149.028.900.805.928.183.585.427.782.974.951.355.515.394.807.209.836.870.484.558.332.897.443.152.653.214.483.870.992.618.171.825.921.582.253.023.974.514.209.142.520.026.807.636.589

Supponiamo ora che, dopo aver selezionato casualmente i numeri primi p e q, li moltiplichiamo per ottenere un intero N. Quest'ultimo intero, quindi, è un numero di 2048 bit che richiede almeno 2048 bit per la sua rappresentazione. È molto, molto più grande di p o q.
Supponiamo di fornire a un computer un numero N e di chiedergli di trovare i due fattori primi di 1024 bit di N. La probabilità che il computer scopra p e q è estremamente piccola. Si può dire che è impossibile per tutti gli scopi pratici. Questo vale anche se si dovesse impiegare un supercomputer o addirittura una rete di supercomputer.

Per iniziare, supponiamo che il computer tenti di risolvere il problema ciclando attraverso numeri di 1024 bit, testando in ogni caso se sono primi e se sono fattori di N. L'insieme dei numeri primi da testare è quindi approssimativamente 1,265 • 10<sup>305</sup>.<sup>[2](#footnote2)</sup>

Anche se si prendessero tutti i computer del pianeta e li si facesse tentare di trovare e testare numeri primi di 1024 bit in questo modo, una possibilità su un miliardo di trovare con successo un fattore primo di N richiederebbe un periodo di calcolo molto più lungo dell'età dell'Universo.

Ora, nella pratica, un computer può fare meglio della procedura approssimativa appena descritta. Esistono diversi algoritmi che il computer può applicare per arrivare a una fattorizzazione più rapidamente. Il punto, tuttavia, è che anche utilizzando questi algoritmi più efficienti, il compito del computer è ancora computazionalmente infattibile.<sup>[3](#footnote3)</sup>

Importante è che la difficoltà della fattorizzazione nelle condizioni appena descritte si basa sull'assunzione che non esistano algoritmi computazionalmente efficienti per calcolare i fattori primi. Non possiamo effettivamente dimostrare che un algoritmo efficiente non esista. Tuttavia, questa assunzione è molto plausibile: nonostante gli sforzi estensivi che durano da centinaia di anni, non siamo ancora riusciti a trovare un tale algoritmo computazionalmente efficiente.

Pertanto, il problema della fattorizzazione, in determinate circostanze, può essere plausibilmente considerato un problema difficile. In particolare, quando p e q sono numeri primi molto grandi, il loro prodotto N non è difficile da calcolare; ma la fattorizzazione data solo N è praticamente impossibile.

## Risultati teorici sui numeri
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Sfortunatamente, il problema della fattorizzazione non può essere utilizzato direttamente per gli schemi crittografici asimmetrici. Tuttavia, possiamo utilizzare un problema più complesso ma correlato a questo scopo: il problema RSA.

Per comprendere il problema RSA, avremo bisogno di capire una serie di teoremi e proposizioni della teoria dei numeri. Questi sono presentati in questa sezione in tre sottosezioni: (1) l'ordine di N, (2) l'invertibilità modulo N, e (3) il teorema di Eulero.

Parte del materiale nelle tre sottosezioni è già stata introdotta nel *Capitolo 3*. Ma qui ripresenterò quel materiale per comodità.

### L'ordine di N

Un intero a è **coprimo** o un **primo relativo** con un intero N, se il massimo comun divisore tra loro è 1. Anche se 1 per convenzione non è un numero primo, è un coprimo di ogni intero (come lo è – 1).

Per esempio, consideriamo il caso in cui a = 18 e N = 37. Questi sono chiaramente coprimi. Il più grande intero che si divide sia in 18 che in 37 è 1. Al contrario, consideriamo il caso in cui a = 42 e N = 16. Questi non sono chiaramente coprimi. Entrambi i numeri sono divisibili per 2, che è maggiore di 1.
Possiamo ora definire l'ordine di N come segue. Supponiamo che N sia un intero maggiore di 1. L'**ordine di N** è, quindi, il numero di tutti i coprimi con N tali che per ogni coprimo a, valga la seguente condizione: 1 ≤ a < N.
Ad esempio, se N = 12, allora 1, 5, 7 e 11 sono gli unici coprimi che soddisfano il requisito sopra menzionato. Pertanto, l'ordine di 12 è uguale a 4.

Supponiamo che N sia un numero primo. Allora ogni intero minore di N ma maggiore o uguale a 1 è coprimo con esso. Questo include tutti gli elementi nel seguente insieme: {1,2,3….,N – 1}. Quindi, quando N è primo, l'ordine di N è N – 1. Questo è affermato nella proposizione 1, dove φ(N) denota l'ordine di N.

**Proposizione 1**. φ(N) = N – 1 quando N è primo

Supponiamo che N non sia primo. Puoi, quindi, calcolare il suo ordine utilizzando la **Funzione Phi di Eulero**. Mentre calcolare l'ordine di un piccolo intero è relativamente semplice, la Funzione Phi di Eulero diventa particolarmente importante per gli interi più grandi. La proposizione della Funzione Phi di Eulero è enunciata di seguito.

*Teorema 2*. Sia N uguale a p<sub>1</sub><sup>e_1</sup> • p<sub>2</sub><sup>e_2</sup> • … • p<sub>i</sub><sup>e_i</sup> • … • p<sub>n</sub><sup>e_n</sup>, dove l'insieme {p<sub>i</sub>} consiste in tutti i fattori primi distinti di N e ogni e_i indica quante volte il fattore primo p<sub>i</sub> si verifica per N. Allora, φ(N) = p<sub>1</sub><sup>e_1 - 1</sup> • (p<sub>1</sub> - 1) • p<sub>2</sub><sup>e_2 - 1</sup> • (p<sub>2</sub> - 1) • … • p<sub>n</sub><sup>e_n - 1</sup> • (p<sub>n</sub> - 1).

Il *Teorema 2* mostra che una volta scomposto qualsiasi N non primo nei suoi fattori primi distinti, è facile calcolare l'ordine di N.

Ad esempio, supponiamo che N = 270. Questo chiaramente non è un numero primo. Scomponendo N nei suoi fattori primi si ottiene l'espressione: 2 • 3<sup>3</sup> • 5. Secondo la Funzione Phi di Eulero, l'ordine di N è quindi il seguente:

* φ(N) = 2<sup>1 – 1</sup> (2 – 1) + 3<sup>3 – 1</sup> (3 – 1) + 5<sup>1 – 1</sup> (5 – 1) = 1 (1) + 9 (2) + 1 (4) = 1 + 18 + 4 = 23
Supponiamo ora che N sia il prodotto di due numeri primi, p e q. *Teorema 2* sopra, quindi, afferma che l'ordine di N è il seguente: p<sup>1 – 1</sup> (p – 1) x q<sup>1 – 1</sup> (q – 1) = (p – 1) x (q – 1). Questo è un risultato chiave per il problema RSA in particolare, ed è enunciato nella *Proposizione 2* qui sotto.
*Proposizione 2*. Se N è il prodotto di due numeri primi, p e q, l'ordine di N è il prodotto (p – 1) x (q – 1).

Per illustrare, supponiamo che N = 119. Questo intero può essere fattorizzato in due numeri primi, precisamente 7 e 17. Di conseguenza, la funzione Phi di Eulero suggerisce che l'ordine di 119 è il seguente:

* φ(119) = (7 – 1) • (17 – 1) = 6 • 16 = 96.

In altre parole, l'intero 119 ha 96 coprimi nell'intervallo da 1 fino a 119. Infatti, questo insieme include tutti gli interi da 1 fino a 119, che non sono multipli né di 7 né di 17.

Da qui in poi, denotiamo l'insieme dei coprimi che determina l'ordine di N come **C<sub>N</sub>**. Per il nostro esempio dove N = 119, l'insieme **C<sub>119</sub>** è troppo grande per essere elencato completamente. Ma alcuni degli elementi sono i seguenti: **C<sub>119</sub>** = {1,2,….6,8….13,15,16,18,….,33,35….,96}.

### Invertibilità modulo N

Possiamo dire che un intero a è **invertibile modulo N**, se esiste almeno un intero b tale che a x b modulo N = 1 modulo N. Qualsiasi tale intero b è definito come un **inverso** (o **inverso moltiplicativo**) di a dato una riduzione per modulo N.

Supponiamo, ad esempio, che a = 5 e N = 11. Ci sono molti interi con cui puoi moltiplicare 5, in modo che 5 x b mod 11 = 1 mod 11. Considera, per esempio, gli interi 20 e 31. È facile vedere che entrambi questi interi sono inversi di 5 per la riduzione modulo 11.

* 5 x 20 mod 11 = 100 mod 11 = 1 mod 11
* 5 x 31 mod 11 = 155 mod 11 = 1 mod 11

Mentre 5 ha molti inversi per la riduzione modulo 11, si può dimostrare che esiste solo un singolo inverso positivo di 5 che è minore di 11. Infatti, questo non è un caso unico per il nostro particolare esempio, ma un risultato generale.

*Proposizione 3*. Se l'intero a è invertibile modulo N, deve essere il caso che esista esattamente un inverso positivo di a che è minore di N. (Quindi, questo inverso unico di a deve provenire dall'insieme {1,…,N – 1}).
Denominiamo l'inverso unico di a dalla Proposizione 3 come a<sup>-1</sup>. Nel caso in cui a = 5 e N = 11, si può vedere che a<sup>-1</sup> = 9, dato che 5 x 9 mod 11 = 45 mod 11 = 1 mod 11.
Si noti che si può ottenere il valore 9 per a<sup>-1</sup> nel nostro esempio semplicemente riducendo qualsiasi altro inverso di a modulo 11. Ad esempio, 20 mod 11 = 31 mod 11 = 9 mod 11. Quindi, ogni volta che un intero a > N è invertibile modulo N, allora a mod N deve essere anch'esso invertibile modulo N.

Non è necessariamente vero che esista un inverso di a nella riduzione modulo N. Supponiamo, per esempio, che a = 2 e N = 8. Non esiste nessun b, o specificamente nessun a<sup>-1</sup>, tale che 2 x b mod 8 = 1 mod 8. Questo perché qualsiasi valore di b produrrà sempre un multiplo di 2, quindi nessuna divisione per 8 potrà mai dare un resto uguale a 1.

Come facciamo esattamente a sapere se un certo intero a ha un inverso per un dato N? Come potreste aver notato nell'esempio sopra, il massimo comun divisore tra 2 e 8 è maggiore di 1, precisamente 2. E questo è in realtà illustrativo del seguente risultato generale:

*Proposizione 4*. Un inverso esiste di un intero a dato nella riduzione modulo N, e specificamente un unico inverso positivo minore di N, se e solo se il massimo comun divisore tra a e N è 1 (cioè, se sono coprimi).

Nel caso in cui a = 5 e N = 11, abbiamo concluso che a<sup>-1</sup> = 9, dato che 5 x 9 mod 11 = 45 mod 11 = 1 mod 11. È importante notare che il contrario è anche vero. Cioè, quando a = 9 e N = 11, si verifica che a<sup>-1</sup> = 5.

### Teorema di Eulero

Prima di passare al problema RSA, dobbiamo comprendere un altro teorema fondamentale, ovvero **il teorema di Eulero**. Esso afferma quanto segue:

*Teorema 3*. Supponiamo che due interi a e N siano coprimi. Allora, a<sup>φ(N)</sup> mod N = 1 mod N.

Questo è un risultato notevole, ma un po' confuso all'inizio. Passiamo a un esempio per capirlo.

Supponiamo che a = 5 e N = 7. Questi sono effettivamente coprimi come richiede il teorema di Eulero. Sappiamo che l'ordine di 7 è uguale a 6, dato che 7 è un numero primo (vedi **Proposizione 1**).

Quello che il teorema di Eulero ora afferma è che 5<sup>6</sup> mod 7 deve essere uguale a 1 mod 7. Di seguito i calcoli per mostrare che questo è effettivamente vero.

* 5<sup>6</sup> mod 7 = 15.625 mod 7 = 1 mod N

L'intero 7 divide 15.624 un totale di 2.233 volte. Pertanto, il resto della divisione di 16.625 per 7 è 1.

Successivamente, utilizzando la funzione Phi di Eulero, *Teorema 2*, è possibile derivare la *Proposizione 5* di seguito.
*Proposizione 5*. φ(a • b) = φ(a) • φ(b) per qualsiasi intero positivo a e b.
Non mostreremo il perché ciò accada. Ma notiamo semplicemente che avete già visto prove di questa proposizione dal fatto che φ(p • q) = φ(p) • φ(q) = (p – 1) • (q – 1) quando p e q sono primi, come affermato nella *Proposizione 2*.

Il teorema di Eulero in congiunzione con la *Proposizione 5* ha implicazioni importanti. Vediamo cosa succede, per esempio, nelle espressioni sottostanti, dove a e N sono coprimi.

* a<sup>2 • φ(N)</sup> mod N = a<sup>φ(N)</sup> • a<sup>φ(N)</sup> mod N = 1 • 1 mod N = 1 mod N
* a<sup>φ(N) + 1</sup> mod N = a<sup>φ(N)</sup> • a<sup>1</sup> mod N = 1 • a<sup>1</sup> mod N = a mod N
* a<sup>8 • φ(N) + 3</sup> mod N = a<sup>8 • φ(N)</sup> • a<sup>3</sup> mod N = 1 • a<sup>3</sup> mod N = a<sup>3</sup> mod N

Quindi, la combinazione del teorema di Eulero e della *Proposizione 5* ci permette di calcolare semplicemente un numero di espressioni. In generale, possiamo riassumere l'intuizione come nella *Proposizione 6*.

*Proposizione 6*. a<sup>x</sup> mod N = a<sup>x mod φ(N)</sup>

Ora dobbiamo mettere tutto insieme in un ultimo passaggio complicato.

Così come N ha un ordine φ(N) che include gli elementi dell'insieme **C<sub>N</sub>**, sappiamo che l'intero φ(N) deve a sua volta avere anche un ordine e un insieme di coprimi. Poniamo φ(N) = R. Allora sappiamo che esiste anche un valore per φ(R) e un insieme di coprimi **C<sub>R</sub>**.

Supponiamo ora di selezionare un intero e dall'insieme **C<sub>R</sub>**. Sappiamo dalla *Proposizione 3* che questo intero e ha un solo inverso positivo unico minore di R. Cioè, e ha un unico inverso dall'insieme **C<sub>R</sub>**. Chiamiamo questo inverso d. Data la definizione di un inverso, ciò significa che e • d = 1 mod R.

Possiamo usare questo risultato per fare una dichiarazione sul nostro intero originale N. Questo è riassunto nella *Proposizione 7*.

*Proposizione 7*. Supponiamo che e • d mod φ(N) = 1 mod φ(N). Allora per qualsiasi elemento a dell'insieme **C<sub>N</sub>** deve essere il caso che a<sup>e • d mod φ(N)</sup> = a<sup>1 mod φ(N)</sup> = a mod N.

Ora abbiamo tutti i risultati teorici dei numeri necessari per enunciare chiaramente il problema RSA.

## Il sistema crittografico RSA
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>
Siamo ora pronti per definire il problema RSA. Supponiamo di creare un insieme di variabili costituito da p, q, N, φ(N), e, d e y. Chiamiamo questo insieme Π. Viene creato come segue:
1. Generare due primi casuali p e q della stessa dimensione e calcolare il loro prodotto N.
2. Calcolare l'ordine di N, φ(N), tramite il seguente prodotto: (p - 1) • (q - 1).
3. Selezionare un e > 2 tale che sia minore e coprimo con φ(N).
4. Calcolare d impostando e • d mod φ(N) = 1.
5. Selezionare un valore casuale y che sia minore e coprimo con N.

Il problema RSA consiste nel trovare un x tale che x^e = y, avendo a disposizione solo un sottoinsieme di informazioni riguardo a Π, nello specifico le variabili N, e e y. Quando p e q sono molto grandi, tipicamente si raccomanda che siano di dimensione 1024 bit, il problema RSA è considerato difficile. Ora si può capire perché ciò sia il caso, alla luce della discussione precedente.

Un modo semplice per calcolare x quando x^e mod N = y mod N è semplicemente calcolando y^d mod N. Sappiamo che y^d mod N = x mod N tramite i seguenti calcoli:

* y^d mod N = x^(e • d) mod N = x^(e • d mod φ(N)) mod N = x^(1 mod φ(N)) mod N = x mod N.

Il problema è che non conosciamo il valore di d, poiché non è dato nel problema. Pertanto, non possiamo calcolare direttamente y^d mod N per produrre x mod N.

Tuttavia, potremmo essere in grado di calcolare indirettamente d dall'ordine di N, φ(N), poiché sappiamo che e • d mod φ(N) = 1 mod φ(N). Ma per ipotesi il problema non fornisce neanche un valore per φ(N).

Infine, l'ordine potrebbe essere calcolato indirettamente con i fattori primi p e q, così da poter eventualmente calcolare d. Ma per ipotesi, anche i valori di p e q non ci sono stati forniti.

Parlando in termini assoluti, anche se il problema della fattorizzazione all'interno di un problema RSA è difficile, non possiamo dimostrare che anche il problema RSA sia difficile. Potrebbero esserci, infatti, altri modi per risolvere il problema RSA che non attraverso la fattorizzazione. Tuttavia, è generalmente accettato e supposto che se il problema della fattorizzazione all'interno del problema RSA è difficile, allora anche il problema RSA stesso è difficile.

Se il problema RSA è effettivamente difficile, allora produce una funzione unidirezionale con una porta segreta. La funzione qui è f(g) = g^e mod N. Con la conoscenza di f(g), chiunque potrebbe facilmente calcolare un valore y per un particolare g = x. Tuttavia, è praticamente impossibile calcolare un particolare valore x conoscendo solo il valore y e la funzione f(g). L'eccezione è quando ti viene fornito un pezzo di informazione d, la porta segreta. In tal caso, puoi semplicemente calcolare y^d per ottenere x.

Passiamo attraverso un esempio specifico per illustrare il problema RSA. Non posso selezionare un problema RSA che sarebbe considerato difficile nelle condizioni sopra menzionate, poiché i numeri sarebbero ingombranti. Invece, questo esempio serve solo a illustrare come funziona generalmente il problema RSA.
Per iniziare, supponiamo di selezionare due numeri primi casuali 13 e 31. Quindi p = 13 e q = 31. Il prodotto N di questi due primi è uguale a 403. Possiamo facilmente calcolare l'ordine di 403. È equivalente a (13 - 1) • (31 - 1) = 360.
Successivamente, come dettato dal passo 3 del problema RSA, dobbiamo selezionare un coprimo di 360 che sia maggiore di 2 e minore di 360. Non dobbiamo selezionare questo valore casualmente. Supponiamo che selezioniamo 103. Questo è un coprimo di 360 poiché il suo massimo comune divisore con 103 è 1.

Il passo 4 ora richiede che calcoliamo un valore d tale che 103 • d mod 360 = 1. Questo non è un compito facile a mano quando il valore per N è grande. Richiede che utilizziamo una procedura chiamata **algoritmo euclideo esteso**.

Anche se non mostro la procedura qui, essa produce il valore 7 quando e = 103. Puoi verificare che la coppia di valori 103 e 7 soddisfa effettivamente la condizione generale e • d mod φ(n) = 1 attraverso i calcoli sottostanti.

* 103 • 7 mod 360 = 721 mod 360 = 1 mod 360

Importante, data la *Proposizione 4*, sappiamo che nessun altro intero tra 1 e 360 per d produrrà il risultato che 103 • d = 1 mod 360. Inoltre, la proposizione implica che selezionando un valore diverso per e, produrrà un diverso valore unico per d.

Nel passo 5 del problema RSA, dobbiamo selezionare un qualche intero positivo y che sia un coprimo minore di 403. Supponiamo che impostiamo y = 2<sup>103</sup>. L'esponenziazione di 2 per 103 produce il risultato sottostante.

* 2<sup>103</sup> mod 403 = 10.141.204.801.825.835.211.973.625.643.008 mod 403 = 349 mod 403

Il problema RSA in questo particolare esempio è ora il seguente: Ti viene fornito N = 403, e = 103, e y = 349 mod 403. Ora devi calcolare x tale che x<sup>103</sup> = 349 mod 403. Cioè, devi trovare che il valore originale prima dell'esponenziazione per 103 era 2.

Sarebbe facile (almeno per un computer) calcolare x se sapessimo che d = 7. In tal caso, potresti semplicemente determinare x come di seguito.

* x = y<sup>7</sup> mod 403 = 349<sup>7</sup> mod 403 = 630.634.881.591.804.949 mod 403 = 2 mod 403

Il problema è che non ti è stata fornita l'informazione che d = 7. Potresti, naturalmente, calcolare d dal fatto che 103 • d = 1 mod 360. Il problema è che non ti è stata data nemmeno l'informazione che l'ordine di N = 360. Infine, potresti anche calcolare l'ordine di 403 calcolando il seguente prodotto: (p - 1) • (q - 1). Ma non ti è stato detto nemmeno che p = 13 e q = 31.
Naturalmente, un computer potrebbe ancora risolvere il problema RSA per questo esempio relativamente facilmente, poiché i numeri primi coinvolti non sono grandi. Ma quando i primi diventano molto grandi, si trova di fronte a un compito praticamente impossibile.
Abbiamo ora presentato il problema RSA, un insieme di condizioni in cui è difficile, e la matematica sottostante. Come può tutto ciò aiutare con la crittografia asimmetrica? Specificamente, come possiamo trasformare la difficoltà del problema RSA sotto certe condizioni in uno schema di crittografia o in uno schema di firma digitale?

Un approccio è prendere il problema RSA e costruire schemi in modo diretto. Per esempio, supponiamo che tu abbia generato un insieme di variabili Π come descritto nel problema RSA, e assicurati che p e q siano sufficientemente grandi. Imposti la tua chiave pubblica uguale a (N, e) e condividi queste informazioni con il mondo. Come descritto sopra, mantieni segreti i valori di p, q, φ(n) e d. Infatti, d è la tua chiave privata.

Chiunque voglia inviarti un messaggio m che è un elemento di **C<sub>N</sub>** potrebbe semplicemente criptarlo come segue: c = m<sup>e</sup> mod N. (Il testo cifrato c qui è equivalente al valore y nel problema RSA.) Puoi facilmente decifrare questo messaggio calcolando semplicemente c<sup>d</sup> mod N.

Potresti tentare di creare uno schema di firma digitale nello stesso modo. Supponiamo che tu voglia inviare a qualcuno un messaggio m con una firma digitale S. Potresti semplicemente impostare S = m<sup>d</sup> mod N e inviare la coppia (m,S) al destinatario. Chiunque può verificare la firma digitale semplicemente controllando se S<sup>e</sup> mod N = m mod N. Tuttavia, qualsiasi attaccante avrebbe davvero difficoltà a creare un S valido per un messaggio, dato che non possiede d.

Sfortunatamente, trasformare quello che di per sé è un problema difficile, il problema RSA, in uno schema crittografico non è così diretto. Per lo schema di crittografia diretto puoi solo selezionare coprimi di N come tuoi messaggi. Questo non ci lascia con molti messaggi possibili, certamente non abbastanza per una comunicazione standard. Inoltre, questi messaggi devono essere selezionati casualmente. Questo sembra alquanto impraticabile. Infine, qualsiasi messaggio che viene selezionato due volte produrrà esattamente lo stesso testo cifrato. Questo è estremamente indesiderabile in qualsiasi schema di crittografia e non soddisfa alcuna nozione moderna rigorosa di sicurezza nella crittografia.

I problemi diventano ancora peggiori per il nostro schema di firma digitale diretto. Così com'è, qualsiasi attaccante può facilmente falsificare firme digitali semplicemente selezionando prima un coprimo di N come firma e poi calcolando il messaggio originale corrispondente. Questo chiaramente infrange il requisito dell'infalsificabilità esistenziale.

Tuttavia, aggiungendo un po' di complessità intelligente, il problema RSA può essere utilizzato per creare uno schema di crittografia a chiave pubblica sicuro così come uno schema di firma digitale sicuro. Non entreremo nei dettagli di tali costruzioni qui.<sup>[4](#footnote4)</sup> Importante, tuttavia, questa complessità aggiuntiva non cambia il problema RSA fondamentale sottostante su cui si basano questi schemi.

### Note

[^1]: La fattorizzazione può anche essere importante per lavorare con altri tipi di oggetti matematici oltre ai numeri. Per esempio, può essere utile fattorizzare espressioni polinomiali come x^2 – 2x + 1. Nella nostra discussione, ci concentreremo solo sulla fattorizzazione dei numeri, specificamente degli interi [^1].
[^2]: Secondo il teorema dei numeri primi, il numero di primi minori o uguali a N è approssimativamente N/ln(N). Questo significa che è possibile approssimare il numero di primi di lunghezza 1024 bit con 2^1024/ln(2^1024) - 2^1023/ln(2^1023) che è approssimativamente 1.265 x 10^305 [^2].

# Contributi
<partId>4556aab1-4876-552a-b6db-df6837bbf27a</partId>

## Informazioni
<chapterId>ff08a57b-740f-5d7e-8cf2-81db0908166e</chapterId>

Qualsiasi contributo è molto ben accetto. Prima di farlo, per favore dai un'occhiata qui sotto per informazioni di base sui miei piani per il libro così come le linee guida per fare contributi.

### Piani attuali

I miei piani attuali per ulteriori sviluppi del libro sono i seguenti:

- Creare un capitolo finale che approfondisca i dettagli delle applicazioni pratiche della crittografia, come la sicurezza del livello di trasporto, il routing onion e lo scambio di valore in Bitcoin
- Creare figure e diagrammi migliori e più dettagliati per supportare la discussione scritta
- Usare LaTeX Math o qualche altra applicazione di composizione tipografica per la notazione formale (piuttosto che solo Markdown)

### Linee guida per i contributi

Se hai correzioni minori o suggerimenti riguardo al testo esistente, puoi creare una pull request o segnalare un problema. Se crei una pull request, per favore tieni presente le seguenti linee guida:

- Crea i commit su un ramo separato nel tuo fork del repository
- Etichetta chiaramente i commit
- Crea commit separati per questioni logicamente distinte per rendere il processo di revisione più facile

Se hai suggerimenti più sostanziali riguardo al libro, per favore segnala un problema o contattami direttamente a **jaburgers@protonmail.com**.

### Licenza

Il lavoro in questo repository è concesso in licenza sotto la Licenza Internazionale Creative Commons Attribuzione-NonCommerciale-SenzaDerivati 4.0 (CC BY-NC-ND 4.0).

Puoi trovare una breve descrizione della licenza [qui](https://creativecommons.org/licenses/by-nc-nd/4.0/).

Puoi trovare una versione completa della licenza [qui](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode).

## Notazione
<chapterId>07250f8d-ad7c-5531-a70c-4417d6d1b865</chapterId>

### Termini chiave

I termini chiave nei primi approcci sono introdotti rendendoli in grassetto. Per esempio, l'introduzione del cifrario di Rijndael come termine chiave apparirebbe così: **cifrario di Rijndael**.

I termini chiave sono esplicitamente definiti, a meno che non siano nomi propri o il loro significato sia ovvio dalla discussione.

Qualsiasi definizione è solitamente data all'introduzione di un termine chiave, anche se a volte è più conveniente lasciare la definizione a un punto successivo.

### Parole e frasi enfatizzate

Le parole e le frasi sono enfatizzate tramite il corsivo. Per esempio, la frase "Ricorda la tua password" apparirebbe così: *Ricorda la tua password*.

### Notazione formale

La notazione formale riguarda principalmente variabili, variabili casuali e insiemi.

* Variabili: Queste sono solitamente indicate solo da una lettera minuscola (ad es., "x" o "y"). A volte sono capitalizzate per chiarezza (ad es., "M" o "K").
* Variabili casuali: Queste sono sempre indicate da una lettera maiuscola (ad es., "X" o "Y").
* Insiemi: Questi sono sempre indicati con lettere maiuscole in grassetto (ad esempio, **S**)
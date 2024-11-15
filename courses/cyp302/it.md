---
name: Introduzione alla crittografia formale
goal: Un'introduzione approfondita alla scienza e alla pratica della crittografia.
objectives:
  - Esplorare i cifrari di Beale e i metodi crittografici moderni per comprendere i concetti di base e storici della crittografia.
  - Approfondire la teoria dei numeri, i gruppi e i campi per padroneggiare i concetti matematici chiave che stanno alla base della crittografia.
  - Studiare il cifrario a flusso RC4 e l'AES con chiave a 128 bit per apprendere sugli algoritmi crittografici simmetrici.
  - Investigare il criptosistema RSA, la distribuzione delle chiavi e le funzioni hash per esplorare la crittografia asimmetrica.

---

# Approfondimento sulla crittografia

È difficile trovare molti materiali che offrano un buon compromesso nell'educazione crittografica.

Da un lato, ci sono trattati formali e lunghi, realmente accessibili solo a coloro che hanno una solida formazione in matematica, logica o qualche altra disciplina formale. Dall'altro lato, ci sono introduzioni molto generali che nascondono troppi dettagli per chiunque sia almeno un po' curioso.

Questa introduzione alla crittografia cerca di catturare il punto di mezzo. Sebbene dovrebbe essere relativamente impegnativa e dettagliata per chiunque sia nuovo alla crittografia, non è il labirinto di un tipico trattato fondazionale.

+++

# Introduzione
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Breve descrizione
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Questo libro offre un'introduzione approfondita alla scienza e alla pratica della crittografia. Dove possibile, si concentra su una esposizione concettuale, piuttosto che formale, del materiale.

> Questo corso si basa sul [repo di JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Tutti i diritti a lui. Il contenuto non è ancora finito ed è qui solo per mostrare come potremmo integrarlo se JWburger's fosse d'accordo.

### Motivazione e obiettivi

È difficile trovare molti materiali che offrano un buon compromesso nell'educazione crittografica.

Da un lato, ci sono trattati formali e lunghi, realmente accessibili solo a coloro che hanno una solida formazione in matematica, logica o qualche altra disciplina formale. Dall'altro lato, ci sono introduzioni molto generali che nascondono troppi dettagli per chiunque sia almeno un po' curioso.

Questa introduzione alla crittografia cerca di catturare il punto di mezzo. Sebbene dovrebbe essere relativamente impegnativa e dettagliata per chiunque sia nuovo alla crittografia, non è il labirinto di un tipico trattato fondazionale.

### Pubblico di riferimento

Dagli sviluppatori ai curiosi intellettualmente, questo libro è utile per chiunque voglia più di una comprensione superficiale della crittografia. Se il tuo obiettivo è padroneggiare il campo della crittografia, allora questo libro è anche un buon punto di partenza.

### Linee guida per la lettura

Il libro attualmente contiene sette capitoli: "Che cos'è la Crittografia?" (Capitolo 1), "Fondamenti Matematici della Crittografia I" (Capitolo 2), "Fondamenti Matematici della Crittografia II" (Capitolo 3), "Crittografia Simmetrica" (Capitolo 4), "RC4 e AES" (Capitolo 5), "Crittografia Asimmetrica" (Capitolo 6) e "Il criptosistema RSA" (Capitolo 7). Un capitolo finale, "La Crittografia nella Pratica", sarà ancora aggiunto. Si concentra su varie applicazioni crittografiche, inclusa la sicurezza del livello di trasporto, il routing a cipolla e il sistema di scambio di valore di Bitcoin.
A meno che tu non abbia una solida formazione in matematica, la teoria dei numeri è probabilmente l'argomento più difficile di questo libro. Offro una panoramica di essa nel Capitolo 3, e appare anche nell'esposizione dell'AES nel Capitolo 5 e del criptosistema RSA nel Capitolo 7.
Se stai davvero lottando con i dettagli formali in queste parti del libro, ti consiglio di accontentarti di una lettura ad alto livello di esse la prima volta.

### Ringraziamenti

Il libro più influente nella formazione di questo è stato _Introduction to Modern Cryptography_ di Jonathan Katz e Yehuda Lindell, CRC Press (Boca Raton, FL), 2015. Un corso accompagnatorio è disponibile su Coursera con il nome "Cryptography".

Le principali fonti aggiuntive che sono state utili nella creazione della panoramica in questo libro sono Simon Singh, _The Code Book_, Fourth Estate (Londra, 1999); Christof Paar e Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) e [un corso basato sul libro di Paar chiamato “Introduction to Cryptography”](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); e Bruce Schneier, Applied Cryptography, 2ª ed., 2015 (Indianapolis, IN: John Wiley & Sons).

Citerò solo informazioni e risultati molto specifici che prendo da queste fonti, ma voglio qui riconoscere il mio debito generale verso di esse.

Per quei lettori che desiderano cercare conoscenze più avanzate sulla crittografia dopo questa introduzione, consiglio vivamente il libro di Katz e Lindell. Il corso di Katz su Coursera è un po' più accessibile del libro.

### Contributi

Si prega di dare un'occhiata [al file dei contributi nel repository](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) per alcune linee guida su come supportare il progetto.

### Notazione

**Termini chiave:**

I termini chiave nei primi approcci sono introdotti rendendoli in grassetto. Per esempio, l'introduzione del cifrario Rijndael come termine chiave apparirebbe come segue: **cifrario Rijndael**.

I termini chiave sono esplicitamente definiti, a meno che non siano nomi propri o il loro significato sia ovvio dalla discussione.

Qualsiasi definizione è solitamente data all'introduzione di un termine chiave, anche se a volte è più conveniente lasciare la definizione fino a un punto successivo.

**Parole e frasi enfatizzate:**

Le parole e le frasi sono enfatizzate tramite il corsivo. Per esempio, la frase "Ricorda la tua password" apparirebbe come segue: *Ricorda la tua password*.

**Notazione formale:**

La notazione formale riguarda principalmente variabili, variabili casuali e insiemi.

* Variabili: Queste sono solitamente indicate solo da una lettera minuscola (ad es., "x" o "y"). A volte sono capitalizzate per chiarezza (ad es., "M" o "K").
* Variabili casuali: Queste sono sempre indicate da una lettera maiuscola (ad es., "X" o "Y")
* Insiemi: Questi sono sempre indicati da lettere maiuscole in grassetto (ad es., **S**)

# Cos'è la Crittografia?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## I cifrari di Beale
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>
Iniziamo la nostra indagine nel campo della crittografia con uno degli episodi più affascinanti e divertenti della sua storia: quello dei cifrari di Beale. [1]
La storia dei cifrari di Beale è, a mio avviso, più probabilmente finzione che realtà. Ma si suppone sia avvenuta come segue.

Nell'inverno del 1820 e del 1822, un uomo di nome Thomas J. Beale soggiornò in una locanda di proprietà di Robert Morriss a Lynchburg (Virginia). Al termine del secondo soggiorno di Beale, egli consegnò a Morriss una scatola di ferro contenente documenti preziosi per la loro custodia.

Qualche mese dopo, Morriss ricevette una lettera da Beale datata 9 maggio 1822. Essa sottolineava il grande valore del contenuto della scatola di ferro e forniva alcune istruzioni a Morriss: se né Beale né nessuno dei suoi associati fossero mai venuti a reclamare la scatola, avrebbe dovuto aprirla esattamente dieci anni dopo la data della lettera (cioè il 9 maggio 1832). Alcuni dei documenti all'interno sarebbero stati scritti in testo normale. Diversi altri, tuttavia, sarebbero stati "incomprensibili senza l'aiuto di una chiave". Questa "chiave" sarebbe stata poi consegnata a Morriss da un amico anonimo di Beale nel giugno del 1832.

Nonostante le istruzioni chiare, Morriss non aprì la scatola nel maggio del 1832 e l'amico misterioso di Beale non si presentò a giugno di quell'anno. Fu solo nel 1845 che l'oste decise finalmente di aprire la scatola. Al suo interno, Morriss trovò una nota che spiegava come Beale e i suoi associati avessero scoperto oro e argento nel West e li avessero sepolti, insieme ad alcuni gioielli, per la loro custodia. Inoltre, la scatola conteneva tre **cifrari**: cioè, testi scritti in codice che richiedono una **chiave crittografica**, o un segreto, e un algoritmo accompagnatorio per essere sbloccati. Questo processo di sblocco di un cifrario è noto come **decrittazione**, mentre il processo di blocco è noto come **crittazione**. (Come spiegato nel Capitolo 3, il termine cifrario può assumere vari significati. Nel nome "cifrari di Beale", sta per cifrati.)

I tre cifrari che Morriss trovò nella scatola di ferro consistono ciascuno in una serie di numeri separati da virgole. Secondo la nota di Beale, questi cifrari forniscono separatamente la posizione del tesoro, il contenuto del tesoro e un elenco di nomi con gli eredi legittimi al tesoro e le loro quote (quest'ultima informazione è rilevante nel caso in cui Beale e i suoi associati non fossero mai venuti a reclamare la scatola).

Morris tentò di decifrare i tre cifrari per vent'anni. Ciò sarebbe stato facile con la chiave. Ma Morriss non aveva la chiave e non ebbe successo nei suoi tentativi di recuperare i testi originali, o **testi in chiaro** come sono tipicamente chiamati in crittografia.

Avvicinandosi alla fine della sua vita, Morriss passò la scatola a un amico nel 1862. Questo amico successivamente pubblicò un opuscolo nel 1885, sotto lo pseudonimo di J.B. Ward. Includeva una descrizione della (presunta) storia della scatola, i tre cifrari e una soluzione che aveva trovato per il secondo cifrario. (A quanto pare, esiste una chiave per ciascun cifrario, e non una chiave unica che funziona su tutti e tre i cifrari come Beale sembrava aver suggerito nella sua lettera a Morriss.)

Puoi vedere il secondo cifrario in *Figura 2* qui sotto. [2] La chiave per questo cifrario è la Dichiarazione d'Indipendenza degli Stati Uniti. La procedura di decrittazione si basa sull'applicazione delle seguenti due regole:
* Per ogni numero n nel testo cifrato, localizza la n-esima parola nella Dichiarazione di Indipendenza degli Stati Uniti* Sostituisci il numero n con la prima lettera della parola che hai trovato

*Figura 1: cifrario di Beale n. 2*

![Figura 1: cifrario di Beale n 2.](assets/Figure1-1.webp "Figura 1: cifrario di Beale n. 2")

Ad esempio, il primo numero del secondo testo cifrato è 115. La 115esima parola della Dichiarazione di Indipendenza è "instituted", quindi la prima lettera del testo in chiaro è "i". Il testo cifrato non indica direttamente gli spazi tra le parole e le maiuscole. Ma dopo aver decifrato le prime parole, si può dedurre logicamente che la prima parola del testo in chiaro era semplicemente "I." (Il testo in chiaro inizia con la frase "I have deposited in the county of Bedford.")

Dopo la decifrazione, il secondo messaggio fornisce i dettagli del contenuto del tesoro (oro, argento e gioielli) e suggerisce che era sepolto in pentole di ferro e coperto con rocce nella contea di Bedford (Virginia). Le persone amano un buon mistero, quindi sono stati fatti grandi sforzi per decifrare gli altri due cifrari di Beale, in particolare quello che descrive la posizione del tesoro. Anche vari crittografi di spicco hanno tentato di risolverli. Tuttavia, fino ad ora, nessuno è stato in grado di decifrare gli altri due testi cifrati.

**Note:**

[1] Per un buon riassunto della storia, vedere Simon Singh, *The Code Book*, Fourth Estate (Londra, 1999), pp. 82-99. Un breve film sulla storia è stato realizzato da Andrew Allen nel 2010. Puoi trovare il film, "The Thomas Beale Cipher," [sul suo sito web](http://www.thomasbealecipher.com/).

[2] Questa immagine è disponibile sulla pagina Wikipedia per i cifrari di Beale.

## Crittografia moderna
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Storie colorate come quella dei cifrari di Beale sono ciò che la maggior parte di noi associa alla crittografia. Tuttavia, la crittografia moderna si differenzia in almeno quattro modi importanti da questi tipi di esempi storici.

Primo, storicamente la crittografia è stata interessata solo alla **segretezza** (o confidenzialità). [3] I testi cifrati venivano creati per garantire che solo certe parti potessero essere a conoscenza delle informazioni nei testi in chiaro, come nel caso dei cifrari di Beale. Affinché uno schema di cifratura serva bene questo scopo, decifrare il testo cifrato dovrebbe essere fattibile solo se si possiede la chiave.

La crittografia moderna si occupa di una gamma più ampia di temi oltre alla semplice segretezza. Questi temi includono principalmente (1) **integrità del messaggio**—cioè, assicurare che un messaggio non sia stato modificato; (2) **autenticità del messaggio**—cioè, assicurare che un messaggio provenga realmente da un mittente particolare; e (3) **non ripudio**—cioè, assicurare che un mittente non possa negare falsamente in seguito di aver inviato un messaggio. [4]

Una distinzione importante da tenere a mente è, quindi, tra uno **schema di cifratura** e uno **schema crittografico**. Uno schema di cifratura è solo interessato alla segretezza. Mentre uno schema di cifratura è uno schema crittografico, il contrario non è vero. Uno schema crittografico può anche servire gli altri temi principali della crittografia, inclusi integrità, autenticità e non ripudio.
I temi dell'integrità e dell'autenticità sono altrettanto importanti quanto la segretezza. I nostri sistemi di comunicazione moderni non sarebbero in grado di funzionare senza garanzie riguardo l'integrità e l'autenticità delle comunicazioni. Anche la non ripudiabilità è una preoccupazione importante, come per i contratti digitali, ma meno ubiquamente necessaria nelle applicazioni crittografiche rispetto alla segretezza, all'integrità e all'autenticità.

In secondo luogo, gli schemi di crittografia classici come i cifrari di Beale coinvolgono sempre una chiave condivisa tra tutte le parti rilevanti. Tuttavia, molti schemi crittografici moderni coinvolgono non una, ma due chiavi: una **privata** e una **pubblica**. Mentre la prima dovrebbe rimanere privata in qualsiasi applicazione, la seconda è tipicamente di conoscenza pubblica (da qui i loro rispettivi nomi). Nel regno della crittografia, la chiave pubblica può essere utilizzata per cifrare il messaggio, mentre la chiave privata può essere utilizzata per decifrarlo.

Il ramo della crittografia che si occupa di schemi in cui tutte le parti condividono una chiave è noto come **crittografia simmetrica**. L'unica chiave in tale schema è solitamente chiamata **chiave privata** (o chiave segreta). Il ramo della crittografia che si occupa di schemi che richiedono una coppia di chiavi privata-pubblica è noto come **crittografia asimmetrica**. Questi rami sono talvolta anche denominati **crittografia a chiave privata** e **crittografia a chiave pubblica**, rispettivamente (anche se ciò può generare confusione, poiché gli schemi crittografici a chiave pubblica hanno anche chiavi private).

L'avvento della crittografia asimmetrica alla fine degli anni '70 è stato uno degli eventi più importanti nella storia della crittografia. Senza di essa, la maggior parte dei nostri sistemi di comunicazione moderni, inclusi Bitcoin, non sarebbero possibili, o almeno molto impraticabili.

Importante, la crittografia moderna non è esclusivamente lo studio degli schemi crittografici a chiave simmetrica e asimmetrica (anche se ciò copre gran parte del campo). Ad esempio, la crittografia si occupa anche di funzioni hash e generatori di numeri pseudocasuali, e si possono costruire applicazioni su queste primitive che non sono correlate alla crittografia a chiave simmetrica o asimmetrica.

Terzo, gli schemi di crittografia classici, come quelli utilizzati nei cifrari di Beale, erano più arte che scienza. La loro sicurezza percepita era in gran parte basata su intuizioni riguardo la loro complessità. Tipicamente venivano corretti quando si apprendeva un nuovo attacco contro di essi, o abbandonati del tutto se l'attacco era particolarmente grave. La crittografia moderna, tuttavia, è una scienza rigorosa con un approccio formale e matematico sia nello sviluppo che nell'analisi degli schemi crittografici.

Specificamente, la crittografia moderna si concentra su **prove formali di sicurezza**. Qualsiasi prova di sicurezza per uno schema crittografico procede in tre passaggi:

1. La dichiarazione di una **definizione crittografica di sicurezza**, ovvero un insieme di obiettivi di sicurezza e la minaccia posta dall'attaccante.
2. La dichiarazione di qualsiasi ipotesi matematica riguardo alla complessità computazionale dello schema. Ad esempio, uno schema crittografico può contenere un generatore di numeri pseudocasuali. Anche se non possiamo dimostrare che esistano, possiamo supporre che lo facciano.
3. L'esposizione di una **prova matematica di sicurezza** dello schema sulla base della nozione formale di sicurezza e di qualsiasi ipotesi matematica.

Quarto, mentre storicamente la crittografia era utilizzata principalmente in ambito militare, è venuta a permeare le nostre attività quotidiane nell'era digitale. Che tu stia facendo operazioni bancarie online, postando sui social media, acquistando un prodotto su Amazon con la tua carta di credito, o inviando una mancia in bitcoin a un amico, la crittografia è il sine qua non della nostra era digitale.

Data queste quattro aspetti della crittografia moderna, potremmo caratterizzare la **crittografia** moderna come la scienza preoccupata dello sviluppo formale e dell'analisi degli schemi crittografici per proteggere le informazioni digitali contro attacchi avversari. La sicurezza qui dovrebbe essere intesa in senso ampio come la prevenzione di attacchi che danneggiano la segretezza, l'integrità, l'autenticazione e/o la non ripudiabilità nelle comunicazioni.
La crittografia è meglio vista come una sottodisciplina della **cybersecurity**, che si occupa di prevenire il furto, il danneggiamento e l'uso improprio dei sistemi informatici. Da notare che molte preoccupazioni legate alla cybersecurity hanno poco o solo un parziale collegamento con la crittografia.
Ad esempio, se un'azienda ospita server costosi localmente, potrebbe essere preoccupata di proteggere questa attrezzatura dal furto e dal danneggiamento. Sebbene questa sia una preoccupazione legata alla cybersecurity, ha poco a che fare con la crittografia.

Per un altro esempio, gli **attacchi di phishing** sono un problema comune nella nostra era moderna. Questi attacchi tentano di ingannare le persone tramite un'e-mail o qualche altro mezzo di messaggistica per indurle a rivelare informazioni sensibili come password o numeri di carte di credito. Sebbene la crittografia possa aiutare a contrastare gli attacchi di phishing fino a un certo punto, un approccio completo richiede più che l'uso della sola crittografia.

**Note:**

[3] Per essere precisi, le applicazioni importanti degli schemi crittografici sono state preoccupate della segretezza. I bambini, ad esempio, usano spesso schemi crittografici semplici per "divertimento". La segretezza non è davvero una preoccupazione in quei casi.

[4] Bruce Schneier, *Applied Cryptography*, 2ª ed., 2015 (Indianapolis, IN: John Wiley & Sons), p. 2.

[5] Vedi Jonathan Katz e Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), spec. pp. 16–23, per una buona descrizione.

[6] Cf. Katz e Lindell, ibid., p. 3. Penso che la loro caratterizzazione abbia alcuni problemi, quindi presento qui una versione leggermente diversa della loro affermazione.

## Comunicazioni aperte
<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

La crittografia moderna è progettata per fornire garanzie di sicurezza in un ambiente di **comunicazioni aperte**. Se il nostro canale di comunicazione è così ben protetto che gli intercettatori non hanno alcuna possibilità di manipolare o anche solo osservare i nostri messaggi, allora la crittografia è superflua. La maggior parte dei nostri canali di comunicazione, tuttavia, è tutt'altro che così ben sorvegliata.

La spina dorsale della comunicazione nel mondo moderno è una vasta rete di cavi in fibra ottica. Effettuare chiamate telefoniche, guardare la televisione e navigare sul web in una casa moderna si basa generalmente su questa rete di cavi in fibra ottica (una piccola percentuale può dipendere esclusivamente da satelliti). È vero che potresti avere diverse connessioni dati nella tua casa, come il cavo coassiale, la linea di abbonamento digitale (asimmetrica) e il cavo in fibra ottica. Ma, almeno nel mondo sviluppato, questi diversi mezzi di dati si uniscono rapidamente fuori dalla tua casa a un nodo in una vasta rete di cavi in fibra ottica che collega l'intero globo. Le eccezioni sono alcune aree remote del mondo sviluppato, come negli Stati Uniti e in Australia, dove il traffico dati potrebbe ancora viaggiare anche per lunghe distanze su tradizionali fili di rame telefonici.

Sarebbe impossibile impedire ai potenziali aggressori di accedere fisicamente a questa rete di cavi e alla sua infrastruttura di supporto. Infatti, sappiamo già che la maggior parte dei nostri dati viene intercettata da varie agenzie di intelligence nazionali in intersezioni cruciali di Internet.[7] Questo include tutto, dai messaggi di Facebook agli indirizzi dei siti web che visiti.

Mentre sorvegliare i dati su larga scala richiede un avversario potente, come un'agenzia di intelligence nazionale, gli aggressori con poche risorse possono facilmente tentare di intercettare su scala più locale. Sebbene ciò possa avvenire a livello di intercettazione dei cavi, è molto più facile intercettare semplicemente le comunicazioni wireless.
La maggior parte dei dati della nostra rete locale, che si trovi nelle nostre case, in ufficio o in un caffè, ora viaggia tramite onde radio verso punti di accesso wireless su router tutto-in-uno, piuttosto che attraverso cavi fisici. Quindi, un attaccante necessita di poche risorse per intercettare qualsiasi traffico locale. Questo è particolarmente preoccupante poiché la maggior parte delle persone fa molto poco per proteggere i dati che viaggiano attraverso le loro reti locali. Inoltre, potenziali attaccanti possono anche prendere di mira le nostre connessioni a banda larga mobile, come 3G, 4G e 5G. Tutte queste comunicazioni wireless sono un facile bersaglio per gli attaccanti.
Pertanto, l'idea di mantenere segrete le comunicazioni proteggendo il canale di comunicazione è un'aspirazione irrealizzabile per gran parte del mondo moderno. Tutto ciò che sappiamo giustifica una severa paranoia: dovresti sempre presumere che qualcuno stia ascoltando. E la crittografia è il principale strumento che abbiamo per ottenere un qualche tipo di sicurezza in questo ambiente moderno.

**Note:**

[7] Vedi, per esempio, Olga Khazan, “The creepy, long-standing practice of undersea cable tapping”, *The Atlantic*, 16 luglio 2013 (disponibile su [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Fondamenti Matematici della Crittografia 1
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Variabili casuali
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

La crittografia si basa sulla matematica. E se vuoi costruire una comprensione della crittografia che vada oltre il superficiale, devi essere a tuo agio con quella matematica.

Questo capitolo introduce la maggior parte delle matematiche di base che incontrerai nell'apprendimento della crittografia. Gli argomenti includono variabili casuali, operazioni modulo, operazioni XOR e pseudocasualità. Dovresti padroneggiare il materiale in queste sezioni per qualsiasi comprensione non superficiale della crittografia.

La prossima sezione tratta della teoria dei numeri, che è molto più impegnativa.

### Variabili casuali

Una variabile casuale è tipicamente denotata da una lettera maiuscola non in grassetto. Quindi, per esempio, potremmo parlare di una variabile casuale $X$, una variabile casuale $Y$ o una variabile casuale $Z$. Questa è la notazione che utilizzerò anche da qui in avanti.

Una **variabile casuale** può assumere due o più valori possibili, ognuno con una certa probabilità positiva. I valori possibili sono elencati nel **set di esiti**.

Ogni volta che **campioni** una variabile casuale, estrai un valore particolare dal suo set di esiti secondo le probabilità definite.

Passiamo a un esempio semplice. Supponiamo una variabile $X$ che è definita come segue:

- $X$ ha il set di esiti $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

È facile vedere che $X$ è una variabile casuale. Primo, ci sono due o più valori possibili che $X$ può assumere, cioè $1$ e $2$. Secondo, ogni valore possibile ha una probabilità positiva di verificarsi ogni volta che campioni $X$, cioè $0.5$.
Tutto ciò che una variabile casuale richiede è un insieme di esiti con due o più possibilità, dove ogni possibilità ha una probabilità positiva di verificarsi al momento del campionamento. In principio, quindi, una variabile casuale può essere definita in modo astratto, priva di qualsiasi contesto. In questo caso, potresti pensare al "campionamento" come all'esecuzione di un esperimento naturale per determinare il valore della variabile casuale.
La variabile $X$ sopra è stata definita in modo astratto. Potresti, quindi, pensare di campionare la variabile $X$ sopra come lanciare una moneta equa e assegnare "2" in caso di testa e "1" in caso di croce. Per ogni campione di $X$, lanci di nuovo la moneta.

Alternativamente, potresti anche pensare di campionare $X$, come lanciare un dado equo e assegnare "2" nel caso in cui il dado mostri $1$, $3$, o $4$, e assegnare "1" nel caso in cui il dado mostri $2$, $5$, o $6$. Ogni volta che campioni $X$, lanci di nuovo il dado.

Veramente, qualsiasi esperimento naturale che ti permetterebbe di definire le probabilità dei possibili valori di $X$ sopra può essere immaginato rispetto al disegno.

Frequentemente, tuttavia, le variabili casuali non sono solo introdotte in modo astratto. Invece, l'insieme dei possibili valori di esito ha un significato esplicito nel mondo reale (piuttosto che solo come numeri). Inoltre, questi valori di esito potrebbero essere definiti rispetto a un tipo specifico di esperimento (piuttosto che come qualsiasi esperimento naturale con quei valori).

Consideriamo ora un esempio di variabile $X$ che non è definita in modo astratto. X è definita come segue per determinare quale delle due squadre inizia una partita di calcio:

- $X$ ha l'insieme di esiti {calcio d'inizio rosso, calcio d'inizio blu}
- Lancio di una moneta particolare $C$: croce = "calcio d'inizio rosso"; testa = "calcio d'inizio blu"

$$
Pr [X = \text{calcio d'inizio rosso}] = 0.5
$$

$$
Pr [X = \text{calcio d'inizio blu}] = 0.5
$$

In questo caso, l'insieme di esiti di X è fornito con un significato concreto, ovvero quale squadra inizia in una partita di calcio. Inoltre, i possibili esiti e le loro probabilità associate sono determinati da un esperimento concreto, ovvero lanciando una moneta particolare $C$.

Nelle discussioni sulla crittografia, le variabili casuali sono solitamente introdotte rispetto a un insieme di esiti con un significato nel mondo reale. Potrebbe trattarsi dell'insieme di tutti i messaggi che potrebbero essere criptati, noto come spazio dei messaggi, o dell'insieme di tutte le chiavi che le parti che utilizzano la crittografia possono scegliere, noto come spazio delle chiavi.

Le variabili casuali nelle discussioni sulla crittografia, tuttavia, non sono solitamente definite rispetto a un esperimento naturale specifico, ma rispetto a qualsiasi esperimento che potrebbe produrre le giuste distribuzioni di probabilità.

Le variabili casuali possono avere distribuzioni di probabilità discrete o continue. Le variabili casuali con una **distribuzione di probabilità discreta**—cioè, variabili casuali discrete—hanno un numero finito di possibili esiti. La variabile casuale $X$ negli esempi finora dati era discreta.

Le **variabili casuali continue** possono invece assumere valori in uno o più intervalli. Potresti dire, ad esempio, che una variabile casuale, al momento del campionamento, assumerà qualsiasi valore reale tra 0 e 1, e che ogni numero reale in questo intervallo è ugualmente probabile. All'interno di questo intervallo, ci sono infiniti valori possibili.

Per le discussioni sulla crittografia, avrai bisogno di comprendere solo le variabili casuali discrete. Qualsiasi discussione sulle variabili casuali da qui in poi dovrebbe, quindi, essere intesa come riferita a variabili casuali discrete, a meno che non sia specificato diversamente.
I valori possibili e le probabilità associate a una variabile casuale possono essere facilmente visualizzati attraverso un grafico. Per esempio, consideriamo la variabile casuale $X$ della sezione precedente con un insieme di risultati $\{1, 2\}$, e $Pr [X = 1] = 0.5$ e $Pr [X = 2] = 0.5$. Tipicamente, visualizzeremmo una tale variabile casuale sotto forma di un grafico a barre come in *Figura 1*.
*Figura 1: Variabile casuale X*

![Figura 1: Variabile casuale X.](assets/Figure2-1.webp)

Le barre larghe in *Figura 1* ovviamente non intendono suggerire che la variabile casuale $X$ sia effettivamente continua. Invece, le barre sono rese larghe al fine di essere più visivamente accattivanti (solo una linea dritta verso l'alto fornisce una visualizzazione meno intuitiva).

### Variabili uniformi

Nell'espressione "variabile casuale", il termine "casuale" significa semplicemente "probabilistico". In altre parole, significa solo che due o più possibili risultati della variabile si verificano con certe probabilità. Questi risultati, tuttavia, non devono necessariamente essere ugualmente probabili (anche se il termine "casuale" può effettivamente avere quel significato in altri contesti).

Una **variabile uniforme** è un caso speciale di variabile casuale. Può assumere due o più valori tutti con la stessa probabilità. La variabile casuale $X$ rappresentata in *Figura 1* è chiaramente una variabile uniforme, poiché entrambi i possibili risultati si verificano con una probabilità $0.5$. Ci sono, tuttavia, molte variabili casuali che non sono istanze di variabili uniformi.

Consideriamo, per esempio, la variabile casuale $Y$. Ha un insieme di risultati $\{1, 2, 3, 8, 10\}$ e la seguente distribuzione di probabilità:

$$
\Pr[Y = 1] = 0.25
$$

$$
\Pr[Y = 2] = 0.35
$$

$$
\Pr[Y = 3] = 0.1
$$

$$
\Pr[Y = 8] = 0.25
$$

$$
\Pr[Y = 10] = 0.05
$$

Mentre due possibili risultati hanno effettivamente una probabilità uguale di verificarsi, ovvero $1$ e $8$, $Y$ può anche assumere certi valori con probabilità diverse da $0.25$ al campionamento. Pertanto, mentre $Y$ è effettivamente una variabile casuale, non è una variabile uniforme.

Una rappresentazione grafica di $Y$ è fornita in *Figura 2*.

*Figura 2: Variabile casuale Y*

![Figura 2: Variabile casuale Y.](assets/Figure2-2.webp "Figura 2: Variabile casuale Y")

Per un ultimo esempio, consideriamo la variabile casuale Z. Ha l'insieme di risultati {1,3,7,11,12} e la seguente distribuzione di probabilità:

$$
\Pr[Z = 2] = 0.2
$$

$$
\Pr[Z = 3] = 0.2
$$

$$
\Pr[Z = 9] = 0.2
$$

$$
\Pr[Z = 11] = 0.2
$$

$$
\Pr[Z = 12] = 0.2
$$

Puoi vederla rappresentata in *Figura 3*. La variabile casuale Z, a differenza di Y, è una variabile uniforme, poiché tutte le probabilità per i possibili valori al campionamento sono uguali.

*Figura 3: Variabile casuale Z*
![Figura 3: Variabile casuale Z.](assets/Figure2-3.webp "Figura 3: Variabile casuale Z")

### Probabilità condizionata

Supponiamo che Bob intenda selezionare uniformemente un giorno dell'ultimo anno solare. Cosa dovremmo concludere riguardo alla probabilità che il giorno selezionato sia in estate?

Finché pensiamo che il processo di Bob sarà davvero uniforme, dovremmo concludere che c'è una probabilità di 1/4 che Bob selezioni un giorno d'estate. Questa è la **probabilità incondizionata** che il giorno selezionato casualmente sia in estate.

Supponiamo ora che, invece di estrarre uniformemente un giorno del calendario, Bob selezioni uniformemente solo tra quei giorni in cui la temperatura di mezzogiorno a Crystal Lake (New Jersey) era di 21 gradi Celsius o superiore. Data questa informazione aggiuntiva, cosa possiamo concludere sulla probabilità che Bob selezioni un giorno d'estate?

Dovremmo davvero trarre una conclusione diversa da prima, anche senza ulteriori informazioni specifiche (ad esempio, la temperatura di mezzogiorno di ogni giorno dell'ultimo anno solare).

Sapendo che Crystal Lake si trova nel New Jersey, certamente non ci aspetteremmo che la temperatura di mezzogiorno sia di 21 gradi Celsius o superiore in inverno. Invece, è molto più probabile che sia una giornata calda in primavera o autunno, o un giorno in estate. Quindi, sapendo che la temperatura di mezzogiorno a Crystal Lake nel giorno selezionato era di 21 gradi Celsius o superiore, la probabilità che il giorno selezionato da Bob sia in estate diventa molto più alta. Questa è la **probabilità condizionata** che il giorno selezionato casualmente sia in estate, dato che la temperatura di mezzogiorno a Crystal Lake era di 21 gradi Celsius o superiore.

A differenza dell'esempio precedente, le probabilità di due eventi possono anche essere completamente non correlate. In tal caso, diciamo che sono **indipendenti**.

Supponiamo, ad esempio, che una certa moneta equa sia atterrata su testa. Dato questo fatto, qual è quindi la probabilità che domani piova? La probabilità condizionata in questo caso dovrebbe essere la stessa della probabilità incondizionata che domani piova, poiché il lancio di una moneta generalmente non ha alcun impatto sul tempo.

Usiamo un simbolo "|" per scrivere le affermazioni di probabilità condizionata. Ad esempio, la probabilità dell'evento $A$ dato che l'evento $B$ si è verificato può essere scritta come segue:

$$
Pr[A|B]
$$

Quindi, quando due eventi, $A$ e $B$, sono indipendenti, allora:

$$
Pr[A|B] = Pr[A] \text{ e } Pr[B|A] = Pr[B]
$$

La condizione per l'indipendenza può essere semplificata come segue:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Un risultato chiave nella teoria della probabilità è noto come **Teorema di Bayes**. Esso afferma sostanzialmente che $Pr[A|B]$ può essere riscritto come segue:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

Invece di usare le probabilità condizionate con eventi specifici, possiamo anche guardare alle probabilità condizionate coinvolte con due o più variabili casuali su un insieme di possibili eventi. Supponiamo due variabili casuali, $X$ e $Y$. Possiamo denotare qualsiasi valore possibile per $X$ con $x$, e qualsiasi valore possibile per $Y$ con $y$. Potremmo dire, quindi, che due variabili casuali sono indipendenti se vale la seguente affermazione:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

per tutti i valori di $x$ e $y$.

Siamo un po' più espliciti su cosa significa questa affermazione.
Supponiamo che i set di risultati per $X$ e $Y$ siano definiti come segue: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ e **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (È tipico indicare i set di valori con lettere maiuscole in grassetto.)
Ora supponiamo che tu campioni $Y$ e osservi $y_1$. La dichiarazione sopra ci dice che la probabilità di ottenere ora $x_1$ campionando $X$ è esattamente la stessa come se non avessimo mai osservato $y_1$. Questo è vero per qualsiasi $y_i$ che avremmo potuto estrarre dal nostro campionamento iniziale di $Y$. Infine, questo vale non solo per $x_1$. Per qualsiasi $x_i$, la probabilità di verificarsi non è influenzata dal risultato di un campionamento di $Y$. Tutto questo si applica anche al caso in cui $X$ sia campionato per primo.

Concludiamo la nostra discussione su un punto leggermente più filosofico. In qualsiasi situazione reale, la probabilità di un evento è sempre valutata rispetto a un particolare insieme di informazioni. Non esiste una "probabilità incondizionata" in nessun senso molto stretto della parola.

Ad esempio, supponiamo che ti chiedessi la probabilità che i maiali voleranno entro il 2030. Anche se non ti do ulteriori informazioni, tu chiaramente sai molto sul mondo che può influenzare il tuo giudizio. Non hai mai visto maiali volare. Sai che la maggior parte delle persone non si aspetterà che volino. Sai che non sono davvero fatti per volare. E così via.

Pertanto, quando parliamo di una "probabilità incondizionata" di un evento in un contesto reale, quel termine può davvero avere significato solo se lo intendiamo come "la probabilità senza ulteriori informazioni esplicite". Qualsiasi comprensione di una "probabilità condizionata" dovrebbe, quindi, essere sempre intesa rispetto a un pezzo specifico di informazione.

Potrei, ad esempio, chiederti la probabilità che i maiali voleranno entro il 2030, dopo averti dato la prova che alcune capre in Nuova Zelanda hanno imparato a volare dopo alcuni anni di addestramento. In questo caso, probabilmente aggiusterai il tuo giudizio sulla probabilità che i maiali voleranno entro il 2030. Quindi la probabilità che i maiali voleranno entro il 2030 è condizionata da questa prova riguardante le capre in Nuova Zelanda.

## L'operazione modulo
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Modulo

L'espressione più basilare con l'**operazione modulo** è della seguente forma: $x \mod y$.

La variabile $x$ è chiamata dividendo e la variabile $y$ il divisore. Per eseguire un'operazione modulo con un dividendo positivo e un divisore positivo, si determina semplicemente il resto della divisione.

Ad esempio, considera l'espressione $25 \mod 4$. Il numero 4 entra nel numero 25 un totale di 6 volte. Il resto di quella divisione è 1. Quindi, $25 \mod 4$ è uguale a 1. In modo simile, possiamo valutare le espressioni qui sotto:

* $29 \mod 30 = 29$ (poiché 30 entra in 29 un totale di 0 volte e il resto è 29)
* $42 \mod 2 = 0$ (poiché 2 entra in 42 un totale di 21 volte e il resto è 0)
* $12 \mod 5 = 2$ (poiché 5 entra in 12 un totale di 2 volte e il resto è 2)
* $20 \mod 8 = 4$ (poiché 8 entra in 20 un totale di 2 volte e il resto è 4)

Quando il dividendo o il divisore è negativo, le operazioni di modulo possono essere gestite diversamente dai linguaggi di programmazione.

Incontrerai sicuramente casi con un dividendo negativo in crittografia. In questi casi, l'approccio tipico è il seguente:

* Prima determina il valore più vicino *inferiore o uguale* al dividendo in cui il divisore divide con un resto di zero. Chiamiamo quel valore $p$.
* Se il dividendo è $x$, allora il risultato dell'operazione di modulo è il valore di $x - p$.

Per esempio, supponiamo che il dividendo sia $-20$ e il divisore 3. Il valore più vicino inferiore o uguale a $-20$ in cui 3 divide uniformemente è $-21$. Il valore di $x - p$ in questo caso è $-20 - (-21)$. Questo equivale a 1 e, quindi, $-20 \mod 3$ equivale a 1. In modo simile, possiamo valutare le espressioni sottostanti:

* $-8 \mod 5 = 2$
* $-19 \mod 16 = 13$
* $-14 \mod 6 = 4$

Riguardo alla notazione, tipicamente vedrai i seguenti tipi di espressioni: $x = [y \mod z]$. A causa delle parentesi, l'operazione di modulo in questo caso si applica solo al lato destro dell'espressione. Se $y$ è uguale a 25 e $z$ è uguale a 4, per esempio, allora $x$ si valuta a 1.

Senza parentesi, l'operazione di modulo agisce su *entrambi i lati* di un'espressione. Supponiamo, per esempio, la seguente espressione: $x = y \mod z$. Se $y$ è uguale a 25 e $z$ è uguale a 4, allora tutto ciò che sappiamo è che $x \mod 4$ si valuta a 1. Questo è coerente con qualsiasi valore per $x$ dall'insieme $\{\ldots,-7, -3, 1, 5, 9,\ldots\}$.

Il ramo della matematica che coinvolge operazioni di modulo su numeri ed espressioni è denominato **aritmetica modulare**. Puoi pensare a questo ramo come l'aritmetica per casi in cui la linea numerica non è infinitamente lunga. Anche se tipicamente incontriamo operazioni di modulo per interi (positivi) nella crittografia, puoi anche eseguire operazioni di modulo usando qualsiasi numero reale.

### Il cifrario di Cesare

L'operazione di modulo è frequentemente incontrata nella crittografia. Per illustrare, consideriamo uno degli schemi di cifratura storici più famosi: il cifrario di Cesare.

Definiamolo prima. Supponiamo un dizionario *D* che equipara tutte le lettere dell'alfabeto inglese, in ordine, con l'insieme di numeri $\{0, 1, 2, \ldots, 25\}$. Assumiamo uno spazio dei messaggi **M**. Il **cifrario di Cesare** è, quindi, uno schema di cifratura definito come segue:

- Seleziona uniformemente una chiave $k$ dallo spazio delle chiavi **K**, dove **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Cifra un messaggio $m \in \mathbf{M}$, come segue:
    - Separa $m$ nelle sue singole lettere $m_0, m_1, \ldots, m_i, \ldots, m_l$
- Converti ogni $m_i$ in un numero secondo *D*
    - Per ogni $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Converti ogni $c_i$ in una lettera secondo *D*
    - Poi combina $c_0, c_1, \ldots, c_l$ per ottenere il testo cifrato $c$
- Decifra un testo cifrato $c$ come segue:
    - Converti ogni $c_i$ in un numero secondo *D*
    - Per ogni $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Converti ogni $m_i$ in una lettera secondo *D*
    - Poi combina $m_0, m_1, \ldots, m_l$ per ottenere il messaggio originale $m$

L'operatore modulo nel cifrario a traslazione assicura che le lettere si avvolgano, in modo che tutte le lettere del testo cifrato siano definite. Per illustrare, considera l'applicazione del cifrario a traslazione sulla parola "DOG".

Supponi di aver selezionato uniformemente un valore di chiave pari a 17. La lettera "O" equivale a 15. Senza l'operazione modulo, l'addizione di questo numero di testo in chiaro con la chiave risulterebbe in un numero di testo cifrato di 32. Tuttavia, quel numero di testo cifrato non può essere trasformato in una lettera di testo cifrato, poiché l'alfabeto inglese ha solo 26 lettere. L'operazione modulo assicura che il numero di testo cifrato sia in realtà 6 (il risultato di $32 \mod 26$), che equivale alla lettera di testo cifrato "G".

L'intera cifratura della parola "DOG" con un valore di chiave di 17 è la seguente:

* Messaggio = DOG = D,O,G = 3,15,6
* $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
* $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
* $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
* $c = UGX$

Tutti possono intuitivamente capire come funziona il cifrario a traslazione e probabilmente usarlo da soli. Tuttavia, per avanzare nella conoscenza della crittografia, è importante iniziare a sentirsi più a proprio agio con la formalizzazione, poiché gli schemi diventeranno molto più complessi. Ecco perché i passaggi per il cifrario a traslazione sono stati formalizzati.

**Note:**

[1] Possiamo definire esattamente questa affermazione, usando la terminologia della sezione precedente. Lascia che una variabile uniforme $K$ abbia $K$ come insieme di possibili risultati. Quindi:

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...e così via. Campiona la variabile uniforme $K$ una volta per ottenere una chiave particolare.

## L'operazione XOR
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Tutti i dati informatici vengono elaborati, memorizzati e inviati attraverso le reti a livello di bit. Anche gli schemi crittografici applicati ai dati informatici operano a livello di bit.

Ad esempio, supponi di aver digitato un'e-mail nella tua applicazione di posta elettronica. Qualsiasi cifratura applichi non avviene direttamente sui caratteri ASCII della tua e-mail. Invece, viene applicata alla rappresentazione in bit delle lettere e degli altri simboli nella tua e-mail.
Un'operazione matematica chiave da comprendere per la crittografia moderna, oltre all'operazione di modulo, è quella dell'**operazione XOR**, o operazione di "o esclusivo". Questa operazione prende in input due bit e produce in output un altro bit. L'operazione XOR sarà semplicemente indicata come "XOR". Produce 0 se i due bit sono uguali e 1 se i due bit sono diversi. Puoi vedere le quattro possibilità di seguito. Il simbolo $\oplus$ rappresenta "XOR":
* $0 \oplus 0 = 0$
* $0 \oplus 1 = 1$
* $1 \oplus 0 = 1$
* $1 \oplus 1 = 0$

Per illustrare, supponiamo che tu abbia un messaggio $m_1$ (01111001) e un messaggio $m_2$ (01011001). L'operazione XOR di questi due messaggi può essere vista di seguito.

* $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$

Il processo è semplice. Prima esegui l'XOR dei bit più a sinistra di $m_1$ e $m_2$. In questo caso è $0 \oplus 0 = 0$. Poi esegui l'XOR della seconda coppia di bit da sinistra. In questo caso è $1 \oplus 1 = 0$. Continui questo processo fino ad aver eseguito l'operazione XOR sui bit più a destra.

È facile vedere che l'operazione XOR è commutativa, cioè $m_1 \oplus m_2 = m_2 \oplus m_1$. Inoltre, l'operazione XOR è anche associativa. Cioè, $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

Un'operazione XOR su due stringhe di lunghezze alternative può avere interpretazioni diverse, a seconda del contesto. Qui non ci occuperemo di operazioni XOR su stringhe di lunghezze diverse.

Un'operazione XOR è equivalente al caso speciale di esecuzione di un'operazione di modulo sull'addizione di bit quando il divisore è 2. Puoi vedere l'equivalenza nei seguenti risultati:

* $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
* $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
* $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
* $(1 + 1) \mod 2 = 1 \oplus 1 = 0$

## Pseudocasualità

Nella nostra discussione sulle variabili casuali e uniformi, abbiamo tracciato una distinzione specifica tra "casuale" e "uniforme". Questa distinzione è tipicamente mantenuta nella pratica quando si descrivono le variabili casuali. Tuttavia, nel nostro contesto attuale, questa distinzione deve essere abbandonata e "casuale" e "uniforme" sono usati sinonimamente. Spiegherò il motivo alla fine della sezione.

Per iniziare, possiamo definire una stringa binaria di lunghezza $n$ **casuale** (o **uniforme**), se è stata il risultato del campionamento di una variabile uniforme $S$ che dà a ogni stringa binaria di tale lunghezza $n$ una probabilità uguale di selezione.
Supponiamo, per esempio, l'insieme di tutte le stringhe binarie di lunghezza 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (È tipico scrivere una stringa di 8 bit in due quartetti, ciascuno chiamato **nibble**.) Chiamiamo questo insieme di stringhe **$S_8$**.
Secondo la definizione sopra, possiamo quindi dire che una particolare stringa binaria di lunghezza 8 è casuale (o uniforme), se è stata il risultato del campionamento di una variabile uniforme $S$ che dà a ogni stringa in **$S_8$** una probabilità uguale di selezione. Dato che l'insieme **$S_8$** include $2^8$ elementi, la probabilità di selezione al campionamento dovrebbe essere di $1/2^8$ per ogni stringa nell'insieme.

Un aspetto chiave della casualità di una stringa binaria è che è definita in riferimento al processo tramite il quale è stata selezionata. La forma di una particolare stringa binaria di per sé, quindi, non rivela nulla sulla sua casualità nella selezione.

Per esempio, molte persone intuitivamente hanno l'idea che una stringa come $1111\ 1111$ non possa essere stata selezionata casualmente. Ma questo è chiaramente falso.

Definendo una variabile uniforme $S$ su tutte le stringhe binarie di lunghezza 8, la probabilità di selezionare $1111\ 1111$ dall'insieme **$S_8$** è la stessa di quella di una stringa come $0111\ 0100$. Quindi, non puoi dire nulla sulla casualità di una stringa, semplicemente analizzando la stringa stessa.

Possiamo anche parlare di stringhe casuali senza specificamente intendere stringhe binarie. Potremmo, per esempio, parlare di una stringa esadecimale casuale $AF\ 02\ 82$. In questo caso, la stringa sarebbe stata selezionata casualmente dall'insieme di tutte le stringhe esadecimali di lunghezza 6. Questo è equivalente a selezionare casualmente una stringa binaria di lunghezza 24, poiché ogni cifra esadecimale rappresenta 4 bit.

Tipicamente l'espressione “una stringa casuale”, senza qualificazioni, si riferisce a una stringa selezionata casualmente dall'insieme di tutte le stringhe della stessa lunghezza. È così che l'ho descritto sopra. Una stringa di lunghezza $n$ può, naturalmente, essere anche selezionata casualmente da un insieme diverso. Uno, per esempio, che costituisce solo un sottoinsieme di tutte le stringhe di lunghezza $n$, o forse un insieme che include stringhe di lunghezza variabile. In questi casi, tuttavia, non ci riferiremmo ad essa come a “una stringa casuale”, ma piuttosto “una stringa che è stata selezionata casualmente da qualche insieme **S**”.

Un concetto chiave all'interno della crittografia è quello di pseudocasualità. Una **stringa pseudocasuale** di lunghezza $n$ appare *come se* fosse stata il risultato del campionamento di una variabile uniforme $S$ che dà a ogni stringa in **$S_n$** una probabilità uguale di selezione. In realtà, tuttavia, la stringa è il risultato del campionamento di una variabile uniforme $S'$ che definisce solo una distribuzione di probabilità—non necessariamente una con probabilità uguali per tutti i possibili esiti—su un sottoinsieme di **$S_n$**. Il punto cruciale qui è che nessuno può realmente distinguere tra campioni da $S$ e $S'$, anche se ne prendi molti.
Supponiamo, per esempio, una variabile casuale $S$. Il suo insieme di risultati è **$S_{256}$**, ovvero l'insieme di tutte le stringhe binarie di lunghezza 256. Questo insieme ha $2^{256}$ elementi. Ogni elemento ha una probabilità uguale di selezione, $1/2^{256}$, quando viene campionato.
Inoltre, supponiamo una variabile casuale $S'$. Il suo insieme di risultati include solo $2^{128}$ stringhe binarie di lunghezza 256. Ha una certa distribuzione di probabilità su quelle stringhe, ma questa distribuzione non è necessariamente uniforme.

Supponiamo ora che io abbia preso migliaia di campioni da $S$ e migliaia di campioni da $S'$ e ti abbia dato i due insiemi di risultati. Ti dico a quale variabile casuale è associato ciascun insieme di risultati. Successivamente, prendo un campione da una delle due variabili casuali. Ma questa volta non ti dico da quale variabile casuale ho preso il campione. Se $S'$ fosse pseudocasuale, allora l'idea è che la tua probabilità di fare la scelta giusta su quale variabile casuale ho campionato è praticamente non migliore di $1/2$.

Tipicamente, una stringa pseudocasuale di lunghezza $n$ è prodotta selezionando casualmente una stringa di dimensione $n – x$, dove $x$ è un intero positivo, e usandola come input per un algoritmo di espansione. Questa stringa casuale di dimensione $n – x$ è conosciuta come il **seme**.

Le stringhe pseudocasuali sono un concetto chiave per rendere la crittografia pratica. Considera, per esempio, i cifrari a flusso. Con un cifrario a flusso, una chiave selezionata casualmente è inserita in un algoritmo di espansione per produrre una stringa pseudocasuale molto più grande. Questa stringa pseudocasuale è poi combinata con il testo in chiaro tramite un'operazione XOR per produrre un testo cifrato.

Se non fossimo in grado di produrre questo tipo di stringa pseudocasuale per un cifrario a flusso, allora avremmo bisogno di una chiave lunga quanto il messaggio per la sua sicurezza. Questa non è un'opzione molto pratica nella maggior parte dei casi.

La nozione di pseudocasualità discussa in questa sezione può essere definita più formalmente. Si estende anche ad altri contesti. Ma non è necessario approfondire questa discussione qui. Tutto ciò di cui hai davvero bisogno per comprendere intuitivamente gran parte della crittografia è la differenza tra una stringa casuale e una pseudocasuale. [2]

Il motivo per cui si abbandona la distinzione tra “casuale” e “uniforme” nella nostra discussione dovrebbe ora essere anche chiaro. Nella pratica, tutti usano il termine pseudocasuale per indicare una stringa che appare **come se** fosse il risultato del campionamento di una variabile uniforme $S$. A rigor di termini, dovremmo chiamare una tale stringa “pseudo-uniforme”, adottando il nostro linguaggio da prima. Poiché il termine “pseudo-uniforme” è sia ingombrante che non utilizzato da nessuno, non lo introdurremo qui per chiarezza. Invece, abbandoniamo semplicemente la distinzione tra “casuale” e “uniforme” nel contesto attuale.

**Note**

[2] Se interessati a un'esposizione più formale su questi argomenti, potete consultare *Introduzione alla Crittografia Moderna* di Katz e Lindell, specialmente il capitolo 3.

# Fondamenti Matematici della Crittografia 2
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

## Cos'è la teoria dei numeri?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>
Questo capitolo tratta un argomento più avanzato sulle fondamenta matematiche della crittografia: la teoria dei numeri. Sebbene la teoria dei numeri sia importante per la crittografia simmetrica (come nel Cifrario di Rijndael), è particolarmente rilevante nell'ambito della crittografia a chiave pubblica.

Se trovi i dettagli della teoria dei numeri complicati, ti consiglierei una lettura ad alto livello la prima volta. Puoi sempre tornarci in un secondo momento.

___

Potresti caratterizzare la **teoria dei numeri** come lo studio delle proprietà degli interi e delle funzioni matematiche che lavorano con gli interi.

Considera, ad esempio, che due numeri $a$ e $N$ sono **coprimi** (o **primi relativi**) se il loro massimo comune divisore è uguale a 1. Supponiamo ora un particolare intero $N$. Quanti interi più piccoli di $N$ sono coprimi con $N$? Possiamo fare affermazioni generali sulle risposte a questa domanda? Questi sono i tipici tipi di domande che la teoria dei numeri cerca di rispondere.

La teoria dei numeri moderna si basa sugli strumenti dell'algebra astratta. Il campo dell'**algebra astratta** è una sottodisciplina della matematica dove gli oggetti principali di analisi sono oggetti astratti noti come strutture algebriche. Una **struttura algebrica** è un insieme di elementi congiunti con una o più operazioni, che soddisfa certi assiomi. Attraverso le strutture algebriche, i matematici possono ottenere intuizioni su specifici problemi matematici, astrattendoli dai loro dettagli.

Il campo dell'algebra astratta è talvolta chiamato anche algebra moderna. Potresti anche incontrare il concetto di **matematica astratta** (o **matematica pura**). Quest'ultimo termine non si riferisce all'algebra astratta, ma significa lo studio della matematica per il suo proprio valore, e non solo con un occhio alle potenziali applicazioni.

Gli insiemi dell'algebra astratta possono trattare molti tipi di oggetti, dalle trasformazioni che preservano la forma su un triangolo equilatero ai modelli di carta da parati. Per la teoria dei numeri, consideriamo solo insiemi di elementi che contengono interi o funzioni che lavorano con interi.

## Gruppi
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Un concetto di base in matematica è quello di un insieme di elementi. Un insieme è solitamente denotato da segni di parentesi graffe con gli elementi separati da virgole.

Ad esempio, l'insieme di tutti gli interi è $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$. Le ellissi qui significano che un certo modello continua in una particolare direzione. Quindi l'insieme di tutti gli interi include anche $3, 4, 5, 6$ e così via, così come $-3, -4, -5, -6$ e così via. Questo insieme di tutti gli interi è tipicamente denotato da $\mathbb{Z}$.

Un altro esempio di insieme è $\mathbb{Z} \mod 11$, o l'insieme di tutti gli interi modulo 11. A differenza dell'intero insieme $\mathbb{Z}$, questo insieme contiene solo un numero finito di elementi, ovvero $\{0, 1, \ldots, 9, 10\}$.
Un errore comune è pensare che l'insieme $\mathbb{Z} \mod 11$ sia effettivamente $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Ma questo non è il caso, data la modalità con cui abbiamo definito in precedenza l'operazione di modulo. Qualsiasi intero negativo ridotto tramite modulo 11 si trasforma in $\{0, 1, \ldots, 9, 10\}$. Per esempio, l'espressione $-2 \mod 11$ si trasforma in $9$, mentre l'espressione $-27 \mod 11$ si trasforma in $5$.

Un altro concetto fondamentale in matematica è quello di operazione binaria. Si tratta di qualsiasi operazione che prende due elementi per produrne un terzo. Ad esempio, dall'aritmetica e algebra di base, sareste familiari con quattro operazioni binarie fondamentali: addizione, sottrazione, moltiplicazione e divisione.

Questi due concetti matematici di base, insiemi e operazioni binarie, sono utilizzati per definire la nozione di gruppo, la struttura più essenziale nell'algebra astratta.

Specificamente, supponiamo un'operazione binaria $\circ$. Inoltre, supponiamo un insieme di elementi **S** equipaggiato con tale operazione. "Equipaggiato" qui significa semplicemente che l'operazione $\circ$ può essere eseguita tra qualsiasi coppia di elementi nell'insieme **S**.

La combinazione $\langle \mathbf{S}, \circ \rangle$ è, quindi, un **gruppo** se soddisfa quattro condizioni specifiche, note come assiomi di gruppo.

1. Per qualsiasi $a$ e $b$ che sono elementi di $\mathbf{S}$, $a \circ b$ è anch'esso un elemento di $\mathbf{S}$. Questo è noto come **condizione di chiusura**.
2. Per qualsiasi $a$, $b$ e $c$ che sono elementi di $\mathbf{S}$, risulta che $(a \circ b) \circ c = a \circ (b \circ c)$. Questo è noto come **condizione di associatività**.
3. Esiste un elemento unico $e$ in $\mathbf{S}$, tale che per ogni elemento $a$ in $\mathbf{S}$, vale la seguente equazione: $e \circ a = a \circ e = a$. Poiché esiste un solo tale elemento $e$, è chiamato **elemento neutro**. Questa condizione è nota come **condizione di identità**.
4. Per ogni elemento $a$ in $\mathbf{S}$, esiste un elemento $b$ in $\mathbf{S}$, tale che vale la seguente equazione: $a \circ b = b \circ a = e$, dove $e$ è l'elemento neutro. L'elemento $b$ qui è noto come **elemento inverso**, ed è comunemente denotato come $a^{-1}$. Questa condizione è nota come **condizione di invertibilità**.

Esploriamo ulteriormente i gruppi. Denotiamo l'insieme di tutti gli interi con $\mathbb{Z}$. Questo insieme combinato con l'addizione standard, o $\langle \mathbb{Z}, + \rangle$, si adatta chiaramente alla definizione di gruppo, poiché soddisfa i quattro assiomi sopra menzionati.

1. Per qualsiasi $x$ e $y$ che sono elementi di $\mathbb{Z}$, $x + y$ è anch'esso un elemento di $\mathbb{Z}$. Quindi $\langle \mathbb{Z}, + \rangle$ soddisfa la condizione di chiusura.
2. Per ogni $x$, $y$ e $z$ che sono elementi di $\mathbb{Z}$, $(x + y) + z = x + (y + z)$. Quindi $\langle \mathbb{Z}, + \rangle$ soddisfa la condizione di associatività.
3. Esiste un elemento neutro in $\langle \mathbb{Z}, + \rangle$, precisamente 0. Per ogni $x$ in $\mathbb{Z}$, vale infatti che: $0 + x = x + 0 = x$. Quindi $\langle \mathbb{Z}, + \rangle$ soddisfa la condizione di elemento neutro.
4. Infine, per ogni elemento $x$ in $\mathbb{Z}$, esiste un $y$ tale che $x + y = y + x = 0$. Se $x$ fosse 10, per esempio, $y$ sarebbe $-10$ (nel caso in cui $x$ sia 0, anche $y$ è 0). Quindi $\langle \mathbb{Z}, + \rangle$ soddisfa la condizione di elemento inverso.

È importante notare che il fatto che l'insieme degli interi con l'addizione costituisca un gruppo non significa che costituisca un gruppo anche con la moltiplicazione. Puoi verificarlo testando $\langle \mathbb{Z}, \cdot \rangle$ contro i quattro assiomi di gruppo (dove $\cdot$ indica la moltiplicazione standard).

I primi due assiomi sono ovviamente soddisfatti. Inoltre, sotto la moltiplicazione, l'elemento 1 può fungere da elemento neutro. Qualsiasi intero $x$ moltiplicato per 1, dà come risultato $x$. Tuttavia, $\langle \mathbb{Z}, \cdot \rangle$ non soddisfa la condizione di elemento inverso. Cioè, non esiste un elemento unico $y$ in $\mathbb{Z}$ per ogni $x$ in $\mathbb{Z}$, tale che $x \cdot y = 1$.

Per esempio, supponiamo che $x = 22$. Quale valore di $y$ dell'insieme $\mathbb{Z}$ moltiplicato per $x$ darebbe l'elemento neutro 1? Il valore di $1/22$ funzionerebbe, ma questo non è nell'insieme $\mathbb{Z}$. Infatti, si incontra questo problema per qualsiasi intero $x$, ad eccezione dei valori di 1 e -1 (dove $y$ dovrebbe essere rispettivamente 1 e -1).

Se consentissimo i numeri reali per il nostro insieme, allora i nostri problemi scomparirebbero in gran parte. Per qualsiasi elemento $x$ dell'insieme, la moltiplicazione per $1/x$ dà 1. Poiché le frazioni sono incluse nell'insieme dei numeri reali, si può trovare un inverso per ogni numero reale. L'eccezione è lo zero, poiché qualsiasi moltiplicazione con zero non darà mai l'elemento neutro 1. Pertanto, l'insieme dei numeri reali non-zero equipaggiato con la moltiplicazione è effettivamente un gruppo.

Alcuni gruppi soddisfano una quinta condizione generale, nota come **condizione di commutatività**. Questa condizione è la seguente:

* Supponiamo un gruppo $G$ con un insieme **S** e un operatore binario $\circ$. Supponiamo che $a$ e $b$ siano elementi di **S**. Se risulta che $a \circ b = b \circ a$ per qualsiasi coppia di elementi $a$ e $b$ in **S**, allora $G$ soddisfa la condizione di commutatività.
Qualsiasi gruppo che soddisfa la condizione di commutatività è noto come **gruppo commutativo**, o **gruppo Abeliano** (in onore di Niels Henrik Abel). È facile verificare che sia l'insieme dei numeri reali con l'addizione sia l'insieme degli interi con l'addizione sono gruppi Abeliani. L'insieme degli interi con la moltiplicazione non è affatto un gruppo, quindi di fatto non può essere un gruppo Abeliano. Al contrario, l'insieme dei numeri reali non nulli con la moltiplicazione è anch'esso un gruppo Abeliano.

Dovresti prestare attenzione a due importanti convenzioni sulla notazione. Primo, i segni "+" o "×" saranno frequentemente impiegati per simboleggiare le operazioni di gruppo, anche quando gli elementi non sono, di fatto, numeri. In questi casi, non dovresti interpretare questi segni come la standard addizione o moltiplicazione aritmetica. Invece, sono operazioni con solo una somiglianza astratta a queste operazioni aritmetiche.

A meno che non ti stia riferendo specificamente all'addizione o moltiplicazione aritmetica, è più semplice usare simboli come $\circ$ e $\diamond$ per le operazioni di gruppo, poiché questi non hanno connotazioni culturalmente radicate.

Secondo, per la stessa ragione per cui "+" e "×" sono spesso usati per indicare operazioni non aritmetiche, gli elementi neutri dei gruppi sono frequentemente simbolizzati da "0" e "1", anche quando gli elementi in questi gruppi non sono numeri. A meno che non ti stia riferendo all'elemento neutro di un gruppo con numeri, è più semplice usare un simbolo più neutro come "$e$" per indicare l'elemento neutro.

Molti insiemi di valori differenti e molto importanti in matematica dotati di certe operazioni binarie sono gruppi. Tuttavia, le applicazioni crittografiche funzionano solo con insiemi di interi o almeno elementi che sono descritti da interi, cioè, all'interno del dominio della teoria dei numeri. Pertanto, insiemi con numeri reali diversi dagli interi non sono impiegati nelle applicazioni crittografiche.

Concludiamo fornendo un esempio di elementi che possono essere "descritti da interi", anche se non sono interi. Un buon esempio sono i punti delle curve ellittiche. Sebbene qualsiasi punto su una curva ellittica non sia chiaramente un intero, tale punto è effettivamente descritto da due interi.

Le curve ellittiche sono, ad esempio, cruciali per Bitcoin. Qualsiasi coppia di chiavi private e pubbliche standard di Bitcoin è selezionata dall'insieme di punti definito dalla seguente curva ellittica:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(il più grande numero primo minore di $2^{256}$). La coordinata $x$ è la chiave privata e la coordinata $y$ è la tua chiave pubblica.

Le transazioni in Bitcoin coinvolgono tipicamente il blocco degli output su una o più chiavi pubbliche in qualche modo. Il valore di queste transazioni può, quindi, essere sbloccato facendo firme digitali con le corrispondenti chiavi private.

## Gruppi ciclici

Una distinzione importante che possiamo tracciare è tra un **gruppo finito** e un **gruppo infinito**. Il primo ha un numero finito di elementi, mentre il secondo ha un numero infinito di elementi. Il numero di elementi in qualsiasi gruppo finito è noto come **ordine del gruppo**. Tutta la crittografia pratica che coinvolge l'uso di gruppi si basa su gruppi finiti (teorico-numerici).

Nella crittografia a chiave pubblica, una certa classe di gruppi Abeliani finiti noti come gruppi ciclici è particolarmente importante. Per comprendere i gruppi ciclici, dobbiamo prima capire il concetto di esponenziazione degli elementi di gruppo.
Supponiamo un gruppo $G$ con un'operazione di gruppo $\circ$, e che $a$ sia un elemento di $G$. L'espressione $a^n$ dovrebbe quindi essere interpretata come l'elemento $a$ combinato con se stesso per un totale di $n - 1$ volte. Per esempio, $a^2$ significa $a \circ a$, $a^3$ significa $a \circ a \circ a$, e così via. (Si noti che l'esponenziazione qui non è necessariamente l'esponenziazione nel senso aritmetico standard.)
Passiamo a un esempio. Supponiamo che $G = \langle \mathbb{Z} \mod 7, + \rangle$, e che il nostro valore per $a$ sia 4. In questo caso, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Alternativamente, $a^4$ rappresenterebbe $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Alcuni gruppi Abeliani hanno uno o più elementi, che possono generare tutti gli altri elementi del gruppo attraverso l'esponenziazione continua. Questi elementi sono chiamati **generatori** o **elementi primitivi**.

Una classe importante di tali gruppi è $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, dove $N$ è un numero primo. La notazione $\mathbb{Z}^*$ qui significa che il gruppo contiene tutti gli interi positivi non zero minori di $N$. Un tale gruppo, quindi, ha sempre $N - 1$ elementi.

Consideriamo, per esempio, $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Questo gruppo ha i seguenti elementi: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. L'ordine di questo gruppo è 10 (che è effettivamente uguale a $11 - 1$).

Esploriamo l'esponenziazione dell'elemento 2 da questo gruppo. I calcoli fino a $2^{12}$ sono mostrati di seguito. Si noti che sul lato sinistro dell'equazione, l'esponente si riferisce all'esponenziazione dell'elemento di gruppo. Nel nostro esempio particolare, questo comporta effettivamente l'esponenziazione aritmetica sul lato destro dell'equazione (ma avrebbe potuto anche coinvolgere, per esempio, l'addizione). Per chiarire, ho scritto l'operazione ripetuta, piuttosto che la forma esponenziale sul lato destro.

* $2^1 = 2 \mod 11$
* $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
* $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
* $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
* $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
* $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
* $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
* $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
* $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
* $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
* $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
* $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$

Se si osserva attentamente, si può vedere che eseguendo l'elevamento a potenza sull'elemento 2 si cicla attraverso tutti gli elementi di $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ nel seguente ordine: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Dopo $2^{10}$, l'elevamento a potenza continuato dell'elemento 2 cicla nuovamente attraverso tutti gli elementi e nello stesso ordine. Pertanto, l'elemento 2 è un generatore in $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Sebbene $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ abbia più generatori, non tutti gli elementi di questo gruppo sono generatori. Consideriamo, per esempio, l'elemento 3. Passando attraverso le prime 10 elevazioni a potenza, senza mostrare i calcoli ingombranti, si ottengono i seguenti risultati:

* $3^1 = 3 \mod 11$
* $3^2 = 9 \mod 11$
* $3^3 = 5 \mod 11$
* $3^4 = 4 \mod 11$
* $3^5 = 1 \mod 11$
* $3^6 = 3 \mod 11$
* $3^7 = 9 \mod 11$
* $3^8 = 5 \mod 11$
* $3^9 = 4 \mod 11$
* $3^{10} = 1 \mod 11$
Invece di ciclare attraverso tutti i valori in $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, l'elevamento a potenza dell'elemento 3 porta solo a un sottoinsieme di quei valori: 3, 9, 5, 4 e 1. Dopo la quinta elevazione a potenza, questi valori iniziano a ripetersi.
Possiamo ora definire un **gruppo ciclico** come qualsiasi gruppo con almeno un generatore. Ovvero, esiste almeno un elemento del gruppo da cui è possibile produrre tutti gli altri elementi del gruppo attraverso l'elevazione a potenza.

Potresti aver notato nel nostro esempio sopra che sia $2^{10}$ che $3^{10}$ sono uguali a $1 \mod 11$. Infatti, anche se non eseguiremo i calcoli, l'elevazione a potenza per 10 di qualsiasi elemento nel gruppo $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ produrrà $1 \mod 11$. Perché è così?

Questa è una domanda importante, ma richiede un po' di lavoro per rispondere.

Per iniziare, supponiamo due interi positivi $a$ e $N$. Un importante teorema in teoria dei numeri afferma che $a$ ha un inverso moltiplicativo modulo $N$ (cioè, un intero $b$ tale che $a \cdot b = 1 \mod N$) se e solo se il massimo comune divisore tra $a$ e $N$ è uguale a 1. Ovvero, se $a$ e $N$ sono coprimi.

Quindi, per qualsiasi gruppo di interi dotato di moltiplicazione modulo $N$, solo i coprimi più piccoli con $N$ sono inclusi nel set. Possiamo denotare questo insieme con $\mathbb{Z}^c \mod N$.

Per esempio, supponiamo che $N$ sia 10. Solo gli interi 1, 3, 7 e 9 sono coprimi con 10. Quindi l'insieme $\mathbb{Z}^c \mod 10$ include solo $\{1, 3, 7, 9\}$. Non puoi creare un gruppo con moltiplicazione intera modulo 10 usando altri interi tra 1 e 10. Per questo particolare gruppo, gli inversi sono le coppie 1 e 9, e 3 e 7.

Nel caso in cui $N$ stesso sia primo, tutti gli interi da 1 a $N – 1$ sono coprimi con $N$. Un tale gruppo, quindi, ha un ordine di $N – 1$. Usando la nostra notazione precedente, $\mathbb{Z}^c \mod N$ è uguale a $\mathbb{Z}^* \mod N$ quando $N$ è primo. Il gruppo che abbiamo selezionato per il nostro esempio precedente, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, è un particolare esempio di questa classe di gruppi.

Successivamente, la funzione $\phi(N)$ calcola il numero di coprimi fino a un numero $N$ ed è nota come **Funzione Phi di Eulero**. [1] Secondo il **Teorema di Eulero**, ogni volta che due interi $a$ e $N$ sono coprimi, vale quanto segue:

* $a^{\phi(N)} \mod N = 1 \mod N$
Questa ha un'importante implicazione per la classe di gruppi $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ dove $N$ è primo. Per questi gruppi, l'esponenziazione degli elementi del gruppo rappresenta l'esponenziazione aritmetica. Ovvero, $a^{\phi(N)} \mod N$ rappresenta l'operazione aritmetica $a^{\phi(N)} \mod N$. Poiché ogni elemento $a$ in questi gruppi moltiplicativi è coprimo con $N$, significa che $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.

Il teorema di Eulero è un risultato davvero importante. Per iniziare, implica che tutti gli elementi in $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ possono solo ciclare attraverso un numero di valori tramite esponenziazione che si divide in $N – 1$. Nel caso di $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, ciò significa che ogni elemento può solo ciclare attraverso 2, 5, o 10 elementi. I valori di gruppo attraverso i quali un elemento cicla mediante esponenziazione sono noti come **ordine dell'elemento**. Un elemento con un ordine equivalente all'ordine di un gruppo è un generatore.

Inoltre, il teorema di Eulero implica che possiamo sempre conoscere il risultato di $a^{N – 1} \mod N$ per qualsiasi gruppo $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ dove $N$ è primo. Questo vale indipendentemente da quanto possano essere complicate le effettive calcolazioni.

Per esempio, supponiamo che il nostro gruppo sia $\mathbb{Z}^* \mod 160,481,182$ (dove 160,481,182 è effettivamente un numero primo). Sappiamo che tutti gli interi da 1 a 160,481,181 devono essere elementi di questo gruppo, e che $\phi(n) = 160,481,181$. Anche se non possiamo eseguire tutti i passaggi nei calcoli, sappiamo che espressioni come $514^{160,481,181}$, $2,005^{160,481,181}$, e $256,212^{160,481,181}$ devono tutte valutare a $1 \mod 160,481,182$.

**Note:**

[1] La funzione opera come segue. Qualsiasi intero $N$ può essere fattorizzato in un prodotto di primi. Supponiamo che un particolare $N$ sia fattorizzato come segue: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ dove tutti i $p$ sono numeri primi e tutti gli $e$ sono interi maggiori o uguali a 1. Allora:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Formula della funzione Phi di Eulero per la fattorizzazione in primi di $N$.

## Campi
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Un gruppo è la struttura algebrica di base in algebra astratta, ma ce ne sono molte altre. L'unica altra struttura algebrica di cui hai bisogno di essere a conoscenza è quella di un **campo**, specificamente quella di un **campo finito**. Questo tipo di struttura algebrica è frequentemente utilizzato in crittografia, come nello Standard di Crittografia Avanzata. Quest'ultimo è il principale schema di crittografia simmetrica che incontrerai nella pratica.
Un campo deriva dalla nozione di gruppo. Specificamente, un **campo** è un insieme di elementi **S** dotato di due operatori binari $\circ$ e $\diamond$, che soddisfa le seguenti condizioni:
1. L'insieme **S** dotato di $\circ$ è un gruppo Abeliano.
2. L'insieme **S** dotato di $\diamond$ è un gruppo Abeliano per gli elementi "non-zero".
3. L'insieme **S** dotato dei due operatori soddisfa quella che è nota come condizione distributiva: Supponiamo che $a$, $b$ e $c$ siano elementi di **S**. Allora **S** dotato dei due operatori soddisfa la proprietà distributiva quando $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Si noti che, come per i gruppi, la definizione di un campo è molto astratta. Non fa affermazioni sui tipi di elementi in **S**, o sulle operazioni $\circ$ e $\diamond$. Afferma semplicemente che un campo è qualsiasi insieme di elementi con due operazioni per cui valgono le tre condizioni sopra citate. (L'elemento “zero” nel secondo gruppo Abeliano può essere interpretato in modo astratto.)

Quindi, quale potrebbe essere un esempio di campo? Un buon esempio è l'insieme $\mathbb{Z} \mod 7$, o $\{0, 1, \ldots, 7\}$ definito sulla somma standard (al posto di $\circ$ sopra) e sulla moltiplicazione standard (al posto di $\diamond$ sopra).

Primo, $\mathbb{Z} \mod 7$ soddisfa la condizione per essere un gruppo Abeliano sulla somma, e soddisfa la condizione per essere un gruppo Abeliano sulla moltiplicazione se si considerano solo gli elementi non-zero. Secondo, la combinazione dell'insieme con i due operatori soddisfa la condizione distributiva.

È didatticamente utile esplorare queste affermazioni utilizzando alcuni valori particolari. Prendiamo i valori sperimentali 5, 2 e 3, alcuni elementi selezionati casualmente dall'insieme $\mathbb{Z} \mod 7$, per ispezionare il campo $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Useremo questi tre valori nell'ordine, come necessario per esplorare particolari condizioni.

Esploriamo prima se $\mathbb{Z} \mod 7$ dotato di addizione è un gruppo Abeliano.

1. **Condizione di chiusura**: Prendiamo 5 e 2 come nostri valori. In tal caso, $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Questo è effettivamente un elemento di $\mathbb{Z} \mod 7$, quindi il risultato è coerente con la condizione di chiusura.
2. **Condizione di associatività**: Prendiamo 5, 2 e 3 come nostri valori. In tal caso, $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Questo è coerente con la condizione di associatività.
3. **Condizione di identità**: Prendiamo 5 come nostro valore. In tal caso, $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Quindi 0 sembra essere l'elemento identità per l'addizione.
4. **Condizione inversa**: Consideriamo l'inverso di 5. Deve verificarsi che $[5 + d] \mod 7 = 0$, per qualche valore di $d$. In questo caso, l'unico valore da $\mathbb{Z} \mod 7$ che soddisfa questa condizione è 2. 5. **Condizione di commutatività**: Prendiamo come nostri valori 5 e 3. In tal caso, $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Questo è coerente con la condizione di commutatività.

L'insieme $\mathbb{Z} \mod 7$ equipaggiato con l'addizione sembra chiaramente essere un gruppo Abeliano. Esploriamo ora se $\mathbb{Z} \mod 7$ equipaggiato con la moltiplicazione è un gruppo Abeliano per tutti gli elementi non-zero.

1. **Condizione di chiusura**: Prendiamo come nostri valori 5 e 2. In tal caso, $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Questo è anche un elemento di $\mathbb{Z} \mod 7$, quindi il risultato è coerente con la condizione di chiusura.
2. **Condizione di associatività**: Prendiamo come nostri valori 5, 2 e 3. In tal caso, $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Questo è coerente con la condizione di associatività.
3. **Condizione di identità**: Prendiamo come nostro valore 5. In tal caso, $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Quindi 1 sembra essere l'elemento identità per la moltiplicazione.
4. **Condizione inversa**: Consideriamo l'inverso di 5. Deve verificarsi che $[5 \cdot d] \mod 7 = 1$, per qualche valore di $d$. L'unico valore da $\mathbb{Z} \mod 7$ che soddisfa questa condizione è 3. Questo è coerente con la condizione inversa.
5. **Condizione di commutatività**: Prendiamo come nostri valori 5 e 3. In tal caso, $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Questo è coerente con la condizione di commutatività.

L'insieme $\mathbb{Z} \mod 7$ sembra chiaramente soddisfare le regole per essere un gruppo Abeliano quando congiunto sia con l'addizione che con la moltiplicazione sugli elementi non-zero.

Infine, questo insieme combinato con entrambi gli operatori sembra soddisfare la condizione distributiva. Prendiamo come nostri valori 5, 2 e 3. Possiamo vedere che $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Abbiamo ora visto che $\mathbb{Z} \mod 7$ equipaggiato con addizione e moltiplicazione soddisfa gli assiomi per un campo finito quando testato con valori particolari. Ovviamente, possiamo anche dimostrarlo in generale, ma non lo faremo qui.

Una distinzione chiave è tra due tipi di campi: campi finiti e campi infiniti.
Un **campo infinito** coinvolge un campo dove l'insieme **S** è infinitamente grande. L'insieme dei numeri reali $\mathbb{R}$ equipaggiato con l'addizione e la moltiplicazione è un esempio di campo infinito. Un **campo finito**, conosciuto anche come **campo di Galois**, è un campo dove l'insieme **S** è finito. Il nostro esempio sopra di $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ è un campo finito.
In crittografia, siamo principalmente interessati ai campi finiti. Generalmente, si può dimostrare che un campo finito esiste per un certo insieme di elementi **S** se e solo se ha $p^m$ elementi, dove $p$ è un numero primo e $m$ un intero positivo maggiore o uguale a uno. In altre parole, se l'ordine di un certo insieme **S** è un numero primo ($p^m$ dove $m = 1$) o una potenza di primo ($p^m$ dove $m > 1$), allora puoi trovare due operatori $\circ$ e $\diamond$ tali che le condizioni per un campo siano soddisfatte.

Se un campo finito ha un numero primo di elementi, allora è chiamato **campo primo**. Se il numero di elementi nel campo finito è una potenza di primo, allora il campo è chiamato **campo esteso**. In crittografia, siamo interessati sia ai campi primi che a quelli estesi. [2]

I principali campi primi di interesse in crittografia sono quelli dove l'insieme di tutti gli interi è modulato da un certo numero primo, e gli operatori sono l'addizione e la moltiplicazione standard. Questa classe di campi finiti includerebbe $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, e così via. Per qualsiasi campo primo $\mathbb{Z} \mod p$, l'insieme degli interi del campo è il seguente: $\{0, 1, \ldots, p – 2, p – 1\}$.

In crittografia, siamo anche interessati ai campi estesi, in particolare a qualsiasi campo con $2^m$ elementi dove $m > 1$. Tali campi finiti sono, per esempio, utilizzati nel Cifrario Rijndael, che costituisce la base dello Standard di Crittografia Avanzata. Mentre i campi primi sono relativamente intuitivi, questi campi estesi base 2 probabilmente non lo sono per chi non è familiare con l'algebra astratta.

Per iniziare, è effettivamente vero che qualsiasi insieme di interi con $2^m$ elementi può essere assegnato a due operatori che farebbero della loro combinazione un campo (purché $m$ sia un intero positivo). Tuttavia, il fatto che un campo esista non significa necessariamente che sia facile da scoprire o particolarmente pratico per certe applicazioni.

Si scopre che, in particolare, i campi estesi applicabili di $2^m$ in crittografia sono quelli definiti su particolari insiemi di espressioni polinomiali, piuttosto che su un certo insieme di interi.

Per esempio, supponiamo che volessimo un campo esteso con $2^3$ (cioè, 8) elementi nell'insieme. Sebbene ci possano essere molti insiemi diversi che possono essere utilizzati per campi di quella dimensione, un tale insieme include tutti i polinomi unici della forma $a_2x^2 + a_1x + a_0$, dove ogni coefficiente $a_i$ è o 0 o 1. Pertanto, questo insieme **S** include i seguenti elementi:
1. $0$: Il caso in cui $a_2 = 0$, $a_1 = 0$ e $a_0 = 0$.
2. $1$: Il caso in cui $a_2 = 0$, $a_1 = 0$ e $a_0 = 1$.
3. $x$: Il caso in cui $a_2 = 0$, $a_1 = 1$ e $a_0 = 0$.
4. $x + 1$: Il caso in cui $a_2 = 0$, $a_1 = 1$ e $a_0 = 1$.
5. $x^2$: Il caso in cui $a_2 = 1$, $a_1 = 0$ e $a_0 = 0$.
6. $x^2 + 1$: Il caso in cui $a_2 = 1$, $a_1 = 0$ e $a_0 = 1$.
7. $x^2 + x$: Il caso in cui $a_2 = 1$, $a_1 = 1$ e $a_0 = 0$.
8. $x^2 + x + 1$: Il caso in cui $a_2 = 1$, $a_1 = 1$ e $a_0 = 1$.

Quindi **S** sarebbe l'insieme $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Quali due operazioni possono essere definite su questo insieme di elementi per garantire che la loro combinazione sia un campo?

La prima operazione sull'insieme **S** ($\circ$) può essere definita come l'addizione standard di polinomi modulo 2. Tutto ciò che devi fare è sommare i polinomi come faresti normalmente, e poi applicare il modulo 2 a ciascuno dei coefficienti del polinomio risultante. Ecco alcuni esempi:

* $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
* $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
* $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

La seconda operazione sull'insieme **S** ($\diamond$) necessaria per creare il campo è più complicata. Si tratta di una sorta di moltiplicazione, ma non la moltiplicazione standard dell'aritmetica. Invece, devi considerare ciascun elemento come un vettore e comprendere l'operazione come la moltiplicazione di quei due vettori modulo un polinomio irriducibile.

Passiamo ora all'idea di un polinomio irriducibile. Un **polinomio irriducibile** è uno che non può essere fattorizzato (proprio come un numero primo non può essere fattorizzato in componenti diversi da 1 e il numero primo stesso). Ai nostri fini, siamo interessati ai polinomi che sono irriducibili rispetto all'insieme di tutti gli interi. (Nota che potresti essere in grado di fattorizzare certi polinomi, per esempio, con i numeri reali o complessi, anche se non puoi fattorizzarli usando gli interi).
Ad esempio, consideriamo il polinomio $x^2 - 3x + 2$. Questo può essere riscritto come $(x – 1)(x – 2)$. Pertanto, non è irriducibile. Ora consideriamo il polinomio $x^2 + 1$. Utilizzando solo interi, non c'è modo di fattorizzare ulteriormente questa espressione. Pertanto, questo è un polinomio irriducibile rispetto agli interi.

Successivamente, passiamo al concetto di moltiplicazione vettoriale. Non esploreremo questo argomento in profondità, ma è sufficiente comprendere una regola di base: la divisione vettoriale può avvenire purché il dividendo abbia un grado superiore o uguale a quello del divisore. Se il dividendo ha un grado inferiore a quello del divisore, allora il dividendo non può più essere diviso dal divisore.

Ad esempio, consideriamo l'espressione $x^6 + x + 1 \mod x^5 + x^2$. Questa si riduce ulteriormente poiché il grado del dividendo, 6, è superiore al grado del divisore, 5. Ora consideriamo l'espressione $x^5 + x + 1 \mod x^5 + x^2$. Anche questa si riduce ulteriormente, poiché il grado del dividendo, 5, e del divisore, 5, sono uguali.

Tuttavia, ora consideriamo l'espressione $x^4 + x + 1 \mod x^5 + x^2$. Questa non si riduce ulteriormente, poiché il grado del dividendo, 4, è inferiore al grado del divisore, 5.

Sulla base di queste informazioni, siamo ora pronti a trovare la nostra seconda operazione per l'insieme $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Ho già detto che la seconda operazione dovrebbe essere intesa come moltiplicazione vettoriale modulo un certo polinomio irriducibile. Questo polinomio irriducibile dovrebbe garantire che la seconda operazione definisca un gruppo Abeliano su **S** ed è coerente con la condizione distributiva. Quindi, quale dovrebbe essere questo polinomio irriducibile?

Poiché tutti i vettori nell'insieme sono di grado 2 o inferiore, il polinomio irriducibile dovrebbe essere di grado 3. Se qualsiasi moltiplicazione di due vettori nell'insieme produce un polinomio di grado 3 o superiore, sappiamo che modulo un polinomio di grado 3 produce sempre un polinomio di grado 2 o inferiore. Questo avviene perché qualsiasi polinomio di grado 3 o superiore è sempre divisibile per un polinomio di grado 3. Inoltre, il polinomio che funge da divisore deve essere irriducibile.

Si scopre che ci sono diversi polinomi irriducibili di grado 3 che potremmo utilizzare come nostro divisore. Ognuno di questi polinomi definisce un campo diverso in congiunzione con il nostro insieme **S** e l'addizione modulo 2. Questo significa che hai più opzioni quando utilizzi i campi di estensione $2^m$ in crittografia.

Per il nostro esempio, supponiamo di selezionare il polinomio $x^3 + x + 1$. Questo è effettivamente irriducibile, perché non è possibile fattorizzarlo utilizzando interi. Inoltre, garantirà che qualsiasi moltiplicazione di due elementi produrrà un polinomio di grado 2 o inferiore.
Lavoriamo attraverso un esempio della seconda operazione utilizzando il polinomio $x^3 + x + 1$ come divisore per illustrare come funziona. Supponiamo che tu moltiplichi gli elementi $x^2 + 1$ con $x^2 + x$ nel nostro insieme **S**. Dobbiamo quindi calcolare l'espressione $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Questo può essere semplificato come segue:
* $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
* $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
* $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Sappiamo che $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ può essere ridotto poiché il dividendo ha un grado superiore (4) rispetto al divisore (3).

Per iniziare, puoi vedere che l'espressione $x^3 + x + 1$ entra in $x^4 + x^3 + x^2 + x$ un totale di $x$ volte. Puoi verificarlo moltiplicando $x^3 + x + 1$ per $x$, che è $x^4 + x^2 + x$. Poiché l'ultimo termine ha lo stesso grado del dividendo, cioè 4, sappiamo che questo funziona. Puoi calcolare il resto di questa divisione per $x$ come segue:

* $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
* $[x^3] \mod x^3 + x + 1 =$
* $x^3$

Quindi, dopo aver diviso $x^4 + x^3 + x^2 + x$ per $x^3 + x + 1$ un totale di $x$ volte, abbiamo un resto di $x^3$. Questo può essere ulteriormente diviso per $x^3 + x + 1$?

Intuitivamente, potrebbe sembrare logico dire che $x^3$ non può più essere diviso per $x^3 + x + 1$, perché quest'ultimo termine sembra più grande. Tuttavia, ricorda la nostra discussione sulla divisione vettoriale in precedenza. Finché il dividendo ha un grado maggiore o uguale al divisore, l'espressione può essere ulteriormente ridotta. Specificamente, l'espressione $x^3 + x + 1$ può entrare in $x^3$ esattamente 1 volta. Il resto è calcolato come segue:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Potresti chiederti perché $(x^3) - (x^3 + x + 1)$ si valuta in $x + 1$ e non in $-x - 1$. Ricorda che la prima operazione del nostro campo è definita modulo 2. Pertanto, la sottrazione di due vettori produce esattamente lo stesso risultato dell'aggiunta di due vettori.
Per riassumere la moltiplicazione di $x^2 + 1$ e $x^2 + x$: Quando moltiplichi questi due termini, ottieni un polinomio di grado 4, $x^4 + x^3 + x^2 + x$, che deve essere ridotto modulo $x^3 + x + 1$. Il polinomio di grado 4 è divisibile per $x^3 + x + 1$ esattamente $x + 1$ volte. Il resto dopo aver diviso $x^4 + x^3 + x^2 + x$ per $x^3 + x + 1$ esattamente $x + 1$ volte è $x + 1$. Questo è effettivamente un elemento nel nostro insieme $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Perché i campi di estensione con base 2 su insiemi di polinomi, come nell'esempio sopra, sono utili per la crittografia? Il motivo è che puoi considerare i coefficienti nei polinomi di tali insiemi, 0 o 1, come elementi di stringhe binarie di una lunghezza particolare. L'insieme **S** nel nostro esempio sopra, ad esempio, potrebbe essere invece visto come un insieme **S** che include tutte le stringhe binarie di lunghezza 3 (da 000 a 111). Le operazioni su **S**, quindi, possono anche essere utilizzate per eseguire operazioni su queste stringhe binarie e produrre una stringa binaria della stessa lunghezza.

**Note:**

[2] I campi di estensione diventano molto controintuitivi. Invece di avere elementi di interi, hanno insiemi di polinomi. Inoltre, qualsiasi operazione viene eseguita modulo qualche polinomio irriducibile.

## L'algebra astratta nella pratica
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Nonostante il linguaggio formale e l'astrattezza della discussione, il concetto di gruppo non dovrebbe essere troppo difficile da afferrare. È semplicemente un insieme di elementi insieme a un'operazione binaria, dove l'esecuzione di quell'operazione binaria su quegli elementi soddisfa quattro condizioni generali. Un gruppo Abeliano ha solo una condizione aggiuntiva nota come commutatività. Un gruppo ciclico, a sua volta, è un tipo speciale di gruppo Abeliano, ovvero uno che ha un generatore. Un campo è semplicemente una costruzione più complessa dalla nozione di base di gruppo.

Ma se sei una persona praticamente incline, potresti chiederti a questo punto: A chi importa? Sapere che un certo insieme di elementi con un operatore è un gruppo, o addirittura un gruppo Abeliano o ciclico, ha qualche rilevanza nel mondo reale? Sapere che qualcosa è un campo?

Senza addentrarci troppo nei dettagli, la risposta è "sì". I gruppi sono stati creati per la prima volta nel XIX secolo dal matematico francese Evariste Galois. Li ha usati per trarre conclusioni sul risolvere equazioni polinomiali di grado superiore a cinque.

Da allora il concetto di gruppo ha aiutato a far luce su un numero di problemi in matematica e altrove. Sulla loro base, ad esempio, il fisico Murray-Gellman è stato in grado di prevedere l'esistenza di una particella prima che fosse effettivamente osservata negli esperimenti. [3] Per un altro esempio, i chimici usano la teoria dei gruppi per classificare le forme delle molecole. I matematici hanno persino utilizzato il concetto di gruppo per trarre conclusioni su qualcosa di così concreto come la carta da parati!
Dimostrare che un insieme di elementi con un certo operatore costituisca un gruppo significa che ciò che si sta descrivendo possiede una particolare simmetria. Non una simmetria nel senso comune del termine, ma in una forma più astratta. E questo può fornire intuizioni sostanziali su sistemi e problemi specifici. Le nozioni più complesse dell'algebra astratta ci danno semplicemente informazioni aggiuntive.
Più importantemente, vedrai l'importanza dei gruppi e dei campi teorici dei numeri nella pratica attraverso la loro applicazione nella crittografia, in particolare nella crittografia a chiave pubblica. Abbiamo già visto, nella nostra discussione sui campi, come i campi di estensione sono impiegati nel Cifrario di Rijndael. Elaboreremo quell'esempio nel *Capitolo 5*.

Per ulteriori discussioni sull'algebra astratta, consiglierei l'eccellente serie di video sull'algebra astratta di Socratica. [4] Raccomanderei in particolare i seguenti video: “What is abstract algebra?”, “Group definition (expanded)”, “Ring definition (expanded)”, e “Field definition (expanded)”. Questi quattro video ti forniranno ulteriori intuizioni su gran parte della discussione precedente. (Non abbiamo discusso degli anelli, ma un campo è semplicemente un tipo speciale di anello.)

Per ulteriori discussioni sulla teoria moderna dei numeri, puoi consultare molte discussioni avanzate sulla crittografia. Come suggerimenti, offrirei l'Introduzione alla Crittografia Moderna di Jonathan Katz e Yehuda Lindell o la Comprensione della Crittografia di Christof Paar e Jan Pelzl per ulteriori discussioni. [5]

**Note:**

[3] Vedi [Video YouTube](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Algebra Astratta](https://www.socratica.com/subject/abstract-algebra)

[5] Katz e Lindell, *Introduzione alla Crittografia Moderna*, 2ª ed., 2015 (CRC Press: Boca Raton, FL). Paar e Pelzl, *Comprensione della Crittografia*, 2010 (Springer-Verlag: Berlino).

# Crittografia Simmetrica
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice e Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Uno dei due principali rami della crittografia è la crittografia simmetrica. Include schemi di cifratura così come schemi preoccupati con l'autenticazione e l'integrità. Fino agli anni '70, tutta la crittografia avrebbe consistito di schemi di cifratura simmetrica.

La discussione principale inizia esaminando gli schemi di cifratura simmetrica e facendo la distinzione cruciale tra cifrari a flusso e cifrari a blocchi. Poi, ci si concentra sui codici di autenticazione dei messaggi, che sono schemi per garantire l'integrità e l'autenticità dei messaggi. Infine, esploriamo come gli schemi di cifratura simmetrica e i codici di autenticazione dei messaggi possono essere combinati per garantire una comunicazione sicura.

Questo capitolo discute varie schemi di crittografia simmetrica dalla pratica in modo superficiale. Il capitolo successivo offre una esposizione dettagliata della cifratura con un cifrario a flusso e un cifrario a blocchi dalla pratica, ovvero RC4 e AES rispettivamente.

Prima di iniziare la nostra discussione sulla crittografia simmetrica, voglio fare brevemente alcune osservazioni sulle illustrazioni di Alice e Bob in questo e nei capitoli successivi.

___

Nell'illustrare i principi della crittografia, le persone spesso si affidano a esempi che coinvolgono Alice e Bob. Farò lo stesso.

Specialmente se sei nuovo alla crittografia, è importante capire che questi esempi di Alice e Bob sono intesi solo come illustrazioni dei principi e delle costruzioni crittografiche in un ambiente semplificato. I principi e le costruzioni, tuttavia, sono applicabili a una gamma molto più ampia di contesti della vita reale.
Di seguito sono riportati cinque punti chiave da tenere a mente riguardo agli esempi che coinvolgono Alice e Bob nella crittografia:
1. Possono essere facilmente tradotti in esempi con altri tipi di attori come aziende o organizzazioni governative.
2. Possono essere facilmente estesi per includere tre o più attori.
3. Negli esempi, Bob e Alice sono tipicamente partecipanti attivi nella creazione di ogni messaggio e nell'applicazione di schemi crittografici su quel messaggio. Ma nella realtà, le comunicazioni elettroniche sono per lo più automatizzate. Quando si visita un sito web utilizzando la sicurezza del livello di trasporto, ad esempio, la crittografia è tipicamente gestita interamente dal proprio computer e dal server web.
4. Nel contesto della comunicazione elettronica, i "messaggi" che vengono inviati attraverso un canale di comunicazione sono solitamente pacchetti TCP/IP. Questi possono appartenere a un'e-mail, un messaggio di Facebook, una conversazione telefonica, un trasferimento di file, un sito web, un caricamento di software, e così via. Non sono messaggi nel senso tradizionale. Tuttavia, i crittografi spesso semplificano questa realtà affermando che il messaggio è, per esempio, un'e-mail.
5. Gli esempi si concentrano tipicamente sulla comunicazione elettronica, ma possono anche essere estesi a forme tradizionali di comunicazione come le lettere.

## Schemi di crittografia simmetrica

Possiamo definire in modo approssimativo uno **schema di crittografia simmetrica** come qualsiasi schema crittografico con tre algoritmi:

1. Un **algoritmo di generazione della chiave**, che genera una chiave privata.
2. Un **algoritmo di crittografia**, che prende la chiave privata e un testo in chiaro come input e produce un testo cifrato come output.
3. Un **algoritmo di decrittazione**, che prende la chiave privata e il testo cifrato come input e produce il testo in chiaro originale come output.

Tipicamente uno schema di crittografia—sia esso simmetrico o asimmetrico—offre un modello per la crittografia basato su un algoritmo di base, piuttosto che una specifica esatta.

Per esempio, consideriamo Salsa20, uno schema di crittografia simmetrica. Può essere utilizzato sia con chiavi di lunghezza 128 bit che 256 bit. La scelta riguardante la lunghezza della chiave influisce su alcuni dettagli minori dell'algoritmo (il numero di round nell'algoritmo per essere precisi).

Ma non si direbbe che usare Salsa20 con una chiave da 128 bit sia uno schema di crittografia diverso da Salsa20 con una chiave da 256 bit. L'algoritmo di base rimane lo stesso. Solo quando l'algoritmo di base cambia si potrebbe realmente parlare di due schemi di crittografia diversi.

Gli schemi di crittografia simmetrica sono tipicamente utili in due tipi di casi: (1) Quelli in cui due o più agenti comunicano a distanza e vogliono mantenere segreto il contenuto delle loro comunicazioni; e (2) quelli in cui un agente vuole mantenere segreto il contenuto di un messaggio nel tempo.

Puoi vedere una rappresentazione della situazione (1) in *Figura 1* qui sotto. Bob vuole inviare un messaggio $M$ ad Alice a distanza, ma non vuole che altri possano leggere quel messaggio.

Bob prima cifra il messaggio $M$ con la chiave privata $K$. Poi, invia il testo cifrato $C$ ad Alice. Una volta che Alice ha ricevuto il testo cifrato, può decifrarlo usando la chiave $K$ e leggere il testo in chiaro. Con un buon schema di crittografia, qualsiasi attaccante che intercetti il testo cifrato $C$ non dovrebbe essere in grado di apprendere nulla di realmente significativo sul messaggio $M$.

Puoi vedere una rappresentazione della situazione (2) in *Figura 2* qui sotto. Bob vuole impedire ad altri di visualizzare certe informazioni. Una situazione tipica potrebbe essere quella in cui Bob è un dipendente che memorizza dati sensibili sul suo computer, che né estranei né i suoi colleghi dovrebbero leggere.
Bob cifra il messaggio $M$ al tempo $T_0$ con la chiave $K$ per produrre il testo cifrato $C$. Al tempo $T_1$ ha nuovamente bisogno del messaggio e decifra il testo cifrato $C$ con la chiave $K$. Qualsiasi attaccante che potrebbe essere venuto a conoscenza del testo cifrato $C$ nel frattempo non dovrebbe essere stato in grado di dedurre nulla di significativo su $M$ da esso.

*Figura 1: Segretezza nello spazio*

![Figura 1: Segretezza nello spazio](assets/Figure4-1.webp "Figura 1: Segretezza nello spazio")

*Figura 2: Segretezza nel tempo*

![Figura 2: Segretezza nel tempo](assets/Figure4-2.webp "Figura 2: Segretezza nel tempo")

## Un esempio: Il cifrario di Cesare
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

Nel Capitolo 2, abbiamo incontrato il cifrario di Cesare, che è un esempio di un semplicissimo schema di cifratura simmetrica. Vediamolo di nuovo qui.

Supponiamo un dizionario *D* che equipara tutte le lettere dell'alfabeto inglese, in ordine, con l'insieme dei numeri $\{0,1,2,\dots,25\}$. Si assume un insieme di possibili messaggi **M**. Il cifrario di Cesare è, quindi, uno schema di cifratura definito come segue:

- Selezionare casualmente una chiave $k$ dall'insieme delle possibili chiavi **K**, dove **K** = $\{0,1,2,\dots,25\}$
- Cifrare un messaggio $m \in$ **M**, come segue:
    - Separare $m$ nelle sue singole lettere $m_0, m_1,\dots, m_i, \dots, m_l$
    - Convertire ogni $m_i$ in un numero secondo *D*
    - Per ogni $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Convertire ogni $c_i$ in una lettera secondo *D*
    - Poi combinare $c_0, c_1,\dots, c_l$ per ottenere il testo cifrato $c$
- Decifrare un testo cifrato $c$ come segue:
    - Convertire ogni $c_i$ in un numero secondo *D*
    - Per ogni $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Convertire ogni $m_i$ in una lettera secondo *D*
    - Poi combinare $m_0, m_1,\dots, m_l$ per ottenere il messaggio originale $m$

Ciò che rende il cifrario di Cesare uno schema di cifratura simmetrica è che la stessa chiave viene utilizzata sia per il processo di cifratura che per quello di decifratura. Ad esempio, supponiamo che tu voglia cifrare il messaggio “DOG” usando il cifrario di Cesare, e che tu abbia selezionato casualmente "24" come chiave. Cifrando il messaggio con questa chiave si otterrebbe “BME”. L'unico modo per recuperare il messaggio originale è utilizzare la stessa chiave, "24", per il processo di decifratura.

Questo cifrario di Cesare è un esempio di **cifrario di sostituzione monoalfabetico**: uno schema di cifratura in cui l'alfabeto del testo cifrato è fisso (cioè, viene utilizzato solo un alfabeto). Assumendo che l'algoritmo di decifratura sia deterministico, ogni simbolo nel testo cifrato di sostituzione può al massimo corrispondere a un simbolo nel testo in chiaro.
Fino al 1700, molte applicazioni della crittografia si affidavano pesantemente ai cifrari di sostituzione monoalfabetica, sebbene spesso fossero molto più complessi del cifrario di Cesare. Si potrebbe, ad esempio, selezionare casualmente una lettera dell'alfabeto per ogni lettera del testo originale con il vincolo che ogni lettera occorra solo una volta nell'alfabeto del testo cifrato. Ciò significa che avresti fattoriale 26 possibili chiavi private, che era enorme nell'era pre-informatica.
Nota che incontrerai spesso il termine **cifrario** nella crittografia. Sii consapevole che questo termine ha vari significati. Infatti, conosco almeno cinque significati distinti del termine all'interno della crittografia.

In alcuni casi si riferisce a uno schema di crittografia, come nel cifrario di Cesare e nel cifrario di sostituzione monoalfabetica. Tuttavia, il termine può anche riferirsi specificamente all'algoritmo di crittografia, alla chiave privata, o semplicemente al testo cifrato di qualsiasi schema di crittografia.

Infine, il termine cifrario può anche riferirsi a un algoritmo di base da cui è possibile costruire schemi crittografici. Questi possono includere vari algoritmi di crittografia, ma anche altri tipi di schemi crittografici. Questo senso del termine diventa rilevante nel contesto dei cifrari a blocchi (vedi la sezione "Cifrari a blocchi" qui sotto).

Potresti anche incontrare i termini **cifrare** o **decifrare**. Questi termini sono semplicemente sinonimi di crittografia e decrittografia.

## Attacchi di forza bruta e il principio di Kerckhoff
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Il cifrario di Cesare è uno schema di crittografia simmetrica molto insicuro, almeno nel mondo moderno. [1] Un attaccante potrebbe semplicemente tentare la decrittazione di qualsiasi testo cifrato con tutte le 26 chiavi possibili per vedere quale risultato ha senso. Questo tipo di attacco, dove l'attaccante sta semplicemente ciclando attraverso le chiavi per vedere cosa funziona, è noto come **attacco di forza bruta** o **ricerca esaustiva della chiave**.

Perché uno schema di crittografia soddisfi una nozione minima di sicurezza, deve avere un insieme di chiavi possibili, o **spazio delle chiavi**, che sia così grande da rendere gli attacchi di forza bruta impraticabili. Tutti gli schemi di crittografia moderni soddisfano questo standard. È noto come il **principio dello spazio delle chiavi sufficiente**. Un principio simile si applica tipicamente in diversi tipi di schemi crittografici.

Per avere un'idea della grandezza massiva dello spazio delle chiavi negli schemi di crittografia moderni, supponiamo che un file sia stato crittografato con una chiave a 128 bit utilizzando lo standard di crittografia avanzato. Ciò significa che un attaccante ha un insieme di $2^{128}$ chiavi attraverso le quali deve ciclare per un attacco di forza bruta. Una possibilità di successo dello 0,78% con questa strategia richiederebbe all'attaccante di ciclare attraverso circa $2.65 \times 10^{36}$ chiavi.

Supponiamo ottimisticamente che un attaccante possa tentare $10^{16}$ chiavi al secondo (cioè, 10 quadrilioni di chiavi al secondo). Per testare lo 0,78% di tutte le chiavi nello spazio delle chiavi, il suo attacco dovrebbe durare $2.65 \times 10^{20}$ secondi. Questo è circa 8,4 trilioni di anni. Quindi, anche un attacco di forza bruta da parte di un avversario assurdamente potente non è realistico con uno schema di crittografia moderno a 128 bit. Questo è il principio dello spazio delle chiavi sufficiente in azione.

Il cifrario di Cesare è più sicuro se l'attaccante non conosce l'algoritmo di crittografia? Forse, ma non di molto.
In ogni caso, la crittografia moderna assume sempre che la sicurezza di qualsiasi schema di crittografia simmetrica dipenda unicamente dal mantenimento segreto della chiave privata. Si presume sempre che l'attaccante conosca tutti gli altri dettagli, inclusi lo spazio dei messaggi, lo spazio delle chiavi, lo spazio dei crittogrammi, l'algoritmo di selezione della chiave, l'algoritmo di cifratura e l'algoritmo di decifratura.
L'idea che la sicurezza di uno schema di crittografia simmetrica possa dipendere solo dal segreto della chiave privata è nota come **principio di Kerckhoffs**.

Come originariamente inteso da Kerckhoffs, il principio si applica solo agli schemi di crittografia simmetrica. Una versione più generale del principio, tuttavia, si applica anche a tutti gli altri tipi di schemi crittografici moderni: il design di qualsiasi schema crittografico non deve essere necessario che sia segreto affinché sia sicuro; il segreto può estendersi solo ad alcune stringhe di informazioni, tipicamente una chiave privata.

Il principio di Kerckhoffs è centrale nella crittografia moderna per quattro motivi. Primo, esiste solo un numero limitato di schemi crittografici per tipi particolari di applicazioni. Ad esempio, la maggior parte delle applicazioni di crittografia simmetrica moderna utilizza il cifrario Rijndael. Quindi, il tuo segreto riguardo al design di uno schema è molto limitato. C'è, tuttavia, molta più flessibilità nel mantenere segreta qualche chiave privata per il cifrario Rijndael.

Secondo, è più facile sostituire una stringa di informazioni che un intero schema crittografico. Supponiamo che tutti i dipendenti di un'azienda abbiano lo stesso software di crittografia e che ogni due dipendenti abbiano una chiave privata per comunicare confidenzialmente. I compromessi delle chiavi sono un problema in questo scenario, ma almeno l'azienda potrebbe mantenere il software con tali violazioni di sicurezza. Se l'azienda si affidasse al segreto dello schema, allora qualsiasi violazione di quel segreto richiederebbe la sostituzione di tutto il software.

Terzo, il principio di Kerckhoffs consente la standardizzazione e la compatibilità tra gli utenti degli schemi crittografici. Questo ha enormi benefici per l'efficienza. Ad esempio, è difficile immaginare come milioni di persone potrebbero connettersi in modo sicuro ai server web di Google ogni giorno, se quella sicurezza richiedesse di mantenere segreti gli schemi crittografici.

Quarto, il principio di Kerckhoff consente il controllo pubblico degli schemi crittografici. Questo tipo di controllo è assolutamente necessario per ottenere schemi crittografici sicuri. A titolo illustrativo, l'algoritmo principale della crittografia simmetrica, il cifrario Rijndael, è stato il risultato di una competizione organizzata dal National Institute of Standards and Technology tra il 1997 e il 2000.

Qualsiasi sistema che tenti di ottenere la **sicurezza tramite l'oscurità** è un sistema che si basa sul mantenimento segreto dei dettagli del suo design e/o implementazione. In crittografia, sarebbe specificamente un sistema che si basa sul mantenimento segreto dei dettagli del design dello schema crittografico. Quindi, la sicurezza tramite l'oscurità è in diretto contrasto con il principio di Kerckhoffs.

La capacità dell'apertura di rafforzare la qualità e la sicurezza si estende anche più ampiamente al mondo digitale rispetto alla sola crittografia. Le distribuzioni Linux libere e open source come Debian, ad esempio, hanno generalmente diversi vantaggi rispetto ai loro omologhi Windows e MacOS in termini di privacy, stabilità, sicurezza e flessibilità. Sebbene ciò possa avere molteplici cause, il principio più importante è probabilmente, come Eric Raymond ha formulato nel suo famoso saggio "The Cathedral and the Bazaar", che "dato un numero sufficiente di occhi, tutti i bug sono superficiali". È questo principio di saggezza della folla che ha dato a Linux il suo successo più significativo.
Non si può mai affermare in modo univoco che uno schema crittografico sia "sicuro" o "insicuro". Invece, esistono varie nozioni di sicurezza per gli schemi crittografici. Ogni **definizione di sicurezza crittografica** deve specificare (1) gli obiettivi di sicurezza, così come (2) le capacità di un attaccante. Analizzare gli schemi crittografici rispetto a una o più nozioni specifiche di sicurezza fornisce intuizioni sulle loro applicazioni e limitazioni.
Sebbene non approfondiremo tutti i dettagli delle varie nozioni di sicurezza crittografica, dovresti sapere che due presupposti sono ubiqui a tutte le nozioni moderne di sicurezza crittografica relative agli schemi simmetrici e asimmetrici (e, in qualche forma, ad altri primitivi crittografici):

* La conoscenza dell'attaccante riguardo allo schema è conforme al principio di Kerckhoffs.
* L'attaccante non può realisticamente eseguire un attacco a forza bruta sullo schema. In particolare, i modelli di minaccia delle nozioni di sicurezza crittografica tipicamente non consentono nemmeno attacchi a forza bruta, poiché si presume che questi non siano una considerazione rilevante.

**Note:**

[1] Secondo Seutonio, un cifrario a sostituzione con un valore chiave costante di 3 veniva utilizzato da Giulio Cesare nelle sue comunicazioni militari. Quindi A diventava sempre D, B sempre E, C sempre F, e così via. Questa particolare versione del cifrario a sostituzione è, quindi, diventata nota come il **Cifrario di Cesare** (anche se non è realmente un cifrario nel senso moderno della parola, poiché il valore della chiave è costante). Il cifrario di Cesare potrebbe essere stato sicuro nel primo secolo a.C., se i nemici di Roma erano molto poco familiari con la crittografia. Ma chiaramente non sarebbe uno schema molto sicuro nei tempi moderni.

[2] Jonathan Katz e Yehuda Lindell, _Introduzione alla Crittografia Moderna_, CRC Press (Boca Raton, FL: 2015), p. 7f.

[3] Eric Raymond, “La Cattedrale e il Bazar”, il documento è stato presentato al Linux Kongress, Würzburg, Germania (27 maggio 1997). Esistono numerose versioni successive disponibili così come un libro. Le mie citazioni provengono dalla pagina 30 del libro: Eric Raymond, _La Cattedrale e il Bazar: Riflessioni su Linux e Open Source da un Rivoluzionario per Caso_, edizione riveduta (2001), O’Reilly: Sebastopol, CA.

## Cifrari a flusso
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Gli schemi di crittografia simmetrica sono standardmente suddivisi in due tipi: **cifrari a flusso** e **cifrari a blocchi**. Questa distinzione è tuttavia alquanto problematica, poiché le persone usano questi termini in modo non coerente. Nelle prossime sezioni, stabilirò la distinzione nel modo che ritengo migliore. Dovresti essere consapevole, tuttavia, che molte persone useranno questi termini in modo un po' diverso da come ho stabilito.

Cominciamo prima con i cifrari a flusso. Un **cifrario a flusso** è uno schema di crittografia simmetrica dove la crittografia consiste di due passaggi.

Primo, viene prodotta una stringa della lunghezza del testo in chiaro tramite una chiave privata. Questa stringa è chiamata **keystream**.

Successivamente, il keystream è combinato matematicamente con il testo in chiaro per produrre un testo cifrato. Questa combinazione è tipicamente un'operazione XOR. Per decifrare, puoi semplicemente invertire l'operazione. (Nota che $A \oplus B = B \oplus A$, nel caso in cui $A$ e $B$ siano stringhe di bit. Quindi l'ordine di un'operazione XOR in un cifrario a flusso non importa per il risultato. Questa proprietà è nota come **commutatività**.)
Un tipico cifrario a flusso XOR è rappresentato nella *Figura 3*. Si inizia prendendo una chiave privata $K$ e utilizzandola per generare un flusso di chiavi. Questo flusso è poi combinato con il testo in chiaro tramite un'operazione XOR per produrre il testo cifrato. Qualsiasi agente che riceve il testo cifrato può facilmente decifrarlo se possiede la chiave $K$. Tutto ciò di cui ha bisogno è creare un flusso di chiavi lungo quanto il testo cifrato seguendo la procedura specificata dallo schema e applicare l'XOR con il testo cifrato.

*Figura 3: Un cifrario a flusso XOR*

![Figura 3: Un cifrario a flusso XOR](assets/Figure4-3.webp "Figura 3: Un cifrario a flusso XOR")

Ricorda che uno schema di cifratura è tipicamente un modello per la cifratura con lo stesso algoritmo di base, piuttosto che una specifica esatta. Di conseguenza, un cifrario a flusso è tipicamente un modello per la cifratura in cui si possono utilizzare chiavi di lunghezze diverse. Anche se la lunghezza della chiave può influenzare alcuni dettagli minori dello schema, non ne influenzerà la forma essenziale.

Il cifrario di Cesare è un esempio di cifrario a flusso molto semplice e insicuro. Utilizzando una singola lettera (la chiave privata), si può produrre una stringa di lettere della lunghezza del messaggio (il flusso di chiavi). Questo flusso è poi combinato con il testo in chiaro tramite un'operazione modulo per produrre un testo cifrato. (Questa operazione modulo può essere semplificata in un'operazione XOR quando si rappresentano le lettere in bit).

Un altro famoso esempio di cifrario a flusso è il **cifrario di Vigenère**, dal nome di Blaise de Vigenère che lo sviluppò completamente alla fine del XVI secolo (anche se altri avevano fatto molto lavoro precedente). È un esempio di **cifrario a sostituzione polialfabetica**: uno schema di cifratura in cui l'alfabeto del testo cifrato per un simbolo del testo in chiaro cambia a seconda della sua posizione nel testo. A differenza di un cifrario a sostituzione monoalfabetica, i simboli del testo cifrato possono essere associati a più di un simbolo del testo in chiaro.

Con la crescente popolarità della cifratura nell'Europa rinascimentale, crebbe anche la **crittoanalisi**—ovvero, la decifrazione dei testi cifrati—particolarmente, utilizzando l'**analisi delle frequenze**. Quest'ultima impiega regolarità statistiche nella nostra lingua per decifrare i testi, ed è stata scoperta dagli studiosi arabi già nel nono secolo. È una tecnica che funziona particolarmente bene con testi lunghi. E anche i più sofisticati cifrari a sostituzione monoalfabetica non erano più sufficienti contro l'analisi delle frequenze nel 1700 in Europa, particolarmente in ambiti militari e di sicurezza. Poiché il cifrario di Vigenère offriva un significativo avanzamento in termini di sicurezza, divenne popolare in questo periodo e si diffuse ampiamente alla fine del 1700.

Parlando in termini informali, lo schema di cifratura funziona come segue:

1. Seleziona una parola di più lettere come chiave privata.
2. Per qualsiasi messaggio, applica il cifrario di Cesare a ogni lettera del messaggio utilizzando la lettera corrispondente nella parola chiave come cifratura.
3. Se hai esaurito la parola chiave ma non hai ancora cifrato completamente il testo in chiaro, applica nuovamente le lettere della parola chiave come cifrario di Cesare alle lettere corrispondenti nel resto del testo.
4. Continua questo processo fino a quando l'intero messaggio è stato cifrato.

Per illustrare, supponiamo che la tua chiave privata sia "GOLD" e tu voglia cifrare il messaggio "CRYPTOGRAPHY". In tal caso, procederesti come segue secondo il cifrario di Vigenère:

- $c_0  = [(2 + 6) \mod 26] = 8 = I$
- $c_1  = [(17 + 14) \mod 26] = 5 = F$
- $c_2  = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Così, il testo cifrato $c$ = "IFJSZCRUGDSB".

Un altro famoso esempio di cifrario a flusso è il **one-time pad**. Con il one-time pad, si crea semplicemente una stringa di bit casuali lunga quanto il messaggio in chiaro e si produce il testo cifrato tramite l'operazione XOR. Pertanto, la chiave privata e il flusso di chiavi sono equivalenti con un one-time pad.

Mentre i cifrari Shift e Vigenere sono molto insicuri nell'era moderna, il one-time pad è molto sicuro se usato correttamente. Probabilmente la più famosa applicazione del one-time pad è stata, almeno fino agli anni '80, per la **linea diretta Washington-Mosca**.

La linea diretta è un collegamento di comunicazione diretto tra Washington e Mosca per questioni urgenti che è stato installato dopo la Crisi dei Missili di Cuba. La tecnologia per questa ha subito trasformazioni nel corso degli anni. Attualmente, include un cavo in fibra ottica diretto così come due collegamenti satellitari (per ridondanza), che abilitano e-mail e messaggistica testuale. Il collegamento termina in vari luoghi negli Stati Uniti. Il Pentagono, la Casa Bianca e Raven Rock Mountain sono punti finali noti. Contrariamente all'opinione popolare, la linea diretta non ha mai coinvolto telefoni.

In sostanza, lo schema del one-time pad funzionava come segue. Sia Washington che Mosca avrebbero avuto due insiemi di numeri casuali. Un insieme di numeri casuali, creato dai Russi, riguardava la cifratura e decifratura di qualsiasi messaggio in lingua russa. Un insieme di numeri casuali, creato dagli Americani, riguardava la cifratura e decifratura di qualsiasi messaggio in lingua inglese. Di tanto in tanto, ulteriori numeri casuali venivano consegnati all'altra parte tramite corrieri fidati.

Washington e Mosca erano, quindi, in grado di comunicare segretamente utilizzando questi numeri casuali per creare one-time pads. Ogni volta che si doveva comunicare, si utilizzava la porzione successiva di numeri casuali per il proprio messaggio.

Sebbene altamente sicuro, il one-time pad affronta significative limitazioni pratiche: la chiave deve essere lunga quanto il messaggio e nessuna parte di un one-time pad può essere riutilizzata. Questo significa che è necessario tenere traccia di dove ci si trova nel one-time pad, conservare un enorme numero di bit e scambiare bit casuali con le controparti di tanto in tanto. Di conseguenza, il one-time pad non è frequentemente usato nella pratica.

Invece, i cifrari a flusso pseudocasuali predominanti usati nella pratica sono **pseudorandom stream ciphers**. Salsa20 e una variante strettamente correlata chiamata ChaCha sono esempi di cifrari a flusso pseudocasuali comunemente utilizzati.
Con questi cifrari a flusso pseudocasuale, si seleziona inizialmente una chiave K casualmente che è più corta della lunghezza del testo in chiaro. Tale chiave casuale K è solitamente creata dal nostro computer sulla base di dati imprevedibili che raccoglie nel tempo, come il tempo tra i messaggi di rete, i movimenti del mouse e così via.
Questa chiave casuale $K$ viene poi inserita in un algoritmo di espansione che crea un flusso di chiavi pseudocasuale lungo quanto il messaggio. È possibile specificare esattamente quanto deve essere lungo il flusso di chiavi (ad esempio, 500 bit, 1000 bit, 1200 bit, 29.117 bit, e così via).

Un flusso di chiavi pseudocasuale appare *come se* fosse stato scelto completamente a caso dall'insieme di tutte le stringhe della stessa lunghezza. Pertanto, la cifratura con un flusso di chiavi pseudocasuale appare come se fosse stata effettuata con un blocco monouso. Ma ovviamente non è così.

Poiché la nostra chiave privata è più corta del flusso di chiavi e il nostro algoritmo di espansione deve essere deterministico affinché il processo di cifratura/decifratura funzioni, non ogni flusso di chiavi di quella particolare lunghezza potrebbe risultare come output dalla nostra operazione di espansione.

Supponiamo, ad esempio, che la nostra chiave privata abbia una lunghezza di 128 bit e che possiamo inserirla in un algoritmo di espansione per creare un flusso di chiavi molto più lungo, diciamo di 2.500 bit. Poiché il nostro algoritmo di espansione deve essere deterministico, il nostro algoritmo può al massimo selezionare $1/2^{128}$ stringhe con una lunghezza di 2.500 bit. Quindi, un tale flusso di chiavi non potrebbe mai essere selezionato interamente a caso da tutte le stringhe della stessa lunghezza.

La nostra definizione di un cifrario a flusso ha due aspetti: (1) un flusso di chiavi lungo quanto il testo in chiaro viene generato con l'aiuto di una chiave privata; e (2) questo flusso di chiavi viene combinato con il testo in chiaro, tipicamente tramite un'operazione XOR, per produrre il testo cifrato.

A volte le persone definiscono la condizione (1) in modo più rigoroso, affermando che il flusso di chiavi deve specificamente essere pseudocasuale. Ciò significa che né il cifrario a traslazione, né il blocco monouso sarebbero considerati cifrari a flusso.

A mio avviso, definire la condizione (1) in modo più ampio fornisce un modo più semplice per organizzare gli schemi di cifratura. Inoltre, significa che non dobbiamo smettere di chiamare un particolare schema di cifratura un cifrario a flusso solo perché apprendiamo che in realtà non si basa su flussi di chiavi pseudocasuali.

**Note:**

[4] Crypto Museum, "Washington-Moscow hotline," 2013, disponibile su [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Cifrari a blocchi
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Il primo modo in cui si comprende comunemente un **cifrario a blocchi** è come qualcosa di più primitivo rispetto a un cifrario a flusso: Un algoritmo principale che esegue una trasformazione che preserva la lunghezza su una stringa di lunghezza adeguata con l'aiuto di una chiave. Questo algoritmo può essere utilizzato per creare schemi di cifratura e forse altri tipi di schemi crittografici.
Spesso, un cifrario a blocchi può accettare stringhe di input di lunghezze variabili come 64, 128 o 256 bit, così come chiavi di lunghezze variabili come 128, 192 o 256 bit. Anche se alcuni dettagli dell'algoritmo potrebbero cambiare a seconda di queste variabili, l'algoritmo di base non cambia. Se cambiasse, parleremmo di due cifrari a blocchi differenti. Nota che l'uso della terminologia "algoritmo di base" qui è lo stesso che per gli schemi di crittografia.

Una rappresentazione di come funziona un cifrario a blocchi può essere vista in *Figura 4* qui sotto. Un messaggio $M$ di lunghezza $L$ e una chiave $K$ fungono da input al cifrario a blocchi. Esso restituisce un messaggio $M'$ di lunghezza $L$. La chiave non deve necessariamente avere la stessa lunghezza di $M$ e $M'$ per la maggior parte dei cifrari a blocchi.

*Figura 4: Un cifrario a blocchi*

![Figura 4: Un cifrario a blocchi](assets/Figure4-4.webp "Figura 4: Un cifrario a blocchi")

Un cifrario a blocchi di per sé non è uno schema di crittografia. Ma un cifrario a blocchi può essere utilizzato con vari **modi di operazione** per produrre diversi schemi di crittografia. Un modo di operazione aggiunge semplicemente alcune operazioni aggiuntive esterne al cifrario a blocchi.

Per illustrare come funziona, supponiamo un cifrario a blocchi (BC) che richiede una stringa di input di 128 bit e una chiave privata di 128 bit. La Figura 5 qui sotto mostra come quel cifrario a blocchi può essere utilizzato con il **modo di codice elettronico a libro** (**modalità ECB**) per creare uno schema di crittografia. (Le ellissi sulla destra indicano che puoi ripetere questo schema quanto è necessario).

*Figura 5: Un cifrario a blocchi con modalità ECB*

![Figura 5: Un cifrario a blocchi con modalità ECB](assets/Figure4-5.webp "Figura 5: Un cifrario a blocchi con modalità ECB")

Il processo per la crittografia del libro codice elettronico con il cifrario a blocchi è il seguente. Vedi se puoi dividere il tuo messaggio in chiaro in blocchi di 128 bit. Se no, aggiungi **padding** al messaggio, in modo che il risultato possa essere diviso uniformemente per la dimensione del blocco di 128 bit. Questi sono i tuoi dati utilizzati per il processo di crittografia.

Ora dividi i dati in pezzi di stringhe di 128 bit ($M_1$, $M_2$, $M_3$, e così via). Fai passare ogni stringa di 128 bit attraverso il cifrario a blocchi con la tua chiave di 128 bit per produrre pezzi di testo cifrato di 128 bit ($C_1$, $C_2$, $C_3$, e così via). Questi pezzi, quando ricombinati, formano il testo cifrato completo.

La decrittazione è semplicemente il processo inverso, anche se il destinatario ha bisogno di un modo riconoscibile per rimuovere qualsiasi padding dai dati decrittati per produrre il messaggio in chiaro originale.

Sebbene relativamente semplice, un cifrario a blocchi con modalità di libro codice elettronico manca di sicurezza. Questo perché porta a una **crittografia deterministica**. Qualsiasi due stringhe di dati identiche di 128 bit sono crittografate esattamente nello stesso modo. Questa informazione può essere sfruttata.

Invece, qualsiasi schema di crittografia costruito da un cifrario a blocchi dovrebbe essere **probabilistico**: cioè, la crittografia di qualsiasi messaggio $M$, o di qualsiasi pezzo specifico di $M$, dovrebbe generalmente produrre un risultato diverso ogni volta. [5]

La **modalità di concatenazione dei blocchi cifrati** (**modalità CBC**) è probabilmente il modo più comune utilizzato con un cifrario a blocchi. La combinazione, se fatta correttamente, produce uno schema di crittografia probabilistico. Puoi vedere una rappresentazione di questa modalità di operazione in *Figura 6* qui sotto.

*Figura 6: Un cifrario a blocchi con modalità CBC*
![Figura 6: Un cifrario a blocchi con modalità CBC](assets/Figure4-6.webp "Figura 6: Un cifrario a blocchi con modalità CBC")
Supponiamo che la dimensione del blocco sia nuovamente di 128 bit. Quindi, per iniziare, dovrai nuovamente assicurarti che il tuo messaggio in chiaro originale riceva il necessario padding.

Poi, esegui lo XOR della prima porzione di 128 bit del tuo testo in chiaro con un **vettore di inizializzazione** di 128 bit. Il risultato viene inserito nel cifrario a blocchi per produrre un criptotesto per il primo blocco. Per il secondo blocco di 128 bit, esegui prima lo XOR del testo in chiaro con il criptotesto del primo blocco, prima di inserirlo nel cifrario a blocchi. Continui questo processo fino a quando non hai criptato l'intero messaggio in chiaro.

Quando hai finito, invii il messaggio criptato insieme al vettore di inizializzazione non criptato al destinatario. Il destinatario ha bisogno di conoscere il vettore di inizializzazione, altrimenti non può decifrare il criptotesto.

Questa costruzione è molto più sicura della modalità libro codice elettronico quando usata correttamente. Dovresti, prima di tutto, assicurarti che il vettore di inizializzazione sia una stringa casuale o pseudocasuale. Inoltre, dovresti usare un vettore di inizializzazione diverso ogni volta che utilizzi questo schema di crittografia.

In altre parole, il tuo vettore di inizializzazione dovrebbe essere un nonce casuale o pseudocasuale, dove un **nonce** sta per "un numero che viene utilizzato una sola volta". Se mantieni questa pratica, allora la modalità CBC con un cifrario a blocchi assicura che qualsiasi due blocchi di testo in chiaro identici saranno generalmente criptati in modo diverso ogni volta.

Infine, rivolgiamo la nostra attenzione alla **modalità di feedback di output** (**modalità OFB**). Puoi vedere una rappresentazione di questa modalità nella *Figura 7*.

*Figura 7: Un cifrario a blocchi con modalità OFB*

![Figura 7: Un cifrario a blocchi con modalità OFB](assets/Figure4-7.webp "Figura 7: Un cifrario a blocchi con modalità OFB")

Con la modalità OFB selezioni anche un vettore di inizializzazione. Ma qui, per il primo blocco, il vettore di inizializzazione viene inserito direttamente nel cifrario a blocchi con la tua chiave. I 128 bit risultanti sono, quindi, trattati come un flusso di chiavi. Questo flusso di chiavi viene eseguito lo XOR con il testo in chiaro per produrre il criptotesto per il blocco. Per i blocchi successivi, utilizzi il flusso di chiavi del blocco precedente come input nel cifrario a blocchi e ripeti i passaggi.

Se osservi attentamente, ciò che è stato effettivamente creato qui dal cifrario a blocchi con modalità OFB è un cifrario a flusso. Generi porzioni di flusso di chiavi di 128 bit fino ad avere la lunghezza del testo in chiaro (scartando i bit che non ti servono dall'ultima porzione di flusso di chiavi di 128 bit). Poi, esegui lo XOR del flusso di chiavi con il tuo messaggio in chiaro per ottenere il criptotesto.

Nella sezione precedente sui cifrari a flusso, ho affermato che produci un flusso di chiavi con l'aiuto di una chiave privata. Per essere precisi, non deve essere creato solo con una chiave privata. Come puoi vedere nella modalità OFB, il flusso di chiavi è prodotto con il supporto sia di una chiave privata che di un vettore di inizializzazione.

Nota che, come con la modalità CBC, è importante selezionare un nonce pseudocasuale o casuale per il vettore di inizializzazione ogni volta che utilizzi un cifrario a blocchi in modalità OFB. Altrimenti, la stessa stringa di messaggi di 128 bit inviata in comunicazioni diverse sarà criptata nello stesso modo. Questo è un modo per creare una crittografia probabilistica con un cifrario a flusso.
Alcuni cifrari a flusso utilizzano solamente una chiave privata per creare un flusso di chiavi. Per questi cifrari a flusso, è importante che tu utilizzi un nonce casuale per selezionare la chiave privata per ogni istanza di comunicazione. Altrimenti, i risultati della cifratura con questi cifrari a flusso saranno anch'essi deterministici, portando a problemi di sicurezza.

Il cifrario a blocchi moderno più popolare è il **cifrario Rijndael**. È stato il vincitore tra quindici proposte in un concorso tenuto dal National Institute of Standards and Technology (NIST) tra il 1997 e il 2000 per sostituire un vecchio standard di cifratura, lo **standard di cifratura dei dati** (**DES**).

Il cifrario Rijndael può essere utilizzato con diverse specifiche per lunghezze di chiave e dimensioni di blocco, così come in diverse modalità di funzionamento. Il comitato per il concorso NIST ha adottato una versione ristretta del cifrario Rijndael, ovvero una che richiede dimensioni di blocco di 128 bit e lunghezze di chiave di 128 bit, 192 bit o 256 bit, come parte dello **standard avanzato di cifratura** (**AES**). Questo è davvero lo standard principale per le applicazioni di cifratura simmetrica. È così sicuro che persino la NSA sembra disposta ad utilizzarlo con chiavi da 256 bit per documenti top secret. [6]

Il cifrario a blocchi AES sarà spiegato in dettaglio nel *Capitolo 5*.

**Note:**

[5] L'importanza della cifratura probabilistica è stata sottolineata per la prima volta da Shafi Goldwasser e Silvio Micali, "Probabilistic encryption," _Journal of Computer and System Sciences_, 28 (1984), 270–99.

[6] Vedi NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).

## Chiarire la confusione

La confusione riguardo la distinzione tra cifrari a blocchi e cifrari a flusso sorge perché a volte le persone interpretano il termine cifrario a blocchi riferendosi specificamente a un *cifrario a blocchi con una modalità di cifratura a blocchi*.

Considera le modalità ECB e CBC nella sezione precedente. Queste richiedono specificamente che i dati per la cifratura siano divisibili per la dimensione del blocco (il che potrebbe richiedere l'uso di padding per il messaggio originale). Inoltre, i dati in queste modalità sono anche operati direttamente dal cifrario a blocchi (e non solo combinati con il risultato di un'operazione di cifrario a blocchi come nella modalità OFB).

Pertanto, alternativamente, puoi definire un **cifrario a blocchi** come qualsiasi schema di cifratura che opera su blocchi di messaggio di lunghezza fissa alla volta (dove ogni blocco deve essere più lungo di un byte, altrimenti si trasforma in un cifrario a flusso). Sia i dati per la cifratura che il testo cifrato devono dividersi uniformemente in questa dimensione di blocco. Tipicamente, la dimensione del blocco è di 64, 128, 192 o 256 bit in lunghezza. Al contrario, un cifrario a flusso può cifrare messaggi in pezzi di un bit o byte alla volta.

Con questa comprensione più specifica del cifrario a blocchi, puoi effettivamente affermare che gli schemi di cifratura moderni sono o cifrari a flusso o cifrari a blocchi. Da qui in poi, intenderò il termine cifrario a blocchi nel senso più generale a meno che non sia specificato diversamente.
La discussione sulla modalità OFB nella sezione precedente solleva anche un altro punto interessante. Alcuni cifrari a flusso sono costruiti a partire da cifrari a blocchi, come Rijndael con OFB. Alcuni, come Salsa20 e ChaCha, non sono creati a partire da cifrari a blocchi. Potresti chiamare questi ultimi **cifrari a flusso primitivi**. (Non esiste realmente un termine standardizzato per riferirsi a tali cifrari a flusso.)
Quando le persone parlano dei vantaggi e degli svantaggi dei cifrari a flusso e dei cifrari a blocchi, di solito stanno confrontando i cifrari a flusso primitivi con gli schemi di crittografia basati su cifrari a blocchi.

Mentre è sempre possibile costruire facilmente un cifrario a flusso a partire da un cifrario a blocchi, è tipicamente molto difficile costruire qualche tipo di costrutto con una modalità di cifratura a blocchi (come con la modalità CBC) a partire da un cifrario a flusso primitivo.

Da questa discussione, ora dovresti comprendere la *Figura 8*. Fornisce una panoramica sugli schemi di crittografia simmetrica. Utilizziamo tre tipi di schemi di crittografia: cifrari a flusso primitivi, cifrari a flusso basati su cifrari a blocchi e cifrari a blocchi in una modalità a blocchi (chiamati anche "cifrari a blocchi" nel diagramma).

*Figura 8: Panoramica degli schemi di crittografia simmetrica*

![Figura 8: Panoramica degli schemi di crittografia simmetrica](assets/Figure4-8.webp "Figura 8: Panoramica degli schemi di crittografia simmetrica")

## Codici di autenticazione dei messaggi
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

La crittografia si occupa della segretezza. Ma la crittografia si occupa anche di temi più ampi, come l'integrità dei messaggi, l'autenticità e la non ripudiabilità. I cosiddetti **codici di autenticazione dei messaggi** (MAC) sono schemi crittografici a chiave simmetrica che supportano l'autenticità e l'integrità nelle comunicazioni.

Perché è necessario qualcosa oltre alla segretezza nella comunicazione? Supponiamo che Bob invii ad Alice un messaggio utilizzando una crittografia praticamente infrangibile. Qualsiasi attaccante che intercetti questo messaggio non sarà in grado di ottenere informazioni significative riguardo al contenuto. Tuttavia, l'attaccante ha ancora almeno due altri vettori di attacco disponibili:

1. Potrebbe intercettare il testo cifrato, alterarne il contenuto e inviare il testo cifrato modificato ad Alice.
2. Potrebbe bloccare completamente il messaggio di Bob e inviare il proprio testo cifrato creato.

In entrambi questi casi, l'attaccante potrebbe non avere alcuna intuizione sui contenuti dai testi cifrati (1) e (2). Ma potrebbe comunque causare danni significativi in questo modo. Qui diventano importanti i codici di autenticazione dei messaggi.

I codici di autenticazione dei messaggi sono definiti in modo non rigoroso come schemi crittografici simmetrici con tre algoritmi: un algoritmo di generazione della chiave, un algoritmo di generazione del tag e un algoritmo di verifica. Un MAC sicuro garantisce che i tag siano **inforgevoli esistenzialmente** per qualsiasi attaccante, ovvero, non possono creare con successo un tag sul messaggio che verifica, a meno che non abbiano la chiave privata.

Bob e Alice possono combattere la manipolazione di un messaggio particolare usando un MAC. Supponiamo per un momento che a loro non importi della segretezza. Vogliono solo assicurarsi che il messaggio ricevuto da Alice sia effettivamente di Bob e non sia stato modificato in alcun modo.

Il processo è rappresentato nella *Figura 9*. Per utilizzare un **MAC** (Codice di Autenticazione del Messaggio), genererebbero prima una chiave privata $K$ condivisa tra loro. Bob crea un tag $T$ per il messaggio utilizzando la chiave privata $K$. Invia quindi il messaggio così come il tag del messaggio ad Alice. Lei può quindi verificare che Bob abbia effettivamente creato il tag, eseguendo la chiave privata, il messaggio e il tag attraverso un algoritmo di verifica.

*Figura 9: Panoramica degli schemi di crittografia simmetrica*
![Figura 9: Panoramica degli schemi di crittografia simmetrica](assets/Figure4-9.webp "Figura 9: Panoramica degli schemi di crittografia simmetrica")
A causa della **inviolabilità esistenziale**, un attaccante non può modificare in alcun modo il messaggio $M$ o creare un proprio messaggio con un tag valido. Questo avviene anche se l'attaccante osserva i tag di molti messaggi tra Bob e Alice che utilizzano la stessa chiave privata. Al massimo, un attaccante potrebbe impedire ad Alice di ricevere il messaggio $M$ (un problema che la crittografia non può affrontare).

Un MAC garantisce che un messaggio sia stato effettivamente creato da Bob. Questa autenticità implica automaticamente l'integrità del messaggio, ovvero, se Bob ha creato un certo messaggio, allora, di fatto, non è stato alterato in alcun modo da un attaccante. Quindi, d'ora in poi, qualsiasi preoccupazione per l'autenticazione dovrebbe essere automaticamente intesa come una preoccupazione per l'integrità.

Sebbene abbia tracciato una distinzione tra autenticità e integrità del messaggio nella mia discussione, è anche comune usare questi termini come sinonimi. Essi, quindi, si riferiscono all'idea di messaggi che sono stati creati da un mittente particolare e non alterati in alcun modo. In questo spirito, i codici di autenticazione dei messaggi sono spesso chiamati anche **codici di integrità dei messaggi**.

## Crittografia autenticata
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Tipicamente, si vorrebbe garantire sia la segretezza che l'autenticità nella comunicazione e, quindi, gli schemi di crittografia e gli schemi MAC sono tipicamente utilizzati insieme.

Uno **schema di crittografia autenticata** è uno schema che combina la crittografia con un MAC in modo altamente sicuro. Specificamente, deve soddisfare gli standard per l'inviolabilità esistenziale così come una nozione molto forte di segretezza, ovvero una che è resistente agli **attacchi a testo cifrato scelto**. [7]

Affinché uno schema di crittografia sia resistente agli attacchi a testo cifrato scelto, deve soddisfare gli standard per la **non malleabilità**: ovvero, qualsiasi modifica di un testo cifrato da parte di un attaccante dovrebbe produrre o un testo cifrato non valido o uno che, una volta decifrato, rivela un testo in chiaro senza alcuna relazione con l'originale. [8]

Poiché uno schema di crittografia autenticata garantisce che un testo cifrato creato da un attaccante sia sempre non valido (poiché il tag non verrà verificato), soddisfa gli standard per la resistenza agli attacchi a testo cifrato scelto. Interessantemente, si può dimostrare che uno schema di crittografia autenticata può sempre essere creato dalla combinazione di un MAC inviolabile esistenzialmente e uno schema di crittografia che soddisfa una nozione di sicurezza meno forte, nota come **sicurezza contro attacchi a testo in chiaro scelto**.

Non entreremo in tutti i dettagli della costruzione degli schemi di crittografia autenticata. Ma è importante conoscere due dettagli della loro costruzione.

Primo, uno schema di crittografia autenticata gestisce prima la crittografia e poi crea un tag del messaggio sul testo cifrato. Si è scoperto che altri approcci, come combinare il testo cifrato con un tag sul testo in chiaro, o prima creare un tag e poi cifrare sia il testo in chiaro che il tag, sono insicuri. Inoltre, entrambe le operazioni hanno la propria chiave privata selezionata casualmente, altrimenti la tua sicurezza è gravemente compromessa.

Il principio sopra menzionato si applica più in generale: *si dovrebbero sempre utilizzare chiavi distinte quando si combinano schemi crittografici di base*.

Uno schema di crittografia autenticata è rappresentato nella *Figura 10*. Bob crea prima un testo cifrato $C$ dal messaggio $M$ utilizzando una chiave $K_C$ selezionata casualmente. Poi crea un tag del messaggio $T$ eseguendo il testo cifrato e una diversa chiave $K_T$ selezionata casualmente attraverso l'algoritmo di generazione del tag. Sia il testo cifrato che il tag del messaggio vengono inviati ad Alice.
Alice verifica ora prima se il tag è valido dato il testo cifrato $C$ e la chiave $K_T$. Se valido, può quindi decifrare il messaggio usando la chiave $K_C$. Non solo le è garantita una nozione molto forte di segretezza nelle loro comunicazioni, ma sa anche che il messaggio è stato creato da Bob.
*Figura 10: Uno schema di crittografia autenticata*

![Figura 10: Uno schema di crittografia autenticata](assets/Figure4-10.webp "Figura 10: Uno schema di crittografia autenticata")

Come vengono creati i MAC? Sebbene i MAC possano essere creati tramite diversi metodi, un modo comune ed efficiente per crearli è tramite **funzioni hash crittografiche**.

Introdurremo le funzioni hash crittografiche più approfonditamente nel *Capitolo 6*. Per ora, sappi solo che una **funzione hash** è una funzione calcolabile efficientemente che prende in input dati di dimensione arbitraria e produce output di lunghezza fissa. Ad esempio, la popolare funzione hash **SHA-256** (secure hash algorithm 256) genera sempre un output di 256 bit indipendentemente dalla dimensione dell'input. Alcune funzioni hash, come SHA-256, hanno applicazioni utili in crittografia.

Il tipo più comune di tag prodotto con una funzione hash crittografica è il **codice di autenticazione del messaggio basato su hash** (HMAC). Il processo è illustrato nella *Figura 11*. Una parte produce due chiavi distinte da una chiave privata $K$, la chiave interna $K_1$ e la chiave esterna $K_2$. Il testo in chiaro $M$ o il testo cifrato $C$ viene quindi hashato insieme alla chiave interna. Il risultato $T'$ viene poi hashato con la chiave esterna per produrre il tag del messaggio $T$.

Esiste una gamma di funzioni hash che possono essere utilizzate per creare un HMAC. La funzione hash più comunemente impiegata è SHA-256.

*Figura 11: HMAC*

![Figura 11: HMAC](assets/Figure4-11.webp "Figura 11: HMAC")

**Note:**

[7] I risultati specifici discussi in questa sezione provengono da Katz e Lindell, pp. 131–47.

[8] Tecnicamente, la definizione di attacchi con testo cifrato scelto è diversa dalla nozione di non-malleabilità. Ma si può dimostrare che queste due nozioni di sicurezza sono equivalenti.

## Sessioni di comunicazione sicure
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Supponiamo che due parti siano in una sessione di comunicazione, quindi inviano più messaggi avanti e indietro.

Uno schema di crittografia autenticata consente al destinatario di un messaggio di verificare che sia stato creato dal suo partner nella sessione di comunicazione (purché la chiave privata non sia stata divulgata). Questo funziona abbastanza bene per un singolo messaggio. Tipicamente, tuttavia, due parti inviano messaggi avanti e indietro in una sessione di comunicazione. E in quel contesto, uno schema di crittografia autenticata semplice, come descritto nella sezione precedente, non è sufficiente a garantire la sicurezza.

Il motivo principale è che uno schema di crittografia autenticata non fornisce alcuna garanzia che il messaggio sia stato effettivamente inviato anche dall'agente che lo ha creato all'interno di una sessione di comunicazione. Considera i seguenti tre vettori di attacco:

1. **Attacco di replay**: Un attaccante reinvia un testo cifrato e un tag che ha intercettato tra due parti in un momento precedente.
2. **Attacco di riordino**: Un attaccante intercetta due messaggi in momenti diversi e li invia al destinatario nell'ordine inverso.
3. **Attacco di riflessione**: Un attaccante osserva un messaggio inviato da A a B e invia anche quel messaggio ad A.

Sebbene l'attaccante non abbia conoscenza del testo cifrato e non possa creare testi cifrati falsificati, gli attacchi sopra menzionati possono comunque causare danni significativi nelle comunicazioni.
Supponiamo, ad esempio, che un particolare messaggio tra due parti comporti il trasferimento di fondi finanziari. Un attacco di tipo replay potrebbe trasferire i fondi una seconda volta. Uno schema di crittografia autenticata vanilla non ha difese contro tali attacchi.
Fortunatamente, questo tipo di attacchi può essere facilmente mitigato in una sessione di comunicazione utilizzando **identificatori** e **indicatori di tempo relativi**.

Gli identificatori possono essere aggiunti al messaggio in chiaro prima della crittografia. Questo impedirebbe qualsiasi attacco di riflessione. Un indicatore di tempo relativo può, ad esempio, essere un numero di sequenza in una particolare sessione di comunicazione. Ogni parte aggiunge un numero di sequenza a un messaggio prima della crittografia, così il destinatario sa in che ordine i messaggi sono stati inviati. Questo elimina la possibilità di attacchi di riordinamento. Elimina anche gli attacchi di replay. Qualsiasi messaggio che un attaccante invia lungo la linea avrà un numero di sequenza vecchio, e il destinatario saprà di non dover elaborare di nuovo il messaggio.

Per illustrare come funzionano le sessioni di comunicazione sicure, supponiamo ancora Alice e Bob. Essi inviano un totale di quattro messaggi avanti e indietro. Potete vedere come funzionerebbe uno schema di crittografia autenticata con identificatori e numeri di sequenza di seguito nella *Figura 11*.

La sessione di comunicazione inizia con Bob che invia un testo cifrato $C_{0,B}$ ad Alice con un tag del messaggio $T_{0,B}$. Il testo cifrato contiene il messaggio, così come un identificatore (BOB) e un numero di sequenza (0). Il tag $T_{0,B}$ è realizzato sull'intero testo cifrato. Nelle loro comunicazioni successive, Alice e Bob mantengono questo protocollo, aggiornando i campi secondo necessità.

*Figura 12: Una sessione di comunicazione sicura*

![Figura 12: Una sessione di comunicazione sicura](assets/Figure4-12.webp "Figura 12: Una sessione di comunicazione sicura")

# RC4 e AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## Il cifrario a flusso RC4
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

In questo capitolo, discuteremo i dettagli di uno schema di crittografia con un moderno cifrario a flusso primitivo, RC4 (o "Rivest cipher 4"), e un moderno cifrario a blocchi, AES. Mentre il cifrario RC4 è caduto in disgrazia come metodo di crittografia, AES è lo standard per la crittografia simmetrica moderna. Questi due esempi dovrebbero dare un'idea migliore di come funziona sotto il cofano la crittografia simmetrica.

___

Per avere un'idea di come funzionano i moderni cifrari a flusso pseudocasuali, mi concentrerò sul cifrario a flusso RC4. È un cifrario a flusso pseudocasuale che è stato utilizzato nei protocolli di sicurezza per punti di accesso wireless WEP e WAP, così come in TLS. Poiché RC4 ha molte debolezze dimostrate, è caduto in disgrazia. Infatti, l'Internet Engineering Task Force ora vieta l'uso delle suite RC4 da parte di applicazioni client e server in tutte le istanze di TLS. Tuttavia, funziona bene come esempio per illustrare come funziona un cifrario a flusso primitivo.

Per iniziare, mostrerò prima come crittografare un messaggio in chiaro con un cifrario RC4 per principianti. Supponiamo che il nostro messaggio in chiaro sia “SOUP.” La crittografia con il nostro cifrario RC4 per principianti, quindi, procede in quattro passaggi.

### Passo 1
Prima, definisci un array **S** con $S[0] = 0$ fino a $S[7] = 7$. Un array qui significa semplicemente una collezione mutabile di valori organizzati per indice, chiamato anche lista in alcuni linguaggi di programmazione (ad esempio, Python). In questo caso, l'indice va da 0 a 7, e i valori vanno anch'essi da 0 a 7. Quindi **S** è come segue:
- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

I valori qui non sono numeri ASCII, ma le rappresentazioni in valore decimale di stringhe di 1 byte. Quindi il valore 2 sarebbe uguale a $0000 \ 0011$. La lunghezza dell'array **S** è, quindi, di 8 byte.

### Passo 2

Secondo, definisci un array chiave **K** della lunghezza di 8 byte scegliendo una chiave tra 1 e 8 byte (senza frazioni di byte permesse). Poiché ogni byte è di 8 bit, puoi selezionare qualsiasi numero tra 0 e 255 per ogni byte della tua chiave.

Supponiamo di scegliere la nostra chiave **k** come $[14, 48, 9]$, in modo che abbia una lunghezza di 3 byte. Ogni indice del nostro array chiave è, quindi, impostato secondo il valore decimale per quel particolare elemento della chiave, in ordine. Se esaurisci l'intera chiave, inizia di nuovo dall'inizio, fino a riempire gli 8 slot dell'array chiave. Quindi, il nostro array chiave è come segue:

- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Passo 3

Terzo, trasformeremo l'array **S** usando l'array chiave **K**, in un processo noto come **programmazione della chiave**. Il processo è il seguente in pseudocodice:

- Crea le variabili **j** e **i**
- Imposta la variabile $j = 0$
- Per ogni $i$ da 0 a 7:
    - Imposta $j = (j + S[i] + K[i]) \mod 8$
    - Scambia $S[i]$ e $S[j]$

La trasformazione dell'array **S** è catturata dalla *Tabella 1*.

Per iniziare, puoi vedere lo stato iniziale di **S** come $[0, 1, 2, 3, 4, 5, 6, 7]$ con un valore iniziale di 0 per **j**. Questo sarà trasformato usando l'array chiave $[14, 48, 9, 14, 48, 9, 14, 48]$.

Il ciclo for inizia con $i = 0$. Secondo il nostro pseudocodice sopra, il nuovo valore di **j** diventa 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Scambiando $S[0]$ e $S[6]$, lo stato di **S** dopo 1 round diventa $[6, 1, 2, 3, 4, 5, 0, 7]$.
Nella riga successiva, $i = 1$. Ripercorrendo il ciclo for, **j** ottiene un valore di 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Scambiando $S[1]$ e $S[7]$ dallo stato corrente di **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, si ottiene $[6, 7, 2, 3, 4, 5, 0, 1]$ dopo il secondo round.
Continuiamo con questo processo fino a produrre la riga finale in fondo per l'array **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Tabella 1: Tabella di pianificazione delle chiavi*

| Round   | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Iniziale|     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |
Come quarto passo, produciamo il **keystream**. Questo è la stringa pseudocasuale di lunghezza uguale al messaggio che vogliamo inviare. Questo sarà utilizzato per criptare il messaggio originale "SOUP". Poiché il keystream deve essere lungo quanto il messaggio, abbiamo bisogno di uno che abbia 4 byte.
Il keystream è prodotto dal seguente pseudocodice:

- Crea le variabili **j**, **i** e **t**.
- Imposta $j = 0$.
- Per ogni $i$ del testo in chiaro, partendo da $i = 1$ e proseguendo fino a $i = 4$, ogni byte del keystream è prodotto come segue:
    - $j = (j + S[i]) \mod 8$
    - Scambia $S[i]$ e $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - Il byte $i^{esimo}$ del keystream = $S[t]$

Puoi seguire i calcoli nella *Tabella 2*.

Lo stato iniziale di **S** è $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Impostando $i = 1$, il valore di **j** diventa 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Poi scambiamo $S[1]$ e $S[4]$ per produrre la trasformazione di **S** nella seconda riga, $[6, 3, 1, 0, 4, 7, 5, 2]$. Il valore di **t** è quindi 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Infine, il byte per il keystream è $S[7]$, ovvero 2.

Proseguiamo quindi a produrre gli altri byte fino ad avere i seguenti quattro byte: 2, 6, 3 e 7. Ognuno di questi byte può quindi essere utilizzato per criptare ogni lettera del testo in chiaro, "SOUP".

Per iniziare, utilizzando una tabella ASCII, possiamo vedere che “SOUP” codificato dai valori decimali delle stringhe di byte sottostanti è “83 79 85 80”. La combinazione con il keystream “2 6 3 7” produce “85 85 88 87”, che rimane invariato dopo un'operazione modulo 256. In ASCII, il testo cifrato “85 85 88 87” equivale a “UUXW”.

Cosa succede se la parola da criptare fosse più lunga dell'array **S**? In tal caso, l'array **S** continua a trasformarsi in questo modo mostrato sopra per ogni byte **i** del testo in chiaro, fino ad avere un numero di byte nel keystream uguale al numero di lettere nel testo in chiaro.

*Tabella 2: Generazione del Keystream*

| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
L'esempio che abbiamo appena discusso è solo una versione semplificata del **cifrario a flusso RC4**. Il vero cifrario a flusso RC4 ha un array **S** di 256 byte di lunghezza, non di 8 byte, e una chiave che può essere tra 1 e 256 byte, non tra 1 e 8 byte. L'array della chiave e i flussi delle chiavi sono quindi tutti prodotti considerando la lunghezza di 256 byte dell'array **S**. I calcoli diventano immensamente più complessi, ma i principi rimangono gli stessi. Utilizzando la stessa chiave, [14,48,9], con il cifrario RC4 standard, il messaggio in chiaro "SOUP" viene criptato come 67 02 ed df in formato esadecimale.

Un cifrario a flusso in cui il flusso delle chiavi si aggiorna indipendentemente dal messaggio in chiaro o dal crittogramma è un **cifrario a flusso sincrono**. Il flusso delle chiavi dipende solo dalla chiave. Chiaramente, RC4 è un esempio di cifrario a flusso sincrono, poiché il flusso delle chiavi non ha alcuna relazione con il messaggio in chiaro o con il crittogramma. Tutti i nostri cifrari a flusso primitivi menzionati nel capitolo precedente, inclusi il cifrario di Cesare, il cifrario di Vigenère e il one-time pad, erano anch'essi di tipo sincrono.

Al contrario, un **cifrario a flusso asincrono** ha un flusso delle chiavi che è prodotto sia dalla chiave che dagli elementi precedenti del crittogramma. Questo tipo di cifrario è anche chiamato **cifrario auto-sincronizzante**.

È importante che il flusso delle chiavi prodotto con RC4 sia trattato come un one-time pad, e non si può produrre il flusso delle chiavi esattamente nello stesso modo la volta successiva. Piuttosto che cambiare la chiave ogni volta, la soluzione pratica è combinare la chiave con un **nonce** per produrre il flusso di byte.

## AES con una chiave a 128 bit
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Come menzionato nel capitolo precedente, l'Istituto Nazionale degli Standard e della Tecnologia (NIST) ha tenuto una competizione tra il 1997 e il 2000 per determinare un nuovo standard di crittografia simmetrica. Il cifrario **Rijndael** si è rivelato essere la proposta vincente. Il nome è un gioco di parole sui nomi dei creatori belgi, Vincent Rijmen e Joan Daemen.
Il cifrario Rijndael è un **cifrario a blocchi**, il che significa che esiste un algoritmo di base, che può essere utilizzato con diverse specifiche per lunghezze di chiave e dimensioni di blocco. Puoi, quindi, usarlo con diverse modalità di funzionamento per costruire schemi di crittografia.
Il comitato per la competizione NIST ha adottato una versione ristretta del cifrario Rijndael, ovvero una che richiede dimensioni di blocco di 128 bit e lunghezze di chiave di 128 bit, 192 bit o 256 bit, come parte dello **Standard di Crittografia Avanzato (AES)**. Questa versione ristretta del cifrario Rijndael può anche essere utilizzata sotto molteplici modalità di funzionamento. La specifica per lo standard è ciò che è noto come **Standard di Crittografia Avanzato (AES)**.

Per mostrare come funziona il cifrario Rijndael, il nucleo dell'AES, illustrerò il processo di crittografia con una chiave di 128 bit. La dimensione della chiave ha un impatto sul numero di round tenuti per ogni blocco di crittografia. Per le chiavi di 128 bit, sono richiesti 10 round. Con 192 bit e 256 bit, sarebbero stati necessari rispettivamente 12 e 14 round.

Inoltre, assumerò che l'AES sia utilizzato in **modalità ECB**. Questo rende l'esposizione leggermente più semplice e non ha importanza per l'algoritmo Rijndael. Per essere sicuri, la modalità ECB non è sicura nella pratica perché porta a una crittografia deterministica. La modalità sicura più comunemente utilizzata con l'AES è **CBC** (Cipher Block Chaining).

Chiamiamo la chiave $K_0$. La costruzione con i parametri sopra indicati, quindi, appare come in *Figura 1*, dove $M_i$ rappresenta una parte del messaggio in chiaro di 128 bit e $C_i$ una parte del testo cifrato di 128 bit. Un padding viene aggiunto al messaggio in chiaro per l'ultimo blocco, se il messaggio in chiaro non può essere diviso equamente per la dimensione del blocco.

*Figura 1: AES-ECB con una chiave di 128 bit*

![Figura 1: AES-ECB con una chiave di 128 bit](assets/Figure5-1.webp "Figura 1: AES-ECB con una chiave di 128 bit")

Ogni blocco di testo di 128 bit passa attraverso dieci round nello schema di crittografia Rijndael. Questo richiede una chiave di round separata per ogni round ($K_1$ fino a $K_{10}$). Queste vengono prodotte per ogni round dalla chiave originale di 128 bit $K_0$ utilizzando un **algoritmo di espansione della chiave**. Quindi, per ogni blocco di testo da crittografare, useremo la chiave originale $K_0$ così come dieci chiavi di round separate. Nota che queste stesse 11 chiavi vengono utilizzate per ogni blocco di testo in chiaro di 128 bit che richiede la crittografia.

L'algoritmo di espansione della chiave è lungo e complesso. Approfondirlo ha poco beneficio didattico. Puoi esaminare l'algoritmo di espansione della chiave da solo, se lo desideri. Una volta prodotte le chiavi di round, il cifrario Rijndael manipolerà il primo blocco di testo in chiaro di 128 bit, $M_1$, come visto in *Figura 2*. Ora passeremo attraverso questi passaggi.

*Figura 2: La manipolazione di $M_1$ con il cifrario Rijndael:*

**Round 0:**
- XOR tra $M_1$ e $K_0$ per produrre $S_0$

---

**Round n per n = {1,...,9}:**
- XOR tra $S_{n-1}$ e $K_n$
- Sostituzione dei Byte
- Scambio di Righe
- Mescolamento delle Colonne
- XOR tra $S$ e $K_n$ per produrre $S_n$

---

**Round 10:**
- XOR $S_9$ e $K_{10}$ - Sostituzione Byte
- Sposta Righe
- XOR $S$ e $K_{10}$ per produrre $S_{10}$
- $S_{10}$ = $C_1$

### Round 0

Il round 0 del cifrario di Rijndael è semplice. Un array $S_0$ viene prodotto da un'operazione XOR tra il testo in chiaro a 128 bit e la chiave privata. Ovvero,

- $S_0 = M_1 \oplus K_0$

### Round 1

Nel round 1, l'array $S_0$ viene prima combinato con la chiave del round $K_1$ usando un'operazione XOR. Questo produce un nuovo stato di $S$.

In secondo luogo, viene eseguita l'operazione di **sostituzione byte** sullo stato corrente di $S$. Funziona prendendo ogni byte dell'array $S$ di 16 byte e sostituendolo con un byte da un array chiamato **S-box di Rijndael**. Ogni byte ha una trasformazione unica, e come risultato viene prodotto un nuovo stato di $S$. La S-box di Rijndael è mostrata in *Figura 3*.

*Figura 3: S-Box di Rijndael*

|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
Il testo fornito sembra essere una sequenza di byte espressi in esadecimale, comunemente utilizzata in contesti di programmazione, crittografia, o analisi di dati a basso livello. Questo tipo di contenuto mantiene il suo significato e utilità solo se presentato nella sua forma originale, quindi non richiede una traduzione nel senso convenzionale. La sequenza di byte deve essere lasciata inalterata per preservare la sua integrità e utilità tecnica.
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |

Questa S-Box è uno dei punti in cui l'algebra astratta entra in gioco nel cifrario Rijndael, specificamente nei **campi di Galois**.

Per iniziare, si definisce ogni possibile elemento byte da 00 a FF come un vettore a 8 bit. Ogni vettore è un elemento del **campo di Galois GF(2^8)** dove il polinomio irriducibile per l'operazione modulo è $x^8 + x^4 + x^3 + x + 1$. Il campo di Galois con queste specifiche è anche chiamato **Campo Finito di Rijndael**.

Successivamente, per ogni possibile elemento nel campo, creiamo quello che viene chiamato la **Nyberg S-Box**. In questa box, ogni byte è mappato sul suo **inverso moltiplicativo** (cioè, in modo che il loro prodotto sia uguale a 1). Mappiamo poi questi valori dalla S-box di Nyberg alla S-Box di Rijndael usando la **trasformazione affine**.

La terza operazione sull'array **S** è l'operazione di **shift rows**. Prende lo stato di **S** ed elenca tutti i sedici byte in una matrice. Il riempimento della matrice inizia in alto a sinistra e procede in giro andando dall'alto verso il basso e poi, ogni volta che una colonna è riempita, spostandosi di una colonna a destra e verso l'alto.

Una volta che la matrice di **S** è stata costruita, le quattro righe vengono spostate. La prima riga rimane uguale. La seconda riga si muove di uno verso sinistra. La terza si muove di due verso sinistra. La quarta si muove di tre verso sinistra. Un esempio del processo è fornito nella *Figura 4*. Lo stato originale di **S** è mostrato in alto, e lo stato risultante dopo l'operazione di shift rows è mostrato sotto.

*Figura 4: Operazione di shift rows*

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |

Nel quarto passo, i **campi di Galois** fanno nuovamente la loro comparsa. Per iniziare, ogni colonna della matrice **S** viene moltiplicata per la colonna della matrice 4 x 4 vista nella *Figura 5*. Ma invece di essere una moltiplicazione di matrici regolare, è una moltiplicazione vettoriale **modulo un polinomio irriducibile**, $x^8 + x^4 + x^3 + x + 1$. I coefficienti vettoriali risultanti rappresentano i singoli bit di un byte.

*Figura 5: Matrice mix columns*

| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
La moltiplicazione della prima colonna della matrice **S** con la matrice 4 x 4 sopra riportata produce il risultato in *Figura 6*.

*Figura 6: Moltiplicazione della prima colonna:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Come passo successivo, tutti i termini nella matrice devono essere trasformati in polinomi. Ad esempio, F1 rappresenta 1 byte e diventerebbe $x^7 + x^6 + x^5 + x^4 + 1$, e 03 rappresenta 1 byte e diventerebbe $x + 1$.

Tutte le moltiplicazioni sono poi eseguite **modulo** $x^8 + x^4 + x^3 + x + 1$. Questo risulta nell'addizione di quattro polinomi in ciascuna delle quattro celle della colonna. Dopo aver eseguito queste addizioni **modulo 2**, si ottengono quattro polinomi. Ognuno di questi polinomi rappresenta una stringa di 8 bit, o 1 byte, di **S**. Non eseguiremo tutti questi calcoli qui sulla matrice in *Figura 6* poiché sono estensivi.

Una volta che la prima colonna è stata elaborata, le altre tre colonne della matrice **S** vengono elaborate nello stesso modo. Alla fine, ciò produrrà una matrice con sedici byte che può essere trasformata in un array.

Come passo finale, l'array **S** viene combinato nuovamente con la chiave di round in un'operazione di **XOR**. Questo produce lo stato $S_1$. Ovvero,

- $S_1 = S \oplus K_0$

### Round dal 2 al 10

I round dal 2 al 9 sono semplicemente una ripetizione del round 1, *mutatis mutandis*. L'ultimo round appare molto simile ai round precedenti, eccetto che il passaggio **mix columns** viene eliminato. Ovvero, il round 10 viene eseguito come segue:

- $S_9 \oplus K_{10}$
- Sostituzione dei Byte
- Shift delle Righe
- $S_{10} = S \oplus K_{10}$

Lo stato $S_{10}$ è ora impostato su $C_1$, i primi 128 bit del testo cifrato. Procedendo attraverso i rimanenti blocchi di testo in chiaro da 128 bit si ottiene l'intero testo cifrato **C**.

### Le operazioni del cifrario di Rijndael

Qual è il ragionamento dietro le diverse operazioni viste nel cifrario di Rijndael?

Senza entrare nei dettagli, gli schemi di cifratura sono valutati sulla base della misura in cui creano confusione e diffusione. Se lo schema di cifratura ha un alto grado di **confusione**, significa che il testo cifrato appare drasticamente diverso rispetto al testo in chiaro. Se lo schema di cifratura ha un alto grado di **diffusione**, significa che qualsiasi piccola modifica al testo in chiaro produce un testo cifrato drasticamente diverso.
Il ragionamento dietro le operazioni del cifrario Rijndael è che producono sia un alto grado di confusione che di diffusione. La confusione è prodotta dall'operazione di sostituzione dei byte, mentre la diffusione è prodotta dalle operazioni di spostamento delle righe e mescolamento delle colonne.

# Crittografia Asimmetrica
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Il problema della distribuzione e gestione delle chiavi
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Come nella crittografia simmetrica, gli schemi asimmetrici possono essere utilizzati per garantire sia la segretezza che l'autenticazione. Tuttavia, a differenza di questi, tali schemi impiegano due chiavi anziché una: una chiave privata e una pubblica.

Iniziamo la nostra indagine con la scoperta della crittografia asimmetrica, in particolare i problemi che l'hanno stimolata. Successivamente, discutiamo come gli schemi asimmetrici per la cifratura e l'autenticazione funzionano ad alto livello. Introduciamo poi le funzioni hash, che sono fondamentali per comprendere gli schemi di autenticazione asimmetrici, e hanno anche rilevanza in altri contesti crittografici, come per i codici di autenticazione dei messaggi basati su hash discussi nel Capitolo 4.

___

Supponiamo che Bob voglia comprare un nuovo impermeabile da Jim’s Sporting Goods, un rivenditore online di articoli sportivi con milioni di clienti in Nord America. Questo sarà il suo primo acquisto da loro e vuole usare la sua carta di credito. Quindi, Bob dovrà prima creare un account con Jim’s Sporting Goods, il che richiede l'invio di dettagli personali come il suo indirizzo e le informazioni della carta di credito. Potrà poi procedere con i passaggi necessari per acquistare l'impermeabile.

Bob e Jim’s Sporting Goods vorranno garantire che le loro comunicazioni siano sicure durante tutto questo processo, considerando che Internet è un sistema di comunicazione aperto. Vorrebbero garantire, ad esempio, che nessun potenziale attaccante possa apprendere i dettagli della carta di credito e dell'indirizzo di Bob, e che nessun potenziale attaccante possa ripetere i suoi acquisti o crearne di falsi per suo conto.

Uno schema avanzato di cifratura autenticata, come discusso nel capitolo precedente, potrebbe certamente rendere sicure le comunicazioni tra Bob e Jim’s Sporting Goods. Ma ci sono chiaramente ostacoli pratici all'implementazione di tale schema.

Per illustrare questi ostacoli pratici, supponiamo di vivere in un mondo in cui esistono solo gli strumenti della crittografia simmetrica. Cosa potrebbero fare Jim’s Sporting Goods e Bob, quindi, per garantire una comunicazione sicura?

In queste circostanze, si troverebbero di fronte a costi sostanziali per comunicare in modo sicuro. Poiché Internet è un sistema di comunicazione aperto, non possono semplicemente scambiarsi un insieme di chiavi su di esso. Quindi, Bob e un rappresentante di Jim’s Sporting Goods dovranno effettuare uno scambio di chiavi di persona.

Una possibilità è che Jim’s Sporting Goods crei delle speciali sedi per lo scambio di chiavi, dove Bob e altri nuovi clienti possono recuperare un insieme di chiavi per una comunicazione sicura. Questo comporterebbe ovviamente costi organizzativi sostanziali e ridurrebbe notevolmente l'efficienza con cui i nuovi clienti possono effettuare acquisti.

In alternativa, Jim’s Sporting Goods può inviare a Bob una coppia di chiavi tramite un corriere di alta fiducia. Questo è probabilmente più efficiente dell'organizzare sedi per lo scambio di chiavi. Ma comporterebbe comunque costi sostanziali, in particolare se molti clienti effettuano solo uno o pochi acquisti.

Inoltre, uno schema simmetrico per la cifratura autenticata costringe anche Jim’s Sporting Goods a conservare set separati di chiavi per tutti i loro clienti. Questa sarebbe una sfida pratica significativa per migliaia di clienti, figuriamoci per milioni.
Per comprendere quest'ultimo punto, supponiamo che Jim’s Sporting Goods fornisca a ciascun cliente la stessa coppia di chiavi. Questo permetterebbe a ogni cliente - o a chiunque altro potesse ottenere questa coppia di chiavi - di leggere e persino manipolare tutte le comunicazioni tra Jim’s Sporting Goods e i suoi clienti. Potresti, quindi, anche non usare affatto la crittografia nelle tue comunicazioni.
Anche ripetere un set di chiavi solo per alcuni clienti è una pessima pratica di sicurezza. Qualsiasi potenziale attaccante potrebbe tentare di sfruttare questa caratteristica del sistema (ricorda che si presume che gli attaccanti conoscano tutto di un sistema tranne le chiavi, in conformità con il principio di Kerckhoffs.)

Quindi, Jim’s Sporting Goods dovrebbe conservare una coppia di chiavi per ogni cliente, indipendentemente da come queste coppie di chiavi vengano distribuite. Questo presenta chiaramente diversi problemi pratici.

- Jim’s Sporting Goods dovrebbe conservare milioni di coppie di chiavi, un set per ogni cliente.
- Queste chiavi dovrebbero essere adeguatamente protette, poiché sarebbero un bersaglio certo per gli hacker. Qualsiasi violazione della sicurezza richiederebbe la ripetizione di costosi scambi di chiavi, sia presso speciali punti di scambio di chiavi sia tramite corriere.
- Qualsiasi cliente di Jim’s Sporting Goods dovrebbe conservare con sicurezza una coppia di chiavi a casa. Si verificheranno perdite e furti, richiedendo una ripetizione degli scambi di chiavi. I clienti dovrebbero anche affrontare questo processo per qualsiasi altro negozio online o altri tipi di entità con cui desiderano comunicare e transigere su Internet.

Queste due principali sfide appena descritte erano preoccupazioni molto fondamentali fino alla fine degli anni '70. Erano conosciute come il **problema della distribuzione delle chiavi** e il **problema della gestione delle chiavi**, rispettivamente.

Questi problemi erano sempre esistiti, ovviamente, e spesso creavano mal di testa in passato. Le forze militari, ad esempio, avrebbero dovuto costantemente distribuire libri con chiavi per la comunicazione sicura al personale sul campo a grandi rischi e costi. Ma questi problemi stavano peggiorando man mano che il mondo si muoveva sempre più verso una comunicazione digitale a lunga distanza, in particolare per le entità non governative.

Se questi problemi non fossero stati risolti negli anni '70, lo shopping efficiente e sicuro presso Jim’s Sporting Goods probabilmente non sarebbe esistito. Infatti, gran parte del nostro mondo moderno con e-mail pratiche e sicure, banking online e shopping probabilmente sarebbe stato solo un lontano sogno. Qualcosa che assomigliasse anche lontanamente a Bitcoin non avrebbe potuto esistere affatto.

Quindi, cosa è successo negli anni '70? Come è possibile che possiamo fare acquisti online all'istante e navigare in modo sicuro sul World Wide Web? Come è possibile che possiamo inviare istantaneamente Bitcoin in tutto il mondo dai nostri smartphone?

## Nuove direzioni nella crittografia
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

Negli anni '70, i problemi della distribuzione delle chiavi e della gestione delle chiavi avevano attirato l'attenzione di un gruppo di crittografi accademici americani: Whitfield Diffie, Martin Hellman e Ralph Merkle. Di fronte allo scetticismo severo della maggior parte dei loro colleghi, si avventurarono a ideare una soluzione.

Almeno una delle principali motivazioni per la loro impresa era la previsione che le comunicazioni informatiche aperte avrebbero profondamente influenzato il nostro mondo. Come Diffie e Hellman notano nel 1976,
Lo sviluppo di reti di comunicazione controllate da computer promette un contatto senza sforzo e a basso costo tra persone o computer situati ai lati opposti del mondo, sostituendo la maggior parte della corrispondenza cartacea e molte trasferte con le telecomunicazioni. Per molte applicazioni, questi contatti devono essere resi sicuri sia contro l'intercettazione sia contro l'iniezione di messaggi illegittimi. Attualmente, tuttavia, la soluzione dei problemi di sicurezza è molto indietro rispetto ad altre aree della tecnologia delle comunicazioni. *La crittografia contemporanea non è in grado di soddisfare i requisiti, in quanto il suo utilizzo imporrebbe agli utenti del sistema inconvenienti così gravi da eliminare molti dei benefici del teleprocessing.* [1]

La tenacia di Diffie, Hellman e Merkle ha dato i suoi frutti. La prima pubblicazione dei loro risultati fu un articolo di Diffie e Hellman nel 1976 intitolato “New Directions in Cryptography”. In esso, presentarono due modi originali per affrontare i problemi della distribuzione delle chiavi e della gestione delle chiavi.

La prima soluzione che offrirono fu un *protocollo di scambio chiavi a distanza*, ovvero, un insieme di regole per lo scambio di una o più chiavi simmetriche attraverso un canale di comunicazione non sicuro. Questo protocollo è ora conosciuto come *scambio di chiavi Diffie-Hellman* o *scambio di chiavi Diffie-Hellman-Merkle*. [2]

Con lo scambio di chiavi Diffie-Hellman, due parti scambiano prima alcune informazioni pubblicamente su un canale insicuro come Internet. Sulla base di queste informazioni, poi, creano indipendentemente una chiave simmetrica (o una coppia di chiavi simmetriche) per la comunicazione sicura. Sebbene entrambe le parti creino le loro chiavi indipendentemente, le informazioni che hanno condiviso pubblicamente assicurano che questo processo di creazione della chiave produca lo stesso risultato per entrambi.

Importante è che, mentre tutti possono osservare le informazioni che vengono scambiate pubblicamente dalle parti sul canale insicuro, solo le due parti coinvolte nello scambio di informazioni possono creare chiavi simmetriche da esse.

Questo, ovviamente, sembra completamente controintuitivo. Come possono due parti scambiare alcune informazioni pubblicamente che permetteranno solo a loro di creare chiavi simmetriche da esse? Perché chiunque altro che osserva lo scambio di informazioni non sarebbe in grado di creare le stesse chiavi?

Si basa su alcune bellissime matematiche, ovviamente. Lo scambio di chiavi Diffie-Hellman funziona tramite una funzione unidirezionale con una botola. Discutiamo il significato di questi due termini a turno.

Supponiamo che ti venga data una certa funzione $f(x)$ e il risultato $f(a) = y$, dove $a$ è un valore particolare per $x$. Diciamo che $f(x)$ è una **funzione unidirezionale** se è facile calcolare il valore $y$ quando sono dati $a$ e $f(x)$, ma è computazionalmente impraticabile calcolare il valore $a$ quando sono dati $y$ e $f(x)$. Il nome **funzione unidirezionale**, ovviamente, deriva dal fatto che tale funzione è pratica da calcolare solo in una direzione.

Alcune funzioni unidirezionali hanno quello che è noto come una **botola**. Mentre è praticamente impossibile calcolare $a$ avendo solo $y$ e $f(x)$, esiste un certo pezzo di informazione $Z$ che rende computazionalmente fattibile calcolare $a$ da $y$. Questo pezzo di informazione $Z$ è conosciuto come la **botola**. Le funzioni unidirezionali che hanno una botola sono note come **funzioni con botola**.
Non approfondiremo i dettagli dello scambio di chiavi Diffie-Hellman qui. Ma essenzialmente, ogni partecipante crea delle informazioni, di cui una parte viene condivisa pubblicamente e una parte rimane segreta. Ogni parte, quindi, prende il proprio pezzo di informazione segreta e l'informazione pubblica condivisa dall'altra parte per creare una chiave privata. E, in modo alquanto miracoloso, entrambe le parti finiscono per avere la stessa chiave privata. 
Qualsiasi parte che osserva solo le informazioni condivise pubblicamente tra le due parti in uno scambio di chiavi Diffie-Hellman non è in grado di replicare questi calcoli. Avrebbero bisogno delle informazioni private di una delle due parti per farlo.

Sebbene la versione base dello scambio di chiavi Diffie-Hellman presentata nel documento del 1976 non sia molto sicura, versioni sofisticate del protocollo di base sono certamente ancora in uso oggi. Più importantemente, ogni protocollo di scambio di chiavi nell'ultima versione del protocollo di sicurezza del livello di trasporto (versione 1.3) è essenzialmente una versione arricchita del protocollo presentato da Diffie e Hellman nel 1976. Il protocollo di sicurezza del livello di trasporto è il protocollo predominante per lo scambio sicuro di informazioni formattate secondo il protocollo di trasferimento ipertestuale (http), lo standard per lo scambio di contenuti Web.

Importante, lo scambio di chiavi Diffie-Hellman non è uno schema asimmetrico. Parlando in modo rigoroso, appartiene probabilmente al regno della crittografia a chiave simmetrica. Ma poiché sia lo scambio di chiavi Diffie-Hellman sia la crittografia asimmetrica si affidano a funzioni numeriche unidirezionali con trappole, di solito vengono discussi insieme.

Il secondo modo proposto da Diffie e Hellman per affrontare il problema della distribuzione e gestione delle chiavi nel loro documento del 1976 era, naturalmente, tramite la crittografia asimmetrica.

A differenza della loro presentazione dello scambio di chiavi Diffie-Hellman, hanno fornito solo i contorni generali di come potrebbero essere plausibilmente costruiti schemi crittografici asimmetrici. Non hanno offerto alcuna funzione unidirezionale che potesse specificamente soddisfare le condizioni necessarie per una sicurezza ragionevole in tali schemi.

Tuttavia, un'implementazione pratica di uno schema asimmetrico fu trovata un anno dopo da tre diversi crittografi e matematici accademici: Ronald Rivest, Adi Shamir e Leonard Adleman. Il sistema crittografico che hanno introdotto è diventato noto come **sistema crittografico RSA** (dalle loro iniziali).

Le funzioni con trappola utilizzate nella crittografia asimmetrica (e nello scambio di chiavi Diffie-Hellman) sono tutte correlate a due principali **problemi computazionalmente difficili**: la fattorizzazione di numeri primi e il calcolo dei logaritmi discreti.

La **fattorizzazione di numeri primi** richiede, come suggerisce il nome, di scomporre un intero nei suoi fattori primi. Il problema RSA è di gran lunga l'esempio più noto di un sistema crittografico relativo alla fattorizzazione di numeri primi.

Il **problema del logaritmo discreto** è un problema che si verifica nei gruppi ciclici. Dato un generatore in un particolare gruppo ciclico, richiede il calcolo dell'esponente unico necessario per produrre un altro elemento nel gruppo dal generatore.

Gli schemi basati sul logaritmo discreto si affidano a due principali tipi di gruppi ciclici: gruppi moltiplicativi di interi e gruppi che includono i punti sulle curve ellittiche. Lo scambio di chiavi Diffie-Hellman originale presentato in "New Directions in Cryptography" funziona con un gruppo moltiplicativo ciclico di interi. L'algoritmo di firma digitale di Bitcoin e il recentemente introdotto schema di firma Schnorr (2021) si basano entrambi sul problema del logaritmo discreto per un particolare gruppo ciclico di curve ellittiche.

Successivamente, passeremo a una panoramica ad alto livello della segretezza e dell'autenticazione nell'ambito asimmetrico. Prima di farlo, tuttavia, dobbiamo fare una breve nota storica.
Ora sembra plausibile che un gruppo di crittografi e matematici britannici che lavoravano per il Government Communications Headquarters (GCHQ) avesse fatto indipendentemente le scoperte menzionate sopra alcuni anni prima. Questo gruppo era composto da James Ellis, Clifford Cocks e Malcolm Williamson.

Secondo i loro racconti e quello del GCHQ, fu James Ellis a ideare per primo il concetto di crittografia a chiave pubblica nel 1969. Presumibilmente, Clifford Cocks scoprì poi il sistema crittografico RSA nel 1973, e Malcolm Williamson il concetto di scambio di chiavi Diffie-Hellman nel 1974. [4] Tuttavia, si sostiene che le loro scoperte non furono rivelate fino al 1997, data la natura segreta del lavoro svolto al GCHQ.

**Note:**

[1] Whitfield Diffie e Martin Hellman, “Nuove direzioni nella crittografia,” _IEEE Transactions on Information Theory_ IT-22 (1976), pp. 644–654, a p. 644.

[2] Ralph Merkle discute anche di un protocollo di scambio di chiavi in “Comunicazioni sicure su canali insicuri”, _Communications of the Association for Computing Machinery_, 21 (1978), 294–99. Sebbene Merkle avesse effettivamente inviato questo articolo prima del lavoro di Diffie e Hellman, fu pubblicato più tardi. La soluzione di Merkle non è esponenzialmente sicura, a differenza di quella di Diffie-Hellman.

[3] Ron Rivest, Adi Shamir e Leonard Adleman, “Un metodo per ottenere firme digitali e sistemi di crittografia a chiave pubblica”, _Communications of the Association for Computing Machinery_, 21 (1978), pp. 120–26.

[4] Una buona storia di queste scoperte è fornita da Simon Singh, _The Code Book_, Fourth Estate (Londra, 1999), Capitolo 6.

## Crittografia asimmetrica e autenticazione
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Viene fornita una panoramica della **crittografia asimmetrica** con l'aiuto di Bob e Alice in *Figura 1*.

Alice crea prima una coppia di chiavi, consistente in una chiave pubblica ($K_P$) e una chiave privata ($K_S$), dove il “P” in $K_P$ sta per “pubblica” e il “S” in $K_S$ per “segreta”. Poi distribuisce liberamente questa chiave pubblica agli altri. Torneremo più tardi sui dettagli di questo processo di distribuzione. Ma per ora, assumiamo che chiunque, incluso Bob, possa ottenere in modo sicuro la chiave pubblica di Alice $K_P$.

In un momento successivo, Bob vuole scrivere un messaggio $M$ ad Alice. Poiché include informazioni sensibili, vuole che il contenuto rimanga segreto per tutti tranne che per Alice. Quindi, Bob prima cripta il suo messaggio $M$ usando $K_P$. Poi invia il testo cifrato risultante $C$ ad Alice, che decripta $C$ con $K_S$ per produrre il messaggio originale $M$.

*Figura 1: Crittografia asimmetrica*

![Figura 1: Crittografia asimmetrica](assets/Figure6-1.webp "Figura 1: Crittografia asimmetrica")

Qualsiasi avversario che ascolti la comunicazione tra Bob e Alice può osservare $C$. Conosce anche $K_P$ e l'algoritmo di crittografia $E(\cdot)$. Importante, tuttavia, queste informazioni non permettono all'attaccante di decriptare in modo fattibile il testo cifrato $C$. La decriptazione richiede specificamente $K_S$, che l'attaccante non possiede.
Gli schemi di crittografia simmetrica generalmente devono essere sicuri contro un attaccante che può validamente criptare messaggi in chiaro (noto come sicurezza contro attacchi con testo cifrato scelto). Tuttavia, non sono progettati con lo scopo esplicito di permettere la creazione di tali testi cifrati validi da parte di un attaccante o di chiunque altro.
Questo è in netto contrasto con uno schema di crittografia asimmetrica, il cui scopo principale è permettere a chiunque, inclusi gli attaccanti, di produrre testi cifrati validi. Gli schemi di crittografia asimmetrica possono, quindi, essere etichettati come **cifrari ad accesso multiplo**.

Per capire meglio cosa sta succedendo, immaginate che invece di inviare un messaggio elettronicamente, Bob volesse inviare una lettera fisica in segreto. Un modo per garantire la segretezza sarebbe per Alice inviare un lucchetto sicuro a Bob, ma tenere la chiave per aprirlo. Dopo aver scritto la sua lettera, Bob potrebbe mettere la lettera in una scatola e chiuderla con il lucchetto di Alice. Potrebbe quindi inviare la scatola chiusa con il messaggio ad Alice che ha la chiave per aprirla.

Mentre Bob è in grado di chiudere il lucchetto, né lui né alcun'altra persona che intercetta la scatola possono aprire il lucchetto se questo è davvero sicuro. Solo Alice può aprirlo e vedere il contenuto della lettera di Bob perché lei ha la chiave.

Uno schema di crittografia asimmetrica è, grossomodo, una versione digitale di questo processo. Il lucchetto è paragonabile alla chiave pubblica e la chiave del lucchetto è paragonabile alla chiave privata. Poiché il lucchetto è digitale, tuttavia, è molto più facile e meno costoso per Alice distribuirlo a chiunque potrebbe voler inviare messaggi segreti a lei.

Per l'autenticazione nell'ambito asimmetrico, usiamo le **firme digitali**. Queste, quindi, hanno la stessa funzione dei codici di autenticazione dei messaggi nell'ambito simmetrico. Una panoramica delle firme digitali è fornita in *Figura 2*.

Bob crea prima una coppia di chiavi, consistente nella chiave pubblica ($K_P$) e nella chiave privata ($K_S$), e distribuisce la sua chiave pubblica. Quando vuole inviare un messaggio autenticato ad Alice, prende prima il suo messaggio $M$ e la sua chiave privata per creare una **firma digitale** $D$. Bob poi invia ad Alice il suo messaggio insieme alla firma digitale.

Alice inserisce il messaggio, la chiave pubblica e la firma digitale in un **algoritmo di verifica**. Questo algoritmo produce o **vero** per una firma valida, o **falso** per una firma non valida.

Una firma digitale è, come il nome chiaramente implica, l'equivalente digitale di una firma scritta su lettere, contratti e così via. Infatti, una firma digitale è solitamente molto più sicura. Con un certo sforzo, puoi falsificare una firma scritta; un processo reso più facile dal fatto che le firme scritte non sono frequentemente verificate attentamente. Una firma digitale sicura, tuttavia, è, proprio come un codice di autenticazione dei messaggi sicuro, **inforgeabile esistenzialmente**: ciò significa che, con uno schema di firma digitale sicuro, nessuno può realisticamente creare una firma per un messaggio che superi la procedura di verifica, a meno che non disponga della chiave privata.

*Figura 2: Autenticazione asimmetrica*

![Figura 2: Autenticazione asimmetrica](assets/Figure6-2.webp "Figura 2: Autenticazione asimmetrica")

Come con la crittografia asimmetrica, vediamo un interessante contrasto tra le firme digitali e i codici di autenticazione dei messaggi. Per questi ultimi, l'algoritmo di verifica può essere impiegato solo da una delle parti a conoscenza della comunicazione sicura. Questo perché richiede una chiave privata. Nell'ambito asimmetrico, tuttavia, chiunque può verificare una firma digitale $S$ fatta da Bob.
Tutto ciò rende le firme digitali uno strumento estremamente potente. Esse costituiscono la base, ad esempio, per la creazione di firme su contratti che possono essere verificati a fini legali. Se Bob avesse apposto una firma su un contratto nello scambio sopra menzionato, Alice può mostrare il messaggio $M$, il contratto e la firma $S$ a un tribunale. Il tribunale può, quindi, verificare la firma utilizzando la chiave pubblica di Bob. [5]

Per un altro esempio, le firme digitali sono un aspetto importante della distribuzione sicura di software e aggiornamenti software. Questo tipo di verificabilità pubblica non potrebbe mai essere creato usando solo codici di autenticazione dei messaggi.

Come ultimo esempio del potere delle firme digitali, consideriamo Bitcoin. Uno dei malintesi più comuni su Bitcoin, specialmente nei media, è che le transazioni siano criptate: non lo sono. Invece, le transazioni Bitcoin lavorano con firme digitali per garantire la sicurezza.

I Bitcoin esistono in lotti chiamati output di transazione non spesi (o **UTXO**). Supponiamo che tu riceva tre pagamenti su un particolare indirizzo Bitcoin per 2 bitcoin ciascuno. Tecnicamente non hai ora 6 bitcoin su quell'indirizzo. Invece, hai tre lotti di 2 bitcoin che sono bloccati da un problema crittografico associato a quell'indirizzo. Per qualsiasi pagamento che fai, puoi usare uno, due o tutti e tre questi lotti, a seconda di quanto ti serve per la transazione.

La prova di proprietà sugli output di transazione non spesi è solitamente mostrata tramite una o più firme digitali. Bitcoin funziona precisamente perché le firme digitali valide sugli output di transazione non spesi sono computazionalmente impossibili da realizzare, a meno che non si sia in possesso delle informazioni segrete necessarie per farle.

Attualmente, le transazioni Bitcoin includono trasparentemente tutte le informazioni che devono essere verificate dai partecipanti nella rete, come le origini degli output di transazione non spesi utilizzati nella transazione. Sebbene sia possibile nascondere alcune di queste informazioni e comunque permettere la verifica (come fanno alcune criptovalute alternative come Monero), ciò crea anche particolari rischi per la sicurezza.

A volte si crea confusione tra le firme digitali e le firme scritte catturate digitalmente. In quest'ultimo caso, si cattura un'immagine della propria firma scritta e la si incolla su un documento elettronico come un contratto di lavoro. Questo, tuttavia, non è una firma digitale nel senso crittografico. Quest'ultima è solo un lungo numero che può essere prodotto solo essendo in possesso di una chiave privata.

Così come nell'impostazione a chiave simmetrica, è possibile utilizzare anche schemi di crittografia asimmetrica e di autenticazione insieme. Si applicano principi simili. Prima di tutto, si dovrebbero usare coppie di chiavi private-pubbliche diverse per la crittografia e per fare firme digitali. Inoltre, si dovrebbe prima criptare un messaggio e poi autenticarlo.

Importante, in molte applicazioni la crittografia asimmetrica non viene utilizzata per tutto il processo di comunicazione. Invece, sarà tipicamente usata solo per *scambiare chiavi simmetriche* tra le parti con cui effettivamente comunicheranno.

Questo è il caso, ad esempio, quando si acquistano beni online. Conoscendo la chiave pubblica del venditore, lei può inviarti messaggi firmati digitalmente che puoi verificare per la loro autenticità. Su questa base, puoi seguire uno dei molti protocolli per lo scambio di chiavi simmetriche per comunicare in modo sicuro.

Il motivo principale della frequenza del suddetto approccio è che la crittografia asimmetrica è molto meno efficiente della crittografia simmetrica nel produrre un determinato livello di sicurezza. Questo è uno dei motivi per cui abbiamo ancora bisogno della crittografia a chiave simmetrica accanto alla crittografia pubblica. Inoltre, la crittografia a chiave simmetrica è molto più naturale in applicazioni particolari come un utente di computer che cripta i propri dati.

Quindi, come esattamente le firme digitali e la crittografia a chiave pubblica affrontano i problemi di distribuzione e gestione delle chiavi?
Non esiste una risposta unica qui. La crittografia asimmetrica è uno strumento e non esiste un unico modo per impiegare tale strumento. Ma prendiamo il nostro esempio precedente di Jim’s Sporting Goods per mostrare come i problemi sarebbero tipicamente affrontati in questo esempio.
Per iniziare, Jim’s Sporting Goods si rivolgerebbe probabilmente a un'autorità di certificazione, un'organizzazione che supporta la distribuzione delle chiavi pubbliche. L'autorità di certificazione registrerebbe alcuni dettagli su Jim’s Sporting Goods e gli concederebbe una chiave pubblica. Quindi, invierebbe a Jim’s Sporting Goods un certificato, noto come certificato TLS/SSL, con la chiave pubblica di Jim’s Sporting Goods firmata digitalmente utilizzando la propria chiave pubblica dell'autorità di certificazione. In questo modo, l'autorità di certificazione afferma che una particolare chiave pubblica appartiene effettivamente a Jim’s Sporting Goods.

La chiave per comprendere questo processo con i certificati TLS/SSL è che, mentre generalmente non avrai la chiave pubblica di Jim’s Sporting Goods memorizzata da nessuna parte sul tuo computer, le chiavi pubbliche delle autorità di certificazione riconosciute sono effettivamente memorizzate nel tuo browser o nel tuo sistema operativo. Queste sono memorizzate in quello che vengono chiamati **certificati radice**.

Pertanto, quando Jim’s Sporting Goods ti fornisce il suo certificato TLS/SSL, puoi verificare la firma digitale dell'autorità di certificazione tramite un certificato radice nel tuo browser o sistema operativo. Se la firma è valida, puoi essere relativamente sicuro che la chiave pubblica sul certificato appartenga effettivamente a Jim’s Sporting Goods. Su questa base, è facile impostare un protocollo per una comunicazione sicura con Jim’s Sporting Goods.

La distribuzione delle chiavi è ora diventata notevolmente più semplice per Jim’s Sporting Goods. Non è difficile vedere che anche la gestione delle chiavi è diventata notevolmente semplificata. Invece di dover memorizzare migliaia di chiavi, Jim’s Sporting Goods deve semplicemente memorizzare una chiave privata che gli consente di fare firme per la chiave pubblica sul suo certificato SSL. Ogni volta che un cliente visita il sito di Jim’s Sporting Goods, può stabilire una sessione di comunicazione sicura da questa chiave pubblica. Anche i clienti non hanno bisogno di memorizzare alcuna informazione (a parte le chiavi pubbliche delle autorità di certificazione riconosciute nel loro sistema operativo e browser).

**Note:**

[5] Qualsiasi schema che tenta di ottenere la non ripudiabilità, l'altro tema discusso nel Capitolo 1, dovrà alla sua base coinvolgere firme digitali.

## Funzioni hash
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Le funzioni hash sono onnipresenti nella crittografia. Non sono né schemi simmetrici né asimmetrici, ma rientrano in una categoria crittografica a sé stante.

Abbiamo già incontrato le funzioni hash nel Capitolo 4 con la creazione di messaggi di autenticazione basati su hash. Sono anche importanti nel contesto delle firme digitali, sebbene per un motivo leggermente diverso: le firme digitali sono tipicamente realizzate sul valore hash di un messaggio (criptato), piuttosto che sul messaggio (criptato) effettivo. In questa sezione, offrirò un'introduzione più approfondita alle funzioni hash.

Iniziamo con la definizione di una funzione hash. Una **funzione hash** è qualsiasi funzione facilmente calcolabile che prende input di dimensione arbitraria e produce output di lunghezza fissa.

Una **funzione hash crittografica** è semplicemente una funzione hash che è utile per applicazioni in crittografia. L'output di una funzione hash crittografica è tipicamente chiamato **hash**, **valore hash** o **digest del messaggio**.

Nel contesto della crittografia, una "funzione hash" si riferisce tipicamente a una funzione hash crittografica. Adotterò questa pratica da qui in avanti.
Un esempio di funzione hash popolare è **SHA-256** (secure hash algorithm 256). Indipendentemente dalle dimensioni dell'input (ad esempio, 15 bit, 100 bit o 10.000 bit), questa funzione produrrà un valore hash di 256 bit. Di seguito puoi vedere alcuni esempi di output della funzione SHA-256.
“Hello”: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

“52398”: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

“La crittografia è divertente”: `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Tutti gli output sono esattamente di 256 bit scritti in formato esadecimale (ogni cifra esadecimale può essere rappresentata da quattro cifre binarie). Quindi, anche se avessi inserito il libro *Il Signore degli Anelli* di Tolkien nella funzione SHA-256, l'output sarebbe comunque di 256 bit.

Le funzioni hash come SHA-256 sono impiegate per vari scopi nella crittografia. Le proprietà richieste da una funzione hash dipendono davvero dal contesto di una particolare applicazione. Ci sono due proprietà generalmente desiderate delle funzioni hash nella crittografia: [6]

1.	Resistenza alle collisioni
2.	Oscuramento

Si dice che una funzione hash $H$ sia **resistente alle collisioni** se è impraticabile trovare due valori, $x$ e $y$, tali che $x \neq y$, eppure $H(x) = H(y)$.

Le funzioni hash resistenti alle collisioni sono importanti, ad esempio, nella verifica del software. Supponiamo che tu voglia scaricare la versione Windows di Bitcoin Core 0.21.0 (un'applicazione server per elaborare il traffico della rete Bitcoin). I passaggi principali che dovresti compiere, per verificare la legittimità del software, sono i seguenti:

1.	Prima di tutto, devi scaricare e importare le chiavi pubbliche di uno o più contributori di Bitcoin Core in un software che possa verificare le firme digitali (ad esempio, Kleopetra). Puoi trovare queste chiavi pubbliche [qui](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Si raccomanda di verificare il software Bitcoin Core con le chiavi pubbliche di più contributori.
2.	Successivamente, devi verificare le chiavi pubbliche che hai importato. Almeno un passaggio che dovresti compiere è verificare che le chiavi pubbliche trovate siano le stesse pubblicate in varie altre località. Potresti, ad esempio, consultare le pagine web personali, le pagine Twitter o le pagine Github delle persone le cui chiavi pubbliche hai importato. Tipicamente, questo confronto delle chiavi pubbliche viene fatto confrontando un breve hash della chiave pubblica noto come impronta digitale.
3.	Poi, devi scaricare l'eseguibile per Bitcoin Core dal loro [sito web](www.bitcoincore.org). Saranno disponibili pacchetti per i sistemi operativi Linux, Windows e MAC.
4.	Successivamente, devi localizzare due file di rilascio. Il primo contiene l'hash SHA-256 ufficiale per l'eseguibile che hai scaricato insieme agli hash di tutti gli altri pacchetti che sono stati rilasciati. Un altro file di rilascio conterrà le firme di vari contributori sul file di rilascio con gli hash dei pacchetti. Entrambi questi file di rilascio dovrebbero essere situati sul sito web di Bitcoin Core.
5. Successivamente, dovrai calcolare l'hash SHA-256 dell'eseguibile che hai scaricato dal sito web di Bitcoin Core sul tuo computer. Poi, confronta questo risultato con quello dell'hash ufficiale del pacchetto per l'eseguibile. Dovrebbero essere uguali.

6. Infine, dovrai verificare che una o più delle firme digitali sul file di rilascio con gli hash ufficiali del pacchetto corrispondano effettivamente a una o più chiavi pubbliche che hai importato (i rilasci di Bitcoin Core non sono sempre firmati da tutti). Puoi farlo con un'applicazione come Kleopetra.

Questo processo di verifica del software ha due benefici principali. Primo, assicura che non ci siano stati errori nella trasmissione durante il download dal sito web di Bitcoin Core. Secondo, garantisce che nessun attaccante potrebbe averti fatto scaricare codice modificato e malevolo, sia hackerando il sito web di Bitcoin Core sia intercettando il traffico.

Come esattamente il processo di verifica del software sopra descritto protegge da questi problemi?

Se hai verificato con diligenza le chiavi pubbliche che hai importato, allora puoi essere abbastanza sicuro che queste chiavi siano effettivamente loro e non siano state compromesse. Dato che le firme digitali hanno l'inforgevolezza esistenziale, sai che solo questi contributori avrebbero potuto fare una firma digitale sugli hash ufficiali del pacchetto sul file di rilascio.

Supponiamo che le firme sul file di rilascio che hai scaricato siano corrette. Ora puoi confrontare il valore hash che hai calcolato localmente per l'eseguibile Windows che hai scaricato con quello incluso nel file di rilascio correttamente firmato. Come sai, la funzione hash SHA-256 è resistente alle collisioni, quindi una corrispondenza significa che il tuo eseguibile è esattamente lo stesso dell'eseguibile ufficiale.

Passiamo ora alla seconda proprietà comune delle funzioni hash: **l'occultamento**. Si dice che una funzione hash $H$ abbia la proprietà di occultamento se, per qualsiasi $x$ selezionato casualmente da un intervallo molto ampio, è impraticabile trovare $x$ quando è dato solo $H(x)$.

Di seguito, puoi vedere l'output SHA-256 di un messaggio che ho scritto. Per garantire sufficiente casualità, il messaggio includeva una stringa di caratteri generata casualmente alla fine. Dato che SHA-256 ha la proprietà di occultamento, nessuno sarebbe in grado di decifrare questo messaggio.

- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Ma non ti lascerò in sospeso fino a quando SHA-256 diventerà più debole. Il messaggio originale che ho scritto era il seguente:

* “Questo è un messaggio molto casuale, o beh, in qualche modo casuale. Questa parte iniziale non lo è, ma terminerò con alcuni caratteri relativamente casuali per garantire un messaggio molto imprevedibile. XLWz4dVG3BxUWm7zQ9qS”.

Un modo comune in cui le funzioni hash con la proprietà di occultamento sono utilizzate è nella gestione delle password (anche la resistenza alle collisioni è importante per questa applicazione). Qualsiasi servizio online decente basato su account come Facebook o Google non memorizzerà direttamente le tue password per gestire l'accesso al tuo account. Invece, memorizzeranno solo un hash di quella password. Ogni volta che inserisci la tua password su un browser, viene prima calcolato un hash. Solo quell'hash viene inviato al server del fornitore di servizi e confrontato con l'hash memorizzato nel database back-end. La proprietà di occultamento può aiutare a garantire che gli aggressori non possano recuperarla dal valore hash.
La gestione delle password tramite hash funziona solo se gli utenti scelgono effettivamente password difficili. La proprietà di occultamento presuppone che x sia scelto casualmente da un intervallo molto ampio. Selezionare password come "1234", "lapropriapassword" o la data del proprio compleanno non fornirà alcuna reale sicurezza. Esistono lunghe liste di password comuni e dei loro hash che gli attaccanti possono sfruttare se mai ottenessero l'hash della tua password. Questi tipi di attacchi sono noti come **attacchi dizionario**. Se gli attaccanti conoscono alcuni dei tuoi dettagli personali, potrebbero anche tentare alcune ipotesi informate. Pertanto, hai sempre bisogno di password lunghe e sicure (preferibilmente lunghe stringhe casuali da un gestore di password).

A volte un'applicazione potrebbe aver bisogno di una funzione hash che abbia sia resistenza alle collisioni sia occultamento. Ma certamente non sempre. Il processo di verifica del software di cui abbiamo discusso, ad esempio, richiede solo che la funzione hash mostri resistenza alle collisioni, l'occultamento non è importante.

Mentre la resistenza alle collisioni e l'occultamento sono le principali proprietà ricercate delle funzioni hash in crittografia, in certe applicazioni potrebbero essere desiderabili anche altri tipi di proprietà.

**Note:**

[6] La terminologia "occultamento" non è un linguaggio comune, ma è presa specificamente da Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller e Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Capitolo 1.

# Il sistema crittografico RSA
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Il problema della fattorizzazione
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Mentre la crittografia simmetrica è solitamente abbastanza intuitiva per la maggior parte delle persone, questo tipicamente non è il caso della crittografia asimmetrica. Sebbene tu possa essere a tuo agio con la descrizione ad alto livello offerta nelle sezioni precedenti, probabilmente ti stai chiedendo cosa siano precisamente le funzioni unidirezionali e come esattamente vengano utilizzate per costruire schemi asimmetrici.

In questo capitolo, rimuoverò parte del mistero che circonda la crittografia asimmetrica, esaminando più a fondo un esempio specifico, ovvero il sistema crittografico RSA. Nella prima sezione, introdurrò il problema della fattorizzazione su cui si basa il problema RSA. Coprirò poi una serie di risultati chiave della teoria dei numeri. Nell'ultima sezione, metteremo insieme queste informazioni per spiegare il problema RSA e come questo possa essere utilizzato per creare schemi crittografici asimmetrici.

Aggiungere questa profondità alla nostra discussione non è un compito facile. Richiede l'introduzione di parecchi teoremi e proposizioni della teoria dei numeri. Ma non lasciare che la matematica ti dissuada. Lavorare attraverso questa discussione migliorerà significativamente la tua comprensione di ciò che sta alla base della crittografia asimmetrica ed è un investimento utile.

Ora passiamo al problema della fattorizzazione.

___

Ogni volta che moltiplichi due numeri, diciamo $a$ e $b$, ci riferiamo ai numeri $a$ e $b$ come **fattori**, e al risultato come **prodotto**. Tentare di scrivere un numero $N$ nella moltiplicazione di due o più fattori è chiamato **fattorizzazione**. [1] Puoi chiamare qualsiasi problema che richiede questo un **problema di fattorizzazione**.

Circa 2.500 anni fa, il matematico greco Euclide di Alessandria scoprì un teorema chiave sulla fattorizzazione degli interi. È comunemente chiamato il **teorema di fattorizzazione unica** e afferma quanto segue:

**Teorema 1**. Ogni intero $N$ maggiore di 1 è o un numero primo, o può essere espresso come un prodotto di fattori primi.
La parte finale di questa affermazione significa semplicemente che è possibile prendere qualsiasi numero intero non primo $N$ maggiore di 1 e scriverlo come una moltiplicazione di numeri primi. Di seguito sono riportati diversi esempi di interi non primi scritti come prodotto di fattori primi.
* $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
* $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
* $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

Per tutti e tre gli interi sopra menzionati, calcolare i loro fattori primi è relativamente facile, anche se si conosce solo $N$. Si inizia con il più piccolo numero primo, ovvero 2, e si verifica quante volte l'intero $N$ è divisibile per esso. Si procede poi testando la divisibilità di $N$ per 3, 5, 7 e così via. Si continua questo processo fino a quando il tuo intero $N$ è scritto come il prodotto di soli numeri primi.

Prendiamo, ad esempio, l'intero 84. Qui sotto puoi vedere il processo per determinare i suoi fattori primi. Ad ogni passo, prendiamo il più piccolo fattore primo rimanente (a sinistra) e determiniamo il termine residuo da fattorizzare. Continuiamo fino a quando il termine residuo è anch'esso un numero primo. Ad ogni passo, la fattorizzazione corrente di 84 è visualizzata sulla destra.

* Fattore primo = 2: termine residuo = 42 	($84 = 2 \cdot 42$)
* Fattore primo = 2: termine residuo = 21 	($84 = 2 \cdot 2 \cdot 21$)
* Fattore primo = 3: termine residuo = 7 	($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
* Poiché 7 è un numero primo, il risultato è $2 \cdot 2 \cdot 3 \cdot 7$, ovvero $2^2 \cdot 3 \cdot 7$.

Supponiamo ora che $N$ sia molto grande. Quanto sarebbe difficile ridurre $N$ ai suoi fattori primi?

Questo dipende davvero da $N$. Supponiamo, ad esempio, che $N$ sia 50,450,400. Anche se questo numero sembra intimidatorio, i calcoli non sono così complicati e possono essere facilmente eseguiti a mano. Come sopra, si inizia con 2 e si procede in avanti. Qui sotto, puoi vedere il risultato di questo processo in modo simile a quanto sopra.

* 2: 25,225,200 	($50,450,400 = 2 \cdot 25,225,200$)  
* 2: 12,612,600 	($50,450,400 = 2^2 \cdot 12,612,600$)  
* 2: 6,306,300 	($50,450,400 = 2^3 \cdot 6,306,300$)  
* 2: 3,153,150 	($50,450,400 = 2^4 \cdot 3,153,150$)  
* 2: 1,576,575 	($50,450,400 = 2^5 \cdot 1,576,575$)
Risolvere questo problema a mano richiede del tempo. Un computer, ovviamente, potrebbe fare tutto questo in una frazione di secondo. Infatti, un computer può spesso anche fattorizzare interi estremamente grandi in una frazione di secondo.

Ci sono, tuttavia, alcune eccezioni. Supponiamo che per prima cosa selezioniamo casualmente due numeri primi molto grandi. È tipico etichettarli con $p$ e $q$, e adotterò questa convenzione qui.

Per essere concreti, diciamo che $p$ e $q$ sono entrambi primi di 1024 bit, e che effettivamente richiedono almeno 1024 bit per essere rappresentati (quindi il primo bit deve essere 1). Quindi, ad esempio, 37 non potrebbe essere uno dei numeri primi. Certamente puoi rappresentare 37 con 1024 bit. Ma chiaramente *non hai bisogno* di così tanti bit per rappresentarlo. Puoi rappresentare 37 con una stringa che ha 6 bit o più. (In 6 bit, 37 sarebbe rappresentato come $100101$).

È importante apprezzare quanto siano grandi $p$ e $q$ se selezionati secondo le condizioni sopra. Come esempio, ho selezionato un numero primo casuale che necessita di almeno 1024 bit per la rappresentazione qui sotto.
* 14.752.173.874.503.595.484.930.006.383.670.759.559.764.562.721.397.166.747.289.220.945.457.932.666.751.048.198.854.920.097.085.690.793.755.254.946.188.163.753.506.778.089.706.699.671.722.089.715.624.760.049.594.106.189.662.669.156.149.028.900.805.928.183.585.427.782.974.951.355.515.394.807.209.836.870.484.558.332.897.443.152.653.214.483.870.992.618.171.825.921.582.253.023.974.514.209.142.520.026.807.636.589

Supponiamo ora che, dopo aver selezionato casualmente i numeri primi $p$ e $q$, li moltiplichiamo per ottenere un intero $N$. Quest'ultimo intero, quindi, è un numero di 2048 bit che richiede almeno 2048 bit per la sua rappresentazione. È molto, molto più grande sia di $p$ che di $q$.

Supponiamo di dare solo a un computer $N$ e di chiedergli di trovare i due fattori primi di 1024 bit di $N$. La probabilità che il computer scopra $p$ e $q$ è estremamente piccola. Si può dire che è impossibile a tutti gli effetti pratici. Questo vale anche se si dovesse impiegare un supercomputer o addirittura una rete di supercomputer.

Per iniziare, supponiamo che il computer tenti di risolvere il problema ciclando attraverso numeri di 1024 bit, testando in ogni caso se sono primi e se sono fattori di $N$. L'insieme dei numeri primi da testare è quindi approssimativamente $1.265 \cdot 10^{305}$. [2]

Anche se si prendessero tutti i computer del pianeta e li si facesse tentare di trovare e testare numeri primi di 1024 bit in questo modo, una possibilità su un miliardo di trovare con successo un fattore primo di $N$ richiederebbe un periodo di calcolo molto più lungo dell'età dell'Universo.

Ora, nella pratica, un computer può fare meglio della grezza procedura appena descritta. Esistono diversi algoritmi che il computer può applicare per arrivare a una fattorizzazione più rapidamente. Il punto, tuttavia, è che anche utilizzando questi algoritmi più efficienti, il compito del computer è ancora computazionalmente impraticabile. [3]

Importante, la difficoltà della fattorizzazione nelle condizioni appena descritte si basa sull'assunzione che non esistano algoritmi computazionalmente efficienti per calcolare i fattori primi. Non possiamo effettivamente dimostrare che un algoritmo efficiente non esista. Tuttavia, questa assunzione è molto plausibile: nonostante gli sforzi estensivi che si protraggono da centinaia di anni, non siamo ancora riusciti a trovare un tale algoritmo computazionalmente efficiente.

Pertanto, il problema della fattorizzazione, in determinate circostanze, può plausibilmente essere considerato un problema difficile. Specificamente, quando $p$ e $q$ sono numeri primi molto grandi, il loro prodotto $N$ non è difficile da calcolare; ma la fattorizzazione data solo $N$ è praticamente impossibile.

**Note:**

[1] La fattorizzazione può anche essere importante per lavorare con altri tipi di oggetti matematici oltre ai numeri. Ad esempio, può essere utile fattorizzare espressioni polinomiali come $x^2 - 2x + 1$. Nella nostra discussione, ci concentreremo solo sulla fattorizzazione dei numeri, specificamente degli interi.
[2] Secondo il **teorema dei numeri primi**, il numero di primi minore o uguale a $N$ è approssimativamente $N/\ln(N)$. Questo significa che puoi approssimare il numero di primi di lunghezza 1024 bit con: 
$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...che equivale approssimativamente a $1.265 \times 10^{305}$.

[3] Lo stesso vale per i problemi di logaritmo discreto. Ecco perché le costruzioni asimmetriche lavorano con chiavi molto più grandi rispetto alle costruzioni crittografiche simmetriche.

## Risultati teorici sui numeri
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Sfortunatamente, il problema della fattorizzazione non può essere utilizzato direttamente per gli schemi crittografici asimmetrici. Tuttavia, possiamo utilizzare un problema più complesso ma correlato a questo scopo: il problema RSA.

Per comprendere il problema RSA, dovremo capire una serie di teoremi e proposizioni dalla teoria dei numeri. Questi sono presentati in questa sezione in tre sottosezioni: (1) l'ordine di N, (2) l'invertibilità modulo N, e (3) il teorema di Eulero.

Parte del materiale nelle tre sottosezioni è già stata introdotta nel *Capitolo 3*. Ma qui ripresenterò quel materiale per comodità.

### L'ordine di N

Un intero $a$ è **coprimo** o un **primo relativo** con un intero $N$, se il massimo comune divisore tra loro è 1. Anche se per convenzione 1 non è un numero primo, è un coprimo di ogni intero (come lo è $-1$).

Per esempio, considera il caso in cui $a = 18$ e $N = 37$. Questi sono chiaramente coprimi. Il più grande intero che divide sia 18 che 37 è 1. Al contrario, considera il caso in cui $a = 42$ e $N = 16$. Questi non sono chiaramente coprimi. Entrambi i numeri sono divisibili per 2, che è maggiore di 1.

Possiamo ora definire l'ordine di $N$ come segue. Supponiamo che $N$ sia un intero maggiore di 1. L'**ordine di N** è, quindi, il numero di tutti i coprimi con $N$ tale che per ogni coprimo $a$, valga la seguente condizione: $1 \leq a < N$.

Per esempio, se $N = 12$, allora 1, 5, 7 e 11 sono gli unici coprimi che soddisfano il requisito sopra. Quindi, l'ordine di 12 è uguale a 4.

Supponiamo che $N$ sia un numero primo. Allora ogni intero minore di $N$ ma maggiore o uguale a 1 è coprimo con esso. Questo include tutti gli elementi nel seguente insieme: $\{1,2,3,….,N - 1\}$. Quindi, quando $N$ è primo, l'ordine di $N$ è $N - 1$. Questo è affermato nella proposizione 1, dove $\phi(N)$ denota l'ordine di $N$.

**Proposizione 1**. $\phi(N) = N - 1$ quando $N$ è primo
Supponiamo che $N$ non sia primo. Puoi, quindi, calcolare il suo ordine utilizzando la **funzione Phi di Eulero**. Mentre calcolare l'ordine di un piccolo intero è relativamente semplice, la funzione Phi di Eulero diventa particolarmente importante per gli interi più grandi. La proposizione della funzione Phi di Eulero è enunciata di seguito.
**Teorema 2**. Sia $N = p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, dove l'insieme $\{p_i\}$ consiste in tutti i fattori primi distinti di $N$ e ogni $e_i$ indica quante volte il fattore primo $p_i$ si verifica per $N$. Allora,

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$

**Teorema 2** mostra che una volta scomposto qualsiasi $N$ non primo nei suoi fattori primi distinti, è facile calcolare l'ordine di $N$.

Per esempio, supponiamo che $N = 270$. Questo non è chiaramente un numero primo. Scomponendo $N$ nei suoi fattori primi si ottiene l'espressione: $2 \cdot 3^3 \cdot 5$. Secondo la funzione Phi di Eulero, l'ordine di $N$ è quindi il seguente:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$

Supponiamo poi che $N$ sia il prodotto di due primi, $p$ e $q$. **Teorema 2** sopra, quindi, afferma che l'ordine di $N$ è il seguente:

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

Questo è un risultato chiave per il problema RSA in particolare, ed è enunciato nella **Proposizione 2** di seguito.

**Proposizione 2**. Se $N$ è il prodotto di due primi, $p$ e $q$, l'ordine di $N$ è il prodotto $(p - 1) \cdot (q - 1)$.

Per illustrare, supponiamo che $N = 119$. Questo intero può essere fattorizzato in due primi, precisamente 7 e 17. Quindi, la funzione Phi di Eulero suggerisce che l'ordine di 119 è il seguente:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$

In altre parole, l'intero 119 ha 96 coprimi nell'intervallo da 1 fino a 119. Infatti, questo insieme include tutti gli interi da 1 fino a 119, che non sono multipli né di 7 né di 17.
Da qui in poi, indichiamo l'insieme dei coprimi che determina l'ordine di $N$ come $C_N$. Per il nostro esempio dove $N = 119$, l'insieme $C_{119}$ è troppo grande per essere elencato completamente. Ma alcuni degli elementi sono i seguenti:
$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$

### Invertibilità modulo N

Possiamo dire che un intero $a$ è **invertibile modulo N**, se esiste almeno un intero $b$ tale che $a \cdot b \mod N = 1 \mod N$. Qualsiasi intero $b$ di questo tipo è definito come un **inverso** (o **inverso moltiplicativo**) di $a$ dato il ridimensionamento per modulo $N$.

Supponiamo, per esempio, che $a = 5$ e $N = 11$. Ci sono molti interi per cui puoi moltiplicare 5, in modo che $5 \cdot b \mod 11 = 1 \mod 11$. Considera, per esempio, gli interi 20 e 31. È facile vedere che entrambi questi interi sono inversi di 5 per la riduzione modulo 11.

* $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
* $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Mentre 5 ha molti inversi per la riduzione modulo 11, puoi dimostrare che esiste solo un singolo inverso positivo di 5 che è minore di 11. Infatti, questo non è unico per il nostro particolare esempio, ma è un risultato generale.

**Proposizione 3**. Se l'intero $a$ è invertibile modulo $N$, deve essere vero che esiste esattamente un inverso positivo di $a$ che è minore di $N$. (Quindi, questo inverso unico di $a$ deve provenire dall'insieme $\{1, \dots, N - 1\}$).

Indichiamo l'inverso unico di $a$ dalla **Proposizione 3** come $a^{-1}$. Nel caso in cui $a = 5$ e $N = 11$, puoi vedere che $a^{-1} = 9$, dato che $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Notare che puoi anche ottenere il valore 9 per $a^{-1}$ nel nostro esempio semplicemente riducendo qualsiasi altro inverso di $a$ per modulo 11. Per esempio, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Quindi, ogni volta che un intero $a > N$ è invertibile modulo $N$, allora $a \mod N$ deve essere anch'esso invertibile modulo $N$.

Non è necessariamente vero che un inverso di $a$ esista per la riduzione modulo $N$. Supponiamo, per esempio, che $a = 2$ e $N = 8$. Non esiste un $b$, o un $a^{-1}$ specificamente, tale che $2 \cdot b \mod 8 = 1 \mod 8$. Questo perché qualsiasi valore di $b$ produrrà sempre un multiplo di 2, quindi nessuna divisione per 8 potrà mai produrre un resto che è uguale a 1.
Come possiamo sapere esattamente se un certo intero $a$ ha un inverso per un dato $N$? Come potreste aver notato nell'esempio sopra, il massimo comune divisore tra 2 e 8 è maggiore di 1, precisamente 2. E questo è in realtà illustrativo del seguente risultato generale:
**Proposizione 4**. Un inverso esiste per un intero $a$ dato il modulo di riduzione $N$, e specificamente un unico inverso positivo minore di $N$, se e solo se il massimo comune divisore tra $a$ e $N$ è 1 (cioè, se sono coprimi).

Nel caso in cui $a = 5$ e $N = 11$, abbiamo concluso che $a^{-1} = 9$, dato che $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. È importante notare che il contrario è anche vero. Cioè, quando $a = 9$ e $N = 11$, si verifica che $a^{-1} = 5$.

### Teorema di Eulero

Prima di passare al problema RSA, dobbiamo comprendere un altro teorema fondamentale, ovvero **il teorema di Eulero**. Esso afferma quanto segue:

**Teorema 3**. Supponiamo che due interi $a$ e $N$ siano coprimi. Allora, $a^{\phi(N)} \mod N = 1 \mod N$.

Questo è un risultato notevole, ma un po' confuso all'inizio. Rivolgiamoci a un esempio per capirlo.

Supponiamo che $a = 5$ e $N = 7$. Questi sono effettivamente coprimi come richiede il teorema di Eulero. Sappiamo che l'ordine di 7 è uguale a 6, dato che 7 è un numero primo (vedi **Proposizione 1**).

Quello che il teorema di Eulero ora afferma è che $5^6 \mod 7$ deve essere uguale a $1 \mod 7$. Di seguito i calcoli per mostrare che questo è effettivamente vero.

* $5^6 \mod 7 = 15.625 \mod 7 = 1 \mod N$

L'intero 7 si divide in 15.624 un totale di 2.233 volte. Pertanto, il resto della divisione di 16.625 per 7 è 1.

Successivamente, utilizzando la funzione Phi di Eulero, **Teorema 2**, è possibile derivare la **Proposizione 5** di seguito.

**Proposizione 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ per qualsiasi intero positivo $a$ e $b$.

Non mostreremo perché ciò accade. Ma notate semplicemente che avete già visto prove di questa proposizione dal fatto che $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ quando $p$ e $q$ sono primi, come affermato nella **Proposizione 2**.

Il teorema di Eulero in congiunzione con la **Proposizione 5** ha implicazioni importanti. Vediamo cosa succede, ad esempio, nelle espressioni sottostanti, dove $a$ e $N$ sono coprimi.

* $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
*a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N*
*a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N*

Pertanto, la combinazione del teorema di Eulero e della **Proposizione 5** ci permette di calcolare semplicemente un numero di espressioni. In generale, possiamo riassumere l'intuizione come nella **Proposizione 6**.

**Proposizione 6**. $a^x \mod N = a^{x \mod \phi(N)}$

Ora dobbiamo mettere tutto insieme in un ultimo passaggio complicato.

Così come $N$ ha un ordine $\phi(N)$ che include gli elementi dell'insieme $C_N$, sappiamo che l'intero $\phi(N)$ deve a sua volta avere anche un ordine e un insieme di coprimi. Poniamo $\phi(N) = R$. Allora sappiamo che esiste anche un valore per $\phi(R)$ e un insieme di coprimi $C_R$.

Supponiamo ora di selezionare un intero $e$ dall'insieme $C_R$. Sappiamo dalla **Proposizione 3** che questo intero $e$ ha solo un unico inverso positivo minore di $R$. Cioè, $e$ ha un unico inverso dall'insieme $C_R$. Chiamiamo questo inverso $d$. Data la definizione di un inverso, ciò significa che $e \cdot d = 1 \mod R$.

Possiamo usare questo risultato per fare una dichiarazione sul nostro intero originale $N$. Questo è riassunto nella **Proposizione 7**.

**Proposizione 7**. Supponiamo che $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Allora per qualsiasi elemento $a$ dell'insieme $C_N$ deve essere il caso che $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Ora abbiamo tutti i risultati teorici dei numeri necessari per enunciare chiaramente il problema RSA.

## Il crittosistema RSA
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Siamo ora pronti per enunciare il problema RSA. Supponi di creare un insieme di variabili costituito da $p$, $q$, $N$, $\phi(N)$, $e$, $d$ e $y$. Chiamiamo questo insieme $\Pi$. È creato come segue:

1. Genera due primi casuali $p$ e $q$ della stessa dimensione e calcola il loro prodotto $N$.
2. Calcola l'ordine di $N$, $\phi(N)$, tramite il seguente prodotto: $(p - 1) \cdot (q - 1)$.
3. Seleziona un $e > 2$ tale che sia minore e coprimo rispetto a $\phi(N)$.
4. Calcola $d$ impostando $e \cdot d \mod \phi(N) = 1$.
5. Seleziona un valore casuale $y$ che sia minore e coprimo rispetto a $N$.
Il problema RSA consiste nel trovare un $x$ tale che $x^e = y$, avendo a disposizione solo un sottoinsieme di informazioni riguardo a $\Pi$, nello specifico le variabili $N$, $e$ e $y$. Quando $p$ e $q$ sono molto grandi, tipicamente si raccomanda che siano di dimensione 1024 bit, il problema RSA è considerato difficile. Ora puoi vedere perché ciò è vero alla luce della discussione precedente.

Un modo semplice per calcolare $x$ quando $x^e \mod N = y \mod N$ è semplicemente calcolando $y^d \mod N$. Sappiamo che $y^d \mod N = x \mod N$ attraverso i seguenti calcoli:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

Il problema è che non conosciamo il valore $d$, poiché non è dato nel problema. Pertanto, non possiamo calcolare direttamente $y^d \mod N$ per produrre $x \mod N$.

Potremmo tuttavia essere in grado di calcolare indirettamente $d$ dall'ordine di $N$, $\phi(N)$, poiché sappiamo che $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Ma per ipotesi il problema non fornisce nemmeno un valore per $\phi(N)$.

Infine, l'ordine potrebbe essere calcolato indirettamente con i fattori primi $p$ e $q$, così da poter eventualmente calcolare $d$. Ma per ipotesi, anche i valori $p$ e $q$ non ci sono stati forniti.

Parlando in termini stretti, anche se il problema della fattorizzazione all'interno di un problema RSA è difficile, non possiamo dimostrare che anche il problema RSA sia difficile. Potrebbero infatti esistere altri modi per risolvere il problema RSA che non attraverso la fattorizzazione. Tuttavia, è generalmente accettato e supposto che, se il problema della fattorizzazione all'interno del problema RSA è difficile, allora anche il problema RSA stesso è difficile.

Se il problema RSA è effettivamente difficile, allora produce una funzione unidirezionale con una botola. La funzione qui è $f(g) = g^e \mod N$. Con la conoscenza di $f(g)$, chiunque potrebbe facilmente calcolare un valore $y$ per un particolare $g = x$. Tuttavia, è praticamente impossibile calcolare un particolare valore $x$ solo conoscendo il valore $y$ e la funzione $f(g)$. L'eccezione è quando ti viene dato un pezzo di informazione $d$, la botola. In quel caso, puoi semplicemente calcolare $y^d$ per ottenere $x$.

Passiamo attraverso un esempio specifico per illustrare il problema RSA. Non posso selezionare un problema RSA che sarebbe considerato difficile nelle condizioni sopra menzionate, poiché i numeri sarebbero ingombranti. Invece, questo esempio serve solo a illustrare come funziona generalmente il problema RSA.

Per iniziare, supponiamo di selezionare due numeri primi casuali 13 e 31. Quindi $p = 13$ e $q = 31$. Il prodotto $N$ di questi due primi è uguale a 403. Possiamo facilmente calcolare l'ordine di 403. È equivalente a $(13 - 1) \cdot (31 - 1) = 360$.
Successivamente, come indicato dal passo 3 del problema RSA, dobbiamo selezionare un coprimo per 360 che sia maggiore di 2 e minore di 360. Non dobbiamo selezionare questo valore casualmente. Supponiamo di selezionare 103. Questo è un coprimo di 360 poiché il suo massimo comune divisore con 103 è 1.
Il passo 4 ora richiede che calcoliamo un valore $d$ tale che $103 \cdot d \mod 360 = 1$. Questo non è un compito facile a mano quando il valore per $N$ è grande. Richiede che utilizziamo una procedura chiamata **algoritmo euclideo esteso**.

Anche se qui non mostro la procedura, essa produce il valore 7 quando $e = 103$. Puoi verificare che la coppia di valori 103 e 7 soddisfa effettivamente la condizione generale $e \cdot d \mod \phi(n) = 1$ attraverso i calcoli sottostanti.

* $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Importante, data la *Proposizione 4*, sappiamo che nessun altro intero tra 1 e 360 per $d$ produrrà il risultato che $103 \cdot d = 1 \mod 360$. Inoltre, la proposizione implica che selezionando un valore diverso per $e$, si otterrà un diverso valore unico per $d$.

Nel passo 5 del problema RSA, dobbiamo selezionare un qualche intero positivo $y$ che sia un coprimo minore di 403. Supponiamo di impostare $y = 2^{103}$. L'esponenziazione di 2 per 103 produce il risultato sottostante.

* $2^{103} \mod 403 = 10.141.204.801.825.835.211.973.625.643.008 \mod 403 = 349 \mod 403$

Il problema RSA in questo particolare esempio è ora il seguente: Ti viene fornito $N = 403$, $e = 103$, e $y = 349 \mod 403$. Ora devi calcolare $x$ tale che $x^{103} = 349 \mod 403$. Cioè, devi trovare che il valore originale prima dell'esponenziazione per 103 era 2.

Sarebbe facile (almeno per un computer) calcolare $x$ se sapessimo che $d = 7$. In tal caso, potresti semplicemente determinare $x$ come di seguito.

* $x = y^7 \mod 403 = 349^7 \mod 403 = 630.634.881.591.804.949 \mod 403 = 2 \mod 403$

Il problema è che non ti è stata fornita l'informazione che $d = 7$. Potresti, naturalmente, calcolare $d$ dal fatto che $103 \cdot d = 1 \mod 360$. Il problema è che non ti è stata data nemmeno l'informazione che l'ordine di $N = 360$. Infine, potresti anche calcolare l'ordine di 403 calcolando il seguente prodotto: $(p - 1) \cdot (q - 1)$. Ma non ti è stato detto nemmeno che $p = 13$ e $q = 31$.

Naturalmente, un computer potrebbe ancora risolvere il problema RSA per questo esempio relativamente facilmente, perché i numeri primi coinvolti non sono grandi. Ma quando i primi diventano molto grandi, si trova di fronte a un compito praticamente impossibile.
Abbiamo ora presentato il problema RSA, un insieme di condizioni in cui risulta difficile, e la matematica sottostante. In che modo tutto ciò aiuta con la crittografia asimmetrica? Specificamente, come possiamo trasformare la difficoltà del problema RSA sotto certe condizioni in uno schema di crittografia o in uno schema di firma digitale?

Un approccio è prendere il problema RSA e costruire schemi in modo diretto. Per esempio, supponiamo che tu abbia generato un insieme di variabili $\Pi$ come descritto nel problema RSA, e assicurati che $p$ e $q$ siano sufficientemente grandi. Imposti la tua chiave pubblica uguale a $(N, e)$ e condividi queste informazioni con il mondo. Come descritto sopra, mantieni segreti i valori di $p$, $q$, $\phi(n)$, e $d$. Infatti, $d$ è la tua chiave privata.

Chiunque voglia inviarti un messaggio $m$ che è un elemento di $C_N$ potrebbe semplicemente criptarlo come segue: $c = m^e \mod N$. (Il testo cifrato $c$ qui è equivalente al valore $y$ nel problema RSA.) Puoi facilmente decriptare questo messaggio calcolando semplicemente $c^d \mod N$.

Potresti tentare di creare uno schema di firma digitale nello stesso modo. Supponiamo che tu voglia inviare a qualcuno un messaggio $m$ con una firma digitale $S$. Potresti semplicemente impostare $S = m^d \mod N$ e inviare la coppia $(m,S)$ al destinatario. Chiunque può verificare la firma digitale semplicemente controllando se $S^e \mod N = m \mod N$. Tuttavia, un attaccante avrebbe molte difficoltà a creare un $S$ valido per un messaggio, dato che non possiede $d$.

Sfortunatamente, trasformare quello che di per sé è un problema difficile, il problema RSA, in uno schema crittografico non è così diretto. Per lo schema di crittografia diretto, puoi solo selezionare coprimi di $N$ come tuoi messaggi. Questo non ci lascia con molti messaggi possibili, certamente non abbastanza per una comunicazione standard. Inoltre, questi messaggi devono essere selezionati casualmente. Questo sembra alquanto impraticabile. Infine, qualsiasi messaggio che viene selezionato due volte produrrà esattamente lo stesso testo cifrato. Questo è estremamente indesiderabile in qualsiasi schema di crittografia e non soddisfa nessuna nozione moderna rigorosa di sicurezza nella crittografia.

I problemi diventano ancora peggiori per il nostro schema di firma digitale diretto. Così com'è, qualsiasi attaccante può facilmente falsificare firme digitali semplicemente selezionando prima un coprimo di $N$ come firma e poi calcolando il messaggio originale corrispondente. Questo chiaramente infrange il requisito dell'infalsificabilità esistenziale.

Tuttavia, aggiungendo un po' di complessità intelligente, il problema RSA può essere utilizzato per creare uno schema di crittografia a chiave pubblica sicuro così come uno schema di firma digitale sicuro. Non entreremo nei dettagli di tali costruzioni qui. [4] Importante, tuttavia, questa complessità aggiuntiva non cambia il problema RSA fondamentale sottostante su cui si basano questi schemi.

**Note:**

[4] Vedi, per esempio, Jonathan Katz e Yehuda Lindell, _Introduzione alla Crittografia Moderna_, CRC Press (Boca Raton, FL: 2015), pp. 410–32 sulla crittografia RSA e pp. 444–41 per le firme digitali RSA.
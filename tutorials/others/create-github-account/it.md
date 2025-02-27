---
name: GitHub Account
description: Come creare il proprio account su GitHub?
---

![cover](assets/cover.webp)

La missione di PlanB è fornire risorse educative di primo livello su Bitcoin, disponibili in quante più lingue possibile. Tutti i contenuti pubblicati sul sito sono open-source e ospitati su GitHub, offrendo a chiunque l'opportunità di contribuire all'arricchimento della piattaforma. I contributi possono assumere varie forme: correzione e revisione dei testi esistenti, traduzione in altre lingue, aggiornamento delle informazioni o creazione di nuovi tutorial non ancora disponibili sul nostro sito.

Se desideri contribuire alla Rete PlanB, dovrai utilizzare Git e GitHub. Se questi strumenti ti sono sconosciuti o se il loro funzionamento ti sembra oscuro, non preoccuparti, questo articolo è per te! Esamineremo insieme i fondamenti di Git e GitHub, così come il gergo tecnico associato, per permetterti di utilizzare efficacemente questi strumenti in seguito.

## Cos'è Git?

Git è un sistema di controllo versione, specificamente progettato per gestire progetti software. Creato nel 2005 da Linus Torvalds, Git è rapidamente diventato lo standard nell'industria dello sviluppo software per il controllo delle versioni. Ma cosa significa esattamente?
![git](assets/11.webp)
Nel suo nucleo, Git permette agli sviluppatori di tracciare le modifiche apportate al codice sorgente di un progetto nel tempo. Questo significa che con ogni modifica nel codice, Git registra una nuova versione del progetto. Se si verifica un errore o se una funzionalità sperimentale non funziona come previsto, è possibile tornare a uno stato precedente del codice, come una sorta di macchina del tempo per i file.

Una delle caratteristiche chiave di Git è la gestione dei branch. Un branch è una sorta di linea parallela dove gli sviluppatori possono lavorare indipendentemente dal resto del progetto. Questo facilita enormemente l'aggiunta di nuove funzionalità o la correzione di bug senza disturbare il codice principale. Una volta che le modifiche sono testate e validate, possono essere unite con il branch principale.

Una delle peculiarità di Git è la sua capacità di operare in modo distribuito. Ogni sviluppatore ha una copia completa del progetto sul proprio disco rigido del computer, permettendogli di lavorare offline e di unire le modifiche in seguito quando è disponibile una connessione Internet. Questo riduce il rischio di conflitti e permette a più sviluppatori di lavorare contemporaneamente sullo stesso progetto senza pestarsi i piedi.
Inizialmente, Git era principalmente progettato per progetti di sviluppo software. Tuttavia, può essere utilizzato anche per gestire progetti di scrittura di contenuti. Invece di collaborare sul codice, collaboriamo sul testo. Ed è precisamente questo metodo che la Rete PlanB ha adottato per gestire i suoi contenuti! Git facilita la collaborazione nella scrittura di corsi e tutorial, poiché permette un tracciamento preciso delle modifiche, una gestione efficiente delle versioni e consente anche la revisione e il miglioramento dei contenuti da parte di altri contributori.
## Cos'è GitHub?

GitHub è una piattaforma di gestione e hosting del codice sorgente basata sul sistema di controllo versione Git di cui abbiamo appena discusso. Lanciato nel 2008, GitHub ha rapidamente guadagnato popolarità ed è diventato un punto di riferimento essenziale per gli sviluppatori in tutto il mondo. Ma in che modo GitHub si differenzia da Git e perché è così cruciale nel nostro metodo di produzione dei contenuti?
![github-](assets/12.webp)
Prima di tutto, è importante capire che GitHub è costruito su Git (di cui abbiamo discusso nella sezione precedente). Mentre Git è lo strumento che traccia le modifiche del codice, GitHub è il servizio online che ospita, condivide e gestisce questo codice.

Immagina Git come una sorta di registro che ogni sviluppatore utilizza sul proprio computer per registrare tutte le modifiche nel proprio progetto. GitHub, d'altra parte, è come una biblioteca pubblica dove tutti questi registri possono essere condivisi, confrontati e combinati.
La differenza fondamentale tra Git e GitHub risiede nella loro funzione: Git è lo strumento utilizzato localmente da ogni sviluppatore per gestire le versioni del proprio codice, mentre GitHub è la piattaforma online che ospita queste versioni e facilita la collaborazione.
GitHub è molto più di un semplice servizio di hosting del codice. È una piattaforma di collaborazione che permette agli sviluppatori di lavorare insieme in modo efficiente. E infatti, PlanB Network utilizza questa piattaforma per ospitare non solo tutto il codice che alimenta il sito web, ma anche, ed è questo che ci interessa, tutto il contenuto (tutorial, formazione, risorse...).

## Alcuni Termini Tecnici

Su Git e GitHub, incontrerai comandi e funzionalità i cui nomi possono sembrare complessi. In questa ultima parte, fornisco definizioni semplici per comprendere i termini tecnici che potresti incontrare utilizzando Git e GitHub:

- **Fetch origin:** Comando che recupera informazioni recenti e modifiche da un repository remoto senza unirle al tuo lavoro locale. Aggiorna il tuo repository locale con nuovi branch e commit presenti nel repository remoto.

- **Pull origin:** Comando che recupera aggiornamenti da un repository remoto e li integra immediatamente nel tuo branch locale per sincronizzarlo. Questo combina i passaggi di fetch e merge in un unico comando.
- **Sync Fork:** Una funzionalità su GitHub che ti permette di aggiornare il tuo fork di un progetto con gli ultimi cambiamenti dal repository sorgente. Questo assicura che la tua copia del progetto rimanga aggiornata con lo sviluppo principale.
- **Push origin:** Comando utilizzato per inviare le tue modifiche locali a un repository remoto.

- **Pull Request:** Una richiesta inviata da un contributore per indicare che ha inviato modifiche a un branch in un repository remoto e desidera che queste modifiche vengano esaminate e, potenzialmente, unite al branch principale del repository.

- **Commit:** Salvare le tue modifiche. Un commit è come uno scatto istantaneo del tuo lavoro in un dato momento, che permette di mantenere una storia delle modifiche. Ogni commit include un messaggio descrittivo che spiega cosa è stato modificato.

- **Branch:** Una versione parallela del repository, che ti permette di lavorare su modifiche senza influenzare il branch principale (spesso chiamato "main" o "master"). I branch facilitano lo sviluppo di nuove funzionalità e la correzione di bug senza il rischio di disturbare il codice stabile.

- **Merge:** Unire consiste nell'integrare le modifiche da un branch a un altro. Viene utilizzato, ad esempio, per aggiungere le modifiche da un branch di lavoro al branch principale, permettendo di aggiungere i vari contributi.

- **Fork:** Fare il fork di un repository significa creare una copia di quel repository sul proprio account GitHub, che ti permette di lavorare sul progetto senza influenzare il repository originale. Il fork può prendere una propria direzione e diventare un progetto diverso dall'originale, oppure può sincronizzarsi regolarmente con il progetto originale per contribuire ad esso.

- **Clone:** Clonare un repository significa fare una copia locale sul tuo computer, che ti dà accesso a tutti i file e alla storia. Questo ti permette di lavorare direttamente sul progetto in locale.

- **Repository:** Spazio di archiviazione per un progetto su GitHub. Un repository contiene tutti i file del progetto così come la storia di tutte le modifiche che sono state apportate. È la base dello storage e della collaborazione su GitHub.

- **Issue:** Uno strumento per tracciare compiti e bug su GitHub. Le issue permettono di segnalare problemi, proporre miglioramenti o discutere di nuove funzionalità. Ogni issue può essere assegnata, etichettata e commentata.

Questa lista ovviamente non è esaustiva. Ci sono molti altri termini tecnici specifici per Git e GitHub. Tuttavia, quelli menzionati qui sono i principali che incontrerai frequentemente.

## Come creare un account GitHub

Se desideri contribuire alla Rete PlanB, avrai bisogno di un account GitHub. In questo tutorial, ti guideremo passo dopo passo su come creare il tuo account, configurarlo e proteggerlo adeguatamente.

- Vai su [https://github.com/signup](https://github.com/signup). 
- Inserisci il tuo indirizzo email, poi clicca sul pulsante verde `Continua`:
![github](assets/1.webp)
- Scegli una password forte, poi clicca sul pulsante verde `Continua`:
![github](assets/2.webp)
- Successivamente, scegli il tuo username. Puoi rivelare la tua vera identità o usare un pseudonimo. Poi, clicca sul pulsante verde `Continua`:
![github](assets/3.webp)
- Completa il Captcha:
![github](assets/4.webp)
- Ti verrà inviata un'email contenente un codice di conferma; dovrai inserirlo per finalizzare la creazione del tuo account:
![github](assets/5.webp)
- Compila le domande se vuoi che GitHub ti guidi verso alcuni strumenti, oppure clicca su `salta personalizzazione` per saltare:
![github](assets/6.webp)
- Scegli il piano gratuito cliccando sul pulsante `Continua gratuitamente`:
![github](assets/7.webp)
- Sarai poi reindirizzato alla tua dashboard.
- Se lo desideri, puoi personalizzare il tuo account cliccando sulla tua immagine del profilo situata in alto a destra dello schermo, poi accedendo al menu `Impostazioni`:
![github](assets/8.webp)
- In questa sezione, hai la possibilità di aggiungere una nuova immagine del profilo, selezionare un nome, personalizzare la tua biografia o aggiungere un link al tuo sito web personale:
![github](assets/9.webp)
- Raccomando anche di visitare il menu `Password e autenticazione` per configurare almeno l'autenticazione a due fattori:
![github](assets/10.webp)

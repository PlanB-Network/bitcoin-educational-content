---
name: GitHub Account
description: Come creare un account su GitHub?
---

![cover](assets/cover.webp)

La missione di Plan ₿ Network è fornire risorse educative di primo livello su Bitcoin, disponibili in quante più lingue possibili. Tutti i contenuti pubblicati sul sito sono open-source e gestiti su GitHub, offrendo a chiunque l'opportunità di contribuire all'arricchimento della piattaforma. La collaborazione con Plan ₿ Network può prendere varie forme: puoi revisionare dei testi esistenti, fare proofreading in altre lingue, aggiornare le informazioni o creare nuovi tutorial non ancora disponibili sul nostro sito.

Se vuoi collaborare con Plan ₿ Network, dovrai utilizzare Git e GitHub. Se questi strumenti ti sono sconosciuti o se il loro funzionamento ti sembra oscuro, non preoccuparti, questo articolo è per te! Esamineremo insieme i fondamenti di Git e GitHub, così come il gergo tecnico associato, per permetterti di utilizzare efficacemente questi strumenti in seguito.

## Cos'è Git?

Git è un sistema progettato per gestire gli aggiornamenti di versione nei progetti software. Creato nel 2005 da Linus Torvalds, Git è rapidamente diventato lo standard nell'industria dello sviluppo software per il controllo delle differenti versioni. Ma cosa significa esattamente?

![git](assets/11.webp)

Alla base, Git permette agli sviluppatori di tracciare le modifiche apportate al codice sorgente di un progetto nel corso del tempo. Questo significa che con ogni modifica nel codice, Git registra una nuova versione del progetto. Se si verifica un errore o se una funzionalità sperimentale non funziona come previsto, è possibile tornare a uno stato precedente del codice, come una sorta di macchina del tempo per i file.

Una delle caratteristiche chiave di Git è la gestione dei branch. Un branch è una sorta di linea parallela dove gli sviluppatori possono lavorare indipendentemente dal resto del progetto. Questo facilita enormemente l'aggiunta di nuove funzionalità o la correzione di bug senza toccare il codice principale. Una volta che le modifiche sono testate e validate, possono essere unite (tramite "merge") al branch principale.

Una delle peculiarità di Git è la sua capacità di operare in modo distribuito. Ogni sviluppatore ha una copia completa del progetto sul proprio disco rigido del computer: ciò gli permette di lavorare offline e di unire le modifiche in seguito, quando si connette ad Internet. Questo riduce il rischio di conflitti e permette a più sviluppatori di lavorare contemporaneamente sullo stesso progetto senza creare sovrapposizioni.
Inizialmente, Git era principalmente usato per gestire progetti di sviluppo software. Tuttavia, può essere utilizzato anche per gestire progetti in cui vengono scritti contenuti testuali. Invece di collaborare sul codice, collaboriamo quindi sulla stesura di un testo. Plan ₿ Network ha adottato precisamente questo metodo per gestire i suoi contenuti! 
Git facilita la collaborazione nella stesura di corsi e tutorial, poiché permette un tracciamento preciso delle modifiche e una gestione efficiente delle varie versioni. Inoltre, consente anche la revisione e il miglioramento dei contenuti da parte di altri contributor esterni.

## Cos'è GitHub?

GitHub è una piattaforma di gestione e hosting del codice sorgente basata sul sistema Git, di cui abbiamo appena discusso. Lanciato nel 2008, GitHub ha rapidamente guadagnato popolarità ed è diventato un punto di riferimento essenziale per gli sviluppatori in tutto il mondo. Ma in che modo GitHub si differenzia da Git, e perché è così cruciale nel per la creazione dei nostri contenuti?

![github-](assets/12.webp)

Prima di tutto, è importante capire che GitHub è basato su Git (di cui abbiamo scritto nella sezione precedente). Mentre Git è lo strumento che traccia le modifiche del codice, GitHub è il servizio online che ospita, condivide e gestisce questo codice.

Immagina Git come una sorta di libro mastro che ogni sviluppatore utilizza sul proprio computer per registrare tutte le modifiche nel proprio progetto. GitHub, d'altra parte, è come una biblioteca pubblica dove tutti questi registri possono essere condivisi, confrontati e combinati.
La differenza fondamentale tra Git e GitHub risiede nella loro funzione: Git è lo strumento utilizzato localmente da ogni sviluppatore per gestire le versioni del codice, mentre GitHub è la piattaforma online che ospita queste versioni e facilita la collaborazione tra diversi utenti.
GitHub è molto più di un semplice servizio di hosting di codice. È una piattaforma di collaborazione che permette agli sviluppatori di lavorare insieme in modo efficiente. E infatti, Plan ₿ Network utilizza questa piattaforma per gestire non solo tutto il codice che alimenta il sito web, ma anche, ed è questo che ci interessa, tutti i contenuti (tutorial, corsi, risorse...).

## Alcuni Termini Tecnici

Su Git e GitHub, incontrerai comandi e funzionalità i cui nomi possono sembrare complessi. In questa ultima parte, ti fornisco alcune definizioni semplici per comprendere i termini tecnici che potresti incontrare utilizzando Git e GitHub:

- **Fetch origin:** Comando che recupera informazioni recenti e modifiche da un repository remoto, senza unirle al tuo lavoro locale. Aggiorna il tuo repository locale con nuovi branch e commit presenti nel repository remoto.

- **Pull origin:** Comando che recupera aggiornamenti da un repository remoto e li integra immediatamente nel tuo branch locale per sincronizzarlo. Questo combina i passaggi di fetch e merge in un unico comando.

- **Sync Fork:** Una funzionalità su GitHub che ti permette di aggiornare il tuo fork di un progetto aggiungendo gli ultimi cambiamenti dal repository sorgente. Questo assicura che la tua copia del progetto rimanga aggiornata con gli ultimi sviluppi nel repository principale.

- **Push origin:** Comando utilizzato per inviare le tue modifiche locali a un repository remoto.

- **Pull Request:** Una richiesta inviata da un collaboratore per indicare che ha effettuato delle modifiche a un branch in un repository remoto. Con essa, l'utente desidera che queste modifiche vengano esaminate e, potenzialmente, unite al branch principale del repository.

- **Commit:** Salvare le tue modifiche. Un commit è come uno scatto istantaneo del tuo lavoro in un dato momento, che permette di mantenere uno storico dei cambiamenti. Ogni commit include un messaggio descrittivo che spiega cosa è stato modificato.

- **Branch:** Una versione parallela del repository, che ti permette di lavorare senza influenzare il branch principale (spesso chiamato "main" o "master"). I branch facilitano lo sviluppo di nuove funzionalità e la correzione di bug senza il rischio di intaccare il codice stabile.

- **Merge:** "Merge" significa integrare le modifiche da un branch a un altro. Viene utilizzato, ad esempio, per aggiungere dei cambiamenti fatti su un branch di lavoro al branch principale, permettendo di aggiungere i vari contributi da parte di diversi utenti.

- **Fork:** Fare il fork di un repository significa creare una copia di quel repository sul proprio account GitHub. Ciò ti permette di lavorare sul progetto senza influenzare il repository originale. Il fork può prendere una propria direzione e diventare un progetto diverso dall'originale, oppure può sincronizzarsi regolarmente con il progetto originale per contribuire allo stesso.

- **Clone:** Clonare un repository significa fare una copia locale sul tuo computer per avere accesso a tutti i file e allo storico dei commit. Questo ti permette di lavorare sul progetto direttamente in locale.

- **Repository:** Spazio di archiviazione di un progetto su GitHub. Un repository contiene tutti i file del progetto, così come lo storico di tutte le modifiche che sono state apportate. È la base della natura collaborativa di GitHub.

- **Issue:** Uno strumento per tracciare compiti assegnati a vari collaboratori e per segnalare i bug su GitHub. Le issue permettono di segnalare problemi, proporre miglioramenti o discutere di nuove funzionalità. Ogni issue può essere assegnata, etichettata e commentata.

Questa lista ovviamente non è esaustiva. Ci sono molti altri termini tecnici specifici per Git e GitHub. Tuttavia, quelli menzionati qui sono quelli che incontrerai frequentemente.

## Come creare un account GitHub

Se desideri collaborare con Plan ₿ Network, avrai bisogno di un account GitHub. In questo tutorial, ti guideremo passo dopo passo su come creare il tuo account, configurarlo e proteggerlo adeguatamente.

- Vai su [https://github.com/signup](https://github.com/signup).

- Inserisci il tuo indirizzo email, poi clicca sul pulsante verde `Continue`:

![github](assets/1.webp)

- Scegli una password forte, poi clicca sul pulsante verde `Continue`:

![github](assets/2.webp)

- Successivamente, scegli il tuo username. Puoi rivelare la tua vera identità o usare un pseudonimo. Poi, clicca sul pulsante verde `Continue`:

![github](assets/3.webp)

- Completa il Captcha:

![github](assets/4.webp)

- Ti verrà inviata un'email con un codice di conferma; dovrai inserirlo per finalizzare la creazione del tuo account:

![github](assets/5.webp)

- Rispondi alle domande se vuoi seguire il tutorial di GitHub per usare alcuni strumenti, oppure clicca su `skip personalization` per saltare:

![github](assets/6.webp)

- Scegli il piano gratuito cliccando sul pulsante `Continue for free`:

![github](assets/7.webp)

- Sarai poi reindirizzato alla tua dashboard.

- Se lo desideri, puoi personalizzare il tuo account cliccando sulla tua immagine del profilo situata in alto a destra dello schermo, poi accedendo al menù `Settings`:

![github](assets/8.webp)

- In questa sezione, hai la possibilità di aggiungere una nuova immagine di profilo, selezionare un nome, personalizzare la tua biografia o aggiungere un link al tuo sito web personale:

![github](assets/9.webp)

- Ti consiglio anche di visitare il menù `Password and authentication` per configurare almeno l'autenticazione a due fattori:

![github](assets/10.webp)

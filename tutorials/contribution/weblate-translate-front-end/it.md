---
name: Weblate - traduzione di elementi statici
description: Come puoi partecipare alla traduzione del front-end sul sito di Plan ₿ Network?
---
![cover](assets/cover.webp)

La missione di Plan ₿ Network è quella di fornire risorse educative di prima classe su Bitcoin e di tradurle nel maggior numero di lingue possibili. Gran parte dei contenuti pubblicati sul sito sono open-source e si trovano su GitHub, consentendo a chiunque di partecipare all'arricchimento della piattaforma. I contributi possono assumere varie forme: correggere e rivedere i contenuti esistenti, aggiornare le informazioni o creare nuovi tutorial da aggiungere alla piattaforma.

In questo tutorial ti mostreremo come contribuire facilmente alla traduzione degli elementi statici del nostro sito web. I dati presenti sulla piattaforma sono suddivisi in due categorie principali:


- i dati/elementi statici del frontend (pagine, pulsanti, ecc.);
- i contenuti didattici (tutorial, corsi, risorse...).

Per tradurre i contenuti didattici, utilizziamo [l'intelligenza artificiale](https://github.com/Asi0Flammeus/LLM-Translator). Poi, per correggere gli eventuali errori presenti in questi file, invitiamo i proofreader a contribuire. Se desideri correggere alcuni contenuti, consulta il seguente tutorial:

https://planb.network/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017

Se invece sei interessato a tradurre gli elementi statici del sito web (esclusi i contenuti didattici), sei nel posto giusto! Per tradurre efficacemente il frontend, utilizziamo lo strumento Weblate, che è molto semplice da usare e facilita l'approccio alla traduzione.


Se desideri aggiungere una lingua completamente nuova a Plan ₿ Network, assicurati di contattare il team di Plan ₿ Network tramite il nostro [gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder). Se non hai Telegram, puoi inviare un'e-mail a mari@planb.network. Assicurati di scrivere una piccola presentazione su chi sei e sulle lingue che parli.

I membri del nostro team ti daranno istruzioni specifiche e apriranno le relative "issue" su Github per coordinare il tuo lavoro.

Segui questa guida specifica prima di aggiungere una nuova lingua a Weblate.

https://planb.network/tutorials/contribution/content/weblate-add-new-language-eef2f5c0-1aba-48a3-b8f0-a57feb761d86

Quando sei pronto per iniziare a tradurre, torna a questo tutorial e passa in rassegna i punti seguenti.

## Registrati su Weblate


- Vai sul [Weblate gestito da Plan ₿ Network](https://weblate.planb.network/):

![weblate](assets/01.webp)


- Se hai già un account Weblate, clicca su "Sign in":

![weblate](assets/02.webp)


- Se non hai un account, clicca su "Register":

![weblate](assets/03.webp)


- Inserisci l'indirizzo e-mail, il nome utente e il nome completo (è possibile utilizzare uno pseudonimo), quindi clicca su "Register":

![weblate](assets/04.webp)


- Nella tua casella di posta elettronica dovresti aver ricevuto un messaggio di conferma da Weblate. Clicca sul link per confermare la registrazione:

![weblate](assets/05.webp)


- Scegli una password forte, quindi clicca su "Change my password":

![weblate](assets/06.webp)


- Ora è possibile tornare alla dashboard di Plan ₿ Network:

![weblate](assets/07.webp)

## Inizia a tradurre


- Clicca sul progetto `Website Elements` (non sul glossario):

![weblate](assets/08.webp)


- Accederai a un'interfaccia in cui è possibile vedere le lingue in corso:

![weblate](assets/09.webp)


- Scegli la tua lingua. Ad esempio, prendiamo il francese:

![weblate](assets/10.webp)


- Per iniziare a tradurre, è sufficiente cliccare sul pulsante "Translate":

![weblate](assets/11.webp)


- Verrai reindirizzato all'interfaccia di lavoro:

![weblate](assets/12.webp)


- Weblate suggerirà automaticamente frasi, paragrafi o addirittura parole da tradurre nella casella "lingua". Nel tuo caso, probabilmente vedrai la stringa principale in inglese e un'altra casella di testo per la tua lingua:

![weblate](assets/13.webp)


- Il tuo compito consiste nel tradurre le stringhe indicate. Devi inserire il testo nella casella corrispondente alla lingua che hai scelto. Ad esempio, se stai lavorando sulla versione francese, scriverai la tua traduzione nella casella `Francese`:

![weblate](assets/14.webp)


- Clicca sulla scheda "Automatic suggestion":

![weblate](assets/15.webp)


- Qui, il Weblate mostra una traduzione fatta dall'intelligenza artificiale:

![weblate](assets/16.webp)


- Se la traduzione suggerita ti sembra pertinente, puoi cliccare sul pulsante `Clone to translation`:

![weblate](assets/17.webp)


- Il suggerimento viene ora inserito nella casella di lavoro:

![weblate](assets/18.webp)


- È quindi possibile modificare manualmente il suggerimento:

![weblate](assets/19.webp)


- Quando la traduzione ti sembra soddisfacente, clicca sul pulsante "Save and Continue". Assicurati di deselezionare la casella "Needs editing" quando sei sicuro della tua traduzione:

![weblate](assets/20.webp)


- Ecco fatto! La traduzione è stata salvata con successo. Weblate ti reindirizzerà automaticamente al prossimo elemento da tradurre. Se torni alla dashboard corrispondente alla tua lingua, puoi notare che ogni stringa ha uno stato di traduzione diverso. Ad esempio, se desideri concentrarti solo sulle "stringhe non tradotte", è possibile cliccare sulla scheda specifica:

![weblate](assets/21.webp)


- Se hai bisogno di cercare una parola specifica, sia nella tua lingua che in quella originale, clicca su "search" e inseriscila:

![weblate](assets/22.webp)

## Linee guida per la traduzione


- Quando trovi parole inserite all'interno di parentesi graffe "{", non è necessario tradurle. Ad esempio, in "Il tuo account è stato creato, {{username}}!", tradurrai l'intera frase mantenendo "username" in inglese.
- Quando trovi "Plan ₿ Network" in una stringa, assicurati di NON tradurre la parola "network" (considera Plan ₿ Network come un marchio). Inoltre, utilizza sempre la ₿ di Bitcoin!
- Se trovi la parola "rete" da sola, puoi invece tradurla.
- Non tradurre "B-CERT", perché è un'altra parola fissa.
- Se trovi stringhe che terminano con uno spazio, è possibile lasciarlo.
- Alcune stringhe potrebbero contenere uno spazio tra l'ultima parola e un segno di punteggiatura: non lasciarlo nella tua lingua a meno che la grammatica non lo implichi. Ad esempio, "Contact information :" dovrebbe essere corretto in "Informazioni di contatto:". In questo caso, traducilo correttamente. È inoltre possibile aggiungere un commento per segnalare agli amministratori questo problema nella versione originale in inglese.

## Nuove caratteristiche


- Stiamo lavorando per aggiungere una sezione "explanation" per ogni stringa, insieme a uno screenshot, per aiutarti a trovare la posizione di una specifica frase/parola sul sito web. Al momento, se hai dubbi su alcune parole e hai bisogno di trovare la loro posizione specifica sul sito, puoi fare una domanda nella sezione "comments" o chiedere chiarimenti al coordinatore sul gruppo Telegram menzionato all'inizio di questo tutorial.

![weblate](assets/23.webp)

Grazie in anticipo per il tuo contributo alla traduzione di Plan ₿ Network! Se hai domande o commenti specifici da farci, non esitare a contattarci tramite il [gruppo Telegram](https://t.me/PlanBNetwork_ContentBuilder).


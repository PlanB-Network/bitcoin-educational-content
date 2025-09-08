---
name: Aggiungere un evento su Plan ₿ Network
description: Come aggiungere un nuovo evento su Plan ₿ Network?
---
![evento](assets/cover.webp)

La missione di Plan ₿ Network è fornire risorse educative di primo livello su Bitcoin in quante più lingue possibile. Tutti i contenuti pubblicati sul sito sono open-source e mantenuti su GitHub, offrendo a chiunque l'opportunità di collaborare all'arricchimento della piattaforma.

Vuoi aggiungere una conferenza Bitcoin su Plan ₿ Network aumentando la visibilità del tuo evento, ma non sai come fare? Questo tutorial è per te!

![evento](assets/01.webp)

- Prima di tutto, devi avere un account su GitHub. Se non sai come crearne uno, abbiamo realizzato un tutorial dettagliato per guidarti.

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Vai al [repository GitHub di Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) nella sezione `resources/conference/`:

![evento](assets/02.webp)

- Clicca in alto a destra sul pulsante `Add file`, poi su `Create new file`:

![evento](assets/03.webp)

- Se non hai mai aggiunto contenuti al repository, dovrai creare il tuo fork. Ciò significa creare una copia di quel repository sul proprio account GitHub, permettendoti di lavorare sul progetto senza influenzare il repository originale. Clicca sul pulsante `Fork this repository`:

![evento](assets/04.webp)

- Arriverai quindi alla pagina di modifica di GitHub:

![evento](assets/05.webp)

- Crea una cartella dedicata alla conferenza (o qualsiasi altro evento). Per fare ciò, nella casella `Name your file...`, inserisci il nome della conferenza in minuscolo con trattini al posto degli spazi. Ad esempio, se la conferenza si chiama "Paris Bitcoin Conference", dovresti scrivere `paris-bitcoin-conference`. Aggiungi anche l'anno, per esempio: `paris-bitcoin-conference-2024`:

![evento](assets/06.webp)

- Per confermare la creazione della cartella, basta inserire uno slash `/` dopo il nome nella stessa, per esempio: `paris-bitcoin-conference-2024/`. Aggiungere uno slash crea automaticamente una directory, anziché un file:

![evento](assets/07.webp)

- In questa cartella, crea un primo file YAML chiamato `events.yml`:

![evento](assets/08.webp)

- Compila questo file con le informazioni sulla tua conferenza usando questo modello:

```yaml
id:
start_date:
end_date:
timezone:
address_line_1:
address_line_2: 
address_line_3: 
name:
project:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language: 
  - 
links:
  website:
  replay_url:    
  live_url :
tags: 
  - 
```

Ad esempio, il tuo file YAML potrebbe apparire così:

```yaml
id: 82011dd9-0a20-42a2-8020-9106336c47f5
start_date: 2024-08-15
end_date: 2024-08-18
timezone: Europe/Paris
address_line_1: Paris, France
address_line_2: 
address_line_3: 
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants every year!
language:
- fr    - en
  - es
  - it
links:
  website: https://paris.bitcoin.fr/conference
  replay_url:
  live_url :
tags: 
  - Bitcoiner
  - Generale
  - Internazionale
```
![evento](assets/09.webp)
Se la tua organizzazione non ha ancora un identificatore "*project*", puoi aggiungerlo seguendo questo altro tutorial.

https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d


- Una volta terminato di apportare modifiche a questo file, salvalo cliccando sul pulsante `Commit changes...`:

![evento](assets/10.webp)

- Aggiungi un titolo e una breve descrizione:

![evento](assets/11.webp)

- Clicca sul pulsante verde `Propose changes`:

![evento](assets/12.webp)

- Arriverai quindi su una pagina che riassume tutte le tue modifiche:

![evento](assets/13.webp)

- Clicca sulla tua immagine del profilo GitHub in alto a destra, poi su `Your Repositories`:

![evento](assets/14.webp)

- Seleziona il tuo fork del repository Plan ₿ Network:

![evento](assets/15.webp)

- Dovresti vedere una notifica in alto alla finestra con il tuo nuovo branch. Probabilmente si chiama `patch-1`. Cliccaci sopra:

![evento](assets/16.webp)

- Ora sei sul tuo branch di lavoro:

![evento](assets/17.webp)

- Torna alla cartella `resources/conference/` e seleziona la cartella della conferenza che hai appena creato tramite commit precedente:

![evento](assets/18.webp)

- Nella cartella della tua conferenza, clicca sul pulsante `Add file`, poi su `Create new file`:

![evento](assets/19.webp)

- Nomina questa nuova cartella `assets` e conferma la creazione mettendo uno slash `/` alla fine:

![evento](assets/20.webp)

- In questa cartella `assets`, crea un file chiamato `.gitkeep`:

![evento](assets/21.webp)

- Clicca sul pulsante `Commit changes...`:

![evento](assets/22.webp)

- Lascia il titolo del commit come predefinito, e assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata. Poi clicca su `Commit changes`:

![evento](assets/23.webp)

- Ritorna alla cartella `assets`:

![evento](assets/24.webp)

- Clicca sul pulsante `Add file`, poi su `Upload files`:

![evento](assets/25.webp)

- Si aprirà una nuova pagina. Trascina e rilascia un'immagine che rappresenta la tua conferenza e che verrà visualizzata sul sito di Plan ₿ Network:

![evento](assets/26.webp)

- Può essere il logo, una miniatura, o anche un poster:

![evento](assets/27.webp)

- Una volta caricata l'immagine, verifica che la casella `Commit directly to the patch-1 branch` sia spuntata, poi clicca su `Commit changes`:

![evento](assets/28.webp)

- Attenzione, la tua immagine deve essere nominata `thumbnail` e deve essere in formato `.webp`. Il nome completo del file dovrebbe quindi essere: `thumbnail.webp`:

![evento](assets/29.webp)

- Ritorna alla cartella `assets` e clicca sul file intermedio `.gitkeep`:

![evento](assets/30.webp)

- Una volta sul file, clicca sui 3 punti in alto a destra, poi su `Delete file`.
- Verifica di essere ancora sullo stesso branch di lavoro, quindi clicca sul pulsante `Commit changes`:

![evento](assets/31.webp)

- Aggiungi un titolo e una descrizione al tuo commit, poi clicca su `Commit changes`:

![evento](assets/32.webp)

- Torna alla root del tuo repository:

![evento](assets/34.webp)

- Dovresti vedere un messaggio che indica che il tuo branch ha subito delle modifiche. Clicca sul pulsante `Compare & pull request`:

![evento](assets/35.webp)

- Aggiungi un titolo chiaro e una descrizione alla tua PR:

![evento](assets/36.webp)

- Clicca sul pulsante `Create pull request`:

![evento](assets/37.webp)

Congratulazioni! La tua PR è stata creata con successo. Un coordinatore la controllerà e, se tutto è in ordine, la unirà al repository principale di Plan ₿ Network. Dovresti vedere il tuo evento apparire sul sito web qualche giorno dopo.

Tieni monitorata la tua PR. Un amministratore potrebbe lasciare un commento chiedendo ulteriori informazioni. Fino a quando la tua PR non è validata, puoi consultarla nella scheda `Pull requests` sul repository GitHub di Plan ₿ Network:

![evento](assets/38.webp)

Grazie mille per il tuo prezioso aiuto! :)



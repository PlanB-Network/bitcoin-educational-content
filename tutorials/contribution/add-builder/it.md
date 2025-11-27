---
name: Aggiungere un progetto
description: Come aggiungere un nuovo progetto sulla Plan ₿ Academy?
---
![project](assets/cover.webp)

La missione di Plan ₿ Academy è fornire risorse educative di primo livello su Bitcoin, nel maggior numero di lingue possibili. Tutti i contenuti pubblicati sul sito sono open-source e gestiti su GitHub, il che consente a chiunque di partecipare all'arricchimento della piattaforma.

Vuoi aggiungere un nuovo "project" Bitcoin al sito di Plan ₿ Academy e dare visibilità alla tua azienda o software, ma non sai come fare? Questo tutorial è per te!

![project](assets/01.webp)

- Prima di tutto, devi avere un account GitHub. Se non sai come crearne uno, abbiamo scritto un tutorial dettagliato per guidarti.

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Vai al [repository GitHub di Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects) nella sezione `resources/project/`:

![project](assets/02.webp)

- Clicca in alto a destra sul pulsante `Add file`, poi su `Create new file`:

![project](assets/03.webp)

- Se non hai mai aggiunto contenuti su Plan ₿ Academy prima d'ora, dovrai creare il tuo fork. Fare un fork di un repository significa creare una copia di quel repository sul proprio account GitHub, il che ti consente di lavorare sul progetto senza influenzare il repository originale. Clicca sul pulsante `Fork this repository`:

![project](assets/04.webp)

- Arriverai quindi alla pagina di modifica di GitHub:

![project](assets/05.webp)

- Crea una cartella per iol tuo progetto. Per fare ciò, nella casella `Name your file...`, scrivi il nome della tua azienda o progetto in minuscolo con i trattini al posto degli spazi. Ad esempio, se la tua azienda si chiama "Bitcoin Baguette", dovresti scrivere `bitcoin-baguette`:

![project](assets/06.webp)

- Per validare la creazione della cartella, basta aggiungere uno slash dopo il nome nella stessa casella, per esempio: `bitcoin-baguette/`. Aggiungere uno slash crea automaticamente una directory, anziché un file:

![project](assets/07.webp)

- In questa cartella, creerai un primo file YAML denominato `project.yml`:

![project](assets/08.webp)

- Compila questo file con le informazioni sulla tua azienda utilizzando questo template:

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

Ecco come compilare ogni voce:
- `name`: Il nome della tua azienda (obbligatorio);
- `address` : L'indirizzo del tuo progetto (facoltativo);
- `language` : I paesi in cui opera il tuo progetto o le lingue supportate (facoltativo);
- `links` : I vari link ufficiali del tuo progetto (facoltativo);
- `tags` : 2 [tag](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) che qualificano il tuo progetto (obbligatorio);
- `category` : La categoria che descrive meglio il campo in cui opera il tuo progetto tra le seguenti scelte:
	- `wallet`,
	- `infrastructure`,
	- `exchange`,
	- `education`,
	- `service`,
	- `communities`,
	- `conference`,
	- `privacy`,
	- `investment`,
	- `node`,
	- `mining`,
	- `news`,
	- `manufacturer`.
 
Ad esempio, il tuo file YAML potrebbe apparire così:

```yaml
name: Bitcoin Baguette

address_line_1: Paris, Francia
address_line_2:
address_line_3: 

language:
  - fr
  - en

links:
  website: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tags:
  - bitcoin
  - education

category: education
```

![project](assets/09.webp)

- Una volta apportate le modifiche a questo file, salvalo cliccando sul pulsante `Commit changes...`:

![project](assets/10.webp)

- Aggiungi un titolo e una breve descrizione per le tue modifiche:

![project](assets/11.webp)

- Clicca sul pulsante verde `Propose changes`:

![project](assets/12.webp)

- Arriverai quindi a una pagina che riassume tutte le tue modifiche:

![project](assets/13.webp)

- Clicca sulla tua immagine del profilo GitHub in alto a destra, poi su `Your Repositories`:

![project](assets/14.webp)

- Seleziona il tuo fork del repository Plan ₿ Academy:

![project](assets/15.webp)

- Dovresti vedere una notifica in alto alla finestra con il tuo nuovo branch. Probabilmente si chiama `patch-1`. Cliccaci sopra:

![project](assets/16.webp)

- Ora sei sul tuo branch di lavoro (**assicurati di essere sullo stesso branch delle tue modifiche precedenti, questo è importante!**):

![project](assets/17.webp)

- Torna alla cartella `resources/projects/` e seleziona la cartella del tuo progetto che hai appena creato tramite il commit precedente:

![project](assets/18.webp)

- Nella cartella del tuo progetto, clicca sul pulsante `Add file`, poi su `Create new file`:

![project](assets/19.webp)

- Denomina questa nuova cartella `assets` e conferma la creazione mettendo uno slash `/` alla fine:

![project](assets/20.webp)

- In questa cartella `assets`, crea un file chiamato `.gitkeep`:

![project](assets/21.webp)

- Clicca sul pulsante `Commit changes...`:

![project](assets/22.webp)

- Lascia il titolo del commit come predefinito, e assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:

![project](assets/23.webp)

- Torna alla cartella `assets`:

![project](assets/24.webp)

- Clicca sul pulsante `Add file`, poi su `Upload files`:

![project](assets/25.webp)

- Si aprirà una nuova pagina. Trascina e rilascia un'immagine della tua azienda o del tuo software nell'area relativa. Questa immagine verrà visualizzata sul sito di Plan ₿ Academy:

![project](assets/26.webp)

- Può essere il logo o un'icona:

![project](assets/27.webp)

- Una volta caricata l'immagine, verifica che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:

![project](assets/28.webp)

- Attenzione, la tua immagine deve essere quadrata, deve essere nominata `logo`, e deve essere in formato `.webp`. Il nome completo del file dovrebbe quindi essere: `logo.webp`:

![project](assets/29.webp)

- Torna alla tua cartella `assets` e clicca sul file intermedio `.gitkeep`:

![project](assets/30.webp)

- Una volta sul file, clicca sui tre piccoli punti in alto a destra e poi su `Delete file`:

![project](assets/31.webp)

- Verifica di essere ancora sullo stesso ramo di lavoro, poi clicca sul pulsante `Commit changes`:

![project](assets/32.webp)

- Aggiungi un titolo e una descrizione al tuo commit, poi clicca su `Commit changes`:

![project](assets/33.webp)

- Torna alla cartella della tua azienda:

![project](assets/34.webp)

- Clicca sul pulsante `Add file`, poi su `Create new file`:

![project](assets/35.webp)

- Crea un nuovo file YAML nominandolo con l'indicatore della tua lingua madre. Questo file sarà utilizzato per la descrizione del project. Ad esempio, se voglio scrivere la mia descrizione in inglese, nominerò questo file `en.yml`:

![project](assets/36.webp)

- Compila questo file YAML utilizzando questo template:
```yaml
description: |
 
contributors:
 - 
```

- Nella sezione `contributors`, puoi aggiungere il tuo identificativo da contributor di Plan ₿ Academy, se ne hai uno. Se non lo hai, lascia questo campo vuoto.

- Nella sezione `description`, devi semplicemente aggiungere un breve paragrafo che descrive la tua azienda o il tuo software. La descrizione deve essere nella stessa lingua del nome del file. Non è necessario tradurre questa descrizione in tutte le lingue supportate sul sito, poiché il team di Plan ₿ Academy lo farà utilizzando il relativo modello. Ad esempio, ecco come potrebbe apparire il tuo file:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is an association based in Paris dedicated to organizing meetups and technical workshops on Bitcoin. We bring together enthusiasts, experts, and curious minds to explore and discuss the complexities of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and deepening the understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be part of the Bitcoin community in Paris and stay updated with the latest advancements in the field.

contributors:
- 
```

![project](assets/37.webp)

- Clicca sul pulsante `Commit changes`:

![project](assets/38.webp)

- Assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, aggiungi un titolo, poi clicca su `Commit changes`:

![project](assets/39.webp)

- La cartella della tua azienda dovrebbe ora apparire così:

![project](assets/40.webp)

- Se tutto è a posto, ritorna alla rotto del tuo fork:

![project](assets/41.webp)

- Dovresti vedere un messaggio che indica che il tuo branch ha subito delle modifiche. Clicca sul pulsante `Compare & pull request`:

![project](assets/42.webp)

- Aggiungi un titolo chiaro e una descrizione al tuo PR:

![project](assets/43.webp)

- Clicca sul pulsante `Create pull request`:

![project](assets/44.webp)

Congratulazioni! La PR è stata creata con successo. Un coordinatore lo esaminerà ora e, se tutto è in ordine, lo integrerà nel repository principale di Plan ₿ Academy. Dovresti vedere apparire il tuo progetto sul sito web qualche giorno dopo.

Assicurati di seguire il progresso della PR. Un amministratore potrebbe lasciare un commento chiedendo ulteriori informazioni. Fino a quando non è validata, puoi consultarla nella scheda `Pull requests` sul repository GitHub di Plan ₿ Academy:

![project](assets/45.webp)

Grazie mille per il tuo prezioso contributo! :)


---
name: Aggiungere un podcast su Plan ₿ Academy
description: Come aggiungere un nuovo podcast su Plan ₿ Academy?
---
![podcast](assets/cover.webp)

La missione di Plan ₿ Academy è fornire risorse educative di primo livello su Bitcoin in quante più lingue possibili. Tutti i contenuti pubblicati sul sito sono open-source e gestiti su GitHub, permettendo a chiunque di partecipare all'arricchimento della piattaforma.

Stai cercando di aggiungere un podcast Bitcoin su Plan ₿ Academy per aumentare la visibilità del tuo show, ma non sai come fare? Questo tutorial è per te!

![podcast](assets/01.webp)

- Prima di tutto, devi avere un account GitHub. Se non sai come crearne uno, abbiamo scritto un tutorial dettagliato per guidarti.

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Vai al [repository GitHub di Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) nella sezione `resources/podcasts/`:

![podcast](assets/02.webp)

- Clicca in alto a destra sul pulsante `Add file`, poi su `Create new file`:

![podcast](assets/03.webp)

- Se non hai mai aggiunto contenuti al repository, dovrai creare il tuo fork. Fare un fork di un repository significa creare una copia del repository principale sul proprio account GitHub, permettendoti di lavorare sul progetto senza influenzare il repository originale. Clicca sul pulsante `Fork this repository`:

![podcast](assets/04.webp)

- Arriverai quindi alla pagina di modifica di GitHub:

![podcast](assets/05.webp)

- Crea una cartella per il tuo podcast. Per fare ciò, nella casella `Name your file...`, scrivi il nome del tuo podcast in minuscolo con i trattini al posto degli spazi. Ad esempio, se il tuo show si chiama "Super Podcast Bitcoin", dovresti scrivere `super-podcast-bitcoin`:

![podcast](assets/06.webp)

- Per confermare la creazione della cartella, basta aggiungere uno slash `/` dopo il nome del tuo podcast, per esempio: `super-podcast-bitcoin/`. Aggiungere uno slash crea automaticamente una directory anziché un file:

![podcast](assets/07.webp)

- In questa cartella, crea un primo file YAML chiamato `podcast.yml`:

![podcast](assets/08.webp)

- Compila questo file con le informazioni sul tuo podcast usando questo modello:

```yaml
name: 
host: 
language: 
links:
  podcast: 
  twitter: 
  website: 
description: |
  
tags:
  - 
  - 
contributors:
  - 
```

Ecco i dettagli da compilare per ogni campo:

- **`name`**: Indica il nome del tuo podcast.
- **`host`**: Elenca i nomi o pseudonimi degli speaker o del conduttore del podcast. Ogni nome dovrebbe essere separato da una virgola.
- **`language`**: Indica il codice della lingua parlata nel tuo podcast. Ad esempio, per l'inglese, nota `en`, per l'italiano `it`...

- **`links`**: Fornisci i link ai tuoi contenuti. Hai due opzioni:
	- `podcast`: il link del tuo podcast,
	- `twitter`: il link del profilo Twitter del podcast o del content creator,
	- `website`: il link del sito web del podcast o del content creator.
- **`description`**: Aggiungi un breve paragrafo che descrive il tuo podcast. La descrizione deve essere nella stessa lingua indicata nel campo `language:`.
- **`tags`**: Aggiungi due tag associati al tuo podcast. Esempi:
    - `bitcoin`
    - `tecnology`
    - `economy`
    - `education`...

- **`contributors`**: Indica il tuo ID da contributor, se ne possiedi uno.

Ad esempio, il tuo file YAML potrebbe apparire così:

```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin is a LIVE technical session held once a week on Twitter to delve into the Bitcoin protocol, layer two solutions, and everything that amazes. Our guests Lounes, Pantamis, Loïc, and Sosthene will answer your questions and provide the most technical show on Bitcoin in the world.

tags:
  - bitcoin
  - tecnology
contributors:
  - rabbit-hole
```

![podcast](assets/09.webp)

- Una volta terminato di apportare modifiche a questo file, salvalo cliccando sul pulsante `Commit changes...`:

![podcast](assets/10.webp)

- Aggiungi un titolo e una breve descrizione per le tue modifiche:

![podcast](assets/11.webp)

- Clicca sul pulsante verde `Propose changes`:

![podcast](assets/12.webp)

- Arriverai quindi su una pagina che riassume tutte le tue modifiche:

![podcast](assets/13.webp)

- Clicca sulla tua immagine del profilo GitHub in alto a destra, poi su `Your Repositories`:

![podcast](assets/14.webp)

- Seleziona il tuo fork del repository Plan ₿ Academy:

![podcast](assets/15.webp)

- Dovresti vedere una notifica in alto alla finestra con il tuo nuovo branch. Probabilmente si chiama `patch-1`. Cliccaci sopra:

![podcast](assets/16.webp)

- Ora sei sul tuo branch di lavoro:

![podcast](assets/17.webp)

- Torna alla cartella `resources/podcast/` e seleziona la cartella del podcast che hai appena creato nel commit precedente:
- 
![podcast](assets/18.webp)

- Nella tua cartella podcast, clicca sul pulsante `Add file`, poi su `Create new file`:

![podcast](assets/19.webp)

- Nomina questa nuova cartella `assets` e conferma la creazione aggiungendo uno slash `/` alla fine:

![podcast](assets/20.webp)

- In questa cartella `assets`, crea un file chiamato `.gitkeep`:

![podcast](assets/21.webp)

- Clicca sul pulsante `Commit changes...`:

![podcast](assets/22.webp)

- Lascia il titolo del commit come predefinito, e assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:

![podcast](assets/23.webp)

- Ritorna alla cartella `assets`:

![podcast](assets/24.webp)

- Clicca sul pulsante `Add file`, poi su `Upload files`:

![podcast](assets/25.webp)

- Si aprirà una nuova pagina. Trascina e rilascia il logo del tuo podcast nell'area indicata. Questa immagine verrà visualizzata sul sito Plan ₿ Academy:

![podcast](assets/26.webp)

- Attenzione, l'immagine deve essere quadrata, per adattarsi al meglio al nostro sito web:

![podcast](assets/27.webp)

- Una volta caricata l'immagine, verifica che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:

- ![podcast](assets/28.webp)
  
- Attenzione, la tua immagine deve essere denominata `logo` e deve essere in formato `.webp`. Il nome completo del file deve quindi essere: `logo.webp`:

- ![podcast](assets/29.webp)

- Torna alla tua cartella `assets` e clicca sul file intermedio `.gitkeep`:

![podcast](assets/30.webp)

- Una volta sul file, clicca sui tre punti in alto a destra e poi su `Delete file`:

- ![podcast](assets/31.webp)

- Verifica di essere ancora sullo stesso branch di lavoro, poi clicca sul pulsante `Commit changes`:

 ![podcast](assets/32.webp)
 
- Aggiungi un titolo e una descrizione al tuo commit, poi clicca su `Commit changes`:

 ![podcast](assets/33.webp)
 
- Torna alla root del tuo repository:

![podcast](assets/34.webp)

- Dovresti vedere un messaggio che indica che il tuo branch ha subito delle modifiche. Clicca sul pulsante `Compare & pull request`:

![podcast](assets/35.webp)

- Aggiungi un titolo chiaro e una descrizione alla tua PR:

![podcast](assets/36.webp)

- Clicca sul pulsante `Create pull request`:

![podcast](assets/37.webp)

Congratulazioni! La tua PR è stata creata con successo. Un coordinatore la esaminerà e, se tutto è in ordine, la unirà al repository principale di Plan ₿ Academy. Dovresti vedere apparire il tuo podcast sul sito web qualche giorno dopo.

Tieni monitorata la tua PR. Un amministratore potrebbe lasciare un commento chiedendo ulteriori informazioni. Finché la tua PR non è validata, puoi visualizzarla nella scheda `Pull requests` sul repository GitHub di Plan ₿ Academy: 

![podcast](assets/38.webp)

Grazie mille per il tuo prezioso aiuto! :)

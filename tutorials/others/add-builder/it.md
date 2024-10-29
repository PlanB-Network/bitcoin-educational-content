---
name: Aggiunta di un Builder
description: Come proporre l'aggiunta di un nuovo builder sulla rete PlanB?
---
![builder](assets/cover.webp)

La missione di PlanB è fornire risorse educative di primo livello su Bitcoin, nel maggior numero di lingue possibile. Tutti i contenuti pubblicati sul sito sono open-source e ospitati su GitHub, il che consente a chiunque di partecipare all'arricchimento della piattaforma.

Vuoi aggiungere un nuovo "builder" Bitcoin al sito della rete PlanB e dare visibilità alla tua azienda o software, ma non sai come fare? Questo tutorial è per te!
![builder](assets/01.webp)
- Prima di tutto, devi avere un account GitHub. Se non sai come crearne uno, abbiamo realizzato un tutorial dettagliato per guidarti.

https://planb.network/tutorials/others/create-github-account


- Vai al [repository GitHub di PlanB dedicato ai dati](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders) nella sezione `resources/builder/`:
![builder](assets/02.webp)
- Clicca in alto a destra sul pulsante `Add file`, poi su `Create new file`:
![builder](assets/03.webp)
- Se non hai mai contribuito ai contenuti della rete PlanB prima d'ora, dovrai creare il tuo fork del repository originale. Fare un fork di un repository significa creare una copia di quel repository sul proprio account GitHub, il che ti consente di lavorare sul progetto senza influenzare il repository originale. Clicca sul pulsante `Fork this repository`:
![builder](assets/04.webp)
- Arriverai quindi alla pagina di modifica di GitHub:
![builder](assets/05.webp)
- Crea una cartella per la tua azienda. Per fare ciò, nella casella `Name your file...`, scrivi il nome della tua azienda in minuscolo con i trattini al posto degli spazi. Ad esempio, se la tua azienda si chiama "Bitcoin Baguette", dovresti scrivere `bitcoin-baguette`:
![builder](assets/06.webp)
- Per validare la creazione della cartella, basta aggiungere uno slash dopo il nome nella stessa casella, per esempio: `bitcoin-baguette/`. Aggiungere uno slash crea automaticamente una cartella anziché un file:
![builder](assets/07.webp)
- In questa cartella, creerai un primo file YAML denominato `builder.yml`:
![builder](assets/08.webp)
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

Ecco cosa compilare per ogni chiave:
- `name`: Il nome della tua azienda (obbligatorio);
- `address` : La localizzazione della tua attività (facoltativo);
- `language` : I paesi in cui opera la tua attività o le lingue supportate (facoltativo);
- `links` : I vari link ufficiali della tua attività (facoltativo);
- `tags` : 2 termini che qualificano la tua attività (obbligatorio);
- `category` : La categoria che descrive meglio il campo in cui opera la tua attività tra le seguenti scelte:
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

address_line_1: Parigi, Francia
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
  - educazione

category: educazione
```

![builder](assets/09.webp)
- Una volta apportate le modifiche a questo file, salvalo cliccando sul pulsante `Commit changes...`:
![builder](assets/10.webp)
- Aggiungi un titolo per le tue modifiche, insieme a una breve descrizione:
![builder](assets/11.webp)
- Clicca sul pulsante verde `Propose changes`:
![builder](assets/12.webp)
- Arriverai quindi a una pagina che riassume tutte le tue modifiche:
![builder](assets/13.webp)
- Clicca sulla tua immagine del profilo GitHub in alto a destra, poi su `Your Repositories`:
![builder](assets/14.webp)
- Seleziona il tuo fork del repository PlanB Network:
![builder](assets/15.webp)
- Dovresti vedere una notifica in alto alla finestra con il tuo nuovo branch. Probabilmente si chiama `patch-1`. Cliccaci sopra:
![builder](assets/16.webp)
- Ora sei sul tuo branch di lavoro (**assicurati di essere sullo stesso branch delle tue modifiche precedenti, questo è importante!**):
![builder](assets/17.webp)
- Torna alla cartella `resources/builders/` e seleziona la cartella della tua attività che hai appena creato nel commit precedente:
![builder](assets/18.webp)
- Nella cartella della tua attività, clicca sul pulsante `Add file`, poi su `Create new file`:
![builder](assets/19.webp)
- Nominare questa nuova cartella `assets` e confermarne la creazione mettendo uno slash `/` alla fine:
![builder](assets/20.webp)
- In questa cartella `assets`, crea un file chiamato `.gitkeep`:
![builder](assets/21.webp)
- Clicca sul pulsante `Commit changes...`:
![builder](assets/22.webp)
- Lascia il titolo del commit come predefinito, e assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`: ![builder](assets/23.webp)
- Torna alla cartella `assets`:
![builder](assets/24.webp)
- Clicca sul pulsante `Add file`, poi su `Upload files`:
![builder](assets/25.webp)
- Si aprirà una nuova pagina. Trascina e rilascia un'immagine della tua azienda o del tuo software nell'area. Questa immagine verrà visualizzata sul sito di PlanB Network:
![builder](assets/26.webp)
- Può essere il logo o un'icona:
![builder](assets/27.webp)
- Una volta caricata l'immagine, verifica che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:
![builder](assets/28.webp)
- Attenzione, la tua immagine deve essere quadrata, deve essere nominata `logo`, e deve essere in formato `.webp`. Il nome completo del file dovrebbe quindi essere: `logo.webp`:
![builder](assets/29.webp)
- Torna alla tua cartella `assets` e clicca sul file intermedio `.gitkeep`:
![builder](assets/30.webp)- Una volta sul file, clicca sui tre piccoli punti in alto a destra e poi su `Delete file`:
![builder](assets/31.webp)
- Verifica di essere ancora sullo stesso ramo di lavoro, poi clicca sul pulsante `Commit changes`:
![builder](assets/32.webp)
- Aggiungi un titolo e una descrizione al tuo commit, poi clicca su `Commit changes`:
![builder](assets/33.webp)
- Torna alla cartella della tua azienda:
![builder](assets/34.webp)
- Clicca sul pulsante `Add file`, poi su `Create new file`:
![builder](assets/35.webp)
- Crea un nuovo file YAML nominandolo con l'indicatore della tua lingua madre. Questo file sarà utilizzato per la descrizione del builder. Ad esempio, se voglio scrivere la mia descrizione in inglese, nominerò questo file `en.yml`:
![builder](assets/36.webp)
- Compila questo file YAML utilizzando questo template:
```yaml
description: |
 
contributors:
 - 
```

- Per la chiave `contributors`, puoi aggiungere il tuo identificativo di contributore a PlanB Network se ne hai uno. Se non lo hai, lascia questo campo vuoto.
- Per la chiave `description`, devi semplicemente aggiungere un breve paragrafo che descrive la tua azienda o il tuo software. La descrizione deve essere nella stessa lingua del nome del file. Non è necessario tradurre questa descrizione in tutte le lingue supportate sul sito, poiché i team di PlanB lo faranno utilizzando il loro modello. Ad esempio, ecco come potrebbe apparire il tuo file:
```yaml
description: |
Fondata nel 2017, Bitcoin Baguette è un'associazione con sede a Parigi dedicata all'organizzazione di meetup e workshop tecnici su Bitcoin. Riuniamo appassionati, esperti e menti curiose per esplorare e discutere le complessità della tecnologia Bitcoin. I nostri eventi offrono una piattaforma per la condivisione di conoscenze, networking e per approfondire la comprensione dei meccanismi interni di Bitcoin. Unisciti a noi a Bitcoin Baguette per far parte della comunità Bitcoin di Parigi e rimanere aggiornato con gli ultimi progressi nel campo.

contributors:
- 
```
![builder](assets/37.webp)
- Clicca sul pulsante `Commit changes`:
![builder](assets/38.webp)
- Assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, aggiungi un titolo, poi clicca su `Commit changes`:
![builder](assets/39.webp)
- La cartella della tua azienda dovrebbe ora apparire così:
![builder](assets/40.webp)
- Se tutto è di tuo gradimento, ritorna alla radice del tuo fork:
![builder](assets/41.webp)
- Dovresti vedere un messaggio che indica che il tuo ramo ha subito delle modifiche. Clicca sul pulsante `Compare & pull request`:
![builder](assets/42.webp)
- Aggiungi un titolo chiaro e una descrizione al tuo PR:
![builder](assets/43.webp)
- Clicca sul pulsante `Create pull request`:
![builder](assets/44.webp)
Congratulazioni! Il tuo PR è stato creato con successo. Un amministratore lo esaminerà ora e, se tutto è in ordine, lo integrerà nel repository principale di PlanB Network. Dovresti vedere apparire il tuo profilo builder sul sito web qualche giorno dopo.

Assicurati di seguire il progresso del tuo PR. Un amministratore potrebbe lasciare un commento chiedendo ulteriori informazioni. Fino a quando il tuo PR non è validato, puoi consultarlo nella scheda `Pull requests` sul repository GitHub di PlanB Network:
![builder](assets/45.webp)
Grazie mille per il tuo prezioso contributo! :)

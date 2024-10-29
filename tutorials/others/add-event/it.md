---
name: Aggiungere un evento su Plan B Network
description: Come suggerisco di aggiungere un nuovo evento su Plan B Network?
---
![evento](assets/cover.webp)

La missione di PlanB è fornire risorse educative di primo livello su Bitcoin in quante più lingue possibile. Tutti i contenuti pubblicati sul sito sono open-source e ospitati su GitHub, offrendo a chiunque l'opportunità di contribuire all'arricchimento della piattaforma.

Se vuoi aggiungere una conferenza su Bitcoin al sito della Rete PlanB e aumentare la visibilità del tuo evento, ma non sai come fare? Questo tutorial è per te!
![evento](assets/01.webp)
- Prima di tutto, devi avere un account su GitHub. Se non sai come crearne uno, abbiamo realizzato un tutorial dettagliato per guidarti.

https://planb.network/tutorials/others/create-github-account


- Vai al [repository GitHub di PlanB dedicato ai dati](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) nella sezione `resources/conference/`:
![evento](assets/02.webp)
- Clicca in alto a destra sul pulsante `Add file`, poi su `Create new file`:
![evento](assets/03.webp)
- Se non hai mai contribuito ai contenuti della Rete PlanB prima d'ora, dovrai creare il tuo fork del repository originale. Fare un fork di un repository significa creare una copia di quel repository sul proprio account GitHub, permettendoti di lavorare sul progetto senza influenzare il repository originale. Clicca sul pulsante `Fork this repository`:
![evento](assets/04.webp)
- Arriverai quindi alla pagina di modifica di GitHub:
![evento](assets/05.webp)
- Crea una cartella per la tua conferenza. Per fare ciò, nella casella `Name your file...`, scrivi il nome della tua conferenza in minuscolo con trattini al posto degli spazi. Ad esempio, se la tua conferenza si chiama "Paris Bitcoin Conference", dovresti annotare `paris-bitcoin-conference`. Aggiungi anche l'anno della tua conferenza, per esempio: `paris-bitcoin-conference-2024`:
![evento](assets/06.webp)
- Per validare la creazione della cartella, basta annotare una barra dopo il nome nella stessa casella, per esempio: `paris-bitcoin-conference-2024/`. Aggiungere una barra crea automaticamente una cartella anziché un file:
![evento](assets/07.webp)
- In questa cartella, creerai un primo file YAML chiamato `events.yml`:
![evento](assets/08.webp)
- Compila questo file con le informazioni sulla tua conferenza usando questo modello:

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
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
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Parigi, Francia
  address_line_2: 
  address_line_3: 
  name: Paris Bitcoin Conference 2024
  builder: Paris Bitcoin Conference
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description: La più grande conferenza su Bitcoin in Francia con oltre 8.000 partecipanti ogni anno!
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
Se la tua organizzazione non ha ancora un identificatore "*builder*", puoi aggiungerlo seguendo questo altro tutorial.

https://planb.network/tutorials/others/add-builder



- Una volta terminato di apportare modifiche a questo file, salvali cliccando sul pulsante `Commit changes...`:
![evento](assets/10.webp)
- Aggiungi un titolo per le tue modifiche, così come una breve descrizione:
![evento](assets/11.webp)
- Clicca sul pulsante verde `Propose changes`:
![evento](assets/12.webp)
- Arriverai quindi su una pagina che riassume tutte le tue modifiche:
![evento](assets/13.webp)
- Clicca sulla tua immagine del profilo GitHub in alto a destra, poi su `Your Repositories`:
![evento](assets/14.webp)
- Seleziona il tuo fork del repository PlanB Network:
![evento](assets/15.webp)
- Dovresti vedere una notifica in alto alla finestra con il tuo nuovo ramo. Probabilmente si chiama `patch-1`. Cliccaci sopra:
![evento](assets/16.webp)
- Ora sei sul tuo ramo di lavoro:
![evento](assets/17.webp)
- Torna alla cartella `resources/conference/` e seleziona la cartella della tua conferenza che hai appena creato nel commit precedente:
![evento](assets/18.webp)
- Nella cartella della tua conferenza, clicca sul pulsante `Add file`, poi su `Create new file`:
![evento](assets/19.webp)
- Nominare questa nuova cartella `assets` e confermarne la creazione mettendo una barra `/` alla fine:
![evento](assets/20.webp)
- In questa cartella `assets`, crea un file chiamato `.gitkeep`:
![evento](assets/21.webp)
- Clicca sul pulsante `Commit changes...`:
![evento](assets/22.webp)
- Lascia il titolo del commit come predefinito, e assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:
![evento](assets/23.webp)
- Ritorna alla cartella `assets`:
![evento](assets/24.webp)
- Clicca sul pulsante `Add file`, poi su `Upload files`: ![evento](assets/25.webp)
- Si aprirà una nuova pagina. Trascina e rilascia un'immagine che rappresenta la tua conferenza e che verrà visualizzata sul sito di PlanB Network:
![evento](assets/26.webp)
- Può essere il logo, una miniatura, o anche un poster:
![evento](assets/27.webp)
- Una volta caricata l'immagine, verifica che la casella `Commit directly to the patch-1 branch` sia spuntata, poi clicca su `Commit changes`:
![evento](assets/28.webp)
- Attenzione, la tua immagine deve essere nominata `thumbnail` e deve essere in formato `.webp`. Il nome completo del file dovrebbe quindi essere: `thumbnail.webp`:
![evento](assets/29.webp)
- Ritorna alla tua cartella `assets` e clicca sul file intermedio `.gitkeep`:
![evento](assets/30.webp)
- Una volta sul file, clicca sui 3 piccoli punti in alto a destra poi su `Delete file`:
- Verifica di essere ancora sullo stesso ramo di lavoro, quindi clicca sul pulsante `Commit changes`:
![evento](assets/31.webp)
- Aggiungi un titolo e una descrizione al tuo commit, poi clicca su `Commit changes`:
![evento](assets/32.webp)
- Torna alla radice del tuo repository:
![evento](assets/34.webp)
- Dovresti vedere un messaggio che indica che il tuo ramo ha subito delle modifiche. Clicca sul pulsante `Compare & pull request`:
![evento](assets/35.webp)
- Aggiungi un titolo chiaro e una descrizione al tuo PR:
![evento](assets/36.webp)
- Clicca sul pulsante `Create pull request`:
![evento](assets/37.webp)
Congratulazioni! Il tuo PR è stato creato con successo. Un amministratore lo controllerà e, se tutto è in ordine, lo unirà al repository principale di PlanB Network. Dovresti vedere il tuo evento apparire sul sito web qualche giorno dopo.

Assicurati di seguire il progresso del tuo PR. Un amministratore potrebbe lasciare un commento chiedendo ulteriori informazioni. Fino a quando il tuo PR non è validato, puoi consultararlo nella scheda `Pull requests` sul repository GitHub di PlanB Network:
![evento](assets/38.webp)
Grazie mille per il tuo prezioso contributo! :)


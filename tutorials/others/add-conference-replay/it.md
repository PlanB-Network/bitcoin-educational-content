---
name: Aggiunta di una Replica di Conferenza
description: Come aggiungere una replica di conferenza su PlanB Network?
---
![conference](assets/cover.webp)

La missione di PlanB è fornire risorse educative di primo livello su Bitcoin in quante più lingue possibile. Tutti i contenuti pubblicati sul sito sono open-source e ospitati su GitHub, permettendo a chiunque di contribuire all'arricchimento della piattaforma.

Vuoi aggiungere la replica della tua conferenza su Bitcoin sul sito di PlanB Network e dare visibilità a questo evento, ma non sai come fare? Questo tutorial è per te!

Tuttavia, se desideri aggiungere una conferenza che si svolgerà in futuro, ti consiglio di leggere questo altro tutorial in cui spieghiamo come aggiungere un nuovo evento al sito.

https://planb.network/tutorials/others/add-event


![conference](assets/01.webp)
- Prima di tutto, devi avere un account su GitHub. Se non sai come crearne uno, abbiamo realizzato un tutorial dettagliato per guidarti.

https://planb.network/tutorials/others/create-github-account


- Vai al [repository GitHub di PlanB dedicato ai dati](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) nella sezione `resources/conference/`:
![conference](assets/02.webp)
- Clicca in alto a destra sul pulsante `Add file`, poi su `Create new file`:
![conference](assets/03.webp)
- Se non hai mai contribuito ai contenuti di PlanB Network prima d'ora, dovrai creare il tuo fork del repository originale. Fare il fork di un repository significa creare una copia di quel repository sul proprio account GitHub, il che ti permette di lavorare sul progetto senza influenzare il repository originale. Clicca sul pulsante `Fork this repository`:
![conference](assets/04.webp)
- Arriverai quindi alla pagina di modifica di GitHub:
![conference](assets/05.webp)
- Crea una cartella per la tua conferenza. Per farlo, nella casella `Name your file...`, scrivi il nome della tua conferenza in minuscolo con i trattini al posto degli spazi. Ad esempio, se la tua conferenza si chiama "Paris Bitcoin Conference", dovresti annotare `paris-bitcoin-conference`. Aggiungi anche l'anno della tua conferenza, per esempio: `paris-bitcoin-conference-2024`:
![conference](assets/06.webp)
- Per validare la creazione della cartella, basta annotare una barra dopo il tuo nome nella stessa casella, ad esempio: `paris-bitcoin-conference-2024/`. Aggiungere una barra crea automaticamente una cartella piuttosto che un file:
![conference](assets/07.webp)
- In questa cartella, creerai un primo file YAML denominato `conference.yml`:
![conference](assets/08.webp)
Riempi questo file con le informazioni relative alla tua conferenza utilizzando questo modello:
```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

Ad esempio, il tuo file YAML potrebbe apparire così:

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - International
  - All Public
```

![conference](assets/09.webp)
Se non hai ancora un identificatore "*builder*" per la tua organizzazione, puoi aggiungerlo seguendo quest'altro tutorial.
https://planb.network/tutorials/others/add-builder

- Una volta terminato di apportare modifiche a questo file, salvali cliccando sul pulsante `Commit changes...`:
![conferenza](assets/10.webp)
- Aggiungi un titolo per le tue modifiche, così come una breve descrizione:
![conferenza](assets/11.webp)
- Clicca sul pulsante verde `Propose changes`:
![conferenza](assets/12.webp)
- Arriverai quindi su una pagina che riassume tutte le tue modifiche:
![conferenza](assets/13.webp)
- Clicca sulla tua immagine del profilo GitHub in alto a destra, poi su `Your Repositories`:
![conferenza](assets/14.webp)
- Seleziona il tuo fork del repository PlanB Network:
![conferenza](assets/15.webp)
- Dovresti vedere una notifica in cima alla finestra con il tuo nuovo branch. Probabilmente si chiama `patch-1`. Cliccaci sopra:
![conferenza](assets/16.webp)
- Ora sei sul tuo branch di lavoro:
![conferenza](assets/17.webp)
- Ritorna alla cartella `resources/conference/` e seleziona la cartella della tua conferenza che hai appena creato nel commit precedente:
![conferenza](assets/18.webp)
- Nella cartella della tua conferenza, clicca sul pulsante `Add file`, poi su `Create new file`:
![conferenza](assets/19.webp)
- Nominare questa nuova cartella `assets` e confermare la sua creazione mettendo uno slash `/` alla fine:
![conferenza](assets/20.webp)
- In questa cartella `assets`, crea un file chiamato `.gitkeep`:
![conferenza](assets/21.webp)
- Clicca sul pulsante `Commit changes...`:
![conferenza](assets/22.webp)
- Lascia il titolo del commit come predefinito, e assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:
![conferenza](assets/23.webp)
- Ritorna alla cartella `assets`:
![conferenza](assets/24.webp)
- Clicca sul pulsante `Add file`, poi su `Upload files`:
![conferenza](assets/25.webp)
- Si aprirà una nuova pagina. Trascina e rilascia un'immagine che rappresenta la tua conferenza e che sarà visualizzata sul sito di PlanB Network: ![conferenza](assets/26.webp)
- Può essere un logo, una miniatura, o anche un poster:
![conferenza](assets/27.webp)
- Una volta caricata l'immagine, verifica che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:
![conferenza](assets/28.webp)
- Attenzione, la tua immagine deve essere nominata `thumbnail` e deve essere in formato `.webp`. Il nome completo del file dovrebbe quindi essere: `thumbnail.webp`:
![conferenza](assets/29.webp)
- Ritorna alla tua cartella `assets` e clicca sul file intermediario `.gitkeep`:
![conferenza](assets/30.webp)
- Una volta sul file, clicca sui 3 piccoli punti in alto a destra poi su `Delete file`:
![conferenza](assets/31.webp)
- Verifica di essere ancora sullo stesso branch di lavoro, poi clicca sul pulsante `Commit changes`:
![conferenza](assets/32.webp)
- Aggiungi un titolo e una descrizione al tuo commit, poi clicca su `Commit changes`:
![conferenza](assets/33.webp)
- Torna alla tua cartella della conferenza: ![conference](assets/34.webp)
- Clicca sul pulsante `Aggiungi file`, poi su `Crea nuovo file`:
![conference](assets/35.webp)
- Crea un nuovo file markdown (.md) nominandolo con l'indicatore della tua lingua madre. Questo file sarà utilizzato per le repliche della tua conferenza. Ad esempio, se voglio scrivere le descrizioni delle conferenze in inglese, nominerò questo file en.md:
![conference](assets/36.webp)
- Compila questo file markdown utilizzando questo modello che puoi adattare alla configurazione della tua conferenza:

```markdown
---
name: Conferenza Bitcoin Parigi 2024
description: La più grande conferenza Bitcoin in Francia con oltre 8.000 partecipanti ogni anno!
--- 

# Palco Principale

## Venerdì mattina

![video](https://youtu.be/XXXXXXXXXXXX)

## Venerdì pomeriggio

![video](https://youtu.be/XXXXXXXXXXXX)

## Sabato mattina

![video](https://youtu.be/XXXXXXXXXXXX)

## Sabato pomeriggio

![video](https://youtu.be/XXXXXXXXXXXX)

# Sala Workshop

## Il Futuro del Mining di Bitcoin: Sfide e Innovazioni

![video](https://youtu.be/XXXXXXXXXXXX)

Relatore: Satoshi Nakamoto, Satoshi Nakamoto

## La Privacy è Ancora Possibile Su Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Relatore: Satoshi Nakamoto

## Bitcoin Core: Immersione Profonda nel Codice

![video](https://youtu.be/XXXXXXXXXXXX)

Relatore: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Costruire e Proteggere Portafogli Bitcoin Con Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Relatore: Satoshi Nakamoto
```

![conference](assets/37.webp)
- All'inizio del tuo documento, nella "materia iniziale", compila il campo `name:` con il nome della tua conferenza e l'anno delle repliche. Nel campo `description:` scrivi una breve descrizione del tuo evento nella lingua del file. Ad esempio, per un file denominato `en.md`, la descrizione dovrebbe essere in inglese. Il team di PlanB Network si occuperà di tradurre la tua descrizione utilizzando il loro modello.
- I titoli di primo livello, contrassegnati da un `#`, sono utilizzati per organizzare la conferenza per scene. Ad esempio, `# Palco Principale` per il palco principale e `# Sala Workshop` per uno spazio dedicato ai workshop.

- I titoli di secondo livello, contrassegnati da un doppio `##`, sono utilizzati per separare i diversi video delle repliche. Se le conferenze sono state filmate continuamente per mezza giornata, indica, ad esempio, `## Venerdì mattina`. Se le conferenze sono state filmate e trasmesse individualmente, nomina direttamente la conferenza con un titolo di secondo livello.

- Sotto ogni titolo di secondo livello, inserisci un link al video della replica corrispondente. La sintassi dovrebbe essere: `![video](https://youtu.be/XXXXXXXXXXXX)`, sostituendo `XXXXXXXXXXXX` con il link effettivo del video.

- Se il formato lo consente (conferenze individuali), puoi aggiungere i nomi dei relatori. Per fare ciò, aggiungi il campo `Relatore:` seguito dal nome o pseudonimo del relatore sotto il link del video. In caso di più relatori, separa ogni nome con una virgola, come questo ad esempio: `Relatore: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Una volta completate le modifiche a questo file, salvale cliccando sul pulsante `Commit changes...`:
![conference](assets/38.webp)
- Aggiungi un titolo per le tue modifiche, così come una breve descrizione:
![conference](assets/39.webp)
- Clicca su `Commit changes`: ![conference](assets/40.webp)
- La cartella della tua conferenza dovrebbe ora apparire così: ![conference](assets/41.webp)
- Se tutto è di tuo gradimento, ritorna alla radice del tuo fork: ![conference](assets/42.webp)
- Dovresti vedere un messaggio che indica che il tuo ramo ha subito modifiche. Clicca sul pulsante `Compare & pull request`: ![conference](assets/43.webp)
- Aggiungi un titolo chiaro e una descrizione per la tua PR: ![conference](assets/44.webp)
- Clicca sul pulsante `Create pull request`: ![conference](assets/45.webp)
Congratulazioni! La tua PR è stata creata con successo. Un amministratore la esaminerà ora e, se tutto è in ordine, la fonderà nel repository principale della Rete PlanB. Dovresti vedere le repliche della tua conferenza apparire sul sito web qualche giorno dopo.

Assicurati di seguire il progresso della tua PR. È possibile che un amministratore possa lasciare un commento chiedendo informazioni aggiuntive. Finché la tua PR non è validata, puoi visualizzarla sotto la scheda `Pull requests` sul repository GitHub della Rete PlanB: ![conference](assets/46.webp)

Grazie mille per il tuo prezioso contributo! :)

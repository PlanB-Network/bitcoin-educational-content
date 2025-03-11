---
name: Aggiungere un Podcast alla Rete PlanB
description: Come aggiungere un nuovo podcast alla Rete PlanB?
---
![podcast](assets/cover.webp)

La missione di PlanB è fornire risorse educative di primo livello su Bitcoin in quante più lingue possibile. Tutti i contenuti pubblicati sul sito sono open-source e ospitati su GitHub, permettendo a chiunque di partecipare all'arricchimento della piattaforma.

Stai cercando di aggiungere un podcast su Bitcoin al sito della Rete PlanB e aumentare la visibilità del tuo show, ma non sai come fare? Questo tutorial è per te!
![podcast](assets/01.webp)
- Prima di tutto, devi avere un account GitHub. Se non sai come crearne uno, abbiamo realizzato un tutorial dettagliato per guidarti.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Vai al [repository GitHub di PlanB dedicato ai dati](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) nella sezione `resources/podcasts/`:
![podcast](assets/02.webp)
- Clicca in alto a destra sul pulsante `Add file`, poi su `Create new file`:
![podcast](assets/03.webp)
- Se non hai mai contribuito al contenuto della Rete PlanB prima d'ora, dovrai creare il tuo fork del repository originale. Fare un fork di un repository significa creare una copia di quel repository sul proprio account GitHub, permettendoti di lavorare sul progetto senza influenzare il repository originale. Clicca sul pulsante `Fork this repository`:
![podcast](assets/04.webp)
- Arriverai quindi alla pagina di modifica di GitHub:
![podcast](assets/05.webp)
- Crea una cartella per il tuo podcast. Per fare ciò, nella casella `Name your file...`, scrivi il nome del tuo podcast in minuscolo con i trattini al posto degli spazi. Ad esempio, se il tuo show si chiama "Super Podcast Bitcoin", dovresti scrivere `super-podcast-bitcoin`:
![podcast](assets/06.webp)
- Per validare la creazione della cartella, basta aggiungere una barra dopo il nome del tuo podcast nella stessa casella, per esempio: `super-podcast-bitcoin/`. Aggiungere una barra crea automaticamente una cartella anziché un file:
![podcast](assets/07.webp)
- In questa cartella, creerai un primo file YAML chiamato `podcast.yml`:
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
	- `podcast`: il link al tuo podcast,
	- `twitter`: il link al profilo Twitter del podcast o dell'organizzazione che lo produce,
	- `website`: il link al sito web del podcast o dell'organizzazione che lo produce.
- **`description`**: Aggiungi un breve paragrafo che descrive il tuo podcast. La descrizione deve essere nella stessa lingua indicata nel campo `language:`.
- **`tags`**: Aggiungi due tag associati al tuo podcast. Esempi:
    - `bitcoin`
    - `tecnologia`
    - `economia`
    - `educazione`...

- **`contributors`**: Menciona il tuo ID di contributore se ne possiedi uno.

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
  Super Podcast Bitcoin è una sessione tecnica LIVE tenuta una volta a settimana su Twitter per approfondire il protocollo Bitcoin, le soluzioni di secondo livello e tutto ciò che stupisce. I nostri ospiti Lounes, Pantamis, Loïc e Sosthene risponderanno alle vostre domande e offriranno lo spettacolo più tecnico su Bitcoin al mondo.

tags:
  - bitcoin
  - tecnologia
contributors:
  - rabbit-hole
```

![podcast](assets/09.webp)

- Una volta terminato di apportare modifiche a questo file, salvali cliccando sul pulsante `Commit changes...`:
![podcast](assets/10.webp)
- Aggiungi un titolo per le tue modifiche, così come una breve descrizione:
![podcast](assets/11.webp)
- Clicca sul pulsante verde `Propose changes`:
![podcast](assets/12.webp)
- Arriverai quindi su una pagina che riassume tutte le tue modifiche:
![podcast](assets/13.webp)
- Clicca sulla tua immagine del profilo GitHub in alto a destra, poi su `Your Repositories`:
![podcast](assets/14.webp)
- Seleziona il tuo fork del repository PlanB Network:
![podcast](assets/15.webp)
- Dovresti vedere una notifica in alto alla finestra con il tuo nuovo branch. Probabilmente si chiama `patch-1`. Cliccaci sopra:
![podcast](assets/16.webp)
- Ora sei sul tuo branch di lavoro:
![podcast](assets/17.webp)
- Torna alla cartella `resources/podcast/` e seleziona la cartella del podcast che hai appena creato nel commit precedente: ![podcast](assets/18.webp)
- Nella tua cartella podcast, clicca sul pulsante `Add file`, poi su `Create new file`:
![podcast](assets/19.webp)
- Nominare questa nuova cartella `assets` e confermarne la creazione aggiungendo una barra `/` alla fine:
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
- Si aprirà una nuova pagina. Trascina e rilascia il logo del tuo podcast nell'area indicata. Questa immagine verrà visualizzata sul sito della Rete PlanB: ![podcast](assets/26.webp)
- Attenzione, l'immagine deve essere quadrata, per adattarsi al meglio al nostro sito web: ![podcast](assets/27.webp)
- Una volta caricata l'immagine, verifica che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`: ![podcast](assets/28.webp)
- Attenzione, la tua immagine deve essere denominata `logo` e deve essere in formato `.webp`. Il nome completo del file deve quindi essere: `logo.webp`: ![podcast](assets/29.webp)
- Torna alla tua cartella `assets` e clicca sul file intermedio `.gitkeep`: ![podcast](assets/30.webp)
- Una volta sul file, clicca sui tre piccoli punti in alto a destra e poi su `Delete file`: ![podcast](assets/31.webp)
- Verifica di essere ancora sullo stesso ramo di lavoro, poi clicca sul pulsante `Commit changes`: ![podcast](assets/32.webp)
- Aggiungi un titolo e una descrizione al tuo commit, poi clicca su `Commit changes`: ![podcast](assets/33.webp)
- Torna alla radice del tuo repository: ![podcast](assets/34.webp)
- Dovresti vedere un messaggio che indica che il tuo ramo ha subito delle modifiche. Clicca sul pulsante `Compare & pull request`: ![podcast](assets/35.webp)
- Aggiungi un titolo chiaro e una descrizione al tuo PR: ![podcast](assets/36.webp)
- Clicca sul pulsante `Create pull request`: ![podcast](assets/37.webp)
Congratulazioni! Il tuo PR è stato creato con successo. Un amministratore lo esaminerà ora e, se tutto è in ordine, lo unirà al repository principale della Rete PlanB. Dovresti vedere apparire il tuo podcast sul sito web qualche giorno dopo.

Assicurati di seguire il progresso del tuo PR. Un amministratore potrebbe lasciare un commento chiedendo ulteriori informazioni. Finché il tuo PR non è validato, puoi visualizzarlo nella scheda `Pull requests` sul repository GitHub della Rete PlanB: ![podcast](assets/38.webp)
Grazie mille per il tuo prezioso contributo! :)

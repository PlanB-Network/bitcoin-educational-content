---
name: Aggiungere un Libro alla Rete PlanB
description: Come aggiungere un nuovo libro alla Rete PlanB?
---
![book](assets/cover.webp)

La missione di PlanB è fornire risorse educative di primo livello su Bitcoin in quante più lingue possibile. Tutti i contenuti pubblicati sul sito sono open-source e ospitati su GitHub, permettendo a chiunque di contribuire all'arricchimento della piattaforma.

**Vuoi aggiungere un libro relativo a Bitcoin sul sito della Rete PlanB e aumentare la visibilità del tuo lavoro, ma non sai come fare? Questo tutorial è per te!**
![book](assets/01.webp)
- Prima di tutto, devi avere un account GitHub. Se non sai come crearne uno, abbiamo realizzato un tutorial dettagliato per guidarti.

https://planb.network/tutorials/others/create-github-account


- Vai al [repository GitHub di PlanB dedicato ai dati](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books) nella sezione `resources/books/`:
![book](assets/02.webp)
- Clicca in alto a destra sul pulsante `Add file`, poi su `Create new file`:
![book](assets/03.webp)
- Se non hai mai contribuito ai contenuti della Rete PlanB prima d'ora, dovrai creare il tuo fork del repository originale. Fare un fork di un repository significa creare una copia di quel repository sul proprio account GitHub, permettendoti di lavorare sul progetto senza influenzare il repository originale. Clicca sul pulsante `Fork this repository`:
![book](assets/04.webp)
- Arriverai quindi alla pagina di modifica di GitHub:
![book](assets/05.webp)
- Crea una cartella per il tuo libro. Per fare ciò, nella casella `Name your file...`, scrivi il nome del tuo libro in minuscolo con i trattini al posto degli spazi. Ad esempio, se il tuo libro si chiama "*Il Mio Libro su Bitcoin*", dovresti annotare `il-mio-libro-su-bitcoin`:
![book](assets/06.webp)
- Per validare la creazione della cartella, basta aggiungere una barra dopo il nome del tuo libro nella stessa casella, per esempio: `il-mio-libro-su-bitcoin/`. Aggiungere una barra crea automaticamente una cartella anziché un file:
![book](assets/07.webp)
- In questa cartella, creerai un primo file YAML denominato `book.yml`:
![book](assets/08.webp)
- Compila questo file con le informazioni sul tuo libro usando questo modello:

```yaml
author: 
level: 
tags:
  - 
  - 
```

Ecco i dettagli da compilare per ogni campo:
- **`author`**: Indica il nome dell'autore del libro.
- **`level`**: Indica il livello richiesto per poter leggere e comprendere bene il libro. Scegli un livello tra i seguenti:
	- `beginner`
	- `intermediate`
- `advanced` - `expert`
- **`tags`**: Aggiungi due o tre tag relativi al tuo libro. Ad esempio:
    - `bitcoin`
    - `storia`
    - `tecnologia`
    - `economia`
    - `educazione`...

Ad esempio, il tuo file YAML potrebbe apparire così:

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - tecnologia
```

![book](assets/09.webp)
- Una volta terminato di apportare modifiche a questo file, salvalo cliccando sul pulsante `Commit changes...`:
![book](assets/10.webp)
- Aggiungi un titolo per le tue modifiche, così come una breve descrizione: ![book](assets/11.webp)
- Clicca sul pulsante verde `Propose changes`:
![book](assets/12.webp)
- Arriverai quindi su una pagina che riassume tutte le tue modifiche:
![book](assets/13.webp)
- Clicca sull'immagine del tuo profilo GitHub in alto a destra, poi su `Your Repositories`:
![book](assets/14.webp)
- Seleziona il tuo fork del repository PlanB Network:
![book](assets/15.webp)
- Dovresti vedere una notifica in cima alla finestra con il tuo nuovo branch. Probabilmente si chiama `patch-1`. Cliccaci sopra:
![book](assets/16.webp)
- Ora sei sul tuo branch di lavoro:
![book](assets/17.webp)
- Torna alla cartella `resources/books/` e seleziona la cartella del tuo libro che hai appena creato nel commit precedente:
![book](assets/18.webp)
- Nella cartella del tuo libro, clicca sul pulsante `Add file`, poi su `Create new file`:
![book](assets/19.webp)
- Nominare questa nuova cartella `assets` e confermarne la creazione mettendo uno slash `/` alla fine:
![book](assets/20.webp)
- In questa cartella `assets`, crea un file chiamato `.gitkeep`:
![book](assets/21.webp)
- Clicca sul pulsante `Commit changes...`:
![book](assets/22.webp)
- Lascia il titolo del commit come predefinito, e assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:
![book](assets/23.webp)
- Ritorna alla cartella `assets`:
![book](assets/24.webp)
- Clicca sul pulsante `Add file`, poi su `Upload files`:
![book](assets/25.webp)
- Si aprirà una nuova pagina. Trascina e rilascia l'immagine di copertina del tuo libro nell'area. Questa immagine verrà visualizzata sul sito di PlanB Network:
![book](assets/26.webp)
- Attenzione, l'immagine deve essere nel formato di un libro, per adattarsi al meglio al nostro sito web, come per esempio:
![book](assets/27.webp)
- Una volta caricata l'immagine, assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:
![book](assets/28.webp)- Si prega di notare, la tua immagine deve essere nominata `cover_en` se la copertina è in inglese e deve essere in formato `.webp`. Pertanto, il nome completo del file dovrebbe essere `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, ecc. Se desideri utilizzare un'immagine di copertina diversa per ogni lingua, ad esempio in caso di traduzione di un libro, puoi posizionarle nella stessa posizione nella cartella `assets`:
![book](assets/29.webp)
- Torna alla tua cartella `assets` e clicca sul file intermedio `.gitkeep`:
![book](assets/30.webp)
- Una volta sul file, clicca sui 3 piccoli punti in alto a destra e poi su `Delete file`:
![book](assets/31.webp)
- Assicurati di essere ancora sullo stesso branch di lavoro, poi clicca sul pulsante `Commit changes...`:
![book](assets/32.webp)
- Aggiungi un titolo e una descrizione al tuo commit, poi clicca su `Commit changes`:
![book](assets/33.webp)
- Ritorna alla cartella del tuo libro: ![libro](assets/34.webp)
- Clicca sul pulsante `Aggiungi file`, poi su `Crea nuovo file`:
![libro](assets/35.webp)
- Crea un nuovo file YAML nominandolo con l'indicatore della lingua del libro. Questo file verrà utilizzato per la descrizione del libro. Ad esempio, se voglio scrivere la mia descrizione in inglese, nominerò questo file `en.yml`:
![libro](assets/36.webp)
- Compila questo file YAML utilizzando questo modello:
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

Ecco i dettagli da compilare per ogni campo:
- **`title`**: Indica il nome del libro tra virgolette.
- **`publication_year`**: Indica l'anno di pubblicazione del libro.
- **`cover`**: Indica il nome del file corrispondente all'immagine di copertina, in conformità con la lingua del file YAML che stai attualmente modificando. Ad esempio, se stai modificando il file `en.yml` e hai precedentemente aggiunto l'immagine di copertina in inglese intitolata `cover_en.webp`, indica semplicemente `cover_en.webp` in questo campo.
- **`description`**: Aggiungi un breve paragrafo che descrive il libro. La descrizione deve essere nella stessa lingua indicata nel titolo del file YAML.
- **`contributors`**: Aggiungi il tuo ID di contributore se ne possiedi uno.

Ad esempio, il tuo file YAML potrebbe apparire così:

```yaml
title: "Il Mio Libro su Bitcoin"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
Scopri il mondo rivoluzionario di Bitcoin con questa guida completa pensata per i principianti. Il Mio Libro su Bitcoin svela le complessità di Bitcoin, fornendo un'introduzione chiara e concisa su come funziona il protocollo. Dalla sua tecnologia rivoluzionaria al suo potenziale impatto sull'economia globale, questo libro offre preziose intuizioni e conoscenze pratiche. Perfetto per chi è nuovo a Bitcoin, copre le basi, consigli sulla sicurezza e il futuro della finanza digitale. Immergiti nel futuro del denaro e dotati della conoscenza per navigare con fiducia nell'era digitale.

contributors:
  - pretty-private

![libro](assets/37.webp)
- Clicca sul pulsante `Commit changes...`:
![libro](assets/38.webp)
- Assicurati che la casella `Commit direttamente sul branch patch-1` sia selezionata, aggiungi un titolo, poi clicca su `Commit changes`:
![libro](assets/39.webp)
- La cartella del libro dovrebbe ora apparire così:
![libro](assets/40.webp)
- Se tutto ti sembra corretto, ritorna alla radice del tuo fork:
![libro](assets/41.webp)
- Dovresti vedere un messaggio che indica che il tuo branch è stato modificato. Clicca sul pulsante `Compara & crea pull request`:
![libro](assets/42.webp)
- Aggiungi un titolo chiaro e una descrizione al tuo PR:
![libro](assets/43.webp)
- Clicca sul pulsante `Crea pull request`:
![libro](assets/44.webp)
Congratulazioni! Il tuo PR è stato creato con successo. Un amministratore lo esaminerà ora e, se tutto è in ordine, lo unirà al repository principale della Rete PlanB. Dovresti vedere apparire il tuo libro sul sito web qualche giorno dopo.

Assicurati di seguire il progresso del tuo PR. Un amministratore potrebbe lasciare un commento chiedendo ulteriori informazioni. Fintanto che il tuo PR non è validato, puoi visualizzarlo nella scheda `Pull requests` sul repository GitHub della Rete PlanB.
Grazie mille per il tuo prezioso contributo! :)

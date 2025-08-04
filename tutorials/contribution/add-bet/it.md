---
name: Aggiungere risorse al "BET"
description: Come aggiungere nuovi materiali educativi su Plan ₿ Network?
---

![event](assets/cover.webp)

La missione di Plan ₿ Network è mettere a disposizione degli utenti risorse educative di primo livello su Bitcoin, in quante più lingue possibile. Tutti i contenuti pubblicati sul sito sono open-source e si trovano su GitHub: ciò consente a chiunque di partecipare all'arricchimento della piattaforma.

Oltre a tutorial e corsi, Plan ₿ Network offre anche una vasta biblioteca di contenuti educativi vari su Bitcoin, accessibili a tutti, [nella sezione "BET" (_Bitcoin Educational Toolkit_)](https://planb.network/resources/bet). Questo database include poster, meme, poster umoristici, diagrammi tecnici, loghi e altri strumenti a disposizione degli utenti. L'obiettivo di questa iniziativa è supportare persone e gruppi in tutto il mondo nell'insegnamento di Bitcoin, fornendo loro le risorse visive necessarie.

Vuoi partecipare all'arricchimento di questo database, ma non sai come fare? Questo tutorial è per te!

*È imperativo che tutti i contenuti integrati nel sito siano liberi da copyright o rispettino la licenza del file sorgente. Inoltre, tutti i contenuti visivi pubblicati su Plan ₿ Network sono resi disponibili con licenza [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*

![event](assets/01.webp)

- Prima di tutto, è necessario avere un account su GitHub. Se non sai come crearne uno, abbiamo realizzato un tutorial dettagliato per guidarti.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Vai al [repository GitHub di PlanB dedicato](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) nella sezione `resources/bet/`:

![event](assets/02.webp)

- Clicca in alto a destra sul pulsante `Add file`, poi su `Create new file`:

![event](assets/03.webp)

- Se non hai mai aggiunto contenuti sul sito di Plan ₿ Network prima d'ora, dovrai creare il tuo fork del repository originale. Fare un fork di un repository significa creare una copia dello stesso sul proprio account GitHub, il che ti consente di lavorare sul progetto senza influenzare il repository originale. Clicca sul pulsante `Fork this repository`:

![event](assets/04.webp)

- Arriverai quindi alla pagina di modifica di GitHub:

![event](assets/05.webp)

- Crea una cartella per il tuo contenuto. Per fare ciò, nella casella `Name your file...`, scrivi il nome del tuo contenuto in minuscolo usando i trattini al posto degli spazi. Nel mio esempio, supponiamo che io voglia aggiungere un PDF che contiene la lista di 2048 parole del BIP39. Quindi, chiamerò la mia cartella `bip39-wordlist`:

![event](assets/06.webp)

- Per confermare la creazione della cartella, basta aggiungere uno slash `/` dopo il nome nella stessa casella, per esempio: `bip39-wordlist/`. Aggiungere uno slash crea automaticamente una cartella anziché un file:
  
![event](assets/07.webp)

- In questa cartella, creerai un primo file YAML denominato `bet.yml`:
  
![event](assets/08.webp)

- Compila questo file con le informazioni relative al tuo contenuto usando questo modello:

```yaml
project: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```
- **`project`**: indica l'identificativo della tua azienda, o progetto su Plan ₿ Network. Se non hai ancora un identificativo, puoi crearne uno seguendo questo tutorial.

https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

 Se non ne possiedi uno, puoi semplicemente usare il tuo nome, il tuo pseudonimo o il nome della tua azienda, senza aver creato un profilo nella sezione progetti.

- **`type`**: seleziona la natura del tuo contenuto tra le seguenti due opzioni:
	- `Educational Content` per contenuti educativi.
	- `Visual Content` per altri tipi di contenuti.

- **`links`**: fornisci i link che collegano ai tuoi contenuti. Hai due opzioni:
	- Se scegli di inserire direttamente il tuo contenuto sul GitHub di Plan ₿ Network, dovrai aggiungere i link a questo file durante i passaggi successivi.
	- Se i tuoi contenuti sono inseriti altrove, ad esempio sul tuo sito web personale, indica qui i link corrispondenti:
	    - `download`: Un link per scaricare il tuo contenuto.
	    - `view`: Un link per visualizzare il tuo contenuto (può essere lo stesso del link di download). Se il tuo contenuto è disponibile in più lingue, aggiungi un link per ogni lingua.

- **`tags`**: Aggiungi due tag associati al tuo contenuto. Esempi:
	- bitcoin
	- tecnologia
	- economia
	- educazione
	- meme...

- **`contributors`**: menziona il tuo identificativo di contributor se ne hai uno.

Ad esempio, il tuo file YAML potrebbe apparire così:

```yaml
project: Plan ₿ Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
```

- Nel mio esempio, lascerò i link vuoti per ora, poiché aggiungerò il mio PDF direttamente su GitHub:

![event](assets/09.webp)

- Una volta completate le modifiche a questo file, salvale cliccando sul pulsante `Commit changes...`:

![event](assets/10.webp)

- Aggiungi un titolo per le tue modifiche, così come una breve descrizione:

![event](assets/11.webp)

- Clicca sul pulsante verde `Propose changes`:

![event](assets/12.webp)

- Arriverai quindi su una pagina che riassume tutte le tue modifiche:

![event](assets/13.webp)

- Clicca sulla tua immagine di profilo GitHub in alto a destra, poi su `Your Repositories`:

![event](assets/14.webp)

- Seleziona il tuo fork del repository Plan ₿ Network:

![event](assets/15.webp)

- Dovresti vedere una notifica in alto con il tuo nuovo branch. Probabilmente si chiama `patch-1`. Cliccaci sopra:

![event](assets/16.webp)

- Ora sei sul tuo branch di lavoro (**assicurati di essere sullo stesso branch delle tue modifiche precedenti, questo è importante!**):

![event](assets/17.webp)

- Torna alla cartella `resources/bet/` e seleziona la cartella del contenuto che hai appena creato nel commit precedente:

![event](assets/18.webp)

- Nella cartella del tuo contenuto, clicca sul pulsante `Add file`, poi su `Create new file`:

![event](assets/19.webp)

- Nominare questa nuova cartella `assets` e confermarne la creazione mettendo uno slash `/` alla fine:

![event](assets/20.webp)

- In questa cartella `assets`, crea un file chiamato `.gitkeep`:

![event](assets/21.webp)


- Clicca sul pulsante `Commit changes...`:

![event](assets/22.webp)

- Lascia il titolo del commit come predefinito e assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:

![event](assets/23.webp)

- Ritorna alla cartella `assets`:

![event](assets/24.webp)

- Clicca sul pulsante `Add file`, poi su `Upload files`:

![event](assets/25.webp)

- Si aprirà una nuova pagina.

Trascina e rilascia nell'area una immagine che rappresenta il tuo contenuto. Questa immagine verrà visualizzata sul sito di Plan ₿ Network:

![event](assets/26.webp)

- Può essere un'anteprima, un logo o un'icona:

![event](assets/27.webp)

- Una volta caricata l'immagine, assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:

![event](assets/28.webp)

- Attenzione, la tua immagine deve essere nominata `logo` e deve essere in formato `.webp`. Il nome completo del file deve quindi essere: `logo.webp`:

![event](assets/29.webp)

- Ritorna alla tua cartella `assets` e clicca sul file intermedio `.gitkeep`:

![event](assets/30.webp)

- Una volta sul file, clicca sui tre piccoli punti in alto a destra poi su `Delete file`:

![event](assets/31.webp)

- Assicurati di essere ancora sullo stesso ramo di lavoro, poi clicca sul pulsante `Commit changes`:

![event](assets/32.webp)

- Aggiungi un titolo e una descrizione al tuo commit, poi clicca su `Commit changes`:

![event](assets/33.webp)

- Ritorna alla cartella del tuo contenuto:

![event](assets/34.webp)

- Clicca sul pulsante `Add file`, poi su `Create new file`:

![event](assets/35.webp)

- Crea un nuovo file YAML nominandolo con l'indicatore della tua lingua madre. Questo file verrà utilizzato per la descrizione del contenuto. Ad esempio, se voglio scrivere la mia descrizione in inglese, nominerò questo file `en.yml`:

![event](assets/36.webp)

- Compila questo file YAML utilizzando questo template:

```yaml
name: 
description: |
  
```

- Per la chiave `name`, puoi aggiungere il nome del tuo contenuto;
- Per la chiave `description`, devi semplicemente aggiungere un breve paragrafo che descrive il tuo contenuto. La descrizione deve essere nella stessa lingua del nome del file. Non è necessario tradurre questa descrizione in tutte le lingue supportate sul sito, poiché il team di Plan ₿ lo faranno successivamente.

Ad esempio, ecco come potrebbe apparire il tuo file:

```yaml
name: BIP39 WORDLIST
description: |
  Lista completa e numerata delle 2048 parole inglesi del dizionario BIP39 utilizzate per codificare le frasi mnemoniche. Il documento può essere stampato su una singola pagina.
```

![event](assets/37.webp)

- Clicca sul pulsante `Commit changes...`:

![event](assets/38.webp)

- Assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, aggiungi un titolo, poi clicca su `Commit changes`:

![event](assets/39.webp)

- La cartella del tuo contenuto dovrebbe ora apparire così:

![event](assets/40.webp)

*Se preferisci non aggiungere il contenuto su GitHub e hai già annotato i link nel file `bet.yml` durante i passaggi precedenti, puoi saltare questa sezione e andare direttamente alla parte relativa alla creazione della Pull Request.*

- Torna alla cartella `/assets`:

![evento](assets/41.webp)

- Clicca sul pulsante `Add file`, poi su `Upload files`:

![evento](assets/42.webp)

- Si aprirà una nuova pagina. Trascina e rilascia nell'area il contenuto che desideri condividere:

![evento](assets/43.webp)

- Ad esempio, ho aggiunto il file PDF della lista BIP39:

![evento](assets/44.webp)

- Una volta caricato il contenuto, assicurati che la casella `Commit directly to the patch-1 branch` sia selezionata, poi clicca su `Commit changes`:

![evento](assets/45.webp)

- Torna alla tua cartella `/assets` e clicca sul file che hai appena caricato:

![evento](assets/46.webp)

- Recupera l'URL del tuo file. Ad esempio, nel mio caso, l'URL è:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Mantieni solo l'ultima parte dell'URL da `/resources` in poi:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Aggiungi le seguenti informazioni alla base dell'URL per avere il link corretto:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

Quello che stiamo facendo qui è anticipare il futuro link al tuo file, una volta che la tua proposta sarà stata "mergiata" al repository sorgente di Plan ₿ Network.

- Torna al tuo file `bet.yml` e clicca sull'icona della matita:

- ![evento](assets/47.webp)

- Aggiungi lì il tuo link:

![evento](assets/48.webp)

- Una volta completate le modifiche, clicca sul pulsante `Commit changes...`:

![evento](assets/49.webp)

- Aggiungi un titolo per le tue modifiche, così come una breve descrizione:

![evento](assets/50.webp)

- Clicca sul pulsante verde `Commit changes`:

![evento](assets/51.webp)

---

- Se tutto ti sembra corretto, torna al tuo fork:

![evento](assets/52.webp)

- Dovresti vedere un messaggio che indica che il tuo branch è stato modificato. Clicca sul pulsante `Compare & pull request`:


![evento](assets/53.webp)

- Aggiungi un titolo chiaro e una descrizione per la tua PR:

![evento](assets/54.webp)

- Clicca sul pulsante `Create pull request`:

![evento](assets/55.webp)

Congratulazioni! La tua PR è stata creata con successo. Un coordinatore del team la esaminerà e, se tutto è in ordine, la unirà al repository principale di Plan ₿ Network. Dovresti vedere il tuo BET apparire sul sito web qualche giorno dopo.

Assicurati di seguire il progresso della tua PR. Un admin potrebbe lasciare un commento chiedendo ulteriori informazioni. Fintanto che la tua PR non è validata, puoi consultarla nella scheda "Pull requests" sul repository GitHub di Plan ₿ Network:

![evento](assets/56.webp)

Grazie mille per il tuo prezioso contributo! :)


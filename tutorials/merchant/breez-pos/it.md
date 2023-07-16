---
name: Punto vendita Breez

description: Guida per iniziare ad accettare bitcoin utilizzando Breez POS
---

![cover](assets/cover.jpeg)

# Punto vendita Breez

_Il testo proviene dal sito di documentazione di Breez: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_

## Cos'è Breez POS?

**Breez** è un'app Lightning a servizio completo e non custodiale. Vediamo nel dettaglio:

- **Lightning** è una rete di pagamento bitcoin che riduce i tempi di transazione da minuti a millisecondi e le commissioni di transazione da diversi dollari a pochi centesimi o meno. Lightning trasforma il bitcoin da oro digitale in valuta digitale, preservando tutti i vantaggi che rendono il bitcoin eccezionale.
- **Non custodiale** significa che Breez non prende possesso dei soldi degli utenti. Molte app Lightning prendono possesso dei soldi dei loro utenti. Sono essenzialmente banche di bitcoin. Con un'app non custodiale come Breez, tutti gli utenti sono le proprie banche.
- **A servizio completo** significa che Breez si occupa automaticamente e in background di quasi tutte le operazioni tecniche. Cose come la creazione di canali, la liquidità in entrata e il routing rimangono sotto il cofano. (Ma Breez è anche open source, quindi chiunque sia interessato a verificare la tecnologia è il benvenuto a farlo!)

**Breez POS** è l'abbreviazione della nostra modalità punto vendita. In altre parole, Breez funziona come una cassa digitale per aziende e commercianti che desiderano accettare pagamenti Lightning (oltre alla sua modalità "standard", che è come la versione digitale di un portafoglio in pelle per bitcoin, e un lettore di podcast di nuova generazione). Ora vediamo come configurare Breez come una cassa Lightning per la tua attività.

## Come iniziare con Breez?

1. Il primo passo è scaricare l'app. È disponibile per Android e iOS (installa TestFlight e clicca sul link dal tuo dispositivo).
2. Breez può eseguire automaticamente il backup su Google Drive, iCloud o qualsiasi server WebDav.
   > Nota che ogni dispositivo esegue il proprio nodo Lightning. Puoi eseguire la modalità POS su quanti dispositivi desideri, ma i saldi rimarranno separati.
3. Con l'app aperta, clicca sull'icona in alto a sinistra per trovare la modalità Punto vendita.

## Configurazione POS

1. Clicca su quell'icona in alto a sinistra e poi su Punto vendita > Impostazioni POS.

### La password del manager

Nelle Impostazioni POS, hai la possibilità di creare una password del manager. La password del manager rende impossibile inviare pagamenti in uscita dall'app Breez senza autorizzazione. Il personale di vendita potrà solo ricevere pagamenti dal dispositivo. Nota che se utilizzi questa opzione, potresti voler impedire l'accesso al backup di Breez, quindi si consiglia di utilizzare un account WebDav esterno (ad esempio, Nextcloud) per questo caso d'uso.

### Elenco degli articoli

L'elenco degli articoli è un catalogo di articoli in vendita e dei loro prezzi. Ci sono due modi per aggiungere articoli all'elenco:

- Per inserire articoli uno alla volta, clicca su Articoli in alto nella vista principale del POS, quindi sul segno "+" in basso a destra. Qui puoi inserire il nome di un singolo tipo di articolo, il prezzo (visualizzato nell'equivalente della valuta di tua scelta) e l'SKU (un identificatore interno univoco per quel tipo di articolo; è facoltativo).
- Per inserire molti articoli contemporaneamente, clicca sull'icona della calcolatrice in alto a sinistra, poi Punto Vendita > Preferenze > Impostazioni POS, e poi clicca sui tre puntini a destra di Elenco Articoli, e infine su Importa da CSV. Questo ti permetterà di importare un file CSV che hai preparato in anticipo contenente i nomi, i prezzi e gli SKU dei tuoi articoli.

### Visualizzazione Fiat

Breez invia e riceve solo bitcoin e per la maggior parte delle transazioni su Lightning, che tendono ad essere di importi più piccoli, la somma viene di solito visualizzata in Satoshis, anche chiamati sats (1 BTC = 100.000.000 sats). Tuttavia, molti commercianti trovano pratico poter vedere (e comunicare ai clienti) il valore dell'acquisto visualizzato nella valuta fiat locale.

Nella visualizzazione principale del POS, la valuta attualmente visualizzata è visibile sul lato destro (il valore predefinito è SAT). C'è anche un elenco a discesa di altre valute disponibili per la visualizzazione. Per aggiungere o rimuovere valute da questo elenco a discesa, clicca su Punto Vendita > Preferenze > Valute Fiat. Poi semplicemente spunta le valute che desideri avere nel tuo menu a discesa e deseleziona quelle che desideri omettere.

I valori visualizzati provengono da yadio, una fonte autorevole di dati sui tassi di cambio, e vengono aggiornati quasi in tempo reale. Ma ricorda: qualunque sia il valore della valuta attualmente visualizzato, il pagamento stesso è in bitcoin.

### Addebitare un Ordine

Per comporre l'ordine, aggiungi gli articoli dall'elenco degli articoli o semplicemente inserisci una somma nella tastiera. Poi clicca su Addebita in alto nella visualizzazione principale del POS. Vedrai quindi un codice QR che il cliente può scansionare con la sua app Lightning, che puoi condividere direttamente da un'altra app sul tuo dispositivo o che puoi copiare e incollare dove necessario.

Scansionando quel codice o cliccando sulla fattura condivisa/incollata, il cliente vedrà la fattura nella sua app Lightning e avrà l'opzione di pagarla e liquidare immediatamente la transazione.

Una volta che vedi l'animazione Pagamento approvato! nell'app Breez sul dispositivo del commerciante, puoi cliccare sull'icona della stampante per generare una ricevuta per il cliente. Per utilizzare una stampante per ricevute su Android, prova a utilizzare questo driver. Nota che puoi anche stampare transazioni passate tramite la schermata Transazioni.

### Rapporto di Vendita

Per visualizzare un rapporto giornaliero/settimanale/mensile delle tue vendite (per scopi contabili o altri), clicca sull'icona in alto a sinistra, e poi clicca su Transazioni. Clicca sull'icona Rapporto per visualizzare il rapporto e sull'icona Calendario per cambiare l'intervallo di date selezionato.

### Esportazione delle Transazioni

Per visualizzare un elenco dei pagamenti ricevuti in Breez, clicca sull'icona in alto a sinistra, e poi clicca su Transazioni. Clicca sui tre puntini in alto a destra, poi su Esporta per esportare un elenco di pagamenti in entrata in formato CSV. Per limitare l'elenco a un certo periodo di tempo, clicca sull'icona del calendario per impostare un intervallo di date.

### Stampa delle Ricevute

Per stampare una ricevuta di vendita, clicca sull'icona di stampa in alto a destra del dialogo di conferma del pagamento. In alternativa, clicca sull'icona in alto a sinistra, e poi clicca su Transazioni. Trova la vendita da stampare, aprila e clicca sull'icona di stampa in alto a destra.

> Nota: utilizza questo driver per stampare su una stampante termica portatile Bluetooth/USB da 58mm/80mm.

## Voglio saperne di più

- Per ulteriori informazioni su Lightning e Breez, visita il nostro [blog](https://breez.technology/blog).
- Per ulteriori suggerimenti tecnici su come ottenere il massimo dall'app e svolgere operazioni comuni, consulta la nostra [documentazione](https://breez.technology/documentation).
- Se ti trovi in difficoltà e non riesci a trovare la risposta in nessuno dei nostri materiali di aiuto, puoi trovarci su [Telegram](https://t.me/breez_labs) o inviarci una [email](mailto:support@breez.technology).
- Se vuoi vedere alcuni video dimostrativi della modalità POS di Breez in azione realizzati dai nostri fan e utenti, [qui](https://www.youtube.com/watch?v=xxxx) ne trovi uno breve e [qui](https://www.youtube.com/watch?v=xxxx) uno più lungo e dettagliato.

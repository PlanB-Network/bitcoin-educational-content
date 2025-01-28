---
name: COLDCARD Q - Avanzato
description: Utilizzo delle opzioni avanzate di COLDCARD Q
---
![cover](assets/cover.webp)

In una precedente esercitazione abbiamo trattato la configurazione iniziale della COLDCARD Q e le sue funzioni di base per i principianti. Se avete appena ricevuto la vostra COLDCARD Q e non l'avete ancora configurata, vi consiglio di iniziare con questa esercitazione prima di continuare qui:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
Questo nuovo tutorial è dedicato alle opzioni avanzate di COLDCARD Q, pensate per gli utenti più esperti e paranoici. Infatti, le COLDCARD si distinguono dagli altri portafogli hardware per le numerose funzioni di sicurezza avanzate. Naturalmente, non è necessario utilizzare tutte queste opzioni. Basta scegliere quelle che si adattano alla vostra strategia di sicurezza.

**Attenzione**, l'uso scorretto di alcune di queste opzioni avanzate può causare la perdita dei bitcoin o la distruzione del portafoglio hardware. Si raccomanda pertanto di leggere attentamente i consigli e le spiegazioni di ciascuna opzione.

Prima di iniziare, assicuratevi di avere accesso a un backup fisico della vostra frase mnemonica di 12 o 24 parole e verificatene la validità tramite il seguente menu: `Avanzate/Strumenti > Zona di pericolo > Funzioni di semina > Visualizza parole di semina`.

![CCQ](assets/fr/01.webp)

## La passphrase BIP39

Se non sapete cos'è una passphrase BIP39 o se non vi è del tutto chiaro il suo funzionamento, vi consiglio vivamente di dare prima un'occhiata a questo tutorial, che copre le basi teoriche necessarie per comprendere i rischi associati all'uso di una passphrase:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Tenete presente che una volta impostata la passphrase sul vostro portafoglio, il mnemonico da solo non sarà sufficiente per riottenere l'accesso ai vostri bitcoin. Avrete bisogno sia del mnemonico che della passphrase. Inoltre, dovrete inserire la passphrase ogni volta che sbloccherete la vostra COLDCARD Q. Questo aumenta la sicurezza rendendo insufficiente l'accesso fisico alla COLDCARD e la conoscenza del PIN senza la passphrase.

Sulle COLDCARD sono disponibili due opzioni per la gestione della passphrase:

1. **Immissione classica:** La passphrase viene immessa manualmente ogni volta che si utilizza il portafoglio hardware, proprio come si fa con altri portafogli hardware. COLDCARD Q semplifica questo compito grazie alla sua tastiera completa.

2. **È possibile scegliere di criptare la passphrase e memorizzarla su una scheda microSD. In questo caso, sarà necessario inserire la microSD nella COLDCARD Q ogni volta che la si utilizza. Si noti che questa microSD funzionerà solo sulla COLDCARD Q e non è un backup. È quindi molto importante conservare una copia della passphrase su un supporto fisico, come carta o metallo.

Per impostare la passphrase del BIP39, accedere al menu "*Passphrase*".

![CCQ](assets/fr/02.webp)

Immettere la passphrase utilizzando la tastiera. Assicuratevi di scegliere una passphrase forte (lunga e casuale) e di effettuare un backup fisico.

![CCQ](assets/fr/03.webp)

Una volta impostata la passphrase, COLDCARD Q mostrerà l'impronta della chiave master del nuovo portafoglio associato alla passphrase. Assicuratevi di salvare questa impronta. Quando in futuro userete nuovamente il dispositivo, potrete verificare che l'impronta digitale visualizzata corrisponda a quella salvata. Questo controllo assicura che non si sia commesso alcun errore nell'inserimento della passphrase.

![CCQ](assets/fr/04.webp)

A questo punto è possibile premere "*INVIO*" per applicare la passphrase alla frase mnemonica e attivare il nuovo portafoglio. Se si preferisce salvare la passphrase su una microSD, inserire la scheda nell'apposito slot e premere "*1*".

![CCQ](assets/fr/05.webp)

La passphrase è stata applicata. L'impronta della chiave appare nella schermata iniziale e nella parte superiore dello schermo.

![CCQ](assets/fr/06.webp)

Ogni volta che si sblocca la COLDCARD Q, è necessario accedere al menu "*Passphrase*" e inserire la passphrase come sopra, per applicarla al mnemonico memorizzato nel dispositivo e accedere al portafoglio Bitcoin corretto.

![CCQ](assets/fr/07.webp)

Se avete salvato la passphrase su una scheda microSD, ogni volta che la utilizzate, inseritela nella COLDCARD e accedete al menu "*Passphrase*". La COLDCARD caricherà la passphrase direttamente dalla microSD, quindi non sarà necessario inserirla manualmente. Fate clic su "*Ripristina salvato*".

![CCQ](assets/fr/08.webp)

Verificare che la lunghezza e la prima lettera della passphrase caricata siano corrette.

![CCQ](assets/fr/09.webp)

Confermate che l'impronta digitale visualizzata corrisponda a quella del vostro portafoglio e cliccate su "*Ripristina*".

![CCQ](assets/fr/10.webp)

Tenete presente che l'uso di una passphrase significa che dovrete importare un nuovo set di chiavi derivate dalla combinazione di frase mnemonica e passphrase nel vostro software di gestione dei portafogli (come Sparrow Wallet). Per farlo, seguite il passo "*Configurare un nuovo portafoglio su Sparrow*" in quest'altro tutorial:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
## Opzioni di sblocco

Le COLDCARD offrono inoltre una serie di opzioni per il processo di sblocco del dispositivo. Scopriamo di più su queste opzioni avanzate.

### PIN truccati

Il Trick PIN è un codice PIN secondario diverso da quello definito durante la configurazione iniziale del dispositivo. Questo codice viene utilizzato per attivare azioni specifiche preconfigurate non appena viene inserito all'accensione della COLDCARD. È possibile configurare diversi Trick PIN, ciascuno collegato a un'azione diversa. Queste funzioni consentono di adattare la COLDCARD alla propria strategia di sicurezza personale. Sono particolarmente utili in caso di costrizione fisica, come ad esempio durante una rapina (comunemente chiamata nella comunità Bitcoin "attacco con chiave da 5 dollari*").

Per attivare un Trick PIN e associarlo a un'azione, accedere al menu `Impostazioni > Impostazioni di accesso > Trick PIN`.

![CCQ](assets/fr/11.webp)

Selezionare "*Aggiungi nuovo trucco*".

![CCQ](assets/fr/12.webp)

Impostare il codice PIN da associare all'azione e ricordarsi di salvarlo.

![CCQ](assets/fr/13.webp)

Scegliere quindi l'azione da eseguire automaticamente ogni volta che si inserisce questo PIN truccato. Ecco l'elenco delle azioni disponibili per un PIN:


- "*Autosuggestione del mattone*: Questa azione distrugge entrambi i chip della COLDCARD Q se viene inserito il Trick PIN, rendendo il dispositivo totalmente inutilizzabile. Sarà quindi impossibile rivenderlo, riutilizzarlo o persino restituirlo alla Coinkite. Il dispositivo diventerà irrimediabilmente obsoleto. Questa funzione può essere utilizzata in caso di rapina per convincere l'aggressore che non sarà mai in grado di accedere ai vostri bitcoin. **Nota bene**: senza un backup fisico della frase mnemonica e di qualsiasi passphrase, i bitcoin andranno definitivamente persi.

![CCQ](assets/fr/14.webp)


- "*Cancella seme*": Questo menu offre diverse azioni per cancellare il seme, cioè per resettare la COLDCARD senza distruggerla. A differenza dell'opzione "*Brick Self*", sarà possibile riconfigurare il dispositivo utilizzando un backup della frase mnemonica. Tuttavia, senza questo backup, i bitcoin andranno persi. Ecco le opzioni disponibili:
 - "Cancella e riavvia": Rimuove il seme e riavvia la COLDCARD senza visualizzare alcuna informazione sullo schermo.
 - "*Silent Wipe*": Cancella silenziosamente il seme e sblocca la COLDCARD su un portafoglio falso casuale, come se non fosse successo nulla.
 - "*Wipe -> Wallet*": Rimuove il seme in modo discreto e sblocca la COLDCARD su un portafoglio secondario preconfigurato, progettato come esca. Questo portafoglio può contenere una piccola parte dei vostri risparmi in bitcoin per soddisfare un aggressore.
 - "*Seme cancellato, stop*": Cancella il seme e visualizza sullo schermo il messaggio "Il seme è stato cancellato, stop".

![CCQ](assets/fr/15.webp)


- "*Portafoglio di sicurezza*": Con questa azione, il codice PIN ingannevole sblocca un portafoglio derivato dal seme utilizzando il BIP85. Questo portafoglio secondario può essere usato come esca per soddisfare un aggressore. La COLDCARD si comporta come se fosse il vero portafoglio, ma senza il PIN principale (diverso dal PIN truffa), l'aggressore non sarà mai in grado di accedere al vero portafoglio. Questa strategia è pensata per far credere che il portafoglio collegato al PIN ingannevole sia l'unico esistente.

![CCQ](assets/fr/16.webp)


- "*Conto alla rovescia del login*": Questo menu raggruppa le azioni con un conto alla rovescia prima della loro esecuzione. **Attenzione, alcune di esse possono distruggere il dispositivo o causare la perdita di bitcoin. Ecco le sottoazioni disponibili:
 - "Cancella e conto alla rovescia": Cancella il seme dalla memoria della COLDCARD, quindi avvia un conto alla rovescia di un'ora. Senza salvare la mnemonica o la passphrase, i bitcoin andranno persi. Questa opzione è progettata per ingannare un aggressore e fargli credere che il dispositivo si sbloccherà al termine del conto alla rovescia, mentre in realtà verrà ripristinato alle impostazioni di fabbrica.
 - "Conto alla rovescia e mattone*": Avvia un conto alla rovescia di un'ora, al termine del quale la COLDCARD distrugge i suoi due chip di sicurezza, rendendola definitivamente inutilizzabile. Senza backup, i bitcoin andranno persi. Questa azione è progettata per ingannare un aggressore, che pensa di essere in attesa di uno sblocco, mentre in realtà il dispositivo si autodistruggerà.
 - "*Solo conto alla rovescia* : Attiva un semplice conto alla rovescia di un'ora, al termine del quale la COLDCARD si riavvia senza ulteriori azioni. Il seme non viene cancellato e il dispositivo rimane intatto. Attenzione a non confondere questa azione con l'opzione "*Conto alla rovescia per l'accesso*", discussa nelle sezioni seguenti, che aggiunge un conto alla rovescia al PIN principale e dà accesso al portafoglio reale.

![CCQ](assets/fr/17.webp)


- "*Sguardo vuoto*": Questa azione fa apparire la COLDCARD vuota, dando l'impressione che il seme sia stato cancellato. In realtà, non succede nulla e il seme rimane intatto. In questo modo si simula una COLDCARD inutilizzata o azzerata.

![CCQ](assets/fr/18.webp)


- "*Basta riavviare* : Quando si utilizza il Trick PIN, la COLDCARD si riavvia semplicemente. Non viene eseguita nessun'altra azione.

![CCQ](assets/fr/19.webp)


- "Modalità *Delta*": Questa azione complessa, riservata a utenti esperti, è progettata per contrastare attacchi di coercizione altamente sofisticati, provenienti da uno Stato o da un parente con informazioni privilegiate. Quando la modalità Delta è attivata, COLDCARD fornisce l'accesso al portafoglio reale, consentendo a un aggressore di navigare e verificare che si tratti del portafoglio corretto. Tuttavia, le firme delle transazioni sono bloccate, impedendo così qualsiasi trasferimento di bitcoin. Inoltre, l'accesso alla frase mnemonica è disabilitato e qualsiasi tentativo di recuperarla comporta la sua cancellazione. Per aumentare la credibilità, il Trick PIN utilizzato con la Modalità Delta deve avere lo stesso prefisso del PIN reale (per visualizzare le stesse parole anti-phishing), ma il suffisso deve essere diverso.

![CCQ](assets/fr/20.webp)

Una volta selezionata un'azione, confermare la scelta.

![CCQ](assets/fr/21.webp)

È quindi possibile visualizzare tutti i PIN configurati nel menu dedicato.

![CCQ](assets/fr/22.webp)

Selezionando un PIN truccato esistente, è possibile controllare l'azione associata. È anche possibile nasconderlo con "*Nascondi trucco*", rendendolo invisibile nel menu PIN trucco. È possibile cancellarlo facendo clic su "*Cancella trucco*", oppure modificare il codice PIN mantenendo l'azione associata con "*Cambia PIN*".

![CCQ](assets/fr/23.webp)

L'opzione "*Aggiungi se sbagliato*", disponibile nel menu "*Trick PIN*", consente di configurare un'azione specifica che si attiva automaticamente dopo un certo numero di tentativi errati di immissione del codice PIN principale. Il numero di tentativi consentiti può essere impostato durante la configurazione.

### Tasti scramble

L'opzione di scramble keys consente di scramble le cifre visualizzate sui tasti della tastiera durante l'immissione del codice PIN. Questa funzione protegge la riservatezza del codice PIN, anche in caso di sorveglianza da parte di persone o telecamere.

Per attivare questa opzione, accedere al menu `Impostazioni > Impostazioni di accesso > Tasti di scramble`.

![CCQ](assets/fr/24.webp)

Selezionare l'opzione "*Tasti di scramble*".

![CCQ](assets/fr/25.webp)

D'ora in poi, quando si sblocca la COLDCARD Q, ai tasti della tastiera verranno assegnati nuovi numeri in modo casuale ad ogni utilizzo.

![CCQ](assets/fr/26.webp)

### Conto alla rovescia per l'accesso

Questa opzione consente di imporre un conto alla rovescia sistematico ogni volta che si tenta di sbloccare la COLDCARD. Può essere integrata nella vostra strategia di sicurezza ritardando l'accesso al dispositivo in caso di furto o imponendo un ritardo prima di firmare una transazione, ad esempio per proteggersi in caso di rapina. Tuttavia, questo conto alla rovescia si applica a tutti i vostri utilizzi, anche quando utilizzate legittimamente la vostra COLDCARD, il che vi obbliga anche a essere pazienti. Attenzione a non confondere questa opzione con l'azione "*Basta il conto alla rovescia*", che si attiva solo quando si utilizza un PIN truccato specifico.

Per configurare questa opzione, accedere al menu `Impostazioni > Impostazioni di accesso > Conto alla rovescia dell'accesso`.

![CCQ](assets/fr/27.webp)

Selezionare il tempo di conto alla rovescia. Ad esempio, se si seleziona 1 ora, si dovrà attendere 1 ora per ogni tentativo di sblocco della COLDCARD Q.

![CCQ](assets/fr/28.webp)

Ogni volta che si sblocca, viene richiesto di inserire il codice PIN.

![CCQ](assets/fr/29.webp)

Attendere quindi il tempo impostato dal conto alla rovescia.

![CCQ](assets/fr/30.webp)

Al termine del conto alla rovescia, sarà necessario immettere nuovamente il PIN per accedere al dispositivo.

![CCQ](assets/fr/31.webp)

### Accesso alla calcolatrice

Questa opzione consente di mascherare la COLDCARD come una calcolatrice al momento dello sblocco. Per attivare questa funzione, accedere al menu `Impostazioni > Impostazioni di accesso > Accesso con calcolatrice`.

![CCQ](assets/fr/32.webp)

Attivare l'opzione selezionandola.

![CCQ](assets/fr/33.webp)

D'ora in poi, a ogni accensione del dispositivo, verrà visualizzata una calcolatrice funzionante con i comandi di base.

![CCQ](assets/fr/34.webp)

Ad esempio, è possibile calcolare l'hash SHA256 di "*Plan B Network*".

![CCQ](assets/fr/35.webp)

Per sbloccare la COLDCARD dalla modalità calcolatrice, iniziare inserendo il prefisso del codice PIN seguito da un trattino. Ad esempio, se il codice PIN è `00-00` (questo codice è debole ed è solo un esempio, quindi scegliete un codice PIN forte), digitate `00-`. La COLDCARD visualizzerà quindi le due parole anti-phishing.

![CCQ](assets/fr/36.webp)

Inserire quindi il codice PIN completo, separato da uno spazio o da un trattino, ad esempio: `00 00`.

![CCQ](assets/fr/37.webp)

La COLDCARD esce quindi dalla modalità calcolatrice e si sblocca normalmente.

## Distruzione pulita della COLDCARD

Se si intende smaltire la COLDCARD Q, ad esempio perché si utilizza un altro portafoglio hardware, è importante distruggere correttamente il dispositivo. In questo modo si garantisce che nessuna informazione relativa al portafoglio possa essere recuperata da terzi.

Esistono tre livelli di distruzione delle informazioni, a seconda delle vostre esigenze. Prima di iniziare, assicuratevi che il vostro portafoglio sia stato importato in un altro portafoglio hardware, che abbiate accesso a tutti i vostri fondi e, soprattutto, che abbiate la vostra frase mnemonica e l'eventuale passphrase, entrambe funzionanti. Senza un backup del portafoglio, la distruzione della COLDCARD comporterà la perdita dei bitcoin.

Il primo livello di distruzione consiste nell'eliminazione del solo seme. Questa opzione cancella la frase mnemonica dalla memoria della COLDCARD, pur lasciando il dispositivo funzionante. È l'ideale se si desidera utilizzare nuovamente la COLDCARD Q in un secondo momento. Per eliminare il seme dalla memoria, accedere al menu `Avanzate/Strumenti > Zona di pericolo > Funzioni seme > Distruggi seme`.

![CCQ](assets/fr/38.webp)

Il secondo livello di distruzione consiste nel disabilitare in modo permanente i due chip di sicurezza della COLDCARD tramite il software. Questa azione rende il dispositivo completamente inutilizzabile. Non sarà possibile rivenderla, riutilizzarla o restituirla a Coinkite: sarà definitivamente distrutta. Per procedere, seguire la procedura descritta nella sezione precedente relativa al PIN "*Brick Me*" Quindi inserire intenzionalmente questo PIN quando si sblocca la COLDCARD.

Il terzo livello prevede la distruzione fisica dei componenti sicuri della COLDCARD Q. Come in precedenza, questo renderà il dispositivo irrimediabilmente inutilizzabile. Come in precedenza, questo renderà il dispositivo irrimediabilmente inutilizzabile. Per farlo, utilizzate un trapano per praticare un foro nei due chip sul lato superiore destro del dispositivo (una volta capovolto), vicino alla scritta "*SHOOT HERE*".

**Precauzioni importanti** :


- Per evitare il rischio di scosse elettriche, rimuovere le batterie dal dispositivo e scollegarlo dalla rete elettrica prima di maneggiarlo.
- Attendere qualche minuto dopo lo spegnimento dell'unità prima di iniziare la perforazione.
- Indossare guanti isolanti e occhiali di sicurezza per garantire la propria sicurezza.

![CCQ](assets/fr/39.webp)

Una volta perforati i chip, non tentare di ricollegare la COLDCARD Q.

Congratulazioni, ora siete al corrente delle opzioni avanzate della COLDCARD Q!

Se avete trovato utile questo tutorial, vi sarei molto grato se lasciaste un pollice verde qui sotto. Sentitevi liberi di condividere questo tutorial sui vostri social network. Grazie mille!

Vi consiglio anche quest'altro tutorial, in cui si parla dell'uso di un concorrente diretto di CCQ, Ledger Flex :

https://planb.network/fr/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a
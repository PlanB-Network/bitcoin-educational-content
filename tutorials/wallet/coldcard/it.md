---
name: Cold Card

description: Creazione, backup e utilizzo di una chiave privata Bitcoin con un dispositivo Coldcard e Bitcoin Core.
---

![copertina](assets/cover.jpeg)

Creazione, backup e uso di una chiave privata Bitcoin con un dispositivo Coldcard e Bitcoin Core

## Guida completa alla generazione di una chiave privata con una Coldcard e al suo utilizzo attraverso l'interfaccia del vostro nodo Bitcoin Core!

Alla base dell'utilizzo della rete Bitcoin c'è il concetto di crittografia asimmetrica: una coppia di chiavi - una privata e una pubblica - che cripta e decripta i dati, un concetto che garantisce la riservatezza della comunicazione.

Nel caso di Bitcoin, generando tale coppia di chiavi private e pubbliche, siamo in grado di immagazzinare bitcoin (UTXO o Unspent Transaction Output) e firmare transazioni per spenderli.

Oggi sono disponibili diversi strumenti che facilitano la generazione casuale di una chiave privata e il suo backup in forma testuale utilizzando il BIP 39, uno standard che determina il modo in cui i portafogli associano una frase mnemonica (seed phrase) alle chiavi di crittografia. Il più delle volte, la frase mnemonica è composta da 12 o 24 parole, che devono essere salvate in modo sicuro per poter recuperare un portafoglio e i suoi bitcoin.
In questo articolo, impareremo come generare una chiave privata utilizzando una Coldcard Mk4, uno dei dispositivi più diffusi e sicuri nel mondo di Bitcoin, utilizzando il metodo del lancio dei dadi per garantire la massima entropia, e come utilizzarla con Bitcoin Core in maniera air-gapped!

> 🧰| Per seguire la guida, procuratevi i seguenti strumenti:
>
> - Dispositivo Coldcard (Mk3 o Mk4)
> - Scheda MicroSD (4 GB sono sufficienti)
> - Cavo USB magnetico di sola alimentazione (mini-usb per Mk3, usb-c per Mk4)
> - Uno o più dadi di qualità

## Generazione di una nuova frase mnemonica con una Coldcard

Inizieremo il processo di creazione di una chiave privata da zero, assumendo una Coldcard appena spacchettata su cui è già stato impostato un PIN (seguire i passaggi sulla Coldcard durante l'inizializzazione del dispositivo).

> Per ripristinare la chiave privata di una Coldcard già configurata, procedere come segue:
> Avanzate/Strumenti > Zona di pericolo > Funzioni di semina > Distruggi seme> ✓
>
> _Attenzione_: la tua Coldcard dimenticherà la chiave privata dopo questi passaggi. Assicurati di aver salvato correttamente la tua frase mnemonica se desideri recuperarla in seguito.

## Passaggi da seguire:

Connessione a Coldcard con il PIN > Nuove parole seed > Lancio di dadi a 24 parole

Effettua 100 lanci di dadi annotando il risultato ottenuto da 1 a 6 su Coldcard dopo ogni lancio. Utilizzando questo metodo, creerai 256 byte di entropia che favoriranno la creazione di una chiave privata completamente casuale. Coinkite fornisce anche la documentazione necessaria per la verifica indipendente del loro sistema di generazione di entropia.

![Screenshot Visuale Cold Card](assets/guide-agora/1.jpeg)

Una volta completati i 100 lanci di dadi, premi ✓ e annota le 24 parole ottenute nell'ordine. Verifica due volte e premi ✓. Infine, completa il test di verifica delle 24 parole su Coldcard e avrai creato la tua nuova chiave privata!

Successivamente, scegli se desideri attivare o meno le funzioni NFC (Mk4) e USB seguendo i passaggi visualizzati. Una volta nel menu principale, è ora il momento di aggiornare il firmware del dispositivo. Vai su Advanced/Tools > Upgrade Firmware > Show Version e consulta il sito web ufficiale per confermare e scaricare l'ultima versione disponibile. È consigliabile aggiornare Coldcard per garantire il massimo della sicurezza.

Prima di procedere, è consigliabile annotare il Master Key Fingerprint (XFP) associato alla chiave privata. Questo dato consente di verificare rapidamente se ci si trova nel portafoglio corretto in caso di recupero, ad esempio. Vai su Advanced/Tools > View Identity > Master Key Fingerprint (XFP) e annota la serie di otto caratteri alfanumerici ottenuti. Il XFP può essere annotato nello stesso punto della frase mnemonica, non è un dato sensibile.

> 💡 È consigliabile testare il backup della frase mnemonica su un software diverso. Per farlo in modo sicuro, consulta il nostro articolo Verifica del backup di un portafoglio Bitcoin con Tails in meno di 5 minuti.

## Bonus di sicurezza: la "Frase Segreta" (opzionale)

Una frase segreta (passphrase) è un elemento fantastico da aggiungere alla configurazione del portafoglio per aggiungere un livello di sicurezza per proteggere i propri bitcoin. La frase segreta funziona in qualche modo come una 25a parola alla frase mnemonica. Una volta aggiunta, viene creato un portafoglio completamente nuovo insieme a una chiave privata e alla sua frase mnemonica associata. Non è necessario annotare la nuova frase mnemonica, poiché è possibile accedere a questo portafoglio combinando la frase mnemonica iniziale con la frase segreta scelta.

L'obiettivo è annotare la frase segreta separatamente dalla frase mnemonica perché un attaccante che ha accesso a entrambi gli elementi avrà accesso ai fondi contenuti. Al contrario, un attaccante che ha accesso solo a uno di questi elementi non avrà alcun accesso ai fondi, ed è proprio questo vantaggio specifico che ottimizza il livello di sicurezza della configurazione del portafoglio.

![Aggiungere una frase segreta porta a un portafoglio completamente diverso](assets/guide-agora/2.jpeg)

## Passaggi per aggiungere una frase segreta con Coldcard:

Passphrase > Aggiungi parole (consigliato) > Applica. Il dispositivo mostrerà l'XFP del portafoglio appena generato tramite la frase segreta, che è consigliabile annotare insieme alla frase segreta per le stesse ragioni menzionate in precedenza.

> 💡 Risorse aggiuntive correlate alla frase segreta:

> https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af > https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/ > https://armantheparman.com/passphrase/

## Esportazione del portafoglio su Bitcoin Core

Il portafoglio è ora pronto per essere esportato su un software per interagire con la rete Bitcoin. In questa guida, useremo Bitcoin Core (v24.1).

Fai riferimento alle nostre guide per l'installazione e la configurazione di Bitcoin Core:

> Eseguire il proprio nodo con Bitcoin Core - https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
>
> Configurazione di Tor per un nodo Bitcoin Core - https://agora256.com/configuration-tor-bitcoin-core/

Inserisci una scheda micro SD nella Coldcard e quindi esporta il portafoglio su Bitcoin Core seguendo questi passaggi:

Advanced/Tools > Esporta Portafoglio > Bitcoin Core. Due file saranno registrati sulla scheda micro SD: bitcoin-core.sig e bitcoin-core.txt. Inserisci la scheda micro SD nel computer su cui è installato Bitcoin Core e apri il file .txt. Vedrai la riga Per il portafoglio con l'impronta digitale della chiave principale. Verifica che l'XFP di otto caratteri corrisponda a quello che hai annotato durante la creazione della tua chiave privata.

Prima di seguire le istruzioni nel file, iniziamo preparando il portafoglio nell'interfaccia di Bitcoin Core seguendo questi passaggi: vai alla scheda File > Crea un portafoglio. Scegli un nome per il tuo portafoglio (termine intercambiabile con "portafoglio" in Core) e seleziona le opzioni Disabilita le chiavi private, Crea un portafoglio vuoto e Portafoglio di descrittori come mostrato nell'immagine qui sotto. Quindi, premi il pulsante Crea.

![crea un portafoglio](assets/guide-agora/3.jpeg)

Una volta creato il portafoglio in Bitcoin Core, vai alla scheda Finestra > Console e assicurati che il portafoglio selezionato in alto nella pagina mostri correttamente il nome di quello che hai creato.

Ora, nel file .txt generato precedentemente da Coldcard, copia la riga che inizia con importdescriptors e incollala nella console di Bitcoin Core. Dovrebbe essere restituita una risposta che include la riga "success": true.

![finestra dei nodi](assets/guide-agora/4.jpeg)

Se la risposta contiene "message": "I descrittori a intervalli non dovrebbero avere un'etichetta", cancella l'ingresso "label": "Coldcard xxxx0000" nella riga copiata dal file .txt e quindi incolla la riga completa nella console di Bitcoin Core.

Aiuto: https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md

## Convalida dell'importazione del portafoglio in Bitcoin Core

Per assicurarsi che l'operazione sia stata eseguita correttamente, è necessario convalidare che sia stato importato il portafoglio desiderato in Bitcoin Core. Un modo semplice per confermarlo è verificare che gli indirizzi generati su Coldcard corrispondano agli indirizzi generati su Bitcoin Core.

Bitcoin Core: Ricevi > Crea un nuovo indirizzo di ricezione
Coldcard: Address Explorer > Scegli l'indirizzo che inizia con bc1q. L'indirizzo Coldcard 'bc1q' deve corrispondere all'indirizzo visualizzato in Bitcoin Core.
Ricevere e inviare transazioni in modalità "air-gapped"

Ricevere una transazione è estremamente semplice; è sufficiente premere Ricevi, etichettare la transazione (opzionale ma consigliato) e creare un nuovo indirizzo di ricezione. Quindi basta condividere l'indirizzo con il mittente.

Ora, l'elemento chiave di questa configurazione Coldcard + Bitcoin Core è l'invio di transazioni senza che Coldcard e la sua chiave privata siano connesse a Internet, un metodo chiamato "air-gapped" che utilizza la funzione TBSP (PSBT - Partially Signed Bitcoin Transactions) di Bitcoin.

Essenzialmente, utilizziamo l'interfaccia Bitcoin Core per costruire una transazione, che successivamente esporteremo tramite la scheda micro SD sulla Coldcard per firmarla, per poi restituire il file di transazione firmato su Bitcoin Core e diffondere la transazione alla rete. Dobbiamo procedere in questo modo poiché comunque il portafoglio importato su Bitcoin Core non ha una chiave privata, solo la chiave pubblica (che ci consente di generare i nostri indirizzi di ricezione), e quindi ci è impossibile firmare una transazione direttamente nel software per spendere i nostri bitcoin.

Prima di procedere, assicurati che le seguenti opzioni siano attivate in Impostazioni > Portafoglio:

> - Abilita le funzioni di controllo delle monete
> - Spendere moneta non confermata (Opzionale)
> - Abilita i controlli TBPS

![opzione](assets/guide-agora/5.jpeg)

### Passaggi per inviare in modalità air-gapped:

Invia > Input > scegli l'utxo desiderato, quindi inserisci l'indirizzo del destinatario in Paga a. Commissioni di transazione: Scegli... > Personalizzate > Inserisci le commissioni di transazione (Bitcoin Core calcola in sats/kilobyte anziché sat/byte come la maggior parte delle soluzioni alternative di portafoglio. Quindi 4000 sats/kilobyte = 4 sats/byte). Crea una transazione non firmata > salva il file nella tua scheda microSD e inseriscila nella Coldcard.

Nella Coldcard, premi Pronto per firmare, verifica i dettagli della transazione e premi ✓ e reinserisci la scheda microSD nel computer una volta generati i file firmati.

Tornando su Bitcoin Core, vai nella scheda File > Carica TBSP da un file e inserisci il file di transazione firmato .psbt. Verrà visualizzata la sezione Operazioni PSBT sullo schermo, confermando che la transazione è completamente firmata e pronta per essere diffusa. Non resta che premere Diffondi la transazione.

![Operazioni PSBT](assets/guide-agora/6.jpeg)

### Conclusioni

La combinazione del dispositivo Coldcard con Bitcoin Core, su cui esegui il tuo proprio nodo, è potente. Aggiungi a ciò una chiave privata generata con 100 lanci di dado e una frase segreta, e la tua configurazione del portafoglio diventa una fortezza sofisticata e robusta.

Non esitare a contattarci per condividere tutti i tuoi commenti e domande! Il nostro obiettivo è condividere le nostre conoscenze e aumentare la nostra saggezza giorno dopo giorno.

---
name: Satscard
description: Configurazione e utilizzo di una Satscard con Nunchuk
---
![cover](assets/cover.webp)

Bitcoin è un sistema di pagamento elettronico che ci permette di eseguire transazioni peer-to-peer. Tuttavia, per essere convinti che una transazione sia immutabile, è necessario attendere diverse conferme (solitamente 6), per evitare qualsiasi tentativo di doppia spesa da parte del mittente. Questo ritardo nella validazione può talvolta essere scomodo, specialmente quando si desidera una finalità immediata simile al contante fisico. A differenza del contante, dove il possesso di una banconota viene trasferito istantaneamente, le transazioni Bitcoin comportano un tempo di attesa prima di essere definitivamente considerate irreversibili.

Qui entra in gioco la Satscard. Offre un metodo per abilitare la trasmissione fisica e istantanea di bitcoin, senza la necessità di eseguire una transazione on-chain. La Satscard funziona come una carta portatore che consente il trasferimento sicuro della proprietà dei bitcoin, offrendo così un'esperienza più vicina al contante tradizionale. In questo tutorial, vi introdurrò a questa soluzione.

## Cos'è una Satscard?

La Satscard di Coinkite è il successore dell'Opendime. È una carta NFC che consente la trasmissione fisica di bitcoin, simile a una banconota o moneta. A differenza di un tradizionale portafoglio hardware, la Satscard è una carta portatore, il che significa che il possesso fisico della carta equivale alla proprietà dei bitcoin che sono assicurati con le chiavi memorizzate su di essa. Il suo prezzo varia tra $6.99 e $17.99 a seconda del design scelto.

![SATSCARD](assets/notext/01.webp)

Il chip della Satscard è dotato di 10 slot, che permettono di memorizzare bitcoin fino a 10 volte su 10 indirizzi diversi. Ogni slot opera indipendentemente e dovrebbe teoricamente essere utilizzato solo una volta per bloccare i bitcoin al suo interno. Per spendere i bitcoin, basta sbloccare lo slot con un'applicazione compatibile, come Nunchuk, inserendo il codice di verifica a 6 cifre annotato sul retro della Satscard.

La carta assicura che la chiave privata che protegge i bitcoin sulla blockchain non possa essere trattenuta dal precedente proprietario una volta che si separa fisicamente dalla carta. Il destinatario può anche verificare la validità di uno slot e l'importo memorizzato al momento dello scambio.

Questo sistema è particolarmente utile per l'acquisto di beni fisici con bitcoin, o per regalare bitcoin.

## Come acquistare una Satscard?

La Satscard è disponibile per l'acquisto [sul sito ufficiale di Coinkite](https://store.coinkite.com/store/category/satscard). Per acquistarla in un negozio fisico, è possibile trovare [l'elenco dei rivenditori certificati](https://coinkite.com/resellers) sul sito.
Avrai anche bisogno di un telefono compatibile con le comunicazioni NFC, o di un dispositivo USB per leggere le carte NFC alla frequenza standard di 13.56 MHz.
## Come caricare uno slot su una Satscard?

Una volta ricevuta la tua Satscard, il primo passo è controllare l'imballaggio per assicurarsi che non sia stato aperto. Se la confezione è danneggiata, potrebbe indicare che la carta è stata compromessa e potrebbe non essere autentica.

Per gestire la Satscard, utilizzeremo l'applicazione mobile **Nunchuk Wallet**. Assicurati che il tuo smartphone sia compatibile NFC, poi scarica Nunchuk dal [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), dall'[App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073), o direttamente tramite il suo file [`.apk`](https://github.com/nunchuk-io/nunchuk-android/releases).
In teoria, potresti inviare direttamente bitcoin all'indirizzo specificato sul retro della tua Satscard senza utilizzare Nunchuk. Tuttavia, sconsiglio di farlo, poiché prima verificheremo che l'indirizzo del primo slot sia effettivamente derivato da una chiave privata memorizzata nella Satscard e che non si tratti di un indirizzo fraudolento.

Se stai utilizzando Nunchuk per la prima volta, l'app ti offrirà di creare un account. Ai fini di questo tutorial, non è necessario crearne uno. Quindi, seleziona "*Continua come ospite*" per continuare senza un account.

Poi clicca su "*Portafoglio non assistito*".

Successivamente, clicca sul pulsante "*Esplorerò da solo*".

Una volta sulla schermata principale di Nunchuk, clicca sul logo "*NFC*" in alto sullo schermo.

Tieni la tua Satscard sul retro del tuo telefono per scansionarla.

Nunchuk mostra l'indirizzo di ricezione corrispondente al primo slot della tua Satscard. Normalmente, questo indirizzo dovrebbe essere identico a quello scritto manualmente sul retro della tua carta. Copia questo indirizzo e usalo per trasferire i bitcoin che desideri bloccare con questo slot.

## Come controllare i bitcoin su uno slot?

Una volta confermata la transazione, puoi controllare il saldo associato a uno slot della tua Satscard scansionandola con Nunchuk. Così, durante una transazione, il destinatario dei bitcoin può verificare istantaneamente, tramite la loro app Nunchuk, che la carta contenga effettivamente i bitcoin a loro dovuti.

Se la controparte non ha l'app Nunchuk, può comunque verificare la validità della Satscard. Basta attivare l'NFC sul loro smartphone e posizionare la Satscard sul retro del dispositivo. Questo aprirà automaticamente il sito web della Satscard in un browser, dove si può controllare la validità della carta così come l'importo in bitcoin ad essa associato.

## Come prelevare bitcoin da uno slot?

Ora che il primo slot della Satscard è stato caricato con una certa quantità di bitcoin, puoi consegnare la carta al destinatario del pagamento.

Se sei il destinatario, devi installare Nunchuk. Una volta nell'app, clicca sul logo "*NFC*" in alto sullo schermo.

Posiziona la tua Satscard sul retro del tuo telefono.

Nunchuk rivelerà l'importo assicurato sull'indirizzo.

Per sbloccare la chiave privata e trasferire i bitcoin a un indirizzo di tua proprietà, clicca sul pulsante "*Sblocca e trasferisci saldo*".

L'opzione "*Trasferisci a un portafoglio*" ti permette di inviare direttamente i bitcoin a un portafoglio già presente nella tua app Nunchuk. Per trasferire i fondi a un diverso indirizzo di ricezione, seleziona "*Preleva su un indirizzo*".
Inserisci l'indirizzo di ricezione dove desideri inviare i bitcoin protetti dalla Satscard. Assicurati che l'indirizzo inserito sia corretto (questa è l'unica volta in cui puoi verificarlo), quindi clicca sul pulsante "Crea transazione".

Inserisci il codice PIN della tua Satscard. Questo codice a 6 cifre è annotato sul retro della carta fisica.

Mantieni la tua Satscard sul retro del tuo smartphone mentre firmi la transazione con la chiave privata memorizzata sulla carta NFC.

La tua transazione è ora firmata e trasmessa sulla rete Bitcoin, il che significa che lo slot utilizzato sulla tua Satscard è ora vuoto.

## Come riutilizzare la Satscard?

A differenza delle soluzioni monouso come Opendime, la Satscard è dotata di un chip contenente 10 slot indipendenti, che permettono fino a 10 operazioni con una singola carta. Il primo slot, preconfigurato in fabbrica da Coinkite, corrisponde all'indirizzo di ricezione scritto sul retro della tua Satscard.

Per attivare gli altri 9 slot, dovrai generare la coppia di chiavi e l'indirizzo tramite l'app Nunchuk. Nella homepage dell'app, clicca sul logo "NFC" in alto sullo schermo.

Posiziona la tua Satscard sul retro del tuo telefono.

Nunchuk indica che nessuno slot è attivo sulla carta, il che è normale poiché il primo è già stato utilizzato e il secondo non è ancora stato generato. Per vedere gli slot precedentemente utilizzati, clicca su "Visualizza slot non sigillati". Si sconsiglia vivamente di riutilizzare questi slot, in quanto ciò porterebbe a un riutilizzo dell'indirizzo dannoso per la tua privacy on-chain. Pertanto, imposteremo un nuovo slot cliccando sul pulsante "Sì".

Ora dovrai scegliere come generare il tuo codice catena master.

Gli slot sulla Satscard seguono lo standard BIP32, il che significa che la derivazione delle chiavi crittografiche che proteggono i bitcoin non si basa su una frase mnemonica come nei portafogli BIP39, ma direttamente su una chiave privata master e un codice catena master. Questi due elementi sono utilizzati come input nella funzione HMAC-SHA512 per generare una coppia di chiavi figlio. Ogni slot ha la propria chiave master e il proprio codice catena master. C'è solo un livello di derivazione per ogni slot.

La coppia di chiavi per il primo slot è pre-generata da Coinkite. Questo è il motivo per cui hai accesso diretto ad essa tramite Nunchuk, e perché l'indirizzo di ricezione è scritto sul retro della carta NFC. Per gli altri slot, tuttavia, sei responsabile della generazione delle chiavi.

La chiave privata master per ogni slot è generata direttamente dalla Satscard, e i codici catena master devono essere forniti dall'esterno. Per il codice catena del tuo nuovo slot, hai due opzioni: lasciare che Nunchuk lo generi automaticamente selezionando "Automatico", o crearlo tu stesso optando per "Avanzato" e inserendolo nello spazio dedicato. Perché il codice catena sia efficace, deve essere il più casuale possibile.
Inserisci il PIN a 6 cifre riportato sul retro della Satscard.
![SATSCARD](assets/notext/26.webp)

Posiziona la tua Satscard sul retro del tuo telefono.

![SATSCARD](assets/notext/27.webp)

Un nuovo slot è stato configurato con successo. Ora puoi vedere l'indirizzo di ricezione per depositare bitcoin. Per procedere con il caricamento, segui le istruzioni nella sezione "*Come caricare uno slot su una Satscard?*" di questo tutorial.
Puoi ripetere questo processo fino a 10 volte su ogni Satscard.

Congratulazioni, ora sei aggiornato sull'uso della Satscard! Se hai trovato utile questo tutorial, apprezzerei se potessi lasciare un pollice in su qui sotto. Sentiti libero di condividere questo articolo sui tuoi social network. Grazie mille!
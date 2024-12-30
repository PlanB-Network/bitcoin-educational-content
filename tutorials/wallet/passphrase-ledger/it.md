---
name: BIP39 Passphrase Ledger
description: Come aggiungere una passphrase al tuo portafoglio Ledger?
---
![cover](assets/cover.webp)

Una passphrase BIP39 è una password opzionale che, combinata con la tua frase mnemonica, fornisce un ulteriore livello di sicurezza per i portafogli Bitcoin deterministici e gerarchici. In questo tutorial, esamineremo insieme come impostare una passphrase sul tuo portafoglio Bitcoin sicuro su un Ledger (indipendentemente dal modello).

Prima di iniziare questo tutorial, se non sei familiare con il concetto di passphrase, come funziona e le sue implicazioni per il tuo portafoglio Bitcoin, ti consiglio vivamente di consultare questo altro articolo teorico dove spiego tutto:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Come funziona la passphrase su un Ledger?

Con i dispositivi Ledger, hai due opzioni diverse per configurare una passphrase sul tuo portafoglio: l'opzione "*legata al PIN*" e l'opzione "*temporanea*".

Con l'opzione "*legata al PIN*", associ una passphrase a un secondo PIN sul tuo Ledger. Questo significa che avrai 2 PIN: uno per accedere al tuo portafoglio regolare senza passphrase e l'altro per accedere al tuo secondo portafoglio protetto dalla passphrase.

![PASSPHRASE BIP39](assets/notext/03.webp)

Fondamentalmente, anche con questa opzione di passphrase legata al secondo PIN, la tua passphrase rimane la tua passphrase. Ciò significa che se perdi il tuo Ledger e desideri recuperare i tuoi bitcoin su un altro dispositivo o software, avrai assolutamente bisogno della tua frase di 24 parole e della tua **passphrase completa**. Il PIN associato alla passphrase viene utilizzato solo per accedervi sul tuo Ledger attuale, ma non funziona su altri Ledger o altri software. È quindi importante fare un backup completo della tua passphrase su un supporto fisico. **Conoscere solo il PIN secondario non è sufficiente per riaccedere al tuo portafoglio**; è semplicemente una funzionalità di comodità sul tuo Ledger.

Questa opzione del secondo PIN è particolarmente interessante per affrontare attacchi fisici. Ad esempio, se un aggressore ti costringe a sbloccare il tuo dispositivo per rubare i tuoi fondi, puoi usare il primo PIN per accedere a un portafoglio esca contenente una piccola quantità di bitcoin, mantenendo i tuoi fondi principali al sicuro dietro il secondo PIN.

Inoltre, questa opzione offre tutti i vantaggi di sicurezza della passphrase BIP39 senza il vincolo di doverla inserire manualmente ogni volta che usi il dispositivo di firma. Ciò ti consente di utilizzare una passphrase lunga e casuale, rafforzando così la protezione contro gli attacchi di forza bruta, evitando al contempo la difficoltà di doverla digitare manualmente ogni volta sui piccoli pulsanti del dispositivo.
L'opzione della "passphrase temporanea" non memorizza la passphrase sul dispositivo. Ogni volta che vuoi accedere al tuo portafoglio protetto, dovrai inserire manualmente la passphrase sul Ledger. Questo rende l'uso più ingombrante ma aumenta leggermente la sicurezza lasciando nessuna traccia della passphrase sul dispositivo. Non appena spegni il dispositivo, questo ritorna al suo stato predefinito e richiede una nuova immissione della passphrase completa per accedere agli account nascosti. Questa opzione di "passphrase temporanea" è quindi simile al funzionamento di altri portafogli hardware.
In questo tutorial, userò il Ledger Flex come esempio. Tuttavia, se stai utilizzando un altro modello di Ledger, il processo rimane lo stesso. Per il Ledger Stax, l'interfaccia è la stessa del Ledger Flex. Per quanto riguarda i modelli Nano S, Nano S Plus e Nano X, anche se l'interfaccia è diversa, il processo e i nomi dei menu rimangono gli stessi.
**Attenzione:** Se hai già ricevuto bitcoin sul tuo Ledger prima di attivare la passphrase, dovrai trasferirli tramite una transazione Bitcoin. La passphrase genera un insieme di nuove chiavi, creando così un portafoglio completamente indipendente dal tuo portafoglio iniziale. Aggiungendo la passphrase, avrai un nuovo portafoglio che sarà vuoto. Tuttavia, questo non cancella il tuo primo portafoglio senza passphrase. Puoi ancora accedervi, direttamente tramite il tuo Ledger senza inserire la passphrase o tramite un altro software utilizzando la tua frase di 24 parole.
Prima di iniziare questo tutorial, assicurati di aver già inizializzato il tuo Ledger e generato la tua frase mnemonica. Se non è così e il tuo Ledger è nuovo, segui il tutorial specifico per il tuo modello disponibile su PlanB Network. Una volta completato questo passaggio, puoi tornare a questo tutorial.

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a
https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4
https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## Come impostare una passphrase temporanea con un Ledger?

Nella homepage del tuo Ledger, clicca sull'icona dell'ingranaggio delle impostazioni.

![PASSPHRASE BIP39](assets/notext/04.webp)

Seleziona il menu "Avanzate", poi "Imposta passphrase".

![PASSPHRASE BIP39](assets/notext/05.webp)

Questo è il passaggio in cui puoi scegliere tra l'opzione "collegata al PIN" o l'opzione "temporanea" di cui abbiamo parlato nella parte precedente. Qui, spiegherò come impostare una passphrase temporanea, quindi clicca su "Imposta passphrase temporanea".

![PASSPHRASE BIP39](assets/notext/06.webp)
Ti verrà chiesto di inserire la tua passphrase. Scegli una passphrase forte e procedi immediatamente con un backup fisico, su un supporto come carta o metallo. In questo esempio, ho scelto la passphrase: `fH3&kL@9mP#2sD5qR!82`. Dopo aver inserito la tua passphrase, clicca sul pulsante "*Continua*".
![PASSPHRASE BIP39](assets/notext/07.webp)

Verifica che la tua passphrase corrisponda a quanto hai annotato sul tuo backup fisico, poi clicca sul pulsante "*Sì, è corretto*" per confermare.

![PASSPHRASE BIP39](assets/notext/08.webp)

Per finalizzare la creazione della tua passphrase, inserisci il codice PIN del tuo Ledger. D'ora in poi, ogni volta che vorrai accedere al tuo portafoglio con una passphrase sul Ledger, dovrai seguire esattamente gli stessi passaggi descritti qui.

![PASSPHRASE BIP39](assets/notext/09.webp)

Ora puoi importare il tuo insieme di chiavi pubbliche su Sparrow Wallet per gestire il tuo portafoglio. Su Sparrow, questo corrisponderà a un portafoglio diverso dal tuo portafoglio iniziale senza passphrase.

Apri Sparrow Wallet. Assicurati che il software sia connesso a un nodo, poi clicca sulla scheda "*File*" e seleziona "*Nuovo Portafoglio*".

![PASSPHRASE BIP39](assets/notext/10.webp)

Scegli un nome per il tuo portafoglio protetto da passphrase. Per questo esempio, ho optato per un nome che include esplicitamente il termine "*passphrase*". Tuttavia, se preferisci mantenere la discrezione di questo portafoglio sul tuo computer, puoi scegliere un nome meno evocativo.

![PASSPHRASE BIP39](assets/notext/11.webp)

Scegli il tipo di script per il tuo portafoglio. Ti consiglio di scegliere "*Taproot*" o alternativamente "*Native SegWit*".

![PASSPHRASE BIP39](assets/notext/12.webp)
Collega il tuo Ledger al computer, poi clicca su "*Connected Hardware Wallet*". Assicurati di aver già inserito la tua passphrase sul tuo Ledger. Se non l'hai fatto, per favore torna ai passaggi precedenti per inserire la tua passphrase. Prima di procedere alla scansione, ricorda anche di aprire l'applicazione "*Bitcoin*" sul tuo Ledger.

Clicca sul pulsante "*Scan...*".

Clicca su "*Import Keystore*" accanto al tuo Ledger.

Il tuo portafoglio protetto dalla passphrase è ora creato su Sparrow. Per confermare, clicca sul pulsante "*Apply*".

Scegli una password forte per proteggere l'accesso a Sparrow Wallet. Questa password garantirà la sicurezza dell'accesso ai dati del tuo portafoglio su Sparrow, aiutando a proteggere le tue chiavi pubbliche, indirizzi, etichette e la cronologia delle transazioni da qualsiasi accesso non autorizzato.
Ti consiglio di salvare questa password in un gestore di password per non dimenticarla.

Ed ecco fatto, il tuo portafoglio è ora creato! Nel menu "*Settings*", Sparrow ti fornirà il tuo "*Master fingerprint*". Questo rappresenta l'impronta digitale della tua chiave principale, usata come base per derivare il tuo portafoglio. Ti raccomando vivamente di tenere una copia di questa impronta digitale. Nel mio esempio, corrisponde a: `281ee33a`.

Ricorda ciò che abbiamo menzionato nelle parti precedenti: un errore, anche minore, nell'inserimento della tua passphrase genererà un portafoglio completamente nuovo con chiavi diverse. Ogni volta che devi assicurarti di accedere al portafoglio giusto con la passphrase corretta, controlla che l'impronta digitale della tua chiave principale corrisponda a quella che hai annotato. Questa informazione, di per sé, non rappresenta un rischio per la sicurezza dei tuoi fondi o per la tua privacy.

Prima di usare il tuo portafoglio con una passphrase, ti consiglio vivamente di eseguire un test di recupero a secco. Annota un pezzo di informazione di riferimento come il tuo xpub o l'impronta digitale della tua chiave principale, poi resetta il tuo Ledger mentre il portafoglio è ancora vuoto. Successivamente, prova a ripristinare il tuo portafoglio sul Ledger usando i tuoi backup cartacei della frase di 24 parole e della passphrase. Controlla che le informazioni generate dopo il ripristino corrispondano a quelle che avevi inizialmente annotato. Se è così, puoi essere sicuro che i tuoi backup cartacei sono affidabili.

## Come impostare una passphrase collegata a un PIN con un Ledger?

Nella homepage del tuo Ledger, clicca sulla ruota dentata delle impostazioni.

Seleziona il menu "*Advanced*", poi "*Set passphrase*".

Questo è il passaggio in cui puoi scegliere tra l'opzione "*linked to PIN*" o "*temporary*" di cui abbiamo parlato nella parte precedente. Qui, spiegherò come impostare una passphrase collegata a un nuovo PIN, quindi clicca su "*Set passphrase and attach it to a new PIN*".

Dovrai quindi scegliere il codice PIN che sarà associato alla tua passphrase. Proprio come con il codice PIN principale, si raccomanda di scegliere un codice PIN di 8 cifre, il più casuale possibile. Inoltre, assicurati di salvare questo codice in un luogo diverso da dove è conservato il tuo Ledger Flex.
Nel mio caso, il codice PIN principale è `58293647` e ho scelto `71425839` come codice PIN secondario associato alla passphrase.
![PASSPHRASE BIP39](assets/notext/22.webp)

Viene quindi richiesto di inserire la vostra passphrase. Scegliete una passphrase forte e procedete immediatamente con un backup fisico, su un supporto come carta o metallo. In questo esempio, ho scelto la passphrase: `fH3&kL@9mP#2sD5qR!82`. Dopo aver inserito la vostra passphrase, cliccate sul pulsante "*Continua*".

![PASSPHRASE BIP39](assets/notext/23.webp)

Verificate che la vostra passphrase corrisponda a quanto avete annotato sul backup fisico, poi cliccate sul pulsante "*Sì, è corretto*" per confermare.

![PASSPHRASE BIP39](assets/notext/24.webp)

Per finalizzare la creazione della vostra passphrase, inserite il codice PIN principale del vostro Ledger (non quello associato alla passphrase).

![PASSPHRASE BIP39](assets/notext/25.webp)

D'ora in poi, ogni volta che vorrete accedere al vostro portafoglio con una passphrase sul Ledger, dovrete inserire non il codice PIN principale, ma il codice PIN secondario:
- Codice PIN principale (`58293647`) > portafoglio senza passphrase.
- Codice PIN secondario (`71425839`) > portafoglio con passphrase.

Ora potete importare il vostro insieme di chiavi pubbliche su Sparrow Wallet per gestire il vostro portafoglio. Su Sparrow, questo corrisponderà a un portafoglio diverso dal vostro portafoglio iniziale senza passphrase.

Aprite Sparrow Wallet. Assicuratevi che il software sia connesso a un nodo, poi cliccate sulla scheda "*File*" e selezionate "*Nuovo Portafoglio*".

![PASSPHRASE BIP39](assets/notext/26.webp)

Scegliete un nome per il vostro portafoglio protetto da passphrase. Per questo esempio, ho optato per un nome che include esplicitamente il termine "*passphrase*". Tuttavia, se preferite mantenere la discrezione di questo portafoglio sul vostro computer, potete scegliere un nome meno evocativo.

![PASSPHRASE BIP39](assets/notext/27.webp)

Scegliete il tipo di script per il vostro portafoglio. Vi consiglio di scegliere "*Taproot*" o, in mancanza di questo, "*Native SegWit*".

![PASSPHRASE BIP39](assets/notext/28.webp)
Collegate il vostro Ledger al computer, poi cliccate su "*Connected Hardware Wallet*". Assicuratevi di avere già la vostra passphrase sul Ledger sbloccandolo con il codice PIN secondario. In caso contrario, riavviate il vostro Ledger e inserite il codice PIN associato alla passphrase. Prima di procedere alla scansione, ricordatevi anche di aprire l'applicazione "*Bitcoin*" sul vostro Ledger.

![PASSPHRASE BIP39](assets/notext/29.webp)

Cliccate sul pulsante "*Scansiona...*".

![PASSPHRASE BIP39](assets/notext/30.webp)

Cliccate su "*Importa Keystore*".

![PASSPHRASE BIP39](assets/notext/31.webp)

Il vostro portafoglio protetto dalla passphrase è ora creato su Sparrow. Per confermare, cliccate sul pulsante "*Applica*".

![PASSPHRASE BIP39](assets/notext/32.webp)

Scegliete una password forte per proteggere l'accesso a Sparrow Wallet. Questa password garantirà la sicurezza dell'accesso ai dati del vostro portafoglio su Sparrow, contribuendo a proteggere le vostre chiavi pubbliche, indirizzi, etichette e cronologia delle transazioni da qualsiasi accesso non autorizzato.

Vi consiglio di salvare questa password in un gestore di password per non dimenticarla.
Ecco fatto, il tuo portafoglio è ora creato! Nel menu "*Impostazioni*", Sparrow ti fornirà il tuo "*Master fingerprint*". Questo rappresenta l'impronta digitale della tua chiave principale, utilizzata alla base della derivazione del tuo portafoglio. Ti consiglio vivamente di conservare una copia di questa impronta digitale. Nel mio esempio, corrisponde a: `281ee33a`.

Ricorda ciò che abbiamo menzionato nelle parti precedenti: un errore, anche minore, nell'inserimento della tua passphrase genererà un portafoglio completamente nuovo con chiavi diverse. Ogni volta che devi assicurarti di accedere al portafoglio corretto con la passphrase giusta, verifica che l'impronta digitale della tua chiave principale corrisponda a quella che hai annotato. Questa informazione, di per sé, non rappresenta un rischio per la sicurezza dei tuoi fondi o per la tua privacy.
Prima di utilizzare il tuo portafoglio con una passphrase, ti consiglio vivamente di eseguire un test di recupero a secco. Annota un pezzo di informazione di riferimento come il tuo xpub o l'impronta digitale della tua chiave principale, poi resetta il tuo Ledger mentre il portafoglio è ancora vuoto. Successivamente, prova a ripristinare il tuo portafoglio sul Ledger utilizzando i tuoi backup cartacei della frase di 24 parole e della passphrase. Controlla che le informazioni generate dopo il ripristino corrispondano a quelle che avevi inizialmente annotato. Se è così, puoi essere sicuro che i tuoi backup cartacei sono affidabili.

Congratulazioni, il tuo portafoglio Bitcoin è ora protetto con una passphrase! Se hai trovato utile questo tutorial, apprezzerei se potessi lasciare un pollice in su qui sotto. Sentiti libero di condividere questo articolo sui tuoi social network. Grazie mille!

Ti consiglio anche di dare un'occhiata a questo altro tutorial completo su come utilizzare il tuo Ledger Flex:

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a
---
name: BitBox02

description: Configurazione e utilizzo di un BitBox02
---

![cover](assets/cover.webp)

Il BitBox02 (https://bitbox.swiss/) è un portafoglio fisico svizzero appositamente progettato per proteggere i tuoi Bitcoin. Alcune delle sue caratteristiche principali includono un facile backup e ripristino tramite una scheda microSD, un design minimalista e discreto e un supporto completo per Bitcoin.

![device](assets/1.webp)

Offre una sicurezza all'avanguardia progettata da esperti, con un design a doppio chip che include un chip sicuro. Il suo codice sorgente è stato completamente auditato da ricercatori di sicurezza ed è completamente open-source. Il BitBox02 è dotato di un'app BitBoxApp semplice ma potente, che offre una gestione sicura dei tuoi Bitcoin. Supporta il nodo completo per Bitcoin e garantisce una comunicazione crittografata end-to-end tra l'app e il dispositivo. Prodotto in Svizzera, il BitBox02 ha guadagnato una reputazione positiva tra i suoi utenti.

![video](https://youtu.be/sB4b2PbYaj0)

> Specifiche
>
> - Connettività: USB-C
> - Compatibilità: Windows 7 e successivi, macOS 10.13 e successivi, Linux, Android
> - Input: Sensori capacitivi touch
> - Microcontrollore: ATSAMD51J20A; 120 Mhz 32-bit Cortex-M4F; Generatore di numeri casuali vero
> - Chip sicuro: ATECC608B; Generatore di numeri casuali vero (NIST SP 800-90A/B/C)
> - Display: 128 x 64 px OLED bianco
> - Materiale: Policarbonato
> - Dimensioni: 54,5 x 25,4 x 9,6 mm inclusa la spina USB-C
> - Peso: Dispositivo 12g; con imballaggio e accessori 160g

Scarica i datasheet sul loro sito web https://bitbox.swiss/bitbox02/

## Come utilizzare il portafoglio hardware BitBox02

### Configurazione del BitBox02

Il BitBox02 ha una connessione USB-C collegata al guscio. Se il tuo computer utilizza la porta USB normale, dovrai utilizzare l'adattatore fornito con il dispositivo.

Collegalo al tuo computer e il dispositivo si accenderà (non farlo ancora).

Ha sensori sopra e sotto e ti chiederà di toccare la parte superiore o inferiore per orientare lo schermo come preferisci.

![image](assets/2.webp)

### Scarica l'app BitBox02

Visita https://shiftcrypto.ch/ e clicca sul link "App" in alto per accedere alla pagina di download:

![image](assets/3.webp)

Clicca sul pulsante blu "Download":

![image](assets/4.webp)

Per verificare il download (aggiunge complessità, ma è consigliato, soprattutto se archivi molte bitcoin), consulta l'Appendice A.

Dopo il download, puoi decomprimere il file. Su un Mac, basta fare doppio clic sul file scaricato e comparirà un'icona dell'app BitBox nella directory dei download. Puoi trascinarla sul desktop (o ovunque) per un accesso facile.

Fai doppio clic sull'app per avviarla (non viene "installata").

Su Mac, il tuo computer ti darà un avviso. Ignoralo e clicca su "Apri":

![image](assets/5.webp)

Vedrai quindi questo:

![image](assets/6.webp)

Procedi e collega il dispositivo al computer.
Mostrerà un codice di abbinamento. Verifica che corrispondano e poi tocca il sensore per selezionare il segno di spunta. Quindi torna alla schermata, il pulsante "Continua" diventerà disponibile per te.
![image](assets/7.webp)

Successivamente avrai l'opzione di creare un nuovo seed o ripristinare un seed. Dimostrerò come creare un nuovo seed (È importante anche ripristinare il seed creato per testare la qualità del tuo backup, prima di caricare bitcoin sul portafoglio).

![image](assets/8.webp)

Il dispositivo è fornito con una scheda microSD. Inseriscila se non l'hai ancora fatto.

![image](assets/9.webp)

Dai un nome al tuo dispositivo e clicca su "Continua", poi conferma sul dispositivo.

![image](assets/10.webp)

Ti verrà quindi chiesto di impostare una password per il dispositivo. Questa non fa parte del tuo seed. Non è nemmeno una frase di accesso (che fa parte del tuo seed). È semplicemente una password per bloccare il dispositivo. Quando accendi il dispositivo, ti verrà chiesto di inserire questa password ogni volta. Hai 10 tentativi consecutivi consentiti prima che il dispositivo cancelli completamente la memoria, quindi fai attenzione. L'animazione sullo schermo ti insegnerà come utilizzare i controlli del dispositivo per impostare la password.

![image](assets/11.webp)

Leggi la schermata successiva, spunta ogni casella e poi continua.

![image](assets/12.webp)
![image](assets/13.webp)
![image](assets/14.webp)

Ed ecco come appare il portafoglio una volta pronto all'uso.

![image](assets/15.webp)

### NON COSÌ VELOCE!!

È piuttosto strano, ma il BitBox02 ci sta dicendo che siamo pronti per utilizzare il dispositivo, ma non ci ha chiesto di annotare le parole del seed! L'UNICO backup che abbiamo è il file salvato sulla scheda microSD. Questo non è sufficiente. Questi dispositivi di archiviazione non durano per sempre (a causa della "bit rot"). Abbiamo bisogno di un backup su carta e duplicati, conservati in una cassaforte (come spiegato nella guida generale su come utilizzare i portafogli hardware)

Per ottenere la frase del seed e scriverla, vai alla scheda "Gestisci dispositivo" a sinistra e poi clicca su "Mostra parole di recupero"

![image](assets/16.webp)

Puoi quindi passare attraverso la conferma e il dispositivo ti presenterà le parole. Scrivile in modo ordinato e non far vedere a nessuno le parole.

![image](assets/17.webp)

Dopo di ciò, puoi cliccare sulla scheda Bitcoin a sinistra per ottenere i tuoi indirizzi di ricezione.

![image](assets/18.webp)

Mostra uno alla volta, ma almeno ti permette di scegliere quale indirizzo utilizzare tra i primi 20:

![image](assets/19.webp)

Cliccando sul pulsante blu verrà mostrato l'indirizzo completo e ti verrà chiesto di verificare che l'indirizzo corrisponda a quello visualizzato sullo schermo. Questa è una buona pratica per confermare che nessun malware sul tuo computer ti sta ingannando per inviare bitcoin a un indirizzo di un attaccante.

![image](assets/20.webp)

Per inviare bitcoin a questo portafoglio, puoi copiare l'indirizzo e incollarlo nella pagina di prelievo dello scambio dove si trovano le tue monete. Ti consiglio di inviare prima una piccola quantità di prova, poi esercitarti a spenderla sia tornando allo scambio che all'indirizzo secondario nel tuo portafoglio.

Per importi più grandi, ti consiglio di creare una frase di accesso (vedi sotto). Il portafoglio originale (senza frase di accesso) può essere utilizzato come portafoglio fittizio (deve contenere una quantità ragionevole per essere credibile come fittizio).

### Connettiti a un nodo

Il BitBox02 si connetterà automaticamente a un nodo. Vediamo dove si sta connettendo. Fai clic sulla scheda delle impostazioni a sinistra e poi su "connetti il tuo nodo completo".

![image](assets/21.webp)

E qui possiamo vedere che si sta connettendo al nodo di shiftcrypto. Non è ottimo. Abbiamo tradito tutti i nostri indirizzi bitcoin a loro e il nostro indirizzo IP (ovviamente non il seed; possono vedere i nostri indirizzi/saldi, ma non possono spenderli). Possiamo inserire i dettagli del nostro nodo in questa pagina (oltre allo scopo di questa guida specifica) o possiamo utilizzare software migliore come Sparrow Bitcoin Wallet, Electrum Desktop Wallet o Specter Desktop. Dimostrerò Sparrow Bitcoin Wallet più avanti nella guida.

![image](assets/22.webp)

Aggiungi una passphrase

Ora che abbiamo configurato il dispositivo con l'app BitBox02 (e rivelato i nostri indirizzi, inevitabile con questo particolare portafoglio hardware), possiamo aggiungere una passphrase alla nostra frase seed. Questo ci permetterà di creare un nuovo portafoglio utilizzando lo stesso seed e ShiftCrypto non vedrà mai i nostri nuovi indirizzi. Connetteremo questo portafoglio solo al nostro software.

### Abilita la passphrase

Vai avanti ora e "abilita" la funzione passphrase (ma non stiamo ancora impostando una passphrase). Vai alla scheda "gestisci dispositivo" e fai clic su "abilita passphrase" (cerchio rosso sotto).

![image](assets/23.webp)

Leggi i passaggi...

![image](assets/24.webp)
![image](assets/25.webp)
![image](assets/26.webp)

Ora scollega il dispositivo e chiudi l'app BitBox02

FINE della sezione bitbox02 di Parman.

Il tuo dispositivo è ora completamente operativo per essere utilizzato su qualsiasi soluzione desktop come specter, sparrow e utilizzando l'interfaccia bitbox.

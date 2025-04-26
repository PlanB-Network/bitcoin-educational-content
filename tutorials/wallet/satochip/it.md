---
name: Satochip
description: Configurazione e utilizzo di una smart card Satochip
---

![cover](assets/cover.webp)

Un portafoglio hardware è un dispositivo elettronico dedicato alla gestione e alla sicurezza delle chiavi private di un portafoglio Bitcoin. A differenza dei portafogli software (o hot wallet) installati su macchine di uso generale spesso connesse a Internet, i portafogli hardware permettono l'isolamento fisico delle chiavi private, riducendo i rischi di hacking e furto.

L'obiettivo principale di un portafoglio hardware è minimizzare le funzionalità del dispositivo per ridurre la sua superficie di attacco. Una superficie di attacco più piccola significa anche meno vettori di attacco potenziali, ovvero meno debolezze nel sistema che gli aggressori potrebbero sfruttare per accedere ai bitcoin.

Si raccomanda di utilizzare un portafoglio hardware per proteggere i propri bitcoin, specialmente se si detengono quantità significative, sia in valore assoluto sia come proporzione dei propri asset totali.

I portafogli hardware sono utilizzati in combinazione con software di gestione del portafoglio su un computer o smartphone. Questo software gestisce la creazione di transazioni, ma la firma crittografica necessaria per validare queste transazioni viene eseguita esclusivamente all'interno del portafoglio hardware. Ciò significa che le chiavi private non sono mai esposte a un ambiente potenzialmente vulnerabile.

I portafogli hardware offrono una doppia protezione per l'utente: da un lato, proteggono i bitcoin da attacchi remoti mantenendo le chiavi private offline e, dall'altro, offrono generalmente una migliore resistenza fisica contro i tentativi di estrarre le chiavi. Ed è proprio su questi 2 criteri di sicurezza che si può giudicare e classificare i diversi modelli disponibili sul mercato.

In questo tutorial, propongo di scoprire una di queste soluzioni: il Satochip.

## Introduzione a Satochip

Il Satochip è un portafoglio hardware sotto forma di carta con un chip certificato _EAL6+_, che rappresenta uno standard di sicurezza molto elevato (_NXP JCOP_). È prodotto da un'azienda belga.

![SATOCHIP](assets/notext/01.webp)

Questa smart card è venduta a €25, che è molto conveniente rispetto ad altri portafogli hardware sul mercato. Il chip è un elemento sicuro che garantisce un'ottima resistenza contro gli attacchi fisici. Inoltre, il suo codice è open-source (_AGPLv3_).
Tuttavia, a causa del suo formato, il Satochip non offre tante opzioni quanto altri hardware. Ovviamente non c'è batteria, né fotocamera, né lettore di schede micro SD, essendo una carta. Il suo più grande svantaggio, a mio parere, è la mancanza di uno schermo sul portafoglio hardware, che lo rende più vulnerabile a certi tipi di attacchi remoti. Infatti, ciò costringe l'utente a firmare alla cieca e a fidarsi di ciò che vede sullo schermo del proprio computer.

Nonostante le sue limitazioni, il Satochip rimane interessante per il suo prezzo ridotto. Questo portafoglio può in particolare essere utilizzato per aumentare la sicurezza di un portafoglio di spesa in aggiunta a un portafoglio di risparmio protetto da un portafoglio hardware dotato di schermo. Costituisce anche una buona soluzione per coloro che detengono piccole quantità di bitcoin e non desiderano investire centinaia di euro in un dispositivo più sofisticato. Inoltre, l'uso di Satochip in configurazioni multisig, o potenzialmente in sistemi di portafoglio con timelock in futuro, può offrire vantaggi interessanti.

L'azienda Satochip offre anche altri 2 prodotti. C'è il Satodime, che è una carta portatore progettata per conservare offline i bitcoin, ma non permette transazioni. È una sorta di portafoglio di carta molto più sicuro, che può essere utilizzato, ad esempio, per fare un regalo. Infine, c'è il Seedkeeper, che è un gestore di frasi mnemoniche. Può essere utilizzato per salvare in modo sicuro il nostro seed senza che sia direttamente annotato su un pezzo di carta.

## Come acquistare un Satochip?

Il Satochip è disponibile per l'acquisto [sul sito ufficiale](https://satochip.io/product/satochip/). Per comprarlo in un negozio fisico, puoi anche trovare [l'elenco dei rivenditori certificati](https://satochip.io/resellers/) sul sito web di Satochip.
Per interagire con il tuo software di gestione del portafoglio, il Satochip offre due possibilità: tramite comunicazione NFC o tramite un lettore di smart card. Per l'opzione NFC, assicurati che il tuo dispositivo sia compatibile con questa tecnologia o procurati un lettore NFC esterno. Il Satochip opera alla frequenza standard di 13,56 MHz. In alternativa, puoi anche acquistare un lettore di smart card. Puoi trovarne uno sul sito web di Satochip o altrove.

![SATOCHIP](assets/notext/02.webp)

## Come configurare un Satochip con Sparrow?

Una volta ricevuto il tuo Satochip, il primo passo è esaminare l'imballaggio per assicurarti che non sia stato aperto. La confezione del Satochip dovrebbe includere un adesivo di sigillo. Se questo adesivo manca o è danneggiato, potrebbe indicare che la smart card è stata compromessa e potrebbe non essere autentica.
![SATOCHIP](assets/notext/03.webp)
Troverai il Satochip all'interno.

![SATOCHIP](assets/notext/04.webp)

Per gestire il portafoglio, in questo tutorial, suggerisco di utilizzare Sparrow. Se non hai ancora il software, [visita il sito ufficiale per scaricarlo](https://sparrowwallet.com/download/). Puoi anche consultare il nostro tutorial su Sparrow Wallet (prossimamente).

![SATOCHIP](assets/notext/05.webp)

Inserisci il tuo Satochip nel lettore di smart card o posizionalo sul lettore NFC e collega il lettore al tuo computer su cui è aperto Sparrow.

![SATOCHIP](assets/notext/06.webp)

Apri Sparrow Wallet e assicurati di essere correttamente connesso a un nodo Bitcoin. Per fare ciò, controlla la spunta in basso a destra: dovrebbe essere gialla se sei connesso a un nodo pubblico, verde per una connessione a Bitcoin Core o blu per Electrum.

![SATOCHIP](assets/notext/07.webp)

Su Sparrow Wallet, clicca sulla scheda "_File_".

![SATOCHIP](assets/notext/08.webp)

Poi sul menu "_Nuovo Portafoglio_".

![SATOCHIP](assets/notext/09.webp)

Scegli un nome per il tuo portafoglio e poi clicca su "_Crea Portafoglio_".

![SATOCHIP](assets/notext/10.webp)

Clicca sul pulsante "_Portafoglio Hardware Connesso_".

![SATOCHIP](assets/notext/11.webp)

Clicca sul pulsante "_Scansiona..._".

![SATOCHIP](assets/notext/12.webp)

Il tuo Satochip dovrebbe apparire. Clicca su "_Importa Keystore_".

![SATOCHIP](assets/notext/13.webp)

Successivamente, devi impostare un codice PIN per sbloccare il tuo Satochip. Scegli una password forte, tra 4 e 16 caratteri. Fai un backup di questa password.

Sii consapevole, questa password non è una passphrase. Questo significa che anche senza questa password, la tua frase mnemonica ti permetterà di re-importare il tuo portafoglio nel software se necessario. La password è utilizzata solo per garantire l'accesso al Satochip stesso. È equivalente al codice PIN trovato su altri portafogli hardware.

Una volta inserita la password, clicca nuovamente sul pulsante "_Importa Keystore_".

![SATOCHIP](assets/notext/14.webp)

Annota nuovamente la password, poi clicca sul pulsante "_Inizializza_".
![SATOCHIP](assets/notext/15.webp)
Arrivi quindi alla finestra per generare la tua frase mnemonica. Clicca sul pulsante "_Genera Nuova_".

![SATOCHIP](assets/notext/16.webp)
Effettua una o più copie fisiche della tua frase di recupero scrivendola su un supporto di carta o metallo. Attenzione, questa frase concede l'accesso completo ai tuoi bitcoin senza alcuna protezione aggiuntiva. Pertanto, se qualcuno dovesse scoprirla, potrebbe rubare istantaneamente i tuoi bitcoin, anche senza accesso al tuo Satochip o al suo codice PIN. È quindi importante mettere al sicuro queste copie di backup. Inoltre, questa frase ti permette di riaccedere ai tuoi bitcoin in caso di perdita, danneggiamento del Satochip, o se dimentichi il tuo codice PIN.
![SATOCHIP](assets/notext/17.webp)

Il tuo portafoglio Bitcoin è stato creato con successo.

![SATOCHIP](assets/notext/18.webp)

Clicca nuovamente sul pulsante "_Importa Keystore_".

![SATOCHIP](assets/notext/19.webp)

Il tuo portafoglio è ora creato. Le tue chiavi private sono ora memorizzate sulla smartcard del tuo Satochip. Clicca sul pulsante "_Applica_" per continuare.

![SATOCHIP](assets/notext/20.webp)

Si raccomanda di impostare una password aggiuntiva per proteggere le informazioni pubbliche gestite da Sparrow Wallet, oltre al codice PIN del tuo Satochip. Questa password garantirà la sicurezza dell'accesso a Sparrow Wallet, contribuendo a proteggere le tue chiavi pubbliche, indirizzi e la cronologia delle transazioni da qualsiasi accesso non autorizzato.

![SATOCHIP](assets/notext/21.webp)

Inserisci la tua password nei due campi, poi clicca sul pulsante "_Imposta Password_".

![SATOCHIP](assets/notext/22.webp)

Ed ecco fatto, il tuo Satochip è ora configurato su Sparrow Wallet.

![SATOCHIP](assets/notext/23.webp)

Ora che il tuo portafoglio è creato, puoi scollegare il tuo Satochip. Tienilo in un luogo sicuro!

## Come ricevere bitcoin con il Satochip?

Una volta nel tuo portafoglio, clicca sulla scheda "_Ricevi_".

![SATOCHIP](assets/notext/24.webp)

Sparrow Wallet genera un indirizzo per il tuo portafoglio. Solitamente, per altri portafogli hardware, si consiglia di cliccare su "_Mostra Indirizzo_" per verificare l'indirizzo direttamente sullo schermo del dispositivo. Purtroppo, questa opzione non è disponibile con il Satochip, ma assicurati di utilizzarla per i tuoi altri portafogli.

![SATOCHIP](assets/notext/25.webp)

Puoi aggiungere un "_Etichetta_" per descrivere la fonte dei bitcoin che saranno assicurati con questo indirizzo. Questa è una buona pratica che ti aiuta a gestire meglio i tuoi UTXO.

![SATOCHIP](assets/notext/26.webp)

Per maggiori informazioni sull'etichettatura, ti consiglio anche di consultare questo altro tutorial:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Puoi quindi utilizzare questo indirizzo per ricevere bitcoin.

![SATOCHIP](assets/notext/27.webp)

## Come inviare Bitcoin con Satochip?

Ora che hai ricevuto i tuoi primi satoshi nel tuo portafoglio sicuro con Satochip, puoi anche spenderli! Collega il tuo Satochip al computer, avvia Sparrow Wallet e poi vai alla scheda "_Invia_" per costruire una nuova transazione.

![SATOCHIP](assets/notext/28.webp)
Se vuoi eseguire il controllo delle monete, ovvero scegliere specificamente quali UTXO consumare nella transazione, vai alla scheda "_UTXOs_". Seleziona gli UTXO che desideri spendere, poi clicca su "_Invia Selezionati_". Sarai reindirizzato alla stessa schermata della scheda "_Invia_", ma con i tuoi UTXO già selezionati per la transazione.

Inserisci l'indirizzo di destinazione. Puoi anche inserire più indirizzi cliccando sul pulsante "_+ Aggiungi_".

Nota una "_Etichetta_" per ricordare lo scopo di questa spesa.

Scegli l'importo da inviare a questo indirizzo.

Regola la tariffa della commissione della tua transazione in base al mercato attuale.

Assicurati che tutti i parametri della tua transazione siano corretti, poi clicca su "_Crea Transazione_".

Se tutto è di tuo gradimento, clicca su "_Finalizza Transazione per la Firma_".

Clicca su "_Firma_".

Clicca nuovamente su "_Firma_" accanto al tuo Satochip.

Inserisci il codice PIN del tuo Satochip, poi clicca nuovamente su "_Firma_" per firmare la tua transazione.

La tua transazione è ora firmata. Clicca su "_Trasmetti Transazione_" per diffonderla nella rete Bitcoin.

Puoi trovarla nella scheda "_Transazioni_" di Sparrow Wallet.

Congratulazioni, ora sei informato su come usare Satochip! Se hai trovato utile questo tutorial, apprezzerei un pollice in su qui sotto. Sentiti libero di condividere questo articolo sui tuoi social network. Grazie mille!


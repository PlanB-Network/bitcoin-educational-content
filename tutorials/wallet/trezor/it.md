---
name: Trezor model One
description: Configurazione e utilizzo di Trezor model One
---

![cover](assets/cover.webp)

Portafoglio hardware a freddo - 60€ - Principiante - Sicuro tra 2.000€ e 50.000€.

Come portafoglio fisico a freddo, Trezor è ideale per iniziare con Bitcoin. È facile da usare, non troppo costoso e funzionale.

Abbiamo già realizzato tutorial su come utilizzarlo:

1. Configurazione
2. Recupero di bitcoin
3. Utilizzo, invio e ricezione di bitcoin

Ti piacerebbe avere anche il tuo Trezor?
Puoi contribuire al progetto cliccando qui sotto!

configurazione: https://www.youtube.com/watch?v=q-BlT6R4_bE

recupero: https://www.youtube.com/watch?v=3n4d4egjiFM

utilizzo: https://www.youtube.com/watch?v=syouZjLC1zY

## guida alla scrittura

guida proposta da https://armantheparman.com/trezor/

## Configurazione di Trezor

Trezor viene fornito con il suo cavo micro USB. Assicurati di utilizzare quello e non un vecchio cavo qualsiasi. Alcuni cavi USB sono solo per la ricarica. Questo trasmette dati E alimentazione. Se utilizzi il dispositivo con un cavo USB per la ricarica del telefono, il dispositivo potrebbe non riuscire a connettersi.

Collegalo al tuo computer e il dispositivo si accenderà. Riceverai un messaggio che dice "Vai su Trezor.io/start". Fallo e scarica Trezor Suite sul tuo computer.

![image](assets/0.webp)

Clicca sul pulsante di download ("Ottieni app desktop")

![image](assets/1.webp)

Nota i link Signature e Signing key. Per verificare il download (controllare che il download non sia stato manomesso), ci sono ulteriori passaggi che sono facoltativi se stai iniziando, ma OBBLIGATORI se hai una ricchezza significativa da proteggere. Le istruzioni per questo si trovano nell'Appendice A (fine della guida).

Collega Trezor al computer con il cavo micro USB e installa ed esegui il programma. Ecco come appare su un Mac:

![image](assets/2.webp)

Riceverai un avviso sciocco dopo aver eseguito il programma, continua semplicemente:

![image](assets/3.webp)

Clicca su Configura Trezor

![image](assets/4.webp)

Se il firmware è obsoleto, permetti a Trezor di aggiornare il firmware.

Successivamente, puoi creare un nuovo seed o ripristinare un portafoglio da un dispositivo diverso con un seed che hai già. Passerò attraverso la creazione di un nuovo seed.

![image](assets/5.webp)

Clicca su "Crea nuovo portafoglio" - e conferma che desideri farlo sul dispositivo stesso cliccando sul pulsante di conferma.

Quindi clicca sull'unica opzione "Backup seed standard"

![image](assets/6.webp)

Poi clicca su "crea backup"

![image](assets/7.webp)

Clicca sui tre segni di spunta per renderli verdi (naturalmente leggi ogni messaggio) e poi clicca su "inizia backup".

![image](assets/8.webp)

Successivamente, vedrai questo:

![image](assets/9.webp)

Sul dispositivo, vedi le parole presentate una per una e scrivile ORDINATAMENTE e NELL'ORDINE.

![image](assets/10.webp)

Imposta un PIN per bloccare il dispositivo (questo non fa parte del tuo seed, serve solo per bloccare il dispositivo in modo che nessuno possa accedere al seed contenuto all'interno).

![image](assets/11.webp)

Hai la possibilità di aggiungere shitcoin al tuo portafoglio - ti esorto a non farlo e a salvare solo in Bitcoin, come spiego qui (perché Bitcoin) e qui (solo Bitcoin).

![image](assets/12.webp)

Dai un nome al tuo portafoglio e clicca su "Access Suite":

![image](assets/13.webp)

È più semplice creare un portafoglio senza frase di accesso, ma è meglio crearne uno con una frase di accesso (il tuo vero portafoglio) E uno senza frase di accesso (il tuo portafoglio fittizio). Ogni volta che accedi al dispositivo tramite Trezor Suite, ti verrà chiesto se vuoi "applicare" la frase di accesso o meno.

![image](assets/14.webp)

Ho selezionato "Hidden Wallet" e ho digitato una frase di accesso che ho inventato "craigwrightisaliarandafraud"

![image](assets/15.webp)

Mi piace come viene chiamato un portafoglio "nascosto", poiché spiega in parte come funzionano le frasi di accesso.

Conferma la frase di accesso sul dispositivo.

Poiché questo portafoglio è vuoto, mi è stato chiesto di confermare che la frase di accesso sia corretta:

![image](assets/16.webp)

Ti verrà quindi chiesto se desideri abilitare l'etichettatura. Non è qualcosa che ho esplorato, ma sembra un modo per etichettare le tue transazioni e salvare i dati sul tuo computer o sul cloud.

![image](assets/17.webp)

Infine, il tuo portafoglio sarà disponibile:

![image](assets/18.webp)

Quello che hai sul tuo computer è ciò che viene chiamato un "portafoglio di osservazione", perché contiene le tue chiavi pubbliche (e indirizzi), ma non le tue chiavi private. Hai bisogno delle chiavi private per spendere (firmando transazioni con le chiavi private). Il modo per farlo è collegare il portafoglio hardware. Il punto del portafoglio hardware è che le transazioni possono essere passate avanti e indietro tra il computer e il Trezor, una firma può essere applicata all'interno del Trezor e la chiave privata rimane sempre contenuta nel dispositivo (per la sicurezza contro i malware informatici).

Trezor Suite è un portafoglio di osservazione scadente per vari motivi. Va bene per il minimo indispensabile, ma se vuoi avanzare, continua a leggere e scopri come collegare il dispositivo a Sparrow Bitcoin Wallet.

## Portafoglio di osservazione

In articoli precedenti, ho spiegato come scaricare e verificare Sparrow Bitcoin Wallet e come collegarlo al tuo nodo o a un nodo pubblico. Puoi seguire queste guide:

- Installa Bitcoin Core
- Installa Sparrow Bitcoin Wallet
- Collega Sparrow Bitcoin Wallet a Bitcoin Core

Un'alternativa all'uso di Sparrow Bitcoin Wallet è Electrum Desktop Wallet, ma procederò a spiegare Sparrow Bitcoin Wallet perché lo considero il migliore per la maggior parte delle persone. Gli utenti avanzati potrebbero preferire utilizzare Electrum come alternativa (vedi la mia guida).

Caricheremo ora Sparrow e collegheremo il Trezor (con la frase di recupero ma ora con una frase di accesso). Questo portafoglio non è mai stato esposto a Trezor Suite perché verrà creato DOPO aver collegato il dispositivo a Trezor Suite. Assicurati di non collegarlo mai più a Trezor Suite per non esporre il tuo nuovo portafoglio. (Puoi collegarlo senza frase di accesso perché può essere il tuo portafoglio fittizio).

Crea un nuovo portafoglio:

![image](assets/19.webp)

Dagli un nome carino

![image](assets/20.webp)

Clicca su "Connected Hardware Wallet".

![image](assets/21.webp)

![image](assets/22.webp)

Clicca su "Scan" e poi su "set passphrase" nella schermata successiva per creare un nuovo portafoglio (usa una nuova frase di accesso, ad esempio la vecchia frase di accesso con un numero dopo funzionerebbe). Poi "send passphrase", poi confermala sul dispositivo.

![image](assets/23.webp)

Clicca poi su "importa keystore".

Non c'è nulla da modificare nella schermata successiva, il Trezor l'ha compilata per te. Clicca su "Applica".

![image](assets/24.webp)

Nella schermata successiva puoi aggiungere una password. Non confonderla con "passphrase"; molte persone lo fanno. La denominazione è sfortunata. La password ti permette di bloccare questo portafoglio sul tuo computer. È specifica per questo software su questo computer. Non fa parte della tua chiave privata Bitcoin.

Clicca su "Applica".

![image](assets/25.webp)

Dopo una pausa, mentre il computer elabora, vedrai che i pulsanti a sinistra cambieranno da grigi a blu. Congratulazioni, il tuo portafoglio è ora pronto all'uso. Effettua e invia transazioni a tuo piacimento.

![image](assets/26.webp)

Ricezione

Per ricevere dei bitcoin, vai alla scheda "Indirizzi" a sinistra e scegli uno degli indirizzi per ricevere. Fai clic destro sull'indirizzo desiderato e seleziona "copia indirizzo". Poi vai al tuo exchange da cui stanno inviando i soldi e incollalo lì. Oppure puoi fornire l'indirizzo a un cliente che può usarlo per pagarti.

Quando utilizzi il portafoglio per la prima volta, dovresti ricevere una quantità molto piccola, prova a spenderla verso un altro indirizzo, sia all'interno del portafoglio che verso l'exchange, per dimostrare che il portafoglio funziona come previsto.

Una volta fatto ciò, devi fare il backup delle parole che hai scritto. Una sola copia non è sufficiente. Hai bisogno di almeno due copie cartacee (meglio se in metallo) e conservarle in due luoghi diversi e ben protetti. Questo riduce il rischio che un disastro naturale distrugga il tuo HWW e il backup cartaceo in un solo incidente. Consulta "Utilizzo dei portafogli hardware Bitcoin" per una discussione completa su questo argomento.

## Invio

![image](assets/27.webp)

Quando effettui un pagamento, devi incollare l'indirizzo a cui stai pagando nel campo "Pagare a". In realtà non puoi lasciare vuota l'etichetta, è solo per i tuoi registri personali del portafoglio, ma Sparrow non lo permette: inserisci qualcosa (solo tu lo vedrai). Inserisci l'importo e puoi anche regolare manualmente la commissione desiderata.

Il portafoglio non può firmare la transazione se l'HWW non è connesso. Questo è il compito dell'HWW: ricevere la transazione, firmarla e restituirla, firmata. Assicurati che quando firmi sul dispositivo, ispezioni visivamente che l'indirizzo a cui stai pagando sia lo stesso sul dispositivo e sullo schermo del computer, e la fattura che ricevi (ad esempio, potresti aver ricevuto un'email per pagare un certo indirizzo).

Presta anche attenzione al fatto che se scegli di utilizzare una moneta che è più grande dell'importo del pagamento, il resto verrà inviato a uno degli indirizzi di cambio del tuo portafoglio. Alcune persone non lo sanno e cercano la loro transazione su una blockchain pubblica, pensando che alcuni bitcoin siano stati inviati all'indirizzo di un attaccante, ma in realtà era il loro stesso indirizzo di cambio.
Firmware

Per aggiornare il firmware, devi connetterti a Trezor Suite. Se vuoi farlo, assicurati di avere a disposizione le tue parole di backup e la passphrase per ripristinare il dispositivo, nel caso in cui il dispositivo si ripristini.
Conclusioni

Questo articolo ti ha mostrato come utilizzare un Trezor HWW in modo più sicuro e privato rispetto a quanto pubblicizzato, ma questo articolo da solo non è sufficiente. Come ho detto all'inizio, dovresti combinarlo con le informazioni fornite in "Utilizzo dei portafogli hardware Bitcoin".
Appendice A - Verifica del download del software

## Appendice A - Verifica del download del software

![image](assets/28 .webp)

Scarica la Firma (un file di testo) e la Chiave di Firma (un file di testo) e prendi nota dei nomi dei file e del percorso in cui hai scaricato i file.

Successivamente, per Mac, dovrai scaricare GPG Suite (Vedi le istruzioni qui).

Per Windows, avrai bisogno di GPG4win (Vedi le istruzioni qui).

Per Linux, GPG è già incluso in ogni pacchetto. Nel caso non lo avessi, ottienilo con il comando: sudo apt-get install gpg

Successivamente, per Mac/Windows o Linux, apri il terminale e inserisci il comando:

```bash
gpg –import XXXXXXXXXX
```

dove XXXXXXXXXX è il percorso completo del file della chiave di firma (percorso completo significa la directory e il nome del file in cui si trova). Dovresti vedere una conferma dell'importazione della chiave riuscita.

Quindi

```bash
gpg –verify ZZZZZZZZZZ WWWWWWWWWW
```

dove ZZZZZZZZZZ è il percorso completo del file di firma e WWWWWWWWWW è il percorso completo del programma Trezor Suite che hai scaricato.

Dovresti vedere un messaggio "Firma valida da SatoshiLabs" da qualche parte nell'output. C'è un avviso in fondo che è sicuro ignorare.

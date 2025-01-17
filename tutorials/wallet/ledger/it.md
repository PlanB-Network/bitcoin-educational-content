---
name: Ledger Nano S

description: Come configurare il tuo dispositivo Ledger Nano S
---

![image](assets/cover.webp)

Portafoglio fisico a freddo - €60 - Principiante - Per proteggere da €2.000 a €50.000

Ledger è la soluzione francese per proteggere i bitcoin in modo semplice.

In questo tutorial, parleremo anche della sezione delle passphrase, una soluzione avanzata per la sicurezza per conservare grandi somme: da 20.000€ a 100.000€.

https://www.youtube.com/watch?v=_vsHNTLi8MQ

# Collegare Ledger a Sparrow Bitcoin Wallet (guida scritta)

Assicurati di leggere prima l'altro articolo "Utilizzo dei portafogli hardware Bitcoin". Scorrerò velocemente alcuni passaggi e mi concentrerò principalmente su ciò che è specifico per Ledger.

## Configurazione del dispositivo

Ledger viene fornito con il suo cavo USB. Assicurati di utilizzare quello e non un vecchio cavo qualsiasi. Alcuni cavi USB sono solo per la ricarica. Questo trasmette dati E alimentazione. Quando ho utilizzato il dispositivo con un cavo USB per la ricarica del telefono che avevo in giro, il dispositivo non si è collegato.

Collegalo al tuo computer e il dispositivo si accenderà.

![image](assets/1.webp)

Scorri tra le opzioni. Vedrai

1. Configura come nuovo dispositivo
2. Ripristina dalla frase di recupero

In pratica, ti chiede se vuoi che il dispositivo crei un seed per te o se ne hai già uno che desideri utilizzare. È una pratica consigliata creare il proprio seed, ma farlo in modo sicuro è molto avanzato e al di fuori dello scopo di questo articolo. Scegli "Configura come nuovo dispositivo".

Ti verrà quindi chiesto di scegliere un PIN. Questo non fa parte del tuo seed Bitcoin ed è specifico solo di questo dispositivo. Blocca il dispositivo.

Ti verranno quindi presentate 24 parole che devi scorrere e annotare.

Stranamente, quando arrivi alla fine, dice "premi sinistra per verificare le tue parole". Questo non descrive come confermare per procedere, significa solo che puoi tornare indietro e rivedere le parole. Premi invece a destra e conferma premendo contemporaneamente sinistra e destra.

La parte successiva è molto fastidiosa. Mescola le 24 parole e devi confermare ognuna, da 1 a 24, scorrere tutte le parole per ogni selezione. Una volta finito, ti permette di confermare con una pressione di due pulsanti e continuare.

![image](assets/2.webp)

Vedrai sulla tua dashboard che hai un pulsante delle impostazioni e un pulsante più che ti consente di installare app. Ma devi connetterti a Ledger Live prima. Faremo questo dopo...

## Scarica Ledger Live

Potresti scaricare Ledger Live dal loro sito web, ma è meglio ottenerlo da GitHub, dove viene conservato il codice sorgente.

Cerca su Google "ledger live GitHub" o clicca su questo link https://github.com/LedgerHQ/ledger-live-desktop

![image](assets/3.webp)

Scorri verso il basso fino a quando non vedi l'intestazione "Download"...

![image](assets/4.webp)

In fondo, vedrai il link: Le istruzioni per verificare l'hash e le firme dei pacchetti di installazione sono disponibili in questa pagina. Clicca su quel link. (https://live.ledger.tools/lld-signatures)

![image](assets/5.webp)

In alto, ci sono scelte di link per il pacchetto software di cui hai bisogno, a seconda del tuo sistema operativo. Clicca su quello appropriato per scaricare.

Successivamente, vogliamo verificare l'hash del download, per una sicurezza extra.
Ledger pubblica l'hash di ciascuno dei file disponibili in questa pagina. Ora calcoleremo l'hash del download e confrontiamo l'output. Deve essere identico per assicurarsi che il file non sia stato manomesso.
Apri il terminale su un Mac o CMD su Windows. Segui questi comandi...

cd Downloads

<Enter>

```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- Per Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- Per Windows
```

<Enter>

Speriamo che sia ovvio che i comandi iniziano dopo le frecce. Assicurati, se questo articolo è obsoleto, di cambiare il nome del file nei comandi con esattamente il nome del file che hai scaricato. Devi premere il tasto <Enter> dopo ogni comando. I comandi come visti qui potrebbero non adattarsi su una sola riga nel tuo browser web. Nota che è tutto digitato su una sola riga.

Guarda l'output dell'hash e assicurati che sia identico a quello pubblicato su GitHub.

Idealmente, vorresti essere extra attento e assicurarti che gli hash pubblicati non siano falsi. Facciamo questo con le firme gpg, ma è al di fuori dello scopo di questo articolo. Se vuoi saperne di più su questo argomento (e ti suggerisco di farlo), leggi questo articolo.

## Connettersi a Ledger Live

Prima di eseguire Ledger Live, è utile attivare una VPN per la privacy. Ledger avrà comunque tutti i tuoi indirizzi, ma non conoscerà il tuo indirizzo IP, che svela il tuo indirizzo di casa. Mullvad VPN è un eccellente servizio VPN e non è molto costoso (non sto facendo pubblicità, è solo quello che uso).

Installa il software sul tuo computer ed eseguilo.

![image](assets/6.webp)

Seleziona il tuo dispositivo e seleziona "Prima volta che lo uso..."

![image](assets/7.webp)

Verrai quindi guidato attraverso una procedura guidata, ma abbiamo già eseguito tutti questi passaggi, quindi puoi passare velocemente.

![image](assets/8.webp)

Dopo molti passaggi e un quiz, verrà verificata l'autenticità del dispositivo. Devi assicurarti di essere connesso e di aver inserito il PIN, quindi verrà chiesto sul dispositivo se consenti a Ledger Live di connettersi. Devi confermare, ovviamente.

![image](assets/9.webp)

C'era una pubblicità di una shitcoin mascherata come "note di rilascio" nella successiva finestra pop-up. Ignorala, e poi dovresti arrivare a questa schermata.

![image](assets/10.webp)

Devi fare clic su "Aggiungi account" per ottenere un portafoglio Bitcoin.

![image](assets/11.webp)

Assicurati di scegliere Bitcoin e non Bitcoin Cash o altre shitcoin. Verrà verificato il dispositivo e dovrai confermare per procedere SUL DISPOSITIVO. Calcolerà gli indirizzi per un paio di minuti. Quindi fai clic su FINE.

![image](assets/12.webp)
![image](assets/13.webp)

Fantastico. Ora hai un gestore di portafogli shitcoin contenente un portafoglio Bitcoin sul tuo computer. In realtà non ne hai più bisogno e puoi eliminarlo. Lo scopo reale era ottenere l'app Bitcoin sul dispositivo stesso, ed è stato l'unico modo, a meno di eseguire alcune tecniche estreme di ingegneria del software.

Ricorda che in precedenza, sul dispositivo, avevamo un pulsante Impostazioni e un pulsante più. Ora abbiamo un pulsante extra: il pulsante App Bitcoin.

Puoi chiudere Ledger Live ora.

## Aggiungi una passphrase

Ora che abbiamo l'app Bitcoin, possiamo aggiungere una passphrase alla nostra frase di recupero. Non potevamo farlo prima quando la frase di recupero è stata creata perché all'inizio non avevamo l'app Bitcoin e dovevamo connetterci a Ledger Live per ottenerla.

Vai al menu "impostazioni" all'interno del dispositivo, quindi al sottomenu "sicurezza". Seleziona quindi la passphrase. Vedrai "Funzione avanzata". Fai clic sul pulsante destro, vedrai "leggi manuale..." e poi dopo un clic sul pulsante destro, vedrai "indietro". Ma non è la fine. Intuitivamente, penseresti che sia così, ma fai clic di nuovo sul pulsante destro. Vedrai "configura passphrase".

Puoi decidere di "associare al PIN" o "impostare temporaneamente". Consiglio di "associare al PIN". In questo modo, puoi accedere a portafogli diversi a seconda del PIN che inserisci quando accendi per la prima volta il dispositivo. Se "imposti temporaneamente", dovrai inserire la passphrase ogni volta che desideri accedere a quel portafoglio, ma sarà sempre dal PIN predefinito.

Inserisci la passphrase e confermala.

Ti chiederà il "PIN corrente". Questo non è il PIN che stai associando alla nuova passphrase. È il PIN che hai inserito quando hai acceso il dispositivo per questa sessione.

Ora puoi uscire dal menu principale selezionando l'opzione indietro alcune volte.

## Portafoglio di osservazione

Nei precedenti articoli, ho spiegato come scaricare e verificare il portafoglio Sparrow e come connetterlo al tuo nodo personale o a un nodo pubblico. Dovresti seguire queste guide:

- Installa Bitcoin Core (https://armantheparman.com/bitcoincore/)

- Installa Sparrow Bitcoin Wallet (https://armantheparman.com/download-sparrow/)

- Collega Sparrow Bitcoin Wallet a Bitcoin Core (https://armantheparman.com/sparrowcore/)

Un'alternativa all'uso di Sparrow Bitcoin Wallet è Electrum Desktop Wallet, ma procederò a spiegare Sparrow Bitcoin Wallet perché lo considero il migliore per la maggior parte delle persone. Gli utenti avanzati potrebbero preferire Electrum come alternativa.

Ora lo caricheremo e collegheremo Ledger, con il portafoglio contenente la passphrase. Questo portafoglio non è mai stato esposto a Ledger Live perché è stato creato DOPO aver collegato il dispositivo a Ledger Live. Assicurati di non collegarlo mai più a Ledger Live per non esporre il tuo nuovo portafoglio privato.

Crea un nuovo portafoglio:

![image](assets/14.webp)

Dagli un nome carino

![image](assets/15.webp)

Nota la casella di controllo "Ha transazioni esistenti". Se si tratta di un portafoglio che hai già utilizzato in precedenza, seleziona questa opzione, altrimenti il saldo verrà mostrato erroneamente come zero. Selezionando questa casella, Sparrow chiederà di esaminare il database di Bitcoin Core (la blockchain) per le transazioni precedenti. Per questa guida, stiamo utilizzando un portafoglio completamente nuovo, quindi puoi lasciare la casella deselezionata.

![image](assets/16.webp)

Fai clic su "Portafoglio hardware collegato" e assicurati che il dispositivo sia effettivamente collegato, acceso, con il PIN inserito e che tu abbia inserito l'app Bitcoin.

![image](assets/17.webp)

Fai clic su "Scansiona" e poi su "Importa Keystore" nella schermata successiva.

![image](assets/18.webp)

Non c'è nulla da modificare nella schermata successiva, Ledger l'ha compilata per te. Fai clic su "Applica"

![image](assets/19.webp)

La schermata successiva ti consente di aggiungere una password. Non confondere questa con "passphrase"; molte persone lo fanno. La denominazione è sfortunata. La password ti consente di bloccare questo portafoglio sul tuo computer. È specifica per questo software su questo computer. Non fa parte della tua chiave privata Bitcoin.

![image](assets/20.webp)

Dopo una pausa, mentre il computer pensa, vedrai i pulsanti a sinistra cambiare da grigi a blu. Congratulazioni, il tuo portafoglio è ora pronto per l'uso. Effettua e invia transazioni a tuo piacimento.

![image](assets/21.webp)

## Ricezione

Per ricevere dei bitcoin, vai alla scheda Indirizzi a sinistra e scegli uno degli indirizzi per ricevere. Fai clic destro sull'indirizzo desiderato e seleziona "copia indirizzo". Quindi vai al tuo exchange da cui viene inviato il denaro e incollalo lì. Oppure puoi fornire l'indirizzo a un cliente che può usarlo per pagarti.

Quando usi il portafoglio per la prima volta, dovresti ricevere una quantità molto piccola, prova a spenderla verso un altro indirizzo, sia all'interno del portafoglio che verso l'exchange, per dimostrare che il portafoglio funziona come previsto.

Una volta fatto ciò, devi fare il backup delle parole che hai scritto. Una singola copia non è sufficiente. Hai bisogno di almeno due copie cartacee (meglio se in metallo) e tienile in due posizioni diverse e ben protette. Questo riduce il rischio che un disastro naturale distrugga il tuo HWW e il backup cartaceo in un solo incidente. Consulta "Utilizzo dei portafogli hardware Bitcoin" per una discussione completa su questo argomento.

## Invio

![image](assets/22.webp)

Quando effettui un pagamento, devi incollare l'indirizzo a cui stai pagando nel campo "Pagare a". In realtà non puoi lasciare vuota l'etichetta, è solo per i tuoi record personali del portafoglio, ma Sparrow non lo permette: inserisci qualcosa (solo tu lo vedrai). Inserisci l'importo e puoi anche regolare manualmente la commissione desiderata.

Il portafoglio non può firmare la transazione se l'HWW non è collegato. Questo è il compito dell'HWW: ricevere la transazione, firmarla e restituirla firmata. Assicurati che quando firmi sul dispositivo, ispezioni visivamente che l'indirizzo a cui stai pagando sia lo stesso sul dispositivo e sullo schermo del computer, e la fattura che ricevi (ad esempio, potresti aver ricevuto un'email per pagare un certo indirizzo).

Presta anche attenzione al fatto che se scegli di utilizzare una moneta che è più grande dell'importo del pagamento, il resto verrà inviato a uno degli indirizzi di cambio del tuo portafoglio. Alcune persone non lo sanno e cercano la loro transazione su una blockchain pubblica, pensando che alcuni bitcoin siano stati inviati a un indirizzo di un attaccante, ma in realtà era il loro stesso indirizzo di cambio.

## Firmware

Per aggiornare il firmware, devi connetterti a Ledger Live. Se vuoi farlo, dovresti cancellare i dati del dispositivo prima e assicurarti di avere a disposizione le tue parole di backup e la passphrase per ripristinare il dispositivo. La ragione per cui preferisco cancellare i dati del dispositivo prima è che devi collegare il tuo dispositivo a Ledger Live per aggiornare il firmware, e preferisco non esporre mai il tuo nuovo portafoglio (quello con la passphrase) a Ledger Live. Semplicemente non mi fido che Ledger non estragga le informazioni sulla mia chiave pubblica dal dispositivo quando mi collego a Ledger Live. Dicono di no, ma non posso verificarlo personalmente a meno che non legga il codice e comprenda anche l'hardware interno.

## Conclusioni

Questo articolo ti ha mostrato come utilizzare un Ledger HWW in modo più sicuro e privato rispetto a quanto pubblicizzato, ma questo articolo da solo non è sufficiente. Come ho detto all'inizio, dovresti combinarlo con le informazioni fornite in "Utilizzo dei portafogli hardware Bitcoin".
Suggerimenti:

Indirizzo Lightning statico: dandysack84@walletofsatoshi.com
https://armantheparman.com/ledgersparrow/


Per approfondire questo argomento e rafforzare la sicurezza del tuo portafoglio su un Ledger Nano con una passphrase BIP39, ti invito a consultare questo tutorial completo:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49


---
name: BitcoinVoucherBot P2P
description: Come Acquistare e vendere Bitcoin P2P con BitcoinVoucherBot
---

![image](assets/cover.webp)

Sentiamo ancora parlare di BitcoinVoucherBot, un bot Telegram nato per acquistare Bitcoin senza [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) tramite bonifico bancario SEPA. Purtroppo a partire da Novembre 2025 il BitcoinVoucherBot nella sua forma centralizzata non è più disponibile come servizio senza KYC.

In questa guida vedremo come funziona la nuova implementazione che permette di acquistare e vendere Bitcoin direttamente sul nuovo marketplace P2P (Peer-To-Peer), quindi no KYC. Per contrastare le nuove restrizioni che sempre più spesso minacciano la libertà digitale e la privacy, gli sviluppatori hanno creato questa estensione, dando agli utenti la possibilità di comprare e vendere Bitcoin con un elevato grado di anonimato tramite il P2P (Peer-To-Peer). Vediamo insieme come funziona questo nuovo metodo di scambio.

Per utilizzare il servizio dovrai effettuare i trasferimenti tramite Lightning Network. Assicurati quindi di avere un wallet che supporti questo protocollo e che ti consenta di usare un “LNURL” o un “Lightning Address” per ricevere e inviare i  fondi. 

Tra i wallet supportati possiamo trovare:

- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodial)
- [Wallet Of Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Custodial con swap a Non-Custodial)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)

Oppure qualsiasi wallet che abbia un “Lightning Address” e che generi una fattura Bolt11. Al momento non sono supportati i wallet che generano una fattura Bolt12. Per maggiori info vedi la definizione di [Bolt](https://planb.academy/resources/glossary/bolt).

Per questo tutorial, dato la sua semplicità d’uso immediato, utilizzeremo Wallet of Satoshi.

**Attenzione**: Wallet of Satoshi, pur diffuso tra i principianti, è custodial, con controllo limitato sui fondi; usalo solo transitoriamente, trasferendoli subito a un non-custodial per piena sovranità. Da ottobre 2025, include una modalità self-custodial stabile worldwide su iOS/Android (aggiorna l'app), con chiavi private autonome, switch tra modalità, indirizzi Lightning personalizzati e backup seed 12 parole. Tuttavia, resta una soluzione provvisoria fino a consolidamento, preferendo wallet non-custodial maturi per la gestione a lungo termine.

Molto bene! Ora possiamo iniziare il nostro percorso, che ti guiderà passo passo nella creazione dell’account, nella gestione dei match di acquisto e vendita e nell’utilizzo della tua area riservata.

## Wallet e Iscrizione

Per prima cosa, se non lo hai già installato sul tuo smartphone, scarica Wallet of Satoshi.

- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)

![image](assets/it/01.webp)

Se non hai mai utilizzato Wallet of Satoshi e vuoi comprenderne il funzionamento, ti consiglio di seguire questo tutorial, così potrai attivarlo correttamente ed eseguire il backup in modo sicuro.

https://planb.network/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Ora che il tuo wallet è pronto, puoi iniziare a inviare una piccola quantità di sats. Tieni presente che, per completare l’iscrizione alla piattaforma P2P (Peer-To-Peer), ti verranno richiesti 1000 sats come misura di controllo: questo serve a creare una barriera contro eventuali attacchi del tipo match fantasma (scam), impedendo che chiunque possa iscriversi senza alcun filtro anti spam.

![image](assets/it/02.webp)

Ora possiamo aprire la piattaforma P2P (Peer-To-Peer) per procedere all’iscrizione. Puoi accedere da PC desktop o browser su smartphone, tramite il bot Telegram BitcoinVoucherBot oppure tramite link .onion, per garantire un livello di privacy ancora maggiore.

se scegli di utilizzare il link Tor .onion ti consilgio anche "Tor Browser". Se ancora non lo conosci puoi approfondire a questo link: 

https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Ora scegli come vuoi raggiungere la piattaforma.

- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Browser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)

Verrai reindirizzato alla pagina principale.

premi su “Get Starter” per iniziare subito

![image](assets/it/03.webp)

Nella schermata successiva devi scegliere una password e inserirla (riquadro A), per poi ripeterla (riquadro B). Ti raccomando di salvare subito questa password su un supporto di backup, che può essere su un dispositivo digitale sicuro come per esempio "Bitwarden":

https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

oppure salva la tua password su un supporto cartaceo (**attenzione**: non è una buona soluzione, va bene però se intesa come soluzione temporanea).

Spunta la casella di verifica dove dichiari di non essere un robot (riquadro C). Nota bene! Non abilitare la crittografia RSA a meno che tu non sappia esattamente cos’è e come funziona. In questa fase non è necessario fare nulla. Clicca su “Generate Avatar” ( Genera Avatar”) (riquadro D).

![image](assets/it/04.webp)

Ora devi pagare i 1000 sats per completre l'iscrizione. 

1. Partendo dall’alto, vedi innanzitutto il tuo “Avatar ID”, generato casualmente e estremamente importante. Salvalo con cura, proprio come ti ho consigliato di fare con la password.
2. Devi quindi inserire il tuo “Lightning Address” nel campo sottostante. Questo ti permetterà di ricevere i pagamenti se acquisti Bitcoin, oppure di ottenere i rimborsi. Se stai usando Wallet Of Satoshi potrai copiare il tuo Address cliccando su ricevi.
3. Spunta la casella di verifica dove dichiari di non essere un robot.
4. Effettua il pagamento di 1000 sats per ottenere l’accesso alla tua area riservata. Se non puoi inquadrarlo, cliccaci sopra con il mouse (su PC) o toccalo con il dito (su smartphone Browser/Telegram) per copiare l’indirizzo che devi incollare su Wallet of Satoshi e completare il pagamento della fattura.

![image](assets/it/05.webp)

Questo e' il tuo LNURL Address.

![image](assets/it/06.webp)

Complimenti! Hai creato il tuo Avatar in modo definitivo e qui puoi visualizzare il riepilogo. Ancora una volta ti raccomando di salvare con cura sia il tuo Avatar che la password, come ti ho già suggerito in precedenza.

Clicca su `I’ve saved my credentials, continue` (tradotto con: "ho salvato le mie credenziali, continua")

![image](assets/it/07.webp)

Ti trovi ora nel cuore della piattaforma, dove puoi visualizzare tutti i match di compravendita con i relativi dettagli. Per una visualizzazione piu chiara, qui sotto vedrai le immagini inerenti al sito web da computer desktop.

- "Type" ("Tipo") definisce se si tratta di una vendita "Sell"("vendi") oppure un acquisto "buy"("compra")
- “Amount” (“Ammontare”): indica quanti sats l’utente sta vendendo se il match è di tipo “Sell” (Vendi), oppure quanti Bitcoin è disposto ad acquistare se il match è di tipo “Buy” (Compra).
- “BTC Price with Margin” (“Prezzo BTC con margine”): mostra il prezzo tenendo conto del margine applicato sopra il valore di marcato.
- "Margin" ("Margine") e' la percentuale che viene applicata al prezzo di mercato, con un segno meno (-) ottieni uno sconto sul prezzo di mercato, Con un segno più (+) viene applicato un premio sul prezzo di mercato.
- "Method" ("Metodo") indica con quale motodo l'utente preferisce essere pagato.
- "Creator" si tratta dell'avatar univoco utilizzato dall'utente sulla piattaforma.
- "Rep" (Reputazione) Il livello di reputazione dell'utente va da -5 inaffidabile a +5 estremamente affidabile.
- “Status” (“Stato”): indica lo stato del match. Nella schermata di esempio tutti i match risultano “Open” (“Aperti”).
- “Expiration” (“Scadenza”): mostra quanto tempo resta prima che il match scada e venga cancellato se non è stato scelto da nessuno.

![image](assets/it/08.webp)

Nella parte superiore a destra clicca sul tuo Avatar per accedere al profilo.

![image](assets/it/09.webp)

Qui puoi vedere il tuo nome Avatar, il tuo User ID, la data di creazione e la tua reputazione, che rifletterà positivamente o negativamente il tuo comportamento nelle trattative.

![image](assets/it/10.webp)

Nella sezione Settings puoi visualizzare il tuo “Lightning Address”, inserito durante la registrazione, e modificarlo se necessario. Hai anche la possibilità di creare una Public Key, che come accennato va impostata solo se possiedi le competenze adeguate. Essa serve per crittografare i messaggi che scambierai con la controparte direttamente dal computer.

La funzione Telegram Notification è vivamente consigliata. Attivandola, ti comparirà un QR code da inquadrare con l’app di Telegram: in questo modo riceverai notifiche in tempo reale su tutte le azioni relative ai tuoi match, direttamente nella chat del bot su Telegram.

![image](assets/it/11.webp)

Infine, trovi la tua sezione referral, con i guadagni generati dagli utenti che hai invitato. Da qui puoi usare il bottone per condividere il tuo link o QR code e, poco più in basso, visualizzare una lista dei match per monitorare la tua reputazione insieme al relativo punteggio.

![image](assets/it/12.webp)

## Crea un ordine per Acquistare Bitcoin

Entra nel Marketplace: dalla barra di navigazione principale, clicca sul simbolo del carrello “Marketplace”(“Mercato”) per aprire il book ordini. poi avvia un nuovo ordine: premi sul pulsante “New Order” (“Nuovo ordine”) per iniziare la procedura.

![image](assets/it/13.webp)

- Imposta i dettagli dell’ordine:
- Seleziona l’opzione “Buy Bitcoin”(“Acquista Bitcoin”).
- Inserisci la quantità di sats che desideri.
- Definisci il margine di prezzo (tra -20% e +20% rispetto al valore di mercato).
- Scegli il metodo di pagamento (Instant SEPA, ecc.).
- Indica la valuta preferita.
- Conferma l’ordine: clicca su “Create Order”(“Conferma ordine”) per passare alla fase di deposito.

![image](assets/it/14.webp)

Deposito richiesto: per attivare l’ordine è necessario versare un deposito pari al 10% dell’importo totale, più una commissione di servizio.
- Pagamento del deposito: al momento della creazione dell’ordine, il sistema genera automaticamente una fattura Lightning. Il deposito è solo temporaneo e viene rimborsato al completamento dell’ordine.
- Caratteristiche principali:
- Deposito cauzionale: 10% del valore dell’ordine.
- Commissione di servizio: costo per l’utilizzo della piattaforma.
- Tempo limite: hai 5 minuti per effettuare il pagamento, altrimenti l’operazione scade.

![image](assets/it/15.webp)
        
Dopo il pagamento andato a buon fine, l’ordine comparirà nel book e sarà visibile a tutti gli utenti, che potranno sceglierlo e accettarlo. Per creare un ordine di vendita ti basta cliccare su “Sell Bitcoin” (“Vendi Bitcoin”), inserire la quantità di satoshi che desideri vendere, impostare il margine, selezionare il metodo di pagamento e la valuta, quindi procedere con il versamento del 10% come deposito cauzionale. Una volta completata l’operazione, il tuo match sarà visibile nell’elenco.

![image](assets/it/16.webp)

## Come accettare un ordine

1. I venditori possono consultare l’elenco di tutti gli ordini disponibili nel book.
2. Controlla i dettagli: ogni ordine mostra informazioni come:
  - Quantità di Bitcoin,
  - Margine sul prezzo,
  - Metodo di pagamento,
  - Reputazione dell’utente.

![image](assets/it/17.webp)

3. Clicca sull’ordine per aprire la scheda completa con tutte le informazioni.
4. Premi su “Sell Bitcoin”(“Vendi Bitcoin”) per accettare la proposta.

![image](assets/it/18.webp)

## Deposito richiesto dal venditore

Quando l’ordine viene accettato, il sistema genera una fattura da pagare. Il deposito comprende:
    • l’importo totale dell’ordine,
    • la commissione di servizio.

Il pagamento del deposito deve essere effettuato entro il tempo limite stabilito, altrimenti la transazione non verrà confermata.

![image](assets/it/19.webp)

## Invio delle istruzioni di pagamento

Dopo aver versato il deposito, l’operazione apparirà nella dashboard personale del venditore, che dovrà fornire i dettagli all’acquirente per completare il pagamento in valuta fiat.

1. Il venditore visualizza la transazione attiva nel proprio pannello.
2. Clicca su “Invia istruzioni di pagamento”.
3. Inserisci tutte le informazioni necessarie per il pagamento fiat (IBAN, destinatario, indirizzo, causale, ecc.).
4. Clicca su “Send Message”(“Invia messaggio”) per trasmettere i dati all’acquirente.

![image](assets/it/20.webp)

## Procedura di pagamento

L’acquirente riceve, all’interno della chat della piattaforma, un messaggio con tutti i dati necessari per eseguire il pagamento in valuta fiat:
- Coordinate bancarie: IBAN con nome e indirizzo del titolare del conto del venditore.
- Somma esatta: importo fiat preciso da trasferire.
- Causale/descrizione: testo da inserire nella transazione.
- Tempo limite: scadenza entro la quale completare il pagamento.
  
Il trasferimento avviene al di fuori del sistema P2P e deve essere effettuato attraverso il proprio istituto bancario.

⚠️ **Nota importante:** la conferma su piattaforma deve avvenire solo dopo aver realmente disposto il bonifico o il pagamento fiat tramite la propria banca.

![image](assets/it/21.webp)

## Conferma del pagamento fiat

Questo passaggio è cruciale per l’acquirente e va eseguito soltanto dopo aver verificato che il pagamento sia stato effettivamente inviato.

1. Ricezione dati: l’acquirente ha ricevuto le istruzioni di pagamento dal venditore.
2. Esecuzione del pagamento: il trasferimento fiat viene disposto dal proprio conto bancario.
3. Verifica: controllare che l’operazione sia stata elaborata correttamente.
4. Conferma su piattaforma: cliccare su “Confirm fiat payment”(“Conferma pagamento fiat”) nella pagina del trade.
Il pulsante “Conferma pagamento fiat” compare nella sezione della transazione e deve essere usato esclusivamente dopo aver verificato che il pagamento è stato davvero inviato.

![image](assets/it/22.webp)

L’ultima fase del processo consiste nella conferma, da parte del venditore, dell’avvenuta ricezione del pagamento fiat, a seguito della quale i sats vengono rilasciati all’acquirente.

![image](assets/it/23.webp)

## Conclusione

Nella speranza che questo tutorial ti possa essere d'aiuto per utilizzare un nuovo metodo per scambiare Bitcoin o anche solo acquistarli, sia per la tua riserva di valore sia per iniziare a dare vita ai pagamenti quotidiani. Resta comunque una porta da esplorare per far fronte a quello che sta per succedere nel nostro mondo digitale. 

Il cappio gestito dagli organi che ci controllano si sta stringendo, per dar vita a un internet sempre più controllato. Comprando P2P, manterrai nel più totale anonimato i tuoi acquisti, senza lasciare tracce e senza dar seguito a ripercussioni da terzi.

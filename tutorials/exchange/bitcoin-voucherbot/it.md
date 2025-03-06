---
name: Bitcoin VoucherBot

description: Un bot Telegram per acquistare Bitcoin in confidenzialità
---

![image](assets/cover.webp)

# Introduzione
BitcoinVoucherBot è uno strumento con il quale si possono acquistare Bitcoin in cambio di euro.
### KYC Light

Cambiare euro per Bitcoin: il primo e fondamentale passo per iniziare a studiare questa materia, ma apparentemente anche il più difficile.
Le opzioni possono essere molteplici, se si pensa all'offerta di exchange centralizzati, i meetup a tema Bitcoin, amici e conoscenti e tanto altro ancora. Ci uniamo alla community di Bitcoiner, **sconsigliando assolutamente l’uso degli exchange centralizzati**, per una maggiore attenzione alla privacy.

Sebbene questa scelta possa risultare meno comoda, è importante capire che gli exchange applicano la normativa KYC (Know Your Cutomer), assegnando quindi un’identità, nonché una posizione fisica, ad ogni satoshi acquistato presso di loro. La "comodità" ha i suoi effetti collaterali.

### Come fare?

Ecco che ci viene incontro [BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot), un bot di Telegram che fa da tramite tra i nostri bonifici SEPA e l'acquisto di sats.

### Pre-requisiti
Per iniziare ad utilizzare BitcoinVoucherBot non c'è bisogno di rilasciare delicate informazioni personali allo staff del Bot. **Non serve autorizzazione**.

Tutto ciò che occorre è un account Telegram già attivo e un conto corrente bancario, che non sia di poste italiane o di una carta ricaricabile.
Nella chat di Telegram prepariamo un ordine, con un bonifico bancario lo paghiamo e, infine, tramite il bot otteniamo un voucher emesso da una società terza che non conosce l'oggetto  dell’acquisto.

### Attivazione del bot e menu
L’attivazione è una semplice operazione che viene eseguita una volta sola.
Da Telegram cercare *@BitcoinVoucherBot* e, appena giunti nella chat del Bot, campeggia in basso un pulsantone grande *Avvia/Start*. L’operazione fa rispondere il Bot che presenta il menu dei principali comandi a disposizione. Appaiono anche i primi messaggi di benvenuto, per i quali consigliamo un'attenta lettura.

![image](assets/01.webp)

Le opzioni appaiono cliccando il tasto *Menu* in basso a sinistra: si può cliccare sulla parola corrispondente al comando, oppure scrivere nella casella del messaggio lo slash "/" seguito dal comando digitato.

![image](assets/02.webp)

Tra le principali operazioni ci sono:
- */purchase* - è la procedura di acquisto vera e propria. Al termine dell’operazione il QR Code viene generato automaticamente dal bot, pronto al riscatto.
- */refill* - disponibile nel momento in cui scriviamo questo tutorial, ma non lo tratteremo perché - per motivi tecnici - questa opzione potrebbe essere elimata in seguito.
- */swap* - apre la procedura di swap, disponibile sia con un comodo bot di Telegram che via web.
- */ap* - accumulation plan, che consente di impostare un **Piano di Accumulo Costante (PAC)**.
- */lnaddress* - con cui ci viene chiesto di collegare un proprio LN Address, per una particolare procedura che vedremo in seguito.
- */credits* - per controllare quanto credito è rimasto per generare voucher.
- */myorders* - mostra gli ordini fatti con il bot. N.B. il sistema tiene traccia soltanto degli ultimi 10 ordini effettuati e non l'intero storico.
- */fees* - un comando per controllare le fee di rete. Per valutarle, è sempre meglio affidarsi a mempool.space.
- */support* - in caso di necessità, fa comparire i contatti per segnalare al team di supporto le problematiche.

# Procedura di acquisto Bitcoin
Preparazione dell'ordine, pagamento e riscatto
# Preparazione dell'ordine
Cliccare */purchase* nel menu dei comandi

![image](assets/03.webp)

Compaiono una serie di opportunità, ma noi scegliamo *BTC Vouchers*

![image](assets/04.webp)

Bitcoin VoucherBot consente di acquistare Bitcoin onchain, Lightning e Liquid.
In questa fase si scelga *Onchain & Lightning 🔗⚡️*

![image](assets/05.webp)

La schermata cambia rapidamente e VoucherBot propone i "tagli" di acquisto. Si parte da un minimo di 100,00 € fino ad arrivare a 900,00 €
In caso di primo acquisto, vengono proposti solo i tagli da 100,00 €, Onchain e Lightning. Per aumentare la confidenzialità, suggeriamo di scegliere *Lightning ⚡️*

![image](assets/06.webp)

VoucherBotc ci avvisa che una prima scelta è stata fatta e che, per confermarla, è necessario scegliere *Proceed*

![image](assets/07.webp)

Si tratta ora di scegliere il metodo di pagamento.
Il trasferimento avviene tramite bonifico **(accettato solo SEPA)**. VoucherBot propone come ricevente una società svizzera, che mette a disposzione due conti correnti, uno in U.K e l'altro in Svizzera. Per realizzare questo tutorial è stata scelta la banca svizzera

![image](assets/08.webp)

A questo punto ci viene chiesto di immettere il nostro IBAN, quello da cui partirà il bonifico verso la banca scelta. Questa informazione va a comporre un puzzle che permetterà al bot, cioè ad una macchina, di mettere insieme alcune informazioni per far scorrere il processo d'acquisto senza il bisogno dell'intervento umano.
L'IBAN deve essere scritto nella barra del messaggio, controllato e inviato al bot.

![image](assets/09.webp)

Nella chat con VoucherBot compare ora un messaggio di controllo.
Se tutto è corretto, proseguire cliccando *Proceed*.

# Pagamento

![image](assets/10.webp)

Dopo qualche istante, necessario per processare i dati, VoucherBot replica con un messaggio che contiene tutti i dettagli necessari a completare l'ordine.
A seconda di quanto richiesto dalla propria banca, le informazioni rilevanti sono:
- IBAN, indispensabile per il versamento, oltre all'indirizzo del ricevente;
- l'importo scelto in precedenza tramite il "taglio", che deve essere rispettato per permettere a VoucherBot di riconoscere l'ordine quando sarà arrivato il pagamento;
- **Payment reason**, ovvero la causale del pagamento;
- un OrderID univoco, cui fare riferimento per richiedere eventuale assistemza.

  Si può quindi procedere con il pagamento, tramite la propria app o banca.
  Quando il pagamento è stato accettato dalla banca, è importante ricordarsi di premere *Notify payment* nella chat con VoucherBot. Questa semplice operazione avvisa che un pagamento sta per arrivare.

![image](assets/11.webp)

VoucherBot risponde con un messaggio che contiene un avviso molto importante: **non cancellare la chat**, almeno fino alla ricezione del voucher, perché è l'unico strumento per ricostruire l'ordine e farlo proseguire.

![image](assets/12.webp)
---
Nota bene:
- sono accettati solo bonifici SEPA;
- i tempi di attesa sono legati esclusivamente alle modalità di processamento delle banche (che non lavorano 24/7/365 come Bitcoin). Potrebbero volerci da poche ore fino a 3 giorni lavorativi per ricevere il voucher;
- per qualsiasi necessità, Bitcoin VoucherBot ha un eccellente servizio di [assistenza](https://t.me/BitcoinVoucherGroup) su Telegram.

---

# Riscatto
Non appena il pagamento è giunto a buon fine, Bitcoin VoucherBot manda il voucher direttamente nella chat.
Il voucher lightning è sottoforma di QR code, stampato su sfondo arancione.

![image](assets/31.webp)

Ci sono tutti i dati necessari per incassarlo:
- l'importo in sats, equivalenti a quello inviato tramite bonifico, escluse
  - fee di servizio
  - fee di rete
- un reference ID del voucher
- la data entro la quale il voucher deve essere riscattato, pena la perdita di fondi, cioè 25 giorni dopo l'emissione.

Si può incassare il voucher inquadrando il QR code con la funzione scan di un wallet Lightning Network compatibile, o tramite l'LN URL, anch'esso indicato sotto il QR code.

Per questo tutorial abbiamo usato Wallet Of Satoshi, usando la funzione di scan attivata dal tasto *Send*

![image](assets/32.webp)

Con la fotocamera del cellulare attivata, inquadrare il QR code nella chat, aprendo Telegram da PC

![image](assets/34.webp)

Prima di procedere, Wallet Of Satoshi da una schermata di verifica che comprende l'importo, il quale corrisponde esattamente a quello espresso sul voucher e, come descrizione, BitcoinVoucherBot.
Per incassare il voucher è sufficiente cliccare si *Receive*

![image](assets/35.webp)

Wallet Of Satoshi processa per pochi istanti

![image](assets/36.webp)

e infine l'incasso è segnalato e subito disponibile nel saldo del wallet.

**Walleto of Satoshi è un'app custodial: subito dopo l'incasso del voucher è consigliabile spostare i sats su un wallet non-custodial.**

![image](assets/37.webp)

# Come incassare un voucher onchain

Come abbiamo visto nella preparazione dell'ordine, VoucherBot permette di acquistare sats direttamente onchain, con la scelta dell'omonimo voucher.

### Preparazione dell'ordine e pagamento, sono sempre gli stessi. Ciò che cambia è come si incassa un voucher onchain.

Dopo aver completato l'ordine, effettuato il pagamento, premuto *Notify payment* e atteso i tempi tecnici delle banche per trasferire il nostro bonifico, VoucherBot risponderà inviando il voucher direttamente nella chat.

Anche questo voucher è sottoforma di QR code, ma il colore principale è il giallo canarino e - soprattutto - in descrizione è ben spiegato che si tratta di un voucher onchain, il quale si incassa direttamente sul proprio wallet onchain e, per iniziare la procedura di incasso, si deve cliccare su *Redeem on Telegram*.
Anche il voucher onchain contiene le informazioni già viste per quello lightning:
- l'importo in sats, equivalenti a quello inviato tramite bonifico, escluse
  - fee di servizio
  - fee di rete;
- un voucher code;
- un reference ID del voucher;
- la data entro la quale il voucher deve essere riscattato, pena la perdita di fondi, cioè 25 giorni dopo l'emissione.

![image](assets/22.webp)

**N.B. fate attenzione** che, cliccato come spiegato, si apre il pop-up di un altro bot: **Voucher RedeemBot.**

Voucher RedeemBot è lo strumento messo a disposizione per questo scopo. Sia che si tratti del primo utilizzo, sia che ci siano degli ordini pregressi, ad ogni nuovo riscatto è sempre necessario cliccare su *START*.

![image](assets/23.webp)

A questo punto RedeemBot carica il voucher onchain, facilmente riconoscibile da Voucher Code e reference ID.
Si sblocca anche la barra per scrivere i messaggi e iniziare a chattare con il bot, che infatti ci invita a comunicargli un indirizzo onchain del nostro wallet.
**Questo indirizzo deve essere Segwit**.

![image](assets/24.webp)

Apriamo a questo punto il nostro wallet e generiamo un indirizzo segwit

![image](assets/25.webp)

lo copiamo

![image](assets/26.webp)

e lo incolliamo nella chat con RedeemBot

![image](assets/27.webp)

Abbiamo adesso a disposizione una schermata di controllo, per verificare il voucher code che sia corretto, così come l'indirizzo che abbiamo comunicato a RedeemBot.
Controlliamo bene perché, cliccando su *Proceed*, la transazione parte e non ci sarà più modo di ritrovarla se abbiamo, ad esempio, comunicato l'indirizzo sbagliato.

![image](assets/28.webp)

La transazione è partita e la procedura di redeem del voucher onchain termina così.

![image](assets/29.webp)

mentre l'importo è visibile in arrivo nella history del nostro wallet.

![image](assets/30.webp)

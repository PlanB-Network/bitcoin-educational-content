---
name: Boltz
description: Passare da uno strato all'altro di Bitcoin mantenendo il controllo.
---


![cover](assets/cover.webp)



Dalla sua introduzione nel 2009, il sistema di contante elettronico peer-to-peer Bitcoin è cresciuto in modo esponenziale, dando vita a soluzioni che oggi lo rendono un sistema che possiamo utilizzare istantaneamente nelle nostre azioni quotidiane, in particolare attraverso il Lightning Network.



Tuttavia, rimaneva un problema importante tra i livelli del protocollo Bitcoin: l'interoperabilità fluida. Per sfruttare appieno il potenziale del Bitcoin, era indispensabile trovare una soluzione che consentisse di effettuare transazioni tra i diversi livelli del protocollo. Questa esigenza ha fatto nascere nel 2019 Boltz, un ponte che collega diversi livelli del Bitcoin.



## Che cos'è Boltz?



[Boltz](https://boltz.Exchange) è una piattaforma non custodiale, ideale per chiunque desideri effettuare transazioni tra i diversi livelli del protocollo Bitcoin:




- on chain**: La catena principale di Bitcoin dove le transazioni sono confermate in media ogni 10 minuti, le commissioni di transazione sono spesso elevate, il che non soddisfa necessariamente le esigenze degli utenti;
- Lightning Network**: Il sovrapposto Bitcoin per pagamenti istantanei a commissioni ridotte, che consente di utilizzare il Bitcoin per i pagamenti giornalieri;
- Liquid Network**: un overlay per il Bitcoin creato da Blockstream, che consente di utilizzare strumenti finanziari veloci, Confidential Transactions e altri strumenti finanziari basati su Bitcoin;
- RootStock**: Una soluzione per lo sviluppo di contratti intelligenti basati sul protocollo Bitcoin.



![layers](assets/fr/01.webp)



L'interoperabilità tra questi diversi livelli è di grande importanza, in quanto offre agli utenti la flessibilità necessaria per sfruttare appieno tutto ciò che l'ecosistema Bitcoin ha da offrire.



Boltz utilizza gli scambi atomici. Questa tecnologia consente di scambiare bitcoin tra 2 livelli (ad esempio BTC onchain in Exchange per BTC su Lightning) direttamente tra due parti, senza bisogno di fiducia e senza la necessità di un intermediario. Questi scambi sono chiamati "atomici" perché possono produrre solo due risultati:




- O il Exchange ha successo e i due partecipanti hanno effettivamente scambiato i loro BTC ;
- O il Exchange fallisce, ed entrambi i partecipanti se ne vanno con i loro BTC originali.



In questo modo, si mantiene un'autocustodia permanente dei propri bitcoin e il Exchange non si basa su alcuna fiducia nella controparte: il Exchange può avere successo o fallire, ma nessuna delle due parti può rubare i fondi dell'altra.



Un Exchange atomico funziona con gli smart contract [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). In questo tipo di Contract, l'importo viene "bloccato" in un canale bidirezionale e viene introdotta una restrizione temporale, in modo che se la transazione non viene completata entro un certo tempo, il saldo torna al depositante. Questo è il meccanismo utilizzato dalla piattaforma Boltz.



## I primi scambi con Boltz



Boltz è una piattaforma web non depositaria che non richiede informazioni personali all'utente. Boltz ha una Interface minimalista e fluida che consente di iniziare a fare trading in meno di un minuto.



![boltz](assets/fr/02.webp)



Una volta sulla piattaforma, è possibile creare scambi atomici tra i vari livelli dell'ecosistema Bitcoin.



![home](assets/fr/03.webp)



Vedrete il numero minimo e massimo di satoshis (l'unità più piccola del Bitcoin) che potete scambiare tramite Boltz, comprese le spese di rete e una percentuale applicata da Boltz tra lo 0,1% e lo 0,5%.



![fees](assets/fr/04.webp)



Quindi selezionare il Layer dal quale si desidera creare un Exchange atomico e selezionare il Layer sul quale si desidera ricevere i bitcoin.



![couches](assets/fr/05.webp)



In questa esercitazione ci concentreremo sul Exchange atomico dal Layer principale al Lightning Network.



È possibile configurare l'unità base per le proprie centrali scegliendo tra le opzioni :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Una volta completate le configurazioni di base, inserite l'importo del vostro Exchange atomico, quindi create un Lightning Invoice per l'importo equivalente, oppure inserite semplicemente il vostro LNURL.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Per sicurezza, verificare i parametri del proprio Exchange atomico per esportare le chiavi di backup collegate al Exchange.



Sull'icona **Impostazioni**, scaricare la chiave di backup e salvare il file in modo appropriato.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Questo file contiene le 12 parole chiave del portafoglio associato agli scambi atomici.



Cliccare quindi sul pulsante **Crea Exchange atomico** e procedere al pagamento dell'importo indicato.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Una volta che il pagamento è stato effettuato e confermato, riceverete automaticamente l'importo equivalente sul vostro Lightning Wallet.



Nel menu **Rimborso**, trovare la cronologia del Exchange atomico per identificare il Exchange su cui si desidera essere rimborsati. È anche possibile importare la cronologia degli scambi effettuati su un altro dispositivo, ad esempio utilizzando il file della chiave di backup associata a tali scambi.



![refund](assets/fr/11.webp)



Nel menu **Storia** è possibile scaricare una cronologia più dettagliata degli scambi associati alla chiave di soccorso facendo clic sul pulsante **Backup**.



![backup](assets/fr/12.webp)



⚠️ Si prega di non divulgare nemmeno questo file, poiché contiene tutte le informazioni associate alle transazioni e la chiave di backup collegata a tali transazioni.



Boltz offre un alto livello di riservatezza grazie al suo accesso tramite un link `.onion` sulla rete Tor. Rendete totalmente anonimi gli scambi atomici selezionando il menu **Onion**, dopo aver attivato la navigazione Tor nel vostro browser.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Ormai conoscete Boltz, una piattaforma Exchange unica nel suo genere che consente l'interoperabilità tra i diversi livelli dell'ecosistema Bitcoin .
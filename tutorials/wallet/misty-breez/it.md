---
name: Misty Breez
description: Il fulmine senza prua Wallet.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez è un Lightning Wallet autoportante sviluppato da Breez sulla base del suo Software Development Kit e della rete **Liquid** sviluppata da BlockStream.


Viene fornito con un approccio completamente nuovo per operare senza un nodo Lightning: un potenziale **GAME CHANGER** nei trasferimenti inter-rete Bitcoin.


In questo tutorial descriveremo il funzionamento di questo portafoglio e vi forniremo una panoramica completa.



## Come funziona Misty Breez?



Misty Breez è un'implementazione senza nodo Lightning come backend. È stata sviluppata sulla base di Breez SDK e Liquid.



Il Liquid è un Layer parallelo alla rete Bitcoin, che offre miglioramenti significativi in termini di velocità e costi di transazione. Questo Layer consente a Misty Breez di fare a meno di un nodo Lightning e di utilizzare invece servizi Exchange di terze parti, come **Boltz**, per garantire l'interoperabilità tra Liquid Network e Lightning Network. Non abbiate fretta, ci torneremo.



Per ora, iniziamo la nostra avventura con la Misty Breez Wallet.



## Come iniziare con Misty Breez



L'applicazione mobile di Misty Breez è disponibile sulle piattaforme di download ufficiali come Google Play Store (su Android) e Apple Store (su iOS). È anche possibile essere reindirizzati all'app giusta dal sito ufficiale [Misty Breez] (https://breez.technology/misty/).



⚠️ Assicuratevi di non confondere Misty Breez con il Breez Wallet.



⚠️ **IMPORTANTE**: Per la sicurezza dei vostri bitcoin, è essenziale scaricare l'applicazione da piattaforme ufficiali per garantirne l'autenticità.



![download-misty-breez](assets/fr/01.webp)



In questa guida partiremo da un dispositivo Android. Tuttavia, tutti i passaggi e le funzioni specifiche descritte in questa sezione sono validi anche per iOS.



Al momento dell'installazione, Misty Breez offre la possibilità di creare un nuovo Wallet o di ripristinare un vecchio Lightning Wallet per il quale si dispone delle parole di ripristino.


In questa esercitazione, abbiamo scelto di creare un nuovo portfolio.



⚠️Misty Breez è attualmente in fase di sviluppo, quindi vi consigliamo di iniziare con quantità ragionevoli.



![create-wallet](assets/fr/02.webp)


### Salvate le parole di recupero:


Una delle prime cose da fare quando si crea un nuovo portfolio è eseguire il backup delle 12 parole di recupero.


Ecco alcuni suggerimenti su come eseguire il backup della frase di backup.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Per eseguire il backup delle frasi, selezionare il menu **Preferenze > Sicurezza**, quindi l'opzione **Controllo della frase di backup**.



![backup](assets/fr/03.webp)


Per maggiore sicurezza, è anche possibile **creare un codice PIN** per autenticare l'accesso al proprio Wallet.




Trovate la vostra valuta locale nella moltitudine di valute accettate da Misty Breez. Configurate la vostra valuta dal menu **Preferenze > Valute Fiat**, quindi selezionate la valuta o le valute desiderate.



![devises](assets/fr/04.webp)



### Effettuare le prime transazioni


Se conoscete già il portafoglio Breez, non sarete affatto scoraggiati dall'intuitivo Interface di Misty Breez.



Nel menu **Bilancio** del Interface, fare clic sull'opzione **Ricevi** per creare fatture per ricevere i bitcoin sul Wallet.



⚠️ Misty Breez vi chiederà di attivare le notifiche per l'applicazione nelle impostazioni del telefono per avere diritto a un Address fulmineo.



Con Misty Breez è possibile :




- Ricevere bitcoin sul Lightning Network da **100 satoshis** fino a **25.000.000 satoshis**.
- Ricevere bitcoin sulla rete principale Bitcoin a partire da **25.000 satoshis**.



![transactions](assets/fr/05.webp)



È qui che inizia la magia di Misty Breez.


A differenza di Breez Wallet, che vi fornisce un nodo Lightning e vi chiede di coprire da soli i costi di apertura e chiusura dei canali di pagamento, Misty Breez non vi chiede di fare nulla. Come già detto, Misty Breez non funziona nemmeno sulla base di un nodo Lightning.



Diamo un'occhiata più da vicino dietro le quinte.



In realtà, possedete un portafoglio Liquid che è associato al vostro portafoglio Misty Breez. Logicamente, tratterete L-BTC (Liquid Bitcoin) a tassi fissi associati a servizi di conversione di satoshi sottomarini di terze parti che vi permetteranno di interoperare con il Lightning Network.



Quando si riceve un pagamento sul proprio Misty Breez Wallet, il mittente invia dei satoshi che passano attraverso un servizio di conversione come Boltz (attualmente utilizzato da Misty Breez), per convertire i satoshi inviati in L-BTC che saranno ricevuti sul proprio Misty Breez Wallet (associato Liquid Wallet).


Ecco un diagramma semplificato del processo dietro le quinte.



![lnswap-in](assets/fr/06.webp)



Fare clic sul Interface nel menu **Balance**, fare clic sull'opzione **Send** per pagare un Invoice Lightning.


Inserite la Lightning Invoice, la Lightning Address del vostro destinatario o semplicemente scansionate il codice QR sulla Invoice per effettuare il pagamento.



![send-bitcoins](assets/fr/07.webp)



Dietro le quinte, si abilita il Liquid Wallet associato al proprio Misty Breez Wallet a convertire l'equivalente di L-BTC in satoshis tramite Boltz, quindi si trasferiscono questi satoshis al Lightning Wallet del destinatario (presente sul Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Questa caratteristica dell'infrastruttura di Misty Breez consente agli utenti di effettuare transazioni anche quando Misty Breez è offline.



Per i più esperti, c'è anche un menu **Preferenze > Sviluppatori** che fornisce maggiori dettagli su :




- La versione del kit di sviluppo software Breez.
- La chiave pubblica della vostra Misty Breez Wallet.
- Il mutuatario, l'identificativo unico derivato dalla chiave pubblica primaria.
- Il saldo del portafoglio.
- Suggerimento Liquid, per l'invio di piccole quantità di L-BTC.
- Il puntale Bitcoin, per l'invio di piccole quantità di Bitcoin.



È inoltre possibile eseguire alcune azioni, come la sincronizzazione con il Liquid Network, il backup delle chiavi, la condivisione del registro attività e la scelta di eseguire una nuova scansione del Liquid Network.



![dev-mode](assets/fr/09.webp)


Congratulazioni! Ora avete una buona conoscenza del portafoglio Misty Breez e del suo contributo alle transazioni interrete Bitcoin. Se questo tutorial vi è stato utile, vi invitiamo a darci un pollice Green . Saremo lieti di ascoltarvi.



Per approfondire, vi consiglio anche di scoprire il nostro tutorial sul Aqua Wallet, che funziona in modo simile al Misty Breez :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125
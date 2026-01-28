---
name: Macadamia Wallet
description: Cashu mobile wallet per pagamenti BTC anonimi e istantanei
---

![cover](assets/cover.webp)



Macadamia Wallet è un wallet mobile per iOS che implementa il protocollo Cashu, un sistema di ecash Chaumian che consente pagamenti Bitcoin totalmente anonimi. Grazie alle firme cieche, nessun osservatore può collegare i vostri depositi alle vostre spese, offrendo una riservatezza simile a quella dei contanti fisici.



In questo tutorial vedremo come installare e configurare Macadamia, eseguire le prime transazioni Cashu (Mint, Send, Receive, Melt) e gestire più mentine per proteggere i vostri fondi.



## Che cos'è la Macadamia Wallet?



### Il protocollo Cashu



Cashu utilizza la firma cieca inventata da David Chaum: si depositano bitcoin presso un server "mint", che emette gettoni equivalenti in satoshi. La zecca firma questi gettoni senza vederne il contenuto, rendendo impossibile collegare un token a un utente. Gli scambi sono off-chain, peer-to-peer e totalmente opachi: nemmeno la zecca può sapere chi paga chi.



Macadamia è un wallet iOS open source sviluppato in Swift/SwiftUI. Funziona senza account o KYC, i vostri token sono memorizzati localmente e protetti da una frase seed. Il codice è verificabile su GitHub e i token sono interoperabili con altri portafogli Cashu (Minibits, Cashu.me).



### Modello di custodia e compromesso



**Importante**: Cashu opera su un modello di custodia. I gettoni sono promesse di pagamento (IOU) sostenute dalle riserve Bitcoin della zecca. Se la zecca scompare, i gettoni perdono il loro valore. Questo è il compromesso per ottenere la massima riservatezza.



Utilizzate Macadamia come wallet fisico: solo piccole quantità. Distribuite i fondi su più zecche per diluire il rischio.



## Caratteristiche principali



Macadamia implementa le quattro operazioni fondamentali del protocollo Cashu. **Mint** converte i satoshis in token tramite una fattura Lightning. **Invia** consente di inviare gratuitamente i gettoni tramite codice QR o link, completamente off-chain. **Ricevi** permette di ricevere gettoni o generate una fattura Lightning. **Fusione** permette di pagare una fattura Lightning distruggendo i gettoni.



wallet supporta la gestione di più zecche contemporaneamente. È possibile scambiare i gettoni tra le diverse zecche tramite Lightning.



## Piattaforme supportate



Macadamia è disponibile solo su iOS 17 o versioni successive per iPhone e iPad. L'applicazione nativa Swift/SwiftUI offre un'integrazione ottimale con l'ecosistema Apple.



Il protocollo Cashu garantisce l'interoperabilità tra i portafogli. È possibile ripristinare la frase seed in altre applicazioni come Minibits su Android o Nutstash su desktop.



La versione attuale è distribuita tramite TestFlight. Utilizzate solo piccole quantità con questa versione beta.



## Installazione



Macadamia è attualmente disponibile tramite TestFlight, il programma di beta testing di Apple. Ecco come installarlo:



### Installazione tramite TestFlight



**Fase 1: Scaricare TestFlight**



Se non avete già l'applicazione TestFlight sul vostro dispositivo, cercate "TestFlight" nell'App Store e installatela. TestFlight è l'applicazione ufficiale di Apple per testare le versioni beta delle applicazioni iOS.



**Fase 2: Partecipare al programma Macadamia beta** (in francese)



Una volta installato TestFlight, seguite questo link di invito dal vostro iPhone o iPad: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Il collegamento aprirà automaticamente TestFlight e vi proporrà di installare Macadamia Wallet. Toccare "Accetta" e poi "Installa" per avviare il download. L'applicazione pesa circa dieci megabyte e richiede solo pochi secondi per essere installata.



![Installation TestFlight](assets/fr/01.webp)



### Informazioni importanti sulle versioni beta



Macadamia è ancora in fase di sviluppo attivo. Le versioni di TestFlight vengono aggiornate frequentemente e possono introdurre nuove funzionalità o correggere bug. Tuttavia, come per ogni versione beta, possono verificarsi malfunzionamenti. **Si consiglia vivamente di utilizzare solo piccole quantità**, che si accetta possano andare perse in caso di problemi tecnici.



Macadamia non raccoglie alcun dato dell'utente in base all'informativa sulla privacy visualizzata. Assicurarsi di verificare che lo sviluppatore sia cypherbase UG al momento dell'installazione.



## Configurazione iniziale



Al primo avvio, Macadamia genera una frase BIP-39 di 12 parole. Scrivetele in un posto sicuro, mai come screenshot. Queste parole permettono di ricreare il wallet e di spendere i gettoni.



![Configuration initiale](assets/fr/02.webp)



Seguite le quattro fasi: benvenuto, accettazione dei termini, salvataggio della frase seed e conferma finale.



![Interface principale](assets/fr/03.webp)



Una volta completata la configurazione, Macadamia presenta tre schede principali. **Wallet** visualizza il saldo e la cronologia delle transazioni. **Mints** consente di gestire i server Cashu. **Impostazioni** consente di accedere alle impostazioni e alla frase seed.



![Ajout d'un mint](assets/fr/04.webp)



Ora è necessario configurare una zecca, ossia un server Cashu che emetterà i gettoni. Andate alla scheda "Zecche", toccate "Aggiungi un nuovo URL di zecca" e inserite l'indirizzo della zecca scelta (ad esempio mint.cubabitcoin.org). Per trovare zecche pubbliche affidabili, consultare bitcoinmints.com o cashu.space. Convalidare solo le zecche di cui si è verificata la reputazione, poiché saranno loro a custodire i satoshi.



## Uso quotidiano



### Creazione di nuovi gettoni (Zecca)



Per alimentare il wallet Macadamia con ecash, è necessario eseguire un'operazione "Mint" (per creare gettoni). Toccare "Ricezione", quindi scegliere l'opzione "Lampo". Inserire l'importo desiderato (ad es. 1000 sats), selezionare la menta da utilizzare, quindi generate la fattura Lightning.



![Opération Mint](assets/fr/05.webp)



Pagate la fattura Lightning generata con il vostro solito wallet (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



I gettoni Cashu appaiono immediatamente nel vostro saldo dopo il pagamento.



### Inviare i gettoni



Per inviare gettoni Cashu a un altro utente, toccare il pulsante "Invia" nella schermata principale, quindi selezionare "Ecash". Inserire l'importo da inviare (ad esempio, 50 sats) e aggiungere un promemoria descrittivo, se necessario.



![Envoi Ecash](assets/fr/07.webp)



Condividete il codice QR o il testo generato tramite iMessage, Signal o Telegram. Il destinatario richiede i fondi immediatamente e gratuitamente.



### Ricevere i gettoni



Per ricevere i gettoni Cashu inviati da un altro utente, toccare "Ricevi" e selezionare "Ecash". Scansionare il codice QR token o incollare il link token ricevuto.



![Réception Ecash](assets/fr/08.webp)



Toccare "Redeem" per richiedere il token.



### Pagamenti fulminei (fusione)



Per pagare una fattura Lightning con i gettoni Cashu, toccare "Invia" e selezionare "Lightning". Incollare la fattura BOLT11 che si desidera pagare.



![Paiement Lightning](assets/fr/11.webp)



La zecca distrugge i vostri gettoni ed esegue il pagamento Lightning. In questo modo è possibile pagare qualsiasi servizio Lightning mantenendo l'anonimato.



### Scambio di mentine



Quando si ricevono gettoni da una zecca non configurata, Macadamia offre diverse opzioni per la gestione di questi gettoni.



![Swap inter-mints](assets/fr/09.webp)



Aggiungete la nuova zecca o scambiate i gettoni con una zecca esistente. Lo scambio utilizza Lightning come ponte per trasferire i fondi in modo anonimo.



### Gestione avanzata di più zecche



Macadamia offre strumenti sofisticati per la gestione simultanea di più zecche e per l'allocazione strategica dei fondi.



![Gestion multi-mints](assets/fr/10.webp)



"Distribuisci fondi" distribuisce automaticamente il saldo in base a percentuali (ad esempio 50/50). "Trasferimento" consente di effettuare trasferimenti manuali tra le zecche per diversificare i rischi.



## Vantaggi e limiti



**Saluti** :





- Massima riservatezza**: Transazioni non rintracciabili, nemmeno dalla zecca. Nessun metadato della blockchain, scambi peer-to-peer senza traccia.
- Veloce e gratuito**: Trasferimenti istantanei gratuiti all'interno di una zecca, ideali per i micropagamenti.
- Interoperabilità**: token Cashu standardizzati da utilizzare con altri portafogli compatibili (Minibits, Nutstash).
- Semplicità**: Interface iOS nativo è accessibile ai principianti pur rimanendo verificabile (open source).



**Costrizioni** :





- Modello di custodia**: è necessaria la fiducia della zecca. Se una zecca scompare, i gettoni perdono il loro valore.
- solo iOS**: Nessuna versione Android/desktop. L'interoperabilità di Cashu consente l'accesso tramite altri portafogli, ma l'esperienza ottimale rimane iOS.
- Dipendenza da Mint**: Mint offline = incapace di effettuare transazioni che richiedono il suo intervento (Mint, Melt).
- Tecnologia emergente** : Sviluppo attivo, possibili bug, standard in evoluzione.



## Le migliori pratiche





- Diversificare le zecche**: Distribuite le vostre fiches su diverse zecche affidabili per diluire il rischio.
- Limitare gli importi**: Utilizzare Macadamia come wallet fisico per i pagamenti quotidiani, non come cassaforte.
- Mettete al sicuro il vostro seed**: Conservare la frase di 12 parole su carta in un luogo sicuro. Testate il restauro di tanto in tanto.
- Controllare le zecche**: Consultate cashu.space e i forum della comunità prima di aggiungere una zecca. Scegliete quelle con un buon tempo di attività e una solida reputazione.
- VPN o Tor**: Nascondete il vostro IP con VPN/Tor per massimizzare la privacy della rete.
- Unisciti alla comunità**: Gruppi Telegram/Discord Cashu per aggiornamenti, consigli sulla menta e best practice.



## Conclusione



Macadamia Wallet porta le proprietà del contante fisico nel Bitcoin digitale. Combinando le firme cieche Chaum e Lightning, offre una soluzione elegante per la riservatezza delle transazioni. La sua interfaccia nativa per iOS rende accessibile una sofisticata tecnologia crittografica, pur rimanendo open source e interoperabile con l'ecosistema Cashu.



Il modello custodiale richiede vigilanza e buone pratiche di sicurezza. Se usato correttamente, Macadamia diventa uno strumento prezioso per i pagamenti quotidiani che richiedono l'anonimato, a complemento dei portafogli non custodiali per i risparmi.



## Risorse



### Documentazione ufficiale




- Sito web ufficiale: [macadamia.cash](https://macadamia.cash)
- FAQ sulla macadamia: [macadamia.cash/faq](https://macadamia.cash/faq)
- Codice sorgente GitHub: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Documentazione Cashu




- Documentazione tecnica: [docs.cashu.space](https://docs.cashu.space)
- Elenco delle zecche pubbliche: [bitcoinmints.com](https://bitcoinmints.com)
- Sito ufficiale del protocollo: [cashu.space](https://cashu.space)



### Comunità




- Gruppo Telegram Cashu: [t.me/cashu_ecash](https://t.me/cashu_ecash)
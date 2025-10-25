---
name: StashPay
description: Il Bitcoin Wallet minimalista per tutti
---

![cover](assets/cover.webp)



L'esperienza dell'utente è un fattore chiave nell'adozione delle soluzioni Bitcoin in tutto il mondo. Fornire un'esperienza fluida, semplice e tecnicamente priva di ostacoli è la priorità per molti portafogli e piattaforme Exchange. A questo proposito, StashPay si distingue per il suo approccio minimalista, dimostrando allo stesso tempo la potenza del Lightning Network.



In questo tutorial daremo un'occhiata a questo portafoglio per scoprire come funziona e come è ideale per le piccole imprese o i solisti.



## Come iniziare con StashPay



StashPay è un Wallet auto-custode di Lightning riconosciuto soprattutto per la sua esperienza d'uso minimalista e incentrata sull'utente.  Con questo Wallet, non è necessaria alcuna conoscenza tecnica per ricevere e inviare i primi satoshi.



StashPay è un progetto open-source sviluppato in React Native e mira a risolvere il problema delle elevate commissioni di transazione anche con le transazioni sulla catena principale del protocollo Bitcoin. È disponibile come applicazione mobile su piattaforme Android e iOS tramite i link di download presenti sul [sito web](https://stashpay.me/).



![introduce](assets/fr/01.webp)



È importante scaricare l'applicazione Android dal sito web, poiché non è disponibile su Google Play Store.


Al termine del download, concedere le autorizzazioni necessarie per installare l'applicazione sul telefono Android.



Una volta installata l'applicazione, StashPay creerà un Bitcoin Wallet iniziale alla prima apertura. Prima di ogni transazione, vi consigliamo di eseguire un backup di questo Wallet. Di seguito, troverete tutte le nostre linee guida per garantire che le vostre frasi di recupero siano correttamente salvate.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Accedere alle impostazioni di StashPay cliccando sull'icona "Impostazioni", quindi cliccare sull'opzione **Crea backup**. Autorizzare quindi la visualizzazione delle frasi di recupero. Non copiate le frasi di recupero negli appunti del telefono, perché potrebbero essere accessibili ad altre applicazioni fraudolente installate sul cellulare.



![backup](assets/fr/02.webp)



È anche possibile recuperare un Bitcoin Wallet già in uso facendo clic sull'opzione **Recupera Wallet** e inserendo le 12 o 24 parole di recupero.



### Ricevi i tuoi primi satoshis su StashPay



Nella schermata iniziale, fare clic sul pulsante **Ricevi** e impostare un importo superiore a quello specificato in rosso. Nel nostro caso, con StashPay Wallet non possiamo ricevere meno di 0,11 USD.



![receive](assets/fr/03.webp)



Una volta definito l'importo, è possibile fare clic sul pulsante **Crea Invoice**, quindi scansionare o copiare il Invoice per inviarlo al mittente di satoshis.



![receive_sats](assets/fr/04.webp)



È possibile visualizzare la cronologia delle transazioni facendo clic sull'icona "orologio" nella pagina iniziale.



![network_fee](assets/fr/05.webp)



Avrete notato che per ricevere i satoshis dovrete pagare una tassa di rete. Queste commissioni verranno detratte dai satoshis che state per ricevere. Questo perché StashPay è un Wallet basato sul Breez Development Kit. Per ricevere i satoshis con l'implementazione senza nodi Lightning del Kit, Breez addebiterà al cliente (StashPay nel nostro caso) `0,25% + 40 satoshis`. Per saperne di più, consultate il nostro tutorial su Misty Breez.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Inviare bitcoin con StashPay



L'invio di bitcoin con StashPay è abbastanza intuitivo grazie alla Interface minimalista. Nella schermata iniziale, fare clic sul pulsante **Invia**. Scansionare il codice QR o incollare il Address a cui si desidera inviare i satoshis. StashPay rileverà automaticamente la catena di protocollo Bitcoin a cui si desidera inviare bitcoin.



![send](assets/fr/06.webp)



Poiché StashPay è un Wallet basato sul kit di sviluppo Breez, beneficia di un interessante vantaggio: l'invio di bitcoin sulla catena principale a basso costo. Breez utilizza il servizio Boltz per effettuare transazioni tra le diverse catene del protocollo Bitcoin, consentendo ai clienti che implementano il kit di sviluppo di beneficiare di questo servizio direttamente nella loro applicazione.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Tuttavia, Breez SDK impone un importo minimo al quale è possibile inviare bitcoin a un Address sulla catena principale.



![onchain](assets/fr/07.webp)



È anche possibile inviare bitcoin utilizzando il Lightning Address del destinatario. Esaminate i dettagli della transazione, quindi confermate facendo clic sul pulsante **Invia**.



![confirm](assets/fr/08.webp)



## Altre configurazioni



Nelle impostazioni di StashPay, è possibile regolare le configurazioni per personalizzare l'uso del Wallet.



StashPay vi permette di Exchange satoshis in base alla valuta locale di vostra scelta. Cliccate sull'opzione **Valute**, quindi cercate la vostra valuta nell'elenco delle +113 valute offerte da StashPay.



![currencies](assets/fr/09.webp)



Nel menu **Opzioni di ricezione** si trovano tutte le impostazioni per ricevere bitcoin con StashPay. Ad esempio, selezionando **Scegli Lightning o Onchain**, abilitate il vostro Wallet a ricevere bitcoin dalla catena principale.



![receive-onchain](assets/fr/10.webp)



L'opzione **Scansione indirizzi OnChain** consente di aggiornare il saldo del Wallet controllando tutti gli UTXO (bitcoin non ancora spesi) collegati ai vari indirizzi.



![rescan](assets/fr/11.webp)



Il menu **Esporta registro** elenca tutte le azioni dell'infrastruttura Breez e Boltz relative alle transazioni e agli scambi atomici tra le varie catene protocollari Bitcoin.



![export](assets/fr/12.webp)



Avete appena imparato a conoscere il minimale Bitcoin Wallet di StashPay. Se questo tutorial vi è stato utile, vi consigliamo il nostro tutorial su come iniziare con Bitcoin e guadagnare i vostri primi bitcoin.



https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f
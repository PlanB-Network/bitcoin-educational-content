---
name: Alby

description: Estensione del browser per Bitcoin e Lightning Network
---

![cover](assets/cover.webp)




Rendere sempre più facili i pagamenti con bitcoin è la sfida che molte aziende del settore devono affrontare. Alby si distingue dalla massa con la sua estensione Alby wallet per i browser. Questa estensione mira a creare un quadro fluido che rileva automaticamente gli indirizzi e consente di effettuare pagamenti in bitcoin senza attriti. In questo tutorial scopriamo l'estensione Alby e testiamo come facilita i pagamenti dal browser.




![video](https://youtu.be/nd5fX2vHuDw)




## Estensione Alby



L'estensione Alby è uno strumento che consente al browser web di interagire in modo semplice e sicuro con la rete Bitcoin e con il suo livello Lightning Network. È caratterizzata da tre aspetti:




- Lightning Network wallet: collegate il vostro nodo o conto Alby per inviare e ricevere bitcoin in modo rapido ed economico tramite il livello Lightning Network.
- Pagamenti fluidi via web: Elimina la necessità di scansionare codici QR o di passare da un'applicazione all'altra per i pagamenti in bitcoin sui siti web che supportano Lightning. Consente transazioni fluide con un solo clic, o senza conferma se si è impostato un budget.
- Un gestore Nostr: L'estensione gestisce le chiavi Nostr, facilitando la connessione e l'interazione con le applicazioni Nostr in qualità di firmatario sicuro senza esporre la chiave privata a tutte le piattaforme.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Collegarsi all'estensione



In questa esercitazione, utilizzeremo l'estensione Alby nel browser Firefox con un sistema operativo Ubuntu. Tuttavia, è disponibile anche su Windows e con browser come Chrome. Tuttavia, è disponibile anche su Windows e su browser come Chrome.



È possibile aggiungere l'estensione Alby al browser visitando il negozio di estensioni [Firefox](https://addons.mozilla.org/fr/firefox/addon/alby/) o il negozio di estensioni [Chrome](https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ È importante verificare che l'autore dell'estensione sia effettivamente l'account ufficiale di Alby, per evitare qualsiasi forma di pirateria o furto di bitcoin.



Aggiungete l'estensione al vostro browser facendo clic sul pulsante a destra.


Concedere le autorizzazioni necessarie per l'installazione e l'uso dell'estensione, quindi applicare l'estensione alla barra degli strumenti per facilitarne il recupero.



![pin](assets/fr/03.webp)



È inoltre necessario definire un codice di sblocco (molto importante), che garantirà un accesso sicuro al Lightning wallet dal browser. Si consiglia di impostare una password alfanumerica forte.



ℹ️ Conservare la password in un luogo sicuro per potervi accedere in caso di dimenticanza, poiché può essere modificata ma non recuperata.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Il Alby dimostra la sua adattabilità offrendo due scelte:




- Continuate con un conto Alby se volete usufruire delle applicazioni mantenendo il controllo dei vostri bitcoin.
- Collegare il proprio nodo wallet o Lightning se ne esiste già uno supportato dall'estensione.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


In questa esercitazione, sceglieremo di continuare con l'account Alby per sfruttare le caratteristiche dell'ecosistema Alby.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Accedere al proprio account Alby o crearne uno se non se ne possiede ancora uno.



![signup](assets/fr/05.webp)



## Effettuare i primi pagamenti



Una volta effettuato l'accesso, è possibile fare clic sull'estensione Alby nella barra degli strumenti per accedere al proprio portafoglio.



![buzzin](assets/fr/06.webp)



Una volta creato il vostro conto Alby, dovrete collegarlo a un wallet per poter spendere i satoshis. Per collegare il bitcoin wallet al vostro conto Alby, vi suggeriamo di utilizzare un nodo Alby Hub, che potete configurare sul vostro computer o sottoscrivere un piano offerto da Alby.



![hubplan](assets/fr/13.webp)




In questa esercitazione, il nostro account Alby è supportato da un'installazione locale sulla nostra macchina.


Per costruire il vostro nodo Alby, vi consigliamo la nostra guida Alby Hub.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Questo nodo consente di creare portafogli Lightning autocustoditi e di gestire in modo efficiente i canali Lightning per inviare e ricevere i satoshi.



![channels](assets/fr/14.webp)



Aprire i canali di ricezione che definiscono il numero totale di satoshi che si possono ricevere.



![receivechanal](assets/fr/15.webp)



Aprire canali di invio bloccando i satoshis su un indirizzo bitcoin onchain. I satoshis bloccati definiscono il totale dei satoshis che si possono spendere.



![spend](assets/fr/16.webp)



È ora possibile inviare e ricevere satoshi tramite l'estensione Alby.



![exchange](assets/fr/08.webp)



Da questo momento in poi, l'estensione Alby è in grado di rilevare gli indirizzi Lightning e le fatture disponibili sulle pagine web visitate dall'utente e suggerirà di pagarle in bitcoin o Lightning direttamente dalla propria estensione.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Protezione delle chiavi di recupero con la chiave master



La chiave master offerta dall'estensione Alby funge da overlay protettivo che consente di comunicare in modo sicuro con il livello di rete principale Bitcoin (Onchain), il sistema Nostr e permette di attivare la connessione Lightning con le applicazioni Nostr.



![masterKey](assets/fr/11.webp)



Questa chiave principale è composta da 12 parole simili alla frase di recupero. Si consiglia pertanto di conservarla con metodi sicuri per garantire che sia accessibile in qualsiasi momento.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Ora potete sperimentare i pagamenti bitcoin e Lightning senza attrito con l'estensione Alby. Se questa esercitazione vi è piaciuta, vi consigliamo la nostra esercitazione Alby Hub per configurare il vostro nodo Alby e controllare tutti gli aspetti dei vostri portafogli Alby da un'interfaccia semplice e potente.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a
---
name: Toro Bitcoin Wallet
description: Scopri come usare il toro Wallet Bitcoin
---

![cover](assets/cover.webp)



Questa guida illustra l'installazione, la configurazione e l'utilizzo di Bull Bitcoin Mobile. Imparerete come ricevere e inviare fondi sulle tre reti: onchain, Liquid e Lightning, e come trasferire il vostro Bitcoin da una rete all'altra. Le appendici forniscono risorse e contatti, informazioni di base e brevi spiegazioni di concetti tecnici.



## Introduzione



**Bull Bitcoin Mobile**, sviluppato da **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([crea account](https://app.bullbitcoin.com/registration/orangepeel)), è un Bitcoin Wallet **autonomo**, il che significa che avete il pieno controllo delle vostre chiavi private e quindi dei vostri fondi, senza dipendere da terzi. Open-source e radicato nella filosofia Cypherpunk, questo Wallet combina semplicità, riservatezza e funzionalità avanzate come gli swap cross-network e il supporto PayJoin. Consente di gestire i bitcoin su tre reti: **Bitcoin onchain**, **Liquid** e **Lightning**, ognuna adattata a usi specifici.



### Contesto di sviluppo



Il Wallet risponde a una sfida importante: Le tariffe della rete Bitcoin non sono adatte per i piccoli pagamenti o per l'apertura di piccoli canali Lightning autogestiti. Il Wallet Bull Bitcoin Mobile offre una soluzione auto-custode pur appoggiandosi alle 3 principali reti Bitcoin:





- Rete Bitcoin (onchain)**: Ideale per l'archiviazione a medio e lungo termine di UTXO e transazioni di grande valore, dove le commissioni sono proporzionalmente trascurabili.
- Liquid Network**: Progettato per transazioni veloci (~2 minuti), più riservate (importi nascosti) e a basso costo, perfetto per accumulare piccole somme o proteggere la propria privacy.
- Rete Lightning**: Ottimizzata per i pagamenti istantanei e a basso costo, adatta alle transazioni quotidiane di valore medio-piccolo.



Con Bull Bitcoin Mobile, ad esempio, si possono accumulare piccoli importi nei portafogli **Liquid** o **Lightning** e poi, una volta raggiunto un importo significativo, si può :





- Trasferimento alla rete onchain per l'archiviazione sicura a medio o lungo termine, con una maggiore riservatezza con Liquid e/o Lightning a monte, e con commissioni onchain per una singola transazione



### Evoluzione continua



Wallet è in continua evoluzione, quindi non stupitevi se troverete delle discrepanze tra questa guida e la vostra applicazione aggiornata.




- Ad esempio, a partire dal 19/07/2025, i pulsanti **"Acquista / Vendi / Paga "** sono visibili ma in grigio nell'applicazione, poiché queste opzioni, disponibili su Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel), saranno presto integrate per un'esperienza unificata. Il loro utilizzo rimarrà del tutto facoltativo. Molti altri sviluppi sono in corso o previsti: gestione multi-Wallet, passphrase, compatibilità con i portafogli hardware...
- Su [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), è possibile consultare gli argomenti attuali e i prossimi sviluppi. Poiché il progetto è al 100% open-source e "costruito in pubblico", è possibile inviare i propri suggerimenti e gli eventuali bug riscontrati.




## 1. Prerequisiti



Prima di iniziare a utilizzare **Bull Bitcoin Mobile**, assicurarsi di disporre dei seguenti elementi:





- Smartphone compatibile**: Un dispositivo **iOS** (iPhone o iPad) o **Android**
- Connessione a Internet
- Supporti di backup sicuri**: Scrivete la vostra **frase di recupero** (12 parole) su carta o metallo e conservatela in un luogo sicuro.
- Conoscenze di base**: È utile una conoscenza minima dei concetti di Bitcoin (indirizzi, transazioni, tariffe), anche se questo tutorial spiega ogni passaggio per i principianti.



## 2. Installazione





- Scarica la domanda** :
 - [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Download dal negozio di applicazioni per dispositivi Android
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Scarica direttamente l'APK per i dispositivi Android**
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)** Download via TestFlight per i dispositivi Apple
 - Controllare il nome dello sviluppatore (Bull Bitcoin) per evitare applicazioni fraudolente.
 - Assicurarsi che la versione scaricata corrisponda all'ultima versione stabile indicata su GitHub.
 - Bull Bitcoin Mobile è **open-source**. Per visualizzare il codice: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Installare l'applicazione




## 3. Configurazione iniziale



### 3.1 Avviare l'applicazione :



L'applicazione utilizza un'unica frase di recupero di 12 parole per entrambi i portafogli:




 - gW-26" Wallet**: Per le transazioni sulla rete Bitcoin (onchain)
 - pagamenti istantanei" Wallet**: Per transazioni istantanee sulle reti Liquid e Lightning



All'apertura, viene richiesto di importare una frase di recupero esistente o di creare un nuovo Wallet :



![image](assets/fr/02.webp)



### 3.2 Frase di recupero :



Se si desidera riutilizzare un Wallet esistente, fare clic su "**Recupera Wallet**" e inserire le 12 parole della frase di recupero.



Altrimenti, fare clic su "**Crea nuovo Wallet**" :




- Scrivete la vostra frase di recupero con la massima cura. Scrivetela su carta o metallo e conservatela in un luogo sicuro (cassetta di sicurezza, luogo offline). Questa frase è l'unico mezzo per accedere ai bitcoin in caso di perdita del dispositivo o di cancellazione dell'applicazione.
- È anche importante notare che chiunque abbia questa frase può rubare tutti i vostri bitcoin. Non conservateli mai in formato digitale:
 - Nessuna schermata
 - Nessun backup su cloud, e-mail o messaggistica
 - Nessun copia/incolla (rischio di salvare negli appunti)



**! Questo punto è fondamentale**. Per ulteriore assistenza :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Protezione dell'accesso :





- Andare alle impostazioni e cliccare su **Codice PIN**.
- Impostare un robusto **codice PIN** per proteggere l'accesso all'applicazione.
- Questa fase è facoltativa, ma fortemente consigliata per evitare che qualcuno che ha accesso al telefono possa accedere al Wallet.



![image](assets/fr/03.webp)



### 3.4 Connessione a un nodo personale (opzionale):



Il Wallet BullBitcoin si connette di default ai server Electrum: il primo gestito da Bull Bitcoin e un server secondario di Blockstream, entrambi considerati privi di registri, riducendo il rischio di tracciamento.



Per una maggiore riservatezza, è possibile collegare l'applicazione al proprio nodo Bitcoin tramite un server Electrum (istruzioni disponibili su [GitHub di BullBitcoin](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Ricezione di fondi



Ricevere fondi con **Bull Bitcoin Mobile** è semplice e adatto alle vostre esigenze, sia che usiate :




  - la rete **Bitcoin (onchain)** per la conservazione a lungo termine,
  - la rete **Liquid** per una rete più veloce e più Confidential Transactions,
  - la rete **Lightning** per pagamenti istantanei e di basso valore.



L'applicazione genera automaticamente gli indirizzi di ricezione Lightning o Invoice, a seconda della rete selezionata. Ecco come procedere per ciascuna rete.



### 4.1. onchain (rete Bitcoin)



Nella schermata iniziale, è possibile :




- oppure selezionare il **Secure Bitcoin Wallet** e cliccare su "**Receive "** :



![image](assets/fr/04.webp)





- oppure fare clic su "**Ricezione "**, quindi scegliere la rete **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Opzione "Copia o scansione solo Address" disabilitata (impostazione predefinita)



![image](assets/fr/06.webp)





- Consente di accedere a parametri avanzati opzionali. È possibile specificare :
 - Un **importo** in BTC, Sats o fiat.
 - Una **nota personale** da includere nella copia del codice URI / QR.
 - Attivazione di **PayJoin** (per i dettagli, vedere l'Appendice 3), che migliora la riservatezza combinando le voci del mittente e del destinatario.





- Esempio di URI generato automaticamente** :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- Utilizzo**: Copiare l'URI per condividerlo con il mittente o fargli scansionare il codice QR.



#### 4.1.2. Opzione "Copia o scansione solo Address" attivata



![image](assets/fr/07.webp)





- Con l'opzione **"Copia o scansione solo Address"** abilitata, l'applicazione genera un semplice Bitcoin Address in formato SegWit (bech32).





- Esempio:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Anche se si inserisce un importo o una nota, questi non saranno inclusi nel codice QR o nella copia del Address





- Utilizzo**: Copiare il Address per condividerlo con il mittente o fargli scansionare il codice QR.



#### 4.1.3. Generazione di un nuovo Address





- Perché utilizzare un nuovo Address per ogni transazione? Questo **protegge la vostra privacy** impedendo che più pagamenti siano collegati allo stesso Address, e limita le possibilità di tracciamento sul Blockchain.
 - Per impostazione predefinita, Bull Bitcoin genera automaticamente un Address.** non utilizzato
 - È possibile forzare la creazione di un nuovo Address facendo clic su **"Nuovo Address"** in fondo alla schermata.
 - Tutti i vostri indirizzi sono collegati alla vostra frase seed: indipendentemente dal numero di indirizzi utilizzati, il vostro portafoglio mostrerà un unico saldo e potrà consolidare automaticamente i fondi quando viene effettuata una spedizione.





- Suggerimento: Utilizzare sempre il nuovo Address** fornito da Bull Bitcoin, a meno che non si abbia una necessità specifica (ad esempio, un Address pubblico per ricevere donazioni).



### 4.2. Liquid



Nella schermata iniziale, è possibile :




- oppure selezionare il **Pagamento immediato Wallet** e cliccare su **"Ricezione "** e poi su **"Liquid"** :



![image](assets/fr/08.webp)





- oppure fare clic su "**Ricezione "**, quindi scegliere la rete **Liquid**:



![image](assets/fr/09.webp)



Una volta visualizzata la schermata **"Ricezione "**, copiare un Liquid Address:





- Nessun importo o nota. Esempio:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Oppure specificando un **importo** (in BTC, Sats o fiat) e/o una **nota personale** da includere nella copia dell'URI / QR Code. Esempio:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Utilizzo**: Copiare il Address/URI per condividerlo con il mittente o fargli scansionare il codice QR.



### 4.3. Fulmini



Nella schermata iniziale, è possibile :




- oppure selezionare il **Pagamento immediato Wallet** e cliccare su "**Ricevi "** :



![image](assets/fr/10.webp)





- oppure fare clic su "**Ricezione "**, quindi scegliere la rete **Lightning**:



![image](assets/fr/11.webp)



#### 4.3.1. Funzionamento, limiti e vantaggi





- Meccanismo**: Bull Bitcoin Wallet è un Wallet che consente di effettuare e ricevere pagamenti tramite Lightning. I fondi ricevuti tramite Lightning sono memorizzati sulla rete **Liquid** (nei pagamenti istantanei Wallet) grazie a uno scambio automatico tramite **Boltz**. In questo modo si ha la possibilità di interagire con Lightning senza dover gestire canali di liquidità, rimanendo in autocustodia.





- Limiti:**
 - Un importo minimo** di 100 satoshi (a partire dal 19.07.2025) per il generate e il Invoice.
 - I costi** sono a vostro carico e vengono detratti dall'importo inviato dal mittente, a differenza della ricezione con Wallet Lightning native, dove solo il mittente paga i costi di trasferimento oltre all'importo inviato. Al 19/07/2025, 47 Sats vengono detratti dall'importo inviato.





- Benefici** :
 - Autotutela**: I vostri fondi rimangono sotto il vostro controllo, memorizzati sul Liquid Network.
 - Nessuna commissione onchain elevata**: L'accumulo su Liquid evita costosi depositi onchain per aprire il canale Lightning o aggiungere liquidità. Queste operazioni possono essere effettuate in un secondo momento, quando l'importo accumulato su Liquid giustifica le commissioni.





- Suggerimento: ** Se il mittente dispone di Wallet Bull Bitcoin, utilizzare direttamente il Liquid Network per evitare le spese di scambio



#### 4.3.2. generate Invoice





- Inserire un **importo** (in BTC, Sats o fiat)





- Aggiungere una **nota personale** che sarà integrata nel Invoice. Se il mittente paga il Invoice, anche il vostro Wallet lo includerà nei dettagli della transazione.





- Validità Invoice:** Il Lightning Invoice è valido per **12 ore**. Dopo questo periodo, scade e non può più essere pagato. È necessario generare un nuovo Invoice.





- Utilizzo**: Copiare il Invoice per condividerlo con il mittente o fargli scansionare il codice QR.




## 5. Invio di fondi



### 5.1. Principio di base



Sia dalla home page, sia dai portafogli :



![image](assets/fr/12.webp)



per accedere alla schermata di invio:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** semplifica l'invio di denaro rilevando automaticamente la rete (Bitcoin, Liquid o Lightning) in base al Address o Invoice inserito (copiato o scansionato tramite codice QR).



### 5.2. trasmissione a catena (rete Bitcoin)



#### 5.2.1. Schermata di invio



**Azione**: Immettere o scansionare un Bitcoin sulla catena Address





- Se l'importo non è stato definito, ad esempio :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Quindi è possibile scegliere nella schermata di invio :
 - Importo in BTC, sat o fiat. Importo minimo: 546 satoshis il 22/07/2025.
 - Una nota opzionale per identificare la transazione. Visibile solo all'utente, nei dettagli della transazione.



![image](assets/fr/14.webp)





- Se l'importo è già stato definito, ad esempio :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Verrete quindi portati direttamente alla schermata di conferma qui sotto.



#### 5.2.2 Schermata di conferma



Prendete il tempo necessario per controllare tutti i parametri, in particolare l'importo, la destinazione Address e le commissioni.


Quindi è possibile regolare i parametri:



![image](assets/fr/15.webp)




- Tariffe**: È possibile scegliere :
  - La velocità di esecuzione** della transazione e le commissioni associate saranno stimate
  - Verranno stimate le commissioni**, in modalità Assoluta (commissioni totali in satoshi) o Relativa (commissioni per byte), e la velocità della transazione





- Impostazioni avanzate** :





 - Replace-by-fee (RBF)** : Attivata per impostazione predefinita, questa funzione accelera la transazione pagando una tariffa più alta (per i dettagli, vedere l'Appendice 4).





 - Selezione manuale del UTXO**: Se i fondi sono archiviati presso diversi indirizzi Wallet, è possibile selezionare gli indirizzi da cui inviare i fondi. Perché farlo? Con la crescente adozione del Bitcoin, le spese di trasferimento stanno aumentando. L'invio da più indirizzi per piccoli importi è più costoso rispetto all'invio da un singolo Address, ma farlo ora evita di doverlo fare in seguito, quando le commissioni saranno ancora più alte. Questa operazione si chiama **consolidamento del UTXO.**



![image](assets/fr/16.webp)





- Invio con PayJoin**: Se la funzione è stata attivata dal destinatario che ha fornito l'URI, ad esempio :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Quindi Bull Bitcoin Mobile configurerà l'invio combinando i propri UTXO con quelli del destinatario come input, migliorando la riservatezza (per i dettagli, vedere l'Appendice 3).



### 5.3. Inviare a Liquid



#### 5.3.1 Schermata di invio



La rete **Liquid** consente transazioni veloci (~2 minuti grazie a un blocco al minuto), più riservate (importi mascherati) rispetto alla rete onchain e con commissioni molto basse. I fondi vengono prelevati da **Instant Payments Wallet**.



**Azione**: Inserire o scansionare un Liquid Address





- Se l'importo non è stato definito, ad esempio :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Quindi è possibile scegliere nella schermata di invio :




- Importo in BTC, sat o fiat. Nessun minimo, 1 Satoshi possibile;
- Una nota opzionale per identificare la transazione. Visibile solo all'utente, nei dettagli della transazione.



![image](assets/fr/17.webp)





- Se l'importo è già stato definito, ad esempio :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Verrete quindi portati direttamente alla schermata di conferma qui sotto.



#### 5.3.2 Schermata di conferma



Prendetevi il tempo necessario per controllare tutti i parametri, in particolare la quantità e la destinazione Address.



![image](assets/fr/18.webp)





- Commissioni**: Proporzionale alla complessità della transazione, generalmente su base 0,1 sat/vB, ossia 20-40 satoshis per una transazione semplice (33 Sats al 22/07/2025).



### 5.4. Invia a Lightning



#### 5.4.1 Schermata di invio



La rete **Lightning** consente pagamenti istantanei e a basso costo per piccoli importi, ideali per le piccole transazioni quotidiane.



**Azione**: Inserire o scansionare un fulmine Invoice





- Se si esegue la scansione di un LN-URL Address che consente di impostare la quantità di


Esempio: `orangepeel@walletofsatoshi.com`.


poi si può scegliere nella schermata di invio :




 - Importo in BTC, sat o fiat. Importo minimo di 1000 satoshis il 23/07/2025
 - Una nota opzionale per identificare la transazione. Verrà inviata al destinatario.



![image](assets/fr/19.webp)





- Se si esegue la scansione di un Lightning Invoice che contiene una quantità definita di


Esempio:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Verrete quindi portati direttamente alla schermata di conferma qui sotto.



Nota: l'importo deve essere superiore a 21 Sats il 23.07.2025



#### 5.4.2 Funzionamento, limiti e vantaggi





- Meccanismo**: I fondi vengono prelevati da **Pagamenti istantanei Wallet** (Liquid) e convertiti tramite uno swap **Liquid → Lightning** con **Boltz**.





- Limiti:**
 - Una quantità minima** superiore a quella di un Wallet Lightning native (vedi sopra)
 - Spese** più Liquid → Scambio di fulmini via Boltz





- Benefici** :
 - Autotutela**: I fondi rimangono sotto il vostro controllo, memorizzati sul Liquid Network e trasferibili tramite Lightning, se necessario
 - Nessuna commissione onchain elevata**: L'accumulo su Liquid vi ha risparmiato costosi depositi onchain per aprire il vostro canale Lightning o aggiungere liquidità. Queste operazioni possono essere effettuate in un secondo momento, quando l'importo accumulato su Liquid giustifica le commissioni.





- Suggerimento: ** Se il destinatario dispone di Wallet Bull Bitcoin, utilizzare direttamente il Liquid Network per evitare costi di scambio



#### 5.3.3 Schermata di conferma



Prendetevi il tempo necessario per controllare tutti i parametri, in particolare la quantità e la destinazione Address.



![image](assets/fr/20.webp)




## 6. Visualizza la storia



**Bull Bitcoin Mobile** consente di monitorare facilmente le transazioni effettuate sulle reti **Bitcoin (onchain)**, **Liquid** e **Lightning**. La cronologia è accessibile in due modi e visualizza informazioni dettagliate per ogni tipo di transazione. È inoltre possibile controllare le transazioni utilizzando browser di blocco esterni.



### 6.1. Storia dell'accesso





- Tramite la schermata iniziale** :
 - Cliccare su **Secure Bitcoin Wallet** per visualizzare le transazioni **onchain**, o su **Instant Payments Wallet** per le transazioni **Liquid** e **Lightning**.
 - Lo storico viene visualizzato direttamente sotto il totale del portafoglio, filtrato in base al tipo di Wallet selezionato.



![image](assets/fr/21.webp)





- Tramite la pagina dedicata** :
 - Nella schermata iniziale, fare clic sul simbolo della **storia** (icona dell'orologio o simile).
 - Accedere a una pagina che elenca tutte le transazioni, con filtri per tipo di azione: **Invio**, **Ricezione**, **Scambio**, **PayJoin**, **Vendita**, **Acquisto** (nota: Vendita e Acquisto sono in fase di sviluppo e non disponibili al momento, 20 luglio 2025).



![image](assets/fr/22.webp)



### 6.2. Dettagli della transazione



Ogni transazione mostra informazioni specifiche a seconda della rete e del tipo di azione (invio o ricezione). Ecco i dettagli disponibili per una **transazione onchain** :



![image](assets/fr/23.webp)



### 6.3. Controllo tramite Block explorer



L'elenco degli esploratori delle reti **Bitcoin onchain**, **Liquid** e **Lightning** è riportato nell'Appendice 4.



Per **Lightning**, le transazioni non sono visibili sui browser pubblici. Controllare i dettagli (compreso lo Swap ID per Boltz) nella domanda.




## 7. Impostazioni



La pagina "Impostazioni" è accessibile direttamente dalla home page dell'applicazione Bull Bitcoin ed è utilizzata per configurare e gestire vari aspetti del portafoglio e dell'esperienza dell'utente.



![image](assets/fr/24.webp)





- Wallet Backup**: Visualizza la frase di ripristino del portafoglio per il backup sicuro. Vedere la sezione 3. sulla creazione del portfolio per le migliori pratiche di gestione e archiviazione della frase di ripristino.





- Wallet Dettagli** :
 - Pubkey**: Chiave pubblica associata al Wallet, utilizzata per gli indirizzi di ricezione del generate Bitcoin.
 - Percorso di derivazione**: Percorso di derivazione utilizzato per ottenere gli indirizzi generate Wallet dalla chiave privata.





- Server Electrum (Nodo Bitcoin)**: Impostare una connessione a un nodo Bitcoin personalizzato per le transazioni onchain.





- Codice PIN**: Attivare e/o modificare il codice di sicurezza per proteggere l'accesso all'applicazione e alle funzioni Wallet.





- Valuta**: Scegliere se visualizzare gli importi in BTC o Sats e la valuta fiat predefinita (dollaro, euro, ecc.).





- Impostazioni di Auto Swap**: La funzione _Auto Swap_ vi permette di automatizzare il trasferimento dei vostri BTC dal **Pagamenti istantanei Wallet (Liquid)** al vostro **Bitcoin On-Chain** Wallet, non appena l'importo raggiunge una soglia che ritenete abbastanza alta da giustificare la commissione di transazione.





- Registri**: Registri di attività visualizzabili, che possono essere condivisi con l'assistenza tecnica per facilitare la risoluzione dei problemi.





- Accesso a Telegram per l'assistenza** : Collegamento diretto al canale Telegram ufficiale per l'assistenza agli utenti.





- Accesso a Github** : Collegamento al [repository Github di Bull Bitcoin](https://github.com/SatoshiPortal) per visualizzare il codice open-source o segnalare problemi.




## APPENDICI



### A1. Spiegazione di PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definizione** :




- PayJoin, o **Pay-to-EndPoint (P2EP)**, è una tecnica di transazione Bitcoin che migliora la riservatezza sulla rete **onchain**. Combina le voci del mittente e del destinatario in un'unica transazione, rendendo gli importi e gli indirizzi più difficili da rintracciare.



**Operazione:**




- In una transazione PayJoin, il mittente e il destinatario collaborano tramite un server PayJoin compatibile per effettuare una transazione congiunta.
- Invece di essere solo il mittente a fornire voci (UTXO), anche il destinatario contribuisce con uno dei propri UTXO. Questo confonde le informazioni visibili sul Blockchain: invece di una singola voce corrispondente all'importo effettivo, ci sono ora due voci, e le uscite non riflettono direttamente l'importo scambiato.
- La transazione finale assomiglia a una transazione Bitcoin standard (multi-input/multi-output), ma nasconde l'importo effettivo inviato e i collegamenti tra gli indirizzi grazie a una struttura steganografica.



**Per l'utilizzo con Bull Bitcoin Mobile**




- Ricezione** (Address Supply): PayJoin è abilitato per impostazione predefinita.
- Invia** : Il Wallet rileva automaticamente un URI PayJoin e configura la transazione di conseguenza, ad esempio:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Benefici**




- Maggiore riservatezza**: Il PayJoin invalida l'ipotesi che tutte le voci di una transazione appartengano a un'unica entità. Con il PayJoin, gli input provengono sia dal mittente che dal destinatario, rompendo questo presupposto.
- Mascheramento dell'importo** : L'importo effettivo scambiato non compare direttamente nei risultati. Viene calcolato come la differenza tra il UTXO in entrata e in uscita del destinatario, rendendo l'analisi fuorviante.



**Limiti**




- PayJoin richiede che il mittente e il destinatario utilizzino portafogli compatibili, altrimenti viene utilizzata una transazione onchain standard.
- La transazione è leggermente più complessa (più ingressi e uscite), con conseguenti costi leggermente più elevati.
- Sebbene sia stata progettata per assomigliare a una transazione standard, l'euristica avanzata (ad esempio, output ambigui, server PayJoin noti) può indurre a sospettare il suo utilizzo, anche se senza certezza assoluta.



**Maggiore informazione:**




- [Glossario](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Spiegazione di Replace-by-fee (RBF)



**Definizione**: Replace-by-fee (RBF) è una funzione della rete Bitcoin che consente al mittente di accelerare la conferma di una transazione **onchain** accettando di pagare una tariffa più alta.



**Limiti** :




- Il RBF non è disponibile per le transazioni Liquid o Lightning.
- La transazione iniziale deve essere contrassegnata come compatibile con RBF al momento della sua creazione, cosa che Bull Bitcoin Mobile fa automaticamente se non è disabilitata.



**Maggiore informazione:**




- [Glossario](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Le migliori pratiche



Per utilizzare **Bull Bitcoin Mobile** in modo sicuro ed efficiente, seguire queste raccomandazioni. Vi aiuteranno a proteggere i vostri fondi, a ottimizzare le vostre transazioni e a preservare la vostra riservatezza sulle reti **Bitcoin (onchain)**, **Liquid** e **Lightning**.





- Proteggete la vostra frase di recupero** :
 - Tutorial: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Utilizzare l'autenticazione sicura** :
 - Attivare un **PIN forte** o una **autenticazione biometrica** (impronta digitale o riconoscimento facciale) per proteggere l'accesso all'applicazione.
 - Non condividete mai il vostro PIN o i dati biometrici.





- Proteggere la privacy** :
 - generate un nuovo Address per ogni ricezione onchain o Liquid per limitare il tracciamento sul Blockchain.
 - Utilizzare il PayJoin quando disponibile per aumentare la riservatezza della quantità inviata sulla catena
 - Per la massima riservatezza, connettete il vostro Wallet al vostro nodo Bitcoin tramite un server Electrum invece di utilizzare il nodo pubblico





- Scegliete la rete più adatta alle vostre esigenze** :
 - Onchain**: Preferito per la custodia a lungo termine o per le transazioni di grande valore (commissioni trascurabili rispetto all'importo).
 - Liquid**: Da utilizzare per trasferimenti rapidi e a basso costo con una maggiore riservatezza.
 - Lampo**: Opta per trasferimenti istantanei e a basso costo per piccoli importi. Se siete due utenti Wallet Bull Bitcoin, scegliete Liquid per evitare le spese di scambio Lightning <> Liquid tramite Boltz.





- Controllare sempre gli indirizzi di spedizione** :
 - Prima di inviare fondi, controllare attentamente il Address. I fondi inviati al Address sbagliato sono persi per sempre. Utilizzare il copia/incolla o la scansione del codice QR, non copiare/modificare mai un Address a mano.





- Ottimizzare i costi** :
 - Per le transazioni onchain, scegliere le tariffe appropriate (lente, medie, veloci) in base all'urgenza e alla congestione della rete.
 - Utilizzare Liquid o Lightning per piccole quantità.
 - Attivare il Replace-by-fee (RBF) (vedere Appendice 4) per le spedizioni onchain se si prevede di dover accelerare la conferma.





- Mantenere l'applicazione aggiornata




### A4. Risorse aggiuntive





- Link ufficiali e supporto:**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : e-mail di supporto
 - [Sito ufficiale di Bull Bitcoin](https://bullbitcoin.com/) :** Informazioni sui servizi di Bull Bitcoin, creazione dell'account, accesso all'applicazione
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** Visualizzare il codice, l'evoluzione e la roadmap, contribuire allo sviluppo...
 - [Account X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)**
 - Gruppo Telegram** per Wallet mobile: chat di gruppo con l'assistenza, vedere la pagina "Impostazioni".





- Esploratori di blocchi :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Fulmine: **[1ML (Lightning Network)](https://1ml.com/)**





- Apprendimento ed esercitazioni:** **[Plan ₿ Network](https://planb.network/)** :
 - Protezione della frase di recupero



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Glossario](https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network** :
 - [Glossario](https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Toro Bitcoin



#### Panoramica dell'azienda



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, è la più antica piattaforma non depositaria Exchange dedicata esclusivamente al Bitcoin, fondata nel 2013 presso l'Ambasciata Bitcoin di Montreal, Canada. Diretta da Francis Pouliot, riconosciuto pioniere dell'ecosistema Bitcoin, l'azienda si posiziona come attore chiave nella promozione della sovranità finanziaria e dell'autonomia degli utenti. La sua missione è consentire agli individui di riprendere il controllo del proprio denaro utilizzando il Bitcoin come strumento di libertà e di pagamento, rifiutando le valute fiat e le criptovalute diverse dal Bitcoin.



![image](assets/fr/26.webp)



[Crea il tuo account](https://app.bullbitcoin.com/registration/orangepeel) con lo 0,25% di sconto su acquisti e vendite di Bitcoin.



#### Valori e filosofia



Bull Bitcoin si distingue per i suoi principi da Commitment a Cypherpunk e per l'etica Bitcoin:





- Focus esclusivo su Bitcoin** : La piattaforma è fedele alla visione di una valuta decentralizzata e resistente alla censura.





- Non depositario** : Gli utenti mantengono il pieno controllo dei loro Bitcoin inviando i fondi ai propri portafogli.





- Riservatezza**: Raccolta di dati personali ridotta al minimo, con opzioni di acquisto senza KYC per transazioni inferiori a 999 USD. I dati sono protetti in conformità alle normative (FINTRAC in Canada, AMF in Francia).





- Trasparenza**: Nessuna spesa nascosta, i costi sono inclusi nello spread (la differenza tra i prezzi di acquisto e di vendita).





- Sovranità finanziaria**: La bolla Bitcoin promuove l'indipendenza dai sistemi bancari tradizionali e dalle istituzioni centralizzate.



#### Servizi principali





- Deposito Fiat** : Gli utenti possono finanziare il proprio conto Bull Bitcoin con valuta fiat (CAD, EUR, ecc.) tramite bonifico bancario o contanti/carta di debito presso uffici postali canadesi selezionati.





- Acquisto di Bitcoin** : Gli utenti possono acquistare il Bitcoin che viene inviato direttamente al loro portafoglio non depositato, garantendo il controllo totale dei loro fondi.





- Acquisto programmato di Bitcoin**: Bull Bitcoin offre un servizio di acquisto ricorrente automatizzato (DCA - Dollar Cost Averaging) a intervalli regolari, attingendo al saldo disponibile, con trasferimento diretto dei Bitcoin a un Wallet controllato dall'utente, riducendo l'impatto della volatilità dei prezzi.



Si noti che un'opzione chiamata "AutoBuy" consente di convertire i fiat non appena toccano il saldo Bull Bitcoin, e di inviare i Bitcoin al proprio Wallet. Questa opzione può anche essere combinata con un bonifico bancario ricorrente programmato con la propria banca per effettuare un DCA. Questa opzione automatizza l'accumulo di Bitcoin senza dover mai aprire l'applicazione.






- Acquisto di Bitcoin a un prezzo fisso "Ordine limite "**: Permette di acquistare il Bitcoin a un prezzo specificato in anticipo dall'utente, che viene eseguito automaticamente quando il prezzo dell'indice Bull Bitcoin raggiunge o scende al di sotto del limite impostato.





- Vendita di Bitcoin**: Gli utenti possono vendere i loro Bitcoin e ricevere i fondi in valuta fiat direttamente sul loro conto bancario tramite bonifico bancario o SEPA.





- Pagamenti da parte di terzi**: Bull Bitcoin consente agli utenti di inviare denaro fiat a conti bancari dai loro Bitcoin, in modo completamente trasparente per il destinatario.





- Bull Bitcoin Prime**: Bull Bitcoin Prime è un servizio premium per i clienti con un alto patrimonio netto e per le aziende, che offre soluzioni personalizzate e un'assistenza premium. Ciò include l'accesso a commissioni ridotte, un gestore del conto dedicato e servizi aziendali su misura. Questo servizio è rivolto a istituzioni, trader professionisti e clienti aziendali che desiderano competenze approfondite e un trattamento prioritario.





- Wallet mobile**: Bull Bitcoin offre un Wallet mobile open-source e autocustodiale, disponibile su Android e iOS, che supporta le transazioni onchain, Liquid e Lightning Network.





- Supporto educativo**: Guide gratuite e coaching personalizzato per aiutare gli utenti a creare, proteggere e gestire il proprio portafoglio Bitcoin, rafforzando l'autonomia finanziaria.



#### Conformità e sicurezza





- Regolamentazione**: Registrato presso FINTRAC (Canada) e AMF (Francia), Bull Bitcoin è conforme ai requisiti KYC/AML.





- Sicurezza**: Utilizzo di portafogli sicuri e raccomandazioni di archiviazione offline. I dati personali sono ospitati sull'infrastruttura Bitcoin di Bull, che è al 100% self-hosted e non si affida a terzi.
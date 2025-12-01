---
name: Debifi
description: Ottenere un prestito non detentivo garantito da Bitcoin.
---

![cover](assets/cover.webp)




## Introduzione



Per secoli, il credito tradizionale ha permesso di finanziare molti progetti. Tuttavia, rimane lento, costoso e poco inclusivo, soprattutto per coloro che non hanno accesso a una solida infrastruttura bancaria.



L'ascesa del protocollo Bitcoin ha inaugurato una nuova era finanziaria, portando con sé una serie di sfide. Una di queste sfide era come ottenere liquidità senza essere costretti a vendere il Bitcoin, perdendo così l'esposizione al suo potenziale di crescita



Il risultato è **Debifi**, una piattaforma che si pone come moderna alternativa alle banche. L'obiettivo è chiaro: rendere il credito il più semplice e trasparente possibile, combinando i vantaggi del sistema finanziario tradizionale con la libertà offerta dal Bitcoin. Il nome Debifi riflette questa visione: ***Finanza decentralizzata Bitcoin***, una contrazione che illustra l'incontro tra la finanza decentralizzata e l'innovazione Bitcoin.



Debifi è una piattaforma di prestito non custodiale sostenuta da Bitcoin, il che significa che l'utente mantiene il controllo delle proprie chiavi private. Permette agli utenti di sbloccare liquidità in cambio dei loro bitcoin bloccati come garanzia. A differenza dei prestiti bancari tradizionali, Debifi utilizza un sistema di deposito a garanzia con più firme (3 su 4) e non accetta la ri-ipotecazione del collaterale, garantendo maggiore sicurezza e trasparenza.



In pratica, ciò significa che né Debifi né un singolo prestatore possono spendere i vostri BTC senza l'accordo di tre parti (voi, il prestatore e una terza parte fidata). Questo rende il sistema più sicuro: se prendete un prestito su Debifi, mantenete la proprietà del vostro Bitcoin fino al completo rimborso del prestito.



## Vantaggi di Debifi



Con Debifi, ottenete prestiti garantiti da Bitcoin che sono iper-collateralizzati e garantiti da on-chain. I vostri fondi sono al sicuro grazie ai portafogli multi-firma, alla 2FA e al controllo totale sul vostro Bitcoin: voi tenete le vostre chiavi, voi tenete le vostre monete. Prestiti in una gamma di opzioni in monete stabili o fiat, a tassi competitivi e con liquidità globale.



Ecco un rapido confronto tra un prestito Debifi e un prestito bancario tradizionale:


| Characteristics        | Loan via Debifi                                                        | Traditional Bank Loan                                                       |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Accessibility          | ✔️ Open to any Bitcoin holder (even without banking history)           | ❌ Often limited to clients with physical collateral and strong records      |
| Speed of approval      | ✔️ Funds available within minutes or hours                             | ❌ Lengthy process (days or weeks)                                           |
| Required guarantees    | ✔️ Bitcoin used as the sole collateral                                 | ❌ Physical guarantees (property, land, stable income)                       |
| Asset control          | ✔️ You keep exposure to Bitcoin and its upside potential               | ❌ No connection between the loan and your financial assets                  |
| Geographic flexibility | ✔️ Available everywhere (no banking jurisdiction constraints)          | ❌ Restricted to the bank’s jurisdiction                                     |
| Main risk              | ❌ Liquidation risk if BTC price drops too sharply                      | ❌ Risk of asset seizure or negative impact on credit score                  |

Prima di mostrarvi passo dopo passo come ottenere un prestito su Debifi, ci sono alcuni punti che credo dobbiate sapere.




## Definizioni





- Le commissioni di accensione** sono spese una tantum applicate al momento della concessione del prestito e calcolate come percentuale dell'importo preso in prestito. Queste commissioni coprono i costi amministrativi, operativi e di gestione.





- La garanzia** è un bene che si deposita per garantire un prestito. Nel caso di Debifi, la garanzia è il Bitcoin (BTC), che il mutuatario deposita nel Multisig 3/4 escrow.





- Il sistema Multisig escrow (3/4)** è un meccanismo di deposito sicuro in cui i bitcoin del mutuatario vengono depositati in un indirizzo a firma multipla. Nello specifico, quattro (4) parti detengono ciascuna una chiave (mutuatario, prestatore, Debifi, terza parte indipendente). Per spostare i fondi, sono necessarie almeno 3 delle 4 firme.





- Una stablecoin** è una criptovaluta il cui valore è ancorato a un asset stabile (ad esempio il dollaro USA), evitando così la volatilità delle Bitcoin. Ad esempio, 1 USDC vale sempre ~1$, in quanto sostenuto da riserve fiat.





- Il rapporto Loan-to-Value (LTV)** di un prestito determina la quantità di contanti che potete prendere in prestito come garanzia per il vostro Bitcoin. Rapporto LTV = Importo del prestito / Importo della garanzia * 100. Ad esempio, un LTV del 50% significa che il valore del prestito è pari al 50% del valore del Bitcoin depositato.




Video tutorial sulle sessioni BTC :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Come iniziare con Debifi



Per iniziare a lavorare su Debifi, sono necessari alcuni prerequisiti.


### Prerequisiti



Prima di prendere in prestito da Debifi, assicuratevi di avere i seguenti elementi:





- Bitcoin wallet: dove detenete i vostri BTC (idealmente non custoditi, ad esempio Hardware Wallet o un wallet mobile fidato). È da questo wallet che invierete il collaterale Bitcoin a Debifi e riceverete il collaterale indietro.



È possibile utilizzare Aqua, un Bitcoin e Liquid wallet che supporta anche la gestione di USDT stablecoin su varie reti. Oppure COLDCARD (Mk4 o Q), attualmente l'unico hardware supportato da Debifi.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): a seconda dell'offerta di prestito scelta, potrebbe essere richiesto un processo di verifica dell'identità. Su Debifi, ogni offerta indica se il KYC è richiesto o meno. Preparatevi di conseguenza. Il KYC viene effettuato da fornitori di servizi terzi affidabili, come Sumsub.



![image](assets/fr/03.webp)





- Applicazione di autenticazione a due fattori: Debifi richiede un codice Authenticator per ogni azione importante. Si tratta di un ulteriore livello di sicurezza. In questa esercitazione utilizzeremo Google Authenticator. In alternativa, potete utilizzarne altri a vostro piacimento.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Sito web e applicazione mobile Debifi: Debifi è sia un sito web che un'applicazione mobile, e i due funzionano in tandem. L'applicazione mobile diventa un wallet, che memorizza la chiave privata e gestisce la firma dei contratti. Inoltre, è necessario utilizzare il sito web per impegnare i contratti (un grande Interface offre una visione generale dei contratti di prestito e delle loro specifiche).





- L'applicazione mobile Debifi (iOS/Android) è necessaria per sottoscrivere i prestiti. È necessario scaricare l'app, creare un account e "collegare" il dispositivo (registrando il dispositivo al proprio account). L'app Debifi supporta l'autenticazione a due fattori (2FA) e senza uno smartphone non è possibile confermare le transazioni su Debifi.



### Creare un account



Visitate [il sito ufficiale di Debifi](https://debifi.com/app).



![image](assets/fr/04.webp)



Installate l'applicazione in base al tipo di smartphone in vostro possesso, quindi apritela.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Una volta entrati nell'applicazione, fare clic sul menu **Impostazioni**.



![image](assets/fr/07.webp)



Cliccare quindi su **Accesso o creazione di un account** per creare un account con il proprio indirizzo e-mail.



![image](assets/fr/08.webp)



![image](assets/fr/09.webp)



![image](assets/fr/10.webp)



Riceverete un codice di verifica via e-mail. Copiate e incollate questo codice nell'applicazione. Aprite quindi l'applicazione Debifi sul vostro smartphone ed effettuate il login.



![image](assets/fr/11.webp)



### Protezione del conto



Per sicurezza, Debifi vi chiederà di seguire tre passaggi.



![image](assets/fr/12.webp)





- Per prima cosa, dovrete impostare un codice PIN forte per accedere alla vostra applicazione in un secondo momento.



![image](assets/fr/13.webp)





- Quindi, impostare l'autenticazione a due fattori (2FA) per associare il dispositivo al proprio account utilizzando il codice 2FA.



![image](assets/fr/14.webp)





- Infine, salvate le 12 parole della vostra chiave privata scrivendole su un supporto affidabile e conservandole in un luogo sicuro. Questa fase è essenziale per recuperare il vostro conto e gestire i vostri fondi.



![image](assets/fr/15.webp)





- Per una maggiore sicurezza, è possibile aggiungere anche un passphrase.



![image](assets/fr/16.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Si noti che solo lo smartphone registrato potrà aprire il conto (un'ulteriore misura di sicurezza).



Una volta completati questi passaggi, cliccate sul menu **Offerte** per visualizzare le offerte di prestito disponibili. Cliccando su un'offerta, si viene reindirizzati al sito web di Debifi.



![image](assets/fr/17.webp)



### Accedere al sito web ed esplorare le offerte di prestito



Una volta collegato il dispositivo, accedere al [sito web Debifi](https://debifi.com/). Effettuare il login per stabilire una connessione sicura tra l'applicazione mobile Debifi e la piattaforma web. In questo modo è più facile interagire con le offerte di prestito disponibili (una visione chiara dei dettagli di ciascuna offerta) e gestire il proprio conto.



![image](assets/fr/18.webp)



![image](assets/fr/19.webp)



![image](assets/fr/20.webp)



![image](assets/fr/21.webp)




Video tutorial su come accedere al proprio account sulla piattaforma:



![video](https://youtu.be/cUwCfTKDAOo)



## Richiesta di prestito



La piattaforma vi mette in contatto con liquidità di qualità istituzionale e offre una gamma di opzioni adatte alle vostre esigenze. Sfogliate la pagina per scoprire cosa è disponibile. Inoltre, avete la possibilità di regolare i parametri dei prestiti in base alla vostra tolleranza al rischio e alla vostra situazione finanziaria.



![image](assets/fr/22.webp)



Le valute fiat attualmente offerte da Debifi possono essere visualizzate sulla piattaforma.



![image](assets/fr/23.webp)



### Clausole contrattuali chiare e flessibili



Debifi si basa su condizioni di prestito trasparenti e flessibili per soddisfare le esigenze di ciascuna parte (mutuante e mutuatario). Le clausole chiave includono:



#### Rapporto prestito/valore (LTV)


Le tranche di prestito Bitcoin sono generalmente in numero di tre (3):





- Conservativo (30% - 40% LTV), che corrisponde a un prestito a basso rischio, è l'ideale per massimizzare la sicurezza contro la volatilità dei prezzi del Bitcoin;





- Bilanciato (50% LTV) ;





- Aggressiva (70% LTV), che offre una maggiore liquidità, ma comporta un rischio molto elevato di liquidazione durante le flessioni del mercato. La scelta di questa tranche richiede un monitoraggio attivo delle condizioni di mercato del Bitcoin.



#### Tassi di interesse



La determinazione dei tassi dipende generalmente dal LTV scelto, dalla durata del prestito, dalla volatilità delle garanzie e dalle valutazioni del rischio specifiche della piattaforma. I tassi rimangono fissi per tutta la durata del prestito.



#### Durata del prestito e flessibilità di rimborso



I piani di rimborso sono flessibili e pensati per soddisfare le esigenze del mutuatario. I prestiti possono essere rimborsati totalmente o parzialmente in qualsiasi momento senza spese aggiuntive, a condizione che i requisiti di garanzia rimangano soddisfatti. Per tutta la durata del prestito, gli interessi vengono pagati periodicamente, mentre il capitale viene saldato alla scadenza.



#### Diritti di liquidazione (Margin call)



Data la volatilità del Bitcoin, i prestiti includono una politica di margin call chiaramente definita. Una richiesta di margine si verifica quando l'LTV aumenta a causa di una diminuzione del valore della garanzia. Debifi avvisa il mutuatario via e-mail e tramite l'app, consentendogli di aggiungere garanzie o di rimborsare parte del prestito.


75% LTV - Primo avviso

80% LTV - Secondo avviso

85% LTV - Allarme finale

90% LTV - La garanzia collaterale viene liquidata



### Avvio del processo di prestito



Per selezionare l'offerta di prestito più adatta alle vostre esigenze, cliccate su di essa per visualizzarne le caratteristiche.



![image](assets/fr/24.webp)



Si può vedere :


1. Nome dell'istituto di credito ;


2. La gamma di importi del prestito;


3. Che riceverete i fondi in USDC Ethereum ;


4. La durata del prestito, il tasso di interesse e il rapporto LTV;


5. Per questa offerta è richiesto il KYC;


6. È necessario inserire l'importo esatto di cui si ha bisogno (l'importo deve rientrare nella fascia, vedi punto 2);


7. È necessario inserire l'indirizzo USDC di Ethereum da utilizzare per ricevere i fondi.



Una volta accettata l'offerta e compilate le informazioni necessarie, cliccate su "Richiesta Contract".



![image](assets/fr/25.webp)



Tornate all'applicazione mobile per ''**fornire la chiave pubblica**''.



![image](assets/fr/26.webp)



Premere ''**Fornisci chiave pubblica**'', quindi scegliere la fonte della chiave pubblica. Anche il prestatore dovrà fornire una chiave pubblica.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Il passo successivo è la firma del contratto. Sempre nell'applicazione mobile, premere ''**Firma Contract**''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Al termine della firma del contratto, Debifi crea automaticamente un indirizzo Bitcoin multi-firma unico (escrow 3-sur-4) per il contratto. Finché i bitcoin sono nell'escrow, non possono essere utilizzati altrove.



### Deposito della garanzia e ricezione dei fondi



Il passo finale consiste nel depositare la garanzia Bitcoin nel sistema di deposito a garanzia multi-firma. Debifi indica l'indirizzo del deposito (B) e la quantità di BTC (A) da inviare come (garanzia + commissione).



![image](assets/fr/33.webp)



Riceverete questa notifica anche nella vostra applicazione mobile.



![image](assets/fr/34.webp)



Non appena il deposito viene confermato, il prestatore versa l'importo del prestito all'indirizzo di ricezione indicato, finalizzando la transazione e dandovi accesso ai fondi di cui avete bisogno.



Riceverete quindi una notifica da Debifi, che vi chiederà di pagare le spese o le commissioni del prestito per far progredire lo stato del vostro prestito.



In realtà, una volta creato il contratto, le spese del prestito vengono automaticamente detratte dalla garanzia depositata dal mutuatario nell'indirizzo di deposito multi-firma.



È sufficiente firmare una transazione che permetta a Debifi di detrarre la sua commissione dalla garanzia. Da parte sua, anche il vostro finanziatore dovrà firmare la transazione di deduzione della commissione, altrimenti Debifi non potrà ricevere la sua commissione.



![image](assets/fr/35.webp)



Le commissioni di prestito applicabili sono dell'1,5-2%, a seconda della durata del contratto. La piattaforma addebita le commissioni solo in Bitcoin.



## Tracciabilità del prestito



Una volta che il prestito è attivo, Debifi permette di seguire il contratto in tempo reale. Nell'interfaccia, troverete:



- L'importo preso in prestito e la durata residua.
- L'attuale rapporto LTV (Loan-to-Value), che aumenta quando il prezzo del BTC diminuisce e il valore della garanzia collaterale si riduce.




I mutuatari vengono avvisati quando il valore della garanzia diminuisce e questa informazione viene visualizzata anche nella pagina di riepilogo del contratto. Per ripristinare il rapporto prestito/valore originale, il mutuatario deve:



- depositare ulteriori garanzie;
- rimborsare tutto o parte del debito.




In caso di aumento del prezzo della garanzia, il mutuatario conserva le eventuali plusvalenze sulla garanzia. Egli deve solo l'importo del prestito, che è predeterminato e indipendente dal prezzo del Bitcoin.




## Rimborso e recupero della garanzia



Alla fine del periodo concordato (o prima, se lo desiderate), dovrete rimborsare il prestito.


In Debifi :





- Accedere al proprio contratto e cliccare su **Eseguire un rimborso**. Inserite l'importo totale dovuto (capitale + interessi).





- Inviate le stablecoin del vostro wallet all'indirizzo del prestatore indicato e tornate a confermare il rimborso sulla piattaforma copiando l'**ID** della transazione di rimborso nella scheda dedicata. In questo modo Debifi potrà effettuare più facilmente i suoi controlli.



Una volta che il pagamento è stato confermato dal prestatore (e da voi), Debifi vi chiederà di effettuare un **rimborso**. La garanzia Bitcoin viene svincolata ed è possibile restituirla dal deposito a garanzia alla propria wallet.  Non dimenticate di raccogliere tutti i vostri Bitcoin.



Non appena si ricevono i bitcoin, il contratto di prestito cambia in **Contract completato**.



Congratulazioni! Avete concluso il processo.




## Migliori pratiche e sicurezza



Qualunque siano i vostri obiettivi o le vostre motivazioni - finanziare un progetto, acquistare una proprietà, comprare bitcoin, ecc... - prestate molta cautela prima di sottoscrivere un prestito sostenuto dal Bitcoin. Prendetevi il tempo necessario per valutare attentamente la vostra decisione, poiché il Bitcoin rimane un asset volatile. **Un forte calo del suo prezzo potrebbe comportare la liquidazione forzata dei vostri bitcoin



Monitorare il rapporto prestito/collaterale (LTV). Se possibile, impostate degli avvisi (prezzo BTC, LTV). Non lasciate che il vostro rapporto si avvicini al 90%. In caso di dubbio, aumentate le garanzie o rimborsate anticipatamente.



Controllare le chiavi. Conservate il vostro BTC in un wallet sicuro (idealmente un hardware o un wallet affidabile). Non impostate un codice PIN legato a una data importante della vostra vita e non condividete mai la vostra frase di recupero. Su Debifi, la chiave privata è generate nell'applicazione e Debifi non la conosce.



Se possibile, iniziate con poco. Per il vostro primo prestito, provate un importo modesto per familiarizzare con il processo.



Utilizzate solo il sito ufficiale di Debifi per essere aggiornati sulle novità di Debifi ed evitate link sconosciuti o di phishing.  Aggiornate l'applicazione, proteggete il vostro smartphone con un codice PIN e scegliete un Hardware Wallet compatibile.



In alternativa, se siete un prestatore, questo video tutorial vi guiderà nell'utilizzo della piattaforma Debifi. Dalla selezione dei mutuatari interessati alla vostra offerta, alla fornitura delle chiavi pubbliche, alla firma degli accordi, al trasferimento di stablecoin e altro ancora.



![video](https://youtu.be/g8iLxwI4xT0)



Ora sapete come utilizzare la piattaforma Debifi per ottenere un prestito.



Vi consiglio di seguire questo corso, che analizza in modo approfondito il Bitcoin, le monete stabili e il loro contributo alla sovranità.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46
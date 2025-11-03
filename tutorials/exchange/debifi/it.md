---
name: Debifi
description: Ottenere un prestito non detentivo garantito da Bitcoin.
---

![cover](assets/cover.webp)




## Introduzione



Per secoli, il credito tradizionale ha permesso di finanziare molti progetti. Tuttavia, rimane lento, costoso e poco inclusivo, soprattutto per coloro che non hanno accesso a una solida infrastruttura bancaria.



L'ascesa del protocollo Bitcoin ha inaugurato una nuova era finanziaria, portando con sé una serie di sfide. Una di queste sfide era come ottenere liquidità senza essere costretti a vendere il Bitcoin, perdendo così l'esposizione al suo potenziale di crescita



Il risultato è **Debifi**, una piattaforma che si pone come moderna alternativa alle banche. L'obiettivo è chiaro: rendere il credito il più semplice e trasparente possibile, combinando i vantaggi del sistema finanziario tradizionale con la libertà offerta da Bitcoin. Il nome Debifi riflette questa visione: ***Finanza decentralizzata Bitcoin***, una contrazione che illustra l'incontro tra finanza decentralizzata e innovazione Bitcoin.



Debifi è una piattaforma di prestito non custodiale con supporto Bitcoin, il che significa che l'utente mantiene il controllo delle proprie chiavi private. Consente agli utenti di sbloccare liquidità in Exchange per i loro bitcoin bloccati come garanzia. A differenza dei prestiti bancari tradizionali, Debifi utilizza un sistema di deposito a garanzia con più firme (3 su 4) e non accetta garanzie ipotecarie, garantendo maggiore sicurezza e trasparenza.



In pratica, ciò significa che né Debifi né un singolo prestatore possono spendere i vostri BTC senza l'accordo di tre parti (voi, il prestatore e una terza parte fidata). Questo rende il sistema più sicuro: se prendete un prestito su Debifi, conservate il Ownership del vostro Bitcoin fino al completo rimborso del prestito.



## Vantaggi di Debifi



Con Debifi, si tratta di prestiti garantiti, sicurezza Blockchain (firma multipla, 2FA), scelta di monete stabili/liquidi, riservatezza e controllo Bitcoin totale. Debifi "vi permette di tenere i vostri soldi" (le vostre chiavi, le vostre monete), offrendo al contempo tassi competitivi e un accesso globale ai prestiti garantiti da BTC.



Ecco un rapido confronto tra un prestito Debifi e un prestito bancario tradizionale:



| Caractéristiques       | Prêt via Debifi                                                       | Prêt bancaire traditionnel                                                 |
| ---------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Accessibilité          | ✔️ Ouvert à tout détenteur de Bitcoin (même sans historique bancaire) | ❌ Souvent réservé aux clients avec garanties physiques et dossiers solides |
| Vitesse d’obtention    | ✔️ Liquide en quelques minutes/heures                                 | ❌ Processus long (jours ou semaines)                                       |
| Garanties exigées      | ✔️ Collatéral en Bitcoin uniquement                                   | ❌ Garanties physiques (maisons, terrains, revenus stables)                 |
| Contrôle de l’actif    | ✔️ Vous conservez l’exposition au Bitcoin et son potentiel de hausse  | ❌ Vous n’avez aucun lien entre le prêt et vos actifs financiers            |
| Souplesse géographique | ✔️ Disponible partout (sans contrainte géographique bancaire)         | ❌ Limité à la juridiction de la banque                                     |
| Risque principal       | ❌ Risque de liquidation si le prix du BTC chute trop                  | ❌ Risque de saisie de biens ou impact négatif sur la cote de crédit        |

Prima di mostrarvi passo dopo passo come ottenere un prestito su Debifi, ci sono alcuni punti che credo dobbiate sapere.




## Definizioni





- Le commissioni di accensione** sono spese una tantum applicate al momento della concessione del prestito e calcolate come percentuale dell'importo preso in prestito. Queste commissioni coprono i costi amministrativi, operativi e di gestione.





- La garanzia** è un bene che si deposita per garantire un prestito. Nel caso di Debifi, la garanzia è il Bitcoin (BTC), che il mutuatario deposita nel Multisig 3/4 escrow.





- Il sistema Multisig escrow (3/4)** è un meccanismo di deposito sicuro in cui i bitcoin del mutuatario sono inseriti in un Address a firma multipla. Nello specifico, quattro (4) parti detengono ciascuna una chiave (mutuatario, prestatore, Debifi, terza parte indipendente). Per spostare i fondi, sono necessarie almeno 3 delle 4 firme.





- Una stablecoin** è una criptovaluta il cui valore è ancorato a un asset stabile (ad esempio, il dollaro USA), evitando così la volatilità del Bitcoin. Ad esempio, 1 USDC vale sempre ~1$, in quanto sostenuto da riserve fiat.





- Il rapporto Loan-to-Value (LTV)** di un prestito determina la quantità di contanti che potete prendere in prestito come garanzia per il vostro Bitcoin. Rapporto LTV = Importo del prestito / Importo della garanzia * 100. Ad esempio, un LTV del 50% significa che il valore del prestito è pari al 50% del valore del Bitcoin depositato.




Video tutorial sulle sessioni BTC :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Come iniziare con Debifi



Per iniziare a lavorare su Debifi, sono necessari alcuni prerequisiti.


### Prerequisiti



Prima di prendere in prestito da Debifi, assicuratevi di avere i seguenti elementi:





- Bitcoin Wallet: dove detenete i vostri BTC (idealmente non custoditi, ad esempio Hardware Wallet o un Wallet mobile fidato). È da questo Wallet che invierete la garanzia Bitcoin a Debifi e riceverete i fondi.





- Stablecoins o fiat: Debifi presta in monete stabili e in alcune valute fiat. Le principali monete stabili utilizzate sono USDT e USDC.



È possibile utilizzare Aqua, un Bitcoin e Liquid Wallet che supporta anche la gestione di USDT stablecoin su varie reti. Oppure la COLDCARD (Mk4 o Q), attualmente l'unico hardware supportato da Debifi.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): a seconda dell'offerta di prestito scelta, potrebbe essere richiesto un processo di verifica dell'identità. Su Debifi, ogni offerta indica se il KYC è richiesto o meno. Preparatevi di conseguenza. Il KYC viene effettuato da fornitori di servizi terzi affidabili, come Sumsub.



![image](assets/fr/03.webp)





- Applicazione di autenticazione a due fattori: Debifi richiede un codice Authenticator per ogni azione importante. Si tratta di un ulteriore Layer di sicurezza. In questa guida utilizzeremo Google Authenticator. In alternativa, potete utilizzarne altri a vostro piacimento.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Sito web e applicazione mobile Debifi: Debifi è sia un sito web che un'applicazione mobile, e i due funzionano in tandem. L'applicazione mobile diventa un Wallet, che memorizza la chiave privata e gestisce la firma dei contratti. Inoltre, è necessario utilizzare il sito web per impegnare i contratti (un grande Interface offre una visione generale dei contratti di prestito e delle loro specifiche).





- L'applicazione mobile Debifi (iOS/Android) è necessaria per sottoscrivere i prestiti. È necessario scaricare l'app, creare un account e "collegare" il dispositivo (registrando il dispositivo al proprio account). L'app Debifi supporta l'autenticazione a due fattori (2FA) e senza uno smartphone non è possibile confermare le transazioni su Debifi.



### Creare un account



Visitate [il sito ufficiale di Debifi](https://debifi.com/app).



![image](assets/fr/04.webp)



Installate l'applicazione in base al tipo di smartphone in vostro possesso, quindi apritela.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Una volta entrati nell'applicazione, fare clic sul menu **Impostazioni**.



![image](assets/fr/07.webp)



Cliccare quindi su **Login o crea account** per creare un account con il proprio indirizzo e-mail Address.



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





- Per una maggiore sicurezza, si può anche aggiungere un passphrase.



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





- Conservativo (20% - 40% LTV), che corrisponde a un prestito a basso rischio, è ideale per massimizzare la sicurezza contro la volatilità dei prezzi del Bitcoin;





- Bilanciato (50% LTV) ;





- Aggressiva (70% - 85% LTV), che offre una maggiore liquidità, ma comporta un rischio molto elevato di liquidazione durante le flessioni del mercato. La scelta di questa tranche richiede un monitoraggio attivo delle condizioni del mercato Bitcoin.



#### Tassi di interesse



La determinazione dei tassi dipende generalmente dal LTV scelto, dalla durata del prestito, dalla volatilità delle garanzie e dalle valutazioni del rischio specifiche della piattaforma. I tassi rimangono fissi per tutta la durata del prestito.



#### Durata del prestito e flessibilità di rimborso



I piani di rimborso dei prestiti sono spesso flessibili e adattati alle esigenze dell'utente. I pagamenti possono essere effettuati in qualsiasi momento, purché siano soddisfatti i requisiti di garanzia. I pagamenti dei prestiti sono generalmente costituiti da interessi per la durata del prestito, mentre il capitale è dovuto alla scadenza.



#### Diritti di liquidazione (Margin call)



Poiché il prezzo del Bitcoin è volatile, un prestito responsabile include nel contratto specifiche politiche di margin call. Questa politica consente al mutuatario di essere avvisato di fornire ulteriori garanzie o di rimborsare una parte del prestito.



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


7. È necessario inserire l'Ethereum USDC Address da utilizzare per ricevere i fondi.



Una volta soddisfatti dell'offerta e dopo aver compilato le informazioni necessarie, cliccate su "Richiesta Contract".



![image](assets/fr/25.webp)



Tornate all'applicazione mobile per ''**fornire la chiave pubblica**''.



![image](assets/fr/26.webp)



Premere ''**Fornisci chiave pubblica**'', quindi scegliere la fonte della chiave pubblica. Anche il prestatore dovrà fornire una chiave pubblica.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Il passo successivo è quello di firmare il Contract. Sempre nell'applicazione mobile, premere ''**Firma Contract**''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Quando si finisce di firmare il Contract, Debifi crea automaticamente un Bitcoin Address multi-firma unico (escrow 3-sur-4) per il Contract. Finché i bitcoin sono nell'escrow, non possono essere utilizzati altrove.



### Deposito della garanzia e ricevimento dei vostri fondi



Il passo finale consiste nel depositare la garanzia Bitcoin nel sistema di deposito a garanzia multi-firma. Debifi mostra quindi il Address in garanzia (B) e la quantità di BTC (A) da inviare come (garanzia + commissione).



![image](assets/fr/33.webp)



Riceverete questa notifica anche nella vostra applicazione mobile.



![image](assets/fr/34.webp)



Non appena il deposito viene confermato, il prestatore versa l'importo del prestito al Address che avete indicato, finalizzando la transazione e dandovi accesso ai fondi di cui avete bisogno.



Riceverete quindi una notifica da Debifi, che vi chiederà di pagare le spese o le commissioni del prestito per far progredire lo stato del vostro prestito.



In realtà, una volta creato il Contract, le spese del prestito vengono automaticamente detratte dalla garanzia depositata dal mutuatario nell'escrow Address a più firme.



È sufficiente firmare una transazione che permetta a Debifi di detrarre la sua commissione dalla garanzia. Da parte sua, anche il vostro creditore dovrà firmare la transazione di deduzione della commissione, altrimenti Debifi non potrà ricevere la sua commissione.



![image](assets/fr/35.webp)



Le commissioni di prestito applicabili sono dell'1,5-2%, a seconda della durata del Contract. La piattaforma applica commissioni solo per il Bitcoin.



## Tracciabilità del prestito



Una volta avviato il prestito, Debifi consente di monitorare il Contract in tempo reale. In Interface, vedrete :





- L'importo preso in prestito e la durata residua.
- Rapporto LTV (Loan-to-Value) attuale: Il LTV aumenta se il prezzo del BTC diminuisce (poiché la garanzia reale vale meno). Viene fissata una soglia di allarme (generalmente il 90%). Se il vostro LTV supera questa soglia, c'è il rischio di una liquidazione forzata. Debifi vi darà 24 ore di tempo per reagire.



I mutuatari saranno informati della riduzione del prezzo. Queste informazioni saranno disponibili anche nella pagina di riepilogo del Contract. Per ripristinare il rapporto prestito/valore originale di un prestito, il mutuatario deve :





- o depositare una garanzia supplementare ;
- rimborsare tutto o parte del debito.



In caso di aumento del prezzo della garanzia, il mutuatario conserva le eventuali plusvalenze sulla garanzia. Egli deve solo l'importo del prestito, che è predeterminato e indipendente dal prezzo del Bitcoin .




## Rimborso e recupero della garanzia



Alla fine del periodo concordato (o prima, se lo desiderate), dovrete rimborsare il prestito.


In Debifi :





- Andate sul vostro Contract e cliccate su **Eseguire un rimborso**. Inserite l'importo totale dovuto (capitale + interessi).





- Inviate le stablecoin dal vostro Wallet al Address indicato dal prestatore, e tornate a confermare il rimborso sulla piattaforma copiando l'**ID** della transazione di rimborso nella scheda dedicata. In questo modo Debifi potrà effettuare più facilmente i suoi controlli.



Una volta che il pagamento è stato confermato dal prestatore (e da voi), Debifi vi chiederà di effettuare un **rimborso**. La garanzia Bitcoin viene rilasciata e può essere restituita dal deposito a garanzia al proprio portafoglio.  Non dimenticate di raccogliere tutti i vostri Bitcoin.



Non appena si ricevono i bitcoin, il prestito Contract cambia in **Contract completato**.



Congratulazioni! Avete concluso il processo.




## Migliori pratiche e sicurezza



Qualunque siano i vostri obiettivi o le vostre motivazioni - finanziamento di un progetto, acquisto di una proprietà, acquisto di bitcoin, ecc. - siate estremamente cauti prima di sottoscrivere un prestito sostenuto da Bitcoin. - siate estremamente cauti prima di sottoscrivere un prestito garantito dal Bitcoin. Prendete tempo per valutare attentamente la vostra decisione, poiché il Bitcoin rimane un asset volatile. **Un forte calo del suo prezzo potrebbe comportare la liquidazione forzata dei vostri bitcoin**.



Monitorare il rapporto prestito/collaterale (LTV). Se possibile, impostate degli avvisi (prezzo BTC, LTV). Non lasciate che il vostro rapporto si avvicini al 90%. In caso di dubbio, aumentate le garanzie o rimborsate anticipatamente.



Controllare le chiavi. Conservate il vostro BTC in un Wallet sicuro (idealmente un hardware o un Wallet affidabile). Non impostate un codice PIN legato a una data importante della vostra vita e non condividete mai la vostra frase di recupero. Su Debifi, la vostra chiave privata è generate nell'applicazione - Debifi non la conosce.



Se possibile, iniziate con poco. Per il vostro primo prestito, provate un importo modesto per familiarizzare con il processo.



Utilizzate solo il sito ufficiale di Debifi per essere aggiornati sulle novità di Debifi ed evitate link sconosciuti o di phishing.  Aggiornate l'applicazione, proteggete il vostro smartphone con un codice PIN e scegliete un Hardware Wallet compatibile.



In alternativa, se siete un prestatore, questo video tutorial vi guiderà nell'utilizzo della piattaforma Debifi. Dalla selezione dei mutuatari interessati alla vostra offerta, alla fornitura delle chiavi pubbliche, alla firma degli accordi, al trasferimento di stablecoin e altro ancora.



![video](https://youtu.be/g8iLxwI4xT0)



Ora sapete come utilizzare la piattaforma Debifi per ottenere un prestito.



Vi consiglio di seguire questo corso che approfondisce il Bitcoin, le monete stabili e il loro contributo alla sovranità.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46
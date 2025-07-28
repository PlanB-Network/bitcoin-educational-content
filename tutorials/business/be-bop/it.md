---
name: be-BOP
description: Guida pratica alla monetizzazione della vostra attività con be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** è una piattaforma di e-commerce pensata per gli imprenditori che desiderano vendere online e offline, in completa autonomia, accettando pagamenti in Bitcoin, tramite conto bancario e in contanti. La soluzione è utile anche per qualsiasi tipo di organizzazione che desideri raccogliere donazioni o monetizzare le proprie attività.



La soluzione è semplice, leggera e autonoma. Permette di creare un negozio online, anche in un ambiente in cui i servizi finanziari tradizionali sono limitati o assenti. Infatti, **be-BOP** è stato progettato per operare in modo efficiente con o senza accesso alle banche, utilizzando il Bitcoin come infrastruttura di pagamento.



In questo tutorial, vi guideremo passo dopo passo attraverso :





- Create il vostro primo negozio online con **be-BOP**
- Personalizzate la vostra vetrina e i vostri prodotti
- Configurare i metodi di pagamento disponibili
- Comprendere le migliori pratiche per vendere online in modo efficace con **be-BOP**



Questo tutorial non richiede competenze tecniche avanzate. Si rivolge a sviluppatori, artigiani, commercianti, cooperative o imprenditori che desiderano intraprendere il commercio digitale in modo sovrano e resiliente.



## Prerequisiti per l'installazione di be-BOP sul proprio server



Prima di iniziare l'installazione di be-BOP, assicurarsi di disporre della seguente infrastruttura tecnica. Questi Elements sono essenziali per il corretto funzionamento della piattaforma:



### Archiviazione compatibile con S3



be-BOP utilizza un sistema di archiviazione per gestire i file (come le immagini dei prodotti). Ciò richiede l'accesso a un servizio S3, come :





- [MinIO](https://min.io/) in hosting autonomo
- Amazon S3 (AWS)
- Archiviazione a oggetti Scaleway



È necessario configurare un bucket e fornire le seguenti informazioni:





- S3_BUCKET**: nome del bucket
- S3_ENDPOINT_URL**: link di accesso al proprio servizio S3
- S3_KEY_ID** e S3_KEY_SECRET: i codici di accesso
- S3_REGION**: la regione del proprio servizio S3



### Database MongoDB in modalità ReplicaSet



be-BOP utilizza MongoDB per memorizzare i dati del negozio, degli utenti, dei prodotti e altri dati.



Avete due opzioni:





- Installare MongoDB in locale con la modalità **ReplicaSet abilitata**
- Utilizzare un servizio online come **Atlante MongoDB**



Sono necessarie le seguenti variabili:





- MONGODB_URL**: connessione al database Address
- MONGODB_DB**: nome del database



## Ambiente Node.js



be-BOP funziona con Node.js. Assicurarsi di avere **Node.js** versione 18 o superiore e **Corepack** abilitato (necessario per gestire i gestori di pacchetti come pnpm). Il comando da eseguire è `corepack enable`



### Git LFS installato



Alcune risorse (come le immagini di grandi dimensioni) sono gestite tramite Git LFS (Large File Storage). Assicurarsi di avere Git LFS installato sulla propria macchina con il comando `git lfs install`. Una volta soddisfatti questi prerequisiti, si è pronti a passare al passo successivo: scaricare e configurare be-BOP.



**Nota: ** Una guida tecnica alla distribuzione del software è disponibile in un'esercitazione separata.



## Creare un account Super-Admin



Al primo avvio di be-BOP viene creato un account **Super Admin**. Questo account dispone di tutte le autorizzazioni necessarie per gestire le funzioni di back-office. Per creare un account, seguire i seguenti passaggi:





- Andate a `il vostro sito web/admin/login`
- Creare un account di super-amministratore con un login e una password sicuri



Questo account vi darà accesso a tutte le funzioni di back-office. Una volta creato, è possibile accedere inserendo il nome utente e la password.



![login](assets/fr/001.webp)



## Configurazione e sicurezza del back office



Prima di configurare la connessione al back-office Interface, è necessario creare un Hash univoco. In questo modo ci si protegge da eventuali malintenzionati che cercano di rubare il link di connessione al proprio Interface admin.



Per creare il Hash, accedere a `/admin/Impostazioni`. Nella sezione dedicata alla sicurezza (ad esempio, "Admin Hash"), definire una stringa unica (Hash). Una volta registrato, l'URL del back-office verrà modificato (ad esempio `/admin-yourhash/login`) per limitare l'accesso alle persone non autorizzate.



![hash-login](assets/fr/002.webp)



2.2. Attivare la modalità di manutenzione (se necessario)



Sempre in /admin/Impostazioni, (Impostazioni > Generali tramite la grafica Interface) verificare l'opzione "abilita modalità di manutenzione" in fondo alla pagina.



![maintenance-mode](assets/fr/003.webp)



Se necessario, è possibile specificare un elenco di indirizzi IPv4 autorizzati (separati da virgole) per consentire l'accesso al front office durante la manutenzione. Il back office rimane accessibile agli amministratori.



![ip-bebop](assets/fr/004.webp)



## Impostazione delle comunicazioni



Per consentire a be-BOP di inviare notifiche (ad esempio per ordini, registrazioni o messaggi di sistema), è necessario configurare almeno un metodo di comunicazione. Sono disponibili due opzioni: e-mail (SMTP) o Nostr.



### Configurazione SMTP (e-mail)



be-BOP può inviare e-mail tramite un server SMTP. È necessario disporre di credenziali SMTP valide, spesso fornite da un servizio di posta elettronica (ad esempio, Mailgun, Gmail, ecc.).



Ecco cosa c'è da sapere:



SMTP_HOST: server SMTP Address (es. smtp.mailgun.org)



SMTP_PORT: la porta da utilizzare (spesso 587 o 465)



SMTP_USER: il nome utente (di solito un'e-mail Address)



SMTP_PASSWORD: la propria password o chiave API



SMTP_FROM: l'e-mail Address che comparirà come mittente




### Configurazione Nostr



be-BOP consente di inviare notifiche tramite il protocollo Nostr, un'infrastruttura di messaggistica decentralizzata. A tal fine, è necessario disporre di una chiave privata di Nostr (NSEC) generate o Supply. Questa chiave può essere generate direttamente tramite il Interface di be-BOP, nella sezione dedicata a Nostr. Quando questi Elements sono configurati correttamente, be-BOP sarà in grado di inviare automaticamente messaggi e avvisi ai vostri utenti.



## Metodi di pagamento compatibili



be-BOP è compatibile con diverse soluzioni di pagamento, consentendovi di offrire ai vostri clienti una maggiore flessibilità. Ecco cosa vi serve per impostare il metodo di pagamento più adatto a voi.



### Bitcoin Onchain



be-BOP consente di accettare pagamenti Bitcoin direttamente sul Blockchain (On-Chain), in modo semplice e sicuro.



**Fasi di configurazione:**





- Andare al menu **Impostazioni di pagamento**
- Fare clic su **Bitcoin Nodeless** per accedere ai parametri di pagamento On-Chain.
- Compilare i seguenti campi:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Suggerimento:** Per ottenere la chiave pubblica estesa (Zpub), è possibile consultare le impostazioni avanzate del proprio Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter, ecc.). Assicurarsi che il Wallet sia **non di sola lettura** se si intende utilizzare la cronologia delle transazioni.



### Lightning Network



be-BOP può anche accettare pagamenti istantanei Bitcoin grazie a Lightning Network. Attualmente sono disponibili due opzioni di configurazione:



**Phoenixd**



Andare al menu "Impostazioni di pagamento", cliccare su "Phoenixd"



![phoenixd](assets/fr/006.webp)



Dovrete quindi inserire **la password o l'autenticazione token** che vi connette alla vostra istanza di Phoenixd, un backend sviluppato da Acinq che vi permette di gestire i pagamenti Lightning con il vostro nodo, ma senza la complessità della gestione dei canali di pagamento.



**Swiss Bitcoin Pay**



Se non volete gestire un nodo Lightning da soli, **Swiss Bitcoin Pay** è una soluzione pronta all'uso e facile da configurare, ideale per iniziare ad accettare pagamenti Lightning senza un'infrastruttura complessa.



Fasi di configurazione :





- Nel menu "Impostazioni di pagamento", cliccare su "Swiss Bitcoin Pay"
- Accedete al vostro conto Swiss Bitcoin Pay (o createne uno se non ne avete già uno).
- Inserire la chiave API fornita da Swiss Bitcoin Pay, quindi fare clic su "Salva"



Una volta configurato, be-BOP emetterà automaticamente le fatture generate Lightning per i vostri clienti, e riceverete i pagamenti direttamente sul vostro conto Swiss Bitcoin Pay. Questa soluzione è ideale per gli utenti che vogliono evitare la complessità tecnica di un nodo personale, accettando al contempo pagamenti veloci e a basso costo.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Oltre a Bitcoin, be-BOP consente anche di accettare pagamenti in contanti tramite PayPal, una soluzione internazionale molto conosciuta e diffusa.



Fasi di configurazione :





- Andare al menu "Impostazioni di pagamento"
- Cliccare su `PayPal
- Nel vostro conto Paypal (sezione sviluppatori), inserite il `Client ID` e la `Secret`
- Selezionare la valuta desiderata (ad es. **USD**, **EUR**, **XOF**, ecc.)
- Fare clic su "Salva



![paypal](assets/fr/008.webp)



**Nota: ** Per ottenere questi identificatori è necessario disporre di un conto PayPal business. È possibile ottenerli tramite il portale [developer] (https://developer.paypal.com)



### SumUp



Il software integra ora la soluzione di pagamento **SumUp**, che consente di accettare pagamenti con carta di credito in modo semplice, sicuro ed efficiente. Per beneficiare di questa funzionalità, è necessaria una configurazione iniziale. Ecco i passi da seguire, numerati per un'implementazione chiara e progressiva:





- Iniziate inserendo la vostra **API Key**, una chiave riservata fornita da SumUp quando avete creato il vostro account di sviluppatore. Essa stabilisce una connessione sicura tra il vostro account SumUp e il software.
- Compilare il campo `Codice commerciante` con il codice univoco che identifica la vostra attività all'interno della piattaforma SumUp. Questo codice è essenziale per associare le transazioni alla vostra attività.
- Nel campo `Valuta`, scegliere la valuta principale utilizzata per le transazioni (ad esempio **EUR**, **USD**, **CDF**, ecc.).
- Una volta compilati correttamente tutti i campi, fare clic sul pulsante "Salva" per salvare le impostazioni. Il sistema stabilirà quindi il collegamento con il vostro account SumUp e il vostro software sarà pronto ad accettare i pagamenti.



![payment-sumup](assets/fr/009.webp)



Dopo questa configurazione, l'integrazione con **SumUp** sarà attiva e operativa, consentendo di incassare rapidamente e di tenere traccia delle transazioni direttamente dal software.



### Striscia



be-BOP offre anche un'integrazione completa con **Stripe**, una delle piattaforme di pagamento online più diffuse. Stripe consente di accettare pagamenti online tramite carta di credito, Wallet digitale e diversi altri metodi di pagamento. Ecco come attivarlo:





- Inserire la **chiave segreta** fornita nella dashboard di Stripe.
- Compilare il campo **chiave pubblica**, anch'esso fornito da Stripe.
- Selezionare la **valuta principale**.
- Salvare la configurazione, quindi fare clic su "Salva".



![payment-stripe](assets/fr/010.webp)



⚠️ **Attenzione:** È essenziale conoscere il regime IVA applicabile alla propria attività (ad esempio: vendita con IVA nel paese del venditore, esenzione giustificata o vendita all'aliquota IVA del paese dell'acquirente) per configurare correttamente le opzioni di fatturazione in **be-BOP**.



## Configurazione della valuta



**be-BOP** offre una gestione avanzata delle valute e si adatta ad ambienti multivaluta e a requisiti contabili specifici. Per garantire la coerenza delle operazioni finanziarie e dei rapporti, è essenziale configurare correttamente le diverse valute utilizzate nel sistema. Ecco i passi da seguire per questa configurazione:





- Selezionare la **valuta principale** (`Main currency`)
- Selezionare `Valuta secondaria
- Definire la **valuta di riferimento** (`valuta di riferimento del prezzo`)
- Indicare "Valuta di contabilità



Una volta configurate correttamente tutte le valute, il software assicura una conversione automatica e accurata delle transazioni in più valute, mantenendo una rigorosa coerenza contabile.



![settings-currencies](assets/fr/011.webp)



## Configurazione dell'accesso di recupero via e-mail o Nostr



Sempre in `/admin/settings', tramite il modulo **ARM**, assicurarsi che l'account di superamministratore includa un **email Address** o un **recovery pub**, facilitando così la procedura se si dimentica la password.



![settings-users](assets/fr/012.webp)



## Impostazioni della lingua



Il software offre una funzionalità multilingue per adattarsi a un pubblico internazionale e migliorare l'esperienza dell'utente. Per attivare la funzionalità multilingue, è importante configurare le lingue disponibili e definire una **lingua predefinita**.



![settings-languages](assets/fr/13.webp)



## Interface e configurazione dell'identità in be-BOP



**be-BOP** fornisce ai designer tutti gli strumenti necessari per progettare un sito web. Il primo passo è aprire la sezione `Admin > Merch > Layout` nelle impostazioni. Iniziare a configurare la **barra superiore**, la **barra di navigazione** e il **piatto inferiore**.



### Le Top Bar



La configurazione **Top Bar** consente di personalizzare l'identità visiva del software visualizzando le informazioni chiave fin dalla prima riga del Interface. Questo rafforza il riconoscimento del marchio e fornisce un contesto chiaro agli utenti. Questo rafforza il riconoscimento del marchio e fornisce un contesto chiaro agli utenti.



#### Fasi di configurazione :





- Nel campo `Brand name`, inserire il nome della propria azienda, organizzazione o prodotto. Questo nome apparirà nella parte superiore del Interface e rappresenterà la vostra principale identità visiva.
- Indicare il titolo del sito**: il titolo scelto deve riassumere lo scopo della piattaforma. Questo titolo può apparire nell'intestazione o nella scheda del browser.
- Aggiungi descrizione del sito web**: qui si inserisce una breve descrizione dell'iniziativa. Questa descrizione aiuta a contestualizzare lo strumento per gli utenti e può essere utilizzata anche a fini SEO.



Una volta inserite queste informazioni, la **Barra superiore** mostrerà una presentazione chiara, professionale e coerente della vostra soluzione.



#### Collegamenti nella barra superiore



La sezione `Links` della barra superiore consente di aggiungere collegamenti a pagine importanti della vostra applicazione o a siti esterni. Questi collegamenti vengono visualizzati direttamente nella barra superiore, offrendo agli utenti un accesso rapido e strutturato.



#### Fasi di configurazione :





- Inserire il nome del collegamento (testo)**: nel campo `Testo`, inserire il nome o l'etichetta del collegamento così come apparirà (ad esempio, Home, Contatti, Aiuto...).
- Indicare il link Address (Url)**: nel campo `Url`, inserire il Address completo della pagina di destinazione (interna o esterna).
- Aggiungere altri collegamenti, se necessario**: ogni riga di configurazione consente di aggiungere un collegamento supplementare utilizzando i campi `Text` e `Url`.
- Salva i link**: una volta inseriti tutti i link, fare clic sul pulsante "Aggiungi link alla barra superiore" per salvarli.



Questa configurazione vi permette di offrire una navigazione chiara, fluida e accessibile attraverso le diverse sezioni del vostro sito web o verso risorse complementari.



![settings-topbar](assets/fr/014.webp)



### Bar La Nav



La sezione **Barra di navigazione** consente di configurare il menu di navigazione principale di be-BOP, solitamente situato sul lato o sulla parte superiore del Interface. Questo menu guida gli utenti alle varie pagine e funzioni dell'applicazione. Questo menu guida gli utenti alle varie pagine e funzioni dell'applicazione. La configurazione dei collegamenti è semplice e intuitiva. Ecco come funziona:





- Inserire il nome del link (`Text`)**: nella riga di configurazione, iniziare a compilare il campo `Text`. Questo corrisponde al nome del collegamento visualizzato nella barra di navigazione (esempi: *Dashboard*, *Utenti*, *Impostazioni*...).
- Inserire il Address del link (`Url`)**: accanto al campo `Text`, si trova il campo `Url`. In questo campo, inserire il Address della pagina a cui il link deve reindirizzare. Può trattarsi di un percorso interno o di un link a una pagina esterna.
- Aggiungere più collegamenti, se necessario**: sotto la prima riga, i nuovi campi `Text` e `Url` sono disponibili per aggiungere tutti i collegamenti necessari. Ogni riga rappresenta un link di navigazione aggiuntivo.
- Salva link**: una volta inseriti tutti i Elements, fare clic sul pulsante `Aggiungi link alla barra di navigazione` per salvare e visualizzare i risultati nella barra di navigazione.



Questa configurazione consente di strutturare in modo efficiente l'accesso alle diverse parti del software, migliorando l'ergonomia e l'esperienza dell'utente.



![navbar](assets/fr/015.webp)



### Il piè di pagina



La sezione **Footer** consente di personalizzare il piè di pagina del software, aggiungendo informazioni o collegamenti utili. Prima di configurare i collegamenti, è necessario attivare un'opzione specifica:





- Abilita la visualizzazione dell'etichetta "Powered by be-BOP "**: attivare il pulsante `Visualizza Powered by be-BOP` per visualizzare questa etichetta nel piè di pagina.
- Inserire il nome del link (`Text`)**: compilare il campo `Text`, che corrisponde alla dicitura del link nel footer (esempi: *Terms*, *Privacy*, *Contact*...).
- Indicare il link Address (`Url`)**: nel campo `Url`, inserire il Address della pagina di destinazione (interna o esterna).
- Aggiungere altri collegamenti se necessario**: utilizzare le righe aggiuntive per creare tutti i collegamenti desiderati.
- Salva link**: fare clic sul pulsante "Aggiungi link a piè di pagina" per salvare i link.



![footer](assets/fr/016.webp)



### Personalizzazione visiva



**⚠️ Non dimenticate di impostare i loghi per i temi chiari e scuri, così come la favicon, tramite** `Admin > Merch > Pictures`.



Ecco come personalizzare l'aspetto del sito:



#### Vai alla sezione Immagini



Menu `Admin` > `Merch` > `Immagini`.



#### Aggiungere una nuova immagine



Fare clic su "Nuova immagine".



#### Selezionare un file locale



Fare clic su "Scegli file", quindi selezionare un'immagine dal disco Hard.



#### Selezionare il file da importare



Fare doppio clic sull'immagine da importare (logo chiaro, logo scuro o favicon).



#### Denominazione dell'immagine



Compilare il campo "Nome dell'immagine".



#### Aggiungi immagine



Fare clic su "Aggiungi" per finalizzare l'importazione.



![pictures](assets/fr/017.webp)



### Impostazione dell'identità del venditore



#### Impostazioni dell'identità



Accessibile tramite `Admin > Identità` (o `Impostazioni > Identità`), questa sezione consente di configurare le informazioni amministrative e legali dell'azienda.



#### Informazioni legali





- Ragione sociale**: nome ufficiale dell'azienda.
- Business ID**: identificativo legale o numero di registrazione (RCCM, SIRET...).



#### Business Address





- Via**: Address postale (via, numero...).
- Paese**: paese.
- Stato**: provincia o regione.
- Città**: città.
- CAP**: codice postale.



#### Informazioni di contatto





- Email**: email professionale Address.
- Telefono**: numero di telefono dell'azienda.



#### Conto corrente bancario





- Nome del titolare del conto**: nome del titolare del conto.
- Titolare del conto Address**: Address del titolare.
- IBAN**: Numero di conto bancario internazionale.
- BIC**: Codice SWIFT/BIC.



![bank-account](assets/fr/019.webp)



#### Fatturazione





- Cliccare su `Compilare con le informazioni principali del negozio` per precompilare i dati.
- Informazioni sull'emittente in alto a destra**: campo per le informazioni legali/fiscali visibili sulle fatture.
- Fare clic su "Aggiorna" per salvare le modifiche.



**Nota: ** è possibile inserire ulteriori informazioni da visualizzare sul Invoice, in base alle proprie esigenze.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Negozio fisico Address



Per chi ha un negozio fisico, aggiungere uno specifico Address completo in `Admin > Impostazioni > Identità` o in una sezione dedicata. In questo modo sarà possibile visualizzarlo sui documenti ufficiali e nel piè di pagina, se necessario.



![seller-id](assets/fr/021.webp)



## Gestione dei prodotti



### Creare un nuovo prodotto



Andare su `Admin > Merch > Products` per aggiungere o modificare un prodotto. Compilate i seguenti campi:



#### Informazioni di base





- Nome del prodotto**: nome del prodotto (ad es. *T-shirt BOP in edizione limitata*).
- Slug**: Identificatore URL senza spazi (ad esempio, `tshirt-bop-edition-limitee`).
- Alias** *(opzionale)*: utile per aggiungere rapidamente al carrello un campo dedicato.



![product-config](assets/fr/028.webp)



#### Prezzi





- Importo del prezzo**: prezzo del prodotto (ad esempio, `25,00`).
- Prezzo Valuta**: valuta (EUR, USD, BTC, ecc.).
- Prodotti speciali** :
  - questo è un prodotto gratuito.
  - questo è un prodotto a pagamento.



#### Opzioni di prodotto





- Prodotto singolo (`standalone`)**: è possibile una sola aggiunta per ordine (ad es. donazione, biglietto d'ingresso).
- Prodotto con variazioni** :
  - Non controllare "Standalone".
  - Controllare `Il prodotto presenta leggere variazioni (nessuna differenza di stock)`.
  - Aggiungi :
    - Nome** (ad es. *Dimensione*),
    - Valori** (ad esempio: S, M, L, XL),
    - Differenze di prezzo** se applicabili (ad esempio: `+2 USD` per XL).



![product-details](assets/fr/029.webp)



## Gestione delle scorte



### Opzioni avanzate per la creazione di un prodotto (stock, consegna, biglietti, ecc.)



#### Prodotto con scorte limitate



Se il prodotto non è disponibile in quantità illimitate, selezionare `Il prodotto ha uno stock limitato`. Questo attiva il monitoraggio automatico delle quantità rimanenti. Una volta selezionata questa casella, appare un campo che indica le **scorte disponibili**.



Il sistema gestisce :





- Scorte riservate** → prodotti in cestini non ancora pagati
- Stock venduto** → prodotti già acquistati



**Tempo di prenotazione del carrello**: Quando un cliente aggiunge un prodotto al suo carrello, questo viene "riservato" per un tempo limitato. È possibile modificare questo tempo in: `Admin > Config > Prenotazione carrello` (valore in minuti)



#### Prodotto da consegnare?



Selezionare `Il prodotto ha un componente fisico che sarà spedito al Address del cliente`. È utile per tutti i prodotti che devono essere inviati fisicamente (libri, magliette, ecc.)



#### Altre opzioni





- Ticket**: spuntare se il prodotto è un biglietto per un evento
- Prenotazione**: controlla se si tratta di uno slot di prenotazione (ad esempio: sessione, appuntamento)



![product-options](assets/fr/030.webp)



### Impostazioni dell'azione (in basso)



Questa sezione determina **dove** e **come** il prodotto può essere visualizzato e acquistato:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Selezionare solo i canali che si desidera utilizzare.



## Creazione e personalizzazione di pagine e widget del CMS



### Pagine CMS obbligatorie



Andare in `Admin > Merch > CMS`. Vedrete un elenco delle pagine esistenti e potrete aggiungerne di nuove con **Aggiungi pagina CMS**.



Le pagine CMS sono importanti per :





- Informare i visitatori (ad es. termini di utilizzo)
- Rispettare la legge (ad esempio, l'informativa sulla privacy)
- Spiegare alcune caratteristiche del negozio (ad es. raccolta IP, IVA 0%)



È possibile aggiungere altre pagine a seconda delle esigenze:





- Chi siamo / Chi siamo
- Sosteneteci / Donazioni
- FAQ
- Contatto
- ecc.



**Suggerimento: fare clic su ciascun link o icona per modificare il **contenuto**, il **titolo** o la **visibilità** di ciascuna pagina.



### Impaginazione e grafica Elements



Andare a : `Admin > Merch > Layout`. È possibile personalizzare il Elements visivo del sito:



![product-options](assets/fr/032.webp)



#### Top Bar





- Modificare o eliminare i link (EX: HOME, ABOUT US,...)
- Navigazione tra le sezioni chiave del sito



#### Navbar (barra di navigazione principale)





- Presente nell'area grigia sotto la barra superiore
- Contiene un accesso rapido a : `Config`, `Impostazioni di pagamento`, `Transazioni`, `Gestione dei nodi`, `Widget`, ecc.
- Solo per i direttori



#### Piè di pagina





- Modificabile da `Admin > Merch > Layout`
- Contiene: informazioni di contatto, link utili, avvisi legali....



#### Personalizzare le immagini



Vai a: `Admin > Merch > Immagini`



È possibile :





- Cambiare il **logo principale**
- Modificare o aggiungere il layout **immagini**



#### Descrizione del sito



Modificabile anche in `Immagini`, consente di visualizzare un **riassunto o uno slogan** nell'intestazione o nel piè di pagina, a seconda del tema.



**Nota: ** questo vi permette di adattare l'aspetto alla vostra identità di marca (educativa, commerciale o comunitaria).



### Integrare i widget nelle pagine del CMS



I widget** arricchiscono le pagine del CMS con Elements dinamici o visivi.



#### Creazione di widget



Andare a: `Admin > Widgets`



Esempi di widget disponibili:





- Sfide**: sfide o missioni
- Tag**: categorie o parole chiave
- Slider**: caroselli di immagini
- Specifiche** : Tabelle delle specifiche
- Moduli**: moduli (di contatto, di feedback, ecc.)
- Conto alla rovescia**: timer
- Gallerie**: gallerie di immagini
- Classifiche**: classifiche degli utenti



![widgets](assets/fr/033.webp)



#### Integrazione nelle pagine del CMS



Utilizzate gli **shortcode** nel contenuto delle vostre pagine CMS:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Parametri attuali** :





- `slug`: identificatore unico del widget
- `display=img-1`: immagine specifica del prodotto
- `width`, `height`, `fit`: dimensioni e stile dell'immagine
- autoplay=3000`: tempo in ms tra due diapositive



**Vantaggi** :





- Facile da inserire (copia e incolla)
- Dinamico: qualsiasi modifica al widget si riflette automaticamente
- Non è necessario uno sviluppatore



## Gestione degli ordini e reportistica



### Tracciabilità dell'ordine



Per visualizzare e gestire gli ordini passati, accedere a: `Admin > Transazione > Ordini`



Qui troverete l'**elenco completo degli ordini** effettuati sul vostro sito.



![orders](assets/fr/034.webp)



#### Visualizzazione e ricerca



Il Interface consente di cercare e filtrare gli ordini in base a diversi criteri:





- numero d'ordine: numero d'ordine
- alias prodotto: identificativo o nome del prodotto
- mezzo di pagamento": metodo di pagamento utilizzato (carta, criptovaluta, ecc.)
- `Email`: email del cliente



Questi filtri facilitano la ricerca rapida e la gestione mirata.



#### Dettagli di ogni ordine



Facendo clic su un ordine, è possibile accedere a un file completo contenente :





- Prodotti ordinati
- Informazioni per i clienti
- Consegna Address (se applicabile)
- Eventuali note associate all'ordine



#### Possibili azioni su un ordine



È possibile :





- Confermare l'ordine (se in sospeso)
- Annullare un ordine (in caso di problema o richiesta del cliente)
- Aggiungere **etichette** (per l'organizzazione interna)
- Consultare / aggiungere **note interne**



**Nota: ** questa sezione è essenziale per una buona logistica e per le relazioni con i clienti.



### Reporting ed esportazione



Per accedere alle statistiche di vendita e di pagamento :


amministratore > Impostazioni > Reporting



![reporting](assets/fr/035.webp)



Qui troverete una panoramica della vostra attività, sotto forma di **rapporti mensili e annuali**.



#### Contenuto del rapporto



I rapporti sono suddivisi in sezioni:





- Dettaglio ordine**: numero di ordini, stato (confermato, annullato, in sospeso), evoluzione
- Dettaglio prodotti**: prodotti venduti, quantità, prodotti popolari
- Dettaglio pagamenti**: importi incassati, suddivisi per metodo di pagamento



#### Esportazione dei dati



Ogni sezione comprende un pulsante **Esporta CSV**, che consente di :





- Scaricare i dati in formato CSV
- Aprirli in Excel, Google Sheets, ecc.
- Archiviazione per uso amministrativo o contabile
- Utilizzateli per i rapporti interni



**Nota: ** ideale per il monitoraggio delle prestazioni, la contabilità e le presentazioni.



## Configurazione di Nostr Messaging (opzionale)



![nostr-config](assets/fr/036.webp)



La piattaforma supporta il protocollo **Nostr** per alcune funzioni avanzate:





- Notifiche decentralizzate
- Accesso senza password
- Amministrazione leggera Interface



### Generazione e aggiunta della chiave privata Nostr



Vai a :


admin > Gestione dei nodi > Nostr





- Fare clic su **Create nsec** se non ne avete uno.
- Il sistema può generate automaticamente.
- In alternativa, è possibile utilizzare una chiave esistente (ad esempio di Damus o Amethyst).



Il prossimo:





- Copiare la chiave `nsec
- Aggiungerlo al file `.env.local` (o `.env`): ```env NOSTR_PRIVATE_KEY=TuoNsecIciKey



### Caratteristiche attivate con Nostr



Una volta configurate, sono disponibili diverse funzioni:



**Notifiche via Nostr**





- Invio di avvisi per ordini, pagamenti o eventi di sistema
- Per gli amministratori o gli utenti



**Amministrazione leggera Interface**





- Accessibile tramite un client Nostr
- Consente una gestione rapida e mobile



**Connessione senza password**





- Accesso tramite link sicuro (inviato tramite Nostr)
- Maggiore sicurezza e fluidità per gli utenti



## Personalizzazione del design e del tema



Per adattare l'aspetto del vostro negozio alla vostra carta grafica, andate su: `Admin > Merchandising > Tema`



Qui si trovano tutte le opzioni per **creare** e **configurare** un tema personalizzato.



### Creare un tema



![theme](assets/fr/037.webp)



Quando si crea o si modifica un tema, è possibile definire :





- Colori**: per pulsanti, sfondi, testo, link, ecc.
- Font**: scelta di caratteri tipografici per titoli, paragrafi, menu
- Stili grafici**: bordi, margini, spaziatura, forme a blocchi



### Sezioni personalizzabili



Ogni parte del sito può essere regolata in modo indipendente:





- Intestazione**: barra di navigazione superiore
- Corpo**: contenuto principale
- Piè di pagina** : fondo pagina



**Nota:** questa granularità assicura la coerenza tra le immagini del sito e l'identità del vostro marchio.



### Attivazione del tema



Una volta configurato il tema :





- Cliccare su **Salva**
- Attivatelo come **tema principale del negozio**



**Nota: ** il tema attivo è quello che sarà visibile ai visitatori.



## Configurazione dei modelli di e-mail



La piattaforma consente di personalizzare le e-mail inviate automaticamente agli utenti. Andare a: `Admin > Impostazioni > Modelli`



![emails-templates](assets/fr/038.webp)



### Creazione/modifica di modelli



Ogni e-mail (conferma dell'ordine, password dimenticata, ecc.) ha :





- Oggetto**: l'oggetto dell'e-mail (ad es. "L'ordine è stato convalidato")
- Corpo HTML**: Contenuto HTML visualizzato nell'e-mail



**Nota:** è possibile inserire testo, immagini, link, ecc. a seconda delle esigenze.



### Utilizzo di variabili dinamiche



Per rendere le e-mail dinamiche, inserire variabili come :





- `{numero d'ordine}}` : sostituito dal numero d'ordine effettivo
- `{fatturaLink}}` : collegamento al Invoice
- `{sitoLink}}`: URL del sito web



**Nota: ** questi tag vengono sostituiti automaticamente quando vengono inviati.



### Suggerimenti avanzati





- Creare email che siano **responsive** per facilitare la lettura su dispositivi mobili
- Aggiungere **pulsanti di azione** (pagamento, download, tracciamento dell'ordine)
- Testate le vostre e-mail inviandole a voi stessi prima della pubblicazione



## Configurazione di tag e widget specifici



### Gestione dei tag



I tag possono essere utilizzati per strutturare e arricchire i contenuti. Per accedervi: `Admin > Widget > Tag`



![tags-config](assets/fr/039.webp)



### Creazione di un tag



Compilare i seguenti campi:





- Nome tag**: nome del tag visualizzato
- Slug**: identificativo unico (senza spazi o accenti)
- Famiglia di tag**: raggruppa i tag per categoria



![targsconfig](assets/fr/040.webp)



#### Famiglie disponibili :





- creatori`: autori o produttori
- rivenditori: venditori o punti vendita
- `Temporale`: periodi o date
- eventi: eventi associati



### Campi opzionali



Questi campi possono essere utilizzati per arricchire un tag come se fosse una pagina di contenuto:





- Titolo
- Sottotitolo
- Contenuto breve**
- Contenuto completo** (in francese)
- CTA** (pulsanti di azione)



### Utilizzo dei tag



I tag possono essere :





- Assegnati ai prodotti
- Integrato nelle pagine CMS con un tag: [Tag=slug?display=var-1]



## Configurazione dei file scaricabili



Per offrire documenti scaricabili ai clienti: `Admin > Merch > Files`



### Aggiunta di un file



1. Fare clic su **Nuovo file**


2. Informare :




   - Nome del file** (ad es. *Guida all'installazione*)
   - File da caricare** (PDF, immagine, Word...)



**Nota:** una volta aggiunto, la piattaforma genera automaticamente un **collegamento permanente**.



### Utilizzando il link



Questo link può essere inserito in :





- Pagina CMS** (come link di testo o pulsante)
- Un **client di posta elettronica** (tramite un modello)
- Una **scheda del prodotto** (ad es. download del manuale)



È ideale per fornire *manuali d'uso, guide tecniche, schede prodotto...* senza la necessità di un hosting esterno.



## Nostr-bot



La piattaforma offre un'integrazione avanzata con il protocollo **Nostr**, attraverso un bot automatizzato.



Andare a: gestione dei nodi > Nostr



### Caratteristiche principali



#### Gestione dei relè





- Aggiungere o rimuovere i **relay** utilizzati dal bot
- Ottimizzare la **raggiunta** e la **affidabilità** dei messaggi inviati



#### Messaggio di presentazione automatica





- Attivare un messaggio automatico alla **prima interazione con l'utente**
- Ideale per :
  - Presentare il servizio
  - Inviare un link utile (ad es. FAQ, contatto, ordine)



#### Certificazione del vostro `npub





- Aggiungete un **logo** e un **nome pubblico**
- Link a un **dominio web verificato**
- Aumenta la credibilità e il riconoscimento della vostra identità Nostr



### Casi d'uso di Nostr-bot





- Invio di **conferme d'ordine** a voi
- Risposta automatica a **eventi (ad es. un nuovo ordine)**
- Creazione di una **interazione decentralizzata con i clienti**



## Sovraccarico delle etichette di traduzione



be-BOP è multilingue (FR, EN, ES...), ma potete adattare le traduzioni alle vostre esigenze.



Per farlo, andare a: `Impostazioni > Lingua`



### Caricamento e modifica



I file di traduzione sono in JSON. È possibile :





- Scarica** i file di lingua
- Modificare** i testi esistenti
- Aggiungere** le proprie traduzioni



Link ai file originali :


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Esempio: ** sostituire `Aggiungi al carrello` con `Ajouter au panier` o `Acheter`.



## Lavoro di squadra e punto vendita (POS)



### Gestione degli utenti e dei diritti di accesso



#### Creazione di ruoli



Andare a: `Admin > Impostazioni > ARM`



Fare clic su **Crea un ruolo** per creare un ruolo (ad esempio, `Super Admin`, `POS`, `Ticket checker`).



Ogni ruolo contiene :





- accesso in scrittura**: accesso in scrittura
- accesso in lettura**: accesso in lettura
- accesso vietato**: sezioni interdette



#### Creazione dell'utente



Nello stesso menu `Admin > Impostazioni > ARM`, aggiungere un utente con :





- accesso
- alias
- recupero della posta elettronica
- (opzionale) `recovery npub` per la connessione via Nostr



Assegnare un ruolo precedentemente definito.



![pos-users](assets/fr/045.webp)



Gli utenti di sola lettura** vedranno i menu in *italiano* e non potranno modificare i contenuti.



## Configurazione del punto vendita (POS)



### Assegnazione del ruolo di POS



Per dare a un utente l'accesso al POS, assegnare il ruolo `Punto vendita (POS)` in: `Admin > Config > ARM`



Può connettersi tramite l'URL sicuro: `/pos` o `/pos/touch`



### Caratteristiche specifiche del POS



Be-BOP offre un Interface dedicato alle vendite fisiche (negozio, evento, ecc.).



#### Aggiunta rapida tramite alias



In `/cart`, un campo consente di aggiungere un prodotto:





- Tramite la scansione di un **codice a barre** (ISBN, EAN13)
- Inserendo manualmente un **alias prodotto**



**Nota: ** il prodotto viene aggiunto automaticamente al carrello.



#### Mezzi di pagamento



Il POS supporta :





- Specie
- Carta di credito
- Lightning Network (crittografia)
- Altri in base alla configurazione



Sono disponibili due opzioni avanzate:





- Esenzione IVA** : applicabile su giustificazione (ONG, stranieri...)
- Sconto regalo**: sconto eccezionale con commento obbligatorio



#### Visualizzazione lato client



L'URL `/pos/sessione` è destinato a uno **schermo secondario** (HDMI, tablet...):



Poster:





- Prodotti in corso di realizzazione
- Importo totale
- Metodo di pagamento
- Sconti applicati



**Nota: ** il cliente segue l'ordine in diretta, mentre il venditore lo registra su `/pos`.



### Riepilogo POS



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Grazie per aver seguito con attenzione questa guida.
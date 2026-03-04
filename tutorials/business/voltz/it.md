---
name: Voltz
description: Il wallet Lightning tutto in uno per la tua azienda.
---

![cover](assets/cover.webp)

L'idea della piattaforma Voltz è nata da un gruppo di bitcoiner che volevano fornire il proprio servizio wallet Bitcoin. Il risultato è stato un'infrastruttura completa per l'accettazione di bitcoin al dettaglio. In questo tutorial, ti accompagniamo alla scoperta di Voltz e delle possibilità di integrazione di Bitcoin che la piattaforma offre.


## Come iniziare con Voltz

Oltre a essere un wallet Lightning custodial che consente di inviare, ricevere e pagare quotidianamente, Voltz è una piattaforma completa che fornisce numerose estensioni per integrare Bitcoin, come punto vendita (POS) o marketplace nella tua attività.

Vai sulla piattaforma [Voltz](https://www.lnvoltz.xyz/en) e crea un account facendo clic sul pulsante "Prova ora".

![voltz](assets/fr/01.webp)

![login](assets/fr/02.webp)

⚠️ È importante che tu imposta una password alfanumerica forte per aumentare le possibilità di contrastare gli attacchi brute-force, e verificare che tu ti trova effettivamente sul sito ufficiale di Voltz per inserire i dati di accesso per proteggersi dal phishing.

L'interfaccia di Voltz è molto simile a quella della piattaforma LnBits.

https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz è infatti costruito su di un server LnBits; dai un'occhiata al nostro tutorial per imparare a montare i tuoi server LnBits e a costruire le tue soluzioni su di essi.

https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

La piattaforma consente di gestire in modo efficiente più wallet. Per impostazione predefinita, quando ti iscrivi, disponi automaticamente di un wallet Lightning. Tuttavia, è possibile aggiungere altri wallet.

![wallets](assets/fr/03.webp)

### Portabilità

Voltz non si limita all'interfaccia web: nella sezione **Accesso mobile** è possibile collegare il wallet Voltz attivo, con applicazioni come Zeus o Blue Wallet.

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

A tal fine, è necessario installare e attivare l'estensione **LndHub** sulla piattaforma.

![lndhub](assets/fr/04.webp)

Seleziona il tuo wallet Voltz attivo e, a seconda dei diritti che desideri concedere, scansiona il codice QR appropriato.

- Il codice QR delle invoice consente solo di leggere lo storico del portafoglio e generare nuove invoice.
- Il codice QR dell'amministratore consente di visualizzare lo storico, le invoice generate e di pagare le invoice Lightning.

![qrs](assets/fr/05.webp)

In questa esercitazione colleghiamo il nostro wallet Voltz all'applicazione Blue Wallet.

![connect](assets/fr/06.webp)

Una volta collegato il nostro wallet, tutte le azioni effettuate saranno sincronizzate tra Blue Wallet e Voltz. Ad esempio, quando si effettua un'invoice con genera su Blue Wallet, si ha anche uno storico su Voltz.

![sync](assets/fr/07.webp)

Nella sezione **Configurazione del wallet** si trovano parametri minimali come la personalizzazione del nome del wallet e la valuta in cui si desidera ricevere i pagamenti.

![config](assets/fr/08.webp)

### Estensioni

Una delle caratteristiche peculiari della piattaforma Voltz è la sua modularità, che consente di attivare le estensioni necessarie. L'elenco delle estensioni si trova nel menu **Estensioni**.

![extensions](assets/fr/09.webp)

Tra queste estensioni c'è il TPoS, un terminale per il punto vendita che può essere utilizzato per tenere un inventario e riscuotere i pagamenti dai clienti.

![tpos](assets/fr/10.webp)

Dal terminale del punto vendita, è possibile:
- Ottenete una pagina web da condividere con i tuoi clienti e partner.
- Gestire l'inventario dei prodotti.
- Generare invoice Lightning.
- Pagamenti diretti tramite carte Bolt.

L'estensione è disponibile in versione gratuita e a pagamento per funzioni più avanzate. Per creare un terminale POS, fai clic sul pulsante **Apri** sotto il logo dell'estensione, quindi fai clic su **New POS**.

![new_tpos](assets/fr/11.webp)

Definisci il nome del tuo punto vendita, quindi collega il wallet Voltz al tuo terminale per incassare i pagamenti. È possibile attivare le mance selezionando la casella **Attiva mance**. Attiva anche l'opzione di stampa delle invoice se desideri rilasciare ricevute ai tuoi clienti (questa funzionalità è ancora in fase di sviluppo, quindi potrebbero verificarsi malfunzionamenti).

Il terminale del punto vendita include anche la configurazione delle imposte, quando desideri applicare le imposte del tuo paese direttamente ai prodotti.

![tpos](assets/fr/12.webp)

Una volta creato il tuo terminale POS, puoi aggiungere prodotti e servizi preconfigurati per garantire a te e ai tuoi clienti un'esperienza di pagamento e di contabilità senza problemi.

![product](assets/fr/13.webp)

Crea i tuoi prodotti definendo il loro nome, aggiungendo un'immagine e impostando un prezzo di vendita.  È possibile suddividere i prodotti in categorie per facilitarne il monitoraggio. È possibile applicare le imposte direttamente a un prodotto specifico. Se il prodotto non ha imposte applicate, l'imposta configurata in fase di creazione del terminale del punto vendita verrà applicata automaticamente.

![products](assets/fr/14.webp)

È possibile importare automaticamente l'elenco dei prodotti da un formato JSON facendo clic sul pulsante **Importa/Esporta**.

![exports](assets/fr/15.webp)

Accedi all'area di cassa tramite il link cliccando sull'icona **New Tab**, oppure condividi la tua piattaforma POS tramite codice QR con i tuoi clienti cliccando sull'icona **QR code**.

![lien](assets/fr/16.webp)

![qr](assets/fr/17.webp)

I tuoi clienti possono consultare il tuo catalogo ed effettuare il pagamento da questa interfaccia.

![pos](assets/fr/18.webp)

![chose](assets/fr/19.webp)

![pay](assets/fr/20.webp)

![checkout](assets/fr/21.webp)

Nel gruppo di estensioni disponibili, troverai anche strumenti come le estensioni **Invoice** e **Payment Link**, che ti permettono di generare invoice con prodotti specifici per raccogliere pagamenti isolati senza passare per il terminale POS.


## Tenere traccia dei pagamenti

Nel menu **Pagamenti**, Voltz offre una panoramica dei pagamenti ai vari wallet.

Puoi seguire i tuoi pagamenti da:
- Stato.
- L'etichetta: ad esempio **TPOS** per i pagamenti nei punti vendita e **lnhub** attraverso la connessione mobile nei wallet Zeus e Blue Wallet.
- Il wallet della collezione.
- Totale dei pagamenti in entrata e in uscita.
- Un periodo ben definito.

![payments](assets/fr/22.webp)


## Altre opzioni

Voltz è anche un'infrastruttura su cui è possibile costruire le proprie soluzioni. Nella sezione **Estensioni** troverai una guida allo sviluppo delle tue estensioni all'interno dell'ecosistema Voltz e LnBits.

![build](assets/fr/23.webp)

Nel caso in cui tu vogli sviluppare soluzioni al di fuori dell'ecosistema, ma utilizzando comunque la loro infrastruttura, nella sezione **URL del nodo** si trovano le chiavi API e le informazioni sulla documentazione con un esempio di cosa si può fare con questi dati.

Puoi creare invoice Lightning dalle tue applicazioni utilizzando il tuo wallet Voltz, pagare invoice Lightning, decodificare e verificare invoice.

![keys](assets/fr/24.webp)

Ora hai una buona conoscenza di Voltz. Se ti è piaciuto questo tutorial, siamo certi che imparerai di più sui metodi e gli strumenti migliori per integrare Bitcoin nella tua azienda con il nostro corso: Bitcoin per le aziende.

https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a

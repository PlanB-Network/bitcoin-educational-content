---
name: Breez - POS
description: Breez semplifica l'incasso dei pagamenti in bitcoin per la tua attività.
---

![cover](assets/cover.webp)

Dopo la pandemia COVID-19, i pagamenti digitali senza contatto si sono diffusi anche nei negozi più piccoli. In questo periodo, molte aziende hanno scoperto la praticità delle soluzioni bitcoin, che consentono di ricevere pagamenti da tutto il mondo. Tuttavia, queste soluzioni sono talvolta difficili da usare o inadatte alle piccole imprese. In questo tutorial vedremo il terminale di pagamento Breez, una soluzione che si distingue per la sua facilità d'uso e per il controllo totale della gestione dei bitcoin.


## Installare Breez POS

Breez POS è un servizio di self-custody fornito da Breez wallet. L'utilità di questo servizio è quella di consentire agli esercenti di riscuotere i pagamenti tramite Bitcoin rimanendo su un'interfaccia semplice, molto simile ai vari portafogli Lightning. Breez POS è disponibile sulle piattaforme di download [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) e [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS).

![download](assets/fr/01.webp)

![setup](assets/fr/12.webp)

⚠️ È importante notare che queste applicazioni sono ancora in fase di sviluppo e che potrebbero esserci degli errori nell'utilizzo delle funzionalità. Si consiglia un uso moderato.

Con questa applicazione, Breez ti offre il controllo completo sulle configurazioni della rete e sulle impostazioni delle commissioni, garantendoti la sovranità nella gestione dei tuoi bitcoin.

Puoi esplorare le varie opzioni di Breez wallet seguendo il nostro tutorial qui sotto. Questo passo ti aiuterà a comprendere meglio l'ecosistema del punto vendita e ad adottare le migliori pratiche per proteggere efficacemente i bitcoin associati al tuo seed.

https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Utilizzo di Breez POS

In questo tutorial ci concentreremo sulla sezione "_Punto vendita_" (Point of sales - POS) per aiutarti a capire come integrarlo come mezzo di pagamento nella tua attività.

Il punto vendita è parte integrante del portafoglio Breez e si basa principalmente su Lightning Network per la riscossione dei pagamenti.

Nel menu "_Punto vendita_" è disponibile un'interfaccia diretta per la riscossione dei pagamenti. È suddivisa in due parti:

### Addebito diretto

La prima parte è la tastiera di addebito diretto. Questa interfaccia è utile per riscuotere un pagamento completo quando si conosce il totale degli acquisti dei clienti, o quando non è necessario un catalogo fisso di prodotti nella propria attività (ad esempio, i servizi dei freelance).

![keyboard](assets/fr/02.webp)

Per utilizzare il POS Breez per la prima volta, è necessario raccogliere un pagamento di oltre 2.500 satoshis (circa 3 euro al cambio attuale). Questa somma, pagata solo al primo incasso, rappresenta il costo della creazione di un canale di pagamento per poter comunicare con altri nodi Lightning Network e inviare e ricevere satoshi.

![channel_fee](assets/fr/03.webp)

### Catalogo prodotti

La seconda parte è il catalogo dei prodotti. Questa interfaccia è ideale quando si dispone di un catalogo di prodotti con prezzi predefiniti. Qui è possibile preconfigurare i prodotti e poi utilizzarli per le fatture generate per migliorare la tracciabilità degli incassi.

![items](assets/fr/04.webp)

È possibile configurare manualmente ogni articolo da questa interfaccia, facendo clic sul pulsante "**Plus**" e definendo il nome, il prezzo e un identificatore per questo articolo.

![add_items](assets/fr/05.webp)

È quindi possibile aggiungerlo e definirne la quantità per riscuotere il pagamento associato.

Quando il tuo catalogo è piuttosto grande, può diventare complicato aggiungere i prodotti uno per uno. A questo scopo, nella sezione **Preferenze > Impostazioni del punto vendita**, dal menu "Elenco articoli", è possibile importare ed esportare automaticamente l'elenco degli articoli da file CSV.

![import](assets/fr/07.webp)

In questa stessa sezione è possibile definire il periodo di validità delle invoice Lightning. D'ora in poi, per tutte le tue invoice, i clienti avranno `N` secondi per effettuare il pagamento, altrimenti dovrai rigenerare una nuova invoice Lightning.

![invoice_time](assets/fr/08.webp)

In qualità di gestore, è possibile rafforzare la sicurezza dei bitcoin aggiungendo una password che sarà richiesta per tutti i pagamenti in uscita dal proprio wallet. Questa funzione è particolarmente utile quando non si è gli unici a gestire il proprio punto vendita.

![manager](assets/fr/09.webp)

Nel menu **Transazioni** si trova un elenco di tutti i pagamenti riscossi. È anche possibile filtrare i risultati su un periodo specifico facendo clic sul pulsante **Calendario**.

![transactions](assets/fr/10.webp)

È inoltre possibile visualizzare un riepilogo giornaliero delle vendite e dell'importo totale incassato facendo clic sul pulsante **Documento**.

![summary](assets/fr/11.webp)

Ora avete una conoscenza completa del punto vendita offerto dall'applicazione Breez per un'integrazione perfetta di Bitcoin nella tua attività. Se questa esercitazione ti è stata utile, ti consigliamo la nostra esercitazione su be-BOP, una piattaforma di e-commerce che ti permette di accettare pagamenti in bitcoin e monetizzare la tua attività.


https://planb.academy/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa

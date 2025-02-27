---
name: Portafoglio Proton
description: Installazione e utilizzo del portafoglio Proton Bitcoin
---
![cover](assets/cover.webp)

Proton è un'azienda svizzera specializzata in privacy digitale, fondata nel 2014 da scienziati del CERN. Nota per le sue soluzioni open source, Proton offre una suite di servizi tra cui Proton Mail, Proton VPN e Proton Drive.

Proton ha recentemente presentato Proton Wallet, un portafoglio Bitcoin open-source e autocustodito, disponibile come applicazione mobile o client web, collegato al proprio account Proton. Le funzionalità del portafoglio sono relativamente classiche per il momento, con gli strumenti essenziali che ci si aspetta da un buon portafoglio Bitcoin, come RBF (*Replace-By-Fee*), tagging o la possibilità di aggiungere una passphrase BIP39.

La particolarità di questo portafoglio è la possibilità di inviare bitcoin utilizzando l'indirizzo e-mail del destinatario, per il quale Proton genera automaticamente un indirizzo Bitcoin vuoto collegato al portafoglio dell'utente. Proton prevede di aggiungere nuove funzionalità in futuro, tra cui Lightning e coinjoin (probabilmente utilizzando Whirlpool, come suggerito dalle attività sul repository GitHub).

## Creare un account Proton

Per utilizzare Proton Wallet, è necessario disporre di un account Proton. Potete crearne uno gratuitamente seguendo i primi passi di questo tutorial dedicato alla creazione di una casella di posta elettronica Proton (solo la sezione "*Creazione di un account Proton*"). Una volta configurato l'account, si può proseguire con il resto del tutorial.

https://planb.network/tutorials/others/general/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
## Connettersi a Proton Wallet

Andate su [il sito web di Proton Wallet](https://proton.me/wallet) e cliccate sul pulsante "*Get Proton Wallet*".

![Image](assets/fr/01.webp)

Scegliere l'opzione di abbonamento "*gratuito*", quindi fare clic su "*Inscriviti*".

![Image](assets/fr/02.webp)

Per accedere, inserire l'e-mail e la password associate al proprio account Proton.

![Image](assets/fr/03.webp)

Il vostro conto dovrebbe ora essere visualizzato. Cliccate su "*Inizia a usare Proton Wallet ora*".

![Image](assets/fr/04.webp)

## Creare un portafoglio Bitcoin

Selezionate la valuta fiat predefinita per il vostro conto, quindi cliccate su "*Crea nuovo portafoglio*".

![Image](assets/fr/05.webp)

Il vostro portafoglio Bitcoin è stato creato. In teoria potete iniziare a usarlo immediatamente, ma è molto importante salvare prima il vostro mnemonico. Per farlo, cliccate su "*Proteggi il tuo portafoglio*" nell'angolo in alto a destra dell'interfaccia.

![Image](assets/fr/06.webp)

Se non l'avete già fatto su Proton, vi verrà chiesto di impostare un backup del vostro conto e di proteggerlo con un metodo 2FA. Queste misure di sicurezza, sebbene applicabili all'intero conto Proton, sono ancora più importanti quando il vostro portafoglio Bitcoin è integrato in esso. Vi consiglio vivamente di metterle in atto.

![Image](assets/fr/07.webp)

Per salvare la frase mnemonica, fare clic su "*Backup this wallet's seed phrase*".

![Image](assets/fr/08.webp)

Inserire la password di Proton.

![Image](assets/fr/09.webp)

Cliccate quindi su "*Vedi la frase seminale del portafoglio*" per visualizzare la frase mnemonica del vostro portafoglio.

![Image](assets/fr/10.webp)

Proton Wallet visualizza la frase mnemonica di 12 parole. **Questa frase mnemonica vi dà accesso completo e illimitato a tutti i vostri bitcoin**. Chiunque sia in possesso di questa frase può rubare i vostri fondi, anche senza accedere al vostro conto Proton. La frase di 12 parole può essere utilizzata per ripristinare l'accesso ai vostri bitcoin se perdete l'accesso al vostro conto. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.

Potete scriverlo su un foglio di carta o, per maggiore sicurezza, vi consiglio di inciderlo su una base di acciaio inossidabile per proteggerlo da incendi, alluvioni o crolli.

![Image](assets/fr/11.webp)

Per ulteriori informazioni sul modo corretto di salvare e gestire la frase mnemonica, vi consiglio di seguire quest'altro tutorial, soprattutto se siete principianti:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
naturalmente, non dovreste mai fotografare queste parole, a differenza di quanto faccio io in questo tutorial.**_

Una volta salvata la frase, fate clic sul pulsante "*Fatto*".

![Image](assets/fr/12.webp)

## Scoprire l'interfaccia

L'interfaccia di Proton Wallet è molto intuitiva. Sulla sinistra si trovano i diversi portafogli e i relativi conti associati. Il conto "*Primario*" è il vostro conto principale. Per motivi di riservatezza, i bitcoin ricevuti tramite l'indirizzo e-mail di Proton vengono inseriti in un conto separato, denominato "*Bitcoin via e-mail*".

![Image](assets/fr/13.webp)

Per aggiungere un nuovo account, cliccare su "*Aggiungi account*".

![Image](assets/fr/14.webp)

Per creare un nuovo portafoglio, cliccare sul simbolo "*+*" accanto a "*Portafogli*".

![Image](assets/fr/15.webp)

Qui è possibile aggiungere una passphrase BIP39 a un nuovo portafoglio.

![Image](assets/fr/16.webp)

Per approfondire la conoscenza della passphrase, vi consiglio questo tutorial:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
## Ricevere bitcoin

Per ricevere bitcoin nel proprio portafoglio, selezionare il conto desiderato sulla sinistra dell'interfaccia, quindi fare clic sul pulsante "*Ricevi*".

![Image](assets/fr/17.webp)

Proton Wallet genera automaticamente un nuovo indirizzo vuoto.

![Image](assets/fr/18.webp)

Una volta completata la transazione, la si troverà nella sezione "*Transazioni*". Fare clic su "*+Aggiungi*" per assegnare un'etichetta alla transazione.

![Image](assets/fr/19.webp)

## Inviare bitcoin

Ora che avete dei bitcoin nel vostro portafoglio, potete inviarli. Selezionate il conto di vostra scelta sul lato sinistro dell'interfaccia, quindi cliccate su "*Invio*".

![Image](assets/fr/20.webp)

Inserire l'indirizzo Bitcoin del destinatario. È possibile scansionare un codice QR facendo clic sul piccolo logo. Per inviare a un indirizzo e-mail, inserirlo direttamente in questo campo. Una volta inserito l'indirizzo Bitcoin, cliccate sulla piccola freccia e poi su "*Conferma*".

![Image](assets/fr/21.webp)

Inserite l'importo da inviare, in valuta fiat o in bitcoin, quindi fate clic su "*Review*".

![Image](assets/fr/22.webp)

Selezionare la commissione di transazione in base alla situazione attuale del mercato.

![Image](assets/fr/23.webp)

Aggiungere un'etichetta alla transazione, quindi ricontrollare tutti i dettagli. Se tutto è corretto, fare clic su "*Conferma e invia*" per firmare e inviare la transazione.

![Image](assets/fr/24.webp)

La transazione apparirà in attesa di conferma nella sezione "*Transazioni*" del vostro conto.

![Image](assets/fr/25.webp)

## Accesso all'applicazione

Oltre al client web, Proton Wallet è accessibile anche tramite un'applicazione mobile. Collegando il portafoglio al proprio conto Proton, è possibile sincronizzarlo tra il client web e l'applicazione mobile.

Scaricate Proton Wallet dal vostro negozio di applicazioni:


- [Su App Store](https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548);
- [Su Google Play Store](https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

Dopo l'installazione, fare clic su "*Log in*" e inserire l'indirizzo e-mail e la password di Proton.

![Image](assets/fr/27.webp)

Avrete quindi accesso al vostro portafoglio Bitcoin, con le stesse funzioni del client web.

![Image](assets/fr/28.webp)

Congratulazioni, ora sapete come configurare e utilizzare Proton Wallet. Se avete trovato utile questo tutorial, vi sarei grato se lasciaste un pollice verde qui sotto. Sentitevi liberi di condividere questo articolo sui vostri social network. Grazie per la condivisione!

Per approfondire, vi consiglio questo tutorial su Jade Plus, l'ultimo portafoglio hardware di Blockstream:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
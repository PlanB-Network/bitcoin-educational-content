---
name: Phoenix
description: Installazione e utilizzo di Phoenix Wallet
---
![cover](assets/cover.webp)

Phoenix è un wallet e un nodo Lightning self-custodial sviluppato da ACINQ, un'azienda francese specializzata in soluzioni software basate su Lightning. A differenza dei wallet Lightning con custodia, come Wallet of Satoshi, dove i bitcoin sono detenuti da terzi, Phoenix consente agli utenti di mantenere il pieno controllo delle proprie chiavi private.

Phoenix funziona come un vero nodo Lightning integrato nel tuo telefono, che apre automaticamente un canale con il nodo Lightning di ACINQ. L'applicazione si basa su Lightning-KMP, un'implementazione multipiattaforma della Lightning Network in Kotlin, ottimizzata per i wallet mobili. A differenza di altre soluzioni di nodi Lightning, Phoenix semplifica notevolmente la gestione. L'utente non deve preoccuparsi di aprire e chiudere canali, eseguire un nodo Bitcoin o gestire la liquidità sulla rete Lightning. Phoenix si occupa automaticamente di tutte queste operazioni tecniche in background.

Questa applicazione combina la facilità d'uso e la convenienza dei wallet Lightning mobili con la sicurezza e la sovranità di un vero e proprio nodo Lightning personale. Phoenix permette di utilizzare la rete Lightning in modo sicuro, efficiente e autonomo, godendo di un'esperienza utente fluida e intuitiva.

In cambio, si applicano alcune tariffe:


- L'invio tramite Lightning costa lo 0,4% dell'importo più 4 sats;
- Se devi ricevere fondi tramite Lightning, viene addebitato l'1% dell'importo;
- L'apertura di ogni canale costa 1000 sats.

A mio parere, Phoenix rappresenta un'eccellente soluzione intermedia tra i wallet Lightning con custodia e la gestione manuale di un nodo Lightning. Questa applicazione è adatta sia ai principianti che agli utenti avanzati che preferiscono non occuparsi dei dettagli della gestione del proprio LND o Core Lightning. Scopriamo come utilizzarla!

![Image](assets/fr/01.webp)

## Installa l'applicazione

Vai nel tuo store di applicazioni e installa Phoenix :


- Sul [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet);
- Su [App Store](https://apps.apple.com/app/phoenix-wallet/id1544097028?l=en-GB).

![Image](assets/fr/02.webp)

È anche possibile installare l'applicazione [con il file apk sul loro repository GitHub](https://github.com/ACINQ/phoenix/releases).

![Image](assets/fr/03.webp)

## Crea il tuo wallet

Una volta avviata l'applicazione, fai clic sul pulsante "*Next*" per saltare la presentazione, quindi su "*Start*".

![Image](assets/fr/04.webp)

Seleziona "*Create a new wallet*".

![Image](assets/fr/05.webp)

Ecco fatto: il wallet e il nodo Lightning sono stati creati.

![Image](assets/fr/06.webp)

## Salva la frase mnemonica

Prima di iniziare, dobbiamo salvare la nostra frase mnemonica di 12 parole. Questa frase dà accesso completo e illimitato a tutti i tuoi bitcoin. Chiunque sia in possesso di questa frase può rubare i tuoi fondi, anche senza accedere fisicamente al tuo telefono.

La frase di 12 parole ripristina l'accesso ai bitcoin in caso di perdita, furto o rottura del telefono. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.

Puoi scriverlo su carta o, per maggiore sicurezza, inciderlo su acciaio inossidabile per proteggerlo da incendi, inondazioni o crolli. La scelta del supporto per la tua mnemonica dipenderà dalla tue strategie di sicurezza, ma se utilizzi Phoenix come wallet di spesa contenente importi moderati, la carta dovrebbe essere sufficiente.

Per ulteriori informazioni sul modo corretto di salvare e gestire la frase mnemonica, ti consiglio di seguire quest'altro tutorial, soprattutto se sei principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Fai clic sul messaggio visualizzato nella parte superiore dell'interfaccia "*Save your wallet...*".

![Image](assets/fr/07.webp)

Poi clicca su "*Save my wallet*".

![Image](assets/fr/08.webp)

Poi clicca su "*View my key*" e salva la tua frase mnemonica su un supporto fisico.

![Image](assets/fr/09.webp)

Spunta le due caselle in fondo all'interfaccia per confermare che il backup è stato completato con successo.

![Image](assets/fr/10.webp)

## Configura l'applicazione

Prima di effettuare le prime transazioni, puoi personalizzare le impostazioni facendo clic sull'icona della ruota dentata in basso a sinistra dell'interfaccia.

![Image](assets/fr/11.webp)

Nel menù "*Display*" puoi scegliere il tema dell'applicazione, la denominazione utilizzata per i bitcoin e la valuta locale.

![Image](assets/fr/12.webp)

In "*Payment options*" torvi varie impostazioni avanzate per i pagamenti Lightning. Puoi mantenere le impostazioni predefinite.

![Image](assets/fr/13.webp)

In "*Channel management*", imposta la tariffa massima che sei disposto a pagare per l'apertura di un canale Lightning.

![Image](assets/fr/14.webp)

Nel menù "*Access control*", ti consiglio vivamente di attivare un sistema di autenticazione per proteggere l'accesso all'applicazione sul tuo telefono. Questo impedirà a chiunque abbia accesso al tuo telefono sbloccato di accedere a Phoenix e rubare i tuoi bitcoin.

![Image](assets/fr/15.webp)

Nel menù "*Electrum server*", se disponi di un server Electrs, puoi collegarlo per trasmettere le transazioni.

![Image](assets/fr/16.webp)

Per migliorare la riservatezza delle tue connessioni, attiva le connessioni via Tor nel menù "*Tor*". Sebbene l'uso di Tor possa rallentare leggermente i pagamenti e richieda che l'applicazione Phoenix sia aperta in primo piano durante la ricezione, aumenta notevolmente la privacy.

![Image](assets/fr/17.webp)

## Ricevi bitcoin on-chain

Al primo utilizzo, hai la possibilità di caricare il vostro wallet Phoenix con i fondi on-chain. Puoi anche effettuare questo primo deposito direttamente da Lightning (vedi sezione successiva), ma in entrambi i casi verranno applicate delle commissioni aggiuntive per l'apertura del primo canale.

Fai clic sul pulsante "*Receive*".

![Image](assets/fr/18.webp)

Fai scorrere il codice QR verso sinistra per scoprire un indirizzo di ricezione di Bitcoin. Invia l'importo che desideri depositare con Phoenix.

![Image](assets/fr/19.webp)

L'importo ricevuto on-chain apparirà prima come in sospeso nel saldo del wallet. Ci vorranno 3 conferme prima che i fondi siano disponibili per l'uso.

![Image](assets/fr/20.webp)

Una volta ricevuti i fondi, Phoenix apre automaticamente un canale Lightning per te. Ora puoi inviare e ricevere bitcoin tramite la rete Lightning.

![Image](assets/fr/21.webp)

## Ricevi bitcoin tramite Lightning

Per ricevere sats tramite la rete Lightning, fai clic sul pulsante "*Receive*".

![Image](assets/fr/22.webp)

Phoenix genera una invoice Lightning. Puoi scannerizzarla o inviarla alla persona che desidera mandarti sats.

![Image](assets/fr/23.webp)

Facendo clic sul pulsante "*Edit*", puoi aggiungere una descrizione che sarà visibile al pagatore sull'invoice e definire un importo specifico che il pagatore deve inviare.

![Image](assets/fr/24.webp)

Le classiche invoice di cui sopra possono essere utilizzate una sola volta. Per un'opzione di pagamento riutilizzabile, puoi ricorrere al tuo codice QR riutilizzabile tramite l'offerta BOLT12.

![Image](assets/fr/25.webp)

Una volta saldata la invoice o l'offerta BOLT12, la transazione apparirà sul tuo wallet Lightning.

![Image](assets/fr/26.webp)

## Invia bitcoin tramite Lightning

Ora che hai i sats su Phoenix, sei pronto ad effettuare i pagamenti tramite la rete Lightning. Inizia facendo clic sul pulsante "*Send*".

![Image](assets/fr/27.webp)

Sono disponibili diverse opzioni. Cliccando su "*Scan QR code*", puoi scansionare una invoice Lightning, un'offerta BOLT12 o anche un indirizzo di ricezione per il pagamento on-chain.

![Image](assets/fr/28.webp)

Puoi inserire queste informazioni anche manualmente tramite la tastiera nel campo in alto nell'interfaccia, oppure inserire un indirizzo Lightning (BOLT12 o LNURL). Puoi anche incollare direttamente le informazioni utilizzando il pulsante "*Paste*".

![Image](assets/fr/29.webp)

In questo esempio, ho scansionato una invoice per 10.000 sats. Per effettuare il pagamento, basta cliccare su "*Pay*".

![Image](assets/fr/30.webp)

La transazione è completata.

![Image](assets/fr/31.webp)

Congratulazioni, ora sai come configurare e utilizzare Phoenix. Se hai trovato utile questo tutorial, ti sarei grato se lasciassi un pollice verde qui sotto. Sentiteti libero di condividere questo articolo sui tuoi social network. Grazie per la condivisione!

Per fare un ulteriore passo avanti, dai un'occhiata a questo tutorial su Alby Hub, un'altra soluzione innovativa e facile da usare per lanciare il tuo nodo Lightning:

https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Per saperne di più sul funzionamento tecnico della rete Lightning, puoi trovare l'eccellente formazione gratuita di Fanis Michalakis su Plan ₿ Network:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

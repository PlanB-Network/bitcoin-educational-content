---
name: BitcoinVoucherBotP2P

description: Come Acquistare e vendere Bitcoin P2P con BitcoinVoucherBot (Nuova Estensione)
---

![image](assets/cover.webp)

Sentiamo ancora parlare di BitcoinVoucherBot, un bot Telegram nato per acquistare Bitcoin senza KYC (“Know Your Customer”), offrendo quindi un livello di anonimato ridotto. Puoi trovare una giuda dettagliata qui:

https://planb.network/en/tutorials/exchange/centralized/bitcoin-voucher-bot-5f5d9449-10a7-4f97-9278-8dfbbea5ab1a

In questa guida vedremo come funziona la nuova implementazione che permette di acquistare e vendere Bitcoin direttamente sul nuovo marketplace P2P (Peer-To-Peer).

Per contrastare le nuove restrizioni che sempre più spesso minacciano la libertà digitale e la privacy, gli sviluppatori hanno creato questa estensione, dando agli utenti la possibilità di comprare e vendere Bitcoin con un elevato grado di anonimato tramite il P2P (Peer-To-Peer).

Ma vediamo come funziona questo nuovo metodo di scambio.

Per utilizzare il servizio dovrai effettuare i trasferimenti tramite Lightning Network. Assicurati quindi di avere un wallet che supporti questo protocollo e che ti consenta di usare un “LNURL” o un “Lightning Address” per ricevere e inviare i  fondi. 

Tra i wallet supportati possiamo trovare:

- [Sats.Mobi](https://planb.academy/it/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodial)
- [Wallet Of Satoshi](https://planb.academy/it/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Custodial con swap a Non-Custodial)
- [Breez](https://planb.academy/it/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)

Oppure qualsiasi wallet che abbia un “Lightning Address” e che generi una fattura Bolt11. Al momento non sono supportati i wallet che generano una fattura Bolt12.

Per questo tutorial, dato la sua semplicità d’uso immediato, utilizzeremo Wallet of Satoshi.

**Attenzione**: Wallet of Satoshi, pur diffuso tra i principianti, è custodial, con controllo limitato sui fondi; usalo solo transitoriamente, trasferendoli subito a un non-custodial per piena sovranità. Da ottobre 2025, include una modalità self-custodial stabile worldwide su iOS/Android (aggiorna l'app), con chiavi private autonome, switch tra modalità, indirizzi Lightning personalizzati e backup seed 12 parole. Tuttavia, resta una soluzione provvisoria fino a consolidamento, preferendo wallet non-custodial maturi per la gestione a lungo termine.

Molto bene! Ora possiamo iniziare il nostro percorso, che ti guiderà passo passo nella creazione dell’account, nella gestione dei match di acquisto e vendita e nell’utilizzo della tua area riservata.

**Wallet e Iscrizione**

Per prima cosa, se non lo hai già installato sul tuo smartphone, scarica Wallet of Satoshi.

- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)

![image](assets/it/01.webp)

Se non hai mai utilizzato Wallet of Satoshi e vuoi comprenderne il funzionamento, ti consiglio di seguire questo tutorial, così potrai attivarlo correttamente ed eseguire il backup in modo sicuro.

https://planb.network/en/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7


Ora che il tuo wallet è pronto, puoi iniziare a inviare una piccola quantità di sats.
Tieni presente che, per completare l’iscrizione alla piattaforma P2P (Peer-To-Peer), ti verranno richiesti 1000 sats come misura di controllo: questo serve a proteggerti da eventuali match fantasma (scam) e impedisce che chiunque possa iscriversi senza limiti.

![image](assets/it/02.webp)

Ora possiamo aprire la piattaforma P2P (Peer-To-Peer) per procedere all’iscrizione.
Puoi accedere da PC desktop o browser su smartphone, tramite il bot Telegram BitcoinVoucherBot oppure tramite link .onion, per garantire un livello di privacy ancora maggiore.

- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Browser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)

Verrai reindirizzato alla pagina principale.

premi su “Get Starter”(“inizia subito”)

![image](assets/it/03.webp)

Nella schermata successiva devi scegliere una password e inserirla (riquadro A), per poi ripeterla (riquadro B). Ti raccomando di salvare subito questa password su un supporto di backup, che può essere su un dispositivo digitale sicuro come per esempio Bitwarden o un documento cartaceo.

Spunta la casella di verifica dove dichiari di non essere un robot (riquadro C).

Nota bene! Non abilitare la crittografia RSA a meno che tu non sappia esattamente cos’è e come funziona. In questa fase non è necessario fare nulla.

Clicca su “Generate Avatar” ( Genera Avatar”) (riquadro D).

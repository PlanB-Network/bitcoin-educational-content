---
name: Bacca
description: Configurazione di un Ledger senza il software Ledger Live
---
![cover](assets/cover.webp)

Se si utilizza un Ledger, probabilmente si è scoperto che è necessario passare attraverso il software Ledger Live, almeno per la configurazione iniziale del dispositivo, per verificarne l'autenticità e installare l'applicazione Bitcoin su di esso. Tuttavia, dopo questa configurazione, molti bitcoiners preferiscono utilizzare un software specializzato nella gestione dei portafogli Bitcoin, come Sparrow o Liana, piuttosto che Ledger Live. Sebbene Ledger produca eccellenti portafogli hardware che includono rapidamente le ultime funzionalità di Bitcoin, il loro software non è necessariamente adattato alle esigenze specifiche dei bitcoiners. Infatti, Ledger Live include molte funzioni pensate per le altcoin, mentre le opzioni dedicate alla gestione dei portafogli Bitcoin sono limitate. Il problema di Sparrow e Liana (per il momento) è che non consentono di installare l'applicazione Bitcoin sul Ledger.

Per evitare di dover utilizzare Ledger Live durante la configurazione iniziale del Ledger, è possibile utilizzare lo strumento Bacca (o "Ledger Installer"). Questo software consente di installare e aggiornare l'applicazione Bitcoin, di verificare l'autenticità del Ledger e di aggiornare successivamente il firmware del dispositivo. Bacca è stato creato da Antoine Poinsot (Darosior), sviluppatore di Bitcoin Core presso Chaincode Labs, co-fondatore [di Revault e Liana] (https://wizardsardine.com/) e Pythcoiner.

In questo tutorial vi mostrerò come utilizzare questo strumento, in modo da poter fare definitivamente a meno del software Ledger Live e continuare a utilizzare i dispositivi Ledger. Funziona su tutti i dispositivi: Nano S Classic, Nano S Plus, Nano X, Flex e Stax.

---
*Si noti che questo strumento è abbastanza nuovo e i suoi sviluppatori specificano che è ancora **in fase di test**. Si consiglia di utilizzarlo solo per scopi di prova e non per un dispositivo destinato a ospitare un vero portafoglio Bitcoin, sebbene sia possibile farlo. A questo proposito, vi raccomando di seguire le raccomandazioni degli sviluppatori di questo strumento, che sono specificate [nel README del loro repository GitHub](https://github.com/darosior/ledger_installer)

---
## Prerequisiti

Sul computer sono necessari due strumenti per utilizzare Bacca:


- Git ;
- Ruggine.

Se li avete già installati, potete saltare questo passaggio.

**Linux:**

Su una distribuzione Linux, Git è generalmente preinstallato. Per verificare se Git è installato sul vostro sistema, potete digitare il seguente comando nel terminale :

```bash
git --version
```

Se non avete Git installato sul vostro sistema, ecco il comando per installarlo su Debian :

```bash
sudo apt install git
```

Infine, per installare l'ambiente di sviluppo Rust, utilizzate il comando :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Windows:**

Per installare Git, visitate [il sito web ufficiale del progetto](https://git-scm.com/). Scaricare il software e seguire le istruzioni di installazione.

![BACCA](assets/fr/01.webp)

Procedete allo stesso modo per installare Rust da [il sito ufficiale](https://www.rust-lang.org/tools/install).

![BACCA](assets/fr/02.webp)

**MacOS:**

Se Git non è ancora installato sul vostro sistema, aprite un terminale ed eseguite il seguente comando per installarlo:

```bash
git --version
```

Se Git non è installato sul vostro sistema, si aprirà una finestra che vi proporrà di installare Xcode, che include Git. È sufficiente seguire le istruzioni sullo schermo per procedere all'installazione.

Per installare Rust, eseguire il seguente comando:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Installazione di Bacca

Aprite un terminale e andate nella cartella in cui volete salvare il software, quindi eseguite il seguente comando:

```bash
git clone https://github.com/darosior/ledger_installer.git
```

Accedere alla directory del software:

```bash
cd ledger_installer
```

Quindi utilizzare Cargo per compilare il progetto ed eseguire la GUI di Bacca:

```bash
cargo run -p ledger_manager_gui
```

Ora si ha accesso all'interfaccia del software.

![BACCA](assets/fr/03.webp)

## Configurazione del libro mastro

Prima di iniziare, se il vostro Ledger è nuovo, assicuratevi di aver impostato il codice PIN e salvato la frase di recupero. Per queste fasi iniziali non è necessario Ledger Live. È sufficiente collegare il Ledger tramite il cavo USB per alimentarlo. Se non si è sicuri di come procedere con questi due passaggi, si può fare riferimento all'inizio del tutorial specifico per il proprio modello:

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Utilizzo di Bacca

Collegare il Ledger al computer e sbloccarlo utilizzando il codice PIN impostato. Bacca dovrebbe rilevare automaticamente il Ledger.

![BACCA](assets/fr/04.webp)

Per confermare l'autenticità del vostro Ledger, fate clic sul pulsante "*Check*". Per continuare, è necessario autorizzare la connessione sul dispositivo Ledger.

![BACCA](assets/fr/05.webp)

Bacca vi informerà quindi se il vostro Ledger è autentico. Se non lo è, significa che il dispositivo è stato compromesso o che è contraffatto. In questo caso, smettete immediatamente di usarlo.

![BACCA](assets/fr/06.webp)

Nel menu "*Apps*" è possibile consultare l'elenco delle applicazioni già installate sul Ledger.

![BACCA](assets/fr/07.webp)

Per installare l'applicazione Bitcoin, fare clic su "*Install*", quindi autorizzare l'installazione sul proprio Ledger.

![BACCA](assets/fr/08.webp)

L'applicazione è ben installata.

![BACCA](assets/fr/09.webp)

Se non è installata l'ultima versione dell'applicazione Bitcoin, Bacca visualizzerà un pulsante "*Aggiornamento*" invece dell'indicazione "*Ultimo*". È sufficiente fare clic su questo pulsante per aggiornare l'applicazione.

![BACCA](assets/fr/10.webp)

Ora che il vostro Ledger è configurato correttamente con l'ultima versione dell'applicazione Bitcoin, siete pronti a importare e utilizzare il vostro portafoglio su software di gestione come Sparrow o Liana, senza dover passare per Ledger Live!

Se avete trovato utile questa guida, vi sarei grato se lasciaste un pollice verde qui sotto. Sentitevi liberi di condividere questo articolo sui vostri social network. Grazie mille!

Vi consiglio anche di dare un'occhiata a questo tutorial su GnuPG, che spiega come verificare l'integrità e l'autenticità del software prima di installarlo. Si tratta di una pratica importante, soprattutto quando si installa un software di gestione del portafoglio come Liana o Sparrow:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

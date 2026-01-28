 ---
name: PureOS
description: La distribuzione Linux che ti dà il controllo sulla tua vita digitale.
---

![cover](assets/cover.webp)

La protezione delle informazioni personali nell'era digitale è una priorità assoluta per ogni utente di Internet. Le aziende, le organizzazioni e persino i sistemi operativi sono utili fonti di informazioni per definire il tuo profilo e il tuo stile di vita. La scelta del sistema operativo giusto è il primo passo per rafforzare la propria privacy online. In questa guida daremo un'occhiata a PureOS, una distribuzione Linux incentrata sulla privacy.

https://planb.academy/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f


## Come iniziare con PureOS

PureOS è un sistema operativo basato su Debian e sviluppato da Purism. PureOS è adatto sia ai professionisti IT che agli utenti che cercano una distribuzione semplice e facile da usare. È unico in quanto è _software libero_ e si concentra sulla protezione dei dati personali dei suoi utenti, creando una struttura basata sulla privacy, la libertà, la sicurezza e la stabilità offerte da Debian.

### Perché scegliere PureOS?

- **Interfaccia semplice e intuitiva**: GNOME offre un'interfaccia desktop chiara, progettata per essere facile da usare, anche per chi non è pratico della riga di comando.

- **Gratuito**: come la maggior parte delle distribuzioni Linux, PureOS è completamente gratuito. Tuttavia, è disponibile un abbonamento mensile per sostenere gli sviluppatori.

- **Sicurezza e stabilità**: l'architettura e la modalità operativa di PureOS ne fanno una distribuzione altamente sicura, che garantisce la protezione dei dati e la stabilità del sistema.

- **Documentazione e comunità attiva**: PureOS dispone di una documentazione chiara e accessibile e di una comunità impegnata e reattiva, che facilita la risoluzione dei problemi e l'apprendimento del sistema passo dopo passo.


## Installazione e configurazione

L'installazione e la configurazione di PureOS sul computer richiedono le seguenti caratteristiche minimali:
- Una chiave USB di almeno 8 GB per eseguire il flash del sistema.
- 4 GB DI RAM.
- 30 GB di spazio libero sull'hard disk.

Accedi al [sito web ufficiale di PureOS](https://pureos.net/) e scarica l'immagine ISO del sistema operativo in base all'architettura della tua macchina.

Per avviare l'installazione di PureOS, è necessario creare una chiave USB avviabile utilizzando un software flash come [Balena Etcher](https://www.balena.io/etcher).

In tre semplici passaggi, otterrai una chiavetta USB avviabile con il sistema operativo PureOS:
- Collega la chiave USB ed esegui il software scaricato Balena Etcher.
- Quindi seleziona l'immagine ISO di PureOS.
- Scegli la chiave USB come dispositivo di output, quindi fai clic sul pulsante **Flash** e attendi il completamento del processo.

![0_01](assets/fr/01.webp)

Una volta avviata la chiave USB, riavvia il computer su cui desideri installare PureOS.

All'avvio, accedi al BIOS premendo i tasti `ESC`, `F9` o `F11`, a seconda della macchina. Seleziona la chiave USB come dispositivo di avvio, quindi premi `ENTER` per confermare.

### Schermata di avvio

PureOS offre diverse opzioni per l'avvio del sistema operativo. Scegli l'opzione **Test o Install PureOS** per avviare l'installazione del sistema operativo.

![0_02](assets/fr/02.webp)

Imposta la lingua e il layout della tastiera che desideri utilizzare sul computer.

![0_03](assets/fr/03.webp)

![0_04](assets/fr/04.webp)

Consenti o nega l'accesso alla tua **località geografica** alle applicazioni per consigli personalizzati basati sulla tua zona.

![0_05](assets/fr/05.webp)

Puoi collegarti all'account **NextCloud** esistente per recuperare i dati collegati alla suite per ufficio in uso su un altro sistema.

![0_06](assets/fr/06.webp)

Viene fornita un'esercitazione, ma puoi chiudere la finestra se desideri saltare questo passaggio.

![0_08](assets/fr/08.webp)

### Avvio dell'installazione

Fai clic sul menu **Attività** ed esplora le applicazioni e gli strumenti preinstallati sul sistema. Fai clic su **Installa PureOS** per avviare l'installazione

![0_09](assets/fr/09.webp)

Imposta la lingua del sistema e il layout della tastiera come richiesto, quindi configura la modalità di partizionamento dell'hard disk.

![0_10](assets/fr/10.webp)

![0_11](assets/fr/11.webp)

![0_12](assets/fr/12.webp)

![0_13](assets/fr/13.webp)

Per il partizionamento dell'hard disk sono disponibili due opzioni:

- **Cancella disco**: per un'installazione completa di PureOS, cancella tutti i dati preesistenti sull'hard disk.

![0_14](assets/fr/14.webp)

- **Partizione manuale** per creare partiture personalizzate.

⚠️ Quando si creano manualmente le partizioni per il sistema operativo, assicurati di allocare una partizione di almeno 2 GB per il funzionamento di PureOS e un'altra partizione per i dati.

![0_15](assets/fr/15.webp)

Attiva la **crittografia del disco** se desideri proteggere i dati. Inserisci una password forte e complessa.

Associa un utente al sistema operativo definendo un nome utente e una password alfanumerica di almeno 20 caratteri per rafforzare la sicurezza dei dati.

![0_16](assets/fr/16.webp)

Rivedi le impostazioni effettuate e modificale se necessario.

![0_17](assets/fr/17.webp)

Fai clic su **Install** e poi su **Install Now** per confermare che PureOS è stato installato sul computer.

![0_18](assets/fr/18.webp)

![0_19](assets/fr/19.webp)

Al termine dell'installazione, seleziona la casella **Restart now** per riavviare il computer e confermare:
- La lingua.
- Layout della tastiera.
- L'account NextCloud (facoltativo).

![0_25](assets/fr/25.webp)


## Aggiornamenti

Prima di iniziare a utilizzare PureOS, è essenziale aggiornare il sistema. Questo vi consentirà di beneficiare delle ultime funzioni e patch di sicurezza, oltre a garantire una maggiore stabilità.

- Aggiornamento tramite interfaccia grafica:

Apri l'applicazione **Software**, quindi accedi alla scheda **Aggiornamenti**. Gli aggiornamenti disponibili vengono visualizzati automaticamente. Fai clic su **Download**, quindi su **Install** una volta completato il download.

- **Aggiornamento tramite terminale**:

Apri il terminale e digita il seguente comando per aggiornare l'elenco dei pacchetti disponibili:

```shell
sudo apt update
```

Immetti la password e conferma. Quindi installa gli aggiornamenti con:

```shell
sudo apt full-upgrade
```


## PureOS per lo sviluppo

Per impostazione predefinita, PureOS non include tutti gli strumenti necessari per lo sviluppo.

Puoi installarli rapidamente con il seguente comando:

```shell
sudo apt install build-essential git curl
```

Questo installerà gli strumenti di compilazione **Git** e **Curl**, utili nella maggior parte degli ambienti di sviluppo.


## Ambiente PureOS

PureOS si distingue per il suo approccio innovativo alla vera convergenza: un unico sistema operativo garantisce un funzionamento fluido e senza interruzioni su una varietà di dispositivi, tra cui laptop, tablet, mini-PC e smartphone.

Le applicazioni PureOS sono progettate per essere adattive: si adattano automaticamente alle dimensioni dello schermo e alla modalità di input (touch o tastiera/mouse). Ad esempio, il browser Web GNOME adatta dinamicamente la sua interfaccia per fornire un'esperienza ottimale sia sui dispositivi mobili che su quelli desktop.

PureOS include anche la suite per ufficio **LibreOffice**, che comprende:
- **Writer**: un elaboratore di testi completo per la creazione e la modifica di documenti.
- **Calc**: un potente programma di foglio elettronico per la gestione dei dati e dei calcoli.
- **Impress**: uno strumento per creare presentazioni professionali.

Questa suite gratuita consente di lavorare in modo efficiente senza dover dipendere da software proprietari.

PureOS offre un ambiente unificato, sicuro e flessibile, basato su una distribuzione 100% open source che garantisce un controllo totale e un rigoroso rispetto della privacy. La sua reale convergenza facilita la creazione di applicazioni compatibili con diversi tipi di dispositivi, come computer, tablet e smartphone, senza la necessità di complessi adattamenti.

Grazie all'accesso nativo a strumenti essenziali, a robusti gestori di pacchetti e a un ricco ecosistema open-source, PureOS semplifica lo sviluppo, il test e la distribuzione di applicazioni in un ambiente sicuro. La sua architettura stabile e l'impegno per la riservatezza lo rendono una piattaforma affidabile per una varietà di usi, tra cui lo sviluppo Blockchain, la prototipazione rapida o gli ambienti di produzione.

Scopri il nostro corso per rafforzare la tua sicurezza e proteggere la tua privacy digitale.

https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

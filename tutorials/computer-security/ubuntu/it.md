---
name: Ubuntu
description: Guida completa all'installazione e all'utilizzo di Ubuntu come alternativa a Windows
---
![cover](assets/cover.webp)


## Introduzione

Un sistema operativo (OS) è il software principale che gestisce tutte le risorse del computer. Scegliere un sistema operativo alternativo come Ubuntu può offrire molti vantaggi in termini di sicurezza, costi e privacy.

### Perché Ubuntu?

- **Sicurezza migliorata**: le distribuzioni Linux sono rinomate per la loro sicurezza e robustezza;
- **Costo zero**: Ubuntu e la maggior parte delle distribuzioni Linux sono gratuite;
- **Grande comunità**: una comunità di utenti pronti ad aiutare tramite forum e tutorial;
- **Rispetto della privacy**: sistema open source per una maggiore trasparenza;
- **Semplicità**: interfaccia intuitiva e facilità d'uso;
- **Ricco ecosistema**: ampio catalogo di software open source;
- **Supporto regolare**: ggiornamenti sicuri da parte di Canonical;


## Installazione e configurazione

### 1. Prerequisiti

**Attrezzatura richiesta**:
- Una chiave USB di almeno 12 GB
- Un computer con almeno 25 GB disponibili

### 2. Scaricare

- Vai su [ubuntu.com/download](https://ubuntu.com/download);
- Scegli la versione stabile (si consiglia la LTS);
- Scarica l'immagine ISO.

![Page de téléchargement Ubuntu](assets/fr/01.webp)

![Sélection de la version Ubuntu](assets/fr/02.webp)

### 3. Creare una chiave USB avviabile

È possibile utilizzare diversi strumenti, come Balena Etcher:
- Scarica e installa [Balena Etcher](https://etcher.balena.io/)

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

![Installation de Balena Etcher](assets/fr/04.webp)

- Apri Balena Etcher, quindi seleziona l'immagine ISO di Ubuntu;
- Seleziona la chiave USB come supporto di destinazione;
- Fai clic su Flash e attendi il completamento del processo.

![Utilisation de Balena Etcher](assets/fr/05.webp)

### 4. Installazione e protezione di Ubuntu

**4.1 Avvio da chiavetta USB**

- Spegni il computer;
- Inserisci la chiavetta USB (contenente Ubuntu);
- Accendi il computer. Sui PC recenti, il sistema dovrebbe riconoscere automaticamente la chiave di avvio USB. In caso contrario, riavviare tenendo premuto il tasto di accesso al BIOS/UEFI (di solito F2, F3, F11, F12, Esc o Canc, a seconda della marca)
 - Nel menu BIOS/UEFI, seleziona la chiave USB come dispositivo di avvio;
 - Salva e riavvia.

**4.2 Avvio dell'installazione**

**Schermo di avvio**

Quando avvii la chiavetta USB, viene visualizzata questa schermata, che consente di avviare Ubuntu.

![Écran de démarrage Ubuntu](assets/fr/06.webp)

**Scelta della lingua**

Scegli la lingua preferita per l'installazione e il sistema.

![Sélection de la langue](assets/fr/07.webp)

**Opzioni di accessibilità**

Configura le opzioni di accessibilità, se necessario (screen reader, contrasto elevato, ecc.).

![Options d'accessibilité](assets/fr/08.webp)

**Configurazione della tastiera**

Seleziona il layout della tastiera. È disponibile un campo di prova per verificare che i tasti corrispondano alla propria configurazione.

![Configuration du clavier](assets/fr/09.webp)

**Connessione alla rete**

Collegati alla rete Wi-Fi o cablata per scaricare gli aggiornamenti durante l'installazione.

![Configuration réseau](assets/fr/10.webp)

**Tipo di installazione**

Scegli tra "Prova Ubuntu" (per testare senza installare) o "Installa Ubuntu".

![Choix du type d'installation](assets/fr/11.webp)

**Metodo di installazione**

Seleziona l'installazione interattiva.

![Mode d'installation](assets/fr/12.webp)

**Selezione dell'applicazione**

Scegli tra l'installazione predefinita o una selezione estesa di applicazioni.

![Sélection des applications](assets/fr/13.webp)

**Applicazioni di terze parti**

Decidi se installare o meno driver aggiuntivi e software proprietario.

![Installation applications tierces](assets/fr/14.webp)

**Tipo di partizione**

Hai due opzioni principali:
- "Cancella il disco e installa Ubuntu": utilizza l'intero disco per Ubuntu;
- "Installazione manuale": creare un dual boot con Windows o personalizzare le partizioni.

![Choix du partitionnement](assets/fr/15.webp)

**Creazione dell'account utente**

Imposta il nome utente e la password per il tuo account Ubuntu.

![Création du compte](assets/fr/16.webp)

**Fuso orario**

Seleziona la tua area geografica per impostare l'ora del sistema.

![Sélection du fuseau horaire](assets/fr/17.webp)

**Riassunto dell'installazione**

Controlla tutte le scelte effettuate prima di avviare l'installazione finale. Una volta fatto clica su "Installa" e il processo inizia.

![Résumé de l'installation](assets/fr/18.webp)

**4.3 Aggiornamento di Ubuntu dopo l'installazione** (in francese)

L'aggiornamento del sistema è una fase importante dopo una nuova installazione. Sono disponibili due opzioni:

**Opzione 1: attraverso l'interfaccia grafica**

- Cerca "Software e aggiornamenti" nel menu Applicazioni;
- L'applicazione controlla automaticamente gli aggiornamenti disponibili;
- Segui le istruzioni sullo schermo per installare gli aggiornamenti.

**Opzione 2: via terminale**

- Apri il terminale (Ctrl + Alt + T)
- Digitare il seguente comando per verificare la disponibilità di aggiornamenti:

```bash
sudo apt update
```

- Inserisci la password quando richiesto;
- Per installare gli aggiornamenti, digitare:

```bash
sudo apt upgrade
```

- Conferma l'installazione digitando "Y" e poi Invio

### 5. Scoprire le attività di base

**5.1 Navigazione in Internet**

Per impostazione predefinita, Firefox si trova spesso nella barra di avvio.

Avvia Firefox e inizia a navigare.

Altri browser (Chrome, Brave, ecc.) possono essere installati tramite il Software Manager o tramite pacchetti .deb.

**5.2 Elaborazione testi**

Ubuntu viene fornito con la suite LibreOffice (Writer per l'elaborazione dei testi).

Per aprirlo: Attività > Cercare "LibreOffice Writer" o fai clic sull'icona se appare nella barra.

Puoi creare, modificare e salvare documenti in diversi formati (compreso .docx).

**5.3 Installazione delle applicazioni**

Gestore software (chiamato "Ubuntu Software"): interfaccia grafica per la ricerca e l'installazione di applicazioni.

Da Terminale, utilizzare il comando:

```bash
sudo apt install nome-del-pacchetto
```

Esempio:

```bash
sudo apt install vlc
```

### 6. Conclusioni e risorse aggiuntive

Ora sei pronto a usare Ubuntu quotidianamente: proteggi il tuo sistema, naviga, fai lavori d'ufficio, installa software e tieni aggiornato il tuo sistema operativo!

Per fare un ulteriore passo avanti nella sicurezza della tua vita digitale, ti consigliamo di dare un'occhiata al nostro servizio di messaggistica criptata, che è perfettamente adatto a proteggere la tua privacy e completa la tua installazione di Ubuntu:

https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

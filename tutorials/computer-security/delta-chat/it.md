---
name: Delta Chat
description: Guida pratica ad uno strumento di messaggistica decentralizzata
---

![image](assets/cover.webp)

## Introduzione – Chat Control e privacy

Negli ultimi anni si parla sempre più spesso di Chat Control, una proposta normativa che punta a introdurre la scansione automatica dei messaggi privati sulle principali piattaforme di comunicazione. L’obiettivo dichiarato è il contrasto a contenuti illegali, il problema è che questo meccanismo comporterebbe di fatto una sorveglianza di massa, andando a minare la cifratura end-to-end e quindi la privacy di tutti gli utenti, non solo di chi commette reati.

Il rischio concreto è che le chat diventino ambienti controllati, dove ogni messaggio, immagine o allegato potrebbe essere analizzato prima ancora di arrivare al destinatario. Ed è proprio qui che entra in gioco una possibile soluzione: abbandonare le piattaforme centralizzate e spostarsi verso sistemi di messaggistica decentralizzata, che non dipendono da un singolo provider e non possono essere facilmente soggetti a questo tipo di controllo.

In questo tutorial si presenterà una di queste soluzioni: Delta Chat. Uno strumento maturo e già utilizzabile.

## Perché Delta Chat e come funziona

Delta Chat è una soluzione di messaggistica già molto valida per l’uso quotidiano: molto utile per parlare con amici, parenti e altre persone, proprio come un vero equivalente di WhatsApp.

Si tratta di un sistema di messaggistica decentralizzato, basato interamente sulle email. In pratica sfrutta l’infrastruttura della posta elettronica tradizionale, ma costruendoci sopra un’interfaccia e un’esperienza da instant messenger moderno. A prima vista può sembrare una cosa un po’ improvvisata, ma in realtà funziona molto bene ed è sorprendentemente solida. È possibile utilizzare dei server di posta dedicati chiamati ChatMail, ma può anche funzionare senza problemi con normali server email. Questo significa che volendo si può accedere con un account già esistente, senza dover creare nulla di nuovo.

Un altro punto forte è il supporto alle WebXDC, ovvero piccole applicazioni web che si possono usare direttamente dentro le chat, in modo simile alle mini-app di Telegram. La differenza importante è che queste app non hanno accesso a Internet, quindi non possono tracciare l’utente o inviare dati all’esterno.

Dal punto di vista della sicurezza, Delta Chat utilizza una cifratura end-to-end verificata, basata su PGP ma con estensioni moderne che la rendono paragonabile, come livello di protezione, a quella di Signal. L’unica mancanza attuale è la Perfect Forward Secrecy, ma è un aspetto in evoluzione.

Essendo basato esclusivamente sulle email, Delta Chat evita del tutto:

- numeri di telefono obbligatori
- ID centralizzati
- registrazioni legate a un singolo servizio

Ed è proprio questo che rende questo strumento molto resistente a normative invasive come il Chat Control.

## Installazione

Dal sito ufficiale di [Delta Chat](https://delta.chat/download) si può andare nella sezione Download. Su Linux è disponibile comodamente tramite Flathub, ma ci sono anche pacchetti per Arch, NixOS, Snap e versioni standalone.

![image](assets/it/01.webp)

È disponibile anche per:

- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Play Store](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/us/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/us/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- e altri store...

Se stai cercando una guida per installare F-Droid, questo tutorial potrebbe aiutarti:

https://planb.academy/it/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Una cosa molto importante: le versioni desktop non richiedono il telefono. A differenza di WhatsApp o SimpleX Chat, non è necessario registrarsi prima da mobile. È possibile creare il profilo direttamente su PC oppure trasferirlo da un altro dispositivo.

## Creazione del profilo

Una volta aperta l’app, Delta Chat chiede se creare un nuovo profilo o usarne uno esistente.

![image](assets/it/02.webp)

Creando un nuovo profilo si può inserire:

- un nome
- un’immagine (opzionale)

Di default viene proposto un server ChatMail, ma è possibile:

- scegliere un altro server ChatMail
- usare un account email classico
- configurare manualmente IMAP e SMTP
- registrarsi tramite codice di invito di un altro utente

Dopo pochi secondi il profilo è pronto e si può iniziare a usare l’app.

![image](assets/it/03.webp)

## Interfaccia e chat

L’interfaccia è molto semplice e immediata:

- Messaggi di dispositivo, che sono comunicazioni locali
- Messaggi salvati, simili a quelli di Telegram e sincronizzabili tra dispositivi

![image](assets/it/04.webp)
  
Per aggiungere un contatto basta:

- mostrare il proprio QR code
- scansionare quello dell’altra persona
- invitare tramite link (condividi collegamento d'invito)

![image](assets/it/05.webp)
  
Una volta stabilita la connessione, la cifratura end-to-end viene configurata automaticamente. L'interfaccia utente delle chat è molto simile a quella di WhatsApp:

- messaggi di testo e vocali
- foto, video e file
- risposte ai messaggi
- reazioni
- messaggi a scomparsa
- notifiche personalizzabili

![image](assets/it/06.webp)

## WebXDC: le app nelle chat:

Delta Chat permette di usare WebXDC, cioè piccole applicazioni integrate nelle conversazioni. Ecco un breve elenco tra le più utili individuate:

- sondaggi
- lavagne per disegnare
- chat private temporanee
- giochi con punteggi condivisi in chat

Anche giochi più complessi possono essere avviati, e ciò dimostra la flessibilità di questo strumento.

![image](assets/it/07.webp)

## Gruppi, canali e funzioni avanzate

È possibile creare gruppi, usare sticker (soprattutto su desktop) e, attivando le opzioni sperimentali, anche canali, simili a quelli di Telegram.

Nelle impostazioni avanzate si possono attivare:

- chiamate vocali (ancora sperimentali)
- gestione avanzata del profilo email
- backup completi

![image](assets/it/08.webp)

## Multidispositivo e backup

Delta Chat supporta perfettamente il multidispositivo:

- è possibile aggiungere un secondo dispositivo tramite QR code
- si può eseguire un trasferimento completo tramite backup

In pochi secondi si ritrovano chat, gruppi e cronologia completa, senza dipendere da un server centrale.

![image](assets/it/09.webp)

## Conclusione

In un periodo in cui si parla sempre più di controllo delle comunicazioni private, Delta Chat rappresenta una risposta concreta: una messaggistica decentralizzata, cifrata e davvero utilizzabile ogni giorno.

È la soluzione che, tra tutte quelle che ho provato, mi ha convinto di più per semplicità, privacy e libertà. Se volete, potete anche contattarmi su Delta Chat tramite il seguente [link di invito](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)

Se questa guida ti è piaciuta, puoi supportarmi con una donazione e lasciando un pollice in su. E ricorda: solo usando ed esplorando Delta Chat sia da mobile che da desktop se ne scoprono davvero tutte le funzionalità.

Alla prossima.

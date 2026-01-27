---
name: Session
description: Invio di messaggi crittografati, non di metadati
---

![cover](assets/cover.webp)

Session è un'applicazione di messaggistica criptata creata nel 2020, progettata per offrire un livello di riservatezza superiore a quello della messaggistica tradizionale. È stata sviluppata prima dalla *Oxen Privacy Tech Foundation*, poi dalla *Session Technology Foundation*.

Session vanta alcune caratteristiche tecniche interessanti: la crittografia end-to-end dei messaggi, una rete decentralizzata organizzata per garantire disponibilità e ridondanza e il routing a cipolla ispirato a Tor. Inoltre, a differenza di WathsApp o Signal, che richiedono un numero di telefono per la registrazione, Session non richiede alcuna informazione personale (né numero, né e-mail, solo una coppia di chiavi crittografiche).

Session consente di inviare messaggi, file, messaggi vocali, chiamate audio, nonché gruppi fino a 100 membri (oltre a ciò, le comunità), riducendo al minimo le fughe di metadati.

![Image](assets/fr/01.webp)

Session si rivolge soprattutto agli utenti che pongono la riservatezza al centro delle loro priorità. Questo servizio di messaggistica rappresenta una seria alternativa a WhatsApp, con un'architettura progettata per resistere ai moderni modelli di sorveglianza.


| Applicazioni         | E2EE 1:1       | E2EE gruppi    | Iscrizione anonima | Licenza client open-source | Licenza server open-source | Server decentralizato  | Anno di creazione |
| -------------------- | :------------: | :------------: | :----------------: | :------------------------: | :------------------------: | :--------------------: | :---------------: |
| WhatsApp             | ✅             | ✅             | ❌                 | ❌                         | ❌                         | ❌                     | 2009             |
| WeChat               | ❌             | ❌             | ❌                 | ❌                         | ❌                         | ❌                     | 2011             |
| Facebook Messenger   | ✅             | 🟡 (opzionale) | ❌                 | ❌                         | ❌                         | ❌                     | 2011             |
| Telegram             | 🟡 (opzionale) | ❌             | 🟡                 | ✅                         | ❌                         | ❌                     | 2013             |
| LINE                 | ✅             | ✅             | ❌                 | ❌                         | ❌                         | ❌                     | 2011             |
| Signal               | ✅             | ✅             | ❌                 | ✅                         | ✅                         | ❌                     | 2014             |
| Threema              | ✅             | ✅             | ✅                 | ✅                         | ❌                         | ❌                     | 2012             |
| Element (Matrix)     | ✅             | ✅             | ✅                 | ✅                         | ✅                         | 🟡 (federata)          | 2016             |
| Delta Chat           | ✅             | ✅             | ✅                 | ✅                         | N/A                        | 🟡 (via email)         | 2017             |
| Conversations (XMPP) | ✅             | ✅             | ✅                 | ✅                         | ✅                         | 🟡 (federata)          | 2014             |
| Session              | ✅             | ✅             | ✅                 | ✅                         | ✅                         | ✅                     | 2020             |
| SimpleX              | ✅             | ✅             | ✅                 | ✅                         | ✅                         | ✅                     | 2021             |
| Olvid                | ✅             | ✅             | ✅                 | ✅                         | ❌                         | 🟡 (nessuna directory) | 2019             |
| Keet                 | ✅             | ✅             | ✅                 | ❌                         | N/A                        | ✅                     | 2022             |
| Jami                 | ✅             | ✅             | ✅                 | ✅                         | N/A                        | ✅                     | 2005             |
| Briar                | ✅             | ✅             | ✅                 | ✅                         | N/A                        | ✅                     | 2018             |
| Tox                  | ✅             | ✅             | ✅                 | ✅                         | N/A                        | ✅                     | 2013             |

*E2EE = crittografia end-to-end*


## Installare l'applicazione Session

Session è disponibile su tutte le piattaforme. Puoi scaricare l'applicazione direttamente dallo store delle applicazioni del telefono:
- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).

Su Android, è anche possibile [installare l'app via APK](https://github.com/session-foundation/session-android/releases).

In questa guida ci concentreremo sulla versione mobile, ma ricordiamo che [sono disponibili anche le versioni per computer](https://getsession.org/download) (MacOS, Linux e Windows). Più avanti vedremo come sincronizzare un account su più dispositivi.


## Creare un account su Session

Al primo avvio, fai clic su "*Crea account*".

![Image](assets/fr/02.webp)

Scegli un nome per il tuo profilo. Può essere uno pseudonimo o il tuo vero nome.

![Image](assets/fr/03.webp)

Dovrai quindi scegliere tra due modalità di gestione delle notifiche:
- Modalità veloce ("_Firebase Cloud Messaging/Apple Push Notification Service_"): consente di ricevere notifiche di messaggi quasi in tempo reale, grazie ai servizi di notifica forniti da Google o Apple (a seconda del sistema). Affinché ciò funzioni, il tuo indirizzo IP e un ID di notifica univoco vengono trasmessi a Google o Apple, e anche l'ID dell'account di sessione viene registrato presso un server STF (tramite Tor). Questa modalità comporta un'esposizione (certamente minima) dei metadati, ma non compromette il contenuto dei messaggi o i contatti e non consente di tracciare l'attività effettiva dell'utente. Questa modalità è quindi più efficiente in termini di reattività, ma si basa su un'infrastruttura centralizzata ed è leggermente meno efficace in termini di riservatezza.
- Modalità lenta (*background polling*): l'applicazione Session rimane attiva in background, effettuando periodicamente il polling della rete per verificare la presenza di nuovi messaggi. Questo approccio garantisce una maggiore riservatezza rispetto al primo, poiché non vengono trasmessi dati a server di terze parti; né Google, né Apple, né i server STF ricevono alcuna informazione. D'altra parte, questa modalità presenta due svantaggi: le notifiche possono essere ritardate (fino a diversi minuti) e il consumo energetico è generalmente più elevato a causa dell'attività dell'applicazione in background.

![Image](assets/fr/04.webp)

Ora sei connesso all'applicazione Session e puoi iniziare a scambiare messaggi.

![Image](assets/fr/05.webp)


## Salvare l'account della sessione

La prima cosa da fare prima di iniziare a utilizzare Session è salvare il tuo account in modo da poterlo ripristinare in caso di smarrimento del dispositivo. A tal fine, fai clic sul pulsante "*Continua*" accanto a "*Salva la password di ripristino*".

![Image](assets/fr/06.webp)

Session visualizzerà quindi una frase Mnemonic. Copiala con cura e conservatela in un luogo sicuro. Questa frase consente l'accesso completo all'account Session, quindi è importante non divulgarla. Ne avrai bisogno per accedere al tuo account su un altro dispositivo, soprattutto se il tuo telefono attuale viene smarrito o sostituito.

![Image](assets/fr/07.webp)

Questa frase funziona in modo simile alle frasi Mnemonic utilizzate nei portafogli Bitcoin. Ti consiglio quindi di consultare quest'altro tutorial, in cui spiego le migliori pratiche per salvare una frase Mnemonic:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Nota bene**: a differenza delle frasi Mnemonic utilizzate nei portafogli Bitcoin, in Session **è assolutamente necessario salvare ogni parola nella sua interezza**. Le prime 4 lettere non sono sufficienti!


## Impostazione dell'applicazione Session

Per accedere alle impostazioni dell'applicazione, fai clic sulla foto del tuo profilo in alto a sinistra nell'interfaccia. Qui è possibile aggiungere una foto del profilo.

![Image](assets/fr/08.webp)

Nel menu "*Privacy*" puoi attivare o disattivare varie funzioni (attenzione, alcune possono esporre il tuo IP Address). Ti consiglio inoltre di attivare l'opzione "*Blocca app*", che richiede l'autenticazione per accedere all'applicazione.

![Image](assets/fr/09.webp)

Nel menu "*Notifiche*" è possibile scegliere tra "*Modalità veloce*" e "*Modalità lenta*" (vedi le parti precedenti del tutorial). È inoltre possibile personalizzare le notifiche in base alle proprie preferenze.

![Image](assets/fr/10.webp)

Infine, vai nel menu "*Aspetto*" per adattare l'interfaccia ai tuoi gusti. Il menu "*Password di recupero*" consente di recuperare la frase di Mnemonic se desideri effettuare un nuovo backup.

![Image](assets/fr/11.webp)


## Invio di messaggi con Session

Per contattare altre persone, fai clic sul pulsante "*+*" nella pagina iniziale.

![Image](assets/fr/12.webp)

Sono disponibili diverse opzioni. Se desideri creare o unirti a un gruppo, selezionare "*Crea gruppo*" o "*Unisciti alla comunità*".

![Image](assets/fr/13.webp)

Se vuoi che qualcuno ti aggiunga come contatto, puoi fargli scansionare il tuo ID Session come codice QR.

![Image](assets/fr/14.webp)

Per inviare il login a distanza, fai clic su "*Invita un amico*". È quindi possibile copiare il proprio ID di Session e inviarlo tramite un altro canale di comunicazione. È possibile recuperare queste informazioni anche cliccando sulla foto del proprio profilo dalla pagina iniziale.

![Image](assets/fr/15.webp)

Se disponi dell'ID di Session di un'altra persona e desideri aggiungerlo, fai clic su "*Nuovo messaggio*".

![Image](assets/fr/16.webp)

È quindi possibile incollare l'identificativo nel testo o scansionarlo direttamente se disponi di un codice QR.

![Image](assets/fr/17.webp)

Quindi invia un primo messaggio a questa persona.

![Image](assets/fr/18.webp)

Non appena la persona accetta la tua richiesta, vedrai apparire il suo nome utente e potrai chattare liberamente con lei.

![Image](assets/fr/19.webp)


## Sincronizzare il software Desktop

Per sincronizzare l'account sul computer, è necessario installare il software. [Scaricatelo dal sito ufficiale](https://getsession.org/download). Ti consiglio di verificarne l'autenticità e l'integrità prima di installarlo.

![Image](assets/fr/20.webp)

Al primo avvio, fai clic su "*Ho un account*".

![Image](assets/fr/21.webp)

Inserisci la tua frase Mnemonic, assicurandoti di lasciare uno spazio tra ogni parola.

![Image](assets/fr/22.webp)

Ora è possibile accedere alle conversazioni dal computer.

![Image](assets/fr/23.webp)

Congratulazioni, ora hai imparato a usare la messaggistica di Session, un'ottima alternativa a WathsApp!

Ti consiglio anche quest'altro tutorial, in cui presento Threema, un'altra interessante alternativa per la tua applicazione di messaggistica:

https://planb.academy/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74

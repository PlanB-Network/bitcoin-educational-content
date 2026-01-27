---
name: Threema
description: Messaggistica istantanea sicura e anonima
---

![cover](assets/cover.webp)

Fondata nel 2012 in Svizzera, Threema è un'app di messaggistica istantanea progettata per garantire privacy e sicurezza. A differenza di WhatsApp, Telegram o Signal, Threema non richiede alcun numero di telefono o indirizzo e-mail per creare un account. Ogni utente ha un identificativo unico, che consente una registrazione completamente anonima.

Dal punto di vista tecnico, le comunicazioni su Threema sono crittografate end-to-end. Il codice dell'applicazione mobile è open source dal 2020, ma l'infrastruttura del server rimane proprietaria e centralizzata. I server sono ospitati esclusivamente in Svizzera (un Paese rinomato per il suo quadro giuridico in materia di protezione dei dati).

![Image](assets/fr/01.webp)

Threema dispone di client di base per Android e iOS. È disponibile anche un'applicazione web e un software per Windows, Linux e macOS. Tuttavia, per utilizzarli, è necessario registrarsi prima su un dispositivo mobile.

L'applicazione Threema non è gratuita. Funziona con un modello di acquisto una tantum: 5,99 euro per utilizzare l'applicazione a vita (o 4,99 euro se la si acquista direttamente). Per utilizzare davvero Threema in modo anonimo, anche il pagamento deve essere anonimo. Ecco perché è possibile acquistare una chiave di attivazione in bitcoin o in contanti sul "_Threema Shop_" per attivare la versione Android. Su iOS, invece, l'acquisto deve avvenire attraverso l'App Store, a causa delle restrizioni di Apple sulla monetizzazione delle app.

Esiste anche una versione dedicata al business, chiamata "*Threema Work*". In questo tutorial ci concentreremo sulla versione domestica.


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

## Installare l'applicazione Threema

Threema è disponibile su tutte le piattaforme. È possibile scaricare l'applicazione direttamente dall'app store del telefono:
- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Droid](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).

Su Android, è anche possibile [installarla via APK](https://shop.threema.ch/en/download).

Esistono anche [versioni per computer](https://threema.ch/download) (MacOS, Linux e Windows). Questa esercitazione mostra come sincronizzarle.


## Acquista la licenza Threema

Una volta installata l'applicazione, se sei passati direttamente da un app store, hai già pagato la licenza e dovrai avere accesso immediato ad essa. Se invece hai utilizzato F-Droid o l'APK, dovrai acquistare la licenza sul sito ufficiale.

[Vai al "_Negozio Threema_" (https://shop.threema.ch/) e clicca sul pulsante "_Acquista Threema per Android_".

![Image](assets/fr/02.webp)

Selezionate il numero di licenze che desideri acquistare (una sola se è solo per te), scegli la valuta e seleziona il metodo di consegna della licenza. Puoi scegliere di ricevere la licenza via e-mail o direttamente sul sito se desideri rimanere anonimo. Quindi fai clic su "_Procedi al pagamento_".

![Image](assets/fr/03.webp)

Scegliete il metodo di pagamento. Nel mio caso, pagherò in bitcoin, cosa che consiglio anche a te, perché ti permette di rimanere anonimo (a patto che usi bitcoin in modo appropriato) ed è molto più conveniente di un pagamento in contanti a distanza. Quindi clicca su "_Avanti_".

![Image](assets/fr/04.webp)

Se non hai bisogno di un'Invoice, fai di nuovo clic su "_Avanti_" senza inserire alcuna informazione personale.

Conferma poi l'acquisto cliccando su "*Conferma pagamento*".

![Image](assets/fr/05.webp)

Dovrai quindi inviare l'importo indicato all'indirizzo Bitcoin fornito (purtroppo Lightning non è ancora supportato). Una volta confermata la transazione sulla Blockchain, fai clic su "*Chiudi*" accanto all'Invoice.

A questo punto avrai accesso alla chiave di licenza. Attenzione: se non è stato inserito un indirizzo e-mail, la chiave verrà visualizzata solo qui. Ricordati di salvare l'URL della pagina per poterti accedere in seguito, se necessario.

![Image](assets/fr/06.webp)


## Crea un account su Threema

Ora che hai la tua chiave di licenza, puoi finalmente lanciare l'applicazione. Al primo avvio, se non hai acquistato Threema tramite un negozio di applicazioni, ti verrà chiesto di inserire la tua chiave di licenza, acquistata sul sito.

![Image](assets/fr/07.webp)

Quindi fai clic sul pulsante "*Imposta ora*".

![Image](assets/fr/08.webp)

Muovi il dito sullo schermo per generare una fonte di entropia, necessaria per creare il tuo "*Threema ID*".

![Image](assets/fr/09.webp)

A questo punto verrà visualizzato il tuo "*Threema ID*". Esso ti consentirà di contattare altri utenti. Fai clic su "_Avanti_".

![Image](assets/fr/10.webp)

Scegli una password. Essa ti consentirà di ripristinare l'accesso al tuo account in caso di necessità. La password deve essere il più possibile lunga e casuale e deve essere conservata in una copia sicura, ad esempio in un gestore di password.

![Image](assets/fr/11.webp)

Scegli quindi un nome utente, che può essere il tuo vero nome o uno pseudonimo.

![Image](assets/fr/12.webp)

È quindi possibile collegare l'ID Threema al tuo numero di telefono. Questo facilita la ricerca tra i contatti, ma se si utilizza Threema, è anche per preservare l'anonimato: quindi è meglio non collegarlo. Cliccare su "_Avanti_".

![Image](assets/fr/13.webp)

Una volta completato questo passaggio, fai clic su "*Finish*".

![Image](assets/fr/14.webp)

Ora sei connesso a Threema e puoi iniziare a comunicare.

![Image](assets/fr/15.webp)


## Impostazione di Threema

Per prima cosa, accedi alle impostazioni facendo clic sui tre puntini in alto a destra, quindi selezionare "*Impostazioni*".

![Image](assets/fr/16.webp)

Nella scheda "_Privacy_" troverai diverse opzioni da adattare alle tue esigenze:
- Sincronizzazione dei contatti sul telefono;
- Accetta messaggi da persone sconosciute;
- Indicatore di scrittura durante l'inserimento dei dati;
- Avviso di ricevimento dei messaggi...

![Image](assets/fr/17.webp)

Nella scheda "_Sicurezza_", si consiglia di attivare l'opzione "_Meccanismo di blocco_" per proteggere l'accesso all'applicazione. È inoltre consigliabile attivare passphrase per proteggere i backup locali.

![Image](assets/fr/18.webp)

Esplora pure le altre sezioni delle impostazioni per personalizzare l'applicazione in base alle tue preferenze.

![Image](assets/fr/19.webp)


## Backup dell'account Threema

Prima di iniziare a scambiare messaggi, è importante pianificare un modo per recuperare il tuo account, soprattutto se il telefono viene cambiato o perso. Per farlo, clicca sui tre punti in alto a destra dell'interfaccia, quindi accedi al menu "*Backup*".

![Image](assets/fr/20.webp)

Qui sono disponibili due opzioni per il backup dei dati:
- "_Treema sicuro_";
- "Backup dei dati".

"**Threema Safe** salva tutti i dati del tuo account, ad eccezione delle tue conversazioni, sui server di Threema. Questi dati sono criptati con la password scelta al momento della creazione dell'account, in modo che Threema non possa accedervi. I backup vengono effettuati automaticamente e regolarmente.

Con "_Threema Safe_", per ripristinare il tuo account su un nuovo dispositivo, è sufficiente inserire il tuo "*Threema ID*" e la tua password. Se manca una di queste due informazioni, sarà impossibile ripristinare l'account.

Questa opzione consente di recuperare solo l'ID, il profilo, i contatti, i gruppi e alcune impostazioni, ma **non la cronologia delle conversazioni**.

Per attivare "_Threema Safe_", è sufficiente selezionare l'opzione nel menu "_Backup_".

![Image](assets/fr/21.webp)

Se desideri anche eseguire il backup e il ripristino della cronologia delle conversazioni, è necessario utilizzare l'opzione "_Backup dei dati_". Questo genera un backup completo dell'account, memorizzato localmente sul telefono. Sarà necessario trasferire questo backup sul nuovo dispositivo e utilizzare la password (ed eventualmente la passphrase) per ripristinare l'intero account.

Poiché questo backup è solo locale, deve essere copiato regolarmente su un supporto esterno. Altrimenti, in caso di perdita del dispositivo, il recupero sarà impossibile. Questo metodo è quindi più adatto a un trasferimento pianificato da un dispositivo a un altro, piuttosto che a situazioni di emergenza.

Nota bene: "Backup dei dati_" funziona solo se si utilizza lo stesso sistema operativo. Non sarà possibile utilizzarlo, ad esempio, per migrare da un Samsung a un iPhone.

## Personalizzare il proprio profilo Threema

Nell'angolo in alto a sinistra dell'interfaccia, fai clic sull'immagine del tuo profilo, quindi seleziona "_Il mio profilo_".

![Image](assets/fr/22.webp)

Qui è possibile personalizzare il tuo profilo: aggiungi una foto, scegli chi può vederlo o visualizza il tuo login Threema.

![Image](assets/fr/23.webp)


## Sincronizza il software del PC

Se desideri accedere alle conversazioni sul tuo PC, è possibile sincronizzare l'account Threema con il software dedicato. Scarica il software per il tuo sistema operativo [dal sito ufficiale](https://threema.ch/en/download).

![Image](assets/fr/24.webp)

Sul telefono, fai clic sui tre punti in alto a destra, quindi apri il menu "_Threema 2.0 for Desktop_".

![Image](assets/fr/25.webp)

Fai clic su "_Aggiungi dispositivo_", quindi utilizza il telefono per scansionare il codice QR visualizzato dal software sul computer.

![Image](assets/fr/26.webp)

Per confermare la sincronizzazione, fai clic sul gruppo di emoji visualizzato nel software.

![Image](assets/fr/27.webp)

Sul computer, effettua il login utilizzando la password.

![Image](assets/fr/28.webp)

Oltre all'applicazione mobile, è ora possibile accedere al tuo account Threema direttamente dal computer.

![Image](assets/fr/29.webp)


## Inviare messaggi con Threema

Ora che tutto è stato impostato correttamente, si può iniziare a comunicare. Fai clic sul pulsante "_Avvia chat_".

![Image](assets/fr/30.webp)

Seleziona "_Nuovo contatto_".

![Image](assets/fr/31.webp)

Immetti o scansiona il "_Threema ID_" del corrispondente.

![Image](assets/fr/32.webp)

Fai clic sull'icona del messaggio.

![Image](assets/fr/33.webp)

Invia un primo messaggio al tuo corrispondente.

![Image](assets/fr/34.webp)

Quando il tuo corrispondente risponderà, verrà stabilita la connessione e potrai vedere il suo nome e la foto del suo profilo. È quindi possibile inviare messaggi, file multimediali e persino effettuare chiamate.

![Image](assets/fr/35.webp)

Congratulazioni, ora sei in grado di utilizzare la messaggistica di Threema, un'ottima alternativa a WathsApp! Se hai trovato utile questo tutorial, ti sarei molto grato se lasciassi un pollice verde qui sotto. Sentitt libero di condividere questo tutorial sui tuoi social network. Grazie mille!

Ti consiglio anche quest'altro tutorial, in cui ti presento Proton Mail, un'alternativa a Gmail molto più rispettosa della privacy:

https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

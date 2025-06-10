---
name: Threema
description: Messaggistica istantanea sicura e anonima
---
![cover](assets/cover.webp)



Fondata nel 2012 in Svizzera, Threema è un'app di messaggistica istantanea progettata per garantire privacy e sicurezza. A differenza di WhatsApp, Telegram o Signal, Threema non richiede alcun numero di telefono o e-mail Address per creare un account. Ogni utente ha un identificativo unico, che consente una registrazione completamente anonima.



Dal punto di vista tecnico, le comunicazioni su Threema sono crittografate end-to-end. Il codice dell'applicazione mobile è open source dal 2020, ma l'infrastruttura del server rimane proprietaria e centralizzata. I server sono ospitati esclusivamente in Svizzera (un Paese rinomato per il suo quadro giuridico in materia di protezione dei dati).



![Image](assets/fr/01.webp)



Threema dispone di client di base per Android e iOS. È disponibile anche un'applicazione web e un software per Windows, Linux e macOS. Tuttavia, per utilizzarli, è necessario registrarsi prima su un dispositivo mobile.



L'applicazione Threema non è gratuita. Funziona con un modello di acquisto una tantum: 5,99 euro per utilizzare l'applicazione a vita (o 4,99 euro se la si acquista direttamente). Per utilizzare davvero Threema in modo anonimo, anche il pagamento deve essere anonimo. Ecco perché è possibile acquistare una chiave di attivazione in bitcoin o in contanti sul "*Threema Shop*" per attivare la versione Android. Su iOS, invece, l'acquisto deve avvenire attraverso l'App Store, a causa delle restrizioni di Apple sulla monetizzazione delle app.



Esiste anche una versione dedicata al business, chiamata "*Threema Work*". In questo tutorial ci concentreremo sulla versione domestica.



| Applicazione         | E2EE 1:1       | E2EE gruppi    | Registrazione anonima | Licenza client open-source | Licenza server open-source | Server decentralizzato   | Anno di creazione |
| -------------------- | -------------- | -------------- | --------------------- | -------------------------- | -------------------------- | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                     | ❌                          | ❌                          | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                     | ❌                          | ❌                          | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opzionale) | ❌                     | ❌                          | ❌                          | ❌                        | 2011              |
| Telegram             | 🟡 (opzionale) | ❌              | 🟡                    | ✅                          | ❌                          | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                     | ❌                          | ❌                          | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                     | ✅                          | ✅                          | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                     | ✅                          | ❌                          | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                     | ✅                          | ✅                          | 🟡 (federato)           | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                     | ✅                          | N/A                        | 🟡 (tramite email)      | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                     | ✅                          | ✅                          | 🟡 (federato)           | 2014              |
| Session              | ✅              | ✅              | ✅                     | ✅                          | ✅                          | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                     | ✅                          | ✅                          | ✅                        | 2021              |
| Olvid                | ✅              | ✅              | ✅                     | ✅                          | ❌                          | 🟡(nessuna directory)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                     | ❌                          | N/A                        | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                     | ✅                          | N/A                        | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                     | ✅                          | N/A                        | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                     | ✅                          | N/A                        | ✅                        | 2013              |

*E2EE = crittografia end-to-end*



## Installare l'applicazione Threema



Threema è disponibile su tutte le piattaforme. È possibile scaricare l'applicazione direttamente dall'app store del telefono:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



Su Android, è anche possibile [installare via APK](https://shop.threema.ch/en/download).



Esistono anche [versioni per computer](https://threema.ch/download) (MacOS, Linux e Windows). Questa esercitazione mostra come sincronizzarle.



## Acquista la licenza Threema



Una volta installata l'applicazione, se siete passati direttamente da un app store, avete già pagato la licenza e dovreste avere accesso immediato ad essa. Se invece avete utilizzato F-Droid o l'APK, dovrete acquistare la licenza sul sito ufficiale.



[Andare al "*Negozio Threema*" (https://shop.threema.ch/) e cliccare sul pulsante "*Acquista Threema per Android*".



![Image](assets/fr/02.webp)



Selezionate il numero di licenze che desiderate acquistare (una sola se è solo per voi), scegliete la valuta e selezionate il metodo di consegna della licenza. Potete scegliere di ricevere la licenza via e-mail o direttamente sul sito se desiderate rimanere anonimi. Quindi fare clic su "*Procedi al pagamento*".



![Image](assets/fr/03.webp)



Scegliete il metodo di pagamento. Nel mio caso, pagherò in bitcoin, cosa che consiglio anche a voi, perché vi permette di rimanere anonimi (a patto che usiate Bitcoin in modo appropriato) ed è molto più conveniente di un pagamento in contanti a distanza. Quindi cliccate su "*Avanti*".



![Image](assets/fr/04.webp)



Se non avete bisogno di un Invoice, fate di nuovo clic su "*Avanti*" senza inserire alcuna informazione personale.



Confermate poi l'acquisto cliccando su "*Conferma pagamento*".



![Image](assets/fr/05.webp)



Dovrete quindi inviare l'importo indicato al Bitcoin Address fornito (purtroppo Lightning non è ancora supportato). Una volta confermata la transazione sul Blockchain, fare clic su "*Chiudi*" accanto al Invoice.



A questo punto si avrà accesso alla chiave di licenza. Attenzione: se non è stato inserito un indirizzo e-mail Address, la chiave verrà visualizzata solo qui. Ricordarsi di salvare l'URL della pagina per potervi accedere in seguito, se necessario.



![Image](assets/fr/06.webp)



## Crea un account su Threema



Ora che avete la vostra chiave di licenza, potete finalmente lanciare l'applicazione. Al primo avvio, se non avete acquistato Threema tramite un negozio di applicazioni, vi verrà chiesto di inserire la vostra chiave di licenza, acquistata sul sito.



![Image](assets/fr/07.webp)



Quindi fare clic sul pulsante "*Imposta ora*".



![Image](assets/fr/08.webp)



Muovete il dito sullo schermo per generate una fonte di entropia, necessaria per creare il vostro "*Threema ID*".



![Image](assets/fr/09.webp)



A questo punto verrà visualizzato il vostro "*Threema ID*". Esso vi consentirà di contattare altri utenti. Fare clic su "*Avanti*".



![Image](assets/fr/10.webp)



Scegliere una password. Essa vi consentirà di ripristinare l'accesso al vostro account in caso di necessità. La password deve essere il più possibile lunga e casuale e deve essere conservata in una copia sicura, ad esempio in un gestore di password.



![Image](assets/fr/11.webp)



Scegliete quindi un nome utente, che può essere il vostro vero nome o uno pseudonimo.



![Image](assets/fr/12.webp)



È quindi possibile collegare l'ID Threema al proprio numero di telefono. Questo facilita la ricerca tra i contatti, ma se si utilizza Threema, è anche per preservare l'anonimato: quindi è meglio non collegarlo. Cliccare su "*Avanti*".



![Image](assets/fr/13.webp)



Una volta completato questo passaggio, fare clic su "*Finish*".



![Image](assets/fr/14.webp)



Ora siete connessi a Threema e potete iniziare a comunicare.



![Image](assets/fr/15.webp)



## Impostazione di Threema



Per prima cosa, accedere alle impostazioni facendo clic sui tre puntini in alto a destra, quindi selezionare "*Impostazioni*".



![Image](assets/fr/16.webp)



Nella scheda "*Privacy*" troverete diverse opzioni da adattare alle vostre esigenze:




- Sincronizzazione dei contatti sul telefono ;
- Accettare messaggi da persone sconosciute;
- Indicatore di scrittura durante l'inserimento dei dati ;
- Avviso di ricevimento dei messaggi...



![Image](assets/fr/17.webp)



Nella scheda "*Sicurezza*", si consiglia di attivare l'opzione "*Meccanismo di blocco*" per proteggere l'accesso all'applicazione. È inoltre consigliabile attivare passphrase per proteggere i backup locali.



![Image](assets/fr/18.webp)



Esplorate pure le altre sezioni delle impostazioni per personalizzare l'applicazione in base alle vostre preferenze.



![Image](assets/fr/19.webp)



## Backup dell'account Threema



Prima di iniziare a scambiare messaggi, è importante pianificare un modo per recuperare il proprio account, soprattutto se il telefono viene cambiato o perso. Per farlo, cliccate sui tre punti in alto a destra di Interface, quindi accedete al menu "*Backup*".



![Image](assets/fr/20.webp)



Qui sono disponibili due opzioni per il backup dei dati:




- "*Treema sicuro*";
- "Backup dei dati*".



"Threema Safe* salva tutti i dati del vostro account, ad eccezione delle vostre conversazioni, sui server di Threema. Questi dati sono criptati con la password scelta al momento della creazione dell'account, in modo che Threema non possa accedervi. I backup vengono effettuati automaticamente e regolarmente.



Con "*Threema Safe*", per ripristinare il proprio account su un nuovo dispositivo, è sufficiente inserire il proprio "*Threema ID*" e la propria password. Se manca una di queste due informazioni, sarà impossibile ripristinare l'account.



Questa opzione consente di recuperare solo l'ID, il profilo, i contatti, i gruppi e alcune impostazioni, ma **non la cronologia delle conversazioni**.



Per attivare "*Threema Safe*", è sufficiente selezionare l'opzione nel menu "*Backup*".



![Image](assets/fr/21.webp)



Se si desidera anche eseguire il backup e il ripristino della cronologia delle conversazioni, è necessario utilizzare l'opzione "*Backup dei dati*". Questo genera un backup completo dell'account, memorizzato localmente sul telefono. Sarà necessario trasferire questo backup sul nuovo dispositivo e utilizzare la password (ed eventualmente il passphrase) per ripristinare l'intero account.



Poiché questo backup è solo locale, deve essere copiato regolarmente su un supporto esterno. Altrimenti, in caso di perdita del dispositivo, il recupero sarà impossibile. Questo metodo è quindi più adatto a un trasferimento pianificato da un dispositivo a un altro, piuttosto che a situazioni di emergenza.



Nota bene: "*Backup dei dati*" funziona solo se si utilizza lo stesso sistema operativo. Non sarà possibile utilizzarlo, ad esempio, per migrare da un Samsung a un iPhone.



## Personalizzare il proprio profilo Threema



Nell'angolo in alto a sinistra di Interface, fare clic sull'immagine del proprio profilo, quindi selezionare "*Il mio profilo*".



![Image](assets/fr/22.webp)



Qui è possibile personalizzare il proprio profilo: aggiungere una foto, scegliere chi può vederlo o visualizzare il proprio login Threema.



![Image](assets/fr/23.webp)



## Sincronizzare il software del PC



Se si desidera accedere alle conversazioni sul proprio PC, è possibile sincronizzare l'account Threema con il software dedicato. Scaricare il software per il proprio sistema operativo [dal sito ufficiale](https://threema.ch/en/download).



![Image](assets/fr/24.webp)



Sul telefono, fare clic sui tre punti in alto a destra, quindi aprire il menu "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Fare clic su "*Aggiungi dispositivo*", quindi utilizzare il telefono per scansionare il codice QR visualizzato dal software sul computer.



![Image](assets/fr/26.webp)



Per confermare la sincronizzazione, fare clic sul gruppo di emoji visualizzato nel software.



![Image](assets/fr/27.webp)



Sul computer, effettuare il login utilizzando la password.



![Image](assets/fr/28.webp)



Oltre all'applicazione mobile, è ora possibile accedere al proprio account Threema direttamente dal computer.



![Image](assets/fr/29.webp)



## Inviare messaggi con Threema



Ora che tutto è stato impostato correttamente, si può iniziare a comunicare. Fare clic sul pulsante "*Avvia chat*".



![Image](assets/fr/30.webp)



Selezionare "*Nuovo contatto*".



![Image](assets/fr/31.webp)



Immettere o scansionare il "*Threema ID*" del corrispondente.



![Image](assets/fr/32.webp)



Fare clic sull'icona del messaggio.



![Image](assets/fr/33.webp)



Inviate un primo messaggio al vostro corrispondente.



![Image](assets/fr/34.webp)



Quando il vostro corrispondente risponderà, verrà stabilita la connessione e potrete vedere il suo nome e la foto del suo profilo. È quindi possibile inviare messaggi Exchange, file multimediali e persino effettuare chiamate.



![Image](assets/fr/35.webp)



Congratulazioni, ora siete in grado di utilizzare la messaggistica di Threema, un'ottima alternativa a WathsApp! Se hai trovato utile questo tutorial, ti sarei molto grato se lasciassi un pollice Green qui sotto. Sentitevi liberi di condividere questo tutorial sui vostri social network. Grazie mille!



Vi consiglio anche quest'altro tutorial, in cui vi presento Proton Mail, un'alternativa a Gmail molto più rispettosa della privacy:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
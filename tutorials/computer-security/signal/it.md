---
name: Segnale
description: Esprimetevi liberamente
---
![cover](assets/cover.webp)



Signal è un'applicazione di messaggistica crittografata end-to-end, progettata per offrire una buona riservatezza di default. Ogni messaggio, chiamata e file è protetto dal protocollo Signal, riconosciuto come uno dei più robusti protocolli di messaggistica. Viene riutilizzato da molte altre applicazioni, tra cui WathsApp, Facebook Messenger, Skype e Google Messages per le comunicazioni RCS.



Signal è stato lanciato nel 2014 da Moxie Marlinspike (pseudonimo) e sviluppato dal 2018 dalla Signal Foundation, un'organizzazione no-profit creata con il supporto di Brian Acton (co-fondatore di WhatsApp).



![Image](assets/fr/01.webp)



Rispetto a WhatsApp, Signal si distingue per la sua trasparenza: il codice dell'applicazione, sia lato client che server, è interamente open source. Ciò consente a chiunque di verificarlo e, in particolare, di controllare che la crittografia sia applicata come pubblicizzato.



Tuttavia, Signal si basa sull'utilizzo di un numero di telefono, che rappresenta il suo principale punto debole in termini di anonimato rispetto ad altre soluzioni. Nonostante ciò, l'applicazione è, a mio avviso, una delle più affidabili in termini di sicurezza e riservatezza, grazie alla sua architettura completamente aperta e a un protocollo di crittografia ampiamente adottato, e quindi testato e verificato, a differenza di altre applicazioni più marginali.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| **Signal**           | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = crittografia end-to-end*




## Installare l'applicazione Signal



Signal è disponibile su tutte le piattaforme. È possibile scaricare l'applicazione direttamente dal negozio di applicazioni del telefono:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669);



Su Android, è anche possibile [installare via APK](https://github.com/signalapp/Signal-Android/releases).



In questa guida ci concentreremo sulla versione mobile, ma ricordiamo che [sono disponibili anche le versioni desktop](https://signal.org/fr/download/) (MacOS, Linux e Windows). Tuttavia, prima di poter sincronizzare il proprio account con la versione desktop, è necessario configurare l'applicazione mobile.



## Creare un account su Signal



Quando si avvia l'applicazione per la prima volta, fare clic sul pulsante "*Continua*".



![Image](assets/fr/02.webp)



Immettere il numero di telefono, quindi fare clic su "*Avanti*".



![Image](assets/fr/03.webp)



Un codice di verifica vi sarà inviato via SMS. Inserite questo codice nell'applicazione Signal.



![Image](assets/fr/04.webp)



Scegliete un codice PIN per proteggere il vostro account Signal. Questo codice cripta i vostri dati e può essere utilizzato per ripristinare l'accesso al vostro account in caso di smarrimento del dispositivo. È quindi importante scegliere un codice PIN robusto, il più lungo e casuale possibile, e conservarlo in modo affidabile.



![Image](assets/fr/05.webp)



Confermare il codice PIN una seconda volta.



![Image](assets/fr/06.webp)



È ora possibile personalizzare il proprio profilo utente. Scegliete una foto, inserite il vostro nome o un nickname. In questa fase, potete anche definire chi può trovarvi su Signal tramite il vostro numero. Selezionate "*Tutti*" se volete essere visibili, oppure "*Nessuno*" per non essere rintracciabili tramite il numero di telefono (potrete essere aggiunti solo con il vostro "*Nome utente*"). Dopo aver effettuato le selezioni, cliccate su "*Avanti*".



![Image](assets/fr/07.webp)



Ora siete connessi a Signal e siete pronti per i messaggi Exchange.



![Image](assets/fr/08.webp)



## Impostazione dell'account Signal



Cliccate sulla foto del vostro profilo nell'angolo in alto a sinistra per accedere alle impostazioni dell'applicazione.



![Image](assets/fr/09.webp)



Il menu "*Account*" consente di gestire le impostazioni del profilo. Vi consiglio di mantenere le impostazioni predefinite. È inoltre possibile attivare l'opzione "*Blocco registrazione*", che protegge l'account da alcuni tipi di attacco. Questo menu contiene anche le opzioni necessarie per trasferire l'account su un nuovo dispositivo.



![Image](assets/fr/10.webp)



Facendo nuovamente clic sull'immagine del profilo nelle impostazioni, si accede alle opzioni di personalizzazione del profilo. Vi consiglio di impostare un "*nome utente*": questo vi permetterà di mettervi in contatto con altre persone senza rivelare il vostro numero di telefono.



![Image](assets/fr/11.webp)



Selezionando "*codice QR o link*", otterrete le informazioni necessarie da condividere con chi vuole aggiungervi a Signal.



![Image](assets/fr/12.webp)



Il menu "*Privacy*" è particolarmente importante. Qui troverete le opzioni per controllare la visibilità del vostro numero, la gestione dei messaggi con i vostri contatti e le varie autorizzazioni concesse all'applicazione.



![Image](assets/fr/13.webp)



E sentitevi liberi di esplorare i menu "*Apparenza*", "*Chat*" e "*Notifiche*" per adattare Interface e il funzionamento dell'applicazione alle vostre esigenze personali.



## Applicazione desktop Connect



Per collegare l'applicazione desktop, iniziare installando il software sul computer (vedere la prima parte di questa guida). Quindi, sul telefono, andare su Impostazioni e aprire la sezione "*Dispositivi collegati*".



![Image](assets/fr/14.webp)



Fare clic sul pulsante "*Collega un nuovo dispositivo*".



![Image](assets/fr/15.webp)



Sul computer, avviare il software, quindi scansionare il codice QR visualizzato sullo schermo utilizzando il telefono. Se si desidera importare le conversazioni, selezionare l'opzione "*Trasferimento della cronologia dei messaggi*".



![Image](assets/fr/16.webp)



I dispositivi sono ora completamente sincronizzati.



![Image](assets/fr/17.webp)



## Inviare messaggi con Signal



Per comunicare con qualcuno su Signal, è necessario aggiungerlo come contatto. Ci sono diverse opzioni: è possibile aggiungerlo tramite il suo numero di telefono (se la persona ha attivato l'opzione per essere trovata con questo mezzo), oppure utilizzare il suo ID Signal.



Fare clic sull'icona della matita nell'angolo in basso a destra del Interface.



![Image](assets/fr/18.webp)



Nel mio caso, voglio aggiungere la persona in base al nome utente. Faccio quindi clic su "*Trova per nome utente*".



![Image](assets/fr/19.webp)



È quindi possibile incollare il suo login o scansionare il suo codice QR.



![Image](assets/fr/20.webp)



Inviategli un messaggio per stabilire un contatto.



![Image](assets/fr/21.webp)



La conversazione apparirà nella pagina iniziale. Se la persona accetta la vostra richiesta di contatto, vedrete il suo nome e la foto del suo profilo.



![Image](assets/fr/22.webp)



Congratulazioni, ora siete in grado di utilizzare la messaggistica di Signal, un'ottima alternativa a WathsApp! Se avete trovato utile questo tutorial, vi sarei molto grato se lasciaste un pollice Green qui sotto. Sentitevi liberi di condividere questa guida sui vostri social network. Grazie mille!



Vi consiglio anche quest'altro tutorial, in cui vi presento Proton Mail, un'alternativa a Gmail molto più rispettosa della privacy:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
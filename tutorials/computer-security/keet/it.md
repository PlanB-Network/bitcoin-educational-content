---
name: Keet
description: Chat peer-to-peer
---
![cover](assets/cover.webp)



Keet è un'applicazione di messaggistica istantanea progettata per funzionare senza server. Lanciata nel 2022 da Holepunch (una società finanziata da Tether e Bitfinex), l'applicazione si basa interamente su una rete peer-to-peer e presenta un approccio radicalmente decentralizzato: messaggi, chiamate e file vengono scambiati direttamente tra gli utenti, senza intermediari.



Keet cripta tutte le comunicazioni end-to-end e non richiede dati personali. La registrazione è anonima, non è richiesto alcun numero di telefono o e-mail. Oltre allo scambio di messaggi di testo, Keet offre videochiamate di altissima qualità e la condivisione illimitata di file. L'applicazione può quindi essere utilizzata in modo ibrido, sia per uso personale che professionale.



![Image](assets/fr/01.webp)



Al momento (aprile 2025), Keet non è completamente open-source. Parte del codice sorgente è disponibile su [Holepunch's GitHub repository](https://github.com/holepunchto), in particolare i componenti crittografici e di rete, ma il client Interface non lo è ancora. Holepunch ha comunque annunciato l'intenzione di rendere l'intera applicazione open-source. A seconda di quando si scopre questo tutorial, questo potrebbe essere già stato fatto.




| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| **Keet**             | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = crittografia end-to-end*



## Installare Keet



Keet è disponibile su tutte le piattaforme. È possibile scaricare l'applicazione direttamente dall'app store del telefono:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



Su Android, è anche possibile [installare via APK](https://github.com/holepunchto/keet-mobile-releases/releases).



In questo tutorial ci concentreremo sulla versione mobile, ma ricordiamo che [sono disponibili anche le versioni per computer](https://keet.io/) (MacOS, Linux e Windows). È anche possibile sincronizzare il proprio account su più dispositivi.



## Crea un account su Keet



Al primo avvio, è possibile ignorare le schermate di presentazione.



![Image](assets/fr/02.webp)



Fare clic sul pulsante "*Sono un nuovo utente*".



![Image](assets/fr/03.webp)



Accettare le condizioni d'uso, quindi fare clic su "*Configurazione rapida*".



![Image](assets/fr/04.webp)



Scegliere un nome o un nickname, quindi fare clic su "*Finish setup*".



![Image](assets/fr/05.webp)



Il profilo è stato creato. Cliccare nuovamente su "*Finish setup*" per finalizzare.



![Image](assets/fr/06.webp)



È possibile personalizzare il proprio profilo in qualsiasi momento dalla scheda "*Profilo*".



## Salva il tuo account Keet



La prima cosa da fare con il vostro nuovo account Keet è salvare la vostra frase di recupero. Si tratta di una sequenza di 24 parole che vi permetterà di ripristinare l'accesso al vostro account in caso di smarrimento o cambio di dispositivo. Questa frase dà pieno accesso al vostro account a chiunque la conosca, quindi è importante fare un backup affidabile e non divulgarlo mai.



A questo scopo, fare clic sulla scheda "*Profilo*" in basso a destra del Interface.



![Image](assets/fr/07.webp)



Accedere quindi al menu "*Impostazioni*".



![Image](assets/fr/08.webp)



Selezionare "*Privacy e sicurezza*".



![Image](assets/fr/09.webp)



Quindi fare clic su "*Frase di recupero*".



![Image](assets/fr/10.webp)



Premete il pulsante "*Vedi frase*" per visualizzare la vostra frase di recupero. Copiatela con cura e conservatela in un luogo sicuro.



![Image](assets/fr/11.webp)



## Inviare messaggi con Keet



Per comunicare su Keet, è necessario creare delle "*Camere*". Per farlo, cliccate sull'icona della matita in alto a destra del Interface.



![Image](assets/fr/12.webp)



Selezionare "*Nuova chat di gruppo*".



![Image](assets/fr/13.webp)



Scegliete un nome e una descrizione per la vostra "*Sala*", quindi fate clic su "*Crea chat di gruppo*".



![Image](assets/fr/14.webp)



La vostra "*Sala*" è stata creata. Fare clic sull'icona "*+*" in alto a destra per invitare i partecipanti.



![Image](assets/fr/15.webp)



Definite i diritti che concedete ai nuovi membri tramite il link di invito, nonché la durata della validità del link. Cliccare quindi su "*Invito generate*".



![Image](assets/fr/16.webp)



Keet invierà a generate un link per unirsi alla vostra "*Sala*". È possibile copiarlo e condividerlo, oppure far scansionare il codice QR alle persone che si desidera invitare.



![Image](assets/fr/17.webp)



Ora è possibile iniziare a scambiare messaggi e file multimediali. Per avviare una chiamata, fare clic sull'icona del telefono nell'angolo in alto a destra.



![Image](assets/fr/18.webp)



Da questo gruppo è anche possibile inviare messaggi privati a un membro specifico. Fare clic sull'immagine del profilo del gruppo, quindi selezionare il membro desiderato nella sezione "*Membri*".



![Image](assets/fr/19.webp)



Fare clic sul pulsante "*Invia richiesta DM*" e inserire il messaggio.



![Image](assets/fr/20.webp)



Una volta accettata la richiesta di DM, troverete questo contatto nella pagina iniziale, dove potrete parlargli privatamente.



![Image](assets/fr/21.webp)



## Sincronizzate il vostro account su più dispositivi



Ora che sapete come usare Keet e avete un account, potete anche sincronizzarlo su un altro dispositivo, ad esempio un computer. Per farlo, aprite l'applicazione sul cellulare, quindi cliccate su "*Profilo*" e accedete a "*Impostazioni*".



![Image](assets/fr/22.webp)



Andate quindi al menu "*I miei dispositivi*".



![Image](assets/fr/23.webp)



Fare clic su "*Aggiungi dispositivo*". Keet visualizzerà un link per sincronizzare un nuovo dispositivo. Copiare questo link.



![Image](assets/fr/24.webp)



Sul secondo dispositivo, installare Keet. Nella schermata iniziale, selezionare l'opzione "*Sono un utente corrente*".



![Image](assets/fr/25.webp)



Quindi fare clic su "*Collegamento dispositivo*".



![Image](assets/fr/26.webp)



Incollare il link fornito dal primo dispositivo, quindi fare clic su "*Avvia sincronizzazione*".



![Image](assets/fr/27.webp)



Sul primo dispositivo, fare clic su "*Conferma collegamento dispositivi*" per autorizzare la connessione.



![Image](assets/fr/28.webp)



Sul secondo dispositivo, completare la procedura facendo clic su "*Collegamento dispositivi*".



![Image](assets/fr/29.webp)



Ora potete accedere a tutte le vostre "*Camere*" e conversazioni da questo nuovo dispositivo.



![Image](assets/fr/30.webp)



Congratulazioni, ora siete in grado di utilizzare la messaggistica di Keet, un'ottima alternativa a WathsApp! Se avete trovato utile questo tutorial, vi sarei molto grato se lasciaste un pollice Green qui sotto. Sentitevi liberi di condividere questo tutorial sui vostri social network. Grazie mille!



Vi consiglio anche quest'altro tutorial, in cui vi presento Proton Mail, un'alternativa a Gmail molto più rispettosa della privacy:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
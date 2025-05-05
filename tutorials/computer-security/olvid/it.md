---
name: Olvid
description: Messaggistica privata per tutti
---
![cover](assets/cover.webp)



Olvid è un'applicazione di messaggistica istantanea francese lanciata nel 2019, progettata per offrire un alto livello di sicurezza, senza compromettere la privacy. A differenza di WhatsApp o Signal, Olvid non chiede alcun dato personale al momento della registrazione: nessun numero di telefono, nessuna email, nulla. L'identificazione tra gli utenti si basa su un Exchange di chiavi, senza server di directory o libro Address condiviso.



Tutti i messaggi sono crittografati end-to-end utilizzando un protocollo crittografico originale, progettato per proteggere anche i metadati: nessuno sa con chi si sta parlando, né quando. Il codice del client è open source, ma il server centrale utilizzato per instradare i messaggi crittografati rimane proprietario e ospitato su AWS.



Olvid offre una versione gratuita e una in abbonamento a 4,99 euro al mese. La versione gratuita offre tutte le funzionalità, ad eccezione dell'esecuzione di chiamate audio e video (anche se è possibile riceverle), e non consente la sincronizzazione dell'account su più dispositivi. Quindi, se avete intenzione di utilizzare esclusivamente il vostro smartphone e non avete bisogno di effettuare chiamate, Olvid è una soluzione eccellente.



Olvid è certificato dall'ANSSI (l'autorità francese per la sicurezza informatica). Questa applicazione è un'ottima alternativa ai servizi di messaggistica tradizionali (WhatsApp, Facebook Messenger, WeChat...) per chi cerca la privacy pur mantenendo la semplicità d'uso.



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
| **Olvid**                | **✅**              | **✅**              | **✅**                   | **✅**                          | **❌**                           | **❌**                    | **2019**              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = crittografia end-to-end*



## Installare l'applicazione Olvid



Olvid è disponibile su tutte le piattaforme. È possibile scaricare l'applicazione direttamente dall'app store del telefono:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);



Su Android, è anche possibile [installare via APK](https://www.olvid.io/download/).



In questo tutorial ci concentreremo sulla versione mobile, ma vi ricordiamo che [sono disponibili anche versioni per computer](https://www.olvid.io/download/) (MacOS, Linux e Windows). Se scegliete la versione a pagamento, potrete sincronizzare il vostro account su più dispositivi.



![Image](assets/fr/01.webp)



## Creare un account su Olvid



Quando si avvia l'applicazione per la prima volta, fare clic sul pulsante "*Sono un nuovo utente*".



![Image](assets/fr/02.webp)



Scegliete un nickname o inserite il vostro nome e cognome.



![Image](assets/fr/03.webp)



Aggiungere una foto del profilo.



![Image](assets/fr/04.webp)



Il vostro account è stato creato.



![Image](assets/fr/05.webp)



Per evitare di perdere l'accesso al vostro account Olvid, vi consigliamo di impostare dei backup automatici. A tal fine, aprire le impostazioni facendo clic sui tre punti in alto a destra di Interface, quindi selezionare "*Impostazioni*".



![Image](assets/fr/06.webp)



Accedere al menu "*Salva chiavi e contatti*".



![Image](assets/fr/07.webp)



Quindi fare clic su "*generate una chiave di backup*". Questa chiave cripterà i vostri backup. Se dovete ripristinare il vostro account su un altro dispositivo e non avete più accesso ad esso, avrete bisogno sia di un backup che di questa chiave per decifrarlo.



![Image](assets/fr/08.webp)



Conservare la chiave in un luogo sicuro. Potete anche farne una copia cartacea.



![Image](assets/fr/09.webp)



Si può quindi scegliere di creare un backup locale o un backup automatico su un servizio cloud. Questa seconda opzione è altamente consigliata per garantire l'accesso al proprio account Olvid in ogni circostanza, anche in caso di smarrimento del telefono.



![Image](assets/fr/10.webp)



Assicurarsi che l'opzione "*Attiva il backup automatico*" sia selezionata.



![Image](assets/fr/11.webp)



È inoltre possibile esplorare le altre impostazioni disponibili per personalizzare l'applicazione in base alle proprie esigenze.



![Image](assets/fr/12.webp)



## Inviare messaggi con Olvid



Per poter inviare messaggi, è necessario aggiungere i contatti. Dalla pagina iniziale, fare clic sul pulsante blu "*+*".



![Image](assets/fr/13.webp)



Olvid visualizza quindi il vostro ID utente. Potete quindi trasmetterlo alle persone con cui desiderate comunicare, in modo che possano aggiungervi come contatto.



Per aggiungere una persona, scansionare il suo documento d'identità con la fotocamera o incollarlo manualmente facendo clic sui tre puntini in alto a destra.



![Image](assets/fr/14.webp)



Una volta scansionato l'ID, è possibile chiedere al proprio contatto di scansionare il codice QR visualizzato, oppure inviargli una richiesta di connessione remota facendo clic su "*Contatto remoto*".



![Image](assets/fr/15.webp)



La connessione è ora stabilita.



![Image](assets/fr/16.webp)



Ora potete iniziare a scambiare messaggi e altri contenuti con il vostro corrispondente!



![Image](assets/fr/17.webp)



Dalla pagina iniziale, troverete tutte le vostre conversazioni.



![Image](assets/fr/18.webp)



La seconda scheda contiene tutti i contatti.



![Image](assets/fr/19.webp)



È anche possibile creare discussioni di gruppo.



![Image](assets/fr/20.webp)



Congratulazioni, ora siete in grado di utilizzare la messaggistica di Olvid, un'ottima alternativa a WathsApp! Se avete trovato utile questo tutorial, vi sarei molto grato se lasciaste un pollice Green qui sotto. Sentitevi liberi di condividere questo tutorial sui vostri social network. Grazie mille!



Vi consiglio anche quest'altro tutorial, in cui vi presento Proton Mail, un'alternativa a Gmail molto più rispettosa della privacy:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
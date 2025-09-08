---
name: Tossico
description: Aprire conversazioni senza intermediari sul protocollo decentralizzato Tox
---
![cover](assets/cover.webp)



La crittografia end-to-end è un servizio offerto da molte app di messaggistica come WhatsApp e Telegram. Per crittografia si intende che il messaggio, prima di essere inviato dal mittente, viene protetto da un blocco crittografico di cui solo il destinatario possiede la chiave. Oggi andiamo a scoprire un'applicazione di messaggistica crittografata end-to-end totalmente decentralizzata, basata su principi simili a Blockchain, per offrire una comunicazione sicura e crittografata end-to-end senza intermediari: Tox Chat.



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
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = crittografia end-to-end*



## Che cos'è il Tox?



Tox è un protocollo di comunicazione decentralizzato e gratuito (open source) che utilizza la tecnologia *Networking and Cryptography Library* (NaCl) e combinazioni di algoritmi di crittografia per garantire la sicurezza e la riservatezza dei suoi utenti. Tox consente di inviare messaggi di testo Exchange, effettuare chiamate audio e video, condividere file e condividere il proprio schermo con gli amici in modo sicuro, decentralizzato e senza intermediari.



La tecnologia utilizzata dal protocollo Tox è simile alle reti peer-to-peer come le blockchain, che favoriscono la decentralizzazione dell'infrastruttura del protocollo. A differenza dei social network e delle applicazioni di messaggistica crittografata end-to-end, l'applicazione Tox Chat è costruita su un protocollo decentralizzato che non ha un server centrale. Tutti gli utenti comunicano in una rete peer-to-peer priva di intermediari e resistente alla censura. Per comunicare, ogni utente è identificato da un ID univoco (ToxID) derivato dalla sua chiave pubblica, memorizzata in una tabella Hash distribuita.



## Unisciti a Tox



È possibile utilizzare il protocollo Tox attraverso un client di messaggistica istantanea scaricabile dal sito [Tox Chat](https://tox.chat).



![download](assets/fr/01.webp)



A seconda del sistema operativo, è possibile scaricare e installare un client Tox che corrisponda a:





- aTox: [aTox](https://github.com/evilcorpltd/aTox), un client Tox scritto in Kotlin disponibile solo su Android



![aTox](assets/fr/02.webp)





- qTox: Un client Tox di [open source](https://github.com/TokTok/qTox) basato sul Qt Framework (C++) disponibile su Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) è un client Tox scritto in C e funzionante su sistemi con interfaccia a riga di comando.



![Toxic](assets/fr/04.webp)



In questa esercitazione, utilizzeremo i client qTox su Windows e aTox per comunicare.



## Come iniziare con qTox



Una volta scaricato, installate il vostro client Tox e create il vostro profilo.



![qTox-acount](assets/fr/05.webp)



Congratulazioni, siete appena entrati a far parte del protocollo Tox. Nel software qTox, potete trovare le informazioni del vostro profilo cliccando sul vostro nome utente.



![profil](assets/fr/06.webp)



In particolare, troverete il vostro Tox ID, che potrete salvare come codice QR e condividere con chi vuole mettersi in contatto con voi.



Esportare il file del profilo Tox per avere un backup del profilo e delle informazioni di contatto da utilizzare per il ripristino. Fare clic sul pulsante **Esporta**, quindi scegliere il percorso del file di backup.



![export](assets/fr/07.webp)



Dal menu **Altro** è possibile aggiungere amici, importare contatti e gestire le richieste di amicizia ricevute.



![friends](assets/fr/08.webp)



Potete contattarmi tramite questo Tox ID, ad esempio: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Una volta inviata la richiesta di amicizia, il destinatario dovrà accettare o rifiutare la richiesta prima di poterlo contattare.



![request](assets/fr/09.webp)



Il client Tox include tutte le opzioni offerte dalle applicazioni di messaggistica istantanea:





- Videochiamate





- Chiamate vocali





- Condivisione di file





- emoji



![chat](assets/fr/10.webp)



### Gruppi peer-to-peer



I vostri client Tox vi permettono anche di comunicare con un gruppo di persone in modo completamente decentralizzato: si tratta delle cosiddette conferenze. Nel menu **Gruppi**, create una nuova conferenza o consultate l'elenco degli inviti a partecipare alle conferenze che avete ricevuto.



![conferences](assets/fr/11.webp)



Una volta creata la conferenza, è possibile invitare gli amici a partecipare alla conferenza sul client Tox. Nell'elenco degli amici, fare clic con il tasto destro del mouse sul nome utente dell'amico che si desidera invitare. Fare clic sull'opzione **Invita alla conferenza**, quindi selezionare il nome della conferenza creata. È possibile invitare un amico anche creando implicitamente una conferenza con l'opzione **Crea una nuova conferenza**.



⚠️ I client Tox sono ancora in fase di sviluppo, pertanto è possibile che si verifichino errori durante l'interazione con il software. Le funzioni di conferenza e di videochiamata non sono ancora disponibili sul client Tox per Android (aTox).



![invite](assets/fr/12.webp)



### Trasferimenti di file



Nel menu **Trasferimenti di file** si trova la cronologia dei file inviati e ricevuti dai propri contatti.



![files](assets/fr/13.webp)



È inoltre possibile personalizzare le configurazioni di condivisione dei file per ogni discussione. Fate clic con il tasto destro del mouse sul nome utente del destinatario e selezionate "Mostra altri dettagli".



![details](assets/fr/14.webp)



Dai dettagli di Interface, è possibile gestire le autorizzazioni concesse al destinatario per:





- Accettazione automatica degli inviti alle conferenze.





- Accettazione automatica dei file.





- Percorsi di backup per i file di discussione.



![permissions](assets/fr/15.webp)



### Altri parametri



Nel menu **Impostazioni** è possibile personalizzare le impostazioni del client Tox.





- Nella sezione **Generale**, modificare la lingua di base del client Tox, definire i percorsi dei file di backup e la dimensione massima dei file da accettare automaticamente.



![general](assets/fr/16.webp)





- Nella sezione **Utente Interface**, modificare i caratteri e le dimensioni dei messaggi. È inoltre possibile modificare il tema del client Tox.



![ui](assets/fr/17.webp)





- La scheda **Privacy** consente di definire i messaggi effimeri deselezionando la casella "Keep chat history". È anche possibile cambiare il codice Nospam quando ci si accorge di essere sommersi da richieste di amicizia facendo clic sul pulsante "generate codice NoSpam casuale".



![privacy](assets/fr/18.webp)



### Cosa garantisce la riservatezza sui Tox?



Il protocollo Tox utilizza la Distributed Hash Table per creare una rete di nodi decentralizzati. Ogni client Tox fa parte della rete DHT e memorizza informazioni sugli altri nodi. Nel caso di Tox, il DHT memorizza gli indirizzi IP come valori associati alle chiavi pubbliche Tox (Tox ID). In questo modo è facile cercare un dispositivo Tox Client senza dover interrogare un server centrale.



Immaginate di scrivere al nostro utente `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` che chiameremo **utente B**. Il client Tox individua questo identificatore nella tabella Hash Distributed e recupera l'IP Address associato. Una volta trovato l'IP Address, il client Tox creerà un canale di comunicazione diretto e crittografato con la macchina dell'**utente B**, oppure utilizzerà altri nodi come relè per raggiungere l'**utente B**. Gli algoritmi di crittografia assicurano che, indipendentemente dal canale di comunicazione, solo **Utente B** sarà in grado di leggere il contenuto del messaggio.



Se vi è piaciuto scoprire Tox e siete riusciti a capire come è utile per rafforzare la vostra privacy, non esitate a dare un pollice in su a questo tutorial. Vi consigliamo anche il nostro tutorial su Simple Login, uno strumento che consente di ricevere e inviare e-mail in modo anonimo.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41
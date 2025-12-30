---
name: PearPass
description: Riprendete il controllo delle vostre password con un gestore di password locale, peer-to-peer e senza cloud
---

![cover](assets/cover.webp)



In un'epoca in cui ogni individuo gestisce decine o addirittura centinaia di account online, la sicurezza dei login è diventata una questione centrale nella sicurezza informatica. Social network, sistemi di messaggistica, servizi professionali, piattaforme finanziarie: ognuno di questi accessi si basa su un segreto, la cui compromissione può avere gravi conseguenze per la vostra vita.



Eppure, nonostante il numero crescente di attacchi, le cattive pratiche rimangono diffuse tra la popolazione: password deboli, password riutilizzate, password memorizzate in chiaro o approssimativamente memorizzate. Per risolvere questi problemi senza complicarsi la vita quotidiana, la soluzione è utilizzare un password manager.



Esistono già decine di gestori di password e Plan ₿ Academy offre un tutorial per la maggior parte di essi. Ma in questo tutorial vorrei presentarvene uno che si distingue chiaramente dagli altri per il suo funzionamento: **PearPass**.



**PearPass è un gestore di password open-source, local-first e peer-to-peer, progettato per dare agli utenti un controllo totale sui propri dati



![Image](assets/fr/01.webp)



## Perché scegliere PearPass?



Un password manager è un programma software che genera, memorizza e organizza tutte le password in modo sicuro. Invece di memorizzare o riutilizzare le password, avete un solo segreto da proteggere: la master password, che cripta l'intera cassaforte. Questo approccio consente di utilizzare password uniche, lunghe e casuali per ogni servizio, riducendo il rischio di dimenticanza e di compromissione e limitando l'impatto di un'eventuale fuga di notizie. Oggi è uno strumento informatico di base che tutti dovrebbero utilizzare.



Esistono due categorie principali di password manager. Da un lato, c'è il software solo locale, molto sicuro perché i dati non vengono mai memorizzati su un server centrale, ma poco pratico, perché non consente di sincronizzare facilmente le credenziali tra diversi dispositivi (computer, smartphone, tablet...). D'altra parte, i gestori di password basati sul cloud memorizzano le credenziali sui loro server e le sincronizzano su tutti i dispositivi. Il loro principale vantaggio è la comodità, ma comportano un compromesso sulla sicurezza, poiché le vostre password sono memorizzate su infrastrutture su cui non avete alcun controllo.



PearPass rompe deliberatamente con entrambi i modelli. Si posiziona tra i gestori locali e le soluzioni cloud: consente la sincronizzazione delle password, pur garantendo che non vengano mai memorizzate su server remoti. Di conseguenza, tutte le credenziali sono memorizzate localmente sui vostri dispositivi e la sincronizzazione tra più macchine è esclusivamente peer-to-peer. Questa architettura elimina i singoli punti di guasto associati ai database centralizzati: non ci sono server da compromettere, né infrastrutture di terze parti che possano accedere alle vostre credenziali. Le comunicazioni tra i dispositivi sono crittografate end-to-end, per garantire che solo le chiavi in vostro possesso consentano l'accesso ai dati.



![Image](assets/fr/02.webp)



Per rendere tutto ciò possibile, come suggerisce il nome, PearPass si basa su **Pears**, un ecosistema tecnologico peer-to-peer dedicato alla creazione e all'esecuzione di applicazioni serverless. Pears fornisce l'ambiente di esecuzione, i meccanismi di distribuzione e i livelli di rete necessari per eseguire applicazioni completamente decentralizzate, in grado di sincronizzarsi direttamente tra peer, senza alcuna infrastruttura centrale. Nel caso di PearPass, Pears fornisce il rilevamento dei dispositivi, la creazione di connessioni crittografate e la sincronizzazione del caveau delle password tra le macchine. Questo approccio garantisce che PearPass rimanga funzionale, resiliente e indipendente da qualsiasi autorità esterna.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Oltre a questa architettura innovativa, PearPass è interamente open-source e tutte le sue funzioni sono gratuite. Il software è stato inoltre sottoposto a un controllo indipendente da parte di Secfault Security. Oltre alla sua architettura specifica, PearPass offre naturalmente tutte le classiche funzioni che ci si aspetta da un buon gestore di password, che scopriremo nel corso di questo tutorial.



In breve, laddove i gestori di password tradizionali chiedono di fidarsi di un'azienda e dei suoi server, PearPass adotta una logica di sovranità: niente cloud, niente account centralizzati, niente intermediari. L'utente mantiene il controllo esclusivo sulle proprie credenziali, beneficiando al contempo della sincronizzazione tra i propri dispositivi.



## Come si installa PearPass?



PearPass è disponibile su tutte le piattaforme: Windows, Linux, macOS, Android, iOS ed estensioni del browser. Non è necessario installare Pears sul computer: PearPass funziona da solo.



### Installazione su Windows



Su Windows, PearPass viene fornito come programma di installazione classico. Andare alla [pagina ufficiale di download] (https://pass.pears.com/download), quindi fare clic sul pulsante "Scarica il programma di installazione di Windows".



Una volta scaricato il file, aprire il programma di installazione e seguire i passaggi indicati dalla procedura guidata. È quindi possibile accedere all'applicazione dal `Menu di avvio` o tramite un collegamento sul desktop.



![Image](assets/fr/03.webp)



### Installazione su macOS



Su macOS, PearPass è distribuito come immagine disco (`.dmg`). Andate su [la pagina ufficiale di download](https://pass.pears.com/download) e scegliete la versione corrispondente all'architettura del vostro Mac (Intel o Apple Silicon). Dopo il download, aprire il file `.dmg` e lanciare l'applicazione dalla cartella `Applications`.



Al primo avvio, macOS visualizzerà un messaggio di sicurezza che indica che l'applicazione proviene da Internet: è sufficiente confermare per continuare.



### Installazione su Linux



Su Linux, PearPass è disponibile nel formato `.AppImage`, che garantisce un'ampia compatibilità con la maggior parte delle distribuzioni senza dipendenze specifiche. Scaricare il file `.AppImage` da [la pagina ufficiale di download](https://pass.pears.com/download), quindi avviarlo direttamente con un doppio clic.



A seconda dell'ambiente, potrebbe essere necessario rendere il file eseguibile tramite le proprietà del file (clic destro) o con il comando `chmod +x`. Una volta autorizzato, PearPass si avvia come applicazione autonoma.



### Installazione dell'estensione del browser



PearPass offre un'estensione del browser per il login automatico e l'accesso rapido alla vostra cassaforte durante la navigazione sul web. L'estensione è attualmente disponibile per Google Chrome e i browser compatibili. Per installarla, visitate [la pagina ufficiale di download] (https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Una volta aggiunta, è possibile appuntarla sulla barra degli strumenti per un accesso rapido. L'attivazione dell'estensione richiede un collegamento con l'applicazione PearPass installata localmente sul computer (torneremo su questo punto più avanti nel tutorial).



### Installazione su iOS e Android



Su iPhone e Android, è sufficiente scaricare l'applicazione dall'app store:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Oltre a questi metodi di installazione classici, è possibile scaricare il software direttamente dai repository GitHub, per ogni :




- [Desktop](https://github.com/tetherto/pearpass-app-desktop);
- [Mobile](https://github.com/tetherto/pearpass-app-mobile);
- [Estensione del browser](https://github.com/tetherto/pearpass-app-browser-extension).



Una volta installato PearPass su una o più piattaforme, si può passare alla configurazione iniziale. In questo tutorial, inizieremo a configurare il software sul desktop, per poi sincronizzarlo con l'estensione del browser e l'applicazione mobile.



## Come si crea una cassaforte PearPass?



Quando si avvia PearPass sul computer, l'applicazione guida l'utente attraverso due fasi: l'impostazione della password principale e la creazione della prima cassaforte.



### Impostare la password principale



Quando l'applicazione viene avviata per la prima volta sul desktop, fare clic sul pulsante `Skip` e poi `Continue` per passare attraverso la schermata di introduzione e raggiungere la fase di configurazione della master password.



![Image](assets/fr/06.webp)



Segue l'importante fase della scelta della password principale. Come abbiamo visto nell'introduzione, questa password è molto importante, poiché consente di accedere a tutte le altre password salvate nel manager. Tecnicamente, viene utilizzata per ricavare le chiavi crittografiche utilizzate per criptare i dati.



La master password comporta due rischi principali: la perdita e la compromissione. Se si perde l'accesso a questa password, non sarà più possibile accedere ai propri dati di accesso. PearPass non conserva mai la password principale: **Se viene persa, i vostri dati di accesso sono definitivamente persi**. Non esiste un meccanismo di recupero. Al contrario, se questa password viene compromessa e un malintenzionato ottiene l'accesso a uno dei vostri dispositivi, sarà in grado di accedere a tutti i vostri account.



Per limitare il rischio di perdita, è possibile eseguire un backup fisico della password principale, ad esempio su carta, e conservarlo in un luogo sicuro. L'ideale sarebbe sigillare questa copia di sicurezza in una busta, in modo da poter verificare periodicamente che non vi si sia acceduto. D'altra parte, non è mai il caso di fare un backup digitale di questa password.



Per ridurre il rischio di compromissione, la master password deve essere forte. Dovrebbe essere la più lunga possibile, includere un'ampia varietà di caratteri ed essere scelta in modo veramente casuale. Nel 2025, le raccomandazioni minime prevedono almeno 13 caratteri tra lettere maiuscole e minuscole, numeri e simboli, a condizione che la password sia casuale. Tuttavia, consiglierei una password di almeno 20 caratteri, se non di più, con tutti i tipi di caratteri, per garantire un livello di sicurezza più duraturo.



Immettere la password principale nell'apposito campo, confermarla una seconda volta e fare clic sul pulsante "Continua".



![Image](assets/fr/07.webp)



Verrete quindi reindirizzati alla schermata di accesso: inserite la vostra password principale per verificare che tutto funzioni correttamente.



![Image](assets/fr/08.webp)



### Creare la prima cassaforte



Una volta effettuato l'accesso, PearPass vi chiederà di creare la vostra prima cassaforte. Una cassaforte è un contenitore crittografato in cui vengono memorizzate password, ID, note sicure e altre informazioni. Ogni cassaforte è isolata e può essere identificata con un nome distinto, consentendovi di organizzare i vostri dati in base ai vostri usi (personali, professionali, progetti specifici...).



Fare clic sul pulsante "Crea un nuovo caveau".



![Image](assets/fr/09.webp)



Scegliere un nome per questo vault, quindi fare clic su "Crea un nuovo vault" per finalizzare la creazione.



![Image](assets/fr/10.webp)



La vostra cassaforte è subito pronta all'uso. Potete iniziare subito ad aggiungere password, login o note sicure.



![Image](assets/fr/11.webp)



## Come faccio ad aggiungere un login a PearPass?



Una volta creata la cassaforte, è possibile iniziare a salvarvi i propri oggetti. PearPass supporta la registrazione di molti tipi di oggetti:




- accedere a un sito o a un servizio ;
- identità: le informazioni personali per compilare rapidamente i moduli, ma anche per memorizzare i documenti di identità direttamente in PearPass ;
- carta di credito: i numeri della vostra carta di credito per velocizzare il pagamento quando fate acquisti online;
- Wi-Fi: password per le reti Wi-Fi ;
- PassPhrase: frase segreta composta da più parole (attenzione: sconsiglio vivamente di usarla per le frasi mnemoniche wallet Bitcoin);
- nota: creazione di note sicure ;
- custom: questa funzione consente di creare un tipo di elemento personalizzato, adatto alle proprie esigenze specifiche.



Iniziate aprendo PearPass e accedendo con la vostra password principale.



![Image](assets/fr/12.webp)



Selezionare la cassaforte in cui si desidera salvare l'identificatore.



![Image](assets/fr/13.webp)



Nella pagina iniziale, fare clic sul pulsante per aggiungere un nuovo elemento, a seconda del tipo di informazioni che si desidera registrare. Nel mio caso, voglio aggiungere un login per il mio account sul sito web di Plan ₿ Academy: faccio quindi clic sul pulsante "Crea un login".



![Image](assets/fr/14.webp)



Una volta selezionato il tipo di elemento che si desidera aggiungere, appare un modulo che consente di inserire le informazioni associate al servizio in questione. A seconda delle esigenze, è possibile inserire il nome del servizio, il login, la password e, se necessario, l'indirizzo del sito web e note aggiuntive.



PearPass dispone anche di un generatore di password che consente di creare una password forte direttamente dal modulo. Per utilizzarlo, fare clic sull'icona che rappresenta tre piccoli punti nel campo `Password`, scegliere la lunghezza desiderata, quindi fare clic su `Insert password`.



Una volta compilati tutti i campi, fare clic sul pulsante "Salva" per salvare l'identificatore nella cassaforte.



![Image](assets/fr/15.webp)



L'identificatore è ora salvato. Appare nell'elenco degli elementi della cassaforte selezionata e può essere visualizzato facendo clic su di esso.



![Image](assets/fr/16.webp)



È possibile modificare facilmente un elemento facendo clic su di esso e poi sul pulsante "Modifica". È anche possibile cancellarlo facendo clic sui tre puntini in alto a destra dell'interfaccia e poi su `Cancella elemento`.



![Image](assets/fr/22.webp)



Su mobile, la logica rimane la stessa, anche se l'interfaccia è stata adattata. Dopo aver effettuato il login, si seleziona la cassaforte desiderata, si tocca il pulsante `+`, si sceglie il tipo di articolo da creare e si compilano le informazioni necessarie.



![Image](assets/fr/17.webp)



## Come organizzare PearPass?



Come abbiamo visto nelle sezioni precedenti, PearPass consente di creare diversi caveau distinti. Questo permette di separare i diversi usi e costituisce un primo livello di organizzazione per il vostro gestore di password. Dalla pagina iniziale, è possibile passare facilmente da un vault all'altro facendo clic sulla freccia in alto a sinistra dell'interfaccia.



![Image](assets/fr/18.webp)



Un altro modo per organizzare le password, anche all'interno di un vault, è quello di creare delle cartelle. A tale scopo, nella colonna di sinistra dell'interfaccia, fare clic sul simbolo `+` accanto a `Tutte le cartelle`, quindi inserire il nome della cartella che si desidera creare.



![Image](assets/fr/19.webp)



È quindi possibile memorizzare gli identificatori di propria scelta, sia direttamente durante la creazione di un elemento, sia in seguito facendo clic su "Modifica". È sufficiente selezionare la cartella desiderata nell'angolo in alto a sinistra del modulo.



![Image](assets/fr/20.webp)



Dopo aver aperto un elemento, ad esempio un login, è possibile fare clic sull'icona della stella in alto a destra dell'interfaccia per aggiungerlo ai preferiti. I preferiti possono essere trovati rapidamente in una cartella dedicata, oltre a quella di base.



![Image](assets/fr/21.webp)



Infine, nella parte superiore dell'interfaccia è presente una barra di ricerca che consente di trovare rapidamente l'elemento desiderato, anche se il caveau contiene molti identificatori.



## Come faccio a sincronizzare PearPass sul mio cellulare?



Ora che avete un caveau funzionante con elementi memorizzati sul vostro computer, probabilmente vorrete accedere alle vostre password dal vostro smartphone o da un altro dispositivo. PearPass consente di sincronizzare il proprio gestore su più macchine in modo sicuro utilizzando Pears. Scopriamo come.



Per iniziare, sul computer di origine (ad esempio, il vostro computer), accedete al vostro vault utilizzando la vostra password principale. Una volta nella pagina iniziale, fare clic sul pulsante "Aggiungi un dispositivo", situato in basso a destra dell'interfaccia.



![Image](assets/fr/23.webp)



PearPass genera quindi un link di invito, disponibile anche come codice QR, per sincronizzare il caveau selezionato sul dispositivo di vostra scelta.



![Image](assets/fr/24.webp)



Se si desidera effettuare la sincronizzazione sul dispositivo mobile, installare prima l'applicazione e poi avviarla. Vi verrà chiesto di creare una password principale per il vostro mobile manager. È possibile scegliere di utilizzare la stessa password del computer o una diversa. In ogni caso, seguite le stesse raccomandazioni: una password forte e casuale salvata su un supporto fisico.



![Image](assets/fr/25.webp)



Se lo si desidera, è possibile attivare l'autenticazione biometrica per evitare di dover inserire manualmente la password principale ogni volta che si sblocca il cellulare.



![Image](assets/fr/26.webp)



Reinserire la password principale, quindi fare clic sul pulsante "Continua".



![Image](assets/fr/27.webp)



Selezionare l'opzione "Carica un vault", quindi fare clic su "Scansiona codice QR" e scansionare il codice QR dell'invito visualizzato da PearPass sulla macchina di origine (il computer).



![Image](assets/fr/28.webp)



I vostri caveau sul computer e sul cellulare sono ora sincronizzati. Ogni ID aggiunto su un dispositivo sarà memorizzato e replicato in modo sicuro sull'altro.



![Image](assets/fr/29.webp)



Sui telefoni cellulari, è possibile attivare il riempimento automatico dei campi. A tale scopo, accedere a `Impostazioni > Avanzate`, quindi fare clic sul pulsante `Imposta come predefinita` nella sezione `Compilazione automatica`.



![Image](assets/fr/30.webp)



## Come faccio a sincronizzare PearPass con l'estensione del browser?



Avere un gestore di password sincronizzato tra il computer e lo smartphone è già molto pratico, ma integrarlo direttamente nel browser lo è ancora di più. Per farlo, iniziate [aggiungendo l'estensione ufficiale di PearPass al vostro browser](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Dal software PearPass installato sul computer locale, andare su `Impostazioni > Avanzate`, quindi attivare l'opzione `Attiva estensione browser`.



![Image](assets/fr/32.webp)



PearPass genera un file di abbinamento token. Copiarlo.



![Image](assets/fr/33.webp)



Quindi aprire l'estensione PearPass nel browser, incollare l'accoppiamento token e fare clic sul pulsante "Verifica", seguito da "Completa".



![Image](assets/fr/34.webp)



Il vostro gestore di password è ora sincronizzato con l'estensione del browser.



![Image](assets/fr/35.webp)



Ora è possibile utilizzarlo per connettersi facilmente ai vari account Web.



![Image](assets/fr/36.webp)



Ora sapete come utilizzare il gestore di password PearPass. Al di là di questo strumento, la sicurezza digitale quotidiana dipende dall'uso corretto di soluzioni adeguate. Se volete imparare a creare un ambiente digitale personale sicuro, stabile ed efficiente, vi invito a scoprire il nostro corso di formazione dedicato a questo argomento:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
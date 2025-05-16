---
name: Trezor U2F e FIDO2
description: Rafforzate la vostra sicurezza online con Trezor
---
![cover](assets/cover.webp)



I dispositivi Trezor sono portafogli hardware originariamente progettati per proteggere un Bitcoin Wallet, ma sono anche dotati di opzioni avanzate per un'autenticazione forte sul web. Grazie alla compatibilità con i protocolli **U2F** e **FIDO2**, consentono di proteggere l'accesso ai propri account online senza affidarsi esclusivamente alle password.



Il protocollo U2F (*Universal 2nd Factor*) è stato introdotto da Google e Yubico nel 2014 e poi standardizzato dalla FIDO Alliance. Consente di aggiungere un secondo fattore di autenticazione fisica (2FA) al momento dell'accesso. Una volta attivato, oltre alla classica password, gli utenti devono approvare ogni tentativo di connessione al proprio account premendo un pulsante sul proprio Trezor. In questo contesto, il Trezor funziona in modo simile a uno Yubikey.



Questo metodo si basa sulla crittografia asimmetrica: non vengono trasmessi dati segreti, rendendo inefficaci gli attacchi di phishing o di intercettazione. U2F è ora supportato da molti servizi online.



Oltre a U2F, che consente l'autenticazione a due fattori, i Trezors supportano anche FIDO2 (*Fast IDentity Online 2.0*), un'evoluzione di U2F. Si tratta di un protocollo di autenticazione standardizzato dal 2018, che estende la logica di U2F e mira a sostituire completamente le password. Si basa su due componenti: *WebAuthn* (lato browser) e *CTAP2* (lato chiave fisica). FIDO2 consente l'autenticazione "senza password": gli utenti si identificano esclusivamente tramite il proprio dispositivo Trezor, che funge da token crittografico unico, senza alcuna password aggiuntiva. Questo protocollo è ora compatibile con numerosi servizi online, in particolare quelli rivolti alle aziende.



Oltre alla funzionalità "senza password*", FIDO2 consente anche l'autenticazione a due fattori in modo simile a U2F.



FIDO2 introduce anche la nozione di credenziali residenti, ossia identificativi memorizzati direttamente nel Trezor, che comprendono sia la chiave privata che consente la connessione sia le informazioni di identificazione dell'utente. Questo meccanismo consente un'autenticazione realmente priva di password: è sufficiente collegare il Trezor e confermare l'accesso, senza inserire né ID né password. Al contrario, le credenziali non residenti, più convenzionali, memorizzano solo la chiave privata nel dispositivo; l'ID utente rimane memorizzato sul lato server e deve quindi essere inserito a ogni connessione. Vedremo più avanti come salvarle con Trezor.



In questo tutorial scopriremo come attivare U2F o FIDO2 per l'autenticazione a due fattori e come configurare FIDO2 per accedere ai vostri account senza password, direttamente con il vostro Trezor.



**Nota:** U2F è compatibile con tutti i modelli Trezor, ma FIDO2 è supportato solo da Safe 3, Safe 5 e Model T, non dal Model One.



## Utilizzo di U2F/FIDO2 per 2FA su Trezor



Prima di iniziare, assicurarsi di aver impostato il Bitcoin Wallet sul proprio Trezor. È importante salvare correttamente il Mnemonic, poiché le chiavi utilizzate per U2F e FIDO2 nell'autenticazione a due fattori derivano da questo Mnemonic. Se il Trezor viene smarrito o danneggiato, è possibile recuperare l'accesso alle chiavi inserendo la frase Mnemonic su un altro dispositivo Trezor (si noti che per le credenziali FIDO2 in modalità "*passwordless*", il solo seed non è sufficiente, come vedremo nelle prossime sezioni).



Collegare il Trezor al computer e sbloccarlo.



![Image](assets/fr/01.webp)



Accedere all'account che si desidera proteggere con l'autenticazione a due fattori. Ad esempio, utilizzerò un account Bitwarden. Di solito l'opzione 2FA si trova nelle impostazioni del servizio, sotto le schede "*autenticazione*", "*sicurezza*", "*login*" o "*password*".



![Image](assets/fr/02.webp)



Nella sezione dedicata all'autenticazione a due fattori, selezionare l'opzione "*Passkey*" (il termine può variare a seconda del sito utilizzato).



![Image](assets/fr/03.webp)



Spesso vi verrà chiesto di confermare la vostra password attuale.



![Image](assets/fr/04.webp)



Assegnare un nome alla chiave di sicurezza per facilitarne il riconoscimento, quindi fare clic su "*Leggi chiave*".



![Image](assets/fr/05.webp)



I dettagli dell'account appariranno sullo schermo di Trezor. Toccare lo schermo o premere il pulsante per confermare. Verrà inoltre richiesto di confermare il codice PIN.



![Image](assets/fr/06.webp)



Registrare questa chiave di sicurezza.



![Image](assets/fr/07.webp)



D'ora in poi, quando vorrete collegarvi al vostro account, oltre alla solita password, vi verrà chiesto di collegare il vostro Trezor.



![Image](assets/fr/08.webp)



È quindi possibile premere lo schermo del Trezor per confermare l'autenticazione.



![Image](assets/fr/09.webp)



Il vantaggio di utilizzare un Trezor Hardware Wallet per l'autenticazione a due fattori è che è possibile recuperare facilmente le chiavi grazie alla frase Mnemonic. Oltre a questo backup di base, è possibile utilizzare un codice di emergenza fornito da ogni servizio in cui è stata attivata la 2FA. Questo codice di emergenza consente di collegarsi al proprio account in caso di smarrimento della chiave di sicurezza. Sostituisce quindi il 2FA per una connessione, se necessario.



Su Bitwarden, ad esempio, è possibile accedere a questo codice facendo clic su "*Vedi codice di recupero*".



![Image](assets/fr/10.webp)



Vi consiglio di conservare questo codice in un luogo diverso da quello in cui conservate la password principale, per evitare che vengano rubati insieme. Ad esempio, se la vostra password è salvata in un password manager, conservate il codice di emergenza 2FA su carta, separatamente.



Questo approccio offre due livelli di backup in caso di smarrimento del Trezor per l'autenticazione 2FA: un primo backup che utilizza la frase Mnemonic per tutti gli account e un secondo specifico per ogni account con i codici di emergenza. Tuttavia, è importante **non confondere il ruolo del Mnemonic con quello del codice di emergenza** :




- La frase Mnemonic, composta da 12 o 24 parole, consente di accedere non solo alle chiavi utilizzate per la 2FA su tutti gli account, ma anche ai bitcoin protetti con il Trezor;
- Il codice di emergenza consente di bypassare temporaneamente la richiesta di 2FA solo sull'account interessato (in questo esempio, solo su Bitwarden).



## Utilizzo di FIDO2 su Trezor



Oltre all'autenticazione a due fattori, FIDO2 consente anche l'autenticazione "senza password", cioè senza dover inserire una password quando si accede a un sito. È sufficiente collegare il Trezor al computer per accedere al proprio account protetto. Ecco come configurare questa funzione.



Prima di iniziare, assicurarsi di aver impostato il Bitcoin Wallet sul proprio Trezor. È importante salvare il Mnemonic, poiché gli identificatori FIDO2 "*senza password*" sono criptati con il seed (scopriremo come salvare correttamente questi identificatori nella prossima sezione).



Collegare il Trezor al computer e sbloccarlo.



![Image](assets/fr/01.webp)



Accedere all'account che si desidera proteggere in modalità "*senza password*". Utilizzerò un account Bitwarden come esempio. Questa opzione si trova solitamente nelle impostazioni del servizio, spesso sotto la scheda "*autenticazione*", "*sicurezza*" o "*password*".



Su Bitwarden, ad esempio, l'opzione si trova nella scheda "*Password principale*". Fare clic su "*Attiva*" per attivare l'autenticazione tramite FIDO2.



![Image](assets/fr/11.webp)



Spesso vi verrà chiesto di confermare la password.



![Image](assets/fr/12.webp)



I dettagli dell'account appariranno sullo schermo di Trezor. Toccare lo schermo o premere il pulsante per confermare. È necessario confermare anche il codice PIN.



![Image](assets/fr/13.webp)



Sul sito, aggiungere un nome per ricordare la chiave di sicurezza, quindi fare clic su "*Accensione*".



![Image](assets/fr/14.webp)



Vi verrà chiesto di identificarvi per verificare il corretto funzionamento della chiave.



![Image](assets/fr/15.webp)



D'ora in poi, quando si accede al proprio account, non sarà più necessario inserire l'e-mail Address o il login. È sufficiente fare clic sul pulsante per autenticarsi con una chiave fisica nel modulo di accesso.



![Image](assets/fr/16.webp)



Confermare la connessione al Trezor immettendo il PIN Hardware Wallet.



![Image](assets/fr/17.webp)



Sarete collegati al vostro account senza dover inserire la password.



![Image](assets/fr/18.webp)



**Si prega di notare che anche se si attiva l'autenticazione "*senza password*" tramite FIDO2 sul proprio Trezor, la password principale del proprio account online sarà ancora valida ai fini del login**



## Salvare le proprie credenziali FIDO2 (residenti delle credenziali)



Se si utilizza FIDO2 o U2F per l'autenticazione a due fattori, ovvero per accedere ad account che richiedono una password oltre alla convalida 2FA tramite Trezor, la frase Mnemonic da sola recupererà l'accesso alle chiavi. Tuttavia, se si utilizza FIDO2 in modalità "*senza password*" come descritto nella sezione precedente, sarà necessario fare una copia delle credenziali FIDO oltre a eseguire il backup della frase Mnemonic che cripta tali credenziali.



Per farlo, è necessario un computer con Python installato. Aprite un terminale ed eseguite il seguente comando per installare il software Trezor necessario:



```shell
pip3 install --upgrade trezor
```



Collegare il Trezor al computer tramite USB e sbloccarlo utilizzando il codice PIN.



![Image](assets/fr/01.webp)



Per recuperare l'elenco degli identificatori FIDO2 memorizzati su Trezor, eseguire il seguente comando:



```shell
trezorctl fido credentials list
```



Confermare l'esportazione sul Trezor.



![Image](assets/fr/19.webp)



Le informazioni di accesso FIDO2 verranno visualizzate sul terminale. Ad esempio, per il mio conto Bitwarden, ho ottenuto queste informazioni:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Copiate e salvate tutte queste informazioni in un file di testo. Non ci sono rischi significativi associati a questo backup, se non quello di rivelare che state utilizzando questi servizi con FIDO2. Il "*Credential ID*" è crittografato utilizzando il seed del Wallet, il che significa che un utente malintenzionato che ottenesse questo backup non sarebbe in grado di connettersi ai vostri account, ma solo di notare che li state utilizzando. Per decifrare questi ID, è necessario il seed del Wallet.



È quindi possibile creare diverse copie di questo file di testo e conservarle in luoghi diversi, ad esempio localmente sul computer, su un servizio di file-hosting e su supporti esterni come una chiavetta USB. Tuttavia, si tenga presente che questo backup non viene aggiornato automaticamente, quindi è necessario rinnovarlo ogni volta che si imposta una nuova connessione "*senza password*" con il Trezor.



Immaginiamo ora che si sia rotto il Trezor. Per recuperare le credenziali FIDO2, dovrete prima recuperare il vostro Wallet utilizzando la frase Mnemonic su un nuovo dispositivo Trezor compatibile con FIDO2.



Una volta completato il ripristino, per importare gli identificatori FIDO2 sul nuovo dispositivo, eseguire il seguente comando nel terminale:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



È sufficiente sostituire `<CREDENTIAL_ID>` con uno dei propri identificatori. Ad esempio, nel mio caso, si otterrebbe :



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Il Trezor chiederà di importare il proprio identificativo FIDO2. Confermare premendo sullo schermo.



![Image](assets/fr/20.webp)



Il login FIDO2 è ora operativo su Trezor. Ripetere questa procedura per ogni identificatore.



Congratulazioni, ora siete in grado di utilizzare il vostro Trezor con U2F e FIDO2! Se hai trovato utile questo tutorial, ti sarei molto grato se lasciassi un pollice Green qui sotto. Sentitevi liberi di condividere questo tutorial sui vostri social network. Grazie mille!



Vi consiglio anche quest'altro tutorial, in cui esaminiamo un'altra soluzione per l'autenticazione U2F e FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e
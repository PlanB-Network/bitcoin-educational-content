---
name: "Trezor U2F & FIDO2"
description: Potenzia la sicurezza online con Trezor
---
![cover](assets/cover.webp)



I dispositivi Trezor sono stati originariamente progettati per proteggere un wallet bitcoin (sono quindi degli hardware wallet), ma sono anche dotati di opzioni avanzate per accedere in modo sicuro a vari siti su Internet. Grazie alla compatibilità con i protocolli **U2F** e **FIDO2**, questi device consentono di proteggere l'accesso ai propri account online senza affidarsi esclusivamente alle password.



Il protocollo U2F (*Universal 2nd Factor*) è stato introdotto da Google e Yubico nel 2014 e poi standardizzato dalla FIDO Alliance. Esso consente di aggiungere un secondo fattore di autenticazione (2FA) di tipo fisico quando si accede a un sito. Una volta attivato, oltre alla classica password, gli utenti devono approvare ogni tentativo di connessione al proprio account premendo un pulsante sul proprio Trezor. In questo contesto, Trezor funziona come una Yubikey.

Questo metodo si basa sulla crittografia asimmetrica: non vengono trasmessi dati segreti, rendendo inefficaci gli attacchi di phishing o di intercettazione. 

U2F è ora supportato da molti servizi online.

Oltre a U2F, che consente l'autenticazione a due fattori, i Trezor supportano anche FIDO2 (*Fast IDentity Online 2.0*), un'evoluzione di U2F. Si tratta di un protocollo di autenticazione standardizzato dal 2018, che estende la logica di U2F e mira a sostituire completamente le password. Si basa su due componenti: *WebAuthn* (lato browser) e *CTAP2* (lato chiave fisica). FIDO2 consente l'autenticazione "senza password": gli utenti si identificano esclusivamente tramite il proprio dispositivo Trezor, che funge da token crittografico unico, senza alcuna password aggiuntiva. Questo protocollo è ora compatibile con numerosi servizi online, in particolare quelli rivolti alle aziende.

Oltre alla funzionalità "senza password", FIDO2 consente anche l'autenticazione a due fattori in modo simile a U2F.

FIDO2 introduce anche il concetto di "resident credentials", ossia identificativi memorizzati direttamente sul Trezor. Questo riguarda sia la chiave privata che consente la connessione, sia le informazioni di identificazione dell'utente. Ciò consente un'autenticazione realmente priva di password: è sufficiente collegare Trezor e confermare l'accesso, senza inserire né ID, né password. Al contrario, le credenziali "non residenti", che sono più convenzionali, memorizzano solo la chiave privata nel dispositivo; l'ID dell'utente rimane memorizzato sul lato server, e deve quindi essere inserito a ogni connessione. Vedremo più avanti come salvare questi dati con Trezor.

In questo tutorial scopriremo come attivare U2F o FIDO2 per l'autenticazione a due fattori, e come configurare FIDO2 per accedere ai tuoi account senza password, direttamente con il tuo Trezor.

**Nota:** U2F è compatibile con tutti i modelli Trezor, ma FIDO2 è supportato solo da Safe 3, Safe 5 e Model T, non dal Model One. Nell'esempio che segue, viene preso come riferimento Trezor Safe 5.

## Come utilizzare U2F/FIDO2 per il 2FA su Trezor

Prima di iniziare, assicurati di aver impostato il wallet bitcoin sul tuo Trezor. È importante salvare correttamente la frase mnemonica, poiché le chiavi utilizzate per U2F e FIDO2 nell'autenticazione a due fattori derivano da essa. Se il tuo Trezor viene smarrito o danneggiato, puoi recuperare l'accesso alle chiavi inserendo la mnemonica su un altro dispositivo Trezor (nota che per le credenziali FIDO2 in modalità "*passwordless*", il solo seed non è sufficiente, come vedremo nelle prossime sezioni).

Collega Trezor al computer e sbloccalo.

![Image](assets/fr/01.webp)

Accedi all'account che desideri proteggere con l'autenticazione a due fattori. Ad esempio, io utilizzerò un account Bitwarden. Di solito l'opzione 2FA si trova nelle impostazioni del servizio, sotto le schede "*authentication*", "*security*", "*login*" o "*password*".

![Image](assets/fr/02.webp)

Nella sezione dedicata all'autenticazione a due fattori, seleziona l'opzione "*Passkey*" (il termine può variare a seconda del sito utilizzato).

![Image](assets/fr/03.webp)

Probabilmente ti verrà chiesto di confermare la password attuale.

![Image](assets/fr/04.webp)

Assegna un nome alla chiave di sicurezza per facilitarne il riconoscimento, quindi clicca su "*Read Key*".

![Image](assets/fr/05.webp)

I dettagli dell'account appariranno sullo schermo del Trezor. Tocca lo schermo o premi il pulsante per confermare. Verrà inoltre richiesto di confermare il codice PIN.

![Image](assets/fr/06.webp)

Registra questa chiave di sicurezza.

![Image](assets/fr/07.webp)

D'ora in poi, quando vorrai collegarti al tuo account, oltre alla solita password, ti verrà chiesto di collegare il tuo Trezor.

![Image](assets/fr/08.webp)

È quindi possibile premere lo schermo sul Trezor per confermare l'autenticazione.

![Image](assets/fr/09.webp)

Il vantaggio di utilizzare l'hardware wallet Trezor per l'autenticazione a due fattori sta nella possibilità di recuperare facilmente le chiavi grazie alla mnemonica. Oltre a questo backup di base, puoi utilizzare un codice di emergenza fornito da ogni servizio in cui è stata attivata la 2FA. Questo codice di emergenza consente di collegarsi al proprio account in caso di smarrimento della chiave di sicurezza. Sostituisce quindi il 2FA per una connessione, se necessario.

Su Bitwarden, ad esempio, è possibile accedere a questo codice cliccando su "*View recovery code*".

![Image](assets/fr/10.webp)

Ti consiglio di conservare questo codice in un luogo diverso da quello in cui conservi la password principale, per evitare che vengano rubati insieme. Ad esempio, se la tua password è salvata in un password manager, scrivi il codice di emergenza 2FA su carta e conservalo separatamente.

Questo approccio offre due livelli di backup per l'autenticazione 2FA in caso di smarrimento del Trezor: un primo backup utilizza la mnemonica per tutti gli account, e un secondo usa i codici di emergenza in modo specifico per ogni account. Tuttavia, è importante **non confondere il ruolo della mnemonica con quello del codice di emergenza**:

- La mnemonica, composta da 12 o 24 parole, consente di accedere non solo alle chiavi utilizzate per il 2FA su tutti gli account, ma anche ai bitcoin protetti con Trezor;
- Il codice di emergenza consente di bypassare temporaneamente la richiesta di 2FA solo sull'account interessato (in questo esempio, solo su Bitwarden).

## Utilizzo di FIDO2 su Trezor

Oltre all'autenticazione a due fattori, FIDO2 consente anche l'autenticazione "senza password", cioè senza dover inserire una password quando accedi a un sito. È sufficiente collegare Trezor al computer per accedere al proprio account protetto. Ecco come configurare questa funzione.

Prima di iniziare, assicurati di aver impostato il wallet bitcoin sul tuo Trezor. È importante salvare la mnemonica, poiché gli identificatori FIDO2 "*senza password*" sono criptati con il seed (scopriremo come salvare correttamente questi identificatori nella prossima sezione).

Collega il Trezor al computer e sbloccalo.

![Image](assets/fr/01.webp)

Accedi all'account che desideri proteggere in modalità "*passwordless*". Io utilizzerò un account Bitwarden come esempio. Questa opzione si trova solitamente nelle impostazioni del servizio, spesso sotto la scheda "*authentication*", "*security*" o "*password*".

Su Bitwarden, ad esempio, l'opzione si trova nella scheda "*Master Password*". Clicca su "*Turn on"*" per attivare l'autenticazione tramite FIDO2.

![Image](assets/fr/11.webp)

Probabilmente ti verrà chiesto di confermare la password.

![Image](assets/fr/12.webp)

I dettagli dell'account appariranno sullo schermo del Trezor. Tocca lo schermo o premi il pulsante per confermare. È necessario confermare anche il codice PIN.

![Image](assets/fr/13.webp)

Sul sito, aggiungi un nome per ricordarti la chiave di sicurezza, quindi clicca su "*Turn on*".

![Image](assets/fr/14.webp)

Ti verrà chiesto di identificarti per verificare il corretto funzionamento della chiave.

![Image](assets/fr/15.webp)

D'ora in poi, quando accedi al tuo account, non sarà più necessario inserire l'indirizzo e-mail o fare il login. È sufficiente cliccare sul pulsante per autenticarti con una chiave fisica nel modulo di accesso.

![Image](assets/fr/16.webp)

Conferma la connessione a Trezor immettendo il PIN dell'hardware wallet.

![Image](assets/fr/17.webp)

Sarai collegato al tuo account senza dover inserire la password.

![Image](assets/fr/18.webp)

**Nota che anche se attivi l'autenticazione "*senza password*" tramite FIDO2 sul tuo Trezor, la password principale del tuo account online sarà ancora valida ai fini del login**

## Salvare le proprie credenziali FIDO2

Se utilizzi FIDO2 o U2F per l'autenticazione a due fattori, ovvero per accedere ad account che richiedono una password oltre alla convalida 2FA tramite Trezor, la mnemonica da sola recupererà l'accesso alle chiavi. Tuttavia, se utilizzi FIDO2 in modalità "*passwordless*" come descritto nella sezione precedente, sarà necessario fare una copia delle credenziali FIDO oltre a eseguire il backup della mnemonica che cripta tali credenziali.

Per farlo, è necessario un computer con Python installato. Apri un terminale ed esegui il seguente comando per installare il software Trezor necessario:

```shell
pip3 install --upgrade trezor
```

Collega Trezor al computer tramite USB e sbloccalo utilizzando il codice PIN.

![Image](assets/fr/01.webp)

Per recuperare l'elenco degli identificatori FIDO2 memorizzati sul Trezor, esegui il seguente comando:

```shell
trezorctl fido credentials list
```

Conferma l'esportazione su Trezor.

![Image](assets/fr/19.webp)

Le informazioni di accesso FIDO2 verranno visualizzate sul terminale. Ad esempio, per il mio account su Bitwarden, ho ottenuto queste informazioni:

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

Copia e salva tutte queste informazioni in un file di testo. Non ci sono rischi significativi associati a questo backup, se non quello di rivelare che stai utilizzando questi servizi con FIDO2. Il "*Credential ID*" è crittografato utilizzando il seed del wallet, il che significa che un utente malintenzionato che ottenesse questo backup non sarebbe in grado di connettersi ai tuoi account, ma può soltanto sapere che li stai utilizzando. Per decifrare questi ID, è necessario il seed del wallet.

È quindi possibile creare diverse copie di questo file di testo e conservarle in luoghi diversi, ad esempio localmente sul computer, su un servizio di file-hosting e su supporti esterni come una chiavetta USB. Tuttavia, tieni presente che questo backup non viene aggiornato automaticamente, quindi è necessario rinnovarlo ogni volta che imposti una nuova connessione "*passwordless*" con Trezor.

Immaginiamo ora che si sia rotto il tuo Trezor. Per recuperare le credenziali FIDO2, devi prima recuperare il tuo wallet utilizzando la mnemonica su un nuovo dispositivo Trezor compatibile con FIDO2.

Una volta completato il ripristino, per importare gli identificatori FIDO2 sul nuovo dispositivo, esegui il seguente comando nel terminale:

```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```

È sufficiente sostituire `<CREDENTIAL_ID>` con uno dei propri identificatori. Ad esempio, nel mio caso, si otterrebbe:

```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```

Trezor chiederà di importare il tuo identificativo FIDO2. Conferma premendo sullo schermo.

![Image](assets/fr/20.webp)

Il login FIDO2 è ora operativo su Trezor. Ripeti questa procedura per ogni identificatore.

Congratulazioni, ora sei in grado di utilizzare Trezor con U2F e FIDO2! Se hai trovato utile questo tutorial, ti sarei molto grato se lasciassi un pollice verde qui sotto. Sentiti libero di condividere questo tutorial sui tuoi social network. Grazie mille!

Ti consiglio anche quest'altro tutorial, in cui esaminiamo un'altra soluzione per l'autenticazione U2F e FIDO2:

https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e
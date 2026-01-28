---
name: "Ledger U2F & FIDO2"
description: Migliora la tua sicurezza online con Ledger
---
![cover](assets/cover.webp)

I dispositivi Ledger sono portafogli hardware originariamente progettati per proteggere un wallet Bitcoin, ma presentano anche opzioni avanzate per un'autenticazione forte sul web. Grazie alla compatibilità con i protocolli **U2F** e **FIDO2**, consentono di proteggere l'accesso ai tuoi account online impostando un secondo fattore di autenticazione.

Il protocollo U2F (Universal 2nd Factor) è stato introdotto da Google e Yubico nel 2014 e poi standardizzato dalla FIDO Alliance. Consente di aggiungere un secondo fattore di autenticazione fisica (2FA) al momento dell'accesso. Una volta attivato, oltre alla classica password, l'utente deve approvare ogni tentativo di connessione al proprio account premendo un pulsante sul proprio Ledger. In questo contesto, il Ledger funziona in modo simile a uno Yubikey. U2F è di fatto un sottocomponente dello standard FIDO2, che lo ingloba apportando notevoli miglioramenti, tra cui il supporto nativo per i browser moderni e una maggiore flessibilità nella gestione delle chiavi di autenticazione.

Questi metodi si basano sulla crittografia asimmetrica: non vengono trasmessi dati segreti, rendendo inefficaci gli attacchi di phishing o di intercettazione. U2F e FIDO2 sono ora supportati da molti servizi online.

In questa esercitazione ti mostrerò come attivare U2F e FIDO2 per l'autenticazione a due fattori con il tuo Ledger.

**Nota:** U2F e FIDO2 sono supportati su tutti i dispositivi Ledger dotati di firmware recente: dalla versione 2.1.0 per Nano X e Nano S classic e dalla versione 1.1.0 per Nano S Plus. I modelli Stax e Flex sono nativamente compatibili.


## Installare l'applicazione Ledger Security Key

Se utilizzi un dispositivo Ledger, probabilmente sai che il firmware da solo non contiene tutte le funzioni necessarie per gestire i portafogli di crittografia. Ad esempio, per utilizzare un wallet Bitcoin, è necessario installare l'applicazione "*Bitcoin*". Allo stesso modo, per gestire le chiavi MFA, è necessario installare l'applicazione "*Security Key*".

Prima di iniziare, assicurarsi di aver configurato il Bitcoin Wallet sul Ledger. È importante salvare correttamente il Mnemonic, poiché le chiavi utilizzate per la 2FA derivano da questo Mnemonic. È importante salvare correttamente il Mnemonic, in quanto le chiavi utilizzate per la 2FA derivano da questo Mnemonic. Se il Ledger viene smarrito o danneggiato, è possibile recuperare l'accesso alle chiavi inserendo la frase Mnemonic su un altro dispositivo Ledger (per il momento, gli identificatori FIDO2 in modalità "*passwordless*" non sono ancora supportati su Ledger, quindi non ci sono identificatori residenti).

Collega il Ledger al computer e sbloccalo.

![Image](assets/fr/01.webp)

Per installare l'applicazione, apri il software [Ledger Live](https://www.ledger.com/Ledger-live), quindi vai alla scheda "*My Ledger*". Trova l'applicazione "*Chiave di sicurezza*" e installala sul dispositivo.

![Image](assets/fr/02.webp)

L'applicazione "*Chiave di sicurezza*" dovrebbe ora apparirsi insieme alle altre applicazioni installate sul Ledger.

![Image](assets/fr/03.webp)

Fai clic sull'applicazione per lasciarla aperta per le fasi successive dell'esercitazione.

![Image](assets/fr/04.webp)


## Utilizzare U2F/FIDO2 per 2FA con un Ledger

Accedi all'account che desideri proteggere con l'autenticazione a due fattori. Ad esempio, utilizzerò un account Bitwarden. Di solito l'opzione 2FA si trova nelle impostazioni del servizio, sotto le schede "*autenticazione*", "*sicurezza*", "*login*" o "*password*".

![Image](assets/fr/05.webp)

Nella sezione dedicata all'autenticazione a due fattori, selezionare l'opzione "*Passkey*" (il termine può variare a seconda del sito utilizzato).

![Image](assets/fr/06.webp)

Spesso ti verrà chiesto di confermare la tua password attuale.

![Image](assets/fr/07.webp)

Assegna un nome alla chiave di sicurezza per facilitarne il riconoscimento, quindi fare clic su "*Leggi chiave*".

![Image](assets/fr/08.webp)

I dettagli del tuo account appariranno sul display del Ledger. Premi il pulsante "*Register*" per confermare (o entrambi i pulsanti contemporaneamente, a seconda del modello in uso).

![Image](assets/fr/09.webp)

La chiave di accesso è stata registrata con successo.

![Image](assets/fr/10.webp)

Registra questa chiave di sicurezza.

![Image](assets/fr/11.webp)

D'ora in poi, quando accedi al tuo account, oltre alla solita password, ti verrà richiesto di collegare il tuo Ledger.

![Image](assets/fr/12.webp)

È quindi possibile premere il pulsante "*Log in*" sul display del Ledger per confermare l'autenticazione (o entrambi i pulsanti contemporaneamente, a seconda del modello in uso).

![Image](assets/fr/13.webp)

Il vantaggio di utilizzare un Hardware Wallet Ledger per l'autenticazione a due fattori è che è possibile recuperare facilmente le chiavi grazie alla frase mnemonica. Oltre a questo backup di base, è possibile utilizzare un codice di emergenza fornito da ogni servizio in cui è stata attivata la 2FA. Questo codice di emergenza ti consente di collegarti al tuo account in caso di smarrimento della chiave di sicurezza. Quindi se necessario, sostituisce il 2FA per una connessione.

Su Bitwarden, ad esempio, è possibile accedere a questo codice facendo clic su "*Vedi codice di recupero*".

![Image](assets/fr/14.webp)

Ti consiglio di conservare questo codice in un luogo diverso da quello in cui conservi la password principale, per evitare che vengano rubati insieme. Ad esempio, se la tua password è salvata in un password manager, conserva il codice di emergenza 2FA su carta, separatamente.

Questo approccio offre due livelli di backup in caso di perdita del Ledger per l'autenticazione 2FA: un primo backup utilizzando la frase mnemonica per tutti gli account e un secondo backup specifico per l'account utilizzando i codici di emergenza. Tuttavia, è importante **non confondere il ruolo della mnemonica con quello del codice di emergenza**:

- La frase mnemonica di 12 o 24 parole consente di accedere non solo alle chiavi utilizzate per la 2FA su tutti gli account, ma anche ai bitcoin protetti con il Ledger;
- Il codice di emergenza consente di bypassare temporaneamente la richiesta di 2FA solo sull'account interessato (in questo esempio, solo su Bitwarden).

Congratulazioni, ora sei in grado di utilizzare il tuo Ledger per l'MFA! Se hai trovato utile questo tutorial, ti sarei molto grato se potessi lasciare un pollice verde qui sotto. Non esitare a condividere questa guida sui tuoi social network. Grazie mille!

Ti consiglio anche quest'altro tutorial, in cui esaminiamo un'altra soluzione per l'autenticazione U2F e FIDO2:

https://planb.academy/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

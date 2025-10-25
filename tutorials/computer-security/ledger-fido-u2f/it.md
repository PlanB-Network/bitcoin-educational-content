---
name: "Ledger U2F & FIDO2"
description: Migliorate la vostra sicurezza online con Ledger
---
![cover](assets/cover.webp)



I dispositivi Ledger sono portafogli hardware originariamente progettati per proteggere un Bitcoin Wallet, ma presentano anche opzioni avanzate per un'autenticazione forte sul web. Grazie alla compatibilità con i protocolli **U2F** e **FIDO2**, consentono di proteggere l'accesso ai propri account online impostando un secondo fattore di autenticazione.



Il protocollo U2F (Universal 2nd Factor) è stato introdotto da Google e Yubico nel 2014 e poi standardizzato dalla FIDO Alliance. Consente di aggiungere un secondo fattore di autenticazione fisica (2FA) al momento dell'accesso. Una volta attivato, oltre alla classica password, l'utente deve approvare ogni tentativo di connessione al proprio account premendo un pulsante sul proprio Ledger. In questo contesto, il Ledger funziona in modo simile a uno Yubikey. U2F è di fatto un sottocomponente dello standard FIDO2, che lo ingloba apportando notevoli miglioramenti, tra cui il supporto nativo per i browser moderni e una maggiore flessibilità nella gestione delle chiavi di autenticazione.



Questi metodi si basano sulla crittografia asimmetrica: non vengono trasmessi dati segreti, rendendo inefficaci gli attacchi di phishing o di intercettazione. U2F e FIDO2 sono ora supportati da molti servizi online.



In questa esercitazione vi mostreremo come attivare U2F e FIDO2 per l'autenticazione a due fattori con il vostro Ledger.



**Nota: ** U2F e FIDO2 sono supportati su tutti i dispositivi Ledger dotati di firmware recente: dalla versione 2.1.0 per Nano X e Nano S classic e dalla versione 1.1.0 per Nano S Plus. I modelli Stax e Flex sono nativamente compatibili.



## Installare l'applicazione Ledger Security Key



Se si utilizza un dispositivo Ledger, probabilmente si sa che il firmware da solo non contiene tutte le funzioni necessarie per gestire i portafogli di crittografia. Ad esempio, per utilizzare un Bitcoin Wallet, è necessario installare l'applicazione "*Bitcoin*". Allo stesso modo, per gestire le chiavi MFA, è necessario installare l'applicazione "*Security Key*".



Prima di iniziare, assicurarsi di aver configurato il Bitcoin Wallet sul Ledger. È importante salvare correttamente il Mnemonic, poiché le chiavi utilizzate per la 2FA derivano da questo Mnemonic. È importante salvare correttamente il Mnemonic, in quanto le chiavi utilizzate per la 2FA derivano da questo Mnemonic. Se il Ledger viene smarrito o danneggiato, è possibile recuperare l'accesso alle chiavi inserendo la frase Mnemonic su un altro dispositivo Ledger (per il momento, gli identificatori FIDO2 in modalità "*passwordless*" non sono ancora supportati su Ledger, quindi non ci sono identificatori residenti).



Collegare il Ledger al computer e sbloccarlo.



![Image](assets/fr/01.webp)



Per installare l'applicazione, aprire il software [Ledger Live] (https://www.Ledger.com/Ledger-live), quindi andare alla scheda "*My Ledger*". Trovare l'applicazione "*Chiave di sicurezza*" e installarla sul dispositivo.



![Image](assets/fr/02.webp)



L'applicazione "*Chiave di sicurezza*" dovrebbe ora apparire insieme alle altre applicazioni installate sul Ledger.



![Image](assets/fr/03.webp)



Fare clic sull'applicazione per lasciarla aperta per le fasi successive dell'esercitazione.



![Image](assets/fr/04.webp)



## Utilizzare U2F/FIDO2 per 2FA con un Ledger



Accedere all'account che si desidera proteggere con l'autenticazione a due fattori. Ad esempio, utilizzerò un account Bitwarden. Di solito l'opzione 2FA si trova nelle impostazioni del servizio, sotto le schede "*autenticazione*", "*sicurezza*", "*login*" o "*password*".



![Image](assets/fr/05.webp)



Nella sezione dedicata all'autenticazione a due fattori, selezionare l'opzione "*Passkey*" (il termine può variare a seconda del sito utilizzato).



![Image](assets/fr/06.webp)



Spesso vi verrà chiesto di confermare la vostra password attuale.



![Image](assets/fr/07.webp)



Assegnare un nome alla chiave di sicurezza per facilitarne il riconoscimento, quindi fare clic su "*Leggi chiave*".



![Image](assets/fr/08.webp)



I dettagli del vostro account appariranno sul display del Ledger. Premere il pulsante "*Register*" per confermare (o entrambi i pulsanti contemporaneamente, a seconda del modello in uso).



![Image](assets/fr/09.webp)



La chiave di accesso è stata registrata con successo.



![Image](assets/fr/10.webp)



Registrare questa chiave di sicurezza.



![Image](assets/fr/11.webp)



D'ora in poi, quando si accede al proprio account, oltre alla solita password, verrà richiesto di collegare il proprio Ledger.



![Image](assets/fr/12.webp)



È quindi possibile premere il pulsante "*Log in*" sul display del Ledger per confermare l'autenticazione (o entrambi i pulsanti contemporaneamente, a seconda del modello in uso).



![Image](assets/fr/13.webp)



Il vantaggio di utilizzare un Hardware Wallet Ledger per l'autenticazione a due fattori è che è possibile recuperare facilmente le chiavi grazie alla frase Mnemonic. Oltre a questo backup di base, è possibile utilizzare un codice di emergenza fornito da ogni servizio in cui è stata attivata la 2FA. Questo codice di emergenza consente di collegarsi al proprio account in caso di smarrimento della chiave di sicurezza. Sostituisce quindi il 2FA per una connessione, se necessario.



Su Bitwarden, ad esempio, è possibile accedere a questo codice facendo clic su "*Vedi codice di recupero*".



![Image](assets/fr/14.webp)



Vi consiglio di conservare questo codice in un luogo diverso da quello in cui conservate la password principale, per evitare che vengano rubati insieme. Ad esempio, se la vostra password è salvata in un password manager, conservate il codice di emergenza 2FA su carta, separatamente.



Questo approccio offre due livelli di backup in caso di perdita del Ledger per l'autenticazione 2FA: un primo backup utilizzando la frase Mnemonic per tutti gli account e un secondo backup specifico per l'account utilizzando i codici di emergenza. Tuttavia, è importante **non confondere il ruolo del Mnemonic con quello del codice di emergenza**:




- La frase Mnemonic di 12 o 24 parole consente di accedere non solo alle chiavi utilizzate per la 2FA su tutti gli account, ma anche ai bitcoin protetti con il Ledger ;
- Il codice di emergenza consente di bypassare temporaneamente la richiesta di 2FA solo sull'account interessato (in questo esempio, solo su Bitwarden).



Congratulazioni, ora siete in grado di utilizzare il vostro Ledger per l'MFA! Se avete trovato utile questo tutorial, vi sarei molto grato se lasciaste un pollice Green qui sotto. Non esitate a condividere questa guida sui vostri social network. Grazie mille!



Vi consiglio anche quest'altro tutorial, in cui esaminiamo un'altra soluzione per l'autenticazione U2F e FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e
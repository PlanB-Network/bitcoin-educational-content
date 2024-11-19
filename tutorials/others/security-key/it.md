---
name: YubiKey 2FA
description: Come utilizzare una chiave di sicurezza fisica?
---
![cover](assets/cover.webp)

Oggi giorno, l'autenticazione a due fattori (2FA) è diventata essenziale per migliorare la sicurezza degli account online contro l'accesso non autorizzato. Con l'aumento degli attacchi informatici, fare affidamento solo su una password per proteggere i propri account è a volte insufficiente.

La 2FA introduce un ulteriore livello di sicurezza richiedendo una seconda forma di autenticazione in aggiunta alla tradizionale password. Questa verifica può assumere varie forme, come un codice inviato tramite SMS, un codice dinamico generato da un'app dedicata, o l'uso di una chiave di sicurezza fisica. L'uso della 2FA riduce significativamente i rischi che i tuoi account vengano compromessi, anche nel caso in cui la tua password venga rubata.

In un altro tutorial, ho spiegato come configurare e utilizzare un'applicazione 2FA TOTP:

https://planb.network/tutorials/others/authy

Qui, vedremo come utilizzare una chiave di sicurezza fisica come secondo fattore di autenticazione per tutti i tuoi account.

## Cos'è una chiave di sicurezza fisica?

Una chiave di sicurezza fisica è un dispositivo utilizzato per migliorare la sicurezza dei tuoi account online tramite l'autenticazione a due fattori (2FA). Questi dispositivi spesso assomigliano a piccole chiavette USB che devono essere inserite nella porta di un computer per verificare che sia davvero l'utente legittimo che sta tentando di connettersi.
![SECURITY KEY 2FA](assets/notext/01.webp)
Quando accedi a un account protetto dalla 2FA e utilizzi una chiave di sicurezza fisica, devi non solo inserire la tua solita password, ma anche inserire la chiave di sicurezza fisica nel tuo computer e premere un pulsante per convalidare l'autenticazione. Questo metodo aggiunge quindi un ulteriore livello di sicurezza, perché anche se qualcuno riesce ad ottenere la tua password, non sarà in grado di accedere al tuo account senza possedere fisicamente la chiave.

La chiave di sicurezza fisica è particolarmente efficace perché combina due diversi tipi di fattori di autenticazione: la prova di conoscenza (la password) e la prova di possesso (la chiave fisica).

Tuttavia, questo metodo di 2FA ha anche degli svantaggi. In primo luogo, devi sempre avere a disposizione la chiave di sicurezza se desideri accedere ai tuoi account. Potresti aver bisogno di aggiungerla al tuo portachiavi. In secondo luogo, a differenza di altri metodi di 2FA, l'uso di una chiave di sicurezza fisica comporta un costo iniziale poiché devi acquistare il piccolo dispositivo. Il prezzo delle chiavi di sicurezza varia generalmente tra i 30 € e i 100 € a seconda delle caratteristiche scelte.

## Quale chiave di sicurezza fisica scegliere?

Per scegliere la tua chiave di sicurezza, devono essere presi in considerazione diversi criteri.
Prima di tutto, è necessario verificare i protocolli supportati dal dispositivo. Come minimo, consiglio di scegliere una chiave che supporti OTP, FIDO2 e U2F. Questi dettagli sono solitamente evidenziati dai produttori nelle descrizioni dei prodotti. Per verificare la compatibilità di ogni chiave, puoi anche visitare [dongleauth.com](https://www.dongleauth.com/dongles/).
Inoltre, assicurati che la chiave sia compatibile con il tuo sistema operativo, anche se marchi noti come Yubikey supportano generalmente tutti i sistemi ampiamente utilizzati.

Dovresti anche selezionare la chiave in base al tipo di porte disponibili sul tuo computer o smartphone. Ad esempio, se il tuo computer ha solo porte USB-C, scegli una chiave con connettore USB-C. Alcune chiavi offrono anche opzioni di connessione tramite Bluetooth o NFC.
![SECURITY KEY 2FA](assets/notext/02.webp)
Puoi anche confrontare i dispositivi in base alle loro caratteristiche aggiuntive come la resistenza all'acqua e alla polvere, oltre alla forma e alle dimensioni della chiave.
Per quanto riguarda i marchi di chiavi di sicurezza, Yubico è il più noto con i suoi dispositivi [YubiKey](https://www.yubico.com/), che personalmente uso e raccomando. Anche Google offre un dispositivo con la [Titan Security Key](https://store.google.com/fr/product/titan_security_key). Per alternative open-source, [SoloKeys](https://solokeys.com/) (non OTP) e [NitroKey](https://www.nitrokey.com/products/nitrokeys) sono opzioni interessanti, ma non ho mai avuto l'occasione di testarle.
## Come usare una chiave di sicurezza fisica?

Una volta ricevuta la tua chiave di sicurezza, non è richiesta alcuna configurazione specifica. La chiave è normalmente pronta all'uso al momento della ricezione. Puoi subito usarla per proteggere i tuoi account online che supportano questo tipo di autenticazione. Ad esempio, ti mostrerò come proteggere il mio account Proton mail con questa chiave di sicurezza fisica.
![SECURITY KEY 2FA](assets/notext/03.webp)
Troverai l'opzione per attivare il 2FA nelle impostazioni del tuo account, spesso sotto la sezione "*Password*" o "*Sicurezza*". Clicca sulla casella o sul bottone che ti permette di attivare il 2FA con una chiave fisica.
![SECURITY KEY 2FA](assets/notext/04.webp)
Collega la tua chiave al computer.
![SECURITY KEY 2FA](assets/notext/05.webp)
Tocca il bottone sulla tua chiave di sicurezza per convalidare.
![SECURITY KEY 2FA](assets/notext/06.webp)
Inserisci un nome per ricordare quale chiave hai usato.
![SECURITY KEY 2FA](assets/notext/07.webp)
Ed ecco fatto, la tua chiave di sicurezza è stata aggiunta con successo per l'autenticazione 2FA del tuo account.
![SECURITY KEY 2FA](assets/notext/08.webp)
Nel mio esempio, se provo a riconnettermi al mio account Proton mail, mi verrà prima chiesto di inserire la mia password insieme al mio nome utente. Questo è il primo fattore di autenticazione.
![SECURITY KEY 2FA](assets/notext/09.webp)
Poi, mi viene chiesto di collegare la mia chiave di sicurezza per il secondo fattore di autenticazione.
![SECURITY KEY 2FA](assets/notext/10.webp)
Successivamente, devo toccare il bottone sulla chiave fisica per convalidare l'autenticazione, e sono riconnesso al mio account Proton mail.
![SECURITY KEY 2FA](assets/notext/11.webp)
Ripeti questa operazione per tutti gli account online che desideri proteggere in questo modo, specialmente per gli account critici come i tuoi account email, i tuoi gestori di password, i tuoi servizi di cloud e archiviazione online, o i tuoi account finanziari.
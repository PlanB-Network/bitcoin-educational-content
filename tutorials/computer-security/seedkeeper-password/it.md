---
name: Seedkeeper - Gestore di password
description: Come salvare le password con la smart card Seedkeeper?
---

![cover](assets/cover.webp)

Seedkeeper è una smartcard sviluppata da Satochip, un'azienda belga specializzata in soluzioni hardware per la gestione e la protezione dei segreti digitali. Rinomata per la sua gamma di smartcard per l'ecosistema Bitcoin, Satochip ha concepito Seedkeeper come alternativa ai metodi tradizionali di memorizzazione di frasi mnemoniche e altri segreti digitali.

In concreto, il Seedkeeper ha la forma di una smart card multifunzionale, certificata EAL6, dotata di un processore sicuro e di una memoria a prova di manomissione (un cosiddetto "Secure Element"). Come suggerisce il nome, il suo ruolo è quello di memorizzare le mnemoniche e le password del portafoglio Bitcoin in modo criptato e protetto. Con Seedkeeper, è possibile generare, importare, organizzare e salvare i propri segreti direttamente nel componente sicuro della carta.

A mio parere, Seedkeeper ha due usi principali, che esploreremo in due esercitazioni separate:
- **Memorizzazione di frasi mnemoniche Bitcoin**: invece di scrivere le vostre 12 o 24 parole su carta, puoi importarle nella smartcard e proteggerle con un codice PIN.
- **Gestione delle password**: puoi generare password forti tramite l'applicazione Seedkeeper e memorizzale direttamente nella smartcard, ottenendo così un gestore di password offline comodo e facile da usare.

Tecnicamente, Seedkeeper ha una capacità di 8192 byte, che gli consente di memorizzare un minimo di 50 segreti separati (il numero esatto dipenderà dalla loro dimensione e dai metadati associati a ciascuno di essi). Puoi accedere a Seedkeeper sia [tramite un lettore di smart card collegato](https://satochip.io/accessories/) a un computer, sia tramite l'applicazione mobile con connessione NFC. L'intero sistema funziona in modalità offline, senza connessione a Internet, garantendo una superficie di attacco limitata.

![Image](assets/fr/001.webp)

Una caratteristica particolarmente interessante è la possibilità di duplicare il contenuto di un Seedkeeper in un altro per creare un backup. In questa guida ti mostrerò come fare.

In questo tutorial, ci occuperemo solo dell'uso di SeedKeeper per le password tradizionali, alla maniera di un gestore di password. Se desideri utilizzare SeedKeeper per salvare le frasi mnemoniche di un Bitcoin wallet, consulta quest'altro tutorial:

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356


## 1. Come si ottiene un Seedkeeper?

Esistono due modi principali per ottenere Seedkeeper. Puoi [acquistarlo direttamente dal negozio ufficiale di Satochip](https://satochip.io/product/seedkeeper/) o da un rivenditore autorizzato. Ma poiché [l'applet Seedkeeper è open-source](https://github.com/Toporin/Seedkeeper-Applet), puoi anche installarla da solo su [una smart card vuota](https://satochip.io/product/blank-javacard-for-diy-project/).

Se desideri utilizzare la funzionalità di backup di Seedkeeper, è ovviamente necessario acquistare due smartcard.


## 2. Installazione del client Seedkeeper

Il primo passo consiste nell'installare il software sul computer o sullo smartphone. Su un PC, è necessario [scaricare l'ultima versione di Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Sui cellulari, l'applicazione Seedkeeper è disponibile su [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) e su [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).

![Image](assets/fr/002.webp)


## 3. Inizializzazione di Seedkeeper

Avvia l'applicazione e fai clic sul pulsante "_Click & Scan_".

![Image](assets/fr/003.webp)

Ti verrà richiesto un codice PIN per la tua Seedkeeper card. Trattandosi di una nuova carta, non è ancora stato definito un PIN. Immetti un codice qualsiasi per saltare questo passaggio, quindi fai clic su "_Avanti_".

![Image](assets/fr/004.webp)

Posiziona quindi la scheda sul retro dello smartphone. L'applicazione rileverà che Seedkeeper non è ancora stato inizializzato e chiederà di impostare il codice PIN della smart card, di lunghezza compresa tra 4 e 16 caratteri. Per una sicurezza ottimale, scegli un codice PIN robusto, il più lungo possibile, casuale e composto da un'ampia varietà di caratteri. Questo PIN è l'unica barriera contro l'accesso fisico alle tue password.

**Ricordati di salvare il PIN**, ad esempio in un gestore di password o su un supporto fisico separato. In quest'ultimo caso, non conservare mai il supporto contenente il PIN nello stesso luogo in cui si trova il tuo Seedkeeper, altrimenti questa sicurezza diventerà inutile. È importante avere un backup affidabile: senza il PIN, non sarà possibile recuperare i segreti memorizzati sul Seedkeeper.

![Image](assets/fr/005.webp)

Conferma il codice PIN una seconda volta.

![Image](assets/fr/006.webp)

Seedkeeper è ora inizializzato. È possibile sbloccarlo inserendo il codice PIN appena impostato.

![Image](assets/fr/007.webp)

A questo punto accedi alla pagina di gestione della smart card.

![Image](assets/fr/008.webp)


## 4. Salvare le password su Seedkeeper

Una volta sbloccato Seedkeeper, fai clic sul pulsante "_+_".

![Image](assets/fr/009.webp)

Seleziona "_Genera segreto_". L'opzione "_Importa un segreto_" consente di salvare un segreto esistente (ad esempio, una password creata in passato).

![Image](assets/fr/010.webp)

Nel nostro caso, vogliamo salvare una password. Fai clic su "_Password_".

![Image](assets/fr/011.webp)

Assegna una "_Etichetta_" a questo segreto, in modo da poterlo identificare facilmente se si memorizzano diverse informazioni in Seedkeeper. Puoi inoltre aggiungere un identificatore associato alla password e all'URL del sito.

![Image](assets/fr/012.webp)

Scegli la lunghezza e i parametri della password, quindi fai clic su "_Generare_" e poi su "_Importare_".

![Image](assets/fr/013.webp)

Posiziona Seedkeeper sul retro dello smartphone.

![Image](assets/fr/014.webp)

La password è stata registrata.

![Image](assets/fr/015.webp)


## 5. Accedere alla password di Seedkeeper

Se vuoi controllare la tua password, prendi il tuo Seedkeeper e fai clic sul pulsante "_Click & Scan_".

![Image](assets/fr/016.webp)

Immetti il codice PIN, quindi premi "_Avanti_".

![Image](assets/fr/017.webp)

Posiziona Seedkeeper sul retro dello smartphone.

![Image](assets/fr/018.webp)

In questo modo si accede a un elenco di tutti i segreti registrati. In questo esempio, voglio visualizzare la password del mio account Plan ₿ Academy, quindi faccio clic su di essa.

![Image](assets/fr/019.webp)

Premi il pulsante "_Rivela_".

![Image](assets/fr/020.webp)

Esegui nuovamente la scansione del Seedkeeper.

![Image](assets/fr/021.webp)

La password salvata in precedenza appare ora sullo schermo. Puoi copiarla e utilizzarla sul sito web in questione.

![Image](assets/fr/022.webp)


## 6. Backup di Seedkeeper

Ora faremo un backup del mio Seedkeeper su un secondo Seedkeeper, in modo da avere due copie. Questa ridondanza può far parte di una strategia per proteggere le password più importanti: ad esempio, conservando i Seedkeeper in due luoghi diversi per limitare i rischi fisici, oppure affidandone una copia a un parente fidato.

Per farlo, porta con te il secondo Seedkeeper (ricorda di identificare uno dei due con un marchio per evitare confusione). Inizia ad inizializzarlo, come descritto nella fase 3 di questa guida. Ancora una volta, scegli un codice PIN forte. A seconda della tua strategia, puoi optare per un PIN diverso o mantenere lo stesso.

![Image](assets/fr/023.webp)

Apri l'applicazione, fai clic su "_Click & Scan_", inserisci il PIN del tuo Seedkeeper n°1 (sorgente), quindi scansionalo.

![Image](assets/fr/024.webp)

Accedi così alla pagina iniziale, con l'elenco dei segreti. Fai clic sui tre puntini in alto a destra dell'interfaccia.

![Image](assets/fr/025.webp)

Seleziona "_Esegui un backup_", quindi premi "_Avvia_".

![Image](assets/fr/026.webp)

Inserisci il codice PIN della scheda di backup (Seedkeeper n°2).

![Image](assets/fr/027.webp)

Quindi scansiona la scheda.

![Image](assets/fr/028.webp)

Fai lo stesso con la scheda principale (Seedkeeper n°1), quindi fai clic su "_Esegui un backup_".

![Image](assets/fr/029.webp)

Il Seedkeeper n°2 contiene ora tutti i segreti memorizzati sul Seedkeeper n°1.

![Image](assets/fr/030.webp)

Puoi scansionare il Seedkeeper n°2 per verificare che i segreti siano stati copiati.

![Image](assets/fr/031.webp)

Questo è tutto! Ora sai come utilizzare Seedkeeper per memorizzare le tue password. In una prossima esercitazione vedrai come utilizzare Seedkeeper per eseguire il backup di un Bitcoin wallet. Ti invito anche a scoprire il suo uso combinato con SeedSigner:

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

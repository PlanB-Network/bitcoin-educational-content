---
name: Custode dei semi
description: Come si esegue il backup del wallet Bitcoin con la smart card Seedkeeper?
---

![cover](assets/cover.webp)



Seedkeeper è una smartcard sviluppata da Satochip, un'azienda belga specializzata in soluzioni hardware per la gestione e la protezione dei segreti digitali. Rinomata per la sua gamma di smartcard per l'ecosistema Bitcoin, Satochip ha progettato Seedkeeper come alternativa ai metodi tradizionali di memorizzazione delle frasi mnemoniche.



Concretamente, il Seedkeeper ha la forma di una smart card multifunzionale, certificata EAL6, con un processore sicuro e una memoria a prova di manomissione (un cosiddetto "Secure Element"). Come suggerisce il nome, il suo ruolo è quello di memorizzare mnemoniche e password Bitcoin wallet in modo criptato e protetto. Con Seedkeeper, è possibile generate, importare, organizzare e salvare i propri segreti direttamente nel componente sicuro della scheda.



A mio parere, Seedkeeper ha due usi principali, che esploreremo in due esercitazioni separate:




- Memorizzazione di frasi mnemoniche Bitcoin**: invece di scrivere le vostre 12 o 24 parole su carta, potete importarle nella smartcard e proteggerle con un codice PIN.
- Gestione delle password**: è possibile gestire generate password forti tramite l'applicazione Seedkeeper e memorizzarle direttamente nella smartcard, ottenendo così un gestore di password offline comodo e facile da usare.



Tecnicamente, Seedkeeper ha una capacità di 8192 byte, che gli consente di memorizzare un minimo di 50 segreti separati (il numero esatto dipenderà dalla loro dimensione e dai metadati associati a ciascuno di essi). Si può accedere a Seedkeeper sia [tramite un lettore di smart card collegato](https://satochip.io/accessories/) a un computer, sia tramite l'applicazione mobile con connessione NFC. L'intero sistema funziona in modalità offline, senza connessione a Internet, garantendo una superficie di attacco limitata.



![Image](assets/fr/001.webp)



Una caratteristica particolarmente interessante è la possibilità di duplicare il contenuto di un Seedkeeper in un altro per creare un backup. In questa guida vi mostreremo come fare.



Seedkeeper è molto interessante anche in combinazione con l'hardware stateless wallet, come SeedSigner o Specter DIY. In questo caso, non è necessario utilizzare il client di Satochip sul computer o sul cellulare. Seedkeeper mantiene il seed nel suo secure element e può essere utilizzato direttamente con il dispositivo di firma, eliminando la necessità di un codice QR cartaceo. Non svilupperò questo particolare caso d'uso in questa guida, poiché è oggetto di un'altra guida dedicata:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Quale caso d'uso per Seedkeeper?



In questa guida tratterò solo i casi d'uso relativi a Bitcoin, poiché è questo l'argomento della guida. Non ci occuperemo della funzionalità di gestione delle password, che sarà oggetto di un altro tutorial.



Rispetto a un semplice backup cartaceo della frase mnemonica, l'uso di un Seedkeeper presenta diversi vantaggi:





- Resistente ai furti:** Il seed nel wallet non è accessibile in chiaro. Per estrarlo, è necessario conoscere il PIN del Seedkeeper. Un ladro che si impossessi del dispositivo non potrà fare nulla senza questo codice.





- Suddivisione del rischio su due fattori:** è possibile suddividere la sicurezza tra un fattore digitale e uno fisico. Ad esempio, se si memorizza il PIN del Seedkeeper nel proprio gestore di password, per ottenere il seed è necessario sia l'accesso a questo gestore che il possesso fisico della smartcard (una probabilità di attacco significativamente ridotta).





- Gestione centralizzata:** Seedkeeper facilita la gestione di più semi provenienti da portafogli diversi.





- Backup facili: ** è sufficiente duplicare i backup crittografati su altri SeedKeepers.



Tuttavia, rispetto a un semplice backup cartaceo del vostro seed, presenta una serie di svantaggi:





- Il prezzo:** sebbene modesto (circa 25 euro), è comunque superiore a quello di un foglio di carta.





- Dipendenza da un dispositivo informatico generico:** l'inserimento e la gestione di seed richiedono un computer o uno smartphone, il che significa che il mnemonico passa attraverso una macchina con una superficie di attacco molto più ampia rispetto all'hardware di wallet. Questo può rappresentare un rischio se la macchina viene compromessa. Per questo motivo non consiglio di usare Seedkeeper per memorizzare il seed di un hardware wallet (tranne che nell'uso stateless senza computer, come con SeedSigner). Il ruolo dell'hardware wallet è proprio quello di memorizzare il seed in un ambiente minimalista e altamente sicuro. Inserendo manualmente il seed sul computer abituale, esso non è più confinato nell'hardware wallet: finisce anche su una macchina generica, esposta a molteplici vettori di attacco. Quindi è meglio usare Seedkeeper per un wallet caldo piuttosto che per uno freddo (tranne SeedSigner / hardware wallet stateless).





- Il rischio di perdita legato al PIN:** l'inaccessibilità diretta del seed, a differenza di un backup cartaceo, fornisce effettivamente una protezione contro il furto fisico. Ma come sempre, la sicurezza è un gioco di equilibri tra il rischio di furto e il rischio di perdita. Se il backup richiede un PIN, la perdita di questo codice renderà impossibile recuperare la frase mnemonica e quindi accedere ai bitcoin.



Alla luce di questi vantaggi e svantaggi, ritengo che i migliori utilizzi di Seedkeeper (a parte la sua funzione di password manager) siano, da un lato, la memorizzazione dei semi dei vostri **portafogli software**, dato che risiedono già sul vostro telefono o computer, o del vostro hardware wallet senza schermo come lo Satochip, e dall'altro lato, l'utilizzo in combinazione con hardware wallet senza stato come il SeedSigner, dove si rivela davvero efficace.



Un altro caso d'uso particolarmente interessante per Seedkeeper è la possibilità di eseguire il backup sicuro e affidabile dei *descrittori* dei portafogli.



## 2. Come si ottiene un Seedkeeper?



Esistono due modi principali per ottenere Seedkeeper. Potete [acquistarlo direttamente dal negozio ufficiale di Satochip](https://satochip.io/product/seedkeeper/) o da un rivenditore autorizzato. Ma poiché [l'applet Seedkeeper è open-source](https://github.com/Toporin/Seedkeeper-Applet), è anche possibile installarla da soli su [una smart card vuota](https://satochip.io/product/blank-javacard-for-diy-project/).



Se si desidera utilizzare la funzionalità di backup di Seedkeeper, è ovviamente necessario acquistare due smartcard.



## 3. Installazione del client Seedkeeper



In questa esercitazione, eseguiremo il backup del nostro portafoglio seed sul nostro Seedkeeper. Il primo passo consiste nell'installare il software sul computer o sullo smartphone. Su un PC, è necessario [scaricare l'ultima versione di Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Sui cellulari, l'applicazione Seedkeeper è disponibile su [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) e su [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Inizializzazione del Seedkeeper



Avviare l'applicazione e fare clic sul pulsante "*Click & Scan*".



![Image](assets/fr/003.webp)



Vi verrà richiesto un codice PIN per la vostra Seedkeeper. Trattandosi di una nuova carta, non è ancora stato definito un PIN. Immettere un codice qualsiasi per saltare questo passaggio, quindi fare clic su "*Avanti*".



![Image](assets/fr/004.webp)



Posizionare quindi la scheda sul retro dello smartphone. L'applicazione rileverà che Seedkeeper non è ancora stato inizializzato e chiederà di impostare il codice PIN della smart card, di lunghezza compresa tra 4 e 16 caratteri. Per una sicurezza ottimale, scegliete una password forte, il più lunga possibile, casuale e composta da un'ampia varietà di caratteri. Il codice PIN è l'unica barriera contro l'accesso fisico alla frase di recupero.



**Ricordarsi di salvare il PIN**, ad esempio in un gestore di password o su un supporto fisico separato. In quest'ultimo caso, non conservate mai il supporto contenente il PIN nello stesso luogo in cui si trova il vostro Seedkeeper, altrimenti questa sicurezza diventerà inutile. È importante avere un backup affidabile: senza il PIN, non sarà possibile recuperare i segreti memorizzati sul Seedkeeper.



![Image](assets/fr/005.webp)



Confermare il codice PIN una seconda volta.



![Image](assets/fr/006.webp)



Il Seedkeeper è ora inizializzato. È possibile sbloccarlo inserendo il codice PIN appena impostato.



![Image](assets/fr/007.webp)



A questo punto si accede alla pagina di gestione della smart card.



![Image](assets/fr/008.webp)



## 5. Registrare un seed su Seedkeeper



Una volta sbloccato il Seedkeeper, fare clic sul pulsante "*+*".



![Image](assets/fr/009.webp)



Selezionare "Importa segreto*". L'opzione "*Genera segreto*" consente di creare una nuova frase mnemonica direttamente dall'applicazione.



![Image](assets/fr/010.webp)



Nel nostro caso, vogliamo salvare il seed nel nostro portafoglio. Fare clic su "*Mnemonic*".



![Image](assets/fr/011.webp)



Assegnare un'"etichetta" a questo segreto, in modo da poterlo identificare facilmente se si memorizzano diverse informazioni nel Seedkeeper.



![Image](assets/fr/012.webp)



Inserire quindi la frase di recupero nell'apposito campo. Se lo desiderate, potete anche aggiungere un passphrase BIP39 o i vostri *Descrittori*. Cliccare quindi su "Importazione*".



![Image](assets/fr/013.webp)



*Il mnemonico visualizzato in questa immagine è fittizio e non appartiene a nessuno. È solo un esempio. Non rivelate mai a nessuno la vostra mnemonica, altrimenti vi verranno rubati i bitcoin



Posizionare Seedkeeper sul retro dello smartphone.



![Image](assets/fr/014.webp)



Il vostro seed è stato registrato.



![Image](assets/fr/015.webp)



## 6. Accedi al tuo seed su Seedkeeper



Se volete controllare la vostra frase mnemonica, prendete il vostro Seedkeeper e fate clic sul pulsante "*Click & Scan*".



![Image](assets/fr/016.webp)



Immettere il codice PIN, quindi premere "*Avanti*".



![Image](assets/fr/017.webp)



Posizionare Seedkeeper sul retro dello smartphone.



![Image](assets/fr/018.webp)



In questo modo si accede a un elenco di tutti i segreti registrati. In questo esempio, voglio visualizzare il seed del mio portafoglio "*Blockstream App*", quindi faccio clic su di esso.



![Image](assets/fr/019.webp)



Premere il pulsante "*Rivela*".



![Image](assets/fr/020.webp)



Eseguire nuovamente la scansione del Seedkeeper.



![Image](assets/fr/021.webp)



La frase mnemonica precedentemente registrata viene ora visualizzata sullo schermo.



![Image](assets/fr/022.webp)



## 7. Backup di Seedkeeper



Ora faremo un backup del mio Seedkeeper su un secondo Seedkeeper in modo da avere due copie. Questa ridondanza può essere parte di una strategia per proteggere i bitcoin: ad esempio, conservare la frase in due luoghi separati per limitare i rischi fisici, o affidare una copia a un parente fidato come parte di un piano di eredità.



Per farlo, portate con voi il secondo Seedkeeper (ricordate di identificare uno dei due con un marchio per evitare confusione). Iniziate ad inizializzarlo, come descritto al punto 4 di questa guida. Scegliete ancora una volta una password forte. A seconda della vostra strategia, potete optare per una password diversa o mantenere la stessa.



![Image](assets/fr/023.webp)



Aprite l'applicazione, fate clic su "*Click & Scan*", inserite la password del vostro Seedkeeper n°1 (sorgente), quindi scansionatelo.



![Image](assets/fr/024.webp)



Si accede così alla pagina iniziale, con l'elenco dei segreti. Fare clic sui tre puntini in alto a destra dell'interfaccia.



![Image](assets/fr/025.webp)



Selezionare "*Esegui un backup*", quindi premere "*Avvia*".



![Image](assets/fr/026.webp)



Inserire il codice PIN della scheda di backup (Seedkeeper n°2).



![Image](assets/fr/027.webp)



Quindi scansionare la scheda.



![Image](assets/fr/028.webp)



Fare lo stesso con la scheda principale (Seedkeeper n°1), quindi fare clic su "*Esegui un backup*".



![Image](assets/fr/029.webp)



Il Seedkeeper n°2 contiene ora tutti i segreti memorizzati nel Seedkeeper n°1.



![Image](assets/fr/030.webp)



È possibile scansionare il Seedkeeper n°2 per verificare che i segreti siano stati copiati.



![Image](assets/fr/031.webp)



Questo è tutto! Ora sapete come utilizzare Seedkeeper per salvare la frase mnemonica di un Bitcoin wallet. In una prossima esercitazione vedremo come utilizzare Seedkeeper per memorizzare le password. Vi invito anche a scoprire il suo uso combinato con SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

In questo tutorial abbiamo menzionato più volte i ***Descrittori*** del vostro portafoglio Bitcoin. Non sapete cosa sono? Non sapete cosa sono? In questo caso, vi consiglio di seguire il nostro corso di formazione gratuito CYP 201, che approfondisce tutti i meccanismi di funzionamento dei portafogli HD!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
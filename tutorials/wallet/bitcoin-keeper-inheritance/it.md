---
name: Bitcoin Keeper - Piano di eredità
description: Pianificate la vostra trasmissione di bitcoin con Bitcoin Keeper
---

![cover](assets/cover.webp)



Il trasferimento delle attività del Bitcoin è una delle sfide più sottovalutate dai titolari. A differenza di un conto bancario, dove l'istituto finanziario può trasmettere i fondi agli eredi legittimi, il Bitcoin si basa interamente sul possesso di chiavi private. Un erede legale perfettamente legittimo non sarà mai in grado di accedere ai fondi senza queste chiavi, mentre un individuo malintenzionato in possesso dei segreti sarà in grado di spenderli senza alcuna formalità.



In questo secondo tutorial di Bitcoin Keeper, esploriamo le funzionalità premium dedicate alla pianificazione successoria. L'applicazione offre strumenti avanzati per la creazione di Enhanced Vault, con meccanismi di protezione temporizzati grazie a Miniscript, e documenti di accompagnamento per guidare i vostri cari.



Questa guida presuppone che abbiate già acquisito le nozioni di base di Bitcoin Keeper (creazione di portafogli, multisig classico, aggiunta di chiavi hardware) come spiegato nel nostro primo tutorial:



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-22cbfb8d-790f-4a6f-a92f-93a117e1e65c

![video](https://youtu.be/tCld_-n2d30)



## Piani di abbonamento Bitcoin Keeper



Bitcoin Keeper opera su un modello freemium con tre livelli di abbonamento che offrono funzionalità progressive. Per accedere ai piani, andare alla scheda **Più**, quindi toccare il piano corrente (quello predefinito è "Pleb") per aprire la schermata **Gestione abbonamento**.



![Plans d'abonnement](assets/fr/01.webp)



Il piano **Pleb** (gratuito) fornisce l'accesso all'essenziale: creazione illimitata di portafogli a chiave singola e multipla, compatibilità con tutti i principali portafogli hardware (Coldcard, Trezor, Ledger, Jade, Tapsigner...), controllo delle monete, etichettatura e connessione a un server Electrum personale. Questo piano è sufficiente per l'utilizzo standard e anche per le configurazioni classiche del multi-sig.



Il piano **Hodler** (9,99 euro/mese, con 1 mese gratuito se si paga annualmente) include tutte le funzionalità di Pleb e aggiunge backup crittografati nel cloud (iCloud o Google Drive) per ripristinare le casseforti su qualsiasi dispositivo, Server Key per aggiungere politiche di spesa automatiche e 2FA al di sopra di una certa soglia, e Canary Wallets per rilevare accessi non autorizzati alle chiavi.



Il piano **Mani di diamante** (29,99 euro/mese, con 1 mese gratuito se pagato annualmente) è il pacchetto completo per la pianificazione successoria. Include l'intero piano Hodler e sblocca la Chiave di Eredità (attivazione differita), la Chiave di Emergenza (chiave di emergenza per il recupero in caso di smarrimento), gli strumenti e i documenti per la Pianificazione dell'Eredità e una chiamata di supporto con il team Concierge per convalidare la configurazione. Questa è l'offerta per i bitcoiners che desiderano trasmettere la propria eredità a più generazioni.



Punto importante: i caveau creati rimarranno accessibili anche se si passa nuovamente al piano gratuito. Le vostre configurazioni sono basate su standard aperti (BSMS, Miniscript) e funzionano indipendentemente dal vostro abbonamento.



## Documenti di eredità



Una volta attivato l'abbonamento a Diamond Hands, accedere alla sezione **Documenti di successione** dalla scheda Altro. Bitcoin Keeper fornisce cinque documenti di esempio per strutturare il vostro piano successorio, oltre a una sezione di suggerimenti:



![Documents d'héritage](assets/fr/02.webp)





- Seed Words Template**: un modello per annotare in modo ordinato le vostre frasi di recupero
- Contatti di fiducia**: un modello per elencare i contatti delle persone di fiducia coinvolte nel piano (notaio, avvocato, eredi, custodi delle chiavi)
- Additional Share Key**: un documento che riporta le informazioni tecniche di ciascuna chiave: Codice PIN, percorso di derivazione, posizione fisica, tipo di dispositivo e qualsiasi altra informazione utile per l'identificazione e l'utilizzo della chiave
- Istruzioni per il recupero**: istruzioni passo-passo per il recupero dei fondi da parte dell'erede o del beneficiario
- Lettera all'avvocato**: una lettera precompilata che può essere adattata all'avvocato o al notaio



La sezione **Consigli per l'eredità** offre consigli pratici su come assicurare le chiavi agli eredi e ottimizzare il piano di eredità.



Personalizzate questi documenti in base alla vostra situazione e conservateli in un luogo sicuro, separato dalle chiavi stesse.



## Configurazione del backup in-the-cloud



Prima di creare il vault legacy, attivare il backup nel cloud per proteggere i file di configurazione. Dalla scheda Altro, premere **Backup cloud personale**.



![Configuration Cloud Backup](assets/fr/03.webp)



Scegliere una password forte per criptare i backup. Questa password protegge solo i file di configurazione di wallet (non le chiavi private). Confermare la password e premere **Conferma**. I backup saranno archiviati su iCloud o Google Drive, a seconda del dispositivo. Premere **Backup Now** per avviare il primo backup.



## Importare le chiavi hardware



Per il nostro esempio, creeremo una cassaforte 2 di 3 con due chiavi aggiuntive (Ereditarietà ed Emergenza). Cominciamo importando tutte le chiavi necessarie nella scheda **Keys**.



![Import des clés hardware](assets/fr/04.webp)



Premere **Aggiungi chiave**, quindi selezionare **Aggiungi chiave da un hardware** per collegare un wallet hardware. Il Bitcoin Keeper supporta molti dispositivi: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner e Specter Solutions.



Nella nostra configurazione, importiamo :




- 2 chiavi **Coldcard** (MK4SP e MK4)
- 2 tasti **Tapsigner** (Metro e Genesis)



Per aggiungere una Coldcard, selezionarla dall'elenco e seguire le istruzioni sullo schermo per esportare la chiave pubblica tramite codice QR, file, USB o NFC. Per maggiori dettagli sull'utilizzo della Coldcard o del Tapsigner, consultare i nostri tutorial dedicati:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Una volta importate tutte le chiavi, le troverete nella scheda Chiavi con i loro nomi personalizzati.



## Creare il wallet tradizionale



Passiamo alla creazione del tronco. Dalla scheda **Portafogli**, premere **Aggiungi Wallet**, selezionare **Bitcoin Wallet**, quindi **Crea Wallet**.



![Création du wallet](assets/fr/05.webp)



Scegliere il tipo di wallet. Per il nostro piano legacy, selezionare **2 di 3 tasti multipli**. In fondo alla schermata, attivare **Opzioni di sicurezza avanzate** e premere **Procedi**.



![Options de sécurité avancées](assets/fr/06.webp)



Nel popup Opzioni di sicurezza avanzate, selezionare :




- Chiave di ereditarietà**: una chiave aggiuntiva che verrà aggiunta al quorum dopo un determinato periodo di tempo
- Chiave di emergenza**: una chiave con controllo totale differito per recuperare i fondi in caso di perdita della chiave



Premere **Salva modifiche**. Quindi selezionare le 3 chiavi che comporranno il wallet tra quelle importate (ad esempio, Seed Key, Coldcard MK4SP e Tapsigner Metro).



## Definizione di scadenze chiave speciali



La schermata successiva consente di configurare la chiave di emergenza e la chiave di eredità. Qui si definiscono i ritardi che regolano l'attivazione di queste chiavi speciali.



![Configuration des délais](assets/fr/07.webp)



Per la **chiave di emergenza**, selezionare la chiave hardware che servirà come backup definitivo (qui Coldcard MK4) e scegliere il ritardo di attivazione (nel nostro esempio: 2 anni). A differenza della Chiave di Eredità, la Chiave di Emergenza non si aggiunge al quorum: vi permette di **bypassare completamente il multisig** e vi dà il controllo totale sui fondi dopo la scadenza del termine. È la soluzione di ultima istanza: se diverse chiavi vengono perse o distrutte, questa singola chiave consente di recuperare tutto. Deve quindi essere protetta con il massimo rigore.



Per la **chiave di eredità**, selezionare la chiave destinata all'erede (qui Coldcard MK4SP) e scegliere il ritardo (nel nostro esempio: 1 anno). Dopo un anno senza movimenti, questa chiave **verrà aggiunta al quorum di firma**. In pratica, il vostro wallet 2 di 3 diventerà un wallet 2 di 4 una volta trascorso questo periodo, consentendo all'erede di partecipare alla firma insieme alle chiavi esistenti.



### Come funzionano gli orologi a tempo?



Il Bitcoin Keeper utilizza **tempi assoluti** (CLTV - CheckLockTimeVerify), resi possibili da Miniscript. A differenza dei timelock relativi (CSV), che iniziano quando ogni UTXO viene ricevuto, i timelock assoluti funzionano con una **data di scadenza fissa** definita quando il wallet viene creato.



In concreto, se si crea un wallet oggi con una chiave di eredità di 1 anno, la data di attivazione sarà "oggi + 1 anno". Tutti i fondi depositati in questo wallet, indipendentemente dalla data di deposito, saranno accessibili tramite la chiave di eredità in questa stessa data.



Il vantaggio dei timelock assoluti è che consentono tempi di consegna superiori a 15 mesi (il limite dei timelock CSV relativi), il che spiega perché Bitcoin Keeper può offrire opzioni come 2 anni.



### Il meccanismo di aggiornamento



Per evitare l'attivazione di chiavi speciali durante la vostra vita, dovete periodicamente "aggiornare" il vostro wallet. Con i timelock assoluti, ciò comporta la **creazione del wallet con una nuova data di scadenza** spostata nel futuro, quindi il trasferimento dei fondi a questo nuovo wallet.



Bitcoin Keeper semplifica questo processo con una funzione di aggiornamento integrata. L'applicazione gestisce automaticamente la complessità in background: è sufficiente seguire i passaggi guidati, senza dover creare manualmente un nuovo wallet o trasferire personalmente i fondi. Pianificate questa operazione su base regolare, con largo anticipo rispetto alla scadenza del periodo più breve configurato. Ad esempio, con una chiave di eredità di 1 anno, aggiornatela ogni 9-10 mesi per mantenere un margine di sicurezza.



## Salvare ed esportare la configurazione



Una volta creato il wallet, l'applicazione ricorda di salvare il file di configurazione. **Questo passaggio è fondamentale**: senza questo file, i vostri eredi non potranno ricostituire il wallet multisig.



![Export de la configuration](assets/fr/08.webp)



Premere **Backup Wallet Recovery File**. Sono disponibili diverse opzioni di esportazione:




- Esportazione PDF**: genera un documento completo con tutte le informazioni del wallet
- Mostra QR**: visualizza un codice QR per importare la configurazione su un altro dispositivo
- Airdrop / Esportazione file**: esporta il file tramite le opzioni di condivisione
- NFC**: condivisione tramite NFC con un dispositivo compatibile



Moltiplicare le copie: una presso il notaio, una nella cassaforte della banca, una versione digitale crittografata. Il nuovo wallet appare ora nella scheda Portafoglio con le etichette "Chiave multipla", "2 di 3", "Chiave di eredità" e "Chiave di emergenza".



## Creare un canarino Wallet



Il Canary Wallet è un sistema di allarme rapido. L'idea è che ogni chiave utilizzata in una chiave multipla wallet può essere utilizzata anche in una chiave singola wallet separata. Depositando una piccola somma su questo "canarino" wallet, qualsiasi movimento non autorizzato segnala la compromissione della chiave.



![Canary Wallets](assets/fr/09.webp)



Esistono due modi per configurare un canarino Wallet. Dalla scheda **Altro**, premere **Portafogli canarini** nella sezione "Chiavi e portafogli". La schermata spiega il principio: se qualcuno accede a una delle vostre chiavi e trova fondi nella chiave singola wallet associata, tenterà di rimuoverli, avvisandovi.



![Configuration Canary depuis une clé](assets/fr/10.webp)



È anche possibile configurare il Canary direttamente da una chiave. Nella scheda **Keys**, selezionare una chiave (ad es. Tapsigner Genesis), premere l'icona **Settings** (ingranaggio), quindi **Canary Wallet**. Il canarino wallet associato si apre, pronto a ricevere alcuni satoshi di sorveglianza.



Depositate una piccola somma (qualche migliaio di satoshi) su ogni Wallet Canary. Se questi fondi si spostano senza il vostro consenso, rimuovete immediatamente la chiave compromessa dalle vostre casseforti multisig.



## Le migliori pratiche



**Testate la vostra configurazione** con una piccola somma di denaro prima di inserirne una grande. Inviate qualche migliaio di satoshi al caveau, quindi provate una spesa in uscita per verificare che abbiate imparato il processo di firma con ogni dispositivo. Provate anche a importare il file di configurazione su un altro telefono per assicurarvi che il backup funzioni.



**Distribuire le chiavi in modo intelligente**. Per i Tapsigner, consegnatele in una busta sigillata con il PIN comunicato separatamente (ad esempio, nella lettera di istruzioni per il recupero conservata altrove). Per i portafogli hardware classici, tenere il dispositivo presso una terza parte fidata e il seed su carta o metallo presso di sé o un'altra terza parte. Annotare l'impronta digitale di ogni chiave e il suo nome nel file di configurazione per evitare confusione.



**Pianificare prove periodiche** (esercitazioni antincendio). Verificare annualmente la possibilità di ricostruire la cassaforte dai backup su un telefono vuoto. Testare gli avvisi Canary controllando i saldi. Simulare scenari di perdita ("cosa succede se perdo la Coldcard?") per confermare che le combinazioni di chiavi rimanenti sono sufficienti.



**Non dimenticate l'aggiornamento**. Se avete impostato la vostra chiave di eredità su 1 anno, aggiornatela ogni 9-10 mesi. Questo è il prezzo da pagare per una trasmissione automatica senza l'intervento di terzi.



**Mantenere il piano aggiornato**. Qualsiasi modifica (sostituzione di una chiave, modifica degli eredi, modifica della scadenza) deve riflettersi in tutti i backup e i documenti. Rigenerare i PDF dopo ogni modifica e ridistribuire le nuove versioni.



## Limiti e considerazioni



Nonostante la potenza di questi strumenti, è importante riconoscerne i limiti per poterli gestire nel modo più efficace possibile.



La **complessità** di una cassaforte multisig con orologi a tempo può essere di per sé un rischio: configurazione errata, incomprensione da parte degli eredi, perdita di un elemento critico tra i tanti componenti. Bitcoin Keeper semplifica il più possibile l'esperienza, ma rimane un'operazione tecnica. Questo piano va utilizzato solo se l'importo da proteggere lo giustifica. Per importi ridotti, può essere sufficiente un piano più semplice.



Vale la pena di riflettere sulla **dipendenza dalle applicazioni**. Sebbene il codice sia open source e basato su standard aperti (Miniscript, BSMS), alcune funzionalità dipendono dall'ecosistema Keeper. Conservate una copia dell'applicazione (Android APK o iOS IPA) e documentate nelle lettere agli eredi la possibilità di utilizzare altri portafogli compatibili con Miniscript (come Liana) per recuperare i fondi.



Gli intermediari di fiducia** introducono un rischio umano. Cosa succede se un parente malintenzionato utilizza la chiave affidatagli prima della scadenza? O se l'avvocato smarrisce i vostri documenti? Scegliete con cura queste persone, spiegate chiaramente le loro responsabilità e prevedete un piano B. I portafogli Canary, i backup ridondanti e la struttura stessa del multisig rimangono la migliore protezione contro questi rischi.



## Conclusione



Bitcoin Keeper, con il suo piano Diamond Hands, offre una cassetta degli attrezzi completa per la pianificazione successoria: Enhanced Vault con chiavi temporizzate, documenti di accompagnamento, portafogli Canary e assistenza personalizzata.



Non è solo una questione tecnica: si tratta di progettare l'architettura dell'eredità, distribuire in modo intelligente chiavi e conoscenze e testare regolarmente il sistema. Un piano di eredità Bitcoin ben progettato trasforma i vostri satoshi in un'eredità reale e trasferibile.
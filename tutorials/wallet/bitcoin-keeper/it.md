---
name: Bitcoin Keeper
description: Bitcoin mobile wallet per la sicurezza e multi-sig
---

![cover](assets/cover.webp)



La gestione sicura dei bitcoin rappresenta una sfida importante per qualsiasi titolare consapevole della posta in gioco nella sovranità finanziaria. Tra la semplicità di un wallet mobile e la solidità di una soluzione multi-sig, il divario tecnico può sembrare scoraggiante per molti utenti. Il Bitcoin Keeper si posiziona esattamente a questo punto di intersezione, offrendo un approccio progressivo alla sicurezza che accompagna gli utenti nella loro evoluzione.



Bitcoin Keeper è un'applicazione mobile open source, dedicata esclusivamente a Bitcoin, sviluppata dal team di BitHyve. La sua ambizione è quella di rendere accessibile la gestione avanzata del portafoglio, in particolare le configurazioni multi-firma, mantenendo un'interfaccia intuitiva per i principianti. L'applicazione adotta lo slogan "Secure today, Plan for tomorrow", che riflette la sua filosofia di supporto a lungo termine.



A differenza dei portafogli generalisti che gestiscono più criptovalute, Bitcoin Keeper si concentra esclusivamente su Bitcoin. Questo approccio riduce la superficie di attacco potenziale e semplifica notevolmente l'esperienza dell'utente. Questo approccio basato esclusivamente sui bitcoin riduce la superficie di attacco potenziale e semplifica notevolmente l'esperienza dell'utente. L'applicazione si distingue anche per l'integrazione nativa dei portafogli hardware più diffusi e per le sue funzionalità avanzate di gestione del UTXO.



## Che cos'è il Bitcoin Keeper?



### Filosofia e obiettivi



Bitcoin Keeper è stato progettato per soddisfare le esigenze specifiche dei bitcoiners che desiderano mantenere il pieno controllo delle proprie chiavi private. Il progetto abbraccia pienamente i principi fondamentali di Bitcoin: codice sorgente aperto e verificabile, rispetto della privacy e sovranità dell'utente. Non è richiesta alcuna registrazione o informazione personale per utilizzare l'applicazione, che può essere eseguita anche offline per le operazioni di firma.



L'obiettivo centrale è quello di offrire uno strumento flessibile e a prova di futuro per conservare BTC per diversi anni e persino per diverse generazioni, grazie a funzionalità ereditarie. L'applicazione consente agli utenti di iniziare semplicemente con un wallet mobile, per poi evolvere gradualmente verso soluzioni più sicure a firma multipla.



### Architettura dell'applicazione



Il Bitcoin Keeper organizza la gestione dei fondi attorno a due concetti distinti. Il **Hot Wallet** è un semplice wallet a chiave singola, memorizzato sul telefono, progettato per le spese quotidiane e per importi modesti. I Vault** sono casseforti a firma multipla (Multi-Key) che richiedono più chiavi per autorizzare una spesa, progettate per la conservazione sicura a lungo termine.



### Caratteristiche principali



Bitcoin Keeper supporta quasi tutti i portafogli hardware presenti sul mercato: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport e Tapsigner di Coinkite. L'integrazione avviene con metodi diversi a seconda del dispositivo: Scansione del codice QR, connessione NFC o importazione di file.



L'applicazione offre anche una gestione avanzata del UTXO con l'etichettatura delle transazioni, il controllo delle monete per selezionare manualmente gli input durante l'invio e il supporto del formato PSBT per le transazioni parzialmente firmate.



## Installazione e configurazione iniziale



Bitcoin Keeper è disponibile gratuitamente su Android tramite Google Play Store e su iOS tramite App Store. L'editore indicato è BitHyve. Prima dell'installazione, assicuratevi che il vostro dispositivo sia privo di malware, aggiornato e non sia rootato o jailbroken.



Al primo avvio, l'applicazione chiede di creare un codice PIN di sicurezza. Questo codice protegge l'accesso al wallet e cripta i dati sensibili in locale. Scegliere un codice forte e memorizzarlo. È quindi possibile attivare l'autenticazione biometrica (impronta digitale o Face ID) per uno sblocco più rapido.



![Installation et configuration du PIN](assets/fr/01.webp)



L'applicazione presenta quindi diverse schermate introduttive che spiegano i suoi tre pilastri: Creazione di wallet per inviare e ricevere bitcoin, gestione delle chiavi con compatibilità hardware wallet e pianificazione legacy per trasmettere bitcoin. Premere "Get Started", quindi scegliere "Start New" per creare una nuova configurazione.



![Écrans d'introduction](assets/fr/02.webp)



## Scoprire l'interfaccia



L'interfaccia di Bitcoin Keeper è organizzata in quattro schede principali accessibili dalla barra di navigazione inferiore:



![Les quatre onglets de l'application](assets/fr/03.webp)



La scheda **Portafogli** visualizza i portafogli e i loro saldi. È qui che si accede ai portafogli per inviare e ricevere bitcoin. I tag "Hot Wallet" e "Single-Key" o "Multi-Key" consentono di identificare rapidamente il tipo di ciascun wallet.



La scheda **Keys** centralizza la gestione delle chiavi di firma. Qui si trovano la chiave mobile generata dall'applicazione e tutte le chiavi importate dai portafogli hardware. Qui è anche possibile aggiungere nuovi dispositivi di firma.



La scheda **Concierge** offre servizi di assistenza: è possibile inviare domande al team di assistenza e connettersi con i consulenti Bitcoin per un'assistenza personalizzata.



La scheda **More** (Altre opzioni) consente di accedere a impostazioni quali la connessione al server personale, il backup delle chiavi, l'ereditarietà dei documenti, le preferenze di visualizzazione e la gestione del wallet.



## Connessione al proprio server



Per rafforzare la riservatezza, Bitcoin Keeper consente di collegare l'applicazione al proprio server Electrum, anziché utilizzare i server pubblici predefiniti.



![Configuration du serveur Electrum](assets/fr/04.webp)



Dalla scheda Altro, scorrere verso il basso per trovare le impostazioni del server. Premere "Aggiungi server" per configurare una nuova connessione. È possibile scegliere tra "Server pubblico" (server pubblici preconfigurati) e "Electrum privato" (il proprio server).



Per un server privato, inserire l'URL (ad esempio umbrel.local per un nodo Umbrel) e il numero di porta (di solito 50001). Attivare SSL se il server lo supporta. È anche possibile scansionare un codice QR di configurazione. Una volta inseriti i parametri, premere "Connetti al server".



Se non avete ancora il vostro nodo Bitcoin, date un'occhiata al nostro tutorial sul Umbrel, un modo semplice e conveniente per realizzare il vostro nodo:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Ricevere bitcoin



Dalla scheda Portafogli, selezionare il wallet da cui si desidera ricevere fondi premendolo. La schermata del wallet visualizza il saldo e tre pulsanti di azione: Invia Bitcoin, Ricevi Bitcoin e Visualizza tutte le monete.



![Réception de bitcoins](assets/fr/05.webp)



Premere "Ricezione Bitcoin". Il Bitcoin Keeper genera un nuovo indirizzo di ricezione in formato Bech32 (che inizia con bc1...), insieme al suo codice QR. È possibile aggiungere un'etichetta a questo indirizzo per identificare la fonte dei fondi. Condividere l'indirizzo con il mittente visualizzando il codice QR o copiando l'indirizzo di testo.



L'applicazione genera automaticamente un nuovo indirizzo per ogni ricezione, preservando la vostra privacy. Se necessario, utilizzare "Ottieni nuovo Address" per ottenere un indirizzo vuoto.



## Gestione UTXO



Il Bitcoin Keeper offre una visibilità completa delle UTXO (uscite di transazione non spese) che compongono il saldo. Da una schermata wallet, premere "Visualizza tutte le monete" per accedere al gestore degli angoli.



![Gestion des UTXO](assets/fr/06.webp)



La schermata "Gestisci monete" elenca ogni UTXO individualmente con il suo importo e la sua etichetta. Questa schermata consente di risalire all'origine delle monete e di organizzarle. Tramite "Seleziona per inviare" è possibile selezionare UTXO specifici da inviare con il controllo delle monete, evitando così di mescolare monete di origine diversa.



## Inviare bitcoin



Per inviare, selezionare il portafoglio di origine e premere "Invia Bitcoin". Inserire l'indirizzo di destinazione (incollato o scansionato tramite codice QR) e aggiungere facoltativamente un'etichetta per identificare il destinatario.



![Envoi de bitcoins](assets/fr/07.webp)



La schermata successiva consente di inserire l'importo da inviare. L'interfaccia visualizza il saldo disponibile e la conversione in valuta fiat. Selezionare la priorità di addebito: Bassa (economica, ~60 minuti), Media o Alta (prioritaria). Le spese stimate in sats/vbyte sono visualizzate in tempo reale. Premere "Invia" per continuare.



![Confirmation et envoi](assets/fr/08.webp)



Una schermata di riepilogo visualizza tutti i dettagli: wallet origine, indirizzo di destinazione, priorità della transazione, costi di rete, importo inviato e totale. Controllare attentamente queste informazioni, poiché le transazioni Bitcoin sono irreversibili. Premere "Conferma e invia" per inviare la transazione.



Viene visualizzata una conferma di "Invio riuscito" con il riepilogo completo. La transazione è visibile nella cronologia "Transazioni recenti" con la sua etichetta.



## Salvare le chiavi



Il backup della chiave di ripristino è un passo fondamentale. Dalla scheda Altro, andare alla sezione "Backup e ripristino" e fare clic su "Chiave di ripristino".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



La schermata visualizza lo stato dei backup. Per verificare il backup, l'applicazione chiede di confermare una parola specifica della frase (ad esempio, la settima parola). Questa verifica assicura che la frase di ripristino sia stata scritta correttamente.



Da "Impostazioni della chiave di recupero", è possibile visualizzare la frase completa tramite "Visualizza chiave di recupero" e vedere l'impronta digitale del firmatario della chiave. Conservare la frase di 12 parole su carta, in un luogo sicuro, lontano da umidità e fuoco. Non conservarla mai su un dispositivo collegato.



## Aggiungere una chiave esterna (hardware wallet)



Uno dei punti di forza del Bitcoin Keeper è l'integrazione dei portafogli hardware. Dalla scheda Chiavi, premere "Aggiungi chiave" per aggiungere un nuovo dispositivo di firma.



![Ajout d'une clé hardware](assets/fr/10.webp)



Selezionare "Aggiungi chiave da un hardware" per collegare un wallet hardware. L'applicazione supporta un'ampia gamma di dispositivi: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner e Specter Solutions.



### Configurazione Tapsigner



La Tapsigner è una scheda NFC di Coinkite particolarmente adatta all'uso mobile. Se volete saperne di più, abbiamo un tutorial dedicato:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Per aggiungere il Tapsigner, selezionarlo dall'elenco dei portafogli hardware.



![Configuration du Tapsigner](assets/fr/11.webp)



Immettere innanzitutto il codice PIN di 6-32 cifre stampato sul retro della scheda (predefinito sulle nuove schede), oppure il proprio PIN se già configurato. Premere "Procedi", quindi avvicinare il Tapsigner al retro del telefono quando viene visualizzato "Pronto per la scansione". La comunicazione NFC importa automaticamente la chiave pubblica. È possibile aggiungere una descrizione (ad esempio "Métro Card") per identificare la chiave.



## Creare un portafoglio multisig



Una volta impostate le chiavi, è possibile creare un wallet a firma multipla che combina diversi dispositivi. Dalla scheda Portafogli, fare clic su "Aggiungi Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Sono disponibili tre opzioni: "Crea Wallet" per un nuovo portafoglio, "Importa Wallet" per ripristinare un wallet esistente o "Wallet collaborativo" per un vault condiviso. Selezionare "Crea Wallet" e poi "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



La schermata successiva offre diverse configurazioni: "Tasto singolo", "2 di 3 tasti multipli" o "3 di 5 tasti multipli". Per un multi-sig personalizzato, premere "Seleziona configurazione personalizzata". Ad esempio, scegliere "1 di 2": è richiesta una sola firma da due possibili chiavi.



Selezionare quindi le chiavi che comporranno il Vault. Nel nostro esempio, combiniamo la "Mobile Key" (chiave software del telefono) con la "TAPSIGNER" (Metro Card). Questa configurazione offre ridondanza: se una delle chiavi diventa inaccessibile, è sempre possibile spendere i fondi con l'altra.



![Finalisation du wallet multisig](assets/fr/14.webp)



Assegnare un nome al wallet (ad esempio "Test PlanB"), aggiungere una descrizione opzionale e selezionare i tasti selezionati. Premere "Crea il tuo Wallet". Viene visualizzato il messaggio di conferma "Wallet creato con successo", che ricorda di salvare il file di ripristino del wallet.



Il nuovo wallet multisig appare ora nella scheda Portafogli con l'etichetta "Multi-key" e l'indicazione "1 di 2".



### Salvare il file di configurazione



**A differenza di un wallet semplice, dove la frase di recupero è sufficiente per ripristinare l'accesso, un wallet multisig richiede anche il file di configurazione che descrive la struttura della cassaforte (quali chiavi partecipano, quante firme sono necessarie). Senza questo file, anche con tutte le frasi di recupero, non sarà possibile ricostruire il wallet.



![Export du fichier de configuration](assets/fr/15.webp)



Per esportare questo file, selezionare il multisig wallet nella scheda Portafogli, quindi premere l'icona Impostazioni (ingranaggio) nell'angolo in alto a destra. In "Impostazioni Wallet", fare clic su "File di configurazione Wallet". Sono disponibili diverse opzioni di esportazione:





- Esportazione PDF**: genera un documento PDF contenente tutte le informazioni di wallet
- Mostra QR**: visualizza un codice QR scansionabile per importare la configurazione in un altro dispositivo
- Airdrop / Esportazione file**: esporta il file tramite le opzioni di condivisione del telefono
- NFC**: condivisione tramite NFC con un dispositivo compatibile



Conservare questo file di configurazione separatamente dalle frasi di recupero, possibilmente su un supporto crittografato o stampato. In caso di smarrimento del telefono, questo file, unito alle frasi di recupero per ciascuna chiave partecipante, consentirà di ricostruire il multisig wallet su Bitcoin Keeper o su qualsiasi altro software compatibile.



## Le migliori pratiche



### Organizzazione del fondo



Strutturate i vostri bitcoin in base al loro utilizzo: un wallet Single-Key caldo per le spese correnti con importi limitati, e uno o più Vault Multi-Key per i risparmi a lungo termine. L'etichettatura sistematica UTXO vi aiuterà a tenere traccia della provenienza dei vostri fondi, particolarmente utile per gestire la riservatezza ed evitare di mescolare monete di origine diversa.



Mantenete il vostro telefono al sicuro: attivate il blocco biometrico, eseguite regolarmente gli aggiornamenti del sistema e rimanete vigili sulle applicazioni installate. E mantenete Bitcoin Keeper aggiornato con le patch di sicurezza.



### Sicurezza del backup



Conservate almeno due copie di ogni frase di recupero su carta, conservate in luoghi geograficamente separati. Per importi elevati, prendete in considerazione un metallo inciso e resistente ai disastri. Non conservate mai queste frasi su un dispositivo connesso a Internet e non fotografatele mai.



Per i vault multi-sig, salvare anche il file di configurazione (Wallet Recovery File), che contiene le chiavi pubbliche partecipanti e la struttura del vault. Questo file, combinato con le frasi di recupero delle chiavi, consente di ricostruire il wallet su qualsiasi software compatibile, come Sparrow o Specter.



## Vantaggi e limiti



### Punti salienti





- L'applicazione solo Bitcoin riduce la complessità e il rischio
- Integrazione nativa dei Vault multisig con guida passo-passo
- Supporto hardware esteso wallet (Tapsigner, Coldcard, Ledger, Jade, ecc.)
- Gestione avanzata di UTXO e controllo delle monete
- Può essere collegato a un server personale Electrum
- Codice sorgente aperto e verificabile



### Vincoli da considerare





- Interface principalmente in inglese
- Alcune funzioni premium (Cloud Backup, Assisted Server) richiedono un aggiornamento
- La configurazione del Multisig richiede una formazione iniziale



## Conclusione



Bitcoin Keeper si distingue come soluzione scalabile per la gestione dei bitcoin. Il suo approccio progressivo, dal semplice wallet a caldo ai Vault multi-firma, significa che la sicurezza può essere aggiornata in base alle esigenze. La possibilità di integrare facilmente portafogli hardware come il Tapsigner apre la strada a configurazioni robuste senza eccessiva complessità.



L'orientamento ai soli bitcoin, il codice open source e il rispetto della privacy ne fanno una scelta in linea con i valori fondamentali dell'ecosistema Bitcoin.



Questo tutorial copre le caratteristiche essenziali di Bitcoin Keeper nella sua versione gratuita. L'applicazione offre anche funzioni premium (Cloud Backup, Assisted Server Backup, Canary Wallets) che saranno oggetto di un tutorial dedicato. In una prossima guida esploreremo anche la funzione di pianificazione dell'eredità, che consente di preparare la trasmissione dei bitcoin ai propri cari, grazie agli Enhanced Vault e ai documenti di accompagnamento integrati nell'applicazione.



## Risorse





- Sito web ufficiale: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Centro assistenza: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Codice sorgente: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)
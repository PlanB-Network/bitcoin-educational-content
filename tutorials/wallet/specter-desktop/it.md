---
name: Specter Desktop
description: Gestite i vostri portafogli Bitcoin multi-firma in totale sovranità con il vostro nodo personale
---

![cover](assets/cover.webp)



Specter Desktop è un'applicazione open source (licenza MIT) sviluppata da Cryptoadvance dal 2019 che facilita la gestione dei portafogli Bitcoin con i vostri portafogli hardware (Ledger, Trezor, Coldcard, BitBox02, Passport, ecc.) e la vostra infrastruttura Bitcoin (nodo Bitcoin Core o server Electrum). L'applicazione eccelle in particolare nelle configurazioni multi-firma, consentendo di proteggere grandi somme distribuendo il potere di firma tra diversi portafogli hardware indipendenti.



**In questa esercitazione, imparerete a:**




- Installare e configurare Specter Desktop sul computer (Windows, macOS o Linux)
- Collegare Specter a un server Electrum (in questo esempio utilizzeremo Umbrel)
- Creare un semplice wallet con hardware wallet (Coldcard)
- Ricevere e inviare bitcoin in totale sovranità
- Impostazione di un wallet multi-firma 2 contro 3 con diversi portafogli hardware
- Installare Specter su un server Umbrel (bonus avanzato)



Tutte le vostre transazioni saranno convalidate localmente attraverso la vostra infrastruttura, senza trasmettere alcuna informazione a server esterni, garantendo la vostra riservatezza e sovranità finanziaria. Controllate sempre le transazioni sullo schermo del vostro hardware wallet prima di firmare.



## Download e installazione



Visitate il sito ufficiale di Specter Desktop per scaricare l'applicazione.



![Page d'accueil Specter](assets/fr/01.webp)



Nella pagina di download, scegliere la versione corrispondente al proprio sistema operativo: macOS, Windows o Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Una volta scaricata, installate l'applicazione seguendo le istruzioni abituali del vostro sistema operativo. Per macOS, trascinare l'icona in Applicazioni. Per Windows, eseguire il programma di installazione. Per Linux, seguire le istruzioni del pacchetto.



## Configurazione iniziale



Al primo avvio, Specter Desktop chiede di scegliere il tipo di connessione. È possibile collegarsi a un server Electrum o al proprio nodo Bitcoin Core.



![Choix du type de connexion](assets/fr/03.webp)



In questo esempio, utilizzeremo una connessione a un server Electrum in esecuzione su Umbrel.



Per ulteriori informazioni, consultate il nostro tutorial su Umbrel:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Questa opzione offre una sincronizzazione più rapida rispetto a Bitcoin Core. Se si preferisce, è possibile selezionare "Bitcoin Core" e configurare la connessione al nodo locale. I passaggi seguenti rimangono invariati, indipendentemente dalla scelta effettuata.



Selezionare "Connessione Electrum", quindi scegliere "Inserisci il mio" per configurare il proprio server Electrum.



![Configuration Electrum](assets/fr/04.webp)



Inserire l'indirizzo del server Electrum. Nel nostro caso con Umbrel, l'indirizzo sarà `umbrel.local` con la porta `50001`. Fare clic su "Connetti" per stabilire la connessione.



Una volta collegati, viene visualizzata la schermata di benvenuto, con una lista di controllo per iniziare. Ora è necessario aggiungere i portafogli hardware.



![Écran d'accueil](assets/fr/05.webp)



## Aggiunta dell'hardware wallet



Nel menu di sinistra, fare clic su "Aggiungi dispositivo" per aggiungere l'hardware wallet.



Specter Desktop supporta numerosi portafogli hardware: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault e molti altri.



Se volete saperne di più, date un'occhiata alle nostre esercitazioni su wallet hardware.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Selezionare l'hardware del wallet. In questo esempio, utilizziamo una Coldcard MK4.



Di seguito troverete il nostro tutorial per questa ferramenta wallet:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Per una Coldcard, è necessario esportare le chiavi pubbliche dall'hardware wallet tramite una connessione USB o una scheda microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Seguire le istruzioni visualizzate per esportare le chiavi dalla Coldcard. Assegnare un nome all'hardware wallet (qui "MK4 Tuto"). Una volta importate le chiavi, è possibile creare un wallet con una sola chiave o aggiungere altri portafogli hardware per un wallet multi-firma.



![Dispositif ajouté](assets/fr/08.webp)



## Creazione del portafoglio



Dopo aver aggiunto l'hardware wallet, fare clic su "Crea chiave singola wallet" per creare un wallet a firma singola.



Date un nome al vostro portafoglio (ad esempio "Wallet for tuto") e selezionate il tipo di indirizzo. Selezionare "Segwit" per utilizzare indirizzi nativi bech32 che ottimizzano i costi di transazione.



![Configuration du portefeuille](assets/fr/09.webp)



Una volta creato il portafoglio, Specter offre la possibilità di salvare un file PDF di backup contenente tutte le informazioni pubbliche necessarie per ripristinare il portafoglio (descrittori, chiavi pubbliche estese). Questo file non contiene le chiavi private.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Ricevere bitcoin



Per ricevere bitcoin, selezionare il proprio wallet nel menu di sinistra, quindi fare clic sulla scheda "Ricevi".



Specter genera automaticamente un nuovo indirizzo di ricezione con un codice QR.



![Génération d'une adresse de réception](assets/fr/11.webp)



È possibile copiare l'indirizzo o scansionare il codice QR. Controllare sempre l'indirizzo sullo schermo dell'hardware del wallet prima di comunicarlo a qualcuno.



## Visualizza la cronologia e gli indirizzi



Una volta ricevuti i bitcoin, è possibile visualizzare le transazioni nella scheda "Transazioni".



![Historique des transactions](assets/fr/12.webp)



La scheda "Indirizzi" consente di visualizzare tutti gli indirizzi generati dal portafoglio, con il relativo stato di utilizzo e gli importi associati.



![Liste des adresses](assets/fr/13.webp)



## Inviare bitcoin



Per inviare bitcoin, fare clic sulla scheda "Invia". Inserire l'indirizzo del destinatario, l'importo da inviare e selezionare le opzioni avanzate se si desidera selezionare manualmente gli UTXO (controllo delle monete).



![Création d'une transaction](assets/fr/14.webp)



Fare clic su "Crea transazione non firmata" per creare la transazione. Specter chiederà quindi di firmare la transazione con l'hardware wallet.



![Signature de la transaction](assets/fr/15.webp)



Se si utilizza una Coldcard, si potrà scegliere se firmare via USB o utilizzare la scheda microSD (air-gapped). Confermate la transazione sullo schermo del vostro hardware wallet, controllando attentamente l'indirizzo di destinazione e l'importo.



Una volta che la transazione è stata firmata, è possibile trasmetterla sulla rete Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Fare clic su "Invia transazione" per inviare la transazione. Specter confermerà l'invio della transazione e sarà possibile seguirne lo stato nella scheda Transazioni.



![Diffusion de la transaction](assets/fr/17.webp)



## Creazione e utilizzo di un portafoglio a più firme



Uno dei punti di forza di Specter Desktop è la sua capacità di semplificare la gestione dei portafogli multi-firma. Un wallet multisigma richiede diverse firme per autorizzare una transazione, eliminando così il singolo punto di fallimento. Una configurazione 2 contro 3, ad esempio, richiede due firme da tre portafogli hardware separati per convalidare qualsiasi spesa.



Per creare un wallet multisig, iniziare ad aggiungere tutti i portafogli hardware di firma tramite "Aggiungi dispositivo". In questo esempio, utilizzeremo tre diversi portafogli hardware: una Coldcard MK4 (già aggiunta in precedenza), un Passport e un Ledger. Questa diversificazione dei produttori rafforza la sicurezza evitando la dipendenza da un'unica catena di fornitura o da un unico firmware.



Ecco i link alle esercitazioni di Ledger e Passport:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Aggiungere il Passport assegnando un nome all'hardware wallet (ad es. "Passport multi") e importando le chiavi tramite scheda microSD o codice QR. Quindi fare clic su "Continua" per proseguire.



![Ajout du Passport](assets/fr/23.webp)



Quindi aggiungere il Ledger collegandolo via USB e aprendo l'applicazione Bitcoin sull'hardware wallet. Dategli un nome (ad esempio "ledger multi") e fate clic su "Get via USB" e poi su "Continue" per importare le chiavi pubbliche.



![Ajout du Ledger](assets/fr/24.webp)



Una volta registrati i tre portafogli hardware in Specter, fare clic su "Aggiungi wallet" e selezionare l'opzione "Firma multipla" per creare un wallet a firma multipla.



![Choix du type de wallet](assets/fr/25.webp)



Selezionare i tre portafogli hardware che si desidera includere nel quorum di firma multipla: MK4 Tuto, Passport multi e Ledger multi. Fare clic su "Continua" per passare alla fase successiva.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Scegliere la configurazione multi-firma. Selezionate "Segwit" come tipo di indirizzo per beneficiare di commissioni ottimizzate. Il parametro "Firme richieste per autorizzare le transazioni (m di 3)" consente di definire la soglia: per una configurazione 2 su 3, sono necessarie 2 firme. Ogni hardware wallet visualizza la chiave multisig corrispondente. Fare clic su "Crea wallet" per finalizzare la creazione.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Il vostro portfolio multi-firma "Multi tuto" è stato creato. Specter raccomanda immediatamente di salvare il file PDF di backup contenente il descrittore del portfolio. Fare clic su "Salva PDF di backup" per scaricare questo file fondamentale.



![Wallet multisig créé](assets/fr/28.webp)



Specter consente inoltre di esportare le informazioni wallet a ciascuno dei portafogli hardware tramite codice QR o file. Ciò consente ad alcuni portafogli hardware (come Coldcard o Passport) di memorizzare la configurazione multisig direttamente nella loro memoria.



Per Passport, sbloccare il dispositivo e andare su "Gestione account" > "Connetti Wallet" > "Specter" > "Multisig" > "Codice QR", quindi scansionare il codice QR generato da Specter. Il Passport chiederà quindi di scansionare un indirizzo di ricezione dal wallet per convalidare la configurazione multisig.



Per l'MK4, collegarlo al PC e sbloccarlo. Quindi fare clic su "Salva file MK4 Tuto" e salvare il file nell'MK4. La prossima volta che si firmerà l'hardware wallet, l'MK4 utilizzerà questo file per completare la configurazione del multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Per vostra informazione, potete accedere ai backup in qualsiasi momento dalla scheda "Impostazioni" del vostro portafoglio, quindi "Esportazione":



![Accès au backup PDF](assets/fr/30.webp)



L'uso quotidiano rimane simile a quello di un semplice wallet: gli indirizzi di ricezione del generate sono normali. Per inviare bitcoin, accedere alla scheda "Invia", inserire l'indirizzo del destinatario e l'importo, quindi fare clic su "Crea transazione non firmata".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter crea un PSBT (Partially Signed Bitcoin Transaction) e visualizza "Acquisito 0 di 2 firme". Ora è necessario firmare con almeno due dei tre portafogli hardware. Cliccare sul primo hardware wallet (ad esempio "MK4 Tuto") per firmare con la Coldcard, quindi sul secondo (ad esempio "Passport multi") per ottenere la seconda firma richiesta.



![Signature de la transaction](assets/fr/32.webp)



Una volta ottenute le 2 firme richieste (l'interfaccia visualizza "Acquisito 2 di 2 firme" e "La transazione è pronta per l'invio"), cliccare su "Invia transazione" per trasmettere la transazione sulla rete Bitcoin.



![Transaction prête à être diffusée](assets/fr/33.webp)



Questo approccio a più firme è particolarmente adatto alle aziende (più manager devono approvare le spese), alle famiglie (protezione di un'eredità multigenerazionale) o ai singoli individui che gestiscono somme ingenti (distribuzione geografica dei portafogli hardware per far fronte a disastri localizzati).



### L'importanza fondamentale dei backup multi-firma



**Nota bene**: il backup di un portafoglio multisigma è fondamentalmente diverso dal backup di un portafoglio singolo. Le frasi di ripristino (frasi seed) da sole non sono sufficienti per ripristinare un portafoglio multisig. È necessario eseguire il backup anche del **output descriptor** (output descriptor), che contiene le informazioni di configurazione del portafoglio multisig.



Il output descriptor include dati essenziali: le chiavi pubbliche estese (xpub) di ciascun cofirmatario, la soglia di firma (2 su 3 nel nostro esempio), il tipo di script utilizzato (Segwit nativo, nidificato o legacy) e i percorsi di bypass per ciascun hardware wallet. Senza questo descrittore, anche se avete due delle tre frasi di recupero, non sarete in grado di ricostruire il vostro wallet o di accedere ai vostri bitcoin. Il descrittore consente al software di sapere come combinare le chiavi pubbliche per generate gli indirizzi Bitcoin corrispondenti ai fondi.



Specter Desktop genera automaticamente un file PDF di backup quando si crea il portafoglio multisig. Questo PDF contiene il descrittore completo, le impronte digitali di ogni hardware wallet e tutte le informazioni pubbliche necessarie per il ripristino. **Questo file non contiene le chiavi private** e quindi non consente di per sé di spendere i bitcoin, ma permette a chiunque vi acceda di vedere la cronologia completa delle transazioni e il saldo.



Per eseguire correttamente il backup della configurazione multi-firma, seguire questa procedura: dopo aver creato il portafoglio, fare clic sulla scheda "Impostazioni", quindi su "Esporta" e selezionare "Salva PDF di backup". Creare diverse copie di questo PDF: stamparne almeno due su carta e conservarne una copia digitale crittografata. Conservate una copia del PDF con ciascuna delle vostre frasi di recupero, in luoghi geograficamente separati.



Incidete le vostre frasi di recupero su piastre metalliche ignifughe e impermeabili per garantirne la longevità. Non sottovalutate mai l'importanza di questi backup: se perdete la cartella `~/.specter` sul vostro computer E perdete uno dei vostri portafogli hardware senza un backup dei descrittori, tutti i vostri fondi saranno irrimediabilmente persi, anche con una configurazione 2 contro 3. La ridondanza multi-firma protegge dalla perdita dell'hardware del wallet, ma solo se è stato eseguito correttamente il backup del descrittore del wallet.



## Vantaggi e limiti di Specter Desktop



**Vantaggi**: Riservatezza ottimale grazie alla convalida locale completa senza server di terze parti. Flessibilità multi-firma per configurazioni avanzate (aziendali, familiari, individuali). Ampio supporto hardware wallet con piena interoperabilità (USB e air-gapped).



**Limitazioni**: Curva di apprendimento significativa sui concetti avanzati del Bitcoin (UTXO, descrittori, percorsi di derivazione).



## Le migliori pratiche



Controllare sempre gli indirizzi e gli importi sulla schermata wallet dell'hardware prima della convalida, per proteggersi dal malware.



Conservate i backup dei PDF separatamente dai vostri semi. Questi descrittori pubblici possono essere archiviati in un caveau bancario o in un cloud crittografato, facilitando il recupero senza esporre le chiavi private.



Testate il recupero su importi token prima di utilizzare i portafogli con fondi di grandi dimensioni. Creare, testare, cancellare e ripristinare per convalidare le procedure.



Mantenete Specter e il vostro firmware aggiornati. Distribuite i vostri cofirmatari multi-firma geograficamente (casa/ufficio/vicino) per far fronte a disastri localizzati. Utilizzate etichette descrittive per facilitare la contabilità e la dichiarazione dei redditi.



## Bonus: Installazione su un server Bitcoin (Umbrel, RaspiBlitz, Start9)



Se possedete già un server Bitcoin come Umbrel, RaspiBlitz, MyNode o Start9, potete installare Specter Desktop direttamente dal loro negozio di applicazioni. Questo approccio offre diversi vantaggi significativi: l'applicazione si configura automaticamente con il vostro nodo Bitcoin Core locale, rimane accessibile 24 ore su 24, 7 giorni su 7, tramite un'interfaccia web da qualsiasi dispositivo della vostra rete e potete persino accedervi in modo sicuro da remoto tramite Tor. L'intera infrastruttura Bitcoin è centralizzata su un unico server dedicato, semplificando la gestione e rafforzando la vostra sovranità.



### Installazione dall'App Store Umbrel



Dall'interfaccia di Umbrel, accedere all'App Store e cercare Specter Desktop. Fare clic su "Installa" per avviare l'installazione.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Una volta completata l'installazione, aprire Specter Desktop su Umbrel. La schermata di benvenuto chiederà di scegliere il tipo di connessione. Se si utilizza Specter su Umbrel, fare clic su "Aggiorna impostazioni" per configurare la connessione.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Selezionare "Connessione USB Specter remota" per abilitare l'uso di portafogli hardware USB collegati al computer locale mentre si utilizza Specter sul server Umbrel remoto.



![Configuration Remote Specter USB](assets/fr/20.webp)



Seguire le istruzioni visualizzate per configurare il ponte HWI. È necessario accedere alle impostazioni del bridge del dispositivo e aggiungere il dominio `http://umbrel.local:25441` alla whitelist. Fare clic su "Aggiorna" per salvare la configurazione.



![HWI Bridge Settings](assets/fr/21.webp)



Se si desidera utilizzare i portafogli hardware USB anche dal computer locale, scaricare l'applicazione Specter Desktop sul computer e impostarla su "Sì, eseguo Specter in remoto". Fare clic su "Salva" per finalizzare la configurazione.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Conclusione



Specter Desktop democratizza le configurazioni Bitcoin avanzate, rendendo accessibile la multi-firma senza sacrificare la sovranità o la riservatezza. Per gli utenti che gestiscono quantità significative di denaro, trasforma le pratiche istituzionali in soluzioni utilizzabili dai privati.



Sebbene l'applicazione richieda un investimento iniziale in infrastrutture e apprendimento, offre una sovranità completa: controllo dell'infrastruttura di convalida, proprietà fisica delle chiavi e transazioni libere dalla sorveglianza di terzi. Che si tratti di un privato che mette al sicuro i propri risparmi, di una famiglia che crea una cassetta di sicurezza multigenerazionale o di un'azienda che gestisce il flusso di cassa, Specter Desktop è lo strumento di riferimento per conciliare massima sicurezza e sovranità assoluta.



## Risorse



### Documentazione ufficiale




- [Sito ufficiale di Specter Desktop](https://specter.solutions/desktop/)
- [Codice sorgente GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Documentazione completa](https://docs.specter.solutions/)



### Comunità e supporto




- [Gruppo comunitario Telegram Specter](https://t.me/spectersupport)
- [Forum di discussione Reddit](https://reddit.com/r/specterdesktop/)
- [Segnalazioni di bug su GitHub](https://github.com/cryptoadvance/specter-desktop/issues)
---
name: Specter Desktop
description: Gestite i vostri portafogli Bitcoin multi-firma in totale sovranità con il vostro nodo personale
---

![cover](assets/cover.webp)



Specter Desktop è un'applicazione open source (licenza MIT) sviluppata da Cryptoadvance dal 2019 che facilita la gestione dei portafogli Bitcoin con i vostri portafogli hardware (Ledger, Trezor, Coldcard, BitBox02, Passport, ecc.) e la vostra infrastruttura Bitcoin (nodo Bitcoin core o Electrum Server). L'applicazione eccelle in particolare nelle configurazioni multi-firma, consentendo di proteggere grandi somme distribuendo il potere di firma tra diversi portafogli hardware indipendenti.



**In questa esercitazione, imparerete a:**




- Installare e configurare Specter Desktop sul computer (Windows, macOS o Linux)
- Collegare Specter a un Electrum Server (in questo esempio useremo Umbrel)
- Creazione di un semplice Wallet con un Hardware Wallet (Coldcard)
- Ricevere e inviare bitcoin in totale sovranità
- Impostazione di un Wallet multi-firma 2 contro 3 con diversi portafogli hardware
- Installare Specter su un server Umbrel (bonus avanzato)



Tutte le vostre transazioni saranno convalidate localmente attraverso la vostra infrastruttura, senza trasmettere alcuna informazione a server esterni, garantendo la vostra riservatezza e sovranità finanziaria. Controllate sempre le transazioni sullo schermo del vostro Hardware Wallet prima di firmare.



## Download e installazione



Visitate il sito ufficiale di Specter Desktop per scaricare l'applicazione.



![Page d'accueil Specter](assets/fr/01.webp)



Nella pagina di download, scegliere la versione corrispondente al proprio sistema operativo: macOS, Windows o Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Una volta scaricata, installate l'applicazione seguendo le istruzioni abituali del vostro sistema operativo. Per macOS, trascinare l'icona in Applicazioni. Per Windows, eseguire il programma di installazione. Per Linux, seguire le istruzioni del pacchetto.



## Configurazione iniziale



Al primo avvio, Specter Desktop chiede di scegliere il tipo di connessione. È possibile collegarsi a un nodo Electrum Server o al proprio nodo Bitcoin core.



![Choix du type de connexion](assets/fr/03.webp)



In questo esempio, utilizzeremo una connessione a un Electrum Server in esecuzione su Umbrel.



Per ulteriori informazioni, consultare il nostro tutorial su Umbrel:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Questa opzione offre una sincronizzazione più rapida rispetto a Bitcoin core. Se si preferisce, è possibile selezionare "Bitcoin core" e configurare la connessione al nodo locale. I passaggi seguenti rimangono invariati, indipendentemente dalla scelta effettuata.



Selezionare "Connessione Electrum", quindi scegliere "Immettere il proprio" per configurare il proprio Electrum Server.



![Configuration Electrum](assets/fr/04.webp)



Inserire il Address del Electrum Server. Nel nostro caso con Umbrel, il Address sarà `umbrel.local` con la porta `50001`. Fare clic su "Connetti" per stabilire la connessione.



Una volta collegati, viene visualizzata la schermata di benvenuto, con una lista di controllo per iniziare. Ora è necessario aggiungere i portafogli hardware.



![Écran d'accueil](assets/fr/05.webp)



## Aggiunta di un Hardware Wallet



Nel menu di sinistra, cliccare su "Aggiungi dispositivo" per aggiungere il Hardware Wallet.



Specter Desktop supporta numerosi portafogli hardware: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault e molti altri.



Se volete saperne di più, date un'occhiata alle nostre esercitazioni su Hardware Wallet.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Selezionare il Hardware Wallet. In questo esempio, utilizziamo una Coldcard MK4.



Qui di seguito trovate il nostro tutorial per questo Hardware Wallet :



https://planb.network/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Per una Coldcard, è necessario esportare le chiavi pubbliche dal Hardware Wallet tramite una connessione USB o una scheda microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Seguire le istruzioni visualizzate per esportare le chiavi dalla Coldcard. Assegnare un nome al Hardware Wallet (qui "MK4 Tuto"). Una volta importate le chiavi, è possibile creare un Wallet con una sola chiave o aggiungere altri portafogli hardware per un Wallet multi-firma.



![Dispositif ajouté](assets/fr/08.webp)



## Creazione del portafoglio



Dopo aver aggiunto il Hardware Wallet, fare clic su "Crea chiave singola Wallet" per creare un Wallet a firma singola.



Date un nome al vostro portafoglio (ad esempio "Wallet per tuto") e selezionate il tipo Address. Selezionare "SegWit" per utilizzare gli indirizzi nativi BECH32, che ottimizzano i costi di transazione.



![Configuration du portefeuille](assets/fr/09.webp)



Una volta creato il portafoglio, Specter offre la possibilità di salvare un file PDF di backup contenente tutte le informazioni pubbliche necessarie per ripristinare il portafoglio (descrittori, chiavi pubbliche estese). Questo file non contiene le chiavi private.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Ricevere bitcoin



Per ricevere bitcoin, selezionare il proprio Wallet nel menu di sinistra, quindi fare clic sulla scheda "Ricevi".



Specter genera automaticamente una nuova ricezione Address con un codice QR.



![Génération d'une adresse de réception](assets/fr/11.webp)



È possibile copiare il Address o scansionare il codice QR. Controllare sempre il Address sullo schermo del Hardware Wallet prima di passarlo a qualcuno.



## Visualizza la cronologia e gli indirizzi



Una volta ricevuti i bitcoin, è possibile visualizzare le transazioni nella scheda "Transazioni".



![Historique des transactions](assets/fr/12.webp)



La scheda "Indirizzi" consente di visualizzare tutti gli indirizzi generati dal portafoglio, con il relativo stato di utilizzo e gli importi associati.



![Liste des adresses](assets/fr/13.webp)



## Inviare bitcoin



Per inviare bitcoin, fare clic sulla scheda "Invia". Inserire il Address del destinatario, l'importo da inviare e selezionare le opzioni avanzate se si desidera selezionare manualmente gli UTXO (controllo Coin).



![Création d'une transaction](assets/fr/14.webp)



Fare clic su "Crea transazione non firmata" per creare la transazione. Specter vi chiederà quindi di firmare la transazione con il vostro Hardware Wallet.



![Signature de la transaction](assets/fr/15.webp)



Se si utilizza una Coldcard, si potrà scegliere se firmare via USB o utilizzare la scheda microSD (air-gapped). Confermate la transazione sullo schermo del Hardware Wallet, controllando attentamente la destinazione Address e l'importo.



Una volta che la transazione è stata firmata, è possibile trasmetterla sulla rete Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Fare clic su "Invia transazione" per inviare la transazione. Specter confermerà l'invio della transazione e sarà possibile seguirne lo stato nella scheda Transazioni.



![Diffusion de la transaction](assets/fr/17.webp)



## Creazione e utilizzo di un portafoglio a più firme



Uno dei punti di forza di Specter Desktop è la sua capacità di semplificare la gestione dei portafogli multi-firma. Un Multisig Wallet richiede più firme per autorizzare una transazione, eliminando il singolo punto di fallimento. Una configurazione 2 contro 3, ad esempio, richiede due firme da tre portafogli hardware separati per convalidare qualsiasi spesa.



Per creare un Multisig Wallet, iniziare aggiungendo tutti i portafogli hardware firmatari tramite "Aggiungi dispositivo". In questo esempio, utilizzeremo tre portafogli hardware diversi: una Coldcard MK4 (già aggiunta in precedenza), un Passport e un Ledger. Questa diversificazione dei produttori rafforza la sicurezza evitando la dipendenza da un'unica catena o firmware Supply.



Ecco i link alle esercitazioni di Ledger e Passport:



https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Aggiungere il Passport assegnando un nome al Hardware Wallet (ad es. "Passport multi") e importando le chiavi tramite scheda microSD o codice QR. Quindi fare clic su "Continua" per proseguire.



![Ajout du Passport](assets/fr/23.webp)



Aggiungere quindi il Ledger collegandolo via USB e aprendo l'applicazione Bitcoin sul Hardware Wallet. Assegnategli un nome (ad esempio "Ledger multi") e fate clic su "Ottieni via USB" e poi su "Continua" per importare le chiavi pubbliche.



![Ajout du Ledger](assets/fr/24.webp)



Una volta registrati i tre portafogli hardware in Specter, fare clic su "Aggiungi Wallet" e selezionare l'opzione "Firma multipla" per creare un Wallet a firma multipla.



![Choix du type de wallet](assets/fr/25.webp)



Selezionare i tre portafogli hardware che si desidera includere nel quorum di firma multipla: MK4 Tuto, Passport multi e Ledger multi. Fare clic su "Continua" per passare alla fase successiva.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Scegliete la configurazione multi-firma. Selezionate "SegWit" come tipo di Address per beneficiare di tariffe ottimizzate. Il parametro "Firme necessarie per autorizzare le transazioni (m di 3)" consente di definire la soglia: per una configurazione 2 su 3, sono necessarie 2 firme. Ogni Hardware Wallet visualizza la chiave Multisig corrispondente. Fare clic su "Crea Wallet" per finalizzare la creazione.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Il vostro portfolio multi-firma "Multi tuto" è ora creato. Specter consiglia immediatamente di salvare il file PDF di backup contenente il portfolio Descriptor. Fare clic su "Salva PDF di backup" per scaricare questo file fondamentale.



![Wallet multisig créé](assets/fr/28.webp)



Specter consente inoltre di esportare le informazioni del Wallet in ciascuno dei portafogli hardware tramite codice QR o file. Ciò consente ad alcuni portafogli hardware (come Coldcard o Passport) di memorizzare la configurazione del Multisig direttamente nella loro memoria.



Per il Passport, sbloccare il dispositivo e andare su "Gestione account" > "Connetti Wallet" > "Specter" > "Multisig" > "Codice QR", quindi scansionare il codice QR generato da Specter. Il Passport chiederà quindi di scansionare un Address ricevente dal proprio Wallet per convalidare la configurazione del Multisig.



Per l'MK4, collegarlo al PC e sbloccarlo. Quindi fare clic su "Save MK4 Tuto file" e salvare il file nell'MK4. La volta successiva che si firma il Hardware Wallet, l'MK4 utilizzerà questo file per completare la configurazione del Multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Per vostra informazione, potete accedere ai backup in qualsiasi momento dalla scheda "Impostazioni" del vostro portafoglio, quindi "Esportazione":



![Accès au backup PDF](assets/fr/30.webp)



L'uso quotidiano rimane simile a quello di un semplice Wallet: gli indirizzi di ricezione generate sono normali. Per inviare bitcoin, accedere alla scheda "Invia", inserire il Address del destinatario e l'importo, quindi fare clic su "Crea transazione non firmata".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter crea un PSBT (Partially Signed Bitcoin Transaction) e visualizza "Acquisito 0 di 2 firme". Ora è necessario firmare con almeno due dei tre portafogli hardware. Cliccare sul primo Hardware Wallet (ad esempio "MK4 Tuto") per firmare con la Coldcard, quindi sul secondo (ad esempio "Passport multi") per ottenere la seconda firma richiesta.



![Signature de la transaction](assets/fr/32.webp)



Una volta ottenute le 2 firme richieste (il Interface visualizza "Acquisito 2 di 2 firme" e "La transazione è pronta per l'invio"), fare clic su "Invia transazione" per trasmettere la transazione sulla rete Bitcoin.



![Transaction prête à être diffusée](assets/fr/33.webp)



Questo approccio a più firme è particolarmente adatto alle aziende (più manager devono approvare le spese), alle famiglie (protezione di un'eredità multigenerazionale) o ai singoli individui che gestiscono somme ingenti (distribuzione geografica dei portafogli hardware per far fronte a disastri localizzati).



### L'importanza fondamentale dei backup multi-firma



**Nota bene**: il backup di un portafoglio con più firme è fondamentalmente diverso dal backup di un portafoglio singolo. Le frasi di ripristino (frasi seed) da sole non sono sufficienti per ripristinare un portafoglio Multisig. È necessario eseguire il backup anche del **output descriptor** (output descriptor), che contiene le informazioni di configurazione del portafoglio a più firme.



Il output descriptor include dati essenziali: le chiavi pubbliche estese (xpub) di ogni cofirmatario, la soglia di firma (2 su 3 nel nostro esempio), il tipo di script utilizzato (SegWit nativo, annidato o legacy) e i percorsi di derivazione per ogni Hardware Wallet. Senza questo Descriptor, anche se avete due delle tre frasi di recupero, non sarete in grado di ricostruire il vostro Wallet o di accedere ai vostri bitcoin. Il Descriptor permette al vostro software di sapere come combinare le chiavi pubbliche per generate gli indirizzi Bitcoin corrispondenti ai vostri fondi.



Specter Desktop genera automaticamente un file PDF di backup quando si crea la cartella Multisig. Questo PDF contiene il Descriptor completo, le impronte digitali di ogni Hardware Wallet e tutte le informazioni pubbliche necessarie per il ripristino. **Questo file non contiene le chiavi private** e quindi non consente di per sé di spendere i bitcoin, ma permette a chiunque vi acceda di vedere la cronologia completa delle transazioni e il saldo.



Per eseguire correttamente il backup della configurazione multi-firma, seguire questa procedura: dopo aver creato il portafoglio, fare clic sulla scheda "Impostazioni", quindi su "Esporta" e selezionare "Salva PDF di backup". Creare diverse copie di questo PDF: stamparne almeno due su carta e conservarne una copia digitale crittografata. Conservate una copia del PDF con ciascuna delle vostre frasi di recupero, in luoghi geograficamente separati.



Masterizzate le frasi di recupero su piastre metalliche ignifughe e impermeabili per garantirne la longevità. Non sottovalutate mai l'importanza di questi backup: se perdete la cartella `~/.specter` del vostro computer E perdete uno dei vostri portafogli hardware senza un backup del Descriptor, tutti i vostri fondi saranno irrimediabilmente persi, anche con una configurazione 2 su 3. La ridondanza a più firme protegge dalla perdita di un Hardware Wallet, ma solo se si è eseguito correttamente il backup del Wallet del Descriptor.



## Vantaggi e limiti di Specter Desktop



**Vantaggi**: Riservatezza ottimale grazie alla convalida locale completa senza server di terze parti. Flessibilità multi-firma per configurazioni avanzate (aziendali, familiari, individuali). Ampio supporto Hardware Wallet con piena interoperabilità (USB e air-gapped).



**Limitazioni**: Curva di apprendimento significativa sui concetti avanzati di Bitcoin (UTXO, descrittori, percorsi di derivazione).



## Le migliori pratiche



Controllare sempre gli indirizzi e gli importi sulla schermata di Hardware Wallet prima della convalida, per proteggersi dal malware.



Conservate i backup dei PDF separatamente dai vostri semi. Questi descrittori pubblici possono essere archiviati in un caveau bancario o in un cloud crittografato, facilitando il recupero senza esporre le chiavi private.



Testate il recupero su importi token prima di utilizzare i portafogli con fondi di grandi dimensioni. Create, testate, cancellate e ripristinate per convalidare le vostre procedure.



Mantenete Specter e il vostro firmware aggiornati. Distribuite i vostri cofirmatari multi-firma geograficamente (casa/ufficio/vicino) per far fronte a disastri localizzati. Utilizzate etichette descrittive per facilitare la contabilità e la dichiarazione dei redditi.



## Bonus: Installazione su un server Bitcoin (Umbrel, RaspiBlitz, Start9)



Se possedete già un server Bitcoin come Umbrel, RaspiBlitz, MyNode o Start9, potete installare Specter Desktop direttamente dal loro negozio di applicazioni. Questo approccio offre diversi vantaggi significativi: l'applicazione si configura automaticamente con il vostro nodo Bitcoin core locale, rimane accessibile 24 ore su 24 e 7 giorni su 7 tramite un web Interface da qualsiasi dispositivo della vostra rete e potete persino accedervi in modo sicuro da remoto tramite Tor. L'intera infrastruttura Bitcoin è centralizzata su un unico server dedicato, semplificando la gestione e rafforzando la vostra sovranità.



### Installazione dall'App Store Umbrel



Dal vostro Umbrel Interface, andate sull'App Store e cercate Specter Desktop. Fare clic su "Installa" per avviare l'installazione.



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



Specter Desktop democratizza le configurazioni avanzate del Bitcoin, rendendo accessibile la multi-firma senza sacrificare la sovranità o la riservatezza. Per gli utenti che gestiscono quantità significative di denaro, trasforma le pratiche istituzionali in soluzioni utilizzabili dai privati.



Sebbene l'applicazione richieda un investimento iniziale in infrastrutture e apprendimento, offre una sovranità completa: controllo dell'infrastruttura di convalida, Ownership fisica delle chiavi e transazioni libere dalla sorveglianza di terzi. Che si tratti di un privato che mette al sicuro i propri risparmi, di una famiglia che crea una cassetta di sicurezza multigenerazionale o di un'azienda che gestisce il flusso di cassa, Specter Desktop è lo strumento di riferimento per conciliare massima sicurezza e sovranità assoluta.



## Risorse



### Documentazione ufficiale




- [Sito ufficiale di Specter Desktop](https://specter.solutions/desktop/)
- [Codice sorgente GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Documentazione completa](https://docs.specter.solutions/)



### Comunità e supporto




- [Gruppo comunitario Telegram Specter](https://t.me/spectersupport)
- [Forum di discussione Reddit](https://reddit.com/r/specterdesktop/)
- [Segnalazioni di bug su GitHub](https://github.com/cryptoadvance/specter-desktop/issues)
---
name: Blue Wallet

description: Bitcoin Portafoglio radicalmente semplice e potente
---
![cover](assets/cover.webp)



Iniziare a utilizzare il Bitcoin sembra essere una grande sfida per le persone che sono scettiche sulla semplicità del suo utilizzo. Trovare gli strumenti giusti per garantire questa semplicità diventa quindi di fondamentale importanza per una migliore adozione del Bitcoin come mezzo di comunicazione del Exchange e non solo come riserva di valore.



In questo tutorial daremo un'occhiata al Blue Wallet, un semplice ma efficacissimo Bitcoin Wallet che permette di gestire personalmente i propri bitcoin e anche di creare cooperative di gestione basate sul [Multisig](https://planb.network/resources/glossary/multisig) (non preoccupatevi, ci torneremo).



![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)



## Come iniziare con Blue Wallet



Blue Wallet è un Bitcoin Wallet open source che consente di assumere il controllo dei propri bitcoin. È disponibile come applicazione mobile su entrambe le piattaforme Android e iOS. In questo tutorial ci baseremo sulla versione Android, tuttavia tutti i processi che verranno sviluppati sono ugualmente validi su iOS.



![download](assets/fr/01.webp)



⚠️ Assicuratevi di scaricare l'applicazione Blue Wallet Bitcoin Wallet su una piattaforma ufficiale per garantirne l'autenticità e proteggere i vostri bitcoin da possibili fughe di notizie e hacking.



Una volta installato, è possibile creare un nuovo Wallet e salvare le 12 parole di recupero, oppure importare un Bitcoin Wallet esistente. Scoprite come effettuare un backup efficiente delle vostre parole chiave per non perdere l'accesso ai vostri bitcoin.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Con Blue Wallet è possibile creare portafogli Bitcoin separati e dedicati. Ad esempio, è possibile avere un Wallet per i risparmi e un altro per le spese quotidiane, tutti nella stessa applicazione.



![home](assets/fr/02.webp)



## Tipi di portafoglio



In Blue Wallet sono presenti due tipi di portafoglio nativi del Bitcoin.



### Portafoglio Bitcoin



Se siete abituati ad altri portafogli Bitcoin, come Phoenix o Aqua, non vi troverete affatto in disaccordo con il Interface con il portafoglio Bitcoin del Blue Wallet.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Il Wallet blu del Bitcoin Il Wallet rappresenta il Wallet standard nell'ecosistema Bitcoin. È possibile spendere bitcoin a patto di essere in possesso delle parole di recupero che forniranno una firma valida sulla rete per autenticare il possesso dei bitcoin.



Per creare un portafoglio Bitcoin, cliccare sul pulsante **Aggiungi ora**, inserire il nome del portafoglio e scegliere il tipo Bitcoin.



![bitcoin-wallet](assets/fr/03.webp)



Cliccando sull'anteprima del vostro Bitcoin Wallet, potrete visualizzare la cronologia delle transazioni e inviare e ricevere bitcoin.



⚠️ Tutte le transazioni nel Bitcoin Wallet sono sulla catena principale del protocollo Bitcoin (Mainnet).





- Ricevere bitcoin con il Bitcoin Blue Wallet Wallet è intuitivo. Nella parte inferiore dello schermo, fare clic sul pulsante **Ricevi**. Condividete il codice QR o il vostro Bitcoin Address con il mittente in modo che possa inviarvi i bitcoin.



È inoltre possibile configurare un importo predefinito per specificare la quantità di Bitcoin che si desidera ricevere.



![receive-bitcoin](assets/fr/04.webp)





- Sul pulsante **Invia**, inviare bitcoin a un Bitcoin Address, impostando l'importo desiderato e convalidando la transazione.



![send-bitcoin](assets/fr/05.webp)



Blue Wallet consente di configurare i parametri della spedizione Bitcoin come si desidera.



È quindi possibile selezionare il rapporto delle commissioni di transazione più adatto alle proprie esigenze se si desidera che la propria transazione venga rapidamente convalidata in un Mempool e inclusa in un blocco dai minatori. A seconda del rapporto scelto, i minatori daranno priorità alla vostra transazione in misura maggiore o minore. Per saperne di più, consultate il nostro tutorial sullo spazio Mempool.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- Con Blue Wallet è possibile aggiungere più destinatari a una singola spedizione.



Quando si aggiunge il Bitcoin Address del primo destinatario, nelle opzioni, fare clic su **Aggiungi destinatario**, aggiungere il Bitcoin Address e quindi impostare l'importo da inviare a questo destinatario, e così via. Blue Wallet invierà i bitcoin per più spedizioni in base alla vostra singola azione.



![add-recipients](assets/fr/07.webp)



È possibile rimuovere uno o tutti i destinatari facendo clic rispettivamente su **Rimuovi destinatario** e **Rimuovi tutti i destinatari**.



![remove-recipient](assets/fr/08.webp)





- **Gonfiare le commissioni**: Avete effettuato una transazione che richiede molto tempo per essere confermata? Abilitando l'inflazione delle commissioni, è possibile aggiungere ulteriori commissioni alla transazione in sospeso per accelerarne la conferma.



![bumping](assets/fr/09.webp)



### Portafoglio Multisig



Il Multisig (multi-firma) Wallet rappresenta un Wallet creato dal raggruppamento di un certo numero (minimo 2) di portafogli Bitcoin. In questo tipo di Wallet, a seconda della configurazione e del metodo scelto, spendere bitcoin diventa un'azione collettiva e cooperativa.



In Blue Wallet è possibile creare portafogli multi-firma per la propria associazione, la propria famiglia, la propria azienda. In questa sezione esploreremo ogni aspetto di questo speciale tipo di portafoglio.



Aggiungere un nuovo portafoglio e selezionare il tipo **Multisig Vault** per creare un portafoglio multi-firma.



![multisig-vault](assets/fr/10.webp)



Definire la configurazione m-de-n nella propria organizzazione multi-firma facendo clic su **Impostazioni di sicurezza**.



⚠️ In una configurazione m-of-n, **m** rappresenta il numero minimo di firme necessarie per approvare una transazione e **n** il numero di portafogli dell'organizzazione.



Assicurarsi di definire un numero minimo di firme (m) per la maggior parte dell'organizzazione. Ad esempio, una configurazione multi-firma 2 su 3 richiede che due portafogli dell'organizzazione firmino la transazione prima che questa possa essere eseguita.



definire una configurazione m-di-n dove n è uguale a m è un grosso rischio. Quando un membro perde l'accesso al suo Wallet, si perde l'autorizzazione a spendere i bitcoin nel Wallet.



Ecco alcuni esempi di configurazioni ottimali per garantire la sicurezza e l'accessibilità ai bitcoin:





- 2-de-3 multi-firma.





- 5-de-7 multi-firma.



![vault-settings](assets/fr/11.webp)



Attenersi alle migliori pratiche selezionando il formato P2WSH.



❗ **[P2WSH](https://planb.network/resources/glossary/p2wsh) o Pay to Witness Script Hash** è un metodo di blocco che blocca i bitcoin in uscita dalla transazione (output) al Hash di uno script personalizzato che Blue Wallet ha impostato. Il vantaggio principale di questo tipo di blocco è che riduce la dimensione dei dati delle transazioni e consente implicitamente di pagare commissioni di transazione inferiori.



Creare o importare ciascuno degli **n** portafogli della configurazione. Nella nostra esercitazione, utilizzeremo una configurazione a 2 di 3 firme multiple. Assicurarsi di salvare le parole di recupero per ogni portafoglio individualmente.



![vault-keys](assets/fr/12.webp)





- Ricevere bitcoin



Nella pagina Multisig Wallet si trovano la cronologia delle transazioni e i pulsanti Ricevi e Invia.



Ricevere bitcoin in un Wallet multi-firma è lo stesso processo che si svolge in un Bitcoin Wallet standard.





- Inviare **bitcoin**:



Gestendo un Wallet a firma multipla, spendere bitcoin diventa un'azione composta, sia con altre persone che con un secondo Wallet proprio. La singola firma del vostro Wallet non è più sufficiente. Questo aggiunge un Layer di sicurezza ai vostri bitcoin, perché un malintenzionato non sarà in grado di spendere quei bitcoin se entra in possesso di una sola delle vostre chiavi private.



Come per il portafoglio standard Bitcoin di Blue Wallet, è possibile definire più destinatari nell'opzione **Aggiungi destinatari**.



Quando si convalida la transazione, è necessaria una seconda firma per approvare la spesa dei bitcoin. Ricordate che siamo in una configurazione multi-firma 2-de-3.



Il secondo firmatario della Wallet, se è anch'egli un utente, può firmare la transazione anche se è fuori da Internet (senza Wi-Fi, senza dati mobili) scansionando il codice QR della [transazione parzialmente firmata](https://planb.network/resources/glossary/psbt) appena creata.



![mutisig-send](assets/fr/13.webp)





- Andate oltre con il **portafoglio multi-firma**:



Sul Interface del Wallet a firma multipla, fare clic sul pulsante **Gestione chiavi**.



Dimenticando una delle parole di recupero di uno dei portafogli firmatari (**Dimentica questo seed...**), si comunica al Wallet blu di cancellare il backup di queste parole dalla sua memoria. Avrete quindi effettuato un backup esterno.



![revoke-key](assets/fr/14.webp)



Eseguendo questa azione, si conserva solo la chiave pubblica associata a queste parole di recupero.



⚠️ La conservazione delle sole chiavi pubbliche (XPUB) consente di aggiungere un ulteriore livello di sicurezza alla configurazione multi-firma 2 su 3. In effetti, potrebbe essere dannoso conservare tutte le parole di recupero in un unico posto quando il telefono viene attaccato. Infatti, potrebbe essere dannoso tenere tutte le parole di recupero in un unico posto quando il telefono è sotto attacco. Gli aggressori che hanno accesso a un solo **VAULT** (parola chiave) che utilizzate per firmare le vostre transazioni, non saranno in grado di rubare i vostri bitcoin (è richiesto un minimo di 02 firme) perché le chiavi pubbliche non possono essere utilizzate per firmare le transazioni.



## Altre opzioni con Blue Wallet



### Migliorare la sicurezza dell'accesso al portafoglio



In Impostazioni, l'opzione **Sicurezza** consente di definire l'uso di un'impronta digitale per effettuare una transazione, esportare o cancellare il Wallet. In questo modo si autentica la persona che utilizza lo smartphone.



![biometry](assets/fr/15.webp)



## Attivare il Lightning Network



Il Lightning Network non è più supportato in modo nativo nell'applicazione Blue Wallet.



In Impostazioni > **Impostazioni Lightning**, è possibile associare manualmente il Lightning Wallet quando si gestisce un nodo Lightning Network Daemon (LND). Installare l'hub LND, quindi associare il Wallet inserendo il link generato dall'hub.



![ln](assets/fr/16.webp)



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Ora avete completato il tour di Blue Wallet e siete pronti a utilizzare Bitcoin in tutta la sua semplicità e potenza. Vi consigliamo di fare il passo successivo e di scoprire come accettare i pagamenti Bitcoin nei vostri negozi, grazie alla potenza di Lightning.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06
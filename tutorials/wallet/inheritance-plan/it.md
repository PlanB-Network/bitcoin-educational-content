---
name: Piano di eredità Bitcoin
description: Come trasferire bitcoin ai propri cari
---

![cover](assets/cover.webp)



La trasmissione dei bitcoin rappresenta un'importante sfida tecnica che molti detentori trascurano. A differenza delle attività bancarie tradizionali, dove un istituto finanziario può rimettere i fondi ai legittimi proprietari, il Bitcoin funziona senza intermediari. I vostri cari non potranno mai accedere ai vostri fondi senza le necessarie informazioni tecniche, indipendentemente dalla loro legittimità legale.



Questa esercitazione vi guida nella creazione di un piano di eredità tecnica. Imparerete come funzionano i meccanismi on-chain per la trasmissione automatica, come documentare le vostre configurazioni e come scegliere le soluzioni giuste per garantire che la vostra eredità Bitcoin rimanga accessibile ai vostri cari.



## Perché un piano tecnico del patrimonio è essenziale



Il Bitcoin si basa su un principio crittografico fondamentale: chi detiene le chiavi private controlla i fondi. Questa sovranità diventa una grande vulnerabilità quando il titolare scompare senza aver trasmesso le informazioni necessarie.



Un piano di eredità Bitcoin deve soddisfare due obiettivi apparentemente contraddittori: consentire ai vostri cari di accedere ai vostri fondi al momento opportuno, impedendo al contempo a chiunque altro di accedervi prematuramente. Questo delicato equilibrio si basa sulle capacità di programmazione native del Bitcoin.



La complessità tecnica aggiunge un ulteriore livello di difficoltà. Gli eredi dovranno manipolare concetti come frasi di recupero, descrittori di portafoglio o percorsi di derivazione. Senza un'adeguata preparazione, anche un erede ben intenzionato rischia di commettere errori irreversibili.



## Come funziona l'ereditarietà del on-chain



Bitcoin utilizza il suo linguaggio di scripting per codificare le condizioni di spesa direttamente nelle transazioni. L'ereditarietà del on-chain sfrutta questa programmabilità per creare percorsi di recupero alternativi che si attivano automaticamente.



### Orologi a tempo



I blocchi temporali sono il meccanismo fondamentale dell'eredità Bitcoin. Consentono di bloccare i fondi fino a quando non viene soddisfatta una condizione temporale.



**CLTV (CheckLockTimeVerify)**: Questo blocco temporale assoluto controlla che sia stato raggiunto un tempo specifico (data o altezza del blocco) prima di autorizzare la spesa. Ad esempio, "questi fondi possono essere spesi solo dopo il blocco 900000" o "dopo il 1° gennaio 2026". Il vantaggio del CLTV è che consente lunghi ritardi (diversi anni), ma la data è fissa e si applica in modo identico a tutti gli UTXO del portafoglio. Per mantenere il controllo dei propri fondi, è necessario creare periodicamente un nuovo portafoglio con una data di scadenza estesa e trasferirvi i fondi.



**CSV (CheckSequenceVerify)**: Questo timelock relativo verifica che sia trascorso un certo numero di blocchi da quando è stato creato il UTXO. Ad esempio, "questi fondi possono essere spesi solo dopo 52560 blocchi (~1 anno) dal ricevimento". Il vantaggio del CSV è che ogni UTXO ha un proprio contatore indipendente. Ogni volta che si esegue una transazione, gli UTXO appena creati azzerano il proprio limite di tempo. Tuttavia, il limite tecnico di 65535 blocchi (~15 mesi al massimo) limita i tempi possibili. Questo approccio è più naturale per l'uso quotidiano, poiché la normale attività fa automaticamente slittare le scadenze.



### Percorsi di spesa multipli



Un portafoglio ereditario combina diversi percorsi di spesa in ogni indirizzo:





- Percorso principale** : Il proprietario può spendere i suoi fondi in qualsiasi momento con la sua chiave principale, senza limiti di tempo.
- Percorso/i di recupero **: Una o più chiavi alternative possono spendere i fondi solo dopo che è trascorso un tempo prestabilito.



Ogni transazione eseguita dal proprietario "rinfresca" il UTXO, creando nuove uscite con timelock azzerati. Questo meccanismo garantisce che, finché il proprietario rimane attivo, i percorsi di ripristino non si attivino mai.



### Miniscript e Taproot



**Miniscript** è un linguaggio strutturato sviluppato da Andrew Poelstra, Pieter Wuille e Sanket Kanjalkar che facilita la scrittura e l'analisi di script Bitcoin complessi. Permette di comporre condizioni di spesa leggibili e verificabili, essenziali per le configurazioni di ereditarietà che coinvolgono più chiavi e orologi a tempo.



**Taproot** (attivato nel novembre 2021) migliora significativamente l'eredità on-chain. Grazie alla sua struttura ad albero (MAST), solo la condizione di spesa utilizzata viene rivelata sulla blockchain. Se il proprietario spende normalmente i suoi fondi, le condizioni di eredità rimangono invisibili. Questa riservatezza riduce anche i costi di transazione per i percorsi complessi.



## L'importanza critica dei descrittori



Per i portafogli legacy, la frase di recupero (seed) non è sufficiente per ripristinare l'accesso ai fondi. Il **descrittore** diventa l'elemento critico.



Un descrittore è una stringa che descrive in modo esaustivo la struttura di un portafoglio: le chiavi pubbliche coinvolte, le condizioni di spesa, i percorsi di derivazione e i timelock configurati. Ecco un esempio semplificato:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Questo descrittore dice: "o la chiave master può spendere immediatamente, o la chiave di recupero può spendere dopo 52560 blocchi".



Vediamo di analizzare questo esempio:




- `wsh()` : Witness Script Hash, indica il tipo di indirizzo (P2WSH)
- or_d()`: condizione "or" con un ramo predefinito
- pk([fingerprint/path]xpub...)`: La chiave pubblica master con la sua impronta digitale e il percorso di derivazione
- e_v()`: condizione "and" che combina la chiave di recupero con il timelock
- più vecchio (52560): Il blocco temporale relativo di 52560 blocchi



**Senza il descrittore, anche con tutte le frasi di recupero, gli eredi non saranno in grado di ricostruire il portafoglio ** Un portafoglio standard può essere ripristinato solo da seed perché segue percorsi di derivazione standardizzati (BIP44, BIP84). Un portafoglio legacy, invece, utilizza script personalizzati che non possono essere indovinati. Il backup del descrittore (o il file di configurazione esportato dal software) deve accompagnare le frasi di ripristino nel piano di ereditarietà.



## Componenti documentali di un piano di successione



Al di là dei meccanismi tecnici, un piano legacy efficace si basa su tre pilastri di documentazione.



### La lettera di eredità



Questa lettera personale è il punto di ingresso al vostro piano. Scritta per i vostri eredi, spiega il contesto e le precauzioni da prendere.



La lettera deve contenere esplicite regole di sicurezza:




- Non abbiate fretta, prendetevi del tempo per imparare prima di muovere i fondi
- Non comunicare mai una frase di recupero completa a una sola persona
- Non inserite mai una frase di recupero in un programma software o in un computer non verificato
- Attenzione alle truffe e alle persone che offrono aiuto non richiesto
- Chiedete il parere di almeno due persone di fiducia prima di prendere una decisione



Questa lettera contiene anche i dati di contatto del notaio e l'ubicazione del testamento. Non deve mai contenere frasi di recupero o password.



### La directory dei contatti di fiducia



Nessun erede dovrebbe affrontare il recupero di bitcoin da solo. Questo elenco elenca le persone che possono fornire assistenza tecnica o legale.



Per ogni contatto, documentare: nome e cognome, relazione con l'erede, ruolo nel piano, livello di fiducia, capacità di Bitcoin e recapiti completi. La regola fondamentale è che gli eredi devono sempre consultare almeno due persone diverse prima di prendere qualsiasi decisione importante.



### Inventario delle attività Bitcoin



In questa sezione sono riportati tutti i vostri bitcoin con le informazioni tecniche necessarie per recuperarli.



Per ogni portafoglio, documentare :




- Tipo di portafoglio**: hardware, software, configurazione (single-sig, multisig, legacy)
- Posizione del dispositivo**: posizione fisica dell'hardware wallet
- Posizione del file Descriptor/configurazione**: critica per i portafogli avanzati
- Posizione della frase di recupero**: separata dal descrittore
- Codici di accesso**: dove vengono memorizzati PIN e passphrase
- Ritardi configurati**: quando si attivano i percorsi di recupero



## Soluzioni tecniche disponibili



Diversi pacchetti software implementano meccanismi di ereditarietà on-chain. Ciascuno di essi ha caratteristiche tecniche proprie. Ognuno di essi ha le proprie caratteristiche tecniche.



### Liana



Liana è un software desktop (Linux, macOS, Windows) che utilizza Miniscript per creare portafogli con percorsi di recupero a tempo. Il progetto è sviluppato da Wizardsardine, co-fondato da Antoine Poinsot (collaboratore di Bitcoin Core).



**Architettura tecnica**: Liana crea portafogli P2WSH (nativi di SegWit) per impostazione predefinita, con il supporto di Taproot disponibile a seconda della compatibilità dell'hardware wallet. L'architettura si basa su un percorso principale e su uno o più percorsi di recupero. Il descrittore generato codifica tutte le condizioni e deve essere salvato.



**Timelocks utilizzati**: Liana utilizza timelock relativi (CSV), limitati a 65535 blocchi (~15 mesi). Per mantenere il controllo, è necessario eseguire una transazione di aggiornamento prima della scadenza del timelock.



**Integrazione hardware wallet**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY e altri dispositivi sono compatibili per la firma delle transazioni.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper è un'applicazione mobile (iOS, Android) che combina multisig e orologi a tempo tramite i suoi "Enhanced Vaults". L'approccio mobile con guida integrata lo rende accessibile anche agli utenti meno tecnici.



**Architettura tecnica**: I caveau potenziati utilizzano Miniscript per creare configurazioni multisigma in cui le chiavi aggiuntive si attivano dopo ritardi definiti. La chiave di eredità si aggiunge al quorum esistente, mentre la chiave di emergenza può bypassare completamente il multisig.



**Timelocks utilizzati**: Il Bitcoin Keeper utilizza orologi temporali assoluti (CLTV), consentendo tempi di consegna superiori a 15 mesi. La data di attivazione viene impostata alla creazione del wallet e si applica a tutti gli UTXO. L'applicazione incorpora una funzione di "revaulting" che gestisce automaticamente il refresh: l'utente deve semplicemente seguire i passi guidati, senza dover creare manualmente un nuovo wallet.



**Caratteristiche aggiuntive**: Documenti di eredità integrati, portafogli Canary per rilevare la compromissione delle chiavi e promemoria di aggiornamento.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Patrimonio



Heritage è un'applicazione desktop che utilizza gli script Taproot per codificare le condizioni di eredità. L'uso di Taproot offre una maggiore riservatezza, poiché i percorsi non utilizzati rimangono invisibili sulla blockchain.



**Architettura tecnica**: Ogni indirizzo del Patrimonio integra un percorso principale e percorsi alternativi per ciascun erede, con tempistiche progressive. La struttura gerarchica consente di definire un backup personale a 6 mesi e gli eredi familiari a 12-15 mesi.



**Modalità di utilizzo**: Versione stand-alone con il proprio nodo (gratuita) o servizio gestito che aggiunge promemoria e notifiche agli eredi (0,05%/anno).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Il processo di recupero dell'erede



Comprendere il processo di recupero aiuta a preparare un piano efficace. Ecco le fasi tecniche che un erede dovrà seguire.



### Requisiti di recupero



L'erede ha bisogno di :


1. **Il descrittore o il file di configurazione** del portafoglio originale (formato JSON o testo, a seconda del software)


2. **La sua frase di recupero** (quella associata alla sua chiave di eredità, di solito 12 o 24 parole)


3. **Software compatibile** (Liana, Bitcoin Keeper, Heritage o Sparrow/Specter per i descrittori standard)


4. **Una connessione a un nodo Bitcoin** per controllare lo stato del timelock e trasmettere la transazione



### Fasi di recupero



1. **Installare il software** su un dispositivo sicuro e configurare la connessione alla rete Bitcoin (nodo personale o server Electrum)


2. **Importare il descrittore** per ricostruire la struttura del portafoglio. Il software generate automaticamente tutti gli indirizzi utilizzati


3. **Ripristinare la chiave di eredità** dalla frase di recupero. Il software verificherà che questa chiave corrisponda a una delle chiavi autorizzate nel descrittore


4. **Sincronizzare il portafoglio** per scoprire tutti gli UTXO e le loro condizioni di spesa


5. **Verifica scadenza timelock**: il software indicherà per ogni UTXO se il percorso di ripristino è attivo


6. **Creare la transazione di recupero** verso un indirizzo controllato esclusivamente dall'erede (idealmente un nuovo singolo wallet)


7. **Firmare e trasmettere** la transazione sulla rete Bitcoin



Se il blocco temporale non è ancora scaduto, l'erede dovrà attendere. Il software visualizzerà la data o il blocco a partire dal quale sarà possibile il recupero. Durante questo periodo di attesa, i fondi rimangono al sicuro sulla blockchain.



### Punti da tenere d'occhio per l'erede



L'erede deve prestare particolare attenzione a :




- Controllare l'autenticità del software scaricato** (checksum, firme)
- Non condividete mai la vostra frase di recupero** con chi vi offre aiuto
- Consultare almeno due persone di fiducia** prima di effettuare il recupero
- Trasferire i fondi in un portafoglio semplice**, che il paziente controlla completamente dopo la guarigione



## Le migliori pratiche



### Separazione delle informazioni



Non memorizzare mai tutte le informazioni in un unico posto. Il descrittore deve essere separato dalle frasi di recupero, che a loro volta sono separate dai codici PIN. Questa distribuzione complica l'accesso di un aggressore, pur rimanendo ricostituibile dagli eredi legittimi.



### Test di recupero



Prima di depositare fondi consistenti, testate l'intero processo di recupero con una piccola somma. Verificare che sia possibile ripristinare il portafoglio dal descrittore e dalle frasi di recupero su un dispositivo vuoto. Documentate i passaggi per i vostri eredi.



### Manutenzione del timer



Pianificate di aggiornare i vostri timelock ben prima della loro scadenza. Per un timelock di 12 mesi, eseguire una transazione ogni 9-10 mesi. Di solito i software offrono promemoria o funzioni di aggiornamento automatico.



### Aggiornamento del piano



La configurazione del Bitcoin si evolve. Ogni cambiamento significativo (nuovo portafoglio, modifica delle scadenze, aggiunta di un erede) deve essere riportato nella documentazione. Stabilire una routine di revisione annuale.



## Scegliere l'approccio



La scelta tra le diverse soluzioni dipende dal profilo tecnico e dalle esigenze specifiche.



**Liana** è adatto agli utenti desktop che preferiscono un software open source con il pieno controllo tramite il proprio nodo. La configurazione rimane accessibile grazie all'interfaccia guidata. I timelocks relativi (CSV) semplificano la manutenzione, poiché la normale attività fa slittare automaticamente le scadenze. Limitazione: ritardo massimo di circa 15 mesi (65535 blocchi).



**Bitcoin Keeper** si rivolge agli utenti mobili che cercano un'interfaccia intuitiva con documenti di accompagnamento integrati. L'applicazione offre due tipi di chiavi speciali: la chiave di eredità (che si aggiunge al quorum) e la chiave di emergenza (che lo aggira completamente). I timelock assoluti (CLTV) consentono tempi di consegna superiori a 15 mesi, con una funzione di revaulting integrata che semplifica il refresh. Il piano Diamond Hands sblocca le funzioni legacy avanzate.



**L'ereditarietà** è rivolta agli utenti tecnici che apprezzano la riservatezza di Taproot e l'ereditarietà gerarchica con ritardi progressivi. La struttura ad albero di Taproot nasconde le condizioni di ereditarietà durante le normali transazioni, rivelando solo la condizione utilizzata durante il recupero.



Tutte e tre le soluzioni hanno una cosa in comune: richiedono un aggiornamento periodico per evitare l'attivazione prematura dei percorsi di ripristino. Questo vincolo è sia il prezzo che la garanzia dell'eredità non affidabile del on-chain. Programmate promemoria regolari e fate in modo che questa manutenzione faccia parte della vostra routine di gestione del Bitcoin.



## Conclusione



Un piano tecnico Bitcoin legacy combina meccanismi crittografici (timelocks, Miniscript, Taproot) con una documentazione rigorosa. I portafogli avanzati consentono di trasmettere automaticamente i bitcoin dopo un periodo di inattività, senza l'intervento di terzi.



Gli elementi critici da trasmettere agli eredi sono: il descrittore o il file di configurazione, la frase di recupero, le istruzioni dettagliate per il recupero e i recapiti delle persone competenti che possono assisterli.



Iniziate scegliendo una soluzione tecnica adatta al vostro profilo, testatela con una piccola quantità, quindi documentate il tutto in un piano strutturato. La complessità iniziale garantisce che il vostro patrimonio Bitcoin venga trasmesso in piena fiducia.



## Risorse



### Modello di piano di successione





- [Modello di piano di eredità Bitcoin (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Modello di documentazione Plan ₿ Network



### Riferimenti tecnici





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Specifiche dei timelock assoluti (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Specifica dei timelock relativi (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Documentazione ufficiale di Miniscript, a cura di Pieter Wuille



### Siti web ufficiali delle soluzioni





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Patrimonio Wallet](https://btc-heritage.com/) - Crypto7
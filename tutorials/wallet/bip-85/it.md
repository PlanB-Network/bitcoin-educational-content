---
name: BIP-85
description: Come si può utilizzare il BIP-85 per generate più frasi di seme da un seed principale?
---
![cover](assets/cover.webp)



## 1. Comprendere il BIP-85



### 1.1 Che cos'è il BIP-85?



BIP-85 è una funzione avanzata che consente di creare diverse **frasi secondarie seed** da una **frase principale seed**.



Ogni frase secondaria seed può essere utilizzata per creare un portafoglio Bitcoin completamente indipendente. Questi portafogli possono essere utilizzati per diversi scopi: un Hot Wallet sul cellulare, un portafoglio per un parente, un portafoglio di risparmio separato, ecc.



Tutte le sottofrasi seed sono **derivate matematicamente**, ma è **impossibile risalire alla frase principale seed** da una sottofrase. Questo garantisce la completa separazione tra ogni portafoglio.



Finché si ha accesso alla frase principale seed (e al passphrase associato, se se ne usa uno), è possibile rigenerare qualsiasi frase secondaria seed in modo **identico**, senza doverla salvare separatamente.



### 1.2 Perché utilizzare il BIP-85?



Il BIP-85 è utile se si desidera :





- Creazione di più portafogli Bitcoin indipendenti senza backup multipli
- Gestire i fondi in base ai diversi usi (risparmi, spese, famiglia, progetti)
- Garantire le tutele per i parenti (funzione "Uncle Jim")
- Cancellare un portafoglio senza perdere l'accesso ai fondi
- Semplificare la sicurezza: solo una frase chiave seed da proteggere



### 1.3 Vantaggi rispetto al BIP-32



Con BIP-32, una singola frase seed può essere utilizzata per generate una gerarchia completa di conti e indirizzi Bitcoin, utilizzando percorsi di derivazione (ad esempio: `m/44'/0'/0'/0/0`). Ogni percorso può rappresentare un account separato, ma **tutti rimangono collegati alla stessa frase seed**. Quindi, se questa frase seed viene compromessa, **tutti gli account derivati diventano accessibili**.



Con BIP-85, una frase principale seed può essere utilizzata per generate diverse frasi secondarie seed totalmente indipendenti: **Se uno di questi semi secondari viene compromesso, l'attaccante non sarà mai in grado di tornare al seed principale o di accedere agli altri portafogli**.


In questo modo è possibile compartimentare i rischi:





- È possibile utilizzare un seed secondario per il Hot Wallet o per un uso temporaneo, accettando un'esposizione maggiore.
- Anche se questo Hot Wallet viene compromesso, gli altri fondi, protetti da altri semi secondari o tenuti offline, **rimangono al sicuro**.



D'altra parte, sia per il BIP-32 che per il BIP-85, se il seed principale viene compromesso, **tutti i fondi sono vulnerabili**. È quindi fondamentale proteggerlo con il massimo livello di sicurezza.



![image](assets/fr/02.webp)


## 2. Casi d'uso pratici per il BIP-85



Il BIP-85 consente di creare più portafogli Bitcoin a partire da un'unica frase centrale seed, ciascuno con la propria frase secondaria seed. Ecco cinque casi d'uso pratici per organizzare e proteggere i fondi Bitcoin. Ogni caso spiega perché l'uso di BIP-85 è più pratico della gestione di più conti seed. Ogni caso spiega perché l'uso di BIP-85 è più pratico rispetto alla gestione di più conti con una singola frase seed tramite BIP-32.



### 2.1 Limitare il rischio di un portafoglio meno sicuro





- Scenario**: Si utilizza un "Hot Wallet" Wallet (installato su un dispositivo connesso a Internet), per le transazioni quotidiane.
- Soluzione BIP-85**: Si crea una frase secondaria seed dedicata a questo portafoglio.
- Vantaggio rispetto al BIP-32**: Non è necessario importare la frase primaria del seed sul telefono, riducendo il rischio di hacking. Solo la frase secondaria del seed viene compromessa, proteggendo gli altri portafogli. Con BIP-32, è necessario utilizzare la frase principale del seed e un percorso di bypass, esponendo tutti i fondi.



### 2.2 Creare un portfolio per un familiare





- Scenario**: Si imposta un Bitcoin Wallet per una persona cara (ad esempio, la propria madre), con la possibilità di recuperarlo in caso di smarrimento.
- Soluzione BIP-85**: Si crea una frase secondaria seed dedicata e si condivide solo questa.
- Vantaggio rispetto a BIP-32**: Con BIP-32, la creazione di un conto per una persona cara richiede la condivisione della frase seed principale, mettendo a rischio tutti i fondi e complicando la gestione per la persona amata (gestione dei percorsi di ramificazione), oppure la creazione di una nuova frase seed da salvare in aggiunta alla frase seed principale.



### 2.3 Facilitare la gestione di portafogli separati





- Scenario**: Separate i vostri bitcoin per scopi diversi (ad esempio, risparmi a lungo termine, fondi non KYC).
- Soluzione BIP-85**: Si creano frasi secondarie seed dedicate a ciascun obiettivo.
- Vantaggio rispetto a BIP-32**: Con BIP-32, tutti i conti condividono la stessa frase seed, il che complica la gestione nei portafogli di terze parti richiedendo la gestione di percorsi di derivazione come `m/44'/0'/0'`. Inoltre, non è possibile assegnare un conto separato per dispositivo (ad esempio, "risparmi su Coldcard", "giornaliero su cellulare", "vacanze su Trezor"). BIP-85 assegna una frase secondaria seed unica per obiettivo, che è facile da identificare e importare separatamente su ogni dispositivo.



### 2.4 Utilizzo di un Wallet temporaneo per le transazioni





- Scenario**: Avete bisogno di un portafoglio temporaneo per una transazione unica o per preservare la riservatezza (ad esempio: miscelazione di fondi, interazione con un KYC Exchange, ecc.)
- Soluzione BIP-85**: Si crea una frase secondaria seed, la si utilizza per la transazione, quindi la si distrugge se necessario, sapendo che può essere rigenerata.
- Vantaggio rispetto a BIP-32**: Con BIP-32, un conto temporaneo dipende dalla frase principale seed, esponendo tutti i vostri fondi se compromessi.





## 3. Prima di iniziare





- Hardware** (opzionale)
 - Coldcard Mk4 o Q1
 - Scheda MicroSD





- Conoscenze di base
 - Comprendere le frasi Mnemonic (BIP-39): un elenco di 12-24 parole per salvare un portfolio.
 - Sapere cos'è un Bitcoin Wallet: un software o un dispositivo per la gestione dei bitcoin e come ripristinarlo con una frase Mnemonic.
 - Altre risorse negli allegati.





- Software compatibile**
 - Sparrow wallet (computer, per la sola sorveglianza o la gestione avanzata)
 - Nunchuck (mobile, per le firme multiple)
 - BlueWallet (mobile)
 - ...





- 3.4 Configurazione Coldcard**
 - Inizializzare una frase seed di 24 parole sulla Coldcard.
 - Opzionale: Aggiungere un passphrase per proteggere l'accesso ai rami BIP-85.
 - Attivare le opzioni utili: NFC (per l'esportazione), disabilitazione dell'USB a batteria (sicurezza).




## 4. Tutorial passo dopo passo



Seguite questi passaggi per creare, utilizzare e recuperare un Mnemonic secondario con BIP-85 sulla vostra Coldcard.



### 4.1 generate a seed frase secondaria



Si creerà una frase secondaria seed a partire dalla frase principale seed.


Accendere la Coldcard, inserire il codice PIN.





- 1. Se si è applicato un passphrase al proprio seed principale:**
 - Dalla schermata principale, andare su `passphrase`.
    - Scegliere "Aggiungi parola" e inserire la password.
    - Premere "Applica".
    - Controllare l'identità del Wallet: Andare su `Avanzate > Visualizza identità` per notare l'impronta digitale del Wallet.





- 2. Andare al menu BIP-85**
 - Nella schermata principale, andare su `Avanzate > Derive seed B85`
 - Leggere l'avviso e confermare.



La ColdCard informa che i semi generati sono matematicamente derivati dal vostro seed principale, ma crittograficamente totalmente indipendenti.


![image](assets/fr/03.webp)





- 3. Scegliere un formato


Selezionare il formato della frase seed: 12, 18 o 24 parole. Controllare il numero di parole accettate dal Wallet in cui si desidera importare la frase seed.


![image](assets/fr/04.webp)





- 4. Selezionare l'indice
 - Inserire un indice compreso tra 0 e 9999.
 - Questo indice è fondamentale per rigenerare il seed secondario in un secondo momento. Conservatelo con cura con un'etichetta come: "Indice 1 = Wallet mobile", "Indice 2 = progetto famiglia", "Indice 4 = miscela di prova", ...
 - Se lo perdete, non perderete l'accesso ai vostri fondi, ma dovrete testare le combinazioni da 0 a 9999 per trovarli.


![image](assets/fr/05.webp)





- 5. Nota o esportazione della frase secondaria seed**


ColdCard visualizza ora una nuova frase secondaria seed. È possibile :




 - La **note manualmente**.
 - Stampa :
     - 1` per salvarlo sulla scheda SD
     - `2` per **inserire la modalità "usa questo seed"** sulla ColdCard (utile per esportare o firmare una transazione)
     - 3` per visualizzare un **codice QR** (da scansionare con un'applicazione mobile come BlueWallet o Nunchuck)
     - 4` per inviarlo tramite **NFC**



💡 A questo punto, avete una frase seed indipendente, utilizzabile in qualsiasi Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Utilizzo del seed secondario



È ora possibile utilizzare questo seed derivato per creare un nuovo portafoglio in :




- un'applicazione mobile
- un altro Hardware Wallet
- un portafoglio Multisig



### 4.3 Recupero di una frase secondaria seed perduta



Per recuperare un seed secondario in qualsiasi momento, ripetere la procedura:


1. Riavviare la ColdCard


2. Inserire il PIN


3. Inserire il proprio passphrase, se definito


4. Andare su `Avanzate > Deriva seed B85


5. Scegliere il formato (12/18/24 parole)


6. Inserire lo stesso indice (ad es. `1`)


7. Otterrete esattamente lo stesso secondario seed




## 5. Limiti, rischi e buone pratiche



### 5.1 Dipendenza dalla frase principale seed + passphrase



L'uso di BIP85 si basa interamente sulla frase principale di 24 parole seed, oltre che su passphrase se ne avete applicata una.




- Da questi due Elements si possono rigenerare tutte le frasi secondarie seed.
- Senza uno di questi 2 Elements, si perde l'accesso a tutti i portafogli derivati.



### 5.2 Rischi della configurazione multi-firma



Si sconsiglia vivamente di utilizzare frasi seed secondarie generate dalla stessa frase seed primaria in una configurazione multi-sig: se il dispositivo o la frase seed primaria vengono compromessi, tutte le chiavi multi-sig potrebbero essere rigenerate da un utente malintenzionato.



### 5.3 Compatibilità del software



Non tutte le applicazioni supportano direttamente la derivazione BIP85. Tuttavia, i semi generati tramite BIP85 sono semi BIP39 standard (12, 18 o 24 parole) e possono quindi essere utilizzati in qualsiasi portafoglio compatibile con BIP39.



### 5.4 Registro dei conti BIP85



Si raccomanda di tenere un registro personale aggiornato delle frasi secondarie del seed.




- Consente di scoprire rapidamente quale indice BIP85 corrisponde a quale portafoglio, senza dover tenere le frasi secondarie seed.
- Questo registro deve rimanere minimalista, senza alcuna menzione esplicita del Bitcoin, e deve essere conservato separatamente dal seed principale. Ricordatevi di menzionarlo nel vostro piano di eredità.



Il registro può contenere :




- bIP85 indice utilizzato (numero da 0 a 9999)
- un nome d'uso o di riferimento (ad esempio Hot Wallet, risparmio personale, Wallet della mamma)
- se necessario, l'impronta digitale Wallet per la verifica in ColdCard



### 5.5 Backup



I backup devono includere :




- il principale seed
- gW-76 (se utilizzato)



Non conservare mai insieme:




- i principali seed e passphrase
- il seed principale e il registro dei conti BIP85



Altre risorse negli allegati.




## APPENDICI



## A.1 Glossario





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [frase seed](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Salvare la frase di recupero



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Comprensione del passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Come funzionano i portafogli Bitcoin



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
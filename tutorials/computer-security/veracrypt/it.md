---
name: VeraCrypt
description: Come criptare facilmente un dispositivo di archiviazione?
---

![cover](assets/cover.webp)

Oggi giorno, è importante implementare una strategia per garantire l'accessibilità, la sicurezza e il backup dei propri file, come documenti personali, foto o progetti importanti. La perdita di questi dati può essere catastrofica.

Per prevenire questi problemi, consiglio di mantenere più backup dei propri file su diversi supporti. Una strategia comunemente utilizzata nell'informatica è la strategia di backup "3-2-1", che garantisce la protezione dei tuoi file:
- **3** copie dei tuoi file;
- Salvate su almeno **2** tipi diversi di supporti;
- Con almeno **1** copia conservata in un luogo esterno.

In altre parole, è consigliabile conservare i propri file in 3 luoghi diversi, utilizzando supporti di natura diversa, come il proprio computer, un disco rigido esterno, una chiavetta USB o un servizio di archiviazione online. E infine, avere una copia esterna significa che si dovrebbe avere un backup conservato fuori dalla propria casa o azienda. Quest'ultimo punto aiuta ad evitare la perdita totale dei propri file in caso di disastri locali come incendi o alluvioni. Una copia esterna, distante dalla propria casa o azienda, garantisce che i propri dati sopravvivranno indipendentemente dai rischi locali.

Per implementare facilmente questa strategia di backup 3-2-1, si può optare per una soluzione di archiviazione online, sincronizzando automaticamente o periodicamente i file dal proprio computer con quelli nel cloud. Tra queste soluzioni di backup online, ci sono ovviamente quelle delle grandi aziende digitali che conoscete: Google Drive, Microsoft OneDrive o Apple iCloud. Tuttavia, queste non sono le migliori soluzioni per proteggere la propria privacy. In un tutorial precedente, ti ho presentato un'alternativa che cripta i tuoi documenti per una migliore riservatezza: Proton Drive.

https://planb.academy/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Adottando questa strategia di backup locale e cloud, si beneficia già di due tipi diversi di supporti per i propri dati, uno dei quali è esterno. Per completare la strategia 3-2-1, è sufficiente aggiungere una copia aggiuntiva. Quello che consiglio di fare è semplicemente esportare periodicamente i propri dati presenti localmente e sul cloud su un supporto fisico, come una chiavetta USB o un disco rigido esterno. In questo modo, anche se i server della tua soluzione di archiviazione online vengono distrutti e il tuo computer si guasta simultaneamente, avrai comunque questa terza copia su un supporto esterno per non perdere i tuoi dati.

![VeraCrypt](assets/notext/01.webp)

Ma è anche importante pensare alla sicurezza della tua archiviazione dati per garantire che nessuno, a parte te o i tuoi cari, possa accedervi. Normalmente, sia i dati locali che quelli online sono sicuri. Sul tuo computer, probabilmente hai impostato una password, e i dischi rigidi dei computer moderni sono spesso criptati di default. Riguardo al tuo archivio online (cloud), ti ho mostrato nel tutorial precedente come proteggere il tuo account con una password forte e l'autenticazione a due fattori. Tuttavia, per la tua terza copia conservata su un supporto fisico, l'unica sicurezza è il suo possesso fisico. Se un ladro riesce a rubare la tua chiavetta USB o il tuo disco rigido esterno, potrebbe facilmente accedere a tutti i tuoi dati.

![VeraCrypt](assets/notext/02.webp)

Per prevenire questo rischio, è consigliabile criptare il proprio supporto fisico. Così, qualsiasi tentativo di accedere ai dati richiederà l'inserimento di una password per decriptare il contenuto. Senza questa password, sarà impossibile accedere ai dati, garantendo la sicurezza dei tuoi file personali anche in caso di furto della tua chiavetta USB o del tuo disco rigido esterno.

![VeraCrypt](assets/notext/03.webp)

In questo tutorial, ti mostrerò come criptare facilmente un supporto di memorizzazione esterno utilizzando VeraCrypt, uno strumento open-source.


## Introduzione a VeraCrypt

VeraCrypt è un software open-source disponibile su Windows, macOS e Linux, che consente di criptare i propri dati in vari modi e su diversi supporti.

![VeraCrypt](assets/notext/04.webp)

Questo software permette la creazione e la manutenzione di volumi criptati al volo, il che significa che i dati vengono automaticamente criptati prima di essere salvati e decriptati prima di essere letti. Questo metodo garantisce che i file rimangano protetti anche in caso di furto del tuo supporto di memorizzazione. VeraCrypt non cripta solo i file, ma anche i nomi dei file, i metadati, le cartelle e persino lo spazio libero sul tuo supporto di memorizzazione.

VeraCrypt può essere utilizzato per criptare file localmente o intere partizioni, inclusi i dischi di sistema. Può anche essere utilizzato per criptare completamente un supporto esterno come una chiavetta USB o un disco come vedremo in questo tutorial.

Un grande vantaggio di VeraCrypt rispetto alle soluzioni proprietarie è che è completamente open source, il che significa che il suo codice può essere verificato da chiunque.


## Come installare VeraCrypt?

Vai sul [sito ufficiale di VeraCrypt](https://veracrypt.io/en/Downloads.html) nella scheda "_Downloads_".

![VeraCrypt](assets/notext/05.webp)

Scarica la versione adatta al tuo sistema operativo. Se sei su Windows, scegli "_EXE Installer_".

![VeraCrypt](assets/notext/06.webp)

Scegli la lingua per la tua interfaccia.

![VeraCrypt](assets/notext/07.webp)

Accetta i termini della licenza.

![VeraCrypt](assets/notext/08.webp)

Seleziona "_Install_".

![VeraCrypt](assets/notext/09.webp)

Infine, scegli la cartella dove verrà installato il software, poi clicca sul pulsante "_Install_".

![VeraCrypt](assets/notext/10.webp)

Attendi il completamento dell'installazione.

![VeraCrypt](assets/notext/11.webp)

L'installazione è terminata.

![VeraCrypt](assets/notext/12.webp)

Se lo desideri, puoi fare una donazione in bitcoin per supportare lo sviluppo di questo strumento open-source.

![VeraCrypt](assets/notext/13.webp)


## Come criptare un dispositivo di memorizzazione con VeraCrypt?

Al primo avvio, arriverai a questa interfaccia:

![VeraCrypt](assets/notext/14.webp)

Per criptare il dispositivo di memorizzazione di tua scelta, inizia collegandolo alla tua macchina. Come vedrai più avanti, il processo di creazione di un nuovo volume criptato su una chiavetta USB o un disco rigido richiederà molto più tempo se il dispositivo contiene già dati che non desideri cancellare. Pertanto, ti raccomando di utilizzare una chiavetta USB vuota o di svuotare il dispositivo in anticipo per creare il volume criptato, al fine di risparmiare tempo.

Su VeraCrypt, clicca sulla scheda "_Volumes_".

![VeraCrypt](assets/notext/15.webp)

Poi sul menu "_Create New Volume..._".

![VeraCrypt](assets/notext/16.webp)

Nella nuova finestra che si apre, seleziona l'opzione "_Encrypt a non-system partition/drive_" e cliccate su "_Next_".

![VeraCrypt](assets/notext/17.webp)

Dovrai quindi scegliere tra "_Volume VeraCrypt standard_" e "_Volume VeraCrypt nascosto_". La prima opzione crea un volume crittografato standard sul tuo dispositivo. L'opzione "_Volume VeraCrypt nascost_" permette di creare un volume nascosto all'interno di un volume VeraCrypt standard. Questo metodo ti consente di negare l'esistenza di questo volume nascosto in caso di coercizione. Ad esempio, se qualcuno ti costringe fisicamente a decrittografare il tuo dispositivo, puoi decrittografare solo la parte standard per soddisfare l'aggressore senza rivelare la parte nascosta. Nel mio esempio, opterò per un volume standard.

![VeraCrypt](assets/notext/18.webp)

Nella pagina successiva, clicca sul pulsante "_Seleziona Dispositivo..._".

![VeraCrypt](assets/notext/19.webp)

Si apre una nuova finestra dove puoi selezionare la partizione del tuo dispositivo di archiviazione dall'elenco dei dischi disponibili sulla tua macchina. Normalmente, la partizione che desideri crittografare sarà elencata sotto una riga intitolata "*Disco Rimovibile N*". Dopo aver selezionato la partizione appropriata, clicca sul pulsante "*OK*".

![VeraCrypt](assets/notext/20.webp)

Il supporto selezionato appare nel riquadro. Ora puoi cliccare sul pulsante "*Avanti*".

![VeraCrypt](assets/notext/21.webp)

Successivamente, dovrai scegliere tra le opzioni "_Crea volume crittografato e formattalo_" o "_Crittografa partizione esistente_". Come accennato in precedenza, la prima opzione cancellerà definitivamente tutti i dati sulla tua chiavetta USB o disco rigido. Scegli questa opzione solo se il tuo dispositivo è vuoto; altrimenti, perderai tutti i dati contenuti. Se desideri mantenere i dati esistenti, puoi trasferirli temporaneamente altrove, scegliere "_Crea volume crittografato e formattalo_" per un processo più veloce che cancella tutto, o optare per "_Crittografa partizione esistente_". Quest'ultima opzione permette di crittografare il volume senza cancellare i dati già presenti, ma il processo sarà molto più lungo. Per questo esempio, dato che la mia chiavetta USB è vuota, seleziono "_Crea volume crittografato e formattalo_", l'opzione che cancella tutto.

![VeraCrypt](assets/notext/22.webp)

Successivamente, avrai l'opzione di scegliere l'algoritmo di crittografia e la funzione hash. A meno che tu non abbia esigenze specifiche, ti consiglio di mantenere le opzioni predefinite. Clicca su "*Avanti*" per continuare.

![VeraCrypt](assets/notext/23.webp)

Assicurati che la dimensione indicata per il tuo volume sia corretta, per crittografare l'intero spazio disponibile sulla chiavetta USB, e non solo una parte. Una volta verificato, clicca su "*Avanti*".

![VeraCrypt](assets/notext/24.webp)

A questo punto, dovrai impostare una password per crittografare e decrittografare il tuo dispositivo. È importante scegliere una password forte per impedire a un attaccante di decrittografare i tuoi contenuti con attacchi di forza bruta. La password dovrebbe essere casuale, il più lunga possibile e includere diversi tipi di caratteri. Ti consiglio di optare per una password casuale di almeno 20 caratteri che includa lettere minuscole, lettere maiuscole, numeri e simboli.

Ti consiglio anche di salvare la tua password in un gestore di password. Questo rende più facile l'accesso ed elimina il rischio di dimenticanza. Per il nostro caso specifico, un gestore di password è preferibile a un supporto cartaceo. Infatti, in caso di furto, anche se il tuo dispositivo di archiviazione potrebbe essere rubato, la password nel gestore non può essere trovata dall'attaccante, il che impedirà l'accesso ai dati. Al contrario, se il tuo gestore di password viene compromesso, l'accesso fisico al dispositivo è comunque necessario per sfruttare la password e accedere ai dati.

Per maggiori informazioni sulla gestione delle password, ti consiglio di scoprire questo altro tutorial completo:

https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Inserisci la tua password nei 2 campi designati, quindi clicca su "*Avanti*".

![VeraCrypt](assets/notext/25.webp)

VeraCrypt ti chiederà quindi se prevedi di memorizzare file più grandi di 4 GB nel volume crittografato. Questa domanda permette al software di selezionare il sistema di file più adatto. Generalmente, viene utilizzato il sistema FAT perché è compatibile con la maggior parte dei sistemi operativi, ma impone un limite massimo di dimensione del file di 4 GB. Se hai bisogno di gestire file più grandi, puoi optare per il sistema exFAT.

![VeraCrypt](assets/notext/26.webp)

Successivamente, raggiungerai una pagina che ti permette di generare una chiave casuale. Questa chiave è importante, poiché sarà utilizzata per crittografare e decrittografare i tuoi dati. Sarà memorizzata in una sezione specifica del tuo supporto, a sua volta protetta dalla password che hai precedentemente stabilito. Per generare una chiave di crittografia forte, VeraCrypt ha bisogno di entropia. Ecco perché il software ti chiede di muovere casualmente il mouse sulla finestra; questi movimenti sono poi utilizzati per generare la chiave. Continua a muovere il mouse fino a quando l'indicatore di entropia è completamente riempito. Poi, clicca su "_Formatta_" per iniziare a creare il volume crittografato.

![VeraCrypt](assets/notext/27.webp)

Attendi mentre viene eseguita la formattazione. Questo può richiedere molto tempo per volumi grandi.

![VeraCrypt](assets/notext/28.webp)

Riceverai quindi una conferma.

![VeraCrypt](assets/notext/29.webp)


## Come utilizzare un'unità crittografata con VeraCrypt?

Per ora, il tuo supporto è crittografato e quindi non puoi aprirlo. Per decrittografarlo, vai su VeraCrypt.

![VeraCrypt](assets/notext/30.webp)

Seleziona una lettera di unità dall'elenco. Ad esempio, ho scelto "_L:_".

![VeraCrypt](assets/notext/31.webp)

Clicca sul pulsante "_Seleziona Dispositivo..._".

![VeraCrypt](assets/notext/32.webp)

Dall'elenco di tutti i dischi sulla tua macchina, seleziona il volume crittografato sul tuo supporto, poi clicca sul pulsante "_OK_".

![VeraCrypt](assets/notext/33.webp)

Controlla che il tuo volume sia ben selezionato.

![VeraCrypt](assets/notext/34.webp)

Clicca sul pulsante "_Monta_".

![VeraCrypt](assets/notext/35.webp)

Inserisci la password scelta durante la creazione del volume, poi clicca su "_OK_".

![VeraCrypt](assets/notext/36.webp)

Puoi vedere che il tuo volume è ora decrittografato e accessibile sulla lettera di unità "_L:_".

![VeraCrypt](assets/notext/37.webp)

Per accedervi, apri l'esplora file e vai all'unità _*L:_" (o un'altra lettera a seconda di quella che hai scelto nei passaggi precedenti).

![VeraCrypt](assets/notext/38.webp)

Dopo aver aggiunto i tuoi file personali al supporto, per crittografare nuovamente il volume, basta cliccare sul pulsante "*Smonta*".

![VeraCrypt](assets/notext/39.webp)

Il tuo volume non appare più sotto la lettera "_L:_". È quindi crittografato nuovamente.

![VeraCrypt](assets/notext/40.webp)

Ora puoi rimuovere il tuo supporto di memorizzazione.

Congratulazioni, ora hai un supporto crittografato per memorizzare in sicurezza i tuoi dati personali, avendo così una strategia completa 3-2-1 in aggiunta alla copia sul tuo computer e alla tua soluzione di archiviazione online.
Se desideri supportare lo sviluppo di VeraCrypt, puoi anche effettuare una donazione in bitcoin [su questa pagina](https://veracrypt.io/en/Donation.html).

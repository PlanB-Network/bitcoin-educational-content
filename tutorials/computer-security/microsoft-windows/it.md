---
name: Windows 11
description: Installazione automatica di Microsoft Windows 11 tramite file di configurazione
---
![cover](assets/cover.webp)


In questa esercitazione scopriremo come installare automaticamente Windows 11 utilizzando un metodo diverso dal processo di installazione standard di Windows.


## Scarica!


La prima cosa di cui avrete bisogno è un file di installazione. Il luogo più sicuro e affidabile per scaricarlo è direttamente il sito ufficiale di Microsoft.


È sufficiente visitare il link fornito di seguito e seguire le istruzioni per scaricare il [file ISO di Windows 11](https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Una volta arrivati alla pagina di download, scorrete verso il basso fino alla sezione per scaricare il file ISO.


![Image](assets/en/01.webp)


e scegliete la versione corretta.


![Image](assets/en/03.webp)


Dopo aver selezionato Windows 11, fare clic sul pulsante Conferma.


In questa fase, potrebbero essere necessari alcuni secondi per elaborare la richiesta, dopodiché verrà visualizzata la seguente pagina:


![Image](assets/en/04.webp)


Dopo aver confermato la richiesta, è necessario scegliere la lingua preferita.


![Image](assets/en/05.webp)


Dopo aver selezionato la lingua e fatto clic sul pulsante Conferma, la richiesta verrà elaborata. Questa fase può richiedere alcuni secondi.


Una volta elaborata la richiesta, verrà visualizzata una pagina con il link per il download del file .iso. Fare clic sul pulsante Download 64-bit per avviare il download.


La dimensione del file è di circa 5,5 GB e il link generato sarà valido per 24 ore.


## Automazione!


In questa fase è necessario apportare modifiche all'installazione standard di Windows. In questa fase, utilizzando l'installazione non presidiata, determiniamo quali elementi verranno installati, senza che l'utente debba intervenire in seguito. Infatti, in questo metodo, si utilizza un file XML per configurare le fasi di installazione e i servizi installati in Windows. In altre parole, l'uso del file Unattended.xml crea un processo di automazione durante l'installazione, impedendo la necessità di selezionare più opzioni ed evitando i noiosi passaggi solitamente richiesti durante la configurazione. Si tratta di un metodo insolito ma standard, introdotto da Microsoft. Ulteriori informazioni sono disponibili su [sito web ufficiale di Microsoft](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


In Internet sono disponibili diversi strumenti per la generazione di file non presidiati. Alcuni di essi sono online, mentre altri sono offline. Uno degli strumenti online per la creazione di questo file è [questo sito web](https://schneegans.de/windows/unattend-generator). Dopo averlo aperto, viene presentata la seguente pagina:


![Image](assets/en/06.webp)


Come indicato all'inizio della pagina, questo metodo può essere usato per l'installazione di Windows 10 e 11. Nella prima fase si seleziona la lingua di Windows. Se si desidera aggiungere una seconda o addirittura una terza lingua all'elenco delle lingue del display e della tastiera di Windows, è possibile utilizzare la casella sottostante:


![Image](assets/en/07.webp)


Nella fase successiva, si seleziona la posizione desiderata.


![Image](assets/en/08.webp)


In questa fase, possiamo anche specificare l'architettura del processore del computer. In questa fase possiamo:

1. Decidere se ignorare le funzioni di sicurezza di Windows, come TPM e Secure Boot. La funzione Secure Boot garantisce che se i file fondamentali di Windows vengono manomessi durante il processo di avvio, il problema viene rilevato e ne viene impedita l'esecuzione. Questa funzione aiuta anche a proteggere il sistema dall'installazione di aggiornamenti dannosi su Windows. L'attivazione dell'opzione per bypassare queste funzioni è talvolta inevitabile su alcuni computer, soprattutto sui modelli più vecchi. Tuttavia, in genere si consiglia di mantenere abilitate funzioni come Secure Boot.

2. Ignora il requisito di una connessione a Internet per completare il processo. Questa opzione è utile nelle situazioni in cui non è disponibile una connessione LAN via cavo, perché nella maggior parte dei casi la scheda wireless non viene ancora riconosciuta durante l'installazione di Windows ed è necessario l'accesso a Internet via cavo. L'attivazione di questa opzione risolve i problemi legati a questo passaggio.


Nella fase successiva, è possibile scegliere un nome per il computer.


![Image](assets/en/09.webp)


Si può anche consentire a Windows di scegliere un nome per il sistema. In questa fase è possibile selezionare il tipo di Windows, se compresso o non compresso, oppure lasciare che sia Windows a determinare la versione appropriata in base alle specifiche del computer. In questa fase è possibile impostare anche il fuso orario.


Il passo successivo riguarda le impostazioni della partizione:


![Image](assets/en/10.webp)


In questa fase è possibile specificare il tipo di partizione per l'installazione di Windows e le impostazioni necessarie per l'installazione dell'ambiente di ripristino di Windows. Selezionando la prima opzione, la selezione e il partizionamento della partizione vengono rimandati al momento dell'installazione di Windows e, durante l'installazione, queste domande verranno poste come nel metodo di installazione normale.


In questo passaggio si seleziona la versione di Windows da installare:


![Image](assets/en/11.webp)


Se è disponibile un codice prodotto, è possibile inserirlo anche in questa fase.


Il passo successivo consiste nel configurare l'account di accesso a Windows:


![Image](assets/en/12.webp)


## Riunioni dei conti


In questa fase:


1. È possibile definire un nome e una password per l'account amministratore. È anche possibile creare più account utente o amministratore.

2. Qui si specifica l'account a cui accedere la prima volta dopo l'installazione di Windows. Le diverse opzioni per questa sezione sono mostrate nell'immagine.

3. Se non si desidera che venga creato alcun account, pulire tutti gli account e selezionare questa opzione. In questo caso, dopo l'installazione di Windows, si accederà automaticamente all'account Amministratore di Windows.


Il passo successivo consiste nel configurare le impostazioni della password e del file host:


![Image](assets/en/13.webp)


In questa fase si stabilisce se le password devono avere un periodo di scadenza. Inoltre, questa sezione include le impostazioni di sicurezza relative ai tentativi di accesso falliti, che possono essere attivate o disattivate in base alle proprie esigenze.


In fondo a questa sezione si trovano le impostazioni per la visualizzazione dei file. Nessuna di queste opzioni è disponibile durante l'installazione standard di Windows e deve essere configurata dopo l'installazione. Con il metodo di installazione non presidiata, invece, queste impostazioni sono facilmente accessibili.


Il passo successivo consiste nel configurare le impostazioni di sicurezza di Windows:


![Image](assets/en/14.webp)


## Impostazioni di sicurezza


In questa fase:


1. Windows Defender può essere attivato o disattivato. Questa funzione agisce come un software di sicurezza in Windows e aiuta a prevenire l'esecuzione di file dannosi, alcuni attacchi di rete e altro ancora.

2. Gli aggiornamenti automatici di Windows possono essere disattivati. Questa è una delle sfide più comuni che gli utenti di Windows devono affrontare!

3. Questa sezione consente di attivare o disattivare l'UAC (User Account Control). Questa funzione impedisce alle applicazioni sospette di essere eseguite con permessi elevati di lettura e scrittura.

4. Questa funzione viene utilizzata da Windows per rilevare il software potenzialmente dannoso.

5. Abilita o disabilita il supporto per i percorsi lunghi nelle applicazioni Windows, come PowerShell e altre.

6. Abilitare o disabilitare Desktop remoto per accedere al sistema da remoto.


A seconda della versione di Windows utilizzata, alcune di queste funzioni possono essere o meno supportate.


Il passo successivo consiste nel configurare le icone:


![Image](assets/en/15.webp)


In questa sezione:


1. Vengono elencate le icone del desktop, che possono essere aggiunte o rimosse a seconda delle necessità.

2. Sono elencate le icone del menu di avvio, che possono essere aggiunte o rimosse in base alle esigenze.

3. Questa sezione consente di configurare l'installazione o meno di strumenti legati alla virtualizzazione. Questa opzione è specifica di Windows 11 e non si applica a Windows 10.


La fase successiva prevede la configurazione delle impostazioni Wi-Fi:


![Image](assets/en/16.webp)


In questa sezione è possibile configurare le impostazioni di rete Wi-Fi. Come già detto, nella maggior parte dei casi la scheda Wi-Fi non viene riconosciuta durante l'installazione di Windows, quindi la connessione durante la configurazione non è solitamente possibile. Tuttavia, configurando questa sezione, se la scheda wireless viene riconosciuta, il sistema può connettersi a Internet.


Il passo successivo prevede un'impostazione importante:


![Image](assets/en/17.webp)


In questa sezione si specifica se le informazioni sui problemi del sistema devono essere inviate o meno a Microsoft.


La fase successiva prevede la configurazione delle applicazioni predefinite:


![Image](assets/en/18.webp)


## Abilitazione/disabilitazione software predefinita


In questa sezione è possibile scegliere le applicazioni che non si desidera vengano installate per impostazione predefinita. Ad esempio, possiamo scegliere di non installare Cortana o Copilot.


Il passo successivo riguarda le impostazioni di sicurezza relative all'esecuzione delle applicazioni:


![Image](assets/en/19.webp)


Applicando le impostazioni WDAC, è possibile impedire l'esecuzione di alcune applicazioni.


Infine, dopo aver applicato le impostazioni desiderate, è possibile scaricare il file XML generato:


![Image](assets/en/20.webp)


Facendo clic su Download XML File, viene scaricato il file autounattend.xml. Per utilizzare questo file, è sufficiente montare la ISO scaricata su un'unità USB, collocare il file autounattend.xml nella directory principale e procedere con l'installazione di Windows.


Uno degli strumenti disponibili per creare un'unità USB avviabile è Rufus. Rufus può creare una chiavetta di installazione di Windows avviabile, con un determinato file ISO di installazione di Windows. È semplice e veloce; potete scaricarlo [qui](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


In questo software, dopo aver selezionato l'unità USB desiderata e il file ISO appropriato, facciamo clic su Start.


![Image](assets/en/22.webp)


In questa fase, disabilitiamo tutte le opzioni, poiché la loro attivazione può causare conflitti quando si utilizza il file Unattend generato. Dopo aver copiato i file sull'unità USB, si posiziona il file autounattend.xml nella directory principale:


![Image](assets/en/23.webp)


A questo punto, l'unità USB è pronta per l'installazione automatica di Windows e l'installazione può essere avviata utilizzando questa unità.


## Modifica ISO


Se dovete installare Windows su una macchina virtuale, potete usare un software per creare e modificare i file ISO. Uno di questi software è AnyBurn. Dopo aver estratto il contenuto del file ISO scaricato dal sito web di Microsoft, collocate il file autounattend.xml nella directory principale. Quindi, utilizzando AnyBurn, creare una nuova ISO con i contenuti aggiornati.


AnyBurn è un software multifunzionale per lavorare con i file ISO. Offre diverse funzioni per la gestione dei file ISO, una delle quali è la creazione di immagini ISO avviabili; [qui](https://www.anyburn.com/download.php) è il sito web originale.


Nella pagina principale del software, selezionare "Crea immagine da file/cartella":


![Image](assets/en/24.webp)


Nella pagina successiva, selezionate tutti i file estratti dalla ISO e il file autounattend.xml.


![Image](assets/en/25.webp)


In questo passaggio si configurano le impostazioni per rendere avviabile il file ISO:


![Image](assets/en/26.webp)


In questa fase è necessario impostare il percorso del file bootfix.bin per rendere l'ISO avviabile. Questo file si trova nella radice della ISO, all'interno della cartella di avvio. Si consiglia inoltre di abilitare entrambe le opzioni ISO9660 e UDF nella sezione Proprietà.


![Image](assets/en/27.webp)


Dopo questo passaggio, facendo clic su Avanti si creerà il file ISO. Questo file può essere utilizzato in software di virtualizzazione come Oracle VirtualBox. Di seguito troverete un'esercitazione su VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
---
name: Whonix
description: Preservare la vostra privacy e riservatezza.
---

![cover](assets/cover.webp)



**Whonix** è una distribuzione Linux basata su **Debian**, progettata per fornire un ambiente che combini **sicurezza**, **anonimato** e **privacy**. Facile da imparare e compatibile con diverse interfacce (macchine virtuali, Qubes OS, modalità Live), include per impostazione predefinita l'instradamento del traffico di rete tramite **Tor**, un **doppio firewall** (un firewall sul Gateway e un altro sulla Workstation), una **protezione completa contro le fughe di IP/DNS** e strumenti per mascherare efficacemente la vostra attività dagli osservatori della rete, compreso il vostro ISP. Più che un semplice sistema anonimo, **Whonix** è un ambiente di sviluppo sicuro e completo.



## Perché scegliere Whonix?





- Gratuito**: Come la maggior parte delle distribuzioni Linux, Whonix è un sistema open-source con licenza completamente gratuita. È sviluppato in open source, con una comunità attiva e trasparente.
- Privacy, sicurezza e anonimato**: L'obiettivo principale di Whonix è offrire un ambiente ultra-sicuro, in cui tutti i dati sono protetti e le comunicazioni criptate attraverso la rete Tor.
- Facile da usare**: Whonix offre un Interface intuitivo e preconfigurato, adatto anche agli utenti meno esperti. Non è necessario essere esperti per beneficiare di una protezione avanzata.
- Ambiente ideale per lo sviluppo sicuro**: Whonix consente di sviluppare, testare, verificare o eseguire programmi senza mai rivelare il vostro vero IP Address o esporre le vostre abitudini di navigazione o di comunicazione in rete.
- Sessioni monouso e modalità Live**: Whonix può essere lanciato in modalità Live o tramite macchine usa e getta (ad esempio tramite **Qubes OS**), consentendo di eseguire attività critiche senza lasciare tracce persistenti una volta terminata la sessione.
- Installazione relativamente semplice**: Vengono fornite immagini pronte all'uso per una rapida installazione in macchine virtuali (VirtualBox, KVM, Qubes). Il sistema è documentato e regolarmente aggiornato.



## Installazione e configurazione



Prima di passare all'installazione di Whonix, è essenziale notare che questa distribuzione **non è ancora ufficialmente disponibile** come sistema principale che può essere installato direttamente sul disco Hard (in modalità bare metal). In altre parole, **non è ancora possibile installare Whonix come un classico sistema operativo ospite**, come Ubuntu o Debian standard.



Tuttavia, sono disponibili diverse edizioni che consentono di utilizzare Whonix in modo **volatile** (modalità Live, sessioni temporanee) o **persistente** (tramite macchine virtuali o integrazione in Qubes OS).



Per un uso stabile e a lungo termine, la **virtualizzazione è attualmente l'unico metodo ufficialmente consigliato**. È possibile eseguire Whonix utilizzando **VirtualBox** (Whonix-Gateway e Whonix-Workstation) o integrarlo in un sistema come **Qubes OS**. In questa guida ci concentreremo sull'installazione di VirtualBox.



### Prerequisiti



Prima di poter installare Whonix in modalità virtuale, assicuratevi che la vostra macchina soddisfi i requisiti tecnici minimi. La virtualizzazione richiede alcune risorse che non tutti i computer possono offrire. È quindi essenziale che il processore supporti la tecnologia di virtualizzazione (Intel VT-x o AMD-V) e che questa opzione sia abilitata nel BIOS/UEFI.



Ecco le specifiche consigliate per un'esperienza fluida e stabile con Whonix:





- Memoria ad accesso casuale (RAM)**: si consiglia vivamente un minimo di **8 GB**. Più RAM si ha, più risorse si possono allocare alle macchine virtuali (Gateway e Workstation), migliorando le prestazioni.
- Spazio disponibile su disco**: prevedere almeno 30 GB di spazio libero su disco**. Questo include lo spazio necessario per le due macchine virtuali, i file di sistema ed eventuali dati o snapshot.
- Processore**: si consiglia un processore con almeno **4 core fisici** (8 thread logici), soprattutto se si desidera eseguire altri servizi o strumenti in parallelo.



### Scaricare Whonix



Whonix è disponibile in diverse edizioni, a seconda del tipo di ambiente in cui si desidera utilizzarlo. Per la maggior parte degli utenti (Windows, Linux o MacOs), l'edizione VirtualBox è la più semplice da configurare. È possibile scaricare l'immagine direttamente da [il sito ufficiale](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **non è compatibile** con i MacBook che utilizzano processori Apple Silicon (architettura ARM).



## Installazione di VirtualBox



Per eseguire Whonix, è necessario un **hypervisor** come VirtualBox, Qubes o KVM.



Una volta scaricato il file, installatelo come fareste con qualsiasi altro software. Accettate le opzioni predefinite, a meno che non abbiate esigenze specifiche. Vi siete persi? Consultate la nostra guida all'uso di VirtualBox.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Importare Whonix



Una volta installato VirtualBox, è possibile importare i file `.ova' di Whonix scaricati in precedenza (`Whonix-Gateway-Xfce.ova' e `Whonix-Workstation-Xfce.ova').



Aprire VirtualBox, quindi fare clic su **File → Importa dispositivo**.


Selezionare il file `.ova' corrispondente (iniziare con il Gateway).



![0_03](assets/fr/03.webp)



Scegliere il percorso in cui verranno archiviati i file della macchina virtuale Whonix.



![0_04](assets/fr/04.webp)



Accettare le condizioni d'uso, quindi avviare l'importazione e attendere il completamento del processo.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Configurazione Whonix



Prima di avviare Whonix, è importante regolare alcune **impostazioni di sistema** per garantire prestazioni migliori:



Selezionare la macchina virtuale **Whonix-Workstation-Xfce**, quindi fare clic su **Configurazione**.



![0_06](assets/fr/07.webp)



Accedere alla scheda **Sistema**, dove l'allocazione predefinita della RAM è di 2048 MB. Si consiglia di **aumentarla a 4096 MB (4 GB)** per una maggiore fluidità, soprattutto se si intende aprire diverse applicazioni o lavorare in lunghe sessioni. Il Gateway può rimanere a 2048 MB, a meno che non si utilizzino molte connessioni Tor in parallelo.



![0_08](assets/fr/08.webp)



### Come iniziare con Whonix



Affinché Whonix funzioni in modo corretto e sicuro, **è necessario seguire questa sequenza di avvio**:



Per prima cosa, avviare la macchina **Whonix-Gateway-Xfce**. Questa macchina è responsabile dell'instradamento di tutto il traffico attraverso la rete **Tor**. Senza il gateway in esecuzione, nessun traffico verrà instradato attraverso Tor e si perderà l'anonimato.



![0_09](assets/fr/09.webp)



Una volta che il Gateway è completamente avviato (vedrete Tor connesso), potete avviare **Whonix-Workstation-Xfce**, che si connetterà automaticamente tramite il Gateway.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Aggiornamento del sistema



Nel terminale, inserite il seguente comando per aggiornare l'elenco dei pacchetti:



```shell
sudo apt update
```



Eseguire quindi il seguente comando per installare gli aggiornamenti disponibili:



```shell
sudo apt full-upgrade
```



## Scoprire Whonix



**Whonix** è un sistema progettato per fornire un ambiente informatico **sicuro**, **anonimo** e **confidenziale**, ideale per navigare in Internet senza compromettere la propria identità o i propri dati. A tal fine, viene fornito con una serie di utili applicazioni quotidiane progettate per rafforzare la vostra sicurezza digitale fin dall'inizio.


### KeepassXC



**KeePassXC** è il gestore di password integrato di Whonix. Consente di **creare, archiviare e gestire** le password in modo sicuro, senza doverle ricordare tutte manualmente. Le password sono memorizzate in un database **crittografato**, protetto da una password principale.



### Browser Tor



**Tor Browser** è il browser Web predefinito di Whonix. Si basa sulla rete **Tor**, che reindirizza il traffico dell'utente attraverso diversi relay in tutto il mondo, rendendo praticamente impossibile l'identificazione del vostro vero IP Address.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Elettro Bitcoin Wallet



**Electrum** è un Bitcoin Wallet leggero e veloce, preinstallato su Whonix per consentire di gestire le **transazioni di criptovaluta** in modo anonimo. Non scarica l'intero Blockchain ma utilizza server remoti per ottenere le informazioni necessarie, rendendolo molto più leggero di un Wallet completo.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix è più di un semplice sistema operativo: è un vero e proprio **ambiente sicuro** progettato per proteggere l'anonimato, la privacy e le attività sensibili. Grazie alla sua architettura basata su Tor, al partizionamento intelligente tra Gateway e Workstation e a strumenti preinstallati come Tor Browser, KeePassXC ed Electrum, offre una soluzione chiavi in mano a chiunque desideri **guidare in modo anonimo**, **lavorare in modo sicuro** o **gestire dati riservati**.



Per rafforzare la sicurezza del vostro sistema Unix, date un'occhiata al nostro tutorial sull'auditing del vostro computer: controllate le falle di sicurezza del vostro sistema operativo e assicuratevi che i vostri dati non siano compromessi.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af
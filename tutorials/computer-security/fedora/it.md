---
name: Fedora
description: La distribuzione Linux che offre uno spazio di lavoro gratuito, completo e sicuro.
---


![cover](assets/cover.webp)





Fedora è un sistema operativo libero e open-source basato su Linux lanciato nel 2003, sviluppato dalla comunità del **Fedora Project** e supportato da **Red Hat Linux**. È rinomato per la sua stabilità, le buone prestazioni e la facilità d'uso, che lo rendono una scelta eccellente sia per i principianti che per gli utenti avanzati. Il sistema funziona sulla maggior parte delle architetture di processore moderne, il che lo rende facile da installare praticamente su qualsiasi computer. Fedora è disponibile anche in diverse edizioni preconfigurate, chiamate "Fedora Spins" o "Fedora Editions", pensate per esigenze specifiche (videogiochi, astronomia, sviluppo...).



## Architettura di Fedora Linux



Come avete letto in precedenza, Fedora è un sistema operativo libero basato sul kernel Linux. Il kernel Linux è la parte del sistema operativo che comunica con l'hardware del computer e gestisce le risorse del sistema, come la memoria e la potenza di elaborazione.



Fedora Linux include una serie di strumenti e applicazioni software necessari per l'esecuzione del sistema operativo in cima al kernel Linux. L'architettura modulare di Fedora significa che consiste principalmente in un insieme di singoli componenti che possono essere facilmente aggiunti, rimossi o sostituiti a seconda delle necessità. Ciò consente di modellare il sistema operativo utilizzando solo le risorse necessarie.



Fedora include anche un ambiente desktop, che è il Interface attraverso il quale gli utenti eseguono le operazioni e accedono alle applicazioni. L'ambiente desktop predefinito di Fedora è GNOME, un ambiente desktop facile da usare e altamente personalizzabile.



## Perché scegliere Fedora?



Tra la moltitudine di distribuzioni Linux disponibili, Fedora si distingue in particolare per:





- Modularità**: Compatibile con diverse architetture di processore, Fedora può essere installato sulla maggior parte dei computer, anche quelli meno potenti, adattandosi perfettamente alle vostre esigenze.





- Un Interface semplice e intuitivo**: Fedora combina un moderno Interface grafico con un potente Interface a riga di comando, rendendolo facile da usare per tutti i profili.





- Stabilità del kernel**: Basata su Red Hat, Fedora è rinomata per l'affidabilità dei suoi aggiornamenti, in particolare quelli del kernel, che vengono eseguiti senza grossi bug grazie ai contributi gratuiti di un'ampia comunità.





- Installazione facile e veloce**: con un'immagine di soli 3 GB, l'installazione è facile e veloce, anche su macchine con risorse limitate.



## Edizioni Fedora



A seconda del profilo e dell'utilizzo, Fedora offre edizioni adatte alle vostre esigenze. Si trovano principalmente le edizioni:





- Fedora Workstation**: Ideale per l'uso personale e/o professionale sui vostri computer, questa edizione è installata con utility generiche come browser, una suite per ufficio (editor di testo) e software di riproduzione multimediale.





- Fedora Server**: Questa edizione è dedicata alla gestione dei server. Fedora Server include una serie di strumenti che aiutano a distribuire e gestire i server sulla propria scala.





- Fedora CoreOS**: Volete eseguire e distribuire facilmente applicazioni cloud? Fedora CoreOS è l'edizione che offre gli strumenti per creare e gestire immagini con Docker e Kubernet, ad esempio.



In questa guida ci occuperemo dell'edizione Fedora Workstation. Tuttavia, i processi descritti di seguito sono simili per le altre edizioni.



## Installazione e configurazione di Fedora Workstation



L'installazione di Fedora Workstation richiede la seguente configurazione hardware:




- Una chiave USB di almeno **8 GB** per avviare il sistema operativo.
- Almeno **40 GB di spazio libero** sul disco Hard del computer.
- 4 GB di RAM** per un'esperienza fluida.



### Scaricare Fedora Workstation



È possibile scaricare l'edizione [Fedora Workstation] (https://fedoraproject.org/fr/workstation/download) dal sito ufficiale del progetto Fedora. Selezionare la versione corrispondente all'architettura del processore (32-bit - 64-bit) e fare clic sull'icona **Download**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Creare una chiave USB avviabile



Per installare Fedora, è necessario creare una chiave USB avviabile utilizzando un software come [Balena Etcher](https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Una volta terminata l'installazione di Balena Etcher, aprire l'applicazione e selezionare l'immagine ISO di Fedora Workspace scaricata. Selezionare la chiave USB come supporto di destinazione e fare clic sul pulsante **Flash** per avviare la creazione della chiave avviabile.



![boot](assets/fr/05.webp)


### Installazione di Fedora



Al termine dell'avvio della chiave USB, spegnere il computer.


Accendere il computer, quindi accedere al BIOS durante l'avvio premendo il tasto `F2`, `F12` o `ESC`, a seconda del computer.



Nelle opzioni di avvio, selezionare la chiave USB come dispositivo di avvio primario. Confermando questa scelta, il computer si riavvierà e lancerà automaticamente il programma di installazione di Fedora** presente sulla chiave USB.



Una volta avviato il computer dalla chiavetta USB, viene visualizzata la schermata **GRUB**.



In questa fase sono disponibili le seguenti opzioni:




- Test media**: Questa opzione consente di verificare l'integrità della chiavetta USB e di assicurarsi che siano presenti tutte le dipendenze necessarie per una corretta installazione. Si tratta di una fase facoltativa, ma consigliata se si hanno dubbi sulla chiavetta USB.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Avvia Fedora**: Avvia Fedora in modalità "live", senza installazione.



Sul desktop di Fedora (modalità live), fare clic su **Installa Fedora** (o Installa su disco Hard) per avviare il processo di installazione. È possibile scegliere di installare in un secondo momento e provare Fedora senza doverlo installare.



![install-live](assets/fr/08.webp)



Il primo passo è quello di selezionare la **lingua di installazione** e il **display della tastiera** di Fedora



![language](assets/fr/10.webp)





- Selezione del disco di installazione:



Scegliere il disco Hard su cui si vuole installare Fedora.



Se il disco è vuoto, Fedora utilizzerà automaticamente tutto lo spazio disponibile. Altrimenti, è possibile personalizzare il partizionamento (manuale o automatico).



![disk](assets/fr/11.webp)





- Crittografia:



A questo punto, Fedora suggerisce di criptare il disco per aggiungere un ulteriore Layer di sicurezza. Questo assicura che i dati possano essere letti solo dal sistema Fedora.



![chiffrement](assets/fr/12.webp)



Prima di avviare l'installazione, Fedora visualizza un riepilogo delle scelte effettuate. Confermare e fare clic sul pulsante di installazione per avviare l'installazione di Fedora.



![resume](assets/fr/13.webp)



Durante l'installazione, Fedora copia i file e configura il sistema. Al termine, il computer si riavvia automaticamente.



![installation](assets/fr/14.webp)



### Configurazione di base


Al primo utilizzo, è necessario finalizzare alcune impostazioni:




- Se necessario, cambiare la lingua del sistema.



![language](assets/fr/15.webp)





- Selezionare un layout di tastiera adatto alle proprie preferenze.



![keyboard](assets/fr/16.webp)





- Scegliete il vostro fuso orario digitando il nome della vostra città nella barra di ricerca, quindi fate clic sul suggerimento corrispondente.



![timezone](assets/fr/17.webp)





 - Abilitate o disabilitate l'accesso alla vostra posizione per le applicazioni che lo richiedono, nonché l'invio automatico di segnalazioni di bug.



![location](assets/fr/18.webp)





- Decidete se volete abilitare i repository di software di terze parti.



![logs](assets/fr/19.webp)





- Inserite il vostro nome completo e definite un nome utente per il vostro account.



![name](assets/fr/20.webp)





- Creare una password sicura per la propria sessione: il più lunga possibile (minimo 20 caratteri), il più casuale possibile e con una varietà di caratteri (minuscole, maiuscole, numeri e simboli). Ricordarsi di salvare la password.



![mdp](assets/fr/21.webp)



Una volta completati tutti questi passaggi, lanciate Fedora e iniziate a usarlo immediatamente, senza ulteriori riavvii.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Una volta completata l'installazione, è possibile consultare il proprio Interface con alcune utility preinstallate.



![install-now](assets/fr/09.webp)



## Scoprite le attività di base



### Navigazione in Internet


Il browser predefinito di Fedora è **Firefox**. È facile da usare e adatto alla maggior parte delle esigenze.


Se preferite un altro browser, potete installarlo dal **software manager** o tramite il **terminale**.


### Elaborazione testi


Fedora include di default la suite per ufficio **LibreOffice**, che offre diversi strumenti utili:




- Writer** per l'elaborazione di testi.
- Calc** per i fogli di calcolo.
- Impress** per creare presentazioni.


## Installazione delle applicazioni


Per installare nuove applicazioni, si può usare il **gestore software** di Fedora (chiamato _Software_), che rende l'installazione facile e visiva.  Tuttavia, l'uso del **terminale** è spesso più veloce e preciso.



Prima di installare qualsiasi software, ricordatevi sempre di aggiornare i **repository** per assicurarvi di avere accesso alle ultime versioni disponibili.



Utilizzate quindi il seguente comando per avviare l'installazione dell'applicazione desiderata:


sudo dnf install software_name`


## Aggiornamento del sistema operativo


Dopo l'installazione, è importante aggiornare Fedora per usufruire delle ultime patch di sicurezza e degli aggiornamenti software.


### Opzione 1: Tramite grafica Interface




- Aprire Fedora **Impostazioni**, quindi andare alla sezione **Sistema**.
- Fare clic su **Aggiornamento software**.
- Avviare il download degli aggiornamenti e attendere il completamento del processo.



Una volta installati gli aggiornamenti, potrebbe essere necessario un **riavvio**.


### Opzione 2: via terminale




- Aprite un terminale e iniziate ad aggiornare i **repository** per assicurarvi di avere le ultime versioni di:



```shell
sudo dnf check-update
```





- Quindi, aggiornare tutto il software installato con il seguente comando:



```shell
sudo dnf upgrade
```



Ora il vostro sistema Fedora è aggiornato e pronto all'uso per tutte le vostre attività quotidiane. Scoprite il nostro tutorial su Linux Mint, un'altra distribuzione Linux, e come configurare un ambiente sano e sicuro per le vostre transazioni Bitcoin.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5
---
name: Debian
description: Una distribuzione Linux rinomata per la sua stabilità, robustezza e compatibilità.
---

![cover](assets/cover.webp)



Debian è una distribuzione GNU/Linux libera, rinomata per la sua robustezza e affidabilità. Il suo kernel Linux e tutti i suoi pacchetti sono rigorosamente testati per garantire una stabilità solida come una roccia e un alto livello di sicurezza. Adatta sia per i server che per le postazioni di lavoro, Debian offre un'esperienza facile da usare e un vasto catalogo di software. Se state cercando un sistema sicuro per l'uso quotidiano o per un ambiente di produzione, Debian è la scelta giusta.



## Perché scegliere Debian?





- Libera e aperta**: Debian è interamente open source, garantendo trasparenza e assenza di costi di licenza.
- Stabilità e sicurezza**: ogni release viene sottoposta a un accurato processo di test, che rende Debian una delle distribuzioni più affidabili e sicure sul mercato.
- Comunità attiva**: una vasta comunità e un'ampia documentazione sono disponibili per supportarvi ogni volta che ne avete bisogno.
- Leggero e scalabile**: è possibile installare Debian su macchine con risorse modeste mantenendo buone prestazioni.
- Ampio catalogo software**: oltre 50.000 pacchetti ufficiali sono disponibili nei repository.



## Scegliere una grafica Interface



Debian offre diversi ambienti desktop per soddisfare le vostre esigenze:





- GNOME**: Interface moderno e intuitivo, ideale per i principianti. Offre un menu grafico fluido e facile da usare per accedere alle applicazioni.
- XFCE**: leggero e veloce, perfetto per le macchine meno potenti.
- KDE Plasma**: altamente personalizzabile, con un aspetto simile a quello di Windows.
- Cinnamon**: Interface semplice ed elegante, ispirato a Windows.
- LXDE / LXQt**: ultraleggero, adatto ai computer più vecchi.
- MATE**: semplice e classico, vicino al vecchio GNOME.



💡 Per un'esperienza confortevole e facile da impugnare, si consiglia di utilizzare **GNOME**.



## Installazione e configurazione di Debian


### Requisiti hardware



Prima di iniziare l'installazione, accertarsi di disporre delle seguenti apparecchiature:





- Chiave USB**: 8 GB minimo per contenere l'immagine ISO avviabile.
- Memoria ad accesso casuale (RAM)**: 4 GB per un'installazione e un funzionamento senza problemi.
- Spazio su disco**: almeno 15 GB di spazio libero per il sistema e gli aggiornamenti.



### Scaricare



La scelta dell'immagine Debian dipende dall'architettura del processore:





- AMD64**: scaricare l'edizione "live hybrid" dall'elenco [download] (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: ottenere l'immagine del DVD dal sito ufficiale [Debian] (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Altre architetture**: trovare l'ISO corrispondente alla propria architettura [qui](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Creare una chiave USB avviabile



Una volta scaricata l'immagine ISO appropriata, procedere alla creazione del supporto di installazione:




- Scaricare Balena Etcher** dal [sito web ufficiale] (https://etcher.balena.io/), quindi ottenere il binario per il proprio sistema e installarlo.



![etcher](assets/fr/02.webp)





- Avviare Etcher**: aprire il software e selezionare l'immagine ISO di Debian scaricata in precedenza.
- Scegliere la chiave USB**: specificare la propria chiave (8 GB+) come destinazione.
- Avvia flash**: fare clic su **Flash!** e attendere il completamento del processo.



![flash](assets/fr/03.webp)



La chiave USB è ora pronta per iniziare l'installazione di Debian.



## Installazione di Debian sul sistema



### Avvio da chiave USB



Per avviare l'installazione dalla chiave USB:




- Spegnere** completamente il computer.
- Riavviare** quindi accedere al BIOS/UEFI premendo immediatamente `ESC`, `F2`, `F11` (o il tasto dedicato a seconda della marca).
- Nel menu di avvio, **selezionare la chiave USB** come dispositivo di avvio.
- Confermare** con il tasto Invio per avviare l'immagine Debian: questo vi porterà alla schermata di benvenuto dell'installatore.



### Avvio dell'installazione



Schermata iniziale:



![starting](assets/fr/04.webp)



Quando si avvia dalla chiavetta USB, la schermata di benvenuto di Debian offre diverse opzioni:




- Live System**: lancia Debian senza installarla, ideale per testare l'ambiente.
- Avvia installatore**: avvia l'installazione direttamente sul disco Hard.
- Opzioni di installazione avanzate**: consente di accedere a modalità di installazione personalizzate.



Per esplorare Debian in modalità live, selezionare **Live System** e confermare con **Enter**. È quindi possibile avviare l'installazione facendo clic su **Installa Debian** nell'ambiente live.



![system](assets/fr/05.webp)





- Selezione della lingua** (opzionale)



Selezionare la lingua principale del sistema Debian dall'elenco, quindi fare clic su OK.



![language](assets/fr/06.webp)





- Fuso orario** (GMT)



Scegliere la zona geografica per impostare automaticamente la data e l'ora.



![timezone](assets/fr/07.webp)





- Layout della tastiera



Selezionare la lingua e il layout della tastiera. Utilizzate il campo di prova incorporato per verificare che ogni tasto produca il carattere previsto.



![keyboard](assets/fr/08.webp)



### Partizionamento del disco





- Cancella disco**: se avete una partizione dedicata, questa opzione cancellerà tutto il suo contenuto.
- Partizionamento manuale**: scegliere questa opzione per creare, ridimensionare o eliminare le partizioni come richiesto.



![disk](assets/fr/09.webp)





- Creazione di un account utente



Inserite il vostro nome completo, il nome dell'account e una password forte per garantire la sicurezza della vostra sessione.



![user](assets/fr/10.webp)





- Sintesi dei parametri**



Viene visualizzato un riepilogo delle scelte effettuate: controllare ogni voce e tornare indietro per modificarla, se necessario.



![settings](assets/fr/11.webp)





- Avvio dell'installazione



Fare clic su **Install** per avviare la copia dei file e la configurazione del sistema, quindi attendere il completamento del processo.



![install](assets/fr/12.webp)





- Riavvio**



Una volta completata l'installazione, riavviare il computer per applicare tutte le configurazioni e accedere al nuovo sistema Debian.



![restart](assets/fr/13.webp)



All'avvio, inserire il nome utente e la password per accedere al sistema.



![login](assets/fr/14.webp)



## Aggiornamento del sistema



Prima di iniziare a utilizzare il sistema, è essenziale aggiornarlo. Ciò consente di beneficiare delle ultime patch software, dei repository aggiornati e, in alcuni casi, delle patch di sicurezza per il sistema operativo stesso.



### Opzione 1: Aggiornamento tramite Interface grafico (GNOME)



Se si è installata Debian con l'ambiente desktop GNOME, è possibile eseguire gli aggiornamenti graficamente. Per farlo, aprire l'applicazione **Software**, quindi andare alla scheda **Aggiornamenti**. Cliccare quindi su **Riavvia e aggiorna** per avviare il processo.



### Opzione 2: Aggiornamento tramite terminale (consigliato)



Questo metodo offre un controllo più completo. Permette di aggiornare i repository, i pacchetti software e, se necessario, il kernel.




- Aprire il terminale utilizzando la scorciatoia `Ctrl + Alt + T`.
- Aggiornate l'elenco dei pacchetti disponibili con il seguente comando:



```shell
sudo apt update
```



Quando viene richiesto, inserire la password (si noti che durante la digitazione non viene visualizzato alcun carattere: è normale).





- Per installare gli aggiornamenti disponibili:



```shell
sudo apt full-upgrade
```



## Scoprite le attività di base



### Navigazione in Internet



Il browser web predefinito su Debian è **Firefox**. Se si preferisce un altro browser, è possibile installarne un altro, purché sia disponibile nei repository Debian (come Chromium, Brave...).



### Elaborazione testi



La suite **LibreOffice** è installata di default su Debian.





- Per scrivere documenti, utilizzare **LibreOffice Writer**, l'equivalente di Microsoft Word.
- Per i fogli di calcolo, **LibreOffice Calc** è un'alternativa a Excel.
- Infine, **LibreOffice Impress** consente di creare presentazioni, proprio come PowerPoint.



## Installazione delle applicazioni



Ci sono due modi per installare le applicazioni su Debian:



### Metodo grafico:



È possibile utilizzare il **software manager** (accessibile tramite il Interface grafico) per cercare e installare facilmente le applicazioni.



### Metodo a riga di comando:



Se l'applicazione che state cercando non appare nel Interface grafico o se preferite il terminale, usate il seguente comando:



```shell
sudo apt install <name>
```



Sostituire `<nome>` con il nome del pacchetto. Ad esempio, per installare `curl`:



```shell
sudo apt install curl
```



### Installazione di un pacchetto scaricato manualmente:



Se avete scaricato un file `.deb' (pacchetto Debian), potete installarlo con il seguente comando:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Il sistema Debian è ora installato e pronto per essere utilizzato per le attività quotidiane.


Grazie all'ambiente desktop **GNOME**, è possibile accedere a un'ampia gamma di applicazioni tramite un Interface grafico di facile utilizzo, ideale sia per i principianti che per gli utenti avanzati.



È anche possibile cambiare l'ambiente desktop (ad esempio XFCE, KDE, ecc.) senza dover reinstallare Debian. Per farlo, basta usare il terminale e installare il nuovo ambiente scelto.



Per saperne di più su Debian, e più in generale sulle distribuzioni GNU/Linux, vi consiglio di consultare questo corso:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
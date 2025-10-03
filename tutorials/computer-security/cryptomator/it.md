---
name: Cryptomator
description: Crittografia dei file nel cloud
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Florian BURNEL pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale.*



___



## I. Presentazione



In questa esercitazione utilizzeremo l'applicazione Cryptomator per crittografare i dati archiviati nel Cloud, sia su Microsoft OneDrive, Google Drive, Dropbox, Box o anche iCloud.



La crittografia dei dati archiviati su soluzioni di archiviazione online come Drive è il modo migliore per proteggere i vostri file e la vostra privacy. Grazie alla crittografia, siete gli unici a poter decifrare e leggere i vostri dati, anche se sono archiviati su un server negli Stati Uniti o in un altro Paese del mondo.



In questa dimostrazione verrà utilizzato un computer Windows 11 22H2 con OneDrive, ma la procedura è identica su altre versioni di Windows e altri servizi di archiviazione. È sufficiente installare il client di sincronizzazione e aggiungere il proprio account. In questo modo Cryptomator potrà memorizzare i propri dati nel caveau.



![Image](assets/fr/020.webp)



Cryptomator è un'alternativa ad altre applicazioni, in particolare Picocrypt presentato in un altro articolo, che ha un aspetto diverso, ma è altrettanto semplice da usare. Cryptomator è anche **open source**, conforme a RGPD e **codifica i dati con l'algoritmo di crittografia AES-256 bit**. Picocrypt, invece, si affida al più veloce algoritmo XChaCha20 (anch'esso a 256 bit).



https://planb.network/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

L'applicazione Cryptomator è disponibile su **Windows** (exe / msi), **Linux**, **macOS,** ma anche **Android** e **iOS**. Tra l'altro, tutte le applicazioni sono gratuite, tranne quella per Android, che è a pagamento (14,99 euro).



Sul vostro computer, **Cryptomator creerà una cartella all'interno della quale creerà una cassaforte**. All'interno della cassaforte, che può essere memorizzata su OneDrive, Google Drive o simili, i dati saranno crittografati. Quindi, se si archiviano tutti i dati nella cassaforte ospitata sul proprio spazio di archiviazione Drive, questi saranno protetti (perché crittografati).



**Nota**: in questo articolo vengono utilizzati come esempio i servizi di archiviazione online, ma Cryptomator può essere utilizzato per crittografare i dati su un disco locale, un disco esterno o persino un NAS. Non ci sono restrizioni, infatti.



## II. Installazione di Cryptomator



Per iniziare, è necessario **scaricare** e **installare** **Cryptomator**. Una volta completato il download, bastano pochi clic per completare l'installazione. Come [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), Cryptomator si affida a WinFsp per **montare un'unità virtuale sulla macchina Windows**.





- [Scarica Cryptomator dal sito ufficiale](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Utilizzo di Cryptomator su Windows



### A. Creare una nuova cassaforte



Per creare una nuova cassaforte, fare clic sul pulsante "**Aggiungi**" e selezionare "**Nuova cassaforte...**". Le casseforti esistenti e conosciute su questa macchina appariranno in Interface, sulla sinistra. **Una cassaforte creata sulla macchina A può essere aperta e modificata sulla macchina B**, a condizione che questa sia dotata di Cryptomator (e che la chiave di crittografia sia nota).



![Image](assets/fr/015.webp)



Iniziate dando un nome al vault, ad esempio "**IT-Connect**". In questo modo verrà creata una directory denominata "**IT-Connect**" nel mio OneDrive.



![Image](assets/fr/011.webp)



Nella fase successiva, Cryptomator probabilmente **rileverà il "Drive "** presente sul vostro computer: Google Drive, OneDrive, Dropbox, ecc.... Per consentirvi di selezionare direttamente il provider. Ho provato su due diversi computer Windows 11, con diverse unità, e non è stato rilevato. Non è un problema, basta definire una "**Collocazione personalizzata**" e selezionare la radice dello spazio di archiviazione. Ad esempio: **C:\Users\<Username>\OneDrive**.



![Image](assets/fr/018.webp)



Successivamente, è possibile regolare un'opzione in Impostazioni esperto.



![Image](assets/fr/021.webp)



Successivamente, è necessario definire **una password corrispondente alla chiave di crittografia**. Questa password vi permetterà di **sbloccare la vostra cassaforte Cryptomator** e di accedere ai suoi dati. **Se la perdete, perdete l'accesso ai vostri dati**. Infine, avete ancora la possibilità di **creare una chiave di backup** selezionando l'opzione "**Sì, meglio prevenire che curare**", nello stesso spirito della chiave di ripristino [BitLocker] (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). È consigliabile, ma non memorizzate la chiave di backup nella root di OneDrive!



Fare clic su "**Crea una cassaforte**".



![Image](assets/fr/019.webp)



Copiate la chiave di recupero e memorizzatela nel vostro password manager preferito. Fare clic su "**Avanti**".



![Image](assets/fr/013.webp)



Ecco fatto, il vostro nuovo baule è stato creato ed è pronto all'uso!



![Image](assets/fr/014.webp)



### B. Figure di accesso



Per accedere a una cassaforte e ai suoi dati, sia per **leggere i dati esistenti che per aggiungerne di nuovi**, è necessario **sbloccarla**. Cryptomator elenca le casseforti conosciute: la cassaforte IT-Connect appare, quindi è sufficiente selezionarla e cliccare su "**Sblocca**".



![Image](assets/fr/016.webp)



Per sbloccare la cassaforte è necessario inserire la password. Quindi fare clic su "**Release drive**".



![Image](assets/fr/022.webp)



**Questa unità, che in questo caso eredita la lettera E, consente di accedere ai dati (in chiaro, poiché la cassaforte è sbloccata).**



![Image](assets/fr/017.webp)



Sul lato OneDrive, non possiamo sfogliare direttamente il vault di Cryptomator. Non possiamo vedere i dati (né i nomi dei file né i contenuti). Questo significa che non è necessario aggiungere i dati al vostro caveau Cryptomator tramite la solita scorciatoia di OneDrive. **Dovete aggiungere i vostri dati utilizzando l'unità virtuale di Cryptomator.**



![Image](assets/fr/012.webp)



### C. Opzioni del tronco



Le impostazioni della cassaforte sono accessibili tramite il pulsante "**Opzioni volume crittografato**" (quando è bloccata) e abilitano il blocco automatico in caso di inattività, proprio come avviene per la cassaforte con password. L'opzione "**Sblocca volume crittografato all'avvio**", come suggerisce il nome, sblocca l'unità senza alcun intervento da parte dell'utente e monta l'unità virtuale. Per motivi di sicurezza, è meglio evitare di attivare questa opzione.



Tramite la scheda "**Montaggio**" si può anche decidere di montarlo in sola lettura o di assegnargli una lettera specifica.



![Image](assets/fr/024.webp)



Inoltre, nelle impostazioni di Cryptomator, è possibile **abilitare l'avvio automatico dell'applicazione**.



## IV. Conclusione



Con **Cryptomator**, è possibile **creare una cassaforte crittografata** in pochi minuti per proteggere i dati che si desidera archiviare su OneDrive e simili. È molto facile da usare quando si tratta di "accoppiarlo" con un'unità: a questo scopo, è da preferire a Picocrypt.
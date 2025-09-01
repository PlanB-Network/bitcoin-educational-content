---
name: Scanner IP arrabbiato
description: Un modo semplice per scansionare la rete
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Florian BURNEL pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale



___



## I. Presentazione



Come si fa a scansionare una rete Windows alla ricerca di macchine connesse in modo semplice e veloce? La risposta è Angry IP Scanner. Questo progetto open source consente di scansionare una rete in modo semplice, utilizzando un Interface grafico facile da usare.



Questo strumento può essere utilizzato da singoli individui per **scansionare la propria rete locale**, ma anche da professionisti IT per lo stesso scopo. A riprova del fatto che **questo strumento è molto pratico**, è già stato utilizzato da **alcuni gruppi di criminali informatici** per scansionare le reti aziendali (allo stesso modo di Nmap). Un buon esempio è [il gruppo di ransomware RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Si tratta comunque di un software valido, ma come per altri strumenti orientati alla rete e alla sicurezza, il suo uso può essere abusato.



Qui lo utilizzeremo su **Windows 11**, ma è perfettamente possibile utilizzarlo su altre versioni di **Windows**, nonché su **Linux** e **macOS**.



Meno completo di Nmap, **Angry IP** Scanner è comunque interessante per una rapida analisi di base della rete, ma anche perché è alla portata di tutti. Rileva gli host connessi alla rete** e identifica i **nomi degli host** e le **porte aperte**.



Se volete approfondire, consultate il tutorial su Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Come iniziare con Angry IP Scanner



### A. Scaricare e installare Angry IP Scanner



È possibile scaricare l'ultima versione di Angry IP Scanner dal sito web ufficiale dell'applicazione o da GitHub. Noi utilizzeremo quest'ultima opzione. Fate clic sul link sottostante e scaricate la versione EXE: "**ipscan-3.9.1-setup.exe**".





- [Scanner IP arrabbiato GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Eseguire l'eseguibile per procedere con l'installazione. Non c'è nulla di particolare da fare durante l'installazione.



![Image](assets/fr/013.webp)



### B. Eseguire una scansione iniziale della rete



Al primo avvio, leggere le istruzioni della finestra "**Inizio**" per saperne di più sul funzionamento dello strumento. A proposito, ci sono diversi termini da considerare:





- Feeder**: modulo responsabile della generazione di elenchi di indirizzi IP da scansionare, a partire da un intervallo IP casuale o da un file con un elenco di indirizzi IP.
- Fetcher**: un insieme di moduli per il recupero di informazioni sugli host della rete. Esistono, ad esempio, fetcher per rilevare gli indirizzi MAC, scansionare le porte, rilevare i nomi degli host o inviare richieste HTTP.



![Image](assets/fr/018.webp)



Per eseguire la scansione di una sottorete IP, è sufficiente inserire il **PI iniziale Address** e il **PI finale Address** nel campo "**intervallo IP**" (altrimenti, modificare il tipo sulla destra). Quindi fare clic sul pulsante "**Avvio**".



![Image](assets/fr/019.webp)



Poche decine di secondi dopo, il risultato sarà visibile nel Interface del software. **Per ogni IP Address nell'intervallo analizzato, si vedrà se Angry IP Scanner ha rilevato un host o meno.** Sullo schermo apparirà anche un riepilogo che indica il numero di host attivi (in questo caso 6) e il numero di host con porte aperte.



![Image](assets/fr/020.webp)



Qui si può notare la presenza di un host denominato "**OPNsense.local.domain**", associato all'IP Address "**192.168.10.1**" e accessibile sulle **porte 80** e **443** (HTTP e HTTPS). Facendo clic con il tasto destro del mouse sull'host si accede ad altri comandi, come il ping, il trace route e l'apertura del browser tramite questo IP Address.



![Image](assets/fr/012.webp)



### C. Aggiungere porte di scansione



Per impostazione predefinita, **Angry IP Scanner** esegue la scansione di 3 porte: **80** (HTTP), **443** (HTTPS) e **8080**. È possibile aggiungere altre porte da scansionare dalle preferenze dell'applicazione. Fare clic sul menu "**Strumenti**", quindi sulla scheda "**Porte**".



Qui è possibile modificare l'elenco delle porte tramite l'opzione "**Selezione porta**". È possibile **indicare numeri di porta specifici separati da una virgola o intervalli di porte**. L'esempio seguente aggiunge due porte: **445** (SMB) e **389** (LDAP). Per eseguire la scansione delle porte da 1 a 1000, inserire "**1-1000**". Non è specificato se la scansione delle porte viene eseguita in TCP, UDP o in entrambi.



![Image](assets/fr/021.webp)



Se si esegue nuovamente la scansione, è probabile che si ottengano nuove informazioni. Nell'esempio seguente, Angry IP Scanner mi dice che le porte 389 e 445 sono aperte sugli host "**SRV-ADDS-01**" e "**SRV-ADDS-02**", grazie alla nuova configurazione delle porte da scansionare.



![Image](assets/fr/022.webp)



**Nota**: dal menu "**Scanner**" è possibile esportare i risultati della scansione in un file di testo.



Se si desidera approfondire la scansione, fare clic sul menu "**Strumenti**", quindi su "**Cercatori**". In questo modo si aggiungono "funzionalità" alla scansione. È sufficiente selezionare un fetcher e spostarlo a sinistra per attivarlo. In questo modo si aggiungerà una colonna in più al risultato della scansione.



![Image](assets/fr/014.webp)



L'esempio seguente mostra le funzioni "**NetBIOS info**" e "**Rilevamento web**". La prima fornisce informazioni aggiuntive come il MAC Address e il nome di dominio della macchina, mentre la seconda visualizza il titolo della pagina web (che può dare qualche indicazione sul tipo di server web o di applicazione).



![Image](assets/fr/011.webp)



Infine, dalle preferenze è possibile modificare il metodo utilizzato per il "**ping**", ossia per valutare se un host è attivo o meno. Poiché alcuni host non rispondono ai ping, è possibile provare altri metodi (pacchetto UDP, sonda della porta TCP, ARP, combinazione UDP + TCP, ecc.)



## III. Conclusione



Semplice ed efficace: Angry IP Scanner rileva gli host connessi a una rete e consente di configurare la scansione delle porte. In termini di opzioni, non è flessibile come Nmap e non va così lontano, ma è un buon inizio per una scansione rapida.



Se si desidera utilizzare **Nmap** con un Interface grafico, è possibile utilizzare **l'applicazione Zenmap** (vedi panoramica sotto).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d
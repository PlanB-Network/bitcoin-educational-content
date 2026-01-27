---
name: Satodime
description: Scopri come utilizzare il Satodime con l'applicazione mobile
---
![cover](assets/cover.webp)



Questa guida illustra l'installazione, la configurazione e l'utilizzo dell'applicazione mobile Satodime. Imparerete a prendere possesso della vostra carta, a creare casseforti, ad aggiungere fondi, a sbloccare e recuperare le vostre chiavi private. Le appendici forniscono risorse, best practice e spiegazioni tecniche.



## Introduzione



**Satodime**, sviluppato da **[Satochip](https://satochip.io/fr/)**, è una carta al portatore sicura per memorizzare Bitcoin in modo tangibile e semplice. Funziona come un hardware wallet auto-custode, dove si ha il pieno controllo delle proprie chiavi private senza dipendere da terzi. Open-source e certificata EAL6+, supporta fino a tre casseforti indipendenti.



### Sfondo del prodotto



Satodime, una **carte au porteur, appartiene a chiunque la possieda fisicamente**, senza necessità di registrazione o identificazione preventiva. Risponde all'esigenza di un deposito di bitcoin sicuro e portatile, consentendo a chiunque sia in possesso della carta di utilizzarla o di trasferire bitcoin scansionandola tramite l'app mobile per prendere possesso o aprire casseforti. A differenza di una banconota cartacea, utilizza un chip sicuro per sigillare le chiavi private, che vengono rivelate solo dopo l'apertura, rendendo la carta simile ai contanti, dove la proprietà è determinata dal possesso fisico. Ideale per regalare bitcoin, facilita il trasferimento sicuro di bitcoin da una mano all'altra, mentre l'applicazione mobile sfrutta l'NFC per un'interazione accessibile con lo smartphone.





- Sicurezza**: Chiavi private generate e memorizzate nel chip a prova di manomissione; stato visibile (sigillato, non sigillato, vuoto).
- Caratteristiche**: Acquistare bitcoin direttamente tramite l'app (partner Paybis); gestire Mainnet e Testnet.
- Open-source**: Codice sotto licenza AGPLv3, verificabile su GitHub.



### Evoluzione continua



L'applicazione si evolve regolarmente. Controllare il sito web di Satochip o i negozi per gli aggiornamenti. Ad esempio, possono essere aggiunte nuove blockchain o funzionalità di acquisto. Controllare [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) per gli sviluppi in corso.



## 1. Prerequisiti



Prima di iniziare a utilizzare **Satodime**, assicuratevi di disporre dei seguenti elementi:





- Smartphone compatibile**: Dispositivo Android o iOS con NFC abilitato.
- Scheda Satodime**: Nuova o non inizializzata.
- Connessione a Internet**: Per scaricare l'applicazione.
- Conoscenze di base**: Comprensione delle chiavi private/pubbliche e dei rischi di perdita (irreversibile).
- Supporto sicuro**: Un luogo sicuro in cui registrare le chiavi private una volta non sigillate (carta, metallo; mai digitale).



## 2. Installazione





- Scarica la domanda** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Controllare lo sviluppatore (Satochip) per evitare frodi.
 - Satodime è **open-source**. Codice sorgente : [GitHub di Satochip](https://github.com/Toporin/Satodime-Applet).





- Installare e avviare l'applicazione**: Attivare l'NFC sul telefono, se necessario.



![image](assets/fr/01.webp)



## 3. Configurazione iniziale



### 3.1 Avviare l'applicazione e scansionare



Aprire l'app e seguire la procedura guidata. Posizionare la scheda Satodime sul lettore NFC del telefono (solitamente sul retro). Tenetela premuta per tutta la durata dell'operazione per garantire una connessione stabile.





- Se l'NFC non funziona, controllate le impostazioni del telefono.
- Un brindisi conferma il successo: "Lettura riuscita".



![image](assets/fr/02.webp)



Come regola generale, **tutte le seguenti operazioni richiedono una conferma tramite scansione della carta Satodime**



### 3.2 Presa di possesso della carta (*Ownership*)



Per il primo utilizzo, diventare il proprietario della carta per assicurarla:





- Fare clic su "*Prendere Ownership*" nell'applicazione.
- Confermare l'operazione: in questo modo si genera una chiave proprietaria unica.
- Eseguire nuovamente la scansione della mappa per applicare le modifiche.
- Attenzione**: Questo passaggio è irreversibile. Consultare [l'articolo sulla *proprietà*](https://satochip.io/satodime-ownership-explained/).



![image](assets/fr/03.webp)




## 4. Creare un ambiente sicuro



Satodime supporta fino a 3 casseforti. Createne una per conservare i bitcoin:





- Selezionare una cassaforte vuota (ad es. Cassaforte 01).
- Selezionare blockchain (Bitcoin).
- Fare clic su "*Crea & Seal*".
- Eseguire la scansione della carta su generate e sigillare la chiave privata (sconosciuta fino a quando non è stata sigillata).
- Congratulazioni**: La vostra cassaforte è ora sigillata e pronta a ricevere fondi.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Aggiungere fondi



Una volta sigillata, caricare la cassaforte con i bitcoin:





- Selezionare la cassaforte.
- Cliccate su "*Aggiungi fondi*".
- Copiare l'indirizzo pubblico o scansionare il codice QR.
- Inviare fondi da un altro wallet.
- Controllare il saldo dopo la conferma sulla blockchain.
- Opzione di acquisto: Cliccare su "*Acquista*" per acquistare direttamente tramite Paybis (Visa, Mastercard, ecc.). Tasse applicabili.



![image](assets/fr/06.webp)



## 6. Scomporre una cassaforte



Per accedere alla chiave privata e trasferire i fondi altrove, è necessario aprire la cassaforte:





- Selezionare la cassaforte sigillata.
- Cliccare su "Unseal".
- Confermare l'avvertenza: questa operazione è irreversibile.
- Scansionare la carta per aprirla.
- La cassaforte è impostata su "*Non sigillata*"; la chiave privata può ora essere visualizzata/esportata.
- Attenzione**: Una volta aperta, la chiave privata è accessibile. Se qualcuno entra in possesso del vostro smartphone, può accedere a questa chiave e quindi recuperare i fondi contenuti nella vostra cassaforte (in modo irreversibile).



![image](assets/fr/07.webp)



## 7. Recuperare la chiave privata



Dopo aver tolto il sigillo, esportare la chiave per utilizzarla in un altro wallet :





- Assicuratevi di essere in un ambiente sicuro.
- Cliccate su "*Mostra chiave privata*".
- Scegliere il formato: Legacy, SegWit, WIF, ecc.
- Copiare la chiave o scansionare il codice QR.
- Sicurezza**: Non condividete mai la vostra chiave privata. Conservatela offline.
- Importarlo in un programma software wallet compatibile con la gestione dei fondi (Sparrow Wallet o Electrum, ad esempio).



![image](assets/fr/08.webp)





## 8. Azzeramento del tronco



La reimpostazione della cassaforte cancella irreversibilmente la chiave privata associata. In altre parole, se non avete protetto una copia della vostra chiave privata, o se non l'avete importata in un altro wallet, il reset della cassaforte causerà la perdita irreversibile dei fondi in essa contenuti.



![image](assets/fr/09.webp)



Il reset del tronco rende lo slot vuoto e pronto per un nuovo tronco.



## 9. Trasferimento di proprietà



Per offrire bitcoin attraverso Satodime, ad esempio, è necessario :




- Prendete possesso della carta,
- Creare una cassaforte Bitcoin,
- Trasferitevi lì,
- Trasferimento della proprietà della carta: la persona successiva che scansiona la carta ne diventa proprietaria,
- Consegnate la carta Satodime a una persona di vostra scelta, invitandola a scaricare l'applicazione e a scansionare la carta per prenderne possesso e quindi accedere ai bitcoin "memorizzati" su di essa.



![image](assets/fr/10.webp)




## APPENDICI



### A1. Le migliori pratiche



Per utilizzare **Satodime** in modo sicuro :





- Proteggere la carta**: Trattatela come un contante; perdita = perdita di fondi se non del proprietario.
- Backup delle chiavi**: Dopo aver tolto il sigillo, registrare le chiavi private su un supporto fisico sicuro. Mai in formato digitale.
- Controllare lo stato**: Eseguire sempre una scansione per confermare la proprietà della carta e lo stato sigillato/non sigillato delle casseforti.
- Riservatezza**: Utilizzare nuovi indirizzi; evitare scambi centralizzati per i trasferimenti.
- Aggiornamenti**: Mantenere l'app aggiornata tramite gli store.
- Recupero**: Se la carta viene smarrita ma è di proprietà, i fondi sono sulla blockchain; utilizzare la chiave privata se non è sigillata.



### A2. Risorse aggiuntive



Specifico per Satodime :




- [Prodotto Satodime](https://satochip.io/fr/product/satodime/)
- [Guida mobile](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Academy](https://planb.academy/) per esercitazioni su autocustodia, chiavi private, ecc.



**Salva la tua frase di recupero** :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tutorial sul Satochip (il primo prodotto della marca) :**



https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Tutorial per custodi di semi:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Informazioni su Satochip



**Link ufficiali** :




- [Sito Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Supporto: info@satochip.io



**Satochip** è un'azienda belga che sviluppa soluzioni hardware e software per la gestione e l'archiviazione di bitcoin e altre criptovalute. Il suo prodotto di punta, l'hardware wallet di Satochip, è una carta NFC dotata di un secure element certificato EAL6+. Completato dal Seedkeeper, un gestore di frasi mnemoniche e segreti, e dal Satodime, una carta al portatore, Satochip offre una gamma completa e adatta alle esigenze degli utenti. I suoi dispositivi, alimentati da software open source, mirano a democratizzare la sicurezza su Bitcoin.
---
name: Dana Wallet
description: Portafoglio minimalista per pagamenti silenziosi (BIP-352)
---

![cover](assets/cover.webp)



Il riutilizzo degli indirizzi Bitcoin è una delle minacce più dirette alla riservatezza degli utenti. Quando un beneficiario condivide un unico indirizzo per ricevere più pagamenti, qualsiasi osservatore può tracciare tutte le transazioni associate e ricostruire la sua storia finanziaria. Questo problema riguarda in particolare i creatori di contenuti, gli enti di beneficenza o gli attivisti che desiderano mostrare pubblicamente l'indirizzo di una donazione senza compromettere la loro privacy o quella dei loro donatori.



Dana Wallet risponde a questo problema con una soluzione elegante: Silent Payments. Questo wallet minimalista e open-source, lanciato nel 2024, genera un indirizzo statico riutilizzabile e garantisce che ogni pagamento ricevuto finisca su un indirizzo separato della blockchain. Il mittente non ha bisogno di alcuna interazione preliminare con il destinatario e nessun osservatore esterno può collegare tra loro le singole transazioni. Sulla blockchain, questi pagamenti appaiono come transazioni Taproot perfettamente ordinarie.



Dana Wallet è disponibile su Mainnet e Signet, ma gli sviluppatori la considerano ancora sperimentale e raccomandano di non depositare fondi che non si è disposti a perdere. In questo tutorial, utilizzeremo la versione Signet per scoprire Silent Payments senza rischiare fondi reali.



## Che cos'è Dana Wallet?



### Filosofia e obiettivi



Dana Wallet adotta un approccio "SP-first": il wallet genera esclusivamente indirizzi Silent Payments e accetta solo questo tipo di pagamento. Con questa applicazione non sarà possibile creare un indirizzo Bitcoin classico (legacy, SegWit o Taproot standard). Questa restrizione deliberata consente di concentrarsi completamente sull'apprendimento del protocollo BIP-352 senza essere distratti da altre funzioni. L'interfaccia ordinata privilegia deliberatamente la facilità d'uso rispetto alla profusione di opzioni, rendendo lo strumento accessibile anche agli utenti che non conoscono i concetti di riservatezza del on-chain.



Il progetto è interamente open-source, sviluppato con Flutter per l'interfaccia mobile e Rust per la logica crittografica interna. Questa architettura combina un'esperienza utente fluida con prestazioni ottimali per le operazioni di scansione intensive.



### Come funzionano i pagamenti silenziosi?



I pagamenti silenziosi (BIP-352) si basano su un sofisticato meccanismo crittografico che utilizza la chiave Elliptic Curve Diffie-Hellman Exchange (ECDH). Il destinatario genera un indirizzo statico (che inizia con `sp1...` su mainnet o `tsp1...` su Signet) composto da due chiavi pubbliche distinte: una chiave di scansione ($B_{scan}$) per rilevare i pagamenti in arrivo e una chiave di spesa ($B_{spend}$) per spendere i fondi ricevuti. Questa separazione consente di mantenere la chiave di spesa sull'hardware wallet e di utilizzare la chiave di scansione su un dispositivo collegato.



Quando un mittente desidera effettuare un pagamento, il suo wallet combina la somma delle chiavi private dei suoi input con la chiave pubblica di scansione del destinatario per calcolare un segreto ECDH condiviso. Questo segreto genera un "tweak" crittografico che, aggiunto alla chiave di spesa del destinatario, crea un indirizzo Taproot unico per quella transazione.



Il destinatario può riprodurre questo calcolo utilizzando la sua chiave di scansione privata e le chiavi pubbliche visibili nella transazione (proprietà matematica Diffie-Hellman). Ciò gli consente di individuare e spendere i fondi senza alcuna interazione preliminare con il mittente.



Questo approccio offre diversi vantaggi:




- Riservatezza del destinatario**: ogni pagamento arriva a un indirizzo diverso
- Riservatezza del mittente**: nessun identificatore persistente che colleghi i pagamenti
- Nessun server di terze parti**: il protocollo funziona in modo autonomo
- Transazioni indistinguibili**: I pagamenti silenziosi appaiono come transazioni Taproot ordinarie



Lo svantaggio principale è il costo della scansione: il destinatario deve analizzare ogni nuova transazione Taproot per individuare quelle destinate a lui.



Se volete saperne di più sul funzionamento tecnico di Silent Payments, vi consigliamo il corso BTC204 sulla riservatezza in Bitcoin, che comprende un capitolo dedicato a Silent Payments:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Piattaforme supportate



Dana Wallet è disponibile come applicazione per Android. L'APK può essere scaricato tramite il repository dedicato F-Droid fornito dagli sviluppatori, tramite Obtainium o direttamente da GitHub. Per gli utenti Linux, è tecnicamente possibile compilare l'applicazione Flutter per desktop.



L'applicazione non è disponibile su iOS o sugli store ufficiali (Google Play, App Store), il che riflette il suo stato sperimentale e la sua attenzione per un pubblico tecnico.



## Installazione



### Prerequisiti essenziali



Per installare Dana Wallet su Android, è necessario un dispositivo Android con l'opzione "Sorgenti sconosciute" attivata nelle impostazioni di sicurezza. Non è necessario alcun account o registrazione.



### Aggiungere il deposito F-Cold



Il metodo consigliato è quello di aggiungere il repository F-Droid dedicato a Dana Wallet. Andate su `fdroid.silentpayments.dev` dove troverete il link al repository e un codice QR da scansionare. Il repository offre attualmente 3 applicazioni: la versione Mainnet, Development e Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Installazione tramite F-Droid



Aprire l'applicazione F-Droid sul dispositivo Android, quindi accedere alle Impostazioni tramite l'icona in basso a destra. Selezionare "Repository" per gestire le fonti delle app. Premere il pulsante "+" per aggiungere un nuovo repository, quindi scansionare il codice QR o incollare il link `https://fdroid.silentpayments.dev/fdroid/repo`. Una volta aggiunto il repository, verranno visualizzate le tre versioni di Dana Wallet disponibili. Selezionare "Dana Wallet - Bookmark" e premere "Install".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Configurazione iniziale



### Creazione del portafoglio



Al primo avvio, Dana Wallet visualizza una schermata di benvenuto che introduce la sua missione: "Inviare e ricevere donazioni senza intermediari". Premere "Inizia" per continuare. La schermata successiva presenta i tre vantaggi principali dell'applicazione:




- Donazioni senza sforzo**: iniziare a ricevere donazioni in pochi secondi
- Privacy by default**: non sono necessari server o infrastrutture complesse
- Esperienza simile all'e-mail**: inviare e ricevere bitcoin con la stessa semplicità di un'e-mail



È possibile scegliere tra "Ripristina" per ripristinare un portafoglio esistente o "Crea nuovo wallet" per crearne uno nuovo. Premere "Crea nuovo wallet".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



L'applicazione genera quindi una frase di ripristino, che deve essere accuratamente annotata su un supporto fisico. Anche per i fondi di prova privi di valore reale, adottare buone pratiche di backup.



### Interface e parametri



Una volta creato il portafoglio, si accede all'interfaccia principale, suddivisa in due schede: "Transact" e "Settings".



La scheda **Transact** mostra il saldo in bitcoin (e la sua conversione in dollari), un elenco delle transazioni recenti e due pulsanti di azione: "Paga" per inviare fondi e un pulsante di ricezione (icona di download).



La scheda **Impostazioni** offre quattro opzioni:




- Mostra frase seed**: visualizza la frase di recupero per conservarla
- Cambia valuta fiat**: cambia la valuta di visualizzazione (USD per impostazione predefinita)
- Impostare l'url del backend**: configurare l'URL del server Blindbit (vedere la sezione successiva)
- Pulisci wallet**: cancella completamente il wallet dal dispositivo



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Il server Blindbit



Dana Wallet utilizza un server di indicizzazione chiamato **Blindbit** per rilevare i pagamenti silenziosi. Capire come funziona è importante per valutare il modello di fiducia dell'applicazione.



**Perché abbiamo bisogno di un server?



Per rilevare un pagamento silenzioso, il wallet deve teoricamente analizzare tutte le transazioni Taproot in ogni blocco ed eseguire un calcolo crittografico (ECDH) per ciascuna di esse. Su un telefono cellulare, questa operazione sarebbe troppo impegnativa dal punto di vista del calcolo e della larghezza di banda.



Il server Blindbit risolve questo problema precalcolando i dati intermedi (chiamati "tweaks") per tutte le transazioni Taproot. Il vostro wallet scarica quindi questi tweak (33 byte per transazione) ed esegue il calcolo finale **localmente** per verificare se un pagamento vi appartiene.



**Preservata riservatezza**



A differenza di un server Electrum convenzionale in cui l'utente rivela il proprio indirizzo, il server Blindbit non sa quali pagamenti appartengono all'utente. Fornisce gli stessi dati a tutti gli utenti ed è il vostro telefono a effettuare la verifica finale. La vostra riservatezza è quindi preservata nei confronti del server.



**Server predefinito



Dana Wallet utilizza il server pubblico `silentpayments.dev/blindbit/signet` (per Signet) o `silentpayments.dev/blindbit/mainnet` (per Mainnet). È possibile modificare questo URL nelle impostazioni se si ospita un proprio server.



**Host del proprio server Blindbit**



Per gli utenti che desiderano una sovranità totale, è possibile ospitare il proprio server Blindbit Oracle. Ciò richiede :




- Un nodo core Bitcoin completo **non aggiogato** (non pruned)
- Installazione di Blindbit Oracle (disponibile su GitHub: `setavenger/blindbit-oracle`)
- Circa 10 GB di spazio aggiuntivo su disco
- Competenze tecniche (compilazione di Go, configurazione del server)



Non è ancora disponibile un'applicazione pacchettizzata per Umbrel o Start9. Per il momento l'installazione rimane manuale. Si tratta di un campo in continua evoluzione e in futuro potrebbero emergere soluzioni più accessibili.



## Uso quotidiano



### Ricezione di fondi



Per ricevere i bitcoin, premere il pulsante di ricezione (icona di download) dalla schermata principale. Dana Wallet visualizza l'indirizzo completo di Silent Payment nel formato `tsp1q...` su Bookmark. L'interfaccia offre diverse opzioni:




- Mostra codice QR**: visualizza il codice QR dell'indirizzo per facilitarne la scansione
- Condividi**: condividere l'indirizzo tramite le applicazioni del telefono
- Copia**: copia l'indirizzo negli appunti



Come mostrato sullo schermo, potete condividere questo indirizzo pubblicamente sui vostri social network senza compromettere la vostra privacy.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Per ottenere i primi fondi di prova su Signet, utilizzare il rubinetto dedicato di Silent Payments accessibile all'indirizzo `silentpayments.dev/faucet/signet`. Copiate il vostro indirizzo `tsp1...`, incollatelo nell'apposito campo del rubinetto, quindi convalidate la richiesta. Attendere che venga estratto un blocco (circa 10 minuti su Signet).



### Inviare un pagamento



Per inviare fondi, premere il pulsante "Paga" dalla schermata principale. Viene visualizzata la schermata "Scegliere il/i destinatario/i" con tre opzioni per specificare il destinatario:




- Inserire manualmente le informazioni di pagamento
- Incolla dagli appunti**: incolla un indirizzo dagli appunti
- Scansione del codice QR**: scansione di un codice QR contenente l'indirizzo



Una volta convalidato l'indirizzo del destinatario, la schermata "Inserisci importo" consente di inserire l'importo da inviare in satoshi. Il saldo disponibile viene visualizzato come riferimento. Premere "Procedere alla selezione della tariffa" per continuare.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



La schermata successiva mostra tre livelli di tariffazione, a seconda dell'urgenza richiesta:




- Veloce** (10-30 minuti): tariffe più alte per la conferma rapida
- Normale** (30-60 minuti): costi moderati
- Lentezza** (1+ ora): tariffa minima per transazioni non urgenti



Dopo aver selezionato il livello di commissione, la schermata di conferma "Pronto per l'invio?" riassume tutti i dettagli: indirizzo di destinazione, importo, tempo stimato e commissione della transazione. Controllate attentamente queste informazioni, quindi premete "Invia" per inviare la transazione.



Una volta inviata, la transazione viene visualizzata nella cronologia con lo stato "Non confermata" finché non viene inclusa in un blocco. Il saldo viene aggiornato di conseguenza.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Vantaggi e limiti



### Punti salienti





- Pedagogico**: interfaccia semplificata incentrata sull'apprendimento Pagamenti silenziosi
- Bidirezionale**: supporta sia l'invio che la ricezione, a differenza di altri portafogli
- Open-source**: codice completamente verificabile su GitHub
- Faucet** dedicato: facilita l'ottenimento di finanziamenti per i test
- Senza account**: non è richiesta alcuna registrazione o dato personale



### Vincoli da considerare





- Sperimentale**: software non verificato, usare con cautela su Mainnet
- Piattaforma limitata**: principalmente Android, nessuna versione iOS
- Funzionalità ridotte**: nessun controllo delle monete, nessun sub-account, nessun Lightning
- Scansione intensiva**: il rilevamento dei pagamenti consuma molte risorse



## Le migliori pratiche



### Sicurezza seed



Anche nel caso di test Signet con sfondi inutili, la frase di recupero deve essere presa sul serio. Utilizzate l'opzione "Mostra frase seed" nelle impostazioni per annotarla con cura. Come buona prassi, mantenete portafogli completamente separati per Signet e Mainnet: non utilizzate mai un seed creato per i test su un wallet destinato a ricevere fondi reali.



### Avviso sullo stato sperimentale



Dana Wallet è ancora considerato sperimentale dai suoi sviluppatori. Come affermano chiaramente: "Non utilizzate fondi che non siete disposti a perdere". Per imparare, optate per la versione Signet. Se si utilizza la versione Mainnet, limitarsi agli importi token.



### Backup e ripristino



Il recupero dei fondi Silent Payments richiede un wallet compatibile con il protocollo BIP-352. Un wallet standard non può eseguire la scansione della blockchain per recuperare i pagamenti silenziosi UTXO. Mantenere Dana Wallet installato o utilizzare l'opzione "Ripristina" al primo avvio per recuperare un wallet esistente.



## Confronto con BIP-47 e PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

I pagamenti silenziosi eliminano la transazione di notifica BIP-47 al costo di una scansione più costosa. Il PayJoin risolve un problema diverso (correlazione degli ingressi) e può essere combinato con i pagamenti silenziosi.



## Conclusione



Dana Wallet è un valido strumento didattico per imparare a conoscere i pagamenti silenziosi in un ambiente privo di rischi. Il suo approccio minimalista consente di comprendere i meccanismi fondamentali del protocollo BIP-352 senza essere distratti da caratteristiche secondarie. Sperimentando con Signet, si svilupperà una comprensione pratica di questa promettente tecnologia per la riservatezza delle transazioni Bitcoin.



I Silent Payments rappresentano un significativo passo avanti nel conciliare facilità d'uso e rispetto della privacy. L'entusiasmo della comunità e le prime integrazioni in vari portafogli (Cake Wallet, BitBox02, BlueWallet per l'invio) lasciano presagire un futuro in cui la pubblicazione di un indirizzo di donazione non comprometterà più la privacy finanziaria del suo proprietario.



## Risorse



### Documentazione ufficiale




- Repository GitHub di Dana Wallet: https://github.com/cygnet3/danawallet
- F-Cold deposito: https://fdroid.silentpayments.dev
- Sito della comunità Silent Payments: https://silentpayments.xyz
- Specifiche BIP-352: https://bips.dev/352



### Strumenti di test Signet




- Faucet Pagamenti silenziosi: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Server Blindbit (self-hosted)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle
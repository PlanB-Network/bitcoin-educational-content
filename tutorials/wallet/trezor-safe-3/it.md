---
name: Trezor Safe 3
description: Configurazione e utilizzo dell'hardware wallet Safe 3
---
![cover](assets/cover.webp)



*Credito immagine: [Trezor.io](https://trezor.io/)*



Trezor Safe 3 è un hardware wallet progettato da SatoshiLabs e creato nel 2023. È un modello molto compatto e leggero (14 grammi) ideato sia per i principianti che per gli utenti intermedi. È il successore del famoso Model One, con aggiunte significative, pur mantenendo l'approccio open-source del marchio che lo distingue dal suo principale concorrente, il Ledger. Il Safe 3 ha un prezzo di 79 euro. Si posiziona quindi nel segmento medio degli hardware wallet, in diretta concorrenza con il Ledger Nano S Plus.



Il Safe 3 non ha una batteria e funziona esclusivamente tramite una connessione USB-C, utilizzata sia per l'alimentazione che per la trasmissione di dati. È dotato di un piccolo display OLED monocromatico da 0,96 pollici e di due pulsanti.

![Image](assets/fr/01.webp)

Il Safe 3 offre tutte le caratteristiche essenziali che ci si aspetta da un buon hardware wallet, compresa un'eccellente integrazione della [passphrase BIP39](https://planb.academy/resources/glossary/passphrase-bip39). Tuttavia, non supporta ancora [Miniscript](https://planb.academy/resources/glossary/miniscript).

Questo modello è particolarmente adatto ai principianti e potrebbe addirittura essere l'hardware wallet che consiglierei a un nuovo utente. È adatto anche agli utenti intermedi. D'altra parte, potrebbe non soddisfare tutte le aspettative degli utenti avanzati che cercano funzioni più specifiche, disponibili su dispositivi come Coldcard. Tuttavia, se non hai bisogno di queste opzioni avanzate, Trezor Safe 3 può essere una scelta eccellente.

## Il modello di sicurezza di Trezor Safe 3

Trezor Safe 3 è ora dotato di un **Secure Element** certificato EAL6+, un progresso significativo rispetto ai modelli precedenti come il Model One e il Model T. Si tratta del chip OPTIGA Trust M V3, che non memorizza direttamente il seed, ma agisce come componente crittografico per proteggerne l'accesso. Il Secure Element conserva un segreto a cui si può accedere solo dopo che l'utente ha inserito correttamente il PIN. Questo segreto viene quindi utilizzato per decifrare il seed, che viene memorizzato in modo criptato nella memoria principale del dispositivo.



Questo sistema di sicurezza ibrido offre una migliore protezione fisica, in particolare contro gli attacchi di estrazione o di analisi invasiva, problemi a cui il Model One era soggetto, in particolare nella gestione dei PIN. Queste vulnerabilità sono ora aggirate grazie all'utilizzo del Secure Element. Questo modello mantiene inoltre un'architettura software open-source: il codice che gestisce la generazione e l'utilizzo delle chiavi private rimane completamente accessibile e verificabile. Il chip OPTIGA gestisce soltanto il codice PIN, un elemento esterno alla gestione delle chiavi bitcoin. Rilascia solo un segreto che può essere utilizzato per decifrare il seed. Inoltre, il chip OPTIGA Trust M V3 beneficia di una licenza relativamente libera, che autorizza SatoshiLabs a pubblicare liberamente le potenziali vulnerabilità.



Questo modello di sicurezza rappresenta, a mio avviso, uno dei migliori compromessi disponibili oggi sul mercato. Combina i vantaggi di un Secure Element con la gestione del software open-source. In precedenza, gli utenti dovevano scegliere tra una maggiore sicurezza fisica con un chip e la trasparenza con l'open-source; con Trezor Safe 3, è possibile beneficiare di entrambi.



In questa guida ti mostro come configurare e utilizzare il tuo Trezor Safe 3 in modo sicuro.



## Unboxing di Trezor Safe 3



Quando ricevi il Safe 3, assicurati che la scatola e il sigillo siano intatti per confermare che la confezione non è stata aperta. In seguito, al momento della configurazione, verrà effettuata una verifica a livello software dell'autenticità e dell'integrità del dispositivo.

Il contenuto della scatola comprende:

- Il Trezor Safe 3;
- Un astuccio contenente dei cartoncini per scrivere la frase mnemonica, insieme ad alcuni adesivi e alle istruzioni;
- Un cavo da USB-C a USB-C.

![Image](assets/fr/02.webp)


Una volta aperto, il Trezor Safe 3 dovrebbe essere protetto da una plastica protettiva, e la porta USB-C dovrebbe essere protetta da un sigillo olografico. Assicurati che sia presente.


![Image](assets/fr/03.webp)



La navigazione sul dispositivo è semplice: utilizza il pulsante destro per scorrere verso destra e il pulsante sinistro per scorrere verso sinistra. Premi entrambi i pulsanti contemporaneamente per confermare un'azione.



![Image](assets/fr/04.webp)



## Prerequisiti



In questo tutorial ti mostrerò come utilizzare Trezor Safe 3 con [Sparrow](https://sparrowwallet.com/download/). Se non hai ancora installato questo software, fallo subito. Se hai bisogno di aiuto, abbiamo anche un tutorial dettagliato sulla configurazione di Sparrow:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

È inoltre necessario il software Trezor Suite per configurare il Safe 3, verificarne l'autenticità e installare il firmware. Utilizzeremo questo software solo per questo, e in seguito sarà necessario solo per gli aggiornamenti del firmware. Per la gestione quotidiana del wallet, utilizzeremo esclusivamente Sparrow, in quanto è ottimizzato per bitcoin e facile da usare, anche per i principianti (Sparrow supporta solo bitcoin, non le altcoin).



[Scarica Trezor Suite dal sito ufficiale](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Per entrambi i programmi, consiglio vivamente di verificarne l'autenticità (con GnuPG) e l'integrità (tramite Hash) prima di installarli sul computer. Se non sai come fare, puoi seguire quest'altra guida:



https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Avvio di Trezor Safe 3



Collega il Safe 3 al computer dove sono già installati Trezor Suite e Sparrow.



![Image](assets/fr/06.webp)



Apri Trezor Suite, quindi fai clic su "*Set up my Trezor*".



![Image](assets/fr/07.webp)



Seleziona "*Bitcoin-only firmware*", quindi fai clic su "*Install Bitcoin-only*".



![Image](assets/fr/08.webp)



Trezor Suite installerà quindi il firmware su Safe 3. Attendi durante l'installazione.



![Image](assets/fr/09.webp)



Fai clic su "*Continue*".



![Image](assets/fr/10.webp)



Procedi quindi al test di autenticità per assicurarti che l'hardware wallet non sia falso o compromesso.



![Image](assets/fr/11.webp)



Sul Safe 3, premi il pulsante destro per confermare.



![Image](assets/fr/12.webp)



Se il Trezor è autentico, in Trezor Suite apparirà un messaggio di conferma.



![Image](assets/fr/13.webp)



È quindi possibile saltare le finestre con le istruzioni operative di base.



![Image](assets/fr/14.webp)



## Creare un wallet Bitcoin



Su Trezor Suite, fai clic sul pulsante "*Create new wallet*".



![Image](assets/fr/15.webp)



Per un wallet standard, si può optare per il tipo di backup predefinito. In questo modo crei un wallet classico a sigla singola con una frase mnemonica di 12 parole. Fai clic su "*Create wallet*".



Se vuoi saperne di più sulle altre opzioni di backup disponibili su Trezor, tra cui *Multi-share Backup*, ti consiglio di consultare anche questo tutorial:



https://planb.academy/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Accetta le condizioni di utilizzo dell'hardware wallet.



![Image](assets/fr/17.webp)



Premi nuovamente il pulsante destro per creare un nuovo wallet.



![Image](assets/fr/18.webp)



In Trezor Suite, fai clic su "*Continue to backup*".



![Image](assets/fr/19.webp)



Il software fornisce istruzioni su come gestire la frase mnemonica.



Questa mnemonica ti dà accesso completo e illimitato a tutti i tuoi bitcoin. Chiunque sia in possesso di questa frase può rubare i tuoi fondi, anche senza avere accesso fisico al tuo Trezor Safe 3.



La frase di 12 parole ripristina l'accesso ai tuoi bitcoin in caso di smarrimento, furto o rottura del tuo hardware wallet. È quindi molto importante salvarla con cura e conservarla in un luogo sicuro.



Puoi scriverla sul cartoncino fornito nella scatola, oppure, per maggiore sicurezza, ti consiglio di inciderla su una base in acciaio inossidabile per salvaguardarla da incendi, allagamenti o crolli di edificio.



Conferma le istruzioni, quindi fai clic sul pulsante "*Create wallet backup*".



![Image](assets/fr/20.webp)



Safe 3 creerà la tua frase mnemonica utilizzando il suo generatore di numeri casuali. Assicurati di non essere osservato durante questa operazione. Scrivi le parole fornite sullo schermo su un supporto fisico di tua scelta. A seconda della tua strategia di sicurezza, puoi pensare di creare diverse copie fisiche della frase completa (ma, cosa importante, non dividerla in più parti). È importante che le parole siano numerate e in ordine sequenziale.



**Ovviamente, non devi mai condividere queste parole su Internet, come faccio io in questo tutorial. Questo wallet di esempio sarà utilizzato solo su Testnet e sarà cancellato alla fine del tutorial.**



Per ulteriori informazioni sul modo corretto di salvare e gestire la frase mnemonica, ti consiglio di seguire quest'altro tutorial, soprattutto se sei un principiante:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Per passare alle parole successive, fai clic con il tasto destro del mouse. È possibile andare indietro facendo clic sul pulsante sinistro. Una volta scritte tutte le parole, tieni premuto il tasto destro per passare alla fase successiva.



![Image](assets/fr/22.webp)



Seleziona le parole della frase mnemonica in base al loro ordine per confermare che sono state scritte correttamente. Utilizza i pulsanti destro e sinistro per spostarsi tra le proposte, quindi seleziona la parola corretta facendo clic contemporaneamente sui due pulsanti.



![Image](assets/fr/23.webp)



Una volta completata la procedura di verifica, fai clic sul pulsante a destra.



![Image](assets/fr/24.webp)



## Impostazione del codice PIN


Ora passiamo alla fase del codice PIN, che serve a sbloccare Trezor e quindi fornisce protezione contro l'accesso fisico non autorizzato. Il codice PIN non serve alla creazione delle chiavi crittografiche del wallet. Di conseguenza, anche se dovessi perdere il PIN, la frase mnemonica di 12 parole ti permetterà di riavere accesso ai tuoi bitcoin.

Su Trezor Suite, fai clic su "*Continue to PIN*", quindi sul pulsante "*Set PIN*".

![Image](assets/fr/25.webp)



Conferma con Safe 3.



![Image](assets/fr/26.webp)



Si consiglia di scegliere un codice PIN il più possibile casuale. Assicurati di conservare questo codice in un luogo diverso da quello in cui è riposto Trezor (ad esempio, usando un password manager). È possibile definire un codice PIN compreso tra 8 e 50 cifre. Si consiglia di scegliere un codice PIN il più lungo possibile, per maggiore sicurezza.

Utilizza i pulsanti destro e sinistro per selezionare ogni numero. Per confermare la scelta e passare al numero successivo, premi entrambi i pulsanti contemporaneamente.

![Image](assets/fr/27.webp)

Al termine, fai clic sul segno di spunta "*ENTER*" all'inizio dei numeri, quindi conferma il PIN una seconda volta.

![Image](assets/fr/28.webp)

Il codice PIN è stato registrato.


![Image](assets/fr/29.webp)

Su Trezor Suite, clicca sul pulsante "*Complete setup*".

![Image](assets/fr/30.webp)

La configurazione del Safe 3 è ora completa. Se lo desideri, è possibile modificare il nome e la pagina iniziale dell'hardware wallet.

![Image](assets/fr/31.webp)

Da ora in poi, non avremo più bisogno del software Trezor Suite, se non per eseguire gli aggiornamenti regolari del firmware sull'hardware wallet o per eseguire un test di ripristino. 

Ora utilizzeremo Sparrow per gestire il wallet, poiché questo software è perfettamente adatto all'uso esclusivo di bitcoin.

## Impostazione del wallet su Sparrow

Inizia scaricando e installando Sparrow [dal sito ufficiale](https://sparrowwallet.com/) sul tuo computer, se non l'hai ancora fatto.

Una volta aperto Sparrow, assicurati che il software sia collegato a un nodo Bitcoin, indicato dal segno di spunta nell'angolo in basso a destra dell'interfaccia. Se hai problemi a collegare Sparrow, ti consiglio di leggere l'inizio di questa guida:

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Fai clic sulla scheda "*File*", quindi su "*New wallet*".

![Image](assets/fr/32.webp)

Assegna un nome al wallet, quindi fai clic su "*Create wallet*".

![Image](assets/fr/33.webp)

Nel menù a discesa "*Script Type*", seleziona il tipo di script che verrà utilizzato per proteggere i bitcoin. Io consiglio "*Taproot*" o, in mancanza, "*Native SegWit*".

![Image](assets/fr/34.webp)

Fai clic sul pulsante "*Connected hardware wallet*". Il Safe 3 deve ovviamente essere collegato al computer e sbloccato.

![Image](assets/fr/35.webp)

Fare clic sul pulsante "*Scan*". Dovrebbe apparire il tuo Safe 3. Fai clic su "*Import Keystore*".

![Image](assets/fr/36.webp)

Ora è possibile visualizzare i dettagli del proprio wallet, compresa la chiave pubblica estesa del primo account. Fai clic sul pulsante "*Apply*" per completare la creazione del wallet.

![Image](assets/fr/37.webp)

Scegli una password forte per proteggere l'accesso a Sparrow. Questa password garantirà un accesso sicuro ai dati, proteggendo le chiavi pubbliche, gli indirizzi, le etichette e la cronologia delle transazioni da accessi non autorizzati.

Ti consiglio di salvare questa password in un password manager per non dimenticarla.

![Image](assets/fr/38.webp)

E ora il tuo wallet è stato importato su Sparrow!

![Image](assets/fr/39.webp)

Prima di ricevere i primi bitcoin, **consiglio vivamente di eseguire un test di ripristino del wallet, ora che è ancora vuoto**. Annota alcune informazioni di riferimento, come il tuo xpub, quindi resetta il tuo Trezor Safe 3 mentre il wallet è ancora vuoto. Fatto questo, prova a ripristinare il wallet su Trezor utilizzando i backup su carta. Verifica che l'xpub generato dopo il ripristino corrisponda a quello scritto in origine. Se così fosse, si può essere certi che i backup che hai scritto siano affidabili.

Per saperne di più su come eseguire un test di ripristino, ti suggerisco di consultare quest'altro tutorial:

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Come posso ricevere bitcoin con Trezor Safe 3?

Su Sparrow, fai clic sulla scheda "*Receive*".

![Image](assets/fr/40.webp)

Prima di utilizzare l'indirizzo proposto da Sparrow, verificalo sullo schermo del tuo Trezor. Ciò consente di confermare che l'indirizzo visualizzato su Sparrow non è fraudolento e che l'hardware wallet contiene effettivamente la chiave privata necessaria per spendere i bitcoin legati a questo indirizzo. In questo modo, si possono evitare diversi tipi di attacchi.

Per eseguire questo controllo, fai clic sul pulsante "*Display Address*".

![Image](assets/fr/41.webp)

Verifica che l'indirizzo visualizzato su Trezor corrisponda a quello del wallet di Sparrow. È consigliabile effettuare questo controllo anche prima di comunicare l'indirizzo al mittente, per essere sicuri della sua validità. Puoi utilizzare i pulsanti per confermare.

![Image](assets/fr/42.webp)

È quindi possibile aggiungere una "*Label*" (etichetta) per descrivere la provenienza dei bitcoin, la quale sarà associata a questo indirizzo. Questa è una buona pratica che consente di gestire meglio gli UTXO.

![Image](assets/fr/43.webp)

A questo punto puoi utilizzare questo indirizzo per ricevere bitcoin.

![Image](assets/fr/44.webp)

## Come si inviano i bitcoin con Trezor Safe 3?

Ora che hai ricevuto i tuoi primi sats sul tuo Safe 3, puoi anche spenderli! Collega il tuo Trezor al computer, sbloccalo con il codice PIN, lancia Sparrow, quindi vai alla scheda "*Send*" per creare una nuova transazione.

![Image](assets/fr/45.webp)

Se desideri fare *coin control*, ossia scegliere specificamente quali [UTXO](https://planb.academy/resources/glossary/utxo) utilizzare nella transazione, vai alla scheda "*UTXO*". Seleziona gli UTXO che desideri spendere, quindi fai clic su "*Send Selected*". Verrai reindirizzato alla stessa schermata della scheda "*Send*", ma con gli UTXO già selezionati per la transazione.

![Image](assets/fr/46.webp)

Inserisci l'indirizzo di destinazione. È possibile inserire più indirizzi facendo clic sul pulsante "*+ Add*".

![Image](assets/fr/47.webp)

Scrivi un "*Label*" per ricordare lo scopo di questa transazione.

![Image](assets/fr/48.webp)

Seleziona l'importo da inviare a questo indirizzo.

![Image](assets/fr/49.webp)

Regola le fee della transazione in base alla media attuale. Ad esempio, è possibile utilizzare [Mempool.space](https://Mempool.space/) per scegliere un'ammontare adeguato.

Assicurati che tutti i parametri della transazione siano corretti, quindi fai clic su "*Create Transaction*".

![Image](assets/fr/50.webp)

Se sei soddisfatto, clicca su "*Finalize Transaction for Signing*".

![Image](assets/fr/51.webp)

Fai clic su "*Sign*".

![Image](assets/fr/52.webp)

Fai clic su "*Sign*" accanto al tuo Trezor Safe 3.

![Image](assets/fr/53.webp)

Controlla i parametri della transazione sullo schermo dell'hardware wallet, compresi l'indirizzo del destinatario, l'importo inviato e l'addebito. Una volta verificata la transazione su Trezor, fai clic su entrambi i pulsanti contemporaneamente per firmarla.

![Image](assets/fr/54.webp)

La transazione è ora firmata. Verifica un'ultima volta che tutto sia a posto, quindi fai clic su "*Broadcast Transaction*" per trasmetterla sulla rete Bitcoin.

![Image](assets/fr/55.webp)

Si trova nella scheda "*Transactions*" di Sparrow.

![Image](assets/fr/56.webp)

Congratulazioni, ora sai come usare Trezor Safe 3 con Sparrow! Per fare un ulteriore passo avanti, ti consiglio questo tutorial completo sull'uso di Trezor con passphrase BIP39 per ottenere maggiore sicurezza:

https://planb.academy/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Se questo tutorial è stato utile, ti sarei grato se lasciassi un pollice verde qui sotto. Sentiti libero di condividere questo articolo sui tuoi social network. Grazie mille!

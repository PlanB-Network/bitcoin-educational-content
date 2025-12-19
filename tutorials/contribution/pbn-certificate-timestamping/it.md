---
name: Marcatura temporale dei certificati di Plan ₿ Academy
description: Comprendi come Plan ₿ Academy rilascia una prova verificabile per i tuoi certificati e diplomi
---

![cover](assets/cover.webp)

Se stai leggendo questo tutorial, c'è un'alta probabilità che tu abbia ricevuto un Certificato dopo il test ₿-CERT, o un diploma per aver completato uno dei corsi su Plan ₿ Academy, quindi congratulazioni per questo traguardo!

In questo tutorial, vedremo come Plan ₿ Academy rilascia una prova verificabile per il tuo Certificato ₿-CERT o qualsiasi Diploma di completamento di un Corso. Poi, in una seconda parte, vedremo come verificare l'autenticità di queste prove.

# Quale meccanismo usa Plan ₿ Academy

I certificati e diplomi di Plan ₿ Academy sono firmati crittograficamente da noi e marcati temporalmente sulla Timechain (ovvero, la blockchain di Bitcoin). Per farlo, abbiamo ideato un metodo per provarne l'autenticità che si basa su 2 operazioni crittografiche:

1. Una firma GPG su un file di testo che sintetizza i tuoi risultati
2. La marcatura temporale di questo file firmato tramite [opentimestamps](https://opentimestamps.org/).

Fondamentalmente, la prima operazione ti permette di verificare chi ha rilasciato il certificato (o diploma), mentre la seconda ti permette di verificare quando è stato rilasciato.
Questo semplice meccanismo ci permette di rilasciare certificati e diplomi con prove indiscutibili che chiunque può verificare autonomamente.

![image](./assets/proof-mechanism.webp)

Da notare che, grazie a questo metodo, qualsiasi tentativo di alterare anche il più piccolo dettaglio del tuo certificato o diploma creerà un hash sha256 completamente diverso del file firmato: ciò rivelerà immediatamente la manomissione del file, perché la firma ed il timestamp non saranno più validi. Inoltre, se qualcuno tentasse di falsificare alcuni certificati o diplomi di Plan ₿ Academy con intenti malevoli, una semplice verifica della firma rivelerà l'inganno.

## Come funziona la firma GPG?

La firma GPG è ottenuta con l'uso di un software open-source chiamato GNU Private Guard. Questo software permette a chiunque non solo di creare facilmente chiavi private, firmare e verificare firme, ma anche di criptare e decriptare file. È bene sapere che Plan ₿ Academy utilizza GPG per creare la sua chiave privata/pubblica e per firmare qualsiasi certificato ₿-CERT o diploma rilasciato alla fine di un corso.

Di conseguenza, se qualcuno volesse verificare l'autenticità di un file firmato, può usare GPG per importare la chiave pubblica dell'emittente e controllare la veridicità della firma. Nella seconda parte del tutorial vedremo come farlo tramite l'uso del terminale.

Se sei curioso e vuoi sapere di più su questo fantastico software, puoi fare riferimento a ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## Come funziona il Timestamping?

Chiunque può usare OpenTimestamps per marcare temporalmente un file e ottenere una prova verificabile della sua esistenza. In altre parole, non ti fornisce una prova di quando il file è stato creato, ma una prova della sua esistenza successiva a un certo momento.
OpenTimestamps è in grado di offrire questo servizio gratuitamente grazie a un modo altamente efficiente di memorizzare tale prova nella Blockchain di Bitcoin. Il sistema parte dall'utilizzo della funziona crittografica hash sha256 per trovare un identificatore unico del file. In seguito, usa la stringa alfanumerica trovata per costruire un Merkle Tree, unendola agli hash dei file di altri utenti. Infine, prende soltanto l'hash alla radice del Merkle Tree e lo inserisce in una Transazione OpReturn.

Una volta che questa transazione è in qualche blocco, chiunque abbia il file iniziale e il file `.ots` ad esso associato può verificare l'autenticità del timestamp. Nella seconda parte del tutorial vedremo come verificare il tuo certificato ₿-CERT o qualsiasi diploma rilasciato alla fine di un corso tramite un terminale e tramite un'interfaccia grafica sul sito web di OpenTimestamps.

# Come verificare un certificato o un diploma di Plan ₿ Academy

## Passo 1. Scarica il certificato o diploma

Accedi alla tua dashboard personale su planb.network.

![image](./assets/login.webp)

Vai alla pagina delle Credenziali cliccando sul menù laterale sinistro, e seleziona la tua sessione d'esame o il tuo diploma.

![image](./assets/credential.webp)

Scarica il file zip.

![image](./assets/download.webp)

Estrai i contenuti cliccando destro sul file `.zip` e selezionando "Estrai". Troverai tre file diversi all'interno:

- Un file di testo firmato (ad es., certificate.txt)
- Un file Open timestamp (OTS) (ad es., certificate.txt.ots)
- Il certificato in PDF (ad es., certificate.pdf)

## Passo 2: Verifica della firma del file di testo

Apri prima un terminale nella cartella dove si trovano i file (clicca con il tasto destro sulla finestra della cartella e poi su "Apri un Terminale qui"). Poi segui le istruzioni sottostanti:

1. Importa la chiave pubblica PGP di Plan ₿ Academy con il seguente comando:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/Plan ₿ Academy-pk.asc | gpg --import
```

Dovresti vedere un messaggio come il seguente, se hai importato con successo la Chiave PGP:

```
gpg: key 8F12D0C63B1A606E: chiave pubblica "Plan ₿ Academy (usata per la piattaforma Plan ₿ Academy) <admin@planb.network>" importata
gpg: Totale elaborato: 1
gpg:               importate: 1
```

NOTA: se vedi che 1 chiave è stata elaborata e 0 sono state importate, molto probabilmente hai già importato in precedenza la stessa chiave, quindi è tutto a posto.

2. Verifica la firma del certificato o del diploma digitando il seguente comando:
   
*Assicurati di essere nella stessa directory nel quale hai salvato i file del punto 1.*

```bash
gpg --verify certificate.txt
```

Questo comando dovrebbe mostrarti i dettagli sulla firma, inclusi:

- Chi l'ha firmato (Plan ₿ Academy)
- Quando è stato firmato
- Se la firma è valida

Questo è un esempio del risultato:

```
gpg: Firma effettuata lun 11 nov 2024, 00:39:04 CET
gpg:                usando la chiave RSA 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                emittente "admin@planb.network"
gpg: Buona firma da "Plan ₿ Academy (usata per la piattaforma Plan ₿ Academy) <admin@planb.network>" [sconosciuto]
```

Se vedi un messaggio come "FIRMA NON VALIDA", significa che il file è stato manomesso.

## Passo 3: Verifica dell'open timestamp

### Verifica tramite interfaccia grafica

1. Visita il sito web di OpenTimestamps: https://opentimestamps.org/
2. Clicca sulla scheda "Stamp & Verify".
3. Trascina e rilascia il file OTS (ad es., `certificate.txt.ots`) nell'area designata.
4. Trascina e rilascia il file con timestamp (ad es. `certificate.txt`) nell'area designata.
5. Il sito web verificherà automaticamente l'open timestamp e mostrerà il risultato.

Se vedi un messaggio come il seguente il tuo timestamp è valido:

![copertina](assets/opentimestamp_wegui_verified.webp)

### Metodo CLI

NOTA: questa procedura **richiederà l'esecuzione di un nodo Bitcoin in locale**

1. Installa il client OpenTimestamps dal [repository ufficiale](https://github.com/opentimestamps/opentimestamps-client) eseguendo il seguente comando:

```
pip install opentimestamps-client
```

2. Naviga nella directory che contiene i file dei certificati estratti.

3. Esegui il seguente comando per verificare l'open timestamp:

```
ots verify certificate.txt.ots
```

Questo comando:

- Verificherà il timestamp confrontandolo con la blockchain di Bitcoin
- Ti mostrerà esattamente quando il file è stato firmato con il timestamp
- Confermerà l'autenticità del timestamp

### Risultati finali

Nota che la verifica è riuscita se vengono visualizzati **entrambi** i seguenti messaggi:

1. La firma GPG è segnalata come **"Buona/Valida firma da Plan ₿ Academy"**
2. La verifica di OpenTimestamps mostra uno specifico timestamp del blocco Bitcoin e riporta **"Successo! Il blocco Bitcoin [altezza del blocco] attesta che i dati esistevano già al [timestamp]"**

Ora che sai come Plan ₿ Academy emette una prova verificabile per qualsiasi certificato ₿-CERT e diploma, puoi facilmente provarne l'integrità.

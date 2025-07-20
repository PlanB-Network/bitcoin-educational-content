---
name: Marcatura temporale dei diplomi Plan ₿ Network
description: Comprendi come Plan ₿ Network rilascia una prova verificabile per i tuoi certificati e diplomi
---

![cover](assets/cover.webp)

Se stai leggendo questo, c'è un'alta probabilità che tu abbia ricevuto un Certificato del B-CERT o un diploma per aver completato uno dei corsi su Plan ₿ Network, quindi congratulazioni per questo traguardo!

In questo tutorial, vedremo come Plan ₿ Network rilascia una prova verificabile per il tuo Certificato del B-CERT o qualsiasi Diploma di Completamento del Corso. Poi, in una seconda parte, vedremo come verificare l'autenticità di queste prove.

# Quale meccanismo usa Plan ₿ Network

A Plan ₿ Network, ti offriamo certificati e diplomi che sono firmati crittograficamente da noi e marcati temporali sulla Timechain (ovvero, la blockchain di Bitcoin). Per raggiungere questo obiettivo, abbiamo dovuto ideare un meccanismo di prova che si basa su 2 operazioni crittografiche:

1. Una firma GPG su un file di testo che sintetizza i tuoi risultati
2. La marcatura temporale di questo file firmato tramite [opentimestamps](https://opentimestamps.org/).

Fondamentalmente, la prima operazione ti permette di verificare chi ha rilasciato il certificato (o diploma), mentre la seconda ti permette di verificare quando è stato rilasciato.
Pensiamo che questo semplice meccanismo ci permetta di rilasciare certificati e diplomi con prove indiscutibili che chiunque può verificare autonomamente.

![image](./assets/proof-mechanism.webp)

Da notare che, grazie a questo meccanismo, qualsiasi tentativo di alterare anche il più piccolo dettaglio del tuo certificato o diploma creerà un hash sha256 completamente diverso del file firmato, che rivelerà immediatamente la manomissione perché la firma ed il timestamp non saranno più validi. Inoltre, se qualcuno tentasse di falsificare maliziosamente alcuni certificati o diplomi per conto di Plan ₿ Network, una semplice verifica della firma rivelerà la frode.

## Come funziona la firma GPG?

La firma GPG è ottenuta con l'uso di un software open-source chiamato GNU Private Guard. Questo software permette a chiunque di creare facilmente chiavi private, firmare e verificare firme e anche criptare e decriptare file. Sappi che Plan ₿ Network utilizza GPG per creare la sua chiave privata/pubblica e per firmare qualsiasi Certificato del B-CERT o Diploma rilasciato alla fine di un corso.

D'altra parte, se qualcuno volesse verificare l'autenticità di un file firmato può usare GPG per importare la chiave pubblica dell'emittente e controllare la veridicità della firma. Nella seconda parte del tutorial vedremo come farlo con il terminale.

Per coloro che sono curiosi e vogliono saperne di più su questo fantastico software, potete fare riferimento a ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## Come funziona il Timestamping?

Chiunque può usare OpenTimestamps per marcare temporalmente un file e ottenere una prova verificabile dell'esistenza del file stesso. In altre parole, non ti fornisce una prova di quando il file è stato creato, ma una prova della sua esistenza successiva a un certo momento.
OpenTimestamps è in grado di offrire questo servizio gratuitamente grazie a un modo altamente efficiente di memorizzare tale prova nella Blockchain di Bitcoin. Utilizza l'hash sha256 del file come identificatore unico e costruisce un Merkle Tree con altri hash di file inviati da altri utenti. Poi ancora solo l'hash della struttura del Merkle Tree in una Transazione OpReturn.
Una volta che questa transazione è in qualche blocco, chiunque abbia il file iniziale e il file `.ots` ad esso associato può verificare l'autenticità del timestamp. Nella seconda parte del tutorial vedremo come verificare il tuo Certificato del B-CERT o qualsiasi Diploma rilasciato alla fine di un corso con un terminale e con un'interfaccia grafica tramite il sito web di OpenTimestamps.

# Come verificare un Certificato o Diploma di Plan ₿ Network

## Passo 1. Scarica il tuo Certificato o Diploma

Accedi alla tua dashboard personale PBN.

![image](./assets/login.webp)

Vai alla pagina delle Credenziali cliccando sul menu laterale sinistro, e seleziona la tua sessione d'esame o il tuo Diploma.

![image](./assets/credential.webp)

Scarica il file zip.

![image](./assets/download.webp)

Estrai i contenuti facendo clic destro sul file `.zip` e selezionando "Estrai". Troverai tre file diversi all'interno:

- File di testo firmato (ad es., certificate.txt)
- File Open timestamp (OTS) (ad es., certificate.txt.ots)
- Certificato PDF (ad es., certificate.pdf)

## Passo 2: Verifica della Firma del File di Testo

Apri prima un terminale nella cartella dove si trovano i file (cliccando con il tasto destro sulla finestra della cartella e clicca su "Apri nel Terminale"). Poi segui le istruzioni sottostanti

1. Importa la chiave pubblica PGP di Plan ₿ Network con il seguente comando:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

Dovresti vedere un messaggio come il seguente se hai importato con successo la Chiave PGP

```
gpg: key 8F12D0C63B1A606E: chiave pubblica "PlanB Network (usata per la piattaforma PBN) <admin@planb.network>" importata
gpg: Totale elaborato: 1
gpg:               importate: 1
```

NOTA: se vedi che 1 chiave è stata elaborata e 0 sono state importate, molto probabilmente hai già importato precedentemente la stessa chiave ed è tutto a posto.

2. Verifica la firma del certificato o diploma con il seguente comando:

*Assicurati di essere nella stessa directory nel quale hai salvato i file al punto 1.*

```bash
gpg --verify certificate.txt
```

Questo comando dovrebbe mostrarti dettagli sulla firma, inclusi:

- Chi l'ha firmato (Plan ₿ Network)
- Quando è stato firmato
- Se la firma è valida

Questo è un esempio del risultato:

```
gpg: Firma effettuata lun 11 nov 2024, 00:39:04 CET
gpg:                usando la chiave RSA 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                emittente "admin@planb.network"
gpg: Buona firma da "PlanB Network (usata per la piattaforma PBN) <admin@planb.network>" [sconosciuto]
```

Se vedi un messaggio come "FIRMA NON VALIDA", significa che il file è stato manomesso.

## Passo 3: Verifica dell'Open Timestamp

### Verifica tramite Interfaccia Grafica

1. Visita il sito web di OpenTimestamps: https://opentimestamps.org/
2. Clicca sulla scheda "Stamp & Verify".
3. Trascina e rilascia il file OTS (ad es., `certificate.txt.ots`) nell'area designata.
4. Trascina e rilascia il file con timestamp (ad es. `certificate.txt`) nell'area designata.
5. Il sito web verificherà automaticamente l'open timestamp e mostrerà il risultato.

Se vedi un messaggio come il seguente il tuo timestamp è valido:
![copertina](assets/opentimestamp_wegui_verified.webp)
### Metodo CLI

NOTA: questa procedura **richiederà l'esecuzione di un nodo Bitcoin locale**

1. Installa il client OpenTimestamps dal repository ufficiale: https://github.com/opentimestamps/opentimestamps-client eseguendo il seguente comando:

```
pip install opentimestamps-client
```

2. Naviga nella directory che contiene i file dei certificati estratti.

3. Esegui il seguente comando per verificare l'open timestamp:

```
ots verify certificate.txt.ots
```

Questo comando:

- Verificherà il timestamp a con un confronto con la blockchain di Bitcoin
- Ti mostrerà esattamente quando il file è stato firmato con il timestamp
- Confermerà l'autenticità del timestamp

### Risultati finali

Nota che la verifica è riuscita se vengono visualizzati **entrambi** i seguenti messaggi:

1. La firma GPG è segnalata come **"Buona firma da Plan ₿ Network"**
2. La verifica di OpenTimestamps mostra uno specifico timestamp del blocco Bitcoin e riporta **"Successo! Il blocco Bitcoin [altezza del blocco] attesta che i dati esistevano già al [timestamp]"**

Ora che sai come Plan ₿ Network emette una prova verificabile per qualsiasi Certificato del B-CERT e Diploma, puoi facilmente verificarne l'integrità.

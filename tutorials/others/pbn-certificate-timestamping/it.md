---
name: Marcatura temporale dei certificati e diplomi della Rete Plan ₿
description: Comprendi come la Rete Plan ₿ rilascia una prova verificabile per il tuo certificato e diplomi
---

![cover](assets/cover.webp)

Se stai leggendo questo, c'è un'alta probabilità che tu abbia ricevuto un Certificato Bitcoin o un diploma di completamento per uno dei corsi che hai fatto sulla Rete Plan B, quindi congratulazioni per questo traguardo!

In questo tutorial, vedremo come la Rete Plan B rilascia una prova verificabile per il tuo Certificato Bitcoin o qualsiasi Diploma di Completamento del Corso. Poi, in una seconda parte, vedremo come verificare l'autenticità di queste prove.

# Meccanismo di prova della Rete Plan B

Nella Rete Plan ₿, ti offriamo un certificato e diplomi che sono firmati crittograficamente da noi e marcatori temporali sulla Timechain (ovvero, la blockchain di Bitcoin). Per raggiungere questo obiettivo, abbiamo dovuto ideare un meccanismo di prova che si basa su 2 operazioni crittografiche:

1. Una firma GPG su un file di testo che sintetizza i tuoi risultati
2. La marcatura temporale di questo file firmato tramite [opentimestamps](https://opentimestamps.org/).

Fondamentalmente, la prima operazione ti permette di verificare chi ha rilasciato il certificato (o diploma), mentre la seconda ti permette di verificare quando è stato rilasciato.
Crediamo che questo semplice meccanismo di prova ci permetta di rilasciare certificati e diplomi con prove indiscutibili che chiunque può verificare autonomamente.

![image](./assets/proof-mechanism.webp)

Nota che grazie a questo meccanismo di prova, qualsiasi tentativo di alterare anche il più piccolo dettaglio del tuo certificato o diploma creerà un hash sha256 completamente diverso del file firmato, che rivelerà immediatamente la manomissione perché la firma e la marcatura temporale non saranno più valide. Inoltre, se qualcuno tenta di falsificare maliziosamente alcuni certificati o diplomi per conto della Rete Plan B, una semplice verifica della firma rivelerà la frode.

## Come funziona la firma GPG?

La firma GPG è ottenuta con l'uso di un software open-source chiamato GNU Private Guard. Questo software permette a chiunque di creare facilmente chiavi private, firmare e verificare firme e anche criptare e decriptare file. Per lo scopo di questo tutorial, sappi che la Rete Plan B utilizza GPG per creare la sua chiave privata/pubblica e per firmare qualsiasi Certificato Bitcoin o Diploma di Completamento del Corso.

D'altra parte, se qualcuno vuole verificare l'autenticità di un file firmato può usare GPG per importare la chiave pubblica dell'emittente e verificare. Nella seconda parte del tutorial vedremo come farlo con un terminale.

Per coloro che sono curiosi e vogliono saperne di più su questo fantastico software, potete fare riferimento a ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## Come funziona la marcatura temporale?

Chiunque può usare OpenTimestamps per marcare temporalmente un file e ottenere una prova verificabile dell'esistenza del file. In altre parole, non ti fornisce una prova di quando il file è stato creato ma una prova dell'esistenza non oltre un certo momento.
OpenTimestamps è in grado di offrire questo servizio gratuitamente grazie a un modo altamente efficiente di memorizzare tale prova nella Blockchain di Bitcoin. Utilizza l'hash sha256 del file come identificatore unico del tuo file e costruisce un albero di Merkle con altri hash di file inviati da altri utenti e ancorare solo l'hash della struttura dell'Albero di Merkle in una Transazione OpReturn.
Una volta che questa transazione è in qualche blocco, chiunque abbia il file iniziale e il file `.ots` ad esso associato può verificare l'autenticità della marcatura temporale. Nella seconda parte del tutorial vedremo come verificare il tuo Certificato Bitcoin o qualsiasi Diploma di Completamento del Corso con un terminale e con un'interfaccia grafica tramite il sito web di OpenTimestamps.

# Come verificare un Certificato o Diploma della Rete Plan B

## Passo 1. Scarica il tuo Certificato o Diploma

Accedi alla tua dashboard personale PBN.

![image](./assets/login.webp)

Vai alla pagina delle Credenziali cliccando sul menu laterale sinistro, e seleziona la tua sessione d'esame o il tuo Diploma di Completamento del Corso.

![image](./assets/credential.webp)

Scarica il file zip.

![image](./assets/download.webp)

Estrai i contenuti facendo clic destro sul file `.zip` e selezionando "Estrai". Troverai tre file diversi all'interno:

- File di testo firmato (ad es., certificate.txt)
- File Open timestamp (OTS) (ad es., certificate.txt.ots)
- Certificato PDF (ad es., certificate.pdf)

## Passo 2: Verifica della Firma del File di Testo

Apri prima un terminale nella cartella dove si trovano i file (cliccando con il tasto destro sulla finestra della cartella e clicca su "Apri nel Terminale"). Poi segui le istruzioni sottostanti

1. Importa la chiave pubblica PGP della Rete Plan ₿ con il seguente comando:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

Dovresti vedere un messaggio come il seguente se hai importato con successo la Chiave PGP

```
gpg: key 8F12D0C63B1A606E: chiave pubblica "PlanB Network (usata per la piattaforma PBN) <admin@planb.network>" importata
gpg: Totale elaborato: 1
gpg:               importate: 1
```

NOTA: se vedi che 1 chiave è stata elaborata e 0 importate, molto probabilmente hai già importato precedentemente la stessa chiave ed è tutto a posto.

2. Verifica la firma del certificato o diploma con il seguente comando:

```bash
gpg --verify certificate.txt
```

Questo comando dovrebbe mostrarti dettagli sulla firma, inclusi:

- Chi l'ha firmato (Rete Plan ₿)
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

2. Naviga nella directory che contiene i file del certificato estratti.

3. Esegui il seguente comando per verificare l'open timestamp:

```
ots verify certificate.txt.ots
```

Questo comando:

- Verificherà il timestamp contro la blockchain di Bitcoin
- Ti mostrerà esattamente quando il file è stato timestampato
- Confermerà l'autenticità del timestamp

### Risultati finali

Nota che la verifica è riuscita se vengono visualizzati **entrambi** i seguenti messaggi:

1. La firma GPG è segnalata come **"Buona firma da Plan ₿ Network"**
2. La verifica di OpenTimestamps mostra uno specifico timestamp del blocco Bitcoin e riporta **"Successo! Il blocco Bitcoin [altezza del blocco] attesta che i dati esistevano già al [timestamp]"**

Ora che sai come Plan B Network emette una prova verificabile per qualsiasi Certificato Bitcoin e Diploma di Completamento del Corso, puoi facilmente verificare l'integrità di esso.
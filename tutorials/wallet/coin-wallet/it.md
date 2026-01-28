---
name: Coin Wallet
description: Esercitazioni su Coin Wallet e sui modi per migliorare la privacy e la sicurezza
---

![cover](assets/cover.webp)


Questo tutorial tratta di [Coin Wallet](https://coin.space/) - una crittografia wallet auto-custodiale per dispositivi mobili, e di come aumentare la sicurezza e la privacy quando si utilizzano applicazioni wallet mobili.



## Informazioni su Coin Wallet


**Coin Wallet** è un wallet open-source auto-custodiale/non-custodiale creato da un team di appassionati di Bitcoin nel 2015. È nato come applicazione web, seguita dall'app per iOS nel 2017 e dall'app per Android nel 2020, disponibile su Google Play, Samsung Galaxy Store e Huawei AppGallery.


Vantaggi principali:


- Architettura non detentiva
- Completamente [codice open-source](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Design semplice e pulito
- Concentrato sull'obiettivo principale: archiviare in modo sicuro le criptovalute, senza funzioni inutili
- Supporto multipiattaforma: mobile (iOS e Android), desktop, web
- Supporto RBF (Replace-By-Fee) - velocizza le transazioni bloccate in qualsiasi momento
- Hardware 2FA con chiave [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2
- Supporto Tor integrato: instrada tutto il traffico attraverso la rete Tor per la massima privacy



## 1️⃣ Installazione di Coin Wallet

Coin Wallet è disponibile su tutte le principali piattaforme.



- [App Store iOS](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (AppGallery Huawei)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [APK Android](https://coin.space/api/v3/download/android-apk/any)



- [Tutti i link alle release](https://github.com/CoinSpace/CoinSpace/releases)


Disponibile anche per desktop (Windows, Linux, macOS), come applicazione web e via Tor.


![image](assets/en/01.webp)


## 2️⃣ Creazione di un Wallet e impostazione del PIN


Un wallet viene creato utilizzando un passphrase - una sequenza casuale di 12 parole separate da spazi, generata da un [elenco di 2048 parole](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet supporta passphrase di 12, 15, 18, 21 o 24 parole importate da altri portafogli.


Il passphrase è la forma leggibile dall'uomo della chiave privata principale. Deve essere salvato in modo sicuro. Il passphrase è tutto ciò che serve per accedere al wallet o per ripristinarlo. Se il passphrase viene perso, il wallet e tutti i fondi sono definitivamente persi. Il passphrase non deve mai essere condiviso. Il Coin Wallet non memorizza le chiavi su alcun server o database.


**Un passphrase di 12 parole è sicuro?

Con 2048 parole possibili per posizione, ci sono 2048¹² ≈ 10³⁹ combinazioni - che forniscono ~128 bit di sicurezza, paragonabili alle chiavi private Bitcoin. Questo livello è ampiamente considerato sufficiente. Questo livello è ampiamente considerato sufficiente.


![image](assets/en/02.webp)


Dopo che il passphrase è stato scritto e confermato, l'app chiede di impostare un PIN** di 4 cifre per l'accesso quotidiano. Per maggiore comodità, è possibile attivare l'autenticazione biometrica (impronta digitale o riconoscimento del volto) invece di utilizzare il PIN.


![image](assets/en/03.webp)



Non c'è nessun account, nessun recupero di chiavi, nessun reset del passphrase e nessuna inversione di transazioni. La sicurezza è sotto la piena responsabilità dell'utente.


Per informazioni dettagliate sulle migliori pratiche di salvataggio della frase mnemonica:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Passphrase + PIN. Quando e come si usano


**Quando è richiesto il passphrase?

Solo in questi rari casi:


- Impostazione del wallet su un nuovo dispositivo
- Reinstallazione dell'applicazione Coin Wallet
- Cancellazione dei dati dell'app/browser (Local Storage)
- Rimozione di una chiave hardware dall'account
- Inserire per tre volte il PIN sbagliato (l'app si blocca per sicurezza)


Nell'uso quotidiano, il PIN a 4 cifre è sufficiente per sbloccare il wallet.


**Passphrase + PIN: come funziona**

La passphrase è la vera chiave privata master e funziona su qualsiasi dispositivo.

Poiché digitare ogni volta 12-24 parole sarebbe scomodo, il Coin Wallet utilizza un PIN a 4 cifre per un accesso rapido e quotidiano sul dispositivo corrente.

Un semplice PIN da solo non è abbastanza sicuro per proteggere direttamente la chiave master, quindi non viene mai utilizzato per la crittografia. Invece:



- Il PIN viene inviato al server e scambiato con un lungo token crittografico.
- Questo token decifra la chiave master crittografata memorizzata solo sul dispositivo.


Se il PIN viene immesso in modo errato per tre volte, il server cancella definitivamente il token. La chiave memorizzata localmente diventa inutilizzabile e l'unico modo per recuperare il wallet è inserire il passphrase originale.

Questo design offre sia la convenienza che una forte protezione di ripiego.



## 4️⃣ Ricevere ₿itcoin - Address Tipi e privacy


Il Coin Wallet supporta tutti e tre i formati di indirizzo del Bitcoin:



- SegWit nativo (Bech32)** - inizia con **bc1q** - tariffe più basse, consigliato
- SegWit (P2SH) annidato ** - inizia con **3**
- Legacy (P2PKH)** - inizia con **1**


![image](assets/en/04.webp)


**Perché l'indirizzo cambia dopo ogni deposito?

Questo è intenzionale e protegge la privacy. Ogni volta che si ricevono monete, Coin Wallet genera automaticamente un nuovo indirizzo non utilizzato. Se lo stesso indirizzo venisse riutilizzato (ad esempio, per lo stipendio mensile), chiunque potrebbe facilmente sommare tutte le transazioni in entrata su un blockchain explorer e conoscere il reddito totale.


I vecchi indirizzi rimangono validi per sempre - si può ancora ricevere ad essi - ma l'utilizzo di un nuovo indirizzo ogni volta è la migliore pratica di privacy raccomandata.


**Come ricevere il Bitcoin:**

1. Aprire la moneta

2. Toccare **Ricezione**

3. Scegliere il tipo di indirizzo desiderato (preferibilmente **bc1q** - `Native SegWit`)

4. Mostrare il codice QR o copiare l'indirizzo e inviarlo al pagatore


**Opzionale - Mecto (per i pagamenti di persona):**

Nella stessa schermata di ricezione è presente un pulsante "Mecto".

Quando si accende:


- Vi sarà chiesto di inserire un **nickname** (gravatar)
- La posizione attuale e l'indirizzo di ricezione sono temporaneamente condivisi con altri utenti Coin Wallet che hanno attivato Mecto
- Possono scoprirvi su una piccola mappa e inviare monete senza dover digitare o scansionare


I dati sono visibili solo agli altri utenti di Mecto e vengono cancellati automaticamente dopo 1 ora (o immediatamente quando si spegne).

Mecto è completamente opzionale: lasciatelo disattivato se preferite la massima privacy.


![image](assets/en/05.webp)


## 5️⃣ Invio di ₿itcoin


Per inviare il Bitcoin:


1. Aprire la moneta → toccare **Invio**

2. Incollare l'indirizzo o scansionare il codice QR

3. Immettere l'importo (o toccare **Max**)

4. Scegliere la velocità della transazione:



| Velocità   | Tempo di conferma approssimativo | Livello commissione     |
|---------|---------------------------|---------------|
| **Lento**    | ~120 minuti              | Più basso
| **Predefinito** | ~60 minuti               | Medio
| **Veloce**    | ~20 minuti               | Più alto

5. Confermare con il PIN a 4 cifre → la transazione viene trasmessa


### Come accelerare una transazione di ₿itcoin in sospeso (RBF)


Se si sceglie una tariffa lenta e la transazione è bloccata:


1. Andare alla scheda **Storia

2. Toccare la transazione in sospeso

3. Toccare **Accelerate** (sostituzione a pagamento)

4. Confermare → la transazione sarà ritrasmessa con una tariffa più alta


L'accelerazione RBF è attualmente supportata per:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Ulteriori informazioni su Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Esportazione di chiavi private


**Quando è necessaria una chiave privata?

(il 99% degli utenti non lo fa mai: le 12 parole del passphrase sono sufficienti)



| Situazione                                      | Perché hai bisogno della chiave privata                     |
|------------------------------------------------|--------------------------------------------------|
| Spazzamento di un vecchio portafoglio di carta                   | Per spostare i fondi al tuo portafoglio attuale             |
| Importazione in un firmatario hardware (ad es. Coldcard) | Per la firma offline                              |
| Recupero di emergenza (semenza persa ma app ancora aperta) | Per salvare monete prima che l'app scompaia           |
| Utilizzo di strumenti che non accettano frasi di semenza     | Alcuni utilitari solo di monitoraggio o firma             |

### Come esportare le chiavi private in Coin Wallet


1. Aperto **Bitcoin (BTC)**

2. Scorrere fino alla fine della pagina e toccare **Esporta chiavi private**

3. L'app mostra ogni indirizzo con il saldo e la sua chiave privata in formato **WIF** (inizia con 5, K o L) e un codice QR.


Vengono visualizzati solo gli indirizzi non vuoti.


**Esempio di chiave WIF**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Cosa fare dopo (consigliato)**


- Aprire Electrum, Sparrow, BlueWallet o qualsiasi altro hardware wallet
- Importazione/spazzatura della chiave privata
- Tutti i fondi vengono immediatamente trasferiti a un nuovo indirizzo sicuro nell'ambito dell'attuale seed


Non conservare mai la chiave privata in formato digitale in chiaro. Dopo lo sweeping, può essere eliminata in modo sicuro.


Per una guida completa sulle chiavi private e sui percorsi di derivazione: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Dettagli tecnici - BIP39, BIP32 e percorsi di derivazione


Coin Wallet segue rigorosamente gli standard ufficiali Bitcoin, utilizzati da quasi tutti i portafogli seri.


`BIP39` - come il passphrase diventa la chiave privata principale


- Numero di parole predefinito: 12
- Opzionale passphrase/password: nessuna ("")
- Entropia iniziale: 128 bit (12 parole) → 256 bit (24 parole)
- Implementazione open-source: https://github.com/paulmillr/scure-bip39
- Elenco di parole: elenco standard inglese di 2048 parole
- Supporta l'importazione di frasi di 12, 15, 18, 21 e 24 parole da qualsiasi altro BIP39 wallet


`BIP32 + BIP44/BIP49/BIP84` - generazione deterministica di tutti gli indirizzi

Da un'unica chiave master, il wallet è in grado di generate miliardi di indirizzi in un ordine rigorosamente definito. Ecco perché le stesse 12 parole inserite in Electrum, Sparrow, Trezor, Ledger, BlueWallet, ecc. mostreranno esattamente gli stessi indirizzi e saldi.





**Percorsi di derivazione utilizzati in Coin Wallet per Bitcoin**

| Tipo di indirizzo              | Standard | Percorso di derivazione       | Inizia con | Commento                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| SegWit nativo (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Formato moderno, commissioni più basse           |
| SegWit annidato (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Wrapper di compatibilità per servizi obsoleti |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Formato più vecchio, commissioni più alte          |

All'interno di ogni percorso:


- `/0` - catena esterna (indirizzi indicati per ricevere i pagamenti)
- `/1` - catena interna (modifica degli indirizzi utilizzati dal wallet stesso)


Poiché il Coin Wallet segue questi standard pubblici senza alcuna modifica, i vostri fondi rimarranno recuperabili in qualsiasi altro wallet compatibile anche tra 10-20-30 anni.


## 8️⃣ Migliorare l'anonimato con Tor


**Perché usare Tor in Coin Wallet**

Tor nasconde il vostro vero indirizzo IP ai nodi Bitcoin, agli scambi e agli osservatori.

Tutto il traffico (saldi, transazioni, scambi) passa attraverso la rete Tor - nessuna connessione diretta, nessuna fuga di IP.

Questo è implementato direttamente nel codice sorgente dell'applicazione (vedere [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet ha un indirizzo .onion nascosto e, dalla versione 6.6.3 (dicembre 2024), **il supporto Tor integrato direttamente nell'app mobile**.


### Come attivare Tor su Android e iOS


1. **Installare Orbot** - applicazione ufficiale del Progetto Tor (gratuita)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Aprire Orbot → toccare Start**

Selezionare **Coin Wallet** dall'elenco in modo che solo il wallet utilizzi Tor (opzionale ma consigliato)

Attendere che venga visualizzato il messaggio **"Connected "** (10-30 secondi)


3. **Aprire Coin Wallet → Impostazioni → Rete**

Attivare **Usare Tor**


4. **Verifica stato**

Nella barra superiore appare un'icona a forma di cipolla Tor di colore viola → tutto il traffico è ora instradato attraverso Tor


![image](assets/en/06.webp)


Ecco fatto: il vostro cellulare Coin Wallet è completamente anonimo.


Godetevi la gestione privata delle criptovalute!


## 📝 Conclusione


[Coin Wallet](https://coin.space/) - uno dei veri pionieri del Bitcoin wallet con una storia di sviluppo decennale.

È volutamente semplice e si concentra sulla sua missione principale: conservare in modo sicuro le criptovalute.

Non c'è pubblicità, non c'è news feed, non ci sono abbonamenti, non ci sono funzioni social, non ci sono distrazioni: solo un wallet pulito, veloce e autocustode che fa esattamente quello che deve fare.

Coin Wallet mette al primo posto la semplicità e la sicurezza - da sempre, da sempre.


## 📖 Risorse


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39
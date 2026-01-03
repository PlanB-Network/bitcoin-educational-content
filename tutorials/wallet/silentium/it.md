---
name: Silentium
description: Web progressivo wallet con supporto per i pagamenti silenziosi (BIP-352)
---

![cover](assets/cover.webp)



Il riutilizzo degli indirizzi Bitcoin è una delle minacce più dirette alla riservatezza degli utenti. Quando un beneficiario condivide un unico indirizzo per ricevere più pagamenti, qualsiasi osservatore può tracciare tutte le transazioni associate e ricostruire la sua storia finanziaria. Questo problema riguarda in particolare i creatori di contenuti, gli enti di beneficenza o gli attivisti che desiderano mostrare pubblicamente un indirizzo di donazione senza compromettere la propria privacy.



Silentium risponde a questo problema con un'elegante soluzione accessibile direttamente dal browser. Questa applicazione web progressiva (PWA) open-source, lanciata nel maggio 2024 da Louis Singer, implementa Silent Payments (BIP-352): un indirizzo statico riutilizzabile in cui ogni pagamento finisce su un indirizzo blockchain separato, senza alcuna interazione preliminare o legame osservabile tra le transazioni.



**Avviso importante**: Silentium è un progetto sperimentale che serve come *prova di concetto* per i portafogli leggeri di Silent Payments. Non dovrebbe essere usato come wallet quotidiano o per immagazzinare somme significative. Gli sviluppatori dichiarano esplicitamente che:



> Utilizzare a proprio rischio e pericolo.

Si noti che questo wallet può essere usato come testnet o regtest.



## Che cos'è il Silentium?



### Filosofia e obiettivi



Silentium è una dimostrazione tecnica dell'implementazione di Silent Payments in un browser wallet leggero. Sebbene supporti anche gli indirizzi Bitcoin convenzionali, l'accento è posto su Silent Payments per consentire agli utenti di sperimentare questa tecnologia di privacy in modo semplice.



### Come funzionano i pagamenti silenziosi?



I pagamenti silenziosi (BIP-352) utilizzano la chiave Elliptic Curve Diffie-Hellman Exchange (ECDH). Il destinatario genera un indirizzo statico (`sp1...` su mainnet, `tsp1...` su testnet) composto da due chiavi pubbliche: una chiave di scansione per rilevare i pagamenti e una chiave di spesa per utilizzarli.



Il mittente combina le sue chiavi private di input con la chiave di scansione del destinatario per calcolare un segreto condiviso che genera un "tweak" crittografico. Questo tweak, aggiunto alla chiave di spesa, crea un indirizzo Taproot unico per ogni transazione. Il destinatario riproduce questo calcolo con la sua chiave di scansione privata per individuare e spendere i fondi senza alcuna interazione preliminare.



Vantaggi: maggiore riservatezza per mittente e destinatario, non è necessario un server di terze parti, le transazioni sono indistinguibili dai pagamenti Taproot tradizionali. Svantaggio principale: scansione intensiva della blockchain per rilevare i pagamenti.



Per saperne di più sul funzionamento teorico dei Silent Payments, si veda l'ultima parte del corso BTC,204 su Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Piattaforme supportate



Silentium è una Progressive Web App (PWA) accessibile da qualsiasi browser moderno (mobile o desktop). È possibile utilizzarla direttamente su `app.silentium.dev`, installarla come applicazione nativa tramite il browser o distribuirla localmente. L'installazione avviene direttamente dal browser, senza passare per gli store ufficiali.



## Utilizzo dell'applicazione web



### Accesso e installazione



[Andare a `https://app.silentium.dev/` dal browser] (https://app.silentium.dev/). L'applicazione si carica immediatamente e visualizza la schermata iniziale.



Per installarlo come applicazione nativa su iOS, premere il pulsante di condivisione (quadrato con freccia verso l'alto) e selezionare "Sulla schermata iniziale". Su Android, il browser di solito offre direttamente una notifica "Aggiungi alla schermata iniziale". Una volta installato, Silentium appare con la sua icona dedicata e funziona come un'applicazione nativa, ma richiede una connessione a Internet per sincronizzare le transazioni.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Creazione del portafoglio



Al primo avvio, scegliere "Crea Wallet" per creare un nuovo portfolio o "Ripristina Wallet" per ripristinare da una frase di ripristino esistente.



Selezionare "Crea Wallet". L'applicazione genera una frase di 12 parole che dovete annotare con cura. Questa frase è l'unico modo per recuperare i fondi. Anche su testnet, adottare buone pratiche di backup. Premere "Continua" dopo aver salvato la frase.



L'applicazione chiede poi di impostare una password per proteggere l'accesso al wallet. Scegliere una password forte e confermarla.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Una volta confermata la frase e impostata la password, si accede all'interfaccia principale.



### Principali e parametri del Interface



L'interfaccia principale visualizza il saldo in satoshi (inizialmente 0 sats), con tre pulsanti in basso:




- Sync**: sincronizza wallet con la blockchain
- Ricevere**: ricevere fondi
- Invia**: per inviare bitcoin



Accedere alle Impostazioni tramite l'icona in alto a destra (tre barre orizzontali). Il menu Impostazioni offre diverse opzioni:





- Informazioni su**: informazioni sull'applicazione
- Backup**: backup della frase di recupero
- Explorer**: selezionare blockchain explorer (Mempool per impostazione predefinita) e il server Silentiumd
- Rete**: selezione della rete (mainnet/testnet)
- Password**: modifica della password
- Ricarica**: ricarica del wallet
- Reset**: reset completo
- Tema**: cambiare il tema



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



La sezione **Explorer** è particolarmente importante: consente di scegliere il blockchain explorer utilizzato (Mempool per impostazione predefinita) e visualizza anche l'URL del server Silentiumd (`https://bitcoin.silentium.dev/v1` per mainnet). Se si ospita un proprio server Silentiumd o si desidera utilizzare testnet, è qui che si configurano questi parametri.



### Ricezione di fondi



Dall'interfaccia principale, premere il pulsante "Ricevi". Per impostazione predefinita, Silentium visualizza l'indirizzo di Silent Payment con il relativo codice QR. L'indirizzo inizia con `sp1...` su mainnet o `tsp1...` su testnet.



È possibile passare dal pagamento silenzioso all'indirizzo classico di Bitcoin utilizzando il pulsante "Passa all'indirizzo classico" / "Passa all'indirizzo silenzioso" nella parte inferiore della schermata.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Una volta trasmessa la transazione, si prega di attendere qualche minuto. Per i pagamenti silenziosi, Silentium scansiona automaticamente la blockchain alla ricerca di transazioni a voi destinate. Le transazioni appaiono con lo stato "Non confermate" prima di essere progressivamente confermate.



### Inviare un pagamento



Dall'interfaccia principale, premere il pulsante "Invia". La schermata di invio vi chiederà :



1. **Address**: incollare un indirizzo Silent Payment (`sp1...` o `tsp1...`) o un indirizzo Bitcoin classico. È possibile utilizzare l'icona QR scan per scansionare un indirizzo.


2. **Importo**: inserire l'importo in satoshi da inviare. Per facilitare l'inserimento, viene visualizzato un tastierino numerico. Il saldo disponibile viene visualizzato in alto come riferimento.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Una volta inseriti l'indirizzo e l'importo, premere "Procedi" per continuare. L'applicazione chiederà di selezionare il livello di commissione desiderato prima di confermare la transazione.



## wallet self-hosting



### Perché fare self-hosting?



L'hosting locale di Silentium offre sovranità totale, verifica del codice, un ambiente di sviluppo e resilienza di fronte ai guasti del sito ufficiale.



### Prerequisiti



Node.js (versione 14+), npm o yarn, Git e circa 500 MB di spazio su disco.



### Installazione locale



Clonare il repository e installare il file :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Avvio e utilizzo



Avviare l'applicazione in modalità di sviluppo:



```bash
yarn start
```



Andate su `http://localhost:3000` nel vostro browser. Per una versione di produzione ottimizzata :



```bash
yarn build
```



I file generati in `build/` possono essere serviti con nginx, Apache o qualsiasi altro server web. Per impostazione predefinita, Silentium si connette al server pubblico `bitcoin.silentium.dev`. Modificare questa impostazione nei parametri per utilizzare testnet o il proprio server.



## Il server Silentiumd



### Ruolo e funzionamento



Silentium utilizza un server di indicizzazione **Silentiumd** per ottimizzare il rilevamento dei pagamenti. La scansione di tutte le transazioni Taproot sarebbe troppo complessa per un browser o un telefono cellulare.



Silentiumd precalcolerà i dati intermedi (tweaks) per ogni transazione Taproot. Il vostro wallet scaricherà questi tweaks (pochi byte per transazione) ed eseguirà il calcolo finale in locale. Il vostro wallet scarica questi tweak (pochi byte per transazione) ed esegue il calcolo finale a livello locale, verificando la proprietà del pagamento. Il server non conosce mai le vostre chiavi né può identificare le vostre transazioni, a differenza dei server Electrum convenzionali.



I filtri compatti BIP158 consentono al vostro wallet di determinare quali blocchi scansionare senza rivelare i vostri indirizzi, preservando così la vostra riservatezza.



### Server pubblico



Il server pubblico `bitcoin.silentium.dev` (mainnet), sponsorizzato da Vulpem Ventures, offre un'esperienza semplice e immediata. Sebbene la riservatezza sia preservata, questo approccio implica una relativa fiducia nell'infrastruttura di terzi.



### Ospitate il vostro server Silentiumd



Per una sovranità totale, ospitate il vostro server Silentiumd. Prerequisiti: Nodo Bitcoin Core non elagged con `txindex=1` e `blockfilterindex=1`, Go 1.21+, 10-20 GB di spazio su disco, capacità di amministrazione del sistema.



**Installazione:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Configurare tramite variabili d'ambiente (vedere `config.md' del repository per i dettagli). Il server indicizza la blockchain ed espone un API che può essere interrogato dal wallet.



Attualmente non esistono soluzioni pacchettizzate per Umbrel o Start9, il che limita l'accessibilità agli utenti non tecnici.



## Vantaggi e limiti



### Punti salienti





- Massima accessibilità**: utilizzo da qualsiasi browser, senza necessità di installazioni pesanti
- Multipiattaforma**: funziona su mobile (Android/iOS) e desktop grazie alla tecnologia PWA
- Semplice self-hosting**: installazione locale possibile con pochi comandi
- Open-source**: codice completamente verificabile su GitHub
- Attenzione alla privacy**: nessun tracciamento, nessuna analisi, calcoli crittografici locali
- Architettura separata**: netta separazione tra wallet (client) e server di indicizzazione
- Senza account**: non è richiesta alcuna registrazione o dato personale



### Vincoli da considerare





- Progetto sperimentale**: solo prova di concetto, non destinato all'uso quotidiano o alla produzione
- Nessuna garanzia**: rischio di bug, vulnerabilità, possibile perdita di fondi
- Supporto limitato**: poca documentazione per l'utente, comunità ristretta, nessun supporto ufficiale
- Dipendenza dal server**: richiede un server Silentiumd funzionante (pubblico o self-hosted)
- Scansione intensiva**: Il rilevamento silenzioso dei pagamenti consuma larghezza di banda
- Funzionalità ridotte**: nessun controllo delle monete, nessun Lightning, nessuna multi-firma



## Le migliori pratiche



### Sicurezza seed



Anche su Testnet, prendete sul serio la vostra frase di recupero. Scrivetela e conservatela in un luogo sicuro. Tenete portafogli separati per testnet e mainnet: non utilizzate mai un seed di prova su un wallet destinato a fondi reali.



### Verifica del codice sorgente



Uno dei vantaggi del self-hosting è la possibilità di controllare il codice sorgente prima di eseguirlo. Se avete intenzione di utilizzare Silentium con fondi reali, prendetevi il tempo di verificare il codice o chiedete a uno sviluppatore fidato di farlo. Confrontate anche l'hash del codice distribuito su `app.silentium.dev` con quello del repository GitHub per assicurarne l'autenticità.



### Backup e ripristino



Il recupero dei fondi Silent Payments richiede un wallet compatibile con il protocollo BIP-352. Un wallet standard non può eseguire la scansione della blockchain per recuperare i Silent Payments UTXO. Mantenete Silentium installato o assicuratevi di avere accesso a un altro wallet compatibile (come il Cake Wallet o altre implementazioni future) per ripristinare i vostri fondi se necessario.



## Conclusione



Silentium offre un terreno di prova accessibile per comprendere i pagamenti silenziosi senza attriti tecnici. Come prova di concetto, dimostra come questa tecnologia per la privacy possa essere integrata in un browser wallet preservando l'autocustodia. Sperimentate su testnet per scoprire questa promettente svolta per la privacy del on-chain.



## Risorse



### Documentazione ufficiale




- Repository GitHub Silentium (wallet): https://github.com/louisinger/silentium
- Repository GitHub di Silentiumd (server): https://github.com/louisinger/silentiumd
- Applicazione web: https://app.silentium.dev/
- Sito della comunità Silent Payments: https://silentpayments.xyz
- Specifica BIP-352: https://bips.dev/352



### Articoli e risorse




- Annuncio ufficiale (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Pagamenti silenziosi: https://bitcoinops.org/en/topics/silent-payments/



### Strumenti Testnet




- Rubinetto Testnet: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet
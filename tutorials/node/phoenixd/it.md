---
name: Phoenixd
description: Distribuire il proprio nodo Lightning minimalista con Phoenixd
---

![cover](assets/cover.webp)



Autonomia finanziaria significa anche controllo della propria infrastruttura Lightning. Per gli sviluppatori e le aziende che desiderano integrare Bitcoin Lightning nelle loro applicazioni, **Phoenixd** rappresenta la soluzione ideale: un nodo Lightning minimalista e specializzato con gestione automatica della liquidità.



Phoenixd è un server Lightning sviluppato da ACINQ, progettato specificamente per inviare e ricevere pagamenti Lightning tramite un'API HTTP. A differenza di implementazioni complete come LND o Core Lightning, Phoenixd astrae tutta la complessità della gestione dei canali, preservando l'autoprotezione dei fondi.



In questa guida vedremo come installare, configurare e utilizzare Phoenixd per sviluppare applicazioni Lightning con un'infrastruttura self-hosted e un'API facile da usare.



## Che cos'è Phoenixd?



Phoenixd è un nodo Lightning minimale e specializzato sviluppato da ACINQ. È una soluzione pensata per gli sviluppatori e le aziende che desiderano integrare Lightning nelle loro applicazioni senza la complessità di gestione di un Full node.



### Principio di funzionamento



**Phoenixd è un nodo Lightning minimo che utilizza ACINQ come LSP (Lightning Service Provider) per la liquidità automatica. Quando riceve pagamenti Lightning, apre automaticamente i canali con i nodi ACINQ per allocare la necessaria capacità in entrata. Questa liquidità "al volo" è istantanea, ma viene addebitata esattamente all'**1% + commissioni Mining** dell'importo ricevuto.



**Gestione automatizzata:** Il sistema gestisce tre Elements fondamentali:




- Canali Lightning**: Apertura, chiusura e gestione automatica in base alle esigenze
- Liquidità in entrata e in uscita**: Approvvigionamento automatico tramite splicing e apertura del canale
- Credito a pagamento** : I piccoli pagamenti insufficienti a giustificare un canale vengono memorizzati come accantonamento per spese future



### Vantaggi di Phoenixd



**Controllate le vostre chiavi private (seed di 12 parole) e i vostri fondi. Phoenixd genera localmente il vostro Wallet senza mai condividere le vostre chiavi.



**Infrastruttura personale:** Phoenixd viene eseguito sul vostro server, dandovi accesso a registri dettagliati, configurazione e controllo API. Non dipendete più da un servizio di terzi per l'accesso ai vostri fondi.



**API integrata:** Phoenixd dispone di un'API HTTP per l'integrazione con altri servizi, il supporto nativo di LNURL e lo sviluppo di applicazioni personalizzate.



**Grazie alla sua semplice API REST, Phoenixd può essere integrato in qualsiasi applicazione o servizio che richieda pagamenti Lightning.



**Nota importante:** La liquidità automatica proviene ancora da ACINQ come LSP (Lightning Service Provider). Phoenixd utilizza lo stesso meccanismo di Phoenix mobile per la gestione automatica dei canali.



## Installazione di Phoenixd



### Prerequisiti



Phoenixd richiede un ambiente Linux (consigliato Ubuntu/Debian), con alcune conoscenze di base della riga di comando. Per ottenere prestazioni ottimali, avrete bisogno di :





- Server Linux**: VPS o macchina locale con connessione stabile
- OpenJDK 21** : Ambiente runtime Java
- Connessione Internet stabile**: Per la sincronizzazione con il Lightning Network
- Nome di dominio** (opzionale) : Per l'accesso sicuro HTTPS all'API



### Download e installazione



**1. Scaricare Phoenixd**



Andare alla pagina [GitHub releases](https://github.com/ACINQ/phoenixd/releases) e scaricare l'ultima versione per la propria architettura:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Primo avvio



Avviare Phoenixd per l'inizializzazione:



```bash
./phoenixd
```



Al primo avvio, vi verrà chiesto di confermare due passaggi importanti digitando "Ho capito":



**Messaggio 1 - Backup:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Conservate queste 12 parole**: sono la vostra unica garanzia di guarigione.



**Messaggio 2 - Liquidità automatica:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Digitare "Ho capito" per ogni conferma.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd si avvia per la prima volta: conferme di backup e liquidità automatica*



**3. Configurazione in servizio** (solo in francese)



Per il funzionamento continuo, creare un file systemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Il servizio Phoenixd è attivo e operativo tramite systemd e `auto-liquidità` a 2m sat*



## Configurazione e sicurezza



### File di configurazione



Phoenixd crea automaticamente `~/.phoenix/phoenix.conf` con i parametri essenziali:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**Parametri chiave:**




- `auto-liquidità`: Dimensione dei canali aperti automaticamente (default: 2M Sats)
- http-password`: Password di amministrazione per l'API (creazione di Invoice E invio di pagamenti)
- http-password-limited-access`: Password limitata (solo per la creazione di Invoice)



### Accesso sicuro con HTTPS



Per impostazione predefinita, l'API di Phoenixd è accessibile solo tramite HTTP locale (`http://127.0.0.1:9740`). Per utilizzare il nodo dall'esterno (applicazioni mobili, altri server, integrazioni web), è necessario configurare un accesso HTTPS sicuro.



**Principio del proxy inverso:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** agisce come **proxy inverso**: ascolta le richieste HTTPS da Internet sulla porta 443, le reindirizza a Phoenixd localmente (porta 9740), quindi invia le risposte crittografate al cliente.



**Il certificato SSL/TLS** è un file digitale che :




- Dimostrare l'identità del server** (previene gli attacchi man-in-the-middle)
- Abilita la crittografia HTTPS**: tutti i dati, comprese le password API, vengono crittografati durante il trasporto
- Rilasciato gratuitamente** da Let's Encrypt tramite lo strumento certbot



Questa configurazione consente di :




- Accesso sicuro all'API da Internet**
- Crittografare le password API** durante il trasporto (per evitare che vengano trasmesse in chiaro)
- Integrare Phoenixd** in applicazioni esterne che richiedono HTTPS
- Conformità agli standard di sicurezza** per le API finanziarie



Configurare questo reverse proxy HTTPS con nginx :



**1. Configurazione di Nginx**



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. Certificato SSL**



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Test di funzionamento



Verificare che Phoenixd funzioni correttamente:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Questi comandi dovrebbero restituire informazioni JSON sullo stato e sul bilancio del nodo (inizialmente vuoto).



![Commandes CLI](assets/fr/03.webp)



*Comandi getinfo e getbalance per verificare lo stato dei nodi*



## Utilizzo dell'API



### Primo test di ricezione



**1. Creare un fulmine** Invoice



Utilizzare l'API per creare il primo Invoice:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Comprendere il meccanismo automatico di liquidità



**Principio fondamentale:** Quando si riceve un pagamento Lightning, Phoenixd deve talvolta aprire un nuovo canale per poterlo ricevere. L'apertura di questo canale costa una tassa che viene **automaticamente** detratta dall'importo ricevuto.



**Esempio concreto con 100.000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Primo test di accettazione: Sats 100k ricevuti, saldo finale di Sats 75.561 dopo la deduzione dei costi di liquidità*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Calcolo del canone:**




- Costo del servizio**: 1% della capacità del canale (2.115.000 Sats) = 21.150 Sats
- Commissioni Mining**: ~3.289 Sats (per la transazione On-Chain)
- Totale**: 24.439 Sats dedotto automaticamente



**Verifica con i comandi CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Saldo finale dopo l'invio del pagamento: 257 Sats rimanenti dopo la spedizione di Lightning*



**Se si ricevono pagamenti troppo piccoli per giustificare l'apertura di un canale (< circa 25k Sats), essi vengono memorizzati in un "credito di quota" non rimborsabile. Questo credito sarà utilizzato per pagare le future tasse di canale quando ne riceverete una quantità sufficiente.



**2. Seguire l'apertura del canale**



Osservare i registri di Phoenixd:



```bash
journalctl -u phoenixd -f
```



Vedrete l'apertura del canale e la deduzione automatica delle commissioni di liquidità. Le commissioni variano in base alle condizioni del Mempool Bitcoin, ma includono sempre una commissione di servizio dell'1% più la commissione Mining corrente.



**3. Controllare il canale**



```bash
./phoenix-cli listchannels
```



Questo comando visualizza i canali attivi con il loro stato e il loro bilancio.



### Operazioni API complete



Phoenixd espone un'API REST sulla porta 9740 che consente :



**Operazioni di base:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Importante sui costi:**




- Ricezione**: 1% + commissione Mining per la liquidità automatica
- Spedizione**: 0.4% di spese di spedizione per il Lightning Network



**Webhooks:** I webhooks consentono a Phoenixd di notificare **automaticamente** le vostre applicazioni quando si verifica un evento (pagamento ricevuto, Invoice pagato, canale aperto, ecc.). Invece di chiedere continuamente aggiornamenti a Phoenixd, la vostra applicazione riceve una notifica HTTP istantanea.



**Il vostro negozio online riceve automaticamente una notifica quando un cliente paga un ordine, consentendo la convalida immediata della transazione.



Configurazione in `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Applicazioni avanzate



### Integrazioni LNURL



Phoenixd supporta nativamente i protocolli LNURL per un'integrazione avanzata:



**LNURL-Pay:** Pagare per i servizi compatibili con LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Recuperare i fondi dai servizi LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Autenticazione tramite Lightning per accedere ai servizi


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integrazione con LNbits



LNbits può utilizzare Phoenixd come fonte di finanziamento secondo la sua [documentazione ufficiale](https://docs.lnbits.org/guide/wallets.html):



**Configurazione di LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Questa integrazione consente di creare sottoconti LNbits alimentati dal vostro nodo Phoenixd, fornendo un Interface basato sul web per la gestione di più portafogli Lightning.



### Applicazioni personalizzate



Grazie alla sua API REST completa, è possibile sviluppare :



**E-commerce:** Integrazione diretta dei pagamenti Lightning nel vostro negozio


**Servizi di donazione:** Sistemi di donazione con fatture e webhook automatici


**Bot per social network:** Bot per Telegram/Discord con funzioni di suggerimento


**Paywall Lightning:** Contenuti premium disponibili a pagamento Lightning



## Sicurezza e buone pratiche



### Protezione dell'accesso



**Password delle API: ** Le password generate automaticamente sono le chiavi del vostro tesoro Lightning. Non condividetele mai e cambiatele in caso di dubbio.



**Firewall:** Non lasciare mai la porta 9740 aperta direttamente a Internet. Utilizzare sempre nginx con HTTPS.



**Autenticazione avanzata:** Considerate una VPN o una Tailscale per limitare l'accesso al vostro server solo ai dispositivi autorizzati.



### Backup essenziali



**Recupero seed:** Salvate le vostre 12 parole in un luogo sicuro, fuori dal server. Questa è l'unica garanzia di recupero.



*~/.phoenix: ** Eseguire regolarmente il backup di questa cartella (dopo che Phoenixd è stato spento) per preservare lo stato del canale e accelerare il ripristino.



**Codici di recupero dei servizi:** Conservate anche i codici di backup di tutti i servizi per i quali avete attivato la 2FA con il vostro Phoenix.



### Monitoraggio e manutenzione



**Registri di monitoraggio:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Aggiornamenti:** Osservare [GitHub releases](https://github.com/ACINQ/phoenixd/releases) per le nuove versioni. L'aggiornamento è semplice come la sostituzione del binario e il riavvio del servizio.



## Confronto con le alternative



### Phoenixd vs Phoenix standard



**Standard Phoenix (mobile) :**




- ✅ Installazione immediata, zero configurazione
- ✅ Interface mobile intuitivo
- ✅ Stesso salvataggio automatico di Phoenixd
- ❌ Nessuna API per gli sviluppatori
- ❌ Nessun accesso ai registri dettagliati



**Phoenixd (server) :**




- aPI HTTP per le integrazioni
- accesso completo ai registri
- infrastruttura personale
- richiede competenze tecniche
- ❌ È necessaria la manutenzione del server



**Entrambi utilizzano ACINQ come LSP per la liquidità automatica.



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- controllo totale, protocollo Lightning completo
- ✅ Grande comunità, ecosistema maturo
- ❌ Gestione manuale complessa della liquidità
- ❌ Ampia curva di apprendimento



**Phoenixd :**




- ✅ Gestione automatica della liquidità (come Phoenix mobile)
- aPI per gli sviluppatori
- ✅ Configurazione semplificata
- ❌ Utilizza ACINQ come LSP (nessun instradamento indipendente)
- ❌ Meno flessibile rispetto ai nodi completi



## Risolvere i problemi più comuni



### Problemi di accesso all'API



*errore "*Autenticazione fallita":**


1. Controllare la password nel file `~/.phoenix/phoenix.conf`


2. Controllare il formato di autenticazione `-u:password`


3. Assicurarsi che Phoenixd sia in esecuzione (`./phoenix-CLI getinfo`)



**Timeout di connessione:**




- Verificare che Phoenixd sia in ascolto sulla porta corretta (9740)
- Testare l'accesso locale prima di configurare HTTPS
- Controllare i log: `journalctl -u phoenixd -f`



### Problemi di liquidità



**I pagamenti non arrivano :**


1. Verificare che l'importo superi la soglia minima (~30k Sats)


2. Consultare i log per identificare gli errori del canale


3. Riavviare Phoenixd se necessario



**Saldo in "credito di spesa":**


I piccoli pagamenti vengono memorizzati come accantonamento. Se si riceve un importo maggiore, si attiva l'apertura del canale e si sbloccano i fondi.



## Conclusione



Phoenixd rappresenta un ottimo compromesso tra facilità d'uso e sovranità tecnica per gli sviluppatori. Offre un'API Lightning semplice ma potente con gestione automatica della liquidità, eliminando la complessità dei nodi Lightning tradizionali.



Questa soluzione è particolarmente adatta agli sviluppatori e alle aziende che desiderano :




- Integrate Bitcoin Lightning nelle vostre applicazioni
- Evitare la complessità della gestione del canale Lightning
- Beneficiare di un'infrastruttura self-hosted
- Un'API semplice e affidabile



Con Phoenixd, costruite la vostra infrastruttura Lightning privata con una moderna API REST e la gestione automatica degli aspetti tecnici. È la soluzione ideale per democratizzare l'integrazione di Lightning nei vostri progetti.



## Risorse utili



### Documentazione ufficiale




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Codice sorgente e release
- Sito di Phoenix Server**: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Documentazione completa
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Domande frequenti



### Sostegno della comunità




- Problemi GitHub** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Supporto tecnico
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Notizie e annunci
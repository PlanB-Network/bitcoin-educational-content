---
name: Lightning Smoke Machine
description: Attivare una macchina del fumo con un pagamento Lightning tramite ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)


## Introduzione

Trasforma una classica macchina del fumo in un dispositivo pagabile in bitcoin via Lightning Network. Ogni pagamento innesca automaticamente un getto di fumo!

- Livello: intermedio.
- Tempo stimato: 2-3 ore.
- Casi d'uso: eventi Bitcoin, performance artistiche, dimostrazioni Lightning, effetti scenici automatizzati.


## Prerequisiti

### Conoscenza

 - Elettronica di base (cablaggio, relè)
 - Saldatura (o utilizzo di connettori Dupont)
 - Configurazione della rete (WiFi, WebSocket)

### Conti richiesti

- Server BTCPay: istanza funzionale (self-hosted o hosted).
- Blink Wallet: conto + accesso API.

### Accesso

- Accesso amministrativo al server BTCPay.
- Connessione WiFi per ESP32.


## Materiali necessari

### Hardware - Componenti elettronici

- 1 microcontrollore - ESP32-WROOM-32

*L'ESP32-WROOM-32 è un microcontrollore WiFi/Bluetooth compatto e a basso costo per collegare dispositivi elettronici a internet e controllarli a distanza*

![ESP32](assets/fr/1.webp)

- 1 Modulo relè - 5V con optoaccoppiatore

*Un relè è come un interruttore che l'ESP32 può azionare per accendere o spegnere la macchina del fumo*

![relay](assets/fr/2.webp)

- ~10 cavi Dupont - maschio/maschio e maschio/femmina

![dupont-cables](assets/fr/3.webp)

- 1 Alimentazione per ESP32 - 5V USB o batteria Li-Po

![battery](assets/fr/4.webp)

- 1 cavo micro-USB - collegamento tra l'ESP32 e l'alimentatore

![micro-usb-cables](assets/fr/5.webp)

- 1 macchina nebbiogena da 220V con telecomando a batteria da 12V

![remote-and-smoke-machine](assets/fr/6.webp)

- 1 flacone di liquido compatibile con la macchina del fumo

### Hardware - Strumenti

- Saldatore + stagno (se si salda).
- Cacciavite.
- Multimetro (consigliato).

### Software

- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**.
- Browser web compatibile con WebSerial (Chrome/Edge/Brave).
- Server BTCPay configurato. Per ulteriori informazioni sulla creazione di un'istanza del server BTCPay, visita questo tutorial:

https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc).


## Architettura del sistema

![architecture-lightning-smoke-machine](assets/fr/7.webp)

---

**⚠️** **AVVERTENZA DI SICUREZZA - LEGGERE PRIMA DI CONTINUARE** **⚠️**

Questo progetto prevede una macchina per nebbia collegata a una **alimentazione di rete a 220 V**. Un funzionamento improprio può provocare **una folgorazione mortale** o un **incendio**.

**Regole non negoziabili**:
1. **Scollega SEMPRE la macchina del fumo dalla rete elettrica** prima di aprire il telecomando o manomettere il cablaggio.
2. **Rimuovi la batteria dal telecomando** prima di maneggiarla (rischio di cortocircuito e di danni ai componenti).
3. **Verifica che tutte le connessioni siano isolate** prima di ricollegare qualsiasi cosa.
4. **Non ricollegare mai la 220V** prima che la scatola del telecomando sia stata chiusa e fissata.

Se non sei a tuo agio con questo tipo di manipolazione, porta con te qualcuno che lo sia.

---


## PARTE 1: Assemblaggio dell'hardware

### Fase 1: preparazione del telecomando

Obiettivo: Collega il relè al pulsante ON/OFF del telecomando

1. Apri il telecomando
    - Identifica il pulsante ON/OFF.
    - Svita la custodia per aprire il telecomando.

2. Individua le connessioni
   - Individua i terminali + e - dell'alimentatore.
   - Test di continuità con un multimetro (opzionale).

![smoke-machine-remote](assets/fr/8.webp)

3. Cablaggio dei pulsanti (saldature o connettori)
    - Salda un cavo nero al terminale `-` del pulsante.
    - Salda un cavo rosso al terminale comune `+`.

![smoke-machine-remote](assets/fr/9.webp)

### Fase 2: Collegamento al modulo relè

**Ricorda: Terminologia dei relè**

| **Terminale**           | **Descrizione**                              | **Funzione**                        |
| ----------------------- | -------------------------------------------- | ----------------------------------- |
| NO (Normalmente Aperto) | Circuito aperto per impostazione predefinita | Si chiude quando il relè è attivato |
| NC (Normalmente Chiuso) | Circuito chiuso per impostazione predefinita | Si apre quando il relè è attivato   |
| COM (Comune)            | Terminale centrale                           | Commuta tra NO e NC                 |

**Cablaggio dal telecomando al modulo relè**:
- Filo nero dal pulsante ON/OFF **→** NO (normalmente aperto).
- Filo rosso (comune) **→** COM (comune).

**Logica**:
- Quando l'ESP32 attiva il relè, collega COM e NO, il che equivale esattamente a premere il pulsante del telecomando.
- Quando l'ESP32 interrompe il relè, COM e NO si separano, il che equivale a rilasciare il pulsante.

![remote-relay](assets/fr/10.webp)

### Fase 3: collegamento dell'ESP32 al modulo relè

**Schema di cablaggio:**

| **ESP32** | **→** | **Modulo Relè** |
| --------- | :---: | --------------- |
| V5 (5V)   | **→** | VCC             |
| GND       | **→** | GND             |
| GPIO 21   | **→** | IN (Ingresso)   |

**Verifica**:
- VCC e GND ben collegati (polarità).
- GPIO 21 utilizzato per il segnale di controllo.
- Nessun cortocircuito visibile.

![relay-esp32](assets/fr/11.webp)

**Frequenza del punto di controllo**

Prima di passare al software, controlla:
- Telecomando correttamente cablato.
- Modulo relè collegato all'ESP32.
- Nessun filo scoperto che tocchi altri componenti.
- 220V sempre scollegato.

![relay-esp32](assets/fr/12.webp)

---


## PARTE 2: Configurazione del software

Utilizzeremo *Blink* come esempio, ma *BTCPay Server* offre anche *Strike, Breez e Boltz* se preferite un'altra opzione.

### Passo 1: Plugin, installazione *BitcoinSwitch* + *Blink*

1 - Accedi all'istanza del proprio *Server BTCPay* con un account di amministratore.

2 - Crea il primo store.

3 - Sul lato sinistro di *BTCPay Server*, scorri fino in fondo e vai su *"Manage Plugins"*.

![btcpay-plugins](assets/fr/13.webp)

4 - Installeremo i plugin *BitcoinSwitch* e *Blink*.

![btcpay-plugins](assets/fr/14.webp)

5 - Scorri l'elenco dei plugin e cliccare su *"Installa "*: *BitcoinSwitch e Blink* (o il wallet disponibile a tua scelta).

![btcpay-plugins](assets/fr/15.webp)

6 - Una volta completata l'installazione, riavvia *BTCPay Server* e attendi 1 minuto per il riavvio dell'istanza.

![btcpay-plugins](assets/fr/16.webp)

7 - Quando torni a *"Manage Plugins"*, verifica che entrambi i plugin siano stati installati.

![btcpay-plugins](assets/fr/17.webp)

### Passo 2: Backend: configurazione del *server BTCPay + Blink

**1 - Creare un wallet *Blink***

- Visita https://www.blink.sv.
- Crea il tuo account. Consulta il tutorial :

https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

**2 - Generazione di una chiave API *Blink***

- Accedi all'interfaccia dell'API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** e accedi con lo stesso account utilizzato per creare il wallet *Blink*.

![blink-api](assets/fr/18.webp)

- Una volta collegato, vai alla scheda *chiavi API*.

![blink-api](assets/fr/19.webp)

- Clicca su *+* nell'angolo in alto a destra per accedere alla configurazione della chiave API.

![blink-api](assets/fr/20.webp)

- Assegna un nome alla chiave API e lascia le impostazioni predefinite. Poi, nel terzo passo, annota la tua chiave API - la vedrai solo una volta: `blink_mZ5KxxxxxxxxxNbmX`

![blink-api](assets/fr/21.webp)

- Una volta creata, dovrebbe apparire nell'elenco delle chiavi API attive.

![blink-api](assets/fr/22.webp)

**3 - Collegare *Blink* al *Server BTCPay***

- Apri il tuo *Server BTCPay*.
- Vai a: *Wallet* **→** *Lightning*.

![btcpay-server](assets/fr/23.webp)

- Fai clic su *Usa un nodo personalizzato*.
- Incolla la seguente stringa di connessione:
- 
```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```

**⚠️** **Importante**:

- Non modificare la prima parte: `type=blink;server=https://api.blink.sv/graphql`;
- Sostituisci solo:
    - api-key= *con la tua chiave API Blink*.
    - wallet-id= *dal tuo wallet Blink* ID.
- Quindi fai clic su *Test connection*, poi su *Save*.

![btcpay-server](assets/fr/24.webp)

- Verifica che la connessione sia stabilita (stato verde).

![btcpay-server](assets/fr/25.webp)

**4 - Creare un punto vendita (PoS)**

- In BTCPay Server, vai alla scheda *Plugins* e clicca su *Point of sale*.

![btcpay-server](assets/fr/26.webp)

- Dai un nome al tuo PoS e cliccate su *Create*.

![btcpay-server](assets/fr/27.webp)

- Configurazione PoS:
    - Scegli lo stile del punto vendita = *Print display*.
    - Valuta = *SATS*
    - Fai clic su *Save*.

![btcpay-server](assets/fr/28.webp)

- Configurazione del prodotto:
    - Elimina tutti i prodotti predefiniti.
    - Poi cliccate su *add item*.

![btcpay-server](assets/fr/29.webp)

![btcpay-server](assets/fr/30.webp)

- Configura il prodotto:
    - Titolo: *macchina del fumo*.
    - Prezzo: *10 sats*.
    - Interruttore GPIO Bitcoin: 21.
    - Bitcoin durata commutazione (in millisecondi): 5000.
    - Fai clic su *Close* e poi su *Save* per salvare il nuovo prodotto.

![btcpay-server](assets/fr/31.webp)

### Fase 3: Firmware: Flashing dell'ESP32

**1 - Vai al sito flash**

- Vai a: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)

![bitcoinswitch-lnbits](assets/fr/32.webp)

**2 - Flash il firmware di BitcoinSwitch**

- Collega l'ESP32 al computer con il cavo USB/Micro-USB.
- Quindi fai clic su *Connect to Device*.
- Si apre una finestra, seleziona la porta USB dell'ESP32, quindi fare clic su *Connect*.

![bitcoinswitch-lnbits](assets/fr/33.webp)

- Una volta collegato l'ESP32, si procederà a flashare il firmware di BitcoinSwitch. Nella sezione *T-Display*, clicca su *Upload Firmware* per l'ultima versione disponibile (attualmente: *bitcoinSwitch T-Display v1.0.1*).

![bitcoinswitch-lnbits](assets/fr/34.webp)

- Attendi il caricamento, il processo è completo quando i log mostrano *"Leaving..."*.

![bitcoinswitch-lnbits](assets/fr/35.webp)

- Scollega l'ESP32.

**3 - Controlla l'installazione del firmware di BitcoinSwitch**

- Ricarica la pagina: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/).
- Ricollega l'ESP32 al computer con il cavo USB/Micro-USB.
- Quindi fai clic su *Connect to device*.
- Seleziona la porta USB del tuo ESP32, quindi fai clic su *Connect* come descritto sopra.
- Una volta collegato, premi il pulsante **RESET** sull'ESP32.
- Controlla nei log che le ultime righe mostrino:

```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```

(Questo è normale, significa che non c'è ancora una configurazione, ma che il firmware è stato installato)

![bitcoinswitch-lnbits](assets/fr/36.webp)

**4 - Generare l'URL LNURL** di WebSocket

Formato finale previsto:

```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```

Fasi di generazione:
- Apri l'istanza del server BTCPay, quindi accedi al PoS creato in seguito.
- Clicca quindi su "Visualizza" per aprire il PoS nel browser

![btcpay-server-https](assets/fr/37.webp)

- Copia l'URL della pagina, ad esempio:

![btcpay-server-https](assets/fr/38.webp)

Scomponiamo questo URL:

```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```

- `XXXXv` → il dominio della tua istanza del server BTCPay.
- `46XXXXXXXXXXXXXXXXwFB` → il tuo identificativo univoco PoS.
- `/pos` → indica un punto vendita.

Cambialo:
- Sostituisci `https://` con `wss://`.
- Aggiungi `/bitcoinswitch` alla fine.

Risultato:

```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```

Conserva questo URL per una configurazione futura, poiché consentirà all'ESP32 di comunicare in tempo reale con il server BTCPay. Il protocollo WebSocket (`wss://`) stabilisce una connessione permanente tra i due: non appena un pagamento Lightning viene confermato sul PoS, BTCPay invia istantaneamente le informazioni all'ESP32, che può quindi attivare la macchina del fumo.

**5 - Configurazione di WiFi e WebSocket**

- Ritorna alla pagina: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) con il vostro ESP32 connesso
- Vai a *Configure Device* → *Wifi Settings*

Scopri:
- SSID WiFi: il nome della rete WiFi in uso.
- Password WiFi: la password WiFi.

![bitcoinswitch-lnbits](assets/fr/39.webp)

- Nella sezione *LNbits Device URL*, incolla l'URL WebSocket creato nel passaggio precedente.
- Fai clic su *Upload config*.

![bitcoinswitch-lnbits](assets/fr/40.webp)

- Attendi il completamento del caricamento; i log dovrebbero visualizzare i parametri appena inseriti (SSID, password e URL WebSocket).

![bitcoinswitch-lnbits](assets/fr/41.webp)

- Attendi che ESP32 stabilisca la connessione WebSocket. Si dovrebbe vedere:

```
WiFi connection established!
[WebSocket] Connected to url: ...
```

![bitcoinswitch-lnbits](assets/fr/42.webp)

- Ora è possibile scollegare l'ESP32

---


## Software Checkpoint

Prima del test finale, controlla:
- Blink connesso a BTCPay.
- PoS creato con almeno 1 articolo.
- ESP32 flashato con BitcoinSwitch.
- WiFi configurato su ESP32.
- URL WebSocket corretto.
- Registri ESP32 senza errori.

---


## Test e debug

### Completare il test finale

1. Inserisci la spina della macchina del fumo (220V) e accendila.
2. Alimenta l'ESP32 (batteria o USB).
3. Apri il PoS BTCPay nel browser.
4. Scansione dell'elemento "macchina del fumo".
5. Paga con un wallet Lightning (Blink o altro wallet).
6. Osserva:
   - Il relè scatta (suono udibile e LED del relè acceso).
   - La macchina del fumo viene attivata.
   - Fumo generato!

### Problemi e soluzioni comuni

| **Problema**                       | **Causa Probabile**             | **Soluzione**                                                                               |
| ---------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------- |
| ESP32 non si connette              | Driver USB mancante             | Installa [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Il relè non fa clic                | Cablaggio GPIO errato           | Controlla GPIO 21 → IN                                                                      |
| La macchina del fumo non risponde  | Telecomando cablato male        | Controlla NO/NC/COM                                                                         |
| Timeout WebSocket                  | URL non corretto                | Controlla wss:// e /bitcoinswitch                                                           |
| WiFi non si connette               | SSID/Password errato            | Riscrivi la configurazione WiFi                                                             |
| Pagamento ricevuto ma nulla accade | ESP32 non collegato a WebSocket | Controlla i log RESET                                                                       |


## Risorse

### Link utili

- Firmware BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Documenti del server BTCPay : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- Piedinatura ESP32 : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)

### Comunità e supporto

- **Server BTCPay**: [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Mattermost ufficiale
- **Server BTCPay Telegram**: [t.me/btcpayserver](https://t.me/btcpayserver)
- **LNbits**: [t.me/lnbits](https://t.me/lnbits) - Telegram ufficiale, comunità attiva
- **BitcoinSwitch** (bug del firmware): [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)

### Codice sorgente

- Codice sorgente del firmware BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)

---

**⚡** Impila sats, fai fumo, divertiti, rimani umile! **⚡**

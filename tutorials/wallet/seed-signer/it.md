---
name: Seed Signer

description: Configurazione del tuo Seed signer
---

![cover](assets/cover.jpeg)

## Materiale:

1. Raspberry Pi Zéro (versione 1.3)

Raspberry Pi Zero

Per una soluzione completamente isolata, assicurati di utilizzare la versione 1.3 senza capacità WiFi o Bluetooth, ma qualsiasi modello Raspberry Pi 2/3/4 o Zero funzionerà.

Nota: I Raspberry Pi di solito non vengono forniti con i pin collegati; i pin dovranno essere saldati o si può utilizzare qualcosa chiamato "GPIO Hammer".
GPIO Hammer

Se la tua saldatura non è abbastanza precisa o se non possiedi ancora un saldatore, puoi utilizzare "GPIO Hammer" come alternativa alla saldatura.

2. Cappello LCD WaveShare 1,3 pollici con schermo 240 × 240 pixel

WaveShare LCD Hat

Waveshare 1.3″ 240×240 pxl LCD

Nota: Scegli attentamente lo schermo Waveshare; assicurati di acquistare il modello con una risoluzione di 240×240 pixel.
ulteriori informazioni

3. Modulo fotocamera compatibile con Pi Zero

Raspberry Pi Camera

Aokin / AuviPal 5MP 1080p con sensore OV5647 Modulo fotocamera video; anche altre marche con il modulo sensore OV5647 dovrebbero funzionare, ma potrebbero non essere compatibili con l'involucro Orange Pill.

Nota: Avrai bisogno di un cavo a nastro per fotocamera specificamente compatibile con Raspberry Pi Zero.

4. Scheda MicroSD con almeno 4 GB di capacità

risorse estese: https://seedsigner.com/explainers/

## Software:

Installazione del software

1. Scarica l'ultima versione del file "seedsigner_x_x_x.img.zip"
   ultima versione

2. Decomprimi il file "seedsigner_x_x_x.img.zip"

3. Utilizza Balena Etcher o un tool simile per scrivere il file immagine .img decompresso su una scheda microsd
   BALENA ETCHER

4. Installa la scheda microsd in SeedSigner.
   Chiave pubblica GPG di SeedSigner
   seedsigner_pubkey.gpg

## Video tutorial

_Guida tratta da Southerbitcoiner, creata da Cole_

### Una raccolta di video guide su SeedSigner: un portafoglio hardware fai-da-te/open source

![image](assets/1.webp)

SeedSigner è un dispositivo di firma Bitcoin che puoi costruire da zero. Sembra difficile, ma questa serie di 4 parti dovrebbe aiutarti :) Ti consiglio di guardare la parte 1 e 2, quindi decidere se vuoi utilizzare un desktop (guarda la parte 3) o un dispositivo mobile (guarda la parte 4).

Tutto ciò che devi sapere sarà riportato di seguito. Altri link utili includono il sito web di SeedSigner, il loro Github, il loro Keybase, l'ultima versione e i requisiti hardware.

### Parte 1: Come costruire un SeedSigner:

In questo video ti mostro come scaricare e verificare il software SeedSigner, quali parti sono necessarie e come assemblare il tuo SeedSigner.

![video](https://youtu.be/mGmNKYOXtxY)

### Parte 2: Test del tuo SeedSigner

Prima di utilizzare il mio SeedSigner, ho fatto alcuni test per assicurarmi che non stesse facendo nulla di malevolo. Ho pensato di condividere anche questo passaggio. Ecco come verificare che il tuo SeedSigner esporti il portafoglio corretto (xpub), come verificare i calcoli dei lanci di dadi di SeedSigner e come verificare i seed figli bip-85 di SeedSigner.

### Parte 3: Come utilizzare SeedSigner con Sparrow Wallet (desktop)

SeedSigner è in grado di generare seed e firmare transazioni bitcoin. Ma da solo, non è in grado di creare transazioni. È necessario utilizzare un "coordinatore" di portafoglio con il tuo SeedSigner. Ecco come utilizzare Sparrow Wallet con il tuo SeedSigner:

![video](ttps://youtu.be/IQb8dh-VTOg)

### Parte 4: Come utilizzare SeedSigner con Blue Wallet (mobile)

SeedSigner è in grado di generare seed e firmare transazioni bitcoin. Ma da solo, non è in grado di creare transazioni. È necessario utilizzare un "coordinatore" di portafoglio con il tuo SeedSigner. Ecco come utilizzare Blue Wallet con il tuo SeedSigner:

![video](https://youtu.be/x0Ee35Ct0r4)

Queste sono tutte le guide di SeedSigner, per ora! Fammi sapere se pensi che mi stia perdendo qualcosa. Questi sono nella mia lista per potenziali video:

> Recensione generale di SeedSigner. È una buona scelta per un dispositivo di firma? Pro/contro?

> Come utilizzare Bip-85 con SeedSigner
> Come essere zio Jim con SeedSigner

Hai trovato utili queste informazioni? Considera di inviare una mancia per contribuire a finanziare futuri video:

https://www.southernbitcoiner.com/donate/

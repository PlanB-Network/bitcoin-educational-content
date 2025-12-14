---
name: LN VPN

description: Configura LN VPN con Lightning per una VPN anonima e su misura
---

![image](assets/cover.webp)

LN VPN è un servizio VPN personalizzato che accetta solo pagamenti lightning. Oggi ti mostrerò come utilizzarlo e lasciare meno tracce quando navighi su Internet.

Ci sono molti fornitori di servizi VPN di qualità, abbiamo infatti fatto una recensione completa in questo articolo (hyperlink), ma LN VPN si distingue e non potevamo non fartelo scoprire.

La maggior parte dei fornitori di servizi VPN come ProtonVPN e Mullvad offre la possibilità di pagare con bitcoin ma richiede la creazione di un account e l'acquisto di un abbonamento a lungo termine, il che potrebbe non essere adatto a tutti i budget.

LN VPN rende possibile l'utilizzo di una VPN personalizzata per una durata anche breve come un'ora grazie alla sua implementazione dei pagamenti in bitcoin tramite lightning network. I pagamenti lightning, istantanei e anonimi, aprono un mondo di possibilità per i micropagamenti.

> 💡 Questa guida descrive come utilizzare LN VPN da un sistema Linux Ubuntu 22.04 LTS

## Prerequisiti: Wireguard

In termini molto semplici, Wireguard serve per creare un tunnel sicuro tra il tuo computer e il server remoto attraverso il quale navigherai su Internet. L'indirizzo IP di questo server apparirà come il tuo per la durata del contratto che seguirai seguendo questa guida.

Guida ufficiale all'installazione di Wireguard: https://www.wireguard.com/install/

```
Installazione di wireguard
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Prerequisiti: Portafoglio Bitcoin Lightning

Se non hai ancora un portafoglio Bitcoin Lightning, non preoccuparti, abbiamo creato una guida molto semplice per te, qui. (la sezione tutorial LN può aiutarti)

## Passaggio 1: Contrattare un contratto

Da https://lnvpn.com, dovrai selezionare il paese dell'IP di uscita del tunnel VPN e una durata. Una volta definiti questi parametri, fai clic su Paga con lightning.

![image](assets/1.webp)

Verrà visualizzata una fattura lightning, dovrai semplicemente scannerizzarla con il tuo portafoglio lightning.

Una volta pagata la fattura, dovrai attendere qualche secondo fino a circa due minuti affinché vengano generati i tuoi parametri di configurazione Wireguard. Se ciò richiede un po' più di tempo, non preoccuparti, abbiamo fatto questa procedura decine di volte, a volte può richiedere un po' più di tempo.

L'immagine seguente verrà visualizzata e ti basterà fare clic su "Download come file" per ricevere il tuo file di configurazione, che avrà un nome simile a lnvpn-xx-xx.conf dove "xx" corrisponderanno alla data odierna

## Passo 2: Attivare il tunnel

Innanzitutto, dovrai rinominare il file di configurazione ottenuto al passo precedente in modo che venga riconosciuto automaticamente da Wireguard.

Vai nella tua cartella di download, sia tramite una finestra del terminale o con l'esploratore di file, e rinomina il file lnvpn-xx-xx.conf in wg0.conf.

bash

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

Fatto! Il tunnel è attivato!

## Passo 3: Verificare

Utilizza un servizio online come "whatismyip" per verificare che il tuo indirizzo IP pubblico sia ora quello del VPN che hai appena attivato.
Passo 4: Disattivare

Quando il contratto scadrà, dovrai disattivare la connessione per ripristinare l'accesso a Internet. Successivamente, potrai ripetere senza problemi i passaggi da 1 a 3 ogni volta che vorrai stabilire una connessione con LN VPN.

Disattivare il tunnel:

perl

```
    $ sudo ip link delete dev wg0
```

Fatto! Ora sai come utilizzare LN VPN, un servizio VPN unico nel suo genere!

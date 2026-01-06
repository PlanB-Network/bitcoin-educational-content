---
name: LN VPN
description: Configura LN VPN con Lightning per una VPN anonima e su misura
---

![image](assets/cover.webp)

LN VPN è un servizio VPN personalizzato che accetta solo pagamenti lightning. Oggi ti mostrerò come utilizzarlo e lasciare meno tracce quando navighi su Internet.

Ci sono molti fornitori di servizi VPN di qualità, ma LN VPN si distingue e non potevamo non fartelo scoprire.

La maggior parte dei fornitori di servizi VPN come ProtonVPN e Mullvad offreno la possibilità di pagare con bitcoin ma richiedono la creazione di un account e l'acquisto di un abbonamento a lungo termine, il che potrebbe non essere adatto a tutti i budget.

LN VPN rende possibile l'utilizzo di una VPN personalizzata per una durata anche breve come un'ora grazie alla sua implementazione dei pagamenti in bitcoin tramite lightning network. I pagamenti lightning, istantanei e anonimi, aprono un mondo di possibilità per i micropagamenti.

> Nota💡 **Questa guida descrive come utilizzare LN VPN da un sistema Linux Ubuntu 22.04 LTS**

## Prerequisiti: [Wireguard](https://www.wireguard.com/papers/wireguard.pdf)

https://planb.academy/tutorials/computer-security/communication/wireguard-81fdd0db-b2bd-4a6c-a082-2de269e26779

In termini molto semplici, Wireguard serve per creare un tunnel sicuro tra il tuo computer e il server remoto attraverso il quale navigherai su Internet. L'indirizzo IP di questo server apparirà come il tuo per la durata del contratto che seguirai seguendo questa guida.

Guida ufficiale all'installazione di Wireguard: https://www.wireguard.com/install/

```
Installazione di wireguard
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Prerequisiti: Bitcoin Lightning wallet

Se non hai ancora un Bitcoin Lightning wallet, non preoccuparti, abbiamo creato più di una guida molto semplici per te. (di seguito ne mettiamo qualcuna)

https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


## Passaggio 1: Creare un nuovo contratto

Da https://lnvpn.com, dovrai selezionare il paese dell'IP di uscita del tunnel VPN e una durata. Una volta definiti questi parametri, fai clic su Paga con lightning.

![image](assets/1.webp)

Verrà visualizzata una invoice lightning, dovrai semplicemente scannerizzarla con il tuo wallet lightning.

Una volta pagata l'invoice, dovrai attendere qualche secondo fino a circa due minuti affinché vengano generati i tuoi parametri di configurazione Wireguard. Se ciò richiede un po' più di tempo, non preoccuparti, abbiamo fatto questa procedura decine di volte, a volte può richiedere un po' più di tempo.

L'immagine seguente verrà visualizzata e ti basterà fare clic su "Download come file" per ricevere il tuo file di configurazione, che avrà un nome simile a lnvpn-xx-xx.conf dove "xx" corrisponderanno alla data di creazione.


## Passo 2: Attivare il tunnel

Innanzitutto, dovrai rinominare il file di configurazione ottenuto al passo precedente in modo che venga riconosciuto automaticamente da Wireguard.

Vai nella tua cartella di download, sia tramite una finestra del terminale o con l'esploratore di file, e rinomina il file lnvpn-xx-xx.conf in wg0.conf.

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

Fatto! Il tunnel è attivato!


## Passo 3: Verifica

Utilizza un servizio online come "whatismyip" per verificare che il tuo indirizzo IP pubblico sia ora quello del VPN che hai appena attivato.


## Passo 4: Disattiva

Quando il contratto scadrà, dovrai disattivare la connessione per ripristinare l'accesso a Internet. Successivamente, potrai ripetere senza problemi i passaggi da 1 a 3 ogni volta che vorrai stabilire una connessione con LN VPN.

Disattiva il tunnel:

```
    $ sudo ip link delete dev wg0
```

Fatto! Ora sai come utilizzare LN VPN, un servizio VPN unico nel suo genere!

Se ti interessa sapere di più sulle VPN quarda il nostro corso SCU101 su PlanB Accademy o [qui](https://planb.academy/it/courses/99c46148-7080-4915-a7e0-9df0e145cd47/vpn-e-connessione-internet-5aac83f4-a685-54b0-9759-d71bea7eeed2)

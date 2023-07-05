---
name: LN VPN

description: Configura la tua VPN
---

![image](assets/cover.jpeg)

# LN⚡VPN

_**Guida proposta da FranklynHart nell'ambito di Agora256, post originale https://agora256.com/lnvpn/**_

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

![image](assets/1.jpeg)

Verrà visualizzata una fattura lightning, dovrai semplicemente scannerizzarla con il tuo portafoglio lightning.

Una volta pagata la fattura, dovrai attendere qualche secondo fino a circa due minuti affinché vengano generati i tuoi parametri di configurazione Wireguard. Se ciò richiede un po' più di tempo, non preoccuparti, abbiamo fatto questa procedura decine di volte, a volte può richiedere un po' più di tempo.
'L'écran suivant s'affichera et il te suffira de cliquer sur "Download as File" pour recevoir ton fichier de config, celui-ci portera un nom qui ressemblera à lnvpn-xx-xx.conf où les "xx" correspondront à la date du jour.
![image](assets/2.jpeg)

## Étape 2 : Activer le tunnel

D'abord, il te faudra renommer le fichier de config obtenu à l'étape précédente de sorte qu'il puisse être automatiquement reconnu par Wireguard.

Rends-toi dans ton dossier de téléchargement, soit dans une fenêtre de terminal ou avec l'explorateur de fichier et renomme le fichier lnvpn-xx-xx.conf ainsi : wg0.conf

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

Voilà, ça y est! Le tunnel est activé!

## Étape 3 : Vérifier

Utilise un service en ligne comme whatismyip pour vérifier que ton adresse IP publique est bien maintenant celle du VPN que tu viens d'activer.

## Étape 4 : Désactiver

Lorsque ton bail sera expiré, il te faudra désactiver la connection pour retrouver ton accès à Internet. Tu pourras ensuite sans problème répéter les étapes 1 à 3 chaque fois que tu voudras contracter un bail avec LN VPN.

Désactiver le tunnel :

```
    $ sudo ip link delete dev wg0
```

Voilà! Tu sais maintenant te servir de LN VPN, un service VPN unique en son genre!

> _**Guide proposé par FranklynHart dans le cadre de Agora256, post original https://agora256.com/lnvpn/**_'

---
name: LN VPN
description: Configurer LN VPN avec Lightning pour un VPN anonyme et à la carte
---

![image](assets/cover.webp)

LN VPN est un service VPN à la carte qui n'accepte que les paiements lightning. Aujourd'hui, je te montre comment t'en servir et laisser moins de traces quand tu te balades sur les interwebs.‌‌‌‌

Il existe de nombreux fournisseurs de services VPN de qualité, nous avons d'ailleurs fait une revue exhaustive dans cet article (hyperlien) mais LN VPN se démarque et nous ne pouvions passer à côté de te le faire découvrir.

La plupart des fournisseurs de services VPN tels que ProtonVPN et Mullvad offrent la possibilité de payer bitcoins mais nécessitent la création d'un compte et l'achat d'un forfait à plus ou moins long terme, ce qui ne correspond pas nécessairement à tous les budgets.

LN VPN rend possible une utilisation VPN à la carte pour une durée aussi courte qu'une heure grâce à son implémentation des paiements en bitcoins par lightning network. Instantanés et anonymes, les paiements lightning ouvrent un monde de possibilités en ce qui a trait aux micropaiements. ‌‌‌‌

> 💡 Ce guide décrit comment utiliser LN VPN à partir d'un système Linux Ubuntu 22.04 LTS

## Prérequis: Wireguard

En termes très simples, Wireguard sert à créer un tunnel sécurisé entre ton ordinateur et le serveur distant à travers lequel tu navigueras sur Internet. C'est l'adresse IP de ce serveur qui apparaîtra comme étant la tienne pour la durée du bail que tu vas contracter en suivant ce guide.

Guide officiel d'installation Wireguard : https://www.wireguard.com/install/‌‌‌‌

```bash
$ sudo apt-get update
$ sudo apt install wireguard
```

## Prérequis : Portefeuille Bitcoin Lightning

Si tu n'as pas encore un portefeuille Bitcoin Lightning, pas de soucis, on a créé un guide très simple pour toi, ici. (la section tutoriel LN pourras t'aider)

## Étape 1 : Contracter un bail

A partir de https://lnvpn.com, il te faudra sélectionner le pays de l'IP de sortie du tunnel VPN ainsi qu'une durée. Une fois ces paramètres définis, clique sur Pay with lightning.

![image](assets/1.webp)

Une facture lightning s'affichera, il te suffira de la scanner avec ton portefeuille lightning.

Une fois la facture payée, il te faudra patienter de quelques secondes à plus ou moins deux minutes pour que tes paramètres de configuration Wireguard soient générés. Si cela prends un peu plus de temps, pas de panique, on a fait cette procédure des dizaines de fois, il arrive parfois que ce soit un petit peu plus long.

L'écran suivant s'affichera et il te suffira de cliquer sur "Download as File" pour recevoir ton fichier de config, celui-ci portera un nom qui ressemblera à lnvpn-xx-xx.conf où les "xx" correspondront à la date du jour.

![image](assets/2.webp)

## Étape 2 : Activer le tunnel

D'abord, il te faudra renommer le fichier de config obtenu à l'étape précédente de sorte qu'il puisse être automatiquement reconnu par Wireguard.

Rends-toi dans ton dossier de téléchargement, soit dans une fenêtre de terminal ou avec l'explorateur de fichier et renomme le fichier lnvpn-xx-xx.conf ainsi : wg0.conf

```bash
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```

Voilà, ça y est! Le tunnel est activé!

## Étape 3 : Vérifier

Utilise un service en ligne comme whatismyip pour vérifier que ton adresse IP publique est bien maintenant celle du VPN que tu viens d'activer.

## Étape 4 : Désactiver

Lorsque ton bail sera expiré, il te faudra désactiver la connection pour retrouver ton accès à Internet. Tu pourras ensuite sans problème répéter les étapes 1 à 3 chaque fois que tu voudras contracter un bail avec LN VPN.

Désactiver le tunnel :

```bash
$ sudo ip link delete dev wg0
```

Voilà! Tu sais maintenant te servir de LN VPN, un service VPN unique en son genre!

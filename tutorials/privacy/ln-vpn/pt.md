---
name: LN VPN

description: Configurar sua VPN
---

![image](assets/cover.jpeg)

# LN⚡VPN

_**Guia oferecido por FranklynHart como parte do Agora256, post original https://agora256.com/lnvpn/**_

LN VPN é um serviço de VPN personalizado que aceita apenas pagamentos em lightning. Hoje, vou te mostrar como usá-lo e deixar menos rastros enquanto navega na internet.

Existem muitos provedores de serviços de VPN de qualidade, inclusive fizemos uma revisão completa neste artigo (link), mas o LN VPN se destaca e não poderíamos deixar de apresentá-lo a você.

A maioria dos provedores de serviços de VPN, como ProtonVPN e Mullvad, oferece a opção de pagamento com bitcoins, mas requer a criação de uma conta e a compra de um plano de longo prazo, o que pode não ser adequado para todos os orçamentos.

O LN VPN possibilita o uso de VPN personalizada por um período tão curto quanto uma hora, graças à sua implementação de pagamentos em bitcoins pela rede lightning. Instantâneos e anônimos, os pagamentos em lightning abrem um mundo de possibilidades para micropagamentos.

> 💡 Este guia descreve como usar o LN VPN a partir de um sistema Linux Ubuntu 22.04 LTS

## Pré-requisitos: Wireguard

Em termos simples, o Wireguard é usado para criar um túnel seguro entre o seu computador e o servidor remoto por meio do qual você navegará na internet. É o endereço IP desse servidor que aparecerá como o seu durante o período do contrato que você seguirá neste guia.

Guia oficial de instalação do Wireguard: https://www.wireguard.com/install/

```
Instalação do wireguard
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Pré-requisitos: Carteira Bitcoin Lightning

Se você ainda não tem uma carteira Bitcoin Lightning, não se preocupe, criamos um guia muito simples para você aqui. (a seção de tutorial LN pode te ajudar)

## Passo 1: Contratar um contrato

A partir de https://lnvpn.com, você precisará selecionar o país do IP de saída do túnel VPN e a duração. Depois de definir esses parâmetros, clique em Pagar com lightning.

![image](assets/1.jpeg)

Uma fatura lightning será exibida, basta escaneá-la com sua carteira lightning.

Após o pagamento da fatura, você precisará aguardar alguns segundos a até dois minutos para que suas configurações do Wireguard sejam geradas. Se isso levar um pouco mais de tempo, não se preocupe, já fizemos esse procedimento dezenas de vezes, às vezes pode demorar um pouco mais.
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

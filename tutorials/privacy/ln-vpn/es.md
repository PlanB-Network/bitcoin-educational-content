---
name: LN VPN

description: Configura tu VPN
---

![image](assets/cover.jpeg)

# LN⚡VPN

_**Guía propuesta por FranklynHart en el marco de Agora256, publicación original https://agora256.com/lnvpn/**_

LN VPN es un servicio VPN personalizado que solo acepta pagos con lightning. Hoy te mostraré cómo utilizarlo y dejar menos rastros cuando navegas por Internet.

Existen muchos proveedores de servicios VPN de calidad, de hecho, hicimos una revisión exhaustiva en este artículo (hipervínculo), pero LN VPN se destaca y no podíamos dejar de presentártelo.

La mayoría de los proveedores de servicios VPN como ProtonVPN y Mullvad ofrecen la opción de pagar con bitcoins, pero requieren la creación de una cuenta y la compra de un plan a largo plazo, lo cual no se ajusta necesariamente a todos los presupuestos.

LN VPN permite utilizar un VPN personalizado por un período tan corto como una hora gracias a su implementación de pagos en bitcoins a través de la red lightning. Los pagos lightning son instantáneos y anónimos, abriendo un mundo de posibilidades en cuanto a micropagos.

> 💡 Esta guía describe cómo utilizar LN VPN desde un sistema Linux Ubuntu 22.04 LTS

## Requisitos previos: Wireguard

En términos muy simples, Wireguard se utiliza para crear un túnel seguro entre tu computadora y el servidor remoto a través del cual navegarás por Internet. Durante el tiempo que sigas esta guía, la dirección IP de este servidor aparecerá como la tuya.

Guía oficial de instalación de Wireguard: https://www.wireguard.com/install/

```
Instalación de Wireguard
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Requisitos previos: Monedero Bitcoin Lightning

Si aún no tienes un monedero Bitcoin Lightning, no te preocupes, hemos creado una guía muy sencilla para ti, aquí. (la sección de tutoriales de LN puede ayudarte)

## Paso 1: Contratar un plan

Desde https://lnvpn.com, deberás seleccionar el país de la IP de salida del túnel VPN y la duración del plan. Una vez que hayas definido estos parámetros, haz clic en "Pagar con lightning".

![image](assets/1.jpeg)

Aparecerá una factura lightning, simplemente escanéala con tu monedero lightning.

Una vez que hayas pagado la factura, deberás esperar unos segundos o hasta dos minutos para que se generen tus configuraciones de Wireguard. Si esto lleva un poco más de tiempo, no te preocupes, hemos realizado este procedimiento decenas de veces y a veces puede llevar un poco más de tiempo.
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

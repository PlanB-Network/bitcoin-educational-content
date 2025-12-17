---
name: Boltz
description: Cambia entre diferentes capas de Bitcoin sin perder el control.
---

![cover](assets/cover.webp)

Desde su lanzamiento en 2009, el sistema de dinero electrónico entre iguales de Bitcoin ha crecido exponencialmente, dando vida a soluciones que hoy le permiten ser un sistema que podemos utilizar instantáneamente en nuestras acciones cotidianas, especialmente a través de Lightning Network.

Sin embargo, persistía un gran problema entre las capas del protocolo Bitcoin: la interoperabilidad fluida. Para aprovechar todo el potencial de Bitcoin, era imprescindible encontrar una solución que permitiera realizar transacciones entre las distintas capas del protocolo. Esta necesidad dio lugar en 2019 a Boltz, un puente que enlaza varias capas de Bitcoin.

## ¿Qué es Boltz?

[Boltz](https://boltz.Exchange) es una plataforma no custodial ideal para cualquiera que desee realizar transacciones entre las distintas capas del protocolo Bitcoin:

- **On chain**: La principal cadena de Bitcoin, donde las transacciones se confirman cada 10 minutos, las comisiones por transacción suelen ser elevadas, lo que no satisface necesariamente las necesidades de los usuarios.
- **Lightning Network**: La capa superpuesta de Bitcoin para pagos instantáneos con comisiones bajas, lo que permite utilizar la Bitcoin para pagos diarios.
- **Liquid Network**: Una superposición para Bitcoin creada por Blockstream, que permite transacciones confidenciales rápidas y el uso de otros instrumentos financieros basados en Bitcoin.
- **RootStock**: Una solución para desarrollar contratos inteligentes basados en el protocolo Bitcoin.

![layers](assets/fr/01.webp)

La interoperabilidad entre estas diferentes capas es de gran importancia, ya que proporciona a los usuarios la flexibilidad que necesitan para aprovechar al máximo todo lo que ofrece el ecosistema Bitcoin.

Boltz utiliza intercambios atómicos. Esta tecnología permite intercambiar Bitcoin entre 2 capas (por ejemplo, intercambiar BTC onchain por BTC en Lightning) directamente entre dos partes, sin necesidad de confianza y sin necesidad de intermediario. Estos intercambios se denominan "atómicos" porque sólo pueden producir dos resultados:

- O bien el intercambio tiene éxito y los dos participantes han intercambiado efectivamente sus BTC.
- O bien el intercambio fracasa, y ambos participantes se marchan con su BTC original.

De este modo, tu conservas la autocustodia permanente de tu Bitcoin, y el intercambio no se basa en ninguna confianza en la contraparte: El intercambio tiene éxito o fracasa, pero ninguna de las partes puede robar los fondos de la otra.

Un intercambio atómico funciona con contratos inteligentes [HTLC](https://planb.academy/resources/glossary/htlc) (*Hashed Timelock Contract*). En este tipo de contrato, la cantidad se "bloquea" en un canal bidireccional y se introduce una restricción temporal, de forma que si la transacción no se completa en un tiempo determinado, el saldo revierte al depositante. Este es el mecanismo utilizado por la plataforma Boltz.

## Tus primeros intercambios con Boltz

Boltz es una plataforma web no depositaria que no requiere información personal de tu parte. Boltz tiene una interfaz minimalista y fluida que te permite empezar a operar en menos de un minuto.

![boltz](assets/fr/02.webp)

Una vez en la plataforma, puedes crear intercambios atómicos entre las distintas capas del ecosistema Bitcoin.

![home](assets/fr/03.webp)

Verás el número mínimo y máximo de satoshis (la unidad más pequeña de Bitcoin) que puedes negociar a través de Boltz, incluidos los gastos de red y un porcentaje recaudado por Boltz de entre el 0,1% y el 0,5%.

![fees](assets/fr/04.webp)

A continuación, selecciona la capa donde deseas hacer un intercambio atómico, y selecciona la capa en el que deseas recibir el Bitcoin.

![couches](assets/fr/05.webp)

En este tutorial, nos centraremos en el intercambio atómico de la capa principal hacia la Lightning Network.

Puedes configurar la unidad base para tus saldos eligiendo entre las opciones:

- BTC.
- Sats.

![unités](assets/fr/06.webp)

Una vez que hayas completado tus configuraciones básicas, inserta la cantidad de tu intercambio atómico, luego crea una factura Lightning por la cantidad equivalente, o simplemente inserta tu LNURL.

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)

Para mayor seguridad, comprueba los parámetros de tu intercambio atómico para exportar las claves de copia de seguridad vinculadas a la transacción.

En el icono **Configuración**, descarga la clave de copia de seguridad y guarda el archivo adecuadamente.

![settings](assets/fr/08.webp)

![rescue-key](assets/fr/09.webp)

Este archivo contiene las 12 palabras clave de la cartera asociada a tus intercambios atómicos.

A continuación, haz clic en el botón **Crear intercambio** atómico y procede al pago del importe indicado.

![payment](assets/fr/10.webp)

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Una vez efectuado y confirmado el pago, recibirás automáticamente el importe equivalente en tu dirección Lightning.

En el menú **Reembolso**, busca el historial de transacciones atómicas para identificar la transacción en la que deseas recibir el reembolso. También puedes importar un historial de intercambios que hayas realizado en otro dispositivo, por ejemplo, utilizando el archivo de copia de seguridad de claves asociado a estos intercambios.

![refund](assets/fr/11.webp)

En el menú **Historial**, puedes descargar un historial más detallado de los intercambios asociados a tu clave de rescate haciendo clic en el botón **Copia de seguridad**.

![backup](assets/fr/12.webp)

⚠️ No compartas este archivo, ya que contiene toda la información asociada a tus transacciones y la clave de seguridad vinculada a las mismas.

Boltz ofrece un alto nivel de confidencialidad gracias a su acceso a través de un enlace `.onion` en la red Tor. Realiza intercambios atómicos totalmente anónimos seleccionando el menú **Onion**, tras activar la navegación Tor en tu navegador.

![onion](assets/fr/13.webp)

https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

A estas alturas ya conoces Boltz, una plataforma única de intercambio que permite la interoperabilidad entre las distintas capas del ecosistema Bitcoin.

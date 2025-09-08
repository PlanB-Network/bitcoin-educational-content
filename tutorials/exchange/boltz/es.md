---
name: Boltz
description: Cambia entre diferentes capas de Bitcoin sin perder el control.
---


![cover](assets/cover.webp)



Desde su despliegue en 2009, el sistema de dinero electrónico entre iguales de Bitcoin ha crecido exponencialmente, dando vida a soluciones que hoy le permiten ser un sistema que podemos utilizar instantáneamente en nuestras acciones cotidianas, especialmente a través de Lightning Network.



Sin embargo, persistía un gran problema entre las capas del protocolo Bitcoin: la interoperabilidad fluida. Para aprovechar todo el potencial de Bitcoin, era imprescindible encontrar una solución que permitiera realizar transacciones entre las distintas capas del protocolo. Esta necesidad dio lugar en 2019 a Boltz, un puente que enlaza varias capas de Bitcoin.



## ¿Qué es Boltz?



[Boltz](https://boltz.Exchange) es una plataforma no custodial ideal para cualquiera que desee realizar transacciones entre las distintas capas del protocolo Bitcoin:




- on chain**: La principal cadena de Bitcoin, donde las transacciones se confirman cada 10 minutos de media, las comisiones por transacción suelen ser elevadas, lo que no satisface necesariamente las necesidades de los usuarios ;
- Lightning Network**: La Bitcoin superpuesta para pagos instantáneos con comisiones bajas, lo que permite utilizar la Bitcoin para pagos diarios;
- Liquid Network**: una superposición para Bitcoin creada por Blockstream, que permite una rápida, Confidential Transactions y el uso de otros instrumentos financieros basados en Bitcoin;
- RootStock**: Una solución para desarrollar contratos inteligentes basados en el protocolo Bitcoin.



![layers](assets/fr/01.webp)



La interoperabilidad entre estas diferentes capas es de gran importancia, ya que proporciona a los usuarios la flexibilidad que necesitan para aprovechar al máximo todo lo que ofrece el ecosistema Bitcoin.



Boltz utiliza intercambios atómicos. Esta tecnología permite intercambiar bitcoins entre 2 capas (por ejemplo, BTC onchain en Exchange por BTC en Lightning) directamente entre dos partes, sin necesidad de confianza y sin necesidad de intermediario. Estos intercambios se denominan "atómicos" porque sólo pueden producir dos resultados:




- O bien la Exchange tiene éxito y los dos participantes han intercambiado efectivamente sus BTC ;
- O bien la Exchange fracasa, y ambos participantes se marchan con su BTC original.



De este modo, usted conserva la autocustodia permanente de sus bitcoins, y la Exchange no se basa en ninguna confianza en la contraparte: la Exchange tiene éxito o fracasa, pero ninguna de las partes puede robar los fondos de la otra.



Una Exchange atómica funciona con contratos inteligentes [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). En este tipo de Contract, la cantidad se "bloquea" en un canal bidireccional y se introduce una restricción temporal, de forma que si la transacción no se completa en un tiempo determinado, el saldo revierte al depositante. Este es el mecanismo utilizado por la plataforma Boltz.



## Sus primeros intercambios con Boltz



Boltz es una plataforma web no depositaria que no requiere información personal por su parte. Boltz tiene un Interface minimalista y fluido que le permite empezar a operar en menos de un minuto.



![boltz](assets/fr/02.webp)



Una vez en la plataforma, puedes crear intercambios atómicos entre las distintas capas del ecosistema Bitcoin.



![home](assets/fr/03.webp)



Verás el número mínimo y máximo de satoshis (la unidad más pequeña de Bitcoin) que puedes negociar a través de Boltz, incluidos los gastos de red y un porcentaje recaudado por Boltz de entre el 0,1% y el 0,5%.



![fees](assets/fr/04.webp)



A continuación, seleccione el Layer del que desea hacer un Exchange atómico, y seleccione el Layer en el que desea recibir los bitcoins.



![couches](assets/fr/05.webp)



En este tutorial, nos centraremos en la Exchange atómica desde la Layer principal hasta la Lightning Network.



Puede configurar la unidad base para sus centrales eligiendo entre las opciones :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Una vez que hayas completado tus configuraciones básicas, inserta la cantidad de tu Exchange atómica, luego crea una Invoice Lightning por la cantidad equivalente, o simplemente inserta tu LNURL.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Para mayor seguridad, compruebe los parámetros de su Exchange atómico para exportar las claves de copia de seguridad vinculadas a su Exchange.



En el icono **Configuración**, descargue la clave de copia de seguridad y guarde el archivo adecuadamente.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Este archivo contiene las 12 palabras clave de la cartera asociada a sus intercambios atómicos.



A continuación, haga clic en el botón **Crear Exchange** atómico y proceda al pago del importe indicado.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Una vez efectuado y confirmado el pago, recibirá automáticamente el importe equivalente en su Wallet Rayo.



En el menú **Reembolso**, busque su historial atómico de Exchange para identificar la Exchange en la que desea recibir el reembolso. También puedes importar un historial de intercambios que hayas realizado en otro dispositivo, por ejemplo, utilizando el archivo de copia de seguridad de claves asociado a estos intercambios.



![refund](assets/fr/11.webp)



En el menú **Historial**, puede descargar un historial más detallado de los intercambios asociados a su clave de rescate haciendo clic en el botón **Copia de seguridad**.



![backup](assets/fr/12.webp)



⚠️ Tampoco divulgue este archivo, ya que contiene toda la información asociada a sus transacciones y la clave de seguridad vinculada a las mismas.



Boltz le ofrece un alto nivel de confidencialidad gracias a su acceso a través de un enlace `.onion` en la red Tor. Realice intercambios atómicos totalmente anónimos seleccionando el menú **Onion**, tras activar la navegación Tor en su navegador.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

A estas alturas ya conoce Boltz, una plataforma única de Exchange que permite la interoperabilidad entre las distintas capas del ecosistema Bitcoin.
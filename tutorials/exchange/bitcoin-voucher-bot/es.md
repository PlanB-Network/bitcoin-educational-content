---
name: BitcoinVoucherBot
description: Un bot de Telegram para comprar Bitcoin de forma confidencial
---
![image](assets/cover.webp)

_Este tutorial fue escrito por_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

## Introducción

El BitcoinVoucherBot es una herramienta con la que se pueden comprar Bitcoins en Exchange a cambio de euros.

### KYC Light

La acción de cambiar euros por Bitcoin es el primer paso y el más fundamental para empezar a estudiar este tema, pero aparentemente es también el más difícil y complejo. Las opciones pueden ser muchas: ofrecer Bitcoin a través de Exchanges centralizados, meetups con temática Bitcoin, amigos, conocidos, etc. Nos unimos a la comunidad Bitcoiner y **recomendamos absolutamente el uso de Exchanges centralizados** para salvaguardar más la privacidad de cada uno.

Aunque esta opción puede ser menos conveniente, es importante entender que las bolsas aplican la normativa "Conozca a su cliente" (Know Your Cutomer, KYC), asignando así una identidad, así como una ubicación física, a cada Satoshi comprado en ellas. la "comodidad" tiene efectos secundarios sorprendentes.

### ¿Cómo hacerlo?

Aquí llega el servicio [BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot), un bot de Telegram que actúa como conducto entre nuestras transferencias SEPA y las compras Sats.

### Requisitos previos

Para empezar a utilizar BitcoinVoucherBot, no hay necesidad de revelar información personal sensible al personal del Bot. **No se necesita autorización**.

Todo lo que se necesita es una cuenta de Telegram ya activa y una cuenta bancaria. **Nota**: No sirve una cuenta abierta en Poste Italiane (para clientes italianos) o, en general, una tarjeta recargable.

En el chat de Telegram preparamos un pedido, con una transferencia bancaria lo pagamos, y finalmente a través del bot obtenemos un vale emitido por una tercera empresa que desconoce el objeto de la compra.

### Activación del bot y menú

La activación es una simple operación de una sola vez. Desde Telegram, busca _@BitcoinVoucherBot_ y nada más llegar al chat del Bot, un gran botón _Start/Start_ destaca en la parte inferior. La operación provoca la respuesta del Bot, que presenta un menú con los principales comandos de que dispone. También aparecen los primeros mensajes de bienvenida, que recomendamos leer atentamente.

**Atención**: hay varios estafadores que se hacen pasar por el VoucherBot original. Si no estás seguro de la búsqueda a través de Telegram, accede al enlace de BitcoinVoucherBot desde el [sitio oficial](https://www.bitcoinvoucherbot.com/)

![image](assets/it/01.webp)

Las opciones aparecen haciendo clic en el botón _Menu_ de la esquina inferior izquierda: puede hacer clic en la palabra correspondiente al comando, o escribir en el cuadro de mensaje la barra `/` seguida del comando tecleado.

![image](assets/it/02.webp)

Las principales operaciones incluyen:


- _/compra_: es el procedimiento de compra propiamente dicho. Cuando se completa la transacción, el bot genera automáticamente el código QR, listo para canjearlo.
- _/refill_: disponible en el momento de escribir este tutorial, pero no la cubriremos porque-por razones técnicas-esta opción puede ser eliminada más adelante.
- _/swap_: abre el procedimiento de intercambio, disponible con un cómodo bot de Telegram o a través de la web.
- _/ap_: plan de acumulación, que permite establecer un **Plan de Acumulación Constante (PAC)**.
- _/lnaddress_: con la que se nos pide que enlacemos una LN Address propia, para un procedimiento concreto que veremos más adelante.
- _/credits_: para comprobar cuánto crédito queda para los bonos generate.
- _/myorders_: muestra los pedidos realizados con el bot (**Atención** el sistema sólo registra los 10 últimos pedidos realizados y no todo el historial).
- _/fees_: un comando para comprobar las tarifas de red. Para evaluarlas, siempre es mejor basarse en Mempool.space.
- _/support_: en caso de necesidad, aparecen contactos para informar de los problemas al equipo de soporte.

## Procedimiento de compra de Bitcoin

### Preparación del pedido

Haga clic en _/comprar_ en el menú de comandos

![image](assets/it/03.webp)

Aparecen varias oportunidades, pero elegimos _BTC Vouchers_

![image](assets/it/04.webp)

BitcoinVoucherBot te permite comprar Bitcoin onchain, Lightning y Liquid.

En esta fase elige _Onchain & Lightning 🔗⚡️_

![image](assets/it/05.webp)

La pantalla cambia rápidamente y VoucherBot propone denominaciones de compra. Comienzan desde un mínimo de 100,00 € hasta 900,00 €.

En caso de primera compra, sólo se ofrecen las denominaciones 100,00 €, Onchain y Lightning. Para aumentar la confidencialidad, le sugerimos que elija _Lightning ⚡️_

![image](assets/it/06.webp)

El VoucherBot nos avisa de que se ha hecho una primera elección y que, para confirmarla, tenemos que elegir _Proceed_

![image](assets/it/07.webp)

Ahora se trata de elegir la forma de pago. La transferencia se realiza por transferencia bancaria **(sólo se acepta SEPA)**. VoucherBot propone como receptor una empresa que proporciona dos cuentas bancarias, una en U.K y la otra en Suiza. El banco suizo fue elegido para llevar a cabo este tutorial

![image](assets/it/08.webp)

En este punto se nos pide que introduzcamos nuestro IBAN, aquel a partir del cual se iniciará la transferencia al banco elegido. Esta información va a conformar un puzzle que permitirá al bot, es decir, a una máquina, unir algunos datos para que el proceso de compra fluya sin necesidad de intervención humana.

El IBAN debe escribirse en la barra de mensajes, comprobarse y enviarse al bot.

![image](assets/it/09.webp)

Ahora aparece un mensaje de control en el chat con VoucherBot.

Si todo es correcto, continúe haciendo clic en _Proceder_.

![image](assets/it/10.webp)

### Pago

Tras unos instantes, necesarios para procesar los datos, VoucherBot responde con un mensaje que contiene todos los detalles necesarios para completar el pedido. Dependiendo de lo que su banco requiere, la información relevante es:


- el `IBAN`, que es esencial para el depósito, así como el Address del beneficiario;
- `el importe elegido` previamente a través del corte, que debe cumplirse para permitir que VoucherBot reconozca el pedido cuando se reciba el pago;
- `Payment reason`, que es el motivo del pago. **Debe copiarse y pegarse sin quitar ni añadir nada en el campo correspondiente de su transferencia. Cualquier "." o "-" presente en el motivo del pago, puede ser sustituido por `espacios en blanco'**.
- un `OrderID` único al que referirse cuando solicite cualquier tipo de asistencia.

A continuación, puede proceder al pago, a través de su app o banco. Cuando el pago haya sido aceptado por el banco, es importante recordar pulsar _Notificar pago_ en el chat con VoucherBot. Esta sencilla operación le avisa de que el pago está en camino.

![image](assets/it/11.webp)

VoucherBot responde con un mensaje que contiene una advertencia muy importante: **no borres el chat**, al menos hasta recibir el vale, porque es el único medio de reconstruir el pedido y mantenerlo en marcha.

![image](assets/it/12.webp)

---
Tenga en cuenta lo siguiente:


- sólo se aceptan transferencias SEPA;
- los tiempos de espera dependen exclusivamente de cómo los bancos (que no trabajan 24 horas al día, 7 días a la semana, 365 días al año, como Bitcoin) procesen el vale. La recepción del vale puede tardar desde unas horas hasta 3 días laborables;
- para cualquier necesidad, Bitcoin VoucherBot tiene un excelente servicio de [soporte](https://t.me/BitcoinVoucherGroup) en Telegram.

---
### Rescate

En cuanto el pago se realiza correctamente, Bitcoin VoucherBot envía el vale directamente al chat. El vale relámpago tiene forma de código QR, impreso sobre fondo naranja.

![image](assets/it/31.webp)

Ahí están todos los datos necesarios para cobrarlo:


- el importe en Sats, equivalente al enviado por transferencia bancaria, excluidas las comisiones de servicio y de red;
- un ID de referencia del vale;
- la fecha límite en la que debe canjearse el vale o, de lo contrario, se perderán los fondos, es decir, 25 días después de su emisión.

Puede canjear el vale enmarcando el código QR con la función de escaneado de una Wallet Lightning Network compatible, o a través de LNURL, que también se muestra debajo del código QR.

Para este tutorial usamos Wallet Of Satoshi, utilizando la función de escaneo activada por el botón _Send_.

![image](assets/it/32.webp)

Con la cámara del móvil activada, enmarca el código QR en el chat, abriendo Telegram desde el PC

![image](assets/it/34.webp)

Antes de continuar, Wallet Of Satoshi muestra una pantalla de verificación que incluye el importe, que coincide exactamente con el indicado en el cupón, y como descripción, BitcoinVoucherBot. Para canjear el cupón, basta con hacer clic en _Receive_.

![image](assets/it/35.webp)

Wallet Of Satoshi procesa durante unos instantes.

![image](assets/it/36.webp)

y, por último, la recaudación se comunica y queda inmediatamente disponible en el saldo de Wallet.

**Wallet of Satoshi es una aplicación custodial: justo después de canjear el cupón se recomienda mover los sats a una billetera no custodial.**

![image](assets/it/37.webp)

### Cómo canjear un vale onchain

Como vimos en la preparación del pedido, VoucherBot permite comprar Sats directamente onchain, con la elección del vale epónimo.

**Nota**: La preparación del pedido y el pago no cambian, son siempre los mismos. Lo que sí cambia es cómo se cobra un vale onchain.

Tras completar el pedido, realizar el pago, pulsar _Notificar pago_ y esperar el tiempo técnico de los bancos para realizar la transferencia, VoucherBot responderá enviando el vale directamente al chat.

Este vale también tiene forma de código QR, pero el color principal es amarillo canario y -lo más importante- en la descripción se explica bien que es un vale onchain, que cobras directamente en tu Wallet onchain y, para iniciar el procedimiento de cobro, tienes que pulsar en _Redeem on Telegram_. El voucher onchain también contiene la información ya vista para el lightning one:


- el importe en Sats, equivalente al enviado por transferencia bancaria, excluidas las comisiones de servicio y de red;
- un código de cupón;
- un ID de referencia del vale;
- la fecha límite en la que debe canjearse el vale o, de lo contrario, se perderán los fondos, es decir, 25 días después de su emisión.

![image](assets/it/22.webp)

**ADVERTENCIA ⚠️:** pulsado como se explica, se abre pop-up de otro bot: **Voucher RedeemBot.**

Voucher RedeemBot es la herramienta puesta a disposición para este fin. Tanto si es la primera vez que se utiliza como si existen pedidos anteriores, cada vez que se realiza un nuevo canje siempre es necesario hacer clic en _START_.

![image](assets/it/23.webp)

En este punto RedeemBot carga el voucher onchain, fácilmente reconocible por el Voucher Code y el ID de referencia. También desbloquea la barra para escribir mensajes y empezar a chatear con el bot, que de hecho nos invita a decirle un Address onchain de nuestro Wallet.

**Nota**: Esta Address debe ser del tipo SegWit.

![image](assets/it/24.webp)

Abrimos nuestra Wallet en este punto y generate a SegWit Address

![image](assets/it/25.webp)

lo copiamos

![image](assets/it/26.webp)

y pégalo en el chat con RedeemBot

![image](assets/it/27.webp)

Ahora tenemos una pantalla de comprobación, para verificar que el código del vale es correcto, así como el Address que hemos comunicado a RedeemBot. Comprobémoslo bien porque, al hacer clic en _Proceed_, se inicia la transacción y no habrá forma de volver a encontrarla si, por ejemplo, hemos comunicado el Address equivocado.

![image](assets/it/28.webp)

La transacción se ha iniciado y el procedimiento Redeem del vale onchain finaliza.

![image](assets/it/29.webp)

mientras que la cantidad se puede ver venir en la historia de nuestro Wallet.

![image](assets/it/30.webp)
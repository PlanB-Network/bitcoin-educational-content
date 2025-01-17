---
name: LNP2PBot
description: Guía completa sobre LNP2PBot y el comercio bitcoin P2P
---
![cover](assets/cover.webp)

## Introducción

Los intercambios P2P (peer-to-peer) son esenciales para preservar la confidencialidad y la autonomía financiera de los usuarios. Permiten transacciones directas entre particulares sin necesidad de verificar la identidad, lo que es crucial para quienes valoran la privacidad. Para profundizar en los conceptos teóricos, consulte el curso BTC204:

https://planb.network/courses/btc204
Comprar y vender bitcoins peer-to-peer (P2P) es uno de los métodos más privados de adquirir o deshacerse de bitcoins. LNP2PBot es un bot de Telegram de código abierto que facilita los intercambios P2P en la red Lightning, permitiendo transacciones rápidas, de bajo coste y libres de KYC.

### ¿Por qué utilizar Lnp2pbot?


- No se requiere CSC
- Transacciones rápidas en Lightning Network
- Costes bajos
- Interfaz sencilla a través de Telegram, una popular aplicación de mensajería accesible desde cualquier lugar del mundo
- Sistema de reputación integrado
- Depósito automático para una negociación segura
- Soporte multidivisa
- Comunidad activa y en crecimiento

### Requisitos previos

Para utilizar Lnp2pbot, necesitarás :

1. Monedero Lightning Network (se recomienda Breez, Phoenix o Blixt)

2. Aplicación Telegram instalada (https://telegram.org/)

3. Una cuenta de Telegram con un nombre de usuario definido

## Instalación y configuración

### 1. Configuración de su monedero Lightning

Empieza por instalar un monedero Lightning compatible. Aquí tienes nuestras recomendaciones detalladas:

**Carteras recomendadas**


- [Breez](https://breez.technology)**:
  - Excelente para principiantes
  - Interfaz intuitiva y moderna
  - Sin custodia (usted conserva el control de sus fondos)
  - Perfectamente compatible con Lnp2pbot
  - Disponible en iOS y Android

A continuación se muestra el enlace al tutorial de esta cartera:

https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

- [Phoenix](https://phoenix.acinq.co)** :
  - Sencillo y fiable
  - Configuración automática de canales
  - Compatibilidad nativa con las facturas BOLT11
  - Excelente para las transacciones cotidianas
  - Disponible en iOS y Android

A continuación se muestra el enlace al tutorial de esta cartera:

https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- [Blixt](https://blixtwallet.github.io)** :
  - Más técnico pero muy completo
  - Opciones avanzadas de configuración
  - Perfecto para usuarios experimentados
  - Código abierto
  - Disponible en Android

A continuación se muestra el enlace al tutorial de esta cartera:

https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f
**Notas importantes sobre otras carteras**

⚠️ **Importante**: Antes de vender sats, asegúrate de que tu cartera soporta facturas "hold", que son utilizadas por el bot como sistema de custodia.


- Cartera de Satoshi**: Funciona bien para recibir sats, pero puede tener retrasos en la actualización del saldo si se cancela una venta.
- Muun**: No recomendado ya que los pagos pueden fallar debido a los límites de la comisión de enrutamiento de bots (máximo 0,2%).
- Aqua**: Funciona para recibir sats, pero puede tener grandes retrasos (hasta 48 horas) para las actualizaciones de saldo en caso de cancelación de una venta.

💡 **Consejo**: Para una experiencia óptima, opta por las carteras recomendadas (Breez, Phoenix o Blixt).

⚠️ **Importante**: No olvides guardar tus frases de recuperación en un lugar seguro.

### 2. Primeros pasos con Lnp2pbot

1. Haz clic en este enlace para acceder al bot: [@lnp2pBot](https://t.me/lnp2pbot)

2. Telegram se abrirá automáticamente

3. Haga clic en "Iniciar" o envíe el comando "/start"

4. El bot te pedirá que crees un nombre de usuario si aún no tienes uno

5. El bot te guiará a través de la configuración inicial

### 3. Únete a la comunidad


- Únete al canal principal: [@p2plightning](https://t.me/p2plightning)
- Soporte: [@lnp2pbotAyuda](https://t.me/lnp2pbotHelp)

## Compra y venta de bitcoins

Hay dos formas principales de intercambiar bitcoins en Lnp2pbot:

1. Examinar y responder a las ofertas existentes en el mercado

2. Cree su propia oferta de compra o venta

En esta guía, veremos en detalle cómo :


- Comprar bitcoins de una oferta existente
- Vende bitcoins creando tu propia oferta

### Cómo comprar Bitcoins

**1. Buscar y seleccionar una oferta**

![Sélection d'une offre de vente](assets/fr/01.webp)

Busque las ofertas en [@p2plightning](https://t.me/p2plightning) y haga clic en el botón "Comprar satoshis" debajo del anuncio que le interese.

**2. Validar oferta e importe**

![Validation de l'offre](assets/fr/02.webp)

1. Volver al chat bot

2. Confirme su elección de oferta

3. Introduzca el importe en moneda fiduciaria que desea comprar

4. El bot te pedirá una factura relámpago por el importe en satoshis

**3. Póngase en contacto con el vendedor**

![Mise en relation](assets/fr/03.webp)

Una vez enviada la factura, el bot te pone en contacto con el vendedor.

**4. Comunicación con el vendedor**

![Chat privé](assets/fr/04.webp)

Haz clic en el apodo del vendedor para abrir un canal de chat privado en el que podrás intercambiar datos de pago en fiat.

**5. Confirmación del pago

![Confirmation du paiement](assets/fr/05.webp)

Tras realizar el pago en fiat, utiliza el comando `/fiatsent` en el chat del bot. Una vez completada la transacción, podrás puntuar al vendedor y la transacción se cerrará.

### Cómo vender Bitcoins

**1. Crear una oferta de venta**

![Création d'une offre de vente](assets/fr/06.webp)

Para crear una oferta de venta, basta con utilizar el comando :

`/vender`

El bot te guiará paso a paso:

1. Elija su moneda

2. Indicar la cantidad de satoshis a vender

3. Por el precio, tienes dos opciones:


   - Establezca un precio fijo para la cantidad de satoshis
   - Utilizar el precio de mercado con la opción de aplicar una prima (positiva o negativa)

💡 **Consejo**: La prima te permite ajustar tu precio en relación al precio de mercado. Por ejemplo, una prima del -1% significa que estás vendiendo por un 1% menos que el precio de mercado.

**2. Confirmación de la creación del pedido**

![Confirmation de l'ordre de vente](assets/fr/07.webp)

Una vez creada la orden, verá una confirmación con la opción de cancelar la orden mediante el comando `/cancel`.

**3. Gestionar las ventas**

![Prise de l'ordre par un acheteur](assets/fr/08.webp)


- Cuando un comprador responda a tu oferta, recibirás una notificación con un código QR y una factura para pagar.
- Compruebe el perfil y la reputación del comprador.

![Mise en relation avec l'acheteur](assets/fr/09.webp)


- Haga clic en el apodo del comprador para abrir un canal de debate privado.
- Comunicar los datos de pago en fiat al comprador.
- Espere la confirmación del pago en fiat por parte del comprador.
- Compruebe que se ha recibido el pago en su cuenta.

![Confirmation de la fin de l'ordre](assets/fr/10.webp)


- Confirme la transacción con `/release` y complete el pedido. Tendrás la oportunidad de puntuar al comprador.

## Buenas prácticas y seguridad

### Consejos de seguridad


- Empezar con pequeñas cantidades
- Comprueba siempre la reputación de los usuarios
- Utilice sólo los métodos de pago sugeridos
- Mantener todas las comunicaciones en bot chat
- No comparta nunca información sensible

### Sistema de reputación


- Cada usuario tiene una puntuación de reputación
- Las transacciones exitosas aumentan su puntuación
- Elija usuarios con buena reputación
- Informar de cualquier comportamiento sospechoso a los moderadores

### Resolución de litigios

1. Cuando surjan problemas, mantenga la calma y la profesionalidad

2. Utilice el comando `/dispute` para abrir un ticket

3. Aportar todas las pruebas necesarias

4. Esperar a un moderador

## Comparación con otras soluciones

Lnp2pbot tiene varias ventajas y desventajas sobre otras soluciones de intercambio P2P como Peach, Bisq, HodlHodl y Robosat:

### Ventajas de Lnp2pbot


- No se requiere KYC** : A diferencia de algunas plataformas, Lnp2pbot no requiere verificación de identidad, preservando así la confidencialidad del usuario.
- Transacciones rápidas**: Gracias a la red Lightning, las transacciones son casi instantáneas.
- Comisiones reducidas** : Los costes de transacción son inferiores a los de las bolsas tradicionales.
- Disponibilidad móvil**: LNP2PBot es accesible a través de Telegram, lo que facilita su uso en dispositivos móviles.
- Fácil de usar** : La interfaz intuitiva de Lnp2pbot hace que sea fácil de usar, incluso para los usuarios menos experimentados.

### Desventajas de Lnp2pbot


- Dependencia de Telegram**: El uso de Lnp2pbot requiere una cuenta de Telegram, que puede no ser adecuada para todos los usuarios.
- Menos liquidez**: En comparación con plataformas más consolidadas como Bisq, la liquidez puede ser más limitada.

En comparación, soluciones como Bisq ofrecen mayor liquidez y una interfaz de escritorio, pero pueden implicar comisiones más elevadas y plazos de transacción más largos. HodlHodl y Robosat, por su parte, también ofrecen negociación sin KYC, pero con estructuras de comisiones e interfaces diferentes.

## Recursos útiles


- Página web oficial: https://lnp2pbot.com/
- Documentación: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Soporte: [@lnp2pbotAyuda](https://t.me/lnp2pbotHelp)
---
name: Blitz Wallet
description: El monedero Bitcoin más sencillo.
---

![cover](assets/cover.webp)

La experiencia de usuario es uno de los factores decisivos a la hora de elegir un monedero Bitcoin. En este tutorial, te presentamos Blitz Wallet, un monedero que sitúa la simplicidad en el centro de su enfoque: gracias a la integración del protocolo **Spark**, Blitz te ofrece uno de los monederos Bitcoin más sencillos y completos del mercado, con pagos instantáneos y sin gestión técnica.

## ¿Qué es Blitz Wallet?

Blitz Wallet es un monedero Bitcoin **self-custodial** y **open source**, que apuesta por tu soberanía y una experiencia de usuario fluida e intuitiva.

[Blitz Wallet](https://blitz-wallet.com/) es una aplicación móvil disponible en Android (Play Store) e iOS (App Store).

A diferencia de los monederos Lightning tradicionales que requieren gestionar canales de pago y liquidez entrante, Blitz Wallet se apoya en el **protocolo Spark** para eliminar estas complejidades técnicas. Resultado: pagos instantáneos desde el primer satoshi recibido, sin ninguna configuración previa. El objetivo de Blitz es hacer que los pagos en bitcoin sean tan sencillos como una aplicación de pago convencional, sin comprometer jamás la self-custody de tus fondos.

Blitz Wallet también soporta las **direcciones legibles** en formato `usuario@dominio.com` (vía LNURL), lo que permite enviar bitcoins con la misma facilidad que un correo electrónico, sin tener que manejar largos invoices o QR codes en cada transacción.

## Comprender el protocolo Spark

Antes de pasar a la práctica, es útil comprender la tecnología que hace funcionar Blitz Wallet bajo el capó: el **protocolo Spark**.

### ¿Qué es Spark?

Spark es un protocolo de capa superior open source construido sobre Bitcoin, desarrollado por el equipo de Lightspark. Permite realizar transacciones instantáneas y de bajo coste, preservando al mismo tiempo la self-custody de tus bitcoins.

A diferencia del Lightning Network, que se basa en **canales de pago** entre dos partes, Spark utiliza una tecnología llamada **statechain** (cadena de estado). El principio fundamental es el siguiente: en lugar de mover los bitcoins en la blockchain con cada transacción, Spark transfiere el **derecho de gasto** de un usuario a otro, sin movimiento on-chain.

### ¿Cómo funciona?

Para entender Spark de forma intuitiva, imaginemos que gastar un bitcoin en Spark requiere completar un puzle de dos piezas:
- Una pieza la posee el usuario (por ejemplo, Alice).
- La otra pieza la posee un grupo de operadores llamado la **Spark Entity (SE)**.

Solo la combinación de las dos piezas correspondientes permite gastar los bitcoins.

Cuando Alice quiere enviar sus bitcoins a Bob, esto es lo que sucede: se crea un nuevo puzle de forma conjunta entre Bob y el SE. El puzle conserva la misma forma, pero las piezas que lo componen cambian. A partir de ahora, es la pieza de Bob la que corresponde con la del SE. La antigua pieza de Alice se vuelve inutilizable, ya que el SE ha destruido su pieza correspondiente. La propiedad de los bitcoins ha cambiado de manos, **sin ninguna transacción en la blockchain**.

Bob puede luego repetir el mismo proceso para enviar esos bitcoins a Carol, y así sucesivamente. Cada transferencia funciona mediante el reemplazo de las piezas del puzle, no mediante un movimiento de fondos on-chain.

### ¿Por qué es seguro?

Una pregunta legítima se plantea: ¿qué ocurre si el SE no destruye realmente su antigua pieza?

La Spark Entity no es una entidad única: es un grupo de operadores independientes. La pieza del SE nunca la posee un solo operador. El reemplazo del puzle requiere la cooperación de varios operadores. Basta con que **un solo operador sea honesto** durante una transferencia para impedir la reactivación de un puzle antiguo. Ningún operador aislado puede conservar secretamente un puzle antiguo activo ni recrearlo posteriormente.

Además, Spark integra un mecanismo de salida unilateral: siempre puedes recuperar tus bitcoins on-chain sin la cooperación del SE. Este mecanismo de respaldo forma parte integral de la arquitectura de Spark y garantiza que nunca dependas de la red para acceder a tus fondos.

### Spark vs Lightning Network

Spark y Lightning no compiten entre sí: son **complementarios**. Blitz Wallet integra ambos, lo que te permite beneficiarte de las ventajas de cada uno.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Tecnología**                | Statechains (cadenas de estado) | Canales de pago    |
| **Gestión de canales**        | No requerida                 | Requerida             |
| **Liquidez entrante**         | No requerida                 | Requerida             |
| **Transacciones instantáneas**| Sí                           | Sí                    |
| **Self-custody**              | Sí                           | Sí                    |
| **Compatibilidad Lightning**  | Sí (vía atomic swaps)        | Nativo                |

El Lightning Network sigue siendo un excelente protocolo para pagos instantáneos, pero impone restricciones técnicas (gestión de canales, liquidez entrante, nodo en línea...) que pueden frenar a los principiantes. Spark elimina estas restricciones manteniendo la compatibilidad con Lightning.

## Instalación y configuración

En este tutorial, nos basamos en la versión Android de Blitz Wallet, pero todos los procesos presentados a continuación son igualmente válidos en iOS.

![installation](assets/fr/01.webp)

Al ser Blitz Wallet un monedero en self-custody, tienes la opción de **crear un nuevo monedero** o **importar una frase de recuperación** (12 o 24 palabras) de un monedero existente.

Aquí partimos de la creación de un nuevo monedero. A continuación encontrarás nuestras recomendaciones sobre la copia de seguridad de tu frase de recuperación:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **IMPORTANTE**: Estas 12 o 24 palabras de recuperación son **la única clave de acceso a tus bitcoins**. Blitz es un monedero self-custodial: ni Blitz ni Spark tienen acceso a tu frase de recuperación ni a tus fondos. Si pierdes estas palabras, perderás definitivamente el acceso a tus bitcoins. No las compartas con nadie: cualquiera que las posea puede gastar tus bitcoins.

A continuación, crea un **código PIN** para asegurar el acceso a tu monedero.

![setup-wallet](assets/fr/02.webp)

## Primeros pasos con Blitz

Realizar transacciones con Blitz es más intuitivo que en la mayoría de los demás monederos Bitcoin. La interfaz es minimalista y se centra en tres acciones principales: enviar, escanear y recibir.

### Recibir bitcoins

Para recibir bitcoins en tu monedero Blitz, haz clic en el icono **"Flecha abajo"** (↓), introduce la cantidad en satoshis que deseas recibir, añade una descripción opcional, y el monedero generará una factura (invoice) que podrás compartir con tu remitente.

⚠️ **NOTA**: El satoshi (o "sat") es la unidad más pequeña de bitcoin: **1 bitcoin = 100 000 000 satoshis**.

Una de las particularidades de Blitz Wallet es que soporta varias redes y protocolos del ecosistema Bitcoin:

- **Lightning Network**: Una de las capas superiores de Bitcoin que permite realizar micropagos de forma instantánea con comisiones muy bajas. Ideal para pequeñas cantidades del día a día.

- **Bitcoin (on-chain)**: La blockchain principal del protocolo Bitcoin, adaptada para transacciones de importes mayores donde la seguridad máxima y la finalidad son prioritarias.

- **Liquid Network**: Una sidechain (cadena paralela) de Bitcoin desarrollada por Blockstream, que permite transacciones rápidas y confidenciales utilizando Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Por defecto, Blitz genera una factura Lightning, pero puedes elegir la red en la que deseas recibir tus satoshis haciendo clic en el botón **"Choose format"** (Elegir formato).

![receive-sats](assets/fr/03.webp)

### Crear contactos

Blitz Wallet simplifica el envío recurrente de bitcoins gracias a su sistema de contactos.

En el menú **Contacts**, puedes registrar nombres de usuario Blitz o direcciones Lightning (LNURL) con las que interactúas frecuentemente.

De esta manera, podrás enviar satoshis a estas direcciones en unos pocos clics, sin tener que escanear un QR code ni introducir manualmente una dirección cada vez.

### Enviar bitcoins

Además de los métodos clásicos de envío de bitcoin (escaneo de QR code, introducción manual de dirección), Blitz ofrece varias opciones prácticas:

- **Desde una imagen** (*From Image*): Importa un QR code desde tu galería de fotos.
- **Desde el portapapeles** (*From Clipboard*): Pega una dirección o una factura copiada previamente.
- **Introducción manual** (*Manual Input*): Introduce directamente una dirección Bitcoin, una factura Lightning o una dirección legible (por ejemplo `usuario@walletofsatoshi.com`).
- **Desde tus contactos**: Selecciona un destinatario previamente registrado para enviar en unos pocos clics.

En el menú **Wallet**, haz clic en el botón **"Flecha arriba"** (↑), elige tu método de envío, introduce la cantidad a enviar, añade una descripción y confirma la transacción.

La cantidad mínima para realizar un envío es actualmente de **1 000 satoshis**.

![send-bitcoin](assets/fr/05.webp)

## La tienda Blitz

Más allá de las operaciones de transferencia de bitcoins, Blitz Wallet integra una tienda en la que puedes gastar tus bitcoins para comprar servicios digitales directamente desde la aplicación.

Desde el menú principal, haz clic en la pestaña **Store** para acceder a la tienda. También encontrarás un acceso a la plataforma **Bitrefill**, que permite comprar tarjetas regalo en miles de comercios de todo el mundo, directamente en bitcoin.

- **Inteligencia artificial**: Accede a los últimos modelos de IA generativa (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) y paga tus créditos directamente en satoshis. Hay varios planes disponibles según tus necesidades (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **SMS anónimos**: Envía y recibe SMS en todo el mundo sin revelar tu número de teléfono personal. El servicio se cobra en satoshis por cada mensaje enviado.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Protege tu privacidad en línea suscribiéndote a una VPN WireGuard (semanal, mensual o trimestral), pagable en bitcoin directamente desde la tienda Blitz. Solo tendrás que descargar la aplicación cliente WireGuard en tu dispositivo para disfrutarlo.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet entre bastidores: ir más allá

Detrás de la simplicidad de uso de Blitz Wallet se esconde una arquitectura técnica bien pensada que combina varias capas del ecosistema Bitcoin.

### La distribución de tu saldo

Blitz Wallet gestiona tu saldo de manera transparente distribuyendo tus fondos entre los diferentes protocolos en función de las necesidades. Cuando tu saldo es inferior a 500 000 satoshis, Blitz utiliza el **Liquid Network** e intercambios atómicos (*atomic swaps*) para ofrecerte una experiencia fluida y permitir transacciones en el Lightning Network incluso con pequeñas cantidades.

Este enfoque garantiza una puesta en marcha sencilla para los nuevos usuarios, sin que necesiten comprender los mecanismos subyacentes. Puedes consultar la distribución de tu saldo entre las diferentes capas en el menú **Ajustes > Balance Info**.

![balance](assets/fr/09.webp)

### El modo Lightning (opcional)

Por defecto, Blitz Wallet utiliza el Liquid Network y el protocolo Spark para ofrecerte una experiencia fluida sin configuración técnica. Sin embargo, Blitz te da la posibilidad de activar el **modo Lightning**, que abrirá automáticamente un canal de pago cuando alcances un saldo de **500 000 satoshis** (0,005 BTC).

Para activar el modo Lightning, dirígete a los **Ajustes**, luego en la sección **Ajustes Técnicos**, haz clic en la opción **Node Info**.

![enable-lightning](assets/fr/10.webp)

Gracias al protocolo Spark, esta activación es **opcional**: Spark ya permite realizar pagos compatibles con Lightning sin necesidad de abrir un canal ni gestionar liquidez entrante. El modo Lightning nativo sigue siendo útil para los usuarios avanzados que desean disponer de su propio nodo Lightning integrado dentro de la aplicación.

### Punto de venta (PoS)

Blitz Wallet integra una funcionalidad de **punto de venta** que permite a los comerciantes aceptar pagos en bitcoin directamente desde la aplicación.

En el menú **Ajustes > Point-of-sale**, puedes configurar:

- El identificador único de tu tienda
- La moneda fiduciaria local en la que mostrar los precios
- Las instrucciones para tus empleados
- La opción de propina para tus clientes

Tus clientes solo tienen que escanear el QR code generado para realizar su pago en bitcoin, de forma instantánea.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Recursos utilizados para redactar este tutorial:
- Blog de [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).

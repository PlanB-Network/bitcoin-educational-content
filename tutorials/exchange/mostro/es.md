---
name: Mostro
description: Plataforma de intercambio Bitcoin P2P sin KYC a través de Lightning y Nostr
---

![cover](assets/cover.webp)

¿Cómo adquirir o vender Bitcoin sin comprometer tu soberanía financiera? Las plataformas centralizadas imponen procedimientos KYC invasivos que exponen tus datos personales, con la posibilidad de congelación arbitraria de cuentas o vigilancia estatal.

**Mostro P2P** ofrece una alternativa descentralizada que combina Lightning Network, el protocolo Nostr y las facturas de retención. Su mayor innovación: Un sistema de custodia automatizado en el que tu Bitcoin permanece bajo su control durante todo el intercambio, eliminando el riesgo de robo, quiebra del intercambio o confiscación arbitraria.

## ¿Qué es Mostro P2P?

Mostro P2P es un protocolo de intercambio Bitcoin de código abierto creado por **grunch**, desarrollador del popular bot de Telegram **lnp2pbot** lanzado en 2021. Aunque lnp2pbot ya permitía intercambios P2P sin KYC a través de Lightning, presentaba una importante vulnerabilidad: **Telegram constituye un punto de fallo centralizado** susceptible de ser censurado por los gobiernos.

Mostro representa la **evolución descentralizada** de este concepto: Al sustituir Telegram por el protocolo **Nostr** (una red incensurable de relés distribuidos), Mostro elimina este riesgo sistémico. El protocolo combina Lightning Network para transacciones instantáneas, Nostr para una comunicación resistente a la censura y **facturas retenidas** para crear un depósito automatizado verdaderamente no custodial.

### Arquitectura técnica

Mostro funciona a través de tres componentes:

- **Daemon Mostrod**: Coordina los intercambios entre usuarios y Lightning Network
- **Nodo Lightning**: Crea facturas retenidas (~24h de custodia criptográfica)
- **Clientes de Mostro**: Interfaces de usuario (CLI, Móvil, Web)

Las órdenes se publican en Nostr como eventos públicos (tipo 38383), mientras que las operaciones privadas se transmiten mediante mensajes cifrados de extremo a extremo (NIP-59, NIP-44). Cada instancia de Mostro define sus propias comisiones (generalmente entre el 0,3% y el 1%) y límites de transacción (que oscilan entre unos pocos miles y varios cientos de miles de sats, según la instancia).

### Ventajas decisivas

**Resistente a la censura**: Ningún gobierno puede cerrar Mostro mientras existan repetidores Nostr en algún lugar del mundo. A diferencia del vulnerable lnp2pbot a través de Telegram, Mostro permite intercambios **a prueba de censura**.

**Escrow sin custodia**: Las facturas de custodia Lightning bloquean tu Bitcoin sin transferirlos permanentemente. Tus fondos permanecen bajo tu control y se te devuelven automáticamente en caso de problema (~24h).

**Confidencialidad por diseño**: Dos modos disponibles para adaptarse a tus necesidades. El modo Reputación** vincula tu reputación a tu clave Nostr para crear una confianza duradera. El modo totalmente privado** favorece el anonimato absoluto con claves efímeras de un solo uso.

## Características principales

**Comunicación descentralizada**: Todos los pedidos se publican en Nostr a través de eventos firmados criptográficamente. Las negociaciones privadas se transmiten mediante mensajes cifrados de extremo a extremo, lo que garantiza una confidencialidad absoluta.

**Sistema de reputación**: Calificación de 5 estrellas con cálculo iterativo almacenado permanentemente en Nostr. Le permite construir gradualmente una reputación como comerciante fiable.

**Arbitraje descentralizado**: En caso de litigio, un árbitro imparcial examina las pruebas y toma una decisión basada en criterios transparentes. Cada litigio genera un token único para su trazabilidad.

**Flexibilidad de pago**: Soporte para muchas monedas fiduciarias a través del servicio de cambio de yadio.io. Acepta transferencias SEPA, PayPal, Revolut, efectivo y cualquier método acordado entre las partes.

## Mostro clientes disponibles

Mostro ofrece dos clientes operativos principales para sus intercambios P2P.

### Mostro CLI - Cliente de línea de comandos

El **Mostro CLI** es el cliente más maduro y funcional. Escrito en Rust, ofrece todas las funciones de Mostro a través de una interfaz de línea de comandos. Compatible con macOS, Linux y Windows.

**Controles principales**:

- `listorders`: Mostrar todos los pedidos disponibles
- `neworder`: Crear una nueva orden de compra o venta
- `takesell` / `takebuy`: Aceptar una orden de compra o de venta
- `fiatsent`: Confirmar el envío del pago fiat
- liberar: Liberar la plica y finalizar el intercambio
- `getdm`: Ver mensajes directos
- `rate`: Evalúe a su contraparte después de un intercambio

Ideal para usuarios técnicos, automatización y entornos que requieran la máxima seguridad.

### Mostro Mobile - Aplicación para smartphone

La **aplicación móvil** en versión alfa permite operar con P2P directamente desde tu smartphone. Interfaz gráfica intuitiva con navegación por pestañas, visualización de órdenes, filtros avanzados y chat integrado para comunicarte con tus contrapartes.

Disponible para **Android** (vía APK en GitHub), es la opción óptima para los usuarios que favorecen la simplicidad y el comercio móvil ocasional.

### Mostro-web - Interface web (en desarrollo)

Interfaz aplicación web JavaScript avanzada en desarrollo activo. Diseñada para ofrecer una experiencia de usuario completa con amplias funcionalidades de negociación y gestión de carteras. Acceso a través del navegador sin necesidad de instalación.

## Instalación y configuración

Este tutorial te guiará a través de la instalación y el uso de los dos principales clientes Mostro: CLI y la aplicación móvil.

### Requisitos esenciales

Antes de empezar, necesitarás:

- **Una billetera Lightning Network** en funcionamiento con suficiente liquidez (o compatible con Lightning)
- Recomendado: Phoenix, Breez, Wallet de Satoshi...
- Mínimo 1000 satoshis de liquidez para probar

https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- **Una clave privada Nostr** (formato `nsec1...`)
- Crear una clave de comercio dedicada en [nostrkeygen.com](https://nostrkeygen.com/)
- **Importante**: Nunca utilices tu clave personal Nostr
- Guarda tu clave privada en un lugar seguro (gestor de contraseñas)
- **Opcional pero recomendado**: Conexión VPN o Tor para enmascarar tu dirección IP

https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Instalación de Mostro CLI

#### En macOS
**Paso 1: Comprobación Rust**

Compruebe que Rust está instalado (se requiere la versión 1.64+):

```bash
rustc --version
```

Si Rust no está instalado:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

**Paso 2: Clonar el repositorio**

```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```

![Vérification Rust et clonage](assets/fr/01.webp)

**Paso 3: Configuración**

Copia y edita el archivo:

```bash
cp .env-sample .env
```

Abre `.env` y configura sus ajustes:

```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```

**Importante para la sincronización CLI/Móvil**: Para acceder a los mismos pedidos en CLI y en la app móvil, debes utilizar la **misma Mostro Pubkey** y los **mismos relés Nostr** en ambos clientes. Comprueba esta configuración en Ajustes de la aplicación móvil.

![Configuration .env](assets/fr/02.webp)

**Paso 4: Instalación**

Compila e instala el programa CLI:

```bash
cargo install --path .
```

La compilación tarda 1-2 minutos. El ejecutable `mostro-cli` se instalará en `~/.cargo/bin/`.

![Installation du CLI](assets/fr/03.webp)

**Paso 5: Comprobar**

Comprueba que todo funciona:

```bash
mostro-cli --help
```

Deberías ver la lista completa de pedidos.

![Vérification avec --help](assets/fr/04.webp)

#### En Linux (Ubuntu/Debian)

Instalación idéntica a la de macOS, con la adición de:

```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```

A continuación, sigue los pasos 3 y 4 de la sección macOS.

#### En Windows

Primero instala Rust vía [rustup.rs](https://rustup.rs/), luego usa PowerShell:

```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```

Configuración idéntica: copia `.env-sample` en `.env` y rellena los parámetros.

### Instalación de Mostro Mobile

#### En Android

**Paso 1**: Dirígete a la [página de versiones de GitHub](https://github.com/MostroP2P/mobile/releases) y descarga el archivo **app-release.apk** (aprox. 65 MB).

![Page GitHub Releases](assets/fr/10.webp)

**Paso 2: Una vez descargado, abre el archivo APK desde tus descargas. Android te pedirá que autorices la instalación desde esta fuente.

![Téléchargement et installation APK](assets/fr/11.webp)

**Paso 3**: Seguir las pantallas de onboarding, que presentan las funcionalidades:

- **Opera con Bitcoin libremente - sin KYC**: Comercio sin verificación de identidad gracias a Nostr
- **Privacidad por defecto**: Elige entre el modo Reputación y el modo Privacidad total
- **Seguridad a cada paso**: Protección con facturas sin retención

![Écrans d'accueil Mostro](assets/fr/12.webp)

**Paso 4**: Continúe el proceso para descubrir:

- **Chat totalmente cifrado**: Comunicación cifrada de extremo a extremo
- **Acepta una oferta**: Navega por la cartera de pedidos y elije una oferta
- **¿No encuentras lo que necesitas?**: Crea tu propio pedido personalizado

![Suite onboarding](assets/fr/13.webp)

**Paso 5**: Una vez completada la integración, la aplicación genera automáticamente un par de claves Nostr. Ve al menú (☰) y luego a **Cuenta** para guardar tus **Palabras Secretas** (frase de recuperación). Es también en esta pantalla donde tienes la opción de cambiar el modo de privacidad antes mencionado.

![Menu et sauvegarde des clés](assets/fr/15.webp)

**Importante**: Anota tu frase de recuperación en un lugar seguro (gestor de contraseñas, caja fuerte de papel).

### Configuración inicial de seguridad

Sea cual sea la plataforma que utilices:

- **Clave dedicada**: Utiliza una identidad Nostr distinta para comerciar
- **Pequeñas cantidades**: Empieza con menos de 10.000 sats para empezar
- **Múltiples relés**: Configure de 3 a 5 relés geográficamente diversos
- **Protección de red**: Activa VPN o Tor para ocultar tu dirección IP
- **Wallet segura**: Activa el bloqueo automático de tu billetera Lightning

## Utilizar con CLI

Esta sección muestra la compra de Bitcoin a través de Mostro CLI siguiendo un caso de uso real.

### Paso 1: Lista de pedidos disponibles

El comando `listorders` muestra todas las órdenes activas:

```bash
mostro-cli listorders
```

Verás una tabla con los detalles de cada pedido: ID, tipo (compra/venta), importe, divisa, forma de pago.

![Liste des ordres disponibles](assets/fr/05.webp)

En este ejemplo, es visible una orden para vender 5 EUR a través de Revolut (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).

### Paso 2: Recepción del pedido

Para comprar este Bitcoin, toma la orden con `takesell` :

```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```

Mostro te pedirá una **factura Lightning** para recibir el BTC. Se indica la cantidad exacta en satoshis (aquí: 4715 sats).

![Prise d'ordre de vente](assets/fr/06.webp)

### Paso 3: Facilita la factura Lightning

Genera una factura Lightning desde tu wallet (Phoenix, Breez, etc.) por el importe exacto y envíala:

```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```

El sistema confirma el envío y te indica que esperes a que el vendedor pague la factura de retención antes de activar la custodia.

![Envoi de la Lightning invoice](assets/fr/07.webp)

### Paso 4: Contactar con el vendedor

Una vez activada la custodia, utiliza `dmtouser` para solicitar los datos de pago al vendedor:

```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```

![Communication avec le vendeur](assets/fr/08.webp)

### Paso 5: Recuperar la respuesta

Consulta los mensajes directos para ver la respuesta del vendedor:

```bash
mostro-cli getdm
```

El vendedor te da su ID de pago (aquí su Revtag: `@satoshi`).

![Réception de la réponse](assets/fr/09.webp)

### Paso 6: Realizar el pago en fiat

Envía el pago a través del método acordado (Revolut en este ejemplo) a los datos de contacto facilitados. **Conserva todos los documentos justificativos** (capturas de pantalla, referencias de transacciones).

### Paso 7: Confirmar el envío del pago

Una vez efectuado el pago, notifícalo a Mostro:

```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```

### Paso 8: Recepción de Bitcoin

En cuanto el vendedor confirme la recepción del fiat y libere la plica con el comando `release`, recibirás al instante tu Bitcoin en la factura Lightning que le hayas proporcionado.

### Paso 9: Evaluación

Valora al vendedor para contribuir a la reputación descentralizada:

```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```

### Comandos útiles

**Cancelar un pedido** (antes de que se tome):

```bash
mostro-cli cancel -o <order-id>
```

**Crear un nuevo pedido de venta**:

```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```

**Abrir una disputa**:

```bash
mostro-cli dispute -o <order-id>
```

## Uso con la aplicación móvil

Esta sección muestra la venta de Bitcoin a través de Mostro Mobile siguiendo un caso de uso real.

### Interfaz principal

La aplicación tiene 3 pestañas principales:

- **Libro de órdenes**: Consulta las órdenes de compra (BUY BTC) y venta (SELL BTC) disponibles
- **Mis Operaciones**: Ve tus órdenes activas e históricas
- **Chat**: Comunícate con tus contrapartes utilizando cifrado

![Interface principale](assets/fr/14.webp)

### Configuración recomendada

Antes de operar, configura algunos ajustes a través del menú (☰) > **Ajustes**:

- **Dirección Lightning** (opcional): Para recibir pagos directamente
- **Relés**: Añadir varios relés Nostr para la resistencia (por ejemplo, `wss://nos.lol`, `wss://relay.damus.io`)
- **Llave pública de Mostro**: Comprueba la clave pública de la instancia de Mostro que estás utilizando

![Paramètres de l'application](assets/fr/16.webp)

**Importante para la sincronización CLI/Móvil**: Si utilizas tanto la CLI como la aplicación móvil, configura **exactamente los mismos relés Nostr y Mostro Pubkey** en ambos clientes. Sin esta configuración idéntica, no verás las mismas órdenes disponibles en ambas interfaces. Los relés y Mostro Pubkey visibles en Configuración (captura de pantalla anterior) deben coincidir con los de su archivo CLI `.env'.

### Paso 1: Crear una orden de venta

Pulsa el botón verde **"+"** de la parte inferior derecha y, a continuación, selecciona **VENDER** (botón rojo).

![Boutons de création d'ordre](assets/fr/17.webp)

Rellene el formulario de creación:

1. **Divisa**: Selecciona la moneda que deseas recibir (EUR, USD, etc.)

2. **Importe**: Introduce el importe en fiat (por ejemplo, de 1 a 3 EUR)

3. **Métodos de pago**: Elige el método (por ejemplo, "Revolut")

4. **Tipo de precio**: Selecciona "Precio de mercado"

5. **Prima**: Ajustar la prima (control deslizante de -10% a +10%, recomendado: 0% para vender rápidamente)

Pulsa **Submit** para publicar tu pedido.

### Paso 2: Confirmación de la publicación

Tu pedido ya está publicado Estará disponible durante 24 horas. Puedes cancelarlo en cualquier momento antes de que un comprador se lo lleve ejecutando el comando `cancel`.

![Ordre publié](assets/fr/18.webp)

La orden aparece en la pestaña **Mis Operaciones** con el estado "Pendiente" y el distintivo "Creada por usted".

### Paso 3: Un comprador recibe tu pedido

Cuando un comprador acepta tu pedido, recibes una notificación. Ver detalles en **Mis operaciones**.

![Ordre pris par un acheteur](assets/fr/19.webp)


**Instrucción importante**: Ahora debes **pagar la factura de retención** mostrada para bloquear el Bitcoin (aquí 4674 sats por 1-5 EUR) en la custodia. Tienes **15 minutos máximo** de lo contrario el intercambio será cancelado.

Copia la factura de retención y págala desde tu wallet Lightning (Phoenix, Breez, etc.).

### Paso 4: Comunicarse con el comprador

Una vez activada la custodia, pulsa **CONTACT** para abrir el chat encriptado con el comprador.

El comprador (aquí "anonymous-gloriaZhao") se pondrá en contacto contigo para solicitarte los datos de pago. Por favor, responde con tus datos (Revtag, IBAN, etc.).

![Chat avec l'acheteur](assets/fr/20.webp)

### Paso 5: Recepción del pago en fiat

Espera a recibir el pago en fiat en tu cuenta Revolut (u otro método acordado). **Compruébalo cuidadosamente**:

- La cantidad exacta
- El remitente
- La referencia, si se solicita

El comprador te informará a través del chat de que ha enviado el pago. Mostro también mostrará un mensaje confirmando que el fiat te ha sido enviado.

![Confirmation d'envoi du paiement](assets/fr/20.webp)

### Paso 6: Liberar la plica

Una vez que hayas **confirmado la recepción** del pago en fiat en tu cuenta, pulsa el botón verde **RELEASE** y confirma para enviar los sats al comprador.

![Libération de l'escrow](assets/fr/20.webp)

La cantidad de Bitcoin se transfiere instantáneamente al comprador a través de su factura Lightning.

### Paso 7: Evaluar la transacción

Después de la liberación, pulsa **Calificar** para calificar al comprador. Selecciona de 1 a 5 estrellas (aquí 5/5) y pulsa **Submitir valoración**.

![Évaluation de la contrepartie](assets/fr/21.webp)

¡Se acabó el intercambio!

### Comprar Bitcoin con la aplicación móvil

El proceso para **comprar** Bitcoin es similar pero a la inversa:

1. Navega por el **Libro de Órdenes** > pestaña **COMPRAR BTC** para ver las órdenes de venta

2. Haz clic en un pedido interesante para ver los detalles

3. Pulsa **Tomar pedido**

4. Proporciona tu factura Lightning (generada a partir de tu wallet)

5. Espera a que el vendedor active la plica

6. Pónte en contacto con el vendedor a través de **CONTACT** para obtener información sobre el pago

7. Enviar pago fiat (conservar justificante)

8. El vendedor libera la plica tras la verificación

9. Recibe Bitcoin al instante en tu factura Lightning

10. Valora al vendedor (1-5 estrellas)

### Gestión de problemas

**Cancelar una orden**: En **Mis Operaciones**, pulsa tu orden y después el botón **CANCELAR** (disponible sólo antes de que se tome).

**Abrir una disputa**: Si surge un desacuerdo, pulsa **DISPUTAR** en los detalles del pedido. Adjunta todas las pruebas (capturas de pantalla del chat, referencias de transacciones bancarias).

## Ventajas y limitaciones

### Beneficios

**Soberanía financiera**: Tu Bitcoin nunca abandona tu control directo gracias al mecanismo de retención de factura, eliminando el riesgo de quiebra o piratería del intercambio.

**Resistente a la censura**: Ninguna autoridad puede cerrar la red ni censurar tus órdenes. El sistema funciona siempre que los relés Nostr estén operativos.

**Anonimato por defecto**: Sólo una clave Nostr seudónima te identifica, sin KYC ni datos personales. Comunicaciones cifradas de extremo a extremo.

**Flexibilidad de pago**: Cualquier método de pago aceptado mutuamente es posible (transferencias, aplicaciones móviles, efectivo, trueque).

### Limitaciones

**Desarrollo inicial**: Se requieren interfaces rudimentarias y una curva de aprendizaje técnico.

**Liquidez limitada**: Número limitado de órdenes, en particular para grandes cantidades o monedas poco comunes.

**Requisitos técnicos**: Se requieren conocimientos básicos de Lightning y Nostr.

**Responsabilidad individual**: No hay apoyo centralizado en caso de problemas, se requiere precaución.

## Conclusión

La P2P de Mostro representa una alternativa prometedora a las plataformas de intercambio centralizadas, ya que combina la Lightning Network, Nostr y la custodia automatizada para una negociación verdaderamente descentralizada. A pesar de su incipiente desarrollo y su limitada liquidez, la plataforma ya ofrece soberanía financiera, resistencia a la censura y anonimato por defecto.

Para los bitcoiners que prefieren autonomía y confidencialidad, Mostro es una opción viable digna de exploración progresiva. Su arquitectura descentralizada garantiza una evolución más comunitaria que comercial, allanando el camino para un futuro de intercambios Bitcoin verdaderamente libres.

## Recursos

### Documentación oficial

- [Sitio web oficial de Mostro](https://mostro.network)
- [Documentación técnica](https://mostro.network/docs-english/index.html)
- [Fundación Mostro](https://mostro.foundation)

### Código fuente y desarrollo

- [Repositorio principal de GitHub](https://github.com/MostroP2P/mostro)
- [Cliente web](https://github.com/MostroP2P/mostro-web)
- [Cliente CLI](https://github.com/MostroP2P/mostro-cli)

### Comunidad

- [Protocolo Nostr](https://nostr.com)
- [Guías Lightning Network](https://lightning.network)

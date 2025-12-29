---
name: Bull Bitcoin Wallet
description: Descubra cómo utilizar la Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Este videotutorial de BTC Sessions te guía a través del proceso de configuración y uso de Bull Bitcoin Wallet!*


Esta guía le lleva a través de la instalación, configuración y uso de Bull Bitcoin Wallet. Aprenderá a enviar y recibir fondos en las redes Bitcoin On-Chain, Liquid y Lightning, así como a mover Bitcoin entre ellas. Las amplias funciones de wallet la convierten en una potente herramienta todo en uno para gestionar su Bitcoin. Empecemos.


## Introducción


Bull Bitcoin Wallet, desarrollada por [Bull Bitcoin](https://www.bullbitcoin.com/), es una Bitcoin wallet **autocustodiada**, lo que significa que usted tiene pleno control sobre sus claves privadas y, por tanto, sobre sus fondos, sin depender de terceros. De código abierto y arraigada en una filosofía Cypherpunk, esta Wallet combina simplicidad, confidencialidad y funciones avanzadas como los swaps entre redes y la compatibilidad con PayJoin. Te permite gestionar tus bitcoins en tres redes: **Bitcoin onchain**, **Liquid** y **Lightning**, cada una adaptada a usos específicos. En [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), puedes consultar los temas actuales y los próximos desarrollos. Como el proyecto es 100% de código abierto y "construido en público", también puedes enviar tus sugerencias y cualquier error que encuentres. Mientras que algunos monederos ahora soportan múltiples redes, el Bull Bitcoin Wallet destaca por integrar profundamente características de privacidad en todas ellas, lo que lo convierte en una poderosa herramienta para gestionar tu Bitcoin en todas las redes principales


## 1️⃣ Requisitos previos


Antes de empezar a utilizar el **Bull Bitcoin Wallet**, asegúrese de que dispone de los siguientes elementos:



- Smartphone compatible**: Un dispositivo **iOS** (iPhone o iPad) o **Android**
- Conexión a Internet
- Asegure los soportes de copia de seguridad**: Escribe tu **frase de recuperación** (12 palabras) en papel o metal y guárdala en un lugar seguro.
- Conocimientos básicos**: Una comprensión mínima de los conceptos de Bitcoin (direcciones, transacciones, tasas) es útil, aunque este tutorial explica cada paso para principiantes.


## 2️⃣ Instalación


Puede instalar la aplicación a través de:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(para dispositivos iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (para dispositivos Android)


Los usuarios de Android también tienen opciones alternativas:



- Descarga el APK directamente desde la página [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) o
- Instalación a través de [Zapstore] compatible con Nostr (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Tras instalar la aplicación, sigue las instrucciones de la pantalla de bienvenida para configurar tu cuenta.


## 3️⃣ Configuración inicial


Al abrirlo, se le ofrecen las siguientes opciones:



- crear nuevo Wallet
- `Recuperar Wallet` y
- opciones avanzadas


Empecemos pulsando sobre `Opciones Avanzadas`.


Aquí podemos configurar los parámetros avanzados antes de crear o recuperar un wallet:


1. Habilita el `Tor proxy` para enrutar el tráfico a través de la red Tor.

1. la [aplicación Orbot](https://orbot.app/en/) debe estar instalada y en funcionamiento antes de activarla

2. Tor Proxy sólo se aplica a Bitcoin (no a Liquid) y puede resultar en una conexión más lenta.

2. Configurar un `Electrum Server personalizado`, o bien

3. Ajuste la configuración de `Recuperar Toro`. Más adelante aprenderemos más sobre [Recover Bull](https://recoverbull.com/).


Una vez realizados todos los ajustes opcionales, pulse `Hecho`. Si desea reutilizar un Wallet existente, pulse `Recuperar Wallet` y rellene las 12 palabras de su frase de recuperación.


Si no, haga clic en `Crear un nuevo Wallet`.


![image](assets/en/01.webp)


## 4️⃣ Pantalla de inicio


Antes de profundizar, echemos un vistazo a la `Pantalla de inicio` para orientarnos:



- el "resumen de transacciones" y el "menú de configuración" se encuentran en la parte superior.
- El "Saldo disponible" tiene una opción de privacidad que puede activarse o desactivarse.
- Acceda a la `Bitcoin Bull Exchange` para `Comprar, Vender o Pagar` (esto depende de la jurisdicción y puede requerir KYC).
- transferencia de fondos entre monederos
- `Secure Bitcoin` es igual a Onchain Bitcoin Wallet
- `Pagos instantáneos` a través de Lightning- / Liquid Network *(Nota: Bull Bitcoin Wallet permite realizar y recibir pagos a través de Lightning. Los fondos recibidos a través de Lightning se almacenan en la [*red Liquid](https://liquid.net/) (en los pagos instantáneos Wallet) gracias a un intercambio automático a través de [*intercambio Boltz](https://boltz.exchange/). Esto le da la posibilidad de interactuar con Lightning sin tener que gestionar canales de liquidez, permaneciendo en autocustodia.)*
- envío y recepción de fondos


![image](assets/en/02.webp)


Primero, hagamos algunas configuraciones importantes y empecemos con el `Backup`.


## 5️⃣ Copia de seguridad


Para iniciar el proceso de copia de seguridad, toca el icono del engranaje (⚙) en la esquina superior derecha de la aplicación y selecciona "Copia de seguridad de Wallet". Se te presentarán dos métodos para proteger tu wallet: "Copia de seguridad cifrada" y "Copia de seguridad física". Exploremos cada uno de ellos.


![image](assets/en/03.webp)


### Copia de seguridad física


Pulse sobre `Respaldo Físico` para ver una lista de 12 palabras que representan su frase de recuperación o seed. Tenga en cuenta lo siguiente:



- Escriba su `frase de recuperación` con sumo cuidado. Escríbela en papel o metal y guárdala en un lugar seguro (caja de seguridad, ubicación offline). Esta frase es tu único medio de acceder a tus bitcoins en caso de pérdida de tu dispositivo o borrado de la aplicación.
- También es importante tener en cuenta que cualquiera con esta frase puede robarte todos tus bitcoins. Nunca los almacenes digitalmente:
- Sin captura de pantalla
- Sin copias de seguridad en la nube, correo electrónico o mensajería
- Sin copiar/pegar (riesgo de guardar en el portapapeles)


![image](assets/en/25.webp)


En la siguiente pantalla tendrás que poner la palabra en el orden correcto para asegurarte de que has acertado la frase seed. Recibirás una confirmación cuando la prueba haya terminado y sea correcta.


¡! **Este punto es crítico**. Para más ayuda :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Bóveda encriptada


También existe la opción de realizar una copia de seguridad cifrada y anónima en la nube. Pero, ¿no hemos mencionado en el último párrafo que las copias de seguridad en la nube son arriesgadas y deben evitarse? Sin embargo, el equipo de Bull Bitcoin ha desarrollado una forma inteligente de hacer que el proceso sea seguro. Así es como funciona:


`Recoverbull` es un protocolo de copia de seguridad que simplifica la seguridad de su Bitcoin wallet dividiendo la copia de seguridad en dos partes. En primer lugar, el archivo de copia de seguridad de su wallet se cifra en su dispositivo utilizando una clave de cifrado fuerte. Puedes guardar este archivo cifrado donde quieras, como Google Drive o tu dispositivo. Segundo, la clave de encriptación necesaria para desbloquear el archivo es almacenada por el Recoverbull Key Server. Para recuperar tu wallet, necesitas tanto el archivo de copia de seguridad cifrado como la clave, a la que accedes con tu PIN o contraseña. Este diseño asegura que su copia de seguridad en la nube por sí sola es inútil y que el servidor de claves por sí solo es inútil sin su archivo de copia de seguridad específico. Esto mantiene sus fondos a salvo incluso si una de las partes se ve comprometida.


Piénsalo como una caja de seguridad. El archivo de copia de seguridad encriptado es la *caja*, que puedes almacenar en cualquier lugar (como Google Drive). Tu PIN de recuperación es la *llave*, que se almacena por separado en el Recoverbull Key Server. Un ladrón necesitaría conseguir tanto tu caja específica como tu llave específica para abrirla. Este diseño asegura que incluso si alguien consigue tu archivo de copia de seguridad, es inútil sin la llave del servidor, y la llave del servidor es inútil sin tu archivo de copia de seguridad único.


Más información sobre el protocolo de copia de seguridad wallet de `Recoverbull` [aquí](https://recoverbull.com/).


Pulse sobre `Encrypted vault` y luego `Continue` para confirmar el uso del servidor predeterminado. La conexión se enrutará a través de la red `Tor` para garantizar la privacidad y el anonimato.


**Entender sus PIN**



- `PIN de desbloqueo de la aplicación`**:** El PIN opcional establecido en `Configuración > PIN de seguridad` para bloquear la aplicación en tu teléfono.
- pIN de recuperación**:** El PIN obligatorio creado durante el proceso de copia de seguridad de la bóveda cifrada, utilizado para descifrar el archivo de copia de seguridad durante la recuperación.


Se trata de dos PIN distintos. No olvides tu PIN de recuperación, ya que es esencial para restaurar tu wallet"


**Configuración del PIN de recuperación:**



- Debe crear un PIN o una contraseña para recuperar el acceso a su wallet.
- El PIN / contraseña debe tener al menos 6 dígitos (por ejemplo, evite secuencias simples como 123456, que no se aceptan).
- Sin este PIN, la recuperación de wallet es imposible.


A continuación, seleccione un proveedor de cámaras acorazadas:



- google Drive o
- una `ubicación personalizada` (por ejemplo, su dispositivo)


![image](assets/en/04.webp)


Ahora, guarde el "archivo de copia de seguridad". A continuación, pulsa "Probar recuperación", selecciona el archivo de copia de seguridad guardado y pulsa "Descifrar bóveda". Introduce tu PIN o contraseña. Si todo ha funcionado, aparecerá la pantalla "Prueba completada con éxito".


### Etiquetas de importación y exportación


Ahora que hemos creado nuestro Backup echemos un vistazo a `Etiquetas`.  La Bull Bitcoin wallet mejora la privacidad y la organización permitiendo a los usuarios crear etiquetas personalizadas para sus direcciones de recepción y sus transacciones. Estas etiquetas le ayudan a categorizar sus fondos, ya que las transacciones enviadas a una dirección etiquetada heredarán esa etiqueta, y también puede etiquetar las transacciones salientes para realizar un seguimiento de su cambio. La wallet es totalmente compatible con el estándar [BIP-329](https://bip329.org/), lo que significa que puede exportar todas sus etiquetas a un archivo e importarlas en otra wallet. Esta característica garantiza que pueda realizar sin problemas copias de seguridad de su historial de transacciones y categorizaciones, o migrarlas entre diferentes instancias de wallet, sin perder su organización personalizada.


![image](assets/en/05.webp)


## 6️⃣ Configuración


Una vez asegurada la copia de seguridad principal, vamos a explorar las demás funciones disponibles en la configuración.


### A - Asegurar el acceso


Para proteger la aplicación, vaya a "Ajustes" y elija "PIN de seguridad" para seleccionar el código PIN. Crea un PIN seguro para bloquear el acceso a tu wallet. Aunque este paso es opcional, se recomienda encarecidamente para evitar el acceso no autorizado si otra persona utiliza el teléfono.


![image](assets/en/06.webp)


### B - Conexión a un nodo personal (opcional)


BullBitcoin Wallet se conecta por defecto a servidores Electrum: el primero gestionado por Bull Bitcoin y un servidor secundario de Blockstream, ambos se considera que no guardan registros, lo que reduce el riesgo de rastreo.


Para una mayor confidencialidad, puede conectar la aplicación a su propio nodo Bitcoin a través de un servidor Electrum. Para ello, pulse `Configuración` > `Configuración Bitcoin` > `Configuración Electrum Server` y, a continuación, pulse `+Añadir servidor personalizado` para introducir la dirección y las credenciales de su servidor.


![image](assets/en/07.webp)


### C - Moneda


El saldo disponible se muestra en la pantalla principal tanto en `sats` como en `USD`. Para cambiarlo, vaya a "Configuración" > "Divisa". Allí podrá alternar entre "sats/BTC" y seleccionar su "moneda fiduciaria predeterminada".


![image](assets/en/08.webp)


### D - Ajustes Bitcoin


El menú `Bitcoin Settings` ofrece un acceso profundo a las configuraciones y datos centrales de su wallet. Aquí, puede inspeccionar los detalles fundamentales de su `Secure Bitcoin` y `Instant payments wallets`, dándole total transparencia y control. Las principales funciones de este menú son:



- Wallet Detalles:** Navegue a su Bitcoin seguro o wallet pagos instantáneos para ver información específica.
- Wallet Fingerprint:** Un identificador único para su wallet.
- Clave pública (Pubkey):** La clave utilizada para generate sus direcciones de recepción Bitcoin.
- Descriptor:** Un resumen técnico de la estructura de su wallet.
- Ruta de derivación:** La ruta específica utilizada para generate todas las direcciones de su clave privada maestra.
- Address View:** Acceda a una lista de sus direcciones de recepción no utilizadas y cambie las direcciones (próximamente)


Además, tienes la opción de:



- habilite la transferencia automática para establecer un saldo máximo instantáneo de wallet, que se transferirá automáticamente a la cuenta segura de bitcoin wallet.
- Importar monederos genéricos mediante la frase `Mnemonic` o importar `watch-only`
- Conectar `Monederos de hardware`: los dispositivos compatibles actualmente son ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade y Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Directamente desde wallet, tienes acceso a la [bolsa de Bull Bitcoin](https://www.bullbitcoin.com/), lo que te permite comprar, vender y pagar Bitcoin sin salir de la app. Esta integración ofrece una cómoda solución para gestionar tus necesidades de Bitcoin. Tenga en cuenta que el acceso a la bolsa y a sus servicios puede estar restringido en función de su jurisdicción, y que puede ser necesario completar la verificación "Conozca a su cliente" (KYC) para cumplir con las normas reguladoras y utilizar todas las funciones de la plataforma.


Para empezar, pulse "Exchange" en la esquina inferior derecha y, a continuación, "Regístrese" o "Inicie sesión" en su cuenta.


La bolsa ofrece las siguientes [prestaciones](https://www.bullbitcoin.com/):



- Compre Bitcoin con autocustodia desde su cuenta bancaria
- Sin custodia
- Particulares o empresas
- Retirada instantánea
- Sin gastos ocultos
- Lightning Network disponible
- Sin límites de transacciones
- Opciones de compra recurrentes


![image](assets/en/09.webp)


Para saber más, visita este tutorial:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Recepción de fondos


Recibir fondos con **Bull Bitcoin Wallet** es sencillo y flexible, ya que admite tres redes distintas adaptadas a diferentes casos de uso:



- La red `Bitcoin (onchain)` para el almacenamiento seguro a largo plazo.
- La red `Liquid` para transacciones rápidas y más confidenciales.
- La red `Lightning` para pagos instantáneos y de bajo coste.


La aplicación genera automáticamente la dirección o factura adecuada en función de la red seleccionada. A continuación te indicamos cómo proceder para cada red.


### Recepción a través de Onchain (red Bitcoin)


Para recibir fondos de on-chain, puede seleccionar `Bitcoin Wallet` en la pantalla de inicio y pulsar `Recibir`, o bien pulsar el botón principal `Recibir` y luego elegir la `red Bitcoin`.


Existen dos modos principales para generar una dirección de recepción:


**Modo por defecto (URI con parámetros de entrada adicionales)


Por defecto, wallet genera un [BIP21 URI](https://bips.dev/21/). Se trata de un formato estandarizado que contiene más información que una simple dirección, incluido un importe, una nota personal y parámetros PayJoin para mejorar la privacidad. Este URI completo se codifica en un código QR y se pone a disposición para su copia. El formato es el siguiente `bitcoin:<dirección>?<parámetro1>=<valor1>&<parámetro2>=<valor2>`.



- Parámetros de entrada adicionales:**
    - Importe:** Especifique el importe solicitado en BTC, sats o una moneda fiduciaria.
    - Mensaje:** Añade una nota personal que será visible para el remitente.
    - PayJoin:** Active esta opción para mejorar la privacidad combinando las entradas del remitente y del destinatario en la transacción.


Ejemplo de URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Nota Importante: Por favor, no envíe fondos a las direcciones de este tutorial, el wallet será eliminado.*


![image](assets/en/10.webp)


**Sólo opción de copia o escaneado Address activada


Con la opción `Copiar o escanear sólo Address` activada, la aplicación genera una dirección Bitcoin simple en formato SegWit (bech32).


Ejemplo:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Aunque introduzcas un importe o una nota, no se incluirán en el código QR ni en la dirección copiada.


![image](assets/en/11.webp)


### Recepción a través de Liquid Network


Puede recibir un pago en la Liquid Network. Una vez en la pantalla `Recibir`, tiene las mismas dos opciones para generar una solicitud de pago:


**1. Address simple:** Copie la dirección estándar `Liquid address`. Se trata de un identificador único para su wallet en la red Liquid y no incluye ninguna cantidad o mensaje específico.


Ejemplo Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Solicitud de pago detallada (URI):** Para una solicitud más estructurada, puede especificar un importe y una nota personal. Esta información se codifica automáticamente en una URI compartible y su correspondiente código QR.



- Importe:** Puede establecer el importe en Bitcoin (BTC), Satoshis (Sats) o una moneda fiduciaria.
- Nota:** Añada un mensaje personal para identificar la transacción.


**Ejemplo URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Para completar la transacción, facilite al remitente la `dirección` o `URI`. Puedes hacerlo copiándolo en el portapapeles o haciendo que escaneen el código QR directamente desde tu pantalla.


![image](assets/en/12.webp)


### Recepción a través de Lightning



La Bull Bitcoin Wallet también le permite enviar y recibir pagos a través de la Lightning Network. Una característica clave es que los fondos recibidos a través de Lightning se intercambian automáticamente y se almacenan en el `Liquid Network` dentro de su `Instant Payments Wallet`. Este servicio funciona con la Boltz. Este diseño le permite disfrutar de la velocidad y el bajo coste de Lightning sin la complejidad de gestionar canales de liquidez, al tiempo que mantiene la autocustodia total de sus fondos. Aunque este enfoque híbrido es de autocustodia y evita la complejidad de gestionar canales, introduce un servicio de terceros (Boltz), una pequeña comisión de intercambio y la dependencia de la federación de funcionarios de la Liquid Network como titulares de claves, que es diferente de una wallet Lightning tradicional, sin autocustodia, en la que usted gestiona sus propios canales. Puede obtener más información sobre la Liquid y su modelo de gobierno aquí:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Límites:**
    - Importe mínimo:** Se requiere un importe mínimo de facturación. Consulta la aplicación para conocer el límite actual
    - Comisiones:** Usted, el receptor, es responsable de una pequeña comisión de intercambio. Esta comisión se deduce del importe que transfiere el remitente y está sujeta a cambios
- Beneficios:**
    - Autocustodia:** Sus fondos están siempre bajo su control, asegurados en la red Liquid.
    - Evite las elevadas comisiones de On-Chain:** Al utilizar Lightning y almacenar en Liquid, elude las comisiones de on-chain asociadas a la apertura de un canal Lightning tradicional. Puede optar por trasladar los fondos a un canal on-chain más adelante, cuando el importe acumulado justifique el gasto.
    - Consejo:** Para realizar la transacción más rentable entre dos usuarios de Bull Bitcoin, utilice directamente la **red Liquid** para evitar por completo las tarifas de intercambio Lightning.


Para recibir un pago, debe generate una `Factura relámpago`:


1. introduzca una cantidad**:** Especifique la cantidad que desea recibir en Bitcoin (BTC), Satoshis (Sats), o una moneda fiduciaria.

2. **(Opcional):** Incluya una nota. Esto se incrustará en la factura y se mostrará en su historial de transacciones una vez que el pago se haya completado, por lo que es más fácil de identificar.

3. `Invoice Validez`**:** La factura relámpago tiene un plazo de validez de **12 horas**. Si no se paga dentro de este periodo, pierde su validez y tendrá que generate una nueva.


Facilite al remitente la factura copiándola en su portapapeles o dejándole escanear el código QR que aparece en su pantalla.


![image](assets/en/13.webp)


## 9️⃣ Envío de fondos


Puede acceder a la pantalla de envío directamente desde la página de inicio o desde cualquiera de sus monederos. Bull Bitcoin Wallet simplifica el proceso detectando automáticamente la red de destino -`Bitcoin`, `Liquid` o `Lightning` - en función de la dirección o factura que introduzcas, ya sea pegada o escaneada mediante código QR.


### On-Chain Transmisión a través de la red Bitcoin


El envío de fondos on-chain significa que su transacción se registra directamente en la blockchain Bitcoin. Este método es el mejor para transferencias grandes o transferencias no sensibles al tiempo. Para empezar, puede pulsar el "Botón de envío" situado abajo a la derecha y escanear o introducir una "dirección Bitcoin estándar".


Si la dirección que proporciona no incluye una cantidad específica, se le pedirá que rellene los detalles en la pantalla de envío. Puede especificar la cantidad en la unidad que prefiera, como BTC, satoshis o un equivalente fiat. También tiene la opción de añadir una nota personal, que es una nota privada para su propia referencia que le ayudará a identificar la transacción más tarde. Esta nota no se comparte con el destinatario.


Por el contrario, si la solicitud de pago que escanea o pega ya contiene todos los datos necesarios, como un URI BIP21 con un importe predefinido, la wallet omitirá la pantalla de introducción de datos y le llevará directamente a la pantalla de confirmación para autorizar el pago.


![image](assets/en/14.webp)


Antes de que se emita su transacción, se le presentará una pantalla de confirmación. Es crucial que se tome un momento y revise detenidamente cada parámetro, prestando especial atención a la dirección del destinatario, el importe que se envía y las tarifas de la red. Esta pantalla también proporciona potentes herramientas para personalizar su transacción.


Puede controlar las tarifas de dos formas principales. La primera consiste en seleccionar la velocidad de transacción deseada (baja, media o alta) y wallet calculará automáticamente la tarifa correspondiente. El segundo método permite un control más preciso, ya que le permite establecer una tarifa específica, ya sea como un total absoluto en satoshis o como una tarifa relativa por byte, que luego proporciona un tiempo de confirmación estimado.


Para usuarios avanzados, wallet ofrece varios ajustes para afinar la transacción. la función `Replace-by-Fee` (RBF) está activada por defecto, una valiosa función que permite acelerar una transacción si se queda atascada en el mempool, retransmitiéndola con una tarifa más alta. También puede seleccionar manualmente de qué `Salidas de transacciones no gastadas` (UTXOs) gastar. Se trata de una potente herramienta para la consolidación UTXO, una estrategia en la que se combinan varias entradas pequeñas en una sola más grande. Aunque esto puede costar más en comisiones para la transacción actual, puede reducir significativamente las comisiones en transacciones futuras, especialmente si se espera que las comisiones de red aumenten.


![image](assets/en/15.webp)


PayJoin se intenta automáticamente cuando se escanea una solicitud de pago de un destinatario (un URI BIP21) que incluye un parámetro `pj=`. Si simplemente pega una dirección sin parámetros adicionales, esta función no se activará. Este método colaborativo mejora la privacidad al combinar las entradas tanto del remitente como del destinatario, rompiendo la heurística de la propiedad común de las entradas y permitiendo también un mejor escalado y ahorro de tasas en algunas circunstancias.


### Envío a la Liquid Network


La `Liquid Network` está diseñada para transacciones rápidas y confidenciales con comisiones mínimas. Cuando envía fondos a través de la Liquid, éstos se retiran de su `Wallet de Pagos Instantáneos`. El proceso es sencillo: basta con introducir o escanear la dirección del destinatario en la Liquid.


Si la dirección no especifica un importe, se le pedirá que lo indique en la pantalla de envío. Puede introducir la cantidad en BTC, satoshis o fiat. Una ventaja clave de Liquid es su bajo umbral mínimo. Al igual que con las transacciones on-chain, puede añadir una nota personal opcional para sus propios registros. Si la solicitud de pago ya incluye un importe, la wallet pasará directamente a la pantalla de confirmación.


En la pantalla de confirmación de una transacción Liquid, revisará los detalles. Las comisiones son notablemente bajas y se calculan en función de la complejidad de la transacción. Suelen rondar los 0,1 sat/vB, lo que para una transacción sencilla equivale a apenas 20-40 satoshis (por ejemplo, 26 satoshis a 21 de diciembre de 2025).


![image](assets/en/16.webp)


### Envío a la Lightning Network


Puede escanear un Address Lightning (por ejemplo, `runningbitcoin@rizful.com`) que le permite establecer el importe y una nota opcional para el destinatario, o escanear una factura con un importe predefinido, que le lleva directamente a la pantalla de confirmación.


*Tenga en cuenta que se aplican importes mínimos y comisiones.*


La Bull Bitcoin Wallet envía pagos Lightning retirando fondos de su `Instant Payments Wallet` (en la Liquid) e intercambiándolos a través de la `Boltz`. Este enfoque híbrido es totalmente autocustodiable y evita las elevadas tarifas de on-chain de gestionar un canal Lightning dedicado, pero requiere pagar una `tarifa de intercambio`. Para obtener el coste más bajo, envíe directamente a la dirección Liquid de un destinatario si también utiliza una Bull Bitcoin wallet.


## 🔟 Transferencia de fondos entre tus carteras


Bull Bitcoin le permite mover su Bitcoin entre su `Secure Bitcoin` wallet y su `Instant Payments Wallet` en la Liquid Network o a una `Wallet externa`. Para realizar una transferencia, simplemente navegue hasta la sección `Transferencia`, seleccione los monederos de origen y destino, introduzca la cantidad que desea mover y confirme la transacción.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Recuperar su Bull Bitcoin Wallet


Esta sección explica cómo recuperar el acceso a sus fondos Bull Bitcoin Wallet si pierde su dispositivo, desinstala la aplicación o simplemente necesita cambiar a uno nuevo. Como ya se ha explicado, hay dos métodos principales para la recuperación: utilizando el método único `Recoverbull` y utilizando una frase estándar `BIP39 seed`.


### Método 1: Recoverbull


Recapitulemos: Las copias de seguridad de Wallet se cifran localmente. El archivo encriptado puede almacenarse en la nube o en otro dispositivo. La clave de encriptación es almacenada por el Recoverbull Key Server. Ambas se mantienen separadas y deben combinarse para recuperar una wallet.


Para empezar voy a borrar el Wallet con todos los fondos en él y reinstalar el wallet. Aterrizaremos de nuevo en la `Pantalla de bienvenida`. Esta vez, seleccione la opción "Recuperar Wallet". Luego, navegue al método `Encrypted Vault`, confirme usando el `Default Key server`, y seleccione la ubicación o `Vault provider` donde almacenó el archivo de respaldo.


![image](assets/en/18.webp)


Indica que la bóveda se ha importado correctamente. Pulse el botón `Decrypt Vault` e introduzca el `PIN`. La siguiente pantalla mostrará sus "saldos" y el "número de transacciones" recuperadas.


![image](assets/en/19.webp)


### Método 2: Frase semilla


Este método utiliza la frase maestra de recuperación de su wallet, una lista estándar de 12 palabras que sirve como copia de seguridad definitiva de sus fondos. Es la forma más universal de recuperar una Bitcoin wallet, ya que no está vinculada a ningún servicio o servidor específico. Siempre que tenga esta frase, podrá recuperar su wallet en cualquier dispositivo compatible, incluso sin acceso al servidor de claves Bull Bitcoin.


En la pantalla de bienvenida, seleccione "Recuperar Wallet". Esta vez, elija el método "Copia de seguridad física". La aplicación presentará una cuadrícula de palabras. Seleccione cuidadosamente cada palabra de su frase seed de 12 palabras en el orden correcto. Sea meticuloso, ya que un solo error resultará en una wallet incorrecta.


## 1️⃣2️⃣ Conexión de una Hardware Wallet


Para obtener el máximo nivel de seguridad, muchos usuarios de Bitcoin optan por guardar sus fondos en `almacenamiento en frío`. Esto significa mantener las claves privadas que controlan su Bitcoin en un dispositivo que nunca está conectado a Internet. Una "wallet de hardware" (o dispositivo de firma) es un dispositivo físico especializado diseñado exactamente para este fin. Actúa como una cámara acorazada digital para sus claves, garantizando que nunca estén expuestas a las amenazas potenciales de un ordenador o smartphone conectado a Internet.


Al conectar una wallet de hardware a la aplicación Bull Bitcoin, obtendrá lo mejor de ambos mundos: la seguridad sin concesiones del almacenamiento en frío para sus claves privadas, combinada con las potentes funciones y la interfaz fácil de usar de la Bull Bitcoin wallet para ver saldos y gestionar transacciones. En este capítulo final, le mostraremos cómo conectar una wallet de hardware, como una [Coldcard Q](https://coldcard.com/q), a su Bull Bitcoin wallet. Este tutorial no cubrirá en profundidad la configuración de una Coldcard Q; puede aprender sobre eso aquí:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Importar una Wallet


![image](assets/en/26.webp)


En primer lugar, en el menú principal de su Coldcard Q, seleccione `Exportar Wallet` y, a continuación, `Bull Wallet`. Su Coldcard generate mostrará un código QR.


![image](assets/en/20.webp)


Abra el Bull Bitcoin Wallet y navegue hasta `Configuración` > `Configuración Bitcoin` > `Importar wallet` y seleccione `Coldcard Q` en su teléfono y pulse `Abrir la cámara` para escanear este código QR e importar las claves públicas de su wallet hardware.


![image](assets/en/21.webp)


### Recepción con Coldcard Q


Para recibir Bitcoin utilizando su Coldcard Q conectada, no necesita que el dispositivo esté físicamente conectado a su teléfono. La Bull Bitcoin Wallet ya ha importado las claves públicas necesarias, lo que le permite generate direcciones por su cuenta.


1. Pulse sobre su dispositivo de firma Coldcard Q importado y seleccione `Recibir`.

2. La aplicación mostrará automáticamente una nueva dirección Bitcoin a partir de la wallet de su Coldcard.

3. Utilice esta dirección para recibir fondos. La Bitcoin se asegurará directamente a las claves de la wallet de hardware, a pesar de que el dispositivo estaba fuera de línea durante el proceso.


![image](assets/en/22.webp)


### Envío con Coldcard Q


El envío de Bitcoin con su Coldcard Q requiere su confirmación física para autorizar cualquier transacción. Aunque la aplicación Bull Wallet se utiliza para crear la transacción, la firma final solo puede crearse en la propia wallet.


Para empezar, abre tu `Coldcard Q` wallet y pulsa sobre `Enviar`. A continuación, abre la cámara para escanear el código QR de la dirección de destino. Después de escanearlo, introduzca el "importe" que desea enviar y ajuste la "prioridad de tarifa" según sea necesario.


Para más opciones, puede buscar en Ajustes avanzados. Aquí encontrará la opción `Reemplazar por cuota` (RBF), que está activada por defecto y le permite acelerar una transacción atascada más adelante. También tiene la opción `Coin Control`, que le permite seleccionar manualmente los UTXO específicos que desea gastar.


Una vez que haya revisado todos los detalles, pulse `Mostrar PSBT` para preparar la transacción.


![image](assets/en/23.webp)


Pulse el botón `Escanear` de su Coldcard Q y utilice su cámara para escanear el código QR que aparece en su teléfono. La pantalla de la tarjeta Coldcard le mostrará todos los detalles de la transacción. Compruebe cuidadosamente el importe, la dirección del destinatario y su dirección de cambio. Si todo es correcto, pulse el botón `Enter` de la Coldcard Q para firmar la transacción. A continuación, aparecerá en la pantalla un código QR de la transacción firmada.


![image](assets/en/24.webp)


En Bull wallet, pulse "He terminado" y, a continuación, pulse el botón "Cámara" para escanear el código QR de la "transacción firmada" desde su Coldcard Q. Bull Wallet mostrará ahora una pantalla de resumen de la transacción firmada. Revísela una última vez y, a continuación, pulse "Transmitir transacción". Esto finaliza el proceso enviando la transacción a la red Bitcoin, y sus fondos estarán en camino.


## 🎯 Conclusión


Ha completado su viaje a través de Bull Bitcoin Wallet. La aplicación pone a tu alcance potentes herramientas de privacidad y seguridad, simplificando el uso de funciones avanzadas. Te ayuda a mantener la privacidad con funciones como `PayJoin`, que oculta tus transacciones en la cadena de bloques, y `Tor integration`, que enmascara tu actividad en la red de miradas indiscretas. Quienes deseen el máximo control pueden conectarse a su "nodo Bitcoin personal" para dejar de depender de servidores de terceros, y utilizar una "wallet de hardware" para mantener sus claves privadas completamente seguras y sin conexión. Con opciones de copia de seguridad inteligentes y compatibilidad sin fisuras con Bitcoin, Liquid y Lightning, Bull Bitcoin Wallet es una sólida opción todo en uno para cualquiera que se tome en serio mantener sus fondos privados, seguros y totalmente bajo su propio control.


## 📚 Recursos de Bull Wallet


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Sitio web ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)
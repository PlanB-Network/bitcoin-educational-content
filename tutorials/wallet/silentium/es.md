---
name: Silentium
description: Web progresiva wallet compatible con pagos silenciosos (BIP-352)
---

![cover](assets/cover.webp)



La reutilización de direcciones Bitcoin es una de las amenazas más directas a la confidencialidad de los usuarios. Cuando un receptor comparte una misma dirección para recibir múltiples pagos, cualquier observador puede rastrear todas las transacciones asociadas y reconstruir su historial financiero. Este problema afecta especialmente a creadores de contenidos, organizaciones benéficas o activistas que desean mostrar públicamente una dirección de donación sin comprometer su privacidad.



Silentium responde a este problema con una elegante solución accesible directamente desde el navegador. Esta aplicación web progresiva (PWA) de código abierto, lanzada en mayo de 2024 por Louis Singer, implementa Silent Payments (BIP-352): una dirección estática reutilizable en la que cada pago acaba en una dirección de blockchain independiente, sin interacción previa ni vínculo observable entre transacciones.



**Aviso importante**: Silentium es un proyecto experimental que sirve como *prueba de concepto* para los monederos ligeros de Silent Payments. No debe utilizarse como wallet diario ni para almacenar cantidades significativas. Los desarrolladores lo afirman explícitamente:



> Utilícelo bajo su propia responsabilidad.

Tenga en cuenta que esta wallet se puede utilizar como red de prueba o regtest.



## ¿Qué es Silentium?



### Filosofía y objetivos



Silentium sirve de demostración técnica para implementar los Pagos Silenciosos en un navegador ligero wallet. Aunque también admite direcciones Bitcoin convencionales, se hace hincapié en los pagos silenciosos para que los usuarios puedan experimentar con esta tecnología de privacidad de forma sencilla.



### ¿Cómo funcionan los pagos silenciosos?



Los pagos silenciosos (BIP-352) utilizan la clave de curva elíptica Diffie-Hellman Exchange (ECDH). El destinatario genera una dirección estática (`sp1...` en mainnet, `tsp1...` en testnet) que consta de dos claves públicas: una clave de exploración para detectar los pagos y una clave de gasto para utilizarlos.



El remitente combina sus claves privadas de entrada con la clave de exploración del destinatario para calcular un secreto compartido que genera un "pellizco" criptográfico. Este "tweak", añadido a la clave de gasto, crea una dirección Taproot única para cada transacción. El destinatario reproduce este cálculo con su clave de escaneado privada para detectar y gastar los fondos sin ninguna interacción previa.



Ventajas: mayor confidencialidad para el emisor y el receptor, no se necesita un servidor externo, las transacciones son indistinguibles de los pagos Taproot convencionales. Principal desventaja: escaneo intensivo de la blockchain para detectar pagos.



Para saber más sobre el funcionamiento teórico de los pagos silenciosos, consulte la última parte del curso BTC,204 sobre Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Plataformas compatibles



Silentium es una Progressive Web App (PWA) accesible desde cualquier navegador moderno (móvil o de escritorio). Utilízala directamente en `app.silentium.dev`, instálala como una aplicación nativa a través de tu navegador, o despliégala localmente. La instalación se realiza directamente desde el navegador, sin pasar por las tiendas oficiales.



## Uso de la aplicación web



### Acceso e instalación



[Vaya a `https://app.silentium.dev/` desde su navegador](https://app.silentium.dev/). La aplicación se carga al instante y muestra la pantalla de inicio.



Para instalarlo como aplicación nativa en iOS, pulsa el botón de compartir (cuadrado con flecha hacia arriba) y luego selecciona "En pantalla de inicio". En Android, el navegador suele ofrecer directamente una notificación de "Añadir a la pantalla de inicio". Una vez instalado, Silentium aparece con su icono dedicado y funciona como una aplicación nativa, pero requiere una conexión a Internet para sincronizar las transacciones.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Creación de carteras



En el primer inicio, elija "Crear Wallet" para generate una nueva cartera, o "Restaurar Wallet" para restaurar desde una frase de recuperación existente.



Seleccione "Crear Wallet". La aplicación genera una frase de 12 palabras que debe escribir cuidadosamente. Esta frase es la única manera de recuperar sus fondos. Incluso en testnet, adopte buenas prácticas de copia de seguridad. Pulse "Continuar" después de guardar su frase.



A continuación, la aplicación le pedirá que establezca una contraseña para proteger el acceso al wallet. Elija una contraseña segura y confírmela.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Una vez confirmada la frase y establecida la contraseña, accederás a la interfaz principal.



### Interface principales y parámetros



La interfaz principal muestra su saldo en satoshis (inicialmente 0 sats), con tres botones en la parte inferior:




- Sync**: sincroniza wallet con blockchain
- Recibir**: recibir fondos
- Enviar**: para enviar bitcoins



Acceda a Ajustes a través del icono situado en la parte superior derecha (tres barras horizontales). El menú Ajustes ofrece varias opciones:





- Acerca de**: información sobre la solicitud
- Copia de seguridad**: copia de seguridad de la frase de recuperación
- Explorador**: seleccione el explorador de blockchain (Mempool por defecto) y el servidor Silentiumd
- Red**: selección de red (mainnet/testnet)
- Contraseña**: cambiar contraseña
- Recarga**: recarga del wallet
- Reinicio**: reinicio completo
- Tema**: cambiar el tema



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



La sección **Explorer** es particularmente importante: le permite elegir el explorador de blockchain utilizado (Mempool por defecto) y también muestra la URL del servidor Silentiumd (`https://bitcoin.silentium.dev/v1` para mainnet). Si aloja su propio servidor Silentiumd o desea utilizar testnet, aquí es donde debe configurar estos parámetros.



### Recepción de fondos



Desde la interfaz principal, pulse el botón "Recibir". Por defecto, Silentium muestra una dirección de Silent Payment con su código QR. La dirección empieza por `sp1...` en mainnet o `tsp1...` en testnet.



Puede cambiar entre el pago silencioso y las direcciones clásicas de Bitcoin utilizando el botón "Cambiar a dirección clásica" / "Cambiar a dirección silenciosa" en la parte inferior de la pantalla.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Una vez emitida la transacción, espere unos minutos. Para los pagos silenciosos, Silentium escanea automáticamente la blockchain en busca de transacciones destinadas a usted. Las transacciones aparecen con el estado "Sin confirmar" antes de confirmarse progresivamente.



### Enviar un pago



Desde la interfaz principal, pulse el botón "Enviar". La pantalla de envío te preguntará :



1. **Address**: pegue una dirección de Pago silencioso (`sp1...` o `tsp1...`) o una dirección clásica de Bitcoin. Puede utilizar el icono de escaneo QR para escanear una dirección.


2. **Importe**: introduzca el importe en satoshis que desea enviar. Aparece un teclado numérico para facilitar la introducción. Su saldo disponible aparece en la parte superior como referencia.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Una vez que haya introducido la dirección y el importe, pulse "Continuar" para proseguir. La aplicación le pedirá que seleccione el nivel de comisión deseado antes de confirmar la transacción.



## wallet autoalojamiento



### ¿Por qué autoalojarse?



El alojamiento local de Silentium ofrece total soberanía, verificación del código, un entorno de desarrollo y resistencia ante fallos del sitio oficial.



### Requisitos previos



Node.js (versión 14+), npm o yarn, Git y unos 500 MB de espacio en disco.



### Instalación local



Clone el repositorio e instale el archivo :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Lanzamiento y uso



Inicie la aplicación en modo de desarrollo:



```bash
yarn start
```



Vaya a `http://localhost:3000` en su navegador. Para una versión de producción optimizada :



```bash
yarn build
```



Los archivos generados en `build/` pueden ser servidos con nginx, Apache o cualquier servidor web. Por defecto, Silentium se conecta al servidor público `bitcoin.silentium.dev`. Modifique esta configuración en los parámetros para utilizar testnet o su propio servidor.



## El servidor Silentiumd



### Función y funcionamiento



Silentium utiliza un servidor de indexación **Silentiumd** para optimizar la detección de pagos. Escanear todas las transacciones de Taproot sería demasiado engorroso para un navegador o un teléfono móvil.



Silentiumd precalcula datos intermedios (tweaks) para cada transacción de Taproot. Su wallet descarga estos tweaks (unos pocos bytes por transacción) y realiza el cálculo final localmente, verificando la propiedad del pago. El servidor nunca conoce tus claves ni puede identificar tus transacciones, a diferencia de los servidores convencionales de Electrum.



Los filtros compactos BIP158 permiten a su wallet determinar qué bloques escanear sin revelar sus direcciones, preservando así su confidencialidad.



### Servidor público



El servidor público `bitcoin.silentium.dev` (mainnet), patrocinado por Vulpem Ventures, ofrece una experiencia sencilla e inmediata. Aunque se preserva la confidencialidad, este enfoque implica una confianza relativa en la infraestructura de terceros.



### Aloje su propio servidor Silentiumd



Para una soberanía total, aloja tu propio servidor Silentiumd. Requisitos previos: Nodo Bitcoin Core non-elagged con `txindex=1` y `blockfilterindex=1`, Go 1.21+, 10-20 GB de espacio en disco, conocimientos de administración de sistemas.



**Instalación:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Configurar mediante variables de entorno (ver el repositorio `config.md` para más detalles). El servidor indexa la cadena de bloques y expone una API que puede ser consultada por tu wallet.



Actualmente no existen soluciones empaquetadas para Umbrel o Start9, lo que limita la accesibilidad a los usuarios no técnicos.



## Ventajas y limitaciones



### Destacados





- Máxima accesibilidad**: uso desde cualquier navegador, sin necesidad de instalación pesada
- Multiplataforma**: funciona en móvil (Android/iOS) y escritorio gracias a la tecnología PWA
- Autoalojamiento sencillo**: instalación local posible con unos pocos comandos
- Código abierto**: código totalmente auditable en GitHub
- Privacidad**: sin seguimiento, sin análisis, cálculos criptográficos locales
- Arquitectura independiente**: separación clara entre wallet (cliente) y el servidor de indexación
- Sin cuenta**: no es necesario registrarse ni introducir datos personales



### Limitaciones a tener en cuenta





- Proyecto experimental**: prueba de concepto únicamente, no destinado al uso diario ni a la producción
- Sin garantías**: riesgo de errores, vulnerabilidades, posible pérdida de fondos
- Soporte limitado**: poca documentación para el usuario, comunidad reducida, sin soporte oficial
- Dependencia del servidor**: requiere un servidor Silentiumd en funcionamiento (público o autoalojado)
- Escaneado intensivo**: La detección silenciosa de pagos consume ancho de banda
- Funcionalidad reducida**: sin control de monedas, sin Lightning, sin multifirmas



## Buenas prácticas



### Seguridad seed



Incluso en testnet, tómate en serio tu frase de recuperación. Anótala y guárdala en un lugar seguro. Mantén carteras separadas para testnet y mainnet: nunca utilices una seed de prueba en una wallet destinada a fondos reales.



### Verificación del código fuente



Una de las ventajas del autoalojamiento es la posibilidad de comprobar el código fuente antes de ejecutarlo. Si está planeando utilizar Silentium con fondos reales, tómese el tiempo necesario para auditar el código o pídale a un desarrollador de confianza que lo haga. Compara también el hash del código desplegado en `app.silentium.dev` con el del repositorio de GitHub para asegurarte de su autenticidad.



### Copia de seguridad y restauración



La recuperación de fondos de Pagos Silenciosos requiere una wallet compatible con el protocolo BIP-352. Una wallet estándar no puede escanear la blockchain para recuperar sus Pagos Silenciosos UTXO. Mantenga Silentium instalado o asegúrese de tener acceso a otro wallet compatible (como Cake Wallet u otras implementaciones futuras) para restaurar sus fondos en caso necesario.



## Conclusión



Silentium proporciona un campo de pruebas accesible para comprender Silent Payments sin fricciones técnicas. Como prueba de concepto, demuestra cómo esta tecnología de privacidad puede integrarse en un navegador wallet preservando la autocustodia. Experimente en testnet para descubrir este prometedor avance para la privacidad de on-chain.



## Recursos



### Documentación oficial




- Repositorio GitHub de Silentium (wallet): https://github.com/louisinger/silentium
- Repositorio GitHub de Silentiumd (servidor): https://github.com/louisinger/silentiumd
- Aplicación web: https://app.silentium.dev/
- Sitio de la comunidad de Pagos Silenciosos: https://silentpayments.xyz
- Especificación BIP-352: https://bips.dev/352



### Artículos y recursos




- Anuncio oficial (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Pagos silenciosos: https://bitcoinops.org/en/topics/silent-payments/



### Herramientas Testnet




- Grifo Testnet: https://testnet-faucet.com/
- Explorador de testnet Mempool: https://mempool.space/testnet
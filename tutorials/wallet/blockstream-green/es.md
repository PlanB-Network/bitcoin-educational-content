---
name: Blockstream Green - Mobile
description: Crear una cartera de software móvil
---
![cover](assets/cover.webp)

Un monedero software es una aplicación instalada en un ordenador, smartphone u otro dispositivo conectado a Internet, que le permite gestionar y proteger las claves de su monedero Bitcoin. A diferencia de los monederos hardware, que aíslan las claves privadas, los monederos "calientes" operan por tanto en un entorno potencialmente expuesto a ciberataques, lo que aumenta el riesgo de piratería y robo.

Los monederos software deberían utilizarse para gestionar cantidades razonables de bitcoins, especialmente para las transacciones cotidianas. También pueden ser una opción interesante para personas con activos limitados en bitcoins, para quienes la inversión en un monedero físico puede parecer desproporcionada. Sin embargo, su exposición constante a Internet las hace menos seguras para almacenar tus ahorros a largo plazo o grandes fondos. Para esto último, es mejor optar por soluciones más seguras, como los monederos físicos.

En este tutorial, me gustaría presentarte una de las mejores soluciones de monedero electrónico para móviles: **Blockstream Green**.

![GREEN](assets/fr/01.webp)

Si quieres saber cómo utilizar Blockstream Green en tu ordenador, consulta este otro tutorial:

https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da
## Presentación de Blockstream Green

Blockstream Green es un monedero de software disponible en móvil y escritorio. Anteriormente conocido como *Green Address*, este monedero se convirtió en un proyecto de Blockstream tras su adquisición en 2016.

Green es una aplicación particularmente fácil de usar, lo que la hace interesante para los principiantes. Ofrece todas las características esenciales de un buen monedero Bitcoin, incluyendo RBF (*Replace-by-Fee*), una opción de conexión Tor, la posibilidad de conectar tu propio nodo, SPV (*Simple Payment Verification*), etiquetado y control de monedas.

Blockstream Green también es compatible con la red Liquid, una cadena lateral de Bitcoin desarrollada por Blockstream para realizar transacciones rápidas y confidenciales fuera de la cadena de bloques principal. Este tutorial se centra exclusivamente en Bitcoin, pero en otro posterior se tratará el uso de Liquid.

## Instalación y configuración de la aplicación Blockstream Green

El primer paso es, por supuesto, descargar la aplicación Green. Ve a tu tienda de aplicaciones:

- [Para Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Para Apple](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).
![GREEN](assets/fr/02.webp)

Los usuarios de Android también pueden instalar la aplicación a través del archivo `.apk` [disponible en GitHub de Blockstream](https://github.com/Blockstream/green_android/releases).

![GREEN](assets/fr/03.webp)

Inicie la aplicación y marque la casilla "Acepto las condiciones...*".

![GREEN](assets/fr/04.webp)

Al abrir Green por primera vez, aparece la pantalla de inicio sin ninguna cartera configurada. Más adelante, si creas o importas carteras, aparecerán en esta interfaz. Antes de pasar a crear una cartera, te aconsejo que ajustes la configuración de la aplicación para adaptarla a tus necesidades. Haga clic en "Configuración de la aplicación".

![GREEN](assets/fr/05.webp)

La opción "*Privacidad mejorada*", disponible solo en Android, mejora la privacidad desactivando las capturas de pantalla y ocultando las vistas previas de las aplicaciones. También bloquea automáticamente el acceso a las aplicaciones en cuanto se bloquea el teléfono, lo que dificulta la exposición de tus datos.

![GREEN](assets/fr/06.webp)

Para aquellos que deseen mejorar su privacidad, la aplicación ofrece la opción de enrutar tu tráfico a través de Tor, una red que encripta todas tus conexiones y dificulta el rastreo de tus actividades. Aunque esta opción puede ralentizar ligeramente el funcionamiento de la aplicación, es muy recomendable para proteger tu privacidad, especialmente si no utilizas tu propio nodo completo.

![GREEN](assets/fr/07.webp)

Para los usuarios que dispongan de su propio nodo completo, Green Wallet ofrece la posibilidad de conectarse a él a través de un servidor Electrum, garantizando un control total sobre la información de la red Bitcoin y la distribución de las transacciones.

![GREEN](assets/fr/08.webp)

Otra función alternativa es la opción "*SPV Verification*", que permite verificar directamente determinados datos del blockchain y reducir así la necesidad de confiar en el nodo predeterminado de Blockstream, aunque este método no ofrece todas las garantías de un nodo completo.

![GREEN](assets/fr/09.webp)

Una vez que hayas ajustado estos parámetros a tus necesidades, pulsa el botón "*Guardar*" y reinicia la aplicación.

![GREEN](assets/fr/10.webp)

## Crear un monedero Bitcoin en Blockstream Green

Ya está listo para crear un monedero Bitcoin. Haga clic en el botón "*Get Started*".

![GREEN](assets/fr/11.webp)

Puedes elegir entre crear un monedero de software local o gestionar un monedero frío a través de un monedero de hardware. Para este tutorial, nos concentraremos en crear un monedero en caliente, por lo que tendrás que seleccionar la opción "*En este dispositivo*". En un futuro tutorial, te mostraré cómo utilizar la otra opción.

La opción "*Watch-only*", por su parte, permite importar una clave pública extendida (`xpub`) para ver las transacciones de una cartera sin poder gastar los fondos asociados, lo que resulta práctico para realizar el seguimiento de una cartera en una cartera de hardware, por ejemplo.

![GREEN](assets/fr/12.webp)

A continuación, puede elegir entre restaurar un monedero Bitcoin existente o crear uno nuevo. Para los propósitos de este tutorial, crearemos un nuevo monedero. Sin embargo, si necesitas regenerar un monedero Bitcoin existente a partir de su frase mnemotécnica, por ejemplo tras la pérdida de tu monedero hardware, tendrás que elegir la segunda opción.

![GREEN](assets/fr/13.webp)

A continuación, puede elegir entre una frase mnemotécnica de 12 o 24 palabras. Esta frase le permitirá recuperar el acceso a su monedero desde cualquier software compatible en caso de problema con su teléfono. Actualmente, optar por una frase de 24 palabras no ofrece más seguridad que una frase de 12 palabras. Por lo tanto, le recomiendo que elija una frase mnemotécnica de 12 palabras.

Green te proporcionará entonces tu frase mnemotécnica. Antes de continuar, asegúrate de que no te están observando. Haz clic en "*Mostrar frase de recuperación*" para que aparezca en pantalla.

![GREEN](assets/fr/14.webp)

**Esta mnemotecnia te da acceso completo y sin restricciones a todos tus bitcoins ** Cualquiera en posesión de esta mnemotecnia puede robar tus fondos, incluso sin acceso físico a tu teléfono.

Restaura el acceso a tus bitcoins en caso de pérdida, robo o rotura de tu teléfono. Así que es muy importante hacer una copia de seguridad cuidadosamente **en un soporte físico (no digital)** y guardarla en un lugar seguro. Puedes escribirla en un papel o, para mayor seguridad, si se trata de un monedero grande, te recomiendo grabarla en un soporte de acero inoxidable para protegerla del riesgo de incendio, inundación o derrumbe (para un monedero caliente diseñado para asegurar una pequeña cantidad de bitcoins, una simple copia de seguridad en papel probablemente sea suficiente).

*Obviamente, nunca debes compartir estas palabras en Internet, como hago yo en este tutorial. Esta cartera de muestra sólo se utilizará en Testnet y se borrará al final del tutorial.*

![GREEN](assets/fr/15.webp)

Una vez que haya grabado correctamente su frase mnemotécnica en un soporte físico, haga clic en "*Continuar*". Cartera Verde le pedirá que confirme algunas de las palabras de su frase mnemotécnica para asegurarse de que las ha grabado correctamente. Rellene los espacios en blanco con las palabras que faltan.

![GREEN](assets/fr/16.webp)

Elige el código PIN de tu dispositivo, que se utilizará para desbloquear tu monedero verde. Es su protección contra el acceso físico no autorizado. Este código PIN no interviene en la derivación de las claves criptográficas de su monedero. Por lo tanto, incluso sin acceso a este código PIN, la posesión de su frase mnemotécnica de 12 o 24 palabras le permitirá recuperar el acceso a sus bitcoins.

Te recomendamos que elijas un código PIN de 6 dígitos lo más aleatorio posible. Asegúrate de guardar este código para no olvidarlo, ya que de lo contrario te verás obligado a recuperar tu monedero a partir de la mnemotecnia. A continuación, puedes añadir una opción de bloqueo biométrico para evitar tener que introducir el PIN cada vez que la utilices. En general, los datos biométricos son mucho menos seguros que el propio PIN. Así que, por defecto, te aconsejo que no configures esta opción de desbloqueo.

![GREEN](assets/fr/17.webp)

Introduzca su PIN una segunda vez para confirmarlo.

![GREEN](assets/fr/18.webp)

Espere a que se cree su cartera y haga clic en el botón "*Crear una cuenta*".

![GREEN](assets/fr/19.webp)

A continuación, puedes elegir entre un monedero estándar de firma única, que utilizaremos en este tutorial, o un monedero protegido por autenticación de dos factores (2FA).

![GREEN](assets/fr/20.webp)

La opción 2FA en Green crea un monedero multifirma 2/2, con una clave en poder de Blockstream. Esto significa que para realizar una transacción se necesitan las dos claves: una local protegida por tu código PIN en el teléfono, y otra remota asegurada por la 2FA en los servidores de Blockstream. En caso de pérdida de acceso a la 2FA o indisponibilidad de los servicios de Blockstream, los mecanismos de recuperación basados en scripts de bloqueo temporal garantizan que tus fondos puedan recuperarse de forma autónoma. Aunque esta configuración reduce significativamente el riesgo de robo de tus bitcoins, es más compleja de gestionar y depende en parte de Blockstream. Para este tutorial, optaremos por un monedero clásico de firma única, con las claves almacenadas localmente en el teléfono.

Su monedero Bitcoin ha sido creado con la aplicación Green

![GREEN](assets/fr/21.webp)

Antes de recibir tus primeros bitcoins en tu monedero, **te aconsejo encarecidamente que realices una prueba de recuperación en vacío**. Anota algunos datos de referencia, como tu xpub o la primera dirección de recepción, y luego borra tu monedero en la aplicación Green mientras esté vacío. A continuación, intenta restaurar tu monedero en Green utilizando tus copias de seguridad en papel. Comprueba que la información de la cookie generada tras la restauración coincide con la que anotaste originalmente. Si es así, puede estar seguro de que sus copias de seguridad en papel son fiables. Para saber más sobre cómo realizar una recuperación de prueba, consulta este otro tutorial:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Crear una cartera en Blockstream Green

Si desea personalizar su cartera, haga clic en los tres puntitos de la esquina superior derecha.

![GREEN](assets/fr/22.webp)

La opción "*Renombrar*" le permite personalizar el nombre de su cartera, lo que resulta especialmente útil si gestiona varias carteras en la misma aplicación.

![GREEN](assets/fr/23.webp)

El menú "*Unidad*" te permite cambiar la unidad base de tu monedero. Por ejemplo, puedes elegir mostrarlo en satoshis en lugar de bitcoins.

![GREEN](assets/fr/24.webp)

El menú "*Configuración*" permite acceder a las distintas opciones de su monedero Bitcoin.

![GREEN](assets/fr/25.webp)

Aquí, por ejemplo, encontrarás tu clave pública extendida y su *descriptor*, útil si planeas configurar un monedero en modo watch-only desde este monedero.

![GREEN](assets/fr/26.webp)

También puedes cambiar el PIN de tu monedero y activar una conexión biométrica.

![GREEN](assets/fr/27.webp)

## Uso de Blockstream Green

Ahora que su monedero Bitcoin está configurado, ¡está listo para recibir sus primeros sats! Simplemente haga clic en el botón "*Recibir*".

![GREEN](assets/fr/28.webp)

Green mostrará entonces la primera dirección de recepción en blanco en tu monedero. Puedes escanear el código QR asociado o copiar directamente la dirección para enviar bitcoins. Este tipo de dirección no especifica la cantidad que debe enviar el pagador. Sin embargo, puedes generar una dirección que solicite una cantidad específica, haciendo clic en los tres pequeños puntos de la esquina superior derecha, luego en "*Solicitar cantidad*", e introduciendo la cantidad deseada.

Como estás utilizando una cuenta Segwit v0 (BIP84), tu dirección empezará por `bc1q...`. En mi ejemplo, estoy usando una cartera Testnet, por lo que el prefijo es ligeramente diferente.

![GREEN](assets/fr/29.webp)

Cuando la transacción se difunda en la red, aparecerá en su monedero.

![GREEN](assets/fr/30.webp)

Espere a recibir suficientes confirmaciones para considerar que la transacción es definitiva.

![GREEN](assets/fr/31.webp)

Con bitcoins en tu monedero, ahora también puedes enviar bitcoins. Haz clic en "*Enviar*".

![GREEN](assets/fr/32.webp)

En la página siguiente, introduce la dirección del destinatario. Puedes introducirla manualmente o escanear un código QR.

![GREEN](assets/fr/33.webp)

Elija el importe del pago.

![GREEN](assets/fr/34.webp)

En la parte inferior de la pantalla, puede seleccionar el tipo de comisión para esta transacción. Puede elegir entre seguir las recomendaciones de la aplicación o personalizar sus tarifas. Cuanto más alta sea la tarifa en relación con otras transacciones pendientes, más rápido se procesará su transacción. Para obtener información sobre el mercado de comisiones, visite [Mempool.space](https://mempool.space/) en la sección "*Cargos por transacción*".

![GREEN](assets/fr/35.webp)

Pulse "*Siguiente*" para acceder a la pantalla de resumen de la transacción. Compruebe que la dirección, el importe y los cargos son correctos.

![GREEN](assets/fr/36.webp)

Si todo va bien, deslice el botón verde de la parte inferior de la pantalla hacia la derecha para firmar y difundir la transacción en la red Bitcoin.

![GREEN](assets/fr/37.webp)

Su transacción aparecerá ahora en el panel de control de su monedero Bitcoin, a la espera de confirmación.

![GREEN](assets/fr/38.webp)

*Este tutorial está basado en [una versión original perteneciente a Bitstack](https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet) escrita por Loïc Morel. Bitstack es un neobanco Bitcoin francés que ofrece la posibilidad de ahorrar en bitcoins, ya sea en DCA (Dollar Cost Averaging), o a través de un sistema de redondeo automático para los gastos diarios.* Bitstack es un neobanco Bitcoin francés que ofrece la posibilidad de ahorrar en bitcoins, ya sea en DCA (Dollar Cost Averaging), o a través de un sistema de redondeo automático para los gastos diarios
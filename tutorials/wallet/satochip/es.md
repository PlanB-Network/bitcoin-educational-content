---
name: Satochip
description: Configuración y uso de una tarjeta inteligente Satochip
---
![cover](assets/cover.webp)

Una cartera de hardware es un dispositivo electrónico dedicado a gestionar y asegurar las claves privadas de una cartera de Bitcoin. A diferencia de las carteras de software (o carteras calientes) instaladas en máquinas de propósito general a menudo conectadas a Internet, las carteras de hardware permiten el aislamiento físico de las claves privadas, reduciendo los riesgos de hackeo y robo.

El objetivo principal de una cartera de hardware es minimizar las funcionalidades del dispositivo para reducir su superficie de ataque. Una superficie de ataque más pequeña también significa menos vectores de ataque potenciales, es decir, menos debilidades en el sistema que los atacantes podrían explotar para acceder a los bitcoins.

Se recomienda usar una cartera de hardware para asegurar tus bitcoins, especialmente si posees cantidades significativas, ya sea en valor absoluto o como proporción de tus activos totales.

Las carteras de hardware se utilizan en combinación con software de gestión de carteras en una computadora o smartphone. Este software gestiona la creación de transacciones, pero la firma criptográfica necesaria para validar estas transacciones se realiza únicamente dentro de la cartera de hardware. Esto significa que las claves privadas nunca están expuestas a un entorno potencialmente vulnerable.

Las carteras de hardware ofrecen una doble protección para el usuario: por un lado, aseguran tus bitcoins contra ataques remotos manteniendo las claves privadas fuera de línea, y por otro lado, generalmente ofrecen una mejor resistencia física contra intentos de extraer las claves. Y es precisamente en estos 2 criterios de seguridad en los que se puede juzgar y clasificar los diferentes modelos disponibles en el mercado.

En este tutorial, propongo descubrir una de estas soluciones: el Satochip.

## Introducción a Satochip

El Satochip es una cartera de hardware en forma de tarjeta con un chip certificado *EAL6+*, que es un estándar de seguridad muy alto (*NXP JCOP*). Es producido por una compañía belga.

![SATOCHIP](assets/notext/01.webp)

Esta tarjeta inteligente se vende por €25, lo que es muy asequible en comparación con otras carteras de hardware en el mercado. El chip es un elemento seguro que asegura una muy buena resistencia contra ataques físicos. Además, su código es de fuente abierta (*AGPLv3*).
Sin embargo, debido a su formato, el Satochip no ofrece tantas opciones como otros hardware. Obviamente no hay batería, ni cámara, ni lector de tarjetas micro SD, ya que es una tarjeta. Su mayor desventaja, en mi opinión, es la falta de una pantalla en la cartera de hardware, lo que la hace más vulnerable a ciertos tipos de ataques remotos. De hecho, esto obliga al usuario a firmar a ciegas y a confiar en lo que ve en la pantalla de su computadora.

A pesar de sus limitaciones, el Satochip sigue siendo interesante debido a su precio reducido. Esta cartera puede ser usada notablemente para mejorar la seguridad de una cartera de gastos además de una cartera de ahorros protegida por una cartera de hardware equipada con pantalla. También constituye una buena solución para aquellos que poseen pequeñas cantidades de bitcoins y no desean invertir cien euros en un dispositivo más sofisticado. Además, el uso de Satochips en configuraciones multisig, o potencialmente en sistemas de carteras con timelock en el futuro, puede ofrecer ventajas interesantes.

La compañía Satochip también ofrece 2 otros productos. Está el Satodime, que es una tarjeta portadora diseñada para almacenar bitcoins fuera de línea, pero no permite realizar transacciones. Es una especie de cartera de papel que es mucho más segura, que puede ser usada, por ejemplo, para hacer un regalo. Finalmente, está el Seedkeeper, que es un gestor de frases mnemotécnicas. Puede ser usado para guardar de manera segura nuestra semilla sin que esté directamente anotada en un pedazo de papel.

## ¿Cómo comprar un Satochip?
El Satochip está disponible para la venta [en el sitio web oficial](https://satochip.io/product/satochip/). Para comprarlo en una tienda física, también puedes encontrar [la lista de revendedores certificados](https://satochip.io/resellers/) en el sitio web de Satochip.
Para interactuar con tu software de gestión de cartera, el Satochip ofrece dos posibilidades: a través de comunicación NFC o mediante un lector de tarjetas inteligentes. Para la opción NFC, asegúrate de que tu máquina sea compatible con esta tecnología o consigue un lector NFC externo. El Satochip opera a la frecuencia estándar de 13.56 MHz. De lo contrario, también puedes comprar un lector de tarjetas inteligentes. Puedes encontrar uno en el sitio web de Satochip o en otro lugar.

![SATOCHIP](assets/notext/02.webp)

## ¿Cómo configurar un Satochip con Sparrow?

Una vez que hayas recibido tu Satochip, el primer paso es examinar el empaque para asegurarte de que no haya sido abierto. El empaque del Satochip debe incluir una etiqueta de sellado. Si esta etiqueta falta o está dañada, podría indicar que la tarjeta inteligente ha sido comprometida y podría no ser auténtica.
![SATOCHIP](assets/notext/03.webp)
Encontrarás el Satochip dentro.

![SATOCHIP](assets/notext/04.webp)

Para gestionar la cartera, en este tutorial, sugiero usar Sparrow. Si aún no tienes el software, [visita el sitio web oficial para descargarlo](https://sparrowwallet.com/download/). También puedes consultar nuestro tutorial sobre Sparrow Wallet (próximamente).

![SATOCHIP](assets/notext/05.webp)

Inserta tu Satochip en el lector de tarjetas inteligentes o colócalo sobre el lector NFC, y conecta el lector a tu computadora en la que Sparrow está abierto.

![SATOCHIP](assets/notext/06.webp)

Abre Sparrow Wallet y asegúrate de estar correctamente conectado a un nodo de Bitcoin. Para hacerlo, verifica la marca de verificación en la parte inferior derecha: debería ser amarilla si estás conectado a un nodo público, verde para una conexión a Bitcoin Core o azul para Electrum.

![SATOCHIP](assets/notext/07.webp)

En Sparrow Wallet, haz clic en la pestaña "*File*".

![SATOCHIP](assets/notext/08.webp)

Luego en el menú "*New Wallet*".

![SATOCHIP](assets/notext/09.webp)

Elige un nombre para tu cartera y luego haz clic en "*Create Wallet*".

![SATOCHIP](assets/notext/10.webp)

Haz clic en el botón "*Connected Hardware Wallet*".

![SATOCHIP](assets/notext/11.webp)

Haz clic en el botón "*Scan...*".

![SATOCHIP](assets/notext/12.webp)

Tu Satochip debería aparecer. Haz clic en "*Import Keystore*".

![SATOCHIP](assets/notext/13.webp)

A continuación, necesitas configurar un código PIN para desbloquear tu Satochip. Elige una contraseña fuerte, entre 4 y 16 caracteres. Haz una copia de seguridad de esta contraseña.

Ten en cuenta, esta contraseña no es una frase de paso. Esto significa que incluso sin esta contraseña, tu frase mnemotécnica te permitirá volver a importar tu cartera en el software si es necesario. La contraseña solo se utiliza para asegurar el acceso al propio Satochip. Es equivalente al código PIN que se encuentra en otras carteras de hardware.

Una vez que la contraseña esté ingresada, haz clic nuevamente en el botón "*Import Keystore*".

![SATOCHIP](assets/notext/14.webp)

Nota la contraseña de nuevo, luego haz clic en el botón "*Initialize*".
![SATOCHIP](assets/notext/15.webp)
Luego llegas a la ventana para generar tu frase mnemotécnica. Haz clic en el botón "*Generate New*".

![SATOCHIP](assets/notext/16.webp)
Haz una o más copias físicas de tu frase de recuperación escribiéndola en un papel o medio metálico. Ten en cuenta que esta frase otorga acceso completo a tus bitcoins sin ninguna protección adicional. Por lo tanto, si alguien la descubriera, podría robar tus bitcoins instantáneamente, incluso sin acceso a tu Satochip o su código PIN. Por lo tanto, es importante asegurar estas copias de seguridad. Además, esta frase te permite recuperar el acceso a tus bitcoins en caso de pérdida, daño al Satochip, o si olvidas tu código PIN.
![SATOCHIP](assets/notext/17.webp)

Tu billetera de Bitcoin ha sido creada con éxito.

![SATOCHIP](assets/notext/18.webp)

Haz clic nuevamente en el botón "*Import Keystore*".

![SATOCHIP](assets/notext/19.webp)

Tu billetera ahora está creada. Tus claves privadas ahora están almacenadas en la tarjeta inteligente de tu Satochip. Haz clic en el botón "*Apply*" para continuar.

![SATOCHIP](assets/notext/20.webp)

Se recomienda configurar una contraseña adicional para asegurar la información pública gestionada por Sparrow Wallet, además del código PIN de tu Satochip. Esta contraseña asegurará la seguridad del acceso a Sparrow Wallet, lo que ayuda a proteger tus claves públicas, direcciones e historial de transacciones contra cualquier acceso no autorizado.

![SATOCHIP](assets/notext/21.webp)

Ingresa tu contraseña en los dos campos, luego haz clic en el botón "*Set Password*".

![SATOCHIP](assets/notext/22.webp)

Y ahí lo tienes, tu Satochip ahora está configurado en Sparrow Wallet.

![SATOCHIP](assets/notext/23.webp)

Ahora que tu billetera está creada, puedes desconectar tu Satochip. ¡Guárdalo en un lugar seguro!

## ¿Cómo recibir bitcoins con el Satochip?

Una vez en tu billetera, haz clic en la pestaña "*Receive*".

![SATOCHIP](assets/notext/24.webp)

Sparrow Wallet genera una dirección para tu billetera. Usualmente, para otras billeteras de hardware, se aconseja hacer clic en "*Display Address*" para verificar la dirección directamente en la pantalla del dispositivo. Desafortunadamente, esta opción no está disponible con el Satochip, pero asegúrate de usarla para tus otras billeteras.

![SATOCHIP](assets/notext/25.webp)

Puedes agregar una "*Label*" para describir la fuente de los bitcoins que serán asegurados con esta dirección. Esta es una buena práctica que te ayuda a gestionar mejor tus UTXOs.

![SATOCHIP](assets/notext/26.webp)

Para más información sobre el etiquetado, también recomiendo revisar este otro tutorial:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Luego puedes usar esta dirección para recibir bitcoins.

![SATOCHIP](assets/notext/27.webp)
## ¿Cómo enviar bitcoins con Satochip?
Ahora que has recibido tus primeros sats en tu billetera segura con Satochip, ¡también puedes gastarlos! Conecta tu Satochip a tu computadora, lanza Sparrow Wallet y luego ve a la pestaña "*Send*" para construir una nueva transacción.

![SATOCHIP](assets/notext/28.webp)
Si deseas realizar control de monedas, es decir, elegir específicamente qué UTXOs consumir en la transacción, ve a la pestaña "*UTXOs*". Selecciona los UTXOs que deseas gastar y luego haz clic en "*Enviar seleccionados*". Serás redirigido a la misma pantalla de la pestaña "*Enviar*", pero con tus UTXOs ya seleccionados para la transacción.
![SATOCHIP](assets/notext/29.webp)

Ingresa la dirección de destino. También puedes ingresar múltiples direcciones haciendo clic en el botón "*+ Añadir*".

![SATOCHIP](assets/notext/30.webp)

Nota una "*Etiqueta*" para recordar el propósito de este gasto.

![SATOCHIP](assets/notext/31.webp)

Elige la cantidad enviada a esta dirección.

![SATOCHIP](assets/notext/32.webp)

Ajusta la tasa de comisión de tu transacción según el mercado actual.

![SATOCHIP](assets/notext/33.webp)

Asegúrate de que todos los parámetros de tu transacción sean correctos, luego haz clic en "*Crear Transacción*".

![SATOCHIP](assets/notext/34.webp)

Si todo es de tu satisfacción, haz clic en "*Finalizar Transacción para Firmar*".

![SATOCHIP](assets/notext/35.webp)

Haz clic en "*Firmar*".

![SATOCHIP](assets/notext/36.webp)

Haz clic en "*Firmar*" nuevamente junto a tu Satochip.

![SATOCHIP](assets/notext/37.webp)

Ingresa el código PIN de tu Satochip, luego haz clic en "*Firmar*" nuevamente para firmar tu transacción.

![SATOCHIP](assets/notext/38.webp)

Tu transacción ahora está firmada. Haz clic en "*Transmitir Transacción*" para difundirla en la red de Bitcoin.

![SATOCHIP](assets/notext/39.webp)

Puedes encontrarla en la pestaña "*Transacciones*" de Sparrow Wallet.

![SATOCHIP](assets/notext/40.webp)

¡Felicidades, ahora tienes conocimientos sobre cómo usar Satochip! Si encontraste útil este tutorial, agradecería un pulgar hacia arriba abajo. Siéntete libre de compartir este artículo en tus redes sociales. ¡Muchas gracias!
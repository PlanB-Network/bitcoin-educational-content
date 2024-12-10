---
name: Samourai Wallet - Recuperación
description: ¿Cómo recuperar bitcoins atascados en Samourai Wallet?
---
![cover](assets/cover.webp)

Tras el arresto de los fundadores de Samourai Wallet y la incautación de sus servidores el 24 de abril, algunas funcionalidades de la aplicación ahora están inoperativas, y los usuarios que no tienen su propio Dojo ya no pueden transmitir transacciones.

Después de ayudar a varios usuarios a recuperar sus bitcoins en los últimos días, creo que he encontrado la mayoría de los problemas que pueden surgir durante la restauración de un Samourai Wallet. Por lo tanto, este tutorial comenzará con un informe de situación para identificar las funcionalidades que siguen operativas y aquellas que ya no están disponibles dentro del ecosistema de Samourai Wallet y el software afectado por este incidente. A continuación, procederemos paso a paso para recuperar un Samourai Wallet utilizando el software Sparrow Wallet. Examinaremos todos los obstáculos potenciales encontrados durante este proceso y veremos soluciones para resolverlos. Finalmente, en la última parte, descubrirás los riesgos potenciales para tu privacidad tras la incautación del servidor.

*Un gran agradecimiento a [@Louferlou](https://twitter.com/Louferlou), quien ha asistido a varios usuarios en su recuperación y compartido sus experiencias conmigo, y que también ha contribuido a las pruebas para determinar qué sigue funcional.*

## ¿Samourai Wallet sigue funcionando?

Sí, **la aplicación Samourai Wallet sigue funcionando**, pero bajo ciertas condiciones.

En primer lugar, es necesario que la aplicación haya sido previamente instalada en tu smartphone. Google Play Store ha eliminado la aplicación, y el APK estaba alojado en el sitio web incautado. Por lo tanto, es complicado instalar Samourai en este momento. Podrías encontrar APKs en línea, pero te aconsejo que no los descargues a menos que estés seguro de la fuente.

Dado que la página de Samourai Wallet ya no está disponible en Google Play Store, no es posible desactivar las actualizaciones automáticas. Si la aplicación regresa a las plataformas de descarga, sería prudente **desactivar las actualizaciones automáticas** hasta que haya más información disponible sobre el desarrollo del caso.

Si Samourai Wallet ya está instalado en tu smartphone, aún deberías poder acceder a la aplicación. Para usar la funcionalidad de billetera de Samourai, es esencial conectar un Dojo. Anteriormente, los usuarios sin un Dojo personal dependían de los servidores de Samourai para acceder a la información de la blockchain de Bitcoin y para transmitir transacciones. Con la incautación de estos servidores, la aplicación ya no puede acceder a estos datos.
Si no tenías un Dojo conectado antes pero tienes uno ahora, puedes configurarlo para usar tu aplicación Samourai nuevamente. Esto implica verificar tus copias de seguridad, eliminar la billetera (la billetera, no la aplicación) y recuperar la billetera conectando tu Dojo a la aplicación. Para más detalles sobre estos pasos, puedes consultar [este tutorial, en la sección "_Preparando tu Samourai Wallet_" : COINJOIN - DOJO](https://planb.network/es/tutorials/privacy/coinjoin-dojo).
Si tu aplicación Samourai ya estaba conectada a tu propio Dojo, entonces la parte de la billetera funciona perfectamente para ti. Todavía puedes ver tu saldo y transmitir transacciones. A pesar de todo lo que está sucediendo, creo que Samourai Wallet sigue siendo el mejor software de billetera móvil en este momento. Personalmente, planeo seguir usándolo.
El principal problema que podrías encontrar es la inaccesibilidad de las cuentas Whirlpool desde la aplicación. Usualmente, Samourai intenta establecer una conexión con tu Whirlpool CLI e iniciar los ciclos de coinjoin antes de darte acceso a estas cuentas. Sin embargo, dado que esta conexión ya no es posible, la aplicación continúa buscando indefinidamente sin nunca darte acceso a las cuentas Whirlpool. En este caso, puedes recuperar estas cuentas en otro software de billetera mientras solo mantienes la cuenta de depósito en Samourai.

### ¿Qué herramientas siguen disponibles en Samourai?

Por otro lado, algunas herramientas están afectadas por el cierre del servidor o completamente no disponibles.

En cuanto a las herramientas de gasto individual, todo funciona normalmente siempre y cuando, por supuesto, tengas tu propio Dojo. Las transacciones Stonewall normales (y no Stonewall x2) funcionan sin ningún problema.

Comentarios en Twitter han resaltado que la privacidad ofrecida por una transacción Stonewall podría ahora estar reducida. El valor agregado de una transacción Stonewall radica en el hecho de que es indistinguible de una transacción Stonewall x2 en términos de estructura. Cuando un analista encuentra este patrón específico, no pueden determinar si se trata de un Stonewall estándar con un solo usuario o un Stonewall x2 que involucra a dos usuarios. Sin embargo, como veremos en los siguientes párrafos, realizar transacciones Stonewall x2 se ha vuelto más complejo debido a la no disponibilidad de Soroban. Algunos, por lo tanto, piensan que un analista podría ahora asumir que cualquier transacción con esta estructura es un Stonewall normal. Personalmente, no comparto esta suposición. Aunque las transacciones Stonewall x2 pueden ser menos frecuentes (y creo que ya lo eran antes de este incidente), el hecho de que todavía sean posibles puede invalidar un análisis completo basado en la suposición de que no lo son.
**[-> Aprende más sobre las transacciones Stonewall.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**
En cuanto a Ricochet, no he podido verificar si el servicio sigue operativo, debido a no poseer un Dojo en el Testnet, y prefiero no arriesgarme a gastar `100 000 sats` hacia una billetera que podría estar controlada por las autoridades. Si has tenido la oportunidad de probar esta herramienta recientemente, te invito a contactarme para que podamos actualizar este artículo.

Si necesitas usar Ricochet, ten en cuenta que siempre puedes realizar esta operación manualmente con cualquier software de billetera. Para aprender cómo realizar manualmente los diversos saltos correctamente, recomiendo consultar este otro artículo: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

La herramienta JoinBot ya no está operativa, ya que dependía enteramente de la participación de una billetera gestionada por Samourai.

En cuanto a otros tipos de transacciones colaborativas, a menudo referidas como "cahoots", siguen siendo posibles, pero solo manualmente. Antes del cierre del servidor, tenías dos opciones para realizar transacciones Stonewall x2 o Stowaway (PayJoin):
- Usar la red Soroban para intercambiar automáticamente y de forma remota los PSBTs;
- O realizar estos intercambios manualmente escaneando múltiples códigos QR.

Después de varias pruebas, parece que Soroban ya no funciona. Para realizar estas transacciones colaborativas, el intercambio de datos debe hacerse, por lo tanto, manualmente. Aquí hay dos opciones para realizar este intercambio:
- Si estás físicamente cerca de tu colaborador, puedes escanear los códigos QR sucesivamente;
- Si estás lejos de tu colaborador, puedes intercambiar los PSBTs a través de un canal de comunicación externo a la aplicación. Sin embargo, ten cuidado, ya que los datos contenidos en estos PSBTs son sensibles en términos de privacidad. Recomiendo usar un servicio de mensajería encriptado para asegurar la confidencialidad del intercambio.
**[-> Aprende más sobre las transacciones Stonewall x2.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4-x2)**

**[-> Aprende más sobre las transacciones Stowaway.](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**

En cuanto a Whirlpool, el protocolo ya no parece funcionar, incluso para usuarios que tienen su propio Dojo. He estado monitoreando mi RoninDojo estos últimos días e intentado algunas manipulaciones básicas, pero el CLI de Whirlpool no ha podido conectarse desde el cierre del servidor.

Sin embargo, sigo teniendo la esperanza de que este protocolo pueda ser reactivado o quizás reimaginado de manera diferente en las próximas semanas, dependiendo de cómo evolucione la situación. Esta pausa podría ser una oportunidad para explorar nuevos enfoques o posibles mejoras a este sistema.
### ¿Qué herramientas externas siguen disponibles?
En cuanto a otras herramientas relacionadas con el entorno de Samourai, algunas siguen disponibles mientras que otras no.

El sitio web gratuito de análisis de cadena OXT.me lamentablemente ya no está disponible por el momento.

La herramienta Whirlpool Stats Tool ya no está disponible para descargar, ya que estaba alojada en el GitLab de Samourai. Incluso si previamente habías descargado esta herramienta Python localmente en tu máquina, o si estaba instalada en tu nodo RoninDojo, WST no funcionará por el momento. De hecho, dependía de los datos proporcionados por OXT.me para su operación, y este sitio ya no es accesible. Actualmente, WST no es particularmente útil ya que el protocolo Whirlpool está inactivo.

El sitio KYCP.org actualmente ya no es accesible.

El GitLab que alojaba el código para la herramienta Python Boltzmann Calculator también ha sido incautado. En este momento, por lo tanto, ya no es posible descargar esta herramienta. Pero si tienes un RoninDojo, puedes continuar usando Boltzmann Calculator de la misma manera que antes.

En cuanto a RoninDojo, este software de nodo-en-caja sigue funcionando correctamente a pesar de la indisponibilidad de ciertas herramientas específicas como Whirlpool CLI y WST. Todavía puede ser utilizado para otro software de billetera gracias a Fulcrum o Electrs. Si deseas obtener más información sobre RoninDojo o si tienes preguntas específicas, te animo a unirte a [su grupo de Telegram](https://t.me/RoninDojoNode).

Sin embargo, el código fuente para RoninDojo actualmente ya no es accesible, ya que estaba alojado en el GitLab de Samourai. Por lo tanto, no es posible instalarlo manualmente en un Raspberry Pi en este momento.

En cuanto al software de billetera de solo visualización Sentinel, la situación es similar a la de la aplicación Samourai. Si tienes tu propio Dojo, puedes continuar usando Sentinel sin ningún problema. Sin embargo, si no tienes un Dojo, ya no podrás establecer una conexión. A diferencia de Samourai, el sitio web de Sentinel todavía es accesible en línea. Pero ten cuidado con este sitio y el APK ofrecido allí, ya que no está claro quién controla actualmente estos recursos.

### ¿Se ve afectado Sparrow Wallet?
Sparrow Wallet continúa operando normalmente, con la excepción de las herramientas de Samourai que ya no están disponibles. Actualmente, ya no es posible realizar coinjoins a través de Sparrow. De manera similar, las herramientas de gasto colaborativo ya no son accesibles, ya que Sparrow no ofrece la opción de intercambio manual de PSBTs, a diferencia de Samourai. Para todas las demás funcionalidades, Sparrow opera sin problemas. También puedes usar este software para recuperar una billetera de Samourai si es necesario.

## ¿Cómo recuperar una billetera Samourai?
Como hemos visto en las secciones anteriores, si posees tu propio Dojo, no es necesariamente requerido cambiar de software. **Samourai sigue siendo una excelente opción de billetera caliente** para tus gastos diarios. Sin embargo, si no tienes un Dojo o si prefieres optar por otro software, explicaré el proceso completo de recuperación, detallando cualquier obstáculo potencial que puedas encontrar.

En cualquier caso, es importante tomarte tu tiempo y asegurarte de no cometer errores. Recuerda, no hay prisa, ya que tienes tus claves privadas, y la incautación de los servidores de Samourai no afecta esto de ninguna manera. Pase lo que pase, obviamente no pueden acceder a tus claves privadas.

### Verificar la frase de paso

Para recuperar tu billetera, debes tener tu frase de paso, incluso si optas por la recuperación a través del archivo de respaldo. Comienza por verificar la validez de esta frase de paso. Abre tu aplicación Samourai Wallet, haz clic en tu icono Paynym en la parte superior izquierda, luego selecciona `Settings`.

![samourai](assets/1.webp)

A continuación, haz clic en `Troubleshooting` y luego en `Passphrase/backup test`.

![samourai](assets/2.webp)

Ingresa tu frase de paso y haz clic en `Ok`. Si es correcta, Samourai lo confirmará. También tienes la opción de verificar el archivo de respaldo si planeas usarlo más tarde.

![samourai](assets/3.webp)

Este paso es opcional pero recomendado. Confirma que la frase de paso es correcta, eliminando una fuente potencial de problemas más adelante. Si Samourai indica que la frase de paso es incorrecta en esta etapa, la recuperación no será posible. Asegúrate de haber ingresado la frase de paso correctamente y revísala nuevamente.

### Opción 1: Recuperar la billetera en Sparrow con el archivo de respaldo

Desde la versión 1.8.6 de Sparrow Wallet, es posible importar directamente tu billetera Samourai usando el archivo de texto de respaldo llamado `samourai.txt`, que tu aplicación genera automáticamente. Este archivo contiene toda la información necesaria para recuperar tu billetera y está cifrado con tu frase de paso por seguridad.

Si eliges esta opción, necesitarás tu archivo `samourai.txt` actualizado y tu frase de paso. Para generar este archivo en Samourai Wallet, haz clic en los tres pequeños puntos en la parte superior derecha, luego selecciona `Export wallet backup`.

![samourai](assets/4.webp)
A continuación, elige `Export to Clipboard`. Después de eso, necesitarás transferir este archivo a tu PC de manera segura. Dado que el archivo está cifrado, pero la frase de paso sola es suficiente para descifrarlo, es importante tomar precauciones durante su transmisión. Si optas por una transferencia directa como texto plano, necesitarás crear un archivo `samourai.txt` en tu PC y pegar el contenido del portapapeles en él. Una alternativa sería recuperar directamente el archivo `samourai.txt` de los archivos almacenados en tu teléfono.
Una vez que tengas acceso al archivo en tu PC, abre Sparrow Wallet, haz clic en la pestaña `File` y selecciona `Import Wallet` para comenzar a importar tu billetera.

![samourai](assets/5.webp)
Desplázate hasta `Samourai Backup`, haz clic en `Importar Archivo` y luego selecciona tu archivo `samourai.txt`.
![samourai](assets/6.webp)

Sparrow te pedirá entonces una contraseña para desencriptar el archivo. Esta contraseña es en realidad tu frase de paso. Ingrésala en el campo correspondiente y haz clic en `Importar`.

![samourai](assets/7.webp)

Si en esta etapa, tu billetera no aparece, es posible que hayas cometido un error al copiar el archivo `samourai.txt` o al ingresar la frase de paso. Puedes consultar la sección de solución de problemas para obtener más ayuda.

![samourai](assets/8.webp)

Para el tipo de script, si no has configurado otros scripts en Samourai, normalmente deberías usar solo SegWit V0 (SegWit Nativo / P2WPKH). Mantén este script predeterminado y haz clic en `Importar`.

![samourai](assets/9.webp)

Nombra tu billetera, por ejemplo, "Recuperación de Samourai", y luego haz clic en `Crear Billetera`.

![samourai](assets/10.webp)

Sparrow te pedirá entonces que elijas una contraseña. Esta contraseña solo protege el acceso a tu billetera en este PC y no se relaciona con la derivación de las claves de tu billetera. Asegúrate de elegir una contraseña fuerte, anótala para recordarla y haz clic en `Establecer Contraseña`.

![samourai](assets/11.webp)

Sparrow derivará entonces las claves de tu billetera y buscará las transacciones correspondientes.

![samourai](assets/12.webp)

Por ahora, solo tu cuenta de depósito es accesible. Si estabas usando Samourai solo para esta cuenta, deberías ver todos tus fondos. Sin embargo, si también estabas usando Whirlpool, necesitarás derivar las cuentas `premix`, `postmix` y `badbank`. En Sparrow, simplemente haz clic en la pestaña `Configuración`, luego en `Agregar Cuentas...`.

![samourai](assets/13.webp)
En la ventana que se abre, selecciona `Cuentas Whirlpool` del menú desplegable, luego haz clic en `OK`.
![samourai](assets/14.webp)

Entonces verás aparecer tus diversas cuentas Whirlpool, y Sparrow derivará las claves necesarias para usar los bitcoins asociados.

![samourai](assets/15.webp)

Si estás usando un software diferente a Sparrow, como Electrum, para recuperar tu billetera Samourai, aquí están los índices de cuenta de Whirlpool para la recuperación manual:
- Depósito: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Ahora tienes acceso a tus bitcoins en Sparrow. Si necesitas ayuda usando Sparrow Wallet, también puedes consultar [nuestro tutorial dedicado](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

También recomiendo importar manualmente las etiquetas que habías asociado con tus UTXOs en Samourai. Esto te permitirá realizar un control de monedas efectivo en Sparrow posteriormente.

### Opción 2: Recuperar la billetera en Sparrow con la frase mnemotécnica

Si no deseas realizar la recuperación con el archivo de respaldo, puedes optar por un método más tradicional simplemente usando tu frase de recuperación de 12 palabras y tu frase de paso. Esta segunda opción suele ser más sencilla.
Para comenzar, asegúrate de tener tu frase de recuperación y tu frase de paso a mano. Luego, abre el software Sparrow Wallet, haz clic en la pestaña `File` y selecciona `Import Wallet` para comenzar a importar tu billetera.
![samourai](assets/16.webp)

Elige `Mnemonic Words (BIP39)` y, en el menú desplegable, haz clic en `Use 12 Words`.

![samourai](assets/17.webp)

Ingresa las 12 palabras de tu frase de recuperación en el orden correcto.

![samourai](assets/18.webp)

Si Sparrow muestra un mensaje de `Invalid Checksum`, esto indica que el checksum de la frase de recuperación no es válido, lo que probablemente significa que cometiste un error al ingresar las palabras.

![samourai](assets/19.webp)

Si tu frase es correcta, marca la casilla `Use Passphrase?` e ingresa tu frase de paso en el campo dedicado. Finalmente, si todo parece correcto, haz clic en el botón `Discover Wallet`.

![samourai](assets/20.webp)

Nombra tu billetera, por ejemplo, "Samourai Recovery", luego haz clic en `Create Wallet`.

![samourai](assets/21.webp)
Sparrow te pedirá entonces que elijas una contraseña. Esta contraseña solo protege el acceso a tu billetera en este PC y no se relaciona con la derivación de las claves de tu billetera. Asegúrate de elegir una contraseña fuerte, escríbela para recordarla y haz clic en `Set Password`.
![samourai](assets/22.webp)

Sparrow derivará entonces las claves para tu billetera y buscará las transacciones correspondientes.

![samourai](assets/23.webp)

Si en esta etapa, tu billetera no aparece, es posible que hayas cometido un error al ingresar la frase de paso o la frase de recuperación. Puedes consultar la sección de solución de problemas dedicada para obtener más ayuda.

Por ahora, solo tu cuenta de depósito es accesible. Si estabas usando Samourai solo para esta cuenta, deberías ver todos tus fondos. Sin embargo, si también estabas usando Whirlpool, necesitarás derivar las cuentas `premix`, `postmix` y `badbank`. En Sparrow, simplemente haz clic en la pestaña `Settings`, luego en `Add Accounts...`.

![samourai](assets/24.webp)

En la ventana que se abre, selecciona `Whirlpool Accounts` de la lista desplegable, luego haz clic en `OK`.

![samourai](assets/25.webp)

Entonces verás aparecer tus diversas cuentas Whirlpool, y Sparrow derivará las claves necesarias para usar los bitcoins asociados.

![samourai](assets/26.webp)

Si estás usando otro software como Electrum para recuperar tu billetera Samourai, aquí están los índices de cuenta Whirlpool para la recuperación manual:
- Depósito: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Ahora tienes acceso a tus bitcoins en Sparrow. Si necesitas ayuda usando Sparrow Wallet, también puedes consultar [nuestro tutorial dedicado](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

También recomiendo importar manualmente las etiquetas que habías asociado con tus UTXOs en Samourai. Esto te permitirá realizar un control de monedas efectivo en Sparrow posteriormente.

### ¿Cuáles son los problemas comunes encontrados?
Después de asistir a varias personas en los últimos días, creo que he encontrado la mayoría de los problemas que pueden impedir la recuperación de tu billetera. Si aún no puedes acceder a tu billetera a pesar de los tutoriales anteriores, aquí tienes algunas recomendaciones adicionales. En primer lugar y lo más importante, para que la recuperación funcione, es absolutamente esencial que la frase de recuperación sea correcta. Si no puedes encontrar tu frase de 12 palabras, puedes usar *opción 1* para recuperarte del archivo de respaldo de Samourai. También puedes acceder a tu frase de recuperación directamente en Samourai Wallet navegando a `Configuración`, luego `Billetera`, y finalmente seleccionando `Mostrar frase de recuperación de 12 palabras`.

A continuación, un error de tipeo en tu frase de paso durante la recuperación resultará en claves derivadas incorrectas, lo que impedirá la recuperación de tu billetera en Sparrow. **¡La frase de paso debe ser perfectamente precisa!**

Para resolver esto, primero te aconsejo que verifiques la validez de tu frase de paso en la aplicación Samourai como se describe en la sección "_Verificar la frase de paso_" de este artículo:
1. **Validación en Samourai:** Si Samourai confirma que la frase de paso es correcta, intenta la recuperación de nuevo desde el principio, asegurándote de ingresar la frase de paso en Sparrow sin errores;
2. **Error de Frase de Paso:** Si Samourai indica que la frase de paso es incorrecta, es inútil continuar los intentos en Sparrow. Mientras no se encuentre la frase de paso correcta, la recuperación de tu billetera es imposible. Si has perdido permanentemente tu frase de paso, mantén tu aplicación Samourai segura. Todo lo que puedes hacer es esperar que los servidores se reinicien para que puedas hacer gastos directamente desde la aplicación sin necesidad de recuperación. **No intentes conectar un Dojo en este caso**, ya que esto implicaría restablecer tu billetera en Samourai, lo cual requiere acceso a la frase de paso.

Entre otros errores encontrados, muchos están relacionados con la configuración de red en Sparrow.

Primero, asegúrate de que Sparrow esté correctamente configurado en modo `mainnet` en lugar de en modo `testnet`. De hecho, si Sparrow busca tus transacciones en el Testnet, no encontrará nada, porque tu billetera está en el Mainnet. El Testnet es una versión alternativa de Bitcoin, utilizada únicamente para pruebas y desarrollo, y opera en una red separada de la red principal (Mainnet), con sus propios bloques y transacciones. Para verificar en qué red estás, haz clic en la pestaña `Herramientas`, luego en `Reiniciar en`. Si se muestra la opción `Mainnet`, entonces no estás en la red principal. Selecciónala para reiniciar Sparrow en el Mainnet, y luego comienza tu proceso de recuperación de nuevo.

![samourai](assets/27.webp)
Algunos también han encontrado dificultades para conectar Sparrow a su nodo. En la parte inferior derecha de Sparrow, un interruptor de colores indica si tu software está correctamente conectado a un nodo de Bitcoin. Para recuperar tus transacciones de Samourai, es esencial que el software esté bien conectado. Verifica que el interruptor esté activado, como en mi imagen a continuación (amarillo para un nodo público, verde para Bitcoin Core y azul para un servidor Electrum).
![samourai](assets/28.webp)

Si el interruptor no está activado, haz clic en él para reactivar la conexión.

![samourai](assets/29.webp)

Si el problema persiste, aquí tienes algunas soluciones posibles:
- Si estás intentando conectarte a tu propio servidor Electrum (azul) o tu Bitcoin Core (verde) y Sparrow no puede conectarse, verifica la información de conexión en `Archivo > Preferencias... > Servidor`;

![samourai](assets/30.webp)
- Si el problema de conexión persiste, podría deberse a una sincronización incompleta de tu nodo. Asegúrate de que tu nodo y tu indexador estén 100% sincronizados. Si es necesario como último recurso, desconecta tu nodo de Sparrow y conéctate a un nodo público; - Si ya estabas conectado a un nodo público y la conexión falla, intenta cambiar el nodo seleccionando otro de la lista desplegable.

![samourai](assets/31.webp)

Si has recuperado con éxito tu billetera, pero parece incompleta, podría haber un problema relacionado con la derivación.

Un problema podría ocurrir si usaste tu cuenta de depósito de Samourai con un tipo de script diferente a `P2WPKH`. Por defecto, Samourai usa este tipo de script, pero si lo has cambiado manualmente, también debes ajustarlo al recuperarlo en Sparrow.

Para derivar ramas para otros tipos de script, necesitas repetir el proceso de recuperación para cada tipo de script utilizado. Para esto, ve a `Archivo > Nueva Billetera` en Sparrow, selecciona otro tipo de script de la lista desplegable, haz clic en `Nueva o Importada Cartera de Software`, y sigue los mismos pasos que en el tutorial inicial.

![samourai](assets/32.webp)

Otro problema de derivación que encontré está relacionado con el valor del Límite de Brecha. Este valor le indica a Sparrow después de cuántas direcciones vacías debe dejar de derivar nuevas direcciones. Si después de la recuperación, notas que faltan algunas transacciones, esto podría deberse a un Límite de Brecha demasiado bajo. Para solucionarlo, ve a la cuenta que está causando el problema, por ejemplo, la cuenta postmezcla (si varias cuentas están afectadas, repite esta operación para cada una).

![samourai](assets/33.webp)

Haz clic en la pestaña `Configuración` y luego en el botón `Avanzado...`.
![samourai](assets/34.webp)
Aumenta gradualmente el valor del Límite de Brecha, por ejemplo, aquí lo establecí en `400`. Luego, haz clic en el botón `Cerrar`.

![samourai](assets/35.webp)

Haz clic en `Aplicar` para finalizar. Sparrow derivará entonces un mayor número de direcciones y buscará fondos en ellas, lo que debería ayudar a recuperar todas tus transacciones.

![samourai](assets/36.webp)

Eso cubre los diversos problemas de recuperación que he encontrado en los últimos días. Si, después de probar todas estas soluciones, todavía tienes problemas, te invito a unirte a [el Discord de Discover Bitcoin](https://discord.gg/xKKm29XGBb) para pedir ayuda. Visito regularmente este Discord y estaría encantado de ayudar si tengo la solución. Otros bitcoiners también podrán compartir sus experiencias y ofrecer su asistencia. **En cualquier caso, es esencial mantener tu frase de recuperación, tu archivo de respaldo y tu frase de paso confidenciales**. No los compartas con nadie, ya que esto podría permitirles robar tus bitcoins.

Una vez que la recuperación esté completa, ahora tienes acceso a tus bitcoins. Eso es algo bueno, pero podría no ser suficiente. De hecho, la incautación de servidores plantea nuevos riesgos potenciales para tu privacidad. En la siguiente sección, examinaremos estos riesgos en detalle y describiremos las precauciones a tomar para proteger tu privacidad.

## ¿Cuáles son las consecuencias para la privacidad de tus transacciones?

### Como usuario de Samourai sin Dojo

Si estabas usando Samourai Wallet sin haber conectado tu propio Dojo, tus xpubs tenían que ser comunicados a los servidores de Samourai para que la aplicación funcionara. Con la incautación de estos servidores, es posible que las autoridades ahora tengan acceso a estos xpubs.
Este escenario sigue siendo hipotético. No sabemos si estos xpubs fueron registrados, si algún almacenamiento potencial fue destruido, si las autoridades los han recuperado y si planean usarlos para análisis de cadena. Sin embargo, en tal situación, es prudente considerar el peor escenario, donde las autoridades tienen los xpubs de usuarios que no conectaron su propio Dojo. Para referencia, un xpub es una cadena de caracteres que contiene todos los elementos necesarios para generar claves públicas hijas (clave pública + código de cadena). Se utiliza en billeteras deterministas jerárquicas para generar direcciones de recepción y observar transacciones de una cuenta sin exponer las claves privadas asociadas. Esto permite, por ejemplo, la creación de una billetera "solo para ver". Sin embargo, revelar xpubs puede comprometer la privacidad del usuario, ya que permiten a terceros rastrear transacciones y ver los saldos de las cuentas asociadas.
Cualquiera que conozca tus xpubs puede ver todas las direcciones de recepción de tu billetera, las utilizadas en el pasado y las que se generarán en el futuro.

Para usuarios sin un Dojo, una posible filtración de tus xpubs tiene dos consecuencias principales:
- Los coinjoins que podrías haber realizado se vuelven ineficaces desde el punto de vista de la privacidad para cualquiera que conozca tus xpubs, por lo tanto, tus monedas pierden todo anonset;
- Esta persona también puede rastrear todas las direcciones de recepción de tu Samourai Wallet.

Por lo tanto, es importante considerar el peor escenario y deshacerse de esta billetera, potencialmente comprometida en términos de privacidad. Para hacer esto, crea una nueva billetera desde cero con otro software, como Sparrow Wallet. Después de verificar la validez de tus respaldos, transfiere todos tus fondos realizando transacciones. Aunque esta operación no rompe el enlace de rastreabilidad de tus monedas, evitará que las autoridades conozcan con certeza las direcciones de tu nueva billetera.

Durante esta operación de transferencia, recomiendo evitar la consolidación de tus monedas. Si asumimos que tus xpubs están comprometidos, la consolidación no tendrá impacto desde el punto de vista de la persona que tiene acceso a estos xpubs, ya que tu privacidad ya está comprometida con ellos. Sin embargo, te aconsejo que no consolides demasiado tus monedas principalmente para proteger tu privacidad de otras personas. En el peor de los casos, solo las autoridades podrían tener acceso a tus xpubs, pero el resto del mundo no sabe sobre ellos. Así, desde el punto de vista de los demás, consolidar tus monedas podría dañar significativamente tu privacidad debido a la Heurística de Propiedad de Entrada Común (CIOH).

Finalmente, para romper definitivamente el rastreo, considera también realizar coinjoins desde esta nueva billetera.
**Advertencia:** Simplemente recuperar tu Samourai wallet en Sparrow Wallet no es suficiente. Es necesario crear una billetera completamente nueva con una nueva frase de recuperación si quieres evitar usar xpubs que podrían haberse filtrado. Si importas tu semilla existente en Sparrow, solo estás cambiando el software de gestión de la billetera, pero la billetera sigue siendo la misma.

### Como usuario de Sparrow o Samourai con Dojo

Si tu billetera solo se gestiona en Sparrow Wallet, tus xpubs no podrían haberse filtrado, ya estés usando un nodo público o tu propio nodo de Bitcoin. De manera similar, si estás usando la aplicación Samourai y siempre has conectado esta aplicación a tu propio Dojo desde la creación de tu billetera, tus xpubs también están seguros.
Sin embargo, si has utilizado la misma billetera durante un período **sin tu propio Dojo** y luego con tu propio Dojo, es posible que los servidores de Samourai podrían haber tenido acceso a tus xpubs, y por lo tanto las autoridades podrían conocerlos. Si te encuentras en esta situación específica, te aconsejo seguir las recomendaciones de la sección anterior y considerar tus xpubs como comprometidos.
Para aquellos que siempre han utilizado Sparrow o Samourai con su propio Dojo, el principal riesgo es que los anonsets de tus monedas podrían potencialmente reducirse. Supongamos, en el peor de los casos, que todos los usuarios sin un Dojo tienen sus xpubs en manos de las autoridades, entonces el camino de sus monedas a través de los ciclos de coinjoin podría ser rastreado por estas autoridades.

Para ilustrar esto, tomemos un ejemplo concreto. Imagina que participaste en un primer ciclo de coinjoin, seguido por dos ciclos adicionales de coinjoin aguas abajo. Si los xpubs de los usuarios sin un Dojo no se han filtrado, entonces el anonset prospectivo de tu moneda sería 13.

![samourai](assets/37.webp)

Sin embargo, si consideramos que los xpubs se han filtrado y que te encontraste con un usuario sin dojo durante el coinjoin inicial, y luego con 2 durante el primer coinjoin aguas abajo, entonces tu anonset prospectivo sería solo 10 en lugar de 13 desde el punto de vista de la autoridad.

![samourai](assets/38.webp)
Esta posible disminución en el anonset es compleja de cuantificar, ya que depende de numerosos factores, y cada moneda se ve afectada de manera diferente. Por ejemplo, un usuario sin Dojo encontrado en los ciclos iniciales afecta mucho más el anonset prospectivo que uno encontrado en los ciclos posteriores. Para darte una idea de la situación, que sigue siendo hipotética, las últimas estadísticas proporcionadas por Samourai indicaron que entre el 85% y el 90% de las monedas involucradas en coinjoins provenían de usuarios con Dojo, Sparrow o Bitcoin Keeper, es decir, usuarios que, incluso en el peor de los casos, no habrían visto sus xpubs filtrados.
Aunque estas cifras son difíciles de verificar, me parecen consistentes por dos razones:
- Sparrow Wallet es ampliamente utilizado;
- La mayoría del software de nodo-en-caja ofrece implementaciones de Dojo, y estos software principales como Umbrel son muy populares hoy en día.

Por lo tanto, se deben considerar varios aspectos. Si la privacidad de tus monedas frente a las autoridades es extremadamente importante para ti, sería prudente prepararse para el peor escenario, y es difícil garantizar al 100% que tus ciclos de coinjoin en Whirlpool no podrían ser rastreados debido a la posible filtración de xpubs de usuarios sin Dojo. Aunque esta suposición es altamente improbable, no es imposible.

Por otro lado, si la privacidad de tus monedas frente a la autoridad potencialmente en posesión de estos xpubs no es crucial para ti, entonces la situación puede considerarse de manera diferente.

Específico "frente a la autoridad" porque es importante recordar que solo la autoridad que incautó los servidores es potencialmente consciente de estos xpubs. Si tu objetivo al usar coinjoin era evitar que tu panadero pudiera seguir tus fondos, entonces él no está mejor informado que antes de la incautación del servidor.
Finalmente, es esencial considerar el anonset inicial de tu moneda, antes de la incautación del servidor. Tomemos el ejemplo de una moneda que había alcanzado un anonset prospectivo de 40,000; la disminución potencial en este anonset es probablemente insignificante. De hecho, con un anonset base ya muy alto, es poco probable que la presencia de unos pocos usuarios sin Dojo pueda cambiar radicalmente la situación. Sin embargo, si tu moneda tenía un anonset de 40, entonces esta fuga potencial podría afectar seriamente tus anonsets y potencialmente permitir el rastreo. Con la herramienta WST ahora fuera de servicio tras el cierre de OXT.me, solo puedes estimar estos anonsets. Para el anonset retrospectivo, no hay demasiado de qué preocuparse ya que el modelo Whirlpool asegura que es muy alto desde el primer coinjoin, gracias al legado de tus pares. El único caso en el que esto podría representar un problema es si tu moneda no ha sido remezclada durante varios años y se mezcló al principio del lanzamiento de un pool. En cuanto al anonset prospectivo, puedes examinar la duración que tu moneda ha estado disponible para coinjoins. Si han pasado varios meses, entonces probablemente tiene un anonset prospectivo extremadamente alto. Por el contrario, si se agregó a un pool solo unas horas antes de que los servidores fueran incautados, entonces su anonset prospectivo es probablemente muy bajo.
[**-> Aprende más sobre los anonsets y su método de cálculo.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

Otro aspecto a considerar es el impacto de las consolidaciones en los anonsets de las monedas que han sido mezcladas. Dado que las cuentas de Whirlpool ya no son accesibles a través de la aplicación Samourai, es probable que muchos usuarios hayan transferido su billetera a otro software e intentado retirar sus fondos de Whirlpool. En particular, el último fin de semana, cuando las tarifas de transacción en la red Bitcoin eran relativamente altas, hubo un fuerte incentivo técnico y económico para consolidar las monedas post-mezcla. Esto significa que es probable que muchos usuarios hayan realizado consolidaciones significativas.

El problema con estas consolidaciones post-mezcla es que siempre reducen los anonsets, no solo para el usuario que las realiza, sino también para los usuarios que encontraron durante sus ciclos de coinjoin. Aunque no he podido verificar o cuantificar este fenómeno con precisión, los incentivos económicos relacionados con las tarifas de transacción en ese momento pueden llevarnos a suponer que los anonsets son potencialmente más bajos.

### Como Usuario de Sentinel

La operación de red de la aplicación de billetera solo de visualización Sentinel es similar a la de Samourai. Para acceder a la información de tu billetera, la aplicación debe transmitir los xpubs, claves públicas y direcciones que has proporcionado a un Dojo. Si siempre has usado tu propio Dojo en Sentinel, no hay problema y puedes continuar usando la aplicación sin preocupaciones. Sin embargo, si dependías de los servidores de Samourai para tu Sentinel, es posible que tus xpubs hayan sido expuestos. En este caso, es aconsejable seguir el mismo proceso de cambio de billetera recomendado para Samourai Wallet cuando se conecta a los servidores de Samourai.

En el improbable caso de que estuvieras usando tu Dojo con Samourai pero no con Sentinel, sería más prudente considerar que tus xpubs están comprometidos.

## Conclusión
Gracias por leer este artículo hasta el final. Si crees que falta información o si tienes sugerencias, por favor no dudes en contactarme para compartir tus pensamientos. Además, si necesitas asistencia adicional para recuperar tu Samourai Wallet a pesar de este tutorial, te invito a unirte al [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) para pedir ayuda. Visito regularmente este Discord y estaría encantado de asistirte si tengo la solución. Otros bitcoiners también podrán compartir sus experiencias y ofrecer su apoyo. **En cualquier caso, es esencial mantener tu frase de recuperación, tu archivo de respaldo y tu passphrase confidenciales**. No los compartas con nadie, ya que esto podría permitirles robar tus bitcoins.
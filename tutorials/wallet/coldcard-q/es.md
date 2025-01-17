---
name: COLDCARD Q
description: Configuración y utilización de una COLDCARD Q
---
![cover](assets/cover.webp)

Un monedero hardware es un dispositivo electrónico dedicado a gestionar y asegurar las claves privadas de un monedero Bitcoin. A diferencia de los monederos de software (o monederos calientes) instalados en máquinas de uso general a menudo conectadas a Internet, los monederos de hardware permiten aislar físicamente las claves privadas, lo que reduce el riesgo de piratería y robo.

El principal objetivo de un monedero hardware es reducir al máximo la funcionalidad del dispositivo para minimizar su superficie de ataque. Menos superficie de ataque también significa menos vectores de ataque potenciales, es decir, menos puntos débiles en el sistema que los atacantes podrían aprovechar para acceder a los bitcoins.

Es aconsejable utilizar un monedero físico para proteger tus bitcoins, especialmente si posees grandes cantidades, ya sea en valor absoluto o como proporción de tus activos totales.

Los monederos físicos se utilizan junto con un software de gestión de monederos en un ordenador o smartphone. Este último gestiona la creación de transacciones, pero la firma criptográfica necesaria para que estas transacciones sean válidas se realiza únicamente dentro del monedero físico. Esto significa que las claves privadas nunca están expuestas a un entorno potencialmente vulnerable.

Los monederos hardware ofrecen una doble protección al usuario: por un lado, protegen sus bitcoins contra los ataques a distancia al mantener las claves privadas fuera de línea y, por otro, ofrecen generalmente una mayor resistencia física a los intentos de extracción de las claves. Y es precisamente sobre estos 2 criterios de seguridad sobre los que podemos juzgar y clasificar los diferentes modelos del mercado.

En este tutorial, me gustaría presentarte una de estas soluciones: la **COLDCARD Q**.

---
Como la COLDCARD Q ofrece multitud de funciones, propongo dividir su uso en 2 tutoriales. En este primer tutorial, veremos la configuración inicial y las funciones básicas del dispositivo. A continuación, en un segundo tutorial, veremos cómo aprovechar todas las opciones avanzadas de su COLDCARD.

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
---
## Presentación de COLDCARD Q

COLDCARD Q es un monedero de hardware exclusivo para Bitcoin desarrollado por la empresa canadiense Coinkite, conocida por sus anteriores modelos MK. La Q representa su producto más avanzado hasta la fecha, y se posiciona como la cartera de hardware Bitcoin definitiva.

En términos de hardware, la COLDCARD Q está equipada con todas las funciones necesarias para una experiencia de usuario óptima:


- Una gran pantalla LCD simplifica la navegación y el manejo;
- Un teclado QWERTY completo;
- Cámara integrada para escanear códigos QR;
- Dos ranuras para tarjetas microSD ;
- Una opción de alimentación totalmente aislada a través de tres pilas AAA (no incluidas), o mediante un cable USB-C ;
- Dos elementos seguros de dos fabricantes diferentes para mayor seguridad;
- La capacidad de comunicarse a través de NFC.

En mi opinión, la COLDCARD Q sólo tiene dos inconvenientes. En primer lugar, debido a sus numerosas funciones, es bastante voluminosa, ya que mide casi 13 cm de largo y 8 cm de ancho, es decir, casi el tamaño de un smartphone pequeño. También es bastante grueso debido al compartimento de la batería. Si buscas una cartera de hardware más pequeña y móvil, la MK4, mucho más compacta, podría ser una mejor opción. El segundo inconveniente es, obviamente, el coste del dispositivo, que tiene un precio de **239,99 dólares** en el sitio web oficial, es decir, 72 dólares más que el MK4, lo que sitúa al Q en competencia directa con los monederos hardware premium como el Ledger Flex o el Passport de Foundation.

![CCQ](assets/fr/001.webp)

En cuanto al software, la COLDCARD Q está tan bien equipada como los demás dispositivos de Coinkite, con una gran cantidad de funciones avanzadas:


- Tira los dados para generar tu propia frase de recuperación ;
- Código PIN ;
- Cuenta atrás para el bloqueo final del PIN ;
- BIP39 frase de contraseña ;
- PIN de bloqueo final ;
- Cuenta atrás de conexión ;
- SeedXOR;
- BIP85...

En resumen, la COLDCARD Q ofrece una experiencia de usuario mejorada con respecto a la MK4, y puede ser ideal para usuarios intermedios y avanzados que busquen una mayor facilidad de uso.

La COLDCARD Q está a la venta [en el sitio web oficial de Coinkite](https://store.coinkite.com/store/coldcard). También puede adquirirse en un punto de venta.

## Preparación del tutorial

Una vez que haya recibido su COLDCARD, el primer paso es inspeccionar el embalaje para asegurarse de que no ha sido abierto. Si el embalaje está dañado, puede indicar que el monedero de hardware ha sido comprometido y puede no ser auténtico.

![CCQ](assets/fr/002.webp)

Cuando abras la caja, encontrarás los siguientes elementos:


- La COLDCARD Q en una bolsa sellada;
- Una tarjeta para anotar tu frase mnemotécnica.

![CCQ](assets/fr/003.webp)

Asegúrese de que la bolsa no ha sido desprecintada o dañada. Compruebe también que el número de la bolsa coincide con el del papel que contiene. Conserve este número para futuras consultas.

![CCQ](assets/fr/004.webp)

Si prefiere alimentar su COLDCARD sin conectarla a un ordenador (air-gap), inserte tres pilas AAA en la parte posterior del dispositivo. También puedes conectarlo al ordenador mediante un cable USB-C.

![CCQ](assets/fr/005.webp)

Para este tutorial, también necesitarás Sparrow Wallet para gestionar tu monedero Bitcoin en tu ordenador. Descarga [Sparrow Wallet](https://sparrowwallet.com/download/) desde el sitio web oficial. Te recomiendo encarecidamente que compruebes tanto su autenticidad (con GnuPG) como su integridad (mediante hash) antes de proceder con la instalación. Si no sabes cómo hacerlo, sigue este tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
## Selección del código PIN

Ahora puede encender su COLDCARD pulsando el botón situado en la esquina superior izquierda.

![CCQ](assets/fr/006.webp)

Pulse el botón "*ENTRAR*" para aceptar las condiciones de uso.

![CCQ](assets/fr/007.webp)

La COLDCARD Q mostrará un número en la parte superior de la pantalla. Asegúrese de que este número coincide con el que aparece en la bolsa precintada y en el trozo de plástico del interior de la bolsa. Esto garantiza que su paquete no ha sido abierto entre el momento en que fue empaquetado por Coinkite y el momento en que usted lo abrió. Pulse "*ENTRAR*" para continuar.

![CCQ](assets/fr/008.webp)

Navegue hasta el menú "*Elegir código PIN*" y confirme con la tecla "*ENTRAR*".

![CCQ](assets/fr/009.webp)

Este código PIN se utiliza para desbloquear su COLDCARD. Por lo tanto, es una protección contra el acceso físico no autorizado. Este código PIN no interviene en la derivación de las claves criptográficas de su monedero. Por lo tanto, incluso sin acceso a este código PIN, la posesión de su frase mnemotécnica le permitirá recuperar el acceso a sus bitcoins.

Los códigos PIN de COLDCARD se dividen en dos partes: un prefijo y un sufijo, cada uno de los cuales puede contener entre 2 y 6 dígitos, para un total de 4 a 12 dígitos. Cuando desbloquee su COLDCARD, primero tendrá que introducir el prefijo, tras lo cual el dispositivo le mostrará 2 palabras. A continuación, introduzca el sufijo. Estas dos palabras se le indicarán durante este paso de configuración, y deberá guardarlas cuidadosamente, ya que las necesitará cada vez que desbloquee su COLDCARD. Si las dos palabras mostradas durante el desbloqueo coinciden con las que guardó durante la configuración, esto confirmará que su dispositivo no ha sido comprometido desde su último uso.

Haga clic de nuevo en "*Elegir PIN*"

![CCQ](assets/fr/010.webp)

Confirme que ha leído las advertencias.

![CCQ](assets/fr/011.webp)

Ahora elegirá su código PIN. Le recomendamos un código PIN largo y aleatorio. Asegúrese de que guarda este código en un lugar distinto de donde está almacenada su COLDCARD. Puede utilizar la tarjeta suministrada en su paquete para anotar este código.

Introduzca el prefijo de su elección y, a continuación, pulse el botón "*ENTRAR*" para confirmar la primera parte del código PIN.

![CCQ](assets/fr/012.webp)

A continuación, aparecerán en su pantalla las dos palabras antiphishing. Guárdelas cuidadosamente para futuras consultas. Puede utilizar la tarjeta incluida en el paquete para anotarlas.

![CCQ](assets/fr/013.webp)

A continuación, introduzca la segunda parte de su código PIN y pulse "*ENTRAR*".

![CCQ](assets/fr/014.webp)

Confirma tu PIN introduciéndolo por segunda vez, comprobando que las dos palabras antiphishing coinciden con las que guardaste anteriormente.

![CCQ](assets/fr/015.webp)

A partir de ahora, cada vez que desbloquee su COLDCARD, recuerde comprobar la validez de las dos palabras antiphishing que aparecen en la pantalla después de introducir el prefijo de su código PIN.

## Actualización del firmware

Cuando utilices tu dispositivo por primera vez, es importante que compruebes y actualices el firmware. Para ello, accede al menú "*Avanzado/Herramientas*".

![CCQ](assets/fr/016.webp)

**Importante:** Si está planeando actualizar su firmware y no es la primera vez que utiliza COLDCARD (es decir, si ya tiene un monedero creado en COLDCARD), asegúrese de que tiene su frase mnemotécnica y de que es funcional (así como la frase de contraseña opcional, si procede). Esto es importante para evitar perder tus bitcoins en caso de problema durante la actualización del dispositivo.

Seleccione "*Actualizar Firmware*".

![CCQ](assets/fr/017.webp)

Seleccione "*Mostrar versión*".

![CCQ](assets/fr/018.webp)

Puede comprobar la versión actual del firmware de su COLDCARD. Por ejemplo, en mi caso, la versión es "*1.2.3Q*".

![CCQ](assets/fr/019.webp)

Compruebe [en el sitio web oficial de COLDCARD](https://coldcard.com/downloads) si hay disponible una versión más reciente. Haga clic en "*Descargar*" para descargar el nuevo firmware.

![CCQ](assets/fr/020.webp)

En este punto, recomendamos encarecidamente comprobar la integridad y autenticidad del firmware descargado. Para ello, descarga [el documento que contiene los hashes de todas las versiones, firmado por los desarrolladores](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), verifica la firma con [la clave pública del desarrollador](https://keybase.io/dochex), y asegúrate de que el hash indicado en el documento firmado coincide con el del firmware descargado del sitio. Si todo es correcto, puedes proceder a la actualización.

Si no estás familiarizado con este proceso de verificación, te recomiendo que sigas este tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Tome una tarjeta microSD y transfiera a ella el archivo de firmware (documento en `.dfu`). Inserta la tarjeta microSD en uno de los puertos de tu COLDCARD.

![CCQ](assets/fr/021.webp)

A continuación, en el menú de actualización del firmware, selecciona "*Desde MicroSD*".

![CCQ](assets/fr/022.webp)

Seleccione el archivo correspondiente al firmware.

![CCQ](assets/fr/023.webp)

Confirme su selección pulsando el botón "*ENTRAR*".

![CCQ](assets/fr/024.webp)

Por favor, espere mientras se actualiza el firmware.

![CCQ](assets/fr/025.webp)

Una vez completada la actualización, introduce tu código PIN para desbloquear el dispositivo.

![CCQ](assets/fr/026.webp)

Su firmware ya está actualizado.

## Parámetros COLDCARD Q

Si lo desea, puede explorar los ajustes de su COLDCARD accediendo al menú "*Ajustes*".

![CCQ](assets/fr/027.webp)

En este menú encontrarás varias opciones de personalización, como ajustar el brillo de la pantalla o seleccionar la unidad de medida por defecto.

![CCQ](assets/fr/028.webp)

Veremos otros ajustes avanzados en el próximo tutorial:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
## Crear un monedero Bitcoin

Ahora es el momento de generar un nuevo monedero Bitcoin Para ello, necesita crear una frase mnemotécnica. En Coldcard, tienes tres métodos para generar esta frase:


- Utilice sólo el generador interno de números aleatorios (TRNG);
- Utiliza una combinación de TRNG y tirada de dados para añadir entropía;
- Utiliza sólo tiradas de dados.

**Para usuarios principiantes e intermedios, recomendamos utilizar únicamente el generador de números aleatorios interno de la COLDCARD**

No recomiendo la opción de sólo dados, ya que una mala ejecución puede llevar a una sentencia con entropía insuficiente, poniendo en peligro la seguridad de tu cartera.

Sin embargo, la mejor opción es seguramente la segunda, que combina el uso de TRNG con una fuente de entropía externa. Este método garantiza una entropía mínima equivalente a la del TRNG por sí solo, y añade un nivel extra de seguridad en caso de un posible fallo del generador interno (voluntario o no). Al elegir esta opción, que combina TRNG y lanzamiento de dados, se beneficia de un mayor control sobre la generación de la sentencia, sin aumentar los riesgos en caso de mala ejecución por su parte.

Haga clic en "*Nuevas palabras semilla*".

![CCQ](assets/fr/029.webp)

Puede elegir la longitud de su frase. Te recomiendo que optes por una sentencia de 12 palabras, ya que es menos compleja de gestionar y no ofrece menos seguridad de cartera que una sentencia de 24 palabras.

![CCQ](assets/fr/030.webp)

La COLDCARD mostrará entonces su frase de recuperación generada por el TRNG. Si desea añadir entropía externa adicional, pulse la tecla "*4*".

![CCQ](assets/fr/031.webp)

Esto te llevará a una página donde puedes añadir entropía tirando los dados. Haz tantos lanzamientos como puedas (se recomienda un mínimo de 50, pero menos no es un gran problema porque ya te estás beneficiando de la entropía del TRNG), y registra los resultados con las teclas "*1*" a "*6*". Cuando hayas terminado, pulsa "*ENTRAR*" para confirmar.

![CCQ](assets/fr/032.webp)

Aparecerá una nueva frase mnemotécnica, basada en la entropía que acabas de proporcionar y en la del TRNG.

**Advertencia: Este mnemotécnico da acceso completo y sin restricciones a todos tus bitcoins**. Cualquiera que posea esta frase puede robar tus fondos, incluso sin tener acceso físico a tu COLDCARD. La frase de 12 palabras restablece el acceso a sus bitcoins en caso de pérdida, robo o rotura de su COLDCARD. Por lo tanto, es muy importante guardarla con cuidado y almacenarla en un lugar seguro.

Puede escribirla en la cartulina suministrada con su COLDCARD o, para mayor seguridad, le recomiendo que la grabe en un soporte de acero inoxidable para protegerla del riesgo de incendio, inundación o derrumbe. En cualquier caso, nunca la guardes en un soporte digital, de lo contrario podrías perder tus bitcoins.

Escriba las palabras que aparecen en la pantalla en el soporte físico de su elección. En función de tu estrategia de seguridad, puedes plantearte hacer varias copias físicas completas de la frase (pero, sobre todo, no la dividas). Es importante que las palabras estén numeradas y en orden secuencial.

Obviamente, **nunca debes compartir estas palabras** en Internet, a diferencia de lo que ocurre en este tutorial. Esta cartera de muestra se utilizará únicamente en Testnet y se borrará al final del tutorial.

Después de escribir las palabras, pulse "*ENTRAR*".

![CCQ](assets/fr/033.webp)

Para asegurarse de que ha guardado correctamente su frase, el sistema le pedirá que confirme ciertas palabras. Seleccione en el teclado el número correspondiente a cada palabra.

![CCQ](assets/fr/034.webp)

Tu monedero ya está creado En la esquina superior derecha de la pantalla, puede ver la huella digital de su clave privada maestra. Pulse "*ENTRAR*".

![CCQ](assets/fr/035.webp)

Ahora accede al menú principal de su COLDCARD.

![CCQ](assets/fr/036.webp)

## Crear una nueva cartera en Sparrow

Existen varias opciones para establecer la comunicación entre el software Sparrow Wallet y su COLDCARD. La más sencilla es utilizar un cable USB-C. Sin embargo, por defecto, su COLDCARD tiene desactivadas las comunicaciones por cable y NFC. Para reactivarlas, vaya a "*Configuración*", luego a "*Hardware activado/desactivado*" y active la opción de comunicación deseada.

![CCQ](assets/fr/037.webp)

Si prefiere mantener su COLDCARD totalmente aislada de su ordenador, puede optar por una comunicación indirecta "air-gap", utilizando códigos QR o una tarjeta microSD. Este es el método que utilizaremos en este tutorial.

Vaya a "*Avanzado/Herramientas*".

![CCQ](assets/fr/038.webp)

Seleccione "*Exportar Cartera*".

![CCQ](assets/fr/039.webp)

A continuación, selecciona "*Billetera Sparrow*".

![CCQ](assets/fr/040.webp)

Pulse "*ENTRAR*" para generar el fichero de configuración.

![CCQ](assets/fr/041.webp)

A continuación, elija cómo enviar este archivo a Sparrow. En este ejemplo, he insertado una microSD en la ranura "*A*", así que seleccionaré el botón "*1*". También puede mostrar la información como un código QR en la pantalla de su COLDCARD pulsando el botón "*QR*", y escanear este código QR con la webcam de su ordenador.

![CCQ](assets/fr/042.webp)

Inicia Sparrow Wallet y salta las páginas introductorias para llegar a la pantalla principal. Asegúrate de que estás correctamente conectado a un nodo comprobando el interruptor de la parte inferior derecha de la pantalla.

![CCQ](assets/fr/043.webp)

Es muy recomendable que utilices tu propio nodo Bitcoin. Para este tutorial, estoy usando un nodo público (amarillo), ya que estoy en la red de pruebas, pero para uso en producción, es mejor usar Bitcoin Core localmente (verde) o un servidor Electrum en un nodo remoto (azul).

Acceda al menú "*Archivo*" y seleccione "*Nueva Cartera*".

![CCQ](assets/fr/044.webp)

Dale un nombre a tu monedero y haz clic en "*Crear monedero*".

![CCQ](assets/fr/045.webp)

En el menú desplegable "*Tipo de script*", elige el tipo de script que protegerá tus bitcoins.

![CCQ](assets/fr/046.webp)

Haga clic en "*Airgapped Hardware Wallet*".

![CCQ](assets/fr/047.webp)

En la pestaña "*Coldcard*", haz clic en "*Escanear...*" si piensas escanear el código QR que aparece en tu COLDCARD, o en "*Importar archivo...*" para importar el archivo desde la microSD (se trata del archivo `.json`).

![CCQ](assets/fr/048.webp)

Tras la importación, compruebe que la "*Huella digital maestra*" que aparece en Sparrow coincide con la que aparece en su COLDCARD. Confirma la creación haciendo clic en "*Apply*".

![CCQ](assets/fr/049.webp)

Establece una contraseña fuerte para asegurar el acceso a tu Billetera Sparrow. Esta contraseña protegerá tus claves públicas, direcciones, etiquetas e historial de transacciones de accesos no autorizados.

Conviene guardar esta contraseña para no olvidarla (por ejemplo, en un gestor de contraseñas).

![CCQ](assets/fr/050.webp)

Tu monedero ya está configurado en Sparrow Wallet.

![CCQ](assets/fr/051.webp)

Antes de recibir tus primeros bitcoins en tu monedero, **te aconsejo encarecidamente que realices una prueba de recuperación en vacío**. Anota alguna información de referencia, como tu xpub, luego reinicia tu COLDCARD Q mientras la cartera está todavía vacía. A continuación, intente restaurar su monedero en la COLDCARD utilizando sus copias de seguridad en papel. Compruebe que el xpub generado tras la restauración coincide con el que anotó originalmente. Si es así, puede estar seguro de que sus copias de seguridad en papel son fiables.

Para saber más sobre cómo realizar una prueba de recuperación, te sugiero que consultes este otro tutorial:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Recibir bitcoins

Para recibir tus primeros bitcoins, empieza por encender y desbloquear tu COLDCARD.

![CCQ](assets/fr/052.webp)

En Sparrow Wallet, haz clic en la pestaña "*Recibir*".

![CCQ](assets/fr/053.webp)

Antes de utilizar la dirección propuesta por Sparrow Wallet, compruébala en la pantalla de tu COLDCARD. Esta práctica le permite confirmar que la dirección mostrada en Sparrow no es fraudulenta, y que el monedero físico posee efectivamente la clave privada necesaria para gastar posteriormente los bitcoins asegurados con esta dirección. Esto te ayuda a evitar varios tipos de ataques.

Para realizar esta comprobación, haga clic en el menú "*Explorador de direcciones*" de la COLDCARD.

![CCQ](assets/fr/054.webp)

Selecciona el tipo de script que estás usando en Sparrow. En mi caso, es Segwit P2WPKH. Hago clic en él.

![CCQ](assets/fr/055.webp)

A continuación, podrá ver sus diferentes direcciones derivadas por orden.

![CCQ](assets/fr/056.webp)

Compruebe con Sparrow que la dirección coincide. En mi caso, la dirección con ruta de derivación `m/84'/1'/0'/0/0` es efectivamente `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` tanto en Sparrow como en COLDCARD.

![CCQ](assets/fr/057.webp)

Otra forma de verificar la propiedad de esta dirección es escanear su código QR directamente en Sparrow desde su COLDCARD. En la pantalla de inicio de tu COLDCARD, selecciona "*Escanear cualquier código QR*". También puede utilizar la tecla "*QR*" del teclado.

![CCQ](assets/fr/058.webp)

Escanea el código QR de la dirección que aparece en Sparrow Wallet.

![CCQ](assets/fr/059.webp)

Asegúrate de que la dirección que aparece en tu COLDCARD coincide con la que aparece en Sparrow. A continuación, pulsa el botón "*1*".

![CCQ](assets/fr/060.webp)

La dirección queda así confirmada con éxito.

![CCQ](assets/fr/061.webp)

Ahora puedes añadir una "*Etiqueta*" para describir la fuente de bitcoins que se asegurará con esta dirección. Esta es una buena práctica que te permite gestionar mejor tus UTXOs.

![CCQ](assets/fr/062.webp)

Para más información sobre el etiquetado, también recomiendo este otro tutorial:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52
A continuación, puede utilizar esta dirección para recibir bitcoins.

![CCQ](assets/fr/063.webp)

## Enviar bitcoins

Ahora que ya has recibido tus primeros sats en tu monedero seguro COLDCARD, ¡también puedes gastarlos!

Como siempre, comience por encender y desbloquear su COLDCARD Q, luego abra Sparrow Wallet y navegue hasta la pestaña "*Enviar*" para preparar una nueva transacción.

![CCQ](assets/fr/064.webp)

Si desea "controlar la moneda", es decir, elegir específicamente qué UTXOs consumir en la transacción, vaya a la pestaña "*UTXOs*". Seleccione los UTXOs que desea gastar y, a continuación, haga clic en "*Enviar seleccionados*". Será redirigido a la misma pantalla de la pestaña "*Enviar*", pero con sus UTXOs ya seleccionados para la transacción.

![CCQ](assets/fr/065.webp)

Introduzca la dirección de destino. También puede introducir varias direcciones pulsando el botón "*+ Añadir*".

![CCQ](assets/fr/066.webp)

Escriba una "*etiqueta*" para recordar la finalidad de este gasto.

![CCQ](assets/fr/067.webp)

Seleccione el importe que desea enviar a esta dirección.

![CCQ](assets/fr/068.webp)

Ajuste el tipo de comisión de su operación en función del mercado actual.

![CCQ](assets/fr/069.webp)

Asegúrese de que todos los parámetros de la transacción son correctos y, a continuación, haga clic en "*Crear transacción*".

![CCQ](assets/fr/070.webp)

Si todo está a su satisfacción, haga clic en "*Finalizar transacción para firmar*".

![CCQ](assets/fr/071.webp)

Una vez que hayas creado tu transacción en Sparrow, es hora de firmarla con tu COLDCARD. Para transmitir la PSBT (transacción sin firmar) a tu dispositivo, tienes varias opciones. Si la transmisión de datos por cable está activada, puedes enviar la transacción directamente a través de una conexión USB-C, como lo harías con cualquier otro monedero de hardware. En este caso, en Sparrow, tendrías que hacer clic en el botón "*Firmar*" de la esquina inferior derecha. En mi ejemplo, este botón está bloqueado porque la COLDCARD no está conectada por cable.

![CCQ](assets/fr/072.webp)

Si prefieres mantener una conexión "en el aire" sin contacto directo entre el monedero hardware y tu ordenador, tienes 2 opciones. La primera, y más compleja, es utilizar una tarjeta microSD. Inserte la tarjeta microSD en su ordenador, registre la transacción a través del botón "*Guardar transacción*" de Sparrow y, a continuación, transfiera esta tarjeta a un puerto de su COLDCARD.

![CCQ](assets/fr/073.webp)

A continuación, acceda al menú "*Listo para firmar*".

![CCQ](assets/fr/074.webp)

Revise los detalles de la transacción en su COLDCARD, incluida la dirección de recepción, el importe enviado y la comisión de la transacción.

![CCQ](assets/fr/075.webp)

Si todo es correcto, pulse el botón "*ENTRAR*" para firmar la transacción.

![CCQ](assets/fr/076.webp)

A continuación, vuelva a colocar la microSD en su ordenador y en Sparrow, haga clic en "*Cargar transacción*" para cargar la transacción firmada desde la microSD. Entonces podrás realizar una comprobación final antes de subirla a la red Bitcoin.

![CCQ](assets/fr/077.webp)

El segundo método para firmar con tu COLDCARD en Air-Gap, que es mucho más sencillo que el método de la microSD, es escanear el PSBT directamente a través de la cámara del dispositivo. En Sparrow, selecciona "*Mostrar QR*".

![CCQ](assets/fr/078.webp)

En la COLDCARD, seleccione "*Escanear cualquier código QR*". También puede utilizar la tecla "*QR*" del teclado.

![CCQ](assets/fr/079.webp)

Utiliza la cámara de la COLDCARD para escanear el código QR que aparece en Sparrow.

![CCQ](assets/fr/080.webp)

Los detalles de la transacción aparecerán de nuevo para su verificación. Pulse "*ENTRAR*" para firmar si todo es de su agrado.

![CCQ](assets/fr/081.webp)

Su COLDCARD mostrará entonces la transacción firmada como un código QR. Utilice la cámara web de su ordenador para escanear este código QR seleccionando "*Escanear QR*" en Sparrow.

![CCQ](assets/fr/082.webp)

Su transacción firmada es ahora visible en Sparrow. Compruebe por última vez que todo está correcto y haga clic en "*transmitir transacción*" para transmitirla a la red Bitcoin.

![CCQ](assets/fr/083.webp)

Puedes hacer un seguimiento de tu transacción en la pestaña "*Transacciones*" de Sparrow Wallet.

![CCQ](assets/fr/084.webp)

Enhorabuena, ya conoce el uso básico de COLDCARD Q con Sparrow Wallet

Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar verde a continuación. No dudes en compartir este tutorial en tus redes sociales. Muchas gracias

También te recomiendo que eches un vistazo a este otro tutorial en el que hablamos de las opciones avanzadas de la COLDCARD Q :

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
---
name: COLDCARD Mk4
description: Guía para configurar y utilizar una COLDCARD Mk4 con Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**Los wallet de hardware** son dispositivos físicos fabricados exclusivamente para almacenar la clave privada de Bitcoin de forma segura. Almacenan las claves privadas fuera de línea, lo que significa que los piratas informáticos no pueden acceder a ellas a través de Internet. Mientras que los **software wallet** se utilizan principalmente para transacciones cotidianas, los **hardware wallet** se suelen utilizar para almacenar grandes cantidades de bitcoins de forma segura durante mucho tiempo. Cuando se realiza una transacción Bitcoin utilizando **hardware wallets**, el wallet puede firmar las transacciones dentro del dispositivo, por lo que la clave privada nunca queda expuesta a entornos conectados a Internet.


En este tutorial, exploraremos una de las wallet de hardware más populares producidas por Coinkite, la Coldcard Mk4. Vamos a echar un vistazo a cómo configurar y utilizar este hardware wallet para realizar transacciones Bitcoin.


## Visión general de Coldcard Mk4


Coldcard Mk4 es un hardware wallet fabricado por Coinkite. Este dispositivo está equipado con una pantalla, un teclado numérico y una cubierta protectora deslizante. Además, el dispositivo ofrece varias formas de conectarse e interactuar, como USB-C, funcionamiento con tapón de aire mediante una tarjeta MicroSD, NFC y un modo de disco virtual. El Mk4 también incluye funciones de seguridad avanzadas, como el BIP39 passphrase y los PIN trucados, que ofrecen a los usuarios un mayor control y protección sobre su Bitcoin.


## Configuración inicial: PIN y palabras antiphishing


Para empezar, la Coldcard Mk4 puede comprarse directamente en [Coinkite's website](https://store.coinkite.com/store). Los compradores también pueden optar por pagar con moneda fiduciaria o Bitcoin. Además, también necesitará una tarjeta MicroSD (4 GB es suficiente) y una fuente de alimentación que se pueda conectar mediante un cable USB-C (la Coldcard Mk4 solo tiene un puerto de entrada de alimentación USB-C). Ten en cuenta que, como la Mk4 no tiene batería integrada, debe estar conectada a la fuente de alimentación en todo momento mientras se utiliza.


Recibirá su Mk4 en una bolsa a prueba de manipulaciones. Asegúrate de que la bolsa no haya sido manipulada. Si detectas algún problema, como daños o roturas en la bolsa, puedes informar a Coinkite enviando un correo electrónico a support@coinkite.com. Además, en la bolsa a prueba de manipulaciones encontrarás un número de 12 dígitos, al que nos referiremos como número de bolsa del Mk4. Este número de bolsa se utilizará posteriormente para verificar que el dispositivo no ha sido manipulado durante el envío y que procede directamente de Coinkite. El número de bolsa se almacena de forma segura en la secure element de la Coldcard utilizando una memoria flash OTP (programable una sola vez), lo que significa que no puede modificarse una vez programado. Al encender el dispositivo por primera vez, el número que aparece en la pantalla debe coincidir con el de la bolsa. Esto garantiza que el Mk4 que ha recibido es el dispositivo original de fábrica y no ha sido sustituido ni modificado. Aunque esta verificación sólo confirma la integridad del dispositivo en el momento del primer encendido, la secure element sigue protegiendo sus claves privadas, PIN y passphrase, haciendo extremadamente difícil que cualquier manipulación pueda comprometer su Bitcoin. Además, las buenas prácticas, como asegurar adecuadamente sus datos relacionados con wallet, serán beneficiosas para la seguridad general de la propia tarjeta Cold. Para más información, puedes consultar este [artículo](https://blog.coinkite.com/understanding-mk4-security-model/) que explica con detalle el modelo de seguridad de la Coldcard.


El teclado consta de 10 botones numéricos, un botón OK (`✓`) y un botón de cancelación (`✕`). Algunos botones numéricos también se pueden utilizar para navegar: `5` para navegar hacia arriba (`^`), `7` para navegar hacia la izquierda (`<`), `8` para navegar hacia abajo `˅`, y `9` para navegar hacia la derecha (`>`).


![01](assets/en/01.webp)


Si no hay problemas con el embalaje, puede abrir la bolsa. El Mk4 vendrá con una tarjeta de copia de seguridad wallet que se puede utilizar para almacenar información sobre el PIN del dispositivo, palabras antiphishing, y seedphrase. Siga los siguientes pasos para la inicialización:


1. Prepara un papel y un bolígrafo.

2. Conecta el Mk4 a una fuente de alimentación (cable USB-C) e inserta la tarjeta MicroSD.

3. Una vez encendido el dispositivo por primera vez, la pantalla mostrará un mensaje relativo a las Condiciones de venta y uso de Coldcard. Navegue hacia abajo y pulse `✓` para continuar.

4. A continuación, aparecerá un número de 12 dígitos en la pantalla. Compruebe este número con el de la bolsa a prueba de manipulaciones y con la copia adicional del número de la bolsa que se incluyó en la bolsa a prueba de manipulaciones para asegurarse de que el dispositivo no ha sido manipulado. Si los números no coinciden, póngase en contacto con el servicio de asistencia de Coinkite inmediatamente antes de continuar. De lo contrario, pulse `✓` para continuar.


![02](assets/en/02.webp)


5. Seleccione "Elegir código PIN".

6. Navegue hacia abajo mientras lee las instrucciones para pasar al siguiente paso.


![03](assets/en/03.webp)


7. En el Mk4, crea e introduce el prefijo PIN (debe tener entre 2 y 6 caracteres) y anótalo, después pulsa `✓` para continuar.

8. Escriba las dos palabras que aparecen en la pantalla. Estas son las palabras antiphishing. Pulse `✓` para continuar.


![04](assets/en/04.webp)


9. Cree e introduzca el sufijo del PIN (o el resto del PIN, debe tener entre 2 y 6 caracteres) y anótelo. Pulse `✓` para continuar.

10. Vuelva a introducir el prefijo PIN. Pulsa `✓` para continuar.


![05](assets/en/05.webp)


11. Compruebe si las palabras antiphishing coinciden con las que escribió en el paso 8. Pulse `✓` para continuar.

12. Vuelva a introducir el sufijo PIN (o el resto del PIN). Pulsa `✓` para continuar.


![06](assets/en/06.webp)


13. El PIN y las palabras antiphishing de tu Mk4 ya se han creado y almacenado correctamente en el dispositivo.


![07](assets/en/07.webp)


Tenga en cuenta que Mk4 siempre le pedirá que introduzca su PIN cada vez que encienda el dispositivo. Sin este PIN, no podrás acceder a tu Coldcard Mk4. Así que asegúrese de crear una copia de seguridad suficiente para el PIN y las palabras anti-phishing.


## Configuración de su Wallet


El siguiente paso es configurar tu wallet. Hay tres maneras de hacerlo:


- Creación de un nuevo wallet (estándar)
- Creación de un nuevo wallet con tiradas de dados
- Importar una wallet


### Creación de una nueva wallet (estándar)


Para crear un nuevo wallet, basta con seguir estos pasos.


1. Seleccione `New Wallet` (o `New Seed Words`) > Seleccione `12 Word` o `24 Word (por defecto)` según sus preferencias.


![08](assets/en/08.webp)


2. El dispositivo generará 12 o 24 palabras como su seedphrase en función de su elección. Navegue hacia abajo mientras escribe cuidadosamente cada palabra en el orden correcto. A continuación, pulsa `✓` para continuar.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. El dispositivo le pedirá que verifique su seedphrase preguntando en un orden aleatorio (por ejemplo, "La palabra 1 es...", "La palabra 5 es...", "La palabra 12 es...", etc.) y habrá tres opciones de palabra para cada pregunta. Consulte la nota del paso 2 y elija las palabras correctamente (pulsando `1`, `2` o `3`, la que corresponda a la palabra correcta) para completar la creación de wallet.


![09](assets/en/09.webp)


4. El Mk4 le preguntará si desea activar NFC/Tap o no. Por ahora, selecciona `✕` para esta opción. Esto se puede cambiar en la configuración en el futuro.

5. Por último, Mk4 también si desea desactivar el puerto USB (que puede ser utilizado para la transferencia de datos no airgapped). Por ahora, selecciona `✓` para esta opción. Esto se puede cambiar en la configuración en el futuro.

6. La pantalla mostrará ahora el menú principal con "Listo para firmar" en la parte superior. De este modo finaliza el proceso de creación de wallet.


![10](assets/en/10.webp)


### Creación de un nuevo wallet con tirada de dados


Alternativamente, también puedes optar por generar el nuevo seedphrase con entropía. Hazlo si no confías en el seedphrase recién generado de Mk4.


El procedimiento en la Coldcard Mk4 es el siguiente:


1. Seleccione `Nuevo Wallet` (o `Nuevas palabras semilla`) > Seleccione `Rollo de dados de 12 palabras` o `Rollo de dados de 24 palabras` según prefiera.

2. Se le pedirá que introduzca los resultados de sus tiradas de dados. Cada tirada de dados añade aleatoriedad al proceso de creación del wallet, garantizando que su seedphrase se genere de forma totalmente segura e impredecible. El número mínimo de tiradas es 50 para seedphrase de 12 palabras y 99 para seedphrase de 24 palabras. Pulsa `✓` después de haber introducido al menos 99 valores de tirada de dados.


![11](assets/en/11.webp)


3. El dispositivo generará 12 o 24 palabras como su seedphrase en función de su elección. Navegue hacia abajo mientras escribe cuidadosamente cada palabra en el orden correcto. A continuación, pulsa `✓` para continuar.

4. El dispositivo le pedirá que verifique su seedphrase preguntando en un orden aleatorio (por ejemplo, "La palabra 1 es...", "La palabra 5 es...", "La palabra 12 es...", etc.) y habrá tres opciones de palabra para cada pregunta. Consulte la nota del paso 3 y elija las palabras correctamente (pulsando `1`, `2` o `3`, la que corresponda a la palabra correcta) para completar la creación de la wallet.


![12](assets/en/12.webp)


5. El Mk4 le preguntará si desea activar NFC/Tap o no. Por ahora, selecciona `✕` para esta opción. Esto se puede cambiar en la configuración en el futuro.

6. Por último, Mk4 también si desea desactivar el puerto USB (que puede ser utilizado para la transferencia de datos no airgapped). Por ahora, selecciona `✓` para esta opción. Esto se puede cambiar en la configuración en el futuro.

7. La pantalla mostrará ahora el menú principal con "Listo para firmar" en la parte superior. De este modo finaliza el proceso de creación de wallet.


![13](assets/en/13.webp)


### Importar una wallet


La última opción es importar una wallet. Puede hacerlo si desea recuperar una wallet a partir de una seedphrase que ya tenga. Puede seguir estos pasos:


1. Seleccione `Importar existentes`.

2. Seleccione "24 palabras", "18 palabras" o "12 palabras", en función del número de palabras de su seedphrase.


![14](assets/en/14.webp)


3. La Coldcard Mk4 le preguntará entonces cuál es cada palabra en orden consecutivo. Para cada palabra, navegue hacia abajo o hacia arriba hasta encontrar el prefijo de escritura de cada palabra. El dispositivo reducirá las posibilidades hasta que encuentres la palabra correcta. Haga lo mismo para el resto de las palabras.

4. Para la palabra final, Coldcard Mk4 mostrará sólo una cantidad limitada de palabras posibles. Si no hay coincidencias, es posible que haya introducido las palabras incorrectamente. En caso contrario, seleccione la palabra que coincida con la de su seedphrase.


![15](assets/en/15.webp)


5. El Mk4 le preguntará si desea activar NFC/Tap o no. Por ahora, selecciona `✕` para esta opción. Esto se puede cambiar en la configuración en el futuro.

6. Por último, Mk4 también si desea desactivar el puerto USB (que puede ser utilizado para la transferencia de datos no airgapped). Por ahora, selecciona `✓` para esta opción. Esto se puede cambiar en la configuración en el futuro.

7. La pantalla mostrará ahora el menú principal con "Listo para firmar" en la parte superior. Esto marca la finalización del proceso de creación de la wallet.


![16](assets/en/16.webp)


Tenga en cuenta que la seedphrase es el único acceso para recuperar su wallet. Crea una copia de seguridad de tu seedphrase y guárdala en un lugar seguro. **Ni tus llaves, ni tus monedas**, ¡quien tenga tu seedphrase tiene acceso a tus bitcoins!


## Configuración de su passphrase


Una de las mejores prácticas en Bitcoin es utilizar una passphrase. La passphrase actúa como la 13ª o 25ª palabra además de la seedphrase. Lo que la hace diferente es que puedes elegir la frase que quieras, mientras que la seedphrase se selecciona de una lista predeterminada de 2048 palabras. Por defecto, después de configurar su wallet, empezará con una wallet con una passphrase en blanco. Para configurar una passphrase que no esté en blanco, simplemente siga los siguientes pasos:


1. Vaya a "Frase de contraseña".

2. Navega hacia abajo para leer la descripción de passphrase y pulsa `✓` para continuar.

3. Seleccione `Editar frase`.


![17](assets/en/17.webp)


4. Introduce tu passphrase:


   - Pulse `1` (letras), `2` (números) o `3` (símbolos) para seleccionar el tipo de carácter.
   - Pulse `4` para alternar entre minúsculas y mayúsculas (sólo se puede utilizar al introducir letras).
   - Navega con `^` o `˅` para seleccionar el personaje de tu passphrase.
   - Navega utilizando `<` o `>` para moverte entre caracteres. También puede utilizar `>` para añadir espacios.
   - Pulse `✕` para borrar los caracteres.
   - Pulse `✓` cuando haya terminado de editar la passphrase.

5. Además, las otras opciones tienen las siguientes funcionalidades:


   - Las opciones "Añadir Palabra" o "Añadir Números" se pueden utilizar para añadir letras/números a la passphrase que esté editando en ese momento.
   - Pulse `Borrar TODO` para reiniciar la passphrase que está editando en ese momento.
   - Pulse `CANCEL` para volver al menú principal.

6. Anota tu passphrase como copia de seguridad.

7. Pulse `APPLY` para acceder al wallet con el passphrase que acaba de configurar.

8. Mk4 mostrará entonces una huella digital de la llave maestra de 8 caracteres de longitud. Esto puede considerarse como el "ID" del wallet. Anote esta huella y pulse `✓` para continuar.


![18](assets/en/18.webp)


9. Ahora, el wallet mostrará el menú principal del wallet con el passphrase que ha introducido.

10. Es importante tener en cuenta que una wallet no le indicará que ha introducido la passphrase incorrecta, ya que cada passphrase corresponde a su propia wallet con una identidad única (huella dactilar de la clave maestra). Por lo tanto, es una buena práctica volver a introducir el mismo passphrase y comprobar si produce la misma huella dactilar de wallet, asegurándose de que lo ha introducido correctamente. Para ello, realice los pasos 11 a 14.

11. En el menú principal, seleccione "Restaurar maestro" y pulse "✓". Ahora está de vuelta en el menú principal del wallet con el passphrase en blanco.


![19](assets/en/19.webp)


12. Vaya de nuevo a "Frase de contraseña" y pulse "✓" para continuar.

13. Vuelva a introducir el passphrase que anotó en el paso 6 y pulse "APLICAR".

14. Compruebe la huella de la llave maestra de 8 caracteres de longitud con la que ha escrito en el paso 8. Si ambas huellas no coinciden, es posible que haya escrito caracteres erróneos. Puede seleccionar un nuevo passphrase en su lugar y repetir el proceso desde el Paso 1. Si ambas huellas coinciden, significa que ha introducido el passphrase correctamente.

15. El wallet con su passphrase elegido está listo para ser utilizado.


## Exportación del Wallet al Sparrow


Al igual que otras wallet de hardware, la Coldcard Mk4 no puede utilizarse por sí sola. Necesita estar conectada con un software wallet que actúe como interfaz. El software wallet le permite ver su saldo, crear transacciones y gestionar direcciones, mientras que la Coldcard firma de forma segura esas transacciones sin exponer nunca sus claves privadas.


En este tutorial, utilizaremos Sparrow Wallet como interfaz. El procedimiento para exportar la wallet es el siguiente:


1. Asegúrate de que tienes una tarjeta MicroSD insertada en el Mk4.

2. Realice los pasos de "Configuración de su passphrase" en la wallet con la passphrase que desea exportar. Si desea exportar la wallet con la passphrase en blanco, puede omitir este paso.

3. Vaya a `Avanzado/Herramientas` > Elija `Exportar Wallet` > Seleccione `Generic JSON` > Desplácese hacia abajo mientras lee las instrucciones y pulse `✓`.


![20](assets/en/20.webp)


4. Ahora Mk4 ha creado un archivo con formato `.json` en la tarjeta MicroSD.


![21](assets/en/21.webp)


5. Extraiga la tarjeta MicroSD de la Coldcard e insértela en el dispositivo donde está instalada la Sparrow Wallet.

6. Abra Sparrow Wallet.

7. Haga clic en `Archivo`


![22](assets/en/22.webp)


A continuación, haga clic en `Nueva Wallet`


![23](assets/en/23.webp)


A continuación, introduzca el nombre de la wallet


![24](assets/en/24.webp)


A continuación, haga clic en "Crear Wallet"


![25](assets/en/25.webp)


8. Seleccione el `tipo de script`.


![26](assets/en/26.webp)


9. En la sección Keystore, seleccione `Airgapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Busque Coldcard y haga clic en `Importar archivo...`.


![28](assets/en/28.webp)


11. Seleccione el archivo creado en el paso 4 (el que tiene el formato `.json`).


![29](assets/en/29.webp)


12. En el Mk4, vuelva al menú principal y vaya a `Advanced/Tools` > `View Identity`. Asegúrese de que la huella dactilar que aparece en la pantalla del Mk4 coincide con la de Sparrow Wallet (la huella dactilar maestra de la sección Almacén de claves)

13. Pulse el botón `Aplicar` en la esquina inferior derecha.


![30](assets/en/30.webp)


14. Opcionalmente, también puede añadir una contraseña para la wallet exportada. Esta contraseña será necesaria cada vez que abra la aplicación Sparrow Wallet para acceder a la wallet. Si olvida la contraseña en el futuro, sólo tiene que repetir los pasos 1-13 y elegir una nueva contraseña.


![31](assets/en/31.webp)


15. La wallet ya se ha exportado correctamente y está lista para su uso.


![32](assets/en/32.webp)


## Recibir bitcoin


A continuación, aprenderemos a recibir Bitcoin utilizando el Mk4. Este proceso es bastante sencillo porque no necesitas utilizar el dispositivo Mk4 en sí. Siempre y cuando ya hayas exportado tu wallet a Sparrow, puedes recibir Bitcoin directamente a través de Sparrow Wallet. Sigue estos pasos para recibir bitcoins con Mk4:


1. Abra Sparrow Wallet.

2. Seleccione `Abrir Wallet` > Elija el archivo wallet al que desea recibir bitcoin > Introduzca la contraseña asociada a esa wallet.


![33](assets/en/33.webp)


3. En la interfaz de Sparrow, haga clic en la pestaña "Recepción" de la parte izquierda de la interfaz.


![34](assets/en/34.webp)


4. En la parte superior aparecerá una dirección junto con un código QR. Puedes copiar y pegar la dirección o escanear el código QR con la wallet que utilizarás para enviar bitcoin a la Sparrow Wallet. Opcionalmente, puedes escribir una etiqueta para el bitcoin que recibas.


![35](assets/en/35.webp)


5. Después de enviar los bitcoins, en la interfaz de Sparrow, haz clic en la pestaña `Transacciones` de la parte izquierda de la interfaz. Verás una nueva entrada en la parte superior del historial de transacciones, que corresponde a la transacción que acabas de realizar.


![36](assets/en/36.webp)


6. También puedes navegar por la pestaña `UTXOs` de la parte izquierda de la interfaz para ver el bitcoin que acabas de recibir.


![37](assets/en/37.webp)


## Enviar bitcoin


A diferencia de la recepción de bitcoins, el gasto de los bitcoins asociados a su Coldcard requiere que utilice la Coldcard para firmar las transacciones. El procedimiento de envío de bitcoins con Mk4 es el siguiente:


1. Inserte la tarjeta MicroSD en el dispositivo donde está instalado su Sparrow Wallet.

2. Abra Sparrow Wallet.

3. Selecciona `Abrir Wallet` > Elige el archivo wallet con el que quieres enviar bitcoins > Introduce la contraseña asociada a ese wallet.


![38](assets/en/38.webp)


4. En la interfaz de Sparrow, haga clic en la pestaña `Enviar` de la parte izquierda de la interfaz.


![39](assets/en/39.webp)


5. En la pestaña "Pagar a", introduzca la dirección a la que desea enviar los bitcoins.

6. Añade una etiqueta para la transacción.

7. Introduzca la cantidad de bitcoins que desea enviar.

8. Introduzca la tarifa activando el "Rango" o introduzca directamente un número en la parte "Tarifa".


![40](assets/en/40.webp)


9. En la esquina inferior derecha, haga clic en `Crear transacción`.


![41](assets/en/41.webp)


10. Aparecerá una nueva pestaña de transacción cuyo nombre es la etiqueta que introdujo en el Paso 6. Haga clic en `Finalizar transacción para firmar`.


![42](assets/en/42.webp)


11. Haga clic en `Guardar transacción` y guarde la transacción en la tarjeta MicroSD. Cambie el nombre del archivo si es necesario. Este paso guardará la transacción como un archivo PSBT.


![43](assets/en/43.webp)


12. Extrae la tarjeta MicroSD e insértala en tu Coldcard Mk4.

13. Enciende tu Mk4 conectándolo a una fuente de alimentación.

14. Introduzca su PIN.

15. Ve a `Passphrase` e introduce el passphrase del wallet que quieres usar para enviar los bitcoins. Si quieres usar la wallet con la passphrase en blanco, omite este paso.

16. Asegúrese de que la huella digital de la llave maestra es la misma que la de su Sparrow Wallet. Puedes comprobarlo en la pestaña "Configuración" de Sparrow Wallet, en la parte izquierda de la interfaz. A continuación, pulsa `✓` en tu Mk4 para continuar. Esto te llevará al menú principal.

17. En el menú principal del Mk4, seleccione "Listo para firmar". En la pantalla aparecerá el mensaje "Listo para enviar". Asegúrate de que la cantidad de bitcoins que quieres enviar y la dirección de recepción son correctas. Pulsa `✓` para confirmar o `✕` para cancelar.

18. Si hay varios archivos PSBT entre los que elegir, Mk4 mostrará el mensaje "Elegir archivo PSBT para firmar". Pulsa `✓` para continuar. A continuación, seleccione el archivo PSBT que desea firmar navegando hacia abajo o hacia arriba. Realice el paso 17 en esa transacción.


![44](assets/en/44.webp)


19. Mk4 mostrará ahora el mensaje `PSBT Signed` junto con el nombre del archivo del PSBT firmado. Pulsa `✓` para continuar.

20. Extraiga la tarjeta MicroSD de la Coldcard e insértela en el dispositivo donde está instalada la Sparrow Wallet.

21. En Sparrow Wallet, haga clic en `Cargar transacción`.


![45](assets/en/45.webp)


22. Seleccione el fichero con el mismo nombre que el creado en el paso 19.


![46](assets/en/46.webp)


23. Haga clic en "Transmitir transacción".


![47](assets/en/47.webp)


24. Su transacción ha sido emitida y está siendo procesada. Puede ir a la pestaña `Transacciones` para ver el estado de confirmación de su transacción.


![48](assets/en/48.webp)


## Actualización del firmware


### Comprobación de la versión del firmware


El firmware de Coldcard Mk4 siempre puede actualizarse a una versión más reciente. Para comprobar si tu Mk4 ha sido actualizado a la última versión o no, realiza los siguientes pasos:

1. Enciende tu Mk4 conectándolo a una fuente de alimentación.

2. Introduzca su PIN.

3. Vaya a `Avanzado/Herramientas` > Seleccione `Actualizar Firmware` > Seleccione `Mostrar Versión`.


![49](assets/en/49.webp)


Comprueba la versión que aparece en la pantalla del Mk4 con la que aparece en [Coinkite's website](https://coldcard.com/downloads). Si la versión es diferente, usted es capaz de actualizar el firmware a la versión más reciente.


![50](assets/en/50.webp)


### Actualización del firmware


Si desea actualizar el firmware a la última versión, siga estos pasos:


1. Inserta la tarjeta MicroSD en tu portátil/PC.

2. Ve a [Coinkite's website](https://coldcard.com/downloads) y descarga el último firmware a tu tarjeta MicroSD (El botón rojo a la derecha de la imagen Mk4 con el número de versión en él).


![51](assets/en/51.webp)


También puede descargar otras versiones haciendo clic en `All Files on Mk4` y explorando la versión que desee descargar. El archivo descargado estará en formato `.dfu`.


![52](assets/en/52.webp)


3. Extrae la tarjeta MicroSD e insértala en tu Mk4.

4. Enciende tu Mk4 conectándolo a una fuente de alimentación.

5. Introduzca su PIN.

6. Ve a `Avanzado/Herramientas` > Selecciona `Actualizar Firmware` > Selecciona `Desde MicroSD` > Desplázate hacia abajo mientras lees las instrucciones y luego pulsa `✓`.


![53](assets/en/53.webp)


7. Seleccione el archivo `.dfu` que descargó en el paso 2.

8. Coldcard Mk4 mostrará el mensaje "Instalar este nuevo firmware". Desplázate hacia abajo mientras lees las instrucciones y pulsa `✓`.


![54](assets/en/54.webp)


9. Espera a que el Mk4 termine de instalar el nuevo firmware. No desconecte la fuente de alimentación durante la instalación.

10. Una vez completado, el Mk4 se reiniciará. Puede introducir su PIN y realizar los pasos de "Comprobación de la versión del firmware" para comprobar si el firmware se ha actualizado o no.


## Funciones avanzadas


### Cambiar el PIN


Si desea cambiar su PIN de acceso, sólo tiene que realizar los siguientes pasos:


1. Prepara un bolígrafo y un trozo de papel.

2. Enciende tu Mk4 conectándolo a una fuente de alimentación.

3. Introduzca su PIN.

4. Vaya a `Configuración` > Seleccione `Configuración de inicio de sesión` > Seleccione `Cambiar PIN principal`

5. Navega hacia abajo mientras lees el mensaje y pulsa `✓` para continuar.


![55](assets/en/55.webp)


6. Introduce tu antiguo PIN.

7. Introduzca su nuevo prefijo PIN (debe tener entre 2 y 6 caracteres) y anótelo.

8. Mk4 mostrará ahora dos nuevas palabras antiphishing, escríbelas y pulsa `✓` para continuar.

9. Introduzca su nuevo sufijo PIN (o el resto del PIN, debe tener entre 2 y 6 caracteres) y anótelo.


![56](assets/en/56.webp)


10. Vuelva a introducir su nuevo prefijo PIN.

11. Compruebe si las palabras antiphishing coinciden con las que escribió en el paso 8.

12. Vuelva a introducir su nuevo sufijo PIN (o el resto del PIN).


![57](assets/en/57.webp)


13. Su PIN ha sido modificado correctamente.


### Truco PIN - Añadir nuevo truco


Un PIN de truco es un código PIN alternativo distinto del que utilizas para configurar tu Coldcard Mk4 por primera vez. Cuando enciendas tu Mk4, podrás introducir el PIN de trucos en lugar de tu PIN principal para activar determinadas acciones. Para configurar el PIN de trucos en Mk4, puedes seguir los siguientes pasos:


1. Prepara un bolígrafo y un trozo de papel.

2. Enciende tu Mk4 conectándolo a una fuente de alimentación.

3. Introduzca su PIN.

4. Ve a `Configuración` > Selecciona `Configuración de inicio de sesión` > Selecciona `PIN de trucos` > Selecciona `Añadir nuevo truco`.


![58](assets/en/58.webp)


5. Introduzca su prefijo PIN trucado (debe tener entre 2 y 6 caracteres) y anótelo.

6. Mk4 mostrará ahora dos nuevas palabras antiphishing, escríbelas y pulsa `✓` para continuar.

7. Introduzca el sufijo de su PIN trucado (o el resto del PIN, debe tener entre 2 y 6 caracteres) y anótelo.


![59](assets/en/59.webp)


8. Desplácese hacia abajo o hacia arriba para seleccionar la acción que desea emparejar con el PIN de truco que acaba de crear. La lista de acciones son:


    - `Brick Self`, cuando se selecciona, los chips de tu Mk4 se destruirán después de introducir el PIN, haciendo que tu Mk4 quede inutilizable permanentemente.
    - `Wipe Seed`, puede elegir entre las siguientes acciones:
      - borrar y reiniciar": El seed se limpia y Coldcard se reiniciará después de introducir el PIN.
      - `Borrado silencioso`: El seed se borra en silencio, sin embargo Coldcard actuará como si el PIN se ha introducido incorrectamente.
      - `Wipe -> Wallet`: La seed se borra silenciosamente, y la Coldcard te llevará a una wallet de coacción.
    - `Duress Wallet`, cuando se selecciona, su Mk4 conducirá a un wallet de coacción después de introducir el PIN.
    - cuenta atrás de inicio de sesión", puede elegir entre las siguientes acciones:
      - `Borrar y Cuenta Atrás`: La seed se limpia inmediatamente y el Mk4 comienza a mostrar una cuenta atrás.
      - cuenta atrás y ladrillo: Comienza la cuenta atrás y el Mk4 se bloqueará a sí mismo cuando acabe el tiempo.
      - `Just Countdown`: El Mk4 iniciará la cuenta atrás y se reiniciará cuando acabe el tiempo.
    - cuando se selecciona esta opción, después de introducir el PIN trucado, la Coldcard actúa como si la seedphrase se hubiera borrado, pero en realidad sigue en la memoria.
    - si se selecciona esta opción, la Coldcard se reiniciará automáticamente una vez introducido el PIN.
    - esta función avanzada está pensada para usuarios experimentados y está diseñada para proteger frente a amenazas graves, como la coacción por parte de alguien con información privilegiada. Cuando se activa el Modo Delta, la COLDCARD parece abrir la wallet real, lo que permite al atacante navegar y confirmar que parece auténtica. Sin embargo, bloquea en secreto la firma de todas las transacciones, por lo que no se puede enviar ningún bitcoin. También desactiva el acceso a la frase seed, y cualquier intento de verla la borrará por completo. Para que la falsa wallet parezca más convincente, el Trick PIN utilizado para el Modo Delta debe empezar con los mismos números que el PIN real (para que muestre las mismas palabras antiphishing) pero terminar de forma diferente.
    - `Desbloqueo de la política`, cuando se selecciona, la Política de Gasto de Firmante Único (SSSP) se desactivará después de introducir el PIN de truco.
    - policy Unlock & Wipe", cuando se selecciona, pretende desactivar SSSP pero borrará la seedphrase en el proceso.

9. Una vez seleccionada la acción que desea asociar al PIN trucado, confirme su elección pulsando `✓`. El PIN trucado se ha configurado correctamente.

10. En `Configuración` > `Configuración de inicio de sesión` > `PIN trucado`, puedes ver la lista de PIN trucados que has creado y las acciones asociadas a ellos. Puedes elegir reconfigurar los PINs trucados y las acciones asociadas a ellos. También puede ocultarlo o eliminarlo seleccionando el PIN y luego `Ocultar truco` o `Eliminar truco`.


![60](assets/en/60.webp)


### Truco PIN - Añadir si es incorrecto


Alternativamente, puede añadir una acción `Añadir si es incorrecto` que se activará después de introducir el PIN incorrecto un cierto número de veces. Para configurarlo, siga estos pasos:


1. Enciende tu Mk4 conectándolo a una fuente de alimentación.

2. Introduzca su PIN.

3. Ve a `Configuración` > Selecciona `Configuración de inicio de sesión` > Selecciona `PINs trucados` > Selecciona `Añadir si es incorrecto`.


![61](assets/en/61.webp)


4. Mk4 mostrará un mensaje relativo a este ajuste. Navega hacia abajo mientras lees la explicación y pulsa `✓` para continuar.

5. Introduzca el número de intentos erróneos necesarios para activar la acción. Nota: El número máximo de intentos es "12". Esto se debe a que Mk4 está diseñado de tal manera que cuando se introduce el PIN incorrecto `13` veces, el dispositivo se bloqueará, haciéndolo inutilizable de forma permanente. Después de introducir el número, pulse `✓` para continuar.

6. Navegue hacia arriba o hacia abajo para seleccionar la acción. Las acciones disponibles son las siguientes:


   - `Borrar, Parar`: La seedphrase se borra y el dispositivo muestra "Seed is wiped, Stop"
   - `Borrar y Reiniciar`: La seedphrase se borra y el dispositivo se reinicia sin ningún mensaje.
   - borrado silencioso: La seedphrase se borra silenciosamente y el dispositivo se comporta como un intento de PIN erróneo (sin mensaje de borrado obvio).
   - `Brick Self`: El dispositivo se desactiva permanentemente y sólo muestra "Bricked"
   - última oportunidad: La seedphrase se borra pero tienes un último intento de introducir el PIN; introduce el PIN incorrecto de nuevo y el dispositivo se bloqueará.
   - simplemente reiniciar": El dispositivo simplemente se reinicia y nada más cambia.

Elija la acción que desea aplicar y pulse `✓` para continuar


![62](assets/en/62.webp)


7. Volverá al directorio `Configuración >Configuración de inicio de sesión > PIN trucado`. En "PINs Trucos" encontrarás la lista de PINs Trucos junto con la acción "PIN ERROR". También puedes ocultarlo o borrarlo seleccionando el PIN y luego `Ocultar Truco` o `Borrar Truco`.


![63](assets/en/63.webp)



## Conclusión


Este tutorial ha proporcionado la guía sobre cómo configurar Mk4, cómo realizar transacciones Bitcoin con Mk4 y cómo utilizar algunas funciones avanzadas de Mk4. Ofrece formas seguras y flexibles de almacenar y gestionar tus bitcoins. Su diseño garantiza que las claves privadas nunca salgan del dispositivo, mientras que funciones como los passphrase, los PIN trucados y las transacciones con air-gap ofrecen a los usuarios un control total sobre su configuración de seguridad. Se puede emparejar con Sparrow Wallet para una experiencia fácil de usar para crear, firmar y gestionar transacciones Bitcoin sin comprometer la privacidad o la seguridad.


Si desea explorar otras funcionalidades, puede consultar la documentación en la página web de Coinkite [aquí](https://coldcard.com/docs/). Espero que encuentres este tutorial beneficioso cuando utilices tu Coldcard Mk4. ¡Gracias y hasta la próxima!
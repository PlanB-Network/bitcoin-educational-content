---
name: Green Wallet

description: Guía de configuración y uso (CC Bistack)
---

![cover](assets/cover.jpeg)

# Tutorial de la billetera - Green Wallet

Billetera móvil caliente - Principiante - Gratis - Para asegurar de 0 a 1,000 €

Para asegurar cantidades por debajo de 1,000 €, una billetera caliente (conectada a Internet) gratuita es perfecta para comenzar. Su configuración es fácil y su interfaz está diseñada para principiantes.

Si deseas visitar su sitio, haz clic aquí (https://blockstream.com/green/)!

## Tutorial en video

![tutorial en video de Green Wallet](https://www.youtube.com/watch?v=lONbCS31am4)

## Tutorial escrito

> Esta guía fue producida y pertenece a Bitstack. Bitstack es un banco de bitcoins neo con sede en París que permite DCA en bitcoin. Guía escrita por Loic Morel el 15/02/2023. Esto les pertenece. https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet

![imagen](assets/0.png)

¿Cómo instalar tu primera billetera de Bitcoin? Tutorial de Green Wallet

Si deseas aprovechar los numerosos beneficios del sistema Bitcoin, incluida la censurabilidad y la incautabilidad de tus fondos, debes conservar tus propias claves que dan acceso a tus bitcoins.

En este tutorial, te explicaré cómo configurar tu primera billetera con Green Wallet. Este software es especialmente adecuado para usuarios principiantes. Es muy fácil de usar, incluso si no tienes conocimientos avanzados sobre Bitcoin.

Green Wallet está disponible en todo tipo de dispositivos. En este tutorial, veremos cómo usarlo en un dispositivo móvil, pero también puedes descargarlo en una computadora.

El primer paso es, obviamente, descargar el software o la aplicación Green Wallet. Si estás en un dispositivo móvil, simplemente puedes descargarlo desde tu tienda. Asegúrate de estar en la página de descarga de la aplicación oficial. Aquí están las páginas según tu sistema:

> - Google Play Store
>
> - Apple App Store

Si descargas el software en una computadora, te recomiendo encarecidamente que verifiques la autenticidad e integridad del binario antes de instalarlo en tu máquina. Te explicaré cómo realizar esta operación en un próximo tutorial.

## Elección de los ajustes de la aplicación

Al iniciar la aplicación, llegarás a la pantalla de inicio. Por ahora, no tienes ninguna billetera. Más adelante, si has creado varias billeteras, podrás encontrarlas aquí.

La primera acción que debes realizar antes de crear tu billetera es abrir los ajustes de la aplicación para elegir los que mejor se adapten a ti.

![imagen](assets/1.png)

- "Enhanced Privacy" te permite desactivar la posibilidad de tomar capturas de pantalla en la aplicación. Esta opción también ocultará las vistas previas y asegurará automáticamente la aplicación cuando bloquees tu teléfono. Solo está disponible en Android;
- Luego puedes elegir enrutar tu tráfico a través de Tor para que todas tus conexiones estén cifradas. Esto ralentiza ligeramente el funcionamiento de tu aplicación, pero te recomiendo que lo actives para preservar tu privacidad;

- La opción "Testnet" te permite crear billeteras en Testnet. Es una red que funciona exactamente como el sistema Bitcoin, excepto que los bitcoins intercambiados en ella no tienen ningún valor real. Esta red de prueba separada es utilizada por usuarios o desarrolladores que desean probar aplicaciones sin asumir riesgos financieros. Si deseas utilizar Green Wallet en el sistema Bitcoin real, puedes dejar esta opción desactivada;

- La opción "Ayudar a Green" te permite enviar información confidencial a Blockstream para que mejoren su aplicación;

- La opción "Servidor Electrum personal" te permite conectar tu propio nodo Bitcoin de forma remota para acceder a la información de la red y transmitir tus transacciones;

- La opción "Verificación SPV" te permite descargar y verificar cierta información de la Blockchain por ti mismo. Esto reduce la necesidad de confiar en el nodo de Blockstream. Ten en cuenta que esta opción no te brinda todas las garantías de un verdadero nodo Bitcoin, pero si no tienes uno, puede ser una buena opción para activar.

Una vez que hayas seleccionado tus configuraciones, puedes hacer clic en el botón "Guardar" y luego reiniciar tu aplicación.

## Creación de una billetera Bitcoin

El siguiente paso es crear tu billetera Bitcoin. Para hacerlo, haz clic en:

> - Agregar una billetera;
> - Nueva billetera;
> - Bitcoin.

![image](assets/3.png)

La opción "Restaurar una billetera" te permite recuperar el acceso a una billetera existente utilizando su frase mnemotécnica. La opción "Billetera de solo lectura" te permite importar una clave pública extendida (xpub) para ver los movimientos de una billetera sin poder gastar sus fondos.

> "La billetera de solo lectura es especialmente útil si tienes una billetera de hardware. Puedes importar la xpub en tu teléfono para crear direcciones de recepción y seguir el saldo de la billetera alojada en la billetera de hardware."
> Las opciones de red le permiten conectar su billetera a diferentes sistemas. La red "Liquid" es una sidechain de Bitcoin. La red "Testnet" es una copia de la red Bitcoin, pero con bitcoins que no tienen ningún valor. Por último, la red "Testnet Liquid" es el equivalente de Testnet para la sidechain Liquid. En este tutorial, simplemente queremos hacer una billetera de Bitcoin, por lo que seleccionamos la red "Bitcoin".
> Luego, se le pregunta qué tipo de billetera desea crear. Lo más sencillo es hacer una billetera "Single Sig". En este caso, cada UTXO (fragmento de bitcoin) que nos pertenezca estará bloqueado solo por un par de claves.

Seleccione "Firma única".

Luego puede elegir tener una frase mnemotécnica de 12 palabras o de 24 palabras. Esta frase le permitirá recuperar el acceso a su billetera desde cualquier software compatible en caso de pérdida, robo o daño de su teléfono.

Una frase de 24 palabras es más segura que una frase de 12 palabras frente a ataques de fuerza bruta. Sin embargo, hasta la fecha, una frase de 12 palabras sigue siendo lo suficientemente segura. Concretamente, si elige una frase de 12 palabras, estará justo por encima del límite mínimo recomendado por el NIST. Esto significa que su frase está segura hoy, pero puede que no lo esté en el futuro debido a la evolución de la informática (a menos que también utilice una frase de contraseña BIP39). Por defecto, le recomiendo que elija una frase de 24 palabras, pero es su elección personal.

![image](assets/6.png)

Luego, el software le proporcionará su frase de recuperación. Debe guardarla adecuadamente anotándola en un soporte físico adecuado. Se desaconseja encarecidamente guardar esta frase en cualquier soporte digital, incluso cifrado. Debe anotarla en papel o en metal según el valor almacenado.

Esta frase es de vital importancia, ya que permite acceder a las claves de su billetera sin ninguna restricción. Si la pierde, no podrá acceder a sus bitcoins si su teléfono deja de funcionar. Si alguien roba esta frase mnemotécnica, podrá robar irrevocablemente todos sus fondos.

Las palabras de esta frase deben ser anotadas juntas. ¡No divida su frase! Además, también es esencial anotar cada palabra en el orden establecido, con su número. Una frase desordenada no sirve de nada.

Para obtener más información sobre los métodos de seguridad de la frase de recuperación, le recomiendo que lea mi artículo dedicado a este tema.

![image](assets/7.png)

Green Wallet luego le pide que confirme algunas palabras de su frase para asegurarse de que las haya anotado correctamente.
'![image](assets/10.png)

A continuación, puedes elegir un nombre para tu billetera para diferenciarla de otras si en el futuro creas varias. En esta etapa, el nombre no es importante ya que eliminaremos esta billetera para verificar la validez de la frase mnemotécnica en el siguiente paso.

También se te pedirá que establezcas un PIN. Esto bloqueará el acceso a tu billetera. Es recomendable establecer una contraseña compleja y aleatoria, especialmente para proteger tu billetera en caso de robo de tu teléfono.

Este PIN no tiene nada que ver con la billetera de Bitcoin en sí. De hecho, solo con la frase de recuperación podrás recuperar el acceso a todos tus bitcoins. El PIN solo bloquea el acceso a tu billetera en tu teléfono. Por lo tanto, la copia de seguridad de la frase es mucho más importante que la copia de seguridad de este PIN.

Luego podrás agregar una opción de bloqueo biométrico para evitar ingresar el PIN cada vez que lo uses. En general, la biometría es mucho menos segura que el PIN en sí. Por lo tanto, por defecto, te recomiendo que no actives esta opción de desbloqueo.

Debes ingresar el PIN elegido nuevamente en la aplicación Green para confirmarlo.

![image](assets/12.png)

¡Felicidades! Has terminado de crear tu billetera de Bitcoin.

![image](assets/14.png)

Si deseas agregar una frase de contraseña BIP39 a esta billetera de Bitcoin, debes hacer clic en los tres puntos en la parte superior derecha de la pantalla cuando ingreses tu PIN para desbloquear la billetera. Ten en cuenta que te desaconsejo firmemente usar una frase de contraseña si no comprendes los mecanismos de derivación involucrados. Podrías perder el acceso a tus bitcoins.

## Simulación de la recuperación de tu billetera de Bitcoin

Antes de enviar bitcoins a tu nueva billetera, es esencial realizar una prueba de recuperación para asegurarte de que tu copia de seguridad de la frase mnemotécnica funcione correctamente. En concreto, eliminaremos la billetera mientras aún está vacía y trataremos de recuperarla solo con la frase de recuperación, como si hubiéramos perdido el acceso a nuestro teléfono.

Además de verificar la validez de la frase, esta práctica también te permite practicar la recuperación de una billetera de Bitcoin. De esta manera, si alguna vez te encuentras en una situación de emergencia, sabrás exactamente qué pasos seguir para recuperar el acceso a tus fondos.

Para hacer esto, antes de eliminar tu billetera, debes obtener una información de referencia que te permita reconocerla más tarde. Por lo tanto, copiarás los últimos 8 caracteres de la primera dirección que se te proporcione.'
Para acceder a esta información, haz clic en el botón "Recibir". La billetera mostrará una dirección. Anota en otro trozo de papel los últimos 8 caracteres. Esto corresponde al checksum de la dirección.

Por ejemplo, en mi billetera, los 8 caracteres a anotar serían: JTbP4482.

![image](assets/16.png)

Una vez que hayas anotado esta información, puedes eliminar tu billetera. Desde la pantalla de inicio de la billetera, haz clic en el ícono de configuración y luego en "Desconectar".

> "Quiero aclarar una vez más que esta operación debe realizarse con una billetera vacía, antes de haber enviado bitcoins. De lo contrario, podrías perderlos".

![image](assets/19.png)

Luego serás redirigido a la pantalla de desbloqueo de tu billetera. Haz clic en los tres puntos en la esquina superior derecha de la pantalla y luego en "Eliminar billetera", y confirma.

![image](assets/21.png)

Ahora estás en la pantalla de inicio de la aplicación Green Wallet y no hay ninguna billetera disponible. Actualmente te encuentras en la misma situación que si hubieras perdido o roto tu teléfono y estuvieras intentando recuperar tu billetera solo con la frase mnemotécnica.

Ahora debes hacer clic en "Agregar billetera", luego en "Restaurar billetera" y finalmente en "Bitcoin".

![image](assets/23.png)

Luego, el software nos pregunta si queremos recuperarla a través de un código QR o mediante una frase mnemotécnica. En nuestro caso, es una frase.

A continuación, se nos solicita que ingresemos la frase de recuperación. Esta es la que anotamos al crear la billetera. Si estás utilizando una frase de 24 palabras, asegúrate de hacer clic en la casilla "24".

Una vez que hayas ingresado todas las palabras, si el software te indica que hay un error, significa que el checksum de tu frase no es correcto. En ese caso, significa que la copia de seguridad en papel de tu frase mnemotécnica es inválida. Debes reiniciar este tutorial desde el principio y asegurarte de escribir correctamente la frase cuando se te dé.

De lo contrario, puedes hacer clic en "Continuar".

![image](assets/26.png)

El software te mostrará "Billetera no encontrada". Esto es completamente normal ya que, por el momento, aún no hemos enviado bitcoins a esta billetera. Por lo tanto, no puede detectar ninguna transacción en la cadena de bloques relacionada con esta billetera.

Haz clic en "Restauración manual" en la parte inferior de la pantalla, luego en "Firma única".

![image](assets/28.png)

Por último, se te pedirá que le des un nombre a esta billetera y le asignes un PIN. Puedes darle el mismo nombre y PIN que a la billetera inicial.
Para recordar, este PIN solo tiene la funcionalidad de desbloquear la billetera en esta aplicación y en este teléfono específicamente. A diferencia de la frase de recuperación, no permite regenerar su billetera en otro software o hardware.
![image](assets/30.png)

Una vez que el PIN se ha validado, volverá a la página de inicio de su billetera. Es hora de verificar si su frase de recuperación funciona correctamente observando la primera dirección derivada. Para hacer esto, una vez más, haga clic en "Recibir" para acceder a la primera dirección.

Si los últimos 8 caracteres son exactamente los mismos que los que ha anotado como testigos en su papel antes de eliminar la billetera, entonces su frase es válida. En mi caso, se puede ver que el checksum de mi primera dirección es igual al valor anotado anteriormente: JTbP4482.

![image](assets/32.png)

Sé que esta práctica de verificación es tediosa, pero es absolutamente esencial para asegurar la seguridad de su billetera de Bitcoin. Le recomiendo encarecidamente que adquiera este hábito cuando cree una billetera, ya sea en software o hardware.

Con Green Wallet, utilicé la primera dirección para realizar este proceso. Sin embargo, también puede tomar como testigo una clave pública extendida (xpub/zpub) o la huella digital de la clave privada maestra (master fingerprint).

## Uso de la billetera Bitcoin Green Wallet

Una vez que haya configurado y verificado su billetera, podrá comenzar a usarla.

Para comenzar correctamente, le recomiendo que personalice la configuración de su billetera. Para hacerlo, haga clic en el ícono de configuración en la parte superior derecha de la pantalla.

- La opción "Unidad mostrada" le permite personalizar la unidad utilizada en su billetera. Si tiene fondos limitados, puede ser relevante mostrar su billetera en sats en lugar de bitcoins. El satoshi (sat) corresponde a una cienmillonésima parte de un bitcoin: 1 BTC = 100,000,000 sats.

- La opción "Monto de tarifas predeterminado" le permite personalizar las tarifas asignadas a sus transacciones de forma predeterminada. Cuanto más altas sean las tarifas por vbyte (byte virtual), más rápidamente se confirmarán sus transacciones. Luego podrá modificar esta tasa de tarifas en cada transacción emitida según la congestión de la red de Bitcoin.

- La opción "Conexión con biometría" le permite desbloquear su billetera con su huella digital en lugar del PIN. Por lo general, no recomiendo activar esta opción. La biometría es mucho menos segura que el código PIN.

![image](assets/34.png)
Por defecto, Green Wallet te asigna una cuenta BIP49 "Nested SegWit" con direcciones P2SH (Pay to Script Hash). Hace algunos años, el uso de este tipo de cuenta era relevante ya que no todos aún soportaban las direcciones nativas SegWit. Hoy en día, la gran mayoría de los servicios relacionados con Bitcoin admiten SegWit, por lo que ya no hay ninguna razón para utilizar una cuenta "Nested SegWit".

Entonces crearemos una nueva cuenta BIP84 "Native SegWit" para aprovechar todas sus ventajas, y también para tener direcciones P2WPKH (Pay to Witness Public Key Hash). Para hacerlo, haz clic en tu cuenta "Legacy SegWit Account", luego en "Agregar una nueva cuenta" y finalmente en "Cuenta SegWit". Luego puedes darle un nombre a esta cuenta si lo deseas.

![image](assets/36.png)

En el futuro, si necesitas crear nuevas cuentas en esta billetera, te recomiendo que elijas por defecto cuentas SegWit V0 BIP84 o SegWit V1 BIP86 (cuando estén disponibles).

En la página de inicio de tu billetera, puedes ver tus diferentes cuentas, incluida tu nueva cuenta SegWit.

Luego, el funcionamiento de la aplicación Green Wallet es muy sencillo. Para recibir bitcoins en tu billetera, haz clic en el botón "Recibir". La billetera te mostrará una dirección de recepción. Una dirección permite recibir bitcoins en tu billetera. Puedes copiarla en formato de texto para enviarla a quien te pague, o escanear el código QR con otra billetera Bitcoin para pagar la dirección.

![image](assets/38.png)

Este tipo de dirección no indica al pagador la cantidad que debe enviarte. También puedes crear una dirección que automáticamente solicite una cantidad elegida al pagador. Para hacerlo, haz clic en "Más opciones" e ingresa la cantidad deseada.

Dado que estás utilizando una cuenta SegWit V0 BIP84, tu dirección debería comenzar con el prefijo "bc1q". En mi ejemplo, estoy utilizando una billetera Testnet, por lo que el prefijo es ligeramente diferente al tuyo.

Una dirección de recepción no debe ser utilizada varias veces. Es una mala práctica que conlleva riesgos para tu privacidad. Por defecto, la billetera Green generará una nueva dirección cuando hagas clic en "Recibir" y la anterior ya haya sido utilizada. También puedes hacer clic en el icono de la flecha giratoria para solicitar una nueva dirección en blanco vinculada a tu billetera.

> "Consejo: Cuando copie y pegue una dirección de recepción, no es necesario verificar que cada carácter de la dirección sea correcto. De hecho, las direcciones incluyen una suma de verificación que permite detectar pequeños errores tipográficos. Solo es necesario verificar los primeros y últimos caracteres de la dirección para asegurarse de su validez.
> En las capturas de pantalla a continuación, puede ver que envié 0.02 btc a mi dirección. La transacción aparece en Green, primero como "no confirmada" mientras espera ser incluida en la cadena de bloques por un minero. Una vez que la transacción ha recibido varias confirmaciones, ha recibido sus bitcoins en su propia billetera.

![image](assets/40.png)

Si desea enviar bitcoins, debe obtener la dirección de recepción a la que desea enviar los fondos y hacer clic en el botón "Enviar". En la siguiente página, debe ingresar la dirección de destino. Puede ingresarla manualmente o escanear un código QR haciendo clic en el icono correspondiente. Luego elija el monto de la transacción. Puede ingresar un monto en bitcoins o un monto en dólares estadounidenses haciendo clic en la flecha doble blanca.

![image](assets/43.png)

En el centro de la pantalla, puede elegir la tarifa asignada a esta transacción. Puede optar por seguir las recomendaciones de la aplicación o personalizar sus tarifas. Cuanto más altas sean las tarifas en comparación con otras transacciones pendientes de confirmación, más rápido se incluirá su transacción y viceversa.

Luego haga clic en "Siguiente". Llegará a una pantalla que le muestra los detalles de su transacción. Puede verificar que la dirección ingresada sea correcta, que el monto sea el que desea enviar y que las tarifas sean correctas.

Para firmar la transacción y difundirla a la red de Bitcoin, deslice el botón verde en la parte inferior de la pantalla hacia la derecha.

![image](assets/46.png)

Su transacción ahora aparece en el panel de control de su billetera Bitcoin.

## Conclusión

¡Felicitaciones! Ahora tiene su propia billetera Bitcoin en custodia propia. Los bitcoins realmente le pertenecen.

Esta billetera Green Wallet de Blockstream es una excelente solución para principiantes con pocos bitcoins. Como pudo ver, es muy fácil de usar. Sin embargo, sigue siendo una billetera en línea. Si tiene grandes cantidades de bitcoins, le recomiendo que considere una billetera de hardware.

Una vez que haya aprendido a dominar Green Wallet y comprenda los mecanismos involucrados, puede explorar soluciones más completas como Samourai Wallet o Sparrow Wallet."

Para concluir, les recuerdo una vez más que es absolutamente necesario cuidar la copia de seguridad de su frase de recuperación. Esta frase brinda acceso directo e ilimitado a sus bitcoins. Si la pierde, no podrá recuperar sus bitcoins si su teléfono se pierde, se rompe o es robado. Cualquier persona que tenga acceso a esta frase podrá robarle sus bitcoins y no habrá forma de recuperarlos.

> Esta guía ha sido producida y pertenece a Bitstack. Bitstack es un banco de bitcoins neo con sede en París que permite el DCA en bitcoin. Guía escrita por Loic Morel el 15/02/2023. Esto les pertenece. [Enlace al artículo](https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet)

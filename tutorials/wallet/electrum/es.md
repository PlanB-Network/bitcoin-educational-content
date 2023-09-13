---
name: Electrum

description: Guía completa de Electrum, de 0 a héroe
---

![portada](assets/cover.png)

Descripción de Electrum

https://twitter.com/ElectrumWallet
https://electrum.org/
https://electrum.readthedocs.io/

# Monedero de Bitcoin Electrum

> "Debo decir que cuando encontré esta guía me sorprendí. Felicitaciones a Arman the Parman por esto. Hubiera sido una lástima no alojarlo aquí y traducirlo a tantos idiomas como sea posible. Honestamente, consejos de ese tipo." Rogzy

![Monedero de escritorio Electrum (Mac / Linux) - descargar, verificar, conectar a tu nodo.](https://youtu.be/wHmQNcRWdHM)

![Realizar una transacción de Bitcoin con Electrum](https://youtu.be/-d_Zd7VcAfQ)

## ¿Por qué Electrum?

Esta es una guía detallada sobre cómo utilizar el monedero de Bitcoin Electrum, con soluciones para todas sus trampas y peculiaridades, algo que he desarrollado después de varios años de uso y de enseñar a estudiantes sobre seguridad/privacidad de Bitcoin. Electrum no es el mejor monedero de Bitcoin para la persona que quiere mantener todo lo más simple posible y prefiere permanecer en el nivel principiante. En cambio, es para la persona que es o aspira a ser un usuario "avanzado".

Para el nuevo usuario de Bitcoin, es excelente solo si está bajo la supervisión de un usuario experimentado que le muestre el camino. Si aprenden a usarlo solos, sería seguro siempre y cuando se tomen su tiempo y lo utilicen en un entorno de prueba con solo una pequeña cantidad de satoshis al principio. Esta guía apoya ese esfuerzo, pero también es una buena referencia para cualquier otra persona.

> Advertencia: Esta guía es extensa. No intentes hacer todo esto en un solo día. Lo mejor es guardar la guía y avanzar poco a poco con el tiempo.

## Descargar Electrum

Idealmente, utiliza una computadora dedicada a Bitcoin para tus transacciones de Bitcoin (Mi guía para esto https://armantheparman.com/mint/) _(TAMBIÉN disponible en la sección de privacidad)_. Está bien practicar con pequeñas cantidades en una computadora "sucia" cuando estás aprendiendo por primera vez (quién sabe cuánto malware oculto ha acumulado tu computadora regular a lo largo de los años, no quieres exponer tus monederos de Bitcoin a ellos).

Obtén Electrum desde https://electrum.org/.

Haz clic en la pestaña de Descargas en la parte superior.

Haz clic en el enlace de descarga que corresponda a tu computadora. Cualquier computadora Linux o Mac puede usar el enlace de Python (círculo rojo). Una computadora Linux con un chip Intel o AMD puede usar el Appimage (círculo verde; esto es como un archivo ejecutable de Windows). Un dispositivo Raspberry Pi tiene un microprocesador ARM y solo puede usar la versión de Python (círculo rojo), no Appimage, aunque las Pi ejecutan Linux. El círculo azul es para Windows y el círculo negro es para Mac.

![imagen](assets/1.png)

## Verificar Electrum

El propósito de "verificar" la descarga es asegurarse de que no se haya alterado ni un solo bit de datos. Esto evita que uses una versión maliciosa "hackeada" del software. Está bien omitir esto siempre y cuando solo uses la copia descargada para practicar, es decir, no uses monederos que contengan dinero importante. Luego, cuando estés listo para usar Electrum con tus fondos reales, debes eliminar tu copia y comenzar de nuevo, esta vez verificando tu descarga.

Para hacer esto, utilizamos herramientas de criptografía de clave pública/privada, como gpg, de las cuales hemos escrito una guía aquí (https://armantheparman.com/gpg/). La herramienta gpg viene con todos los sistemas operativos Linux. Para Mac y Windows, consulta el enlace de gpg para obtener instrucciones de descarga.

Además de descargar el software Electrum, por seguridad, también necesitas la FIRMA digital del software. Esta es una cadena de texto (en realidad, es un número codificado usando texto) que el desarrollador produjo con su clave gpg PRIVADA. Usando el programa gpg, podemos luego "probar" la FIRMA contra su clave PÚBLICA (creada a partir de la clave privada del desarrollador) a la cual todos tienen acceso, en comparación con el ARCHIVO de descarga.

En otras palabras, con las tres entradas (firma, clave pública y archivo de datos), obtenemos una salida verdadera o falsa para confirmar que el archivo no ha sido manipulado.

Para obtener la firma, haz clic en el enlace correspondiente al archivo que descargaste (ver flechas de colores):

![imagen](assets/2.png)

Al hacer clic en el enlace, es posible que el archivo se descargue automáticamente en tu carpeta de descargas o que se abra en el navegador. Si se abre en el navegador, debes guardar el archivo. Puedes hacer clic derecho y seleccionar "guardar como". Dependiendo del sistema operativo o navegador, es posible que debas hacer clic derecho en el área de espacio en blanco, no en el texto.

A continuación, se muestra cómo se ve el texto descargado. Puedes ver que hay múltiples firmas, estas son firmas de diferentes personas. Puedes verificar cada una o cualquiera. Te mostraré cómo verificar solo la del desarrollador.

![imagen](assets/3.png)

A continuación, necesitas obtener la clave pública de ThomasV, que es el principal desarrollador. Puedes obtenerla directamente de él, de su cuenta de Keybase, Github, de alguien más, de un servidor de claves o del sitio web de Electrum.

Obtenerla del sitio web de Electrum es en realidad la forma menos segura, porque si este sitio web es malicioso (lo que estamos comprobando), ¿por qué obtendríamos una clave pública de él (la clave pública podría ser falsa)?

Para simplificarlo por ahora, te mostraré cómo obtenerla del sitio web de todos modos, pero ten esto en cuenta. Aquí está la copia (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc) en GitHub, con la que puedes compararla.

Desplázate un poco hacia abajo en la página para encontrar el enlace a la clave pública de ThomasV (círculo rojo a continuación). Haz clic en él y descárgalo, o si se abre algún texto en el navegador, haz clic derecho para guardarlo.

![imagen](assets/4.png)

Ahora tienes 3 archivos nuevos, probablemente todos en la carpeta de descargas. No importa dónde estén, pero el proceso es más fácil si los colocas todos en la misma carpeta.

Los tres archivos son:

1. La descarga de Electrum
2. El archivo de firma (generalmente tiene el mismo nombre de archivo que la descarga de Electrum con una extensión ".asc")
3. La clave pública de ThomasV.

Abre una terminal en Mac o Linux, o el símbolo del sistema (CMD) en Windows.

Navega hasta el directorio de Descargas (o donde hayas colocado los tres archivos). Si no tienes idea de lo que esto significa, aprende de este breve video para Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) y este otro para Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Recuerda que en las computadoras Linux, los nombres de los directorios distinguen entre mayúsculas y minúsculas.
En la terminal, escribe esto para importar la clave pública de ThomasV en el "keyring" de tu computadora (el "keyring" es un concepto abstracto, en realidad es solo un archivo en tu computadora):

```
gpg --import ThomasV.asc
```

Asegúrate de que el nombre del archivo coincida con el que has descargado. También, ten en cuenta que hay dos guiones antes y después de "import". Luego presiona <enter>.

El archivo debería importarse. Si recibes un error, verifica que te encuentres en el directorio donde realmente existe el archivo. Para verificar en qué directorio te encuentras (en Mac o Linux), escribe pwd. Para ver qué archivos hay en el directorio en el que te encuentras (en Mac o Linux), escribe ls. Deberías ver el archivo de texto "ThomasV.asc" en la lista, posiblemente junto con otros archivos.

Luego ejecutamos el comando para verificar la firma.

```
gpg –verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Observa que hay 4 "elementos" aquí, separados por un espacio. He resaltado en negrita el texto alternativamente para ayudarte a verlo. Los cuatro elementos son:

1. el programa gpg
2. la opción –verify
3. el nombre del archivo de la firma
4. el nombre del programa

De interés, a veces puedes omitir el cuarto elemento y la computadora adivinará a qué te refieres. No estoy seguro, pero creo que solo funciona si los nombres de archivo solo difieren por el "asc" al final.

No copies simplemente los nombres de archivo que he mostrado aquí, asegúrate de que coincidan con el nombre del archivo que tienes en tu sistema.

Presiona <enter> para ejecutar el comando. Deberías ver una "buena firma de ThomasV" para indicar que fue exitoso. Habrá algunos errores porque no tenemos las claves públicas de las firmas de otras personas que están contenidas en el archivo de firma (este sistema de combinar firmas en un solo archivo puede cambiar en versiones posteriores). Además, hay una advertencia en la parte inferior que podemos ignorar (esto nos alerta de que no le hemos dicho explícitamente a la computadora que confiamos en la clave pública de ThomasV).

Ahora tenemos una copia verificada de Electrum que es segura de usar.

## Ejecutando Electrum

### Ejecutando Electrum si usas Python

Si descargaste la versión de Python, así es como puedes hacer que funcione. Verás esto en la página de descarga:

![image](assets/5.png)

Para Linux, es una buena idea actualizar primero tu sistema:

```
sudo apt-get update
sudo apt-get upgrade
```

Copia el texto amarillo resaltado, pégalo en la terminal y presiona <enter>. Se te pedirá tu contraseña, posiblemente una confirmación para continuar, y luego se instalarán esos archivos ("dependencias").

También necesitarás extraer el archivo comprimido a un directorio de tu elección. Puedes hacer esto con la interfaz gráfica de usuario o desde la línea de comandos (comando resaltado en rosa) - recuerda que los nombres de tus archivos pueden ser diferentes. (Ten en cuenta que cuando verificamos la descarga en la sección anterior, verificamos el archivo zip, no el directorio extraído).

Hay una opción de "instalación" usando el programa PIP, pero esto es innecesario y agrega pasos adicionales e instalación de archivos. Simplemente ejecuta el programa usando la terminal para evitar todo eso.

Los pasos (Linux) son:

1. navegar hasta el directorio donde se extrajeron los archivos
2. escribir: ./run_electrum

En un Mac, los pasos son los mismos, pero es posible que primero necesites instalar Python3 y usar este comando para ejecutarlo:

````
```python3 ./run_electrum```
````

Una vez que Electrum esté en funcionamiento, la ventana de la terminal permanecerá abierta. Si la cierras, se terminará el programa de Electrum. Solo minimízala mientras uses Electrum.

### Ejecutar Electrum con Appimage

Esto es un poco más fácil, pero no tan fácil como un archivo ejecutable de Windows. Dependiendo de la versión de Linux que estés utilizando, por defecto, los archivos Appimage pueden tener atributos configurados para que el sistema no permita su ejecución. Debemos cambiar esto. Si tu Appimage funciona, puedes omitir este paso. Navega hasta donde se encuentra el archivo, utilizando la terminal, y luego ejecuta este comando:

```
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

"sudo" otorga privilegios de superusuario; "chmod" es un comando para cambiar el modo, alterando quién puede leer, escribir o ejecutar; "ug+x" significa que estamos modificando el usuario y el grupo para permitir la ejecución.

Ajusta el nombre del archivo para que coincida con tu versión.

Luego, Electrum se ejecutará haciendo doble clic en el icono de Appimage.

### Ejecutar Electrum en Mac

Simplemente haz doble clic en el archivo descargado (es un "disco"). Se abrirá una ventana. Arrastra el icono de Electrum en la ventana hacia tu escritorio, o donde quieras guardar el programa. Luego puedes "expulsar" el disco y eliminar el archivo descargado.

Para ejecutar el programa, simplemente haz doble clic en él. Es posible que aparezcan algunos errores específicos de Mac que deban ser omitidos.

### Ejecutar Electrum en Windows

A pesar de que odio Windows más que cualquier otro sistema operativo, este es el método más sencillo. Simplemente haz doble clic en el archivo ejecutable para ejecutarlo.

## Comenzar con una billetera ficticia

Cuando cargues Electrum por primera vez, se abrirá una ventana como esta:

![image](assets/6.png)

Más adelante seleccionaremos tu servidor manualmente, pero por ahora, deja el valor predeterminado y la conexión automática.

A continuación, crea una billetera ficticia; nunca pongas fondos en esta billetera. El propósito de esta billetera ficticia es avanzar a través del software y asegurarte de que todo funcione correctamente antes de cargar tu billetera real. Estamos tratando de evitar revelar accidentalmente la privacidad con una billetera real. Si solo estás practicando, la billetera que crees se puede considerar una billetera ficticia de todos modos.

Puedes dejar el nombre como "default_wallet" o cambiarlo a lo que prefieras, y haz clic en siguiente. Más adelante, si tienes varias billeteras, puedes encontrarlas y abrirlas en esta etapa haciendo clic en "Elegir..."

![image](assets/7.png)

Elige "Billetera estándar" y <Siguiente>:

![image](assets/8.png)

Luego, selecciona "Ya tengo una semilla". No quiero que te acostumbres a crear una semilla de Electrum, ya que utiliza su propio protocolo que no es compatible con otras billeteras; por eso no hacemos clic en "nueva semilla".

![image](assets/9.png)

Ve a https://iancoleman.io/bip39/ y crea una semilla ficticia. Primero, cambia el número de palabras a 12 (que es una práctica común), luego haz clic en "generar" y copia las palabras en el cuadro al portapapeles.

![image](assets/10.png)

Luego pega las palabras en Electrum. Aquí tienes un ejemplo:

![image](assets/11.png)

Electrum buscará palabras que coincidan con su propio protocolo. Tenemos que evitar eso. Haz clic en opciones y selecciona "Semilla BIP39":

![image](assets/12.png)

La semilla entonces se vuelve válida. (Antes de hacer esto, Electrum esperaba una semilla de Electrum, por lo que esta semilla se consideraba inválida). Antes de hacer clic en siguiente, fíjate en el texto que dice "Checksum OK". Es importante (para la billetera real que puedas usar más adelante) que veas esto antes de continuar, ya que confirma la validez de la semilla que ingresaste. La advertencia cerca de la parte inferior se puede ignorar, es la queja del desarrollador de Electrum sobre BIP39 y sus afirmaciones "FUD" de que su versión (que no es compatible con otras billeteras) es superior.

> Un pequeño desvío para una advertencia importante. El propósito del checksum es asegurarse de que hayas ingresado tu semilla sin errores de escritura. El checksum es la parte final de la semilla (la palabra número 12 termina siendo la palabra de checksum) que se determina matemáticamente por la primera parte de la semilla (11 palabras). Si escribieras algo incorrecto al principio, la palabra de checksum no coincidirá matemáticamente y el software de la billetera te alertará con una advertencia. Esto no significa que la semilla no se pueda usar para crear una billetera de Bitcoin funcional. Imagina crear una billetera con un error de escritura, cargar la billetera con bitcoin y luego un día necesitar restaurar la billetera, pero cuando lo hagas, no recrearás el error de escritura, ¡restaurarás la billetera equivocada! Es bastante peligroso que Electrum te permita continuar y crear una billetera si tu checksum es inválido, así que ten cuidado, es tu responsabilidad asegurarte. Otras billeteras no te permitirán continuar, lo cual es mucho más seguro. Esto es una de las cosas a las que me refiero cuando digo que Electrum está bien para usar, una vez que aprendes a usarlo correctamente (los desarrolladores de Electrum deberían solucionar esto).

Ten en cuenta que si deseas agregar una frase de contraseña, la opción para seleccionarla está en esta ventana de opciones, justo en la parte superior.

Después de hacer clic en OK, volverás a donde escribiste la frase de la semilla. Si seleccionaste una opción de frase de contraseña, NO la ingreses con las palabras de la semilla (la indicación para eso vendrá después).

Si no solicitaste una frase de contraseña, verás esta pantalla a continuación: más opciones para el tipo de script y la ruta de derivación de tu billetera, sobre las cuales puedes obtener más información aquí (https://armantheparman.com/public-and-private-keys/), pero simplemente deja los valores predeterminados y continúa.

![image](assets/13.png)

> Para información adicional: La primera opción te permite elegir entre legacy (direcciones que comienzan con "1"), pay-to-script-hash (direcciones que comienzan con "3") o bech32/native segwit (direcciones que comienzan con "bc1q"). En el momento de escribir esto, Electrum aún no admite taproot (direcciones que comienzan con "bc1p"). La segunda opción en esta ventana te permite modificar la ruta de derivación. Te sugiero que nunca modifiques esto, especialmente antes de entender qué significa. Las personas enfatizarán la importancia de escribir la ruta de derivación para que puedas recuperar tu billetera si es necesario, pero si la dejas como predeterminada, probablemente estarás bien, así que no entres en pánico, pero aún así es una buena práctica escribir la ruta de derivación.

A continuación, se te dará la opción de agregar una CONTRASEÑA. Esto no debe confundirse con "FRASE DE CONTRASEÑA". Una contraseña bloquea el archivo en tu computadora. Una frase de contraseña es parte de la composición de la clave privada. Dado que esta es una billetera ficticia, puedes dejar la contraseña en blanco y continuar.

![image](assets/14.png)

Obtendrás una ventana emergente sobre las notificaciones de nuevas versiones (te sugiero que selecciones no). La billetera se generará y estará lista para usar (pero recuerda, esta billetera está destinada a ser eliminada, es solo una billetera ficticia).

![image](assets/15.png)

Hay algunas cosas que te sugiero hacer para configurar el entorno de software (solo se requiere una vez):

### Cambiar las unidades a BTC

Ve al menú superior, herramientas -> preferencias de electrum, y allí, en la pestaña general, encontrarás la opción para cambiar la "unidad base" a BTC.
Habilitar la pestaña de Direcciones y Monedas

Ve al menú superior, ver, y selecciona "mostrar direcciones". Luego vuelve a ver y selecciona "mostrar monedas".

### Habilitar Oneserver

Por defecto, Electrum se conecta a un nodo aleatorio. También se conecta a muchos otros nodos secundarios. No estoy seguro de qué datos se intercambian con esos nodos secundarios, pero no queremos que eso suceda por motivos de privacidad. Incluso si especificas un nodo, por ejemplo, tu propio nodo, también se conectarán estos múltiples nodos secundarios, y no estoy seguro de qué información se comparte. Sin embargo, es fácil de prevenir. Antes de mostrarte cómo especificar tu propio nodo, obligaremos a Electrum a conectarse solo a un servidor a la vez.

> Hay una forma de hacer esto especificando "oneserver" desde la línea de comandos, pero no recomiendo este método. Mostraré una alternativa que creo que es más fácil a largo plazo y menos probable que te conectes accidentalmente a otros nodos.

La razón por la que estamos usando una billetera ficticia es que si hubiéramos cargado nuestra billetera real, con nuestros bitcoins reales, habríamos conectado inadvertidamente a un nodo aleatorio en este momento (incluso si seleccionamos "establecer servidor manualmente" al principio, aún se conecta a estos otros nodos secundarios por alguna razón (oye desarrolladores de Electrum, deberían solucionar esto). Si nuestra billetera fuera privada, esto sería un desastre.

Tampoco podemos realizar los pasos que te mostraré a continuación sin cargar primero algún tipo de billetera. (Vamos a editar un archivo de configuración que solo se completa y está listo para editar una vez que se carga una billetera).

**Apaga Electrum (IMPORTANTE, si no haces esto, los cambios que realices se borrarán).**

### Archivo de configuración LINUX/MAC

Abre la terminal en Linux o Mac (instrucciones para Windows más adelante):

Deberías estar automáticamente en la carpeta de inicio. Desde allí, navega hasta la carpeta oculta de configuración de electrum (esto es diferente a donde se encuentra la aplicación).

```
cd .electrum
```

Observa el punto antes de "electrum", que indica que es una carpeta oculta.

Otra forma de llegar allí es escribir:

```
cd ~/.electrum
```

donde "~" representa la ruta de tu directorio de inicio. Puedes ver la ruta completa de tu directorio actual con el comando "pwd".

Una vez en el directorio ".electrum", escribe "nano config" y presiona <enter>.

Se abrirá un editor de texto (llamado nano) con el archivo de configuración abierto. El mouse no funciona mucho aquí. Usa las teclas de flecha para llegar a la línea que dice:

```
"oneserver": false,
```

Cambia "false" a "true"; y no alteres la sintaxis (no borres la coma o el punto y coma).

Presiona <ctrl> x para salir, luego "y" para guardar, luego <enter> para confirmar los cambios sin editar el nombre del archivo.
Ahora ejecuta Electrum nuevamente. Luego haz clic en el círculo en la parte inferior derecha, que abre la configuración de red. Luego, cerca de la parte superior en la pestaña de resumen, verás "conectado a 1 nodo", lo cual indica éxito.
Justo debajo de eso, verás un campo de texto y la dirección del servidor está ahí. Actualmente estás conectado a ese nodo aleatorio. Más información sobre cómo conectarse a un nodo en la siguiente sección.

### Archivo de configuración de Windows

El archivo de configuración de Windows es un poco más difícil de encontrar. El directorio es:

```
C:/Users/Parman/AppData/Roaming/Electrum
```

Obviamente, debes cambiar "Parman" por tu propio nombre de usuario en la computadora.

En esa carpeta encontrarás el archivo de configuración. Ábrelo con un editor de texto y edita la línea:

```
"oneserver": false,
```

Cambia "false" por "true"; no alteres la sintaxis (no elimines la coma o el punto y coma).

Luego guarda el archivo y sal.

## Conectar Electrum a un nodo

A continuación, queremos conectar nuestra billetera ficticia a un nodo de nuestra elección. Si no estás listo para ejecutar un nodo, puedes hacer una de las siguientes opciones:

1. Conectarte al nodo personal de un amigo (requiere Tor)
2. Conectarte al nodo de una empresa confiable
3. Conectarte a un nodo aleatorio (no recomendado).

Por cierto, aquí tienes instrucciones para ejecutar tu propio nodo, y estas son las razones por las que deberías hacerlo (todos los tutoriales en la sección de Nodo o en nuestros cursos gratuitos).

### Conectarse al nodo de un amigo a través de Tor (Guía próximamente).

### Conectarse al nodo de una empresa confiable

La única razón para hacer esto sería si necesitas acceder a la cadena de bloques y no tienes disponible tu propio nodo (o el de un amigo).

Conectémonos al nodo de Bitaroo: nos dicen que no están recopilando datos. Son un intercambio solo de Bitcoin, dirigido por un apasionado de Bitcoin. Conectarse a ellos implica un poco de confianza, pero es mejor que conectarse a un nodo aleatorio, que podría ser una empresa de vigilancia.

Ve a la Configuración de Red haciendo clic en el círculo en la parte inferior derecha de la ventana de la billetera (el rojo indica no conectado, el verde indica conectado y el azul indica conectado a través de Tor).

![image](assets/16.png)

Una vez que hagas clic en el ícono del círculo, aparecerá una ventana emergente: Tu billetera mostrará "conectado a 1 nodo" ya que lo forzamos anteriormente.

Desmarca la casilla "seleccionar servidor automáticamente" y luego en el campo del servidor, escribe los detalles de Bitaroo como se muestra:

![image](assets/17.png)

Cierra la ventana y ahora deberíamos estar conectados al nodo de Bitaroo. Para confirmar, el círculo debería ser verde. Haz clic nuevamente en él y verifica que los detalles del servidor no hayan vuelto a cambiar a un nodo aleatorio.

### Conectarse a tu propio nodo

Si tienes tu propio nodo, eso es genial. Si solo tienes Bitcoin Core y no un SERVIDOR de Electrum también, aún no podrás conectar una BILLETERA de Electrum a tu nodo.

> Nota: El Servidor de Electrum y la Billetera de Electrum son cosas diferentes. El servidor es el software necesario para que la Billetera de Electrum pueda comunicarse con la cadena de bloques de Bitcoin; no sé por qué se diseñó de esta manera, posiblemente para mayor velocidad, pero podría estar equivocado.
> Si ejecutas un paquete de software de nodo como MyNode (el que recomiendo a las personas para comenzar), Raspiblitz (recomendado a medida que te vuelves más avanzado) o Umbrel (personalmente aún no lo recomiendo ya que he experimentado demasiados problemas), entonces podrás conectar tu billetera simplemente ingresando la dirección IP de la computadora (Raspberry Pi) que ejecuta el nodo, seguido de dos puntos y 50002, como se muestra en la imagen de la sección anterior. (Más adelante te mostraré cómo encontrar la dirección IP de tu nodo).
> Abre la configuración de red (haz clic en el círculo verde o rojo en la esquina inferior derecha). Desmarca la casilla "seleccionar servidor automáticamente" y luego ingresa tu dirección IP como lo he hecho yo, la tuya será diferente, pero los dos puntos y "50002" deberían ser iguales.

![image](assets/18.png)

Cierra la ventana y ahora deberíamos estar conectados a tu nodo. Para confirmar, haz clic en el círculo nuevamente y verifica que los detalles del servidor no hayan vuelto a cambiar a un nodo aleatorio.

A veces, a pesar de hacer todo correctamente, parece que se niega a conectarse. Aquí hay algunas cosas que puedes intentar...

- Actualiza a una versión más nueva de Electrum y tu software de nodo.
- Intenta eliminar la carpeta de caché en el directorio ".electrum".
- Intenta cambiar el puerto de 50002 a 50001 en la configuración de red.
- Utiliza esta guía para conectarte utilizando Tor como alternativa (https://armantheparman.com/tor/).
- Reinstala el servidor Electrum en el nodo.

## CÓMO ENCONTRAR LA DIRECCIÓN IP DE TU NODO

Una dirección IP no es algo que un usuario regular comúnmente sepa cómo buscar y usar. He ayudado a muchas personas a ejecutar un nodo y luego conectar sus billeteras al nodo, y un obstáculo común parece ser encontrar su dirección IP.

Para MyNode, puedes escribir en una ventana del navegador:

```
mynode.local
```

A veces, "mynode.local" no funciona (asegúrate de no escribirlo en la barra de búsqueda de Google). Para forzar la barra de navegación a reconocer tu texto como una dirección y no como una búsqueda, precede el texto con http://

así:

```
http://mynode.local
```

si eso no funciona, pruébalo con una "s", así:

```
https://mynode.local
```

Esto accederá al dispositivo y puedes hacer clic en el enlace de configuración (ver mi "círculo" azul a continuación) para mostrar esta pantalla donde se encuentra la dirección IP:

![image](assets/19.png)

Esta página se cargará y verás la dirección IP del nodo (círculo azul).

![image](assets/20.png)

Luego, en el futuro, puedes escribir 192.168.0.150 o http://192.168.0.150 en tu navegador.

Para el Raspiblitz (cuando no se conecta una pantalla), necesitas un método diferente (que también funciona para MyNode):

Inicia sesión en la página web de tu enrutador: aquí encontraremos la dirección IP de todos tus dispositivos conectados. La página web del enrutador será una dirección IP que ingreses en un navegador web. La mía es:

    http://192.168.0.1

Para obtener las credenciales de inicio de sesión del enrutador, puedes buscarlas en el manual del usuario o a veces incluso en una etiqueta pegada en el propio enrutador. Busca el nombre de usuario y la contraseña. Si no puedes encontrarlo, prueba con Usuario: "admin" Contraseña: "password".
Si puedes iniciar sesión, verás tus dispositivos conectados y por sus nombres, puede ser claro cuál es tu nodo. La dirección IP estará allí.

### Si los primeros dos métodos fallan, el último funcionará pero es tedioso:

Primero, encuentra la dirección IP de cualquier dispositivo en tu red (la computadora actual servirá).

En una Mac, la encontrarás en las preferencias de red:

![image](assets/21.png)

Nos interesan los primeros 4 elementos (192.168.0), no el cuarto elemento, el "166" que ves en la imagen (el tuyo será diferente).

Para Linux, usa la línea de comandos:

```
ifconfig | grep inet
```

Esa línea vertical es el símbolo de "pipe" y lo encontrarás debajo de la tecla <delete>. Verás alguna salida y una dirección IP. (Ignora 127.0.0.1, no es eso, e ignora la máscara de red)

Para Windows, abre el símbolo del sistema (cmd) y escribe:

```
ipconfig/all
```

y presiona Enter. La dirección IP se puede encontrar en la salida.

Eso fue lo fácil. La parte difícil es encontrar la dirección IP de tu nodo, necesitamos adivinar por fuerza bruta. Digamos, por ejemplo, que la dirección IP de tu computadora comienza con 192.168.0.xxx, entonces para tu nodo, en un navegador, intenta:

```
https://192.168.0.2
```

El número más pequeño posible es 2 (0 significa cualquier dispositivo, y 1 pertenece al enrutador) y el más alto, creo que es 255 (esto resulta ser 11111111 en binario, el número más grande que puede contener 1 byte).

Uno por uno, avanza hacia 255. Eventualmente, te detendrás en el número correcto que carga tu página de MyNode (o página de RaspiBlitz). Entonces sabrás qué número ingresar en la configuración de red de Electrum para conectarte a tu nodo.

Se verá algo así (asegúrate de incluir los dos puntos y el número después):

![image](assets/22.png)

> Es útil saber que estas direcciones IP son INTERNAS a tu red doméstica. Nadie externo puede verlas y no son sensibles. Son como extensiones telefónicas en una gran organización que te dirigen a diferentes teléfonos.

## Eliminar billetera falsa

Ahora hemos conectado con éxito a un único nodo. Así es como Electrum se cargará de forma predeterminada a partir de ahora. Ahora debes eliminar la billetera falsa (Menú: archivo -> eliminar), en caso de que accidentalmente envíes fondos a esta billetera insegura (es insegura porque no la creamos de manera segura).

## Crear una billetera de práctica

Después de eliminar la billetera falsa, comienza de nuevo y crea una nueva, de la misma manera, pero esta vez, anota las palabras de recuperación y guárdalas de manera segura.

Es una buena idea aprender cómo funciona Electrum con esta billetera de práctica, sin la engorrosa billetera de hardware (necesaria para alta seguridad). Solo coloca una pequeña cantidad de bitcoin en esta billetera: asume que perderás este dinero. Una vez que seas competente, luego aprende a usar Electrum con una billetera de hardware.

En la nueva billetera que has creado, verás una lista de direcciones. Las verdes se llaman "direcciones de recepción". Son producto de 3 cosas:

- La frase de recuperación
- La frase de contraseña
- La ruta de derivación
  Tu nueva billetera tiene un conjunto de direcciones de recepción que pueden ser creadas matemáticamente y de forma reproducible por cualquier billetera de software que tenga la semilla, la frase de contraseña y la ruta de derivación. ¡Hay 4.300 millones de ellas! Más de las que necesitarás. Electrum solo te muestra las primeras 20, y luego más a medida que uses las primeras.

Más información sobre las claves privadas de Bitcoin se puede encontrar en esta guía.

![image](assets/23.png)

Esto es muy diferente a algunas otras billeteras que solo presentan una dirección a la vez.

Debido a que ingresaste la frase de semilla al crear esta billetera, Electrum tiene la clave privada de cada una de las direcciones, y es posible gastar desde estas direcciones.

También ten en cuenta que hay direcciones amarillas, llamadas "direcciones de cambio" - Estas son solo otro conjunto de direcciones de una rama matemática diferente (otras 4.300 millones de estas existen). Son utilizadas por la billetera para enviar automáticamente los fondos excedentes de vuelta a la billetera como cambio. Por ejemplo, si tomas 1.5 bitcoin y gastas 0.5 en un comercio, los 1.0 restantes necesitan ir a algún lugar. Tu billetera los enviará a la siguiente dirección de cambio amarilla vacía, ¡de lo contrario, irán al minero! Para obtener más información sobre esto (UTXOs), consulta esta guía. (https://armantheparman.com/utxo/)

A continuación, regresa al sitio web de la clave privada de Ian Colman e ingresa la semilla (en lugar de generar una). Verás que la información de la clave privada y pública cambia; todo lo que está debajo depende de lo anterior en la página.

> Recuerda, "nunca" debes ingresar la semilla en una computadora para tu billetera de Bitcoin real, ya que el malware puede robarla. Solo estamos usando una billetera de práctica, con fines de aprendizaje, así que está bien por ahora.

Desplázate hacia abajo y cambia la ruta de derivación a BIP84 (segwit) para que coincida con tu billetera Electrum haciendo clic en la pestaña BIP84.

![image](assets/24.png)

Debajo de eso, verás la clave privada extendida de la cuenta y la clave pública extendida de la cuenta:

![image](assets/25.png)

Ve a Electrum y compara que coincidan. Hay un menú en la parte superior, billetera -> información:

![image](assets/26.png)

Esto aparecerá:

![image](assets/27.png)

Observa que las dos claves públicas coinciden.

A continuación, compara las direcciones. Regresa al sitio de Ian Coleman y desplázate hacia abajo:

![image](assets/28.png)

Observa que coinciden con las direcciones en Electrum.

Ahora verificaremos las direcciones de cambio. Desplázate un poco hacia arriba hasta la ruta de derivación y cambia el último 0 por un 1:

![image](assets/29.png)

Ahora desplázate hacia abajo y compara que las direcciones coincidan con las direcciones amarillas en Electrum.

¿Por qué hicimos todo esto?

Tomamos las palabras de la semilla y las pasamos por dos programas de software independientes para asegurarnos de que nos estaban dando la misma información. Esto reduce significativamente el riesgo de que haya código malicioso oculto que nos proporcione claves privadas o públicas, o direcciones falsas.

Lo siguiente que debes hacer es recibir una pequeña prueba y gastarla dentro de la billetera de una dirección a otra.

## Probando la billetera (Aprende a usarla)

Aquí te mostraré cómo recibir un UTXO en tu billetera y luego moverlo (gastarlo) a otra dirección dentro de la billetera. Esta es una cantidad muy pequeña que no nos importará arriesgar a perder.

Esto tiene varios propósitos.

- Demostrará que tienes el poder de gastar monedas en la nueva billetera.
- Demostrará cómo usar el software Electrum para hacer un gasto (y algunas características), antes de agregar complejidad adicional para la seguridad (usando una billetera de hardware o una computadora sin conexión a internet).
- Reforzará la idea de que tienes muchas direcciones para elegir para recibir y gastar, dentro de la misma billetera.

Abre tu billetera de prueba Electrum y haz clic en la pestaña "Direcciones", luego haz clic derecho en la primera dirección y selecciona Copiar -> Dirección:

![image](assets/30.png)

La dirección ahora está en la memoria de tu computadora.

Ahora ve a un intercambio donde tengas algunos bitcoins y vamos a retirar una pequeña cantidad a esta dirección, digamos 50,000 sats. Voy a usar Coinbase como ejemplo porque es el intercambio más comúnmente utilizado, aunque sean enemigos de Bitcoin y me disguste iniciar sesión en una cuenta antigua abandonada para este propósito.

Inicia sesión y haz clic en el botón "Enviar/Recibir", que hoy en día se encuentra en la esquina superior derecha de la página web.

![image](assets/31.png)

Obviamente no tengo fondos en Coinbase, pero imagina que hay fondos aquí y sigue los pasos: pega la dirección de Electrum en el campo "Para" como lo he hecho. También necesitarás seleccionar una cantidad (sugiero alrededor de 50,000 sats). No pongas un "mensaje opcional": Coinbase está recopilando suficiente información tuya (y vendiéndola), no hay necesidad de ayudarles. Por último, haz clic en "Continuar". Después de eso, no sé qué otras ventanas emergentes aparecerán, estás por tu cuenta, pero el método es similar para todos los intercambios.

![image](assets/32.png)

Dependiendo del intercambio, es posible que veas los sats en tu billetera de inmediato o que haya un retraso de horas/días.

Ten en cuenta que Electrum te mostrará las monedas recibidas incluso si no se han confirmado en la cadena de bloques. Las monedas que tienes se están leyendo desde la lista de espera de un nodo de Bitcoin, o "mempool". Cuando se incluyan en un bloque, verás los fondos como confirmados.

Ahora que tenemos un UTXO en nuestra billetera, deberíamos etiquetarlo. Solo nosotros podemos ver esta etiqueta, no tiene nada que ver con el libro mayor público. Todas nuestras etiquetas de Electrum solo son visibles en la computadora que estamos usando. De hecho, podemos guardar un archivo y usarlo para restaurar todas nuestras etiquetas en una computadora diferente que ejecute la misma billetera.

### Hacer una etiqueta para un UTXO

Necesitaba una donación para esta billetera de prueba, gracias a @Sathoarder por proporcionarme un UTXO en vivo (10,000 sats), y otra persona (anónima) donó a la misma dirección (5000 sats). Observa que hay 15,000 sats en el saldo de la primera dirección y un total de 2 transacciones (columna de la extrema derecha). En la parte inferior, el saldo es de 10,000 sats confirmados y otros 5,000 sats están sin confirmar (todavía en el mempool).

![image](assets/33.png)

Ahora, si vamos a la pestaña "Monedas", podemos ver dos "monedas recibidas" o UTXOs. Ambos están en la misma dirección.

![image](assets/34.png)

Volviendo a la pestaña de direcciones, si haces doble clic en el área de "etiquetas" junto a la dirección, podrás ingresar algún texto y luego presionar <enter> para guardar:

![image](assets/35.png)
Esta es una buena práctica para que puedas hacer un seguimiento de dónde provienen tus monedas, si son KYC-free o no, y cuánto te costó cada UTXO (en caso de que necesites vender y calcular el impuesto que tu gobierno te robará).
Idealmente, debes evitar acumular múltiples monedas en la misma dirección. Si decides hacerlo (no lo hagas), puedes etiquetar cada moneda en lugar de todas ellas con la misma etiqueta utilizando el método de dirección. En realidad, no puedes ir a la pestaña "monedas" y editar las etiquetas allí (no, ¡eso sería demasiado intuitivo!). Tienes que ir a la pestaña Historial, encontrar la transacción, etiquetarla y luego verás las etiquetas en la sección de monedas. Cualquier etiqueta que veas en la sección de monedas proviene de las etiquetas de dirección O las etiquetas de historial, pero cualquier etiqueta de historial anula cualquier etiqueta de dirección. Para hacer una copia de seguridad de tus etiquetas en un archivo, puedes exportarlas desde el menú en la parte superior, billetera->etiquetas->exportar.

A continuación, gastemos las monedas de la primera dirección a la segunda dirección. Haz clic derecho en la primera dirección y selecciona "gastar desde" (esto en realidad no es necesario en este escenario, pero imagina que tenemos muchas monedas en muchas direcciones; utilizando esta función, podemos obligar a la billetera a gastar solo las monedas que queremos. Si queremos seleccionar varias monedas en varias direcciones, podemos seleccionar las direcciones con un clic izquierdo mientras mantenemos presionada la tecla de comando, luego hacer clic derecho y seleccionar "gastar desde":

![image](assets/36.png)

Una vez que hagas eso, habrá una barra verde en la parte inferior de la ventana de la billetera que indica la cantidad de monedas que has seleccionado y el total disponible para gastar.

También puedes gastar monedas individuales dentro de una dirección y excluir otras en la misma dirección, pero esto no se recomienda porque estás dejando monedas en una dirección que ha sido debilitada criptográficamente debido al gasto de una de las monedas (otra razón para no poner múltiples monedas en una dirección, además de razones de privacidad, es que dado que debes gastarlas todas si gastas una, esto se vuelve innecesariamente costoso). Así es cómo seleccionar una sola moneda de una dirección compartida, pero no lo hagas:

![image](assets/37.png)

Ahora, tenemos las dos monedas seleccionadas para gastar. A continuación, decidimos dónde gastarlas. Enviémoslas a la segunda dirección. Necesitaremos copiar la dirección de la siguiente manera:

![image](assets/38.png)

Luego ve a la pestaña "Enviar" y pega la segunda dirección en el campo "pagar a". No es necesario agregar una descripción; podrías hacerlo, pero puedes hacerlo más tarde editando las etiquetas. Para la cantidad, selecciona "Máx" para gastar todas las monedas que hemos seleccionado. Luego haz clic en "Pagar" y luego haz clic en el botón "avanzado" en la ventana emergente que aparece.

![image](assets/39.png)

Siempre haz clic en "avanzado" en esta etapa para que podamos tener un control preciso y verificar exactamente qué hay en la transacción. Aquí está la transacción:

![image](assets/40.png)

Vemos dos ventanas internas blancas. La de arriba es la ventana de entradas (qué monedas se están gastando) y la de abajo es la de salidas (a dónde van las monedas).
Nota, el estado (arriba a la izquierda) es "no firmado" por ahora. El "Monto enviado" es 0 porque las monedas se están transfiriendo dentro de la billetera. La tarifa es de 481 sats. Ten en cuenta que si fuera 480 sats, el cero final se eliminaría, así: 0.0000048 y para el ojo cansado, esto puede parecer 48 sats, ten cuidado (algo que los desarrolladores de Electrum deberían solucionar).
El tamaño de la transacción se refiere al tamaño de los datos en bytes, no a la cantidad de bitcoin. El "reemplazo por tarifa" está activado de forma predeterminada y te permite reenviar la transacción con una tarifa más alta si es necesario. El LockTime te permite ajustar cuándo es válida la transacción, aún no he jugado con eso, pero aconsejo no usarlo a menos que entiendas completamente lo que estás haciendo y hayas practicado con pequeñas cantidades.

En la parte inferior, tenemos algunas herramientas de ajuste de tarifas de minería elegantes. Todo lo que necesitas hacer para transferencias internas es establecer la tarifa mínima de 1 sat/byte. Simplemente escribe manualmente el número en el campo de tarifa objetivo. Para verificar una tarifa adecuada para un pago externo, puedes consultar https://mempool.space para ver qué tan ocupado está el mempool y se muestran algunas tarifas sugeridas.

![image](assets/41.png)

He seleccionado 1 sat/byte.

En la ventana de entrada, vemos dos entradas. La primera es la donación de 5000 sats. Vemos a la izquierda su hash de transacción (que podemos buscar en la cadena de bloques). Junto a él, hay un "21", lo que indica que es la salida etiquetada como 21 en esa transacción (en realidad es la 22ª salida porque la primera está etiquetada como cero).

Algo a tener en cuenta aquí: las UTXO existen solo dentro de una transacción. Para gastar una UTXO, tenemos que hacer referencia a ella y poner esa referencia en la entrada de una nueva transacción. Las salidas luego se convierten en nuevas UTXO y la antigua UTXO se convierte en un STXO (gasto de salida de transacción).

La segunda línea es la donación de 10,000 sats. Tiene un "0" junto al hash de transacción del que proviene porque es la primera (y posiblemente única) salida de esa transacción.

En la ventana inferior, vemos nuestra dirección. Observa que el total de bitcoin de las entradas no coincide exactamente con el total de las salidas. La diferencia va al minero. El minero analiza la discrepancia en todas las transacciones en el bloque que está intentando minar y agrega ese número a su recompensa. (Las tarifas de minería de esta manera están totalmente desconectadas de la cadena de transacciones y comienzan una nueva vida).

Si ajustamos la tarifa de minería, el valor de salida cambiará automáticamente.

> Vale la pena señalar aquí: Observa el color de las direcciones en la ventana de transacción. Recuerda que las direcciones verdes están listadas en tu pestaña de direcciones. Si una dirección está resaltada en verde (o amarillo) en una ventana de transacción, entonces Electrum ha reconocido la dirección como propia. Si la dirección no tiene resaltado, entonces es una dirección externa (externa a la billetera abierta actualmente) y debes verificarla con especial cuidado.

Una vez que verifiques todo en la transacción y estés seguro de que estás satisfecho con las monedas que estás gastando y a dónde van las monedas, puedes hacer clic en "finalizar".

![image](assets/42.png)
Después de hacer clic en "finalizar", ya no puedes hacer ediciones. Si necesitas hacer cambios, debes cerrar esto y comenzar de nuevo. Observa que el botón "finalizar" ha cambiado a "exportar" y han aparecido nuevos botones: "guardar", "combinar", "firmar" y "transmitir". El botón "transmitir" está en gris porque la transacción no está firmada y, por lo tanto, no es válida en esta etapa.
Una vez que hagas clic en "firmar", si tienes una contraseña para la billetera, se te pedirá que la ingreses, y luego el estado (arriba a la derecha) cambiará de "No firmada" a "Firmada". Luego, el botón "Transmitir" estará disponible.

Después de transmitir, puedes cerrar la ventana de transacción. Si vas a la pestaña de direcciones, verás que la primera dirección está vacía y la segunda dirección tiene 1 UTXO.

Nota: Verás todos estos cambios incluso antes de que la transacción se haya minado en un bloque o se haya "confirmado". Esto se debe a que Electrum actualiza los saldos/transacciones en función no solo de los datos de la cadena de bloques, sino también de los datos del mempool. No todos los monederos hacen esto.

Algo importante a tener en cuenta es que, en lugar de transmitir, podemos guardar la transacción para más tarde. Se puede guardar tanto en los estados no firmados como en los firmados.

Haz clic en el botón "exportar" (paradójicamente, NO hagas clic en el botón "guardar") y verás varias opciones. La transacción está codificada con texto y, por lo tanto, se puede guardar de varias formas.

![image](assets/43.png)

Guardar en un código QR es muy interesante. Si eliges esto, aparecerá un código QR:

![image](assets/44.png)

Luego puedes tomar una foto del código QR. Hay varias cosas que puedes hacer con esto, pero por ahora, digamos que lo estás cargando de nuevo en la billetera más tarde. Puedes cerrar Electrum, cargar la billetera nuevamente e ir al menú Herramientas:

![image](assets/45.png)

Esto abrirá la cámara de tu computadora. Luego, muestras a la cámara la foto del código QR en tu teléfono y esto cargará la transacción nuevamente, exactamente como la dejaste.

No es intuitivo cómo cargar transacciones guardadas, así que presta especial atención. Cargar una transacción no es una "herramienta", pero la opción está oculta en el menú de herramientas (otra cosa que los desarrolladores de Electrum deberían solucionar).

Un proceso similar es posible con una transacción guardada como archivo. Prueba practicar con cualquiera de los métodos, dentro de la misma billetera. No lo explicaré aquí, pero puedes usar esta función para pasar una transacción entre la misma billetera en diferentes computadoras, entre billeteras de múltiples firmas y hacia y desde billeteras de hardware. Aquí tienes algunas instrucciones.

Ahora, volviendo al botón "guardar": esto no es cómo guardar el texto de la transacción. Lo que realmente hace es indicarle a la billetera Electrum que reconozca esta transacción en la computadora local como un pago enviado. Si lo haces por accidente, verás la transacción con un pequeño ícono de computadora. Puedes hacer clic derecho y eliminar la transacción, no te preocupes, no puedes eliminar bitcoins de esta manera. Electrum luego olvidará que esta transacción ocurrió y "reembolsará" los satoshis y mostrará los satoshis en la ubicación correcta donde realmente existen.

### Direcciones de cambio

Las direcciones de cambio son interesantes. Necesitas entender los UTXO para comprender esta explicación. Si estás gastando a una dirección una cantidad menor que el UTXO, entonces el bitcoin restante irá al minero a menos que se especifique una salida de cambio.
Podrías tener un UTXO de 6.15 bitcoins y querer gastar 0.15 bitcoins para donar a algunos manifestantes oprimidos por el tiránico gobierno "democrático" en algún lugar del mundo. Luego tomarías los 6.15 bitcoins (usando la función "gastar desde" en Electrum) y los pondrías en una transacción.

Pegarías la dirección de los manifestantes en el campo "pagar a", tal vez pondrías "EndTheFed & WEF" en el campo "descripción" y para la cantidad, pondrías 0.15 bitcoins y hacer clic en "pagar", luego en "avanzado".

En la pantalla de la transacción, en la ventana de entrada, verías el UTXO de 6.15 bitcoins. En la ventana de salida, verías una dirección que no tiene resaltado (esta es la dirección de los manifestantes) con 0.15 bitcoins junto a ella. También verías una dirección amarilla con ligeramente menos de 6.0 bitcoins. Esta es la dirección de cambio seleccionada automáticamente por la billetera de entre sus propias direcciones de cambio amarillas. El propósito de la dirección de cambio es que la billetera pueda poner monedas de cambio en ellas sin afectar la disponibilidad de las direcciones de recepción que puedas tener planes para, o facturas enviadas. Si van a ser utilizadas más tarde por clientes, por ejemplo, no quieres que tu billetera las use automáticamente y las llene. Es desordenado y malo para la privacidad.

Ten en cuenta que al ajustar la tarifa de minería, el monto de salida de cambio se ajustará automáticamente, no el monto de pago.

### Cambio manual o pago a muchos

Esta es una característica realmente interesante de Electrum. Puedes acceder a ella de la siguiente manera.

![imagen](assets/46.png)

Luego puedes ingresar múltiples destinos para el saldo UTXO que estás gastando, así:

![imagen](assets/47.png)

Pega la dirección, escribe una coma, luego un espacio, luego el monto, luego <enter>, y hazlo de nuevo. NO INGRESES MONTOS EN LAS VENTANAS "MONTO" - Electrum completará el total aquí a medida que escribas los montos individuales en la ventana "Pagar a".

Esto te permite determinar manualmente dónde va el cambio (por ejemplo, una dirección específica en tu billetera o en otra billetera), o puedes pagar a muchas personas a la vez. Si tu total no es suficientemente alto para igualar el tamaño del UTXO, Electrum aún creará una salida de cambio adicional para ti.

La función Pagar a Muchos también permite la posibilidad de crear tus propios "PayJoins" o "CoinJoins" - fuera del alcance de este artículo, pero tengo una guía aquí. (https://armantheparman.com/cj/)

## Billeteras

Quiero demostrar una Billetera de Solo Observación utilizando Electrum. Para hacer eso, primero necesito definir "billetera". Hay dos formas en que se usa "billetera" en Bitcoin:

- Tipo A, "billetera" - se refiere al software que muestra tus direcciones y saldos, como Electrum, Blue Wallet, Sparrow Wallet, etc.

- Tipo B, "billetera" - se refiere a la colección única de direcciones que están asociadas con la combinación de nuestra frase de semilla/frase de contraseña/ruta de derivación. Hay 8.6 mil millones de direcciones en cualquier billetera (4.3 mil millones de direcciones de recepción y 4.3 mil millones de direcciones de cambio). Si cambias algo en la frase de semilla, frase de contraseña o ruta de derivación, obtienes una billetera no utilizada con 8.6 mil millones de direcciones vacías nuevas y únicas.

Qué tipo se está refiriendo cuando se usa la palabra "billetera" es obvio en contexto.

## Billetera de Solo Observación - un ejercicio

No está completamente claro para qué sirve una billetera de observación, pero comenzaré explicando qué es, cómo hacer una práctica y luego volveremos a su propósito más adelante cuando explique más sobre las billeteras de hardware. (Para una revisión detallada de cómo usar una billetera de hardware y varias marcas específicas, vea aquí).

Vamos a hacer una billetera regular ficticia (esta vez agregando un poco más de complejidad con una frase de contraseña) y luego su correspondiente billetera de observación. Si quieres, puedes copiar exactamente la que hice o crear la tuya propia; esta billetera debe ser descartada, no la uses realmente. Comienza generando una semilla de 12 palabras usando el sitio web de Ian Coleman.

Observa las 12 palabras aleatorias en la captura de pantalla a continuación y que he ingresado una frase de contraseña en el campo de frase de contraseña:

FRASE DE CONTRASEÑA: "Craig Wright es un mentiroso y un estafador y debería estar en la cárcel. Además, Ross Ulbricht debería ser liberado de la prisión de inmediato".

La frase de contraseña puede tener hasta 100 caracteres y idealmente no debe ser ambigua ni demasiado corta. La que he usado es solo por diversión. Generalmente sugiero evitar letras mayúsculas y símbolos para reducir el estrés al intentar combinar si alguna vez tienes problemas para recordar tu frase de contraseña.

![image](assets/48.png)

A continuación, en Electrum, ve al menú archivo->nuevo/restaurar. Escribe un nombre único para crear una nueva billetera y haz clic en "siguiente".

![image](assets/49.png)

Los siguientes pasos ya deberías estar familiarizado con ellos, así que los enumeraré sin imágenes:

- Billetera estándar
- Ya tengo una semilla
- Copia y pega las 12 palabras en el cuadro o escríbelas manualmente.
- Haz clic en opciones y selecciona BIP39, y también marca la casilla de frase de contraseña ("extender esta semilla con palabras personalizadas").
- Ingresa tu frase de contraseña exactamente como lo hiciste en la página de Ian Coleman.
- Deja las opciones de script y ruta de derivación por defecto.
- No es necesario agregar una contraseña (bloquea la billetera).

Ahora regresa al sitio de Ian Coleman, baja a la sección "ruta de derivación" y haz clic en la pestaña "BIP 84" para seleccionar las mismas opciones de script que los valores predeterminados en Electrum (Segwit nativo).

![image](assets/50.png)

Las claves privadas y públicas extendidas están justo debajo y cambian cuando haces cambios en la ruta de derivación (o cualquier otra cosa en la página).

![image](assets/51.png)

También verás las claves privadas/públicas extendidas "BIP32" - por ahora, debes ignorarlas.

La clave privada extendida de la cuenta se puede utilizar para regenerar completamente tu billetera. Sin embargo, la clave pública extendida de la cuenta solo puede producir una versión limitada de la misma billetera (billetera de observación). Si colocas esta clave en Electrum, seguirá produciendo las 8.6 mil millones de direcciones que la semilla o la clave privada extendida tendrían, pero no habrá claves privadas disponibles para Electrum, por lo que no será posible gastar. Hagámoslo ahora para demostrarlo:

Copia la "clave pública extendida de la cuenta" en el portapapeles.

Luego ve a Electrum, deja abierta la billetera actual que creamos y ve a archivo->nuevo/restaurar. El proceso para crear la billetera es un poco diferente que antes:

- Billetera estándar
- Usar una clave maestra
- Pega la clave pública extendida en el cuadro y continúa
- No es necesario ingresar una frase de contraseña; ya es parte de la clave pública extendida
- No es necesario ingresar las opciones de script y ruta de derivación
- No es necesario agregar una contraseña (bloquea la billetera)
  Cuando se carga la billetera, deberías notar que se cargan exactamente las mismas direcciones que antes cuando se ingresó la semilla. También deberías notar en la parte superior de la barra de título que dice "observando billetera". Esta billetera puede mostrarte tus direcciones y saldos (verificando los saldos a través de un nodo), pero no puedes FIRMAR transacciones (porque la billetera de observación no tiene claves privadas).
  Entonces, ¿cuál es el punto de esto?

Una razón, y no la principal, es que potencialmente puedes observar tu billetera y su saldo en una computadora sin exponer tus claves privadas a ningún malware en la computadora.

Otra razón es que es REQUERIDO para realizar pagos si eliges mantener tus claves privadas fuera de la computadora; lo explicaré:

> Las billeteras de hardware (HWW) fueron creadas para que un dispositivo pueda mantener tus claves privadas de forma segura (bloqueadas con un PIN), nunca exponga las claves a una computadora (incluso cuando esté conectado a una computadora a través de un cable) y ellos mismos no puedan conectarse a Internet. Un dispositivo así no puede realizar transacciones por sí solo porque todas las transacciones de bitcoin comienzan haciendo referencia a una UTXO(s) en la cadena de bloques (que está en un nodo). Una billetera debe especificar en qué ID de transacción se encuentra la UTXO y cuál es la salida de la transacción que se va a gastar. Solo después de especificar la entrada se puede crear una nueva transacción en primer lugar, y mucho menos firmarla. Las billeteras de hardware no pueden crear transacciones porque no tienen acceso a ninguna UTXO, ¡no están conectadas a nada! Por lo general, se extrae una clave pública extendida del HWW y luego se muestran las direcciones en una computadora; muchas personas estarán familiarizadas con el software de Ledger o Trezor Suite que muestra direcciones y saldos en su computadora, esto es una billetera de observación. Estos programas pueden crear transacciones, pero no pueden firmar. Solo pueden tener transacciones firmadas por HWW que estén conectados a ellos. El HWW toma la transacción recién generada de la billetera de observación, la firma y luego la envía de vuelta a la computadora para su difusión a un nodo. El HWW no puede difundir por sí mismo, su billetera de observación asociada lo hace. De esta manera, las dos billeteras (billetera de clave pública en la computadora y billetera de clave privada en el HWW) cooperan para generar, firmar y difundir, todo asegurándose de que las claves privadas permanezcan aisladas y lejos de un dispositivo conectado a Internet.

## Transacciones de Bitcoin parcialmente firmadas (PSBTs)

Es posible crear una transacción y guardarla en un archivo, luego volver a cargarla, firmarla, guardarla y finalmente difundirla; no estoy diciendo que alguien necesite hacer esto, es solo algo que es posible.

Ahora considera una billetera multisignature de 3 de 5: 5 claves privadas crean una billetera y se necesitan 3 para firmar completamente una transacción (ver aquí para obtener más información sobre las claves de billetera multisignature). Es posible tener 5 computadoras diferentes, cada una con una de las cinco claves privadas.

La computadora uno podría generar una transacción y firmarla. Luego podría guardarla en un archivo y enviarla por correo electrónico a la computadora dos. La computadora dos puede luego firmarla y potencialmente guardar el archivo en un código QR y transmitir el código QR a través de una llamada de Zoom a la computadora tres al otro lado del mundo. La computadora tres puede capturar el código QR, cargar la transacción en Electrum y firmar la transacción. Después de las primeras 2 firmas, la transacción era una PSBT (transacción de bitcoin parcialmente firmada). Después de la tercera firma, la transacción se convirtió en completamente firmada y válida, lista para su difusión.
Para obtener más información sobre PSBTS, consulte esta guía. (https://armantheparman.com/psbt/)

## Uso de monederos de hardware con Electrum

Tengo una guía sobre el uso de monederos de hardware en general, que creo que sería importante que las personas que son nuevas en los monederos de hardware la lean. (https://armantheparman.com/using-hwws/)

También hay guías sobre varias marcas de monederos de hardware que se conectan a Sparrow Bitcoin Wallet que se encuentran aquí. (https://armantheparman.com/hwws/)

Esta será mi primera guía que muestra cómo usar un monedero de hardware con Electrum: voy a usar el monedero de hardware ColdCard como ejemplo. Esto no pretende ser una guía detallada sobre el ColdCard en particular, esa guía está aquí. Solo estoy mostrando puntos específicos de Electrum. (https://armantheparman.com/cc/)

### Conexión a través de la tarjeta micro SD (con aire)

Antes de conectar su monedero real a través del ColdCard, espero que haya pasado por los pasos anteriores de cargar una billetera simulada de Electrum y configurar los parámetros de red.

Luego, en el ColdCard, inserte la tarjeta SD. Supongo que ya ha creado su semilla. Si está accediendo a la billetera con una frase de contraseña, aplíquela ahora. Desplácese hacia abajo y seleccione el menú Avanzado/Herramientas –> Exportar Billetera –> Billetera Electrum.

Puede desplazarse hacia abajo y leer el mensaje. Siempre le ofrece seleccionar "1" para ingresar un número de cuenta distinto de cero (parte de la ruta de derivación), pero si siguió mi consejo, no ha modificado las rutas de derivación predeterminadas, por lo que no querrá un número de cuenta distinto de cero; simplemente presione la marca de verificación para continuar.

Luego seleccione la semántica del script. La mayoría de las personas seleccionarán "Segwit nativo".

Dirá "Archivo de billetera de Electrum escrito" y mostrará el nombre del archivo. Haga una nota mental de ello.

Luego saque la tarjeta micro SD y colóquela en la computadora con Electrum.

Algunos sistemas operativos abrirán automáticamente el explorador de archivos cuando inserte la microSD. Muchas personas verán el nuevo archivo de billetera y harán doble clic en él, y se preguntarán por qué no funciona. No es un gran diseño. En realidad, debe ignorar el explorador de archivos (cerrarlo) y abrir el archivo de billetera usando Electrum:

Abra Electrum. Si ya está abierto con otra billetera, seleccione archivo –> nuevo. Estamos buscando esta ventana:

![image](assets/52.png)

Aquí está el truco, no es intuitivo. Haga clic en "elegir". Luego navegue por el sistema de archivos en la tarjeta microSD y encuentre el archivo de billetera y ábralo.

Ahora ha abierto la billetera de seguimiento correspondiente a su monedero de hardware. Genial.

### Conexión a través del cable USB.

Esta forma debería ser más fácil, pero para las computadoras Linux, es mucho más difícil. Se necesita actualizar algo llamado "reglas Udev". Así es cómo (guía detallada https://armantheparman.com/gpg-articles/ ), y brevemente:

Es una buena idea asegurarse de que el sistema esté actualizado. Luego:

```
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

luego...

```
python3 -m pip install ckcc-protocol
```

Si obtiene un error, asegúrese de que pip esté instalado. Puede verificarlo con (pip –version) y puede instalarlo con (sudo apt install pythron3-pip)

Cree o modifique el archivo existente, /etc/udev/rules.d/

Así:

```
sudo nano /etc/udev/rules.d
```

Un editor de texto se abrirá. Copia el texto desde aquí y pégalo en el archivo rules.d, guarda y cierra.
![image](assets/53.png)

Luego ejecuta estos comandos uno tras otro:

```
sudo groupadd plugdev

sudo usermod -aG plugdev $(whoami)

sudo udevadm control –reload-rules && sudo udevadm trigger
```

Si recibes el mensaje "group plugdev" ya existe, está bien, continúa. Después del segundo comando, no recibirás ningún mensaje de confirmación, simplemente continúa con el tercer comando.

Es posible que necesites desconectar y luego volver a conectar el ColdCard a la computadora.

Si después de todo esto aún no puedes conectar el ColdCard, te recomendaría actualizar el firmware (pronto habrá una guía, pero por ahora puedes encontrar instrucciones en el sitio web del fabricante).

A continuación, crea una nueva billetera:

- Billetera estándar
- Usa un dispositivo de hardware
- Escaneará y detectará tu ColdCard. Continúa.
- Selecciona la semántica del script y la ruta de derivación
- Decide si el archivo de la billetera debe estar encriptado (recomendado)

### Transacciones usando el ColdCard

Con el cable conectado, las transacciones son fáciles. Firmar transacciones será sencillo.

Si utilizas el dispositivo de forma aislada, deberás pasar manualmente la transacción guardada entre dispositivos utilizando la tarjeta microSD. Hay algunos trucos.

Después de crear una transacción y finalizarla, debes hacer clic en el botón de exportar en la esquina inferior izquierda. Verás "guardar en archivo", lo cual es confuso, ya que en realidad debes ir a la última opción del menú que dice "para billeteras de hardware" y luego, dentro de esa selección, encontrar el otro "guardar en archivo" y seleccionarlo. Luego guarda el archivo en la microSD, saca la tarjeta y colócala en el ColdCard. Recuerda que es posible que necesites aplicar una frase de contraseña para seleccionar la billetera correcta. La pantalla mostrará "listo para firmar". Haz clic en la marca de verificación, inspecciona la transacción y procede confirmando con la marca de verificación. Una vez hecho esto, saca la tarjeta y vuelve a colocarla en la computadora.

Luego debemos abrir la transacción utilizando Electrum. La función está oculta en el menú Herramientas -> Cargar transacción. Navega por el sistema de archivos y encuentra el archivo. Habrá tres archivos cada vez que firmes. El archivo original guardado que hizo la Billetera de Vigilancia y dos archivos hechos por el ColdCard (no sé por qué hace esto). Uno dirá "firmado" y otro dirá "final". No es intuitivo, pero el que dice "firmado" no es útil, necesitamos abrir la transacción "final".

Una vez que cargues eso, puedes hacer clic en "transmitir" y se realizará el pago.

## Actualización de Electrum y el directorio oculto ".electrum"

Electrum se encuentra en dos lugares en tu computadora. Está la aplicación en sí y hay una carpeta de configuración oculta. Esa carpeta se encuentra en diferentes lugares según tu sistema operativo:

Windows:

> C:/Users/tu_nombre_de_usuario/AppData/Roaming/Electrum

Mac:

> /Users/tu_nombre_de_usuario/.electrum

Linux:

> /home/tu_nombre_de_usuario/.electrum

Ten en cuenta el "." antes de "electrum" en Linux y Mac, eso indica que el directorio está oculto. Además, ten en cuenta que este directorio solo se crea (automáticamente) una vez que ejecutas Electrum por primera vez. El directorio contiene el archivo de configuración de Electrum y también el directorio que contiene las billeteras que has guardado.
Si eliminas el programa Electrum de tu computadora, el directorio oculto permanecerá a menos que lo elimines activamente también.
Para actualizar Electrum, debes seguir el mismo procedimiento que describí al principio para descargar y verificar. Luego tendrás dos copias del programa en tu computadora y podrás ejecutar cualquiera de ellas: cada programa accederá a la misma carpeta oculta de Electrum para su configuración y acceso a la billetera. Todo lo que guardamos, como la unidad base, el nodo predeterminado al que conectarse, otras preferencias y el acceso a las billeteras, permanecerá porque todo eso se guarda en esa carpeta.

### Mover tu Electrum y billeteras a otra computadora

Para hacer esto, puedes copiar los archivos del programa en una unidad USB y también copiar el directorio .electrum. Luego, cópialos o muévelos a la nueva computadora. No necesitas verificar el programa nuevamente. Asegúrate de copiar el directorio .electrum en la ubicación predeterminada (recuerda copiarlo ANTES de ejecutar Electrum por primera vez en esa computadora, de lo contrario se creará una carpeta .electrum vacía por defecto y podrías confundirte).

## Etiquetas

Como expliqué anteriormente, en la pestaña de direcciones hay una columna de etiquetas. Puedes hacer doble clic allí e ingresar notas para ti mismo (solo en tu computadora, no es público ni está en la cadena de bloques).

![image](assets/54.png)

Cuando muevas tu billetera Electrum a otra computadora, es posible que no desees perder todas estas notas. Puedes hacer una copia de seguridad de ellas en un archivo utilizando el menú wallet–>labels–>export, y luego en la nueva computadora, usar wallet–>labels–>import.

## Consejos:

Si encuentras útil este recurso y te gustaría apoyar lo que hago por Bitcoin, puedes donar algunos sats aquí:

Dirección estática de Lightning: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/

---
name: My Node
description: Configura tu nodo Bitcoin MyNode
---

![imagen](assets/0.jpeg)

https://mynodebtc.com/

¡La forma más fácil y poderosa de ejecutar un nodo Bitcoin y Lightning! Combinamos el mejor software de código abierto con nuestra interfaz, gestión y soporte para que puedas usar Bitcoin y Lightning de manera fácil, privada y segura.

## Tipos de configuraciones de nodos

Existen varias configuraciones de nodos. MyNode es excelente. Viene con muchas aplicaciones y aún más si pagas por la versión premium. De lo contrario, sería muy tedioso descargar todas esas aplicaciones por tu cuenta. MyNode lo hace bastante fácil, como verás.

Otra opción alternativa y similar es RaspiBlitz. La interfaz gráfica no es tan buena y las aplicaciones se superponen mucho con las aplicaciones que vienen con MyNode, pero RaspiBlitz es software de código abierto gratuito (FOSS) y MyNode no lo es del todo. Otra diferencia es que MyNode se ejecuta en un contenedor Docker. Personalmente, encuentro Docker intimidante y difícil de solucionar problemas. Esto solo es un problema si te encuentras con errores o fallos. El desarrollador ofrece ayuda para los usuarios premium y también hay un grupo de chat en Telegram.

RaspiBlitz es simplemente la instalación de varios programas en Linux, sin Docker. El disco duro externo se puede conectar fácilmente a otra máquina Linux con Bitcoin Core, y listo, si es necesario.

Otra opción es simplemente instalar Bitcoin Core y una variedad de servidor Electrum (hay varios) en un sistema operativo. Tengo guías para Linux (Raspberry Pi), Mac y Windows.

## Lista de compras

- Raspberry Pi 4, 4 GB de memoria o 8 GB (4 GB es suficiente)

- Fuente de alimentación oficial de Raspberry Pi (¡Muy importante! No compres genéricas, en serio)

- Una carcasa para el Pi. La carcasa FLIRC es increíble. Toda la carcasa es un disipador de calor y no necesitas un ventilador, lo cual puede ser ruidoso.

- Tarjeta microSD de 16 GB (necesitas una, pero tener algunas a mano es útil)

- Un lector de tarjetas de memoria (la mayoría de las computadoras no tienen una ranura para tarjetas microSD).

- Disco duro externo SSD de 1 TB.  
  Nota: El SSD es crucial. No uses un disco duro externo portátil, aunque sea más barato.

- Un cable Ethernet (para conectarlo a tu enrutador doméstico)

- No necesitas un monitor

## Descargar la imagen de MyNode

Ve al enlace del sitio web de MyNode

![imagen](assets/1.jpeg)

Haz clic en <Descargar ahora>

Descarga la versión para Raspberry Pi 4:

![imagen](assets/2.jpeg)

Es un archivo grande:

![imagen](assets/3.jpeg)

Descarga los hashes SHA 256

![imagen](assets/4.jpeg)

Abre la terminal en Mac o Linux o el símbolo del sistema en Windows. Escribe:

```
Mac/Linux: “shasum -a 256 NOMBREDELARCHIVODESCARGADO”
Windows: “certUtil -hashfile NOMBREDELARCHIVODESCARGADO SHA256”
```

La computadora piensa durante unos 20 segundos. Luego, verifica que el hash del archivo de salida coincida con el descargado desde el sitio web en el paso anterior. Si es idéntico, puedes continuar.
Flashea la tarjeta SD

## Descarga e instala Balena Etcher. Enlace

No pude encontrar la firma digital para esto. Si sabes cómo, por favor avísame y actualizaré este artículo.
Etcher es fácil de usar. Inserta tu tarjeta micro SD y flashea el software de Raspberry Pi (archivo .img) en la tarjeta SD.

![image](assets/5.jpeg)
![image](assets/6.jpeg)
![image](assets/7.jpeg)
![image](assets/8.jpeg)
![image](assets/9.jpeg)
![image](assets/10.jpeg)
![image](assets/11.jpeg)

Una vez hecho esto, la unidad ya no es legible. Es posible que recibas un error del sistema operativo y la unidad desaparezca del escritorio. Retira la tarjeta.

## Configura el Pi e inserta la tarjeta SD

Las partes (la carcasa no se muestra):

![image](assets/12.jpeg)
![image](assets/13.jpeg)

Conecta el cable Ethernet y el conector USB del disco duro (aún no lo conectes a la corriente). Evita conectar a los puertos USB de color azul en el centro. Son USB 3. MyNode recomienda que uses el puerto USB 2, aunque el disco duro sea compatible con USB 3.

![image](assets/14.jpeg)

La tarjeta micro SD va aquí:

![image](assets/15.jpeg)

Finalmente, conecta la corriente:

![image](assets/16.jpeg)

## Encuentra la dirección IP del Pi

Nunca necesitas un monitor con MyNode. Sin embargo, necesitas otra computadora en la red doméstica. Si tu Pi no está conectado por Ethernet y quieres usar WiFi, encontrar la IP requiere habilidades informáticas de alto nivel. No puedo ayudarte, lo siento. Necesitas una conexión Ethernet. (El problema surge de la necesidad de acceder a un monitor y al sistema operativo para conectarse al WiFi e ingresar una contraseña).

Verifica tu enrutador para obtener una lista de todas las IP de todos los dispositivos conectados.

Escribí 192.168.0.1 en el navegador (instrucciones que vinieron con mi enrutador), inicié sesión y pude ver un dispositivo "MyNode" con la IP 192.168.0.18. Ten en cuenta que estas direcciones IP no son visibles públicamente en Internet (pasan primero por el enrutador), solo son identificadores para los dispositivos en tu red doméstica.

Encontrar la IP es crucial.

> ACTUALIZACIÓN: puedes usar la terminal en una máquina Mac o Linux para encontrar la dirección IP de todos los dispositivos conectados por Ethernet en la red doméstica usando el comando "arp -a". La salida no es tan bonita como lo que mostrará el enrutador, pero toda la información que necesitas está ahí. Si no está claro cuál es el Pi, realiza prueba y error.

## Accede al Pi por SSH

Tienes la opción de iniciar sesión en el dispositivo de forma remota mediante el comando SSH, pero no es necesario (sí lo es para RaspiBlitz Node). De todos modos, te mostraré cómo hacerlo, ya que es muy útil.

Abre una computadora Mac o Linux (para Windows, descarga putty, una herramienta SSH) y escribe:

```
ssh admin@192.168.0.18
```

Usa tu propia dirección IP. El nombre de usuario para el dispositivo MyNode es "admin" de forma predeterminada. La contraseña es "bolt" de forma predeterminada.

Si has usado tu Pi antes y has cambiado la tarjeta micro SD, obtendrás este error:

![image](assets/17.jpeg)

Lo que debes hacer es navegar hasta donde se encuentra el archivo "known_hosts" y eliminarlo. Es seguro hacerlo. El mensaje de error te muestra la ruta. Para mí fue /Usuarios/MiNombreDeUsuario/.ssh/'
No olvides el "." antes de ssh, esto indica que es un directorio oculto.
Luego intenta el comando ssh nuevamente.

Esta vez verás esta salida:

![image](assets/18.jpeg)

El archivo que eliminaste ha sido eliminado y estás agregando una nueva huella digital. Escribe "yes" y <enter>.

Se te pedirá que ingreses la contraseña. Es "bolt".

Ahora tienes acceso al terminal de MyNode Pi, sin un monitor, y puedes confirmar que todo se ha cargado correctamente.

![image](assets/19.jpeg)

## Acceso a través del navegador web

Abre un navegador. Debe ser una computadora en tu red doméstica, no puedes hacer esto desde fuera. Hay una forma, pero es difícil. No lo he probado.

Escribe la dirección IP en la ventana de dirección del navegador. Esto sucederá:

![image](assets/20.jpeg)

Ingresa la contraseña "bolt" - cámbiala más tarde.

Luego sucederá esto:

![image](assets/21.jpeg)

Elige "Format Drive"

![image](assets/22.jpeg)

Ahora esperamos.

En algún momento se te preguntará si deseas ingresar tu clave de producto o usar la versión gratuita "community edition" - Voy a mostrar la edición Premium. Recomiendo pagar por la versión premium si puedes permitírtelo, realmente vale la pena.

![image](assets/23.jpeg)

Luego verás el progreso de los bloques descargados. Esto lleva días:

![image](assets/24.jpeg)

Es seguro apagar la máquina durante la descarga si es necesario. Ve a configuración y encuentra el botón para apagar la máquina. No simplemente desconectes el cable, podrías corromper la instalación o el disco duro.

Asegúrate, al principio, de ir a "Configuración" y desactivar quicksync. Comenzará la descarga inicial de bloques desde el principio.

![image](assets/25.jpeg)

Quería continuar con la creación de la guía, así que aquí hay otro MyNode que preparé anteriormente. Esto es cómo se ve la página cuando el blockchain está sincronizado y se han habilitado y sincronizado varias "aplicaciones":

![image](assets/26.jpeg)

Ten en cuenta que el servidor Electrum también necesita sincronizarse, así que tan pronto como el blockchain de Bitcoin esté sincronizado, haz clic en el botón para iniciar ese proceso, lleva uno o dos días. Todo lo demás se habilita en pocos minutos una vez que lo seleccionas. Puedes hacer clic en cosas y explorar. No romperás nada. Si algo se rompe (esto me pasó a mí, pero creo que fue porque tenía piezas baratas), tendrás que volver a flashear y comenzar a descargar nuevamente. El problema que tengo con MyNode es que si necesitas "reflashear", debes volver a sincronizar el blockchain desde cero. Hay formas técnicas de solucionar esto, pero no es fácil.

Si también quieres probar otro nodo, como un RaspiBlitz, necesitarás un disco duro externo SSD adicional y otra tarjeta micro SD para flashear. De lo contrario, es el mismo equipo, simplemente no puedes ejecutar MyNode y RaspiBlitz simultáneamente, obviamente. Si quieres hacer eso, es hora de comprar otro Raspberry Pi.

Ahora que tienes un nodo en funcionamiento, úsalo, no lo dejes ahí sin hacer nada por ti. Sigue mi artículo (y video) sobre cómo conectar tu billetera de escritorio Electrum a Electrum Server y Bitcoin Core aquí.

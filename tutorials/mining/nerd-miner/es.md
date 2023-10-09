---
name: Nerdminer
description: Comienza a minar bitcoin con una probabilidad de ganar cercana a 0
---

![portada](assets/cover.jpeg)

> Configuración de tu NerdMiner_v2

En este tutorial, te guiaremos a través de los pasos necesarios para configurar un NerdMiner_v2, que es un hardware (un ESP-32 S3) dedicado a la minería de bitcoin.
Obviamente, la potencia de cálculo de un dispositivo como este no puede competir con los ASIC de los mineros aficionados o profesionales. Sin embargo, el NerdMiner es una herramienta educativa perfecta para hacer la minería de bitcoin más concreta. Y quién sabe, con (mucha mucha) suerte, tal vez encuentres un bloque y la recompensa que lo acompaña. Para los curiosos, veremos en la sección [Estimación de la probabilidad de ganancia](#estimacion-de-la-probabilidad-de-ganancia). En términos de consumo eléctrico, un NerdMiner consume 0.5W; para comparar, una lámpara LED consume en promedio 20 veces más.

Antes de revisar los diferentes pasos, enumeremos el hardware necesario para realizarlo:

- una [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- una [fuente de alimentación USB-C](https://amzn.eu/d/gIOot90)
- una carcasa 3D: si tienes una impresora 3D, puedes descargar el [archivo 3D](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons) o puedes comprar uno en la [tienda en línea de Silexperience](https://silexperience.company.site/NerdMiner_V2-p544379757).
- una PC con el navegador Chrome instalado
- una conexión a internet
- una dirección de bitcoin

También puedes comprar un kit NerdMiner ya ensamblado en varios distribuidores como:

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

En primer lugar, veremos cómo flashear el software en el ESP-32 S3, y luego veremos cómo reiniciarlo para cambiar la red wifi. Estos pasos están destinados a usuarios de Windows, si estás utilizando un sistema operativo Linux, realiza los [pasos preliminares](#pasos-preliminares-para-usuarios-de-linux) para permitir el reconocimiento del ESP-32 S3 por tu sistema.

# Instalación del software NerdMiner_v2

La instalación del software se simplifica en gran medida gracias al uso del webflasher.

## Paso 1: Preparación del webflasher

En primer lugar, debes ir al [flasher NM2 en línea](https://bitmaker-hub.github.io/diyflasher/).

Luego, selecciona el firmware correspondiente a tu ESP-32. La mayoría de las veces es el predeterminado: el T-Display S3. Luego haz clic en "Flash".

> ⚠️ Es importante que utilices el navegador Chrome, ya que este permite por defecto el uso de flash y el acceso a tus puertos USB.

![](assets/webflasher.png)

## Paso 2: Conexión del ESP-32

Una vez que se haya iniciado el webflasher, se abrirá una ventana emergente que muestra los diferentes puertos USB reconocidos por el navegador.
En ese momento, puedes conectar tu ESP-32 y se mostrará un nuevo puerto (en este caso, es el puerto ttyACM0). Debes seleccionarlo y hacer clic en "connect".

![](assets/flasher-port-serial.png)

El software se descargará en tu ESP32 en cuestión de segundos.

![](assets/NM2-sucessfully-installed.png)

## Paso 3: Configuración del NerdMiner

La configuración de tu NerdMiner se realizará a través de un teléfono inteligente o una computadora.
Activa el WiFi y conéctate a la red local NerdMinerAP. Si estás utilizando un teléfono inteligente, se abrirá automáticamente el portal de configuración; de lo contrario, ingresa la dirección 192.168.4.1 en un navegador.
Luego, selecciona "Configure WiFi".

Ahora podrás configurar tu Nerdminer.
En primer lugar, comienza conectándote a tu red WiFi, seleccionando el nombre de tu red y agregando la contraseña correspondiente.

Luego, puedes elegir el grupo de minería al que deseas unirte. De hecho, es común en la industria minera de Bitcoin compartir la potencia de cálculo para aumentar las posibilidades de encontrar un bloque a cambio de compartir la recompensa proporcional al hashrate proporcionado.
Para los NerdMiner, puedes elegir conectarte a uno de estos grupos:

| Pool URL          | Port  | URL                        | Estado                                                    |
| ----------------- | ----- | -------------------------- | --------------------------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Grupo de minería predeterminado, solo y de código abierto |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Mantenido por CHMEX                                       |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Mantenido por djerfy                                      |

Una vez que hayas elegido tu grupo, debes ingresar tu dirección de Bitcoin para poder recibir la recompensa en caso de encontrar un bloque (lo cual es excepcional).

También elige tu zona horaria para que el NerdMiner pueda mostrar correctamente la hora. Ahora puedes hacer clic en "save".

![](assets/wifi-configuration.jpg)

¡Felicitaciones, ahora eres parte de la red de minería de Bitcoin!

## Manipulación del NerdMiner

El software NerdMinerv2 tiene 3 pantallas diferentes, a las que puedes acceder haciendo clic en el botón en la parte superior derecha de la pantalla:

- La pantalla principal muestra las estadísticas de tu NerdMiner.
- La segunda pantalla muestra la hora, tu hashrate, el precio de Bitcoin y la altura del bloque.
- La tercera pantalla proporciona acceso a las estadísticas de la red mundial de minería de bitcoin.
  ![](assets/NM2-screens.png)

Si desea reiniciar su NerdMiner, por ejemplo, para cambiar la red WiFi, debe presionar el botón superior durante 5 segundos.

Si presiona una vez el botón inferior, apagará su NerdMiner. Hacer clic dos veces invertirá la orientación de la pantalla.

### Pasos preliminares para usuarios de Linux

Aquí están los pasos para que Chrome pueda detectar su puerto serie en Linux.

1. Identificar el puerto asociado:

- Conecte su ESP-32 a su computadora.
- Abra una terminal.
- Ingrese el siguiente comando para listar todos los puertos:
  - `dmesg | grep tty`
  - o `ls /dev/tty*`
- Para asegurarse del puerto, puede proceder por eliminación repitiendo el comando sin que el ESP-32 esté conectado.

2. Cambiar los permisos del puerto asociado:

- Por defecto, el acceso a los puertos serie puede requerir permisos de root, por lo que los haremos disponibles agregando su usuario al grupo `dialout`.
  - `sudo usermod -a -G dialout SU_NOMBRE_DE_USUARIO`, reemplace `SU_NOMBRE_DE_USUARIO` con su nombre de usuario.
  - luego cierre sesión y vuelva a iniciar sesión con este usuario, o reinicie el sistema para asegurarse de que los cambios de grupo surtan efecto.

Ahora que su ESP-32 es reconocido por su sistema, puede volver al [primer paso](#etape-1-preparation-du-webflasher) para instalar el software.

## Conclusión

¡Y eso es todo! Su NerdMiner_v2 ahora está configurado y listo para usar.

¡Buena minería y que la suerte esté de su lado!

### Estimación de la probabilidad de ganancia

Divirtámonos estimando la probabilidad de que podamos ganar la recompensa de un bloque. Esta estimación será aproximada y solo busca obtener el orden de magnitud de la probabilidad.
Supongamos que nuestro NerdMiner tiene una tasa de hash de aproximadamente 50kH/s y está conectado a la [pool pública por defecto](https://web.public-pool.io/#/) que tiene una tasa de hash total de aproximadamente 100 TH/s.

Dado que la tasa de hash total es de aproximadamente 450EH/s (es decir, $4.5 x 10^20$ hashes por segundo), podemos considerar que la probabilidad de que la pool de minería en solitario gane el próximo bloque es de 2 posibilidades entre 10 millones, es decir, aproximadamente 1 vez cada 5 millones de bloques, lo que puede suceder aproximadamente una vez por siglo. Y en tal eventualidad, un NerdMiner recibirá una parte de mil millonésima ($5 x 10^(-10)$) de la recompensa del bloque; es decir, 31.25 Msats para una recompensa de 6.25btc.
Las posibilidades de ganar son más que insignificantes, pero NerdMiner puede servirte, además de ser una herramienta educativa y objeto de curiosidad, como un boleto de lotería en la minería de bitcoins a un costo eléctrico mínimo de 0.5 W. Entonces, ¿por qué no intentar tu suerte?

### Información adicional

Aquí tienes algunos enlaces si deseas ampliar tu lectura sobre el tema:

- [Página del proyecto NerdMiner_v2](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Documentación completa de los NerdMiners](https://docs.bitwater.ch/nerd-miner-v2/)

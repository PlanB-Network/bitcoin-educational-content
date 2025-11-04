---
name: Canaan Avalon Mini 3
description: Configuración de un ASIC Avalon para la minería en solitario o en grupo.
---

![cover](assets/cover.webp)

En este tutorial, veremos cómo configurar el Canaan Avalon Mini 3, para facilitar la minería doméstica.

Hasta ahora, las máquinas ASIC (*Application Specific Integrated Circuit*) diseñadas específicamente para realizar una tarea determinada -en este caso, el cálculo Hash (SHA-256) para Miner de Bitcoin- eran especialmente inadecuadas para uso doméstico. Las molestias del ruido, el calor generado y la necesidad de adaptar la instalación eléctrica para soportar la enorme potencia de estos aparatos impedían a la mayoría de nosotros participar.

Hoy en día, Canaan, uno de los principales fabricantes de máquinas ASIC, ha decidido abordar el mercado de los particulares que desean minar en casa, ofreciendo una gama de productos relativamente silenciosos y muy fáciles de instalar (plug & play).

Estos dispositivos se comercializan como un calefactor auxiliar en el caso del **Avalon Nano 3S (140W)**, o como un mini radiador con una potencia de **800W** en el caso del **Avalon Mini 3**.

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Ten en cuenta que la diferencia de precio con los calentadores tradicionales de potencia equivalente no permite, en la inmensa mayoría de los casos, obtener un beneficio financiero. Los satoshis generados por la actividad de minería nunca compensarán esta diferencia de precio, a menos que tengas acceso a electricidad gratuita (excedente) o muy barata.

En nuestra opinión, estos dispositivos deberían verse más como una forma sencilla de minar en casa para aquellos que lo deseen por motivos personales: *obtener Satss sin KYC / jugar a la "lotería" solominando / participar en la descentralización Hashrate etc..*., mientras se benefician **como extra** del calor generado para calentar la habitación de uno en invierno. Pero no como una forma de ahorrar dinero en la mayoría de los casos al menos (países occidentales).

## Unboxing y características

### Avalon Nano 3S

En primer lugar, veamos qué hay dentro de la caja de Avalon Mini 3.

![image](assets/fr/24.webp)

Cuando abres la caja, las instrucciones de uso están justo delante de ti, pero lo más importante es que el módulo receptor WIFI está oculto bajo la pegatina blanca redonda a la izquierda de las instrucciones de uso. Lo necesitarás más adelante.

![image](assets/fr/25.webp)

Debajo del bloque de espuma está el aparato y, una vez sacado de la caja, la unidad de alimentación.

![image](assets/fr/26.webp)

![image](assets/fr/27.webp)

## Encendido y conexión a la red local

Una vez desembalado, coloca tu Avalon Mini 3 en una zona relativamente abierta, si es posible, para permitir que el calor circule correctamente. A continuación, empieza por insertar el pequeño módulo receptor WIFI en el puerto USB de la parte inferior del dispositivo, enchufa el cable de alimentación y asegúrate de que el botón de encendido está en la posición "1".

![image](assets/fr/28.webp)

Una vez completados estos pasos, la pantalla LED del dispositivo se ilumina y muestra el símbolo "Bluetooth", indicando que está listo para conectarse a la red local a través de la aplicación Avalon Family.

![image](assets/fr/29.webp)

![image](assets/fr/30.webp)

Para ello, ve a la tienda de aplicaciones de tu móvil, busca y descarga la aplicación **Avalon Family**.

![image](assets/fr/11.webp)

Una vez instalado, ábrelo pulsando en "Saltar" en la esquina superior derecha, después en el botón "Añadir" y por último en "Buscar". Asegúrate de tener activado Bluetooth en tu smartphone, para que la detección del dispositivo se realice sin problemas.

![image](assets/fr/12.webp)

Una vez que el dispositivo haya sido detectado por la aplicación, pulsa sobre él y elige "Conectar". A continuación, accederás a la pantalla donde podrás introducir los datos de tu conexión WIFI.

![image](assets/fr/13.webp)

Una vez conectado a tu red local, tu Mini 3 mostrará información como IP Address, hora, Hashrate y potencia eléctrica.

A continuación se ofrece una tabla resumen de las especificaciones técnicas generales del Mini 3:

| Caractéristica                                       | Valor                                                     |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consumo de electricidad                              | 800 W                                                     |
| Ruido                                                | 35-55 dB                                                  |
| Temperatura del aire de salida                       | 60-70°C (a temperatura ambiente 25°C)                     |
| Requisitos de temperatura ambiente para su uso       | -5° C - 40°C                                              |
| Rango de entrada del dispositivo                     | 110V-240V AC 50/60Hz                                      |
| Tamaño del dispositivo                               | Largo: 760 mm / Profundo: 104 mm / Alto: 214.5 mm         |
| Peso del dispositivo                                 |  8.35 kg                                                  |

## Conexión a un Mining pool

**Esta parte es igual en los dispositivos Nano 3s y Mini 3, ya que los procesos son estrictamente idénticos**

Tanto si queremos "solominar" como si queremos minar en "grupo", necesitaremos conectarnos a una Mining pool. De hecho, nuestro dispositivo no es más que un Hash-maker sin conocimiento de la red Bitcoin. Conectarlo a un pool le da acceso a la red Bitcoin, y le permite recibir plantillas de bloques sobre las que trabajar.

### Utilización de la aplicación para conectarse a una Mining pool

En la aplicación Avalon Family, selecciona el dispositivo como se muestra a continuación. A continuación, se te pedirá automáticamente que cambies la contraseña de administrador de la máquina. Pulsa en "Aceptar" si lo deseas, o en cancelar para dejar la contraseña de acceso por defecto "admin".

![image](assets/fr/16.webp)

A continuación, selecciona "Configuración", luego "Configuración de la piscina" e introduce los parámetros de las 3 pools solicitadas.

Los pools #2 y #3 actuarán como respaldos en el caso de que uno de ellos falle, para que tu Miner no funcione en vano. Por defecto, rl Hashrate apuntará al pool #1

En nuestro caso elegimos:
- 1 - Pool pública,
- 2 - CkPool,
- 3 - Ocean.

![image](assets/fr/17.webp)

Si deseas más información sobre cómo conectarse a una Mining pool, consulta estos tutoriales:

https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

En resumen, necesitamos

- La dirección del pool, normalmente **stratum+tcp://xxxxxxxx:puerto**.

- El nombre del "trabajador" compuesto por *tu dirección Bitcoin* y el *pseudo* que elijas para tu dispositivo, los 2 separados por un *punto*, por ejemplo:**bc1qxxxxxxxxxxx.MonAvalonNano3S**

- La contraseña, que suele ser siempre "**x**"

Una vez introducidos los datos del pool, haz clic en "Guardar".

![image](assets/fr/18.webp)

Reinicia el dispositivo siguiendo las instrucciones y espera unos minutos hasta que el Hashrate apunte a tu pool preferida (nº 1).

### Utilizar el navegador para conectarse a una Mining pool

También puedes conectarye a una Mining pool y, de forma más general, acceder a la interfaz de tu dispositivo a través de tu navegador favorito.

Para ello, escribe en la barra de búsqueda del navegador la IP Address del dispositivo que aparece en la pantalla de abajo, en nuestro ejemplo **192.168.144.6**

![image](assets/fr/15.webp)

Aparecerá la siguiente página, en la que se te pedirá que abras la aplicación Avalon Family y escanees el código QR que se muestra con la aplicación.

![image](assets/fr/20.webp)

Abre la aplicación, y pulsa en los 3 guiones de la parte superior derecha, y luego en escanear. Escanea el código QR del navegador, después introduce la contraseña de administrador de la aplicación y pulsa OK.

![image](assets/fr/21.webp)

Aquí estás en la página web que te permite interactuar con tu Avalon. Es más un panel de control para mostrar las métricas de la máquina que un medio para configurarla.

Pero todavía se puede acceder a la configuración del pool de esta manera, haciendo clic en **"Pool Config "** en la esquina inferior derecha.

![image](assets/fr/22.webp)

Al igual que en la aplicación móvil, aquí puede introducir los parámetros del pool.

![image](assets/fr/23.webp)

## Controla tu dispositivo a través de la app Avalon Family

Ya hemos conectado nuestro minero doméstico a nuestra red local y hemos apuntado nuestra Hashrate a pools de minería. Ahora vamos a descubrir las características esenciales de nuestra máquina a través de la aplicación Avalon Family.

En el menú principal de la aplicación Avalon Family, pulsa sobre el icono correspondiente al Avalon Mini 3. Accederás directamente al menú de gestión de los modos de funcionamiento.

hay 3 opciones disponibles: modo "Calefacción", modo "Mining" o modo "Noche".

- En el modo "Calentador" tienes 2 niveles de potencia "Eco" o "Super".

El nivel "Eco" corresponde a una potencia calorífica de 500 W para un Hashrate de unos 25 Th/s y 40 dB para el nivel sonoro.

El nivel "Super" corresponde a una potencia de salida de 650 W a unos 30Th/s y 45 dB. Este modo permite fijar una temperatura ambiente máxima por encima de la cual la unidad dejará de funcionar.

![image](assets/fr/36.webp)

- En el modo "Mining", la unidad funciona a máxima velocidad, sin la posibilidad de fijar una temperatura objetivo (aparte del límite de sobrecalentamiento incorporado, por supuesto). El objetivo es aprovechar al máximo las prestaciones del minero. Aquí, la potencia de salida se acerca a los 800 W a unos 37,5 Th/s y un nivel de ruido de 50-55 dB.

![image](assets/fr/37.webp)

Por último, en el modo "Noche", el Mini 3 funciona a la velocidad más baja posible con el mínimo ruido. 400 W, 20 Th/s y aproximadamente 33 dB.

Aquí también podrás establecer una temperatura objetivo por encima de la cual la unidad pasa al modo inactivo y deja de minar. Si la temperatura desciende, la unidad se reiniciará y reanudará el calentamiento y el minado. En este modo, los LED de la pantalla están apagados por defecto, pero puedes optar por encenderlos si es necesario para iluminar la habitación en la oscuridad, como una luz nocturna (véase la foto de abajo).

![image](assets/fr/38.webp)

![image](assets/fr/39.webp)

Por último, puedes jugar con los LED de tu Avalon a través del menú "Pantalla". Puedes elegir desplazarte por la información de funcionamiento relevante, elegir mostrar la hora o incluso una imagen personalizada (pixelada).

![image](assets/fr/40.webp)

![image](assets/fr/41.webp)

Al igual que en el Avalon Nano 3S, el menú "Ajustes" permite cambiar la contraseña del administrador, los ajustes del pool, comprobar la obstrucción del filtro (situado en la parte inferior del dispositivo), ponerse en contacto con el servicio de asistencia o ver los registros del dispositivo.

![image](assets/fr/42.webp)

Una vez más, el filtro de la parte inferior de la unidad puede limpiarse con una aspiradora, cuanto más regularmente mejor.

Hemos llegado al final de este tutorial, que nos ha enseñado cómo conectar nuestro Avalon Mini 3 a nuestra red local, cómo apuntar nuestro Hashrate a las pools de minado, y cómo navegar por las opciones y configuraciones utilizando la aplicación Avalon Family.

Para saber más, echa un vistazo a nuestro tutorial sobre la versión más pequeña del Avalon: el Nano 3S.

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

---
name: Canaan Avalon Nano 3S
description: Configuración de un ASIC Avalon para la minería en solitario o grupal
---

![cover](assets/cover.webp)

En este tutorial, vamos a echar un vistazo a cómo configurar el Canaan Avalon Nano 3S, para facilitar la minería en casa.

Hasta ahora, las máquinas ASIC (*Application Specific Integrated Circuit*) diseñadas específicamente para realizar una tarea determinada -en este caso, el cálculo Hash (SHA-256) para minería de Bitcoin- eran especialmente inadecuadas para uso doméstico. Las molestias del ruido, el calor generado y la necesidad de adaptar la instalación eléctrica para soportar la enorme potencia de estos aparatos impedían a la mayoría de nosotros participar.

Hoy en día, Canaan, uno de los principales fabricantes de máquinas ASIC, ha decidido abordar el mercado de los particulares que desean minar en casa, ofreciendo una gama de productos relativamente silenciosos y muy fáciles de instalar (plug & play).

Estos dispositivos se comercializan como un calefactor auxiliar en el caso del **Avalon Nano 3S (140W)**, o como un mini radiador con una potencia de **800W** en el caso del **Avalon Mini 3**.

https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Ten en cuenta que la diferencia de precio con los calefactores tradicionales de potencia equivalente no te permite, en la inmensa mayoría de los casos, obtener un beneficio económico. Los satoshis generados por la actividad de minería nunca compensarán esta diferencia de precio, a menos que tengas acceso a electricidad gratuita (excedente) o muy barata.

En nuestra opinión, estos dispositivos deberían verse más como una forma sencilla de minar en casa para aquellos que lo deseen por motivos personales: *obtener Sats sin KYC / jugar a la "lotería" solominando / participar en la descentralización del Hashrate etc..*., mientras se benefician **como extra** del calor generado para calentar una habitación en los meses fríos. Pero no como una forma de ahorrar dinero en la mayoría de los casos al menos (países occidentales).

## Unboxing y características

Primero, veamos qué hay dentro de la caja del Avalon Nano 3S.

![image](assets/fr/01.webp)

![image](assets/fr/02.webp)

Una vez abierta la caja, encontrarás una funda de cartón que contiene un receptor WIFI que, como veremos más adelante, deberás conectar al puerto USB del dispositivo para que pueda conectarse a tu red local. También se incluye el manual de instrucciones y un alfiler metálico para restablecer los valores de fábrica en caso necesario.

![image](assets/fr/03.webp)

![image](assets/fr/04.webp)

Una vez sacado todo de la caja, esto es lo que hay: la propia máquina, por supuesto, el manual de usuario, el receptor WIFI, la punta metálica antes mencionada y el cable de alimentación del dispositivo. La tarjeta de crédito suministrada no es digna de mención en nuestra opinión.

![image](assets/fr/05.webp)

A continuación encontrarás una tabla que resume las especificaciones técnicas generales del Nano 3S:

| Caractéristicas                                      | Valor                                                   |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Tasa de Hash                                         | 6 Th/s +- 5%                                            |
| Consumo de energía                                   | 140 W                                                   |
| Ruido                                                | 30 - 40 dB                                              |
| Temperatura del aire de salida                       | 60-70°C (a temperatura ambiente 25°C)                   |
| Requisitos de temperatura ambiente para su uso       | de -5 a 30°C                                            |
| Rango de entrada del dispositivo                     | 28V 5A continua                                         |
| Rango de entrada del adaptador                       | 110-240V AC 50/60Hz                                     |
| Tamaño del dispositivo                               | Largo: 205 mm /  alto: 115 mm / profundo:  58.5 mm      |
| Peso del dispositivo                                 | 0.86 kg                                                 |

## Encendido y conexión a la red local

Una vez desempaquetado, coloca tu Avalon Nano 3S si es posible en una zona relativamente abierta para permitir que circule el calor. A continuación, comienza por insertar el pequeño módulo receptor WIFI como se muestra a continuación:

![image](assets/fr/06.webp)

A continuación, conecta la entrada USB-C del cable al puerto USB-C del dispositivo para alimentarlo.
![image](assets/fr/07.webp)

![image](assets/fr/08.webp)

El dispositivo se iniciará y aparecerá el logotipo de Avalon Nano en la pantalla, seguido de un logotipo de "teléfono móvil" con las palabras "Please Configure the Network With Avalon Family App".

![image](assets/fr/09.webp)

![image](assets/fr/10.webp)

Para ello, ve a la tienda de aplicaciones de tu móvil, busca y descarga la aplicación **Avalon Family**.

![image](assets/fr/11.webp)

Una vez instalado, ábrelo pulsando en "Saltar" en la esquina superior derecha, después en el botón "Añadir" y por último en "Buscar". Asegúrate de tener activado Bluetooth en tu smartphone, para que la detección del dispositivo se realice sin problemas.

![image](assets/fr/12.webp)

Una vez que el dispositivo haya sido detectado por la aplicación, pulsa sobre él y elige "Conectar". A continuación, accederás a la pantalla donde podrás introducir los datos de tu conexión WIFI.

![image](assets/fr/13.webp)

Una vez que el dispositivo esté conectado a tu red local, la pantalla tendrá este aspecto:

![image](assets/fr/14.webp)

Muestra una Hashrate "ficticia", ya que aún no se ha configurado ningún pool, y la hora, fecha, potencia e IP Address del dispositivo - muy útil si quieres acceder a la Interface del dispositivo a través de un PC y un navegador (más sobre esto más adelante).

![image](assets/fr/15.webp)

## Conexión a un Mining pool

**Esta parte es común a los Nano 3s y Mini 3, ya que los procesos son estrictamente idénticos**.

Tanto si queremos "solominar" como minar "en grupo", vamos a tener que conectarnos a una Mining pool. De hecho, nuestro dispositivo no es más que un Hash-maker sin conocimiento de la red Bitcoin. Conectarlo a un pool le da acceso a la red Bitcoin, y le permite recibir plantillas de bloques sobre las que trabajar.

### Uso de la aplicación para conectarse a un Mining pool

En la aplicación Avalon Family, selecciona el dispositivo como se muestra a continuación. Después, se te pedirá automáticamente que cambies la contraseña de administrador del equipo. Pulsa en "Aceptar" si lo deseas, o en cancelar para dejar la contraseña de acceso por defecto "admin".

![image](assets/fr/16.webp)

A continuación, selecciona "Configuración", luego "Configuración del pool" e introduce los parámetros de las 3 pools solicitadas.

Las pools #2 y #3 actuarán como copias de seguridad en caso de que uno de ellos falle, para que tu minero no funcione en vano. Por defecto, el hashrate apuntará al pool #1

En nuestro caso elegimos:
- 1 - Pool pública,
- 2 - CkPool,
- 3 - Ocean.

![image](assets/fr/17.webp)

Para más detalles sobre cómo conectarse a un Mining pool, consulta estos tutoriales:

https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

En resumen, necesitamos:

- La dirección del pool, normalmente **stratum+tcp://xxxxxxxx:puerto**.

- El nombre del "trabajador" compuesto por *tu Bitcoin Address* y el *pseudo* que elijas para tu dispositivo, los 2 separados por un *punto*, por ejemplo:**bc1qxxxxxxxxxxx.MonAvalonNano3S**
- La contraseña, que suele ser siempre "**x**"

Una vez introducidos los datos del pool, haz clic en "Guardar".

![image](assets/fr/18.webp)

Reinicia el dispositivo siguiendo las instrucciones y espera unos minutos hasta que el Hashrate apunte a tu piscina preferida (nº 1).

### Utilizar el navegador para conectarse a una Mining pool

También puedes conectarte a una Mining pool y, de forma más general, acceder a la interfaz de tu dispositivo a través de tu navegador favorito.

Para ello, escribe en la barra de búsqueda del navegador la IP Address del dispositivo que aparece en la pantalla de abajo, en nuestro ejemplo **192.168.144.6**

![image](assets/fr/15.webp)

Aparecerá la siguiente página, en la que se te pedirá que abras la aplicación Avalon Family y escanees el código QR que se muestra con la aplicación.

![image](assets/fr/20.webp)

Abre la aplicación, y pulsa en los 3 guiones de la parte superior derecha, y luego en escanear. Escanea el código QR del navegador, después introduce la contraseña de administrador de la aplicación y pulsa OK.

![image](assets/fr/21.webp)

Aquí estás en la página web que te permite interactuar con tu Avalon. Es más un panel de control para mostrar las métricas de la máquina que un medio para configurarla.

Pero todavía se puede acceder a la configuración del pool de esta manera, haciendo clic en **"Pool Config "** en la esquina inferior derecha.

![image](assets/fr/22.webp)

Al igual que en la aplicación móvil, aquí puedes introducir los parámetros del pool.

![image](assets/fr/23.webp)

## Controla tu dispositivo a través de la app Avalon Family

Ya hemos conectado nuestro minero casero a nuestra red local, y hemos apuntado nuestra Hashrate a pools de minería. Ahora vamos a descubrir las características esenciales de nuestra máquina a través de la aplicación Avalon Family.

En la aplicación Avalon Family, haz clic en el icono correspondiente al Avalon Nano 3S.

se presentan 3 menús: "Modo de trabajo", "Control de la luz" y "Ajustes". En primer lugar, haz clic en "Modo de trabajo". Se te ofrecerán 3 modos de alimentación para tu máquina.

**Bajo**: proporciona unos 3 Th/s de Hashrate para un consumo de 70 W

**Media**: proporciona aproximadamente 4,5 Th/s de Hashrate para un consumo de 100 W

**Alto**: te proporcionará unos 6 Th/s de Hashrate con un consumo máximo de 140 W

![image](assets/fr/31.webp)

Demos un paso atrás y exploremos el menú "Control de luz". Es puramente cosmético. Dispone de toda una serie de opciones para variar el color, la intensidad, el calor, apagar los LED del dispositivo por la noche, etc... Es fácil descubrirlo por uno mismo.

![image](assets/fr/32.webp)

![image](assets/fr/33.webp)

![image](assets/fr/34.webp)

Finalmente, el último menú del que disponemos es el de "Configuración" que ya hemos visto para conectarnos a nuestras pools de minería. Aquí podremos gestionar nuestros pools, cambiar la contraseña de administrador del dispositivo y observar diversas métricas como la fecha de caducidad de la garantía, la limpieza de los filtros o cómo contactar con el soporte en caso de avería.

![image](assets/fr/35.webp)

Para el mantenimiento y para mantener el filtro lo más limpio posible, recomendamos utilizar un aspirador y aspirar regularmente las entradas y salidas de aire para evitar que se obstruyan.

Hemos llegado al final de este tutorial, que nos ha enseñado cómo conectar nuestro Avalon Nano 3S a nuestra red local, cómo apuntar nuestro Hashrate a los pools de minería de Bitcoin, y cómo navegar por las opciones y configuraciones utilizando la aplicación Avalon Family.

Para saber más, echa un vistazo a nuestro tutorial sobre la versión superior del Avalon: el Mini 3.

https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

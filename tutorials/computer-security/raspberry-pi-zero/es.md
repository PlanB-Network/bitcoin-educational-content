---
name: Raspberry Pi Zero
description: Cómo construir una computadora mínima, aislada y de bajo costo utilizando una Raspberry Pi Zero y un kit de accesorios.
---
![cover](assets/cover.webp)



Si llevas un tiempo en las páginas de Plan ₿ Network, ya habrás aprendido que una de las configuraciones de seguridad más recomendadas, casi una obligación, **es la gestión de fondos mediante el almacenamiento offline de tus claves privadas**.



Si aún no lo has descubierto, a lo largo de este tutorial encontrarás enlaces a recursos de código abierto con los que aprender más sobre él.



Para gestionar las claves privadas sin conexión, se necesita un dispositivo permanentemente desconectado de la red, ya sea un [monedero de hardware](https://planb.network/resources/glossary/hardware-wallet) o un ordenador con airgap, dedicado a esta función específica.



¿Cómo hacerlo si, por ejemplo, no se tiene la posibilidad de adquirir un hardware que realice únicamente esta tarea, pero no se quiere renunciar a este paso de seguridad?



## La solución


¿Y si le dijera que se puede fabricar un dispositivo offline en forma de ordenador con cámara de aire que tiene el tamaño y el peso de una memoria USB y cuesta 35 euros? ¿No se lo creería?



Continúe leyendo.



Le diré más: lea hasta el final. La solución propuesta es barata, pero no es precisamente la más fácil. Primero te haces una idea general, luego decides invertir parte de tu tiempo en una investigación personal y eliges, con la mayor tranquilidad posible, si proceder y cómo.



## Requisitos


**1** Una [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): la PI Zero (sin ningún sufijo) es la base para crear un ordenador de rendimiento mínimo, pero sobre todo carece de tarjetas Wi-Fi y Bluetooth, requisitos indispensables para el propósito de este ejercicio.





- Coste**: unos 15,00 en el momento de escribir este tutorial (agosto de 2025).
- Continuidad de la producción**: Raspberry garantiza la producción hasta enero de 2030.



PI Zero sin Wi-Fi ni Bluetooth, desgraciadamente prácticamente no están disponibles. Puede que encuentres más fácilmente las alternativas PI Zero W y PI Zero 2W. En este caso, puedes desactivar las funciones de conexión cambiando el archivo config. Después de instalar el sistema operativo, tendrás que añadir estos elementos al config:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



una sección de esta guía te mostrará cómo y dónde hacerlo. Sin embargo, si realmente quieres estar seguro, puedes encontrar varios tutoriales en la web para retirar el chip Wi-Fi con un cúter pequeño, de los adecuados para trabajar en placas electrónicas.



**2** Un _starter kit_ para Raspberry PI Zero: como es habitual en el mundo Raspberry, bare bones, sin carcasa externa. Además, los limitados recursos de una placa tan pequeña condicionan las posibilidades de conexión con el exterior.



Cuando decidí seguir adelante, encontré [este kit](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) lleno de accesorios, para aprovechar todo el potencial de la PI Zero. De hecho, el kit contiene un Supply de alimentación USB A -> micro USB, un pequeño concentrador USB, un adaptador mini-HDMI -> HDMI, un disipador térmico de cobre y una carcasa exterior de aluminio. El kit también incluye los tornillos y la llave Allen necesarios para colocar la PI Zero en la nueva carcasa.





- Coste**: 19.99 euros.



**3** Este tutorial no requiere que gastes grandes presupuestos en el ordenador del airgap. Debe saber, sin embargo, que necesitará un teclado y un ratón USB (estrictamente con cable, evite Bluetooth) y un monitor. Dependiendo de la entrada de su monitor, es posible que necesite un adaptador de mini-HDMI, la única salida disponible en la PI Zero. Por último, mira Hard por el hecho de que todos tenemos un teclado no inalámbrico y el ratón en la casa en alguna parte-es hora de Dust fuera de ellos.



## Presupuesto extra



**4** Puedes conseguir la Supply de alimentación original de Raspberry, que cuesta unos 15,00 euros.



**5** Personalmente opté por utilizar el Supply de alimentación suministrado en el _starter kit_, combinándolo, eso sí, con un cable USBA → miniUSB de los llamados `no data`, que cuesta 3,70 euros.



**6** Una tarjeta micro SD, para tener un mínimo de al menos 32 GB de almacenamiento masivo; si es de calidad/nivel industrial mejor.



**7** Necesitarás un sistema, un adaptador de USB a micro SD, como el que ves en la foto. El sistema operativo de tu PI Zero y su memoria funcionarán, de hecho, en ese soporte.



![img](assets/it/06.webp)



## Instalación del sistema operativo


Antes de cerrar tu PI Zero en el maletín, te recomiendo que instales el sistema operativo. Así podrás comprobar el LED que indica el funcionamiento, de buenas a primeras.



Para elegir y grabar el sistema operativo, opté por la forma más sencilla: utilizar la herramienta `PI Imager` de Raspberry.



![img](assets/it/01.webp)



Ve al [Github de Raspberry](https://github.com/raspberrypi/rpi-imager/releases) para descargar la última versión del Imager, eligiendo la más adecuada para tu sistema operativo (v. 1.9.6 en el momento de redactar). Notarás que, junto a cada recurso, también aparece el hash del archivo correspondiente. Nos servirá para la verificación.



![img](assets/it/02.webp)



Le recomiendo que verifique el sistema operativo que va a utilizar en su computadora airgap, para su propia tranquilidad personal. Esto le dará la confianza de que está operando con una versión legítima (no maliciosa) del Imager y, en consecuencia, Raspi OS.



Realice la verificación inmediatamente después de la descarga, con la máquina que utiliza normalmente conectada a Internet



A continuación, abra el terminal Linux y prepare la descarga, creando un directorio `raspios` útil para trabajar con él.



![img](assets/it/19.webp)



Descargue el Imager para su distribución Linux con `wget`.



![img](assets/it/20.webp)



Por último, ejecuta el comando file `sha256sum` y compara el Hash con el proporcionado por Raspberry en su Github.



![img](assets/it/21.webp)



O, si tiene Windows, abra Power Shell y escriba el siguiente comando:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Obtendrás el Hash que debe coincidir con el publicado en el Github de Raspberry.



Una vez verificada la descarga, puedes instalar Imager en tu ordenador de diario y abrirlo. Imager es la herramienta que necesitas para grabar el sistema operativo en la micro SD, que será el "disco de sistema" de PI Zero.



El proceso es extremadamente simple: primero elige el dispositivo Raspberry que vas a utilizar (así que presta atención a **tu modelo** de Raspi Zero), luego la versión del SO, y finalmente el punto de montaje de la tarjeta micro SD para flashear el SO.



### Primer paso



![img](assets/it/03.webp)



### Segundo paso



![img](assets/it/07.webp)



**Nota bien**: elige `PI OS 32-bit`, el único que funciona con PI Zero.



### Tercer paso



![img](assets/it/08.webp)



(Tenga mucho cuidado de dejar seleccionado _Excluir Unidad de Sistema_ para evitar que se le solicite instalar el sistema operativo de la Raspi en su computadora)



Cuando todo esté configurado, el Imager le preguntará si desea utilizar ajustes personalizados. Elija lo que desee o haga clic en _No_ para continuar con las opciones predeterminadas.



![img](assets/it/09.webp)



Confirme que desea borrar el contenido de la micro SD



![img](assets/it/10.webp)



El Imager comienza a flashear el sistema operativo a la micro SD, una barra de desplazamiento le notificará del progreso.



![img](assets/it/11.webp)



Al final hay verificación automática, te aconsejo que no la detengas.



![img](assets/it/12.webp)



Finalmente aparece un mensaje en la pantalla, y si todo ha ido bien, se parece a lo que se lee en la imagen.



![img](assets/it/13.webp)



Ahora puedes retirar realmente la micro SD del lector y colocarla en la ranura de la PI Zero. Enciende la pequeña Raspberry y observa el LED: esperamos que sea de color verde y que parpadee indicando la carga normal del sistema operativo, para luego permanecer encendido de forma continua. Si tienes otras indicaciones, por ejemplo si el LED parpadea con una frecuencia regular o es de color rojo, consulta las FAQ o [las páginas del foro de soporte](https://forums.raspberrypi.com/).



## Primera configuración


El primer arranque del Raspi OS es un poco más lento de lo habitual porque tiene que realizar una serie de tareas de instalación reales. Pero si todo ha ido bien, encontrará una pantalla de bienvenida.



![img](assets/it/14.webp)



Haga clic en _Siguiente_ para establecer la región geográfica, especialmente para cargar el teclado correcto. Preste especial atención a esto último.



![img](assets/it/15.webp)



Pulsa en _Siguiente_ y se te pedirá que crees tu usuario, anota tus credenciales y guárdalas bien.



![img](assets/it/16.webp)



El asistente te pide que elijas un navegador web por defecto, entre Chromium y Firefox; también puede preguntarte por la configuración de la red Wi-Fi si estás trabajando con una Zero W o 2W PI. Siga adelante y haga clic en _Skip_.



En algún momento se le pedirá que actualice el software de a bordo y el sistema operativo. Elija _Skip_: para los fines de este ejercicio estamos construyendo de hecho una máquina desconectada, que debe permanecer desconectada a partir de este momento.



Finalmente, puede pedirte que habilites `ssh`, pero rechaza este paso también, ya que es una IP Zero airgap.



![img](assets/it/17.webp)



No hay mucho más que configurar. Cuando haya terminado, reinicie la Raspberry para que los cambios surtan efecto.



![img](assets/it/18.webp)



## Un nuevo entrehierro informático


Después de reiniciar, su nuevo ordenador airgap está listo. PI Zero le muestra el nuevo escritorio, con el que puede trabajar a través de GUI o desde la línea de comandos.



![img](assets/it/22.webp)



### Primeros pasos para PI Cero W o 2W


Si estás trabajando con una Raspberry PI Zero serie W o 2W, tu placa tiene chips para Wi-Fi y Bluetooth a bordo. Durante la primera configuración te has saltado la configuración de la conexión, por lo que la PI Zero no está conectada a Internet. Ahora puedes desactivar los dos chips de forma permanente a través del software.



De hecho, Raspi OS proporciona un archivo `config.txt` que puede editar a su gusto. El `config` se encuentra en la partición `boot`, en el directorio `firmware`, y puede editarlo y guardarlo con privilegios de `root`.



Abre el terminal desde el icono de la parte superior izquierda y pasa a ser `root`.(1)



![img](assets/it/23.webp)



(1) Si Raspi OS no le hizo crear la contraseña `root` durante los pasos anteriores, le recomiendo que lo haga ahora, con el comando `passwd`. Tener al usuario `root` moviéndose independientemente de su usuario personal puede resultar muy conveniente en situaciones de recuperación.



Con el terminal, busca el archivo `config.txt` y prepárate para editarlo con el editor `nano`.



![img](assets/it/24.webp)



La edición debe hacerse en la parte inferior de todo el `config`, después de las palabras `[All]`. Es en este punto donde añadirá los comandos `dtoverlay` mostrados al principio del tutorial.



![img](assets/it/25.webp)



Guardar, cerrar y reiniciar. En el siguiente paso iremos a la exploración de la pequeña Raspberry.



## ¿Qué se puede esperar de este dispositivo?


Al observar las [especificaciones técnicas](https://www.raspberrypi.com/products/raspberry-pi-zero/) en el sitio de Raspberry, la PI Zero tiene un procesador BCM2835 de un solo núcleo y 512 MB de RAM, por lo tanto no se perfila como muy potente.



Dado que el terminal es más ligero, utilizaremos la línea de comandos para explorar las configuraciones del sistema.



Al encenderlo verás una breve pantalla con los colores del arco iris, seguida de un mensaje de bienvenida de Raspberry y, en la esquina inferior izquierda, mensajes del kernel relacionados con el arranque.



Cuando aparezca el escritorio de PI OS, abra el terminal y escriba:



```bash
uname -a
```


Este comando le mostrará la versión del kernel actualmente en uso en la pantalla, además de otra información.



![img](assets/it/26.webp)



También puedes ver información sobre la CPU y el hardware escribiendo:



```bash
lscpu
```



![img](assets/it/27.webp)



Y vea también `proc/mem/info`.



![img](assets/it/28.webp)



Para conocer la versión de Debian y el nombre en clave de la versión:



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Utilice


Aunque el rendimiento parece limitado (sobre el papel y en comparación con la potencia de las máquinas actuales), la PI Zero es eficaz, especialmente como terminal.





- Primero puedes ir a los menús principales e inspirarte en el panel _Add/Remove software_, donde encontrarás una serie de utilidades para programar y practicar. Recuerda que también puedes hacerlo desde el terminal, pero siempre con privilegios de `root`.



![img](assets/it/33.webp)





- Puedes "adoptar" este dispositivo offline para almacenar diversos documentos confidenciales, que permanecerán accesibles cuando los necesites, sin estar nunca expuestos a Internet.
- Puedes utilizar esta configuración para generate tus claves GPG de forma segura.
- Incluso podrías aprovechar este nuevo "juguetito" como un dispositivo de firma airgap, [siguiendo los consejos de Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Entre los Wallets que conozco, el único que proporciona una versión de 32 bits es Electrum. Bueno: la IP cero como lo preparamos en este tutorial le permitiría mantener las claves privadas fuera de línea la configuración para Wallet airgap que cubrimos en este tutorial:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Conclusiones


La configuración tiene, probablemente, una gran debilidad: la micro SD es un medio que podría dar problemas. Es vulnerable al uso intensivo; quizás ya tengas experiencia con esto, por usarla con tu teléfono. Después de instalar todo el software que querrás utilizar en la Zero airgap IP, haz una buena copia de seguridad de la preciada micro SD, utilizando la herramienta Raspi OS que tengas disponible.



![img](assets/it/34.webp)



A medida que tus necesidades crezcan, y con ellas tus posibilidades presupuestarias, puedes explorar otras soluciones Raspberry o similares. Hablando de memoria, por ejemplo, la PI 5 ofrece la posibilidad de montar una unidad M2 NVME, sin duda más robusta que la microSD.



No olvide tomar notas y documentar cada paso de la instalación del software de utilidad que va a utilizar fuera de línea. **tarde o temprano saldrá una actualización del SO Raspi** que definitivamente querrás aprovechar. En ese momento tendrás que borrar todo y hacerlo todo de nuevo (tal vez con una nueva micro SD 😂).



El ejercicio que acabamos de hacer, suponiendo que también sea tu primer experimento, lo recordarás durante mucho tiempo. No siempre es posible dedicar hardware a operaciones `embedded` offline, sin descuidar la atención a una máquina airgapped para encender y comprobar de vez en cuando.



Pero lo has conseguido, ¡enhorabuena! Y podrás sugerir esta solución a todos aquellos que necesiten mantener bajos sus presupuestos.
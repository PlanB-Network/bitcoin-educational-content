---
name: DietPi
description: Sistema operativo ligero optimizado para máquinas de bajo rendimiento. Con preferencia por el autoalojamiento
---

![cover](assets/cover.webp)



En círculos no técnicos, marcas como `Odroid`, `Raspberry Pi`, `Orange Pi` o `Radxa`, son poco conocidas. Pero basta con echar un vistazo en los círculos tecnológicos para descubrir que los ordenadores **SBC** -construidos sobre una única placa base, a menudo de tamaño microscópico en comparación con los ordenadores de uso común- se han convertido en indispensables como soporte para cualquier proyecto personal.



Se trata de ordenadores fabricados en una amplia variedad de modelos. Albergan preferentemente distribuciones Linux, a menudo adaptadas para funcionar sin problemas en estas máquinas poco potentes.



**DietPi no es una excepción**: es un sistema operativo basado en Debian, optimizado para ser lo más ligero posible y hacer que incluso el `SBC` de menor rendimiento sea muy rápido. Cambiado de Debian12 Bookworm a Debian13 Trixie justo cuando se estaba escribiendo este tutorial, ahora también soporta SBCs de código abierto basados en procesadores `RISC-V`. DietPi es un agradable descubrimiento que merece ser estudiado más a fondo.



## Puntos fuertes



No es el "duplicado habitual" de Debian para placas pequeñas tipo Raspberry. DietPi lo es:




- Optimizada para la velocidad y la ligereza**: una [comparación con otras distribuciones Debian para SBC](https://dietpi.com/blog/?p=888), DietPi es más ligera en todo. La imagen ISO de DietPi pesa menos de 1 GB, con diferencia la más pequeña entre las dedicadas a modelos más antiguos de Raspberry o Orange PI (por ejemplo). La demanda de recursos RAM y CPU es muy baja, por lo que siempre saca lo mejor de las placas, incluso de las más antiguas.
- Automatizaciones e instaladores integrados**: Un conjunto de comandos específicos ayuda a los usuarios a supervisar los recursos del sistema, así como a automatizar tareas para instalar y ejecutar programas, actualizar versiones, realizar copias de seguridad y comprobar todos los registros.
- Una comunidad fuerte y orientada a la experimentación**: los [tutoriales](https://dietpi.com/forum/c/community-tutorials/8) y proyectos de la comunidad DietPi, son ideales para inspirarse con software que puede instalar con un solo clic, gracias a DietPi.



**Exprimir hasta el último bit de su SBC nunca ha sido tan fácil**.



## Automatizaciones para el autoalojamiento


¿Quieres experimentar con tu propio servidor para ejecutar soluciones de red avanzadas, o herramientas para evolucionar tu experiencia en Bitcoin? DietPi puede ser la solución que estabas buscando. Aunque mucha gente sabe gestionar su propia infraestructura y ejecutar servidores perfectamente configurados y protegidos, DietPi es un paso adecuado para aquellos que quieren empezar desde cero.



En lugar de realizar manualmente todas las complejas tareas que una tarea así requiere, DietPi te permite construirlas con un `wizard` y su propia línea de comandos. Aquí puedes experimentar con tu propia nube personal, gestión de dispositivos _smart home_, copias de seguridad automatizadas y crontab, así como soluciones más avanzadas.



![img](assets/en/01.webp)



## Instalación



### Descargar



DietPi ofrece un innumerable conjunto de imágenes ISO, para grabar el sistema operativo en muchos dispositivos diferentes. Algunas sólo son compatibles: la ISO para Raspberry PI5 aún está en pruebas, por ejemplo, pero seguro que puedes encontrar la adecuada para tu placa.



Para esta guía elegí instalarlo en un cliente ligero, por lo que la elección fue a _PC/VM_ y luego a _Native PC_. Hay dos imágenes ISO para estos dispositivos, que difieren en la generación del gestor de arranque. La máquina utilizada en el tutorial es bastante antigua, por lo que la elección recayó en la versión _BIOS/CSM_. Si tienes una máquina más nueva, la versión correcta podría ser la `UEFI`.



![img](assets/en/02.webp)



Llegará a la página que contiene la `imagen del instalador`, el `sha256` y las `Firmas`.



![img](assets/en/03.webp)



Prepara un directorio en el `home` de tu ordenador de diario, para poder descargar los archivos necesarios, con `wget`.



![img](assets/en/04.webp)



La clave pública del desarrollador requirió un mínimo de investigación, pero puedes encontrarla en este enlace: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Compruebe el contenido del directorio con `ls -la` e importe la clave MichaIng a su llavero, con `gpg --import`.



### Verificación y flash



Por último, la parte que más recomiendo: asegúrate de la autenticidad del sistema operativo que has descargado y que vas a instalar en tu SBC.



![img](assets/en/06.webp)



Si también obtuviste el resultado `Good signature` y el mismo control Hash con el comando sha256sum, puedes proceder a flashear la ISO a una memoria USB. Usa aplicaciones como Whale Etcher para hacer esto.



![img](assets/en/07.webp)



## Instalación de DietPi



![img](assets/en/09.webp)



Transfiera la unidad flash al dispositivo que alojará DietPi y comience la instalación del sistema operativo Green de cal. En este ejercicio estamos utilizando un cliente ligero con 16 GB de RAM, un SSD de 128 GB para el sistema operativo y un segundo disco de datos de 1 TB. La instalación llevó menos de 30 minutos, pero si vas a utilizar una Raspberry, por ejemplo, los recursos pueden ser menores y llevar más tiempo. Se te mostrará el progreso durante la instalación.



![img](assets/en/08.webp)



Siendo diseñado para Raspberries y similares, la verdadera naturaleza de DietPi es la llamada instalación `headless`, sin entorno gráfico y con acceso nativo `shsh'. En la guía, en cambio, verás un entorno gráfico, LXDE para ser precisos.



Durante este paso también se le pedirá que decida qué navegador web desea utilizar por defecto, entre Chromium y Firefox. Ambos funcionan bien; no hay contraindicaciones particulares para ninguno de ellos, salvo tu preferencia personal.



Hacia el final, el instalador puede preguntarte si quieres instalar algún programa ya, pero aquí **te aconsejo que no precargues nada**. Debes saber que después de este paso, se te pedirá que cambies las contraseñas por defecto de los dos usuarios, por razones de seguridad. Lo más importante es que se te pedirá **establecer la `Contraseña Global de Software (GSP)`**, que asegurará el acceso a los distintos software de forma controlada. **Si descarga cualquier software durante la instalación del sistema operativo, sin la `Contraseña Global de Software` establecida, permanecerá virtualmente inaccesible**. Tendrás que desinstalarlos y volverlos a instalar después de establecer la `Contraseña Global de Software`: por lo tanto, **no pongas nada para evitar el doble trabajo**. (El inconveniente es probable, no 100% seguro).



La instalación termina con una solicitud para activar DietPi-Survey, un servicio automatizado de recogida de datos que se utiliza para apoyar el desarrollo del sistema operativo. Según el sitio web, la recogida de datos se activa al descargar cualquiera de los programas de la automatización proporcionada por DietPi, o al actualizar a la siguiente versión. Todo el mundo tiene la opción de participar (_Opt IN_) o no participar (_Opt OUT_).



![img](assets/en/23.webp)



Una vez completada la instalación y el subsiguiente reinicio, DietPi aparece en la pantalla tal y como lo configuraste. Para el tutorial, como mencioné, elegí el entorno gráfico `LXDE`. En el escritorio encontré el acceso directo para iniciar `htop` y la terminal abierta.



![img](assets/en/10.webp)



### "Herramientas" del sistema operativo



Olvídate de la mayoría de los programas que utilizas en tu distribución de Linux-DietPi está tan optimizado, que ha dejado fuera bastantes. Básicamente tendrías que instalar un montón de comandos manualmente, pero si sólo estás probando, resiste la tentación e intenta poner a prueba las automatizaciones de DietPi.



Sin duda, el terminal es la primera herramienta útil para empezar a utilizar tu nuevo sistema operativo, y se abre automáticamente cada vez que lo enciendes.



![img](assets/en/11.webp)



En la pantalla del terminal, encontrará listados una serie de comandos precedidos por `dietpi-` que representan las [herramientas](https://dietpi.com/docs/dietpi_tools/) de este sistema operativo:




- `dietpi-launcher`: para acceder al sistema operativo, al gestor de archivos, etc
- `dietpi-Software`: que representa la herramienta con la que puede instalar todo el software ya disponible en la suite
- `dietpi-config`: para acceder a las configuraciones del sistema, incluso a las más avanzadas.



![img](assets/en/14.webp)



### Copia de seguridad



Hacer una copia de seguridad de un servidor es una rutina que el administrador del sistema debe prever desde la primera puesta en marcha.



Con DietPi existe el comando `dietpi-Backup`, que recomiendo explorar para encontrar la solución ideal: permite configurar una copia de seguridad periódica, incremental o no en función de las aplicaciones utilizadas, y todas las opciones para personalizar la rutina.



![img](assets/en/22.webp)



Seleccione el destino de la copia de seguridad, por ejemplo otro disco, iniciando `dietpi-Drive_Manager` para montar la unidad de destino y utilizarla para esta función.



## Configuración



El autoalojamiento es una experiencia recomendable para todos, ya sean curiosos o simples entusiastas. Sin embargo, poner en marcha y configurar un servidor implica algunos retos tecnológicos nada desdeñables. Aquí es donde entra en juego **la sencillez de DietPi**, que te permite configurar un sistema a tu medida en unos sencillos pasos.



![img](assets/en/24.webp)



Ajustes básicos y avanzados, todo al alcance de tu mano en el único Interface disponible con el mando:



``dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-software


```
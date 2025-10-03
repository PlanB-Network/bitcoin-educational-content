---
name: Braiins Mini Miner
description: Hacer Mining fácilmente desde casa.
---
![cover](assets/cover.webp)



### Introducción



El Mini Miner braiins BMM 100 es un producto creado por Mining pool Braiins. Este dispositivo tiene un diseño atractivo y es extremadamente silencioso. Produce 1,1 Th/s de potencia de cálculo y consume unos 40 vatios. A diferencia de otros dispositivos, no es de código abierto, pero es realmente fácil de instalar, ¡realmente sólo se necesitan unos pocos clics! El Mini Miner BMM 100 es la primera versión que salió al mercado. Ahora está en producción la versión 2, llamada BMM 101, que se diferencia de la primera por tener una pantalla más grande y la presencia de Wi-Fi, pero los procedimientos de instalación son los mismos.



También puede encontrar mucha más información importante consultando la guía completa directamente en [sitio del fabricante](https://braiins.com/hardware/mini-Miner-bmm-100).



### Visión general de BMM 100



el dispositivo parece un paralelepípedo con una pantalla en la parte delantera



![image](assets/en/01.webp)



un ventilador en la parte superior



![image](assets/en/02.webp)



mientras que en la parte trasera tenemos: el agujero para la alimentación, espacio para una tarjeta SD (que puede ser necesaria para cualquier actualización), un pequeño botón que dice `IP REPORT` que permite conocer la IP Address del mini Miner, que Address es necesaria para acceder al dashboard del dispositivo. Una vez pulsado el botón, se muestra la IP Address durante unos 5 segundos, luego desaparece y vuelve a aparecer la pantalla de configuración. Sin embargo, si necesita cambiar alguna configuración, basta con volver a pulsar el botón en cuestión y la IP Address reaparecerá en la pantalla. Siguiendo con la lista nos encontramos con un puerto Ethernet y un acceso para realizar un reset del dispositivo, para lo cual tendrás que coger un pin y mantenerlo pulsado durante 10 segundos con el fin de resetear todos los ajustes de la mini Miner. Finalmente encontramos dos luces indicadoras, una Green y otra roja, que nos indican el estado del Miner.



![image](assets/en/03.webp)



### Conexión del Mini Miner



Será necesario conectar el dispositivo a internet vía ethernet, tenga en cuenta que con la nueva versión (BMM 101) esto ya no es necesario. Volviendo a este mini Miner, una vez localizada la ubicación tendremos que conectarlo primero a la línea de internet y después a la corriente: el dispositivo se encenderá automáticamente y mostrará su IP Address en la pantalla.



### Configuración



Tenemos que abrir un navegador e introducir la IP Address que nos muestra el mini Miner en la barra de búsqueda. Os recuerdo que para encontrar el dispositivo en la red tendrá que ser local, por lo que tendréis que tener el ordenador que estéis utilizando conectado a la misma red que el mini Miner. una vez introducida la IP Address pulsamos enter y nos aparecerá en pantalla la página de login al sistema operativo del mini Miner, que es Braiins OS.



![image](assets/en/06.webp)



Para iniciar sesión tendrás que introducir `root` como nombre de usuario, mientras que puedes dejar la contraseña en blanco. Haz clic en iniciar sesión y aparecerá tu mini panel de Miner.



![image](assets/en/07.webp)



### Configuración general



Vamos a Sistema



![image](assets/en/24.webp)



dentro de los ajustes encontramos algunos ajustes generales como el tema (claro u oscuro), el idioma, la zona horaria y el cambio de contraseña.



![image](assets/en/25.webp)



Si vamos a "Pantalla Mini Miner" en su lugar tenemos la configuración de nuestra mini Miner, como la visualización de la pantalla. Podemos elegir si mostrar la hora, o el precio de Bitcoin, o la pantalla con la información del estado de la máquina como el producto Hash, la temperatura, los vatios consumidos, etc. Aquí depende de usted para elegir lo que quiere ver en la pantalla, también podemos cambiar el brillo de la pantalla, establecer el modo nocturno, y mostrar la hora con formato de 12 o 24 horas.



![image](assets/en/26.webp)



Una vez realizados los cambios, haz clic en `Guardar cambios` y verás los cambios en la pantalla de tu dispositivo



![image](assets/en/27.webp)



### Conexión con Mining pool



Ahora todavía no estamos operativos, porque tenemos que conectarnos a un pool para poder arrancar Mining, así que tenemos que ir a "Configuración"



![image](assets/en/08.webp)



y la primera entrada es simplemente `Pools`.



![image](assets/en/09.webp)



Aquí tendremos que decidir qué piscina utilizar. En este tutorial os mostraré dos opciones. La primera es conectarnos a Mining pool Braiins que también es utilizado por mineros profesionales, como puedes ver en este tutorial:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

La segunda opción es conectarnos a un Mining pool que mina en solitario, como Public Pool, sigue esta guía para hacerlo:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

#### Piscina Braiins



Para conectarnos a este pool necesitamos crear una cuenta. Este pool también realiza pagos utilizando Lightning Network, por lo que podremos recibir unos cuantos Sats al día. Para ello necesitamos crear un rayo Address en el que recibir las recompensas. Si no sabes cómo crear una cuenta en braiins pool o cómo configurar tu Address lightning puedes seguir esta guía:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Una vez hecho esto nos encontramos en el dashboard del pool de Braiins. Lo que tenemos que hacer es decirle al pool que queremos conectarnos con uno de nuestros Mineros, para ello en la parte izquierda de la pantalla encontraremos una serie de entradas. Tenemos que ir a "trabajadores"



![image](assets/en/04.webp)



y tenemos que hacer clic en el botón morado de la derecha que dice "Conectar trabajadores"



![image](assets/en/05.webp)



Aquí viene la ventana con la información que necesitamos para conectar nuestro mini Miner al pool. Aquí el único cambio que podemos hacer es elegir Stratum V2. Para saber qué es Stratum v2 consulta esta entrada en el [glosario](https://planb.network/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Ahora tenemos que copiar esta cadena que empieza por stratumv2. Así que hacemos click en el simbolito de "copiar", luego vamos al dashboard de nuestro mini Miner que habíamos dejado en configuración y pools. Pinchamos en añadir nuevo pool



![image](assets/en/11.webp)



y pegar la cadena que hemos copiado en el espacio debajo de Pool URL.



![image](assets/en/12.webp)



Ahora tenemos que añadir el nombre de usuario y la contraseña. Volvamos al dashboad del pool. Debajo también tenemos un userID y una contraseña. El userID y nuestro username, el que dimos al crear la cuenta, más el nombre del Miner que queremos poner. puedes decidir si poner o no un nombre al dispositivo que estás conectando al pool, es opcional, pero es recomendable ponerlo, así si conectas varios dispositivos será más fácil identificarlos enseguida. Si no quieres poner nada en su lugar puedes dejar `workerName`.



![image](assets/en/13.webp)



Luego vamos a nuestro miniminer Miner e introducimos el nombre de usuario. Aquí introduciremos en mi caso "finalstepbitcoin" que es mi userID, miniminer punto. Este es el nombre que decidí darle al dispositivo. Si no quieres ponerle nombre simplemente escribe userid punto workername. En mi caso sería finalstepbitcoin.nombretrabajo. Una vez introducido el nombre de usuario puedes elegir una contraseña y escribirla en el campo en blanco. También puedes poner anithing123, que es la que también aparece en la pantalla del pool, pero simplemente quiere indicarte que puedes poner la contraseña que quieras.



Una vez introducidos todos los datos hay que pulsar el botón de guardar de la derecha (el que tiene forma de disquete) y de esta forma habremos configurado los datos del pool en el mini Miner.



![image](assets/en/14.webp)



Ahora tienes que volver al panel de la piscina y hacer clic en "¡Conectado! Volver atrás"



![image](assets/en/15.webp)



¡Hemos conectado nuestro mini Miner al pool de braiins! Ahora puedes verlo en la lista de trabajadores. Si no aparece haz un refresh y espera unos instantes. Una vez que aparezca, comprueba que tiene el estado "OK" con una marca de verificación Green.



![image](assets/en/17.webp)



si volvemos al dashboard deberíamos empezar a ver movimiento en el gráfico y ver el Hashrate de nuestro dispositivo. Esto significa que la piscina está recibiendo nuestro trabajo y por lo tanto estamos a todos los efectos socavar.



![image](assets/en/16.webp)



#### Piscina pública



A través de este pool uno puede probar suerte y minar en solitario, apoyándose en un pool. En este caso no recibiremos recompensa, pero sí la recompensa completa si alguna vez conseguimos minar un bloque. A continuación enlazaremos con el pool público, un pool exclusivo para Mining que es completamente de código abierto. Abrimos una nueva ventana en el navegador y vamos a [web.public-pool.io](https://web.public-pool.io/#/).



![image](assets/en/18.webp)



aparece una página con toda la información que necesitamos. A continuación, copiamos allí el estrato Address



![image](assets/en/19.webp)



luego volvemos al dashboard de nuestra mini Miner, vamos a configuración y a pools, pinchamos en añadir nuevo pool (mismo proceso que visto anteriormente) y pegamos el 'stratum Address bajo pool url.



![image](assets/en/20.webp)



Ahora volvamos a la página del pool y veamos que como nombre de usuario tenemos que introducir un Bitcoin Address, que será con el que recibiremos la recompensa en caso de que socavemos un bloqueo, luego un punto y después el nombre de nuestro dispositivo, como hicimos anteriormente con Braiins Pool, mientras que la contraseña la podemos elegir nosotros mismos.



![image](assets/en/21.webp)



Volvemos al mini Miner y en nombre de usuario pegamos un Address Bitcoin seguido de punto y el nombre, yo pondré `miniminer`. En la contraseña en su lugar pondré test, vosotros ponéis lo que queráis.



![image](assets/en/22.webp)



Ahora guardamos la configuración y desactivamos la piscina Braiins.



![image](assets/en/23.webp)



¡Bien! ¡Ahora somos Mining en la piscina pública!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)
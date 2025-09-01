---
name: Pi-Hole
description: Un bloqueador de anuncios para toda la red
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Florian Duchemin publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es posible que se hayan realizado cambios en el texto original.*



___



## I. Presentación



Todos lo hemos hecho nada más arrancar nuestro navegador favorito: instalar un **adblocker** (bloqueador de anuncios). Sin embargo, cuando usamos el navegador de la tele o un dispositivo Android, etc... Es un poco más complicado encontrar algo que funcione. Y si hay más de un dispositivo en casa, ¡pues hay que repetir la operación para cada navegador!



En este tutorial, vamos a resolver un problema sencillo**: proporcionar un bloqueador de anuncios a todas las máquinas de nuestra red y gestionarlo de forma centralizada.**



Para ello, utilizaremos una herramienta desarrollada a tal efecto: **Pi-Hole**



Pi-Hole es un sumidero DNS. Utilizará las peticiones DNS realizadas por tus dispositivos para validar o denegar el tráfico, protegiéndote así de direcciones y dominios conocidos por distribuir publicidad, malware, etc.



DNS significa Sistema de Nombres de Dominio. ¿Qué es un nombre de dominio? Bueno, "it-connect.fr" es sólo un ejemplo. Un nombre de dominio es un identificador único para uno o más recursos, generalmente administrados por una única entidad.



El nombre de la máquina más el nombre del dominio se denomina FQDN (Fully Qualified Domain Name). Permite acceder a una máquina concreta simplemente "llamándola". Por ejemplo, cuando escribes "www.trucmachin.com", en realidad estás llamando a la máquina "www", que pertenece al dominio "trucmachin.com".



Excepto que nuestros ordenadores no entienden el lenguaje humano, todo lo que entienden es binario, por lo que necesitan una IP Address, que es el equivalente a un número de teléfono, para llegar al sitio web.



Así, cada vez que introduce el nombre de un sitio web en su navegador o pulsa sobre un enlace, su ordenador pregunta primero a un servidor DNS por la IP Address correspondiente a ese nombre.



**Pi-Hole inspeccionará estas peticiones (¡hay cientos de ellas cada día!) y bloqueará automáticamente las que se sepa que alojan publicidad o incluso archivos maliciosos



## II. Instalación de Pi-Hole



Con un nombre como Pi-Hole, podrías asumir que necesitas una Raspberry-Pi... Pero eso no es del todo cierto. **Pi-Hole puede instalarse en cualquier ordenador con Linux (Debian, Fedora, Rocky, Ubuntu, etc.)



Por otro lado, hay que tener en cuenta que **este dispositivo tendrá que funcionar las 24 horas del día por una sencilla razón: ¡sin DNS, no hay Internet!** Por lo tanto, la Raspberry es una buena idea, ya que apenas consume energía.



Para instalarlo, simplemente conéctese a su máquina Linux a través de SSH e introduzca el siguiente comando como "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Nota**: en circunstancias normales, no es aconsejable "piratear" un script sin saber antes lo que hace. Si no estás seguro, ve a la página con un navegador o descarga el contenido como archivo.
>


> **Nota: en versiones mínimas de Debian 11, Curl no está instalado, por lo que necesita instalarlo manualmente con el comando **apt-get install curl** antes de escribir el comando anterior.

Una vez ejecutado el script, se realizarán una serie de pruebas y la propia instalación se hará por sí sola:



![Image](assets/fr/019.webp)



Instalación de Pi-Hole



Una vez finalizada la instalación, aparecerá esta pantalla:



![Image](assets/fr/020.webp)



Pantalla de inicio Pi-Hole



> **Nota**: si estás utilizando DHCP en tu máquina, recibirás un mensaje de advertencia al respecto. Por supuesto, para un uso correcto, le recomendamos encarecidamente que asigne una IP fija a su máquina.

Después de esta pantalla, aparecerán algunos mensajes informativos, y a continuación pasarás al asistente de configuración, que te preguntará en primer lugar a qué servidor DNS reenviará Pi-Hole las peticiones. Por mi parte, he elegido Quad9, que tiene una carta de privacidad del usuario.



![Image](assets/fr/021.webp)



Selección de DNS - Pi-Hole



> **Nota: si estás en una empresa, lo más probable es que tu servidor DNS actual sea el controlador de dominio de Active Directory. Pero no te preocupes, más adelante podrás especificar un redireccionador condicional para un dominio de tu elección. Normalmente, podrá redirigir cualquier petición relativa a su dominio local a su servidor DNS.

Verás que algunas opciones incluyen la opción DNSSEC. Básicamente, el protocolo DNS no es seguro (no se diseñó teniendo esto en cuenta en su momento). DNSSEC resuelve este problema añadiendo un Layer de seguridad mediante el cifrado y la firma de los intercambios, como se explica en el artículo correspondiente: [Seguridad DNS](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Cualquier bloqueador de anuncios se basa en una o más listas para hacer su trabajo. Pi-Hole viene con una sola lista de serie, así que selecciónala y añade más después.



![Image](assets/fr/022.webp)



Ven la pregunta sobre Interface web, su instalación es opcional, ya que la herramienta tiene su propia línea de comandos para la gestión y visualización. Pero este Interface es bastante agradable y bien hecho, por lo que recomiendo que instale al mismo tiempo:



![Image](assets/fr/023.webp)



Si está instalando Pi-Hole en una máquina que ya tiene un servidor Web, puede responder "no" a la siguiente pregunta. Tenga en cuenta, sin embargo, que PHP y varios módulos son necesarios para que esto funcione. En caso contrario, **lighttpd se instalará con todos los módulos necesarios**.



![Image](assets/fr/024.webp)



A continuación se le pregunta si desea registrar las peticiones DNS. **Si desea mantener un historial, configúrelo como sí; de lo contrario, configúrelo como no, pero perderá parte de la funcionalidad** (consulte la siguiente pantalla).



![Image](assets/fr/025.webp)



Para su web Interface, Pi-Hole utiliza una función propia llamada FTLDNS, que proporciona una API y genera estadísticas a partir de las peticiones DNS. Esta función puede incluir un modo de "privacidad" que enmascara los dominios solicitados, los clientes detrás de la solicitud, o ambos. Práctico si quieres hacer monitorización sin vulnerar la privacidad de las personas, o simplemente si quieres cumplir con la normativa pertinente en caso de uso en una red pública.



![Image](assets/fr/026.webp)



Elección del estilo de vida privado



Una vez respondida esta última pregunta, el script hará lo que se supone que debe hacer: descargar los repositorios de GitHub y configurar Pi-Hole. Al final de la instalación, aparecerá una pantalla de resumen con la información importante:



![Image](assets/fr/027.webp)



Pantalla de resumen de la instalación



Anote la contraseña web de Interface y la información de red. Ahora es el momento de configurar el servicio DHCP en nuestra ubicación actual.



## III. Configuración DHCP



Para funcionar, Pi-Hole necesita "resolver" las peticiones DNS de los clientes, para que sepan que es a él a quien deben enviarlas. Hay varias formas de hacerlo:





- Modifique la configuración DNS en su servidor DHCP (por ejemplo, su Box)
- Desactiva este servidor y utiliza el proporcionado por Pi-Hole
- Modificar manualmente cada dispositivo para utilizar Pi-Hole como DNS



Yo personalmente elijo la primera solución. Lo más probable es **que tengas un servidor DHCP donde estás** (normalmente tu caja). Así que no hay necesidad de molestarse.



Como hay un gran número de posibilidades, entre las cajas de los diferentes operadores (que no conozco todos) y los que tienen su propio router, no voy a proporcionar una captura de pantalla para estas modificaciones. En cualquier caso, tendrás que ir a la configuración DHCP y modificar el parámetro "DNS" para incluir la IP Address de tu Pi-Hole.



Una vez hecho esto, si algún dispositivo se ha encendido antes, habrá conservado la configuración anterior, por lo que tendrás que reiniciar la solicitud de configuración.



En estaciones de trabajo Windows, con un símbolo del sistema:



```
ipconfig /renew
```



En una estación de trabajo Linux:



```
dhclient
```



Para el resto de dispositivos, hay que apagarlos y volverlos a encender.



Así que deben obtener los parámetros correctos, para comprobar:



```
ipconfig /all
```



En el campo DNS, debes tener el Address de tu Pi-Hole, en mi caso 192.168.1.42:



![Image](assets/fr/029.webp)



## IV. Uso del Interface web Pi-Hole



Para facilitar la administración, **Pi-Hole** se beneficia de una web Interface bien diseñada. Fácil de usar y accesible, le permite:





- Visualice en tiempo real el número de solicitudes, las solicitudes bloqueadas, etc.
- Gestione sus listas blancas y negras
- Añade entradas estáticas, alias, etc.
- Añadir listas
- Y muchas otras funciones



Por mi parte, voy a añadir una lista de bloqueo. Como ya se ha dicho, sólo se instaló una lista al mismo tiempo que Soft. Hay muchas listas para sitios de anuncios, pero es mejor elegir al menos una específica para el país en el que vives. Una de las listas más conocidas es **EasyList**, y una de ellas es específica para Francia: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Para añadirlo, conéctate primero al admin de Interface: **http://<ip_du_PiHole>/admin**



La contraseña de administrador ya se ha generado (véase la captura de pantalla de fin de instalación), por lo que basta con introducirla para acceder a Interface:



![Image](assets/fr/030.webp)



Interface de Pi-Hole



Podemos ver, por ejemplo, que hay dos clientes conectados al Pi-Hole, que ha procesado 442 peticiones y que 8 de ellas han sido bloqueadas. Estos gráficos pueden ser una buena fuente de información, sobre todo en un contexto profesional.



Para añadir nuestra lista, vaya a los menús "**Gestión de grupos**" y "**Listas**":



![Image](assets/fr/031.webp)



Podemos ver nuestra primera lista "**StevenBlack**", para añadir la nuestra, copiamos el enlace que os he dado arriba y lo insertamos en el campo "**Address**", para la descripción, yo opto por poner el nombre de la lista:



![Image](assets/fr/032.webp)



Añadir una lista en Pi-Hole



Sólo nos queda hacer clic en "**Añadir**" para añadirlo. Para activarlo, necesitamos realizar un paso adicional para "avisar" a Pi-Hole para que se haga cargo de esta lista. Para ello:





- Utilice la línea de comandos integrada
- O bien la web Interface



Personalmente he elegido la segunda, porque si te has fijado bien, el enlace al script PHP que realiza la actualización está directamente en la página en la que nos encontramos (la palabra "online"). Así que todo lo que tienes que hacer es hacer clic en él, que te llevará a una página con una sola opción:



![Image](assets/fr/033.webp)



La página mostrará el resultado del script una vez completado, lo que significa que la lista ha sido tenida en cuenta (a menos que se muestre un mensaje de error, por supuesto).



Como se anunció al principio de este tutorial, Pi-Hole también te permite **bloquear dominios conocidos por distribuir malware. Para reforzar esta característica, te sugiero que añadas también la lista de dominios actualizada regularmente distribuida por Abuse.ch**, que reforzará significativamente la seguridad de tu red, disponible en [this Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Por supuesto, puede añadir cualquier lista que considere relevante o gestionar su lista negra manualmente a través del menú de listas negras.



## V. Pruebas Pi-Hole



Ahora que todo está listo, lo único que tienes que hacer es probar la solución para asegurarte de que funciona correctamente.



Por ejemplo, intentaré llegar al dominio *http://admin.gentbcn.org/* que está en la lista de Abuse.ch porque se sabe que aloja malware:



![Image](assets/fr/034.webp)



Obviamente, me han bloqueado en algún sitio. Para asegurarnos de que es el Pi-Hole el que ha hecho el trabajo, podemos comprobar el registro de consultas en la web Interface "Query Log" para ver que se trata de un bloqueo de una entrada de la lista:



![Image](assets/fr/035.webp)



## VI. Conclusión



En este tutorial, te mostramos cómo configurar un servidor DNS que no sólo elimina la mayoría de los anuncios para tu comodidad de navegación, sino que también añade **un Layer de seguridad bloqueando dominios de phishing y de propagación de malware**.



Todo ello gratuito y económico si se instala en una Raspberry-Pi (en términos de consumo de energía).
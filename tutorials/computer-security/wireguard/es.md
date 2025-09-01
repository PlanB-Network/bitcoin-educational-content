---
name: WireGuard
description: Configuración de WireGuard VPN en Debian y Windows
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Florian BURNEL publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es posible que se hayan realizado cambios en el texto original.*



___



## I. Presentación



En este tutorial, aprenderemos a configurar una VPN basada en WireGuard, una solución VPN gratuita y de código abierto que aumenta el rendimiento sin descuidar la seguridad.



WireGuard es una solución relativamente reciente, disponible como versión estable desde marzo de 2020, y ha tenido el honor de integrarse directamente en el **núcleo Linux desde la versión 5.6**. Esto no impide que sea accesible desde distribuciones Linux más antiguas que utilicen una versión diferente del kernel. Comparado con soluciones como OpenVPN e IPSec, WireGuard es más sencillo de usar y mucho más rápido, como veremos al final de este artículo.



Algunos puntos clave sobre WireGuard:





- Sencillo, ligero y ultraeficiente
- Funcionamiento sólo UDP (lo que puede suponer una desventaja al atravesar determinados cortafuegos)
- Funciona con un modelo de igual a igual en lugar de cliente-servidor
- Autenticación por clave Exchange, según el mismo principio que SSH con claves privadas/públicas
- Utilización de varios algoritmos: cifrado simétrico con ChaCha20, autenticación de mensajes con Poly1305, así como otros como Curve25519, BLAKE2 y SipHash24
- Admite IPv4 e IPv6
- Multiplataforma: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (e implementado en ProtonVPN)
- Sólo 4.000 líneas de código, frente a los cientos de miles de otras soluciones



En cuanto a la parte criptográfica, los distintos algoritmos utilizados se seleccionan a mano, se someten a diversas auditorías y son examinados por investigadores de seguridad especializados en la materia.



El sitio web oficial del proyecto: [wireguard.com](https://www.wireguard.com/)



¿Le convence esta solución después de leer esta introducción? Sólo le queda seguir leyendo



## II. Diagrama del laboratorio WireGuard



Antes de presentar mi laboratorio para configurar WireGuard, debe saber que puede imaginar **utilizar WireGuard para interconectar dos infraestructuras remotas**, pero también para **conectar un cliente remoto a una infraestructura como una red corporativa o su red doméstica**. Esto tiene el mismo espíritu que con OpenVPN, como vimos recientemente en el tutorial "[OpenVPN en Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Si WireGuard no está configurado directamente en el router o firewall, como es concebible con OpenWRT, tendrá que configurar el reenvío de puertos para que el flujo llegue al par WireGuard.



![Image](assets/fr/034.webp)



Ahora te hablaré de mi laboratorio y de lo que vamos a preparar hoy.



Voy a utilizar una máquina Debian 11 como servidor de WireGuard y un cliente Windows como cliente VPN de WireGuard. Aunque es un poco engañoso hablar de una relación cliente-servidor, porque **WireGuard funciona en un modelo "peer-to-peer "**. Eso es un poco engañoso cuando se trata de establecer una conexión "cliente-servidor". Digamos en cambio que voy a tener dos pares o **dos puntos de conexión WireGuard** si lo prefiere: uno bajo Debian 11 y el otro bajo Windows.



Estos dos pares pueden comunicarse entre sí en ambas direcciones, lo que significa que desde mi máquina Windows puedo acceder a la LAN remota de la máquina Debian 11, y viceversa: todo depende de la configuración del túnel y del cortafuegos del par WireGuard.



En este ejemplo, me centraré en el siguiente caso: **desde mi Windows Peer 1 conectado a mi red doméstica, quiero acceder a mi red corporativa para acceder a los servidores de la empresa a través del túnel VPN de WireGuard**. Esto da el siguiente diagrama:



![Image](assets/fr/035.webp)



En términos de direcciones IP, esto da:





- Red doméstica**: 192.168.1.0/24
- Red corporativa**: 192.168.100.0/24
- Red de túneles de WireGuard**: 192.168.110.0/24


+ IP Address del Peer 1 (Windows) en el túnel: 192.168.110.2/24


+ IP Address del Peer 2 (Debian) en el túnel: 192.168.110.121/24



Eso es todo Pasemos a la configuración



**Nota: por defecto, WireGuard opera en modo UDP en el **puerto 51820**.



## III Instalación y configuración del servidor WireGuard



Voy a usar los términos "cliente" para la máquina Windows y "servidor" para la máquina Debian en este tutorial, porque aunque es peer-to-peer, parece más significativo.



### A. Instalación de WireGuard en Debian 11



El paquete de instalación de WireGuard está disponible en los repositorios oficiales de Debian 11, así que todo lo que tenemos que hacer es actualizar la caché de paquetes e instalarlo:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



Se instalará la parte del servidor WireGuard, junto con varias herramientas que dan acceso a comandos útiles para gestionar la configuración.



### B. Instalación de un Interface WireGuard



Mediante el **comando "wg "** necesitamos generate una clave privada y una clave pública: esenciales para la autenticación entre dos pares, es decir, el servidor y un cliente (que también necesitará un par de claves).



Crearemos la clave privada "**/etc/wireguard/wg-private.key**" y la pública "**/etc/wireguard/wg-public.key**" con esta secuencia de comandos:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



El valor de la llave publica sera devuelto en la consola. En el fichero de configuración de WireGuard, necesitamos **añadir el valor de nuestra clave privada**. Para recuperar este valor, introduzca el siguiente comando y copie el valor:



```
sudo cat /etc/wireguard/wg-private.key
```



Es hora de crear un archivo de configuración en "**/etc/wireguard/**". Por ejemplo, podemos nombrar este archivo "**wg0.conf**", si pensamos que la red Interface asociada con WireGuard será "wg0", en el mismo principio que "eth0", por ejemplo.



```
sudo nano /etc/wireguard/wg0.conf
```



En este archivo, primero debemos añadir el siguiente contenido (volveremos a completarlo más adelante):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



La sección `[Interface]` se utiliza para declarar la parte del servidor. Aquí hay alguna información:





- Address**: la IP Address del Interface WireGuard dentro del túnel VPN (subred diferente de la LAN remota)
- SaveConfig**: la configuración se guarda (y se protege) mientras Interface esté activo
- ListenPort**: El puerto de escucha de WireGuard. En este caso, 51820 es el puerto por defecto, pero puede personalizarlo
- PrivateKey**: el valor de la clave privada de nuestro servidor (*wg-private.key*)



Guarda el archivo y ciérralo. Con el comando "**wg-quick**", podemos iniciar este Interface especificando su nombre (wg0, ya que el archivo se llama wg0.conf):



```
sudo wg-quick up wg0
```



Si lista las direcciones IP de su servidor Debian 11, verá una nueva Interface llamada "wg0" con la IP Address definida en el archivo de configuración:



```
ip a
```



![Image](assets/fr/027.webp)



Con el mismo espíritu, podemos visualizar la configuración de Interface "wg0" mediante el comando "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Por último, debemos activar el arranque automático de nuestro WireGuard Interface wg0:



```
sudo systemctl enable wg-quick@wg0.service
```



Por el momento, dejaremos de lado la configuración del lado del servidor de WireGuard.



### C. Activar el reenvío de IP



Para que nuestra máquina Debian 11 pueda **enrutar paquetes entre diferentes redes (como un router)**, es decir, entre la red VPN y la red local, necesitamos habilitar [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Por defecto, esta función está desactivada.



Modificar este archivo de configuración:



```
sudo nano /etc/sysctl.conf
```



Añada la siguiente directiva al final del archivo y guarde:



```
net.ipv4.ip_forward = 1
```



Eso es todo.



### D. Habilitar IP Masquerade



Para que nuestro servidor enrute los paquetes correctamente y para que la LAN remota sea accesible a la máquina Windows, necesitamos activar IP Masquerade en nuestro servidor Debian. Este es un tipo de activación NAT. Voy a realizar esta configuración en el cortafuegos de Linux a través de UFW, que estoy acostumbrado a usar ([tutorial de ufw en Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Si aún no tienes UFW y quieres configurarlo (también puedes usar Nftables), empieza por instalar:



```
sudo apt install ufw
```



En primer lugar, es necesario habilitar SSH para no perder el control del servidor remoto (adaptar el número de puerto):



```
sudo ufw allow 22/tcp
```



El puerto 51820 en UDP también debe estar autorizado, ya que lo utilizamos para WireGuard (de nuevo, adapte el número de puerto):



```
sudo ufw allow 51820/udp
```



A continuación, continuaremos con la configuración para habilitar la mascarada IP. Para ello, necesitamos recuperar el nombre de la Interface conectada a la red local. Si no sabes el nombre, ejecuta "ip a" para ver el nombre de la tarjeta. En mi caso, es la tarjeta "**ens192**".



![Image](assets/fr/036.webp)



Vamos a utilizar esta información. Edita el siguiente archivo:



```
sudo nano /etc/ufw/before.rules
```



Añade estas líneas al final del fichero para **habilitar la mascarada IP en el Interface ens192** (adapta el nombre del Interface) dentro de la cadena POSTROUTING de la tabla NAT de nuestro firewall local:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



La imagen muestra:



![Image](assets/fr/037.webp)



Mantenga abierto este archivo de configuración y continúe con el siguiente paso 😉



### E. Configuración de firewall Linux para WireGuard



Siguiendo en el mismo fichero de configuración, vamos a declarar la red corporativa "192.168.100.0/24" para poder contactar con ella. Aquí están las dos reglas a añadir (idealmente después de la sección "*# ok icmp code for FORWARD*" para agrupar las reglas):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Si sólo quieres autorizar un host, por ejemplo "192.168.100.11", es fácil:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Ahora puede guardar el archivo y cerrarlo. Sólo queda activar UFW y reiniciar el servicio para aplicar nuestros cambios:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



La primera parte de la configuración del servidor Debian ya está completa.



## IV. Cliente WireGuard para Windows



El cliente WireGuard está disponible para Windows, macOS, Android, etc... Esto es una gran noticia. Todas las descargas están disponibles en esta página: [Cliente WireGuard](https://www.wireguard.com/install/). En este ejemplo, voy a configurar el cliente en Windows. Para configurar el cliente WireGuard en Linux, siga el mismo principio que para crear el archivo wg0.conf en la máquina Debian (sin todo el NAT, etc.).



### A. Instalación del cliente Windows de WireGuard



Una vez descargado el ejecutable o el paquete MSI, la instalación es sencilla: basta con ejecutar el instalador y... voilà, ¡listo! 🙂 ..



![Image](assets/fr/038.webp)



### B. Crear un perfil WireGuard



Empieza abriendo el programa para crear un nuevo túnel. Para ello, haz clic en la flecha situada a la derecha del botón "**Añadir túnel**" y pulsa el botón "**Añadir túnel vacío**".



![Image](assets/fr/028.webp)



Se abrirá una ventana de configuración. Cada vez que se crea una nueva configuración de túnel, WireGuard genera un par de claves privada/pública específico para esta configuración. **En esta configuración, necesitamos declarar el "peer", es decir, el servidor remoto:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Necesitamos completar esta configuracion, en particular declarar la IP Address en este Interface (*Address*), pero tambien declarar el servidor remoto WireGuard via un bloque [Peer]. La imagen de abajo deberia recordarle el archivo de configuracion que creamos en el lado del servidor Linux.



Empecemos por el bloque `[Interface]`, añadiendo la IP Address "**192.168.110.2**"; recordemos que el servidor tiene la IP Address "**192.168.110.121**" en este segmento de red. Esto da:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



A continuación, tenemos que declarar el bloque "Peer" con tres propiedades, lo que resulta en esta configuración:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



En imágenes:



![Image](assets/fr/029.webp)



**Algunas explicaciones sobre el bloque [Peer]:





- PublicKey**: es la clave pública del servidor WireGuard Debian 11 (puede obtener su valor con el comando "*sudo wg*")
- AllowedIPs**: son las direcciones IP / subredes accesibles a través de esta red VPN WireGuard, en este caso la subred específica para mi VPN WireGuard (*192.168.110.0/24*) y mi LAN remota (*192.168.100.0/24*)
- Endpoint**: esta es la IP Address del host Debian 11, ya que este es nuestro punto de conexión WireGuard (necesitará especificar la IP pública Address)



Por último, introduce un nombre en el campo "**Nombre**" (sin espacios) y copia y pega la clave pública del cliente, ya que necesitaremos declararla en el servidor. Haz clic en "**Registrar**".



### C. Declarar cliente en el servidor WireGuard



Es hora de volver al servidor Debian para declarar el "**Peer**", es decir, nuestro PC Windows, en la configuración de WireGuard. En primer lugar, necesitamos **detener el Interface "wg0"** para poder modificar su configuración:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



A continuación, modifique el archivo de configuración creado anteriormente:



```
sudo nano /etc/wireguard/wg0.conf
```



En este archivo, después del bloque `[Interface]`, tenemos que declarar un bloque `[Peer]`:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Este bloque [Peer] contiene la clave pública del PC Windows 10 (**PublicKey**) y la IP Address del Interface del PC (**AllowedIPs**): el servidor se comunicará en este túnel WireGuard sólo para contactar con el cliente Windows, de ahí el valor "**192.168.110.2/32**".



Sólo queda guardar el archivo (*CTRL+O luego Enter luego CTRL+X vía Nano*). Reinicia Interface "wg0":



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Para comprobar que la declaración de pares funciona, puede utilizar este comando:



```
sudo wg show
```



Una vez que el host remoto ha configurado su conexión WireGuard, su IP Address se moverá al valor "endpoint".



![Image](assets/fr/033.webp)



Por último, protegeremos los archivos de configuración para limitar el acceso root:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Primera conexión WireGuard



Ahora que la configuración está lista, podemos iniciarla desde el PC con Windows. Para ello, en el cliente "**WireGuard**", pulse sobre el botón "**Activar**": la conexión **cambiará de "Apagado" a "Encendido "**, pero eso no significa que vaya a funcionar. Todo depende de si tu configuración es correcta o no. **¡Cuando se establece la conexión, nuestras dos máquinas se comunican a través del Interface WireGuard configurado en cada lado!



![Image](assets/fr/030.webp)



En caso de problema, esto será visible en la pestaña "**Logbook**". Los dos hosts Exchange paquetes regularmente para comprobar el estado de la conexión, de ahí los mensajes "*Receiving keepalive packet from peer 1*".



![Image](assets/fr/031.webp)



Si la pestaña "**Journal**" de WireGuard muestra un mensaje como el siguiente, debe comprobar que las claves públicas declaradas en ambos lados son correctas.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Desde mi PC remoto, puedo hacer ping a la IP Address de mi Interface WireGuard en el lado del servidor, así como a un host en mi LAN remota.



![Image](assets/fr/032.webp)



### E. Rendimiento: OpenVPN vs WireGuard



Desde mi PC remoto conectado a mi VPN WireGuard, pude acceder a un servidor de archivos y transferir un archivo a través de [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), para ver la velocidad de transferencia. **Con WireGuard, alcanzo un máximo de 45 Mb/s, lo cual es genial, ya que estoy conectado a WiFi



![Image](assets/fr/025.webp)



En las mismas condiciones, pero a través de una conexión OpenVPN (en UDP) esta vez, con el mismo funcionamiento, el rendimiento es totalmente diferente: alrededor de 3 MB/s. La diferencia es evidente



![Image](assets/fr/026.webp)



Esto es interesante, porque si, por ejemplo, cambias de una conexión WiFi a una 4G/5G, la reconexión será tan rápida que la interrupción no será visible.



### F. Bonificación: túnel completo WireGuard



Con la configuración actual, parte del tráfico fluye a través de la VPN, y el resto a través de la conexión a Internet del cliente, incluyendo la navegación por Internet. Si queremos cambiar a WireGuard **full tunnel mode**, para que todo pase a través del túnel VPN, necesitamos hacer algunos cambios en nuestra configuración....



En primer lugar, debe instalar el paquete "resolvconf" en el directorio:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Una vez hecho esto, necesita modificar el perfil "wg0.conf" en la máquina Debian: detenga Interface, modifíquelo y reinicie.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



A continuación, **en el bloque `[Interface]`, añadimos el servidor DNS a utilizar**. En mi caso, es el controlador de dominio de mi laboratorio, pero también podríamos instalar Bind9 en la máquina Debian para tener un resolvedor local.



```
DNS = 192.168.100.11
```



Guarde el archivo y reinicie Interface:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Por último, en la configuración del túnel en la estación de trabajo de Windows 10, es necesario modificar la sección "AllowedIPs" para indicar que todo debe pasar a través del túnel. Sustituye:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Por:



```
AllowedIPs = 0.0.0.0/0
```



Puedes ver que esto también habilita la opción "**Interruptor asesino*".



![Image](assets/fr/040.webp)



Por último, aproveché este túnel lleno para realizar una pequeña prueba de caudal, cuyos resultados se muestran a continuación:



![Image](assets/fr/039.webp)



La configuración de WireGuard es bastante sencilla y fácil de entender, y sobre todo de mantener. **WireGuard está considerado como el futuro de las VPN**, ¡así que será mejor que lo sigamos de cerca! También podemos ver que el beneficio es significativo en términos de rendimiento, lo cual es una gran ventaja para WireGuard en comparación con OpenVPN.



Documentación adicional:





- [Hombre - Comando wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Hombre - Comando wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**Su VPN WireGuard está funcionando ¡Enhorabuena!
---
name: Bitcoin Core (Linux)
description: Ejecutar su propio nodo con Bitcoin core en Linux
---

![cover](assets/cover.webp)


## Ejecutar su propio nodo con Bitcoin core


Introducción a Bitcoin y al concepto de nodo, complementada con una completa guía de instalación en Linux.


Uno de los aspectos más emocionantes de Bitcoin es la posibilidad de ejecutar el programa uno mismo, y así participar a un nivel granular en la red y en la verificación de la transacción pública Ledger.


Bitcoin, como proyecto de código abierto, está disponible gratuitamente y se distribuye públicamente desde 2009. Casi 17 años después de su creación, Bitcoin es ahora una red monetaria digital robusta e imparable, que se beneficia de un poderoso efecto de red orgánico. Por sus esfuerzos y su visión, Satoshi Nakamoto merece nuestra gratitud. Por cierto, alojamos el whitepaper de Bitcoin aquí en Agora 256 (nota: también en la universidad).


### Convertirse en su propio banco


Gestionar tu propio nodo se ha convertido en algo esencial para los adeptos a la ética de Bitcoin. Sin pedir permiso a nadie, es posible descargar el Blockchain desde el principio y verificar así todas las transacciones de la A a la Z según el protocolo Bitcoin.


El programa también incluye su propio Wallet. Así, tenemos el control sobre las transacciones que enviamos al resto de la red, sin intermediarios ni terceros. Usted es su propio banco.


El resto de este artículo es, por tanto, una guía para instalar Bitcoin core -la versión de software Bitcoin más utilizada- específicamente en distribuciones Linux compatibles con Debian, como Ubuntu y Pop!OS. Sigue esta guía para dar un paso más hacia tu soberanía individual.


## Guía de instalación de Bitcoin core para Debian/Ubuntu


**Requisitos previos**


- Mínimo 6 GB de almacenamiento de datos (nodo pruned) - 1 TB de almacenamiento de datos (Full node)
- La *Descarga Inicial de Bloques* (IBD) tardará al menos 24 horas. Esta operación es obligatoria incluso para un nodo pruned.
- Permita ~600GB de ancho de banda para el IBD, incluso para un nodo pruned.


**Nota:💡** los siguientes comandos están predefinidos para Bitcoin core versión 24.1.


### Descarga y verificación de archivos



- [Descargar](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, así como los archivos `SHA256SUMS` y `SHA256SUMS.asc` (obviamente, deberá descargar la última versión del software).



- Abra un terminal en el directorio donde se encuentran los archivos descargados. Ejemplo: `cd ~/Downloads/`.



- Compruebe que la suma de comprobación del archivo de versiones aparece en el archivo de sumas de comprobación mediante el comando `sha256sum --ignore-missing --check SHA256SUMS`.



- La salida de este comando debe incluir el nombre del archivo de la versión descargada seguido de `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Instala git usando el comando `sudo apt install git`. A continuación, clona el repositorio que contiene las claves PGP de los firmantes de Bitcoin core utilizando el comando `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Importe las claves PGP de todos los firmantes utilizando el comando `gpg --import guix.sigs/builder-keys/*`



- Compruebe que el archivo de suma de comprobación está firmado con las claves PGP de los firmantes mediante el comando `gpg --verify SHA256SUMS.asc`.



Cada firma válida mostrará una línea que empieza por: `gpg: Good signature` y otra línea que termina con: `Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (ejemplo de huella digital de clave PGP de Pieter Wuille).


**Nota💡:** no es necesario que todas las claves de firmante devuelvan un "OK". De hecho, puede que sólo sea necesaria una. Depende del usuario determinar su propio umbral de validación para la verificación PGP.


Puedes ignorar las advertencias:



- esta clave no está certificada con una firma de confianza



- `No hay indicios de que la firma pertenezca al propietario.`


### Instalación del Bitcoin core gráfico Interface



- En el terminal, todavía en el directorio donde se encuentra el archivo de la versión Bitcoin core, utilice el comando `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` para extraer los ficheros contenidos en el archivo.



- Instale los archivos previamente extraídos utilizando el comando `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Instale las dependencias necesarias utilizando el comando `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Inicie _bitcoin-qt_ (Bitcoin core gráfica Interface) utilizando el comando `Bitcoin-qt`.



- Para elegir un nodo pruned, marque _Limitar almacenamiento Blockchain_ y configure el límite de datos a almacenar:


![welcome](assets/fr/02.webp)


### Conclusión de la Parte 1: Guía de instalación


Una vez instalada Bitcoin core, se recomienda mantenerla en funcionamiento en la medida de lo posible para que contribuya a la red Bitcoin verificando transacciones y transmitiendo nuevos bloques a otros pares.


Sin embargo, ejecutar y sincronizar el nodo de forma intermitente, aunque sólo sea para validar las transacciones recibidas y enviadas, sigue siendo una buena práctica.


![Creation wallet](assets/fr/03.webp)


## Configurando Tor para un Nodo Bitcoin core


**Nota💡:** esta guía está diseñada para Bitcoin core 24.0.1 en distribuciones Linux compatibles con Ubuntu/Debian.


### Instalando y configurando Tor para Bitcoin core


En primer lugar, necesitamos instalar el servicio Tor (The Onion Router), una red utilizada para la comunicación anónima, que nos permitirá anonimizar nuestras interacciones con la red Bitcoin. Para una introducción a las herramientas de protección de la privacidad en línea, incluyendo Tor, consulte nuestro artículo sobre este tema.


Para instalar Tor, abra un terminal e introduzca `sudo apt -y install tor`. Una vez completada la instalación, el servicio se iniciará automáticamente en segundo plano. Compruebe que se está ejecutando correctamente con el comando `sudo systemctl status tor`. La respuesta debería mostrar `Active: active (exited)`. Pulse `Ctrl+C` para salir de esta función.


**Consejo:** en cualquier caso, puede usar los siguientes comandos en el terminal para iniciar, detener o reiniciar Tor:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


A continuación, vamos a lanzar el Bitcoin core gráfico Interface con el comando `Bitcoin-qt`. Luego, habilitamos la característica automática del software para enrutar nuestras conexiones a través de un proxy Tor: configuración > Red_, y desde allí marque _Conectar a través de proxy SOCKS5 (proxy por defecto)_ así como _Usar un proxy SOCKS5 separado para alcanzar pares a través de servicios Tor onion_.


![option](assets/fr/04.webp)


Bitcoin core detecta automáticamente si Tor está instalado y, si es así, creará por defecto conexiones salientes a otros nodos que también usen Tor, además de conexiones a nodos que usen redes IPv4/IPv6 (clearnet).


**Nota💡:** para cambiar el idioma de la pantalla a francés, ve a la pestaña Pantalla en Ajustes.


### Configuración avanzada de Tor (opcional)


Es posible configurar Bitcoin core para que sólo utilice la red Tor para conectarse con pares, optimizando así nuestro anonimato a través de nuestro nodo. Dado que no hay funcionalidad incorporada para esto en el Interface gráfico, tendremos que crear manualmente un archivo de configuración. Vaya a Configuración, luego a Opciones.


![option 2](assets/fr/05.webp)


Aquí, haga clic en _Abrir archivo de configuración_. Una vez en el fichero de texto `Bitcoin.conf`, simplemente añada una línea `onlynet=onion` y guarde el fichero. Es necesario reiniciar Bitcoin core para que este comando surta efecto.


A continuación, configuraremos el servicio Tor para que Bitcoin core pueda recibir conexiones entrantes a través de un proxy, permitiendo a otros nodos de la red utilizar nuestro nodo para descargar datos de Blockchain sin comprometer la seguridad de nuestra máquina.


En el terminal, introduzca `sudo nano /etc/tor/torrc` para acceder al fichero de configuración del servicio Tor. En este fichero, busque la línea `#ControlPort 9051` y elimine el `#` para habilitarlo. Ahora añada dos nuevas líneas al fichero:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Para salir del archivo mientras lo guarda, pulse `Ctrl+X > Y > Enter`. De vuelta en el terminal, reinicie Tor introduciendo el comando `sudo systemctl restart tor`.


Con esta configuración, Bitcoin core podrá establecer conexiones entrantes y salientes con otros nodos de la red sólo a través de la red Tor (Onion). Para confirmar esto, haga clic en la pestaña _Window_, luego _Peers_.


![Nodes Window](assets/fr/06.webp)


### Recursos adicionales


En última instancia, utilizar sólo la red Tor (`onlynet=onion`) podría hacerte vulnerable a un Sybil Attack. Por eso algunos recomiendan mantener una configuración multi-red para mitigar este tipo de riesgo. Además, todas las conexiones IPv4/IPv6 serán enrutadas a través del proxy Tor una vez configurado, como se indicó anteriormente.


Alternativamente, para permanecer únicamente en la red Tor y mitigar el riesgo de un Sybil Attack, puede añadir el Address de otro nodo de confianza a su archivo `Bitcoin.conf` añadiendo la línea `addnode=dirección_confiada.onion`. Puedes añadir esta línea varias veces si quieres conectarte a varios nodos de confianza.


Para ver los registros de su nodo Bitcoin específicamente relacionados con su interacción con Tor, añada `debug=tor` a su fichero `Bitcoin.conf`. Ahora tendrá información relevante de Tor en su registro de depuración, que puede ver en la ventana _Información_ con el botón _Archivo de Depuración_. También es posible ver estos registros directamente en el terminal con el comando `bitcoind -debug=tor`.


**Tip💡:** aquí hay algunos enlaces interesantes:


- [Página Wiki que explica Tor y su relación con Bitcoin](https://en.Bitcoin.it/wiki/Tor)
- [Generador de archivos de configuración Bitcoin core por Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Guía de configuración de Tor por Jon Atack](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Como siempre, si tienes alguna pregunta, no dudes en compartirla con la comunidad de Agora256. ¡Aprendemos juntos para ser mañana mejores de lo que somos hoy!
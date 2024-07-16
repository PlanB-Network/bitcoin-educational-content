---
name: Noeud Bitcoin Core (linux)
description: Faire tourner son propre nœud avec Bitcoin Core
---

![cover](assets/cover.webp)

# Faire tourner son propre nœud avec Bitcoin Core

Introducción a Bitcoin y al concepto de nodo, complementado con una guía completa de instalación en Linux.

Una de las propuestas más emocionantes de Bitcoin es poder ejecutar el programa uno mismo y así participar a nivel granular en la red y en la verificación del registro público de transacciones.

Bitcoin, un proyecto de código abierto, se distribuye públicamente y está disponible de forma gratuita desde 2009. Casi 15 años después de su aparición, Bitcoin es ahora una red monetaria digital sólida e imparable, que se beneficia de un poderoso efecto de red orgánica. Por sus esfuerzos y visión, Satoshi Nakamoto merece nuestro agradecimiento. De hecho, alojamos el libro blanco de Bitcoin aquí en Agora 256 (nota: también en la universidad).

## Convertirse en su propio banco

Hacer funcionar su propio nodo se ha convertido en algo imprescindible para los seguidores del axioma de Bitcoin. Sin pedir permiso a nadie, es posible descargar la cadena de bloques desde el principio y así verificar todas las transacciones de principio a fin según el protocolo de Bitcoin.

El programa también incluye su propia billetera. De esta manera, tenemos control sobre las transacciones que emitimos al resto de la red, sin intermediarios ni terceros. Usted es su propio banco.

La siguiente parte de este artículo es una guía de instalación de Bitcoin Core, la versión de software de Bitcoin más extendida, específicamente en distribuciones de Linux compatibles con Debian, como Ubuntu y Pop!/\_OS. Siga esta guía para dar un paso más hacia su soberanía individual.

## Guía de instalación de Bitcoin Core en Debian/Ubuntu

> Requisitos previos
>
> - Al menos 6GB de almacenamiento de datos (nodo podado/pruned node) - 1TB de almacenamiento de datos (nodo completo/full node)
> - Prever al menos 24 horas para completar el IBD (Initial Block Download o Descarga Inicial de Bloques). Esta operación es obligatoria incluso para un nodo podado.
> - Prever ~600GB de ancho de banda para el IBD, incluso para un nodo podado.

> 💡 Los siguientes comandos están predefinidos para la versión 24.1 de Bitcoin Core.

## Descarga y verificación de archivos

1. Descargar bitcoin-24.1-x86_64-linux-gnu.tar.gz, así como los archivos SHA256SUMS y SHA256SUMS.asc. (https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Abrir una terminal en el directorio donde se encuentran los archivos descargados. Ejemplo: cd ~/Downloads/.
3. Verificar que el checksum del archivo de versión esté listado correctamente en el archivo de checksum utilizando el comando sha256sum --ignore-missing --check SHA256SUMS.
4. La salida de este comando debería incluir el nombre del archivo de versión descargado seguido de "OK". Ejemplo: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Instalar git utilizando el comando sudo install git. Luego, clonar el repositorio que contiene las claves PGP de los firmantes de Bitcoin Core utilizando el comando git clone https://github.com/bitcoin-core/guix.sigs.
6. Importar las claves PGP de todos los firmantes utilizando el comando gpg --import guix.sigs/builder-keys//\*
7. Verificar que el archivo de checksum esté firmado correctamente con las claves PGP de los firmantes utilizando el comando gpg --verify SHA256SUMS.asc.

Cada firma devolverá una línea que comienza con: gpg: Good signature y otra que termina con Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (ejemplo de la huella digital de la clave PGP de Pieter Wuille).

> 💡 No es necesario que todas las claves de los firmantes devuelvan un "OK". En realidad, solo una podría ser necesaria. Depende del usuario determinar su propio umbral de validación en relación a la verificación mediante PGP.
>
> Puede ignorar los mensajes WARNING: This key is not certified with a trusted signature!

> There is no indication that the signature belongs to the owner.

## Instalación de la interfaz gráfica de Bitcoin Core

1. En la terminal, aún en el directorio donde se encuentra el archivo de versión de Bitcoin Core, utilizar el comando tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz para extraer los archivos contenidos en el archivo comprimido.

2. Instalar los archivos extraídos anteriormente utilizando el comando sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*

3. Instalar las dependencias necesarias utilizando el comando sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev

4. Iniciar bitcoin-qt (interfaz gráfica de Bitcoin Core) utilizando el comando bitcoin-qt.

5. Para seleccionar un nodo reducido, marcar Limit blockchain storage y configurar el límite de datos a almacenar:

![welcome](assets/1.webp)

## Conclusión de la parte 1: guía de instalación

Una vez que Bitcoin Core esté instalado, se recomienda dejarlo funcionando el mayor tiempo posible para contribuir a la verificación de transacciones y la transmisión de nuevos bloques a otros pares en la red de Bitcoin.

Sin embargo, ejecutar y sincronizar el nodo de forma intermitente, aunque sea solo para validar las transacciones recibidas y emitidas, sigue siendo una buena práctica.

![Creation wallet](assets/2.webp)

# Configurando Tor para un nodo Bitcoin Core

> Esta guía está diseñada para Bitcoin Core 24.0.1 en distribuciones Linux compatibles con Ubuntu/Debian.

## Instalar y configurar Tor para Bitcoin Core

Primero, necesitamos instalar el servicio Tor (The Onion Router), una red utilizada para la comunicación anónima, que nos permitirá anonimizar nuestras interacciones con la red Bitcoin. Para una introducción a las herramientas de privacidad online, incluyendo Tor, vea nuestro artículo sobre el tema.

Para instalar Tor, abra un terminal e introduzca sudo apt -y install tor. Una vez instalado, el servicio debería iniciarse automáticamente en segundo plano. Compruebe que se está ejecutando correctamente con sudo systemctl status tor. La respuesta debería ser Activo: active (exited). Pulse Ctrl+C para salir de esta función.

> En cualquier caso, puede utilizar los siguientes comandos en el terminal para iniciar, detener o reiniciar Tor:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

A continuación, iniciamos la interfaz gráfica de Bitcoin Core con el comando bitcoin-qt. A continuación, vamos a activar la funcionalidad automática del software para dirigir nuestras conexiones a través de un proxy Tor: Configuración > Red, y desde allí podemos marcar Conectar a través de un proxy SOCKS5 (proxy por defecto), así como Usar un proxy SOCKS5 separado para llegar a los pares a través de los servicios de cebolla de Tor.

![opción](activos/3.webp)

Bitcoin Core detecta automáticamente si Tor está instalado y, si es así, creará por defecto conexiones Salientes a otros nodos que también usen Tor, además de conexiones a nodos que usen redes IPv4/IPv6 (clearnet).

> Para cambiar el idioma de visualización a Francés, vaya a la pestaña Visualización en Configuración.

## Configuración avanzada de Tor (opcional)

Es posible configurar Bitcoin Core para usar sólo la red Tor para conectarse con peers, optimizando nuestro anonimato a través de nuestro nodo. Como no hay funcionalidad para esto en la GUI, tendremos que crear manualmente un fichero de configuración. Vaya a Configuración, luego a Opciones.

![opción 2](activos/4.webp)

Aquí, haga clic en Abrir archivo de configuración. Una vez en el archivo de texto bitcoin.conf, simplemente añade una línea onlynet=onion y guarda el archivo. Debe reiniciar Bitcoin Core para que este comando surta efecto.

A continuación, vamos a configurar el servicio Tor para que Bitcoin Core pueda recibir conexiones entrantes a través de un proxy, permitiendo que nuestros pares de la red utilicen nuestro nodo para descargar datos de la cadena de bloques sin comprometer la seguridad de nuestra máquina.

En la terminal, ingrese sudo nano /etc/tor/torrc para acceder al archivo de configuración del servicio Tor. En este archivo, busque la línea #ControlPort 9051 y elimine el # para activarla. Ahora agregue dos nuevas líneas al archivo: HiddenServiceDir /var/lib/tor/bitcoin-service/ y HiddenServicePort 8333 127.0.0.1:8334. Para salir del archivo y guardarlo, presione Ctrl+X > Y > Enter. De vuelta en la terminal, reinicie Tor ingresando el comando sudo systemctl restart tor.

Con esta configuración, Bitcoin Core podrá establecer conexiones entrantes y salientes solo a través de la red Tor (Onion). Para confirmar que esto es así, haga clic en la pestaña Ventana y luego en Pares.

![Fenetre des noeuds](assets/5.webp)

## Recursos adicionales

En última instancia, utilizar solo la red Tor (onlynet=onion) podría hacerlo vulnerable a un ataque Sybil. Es por eso que algunos recomiendan mantener una configuración de red múltiple para mitigar este tipo de riesgo. Además, todas las conexiones IPv4/IPv6 serán dirigidas a través del proxy Tor una vez que esté configurado, como se indicó anteriormente.

Alternativamente, para permanecer solo en la red Tor y mitigar el riesgo de un ataque Sybil, puede agregar la dirección de otro nodo de confianza a su archivo bitcoin.conf agregando la línea addnode=trusted_address.onion. Es posible agregar esta línea varias veces si desea conectarse a varios nodos de confianza.

Para consultar los registros de su nodo Bitcoin en relación específicamente con su interacción con Tor, agregue debug=tor a su archivo bitcoin.conf. Ahora tendrá la información relevante sobre Tor en su registro de depuración, que puede consultar en la ventana Información con el botón Archivo de registro de depuración. También es posible consultar estos registros directamente en la terminal con el comando bitcoind -debug=tor.

> 💡 Algunos enlaces interesantes:
>
> - Página wiki que explica Tor y su relación con Bitcoin
> - Generador de archivo de configuración de Bitcoin Core por Jameson Lopp
> - Guía de configuración de Tor por Jon Atack

Como siempre, si tiene alguna pregunta, no dude en compartirla con la comunidad Agora256, ¡aprendemos juntos para ser mejores mañana de lo que somos hoy!

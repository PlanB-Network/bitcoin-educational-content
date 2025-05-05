---
name: Paraguas
description: Descubre e instala Umbrel - Tu nodo Bitcoin y servidor doméstico
---

![cover](assets/cover.webp)



## Introducción



### ¿Qué es un nodo Bitcoin?



Un nodo Bitcoin es un ordenador que participa en la red Bitcoin ejecutando el software Bitcoin Core o un cliente alternativo. Su papel es esencial para el funcionamiento y la seguridad de la red:





- Almacenamiento de Blockchain**: Mantiene una copia completa y actualizada del Blockchain Bitcoin
- Verificación de transacciones**: valida cada transacción y bloque de acuerdo con las normas del protocolo
- Difusión de la información**: Comparte nuevas transacciones y bloques con otros nodos
- Creación de consenso**: Contribuye a la aplicación de las normas de la red



Gestionar su propio nodo Bitcoin es un paso crucial hacia la soberanía financiera, ya que ofrece varias ventajas clave:





- Confidencialidad**: Comparte tus transacciones sin revelar tu información a terceros
- Resistencia a la censura**: Nadie puede impedirte usar Bitcoin
- Verificación independiente**: No necesitas confiar en nodos ajenos para verificar tus transacciones
- Creación de consenso**: Contribuir a la aplicación de las normas de la red Bitcoin
- Apoyo a la red**: Participe activamente en la distribución y descentralización de la red



### Paraguas: Una solución sencilla para ejecutar un nodo Bitcoin



Umbrel es un sistema operativo de código abierto que simplifica la instalación y gestión de un nodo Bitcoin. También transforma tu ordenador en un servidor doméstico personal y privado, facilitando el alojamiento de :





- Un nodo Bitcoin completo
- Bitcoin aplicaciones esenciales (Electrs, Mempool.space)
- Otros servicios personales (almacenamiento en la nube, streaming, VPN, etc.)



Con su elegante e intuitivo Interface de usuario, Umbrel hace que los servicios autoalojados sean accesibles para todos, al tiempo que conserva el control total sobre sus datos.



## Opciones de instalación del paraguas



Umbrel ofrece dos formas principales de utilizar su solución: una opción llave en mano (Umbrel Home) y una versión gratuita de código abierto (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: la solución llave en mano



Umbrel Home es un servidor doméstico preconfigurado, especialmente diseñado para una experiencia óptima. Esta solución de hardware todo en uno incluye:



**Características del hardware**




- Procesador de alto rendimiento optimizado para el autoalojamiento
- Almacenamiento SSD de alta velocidad preinstalado
- Sistema de refrigeración silencioso
- Diseño compacto y elegante
- Puertos USB y Ethernet integrados



**Beneficios exclusivos**




- Instalación Plug and Play: enchufar y listo
- Soporte Premium con asistencia dedicada
- Actualizaciones automáticas garantizadas
- Asistente de migración integrado
- Garantía total del hardware
- Compatibilidad total con todas las funciones



**Precio**: 399 euros (el precio puede variar según la temporada)



### UmbrelOS: La versión de código abierto



UmbrelOS es la versión gratuita y de código abierto del sistema operativo Umbrel. Esta solución flexible te permite utilizar tu propio hardware al tiempo que te beneficias de las funciones esenciales de Umbrel.



**Beneficios**




- Totalmente gratis
- Código fuente abierto y verificable
- Libertad de elección
- Opciones avanzadas de personalización



**Plataformas compatibles**




- Raspberry Pi 5: una solución popular y asequible
- Sistemas X86: Para PC o servidores estándar
- Máquina virtual: Para pruebas o uso en infraestructura existente



**Limitaciones




- Sólo apoyo comunitario
- Algunas funciones avanzadas reservadas a Umbrel Home
- Configuración inicial más técnica
- El rendimiento depende del hardware seleccionado



Esta versión es ideal para :




- Usuarios técnicos
- Los que ya poseen equipos compatibles
- Personas con ganas de aprender y experimentar
- Desarrolladores que deseen contribuir al proyecto



Enlaces oficiales de instalación :




- [Instalación en Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Instalación en sistemas x86 (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Instalación de una máquina virtual](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



En este tutorial, nos centraremos en la instalación de UmbrelOS en una Raspberry Pi 5, pero los principios básicos siguen siendo similares para otras plataformas.



## Instalación de Umbrel OS en Raspberry Pi 5



### Componentes necesarios



Para esta instalación necesitarás :





- Raspberry Pi 5 (4 GB u 8 GB de RAM)
- Una fuente de alimentación oficial de Raspberry Pi Supply (¡esencial para la estabilidad!)
- Tarjeta MicroSD (32 GB mínimo)
- Un lector de tarjetas microSD
- Un SSD externo para almacenar datos
- Cable Ethernet
- Un cable USB para conectar la unidad SSD



### Pasos de la instalación



**Descargar UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Visite el [sitio web oficial](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Descargar la última versión de UmbrelOS para Raspberry Pi 5



**Instalación de Balena Etcher**



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Descargue e instale [Balena Etcher](https://www.balena.io/etcher/) en su ordenador



**Preparación de la tarjeta microSD



![Insertion carte microSD](assets/fr/03.webp)




- Inserta tu tarjeta microSD en el lector de tarjetas de tu ordenador



**Imagen intermitente**



![Flashage UmbrelOS](assets/fr/04.webp)




- Lanzar Balena Etcher
- Seleccione la imagen UmbrelOS descargada
- Elige tu tarjeta microSD como destino
- Haz clic en "¡Flash!" y espera a que termine el proceso
- Expulsar la tarjeta de forma segura



**instalación de tarjeta microSD



![Installation microSD](assets/fr/05.webp)




- Inserta la tarjeta microSD en tu Raspberry Pi 5



**Conexión periférica**



![Connexion périphériques](assets/fr/06.webp)




- Conecte la unidad SSD externa a un puerto USB disponible
- Conecte el cable Ethernet entre la Pi y su router



**Encendido



![Démarrage du Pi](assets/fr/07.webp)




- Conecta la alimentación oficial de Raspberry Pi Supply
- Espere unos minutos a que se inicie el sistema



**Primer acceso**



![Accès interface web](assets/fr/08.webp)




- En un dispositivo conectado a la misma red, abra su navegador
- Acceda al sitio web Interface de Umbrel en: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Si `umbrel.local` no funciona, tendrás que encontrar la IP Address de tu Raspberry Pi en tu red local. Puedes :




- Consulte la Interface de su router
- Utilizando un escáner de red como nmap
- Utilice el comando `arp -a` en el terminal de su ordenador



## Primer paso en Umbrel



Una vez que tu Umbrel esté iniciado y accesible a través de tu navegador, sigue estos pasos para empezar:



### Configuración inicial



**Crea tu cuenta**



![Création compte](assets/fr/10.webp)




- Elija un nombre de usuario
- Establecer una contraseña segura
- Necesitará estas credenciales para acceder a su Umbrel



**Confirmación de la cuenta



![Confirmation compte](assets/fr/11.webp)




- Haga clic en "Siguiente" para acceder a su panel de control



**Descubrimiento del Interface**



![Interface Umbrel](assets/fr/12.webp)




- Acceder a la App Store de Umbrel
- Descubra las numerosas aplicaciones disponibles
- Empecemos por instalar las aplicaciones esenciales para Bitcoin



### Instalación de aplicaciones Bitcoin



**Nodo Bitcoin**



![Bitcoin Node](assets/fr/13.webp)




- Primera aplicación a instalar
- Descargue y compruebe toda la Blockchain Bitcoin



**Electrs**



![Installation Electrs](assets/fr/14.webp)




- Servidor Electrum para conectar los monederos Bitcoin
- Sincroniza con su nodo Bitcoin



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Pantalla Interface para Blockchain
- Seguimiento de transacciones y bloqueos en tiempo real



## Seguimiento de una transacción con Mempool.space



Mempool.space es un explorador de código abierto de Blockchain que proporciona una visualización en tiempo real de la red Bitcoin. Te permite hacer un seguimiento de tus transacciones y comprender cómo se propagan las transacciones en la red.



### Entender Mempool y las confirmaciones



La "Mempool" (reserva de memoria) es como una sala de espera virtual donde se almacenan todas las transacciones no confirmadas de la Bitcoin antes de ser incluidas en un bloque. Así es como se procesa una transacción:



1. **Difusión**: Cuando envías una transacción, primero se difunde en la red Bitcoin


2. **En espera en Mempool**: En espera de ser seleccionado por un Miner en función de los costes


3. **Primera confirmación**: Un menor lo incluye en un bloque (1ª confirmación)


4. **Confirmaciones adicionales**: Cada nuevo bloque minado después del que contiene su transacción añade una confirmación



El número recomendado de confirmaciones depende de la cantidad :




- Para cantidades pequeñas: 1-2 confirmaciones pueden ser suficientes
- Para grandes importes: 6 confirmaciones se consideran generalmente muy seguras



### Explorar Interface desde Mempool.space



1. **La página de inicio** le ofrece una visión general de la red Bitcoin:




   - Bloques minados recientemente
   - Estimaciones de costes para diferentes prioridades
   - Estado actual de Mempool



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Buscar una transacción**: Para rastrear una transacción específica, pegue su identificador (txid) en la barra de búsqueda situada en la parte superior de la página.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analizar los detalles de las transacciones



Una vez encontrada su transacción, Mempool.space le presenta un análisis completo:



1. **Información esencial** :




   - Estado (confirmado o no)
   - Gastos pagados (en Sats/vB)
   - Tiempo estimado de confirmación



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Estructura de transacción** :




   - Representación visual de entradas y salidas
   - Lista detallada de las direcciones implicadas
   - Importes transferidos



3. **Datos técnicos** :




   - Peso de la transacción
   - Tamaño virtual
   - Formato y versión utilizados
   - Otros metadatos específicos



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Ventajas de utilizar Mempool.space en Umbrel



1. **Confidencialidad**: Tus peticiones pasan por tu propio nodo


2. **Independencia**: No es necesario depender de un servicio de terceros


3. **Fiabilidad**: Acceso a los datos incluso cuando los navegadores públicos no funcionan



Con esta aplicación, puede supervisar eficazmente sus transacciones, entender cómo afectan las comisiones a la velocidad de confirmación y comprender mejor cómo funciona la red Bitcoin.



## Conexión de un Wallet Bitcoin a su nodo



### Configuración Electrs



**Conexión local



![Connexion locale](assets/fr/18.webp)




- Para uso en su red local
- Instalación más rápida y sencilla



**Conexión remota a través de Tor**



![Connexion Tor](assets/fr/19.webp)




- Para acceder a tu nodo desde cualquier lugar
- Más seguro y privado



### Conexión con Sparrow Wallet



**Acceso a los parámetros



![Paramètres Sparrow](assets/fr/20.webp)




- Gorrión abierto Wallet
- Vaya a Preferencias > Servidor
- Haga clic en "Modificar conexión existente"



**Elección del tipo de conexión



Sparrow ofrece tres modos de conexión:



***Servidor público***




- Conexión a servidores públicos (por ejemplo, blockstream.info, Mempool.space)
- Sencillo pero menos privado



***Bitcoin Core***




- Conexión directa a un nodo Bitcoin
- Privado pero más lento



***Private Electrum***




- Conéctese a su servidor Electrs
- Combina confidencialidad y rendimiento



*configuración *Electrs**



Elija su tipo de conexión utilizando la información que aparece en la aplicación Electrs que vimos antes:



En ambos casos, deje sin marcar las opciones "Usar SSL" y "Usar proxy".



**Conexión local


Host: umbrel.local


Número de puerto: 50001



**Conexión remota (Tor)**


Anfitrión : [su-Address-onion]


Número de puerto: 50001



La conexión Tor es necesaria si quieres acceder a tu nodo fuera de tu red local.



![Configuration connexion](assets/fr/21.webp)


Para más información sobre el software Sparrow Wallet, disponemos de un completo tutorial :


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Conclusión



Su Umbrel ya está listo para ser utilizado. Participarás activamente en la red Bitcoin manteniendo el control total de tus datos. No dudes en explorar las muchas otras aplicaciones disponibles en la App Store de Umbrel para ampliar las capacidades de tu servidor doméstico.



## Recursos útiles



### Documentación oficial




- [Página web oficial de Umbrel](https://umbrel.com)
- [Documentación de Umbrel](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Aplicaciones Bitcoin




- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Gorrión Wallet](https://sparrowwallet.com)



### Comunidad




- [Paraguas del Foro](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)
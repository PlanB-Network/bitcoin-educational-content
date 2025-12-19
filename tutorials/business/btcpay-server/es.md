---
name: BTCPay Server
description: Aceptar pagos en BTC sin intermediarios
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server es un programa informático gratuito y de código abierto creado por Nicolas Dorier que permite aceptar pagos en bitcoin sin intermediarios. Diseñado para ofrecer autonomía y soberanía financiera, se instala en su propio servidor y proporciona una gestión completa de las transacciones, desde la facturación hasta la validación de los pagos on-chain o Lightning Network, pasando por la contabilidad. Se integra fácilmente con sitios de comercio electrónico (WooComerce, Shopify, etc.) o puede utilizarse como terminal de pago para tiendas físicas (*POS*).



BTCPay Server es sin duda la solución más avanzada para los comerciantes que desean aceptar bitcoin. Es el software más completo y robusto en términos de seguridad, soberanía y confidencialidad. Por otro lado, también es el más complejo de instalar y mantener. También existen alternativas más sencillas: algunas son totalmente custodiables, como OpenNode, mientras que otras ofrecen un interesante compromiso entre facilidad de uso y soberanía, como Swiss Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

El objetivo de este tutorial es guiarle paso a paso a través de la instalación, configuración y uso de BTCPay Server, para que pueda desplegar una infraestructura de pago segura e independiente en línea con la ética de Bitcoin.



## Características del servidor BTCPay



Las soluciones centralizadas de punto de venta Bitcoin, como *OpenNode* por ejemplo, ofrecen facilidad de uso, pero dependen de una tercera empresa ya que no pueden ser autoalojadas y son, en la mayoría de los casos, propietarias. Aunque facilitan la configuración de los pagos, implican gastos de comisión y exponen a sus usuarios a más riesgos que una solución como BTCPay Server, tanto en términos de custodia de fondos como de confidencialidad.



BTCPay Server está dirigido a comerciantes en línea o físicos, asociaciones y organizaciones sin ánimo de lucro que deseen recibir donaciones en bitcoins. También es una solución ideal para propietarios de proyectos y desarrolladores que busquen el apoyo directo de su comunidad.



Las características especiales de BTCPay Server incluyen :




- su **completa autonomía**,
- la ausencia de un procedimiento **KYC**,
- control total de los fondos**,
- la **eliminación de las comisiones de plataforma**.



Al convertirse en su propio procesador de pagos, elimina cualquier dependencia de un tercero centralizado entre usted y sus clientes. Puede aceptar pagos directamente en bitcoins y facturas de pago generate. Esto garantiza que ni usted ni su empresa puedan ser vetados por nadie. Usted desempeña el papel tanto de banco como de procesador de pagos, sin tener que pagar comisiones a un intermediario por cada transacción.



Las comisiones de transacción para **on-chain** se mantienen, pero pueden reducirse utilizando la red **Liquid** o **Lightning**.



Además :




- Interfaz y facturas totalmente personalizables;
- Compatibilidad nativa con **Tor** para una mayor confidencialidad;
- Soporte para **crowdfunding**, **POS** y **botones de pago**;
- Compatible con muchas divisas ;
- Bitcoin pagos directos y entre pares ;
- Control total sobre sus claves privadas;
- Mayor privacidad ;
- Mayor seguridad ;
- Software autoalojado ;
- Compatibilidad con **SegWit** y **red relámpago** ;
- Cartera interna basada en nodos, con integración de carteras de hardware.



## Instalación y configuración del servidor BTCPay



### Elegir el modo de alojamiento



BTCPay Server puede instalarse de diferentes maneras. Dependiendo de sus necesidades y recursos, hay tres opciones principales:




- Servidor BTCPay alojado por un tercero**: usted utiliza una plataforma que aloja el servicio por usted. Es sencillo, pero no suele ser gratuito.
- Servidor BTCPay autoalojado en un servidor en la nube** (por ejemplo, a través de [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) o cualquier otro proveedor). Esta es la solución recomendada para la mayoría de los comerciantes principiantes.
- BTCPay Server instalado en su propio hardware (localmente)** : en un ordenador, mini-PC o Umbrel. Este método es más técnico, pero ofrece total independencia.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Para un comerciante en fase de lanzamiento, la **implantación en un servidor en nube** es el mejor compromiso entre autonomía, sencillez y seguridad, sin tener que gestionar toda la infraestructura técnica.



BTCPay Server puede desplegarse rápidamente desde varios proveedores de alojamiento. Entre ellos, **Voltage** destaca como solución de referencia para los usuarios que requieren una infraestructura **fiable**, **profesional** y **soberana**.



### Crear una instancia de BTCPay Server en Voltage



**Voltage** es una plataforma de alojamiento Bitcoin y Lightning llave en mano que le permite desplegar instantáneamente su propio servidor BTCPay, sin configuraciones complejas ni mantenimiento del servidor.



Visite el [sitio web oficial de Voltage](https://voltage.cloud).



![capture](assets/fr/03.webp)



Cree una **cuenta de usuario** con una dirección de correo electrónico válida y una contraseña segura.



![capture](assets/fr/04.webp)



Voltage ofrece una **prueba gratuita de 7 días**. Tenga en cuenta que después de nuestros 7 días de prueba gratuita, se le invitará a contratar una suscripción fija de **25 $ al mes** para seguir **manteniendo sus nodos activos**.



Una vez que hayas creado tu cuenta Voltage y te hayas conectado por primera vez, serás redirigido a la página de inicio, que tiene dos secciones principales:




- Una sección **Infraestructura** para gestionar los nodos Lightning, Bitcoin Core, BTCPay Server y otros servicios de Bitcoin en la nube;
- y una sección **Pagos** que le permite acceder a API Lightning de Voltage para integrar los pagos de Bitcoin en aplicaciones personalizadas.



Para desplegar su instancia de **BTCPay Server**, haga clic en **Infraestructura de acceso**. Aquí es donde puede crear, gestionar y supervisar todos sus servicios, incluido su nodo Bitcoin y BTCPay Server.



#### Crear un grupo



Antes de desplegar un servicio, la plataforma te pedirá **crear un grupo**. Un **grupo** (espacio de trabajo) es un espacio de trabajo que agrupa todos tus servicios Bitcoin y Lightning (por ejemplo, un nodo, un servidor BTCPay, un explorador, etc.). Es un poco como una carpeta que contiene sus diferentes proyectos.



![capture](assets/fr/05.webp)



A efectos de este tutorial, el grupo que hemos creado se llamará **Genesis**. Si lo deseas, puedes añadir una foto de perfil. Una vez hecho esto, haz clic en el botón **Crear**. Puedes invitar a otros usuarios a unirse al grupo, e incluso cambiar el nombre del grupo si lo deseas.



En la página de inicio del grupo aparecen varias opciones:




- Nodos Lightning** : para desplegar un nodo Lightning completo (LND) ;
- Bitcoin Core Nodes** : para lanzar un nodo Bitcoin completo ;
- Servidor BTCPay** : para alojar una instancia BTCPay lista para usar;
- Cuentas Nostr**: para gestionar identidades Nostr.



Active la **doble autenticación (2FA)** para proteger su cuenta y sus servicios (el botón aparece en rojo si está desactivado).



![capture](assets/fr/06.webp)



Haga clic en **BTCPay Server** entre las opciones, y luego en **Launch a BTCPay Store**.



![capture](assets/fr/07.webp)



Voltage le pedirá **crear y configurar su instancia de servidor BTCPay** eligiendo un **nombre de servicio** (1) y habilitando los pagos Lightning (2).



Necesitarás un nodo Lightning si decides aceptar pagos Lightning.



Si aún no tienes un nodo Bitcoin o Lightning, Voltage te sugerirá que crees uno automáticamente.



Haga clic en **Crear un nodo Rayo** (3) .



![capture](assets/fr/08.webp)



Una vez en la interfaz de creación de nodos, se te pedirá que elijas entre los diseños **estándar** y **profesional**.



Puede crear un nodo real (**Mainnet**) o un nodo de prueba (**Testnet**). A continuación, haz clic en el botón **Continuar**.



![capture](assets/fr/09.webp)



Para este tutorial, vamos a utilizar el plan estándar. Introduzca el **nombre del nodo**, una **contraseña** y pulse el botón **Crear**.



![capture](assets/fr/10.webp)



Al cabo de unos instantes, tu nodo estará operativo y podrás abrir un canal libre con una capacidad de recepción de 500.000 sats.



![capture](assets/fr/11.webp)



Un poco más abajo, a la derecha, encontrará toda la información que necesita sobre su nudo



![capture](assets/fr/12.webp)



Ahora que tenemos nuestro nodo Lightning funcionando, volvamos a instalar nuestro servidor BTCPay. Ahora puedes hacer clic en el botón **Crear BTCPay**.



![capture](assets/fr/13.webp)



Se abrirá una página con tus datos de acceso por defecto, junto con un mensaje que te pedirá que cambies tu contraseña inicial. Una vez hecho esto, haz clic en el botón **Iniciar sesión ahora** para acceder a tu interfaz.



![capture](assets/fr/14.webp)



Ya está Su servidor BTCPay está listo para ser utilizado. Será redirigido directamente a la página de inicio de sesión de su servidor BTCPay.



![capture](assets/fr/15.webp)



Una vez que haya iniciado sesión, configure su primera **tienda**:





- Ponle un **nombre**.





- Elija la **moneda por defecto** (EUR, USD, CFA, etc.).





- Seleccione un **proveedor de tipos de cambio** (por ejemplo, CoinGecko).



![capture](assets/fr/16.webp)



A continuación, se le redirigirá al panel de control de su tienda. En la interfaz del panel de control, verá que el botón **Crear su tienda** está marcado en verde, ya que este paso ya se ha completado.



![capture](assets/fr/17.webp)



Un poco más abajo tenemos los botones **Configurar wallet** y **Configurar nodo Lightning**. En nuestro caso, ya nos hemos conectado a un nodo Lightning que funciona con tensión. Así que no tendremos que hacerlo aquí.



Pasemos a configurar una cartera. Haga clic en el botón **Configurar una cartera**.



Ya que estamos empezando con BTCPay Server, vamos a conectar una wallet existente. Así que pulse **Conectar una cartera existente**.



![capture](assets/fr/18.webp)



A continuación, debe elegir su **método de importación**. Entre las opciones disponibles, seleccione **Introducir clave pública extendida**.



![capture](assets/fr/19.webp)



Al vincular una wallet existente, puede recibir sus pagos **directamente en esta wallet externa**, sin que el servidor de BTCPay tenga acceso a su clave privada. Así, incluso si el servidor fuera hackeado o la clave pública (`xpub`) comprometida, un atacante podría ver su historial de transacciones, pero le sería **imposible acceder a sus fondos**.



Una vez que haga clic en el botón **Introducir clave pública extendida**, será **redirigido** a la página donde debe proporcionar esta clave.



Ahora vamos a recuperar la **clave pública extendida**.



### Conexión de un Bitcoin wallet



Para recibir sus pagos, necesita conectar una Bitcoin wallet a su tienda. Para ello, tiene varias opciones:





- Cartera de hardware** (Ledger, Trezor, Coldcard...) ;





- Cartera de software** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- Servidor BTCPay** interno wallet (no recomendado, ya que es menos seguro y expone más sus fondos en caso de pirateo del servidor).



En este tutorial, utilizaremos una **cartera de software**, que es más accesible para la configuración inicial. Puede elegir entre varias aplicaciones compatibles: **Electrum**, **Phoenix**, **Zeus**, **Muun**, etc.



Para la demostración, utilizaremos **Electrum**. Abra **Electrum**, haga clic en **Cartera** y luego en **Información** :



![capture](assets/fr/20.webp)



A continuación, copia la **clave pública maestra (xpub)**.



![capture](assets/fr/21.webp)



Una vez que haya copiado la clave pública maestra, péguela en el campo correspondiente de la página del servidor BTCPay.



![capture](assets/fr/22.webp)



Tras la verificación, se le redirigirá al panel de control de su tienda.



![capture](assets/fr/23.webp)



### Generar un Punto de Venta (PdV)



Una vez que haya configurado su tienda y su cartera, ya puede configurar un **punto de venta (PoS)** para empezar a recibir pagos Bitcoin directamente de sus clientes.



Esta función integrada de **BTCPay Server** es ideal para **comerciantes, artesanos, restauradores o proveedores de servicios** que deseen aceptar Bitcoin **sin sitio web** ni conocimientos técnicos especiales.



### ¿Cuál es el punto de venta?



El **PoS** es una **interfaz de TPV simplificada** que actúa como un **terminal de pago Bitcoin**.


Le permite :




- Crear un **menú de productos o servicios** con precios fijos.
- Genere una **factura instantánea con código QR** para escanear.
- Comparta una **URL de pago** accesible a través de smartphone, tableta u ordenador.



En otras palabras, PoS convierte su servidor BTCPay en una **interfaz de venta directa**, donde cada pago se recibe **en su propia Bitcoin wallet**, sin intermediarios.



### Configuración de PoS



En el panel de control de BTCPay, haga clic en **PLUGINS** y, a continuación, en **Punto de venta**.



A continuación, haga clic en **Crear una nueva aplicación PoS**. Esta acción añade una **nueva aplicación** a su tienda BTCPay, como si instalara un mini sitio de venta interno.



Se abre una página para crear su aplicación. Defina un **nombre de aplicación**: se trata de un nombre interno, visible únicamente desde su panel de control (por ejemplo, _Shoe Shop_).



Haga clic en **Crear** para validar.



![capture](assets/fr/24.webp)



Una vez creado, será redirigido a la **página de configuración detallada** del Punto de Venta.



### Personalice su interfaz de ventas



En esta página puede definir los elementos esenciales de su punto de venta:





- Nombre de la aplicación** (nombre de gestión interna, puede cambiarse en cualquier momento).





- Título de la pantalla** (lo que verán sus clientes en la parte superior de la página).





- Estilo de punto de venta** (el modo **Descripción** es adecuado para servicios como cortes de pelo o comidas, mientras que el modo **Catálogo de productos** es ideal para tiendas que ofrecen varios artículos).





- Divisa de visualización** (elija **XOF**, **EUR** o **USD** según sus precios habituales).





- Lista de productos** (añada aquí sus productos, descripciones y precios).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Guarda y prueba tu PoS



Cuando haya terminado de configurar, haga clic en **Guardar** para guardar la configuración y, a continuación, en **Ver** para obtener una vista previa de su TPV.



Verá una página de presentación de sus productos, en la que cada botón corresponde a un artículo o servicio.



En cuanto un cliente selecciona un producto :



1. BTCPay genera automáticamente una factura Bitcoin o Lightning**.



2. En la pantalla aparece un **código QR**.



3. Los clientes pueden **escanear y pagar directamente** con su Bitcoin wallet.




![capture](assets/fr/27.webp)



### Resultado final



Ahora dispone de un completo **Punto de Venta Bitcoin** que puede :





- Abrir desde un smartphone o tablet en su tienda ;





- Mostrar en una pantalla para que el cliente escanee ;





- O compártalo a través de una **URL** pública, como una página de pedidos simplificada.



Con cada pago, el importe se abona automáticamente en **su propio wallet de BTCPay**, sin intermediarios ni comisiones de terceros.


Esto convierte su TPV en un **terminal de pago Bitcoin autónomo**.




## Uso diario



Antes de cobrar cualquier pago real, le recomendamos que realice **una prueba** para comprobar que todo funciona correctamente.



### Probar un pago





- Cree una factura** desde su interfaz de TPV (por ejemplo, un producto de 1 satoshi o un importe pequeño).





- Escanee el código QR en pantalla** utilizando una Bitcoin o una wallet Lightning (como **Phoenix**, **Muun** o **Wallet de Satoshi**).




![capture](assets/fr/28.webp)





- Valide el pago** en su wallet: la transacción se envía al instante.





- Volver al servidor BTCPay**: la factura aparecerá como **Pagada** en la lista.



![capture](assets/fr/29.webp)



¡Enhorabuena! Su Punto de Venta ya es **funcional**. Ya puede empezar a recibir pagos Bitcoin de sus clientes, de forma sencilla, rápida y sin intermediarios.



### Crear una factura para un cliente



En el menú **Facturas**, haga clic en **Nueva factura**.



![capture](assets/fr/30.webp)



Introduzca el **importe** y la **moneda local** (BTCPay calcula automáticamente el equivalente en BTC), así como otra información sobre el producto.



![capture](assets/fr/31.webp)



Comparta el **código QR** o **URL** con el cliente.



![capture](assets/fr/32.webp)



### Seguimiento de los pagos recibidos



Siempre en el menú **Facturas**, verá una lista de todas sus transacciones.


Los estados posibles son :





- Pendiente**: pago aún no confirmado.





- Pagado**: pago confirmado.





- Caducada**: factura no pagada en la fecha de vencimiento.



### Reembolso a un cliente



En el menú **Facturas**, seleccione la factura que desea reembolsar.



![capture](assets/fr/33.webp)



Haga clic en **Reembolso** e introduzca la dirección Bitcoin facilitada por el cliente.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Informes y exportación de datos



BTCPay Server le permite **exportar sus transacciones** (en formato CSV o Excel). Esto es muy práctico para su contabilidad y seguimiento de caja.



![capture](assets/fr/36.webp)



En el menú **Informe**, haga clic en **Exportar**: todas sus transacciones se guardarán en un archivo CSV, que podrá consultar localmente.



## Seguridad y buenas prácticas



La autonomía que le confiere el servidor BTCPay (plena soberanía sobre sus fondos) es un verdadero punto fuerte. Pero esta libertad conlleva una mayor responsabilidad en términos de seguridad. Al gestionar sus propios pagos, usted asume el papel de su propio banco. Por eso es imperativo adoptar las mejores prácticas para proteger sus fondos, sus datos y su infraestructura. He aquí los principales puntos a tener en cuenta.



### Acceso seguro a su servidor





- Utilice una contraseña segura: combine mayúsculas y minúsculas, números y caracteres especiales. Evita reutilizar una contraseña ya existente.
- Active la autenticación de dos factores (2FA) para acceder a su interfaz BTCPay.
- Actualice regularmente su sistema operativo, su instancia de BTCPay Server y sus dependencias (Docker, nodo Bitcoin, nodo Lightning...). Las actualizaciones suelen corregir vulnerabilidades de seguridad.



### Gestión y copia de seguridad de claves privadas





- Guarde sus claves privadas y frases-semilla fuera de línea, en soportes físicos (papel o metal).
- Utilice preferentemente un wallet de hardware.
- Guarda varias copias de tus copias de seguridad, en ubicaciones físicas separadas y protegidas.



### Pagos seguros y confidencialidad





- Utilice la red Tor o una VPN para ocultar la dirección IP de su servidor y proteger su privacidad.
- Desactive los puertos innecesarios en su servidor y restrinja las conexiones SSH sólo a direcciones de confianza.
- Active HTTPS (certificado SSL) para todas las conexiones a su interfaz web BTCPay.
- Nunca comparta su interfaz de administración con personal no formado en la gestión de carteras Bitcoin.



### Aplicación de las mejores prácticas para la red Lightning



Su tienda está conectada a un **nodo Lightning alojado en Voltage**, lo que simplifica considerablemente la gestión técnica de la red. No obstante, sigue siendo importante adoptar **buenas prácticas de supervisión y seguridad**:





- Guarde las claves de acceso y de inicio de sesión API** de su nodo Voltage (que permiten la conexión de BTCPay).
- Proteja su cuenta de Voltage** con autenticación de dos factores y una contraseña segura.
- Supervise el estado de los nodos y canales** desde su panel de control de Voltage: esto le ayuda a detectar cualquier anomalía o desincronización.
- Evite compartir sus credenciales de API** o exponerlas públicamente (por ejemplo, en el código del sitio).
- En caso de migración, basta con **reconfigurar el enlace entre BTCPay y Voltage**: no es necesario cerrar manualmente ningún canal.



Con Voltage, usted se beneficia de una infraestructura **segura, de alta disponibilidad** y **con copias de seguridad automáticas**, al tiempo que conserva **la plena soberanía sobre sus pagos Lightning**.



### Organizar y estructurar los procedimientos internos





- Defina una política clara de gestión de accesos: quién puede crear una factura, ver los pagos, acceder al nodo, etc.
- Documente sus procedimientos de copia de seguridad y restauración para poder reaccionar rápidamente en caso de incidente.
- Prueba regularmente la restauración de tus copias de seguridad para asegurarte de que funcionan correctamente.
- Forme a su personal o colaboradores en seguridad operativa básica: vigilancia contra el phishing, uso de contraseñas seguras, respeto de la confidencialidad.



### Supervisar y establecer un mantenimiento continuo





- Supervise continuamente la actividad de su servidor mediante herramientas de registro o supervisión.
- Programe una revisión periódica de la seguridad: compruebe las actualizaciones, el acceso, las copias de seguridad y la coherencia de las transacciones.



¡Enhorabuena! Ha llegado al final de este tutorial. Ahora puede manejar BTCPay Server por su cuenta, lo que le facilitará la gestión de su tienda.



Para saber más, le recomiendo que siga nuestro completo curso de formación sobre la integración de Bitcoin en su empresa:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a
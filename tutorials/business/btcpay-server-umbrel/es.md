---
name: BTCPAY SERVER - Paraguas
description: Instalación y uso de BTCPAY SERVER en Umbrel para aceptar Bitcoin y Lightning
---

![cover](assets/cover.webp)



En el ecosistema Bitcoin, aceptar pagos representa un gran reto tanto para los comerciantes como para las empresas. Las soluciones tradicionales, ya sean bancarias (tarjetas de crédito, Stripe, PayPal) o incluso Bitcoin (BitPay, Coinbase Commerce), imponen intermediarios que cobran comisiones sustanciales, recopilan tus datos comerciales confidenciales y pueden BLOCK o censurar tus transacciones a su antojo. Esta dependencia es contraria a los principios fundamentales de Bitcoin de descentralización, confidencialidad y soberanía financiera.



BTCPAY SERVER se perfila como la respuesta de código abierto a este problema. Este procesador de pagos autoalojado convierte tu propio nodo Bitcoin en una infraestructura profesional, sin intermediarios, sin tarifas de procesamiento adicionales y sin comprometer la privacidad. Desarrollado por una comunidad global de colaboradores desde 2017, BTCPAY SERVER te permite recibir pagos de Bitcoin y Lightning directamente en tus monederos, conservando el control total de tus fondos en todo momento.



Tradicionalmente, la instalación de BTCPAY SERVER requiere conocimientos técnicos avanzados: Configuración de servidores Linux, dominio de Docker, gestión de certificados SSL y seguridad de red. Umbrel revoluciona este enfoque con una instalación de un solo clic directamente integrada con sus Bitcoin y LIGHTNING NODE. Esta simplificación pone al alcance de todos lo que antes estaba reservado a técnicos experimentados.



**Importante entender**: BTCPAY SERVER en Umbrel funciona por defecto sólo en tu red local. Puedes crear facturas, aceptar pagos Lightning y Bitcoin, y gestionar tu contabilidad desde cualquier dispositivo conectado a tu red local (ordenador, smartphone, tablet). Esta configuración es ideal para facturar servicios presenciales, gestionar pagos presenciales o utilizar BTCPAY SERVER desde tu red local. Por otro lado, para integrar BTCPAY SERVER en una tienda online de acceso público en Internet, será necesaria una configuración adicional con exposición pública (trataremos este tema al final del tutorial).



Este tutorial le lleva a través de la instalación completa de BTCPAY SERVER en Umbrel, la configuración de su Bitcoin Wallet y LIGHTNING NODE, la creación y el pago de facturas, y la gestión de informes de contabilidad. Descubrirá cómo utilizar BTCPAY SERVER de forma eficaz en su red local y, a continuación, hablaremos de soluciones para su visualización pública si desea integrarlo con un sitio de comercio electrónico.



## Requisitos previos



Para seguir este tutorial, necesitas tener Umbrel correctamente instalado y configurado. Si aún no lo has hecho, consulta nuestro tutorial sobre la instalación de Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Su nodo Bitcoin core debe estar totalmente sincronizado con Blockchain (100% en la aplicación Bitcoin de Umbrel). Esta sincronización inicial suele tardar entre 3 días y 2 semanas, dependiendo de su hardware y conexión a Internet.



Para aceptar pagos instantáneos con Lightning, también tendrás que instalar LND (Lightning Network Daemon) en Umbrel. Consulte nuestro tutorial sobre la instalación y configuración de LND en Umbrel si desea activar esta función.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Deje al menos 50 GB de espacio libre en disco para BTCPAY SERVER, sus bases de datos y los datos de Lightning. Se recomienda encarecidamente una conexión estable a Internet mediante cable Ethernet para evitar desconexiones.



## Instalación de BTCPAY SERVER en Umbrel



Desde Umbrel Interface (`umbrel.local`), vaya a la App Store y busque "BTCPAY SERVER" en la categoría Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Haga clic en Instalar. Umbrel comprueba automáticamente que Bitcoin core y LND están instalados y, a continuación, inicia el despliegue (2-5 minutos).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Una vez instalada, abre la aplicación. Tendrás que crear una cuenta de administrador con credenciales sólidas.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Una vez creada su cuenta, BTCPAY SERVER le pedirá inmediatamente que cree su primera tienda. Elija un nombre profesional y seleccione una moneda de referencia (EUR, USD o BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Acceda a BTCPAY SERVER en su red local



BTCPAY SERVER es accesible desde cualquier dispositivo de su red local (WiFi o Ethernet). Accede desde tu navegador a :



```url
http://umbrel.local
```



O directamente a :



```url
http://umbrel.local:3003
```



**Acceso remoto con Tailscale**: Para acceder a BTCPAY SERVER desde cualquier parte del mundo, utiliza Tailscale. Esta VPN segura te permite conectarte a tu Umbrel como si estuvieras en tu red local. Consulte nuestro tutorial dedicado a Tailscale en Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Configuración de su cartera Bitcoin



Para aceptar pagos, es necesario configurar una Bitcoin Wallet. BTCPAY SERVER muestra las opciones de configuración en el panel de control.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Para configurar Wallet Bitcoin, vaya a "Carteras" > "Bitcoin".



Tiene dos opciones: crear una nueva cartera directamente en BTCPay, o importar una cartera existente. Para la importación, hay varios métodos disponibles:




- Conectar Hardware Wallet** (recomendado): Importa tus claves públicas a través de la aplicación Vault
- Importar archivo Wallet** (recomendado): Cargue un archivo exportado de su cartera
- Introduzca la clave pública extendida**: Introduzca su XPub/YPub/ZPub manualmente
- Escanear código QR de Wallet** : Escanea un código QR desde BlueWallet, Cobo Vault, Passport o Specter DIY
- Introduzca Wallet seed** (no recomendado) : Introduzca su frase de recuperación de 12 o 24 palabras



![Options de création de portefeuille](assets/fr/06.webp)



Para este tutorial, vamos a crear una nueva Hot Wallet: la clave privada se almacenará por tanto en nuestro servidor Umbrel. En este caso, le aconsejamos encarecidamente que traslade los fondos regularmente a una Cold Wallet para evitar almacenar grandes cantidades en el servidor.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Una vez configurado, BTCPAY SERVER confirma que su Wallet está listo para aceptar pagos On-Chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Activar Lightning Network



Para aceptar pagos instantáneos con Lightning, ve a Monederos > Lightning. A continuación, como tu nodo LND ya está instalado en Umbrel, solo tienes que hacer clic en el botón "Guardar" para validar la conexión entre tu BTCPAY SERVER y tu LIGHTNING NODE.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Crear y pagar facturas



En Interface BTCPAY SERVER, vaya a Facturas > Crear Invoice. Introduzca el importe, añada una descripción opcional y haga clic en Crear.



![Création d'une nouvelle facture](assets/fr/10.webp)



A continuación, puede hacer clic en el botón "Checkout" para visualizar la Invoice. BTCPay genera entonces una Invoice con un código QR unificado (BIP21) que contiene la Bitcoin Address y la Invoice Lightning.



![Détails de la facture générée](assets/fr/11.webp)



Su cliente puede escanear el código QR con cualquier Wallet compatible.



![Page de paiement avec QR code](assets/fr/12.webp)



Una vez pagado, el Invoice se "Liquida" en cuestión de segundos para el Rayo.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Gestión y seguimiento de pagos



En la sección "Informes", pestaña "Facturas", encontrará un historial completo de sus facturas, con fecha, importe, estado y forma de pago. Si lo desea, puede exportarlo.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Configuración de la tienda



BTCPAY SERVER le permite gestionar varias tiendas con parámetros distintos. Cada tienda representa una entidad empresarial independiente: tienda de comercio electrónico, punto de venta físico o facturación de servicios.



En los ajustes de la tienda, encontrará varias secciones importantes:



![Paramètres du magasin](assets/fr/15.webp)





- Configuración general**: Nombre de la tienda, moneda de referencia (BTC, EUR, USD), tiempo de caducidad de Invoice (por defecto 15 minutos), número de confirmaciones de Blockchain necesarias
- Tarifas**: Configuración de fuentes de tipos Exchange y conversiones fiat/Bitcoin
- Aspecto del pago**: Personaliza la apariencia de tus páginas de pago (logo, colores, mensajes personalizados)
- Configuración de correo electrónico**: Configuración de las notificaciones por correo electrónico de los pagos recibidos
- Tokens de acceso**: API Gestión de token para integraciones de comercio electrónico (WooCommerce, Shopify, etc.)
- Usuarios**: Gestionar el acceso de usuarios a la tienda con diferentes niveles de permisos (Propietario, Invitado)
- Webhooks**: Configuración de Webhooks para la sincronización en tiempo real con su sistema de contabilidad o ERP



BTCPAY SERVER también ofrece una sección de plugins para ampliar la funcionalidad con integraciones de comercio electrónico, sistemas de punto de venta y herramientas adicionales.



![Gestion des plugins](assets/fr/16.webp)



## Ventajas y limitaciones del uso local



**Beneficios de BTCPAY SERVER en Umbrel** :




- Soberanía total: control exclusivo de las claves privadas y los fondos, ningún tercero puede congelar o censurar sus pagos
- Ahorro sustancial: sólo Bitcoin de costes de red (unos céntimos en Lightning) frente al 2-3% de los procesadores tradicionales
- Máxima confidencialidad: sin registro, verificación de identidad ni intercambio de datos con terceras empresas
- La arquitectura de código abierto garantiza la transparencia, auditabilidad y sostenibilidad a través de una amplia comunidad de desarrolladores
- Fácil instalación a través de Umbrel, sin necesidad de conocimientos técnicos avanzados



**Limitaciones importantes** :




- Sólo red local**: BTCPAY SERVER en Umbrel sólo es accesible desde su red doméstica. Perfecto para facturación presencial, servicios de autónomos o pequeños negocios físicos, pero inadecuado para tiendas online de acceso público en Internet.
- Responsabilidad técnica total: mantenimiento de nodos, copias de seguridad periódicas, supervisión de la conectividad
- Gestión de la liquidez de los rayos: apertura y gestión de canales con suficiente capacidad de entrada
- Soporte limitado a la documentación y foros de la comunidad, lo que requiere más autonomía que un departamento comercial de atención al cliente



Esta limitación de LAN es el principal obstáculo para integrar BTCPAY SERVER en una tienda de comercio electrónico, donde los clientes necesitan poder acceder a las páginas de pago desde cualquier lugar de Internet.



## Buenas prácticas y seguridad



Activa las copias de seguridad automáticas de Umbrel y guarda una copia en un soporte externo (memoria USB, disco Hard, nube cifrada). Guarde sus semillas Bitcoin (frases de recuperación) en un lugar seguro y físicamente separado. Guarda el archivo channel.backup de LND para la recuperación de Lightning.



Supervise regularmente la sincronización de Bitcoin core, los canales Lightning y la respuesta de BTCPAY SERVER. Una simple prueba semanal: generate y pagar una factura de unos cuantos satoshis. Mantén Umbrel actualizado (parches de seguridad, mejoras). Haga una copia de seguridad antes de actualizaciones importantes. Para uso profesional, considere la monitorización externa (UptimeRobot) con alertas por correo electrónico/SMS.



## Mostrar BTCPAY SERVER públicamente para una tienda online



Para integrar BTCPAY SERVER en una tienda de comercio electrónico basada en web (WooCommerce, Shopify, etc.), sus clientes necesitan poder acceder a las páginas de pago desde cualquier lugar, no sólo desde su red local.



**Solución: Nginx Proxy Manager**



Puede exponer BTCPAY SERVER públicamente utilizando Nginx Proxy Manager (disponible en Umbrel App Store). Esta solución requiere :




- Un nombre de dominio (clásico o gratuito a través de DuckDNS, No-IP, Afraid.org)
- Configuración del reenvío de puertos (puertos 80 y 443) en el router
- Instalación de Nginx Proxy Manager, que gestiona automáticamente los certificados SSL



Esta configuración expone su servidor a Internet y requiere una vigilancia adicional (contraseñas seguras, 2FA, actualizaciones regulares). Vamos a preparar un tutorial dedicado detallando este procedimiento completo.



## Conclusión



BTCPAY SERVER on Umbrel combina la potencia del nodo Bitcoin con la sencillez de Umbrel para crear una infraestructura de pago profesional autoalojada y accesible para todos. Esta soberanía financiera conlleva una responsabilidad de mantenimiento, pero Umbrel simplifica enormemente la carga operativa en comparación con los beneficios: eliminación de las tasas de procesamiento, protección de tu privacidad, resistencia a la censura y control total de tus fondos.



El uso de la red local cubre ya un amplio abanico de aplicaciones: facturación de servicios de autónomos, pagos presenciales, pequeñas tiendas físicas, o simplemente aprender y experimentar con Bitcoin y Lightning en un entorno controlado. Para necesidades de comercio electrónico que requieran exposición pública, existe la solución Nginx Proxy Manager, pero requiere una configuración técnica adicional, que detallaremos en un tutorial dedicado.



Tanto si diriges un negocio, un proyecto incipiente o simplemente estás experimentando, BTCPAY SERVER en Umbrel te ofrece total autonomía financiera. El camino comienza con una primera tienda, un primer Invoice, un primer pago recibido directamente en tu infraestructura soberana.



## Recursos



### Documentación oficial




- [Sitio web oficial de BTCPAY SERVER](https://btcpayserver.org)
- [Documentación completa del BTCPAY SERVER](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Documentación de Tailscale](https://tailscale.com/kb)


### Comunidad y apoyo




- [Foro BTCPAY SERVER](https://chat.btcpayserver.org)
- [Paraguas del Foro](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)
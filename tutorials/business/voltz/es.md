---
name: Voltz
description: El Lightning wallet todo en uno para su empresa.
---

![cover](assets/cover.webp)



La idea de la plataforma Voltz surgió de un grupo de bitcoiners que querían ofrecer su propio servicio wallet de bitcoin. El resultado fue una infraestructura completa para aceptar bitcoin en comercios. En este tutorial, te llevamos a conocer Voltz y las posibilidades de integración de bitcoin que ofrece la plataforma.



## Primeros pasos con Voltz



Más allá de ser un Lightning wallet de custodia que te permite enviar, recibir y pagar diariamente, Voltz es una plataforma completa que proporciona numerosas extensiones para integrar bitcoin como punto de venta o marketplace en tu negocio.



Vaya a la plataforma [Voltz] (https://www.voltz.com/en) y cree una cuenta haciendo clic en el botón "Probar ahora".



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Es importante establecer una contraseña alfanumérica fuerte para aumentar tus posibilidades contra los ataques de fuerza bruta, y comprueba que estás realmente en el sitio web oficial de Voltz para rellenar tus datos de acceso para protegerte contra el phishing.



La interfaz de Voltz es muy similar a la de la plataforma LnBits.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz está de hecho construido sobre un servidor LnBits; echa un vistazo a nuestro tutorial para aprender a montar tus propios servidores LnBits y construir tus soluciones sobre ellos.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

La plataforma le permite gestionar eficazmente varias carteras. Por defecto, cuando te registras, tienes automáticamente una cartera Lightning. Sin embargo, puedes añadir otras carteras.



![wallets](assets/fr/03.webp)



### Portabilidad



Voltz no se limita a una interfaz web: en la sección **Acceso móvil**, puede conectar su Voltz wallet activo a aplicaciones como Zeus o Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Para ello, es necesario instalar y activar la extensión **LndHub** en la plataforma.



![lndhub](assets/fr/04.webp)



Seleccione su cartera Voltz activa y, en función de los derechos que desee conceder, escanee el código QR correspondiente.




- El código QR de la factura sólo le permite leer el historial de su cartera y generate nuevas facturas.
- El código QR del administrador le permite ver el historial, las facturas de generate y también pagar las facturas relámpago.



![qrs](assets/fr/05.webp)



En este tutorial, conectamos nuestro Voltz wallet a la aplicación Blue Wallet.



![connect](assets/fr/06.webp)



Una vez conectada nuestra cartera, todas las acciones realizadas se sincronizarán entre Blue Wallet y Voltz. Por ejemplo, cuando generate una factura en Blue Wallet, también tendrá un historial en Voltz.



![sync](assets/fr/07.webp)



En la sección **Configuración de la cartera**, encontrará parámetros mínimos como la personalización del nombre de la cartera y la moneda en la que desea recibir sus pagos.



![config](assets/fr/08.webp)



### Extensiones



Una de las características especiales de la plataforma Voltz es su modularidad, que le permite activar las extensiones que necesite. La lista de extensiones se encuentra en el menú **Extensiones**.



![extensions](assets/fr/09.webp)



Entre estas extensiones se encuentra el TPoS, un terminal de punto de venta que puede utilizar para llevar un inventario y cobrar los pagos de sus clientes.



![tpos](assets/fr/10.webp)



Desde el Terminal Punto de Venta, puede :




- Consiga una página web que pueda compartir con sus clientes y socios;
- Gestionar el inventario de productos;
- Generar facturas Lightning;
- Pagos en efectivo mediante tarjetas Bolt.



La extensión está disponible como versión gratuita y como versión de pago para funciones más avanzadas. Para crear un TPV, haga clic en el botón **Abrir** situado debajo del logotipo de la extensión y, a continuación, haga clic en **Nuevo TPV**.



![new_tpos](assets/fr/11.webp)



Defina el nombre de su punto de venta y, a continuación, conecte su Voltz wallet a su terminal para cobrar los pagos. Puede activar las propinas marcando la casilla **Activar propinas**. Active también la opción de impresión de facturas si desea emitir recibos a sus clientes (esta funcionalidad está aún en desarrollo, por lo que puede haber fallos de funcionamiento).



El terminal punto de venta también incluye la configuración de impuestos cuando desee aplicar el impuesto de su país directamente a sus productos.



![tpos](assets/fr/12.webp)



Una vez creado su terminal punto de venta, puede añadir productos y servicios preconfigurados para garantizar una experiencia de pago y contabilidad fluida para usted y sus clientes.



![product](assets/fr/13.webp)



Crea tus productos definiendo su nombre, añadiendo una imagen y fijando un precio de venta.  Puede categorizar sus productos para facilitar su seguimiento. Puede aplicar impuestos directamente a un producto específico. Si el producto no tiene ningún impuesto aplicado, se aplicará automáticamente el impuesto configurado en la fase de creación del terminal punto de venta.



![products](assets/fr/14.webp)



Puede importar automáticamente su lista de productos desde un formato JSON haciendo clic en el botón **Importar/Exportar**.



![exports](assets/fr/15.webp)



Acceda a la zona de caja a través del enlace haciendo clic en el icono **Nueva pestaña**, o comparta su plataforma TPV a través de código QR con sus clientes haciendo clic en el icono **Código QR**.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Sus clientes pueden consultar su catálogo y realizar el pago desde esta interfaz.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



En el grupo de extensiones disponibles, también encontrará herramientas como las extensiones **Invoice** y **Payment Link**, que le permiten generate facturas con productos específicos para cobrar pagos aislados sin pasar por el terminal de punto de venta.



## Controle sus pagos



En el menú **Pagos**, Voltz le ofrece una visión general de los pagos efectuados a sus distintas carteras.


Puede seguir sus pagos por :




- Estado.
- La etiqueta: por ejemplo **TPOS** para pagos en puntos de venta y **lnhub** a través de la conexión móvil en los monederos Zeus y Blue Wallet.
- La cartera de la colección.
- Total de pagos recibidos y efectuados.
- Un periodo bien definido.



![payments](assets/fr/22.webp)



## Más opciones



Voltz es también una infraestructura sobre la que puedes construir tus propias soluciones. En la sección **Extensiones** encontrará una guía para desarrollar sus propias extensiones dentro del ecosistema de Voltz y LnBits.



![build](assets/fr/23.webp)



En caso de que quieras desarrollar soluciones fuera del ecosistema pero seguir utilizando su infraestructura, en la sección **URL del nodo** encontrarás claves API e información sobre documentación con un ejemplo de lo que puedes hacer con estos datos.



Puede crear facturas Lightning desde sus aplicaciones utilizando su Voltz wallet, pagar facturas Lightning, descodificar y verificar facturas.



![keys](assets/fr/24.webp)



Ahora ya tienes un buen conocimiento de Voltz. Si te ha gustado este tutorial, estamos seguros de que aprenderás más sobre los mejores métodos y herramientas para integrar bitcoin en tu negocio con nuestro curso: Bitcoin para empresas.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a
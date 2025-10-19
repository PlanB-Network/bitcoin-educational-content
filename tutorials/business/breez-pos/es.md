---
name: Breez - TPV
description: Breez facilita el cobro de pagos Bitcoin para su empresa.
---

![cover](assets/cover.webp)



Desde la pandemia del COVID-19, los pagos digitales sin contacto se han generalizado, incluso en los comercios más pequeños. Durante este periodo, muchos comercios han descubierto la utilidad de las soluciones de efectivo Bitcoin, que les permiten recibir pagos de todo el mundo. Sin embargo, estas soluciones son a veces difíciles de usar o inadecuadas para los pequeños comercios. En este tutorial, vamos a echar un vistazo a la terminal de pago Breez, una solución que destaca por su facilidad de uso, mientras que le da un control total sobre la gestión de sus bitcoins.



## Instalar Breez POS



Breez POS es un servicio de autocustodia proporcionado por la Wallet de Breez. La utilidad de este servicio es permitir a los comerciantes cobrar pagos a través de Bitcoin permaneciendo en una simple Interface, muy similar a las diversas carteras Lightning. Breez POS está disponible en las plataformas de descarga [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) y [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS).



![download](assets/fr/01.webp)



![setup](assets/fr/12.webp)



⚠️ Es importante tener en cuenta que estas aplicaciones están aún en fase de desarrollo y que puede haber algunos errores en el uso de las funcionalidades. Recomendamos un uso moderado.



Con esta aplicación, Breez te ofrece un control total sobre las configuraciones de red y los ajustes de tarifas, al tiempo que garantiza tu soberanía en la gestión de tus bitcoins.



Puede explorar las distintas opciones de la Wallet de Breez siguiendo nuestro tutorial a continuación. Este paso le ayudará a comprender mejor el ecosistema del punto de venta y a adoptar las mejores prácticas para asegurar de forma eficaz los bitcoins asociados a su seed.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Uso de Breez POS



En este tutorial, nos centraremos en la sección "*Punto de venta*" para ayudarte a entender cómo integrarlo como medio de pago en tu negocio.



El punto de venta es parte integrante de la cartera de Breez y se basa principalmente en la Lightning Network para cobrar los pagos.



En el menú "*Punto de venta*" encontrará un Interface para cobrar los pagos. Se divide en dos partes:



### Domiciliación bancaria



La primera parte es el teclado de domiciliación bancaria. Este Interface es práctico para cobrar un único pago cuando conoces las compras totales de tus clientes, o cuando no necesitas un catálogo fijo de productos en tu negocio (por ejemplo, servicios de autónomos).



![keyboard](assets/fr/02.webp)



Para utilizar el TPV de Breez por primera vez, tendrás que reunir un pago de más de 2.500 satoshis (unos 3 euros al cambio actual de Exchange). Esta cantidad, que sólo se paga en tu primer cobro, representa el coste de crear un canal de pago para que puedas comunicarte con otros nodos de Lightning Network y enviar y recibir satoshis.



![channel_fee](assets/fr/03.webp)


### Catálogo de productos



La segunda parte es el catálogo de productos. Este Interface es ideal cuando se dispone de un catálogo de productos con precios predefinidos. Aquí puede preconfigurar sus productos y luego utilizarlos para generate facturas para mejorar la trazabilidad de sus ingresos en efectivo.



![items](assets/fr/04.webp)



Puede configurar manualmente cada artículo de este Interface haciendo clic en el botón "**Plus**" y definiendo a continuación el nombre, el precio y un identificador para este artículo.



![add_items](assets/fr/05.webp)



A continuación, puede añadirlo y definir su cantidad para cobrar el pago asociado.



Cuando su catálogo es bastante grande, puede resultar complicado añadir sus productos uno a uno. Para ello, en la sección **Preferencias > Configuración del punto de venta**, desde el menú "Lista de artículos", puede importar y exportar automáticamente su lista de artículos desde archivos CSV.



![import](assets/fr/07.webp)



En esta misma sección, puede definir el periodo de validez de sus facturas Lightning. A partir de ahora, para todas tus facturas, tus clientes tienen `N` segundos para realizar el pago, de lo contrario tendrás que volver a generar una nueva Invoice Lightning.



![invoice_time](assets/fr/08.webp)



Como gestor, puedes reforzar la seguridad de tus bitcoins añadiendo una contraseña que será necesaria para todos los pagos salientes de tu Wallet. Esta función es especialmente útil cuando no eres el único que gestiona tu punto de venta.



![manager](assets/fr/09.webp)



En el menú **Transacciones**, encontrará una lista de todos los pagos que ha cobrado. También puedes filtrar los resultados por un periodo concreto pulsando el botón **Calendario**.



![transactions](assets/fr/10.webp)



También puede ver un resumen diario de sus ventas y el importe total recaudado haciendo clic en el botón **Documento**.



![summary](assets/fr/11.webp)



Ahora ya conoces a fondo el punto de venta que ofrece la aplicación Breez para integrar Bitcoin en tu negocio sin problemas. Si te ha resultado útil este tutorial, te recomendamos nuestro tutorial sobre be-BOP, una plataforma de comercio electrónico que te permite aceptar pagos en bitcoins y monetizar tu negocio.



https://planb.network/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa
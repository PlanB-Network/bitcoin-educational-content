---
name: Solución de compra-venta de Bitcoin peer-to-peer
goal: Explorar soluciones de compra y venta de Bitcoin sin KYC
objectives:
  - Comprender los diferentes tipos de KYC, sus riesgos y beneficios
  - Comprender las ventajas de una compra peer-to-peer
  - Implementar la solución que se adapte a sus necesidades
  - Mejorar la gestión de sus UTXO (KYC y no KYC)
---

# Un viaje al mundo sin KYC

Pierre nos propone este curso que nos sumerge en las diferentes soluciones existentes para comprar y vender bitcoins peer-to-peer. La compra peer-to-peer es completamente legal y permite tener más anonimato, ya que estas soluciones no tienen KYC. El KYC (Know Your Customer) es una regla de los reguladores de mercados (AMF) que consiste en pedir la identificación al cliente que desea comprar o vender bitcoins. Estas reglas tienen como objetivo evitar el lavado de dinero, el financiamiento del terrorismo y la evasión fiscal. A riesgo de importantes consecuencias para el usuario, el KYC tiene como objetivo defender y proteger a su usuario, aunque muy a menudo se observa el efecto contrario.

Por lo tanto, exploraremos los diferentes tipos de KYC (los full KYC tipo Francia, los KYC Light tipo Suiza y los no KYC tipo peer-to-peer). Pierre nos presentará más de 6 soluciones, por lo que tendrás todas las cartas en la mano para descubrir cuál te corresponde. Si deseas una solución KYC, ten en cuenta que están presentes en la formación BTC 102.

+++

# Introducción


## Explicación y tipo de KYC

El KYC, para "Know Your Customer" (Conoce a tu cliente), es una norma regulatoria que requiere la recopilación de información privada de los clientes, como su dirección física, su identificación o sus extractos bancarios. Esta práctica es común en las plataformas de corretaje, que pueden solicitar un KYC completo, que incluye información detallada como una identificación, una foto, un comprobante de domicilio, hojas de salario, etc.

El objetivo principal del KYC es combatir el lavado de dinero, el financiamiento del terrorismo y la evasión fiscal. Es una ley establecida por la AMF (Autoridad de los Mercados Financieros), el organismo regulador del mercado francés. Sin embargo, la aplicación del KYC conlleva la centralización de bases de datos muy sensibles que contienen información personal de los usuarios. Esta información, que tiene cierto valor, puede ser vendida a entidades malintencionadas.

En adición, las plataformas de intercambio a menudo solicitan una cantidad excesiva de información personal, poniendo en peligro a los usuarios y aumentando los costos de cumplimiento. Estos costos regulatorios pueden desalentar a las empresas francesas y perjudicar su competitividad a nivel internacional.

Existen tres tipos de KYC, incluyendo el KYC completo que requiere una recopilación completa y regulada de información para acceder al servicio. En Suiza, una alternativa llamada "KYC light" permite la compra y venta de bitcoins sin proporcionar una identificación, siempre y cuando el monto de compra no supere los 1000 euros por día. Soluciones como Relay permiten utilizar este método.

En este marco, las autoridades suizas pueden acceder a la información bancaria para investigar a las personas consideradas de riesgo. Las direcciones de entrega de bitcoins también son rastreables a través del sistema bancario. El KYC light generalmente se considera más simple y menos costoso que el sistema francés.

En Francia, la compra de bitcoins en línea requiere el envío de dinero a un tercero, por transferencia SEPA o Paypal. Para aquellos que prefieren el anonimato, la seguridad y la privacidad, también están disponibles soluciones de compra de bitcoins en efectivo. Para volúmenes bajos, la compra de bitcoins en efectivo es una opción simple y legal.

Para poder vender diariamente PLT de 100 euros de bitcoin a cualquier persona, se requiere regulación por parte de la AMF (Autorité des Marchés Financiers). En Francia, esta regulación se aplica principalmente a particulares que realizan grandes volúmenes de transacciones. Los otros dos métodos de compra de bitcoin incluyen el uso de cajeros automáticos (ATM) y los intercambios entre amigos. Los ATM están regulados y requieren una identificación para transacciones superiores a 500 euros. El intercambio entre amigos, por otro lado, ofrece una exposición discreta al bitcoin.
Estas medidas regulatorias están en su lugar para contrarrestar el financiamiento del terrorismo, la evasión fiscal y el lavado de dinero. El bitcoin, como base de datos completamente rastreable, hace que el lavado de dinero sea particularmente difícil. El uso de Bitcoin por parte de los delincuentes puede ser rastreado, lo que hace que Bitcoin sea una herramienta poco efectiva para el lavado de dinero.

Es importante tener en cuenta que esta formación presenta diversas alternativas, así como herramientas que pueden ser utilizadas con fines malintencionados o no. Además, ofrece explicaciones sobre el funcionamiento de los libros de órdenes entre los creadores de mercado y los tomadores de órdenes.

También es importante tener en cuenta que la información presentada aquí no respalda ninguna solución en particular. Simplemente se trata de presentar las opciones disponibles para una mejor comprensión del tema. Para cualquier pregunta adicional sobre Bitcoin, no dude en consultar recursos en línea como www.découvrebitcoin.com.

## Comparativa de soluciones de compra-venta peer-to-peer

Soluciones P2P para la compra de Bitcoin: Bisq, RoboSat, LNP2PBot, Peach y HodlHodl

La compra de Bitcoin peer-to-peer (P2P) es una opción preferida para los inversores que desean evitar las plataformas de intercambio centralizadas. Esta parte del curso examina diferentes soluciones P2P disponibles, incluyendo Bisq, RoboSat, LNP2PBot, Peach y HodlHodl.
Comparativa de ventajas e inconvenientes de las diferentes soluciones

Cada solución P2P tiene sus propias ventajas e inconvenientes. A continuación, ofrecemos una visión general de las características clave de cada solución.

### Bisq

[Bisq](https://bisq.network/) es una solución P2P no custodial que cuenta con un sistema DAO (Organización Autónoma Descentralizada) y utiliza el multisign para la gestión de disputas. Su código es de código abierto, lo que contribuye a su robustez y a la protección de la privacidad de los usuarios.

| Ventajas                                     | Inconvenientes                                                                                      |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| - Solución P2P, no custodial, multisign, DAO | - La aplicación es bastante pesada y no muy amigable, solo disponible en ordenador                  |
| - Robusta y segura                           | - Las limitaciones de compra y venta, así como la gestión de cuentas con firmas, son de doble filo. |
| - Código abierto                             |                                                                                                     |

### RoboSat

[RoboSat](https://learn.robosats.com/) es una solución fácil de usar, rápida, que funciona con TOR y no requiere una cuenta. Es de código abierto y utiliza la Lightning Network para permitir transacciones rápidas.

| Ventajas                                                  | Inconvenientes                                                             |
| --------------------------------------------------------- | -------------------------------------------------------------------------- |
| - Fácil de usar                                           | - El protocolo es frágil con un solo coordinador                           |
| - Bajos costos de transacción                             | - Requiere conocimientos técnicos y comprensión de la privacidad           |
| - Utiliza la Lightning Network para transacciones rápidas | - La aplicación Umbrell permite administrar su propia instancia de cliente |
| - Código abierto                                          |                                                                            |

### LNP2PBot

[LNP2PBot](https://lnp2pbot.com/) es accesible a través de Telegram para la compra de Bitcoin sin KYC. Ofrece transacciones rápidas gracias a la Lightning Network y bajos costos de transacción.

| Ventajas                                                         | Inconvenientes                                                 |
| ---------------------------------------------------------------- | -------------------------------------------------------------- |
| - Accesible a través de Telegram                                 | - Menos robusto y seguro que otras soluciones                  |
| - Rapidez gracias a la Lightning Network                         | - Menos rápido y menos amigable que Robosat                    |
| - Bajos costos de transacción                                    | - Puede estar vinculado a la identidad de Telegram del usuario |
| - Gestión de disputas internamente                               | - Falta de liquidez y fragilidad de la aplicación              |
| Propuestas comunitarias para limitar el problema de la confianza | Hay que confiar en LNP2Pbot para gestionar los litigios        |

### Peach

[Peach](https://peachbitcoin.com/) es una aplicación móvil dedicada al trading de Bitcoin. Se distingue por su simplicidad, no requiere la creación de una cuenta para operar. Las transacciones son rápidas, incluso sin Lightning Network. Además, las notificaciones en los teléfonos aceleran el proceso de transacción.

| Ventajas                                                      | Desventajas                                                                                                                    |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| - Uso simplificado: no se requiere la creación de una cuenta. | - Seguridad y robustez: al estar vinculada a una empresa, Peach presenta posibles debilidades en seguridad.                    |
| - Velocidad de transacción: los intercambios son rápidos.     | - Ausencia de Lightning Network: esta tecnología, que permite transacciones de Bitcoin más rápidas, no es utilizada por Peach. |
| - Notificaciones: aceleran el proceso de transacción.         |                                                                                                                                |

### HodlHodl

[HodlHodl](https://hodlhodl.com/) es una solución no custodial para el intercambio de Bitcoin. Ofrece muchas ventajas como una gran liquidez, la posibilidad de intercambios privados, un sistema de referidos, así como cuentas con historial de intercambio y un sistema de calificación. Sin embargo, los intercambios están vinculados a la dirección de correo electrónico y la identidad digital del usuario, almacenados en HodlHodl. Además, el código fuente de HodlHodl no está abierto al público y la aplicación no se puede utilizar con Tor.

| Ventajas                                                                                                                         | Desventajas                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| - No custodial: el usuario mantiene el control de sus claves privadas.                                                           | - Almacenamiento de información personal: la dirección de correo electrónico y la identidad digital del usuario se almacenan en HodlHodl. |
| - Liquidez: HodlHodl ofrece una amplia gama de posibilidades de intercambio.                                                     | - Código fuente cerrado: el código de HodlHodl no está abierto al público.                                                                |
| - Posibilidad de intercambios privados: el usuario puede elegir con quién intercambiar.                                          | - Incompatibilidad con Tor: HodlHodl no se puede utilizar con esta red centrada en la privacidad.                                         |
| - Sistema de referidos: HodlHodl recompensa el boca a boca.                                                                      | - Posibilidad de KYC forzado: en algunas situaciones, HodlHodl puede exigir información de identificación para recuperar fondos.          |
| - Historial de intercambio y sistema de calificación: estas características permiten evaluar la confiabilidad de otros usuarios. |                                                                                                                                           |

## Conclusión sobre las soluciones P2P

En resumen, cada solución P2P tiene sus ventajas e inconvenientes. Bisq se considera la más robusta y segura, pero menos accesible. RoboSat es de código abierto pero menos robusta que Bisq. LNP2PBot es menos robusta y segura que otras soluciones, menos rápida y menos amigable que RoboSat, pero más que Bisq. Peach es la aplicación más fácil y rápida para comprar Bitcoin sin KYC, pero una empresa está detrás, por lo que hay debilidades en términos de seguridad y robustez. HodlHodl es un protocolo gestionado por una empresa y cerrado, por lo que hay debilidades en términos de seguridad y robustez, y es un poco más complicado que Peach.

El buen y viejo efectivo en persona sigue siendo una solución para pequeñas cantidades.

Además de las soluciones P2P, existen otras opciones de intercambio de criptomonedas. kycnot.me ofrece servicios como VPN, VPS, SMS, etc. Bitrefil permite comprar tarjetas de regalo. Cada solución en [kycnotme](https://kycnot.me/) se presenta con sus puntos positivos y negativos.

# Tutoriales sobre soluciones de compra/venta P2P

## Robosats

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/) es un proyecto de código abierto desarrollado por Reckless Satoshi para intercambiar Bitcoins de forma privada por monedas nacionales. Simplifica la experiencia peer-to-peer y utiliza facturas Lightning para minimizar las necesidades de custodia y confianza. Para usarlo, necesitaremos Tor, una red de comunicación anónima.

Lo primero que debemos hacer es descargar Tor. Puede encontrarlo en GitHub o directamente en el sitio oficial en la siguiente dirección: tor.org/download.
Una vez que Tor esté descargado e instalado:

- Presione "Conectar" para establecer la conexión.
- Vaya a la [dirección onion de robosats](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/).
- Copie el token para guardar su identidad.

Aquí están los pasos para comprar bitcoins con Robosats:

- Consulte el libro de órdenes, puede filtrar por moneda y método de pago, por ejemplo, comprar bitcoin en euros con Revolut.
- Antes de comprar, verifique la caducidad de la oferta, el precio en euros y el premium (también puede filtrar las ofertas por premium).
- Preferiblemente, elija una oferta con un usuario activo y con un premium inferior al promedio.
- Verifique el resumen del pedido con el monto, el método de pago, el premium, el ID del pedido y la caducidad.
- Puede obtener sus satoshis en una dirección de bitcoin con una tarifa de intercambio (de LN a BTC-onchain) del orden del 1% (puede modificar las tarifas de minería on-chain).
- De lo contrario, cree una factura con una billetera LN de esta [lista](https://learn.robosats.com/docs/wallets/) y copie la factura en Robosats.
- Contacte al vendedor a través de chat cifrado para discutir el pago en fiat.

Ahora veamos los pasos para vender bitcoins en Robosats:

- Personalice su oferta eligiendo el método de pago, la prima, la duración de vencimiento, etc.
- El tamaño del bono de fidelidad es equivalente al depósito de garantía en BISC. Coloque un depósito de garantía del 15% o 10% para incentivar a la otra parte a jugar limpio.
- Bloquee los satoshis para confirmar la creación del pedido y evitar el spam.
- Si alguien acepta su oferta de venta, hable con la otra parte para proceder al pago en fiat. Una vez que se realiza el pago, ¡el intercambio está completo y los satoshis se venden!

## BISQ: solución de compra peer to peer

[Bisq](https://bisq.network/) es una plataforma de intercambio descentralizada para activos digitales, principalmente Bitcoin. Permite transacciones directas, seguras y privadas entre usuarios de todo el mundo sin necesidad de un intermediario.

🚨 Tenga cuidado al usar Bisq, ya que es una solución avanzada. Puede que no sea adecuado para usuarios principiantes. Asegúrese de tener cierta experiencia y comprensión antes de comenzar. 🚨

Examinamos esta solución en detalle, aquí están los videos tutoriales:

![parte 1](https://tube.nuagelibre.fr/videos/watch/b3885ea9-23e9-4b58-aa3f-401348da85a1)

![parte 2](https://tube.nuagelibre.fr/videos/watch/53276305-70d6-4c7f-9df9-e100a82eee16)

Para los más hábiles, aquí hay una guía sintética que describe rápidamente los pasos esenciales:

1. Descargar e instalar: Visite el sitio web de Bisq y descargue la aplicación. Instálela en su sistema.
2. Configurar el modo de pago: Abra la aplicación y vaya a "Cuenta". Agregue los detalles de su modo de pago.
3. Financiar su billetera Bisq: Haga clic en "Fondos" y "Recibir fondos" para obtener su dirección Bisq. Envíe bitcoins a esta dirección.
4. Hacer una transacción: Haga clic en "Comprar/Vender" y elija la transacción deseada. Siga las instrucciones para completar la transacción.
5. Confirmar la Recepción: Una vez que hayas recibido el pago, confírmalo en la aplicación Bisq. Esto libera el Bitcoin del depósito en garantía.
   No olvides siempre verificar todos los detalles de tus transacciones y tratar solo con partes de confianza.

Aquí tienes una guía completa que te guiará a través de todos los pasos para usar Bisq.

BISQ es una red descentralizada y segura que respeta tu propiedad privada. De hecho, es no custodial, lo que significa que siempre posees tus fondos. Además, BISQ utiliza un token, el BSQ, que te permite pagar tarifas de transacción más bajas y estimula tu participación en la DAO (Organización Autónoma Descentralizada). Para proteger a los vendedores en transacciones Bitcoin-fiat, BISQ ha establecido un sistema de firmas y límites de cuenta. Como comprador, deberás obtener una cuenta firmada para aumentar tu límite de compra. La firma también es una forma de verificar el historial de los traders, asegurando así la seguridad de las transacciones.

Para instalar Bisq y respaldar tus datos, sigue estos simples pasos:

- Ve al sitio bisc.network para descargar el software (Captura de pantalla de la página de descarga)
- Verifica la integridad del software utilizando herramientas como las propuestas por Loïc Morel para usuarios de Windows.
- Una vez verificado el instalador, inicia BISQ, otorga los permisos necesarios y acepta los términos de uso. (Captura de pantalla de los términos de uso)
- BISQ se conectará a la red Bitcoin y a sí mismo a través de Tor, esto puede tomar algún tiempo.
- Configura tu cuenta de pago y haz copias de seguridad de tu SID (Identificador Seguro) de tu billetera para prevenir cualquier pérdida o robo. (Captura de pantalla de la página de configuración de la cuenta)
- También establece una contraseña para cifrar tu información.

Dependiendo de tu sistema operativo, los datos de BISQ se almacenarán en diferentes ubicaciones. Puedes encontrarlos en la carpeta "Directorio de Datos". Ten cuidado, si eliminas esta carpeta, todos tus datos de BISQ se perderán.
Para recuperar tus datos a través de una copia de seguridad:

- Copia la carpeta de respaldo en la ubicación 'usuario / soporte de aplicación / BISQ'.
- Renombra la carpeta de respaldo como 'BISQ'.
- Reinicia BISQ y todos tus datos deberían ser restaurados.

Antes de comenzar a comprar o vender Bitcoin en BISQ, es crucial configurar tu cuenta de pago. Por ejemplo, puedes configurar una cuenta en tu moneda nacional, como una cuenta SEPA, una cuenta REVOLUT o una cuenta PAYPAL.
Para configurar tu cuenta REVOLUT:

- Agrega una cuenta y selecciona REVOLUT en la lista de opciones. (Captura de pantalla de la lista de opciones de cuenta)
- Puedes elegir diferentes monedas: euro, libra esterlina, dólar estadounidense o franco suizo.
- La durée maximale de la transaction es de un día y el límite de compra es de 0,25 Bitcoin.
- Utilice su nombre de cuenta personal REVOLUT para evitar confusiones.
- Asegúrese de firmar sus cuentas y establecer límites de compra para mayor seguridad.

Para comprar Bitcoin en BISQ:

- Acceda a la sección "Comprar" donde puede elegir diferentes mercados. (Captura de pantalla de la sección "Comprar")
- Para obtener tarifas reducidas, le recomendamos que compre BSQ, que puede comprar con Bitcoin.
- Puede elegir entre diferentes ofertas según el precio, la cantidad, el método de pago, etc.
- Para comprar BSQ, primero deposite Bitcoin en su billetera.
- Elija una oferta con una prima baja y una cantidad baja para la compra de BSQ.
- BISQ verifica la validez de la oferta y la conexión del par.
- Si el vendedor no está conectado, elija otro.
- Verifique la oferta y acepte una prima del 5%.
- Confirme las tarifas y el intercambio de BSQ, luego espere la confirmación de la transacción para comprar Bitcoins con BSQ.

Para vender Bitcoin en BISQ:

- Cree una nueva oferta en la pestaña "Vender". (Captura de pantalla de la pestaña "Vender")
- Puede elegir fijar la cantidad de Bitcoins a vender o el monto en euros que desea recibir.
- Puede establecer una prima en porcentaje por encima del precio de mercado.
- Puede crear un rango de venta o dejar la elección al comprador.
- También puede establecer un precio para detener la oferta.
- Elija el monto mínimo del depósito y las tarifas de transacción.
- Financie el pedido depositando los Bitcoins a vender, el monto del depósito de garantía y las tarifas.
- Una vez que haya creado la oferta, espere a que un comprador se presente.

Una vez que el comprador haya realizado el depósito de la transacción en BISQ, los Bitcoins se envían automáticamente al comprador y usted recibe el dinero. La cuenta se verifica y firma después de una transacción con una cuenta firmada.

## LNP2PBOT

![Tutorial de LNp2pbot](https://tube.nuagelibre.fr/videos/watch/57ed232d-6149-4267-be38-92b0f32800f7)

[Telegram](https://telegram.org/) es una plataforma de mensajería que, con la ayuda del bot [Lnp2pbot](https://lnp2pbot.com/), le permite comprar y vender bitcoins de manera rápida y fácil. Así es como se hace:

Para comprar Bitcoins a través del Bot LNP2PBOT en Telegram, siga los siguientes pasos:

- Comience por ir a la cuenta de Twitter del bot Lnp2pbot y haga clic en el enlace en la biografía. (Captura de pantalla de la cuenta de Twitter del bot y del enlace en la biografía)
- En Telegram, use los comandos "/buy" o "/sell" para publicar órdenes de compra o venta. (Captura de pantalla del uso de los comandos "/buy" o "/sell")
- Acceda al canal P2P Lightning para encontrar ofertas de compra y venta según sus criterios. (Captura de pantalla del canal P2P Lightning)
- Cree una oferta de compra utilizando el bot Lnp2pbot y el comando "/buy".
- Seleccione la moneda de su elección, indique la cantidad, el precio (con una prima si lo desea) y elija su método de pago.
- Espere a que un posible vendedor se ponga en contacto con usted.

Para vender Bitcoins a través de Revolut, siga estos pasos:

- Haga clic en 'vendre Satoshi' para abrir una notificación en LNP2PBot. (Captura de pantalla de la opción 'vendre Satoshi')
- Reciba una factura Lightning para pagar por la venta de los Satoshis. (Captura de pantalla de la factura Lightning)
- Espere a que el comprador envíe una factura con los satoshis para recibir los pagos.
- Establezca un contacto directo con el comprador a través de Telegram para acordar el método de pago e intercambiar la información necesaria.
- Valide la transacción con una nota.

Si desea comprar Bitcoins enviando una factura LN, siga estos pasos:

- Copie la factura y envíela al bot para comprar Satoshis.
- Póngase en contacto con el vendedor para finalizar la compra de los bitcoins.
- En caso de problemas, proponga esperar o intentar cancelar.
- Cancela la oferta y busca una nueva si es necesario.
- Elija una oferta que acepte CPA instantáneos para la compra de Satoshis.
- Envíe la factura y espere la confirmación de pago del vendedor.
- Una vez realizado el pago, envíe la confirmación al bot.
- Espere la validación de recepción de euros y el envío de satoshis por parte del vendedor.

Utilizando estos métodos, puede comprar y vender bitcoins de manera segura en Telegram.

## Peach Bitcoin

sitio: https://peachbitcoin.com/

Estamos examinando en detalle esta solución en BTC 205 ofrecido por @pivi\_, aquí están los videos tutoriales:

[Peach](https://peachbitcoin.com/) es una aplicación móvil suiza que permite comprar y vender bitcoins de igual a igual. Esta solución fácil de usar ofrece una interfaz intuitiva, ideal para transacciones en criptomonedas.

La interfaz de la aplicación Peach consta de cuatro pestañas: comprar, vender, historial y configuración. (Captura de pantalla de la interfaz de la aplicación)
La compra de bitcoins en Peach es simplificada. Para empezar, es necesario crear una oferta. Esto es posible accediendo a la pestaña "comprar". (Captura de pantalla de la pestaña "comprar") Luego, navegue por las ofertas disponibles deslizando hasta encontrar la que le convenga. Los medios de pago aceptados son variados, incluyendo transferencia bancaria, monedero en línea, tarjeta de regalo y opción local. (Captura de pantalla de los medios de pago disponibles)

Una vez que haya elegido una oferta, puede hablar con el vendedor a través del chat integrado en la aplicación. (Captura de pantalla del chat de la aplicación) Después del pago, confirmado por el vendedor, la transacción está completa. Los bitcoins son enviados al comprador, quien recibe una notificación confirmando la recepción de los fondos. (Captura de pantalla de la notificación de recepción de bitcoins)

Peach es una aplicación no custodial, lo que significa que los bitcoins permanecen en su posesión durante todo el proceso. Sin embargo, las posibles disputas son manejadas de manera centralizada. Por lo tanto, es crucial guardar la información relacionada con la transacción y su información personal utilizando la función Backup. (Captura de pantalla de la función Backup) Como Peach todavía está en versión beta, pueden ocurrir algunos errores. Se recomienda verificar toda la información antes de concluir una transacción.

En resumen, la aplicación móvil Peach ofrece una solución accesible para comprar y vender bitcoins de igual a igual. El uso seguro y óptimo de Peach es la clave para el éxito de sus transacciones.

## Hold Hodl

[HodlHodl](https://hodlhodl.com/) es un mercado descentralizado de Bitcoin que prioriza el control y la seguridad de los usuarios. A diferencia de los intercambios tradicionales, funciona según un modelo de igual a igual, permitiendo intercambios directos entre usuarios. Gracias a su sistema de custodia multi-firma, Hodl Hodl garantiza la seguridad de los fondos durante las transacciones. La plataforma también admite varios métodos de pago y ofrece opciones de negociación como contratos por diferencia (CFD).

En este tutorial, le explicamos cómo comprar y vender bitcoins de igual a igual en la plataforma HodlHodl.

Antes de comenzar a usar la plataforma HodlHodl, se necesitan algunas etapas de preparación:

- Abra el sitio web de HodlHodl.
- Cree una cuenta utilizando una dirección de correo electrónico para mantener un historial de sus transacciones.
- Lea cuidadosamente la guía de seguridad antes de comenzar a operar.
- Tenga en cuenta que la plataforma no es de código abierto y conserva cierta información personal.

Este es el proceso a seguir para realizar una compra en la plataforma HodlHodl:

- Utilice la función de filtro para encontrar las ofertas que le convengan.
- Haga clic en la oferta que le interese.
- Rellene los campos necesarios para aceptar el contrato.
- En nuestro ejemplo, hemos utilizado Revolut como método de pago.

La configuración del contrato multisig para la transacción se realiza de la siguiente manera en HodlHodl:

- Una vez aceptada la oferta, realice el pago a través del método elegido (Revolut en nuestro caso).
- Cree un contrato multisig generando una contraseña.
- Espere a que se depositen los bitcoins en la dirección multisig.
- Elija el número de confirmaciones para el contrato.
- Realice el pago del monto acordado al vendedor y confírmelo en HodlHodl.
- Sea paciente ya que la duración del depósito puede ser larga, dependiendo del banco utilizado.
- Espere la confirmación del vendedor antes de liberar los bitcoins después de la compra.

La creación de una oferta de venta o compra de bitcoins en HodlHodl se realiza de la siguiente manera:

- En el sitio web de HodlHodl, indique la dirección de liberación para las ofertas de compra.
- Proporcione la cantidad, el precio y el método de pago.
- También puede agregar opciones opcionales como límites de transacción o un título para la oferta.
- Una vez creada la oferta, puede verla, editarla, duplicarla o eliminarla a su gusto.

## Bonus: Side Shift.AI

Aquí hay un breve tutorial sobre cómo usar [SideShift AI](https://sideshift.ai/), una herramienta muy útil para convertir shitcoins en bitcoin. Es la herramienta ideal para aquellos que han cerrado todos sus exchanges personales. No se necesita ningún sistema de orden y hay liquidez disponible. Sin embargo, tenga en cuenta que hay una tarifa del 2,5% por transacción.

Si ha comprado criptomonedas de manera KYC, se recomienda usar Monero para convertir esas criptomonedas en bitcoin. Monero ofrece una privacidad superior a la de Bitcoin. Para una mayor seguridad, también se recomienda la operación de CoinJoin. CoinJoin mezcla sus transacciones con las de otros usuarios para complicar la trazabilidad de sus transacciones.

También me gustaría presentarle una herramienta de código abierto para comprar y vender bitcoins. Esta herramienta le permite elegir entre muchas blockchains. Solo necesita ingresar su dirección de Bitcoin y seleccionar la cantidad que desea enviar. No es necesario crear una cuenta o conectar su billetera a la herramienta. Puede usar una tasa fija para enviar o recibir una cantidad específica. Además, esta herramienta también permite la venta de bitcoins a cambio de USDC.

### Soutiens-nous

Este curso, así como todo el contenido presente en esta universidad, ha sido ofrecido gratuitamente por nuestra comunidad. Para apoyarnos, puedes compartirlo con tus amigos, convertirte en miembro de la universidad e incluso contribuir a su desarrollo a través de GitHub. ¡En nombre de todo el equipo, gracias!

### Nota de la formación

¡Pronto se integrará un sistema de calificación para la formación en esta nueva plataforma de E-learning! Mientras tanto, muchas gracias por seguir el curso y si lo has disfrutado, piensa en compartirlo con tus amigos.

# Para ir más allá

## Entrevista con Steph de Peach Bitcoin

Aquí hay un resumen de la entrevista:

Pitch Bitcoin es una aplicación móvil no custodial que permite la compra y venta de Bitcoin de igual a igual. Actualmente, el equipo de Pitch Bitcoin, con sede en Suiza, consta de ocho miembros y está trabajando para hacer evolucionar la aplicación para que también sirva como billetera. El modelo único de Pitch Bitcoin se basa en una estructura empresarial centralizada, manteniendo un libro de órdenes descentralizado. Además, la aplicación ofrece una opción para transacciones en efectivo en reuniones en persona.

Una de las principales ventajas de Pitch Bitcoin es el nivel de seguridad que ofrece a los usuarios. El sistema deskrow con multisignature y time lock está diseñado para manejar conflictos y garantizar la seguridad de las transacciones. Además, Pitch Bitcoin tiene acceso prioritario al dinero de multisignature, lo que le permite transferir los bitcoins al comprador en caso de comportamiento malicioso por parte del vendedor. La empresa tiene como objetivo integrar todas las monedas europeas y otros métodos de pago en su lanzamiento en open beta en enero.

La idea de Pitch Bitcoin surgió de la experiencia personal de su fundadora en la industria de Bitcoin. Después de descubrir Bitcoin en 2017 y asistir a varias reuniones y conferencias, se convirtió en una maximalista de Bitcoin y vio la oportunidad de crear una plataforma que permitiera a los Bitcoiners reunirse y hacer transacciones en efectivo. Además, la aplicación incluye un chat cifrado para comunicarse con otros usuarios, preservando el anonimato de los usuarios.

Actualmente, Pitch Bitcoin está desarrollando varias características para facilitar el trabajo de los vendedores, incluyendo la creación de una API para los vendedores, una plataforma para los grandes vendedores y la integración de BTC Pay Server para automatizar las transferencias. La aplicación se lanzará en open beta en enero de 2023.

En conclusión, la fundadora de Pitch Bitcoin destaca la importancia de la competencia en el ecosistema de Bitcoin, ya que lo que es bueno para Bitcoin es beneficioso para todos. También fomenta la diversidad y la inclusión en la industria de Bitcoin y más allá.

## Entrevista con Pierre

Aquí hay un resumen de la entrevista:

Esta entrevista cierra la formación Bitcoin 205 que aborda el tema de las soluciones de compra peer-to-peer de Bitcoin. Organizada por Pierre, esta formación tiene como objetivo educar al público francófono sobre las soluciones técnicas de compra peer-to-peer de Bitcoin, un área hasta ahora descuidada. Gracias a los avances realizados, ahora es posible comprar y usar Bitcoin preservando la privacidad, incluso con un simple teléfono y la aplicación Telegram.

Uno de los métodos destacados es el uso de CoinJoin con Samouraï para reforzar la seguridad. Esta solución permite minimizar los riesgos relacionados con las entidades centralizadas que tienen información personal sobre los usuarios de Bitcoin. Se recomienda comprar Bitcoins en no-KawaiiShii, un método que permite reforzar el anonimato. Además, algunas plataformas de intercambio como Kraken ofrecen tarifas de retiro más bajas que otras, lo que va en línea con los principios de Bitcoin.

Bisq, Robosat y Peach se presentan como soluciones democráticas para el comercio de bitcoins. Peach, en particular, se destaca por su facilidad de acceso como aplicación móvil. Sin embargo, existen desafíos por enfrentar, como la regulación de las criptomonedas y la necesidad de respetar ciertos límites para evitar una regulación excesiva.

También se aborda el uso de cajeros automáticos de Bitcoin, que representan un método económico para obtener bitcoins no-KYC. Dependiendo de la regulación local, estos cajeros pueden instalarse en el hogar o en lugares públicos y pueden usarse para ofrecer bitcoins a familiares o para pagos en bares.

La formación destaca la importancia del papel de la educación en la comprensión de Bitcoin. Se sugiere que Bitcoin puede ofrecer una solución en caso de recesión o hiperinflación y que es importante concienciar a las personas sobre su potencial antes de que sea demasiado tarde. Además, se destaca que la separación del Estado y la moneda es tan esencial como la separación del Estado y la religión.

En conclusión, Bitcoin se presenta como una moneda descentralizada que requiere educación pública y apertura mental para ser plenamente comprendida y utilizada. La formación tiene como objetivo ayudar a los participantes a comprender las diversas soluciones de compra peer-to-peer y a utilizar estas herramientas para reforzar su anonimato y seguridad al usar Bitcoin.

## Artículo de bonificación sobre privacidad

Un excelente [artículo](https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/) de Loïc Morel sobre KYC e identificación.
Este artículo detallado explora los desafíos y soluciones para preservar la privacidad al adquirir y utilizar bitcoins. Loïc desmonta algunas ideas preconcebidas sobre la identificación KYC (Conoce a tu cliente), detalla los riesgos asociados con este proceso y ofrece técnicas para mantener el anonimato de las transacciones. Es una lectura imprescindible para aquellos que buscan comprender las sutilezas de la privacidad en el mundo de Bitcoin y aprender cómo utilizar herramientas como CoinJoin, Stonewall y PayJoin para difuminar el rastreo de transacciones y proteger su privacidad.

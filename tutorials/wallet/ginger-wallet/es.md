---
name: Ginger Wallet
description: Software de código abierto y autocustodia Bitcoin wallet, fork de Wasabi Wallet, integrando Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet es una cartera de Bitcoin de código abierto, sin custodia, centrada en la confidencialidad y la privacidad. Comenzó su vida como fork a partir de Wasabi Wallet (después de la versión 2.0.7.2 - licencia MIT).



Ginger Wallet mantiene la arquitectura técnica de Wasabi y añade algunas características específicas. Según la [documentación de Ginger Wallet](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet), Wasabi hace hincapié en la **autonomía y el control**, mientras que Ginger se centra en la **facilidad de uso, la seguridad y una experiencia simplificada**, lo que lo hace accesible a quienes están menos familiarizados con los aspectos técnicos.



Ginger Wallet es el software wallet sólo para ordenadores (sin aplicación móvil).



## ¿Qué es Coinjoin?



El **coinjoin** es una estructura de transacción especial de Bitcoin que reúne a varios participantes en una única transacción colaborativa. Este mecanismo mezcla las entradas de distintos usuarios en una transacción común, lo que hace extremadamente difícil -si no a menudo imposible, si se hace correctamente- rastrear los fondos. Como resultado, resulta casi imposible para un observador externo identificar con certeza el origen y el destino de los bitcoins implicados, a diferencia de lo que ocurre en las transacciones Bitcoin convencionales.



Para ti, como usuario, coinjoin te ayuda a preservar tu confidencialidad. Por ejemplo, si recibes una donación de 10.000 sats en una dirección Bitcoin, el remitente puede rastrear estos fondos y, en algunos casos, deducir que posees una mayor cantidad de bitcoins, u observar tus actividades. Al hacer un coinjoin después de esta donación de 10.000 sats, rompes la trazabilidad: el remitente ya no podrá deducir ninguna información sobre ti a partir de este pago.



El coinjoin Chaumian ofrece un alto nivel de seguridad, ya que los fondos permanecen en todo momento bajo el control exclusivo del usuario. Ni siquiera los operadores de los servidores coordinadores pueden desviar los bitcoins de los participantes bajo ninguna circunstancia. Ni los usuarios ni los coordinadores necesitan confiar los unos en los otros: cada uno conserva el control de sus claves privadas y sigue siendo el único autorizado para validar las transacciones. Por tanto, ningún tercero puede apropiarse de tus bitcoins durante un coinjoin, ni establecer un vínculo directo entre tus entradas y salidas.



Para saber más sobre coinjoin, consulta el curso BTC 204 de Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Instalar Ginger Wallet



Para instalar Ginger Wallet, visite el sitio web [Ginger Wallet](https://gingerwallet.io).



Pulse **Descargar** para descargar la versión adecuada para su ordenador (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Otra opción es ir a [GitHub] del proyecto (https://github.com/GingerPrivacy/GingerWallet/releases) para descargarlo.



![screen](assets/fr/04.webp)



A continuación, ejecute el programa de instalación.



![screen](assets/fr/05.webp)




## Configuración de los parámetros



### Configuraciones preliminares



Abre Ginger Wallet, elige el idioma que prefieras.



![screen](assets/fr/06.webp)



Desde el principio, Ginger te recuerda los costes que conlleva el proceso de coinjoin.



![screen](assets/fr/07.webp)



A continuación, pulse **Inicio** y luego **Nuevo** para crear una nueva cartera.



![screen](assets/fr/08.webp)



A continuación, guarda y confirma tu seedphrase.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Para mayor seguridad, Ginger Wallet le da la opción de añadir una passphrase.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Este passphrase, una vez añadido, se solicitará cada vez que intente acceder a su cartera.



![screen](assets/fr/12.webp)



Ginger activa automáticamente el **Coinjoin** por defecto cuando usted crea su cartera. Se le informa de ello y, a continuación, puede personalizar la configuración para adaptarla a sus necesidades.



![screen](assets/fr/13.webp)




### Configuración general



Una vez que hayas creado tu primera cartera, accederás a la interfaz de Ginger Wallet.



![screen](assets/fr/14.webp)



Active el **modo discreto**, si desea ocultar los saldos de sus monederos.



![screen](assets/fr/15.webp)



Puedes crear varias carteras en Ginger Wallet. Solo tienes que hacer clic en **Añadir una cartera**.



![screen](assets/fr/16.webp)



Ginger admite el uso de carteras de hardware a través de la interfaz estándar Bitcoin Core, aunque aún no está disponible la integración directa desde o hacia una cartera de hardware.



Las carteras de hardware compatibles incluyen (pero no se limitan a) :




- Blockstream Jade
- Tarjeta Coldcard MK4
- Tarjeta Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Modelo T
- Trezor Safe 3
- etc.



Ahora haga clic en **Configuración**.



![screen](assets/fr/17.webp)



Estos ajustes son los de la aplicación en general, y las configuraciones que realice allí se aplicarán a todas las carteras.



En **Configuración**, tienes las pestañas :





- General**



![screen](assets/fr/18.webp)





- Apariencia



En esta pestaña, puede cambiar el idioma, la moneda y la unidad de visualización de la comisión (BTC/Satoshi), entre otros.



![screen](assets/fr/19.webp)





- Bitcoin**



Esta pestaña te permite activar Bitcoin Knots para que se ejecute al inicio de la aplicación, elegir tu red (Principal/RegTest), y tu proveedor de tarifas de carga (Mempool Space/Blockstream info/Full Node), etc.



![screen](assets/fr/20.webp)





- Características de seguridad**



En la pestaña Seguridad, puede activar la autenticación de dos factores, activar o desactivar Tor e incluso desactivarlo una vez cerrada la aplicación Ginger.



![screen](assets/fr/21.webp)



**NB** :




- Para la autenticación de dos factores, asegúrese de que su aplicación de autenticación admite el protocolo SHA256 y códigos de 8 dígitos. Ginger Wallet requiere un código 2FA de 8 dígitos para mejorar la seguridad. Este formato más largo hace que el código sea mucho más difícil de adivinar o comprometer, ofreciendo una mayor protección contra el acceso no autorizado.
- Por defecto, todo el tráfico de red de Ginger pasa a través de Tor, eliminando la necesidad de configuración manual. Si Tor ya está activo en su sistema, Ginger le dará prioridad automáticamente.



Pero una vez que desactiva Tor en los ajustes, su privacidad permanece generalmente preservada, excepto en dos situaciones:




- durante un Coinjoin, el coordinador podría vincular tus entradas y salidas a tu dirección IP;
- al difundir una transacción, un nodo malicioso al que te conectes podría asociar tu transacción con tu IP.



No olvide pulsar **Hecho** (en la esquina inferior derecha) cada vez, para guardar sus ajustes. Algunos ajustes requieren reiniciar Ginger Wallet para que surtan efecto.



Además, la barra de búsqueda situada en la parte superior de las carteras permite buscar y acceder a cualquier parámetro, etc.



![screen](assets/fr/22.webp)




### Configuración de la cartera



Se pueden crear varias carteras en la aplicación, por lo que cada cartera puede configurarse según sus necesidades. Para ello, haga clic en los **tres puntos** situados delante del nombre de la cartera y, a continuación, en **Configuración de la cartera**.



![screen](assets/fr/23.webp)



Como puedes ver, aparte del parámetro wallet, podrás ver tus UTXOs (lista de tokens que posees), estadísticas e información de wallet (la clave pública extendida, por ejemplo).



Para volver a la configuración de nuestra cartera, una vez que haga clic en parámetros de la cartera, accederá a las siguientes pestañas:




- General** (donde puede cambiar el nombre de la cartera) ;



![screen](assets/fr/24.webp)





- Coinjoin** (donde puede personalizar la configuración de coinjoin para este wallet) ;



![screen](assets/fr/25.webp)





- Herramientas** (donde puedes consultar tu seedphrase, sincronizar de nuevo tu cartera o eliminarla).



![screen](assets/fr/26.webp)




## Recibir bitcoins



![video](https://youtu.be/cqv35wBDWMQ)



Para recibir bitcoins en tu wallet en Ginger Wallet:




- pulse **Recibir** ;



![screen](assets/fr/27.webp)





- Introduzca el nombre de la fuente a la que desea asociar la dirección. Se trata de un etiquetado para realizar un seguimiento de los pagos. Esto no tiene implicaciones on-chain; es simplemente información de trazabilidad almacenada localmente en su aplicación;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- haga clic en la flechita a la izquierda de **Generar** para elegir su formato de dirección (**SegWit** /**Taproot**) , luego haga clic en **Generar**, para generate una dirección y un código QR.



![screen](assets/fr/29.webp)



El remitente utilizará esta dirección o código QR para enviarte bitcoins.



![screen](assets/fr/30.webp)




## Enviar bitcoins




![video](https://youtu.be/2nf5aAimfhg)



Para ello :




- Pulse el botón **Enviar**;
- introduzca la dirección del destinatario, el importe a enviar y una etiqueta;
- compruebe el resumen de la transacción y confirme el envío.



![screen](assets/fr/31.webp)




## Gastar bitcoins



Es fácil comprar y vender Bitcoin con Ginger Wallet. En solo unos pasos, puedes gastar tus bitcoins.



### Comprar bitcoins



![video](https://youtu.be/lEqTBzm5MEA)



Los usuarios de Ginger Wallet pueden comprar bitcoins.





- Pulse el botón **Comprar**. Este botón permanece visible aunque la wallet esté vacía.



![screen](assets/fr/32.webp)





- Selecciona tu país, o incluso tu estado (en algunas regiones, como Canadá), antes de proceder a la compra de bitcoins. De hecho, cuando hagas clic en la función **Comprar** por primera vez, también tendrás que especificar tu región.



![screen](assets/fr/33.webp)



Pulse **Continuar** para avanzar en el proceso de compra.





- A continuación, introduzca la cantidad de bitcoins que desea comprar en el campo correspondiente. También puedes elegir la moneda de la transacción.



![screen](assets/fr/34.webp)



Cada divisa tiene un límite mínimo y máximo de compra. Por ejemplo, en USD, el límite máximo es de 30.000 $.



Si ya ha realizado una compra, puede consultar su historial de transacciones haciendo clic en el botón **Pedidos anteriores**. Aparecerá una lista de transacciones anteriores y su estado.





- Elija la oferta que más le convenga.



En este punto, verá una lista de todas las ofertas disponibles. Para cada oferta, tienes :




 - nombre del proveedor (1) ;
 - el número de bitcoins equivalente al importe introducido previamente, el método de pago y la comisión de compra (2) ;
 - el botón **Aceptar** (3).



![screen](assets/fr/35.webp)



Las tasas indicadas en la oferta no constituyen un coste adicional. Ya están incluidas en el importe total de la oferta.



La esquina superior derecha de la pantalla, denominada **Todos**, le permite filtrar las ofertas por método de pago. El método de pago seleccionado se establecerá por defecto, pero puede cambiarse en cualquier momento.



![screen](assets/fr/36.webp)



Si encuentra una oferta adecuada, haga clic en el botón **Aceptar** para proceder a la compra. A continuación se le redirigirá a la página del vendedor, donde podrá finalizar la transacción.



### Vender bitcoins



Los usuarios de Ginger Wallet pueden vender Bitcoin. El botón **Vender** sólo es visible cuando hay fondos disponibles en la cartera.





- Haga clic en **Vender**.



![screen](assets/fr/37.webp)





- Al igual que con la opción **Comprar**, cuando utilice la función Vender por primera vez, deberá seleccionar su país antes de proceder a la venta de bitcoins.





- A continuación, debe introducir la cantidad de Bitcoins que desea vender. Puede introducir esta cantidad en BTC o en una moneda fiduciaria como el dólar estadounidense (USD).





- Una vez hecho esto, verás una lista de ofertas disponibles. Elige la oferta que más te convenga y haz clic en **Aceptar** para continuar.





- Ahora tienes que finalizar la transacción:
 - Una vez que haya aceptado una oferta, se le redirigirá a la página del proveedor;
 - Siga las instrucciones de la página del proveedor;
 - En algún momento, recibirá la dirección del destinatario y el importe exacto que debe enviar;
 - A continuación, vuelva a Ginger Wallet para continuar el proceso;
 - Una vez de vuelta en Ginger Wallet, aparecerá un cuadro de diálogo que le permitirá continuar pulsando **Enviar**.



Se abrirá la pantalla **Enviar** con la dirección del destinatario y el importe rellenados previamente. También puede utilizar el botón **Enviar** de la pantalla de inicio. Aunque puede enviar la transacción manualmente, le recomendamos que lo haga a través del cuadro de diálogo para optimizar el proceso.



## Hacer un coinjoin en Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Proteja la confidencialidad de sus bitcoins con **Coinjoin**, integrado directamente en Ginger Wallet. wallet utiliza **WabiSabi**, un protocolo de coinjoin chaumiano diseñado para facilitar coinjoins más accesibles y eficientes.



Tú eliges la estrategia de coinjoin (automática o manual) que más te convenga.



Ginger Coinjoin está listo para usar en cuanto lo descargas (no requiere pasos adicionales). Automáticamente, Ginger Coinjoin se ejecuta en segundo plano para proteger tu privacidad en cada transacción. En la práctica, el reproductor de Coinjoin aparecerá siempre que tengas un saldo que se pueda anonimizar.



En cuanto a la puesta en marcha manual de coinjoin, es una operación de un solo clic. Inicia la ronda y espera a que se cree y confirme la transacción coinjoin. Verás la puntuación de anonimización en la interfaz.



Se pueden realizar varias mezclas hasta alcanzar el nivel de anonimato deseado. También se pueden excluir determinadas partes de la mezcla.



Por defecto, Ginger utiliza su propio coordinador con todos los parámetros preconfigurados y comisiones garantizadas. Los coinjoins de tokens por valor superior a 0,03 BTC incurren en una comisión de coordinador del 0,3%, además de la comisión de mining. Las entradas de 0,03 BTC o menos, así como las remezclas, están exentas de comisiones de coordinador, incluso después de una única transacción. Por lo tanto, un pago realizado con fondos Coinjoin permite tanto al emisor como al receptor remezclar sus monedas sin incurrir en tasas de coordinador.



Ginger prefiere coinjoins con más participantes a rondas más pequeñas y rápidas. Los coinjoins más grandes ofrecen más anonimato, menores costes y mayor eficiencia del espacio de bloques.




## Seguridad y buenas prácticas



El deseo de descentralización y la preservación de la privacidad exigen la adopción de varias buenas prácticas:




- Guarde siempre su seedphrase en un lugar seguro fuera de línea;
- Si pierde su ordenador o sospecha de un acceso no autorizado, cree inmediatamente una nueva wallet. Transfiera sus fondos a esta nueva cartera y elimine la antigua;
- Utilice una dirección diferente para cada recepción para evitar reutilizar direcciones;
- Descargue siempre las aplicaciones de su cartera exclusivamente de la cuenta oficial de GitHub o del sitio web oficial.



Ahora ya estás familiarizado con el uso de la aplicación Ginger Wallet para enviar, recibir y gastar tus bitcoins.



Si este tutorial te ha resultado útil, déjame un pulgar verde a continuación. Por favor, siéntase libre de compartir este artículo a través de sus plataformas de medios sociales. Muchas gracias



También te sugiero que eches un vistazo a este tutorial sobre cómo utilizar la aplicación informática Liana para enviar y recibir bitcoins, así como para poner en marcha un plan patrimonial automatizado.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
---
name: Alby Hub
description: ¿Cómo lanzar fácilmente su propio nodo Lightning?
---
![cover](assets/cover.webp)

Alby Hub es el último software de código abierto de Alby, la empresa detrás de la popular extensión web de Lightning. Alby Hub es una billetera auto-custodiada con el nodo Lightning más fácil de usar, accesible desde cualquier lugar para integrarse con docenas de aplicaciones. Alby Hub es una interfaz fácil de usar para gestionar nodos Lightning.

En este tutorial, veremos diferentes formas de usar Alby Hub y cómo conectarlo a Alby Go, la aplicación móvil de Alby o la extensión de navegador Alby. Esto le permitirá gastar sus sats en movimiento mientras mantiene la autonomía en la gestión de su nodo.


![ALBY HUB](assets/fr/01.webp)

## ¿Qué es Alby Hub?

Alby Hub está destinado a ser la nueva herramienta principal en el ecosistema de Alby. Este software permite a los usuarios gestionar fácilmente su propia billetera auto-custodiada con un nodo Lightning integrado, mientras mantienen la propiedad de sus claves (auto-custodia).

Alby Hub es una herramienta muy adaptable. Puede satisfacer las necesidades tanto de principiantes como de usuarios avanzados. Los novatos lo utilizarán para manejar fácilmente un nodo Lightning real por su cuenta, sin tener que lidiar con la complejidad subyacente. Para los usuarios más experimentados, Alby Hub se puede utilizar como una interfaz completa para la gestión avanzada de un nodo Lightning existente.

En función de sus necesidades, Alby Hub está disponible en 4 configuraciones:


- Alby Hub Nube :**

Ideal para principiantes, esta primera opción es la opción en la nube de Alby. Permite desplegar un Hub directamente en un servidor gestionado por Alby, accesible a través de tu interfaz de Alby Hub. Aunque Alby gestiona el servidor, mantienes la soberanía sobre tus fondos, ya que tus claves están encriptadas con una contraseña que solo tú conoces. Sin embargo, tus claves deben permanecer desencriptadas en la RAM para que el nodo funcione, lo que teóricamente las expone a riesgo si alguien accede físicamente al servidor. Es un compromiso interesante para principiantes, pero es importante ser consciente de los riesgos.

La mayor ventaja de esta opción es que dispones de un nodo Lightning en funcionamiento 24/7, sin tener que gestionar tú mismo el alojamiento. Además, las copias de seguridad de tu nodo Lightning están simplificadas y automatizadas, en comparación con las opciones autoalojadas, en las que tienes que gestionar tú mismo las copias de seguridad de los canales.

Alby Cloud es un servicio de pago [Consulta sus precios](https://albyhub.com/#pricing) para más detalles. La tarifa se deduce automáticamente de tu billetera a través de una factura Lightning emitida por Alby. Esto se realiza mediante una conexión NWC que configura tu nodo para pagar automáticamente las facturas de Alby relacionadas con tu suscripción.


- Alby Hub con un nodo existente :**

Si ya dispone de un nodo alojado, por ejemplo en Umbrel o Start9, Alby Hub puede utilizarse como interfaz de gestión avanzada, del mismo modo que ThunderHub o RTL.


- Alby Hub local :**

También es posible instalar Alby Hub directamente en tu PC, aunque esta opción es menos práctica, ya que tu PC debe permanecer activo en todo momento para acceder remotamente al nodo Lightning. Sin embargo, esta alternativa puede ser adecuada para tus necesidades específicas.


- Alby Hub en un servidor personal :**

Para usuarios avanzados, Alby Hub puede ser desplegado en un servidor personal con un simple comando. Esta opción no está cubierta en este tutorial, pero puedes encontrar instrucciones dedicadas [en el GitHub de Alby](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Este tutorial se centra principalmente en la interfaz, que será la misma independientemente de la opción elegida. También veremos cómo desplegar Alby Hub con la opción de pago en la nube, y luego con la opción node-in-box (Umbrel o Start9).

![ALBY HUB](assets/fr/02.webp)

Para la instalación local en su PC, [descargue e instale el software según su sistema operativo](https://github.com/getAlby/hub/releases), luego siga las mismas instrucciones en la interfaz.

![ALBY HUB](assets/fr/03.webp)

## Crear una cuenta Alby

El primer paso es crear una cuenta Alby. Aunque no es imprescindible para utilizar Alby Hub, te permite aprovechar al máximo las opciones disponibles, incluida la posibilidad de obtener una dirección Lightning.

Visita [el sitio web oficial de Alby](https://getalby.com/) y haz clic en el botón "*Crear cuenta*".

![ALBY HUB](assets/fr/04.webp)

Introduzca un apodo y una dirección de correo electrónico y haga clic en "*Inscribirse*". Esta dirección de correo electrónico se utilizará para iniciar sesión en su cuenta más adelante.

![ALBY HUB](assets/fr/05.webp)

Introduzca el código de verificación que ha recibido por correo electrónico.

![ALBY HUB](assets/fr/06.webp)

Una vez conectado a su cuenta en línea, haga clic en el botón "*Continuar*".

![ALBY HUB](assets/fr/07.webp)

Vuelva a hacer clic en "*Continuar*".

![ALBY HUB](assets/fr/08.webp)

## La opción de alojamiento en la nube

A continuación, tendrás que elegir entre una opción autohospedada, donde instalas Alby Hub en tu propio dispositivo, u opciones premium. Comenzaré explicando cómo proceder con la opción Pro Cloud (ten en cuenta que esta es una opción de pago, consulta los detalles en la sección anterior).

Haga clic en "*Actualizar*".

![ALBY HUB](assets/fr/09.webp)

Confirme haciendo clic en "*Suscribirse ahora*".

![ALBY HUB](assets/fr/10.webp)

Haz clic en "*Lanzar Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Espere unos instantes mientras se crea su nodo.

![ALBY HUB](assets/fr/12.webp)

Y eso es todo, tu Alby Hub ya está configurado. En la siguiente sección, te mostraré cómo instalar Alby Hub en un nodo existente. Si aún no tienes un nodo Lightning, puedes saltar a la siguiente sección para configurar Alby Hub en Alby Cloud.


![ALBY HUB](assets/fr/13.webp)

## La opción del autoalojamiento

Si prefiere utilizar Alby Hub como interfaz para su nodo Lightning existente, tiene varias opciones: instalarlo en un servidor, localmente en su ordenador o a través de un node-in-box (Umbrel o Start9). El uso de Alby Hub en estas configuraciones es gratuito. Vamos a centrarnos en la opción node-in-box, ya que considero que la opción de servidor, sin acceso físico, presenta riesgos similares a la versión en la nube, y la instalación local en un PC suele ser inadecuada.

Para configurar esto en Umbrel (los pasos para Start9 son idénticos), primero debe tener un nodo LND ya configurado.

Accede a tu interfaz Umbrel y ve a la tienda de aplicaciones.

![ALBY HUB](assets/fr/14.webp)

Busca la aplicación "*Alby Hub*".

![ALBY HUB](assets/fr/15.webp)

Instálalo en tu nodo.

![ALBY HUB](assets/fr/16.webp)

Tu interfaz Alby Hub ya está lista. Puedes seguir el resto del tutorial como si estuvieras usando la interfaz en la nube, pero sin las opciones de la versión de pago. Además, a diferencia de la versión en la nube, tus claves se almacenan localmente en tu nodo, no en los servidores de Alby.

![ALBY HUB](assets/fr/17.webp)

## Lanzamiento de Alby Hub

Haga clic en el botón "*Iniciar*".

![ALBY HUB](assets/fr/18.webp)

Alby Hub te pedirá que elijas una contraseña. Esta contraseña es muy importante, ya que se utilizará para cifrar tu monedero. En la versión de pago en la nube, tus claves se almacenan en el servidor de Alby, cifradas con esta contraseña que solo tú conoces, luego se descifran y se almacenan solo en la memoria RAM para firmar transacciones cuando sea necesario.

Por lo tanto, es esencial elegir una contraseña fuerte. Cualquiera que tenga esta contraseña podría potencialmente acceder a tu nodo. Asegúrate de hacer una o más copias de seguridad físicas de esta contraseña en un papel, o mejor aún, en un trozo de metal para mayor seguridad.

Una vez que haya elegido y guardado cuidadosamente su contraseña, haga clic en "*Crear contraseña*".

![ALBY HUB](assets/fr/19.webp)

Ahora tienes acceso a tu nodo Lightning.

![ALBY HUB](assets/fr/20.webp)

La primera acción a realizar es guardar tu frase de recuperación, de la cual se derivan tus claves. Para hacer esto, haz clic en "Configuración". Esta frase te permite recuperar el acceso a tu billetera si habilitaste las copias de seguridad automáticas.

![ALBY HUB](assets/fr/21.webp)

A continuación, ve a la pestaña "*Backup*". Introduce tu contraseña para acceder a ella.

![ALBY HUB](assets/fr/22.webp)

Así tendrá acceso a su frase de recuperación de 12 palabras. Haz una o varias copias de seguridad físicas de esta frase en papel o metal y guárdalas en un lugar seguro.

![ALBY HUB](assets/fr/23.webp)

Cuando hayas guardado la frase, marca la casilla para confirmar que la has guardado y haz clic en "*Continuar*".

![ALBY HUB](assets/fr/24.webp)

## ¿Cómo puedo recuperar el acceso a mis bitcoins?

Antes de enviar fondos a tu Alby Hub, es importante comprender cómo recuperarlos en caso de un problema, así como qué información se necesita para esta recuperación. El proceso varía según la naturaleza de los fondos a recuperar y el modo de alojamiento de tu nodo.

Para los usuarios de la nube de pago, la recuperación completa de tus bitcoins requiere tres elementos esenciales:

- Tu frase de recuperación;
- Acceso a tu cuenta de Alby para recuperar las copias de seguridad automáticas.

La ausencia de cualquiera de estas dos piezas de información haría imposible recuperar tus bitcoins por completo.

Para aquellos que ejecutan Alby Hub en su propio dispositivo, el proceso de recuperación está documentado [aquí](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account).

Si instalaste Alby Hub en un nodo existente, deberás seguir el proceso de recuperación del sistema operativo específico de ese nodo. Por ejemplo: Umbrel ofrece [una opción](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) para cifrar el último estado de tus canales Lightning y guardarlo de manera dinámica y anónima a través de Tor. Ten en cuenta que solo las copias de seguridad automáticas de Alby te permiten recuperar tu Hub completamente sin cerrar ningún canal.

## Compre su primer canal Lightning

Ahora puede seguir las instrucciones proporcionadas por Alby Hub. Haz clic en el botón para abrir tu primer canal de entrada de dinero.

![ALBY HUB](assets/fr/25.webp)

Selecciona "*Canal abierto*". Si no tienes intención de convertirte en un nodo de enrutamiento y no lo necesitas específicamente, te recomiendo que optes por los canales privados.

![ALBY HUB](assets/fr/26.webp)

Alby Hub generará una factura para que la pagues. Este pago cubre las tasas de transacción necesarias para abrir tu canal, así como las tasas de servicio del LSP (*Lightning Service Provider*) que abrirá un canal a tu nodo, permitiéndote recibir pagos inmediatamente.

![ALBY HUB](assets/fr/27.webp)

Una vez pagada la factura y confirmada la transacción, se establece su primer canal Lightning.

![ALBY HUB](assets/fr/28.webp)

En la pestaña "*Nodo*", puedes ver que ahora tienes efectivo entrante, lo que te permite recibir pagos a través de Lightning.

![ALBY HUB](assets/fr/29.webp)

Para recibir el pago, haga clic en la pestaña "*Billetera*" y luego en "*Recibir*".

![ALBY HUB](assets/fr/30.webp)

Introduzca un importe y añada una descripción si es necesario, después haga clic en "*Crear factura*".

![ALBY HUB](assets/fr/31.webp)

He recibido mi primer pago de 120.000 sats.

![ALBY HUB](assets/fr/32.webp)

Si vuelves a la pestaña "*Monedero*", podrás consultar el saldo de tu monedero. Tenga en cuenta que Alby Hub reserva automáticamente 354 sats cuando realiza su primer pago. Por cada canal Lightning que abra a partir de entonces, Alby Hub apartará automáticamente una reserva equivalente al 1% de la capacidad del canal. Esta reserva es una medida de seguridad que permite a tu nodo recuperar los fondos del canal en caso de intento de fraude por parte de tu par. Por eso, aunque he enviado 120.000 sats, en mi saldo sólo aparecen 119.646 sats.

![ALBY HUB](assets/fr/33.webp)

## Depósito de bitcoins onchain

Si quieres disponer de efectivo saliente para realizar pagos, también puedes abrir un canal tú mismo. Para ello, necesitarás bitcoins onchain en tu monedero.

En la pestaña "*Nodo*", haga clic en "*Depósito*".

![ALBY HUB](assets/fr/34.webp)

Envía bitcoins a la dirección mostrada. Esta dirección se deriva de su frase de recuperación previamente guardada.

![ALBY HUB](assets/fr/35.webp)

He enviado 72.000 sats. Ahora son visibles en "*Saldo de Ahorros*", que incluye todos los fondos que poseo onchain, y no en Lightning.

![ALBY HUB](assets/fr/36.webp)

## Abrir un canal Lightning

Ahora que dispones de fondos onchain, puedes abrir un nuevo canal Lightning. Es aconsejable abrir varios canales, con cantidades suficientes para asegurarte de que siempre puedes realizar pagos sin restricciones. La mayoría de los LSPs (*Lightning Service Providers*) requieren un mínimo de 150.000 sats para abrir un canal contigo.

En la pestaña "*Nodo*", haz clic en "*Abrir canal*".

![ALBY HUB](assets/fr/37.webp)

Selecciona el tamaño de tu canal. Te recomiendo que no abras canales demasiado pequeños, teniendo en cuenta que se trata de un nodo Lightning y que la máquina que aloja tus claves no ofrece el mismo nivel de seguridad que un monedero hardware. Así que ten cuidado con las cantidades que decides bloquear.

![ALBY HUB](assets/fr/38.webp)

En el menú "*Opciones avanzadas*", puede elegir con qué LSP abrir su canal o introducir manualmente otro nodo Lightning.

![ALBY HUB](assets/fr/39.webp)

A continuación, haz clic en "*Abrir canal*".

![ALBY HUB](assets/fr/40.webp)

Espere a que se confirme su canal en la cadena.

![ALBY HUB](assets/fr/41.webp)

Tu nuevo canal aparecerá ahora en la pestaña "*Nodo*".

![ALBY HUB](assets/fr/42.webp)

## Gestión del nodo

Gestionar tus canales Lightning es más fácil de lo que piensas. Alby Hub te permite transferir sats entre tu saldo de gastos y tu saldo on-chain. Así es como puedes aumentar la capacidad de gasto o de recepción.

![ALBY HUB](assets/fr/66.webp)


## Conectar una aplicación de gastos

Ahora que tienes un nodo Lightning en funcionamiento, puedes utilizarlo para recibir y gastar sats a diario. Aunque la interfaz web de Alby Hub es práctica para gestionar tu nodo, no es ideal para realizar transacciones rápidas sobre la marcha. Para ello, vamos a utilizar una aplicación de monedero Lightning instalada en nuestro smartphone.

En este tutorial, te recomiendo que optes por Alby Go, que es muy fácil de usar, pero también puedes utilizar otras aplicaciones compatibles como Zeus.

![ALBY HUB](assets/fr/43.webp)

Para instalar Alby Go, ve a la tienda de aplicaciones de tu dispositivo:


- [Para Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Para Apple](https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Los usuarios de Android también pueden instalar la aplicación a través del archivo `.apk` [disponible en el GitHub de Alby](https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Cuando se inicie la aplicación, haga clic en "*Conectar Cartera*".

![ALBY HUB](assets/fr/46.webp)

En tu Alby Hub, en la sección App Store, encuentra “Alby Go” y haz clic en “Connect”  
![ALBY HUB](assets/fr/47.webp)  
Haz clic en “Connect with One-Tab Connections”. Esto te permitirá vincular tu Alby Hub con un clic a otras aplicaciones que usan Alby Go.  

![ALBY HUB](assets/fr/48.webp)  

Alby Hub generará entonces un secreto para establecer la conexión con Alby Go.


![ALBY HUB](assets/fr/49.webp)

Vuelve a la aplicación Alby Go, escanea el código QR o pega el secreto.

![ALBY HUB](assets/fr/50.webp)

Haga clic en "Finalizar*".

![ALBY HUB](assets/fr/51.webp)

Ahora tienes acceso remoto a tu nodo Lightning impulsado por Alby Hub desde tu smartphone, lo que facilita el envío y recepción de sats en movimiento todos los días.


![ALBY HUB](assets/fr/52.webp)

Si es necesario, puede gestionar los permisos para esta conexión directamente en Alby Hub haciendo clic sobre ella.

![ALBY HUB](assets/fr/53.webp)

Para recibir saturaciones, basta con hacer clic en "*Recibir*".

![ALBY HUB](assets/fr/54.webp)

Modifique el importe y la descripción de la factura haciendo clic en "*Factura*".

![ALBY HUB](assets/fr/55.webp)

Cargar la factura para recibir la saturación.

![ALBY HUB](assets/fr/56.webp)

Para enviar saturaciones, haz clic en "*Enviar*".

![ALBY HUB](assets/fr/57.webp)

Escanee la factura que desea pagar.

![ALBY HUB](assets/fr/58.webp)

A continuación, haga clic en "*Pagar*".

![ALBY HUB](assets/fr/59.webp)

Su transacción está confirmada.

![ALBY HUB](assets/fr/60.webp)

Haciendo clic en la flecha pequeña, puede acceder a su historial de transacciones.

![ALBY HUB](assets/fr/61.webp)

Estas transacciones también son visibles en su Alby Hub.

![ALBY HUB](assets/fr/62.webp)

## Personaliza tu dirección Lightning

Alby le ofrece la opción de una dirección Lightning. Esto te permite recibir pagos en tu nodo sin tener que generar manualmente una factura cada vez. Por defecto, Alby te asigna una dirección Lightning, pero puedes personalizarla. Inicie sesión en su cuenta en línea de Alby, haga clic en su nombre en la esquina superior derecha y, a continuación, seleccione "*Configuración*".

![ALBY HUB](assets/fr/63.webp)

Navegue hasta el menú "*Dirección del rayo*".

![ALBY HUB](assets/fr/64.webp)

Modifique su dirección y confirme haciendo clic en "*Actualizar su dirección de rayos*".

![ALBY HUB](assets/fr/65.webp)

Ten en cuenta que una vez cambiada tu dirección, ya no te pertenece. Así que asegúrate de no volver a enviar saturaciones a esa dirección.

Y eso es todo, ahora ya sabes cómo usar Lightning con tu propio nodo usando la herramienta Alby Hub. Si te ha resultado útil este tutorial, te agradecería mucho que pusieras un pulgar verde abajo. No dudes en compartir este artículo en tus redes sociales. ¡Muchas gracias!

Para comprender en detalle todos los mecanismos de Lightning que hemos manipulado en este tutorial, le aconsejo encarecidamente que descubra nuestra formación gratuita sobre el tema :

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

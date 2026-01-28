---
name: Tiankii
description: Conjunto de herramientas "relámpago" para minoristas y consumidores
---

![cover](assets/cover.webp)



En el ecosistema de la Bitcoin, aceptar pagos en tiempo real sigue siendo un reto importante para empresas y particulares. Las soluciones tradicionales suelen exigir conocimientos técnicos avanzados, una infraestructura compleja de mantener o que los fondos estén en manos de intermediarios. Esta situación está frenando la adopción masiva de la Bitcoin como moneda de uso cotidiano, a pesar de lo prometedor de los avances tecnológicos de la Lightning Network.



Tiankii, una empresa salvadoreña nacida en 2021, responde a este problema ofreciendo una infraestructura Bitcoin accesible y modular. En lugar de forzar la adopción de un ecosistema cerrado, Tiankii ofrece un conjunto de herramientas interconectadas que permiten a cualquiera integrar Bitcoin Lightning en su negocio sin sacrificar el control de sus fondos.



## ¿Qué es Tiankii?



### Origen y filosofía



Tiankii -término náhuatl que significa "mercado al aire libre accesible a todos"- es la primera empresa emergente 100% de Bitcoin de El Salvador. Fundada por Darvin Otero tras la adopción del Bitcoin como moneda de curso legal en el país, la empresa pretende transformar el Bitcoin de un depósito de valor en una moneda transaccionable para las compras cotidianas. A diferencia de las plataformas de custodia, Tiankii adopta un enfoque no custodial en el que los usuarios conservan el control de sus fondos, y la infraestructura sirve únicamente de intermediario técnico.



### Arquitectura técnica



Tiankii se posiciona como proveedor de infraestructura Bitcoin-as-a-Service basada en Lightning Network. Esta tecnología de segunda capa permite transacciones casi instantáneas con costes insignificantes, haciendo posibles los micropagos y las compras cotidianas.



La arquitectura se basa en tres pilares:



**Primero Lightning**: Favorecer sistemáticamente la red Lightning por su velocidad y menores costes, manteniendo el soporte de transacciones on-chain para grandes importes.



**Normas abiertas**: Uso de LNURL para automatizar las solicitudes de pago, Lightning Address para identificadores de correo electrónico legibles y tarjeta Bolt para pagos NFC interoperables.



**Modularidad agnóstica wallet**: Posibilidad de conectar diferentes carteras de Lightning (LNbits, Blink, BlueWallet) o su propio nodo, ofreciendo la máxima flexibilidad en función del nivel de experiencia y autonomía requerido.



## Herramientas del ecosistema Tiankii



### Bitcoin POS - Terminal de pago en tienda



La aplicación convierte el smartphone o la tableta en un terminal Lightning. El comerciante introduce el importe en la moneda local y la app genera un código QR Lightning o acepta una tarjeta Bolt Card. Las transacciones se abonan al instante sin comisiones, con conversiones automáticas en más de 150 divisas, gestión de propinas e historial de ventas.



### Cuadro de mandos de vendedor - Gestión unificada de ventas



Interface web centralizada para conectar su wallet Lightning, seguir las transacciones en tiempo real, emitir facturas e informes contables generate. La plataforma agrega todos los canales: pagos en tienda (TPV), ventas en línea (complementos de comercio electrónico) o integraciones API. Los pagos convergen en la wallet elegida.



### Tarjeta sin contacto Bitcoin (Tarjeta Bolt)



La tarjeta NFC Bolt representa la mayor innovación de Tiankii en la democratización de Bitcoin para el gran público. Funciona como una tarjeta bancaria sin contacto y permite pagar las compras de Bitcoin Lightning con solo tocar un terminal compatible.



A diferencia de las soluciones tradicionales de custodia, esta tarjeta sigue un estándar abierto que garantiza la interoperabilidad. Los usuarios pueden vincularla a su propia wallet a través de la aplicación IBI, conservando así sus claves privadas y el control total sobre los fondos asociados. El pago se realiza en un segundo, sin necesidad de sacar el smartphone o tener una conexión a Internet activa en el momento del pago.



Esta solución es especialmente inclusiva para las personas que no están familiarizadas con los teléfonos inteligentes, ya que ofrece una puerta de acceso accesible a la economía Bitcoin.



### Aplicación IBI - Interface individual Bitcoin



La aplicación IBI (Individual Bitcoin Interface) está diseñada para particulares que deseen utilizar Bitcoin Lightning a diario. Su principal ventaja reside en la generación de un Address Lightning personalizado, un identificador de pago legible en formato de correo electrónico (ejemplo: alice@ibi.me).



Este identificador simplifica drásticamente la recepción de pagos: no es necesario generate una nueva factura para cada transacción, el remitente puede simplemente introducir la dirección Lightning. La interfaz también permite gestionar la tarjeta Bolt (activación, desactivación, límites de gasto), conectar varios monederos Lightning y realizar pagos escaneando códigos QR.



### Plugins de comercio electrónico



Integraciones listas para usar para WooCommerce, Shopify y Cloudbeds. Se instala en minutos para añadir Bitcoin Lightning al proceso de pago. Ventajas: comisión cero (frente al 2-3% de las tarjetas de crédito), liquidación instantánea, acceso mundial, eliminación de devoluciones de cargo. Los pagos llegan directamente a la wallet conectada del comerciante.



### Bitcoin API y herramientas para desarrolladores



El SDK de Tiankii permite integrar Bitcoin Lightning en las aplicaciones existentes sin necesidad de mantener un nodo propio. API gestiona la creación de facturas, la verificación de pagos y los envíos masivos a través de una sólida infraestructura alojada en Google Cloud. Command Center completa la oferta para organizaciones con Address Lightning en dominios personalizados, pagos masivos y gestión centralizada de terminales y tarjetas NFC.



## Instalación y primeros pasos



### Requisitos esenciales



El uso de Tiankii no requiere complejos requisitos técnicos previos. Las aplicaciones funcionan a través de un navegador web en un smartphone, tableta u ordenador. No es necesario instalar ninguna aplicación nativa: todo lo que necesita es acceso a Internet y un navegador reciente para acceder a IBI o al Cuadro de mandos del comerciante.



**Para usuarios privados (IBI App)**: No se requiere wallet Lightning previo. Cuando creas tu cuenta, Tiankii configura automáticamente una Address Lightning en funcionamiento a través del [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), una implementación sin nodos que utiliza la red Liquid en segundo plano. Puede recibir y enviar pagos inmediatamente sin ninguna configuración técnica. Esta solución simplifica drásticamente el acceso para principiantes, sin dejar de ser autocustodiada.



**Para comerciantes (Panel de comerciante)** : La conexión de un wallet Lightning existente es obligatoria para utilizar terminales de punto de venta y recibir pagos. Tiankii soporta muchas soluciones: monederos móviles (Blink, Strike), soluciones auto-alojadas (LNbits, LND/CLN node), o monederos web (Alby). Las guías detalladas de conexión están disponibles en la sección Recursos de este tutorial.



### Para clientes particulares: Aplicación IBI



**Creación de cuenta



Vaya a accounts.ibi.me para crear su cuenta. En esta página puede elegir entre dos tipos de cuenta: "Uso personal" para uso individual, o "Uso comercial" para uso comercial. Seleccione "Uso personal" para acceder a las herramientas de recepción y envío de pagos en Bitcoin.



![Choix du type de compte](assets/fr/01.webp)



Tras seleccionar "Uso personal", será redirigido automáticamente a go.ibi.me para completar su registro. Puede hacerlo por correo electrónico, número de teléfono o utilizando su cuenta de Google, Microsoft o Twitter. Una vez creado, podrá acceder inmediatamente a su interfaz IBI, con su Lightning Address ya operativo.



![Création du compte](assets/fr/02.webp)



**Interface principal**



La interfaz de IBI muestra tu saldo en satoshis y en moneda local (USD). Tres botones permiten interactuar: "Recibir" para recibir pagos, "Escanear" para escanear un código QR y "Enviar" para enviar satoshis.



![Interface IBI](assets/fr/03.webp)



**Recibir el pago**



Para recibir satoshis, pulse "Recibir". La aplicación genera automáticamente un código QR y muestra su Address Lightning personalizado (formato nom@ibi.me). Comparte esta dirección o el código QR con el remitente: los fondos llegan al instante a tu cuenta IBI.



![Réception avec Lightning Address](assets/fr/04.webp)



Una vez acreditado su saldo, puede utilizar estos satoshis para efectuar pagos.



**Enviar un pago**



Para enviar satoshis, pulse "Enviar". Puede escanear un código QR de Lightning o introducir directamente un destino de Lightning Address.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Introduzca el importe deseado en satoshis, compruebe el importe equivalente en moneda local y, a continuación, confirme el pago.



![Confirmation du montant](assets/fr/07.webp)



Una notificación de éxito confirma el envío con detalles: importe enviado, comisión de transacción y destinatario.



![Paiement réussi](assets/fr/08.webp)



**Gestión de cuentas



En Ajustes, puede gestionar sus tarjetas Bitcoin NFC (Bolt Cards). La interfaz le permite activar, desactivar o establecer límites de gasto para sus tarjetas.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Para comerciantes: Panel de control para comerciantes y TPV



**Creación de cuentas de empresa



Vaya a accounts.ibi.me para crear su cuenta. Seleccione "Uso comercial" para acceder a las herramientas para comerciantes. Este tipo de cuenta desbloquea el acceso al panel de control para comercios y a los terminales de punto de venta.



Tras seleccionar "Uso comercial", se le redirigirá automáticamente al panel de control del comerciante (pay.tiankii.com). Esto le llevará a la interfaz de gestión empresarial con seguimiento de ingresos, transacciones y herramientas de pago. Para empezar a aceptar pagos, primero debe conectar su wallet Lightning haciendo clic en el enlace de la parte superior de la página (véase la flecha de la imagen).



![Dashboard marchand](assets/fr/11.webp)



**Conexión wallet Lightning**



Paso crucial para activar su punto de venta: conecte su wallet Lightning para recibir pagos. La interfaz ofrece varias opciones de conexión. Tenga en cuenta que algunas opciones (Bitcoin Onchain y Lightning Network) aún están en desarrollo y aparecen en gris en la interfaz.



![Options de connexion wallet](assets/fr/12.webp)



Para este tutorial, vamos a utilizar la conexión Lightning Address, compatible con Chivo, Blink Wallet y Strike. Introduce tu Lightning Address (formato nom@domaine.com), por ejemplo de LN Markets, Alby, o cualquier otro proveedor compatible.



![Saisie de la Lightning Address](assets/fr/13.webp)



Una vez que haya iniciado sesión, su cuenta estará operativa. Ahora puedes acceder al TPV o volver al panel de control para configurar otros ajustes.



![Connexion réussie](assets/fr/14.webp)



*enlaces de pago** *Enlaces de pago



El menú "Herramientas de pago" da acceso a "Solicitud de pago", que permite crear y gestionar enlaces de pago. Esta función es útil para generar enlaces de pago personalizados que se enviarán por correo electrónico o mensaje: donaciones, pagos únicos, pagos múltiples o incluso paywalls para proteger contenidos. Puede crear distintos tipos de enlaces para adaptarlos a las necesidades de su empresa.



![Liens de paiement](assets/fr/15.webp)



**Configuración del terminal de ventas**



Para aceptar pagos en tienda, acceda al menú "Terminal de venta" desde "Herramientas de pago". Esta sección le permite crear y gestionar sus terminales de punto de venta (el número de terminales depende de su plan, ver planes Freemium vs. Business más abajo). Haga clic en "Abrir" para abrir la interfaz de TPV en su navegador.



![Gestion des terminaux](assets/fr/16.webp)




**Generar una venta**



El terminal muestra un teclado numérico para introducir el importe de la venta. Introduzca el importe en su moneda local (por ejemplo, 500 sats corresponden a 630,74 ARS) y pulse "OK" para confirmar.



![Saisie du montant](assets/fr/17.webp)



La aplicación genera instantáneamente un código QR Lightning y una Address Lightning para el pago. Los clientes pueden escanear el código QR con su wallet o utilizar su tarjeta Bolt en un terminal NFC.



![QR code de paiement](assets/fr/18.webp)



En cuanto se recibe el pago, aparece una pantalla de confirmación con el importe recibido en moneda local y en satoshis. Puedes enviar un recibo por correo electrónico, imprimir el ticket o iniciar una nueva venta inmediatamente.



![Paiement encaissé](assets/fr/19.webp)



**Supervisión y gestión**



Todas las transacciones se registran en su panel de control de vendedor. Dispone de un seguimiento completo de los ingresos por periodo, el número total de ventas y un historial detallado para su contabilidad.



La interfaz de Configuración ofrece varias pestañas de configuración. La pestaña "Configuración general" le permite gestionar su perfil de vendedor y las notificaciones. La pestaña "Usuarios" le permite añadir y gestionar el acceso al panel de comerciante para su equipo (gestión multiusuario según su plan). La pestaña "Espacio de trabajo de desarrollo" le da acceso a las claves API para integraciones avanzadas, mientras que "Suscripción" le permite gestionar su suscripción.



![Paramètres du compte marchand](assets/fr/20.webp)



**Planes freemium vs Business



Tiankii ofrece dos paquetes para el Merchant Dashboard. El plan **Freemium** (gratuito) es adecuado para empresas de nueva creación con limitaciones: un único punto de venta, un único usuario, volumen mensual limitado a 1.000 USD y sin acceso a conectores de comercio electrónico. El plan **Business** (0,5% de comisión por transacción) ofrece terminales ilimitados, usuarios ilimitados, volumen ilimitado, acceso a los plugins WooCommerce/Shopify/Cloudbeds y notificaciones exclusivas por WhatsApp.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Ventajas y limitaciones



### Destacados



**Autocustodia**: Mantienes tus claves privadas y el control total de tus fondos. Sin riesgo de congelación de cuentas o quiebra de plataformas de terceros.



**Simplicidad**: Lightning Address como dirección de correo electrónico, pagos NFC con un simple toque, interfaz intuitiva sin necesidad de conocimientos técnicos.



**Ecosistema completo**: Herramientas para todos los perfiles (particulares, minoristas, desarrolladores) con integraciones modulares que se adaptan a tus necesidades.



**Cumplimiento profesional**: Alojamiento seguro en la nube, cumplimiento de PCI-DSS, cumplimiento de la normativa salvadoreña.



### Limitaciones



**Ligeras limitaciones**: Requiere conexión permanente wallet, gestión de liquidez para grandes volúmenes, riesgo de fallo si el destinatario está fuera de línea. Tiankii mitiga estos aspectos con LSP integrados.



**Dependencia de SaaS**: Si Tiankii no está disponible, la generación de facturas es temporalmente imposible (sus fondos permanecen seguros).



**Privacidad**: Tiankii puede observar los metadatos de las transacciones (importes, fechas). Menos privado que una solución autoalojada como BTCPay Server.



## Conclusión



Tiankii ilustra cómo una infraestructura bien diseñada puede eliminar las barreras técnicas que impiden la adopción masiva de la Bitcoin como moneda de uso cotidiano. Al combinar la potencia de la Lightning Network con un enfoque no custodial y herramientas accesibles, el ecosistema ofrece una vía equilibrada entre soberanía financiera y facilidad de uso.



Para los comerciantes, Tiankii representa una oportunidad de reducir drásticamente los costes de transacción y acceder a una nueva base de clientes. Para los consumidores, las tarjetas Lightning Address y NFC transforman la Bitcoin en una moneda práctica, sin complejidad técnica.



Aunque la adopción generalizada de la Bitcoin sigue siendo un reto que requiere educación y tiempo, infraestructuras como Tiankii demuestran que las herramientas técnicas ya existen. La misión de simplificar los pagos con Bitcoin ya no es una visión lejana, sino una realidad accesible a cualquiera que esté dispuesto a dar el paso.



## Recursos



### Documentación oficial




- [Sitio web oficial de Tiankii](https://tiankii.com)
- [Centro de Ayuda Tiankii](https://help.tiankii.com)
- [solicitud IBI](https://go.ibi.me)
- [Panel de control del comerciante](https://pay.tiankii.com)
- [Centro de Mando](https://cc.ibi.me)



### Guías de conexión Wallet




- [Conectar LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Conectar BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Conectar Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Comunidad




- [Lightning Network Plus](https://lightningnetwork.plus) - Recurso educativo sobre rayos
- [Playa Bitcoin](https://www.bitcoinbeach.com) - Iniciativa salvadoreña de economía circular Bitcoin



### Herramientas relacionadas




- [Blink Wallet](https://blink.sv) - Se recomienda Wallet Lightning compatible
- [LNbits](https://lnbits.com) - Solución wallet autoalojada
- [Tarjeta Bolt estándar](https://github.com/boltcard) - Especificaciones técnicas de las tarjetas NFC
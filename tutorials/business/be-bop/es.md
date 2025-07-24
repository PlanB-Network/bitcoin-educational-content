---
name: be-BOP
description: Guía práctica para monetizar tu negocio con be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** es una plataforma de comercio electrónico diseñada para empresarios que deseen vender en línea y fuera de línea, con total autonomía, aceptando pagos en Bitcoin, a través de una cuenta bancaria y en efectivo. La solución también es útil para cualquier tipo de organización que desee recaudar donativos o monetizar sus diversas actividades.



La solución es sencilla, ligera y autónoma. Permite crear una tienda en línea, incluso en un entorno en el que los servicios financieros tradicionales son limitados o inexistentes. De hecho, **be-BOP** se ha diseñado para funcionar eficazmente con o sin acceso a los bancos, utilizando Bitcoin como infraestructura de pago.



En este tutorial, le llevaremos paso a paso a través de :





- Cree su primera tienda en línea con **be-BOP**
- Personalice su escaparate y sus productos
- Configurar los métodos de pago disponibles
- Comprender las mejores prácticas para vender eficazmente en línea con **be-BOP**



Este tutorial no requiere conocimientos técnicos avanzados. Está dirigido tanto a desarrolladores como a artesanos, comerciantes, cooperativas o emprendedores que deseen embarcarse en el comercio digital de forma soberana y resiliente.



## Requisitos previos para instalar be-BOP en su propio servidor



Antes de empezar a instalar be-BOP, asegúrese de que dispone de la siguiente infraestructura técnica. Estos Elements son esenciales para que la plataforma funcione correctamente:



### Almacenamiento compatible con S3



be-BOP utiliza un sistema de almacenamiento para gestionar archivos (como imágenes de productos). Para ello es necesario acceder a un servicio S3, como :





- [MinIO](https://min.io/) autoalojado
- Amazon S3 (AWS)
- Almacenamiento de objetos Scaleway



Deberá configurar un cubo y proporcionar la siguiente información:





- S3_BUCKET**: nombre del cubo
- S3_ENDPOINT_URL**: enlace de acceso a su servicio S3
- S3_KEY_ID** y S3_KEY_SECRET: sus códigos de acceso
- S3_REGION**: la región de su servicio S3



### Base de datos MongoDB en modo ReplicaSet



be-BOP utiliza MongoDB para almacenar datos de tiendas, usuarios, productos y otros.



Tienes dos opciones:





- Instale MongoDB localmente con el modo **ReplicaSet activado**
- Utiliza un servicio en línea como **MongoDB Atlas**



Necesitarás las siguientes variables:





- MONGODB_URL**: conexión a la base de datos Address
- MONGODB_DB**: nombre de la base de datos



## Entorno Node.js



be-BOP funciona con Node.js. Asegúrate de que tienes **Node.js** versión 18 o superior y **Corepack** habilitado (necesario para gestionar gestores de paquetes como pnpm). El comando a ejecutar es `corepack enable`



### Git LFS instalado



Algunos recursos (como las imágenes de gran tamaño) se gestionan a través de Git LFS (Large File Storage). Asegúrate de tener instalado Git LFS en tu máquina con el comando `git lfs install`. Una vez que estos prerrequisitos están en su lugar, estás listo para pasar al siguiente paso: descargar y configurar be-BOP.



**Nota:** Una guía técnica para el despliegue de software está disponible en un tutorial separado.



## Crear una cuenta Super-Admin



La primera vez que se inicia be-BOP, se crea una cuenta **Super Admin**. Esta cuenta tiene todas las autorizaciones necesarias para gestionar las funciones de back-office. Para crear una cuenta, siga estos pasos:





- Vaya a `su_sitioweb/admin/login`
- Crear una cuenta de superadministrador con un nombre de usuario y una contraseña seguros



Esta cuenta le dará acceso a todas las funciones de back-office. Una vez creada, podrá conectarse introduciendo su nombre de usuario y contraseña.



![login](assets/fr/001.webp)



## Configuración y seguridad del back-office



Antes de configurar su conexión con el back-office de Interface, debe crear una Hash única. Esto proporciona protección contra los actores maliciosos que intentan robar el enlace de conexión a su Interface admin.



Para crear Hash, vaya a `/admin/Settings`. En la sección dedicada a la seguridad (por ejemplo, `Admin Hash`), defina una cadena única (Hash). Una vez registrado, se modificará la URL del back-office (por ejemplo, `/admin-yourhash/login`) para restringir el acceso a personas no autorizadas.



![hash-login](assets/fr/002.webp)



2.2. Activar el modo de mantenimiento (si es necesario)



Todavía en /admin/Configuración, (Configuración > General a través de los gráficos Interface) compruebe la opción "activar el modo de mantenimiento" en la parte inferior de la página.



![maintenance-mode](assets/fr/003.webp)



Si es necesario, puede especificar una lista de direcciones IPv4 autorizadas (separadas por comas) para permitir el acceso al front office durante el mantenimiento. El back office permanece accesible para los administradores.



![ip-bebop](assets/fr/004.webp)



## Configuración de las comunicaciones



Para que be-BOP pueda enviar notificaciones (por ejemplo, de pedidos, registros o mensajes del sistema), debe configurar al menos un método de comunicación. Hay dos opciones disponibles: correo electrónico (SMTP) o Nostr.



### Configuración SMTP (correo electrónico)



be-BOP puede enviar e-mails a través de un servidor SMTP. Necesitará credenciales SMTP válidas, a menudo proporcionadas por un servicio de correo electrónico (por ejemplo, Mailgun, Gmail, etc.).



Esto es lo que debe saber:



SMTP_HOST: servidor SMTP Address (por ejemplo, smtp.mailgun.org)



SMTP_PORT: el puerto a utilizar (a menudo 587 o 465)



SMTP_USER: su nombre de usuario (normalmente un correo electrónico Address)



SMTP_PASSWORD: su contraseña o clave API



SMTP_FROM: el Address de correo electrónico que aparecerá como remitente




### Configuración Nostr



be-BOP le permite enviar notificaciones a través del protocolo Nostr, una infraestructura de mensajería descentralizada. Para ello, necesita generate o Supply una clave privada de Nostr (NSEC). Puede generate esta clave directamente a través de Interface de be-BOP, en la sección dedicada a Nostr. Cuando estas Elements estén correctamente configuradas, be-BOP podrá enviar automáticamente mensajes y alertas a sus usuarios.



## Formas de pago compatibles



be-BOP es compatible con varias soluciones de pago, lo que le permite ofrecer a sus clientes una mayor flexibilidad. Esto es lo que necesita para configurar el método de pago que más le convenga.



### Bitcoin En cadena



be-BOP le permite aceptar pagos de Bitcoin directamente en Blockchain (On-Chain), de forma sencilla y segura.



**Pasos de configuración:**





- Ir al menú **Configuración de pagos**
- Haga clic en **Bitcoin Nodeless** para acceder a los parámetros de pago de On-Chain.
- Rellene los siguientes campos:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Consejo:** Para obtener su clave pública extendida (Zpub), puede consultar la configuración avanzada de su Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter, etc.). Asegúrese de que su Wallet es **no de sólo lectura** si tiene intención de utilizar el historial de transacciones.



### Lightning Network



be-BOP también puede aceptar pagos instantáneos Bitcoin gracias a Lightning Network. Actualmente hay disponibles dos opciones de configuración:



**Phoenixd**



Vaya al menú `Configuración de pagos`, haga clic en `Phoenixd`



![phoenixd](assets/fr/006.webp)



A continuación, tendrás que introducir **la contraseña o autenticación token** que te conecta a tu instancia Phoenixd, un backend desarrollado por Acinq que te permite gestionar pagos Lightning con tu propio nodo, pero sin la complejidad de gestionar canales de pago.



**Swiss Bitcoin Pay**



Si no quieres gestionar tú mismo un nodo Lightning, **Swiss Bitcoin Pay** es una solución lista para usar y fácil de configurar, ideal para empezar a aceptar pagos Lightning sin una infraestructura compleja.



Pasos de configuración :





- En el menú "Opciones de pago", haga clic en `Swiss Bitcoin Pay`
- Acceda a su cuenta de Swiss Bitcoin Pay (o cree una si aún no la tiene).
- Introduzca la clave API proporcionada por Swiss Bitcoin Pay y, a continuación, haga clic en "Guardar"



Una vez configurado, be-BOP emitirá automáticamente facturas generate Lightning para sus clientes, y usted recibirá los pagos directamente en su cuenta suiza Bitcoin Pay. Esta solución es ideal para usuarios que desean evitar la complejidad técnica de un nodo personal y, al mismo tiempo, aceptar pagos rápidos y de bajo coste.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Además de Bitcoin, be-BOP también le permite aceptar pagos en efectivo a través de PayPal, una solución internacional muy conocida y utilizada.



Pasos de configuración :





- Ir al menú `Configuración de pagos
- Haga clic en `PayPal
- En su cuenta Paypal (sección desarrollador), introduzca el `Client ID` y el `Secret`
- Seleccione la divisa de su elección (por ejemplo, **USD**, **EUR**, **XOF**, etc.)
- Haga clic en `guardar



![paypal](assets/fr/008.webp)



**Nota:** Debe tener una cuenta PayPal Business para generate estos identificadores. Puede obtenerlos a través del portal [desarrollador] (https://developer.paypal.com)



### SumUp



El software integra ahora la solución de pago **SumUp**, que permite aceptar pagos con tarjeta de crédito de forma sencilla, segura y eficaz. Para beneficiarse de esta funcionalidad, es necesaria una configuración inicial. He aquí los pasos a seguir, numerados para una implantación clara y progresiva:





- Empiece introduciendo su **clave API**, una clave confidencial que SumUp le proporcionó cuando creó su cuenta de desarrollador. Establece una conexión segura entre su cuenta de SumUp y el software.
- Rellene el campo `Código de comerciante` con el código único que identifica a su negocio dentro de la plataforma SumUp. Este código es esencial para asociar las transacciones a su negocio.
- En el campo `Moneda`, elija la moneda principal que utiliza para sus transacciones (por ejemplo, **EUR**, **USD**, **CDF**, etc.).
- Una vez que haya rellenado todos los campos correctamente, haga clic en el botón `Guardar` para guardar la configuración. El sistema establecerá el enlace con su cuenta de SumUp y su software estará listo para aceptar pagos.



![payment-sumup](assets/fr/009.webp)



Tras esta configuración, la integración de **SumUp** estará activa y operativa, permitiéndole cobrar rápidamente y realizar un seguimiento de sus transacciones directamente desde el software.



### Raya



be-BOP también ofrece integración completa con **Stripe**, una de las plataformas de pago en línea más populares. Stripe le permite aceptar pagos en línea a través de tarjeta de crédito, Wallet digital y varios otros métodos de pago. He aquí cómo activarlo:





- Introduzca la **clave secreta** proporcionada en el panel de Stripe.
- Rellene el campo **Clave pública**, también proporcionado por Stripe.
- Seleccione la **moneda principal**.
- Guarde la configuración y haga clic en `Guardar`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Por favor, tenga en cuenta:** Es imprescindible conocer el régimen de IVA aplicable a su actividad (por ejemplo: venta bajo IVA en el país del vendedor, exención bajo justificación, o venta al tipo de IVA del país del comprador) para configurar correctamente las opciones de facturación en **be-BOP**.



## Configuración de divisas



**be-BOP** ofrece una gestión avanzada de divisas y se adapta a entornos multidivisa y a requisitos contables específicos. Para garantizar la coherencia de las operaciones y los informes financieros, es esencial configurar correctamente las distintas divisas utilizadas en el sistema. A continuación se indican los pasos a seguir para esta configuración:





- Seleccione la **moneda principal** (`Main currency`)
- Seleccione `Moneda secundaria
- Definir **moneda de referencia** (`Moneda de referencia del precio`)
- Indique `Moneda contable



Una vez configuradas correctamente todas las divisas, el software garantiza la conversión automática y precisa de las transacciones multidivisa, manteniendo al mismo tiempo una rigurosa coherencia contable.



![settings-currencies](assets/fr/011.webp)



## Configuración del acceso de recuperación por correo electrónico o Nostr



Siempre en `/admin/settings`, a través del módulo **ARM**, asegúrate de que la cuenta de superadministrador incluye un **email Address** o un **recovery pub**, facilitando así el procedimiento si olvidas tu contraseña.



![settings-users](assets/fr/012.webp)



## Ajustes de idioma



El software ofrece capacidad multilingüe para adaptarse a un público internacional y mejorar la experiencia del usuario. Para activar la funcionalidad multilingüe, es importante configurar los idiomas disponibles y definir un **idioma predeterminado**.



![settings-languages](assets/fr/13.webp)



## Interface y configuración de identidad en be-BOP



**be-BOP** proporciona a los diseñadores todas las herramientas que necesitan para diseñar un sitio web. El primer paso es abrir la sección `/Admin > Merch > Layout` en los ajustes. Empieza configurando la **barra superior**, la **barra de navegación** y el **pie de página**.



### Le Top Bar



La configuración **Barra superior** le permite personalizar la identidad visual de su software mostrando información clave desde la primera línea de Interface. Esto refuerza el reconocimiento de la marca y proporciona un contexto claro para los usuarios.



#### Pasos de configuración :





- En el campo "Nombre de marca", introduzca el nombre de su empresa, organización o producto. Este nombre aparecerá en la parte superior de la Interface y representará su identidad visual principal.
- Indique el título del sitio web**: el título elegido debe resumir la finalidad de la plataforma. Este título puede aparecer en la cabecera o en la pestaña del navegador.
- Añadir descripción del sitio web**: aquí es donde debe introducir una breve descripción de su iniciativa. Esta descripción ayuda a contextualizar la herramienta para los usuarios y también puede utilizarse con fines de SEO.



Una vez introducida esta información, la **barra superior** mostrará una presentación clara, profesional y coherente de su solución.



#### Enlaces en la barra superior



La sección `Enlaces` de la barra superior le permite añadir accesos directos a páginas importantes de su aplicación o de sitios externos. Estos enlaces se muestran directamente en la barra superior, ofreciendo a los usuarios un acceso rápido y estructurado.



#### Pasos de configuración :





- Introduzca el nombre del enlace (Texto)**: en el campo `Texto`, introduzca el nombre o etiqueta del enlace tal y como aparecerá (por ejemplo, Inicio, Contacto, Ayuda...).
- Indicar enlace Address (Url)**: en el campo `Url`, introduzca el Address completo de la página de destino (interna o externa).
- Añada otros enlaces si es necesario**: cada línea de configuración le permite añadir un enlace adicional utilizando los campos `Text` y `Url`.
- Guardar enlaces**: una vez introducidos todos los enlaces, haga clic en el botón "Añadir enlace de la barra superior" para guardarlos.



Esta configuración le permite ofrecer una navegación clara, fluida y accesible por las distintas secciones de su sitio web o hacia recursos complementarios.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



La sección **Navbar** le permite configurar el menú de navegación principal de su be-BOP, normalmente situado en la parte lateral o superior de la Interface. Este menú guía a los usuarios a las distintas páginas y funciones de la aplicación. Este menú guía a los usuarios a las distintas páginas y funciones de la aplicación. La configuración del enlace es sencilla e intuitiva. Funciona de la siguiente manera:





- Introduzca el nombre del enlace (`Text`)**: en la línea de configuración, comience rellenando el campo `Text`. Corresponde al nombre del enlace que aparece en la barra de navegación (ejemplos: *Dashboard*, *Users*, *Settings*...).
- Introduzca el Address del enlace (`Url`)**: junto al campo `Text`, encontrará el campo `Url`. En este campo, introduzca el Address de la página a la que debe redirigir el enlace. Puede ser una ruta interna o un enlace a una página externa.
- Añadir varios enlaces si es necesario**: debajo de la primera línea, hay nuevos campos `Text` y `Url` disponibles para añadir tantos enlaces como sea necesario. Cada línea representa un enlace de navegación adicional.
- Guardar enlaces**: una vez que haya introducido todos los Elements, haga clic en el botón `Añadir enlace a la barra de navegación` para guardar y mostrar los resultados en la barra de navegación.



Esta configuración permite estructurar eficazmente el acceso a las distintas partes del software, mejorando la ergonomía y la experiencia del usuario.



![navbar](assets/fr/015.webp)



### Pie de página



La sección **Pie de página** le permite personalizar el pie de página de su programa, añadiendo información útil o enlaces. Antes de configurar los enlaces, empieza por activar una opción específica:





- Activar la visualización de la etiqueta "Powered by be-BOP "**: active el botón `Display Powered by be-BOP` para mostrar esta etiqueta en el pie de página.
- Introduzca el nombre del enlace (`Text`)**: rellene el campo `Text`, que corresponde al texto del enlace en el pie de página (ejemplos: *Condiciones generales*, *Privacidad*, *Contacto*...).
- Indicar enlace Address (`Url`)**: en el campo `Url`, introduzca el Address de la página de destino (interna o externa).
- Añada más enlaces si es necesario**: utilice las líneas adicionales para crear tantos enlaces como desee.
- Guardar enlaces**: haga clic en el botón "Añadir enlace a pie de página" para guardar los enlaces.



![footer](assets/fr/016.webp)



### Personalización visual



**⚠️ No olvide configurar los logotipos para los temas claro y oscuro, así como el favicon, a través de** `Admin > Merch > Pictures`.



A continuación te explicamos cómo personalizar el aspecto de tu sitio web:



#### Ir a la sección Imágenes



Menú `Admin` > `Merch` > `Imágenes`.



#### Añadir una nueva imagen



Haz clic en `Nueva imagen`.



#### Seleccione un archivo local



Haga clic en "Elegir archivos" y seleccione una imagen de su disco Hard.



#### Seleccione el archivo que desea importar



Haga doble clic en la imagen que desea importar (logotipo claro, logotipo oscuro o favicon).



#### Poner nombre a la imagen



Rellene el campo `Nombre de la imagen`.



#### Añadir imagen



Haga clic en `Añadir` para finalizar la importación.



![pictures](assets/fr/017.webp)



### Configuración de la identidad del vendedor



#### Configuración de la identidad



Accesible a través de `Admin > Identidad` (o `Configuración > Identidad`), esta sección le permite configurar la información administrativa y legal de su empresa.



#### Información jurídica





- Razón social**: nombre oficial de la empresa.
- Identificación de la empresa**: identificador legal o número de registro (RCCM, SIRET...).



#### Address empresarial





- Calle**: Address postal (calle, número...).
- País**: país.
- Estado**: provincia o región.
- Ciudad**: ciudad.
- Código postal**: código postal.



#### Información de contacto





- Correo electrónico**: correo electrónico profesional Address.
- Teléfono**: número de teléfono de la empresa.



#### Cuenta bancaria





- Nombre del titular de la cuenta**: nombre del titular de la cuenta.
- Titular de la cuenta Address**: Address del titular.
- IBAN**: Número internacional de cuenta bancaria.
- BIC**: Código SWIFT/BIC.



![bank-account](assets/fr/019.webp)



#### Facturación





- Haga clic en "Rellenar con la información principal de la tienda" para rellenar los datos.
- Información del emisor muy arriba a la derecha**: campo para la información legal/tributaria visible en las facturas.
- Haga clic en "Actualizar" para guardar los cambios.



**Nota:** también puede introducir información adicional para que aparezca en la Invoice, según sus necesidades.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Tienda física Address



Para quienes tengan una tienda física, añada un Address completo específico en `Admin > Configuración > Identidad` o una sección dedicada. Esto permitirá que aparezca en los documentos oficiales y en el pie de página si es necesario.



![seller-id](assets/fr/021.webp)



## Gestión de productos



### Crear un nuevo producto



Vaya a `Admin > Merch > Products` para añadir o modificar un producto. Rellene los siguientes campos:



#### Información básica





- Nombre del producto**: nombre del producto (por ejemplo, *BOP T-shirt limited edition*).
- Slug**: Identificador de URL sin espacios (por ejemplo, `tshirt-bop-edition-limitee`).
- Alias** *(opcional)*: útil para añadir rápidamente a la cesta mediante un campo específico.



![product-config](assets/fr/028.webp)



#### Precios





- Precio Importe**: precio del producto (por ejemplo, `25,00`).
- Divisa del precio**: divisa (EUR, USD, BTC, etc.).
- Productos especiales** :
  - este es un producto gratuito.
  - este es un producto de pago por uso.



#### Opciones de productos





- Producto único (`standalone`)**: sólo es posible un añadido por pedido (por ejemplo, donación, entrada).
- Producto con variaciones** :
  - No compruebes `Standalone`.
  - Marque `El producto tiene ligeras variaciones (no hay diferencia de stock)`.
  - Añadir :
    - Nombre** (por ejemplo, *Tamaño*),
    - Valores** (por ejemplo: S, M, L, XL),
    - Diferencias de precio** si procede (por ejemplo: `+2 USD` para XL).



![product-details](assets/fr/029.webp)



## Gestión de existencias



### Opciones avanzadas al crear un producto (Stock, Entrega, Tickets, etc.)



#### Producto con existencias limitadas



Si su producto no está disponible en cantidades ilimitadas, marque `El producto tiene un stock limitado`. Esto activa el seguimiento automático de las cantidades restantes. Una vez marcada esta casilla, aparecerá un campo para indicar el **stock disponible**.



El sistema gestiona :





- Existencias reservadas** → productos de las cestas aún no pagados
- Existencias vendidas** → productos ya comprados



**Tiempo de reserva de la cesta**: Cuando un cliente añade un producto a su cesta, éste queda "reservado" durante un tiempo limitado. Puede modificar este tiempo en: `Admin > Config > Reserva de cesta` (valor en minutos)



#### ¿Producto a entregar?



Marque `El producto tiene un componente físico que se enviará al Address del cliente`. Esto es útil para todos los productos que se enviarán físicamente (libros, camisetas, etc.)



#### Otras opciones





- Entrada**: marque esta casilla si el producto es una entrada para un evento
- Reserva**: compruebe si se trata de una franja horaria de reserva (por ejemplo: sesión, cita)



![product-options](assets/fr/030.webp)



### Ajustes de acción (abajo)



Esta sección determina **dónde** y **cómo** se puede ver y comprar el producto:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Marque sólo los canales que desee utilizar.



## Creación y personalización de páginas y widgets CMS



### Páginas CMS obligatorias



Vaya a `Admin > Merch > CMS`. Verás una lista de páginas existentes y puedes añadir nuevas con **Añadir página CMS**.



Las páginas CMS son importantes para :





- Informe a sus visitantes (por ejemplo, condiciones de uso)
- Cumplir la ley (por ejemplo, la política de privacidad)
- Explicar determinadas características de la tienda (por ejemplo, recogida de IP, 0% de IVA)



Si lo desea, puede añadir otras páginas:





- Quiénes somos
- Ayúdenos / Donaciones
- PREGUNTAS FRECUENTES
- Póngase en contacto con
- etc.



**Consejo: Haga clic en cada enlace o icono para modificar el **contenido**, el **título** o la **visibilidad** de cada página.



### Maquetación y gráficos Elements



Vaya a : `Admin > Merch > Layout`. Puede personalizar el Elements visual de su sitio:



![product-options](assets/fr/032.webp)



#### Barra superior





- Modificar o eliminar enlaces (EX: HOME, ABOUT US,...)
- Navegación entre las principales secciones del sitio



#### Navbar (barra de navegación principal)





- Presente en la zona gris debajo de la barra superior
- Contiene acceso rápido a : `Configurar`, `Configuración de pagos`, `Transacciones`, `Gestión de nodos`, `Widgets`, etc.
- Sólo directores



#### Pie de página





- Editable desde `Admin > Merch > Layout`
- Contiene: información de contacto, enlaces útiles, avisos legales..



#### Personalizar los elementos visuales



Ir a: `Admin > Merch > Pictures`



Puede :





- Cambiar el **logotipo principal**
- Modificar o añadir diseño **imágenes**



#### Descripción



También modificable en `Imágenes`, permite mostrar un **resumen o eslogan** en la cabecera o pie de página, según el tema.



**Nota:** esto le permite ajustar la apariencia a su identidad de marca (educativa, comercial o comunitaria).



### Integración de widgets en páginas CMS



Los widgets** enriquecen sus páginas CMS con Elements dinámicos o visuales.



#### Creación de widgets



Vaya a: `Admin > Widgets`



Ejemplos de widgets disponibles:





- Desafíos**: desafíos o misiones
- Etiquetas**: categorías o palabras clave
- Sliders**: carruseles de imágenes
- Especificaciones** : Tablas de especificaciones
- Formularios**: formularios (contacto, comentarios, etc.)
- Cuenta atrás**: temporizadores
- Galerías**: galerías de imágenes
- Tablas de clasificación**: clasificaciones de los usuarios



![widgets](assets/fr/033.webp)



#### Integración en páginas CMS



Utilice **códigos cortos** en el contenido de sus páginas CMS:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Parámetros actuales** :





- `slug`: identificador único del widget
- `display=img-1`: imagen específica del producto
- `width`, `height`, `fit`: dimensiones y estilo de la imagen
- autoplay=3000`: tiempo en ms entre dos diapositivas



**Ventajas** :





- Fácil de insertar (copiar y pegar)
- Dinámico: cualquier modificación del widget se refleja automáticamente
- No necesita programador



## Gestión de pedidos e informes



### Seguimiento de pedidos



Para ver y gestionar pedidos anteriores, vaya a: `Admin > Transacción > Pedidos`



Aquí encontrará la **lista completa de los pedidos** realizados en su sitio.



![orders](assets/fr/034.webp)



#### Visualización y búsqueda



La Interface permite buscar y filtrar pedidos según varios criterios:





- número de pedido: número de pedido
- alias del producto: identificador o nombre del producto
- medio de pago": medio de pago utilizado (tarjeta, criptomoneda, etc.)
- `Email`: correo electrónico del cliente



Estos filtros facilitan las búsquedas rápidas y la gestión selectiva.



#### Detalles de cada pedido



Al hacer clic en un pedido, puede acceder a un archivo completo que contiene :





- Productos solicitados
- Información al cliente
- Entrega Address (si procede)
- Cualquier nota asociada a la orden



#### Posibles acciones sobre una orden



Puede :





- Confirmar pedido (si está pendiente)
- Cancelar un pedido (en caso de problema o petición del cliente)
- Añadir **etiquetas** (para organización interna)
- Consultar / añadir **notas internas**



**Nota:** esta sección es esencial para una buena logística y relación con el cliente.



### Informes y exportación



Para acceder a las estadísticas de ventas y pagos :


administrador > Configuración > Informes



![reporting](assets/fr/035.webp)



Aquí encontrará una visión general de su negocio, en forma de **informes mensuales y anuales**.



#### Contenido del informe



Los informes se dividen en secciones:





- Detalle del pedido**: número de pedidos, estado (confirmado, cancelado, pendiente), evolución
- Detalle del producto**: productos vendidos, cantidades, productos populares
- Detalle de los pagos**: importes cobrados, desglose por forma de pago



#### Exportación de datos



Cada sección incluye un botón **Exportar CSV**, que permite :





- Descargar datos en formato CSV
- Ábrelos en Excel, Google Sheets, etc.
- Archivado para uso administrativo o contable
- Utilícelos para informes internos



**Nota:** ideal para el seguimiento del rendimiento, la contabilidad y las presentaciones.



## Configuración de Nostr Messaging (opcional)



![nostr-config](assets/fr/036.webp)



La plataforma es compatible con el protocolo **Nostr** para determinadas funciones avanzadas:





- Notificaciones descentralizadas
- Iniciar sesión sin contraseña
- Interface administración ligera



### Generar y añadir la clave privada de Nostr



Ir a :


admin > Gestión de nodos > Nostr





- Haz clic en **Crear nsec** si no tienes uno.
- El sistema puede generate automáticamente.
- También puede utilizar una llave existente (por ejemplo, de Damus o Amatista).



Siguiente:





- Copiar la clave `nsec
- Añádalo a su archivo `.env.local` (o `.env`): ```env NOSTR_PRIVATE_KEY=TuNsecIciKey



### Funciones activadas con Nostr



Una vez configurado, dispone de varias funciones:



**Notificaciones a través de Nostr**





- Enviar alertas de pedidos, pagos o eventos del sistema
- Para administradores o usuarios



**Interface administración ligera**





- Accesible a través de un cliente Nostr
- Permite una gestión rápida y móvil



**Conexión sin contraseña**





- Inicio de sesión mediante enlace seguro (enviado a través de Nostr)
- Mayor seguridad y fluidez para el usuario



## Diseño y personalización de temas



Para adaptar la apariencia de su tienda a su carta gráfica, vaya a: `Admin > Merch > Theme`



Aquí encontrarás todas las opciones para **crear** y **configurar** un tema personalizado.



### Crear un tema



![theme](assets/fr/037.webp)



Al crear o modificar un tema, puede definir :





- Colores**: para botones, fondos, texto, enlaces, etc.
- Tipos de letra**: elección de tipos de letra para títulos, párrafos y menús
- Estilos gráficos**: bordes, márgenes, espaciado, formas de bloque



### Secciones personalizables



Cada parte del sitio puede ajustarse de forma independiente:





- Cabecera**: barra de navegación superior
- Cuerpo**: contenido principal
- Pie de página** : parte inferior de la página



**Nota:** esta granularidad garantiza la coherencia entre los elementos visuales del sitio y la identidad de su marca.



### Activación del tema



Una vez configurado el tema :





- Haga clic en **Guardar**
- Activarlo como **tema principal** de la tienda



**Nota:** el tema activo es el que será visible para los visitantes.



## Configuración de plantillas de correo electrónico



La plataforma permite personalizar los correos electrónicos que se envían automáticamente a los usuarios. Vaya a: `Admin > Configuración > Plantillas`



![emails-templates](assets/fr/038.webp)



### Creación / edición de plantillas



Cada correo electrónico (confirmación de pedido, contraseña olvidada, etc.) tiene :





- Asunto**: el asunto del correo electrónico (por ejemplo, "Su pedido ha sido validado")
- Cuerpo HTML**: Contenido HTML mostrado en el correo electrónico



**Nota:** puede insertar texto, imágenes, enlaces, etc., según sea necesario.



### Uso de variables dinámicas



Para que los correos electrónicos sean dinámicos, inserte variables como :





- `{orderNumber}}` : sustituido por el número de pedido real
- `{invoiceLink}}` : enlace a la Invoice
- `{websiteLink}}`: URL de su sitio web



**Nota:** estas etiquetas se sustituyen automáticamente cuando se envían.



### Consejos avanzados





- Crear mensajes de correo electrónico **responsivos** para facilitar su lectura en dispositivos móviles
- Añadir **botones de acción** (pago, descarga, seguimiento del pedido)
- Pruebe sus correos enviándoselos a sí mismo antes de publicarlos



## Configuración de etiquetas y widgets específicos



### Gestión de etiquetas



Las etiquetas permiten estructurar y enriquecer los contenidos. Para acceder a ellas: `Admin > Widgets > Etiqueta`



![tags-config](assets/fr/039.webp)



### Crear una etiqueta



Rellene los siguientes campos:





- Nombre de la etiqueta**: nombre de la etiqueta mostrada
- Slug**: identificador único (sin espacios ni acentos)
- Familia de etiquetas**: agrupa las etiquetas por categorías



![targsconfig](assets/fr/040.webp)



#### Familias disponibles :





- creadores`: autores o productores
- minoristas: vendedores o puntos de venta
- `Temporal`: periodos o fechas
- eventos: eventos asociados



### Campos opcionales



Estos campos pueden utilizarse para enriquecer una etiqueta como si fuera una página de contenido:





- Título
- Subtítulo
- Contenidos breves
- Contenido completo** (en francés)
- CTA** (botones de acción)



### Uso de etiquetas



Las etiquetas pueden ser :





- Asignado a productos
- Integrado en páginas CMS con una etiqueta: [Tag=slug?display=var-1]



## Configuración de archivos descargables



Para ofrecer documentos descargables a sus clientes: `Admin > Merch > Files`



### Añadir un archivo



1. Haga clic en **Nuevo archivo**


2. Inform :




   - Nombre del archivo** (por ejemplo, *Guía de instalación*)
   - Archivo a cargar** (PDF, imagen, Word...)



**Nota:** una vez añadido, la plataforma genera automáticamente un **enlace permanente**.



### A través del enlace



Este enlace puede insertarse en :





- Página CMS** (como enlace de texto o botón)
- Un **cliente de correo electrónico** (a través de una plantilla)
- Una **hoja de producto** (por ejemplo, descarga del manual)



Es ideal para proporcionar *manuales de usuario, guías técnicas, fichas de producto...* sin necesidad de alojamiento externo.



## Nostr-bot



La plataforma ofrece integración avanzada con el protocolo **Nostr**, a través de un bot automatizado.



Vaya a : nodo Gestión > Nostr



### Características principales



#### Gestión de relés





- Añadir o eliminar **relés** utilizados por el bot
- Optimizar el **alcance** y la **fiabilidad** de los mensajes enviados



#### Mensaje automático de introducción





- Activar un mensaje automático en **primera interacción del usuario**
- Ideal para :
  - Presentar su servicio
  - Enviar un enlace útil (por ejemplo, FAQ, contacto, pedido)



#### Certificación de su `pub





- Añade un **logotipo** y un **nombre público**
- Enlace a un **dominio web verificado**
- Aumenta la credibilidad y el reconocimiento de su identidad Nostr



### Casos de uso de Nostr-bot





- Le enviamos **confirmaciones de pedido**
- Respuesta automática a **eventos (por ejemplo, un nuevo pedido)**
- Crear una **interacción descentralizada con el cliente**



## Sobrecarga de etiquetas de traducción



be-BOP es multilingüe (FR, EN, ES...), pero puede adaptar las traducciones a sus necesidades.



Para ello, vaya a: `Configuración > Idioma`



### Carga y edición



Los archivos de traducción están en JSON. Puede :





- Descargar** archivos de idioma
- Modificar** textos existentes
- Añade** tus propias traducciones



Enlace a los archivos originales :


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Ejemplo:** sustituye `Add to cart` por `Ajouter au panier` o `Acheter`.



## Trabajo en equipo y punto de venta (TPV)



### Gestión de usuarios y derechos de acceso



#### Creación de roles



Vaya a: `Admin > Configuración > ARM`



Haga clic en **Crear un rol** para crear un rol (por ejemplo, `Super Admin`, `POS`, `Ticket checker`).



Cada rol contiene :





- acceso de escritura**: acceso de escritura
- acceso de lectura**: acceso de lectura
- acceso prohibido**: secciones interdites



#### Creación de usuarios



En el mismo menú `Admin > Configuración > ARM`, añada un usuario con :





- inicio de sesión
- alias
- recuperación de correo electrónico
- (opcional) `recovery npub` para conexión vía Nostr



Asignar un rol previamente definido.



![pos-users](assets/fr/045.webp)



Los usuarios de sólo lectura** verán los menús en *itálica* y no podrán modificar el contenido.



## Configuración del punto de venta (TPV)



### Asignación del rol POS



Para dar acceso a un usuario al TPV, asigne el rol `Punto de Venta (TPV)` en: `Admin > Config > ARM`



Puede conectarse a través de la URL segura `/pos` o `/pos/touch`



### Funciones específicas para TPV



Be-BOP ofrece una Interface dedicada a las ventas físicas (tienda, evento, etc.).



#### Adición rápida mediante alias



En `/cart`, un campo permite añadir un producto:





- Escaneando un **código de barras** (ISBN, EAN13)
- Introduciendo un **alias de producto** manualmente



**Nota:** el producto se añade automáticamente a la cesta.



#### Medios de pago



POS soporta :





- Especie
- Tarjeta de crédito
- Lightning Network (criptografía)
- Otros según configuración



Existen dos opciones avanzadas:





- Exención del IVA** : aplicable a la justificación (ONG, extranjeros...)
- Descuento regalo**: descuento excepcional con comentario obligatorio



#### Visualización en el cliente



La URL `/pos/session` está destinada a una **pantalla secundaria** (HDMI, tableta...):



Cartel:





- Productos en curso
- Importe total
- Forma de pago
- Descuentos aplicados



**Nota:** el cliente sigue el pedido en directo, mientras que el vendedor lo registra en `/pos`.



### Resumen del TPV



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Gracias por seguir atentamente este tutorial.
---
name: Peach
description: Guía completa para utilizar Peach y comerciar con bitcoins en P2P
---

![cover](assets/cover.webp)





## Introducción



Los intercambios peer-to-peer (P2P) libres de KYC son esenciales para preservar la confidencialidad y la autonomía financiera de los usuarios. Permiten transacciones directas entre particulares sin necesidad de verificar la identidad, lo que es crucial para quienes valoran la privacidad. Para profundizar en los conceptos teóricos, consulte el curso BTC204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. ¿Qué es la Peach?



Peach es una plataforma de intercambio P2P que permite a los usuarios comprar y vender bitcoins sin KYC. Ofrece una interfaz intuitiva y funciones de seguridad avanzadas. Comparada con otras soluciones como Bisq, HodlHodl y Robosat, Peach destaca por su facilidad de uso.


Un sistema de custodia (2-2) de multisig garantiza la seguridad de los fondos durante las transacciones. Peach admite varios métodos de pago y cuenta con un sistema de reputación para guiar a los comerciantes en sus acciones. Por lo tanto, como es habitual en las plataformas P2P, es importante mantener una buena reputación para conservar la credibilidad ante otros operadores.



### 2. Privacidad y datos recogidos



**¿Qué información recopila Peach?



Peach se esfuerza por almacenar el mínimo absoluto de datos sobre sus usuarios. He aquí un resumen de los datos almacenados en nuestros servidores:





- Un hash de su identificador único de solicitud (AdID)
- Un hash de sus datos de pago
- Tus conversaciones encriptadas
- Datos de las transacciones para garantizar que los usuarios anónimos no superan el límite de negociación (tipos de métodos de pago utilizados, importes de compra y venta)
- Addresses utilizado para enviar y recibir de la cuenta de garantía bloqueada
- Datos de uso (Firebase y Google Analytics), sólo con su consentimiento



Como recordatorio, un hash son datos que se vuelven irreconocibles, de forma similar a la encriptación. Los mismos datos siempre producirán el mismo hash, lo que permite detectar duplicados sin conocer los datos originales.



*Para una explicación más detallada de hashing, siga este curso:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**¿Quién puede ver mis datos de pago?





- Sólo su contraparte puede ver sus datos de pago
- Los datos se transmiten a través de los servidores de Peach, pero están totalmente encriptados de extremo a extremo
- En caso de litigio, los datos de pago y el historial de conversaciones serán visibles para el mediador asignado de Peach



## Instalación y configuración



### 1. Instalar la aplicación Peach



![Installation de Peach](assets/fr/01.webp)





- Descarga la aplicación desde [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). En iOS, primero tendrás que instalar la aplicación [testflight](https://apps.apple.com/us/app/testflight/id899247664).
- Sigue las instrucciones de instalación de tu dispositivo.
- Durante la instalación, se te pedirá que elijas si deseas compartir determinados datos para mejorar la aplicación Peach. (imagen 1)
- En la siguiente pantalla (imagen 2), tiene dos opciones:
 - Si es un nuevo usuario, haga clic en "Nuevo usuario" para crear un nuevo perfil
 - Si ya tiene una cuenta, utilice "Restaurar" para restaurar su perfil existente
- Si tiene un código de referencia, puede introducirlo aquí.
- Para restaurar una cuenta existente (imagen 3), necesitarás :
 - Su archivo de copia de seguridad
 - La contraseña para descifrar este archivo



### 2. Vista general de las pantallas principales



La aplicación Peach está organizada en torno a cuatro pantallas principales accesibles desde la barra de navegación inferior:



![Navigation dans l'application](assets/fr/02.webp)





- Inicio (4)** : La pantalla principal desde la que puede elegir comprar o vender, crear nuevas transacciones y acceder a las ofertas disponibles:
 - crear ofertas con los dos botones de abajo (crear compra / crear venta)
 - aprovechar las ofertas existentes creadas por otros usuarios, utilizando los dos botones de abajo ("Comprar"/"Vender").





- Wallet (5)** : Su bitcoin integrado wallet que le permite :
 - Compruebe su saldo
 - Recibir bitcoins
 - Envoyer bitcoins (con control de monedas)
 - Consultar el historial de transacciones
 - Financiar sus ventas





- Operaciones (6)**: tus contratos actuales y pasados, en tres pestañas:
 - Compras en curso
 - Ventas en curso
 - La historia de sus intercambios





- Configuración (7)** : El centro de configuración para
 - Ver tu perfil (reputación, insignias, límites, etc.)
 - Gestión de la seguridad (copia de seguridad, pin)
 - Gestione sus medios de pago
 - Contactar con el servicio de asistencia
 - Cambiar de idioma
 - etc.



### 3. Configure sus métodos de pago



![Accès aux paramètres de paiement](assets/fr/03.webp)



Puedes gestionar tus métodos de pago en los ajustes (imagen 8)



Peach ofrece pagos en línea y presenciales (sólo en los encuentros registrados).



**Pagos en línea



**Importante:**


para proteger a los usuarios, Peach exige que el origen de los fondos coincida con el anunciado. Corresponde a los comerciantes asegurarse de que así sea, por su propia protección.



![Configuration des paiements en ligne](assets/fr/04.webp)



Para añadir un método :




- En la pestaña "en línea", haga clic en "añadir una divisa/método"
- Elija su moneda
- Seleccione su forma de pago preferida



*Tipos de métodos de pago disponibles:*



***Para transferencias bancarias: ***




- SEPA (estándar o instantánea)
- Introduzca sus datos bancarios SEPA.



***Se aceptan wallet en línea :***




- Varias opciones disponibles en función de su país (Revolut, Paypal, Wise, Strike, etc.)
- Siga las instrucciones para añadir sus datos de acceso



*tarjeta regalo utilizable:*** Tarjeta regalo utilizable:*** Tarjeta regalo utilizable:*** Tarjeta regalo utilizable:*** Tarjeta regalo utilizable:*** Tarjeta regalo utilizable:***




- Amazon, Steam, etc.
- Introduzca el país de emisión de la tarjeta y otra información necesaria



***Opciones de pago nacionales:***


Sistemas de pago específicos de cada país :




- Satispay (Italia)
- MB Way (Portugal)
- Bizum (España)
- Pagos más rápidos (Reino Unido)
- etc.



***Para pagos presenciales: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Seleccione "Meetup" (imagen 12)
- A continuación, seleccione su reunión en la lista (imagen 13)



### Instrucciones de uso





- Puede añadir varios métodos de pago
- Cuantos más métodos añadas, mayor será la gama de ofertas a las que tendrás acceso
- Compruebe la exactitud de sus datos antes de inscribirse
- Puede cambiar o eliminar sus métodos de pago en cualquier momento



**Nota de seguridad**: Su información de pago está encriptada y sólo se comparte con su socio de intercambio durante una transacción, excepto en caso de disputa, donde un mediador de Peach también tendrá acceso.



### 4. Cómo asegurar su cartera



**Comprender su cuenta Peach



Una cuenta Peach no tiene nombre de usuario ni contraseña. Es un archivo almacenado localmente en tu teléfono, lo que significa que Peach no necesita almacenar tus datos ni conocer tu identidad: tú tienes el control. Este archivo contiene todos tus datos: incluyendo las 12 palabras de recuperación de bitcoin, las claves PGP, los detalles de pago y demás. Así que es crucial guardar este archivo y protegerlo con una contraseña __robust__.



Este enfoque garantiza cierto grado de confidencialidad y deja la responsabilidad de la gestión de los datos y las copias de seguridad en manos del usuario. Perder el teléfono sin una copia de seguridad significa perder el acceso a la cuenta y los fondos de Peach.



**Crea tus copias de seguridad**






- Accede a los ajustes desde la pestaña situada en la parte inferior derecha de la pantalla de inicio
- Seleccione la opción "copias de seguridad" en el menú de configuración



![Processus de sauvegarde](assets/fr/06.webp)



Existen dos tipos de copias de seguridad:



**Guardar archivo de cuenta (imagen 14)**




- Haga clic en "Crear nueva copia de seguridad"
- Crea una contraseña **fuerte** para cifrar tu archivo de copia de seguridad
- Envía este archivo a un lugar que garantice su redundancia en caso de pérdida del teléfono.



La copia de seguridad de archivos restaura su cuenta Peach completa, incluidos los archivos :




- Su cartera
- Sus formas de pago
- Datos de pago
- Historial de transacciones con detalles de las contrapartes y conversaciones con ellas



**Guardando la frase de recuperación (imagen 15)**




- Siga las instrucciones para visualizar su frase de recuperación
- Escribe cuidadosamente las palabras en el orden correcto
- Guarde esta copia de seguridad en un lugar seguro, idealmente distinto del archivo de la cuenta



La frase de recuperación permite recuperar :




- Su reputación, sus operaciones
- Tus fondos en bitcoin



Pero **NO** lo siguiente:




- Sus conversaciones actuales y pasadas
- Datos de pago
- Información sobre la contraparte en el historial de transacciones




## Compra y venta de bitcoins



### 1.a Cómo comprar bitcoins: Acepte una oferta de venta



El primer reflejo de un comprador debería ser comprobar las ofertas en venta que ya están financiadas con bitcoin.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- En la pantalla de inicio, pulse el botón "Comprar" (imagen 16)
- A continuación, puede consultar una lista de bitcoins que se han colocado en el sistema de custodia y están listos para la venta (imagen 17). Puede ver el importe, el precio (en % con respecto al mercado KYC), los métodos de pago y las divisas aceptadas.
- Utilice filtros para clasificar y ordenar las ofertas (imagen 18).
- Nota: el botón situado en la parte inferior de la página de filtros le permite recibir una notificación cuando se publique una oferta que coincida con sus filtros; y el botón "reiniciar", que simplemente borra todos los filtros (imagen 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Ver la oferta que le conviene y enviar una solicitud de intercambio (imagen 19)
- Puede realizar varias solicitudes de intercambio, y la primera oferta positiva anulará las demás solicitudes.
- Realice el pago mediante el método acordado.


**Recordatorio:** la fuente de fondos debe coincidir con la que especificó al añadir el método de pago.




- Confirme su pago en la aplicación en cuanto esté hecho**.
- Esperar a que el vendedor reciba el pago y declararlo como tal (imagen 20)
- Y por último, evalúa tu experiencia con el vendedor (imagen 21)



![Réception des bitcoins](assets/fr/09.webp)





- Seguimiento del estado de su transacción
- Comprobar confirmación de recepción de bitcoins
- Los fondos estarán disponibles en su cartera Peach (imagen 22 y 23)



### 1.b Cómo comprar bitcoins: Crear una oferta



Si no encuentras una oferta de venta adecuada, puedes crear una oferta de compra. Dado que esto no compromete ningún bitcoin en esta fase, tendrás menos posibilidades de encontrar un socio de intercambio, especialmente si tu historial y reputación son pobres o inexistentes. Para remediar esto, es importante, al crear la oferta, *hacer una oferta de alta prima* para motivar a los vendedores a seleccionar tu oferta. Procedamos:



![Creation d'ordre d'achat](assets/fr/10.webp)





- En la pantalla de inicio, haga clic en el botón "Crear una oferta de compra" (imagen 24)
- Añada un método de pago, si aún no lo ha hecho, e introduzca sus preferencias (cantidad, prima, etc.) (imagen 25).


La opción "instantánea" le permite aceptar una solicitud de intercambio automáticamente.




 - Haga clic de nuevo en "crear una oferta" para continuar
- Una vez creada, es el turno de los vendedores de acudir a ti con una solicitud de intercambio. Puedes cerrar y salir de la app sin preocupaciones.
- Puede cambiar la prima si no recibe ninguna solicitud. Recuerda: una prima más alta motivará a los vendedores a venir a buscar tu oferta (imagen 26).
- Encontrará su oferta en la pestaña "Comprar", que a su vez está en la ventana "Exchange" (fig. 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Cuando reciba una solicitud de compra (fig. 28) (y si no ha desactivado el comercio instantáneo en la fig. 25), acepte la operación tras comprobar la reputación del vendedor. Si el comercio instantáneo está activado, salta directamente a la imagen 29.
- A continuación, el vendedor debe depositar el bitcoin en el sistema de custodia, ("financiar la caja fuerte"). (imagen 29)
- A continuación, pague al vendedor en el destino indicado en la Fig. 30, a través de su sistema bancario personal. ¡No arrastre el cursor "He efectuado el pago" hasta que lo haya hecho!
- Puede comunicarse con el vendedor a través del sistema de mensajería (cifrado P2P). En caso de problema, puede abrir una disputa haciendo clic en el icono de la esquina superior derecha (imagen 31). Un mediador Peach entrará entonces en la discusión.



![Offre de vente completée](assets/fr/12.webp)





- Una vez que el vendedor haya recibido el dinero, informará de ello y el sistema de custodia liberará el bitcoin, que estará de camino a su wallet (por defecto a través de GroupHug, el sistema de agrupación de transacciones de Peach, que se ejecuta una vez al día),
- Valore su experiencia con el vendedor



¡Eso es!



**Nota para nuevos compradores:** los vendedores basan sus intercambios en la reputación de los compradores, y tienden a evitar las ofertas de compradores sin intercambios completados. Es más fácil, en un primer momento, labrarse una reputación aceptando ofertas de venta existentes.




### 2.a Cómo vender bitcoins: Crear una venta



La forma más rápida y sencilla de vender en Peach es **crear una oferta de venta**.



![Création d'un ordre de vente](assets/fr/13.webp)





- En la página de inicio, haga clic en "Crear una oferta de venta" (imagen 32)
- Configure su oferta, asegúrese de insertar un método de pago y los parámetros correctos


también puedes :




  - crear varias ofertas idénticas
  - activar el "intercambio instantáneo" para que el primer comprador que se presente pueda aceptar el contrato (sin tu confirmación) y proceder al pago.
  - elija una dirección de reembolso
  - financiar el tronco de su wallet Peach
- Financiar la transacción enviando los bitcoins a la dirección facilitada (imagen 34)
- Espere la confirmación de la transacción. Una vez hecho esto, su oferta será visible en el mercado.



![Attente du paiement](assets/fr/14.webp)





- Espere a que un comprador acepte su oferta. Considera la posibilidad de aumentar la prima (%) si quieres acelerar las cosas (imagen 36)
- Cuando recibas una solicitud de intercambio, comprueba la reputación del comprador. Juzga por ti mismo si el perfil es adecuado para ti, y haz clic en "aceptar" si lo es. (37)
- Ahora le toca al comprador hacer el pago desde su banco al tuyo. A continuación, él te remitirá el pago a ti. No dudes en ponerte en contacto con el comprador en el chat.
- tras comprobar que los fondos han sido recibidos por su banco*, libere los fondos pulsando el botón "he recibido el pago" (imagen 38). No confirme nunca la recepción de un pago antes de comprobar que se ha recibido en su cuenta.
- Evaluar la transacción
- Los Bitcoin se entregan automáticamente al comprador,



¡Ya está!



**Nota de seguridad y consejos para una transacción satisfactoria:**




 - Observa los datos del comprador, y comprueba que el origen de los fondos coincide con el descrito en Peach Si el origen de los fondos no coincide con el anunciado, ve al Chat y abre una discusión (imagen 39), y devuelve los fondos a su origen.
 - Sigue las instrucciones del gato amarillo.
 - Responda rápidamente a los mensajes de su contraparte
 - desconfiar de la actitud del comprador, sobre todo si se trata de un perfil con poca experiencia
 - No dude en recurrir al servicio de mediación si tiene un problema



### 2.b Cómo vender bitcoins: haz una oferta



También es posible ver y seleccionar ofertas de compra. Deberá tener especial cuidado, ya que es aquí donde se encuentran la mayoría de los estafadores.



![Prendre une offre d'achat](assets/fr/15.webp)





- En la página de inicio, haga clic en "Ventas" (imagen 40)
- Utilice los filtros para ver y seleccionar las ofertas más atractivas (imagen 41)



![vérification de la réputation](assets/fr/16.webp)





- antes de solicitar un intercambio, le recomendamos que evalúe la idoneidad del perfil del comprador. Puede hacer clic en una oferta y, a continuación, en el identificador del usuario para ver su perfil. Por ejemplo, la oferta de la imagen 42 podría considerarse "arriesgada" (usuario nuevo, importe relativamente elevado). El "riesgo" que corres al aceptar esta oferta es simplemente el de perder el tiempo, siempre y cuando no cometas el error de liberar los bitcoins sin haber recibido el dinero. Puedes seguir depositando los bitcoins en la caja fuerte.


La de la imagen 43, en cambio, procede de un operador con experiencia (imagen 44), sin disputas en su historial. Por tanto, es una oferta menos arriesgada.



![Match avec vendeur](assets/fr/17.webp)





- Una vez solicitada la oferta, si el comprador acepta su solicitud, la aplicación le llevará a la imagen 34, donde podrá continuar la operación como se describe a continuación.




## Ventajas e inconvenientes



### Ventajas de Peach





- No se requiere KYC**: Preserva la confidencialidad del usuario.
- Sin acceso a datos bancarios**: Peach no tiene acceso a tus datos bancarios ni a tu identidad.
- Interface intuitivo**: Fácil de usar para usuarios intermedios.
- Código abierto** : El código fuente es público y verificable por la comunidad.



### Desventajas de Peach





- Liquidity** limitada: Menor volumen de negociación que plataformas más consolidadas.
- Riesgo reglamentario** : La aplicación está gestionada por una empresa suiza. Por tanto, está sujeta a la normativa suiza, que podría evolucionar y potencialmente censurar la aplicación.



## Recursos útiles





- Vídeo explicativo en francés: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Guía de inicio rápido: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (cuidado con los estafadores, los administradores nunca te escribirán primero por mensaje privado)
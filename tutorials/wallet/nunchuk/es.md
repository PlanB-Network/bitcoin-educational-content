---
name: Nunchuk
description: Wallet móvil apto para todos
---
![cover](assets/cover.webp)



## Una potente Wallet


Nunchuk llegó a finales de 2020 con una filosofía clara: hacer de la multifirma un estándar. Por ello, se diseñó para realizar funciones muy avanzadas, con la valiosa opción de construir el diseño directamente sobre Bitcoin Core, el software de referencia para el ecosistema Bitcoin.



Tras más de 4 años de desarrollo y uso, está listo para ser probado a gran escala. Si eres principiante y no estás familiarizado con el Nunchuk, esta guía te ayudará a dar tus primeros pasos y a descubrir este software, cuyas funciones avanzadas podrás conocer una vez superado el primer impacto. El tutorial en sí está dedicado a usuarios intermedios que posean los conocimientos necesarios para seguir todos los pasos, pero puede servir de inspiración para que todo el mundo descubra cómo aumentar sus habilidades. Empezaremos con la versión para móviles, y esta puntualización es necesaria, ya que Nunchuk dispone del software para funcionar también en ordenadores.



## Descargar


El primer paso es, sin duda, decidir dónde descargar la aplicación. Dirígete al [sitio oficial](https://nunchuk.io/), donde encontrarás algo de documentación (no es mucho, pero es un comienzo), la presentación de las características y, hacia el final de la página, todos los enlaces de descarga.



📌 Para este tutorial decidí mostrarte cómo descargar Software Wallet desde el repositorio de Github y cómo verificar la versión antes de instalarla en tu celular. **El siguiente procedimiento sólo se puede hacer desde tu ordenador**, por lo que te recomiendo hacer todos estos pasos desde tu ordenador de sobremesa o portátil y -después de todas las verificaciones- transferir el archivo `.apk` a tu móvil.



![image](assets/en/01.webp)



Si tus conocimientos no son muy avanzados, puedes decidir descargar el `.apk` de las tiendas oficiales y saltar directamente a la parte de configuración de este tutorial. Si, por el contrario, quieres dar el salto, sigue paso a paso.



Así que desde tu ordenador de sobremesa haz clic en _Visita nuestro repositorio de código abierto_



El enlace te llevará a la página de Github de Nunchuk, donde encontrarás varios repos. Nos centraremos en el de _nunchuk-android_



![image](assets/en/02.webp)



En la siguiente pantalla, localice a la derecha la sección de _Releases_ y elija _Latest_



![image](assets/en/03.webp)



En _Assets_, descarga la versión (en este ejemplo 1.67.apk), junto con el archivo SHA256SUMS y SHA256SUMS.asc.



![image](assets/en/04.webp)



Para encontrar la clave GPG del desarrollador, vuelva a la sección _Releases_ del repositorio y busque la versión 1.9.53 (o anterior) que contiene el enlace para obtener y descargar la _Clave GPG_



![image](assets/en/05.webp)



Procederemos a la verificación mediante una práctica herramienta ofrecida por Sparrow wallet, que dispone de una ventana dedicada a este fin y admite firmas PGP y manifiestos SHA256.



A continuación, inicie Sparrow y, en el menú _Herramientas_, elija _Verificar descarga_.



![image](assets/en/06.webp)



En la ventana que aparece, encontrarás campos para "rellenar": elige el botón _Browse_ de la derecha y selecciona, para cada campo, los archivos correspondientes que acabas de descargar de Github. Cuando hayas completado todos los pasos, la ventana tendrá el siguiente aspecto, con las marcas Green y Hash de confirmación del manifiesto.



![image](assets/en/07.webp)


**N.B. la captura de pantalla es de un PC con Windows, la misma práctica se puede utilizar para cualquier sistema operativo en su ordenador, sólo tiene que tener Sparrow wallet instalado. Y verificado!**



Puede encontrar la guía de Sparrow wallet para descargar este Software Wallet


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

A continuación, puedes transferir el archivo `.apk` de tu ordenador a tu teléfono



![image](assets/en/08.webp)



e instala el Nunchuk



![image](assets/en/09.webp)



Antes de lanzar el Nunchuk en tu teléfono, abre Orbot y pon al recién llegado en la lista de aplicaciones que se enrutarán bajo Tor.



![image](assets/en/11.webp)



Ahora ejecuta Nunchuk. Para las características del proyecto-que no son el tema de este tutorial-Nunchuk, una vez abierto, le invitará a iniciar sesión a través de un correo electrónico o perfil de Google. Hasta que planee aprovechar los planes avanzados de Nunchuk Inc, **evite iniciar sesión** y proceda eligiendo la opción _Continuar como invitado_.



![image](assets/en/12.webp)



## Ajustes


Nunchuk se presenta con una ventana de presentación _Home_, en la que es fácil entender su filosofía de funcionamiento y sobre la que profundizaremos en un momento.



En la parte inferior encontrarás los menús, y como primer paso, elige _Perfil_ para acceder a la configuración.



![image](assets/en/10.webp)



A continuación, elija _Configuración de la pantalla_, y siga ignorando la invitación a crear una cuenta.



![image](assets/en/14.webp)



En la siguiente pantalla puede comprobar si Wallet está en línea y puede conectar su servidor, prestando mucha atención a las instrucciones del enlace que se ofrece pulsando sobre _esta guía_.



![image](assets/en/15.webp)



Guarde la configuración con el comando _Guardar configuración de red_, vuelva al menú _Perfil_ y seleccione _Configuración de seguridad_.



![image](assets/en/16.webp)



Desde este menú configuras cómo defender la apertura de la app. Para evitar accesos no deseados puedes proteger Nunchuk con el biométrico del teléfono, y/o añadir un PIN de seguridad.



![image](assets/en/17.webp)



Eche un vistazo también al menú _Acerca de_, que encontrará siempre en la ventana _Perfil_



![image](assets/en/18.webp)



que te permitirá comprobar la versión de la aplicación, o ponerte en contacto con los desarrolladores si es necesario.



![image](assets/en/19.webp)



## Generación de claves y Wallet


Como es fácil adivinar por la filosofía de Nunchuk, el software pretende ser una herramienta útil para la gestión de Carteras multifirma. Para realizar esta función, Nunchuk permite la creación de Wallet separándolos de las claves necesarias para organizar las firmas digitales.



De hecho, el funcionamiento ideal de Nunchuk implica la creación de Carteras que pueden ser sólo reloj, dependientes de teclas que pueden ser "Frías"



En las pantallas anteriores habrás notado que hay un menú en la parte inferior llamado _Keys_. Si acabas de descargar Nunchuk, tanto en _Home_ como en _Keys_ verás un gran botón que te invita a añadir una tecla, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**Así es como funciona el Nunchuk:** primero generate/importas las claves y luego creas el Wallet, configurándolo para elegir qué claves autorizarán el desbloqueo de los fondos almacenados en él.



Incluso en el caso de Wallet singlesig, se crea la clave en primer lugar y sólo entonces el Wallet. Y eso es exactamente lo que haremos ahora, comenzando con un singlesig Wallet para romper el hielo y descubrir las funciones de Nunchuk.



Haga clic en _Añadir clave_



![image](assets/en/22.webp)



Nunchuk muestra una serie de dispositivos de firma compatibles pero, para empezar, elige _Software_.



![image](assets/en/23.webp)



Nunchuk generate un Mnemonic que se almacenará en el dispositivo. A continuación, tienes que escribir la secuencia de palabras para la copia de seguridad, creando las mejores condiciones ambientales y asegurándote de que tienes tiempo para hacerlo bien y en silencio. El software muestra la Mnemonic sólo una vez, tanto si eliges mostrarla ahora como más tarde, así que elige _Crear y hacer copia de seguridad ahora_.



![image](assets/en/24.webp)



El Nunchuk genera frases Mnemonic de 24 palabras, que aparecen inmediatamente en la siguiente pantalla



![image](assets/en/25.webp)



y luego procedió a hacer una comprobación rápida, pidiéndole que seleccionara la palabra correcta, de entre 3 opciones, correspondiente al número de la secuencia Mnemonic.


Si ha escrito correctamente la Mnemonic, el botón _Continuar_ pasa a estar operativo. Púlselo para continuar.



![image](assets/en/26.webp)



Dale un nombre a tu tecla y pulsa _Continuar_.



![image](assets/en/27.webp)



Al final de estos pasos, se le preguntará si desea añadir una [passphrase](https://planb.academy/en/resources/glossary/passphrase-bip39) a su frase Mnemonic. Si no tienes los conocimientos necesarios sobre cómo utilizar passphrase, organizar su copia de seguridad o cómo funciona, te recomiendo que elijas _No necesito una frase_.



![image](assets/en/28.webp)



La clave se crea finalmente y se le muestra en el menú:




- Con _Key Spec_ se indica la huella maestra
- Tienes los ajustes, los tres puntos arriba a la derecha, donde puedes borrar la clave o firmar un mensaje
- Junto al nombre de la llave encontrará un icono de plumilla, pulsando el cual podrá editar el nombre de la llave, por ejemplo para mantener sus llaves en orden en el futuro.
- Como último comando, puedes comprobar el estado de salud de la llave: pulsando _Run health check_ puedes hacer que la app compruebe si una llave está comprometida.



Cuando esté bien, pulse _Done_



![image](assets/en/29.webp)



En el menú _Teclas_ verás aparecer tu primera tecla.



![image](assets/en/30.webp)



Yendo al menú _Home_, aparece la opción de crear Wallet. Haz clic en _Crear nuevo monedero_.



![image](assets/en/31.webp)



Nunchuk te muestra una serie de posibilidades que tienen que ver, en su mayoría, con servicios que ofrece la compañía y que no son objeto de este tutorial.



En esta guía crearemos un _Hot Wallet y un _Custom wallet_ detallando los pormenores.


Empecemos por _Cartera personalizada_.



![image](assets/en/32.webp)



De forma sencilla, la aplicación te pedirá que nombres este nuevo Wallet y que elijas el script para las direcciones. Para el tutorial elegí dejar la configuración por defecto, _Native segwit_. Cuando haya terminado, elija _Continue_



![image](assets/en/33.webp)



La configuración de la Wallet pasa a pedirle que establezca con qué llave se desbloquearán los fondos de esta Wallet. En caso de que existan varias claves, se le mostrará una lista entre las que podrá elegir. Nosotros de momento sólo hemos creado una, así que optamos por marcarla. En la esquina inferior derecha puedes ver como Nunchuk te pedirá que configures tus futuras Wallet multifirmas, aumentando el número de _Llaves requeridas_.



![image](assets/en/34.webp)



Como estamos creando un singlesig, dejamos `1` y pulsamos _Continuar_.



Por último, aparece una pantalla de verificación en la que puede comprobar las características del Wallet:




- el nombre
- el `1/1 Multisig` tage, que es como Nunchuk nombra el Wallet singlesig
- el tipo de script, `Native SegWit`
- la clave `Keys`, con su huella digital y su ruta de derivación



Cuando esté satisfecho, pulse _Crear cartera_



![image](assets/en/35.webp)



Wallet ha sido creado y puede descargar el archivo [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) como copia de seguridad. Para volver al menú principal, haga clic en la flecha de la esquina superior izquierda.



![image](assets/en/36.webp)



Se encuentra en _Home_, donde se le muestra la Wallet recién creada informando del saldo y estado de la conexión. Pulsando en el espacio azul, puede acceder a las principales funciones de Wallet.



![image](assets/en/37.webp)





- El icono de la lente en la esquina superior derecha le permite realizar una búsqueda de transacciones;
- `View Wallet config` da acceso al menú de configuración, donde se puede editar el nombre de la Wallet y activar las opciones avanzadas, arriba a la derecha (de las que no se pueden obtener capturas de pantalla). Aquí puedes exportar la configuración de la Wallet, etiquetas, reemplazar teclas, cambiar el [gap limit](https://planb.academy/en/resources/glossary/gap-limit) y más.



## Operaciones con el Nunchuk



Premios _Recibir



![image](assets/en/38.webp)



La aplicación está programada para mostrar el código QR del Address o copiar/compartir el scriptPubKey para recibir fondos onchain.



![image](assets/en/39.webp)



En este primer Address llegó un UTXO,



![image](assets/en/40.webp)



pero seguimos haciendo clic en _Recibir_ para recibir otro.



![image](assets/en/41.webp)



El propósito es que descubras que Nunchuk te reporta este nuevo Address como una _Dirección no utilizada_ pero también te muestra que tienes _Direcciones utilizadas_ y el conteo de las mismas.



### Transacción de gasto con control de monedas



Cuando esta segunda UTXO también haya llegado, vuelva a la pantalla principal de la Wallet para comprobar el estado de las dos transacciones entrantes y, sobre todo, haga clic en la opción _Ver monedas_



![image](assets/en/42.webp)



donde se le mostrarán los UTXO individuales. Aquí puede elegir ver uno en particular haciendo clic en la pequeña flecha situada junto al importe



![image](assets/en/43.webp)



y comprobar cuando llegó, la descripción, bloque UTXO para que no se gasta y más.



![image](assets/en/44.webp)



Pero si vuelves al menú _Coins_ haciendo clic en la flecha de la esquina superior derecha, puedes activar el "Control de monedas" para gastar tus UTXOs de forma más controlada.



En el siguiente ejemplo, he elegido seleccionar UTXO de 21.000 Sats y, a continuación, hacer clic en el símbolo de la esquina inferior izquierda.



![image](assets/en/45.webp)



Nunchuk abre automáticamente la ventana _Nueva transacción_ para gastar este UTXO. En la transacción de gasto, en primer lugar, debe establecer la cantidad manualmente o seleccionando _Enviar todo seleccionado_ para enviar todo el saldo de control de monedas, sin generar remanentes. Una vez fijado el importe, seleccione _Continuar_



![image](assets/en/46.webp)



Ahora Nunchuk muestra dónde pegar el Address al que transferir estos fondos, detallar una descripción y finalizar la transacción.



![image](assets/en/47.webp)



Elegir _Crear transacción_ delega en la aplicación la gestión automática de comisiones y transacciones. Recomiendo elegir _Transacción personalizada_ para tener más control.



En esta nueva pantalla es importante seleccionar




- _Restar tasa del importe de envío_, para evitar que las tasas sean pagadas por otro UTXO presente en Wallet, gastándolo y generando un remanente (lo que supone una pérdida de privacidad evitable);
- y luego establecer las tasas manualmente después de comprobar en el explorador.



Una vez realizados todos estos pasos, haga clic en _Continuar_



![image](assets/en/48.webp)



La siguiente pantalla es el resumen completo de la transacción. Si todo está bien, confirme seleccionando _Confirmar y crear transacción_.



![image](assets/en/49.webp)



Con _Firmas pendientes_ Nunchuk te avisa de que la transacciónp está esperando tu firma para aprobar el gasto, que estampas haciendo clic en _Firmar_.



![image](assets/en/50.webp)



El comando _Broadcast_ aparece en la parte inferior para propagar la transacción finalizada y firmada.



![image](assets/en/51.webp)



### Transacción de gastos desde el menú _Enviar_



Mientras que en la página principal de Wallet vemos la transacción saliendo y esperando confirmación, utilizamos el menú _Enviar_ para simular un gasto diario.



![image](assets/en/52.webp)



De hecho, al hacer clic en _Enviar_, aparece la pantalla de envío de la transacción, que es la misma que la que acabamos de ver pero sin pasar por el control de monedas.



También en este segundo ejemplo decidí seleccionar _Transacción personalizada_ y enviar el importe completo, pero podría haberlo establecido manualmente. Una vez decidido el importe a enviar pulse _Continuar_.



![image](assets/en/53.webp)



A continuación, decida siempre si las tasas se restan de la UTXO en cuestión (en este ejemplo la elección es forzosa, porque sólo hay una), ajuste manualmente las tasas según la situación del momento en la Mempool, y pulse _Continuar_.



![image](assets/en/54.webp)



Si la pantalla de resumen es satisfactoria, seleccione _Confirmar y crear transacción_.



![image](assets/en/55.webp)



Firme la transacción con _Sign_



![image](assets/en/56.webp)



y propagarlo a la red.



![image](assets/en/57.webp)



Wallet se encuentra en este punto con el saldo a cero y el historial actualizado.



![image](assets/en/58.webp)



## Creación de un "Hot Wallet"



Por último, y para no dejar de lado nada de las fases iniciales del Nunchuk móvil, veamos cómo se crea lo que la aplicación llama "Hot Wallet"



En el menú _Home_ del Nunchuk, donde aparece la lista de Carteras, haz clic en el signo `+` de la esquina superior derecha.



![image](assets/en/59.webp)



Elija _Monedero caliente_ entre las opciones



![image](assets/en/60.webp)



Nunchuk da algunos consejos sobre el manejo de las Carteras Hot en la página de presentación, donde seleccionarás _Continuar_ para continuar.



![image](assets/en/61.webp)



Después de unos momentos la Wallet es creada y aparece en la lista en color café. Este es el color con el que el Nunchuk te avisa de que aún no has realizado la copia de seguridad de la Wallet.



![image](assets/en/62.webp)



Haga clic en el nombre de la Wallet para acceder a sus configuraciones.



![image](assets/en/63.webp)



El procedimiento es el mismo que hemos visto antes, así que no nos pararemos sobre él otra vez. Una vez hecho esto, Nunchuk le llevará a la página de la clave correspondiente, que se puede editar como el que ha creado con el procedimiento _Custom_.



![image](assets/en/64.webp)



Prueba también a _Ejecutar chequeo_



![image](assets/en/65.webp)



o para ver cómo mostrar todas tus Carteras en el _Home_ de la aplicación.



![image](assets/en/66.webp)



## A tener en cuenta para continuar de forma independiente


Al igual que existe un orden para la creación, es decir, primero generar las claves y luego la Wallet, deberás mantener el orden inverso para eliminar estos elementos de tu aplicación.



Si necesitas eliminar una de las claves, primero debes tener la precaución de eliminar Wallet, o Wallets, que emplean una de las claves de firma para las transacciones: primero eliminas Wallets y sólo después las claves. Si no sigues este orden, te encontrarás con que no puedes eliminar la clave.



Ahora que ya sabes cómo empezar a utilizar el Nunchuk, puedes seguir estudiando esta aplicación y descubrir sus secretos. En este tutorial sólo hemos dado los primeros pasos, pero hay aplicaciones más sofisticadas y necesidades avanzadas que este Software Wallet puede ayudarte a satisfacer.
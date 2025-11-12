---
name: Ashigaru
description: La fork de Samourai Wallet para asegurar, gestionar y mezclar sus bitcoins
---

![cover](assets/cover.webp)



Ashigaru es una aplicación para móviles Bitcoin wallet que da continuidad al proyecto Samourai Wallet, pero bajo una nueva forma. Este software nació en un contexto particular: en abril de 2024, los fundadores de Samourai Wallet fueron detenidos por las autoridades estadounidenses, y sus servidores fueron incautados. Aunque la aplicación Samurai en sí siguió siendo utilizable, actualmente ya no se mantiene. Ashigaru es una versión libre fork de Samurai Wallet, mantenida por un equipo anónimo para garantizar la continuidad de la funcionalidad de Samurai y salvaguardar su filosofía original: defender la privacidad y la soberanía de los usuarios de Bitcoin.



Ashigaru retoma gran parte del ADN de Samourai: una interfaz similar, un enfoque obviamente autocustodiado, código abierto y un enfoque centrado en la privacidad. El código se distribuye bajo la licencia GNU GPLv3, que garantiza que cualquiera pueda auditar, modificar o redistribuir el software.



La aplicación Ashigaru integra un conjunto de herramientas avanzadas para la confidencialidad y la gestión de sus UTXOs:




- Whirlpool**, un protocolo de coinjoin basado en Zerolink, que le permite romper los vínculos deterministas entre entradas y salidas de transacciones, sin perder la soberanía sobre sus fondos.
- PayNym**, que implementa códigos de pago reutilizables (BIP47), ahora representados mediante un sistema de avatar "*Pepehash*".
- Ricochet**, una función que añade saltos intermedios a las transacciones para dificultar su rastreo.
- Y, por supuesto, ***Coin Control*** para seleccionar, congelar y etiquetar sus UTXO con precisión.
- Gastos por lotes***, para reducir costes agrupando varios pagos en una sola transacción.
- El **Modo Sigilo**, que oculta la aplicación en tu móvil tras un lanzador ficticio para pasar desapercibida durante una inspección física de tu teléfono.
- Herramientas avanzadas de gasto para optimizar su confidencialidad (payjoin, stonewall...).
- Un sistema de recuperación optimizado utilizando la frase de contraseña BIP39.
- Un sistema para optimizar automáticamente la elección de las tarifas de transacción.



![Image](assets/fr/01.webp)



Por lo tanto, Ashigaru está dirigida a usuarios conscientes de los problemas que rodean a la trazabilidad de las transacciones en Bitcoin. Tanto si eres un usuario preocupado por su privacidad, un bitcoiner experimentado comprometido con la autocustodia o un individuo expuesto a los riesgos de una mayor vigilancia, esta aplicación para wallet te proporciona las herramientas que necesitas para recuperar el control de tu actividad en Bitcoin.



Ashigaru está disponible en versión móvil a través de su aplicación, que exploraremos en este tutorial. Pero también se puede utilizar en el PC con ***Ashigaru Terminal***, que presentaremos en un futuro tutorial.



![Image](assets/fr/02.webp)



En este tutorial, me gustaría presentarte el uso básico de Ashigaru: instalación, conexión al Dojo, copias de seguridad, recepción y envío de bitcoins. Las herramientas avanzadas serán presentadas en otros tutoriales dedicados.



## 1. Requisitos previos para Ashigaru



La aplicación requiere algunos requisitos previos para funcionar correctamente. En primer lugar, no es una aplicación disponible en tiendas clásicas como Google Play Store o App Store. Se instala manualmente en tu teléfono sólo desde su archivo `.apk`, descargable a través de la red Tor. Así que si usas un iPhone, este método no funcionará: necesitarás un dispositivo Android.



Para descargar el archivo `.apk` a través de Tor, necesitarás un navegador capaz de acceder a sitios `.onion`. La forma más fácil es instalar la aplicación Tor Browser en tu teléfono, disponible en [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) o directamente [a través de su `.apk`](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



La mayoría de los smartphones recientes bloquean la instalación de aplicaciones de fuentes desconocidas por defecto. Tendrás que activar temporalmente esta opción para el Navegador Tor en la configuración de tu dispositivo para permitir la instalación. Una vez instalada la aplicación, recuerda desactivar esta función para reforzar la seguridad de tu teléfono.



Otro prerrequisito esencial para usar Ashigaru es un nodo Dojo Bitcoin. Por razones de seguridad y soberanía, el equipo de Ashigaru no mantiene un servidor centralizado para conectar tu aplicación. Así que necesitarás ejecutar tu propia instancia de Dojo, o conectarte a una de confianza.



El Dojo permite a su aplicación Ashigaru consultar la información del blockchain, ver los saldos de sus direcciones y difundir sus transacciones en la red Bitcoin.



Para saber más sobre Dojo y aprender a instalarlo, te invito a seguir este tutorial dedicado :



https://planb.network/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Si realmente no puedes permitirte tener tu propio Dojo, puedes encontrar gente dispuesta a compartir su instancia de forma gratuita en [dojobay.pw](https://www.dojobay.pw/mainnet/). Esta puede ser una solución temporal, pero a largo plazo, te recomiendo que utilices tu propio Dojo para garantizar tu soberanía y confidencialidad.



## 2. Compruebe e instale la aplicación Ashigaru



### 2.1. Descargar la aplicación Ashigaru



En su teléfono, abra el Navegador Tor y vaya a [la web oficial de Ashigaru](https://ashigaru.rs/download/), en la sección `Download`. A continuación, haga clic en el botón `Download for Android` para descargar el archivo de instalación.



![Image](assets/fr/04.webp)



Antes de instalar la aplicación en tu dispositivo, comprobaremos su autenticidad e integridad. Este es un paso muy importante, especialmente cuando se instala una aplicación directamente desde un archivo `.apk'.



### 2.2. Compruebe la aplicación Ashigaru



Vuelve a [la página oficial de Ashigaru](https://ashigaru.rs/download/) en la sección `Download`, luego copia el mensaje que aparece bajo el título `SHA-256 Hash del archivo APK`. Copie todo el bloque, desde `BEGIN PGP SIGNED MESSAGE` hasta `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Todavía en su teléfono, abra una nueva pestaña en el Navegador Tor y vaya a [la herramienta de verificación Keybase](https://keybase.io/verify). Pega el mensaje que acabas de copiar en el campo proporcionado, luego haz clic en el botón `Verify`.



![Image](assets/fr/06.webp)



Si la firma es auténtica, Keybase mostrará un mensaje confirmando que el archivo ha sido firmado por los desarrolladores de Ashigaru. También puede hacer clic en el perfil `ashigarudev` indicado por Keybase y comprobar que su huella digital de clave se corresponde exactamente con : `A138 06B1 FA2A 676B`.



Sin embargo, si aparece un error en esta fase, significa que la firma no es válida. En este caso, **no instales el APK**. Vuelve a empezar desde el principio o pide ayuda a la comunidad antes de continuar.



![Image](assets/fr/07.webp)



Keybase te ha proporcionado el hash de la aplicación. Ahora comprobaremos que el hash del archivo `.apk` que has descargado coincide con el verificado en Keybase. Para ello, ve a [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Haga clic en el botón `BROWSE...` y seleccione el archivo `.apk` descargado en el paso 2.1.


A continuación, elija la función hash `SHA-256` y haga clic en `CALCULAR HASH` para calcular el hash de su archivo.



![Image](assets/fr/09.webp)



El sitio mostrará el hash de tu archivo `.apk`. Compárelo con el hash que verificó en Keybase.io. Si los dos hashes son idénticos, la comprobación de autenticidad e integridad se ha realizado correctamente. Ahora puede proceder a instalar la aplicación.



![Image](assets/fr/10.webp)



### 2.3. instalar la aplicación Ashigaru



Para instalar la aplicación, abre el gestor de archivos de tu teléfono y ve a la carpeta de descargas. A continuación, haz clic en el archivo `.apk` que acabas de consultar y confirma la instalación cuando se te solicite.



![Image](assets/fr/11.webp)



Ashigaru ya está instalado en tu teléfono.



## 3. Inicializar la aplicación y crear una cartera Bitcoin



Al iniciar la aplicación por primera vez, seleccione `MAINNET`.



![Image](assets/fr/12.webp)



A continuación, haga clic en "Empezar".



![Image](assets/fr/13.webp)



Ahora vamos a crear una nueva cartera Bitcoin. Pulse el botón `Crear una nueva wallet`.



![Image](assets/fr/14.webp)



### 3.1. crear una cartera Bitcoin



Ashigaru requiere un passphrase BIP39. Elige tu passphrase e introdúcelo en los campos correspondientes. Debe ser lo más largo y aleatorio posible para resistir un ataque de fuerza bruta.



Haga una copia de seguridad física de este passphrase inmediatamente. Este es un paso muy importante: si pierde su teléfono, **si ya no tiene esta passphrase, ya no podrá acceder a sus bitcoins** almacenados con su Ashigaru wallet. Esta misma passphrase se utiliza también para encriptar el archivo de recuperación de la wallet.



Si no sabes lo que es una passphrase o no entiendes bien cómo funciona, te recomiendo encarecidamente que leas este tutorial adicional. Esto es importante, porque la passphrase es un elemento crítico de su seguridad: malinterpretar su uso podría resultar en la pérdida permanente de sus fondos.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Una vez que haya introducido su passphrase, haga clic en `NEXT`.



![Image](assets/fr/15.webp)



A continuación, elija un código PIN. Este código se utilizará para desbloquear su Ashigaru wallet, protegiéndolo contra el acceso físico no autorizado. No interviene en la derivación criptográfica de las claves de su wallet. Esto significa que, incluso sin conocer el código PIN, cualquiera con su frase mnemotécnica y su passphrase podrá recuperar el acceso a sus bitcoins.



Opta por un código PIN largo y aleatorio. Recuerda guardar una copia de seguridad en un lugar distinto al de tu teléfono, para evitar que se pongan en peligro simultáneamente.



![Image](assets/fr/16.webp)



Una vez creado el código PIN, Ashigaru muestra la frase mnemotécnica de su wallet. Advertencia: esta frase, combinada con tu passphrase, da acceso completo a tus bitcoins. Cualquiera que la tenga puede tomar posesión de tus fondos, incluso si no tiene acceso a tu teléfono. Esta secuencia de 12 palabras puede utilizarse para restaurar tu wallet en caso de pérdida, robo o rotura de tu teléfono. Por lo tanto, es importante guardarla con el máximo cuidado en un soporte físico (papel o metal).



Nunca guardes esta frase en formato digital, o corres el riesgo de exponer tus fondos a robos. Dependiendo de tu estrategia de seguridad, puedes crear varias copias físicas, pero nunca dividirla. Conserva las palabras en su orden exacto y asegúrate de que están numeradas.



Por último, nunca almacene la mnemónica y la passphrase en el mismo lugar. Si ambos estuvieran comprometidos simultáneamente, un atacante podría acceder a tu wallet.



![Image](assets/fr/17.webp)



Para saber más sobre cómo asegurar su frase mnemotécnica, consulte este tutorial complementario :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru le pedirá que reconfirme su passphrase. Aprovecha esta oportunidad para comprobar que tu copia de seguridad física es correcta.



![Image](assets/fr/18.webp)



### 3.2. conectar un dojo



A continuación viene el paso de conectarse a su Dojo. Como se explicó en la introducción, Ashigaru debe estar conectado a un Dojo para poder interactuar con la red Bitcoin.



Accede a la "Herramienta de mantenimiento" de tu Dojo y abre el menú `PAIRING`.



![Image](assets/fr/19.webp)



En Ashigaru, pulse el botón "Escanear QR" y escanee el código QR de conexión mostrado por su DMT. A continuación, pulse "Continuar" para confirmar.



![Image](assets/fr/20.webp)



Introduzca su código PIN para desbloquear la wallet. Esto le llevará a la página de sincronización. Es normal que aparezcan errores *PayNym* en esta fase, ya que la wallet es nueva. Simplemente haga clic en "Continuar".



![Image](assets/fr/21.webp)



A continuación, accederá a la página de inicio de su cartera.



![Image](assets/fr/22.webp)



Antes de seguir adelante, te recomiendo que realices una recuperación de prueba mientras el wallet aún no contiene bitcoin. Esto te permitirá comprobar que tus copias de seguridad en papel funcionan correctamente. Para saber cómo, sigue este tutorial:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Configuración de la aplicación Ashigaru



Para acceder a la configuración de la aplicación, haga clic en la imagen de su *PayNym* en la esquina superior izquierda y seleccione `Configuración`.



![Image](assets/fr/23.webp)



Aquí encontrará varias opciones para adaptar el funcionamiento de Ashigaru a sus necesidades. Sin embargo, te recomiendo encarecidamente que actives 2 parámetros importantes desde el principio.



Comience abriendo el menú `Seguridad > Modo oculto` y active esta función si la necesita. Oculta la aplicación Ashigaru tras el nombre, logo e interfaz de una aplicación normal instalada en su teléfono. El objetivo es evitar que alguien identifique Ashigaru en caso de una inspección física de su teléfono.



![Image](assets/fr/24.webp)



Cada aplicación falsa que se ofrece tiene un método específico para desbloquear la interfaz Ashigaru real. Por ejemplo, si eliges la calculadora, la aplicación Ashigaru desaparece de tu pantalla de inicio y es sustituida por una calculadora falsa. Cuando la abres, ves una interfaz de calculadora clásica que funciona, pero para acceder a Ashigaru, todo lo que tienes que hacer es tocar el símbolo `=` cinco veces rápidamente.



El segundo parámetro importante que hay que activar es [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Esta opción permite aumentar el coste de una transacción si se queda atascada en los mempools porque el coste es demasiado bajo. Puede activarla a través del menú `Transacciones > Gastar usando RBF`.



![Image](assets/fr/25.webp)



Consejo: Puede cambiar la unidad de visualización de su cartera de `BTC` a `sat` simplemente haciendo clic en el saldo total que aparece en la página de inicio.



## 5. Recibir bitcoins en Ashigaru



Ahora que su cartera está operativa, puede recibir satss. Para ello, pulse el botón `+` situado en la parte inferior derecha de la interfaz y, a continuación, el botón verde `Recibir`.



![Image](assets/fr/26.webp)



Ashigaru entonces te muestra la primera dirección de recepción no utilizada en tu wallet, para evitar la reutilización de direcciones (la reutilización de direcciones es una muy mala práctica para tu privacidad). Puedes entonces reenviar esta dirección a la persona o servicio que necesite enviarte bitcoins.



![Image](assets/fr/27.webp)



Una vez que la transacción se haya difundido en la red, aparecerá automáticamente en la página de inicio de la aplicación.



![Image](assets/fr/28.webp)



## 6. Envía bitcoins con Ashigaru



Ahora que tienes bitcoins en tu Ashigaru wallet, también puedes enviarlos. Para ello, pulsa el botón `+` de la parte inferior derecha y, a continuación, selecciona el botón rojo `Enviar`.



![Image](assets/fr/29.webp)



A continuación, elija la cuenta desde la que desea realizar el gasto. De momento, aún no hemos abordado la cuenta `Postmix`, reservada a los coinjoins, que veremos en un tutorial posterior. Así que vamos a enviar fondos desde la cuenta de depósito principal.



![Image](assets/fr/30.webp)



Introduzca los datos de la transacción: el importe a enviar y la dirección Bitcoin del destinatario.



![Image](assets/fr/31.webp)



Haciendo clic en los tres puntitos de la esquina superior derecha y luego en `Mostrar salidas no gastadas`, también puedes elegir con precisión qué UTXOs deseas gastar, para aumentar tu privacidad.



![Image](assets/fr/32.webp)



Cuando hayas rellenado todos los datos, haz clic en la flecha blanca de la parte inferior de la interfaz para continuar.



A continuación, accederá a una página de resumen que muestra todos los detalles de su transacción. Se muestran varios elementos importantes:




- En el bloque `Destino`, compruebe por última vez que la dirección del destinatario y el importe enviado son correctos;
- En el bloque `Tarifas`, puede ver la tarifa de tasas seleccionada automáticamente por Ashigaru y, si es necesario, modificarla pulsando en `GESTIÓN` ;
- El bloque `Transaction` indica el tipo de transacción que está a punto de realizar. Aquí, estamos hablando de una transacción simple, pero Ashigaru también soporta otros tipos de transacciones de privacidad optimizada, que cubriremos en detalle en un futuro tutorial;
- El bloque rojo "Alerta de transacción" le avisa si su transacción muestra patrones que puedan ser reconocidos por las herramientas de análisis de la cadena, y que podrían comprometer su privacidad. Pulsando sobre él, puede ver los detalles. Por ejemplo, en mi caso, Ashigaru me indica que la cantidad enviada es redonda (`3000 sats`), lo que me permite deducir qué salida corresponde al gasto y cuál al intercambio. Para saber más sobre esta heurística de análisis de cadenas, te invito a seguir mi formación sobre BTC 204 en Plan ₿ Academy ;
- Por último, puede añadir una etiqueta a su transacción para dejar constancia de su finalidad.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Cuando hayas comprobado toda la información, utiliza la flecha verde para enviar los bitcoins. Mantén pulsada la flecha y arrástrala hacia la derecha para confirmar la subida.



![Image](assets/fr/33.webp)



Su transacción ha sido difundida en la red Bitcoin.



![Image](assets/fr/34.webp)



## 7. Recuperar tu Ashigaru wallet



La recuperación de una Ashigaru wallet difiere ligeramente de la de una Bitcoin wallet clásica, ya que la aplicación utiliza los mismos métodos que la Samurai Wallet. Si pierdes el acceso a tu wallet (ya sea porque has olvidado el PIN, la has desinstalado o has perdido el teléfono), hay varias formas de recuperar tus bitcoins.



Si todavía tiene acceso a su teléfono, o si había hecho una copia de seguridad de este archivo, el método más sencillo es utilizar el archivo de copia de seguridad `ashigaru.txt`. Este archivo contiene toda la información que necesita para restaurar su cartera en una nueva instancia de Ashigaru (o en Sparrow Wallet), pero está encriptado con el passphrase que definió en el paso 3.1 de este tutorial. Por lo tanto, debe tener tanto el archivo `ashigaru.txt` como su passphrase para utilizar este método.



Con estos dos elementos, puede, por ejemplo, restaurar su cartera en Sparrow Wallet.



![Image](assets/fr/35.webp)



Si no tiene acceso al archivo `ashigaru.txt`, aún puede recuperar el acceso a sus fondos utilizando su frase mnemotécnica passphrase, tal como lo haría para cualquier otra cartera Bitcoin. Le recomiendo que realice esta restauración en una nueva instancia de Ashigaru, o directamente en Sparrow Wallet, para recuperar fácilmente las rutas de desvío de Whirlpool si las estaba utilizando. Alternativamente, puede importar esta información en cualquier otro software compatible con BIP39 introduciendo manualmente las rutas de derivación.



Para más información sobre este proceso, consulte el tutorial completo que he escrito sobre la recuperación de un Wallet Samurai wallet. Dado que Ashigaru es un fork, el procedimiento es idéntico:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Como ves, sea cual sea el método de restauración que utilices, el passphrase es indispensable. Así que asegúrate de hacer una copia de seguridad con cuidado. También puedes hacer varias copias, en función de tu estrategia de seguridad.



## 8. Actualizar aplicación



Para actualizar la aplicación Ashigaru, ya que la instalaste desde un archivo `.apk` y no a través de la Play Store como una aplicación normal, tendrás que descargar el nuevo archivo `.apk` correspondiente a la versión actualizada, y luego instalarlo manualmente.



Repita los pasos descritos en la sección 2 de este tutorial, excepto que cuando pulse sobre el archivo `.apk` para iniciar la instalación, **su teléfono Android debería ofrecerle la opción `Actualizar`, no `Instalar`**.



![Image](assets/fr/41.webp)



Este es un punto muy importante: si Android muestra `Install` en lugar de `Update`, probablemente esté instalando una versión fraudulenta. En este caso, interrumpa inmediatamente el proceso de instalación.



Al igual que con la primera instalación, compruebe la autenticidad e integridad del archivo `.apk` antes de proceder a la actualización.



Para saber cuándo está disponible una nueva versión, consulte de vez en cuando el sitio web oficial de Ashigaru. Tenga la seguridad de que Ashigaru es una aplicación estable y madura, heredada de Samourai Wallet, y las actualizaciones son relativamente poco frecuentes en comparación con software más joven.



## 9. Dona al proyecto Ashigaru



Ashigaru es un proyecto de código abierto. Si quieres apoyar su desarrollo, puedes hacer una donación directamente desde la aplicación a través de PayNym.



Para ello, haga clic en su PayNym en la parte superior derecha de la interfaz y, a continuación, seleccione su código de pago que empieza por `PM...`.



![Image](assets/fr/36.webp)



A continuación, pulsa el botón `+` situado en la parte inferior derecha de la pantalla.



![Image](assets/fr/37.webp)



Selecciona `Ashigaru Open Source Project` como destinatario.



![Image](assets/fr/38.webp)



Haga clic en el botón `CONECTAR` para establecer el canal de comunicación BIP47 (más información sobre este protocolo en el tutorial a continuación).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Una vez confirmada la transacción de notificación, puede enviar sus donativos al proyecto haciendo clic en la pequeña flecha blanca de la esquina superior derecha de la interfaz.



![Image](assets/fr/40.webp)



Ahora ya sabe cómo utilizar las funciones básicas de la aplicación Ashigaru. En futuros tutoriales, veremos cómo aprovechar las transacciones de gasto avanzadas, así como Whirlpool, la implementación coinjoin heredada de Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

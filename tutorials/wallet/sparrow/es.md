---
name: Gorrión Wallet
description: Instalación, configuración y uso de Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet es un software de gestión de carteras Bitcoin de autocustodia desarrollado por Craig Raw. Este software de código abierto es apreciado por los bitcoiners por sus numerosas funciones y su Interface intuitivo.

Hay dos formas de utilizar Sparrow:


- Como una Hot Wallet, donde sus claves privadas se almacenan en su PC.
- Como gestor de Cold Wallet, donde las claves privadas se mantienen en un Hardware Wallet. En este modo, Sparrow sólo manipula información pública de Wallet, rastrea fondos, genera direcciones y construye transacciones, pero la firma de Hardware Wallet es necesaria para que estas transacciones sean válidas. Por tanto, puede sustituir a aplicaciones como Ledger Live o Trezor Suite.

Sparrow soporta monederos de firma única y multi-firma, y permite una gestión fluida de múltiples monederos. Por ejemplo, puedes controlar simultáneamente una Wallet conectada a una Ledger, otra a un Trezor, y tener también una Hot Wallet.

El software también ofrece funciones avanzadas de control de monedas, que le permiten elegir con precisión qué UTXO utilizar en sus transacciones para optimizar su confidencialidad.

En términos de conexión, Sparrow te permite conectarte a tu propio nodo Bitcoin, ya sea remotamente a través de un Servidor Electrum, o con Bitcoin Core. También es posible usar un nodo público si aún no tienes uno propio. Las conexiones remotas se realizan a través de Tor.

## Instalar Sparrow Wallet

Vaya a [la página oficial de descarga de Sparrow Wallet](https://sparrowwallet.com/download/) y elija la versión de software que corresponda a su sistema operativo.

![Image](assets/fr/01.webp)

Es importante comprobar la integridad y autenticidad del software antes de instalarlo. Si no sabes cómo hacerlo, encontrarás un completo tutorial aquí :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Una vez instalado Sparrow, puedes saltarte las pantallas explicativas iniciales e ir directamente a la pantalla de gestión de la conexión.

![Image](assets/fr/02.webp)

## Conexión a la red Bitcoin

Para interactuar con la red Bitcoin y transmitir sus transacciones, Sparrow debe estar conectado a un nodo Bitcoin. Hay tres formas principales de establecer esta conexión:


- 🟡 Utilizando un nodo público, es decir, conectándote a un nodo de terceros que permita este tipo de conexiones. Si no tienes tu propio nodo Bitcoin, esta opción te permite empezar a usar Sparrow rápidamente. Sin embargo, el nodo al que te conectes verá todas tus transacciones, lo que podría comprometer tu confidencialidad. Tener control sobre tus claves es esencial, pero tener tu propio nodo es aún mejor. Así que utiliza esta opción sólo si estás empezando, siendo consciente de los riesgos para tu privacidad.
- 🟢 Conexión a un nodo Bitcoin Core. Si tienes tu propio nodo Bitcoin Core, puedes conectarlo a Sparrow Wallet, ya sea localmente si Bitcoin Core está instalado en la misma máquina, o remotamente.
- 🔵 Conexión a través de un servidor Electrum. Si tu nodo Bitcoin está equipado con Electrs, como es el caso de las soluciones node-in-a-box como Umbrel o Start9, puedes conectarte a él remotamente desde Sparrow.

**Es preferible utilizar una conexión a través de Electrs o Bitcoin Core en su propio nodo para reducir la necesidad de confiar en un tercero y optimizar su confidencialidad**

### Conectarse a un nodo público 🟡

Conectarse a un nodo público es muy sencillo. Haz clic en la pestaña "*Servidor público*".

![Image](assets/fr/03.webp)

Seleccione un nodo de la lista desplegable.

![Image](assets/fr/04.webp)

A continuación, haga clic en "*Probar conexión*".

![Image](assets/fr/05.webp)

Una vez conectado, Sparrow Wallet mostrará una marca amarilla en la esquina inferior derecha de Interface para indicar que estás conectado a un nodo público.

![Image](assets/fr/06.webp)

### Conexión a un Bitcoin Core 🟢

El segundo método para conectarse a un nodo Bitcoin es vincular Sparrow a un Bitcoin Core. Si el Bitcoin Core está instalado en la misma máquina, la autenticación será a través del archivo cookie. Si Bitcoin Core está en una máquina remota, necesitará usar la contraseña definida en el archivo `Bitcoin.conf`.

Ten en cuenta que si utilizas un nodo Core Bitcoin podado, no podrás restaurar un Wallet que contenga transacciones anteriores a los bloques almacenados localmente. Sin embargo, para una nueva Wallet creada en Sparrow, esto no será un problema: tus nuevas transacciones serán visibles, incluso con un nodo podado.

Para configurar un nodo Bitcoin Core, puede consultar uno de los siguientes tutoriales, en función de su sistema operativo:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
En Sparrow, vaya a la pestaña "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Con Bitcoin Core local:**

Si Bitcoin Core está instalado en su ordenador, localice el archivo `Bitcoin.conf` entre los archivos de software. Si este archivo no existe, puede crearlo. Ábralo con un editor de texto e inserte la siguiente línea:

```ini
server=1
```

A continuación, guarda los cambios.

También puede hacerlo a través del gráfico Interface de Bitcoin-QT navegando a "*Configuración*" > "*Opciones...*" y activando la opción "*Habilitar servidor RPC*".

No olvide reiniciar el programa después de realizar estos cambios.

![Image](assets/fr/08.webp)

A continuación, vuelva a Sparrow Wallet e introduzca la ruta a su archivo cookie, normalmente ubicado en la misma carpeta que `Bitcoin.conf`, dependiendo de su sistema operativo:

| **macOS** | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin | |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Deje los demás parámetros por defecto, URL `127.0.0.1` y puerto `8332`, y haga clic en "*Test Connection*".

![Image](assets/fr/10.webp)

Se establece la conexión. Aparecerá una marca Green en la esquina inferior derecha para indicar que está conectado a un nodo Bitcoin Core.

![Image](assets/fr/11.webp)

**Con Bitcoin Core remote:**

Si Bitcoin Core está instalado en otra máquina conectada a la misma red, localice primero el archivo `Bitcoin.conf` entre los archivos de software. Si este archivo aún no existe, puede crearlo. Abra este archivo con un editor de texto y añada la siguiente línea:

```ini
server=1
```

Después de editar el archivo, asegúrate de guardarlo en la carpeta adecuada para tu sistema operativo:

| **macOS** | ~/Library/Application Support/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

Esta operación también puede realizarse a través del Bitcoin-QT Interface gráfico. Vaya al menú "*Configuración*", luego a "*Opciones...*", y active la opción "*Habilitar servidor RPC*" marcando la casilla correspondiente. Si el fichero `Bitcoin.conf` no existe, puedes crearlo directamente desde esta Interface pulsando en "*Abrir fichero de configuración*".

![Image](assets/fr/12.webp)

Encuentra la IP Address de la máquina que aloja Bitcoin Core en tu red local. Para ello, puede utilizar una herramienta como [Angry IP Scanner](https://angryip.org/). Asumamos, por el bien del argumento, que la IP Address de tu nodo es `192.168.1.18`.

En el fichero `Bitcoin.conf`, añade las siguientes líneas, configurando `rpcbind=192.168.1.18` para que coincida con la IP Address de tu nodo.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

En el archivo `Bitcoin.conf`, añade un nombre de usuario y una contraseña para las conexiones remotas. Asegúrate de sustituir `loic` por tu nombre de usuario y `my_password` por una contraseña segura:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Después de modificar y guardar el archivo, reinicie el software Bitcoin-QT.

Ahora puedes volver a Sparrow Wallet. Vaya a la pestaña "*User / Pass*". Introduzca el nombre de usuario y la contraseña que configuró en el archivo `Bitcoin.conf`. Deje el resto de parámetros por defecto, es decir, URL `127.0.0.1` y puerto `8332`. A continuación, haz clic en "*Probar conexión*".

![Image](assets/fr/15.webp)

La conexión está establecida. Aparecerá una marca Green en la esquina inferior derecha para indicar que está conectado a un nodo Bitcoin Core.

![Image](assets/fr/16.webp)

### Conexión a un servidor Electrum 🔵

La última opción para conectarse es utilizar un servidor Electrum remoto. Este método te permite conectarte a tu nodo vía Tor desde otro dispositivo, y aprovecha un indexador para navegar por tus carteras en Sparrow más rápidamente. Es particularmente adecuado si tienes una solución node-in-a-box como Umbrel o Start9, que te permiten instalar Electrs con un solo clic.

Para ello, obtenga el Address Tor `.onion' de su servidor Electrum. Con Umbrel, por ejemplo, lo encontrarás en la aplicación Electrs.

![Image](assets/fr/17.webp)

En Sparrow Wallet, accede a la pestaña "*Private Electrum*".

![Image](assets/fr/18.webp)

Introduzca su Tor Address en el espacio proporcionado. Otros ajustes pueden permanecer por defecto. Luego haga clic en "*Probar Conexión*".

![Image](assets/fr/19.webp)

Se confirma la conexión. Si cierra esta ventana, aparecerá una marca azul en la esquina inferior derecha, indicando que está conectado a un servidor Electrum.

![Image](assets/fr/20.webp)

## Crear una cartera cálida

Ahora que Sparrow Wallet está configurado para comunicarse con la red Bitcoin, estás listo para crear tu primer Wallet. Esta sección te guía a través de la creación de una Hot Wallet, es decir, una Wallet cuyas claves privadas están almacenadas en tu ordenador. Dado que su ordenador es una máquina compleja conectada a Internet, presenta una superficie de ataque muy grande. En consecuencia, una Hot Wallet sólo debería utilizarse para cantidades limitadas de bitcoins. Para almacenar cantidades mayores, opte por una Wallet segura con una Hardware Wallet. Si esto es lo que estás buscando, puedes pasar a la siguiente sección.

Para crear una Hot Wallet, desde la pantalla de inicio de Sparrow Wallet, haz clic en la pestaña "*Archivo*" y luego en "*Nueva Wallet*".

![Image](assets/fr/21.webp)

Introduzca un nombre para su cartera y haga clic en "*Crear Wallet*".

![Image](assets/fr/22.webp)

En la parte superior de la Interface, puede elegir si desea crear una cartera "*Single Signature*" o "*Multi Signature*". Justo debajo, selecciona el tipo de script para bloquear tus UTXOs. Le recomiendo que utilice el último estándar: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

A continuación, haga clic en "*New or Imported Software Wallet*".

![Image](assets/fr/24.webp)

Elija el estándar BIP39, ya que es compatible con prácticamente todos los programas de la cartera Bitcoin. A continuación, elija la longitud de su frase de recuperación. Actualmente, una frase de 12 palabras es suficiente, ya que ambas ofrecen una seguridad similar, pero la frase de 12 palabras es más sencilla de guardar.

![Image](assets/fr/25.webp)

Haga clic en el botón "*generate Nuevo*" para generate su Wallet's Mnemonic frase. Esta frase te da acceso completo y sin restricciones a todos tus bitcoins. Cualquiera en posesión de esta frase puede robar tus fondos, incluso sin acceso físico a tu ordenador.

La frase de 12 palabras restablece el acceso a tus bitcoins en caso de pérdida, robo o rotura de tu ordenador. Por lo tanto, es muy importante guardarla con cuidado y almacenarla en un lugar seguro.

Puede inscribirlo en papel o, para mayor seguridad, grabarlo en acero inoxidable para protegerlo de incendios, inundaciones o derrumbes. La elección del soporte para tu Mnemonic dependerá de tu estrategia de seguridad, pero si utilizas Sparrow como Wallet de gasto caliente que contiene cantidades moderadas, el papel debería ser suficiente.

Para más información sobre la forma correcta de guardar y gestionar tu frase Mnemonic, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
![Image](assets/fr/26.webp)

**Obviamente, nunca debes compartir estas palabras en Internet, como hago yo en este tutorial. Este ejemplo Wallet se utilizará sólo en el Testnet y se eliminará al final del tutorial.**

También puedes optar por añadir un passphrase BIP39 haciendo clic en la casilla "*Usar passphrase*". Advertencia: utilizar un passphrase puede ser muy útil, pero si no entiendes cómo funciona, puede ser muy arriesgado. Por eso te aconsejo encarecidamente que leas este breve artículo teórico sobre el tema:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Una vez que hayas guardado tu Mnemonic y cualquier passphrase en un soporte físico, haz clic en "*Confirmar copia de seguridad*".

![Image](assets/fr/27.webp)

Vuelva a introducir sus 12 palabras para confirmar que se han guardado correctamente y, a continuación, haga clic en "*Crear almacén de claves*".

![Image](assets/fr/28.webp)

A continuación, haga clic en "*Import Keystore*" para generate sus claves de cartera de la frase Mnemonic.

![Image](assets/fr/29.webp)

Haga clic en "*Aplicar*" para finalizar la creación de la cartera.

![Image](assets/fr/30.webp)

Establece una contraseña segura para acceder a tu cartera de Sparrow. Es una buena idea guardar esta contraseña en un gestor de contraseñas, para no olvidarla. Tenga en cuenta que esta contraseña no juega ningún papel en la derivación de sus claves. Sólo se utiliza para acceder a su Wallet a través de Sparrow Wallet. Así que, incluso sin esta contraseña, tu frase Mnemonic será suficiente para acceder a tus bitcoins desde cualquier aplicación compatible con BIP39.

![Image](assets/fr/31.webp)

Tu Hot Wallet está ahora creada. Puedes saltar a la sección *Recibir Bitcoins* de este tutorial si no planeas usar una Hardware Wallet con Sparrow.

## Gestión de una cartera Cold

La segunda forma de utilizar Sparrow Wallet es configurarlo como gestor de cartera con un Hardware Wallet. En esta configuración, las claves privadas de su Bitcoin Wallet permanecen exclusivamente en la Hardware Wallet, mientras que Sparrow sólo accede a la información pública. Este enfoque ofrece un mayor nivel de seguridad que los monederos Hot comentados anteriormente, ya que las claves privadas se guardan en un dispositivo especializado, a menudo con un chip seguro, que no está conectado a Internet y, por lo tanto, presenta una superficie de ataque mucho menor que un ordenador tradicional.

Hay dos maneras principales para conectar su Hardware Wallet a Sparrow:


- Por cable, se utiliza habitualmente con modelos básicos como Trezor Safe 3 o Ledger Nano S Plus ;
- En modo Air-Gap, es decir, sin conexión directa por cable, mediante tarjeta MicroSD o código QR Exchange.

Sparrow soporta todos estos métodos de comunicación y es compatible con la mayoría de los monederos hardware del mercado.

Para este tutorial, utilizaré una Ledger Nano S con cable, pero el procedimiento es similar en modo Air-Gap. Encontrarás detalles específicos para tu Hardware Wallet en su tutorial dedicado sobre Plan ₿ Network.

Antes de empezar, asegúrese de que la Wallet ya está configurada en su Hardware Wallet. Si utiliza una conexión por cable, conéctela a su ordenador mediante el cable.

Para importar el llamado "*Keystore*" (la información pública necesaria para gestionar la cartera) a Sparrow Wallet, haga clic en la pestaña "*Archivo*" y, a continuación, en "*Nuevo Wallet*".

![Image](assets/fr/32.webp)

Pon un nombre a tu cartera y haz clic en "*Crear Wallet*". Te aconsejo que introduzcas el nombre de tu Hardware Wallet para identificarla fácilmente más adelante.

![Image](assets/fr/33.webp)

En la parte superior de Interface, elija entre una cartera "*Single Signature*" o "*Multi Signature*". Para nuestro ejemplo, configuraremos una cartera de una sola firma.

Justo debajo, selecciona el tipo de script para bloquear tus UTXOs. Si tu Hardware Wallet lo soporta, te sugiero que elijas "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

A continuación, el procedimiento varía en función de su método de conexión. Si utilizas un método Air-Gap, selecciona "*Airgapped Hardware Wallet*". A continuación, sigue las instrucciones específicas de tu dispositivo.

![Image](assets/fr/35.webp)

Si utilizas una conexión por cable, como en mi caso, elige "*Conectado Hardware Wallet*".

![Image](assets/fr/36.webp)

Haz clic en "*Escanear*" para que Sparrow detecte tu dispositivo. Asegúrate de que está enchufado y desbloqueado. Para algunos modelos, como el Ledger, tendrás que abrir la aplicación "*Bitcoin*" para activar la detección.

![Image](assets/fr/37.webp)

Seleccione "*Importar almacén de claves*".

![Image](assets/fr/38.webp)

Haga clic en "*Aplicar*" para finalizar la creación de la cartera.

![Image](assets/fr/39.webp)

Establezca una contraseña fuerte para asegurar el acceso a su Sparrow Wallet. Esta contraseña protegerá tus claves públicas, direcciones e historial de transacciones. Le recomendamos que la guarde en un gestor de contraseñas. Ten en cuenta que esta contraseña no juega ningún papel en la derivación de tus claves. Incluso sin ella, puedes recuperar el acceso a tus bitcoins con tu Mnemonic a través de cualquier software compatible con BIP39.

![Image](assets/fr/40.webp)

Su cartera de gestión está ahora configurada en Sparrow.

![Image](assets/fr/41.webp)

## Recibir bitcoins

Ahora que tu Wallet está configurado en Sparrow, puedes recibir bitcoins. Simplemente accede al menú "*Recibir*".

![Image](assets/fr/42.webp)

Sparrow mostrará la primera Address sin usar en tu Wallet. Puedes añadir una "*Etiqueta*" a esta Address para recordar el origen de estos satoshis en el futuro.

![Image](assets/fr/43.webp)

Si está utilizando una Hot Wallet, la Address mostrada puede utilizarse inmediatamente, ya sea copiándola o escaneando el código QR asociado.

Si estás usando un Hardware Wallet, es muy importante que compruebes el Address en la pantalla del dispositivo antes de usarlo. Para dispositivos con cable, conecta y desbloquea tu Hardware Wallet, luego en Sparrow, haz clic en "*Mostrar Address*". Asegúrese de que la Address que se muestra en su Hardware Wallet coincide con la que se muestra en Sparrow.

![Image](assets/fr/44.webp)

Para los usuarios de Hardware Wallet Air-Gap, la verificación Address varía según el modelo de dispositivo. Consulte el tutorial dedicado a Plan ₿ Network para obtener instrucciones precisas.

Una vez que el pagador haya emitido la transacción, la verá aparecer en la pestaña "*Transacciones*". Puede hacer clic en ella para obtener más detalles, como el txid.

![Image](assets/fr/45.webp)

En la pestaña "*Direcciones*" encontrarás una lista de todas las direcciones de tu bandeja de entrada. Puedes ver si ya han sido utilizadas y si se ha añadido una etiqueta. *Las direcciones "Recibir*" son las que Sparrow muestra cuando haces clic en "*Recibir*" y están destinadas a los pagos entrantes. Las direcciones "*Cambiar*" se utilizan para Exchange en tus transacciones, es decir, para recuperar la parte no utilizada de tus UTXOs en entradas.

![Image](assets/fr/46.webp)

La pestaña "*UTXOs*" te muestra todos tus UTXOs, es decir, los fragmentos de Bitcoin que tienes. Puedes ver la cantidad de cada UTXO y la etiqueta asociada.

![Image](assets/fr/47.webp)

## Enviar bitcoins

Ahora que tienes unos cuantos satoshis en tu Wallet, también tienes la opción de enviar algunos. Aunque hay varias formas de hacerlo, te recomiendo que utilices el menú "*UTXOs*" para tener un control más preciso sobre las monedas que gastas (*control de monedas*), en lugar de ir directamente al menú "*Enviar*" (aunque esto último puede bastar si eres principiante).

![Image](assets/fr/48.webp)

Seleccione los UTXO que desea utilizar como entradas para esta transacción y, a continuación, haga clic en "*Enviar seleccionados*". Este enfoque le permite seleccionar las fuentes más apropiadas entre sus UTXOs, en función de sus gastos y de las etiquetas aplicadas cuando se reciben, con el fin de optimizar la confidencialidad de sus pagos. Asegúrese de que la suma de los UTXO seleccionados es superior al importe que desea enviar.

![Image](assets/fr/49.webp)

Introduzca el Address del destinatario en el campo "*Pagar a*". También puede escanear el Address con su webcam haciendo clic en el icono de la cámara. El botón "*+Añadir*" te permite pagar a varias direcciones en una sola transacción.

![Image](assets/fr/50.webp)

Añada una etiqueta a su transacción para recordar su finalidad. Esta etiqueta también se asociará a su eventual Exchange.

![Image](assets/fr/51.webp)

Introduzca el importe que se enviará a esta Address.

![Image](assets/fr/52.webp)

Ajuste la tarifa de acuerdo con las condiciones actuales del mercado. Puede hacerlo introduciendo un valor absoluto de la tasa o ajustándola con el control deslizante.

![Image](assets/fr/53.webp)

En la parte inferior de la Interface, puedes elegir entre "*Eficiencia*" y "*Privacidad*". En mi caso, la opción "*Privacidad*" no está disponible, ya que sólo tengo una UTXO en esta cartera. "*Eficiencia*" corresponde a una transacción clásica, mientras que "*Privacidad*" es una transacción de tipo Stonewall, una estructura de transacción que refuerza su confidencialidad simulando un mini-CoinJoin, lo que hace más complejo el análisis de la cadena.

![Image](assets/fr/54.webp)

Sparrow muestra un diagrama resumen que muestra tus entradas, salidas y tasas de transacción (ten en cuenta que las tasas no son realmente una salida, al contrario de lo que sugiere este diagrama). Si está satisfecho con todo, haga clic en "*Crear transacción*".

![Image](assets/fr/55.webp)

Esto le lleva a una página que detalla el Elements de su transacción. Compruebe que toda la información es correcta y, a continuación, haga clic en "*Finalizar transacción para firmar*".

![Image](assets/fr/56.webp)

Es importante mantener el Sighash por defecto. Para entender por qué, echa un vistazo a este curso de formación, en el que explico todo lo que necesitas saber sobre Sighash:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
En la siguiente pantalla, las opciones varían según el tipo de Wallet que esté utilizando:


- Para un Hardware Wallet Air-Gap, haz clic en "*Mostrar QR*" para mostrar un PSBT que puedes firmar con tu dispositivo, luego carga el PSBT firmado en Sparrow usando "*Escanear QR*". La opción "*Guardar transacción*" funciona de forma similar, pero con intercambios en una microSD ;
- Para una Hot Wallet, basta con hacer clic en "*Firmar*" e introducir la contraseña de Wallet para firmar ;
- Para una Hardware Wallet con cable, haz clic también en "*Firmar*" para enviar la transacción sin firmar a tu dispositivo.

![Image](assets/fr/57.webp)

En su Hardware Wallet, compruebe el Address del destinatario, el importe enviado y los gastos. Si todo es correcto, procede a la firma.

Una vez firmada la transacción, reaparecerá en Sparrow, lista para ser emitida en la red Bitcoin para su posterior inclusión en un bloque. Si todo es correcto, haga clic en "*Broadcast Transaction*".

![Image](assets/fr/58.webp)

Su transacción ya ha sido emitida y está a la espera de confirmación.

![Image](assets/fr/59.webp)

## Gestión y configuración de carteras en Sparrow

En la pestaña "*Configuración*" encontrará información detallada sobre su cartera, como :


- Tipo de cartera (single-sig o multi-sig) ;
- Tipo de guión utilizado ;
- El nombre que ha asignado a la cartera ;
- Impresión de llave maestra;
- La ruta de derivación ;
- La clave pública extendida de la cuenta.

![Image](assets/fr/60.webp)

El botón "*Exportar*" le permite exportar la información de su cartera para que pueda utilizarla en otro software conservando la información configurada en Sparrow.

El botón "*Añadir cuenta*" le permite añadir una cuenta adicional a su cartera. Una cuenta corresponde a un conjunto separado de direcciones de buzón de entrada. Esta función puede ser útil, por ejemplo, si desea separar una cuenta personal de una de empresa, con una única frase Mnemonic.

El botón "*Avanzado*" da acceso a los ajustes avanzados, como personalizar la búsqueda Address de Sparrow y cambiar la contraseña de la cartera.

![Image](assets/fr/61.webp)

Cuando cierras Sparrow Wallet, tu Wallet se bloquea automáticamente. La próxima vez que abras el software, una ventana te pedirá que desbloquees tu Wallet con su contraseña.

![Image](assets/fr/62.webp)

Si esta ventana no se abre, o si desea abrir otra cartera en Sparrow, haga clic en la pestaña "*Archivo*" y seleccione "*Abrir Wallet*".

![Image](assets/fr/63.webp)

Esto abrirá tu Administrador de Archivos en la carpeta donde Sparrow almacena tus monederos. Simplemente selecciona la Wallet que deseas abrir e introduce la contraseña para desbloquearla.

![Image](assets/fr/64.webp)

En el menú "*Archivo*", dentro de "*Configuración*", encontrarás los parámetros de conexión a la red Bitcoin ya explorados en apartados anteriores. También puedes ajustar diversos parámetros, como la unidad utilizada, la moneda fiduciaria para las conversiones y las fuentes de información.

![Image](assets/fr/65.webp)

La pestaña "*Ver*" ofrece opciones de personalización y acceso a algunos comandos útiles, como "*Refrescar Wallet*", que actualiza la búsqueda de transacciones de su cartera.

![Image](assets/fr/66.webp)

La pestaña "*Herramientas*" agrupa varias herramientas avanzadas, como :


- "*Firmar/Verificar mensaje*" permite demostrar la posesión de un Address receptor o verificar una firma.
- "*Enviar a muchos*" ofrece una Interface simplificada para realizar transacciones a varias direcciones receptoras a la vez, lo que resulta práctico para el gasto por lotes.
- "*Sweep Private Key*" te permite recuperar bitcoins asegurados por una simple clave privada y transferirlos a tu Sparrow Wallet. Esto puede ser particularmente útil para aquellos con bitcoins que datan de principios de 2010, antes de la era de los monederos HD.
- "Verificar descarga" comprueba la integridad y autenticidad del software descargado antes de instalarlo en su dispositivo.
- "*Reiniciar en*" le permite cambiar a sus monederos en redes Testnet o Signet. Esto puede ser útil si deseas acceder a redes de prueba con monedas sin valor real.

![Image](assets/fr/67.webp)

Ahora ya lo sabe todo sobre el software Sparrow Wallet, una excelente herramienta para gestionar diariamente sus carteras Bitcoin.

Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. Siéntete libre de compartirlo en tus redes sociales. Muchas gracias

También recomiendo este otro tutorial en el que explico cómo configurar la COLDCARD Q Hardware Wallet con la Wallet de Sparrow :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3
---
name: Coin Control
description: Iníciese en Coin Control, una herramienta clave para proteger su privacidad en Bitcoin
---
![cover](assets/cover.webp)


*Este tutorial está importado de [una lección de Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Introducción



La solidez del protocolo Bitcoin está garantizada por conceptos clave simples. Entre ellos destaca la transparencia: todas las transacciones de Bitcoin son públicas y fácilmente verificables por cualquiera. Aunque esta característica es un pilar del protocolo, ya que previene fraudes y garantiza la autenticidad de los fondos, también puede representar un desafío para la confidencialidad. **¿Te has preguntado si tanta transparencia puede afectar tu privacidad?**



Deberías hacerlo. Aunque acumular Satoshi no kyc es bastante fácil, tu privacidad corre el mayor riesgo justo en la fase de gasto.



### Qué pasa cuando gastas un UTXO



Gastar Bitcoin no es simplemente transferir valor a otra persona.



En efecto, al consumir uno de sus UTXO, usted debe cumplir las condiciones impuestas para la transparencia del protocolo, ya que tiene la obligación de demostrar que es el propietario de esos fondos. Por lo tanto, usted se hace responsable de :




- exponga su clave pública;
- producir una firma digital.



El momento del gasto es, por tanto, el más crítico: **gastar Bitcoin es un acto que debe hacerse conscientemente y con el mayor control posible**.



## Coin Control



En el protocolo Bitcoin, elementos como _cuenta_ o _unidades monetarias_ no existen. El concepto de UTXO se explica excelentemente en el siguiente curso, que recomiendo encarecidamente:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Con Bitcoin lo que acumulas y luego gastas son pequeñas o grandes unidades de cuenta medidas en Satoshi, representadas por `salidas de transacción no gastadas`, los **UTXO**, también llamados `coins`. Cuando utilizas UTXOs para crear una transacción, se destruyen completamente y se crean otros UTXOs en su lugar.



Los monederos software se desarrollan para hacer esta elección automáticamente, utilizando monedas seleccionadas "al azar", adoptando ciertos algoritmos proporcionados por el protocolo. El único criterio que cumplen estos algoritmos, es cubrir la cantidad necesaria para el gasto.



Pueden mezclar UTXOs de diferentes edades, o favorecer el gasto de los más nuevos o "más antiguos", dependiendo del algoritmo elegido por los desarrolladores. Los mejores Software Wallets, también planean dejar al usuario con una importante elección.



El `Coin Control`manual, que también puedes encontrar referido como `Coin Selection`, es una característica de algunas Carteras Software que te permite **seleccionar manualmente UTXOs para gastar cuando construyes tu transacción**.



Supongamos que tenemos un Wallet con 3 UTXOs de 21.000, 42.000 y 63.000 Satoshi, respectivamente.



![img](assets/en/01.webp)



Si tiene que gastar 24.000 Sats y dejar que un algoritmo haga la selección automática, un buen Software Wallet podría elegir combinar UTXO 1 + UTXO 2 para pagar las tasas de 24k Sats y Miner, creando un remanente que vuelve a un Address interno del Wallet inicial.



![img](assets/en/02.webp)



Tras la transacción, la nueva situación de Wallet, contando sólo los UTXO, puede resumirse del siguiente modo.



![img](assets/en/03.webp)



Sin embargo, con el software adecuado y tu conciencia, podrías haber hecho una elección diferente, en cierto modo más correcta. Por ejemplo, seleccionando sólo el UTXO2 (de 42.000 Sats).



![img](assets/en/04.webp)



Con una situación final en su Wallet, en el nivel de UTXO, que se ve diferente de antes.



![img](assets/en/05.webp)



## ¿Por qué el coin control manual?



![img](assets/en/06.webp)



En los dos ejemplos anteriores, el saldo es en realidad el mismo `108.280 Sats`. Después de gastar 24.000 Sats, sin selección manual tendríamos 2 UTXO en Wallet; con el control manual de Coin tenemos 3 en total.



La pregunta que podríamos hacernos es la siguiente: **¿por qué hacer todo esto?** Hay, o podría haber, varias razones por las que no hemos usado `UTXO1` **y todas están en la base de por qué, en el momento de gastar, activar el coin control manual es una de las buenas prácticas a seguir**.



Seleccionar UTXOs te permite favorecer unos aspectos sobre otros. La elección depende realmente de los objetivos que quieras alcanzar.



### Privacidad



Una de las principales ventajas, cuando se trata del control manual de Coin, es una **mayor privacidad para el gastador**. Tomemos siempre nuestro ejemplo: el gasto de 24.000 Satoshi _sin selección manual de Coin_. Dado que Blockchain de Bitcoin es un registro público, un observador externo puede declarar, sin ningún género de dudas, que las entradas `UTXO1 de 21.000 Sats` y `UTXO2 de 42.000 Sats`, así como el resto, la `UTXO5 de 38.280 Sats` **pertenecen las tres al mismo usuario**.



En cambio, al seleccionar manualmente "UTXO2", "UTXO1" permanece completamente reservado, en el conjunto UTXO a la espera de ser utilizado en un momento más apropiado.



El `UTXO1` podría proceder de una fuente KYC, como un pago recibido en Exchange por bienes y servicios, mientras que los demás UTXOs no. Mezclar un UTXO-kyc con otros más confidenciales compromete el conjunto de anonimato de los fondos no kyc.



**Los fondos KYC llevarían inevitablemente a rastrear la identidad del pagador. Si fuera tu wallet, ¿querrías que un observador externo pudiera rastrear tu identidad con una certeza tan absoluta?**



Intente entonces considerar que las Carteras que implementan la selección manual de UTXOs, por ejemplo, permiten **segregar uno o más UTXOs**, una función a utilizar cuando se presenten estas situaciones.



Aunque estoy convencido de que los fondos KYC deben mantenerse en una Wallet separada de la Bitcoin comprada sin kyc, si este es tu caso la segregación de algunas de tus direcciones es una ayuda clave, que podrías aprovechar aprendiendo a seleccionar manualmente tus entradas de gasto.



### Ahorro de tasas



La selección de la UTXO correcta para realizar un gasto, **permite optimizar las tarifas**. De nuevo partiendo de nuestro ejemplo inicial, Software Wallet seleccionó dos UTXOs para cubrir el gasto a realizar. Dos UTXOs implican dos firmas a mostrar a la red. De ello se deduce que la transacción tiene un mayor "peso" en términos de vBytes.



Con el control manual de Coin, en cambio, puede seleccionar sólo uno que sea suficiente para cubrir el importe, ahorrando comisiones al disminuir el "peso" de la transacción.



En épocas en que las tasas son elevadas, pero usted se ve obligado a gastar Bitcoin On-Chain (por ejemplo, para abrir un canal Lightning Network), es cuando el control Coin resulta ser el incentivo económico adecuado al que recurrir.



### Agregación de los restos



Cuando realizas un pago y utilizas Bitcoin On-Chain, la posibilidad de recibir cambio casi siempre se convierte en una certeza. Cada resto es en sí mismo una pequeña pérdida de privacidad, ya que revela a la red (y especialmente al receptor del pago) una Address tuya que puede asociarse a tu entrada de origen.



Teniendo en cuenta que los mejores Wallet HDs generate direcciones especiales para los remanentes, puedes reconocerlos fácilmente y "segregar" todos los remanentes de las distintas transacciones realizadas; cuando hayan alcanzado una determinada cantidad puedes seleccionarlos manualmente y consolidarlos, o pasar a Lightning Network (mi método preferido) y procesarlos para recuperar la privacidad perdida en el gasto.



### Gastos de una Cold Wallet



La Cold Wallet es un instrumento con el que se puede obtener razonablemente un buen grado de seguridad, para guardar cualquier cantidad de fondos para mantenerla apartada durante un largo periodo de tiempo. Sin embargo, pueden surgir imprevistos, por lo que surge la necesidad de echar mano de los ahorros y hacer frente a algunos gastos inesperados.



No sé cuántos pueden compartir mi planteamiento, pero mi consejo es **nunca realices el gasto directamente desde Cold Wallet, para evitar recibir el cambio entre las direcciones de las mismas**. Aprende a seleccionar manualmente los UTXOs necesarios para cubrir el gasto, transfiérelos a una Wallet Hot y prepara tu transacción desde esta última. Cualquier cambio, entonces, puede enviarlo de nuevo a una Cold Wallet Address (si la cantidad es adecuada), utilizarlo para otros gastos, o aún segregarlo como acabamos de ver.



## Presentación práctica


Después de la introducción técnica del `por qué`, vamos a ver cómo poner en práctica el control manual Coin con diferentes programas, de sobremesa y móviles. Utilizaremos siempre la misma Wallet BIP39, importada en cada una de las herramientas elegidas, para mostrarte las pequeñas diferencias entre ellas.



## Sobremesa Wallet



### Sparrow



Si utiliza Sparrow, abra su Wallet y seleccione _UTXOs_ en el menú de la izquierda. Verá una lista de todos los UTXOs asociados a su Wallet.



Basta con hacer clic con el ratón en uno de ellos y luego elegir _Enviar Seleccionado_. Sparrow también le muestra el total disponible para gastar después de la selección, justo al lado del comando. Gráficamente Sparrow le muestra la UTXO seleccionada resaltándola en azul.



![img](assets/en/07.webp)



También puede seleccionar más de uno. Ayúdate de la tecla _CTRL_ para seleccionar UTXOs no adyacentes en la lista.



![img](assets/en/08.webp)



Después de seleccionar manualmente UTXO, puede empezar a construir la operación, y Sparrow le mostrará bien, gráficamente, cómo está constituida.



![img](assets/en/09.webp)



#### Segregación de UTXO



Segregar fondos significa "bloquearlos" dentro de Wallet para que no puedan ser utilizados como entrada en una transacción. Sparrow permite esta funcionalidad, a la que se accede siempre desde el menú _UTXOs_: se sitúa el ratón sobre el UTXO a "bloquear" y se pulsa el botón derecho del ratón. Entre las funcionalidades de este procedimiento aparecerá _Congelar UTXO_. Así podrá segregar Coins con los monederos Sparrow.



![img](assets/en/29.webp)



### Electrum



Si su escritorio Wallet es Electrum, debe saber que puede seleccionar manualmente UTXOs desde el menú _Direcciones_ o desde el menú _Monedas_. En ambos menús, la selección se realiza apuntando con el ratón al UTXO deseado y eligiendo _Añadir al control Coin_ tras hacer clic con el botón derecho.



![img](assets/en/10.webp)



Incluso con este software puede seleccionar más de una UTXO, ayudándose con la tecla _CTRL_ de su teclado si no están adyacentes entre sí.



![img](assets/en/11.webp)



Gráficamente Electrum le mostrará la selección resaltando los UTXOs seleccionados en Green, mientras que en la parte inferior aparece una barra, resaltada en el mismo color, que muestra el saldo disponible tras el control Coin.



![img](assets/en/12.webp)



Una vez que haya seleccionado la salida, o salidas, puede construir su transacción como lo hace habitualmente desde el menú _Enviar_.



#### Segregación de UTXO



Electrum proporciona esta funcionalidad yendo al menú _Coins_, donde irás a seleccionar un UTXO en particular y luego eligiendo _Freeze_ con un clic derecho. Puede "congelar" la Address incluso sin fondos desde el menú _Direcciones_, o la "Coin" para no gastarla.



![img](assets/en/28.webp)



### Nunchuk



Nunchuk te permite seleccionar manualmente UTXOs desde el menú principal una vez abierto. Inicia Nunchuk y haz clic en _Ver monedas_.



![img](assets/en/13.webp)



Esto abre la ventana que contiene todos los UTXOs en su Wallet, donde puede seleccionar uno o más activando la marca de verificación junto a cada importe. Después de hacer su selección, continúe con _Crear transacción_.



![img](assets/en/14.webp)



A continuación, puede introducir el Address de destino y establecer el importe y las tasas.



![img](assets/en/15.webp)



#### Segregación de UTXO



Para completar, el Nunchuk también permite entre sus características, segregar una (o más) UTXOs y lo hace de dos maneras diferentes. Accede al menú _Ver monedas_ y elige manualmente de la lista de monedas. A continuación, haz clic en el menú _Más_ de la parte inferior derecha: aparecerá una lista de opciones, entre las que podrás elegir _Bloquear monedas_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



También puede hacer clic en el espacio reservado a la UTXO, para acceder a la ventana _Detalles de la moneda_. Aquí aparece en la esquina superior derecha el comando para bloquear/desbloquear la UTXO en cuestión.



![img](assets/en/41.webp)



### Aplicación Blockstream



Blockstream App desktop, antes conocida como Green, te permite hacer la selección de Coin cuando ya has empezado a construir la transacción. Por lo tanto, abra su Wallet y haga clic en _Enviar_.



![img](assets/en/16.webp)



Pegue la Address de destino en el campo correspondiente y, a continuación, seleccione _Selección manual de Coin_.



![img](assets/en/17.webp)



Se abre la ventana en la que puede seleccionar una o varias monedas UTXO. En el ejemplo siguiente, hemos seleccionado dos monedas. A continuación, confirme su elección haciendo clic en _Confirmar selección Coin_.



![img](assets/en/18.webp)



Establezca el importe y las comisiones y, a continuación, proceda normalmente con su transacción.



![img](assets/en/19.webp)



⚠️ N.B. En el menú _Coins_ de Green hay elementos _Lock_/_Unlock_ que prefiguran la posibilidad de segregar UTXO. Esta característica sólo se activa en las llamadas cuentas Multisig; también se activa sólo seleccionando UTXO de importe muy pequeño, cercano al umbral de `Dust`.



## Wallet móvil



También se pueden elegir carteras desde el móvil, que permiten seleccionar UTXOs manualmente. Veamos Blue Wallet como primer ejemplo.



### Azul Wallet



Si usted es usuario de esta Wallet, ábrala y pulse para acceder a las pantallas de control relacionadas con una de sus Carteras. Para acceder al manual de control de la Coin debe entrar en la fase de gasto y pulsar _Enviar_.



![img](assets/en/21.webp)



En la pantalla siguiente, seleccione los menús indicados por los tres puntos en la esquina superior derecha. Se abre una ventana desplegable con una serie de comandos. Elija el último: _Coin Control_.



![img](assets/en/22.webp)



En este punto Blue Wallet muestra todos sus UTXOs. Además de las cantidades, se diferencian gráficamente por diferentes colores.



![img](assets/en/27.webp)



Elija la UTXO que desee seleccionar y después seleccione _Use Coin_.



![img](assets/en/23.webp)



La Wallet azul le lleva de nuevo a la ventana _Enviar_ para continuar construyendo la transacción. Ajuste el importe y las comisiones, tras lo cual elija _Siguiente_.



![img](assets/en/24.webp)



En este punto puede finalizar la transacción, como suele hacer.



#### Segregación de una UTXO



La Wallet azul también permite segregar UTXOs, haciendo que no estén disponibles para gastar, lo que no es una mala función para una Wallet desde un dispositivo móvil. Accedes al control de la Coin con el procedimiento que acabamos de explicar y, tras seleccionar la UTXO, eliges _Freeze_ en lugar de _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



La versión móvil de Nunchuk también ofrece al usuario la posibilidad de hacer control Coin. Si utilizas esta aplicación desde el móvil, ábrela y ve al menú _Wallet_. Desde allí elige _Ver monedas_.



![img](assets/en/30.webp)



En la ventana donde aparece la lista de UTXOs, haga clic en _Select_.



![img](assets/en/38.webp)



Junto a cada UTXO aparece una función de selección. Al igual que en la versión de escritorio, la selección manual en el Nunchuk móvil se realiza marcando el cuadradito situado junto a la cantidad. La pantalla muestra el número de UTXOs seleccionados y la cantidad total disponible. Cuando haya terminado, haga clic en el símbolo ₿ en la esquina inferior izquierda, que es el comando para iniciar la construcción de la transacción.



![img](assets/en/31.webp)



Ahora puede completar la transacción, eligiendo el importe y pulsando _Continuar_.



![img](assets/en/32.webp)



Continúe como siempre, pegando un Address de destino, una descripción y personalizando la configuración de las tarifas.



#### Segregación de UTXO



También puedes segregar UTXOs con el Nunchuk del móvil. Accede a la ventana dedicada a la lista de monedas y selecciona la flecha junto al UTXO que quieras segregar.



![img](assets/en/42.webp)



Verá el espacio reservado a _Detalles de la moneda_, donde puede seleccionar _Bloquear esta moneda_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper es la última Wallet que veremos en esta guía. Vemos su funcionalidad aplicada al control de Coin con una Wallet single-sig, aunque tal uso no es el propósito de esta app en particular. Después de configurar Keeper en tu teléfono, ejecútalo y abre una Wallet que contenga algunos fondos. En el centro de la pantalla principal pulsa _Ver todas las monedas_.



![img](assets/en/34.webp)



Keeper muestra un resumen de los UTXO. Para acceder a la pantalla de selección, haga clic en _Select To Send_.



![img](assets/en/35.webp)



Puede seleccionar las monedas marcándolas haciendo clic en el comando correspondiente. Cuando haya terminado, haga clic en _Enviar_.



![img](assets/en/36.webp)



Bitcoin Keeper le lleva directamente al menú _Enviar_, donde puede construir la transacción con los UTXOs seleccionados.



![img](assets/en/37.webp)



## Hardware Wallet



Cada uno de los Billeteros Software vistos en esta guía puede ser el Interface de guardia a uno de sus Billeteros Hardware. Esto significa que el control Coin para el dispositivo de firma fuera de línea se realiza con los pasos vistos hasta ahora.



### Recomendaciones generales



El control Coin es una práctica muy eficaz para seleccionar las entradas de sus transacciones. La selección manual es aún más eficaz si, al comprar/recibir sus fondos, ha etiquetado bien la fuente de sus Satoshis. Si desea aprender bien esta técnica, le recomiendo el siguiente tutorial:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Ya hemos hablado anteriormente de la `segregación de restos`. Si quiere bloquear los restos para procesarlos más tarde y recuperar la privacidad (intercambio en Layer 2), debe tener cuidado de `etiquetarlos` cada vez que reciba uno. De las Carteras Software vistas hasta ahora, sólo Electrum colorea gráficamente los remanentes de UTXO para hacerlos visibles a simple vista. Otros, como Sparrow, le muestran la cadena en la ruta de derivación del UTXO individual (`m/84'/0'/0'/1/11`).



Para aplicar esta técnica con eficacia, recuerde añadir siempre una descripción en el cambio que reciba: la persona a la que envió sus fondos (un pago, una tutoría u otro), conoce la Address asociada al cambio y sabe que le pertenece, ¡ya que procede de la transacción que hicieron juntos!
---
name: Bricolaje Jade
description: Convierte una placa de desarrollo de 15 dólares en un Bitcoin hardware wallet totalmente funcional
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Construcción para principiantes


**Audiencia:** Constructores curiosos con poca o ninguna experiencia en empotrados.


**Duración:** 2 horas (flexible)


**Resultados:** Al final, los estudiantes podrán:



- Reconocer el modelo de seguridad de los monederos hardware DIY frente a los dispositivos comerciales.
- Montar un dispositivo de firma basado en un microcontrolador.
- Flashea el firmware de código abierto y verifica la suma de comprobación de la compilación.
- Firmar y emitir una transacción mainnet utilizando su nuevo dispositivo.


---

## Resumen


Este taller de 2 horas enseña a los principiantes a construir un Bitcoin hardware wallet funcional flasheando el firmware Jade de código abierto en una placa LilyGO T-Display de 15 dólares. Los estudiantes transforman el hardware de desarrollo genérico en un dispositivo de firma comparable a los monederos comerciales que cuestan 150 dólares, aprendiendo los fundamentos de la seguridad a través de la experiencia práctica en lugar de la teoría.


### Filosofía


Construir tu propio dispositivo de firma no es sólo cuestión de ahorrar dinero, sino de comprender la tecnología que protege tu Bitcoin. Este taller apuesta por la "seguridad a través de la comprensión" en lugar de la confianza de caja negra. Al adquirir componentes, instalar firmware de código abierto y generar entropía por sí mismos, los estudiantes reducen el riesgo de la cadena de suministro a la vez que aprenden a evaluar las afirmaciones de seguridad de forma crítica. El objetivo es la autonomía informada: los estudiantes deben comprender tanto la potencia como las limitaciones de su dispositivo DIY en comparación con las alternativas comerciales reforzadas.


---

## Introducción al concepto (15 min)


### ¿Qué es la autocustodia y por qué es importante?


Bitcoin se creó para eliminar de nuestro sistema monetario la necesidad de terceros de confianza, como bancos y empresas. En lugar de recurrir a la confianza, bitcoin utiliza las matemáticas, la física y la criptografía para que cualquiera pueda poseer y controlar su dinero sin necesidad del permiso de nadie.


El bitcoin existe en un libro de contabilidad digital global llamado blockchain, también conocido como bitcoin timechain, que es un libro de contabilidad público y transparente gestionado por ordenadores, en lugar de un libro de contabilidad centralizado como una cuenta bancaria.


Lo importante es entender que para mover bitcoin de un lugar a otro, tienes que firmar esa transacción con lo que se llama una clave privada. Es como abrir una cámara acorazada con una contraseña y trasladar el bitcoin a la cámara de otra persona. Bitcoin te da el poder de tener tú mismo las llaves de esa cámara acorazada, en lugar de depender de un banco que mueva tu dinero por ti.


Un gran poder conlleva una gran responsabilidad: si pierdes las llaves, tus fondos desaparecen para siempre. De este modo, puedes pensar en las llaves de la cámara acorazada como si fueran el propio dinero. Aunque las llaves no son lo mismo que el bitcoin, son el mecanismo para mover tus fondos y, por tanto, es extremadamente importante protegerlas. Por eso decimos "ni tus llaves, ni tus monedas".


El término autocustodia puede sonar confuso, pero todo lo que significa es tener tus propias claves privadas y controlar tu propio bitcoin. Si no tienes esa clave, estás confiando en otra persona para que la custodie por ti. Si tu bitcoin está en un ETF o en una bolsa (Mt. Gox, FTX, Coinbase, Binance, etc.), no posees bitcoin, posees un derecho sobre bitcoin. Esto introduce todo tipo de riesgos, como que pirateen las bolsas y pierdas tu bitcoin o que las empresas presten tu dinero y te den sólo una fracción de reserva. Además, los terceros de confianza tendrían el control total de tu dinero y podrían limitar o congelar las retiradas.


![image](assets/fr/01.webp)


Con la autocustodia eliminas la confianza de la ecuación. Nadie puede congelar tus fondos o denegar una transacción, puedes enviar dinero a través de las fronteras, a cualquiera, en cualquier momento, y no necesitas una cuenta bancaria, una identificación o la aprobación de nadie. Nadie puede detenerte, censurarte o robarte, liberando todo el poder del bitcoin como dinero de la libertad. Por eso decimos que con bitcoin puedes ser tu propio banco.


La Bitcoin se creó para resolver el problema de la manipulación de la confianza y el dinero, una salida de nuestro sistema actual, pero la salida sólo funciona si coges las llaves. Por eso es tan importante la autocustodia.


### ¿Qué es una Wallet?


El término wallet es un poco equívoco y, por lo tanto, puede resultar confuso. Sí, es cierto que una wallet de bitcoin, al igual que una wallet física, almacena valor. Pero la principal diferencia es que los monederos bitcoin en realidad no almacenan ningún bitcoin.


Bitcoin sólo existe como una entrada del libro mayor en el blockchain público, o dentro de las bóvedas metafóricas en el ciberespacio. Recuerda que para mover bitcoin tienes que usar tus claves para abrir la bóveda y mover las monedas a otro lugar, las claves privadas son las que se usan para gastar bitcoin. Cuando haces una transacción con tu wallet, en realidad sólo estás usando tus claves para firmar la transacción. Así es como demuestras que eres el dueño del dinero y que tienes derecho a gastar esas monedas.


Los monederos Bitcoin en realidad sólo almacenan tus claves privadas, por lo que sería más exacto llamarlos llaveros.


### Carteras Hot vs Cold


Un hot wallet es una aplicación de software que se instala en el teléfono o el ordenador. Está conectada a Internet, por lo que es más fácil de usar y más rápida a la hora de firmar transacciones, pero esto también significa que está más expuesta a hackers, malware y phishing. Se llama "caliente" porque está conectado a internet, enchufado y encendido. Un ejemplo sería un teléfono wallet o un navegador wallet.


Por otro lado, una wallet fría, o wallet de hardware, es un dispositivo que crea y almacena su clave fuera de línea. Esto elimina la posibilidad de que alguien piratee tus fondos y es mucho más seguro para los ahorros a largo plazo, sin embargo es un dispositivo que se necesita para firmar cada transacción y puede ser menos conveniente.


### Modelo de amenaza Hardware Wallet


Los monederos de hardware existen para resolver un problema fundamental: ¿cómo firmar transacciones Bitcoin sin exponer tus claves privadas a un ordenador conectado a Internet que podría verse comprometido por malware o atacantes remotos? El modelo básico de amenazas parte de la base de que tu ordenador portátil o tu teléfono de uso cotidiano son potencialmente hostiles. Una wallet de hardware crea un entorno aislado en el que las claves privadas nunca salen del dispositivo, y la firma de las transacciones se realiza en una secure element o un microcontrolador que sólo comunica la firma al ordenador central, no la clave en sí. Incluso si su ordenador está completamente comprometido, un atacante no puede robar su Bitcoin sin acceso físico al dispositivo y a su PIN.


Sin embargo, los monederos de hardware introducen sus propias amenazas. Debes confiar en que el fabricante no haya introducido puertas traseras, que la cadena de suministro no haya sido manipulada y que la generación de números aleatorios sea realmente aleatoria. Los atacantes físicos podrían extraer claves mediante ataques de canal lateral o manipulación del chip, y alguien con acceso temporal podría modificar tu dispositivo. Construir su propio hardware wallet le ayudará a entender estas ventajas y desventajas: tomará decisiones sobre elementos seguros frente a microcontroladores de uso general, sobre cómo verificar las transacciones en una pantalla y sobre cómo protegerse frente a amenazas tanto remotas como físicas. El objetivo no es conseguir una seguridad perfecta, sino comprender contra qué amenazas se está protegiendo y cuáles quedan.


### Conceptos clave



- Entropía y frases seed:** Tu wallet es tan seguro como la aleatoriedad que lo hace nacer. Mezclaremos el generador de números aleatorios del dispositivo con trucos aptos para humanos, como tiradas de dados, convertiremos esa entropía en una [frase BIP39] de 12 o 24 palabras (https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) y saldremos de la habitación con un respaldo escrito o metálico en el que confíes.
- Higiene de la frase semilla:** Trata la seed como las llaves maestras de tus ahorros. Nunca escribas las palabras en un teléfono u ordenador: los keyloggers, las capturas de pantalla y las copias de seguridad en la nube pueden filtrarlas para siempre. Mantén la frase fuera de línea, guárdala en algún lugar al que sólo tú puedas acceder y practica su lectura en voz alta antes de salir.
- Elemento seguro + microcontrolador:** Piense en la secure element como la cámara acorazada y en el microcontrolador como el cerebro. La secure element guarda las claves privadas con resistencia a la manipulación, mientras que el microcontrolador maneja la pantalla, los botones y la lógica del firmware. Tenga en cuenta que las carteras de hardware que estamos construyendo hoy en día no tienen una secure element. Esto no significa que sea inseguro, sólo que tiene un nivel menos de protección.
- Confiar en el firmware:** El firmware es el sistema operativo invisible de la wallet. Descargue siempre desde versiones etiquetadas, compruebe el hash publicado y entienda que las compilaciones reproducibles permiten que varias personas compilen el mismo código y lleguen exactamente al mismo binario. Si la suma de comprobación no coincide, no firme.


---

## ¿Qué estamos construyendo?


Estamos tomando hardware genérico, el LilyGo T-Display, y flasheando el firmware Jade SDK en él. El [Jade Plus](https://blockstream.com/jade/jade-plus/) es un wallet de código abierto que suele costar 150 dólares:


![image](assets/fr/02.webp)


Hoy, en cambio, flashearemos su firmware en un hardware de 15 dólares.


### Qué comprar


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB con carcasa, modelo K164)** - [Pedir directamente a LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) por unos 15 dólares. Esta placa ESP32 proporciona la pantalla, los botones y la interfaz USB que reflejan el Jade Plus de Blockstream. La placa ESP32 también incluye radios Wi-Fi y Bluetooth; enviaremos un firmware que las mantiene desactivadas, pero conforman su modelo de amenaza porque un código malicioso podría volver a activarlas.
- Cable USB-C** - Trae un cable con capacidad de datos para que puedas flashear el firmware y alimentar la placa directamente desde tu portátil (totalmente válido para uso en clase).


### ¿Por qué construir su propia Hardware Wallet?



- Ahorre unos 135 dólares frente a la compra de un aparato comercial.
- Consigue comodidad con el flasheo de firmware, elementos seguros e higiene wallet.
- Active dispositivos de firma adicionales para repartir el ahorro entre varios monederos.
- Reduzca el riesgo de la cadena de suministro adquiriendo y montando usted mismo todos los componentes.
- Tenga presente el mantra de Lopp: soberanía y conveniencia siempre están reñidas.


## Configuración física


### Prepare su caso


Tiene dos opciones para alojar su placa LilyGO T-Display: una carcasa impresa en 3D o la carcasa oficial de LilyGO. La carcasa impresa se puede encontrar e imprimir desde [este modelo](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Ofrece una carcasa ligera y personalizable para su dispositivo.


![image](assets/fr/04.webp)


Como alternativa, puede utilizar la funda oficial de LilyGO, que proporciona un ajuste y un acabado ligeramente diferentes, ofreciendo una protección más robusta y un aspecto más pulido.


![image](assets/fr/05.webp)


Tenga en cuenta que las carcasas impresa y oficial difieren ligeramente en diseño y montaje. Sea cual sea la opción que elijas, asegúrate de que la placa esté bien asentada dentro de la carcasa para evitar conexiones sueltas o daños.


### Inspeccionar la Junta


Antes de continuar, inspeccione cuidadosamente su placa LilyGO T-Display para detectar cualquier defecto o suciedad visible. Compruebe que la pantalla, los botones y el puerto USB-C estén limpios y libres de polvo o salpicaduras de soldadura. Manipule la placa con cuidado y tenga en cuenta la seguridad frente a descargas electrostáticas (ESD) conectándose a tierra o utilizando una muñequera ESD para evitar daños en los componentes sensibles.


### Conéctate a tu portátil


Utilizando un cable USB-C apto para datos, conecte la placa LilyGO a su ordenador portátil. Esta conexión le proporcionará alimentación y le permitirá flashear el firmware.


Al arrancar, aparecerá la siguiente pantalla:


![image](assets/fr/06.webp)



Al encenderlo, LilyGO mostrará una pantalla de prueba de colores que irá pasando por colores sólidos. Esto confirma que la pantalla y la placa funcionan correctamente antes de flashear el firmware.


Una vez completada la prueba de color, la pantalla se establecerá en un estado predeterminado, indicando que la placa está lista para los siguientes pasos en el proceso de construcción.


![image](assets/fr/07.webp)


## El camino fácil o el camino Hard


Existen dos métodos principales para flashear el firmware del wallet: el método fácil y el método difícil. La forma fácil utiliza herramientas preconfiguradas o flashers basados en web que cargan automáticamente el firmware en su dispositivo con una entrada mínima. Este método es ideal para principiantes que quieren una victoria rápida o prefieren evitar las complejidades de la depuración y las interacciones de línea de comandos. Simplifica el proceso y te pone en marcha más rápidamente, por lo que es accesible para los nuevos en el desarrollo embebido o carteras de hardware.


Por otro lado, el método difícil implica utilizar manualmente herramientas de línea de comandos para flashear el firmware. Este método requiere verificar las firmas y las sumas de comprobación del firmware para garantizar su autenticidad e integridad, lo que permite comprender mejor el proceso de flasheo y cómo interactúa el firmware con el hardware. Aunque exige más esfuerzo y familiaridad con los comandos de terminal, ofrece mayor control, transparencia y confianza en la seguridad del dispositivo.


Cada método tiene sus ventajas y sus inconvenientes: el método fácil sacrifica cierto grado de confianza y comprensión a cambio de rapidez y comodidad, mientras que el método difícil requiere más tiempo y conocimientos técnicos, pero recompensa con flexibilidad y una mayor comprensión de la tecnología subyacente. Los instructores deben animar a los alumnos a elegir el camino que mejor se adapte a su nivel de comodidad y curiosidad, fomentando tanto la confianza como la exploración.


## El camino más fácil


La forma más fácil de flashear un ESP32



- Ve al Github oficial de Blockstream: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Puedes descargar el archivo fuente y ejecutar el sitio web localmente, pero GitHub ya lo aloja en [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub sirve el HTML, CSS, JavaScript, etc. directamente a tu navegador para que puedas flashear el dispositivo sin instalar herramientas de desarrollador.


![image](assets/fr/09.webp)



- Abre el menú desplegable (probablemente por defecto sea `M5Stack Core2`) y selecciona tu placa de desarrollo - para esta clase, elige `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Cuando pulses flash aparecerá esto. Para saber que dispositivo es el LILYGO, desenchufa el lilygo y vuelve a enchufarlo. El puerto com que el lilygo aparecerá y desaparecerá. Haz click en el puerto COM en el que está enchufado el Jade


![image](assets/fr/11.webp)



- Eso es todo una barra de progreso debe mostrar y cuando haya terminado su listo para configurarlo


## Configuración de Jade Wallet


Una vez que el firmware se ha flasheado correctamente, su LilyGO T-Display es ahora un wallet de hardware de Jade totalmente funcional. Esta sección le guiará a través del proceso de configuración inicial, desde la generación de su frase seed hasta la conexión del dispositivo con el software wallet como Sparrow o la aplicación móvil Blockstream Green.


### Arranque inicial y configuración de dispositivos



- Encienda el dispositivo:** Con el LilyGO todavía conectado a su portátil mediante USB-C, el firmware Jade debería arrancar automáticamente. Verá aparecer el logotipo de Jade en la pantalla.



- Entre en el modo de configuración:** El dispositivo le presentará un menú inicial. Utiliza los dos botones físicos de la placa para navegar:
 - Botón izquierdo:** Subir/bajar
 - Botón derecho:** Mover hacia abajo/adelante
 - Ambos botones simultáneamente:** Seleccionar/confirmar



- Seleccione "Configuración":** Navegue hasta la opción Configuración y pulse ambos botones para confirmar. El dispositivo le guiará a través del proceso de configuración inicial.


### Creación de su Wallet



- Seleccione "Begin Setup":** El dispositivo le pedirá que inicie el proceso de creación de la wallet. Confirme su selección.



- Seleccione "Crear nuevo Wallet":** Se le presentarán dos opciones:
 - Crear nueva Wallet:** Genera una nueva frase seed (elíjala para el taller)
 - Restaurar Wallet:** Recuperar una wallet existente a partir de una frase seed (para usuarios avanzados)



- Seleccione "Crear nuevo Wallet" y confirme.



- Generar entropía:** El dispositivo utilizará su generador de números aleatorios para crear entropía criptográfica. Este proceso tarda unos segundos, ya que el dispositivo recopila aleatoriedad de múltiples fuentes.


### Grabación de la frase semilla



- Escriba su frase seed:** El dispositivo mostrará ahora una frase BIP39 seed de 12 palabras, una palabra cada vez. Este es el paso más crítico de todo el proceso.


**Prácticas de seguridad importantes:**


- Escriba cada palabra claramente en un papel (utilice las tarjetas de frases seed proporcionadas si dispone de ellas)
- Comprueba dos veces cada palabra mientras la escribes
- Nunca fotografíe la frase seed con su teléfono
- Nunca escriba las palabras en cualquier ordenador o teléfono
- Mantén tu frase seed en privado: no compartas tu pantalla ni se la enseñes a nadie



- Verifique su frase seed:** Después de escribir las 12 palabras, el dispositivo le pedirá que confirme varias palabras de la frase para asegurarse de que las ha grabado correctamente. Utilice los botones para seleccionar la palabra correcta para cada pregunta.


**Consejo profesional:** Antes de continuar, practica la lectura de tu frase seed en voz alta (en voz baja, para que no te oigan los demás). Esto te ayudará a detectar errores de escritura o ambigüedades.


### Método de conexión



- Elija el tipo de conexión:** El firmware Jade admite dos métodos de conexión:
 - USB:** Conexión por cable mediante cable USB-C (recomendado para este taller)
 - Bluetooth:** Conexión inalámbrica a dispositivos móviles



- Seleccione **USB** por ahora, ya que es la opción más sencilla para el software wallet de escritorio y no introduce vectores de ataque inalámbricos.



- Nomenclatura del dispositivo:** El Jade mostrará un identificador único como "Connect Jade A7D924". Este identificador le ayuda a distinguir entre varias carteras de hardware si termina construyendo más de una. Anote este identificador si lo desea.


### Conexión al software Wallet


Ahora tiene dos opciones principales para interactuar con su recién creado hardware wallet: la aplicación móvil Blockstream Green (para uso sobre la marcha) o Sparrow Wallet (para uso de escritorio con funciones más avanzadas). Para este taller, nos centraremos en Sparrow Wallet, ya que ofrece una mejor visibilidad de los detalles técnicos de las transacciones Bitcoin.


#### Opción 1: Aplicación móvil Blockstream Green (Inicio rápido)


Si quieres probar tu dispositivo rápidamente con un dispositivo móvil:



- Descargue la aplicación **Blockstream Green** de App Store (iOS) o Google Play (Android)
- Abre la aplicación y selecciona "Conectar Hardware Wallet"
- Elige "Jade" en la lista de dispositivos compatibles
- Conecta tu Jade a tu teléfono utilizando un cable USB-C a USB-C (o un adaptador USB-C a Lightning para iPhone 15+)
- Siga las instrucciones en pantalla para conectarse y crear su primer wallet


**Nota sobre Liquid:** La aplicación Blockstream Green es compatible tanto con Bitcoin como con Liquid (una cadena lateral de Bitcoin). Si utiliza las funciones de Liquid, es posible que se le pida que "exporte la clave maestra de cegamiento", que permite a la aplicación ver los importes de las transacciones en la red de Liquid, que de otro modo son confidenciales. Para este taller, puede omitir las funciones de Liquid y centrarse en las transacciones estándar de Bitcoin.


#### Opción 2: Sparrow Wallet (Recomendado para taller)


Sparrow Wallet es una potente aplicación de escritorio que le proporciona un control granular sobre sus transacciones Bitcoin y se conecta sin problemas con su hardware Jade wallet.


**Instalación:**



- Descargue Sparrow Wallet desde el sitio web oficial: [sparrowwallet.com](https://sparrowwallet.com)
- Verifique la firma de la descarga (consulte la documentación de Sparrow para más detalles)
- Instalar e iniciar la aplicación


**Conectando tu Jade a Sparrow:**



- En Sparrow, vaya a **Archivo → Nuevo Wallet**
- Dale un nombre a tu wallet (por ejemplo, "Mi Wallet de Jade")
- Haga clic en **Conectado Hardware Wallet**
- Sparrow debería detectar automáticamente su dispositivo Jade conectado
- Si se le solicita, confirme la conexión en la pantalla Jade pulsando ambos botones
- Seleccione el tipo de guión que desee:
 - Segwit nativo (P2WPKH):** Recomendado para principiantes: las comisiones más bajas y la mayor compatibilidad con los monederos modernos
 - Segwit anidado (P2SH-P2WPKH):** Para compatibilidad con servicios antiguos
 - Taproot (P2TR):** La más avanzada, ofrece la mejor privacidad y las tarifas más bajas, pero requiere soporte de vanguardia wallet
- Haga clic en **Importar almacén de claves** para completar la conexión


**Configurar la conexión al servidor de Sparrow:**


Antes de que pueda ver su saldo o transmitir transacciones, Sparrow necesita conectarse a un nodo Bitcoin para obtener datos de la cadena de bloques. Tienes varias opciones, cada una con distintas compensaciones entre comodidad, privacidad y confianza:



- Electrum Server pública (Más fácil, menos privada):** Se conecta a un servidor público operado por terceros. Rápido de configurar, pero el servidor puede ver las direcciones de tu wallet y potencialmente vincularlas a tu dirección IP. Bueno para pruebas en testnet.
 - En Sparrow, vaya a **Herramientas → Preferencias → Servidor**
 - Seleccione **Servidor público** y elija un servidor de la lista
 - Haga clic en **Probar conexión** para verificar



- Bitcoin Core o Knots Node (Más privado, más trabajo):** Ejecuta tu propio nodo Bitcoin completo. Este es el estándar de oro para la privacidad y la verificación, ya que valida cada transacción usted mismo y no confía en el servidor de nadie más. Sin embargo, requiere descargar toda la cadena de bloques (~600GB) y mantener tu nodo sincronizado.
 - Instalar y sincronizar el núcleo o los nudos Bitcoin
 - En Sparrow, vaya a **Herramientas → Preferencias → Servidor**
 - Seleccione **Bitcoin Core o Nudos** e introduzca los datos de conexión de su nodo



- Electrum Server Privado (Buen equilibrio):** Aloja tu propio servidor Electrum (como Fulcrum o Electrs) conectado a tu nodo Bitcoin Core o Knots. Ofrece total privacidad sin necesidad de ejecutar Sparrow en la misma máquina que su nodo.
 - Configure un servidor Electrum que apunte a su nodo Bitcoin Core o Knots
 - En Sparrow, vaya a **Herramientas → Preferencias → Servidor**
 - Seleccione **Private Electrum** e introduzca la URL de su servidor


Para este taller, el uso de una **Electrum Server pública** está perfectamente bien para las transacciones de la red de pruebas. En un entorno de producción con fondos reales, deberías considerar ejecutar tu propio nodo o utilizar un servidor privado de confianza para obtener la máxima privacidad.


#### Opción 3: Blockstream Green Desktop App (Inicio rápido)


Blockstream Green es el software para terminar de configurar el JadeDIY y debe ser con la versión de escritorio



- Consigue la aplicación oficial de Blockstream - este es el enlace a ella desde su página web. Cuando estés allí, haz clic en [Descargar ahora](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Dependiendo de dónde vayan tus descargas, lo más probable es que el archivo esté en tu carpeta de Descargas. Compruébelo y haga doble clic en el archivo ejecutable para instalar el software.


![image](assets/fr/13.webp)



- Es posible que tenga que dar derechos de administrador para ejecutar el instalador. Una vez que lo hagas, aparecerá una ventana parecida a la siguiente imagen: haz clic en **Siguiente**.


![image](assets/fr/14.webp)



- Elija dónde desea que resida la aplicación instalada (en una ubicación junto a sus otros programas o en algún lugar fácil de encontrar) y, a continuación, haga clic en **Siguiente**.


![image](assets/fr/15.webp)



- El instalador le pedirá un nombre para el acceso directo. Introduzca uno o mantenga el predeterminado y haga clic en **Siguiente**.


![image](assets/fr/16.webp)



- Si desea un acceso directo en el escritorio, marque la casilla; de lo contrario, haga clic en **Siguiente**.


![image](assets/fr/17.webp)



- Por último, haga clic en **Instalar** y espere unos minutos a que finalice la instalación.


![image](assets/fr/18.webp)



- La barra de progreso debe llenarse hasta el final.


![image](assets/fr/19.webp)



- Cuando termine, aparecerá una nueva página - haga clic en **Finalizar**.


![image](assets/fr/20.webp)



- Busca tu aplicación Blockstream recién instalada (ejemplo mostrado en el menú Inicio de Windows 11).


![image](assets/fr/21.webp)



- Cuando lo encuentres, haz clic para iniciarlo: debería aparecer una pantalla de bienvenida.


### Verificación de la configuración


Una vez conectado a Sparrow (u otra aplicación wallet):



- Verifique sus direcciones:** Sparrow mostrará las direcciones de recepción derivadas de su frase seed. Puede verificar una dirección en su dispositivo Jade yendo a la pestaña "Recibir" en Sparrow y haciendo clic en "Mostrar Address"-la dirección debería aparecer tanto en la pantalla de su ordenador como en la pantalla de Jade.



- Genere una dirección de recepción:** Haga clic en la pestaña **Recibir** de Sparrow y copie su primera dirección de recepción de Bitcoin.



- Listo para transacciones:** Su hardware wallet está ahora completamente configurado y listo para recibir y firmar transacciones Bitcoin. Continúe con la siguiente sección para practicar la firma de una transacción testnet.



---

### Lista de comprobación rápida



- El firmware Jade arranca correctamente
- Nueva wallet creada con la frase seed de 12 palabras
- Frase semilla escrita claramente y verificada
- Modo de conexión USB seleccionado
- Software Wallet (Sparrow) instalado y conectado
- Conexión servidor configurada (Electrum pública para mainnet)
- Primera dirección de recepción generada y verificada en el dispositivo



---

**Licencia MIT**


**Copyright (c) 2025 The Bitcoin Network NYC**


Por la presente se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), para comerciar con el Software sin restricciones, incluyendo sin limitación los derechos de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de copias del Software, y para permitir a las personas a las que se proporcione el Software que lo hagan, sujeto a las siguientes condiciones:


El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.


EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUIDAS, ENTRE OTRAS, LAS GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN FIN DETERMINADO Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O LOS TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN CONTRACTUAL, EXTRACONTRACTUAL O DE OTRO TIPO, QUE SURJA DE, O ESTÉ RELACIONADA CON EL SOFTWARE O EL USO U OTRAS OPERACIONES CON EL SOFTWARE.


---
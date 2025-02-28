---
name: Construir con elementos y red líquida
goal: Aprenda a utilizar y desarrollar con la plataforma blockchain de código abierto Elements y sus características clave
objectives: 

  - Comprender los conceptos básicos de la plataforma de cadena de bloques Elements y las cadenas laterales Liquid.
  - Aprenda a configurar y ejecutar nodos Elements para configuraciones independientes y de cadena lateral.
  - Adquiera experiencia práctica con la firma federada de bloques y el Federated 2-Way Peg.
  - Configure y gestione entornos de cadena de bloques seguros y eficientes para casos de uso del mundo real.

---
# Construir sobre líquido y elementos

Descubra las funciones y capacidades avanzadas de Liquid y Elements, y aprenda a utilizar eficazmente estas herramientas para mejorar sus proyectos de desarrollo. Esta formación proporciona una base teórica y práctica completa que le permitirá dominar funciones como las transacciones confidenciales, los activos emitidos y la firma en bloque federada.

Liquid, basado en el marco Elements, está diseñado para mejorar la privacidad, la escalabilidad y la funcionalidad de las soluciones financieras y técnicas. En este curso, obtendrá experiencia práctica con la emisión y gestión de activos, la Federated 2-Way Peg y el uso de herramientas como elementsd y elements-cli, lo que le permitirá crear soluciones innovadoras adaptadas a sus necesidades.

Este curso está adaptado a desarrolladores de todos los niveles de experiencia. Los usuarios principiantes e intermedios encontrarán explicaciones accesibles y ejemplos prácticos, mientras que los usuarios avanzados podrán profundizar en los detalles técnicos y las funciones menos conocidas de Liquid y Elements.

Únase a nosotros para elevar sus habilidades, desbloquear todo el potencial de Liquid y Elements, y crear herramientas impactantes para el futuro de la innovación de Liquid.

+++
# Introducción

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Cursos Introducción

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

El objetivo de la Academia Elements es presentar y explicar los conceptos clave de Elements, la plataforma de código abierto en la que se basa Liquid. Al final del curso, usted deberá tener una buena comprensión de las principales características de Elements, tales como Transacciones Confidenciales y Activos Emitidos, y los procesos involucrados en el funcionamiento de Elements Core.

Cada sección tendrá lecciones con texto explicativo y un vídeo que termina con un cuestionario. El número de preguntas está relacionado con la extensión del tema anterior. La sección 10 resumirá el contenido del curso y terminará con un cuestionario más amplio.

Cualquier pregunta, solicitud de información adicional o duda sobre las respuestas del cuestionario puede dirigirse a su profesor James Dorfman.

## Visión general de los elementos

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements es una plataforma de blockchain de código abierto con capacidad para sidechain, que proporciona acceso a potentes funciones desarrolladas por miembros de la comunidad, como Transacciones Confidenciales y Activos Emitidos.

Elements es, en esencia, un protocolo que permite llegar a un consenso en torno al historial de transacciones y las normas que rigen la transferencia y creación de activos almacenados en un libro mayor distribuido de blockchain.

Encontrará más información sobre Elements en el sitio web del proyecto (https://elementsproject.org/), el blog oficial de Liquid (https://blog.liquid.net/) y el portal para desarrolladores (https://liquid.net/devs).

### Elementos

Lanzado en 2015, Elements reduce los costes internos de desarrollo e investigación y aprovecha la tecnología blockchain más avanzada, abriendo muchos nuevos casos de uso para su implementación. Una cadena de bloques basada en Elements puede funcionar como una cadena de bloques independiente o vincularse a otra y funcionar como una cadena lateral. Ejecutar Elements como Sidechain permite transferir activos de forma verificable entre diferentes blockchains.

Construido sobre el código base de Bitcoin y ampliándolo, permite a los desarrolladores familiarizados con la API de Bitcoin crear blockchains funcionales y probar proyectos de prueba de concepto de forma rápida y rentable. Al estar construido sobre la base de código de Bitcoin, Elements también puede funcionar como banco de pruebas para cambios en el propio protocolo Bitcoin.

A continuación se enumeran algunas de las principales características de Elements.

#### Transacciones confidenciales

Por defecto, todas las direcciones en Elements están cegadas utilizando Transacciones Confidenciales. El cegado es el proceso por el cual la cantidad y el tipo de activo que se transfiere se oculta criptográficamente a todo el mundo, excepto a los participantes y a aquellos a los que decidan revelar la clave de cegado.

#### Activos emitidos

Los Activos Emitidos en Elementos permiten emitir y transferir múltiples tipos de activos entre los participantes de la red. Un Activo Emitido también se beneficia de las Transacciones Confidenciales y puede ser reemitido o destruido por cualquiera que posea el token de reemisión correspondiente.

#### Clavija federada de 2 vías

Elements es una plataforma de cadena de bloques de uso general que también puede "vincularse" a una cadena de bloques existente (como Bitcoin) para permitir la transferencia bidireccional de activos de una cadena a otra. Implementar Elements como una cadena lateral permite eludir algunas de las propiedades inherentes a la cadena principal, al tiempo que se conserva un buen grado de la seguridad proporcionada por los activos asegurados en la cadena principal.

#### Bloques firmados

Elements utiliza una Federación Fuerte de firmantes, llamados Firmantes de Bloques, que firman y crean bloques de forma fiable y puntual. Esto elimina la latencia de transacción del proceso de minería PoW, que está sujeta a una gran variación en el tiempo de bloque debido a su distribución poisson aleatoria. El proceso Federated Block Signing consigue una creación de bloques fiable sin introducir la necesidad de la confianza de terceros o la minería basada en "algoritmos" computacionales.

Elements añade todas estas características sobre la base de código de Bitcoin Core, ampliando la capacidad del protocolo mainchain y permitiendo nuevos casos de uso empresarial cuando se despliega como sidechain o como solución blockchain independiente.

# Elemento

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Cómo funcionan los elementos

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements ofrece una solución técnica a los problemas a los que se enfrentan a diario los usuarios de blockchain: latencia de las transacciones, falta de privacidad y riesgo de fungibilidad.

Elements supera estos problemas mediante el uso de la Firma en Bloque Federada y las Transacciones Confidenciales.

A diferencia de la red Bitcoin, el proceso de firma de bloques en Elements no depende de las firmas multiparte de membresía dinámica (DMMS) ni de la prueba de trabajo (PoW). En su lugar, Elements utiliza una Federación Fuerte de firmantes, llamados Firmantes de Bloques, que pueden firmar y crear bloques de forma fiable y oportuna. Esto elimina la latencia de transacción del proceso de minería PoW, que está sujeto a una gran varianza de tiempo de bloque debido a su distribución poisson aleatoria. El proceso Federated Block Signing consigue una creación de bloques fiable sin introducir la necesidad de la confianza de terceros.

Los elementos pueden funcionar como una cadena lateral de otra cadena de bloques, como Bitcoin, o como una cadena de bloques independiente sin depender de otras redes.

Cuando se utiliza como sidechain, la Strong Federation también contiene miembros que permiten la transferencia segura y controlada de activos entre una cadena principal y una sidechain de Elements. La transferencia controlada de activos se denomina Federated 2-Way Peg y los miembros que desempeñan la función de transferencia de activos se llaman Watchmen.

Los procesos que intervienen en el funcionamiento de una red Elements y las funciones de los participantes en la red son importantes para entender cómo funciona Elements.

Tanto si se implementa como sidechain o como blockchain independiente, Elements hace uso de Federaciones Fuertes de Firmantes de Bloques para producir bloques.

### Federaciones fuertes

Elements utiliza un modelo de consenso propuesto por primera vez por Blockstream, denominado Federaciones Fuertes. Una Federación Sólida no necesita Prueba de Trabajo (PoW) y en su lugar se basa en las acciones colectivas de un grupo de participantes que desconfían mutuamente, llamados Funcionarios.

Los papeles que puede desempeñar un Funcionario dentro de una Federación Fuerte son: Firmantes de Bloques y Vigilantes. Los firmantes de bloques son necesarios si ejecutas Elements en modo de cadena de bloques lateral o independiente, mientras que los vigilantes solo son necesarios en una configuración de cadena lateral.

Las acciones que puede realizar un miembro de una federación sólida se dividen en dos funciones distintas para mejorar la seguridad y limitar los daños que puede causar un atacante.

Cuando se combinan, las funciones de estos participantes permiten a Elements ofrecer tanto una rápida creación de bloques (confirmación más rápida y definitiva de las transacciones) como activos seguros y transferibles (activos vinculados directamente a otra blockchain).

Puede leer el informe sobre Federaciones Fuertes aquí: https://blockstream.com/strong-federations.pdf

### Bloquear firmantes

Una cadena de bloques como la de Bitcoin se amplía cuando cualquiera que forme parte de un grupo dinámico de firmantes de bloques amplía la cadena demostrando el trabajo realizado. La naturaleza dinámica del conjunto introduce los problemas de latencia inherentes a estos sistemas.

Mediante el uso de un conjunto fijo de firmantes, un modelo federado sustituye el conjunto dinámico por un conjunto conocido, un esquema multi-firma. La reducción del número de participantes necesarios para ampliar la blockchain aumenta la velocidad y escalabilidad del sistema, mientras que la validación por todas las partes garantiza la integridad del historial de transacciones.

La firma federada de bloques consta de varias fases:


- Paso 1 - Los firmantes de bloques proponen bloques candidatos a todos los demás firmantes de bloques participantes.
- Paso 2 - Cada firmante de bloques señala su intención comprometiéndose previamente a firmar el bloque candidato dado.
- Paso 3 - Si se alcanza el umbral dado para el precompromiso, cada firmante del bloque firma el bloque.
- Paso 4 - Si se alcanza el umbral de firma (que puede ser diferente al del paso 3), el bloque se acepta y se envía a la red. La Strong Federation ha alcanzado un consenso sobre el último bloque de transacciones.
- Paso 5 - El siguiente bloque es propuesto por el siguiente firmante en la ronda y el proceso se repite.

Dado que la generación de bloques de una federación sólida no es probabilística y se basa en un conjunto fijo de firmantes, nunca estará sujeta a reorganizaciones multibloque. Esto permite reducir significativamente el tiempo de espera asociado a la confirmación de transacciones. También elimina el incentivo de minar para obtener beneficios (es decir, las recompensas por bloque) y lo sustituye por un incentivo para participar de forma productiva en una red en la que todos los participantes tienen el mismo objetivo compartido: garantizar que la red siga funcionando de forma beneficiosa para todos. Y lo hace sin introducir un único punto de fallo ni mayores requisitos de confianza.

### Elementos como cadena lateral - Watchmen y la clavija bidireccional federada

Cuando se ejecuta como una cadena lateral, algunos miembros de la Strong Federation tienen un papel adicional que desempeñar, el de Vigilantes. Los Vigilantes son responsables de la transferencia de activos dentro y fuera de una cadena lateral de Elementos, procesos conocidos como `Peg-In` y `Peg-Out`.

Para que una cadena lateral funcione de forma fiable, debe permitir a los participantes verificar que el suministro de activos está controlado y es verificable. Una sidechain de Elements utiliza un 2-Way Federated Peg para permitir la transferencia bidireccional de activos dentro y fuera de una blockchain de Elements. Esto satisface los requisitos de emisión comprobable y transferencias entre cadenas.

La función Federated 2-way Peg permite que un activo sea interoperable con otros blockchains y representativo del activo nativo de otro blockchain. Al vincular su cadena de bloques a otra, puede ampliar las capacidades de la cadena principal y superar algunas de sus limitaciones inherentes.

A alto nivel, las transferencias a la cadena lateral se producen cuando alguien envía activos de la cadena principal a una dirección controlada por un monedero Watchmen multifirma. Esto congela los activos en la cadena principal. Watchmen valida entonces la transacción y libera la misma cantidad del activo asociado dentro de la cadena lateral. Los activos liberados se envían a un monedero de la cadena lateral que pueda demostrar que reclama los activos originales de la cadena principal. Este proceso traslada los activos de la cadena principal a la cadena lateral.

Para transferir activos de vuelta a la cadena principal, el usuario realiza una transacción especial en la cadena lateral. Esta transacción es comprobada por los Watchmen, que a continuación firman un gasto de transacción desde la cartera multifirma que controlan en la cadena principal. Para que la transacción de la cadena principal sea válida, debe firmar un número mínimo de participantes de la federación. Cuando los Vigilantes envían un activo de vuelta a la cadena principal, también destruyen la cantidad correspondiente en la cadena lateral, transfiriendo de hecho los activos entre cadenas de bloques.

## Configuración y funcionamiento de los elementos

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Dado que Elements se basa en el código base de Bitcoin, los componentes que conforman una red operativa son muy similares.

El propio software del nodo Elements se llama `elementsd` y se ejecuta como un demonio en la máquina de un usuario. Un demonio (o servicio en Windows) es un programa que se ejecuta como un servicio en segundo plano sin requerir el control directo de un usuario conectado.

Nota: A lo largo de este documento, siempre nos referiremos a elementsd como la versión daemon, pero todo podría hacerse con elements-qt, siempre que la opción de servidor esté activada.

El demonio Elements se conecta a otros nodos de la red para intercambiar datos de transacciones y bloques, validando y ampliando su copia local de la cadena de bloques de la red.

El software Elements también consta de un programa cliente llamado `elements-cli` que permite enviar comandos de llamada a procedimiento remoto (RPC) a elementsd desde la línea de comandos. Esto puede utilizarse, por ejemplo, para consultar el saldo de un monedero, ver datos de transacciones o bloques o transmitir una transacción. Esta configuración debería ser familiar para cualquiera que haya utilizado los equivalentes de Bitcoin; bitcoind y bitcoin-cli.

Como un nodo Elements puede configurarse pasando parámetros al inicio o a través de un archivo de configuración, es posible tener más de una instancia ejecutándose en la misma máquina. Esto es útil para pruebas y desarrollo, ya que puedes configurar tu propia red local en una sola máquina, con cada nodo de Elements teniendo su propia copia de los datos de la cadena de bloques, gestionando su propio grupo de transacciones válidas no confirmadas y escuchando peticiones RPC en diferentes puertos.

### Comunidad y repositorio de código de Elements

Elements es un proyecto de código abierto y su código fuente puede encontrarse en el repositorio GitHub de Elements en https://github.com/ElementsProject/elements. El repositorio contiene el código fuente de los programas elementsd y elements-cli, así como herramientas de instalación y compilación, un conjunto de pruebas y documentación didáctica.

Para complementar el repositorio de código, existe también el sitio web https://elementsproject.org, un recurso centrado en la comunidad que contiene explicaciones sobre qué es Elements, cómo funciona y una completa sección de tutoriales. El tutorial se centra en el aprendizaje de Elements siguiendo ejemplos de línea de comandos y muestra cómo crear aplicaciones web y de escritorio sencillas sobre él. El sitio también incluye foros de debate populares de la comunidad de Elements y está alojado en GitHub, lo que permite que la comunidad contribuya al contenido del sitio.

Para ejecutar Elements en su máquina, primero tendrá que clonar (descargar una copia) el código fuente, instalar las dependencias que tenga el código y, por último, compilar los ejecutables demonio y cliente. El software Elements estará listo para ser configurado y ejecutado.

## Configuración de nodos y redes

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Los ajustes de configuración pueden pasarse a un nodo Elements al iniciarse para cambiar la forma en que se ejecuta, valida los datos, se conecta a otros nodos e inicializa sus datos de blockchain.

Los ajustes se cargan desde el archivo designado `elements.conf` o se pasan como parámetros a través de la línea de comandos.

Algunas de las cosas se pueden cambiar utilizando estos parámetros:


- El nombre del activo por defecto utilizado en las implementaciones de blockchain independientes.
- El número del activo inicial creado.
- El activo que se utilizará para pagar las comisiones de transacción en la red.
- La ubicación de almacenamiento de los archivos de datos de la cadena de bloques.
- Las credenciales RPC utilizadas para conectarse a un nodo Bitcoin.
- El umbral `n de m` que debe cumplirse y las claves públicas válidas que pueden firmar bloques.
- El script que necesita satisfacerse para transferir activos dentro y fuera de una cadena lateral.
- Si conectarse a un nodo Bitcoin como sidechain o no.

Muchos de ellos forman parte de las reglas de consenso de la red, por lo que es importante que se apliquen en todos los nodos al iniciarse. Algunas pueden cambiarse después de inicializar una cadena, pero otras deben fijarse después de utilizarlas para inicializar una cadena.

El uso de parámetros se tratará más adelante en el curso a medida que se relacionen con cada sección.

### Operaciones básicas con la línea de comandos

Este curso mostrará ejemplos que utilizan el programa `elements-cli` para realizar llamadas RPC a uno o más nodos Elements. Esto se hace desde una sesión de terminal y para hacer los comandos más breves se utilizará un `alias`. Por esta convención cuando veas algo como los siguientes comandos:

```bash
e1-dae
e1-cli getnewaddress
```

Los `e1-dae` y `e1-cli` son en realidad un atajo tipográfico que hace uso de la función `alias` de la terminal. Los `e1-dae` y `e1-cli` serán sustituidos cuando se ejecute el comando y el comando que se ejecutará será similar a:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Lo que vemos arriba es una llamada para iniciar el demonio Elements y una llamada a los programas elements-cli ubicados en el directorio `$HOME/elements/src` y un valor para el parámetro `datadir`. El parámetro `datadir` nos permite indicar a las instancias demonio y cliente dónde ubicar sus archivos de configuración y, en el caso del demonio, dónde almacenar su copia de la cadena de bloques. Como comparten un archivo de configuración, el cliente podrá hacer llamadas RPC al demonio.

Ejecutando el comando anterior de nuevo, pero con un valor diferente de `datadir`, podemos iniciar más de una instancia de Elements, cada una con su propia copia de la cadena de bloques y configuración. Por esta convención usaremos los alias `e2-dae` y `e2-cli` en el curso para referirnos a un directorio datadir diferente al de e1. Así que el ejemplo anterior para nuestra segunda instancia `e2` sería:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

Esto nos permitirá realizar todo tipo de operaciones como la transacción de activos entre nodos, la emisión de activos y la comprobación del uso del cegamiento en Transacciones Confidenciales entre diferentes nodos de la misma red.

# Uso del elemento Caso práctico

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Transacciones confidenciales

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

En esta sección aprenderá a utilizar la función Transacciones Confidenciales de Elementos.

Todas las direcciones de Elements están, por defecto, cegadas mediante Transacciones Confidenciales, que mantienen la cantidad y el tipo de activos transferidos visibles sólo para los participantes en la transacción (y aquellos a los que decidan revelar la clave de cegado), al tiempo que garantizan criptográficamente que no se pueden gastar más monedas de las disponibles.

### Direcciones confidenciales y transacciones confidenciales

Por defecto, cuando se crea una nueva dirección en Elements mediante el comando `getnewaddress` se crea como dirección confidencial.

Para demostrar las transacciones confidenciales, haremos que e2 se envíe a sí mismo algunos fondos y luego intente ver la transacción desde e1. Esto demostrará la naturaleza confidencial de las transacciones en Elements.

Cada nueva dirección generada por un nodo Elements es confidencial por defecto. Podemos demostrarlo haciendo que e2 genere una nueva dirección.

```
e2-cli getnewaddress
```

Observe que la dirección empieza por e1. Esto la identifica como una dirección confidencial. Examinar la dirección con más detalle utilizando el comando getaddressinfo muestra más detalles de la dirección.

```
e2-cli getaddressinfo <address>
```

Puedes ver que hay una propiedad confidential_key que nos indica que es una dirección confidencial.

La clave_confidencial es la clave cegadora pública, que se añade a la propia dirección confidencial. Esta es la razón por la que una dirección confidencial es tan larga.

También tiene asociada una dirección no confidencial. Si desea utilizar transacciones normales, no confidenciales, dentro de Elements, los activos deben enviarse a esta dirección en lugar de a la que tiene el prefijo lq1.

Ahora podemos hacer que e2 envíe algunos fondos a la dirección que generó. Esto demostrará posteriormente que e1, al no ser una de las partes de la transacción, no podrá ver los detalles de la misma.

```
e2-cli sendtoaddress <address>
```

Anote el ID de la transacción. Confirme la transacción.

```
e2-cli -generate 101
```

Observando la transacción en la que e2 se envió algunos fondos a sí misma desde la perspectiva de la propia e2.

```
e2-cli gettransaction <txid>
```

Al desplazarse hacia arriba por los detalles de la transacción, puede ver que e2 puede ver los importes enviados y recibidos, así como el activo transaccionado. También puede ver las propiedades amountblinder y assetblinder, que se utilizan para ocultar los detalles de otros nodos que no participan en la transacción.

Para comprobar los detalles de la misma transacción desde e1, primero necesitamos obtener los detalles de la transacción sin procesar.

```
e1-cli getrawtransaction <txid>
```

Que devuelve los detalles de la transacción en bruto. Si miras dentro de la sección vout puedes ver que hay tres instancias. Las dos primeras instancias son los importes de recepción y cambio, y la tercera es la comisión de la transacción. De estos tres importes, la comisión es el único en el que se puede ver un valor, ya que la comisión en sí siempre está sin ocultar dentro de Elements.

### Claves cegadoras

Lo que muestran las dos primeras secciones de vout son "rangos ciegos" de los importes de valor y los datos de compromiso que actúan como prueba del importe real y el tipo de activo transaccionado.

Incluso si importáramos la clave privada de e2 en el monedero de e1, éste seguiría sin poder ver las cantidades y el tipo de activo transaccionado porque todavía no tiene conocimiento de la clave cegadora utilizada por e2. Demostraremos esto importando la clave privada utilizada por el monedero de e2 al de e1. Primero tenemos que exportar la clave de e2

```
e2-cli dumpprivkey <address>
```

A continuación, impórtalo en e1.

```
e1-cli importprivkey <privkey>
```

Ahora podemos demostrar que e1 todavía no puede ver los valores.

```
e1-cli gettransaction <txid>
```

Efectivamente, muestra 0 como cantidad de tx cuando en realidad era 1.

Para poder ver el valor real sin cegar, necesitamos la clave de cegado. Para ello, primero exportamos la clave de cegado de e2.

```
e2-cli dumpblindingkey <address>
```

A continuación, impórtalo en e1.

```
e1-cli importblindingkey <address> <blinding key>
```

Ahora cuando obtengamos los detalles de la transacción de e1.

```
e1-cli gettransaction <txid>
```

Muestra que con la clave cegadora importada, ahora podemos ver el valor real de 1 dentro de la transacción.

En esta sección hemos visto que el uso de una clave cegadora oculta la cantidad y el tipo de activos en una transacción, y que importando la clave cegadora correcta, podemos revelar esos valores. En la práctica, una clave de ocultación puede, por ejemplo, entregarse a un auditor, en caso de que sea necesario verificar las cantidades y los tipos de activos que posee una parte. La función de transacciones confidenciales de Elements también permite realizar "pruebas de rango". Las pruebas de rango pueden demostrar que una cantidad de un activo se mantiene dentro de un rango determinado, sin necesidad de exponer la cantidad real en sí.

También hemos visto que las Transacciones Confidenciales son opcionales, pero se activan por defecto cuando se genera una nueva dirección.

Eso es todo por esta lección; ¡buena suerte en el examen y hasta la próxima!

## Activos emitidos

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

En esta sección aprenderá a utilizar la función Activos emitidos de Elementos.

Los activos emitidos permiten emitir y transferir múltiples tipos de activos entre los participantes de la red Elements. Cualquier nodo de la red puede emitir sus propios activos. Las emisiones pueden representar la propiedad fungible de cualquier activo, incluyendo vales, cupones, monedas, depósitos, bonos, acciones, etc. Issued Assets abre la puerta a la construcción de intercambios sin confianza, opciones y otros contratos inteligentes avanzados que implican activos autoemitidos.

Un Activo Emitido también se beneficia de las Transacciones Confidenciales y puede ser reemitido por cualquiera que posea el token asociado.

El primer paso es que necesitaremos acceso a dos nodos Elements, que llamaremos e1 y e2. Los nodos han tenido sus blockchains reiniciados y el activo por defecto dividido entre ellos.

Los dos nodos se encuentran en la misma red local y están conectados entre sí, por lo que comparten las mismas transacciones en su mempool de transacciones y blockchains idénticos. Aunque se ejecutan en la misma máquina, cabe señalar que no comparten los mismos archivos de cadena de bloques. Cada nodo gestiona su propia copia local del blockchain, que contiene el mismo historial de transacciones porque están en consenso y se adhieren a las mismas reglas de protocolo que los demás.

Empecemos por comprobar la opinión de cada nodo sobre las emisiones de activos existentes en la red.

Para ello se utiliza el comando listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Como puede ver, ambos nodos muestran el mismo historial de emisiones. Ambos muestran un activo, la emisión inicial de 21 millones de Bitcoin que fueron creados en la inicialización de la cadena. Puedes ver el id hexadecimal del activo en los resultados de ejecutar el comando anterior y también la etiqueta asignada al activo, que es 'bitcoin'.

Vale la pena señalar que el activo por defecto siempre recibe una etiqueta cuando se inicializa la cadena. Cuando usted emite sus propios activos, puede establecer etiquetas para ellos, lo que haremos en breve. Antes de que podamos hacer eso, tenemos que emitir nuestro propio activo.

Haremos que e1 emita el nuevo activo. Esto se hace utilizando el comando issueasset.

```
e1-cli issueasset 100 1 false
```

`issueasset` acepta 3 parámetros.

La cantidad del nuevo activo a emitir, hemos utilizado 100. La cantidad de tokens a crear (los tokens se utilizan para reemitir cantidades de un activo), de los cuales hemos elegido 1. El último parámetro indica a Elements que cree la emisión de activos como ciega o no ciega. Usaremos unblinded ya que queremos ver las cantidades de emisión desde e2 en un minuto, así que introduciremos false.

La ejecución del comando devuelve datos sobre la emisión. Entre ellos se incluyen el identificador de transacción, del que puedes hacer una copia para su uso posterior, el valor hexadecimal único del activo y el valor hexadecimal único del token del activo.

Generar un bloque para confirmar la transacción de emisión.

```
e1-cli -generate 1
```

Ejecute de nuevo el comando `listissuances` contra e1.

```
e1-cli listissuances
```

Eso nos muestra que e1 es ahora consciente de 2 emisiones, la emisión inicial de Bitcoin y nuestro nuevo activo emitido, del cual podemos ver 100. Obsérvese el valor hexadecimal del nuevo activo y que no hay ninguna etiqueta de activo asociada, como sí la hay para la emisión de bitcoin.

Compruebe de nuevo la lista de emisiones conocidas de e2.

```
e2-cli listissuances
```

Eso nos muestra que e2 no está al tanto de la emisión de activos que hizo e1. Sólo puede ver la emisión inicial de bitcoin que ya podía ver.

Esto se debe a que e2 desconoce, y no está vigilando, la dirección a la que se envió el nuevo activo cuando fue emitido por e1.

Cabe señalar que aunque e2 no pueda ver la emisión en sí, e1 podría enviar a e2 parte del activo. El nuevo activo aparecería entonces como saldo disponible en el monedero de e2, aunque no tenga conocimiento de la emisión original.

Para que e2 pueda ver la emisión real (y, por tanto, el importe emitido), tenemos que añadir la dirección a e2 como dirección vigilada.

Para ello necesitamos averiguar la dirección a la que se envió el activo. Para ello, utilizaremos el identificador de transacción que copiamos anteriormente y haremos que e1 recupere los detalles de esa transacción para que podamos averiguar la dirección correcta para añadirla a la lista de vigilancia de carteras de e2.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Desplazándose hacia arriba más allá del hexágono de los datos de la transacción verá la dirección que recibió 100 de nuestro nuevo activo, identificada por su valor hexadecimal.

Coge la dirección y cópiala para poder importarla a e2.

Ahora vamos a importar esa dirección a e2. Para ello utilizamos el comando importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Si ahora comprobamos la lista de emisiones de e2.

```
e2-cli listissuances
```

Puede ver que nuestro activo recién emitido está ahora incluido en la lista. El nodo e2 también es capaz de determinar el importe del activo que se emitió, junto con el importe del token asociado, ya que la emisión fue una emisión no oculta. Para habilitar el uso de la asignación de ID de activo a nombre dentro de Elementos, primero detenga Elementos.

```
e1-cli stop
```

A continuación, reinícielo con un parámetro adicional que asigne el hexágono de un activo a la etiqueta proporcionada. Esto permite que el nodo nos muestre datos sobre el activo en un formato más legible para los humanos. Puedes añadir esto al final de elements.conf si lo prefieres, entonces no necesitarás añadir el argumento al demonio cada vez que lo inicies. Por ejemplo:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Pero aquí utilizaremos el método de los argumentos.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Volviendo a consultar el nodo para obtener una lista de emisiones.

```
e1-cli listissuances
```

Eso nos muestra que el mapeo del valor hexadecimal del activo a su etiqueta está funcionando. Comprobando de nuevo la lista de emisiones del nodo e2.

```
e2-cli listissuances
```

Puede ver que el nodo e2 no tiene acceso a esta etiqueta, porque las etiquetas sólo están disponibles para el nodo que las estableció. De hecho, podemos asignar una etiqueta diferente al mismo hexágono de activo en e2 de lo que hicimos en e1. Primero detenga el nodo e2.

```
e2-cli stop
```

Reiniciando con una etiqueta diferente asignada al hexágono de nuestro nuevo activo.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Listado de emisiones de e2.

```
e2-cli listissuances
```

Las etiquetas de los activos son locales a cada nodo, sólo el hexágono del activo es reconocido por otros nodos de la red.

El mapeo de etiqueta a hexágono de activo es útil cuando se realizan acciones como transacciones y consultas de saldo de cartera, ya que permite una forma abreviada de referirse a un activo. Por ejemplo, si quisiéramos enviar parte de nuestro nuevo activo (una cantidad de 10) de e1 a e2 sin utilizar la etiqueta.

Primero tenemos que obtener una dirección a la que enviar el activo.

```
e2-cli getnewaddress
```

A continuación, utilice el comando sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Confirme la transacción generando un bloque.

```
generate 1
```

Comprobación de que el activo se recibió en e2.

```
e2-cli getwalletinfo
```

Podemos ver que, efectivamente, se ha recibido el activo.

Tenga en cuenta que e2 mapea el hex del activo recibido y lo muestra utilizando su propia etiqueta. Una forma más sencilla de hacer lo mismo sería utilizar la etiqueta de activo de e1 al enviar.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Entre bastidores, Elements asigna etiquetas locales a valores hexadecimales para ayudar a simplificar el uso de los activos emitidos.

En esta sección hemos visto cómo emitir y etiquetar activos. En la siguiente sección veremos cómo reemitir y destruir cantidades de un activo emitido.

## Reemisión de activos

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

En esta sección aprenderá cómo emitir más de un activo ya emitido y también cómo destruir una cantidad determinada de un activo emitido.

La necesidad de reemitir (crear más) de un activo o de destruir una cantidad del activo es algo que probablemente ocurra cuando el activo representa algo que no tiene un suministro fijo. Esto podría aplicarse a los activos que representan oro guardado en una cámara acorazada, por ejemplo; a medida que las unidades de oro entran y salen de la cámara acorazada, el activo que representa el suministro de la cámara acorazada debe ajustarse al alza o a la baja en consecuencia.

La reemisión de una cantidad de un activo requiere la propiedad del token asociado que se creó junto con el activo cuando se emitió inicialmente.

Al crear más de un activo, no importa qué nodo emitió el activo en primer lugar, siempre y cuando el nodo que está reemitiendo una cantidad de un activo esté en posesión de lo que comúnmente se llama token de reemisión del activo. Veremos cómo crear inicialmente el token de reemisión, cómo usarlo para reemitir una cantidad de un activo y también cómo transferir el token de reemisión a otros nodos, para que también tengan permiso para reemitir el activo.

Necesitaremos acceso a dos nodos Elements, que llamaremos e1 y e2. Los nodos han tenido sus blockchains reiniciados y el activo por defecto dividido entre ellos.

Haremos que e1 emita una cantidad de 100 de un nuevo activo y cree 1 token de reemisión para ese mismo activo. Crearemos la emisión como no cegada para simplificar el ejemplo. Así que vamos a seguir adelante y emitir el activo y su token de reemisión asociado.

```
e1-cli issueasset 100 1 false
```

Anote el ID del activo y también el del token (de reemisión).

Como más adelante volveremos a emitir más activos desde e2, tendremos que tomar nota del ID de transacción con el que se emitió el activo y utilizarlo para importar la dirección a la que se envió el activo.

Confirme la transacción.

```
e1-cli -generate 1
```

Ahora comprobaremos los detalles de la transacción utilizando el comando gettransaction:

```
e1-cli gettransaction <txid>
```

Desplazándose hacia arriba más allá del hexágono de los datos de la transacción verá que en la transacción e1 recibió 1 token de reemisión y 100 del activo asociado.

Tome una copia de la dirección para que podamos importarla a e2.

Y ahora importando la dirección a la cartera de e2.

```
e2-cli importaddress <address>
```

Ahora podemos ver que tanto e1 como e2 están al tanto de la emisión de activos.

```
e1-cli listissuances
e2-cli listissuances
```

Actualmente e1 posee una cantidad del activo y el token de reemisión 1, pero e2 no.

```
e1-cli getwalletinfo
```

Observe también que e1 tiene menos del activo por defecto que antes porque pagó una pequeña cantidad para cubrir las comisiones de transacción. Esta cantidad la cobrará e1 cuando el bloque creado madure a más de 100 bloques de profundidad.

```
e2-cli getwalletinfo
```

Como e1 tiene el token de reemisión, puede reemitir más. Esto se hace utilizando el comando reissueasset. Hagamos que e1 reemita otros 100 del activo.

```
e1-cli reissueasset <asset-id> 100
```

La comprobación de la reemisión ha funcionado.

```
e1-cli getwalletinfo
```

Puede ver que e1 tiene ahora 200 del activo, como se esperaba.

Como e2 no dispone de una cantidad del token de reemisión, recibirán un error si intentan reemitir el activo.

```
e2-cli reissueasset <asset-id> 100
```

Observe el mensaje de error.

Podemos ver los detalles de la reemisión desde e1 utilizando el comando listissuances.

```
e1-cli listissuances
```

Tenga en cuenta el indicador `is_reissuance`.

Si ahora enviamos a e2 una cantidad del token de reemisión, ellos mismos podrán reemitir una cantidad del activo. Primero necesitamos una dirección a la que enviarlo. Vale la pena señalar que el token de reemisión se trata igual que cualquier otro activo dentro de elements a la hora de enviar y mostrar saldos y que también se puede desglosar en denominaciones más pequeñas como cualquier otro activo, por lo que no necesitamos enviar el 1 token de reemisión a e2 para que pueda reemitir el activo. Cualquier denominación será suficiente. Generar una dirección para que e2 reciba el token de reemisión.

```
e2-cli getnewaddress
```

A continuación, envía una fracción del RIT de e1 a e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirme la transacción.

```
e1-cli -generate 1
```

Ahora podemos ver que e2 mantiene el 0,1 que se le envió.

```
e2-cli getwalletinfo
```

Esto significa que ahora e2 puede reemitir más del activo asociado al RIT que tiene en su monedero. Haremos que e2 vuelva a emitir 500 del activo.

```
e2-cli reissueasset <asset-id> 500
```

Compruebe el resultado de la reemisión.

```
e2-cli getwalletinfo
```

Puede verse que e2 mantiene ahora la cantidad reemitida en el saldo de su monedero y que el propio RIT no se consume en el proceso de reemisión de activos.

Destruir una cantidad de un activo es algo que puede hacer cualquiera que posea al menos la cantidad que se está destruyendo, no se rige por el token de reemisión.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

En esta sección hemos visto cómo emitir un activo, junto con cómo hacer uso del token de reemisión que se crea opcionalmente como parte de la emisión de activos. También hemos visto cómo transferir un token de reemisión es tan sencillo como transferir cualquier otro activo, y que poseer cualquier cantidad de un token de reemisión otorga a su poseedor el derecho a emitir más del activo asociado. Por lo tanto, es muy importante controlar quién tiene acceso a los tokens de reemisión en tu red. También hemos visto cómo destruir una cantidad de un activo y que este proceso no está controlado por la posesión del token de reemisión.

# Federación de Elementos

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Firma en bloque

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements admite un modelo de firma federada que permite especificar el número de miembros de Strong Federation que deben firmar un bloque propuesto para producir un bloque válido.

Anteriormente, y para facilitar el ejemplo, hemos estado creando bloques utilizando el comando `generate`, que no ha tenido que satisfacer un requisito de multifirma para que los bloques creados fueran aceptados por la red como válidos.

Configuraremos nuestros nodos para que requieran la creación de bloques 2-de-2 multisig. Esto se configurará utilizando el parámetro signblockscript, que puede añadirse al archivo de configuración o pasarse al nodo al iniciarse. Para inicializar una cadena con este parámetro, primero necesitamos construir el script que la compone.

Para ello, utilizaremos algunos nodos existentes, guardaremos los datos que generen y, a continuación, borraremos la cadena para poder reiniciarla utilizando nuestro parámetro signblockscript. Esto es necesario ya que el script forma parte de las reglas de consenso de la red y tendrá que establecerse en la inicialización de la cadena. No puede añadirse posteriormente a una cadena ya existente.

Necesitaremos acceso a dos nodos Elements, que llamaremos e1 y e2. Los nodos han tenido sus blockchains reiniciados y el activo por defecto dividido entre ellos.

Asegúrese de que el parámetro con_max_block_sig_size se establece en un valor alto en su archivo elements.conf, de lo contrario, la firma de bloque fallará más adelante en esta sección. Hemos establecido con_max_block_sig_size=2000 para este tutorial.

Como vamos a reiniciar nuestra cadena de bloques y a borrar los monederos asociados a e1 y e2, necesitaremos hacer una copia de las direcciones, claves públicas y claves privadas que utilizamos para generar el script de firma de bloques, para poder utilizarlas más adelante.

En primer lugar, necesitamos que cada uno de los que serán los nodos de firma de bloques genere una nueva dirección, de la que hay que sacar una copia.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

A continuación, debemos extraer las claves públicas de las direcciones y anotarlas para su uso posterior.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

A continuación, extraemos las claves privadas, que volveremos a importar más tarde para que los nodos puedan firmar los bloques después de reiniciar nuestra cadena de bloques y los datos del monedero.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Ahora tenemos que generar un script redeem con un 2 de 2 requisitos multi-firma. Para ello, utilizamos el comando createmultisig y pasamos el primer parámetro como 2 y, a continuación, proporcionamos dos claves públicas. Son estas claves las que hay que probar posteriormente cuando se cree el bloque.

Cualquiera de los dos nodos, e1 o e2, podría generar el multisig.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

Esto nos da nuestro redeemscript, que puedes copiar para usarlo más tarde.

Ahora tenemos que borrar los datos existentes de la cadena de bloques y de la cartera para poder empezar de nuevo con el nuevo signblockscript como parte de las reglas de consenso de la cadena. Esta es la razón por la que antes necesitábamos hacer una copia de algunos de los datos, como las claves privadas que se utilizarán en la nueva cadena para firmar bloques. Es necesario hacer esto antes de continuar.

Con nuestra cartera existente y los datos de la cadena eliminados, ahora podemos iniciar nuestros nodos y hacer que inicialicen una nueva cadena utilizando el parámetro signblockscript. Vamos a pasar -evbparams=dynafed:0::: para desactivar la activación dynafed, porque no necesitamos esa característica avanzada para este ejemplo.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Ahora tenemos que importar las claves privadas que hemos guardado antes para que nuestros nodos puedan firmar y ayudar a completar los bloques propuestos.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

El uso del comando generate ahora debería dar error ya que no cumple con las reglas de firma de bloques requeridas que ahora imponen nuestros nodos.

```
e1-cli -generate 1
```

Para proponer un nuevo bloque, cualquier nodo puede llamar al comando getnewblockhex. Esto devuelve el hexadecimal de un nuevo bloque que necesitará ser firmado antes de ser aceptado por cualquier nodo de nuestra red.

```
e1-cli getnewblockhex
```

Recuerde que el comando sólo crea un bloque propuesto, no lo genera.

Para confirmar esto podemos ver que actualmente no hay bloques en nuestra blockchain.

```
e1-cli getblockcount
```

Si intentamos enviar el hexágono de bloque sin firmarlo antes.

```
e1-cli submitblock <block-hex>
```

Recibimos un mensaje que nos dice que la prueba de bloque no es válida. Esto se debe a que aún no ha sido firmada por 2 de las 2 partes requeridas.

Así que hagamos que e1 firme el bloque propuesto.

```
e1-cli signblock <block-hex>
```

Que e2 firme el hexágono.

```
e2-cli signblock <block-hex>
```

Observa que e2 no firma la salida creada a partir de e1 firmando el bloque propuesto. Ambos firman el bloque hexadecimal propuesto independientemente de los resultados del otro.

Ahora tenemos que combinar las firmas de bloque de e1 y e2. Cualquiera de los nodos puede hacerlo, todo lo que necesitan es el hex de bloque firmado del otro nodo.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Puede ver que el comando combineblocksigs muestra el hexadecimal del bloque firmado, así como un estado de completo, que nos indica que el hexadecimal del bloque está listo para ser enviado.

Ahora cualquiera de los nodos puede enviar el hexágono de bloque completado. Haremos que e1 lo haga.

```
e1-cli submitblock <combined-signed-hex>
```

Comprobación de que el envío ha sido válido.

```
e1-cli getblockcount
e2-cli getblockcount
```

Puedes ver que tanto e1 como e2 han aceptado el bloque como válido y lo han añadido a la punta de sus copias locales del blockchain.

Para resumir el proceso. En esta sección tenemos:


- Propuso un bloque.
- Hizo que cada nodo lo firmara.
- Combina las firmas.
- Comprobado que las firmas son válidas y cumplen el umbral de redenominación de la cadena.
- Presentado el bloque.

Cada nodo de la red validaba el bloque y lo añadía a su copia local de la cadena de bloques.

### BLOQUEO

Aunque inicialmente el proceso parece complejo, la secuencia de firma de bloques en Elements es siempre la misma y la configuración inicial sólo debe realizarse una vez:

1. Configuración inicial (se realiza una vez)

2. Se crea una dirección multifirma llamada `signblockscript` utilizando las claves públicas de los Federated Block Signers.

3. La secuencia de comandos redimir de esto se utiliza para iniciar un nuevo blockchain.

4. Producción en bloque (en curso)

5. Los bloques propuestos se generan e intercambian para su firma.

Una vez que un número mínimo de firmantes ha firmado el bloque propuesto, éste se combina y se envía a la red. Si cumple los criterios del `signblockscript` de la cadena, los nodos lo aceptan como bloque válido.

## Elemento como cadena lateral

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements es una plataforma de cadena de bloques de código abierto y uso general que también puede vincularse a una cadena de bloques existente, como Bitcoin. Cuando se vincula a otra cadena de bloques, se dice que Elements funciona como una "cadena lateral". Las cadenas laterales permiten la transferencia bidireccional de activos de una cadena a otra. Implementar Elements como sidechain permite sortear algunas de las limitaciones inherentes a la mainchain, al tiempo que se conserva un buen grado de la seguridad proporcionada por los activos asegurados en la mainchain.

Mientras que una sidechain conoce la mainchain y su historial de transacciones, la mainchain no tiene conocimiento de la sidechain y no necesita ninguno para su funcionamiento. Esto permite a las sidechains innovar sin restricciones ni los retrasos asociados a las propuestas de mejora del protocolo de la mainchain. En lugar de intentar alterarlo directamente, ampliar el protocolo principal permite que la propia mainchain siga siendo segura y especializada, apuntalando el buen funcionamiento de la sidechain.

Al ampliar la funcionalidad de Bitcoin y aprovechar su seguridad subyacente, una cadena lateral basada en elementos es capaz de proporcionar nuevas funcionalidades que antes no estaban disponibles para los usuarios de la cadena principal. Un ejemplo de cadena lateral basada en Elements que se utiliza en producción es Liquid Network.

Para inicializar un blockchain de Elements como sidechain, necesitamos utilizar el parámetro de script federated peg. Este parámetro puede establecerse en el archivo de configuración de un nodo o pasarse al inicio.

El guión de peg federado define qué miembros de la federación fuerte pueden realizar funciones de peg-in y peg-out. A estos funcionarios se les denomina "vigilantes", ya que vigilan la cadena principal y las cadenas laterales en busca de transacciones válidas de entrada y salida de activos (peg-in y peg-out) y las ejecutan si son válidas. Salir" significa mover activos bloqueados de la cadena lateral a la principal, y "entrar" significa mover activos bloqueados de la cadena principal a la cadena lateral. Cuando decimos "mover a la cadena lateral", lo que realmente queremos decir es que los fondos se bloquean en una dirección multi-firma en la cadena principal y se crea una cantidad correspondiente del activo en la cadena lateral de elementos. Cuando decimos "salir de la cadena lateral", lo que queremos decir es que los activos se destruyen en la cadena lateral de Elements y se libera la cantidad correspondiente de los fondos bloqueados en la cadena principal. El permiso para realizar las funciones de peg-in y peg-out requiere que los funcionarios demuestren la propiedad de las claves públicas utilizadas en el script de peg federado. Para ello se utilizan las claves privadas correspondientes.

Por lo tanto, para crear un script peg federado, primero necesitamos que cada uno de nuestros nodos genere una clave pública. También tenemos que almacenar las claves privadas asociadas para su uso posterior, ya que tendremos que borrar cualquier dato de la cadena existente e inicializar una nueva cadena utilizando el script de la clavija federada. Esto se debe a que el script peg federado forma parte de las reglas de consenso de una cadena lateral, y no puede aplicarse a una cadena de bloques existente, no pegada, en una fecha posterior.

Así que vamos a generar una dirección con cada uno de nuestros nodos, almacenar los datos relevantes para su uso posterior y generar el script peg federado que utilizaremos para inicializar nuestra sidechain más tarde.

Primero necesitamos que cada uno de nuestros nodos, que actuarán como Watchmen en nuestra red, genere una nueva dirección.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

A continuación, validamos la dirección para obtener las claves públicas.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Y luego recuperar las claves privadas asociadas a cada dirección.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Almacena las claves privada y pública para su uso posterior.

Ahora tenemos que borrar la cadena de bloques existente y los datos del monedero, ya que vamos a inicializar una nueva cadena utilizando un script peg federado. Puedes hacerlo ahora. No olvide iniciar el demonio Bitcoin, que necesitaremos para peg-in.

Ahora podemos inicializar una nueva cadena con un script de peg federado creado utilizando las claves públicas que almacenamos anteriormente. Los números que introducimos y que rodean a nuestras claves públicas definen y delimitan el número de claves utilizadas, y la propiedad de las claves que debe probarse para pegar y sacar de nuestra cadena lateral.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Ahora importaremos las claves privadas que guardamos antes, para que nuestros nodos puedan después firmar y completar la transferencia de activos entre cadenas y satisfacer los requisitos del script de la clavija federada.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Ahora necesitamos madurar algunos bloques en ambas cadenas. La madurez de los bloques es un requisito del proceso de vinculación, ya que protege contra las reorganizaciones de bloques en la cadena principal que conducen a una inflación de la oferta de activos vinculados dentro de la cadena lateral.

Para mantener esta sección centrada en la clavija federada, generaremos bloques sin utilizar el modelo de firma de bloques que vimos en la última sección, y volveremos a utilizar el comando "generate" para crear nuevos bloques.

```
b-cli generate 101
e1-cli generate 1
```

No necesitamos necesariamente generar bloques ahora mismo para los elementos. Pero, vamos a generar uno de todos modos. Es una buena práctica para evitar posibles incoherencias.

Ahora nuestra cadena está lista para el peg-in. Para hacer el peg-in necesitamos generar un tipo especial de dirección usando el comando getpeginaddress. Ten en cuenta que el tiempo que transcurre entre la generación de una dirección peg-in con getpeginaddress y su reclamación con claimpegin debe ser el mínimo posible. las direcciones peg-in no son duraderas y no deben reutilizarse.

```
e1-cli getpeginaddress
```

Puedes ver que el comando crea una nueva dirección mainchain, así como un nuevo script que necesitará ser satisfecho para reclamar los fondos peg-in. La dirección mainchain es una dirección `pay to script hash` que será utilizada por los funcionarios que desempeñen el papel de Watchmen dentro de la red Elements.

Al igual que getnewaddress, getpeginaddress añade un nuevo secreto a la cartera del nodo de llamada, por lo que es importante factor de copia de seguridad del archivo de cartera en su proceso de gestión de nodos.

Ahora enviaremos algunos bitcoin desde la mainchain a la sidechain. Nuestra billetera de prueba de regresión mainchain ya tiene algunos fondos.

```
b-cli getwalletinfo
```

Podemos ver que la cartera tiene 50 bitcoin. Vamos a enviar un bitcoin de la mainchain a la sidechain. Tenemos que enviar los fondos a la dirección mainchain que nuestro nodo generó anteriormente.

```
b-cli sendtoaddress <e1-pegin-address>
```

Debemos conservar el ID de esta transacción, ya que lo necesitamos como prueba de financiación más adelante.

Ahora podemos ver que el saldo de la cartera mainchain ha disminuido en la cantidad que enviamos, más una pequeña cantidad adicional para cubrir los gastos de las transacciones.

```
b-cli getwalletinfo
```

Necesitamos madurar la transacción de nuevo.

```
b-cli generate 101
```

Para que nuestro nodo Elements reclame los fondos de peg-in necesitamos obtener la `prueba` de que se ha realizado la transacción de peg-in. La prueba criptográfica utiliza el ID de la transacción de financiación para calcular la ruta de merkel y demuestra que la transacción está presente en un bloque confirmado.

```
b-cli gettxoutproof '["<tx-id>"]'
```

También necesitamos los datos brutos de las transacciones.

```
b-cli getrawtransaction <tx-id>
```

Con la prueba y los datos sin procesar de la transacción, nuestro nodo de elementos puede ahora reclamar el peg-in utilizando la transacción sin procesar y la prueba de la transacción.

```
e1-cli claimpegin <raw> <proof>
```

Tenga en cuenta que hay un tercer argumento opcional que podríamos haber proporcionado a claimpegin. Este tercer parámetro puede utilizarse para especificar la dirección de la cadena lateral a la que enviar los fondos reclamados. Esto no era necesario en nuestro ejemplo, ya que estábamos llamando al comando desde el mismo nodo que posee la dirección a la que van los fondos reclamados.

Comprobación del saldo de e1.

```
e1-cli getwalletinfo
```

Generar un bloque para confirmar la reclamación.

```
e1-cli generate 1
```

Comprobación del saldo de e1.

```
e1-cli getwalletinfo
```

Podemos ver que la clavija ha sido reclamada con éxito.

Para peg-out, el proceso es similar. Se genera una dirección, se le envían fondos y éstos se liberan si la transacción es válida. No cubriremos todo el proceso de peg-out ya que implica trabajo en la mainchain que está fuera del alcance de este curso. Los pasos en términos de los eventos de Elements son que se genera una dirección en la mainchain.

```
b-cli getnewaddress
```

Los fondos se envían a la dirección mainchain desde un nodo Elements utilizando el comando sendtomainchain.

```
e1-cli sendtomainchain <new-address> 1
```

Generar un bloque para confirmar la transacción.

```
e1-cli generate 1
```

Comprueba el saldo del monedero del nodo.

```
e1-cli getwalletinfo
```

Y ver que el saldo ha disminuido.

En esta sección hemos visto cómo:


- Generar un script de peg federado.
- Inicializa una nueva cadena que utiliza el script como regla de parámetro de consenso de red.
- Enviar fondos de la mainchain a la sidechain.
- Reclama los fondos dentro de la cadena lateral Elements.
- Entender cómo se inicia el envío de fondos de vuelta a la mainchain.

### FederatedPegScript

Para que Elements funcione como sidechain, el bloque génesis de su blockchain debe crearse con un `fedpegscript`. Esto se hace pasando el parámetro `fedpegscript` al iniciar el nodo. El script formará parte de las reglas de consenso de la blockchain de Elements y permitirá que las solicitudes de peg-in y peg-out sean validadas y procesadas.

El `fedpegscript` se compone de claves públicas controladas por las personas autorizadas a realizar las acciones peg. A continuación se muestra el formato de ejemplo de un fedpegscript multifirma 2-de-2:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Nota: Los caracteres fuera de las claves públicas son delimitadores que indican los requisitos de clave pública y `n de m`. Por ejemplo, la plantilla para un fedpegscript 1-de-1 sería '5121<clave pública 1>51ae'.

### Peg-in

Antes de que una cadena lateral de Elements acepte una vinculación, debe tener suficientes confirmaciones en la cadena principal. Esto es necesario para evitar la inflación en el suministro del activo vinculado en la cadena lateral de Elements que podría provocar una reorganización de la cadena principal.

Se esperan breves reorganizaciones de la punta de la blockchain de Bitcoin como parte del funcionamiento normal del mecanismo de consenso Proof of Work (PoW). Como tal, Elements sólo acepta que un peg-in sea válido cuando tiene suficiente profundidad dentro del blockchain de Bitcoin. Esto sirve para evitar que Elements acepte el mismo peg-in más de una vez.

### Peg-Out

Un peg-out se produce cuando un nodo Elements llama al comando `sendtomainchain`, que toma como entrada una dirección mainchain (el destino del peg-out), así como la cantidad del activo pegged a `retirar`. De este modo, se crea una transacción de "peg-out" en la cadena lateral. Una vez que los Funcionarios que actúan como Vigilantes detectan que la transacción de "peg-out" ha sido confirmada en la cadena lateral, se encargan de liberar el activo en la cadena principal hacia el destino del "peg-out", como aprendimos en secciones anteriores del curso.

## Elementos como cadena de bloques independiente

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Hasta ahora, hemos visto cómo ejecutar Elements como sidechain. Sin embargo, también puede funcionar como una solución de cadena de bloques independiente con su propio activo nativo predeterminado. En esta configuración, una blockchain de Elements conserva todas las características de una implementación sidechain, como las transacciones confidenciales y los activos emitidos, pero no necesita peg-in o peg-out para añadir o eliminar cantidades de activos predeterminados de la circulación.

En esta sección lo haremos:

Inicializa una nueva cadena de bloques de Elements con un activo por defecto llamado `newasset`.

Especifique que se crearán 1.000.000 `newasset` junto con 2 tokens de reemisión para él.

Reclama todas las monedas "newasset" que cualquiera pueda gastar.

Reclama todos los tokens de reemisión que cualquiera pueda gastar para "newasset".

Envía el activo y su token de reemisión a la cartera de otro nodo.

Reemite más 'newasset' de ambos nodos.

Con el fin de inicializar una red Elements para que funcione como una blockchain independiente, es necesario iniciar cada nodo con algunos parámetros básicos. Se utilizan para indicar al nodo que no intente validar peg-ins de otra blockchain, el nombre del activo predeterminado de la red y la cantidad de activo predeterminado y token de reemisión asociado que se creará.

Ahora empezaremos una nueva cadena utilizando estos parámetros en nuestros dos nodos Elements conectados. Llamaremos al activo por defecto `newasset` y emitiremos un millón de ellos y dos tokens de reemisión `newasset`.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Tenga en cuenta que las cantidades utilizadas aquí son en la denominación más pequeña que la red puede aceptar, por lo que los doscientos millones de tokens de reemisión equivalen en realidad a dos tokens enteros. Lo mismo ocurre con la denominación de las monedas libres iniciales.

Consulta los saldos actuales de los monederos de nuestros nodos.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Podemos ver que la inicialización ha funcionado correctamente.

Como la emisión inicial de activos se crea como "cualquiera puede gastar", haremos que e1 los reclame todos para poder eliminar el acceso de e2 a ellos.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Tenga en cuenta que no es necesario especificar "newasset" como activo a enviar, puesto que ya es el activo por defecto y, por tanto, también el activo por defecto utilizado para pagar las tarifas de red.

Dentro de Elements, puedes enviar múltiples tipos de activos a la misma dirección, por lo que podemos reutilizar la dirección que acabamos de generar para recibir el activo por defecto, y utilizarla como dirección de destino para los tokens de reemisión.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirme las transacciones.

```
e1-cli generate 101
```

Ahora comprobaremos que e1 es el único titular del activo y de su token de reemisión.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Lo que podemos ver que es el caso.

Ahora enviaremos parte del 'newasset' a e2, que actualmente tiene un saldo de cero.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Tenga en cuenta que no hemos tenido que especificar el tipo de activo que se enviará, ya que `newasset` se ha creado como el activo por defecto de la red

Enviemos también algunos de los tokens de reemisión para `newasset` a e2.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirme las transacciones.

```
e1-cli generate 101
```

Podemos comprobar que los monederos se han actualizado en consecuencia.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Ahora reemitiremos algunos de los activos por defecto de e1. Tenga en cuenta que la capacidad de hacer esto está habilitada por el parámetro de inicio initialreissuancetokens. El cual si se omite o se pone a cero resultará en un activo por defecto que no podrá ser reemitido en una fecha posterior.

```
e1-cli reissueasset newasset 100
```

Hemos podido utilizar la etiqueta de `newasset` en lugar de tener que proporcionar el valor de id hexadecimal porque una cadena de Elementos siempre etiqueta su activo por defecto.

Comprobación de que la reemisión del activo por defecto ha funcionado:

```
e1-cli generate 101
e1-cli getwalletinfo
```

Ahora demostraremos que, dado que e2 posee algunos de los tokens de reemisión `newasset`, también puede reemitir el activo por defecto.

```
e2-cli reissueasset newasset 100
```

Comprobación de que la reemisión del activo por defecto por parte de e2 ha funcionado.

```
e2-cli generate 101
e2-cli getwalletinfo
```

En esta sección hemos configurado Elements como una cadena de bloques independiente y hemos comprobado que la funcionalidad básica funciona como cabría esperar.

Utilizamos parámetros de arranque para:

Inicializa una nueva blockchain de Elements con un activo por defecto llamado 'newasset'.

Especifica la cantidad del activo por defecto a crear en la inicialización de la cadena.

Crea algunos tokens de reemisión para el activo por defecto y reemite más del activo por defecto desde ambos nodos.

En nuestra red autónoma blockchain Elements, todas las demás operaciones transaccionales funcionarán de la misma manera que los ejemplos cubiertos en las secciones principales del curso, pero utilizarán "newasset" en lugar de "bitcoin" como activo por defecto y de pago.

### Parámetros de inicio del nodo e inicialización de la cadena

Para indicarle a un nodo Elements que funcione como una blockchain autónoma se deben utilizar algunos parámetros juntos. Echemos un vistazo a cada uno de ellos y averigüemos qué hacen.

#### `validatepegin=0`

Como una blockchain autónoma no necesita validar ninguna transacción peg-in o peg-out, necesitamos desactivar esas comprobaciones. Con esta configuración, no es necesario ejecutar el software cliente de Bitcoin ni almacenar una copia de la blockchain de Bitcoin, ya que la red Elements funcionará de forma independiente.

#### nombredeactivopegadopordefecto

Permite especificar el nombre del activo por defecto creado al inicializar el blockchain.

#### `initialfreecoins`

El número (en el equivalente a la unidad Satoshi de Bitcoin) del activo por defecto a crear.

#### `fichas de reemisión inicial

El número (en el equivalente a la unidad Satoshi de Bitcoin) de tokens de reemisión para el activo por defecto a crear. Sin esto sería imposible crear más del activo por defecto. Si no quieres que sea posible crear más del activo por defecto esto puede ser puesto a cero u omitido.

Utilizando estos parámetros, el común para iniciar un nodo se vería algo como esto:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Operaciones básicas

El parámetro `defaultpeggedassetname` aplica una etiqueta al activo por defecto. Sin este parámetro, el activo por defecto se llamará automáticamente `bitcoin`. En secciones anteriores, cuando enviábamos activos emitidos por nosotros mismos a otro nodo, teníamos que especificar el hex del activo o la etiqueta del activo aplicada localmente para indicar a Elements qué activo estábamos enviando. Como `defaultpeggedassetname` se aplica a todos los nodos no necesitamos nombrarlo cuando lo enviamos, aunque su nombre no sea `bitcoin`. Todas las funciones que antes enviaban `bitcoin` por defecto ahora enviarán lo que hayas elegido para etiquetar el activo por defecto.

Así que enviar 10 del nuevo activo por defecto a una dirección es tan simple como:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Si también has proporcionado al nodo un valor para `initialreissuancetokens` mayor que cero, entonces también podrás reemitir más del activo por defecto, algo que no es posible si ejecutas Elements como sidechain.

Para ello, cualquier nodo que posea una cantidad del token asociada al activo por defecto sólo tiene que emitir un comando de la forma:

```
e1-cli reissueasset <default asset name> <amount>
```

Utilizando los parámetros anteriores puede operar Elements como un blockchain independiente con su propio activo por defecto, desacoplado de Bitcoin y otros blockchains.

## Conclusión

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

En este curso hemos aprendido que Elements es un protocolo de red de código abierto que puede implementarse como una cadena lateral de otra cadena de bloques o como una solución de cadena de bloques independiente.

Hemos visto que el código fuente y el sitio web de Elements (https://github.com/ElementsProject/elements) están alojados en GitHub y que existen foros de debate comunitarios, como Build On L2(https://community.liquid.net/c/developers/), o Liquid Developers Telegram (https://t.me/liquid_devel), que pueden utilizarse para obtener más información sobre la implantación y el desarrollo de aplicaciones en Elements y Liquid. Se trataron aspectos clave como las transacciones confidenciales y los activos emitidos, así como el modo en que los miembros de una federación sólida permiten la firma federada de bloques y el mecanismo 2-Way Peg.

El siguiente paso es desafiarte a ti mismo con un cuestionario acumulativo que cubra todas las secciones anteriores, y después comenzar tu viaje de Elementos... ¡buena suerte!

# Conclusión

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Opiniones y valoraciones

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>verdadero</isCourseReview>

## Conclusión

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Enhorabuena por completar este curso

Estamos encantados de que hayas alcanzado con éxito este hito en tu viaje de aprendizaje. Gracias a tu dedicación y compromiso, has adquirido valiosos conocimientos y habilidades que te serán de gran utilidad en tu desarrollo profesional.
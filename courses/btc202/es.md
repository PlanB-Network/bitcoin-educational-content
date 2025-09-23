---
name: Configuración del primer nodo Bitcoin
goal: Comprender, instalar, configurar y utilizar un nodo Bitcoin
objectives: 


  - Comprender el papel y la finalidad de un nodo Bitcoin.
  - Identificar las diferentes soluciones de hardware y software disponibles.
  - Instale y configure una Full node (Bitcoin core).
  - Utilice el Paraguas Interface y añada aplicaciones útiles.
  - Conecta una Wallet personal a su propio nodo.
  - Explore la configuración avanzada y las mejores prácticas de seguridad.


---
# Conviértete en un bitcoiner soberano



Probablemente estés familiarizado con el adagio "Ni tus llaves, ni tus monedas", que anima a la autocustodia de tus bitcoins. Poseer tus propias claves es, en efecto, un primer paso esencial, pero no es suficiente. Para lograr una verdadera soberanía monetaria, también necesitas instalar y utilizar tu propio nodo Bitcoin. Este curso está diseñado para guiarte a través de este paso fundamental en tu viaje por Bitcoin



BTC 202 es un curso accesible diseñado para enseñarte a hacer tu propio nudo Bitcoin, incluso si no eres un experto técnico. Empezaremos definiendo qué es un nudo Bitcoin, para qué sirve y por qué es absolutamente esencial que hagas uno tú mismo. Luego te guiaré paso a paso en la elección de tu hardware, la instalación del software necesario, la conexión de tu Wallet y las primeras optimizaciones posibles para llevarlo más lejos.



Ejecutar un nodo Bitcoin no es sólo una opción para expertos; es una necesidad. Es una herramienta de resiliencia que todo usuario necesita entender e implementar. ¡Este curso es tu punto de partida para convertirte en un bitcoiner soberano!




+++




# Introducción


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Resumen del curso


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Bienvenido a BTC 202, donde aprenderás a instalar, configurar y utilizar un nodo Bitcoin de forma fácil e independiente. Pero eso no es todo: también aprenderás más sobre el lugar y la función de los nodos en el sistema Bitcoin. El curso alterna entre explicaciones teóricas y prácticas guiadas.



### Parte 1 - Introducción



En esta primera parte del curso, aclararemos las nociones básicas y luego pasaremos a definiciones más precisas. ¿Qué es un nodo? ¿Cuáles son las diferencias entre nodo, Wallet y Miner? A continuación, aprenderá sobre Bitcoin core y las implementaciones del protocolo. El objetivo es hablar el mismo idioma, evitar confusiones y establecer una base teórica sólida.



### Parte 2 - Convertirse en un bitcoiner soberano



En esta segunda parte, empezaré explicando por qué es importante tener tu propio nodo Bitcoin. Luego exploraremos los distintos tipos de nodos que existen (completo, pruned, SPV...), cómo funcionan y sus implicaciones técnicas.



A continuación, le ofreceremos una visión general del software disponible para ejecutar un nodo Bitcoin, incluidas sus ventajas e inconvenientes. Por último, concluiremos con algunas recomendaciones muy prácticas para elegir el hardware adecuado a tus necesidades y presupuesto.



Esta sección, por tanto, ilustra el camino del bitcoiner soberano: entender por qué es necesario ejecutar un nodo, elegir el tipo de nodo, en función de esta elección, seleccionar el software y, en función del software elegido, determinar el hardware apropiado.



### Parte 3 - Instalar fácilmente un nodo Bitcoin



Una vez completada esta preparación, es hora de ponerse prácticos con la Parte 3 dedicada a Umbrel: el SO para la nube doméstica que simplifica el autoalojamiento y la instalación de un nodo Bitcoin y Lightning.



Después de una breve introducción a Umbrel, vamos a ofrecer un tutorial detallado para guiarte a través del proceso de instalación y configuración en tu propia máquina DIY. El objetivo de esta parte es claro: tener tu primer nodo Bitcoin totalmente funcional y sincronizado.



### Parte 4 - Conexión de la Wallet al nodo



Ahora que ya has configurado un nodo Bitcoin, ¡es hora de utilizarlo! En esta sección, aprenderás a conectar tu software de gestión Wallet (como Sparrow wallet) a tu propio indexador Address (Electrs o Fulcrum), o directamente a Bitcoin core, para que ya no dependas de servidores públicos.



También examinaremos el papel de los indexadores y los distintos métodos de conexión a tu nodo (LAN, Tor, Tailscale, etc.). Finalmente, en el último capítulo, repasaremos las aplicaciones más útiles disponibles en Umbrel para el bitcoiner cotidiano.



### Parte 5 - Conceptos avanzados y buenas prácticas



En esta última parte de BTC 202, el objetivo es profundizar en tus conocimientos. En primer lugar, veremos las mejores prácticas que debes adoptar con tu nuevo nodo Bitcoin y cómo mantenerlo a largo plazo.



A continuación, nos tomaremos el tiempo para revisar parte de la teoría tratada anteriormente en el curso, incluyendo la comprensión del proceso IBD y el descubrimiento de pares en detalle, explorando la anatomía de un nodo, y, finalmente, aprender a utilizar el archivo `Bitcoin.conf` para afinar la configuración.



### Parte 6 - Sección final



Como en todos los cursos de Plan ₿ Network, en la sección final encontrará un examen final que pondrá a prueba sus conocimientos sobre los nodos de Bitcoin.



Entonces, ¿estás listo para encender tu primer nodo Bitcoin? ¡Ponga rumbo a la soberanía!



## ¿Qué es un nodo Bitcoin?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Tal y como la describe su creador, Satoshi Nakamoto, Bitcoin se presenta como un sistema de dinero electrónico entre iguales. Esta simple frase, que es el título del Libro Blanco, encierra muchas pistas sobre la naturaleza de Bitcoin:




- En primer lugar, Satoshi describe Bitcoin como un "sistema", es decir, un conjunto coherente de componentes de hardware y software que interactúan para prestar un servicio específico o realizar una función concreta;
- A continuación, explica que este sistema permite utilizar dinero electrónico, es decir, una forma de moneda intangible;
- Por último, señala que este sistema no depende de ninguna entidad central: es "peer-to-peer", es decir, que son los propios usuarios quienes hacen funcionar el sistema.



Dado que Bitcoin es un sistema, debe ejecutarse necesariamente en ordenadores. Y, debido a su naturaleza peer-to-peer, son los propios usuarios quienes asumen la responsabilidad de hacer funcionar estas máquinas. Lo que llamamos "nodo Bitcoin" es precisamente el ordenador en el que se ejecuta el software que implementa el protocolo Bitcoin (como Bitcoin core, pero volveremos sobre ello más adelante). Esto es lo que permite a Bitcoin funcionar sin una autoridad central: la validación se lleva a cabo de forma distribuida, por miles de máquinas independientes pertenecientes a miles de usuarios.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Son precisamente estos usuarios los que garantizan la seguridad de Bitcoin. Como explica Eric Voskuil en su libro *Cryptoeconomics*, la seguridad de Bitcoin no depende ni de Blockchain, ni de la potencia de hashing, ni de la validación, ni de la descentralización, ni de la criptografía, ni del código abierto, ni de la teoría de juegos. La seguridad de Bitcoin depende principalmente de los individuos que están dispuestos a exponerse a un riesgo personal. La descentralización permite repartir este riesgo entre un gran número de individuos, y sólo su capacidad de resistencia garantiza la solidez del sistema.



Este principio es fácil de entender: si Bitcoin dependiera de un solo nodo propiedad de una sola persona, bastaría con encarcelarla para cerrar la red, ya que ella sola asumiría todos los riesgos. Con decenas de miles de nodos repartidos por todo el mundo, el riesgo está diseminado: habría que neutralizar a cada uno de estos operadores para apagar Bitcoin.



![Image](assets/fr/048.webp)



Así, podemos distinguir y nombrar varios conceptos para aclarar las cosas para el resto de este curso:




- Bitcoin moneda: unidad de cuenta utilizada para las transacciones dentro de este sistema;
- La red Bitcoin: el conjunto de todos los nodos conectados;
- Nodos Bitcoin: máquinas que ejecutan una implementación de Bitcoin;
- Bitcoin implementaciones: software que traduce el protocolo en instrucciones ejecutables;
- Protocolo Bitcoin: conjunto de normas que rigen el funcionamiento del sistema;
- El sistema Bitcoin: la combinación coherente de todos estos Elements.



### El papel del nodo Bitcoin



Los nodos de Bitcoin forman juntos lo que se conoce como la red Bitcoin. Permiten que todo el sistema funcione de forma autónoma, sin recurrir a una autoridad central ni a una jerarquía de servidores.



Desde el principio, Bitcoin se diseñó para que cada usuario pudiera gestionar un nodo personal. Este caso sigue siendo válido con el software Bitcoin core actual, que combina las funciones de Wallet y nodo. Pero hoy en día, esta función suele estar disociada: muchos monederos modernos de Bitcoin son sólo monederos que se conectan a nodos externos (propiedad de la misma persona o no).



### Mantener Blockchain



La primera tarea de un nodo es mantener una copia local de la Blockchain. Para evitar Double-spending en Bitcoin sin implicar a una autoridad central, cada usuario debe comprobar que no existe ninguna transacción en el sistema. La única forma de estar seguro de ello es conocer todas las transacciones realizadas en Bitcoin. Por este motivo, todas las transacciones llevan una marca de tiempo y se agrupan en bloques, y cada nodo almacena toda la Blockchain.



> La única manera de confirmar la ausencia de una transacción es estar al tanto de todas las transacciones.

Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Blockchain es, por tanto, un registro en evolución: cada vez que un Miner publica un nuevo bloque, el nodo comprueba su validez antes de añadirlo a su propia copia local de la cadena. A fecha de hoy (julio de 2025), el Blockchain completo supera los 675 GB, y este tamaño sigue creciendo, ya que se añade un nuevo bloque cada 10 minutos por término medio.



![Image](assets/fr/049.webp)



El nodo también mantiene un registro local de todos los UTXOs existentes en un momento dado, conocido como **Conjunto UTXO**. Esta base de datos contiene todos los fragmentos no gastados de Bitcoin. Volveremos sobre este tema en detalle en la parte final del curso.



### Verificar y distribuir transacciones



La segunda función de un nodo es garantizar la verificación y propagación de las transacciones. Cuando una nueva transacción llega al nodo (ya sea a través del software Wallet o de otro nodo), éste comprobará que cumple una serie de reglas (reglas de consenso y reglas de retransmisión). Por ejemplo:




- los bitcoins gastados deben existir en su conjunto UTXO (la base de datos de salidas no gastadas);
- la firma debe ser válida y deben cumplirse todas las condiciones de gasto (escritura válida);
- la cantidad total de productos no debe superar la cantidad total de insumos, lo que significa que los costes no pueden ser negativos.



![Image](assets/fr/050.webp)



Una vez validada, la transacción se almacena en la Mempool del nodo, un espacio de memoria temporal reservado para transacciones no confirmadas, y luego se retransmite a los demás pares de la red a los que está conectado. Este mecanismo de distribución y validación continúa de nodo a nodo. De este modo, la transacción se propaga a través de la red Bitcoin, y cada nodo la almacena en Mempool hasta que es incluida en un bloque válido por un Miner, que actúa entonces sobre su primera confirmación.



### Comprobar y distribuir bloques



La tercera función del nodo consiste en gestionar los bloques minados. Cuando una Miner descubre un nuevo bloque con una Proof of Work válida, lo difunde por la red. Los nodos lo reciben, comprueban que cumple todas las normas del protocolo y lo integran en su propia copia local de la Blockchain si es válido. Al igual que ocurre con las transacciones, los bloques recién validados se retransmiten a todos los pares conectados al nodo. Este proceso continúa hasta que todos los nodos de la red Bitcoin conocen el nuevo bloque.



![Image](assets/fr/051.webp)



## ¿Cuál es la diferencia entre un arco y una Wallet?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Es esencial distinguir entre dos tipos distintos de software cuando se utiliza Bitcoin: el nodo y Wallet.



Un nodo Bitcoin, como ya se ha dicho, es un programa informático que participa activamente en la red entre iguales. Realiza tres tareas principales:




- copia de seguridad de Blockchain,
- validación y retransmisión de transacciones,
- validación y retransmisión de bloques.



Una Bitcoin Wallet, por otro lado, es una pieza de software diseñada para almacenar y gestionar tus claves privadas. Estas claves te permiten gastar tus bitcoins satisfaciendo los scripts de bloqueo (normalmente mediante una firma). Un Wallet puede conectarse a un nodo (ya sea local o remoto) para consultar el estado del Blockchain y difundir las transacciones que construye, pero no es, como tal, un participante en la red.



En algunos casos, estas dos funciones coexisten dentro del mismo software, como es el caso de Bitcoin core, que sirve tanto de Full node como de Wallet. Sin embargo, muchos programas populares de Wallet (Sparrow, BlueWallet, etc.) requieren una conexión a un nodo externo (ya sea propio o de terceros) para emitir transacciones y determinar el saldo de Wallet.



![Image](assets/fr/052.webp)



## ¿Cuál es la diferencia entre un nodo y un Miner?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Las nociones de nodo y de Miner se confunden a menudo. Sin embargo, estos dos Elements desempeñan funciones radicalmente distintas dentro del sistema.



Inicialmente, cuando Bitcoin fue lanzada por Satoshi Nakamoto en 2009, se esperaba que cada usuario participara en la red como un todo. Así, el software original de Bitcoin combinaba varias funciones a la vez: actuaba como Wallet, un nodo, y también como Miner, capaz de generar nuevos bloques. En aquella época, la dificultad de Mining era muy baja. Todo lo que había que hacer era ejecutar el software Bitcoin en el ordenador para encontrar bloques y recibir bitcoins como recompensa.



Sin embargo, con la popularización gradual de la Bitcoin y el aumento del número de mineros, el panorama competitivo de la Mining ha experimentado un cambio radical. Hoy en día, Mining se ha convertido en una actividad extremadamente competitiva, dominada por actores industriales equipados con infraestructuras especializadas. La potencia necesaria para minar un nuevo bloque es ahora tan grande que es prácticamente imposible que un usuario individual lo consiga utilizando únicamente un ordenador convencional. Como consecuencia, Mining se realiza ahora principalmente con máquinas especializadas llamadas ASIC (*Application-Specific Integrated Circuits*). Estos chips están optimizados exclusivamente para ejecutar el doble SHA-256, el algoritmo utilizado para Mining en Bitcoin.



![Image](assets/fr/053.webp)



Ante esta evolución, las funciones del nodo Bitcoin y del Miner se han diferenciado claramente. Como ya se ha indicado, la función de un nodo de Bitcoin es puramente informativa y de validación. La función de Miner es diferente:




- Selecciona las transacciones pendientes en la Mempool.
- Construye un bloque candidato integrando estas transacciones.
- Busca por ensayo y error una Proof of Work válida.
- Si encuentra una prueba válida, difunde el bloque a través de su nodo a los demás nodos.



Un Miner necesita un nodo Bitcoin para interactuar con la red.



El papel de la Miner también se diferencia a veces del de la picadora. Una picadora es una máquina cuya tarea consiste en Hash plantillas de bloques suministradas por el servidor de un pool, buscando hashes que satisfagan el objetivo de dificultad definido para las acciones, y no el de Bitcoin. El resto del proceso de Mining, que incluye la construcción real de bloques, la selección de transacciones o la búsqueda de Proof-of-Work según la dificultad propia de Bitcoin, así como la distribución, es realizado directamente por los pools.



![Image](assets/fr/054.webp)



Por último, existe una importante diferencia en términos de incentivo económico entre la Miner y el nodo. Dirigir un nodo de Bitcoin no proporciona ningún beneficio monetario directo. En cambio, participar en Mining reporta recompensas (subvenciones y comisiones por transacción) por cada bloque encontrado.



En la Parte 2, exploraremos con más detalle los beneficios prácticos y personales de instalar y utilizar un nodo Bitcoin, más allá de los puramente económicos.



## Bitcoin core y aplicación de protocolos


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



El protocolo Bitcoin no es software: es un conjunto de reglas tácitas compartidas entre los usuarios de la red. Define las condiciones de validez de las transacciones, los mecanismos de creación de dinero, el formato de los bloques, las condiciones de Proof-of-Work y muchas otras especificaciones. Para interactuar con este protocolo, los usuarios deben ejecutar un software que implemente estas reglas: esto se conoce como una **implementación** de Bitcoin.



Una implementación es, por tanto, software de nodo: un programa capaz de interactuar con otras máquinas de la red Bitcoin, descargar, verificar, almacenar y propagar bloques y transacciones, y aplicar localmente reglas de consenso y retransmisión. Cada implementación es una interpretación concreta del protocolo, escrita en un lenguaje de programación determinado, con su propia arquitectura, rendimiento y ergonomía. Cada implementación tendrá también su propia organización de desarrollo, con su propia división de responsabilidades.



Entre estas implementaciones, una domina con diferencia: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Una aplicación histórica que se ha convertido en una referencia



Bitcoin core es el software de referencia para el protocolo Bitcoin. Se deriva del código original escrito por Satoshi Nakamoto en 2008-2009, y es una continuación directa del mismo. Inicialmente conocido como "*Bitcoin*", luego "*Bitcoin QT*" (debido a la adición de un Interface gráfico a través de la biblioteca Qt), fue rebautizado como "*Bitcoin core*" en 2014 para diferenciar claramente el software de la red. Desde la versión 0.5, se distribuye con dos componentes: `Bitcoin-qt` (el Interface gráfico) y `bitcoind` (el Interface de línea de comandos).



En teoría, Bitcoin core no representa el protocolo Bitcoin, sino que es una implementación entre muchas otras. Sin embargo, se distingue por su adopción masiva, su antigüedad, la solidez de su código y el rigor de su proceso de desarrollo. Por consiguiente, en la práctica, las normas aplicadas por Bitcoin core son de facto las del protocolo Bitcoin: usuarios, desarrolladores, mineros y servicios ecosistémicos se refieren a él casi exclusivamente.



### Distribución actual de las implantaciones



Según [datos recogidos en agosto de 2025 por Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (un conocido desarrollador del ecosistema), la distribución de implementaciones entre los nodos públicos de la red es la siguiente:




- Bitcoin core**: 87.3% de los nodos
- Bitcoin Knots**: 12.5
- Otras implementaciones acumuladas**: 0.2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



En otras palabras, aproximadamente 9 de cada 10 nodos públicos utilizan Bitcoin core. El resto de la red depende de clientes más marginales. El resto de la red depende de clientes más marginales (aunque la cuota de Knots ha aumentado considerablemente en los últimos meses, sobre todo a raíz de los debates sobre el límite de tamaño de `OP_RETURN`). Estas implementaciones alternativas suelen ser mantenidas por una sola persona o un pequeño equipo.



**Nota:** No obstante, estas cifras siguen siendo estimaciones, ya que se basan principalmente en los *nodos que escuchan*, es decir, los nodos que aceptan conexiones entrantes (con el puerto 8333 abierto). Los nodos que no escuchan* son mucho más complejos de contabilizar, ya que es imposible conectarse a ellos directamente: hay que esperar a que la iniciativa venga de ellos, en forma de conexión saliente. El sitio de Luke Dashjr afirma que también intenta contabilizar estos *nodos que no escuchan*, pero sigue siendo imposible obtener datos perfectamente precisos sobre ellos, y la actualización de estas estadísticas va inevitablemente por detrás de la realidad.



### Funcionamiento interno de Bitcoin core



Bitcoin core está escrito en C++. También es un proyecto de código abierto mantenido por una comunidad de desarrolladores voluntarios o remunerados por diversas entidades (a menudo por empresas del ecosistema interesadas en el desarrollo de Core). [El código está alojado en GitHub](https://github.com/Bitcoin/Bitcoin), y el desarrollo sigue un riguroso:




- Los colaboradores** presentan propuestas en forma de _pull requests_ (PR). En principio, cualquiera puede proponer un cambio, pero debe probarse, documentarse y pasar por un proceso de revisión por pares.
- Los **maintainers** tienen derecho a aprobar y fusionar los PR. Son los que garantizan la coherencia y la estabilidad del proyecto. En julio de 2025, son cinco: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao y Ryan Ofsky.
- No ha habido **mantenedor principal** desde febrero de 2023. Esta función fue desempeñada inicialmente por Satoshi Nakamoto en el lanzamiento de Bitcoin, luego por Gavin Andresen tras la marcha de Nakamoto a principios de 2011 y, por último, por Wladimir J. Van Der Laan desde 2014 hasta 2023.



![Image](assets/fr/057.webp)



El desarrollo de Bitcoin core sigue una lógica meritocrática: se anima a los nuevos colaboradores a revisar y probar el código antes de proponer ellos mismos cualquier cambio. Las decisiones se basan en el consenso técnico, y las modificaciones importantes (sobre todo en áreas de consenso) requieren debates previos en canales públicos, como listas de correo o clubes de revisión de relaciones públicas.



### Otras implantaciones de Bitcoin



Aunque marginales en términos de adopción, existen otros clientes. El principal es Bitcoin Knots, desarrollado por Luke Dashjr, un Fork de Bitcoin core que incorpora opciones adicionales y un enfoque más conservador del desarrollo. Entre ellas, restricciones más estrictas en los formatos de transacción.



![Image](assets/fr/058.webp)



También podemos mencionar:




- Libbitcoin**: una biblioteca modular en C++ desarrollada por Amir Taaki y mantenida por Eric Voskuil;
- Bcoin**: una implementación de JavaScript, que ya no se mantiene activamente;
- BTCD/btcsuit**e: una implementación en Go.



Estos proyectos contribuyen a la diversidad del ecosistema, pero su adopción sigue siendo muy limitada, lo que dificulta que Bitcoin core evolucione de forma independiente.



### El poder de los desarrolladores de Core



Podría pensarse que los desarrolladores de Bitcoin core tienen control directo sobre Bitcoin, pero no es así. No pueden imponer un cambio en el protocolo. Su papel es proponer código. Corresponde a cada usuario, a través de su nodo, decidir si utiliza o no este código.



Esto significa que si un cambio en Bitcoin core no obtiene consenso, puede ser ignorado por los nodos, ya sea no actualizando Bitcoin core o simplemente cambiando la implementación. Por el contrario, si una característica deseada por los usuarios se bloquea en el proceso de desarrollo de Core, siempre es posible cambiar a otra implementación o Fork el proyecto.



Como veremos más adelante, son los nodos, en función de su peso económico (es decir, los comerciantes), los que confieren utilidad a una versión del protocolo (y, por tanto, a la moneda correspondiente), al aceptar unidades que respeten sus reglas. Por tanto, el verdadero poder de gobierno sobre Bitcoin reside en estos comerciantes, no en los desarrolladores.




# Conviértete en un bitcoiner soberano


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## ¿Por qué retorcer tu propio nudo?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Existe la creencia generalizada de que operar un nodo de Bitcoin es un acto puramente altruista, sin ningún beneficio personal, únicamente al servicio de la descentralización de la red. Algunos consideran que es una forma de deber de los bitcoiners apoyar el sistema y mostrar su gratitud a Bitcoin.



De hecho, como hemos señalado en los capítulos anteriores, no hay ningún beneficio económico directo en hacer un nudo. Por tanto, se podría pensar que no hay ningún interés personal en hacerlo. Sin embargo, dirigir su propio nodo aporta muchos beneficios individuales. Para convencerte de ello, voy a presentarte en este capítulo todas las razones, tanto técnicas como estratégicas, por las que deberías instalar y utilizar tu propio nodo Bitcoin.



### Difusión más confidencial de las transacciones



Cuando el software Wallet se conecta a un nodo externo, transmite sus transacciones a una infraestructura que no está bajo su control. Esto genera riesgos evidentes de vigilancia: el operador del nodo remoto puede analizar los detalles de sus transacciones, incluidos importes y frecuencias, y, cruzando ciertos metadatos (como direcciones IP, horas y ubicaciones), asociarlos potencialmente con su identidad.



De hecho, como se señaló en un capítulo anterior, los monederos no se comunican con la red Bitcoin por arte de magia; deben conectarse a un nodo para poder consultar saldos o difundir transacciones. Si nunca ha creado su propio nodo, esto significa que su Wallet depende de la infraestructura de un tercero (normalmente la empresa que está detrás del software). Este tercero, sobre todo si es una empresa, puede observar, explotar o incluso divulgar estos datos: ya sea por motivos comerciales, por imperativo legal o como resultado de la piratería.



![Image](assets/fr/059.webp)



Al utilizar tu propio nodo, transmites tus transacciones directamente a la red, evitando intermediarios. Siempre que asegures tu nodo adecuadamente (de lo que hablaremos más adelante) o cumplas ciertas normas, ninguna información queda expuesta: ni tu IP Address ni los detalles de tus transacciones pasan por una entidad que no controlas. Éste es un requisito básico para preservar tu confidencialidad en Bitcoin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Transacciones no censurables



Por las mismas razones mencionadas anteriormente, el software Wallet basado en un nodo de terceros es vulnerable al riesgo de censura: el operador del nodo remoto puede negarse a retransmitir determinadas transacciones por diversas razones. Puede considerarlas sospechosas o contrarias a su política. La transacción también puede bloquearse si no cumple las normas de retransmisión del nodo. Por último, el operador puede apuntar específicamente a su IP Address para bloquear la retransmisión de sus transacciones.



Por el contrario, al utilizar su propio nodo, usted garantiza la propagación de sus transacciones dentro de la red de pares. Esto significa que conservas el control total sobre la distribución de tus transacciones, sin depender de ningún intermediario. Siempre que la transacción cumpla las normas de consenso y retransmisión de los nodos conectados al suyo, se difundirá en la red y después, siempre que se incluyan suficientes comisiones, será integrada en un bloque por un Miner. Tener tu propio nodo garantiza una confirmación neutral y sin permisos de tus transacciones.



### Verificación independiente de los datos



Sin un nodo personal, sigues dependiendo de un tercero para acceder a la información, como tu saldo de Address, el estado de confirmación de las transacciones y la validez de los bloques. Esto implica una confianza implícita en la exactitud e integridad del nodo externo.



![Image](assets/fr/060.webp)



Utilizar una Full node significa que usted mismo puede comprobar todas las reglas del protocolo, para cada transacción y cada bloque. Como resultado, el saldo que muestra su Wallet no son datos recibidos de un servidor remoto, sino un resultado calculado localmente a partir de una copia completa de la Blockchain, validada bloque a bloque. Este enfoque da pleno sentido a la máxima de los bitcoiners:



> No confíes, verifica.

### Mejor distribución de la seguridad del sistema



Cada nodo que se une a la red refuerza la redundancia y resistencia de Bitcoin. Facilita la difusión de información y permite que nuevos pares se conecten entre sí. Sin los nodos, el sistema sería sencillamente inoperante.



Como hemos visto, la seguridad de Bitcoin no se basa en la descentralización, Mining o la criptografía: como cualquier sistema, depende de los individuos. Más concretamente, depende de la capacidad de los operadores de los nodos para resistir la coacción.



Lo que distingue a los sistemas descentralizados como Bitcoin es la distribución del riesgo entre todos los implicados en su funcionamiento. Dirigir tu propio nodo de Bitcoin significa aceptar una parte de este riesgo garantizando la seguridad de tu instancia; al hacerlo, también aligeras la carga de riesgo para otros operadores de nodos.



Por tanto, no se trata de un beneficio personal directo: dirigir un nodo te hace en parte responsable de la seguridad de la red. Es, sobre todo, un beneficio colectivo, porque tu participación contribuye a repartir el riesgo. A su vez, aumentas tu propia capacidad para utilizar Bitcoin de forma fiable.



### Profundizar en el conocimiento del sistema



Instalar una Full node no es una operación trivial. Implica instalar el software, comprender el funcionamiento básico, supervisar la sincronización, examinar los registros en caso de problemas e incluso utilizar el terminal. Esto le llevará necesariamente a profundizar en el conocimiento del protocolo. Se trata de una ventaja indirecta, pero no insignificante.



Adquirir estos conocimientos refuerza su confianza en la herramienta y puede reducir el riesgo de error o de exposición a estafas. Hacer tu propio nudo también es una forma de aprendizaje.



### Elección de las normas aplicables



Un aspecto importante, a menudo mal entendido, es que el funcionamiento de un nodo permite elegir las reglas que se aplican localmente. Hay dos tipos principales de reglas:





- El consenso manda**:



Estas son las reglas fundamentales del protocolo Bitcoin, que garantizan la integridad del sistema y establecen los criterios de validación de las transacciones y los bloques. Cualquier transacción que no cumpla estas reglas de consenso nunca podrá incluirse en un bloque válido. Por ejemplo, una transacción con una firma no válida en una de sus entradas será sistemáticamente excluida.



Cambiar estas reglas equivale a cambiar el protocolo y, por tanto, la moneda (Hard Fork). Sin embargo, incluso sin intentar modificarlas, el simple hecho de aplicar estrictamente las normas existentes confiere cierto poder: si un bloque infringe las normas, el nodo lo rechaza inmediatamente.





- Reglas de relevo**:



Se trata de reglas específicas de cada nodo de la Bitcoin, que se añaden a las reglas de consenso para definir la estructura de las transacciones no confirmadas aceptadas en la Mempool y retransmitidas a los pares. Cada nodo configura y aplica estas reglas localmente, lo que explica por qué pueden diferir de un nodo a otro. Sólo se aplican a las transacciones no confirmadas: una transacción considerada "no estándar" por un nodo sólo se aceptará si ya aparece en un bloque válido. La modificación de estas normas no excluye al nodo del sistema Bitcoin.



Por ejemplo, una transacción sin comisiones es, según las reglas de consenso, perfectamente válida, pero será rechazada por defecto según la política de retransmisión de Bitcoin core, porque el parámetro `minRelayTxFee` está fijado en `0.00001` (en BTC/kB). Sin embargo, es posible, en tu propio nodo, bajar este umbral para retransmitir transacciones con comisiones más bajas, o, a la inversa, aumentar el límite, por ejemplo, a 2 Sats/vB, para evitar retransmitir transacciones con comisiones bajas.



Dar vueltas a tu propio nodo significa afirmar: "Valido lo que decido validar, según las reglas que yo mismo he adoptado "*. Te conviertes así en un actor de la gobernanza del sistema, capaz de rechazar una evolución que te parece inaceptable, o de aprobar una actualización según tus propios criterios.



Así que podemos intentar comprender rápidamente cuánto poder tienes sobre las reglas gracias a tu nodo. Y el alcance de este poder dependerá del tipo de regla.



#### Para las reglas de relevo



En cuanto a las normas de retransmisión, lo esencial es simplemente poseer un nodo, independientemente de su actividad económica. Lo que está en juego es si acepta o no retransmitir determinados tipos de transacciones.



Si, por ejemplo, crees que las transacciones con tasas inferiores a 1 sat/vB deben aceptarse en Bitcoin, puedes ajustar esta regla en tu nodo para que difunda estas transacciones, facilitando así su propagación en la red hasta que un Miner acabe incluyéndolas en un bloque válido. Se trata, pues, esencialmente de una cuestión de poder sobre la difusión de las transacciones: cada nodo tiene poder de decisión, ya que aceptar retransmitir un tipo de transacción equivale a promover su aceptación en la red Bitcoin. Por consiguiente, si gestionas varios nodos, tienes una mayor influencia sobre la política de retransmisión, ya que cada nodo tiene sus propias conexiones y zonas de impacto en la red.



En efecto, tener uno o varios nodos configurados con reglas de retransmisión específicas significa determinar qué parte de la red acepta propagar un tipo de transacción dado. La propagación de un mensaje en un grafo entre pares, como es el caso de las transacciones Bitcoin, sigue la lógica de la teoría de la percolación. Imaginemos cada nodo como un sitio que puede estar activo (`p` = retransmite) o inactivo (`1-p`). En cuanto la proporción `p` cruza un umbral crítico (`p_c`), surge un componente gigante: la transacción consigue atravesar la red y tiene todas las posibilidades de llegar a una Miner. En una red como Bitcoin, en la que cada nodo mantiene una media de 8 conexiones salientes, el umbral `p_c` suele fijarse en apenas un tanto por ciento, incluso más bajo si algunos nodos tienen un número muy elevado de conexiones.



![Image](assets/fr/061.webp)



Mientras `p` se mantenga por debajo de `p_c`, una transacción permanece confinada en focos aislados y no alcanza una Miner. En cuanto se supera este umbral, se propaga casi instantáneamente por toda la red.



En última instancia, son siempre los mineros quienes deciden si incluir o no una transacción en un bloque. Sin embargo, los nodos intervienen en sentido ascendente influyendo en la distribución de las transacciones: determinan si los mineros tendrán o no conocimiento de una transacción determinada. Si una transacción no se transmite a los mineros, es obviamente imposible que éstos la incluyan en un bloque.



Por tanto, añadir unos pocos nodos más sólo tendrá un impacto marginal si la red ya se encuentra en la fase de percolación para un determinado tipo de transacción, pero puede resultar decisivo a medida que se acerca el umbral de percolación. Poseer o influir en varios nodos, especialmente si están bien conectados, puede aumentar o reducir el valor de `p` y, en consecuencia, dirigir indirectamente las reglas de retransmisión que determinan qué transacciones son vistas y finalmente aceptadas por los mineros.



#### Para las normas de consenso



Cuando se trata de la influencia de tu nodo en las reglas de consenso, su peso económico es, sobre todo, lo que será decisivo. Se trata de un concepto crucial: el valor de cualquier moneda está directamente relacionado con su capacidad para facilitar Exchange. De hecho, si un objeto no es aceptado por nadie en Exchange a cambio de bienes o servicios, teóricamente no tiene ninguna utilidad monetaria. Por ejemplo, si ningún comerciante acepta guijarros como medio de pago, no tienen utilidad como dinero. Por supuesto, la utilidad sigue siendo una noción subjetiva a escala individual, pero en un territorio dado, cuanto mayor es el número de comerciantes que aceptan un objeto como medio de Exchange, más probable es que este objeto tenga una utilidad monetaria para las personas que viven en este territorio.



Tomemos el ejemplo de un pueblo en el que muchos comerciantes aceptan oro en Exchange a cambio de mercancías: lo más probable es que el oro tenga una utilidad monetaria para los habitantes del pueblo. Esto indica que la utilidad de una moneda depende directamente de la decisión de los comerciantes de aceptarla o rechazarla.



Este concepto es crucial para entender la dinámica de poder en juego en el sistema Bitcoin. Satoshi lo deja claro: Bitcoin es un sistema de dinero electrónico; en otras palabras, proporciona un servicio que ofrece una forma de moneda, Bitcoin (o BTC). Cuando las reglas del protocolo se modifican de una forma que no es compatible con versiones anteriores (Hard Fork), esto equivale a crear un nuevo sistema y, por tanto, una nueva moneda. El éxito o el fracaso de esta Fork depende entonces del tamaño de su economía, que a su vez viene determinado por el número de comerciantes que aceptan esta nueva forma de moneda.



![Image](assets/fr/062.webp)



Pongamos un ejemplo: supongamos que Bitcoin sufre un Hard Fork. Entonces habría 2 formas distintas de moneda: BTC-1 (la versión original, sin cambios) y BTC-2 (la nueva moneda con reglas de consenso diferentes). Si todos los comerciantes que aceptaban BTC-1 siguen haciéndolo, pero rechazan BTC-2, esta última tendrá, en teoría, una utilidad monetaria muy limitada. Como usuario, no tendría ningún interés en conservar y utilizar BTC-2, sabiendo que ningún comerciante lo querría en Exchange para bienes o servicios. Por el contrario, si el 50% de los comerciantes decide aceptar exclusivamente BTC-2 y el 50% restante sólo acepta BTC-1, entonces la utilidad del BTC-1, en teoría, se habrá reducido a la mitad. Utilizo el término "en teoría" porque la utilidad sigue siendo subjetiva a nivel individual y depende de multitud de factores (como el territorio y los hábitos de consumo) que son difíciles de comprender caso por caso.



En Bitcoin, el papel de "comerciante", entendido como cualquier entidad con un cierto peso económico, incluye por supuesto a los comercios (tiendas físicas, sitios de venta online, proveedores de servicios, etc.), pero también a las plataformas de Exchange, ya que aceptan Bitcoin en Exchange por otras monedas, y a los mineros, ya que aceptan Bitcoin vía comisiones en Exchange por el servicio de incluir una transacción en un bloque.



En lo que respecta a las reglas de consenso, su nodo le permite orientar su actividad económica hacia una u otra moneda. Por ejemplo, si tienes 10 nodos completos en casa, pero ninguna actividad económica significativa, tu influencia durante una Fork será casi nula. Por el contrario, un solo nodo utilizado para gestionar una cadena de 200 tiendas que aceptan Bitcoin confiere un peso económico significativo.



Así que lo importante no es el número de nodos, sino la importancia de la actividad económica que soportan. Es más, si tu actividad económica depende de un nodo que no controlas, su propietario decidirá qué moneda utilizas, mientras sigas conectado a ese nodo. Por eso, gestionar y utilizar tu propio nodo es especialmente importante en el contexto de la gobernanza del sistema:



> Ni tu nudo, ni tus reglas.


## Los distintos tipos de nodos Bitcoin


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Un nodo Bitcoin es, por tanto, una máquina que ejecuta una implementación del protocolo Bitcoin. Detrás de esta definición común de nodos, existen varias configuraciones posibles, no todas ellas ofrecen el mismo nivel de autonomía, consumo de recursos y utilidad para la red. En este capítulo, intentaremos comprender estas diferencias para ayudarte a elegir una arquitectura de nodos que se adapte a tu uso y a tus limitaciones de hardware.



### El nudo completo



Una Full node es simplemente un nodo Bitcoin que descarga toda la Blockchain del bloque Genesis, valida cada bloque independientemente, y almacena la historia de toda esa Blockchain localmente. Esta es la forma "normal" de un nodo Bitcoin, tal y como lo imaginó Satoshi Nakamoto.



![Image](assets/fr/063.webp)



El Full node no necesita confiar en nadie porque valida y conoce toda la información del sistema. Es el tipo de nodo que le ofrece más garantías: sabe, sin depender de terceros, si un pago es válido, si un bloque es válido, si una reorganización es legítima, etc.



En la práctica, una Full node requiere recursos no triviales, incluidos varios cientos de gigabytes para archivos de bloques, un procesador capaz de validar scripts, RAM para la Mempool y cachés, y un ancho de banda estable. La primera sincronización (*IBD*) lee y verifica el historial completo: es intensiva, pero sólo ocurre una vez. Una Full node participa activamente en la red, retransmitiendo bloques y transacciones, y puede aceptar conexiones entrantes para ayudar a otros pares.



En función de sus necesidades, puede añadir un indexador a su Full node. Bitcoin core ofrece la indexación de transacciones como una función opcional (desactivada por defecto), que puede ser útil para fines específicos. Sin embargo, no incluye un indexador Address, que suele ser la función más solicitada por los usuarios particulares. Para remediarlo, puede instalar software dedicado en su nodo, como Electrs o Fulcrum, para acelerar las consultas de verificación de saldos Address de los UTXO asociados. Volveremos sobre el papel del indexador con más detalle en otro capítulo.



### El nudo pruned



El nodo pruned valida todo como Full node, desde el bloque Genesis hasta la cabeza de la cadena con más trabajo, pero **sólo conserva la parte más reciente de los archivos de bloques**. Una vez comprobados los bloques antiguos, los borra gradualmente para mantenerse por debajo de un límite de espacio que puedes establecer. Esta configuración es ideal si tiene limitaciones de espacio en disco: conserva la independencia de la validación de bloques, sin almacenar el archivo histórico completo de Blockchain. Esta opción es especialmente útil si simplemente desea instalar Bitcoin core en su ordenador personal, sin utilizar una máquina dedicada.



![Image](assets/fr/064.webp)



Las implicaciones técnicas de esta opción son bastante sencillas: el nodo pruned es perfectamente capaz de difundir sus transacciones, participar en la retransmisión, verificar bloques y transacciones, y seguir la cadena. Por otro lado, no puede servir como fuente de datos históricos más allá de sus límites para otras aplicaciones (por ejemplo, exploradores completos, indexadores, monederos). Por tanto, las funciones que requieran el archivo (o un índice global) no estarán disponibles.



En términos prácticos, puede utilizar un nodo pruned para conectar un software de gestión Wallet como Sparrow wallet. Sin embargo, no podrá escanear transacciones en su Wallet que sean anteriores al límite de poda. Por ejemplo, si tiene una transacción registrada en el bloque 901 458, pero su nodo sólo conserva los bloques del 905 402 en adelante (porque los más antiguos han sido pruned), no podrá escanear esta transacción. En cambio, si ya la había escaneado cuando su nodo aún tenía esta altura de bloque, su software de gestión Wallet almacenará la información y mostrará correctamente el saldo de los UTXO correspondientes.



En resumen, el seguimiento de Wallet funciona sin problemas en un nodo pruned si crea una nueva Wallet mientras su software ya está conectado a ese nodo. Por otro lado, puede encontrar dificultades si restaura una Wallet antigua, ya que las transacciones pasadas que ya no conserve el nodo obviamente no se podrán recuperar.



### El nudo ligero / SPV



Un nodo SPV (*Simplified Payment Verification*), o nodo ligero, conserva sólo las cabeceras de los bloques, no los detalles de las transacciones, y depende de otros nodos completos para obtener pruebas de que una transacción está en un bloque (pruebas Merkle a través de árboles) del que tiene la cabecera. El concepto de verificación simplificada de pagos no es nuevo, ya que fue propuesto por el propio Satoshi Nakamoto en la parte 8 del Libro Blanco.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Obviamente, este tipo de nodo es mucho más ligero en términos de almacenamiento y uso de CPU que un nodo Full node o incluso pruned. El nodo SPV es, por tanto, muy adecuado para dispositivos más pequeños y conexiones intermitentes. De hecho, a menudo se integra directamente en Wallet, especialmente en software móvil como Blockstream App.



La contrapartida es la confianza y la confidencialidad: un cliente SPV no comprueba los scripts ni las políticas de validación por sí mismo; asume que la cadena con más trabajo es válida, y depende de uno o varios nodos completos para obtener respuestas. Por tanto, utilizar este tipo de nodo es una opción mejor que conectarse a un nodo de terceros; sin embargo, sigue siendo menos ventajoso que tener un nodo Full node o incluso pruned.



![Image](assets/fr/065.webp)



### ¿Qué nodo para qué necesidad?





- Móvil / usuario principiante



Para un usuario novato que sólo disponga de una Wallet en una aplicación móvil, utilizar un nodo SPV es sin duda la mejor manera de empezar. La instalación es rápida, requiere pocos recursos y la experiencia es sencilla y fluida. Esto significa que usted mismo puede verificar cierta información y, por lo tanto, depender menos de nodos de terceros, siendo al mismo tiempo más independiente a la hora de emitir transacciones.





- PC / usuario intermedio



Un usuario intermedio con un PC puede instalar un nodo pruned para beneficiarse de casi todas las ventajas de un Full node, sin sobrecargar su máquina a diario: validación completa, uso moderado del disco y mantenimiento sencillo. Es una solución ideal para conectar sus monederos de sobremesa y seguir siendo independiente en la distribución de sus transacciones, sin invertir en una máquina dedicada ni sobrecargar su espacio en disco.





- Bitcoiner soberano / avanzado



Una Full node sigue siendo la mejor solución si quieres ser totalmente independiente en el uso de la Bitcoin y no limitarte más adelante a usos avanzados como un indexador, un nodo Lightning o incluso una Block explorer. ¡Eso es exactamente lo que vamos a explorar en este curso!



## Soluciones de software


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Desde el punto de vista del software, hay dos formas principales de hacer funcionar un nodo Bitcoin:




- instalar directamente una implementación de protocolo, como Bitcoin core (recomendado), o Bitcoin Knots,
- o utilizar una distribución llave en mano (a menudo denominada "_node-in-a-box_") que integra una implementación de Bitcoin del mismo modo, pero que también incluye un sistema de administración de Interface, un almacén de aplicaciones y herramientas listas para usar (Lightning, navegadores, servidores de índices, incluso aplicaciones de autoalojamiento externas a Bitcoin...).



Ambos enfoques conducen al mismo objetivo: tener tu propio nodo, pero difieren en términos de instalación y uso de Interface, mantenimiento, capacidad de ampliación y coste. Eso es lo que exploraremos en este capítulo.



### Implementaciones de nodos Bitcoin en bruto



Instalar una implementación raw significa utilizar directamente el software de una implementación de protocolo Bitcoin (como Core), sin ningún software adicional Layer. Usted mismo gestiona la configuración, las actualizaciones y los servicios asociados (indexación, API, Lightning, copias de seguridad, etc.), en función de sus necesidades.



Es el enfoque más soberano y flexible: sabes exactamente qué se está ejecutando, dónde están los datos y cómo funciona todo. Por otro lado, se vuelve más complejo en cuanto quieres ir más allá del simple funcionamiento de un nodo Bitcoin. Si tu objetivo es simplemente tener un nodo, la complejidad es comparable a la de un nodo en una caja, o incluso menor, ya que se trata simplemente de instalar software.



#### Bitcoin core (cliente ultramayoritario)



[Bitcoin core es el cliente ultramayoritario de la red](https://bitcoincore.org/). Descarga, valida y mantiene la Blockchain, proporciona APIs RPC/REST, y puede integrar una Wallet. Si prefieres las herramientas estándar y te sientes cómodo añadiendo servicios por ti mismo (como el servidor Electrum, el explorador y LND), es mejor que utilices Core tal cual.



**Beneficios:** Máxima estabilidad, comportamiento predecible, experiencia bruta, fácil de instalar y configurar.



**Desventajas:** Debes construir manualmente el resto de la pila para crear un entorno de aplicación completo, en lugar de sólo un nodo Bitcoin.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (principal cliente alternativo)



[Bitcoin Knots es un Fork de Bitcoin core](https://bitcoinknots.org/), mantenido por Luke Dashjr. Es el principal cliente alternativo a Core para implementar el protocolo Bitcoin. Totalmente compatible con el resto de la red (no es en absoluto un Hard Fork como Bitcoin Cash), ofrece sin embargo características adicionales, incluyendo opciones de política de retransmisión que están ausentes en Core, o que se aplican más estrictamente por defecto para limitar lo que algunos consideran spam.



Hay 2 posibles razones para elegir Nudos en lugar de Núcleo:




- Técnicas**: Diferentes opciones de Core, sobre todo en cuanto a la gestión de relés, determinando qué transacciones son aceptadas y difundidas por su nodo.
- Política**: Algunas personas prefieren utilizar clientes alternativos como Knots por razones no técnicas, en particular para apoyar una alternativa a Core y reducir así su monopolio. Si alguna vez Core se viera comprometido, sería útil no sólo disponer de clientes alternativos sólidos y bien mantenidos, sino también saber cómo utilizarlos eficazmente. Otros utilizan Nudos con fines de protesta, porque han perdido la confianza en los desarrolladores de Core o desaprueban la mayor parte de la gestión del cliente.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Personalmente, le recomiendo que elija Core, principalmente para beneficiarse de los parches de seguridad más rápidamente. En efecto, algunas vulnerabilidades descubiertas en Knots se corrigen con retraso. De forma más general, el proceso de desarrollo de Core está sólidamente estructurado y cuenta con el apoyo de un gran número de colaboradores, mientras que Knots es mantenido por una sola persona y cuenta con una comunidad mucho más reducida. Por otra parte, las reglas de retransmisión tienden a perder su utilidad hoy en día, sobre todo cuando sólo las aplica una pequeña fracción de la red (según la teoría de la percolación).



### Distribuciones Node-in-a-box



El _node-in-a-box_ combina Bitcoin core (o Knots) con un sistema operativo preconfigurado, una Interface Web y una App Store de servicios de autoalojamiento (Lightning, exploradores, servidor Electrum, Mempool, servidor BTCPay, Nextcloud, etc.). En un solo clic, puede instalar, actualizar e interconectar estos diferentes módulos.



Es una solución mucho más sencilla para arrancar y gestionar numerosas aplicaciones auxiliares en el día a día. El inconveniente es que cuando se produce un problema (por ejemplo, un conflicto de imagen Docker, una actualización defectuosa, una base de datos dañada), la depuración puede resultar muy compleja, ya que dependes de la propia integración de la distribución. Además, el soporte comunitario u oficial suele ser complicado.



Así pues, un nodo en una caja es extremadamente fácil de usar siempre que todo funcione correctamente, pero en caso de error, hay que estar preparado para realizar largas búsquedas, esperar ayuda y ensuciarse las manos.



La mayoría de estas soluciones están disponibles en dos formatos:




- Máquina premontada: un ordenador completo con el sistema operativo ya instalado. Estas máquinas de pago por uso sólo necesitan enchufarse a la red eléctrica y conectarse a Internet para ser operativas. Si su presupuesto se lo permite, esta opción tiene la ventaja de ser muy sencilla de configurar, ofrecer a menudo un soporte prioritario y contribuir a la financiación del desarrollo, ya que el modelo de negocio de estas empresas se basa generalmente en la venta de hardware.
- DIY: instala el SO de la distribución en tu propia máquina (PC antiguo, NUC, Raspberry Pi, servidor doméstico...). Esta es la solución más económica, ya que puedes reciclar una máquina vieja o elegir el hardware que se ajuste exactamente a tus necesidades y presupuesto. También es la opción más flexible y la más satisfactoria de configurar. Este es el enfoque que exploraremos en la parte práctica del curso.



He aquí un resumen de las principales soluciones "node-in-a-box" disponibles (en 2025):



### Umbrel (umbrelOS y Umbrel Home)



[Hoy en día, Umbrel es el líder en soluciones node-in-a-box (https://umbrel.com/). Su éxito se debe en gran medida a la sencillez de su instalación (cuando se lanzó en una simple Raspberry Pi), a su elegante e intuitivo Interface, y a un ecosistema de aplicaciones que ha crecido rápidamente y ahora es amplísimo.



![Image](assets/fr/067.webp)



Lanzado en 2020 como un simple nodo Bitcoin acompañado de unas pocas aplicaciones auxiliares, Umbrel ha evolucionado gradualmente hasta convertirse en una nube doméstica completa y moderna.



No voy a entrar aquí en más detalles sobre su funcionamiento y sus características específicas, ya que las examinaremos en mayor profundidad en el primer capítulo de la siguiente parte. De hecho, para los propósitos de este curso BTC 202, he optado por utilizar UmbrelOS, que creo que es la mejor solución actual node-in-a-box para usuarios principiantes e intermedios.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 ofrece StartOS (https://start9.com/), un sistema diseñado para la "informática soberana": el objetivo es que todo el mundo posea y gestione su propio servidor privado, potenciado por un mercado de aplicaciones autoalojadas. Puedes comprar un servidor Start9 (Server One a 619 $, Server Pure a 899 $) o montar el tuyo propio en modo DIY en tu propia máquina.



Por el lado de Bitcoin, StartOS permite instalar una Full node, un nodo Lightning, BTCPay Server, Electrs y muchos otros servicios. Sin embargo, el atractivo de Start9 va más allá: ofrece la posibilidad de descubrir, configurar y exponer diversos programas (nube de archivos, mensajería, monitorización) de forma unificada, con un control total. El proyecto se dirige, por tanto, a los usuarios que desean una plataforma robusta de autoalojamiento, no un simple nodo Bitcoin. Es probablemente el ecosistema más completo después de Umbrel.



![Image](assets/fr/068.webp)



La principal diferencia con Umbrel radica en la Interface. Umbrel apuesta por una UX muy pulida, mientras que Start9 ofrece un Interface más tosco y funcional. El ecosistema de aplicaciones de Start9 es menos rico que el de Umbrel, pero lo compensa con varias ventajas técnicas: el acceso a la configuración avanzada de las aplicaciones está simplificado, mientras que Umbrel se vuelve rápidamente restrictivo si la opción deseada no la proporciona el Interface. Start9 también destaca en la gestión de copias de seguridad: aparte de la eficaz solución de Umbrel para LND, no existe ningún mecanismo unificado, a diferencia de Start9. Además, ofrece herramientas de supervisión más accesibles y una conexión remota cifrada (`https`), mientras que el acceso local a Umbrel se realiza mediante `http`.



En resumen, si usted simplemente necesita las aplicaciones esenciales para Bitcoin, sin ningún interés particular en el muy rico ecosistema de Umbrel, y el usuario de Interface no es una prioridad, entonces Start9 es una mejor opción. De lo contrario, Umbrel es la mejor opción.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MiNodo



[MyNode es una distribución centrada exclusivamente en Bitcoin y Lightning](https://mynodebtc.com/), que ofrece una Interface web, un mercado de aplicaciones y actualizaciones con un solo clic. Puedes comprar hardware listo para usar (*Modelo Dos* disponible a 549 dólares) o instalar MyNode gratuitamente en tu propia máquina. El proyecto también ofrece una versión *Premium* del software (94 $), que incluye soporte prioritario y funciones avanzadas.



![Image](assets/fr/069.webp)



En la práctica, MyNode reúne todos los elementos básicos necesarios para hacer funcionar una Full node, así como las aplicaciones esenciales para los usuarios de Bitcoin. Por lo tanto, es una solución adecuada si no necesitas aplicaciones externas al ecosistema de Bitcoin, como las apps autoalojadas que se encuentran en los sistemas Start9 y Umbrel.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz es un proyecto 100% de código abierto](https://docs.raspiblitz.org/) (licencia MIT) para montar un nodo Bitcoin y un nodo Lightning en una Raspberry Pi. Simplemente descarga la imagen, arranca y sigue el asistente para tener un nodo en una caja funcionando en tu Raspberry Pi. También hay disponibles kits premontados de terceros, normalmente entre 300 y 400 dólares, dependiendo del hardware. RaspiBlitz también ofrece una gama de aplicaciones adicionales, fáciles de instalar.



![Image](assets/fr/070.webp)



Si posees una Raspberry Pi, esta es una excelente opción, ya que sistemas más completos como Umbrel son cada vez más pesados para este tipo de mini-PC.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo es un node-in-a-box](https://wiki.ronindojo.io/en/home) centrado en la privacidad que automatiza el despliegue de Samurai Dojo y Whirlpool, con un Interface dedicado y plugins diseñados específicamente para el ecosistema Samurai.



El principio es simple: si utilizas Ashigaru Wallet (el sucesor de Samurai Wallet, tras el arresto de sus desarrolladores) o si quieres beneficiarte de herramientas avanzadas de privacidad, RoninDojo es para ti.



![Image](assets/fr/071.webp)



El proyecto ofrecía anteriormente una máquina preconfigurada llamada Tanto, pero actualmente no está disponible. Puede que vuelva más adelante. Mientras tanto, es posible instalar fácilmente RoninDojo en una Rock5B+ o Rockpro64, o incluso indirectamente en una Raspberry Pi.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Otra solución [node-in-a-box es Nodl](https://www.nodl.eu/). Como en los proyectos anteriores, puedes comprar el hardware preconfigurado (entre 599 y 799 euros, según el modelo) o instalarlo tú mismo en modo bricolaje.



En cuanto al software, Nodl integra Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, así como BTC RPC Explorer, todo ello con una cadena de actualización integrada y código abierto bajo licencia MIT.



![Image](assets/fr/072.webp)



Una vez exploradas las distintas soluciones de software, es hora de elegir la máquina que alojará tu nodo




## Resumen de soluciones de hardware


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Ahora que ya hemos explorado todas las posibilidades del software, centrémonos en el hardware necesario para tu nodo. Te daré algunos consejos concretos para seleccionar tus componentes, junto con configuraciones adaptadas a diferentes presupuestos. Por supuesto, ésta es mi opinión personal: sin duda existen otras alternativas relevantes además de las aquí presentadas. Además, no volveré sobre las máquinas premontadas que ofrecen los proyectos de nodos en caja, que ya hemos tratado en el capítulo anterior. Aquí nos centraremos exclusivamente en las soluciones de bricolaje.



### ¿Realmente necesitas una máquina dedicada?



En los últimos años, los bitcoiners han sido cada vez más conscientes de un error común, sobre todo con la popularización de los node-in-a-box a principios de la década de 2020: un nodo Bitcoin debe funcionar necesariamente en una máquina dedicada exclusivamente a este fin. Pero esto no es cierto. No se necesita necesariamente un ordenador dedicado para ejecutar un nodo Bitcoin: Bitcoin core es perfectamente capaz de funcionar en su PC de todos los días. Si dispone de suficiente espacio en disco para Blockchain o activa la poda, puede validar la cadena, conectar su Wallet e incluso cerrar el programa cuando termine de utilizarlo. La ventaja de este enfoque es considerable: inversión inicial cero y complejidad mínima.



![Image](assets/fr/074.webp)



Dicho esto, utilizar una máquina dedicada suele ser más cómodo. Puede funcionar continuamente (24/7), ser accesible remotamente en todo momento, no monopolizar los recursos de tu máquina principal y, sobre todo, aislar los usos (una buena práctica de seguridad: si tu PC personal tiene un problema, tu nodo sigue funcionando, y viceversa). Así que la pregunta no es "¿Necesito dedicar una máquina?", sino más bien "¿Necesito un nodo que esté constantemente en línea, accesible por otros dispositivos y capaz de evolucionar?" (Lightning, indexadores, aplicaciones adicionales...). Si la respuesta es afirmativa, optar por una máquina independiente simplificará mucho las cosas.



### 3 métodos de adquisición: reciclaje, segunda mano y nuevo



#### Reciclar un PC antiguo



Es la solución más económica. La mayoría de nosotros tenemos un viejo PC reuniendo Dust en casa, o con amigos y familiares: ¡esta es la oportunidad perfecta para volver a ponerlo en servicio! Para adaptarlo para su uso como nodo Bitcoin, basta con añadir un SSD de 2 TB y, en función de sus necesidades, sustituir o añadir barras de RAM para aumentar la memoria RAM. Espere pagar entre 100 y 200 euros por una máquina completamente funcional.



Antes de comprar cualquier hardware, comprueba el número de ranuras de disco disponibles, el tipo de conexión (M.2 o SATA), el formato de la RAM (SODIMM o DIMM) y su generación (DDR4, etc.). También deberías aprovechar para limpiar la máquina, especialmente el ventilador, para garantizar un rendimiento óptimo.



Ten cuidado, sin embargo, si utilizas un portátil: la batería puede convertirse en un problema con el tiempo (más sobre esto más adelante en el capítulo).



#### Reacondicionado o usado



El mercado está lleno de mini PC profesionales reacondicionados como *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* o *Dell OptiPlex Micro*. Estas máquinas son sólidas, compactas, silenciosas y energéticamente eficientes. Su precio está muy por debajo del de los nuevos, y es fácil encontrar modelos equipados con procesadores i5/i7 de 6ª a 10ª generación y de 8 a 16 GB de RAM, todo ello por precios muy atractivos, generalmente entre 70 y 200 euros, según la configuración. En mi opinión, esta es probablemente la mejor opción si buscas una máquina dedicada para tu nodo Bitcoin.



![Image](assets/fr/075.webp)



También es posible encontrar PC y portátiles usados de hace unos años, con configuraciones interesantes y una excelente relación calidad-precio.



**Nota:** las máquinas de flotas corporativas, como el *ThinkCentre Tiny*, a menudo sólo están equipadas con un puerto *DisplayPort* (DP) para la pantalla, sin salida HDMI. Así que no olvides traer un adaptador o un cable DP a HDMI si lo necesitas.



#### Comprar nuevo



Si tu presupuesto te lo permite, también puedes optar por una máquina nueva. Esta es una buena opción si desea disponer de hardware reciente con un buen rendimiento, especialmente si planea utilizar Umbrel o Start9 con aplicaciones adicionales fuera del ecosistema Bitcoin para autoalojarse.



### ¿Qué tipo de máquina debo elegir?



#### Mini PC "NUC" / barebone



En mi opinión, los mini PC son la mejor solución para alojar un nodo Bitcoin en casa. Ahorran espacio, caben fácilmente en una estantería, consumen un mínimo de energía y se prestan a modificaciones de hardware sencillas, como añadir RAM o sustituir el SSD.



Personalmente, prefiero los *Lenovo ThinkCentre Tiny*, muy extendidos en el mercado de segunda mano (procedentes de flotas de empresas); son especialmente robustos y fáciles de modificar. Por supuesto, hay muchos equivalentes de otros fabricantes: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*...



![Image](assets/fr/001.webp)



**Destacables:** tamaño reducido, consumo moderado, bajo nivel de ruido, escalabilidad (según el modelo) y fiabilidad.



**Debilidades:** ligeramente más caro que un SBC tipo Raspberry Pi, sin pantalla integrada (acceso remoto o mediante monitor externo), sin batería (apagado repentino en caso de corte de corriente).



#### Portátil dedicado



Es una excelente alternativa económica al mini-PC: hoy en día, se pueden encontrar portátiles de segunda mano o incluso nuevos a bajo precio, equipados con procesadores decentes, numerosos puertos, así como una pantalla y un teclado integrados (muy prácticos para la instalación inicial). Sobre todo, la batería actúa como un SAI natural: en caso de corte de corriente, el nodo no se apaga bruscamente, e incluso puede permanecer operativo durante varias horas.



![Image](assets/fr/076.webp)



**Destacables:** Solución todo en uno, la batería actúa como SAI (sin apagones), instalación simplificada gracias a una pantalla y un teclado integrados, una tarjeta Wi-Fi integrada y una amplia oferta de mercados de segunda mano y nuevos (lo que a menudo significa que puede negociar los precios).



**Puntos débiles:** consumo de energía ligeramente superior al de un mini PC desnudo, desgaste gradual de la batería en funcionamiento 24/7 con pérdida de capacidad, riesgo poco frecuente pero real de hinchamiento de la batería o desbocamiento térmico con la edad. Es principalmente este aspecto el que me hace considerar el mini PC una mejor opción que el portátil: la degradación gradual de la batería y los riesgos asociados.



Si optas por esta solución, te recomiendo que vigiles de cerca el estado de la batería para prevenir cualquier peligro. Esté atento a la aparición de calor excesivo, olores extraños, inestabilidad o una carcasa deformada. En caso de alarma, apague y desenchufe el ordenador inmediatamente y, a continuación, deseche la batería en un centro de reciclaje especializado.



**Consejo:** Si BIOS/UEFI o la herramienta del fabricante lo permiten, establece un límite de carga (por ejemplo, 60% u 80%) para alargar la vida de la batería.



#### Raspberry Pi y otros SBC: la idea equivocada



A principios de la década de 2020, con el auge del software node-in-a-box, surgió también la moda de Raspberry Pi como medio para hacer funcionar un nodo Bitcoin. La idea parecía atractiva: barata, compacta y accesible.



![Image](assets/fr/073.webp)



En la práctica, si tu objetivo es únicamente ejecutar un nodo Bitcoin sin aplicaciones adicionales, una Raspberry Pi puede ser suficiente. Pero en cuanto quieras utilizar Umbrel, Start9 o un ecosistema más rico (Block explorer, indexador Address, nodo Lightning, aplicaciones de autoalojamiento...), la máquina alcanza rápidamente sus límites.



La Raspberry Pi tiene una serie de desventajas:




- procesadores demasiado delgados, con una arquitectura ARM que a veces es incompatible con cierto software o requiere más manipulación;
- RAM soldada, imposible de actualizar, con configuraciones limitadas (a menudo un máximo de 8 GB);
- cajas externas para SSD conectadas por cable, fuentes frecuentes de fallos, que requieren la compra de una tarjeta específica para un SSD estable;
- tendencia a calentarse rápidamente y dificultad para garantizar un enfriamiento correcto;
- necesidad de adquirir hardware adicional (carcasa, ventilador, tarjeta SSD, etc.);
- conectividad muy limitada.



Históricamente, la gran ventaja de los SBC como el Raspberry Pi era su precio: por unas decenas de euros, podías conseguir una máquina dedicada. Sin embargo, hoy en día, los precios han subido mucho y, una vez añadido todo el hardware adicional imprescindible, el coste se acerca al de los primeros mini PC x86 usados o reacondicionados, que, en mi opinión, ofrecen muchas más ventajas. Por esta razón, no recomiendo optar por un SBC.



### Selección de componentes



#### Almacenamiento en disco: SSD obligatorio, 2 TB mínimo



Técnicamente, es posible ejecutar un nodo Bitcoin en un HDD. El problema es que todo se ralentizará considerablemente, especialmente el IBD, que se hará extremadamente largo debido al uso intensivo que Bitcoin core hace del disco como caché (especialmente para el conjunto UTXO). Por eso desaconsejo encarecidamente el uso de un HDD: crea un verdadero cuello de botella, limita gravemente la evolución futura (por ejemplo, para un nodo Lightning), y puede incluso provocar un desajuste de sincronización con la cabeza Blockchain. Además, el estrés constante sobre el disco mecánico aumenta el riesgo de desgaste prematuro.



Las unidades SSD cambian radicalmente su experiencia de usuario: todo se vuelve más rápido y fluido, con una fiabilidad mucho mayor. Por tanto, el uso de una unidad SSD es (casi) obligatorio para tu nodo, y no te arrepentirás, sobre todo porque los modelos de alta capacidad son ahora relativamente asequibles.



![Image](assets/fr/077.webp)



En términos de capacidad, los 2 TB se están estableciendo gradualmente como el nuevo mínimo razonable. En el verano de 2025, Blockchain ya se acerca a los 700 GB, y si añades Umbrel, un indexador Address y unas cuantas aplicaciones, un SSD de 1 TB se saturará rápidamente. Con 2 TB, tienes un cómodo margen para los próximos años (en una estimación amplia, entre 5 y 15 años). También puedes optar por 4 TB si piensas utilizar muchas aplicaciones en Umbrel, almacenar archivos de gran tamaño en autoalojamiento o si quieres anticipar en gran medida tus necesidades de espacio en disco.



![Image](assets/fr/078.webp)



En cuanto al formato, esto dependerá de los puertos disponibles en tu máquina; sin embargo, si es posible, recomiendo usar un SSD M.2 NVMe.



#### Memoria (RAM): 8 a 16 GB



Para Bitcoin core solo (sin superposición de Umbrel), las recomendaciones del desarrollador indican un mínimo de 256 MB de RAM con la configuración ajustada al mínimo, 512 MB con la configuración predeterminada y 1 GB para un uso normal.



Por otro lado, si utilizas un sistema node-in-a-box como Umbrel o Start9, los requisitos de RAM son significativamente mayores. Los desarrolladores de Umbrel recomiendan un mínimo de 4 GB de RAM. Esto puede ser suficiente para ejecutar sólo Core, pero pronto estarás limitado. Por lo tanto, recomiendan 8 GB, que también considero el mínimo para una configuración básica en torno a Bitcoin (Core, LND, indexador y unas pocas aplicaciones). En mi experiencia, con Umbrel y algunos servicios adicionales, 8 GB siguen siendo un poco justos. Para estar realmente cómodo y tener algo de margen, recomendaría 16 GB de RAM.



#### Procesador (CPU)



Para un nodo Umbrel, el requisito mínimo es un procesador dual-core de 64 bits de Intel o AMD. Si quieres utilizar algunas aplicaciones además de Bitcoin core, un procesador de cuatro núcleos (o superior) marcará una verdadera diferencia en términos de fluidez. Por ejemplo, los procesadores i5/i7 de 6ª a 10ª generación son excelentes opciones en el mercado de segunda mano.



### Ejemplos de configuraciones concretas



A continuación, propongo tres configuraciones concretas, adaptadas a distintos presupuestos y necesidades, con modelos precisos para apoyarlas. Estas opciones se ofrecen como ejemplos para ilustrar la información de este capítulo; no tienes ninguna obligación de elegir exactamente estos modelos. Como considero que el mini PC es la mejor opción a largo plazo, me basaré en este formato para las tres configuraciones propuestas.



*Los precios que figuran a continuación son indicativos y pueden variar según la región, el vendedor y el periodo*



En primer lugar, necesita una unidad SSD lo bastante grande para alojar la Blockchain, pero que deje margen de maniobra. Las SSD tienen una vida útil limitada en cuanto a ciclos de escritura y volumen total de datos escritos. Sin embargo, un nodo Bitcoin supone una carga importante para el disco al escribir. Por eso no recomiendo los modelos básicos; en su lugar, sugiero una SSD NVMe, que ofrece un rendimiento significativamente mejor.



Como ejemplo, para los propósitos de este curso, he elegido el siguiente modelo: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, disponible por unos 120 euros en Amazon. También puedes optar por otras marcas conocidas como Crucial, Western Digital o Kingston.



![Image](assets/fr/046.webp)



#### Configuración de bajo presupuesto



Evidentemente, si tu presupuesto es muy limitado (menos de 200 euros), te aconsejo que no inviertas en una máquina dedicada, sino que instales Bitcoin core directamente en tu PC de uso cotidiano (en modo pruned si te falta espacio en disco).



Por lo demás, para un presupuesto básico, recomiendo el *HP EliteDesk 800 G2 Mini*. Encontré un modelo reacondicionado por 96 € en Amazon, equipado con un procesador Intel Core i5 de 6ª generación y 8 GB de RAM. Se trata de una opción especialmente interesante para principiantes: este procesador y esta cantidad de memoria son más que suficientes para ejecutar Core en Umbrel, así como varias aplicaciones simultáneamente, como un indexador Electrs, un nodo Lightning y una instancia Mempool, siempre que no asignes demasiada caché a Core. Además, este tipo de mini PC permite aumentar fácilmente la memoria RAM a 16 GB, por ejemplo, en caso necesario (hay que pagar unos 30-40 euros más por uno o dos lápices de memoria de calidad).



![Image](assets/fr/045.webp)



A continuación, basta con añadir el SSD al presupuesto. Empezando con el Samsung de 2 TB a 120 €, obtenemos un coste total de 216 € para una máquina completa y funcional.



#### Configuración de presupuesto medio



Si tienes un presupuesto medio de unos 300 € para la máquina que alojará tu nodo, te recomiendo un *Lenovo ThinkCentre Tiny*, por ejemplo, equipado con un procesador de alto rendimiento y suficiente RAM. Encontré un modelo reacondicionado en Amazon por 180 euros, con un procesador Intel Core i7 de 6ª generación y 16 GB de RAM. Si añadimos el SSD de 2 TB a 120 €, el coste total asciende a 300 €.



![Image](assets/fr/044.webp)



Con esta máquina, tienes una configuración cómoda: un IBD rápido y la capacidad de ejecutar numerosas aplicaciones en tu Umbrel o Start9 sin dificultad. Esta es precisamente la configuración que estoy utilizando para este curso BTC 202.



#### Configuración de gama alta



Con un presupuesto mayor, las posibilidades se amplían considerablemente. Puedes elegir una configuración DIY, o incluso optar por una máquina premontada ofrecida directamente por un proyecto node-in-a-box.



Por ejemplo, el *ASUS NUC 14 Pro* está disponible nuevo en Amazon por 540 euros. Por este precio, obtienes un procesador Intel Core Ultra 5 (reciente y particularmente de alto rendimiento), acompañado de 16 GB de RAM DDR5. Con una configuración así, podrás completar un IBD en un tiempo récord e instalar aplicaciones exigentes sin dificultad.



Se trata de una configuración extremadamente cómoda, incluso excesiva si el objetivo inicial es simplemente ejecutar un nodo Bitcoin. Por otro lado, si quieres aprovechar al máximo todas las aplicaciones de autoalojamiento disponibles en Umbrel y Start9, este nivel de potencia es el adecuado para ti.



![Image](assets/fr/043.webp)



Dependiendo del uso que le vaya a dar, puede optar por una unidad SSD de 2 TB, como en las otras configuraciones, o directamente por una unidad SSD de 4 TB a 260 euros si también desea almacenar archivos personales y ampliar sus usos de autoalojamiento. Con un SSD de 2 TB, el coste total de la configuración es de 660 €, mientras que con un SSD de 4 TB, alcanza los 800 €.



### Algunos consejos más





- Si quieres comprar material de segunda mano y pagar en bitcoins, ¡acércate a un encuentro cerca de ti! Charlando con otros participantes, seguro que encuentras equipos adecuados a buen precio, al tiempo que contribuyes a mantener viva la economía circular en torno a la Bitcoin. También es una oportunidad para beneficiarse de los buenos consejos de la comunidad.





- Para la conexión a Internet necesitarás, por supuesto, un cable Ethernet RJ45, al menos para la instalación del sistema.





- Algunos entornos, como Umbrel, permiten entonces utilizar Wi-Fi, pero el rendimiento será generalmente inferior (especialmente si desea utilizar su nodo Lightning de forma remota, ya que esto puede repercutir). Si eliges Wi-Fi, asegúrate de que tu máquina tiene una tarjeta integrada o añade un dongle compatible.





- Utilice siempre el Supply original del fabricante para su máquina. Esto es crucial para evitar daños en su equipo y prevenir el riesgo de provocar un incendio.





- Si tu máquina no tiene batería incorporada, es buena idea invertir en un inversor para evitar apagones repentinos.





- En función del valor de sus equipos y de su situación geográfica, también puede ser conveniente instalar un sistema pararrayos, ya sea directamente en el cuadro eléctrico o en la regleta utilizada.





- Por último, recuerda optimizar la refrigeración de tu máquina: límpiala con regularidad e instálala en un lugar fresco, bien ventilado y despejado para evitar el sobrecalentamiento, que podría provocar el throttling (limitación voluntaria de la velocidad de tu procesador).



# Instalación sencilla de un nodo Bitcoin


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: mucho más que un nodo Bitcoin


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel es un sistema operativo de servidor personal diseñado para hacer accesible el autoalojamiento: instalas Umbrel, abres un navegador en `umbrel.local`, y gestionas todo a través de un sencillo Interface remoto.



El proyecto popularizó primero la idea de un nodo Bitcoin y Lightning con un solo clic, y luego se amplió hasta convertirse en una auténtica "nube doméstica": almacenamiento de archivos y fotos, streaming multimedia, herramientas de red, domótica, IA local y cientos de aplicaciones instalables desde una App Store integrada.



En Umbrel, cada aplicación se ejecuta en un contenedor Docker (aislamiento, actualizaciones atómicas, inicio/parada independientes). Interface centraliza el acceso a todas estas aplicaciones, ofreciendo inicio de sesión único (con 2FA opcional), actualizaciones con un solo clic para el sistema operativo y las aplicaciones, supervisión en directo de la máquina (CPU, RAM, temperatura, almacenamiento), gestión de permisos entre aplicaciones y una visión general de su consumo.



El objetivo de Umbrel es, por tanto, devolverle el control y la confidencialidad sobre sus datos, sin depender de servicios en la nube, más allá del simple funcionamiento de un nodo Bitcoin.



### Umbrel Home vs umbrelOS



Umbrel ofrece dos enfoques distintos:





- [Umbrel Home**](https://umbrel.com/umbrel-home): se trata de un miniservidor listo para usar, especialmente diseñado y optimizado para umbrelOS. Compacto, silencioso, conectado a Ethernet, está equipado con un SSD NVMe (hasta 4 TB opcional), 16 GB de RAM y una CPU de cuatro núcleos. Lo pides, lo conectas y entras en `umbrel.local`. Puedes tener un Umbrel operativo y funcionando en cuestión de minutos. Esa es la opción plug-and-play.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): es el sistema operativo que puedes instalar tú mismo en tu propio hardware (mini-PC, NUC, torre, portátil dedicado...). Tienes el mismo Interface y el mismo App Store que en Umbrel Home.



![Image](assets/fr/080.webp)



En ambos casos, la experiencia del usuario es idéntica en lo que respecta al software: administración basada en navegador, actualizaciones con un solo clic, instalación de aplicaciones a la carta... La solución DIY es a menudo más económica que la compra de un Umbrel Home (dependiendo de la máquina utilizada). Sin embargo, yo no recomendaría necesariamente optar siempre por la opción DIY, ya que **comprar un Umbrel Home contribuye directamente a financiar el desarrollo del proyecto**, puesto que su modelo de negocio se basa en la venta de hardware. Y, francamente, a 389 euros por 2 TB de almacenamiento, el precio sigue siendo muy razonable dada la calidad de la máquina que se ofrece.



![Image](assets/fr/079.webp)



En el próximo capítulo, exploraremos cómo instalar umbrelOS DIY en tu propia máquina. Sin embargo, puedes seguir este curso BTC 202 de la misma manera si has optado por un Umbrel Home.



### Caso práctico: del nodo Bitcoin a la nube doméstica



Umbrel puede seguir siendo muy minimalista y centrarse únicamente en Bitcoin, o evolucionar hasta convertirse en un auténtico servidor personal multifuncional, en función de tus necesidades. Estos son los principales usos de Umbrel:





- Nodo Bitcoin simple**: este es el uso fundacional en el que Umbrel se ha basado desde el principio. Puedes ejecutar Bitcoin core (o Knots), conectar tus monederos directamente a tu nodo, exponer un servidor de Electrum, alojar tu Mempool Block explorer para ver el Blockchain, y estimar cargos... Son estos usos en los que nos centraremos en este curso.



![Image](assets/fr/082.webp)





- Lightning Network**: Umbrel también te permite desplegar LND o Core Lightning, dos implementaciones de Lightning Network, para gestionar tu propio nodo Lightning. Podrá abrir canales, gestionar su liquidez, realizar pagos, automatizar el balanceo, ofrecer servicios, conectar una Wallet remota o aprovechar la gestión avanzada de Interface gracias a las numerosas aplicaciones disponibles. Veremos este caso de uso específico en nuestro próximo curso LNP 202.



![Image](assets/fr/083.webp)





- Autoalojamiento general**: con Nextcloud, Immich, Jellyfin/Plex, bloqueadores de publicidad a nivel de DNS (Pi-hole/AdGuard), VPNs (WireGuard, Tailscale), domótica (Home Assistant), copias de seguridad, gestión de notas, herramientas de oficina, IA local (Ollama + Open WebUI)... Umbrel puede convertirse en tu servidor personal, permitiéndote recuperar el control de tus datos. Usted mismo aloja los servicios que utiliza a diario, con una experiencia de usuario pulida que se asemeja mucho a las soluciones externas, al tiempo que conserva el control total sobre sus datos y su privacidad.



Al desplegar aplicaciones en contenedores, puede dar a Umbrel la forma que desee: empiece con un simple nodo Bitcoin y unas cuantas aplicaciones vinculadas a su ecosistema, luego instale un nodo Lightning junto a su nodo Bitcoin y enriquezca gradualmente su instancia con las aplicaciones autoalojadas que necesite.



### Comunidad y ayuda mutua



Una de las principales ventajas de Umbrel frente a sus competidores es su amplia y activa comunidad de usuarios. Puedes contactar con ellos principalmente a través de [su Discord](https://discord.gg/efNtFzqtdx) y [su foro en línea](https://community.umbrel.com/). Aquí no sólo encontrarás consejos prácticos, sino sobre todo soluciones para resolver problemas o corregir errores. Es un buen lugar para empezar, progresar y, finalmente, ayudar a otros usuarios, para que no te quedes solo con tu Coin.



![Image](assets/fr/084.webp)



### Licencia UmbrelOS



El código de umbrel está disponible públicamente (puedes verlo, Fork, y modificarlo), pero no está bajo una verdadera licencia de código abierto. De hecho, umbrelOS se distribuye bajo la licencia [*PolyForm Noncommercial 1.0*] (https://polyformproject.org/licenses/noncommercial/1.0.0/), aunque algunas herramientas de desarrollo asociadas están disponibles bajo la licencia MIT.



En la práctica, puedes hacer prácticamente lo que quieras con umbrelOS, siempre que sea para uso personal y no comercial: modificación, redistribución con fines no lucrativos, creación de derivados para ti mismo o para organizaciones sin ánimo de lucro, siempre que respetes los avisos legales.



Sin embargo, está prohibido vender Umbrel o sus derivados (por ejemplo, una máquina premontada con umbrelOS preinstalado), ofrecer comercialmente servicios relacionados con Umbrel o integrar su código en un producto con ánimo de lucro.



Técnicamente, esta licencia no restringe la instalación, auditoría o adaptación de Umbrel para uso personal. Desde el punto de vista legal, protege el proyecto contra la reventa no autorizada o el alojamiento comercial, especialmente por parte de proveedores de servicios en la nube. Umbrel no es, por tanto, de código abierto, aunque su código sigue siendo de acceso público.



Sin embargo, cada aplicación de la Tienda conserva su propia licencia, a menudo de código abierto.




## Instalación de un Full node con paraguas


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Ahora que tenemos toda la información necesaria, es hora de profundizar en los detalles. En este tutorial, te mostraremos cómo instalar un nodo Bitcoin completo usando UmbrelOS.



### Material necesario



Aquí utilizaremos la imagen UmbrelOS x86 (más concretamente, la versión x86_64). Podrás seguir esta guía en cualquier máquina que elijas, siempre y cuando no esté equipada con un procesador de arquitectura ARM (nada de Apple Silicon, Raspberry Pi, etc.). Esto significa que cualquier ordenador con un procesador Intel o AMD de 64 bits será suficiente, siempre y cuando cumpla los requisitos mínimos, dependiendo del uso que pretendas darle a tu Umbrel (se recomienda al menos un procesador de doble núcleo).



Si has optado por una Raspberry Pi 5 (una opción que no recomiendo, como se menciona en la sección anterior), la instalación es ligeramente diferente. A continuación, puede seguir este tutorial dedicado y volver a mi curso una vez en la web Interface `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Como mencioné en la sección anterior, elegí ejecutar este tutorial en un pequeño PC reacondicionado que encontré a buen precio: un *Lenovo ThinkCentre M900 Tiny* equipado con un procesador Intel Core i7 y 16 GB de RAM. Se trata de una configuración muy cómoda para ejecutar Umbrel, especialmente para un nodo Bitcoin. Sin embargo, he elegido esta configuración porque quiero instalar un nodo Lightning y otras aplicaciones más exigentes más adelante. También he añadido un SSD de 2 TB a mi ThinkCentre para conservar el Blockchain completo y seguir teniendo un margen cómodo. Con esta configuración, el coste total es de 270 euros, incluidos todos los gastos.



![Image](assets/fr/001.webp)



Me gusta especialmente la gama ThinkCentre Tiny de Lenovo, ya que son máquinas compactas, silenciosas y muy robustas. Estos ordenadores son muy populares entre las empresas, por lo que abundan en el mercado de segunda mano, donde se pueden encontrar configuraciones interesantes entre 70 y 200 €.



Si, como yo, has optado por un PC sin monitor, **necesitarás conectar un monitor y un teclado** sólo mientras dure la instalación. Después, podrás acceder a él a distancia desde otro ordenador de la misma red (o mediante otros métodos que veremos en capítulos posteriores). También necesitarás un cable Ethernet RJ45 para conectar tu máquina a la red local, y una memoria USB de al menos 4 GB para almacenar la imagen de instalación.



Para recapitular, estos son los requisitos de equipamiento:




- Ordenador con procesador x86_64 (mínimo Dual-core, recomendado Quad-core);
- Memoria RAM (4 GB mínimo, 8 GB recomendado o más para un uso prolongado);
- SSD (recomendado + 2 TB);
- Llave USB (+ 4 GB) para la instalación de la imagen UmbrelOS;
- Monitor y teclado (útil sólo para la instalación inicial si el PC no está equipado con uno);
- Cable Ethernet RJ45.



### Paso 1 - Montaje del ordenador



Dependiendo del hardware que hayas elegido, el primer paso es ensamblar los distintos componentes de tu ordenador. Por ejemplo, en mi caso, el SSD original tenía una capacidad de sólo 256 GB, así que lo reciclaré para darle otro uso y lo sustituiré por un SSD de 2 TB. Si también quieres sustituir los módulos de RAM, ahora es el momento de hacerlo.



### Paso 2: Preparar una llave USB de arranque



Antes de instalar UmbrelOS en tu máquina, necesitarás crear una llave USB de arranque que contenga el sistema operativo. Todos los pasos del paso 2 deben realizarse en tu ordenador personal (y no directamente en el ordenador destinado a convertirse en tu nodo).





- Empieza descargando la última versión de UmbrelOS en formato USB:



Vaya a [la página web oficial de Umbrel para descargar la imagen ISO](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) para la instalación mediante llave USB. Asegúrate de seleccionar la versión compatible con la arquitectura x86_64 (archivo llamado `umbrelos-amd64-usb-installer.iso`). La descarga puede llevar algún tiempo, ya que la imagen es bastante grande.



![Image](assets/fr/002.webp)





- Instalar Balena Etcher:



Para crear la memoria USB de arranque, utilizarás una sencilla herramienta multiplataforma llamada [Balena Etcher](https://www.balena.io/etcher/). Descárgala e instálala en tu ordenador.



![Image](assets/fr/003.webp)





- Inserte una memoria USB en blanco de al menos 4 GB:



Conecta una llave USB a tu ordenador (aquella en la que acabas de descargar la imagen de UmbrelOS y Balena Etcher). **Advertencia: todos los datos de la llave se borrarán**. Asegúrate de que no contiene ningún archivo importante.





- Graba la imagen ISO en la memoria USB con Balena Etcher:



Inicie Balena Etcher y seleccione el archivo ISO `umbrelos-amd64-usb-installer.iso` que acaba de descargar haciendo clic en el botón "*Flash from file*". A continuación, selecciona la llave USB como dispositivo de destino y haz clic en "*Flash!*" para empezar a escribir.



![Image](assets/fr/004.webp)



Una vez completada la operación, tendrás una llave USB de arranque que contiene UmbrelOS, lista para arrancar e instalar Umbrel en tu máquina.



![Image](assets/fr/005.webp)



### Paso 3: Arrancar el ordenador desde la llave USB



Ahora que tu memoria USB de arranque que contiene UmbrelOS está lista, puedes arrancar tu ordenador en ella para iniciar la instalación del sistema. Desconecte la llave USB de su ordenador principal e insértela en el dispositivo en el que desea instalar Umbrel y su nodo Bitcoin.



Como se explica al principio de este capítulo, para completar la instalación necesitarás un dispositivo de visualización y un dispositivo de entrada. Conecta una pantalla a través de HDMI (u otro puerto, dependiendo de tu PC) y conecta un teclado a través de USB a tu máquina. Estos dispositivos sólo son necesarios para la instalación; no los necesitarás después, ya que podrás acceder a Umbrel de forma remota desde otro ordenador. Conecta estos dos dispositivos a tu PC.



**Consejo:** Si no tienes una pantalla periférica en casa, puedes utilizar tu televisor. Con su entrada HDMI (u otra), puede utilizarse como pantalla temporal mientras instalas el sistema operativo.



Umbrel requiere obviamente una conexión a Internet. Conecta el cable Ethernet RJ45 entre tu dispositivo y el router.



![Image](assets/fr/006.webp)



Enciende tu ordenador. En la mayoría de los casos, debería detectar automáticamente la llave USB y arrancar desde ella. Entonces verás aparecer la pantalla de instalación de UmbrelOS Interface.



Si el dispositivo arranca en otro sistema o muestra un mensaje de error, probablemente significa que no está arrancando automáticamente desde la llave USB. En este caso, reinicie y entre en la configuración BIOS/UEFI (normalmente se accede pulsando `DEL`, `F2`, `F12`, o `ESC`, dependiendo del fabricante del ordenador). A continuación, cambia el orden de arranque para dar prioridad a la llave USB. A continuación, reinicie el dispositivo para iniciar UmbrelOS.



### Paso 4: Instala UmbrelOS en tu ordenador



Una vez que el dispositivo ha arrancado desde la memoria USB, será recibido por la instalación de UmbrelOS Interface. Este paso consiste en instalar el sistema directamente en el disco interno de la Hard.



La pantalla que aparece enumera todos los dispositivos de almacenamiento interno detectados por el ordenador. Cada disco va acompañado de un número, un nombre y una capacidad de almacenamiento. Localice el disco en el que desea instalar Umbrel. **Advertencia: todos los archivos de este disco se borrarán permanentemente



![Image](assets/fr/007.webp)



Una vez que haya identificado el disco correcto (normalmente el de mayor capacidad, para alojar la Blockchain), anote el número que tiene asignado. Por ejemplo, si el disco que ha elegido aparece bajo el número `2`, simplemente introduzca `2` y pulse la tecla `Enter` del teclado.



![Image](assets/fr/008.webp)



El programa formateará el disco seleccionado, instalará UmbrelOS y configurará automáticamente el sistema. Esto puede tardar unos minutos. Deje que el proceso se ejecute sin interrupción.



![Image](assets/fr/009.webp)



Una vez finalizada la instalación, se le pedirá que apague el dispositivo. Pulsa cualquier tecla para apagar el ordenador.



![Image](assets/fr/010.webp)



Ya puedes retirar la llave USB, el teclado y la pantalla, que ya no son necesarios para tu Umbrel. Todo lo que queda de tu nodo es la Supply de alimentación y el cable Ethernet RJ45.



![Image](assets/fr/011.webp)



Antes de reiniciar el dispositivo, compruebe los dos puntos siguientes:





- La llave USB está desconectada**: si permanece conectada, el sistema puede reiniciarse en ella en lugar de en el disco interno;
- El cable Ethernet está enchufado**: el aparato debe estar conectado al router para funcionar.



Pulse el botón de encendido. El sistema arranca automáticamente desde el disco interno donde UmbrelOS fue instalado. El primer arranque puede tardar aproximadamente **5 minutos**. Durante este tiempo, Umbrel inicializa sus servicios y Interface.



Desde otro ordenador (tu PC de siempre) conectado a la **misma red local**, abre un navegador web (Firefox, Chrome...) y ve a:



```
http://umbrel.local
```



Esta Address se utiliza para acceder remotamente a la Interface gráfica de usuario de Umbrel y comenzar la configuración.



Si el Address `http://umbrel.local` no funciona en su navegador después de esperar al menos 5 minutos, simplemente inténtelo:



```
http://umbrel
```



Si esto sigue sin funcionar, introduce la IP local Address de tu Umbrel directamente en el navegador. Por ejemplo (sustituye `42` por el número de tu máquina que aloja Umbrel en la red local):



```
http://192.168.1.42
```



Para identificar su IP Address de Umbrel, existen varios métodos, desde el más sencillo hasta el más avanzado:





- Acceda a la administración de su router Interface y busque la IP Address del dispositivo Umbrel en la red local.





- Utiliza un software de exploración de redes como Angry IP Scanner para detectar los dispositivos conectados y localizar la IP Address de tu Umbrel.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Como último recurso, vuelva a conectar un monitor y un teclado al dispositivo, inicie sesión (inicio de sesión predeterminado: `umbrel`, contraseña: `umbrel`) y escriba el siguiente comando:



```
hostname -I
```



Ya puedes utilizar Umbrel



### Paso 5: Primeros pasos con Umbrel



Para empezar a configurar tu Umbrel, haz clic en el botón "*Iniciar*".



![Image](assets/fr/013.webp)



#### Crear una cuenta



Elige un seudónimo o introduce tu nombre, luego establece una contraseña fuerte. Ten cuidado: esta contraseña es la única barrera que protege el acceso a tu Umbrel desde tu red (y por lo tanto, potencialmente, a tus bitcoins si ejecutas un nodo Lightning en Umbrel). También protege el acceso remoto a través de Tor o VPN, si estos servicios están habilitados.



Elija una contraseña segura y asegúrese de guardar al menos una copia de seguridad (se recomienda utilizar un gestor de contraseñas).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Una vez introducida la contraseña, haz clic en el botón "*Crear*".



![Image](assets/fr/014.webp)



La configuración de Umbrel ya está completa.



![Image](assets/fr/015.webp)



#### Descubrimiento de Interface



El Interface de Umbrel es bastante intuitivo:





- En la página de inicio, puedes ver las aplicaciones y widgets que tienes instalados.



![Image](assets/fr/016.webp)





- La "*App Store*" te permite instalar nuevas aplicaciones,



![Image](assets/fr/017.webp)





- El menú "*Archivos*" centraliza todos los documentos almacenados en tu Umbrel.



![Image](assets/fr/018.webp)





- El menú "*Configuración*" te permite modificar la configuración de tu Umbrel y acceder a su información, entre otras cosas:
    - Actualice, reinicie o detenga su máquina;
    - Consulte el espacio de almacenamiento disponible, el uso de RAM y la temperatura del procesador;
    - Cambia el fondo de pantalla;
    - Gestione el acceso remoto mediante Tor, active Wi-Fi o 2FA.



![Image](assets/fr/019.webp)



#### Ajustes de seguridad y conexión



En primer lugar, recomiendo encarecidamente activar la autenticación de dos factores (2FA). Esto añade un Layer extra de seguridad a tu contraseña. Es casi indispensable si planeas utilizar tu Umbrel para almacenar archivos personales, ejecutar un nodo Lightning o realizar cualquier otra actividad sensible.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Para ello, haga clic en la casilla correspondiente de la configuración.



![Image](assets/fr/020.webp)



A continuación, escanee el código QR que se muestra utilizando su aplicación de autenticación. A continuación, introduce el código dinámico de 6 dígitos en el campo previsto para ello en tu Umbrel.



A partir de ahora, cada nueva conexión a tu Umbrel requerirá tanto la contraseña como el código de 6 dígitos generado por tu aplicación de autenticación de dos factores (2FA).



![Image](assets/fr/021.webp)



En cuanto al acceso remoto vía Tor, si no lo necesitas, te recomiendo dejar esta opción desactivada para limitar la superficie de ataque de tu Umbrel. Por defecto, sólo se puede acceder a tu nodo desde una máquina conectada a la misma red local. No obstante, habilitar el acceso vía Tor te permitirá gestionar tu Umbrel en movilidad.



Si habilita esta característica, teóricamente es posible que cualquier máquina en el mundo intente conectarse a su nodo, siempre que conozca la Address de Tor. Sin embargo, su contraseña y 2FA le seguirán protegiendo.



Si activa esta opción, asegúrese de tener activada la autenticación de dos factores (2FA), una contraseña segura y nunca revele su conexión Tor Address.



Simplemente introduce este Tor Address en tu navegador Tor para acceder al Interface de Umbrel desde cualquier red.



![Image](assets/fr/026.webp)



Por último, en esta página de configuración, también puede activar la conexión Wi-Fi. Si su máquina que aloja Umbrel dispone de una tarjeta de red Wi-Fi o de un dongle Wi-Fi, esto le permite acceder a Internet sin utilizar el cable RJ45. Sin embargo, dependiendo de tu configuración, esta solución puede ralentizar la conexión, lo que puede afectar a la sincronización inicial (IBD) y al uso futuro del nodo (por ejemplo, para transacciones Lightning). Personalmente, no recomiendo esta opción, ya que un nodo no está pensado para un uso móvil: siempre se accede a él de forma remota, así que más vale dejarlo enchufado.



### Paso 6: Instalar un nodo Bitcoin en Umbrel



Ahora que UmbrelOS está correctamente instalado y configurado en tu máquina, puedes proceder a instalar tu nodo Bitcoin. Nada más sencillo: ve a la App Store, abre la categoría "*Bitcoin*" y selecciona la aplicación "*Bitcoin Node*" (en realidad es Bitcoin core).



![Image](assets/fr/022.webp)



A continuación, haz clic en el botón "*Instalar*".



![Image](assets/fr/023.webp)



Una vez completada la instalación, su nodo Bitcoin lanzará su IBD (*Descarga Inicial de Bloques*): descargará y validará todas las transacciones y bloques desde que Bitcoin fue creado en 2009.



![Image](assets/fr/024.webp)



Esta etapa es especialmente lenta, ya que su duración depende de varios factores, como la cantidad de RAM asignada a la caché del nodo, la velocidad del disco, la velocidad de conexión a Internet y la potencia del procesador. El rango de duraciones es por tanto muy amplio, dependiendo de la configuración. Con un PC de alto rendimiento (SSD NVMe, +32 GB de RAM, procesador potente y buena conexión a Internet), el IBD puede completarse en unas diez horas. En cambio, un procesador antiguo, poca RAM o, peor aún, un disco mecánico Hard (totalmente desaconsejado) pueden alargar esta operación hasta varias semanas.



Con un PC de configuración normal (un procesador decente, de 8 a 16 GB de RAM y una unidad SSD), da para unos 2 a 7 días.



Para acelerar ligeramente el IBD, puedes aumentar la RAM asignada a la caché del nodo (utilizada principalmente para el conjunto UTXO, que revisaremos más adelante en el curso) mediante el parámetro `dbcache`. En Umbrel, esta modificación se realiza en tus parámetros de nodo, en la pestaña "*Optimización*".



![Image](assets/fr/025.webp)



Por defecto, el valor del parámetro `dbcache` en Bitcoin core está fijado en 450 MiB, o alrededor de 472 MB. Aumentando este valor, puedes acelerar ligeramente el IBD. Sin embargo, yo no recomendaría forzar este parámetro demasiado: incluso ajustándolo a 4 GiB sólo hará la sincronización un 10% más rápida, y puede hacerle perder tiempo en el caso de una interrupción durante el IBD.



Tenga cuidado de no asignar un valor demasiado grande para su máquina. Si la RAM disponible para UmbrelOS se agota, tu nodo puede pararse bruscamente, interrumpiendo el IBD y obligándote a reiniciarlo manualmente, con la consiguiente pérdida de tiempo considerable.



Para saber más sobre el impacto del parámetro `dbcache` en la sincronización inicial, recomiendo este análisis de Jameson Lopp: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Una vez completado el IBD de tu nodo (100% de sincronización), ya tienes un nodo Bitcoin totalmente operativo. Enhorabuena, ¡ya eres parte integrante de la red Bitcoin!



![Image](assets/fr/027.webp)



En la siguiente parte, exploraremos el uso práctico de tu nuevo nodo: cómo conectar tu Wallet a él y qué aplicaciones deberías instalar para convertirte en un Bitcoiner soberano.





# Conexión de Wallet al nodo


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indexadores: función, funcionamiento y soluciones


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Si ya ha explorado los nodos Bitcoin antes de realizar este curso, es posible que se haya encontrado con el término "indexador". Se trata de herramientas como Electrs o Fulcrum, que pueden añadirse a un nodo Bitcoin core. Pero, ¿cuál es exactamente su función? ¿Cómo funcionan en la práctica? ¿Debería instalar uno en su nuevo nodo Bitcoin? Eso es lo que vamos a explorar en este capítulo.



### ¿Qué es un indexador?



En términos generales, un indexador es un programa que escanea un conjunto de datos en bruto, extrae las claves relevantes (como palabras, identificadores y direcciones) y construye un archivo auxiliar, denominado "índice", en el que cada clave hace referencia a la ubicación exacta de los datos en el corpus. Esta fase de preprocesamiento utiliza tiempo de CPU y requiere algo de espacio en disco, pero elimina la necesidad de procesar todo el corpus cada vez que se consulta la base de datos; basta con interrogar el índice para obtener una respuesta casi inmediata.



En términos sencillos, es el mismo principio que el índice de un libro: si busca una información concreta, en lugar de releer todo el libro, consulta el índice para encontrar directamente la página donde aparece la información que busca.



En un nodo Bitcoin, como Bitcoin core, los datos Blockchain se almacenan en su forma cruda y cronológica. Cada bloque contiene transacciones, que a su vez contienen entradas y salidas, sin ninguna clasificación particular por Address, identificador o Wallet. Esta organización lineal está optimizada para la validación de bloques, pero es inadecuada para búsquedas específicas. Por ejemplo, si quisiéramos encontrar todas las transacciones vinculadas a un Address concreto en un nodo no indexado, tendríamos que revisar manualmente todo el Blockchain, bloque por bloque y transacción por transacción. Aquí es precisamente donde entra en juego el indexador de su nodo Bitcoin.



![Image](assets/fr/085.webp)



Un indexador es un programa informático especializado que analiza esta masa de datos en bruto (conjunto Blockchain, Mempool, UTXO) y extrae claves, como identificadores de transacciones, direcciones y alturas de bloque. A partir de estas claves, construye su índice, asociando cada clave a la ubicación exacta de la información en el almacenamiento del nodo.



![Image](assets/fr/086.webp)



La indexación le permite buscar información en su nodo de forma rápida, precisa y eficaz. Por ejemplo, cuando conectas una Wallet como Sparrow a tu nodo, éste puede mostrar el saldo de una Address casi al instante. En concreto, consulta al indexador con una petición como: "_¿Qué UTXOs están asociados a este script-Hash?_" El indexador responde casi de inmediato, sin tener que releer todo el Blockchain, puesto que estos datos ya figuran en su base de datos.



### ¿Tiene Bitcoin core un indexador?



Sin necesidad de software adicional, Bitcoin core no ofrece, estrictamente hablando, un indexador Address completo comparable a los que se encuentran en software como Electrs o Fulcrum. No obstante, incorpora varios mecanismos internos de indización, así como opciones opcionales para ampliar sus capacidades de consulta. Para entender bien la situación, hay que dar un rodeo por la historia del proyecto.



Hasta la versión 0.8.0 de Bitcoin core, la validación de transacciones se basaba en un índice global de transacciones, conocido como `txindex`. Este índice referenciaba todas las transacciones de Blockchain y sus salidas. Cuando un nodo recibía una nueva transacción, consultaba este índice para verificar que las salidas consumidas (en entradas) existían realmente y no se habían gastado ya. por tanto, `txindex` era indispensable para la validación de transacciones en aquella época.



Sin embargo, este enfoque tenía sus limitaciones: era lento, costoso en términos de almacenamiento y redundante en términos de información. Para remediarlo, la versión 0.8.0 introduce una revisión del modelo de validación denominada ***Ultraprune***. En lugar de almacenarlo todo en forma de índices de transacciones, Bitcoin core mantiene una sencilla base de datos dedicada únicamente a los UTXO, denominada `chainstate` (en lenguaje cotidiano, se conoce como "UTXO set"), y actualiza su lista a medida que se consumen y crean salidas.



Este método es mucho más rápido y almacena sólo el estado actual del registro, haciendo innecesario el indexador `txindex`. Sin embargo, en lugar de eliminar el código `txindex`, los desarrolladores han optado por mantener esta funcionalidad detrás de un simple parámetro (`txindex=1`). Activando esta opción en tu nodo, podrás consultar cualquier transacción desde su `txid`.



Contrariamente a la creencia popular, Bitcoin core no ofrece indexación basada en Address como Electrs o Fulcrum. Hay varias razones para esta elección:





- El papel de Bitcoin core no es convertirse en un Block explorer completo, ni proporcionar una API adaptada a cada uso. Integrar un índice basado en Address implicaría un mantenimiento a largo plazo Commitment que va más allá del alcance inicial del software.





- La mayoría de los casos de uso ya pueden cubrirse de otras formas. Por ejemplo, para estimar el saldo de una Address, puede utilizar el comando `scantxoutset`, que consulta directamente el conjunto UTXO sin necesidad de un índice completo.





- Cada programa de software tiene requisitos específicos en cuanto al formato o tipo de datos que deben indexarse (Address, script Hash, etiqueta propietaria, etc.). Es más flexible y lógico dejar que estos programas construyan sus propios índices personalizados que fijar una solución genérica en Bitcoin core.



Bitcoin core tiene un indexador de transacciones opcional (`txindex`), un vestigio de su funcionamiento histórico, pero no proporciona un índice Address, ni un Interface directo para búsquedas complejas. En algunos casos, por tanto, puede ser útil añadir un indexador externo.



### ¿Debería añadir un indexador Address a su nodo?



Añadir un indexador Address, como Electrs o Fulcrum, no es obligatorio; depende de sus necesidades específicas.



Si simplemente desea conectar un Wallet, como Sparrow, a su nodo para ver los saldos y las transacciones de difusión, esto es totalmente posible directamente a través de Interface RPC de Bitcoin core, ya sea localmente o de forma remota a través de Tor.



Por otra parte, para utilizar un software más avanzado, como el funcionamiento de un Mempool.Localmente, la instalación de un indexador Address se hace indispensable para el espacio Block explorer.



El indexador requiere cierto tiempo de sincronización (menos que el IBD) y ocupará espacio adicional en disco. Si su SSD todavía tiene suficiente espacio libre después de descargar Blockchain, puede añadir fácilmente un indexador.



### ¿Qué indexador elegir?



Para construir este tipo de índice Address y hacerlo accesible se utilizan habitualmente dos programas informáticos: **Electrs** y **Fulcrum**. Estas herramientas indexan el Blockchain según el script-Hash (direcciones) y proponen a continuación un Interface normalizado (el protocolo Electrum), al que se conectan numerosos monederos, como Electrum Wallet, Sparrow o Phoenix.



![Image](assets/fr/087.webp)



En pocas palabras, Electrs es bastante compacto: indexa Blockchain más rápido y ocupa menos espacio en disco, pero su rendimiento en las consultas es ligeramente inferior al de Fulcrum. En cambio, Fulcrum consume más espacio en disco y tarda más en indexar, pero ofrece un rendimiento superior en las consultas.



Para uso individual, recomiendo Electrs: consume menos espacio, está bien mantenido y, aunque es ligeramente más lento en ciertas peticiones que Fulcrum, sigue siendo más que suficiente para el uso diario. Si tienes tiempo y espacio en disco, también puedes probar Fulcrum, que funcionará bastante mejor, especialmente en carteras con numerosas direcciones que verificar.



En concreto, en agosto de 2025, Electrs necesitará aproximadamente 56 GB de almacenamiento, frente a los aproximadamente 178 GB de Fulcrum. La elección del indexador, por tanto, también depende de la capacidad de almacenamiento:




- Si su espacio en disco es muy limitado, tendrá que conformarse con Bitcoin core sin un indexador externo Address.
- Si desea utilizar un indexador, pero sigue teniendo limitaciones de capacidad, opte por Electrs.
- Si dispones de una buena cantidad de espacio en disco, Fulcrum puede ser justo lo que estás buscando.



Para el resto de este curso BTC 202, utilizaré Electrs, pero puedes seguirlo fácilmente con Fulcrum: el procedimiento de instalación es idéntico, al igual que la conexión de Interface a Wallet, ya que ambos exponen un servidor Electrum.



### ¿Cómo se instala un indexador en Umbrel?



Para instalar Electrs (o Fulcrum) en su Umbrel, el procedimiento es sencillo: vaya a la App Store, busque la aplicación correspondiente (situada en la pestaña Bitcoin) y pulse el botón "*Install*".



![Image](assets/fr/028.webp)



Una vez finalizada la instalación, Electrs procederá a una fase de sincronización (indexación), que puede durar varias horas.



![Image](assets/fr/029.webp)



Una vez finalizada la sincronización, puede conectar su software Wallet a su servidor Electrum, que está alojado en Umbrel.



## ¿Cómo conecto mi Wallet a mi nodo Bitcoin?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Ahora que tienes un nodo Bitcoin completo, ¡es hora de darle un buen uso! En el próximo capítulo, exploraremos otros usos potenciales para su instancia de Umbrel. Sin embargo, empecemos por lo básico: conectar su software Wallet para utilizar la información de su propio Blockchain y distribuir transacciones a través de su propio nodo.



Como ya se ha mencionado, existen dos interfaces de conexión principales:




- Conexión directa con Bitcoin core a través de RPC;
- O conectarse a un servidor Electrum (Electrs o Fulcrum).



En este tutorial, nos concentraremos en conectarnos a tu nodo a través de Tor, ya que es una solución simple y segura para principiantes. Le recomiendo encarecidamente que no exponga el puerto RPC de su nodo en claro, ya que una mala configuración representa un riesgo significativo para la seguridad y confidencialidad de sus datos. La principal desventaja de las comunicaciones vía Tor es su lentitud. En el próximo capítulo, exploraremos una alternativa rápida y segura a Tor para el acceso remoto a su nodo: VPN.



Utilizaremos Sparrow como ejemplo en este capítulo, pero el procedimiento es el mismo para todos los demás programas de gestión de Wallet que acepten conexiones a servidores Electrum. Simplemente localice el ajuste correspondiente en los parámetros de su aplicación (normalmente en "*Servidor*", "*Red*", "*Nodo*"...).



En Sparrow, abra la pestaña "*Archivo*" y vaya al menú "Configuración".



![Image](assets/fr/030.webp)



A continuación, haga clic en "*Servidor*" para acceder a los parámetros de conexión.



![Image](assets/fr/031.webp)



A continuación, descubrirá tres opciones para vincular su software a un nodo Bitcoin:




- Servidor Público* (amarillo): por defecto, si no posees un nodo Bitcoin, esta opción te conecta a un nodo público que no poseas (normalmente el de una empresa). Esta opción no es relevante aquí, ya que tienes tu propio nodo en Umbrel.
- Bitcoin core* (Green): esta opción corresponde a la conexión a través de Interface RPC, es decir, directamente a Bitcoin core.
- Electrum privado* (azul): esta opción le permite conectarse a través del servidor Electrum Interface de su indexador (Electrs o Fulcrum).



### Conexión a Bitcoin core RPC



Si su nodo Umbrel no tiene un indexador, esta es la opción que debe seleccionar. En Sparrow, haga clic en "*Bitcoin core*".



![Image](assets/fr/032.webp)



A continuación, deberá introducir varios datos para establecer la conexión con su nodo. Se puede acceder a todos estos datos desde la aplicación "*Bitcoin Node*" de Umbrel pulsando el botón "*Connect*" en la esquina superior derecha del Interface.



![Image](assets/fr/033.webp)



La pestaña "*Detalles RPC*" muestra toda la información necesaria para la conexión. Elija conectarse a través de Tor Address (en `.onion`).



![Image](assets/fr/034.webp)



Introduzca estos datos en los campos correspondientes de la Sparrow wallet y, a continuación, pulse el botón "*Probar conexión*".



![Image](assets/fr/035.webp)



Si la conexión se realiza correctamente, aparecerá una marca Green y un mensaje de confirmación.



![Image](assets/fr/036.webp)



La marca en la parte inferior derecha de la Interface Sparrow wallet será ahora Green (lo que indica una conexión directa con Bitcoin core).



**Nota:** Para que la conexión tenga éxito, su nodo debe estar sincronizado al 100%. Si este no es el caso, por favor espere hasta el final del IBD.



### Conectar con Electrs



Si su nodo tiene un indexador, es mejor conectarse a él que utilizar Bitcoin core directamente, ya que sus consultas se procesarán más rápidamente.



En Sparrow, ve a la pestaña "*Private Electrum*".



![Image](assets/fr/037.webp)



A continuación, deberá introducir varios datos para establecer la conexión con su indexador. Encontrarás estos datos en la aplicación "*Electrs*" (o, en su caso, "*Fulcrum*") de Umbrel.



Seleccione la pestaña "*Tor*" para obtener la conexión `.onion` Address. Si desea conectar un software Wallet móvil, también puede escanear el código QR directamente.



![Image](assets/fr/038.webp)



Sólo tiene que introducir el Tor Address de su servidor Electrum en el campo "*URL*" y hacer clic en el botón "*Test Connection*".



![Image](assets/fr/039.webp)



Si la conexión se realiza correctamente, aparecerá una marca de verificación y un mensaje de confirmación.



![Image](assets/fr/040.webp)



La marca en la esquina inferior derecha de la Interface Sparrow wallet se volverá azul (el color asociado a la conexión con un servidor Electrum).



**Nota:** Para que la conexión funcione, su indexador debe estar sincronizado al 100%. Si este no es el caso, espere hasta que el proceso de indexación se haya completado.



¡Ahora ya sabe cómo conectar su Wallet a su nodo Bitcoin! En el próximo capítulo, le presentaré varias aplicaciones adicionales disponibles en Umbrel que me gustan especialmente, y que le permitirán mejorar el uso diario de Bitcoin a través de su nodo.




## Resumen de las aplicaciones disponibles


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel ofrece una extensa tienda de aplicaciones. Como verás, hay muchas herramientas relacionadas con Bitcoin, pero también una gran variedad de aplicaciones en campos muy diferentes: soluciones de autoalojamiento para servicios y archivos, aplicaciones de productividad, herramientas financieras más generales, gestión de medios, seguridad y administración de redes, desarrollo, inteligencia artificial, redes sociales e incluso domótica.



En este curso BTC 202, nos centraremos exclusivamente en las aplicaciones relacionadas con Bitcoin. No obstante, no dude en explorar el resto del catálogo en busca de herramientas que puedan serle de utilidad.



Por supuesto, sería imposible enumerar aquí todas las aplicaciones de Bitcoin. En este capítulo, me gustaría presentarle las herramientas esenciales que facilitarán y enriquecerán su uso diario de Bitcoin.



### Mempool.space



En el uso diario de Bitcoin, si hay una herramienta verdaderamente indispensable, ésa es Block explorer. Accesible en línea o instalada localmente, transforma los datos brutos de Blockchain en un formato estructurado, claro y fácil de leer. También cuenta con un motor de búsqueda que permite a los usuarios localizar rápidamente un bloque, transacción o Address concretos.



En concreto, el explorador le permite estimar las comisiones necesarias para que su transacción se incluya en un bloque, luego seguir su evolución: averiguar si es probable que se incluya en un futuro próximo, en función del mercado de comisiones, y, por último, confirmar que efectivamente se ha incluido en un bloque. También ofrece la posibilidad de analizar sus transacciones anteriores y consultar su historial. En resumen, es la navaja suiza del bitcoiner.



Como ya se ha mencionado, un explorador puede estar alojado en línea en un sitio web o ejecutarse localmente en tu máquina. Una gran desventaja de los servicios online es que pueden comprometer tu privacidad. Sin VPN o Tor, el servidor que aloja el explorador puede vincular tu IP Address a las transacciones que estás viendo, lo que puede proporcionar un punto de entrada ideal para el análisis en cadena.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Es más, su proveedor de servicios de Internet (ISP) puede saber que usted está viendo una transacción concreta a través del sitio Block explorer. Esto también plantea una cuestión de confianza: debe confiar en que el servicio en línea le proporcione información exacta sobre sus transacciones, sin poder comprobar usted mismo su veracidad.



Por eso siempre es mejor utilizar tu propio Block explorer local. De esta forma, no se filtrará ningún dato relacionado con su actividad de búsqueda, ya que todas las consultas se procesan directamente en una máquina que usted controla, sin pasar por Internet. Es más, un explorador local se basa en datos de tu propio nodo Bitcoin, que tú mismo has validado, según tus propias reglas, y en los que puedes confiar.



Umbrel ofrece varios exploradores de bloques:




- Mempool.Espacio
- Bitfeed
- Explorador BTC RPC



A mí me gusta especialmente Mempool.Space, que he instalado en mi nodo. Atención: para utilizar la mayoría de los exploradores de bloques en Umbrel, se necesita un indexador Address. Por lo tanto, necesitas la aplicación Bitcoin Node (o Bitcoin Knots), que tiene un Blockchain sincronizado al 100%, así como un indexador como Electrs o Fulcrum, que también está sincronizado al 100%.



Una vez instalada la aplicación, sólo tienes que abrirla para acceder a tu propio explorador.



![Image](assets/fr/041.webp)



Para saber más sobre el uso del explorador Mempool.Space, le recomiendo este completo tutorial:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Nodo Rayo



Ahora que dispone de su propio nodo Bitcoin, también puede configurar su propio nodo Lightning para realizar transacciones off-chain, sin depender de una infraestructura de terceros.



Umbrel ofrece una serie de aplicaciones para ayudarte a poner en marcha tu nodo Lightning. Ya puedes elegir entre dos implementaciones principales:




- LND, a través de la aplicación *Lightning Node*;
- Core Lightning.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

A continuación, puede administrar su nodo desde el Interface principal o, para una funcionalidad aún mayor y opciones avanzadas, instalar *Ride The Lightning* o *ThunderHub*. Estas herramientas le proporcionarán un sistema de gestión de Interface basado en web mucho más completo para su nodo.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Por último, te recomiendo la aplicación *Lightning Network+*, que te permite encontrar compañeros con los que abrir canales, lo que permite realizar transacciones en efectivo tanto salientes como entrantes.



![Image](assets/fr/089.webp)



Gracias a Umbrel, la gestión de un nodo personal Lightning se ha simplificado mucho, pero sigue siendo relativamente compleja. Por este motivo, profundizaremos en este tema en un próximo curso dedicado íntegramente a este uso.



### Tailscale



Otra aplicación que me gusta especialmente de Umbrel es Tailscale. Es una aplicación VPN diseñada para simplificar la creación de redes seguras entre múltiples dispositivos, estén donde estén en el mundo. A diferencia de las VPN tradicionales, que dependen de servidores centralizados, Tailscale utiliza el protocolo WireGuard para establecer conexiones cifradas de extremo a extremo entre tus distintas máquinas. Esto significa que puedes desplegar una VPN operativa en sólo unos minutos, sin necesidad de complicadas configuraciones de red.



En Umbrel, la instalación de Tailscale conecta tu nodo Bitcoin a tu propia red privada virtual. Una vez configurado, tu nodo obtiene una IP Tailscale Address privada, accesible solo desde otros dispositivos conectados a la misma red Tailscale (como ordenadores, smartphones y tablets). Esta conexión está cifrada de extremo a extremo y no pasa por una red pública desprotegida, lo que mejora significativamente la seguridad en comparación con una conexión no cifrada.



![Image](assets/fr/090.webp)



En concreto, Tailscale te ofrece varias ventajas a la hora de utilizar tu Umbrel:





- Puede administrar el Interface Umbrel o acceder a las aplicaciones vinculadas a su nodo (como Mempool, Ride The Lightning, ThunderHub...) desde cualquier lugar, como si estuviera en la misma red local, sin exponer puertos en Internet y sin pasar por Tor, que es muy lento;





- Puede conectarse a su servidor Electrum (Electrs o Fulcrum) o directamente a Bitcoin core a través de su VPN, evitando Tor. Esto proporciona una conexión segura, comparable al uso de Tor, pero con una velocidad mucho mayor y una latencia reducida. En resumen, conserva las ventajas de privacidad y seguridad de Tor mientras disfruta de la velocidad de una conexión Clearnet. Para un On-Chain Wallet, esta ganancia puede parecer marginal, pero si está pensando en montar su propio nodo Lightning más adelante, la diferencia es considerable. De hecho, realizar pagos a través de tu nodo en movimiento en Tor es extremadamente lento debido a los numerosos intercambios necesarios, mientras que con Tailscale, funciona perfectamente.





- No es necesario configurar reglas NAT, abrir puertos ni configurar un servidor VPN convencional. Una vez instalada la aplicación en Umbrel y en tus dispositivos, la red se establece automáticamente.



Tailscale on Umbrel es, por tanto, una solución muy interesante si quieres acceder a tu nodo desde cualquier parte del mundo de una forma segura, de alto rendimiento y fácil de configurar, sin sacrificar la privacidad o la seguridad.



Para instalar y configurar Tailscale en tu Umbrel, consulta este tutorial, sección 4: "*Using Tailscale on Umbrel*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, acrónimo de "*Notes and Other Stuff Transmitted by Relays*", es un protocolo abierto y descentralizado diseñado para permitir la publicación e intercambio de mensajes en Internet sin depender de una plataforma centralizada. Cada usuario dispone de un par de claves criptográficas: la clave pública (`npub`), que sirve de identificador, y la clave privada (`nsec`), que se utiliza para firmar los mensajes y garantizar su autenticidad.



Los mensajes se transmiten a través de una red de repetidores independientes. Esta arquitectura distribuida hace que Nostr sea resistente a la censura: ningún servidor controla el acceso o la distribución, y un usuario puede conectarse a tantos repetidores como desee.



Este protocolo es muy popular dentro de la comunidad Bitcoin porque, al igual que Bitcoin, Nostr aborda cuestiones de soberanía digital y control de datos. Su creador, Fiatjaf, es un desarrollador ya reconocido en el ecosistema por sus numerosas contribuciones.



Con tu Umbrel, puedes optimizar el uso de Nostr. Instalando la aplicación ***Nostr Relay***, puedes alojar tu propio relé privado directamente en tu máquina, asegurándote de que todas tus publicaciones e interacciones en Nostr se guardan localmente y no pueden perderse por el borrado de los relés públicos.



Los clientes de Nostr ***noStrudel*** o ***Snort*** también están disponibles en Umbrel. Gracias a estas aplicaciones, puedes publicar, leer, buscar perfiles e interactuar con el ecosistema Nostr directamente desde la web Interface en tu Umbrel.



Por último, está la app ***Nostr Wallet Connect*** en Umbrel, que permite realizar pagos nativos Lightning en Nostr. En concreto, puedes vincular tu futuro nodo Lightning a tus clientes de Nostr para enviar micropagos, llamados "*zaps*", para recompensar contenidos o interactuar de forma monetizada, sin necesidad de pasar por un servicio de terceros. Estos pagos se envían directamente desde tu nodo personal a través de tus canales.



Para saber cómo utilizar todas estas aplicaciones, te recomiendo que eches un vistazo a este completo tutorial:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### Servidor BTCPay



BTCPay Server es un procesador de pagos gratuito y de código abierto que le permite aceptar pagos a través de Bitcoin y Lightning Network sin intermediarios, conservando la autocustodia de los fondos.



La arquitectura de BTCPay Server se basa en un nodo Bitcoin y, para Lightning, en una implementación compatible (LND, Core Lightning...), lo que la convierte en una de las únicas soluciones PoS totalmente no custodiables. También es el software más completo para el seguimiento y la contabilidad.



![Image](assets/fr/091.webp)



Si tiene un negocio y desea aceptar pagos Bitcoin directamente a través de su nodo Umbrel, la aplicación BTCPay Server es ideal para usted. Para saber más sobre este tema, te recomiendo consultar los siguientes recursos:





- El curso BIZ 101 sobre el uso de Bitcoin en su empresa:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- El curso POS 305 sobre el uso de BTCPay Server:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- El tutorial del servidor BTCPay:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Conceptos avanzados y mejores prácticas


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Mantenimiento del nudo paraguas


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Para empezar esta sección final, y antes de pasar a la teoría más avanzada, me gustaría examinar en este breve capítulo las mejores prácticas y acciones concretas que puedes llevar a cabo una vez que tu nodo Umbrel esté instalado, sincronizado y correctamente configurado. ¿Cómo lo mantienes a diario?



### Mantener los equipos en buen estado



Un nodo fiable empieza por un hardware estable. Asegúrese de que la máquina que aloja su nodo está correctamente ventilada, sin Dust, e instalada en un entorno seco, lejos de cualquier fuente de calor y humedad. Evite apretujarlo en un espacio reducido y opte por un lugar bien ventilado.



En Raspberry Pi y mini-PCs, el Dust acaba obstruyendo los disipadores, elevando la temperatura y provocando el throttling (limitación voluntaria del uso de recursos), lo que a su vez se traduce en una caída de la eficiencia de tu nodo. Por eso recomiendo limpiar la entrada de aire y el ventilador periódicamente, idealmente cada pocos meses.



Asegúrese de utilizar una Supply de alta calidad, ya que un voltaje inestable puede dañar el sistema e incluso suponer un riesgo de incendio. Lo ideal es utilizar la Supply original suministrada por el fabricante de su máquina. Tenga cuidado también con el sobrecalentamiento debido al efecto Joule en las regletas: respete siempre la potencia máxima admisible y no conecte nunca varias regletas en cascada.



También recomiendo invertir en un SAI. Esto protege tu nodo de apagones repentinos, permite que Umbrel se apague limpiamente en caso de apagón y garantiza la continuidad del funcionamiento durante microcortes o fallos de corta duración.



En cuanto al almacenamiento, vigila el progreso: si el disco se acerca a la saturación, considera la posibilidad de liberar espacio (desinstala las aplicaciones que no utilices, ajusta la configuración del indexador) o migra a un SSD más grande. La desventaja de un nodo Bitcoin completo es que sus requisitos de almacenamiento aumentan continuamente, ya que se genera un nuevo bloque cada 10 minutos y los bloques antiguos no se pueden eliminar (a menos que el nodo sea pruned). Por lo tanto, te aconsejo que preveas una capacidad suficientemente grande cuando compres tu hardware (2 TB como mínimo).



### Actualización



Las actualizaciones de los nodos son importantes por tres razones principales: en primer lugar, la seguridad (parches de vulnerabilidad, endurecimiento de la red y protección DoS); en segundo lugar, la compatibilidad (cambios en las políticas de retransmisión, cambios de formato y actualizaciones de protocolo); y en tercer lugar, la fiabilidad y el rendimiento (corrección de errores, consumo de recursos y otras mejoras). Así que comprueba periódicamente que UmbrelOS y tus aplicaciones están al día:





- Para actualizar el sistema: Abre el menú de ajustes y, a continuación, haz clic en el botón "*Check for Update*" situado junto al parámetro "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Para actualizar aplicaciones: Vaya a la App Store. Si alguna de tus aplicaciones requiere actualización, aparecerá un botón con una burbuja roja en la esquina superior derecha de Interface. Simplemente haga clic en él y, a continuación, actualice cada aplicación.



Realice esta operación regularmente para mantener su sistema operativo y aplicaciones actualizados.



### Copias de seguridad



Si sólo utilizas tu nodo Bitcoin para validar y distribuir tus transacciones, pero tus monederos se gestionan fuera de Umbrel (por ejemplo, con un Hardware Wallet y un Sparrow wallet), no hay nada que respaldar directamente en Umbrel. En este caso, la copia de seguridad esencial sigue siendo la de la frase de recuperación y Descriptor de tu Wallet externa, y esto se aplica tanto si utilizas tu propio nodo como si no. Así que nada cambia respecto a tu configuración anterior.



Por otro lado, dependiendo de las aplicaciones adicionales que utilices en Umbrel, puede que sea necesario realizar más copias de seguridad. Esto es especialmente cierto si utilizas un nodo Lightning en Umbrel. En este caso, es absolutamente esencial hacer una copia de seguridad de la seed suministrada cuando instaló su nodo Lightning. Además de la seed, necesita una ***Static Channel Backup (SCB)*** actualizada para poder restaurar su nodo Lightning en caso de problema. El SCB le permite recuperar sus fondos cerrando canales a la fuerza. Si falta la seed o la SCB, es imposible restaurar un nodo Lightning.



Umbrel también ofrece la opción de realizar copias de seguridad automáticas y dinámicas de este SCB en sus servidores, a través de Tor, para garantizar que siempre haya disponible un archivo actualizado. En este caso, sólo se necesita la seed para restaurar el nodo.



Revisaremos estos aspectos en detalle en el próximo curso LNP202.



### Seguridad operativa diaria



En términos de seguridad, utiliza una contraseña larga, única y aleatoria para Interface Umbrel, y recuerda activar la autenticación de dos factores (2FA). En el caso de las aplicaciones que ofrecen protección mediante contraseña y 2FA, activa siempre ambas y cambia las contraseñas predeterminadas.



Nunca expongas el salpicadero a Internet sin utilizar una pasarela segura (como una VPN, Tor o sólo acceso local). Limita el número de aplicaciones que instalas y elimina regularmente las que ya no necesites para reducir la superficie de ataque.



Para profundizar tus conocimientos sobre seguridad informática en general, te recomiendo encarecidamente que eches un vistazo a este otro curso gratuito:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnóstico y autoayuda



En caso de que se produzca un error en tu Umbrel, primero generate un paquete de diagnóstico a través de la sección de solución de problemas de UmbrelOS o de la aplicación en cuestión y, a continuación, reinicia limpiamente la aplicación. Si es necesario, intente también un reinicio completo del sistema.



Si el problema persiste, te recomiendo que [te unas a la comunidad de usuarios de Umbrel en su Discord](https://discord.gg/efNtFzqtdx). Empieza haciendo una búsqueda para determinar si alguien se ha encontrado ya con la misma dificultad y ha encontrado una solución. Si no es así, puedes publicar un mensaje en el canal `general-support`. También puedes utilizar [el foro de Umbrel](https://community.umbrel.com/).



Estas áreas le permitirán no sólo seguir los anuncios y actualizaciones de seguridad, sino también hacer preguntas y, en última instancia, ayudar a otros usuarios. A menudo es en estos intercambios donde se descubren las mejores prácticas.



Con estos sencillos hábitos, tu nodo Umbrel se mantendrá estable, seguro y útil, tanto para ti como para la red Bitcoin.




## Comprender la EII y el proceso de descubrimiento de pares


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Su nodo Bitcoin arranca sin ningún conocimiento previo del historial de transacciones. Inicialmente, es sólo un ordenador que ejecuta software (Bitcoin core o similar). Para convertirse en un nodo Bitcoin totalmente sincronizado y operativo, debe reconstruir localmente el estado de la Ledger comprobando todos los bloques publicados desde el bloque Genesis (bloque 0, publicado por Satoshi Nakamoto el 3 de enero de 2009). Este paso se denomina **IBD (_Descarga Inicial de Bloques_)**.



El IBD consiste en descargar y verificar cada bloque y transacción individualmente, aplicando las reglas de consenso, para construir su propia versión del Blockchain. El objetivo no es simplemente recuperar una copia de datos no verificados, sino llegar a la misma conclusión de forma completamente independiente, como la mayoría honesta de la red.



![Image](assets/fr/092.webp)



### Hitos de la EII



La sincronización comienza con el paso _**headers-first**_. Su nodo solicita la secuencia de cabeceras de bloque a varios pares y, para cada una de ellas, verifica las reglas Proof of Work, de ajuste de dificultad, de sintaxis, así como Timestamp y de número de versión. En resumen, se asegura de que cada cabecera recibida cumple las reglas de consenso.



![Image](assets/fr/093.webp)



Como recordatorio, un bloque Bitcoin consta de una cabecera de 80 bytes y una lista de transacciones. La huella digital del bloque se obtiene aplicando un doble SHA-256 Hash a esta cabecera, que contiene 6 campos:




- versión
- Hash del bloque anterior
- Merkle Root de transacciones
- Timestamp (mayor que la mediana de tiempo de los 11 bloques anteriores)
- objetivo de dificultad
- Nonce



![Image](assets/fr/094.webp)



Las transacciones se consignan en una Merkle Tree. Se trata de una estructura que resume un gran conjunto de datos (en este caso, todas las transacciones del bloque) agregando sus hashes progresivamente de dos en dos hasta llegar a una única "raíz", demostrando así que un elemento pertenece al conjunto (y detectando cualquier modificación). De este modo, cualquier modificación de una transacción modifica también la raíz del Merkle Tree y, por tanto, la huella digital de la cabecera del bloque. SegWit ha introducido una Commitment adicional separada para las cookies (firmas), colocada en la coinbase.



![Image](assets/fr/095.webp)



Este paso _**primero las cabeceras**_ permite al nodo identificar la rama con más trabajo (independientemente de su número de bloques), que es la rama en la que se sincronizan los nodos Bitcoin. Una vez identificada esta rama, el nodo descarga el contenido de los bloques en paralelo desde varias conexiones y, a continuación, valida cada transacción: formato, validez de los guiones (excepto `assumevalid=1`), importes y ausencia de doble gasto. Con cada comprobación correcta, el estado actual de las monedas no gastadas (conjunto UTXO) se actualiza en la base de datos `chainstate/`: las salidas gastadas se eliminan, mientras que las nuevas salidas válidas se añaden.



Mempool, por su parte, sólo entra en juego cuando se acerca a la punta de la cadena: mientras el nodo permanezca retrasado, no tiene transacciones pendientes que almacenar.



Una vez completado el IBD, el nodo entra en su fase normal: valida los nuevos bloques a medida que se publican, mantiene su Mempool con transacciones pendientes según sus reglas de retransmisión, retransmite transacciones y bloques, y gestiona cualquier reorganización de la cadena.



### SuponerVálido



Bitcoin core incorpora un mecanismo diseñado para reducir el tiempo necesario antes de que un nodo sea plenamente operativo, conservando al mismo tiempo la esencia del principio de verificación autónoma: AssumeValid.



El parámetro `assumevalid` se basa en un bloque de referencia anterior, cuyo Hash está integrado en cada versión del software. Durante el IBD, si el nodo descubre que este bloque se encuentra efectivamente en la rama con más trabajo, puede ignorar la verificación de secuencias de comandos para todas las transacciones anteriores a este punto.



Todas las demás normas (estructura de bloques, Proof of Work, límites de tamaño, importes de transacción, UTXOs, etc.) siguen estando totalmente verificadas. Sólo se ignora el cálculo de las escrituras anteriores a este bloque de referencia. El aumento de rendimiento es significativo en el IBD, ya que la verificación de firmas representa una parte importante de la carga de la CPU. Más allá de este bloque de referencia, la verificación vuelve a su estado normal.



Puede forzar la validación completa de todos los scripts desactivando este mecanismo, a costa de un IBD mucho más largo, utilizando el parámetro `assumevalid=0` en el archivo `Bitcoin.conf`.



### SupongamosUTXO



`assumeutxo` es otro parámetro existente, pero a diferencia de `assumevalid`, no está activado por defecto. Este mecanismo permite al software cargar una instantánea del conjunto UTXO, junto con sus metadatos, y considerarlo provisionalmente como estado de referencia, tras comprobar que las cabeceras conducen efectivamente al Blockchain con más trabajo.



De este modo, el nodo se vuelve rápidamente operativo para los usos comunes (RPC, conexión de monederos, etc.), al tiempo que lanza la reconstrucción completa y verificada de su propio conjunto UTXO en segundo plano. Una vez finalizada esta etapa, la instantánea inicial se sustituye por el estado reconstruido localmente. Este enfoque separa la provisión rápida de nodos de la verificación completa, sin comprometer esta última.



### Descubrimiento de pares: ¿Cómo encuentra tu nodo la red Bitcoin?



Cuando un nodo arranca por primera vez, aún no conoce a ningún peer. Sin embargo, debe encontrar otros nodos Bitcoin en Internet para solicitar cabeceras y, a continuación, bloques, con el fin de completar su IBD. Para iniciar estas conexiones, Bitcoin core sigue una lógica prioritaria.



![Image](assets/fr/096.webp)



Cuando el nodo se reinicia después de haber sido utilizado, Core primero intenta reconectarse a los peers salientes registrados antes del apagado, información almacenada en el fichero `anchors.dat`. Después, consulta su libro IP Address **`peers.dat`**, que almacena la lista de peers encontrados previamente, para reconectarse a ellos. Se trata simplemente de un fichero local, actualizado y conservado por Core. Por otra parte, para un nuevo nodo que acaba de ser lanzado, estos 2 archivos están vacíos, ya que nunca se ha comunicado con otros nodos Bitcoin.



En este caso, el software consulta _**Semillas DNS**_. Se trata de [servidores mantenidos por desarrolladores reconocidos del ecosistema](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), que devuelven una lista de direcciones IP de supuestos nodos activos. Estas direcciones permiten al nuevo nodo iniciar sus primeras conexiones y solicitar los datos necesarios al IBD. He aquí la lista de *semillas DNS* activas hasta la fecha (agosto de 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: `seed.Mainnet.achownodes.xyz.`



En la gran mayoría de los casos, el paso *Semillas DNS* es suficiente para establecer las primeras conexiones con otros nodos. Si, excepcionalmente, estos servidores no responden en 60 segundos, el nodo cambia a otro método: el código de Bitcoin core incluye [una lista estática de más de 1.000 direcciones](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) de _nodos semilla_ que se actualiza periódicamente. Si fallan los dos primeros métodos de obtención de direcciones IP, esta última solución establece una conexión inicial, a partir de la cual el nodo puede solicitar nuevas direcciones IP.



![Image](assets/fr/097.webp)



Como último recurso, puedes utilizar manualmente Supply direcciones IP a través del archivo `peers.dat` para forzar conexiones específicas.



Una vez arrancado, el gestor interno de Address diversifica las fuentes (redes autónomas distintas, clearnet y Tor, así como distintas zonas geográficas) para reducir el riesgo de aislamiento topológico. El nodo establece estas conexiones salientes (conexiones que selecciona él mismo y que, por tanto, son más seguras).



Si tu nodo está escuchando en un puerto abierto (por defecto, 8333), acepta conexiones entrantes. Éstas refuerzan la resistencia general de la red proporcionando un punto de contacto para nuevos nodos, sin aportar ningún beneficio particular a su propio IBD. Si su nodo funciona con Tor, la lógica sigue siendo la misma, pero las direcciones utilizadas son servicios `.onion`.




## Anatomía de su nudo Bitcoin


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Cuando el nodo ha completado su sincronización inicial, almacena localmente varios conjuntos de datos complementarios, lo que le permite validar bloques y transacciones, servir a los pares de la red y reiniciarse rápidamente manteniendo su estado. 3 ladrillos principales son esenciales en un nodo:




- gW-402 **bloques** almacenados en disco,
- el **conjunto UTXO** mantenido en una base de datos clave-valor,
- y el **Mempool** se almacena en RAM y se serializa periódicamente.



Además, varios ficheros auxiliares (pares, estimaciones de honorarios, listas de exclusión, carteras, etc.) completan el cuadro. Descubramos la función de todos estos ficheros.



### ¿Dónde se encuentran realmente los datos del nodo?



Por defecto, Bitcoin core guarda sus datos en un directorio de trabajo específico. En GNU/Linux, suele estar en `~/.Bitcoin/`, en Windows en `%APPDATA%\Bitcoin/`, y en macOS en `~/Library/Application Support/Bitcoin/`. Si está utilizando una solución empaquetada (por ejemplo, dentro de una distribución de nodos), este directorio puede estar montado en otro lugar, pero su estructura sigue siendo la misma. Las subcarpetas y archivos importantes que se describen a continuación siguen estando aquí.



![Image](assets/fr/098.webp)



### Los bloques



Blockchain es, por tanto, una colección de bloques. Una Full node almacena estos bloques como archivos planos secuenciales y mantiene un índice paralelo para una rápida recuperación. Cuando es necesario (reorganización, reexploración de Wallet, servicio de pares), estos datos se releen tal cual.



**Nota:** Una reorganización, o resincronización, es un fenómeno en el que la Blockchain sufre una modificación de su estructura debido a la existencia de bloques competidores a la misma altura. Esto ocurre cuando una parte del Blockchain es sustituida por otra cadena con una mayor cantidad de trabajo acumulado. Estas resincronizaciones son una parte natural del funcionamiento de Bitcoin, donde distintos mineros pueden encontrar nuevos bloques casi simultáneamente, dividiendo así la red Bitcoin en dos. En tales casos, la red puede dividirse temporalmente en cadenas competidoras. Con el tiempo, a medida que una de estas cadenas acumula más trabajo, las otras cadenas son abandonadas por los nodos, y sus bloques pasan a conocerse como "bloques obsoletos" o "bloques huérfanos" Este proceso de sustitución de una cadena por otra se denomina resincronización.



#### Archivos Blk*.dat (datos de bloque sin procesar)



Los bloques recibidos y validados se escriben en contenedores secuenciales llamados `blkNNNNN.dat`, almacenados en la carpeta `blocks/`. Cada archivo se llena en secuencia hasta que alcanza un tamaño máximo de 128 MiB, momento en el que Core abre el siguiente archivo. En su interior, cada bloque se serializa en formato de red, precedido de un identificador mágico y una longitud. Esta organización permite una escritura rápida en disco y facilita el servicio de bloques para sincronizar pares.



![Image](assets/fr/099.webp)



En el modo pruned, el nodo retiene sólo una ventana reciente de estos archivos para limitar la huella de disco. Elimina los contenedores `blk*.dat` más antiguos en cuanto se alcanza el objetivo de espacio configurado, conservando al mismo tiempo el historial suficiente para seguir siendo coherente con la cadena más conocida. El índice y el conjunto UTXO permanecen normales, lo que permite validar las siguientes transacciones y bloques.



#### Ficheros Rev*.dat (datos de cancelación)



Para poder retroceder en el tiempo durante una reorganización, Core guarda, en paralelo con cada archivo `blk`, un archivo `revNNNNN.dat` en `blocks/`. Este archivo contiene la información necesaria para deshacer el efecto de un bloque en el conjunto de UTXO: para cada salida consumida por el bloque, se almacena el estado anterior de la UTXO correspondiente (cantidad, guión, altura...). En caso de que se aborte un bloque, el nodo puede reconstituir rápidamente el estado anterior sin tener que volver a escanear toda la cadena.



![Image](assets/fr/100.webp)



#### Índice de bloques (bloques/índice)



Buscar un bloque directamente en los archivos planos llevaría demasiado tiempo. Por ello, Core mantiene una base de datos LevelDB en `blocks/index/` que enumera, para cada bloque conocido, metadatos como Hash, altura, estado de validación, archivo `blk` y offset donde se encuentra. Cuando un compañero solicita un bloque, o cuando un componente interno necesita acceder a un bloque específico, este índice proporciona un acceso rápido. Sin este índice, se necesitarían demasiadas operaciones.



![Image](assets/fr/101.webp)



#### Índices opcionales (índices/)



Algunos índices son opcionales y están desactivados por defecto, ya que aumentan la huella de disco:




- `indexes/txindex/`, que ya hemos mencionado, proporciona una tabla de mapeo transacción → ubicación, lo que permite recuperar cualquier transacción confirmada sin conocer el bloque que la contiene. Esto es útil para consultas fuera de Wallet del tipo `getrawtransaction`, pero es bastante caro.
- indexes/blockfilter/` que puede contener filtros de bloque compactos (BIP157/158) para clientes ligeros. Estas estructuras aceleran la verificación del lado del cliente a expensas de almacenamiento adicional en el nodo indexador.



### Juego UTXO (estado de la cadena)



El modelo UTXO (*Salida de transacción no gastada*) es la representación contable de Bitcoin: cada salida no gastada es una "Coin" disponible que puede utilizarse como entrada para una transacción futura.



![Image](assets/fr/102.webp)



La totalidad de todas estas piezas en un momento dado T constituye el conjunto UTXO: una gran lista de todas las piezas ahora disponibles. Es este estado el que el nodo consulta para decidir si una transacción gasta unidades legítimas no utilizadas ya en una transacción anterior (para evitar Double-spending).



![Image](assets/fr/103.webp)



El conjunto UTXO se almacena en la carpeta `chainstate/` como una base de datos compacta LevelDB. Cada parte asocia una clave derivada de la Hash de la transacción y el índice de salida con un valor que contiene: el importe, el bloqueo `scriptPubKey`, la altura del bloque de creación y un indicador coinbase.



![Image](assets/fr/104.webp)



El nodo mantiene una caché de memoria sobre LevelDB para absorber las operaciones frecuentes de lectura y escritura. El parámetro `dbcache` puede utilizarse para modificar el tamaño de esta caché: cuanto mayor sea, más accesos a memoria se beneficiarán el IBD y la validación actual, a costa de un mayor consumo de RAM. Cuando un Miner encuentra un nuevo bloque, el nodo borra del conjunto UTXO las salidas gastadas (o consumidas) por las transacciones incluidas en el bloque y añade las salidas recién creadas.



En teoría, podríamos validar una transacción volviendo a escanear el historial de bloques para comprobar que nunca se ha gastado una salida. En la práctica, sin embargo, esto llevaría demasiado tiempo, ya que habría que escanear toda la Blockchain para cada nueva transacción. Por lo tanto, el conjunto UTXO proporciona la vista mínima necesaria para demostrar localmente y en un tiempo razonable la ausencia de Double-spending.



Obsérvese que el conjunto UTXO suele estar en el centro de las preocupaciones sobre la descentralización de Bitcoin, ya que su tamaño aumenta rápidamente de forma natural. Esto se debe en parte al aumento del precio de Bitcoin, que fomenta la fragmentación de las piezas, y en parte a la creciente adopción del sistema: cuantos más usuarios hay, mayor es la demanda de UTXO.



![Image](assets/fr/105.webp)



El crecimiento del conjunto UTXO también se debe a la estructura de las transacciones de pago simples en Bitcoin. En efecto, cuando se realiza un pago, se consume un único UTXO como entrada y se crean 2 nuevos UTXO como salida (uno para el pago y otro para el Exchange). Por último, una heurística de análisis de cadenas, denominada CIOH (*Common Input Ownership Heuristic*), proporciona un incentivo adicional para evitar la consolidación de Coin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Dado que una parte debe mantenerse en RAM para verificar las transacciones en un tiempo razonable, el conjunto UTXO puede hacer que el funcionamiento de una Full node sea gradualmente demasiado costoso. Para resolver este problema, ya existen algunas propuestas, en particular [Utreexo](https://planb.network/resources/glossary/utreexo).



### La Mempool



La Mempool es el conjunto local de transacciones válidas que se han recibido pero aún no se han confirmado. Como recordatorio, una "transacción confirmada" es aquella que ha sido incluida en un bloque válido. Cada nodo mantiene su propia Mempool, que puede diferir de la de otros nodos de la red en función de:




- el tamaño asignado a la Mempool mediante el parámetro `maxmempool`: un nodo con una Mempool más grande podrá contener más transacciones que un nodo con una Mempool más pequeña (a menos que esta última quede vacía);
- reglas gW-433: son un subconjunto de las reglas de retransmisión del nodo y definen las características que debe cumplir una transacción no confirmada para ser aceptada en Mempool;
- percolación de transacciones: debido a diversos factores, una transacción determinada puede haberse distribuido a una parte de la red, pero no haber llegado aún a otra.



Es importante señalar que los mempools de los nodos no tienen valor de consenso. La Bitcoin funciona perfectamente aunque cada nodo tenga una Mempool diferente. En última instancia, los bloques autorizados son siempre los que se añaden a la Blockchain. Por ejemplo, aunque un nodo rechace inicialmente una determinada transacción en su Mempool (válida según las reglas de consenso), estará obligado a aceptarla si finalmente se incluye en un bloque con una Proof of Work válida. Si no lo hiciera y rechazara este bloque, aunque cumpliera las reglas de consenso, desencadenaría una Hard Fork, es decir, la creación de una nueva Bitcoin independiente en la que estaría solo.



#### Política y gestión de la memoria



Cuando se recibe una transacción, Core aplica una serie de comprobaciones con respecto a las reglas de consenso (sintaxis, guiones válidos, no doble gasto, etc.) y las reglas Mempool, que son una política local (RBF, umbrales mínimos de cobro, límite de datos en `OP_RETURN`, etc.). Si la transacción cumple estas normas, se almacena en memoria.



El tamaño de la Mempool está limitado por el parámetro `maxmempool` en el archivo `Bitcoin.conf` (más sobre esto en el próximo capítulo). Por defecto, el límite es de 300 MB. Cuando está lleno, el nodo aumenta dinámicamente su umbral de carga mínima y expulsa primero las transacciones menos rentables (es decir, retiene las transacciones que deberían minarse primero). Las transacciones demasiado antiguas también pueden caducar tras un retardo configurado.



#### Mempool persistencia en disco



Para acelerar los reinicios, Core serializa periódicamente el estado de la Mempool en el archivo `Mempool.dat` cuando se apaga el nodo. Además de la Mempool real, que permanece en memoria, Core almacena este archivo `Mempool.dat` en el disco. La próxima vez que se inicie el nodo, recargará esta instantánea y borrará todo lo que ya no sea válido para la Blockchain actual.



### Archivos auxiliares y bases de datos



Varios otros ficheros al mismo nivel que `blocks/`, `chainstate/`, y `indexes/` participan en el buen funcionamiento del:




- `peers.dat` mantiene un libro de Address IP de peers potenciales, alimentado por el descubrimiento inicial de DNS, intercambios de red y adiciones manuales. Cuando el nodo arranca, puede recurrir a este archivo para establecer conexiones salientes.
- Cuando el nodo se apaga, `anchors.dat` guarda las direcciones de los pares salientes, para que puedas intentar contactar con ellos rápidamente la próxima vez que arranques.
- `banlist.json` contiene prohibiciones locales decididas por el operador o por el nodo (comportamiento inválido repetido), para evitar que el nodo se vuelva a conectar o acepte conexiones de estos pares específicos.
- el archivo `fee_estimates.dat` almacena estadísticas de horizonte temporal sobre las confirmaciones observadas, utilizadas por el estimador de tasas para proponer tasas coherentes con los objetivos de demora elegidos al crear una transacción.
- gW-446.conf` contiene los parámetros de configuración de tu nodo. Aquí es donde puedes ajustar las reglas de retransmisión. Te contaré más sobre esto en el próximo capítulo.
- `settings.json` contiene parámetros adicionales a `Bitcoin.conf`.
- `debug.log` es el registro de texto de diagnóstico, que puede utilizarse para comprender la actividad del nodo en caso de fallo.
- gW-448.pid` almacena el identificador del proceso en tiempo de ejecución, permitiendo a otras aplicaciones o scripts identificar fácilmente bitcoind (*Bitcoin daemon*) e interactuar con él si es necesario. Se crea al iniciar el nodo y se elimina al apagarlo.
- `ip_asn.map` es una tabla de mapeo IP → ASN (sistema autónomo) utilizada para bucketing y diversificación de pares (opción `-asmap`).
- `onion_v3_private_key` almacena la clave privada del servicio Tor v3 cuando la opción `-listenonion` está habilitada, para mantener una Address cebolla estable entre reinicios.
- `i2p_private_key` almacena la clave privada de I2P cuando se utiliza `-i2psam=`, para realizar conexiones salientes y posiblemente entrantes en I2P.
- `.cookie` contiene un RPC efímero de autenticación token (creado al arrancar, borrado al apagar) cuando se utiliza la autenticación cookie. Se puede utilizar, por ejemplo, para conectar el software Wallet.
- .lock` es el bloqueo del directorio de datos, que impide que varias instancias escriban simultáneamente en el mismo datadir.
- `guisettings.ini.bak` es el guardado automático de la configuración GUI (*Bitcoin Qt*) cuando se utiliza la opción `-resetguisettings`.



Como vimos en las primeras partes de este curso BTC 202, Bitcoin core es a la vez un software de nodo Bitcoin y Wallet. Sin embargo, no es necesariamente la solución que recomendaría para gestionar sus carteras, ya que su Interface sigue siendo básico y sus funcionalidades son limitadas en comparación con software moderno como Sparrow o Liana. Core también incluye archivos para gestionar sus monederos:





- `wallets/` es el directorio por defecto que aloja uno o más;
- `wallets/<name>/Wallet.dat` es la base de datos SQLite de la Wallet (claves, descriptores, metadatos de transacciones, etc.);
- wallets/<name>/Wallet.dat-journal` es el registro de retrocesos de SQLite.



A modo de resumen, ésta es la estructura del archivo Bitcoin core:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Ruta de validación de un nuevo bloque



Al recibir un nuevo bloque, su nodo comprueba el Proof of Work y, de forma más general, el cumplimiento de las reglas de consenso. Si todo es correcto, aplica los cambios transacción por transacción a su conjunto UTXO: comprueba que cada entrada gasta UTXOs existentes con un guión válido, borra estos UTXOs y añade las nuevas salidas. Si todo es válido, los cambios se consignan en `chainstate/`.



En paralelo, los datos de deshacer se escriben en `rev*.dat` y los metadatos en el índice `blocks/index/`. A continuación, el bloque se serializa en el archivo `blk*.dat` correcto. En caso de reorganización, el nodo lee `rev*.dat` en sentido inverso para desconectar limpiamente los bloques abandonados, restaurar el conjunto UTXO y, a continuación, conectar los bloques de la nueva mejor cadena.





## Entender Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



El archivo `Bitcoin.conf` es el principal archivo de configuración de Interface para Bitcoin core. Te permite ajustar el comportamiento y los parámetros de tu nodo sin tener que recompilar su código fuente o hacer modificaciones en la línea de comandos. En concreto, es un archivo de texto plano estructurado en pares clave-valor, lo que significa que cada línea del archivo hace referencia a un parámetro específico (la clave) y su valor asociado, que puede modificarse para ajustar ese parámetro.



Los parámetros de red, retransmisión de transacciones, rendimiento, indexación, registro y acceso a RPC pueden definirse en `Bitcoin.conf`. Sin embargo, este archivo de configuración nunca modifica las reglas de consenso del protocolo: sólo establece la política local del nodo (reglas de retransmisión), la forma en que se conecta, indexa y expone los servicios.



### Localización y prioridad



Por defecto, `Bitcoin.conf` reside en el directorio de datos de Bitcoin core. Este es el famoso directorio que mencionamos en el capítulo anterior. Sin embargo, este archivo no es creado automáticamente por Bitcoin core, excepto en ciertos entornos, como Umbrel. Si no existe, tendrá que crearlo usted mismo, simplemente creando un archivo llamado `Bitcoin.conf`, y abriéndolo en un editor de texto para hacer sus modificaciones.



Los parámetros definidos en el `Bitcoin.conf` pueden ser anulados por 2 capas:




- `settings.json` (escrito dinámicamente por los gráficos Interface o algunos RPC),
- y opciones modificadas mediante líneas de comandos.



Tenga en cuenta que cualquier modificación en `Bitcoin.conf` requiere reiniciar el nodo para que surta efecto.



### Formato y estructura



El formato del `Bitcoin.conf` es por tanto muy simple: una línea por opción, en la forma `opción=valor`. Los espacios innecesarios y las líneas en blanco se ignoran, y los comentarios de código empiezan por `#`.



Casi todas las opciones booleanas pueden desactivarse con el prefijo `no`. Por ejemplo, `listen=0` y `nolisten=1` son equivalentes según la versión.



Para segmentar la configuración por red, puedes utilizar secciones: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. También puedes anteponer al nombre de la opción `regtest.maxmempool=100`.



### Qué puede y qué no puede hacer Bitcoin.conf



Como se ha explicado anteriormente, las reglas de consenso obviamente no son configurables en `Bitcoin.conf`, ya que esto podría crear un Hard Fork. En cambio, muchos otros aspectos sí son configurables. Hay 3 clases útiles a tener en cuenta:




- Parámetros puramente locales. Sólo afectan a tu nodo: tamaño de la caché (`dbcache`), modo pruned (`prune`), índices opcionales... Influyen en el rendimiento de tu máquina, pero no en el de la red.
- Políticas de retransmisión y Mempool. Éstas deciden lo que tu nodo acepta, retiene y retransmite antes de la confirmación: umbral mínimo de tarifa (`minrelaytxfee`), tamaño y tiempo de retención de Mempool (`maxmempool`, `mempoolexpiry`), sustitución de transacciones (RBF)... Estas reglas no forman parte del consenso, por lo que dos nodos diferentes pueden tener políticas distintas y seguir siendo totalmente compatibles. Por otra parte, estos parámetros influirán en la red Bitcoin (como se explicó en la primera parte, en particular con la teoría de la percolación).
- Conectividad de red. Estas opciones determinan cómo su nodo encuentra pares, escucha, atraviesa un NAT, utiliza Tor o un proxy, o limita su ancho de banda. Dan forma a su topología, pero no alteran la retransmisión de transacciones.



Entender esta separación es crucial: si una transacción no se adhiere a las reglas de consenso, su nodo la rechazará en cualquier caso. Pero una política local más estricta puede negarse a retransmitir una transacción que sea válida en el sentido del consenso.



### Red y topología



En primer lugar, es importante distinguir claramente entre los 2 tipos de conexión que puede tener un nodo Bitcoin:




- Conexiones salientes, que son iniciadas por nuestro nodo hacia otro nodo;



![Image](assets/fr/106.webp)





- Conexiones entrantes, iniciadas por otro nodo hacia el nuestro.



![Image](assets/fr/107.webp)



Estos dos tipos de conexión son perfectamente capaces de intercambiar los mismos datos en ambas direcciones; no se trata de limitar la dirección del flujo, sino sólo de una diferencia en el iniciador de la conexión. Desde el punto de vista de nuestro nodo, las conexiones salientes suelen considerarse más seguras, ya que nosotros las iniciamos y elegimos con precisión a qué nodo conectarnos, lo que hace poco probable que la conexión sea maliciosa. Por defecto, Bitcoin core mantiene 10 conexiones salientes (8 "*full-relay*" + 2 "*block-relay-only*").



Una Full node añade más valor a la red aceptando conexiones entrantes. El parámetro `listen=1` habilita la escucha en el puerto por defecto 8333 de la red en cuestión, permitiendo recibir estas conexiones entrantes en la clearnet. Para que esto funcione, este puerto también debe estar abierto en tu router. Si no lo está, su nodo seguirá funcionando sólo con conexiones salientes, lo que no tendrá ningún impacto en su uso personal de Bitcoin. La decisión de permitir o no las conexiones entrantes es tuya; no hay una "mejor opción"



Si prefiere no abrir un puerto en su router, pero aún así aceptar conexiones entrantes, puede activar el parámetro `listenonion=1`. Esto conseguirá el mismo resultado, pero sólo a través de la red Tor en lugar de clearnet.



A nivel de red, también tenemos:




- `addnode`: añade un par amigo con el que contactar además del descubrimiento habitual (puede especificarse varias veces).
- connect`: restringe estrictamente las conexiones al Address proporcionado (puede especificarse varias veces). El núcleo no se conectará a ningún otro nodo.
- `seednode`: se utiliza sólo para rellenar el libro-Address cuando se conecta a un nodo y luego se desconecta.
- `maxconnections`: define el límite global de conexiones entrantes + salientes. Por defecto, este parámetro se establece en 125, lo que significa que tu nodo nunca aceptará más de 125 conexiones.
- maxuploadtarget`: limita las subidas para limitar el ancho de banda en una ventana móvil de 24 horas. Este tope no sacrifica la propagación de Elements recientes esenciales.
- `onlynet`: limita las conexiones salientes sólo a las redes seleccionadas (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Por ejemplo, si quiere que su nodo se conecte a la red Bitcoin sólo a través de Tor, puede habilitar el parámetro `onlynet=onion` y deshabilitar las conexiones entrantes (o sólo permitir conexiones a través de Tor también).
- `dnsseed`: permite o no permite que _DNS seeds_ solicite peers cuando el pool local de Address es bajo (por defecto: `1`, a menos que `-connect` o `-maxconnections=0`).
- `forcednsseed`: obliga a solicitar _DNS seeds_ al inicio, incluso si ya tiene direcciones en stock (por defecto: `0`).
- `fixedseeds`: Permitir el uso de *nodos seed* (lista Address codificada) si las _semillas DNS_ fallan o están deshabilitadas (por defecto: `1`).
- `dns`: Autoriza las resoluciones DNS en general (por ejemplo, para `-addnode`/`-seednode`/`-connect`).



Por defecto, tu nodo se comunica a través de clearnet, Tor e I2P. Esto significa que los pares con los que se conecta en clearnet pueden ver tu IP pública Address, y es probable que tu ISP pueda detectar que estás ejecutando un nodo Bitcoin (aunque P2P Transport V2 hace que sea más difícil para un ISP espiar). Esto no es necesariamente un problema, pero si quieres evitar cualquier filtración de esta información, puedes conectar tu nodo exclusivamente a través de la red Tor.



Para estar completamente habilitado para Tor, necesita forzar a Bitcoin core a usar sólo esta red y crear un servicio oculto para las conexiones entrantes (si quiere habilitarlas). En el `Bitcoin.conf`, necesita añadir esta configuración:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Todas tus conexiones P2P van a través de Tor. Su nodo recibe una Address `.onion` para las conexiones entrantes, por lo que no es necesario abrir puertos en el router. Su ISP sólo ve el tráfico Tor, y sus pares desconocen su IP pública real Address.



Para evitar la resolución DNS, puedes añadir `dnsseed=0` y `dns=0` a tu configuración. A continuación, tendrás que proporcionar manualmente peers `.onion` a través de `seednode=` o `addnode=`, ya que el descubrimiento de nuevos nodos será difícil de otra manera.



Obviamente, si eres un principiante, te aconsejo que dejes todas estas configuraciones de red por el momento. La configuración por defecto suele ser suficiente.



### Mempool y política de retransmisión



#### Parámetros básicos



Estos son los parámetros básicos que puede modificar en su `Bitcoin.conf` relativos a la gestión de su Mempool y la retransmisión de transacciones no confirmadas:





- `maxmempool=<n>`: Limita el tamaño máximo de la Mempool local a `<n>` megabytes (por defecto: `300`). Cuando se alcanza el límite, su nodo aumenta dinámicamente su umbral de tarifa efectiva y prioriza las transacciones menos rentables (basándose en la tasa de tarifa, no en el valor absoluto) para mantenerse por debajo del límite. Puede dejar esta configuración por defecto. Aumentarlo puede ser útil si está Mining solo, o si quiere tener una visión más precisa de la congestión Mempool y mejorar la estimación de tasas. Por el contrario, reducirlo ahorrará RAM y, en menor medida, otros recursos del sistema.





- `mempoolexpiry=<n>`: Tiempo máximo de retención para transacciones no confirmadas en Mempool (en horas, por defecto: `336`). Pasado este tiempo, las transacciones se eliminan aunque quede espacio disponible.





- `persistmempool=1`: Guarda una instantánea de la Mempool en reposo y la recarga al reiniciar (por defecto: `1`). Esto acelera la recuperación después del reinicio, evitando la necesidad de volver a aprender el estado a través de la red.





- `maxorphantx=<n>`: Número máximo de transacciones huérfanas retenidas (entradas dependientes de UTXOs aún no vistas en el conjunto UTXO, por defecto: `100`). Más allá de este umbral, se eliminan las transacciones más antiguas para evitar un crecimiento incontrolado de la caché.





- blocksonly=1`: Desactiva la aceptación y retransmisión de transacciones no confirmadas recibidas de pares (a menos que se concedan permisos especiales). El nodo ahora sólo sube y anuncia bloques. Las transacciones creadas localmente pueden seguir siendo retransmitidas (para utilizar su nodo con su software Wallet). Esto reduce enormemente los requisitos de ancho de banda y RAM, aunque a costa de una menor utilidad para el relé y un desconocimiento total de la Mempool.





- `minrelaytxfee=<n>`: Tarifa mínima (en BTC/kvB) por debajo de la cual las transacciones no se aceptan en el Mempool del nodo y no se retransmiten a los pares (por defecto: `0.00001` = 1 sat/vB). Cuanto mayor sea este valor, más agresivamente filtrará su nodo las transacciones de bajo coste.





- `mempoolfullrbf=1`: Aceptar transacciones en RBF incluso sin señalización explícita de RBF en la transacción sustituida. Con esta política "*full-RBF*", una transacción que ofrezca una tarifa más alta puede sustituir a otra en Mempool si se cumplen las demás condiciones de sustitución.



Como recordatorio, RBF es un mecanismo transaccional que permite al remitente sustituir una transacción por otra que tenga tasas más altas para acelerar la confirmación. Si una transacción con una comisión demasiado baja permanece bloqueada, el remitente puede utilizar *Replace-by-fee* para aumentar la comisión y dar prioridad a su transacción de sustitución en los mempools y con los mineros.



#### Ajustes avanzados y específicos



Aquí están los ajustes avanzados para Mempool y la política de retransmisión. Si eres principiante, no deberías necesitar modificar estos ajustes:





- datacarrier=1`: Permite la retransmisión y (si Mining a través de nodo) la inclusión de transacciones que transporten datos no financieros a través de una salida `OP_RETURN` (por defecto: `1`). La desactivación de este parámetro reduce ligeramente la superficie de spam de datos no financieros, a costa de una menor compatibilidad con determinados usos. En todos los casos, debe aceptar la salida `OP_RETURN`.





- `datacarriersize=<n>`: Tamaño máximo (en bytes) del `OP_RETURN` que retransmite el nodo (por defecto: `83`). Reducir este valor restringe las cargas útiles transportadas a través de `OP_RETURN`. Tenga en cuenta que este límite se eliminará por defecto en una futura versión de Bitcoin core.





- `bytespersigop=<n>`: Parámetro que convierte las transacciones de firma en bytes equivalentes para la evaluación del límite de relés (por defecto: `20`). Esto influirá en la aceptación de transacciones ricas en `sigops` según las reglas de la política local.





- `permitbaremultisig=1`: Permite la retransmisión de transacciones *bare-Multisig* P2MS (por defecto: `1`). Esta es la plantilla de script más antigua para establecer condiciones multifirma en una UTXO (inventada en 2011 por Gavin Andresen).





- `whitelistrelay=1`: Concede automáticamente permiso de retransmisión a los pares entrantes de la lista blanca (por defecto: `1`). Estos pares tienen sus transacciones aceptadas por el relé, incluso si su nodo no está en modo de retransmisión general.





- `whitelistforcerelay=1`: Asigna el permiso "*forcerelay*" a los peers de la lista blanca con permisos por defecto (por defecto: `0`). El nodo retransmite sus transacciones incluso si ya están presentes en Mempool, saltándose así los mecanismos anti-redundancia.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Vincula un intervalo Interface o Address y asigna permisos detallados a los pares correspondientes: `relay`, `forcerelay`, `Mempool` (solicitud de contenido Mempool), `noban`, `download`, `addr`, `bloomfilter`. Esto puede ser útil para conceder un tratamiento privilegiado a pares de confianza (como pasarelas, LAN y servicios internos).





- peerbloomfilters=1`: Habilita el soporte de filtros Bloom (BIP37) para servir bloques/transacciones filtrados a clientes ligeros (por defecto: `0`). Advertencia: esto aumenta la carga de sus recursos.





- peerblockfilters=1`: Sirve filtros compactos BIP157 (*Neutrino*) a los pares (por defecto: `0`).





- `blockreconstructionextratxn=<n>`: Número adicional de transacciones retenidas en memoria para reconstruir bloques compactos (por defecto: `100`). Mejora el éxito de las reconstrucciones durante las sincronizaciones compactas, a costa de un poco de memoria.



Como recordatorio, todas estas reglas de retransmisión no tienen ningún impacto en la validez de las transacciones incluidas en un bloque válido. Sirven para ajustar su contribución al relevo, proteger sus recursos y hacer que su nodo sea predecible en entornos con restricciones, pero nunca le permiten rechazar bloques que respeten las reglas de consenso.



### Billeteras



También puede ajustar la forma en que se gestionan sus carteras en el archivo `Bitcoin.conf`. Si no está utilizando Wallet directamente en Core, sino software de gestión externo como Sparrow o Liana, estos parámetros serán de poca importancia:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Define el formato de las direcciones generadas por Wallet para la recepción.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Fuerza el formato Exchange Address (resto de una entrada en un único pago).





- `Wallet=<ruta>`: Carga un Wallet existente al inicio (puede repetirse para cargar varios monederos).





- `walletdir=<dir>`: Directorio que contiene los monederos (por defecto: `<datadir>/wallets` si existe, en caso contrario `<datadir>`). Esto puede ser útil si desea almacenar los monederos en un volumen dedicado o encriptado.





- `walletbroadcast=1`: Difunde automáticamente las transacciones creadas por los monederos cargados (por defecto: `1`). Establezca `0` si desea gestionar la difusión a través de otro canal.





- `walletrbf=1`: Activa la opción RBF para señalar RBF en todas las transacciones (por defecto: `1`). Permite aumentar las comisiones posteriormente en caso de transacción bloqueada.





- `txconfirmtarget=<n>`: Objetivo de confirmación para la transacción (en número de bloques, por defecto: `6`). Wallet fijará automáticamente la comisión para que la transacción se confirme en este número de bloques.





- `paytxfee=<amt>`: Tasa de comisión fija (BTC/kvB) aplicada a las transacciones Wallet. Evitar en general: utilizar estimación adaptativa mediante `txconfirmtarget`.





- fallbackfee=<amt>`: Tasa de fallback (BTC/kvB) utilizada si el estimador se queda sin datos (por defecto: `0.00`). Si se establece en 0, se desactiva por completo.





- `mintxfee=<amt>`: Umbral mínimo (BTC/kvB) para que Wallet cree transacciones (por defecto: `0.00001`). Wallet se negará a crear una transacción por debajo de este umbral.





- `maxtxfee=<amt>`: Límite absoluto de las comisiones totales de una transacción Wallet (por defecto: `0,10` BTC). Protege contra comisiones anormalmente altas que destruirían bitcoins innecesariamente.





- `avoidpartialspends=1`: Selecciona UTXOs por grupos Address para evitar gastos parciales.





- `spendzeroconfchange=1`: Permite reutilizar una UTXO Exchange no confirmada como entrada en una nueva transacción (por defecto: `1`).





- `consolidatefeerate=<amt>`: Tasa máxima (BTC/kvB) a partir de la cual Wallet evita añadir más insumos de los necesarios para consolidar. Esto permite consolidaciones oportunistas a precios bajos y reduce los costes cuando éstos son elevados.





- `maxapsfee=<n>`: Presupuesto de gastos adicionales (BTC, valor absoluto) que Wallet acepta pagar para activar la opción "*evitar gastos parciales*".





- `discardfee=<amt>`: Tasa (BTC/kvB) que indica su tolerancia a tirar el Exchange sumándolo a la tasa. Las salidas que costarían más de un tercio de su valor con esta tasa se descartan.





- `keypool=<n>`: Tamaño del pool Address pregenerado (por defecto: `1000`). Los valores demasiado pequeños aumentan el riesgo de restauraciones incompletas.





- `disablewallet=1`: Inicia Bitcoin core sin el subsistema Wallet y desactiva los RPCs asociados. Reduce la superficie de ataque y la huella si el nodo solo se utiliza para validación/liberación.



### Almacenamiento, indexación y rendimiento



El archivo de configuración también le permite ajustar los parámetros relacionados con su máquina. Esto puede ser especialmente relevante si dispones de recursos limitados o, por el contrario, de una gran capacidad disponible:





- `datadir=<dir>`: Establece el directorio de datos principal de Bitcoin core.





- `dirbloques=<dir>`: Desacopla la ubicación de los archivos de bloques (`blocks/blk*.dat` y `blocks/rev*.dat`) del `datadir`. Esto puede ser útil para colocar el archivo de bloques en un volumen diferente, mientras se mantiene la base de estado (`chainstate/`) en un medio más rápido, por ejemplo.





- `dbcache=<n>`: Asigna `<n>` MiB a la caché de la base de datos (*LevelDB*) utilizada por el índice de bloques y `chainstate` (por defecto: `450`). Cuanto mayor sea el valor, más rápido será el IBD y la validación actual, a costa de un mayor consumo de RAM.





- `prune=<n>`: Activa la poda de archivos de bloque y establece un objetivo de espacio en disco en MiB (por defecto: `0` = desactivado; `1` = poda manual a través de RPC; `>=550` = poda automática por debajo del objetivo). Incompatible con `txindex=1`. El nodo sigue siendo un nodo de validación completa, pero ya no puede proporcionar el historial antiguo. Esta opción es particularmente útil si su espacio en disco es limitado, por ejemplo, al instalar un nodo en su ordenador personal.





- txindex=1`: Construye y mantiene un índice global de transacciones confirmadas. Esencial para ciertas consultas (`getrawtransaction` no-Wallet) y para propósitos de exploración, pero aumenta significativamente la huella de disco. Incompatible con el modo pruned.





- `assumevalid=<hex>`: Indica un bloque que se asume como válido, permitiéndole saltarse las comprobaciones de script para sus ancestros (establezca `0` para comprobarlo todo). Consulte el capítulo anterior para obtener más información.





- `reindex=1`: Reconstruye los índices de bloque y el estado (`chainstate`) a partir de los ficheros `blk*.dat` del disco. También reconstruye los índices activos opcionales. Se trata de una operación que requiere mucho tiempo para reparar una base de datos corrupta o activar/desactivar índices pesados.





- `reindex-chainstate=1`: Reconstruye sólo el `chainstate` del índice de bloques actual. Preferido cuando los archivos de bloque están en buen estado.





- `blockfilterindex=<tipo>`: Mantiene los índices de los filtros de bloque compactos (por ejemplo, `basic`) utilizados por los clientes ligeros (BIP157/158) y algunos RPC. Desactivado por defecto (`0`). Consume espacio adicional en disco y tiempo de indexación.





- `coinstatsindex=1`: Mantiene un índice de estadísticas del conjunto UTXO operado por la llamada `gettxoutsetinfo`. Útil para auditorías y métricas, eliminando la necesidad de un costoso recálculo. Desactivado por defecto.





- `loadblock=<archivo>`: Importa bloques al inicio desde un archivo externo `blk*.dat`. Se utiliza para precargar el historial desde una fuente offline (copia local, medio externo) para acelerar la inicialización.





- `par=<n>`: Establece el número de hilos de verificación del script (de `-10` a `15`, `0` = auto, `<0` = deja este número de núcleos libres). Permite ajustar el paralelismo de la CPU durante la validación. El modo automático es adecuado en la mayoría de los casos.





- `debuglogfile=<file>`: Especifica la ubicación del registro `debug.log`.





- `shrinkdebugfile=1`: Reduce el tamaño de `debug.log` al inicio (por defecto: `1` cuando `-debug` no está activo).





- `settings=<archivo>`: Ruta al archivo de configuración dinámica `settings.json`.



### RPC acceso y seguridad de funcionamiento



Finalmente, el archivo `Bitcoin.conf` también te permite configurar los parámetros de acceso para tu nodo. Ten cuidado con estos ajustes, especialmente si estás empezando: evita cambiarlos sin un conocimiento profundo de las implicaciones, ya que esto podría introducir vulnerabilidades.





- `server=1`: Activa el servidor JSON-RPC. Esencial si estás manejando `bitcoind` a través de `bitcoin-cli` o una aplicación de terceros. Desactivar (`0`) en un nodo puramente validador que no expone ninguna API, o ya utiliza un servidor Electrum.





- `rpcbind=<dirección>[:puerto]`: Servidor RPC escuchando Address/puerto. Por defecto, la escucha se realiza sólo localmente (`127.0.0.1` y `::1`). Este parámetro se ignora si `rpcallowip` no está también definido. Utilícelo para restringir explícitamente Interface.





- `rpcport=<puerto>`: Puerto RPC (por defecto: `8332` en Mainnet, `18332` en Testnet, `38332` en bookmark, `18443` en regtest).





- `rpcallowip=<ip|cidr>`: Permite clientes RPC desde una IP o subred dada (puede repetirse). Usar junto con `rpcbind` para exponer la API sólo a un segmento de confianza (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Método de autenticación RPC recomendado (contraseña hash). Permite múltiples entradas y evita almacenar un secreto en texto claro.





- `rpccookiefile=<ruta>`: Ruta a la cookie de autenticación (por defecto: archivo `.cookie` bajo `datadir/`). Se utiliza para el acceso local del mismo usuario sin gestionar contraseñas persistentes. Por ejemplo, puede usarlo para conectar la Liana Wallet a su Bitcoin core en la misma máquina.





- `rpcuser=<usuario>` / `rpcpassword=<pw>`: Autenticación clásica RPC con contraseña en texto plano. Evite usar esto en favor de `rpcauth` o una cookie.





- `rpcthreads=<n>`: Número de hilos para servir llamadas RPC (por defecto: `4`). Auméntelo si tiene picos altos de llamadas en el lado de la herramienta de monitorización/externa.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Lista blanca de APIs autorizadas. Reduce la superficie de ataque restringiendo los métodos accesibles.





- `rpcwhitelistdefault=1|0`: Comportamiento por defecto de la lista blanca: si se activa y se utiliza una lista blanca, se rechazan las llamadas no listadas. Esto también puede forzar un conjunto vacío por defecto (no se permiten llamadas) siempre y cuando no se liste nada explícitamente.





- `rest=1`: Habilitar la API REST pública (deshabilitada por defecto). Solo debe exponerse en una red de confianza (misma precaución que con JSON-RPC).





- `conf=<archivo>`: Especifica, sólo en la línea de comandos, un archivo de configuración de sólo lectura. Útil para congelar un perfil de ejecución (inmutable) en el lado de operaciones.





- `includeconf=<fichero>`: Carga un fichero de configuración adicional (ruta relativa a `datadir/`). Permite la separación de roles: base común + sobrecarga local sensible.





- gW-769=1` / `daemonwait=1`: Inicia `bitcoind` en segundo plano y, con `daemonwait`, espera a que finalice la inicialización antes de entregarlo. Esto facilita la integración con supervisores (systemd, runit).





- `pid=<archivo>`: Ubicación del archivo PID.





- `sandbox=<log-y-abort|abort>`: Activa el sandboxing experimental de syscalls: sólo se permiten las syscalls esperadas.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Ejecuta un comando en el arranque o en el apagado.





- `alertnotify=<cmd>`: Activa un comando al recibir una alerta.





- `blocknotify=<cmd>`: Ejecuta un comando para cada nuevo bloque.





- `debug=<category>|1` / `debugexclude=<category>`: Activa/desactiva categorías de registro detalladas (por ejemplo, `net`, `Mempool`, `RPC`, `validation`...).





- `logips=1`: Registra las direcciones IP.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Añade ubicaciones de origen, nombres de hilo y marcas de tiempo precisas a los registros, respectivamente.





- `printtoconsole=1`: Envía trazas/debugs a la consola (*stdout*).





- `help-debug=1`: Muestra la ayuda de la opción debug y se cierra.





- `uacomment=<cmt>`: Añade un comentario a User-Agent P2P.



Ahora hemos terminado de listar la mayoría de los parámetros de configuración. Este archivo `Bitcoin.conf` constituye así el verdadero tablero de su nodo: define la configuración de red, la gestión de Mempool, el uso de disco y memoria, la indexación y la administración general. Si desea obtener más información sobre este archivo y crear uno adaptado a sus necesidades, le recomiendo que utilice el [generador de Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/).



Hemos llegado a la conclusión de este curso BTC 202, que te habrá permitido no sólo comprender los fundamentos del funcionamiento de los nodos y cómo interactúan dentro del sistema, sino también crear el tuyo propio. Ahora eres un Bitcoiner soberano, con tu propio Wallet de autocustodia, transmitiendo tus transacciones a través de tu propio nodo. ¡Enhorabuena!



Ahora puede pasar a la parte final del curso, donde podrá evaluar BTC 202 y, a continuación, obtener su diploma para comprobar que domina todos los conceptos tratados.



Ahora tienes varias opciones abiertas. El siguiente paso lógico es crear su propio nodo Lightning, lo que le permitirá ser totalmente independiente para sus transacciones off-chain. Este será el tema de un próximo curso, que se publicará este otoño de 2025 sobre Plan ₿ Network.



Mientras tanto, le invito a descubrir la formación BTC 204, que le permitirá comprender y dominar los principios de protección de la intimidad en su uso de Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Parte final


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Opiniones y valoraciones


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Examen final


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Conclusión


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>
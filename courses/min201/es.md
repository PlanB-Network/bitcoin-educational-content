---
name: Introducción a la Minería de Bitcoin
goal: Comprender el funcionamiento de la industria minera a través de un ejercicio práctico de reutilización de ASICs.
objectives:
  - Comprender la teoría sobre la minería
  - Comprender la industria minera
  - Convertir un S9 en calefacción
  - Minar el primer satoshi
---

# ¡Tus primeros pasos en la minería!

En este curso, profundizaremos en la industria minera para desmitificar este tema tan complejo. El curso es accesible para todos y no requiere una inversión inicial.

La primera sección será teórica, donde con Ajelex, tendremos una discusión en profundidad sobre diversos temas relacionados con la minería. Esto nos permitirá comprender mejor esta industria y los desafíos económicos y geopolíticos asociados.

En la segunda sección, abordaremos un caso práctico. De hecho, aprenderemos a convertir un minero S9 de segunda mano en una calefacción auxiliar para el hogar. A través de guías escritas y videos, le mostraremos y explicaremos todos los pasos para lograrlo en su propio hogar.

Esperamos que a través de este curso podamos mostrarle que la industria minera es más compleja de lo que parece y estudiarla nos permite matizar el debate ecológico asociado. Si necesita ayuda para su proyecto, hemos creado un grupo de Telegram para los estudiantes y todos los componentes necesarios se pueden encontrar en nuestra plataforma de comercio electrónico.

+++

# Introducción

## ¡Bienvenido!

Bienvenido a MINING 201: una introducción a la minería. Ajelex, Jim y Rogzy están encantados de acompañarte en tus primeros pasos concretos en esta nueva industria. ¡Esperamos que disfrutes del curso y te unas a la aventura de la minería en casa!

### Resumen del curso

En este curso, la primera sección estará dedicada a la teoría de la minería con Ajelex. Discutiremos en profundidad los diversos temas relacionados con la minería, lo que nos permitirá comprender mejor esta industria y los desafíos económicos y geopolíticos asociados.

En la segunda sección, nos embarcaremos en un fascinante caso práctico, aprendiendo a convertir un minero S9 de segunda mano en una calefacción auxiliar para el hogar. Gracias a guías escritas y videos, se explicarán minuciosamente todos los pasos necesarios, garantizando así tu éxito en este proyecto innovador.

Este viaje de aprendizaje te mostrará que la industria minera es más compleja de lo que parece, ofreciendo una perspectiva equilibrada sobre el debate ecológico asociado. Se brindará ayuda continua a través de un grupo de Telegram dedicado para los estudiantes, y todos los componentes necesarios estarán fácilmente disponibles en nuestra plataforma de comercio electrónico.

### Plan de estudios:

Sección Teórica:
* Explicación de la minería.
* La industria minera.
* Los matices de la industria minera.
* La minería en el protocolo de Bitcoin.
* Precio de bitcoin y hashrate, ¿hay una correlación?* Soberanía y regulación
* Entrevista a un profesional de la industria minera

Sección Práctica: Attakai
* Introducción a Attakai.
* Guía de compra.
* Modificación del software de un Antminer S9.
* Reemplazo de los ventiladores para reducir el ruido.
* Configuración de un pool.
* Configuración de un Antminer S9 con Braiins OS+.

¿Listos para comenzar esta emocionante aventura? ¡Sumergámonos juntos en el fascinante mundo de la minería doméstica!

# Conoce todo sobre la minería

## Explicación de la minería

### La Minería Explicada: La Analogía del Rompecabezas

Para explicar de manera simplificada el concepto de la minería, se puede utilizar una analogía relevante: la del rompecabezas. Al igual que un rompecabezas, la minería es una tarea compleja de realizar, pero fácil de verificar una vez completada. En el contexto de la minería de Bitcoin, los mineros se esfuerzan por resolver rápidamente un rompecabezas digital. El primer minero en resolver el rompecabezas presenta su solución a toda la red, que luego puede verificar fácilmente su validez. Esta verificación exitosa permite al minero validar un nuevo bloque y agregarlo a la cadena de bloques de Bitcoin. Como reconocimiento a su trabajo, que implica costos significativos, el minero es recompensado con una cierta cantidad de bitcoins. Esta recompensa es un incentivo financiero para que los mineros continúen su trabajo de validación de transacciones y seguridad de la red Bitcoin.

![imagen](assets/overview/puzzle.png)

Inicialmente en la red Bitcoin, la recompensa otorgada era de 50 bitcoins cada diez minutos, al mismo tiempo que se descubría un bloque cada diez minutos en promedio por los mineros. Esta recompensa se divide a la mitad cada 210,000 bloques, aproximadamente cada cuatro años. Esta remuneración sirve como un poderoso incentivo para alentar a los mineros a participar en el proceso de minería a pesar de su costo energético. Sin la recompensa, la minería, que es costosa en electricidad, sería abandonada, comprometiendo así la seguridad y estabilidad de toda la red Bitcoin.

La recompensa actual de minería es doble. Por un lado, incluye la creación de nuevos bitcoins, que ha pasado de 50 bitcoins cada diez minutos en sus inicios a 6,25 bitcoins hoy en día (2023). Por otro lado, incluye las tarifas de transacción, o tarifas de minería, de las transacciones que el minero elige incluir en su bloque. Cuando se realiza una transacción de bitcoin, se pagan tarifas de transacción. Estas tarifas funcionan como una especie de subasta donde los usuarios indican cuánto están dispuestos a pagar para que su transacción se incluya en el siguiente bloque. Para maximizar su recompensa, los mineros, actuando en su propio interés, seleccionan las transacciones más rentables para incluirlas en su bloque, teniendo en cuenta el espacio limitado disponible. Así, la recompensa de minería se compone tanto de la generación de nuevos bitcoins como de las tarifas de transacción, garantizando un incentivo continuo para los mineros y asegurando la sostenibilidad y seguridad de la red Bitcoin.

### Mineros y sus herramientas: Minería

El proceso de minería consiste en encontrar un hash válido aceptable por la red Bitcoin. Este hash, una vez calculado y encontrado, es irreversible, al igual que las papas convertidas en puré. Verifica una función determinada sin posibilidad de retroceder. Los mineros, compitiendo entre sí, utilizan máquinas para calcular estos hashes. Aunque teóricamente es posible encontrar este hash manualmente, la complejidad de la operación hace que esta opción sea inviable. Por lo tanto, se utilizan computadoras capaces de realizar estos cálculos rápidamente, aunque consumen una cantidad significativa de electricidad.

Al principio, la era de la CPU dominaba, donde los mineros utilizaban sus computadoras personales para la minería de Bitcoin. El descubrimiento de las ventajas de las GPU (tarjetas gráficas) para esta tarea marcó un punto de inflexión, aumentando sustancialmente la tasa de hash y reduciendo el consumo de energía. El progreso no se detuvo allí, con la posterior introducción de los FPGA (field-programmable gate array / matriz de puertas programables en campo). Los FPGA sirvieron como plataforma para el desarrollo de los ASIC (application-specific integrated circuit / circuito integrado específico de aplicación).

![image](assets/overview/chip.png)

Los ASIC son chips, similares a los chips de una CPU, sin embargo, están diseñados para realizar un solo tipo de cálculo específico de la manera más eficiente posible. En otras palabras, una CPU es capaz de realizar una multitud de tipos de cálculos diferentes sin estar especialmente optimizada para un tipo de cálculo u otro, mientras que un ASIC será capaz de realizar un solo tipo de cálculo, pero de manera muy eficiente. En este caso, los ASIC de Bitcoin están diseñados para calcular el algoritmo SHA256.

En la actualidad, los mineros utilizan exclusivamente ASICs dedicadas a esta operación, optimizadas para probar el mayor número posible de combinaciones con el menor consumo de energía y la mayor rapidez posible. Estas computadoras, incapaces de realizar tareas distintas a la minería de Bitcoin, son un testimonio tangible de la continua evolución y especialización de la industria minera de Bitcoin. Esta evolución constante refleja la dinámica intrínseca de Bitcoin, donde un ajuste de la dificultad garantiza la producción de un bloque cada diez minutos a pesar del aumento exponencial de la capacidad de minería.

Para ilustrar la intensidad de este proceso, consideremos un minero típico capaz de realizar 14 TeraHash por segundo, es decir, 14,000 billones de intentos cada segundo para encontrar el hash correcto. A escala de la red de Bitcoin, actualmente se alcanzan aproximadamente 300 HexaHash por segundo, lo que destaca la potencia colectiva movilizada en la minería de Bitcoin.

### Ajuste de la dificultad:

El ajuste de la dificultad es un mecanismo crucial en el funcionamiento de la red de Bitcoin, garantizando que los bloques se minen en promedio cada 10 minutos. Esta duración es un promedio, ya que el proceso de minería es en realidad un juego de probabilidades, similar a lanzar dados con la esperanza de obtener un número menor al número definido por la dificultad. Cada 2016 bloques, la red ajusta la dificultad de minería en función del tiempo promedio necesario para minar los bloques anteriores. Si el tiempo promedio es superior a 10 minutos, la dificultad se reduce, y viceversa si el tiempo promedio es inferior, la dificultad se incrementa. Este mecanismo de ajuste asegura que el tiempo de minería de los nuevos bloques se mantenga constante a lo largo del tiempo, independientemente del número de mineros o de la potencia de cálculo global de la red. Es por esta razón que la Blockchain de Bitcoin también se llama Timechain.

![image](assets/overview/chinaban.png)

* Ejemplo de China:
El caso de China ilustra perfectamente este mecanismo de ajuste de dificultad. Siendo rica en energía abundante y barata, era el principal centro mundial de minería de Bitcoin. En 2021, el país prohibió abruptamente la minería de Bitcoin en su territorio, lo que provocó una caída masiva de la tasa de hash global de la red Bitcoin, del orden del 50%. Esta rápida disminución de la potencia de minería podría haber perturbado gravemente la red Bitcoin, aumentando el tiempo promedio de minería de bloques. Sin embargo, el mecanismo de ajuste de dificultad intervino, reduciendo la dificultad de minería para garantizar que la frecuencia de minería de bloques se mantenga en promedio en 10 minutos. Este caso demuestra la eficacia y la resiliencia del mecanismo de ajuste de dificultad de Bitcoin, que asegura la estabilidad y previsibilidad de la red, incluso ante cambios bruscos e importantes en el panorama de la minería mundial.

### Evolución de las Máquinas de Minería de Bitcoin

En cuanto a la evolución de las máquinas de minería de Bitcoin, es importante destacar que el contexto se orienta más hacia un modelo de negocio tradicional. Los mineros obtienen sus ingresos validando bloques, una tarea con una probabilidad de éxito relativamente baja. El modelo de máquina actualmente en uso, el Antminer S9, aunque es un modelo más antiguo lanzado alrededor de 2016, sigue circulando en el mercado de segunda mano y se negocia entre 100€ y 200€. Sin embargo, el precio de las máquinas de minería varía según el valor de Bitcoin, y un modelo más reciente, el Antminer S19, actualmente se estima en alrededor de 3000€.

Ante la constante evolución tecnológica en el campo de la minería, los profesionales deben posicionarse estratégicamente. La industria minera está sujeta a continuas innovaciones, como lo demuestra el reciente lanzamiento de la versión J del S19 y la próxima versión anticipada del S19 XP, que ofrecen capacidades de minería significativamente superiores. Además, las mejoras no se limitan solo al rendimiento bruto de las máquinas. Por ejemplo, el nuevo modelo S19 XP utiliza un sistema de enfriamiento líquido, una modificación técnica que permite una mejora significativa en la eficiencia energética. Aunque la innovación sigue siendo constante, es probable que las futuras ganancias de eficiencia sean menores en comparación con las observadas hasta ahora, debido a la alcanzada de un cierto umbral de innovación tecnológica.

![image](assets/overview/chipevolution.png)

En conclusión, la industria de la minería de Bitcoin continúa adaptándose y desarrollándose, los actores del campo deben anticipar ganancias de eficiencia más limitadas en el futuro y ajustar sus estrategias en consecuencia. Los avances tecnológicos futuros, aunque aún presentes, probablemente se producirán a una escala más reducida, reflejando una madurez creciente del sector.

## La industria de la minería


### Los Pools de Minería

En la actualidad, la minería de Bitcoin ha evolucionado para convertirse en una industria seria y sustancial, con muchos actores ahora públicos y un número creciente de mineros significativos. Esta evolución ha hecho que la minería sea casi inaccesible para los pequeños actores debido al alto costo asociado con la adquisición de nuevas máquinas de minería. Por lo tanto, surge la cuestión de la distribución del hashrate entre diversos actores del mercado. La situación es compleja, ya que es esencial examinar tanto la distribución del hashrate entre diferentes empresas como entre diferentes pools de minería.

![imagen](assets/overview/pool.png)

Un pool de minería es un grupo de mineros que unen sus recursos de cálculo para aumentar sus posibilidades de minería. Esta cooperación es necesaria porque una pequeña máquina de minería aislada compite con gigantes de la industria, reduciendo sus posibilidades de éxito a un nivel insignificante. La minería funciona según el principio de la lotería, y las posibilidades de ganar un bloque (y por lo tanto la recompensa en Bitcoin) cada diez minutos son extremadamente bajas para un pequeño minero individual. Al unirse en pools, los mineros pueden combinar su poder de cálculo, encontrar bloques con más frecuencia y luego distribuir las recompensas de manera proporcional a la contribución de cada minero al pool.

Por ejemplo, si un pool encuentra un bloque y gana 6,25 bitcoins, un minero que contribuye al 1% del poder de cálculo total del pool recibiría el 1% de los 6,25 bitcoins ganados. Sin embargo, cabe destacar que los pools de minería suelen cobrar una pequeña comisión (generalmente alrededor del 2%) para cubrir los costos operativos de la cooperativa.

### Los softwares utilizados por la industria

En el contexto de la minería de Bitcoin, el papel del software es tan crucial como el hardware. Un ejemplo de esto se ilustra con el papel de Bitmain, un fabricante prolífico que ha desarrollado el Antminer S9. Además del hardware de minería, la industria depende en gran medida de los pools de minería colaborativos, como Brainspool, que controla aproximadamente el 5% del hashrate global de la red Bitcoin.

Los actores de esta industria buscan constantemente aumentar la eficiencia a través del hardware y el software. Por ejemplo, un software popular utilizado en este contexto es BrainsOS Plus. Este software reemplaza el sistema operativo original de la máquina de minería, lo que permite ejecutar las mismas operaciones de manera más eficiente. Con este software, un minero puede aumentar la eficiencia de su máquina en un 25%. Esto significa que, con la misma cantidad de electricidad, la máquina puede producir un 25% más de hashrate, lo que aumenta las recompensas recibidas por el minero. Esta optimización de software es un elemento esencial para la competitividad en la minería de Bitcoin, demostrando la importancia de un enfoque integrado que combine mejoras tanto en hardware como en software para maximizar la eficiencia y los rendimientos.

### La regulación y el costo de la electricidad

Como se ha observado en China y en otros lugares, la regulación tiene una influencia considerable en la minería. Aunque no hay mineros significativos en Francia, la regulación y los altos costos de electricidad en Europa son obstáculos importantes. Los mineros están constantemente buscando electricidad más barata para maximizar sus ganancias. Por lo tanto, el alto costo de la electricidad en Europa y en Francia no favorece la atracción de mineros en estas regiones.

Los mineros tienden a dirigirse a regiones con tarifas eléctricas bajas, a menudo en países en desarrollo o países con excedentes de energía. Por ejemplo, una gran parte del hashrate mundial se encuentra en Texas, Estados Unidos. Texas tiene una red eléctrica independiente que no comparte sus recursos energéticos con otros estados. Esta característica obliga a Texas a producir a menudo más electricidad de la necesaria para evitar escasez, creando así un excedente. Los mineros de Bitcoin aprovechan este excedente al establecerse en Texas, donde pueden minar bitcoins a tarifas eléctricas muy bajas durante los períodos de excedente energético. Esta situación demuestra la influencia significativa de la regulación y los costos de electricidad en la minería de Bitcoin, resaltando la importancia de estos factores en la decisión de los mineros sobre la ubicación de sus operaciones de minería.

### ¿Dónde van los mineros y la gestión de la energía?

Al resaltar el impacto de los mineros de bitcoins en el mundo de la energía, la tendencia es clara: estos actores están constantemente buscando fuentes de electricidad barata, a menudo aquellas que se desperdician o no se aprovechan. Este fenómeno es evidente en regiones con nuevas infraestructuras eléctricas, como aquellas equipadas con represas hidroeléctricas recientes.

Tomemos un ejemplo. En un país que está construyendo una presa, la producción de electricidad a menudo comienza antes de que las líneas de distribución estén completamente operativas. Esta discrepancia puede generar un costo considerable y desalentar la inversión en proyectos de infraestructura de este tipo. Sin embargo, los mineros de bitcoins pueden intervenir como una fuente de demanda flexible, dispuestos a consumir esta "electricidad huérfana", ayudando así a amortizar los costos de infraestructura. La implicación aquí es que se pueden rentabilizar de inmediato nuevas instalaciones, fomentando la creación de nuevas fuentes de electricidad. Este principio también se aplica a escalas más pequeñas. Ya sea un individuo utilizando un generador hidroeléctrico en un pequeño río o un hogar equipado con paneles solares, el exceso de electricidad producido puede utilizarse para alimentar una operación de minería de bitcoins.

En Francia, por ejemplo, el exceso de electricidad de los paneles solares se inyecta en la red y los productores son remunerados con un crédito de consumo por parte de EDF. De manera similar, se puede imaginar a un minero operando con este exceso de electricidad, apagándose cuando la demanda local iguala la oferta. Aunque esto puede parecer egoísta, priorizando la producción de bitcoins en lugar de apoyar la red eléctrica local, presenta otro ángulo: la estabilización de la red eléctrica. La gestión compleja de los excedentes de electricidad, a veces incluso con costos asociados a su eliminación, puede simplificarse en gran medida. Los mineros de bitcoins pueden absorber estos excedentes, actuando como un amortiguador flexible, ajustando la demanda en lugar de la oferta. En un mundo donde la producción de electricidad a partir de fuentes renovables (poco controlables) está en constante aumento, los mineros pueden desempeñar un papel clave para garantizar el equilibrio de nuestras redes eléctricas, al tiempo que se benefician de la electricidad barata o excedente para alimentar sus operaciones de minería.

### La centralización de la minería

La centralización de la minería se aborda como un desafío importante. Grandes actores, como Foundry, dominan el mercado, lo que puede potencialmente llevar a la censura de transacciones. Esta centralización también puede hacer que la red sea vulnerable a ataques, como el ataque del 51%, donde un actor o grupo controla más del 50% del poder de hash de la red, lo que les permite controlar y manipular la red.
Riesgo de regulación Se destaca que si un país como Estados Unidos decidiera regular o prohibir ciertas transacciones de Bitcoin, esto podría tener un impacto considerable en la red, especialmente si gran parte del poder de hash está centralizado en ese país.

![image](assets/overview/foundry.png)

Para combatir esta centralización, se abordan diferentes estrategias:
* Home Mining: La idea del Home Mining se basa en la descentralización de la actividad minera. Alentar a las personas a participar en la actividad minera desde sus hogares, distribuyendo así el hashrate de manera más amplia.
* Stratum V2: El protocolo Stratum V2 ofrece otro enfoque. A diferencia de su predecesor, Stratum V2 permite a los mineros elegir las transacciones que incluirán en los bloques que minan. Esta capacidad refuerza la resistencia a la censura y reduce la capacidad de las grandes pools de minería para dominar la red. Al dar más poder a los mineros individuales, el protocolo Stratum V2 puede desempeñar un papel crucial en la lucha contra la centralización del hashrate.
Open-Sourcing de Software de Minería
* Open-Sourcing de software de minería: Esta es otra estrategia potencialmente efectiva. Al hacer que el software de minería sea accesible para todos, los pequeños mineros tendrían las mismas oportunidades que las grandes empresas mineras para participar y contribuir a la red blockchain. Este enfoque fomentaría una distribución más amplia del hashrate, contribuyendo así a la descentralización de la red.
* Diversificación de actores y geografía: Fomentar la participación de diversos actores de diferentes regiones geográficas en la minería de criptomonedas también puede ser efectivo. Al diversificar geográficamente el hashrate, se vuelve más difícil para un solo actor o país ejercer un control o influencia desproporcionada sobre la red. Este enfoque puede contribuir a proteger la red contra posibles ataques y fortalecer su descentralización.

La conclusión general es que la descentralización es crucial para la seguridad y resiliencia de la red Bitcoin. Si bien la centralización puede ofrecer ventajas en términos de eficiencia, expone a la red a riesgos significativos, como la censura y los ataques del 51%. Iniciativas como Takai y la adopción de nuevos protocolos como Stratum V2 son pasos importantes hacia la descentralización y protección de la red Bitcoin contra estas amenazas.

## Las sutilezas de la industria minera

### El principio de Attakai

En el contexto actual, la práctica de la minería de Bitcoin en S9 puede parecer compleja, pero un análisis más profundo abre el camino a alternativas innovadoras. El principio de Attakai se basa en una reflexión sobre el uso de instalaciones mineras en diversos tipos de edificios, como escuelas u hospitales. La idea principal es colocar algunas máquinas mineras en diferentes lugares, lo que permite reutilizar el calor emitido por estas máquinas para calentar los establecimientos. Al optar por modelos más eficientes como el S19, sería posible distribuir la actividad minera, favoreciendo así un mejor rendimiento general y contribuyendo de manera útil a la sociedad. Esta iniciativa tiene como objetivo competir con las grandes instalaciones mineras centralizadas utilizando el calor generado por las máquinas mineras de manera productiva y eficiente.

La iniciativa Attakai surge de una experimentación personal de minería en el hogar realizada por dos amigos que deseaban participar activamente en la red de Bitcoin. Se encontraron con obstáculos importantes, como el alto nivel de ruido de los equipos de minería, diseñados para uso industrial y no doméstico. Para solucionar este problema, se realizaron modificaciones de hardware a las máquinas mineras. Se reemplazaron los equipos originales por ventiladores más eficientes y silenciosos, lo que hizo que la minería en el hogar fuera más accesible y menos molesta. Además, la adición de un adaptador Wi-Fi eliminó la necesidad de una conexión Ethernet por cable, simplificando aún más el proceso de minería en el hogar. En invierno, estos mineros modificados se utilizaron como fuente de calefacción, convirtiendo una molestia en un beneficio.

Al exponer su proyecto a la comunidad de Bitcoin y ante el interés generado, los inventores de Attakai decidieron publicar guías detalladas en la plataforma Découvre Bitcoin, permitiendo que cualquiera pueda reproducir su experiencia de minería en el hogar. Ahora están considerando ampliar este concepto más allá del ámbito doméstico. El objetivo es demostrar cómo un minero modificado puede convertirse en una calefacción adicional silenciosa utilizada durante el invierno, ofreciendo una transición suave a una segunda parte de formación dedicada a la implementación práctica de estas modificaciones, ilustrada con videos explicativos. Sin embargo, la pregunta sigue siendo si esta iniciativa puede expandirse a una escala más grande, ofreciendo así una alternativa realista y sostenible a las estructuras de minería centralizadas actuales.

### ¿Cuál es el límite de esta descentralización?

Aunque la idea de descentralizar la minería mediante el uso productivo del calor generado parece prometedora, tiene ciertos límites y quedan preguntas sin respuesta. Establecimientos con alto consumo de energía, como saunas y piscinas, podrían beneficiarse de este concepto utilizando el calor generado por los mineros para calentar el agua de sus instalaciones. Algunos miembros de la comunidad Bitcoin ya están implementando esta práctica, explorando diferentes métodos para utilizar de manera eficiente el calor generado por los equipos de minería. Por ejemplo, teóricamente, un salón de eventos podría ser calentado por tres o cuatro S19, cada uno consumiendo 3000 vatios y generando una cantidad equivalente de calor.

Sin embargo, es importante destacar que el consumo de energía y la producción de calor son equivalentes, ya sea que la energía sea utilizada por un radiador eléctrico o por un minero. Por cada kilovatio de electricidad utilizado, la cantidad de calor producido será la misma en ambos casos. La diferencia radica en que el minero no solo proporcionará calor, sino también una recompensa en bitcoins, lo que ofrece un incentivo económico para utilizar un minero en lugar de un simple radiador eléctrico. Esta recompensa adicional podría ayudar a mitigar las preocupaciones relacionadas con el alto consumo de energía de los mineros.

La cuestión de la eficiencia y la viabilidad a largo plazo del uso de los mineros de bitcoin para la calefacción sigue abierta. Las continuas innovaciones en el hardware de minería y en las tecnologías de calefacción pueden abrir nuevas vías para un uso más eficiente del calor generado por la minería, contribuyendo así a la viabilidad de este enfoque en el futuro.

### ¿Por qué recibir recompensas en BTC?

La cuestión de recibir recompensas en bitcoin en lugar de otra moneda es fundamental en el sistema ideado por Satoshi Nakamoto. La creación de Bitcoin se caracteriza por un límite fijo de 21 millones de unidades. El objetivo era encontrar una forma justa de distribuir estas unidades recién creadas. Los mineros, al proporcionar su poder de cálculo para asegurar la red y hacer que cualquier ataque sea cada vez más costoso, protegen eficazmente la red de Bitcoin. A cambio de esta contribución crucial, son recompensados con los nuevos bitcoins creados, facilitando así la distribución de las monedas en el ecosistema.

Es un sistema de ganar-ganar. Los mineros son remunerados tanto por asegurar la red como por aprobar las transacciones. Los nuevos bitcoins creados se dan como incentivo para fortalecer la seguridad, y las tarifas de transacción son un ingreso adicional por aprobar las transacciones. Estos dos elementos combinados constituyen la recompensa total por la minería. La cuestión del futuro de la minería surge debido a la reducción programada de las recompensas de minería, que se reducen a la mitad cada cuatro años, en un evento conocido como "halving". Para 2032, la recompensa del bloque será inferior a un bitcoin, y para 2140, no se crearán nuevos bitcoins. En este punto, los mineros dependerán únicamente de las tarifas de transacción como compensación. La red de Bitcoin deberá soportar una gran cantidad de transacciones, con tarifas lo suficientemente altas, para garantizar la rentabilidad de la minería.

La aparición de la Lightning Network, que permite transacciones rápidas y de bajo costo fuera de la cadena principal de Bitcoin, plantea preguntas sobre el futuro de la minería. La Lightning Network tiene el potencial de reducir significativamente las tarifas de transacción, lo que afectaría los ingresos de los mineros. Sin embargo, esto dependerá de la adopción y el uso de la Lightning Network en comparación con la red principal de Bitcoin. En un escenario pesimista, los mineros podrían encontrar rentable minar incluso a pérdida si han amortizado sus costos y tienen acceso a electricidad barata. En un escenario más optimista, las tarifas de transacción en la red principal de Bitcoin podrían seguir siendo lo suficientemente altas como para mantener la rentabilidad de la minería.

### ¿Qué se debe incluir en un bloque de Bitcoin?

En cuanto a la cuestión de qué se debe incluir en un bloque de Bitcoin, es crucial considerar la naturaleza complementaria de las diferentes capas de la red de Bitcoin. Aunque la Lightning Network puede permitir transacciones más rápidas y menos costosas, aún depende de la capa base de Bitcoin, a menudo llamada "capa de liquidación", para la apertura y cierre de canales de pago.

Con el crecimiento previsto de la Lightning Network y el consiguiente aumento en la apertura y cierre de canales, el espacio en los bloques de Bitcoin se volverá cada vez más valioso. La comunidad de Bitcoin tiende a valorar la preservación de este espacio, reconociendo su limitación intrínseca. Esta conciencia ha dado lugar a discusiones sobre el uso legítimo o no del espacio de los bloques, con preocupaciones sobre el "spam" en la cadena de bloques mediante transacciones consideradas no esenciales.

![image](assets/overview/block.png)

La especulación rodea el uso futuro del espacio de bloques, pero generalmente se acepta que es un recurso escaso que debe utilizarse de manera prudente. Aunque existe el deseo de llenarlo, es esencial preservarlo para garantizar la viabilidad a largo plazo de la red de Bitcoin, anticipando un aumento futuro en la demanda de espacio en los bloques. Como en cualquier mercado libre, la oferta y la demanda regularán el uso del espacio de bloques. Con una oferta limitada, las partes interesadas deberán tomar decisiones informadas sobre el uso de este valioso espacio para garantizar la eficiencia y la seguridad a largo plazo de la red de Bitcoin.

## La minería en el protocolo de Bitcoin

El papel de los mineros en la red de Bitcoin ha sido objeto de intenso debate durante la guerra de bloques. Aunque son esenciales para la seguridad y funcionalidad de la red, los mineros no necesariamente tienen el poder supremo en el ecosistema de Bitcoin. El equilibrio entre los mineros, los nodos y los usuarios finales garantiza la integridad y distribución de la red.

### La guerra de bloques

Durante la guerra de bloques, muchos mineros se opusieron a ciertas evoluciones de la red, destacando la tensión entre los diferentes actores del ecosistema. La pregunta sigue siendo cómo equilibrar el poder entre los mineros, los nodos y los usuarios para garantizar la seguridad a largo plazo de Bitcoin.

Seguridad y Equilibrio de Poder

![imagen](assets/overview/blocksize-wars--BTC-vs-BCH-.webp)

El dilema de la seguridad de Bitcoin se basa en un delicado equilibrio. Aunque los mineros desempeñan un papel crucial en la validación y creación de bloques, los nodos mantienen la integridad al verificar y validar las transacciones y los bloques. Un bloque incorrecto o fraudulento será rechazado por los nodos, censurando así al minero y preservando la seguridad de la red. El poder también es detentado por los nodos y los usuarios de la red de Bitcoin. Los nodos tienen el poder de verificación y validación, mientras que los usuarios tienen el poder de elegir qué cadena de bloques utilizar. Esta distribución de poder asegura la distribución y la integridad de la red de Bitcoin.

La guerra de bloques ha revelado la incertidumbre y la tensión inherentes a la gestión de la red de Bitcoin. Aunque Bitcoin Core es actualmente la cadena dominante, el debate sobre la gobernanza y la gestión de la red persiste.
En última instancia, la responsabilidad se comparte entre todos los actores de la red de Bitcoin. Una disminución en el número de usuarios, nodos o mineros podría debilitar la red, aumentando el riesgo de centralización y vulnerabilidad a los ataques. Cada actor contribuye a la robustez y seguridad de la red, reforzando la importancia de mantener un equilibrio de poder y responsabilidad.

### El poder de los mineros

La elegante teoría de juegos de Satoshi Nakamoto establece una situación en la que cada actor de la red de Bitcoin está incentivado a actuar correctamente para proteger tanto sus propios intereses como los de los demás participantes. Esto crea un equilibrio donde el mal comportamiento puede ser castigado, fortaleciendo así la seguridad y estabilidad de todo el sistema. A pesar de este equilibrio, los Estados siguen siendo una amenaza potencial. Como se indica en la presentación en Surfing Bitcoin 2022, los Estados pueden intentar atacar la industria minera, exponiendo a la red de Bitcoin a riesgos de centralización y ataque. Escenarios hipotéticos como un ataque militar dirigido a las instalaciones de producción de hardware de minería resaltan la importancia de la diversificación geográfica e industrial para la resiliencia de la red de Bitcoin.

![image](assets/overview/miner.png)

La centralización de la producción de hardware de minería en China plantea otro riesgo. La negativa a exportar máquinas de minería o la acumulación de hashrate para un posible ataque del 51% por parte de China resaltan la necesidad de una producción diversificada de hardware de minería. Frente a estos riesgos, la comunidad de Bitcoin está explorando activamente soluciones. Empresas como Intel están considerando la producción de equipos de minería en Estados Unidos, contribuyendo a la distribución de la producción. Otras iniciativas, como la de Block con su Mining Development Kit (MDK) de código abierto, tienen como objetivo reducir el monopolio en el diseño y producción de hardware de minería, permitiendo una distribución más amplia del hashrate. En el centro de estas discusiones se encuentra la misión fundamental de Bitcoin: ser una red de intercambio de valor resistente a la censura. La comunidad de Bitcoin se esfuerza constantemente por fortalecer la distribución, la resistencia a la censura y la antifragilidad de la red, rechazando propuestas como el cambio a la prueba de participación, que no se alinean con estos principios fundamentales.

### La conexión física de la prueba de trabajo vs la Prueba de participación

La relación entre el precio de Bitcoin y la tasa de hash, ¿existe una correlación?

El precio de Bitcoin y la tasa de hash, que representa la cantidad de poder de cómputo dedicado a la minería de Bitcoin, son dos métricas importantes que a menudo se analizan en conjunto. Algunos argumentan que existe una correlación entre el precio de Bitcoin y la tasa de hash, lo que significa que cuando el precio de Bitcoin sube, también lo hace la tasa de hash, y viceversa.

La lógica detrás de esta correlación es que un precio más alto de Bitcoin atrae a más mineros, lo que aumenta la competencia y la tasa de hash. Por otro lado, cuando el precio de Bitcoin cae, algunos mineros pueden volverse menos rentables y salir del mercado, lo que reduce la tasa de hash.

Sin embargo, es importante tener en cuenta que esta correlación no es perfecta y puede haber otros factores que influyan en el precio de Bitcoin y la tasa de hash de manera independiente. Por ejemplo, eventos macroeconómicos, regulaciones gubernamentales, noticias del mercado y cambios en la dificultad de la minería también pueden afectar tanto el precio de Bitcoin como la tasa de hash.

En resumen, si bien existe una correlación general entre el precio de Bitcoin y la tasa de hash, no es una relación directa y puede haber otros factores que influyan en estas métricas de manera independiente.
Minar para obtener ganancias o para la red?
La soberanía y la regulación son temas importantes en el contexto del minado de Bitcoin. La soberanía se refiere a la capacidad de los individuos y las comunidades para tener control sobre sus propias acciones y decisiones en relación con el minado de Bitcoin. La regulación, por otro lado, se refiere a las leyes y políticas que se implementan para supervisar y controlar el minado de Bitcoin.

En el debate sobre la soberanía, algunos argumentan que el minado de Bitcoin es una forma de empoderamiento financiero y tecnológico, ya que permite a las personas tener control sobre su propio dinero y participar en la red descentralizada de Bitcoin. Sin embargo, otros argumentan que la falta de regulación puede llevar a la centralización del poder de minado en manos de unos pocos actores dominantes, lo que podría socavar la naturaleza descentralizada de Bitcoin.

En cuanto a la regulación, algunos argumentan que es necesaria para proteger a los usuarios y prevenir actividades ilegales, como el lavado de dinero y el financiamiento del terrorismo. Sin embargo, otros argumentan que una regulación excesiva podría obstaculizar la innovación y limitar la accesibilidad al minado de Bitcoin.

En última instancia, encontrar un equilibrio entre la soberanía y la regulación es un desafío importante para la comunidad de Bitcoin. Se requiere un enfoque cuidadoso y colaborativo para garantizar que el minado de Bitcoin siga siendo seguro, accesible y alineado con los valores fundamentales de la red.

### ¿Soberanía antes que beneficio?

Para abordar la cuestión crucial de la riqueza a través de la minería, es importante considerar diversas perspectivas y enfoques. Las preguntas sobre la rentabilidad de la minería son frecuentes, con interrogantes sobre la compra de acciones de empresas como Riot o el alquiler de máquinas de minería en países con bajos costos energéticos como Islandia o Rusia. Antes de aventurarse en la minería, una consideración esencial sería comparar la rentabilidad de la minería con la compra directa de Bitcoin. Si el costo de minar un Bitcoin supera el costo de compra directa, generalmente es más prudente comprar el Bitcoin directamente. Esto evita los múltiples desafíos y costos asociados con el proceso de minería.

Sin embargo, la minería ofrece oportunidades únicas para involucrarse en el ecosistema de Bitcoin. Por ejemplo, minar Bitcoin en invierno puede ser una forma ingeniosa de calentar su hogar mientras genera ingresos en Bitcoin. Otra opción es invertir en empresas que venden hardware de minería y que almacenan y gestionan las máquinas en ubicaciones con bajos costos energéticos, lo que brinda acceso a tarifas eléctricas ventajosas sin las molestias de la gestión de equipos.

A pesar de estas opciones, la minería presenta desafíos significativos. El conocido dicho en el mundo de las criptomonedas, "No tus claves, no tus Bitcoins", encuentra una resonancia similar en el mundo de la minería: "No tu tasa de hash, no tu recompensa". Las historias de decepciones y máquinas desconectadas son comunes, con muchos actores prometiendo resultados excepcionales pero sin cumplirlos. Los problemas de suministro eléctrico y las fallas de las máquinas pueden dejar a los inversores impotentes, con equipos costosos que no controlan. En este contexto, la prudencia y una comprensión profunda del sector minero son cruciales antes de aventurarse en él. Aunque existen oportunidades de ganancias, los riesgos son significativos y se requiere un enfoque informado y reflexivo para navegar en este campo complejo y a menudo impredecible. Por lo tanto, es vital realizar una investigación exhaustiva y considerar cuidadosamente las ventajas y desventajas antes de comprometerse con la minería de Bitcoin.

![image](assets/overview/self.png)

### Bitcoins Vírgenes

La minería prohibida en Europa?

Con la cuestión del potencial de prohibición de la minería en Europa, las discusiones sobre la regulación se vuelven cada vez más relevantes. El paisaje regulatorio fluctuante puede influir considerablemente en la industria minera de Bitcoin. La prohibición de la minería en Europa es un escenario posible, especialmente considerando los precedentes en China. Aunque las operaciones mineras continúan en China a pesar de la prohibición, Europa podría seguir un camino similar. Una distribución más amplia de la tasa de hash en diferentes regiones podría ayudar a fortalecer la comunidad minera en Europa, permitiéndoles oponerse eficazmente a los malentendidos y conceptos erróneos sobre la minería, su impacto ambiental y su huella en la red eléctrica.

![imagen](assets/overview/regulation.jpg)

Frente a campañas como las de Greenpeace y las cifras a menudo engañosas de algunos estudios, la mejor arma sigue siendo la información verídica. Es esencial informar al público en general y a los tomadores de decisiones sobre la realidad de la minería, su complejidad y sus matices, en lugar de permitirles basarse en estereotipos e información inexacta. Cuantas más personas estén informadas y sean conscientes de lo que realmente es la minería, mejor podrá defenderse la industria contra posibles regulaciones restrictivas.

En conclusión, a pesar del riesgo regulatorio y la posibilidad de una prohibición de la minería en Europa, la arma más poderosa sigue siendo la educación y la información. Una comprensión clara y precisa de la minería, su funcionamiento y su impacto puede ayudar a desmitificar la industria y combatir la desinformación, ofreciendo así una mejor resistencia a las regulaciones potencialmente perjudiciales. La iniciativa de formar e informar a las personas sobre la minería, como lo hace esta discusión, es un paso en la dirección correcta para garantizar la sostenibilidad y el crecimiento de la minería en Europa y en todo el mundo. Los esfuerzos continuos para educar e informar son esenciales para asegurar un futuro seguro y próspero para la industria de la minería de Bitcoin.

# Minería en casa y reutilización del calor

## Attakai - ¡La minería en casa hecha posible y accesible!

Attakai, que significa "la temperatura ideal" en japonés, es el nombre de la iniciativa para descubrir la minería de bitcoins a través de la reutilización del calor lanzada por @ajelexBTC y @jimzap21 con Découvre Bitcoin.
Esta guía de modernización de un ASIC servirá como base para aprender más sobre la minería, su funcionamiento y la economía subyacente, demostrando la posibilidad de adaptar un minero de Bitcoin para su uso como radiadores en viviendas. Esto ofrece más comodidad y ahorro, permitiendo a los participantes obtener reembolsos en BTC sin KYC en su factura de calefacción eléctrica.

Bitcoin ajusta automáticamente la dificultad de minería y recompensa a los mineros por su participación, sin embargo, la concentración del hashrate puede plantear riesgos para la neutralidad de la red. Utilizar la potencia de cálculo de Bitcoin para soluciones de calefacción beneficia directamente a la red misma, aumentando la distribución de la potencia de cálculo.

### ¿Por qué reutilizar el calor de un ASIC?

Es importante entender la relación entre la energía y la producción de calor en un sistema eléctrico.

Por una inversión de 1 kW de energía eléctrica, un radiador eléctrico produce 1 kW de calor, ni más ni menos. Los nuevos radiadores no son más eficientes que los radiadores tradicionales. Su ventaja radica en su capacidad para difundir el calor de manera continua y uniforme en una habitación, brindando así más comodidad en comparación con los radiadores tradicionales que alternan entre una alta potencia de calefacción y la falta de calefacción, generando fluctuaciones regulares de temperatura e incomodidad.

Una computadora, o más ampliamente una tarjeta electrónica, no consume energía para realizar cálculos, simplemente necesita que la energía circule en sus componentes para funcionar. El consumo de energía se debe a la resistencia eléctrica de los componentes, que produce pérdidas y genera calor, esto es lo que se conoce como el efecto Joule.

Algunas empresas han tenido la idea de combinar las necesidades de potencia de cálculo y las necesidades de calefacción mediante radiadores/servidores. La idea es distribuir los servidores de una empresa en pequeñas unidades que podrían colocarse en viviendas u oficinas. Sin embargo, esta idea enfrenta varios problemas. Las necesidades de los servidores no están relacionadas con las necesidades de calefacción y las empresas no pueden utilizar las capacidades de cálculo de sus servidores de manera flexible. También existen limitaciones en el ancho de banda que los particulares pueden tener. Todas estas restricciones no permiten que la empresa rentabilice estas costosas instalaciones ni brinde una oferta estable de servidores en línea sin tener centros de datos capaces de asumir el control cuando no se necesita calefacción.

"El calor de tu computadora no se desperdicia si necesitas calentar tu hogar. Si estás utilizando calefacción eléctrica en tu casa, entonces el calor de tu computadora no es un desperdicio. Es el mismo costo si generas este calor con tu computadora. Si tienes otro sistema de calefacción más barato que el eléctrico, entonces el desperdicio está solo en la diferencia de costo. Si es verano y estás utilizando aire acondicionado, entonces es el doble. La minería de bitcoins debería ocurrir donde sea más barata. Tal vez sea en lugares con clima frío y calefacción eléctrica, donde la minería se vuelva gratuita".

Bitcoin y su prueba de trabajo se destacan porque ajustan automáticamente la dificultad de la minería en función de la cantidad de cálculos realizados por toda la red, esta cantidad se llama hashrate y se expresa en hash/segundo. Hoy en día se estima en 380 Exahash/segundo, lo que equivale a 380 billones de billones de hash/segundo. Este hashrate representa trabajo y, por lo tanto, una cantidad de energía gastada. Cuanto mayor sea el hashrate, mayor será la dificultad y viceversa. De esta manera, se puede activar o desactivar un minero de Bitcoin en cualquier momento sin afectar a la red, a diferencia de los radiadores/servidores que necesitan mantenerse estables para ofrecer su servicio. El minero es recompensado por su participación, por pequeña que sea, en relación con la de los demás.

En resumen, un radiador eléctrico y un minero de Bitcoin producen ambos 1 kW de calor por cada 1 kW de electricidad gastada. Sin embargo, el minero también recibe bitcoins como recompensa. Independientemente del precio de la electricidad, el precio de bitcoin o la competencia en la actividad minera en la red de Bitcoin, es económicamente más ventajoso calentarse con un minero que con un radiador eléctrico.

### El valor agregado para Bitcoin

Lo importante de entender es cómo la minería contribuye a la descentralización de Bitcoin.
Varias tecnologías existentes se han combinado ingeniosamente para dar vida al consenso de Nakamoto. Este consenso permite recompensar económicamente a los actores honestos por su participación en el funcionamiento de la red de Bitcoin, al mismo tiempo que desalienta a los actores deshonestos. Este es uno de los puntos clave que permite que la red exista de manera sostenible.
Los actores honestos, aquellos que realizan la minería de acuerdo con las reglas, compiten entre sí para obtener la mayor parte posible de la recompensa por la producción de nuevos bloques. Este incentivo económico naturalmente conduce a una forma de centralización, ya que las empresas eligen especializarse en esta actividad lucrativa al reducir sus costos a través de economías de escala. Estos actores industriales tienen una posición ventajosa para la compra, mantenimiento de máquinas y negociación de tarifas de electricidad al por mayor.

> "Al principio, la mayoría de los usuarios ejecutarían nodos de red, pero a medida que la red creciera más allá de cierto punto, cada vez más se dejaría en manos de especialistas con granjas de servidores de hardware especializado. Una batería de servidores solo necesitaría un nodo en la red y el resto de la LAN se conectaría a ese nodo".
>
> - Satoshi Nakamoto - 2 de noviembre de 2008

Algunas entidades poseen un porcentaje considerable de la tasa de hash total en grandes granjas de minería. Se puede observar la reciente ola de frío en los Estados Unidos, donde una parte importante de la tasa de hash se desconectó para redirigir la energía a los hogares que necesitaban electricidad de manera excepcional. Durante varios días, los mineros fueron incentivados económicamente a apagar sus granjas, por lo que se puede ver este clima excepcional en la curva de la tasa de hash de Bitcoin.

Este tema podría volverse problemático y representar un riesgo importante para la neutralidad de la red. Un actor que posea más del 51% de la tasa de hash podría censurar transacciones más fácilmente si así lo deseara. Por eso es importante distribuir la tasa de hash entre múltiples actores en lugar de entidades centralizadas que podrían ser más fácilmente confiscadas por un gobierno, por ejemplo.

**Si los mineros están distribuidos en miles, incluso millones, de hogares en todo el mundo, se vuelve muy complicado para un Estado tomar el control.**

Cuando sale de fábrica, un minero no es adecuado para servir como calefactor en una vivienda debido a dos problemas principales: ruido excesivo y falta de ajuste. Sin embargo, estos problemas se pueden resolver fácilmente mediante modificaciones de hardware y software, lo que permite obtener un minero mucho más silencioso y que se puede configurar y automatizar como los calentadores eléctricos modernos.

**Attakaï es una iniciativa educativa que te enseña cómo realizar una adaptación del Antminer S9 de la manera más económica posible.**

Es una excelente oportunidad para aprender practicando y ser recompensado por tu participación con satoshis sin necesidad de KYC.

## Guía de compra para un ASIC de segunda mano

En esta sección veremos las mejores prácticas para comprar un Bitmain Antminer S9 de segunda mano, la máquina en la que se basará este tutorial de retrofitting en radiador. Esta guía también funciona para otros modelos de ASIC, ya que es una guía de compra general para equipos de minería de segunda mano.

El Antminer S9 es un dispositivo ofrecido por Bitmain desde mayo de 2016. Consume 1400W de electricidad y produce 13.5 TH/s. Aunque se considera antiguo, sigue siendo una excelente opción para comenzar a minar. Dado que se produjo en grandes cantidades, es fácil encontrar piezas de repuesto en abundancia en muchas regiones del mundo. Por lo general, se puede adquirir de persona a persona en sitios como Ebay o LeBonCoin, ya que los revendedores dirigidos a profesionales ya no lo ofrecen debido a su menor competitividad en comparación con máquinas más nuevas. Es menos eficiente que ASIC como el Antminer S19, lanzado en marzo de 2020, pero esto lo convierte en un hardware de segunda mano asequible y más adecuado para las modificaciones que vamos a realizar.

El Antminer S9 existe en varias variantes (i, j) que realizan cambios menores en el hardware de primera generación. No creemos que este elemento deba influir en su decisión de compra y esta guía funciona para todas estas variantes.

El precio de los ASIC varía según muchos factores como el precio del bitcoin, la dificultad de la red, la eficiencia de la máquina y el costo de la electricidad. Por lo tanto, es difícil dar una estimación precisa para la compra de una máquina de segunda mano. En febrero de 2023, el precio esperado en Francia generalmente oscila entre 100€ y 200€, pero estos precios pueden cambiar rápidamente.

![imagen](assets/guide-achat/1.jpeg)

El Antminer S9 está compuesto por las siguientes partes:

- 3 hashboards que contienen los chips que producen el hash

![imagen](assets/guide-achat/2.jpeg)

- Una tarjeta de control que incluye una ranura para una tarjeta SD, un puerto Ethernet y conectores para los hashboards y los ventiladores. Es el cerebro de su ASIC.

![imagen](assets/guide-achat/3.jpeg)

- 3 cables de datos que conectan los hashboards con la tarjeta de control

![imagen](assets/guide-achat/4.jpeg)

- La fuente de alimentación que funciona con 220V y, por lo tanto, se puede conectar como un electrodoméstico común

![imagen](assets/guide-achat/5.jpeg)

- 2 ventiladores de 120mm

![imagen](assets/guide-achat/6.jpeg)

- Un cable macho C13

![imagen](assets/guide-achat/7.jpeg)

Cuando compres una máquina de segunda mano, es importante verificar que todas las piezas estén incluidas y funcionales. Durante el intercambio, debes pedir al vendedor que encienda la máquina para verificar su correcto funcionamiento. Es importante comprobar que el dispositivo se encienda correctamente y luego verificar la conectividad a Internet conectando un cable Ethernet y accediendo a la interfaz de inicio de sesión de Bitmain a través de un navegador web en la misma red local. Puedes encontrar esta dirección IP conectándote a la interfaz de tu enrutador de Internet y buscando los dispositivos conectados. Esta dirección debería tener el siguiente formato: 192.168.x.x

![image](assets/guide-achat/8.gif)

También verifica que las credenciales predeterminadas funcionen (nombre de usuario: root, contraseña: root). Si las credenciales predeterminadas no funcionan, deberás restablecer la máquina.

![image](assets/guide-achat/9.jpeg)

Una vez conectado, deberías poder ver el estado de cada placa hash en el panel de control. Si el minero está conectado a un grupo de minería, deberías ver que todas las placas hash funcionen. Es importante tener en cuenta que los mineros hacen mucho ruido, es normal. Asegúrate también de que los ventiladores funcionen correctamente.

Luego puedes eliminar el grupo de minería del antiguo propietario para configurar el tuyo propio más adelante. Si lo deseas, también puedes inspeccionar las placas hash desmontando la máquina. Sin embargo, este paso es más complejo y requiere más tiempo y algunas herramientas. Si deseas realizar este desmontaje, puedes consultar la siguiente parte de este tutorial que detalla cómo hacerlo. Es importante tener en cuenta que los mineros acumulan mucho polvo y requieren un mantenimiento regular. Podrás observar esta acumulación de polvo y la calidad del mantenimiento al desmontar la máquina.
Después de revisar todos estos puntos, puedes comprar tu máquina con un alto grado de confianza. En caso de duda, consulta a la comunidad.

Para resumir esta guía en una frase: **"No confíes, verifica"**.

[También puedes recurrir a profesionales en la reacondicionamiento de máquinas de minería, como nuestro socio 21energy. Ofrecen S9 probados, limpios y con el software BraiiinOS+ ya instalado. Con el código de afiliación "decouvre", obtendrás un 10% de descuento en la compra de un S9 mientras apoyas el proyecto Attakai.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)

## Guía de compra de piezas para modificaciones de hardware del S9

Propietario de un Antminer S9, probablemente sepas lo ruidoso y voluminoso que puede ser este equipo. Sin embargo, es posible convertirlo en una calefacción silenciosa y conectada siguiendo algunos pasos simples. En esta sección, te presentaremos los equipos necesarios para realizar las modificaciones.
Si eres un hábil manitas y estás buscando convertir un minero en una calefacción, este tutorial es para ti. Queremos advertirte que las modificaciones realizadas a un dispositivo electrónico pueden presentar riesgos eléctricos. Por lo tanto, es esencial tomar todas las precauciones necesarias para evitar cualquier daño o lesión.

1. Reemplazar los ventiladores

Los ventiladores originales del Antminer S9 son demasiado ruidosos para usar tu Antminer como calefacción. La solución es reemplazarlos por ventiladores más silenciosos. Nuestro equipo ha probado varios modelos de la marca Noctua y ha seleccionado el Noctua NF-A14 iPPC-2000 PWM como la mejor opción, asegúrate de elegir la versión de 12V de los ventiladores. Este ventilador de 140mm puede generar hasta 1200W de calefacción manteniendo un nivel teórico de ruido de 31 dB. Para poder instalar estos ventiladores de 140mm, deberás utilizar un adaptador de 140mm a 120mm que podrás encontrar en la tienda de DécouvreBitcoin. También agregaremos rejillas de protección de 140mm.

![imagen](assets/piece/1.jpeg)
![imagen](assets/piece/2.jpeg)
![imagen](assets/piece/3.jpeg)

El ventilador de la fuente de alimentación también es bastante ruidoso y debe ser reemplazado. Recomendamos el Noctua NF-A6x25 PWM. Ten en cuenta que los conectores de los ventiladores Noctua no son los mismos que los originales, por lo que necesitarás un adaptador para conectarlos, con 2 será suficiente. También asegúrate de elegir la versión de 12V del ventilador.

![imagen](assets/piece/4.jpeg)
![imagen](assets/piece/5.jpeg)

2. Agregar un puente WIFI/Ethernet

En lugar de utilizar un cable Ethernet, puedes conectar tu Antminer a través de WIFI agregando un puente WIFI/Ethernet. Hemos seleccionado el vonets vap11g-300 porque permite recuperar fácilmente la señal WIFI de tu caja de Internet y transmitirla a tu Antminer a través de Ethernet sin crear una subred. Si tienes habilidades eléctricas, puedes alimentarlo directamente con la fuente de alimentación del Antminer sin necesidad de agregar un cargador USB, para ello necesitarás un conector hembra de 5,5mmx2,1mm.

![imagen](assets/piece/6.jpeg)
![imagen](assets/piece/7.jpeg)

3. Opcional: agregar un enchufe conectado.
Si desea encender/apagar su Antminer desde su teléfono inteligente y monitorear su consumo de energía, puede agregar un enchufe inteligente. Hemos probado el enchufe ANTELA en su versión de 16A compatible con la aplicación smartlife. Este enchufe inteligente permite consultar el consumo diario y mensual y se conecta directamente a su enrutador de Internet a través de WIFI.
![imagen](assets/piece/8.jpeg)

Lista de materiales y enlaces

* 2X adaptador de pieza 3D de 140 mm a 120 mm

* [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)

* [2X rejillas de ventilador de 140 mm](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
  
* [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)

* [Cable eléctrico de 2,5 mm2](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
* [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
* [Enchufe inteligente opcional ANTELA](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

# Attakai - modificación del software de un Antminer S9

## Configuración de un puente WIFI/Ethernet Vonet

Para conectar su ASIC a través de WIFI, necesitará un dispositivo llamado puente, que permite recibir la señal WIFI de su enrutador y transmitirla a otro dispositivo a través de Ethernet.

Hay muchos dispositivos que pueden hacer esto, recomendamos el VONETS WiFi Bridge/Repeteur por su practicidad.

Alimente el puente conectándolo a través de USB.

Desde su computadora, conéctese a la red WIFI VONETS_****** con la contraseña 12345678.

![imagen](assets/software/vonet1.png)

Identificación de administrador: admin admin

![imagen](assets/software/vonet2.png)

Seleccione "Wizard"

![imagen](assets/software/vonet3.png)

Seleccione la red WIFI a la que desea conectar su minero y haga clic en "Next".

ATENCIÓN: el puente Vonet solo funciona en 2,4 GHz. Hoy en día, los enrutadores generalmente ofrecen dos redes WIFI, una en 2,4 GHz y otra en 5 GHz.

![imagen](assets/software/vonet4.png)

Ingrese la contraseña de su red WIFI en "Source WIFI hotspot password".
Si no desea utilizar su puente Vonet para extender su red WIFI, marque la casilla "Disable Hotspot". De lo contrario, puede dejar esta casilla desmarcada.

Luego, puede hacer clic en "Apply".

Y finalmente, deberá hacer clic en "reboot" para reiniciar el puente. El puente se reiniciará en unos minutos.

El puente debería conectarse a su enrutador y aparecerá con el nombre de "[VONETS.COM](http://vonets.com/)".
Es posible que sea necesario desconectar y volver a conectar el puente si no se conecta después de unos minutos.

Una vez que el puente esté conectado, conecte el cable Ethernet del puente a su ASIC y luego conecte el ASIC a la corriente. Luego podrá acceder a la interfaz del ASIC de la misma manera que si estuviera conectado directamente a su enrutador a través de Ethernet.

## Restablecer un Antminer S9

Antes de instalar BraiinOS+, puede ser necesario restablecer su S9 a sus configuraciones de fábrica.
Esta método se puede aplicar entre 2 minutos y 10 minutos después de encender el minero.
2 minutos después de encender el minero, presione el botón "Reset" durante 5 segundos y luego suéltelo. El minero se restaurará a los ajustes de fábrica en 4 minutos y se reiniciará automáticamente (no es necesario apagarlo).

![imagen](assets/software/1.jpeg)

## Instalar BraiinsOS+ en un Antminer S9

El software original instalado por Antminer en sus máquinas de minería tiene funciones limitadas. Por eso, en esta guía vamos a instalar otro software llamado BraiinsOS+. Es un software de terceros desarrollado por el primer grupo de minería de Bitcoin que tiene más funciones y permite, por ejemplo, modificar la potencia de la máquina.

Hay varias formas de instalar Braiins OS+ en un ASIC. Puede consultar esta guía, así como la [documentación oficial de Braiins](https://academy.braiins.com/en/braiins-os/about/).

Aquí veremos cómo instalar fácilmente Braiins OS+ directamente en la memoria de su Antminer con el software BOS toolbox, reemplazando así el sistema operativo original, a través de los siguientes pasos detallados.

1. Encienda su Antminer y conéctelo a su caja de internet.
2. Descargue BOS toolbox para Windows / Linux.
3. Descomprima el archivo descargado y abra el archivo bos-toolbox.bat, elija el idioma y después de unos momentos verá esta ventana:

![imagen](assets/software/5.jpeg)

4. BOS toolbox le permitirá encontrar fácilmente la dirección IP de su Antminer e instalar BraiinsOS+. Si ya conoce la dirección IP de su máquina, puede pasar al paso 8. De lo contrario, vaya a la pestaña de escaneo.

![imagen](assets/software/6.jpeg)

5. Por lo general, en las redes domésticas, el rango de direcciones IP se encuentra entre 192.168.1.1 y 192.168.1.255, así que ingrese "192.168.1.0/24" en el campo de rango de IP. Si su red es diferente, cambie estas direcciones en consecuencia. Luego haga clic en "Start".

6. Tenga en cuenta que si el Antminer tiene una contraseña, la detección no funcionará. Si ese es el caso, lo más sencillo es realizar un reinicio.

7. Debería ver todos los Antminer en su red, aquí la dirección IP es 192.168.1.37.

![imagen](assets/software/7.jpeg)

8. Haga clic en "Back" y luego en la pestaña "install", ingrese la dirección IP encontrada anteriormente y haga clic en "Start".

> Si la instalación no funciona, puede ser necesario realizar un reinicio y volver a intentarlo (consulte la sección anterior).
9. Después de unos momentos, su Antminer se reiniciará y podrá acceder a la interfaz de Braiins OS+ en la dirección IP mencionada, aquí 192.168.1.37, que debe ingresar directamente en la barra de direcciones de su navegador, el nombre de usuario predeterminado es "root" y no hay contraseña predeterminada.

## Configurar BraiinsOS+

Deberá conectarse a su ASIC utilizando la dirección IP local de su dispositivo en su red a través de un navegador.

Puede encontrar la dirección IP de su máquina con la herramienta BOS toolbox o directamente en la página web de su enrutador.

Las credenciales predeterminadas son las mismas que las del sistema operativo original.

- nombre de usuario: root
- contraseña: (ninguna)

Luego será recibido por el panel de control de Brains OS+.

### Panel de control

![image](assets/software/14.jpeg)

En esta primera página, podrá observar el rendimiento de su máquina en tiempo real.

- Tres gráficos en tiempo real que muestran la temperatura, el hashrate y el estado general de su máquina.
- A la derecha, el hashrate real, la temperatura promedio de los chips, su eficiencia estimada en W/THs y el consumo de energía.
- Debajo, la velocidad de rotación de los ventiladores en porcentaje de la velocidad máxima y el número de rotaciones por minuto.

![image](assets/software/15.jpeg)

- Más abajo encontrará una vista detallada de cada hashboard. La temperatura promedio de la placa y los chips que la componen, el voltaje y la frecuencia.
- Detalles sobre los grupos de minería activos en Pools.
- El estado de la sintonización automática en Tuner Status.
- A la derecha, detalles sobre los datos transmitidos al grupo de minería.

### Configuración

![image](assets/software/16.jpeg)

### Sistema

![image](assets/software/17.jpeg)

### Acciones rápidas

![image](assets/software/18.jpeg)

# Attakai - Modificación de los ventiladores

## Reemplazar el ventilador de la fuente de alimentación

> ADVERTENCIA: Es esencial haber instalado previamente Braiins OS+ en su minero, u otro software que tenga la capacidad de reducir el rendimiento de su máquina. Esta medida es crucial, ya que para reducir el ruido, instalaremos ventiladores menos potentes, que podrán disipar menos calor.

![image](assets/hardware/cover.jpeg)

### Materiales necesarios

- 1 ventilador Noctua NF-A6x25 PWM
- Cable eléctrico de 2,5 mm2

> ADVERTENCIA: Antes de comenzar, asegúrese de haber desconectado su minero para evitar cualquier riesgo de electrocución.

![image](assets/hardware/1.jpeg)

Primero, retire las 6 tornillos en el lateral de la carcasa que la mantienen cerrada. Una vez retirados los tornillos, abre cuidadosamente la carcasa para quitar la protección de plástico que cubre los componentes.

![image](assets/hardware/2.jpeg)
![image](assets/hardware/3.jpeg)

Luego, es hora de quitar el ventilador original teniendo cuidado de no dañar los otros componentes. Para hacerlo, retire los tornillos que lo mantienen en su lugar y despegue suavemente el adhesivo blanco que rodea el conector. Es importante proceder con delicadeza para evitar dañar los cables o los conectores.

![image](assets/hardware/4.jpeg)

Una vez retirado el ventilador original, notarás que los conectores del nuevo ventilador Noctua no coinciden con los del ventilador original. De hecho, el nuevo ventilador tiene 3 cables, incluido un cable amarillo que permite controlar la velocidad. Sin embargo, este cable no se utilizará en este caso específico. Para conectar el nuevo ventilador, se recomienda utilizar un adaptador especial. Sin embargo, es importante tener en cuenta que este adaptador a veces puede ser difícil de encontrar.

![image](assets/hardware/5.jpeg)

Si no tienes este adaptador, aún puedes conectar el nuevo ventilador utilizando un empalme de cables. Para ello, deberás cortar los cables del ventilador antiguo y del nuevo ventilador.

![image](assets/hardware/6.jpeg)
![image](assets/hardware/7.jpeg)

En el nuevo ventilador, usa un cortador y corta cuidadosamente los contornos de la cubierta principal a 1 cm sin cortar las cubiertas de los cables debajo.

![image](assets/hardware/8.jpeg)

Luego, tirando hacia abajo de la cubierta principal, corta las cubiertas de los cables rojo y negro de la misma manera que antes. Y corta el cable amarillo al ras.

![image](assets/hardware/9.jpeg)

En el ventilador antiguo, es más delicado cortar la cubierta principal sin dañar las cubiertas de los cables rojo y negro. Para ello, hemos utilizado una aguja que hemos deslizado entre la cubierta principal y los cables rojo y negro.

![image](assets/hardware/10.jpeg)
![image](assets/hardware/11.jpeg)

Una vez que los cables rojo y negro estén libres, corta las cubiertas con cuidado para no dañar los cables eléctricos.

![image](assets/hardware/12.jpeg)

Luego, conecta los cables con un empalme, el cable negro con el negro y el cable rojo con el rojo. También puedes añadir cinta aislante.

![image](assets/hardware/13.jpeg)
![image](assets/hardware/14.jpeg)

Una vez realizada la conexión, es hora de instalar el nuevo ventilador Noctua con la rejilla y los tornillos antiguos, los nuevos tornillos que se encuentran en la caja se reutilizarán más adelante. Asegúrese de colocarlo en la orientación correcta. Notará una flecha en uno de los lados del ventilador, que indica la dirección del flujo de aire. Es importante colocar el ventilador de manera que esta flecha apunte hacia el interior del estuche. Luego, vuelva a conectar el ventilador.

![image](assets/hardware/15.jpeg)
![image](assets/hardware/16.jpeg)

> Opcional: Si tiene conocimientos de electricidad, puede agregar directamente a la salida de alimentación de 12V un conector hembra jack de 5,5 mm que permitirá alimentar directamente el puente Wi-Fi Vonet. Sin embargo, si no está seguro de sus habilidades eléctricas, es mejor utilizar el conector USB con un cargador de tipo smartphone para evitar cualquier riesgo de cortocircuito o daño eléctrico.

![image](assets/hardware/17.jpeg)

Una vez realizadas las conexiones, vuelva a colocar la cubierta de plástico sobre la carcasa de plástico y no dentro de ella.

![image](assets/hardware/18.jpeg)

Finalmente, vuelva a colocar la cubierta de la carcasa en su lugar y vuelva a atornillar los 6 tornillos en los lados para mantener todo en su lugar. ¡Y listo, su caja de alimentación ahora está equipada con un nuevo ventilador!

## Reemplazar los ventiladores principales

> ATENCIÓN: Es esencial haber instalado previamente Braiins OS+ en su minero, u otro software que tenga la capacidad de reducir el rendimiento de su máquina. Esta medida es crucial, ya que con el fin de reducir el ruido, instalaremos ventiladores menos potentes, que podrán disipar menos calor.

![image](assets/hardware/cover.jpeg)

### Materiales necesarios

- 2 adaptadores 3D de 140 mm a 120 mm
- 2 ventiladores Noctua NF-A14 iPPC-2000 PWM
- 2 rejillas de ventilador de 140 mm

> ATENCIÓN: En primer lugar, antes de comenzar, asegúrese de haber desconectado su minero para evitar cualquier riesgo de electrocución.

1. En primer lugar, desconecte los ventiladores y desenrósquelos.

![image](assets/hardware/19.jpeg)

2. Los conectores de los nuevos ventiladores Noctua no coinciden con los originales, ¡pero no se preocupe! Saque su cortador y corte cuidadosamente las pequeñas lengüetas de plástico para que los conectores se adapten perfectamente a su minero.

![image](assets/hardware/20.jpeg)
![image](assets/hardware/21.jpeg)

3. ¡Es hora de instalar las piezas 3D!
Fíjelas en ambos lados del minero utilizando los tornillos que retiraste de los ventiladores. Aprieta hasta que la cabeza del tornillo esté dentro de la pieza 3D y esta esté bien sujeta en su lugar. Ten cuidado de no apretar demasiado, ¡podrías deformar la pieza y uno de los tornillos podría tocar un condensador!

![imagen](assets/hardware/22.jpeg)

4. Ahora pasemos a los ventiladores.
Fíjalos en las piezas 3D utilizando los tornillos proporcionados en la caja. Ten en cuenta la dirección del flujo de aire, las flechas en los lados de los ventiladores te indicarán la dirección a seguir. Ve desde el lado del puerto Ethernet hacia el otro lado. Ver foto a continuación.

![imagen](assets/hardware/23.jpeg)
![imagen](assets/hardware/24.jpeg)
![imagen](assets/hardware/25.jpeg)

5. Último paso: conecta los ventiladores y fija las rejillas encima con los tornillos que no se utilizaron en la caja del ventilador de la fuente de alimentación. Solo tienes 4, pero 2 por rejilla en ángulos opuestos serán suficientes. Si es necesario, también puedes buscar otros tornillos similares en una tienda de bricolaje.

![imagen](assets/hardware/26.jpeg)
![imagen](assets/hardware/27.jpeg)

Mientras esperas para poder ofrecer una carcasa más atractiva a tu nuevo calentador, puedes sujetar la caja y la fuente de alimentación con abrazaderas de electricista.

![imagen](assets/hardware/28.jpeg)

Y para el toque final, conecta el puente Vonet al puerto Ethernet a su fuente de alimentación.

![imagen](assets/hardware/29.jpeg)

¡Y listo, felicidades! Acabas de reemplazar toda la parte mecánica de tu minero. Ahora deberías escuchar mucho menos ruido.

# Attakai - Configuración

## Unirse a un grupo de minería

Se puede imaginar un grupo de minería como una cooperativa agrícola. Los agricultores unen sus producciones para reducir la variabilidad de la oferta y la demanda, y así obtener ingresos más estables para su explotación. Un grupo de minería funciona de la misma manera, y la materia prima que se comparte son los hash. De hecho, el descubrimiento de un solo hash válido permite la creación de un bloque y, por lo tanto, ganar la coinbase o la recompensa actual de 6.25 BTC más las tarifas de transacción incluidas en el bloque. 

Si minas solo, solo serás recompensado cuando encuentres un bloque. Al competir contra todos los demás mineros del planeta, tendrías muy pocas posibilidades de ganar esta gran lotería y aún así tendrías que pagar las tarifas asociadas al uso de tu minero sin ninguna garantía de éxito. Los grupos de minería abordan este problema al compartir la potencia de cálculo de varios (miles) de mineros y compartir la recompensa de acuerdo con el porcentaje de participación en el hashrate del grupo cuando se encuentra un bloque. Para visualizar tus posibilidades de minar un bloque por tu cuenta, puedes usar esta herramienta. Al ingresar la información de un Antminer S9, se puede ver que las posibilidades de encontrar un hash que permita la creación de un bloque son de 1/24,777,849 por bloque o de 1/172,068 por día. En promedio (con un hashrate y una dificultad constantes), tomaría 471 años encontrar un bloque.

Sin embargo, como en Bitcoin todo es una cuestión de probabilidad, a veces los "mineros en solitario" son recompensados por asumir este riesgo: Un minero de Bitcoin en solitario resuelve un bloque con una tasa de hash de solo 10 TH/s, venciendo probabilidades extremadamente improbables - Decrypt

Si te gusta jugar, puedes intentarlo, pero nuestra guía no se centrará en esa dirección. En cambio, nos enfocaremos en el grupo de minería que mejor se adapte a nuestras necesidades para crear un sistema de calefacción.
Las consideraciones a tener en cuenta al elegir un grupo de minería son el funcionamiento de las recompensas del grupo, que pueden ser diferentes, así como el monto mínimo antes de poder retirar las recompensas a una dirección. Por ejemplo, Braiins, que ofrece el software del que estamos hablando aquí, también ofrece un grupo de minería. 

Este grupo tiene un sistema de recompensa llamado "Score" que incentiva a los mineros a minar durante largos períodos de tiempo. La participación incluye un factor de tiempo de actividad que se expresa con una "tasa de hash de puntuación". En nuestro caso, donde queremos un sistema de calefacción que se pueda encender solo durante unos minutos, este no es el sistema de recompensa ideal. Preferimos un sistema de recompensa que nos dé una recompensa igual por cada participación. Además, el monto mínimo de retiro para Braiins Pool es de 100,000 sats y On-Chain. Por lo tanto, perdemos algunos sats en tarifas de transacción y parte de nuestra recompensa puede quedar bloqueada si no minamos lo suficiente durante el invierno.

El modelo de recompensa que nos interesa es el PPS, que significa "pago por acción". Esto significa que el minero recibirá una recompensa por cada acción válida. También existe una variante de este sistema, el FPPS (Pago Completo por Acción), que divide no solo la recompensa de la coinbase, sino también las tarifas de transacción incluidas en el bloque. Los grupos de minería que recomendamos para conectar su minería/calefacción son Linecoin Pool (FPPS) y Nicehash (PPS).

- Nicehash: La ventaja de Nicehash es que el retiro se puede hacer utilizando Lightning con tarifas mínimas. Además, el monto mínimo de retiro es de 2000 sats. La desventaja es que Nicehash utiliza su tasa de hash para la cadena de bloques más rentable, sin dar realmente control al usuario y, por lo tanto, no siempre participa en la tasa de hash de Bitcoin.

- Lincoin: La ventaja de Linecoin es la cantidad de características que ofrece, como un panel de control detallado, la posibilidad de hacer retiros con un Paynym (BIP 47) para una mejor protección de la privacidad, y la integración de un bot de Telegram y automatizaciones directamente configurables en la aplicación móvil. Este grupo solo mina bloques de Bitcoin, pero el monto mínimo para retirar sigue siendo alto, 100,000 sats. Analizaremos más detalladamente la interfaz de uno de estos grupos en un próximo artículo.

Para configurar un grupo en Braiins 0S+, deberá crear una cuenta en uno de los grupos de su elección. Aquí tomaremos el ejemplo de Lincoin:

![imagen](assets/software/19.jpeg)

Una vez que haya creado su cuenta, haga clic en "Connect To Pool".

Luego copie la dirección Stratum y su nombre de usuario:

![imagen](assets/software/20.jpeg)

Ahora puede volver a la interfaz de Braiins OS+ para ingresar estas credenciales. Para la contraseña, puede dejar el campo vacío.

![imagen](assets/software/21.jpeg)

## Optimizar el rendimiento de su Antminer S9

El overclocking y el autoajuste consisten en ajustar las frecuencias en las tarjetas de hash para mejorar el rendimiento del ASIC. La diferencia entre ambos radica en la complejidad de estos ajustes de frecuencia.

El overclocking es un ajuste simple que consiste en aumentar la frecuencia en las tarjetas de hash para aumentar la tasa de hash de la máquina. El underclocking, por otro lado, consiste en disminuir la frecuencia de reloj de un circuito integrado por debajo de su frecuencia nominal. Al reducir la frecuencia de reloj de un ASIC mediante el underclocking, también se reduce el calor generado por el hardware. Esto permite disminuir la velocidad de los ventiladores necesarios para enfriar el ASIC, ya que no tienen que trabajar tan duro para mantener una temperatura adecuada. Al reducir la velocidad de los ventiladores, también se reduce el ruido generado por el ASIC. Esto puede ser especialmente útil para los usuarios que utilizan ASIC en casa y buscan minimizar las molestias sonoras causadas por el equipo de minería.

Braiins OS+ admite el overclocking, el underclocking de los ASIC y el autoajuste. Permite a los usuarios ajustar la frecuencia de reloj de su hardware de manera flexible para maximizar el rendimiento o ahorrar energía según sus preferencias.

### Optimizar el rendimiento de su Antminer S9 con autoajuste

Antes de 2018, los mineros tenían dos formas de obtener una ventaja en su actividad: encontrar electricidad a un costo razonable y comprar hardware más eficiente. Sin embargo, en 2018, se descubrió un nuevo avance en el campo del software y firmware minero, llamado AsicBoost. Esta técnica permite a los mineros reducir sus costos en aproximadamente un 13% al modificar el firmware que se ejecuta en sus dispositivos.

Hoy en día, hay un nuevo avance en el sector de software y firmware minero llamado autorregulación (o autotuning) que ofrece una ventaja aún mayor que AsicBoost. Los ASIC están compuestos por numerosos chips informáticos pequeños que realizan el hashing. Estos chips están hechos de silicio, el mismo elemento ampliamente utilizado en semiconductores y otros componentes microelectrónicos. La comprensión clave aquí es que no todos los chips de silicio son idénticos, cada uno puede variar ligeramente en sus propiedades eléctricas. Los fabricantes de hardware lo saben y publican las especificaciones de rendimiento de sus máquinas mineras en función del límite inferior de sus tolerancias. En otras palabras, los fabricantes conocen la frecuencia que funciona mejor para los chips promedio y utilizan esta frecuencia de manera uniforme para todos los chips de la máquina.

Esto pone un límite superior a la tasa de hashing que una máquina puede tener. La autorregulación es un proceso en el que los algoritmos evalúan las frecuencias óptimas para el hashing chip por chip, en lugar de tratar toda la máquina como una sola unidad. Esto significa que un chip de mejor calidad que puede realizar más hash por segundo obtendrá una frecuencia más alta, y un chip de menor calidad que puede realizar relativamente menos obtendrá una frecuencia más baja. La autorregulación por chip es esencialmente una forma de optimizar el rendimiento de un ASIC a través del software y firmware que se ejecutan en él.

El resultado final es una tasa de hashing más alta por vatio de electricidad, lo que significa márgenes de beneficio más grandes para los mineros. La razón por la cual las máquinas no se distribuyen con este tipo de software es que la variabilidad por máquina no es deseable, ya que los clientes quieren saber exactamente lo que están obteniendo y, por lo tanto, es una mala idea para los fabricantes vender un producto que no tiene un rendimiento constante y predecible de una máquina a otra. Además, la autorregulación por chip requiere considerables recursos de desarrollo, ya que es compleja de implementar. Los fabricantes ya gastan muchos recursos en desarrollar sus propios firmwares. Existen soluciones de software que permiten implementar la autorregulación, como Braiins OS+. Además de mejorar el rendimiento del ASIC hasta en un 20%.

## Controlar un Antminer S9 desde un smartphone

### Crear accesos directos en iOS

![Controlar un Antminer S9 con un smartphone](https://www.youtube.com/watch?v=OsKmdB2iw88&t=60s)

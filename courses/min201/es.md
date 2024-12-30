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

<partId>a99dc130-3650-563f-8d42-a0b5160af0ab</partId>

## ¡Bienvenido!

<chapterId>7ad1abeb-a190-5c85-8bff-44df71331e4d</chapterId>

Bienvenido a MINING 201: una introducción a la minería. Ajelex, Jim y Rogzy están encantados de acompañarte en tus primeros pasos concretos en esta nueva industria. ¡Esperamos que disfrutes del curso y te unas a la aventura de la minería en casa!

### Resumen del curso

En este curso, la primera sección estará dedicada a la teoría de la minería con Ajelex. Discutiremos en profundidad los diversos temas relacionados con la minería, lo que nos permitirá comprender mejor esta industria y los desafíos económicos y geopolíticos asociados.

En la segunda sección, nos embarcaremos en un fascinante caso práctico, aprendiendo a convertir un minero S9 de segunda mano en una calefacción auxiliar para el hogar. Gracias a guías escritas y videos, se explicarán minuciosamente todos los pasos necesarios, garantizando así tu éxito en este proyecto innovador.

Este viaje de aprendizaje te mostrará que la industria minera es más compleja de lo que parece, ofreciendo una perspectiva equilibrada sobre el debate ecológico asociado. Se brindará ayuda continua a través de un grupo de Telegram dedicado para los estudiantes, y todos los componentes necesarios estarán fácilmente disponibles en nuestra plataforma de comercio electrónico.

### Plan de estudios:

Sección Teórica:

- Explicación de la minería.
- La industria minera.
- Los matices de la industria minera.
- La minería en el protocolo de Bitcoin.
- Precio de bitcoin y hashrate, ¿hay una correlación?\* Soberanía y regulación
- Entrevista a un profesional de la industria minera

Sección Práctica: Attakai

- Introducción a Attakai.
- Guía de compra.
- Modificación del software de un Antminer S9.
- Reemplazo de los ventiladores para reducir el ruido.
- Configuración de un pool.
- Configuración de un Antminer S9 con Braiins OS+.

¿Listos para comenzar esta emocionante aventura? ¡Sumergámonos juntos en el fascinante mundo de la minería doméstica!

# Conoce todo sobre la minería

<partId>aa99ef2c-da29-5317-a533-2ffa4f66f674</partId>

## Explicación de la minería

<chapterId>36a82de7-87ee-5e7a-b69e-48fc30030447</chapterId>

### La Minería Explicada: La Analogía del Rompecabezas

Para explicar de manera simplificada el concepto de la minería, se puede utilizar una analogía relevante: la del rompecabezas. Al igual que un rompecabezas, la minería es una tarea compleja de realizar, pero fácil de verificar una vez completada. En el contexto de la minería de Bitcoin, los mineros se esfuerzan por resolver rápidamente un rompecabezas digital. El primer minero en resolver el rompecabezas presenta su solución a toda la red, que luego puede verificar fácilmente su validez. Esta verificación exitosa permite al minero validar un nuevo bloque y agregarlo a la cadena de bloques de Bitcoin. Como reconocimiento a su trabajo, que implica costos significativos, el minero es recompensado con una cierta cantidad de bitcoins. Esta recompensa es un incentivo financiero para que los mineros continúen su trabajo de validación de transacciones y seguridad de la red Bitcoin.

![imagen](assets/en/01.webp)

Inicialmente en la red Bitcoin, la recompensa otorgada era de 50 bitcoins cada diez minutos, al mismo tiempo que se descubría un bloque cada diez minutos en promedio por los mineros. Esta recompensa se divide a la mitad cada 210,000 bloques, aproximadamente cada cuatro años. Esta remuneración sirve como un poderoso incentivo para alentar a los mineros a participar en el proceso de minería a pesar de su costo energético. Sin la recompensa, la minería, que es costosa en electricidad, sería abandonada, comprometiendo así la seguridad y estabilidad de toda la red Bitcoin.

La recompensa actual de minería es doble. Por un lado, incluye la creación de nuevos bitcoins, que ha pasado de 50 bitcoins cada diez minutos en sus inicios a 6,25 bitcoins hoy en día (2023). Por otro lado, incluye las tarifas de transacción, o tarifas de minería, de las transacciones que el minero elige incluir en su bloque. Cuando se realiza una transacción de bitcoin, se pagan tarifas de transacción. Estas tarifas funcionan como una especie de subasta donde los usuarios indican cuánto están dispuestos a pagar para que su transacción se incluya en el siguiente bloque. Para maximizar su recompensa, los mineros, actuando en su propio interés, seleccionan las transacciones más rentables para incluirlas en su bloque, teniendo en cuenta el espacio limitado disponible. Así, la recompensa de minería se compone tanto de la generación de nuevos bitcoins como de las tarifas de transacción, garantizando un incentivo continuo para los mineros y asegurando la sostenibilidad y seguridad de la red Bitcoin.

### Mineros y sus herramientas: Minería

El proceso de minería consiste en encontrar un hash válido aceptable por la red Bitcoin. Este hash, una vez calculado y encontrado, es irreversible, al igual que las papas convertidas en puré. Verifica una función determinada sin posibilidad de retroceder. Los mineros, compitiendo entre sí, utilizan máquinas para calcular estos hashes. Aunque teóricamente es posible encontrar este hash manualmente, la complejidad de la operación hace que esta opción sea inviable. Por lo tanto, se utilizan computadoras capaces de realizar estos cálculos rápidamente, aunque consumen una cantidad significativa de electricidad.

Al principio, la era de la CPU dominaba, donde los mineros utilizaban sus computadoras personales para la minería de Bitcoin. El descubrimiento de las ventajas de las GPU (tarjetas gráficas) para esta tarea marcó un punto de inflexión, aumentando sustancialmente la tasa de hash y reduciendo el consumo de energía. El progreso no se detuvo allí, con la posterior introducción de los FPGA (field-programmable gate array / matriz de puertas programables en campo). Los FPGA sirvieron como plataforma para el desarrollo de los ASIC (application-specific integrated circuit / circuito integrado específico de aplicación).

![image](assets/en/02.webp)

Los ASIC son chips, similares a los chips de una CPU, sin embargo, están diseñados para realizar un solo tipo de cálculo específico de la manera más eficiente posible. En otras palabras, una CPU es capaz de realizar una multitud de tipos de cálculos diferentes sin estar especialmente optimizada para un tipo de cálculo u otro, mientras que un ASIC será capaz de realizar un solo tipo de cálculo, pero de manera muy eficiente. En este caso, los ASIC de Bitcoin están diseñados para calcular el algoritmo SHA256.

En la actualidad, los mineros utilizan exclusivamente ASICs dedicadas a esta operación, optimizadas para probar el mayor número posible de combinaciones con el menor consumo de energía y la mayor rapidez posible. Estas computadoras, incapaces de realizar tareas distintas a la minería de Bitcoin, son un testimonio tangible de la continua evolución y especialización de la industria minera de Bitcoin. Esta evolución constante refleja la dinámica intrínseca de Bitcoin, donde un ajuste de la dificultad garantiza la producción de un bloque cada diez minutos a pesar del aumento exponencial de la capacidad de minería.

Para ilustrar la intensidad de este proceso, consideremos un minero típico capaz de realizar 14 TeraHash por segundo, es decir, 14,000 billones de intentos cada segundo para encontrar el hash correcto. A escala de la red de Bitcoin, actualmente se alcanzan aproximadamente 300 HexaHash por segundo, lo que destaca la potencia colectiva movilizada en la minería de Bitcoin.

### Ajuste de la dificultad:

El ajuste de la dificultad es un mecanismo crucial en el funcionamiento de la red de Bitcoin, garantizando que los bloques se minen en promedio cada 10 minutos. Esta duración es un promedio, ya que el proceso de minería es en realidad un juego de probabilidades, similar a lanzar dados con la esperanza de obtener un número menor al número definido por la dificultad. Cada 2016 bloques, la red ajusta la dificultad de minería en función del tiempo promedio necesario para minar los bloques anteriores. Si el tiempo promedio es superior a 10 minutos, la dificultad se reduce, y viceversa si el tiempo promedio es inferior, la dificultad se incrementa. Este mecanismo de ajuste asegura que el tiempo de minería de los nuevos bloques se mantenga constante a lo largo del tiempo, independientemente del número de mineros o de la potencia de cálculo global de la red. Es por esta razón que la Blockchain de Bitcoin también se llama Timechain.

![image](assets/en/03.webp)

- Ejemplo de China:
  El caso de China ilustra perfectamente este mecanismo de ajuste de dificultad. Siendo rica en energía abundante y barata, era el principal centro mundial de minería de Bitcoin. En 2021, el país prohibió abruptamente la minería de Bitcoin en su territorio, lo que provocó una caída masiva de la tasa de hash global de la red Bitcoin, del orden del 50%. Esta rápida disminución de la potencia de minería podría haber perturbado gravemente la red Bitcoin, aumentando el tiempo promedio de minería de bloques. Sin embargo, el mecanismo de ajuste de dificultad intervino, reduciendo la dificultad de minería para garantizar que la frecuencia de minería de bloques se mantenga en promedio en 10 minutos. Este caso demuestra la eficacia y la resiliencia del mecanismo de ajuste de dificultad de Bitcoin, que asegura la estabilidad y previsibilidad de la red, incluso ante cambios bruscos e importantes en el panorama de la minería mundial.

### Evolución de las Máquinas de Minería de Bitcoin

En cuanto a la evolución de las máquinas de minería de Bitcoin, es importante destacar que el contexto se orienta más hacia un modelo de negocio tradicional. Los mineros obtienen sus ingresos validando bloques, una tarea con una probabilidad de éxito relativamente baja. El modelo de máquina actualmente en uso, el Antminer S9, aunque es un modelo más antiguo lanzado alrededor de 2016, sigue circulando en el mercado de segunda mano y se negocia entre 100€ y 200€. Sin embargo, el precio de las máquinas de minería varía según el valor de Bitcoin, y un modelo más reciente, el Antminer S19, actualmente se estima en alrededor de 3000€.

Ante la constante evolución tecnológica en el campo de la minería, los profesionales deben posicionarse estratégicamente. La industria minera está sujeta a continuas innovaciones, como lo demuestra el reciente lanzamiento de la versión J del S19 y la próxima versión anticipada del S19 XP, que ofrecen capacidades de minería significativamente superiores. Además, las mejoras no se limitan solo al rendimiento bruto de las máquinas. Por ejemplo, el nuevo modelo S19 XP utiliza un sistema de enfriamiento líquido, una modificación técnica que permite una mejora significativa en la eficiencia energética. Aunque la innovación sigue siendo constante, es probable que las futuras ganancias de eficiencia sean menores en comparación con las observadas hasta ahora, debido a la alcanzada de un cierto umbral de innovación tecnológica.

![image](assets/en/04.webp)

En conclusión, la industria de la minería de Bitcoin continúa adaptándose y desarrollándose, los actores del campo deben anticipar ganancias de eficiencia más limitadas en el futuro y ajustar sus estrategias en consecuencia. Los avances tecnológicos futuros, aunque aún presentes, probablemente se producirán a una escala más reducida, reflejando una madurez creciente del sector.

## La industria de la minería

<chapterId>0896dfc1-c97e-5bec-9bf1-8c20b3388a2c</chapterId>

### Los Pools de Minería

En la actualidad, la minería de Bitcoin ha evolucionado para convertirse en una industria seria y sustancial, con muchos actores ahora públicos y un número creciente de mineros significativos. Esta evolución ha hecho que la minería sea casi inaccesible para los pequeños actores debido al alto costo asociado con la adquisición de nuevas máquinas de minería. Por lo tanto, surge la cuestión de la distribución del hashrate entre diversos actores del mercado. La situación es compleja, ya que es esencial examinar tanto la distribución del hashrate entre diferentes empresas como entre diferentes pools de minería.

![imagen](assets/en/05.webp)

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

![image](assets/en/06.webp)

Para combatir esta centralización, se abordan diferentes estrategias:

- Home Mining: La idea del Home Mining se basa en la descentralización de la actividad minera. Alentar a las personas a participar en la actividad minera desde sus hogares, distribuyendo así el hashrate de manera más amplia.
- Stratum V2: El protocolo Stratum V2 ofrece otro enfoque. A diferencia de su predecesor, Stratum V2 permite a los mineros elegir las transacciones que incluirán en los bloques que minan. Esta capacidad refuerza la resistencia a la censura y reduce la capacidad de las grandes pools de minería para dominar la red. Al dar más poder a los mineros individuales, el protocolo Stratum V2 puede desempeñar un papel crucial en la lucha contra la centralización del hashrate.
  Open-Sourcing de Software de Minería
- Open-Sourcing de software de minería: Esta es otra estrategia potencialmente efectiva. Al hacer que el software de minería sea accesible para todos, los pequeños mineros tendrían las mismas oportunidades que las grandes empresas mineras para participar y contribuir a la red blockchain. Este enfoque fomentaría una distribución más amplia del hashrate, contribuyendo así a la descentralización de la red.
- Diversificación de actores y geografía: Fomentar la participación de diversos actores de diferentes regiones geográficas en la minería de criptomonedas también puede ser efectivo. Al diversificar geográficamente el hashrate, se vuelve más difícil para un solo actor o país ejercer un control o influencia desproporcionada sobre la red. Este enfoque puede contribuir a proteger la red contra posibles ataques y fortalecer su descentralización.

La conclusión general es que la descentralización es crucial para la seguridad y resiliencia de la red Bitcoin. Si bien la centralización puede ofrecer ventajas en términos de eficiencia, expone a la red a riesgos significativos, como la censura y los ataques del 51%. Iniciativas como Takai y la adopción de nuevos protocolos como Stratum V2 son pasos importantes hacia la descentralización y protección de la red Bitcoin contra estas amenazas.

## Las sutilezas de la industria minera

<chapterId>7b9ee427-316a-54e3-a2d4-4ea97839a31b</chapterId>

### El principio de Attakai

En el contexto actual, la práctica de la minería de Bitcoin en S9 puede parecer compleja, pero un análisis más profundo abre el camino a alternativas innovadoras. El principio de Attakai se basa en una reflexión sobre el uso de instalaciones mineras en diversos tipos de edificios, como escuelas u hospitales. La idea principal es colocar algunas máquinas mineras en diferentes lugares, lo que permite reutilizar el calor emitido por estas máquinas para calentar los establecimientos. Al optar por modelos más eficientes como el S19, sería posible distribuir la actividad minera, favoreciendo así un mejor rendimiento general y contribuyendo de manera útil a la sociedad. Esta iniciativa tiene como objetivo competir con las grandes instalaciones mineras centralizadas utilizando el calor generado por las máquinas mineras de manera productiva y eficiente.

La iniciativa Attakai surge de una experimentación personal de minería en el hogar realizada por dos amigos que deseaban participar activamente en la red de Bitcoin. Se encontraron con obstáculos importantes, como el alto nivel de ruido de los equipos de minería, diseñados para uso industrial y no doméstico. Para solucionar este problema, se realizaron modificaciones de hardware a las máquinas mineras. Se reemplazaron los equipos originales por ventiladores más eficientes y silenciosos, lo que hizo que la minería en el hogar fuera más accesible y menos molesta. Además, la adición de un adaptador Wi-Fi eliminó la necesidad de una conexión Ethernet por cable, simplificando aún más el proceso de minería en el hogar. En invierno, estos mineros modificados se utilizaron como fuente de calefacción, convirtiendo una molestia en un beneficio.

Al exponer su proyecto a la comunidad de Bitcoin y ante el interés generado, los inventores de Attakai decidieron publicar guías detalladas en la plataforma Découvre Bitcoin, permitiendo que cualquiera pueda reproducir su experiencia de minería en el hogar. Ahora están considerando ampliar este concepto más allá del ámbito doméstico. El objetivo es demostrar cómo un minero modificado puede convertirse en una calefacción adicional silenciosa utilizada durante el invierno, ofreciendo una transición suave a una segunda parte de formación dedicada a la implementación práctica de estas modificaciones, ilustrada con videos explicativos. Sin embargo, la pregunta sigue siendo si esta iniciativa puede expandirse a una escala más grande, ofreciendo así una alternativa realista y sostenible a las estructuras de minería centralizadas actuales.

![image](assets/en/07.webp)

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

![image](assets/en/08.webp)

La especulación rodea el uso futuro del espacio de bloques, pero generalmente se acepta que es un recurso escaso que debe utilizarse de manera prudente. Aunque existe el deseo de llenarlo, es esencial preservarlo para garantizar la viabilidad a largo plazo de la red de Bitcoin, anticipando un aumento futuro en la demanda de espacio en los bloques. Como en cualquier mercado libre, la oferta y la demanda regularán el uso del espacio de bloques. Con una oferta limitada, las partes interesadas deberán tomar decisiones informadas sobre el uso de este valioso espacio para garantizar la eficiencia y la seguridad a largo plazo de la red de Bitcoin.

## La minería en el protocolo bitcoin

<chapterId>879a66b0-c20a-56b5-aad0-8a21be61e338</chapterId>

![¿Quién tiene el poder? Bitcoin, energía y fabricantes](https://www.youtube.com/watch?v=4wywK6BfDw8)

El papel de los mineros en la red Bitcoin ha sido un tema de debate intenso durante la guerra de los bloques. Aunque son esenciales para la seguridad y la funcionalidad de la red, los mineros no necesariamente poseen el poder último en el ecosistema Bitcoin. El equilibrio entre los mineros, los nodos y los usuarios finales garantiza la integridad y la distribución de la red.

### La guerra de los bloques

Durante la guerra de los bloques, muchos mineros se opusieron a ciertas evoluciones de la red, destacando la tensión entre los diferentes actores del ecosistema. La cuestión sigue siendo cómo equilibrar el poder entre los mineros, los nodos y los usuarios para asegurar la seguridad a largo plazo de Bitcoin.

![image](assets/en/09.webp)

El dilema de la seguridad de Bitcoin se basa en un equilibrio delicado. Aunque los mineros juegan un papel crucial en la validación y creación de bloques, los nodos mantienen la integridad al verificar y validar las transacciones y los bloques. Un bloque incorrecto o fraudulento será rechazado por los nodos, censurando así al minero y preservando la seguridad de la red. El poder también es detentado por los nodos y los usuarios de la red Bitcoin. Los nodos tienen el poder de verificación y validación, mientras que los usuarios tienen el poder de elegir qué cadena de bloques utilizar. Esta distribución de poder asegura la distribución y la integridad de la red Bitcoin.

La guerra de los bloques reveló la incertidumbre y la tensión inherentes a la gestión de la red Bitcoin. Aunque Bitcoin Core es actualmente la cadena dominante, el debate sobre la gobernanza y la gestión de la red persiste.

En última instancia, la responsabilidad es compartida entre todos los actores de la red Bitcoin. Una disminución en el número de usuarios, nodos o mineros podría debilitar la red, aumentando el riesgo de centralización y vulnerabilidad a ataques. Cada actor contribuye a la robustez y seguridad de la red, reforzando la importancia de mantener un equilibrio de poder y responsabilidad.

### El poder de los mineros

La elegante teoría del juego de Satoshi Nakamoto ha establecido una situación donde cada actor de la red Bitcoin está incentivado a actuar correctamente para proteger tanto sus propios intereses como los de los demás participantes. Esto crea un equilibrio donde el mal comportamiento puede ser reprendido, reforzando así la seguridad y la estabilidad del sistema completo. A pesar de este equilibrio, los estados siguen siendo una amenaza potencial. Como se indicó en la presentación en Surfing Bitcoin 2022, los estados pueden intentar atacar la industria de la minería, exponiendo la red Bitcoin a riesgos de centralización y ataque. Escenarios hipotéticos como un ataque militar dirigido a las instalaciones de producción de hardware de minería subrayan la importancia de la diversificación geográfica e industrial para la resiliencia de la red Bitcoin.

![image](assets/en/10.webp)

La centralización de la producción de hardware de minería en China representa otro riesgo. Una negativa a exportar máquinas de minería o una acumulación de hashrate para un potencial ataque del 51% por parte de China subrayan la necesidad de una producción diversificada de hardware de minería. Ante estos riesgos, la comunidad Bitcoin está explorando activamente soluciones. Empresas como Intel están considerando producir equipos de minería en los Estados Unidos, contribuyendo a la distribución de la producción. Otras iniciativas, como la de Block con su Mining Development Kit (MDK) de código abierto, buscan disminuir el monopolio en el diseño y la producción de hardware de minería, permitiendo una distribución más amplia del hashrate. En el corazón de estas discusiones se encuentra la misión fundamental de Bitcoin: ser una red de intercambio de valor resistente a la censura. La comunidad Bitcoin se esfuerza constantemente por fortalecer la distribución, la resistencia a la censura y la anti-fragilidad de la red, rechazando propuestas como el cambio a proof of stake, que no se alinean con estos principios fundamentales.

### El vínculo físico del proof of work vs el proof of stake

El Proof of Work (PoW) es esencial porque representa el vínculo físico entre el mundo real y Bitcoin. Aunque los bitcoins son intangibles, su producción requiere energía tangible, estableciendo así un enlace directo con el mundo físico y real. Esta conexión asegura que la producción y validación de bitcoins y bloques tengan un costo energético real, anclando así la red Bitcoin en la realidad física y previniendo su dominación completa por entidades poderosas. El PoW actúa como un baluarte contra la centralización, asegurando que la participación en la red y la validación de transacciones requieran una inversión en recursos tangibles. Esto impide la monopolización de la red por entidades que podrían de otro modo tomar control sin ninguna barrera de entrada significativa, asegurando así una distribución más equitativa del poder y la influencia dentro de la red Bitcoin.

![image](assets/en/11.webp)

### Las Limitaciones del Proof of Stake

Por otro lado, el Proof of Stake (PoS), aunque permite la participación a pequeña escala, no garantiza una protección equivalente contra la centralización. En una red PoS, aquellos que ya poseen una gran cantidad de la moneda tienen un poder desproporcionado, reflejando las desigualdades de poder existentes en la sociedad en general. Esta dinámica podría potencialmente perpetuar la centralización y la concentración del poder en manos de unos pocos, en contra de los objetivos fundamentales de distribución de la red Bitcoin. El argumento de que todos pueden participar en el PoS, incluso a pequeña escala, uniéndose a pools, no es necesariamente sólido. En una red PoW, incluso un pequeño contribuyente, con equipo modesto, puede participar activamente y contribuir a la seguridad y distribución de la red.

### Resumen

Para resumir, los mineros fortalecen la red Bitcoin contra la censura utilizando electricidad para calcular la prueba de trabajo de Bitcoin, y son recompensados con nuevos bitcoins y las tarifas de transacción. Con la profesionalización de la industria, emergen diferentes actores, desempeñando varios roles, desde la creación de chips hasta la gestión de granjas de minería. Además, las finanzas también intervienen, ejerciendo control, decidiendo quién sobrevive durante las diferentes fases del mercado. La problemática de la centralización persiste, con las entidades más ricas dominando potencialmente el mercado. Sin embargo, se están desarrollando alternativas a nivel de hardware y software. Corresponde a cada individuo actuar y contribuir a la distribución de la red. Bitcoin representa una oportunidad sin precedentes no solo en términos de libertad, sino también de independencia energética. A pesar de las controversias sobre su consumo de electricidad, Bitcoin ofrece un incentivo económico para una transición hacia un uso más racional y abundante de la energía, materializando lo que antes era un ideal ecológico.

## Precio del bitcoin y hashrate, ¿una correlación?

<chapterId>e6676214-007c-5181-968e-c27536231bd6</chapterId>

![¿Cómo obtener un bitcoin blanco y puro?](https://youtu.be/A5MTtn4mm44?si=D1Yi0dVwkyafeHv-)

### Hashrate, precio y rentabilidad

El actual tasa de hash, aunque el precio del Bitcoin esté en 30,000$ comparado con su pico anterior de 69,000$, subraya el vínculo tangible entre la minería y el mundo real. Los períodos de aumento de precios (mercado alcista) generan una alta demanda de minería de Bitcoin y un incremento en los pedidos de máquinas a fabricantes como Avalon y Bitmain. Sin embargo, la producción y entrega no son instantáneas, creando un desajuste entre una demanda creciente y una disponibilidad posterior. Esto puede llevar a la entrega de máquinas ordenadas durante un mercado alcista en un mercado en declive, destacando una asimetría notable entre un precio bajo y una tasa de hash alta.

Esta situación también ilustra la resiliencia del Bitcoin, a menudo evaluada en función de su precio. No obstante, un análisis más profundo de la salud del Bitcoin requiere la revisión de su tasa de hash, que mide los cálculos por segundo en la red de Bitcoin. Mientras que el precio del Bitcoin fluctúa, su costo, vinculado a la electricidad necesaria para operar las máquinas de minería, sigue siendo esencial para entender la dinámica del mercado. Al enfocarse en el costo en lugar del precio, se obtiene una perspectiva más coherente sobre la estabilidad y la viabilidad a largo plazo del Bitcoin. En general, el costo del Bitcoin es proporcional a su precio, ofreciendo una mejor comprensión de las fluctuaciones de precio y las perspectivas futuras.

![image](assets/en/12.webp)

### Tasa de Hash y Recompensa

La minería establece un precio mínimo para el Bitcoin, por debajo del cual los mineros venderían a pérdida. El costo de la minería influye considerablemente en el precio, como se ilustró con la prohibición de la minería en China, donde la tasa de hash y el precio cayeron significativamente, pero se recuperaron rápidamente. Centrarse únicamente en el precio puede ser engañoso. El estudio del costo, a través de calculadoras de rentabilidad, ofrece una perspectiva más equilibrada. Sin embargo, el mercado puede comportarse de manera irracional, y los mineros pueden verse obligados a vender a pérdida, potencialmente bajando el precio por debajo del costo de minería. Para evaluar la salud del Bitcoin y su descentralización, se podría desarrollar una ecuación que integre diversos factores, como el número de nodos y el precio. Este enfoque podría proporcionar un análisis más matizado del Bitcoin en comparación con las discusiones basadas únicamente en el precio.

### Minar para el beneficio o para la red?

La pregunta es profunda y abarca varias dimensiones de la minería de Bitcoin. El equilibrio entre la búsqueda de beneficio y la contribución a la seguridad y distribución de la red de Bitcoin es un dilema constante para los mineros. El debate continúa en la comunidad de Bitcoin, con argumentos sólidos de ambos lados.

- Minar para el beneficio:

* A favor: Los mineros están naturalmente atraídos por el potencial de ganancia que ofrece la minería de Bitcoin. La inversión en equipos de minería costosos puede ser rentabilizada a través de las recompensas de minería y las tarifas de transacción, especialmente cuando el precio del Bitcoin es alto.
* En contra: La búsqueda de ganancias puede llevar a la centralización del poder de hash si solo unas pocas grandes empresas pueden permitirse invertir en equipos de minería de alta gama. Además, el consumo de energía de la minería para obtener ganancias puede tener un impacto ambiental significativo.

- Minar para la red:

* A favor: Minar para contribuir a la seguridad y la descentralización de la red Bitcoin es una iniciativa noble. Esto ayuda a fortalecer la resiliencia de la red y a resistir la censura y los ataques.
* En contra: Sin un incentivo financiero suficiente, puede ser difícil para los mineros continuar apoyando la red, especialmente si operan con pérdidas.

La iniciativa Attakai destaca la importancia de contribuir a la red mientras ofrece soluciones para hacer la minería más accesible y menos perjudicial. La posibilidad de minar en casa, con equipos más asequibles y soluciones para reducir la contaminación acústica, puede ayudar a democratizar la minería de Bitcoin. Anima a aquellos interesados en Bitcoin no solo a invertir y poseer bitcoins, sino también a participar activamente en la seguridad de la red. Al proporcionar equipos probados y guías para el ensamblaje e instalación, Attakai facilita la entrada al mundo de la minería de Bitcoin. También fomenta la innovación y las mejoras continuas, invitando a la comunidad a contribuir y compartir sus ideas y experiencias para mejorar la minería en casa. El modelo Attakai es una respuesta a la pregunta de minar por ganancias o por la red. No se trata solo de obtener ganancias, sino también de fortalecer la distribución y la seguridad de la red Bitcoin, permitiendo que más personas participen en la minería, aprendan y comprendan esta industria crucial. El desafío de una posible prohibición de la minería en Europa sigue siendo una cuestión abierta. Esto plantea preocupaciones sobre el futuro de la minería de Bitcoin en la región y la necesidad de una regulación equilibrada que reconozca la importancia de la minería para la seguridad y viabilidad de la red Bitcoin, mientras se abordan las cuestiones ambientales. Attakai y otras iniciativas similares pueden desempeñar un papel crucial en este debate, mostrando que es posible minar de manera más sostenible y responsable, contribuyendo positivamente a la red Bitcoin.

## Soberanía y regulación

<chapterId>9d9a5908-2acc-501e-906b-a6fce9ecfebd</chapterId>

### ¿Soberanía antes que ganancias?

Para abordar la cuestión crucial de la riqueza a través de la minería, es importante considerar diversas perspectivas y enfoques. Las preguntas sobre la rentabilidad de la minería son frecuentes, con cuestiones que rodean la compra de acciones de empresas como Riot o el alquiler de máquinas para minar en países con bajo costo energético como Islandia o Rusia. Antes de aventurarse en la minería, una consideración esencial sería comparar la rentabilidad de la minería con la compra directa de Bitcoin. Si el costo de minar un Bitcoin supera el costo de compra directa, generalmente es más sensato comprar el Bitcoin directamente. Esto evita los múltiples desafíos y costos asociados al proceso de minería.

Sin embargo, la minería ofrece vías únicas para involucrarse en el ecosistema de Bitcoin. Por ejemplo, minar Bitcoin en invierno puede ser una manera ingeniosa de calentar tu vivienda mientras generas ingresos en Bitcoin. Otra opción consiste en invertir en empresas que venden hardware de minería y que almacenan y gestionan las máquinas en ubicaciones de bajo costo energético, ofreciendo así acceso a tarifas eléctricas ventajosas sin los problemas de gestionar los equipos.

A pesar de estas opciones, la minería presenta desafíos significativos. El adagio bien conocido del mundo de las criptomonedas, "No tus claves, no tus Bitcoins", encuentra un eco similar en el mundo de la minería: "No tu tasa de hash, no tu recompensa". Las historias de decepciones y de máquinas desconectadas son comunes, con muchos actores prometiendo resultados excepcionales pero no cumpliéndolos. Los problemas de suministro eléctrico y las averías de las máquinas pueden dejar a los inversores impotentes, con equipos costosos que no controlan. En este contexto, la prudencia y una comprensión profunda del sector de la minería son cruciales antes de aventurarse en él. Aunque existen oportunidades de ganancias, los riesgos son significativos, y un enfoque informado y reflexivo es esencial para navegar en este campo complejo y a menudo impredecible. Por lo tanto, es vital realizar investigaciones exhaustivas y sopesar bien los pros y los contras antes de comprometerse con la minería de Bitcoin.

![image](assets/en/13.webp)

### Bitcoins Virgenes

La aspiración de poseer su propio hashrate se presenta como un camino prometedor en el universo de la minería. Sin embargo, navegar en este ecosistema complejo requiere un enfoque prudente. El ámbito del cloud mining está marcado por un gran número de estafas, alimentadas por una falta de comprensión del minado por parte de muchos inversores. Las ofertas tentadoras, presentadas de diversas maneras, pueden fácilmente inducir a error a aquellos que no están suficientemente informados. Por otro lado, poseer su propio equipo de minería ofrece ventajas considerables. Además de la satisfacción personal de contribuir activamente a la seguridad de la red Bitcoin y de ver las recompensas acumularse en su cartera, está el atractivo de los "bitcoins vírgenes". Estos son bitcoins recién minados, que nunca han sido gastados y que no tienen ninguna historia adjunta a ellos. Estos bitcoins son a menudo considerados más valiosos porque nunca han sido "contaminados", ofreciendo cierta garantía contra el rechazo por parte de reguladores o grandes plataformas de intercambio.

La posibilidad de minar bitcoins vírgenes mientras se evitan los procedimientos de conocimiento del cliente (KYC) es otro valor añadido. Muchos pools de minería no requieren la identidad de los mineros, permitiendo así adquirir bitcoins sin pasar por verificaciones de identidad tediosas. Los bitcoins vírgenes son percibidos como "limpios", sin llevar ninguna historia ni asociación pasada. Son especialmente buscados por los grandes actores institucionales que pueden garantizar la legitimidad de sus activos digitales frente a las autoridades de regulación. Sin embargo, a pesar de estas ventajas, es crucial reconocer que la industria de la minería sigue siendo extremadamente competitiva y volátil y que incidentes imprevistos pueden perturbar las operaciones de minería.

En este contexto, la elección de un enfoque autónomo y educado en materia de minería parece prudente. Adquirir su propio hashrate e invertir en equipos de minería personales, mientras se permanece consciente de los riesgos y desafíos, puede potencialmente ofrecer un camino más seguro y más satisfactorio hacia la adquisición de bitcoins vírgenes, reforzando así la soberanía financiera del individuo mientras se apoya al ecosistema Bitcoin en su conjunto.

### ¿La minería prohibida en Europa?

Con la cuestión del potencial de prohibición de la minería en Europa, las discusiones sobre la regulación se vuelven cada vez más pertinentes. El paisaje regulatorio fluctuante puede, de hecho, influir considerablemente en la industria de la minería de Bitcoin. La prohibición de la minería en Europa es un escenario posible, especialmente considerando los precedentes en China. Aunque las operaciones de minería continúan en China a pesar de la prohibición, Europa podría seguir un camino similar. Una distribución más amplia del hashrate en diferentes regiones podría ayudar a fortalecer la comunidad de mineros en Europa, permitiéndoles oponerse eficazmente a los malentendidos y las ideas erróneas sobre la minería, su impacto ambiental y su huella en la red eléctrica.
![image](assets/en/14.webp)

Ante campañas como las de Greenpeace y las cifras a menudo engañosas de algunos estudios, la mejor arma sigue siendo la información veraz. Es esencial informar al público general y a los tomadores de decisiones sobre la realidad de la minería, su complejidad y su matiz, en lugar de dejar que se apoyen en clichés e información inexacta. Cuantas más personas estén informadas y conscientes de lo que realmente es la minería, mejor podrá defenderse la industria contra posibles regulaciones restrictivas.

En conclusión, a pesar del riesgo regulatorio y la posibilidad de una prohibición de la minería en Europa, la herramienta más poderosa sigue siendo la educación y la información. Una comprensión clara y precisa de la minería, su funcionamiento y su impacto puede ayudar a desmitificar la industria y combatir la desinformación, ofreciendo así una mejor resistencia a las regulaciones potencialmente dañinas. La iniciativa de formar e informar a la gente sobre la minería, como lo hace esta discusión, es un paso en la dirección correcta para garantizar la sostenibilidad y el crecimiento de la minería en Europa y en todo el mundo. Los esfuerzos continuos para educar e informar son esenciales para asegurar un futuro seguro y próspero para la industria de la minería de Bitcoin.

## Entrevista a un profesional de la industria de la minería

<chapterId>4d613261-d1a8-5ffe-a50c-047a3d77d6c5</chapterId>

### Los entresijos de la minería industrial - Sebastien Gouspillou

![Los entresijos de la minería industrial - Sebastien Gouspillou](https://www.youtube.com/watch?v=vYaQRLSDr5E&t=69s)

# Minería en casa y reutilización del calor

<partId>78d22d06-2c4a-573f-86bb-1027115dad3a</partId>

## Attakai - ¡La minería en casa hecha posible y accesible!

<chapterId>1f5d1b74-2f99-5f31-a088-a73d36491ebf</chapterId>

Attakai, que significa "la temperatura ideal" en japonés, es el nombre de la iniciativa para descubrir la minería de bitcoins a través de la reutilización del calor lanzada por @ajelexBTC y @jimzap21 con Découvre Bitcoin.
Esta guía de modernización de un ASIC servirá como base para aprender más sobre la minería, su funcionamiento y la economía subyacente, demostrando la posibilidad de adaptar un minero de Bitcoin para su uso como radiadores en viviendas. Esto ofrece más comodidad y ahorro, permitiendo a los participantes obtener reembolsos en BTC sin KYC en su factura de calefacción eléctrica.

Bitcoin ajusta automáticamente la dificultad de minería y recompensa a los mineros por su participación, sin embargo, la concentración del hashrate puede plantear riesgos para la neutralidad de la red. Utilizar la potencia de cálculo de Bitcoin para soluciones de calefacción beneficia directamente a la red misma, aumentando la distribución de la potencia de cálculo.

### ¿Por qué reutilizar el calor de un ASIC?

Es importante entender la relación entre la energía y la producción de calor en un sistema eléctrico.

Por una inversión de 1 kW de energía eléctrica, un radiador eléctrico produce 1 kW de calor, ni más ni menos. Los nuevos radiadores no son más eficientes que los radiadores tradicionales. Su ventaja radica en su capacidad para difundir el calor de manera continua y uniforme en una habitación, brindando así más comodidad en comparación con los radiadores tradicionales que alternan entre una alta potencia de calefacción y la falta de calefacción, generando fluctuaciones regulares de temperatura e incomodidad.

Una computadora, o más ampliamente una tarjeta electrónica, no consume energía para realizar cálculos, simplemente necesita que la energía circule en sus componentes para funcionar. El consumo de energía se debe a la resistencia eléctrica de los componentes, que produce pérdidas y genera calor, esto es lo que se conoce como el efecto Joule.

Algunas empresas han tenido la idea de combinar las necesidades de potencia de cálculo y las necesidades de calefacción mediante radiadores/servidores. La idea es distribuir los servidores de una empresa en pequeñas unidades que podrían colocarse en viviendas u oficinas. Sin embargo, esta idea enfrenta varios problemas. Las necesidades de los servidores no están relacionadas con las necesidades de calefacción y las empresas no pueden utilizar las capacidades de cálculo de sus servidores de manera flexible. También existen limitaciones en el ancho de banda que los particulares pueden tener. Todas estas restricciones no permiten que la empresa rentabilice estas costosas instalaciones ni brinde una oferta estable de servidores en línea sin tener centros de datos capaces de asumir el control cuando no se necesita calefacción.

> El calor de tu computadora no se desperdicia si necesitas calentar tu hogar. Si estás utilizando calefacción eléctrica en tu casa, entonces el calor de tu computadora no es un desperdicio. Es el mismo costo si generas este calor con tu computadora. Si tienes otro sistema de calefacción más barato que el eléctrico, entonces el desperdicio está solo en la diferencia de costo. Si es verano y estás utilizando aire acondicionado, entonces es el doble. La minería de bitcoins debería ocurrir donde sea más barata. Tal vez sea en lugares con clima frío y calefacción eléctrica, donde la minería se vuelva gratuita.
> Satoshi Nakamoto - 8. agosto 2010

Bitcoin y su prueba de trabajo se destacan porque ajustan automáticamente la dificultad de la minería en función de la cantidad de cálculos realizados por toda la red, esta cantidad se llama hashrate y se expresa en hash/segundo. Hoy en día se estima en 380 Exahash/segundo, lo que equivale a 380 billones de billones de hash/segundo. Este hashrate representa trabajo y, por lo tanto, una cantidad de energía gastada. Cuanto mayor sea el hashrate, mayor será la dificultad y viceversa. De esta manera, se puede activar o desactivar un minero de Bitcoin en cualquier momento sin afectar a la red, a diferencia de los radiadores/servidores que necesitan mantenerse estables para ofrecer su servicio. El minero es recompensado por su participación, por pequeña que sea, en relación con la de los demás.

En resumen, un radiador eléctrico y un minero de Bitcoin producen ambos 1 kW de calor por cada 1 kW de electricidad gastada. Sin embargo, el minero también recibe bitcoins como recompensa. Independientemente del precio de la electricidad, el precio de bitcoin o la competencia en la actividad minera en la red de Bitcoin, es económicamente más ventajoso calentarse con un minero que con un radiador eléctrico.

### El valor agregado para Bitcoin

Lo importante de entender es cómo la minería contribuye a la descentralización de Bitcoin.
Varias tecnologías existentes se han combinado ingeniosamente para dar vida al consenso de Nakamoto. Este consenso permite recompensar económicamente a los actores honestos por su participación en el funcionamiento de la red de Bitcoin, al mismo tiempo que desalienta a los actores deshonestos. Este es uno de los puntos clave que permite que la red exista de manera sostenible.
Los actores honestos, aquellos que realizan la minería de acuerdo con las reglas, compiten entre sí para obtener la mayor parte posible de la recompensa por la producción de nuevos bloques. Este incentivo económico naturalmente conduce a una forma de centralización, ya que las empresas eligen especializarse en esta actividad lucrativa al reducir sus costos a través de economías de escala. Estos actores industriales tienen una posición ventajosa para la compra, mantenimiento de máquinas y negociación de tarifas de electricidad al por mayor.

> Al principio, la mayoría de los usuarios ejecutarían nodos de red, pero a medida que la red creciera más allá de cierto punto, cada vez más se dejaría en manos de especialistas con granjas de servidores de hardware especializado. Una batería de servidores solo necesitaría un nodo en la red y el resto de la LAN se conectaría a ese nodo.
> Satoshi Nakamoto - 2 de noviembre de 2008

Algunas entidades poseen un porcentaje considerable de la tasa de hash total en grandes granjas de minería. Se puede observar la reciente ola de frío en los Estados Unidos, donde una parte importante de la tasa de hash se desconectó para redirigir la energía a los hogares que necesitaban electricidad de manera excepcional. Durante varios días, los mineros fueron incentivados económicamente a apagar sus granjas, por lo que se puede ver este clima excepcional en la curva de la tasa de hash de Bitcoin.

Este tema podría volverse problemático y representar un riesgo importante para la neutralidad de la red. Un actor que posea más del 51% de la tasa de hash podría censurar transacciones más fácilmente si así lo deseara. Por eso es importante distribuir la tasa de hash entre múltiples actores en lugar de entidades centralizadas que podrían ser más fácilmente confiscadas por un gobierno, por ejemplo.

**Si los mineros están distribuidos en miles, incluso millones, de hogares en todo el mundo, se vuelve muy complicado para un Estado tomar el control.**

Cuando sale de fábrica, un minero no es adecuado para servir como calefactor en una vivienda debido a dos problemas principales: ruido excesivo y falta de ajuste. Sin embargo, estos problemas se pueden resolver fácilmente mediante modificaciones de hardware y software, lo que permite obtener un minero mucho más silencioso y que se puede configurar y automatizar como los calentadores eléctricos modernos.

**Attakaï es una iniciativa educativa que te enseña cómo realizar una adaptación del Antminer S9 de la manera más económica posible.**

Es una excelente oportunidad para aprender practicando y ser recompensado por tu participación con satoshis sin necesidad de KYC.

## Guía de compra para un ASIC de segunda mano

<chapterId>3b0b3bf0-859b-57f2-b92f-843ac70b7e68</chapterId>

En esta sección veremos las mejores prácticas para comprar un Bitmain Antminer S9 de segunda mano, la máquina en la que se basará este tutorial de retrofitting en radiador. Esta guía también funciona para otros modelos de ASIC, ya que es una guía de compra general para equipos de minería de segunda mano.

El Antminer S9 es un dispositivo ofrecido por Bitmain desde mayo de 2016. Consume 1400W de electricidad y produce 13.5 TH/s. Aunque se considera antiguo, sigue siendo una excelente opción para comenzar a minar. Dado que se produjo en grandes cantidades, es fácil encontrar piezas de repuesto en abundancia en muchas regiones del mundo. Por lo general, se puede adquirir de persona a persona en sitios como Ebay o LeBonCoin, ya que los revendedores dirigidos a profesionales ya no lo ofrecen debido a su menor competitividad en comparación con máquinas más nuevas. Es menos eficiente que ASIC como el Antminer S19, lanzado en marzo de 2020, pero esto lo convierte en un hardware de segunda mano asequible y más adecuado para las modificaciones que vamos a realizar.

El Antminer S9 existe en varias variantes (i, j) que realizan cambios menores en el hardware de primera generación. No creemos que este elemento deba influir en su decisión de compra y esta guía funciona para todas estas variantes.

El precio de los ASIC varía según muchos factores como el precio del bitcoin, la dificultad de la red, la eficiencia de la máquina y el costo de la electricidad. Por lo tanto, es difícil dar una estimación precisa para la compra de una máquina de segunda mano. En febrero de 2023, el precio esperado en Francia generalmente oscila entre 100€ y 200€, pero estos precios pueden cambiar rápidamente.

![imagen](assets/en/15.webp)

El Antminer S9 está compuesto por las siguientes partes:

- 3 hashboards que contienen los chips que producen el hash

![imagen](assets/en/16.webp)

- Una tarjeta de control que incluye una ranura para una tarjeta SD, un puerto Ethernet y conectores para los hashboards y los ventiladores. Es el cerebro de su ASIC.

![imagen](assets/en/17.webp)

- 3 cables de datos que conectan los hashboards con la tarjeta de control

![imagen](assets/en/18.webp)

- La fuente de alimentación que funciona con 220V y, por lo tanto, se puede conectar como un electrodoméstico común

![imagen](assets/en/19.webp)

- 2 ventiladores de 120mm

![imagen](assets/en/20.webp)

- Un cable macho C13

![imagen](assets/en/21.webp)

Cuando compres una máquina de segunda mano, es importante verificar que todas las piezas estén incluidas y funcionales. Durante el intercambio, debes pedir al vendedor que encienda la máquina para verificar su correcto funcionamiento. Es importante comprobar que el dispositivo se encienda correctamente y luego verificar la conectividad a Internet conectando un cable Ethernet y accediendo a la interfaz de inicio de sesión de Bitmain a través de un navegador web en la misma red local. Puedes encontrar esta dirección IP conectándote a la interfaz de tu enrutador de Internet y buscando los dispositivos conectados. Esta dirección debería tener el siguiente formato: 192.168.x.x

![image](assets/en/22.webp)

También verifica que las credenciales predeterminadas funcionen (nombre de usuario: root, contraseña: root). Si las credenciales predeterminadas no funcionan, deberás restablecer la máquina.

![image](assets/en/23.webp)

Una vez conectado, deberías poder ver el estado de cada placa hash en el panel de control. Si el minero está conectado a un grupo de minería, deberías ver que todas las placas hash funcionen. Es importante tener en cuenta que los mineros hacen mucho ruido, es normal. Asegúrate también de que los ventiladores funcionen correctamente.

Luego puedes eliminar el grupo de minería del antiguo propietario para configurar el tuyo propio más adelante. Si lo deseas, también puedes inspeccionar las placas hash desmontando la máquina. Sin embargo, este paso es más complejo y requiere más tiempo y algunas herramientas. Si deseas realizar este desmontaje, puedes consultar la siguiente parte de este tutorial que detalla cómo hacerlo. Es importante tener en cuenta que los mineros acumulan mucho polvo y requieren un mantenimiento regular. Podrás observar esta acumulación de polvo y la calidad del mantenimiento al desmontar la máquina.
Después de revisar todos estos puntos, puedes comprar tu máquina con un alto grado de confianza. En caso de duda, consulta a la comunidad.

Para resumir esta guía en una frase: **"No confíes, verifica"**.

[También puedes recurrir a profesionales en la reacondicionamiento de máquinas de minería, como nuestro socio 21energy. Ofrecen S9 probados, limpios y con el software BraiiinOS+ ya instalado. Con el código de afiliación "decouvre", obtendrás un 10% de descuento en la compra de un S9 mientras apoyas el proyecto Attakai.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)

## Guía de compra de piezas para modificaciones de hardware del S9

<chapterId>fa5f5eca-bcbf-5a83-9b03-98ecbadbabd6</chapterId>

Propietario de un Antminer S9, probablemente sepas lo ruidoso y voluminoso que puede ser este equipo. Sin embargo, es posible convertirlo en una calefacción silenciosa y conectada siguiendo algunos pasos simples. En esta sección, te presentaremos los equipos necesarios para realizar las modificaciones.
Si eres un hábil manitas y estás buscando convertir un minero en una calefacción, este tutorial es para ti. Queremos advertirte que las modificaciones realizadas a un dispositivo electrónico pueden presentar riesgos eléctricos. Por lo tanto, es esencial tomar todas las precauciones necesarias para evitar cualquier daño o lesión.

1. Reemplazar los ventiladores

Los ventiladores originales del Antminer S9 son demasiado ruidosos para usar tu Antminer como calefacción. La solución es reemplazarlos por ventiladores más silenciosos. Nuestro equipo ha probado varios modelos de la marca Noctua y ha seleccionado el Noctua NF-A14 iPPC-2000 PWM como la mejor opción, asegúrate de elegir la versión de 12V de los ventiladores. Este ventilador de 140mm puede generar hasta 1200W de calefacción manteniendo un nivel teórico de ruido de 31 dB. Para poder instalar estos ventiladores de 140mm, deberás utilizar un adaptador de 140mm a 120mm que podrás encontrar en la tienda de DécouvreBitcoin. También agregaremos rejillas de protección de 140mm.

![imagen](assets/en/24.webp)
![imagen](assets/en/25.webp)
![imagen](assets/en/26.webp)

El ventilador de la fuente de alimentación también es bastante ruidoso y debe ser reemplazado. Recomendamos el Noctua NF-A6x25 PWM. Ten en cuenta que los conectores de los ventiladores Noctua no son los mismos que los originales, por lo que necesitarás un adaptador para conectarlos, con 2 será suficiente. También asegúrate de elegir la versión de 12V del ventilador.

![imagen](assets/en/27.webp)
![imagen](assets/en/28.webp)

2. Agregar un puente WIFI/Ethernet

En lugar de utilizar un cable Ethernet, puedes conectar tu Antminer a través de WIFI agregando un puente WIFI/Ethernet. Hemos seleccionado el vonets vap11g-300 porque permite recuperar fácilmente la señal WIFI de tu caja de Internet y transmitirla a tu Antminer a través de Ethernet sin crear una subred. Si tienes habilidades eléctricas, puedes alimentarlo directamente con la fuente de alimentación del Antminer sin necesidad de agregar un cargador USB, para ello necesitarás un conector hembra de 5,5mmx2,1mm.

![imagen](assets/en/29.webp)
![imagen](assets/en/30.webp)

3. Opcional: agregar un enchufe conectado.
   Si desea encender/apagar su Antminer desde su teléfono inteligente y monitorear su consumo de energía, puede agregar un enchufe inteligente. Hemos probado el enchufe ANTELA en su versión de 16A compatible con la aplicación smartlife. Este enchufe inteligente permite consultar el consumo diario y mensual y se conecta directamente a su enrutador de Internet a través de WIFI.
   ![imagen](assets/en/31.webp)

Lista de materiales y enlaces

- 2X adaptador de pieza 3D de 140 mm a 120 mm

- [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)

- [2X rejillas de ventilador de 140 mm](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)

- [Cable eléctrico de 2,5 mm2](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
- [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
- [Enchufe inteligente opcional ANTELA](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

# Attakai - modificación del software de un Antminer S9

<partId>afc9c29a-84aa-5f1d-82e2-5fd9ff2e1805</partId>

## Configuración de un puente WIFI/Ethernet Vonet

<chapterId>3cf487a4-21ef-5b24-83d5-789b811f740f</chapterId>

Para conectar su ASIC a través de WIFI, necesitará un dispositivo llamado puente, que permite recibir la señal WIFI de su enrutador y transmitirla a otro dispositivo a través de Ethernet.

Hay muchos dispositivos que pueden hacer esto, recomendamos el VONETS WiFi Bridge/Repeteur por su practicidad.

Alimente el puente conectándolo a través de USB.

Desde su computadora, conéctese a la red WIFI VONETS\_**\*\*** con la contraseña 12345678.

![imagen](assets/en/32.webp)

Identificación de administrador: admin admin

![imagen](assets/en/33.webp)

Seleccione "Wizard"

![imagen](assets/en/34.webp)

Seleccione la red WIFI a la que desea conectar su minero y haga clic en "Next".

ATENCIÓN: el puente Vonet solo funciona en 2,4 GHz. Hoy en día, los enrutadores generalmente ofrecen dos redes WIFI, una en 2,4 GHz y otra en 5 GHz.

![imagen](assets/en/35.webp)

Ingrese la contraseña de su red WIFI en "Source WIFI hotspot password".
Si no desea utilizar su puente Vonet para extender su red WIFI, marque la casilla "Disable Hotspot". De lo contrario, puede dejar esta casilla desmarcada.

Luego, puede hacer clic en "Apply".

Y finalmente, deberá hacer clic en "reboot" para reiniciar el puente. El puente se reiniciará en unos minutos.

El puente debería conectarse a su enrutador y aparecerá con el nombre de "[VONETS.COM](http://vonets.com/)".
Es posible que sea necesario desconectar y volver a conectar el puente si no se conecta después de unos minutos.

Una vez que el puente esté conectado, conecte el cable Ethernet del puente a su ASIC y luego conecte el ASIC a la corriente. Luego podrá acceder a la interfaz del ASIC de la misma manera que si estuviera conectado directamente a su enrutador a través de Ethernet.

## Restablecer un Antminer S9

<chapterId>b518b6bd-9dae-5136-ae3c-1fafb1cb2592</chapterId>

Antes de instalar BraiinOS+, puede ser necesario restablecer su S9 a sus configuraciones de fábrica.
Esta método se puede aplicar entre 2 minutos y 10 minutos después de encender el minero.
2 minutos después de encender el minero, presione el botón "Reset" durante 5 segundos y luego suéltelo. El minero se restaurará a los ajustes de fábrica en 4 minutos y se reiniciará automáticamente (no es necesario apagarlo).

![imagen](assets/en/36.webp)

## Instalar BraiinsOS+ en un Antminer S9

<chapterId>38e8b1a8-8b1d-51ed-8b92-59d4ddb15184</chapterId>

El software original instalado por Antminer en sus máquinas de minería tiene funciones limitadas. Por eso, en esta guía vamos a instalar otro software llamado BraiinsOS+. Es un software de terceros desarrollado por el primer grupo de minería de Bitcoin que tiene más funciones y permite, por ejemplo, modificar la potencia de la máquina.

Hay varias formas de instalar Braiins OS+ en un ASIC. Puede consultar esta guía, así como la [documentación oficial de Braiins](https://academy.braiins.com/en/braiins-os/about/).

Aquí veremos cómo instalar fácilmente Braiins OS+ directamente en la memoria de su Antminer con el software BOS toolbox, reemplazando así el sistema operativo original, a través de los siguientes pasos detallados.

1. Encienda su Antminer y conéctelo a su caja de internet.
2. Descargue BOS toolbox para Windows / Linux.
3. Descomprima el archivo descargado y abra el archivo bos-toolbox.bat, elija el idioma y después de unos momentos verá esta ventana:

![imagen](assets/en/37.webp)

4. BOS toolbox le permitirá encontrar fácilmente la dirección IP de su Antminer e instalar BraiinsOS+. Si ya conoce la dirección IP de su máquina, puede pasar al paso 8. De lo contrario, vaya a la pestaña de escaneo.

![imagen](assets/en/38.webp)

5. Por lo general, en las redes domésticas, el rango de direcciones IP se encuentra entre 192.168.1.1 y 192.168.1.255, así que ingrese "192.168.1.0/24" en el campo de rango de IP. Si su red es diferente, cambie estas direcciones en consecuencia. Luego haga clic en "Start".

6. Tenga en cuenta que si el Antminer tiene una contraseña, la detección no funcionará. Si ese es el caso, lo más sencillo es realizar un reinicio.

7. Debería ver todos los Antminer en su red, aquí la dirección IP es 192.168.1.37.

![imagen](assets/en/39.webp)

8. Haga clic en "Back" y luego en la pestaña "install", ingrese la dirección IP encontrada anteriormente y haga clic en "Start".

> Si la instalación no funciona, puede ser necesario realizar un reinicio y volver a intentarlo (consulte la sección anterior).

![image](assets/en/40.webp)

9. Después de unos momentos, su Antminer se reiniciará y podrá acceder a la interfaz de Braiins OS+ en la dirección IP mencionada, aquí 192.168.1.37, que debe ingresar directamente en la barra de direcciones de su navegador, el nombre de usuario predeterminado es "root" y no hay contraseña predeterminada.

## Configurar BraiinsOS+

<chapterId>36e432f2-85bc-52d0-a62a-009fc4c69338</chapterId>

Deberá conectarse a su ASIC utilizando la dirección IP local de su dispositivo en su red a través de un navegador.

Puede encontrar la dirección IP de su máquina con la herramienta BOS toolbox o directamente en la página web de su enrutador.

Las credenciales predeterminadas son las mismas que las del sistema operativo original.

- nombre de usuario: root
- contraseña: (ninguna)

Luego será recibido por el panel de control de Brains OS+.

### Panel de control

![image](assets/en/41.webp)

En esta primera página, podrá observar el rendimiento de su máquina en tiempo real.

- Tres gráficos en tiempo real que muestran la temperatura, el hashrate y el estado general de su máquina.
- A la derecha, el hashrate real, la temperatura promedio de los chips, su eficiencia estimada en W/THs y el consumo de energía.
- Debajo, la velocidad de rotación de los ventiladores en porcentaje de la velocidad máxima y el número de rotaciones por minuto.

![image](assets/en/42.webp)

- Más abajo encontrará una vista detallada de cada hashboard. La temperatura promedio de la placa y los chips que la componen, el voltaje y la frecuencia.
- Detalles sobre los grupos de minería activos en Pools.
- El estado de la sintonización automática en Tuner Status.
- A la derecha, detalles sobre los datos transmitidos al grupo de minería.

### Configuración

![image](assets/en/43.webp)

### Sistema

![image](assets/en/44.webp)

### Acciones rápidas

![image](assets/en/45.webp)

# Attakai - Modificación de los ventiladores

<partId>98266a8f-3745-58a0-9f6b-26a9734e1427</partId>

## Reemplazar el ventilador de la fuente de alimentación

<chapterId>0c6befa7-f3ef-5bcf-ae8d-0ad5e5d41d70</chapterId>

> ADVERTENCIA: Es esencial haber instalado previamente Braiins OS+ en su minero, u otro software que tenga la capacidad de reducir el rendimiento de su máquina. Esta medida es crucial, ya que para reducir el ruido, instalaremos ventiladores menos potentes, que podrán disipar menos calor.

![image](assets/en/46.webp)

### Materiales necesarios

- 1 ventilador Noctua NF-A6x25 PWM
- Cable eléctrico de 2,5 mm2

> ADVERTENCIA: Antes de comenzar, asegúrese de haber desconectado su minero para evitar cualquier riesgo de electrocución.

![image](assets/en/47.webp)

Primero, retire las 6 tornillos en el lateral de la carcasa que la mantienen cerrada. Una vez retirados los tornillos, abre cuidadosamente la carcasa para quitar la protección de plástico que cubre los componentes.

![image](assets/en/48.webp)
![image](assets/en/49.webp)

Luego, es hora de quitar el ventilador original teniendo cuidado de no dañar los otros componentes. Para hacerlo, retire los tornillos que lo mantienen en su lugar y despegue suavemente el adhesivo blanco que rodea el conector. Es importante proceder con delicadeza para evitar dañar los cables o los conectores.

![image](assets/en/50.webp)

Una vez retirado el ventilador original, notarás que los conectores del nuevo ventilador Noctua no coinciden con los del ventilador original. De hecho, el nuevo ventilador tiene 3 cables, incluido un cable amarillo que permite controlar la velocidad. Sin embargo, este cable no se utilizará en este caso específico. Para conectar el nuevo ventilador, se recomienda utilizar un adaptador especial. Sin embargo, es importante tener en cuenta que este adaptador a veces puede ser difícil de encontrar.

![image](assets/en/51.webp)

Si no tienes este adaptador, aún puedes conectar el nuevo ventilador utilizando un empalme de cables. Para ello, deberás cortar los cables del ventilador antiguo y del nuevo ventilador.

![image](assets/en/52.webp)
![image](assets/en/53.webp)

En el nuevo ventilador, usa un cortador y corta cuidadosamente los contornos de la cubierta principal a 1 cm sin cortar las cubiertas de los cables debajo.

![image](assets/en/54.webp)

Luego, tirando hacia abajo de la cubierta principal, corta las cubiertas de los cables rojo y negro de la misma manera que antes. Y corta el cable amarillo al ras.

![image](assets/en/55.webp)

En el ventilador antiguo, es más delicado cortar la cubierta principal sin dañar las cubiertas de los cables rojo y negro. Para ello, hemos utilizado una aguja que hemos deslizado entre la cubierta principal y los cables rojo y negro.

![image](assets/en/56.webp)
![image](assets/en/57.webp)

Una vez que los cables rojo y negro estén libres, corta las cubiertas con cuidado para no dañar los cables eléctricos.

![image](assets/en/58.webp)

Luego, conecta los cables con un empalme, el cable negro con el negro y el cable rojo con el rojo. También puedes añadir cinta aislante.

![image](assets/en/59.webp)
![image](assets/en/60.webp)

Una vez realizada la conexión, es hora de instalar el nuevo ventilador Noctua con la rejilla y los tornillos antiguos, los nuevos tornillos que se encuentran en la caja se reutilizarán más adelante. Asegúrese de colocarlo en la orientación correcta. Notará una flecha en uno de los lados del ventilador, que indica la dirección del flujo de aire. Es importante colocar el ventilador de manera que esta flecha apunte hacia el interior del estuche. Luego, vuelva a conectar el ventilador.

![image](assets/en/61.webp)
![image](assets/en/62.webp)

> Opcional: Si tiene conocimientos de electricidad, puede agregar directamente a la salida de alimentación de 12V un conector hembra jack de 5,5 mm que permitirá alimentar directamente el puente Wi-Fi Vonet. Sin embargo, si no está seguro de sus habilidades eléctricas, es mejor utilizar el conector USB con un cargador de tipo smartphone para evitar cualquier riesgo de cortocircuito o daño eléctrico.

![image](assets/en/63.webp)

Una vez realizadas las conexiones, vuelva a colocar la cubierta de plástico sobre la carcasa de plástico y no dentro de ella.

![image](assets/en/64.webp)

Finalmente, vuelva a colocar la cubierta de la carcasa en su lugar y vuelva a atornillar los 6 tornillos en los lados para mantener todo en su lugar. ¡Y listo, su caja de alimentación ahora está equipada con un nuevo ventilador!

## Reemplazar los ventiladores principales

<chapterId>a29f60f1-3fa3-57fc-a630-9c97cec30e56</chapterId>

> ATENCIÓN: Es esencial haber instalado previamente Braiins OS+ en su minero, u otro software que tenga la capacidad de reducir el rendimiento de su máquina. Esta medida es crucial, ya que con el fin de reducir el ruido, instalaremos ventiladores menos potentes, que podrán disipar menos calor.

![image](assets/en/46.webp)

### Materiales necesarios

- 2 adaptadores 3D de 140 mm a 120 mm
- 2 ventiladores Noctua NF-A14 iPPC-2000 PWM
- 2 rejillas de ventilador de 140 mm

> ATENCIÓN: En primer lugar, antes de comenzar, asegúrese de haber desconectado su minero para evitar cualquier riesgo de electrocución.

1. En primer lugar, desconecte los ventiladores y desenrósquelos.

![image](assets/en/65.webp)

2. Los conectores de los nuevos ventiladores Noctua no coinciden con los originales, ¡pero no se preocupe! Saque su cortador y corte cuidadosamente las pequeñas lengüetas de plástico para que los conectores se adapten perfectamente a su minero.

![image](assets/en/66.webp)
![image](assets/en/67.webp)

3. ¡Es hora de instalar las piezas 3D!
   Fíjelas en ambos lados del minero utilizando los tornillos que retiraste de los ventiladores. Aprieta hasta que la cabeza del tornillo esté dentro de la pieza 3D y esta esté bien sujeta en su lugar. Ten cuidado de no apretar demasiado, ¡podrías deformar la pieza y uno de los tornillos podría tocar un condensador!

![imagen](assets/en/68.webp)

4. Ahora pasemos a los ventiladores.
   Fíjalos en las piezas 3D utilizando los tornillos proporcionados en la caja. Ten en cuenta la dirección del flujo de aire, las flechas en los lados de los ventiladores te indicarán la dirección a seguir. Ve desde el lado del puerto Ethernet hacia el otro lado. Ver foto a continuación.

![imagen](assets/en/69.webp)
![imagen](assets/en/70.webp)
![imagen](assets/en/71.webp)

5. Último paso: conecta los ventiladores y fija las rejillas encima con los tornillos que no se utilizaron en la caja del ventilador de la fuente de alimentación. Solo tienes 4, pero 2 por rejilla en ángulos opuestos serán suficientes. Si es necesario, también puedes buscar otros tornillos similares en una tienda de bricolaje.

![imagen](assets/en/72.webp)
![imagen](assets/en/73.webp)

Mientras esperas para poder ofrecer una carcasa más atractiva a tu nuevo calentador, puedes sujetar la caja y la fuente de alimentación con abrazaderas de electricista.

![imagen](assets/en/74.webp)

Y para el toque final, conecta el puente Vonet al puerto Ethernet a su fuente de alimentación.

![imagen](assets/en/75.webp)

¡Y listo, felicidades! Acabas de reemplazar toda la parte mecánica de tu minero. Ahora deberías escuchar mucho menos ruido.

# Attakai - Configuración

<partId>9c3918a8-d9a3-5a1f-bb9a-70314f7ac175</partId>

## Unirse a un grupo de minería

<chapterId>b57a6105-0a53-5fe9-bad1-d6d9daf97c0d</chapterId>

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

![imagen](assets/en/76.webp)

Una vez que haya creado su cuenta, haga clic en "Connect To Pool".

Luego copie la dirección Stratum y su nombre de usuario:

![imagen](assets/en/77.webp)

Ahora puede volver a la interfaz de Braiins OS+ para ingresar estas credenciales. Para la contraseña, puede dejar el campo vacío.

![imagen](assets/en/78.webp)

## Optimizar el rendimiento de su Antminer S9

<chapterId>25380972-31c7-540d-80d8-17a06b171ca0</chapterId>

El overclocking y el autoajuste consisten en ajustar las frecuencias en las tarjetas de hash para mejorar el rendimiento del ASIC. La diferencia entre ambos radica en la complejidad de estos ajustes de frecuencia.

El overclocking es un ajuste simple que consiste en aumentar la frecuencia en las tarjetas de hash para aumentar la tasa de hash de la máquina. El underclocking, por otro lado, consiste en disminuir la frecuencia de reloj de un circuito integrado por debajo de su frecuencia nominal. Al reducir la frecuencia de reloj de un ASIC mediante el underclocking, también se reduce el calor generado por el hardware. Esto permite disminuir la velocidad de los ventiladores necesarios para enfriar el ASIC, ya que no tienen que trabajar tan duro para mantener una temperatura adecuada. Al reducir la velocidad de los ventiladores, también se reduce el ruido generado por el ASIC. Esto puede ser especialmente útil para los usuarios que utilizan ASIC en casa y buscan minimizar las molestias sonoras causadas por el equipo de minería.

Braiins OS+ admite el overclocking, el underclocking de los ASIC y el autoajuste. Permite a los usuarios ajustar la frecuencia de reloj de su hardware de manera flexible para maximizar el rendimiento o ahorrar energía según sus preferencias.

### Optimizar el rendimiento de su Antminer S9 con autoajuste

Antes de 2018, los mineros tenían dos formas de obtener una ventaja en su actividad: encontrar electricidad a un costo razonable y comprar hardware más eficiente. Sin embargo, en 2018, se descubrió un nuevo avance en el campo del software y firmware minero, llamado AsicBoost. Esta técnica permite a los mineros reducir sus costos en aproximadamente un 13% al modificar el firmware que se ejecuta en sus dispositivos.

Hoy en día, hay un nuevo avance en el sector de software y firmware minero llamado autorregulación (o autotuning) que ofrece una ventaja aún mayor que AsicBoost. Los ASIC están compuestos por numerosos chips informáticos pequeños que realizan el hashing. Estos chips están hechos de silicio, el mismo elemento ampliamente utilizado en semiconductores y otros componentes microelectrónicos. La comprensión clave aquí es que no todos los chips de silicio son idénticos, cada uno puede variar ligeramente en sus propiedades eléctricas. Los fabricantes de hardware lo saben y publican las especificaciones de rendimiento de sus máquinas mineras en función del límite inferior de sus tolerancias. En otras palabras, los fabricantes conocen la frecuencia que funciona mejor para los chips promedio y utilizan esta frecuencia de manera uniforme para todos los chips de la máquina.

Esto pone un límite superior a la tasa de hashing que una máquina puede tener. La autorregulación es un proceso en el que los algoritmos evalúan las frecuencias óptimas para el hashing chip por chip, en lugar de tratar toda la máquina como una sola unidad. Esto significa que un chip de mejor calidad que puede realizar más hash por segundo obtendrá una frecuencia más alta, y un chip de menor calidad que puede realizar relativamente menos obtendrá una frecuencia más baja. La autorregulación por chip es esencialmente una forma de optimizar el rendimiento de un ASIC a través del software y firmware que se ejecutan en él.

El resultado final es una tasa de hashing más alta por vatio de electricidad, lo que significa márgenes de beneficio más grandes para los mineros. La razón por la cual las máquinas no se distribuyen con este tipo de software es que la variabilidad por máquina no es deseable, ya que los clientes quieren saber exactamente lo que están obteniendo y, por lo tanto, es una mala idea para los fabricantes vender un producto que no tiene un rendimiento constante y predecible de una máquina a otra. Además, la autorregulación por chip requiere considerables recursos de desarrollo, ya que es compleja de implementar. Los fabricantes ya gastan muchos recursos en desarrollar sus propios firmwares. Existen soluciones de software que permiten implementar la autorregulación, como Braiins OS+. Además de mejorar el rendimiento del ASIC hasta en un 20%.

# Conclusión

<partId>fa42ec0b-b1fd-47f6-8268-6eab684c1d2b</partId>

## Evalúe este curso

<chapterId>6af13742-df68-5cf4-b7aa-93dc0c2eaae9</chapterId>
<isCourseReview>true</isCourseReview>

## Examen final

<chapterId>f51a7c88-3b7e-48df-b45f-22bb10fe619f</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusión

<chapterId>2941f29a-d6ce-4a3c-b61b-6e399f5395b1</chapterId>
¡Felicitaciones por completar este curso!

Nos complace que hayas alcanzado este importante hito en tu viaje de aprendizaje.

A través de tu dedicación y compromiso, has adquirido valiosos conocimientos y habilidades que te servirán en tu desarrollo profesional.

Para continuar explorando en profundidad el universo de Bitcoin, te invitamos a descubrir todos los otros cursos disponibles en Plan ₿ Network:

#### Descubre Bitcoin y sus fundamentos con

https://planb.network/courses/btc101

#### Descubre la Lightning Network con

https://planb.network/courses/lnp201

#### Domina los principios de la privacidad en Bitcoin

https://planb.network/courses/btc204

#### Descubre la historia de los orígenes de Bitcoin con

https://planb.network/courses/his201

#### Comprende cómo funciona la cartera Bitcoin con

https://planb.network/courses/cyp201

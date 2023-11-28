---
name: Acelerador de Desarrollo de Bitcoin
goal: Adquirir todas las bases para comenzar a desarrollar en Bitcoin
objectives:
  - Comprender los conceptos fundamentales y la tecnología que respalda a Bitcoin.
  - Adquirir habilidades prácticas en seguridad de Bitcoin, desarrollo de software y gobernanza de la red.
  - Desarrollar un dominio de la Lightning Network y sus protocolos asociados.
---

# Introducción

## Introducción a los cursos de CUBO+

![Video](https://youtu.be/4VuI9we_XYM)

Filippo y Mario ofrecen una charla introductoria sobre CUBO+, preparando el escenario para el completo viaje de aprendizaje que espera. Discuten la estructura de los cursos, los resultados de aprendizaje y cómo estos empoderarán a los estudiantes en el espacio del desarrollo de Bitcoin.

### Objetivos

El curso tiene como objetivo equipar a los participantes con una comprensión profunda de los principios subyacentes de Bitcoin, habilidades prácticas de desarrollo y la capacidad de navegar y contribuir al ecosistema de Bitcoin de manera efectiva. A través de una combinación de conocimientos teóricos y ejercicios prácticos, los estudiantes dominarán los aspectos esenciales de la seguridad de Bitcoin, las complejidades de su pila de software y los mecanismos de su gobernanza.

### Prerrequisitos

Se espera que los participantes tengan un fuerte sentido de curiosidad, un deseo de aprender a nivel profesional y algunos conocimientos fundamentales en desarrollo. Si bien no se requiere un conocimiento detallado de Bitcoin, es esencial tener una comprensión básica de los principios de codificación y una disposición para involucrarse con conceptos técnicos complejos para aprovechar al máximo el acelerador.

# Fundamentos de Bitcoin

## Pensamiento de Seguridad en Bitcoin

![Video](https://youtu.be/2f_rK74MB3U)

Peter Todd profundiza en las consideraciones de seguridad únicas de Bitcoin, enseñando a los desarrolladores cómo adoptar una mentalidad de seguridad en primer lugar. La conferencia tiene como objetivo inculcar una base sólida en el reconocimiento y mitigación de posibles amenazas en el desarrollo de Bitcoin, basándose en un ejercicio práctico de explicitar el Modelo de Amenazas del software para la marca de tiempo de las elecciones.

## Software Libre y de Código Abierto (FLOSS) en Bitcoin
![Video](https://youtu.be/GM-ho5M5_mQ)

El uso de Software Libre y de Código Abierto (FLOSS) es fundamental en el ecosistema de Bitcoin. Peter Todd explora la importancia de FLOSS para Bitcoin, explorando la historia de FLOSS y examinando cómo Github nos permite construir de manera colaborativa software de código abierto como Bitcoin.

## Criptografía en Bitcoin
![Video](https://youtu.be/4Fw9xS7JlVU)

Adam Gibson guía a los participantes a través de los fundamentos criptográficos de Bitcoin desde una perspectiva matemática. La sesión cubre las funciones criptográficas esenciales que están presentes en Bitcoin, como los hashes y su seguridad, los árboles de Merkle, los protocolos de identidad y firma, los logs discretos y las curvas elípticas.

## Modelo de Gobernanza de Bitcoin

![Video](https://youtu.be/KSpKwTFSOdc)

Peter Todd analiza el modelo de gobernanza de Bitcoin, brindando información sobre cómo se toman las decisiones dentro de la comunidad de Bitcoin y cómo este enfoque descentralizado influye en el desarrollo y la estabilidad del protocolo. En particular, explora cómo diferentes tipos de cambios pueden llevar a bifurcaciones suaves o bifurcaciones duras, cómo difiere la gobernanza entre cambios de política y reglas de consenso, y cuál es el juego político del cambio en Bitcoin.

# Conceptos de la Capa Uno

## Componentes de un Nodo en Bitcoin

![Video](https://youtu.be/jdHc-pbDI9E)

Adam Gibson desglosa los diversos componentes de un nodo de Bitcoin. El capítulo se centra en el papel que desempeña cada componente en el mantenimiento de la funcionalidad e integridad de la red. En particular, se enfoca en por qué deberíamos ejecutar un nodo de Bitcoin, qué hace un nodo de Bitcoin y cómo funcionan los diferentes componentes de un nodo de Bitcoin.

## Estructuras de Datos de Bitcoin

(el video estará disponible pronto)
Alekos Filini presenta un análisis en profundidad de las estructuras de datos de Bitcoin. Esto cubre la organización de los datos dentro de la cadena de bloques y cómo permite la robustez y eficiencia de la red.
## Pila de Software Bitcoin L1

![Video](https://youtu.be/L6FkntRwkOU)

Daniela Brozzoni ofrece una descripción general completa de la pila de software de la Capa 1 de Bitcoin, explicando las capas que componen la base del protocolo de Bitcoin (es decir, nodos de Bitcoin y billeteras de Bitcoin) y cómo construir software de Bitcoin con una introducción a las bibliotecas de Bitcoin y una inmersión profunda en el Kit de Desarrollo de Bitcoin (BDK).

# Lightning Network

## Historia de los Canales de Pago

![Video](https://youtu.be/0ZgE-LjHWvI)

Gabriel Comte ofrece una perspectiva histórica sobre el desarrollo de los canales de pago, que son fundamentales para la Lightning Network. Este capítulo explora la evolución de los canales de pago y su importancia en la escalabilidad de las transacciones de Bitcoin, desde los canales de pago de Satoshi hasta soluciones de canales de pago bidireccionales como Duplex Micropayment Channels o canales de pago de Lightning.

## Historia del Enrutamiento Atómico

![Video](https://youtu.be/RaMeYgSBJQ0)

Gabriel Comte relata la historia del enrutamiento atómico, detallando varias técnicas que han sido la base de la capa de enrutamiento de la red Lightning, como el modelo de concentradores y radios, el modelo Ripple y los contratos con bloqueo de tiempo hash (HTLC). Esta historia ha sido fundamental para permitir transacciones seguras y sin confianza en la Lightning Network.

## Revisión de BOLT

![Video](https://youtu.be/Fy5W_ryWrCY)

asi0 revisa BOLT, la Base de la Tecnología Lightning, explicando las especificaciones que cualquier implementación de Lightning Network debe respetar. Esta será una primera inmersión profunda en las diferentes capas de la Lightning Network.

## Principales Clientes de LN

![Video](https://youtu.be/a0Q_5dzpqKw)

asi0 presenta los principales clientes de la Lightning Network (LN), proporcionando un análisis de sus características y fortalezas basado en una matriz 2x2 que evalúa el nivel de custodia y gestión de liquidez que el usuario tiene con los clientes de LN.

# Los Desafíos de LN

## Desafíos Prácticos para LN

(el video estará disponible pronto)

asi0 aborda los desafíos prácticos que se enfrentan al trabajar con la Lightning Network. Esto incluye una discusión sobre las limitaciones actuales y los esfuerzos en curso para superarlas basados en 4 desafíos principales (gestión de liquidez, abstracción L1/L2, recepción sin conexión y gestión de respaldo) que se exploran desde el punto de vista del usuario y desde el punto de vista del desarrollador.

## Futura Evolución de LN

![Video](https://youtu.be/TIrAMFK6Peg)

Gabriel Comte especula sobre la futura evolución de la Lightning Network, examinando posibles desarrollos, como canales de financiación dual eltoo, BOLT 12, PTLCs, Watchtowers y estándares LSP, y cómo podrían transformar el panorama de las transacciones de Bitcoin.

## Protocolos sobre LN

![Video](https://youtu.be/OLTQLtQyoZE)

Alekos Filini examina los protocolos construidos sobre la Lightning Network, explicando cómo contribuyen a la escalabilidad y funcionalidad de Bitcoin.

# Bonus

## Minería en Bitcoin

![Video](https://youtu.be/22LadAWEMQo)

Ajelex se adentra en el mundo de la minería de Bitcoin, detallando el proceso y su importancia en el contexto de la seguridad de la red y la creación de nuevos bitcoins.

## Joinmarket

![Video](https://youtu.be/VFjccozVwc8)
Adam explora Joinmarket, una implementación de CoinJoin que mejora la privacidad y fungibilidad al permitir a los usuarios crear transacciones de Bitcoin colaborativas, sin confianza y anónimas.
## Protocolos sobre la Red Lightning

![Video](https://youtu.be/OLTQLtQyoZE)

Alekos analiza los diversos protocolos que operan sobre la Red Lightning, mejorando sus capacidades más allá de los simples canales de pago. Este capítulo explora las innovaciones que estos protocolos aportan a la red, cómo interoperan entre sí y su papel en el ecosistema más amplio de Bitcoin, como Keysend, LNURL, Nostr y Lightning LSPs.

# Bonus

## Fundamentos de la Minería de Bitcoin

![Video](https://youtu.be/22LadAWEMQo)

Ajelex se centra en el aspecto empresarial de la minería de Bitcoin, examinando estrategias para mantener la rentabilidad en un mercado competitivo. La discusión incluye un análisis de los costos operativos, medidas de eficiencia y la economía que impulsa la industria minera.

## Comprendiendo Joinmarket

![Video](https://youtu.be/VFjccozVwc8)

Adam Gibson ofrece información sobre Joinmarket, detallando cómo esta implementación de CoinJoin mejora la privacidad y fungibilidad de Bitcoin. Habla sobre cómo Joinmarket facilita transacciones colaborativas, sin confianza y anónimas dentro del ecosistema de Bitcoin. Luego, en una segunda parte, muestra cómo ejecutar Joinmarket en Signet.

## Cubo+ primer año Hackathon

### Grupo 1 Hackathon - El Legado de Satoshi

![Video](https://youtu.be/NiaahH57N1w)

El grupo El Legado de Satoshi presenta su trabajo en la construcción de un comercio electrónico Lightning con Shopify, React JS y Hydrogen, y la pasarela de pago IBEX.

### Grupo 2 Hackathon - Honey Badger

![Video](https://youtu.be/dds0-SV8ltE)

El grupo Honey Badger presenta su solución para un blog con pagos micropagos Lightning integrados utilizando LnBits y Next.js, Node.js y Hydrogen.

### Grupo 3 Hackathon

![Video](https://youtu.be/2YjrrDMGU9c)

El tercer grupo presenta un panel de control de nodo de la Red Lightning a través de una API personalizada, LND, vue.js, node.js y Bootstrap.

### Grupo 4 Hackathon - Satoshi Fellowship

![Video](https://youtu.be/mxLKiHa0mes#)

El grupo de Satoshi Fellowship presenta una aplicación de juegos LN utilizando LnBits y MongoDB, Poetry, Node.js.

### Grupo 5 Hackathon - Lighting Walker

![Video](https://youtu.be/IiY5PmkGNVo)

El grupo Lighting Walker presenta su solución para un servicio de remesas utilizando MySQL, JavaScript y la API de ZDB.

# Reconocimientos y Sigue Profundizando en la Madriguera del Conejo

Nos gustaría reconocer las contribuciones de nuestros educadores:

- Peter Todd
- Adam Gibson
- Alekos Filini
- Daniela Brozzoni
- Ajelex
- asi0
- Gabriel Comte

Su experiencia ha sido invaluable para el éxito de este curso. Este ha sido el primer curso basado en la primera edición de la iniciativa Cubo+, realizado en julio de 2023. Gracias a todos los participantes y educadores por ser parte de este viaje educativo pionero. Marca el comienzo de lo que esperamos sea un largo y fructífero camino en el desarrollo de Bitcoin. Como primera cohorte, su participación ha establecido el estándar para futuras clases.

Continúa explorando, aprendiendo y contribuyendo al ecosistema de Bitcoin. El conocimiento adquirido aquí es solo un punto de partida. Sigue profundizando en la madriguera del conejo y descubrirás un mundo de oportunidades en constante expansión.

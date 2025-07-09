---
name: Filosofía de desarrollo de Bitcoin
goal: Desarrollar una profunda comprensión filosófica de los principios de diseño de Bitcoin.
objectives: 

  - Analizar los compromisos fundamentales y las decisiones arquitectónicas de Bitcoin
  - Aprenda a evaluar los cambios e innovaciones propuestos para el protocolo Bitcoin
  - Sintetizar más de una década de historia del desarrollo de Bitcoin y debates comunitarios
  - Aplicar marcos de pensamiento crítico al evaluar los nuevos PIF


---

# Profundizar en la filosofía del desarrollo de Bitcoin



La filosofía de desarrollo de Bitcoin es un curso para desarrolladores de Bitcoin que ya entienden los conceptos y procesos básicos, como Proof-of-Work, la construcción de bloques y el ciclo de vida de las transacciones, y que desean subir de nivel profundizando en los compromisos y la filosofía de diseño de Bitcoin.

Debería ayudar a los nuevos desarrolladores a asimilar las lecciones más importantes de más de una década de desarrollo y debate público de Bitcoin, al tiempo que les proporciona un contexto útil para evaluar nuevas ideas (¡buenas y malas!).


### ¿Qué esperar?


Como ya se ha dicho, ésta es una guía práctica para desarrolladores de Bitcoin. Sin embargo, Bitcoin es un tema amplio y complejo y no podríamos cubrir todos sus aspectos aquí. Con este curso, esperamos discutir las características necesarias para iniciar su actividad de desarrollo, así como para que pueda seguir explorándolo por su cuenta.


Hay mucha gente implicada en Bitcoin; como algunos tienen opiniones opuestas, aquí puede encontrar recursos que expresan ideas contradictorias. Sin embargo, siempre intentamos ceñirnos al ámbito de los hechos, donde las opiniones no importan.


### ¿Quién ha escrito esto?


Este curso es una adaptación del libro homónimo cuyo autor principal es Kalle Rosenbaum, y Linnéa Rosenbaum colaboró como coautora.

El libro fue encargado y financiado por [Chaincode Labs](https://learning.chaincode.com/), un centro de desarrollo que imparte programas educativos para desarrolladores que quieren aprender sobre el desarrollo de Bitcoin.


+++



# Introducción

<partId>58c48e9b-e285-4dc6-8952-6cc5140b1313</partId>


## Resumen del curso

<chapterId>28b7256b-9cb0-463e-a82d-d732be86c98c</chapterId>


Bienvenido a este curso PHI 301 sobre la filosofía de desarrollo de Bitcoin.


Bitcoin es más que una criptomoneda, encarna una visión filosófica sobre la descentralización, la privacidad, la confianza y la resiliencia. Este curso está diseñado específicamente para desarrolladores ya familiarizados con los fundamentos técnicos de Bitcoin que ahora buscan profundizar su comprensión de los principios que sustentan el diseño y la gobernanza de Bitcoin.


A lo largo de este curso, adquirirás claridad sobre los valores y estrategias esenciales que han guiado la evolución de Bitcoin durante más de una década. Al explorar estos temas en profundidad, desarrollarás la perspectiva crítica necesaria para evaluar y contribuir a futuros desarrollos con confianza.


### Valores centrales de Bitcoin


¿Qué hace única a Bitcoin? Esta sección revela los valores fundamentales en los que se basa el diseño de Bitcoin. Explorarás la **descentralización**, la piedra angular que garantiza que ninguna entidad controle la red; la **desconfianza**, la clave para eliminar la dependencia de terceros; la **privacidad**, esencial tanto para la libertad individual como para la integridad del sistema; y la **Supply infinita**, la garantía codificada de escasez que da forma a la identidad económica de Bitcoin. Dominar estos conceptos le permitirá comprender plenamente los puntos fuertes y débiles de Bitcoin.


### Bitcoin Gobernanza


Navegar por el complejo panorama de la gobernanza de Bitcoin requiere algo más que conocimientos técnicos, exige comprender el enfoque único de Bitcoin respecto al consenso y la toma de decisiones. En esta sección, te adentrarás en los mecanismos y filosofías que subyacen a procesos críticos como las actualizaciones de protocolos, la necesidad del pensamiento contradictorio, la fuerza de la colaboración de código abierto, los continuos retos de la ampliación y las matizadas estrategias necesarias cuando las cosas inevitablemente van mal. Equipado con estos conocimientos, estarás preparado no sólo para participar, sino para dar forma al futuro de Bitcoin de manera eficaz y responsable.


¿Listo para dar el siguiente paso en su viaje hacia la Bitcoin? Comencemos


***N.B.**: Si durante el curso encuentra algún término desconocido relacionado con Bitcoin, consulte el [glosario](https://planb.network/resources/glossary) para encontrar definiciones.*




# Bitcoin Valores centrales

<partId>2d6c683b-54c8-5465-b2ca-4e96a6828834</partId>


## Descentralización

<chapterId>9397c84b-0038-5d0e-88d5-11767ce8182d</chapterId>




Se analiza qué es la descentralización y por qué es esencial para que Bitcoin funcione. Distinguimos entre la

descentralización de los mineros y la de los nodos completos, y discutir qué aportan a la resistencia a la censura, una de las propiedades más centrales de Bitcoin.


A continuación, el debate se centra en la neutralidad (o ausencia de permisos para usuarios, mineros y desarrolladores), que es una propiedad necesaria de cualquier sistema descentralizado. Por último, abordamos cómo Hard puede ser entender un sistema descentralizado como Bitcoin, y presentamos algunos modelos mentales que pueden ayudar a entenderlo.


Un sistema sin ningún punto central de control se denomina *descentralizado*. Bitcoin está diseñado para evitar que haya un punto central de control, o más exactamente un *punto central de censura*.


La descentralización es un medio para lograr la *resistencia a la censura*.


Hay dos aspectos principales de la descentralización en Bitcoin: La descentralización de Miner y la descentralización de Full node.


La descentralización Miner se refiere al hecho de que el procesamiento de las transacciones no es realizado ni coordinado por ninguna entidad central. La descentralización Full node se refiere al hecho de que la validación de los bloques, es decir, los datos que producen los mineros, se realiza en el extremo de la red, en última instancia por sus usuarios, y no por unas pocas autoridades de confianza.


![](assets/decentralization-banner.webp)


### Descentralización de Miner



Hubo intentos de crear monedas digitales antes de Bitcoin, pero la mayoría fracasaron por falta de descentralización de la gobernanza y resistencia a la censura.


La descentralización de Miner en Bitcoin significa que la *ordenación de las transacciones* no es llevada a cabo por una única entidad o conjunto fijo de entidades. Se lleva a cabo colectivamente por todos los actores que quieran participar en ella; este colectivo de mineros es un conjunto dinámico de usuarios. Cualquiera puede unirse a él o abandonarlo cuando lo desee. Esta propiedad hace que Bitcoin sea resistente a la censura.


Si el Bitcoin estuviera centralizado, sería vulnerable a quienes quisieran censurarlo, como los gobiernos. Correría la misma suerte que intentos anteriores de crear dinero digital. En la introducción de [un artículo](https://www.blockstream.com/sidechains.pdf) titulado "Enabling Blockchain Innovations with Pegged Sidechains", los autores explican cómo las primeras versiones del dinero digital no estaban preparadas para un entorno adversario (véase también el capítulo sobre Pensamiento adversario en la siguiente parte).


David Chaum introdujo el efectivo digital como tema de investigación en 1983, en un entorno con un servidor central en el que se confía para evitar Double-spending. Para mitigar el riesgo para la privacidad de las personas de esta parte central de confianza, y para hacer cumplir la fungibilidad, Chaum introdujo la firma ciega, que utilizó para proporcionar un medio criptográfico para evitar la vinculación de las firmas del servidor central (que representan monedas), al tiempo que permitía al servidor central realizar la prevención del doble gasto.

El requisito de un servidor central se convirtió en el talón de Aquiles del efectivo digital[Gri99]. Aunque es posible distribuir este único punto de fallo sustituyendo la firma del servidor central por una firma umbral de varios firmantes, es importante para la auditabilidad que los firmantes sean distintos e identificables. Sin embargo, el sistema sigue siendo vulnerable a los fallos, ya que cada firmante puede fallar, o hacer que falle, uno por uno.


Quedó claro que utilizar un servidor central para ordenar las transacciones no era una opción viable debido al alto riesgo de censura. Incluso si se sustituyera el servidor central por una federación de un conjunto fijo de n servidores, de los cuales al menos m deben aprobar un pedido, seguiría habiendo dificultades. En efecto, el problema se trasladaría a otro en el que los usuarios deben ponerse de acuerdo sobre este conjunto de n servidores, así como sobre la forma de sustituir los servidores maliciosos por otros buenos sin depender de una autoridad central.


Contemplemos lo que podría ocurrir si Bitcoin fuera censurable. El censor podría presionar a los usuarios para que se identificaran, declararan de dónde procede su dinero o qué compran con él antes de permitir que sus transacciones entraran en Blockchain.


Además, la falta de resistencia a la censura permitiría al censor coaccionar a los usuarios para que adoptaran nuevas reglas del sistema. Por ejemplo, podrían imponer un cambio que les permitiera inflar el dinero Supply, enriqueciéndose así. En tal caso, un usuario que verificara los bloqueos tendría tres opciones para manejar las nuevas reglas:



- Adoptar: Aceptar los cambios y adoptarlos en su Full node.
- Rechazar: Rechazar la adopción de los cambios; esto deja al usuario con un sistema que ya no procesa transacciones, ya que los bloqueos del censor son ahora considerados inválidos por el Full node del usuario.
- Mudanza: Designar un nuevo punto central de control; todos los usuarios deben averiguar cómo coordinarse y luego ponerse de acuerdo sobre el nuevo punto central de control.


Si lo consiguen, lo más probable es que los mismos problemas resurjan en algún momento en el futuro, teniendo en cuenta que el sistema sigue siendo tan censurable como antes.


Ninguna de estas opciones es beneficiosa para el usuario.


La resistencia a la censura mediante la descentralización es lo que separa a Bitcoin de otros sistemas monetarios, pero no es algo fácil de conseguir debido al *problema Double-spending*. Este es el problema de asegurarse de que nadie pueda gastar la misma moneda dos veces, una cuestión que mucha gente pensaba que era imposible de resolver de forma descentralizada. Satoshi Nakamoto escribe en su [Bitcoin whitepaper](https://planb.network/Bitcoin.pdf) sobre cómo resolver el problema Double-spending:


> En este trabajo, proponemos una solución al problema Double-spending utilizando un servidor Timestamp distribuido peer-to-peer para generate prueba computacional del orden cronológico de las transacciones.


Aquí utiliza la peculiar expresión "servidor Timestamp distribuido de igual a igual". La palabra clave aquí es *distribuido*, que en este contexto significa que no hay un punto central de control. A continuación, Nakamoto explica cómo Proof-of-Work es la solución.

Sin embargo, nadie lo explica mejor que

[Gregory Maxwell en Reddit](https://www.reddit.com/r/Bitcoin/comments/ddddfl/question_on_the_vulnerability_of_bitcoin/f2g9e7b/), donde responde a alguien que propone limitar la potencia Hash de los mineros para evitar posibles ataques del 51%:


> Un sistema descentralizado como Bitcoin utiliza una elección pública. Pero en un sistema descentralizado no se puede votar sólo por la "gente", porque para ello sería necesario que una parte centralizada autorizara a la gente a votar. En cambio, Bitcoin utiliza un voto de potencia de cálculo porque es posible verificar la potencia de cálculo sin la ayuda de ningún sistema centralizado
tercero.


El post explica cómo la red descentralizada Bitcoin puede llegar a un acuerdo sobre el orden de las transacciones mediante el uso de Proof-of-Work.


Luego concluye diciendo que el ataque del 51% no es especialmente preocupante, comparado con que a la gente no le importe o no entienda las propiedades de descentralización de Bitcoin:


> Un riesgo mucho mayor para la Bitcoin es que el público que la utilice no lo entienda, no le importe y no proteja las propiedades de descentralización que la hacen valiosa frente a las alternativas centralizadas en primer lugar.

La conclusión es importante. Si la gente no protege la descentralización de Bitcoin, que es un sustituto de su resistencia a la censura, Bitcoin podría ser víctima de los poderes centralizadores, hasta que esté tan centralizada que la censura se convierta en una cosa. Entonces, la mayor parte de su propuesta de valor, si no toda, desaparecería. Esto nos lleva a la siguiente sección sobre la descentralización de Full node.


### Full node descentralización



En los párrafos anteriores, hemos hablado principalmente de la descentralización de Miner y de cómo la centralización de los mineros puede permitir la censura. Pero también hay otro aspecto de la descentralización, la *descentralización Full node*.


La importancia de la descentralización de Full node está relacionada con la desconfianza. Supongamos que un usuario deja de gestionar su propia Full node debido, por ejemplo, a un aumento prohibitivo del coste de funcionamiento. En ese caso, tienen que interactuar con la red Bitcoin de alguna otra manera, posiblemente utilizando monederos web o monederos ligeros, lo que requiere un cierto nivel de confianza en los proveedores de estos servicios.


El usuario pasa de aplicar directamente las reglas de consenso de la red a confiar en que otro lo haga. Supongamos ahora que la mayoría de los usuarios delegan la aplicación del consenso en una entidad de confianza. En ese caso, la red puede entrar rápidamente en una espiral de centralización, y las reglas de la red pueden ser modificadas por actores malintencionados que conspiren.


En [a

Artículo de Bitcoin Magazine](https://bitcoinmagazine.com/technical/decentralist-perspective-Bitcoin-might-need-small-blocks-1442090446), Aaron van Wirdum entrevista a los desarrolladores de Bitcoin sobre sus puntos de vista acerca de la descentralización y los riesgos que conlleva aumentar el tamaño máximo de bloque de Bitcoin. Este debate fue un tema de Hot durante la era 2014-2017, cuando mucha gente discutía sobre aumentar el límite de tamaño de bloque para permitir un mayor rendimiento de las transacciones.


Un argumento de peso contra el aumento del tamaño de los bloques es que incrementa el coste de verificación Si el coste de verificación aumenta, empujará a algunos usuarios a dejar de ejecutar sus nodos completos. Esto, a su vez, hará que más personas no puedan utilizar el sistema de forma Trustless.


Pieter Wuille es citado en el artículo, donde explica los riesgos de la centralización de Full node:


> Si muchas empresas gestionan una Full node, significa que hay que convencerlas a todas de que apliquen un conjunto de reglas diferente. En otras palabras: la descentralización de la validación de bloques es lo que da peso a las reglas de consenso.
> Pero si el recuento de Full node bajara mucho, por ejemplo porque todo el mundo utiliza los mismos monederos web, intercambios y SPV o monederos móviles, la regulación podría convertirse en una realidad. Y si las autoridades pueden regular las reglas de consenso, significa que pueden cambiar cualquier cosa que haga Bitcoin Bitcoin. Incluso el límite de 21 millones de Bitcoin.

Ahí lo tienes. Los usuarios de Bitcoin deberían gestionar sus propios nodos completos para disuadir a los reguladores y a las grandes corporaciones de intentar cambiar las reglas del consenso.


### Neutralidad



Bitcoin es neutral, o sin permisos, como a la gente le gusta llamarlo. Esto significa que a Bitcoin le da igual quién seas o para qué lo uses.


Bitcoin es neutral, lo cual es bueno y la única forma de que funcione. Si estuviera controlada por una organización, sería otro tipo de objeto virtual y no me interesaría en absoluto


Mientras sigas las reglas, eres libre de usarlo como quieras, sin pedir permiso a nadie. Esto incluye *Mining*, *transacciones* y *construcción de protocolos y servicios* sobre Bitcoin:



- Si *Mining* fuera un proceso con permisos, necesitaríamos una autoridad central que seleccionara a quién se le permite minar. Lo más probable es que los mineros tuvieran que firmar contratos legales en los que se comprometieran a

censurar las transacciones según los caprichos de la autoridad central, lo que, en primer lugar, contradice el propósito de Mining.



- Si las personas que *transaccionan* en Bitcoin tuvieran que proporcionar información personal, declarar para qué son sus transacciones o demostrar de otro modo que son dignas de realizar transacciones, también necesitaríamos un punto central de autoridad para aprobar usuarios o transacciones. De nuevo, esto llevaría a la censura y la exclusión.



- Si los desarrolladores tuvieran que pedir permiso para *construir protocolos* sobre Bitcoin, sólo se desarrollarían los protocolos permitidos por el comité central de concesión de desarrolladores. Esto, debido a la intervención del gobierno, excluiría inevitablemente todos los protocolos que preserven la privacidad y todos los intentos de mejorar la descentralización.


A todos los niveles, tratar de imponer restricciones sobre quién puede usar Bitcoin para qué perjudicará a Bitcoin hasta el punto de que ya no esté a la altura de su propuesta de valor.


Pieter Wuille https://Bitcoin.stackexchange.com/a/92055/69518[responde a una pregunta sobre Stack Exchange] acerca de cómo se relaciona la Blockchain con las bases de datos normales. Explica cómo se puede lograr la ausencia de permisos mediante el uso de Proof-of-Work en combinación con incentivos económicos.


Y concluye:


> El uso de algoritmos de consenso Trustless como PoW añade algo que ninguna otra construcción te da (participación sin permiso, lo que significa que no hay un grupo determinado de participantes que puedan censurar tus cambios), El uso de algoritmos de consenso Trustless como PoW añade algo no pero tiene un alto coste, y sus supuestos económicos lo hacen prácticamente sólo útil para los sistemas que definen su propia criptomoneda.
> Probablemente sólo haya un lugar en el mundo para uno o unos pocos de estos realmente usados.

Explica que, para lograr la ausencia de permisos, lo más probable es que el sistema necesite su propia moneda, lo que "limitaría los casos de uso a las criptomonedas". Esto se debe a que la participación sin permiso, o Mining, requiere incentivos económicos integrados en el propio sistema.


### Descentralización



Un aspecto convincente de Bitcoin es lo Hard que es comprender que nadie la controla. No hay comités ni ejecutivos en Bitcoin. Gregory Maxwell, de nuevo [en el subreddit Bitcoin](https://www.reddit.com/r/Bitcoin/comments/s82t2n/comment/htdte7w/?utm_source=share&utm_medium=web2x&context=3), compara esto con el idioma inglés de una manera intrigante:


> A mucha gente le cuesta Hard entender los sistemas autónomos, hay muchos en su vida, cosas como la lengua inglesa, pero la gente simplemente los da por sentados y ni siquiera piensa en ellos como sistemas. Están atascados en una forma de pensar centralizada en la que todo lo que consideran una "cosa" tiene una autoridad que lo controla.
>

> Bitcoin no se centra en nada. Varias personas que han adoptado Bitcoin eligieron por su propia voluntad promoverla, y cómo decidan hacerlo es asunto suyo. Las personas obsesionadas con la autoridad pueden ver estas actividades y creer que son alguna operación de la autoridad de Bitcoin, pero no existe tal autoridad.


El funcionamiento descentralizado de Bitcoin se asemeja a la extraordinaria inteligencia colectiva de muchas especies de la naturaleza. La informática Radhika Nagpal habla en una [charla Ted](https://www.ted.com/talks/radhika_nagpal_what_intelligent_machines_can_learn_from_a_school_of_fish) sobre el comportamiento colectivo de los bancos de peces y cómo los científicos intentan imitarlo utilizando robots.


> En segundo lugar, y lo que me sigue pareciendo más extraordinario, es que sabemos que no hay líderes supervisando este banco de peces. En su lugar, este increíble comportamiento de mente colectiva está surgiendo puramente de las interacciones de un pez y otro.
> De algún modo, existen interacciones o reglas de enfrentamiento entre peces vecinos que hacen que todo funcione.

Señala que muchos sistemas, naturales o artificiales, pueden funcionar y funcionan sin líderes, y son poderosos y resistentes. Cada individuo sólo interactúa con su entorno inmediato, pero juntos forman algo tremendo.


![](assets/fishschool.webp)

*Los bancos de peces no tienen líderes*


No importa lo que pienses de Bitcoin, su naturaleza descentralizada hace que sea difícil de controlar. Bitcoin existe, y no hay nada que puedas hacer al respecto. Es algo que hay que estudiar, no debatir.


### Conclusión sobre la descentralización


Distinguimos entre descentralización Full node y descentralización Mining. La descentralización Mining es un medio para lograr la resistencia a la censura, mientras que la descentralización Full node es lo que hace que las reglas de consenso de la red Hard no cambien sin un amplio apoyo entre los usuarios.


La naturaleza descentralizada de Bitcoin permite la neutralidad frente a desarrolladores, usuarios y mineros. Cualquiera es libre de participar sin pedir permiso.


Resulta difícil comprender los sistemas descentralizados, pero hay algunos modelos mentales que pueden ayudar, como el idioma inglés o los bancos de peces.


## Desconfianza

<chapterId>0506ba61-16a3-543c-95fa-3f3e2dd64121</chapterId>



![](assets/trustlessness-banner.webp)


Este capítulo disecciona el concepto de trustlessness, lo que significa desde el punto de vista de la informática y por qué Bitcoin tiene que ser Trustless para mantener su propuesta de valor.

A continuación hablaremos de lo que significa utilizar Bitcoin de forma Trustless, y qué tipo de garantías puede y no puede ofrecerle una Full node.

En la última sección, analizamos la interacción en el mundo real entre Bitcoin y los programas informáticos o usuarios reales, y la necesidad de hacer concesiones entre la comodidad y la falta de confianza para conseguir hacer algo.


La gente suele decir cosas como "Bitcoin es genial porque es Trustless".


¿Qué quieren decir con Trustless? Pieter Wuille explica este término tan utilizado en [Stack Exchange](https://Bitcoin.stackexchange.com/a/45674/69518):


> La confianza de la que hablamos en "Trustless" es un término técnico abstracto. Un sistema distribuido se denomina Trustless cuando no requiere ninguna parte de confianza para funcionar correctamente.

En resumen, la palabra *Trustless* se refiere a una propiedad del protocolo Bitcoin por la que puede funcionar lógicamente sin "ninguna parte de confianza". Esto es diferente de la confianza que inevitablemente tienes que poner en el software o hardware que ejecutas. Este último aspecto de la confianza se tratará más adelante en este capítulo.


En los sistemas centralizados, dependemos de la reputación de un actor central para asegurarnos de que se ocupará de la seguridad o dará marcha atrás en caso de problemas, así como del sistema legal para sancionar cualquier infracción. Estos requisitos de confianza son problemáticos en los sistemas descentralizados seudónimos: no hay posibilidad de recurso, por lo que realmente no puede haber confianza. En la introducción de [el libro blanco de Bitcoin](https://Bitcoin.org/Bitcoin.pdf), Satoshi Nakamoto describe este problema:


> El comercio en Internet ha pasado a depender casi exclusivamente de instituciones financieras que actúan como terceros de confianza para procesar los pagos electrónicos.
> Aunque el sistema funciona suficientemente bien para la mayoría de las transacciones, sigue adoleciendo de las debilidades inherentes al modelo basado en la confianza.  Las transacciones completamente no reversibles no son realmente posibles, ya que las instituciones financieras no pueden evitar mediar en las disputas. El coste de la mediación aumenta los costes de transacción, limitando el tamaño mínimo práctico de la transacción y eliminando la posibilidad de pequeñas transacciones casuales, y hay un coste más amplio en la pérdida de capacidad para realizar pagos no reversibles por servicios no reversibles.
> Ante la posibilidad de un retroceso, se extiende la necesidad de confianza. Los comerciantes deben desconfiar de sus clientes, atosigándoles para obtener más información de la que necesitarían.  Un cierto porcentaje de fraude se acepta como inevitable. Estos costes e incertidumbres de pago pueden evitarse en persona utilizando moneda física, pero no existe ningún mecanismo para realizar pagos a través de un canal de comunicaciones sin una parte de confianza

Parece que no podemos tener un sistema descentralizado basado en la confianza, y por eso la falta de confianza es importante en Bitcoin.


Para utilizar Bitcoin de forma Trustless, tiene que ejecutar un nodo Bitcoin de validación completa. Sólo entonces podrás verificar que los bloques que recibes de otros siguen las reglas del consenso; por ejemplo, que se cumple el calendario de emisión de monedas y que no se produce un doble gasto en la Blockchain. Si no gestiona una Full node, subcontrata la verificación de los bloques de la Bitcoin a otra persona y confía en que le diga la verdad, lo que significa que no está utilizando la Bitcoin de forma fiable.


David Harding ha escrito [un artículo en el sitio web Bitcoin.org](https://Bitcoin.org/en/Bitcoin-core/features/validation) en el que explica cómo el funcionamiento de una Full node -o el uso de la Bitcoin sin confianza- realmente le ayuda:


> La moneda Bitcoin sólo funciona cuando la gente acepta bitcoins en Exchange por otras cosas de valor. Eso significa que son las personas que aceptan bitcoins las que le dan valor y las que deciden cómo debe funcionar Bitcoin.
>

> Cuando aceptas bitcoins, tienes el poder de hacer cumplir las normas de Bitcoin, como impedir la confiscación de los bitcoins de cualquier persona sin acceso a las claves privadas de esa persona.
>

> Por desgracia, muchos usuarios externalizan su poder de aplicación. Esto deja la descentralización de Bitcoin en un estado debilitado en el que un puñado de mineros puede confabularse con un puñado de bancos y servicios gratuitos para cambiar las reglas de Bitcoin para todos aquellos usuarios no verificadores que externalizaron su poder.
>

> A diferencia de otros monederos, Bitcoin Core hace cumplir las reglas, por lo que si los mineros y los bancos cambian las reglas para sus usuarios no verificadores, esos usuarios no podrán pagar a los usuarios de Bitcoin Core con validación completa como tú.


Dice que utilizar una Full node te ayudará a verificar todos los aspectos de la Blockchain sin confiar en nadie más, para asegurarte de que las monedas que recibes de otros son auténticas. Esto está muy bien, pero hay una cosa importante en la que la Full node no puede ayudarte: no puede evitar el doble gasto mediante la reescritura de la cadena:


> Tenga en cuenta que aunque todos los programas, incluido Bitcoin Core, son vulnerables a la reescritura de la cadena, Bitcoin proporciona un mecanismo de defensa: cuantas más confirmaciones tengan sus transacciones, más seguro estará. No se conoce ninguna defensa descentralizada mejor que esa.

Por muy avanzado que sea tu software, sigues teniendo que confiar en que los bloques que contienen tus monedas no se reescribirán. Sin embargo, como señala Harding, puedes esperar una serie de confirmaciones, tras las cuales consideras que la probabilidad de que se reescriba la cadena es lo suficientemente pequeña como para ser aceptable.


Los incentivos para utilizar Bitcoin de forma Trustless se alinean con la necesidad del sistema de descentralización Full node. Cuantas más personas utilicen sus propios nodos completos, mayor será la descentralización de Full node y, por tanto, más fuerte será Bitcoin frente a cambios maliciosos en el protocolo. Pero, por desgracia, como se explica en la sección de descentralización de Full node, los usuarios suelen optar por servicios de confianza como consecuencia del inevitable compromiso entre falta de confianza y comodidad.


La trustlessness de Bitcoin es absolutamente imperativa desde la perspectiva del sistema. En 2018, Matt Corallo, [habló sobre trustlessness](https://btctranscripts.com/baltic-honeybadger/2018/trustlessness-scalability-and-directions-in-security-models/) en la conferencia Baltic Honeybadger en Riga.


![video](https://youtu.be/66ZoGUAnY9s?t=4019)


La esencia de esa charla es que no puedes construir sistemas Trustless sobre un sistema de confianza, pero sí puedes construir sistemas de confianza -por ejemplo, un Wallet de custodia- sobre un sistema Trustless.



![width=50%](assets/trust.webp)


Una Trustless de base Layer permite diversas compensaciones en niveles superiores


Este modelo de seguridad permite al diseñador del sistema seleccionar compromisos

que tengan sentido para ellos sin obligar a los demás a hacer concesiones.


### No confíe, verifique



Bitcoin funciona de forma fiable, pero aún así tienes que confiar en tu software y hardware hasta cierto punto. Esto se debe a que el software o el hardware pueden no estar programados para hacer lo que se indica en la caja. Por ejemplo:



- La CPU podría estar maliciosamente diseñada para detectar operaciones criptográficas de clave privada y filtrar los datos de la clave privada.
- El generador de números aleatorios del sistema operativo podría no ser tan aleatorio como afirma.
- Bitcoin Core podría haber colado código que enviará tus claves privadas a algún mal actor.


Así que, además de ejecutar una Full node, también tienes que asegurarte de que estás ejecutando lo que pretendes. El usuario de Reddit brianddk [escribió un artículo](https://www.reddit.com/r/Bitcoin/comments/smj1ep/bitcoin_v220_and_guix_stronger_defense_against/) sobre los distintos niveles de confianza que puedes elegir a la hora de verificar tu software. En la sección "Trusting the builders", habla de compilaciones reproducibles:


> Las compilaciones reproducibles son una forma de diseñar software para que muchos desarrolladores de la comunidad puedan compilarlo y asegurarse de que el instalador final es idéntico al que producen otros desarrolladores. Con un proyecto muy público y reproducible como Bitcoin, no es necesario confiar plenamente en un único desarrollador. Muchos desarrolladores pueden realizar la compilación y atestiguar que han producido el mismo archivo que el que el constructor original firmó digitalmente.

El artículo define 5 niveles de confianza: confiar en el sitio, en los constructores, en el compilador, en el núcleo y en el hardware.


Para profundizar en el tema de las construcciones reproducibles, Carl Dong [hizo una presentación sobre Guix](https://btctranscripts.com/breaking-Bitcoin/2019/Bitcoin-build-system/) explicando por qué confiar en el sistema operativo, las bibliotecas y los compiladores puede ser problemático, y cómo solucionarlo con un sistema llamado Guix, que es el que utiliza Bitcoin Core en la actualidad.


> Entonces, ¿qué podemos hacer con el hecho de que nuestra cadena de herramientas puede tener un montón de binarios de confianza que pueden ser reproduciblemente maliciosos? Necesitamos ser más que reproducibles. Tenemos que ser arrancables. No podemos tener tantas herramientas binarias que necesitemos descargar y confiar desde servidores externos controlados por otras organizaciones.
>

> Debemos saber cómo se construyen estas herramientas y exactamente cómo podemos pasar por el proceso de construirlas de nuevo, preferiblemente a partir de un conjunto mucho más pequeño de binarios de confianza. Necesitamos minimizar nuestro conjunto de binarios de confianza tanto como sea posible, y tener un camino fácilmente auditable desde esas cadenas de herramientas hasta lo que usamos para construir Bitcoin. Esto nos permite maximizar la verificación y minimizar la confianza. Esto nos permite maximizar la verificación y minimizar la confianza.

Luego explica cómo Guix sólo nos permite confiar en un binario mínimo de 357 bytes que puede verificarse y entenderse completamente si sabes interpretar las instrucciones. Esto es bastante notable: uno verifica que el binario de 357 bytes hace lo que debe, luego lo usa para construir el sistema de construcción completo a partir del código fuente, y termina con un binario Bitcoin Core que debería ser una copia exacta de la construcción de cualquier otro.


Hay un mantra al que se suscriben muchos bitcoiners, que capta bien gran parte de lo anterior:


> No confíes, verifica.

Esto alude a la frase "[confía, pero verifica](https://en.wikipedia.org/wiki/Trust,_but_verify)" que el ex presidente estadounidense Ronald Reagan utilizó en el contexto del desarme nuclear. [Bitcoiners](https://twitter.com/Truthcoin/status/1491415722123153408?s=20&t=ZyROxZxlBppdRpuuzsiF5w) la cambió para destacar el rechazo a la confianza y la importancia de ejecutar un Full node.


Depende de los usuarios decidir hasta qué punto quieren verificar el software que utilizan y los datos de Blockchain que reciben. Como ocurre con tantas otras cosas en Bitcoin, hay un equilibrio entre comodidad y fiabilidad. Casi siempre es más cómodo utilizar un Wallet custodiado que ejecutar Bitcoin Core en su propio hardware. Sin embargo, como el software de Bitcoin está madurando y las interfaces de usuario están mejorando, con el tiempo debería mejorar el apoyo a los usuarios dispuestos a trabajar hacia la confianza. Además, a medida que los usuarios adquieran más conocimientos con el tiempo, deberían ser capaces de eliminar gradualmente la confianza de la ecuación.


Algunos usuarios piensan de forma adversaria y verifican la mayoría de los aspectos del software que ejecutan. Como consecuencia, reducen la necesidad de confianza al mínimo, ya que sólo necesitan confiar en el hardware y el sistema operativo de su ordenador. Al hacerlo, también ayudan a las personas que no verifican su hardware tan a fondo alzando la voz en público para advertir de cualquier problema que puedan encontrar. Un buen ejemplo de esto es un [suceso que ocurrió en 2018](https://bitcoincore.org/en/2018/09/20/notice/), cuando alguien descubrió un error que permitiría a los mineros gastar una salida dos veces en la misma transacción:


> CVE-2018-17144, cuya corrección se publicó el 18 de septiembre en las versiones 0.16.3 y 0.17.0rc4 de Bitcoin Core, incluye tanto un componente de denegación de servicio como una vulnerabilidad de inflación crítica. Originalmente se informó a varios desarrolladores que trabajan en Bitcoin Core, así como en proyectos que soportan otras criptomonedas, incluyendo ABC y Unlimited el 17 de septiembre como un error de denegación de servicio solamente, sin embargo, rápidamente determinamos que el problema también era una vulnerabilidad de inflación con la misma causa raíz y solución.

En este caso, una persona anónima informó de un problema que resultó ser mucho peor de lo que el informador se imaginaba. Esto pone de relieve el hecho de que las personas que verifican el código a menudo informan de los fallos de seguridad en lugar de explotarlos. Esto beneficia a quienes no pueden verificar todo por sí mismos.


Sin embargo, los usuarios no deben confiar en que otros los mantengan a salvo, sino verificar por sí mismos siempre y cuando puedan; así es como uno se mantiene lo más soberano posible, y como prospera la Bitcoin. Cuantos más ojos haya sobre el software, menos probabilidades habrá de que se cuelen códigos maliciosos y fallos de seguridad.


### Conclusión sobre la desconfianza



El protocolo Bitcoin es Trustless porque permite a los usuarios interactuar con él sin confiar en terceros. En la práctica, sin embargo, la mayoría de la gente no es capaz de verificar toda la pila de software y hardware en la que se ejecuta Bitcoin. Las personas cualificadas que verifican el software o el hardware son capaces de advertir a otras personas menos cualificadas cuando encuentran código malicioso o errores.


Sin confianza, no podemos tener descentralización, porque la confianza implica inevitablemente algún punto central de autoridad. Se puede construir un sistema de confianza sobre un sistema Trustless, pero no se puede construir un sistema Trustless sobre un sistema de confianza.


## Privacidad

<chapterId>1b960afe-0008-589b-b2f4-007d60d264c6</chapterId>



![](assets/privacy-banner.webp)


Este capítulo trata de cómo mantener en secreto tu información financiera privada. Explica qué significa privacidad en el contexto de Bitcoin, por qué es importante y qué significa decir que Bitcoin es pseudónimo. También analiza cómo pueden filtrarse datos privados, tanto de On-Chain como de off-chain.


A continuación, habla del hecho de que los bitcoins deben ser fungibles, es decir, intercambiables por cualquier otro bitcoin, y de cómo la fungibilidad y la privacidad van de la mano. Por último, el capítulo presenta algunas medidas que puedes tomar para mejorar tu privacidad y la de los demás.


Bitcoin puede describirse como un sistema seudónimo, en el que los usuarios tienen múltiples seudónimos en forma de claves públicas. A primera vista, parece una forma bastante buena de proteger a los usuarios de ser identificados, pero en realidad es muy fácil filtrar información financiera privada de forma no intencionada.


### ¿Qué significa privacidad?



La privacidad puede significar cosas distintas en contextos diferentes. En Bitcoin, generalmente significa que los usuarios no tienen que revelar su información financiera a otros, a menos que lo hagan voluntariamente.


Hay muchas formas de filtrar tu información privada a otras personas, con o sin saberlo. Los datos pueden filtrarse desde la Blockchain pública o por otros medios, por ejemplo cuando agentes malintencionados interceptan tus comunicaciones por internet.


### ¿Por qué es importante la privacidad?


Puede parecer obvio por qué la privacidad es importante en Bitcoin, pero hay algunos aspectos en los que uno puede no pensar inmediatamente. [En el foro Bitcoin Talk](https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908), Gregory Maxwell nos explica un montón de buenas razones por las que cree que la privacidad es importante. Entre ellas están el libre mercado, la seguridad y la dignidad humana:


> La privacidad financiera es un criterio esencial para el funcionamiento eficaz de un mercado libre: si usted dirige una empresa, no puede fijar eficazmente los precios si sus proveedores y clientes pueden ver todas sus transacciones en contra de su voluntad.
> No puedes competir eficazmente si tu competencia está rastreando tus ventas.  Individualmente, si no tienes privacidad sobre tus cuentas, pierdes influencia informativa en tus transacciones privadas: si pagas a tu casero en Bitcoin sin tener suficiente privacidad, tu casero verá cuándo has recibido un aumento de sueldo y podrá pedirte más alquiler.
>

> La privacidad financiera es esencial para la seguridad personal: si los ladrones pueden ver sus gastos, ingresos y posesiones, pueden utilizar esa información para atacarle y explotarle. Sin privacidad, los malintencionados tienen más capacidad para robar su identidad, arrebatarle grandes compras en la puerta de su casa o hacerse pasar por empresas con las que realiza transacciones hacia usted... pueden saber exactamente por cuánto intentar estafarle.
>

> La privacidad financiera es esencial para la dignidad humana: nadie quiere que el mocoso camarero de la cafetería o sus entrometidos vecinos hagan comentarios sobre sus ingresos o hábitos de gasto. Nadie quiere que su familia política, loca por los bebés, le pregunte por qué compra anticonceptivos (o juguetes sexuales). Su empleador no tiene por qué saber a qué iglesia dona. Sólo en un mundo libre de discriminación y perfectamente ilustrado, donde nadie tenga una autoridad indebida sobre los demás, podríamos conservar nuestra dignidad y realizar libremente nuestras transacciones legales sin autocensurarnos si no tenemos privacidad.

Maxwell también aborda la fungibilidad, que se tratará más adelante en este capítulo, así como el hecho de que la privacidad y la aplicación de la ley no son contradictorias.


### Pseudonimato


Antes hemos mencionado que Bitcoin es seudónima, y que los seudónimos son claves públicas. En los medios de comunicación se oye a menudo que Bitcoin es anónima, lo cual no es correcto. Hay una distinción entre anonimato y seudonimato.


Andrew Poelstra [explica en un post de Bitcoin Stack Exchange](https://Bitcoin.stackexchange.com/a/29473/69518) cómo sería el anonimato en las transacciones:


> El anonimato total, en el sentido de que cuando gastas dinero no hay rastro de dónde viene o adónde va, es teóricamente posible utilizando la técnica criptográfica de las pruebas de conocimiento cero.

La diferencia parece ser que en una forma seudónima de dinero se pueden rastrear los pagos entre seudónimos, mientras que en una forma anónima de dinero no se puede. Dado que los pagos de Bitcoin se pueden rastrear entre seudónimos, no es un sistema anónimo.


También hemos dicho que los seudónimos son claves públicas, pero en realidad son direcciones derivadas de claves públicas. ¿Por qué usamos direcciones como seudónimos y no otra cosa, por ejemplo algunos nombres descriptivos, como "watchme1984"? Esto ha sido [bien explicado](https://Bitcoin.stackexchange.com/a/25175/69518) por el usuario Tim S., también en Bitcoin Stack Exchange:


> Para que la idea de Bitcoin funcione, debes tener monedas que sólo pueda gastar el propietario de una determinada clave privada. Esto significa que lo que envíes debe estar vinculado, de algún modo, a una clave pública.
>

> Usar seudónimos arbitrarios (por ejemplo, nombres de usuario) significaría que tendrías que vincular de algún modo el seudónimo a una clave pública para permitir la criptografía de clave pública/privada. Esto eliminaría la posibilidad de crear direcciones/pseudónimos offline de forma segura (por ejemplo, antes de que alguien pudiera enviar dinero al nombre de usuario "tdumidu", tendrías que anunciar en la Blockchain que "tdumidu" es propiedad de la clave pública "a1c...", e incluir una tarifa para que otros tuvieran una razón para anunciarlo), reduciría el anonimato (al animarte a reutilizar pseudónimos), y aumentaría innecesariamente el tamaño de la Blockchain. También crearía una falsa sensación de seguridad de que estás enviando a quien crees que eres (si tomo el nombre de "Linus Torvalds" antes que él, entonces es mío y la gente podría enviar dinero pensando que están pagando al creador de Linux, no a mí).

Al utilizar direcciones, o claves públicas, conseguimos objetivos importantes, como eliminar la necesidad de registrar de algún modo un seudónimo de antemano, reducir los incentivos para la reutilización de seudónimos, evitar la hinchazón Blockchain y dificultar la suplantación de otras personas.


### Blockchain privacidad



La privacidad de Blockchain se refiere a la información que usted revela al realizar transacciones en Blockchain. Se aplica a todas las transacciones, tanto las que envía como las que recibe. Se aplica a todas las transacciones, tanto las que envías como las que recibes.


Satoshi Nakamoto reflexiona sobre la privacidad de On-Chain en la sección 7 de su [Bitcoin whitepaper](https://Bitcoin.org/Bitcoin.pdf):


> Como cortafuegos adicional, se debe utilizar un nuevo par de claves para cada transacción para evitar que se vinculen a un propietario común. No obstante, es inevitable que se produzcan algunos vínculos en las transacciones con varias entradas, que revelan necesariamente que sus entradas pertenecían al mismo propietario. El riesgo es que si se revela el propietario de una clave, la vinculación podría revelar otras transacciones que pertenecían al mismo propietario.

El documento resume los principales problemas de la privacidad de Blockchain, a saber, la reutilización de Address y la agrupación de Address. El primero se explica por sí mismo, el segundo se refiere a la capacidad de decidir, con cierto nivel de certeza, que un conjunto de direcciones diferentes pertenece al mismo usuario.


![](assets/address-reuse-clustering.webp)


Fugas de privacidad típicas en la Blockchain


Chris Belcher [escribió con gran detalle](https://en.Bitcoin.it/Privacy#Blockchain_attacks_on_privacy) sobre los diferentes tipos de filtraciones de privacidad que pueden ocurrir en la Bitcoin Blockchain. Te recomendamos que leas al menos las primeras subsecciones bajo "Ataques a la privacidad en la Blockchain"


La conclusión es que la privacidad en Bitcoin no es perfecta. Requiere una cantidad significativa de trabajo para realizar transacciones privadas. La mayoría de la gente no está dispuesta a ir tan lejos por la privacidad. Parece haber un claro equilibrio entre privacidad y facilidad de uso.


Otro aspecto importante de la privacidad es que las medidas que tomas para proteger tu propia privacidad afectan también a otros usuarios. Si eres descuidado con tu propia privacidad, otras personas también pueden ver reducida su privacidad. Gregory Maxwell lo explica muy claramente en el mismo debate de Bitcoin Talk [que enlazamos anteriormente](https://bitcointalk.org/index.php?topic=334316.msg3589252#msg3589252), y concluye con un ejemplo:


> Esto también funciona en la práctica... Un buen hacker de sombrero blanco en IRC estaba jugando con el cracking de brainwallet y dio con una frase con ~250 BTC en ella.  Fuimos capaces de identificar al propietario sólo con el Address, porque había sido pagado por un servicio de Bitcoin que reutilizaba direcciones y él fue capaz de hablar con ellos para que le dieran la información de contacto del usuario. Consiguió hablar por teléfono con el usuario, que estaba sorprendido y confuso, pero agradecido por no haber perdido su dinero.  Un final feliz. (No es el único ejemplo, ni mucho menos, pero es uno de los más divertidos).

En este caso, todo salió bien gracias al hacker de mentalidad filantrópica, pero no cuentes con eso la próxima vez.


### Privacidad no Blockchain


Aunque la Blockchain ha demostrado ser una fuente notoria de filtraciones de privacidad, hay muchas otras filtraciones que no utilizan la Blockchain, algunas más furtivas que otras. Estas van desde key-loggers hasta análisis de tráfico de red. Para conocer algunos de estos métodos, consulte de nuevo [el artículo de Chris Belcher](https://en.Bitcoin.it/Privacy#Non-blockchain_attacks_on_privacy), concretamente la sección "Non-Blockchain attacks on privacy".


Entre una plétora de ataques, Belcher menciona la posibilidad de que alguien husmee en su conexión a Internet, por ejemplo, su ISP:


> Si el adversario ve salir de tu nodo una transacción o un bloque que no había entrado anteriormente, entonces puede saber con casi total certeza que la transacción la hiciste tú o que el bloque fue minado por ti. Como se trata de conexiones a Internet, el adversario podrá vincular la IP Address con la información Bitcoin descubierta.

Sin embargo, entre las fugas de privacidad más evidentes se encuentran las bolsas. Debido a las leyes, normalmente denominadas KYC (Know Your Customer) y AML (Anti-Money Laundering), que son válidas en las jurisdicciones en las que operan, los intercambios y las empresas relacionadas a menudo tienen que recopilar datos personales sobre sus usuarios, creando grandes bases de datos sobre qué usuarios poseen qué bitcoins. Estas bases de datos son grandes "honeypots" para gobiernos malvados y criminales que siempre están a la caza de nuevas víctimas. Existen mercados reales para este tipo de datos, donde los hackers

vender datos al mejor postor.


Para empeorar las cosas, las empresas que gestionan estas bases de datos suelen tener poca experiencia en la protección de datos financieros, de hecho muchas de ellas son jóvenes empresas de nueva creación, y sabemos de buena tinta que ya se han producido varias filtraciones. Algunos ejemplos

[MobiQwik](https://bitcoinmagazine.com/business/probably-the-largest-kyc-data-leak-in-history-demonstrates-the-importance-of-Bitcoin-privacy) y [HubSpot](https://bitcoinmagazine.com/business/hubspot-security-breach-leaks-Bitcoin-users-data).


De nuevo, proteger los datos contra esta amplia gama de ataques es Hard, y es probable que no puedas hacerlo completamente. Tendrás que optar por el compromiso entre comodidad y privacidad que más te convenga.


### Fungibilidad


La fungibilidad, en el contexto de las monedas, significa que una moneda es intercambiable por cualquier otra moneda de la misma divisa. Esta graciosa

ya se ha mencionado brevemente en este capítulo.


En el artículo allí comentado, Gregory Maxwell [afirmaba](https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908):


> La privacidad financiera es un elemento esencial para la fungibilidad en Bitcoin: si puedes distinguir significativamente una moneda de otra, entonces su fungibilidad es débil. Si nuestra fungibilidad es demasiado débil en la práctica, entonces no podemos ser descentralizados: si alguien importante anuncia una lista de monedas robadas de las que no aceptará monedas derivadas, debes comprobar cuidadosamente las monedas que aceptas con esa lista y devolver las que fallen.  Todo el mundo se queda atascado comprobando listas negras emitidas por diversas autoridades porque en ese mundo a todos no nos gustaría quedarnos atascados con monedas malas. Esto añade fricción y costes transaccionales y hace que la Bitcoin sea menos valiosa como moneda.

Aquí habla de los peligros derivados de la falta de fungibilidad. Supongamos que tenemos una UTXO. La historia de esa UTXO puede rastrearse normalmente varios saltos atrás, extendiéndose a multitud de salidas anteriores. Si alguna de esas salidas estuvo implicada en alguna actividad ilegal, no deseada o sospechosa, algunos posibles receptores de su moneda podrían rechazarla. Si crees que los receptores de tus pagos verificarán tus monedas con algún servicio centralizado de listas blancas o negras, puede que tú también empieces a comprobar las monedas que recibes, sólo para estar seguro. El resultado es que una mala fungibilidad reforzará una fungibilidad aún peor.


Adam Back y Matt Corallo [hicieron una presentación sobre fungibilidad](https://btctranscripts.com/scalingbitcoin/milan-2016/fungibility-overview/) en Scaling Bitcoin en Milán en 2016. Estaban pensando en lo mismo:


> Se necesita fungibilidad para que Bitcoin funcione. Si recibes monedas y no puedes gastarlas, entonces empiezas a dudar de si puedes gastarlas. Si hay dudas sobre las monedas que recibes, entonces la gente va a ir a los servicios de taint y comprobar si "estas monedas están bendecidas" y entonces la gente se va a negar a comerciar. Esto hace que Bitcoin pase de ser un sistema descentralizado sin permisos a un sistema centralizado con permisos en el que los proveedores de la lista negra te dan un "pagaré".

Parece que la privacidad y la fungibilidad van de la mano. La fungibilidad se debilitará si la privacidad es débil, por ejemplo, ya que las monedas de personas no deseadas pueden entrar en una lista negra. Del mismo modo, la privacidad se debilitará si la fungibilidad es débil: si hay una lista negra, tendrás que preguntar a los proveedores de la lista negra sobre qué monedas aceptar, con lo que posiblemente reveles tu IP Address, correo electrónico Address y otra información sensible. Estas dos características están tan entrelazadas que es Hard hablar de cualquiera de ellas de forma aislada.


### Medidas de protección de la intimidad



Se han desarrollado varias técnicas para ayudar a las personas a protegerse de las filtraciones de privacidad. Entre las más obvias se encuentra, como ya ha señalado Nakamoto, el uso de un único

para cada transacción, pero existen varios más. No vamos a enseñarte a convertirte en un ninja de la privacidad. Sin embargo, Bitcoin Q+A tiene un [resumen rápido de las tecnologías que mejoran la privacidad](https://bitcoiner.guide/privacytips/), ordenadas de alguna manera por cómo Hard son de implementar. Cuando lo leas, te darás cuenta de que la privacidad de Bitcoin a menudo tiene que ver con cosas ajenas a Bitcoin. Por ejemplo, no deberías alardear de tus bitcoins, y deberías usar Tor y VPN.


El post también enumera algunas medidas directamente relacionadas con Bitcoin:


- Full node: Si no utilizas tu propia Full node, filtrarás mucha información sobre tu Wallet a servidores en Internet. Ejecutar una Full node es un gran primer paso.
- Lightning Network: Existen varios protocolos sobre Bitcoin, por ejemplo Lightning Network y Liquid de Blockstream Sidechain.
- CoinJoin: Una forma de que varias personas fusionen sus transacciones en una sola, lo que dificulta el análisis de la cadena.


En [una charla](https://btctranscripts.com/breaking-Bitcoin/2019/breaking-Bitcoin-privacy/) en la conferencia Breaking Bitcoin, Chris Belcher dio un interesante ejemplo práctico de cómo se ha mejorado la privacidad:


> Eran un casino Bitcoin. El juego online no está permitido en EEUU. Cualquier cliente de Coinbase que depositó directamente a Bustabit tendría sus cuentas cerradas porque Coinbase estaba monitoreando para esto. Bustabit hizo algunas cosas. Hicieron algo llamado evasión de cambio donde vas a través de- y ves si puedes construir una transacción que no tenga salida de cambio. Esto ahorra Miner honorarios y también dificulta el análisis.
>

> Además, importaron sus direcciones de depósito reutilizadas en joinmarket. En este punto, los clientes de coinbase.com nunca fueron baneados. Parece que el servicio de vigilancia de Coinbase fue incapaz de hacer el análisis después de esto, por lo que es posible romper estos algoritmos.

También mencionó este ejemplo, entre otros, en la [Página de privacidad](https://en.Bitcoin.it/Privacy) de la wiki Bitcoin.


Obsérvese cómo se puede conseguir una mayor privacidad construyendo sistemas sobre Bitcoin, como es el caso de Lightning Network:


![image](assets/privacy.webp)


Las capas sobre la Bitcoin pueden añadir privacidad


En el último chaperón señalamos que la necesidad de confianza sólo puede aumentar con capas por encima, pero no parece ser el caso de la privacidad, que puede mejorar o empeorar arbitrariamente en capas por encima. ¿Por qué? Cualquier Layer encima de Bitcoin, como se explica en el párrafo Escalado por capas del futuro capítulo Escalado, debe utilizar transacciones On-Chain ocasionalmente, de lo contrario no estaría "encima de Bitcoin". Las capas que mejoran la privacidad generalmente intentan utilizar la Layer base lo menos posible para minimizar la cantidad de información revelada.


Las anteriores son formas algo técnicas de mejorar su privacidad. Pero hay otras maneras. Al principio de este capítulo dijimos que Bitcoin es un sistema seudónimo. Esto significa que los usuarios de Bitcoin no son conocidos por sus nombres reales u otros datos personales, sino por sus claves públicas. Una clave pública es un seudónimo de un usuario, y un usuario puede tener varios seudónimos. En un mundo ideal, tu identidad en persona está disociada de tus seudónimos de Bitcoin. Desgraciadamente, debido a los problemas de privacidad descritos en este capítulo, esta disociación suele degradarse con el tiempo.


Para mitigar los riesgos de que se revelen tus datos personales, lo primero es no darlos ni entregarlos a servicios centralizados, que construyen grandes bases de datos que pueden filtrarse. Un artículo de Bitcoin Q+A [explica el KYC](https://bitcoiner.guide/nokyconly/) y los peligros que de él se derivan. También sugiere algunas medidas que puedes tomar para mejorar tu situación:


> Afortunadamente, existen algunas opciones para comprar Bitcoin a través de fuentes sin KYC. Estos son todos P2P (peer to peer) intercambios donde se está negociando directamente con otra persona y no un tercero centralizado. Lamentablemente, algunos venden otras monedas además de Bitcoin, por lo que le recomendamos que tenga cuidado.

El artículo sugiere evitar el uso de intercambios que requieran KYC/AML y en su lugar operar en privado, o utilizar intercambios descentralizados como [bisq](https://bisq.network/).


https://planb.network/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04

Para profundizar en las contramedidas, consulte el [artículo wiki sobre privacidad] antes mencionado (https://en.Bitcoin.it/wiki/Privacy#Methods_for_improving_privacy_.28non-Blockchain.29), empezando por "Métodos para mejorar la privacidad (no Blockchain)".


### Conclusión sobre la privacidad



La privacidad es muy importante, pero Hard para conseguirla. No existe una solución milagrosa.


Para conseguir una privacidad decente en Bitcoin, hay que tomar medidas activas, algunas de las cuales son costosas y requieren mucho tiempo.


## Finito Supply

<chapterId>af125ba2-ef98-5905-8895-41a538fe5ea5</chapterId>



![](assets/finitesupply-banner.webp)


Este capítulo analiza el límite de 21 millones de BTC de Bitcoin Supply, o ¿cuánto es en realidad? Hablamos de cómo se aplica este límite y qué se puede hacer para verificar que se respeta. Además, echamos un vistazo a la bola de cristal y analizamos la dinámica que entrará en juego cuando la Block reward pase de estar basada en subvenciones a estar basada en comisiones.


El conocido Supply finito de 21 millones de BTC se considera una propiedad fundamental del Bitcoin. Pero, ¿está realmente grabada en piedra?


Empecemos por ver qué dicen las reglas de consenso actuales sobre el Supply del Bitcoin, y cuánto de él será realmente utilizable. Pieter Wuille escribió un artículo sobre esto [en Stack Exchange](https://Bitcoin.stackexchange.com/a/38998/69518), en el que contaba cuántos bitcoins habría una vez minadas todas las monedas:


> Si se suman todas estas cifras, se obtiene 20999999.9769 BTC.

Pero debido a una serie de razones -como los problemas iniciales con las transacciones de Coinbase, los mineros que involuntariamente reclaman menos de lo permitido y la pérdida de claves privadas- ese límite superior nunca se alcanzará. Wuille concluye:


> Esto nos deja con 20999817.31308491 BTC (teniendo en cuenta todo hasta el bloque 528333)

Sin embargo, varias carteras se han perdido o han sido robadas, se han enviado transacciones a la Address equivocada, la gente ha olvidado que poseía la Bitcoin. El total puede ascender a millones. La gente ha intentado hacer un recuento de las pérdidas conocidas [aquí](https://bitcointalk.org/index.php?topic=7253.0).


Esto nos deja con: ??? BTC.


Por lo tanto, podemos estar seguros de que la Bitcoin Supply será 20999817.31308491 BTC como máximo. Cualquier moneda perdida o quemada de forma no verificable hará que esta cifra sea menor, pero no sabemos en cuánto. Lo interesante es que en realidad no importa, o mejor dicho, importa de forma positiva para los poseedores de Bitcoin,

[como se explica](https://bitcointalk.org/index.php?topic=198.msg1647#msg1647) por Satoshi Nakamoto:


> Las monedas perdidas sólo hacen que las de los demás valgan un poco más.  Considéralo una donación para todos.

La Supply finita se reducirá y esto debería, al menos en teoría, provocar una deflación de los precios.


Más importante que el número exacto de monedas en circulación es la forma en que se aplica el límite Supply sin ninguna autoridad central. Alias chytrik lo explica muy bien en [Stack Exchange](https://Bitcoin.stackexchange.com/a/106830/69518):


> Así que la respuesta es que no tienes que confiar en que alguien no haya aumentado la Supply. Sólo tienes que ejecutar algún código que verifique que no lo han hecho.

Incluso si algunos nodos completos se pasan al lado oscuro y deciden aceptar bloques con transacciones coinbase de mayor valor, todos los nodos completos restantes simplemente los desatenderán y seguirán haciendo negocios como de costumbre. Algunos nodos completos pueden, intencionadamente o no, ejecutar softwares malignos, pero el colectivo asegurará sólidamente la Blockchain. En conclusión, puedes elegir confiar en el sistema sin tener que confiar en nadie.


### Subvención en bloque y gastos de transacción



Una Block reward se compone de la subvención por bloque más las comisiones por transacción. La Block reward tiene que cubrir los costes de seguridad de la Bitcoin. Podemos afirmar con seguridad que, en las condiciones actuales en lo que respecta a la subvención por bloque, las comisiones por transacción, el precio del Bitcoin, el tamaño del Mempool, la potencia del Hash, el grado de descentralización, etc., los incentivos para que todos los jugadores respeten las reglas son lo suficientemente altos como para preservar un sistema monetario seguro.


¿Qué ocurre cuando la subvención en bloque se aproxima a cero? Para simplificar, supongamos que es igual a cero. Llegados a este punto, el coste de seguridad del sistema se cubre únicamente mediante las comisiones por transacción. No podemos saber qué nos deparará el futuro cuando esto ocurra. Los factores de incertidumbre son numerosos y no nos queda más remedio que especular. Por ejemplo, la contribución de Paul Sztorc al tema [en su blog Truthcoin](https://www.truthcoin.info/blog/security-budget/) es en su mayor parte especulaciones, pero tiene al menos un punto sólido (por favor, ten en cuenta que M2, tal y como lo menciona Sztorc, es una medida de un Supply de dinero fiduciario):


> Mientras que los dos se mezclan en el mismo "presupuesto de seguridad", la subvención en bloque y las tasas txn son total y completamente diferentes. Son tan diferentes entre sí, como "los beneficios totales de VISA en 2017" lo son del "incremento total de M2 en 2017".

Hoy son los tenedores quienes pagan por la seguridad (vía inflación monetaria). Mañana les tocará a los derrochadores asumir de algún modo esta carga, como se ilustra a continuación.


![image](assets/finitesupply.webp)


A medida que pase el tiempo, los costes de seguridad pasarán de los poseedores a los gastadores


Cuando las comisiones por transacción son la principal motivación para la Mining, los incentivos cambian. En particular, si la Mempool de una Miner no contiene suficientes comisiones por transacción, puede resultar más rentable para esa Miner reescribir la historia de la Bitcoin en lugar de ampliarla. Bitcoin Optech tiene una [sección sobre este comportamiento](https://bitcoinops.org/en/topics/fee-sniping/) específica, llamada *fee sniping*, escrita por David Harding:


> El recorte de comisiones es un problema que puede surgir a medida que la subvención de Bitcoin siga disminuyendo y las comisiones por transacción empiecen a dominar las recompensas por bloque de Bitcoin. Si las comisiones por transacción son lo único que importa, entonces un Miner con un `x` por ciento de la tasa de Hash tiene un `x` por ciento de posibilidades de Mining el siguiente bloque, por lo que el valor esperado para ellos de Mining honestamente es el `x` por ciento del [mejor conjunto feerado de transacciones](https://bitcoinops.org/en/newsletters/2021/06/02/#candidate-set-based-csb-block-template-construction) en su Mempool.
>

> Alternativamente, un Miner podría intentar deshonestamente volver a minar el bloque anterior más un bloque completamente nuevo para extender la cadena. Este comportamiento se conoce como "fee sniping", y la probabilidad de que el Miner deshonesto lo consiga si todos los demás Miner son honestos es `(x/(1-x))^2`. Aunque el "fee sniping" tiene en general una probabilidad de éxito menor que el Mining honesto, intentar el Mining deshonesto podría ser la opción más rentable si las transacciones del bloque anterior pagaron comisiones significativamente más altas que las transacciones actuales en el Mempool: una pequeña oportunidad para una gran cantidad puede valer más que una gran oportunidad para una pequeña cantidad.

El hecho de que si los mineros empiezan a practicar el francotirador de tarifas, incentivará a otros a hacer lo mismo, reduciendo aún más el número de mineros honrados. Esto podría afectar gravemente a la seguridad general de Bitcoin. Harding pasa a enumerar algunas contramedidas que pueden tomarse, como confiar en los bloqueos de tiempo de transacción para restringir en qué parte del Blockchain puede aparecer la transacción.


Así pues, dado que se mantiene el consenso sobre la Supply finita, la subvención por bloque -gracias a [BIP42](https://github.com/Bitcoin/bips/blob/master/bip-0042.mediawiki) que corrigió un error de inflación a muy largo plazo- llegará a cero en torno al año 2140. ¿Serán suficientes las comisiones por transacción para asegurar la red?


Es imposible decirlo, pero sabemos algunas cosas:


- Un siglo es *mucho* tiempo desde la perspectiva de Bitcoin. Si sigue existiendo, probablemente habrá evolucionado enormemente.
- Si una abrumadora mayoría económica considera necesario cambiar las reglas e introducir, por ejemplo, una inflación monetaria anual perpetua del 0,1% o del 1%, el Supply del Bitcoin dejará de ser finito.
- Con una subvención por bloque nula y una Mempool vacía o casi vacía, las cosas pueden tambalearse debido al tijeretazo de las tasas.


Dado que la transición a una Block reward de pago está tan lejos en el futuro, quizá sea prudente no sacar conclusiones precipitadas e intentar solucionar los posibles problemas mientras podamos. Por ejemplo, Peter Todd cree que existe un riesgo real de que el presupuesto de seguridad de Bitcoin no sea suficiente en el futuro y, en consecuencia, aboga por una pequeña inflación perpetua en Bitcoin. Sin embargo, también piensa que no es una buena idea discutir tal cuestión en este momento, como [dijo en el podcast What Bitcoin Did](https://www.whatbitcoindid.com/podcast/peter-todd-on-the-essence-of-Bitcoin):


> Pero, eso es un riesgo como 10, 20 años en el futuro. Eso es mucho tiempo. Y, para entonces, ¿quién diablos sabe cuáles son los riesgos?

Quizá podríamos pensar en el Bitcoin como algo orgánico. Imagine una pequeña planta de roble que crece lentamente. Imagina también que nunca has visto un árbol completamente crecido en tu vida. ¿No sería prudente entonces refrenar sus problemas de control en lugar de establecer de antemano todas las reglas sobre cómo se debe permitir que esta planta evolucione y crezca?


### Conclusión sobre Finite Supply



Si el Bitcoin Supply crecerá más allá de los 21 millones no podemos decirlo hoy, y eso probablemente no sea tan malo. Garantizar que el presupuesto de seguridad siga siendo suficientemente alto es crucial, pero no urgente. Tengamos esta discusión dentro de 10-50 años, cuando sepamos más. Si es que sigue siendo relevante.


# Bitcoin Gobierno

<partId>411bf53f-af4b-50f1-b71b-e40fe3ff64b7</partId>


## Actualización de

<chapterId>3ffa84d1-adfa-5fbc-9b13-384ea783fcdd</chapterId>



![](assets/upgrading-banner.webp)


Actualizar la Bitcoin de forma segura puede ser extremadamente difícil. Algunos cambios tardan varios años en llevarse a cabo. En este capítulo, conoceremos el vocabulario común en torno a la actualización de Bitcoin y exploraremos algunos ejemplos de actualizaciones históricas de su protocolo, así como los conocimientos que hemos obtenido de ellas. Por último, hablaremos de las escisiones en cadena y de los riesgos y costes que conllevan.


Para ponerse a tono para este capítulo, debería leer [el artículo de David Harding sobre armonía y discordia](https://bitcointalk.org/dec/p1.html):


> Los expertos Bitcoin hablan a menudo de consenso, cuyo significado es abstracto y Hard difícil de precisar. Pero la palabra consenso evolucionó de la palabra latina concentus, "una armonía que canta junta", así que no hablemos de Bitcoin consenso sino de Bitcoin armonía.
>

> La armonía es lo que hace que Bitcoin funcione. Miles de nodos completos trabajan cada uno de forma independiente para verificar que las transacciones que reciben son válidas, produciendo un acuerdo armonioso sobre el estado de Bitcoin Ledger sin que ningún operador de nodo necesite confiar en ningún otro. Es similar a un coro en el que cada miembro canta la misma canción al mismo tiempo para producir algo mucho más hermoso de lo que cualquiera de ellos podría producir por sí solo.
>

> El resultado de la armonía Bitcoin es un sistema en el que los bitcoins están a salvo no sólo de ladrones de poca monta (siempre que mantengas tus claves seguras), sino también de una inflación interminable, de confiscaciones masivas o selectivas, o simplemente del marasmo burocrático que es el sistema financiero heredado.

En este capítulo se analiza cómo actualizar Bitcoin sin provocar discordia. Mantener la armonía, es decir, mantener el consenso, es sin duda uno de los mayores retos del desarrollo de Bitcoin. Hay muchos matices en los mecanismos de actualización, que pueden entenderse mejor estudiando casos reales de actualizaciones anteriores. Por esta razón, el capítulo se centra en ejemplos históricos y empieza preparando el terreno con un vocabulario útil.


### Vocabulario



Según Wikipedia, [forward compatibility](https://en.wikipedia.org/wiki/Forward_compatibility) se refiere a la condición en la que un software antiguo puede procesar datos creados por softwares más nuevos, ignorando las partes que no entiende:


Una norma es compatible con el futuro si un producto que cumple las versiones anteriores puede procesar "sin problemas" los datos diseñados para versiones posteriores de la norma, ignorando las partes nuevas que no entiende.


Y viceversa, [compatibilidad con versiones anteriores](https://en.wikipedia.org/wiki/Backward_compatibility) se refiere a cuando los datos de un software antiguo pueden utilizarse en softwares más recientes. Se dice que un cambio es totalmente compatible si lo es tanto hacia adelante como hacia atrás.


Se dice que una modificación de las reglas de consenso de Bitcoin es una *Soft Fork* si es totalmente compatible. Esta es la forma más común de actualizar Bitcoin, por una serie de razones que discutiremos más adelante en este capítulo. Si un cambio en las reglas de consenso de Bitcoin es compatible hacia atrás pero no hacia adelante, se dice que es una *Hard Fork*.


Para obtener una visión general técnica de las bifurcaciones de Soft y Hard, lea el [capítulo 11 de Grokking Bitcoin](https://rosenbaum.se/book/grokking-Bitcoin-11.html). Explica estos términos y también se sumerge en los mecanismos de actualización. Es recomendable, aunque no estrictamente necesario, que te familiarices con esto antes de seguir leyendo.


### Mejoras históricas



Bitcoin no es lo mismo hoy que cuando se creó el bloque Genesis. Se han realizado varias actualizaciones a lo largo de los años. En 2018, Eric Lombrozo [habló en la conferencia Breaking Bitcoin](https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) sobre los diferentes mecanismos de actualización de Bitcoin, señalando lo mucho que han evolucionado con el tiempo. Incluso explicó cómo Satoshi Nakamoto una vez actualizó Bitcoin a través de un Hard Fork:


> De hecho había un Hard-Fork en Bitcoin que Satoshi hizo que nunca lo haríamos de esta manera-es una forma bastante mala de hacerlo. Si miras la descripción del commit de git aquí [[757f076](https://github.com/Bitcoin/Bitcoin/commit/757f0769d8360ea043f469f3a35f6ec204740446)], dice algo sobre revertir makefile.unix wx-config versión 0.3.6. Correcto. Eso es todo lo que dice. No tiene ninguna indicación de que tiene un cambio de ruptura en absoluto. Básicamente lo estaba escondiendo ahí. También [publicó en bitcointalk](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) y dijo, por favor actualice a 0.3.6 lo antes posible. Hemos corregido un error de implementación por el que es posible que transacciones falsas aparezcan como aceptadas. No aceptes pagos de Bitcoin hasta que actualices a 0.3.6. Si no puede actualizar inmediatamente, lo mejor sería apagar su nodo Bitcoin hasta que lo haga. Y encima, no sé por qué decidió hacer esto también, decidió añadir algunas optimizaciones en el mismo código. Arreglar un bug y añadir algunas optimizaciones.

Señala que, intencionadamente o no, esta Hard Fork creó oportunidades para futuras bifurcaciones de Soft, concretamente los operadores de script (opcodes) OP_NOP1-OP_NOP10. Analizaremos más a fondo este cambio de código en cve-2010-5141. Estos opcodes se han utilizado en dos bifurcaciones de Soft hasta ahora:


- [BIP65](https://github.com/Bitcoin/bips/blob/master/bip-0065.mediawiki) (OP_CHECKLOCKTIMEVERIFY)
- [BIP113](https://github.com/Bitcoin/bips/blob/master/bip-0112.mediawiki) (OP_SEQUENCEVERIFY).


Lombrozo también ofrece una visión general de cómo han evolucionado los mecanismos de actualización a lo largo de los años, hasta 2017. Desde entonces, solo se ha desplegado otra actualización importante, Taproot. El largo y algo caótico proceso que condujo a su activación nos ha ayudado a conocer mejor los mecanismos de mejora de Bitcoin.


#### Actualización de SegWit



Mientras que todas las actualizaciones anteriores a SegWit habían sido más o menos indoloras, esta fue diferente. Cuando se publicó el código de activación de SegWit, en octubre de 2016, parecía haber un apoyo abrumador entre los usuarios de Bitcoin, pero por alguna razón los mineros no señalaron su apoyo a esta actualización, lo que paralizó la activación sin solución a la vista.


Aaron van Wirdum describe este sinuoso camino en su artículo de Bitcoin Magazine [The Long Road To SegWit](https://bitcoinmagazine.com/technical/the-long-road-to-SegWit-how-bitcoins-biggest-protocol-upgrade-became-reality). Comienza explicando qué es la SegWit y cómo incide en el debate sobre el tamaño de los bloques. A continuación, Van Wirdum esboza el giro de los acontecimientos que condujeron a su activación final. En el centro de este proceso estaba un mecanismo de actualización llamado *Soft Fork activada por el usuario*, o UASF para abreviar, que fue propuesto por el usuario Shaolinfry:


> Shaolinfry propuso una alternativa: una Soft Fork activada por el usuario (UASF). En lugar de la activación de la energía Hash, una Soft Fork activada por el usuario tendría una "'activación de día de bandera' en la que los nodos comienzan la aplicación en un momento predeterminado en el futuro" Siempre que tal UASF sea aplicado por una mayoría económica, esto debería obligar a una mayoría de mineros a seguir (o activar) la Soft Fork.

Entre otras cosas, cita el correo electrónico de Shaolinfry a la lista de correo Bitcoin-dev. En esa ocasión Shaolinfry [argumentó en contra de las bifurcaciones Miner activadas Soft](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-February/013643.html), enumerando una serie de problemas con ellas:


> En primer lugar, requiere confiar en que la potencia Hash se validará tras la activación.  La Soft Fork BIP66 fue un caso en el que el 95% de la Hashrate señalaba que estaba preparada, pero en realidad cerca de la mitad no estaba validando las reglas actualizadas y minó sobre un bloque no válido por error.
>

> En segundo lugar, la señalización de Miner tiene un veto natural que permite a un pequeño porcentaje de Hashrate vetar la activación del nodo de la actualización para todo el mundo. Hasta la fecha, las bifurcaciones de Soft se han aprovechado del panorama relativamente centralizado de Mining, en el que hay relativamente pocos grupos de Mining que construyan bloques válidos; a medida que avancemos hacia una mayor descentralización de Hashrate, es probable que suframos cada vez más la "inercia de la actualización", que vetará la mayoría de las actualizaciones.

Shaolinfry también llamó la atención sobre una interpretación errónea habitual de la señalización Miner: la gente solía pensar que era un medio por el que los mineros podían decidir sobre las actualizaciones del protocolo, en lugar de una acción que ayudaba a coordinar las actualizaciones. Debido a este malentendido, los mineros también podrían haberse sentido obligados a proclamar en público su opinión sobre una determinada Soft Fork, como si eso diera peso a la propuesta.


La propuesta de la UASF consiste, en pocas palabras, en un "día de bandera" en el que los nodos empiecen a aplicar nuevas normas específicas. De este modo, los mineros no tienen que hacer un esfuerzo colectivo para coordinar la actualización, sino que *pueden* activarla antes del día de la bandera si un número suficiente de bloques señalan su apoyo:


> Mi sugerencia es tener lo mejor de ambos mundos. Dado que un Soft Fork activado por el usuario necesita un plazo relativamente largo antes de la activación, podemos combinarlo con el BIP9 para dar la opción de una activación coordinada más rápida del Hash o una activación por día de bandera, lo que ocurra antes.
> En ambos casos, podemos aprovechar los sistemas de alerta de BIP9. El cambio es relativamente sencillo: se añade un parámetro de tiempo de activación que cambiará el estado de BIP9 a LOCKED_IN antes de que finalice el tiempo de espera de despliegue de BIP9.

Esta idea despertó mucho interés, pero no pareció alcanzar un apoyo casi unánime, lo que causó preocupación por una posible ruptura de la cadena. El artículo de Aaron van Wirdum explica cómo se resolvió finalmente gracias a [BIP91](https://github.com/Bitcoin/bips/blob/master/bip-0091.mediawiki), cuyo autor es James Hilliard:


> Hilliard propuso una solución algo compleja pero inteligente que lo haría todo compatible: La activación segregada de testigos propuesta por el equipo de desarrollo de Bitcoin Core, el UASF de BIP148 y el mecanismo de activación del Acuerdo de Nueva York. Su BIP91 podría mantener íntegro Bitcoin, al menos durante la activación de SegWit.

Hubo más factores complicados (por ejemplo, el llamado "Acuerdo de Nueva York"), que este PIF tuvo que tener en cuenta. Le animamos a leer el artículo completo de Van Wirdum para conocer los numerosos detalles interesantes de esta historia.


#### Debate posterior a SegWit


Tras el despliegue de SegWit, surgió un debate sobre los mecanismos de despliegue. Como señalaron Eric Lombrozo en [su charla en la conferencia Breaking Bitcoin](https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) y Shaolinfry, una Miner activada Soft Fork no es el mecanismo de actualización ideal:


> Es probable que en algún momento queramos añadir más funciones al protocolo Bitcoin. Es una gran pregunta filosófica que nos hacemos. ¿Hacemos un UASF para el próximo? ¿Y un enfoque híbrido? Miner activado por sí mismo ha sido descartado. bip9 no vamos a volver a utilizarlo.

En enero de 2020, Matt Corallo [envió un correo electrónico](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2020-January/017547.html) a la lista de correo Bitcoin-dev que inició una discusión sobre los futuros mecanismos de despliegue de Soft Fork. Enumeró cinco objetivos que consideraba esenciales en una actualización. David Harding [los resume en un boletín de Optech sobre Bitcoin](https://bitcoinops.org/en/newsletters/2020/01/15/#discussion-of-Soft-Fork-activation-mechanisms) como:


> La capacidad de abortar si se encuentra una objeción seria a los cambios propuestos en las reglas de consenso . La asignación de tiempo suficiente tras la publicación del software actualizado para garantizar que la mayoría de los nodos económicos se actualicen para aplicar dichas normas. La expectativa de que la tasa de Hash de la red sea aproximadamente la misma antes y después del cambio, así como durante cualquier transición . La prevención, en la medida de lo posible, de la creación de bloques que no sean válidos según las nuevas normas, lo que podría dar lugar a falsas confirmaciones en nodos no actualizados y clientes SPV. La garantía de que los mecanismos de cancelación no puedan ser utilizados indebidamente por griefers o partisanos para retener una actualización ampliamente deseada y sin problemas conocidos

Lo que Corallo propone es una combinación de una Miner activada Soft Fork y una Soft Fork activada por el usuario:


> Así, como algo un poco más concreto, creo que un método de activación que siente el precedente correcto y considere adecuadamente los objetivos anteriores, sería:
>

> 1) un despliegue estándar del PIF 9 con un horizonte temporal de un año para
activación con un 95% de preparación Miner, +

> 2) en caso de que no se produzca ninguna activación en el plazo de un año, un plazo de seis meses
periodo de calma durante el cual la comunidad puede analizar y debatir

las razones de la no activación y, +

> 3) en el caso de que tenga sentido, un simple parámetro de línea de comandos/Bitcoin.conf compatible desde la versión de despliegue original permitiría a los usuarios optar por un despliegue BIP 8 con un horizonte temporal de 24 meses para la activación del día de la bandera (así como una nueva versión de Bitcoin Core que habilite la bandera de forma universal).
>

> Esto proporciona un horizonte temporal muy largo para una activación más estándar, al tiempo que garantiza el cumplimiento de los objetivos del nº 5, incluso si, en esos casos, el horizonte temporal tiene que ampliarse significativamente para cumplir los objetivos del nº 3. Desarrollar Bitcoin no es una carrera. Si tenemos que hacerlo, esperar 42 meses garantiza que no sentamos un precedente negativo del que nos arrepentiremos cuando Bitcoin siga creciendo.

#### Actualización Taproot - Juicio rápido



Cuando Taproot estuvo listo para su despliegue en octubre de 2020, es decir, cuando todos los detalles técnicos de sus reglas de consenso se habían implementado y habían alcanzado una amplia aprobación dentro de la comunidad, los debates sobre cómo desplegarlo realmente empezaron a calentarse. Hasta entonces, los debates habían sido bastante discretos.


Empezaron a circular muchas propuestas de mecanismos de activación, y David Harding

[los resumió en la Bitcoin Wiki](https://en.Bitcoin.it/wiki/Taproot_activation_proposals). En su artículo explicaba algunas propiedades de la BIP8, que en aquel momento había sufrido algunos cambios recientes para hacerla más flexible.


> En el momento de redactar este documento, se ha redactado [BIP8](https://github.com/Bitcoin/bips/blob/master/bip-0008.mediawiki) basándose en las lecciones aprendidas en 2017. Un cambio notable tras las BIP 9+148 es que la activación forzada se basa ahora en la altura del bloque en lugar de en la mediana del tiempo transcurrido; un segundo cambio notable es que la activación forzada es un parámetro booleano que se elige cuando se establecen los parámetros de activación de un Soft Fork, ya sea para el despliegue inicial o para su actualización en un despliegue posterior.

BIP8 sin activación forzada es muy similar a [BIP9](https://github.com/Bitcoin/bips/blob/master/bip-0009.mediawiki) versión bits con tiempo de espera y retardo, con la única diferencia significativa del uso de BIP8 de alturas de bloque en comparación con el uso de BIP9 de tiempo pasado medio. Esta configuración permite que el intento falle (pero se puede reintentar más tarde).


El BIP8 con activación forzada concluye con un periodo de señalización obligatoria en el que todos los bloques producidos de acuerdo con sus reglas deben señalar que están listos para el Soft Fork de forma que se desencadene la activación en un despliegue anterior del mismo Soft Fork con activación no obligatoria. En otras palabras, si se lanza la versión x del nodo sin activación obligatoria y, más tarde, se lanza la versión y que obliga con éxito a los mineros a comenzar a señalar la preparación dentro del mismo periodo de tiempo, ambas versiones comenzarán a aplicar las nuevas reglas de consenso al mismo tiempo.


Esta flexibilidad de la propuesta revisada del PIF8 permite expresar algunas otras ideas en términos de cómo serían utilizando el PIF8. Esto proporciona un factor común para categorizar muchas propuestas diferentes.


A partir de este momento, las discusiones se hicieron muy acaloradas, especialmente en torno a si `lockinontimeout` debía ser `true` (como en una Soft Fork activada por el usuario, denominada "BIP8 con activación forzada" por Harding) o `false` (como en una Miner Soft Fork activada por el usuario, denominada "BIP8 sin activación forzada" por Harding).


Entre las propuestas enumeradas, una se titulaba "A ver qué pasa". Por alguna razón, esta propuesta no tuvo mucha tracción hasta siete meses después.


Durante esos siete meses, la discusión continuó y parecía que no había forma de alcanzar un consenso amplio sobre qué mecanismo de despliegue utilizar. Había principalmente dos bandos: uno que prefería `lockinontimeout=true` (la multitud del UASF) y otro que prefería `lockinontimeout=false` (la multitud de "inténtalo y si falla vuelve a pensarlo"). Como no había un apoyo abrumador a ninguna de estas opciones, el debate se desarrolló en círculos sin que pareciera haber forma de avanzar. Algunas de estas discusiones se mantuvieron en IRC, en un canal llamado ##Taproot-activation, pero [el 5 de marzo de 2021](https://gnusha.org/Taproot-activation/2021-03-05.log), algo cambió:


```
06:42 < harding> roconnor: is somebody proposing BIP8(3m, false)?  I mentioned that the other day but I didn't see any responses.
[...]
06:43 < willcl_ark_> Amusingly, I was just thinking to myself that, vs this, the SegWit activation was actually pretty straightforward: simply a LOT=false and if it fails a UASF.
06:43 < maybehuman> it's funny, "let's see what happens" (i.e. false, 3m) was a poular choice right at the beginning of this channel iirc
06:44 < roconnor> harding: I think I am.  I don't know how much that is worth.  Mostly I think it would be a widely acceptable configuration based on my understanding of everyone's concerns.
06:44 < willcl_ark_> maybehuman: becuase everybody actually wants this, even miners reckoned they could upgrade in about two weeks (or at least f2pool said that)
06:44 < roconnor> harding: BIP8(3m,false) with an extended lockin-period.
06:45 < harding> roconnor: oh, good.  It's been my favorite option since I first summarized the options on the wiki like seven months ago.
06:45 <@michaelfolkson> UASF wouldn't release (true,3m) but yeah Core could release (false, 3m)
06:45 < willcl_ark_> harding: It certainly seems like a good approach to me. _if_ that fails, then you can try an understand why, without wasting too much time
```


El planteamiento de "vamos a ver qué pasa" pareció calar por fin en la mente de la gente. Este proceso se etiquetaría más tarde como "Juicio Rápido" debido a su corto periodo de señalización. David Harding explica esta idea a la comunidad en general en un

[correo electrónico a la lista de correo Bitcoin-dev](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-March/018583.html):

> La versión anterior de esta propuesta se documentó hace más de 200 días y el código subyacente de Taproot se fusionó en Bitcoin Core hace más de 140 días. Si hubiéramos iniciado la prueba rápida en el momento en que se fusionó Taproot (lo cual es poco realista), o bien estaríamos a menos de dos meses de tener Taproot o habríamos pasado al siguiente intento de activación hace más de un mes.
>

> En su lugar, hemos debatido largo y tendido y no parece que estemos más cerca de lo que creo que es una solución ampliamente aceptable que cuando la lista de correo empezó a discutir esquemas de activación post-SegWit hace más de un año Creo que Speedy Trial es una forma de generate rápido progreso que pondrá fin al debate (por ahora, si la activación tiene éxito) o nos dará algunos datos reales sobre los que basar futuras propuestas de activación Taproot.

Este mecanismo de despliegue se perfeccionó a lo largo de dos meses y luego se publicó en [Bitcoin Core version 0.21.1](https://github.com/Bitcoin/Bitcoin/blob/master/doc/release-notes/release-notes-0.21.1.md#Taproot-Soft-Fork). Los mineros empezaron rápidamente a señalar esta actualización moviendo el estado de despliegue a `LOCKED_IN`, y tras un periodo de gracia las reglas Taproot se activaron a mediados de noviembre de 2021 en el bloque [709632](https://Mempool.space/block/0000000000000000000687bca986194dc2c1f949318629b44bb54ec0a94d8244).


#### Futuros mecanismos de despliegue


Dados los problemas con las recientes bifurcaciones de Soft, SegWit y Taproot, no está claro cómo se desplegará la próxima actualización. Speedy Trial se utilizó para desplegar Taproot, pero se utilizó para salvar el abismo entre las multitudes de la UASF y la MASF, no porque haya surgido como el mecanismo de despliegue más conocido.


### Riesgos


Durante la activación de cualquier Fork, ya sea Hard o Soft, Miner activada o activada por el usuario, existe el riesgo de que se produzca una ruptura duradera de la cadena. Una escisión que se prolongue durante más de unos bloques puede causar graves daños al sentimiento en torno a Bitcoin, así como a su precio. Pero, sobre todo, causaría una gran confusión sobre lo que es Bitcoin. ¿Es Bitcoin esta cadena o aquella cadena?


El riesgo con una Soft Fork activada por el usuario es que las nuevas reglas se activen aunque la mayoría de la potencia Hash no las apoye. Este escenario daría lugar a una ruptura duradera de la cadena, que persistiría hasta que la mayoría de la potencia de Hash adoptara las nuevas reglas. Podría ser especialmente Hard para incentivar a los mineros a cambiar a la nueva cadena si ya habían minado bloques después de la división en la antigua cadena, porque al cambiar de rama estarían abandonando sus propias recompensas de bloques. Sin embargo, vale la pena mencionar un episodio notable: en marzo de 2013 se produjo una escisión de larga duración, debido a una Hard Fork no intencionada y, en contra de este incentivo, dos grandes pools Mining tomaron la decisión de abandonar su rama de la escisión para restaurar el consenso.


Por otro lado, el riesgo con una Miner activada Soft Fork es consecuencia del hecho de que los mineros pueden realizar falsas señales, lo que significa que la parte real de la potencia Hash que apoya el cambio podría ser menor de lo que parece. Si el apoyo real no comprende una mayoría del poder Hash, probablemente veríamos una división de la cadena de larga duración similar a la descrita en el párrafo anterior. Esto, o al menos un problema similar, ha ocurrido en la realidad cuando se desplegó el BIP66, pero se resolvió en 6 bloques más o menos.


#### Costes de una escisión



Jimmy Song [habló de los costes asociados a las horquillas Hard](https://btctranscripts.com/breaking-Bitcoin/2017/socialized-costs-of-Hard-forks/) en Breaking Bitcoin en París, pero gran parte de lo que dijo se aplica también a una ruptura de cadena debida a una Soft Fork fallida. Habló de *externalidades negativas*, y las definió como el precio que otro tiene que pagar por tus propias acciones:


> El ejemplo clásico de externalidad negativa es una fábrica. Tal vez produzcan, tal vez sea una refinería de petróleo y produzcan un bien que es bueno para la economía, pero también producen algo que es una externalidad negativa, como la contaminación. No es sólo algo por lo que todo el mundo tiene que pagar, limpiar o sufrir. Pero también hay efectos de segundo y tercer orden, como más tráfico hacia la fábrica como resultado de más trabajadores que necesitan ir allí. También es posible que se ponga en peligro la vida salvaje de los alrededores. No es que todo el mundo tenga que pagar por las externalidades negativas, pueden ser personas concretas, como las personas que antes utilizaban esa carretera o los animales que estaban cerca de esa fábrica, y que también están pagando por el coste de esa fábrica.

En el contexto de Bitcoin, ejemplifica las externalidades negativas utilizando Bitcoin Cash (bcash), que es un Hard Fork de Bitcoin creado poco antes de esa conferencia en 2017. Clasifica las externalidades negativas de una Hard Fork en costes únicos y costes permanentes.


Entre los muchos ejemplos de costes únicos, menciona los de las bolsas:


> Así que tenemos un montón de intercambios y tenían un montón de costes únicos que tenían que pagar. Lo primero que ocurrió es que los depósitos y las retiradas tuvieron que detenerse durante uno o dos días porque no sabían qué iba a pasar. Muchos de estos intercambios tuvieron que recurrir al almacenamiento de Cold porque sus usuarios demandaban bcash. Es parte de su deber fiduciario, tienen que hacerlo. También tienen que auditar el nuevo software. Esto es algo que tuvimos que hacer en itbit. Queremos gastar bcash- ¿cómo lo hacemos? ¿Tenemos que descargar electron cash? ¿Tiene malware? Tenemos que ir y auditarlo. Tuvimos como 10 días para averiguar si esto estaba bien o no. Y luego tienes que decidir, ¿vamos a permitir una retirada de una sola vez, o vamos a listar esta nueva moneda? Para que una Exchange liste una nueva moneda, no es fácil, hay todo tipo de nuevos procedimientos para el almacenamiento de Cold, firma, depósitos, retiros. O se podría hacer un evento único en el que se les diera el dinero en un momento dado y no se volviera a pensar en ello. Pero eso también tiene sus problemas. Y por último, y sea cual sea la forma en que lo hagas, retiros o listados, vas a necesitar una nueva infraestructura para trabajar con este token de alguna manera, incluso si se trata de un retiro de una sola vez. Necesitas alguna forma de dar estos tokens a tus usuarios. De nuevo, a corto plazo. ¿Correcto? No hay tiempo para hacer esto, tiene que hacerse rápidamente.

También enumera los costes únicos en que incurren comerciantes, procesadores de pagos, monederos, mineros y usuarios, así como algunos de los costes permanentes, por ejemplo la pérdida de privacidad y un mayor riesgo de reorganizaciones.


De hecho, cuando se produce una escisión y la cadena con las normas más generales se hace más fuerte que la cadena con las normas más estrictas, se producirá una reorganización. Esto tendrá un grave impacto en todas las transacciones realizadas en la rama eliminada. Por estas razones, es muy importante intentar evitar las divisiones de cadenas en todo momento.


### Conclusión sobre la actualización


Bitcoin crece y evoluciona con el tiempo. A lo largo de los años se han utilizado distintos mecanismos de actualización y la curva de aprendizaje es pronunciada. Se siguen inventando métodos cada vez más sofisticados y robustos, a medida que aprendemos más sobre cómo reacciona la red.


Para mantener la armonía en Bitcoin, las bifurcaciones de Soft han demostrado ser el camino a seguir, pero la gran pregunta aún no tiene respuesta: ¿cómo desplegamos de forma segura las bifurcaciones de Soft sin causar discordia?


## Pensamiento adversario

<chapterId>d4982f3d-4694-51cc-99be-28f54b03a2a2</chapterId>


![](assets/adversarialthinking-banner.webp)


Este capítulo aborda el *pensamiento adversario*, una mentalidad que se centra en lo que podría salir mal y en cómo podrían actuar los adversarios. Comenzamos discutiendo los supuestos de seguridad y el modelo de seguridad de Bitcoin, tras lo cual explicamos cómo los usuarios ordinarios pueden mejorar su auto-soberanía y la descentralización Full node de Bitcoin pensando de forma adversaria. A continuación, examinamos algunas amenazas reales a Bitcoin, así como la mente del adversario. Por último, hablamos del *axioma de la resistencia*, que puede ayudarte a entender por qué la gente está trabajando en Bitcoin en primer lugar.


Cuando se habla de seguridad en varios sistemas, es importante entender cuáles son los supuestos de seguridad. Un supuesto de seguridad típico en Bitcoin es que "el problema del logaritmo discreto es Hard imposible de resolver", lo que, en pocas palabras, significa que es prácticamente imposible encontrar una clave privada que corresponda a una clave pública concreta. Otra suposición de seguridad bastante fuerte es que la mayoría del hashpower de la red es honesto, lo que significa que juegan según las reglas. Si se demuestra que estas suposiciones son erróneas, entonces Bitcoin está en problemas.


En 2015 Andrew Poelstra [dio una charla](https://btctranscripts.com/scalingbitcoin/hong-kong-2015/security-assumptions/) en la conferencia Scaling Bitcoin de Hong Kong, durante la cual analizó los supuestos de seguridad de Bitcoin. Comienza señalando que muchos sistemas no tienen en cuenta a los adversarios hasta cierto punto; por ejemplo, es realmente Hard proteger un edificio contra todo tipo de eventos adversos. En su lugar, generalmente aceptamos la posibilidad de que alguien queme el edificio, y hasta cierto punto prevenimos este y otros comportamientos adversos mediante la aplicación de la ley, etc.


Ver la analogía del edificio de Greg Maxwell:


![](https://youtu.be/Gs9lJTRZCDc?t=2799)


Pero en Internet las cosas son diferentes:


> Sin embargo, en Internet no tenemos esto. Tenemos comportamientos seudónimos y anónimos, cualquiera puede conectarse a todo el mundo y dañar el sistema. Si es posible perjudicar al sistema, lo harán. No podemos asumir que serán visibles y que serán descubiertos.

La consecuencia es que todos los puntos débiles conocidos de Bitcoin deben solucionarse de alguna manera, de lo contrario serán explotados. Después de todo, Bitcoin es el mayor tarro de miel del mundo.


Poelstra continúa mencionando cómo Bitcoin es un nuevo tipo de sistema; es más nebuloso que, por ejemplo, un protocolo de firma que tiene unos supuestos de seguridad muy claros.


En su blog personal, el ingeniero de software Jameson Lopp, [se sumerge en este tema](https://blog.lopp.net/bitcoins-security-model-a-deep-dive/):


> En realidad, el protocolo Bitcoin se construyó y se sigue construyendo sin una especificación o un modelo de seguridad formalmente definidos. Lo mejor que podemos hacer es estudiar los incentivos y el comportamiento de los actores dentro del sistema para comprenderlo mejor e intentar describirlo.

Así pues, tenemos un sistema que parece funcionar en la práctica, pero que no podemos demostrar formalmente que sea seguro. Una prueba probablemente no es posible debido a

la complejidad del propio sistema.


### No sólo para expertos en Bitcoin



La importancia del pensamiento adversario también se extiende hasta cierto punto a los usuarios cotidianos de Bitcoin, no sólo a los desarrolladores y expertos acérrimos de Bitcoin. Ragnar Lifthasir menciona en un [tweetstorm](https://bitcoinwords.github.io/tweetstorm-on-adversarial-thinking) cómo las narrativas simplistas en torno a Bitcoin - por ejemplo, "sólo HODL" - pueden ser degradantes para Bitcoin en sí, y concluye diciendo


> Para que Bitcoin y nosotros mismos seamos más fuertes, tenemos que pensar como los ingenieros de software que contribuyen a Bitcoin. Hacen revisiones por pares, buscando fallos sin piedad. En sus eventos técnicos hablan de todas las formas en que puede fallar una propuesta. Piensan de forma contradictoria. Son conservadores

Se refiere a estas narrativas simplistas como monomanías. Con esta definición quiere decir que al centrarse en una sola cosa -por ejemplo, "sólo HODL"- se corre el riesgo de pasar por alto cosas posiblemente más importantes, como mantener la seguridad de Bitcoin o hacer todo lo posible por utilizar Bitcoin de manera Trustless.


### Amenazas



Hay muchas debilidades conocidas en Bitcoin, y muchas de ellas están siendo explotadas activamente. Para hacerse una idea, eche un vistazo a la [Página de debilidades](https://en.Bitcoin.it/wiki/Weaknesses) en la wiki de Bitcoin. Allí se menciona una amplia variedad de problemas, tales como

Wallet robo y ataques de denegación de servicio:


> Si un atacante intenta llenar la red con clientes que controla, entonces sería muy probable que se conectara sólo a nodos atacantes. Aunque Bitcoin nunca utiliza un recuento de nodos para nada, aislar completamente un nodo de la red honesta puede ser útil en la ejecución de otros ataques.

Este tipo de ataque se denomina *Ataque Sibila*, y se produce siempre que una única entidad controla varios nodos de una red y los utiliza para aparecer como varias entidades.


Como también menciona la cita, el ataque Sybil no es efectivo en la red Bitcoin porque no hay votación a través de nodos u otras entidades numerables, sino a través de la potencia de cálculo. No obstante, esta estructura plana hace que el sistema sea susceptible de otros ataques. La página wiki de Bitcoin también esboza otros posibles ataques, como el ocultamiento de información (a menudo conocido como *ataque eclipse*), y la forma en que Bitcoin Core implementa algunas contramedidas heurísticas contra tales ataques.


Los anteriores son ejemplos de amenazas reales de las que hay que ocuparse.


### Campo de sabotaje simple


![](assets/sabotage-manual.webp)


Extracto del Manual de campo del sabotaje simple


Para comprender mejor la mente del adversario, puede ser útil echar un vistazo a su forma de operar. Un organismo gubernamental estadounidense llamado Oficina de Servicios Estratégicos, que operó durante la Segunda Guerra Mundial y tenía entre sus propósitos llevar a cabo espionaje, realizar sabotajes y difundir propaganda, elaboró un [manual](https://www.gutenberg.org/ebooks/26184) para su personal sobre cómo sabotear adecuadamente al enemigo. Su título era "Simple Sabotage Field Manual" y contenía consejos concretos sobre cómo infiltrarse en el enemigo para hacerle la vida Hard. Los consejos iban desde quemar almacenes hasta causar desgaste a los taladros para disminuir la capacidad de reacción del enemigo

eficacia.


Por ejemplo, hay una sección sobre cómo un infiltrado puede desbaratar organizaciones. No es Hard ver cómo esas tácticas podrían utilizarse para atacar el proceso de desarrollo Bitcoin, en el que cualquiera puede participar. Un atacante dedicado puede seguir paralizando el progreso con interminables preocupaciones sobre cuestiones irrelevantes, regatear sobre redacciones precisas e intentar reiterar discusiones que ya se han abordado exhaustivamente. El atacante también puede contratar a un ejército de trolls para multiplicar su propia eficacia; podemos llamar a esto un ataque social Sybil. Utilizando un ataque social Sybil, pueden hacer que parezca que hay más resistencia contra un cambio propuesto de la que realmente hay.


Esto pone de relieve cómo un Estado decidido puede hacer y hará todo lo que esté en su mano para destruir al enemigo, incluso acabar con él desde dentro. Dado que la Bitcoin es una forma de dinero que compite con las monedas fiduciarias establecidas, lo más probable es que los Estados consideren a la Bitcoin como un enemigo.


### Axioma de la resistencia


Eric Voskuil [escribe en su página wiki de Criptoeconomía](https://github.com/libbitcoin/libbitcoin-system/wiki/Axiom-of-Resistance) sobre lo que él llama el "axioma de la resistencia":


> En otras palabras, se supone que es posible que un sistema resista el control del estado. Esto no se acepta como un hecho, sino que se considera una suposición razonable, debida al estudio empírico del comportamiento de sistemas similares, en la que basar el sistema.
>

> Quien no acepte el axioma de la resistencia está contemplando un sistema totalmente distinto al Bitcoin. Si uno asume que no es posible que un sistema resista los controles del estado, las conclusiones no tienen sentido en el contexto de Bitcoin - al igual que las conclusiones en geometría esférica contradicen la euclidiana. ¿Cómo puede Bitcoin ser sin permiso o resistente a la censura sin el axioma? La contradicción lleva a cometer errores evidentes en un intento de racionalizar el conflicto.


Lo que está diciendo esencialmente es que sólo cuando se asume que es posible crear un sistema que los Estados no puedan controlar, tiene sentido intentarlo.


Esto significa que para trabajar en Bitcoin debes aceptar el axioma de la resistencia, de lo contrario será mejor que dediques tu tiempo a otros proyectos. Reconocer ese axioma le ayuda a centrar sus esfuerzos de desarrollo en los verdaderos problemas que tiene entre manos: codificar en torno a adversarios a nivel de estado. En otras palabras, piensa de forma adversaria.


### Conclusión sobre el pensamiento adversario



Un sistema descentralizado no puede tener responsabilidad fuera del propio sistema, por lo que Bitcoin debe prevenir el comportamiento malicioso de forma más rigurosa que los sistemas tradicionales. El pensamiento adversario es imperativo en un sistema de este tipo.


Para mantener a salvo la Bitcoin hay que conocer a sus enemigos y sus incentivos. La mayoría de las amenazas parecen reducirse a los Estados nación, que tienen un enorme poder económico a través de los impuestos y la impresión de dinero. Probablemente no renunciarán fácilmente a sus privilegios de impresión de dinero.


## Código abierto

<chapterId>427a160c-f893-5b2c-afba-7b24e71ba899</chapterId>



![](assets/opensource-banner.webp)


Bitcoin se ha construido utilizando software de código abierto. En este capítulo analizamos qué significa esto, cómo funciona el mantenimiento del software y cómo el software de código abierto en Bitcoin permite el desarrollo sin permisos. Nos sumergimos en la *criptografía de selección*, que trata de la selección y el uso de bibliotecas en sistemas criptográficos. El capítulo incluye una sección sobre el proceso de revisión de Bitcoin, seguida de otra sobre las formas en que los desarrolladores de Bitcoin obtienen financiación. La última sección habla de cómo la cultura de código abierto de Bitcoin puede parecer realmente extraña desde fuera, y por qué esta rareza percibida es en realidad un signo de buena salud.


La mayoría de los programas de Bitcoin, y especialmente Bitcoin Core, son de código abierto. Esto significa que el código fuente del software se pone a disposición del público en general para su escrutinio, retoque, modificación y redistribución. La definición de código abierto en [](https://opensource.org/osd) incluye, entre otros, los siguientes puntos importantes:


> Redistribución gratuita: La licencia no restringirá a ninguna parte la venta o regalo del software como componente de una distribución agregada de software que contenga programas de varias fuentes diferentes. La licencia no exigirá el pago de regalías u otros derechos por dicha venta.
>

> Código fuente: El programa debe incluir el código fuente y debe permitir su distribución tanto en código fuente como compilado. Cuando alguna forma de un producto no se distribuya con el código fuente, debe existir un medio bien publicitado para obtener el código fuente por un coste de reproducción no superior al razonable, preferiblemente descargándolo a través de Internet sin coste alguno. El código fuente debe ser la forma preferida en la que un programador modificaría el programa. No se permite el código fuente ofuscado deliberadamente. No se permiten formas intermedias como la salida de un preprocesador o traductor.
>

> Obras derivadas: La licencia debe permitir modificaciones y trabajos derivados, y debe permitir que se distribuyan bajo los mismos términos que la licencia del software original.

Bitcoin Core se adhiere a esta definición distribuyéndose bajo la [Licencia MIT](https://github.com/Bitcoin/Bitcoin/blob/master/COPYING):


```
The MIT License (MIT)

Copyright (c) 2009-2022 The Bitcoin Core developers
Copyright (c) 2009-2022 Bitcoin Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```


Como se indica en el capítulo "No confíe, verifique", es importante que los usuarios puedan verificar que el software Bitcoin que ejecutan "funciona como se anuncia". Para ello, deben tener acceso sin restricciones al código fuente del software que desean verificar.


En las próximas secciones nos sumergiremos en otros aspectos interesantes del software de código abierto en Bitcoin.


### Mantenimiento del software



El código fuente de Bitcoin Core se mantiene en un repositorio Git alojado en [GitHub](https://github.com/Bitcoin/Bitcoin). Cualquiera puede clonar ese mismo repositorio sin pedir ningún permiso, y luego inspeccionarlo, compilarlo o hacerle cambios localmente. Esto significa que hay muchos miles de copias del repositorio repartidas por todo el mundo. Son todas copias del mismo repositorio, así que ¿qué hace que este repositorio específico de GitHub Bitcoin Core sea tan especial? Técnicamente no es especial en absoluto, pero socialmente se ha convertido en el punto focal del desarrollo de Bitcoin.


El experto en Bitcoin y seguridad Jameson Lopp lo explica muy bien en una [entrada de blog](https://blog.lopp.net/who-controls-Bitcoin-core-/) titulada "¿Quién controla Bitcoin Core?":


> Bitcoin Core es un punto focal para el desarrollo del protocolo Bitcoin más que un punto de mando y control. Si dejara de existir por cualquier motivo, surgiría un nuevo punto focal - la plataforma de comunicaciones técnicas en la que se basa (actualmente el repositorio GitHub) es una cuestión de conveniencia más que de definición / integridad del proyecto. De hecho, ya hemos visto cómo el punto focal de Bitcoin para el desarrollo cambiaba de plataforma ¡e incluso de nombre!

A continuación explica cómo se mantiene y protege el software de Bitcoin Core frente a cambios de código malintencionados. La conclusión general de este artículo se resume al final del mismo:


> Nadie controla Bitcoin.
>

> Nadie controla el punto focal del desarrollo de Bitcoin.

Eric Lombrozo, desarrollador del núcleo Bitcoin, habla más a fondo del proceso de desarrollo en su [Medium post](https://medium.com/@elombrozo/the-Bitcoin-core-merge-process-74687a09d81d) titulado "The Bitcoin Core Merge Process" (El proceso de fusión del núcleo Bitcoin):


> Cualquiera puede Fork el repositorio de código base y hacer cambios arbitrarios en su propio repositorio. Pueden construir un cliente desde su propio repositorio y ejecutarlo si lo desean. También pueden hacer compilaciones binarias para que otras personas las ejecuten.
>

> Si alguien quiere fusionar un cambio que ha hecho en su propio repositorio en Bitcoin Core, puede presentar una solicitud de extracción. Una vez enviado, cualquiera puede revisar los cambios y comentarlos independientemente de si tienen o no acceso a Bitcoin Core.

Hay que tener en cuenta que las pull requests pueden tardar mucho tiempo en ser incorporadas al repositorio por los mantenedores, y eso suele deberse a la falta de revisión, que a menudo se debe a la falta de *revisores*.


Lombrozo también habla del proceso que rodea a los cambios de consenso, pero eso va un poco más allá del alcance de este capítulo. Consulte el capítulo anterior "Actualización" para obtener más información sobre cómo se actualiza el protocolo Bitcoin.


### Desarrollo sin permiso



Hemos establecido que cualquiera puede escribir código para Bitcoin Core sin pedir ningún permiso, pero no necesariamente fusionarlo con el repositorio Git principal. Esto afecta a cualquier modificación, desde cambiar los esquemas de color del usuario gráfico Interface, hasta la forma en que se formatean los mensajes peer-to-peer, e incluso las reglas de consenso, es decir, el conjunto de reglas que definen un Blockchain válido.


Probablemente igual de importante es que los usuarios son libres de desarrollar sistemas sobre Bitcoin, sin pedir ningún permiso. Hemos visto innumerables proyectos de software de éxito que se construyeron sobre Bitcoin, como:



- Lightning Network: Red de pago que permite el pago rápido de cantidades muy pequeñas. Requiere muy pocas On-Chain Bitcoin transacciones. Existen varias implementaciones interoperables, como [Core Lightning](https://github.com/ElementsProject/lightning), [LND](https://github.com/lightningnetwork/LND), [Eclair](https://github.com/ACINQ/eclair) y [Lightning Dev Kit](https://github.com/lightningdevkit).
- CoinJoin: Varias partes colaboran para combinar sus pagos en una única transacción para dificultar la agrupación Address. Existen varias implementaciones.
- Cadenas laterales: Este sistema puede bloquear una moneda en la Blockchain de Bitcoin para desbloquearla en alguna otra Blockchain. Esto permite trasladar bitcoins a otra Blockchain, es decir, a una Sidechain, para poder utilizar las funciones disponibles en esa Sidechain. Algunos ejemplos son [Blockstream's Elements](https://github.com/ElementsProject/Elements).
- OpenTimestamps: Le permite [Timestamp un documento](https://opentimestamps.org/) en Blockchain de Bitcoin de forma privada. A continuación, puede utilizar ese Timestamp para demostrar que un documento debe haber existido antes de un cierto tiempo.


Sin el desarrollo sin permisos, muchos de estos proyectos no habrían sido posibles. Como se indica en el capítulo sobre Neutralidad, si los desarrolladores tuvieran que pedir permiso para construir protocolos sobre Bitcoin, sólo se desarrollarían los protocolos permitidos por el comité central de concesión de permisos a desarrolladores.


Es habitual que sistemas como los mencionados anteriormente se licencien a su vez como software de código abierto, lo que a su vez permite que la gente contribuya, reutilice o revise su código sin pedir ningún permiso. El código abierto se ha convertido en el estándar de oro de las licencias de software Bitcoin.


### Desarrollo de seudónimos



No tener que pedir permiso para desarrollar software Bitcoin pone sobre la mesa una opción interesante e importante: puede escribir y publicar código, en Bitcoin Core o en cualquier otro proyecto de código abierto, sin revelar su identidad.


Muchos desarrolladores eligen esta opción operando bajo un seudónimo y tratando de mantenerlo desvinculado de su verdadera identidad. Las razones para hacerlo pueden variar de un desarrollador a otro. Un usuario con seudónimo es ZmnSCPxj. Entre otros proyectos, contribuye a Bitcoin Core y Core Lightning, una de las varias implementaciones de Lightning Network. [Escribe](https://zmnscpxj.github.io/about.html) en su página web:


> Soy ZmnSCPxj, una persona de Internet generada aleatoriamente. Mis pronombres son él/ella/él.
>

> Comprendo que los humanos deseen instintivamente conocer mi identidad. Sin embargo, creo que mi identidad es en gran medida inmaterial, y prefiero que me juzguen por mi trabajo.
>

> Si te estás preguntando si donar o no, y te preguntas cuál es mi coste de vida o mis ingresos, por favor entiende que hablando con propiedad, deberías donarme en función de la utilidad que encuentres a mi
artículos y mi trabajo sobre el Bitcoin y el Lightning Network.


En su caso, la razón para utilizar un seudónimo debe juzgarse por sus méritos y no por quién es o son la persona o personas que se esconden tras el seudónimo. Curiosamente, reveló en un [artículo en CoinDesk](https://www.coindesk.com/markets/2020/06/29/many-Bitcoin-developers-are-choosing-to-use-pseudonyms-for-good-reason/) que el seudónimo se creó por un motivo diferente.


> Mi razón inicial [para usar un seudónimo] era simplemente que me preocupaba [cometer] un error masivo; así, ZmnSCPxj pretendía ser un seudónimo desechable que pudiera abandonarse en tal caso. Sin embargo, parece que ha cosechado una reputación mayoritariamente positiva, así que lo he mantenido

En efecto, utilizar un seudónimo te permite hablar con más libertad sin poner en riesgo tu reputación personal en caso de que digas algo estúpido o cometas algún error grave. Resultó que su seudónimo se hizo muy famoso y en 2019 [incluso consiguió una subvención para el desarrollo](https://twitter.com/spiralbtc/status/1204815615678177280), lo que es en sí mismo un testimonio de la naturaleza sin permiso de Bitcoin.


Podría decirse que el seudónimo más conocido de Bitcoin es Satoshi Nakamoto. No está claro por qué eligió ser seudónimo, pero en retrospectiva probablemente fue una buena decisión por múltiples razones:


- Como muchos especulan con que Nakamoto posee una gran cantidad de Bitcoin, es imperativo para su seguridad financiera y personal mantener su identidad en el anonimato.
- Al desconocerse su identidad, no hay posibilidad de procesar a nadie, lo que da a las diversas autoridades gubernamentales un tiempo Hard.
- No hay ninguna persona autoritaria a la que admirar, lo que hace que la Bitcoin sea más meritocrática y resistente al chantaje.


Nótese que estos puntos no sólo son válidos para Satoshi Nakamoto, sino para cualquiera que trabaje en Bitcoin o posea cantidades significativas de la moneda, en diversos grados.


### Criptografía de selección


Los desarrolladores de código abierto suelen utilizar bibliotecas de código abierto desarrolladas por otras personas. Se trata de una parte natural e increíble de cualquier ecosistema saludable. Pero el software Bitcoin maneja dinero real y, en vista de ello, los desarrolladores tienen que ser muy cuidadosos a la hora de elegir de qué bibliotecas de terceros deben depender.


En una [charla sobre criptografía] filosófica (https://btctranscripts.com/greg-maxwell/2015-04-29-gmaxwell-Bitcoin-selection-cryptography/), Gregory Maxwell quiere redefinir el término "criptografía", que considera demasiado restringido. Él explica que fundamentalmente *la información quiere ser libre*, y hace su definición de criptografía basada en eso:


> La criptografía es el arte y la ciencia que utilizamos para luchar contra la naturaleza fundamental de la información, para doblegarla a nuestra voluntad política y moral, y para dirigirla hacia fines humanos contra todo azar y esfuerzo por oponerse a ella.

A continuación introduce el término *criptografía de selección*, referido como el arte de seleccionar herramientas criptográficas, y explica por qué es una parte importante de la criptografía. Gira en torno a cómo seleccionar bibliotecas, herramientas y prácticas criptográficas, o como él dice "el criptosistema de seleccionar criptosistemas".


Utilizando ejemplos concretos, muestra cómo la criptografía de selección puede salir terriblemente mal con facilidad, y también propone una lista de preguntas que podrías hacerte al practicarla. A continuación presentamos una versión resumida de esa lista:


- ¿El software está pensado para sus fines?
- ¿Se toman en serio las consideraciones criptográficas?
- ¿Cuál es el proceso de revisión? ¿Existe?
- ¿Cuál es la experiencia de los autores?
- ¿Está documentado el software?
- ¿Es portátil el programa?
- ¿Se ha probado el software?
- ¿Adopta el software las mejores prácticas?


Aunque ésta no es la guía definitiva para el éxito, puede ser muy útil repasar estos puntos a la hora de hacer criptografía de selección.


Debido a los problemas mencionados anteriormente por Maxwell, Bitcoin Core intenta realmente Hard [minimizar su exposición a librerías de terceros](https://github.com/Bitcoin/Bitcoin/blob/master/doc/dependencies.md). Por supuesto, no puedes erradicar todas las dependencias externas, de lo contrario tendrías que escribir todo por ti mismo, desde el renderizado de fuentes hasta la implementación de llamadas al sistema.


### Consulte



Esta sección se llama "Revisión", en lugar de "Revisión del código", porque la seguridad de Bitcoin se basa en gran medida en la revisión a múltiples niveles, no sólo del código fuente. Además, diferentes ideas requieren una revisión a diferentes niveles: un cambio en las reglas de consenso requeriría una revisión más profunda a más niveles en comparación con un cambio en el esquema de colores o la corrección de un error tipográfico.


En su camino hacia la adopción final, una idea suele pasar por varias fases de debate y revisión. A continuación se enumeran algunas de ellas:



- Se ha publicado una idea en la lista de correo Bitcoin-dev
- La idea se formaliza en una Propuesta de Mejora Bitcoin (BIP)
- El BIP se implementa en una solicitud de pull (PR) a Bitcoin Core
- Se debaten los mecanismos de despliegue
- Algunos mecanismos de despliegue competidores se implementan en pull requests a Bitcoin Core
- Las pull requests se fusionan con la rama maestra
- Los usuarios eligen si utilizar el programa o no


En cada una de estas fases, personas con distintos puntos de vista y formación revisan la información disponible, ya sea el código fuente, un BIP o simplemente una idea descrita vagamente. Las fases no suelen realizarse de manera estrictamente descendente; de hecho, pueden darse varias fases simultáneamente, y a veces se pasa de una a otra. También es posible que diferentes personas aporten su opinión durante las distintas fases.


Uno de los más prolíficos revisores de código en Bitcoin Core es Jon Atack. Él escribió [una entrada de blog](https://jonatack.github.io/articles/how-to-review-pull-requests-in-Bitcoin-core) sobre cómo revisar pull requests en Bitcoin Core. Hace hincapié en que un buen revisor de código se centra en la mejor manera de añadir valor.


> Como recién llegado, el objetivo es intentar aportar valor, con amabilidad y humildad, mientras se aprende todo lo posible.
>

> Un buen enfoque es hacer que no se trate de ti, sino de "¿Cómo puedo servir mejor?"

Destaca el hecho de que la revisión es un factor realmente limitante en Bitcoin Core. Muchas buenas ideas se quedan atascadas en un limbo donde no se produce ninguna revisión, pendientes. Observa que la revisión no sólo es beneficiosa para Bitcoin, sino también una excelente manera de aprender sobre el software y, al mismo tiempo, aportarle valor. La regla general de Atack es revisar de 5 a 15 PRs antes de hacer tu propio PR. De nuevo, debes centrarte en cómo servir mejor a la comunidad, no en cómo conseguir que tu propio código se fusione. Además, subraya la importancia de realizar la revisión en el nivel adecuado: ¿es el momento de corregir errores tipográficos o el desarrollador necesita una revisión más conceptual? Jon Attack añade:


> Una primera pregunta útil al comenzar una revisión puede ser: "¿Qué es lo que más se necesita aquí en este momento?" Responder a esta pregunta requiere experiencia y contexto acumulado, pero es una pregunta útil para decidir cómo se puede aportar el máximo valor en el menor tiempo posible.

La segunda mitad del artículo contiene orientaciones técnicas prácticas sobre cómo realizar la revisión y proporciona enlaces a documentación importante que puede consultarse.


La desarrolladora de Bitcoin Core y revisora de código Gloria Zhao ha escrito [un artículo](https://github.com/glozow/Bitcoin-notes/blob/master/review-checklist.md) con las preguntas que suele hacerse durante una revisión. También explica lo que considera una buena revisión:


> Personalmente, creo que una buena crítica es aquella en la que me he planteado muchas preguntas concretas sobre el RP y he quedado satisfecho con las respuestas
a ellas. [...] Naturalmente, empiezo con preguntas conceptuales, luego preguntas relacionadas con el enfoque y, por último, preguntas sobre la implementación. En general, personalmente creo que es inútil dejar comentarios relacionados con la sintaxis de C++ en un borrador de PR, y me sentiría mal volviendo a "¿esto tiene sentido?" después de que el autor haya respondido a más de 20 de mis sugerencias sobre la organización del código.


Su idea de que una buena revisión debe centrarse en lo que más se necesita en un momento determinado coincide con los consejos de Jon Atack. Ella

propone una lista de preguntas que puedes hacerte en los distintos niveles del proceso de revisión, pero subraya que esta lista no es en modo alguno exhaustiva ni una receta directa. La lista se ilustra con ejemplos reales de GitHub.


### Financiación



Mucha gente trabaja con el desarrollo de código abierto de Bitcoin, ya sea para Bitcoin Core o para otros proyectos. Muchos lo hacen en su tiempo libre sin recibir ninguna compensación, pero algunos desarrolladores también cobran por hacerlo.


Las empresas, individuos y organizaciones interesados en el éxito continuado de Bitcoin pueden donar fondos a los desarrolladores, ya sea directamente o a través de organizaciones que, a su vez, distribuyen los fondos a desarrolladores individuales. También hay una serie de empresas centradas en Bitcoin que contratan a desarrolladores cualificados para que trabajen a tiempo completo en Bitcoin.


### Choque cultural



A veces la gente tiene la impresión de que entre los desarrolladores de Bitcoin hay muchas luchas internas e interminables debates acalorados, y que son incapaces de tomar decisiones.


Por ejemplo, el mecanismo de despliegue de Taproot, se debatió durante un largo periodo de tiempo en el que se formaron dos "bandos". Uno quería "suspender" la actualización si los mineros no habían votado abrumadoramente a favor de las nuevas reglas a partir de un determinado momento, mientras que el otro quería aplicar las reglas a partir de ese momento pasara lo que pasara. Michael Folkson resume los argumentos de los dos bandos en un [email](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-February/018380.html) a la lista de correo Bitcoin-dev.


El debate parecía interminable y no se vislumbraba un consenso a corto plazo. Esto hizo que la gente se frustrara y, como resultado, se intensificó el calor. A Gregory Maxwell (como usuario nullc) le preocupaba [en Reddit](https://www.reddit.com/r/Bitcoin/comments/hrlpnc/technical_taproot_why_activate/fyqbn8s/?utm_source=share&utm_medium=web2x&context=3) que las largas discusiones hicieran que la actualización fuera menos segura:


> En esta coyuntura, la espera adicional no añade más revisión y certidumbre. Por el contrario, el retraso adicional está minando la inercia y aumentando potencialmente el riesgo en cierta medida, ya que la gente empieza a olvidar detalles, retrasa el trabajo sobre el uso posterior (como la compatibilidad con Wallet) y no invierte tanto esfuerzo de revisión adicional como el que invertiría si se sintiera segura sobre el plazo de activación.

Finalmente, esta disputa se resolvió gracias a una nueva propuesta de David Harding y Russel O'Connor llamada Speedy Trial, que implicaba un periodo de señalización comparativamente más corto para que los mineros bloquearan la activación de Taproot, o fail fast. Si lo activaban durante ese periodo de tiempo, el Taproot se desplegaría aproximadamente 6 meses después.


Alguien que no esté acostumbrado al proceso de desarrollo de Bitcoin probablemente pensaría que estos acalorados debates tienen muy mala pinta e incluso son tóxicos. Hay al menos dos factores que los hacen parecer malos, a ojos de algunas personas:



- En comparación con las empresas de código cerrado, todos los debates se producen en abierto, sin editar. Una empresa de software como Google nunca dejaría que sus empleados debatieran abiertamente sobre las características propuestas; de hecho, como mucho publicaría una declaración sobre la postura de la empresa al respecto. Esto hace que las empresas parezcan más armónicas en comparación con Bitcoin.
- Como Bitcoin no necesita permisos, cualquiera puede expresar su opinión. Esto es fundamentalmente diferente de una empresa de código cerrado que tiene un puñado de personas con una opinión, por lo general personas de ideas afines. La plétora de opiniones expresadas en Bitcoin es sencillamente asombrosa en comparación con, por ejemplo, PayPal.


La mayoría de los desarrolladores de Bitcoin argumentarían que esta apertura propicia un entorno bueno y saludable, e incluso que es necesaria para producir el mejor resultado.


Como se insinuó en el capítulo Amenaza, el segundo punto anterior puede ser muy beneficioso, pero tiene un inconveniente. Un atacante podría utilizar tácticas dilatorias, como las descritas en el [Manual de Campo de Sabotaje Simple](https://www.gutenberg.org/ebooks/26184), para distorsionar la toma de decisiones y el proceso de desarrollo.


Otra cosa que vale la pena mencionar es que, puesto que Bitcoin es dinero y Bitcoin Core asegura cantidades insondables de dinero, la seguridad en este contexto no se toma a la ligera. Por eso, el experimentado Bitcoin Core

los desarrolladores pueden parecer muy Hard cabezas huecas, actitud que suele estar justificada. De hecho, una función con una lógica débil detrás no va a ser aceptada. Lo mismo ocurriría si rompiera el

construcciones reproducibles, añadido nuevas dependencias, o si el código no seguía las [mejores prácticas] de Bitcoin (https://github.com/Bitcoin/Bitcoin/blob/master/doc/developer-notes.md).


Los nuevos (y viejos) desarrolladores pueden sentirse frustrados por esto. Pero, como es habitual en el software de código abierto, siempre puedes Fork el repositorio, fusionar lo que quieras a tu propio Fork, y construir y ejecutar tu propio binario.


### Conclusión sobre el código abierto


Bitcoin Core y la mayoría del software de Bitcoin es de código abierto, lo que significa que cualquiera es libre de distribuir, modificar y utilizar el software como quiera. El repositorio de Bitcoin Core en GitHub es actualmente el punto focal del desarrollo de Bitcoin, pero ese estatus puede cambiar si la gente empieza a desconfiar de sus mantenedores, o del propio sitio web.


El código abierto permite el desarrollo sin permisos en y sobre Bitcoin. Tanto si escribes código como si revisas código o protocolos, el código abierto es lo que te permite hacerlo, seudónomamente o no.


El proceso de desarrollo en torno a Bitcoin es radicalmente abierto, lo que puede hacer que Bitcoin parezca un lugar tóxico e ineficiente, pero eso es lo que mantiene a Bitcoin resistente frente a los actores maliciosos.


## Escala

<chapterId>bb3f3924-202c-5cdd-b2e9-e0c1cab0e48e</chapterId>



![](assets/scaling-banner.webp)



En este capítulo analizaremos cómo se amplía y cómo no se amplía Bitcoin. Empezaremos viendo cómo se ha razonado sobre el escalado en el pasado. A continuación, la mayor parte de este capítulo explica varios enfoques para escalar Bitcoin, concretamente el escalado vertical, horizontal, hacia dentro y por capas. Cada descripción va seguida de consideraciones sobre si el enfoque interfiere con la propuesta de valor de Bitcoin.


En el espacio Bitcoin, distintas personas atribuyen diferentes definiciones a la palabra "escala". Algunos la conciben como el aumento de la capacidad de transacción de Blockchain, otros creen que equivale a utilizar Blockchain de forma más eficiente y otros la ven como el desarrollo de sistemas sobre Bitcoin.


En el contexto de Bitcoin, y para los propósitos de este libro, definimos escalar como *aumentar la capacidad de uso de Bitcoin sin comprometer su resistencia a la censura*. Esta definición abarca varios aspectos

tipos de cambios, por ejemplo:


- Menor consumo de bytes en las transacciones
- Mejora del rendimiento de la verificación de firmas
- Hacer que la red peer-to-peer utilice menos ancho de banda
- Dosificación de transacciones
- Arquitectura por capas


Pronto nos adentraremos en los distintos enfoques de la ampliación, pero empecemos con un breve repaso de la historia de Bitcoin en el contexto de la ampliación.


### Historia del escalado



El escalado ha sido un punto central de discusión desde la Genesis de Bitcoin. La primera frase del [primer correo electrónico](https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) en respuesta al anuncio de Satoshi del libro blanco de Bitcoin en la lista de correo de Criptografía trataba, de hecho, sobre el escalado:


> Satoshi Nakamoto escribió:
>

> "He estado trabajando en un nuevo sistema de dinero electrónico que es totalmente peer-to-peer, sin terceros de confianza.  El documento está disponible en http://www.Bitcoin.org/Bitcoin.pdf"
>

> Necesitamos urgentemente un sistema de este tipo, pero por lo que veo en su propuesta, no parece tener el tamaño necesario.

Puede que la conversación en sí no sea muy interesante ni precisa, pero demuestra que el escalado ha sido una preocupación desde el principio.


Los debates sobre el escalado alcanzaron su máximo interés en torno a 2015-2017, cuando circularon muchas ideas diferentes sobre si aumentar el límite máximo de tamaño de bloque y cómo hacerlo. Se trataba de un debate poco interesante sobre el cambio de un parámetro en el código fuente, un cambio que no solucionaba nada en esencia pero que empujaba el problema del escalado hacia el futuro, generando deuda técnica.


En 2015, se celebró en Montreal una conferencia llamada [Scaling Bitcoin](https://scalingbitcoin.org/), con una conferencia de seguimiento seis meses después en Hong Kong y, posteriormente, en otros lugares del mundo. El tema central era precisamente cómo escalar Address. Muchos desarrolladores de Bitcoin y otros entusiastas se reunieron en estas conferencias para debatir diversas cuestiones y propuestas de escalado. La mayoría de estas discusiones no giraban en torno al aumento del tamaño de los bloques, sino sobre soluciones a más largo plazo.


Tras la conferencia de Hong Kong, en diciembre de 2015, Gregory Maxwell [resumió su punto de vista](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-December/011865.html) sobre muchas de las cuestiones que se habían debatido, empezando por cierta filosofía general del escalado:


> Con la tecnología disponible, hay compensaciones fundamentales entre escala y descentralización. Si el sistema es demasiado costoso, la gente se verá obligada a confiar en terceros en lugar de aplicar de forma independiente las reglas del sistema. Si el uso de recursos de Bitcoin, en relación con la tecnología disponible, es demasiado grande, Bitcoin pierde sus ventajas competitivas frente a los sistemas heredados porque la validación será demasiado costosa (expulsando a muchos usuarios), lo que obligará a volver a confiar en el sistema.  Si la capacidad es demasiado baja y nuestros métodos de transacción demasiado ineficaces, el acceso a la cadena para la resolución de disputas será demasiado costoso, lo que también devolverá la confianza al sistema.

Habla del equilibrio entre rendimiento y descentralización. Si se permiten bloques más grandes, se expulsará a algunas personas de la red porque ya no dispondrán de recursos para validar los bloques. Pero, por otro lado, si el acceso al espacio de bloques se encarece, menos gente podrá permitirse utilizarlo como mecanismo de resolución de disputas. En ambos casos, los usuarios se ven empujados hacia servicios de confianza.


Continúa resumiendo los numerosos enfoques de escalado presentados en la conferencia. Entre ellas se encuentran verificaciones de firmas más eficientes desde el punto de vista computacional, *testigo segregado* que incluye un cambio en el límite de tamaño de los bloques, un mecanismo de propagación de bloques más eficiente desde el punto de vista espacial y la construcción de protocolos por capas sobre Bitcoin. Muchas de estas

desde entonces.


### Planteamientos a escala



Como ya se ha indicado, la ampliación de Bitcoin no consiste necesariamente en aumentar el límite de tamaño de bloque u otros límites. Ahora repasamos algunos enfoques generales para el escalado, algunos de los cuales no sufren la disyuntiva rendimiento-descentralización mencionada en la sección anterior.


#### Escala vertical



El escalado vertical es el proceso de aumentar los recursos informáticos de las máquinas que procesan los datos. En el contexto de Bitcoin, estas últimas serían los nodos completos, es decir, las máquinas que validan la Blockchain en nombre de sus usuarios.


La técnica más discutida para el escalado vertical en Bitcoin es el aumento del límite de tamaño de los bloques. Esto requeriría que algunos nodos completos actualizasen su hardware para estar a la altura de las crecientes demandas computacionales. El inconveniente es que se produce a costa de la centralización.


Además de los efectos negativos sobre la descentralización de Full node, el escalado vertical también podría afectar negativamente a la descentralización y seguridad de Mining de formas menos obvias. Veamos cómo "deberían" operar los mineros. Supongamos que un Miner mina un bloque a la altura 7 y publica ese bloque en la red Bitcoin. Este bloque tardará algún tiempo en alcanzar una amplia aceptación, lo que se debe principalmente a dos factores:


- La transferencia del bloque entre pares lleva tiempo debido a las limitaciones del ancho de banda.
- La validación del bloque lleva tiempo.


Mientras el bloque 7 se propaga por la red, muchos mineros todavía están Mining sobre el bloque 6 porque aún no han recibido y validado el bloque 7. Durante este tiempo, si alguno de estos mineros encuentra un nuevo bloque a la altura 7, habrá dos bloques compitiendo a esa altura. Sólo puede haber un bloque en la altura 7 (o en cualquier otra altura), lo que significa que uno de los dos candidatos debe quedar obsoleto.


En resumen, los bloques obsoletos se producen porque cada bloque tarda tiempo en propagarse, y cuanto más tarda la propagación, mayor es la probabilidad de que se produzcan bloques obsoletos.


Supongamos que se suprime el límite de tamaño de los bloques y que el tamaño medio de los bloques aumenta considerablemente. En ese caso, los bloques se propagarían más lentamente por la red debido a las limitaciones de ancho de banda y al tiempo de verificación. Un aumento del tiempo de propagación también aumentará las posibilidades de que se produzcan bloques obsoletos.


A los mineros no les gusta que sus bloques se bloqueen porque perderían su Block reward, así que harán todo lo posible para evitarlo

escenario. Entre las medidas que pueden adoptar figuran:



- Aplazamiento de la validación de un bloque entrante, también conocido como *Mining sin validación*. Los mineros pueden comprobar la Proof-of-Work de la cabecera del bloque y minar sobre ella, mientras descargan el bloque completo y lo validan.
- Conexión a una Mining pool con mayor ancho de banda y conectividad.


La Mining sin validación socava aún más la descentralización de la Full node, ya que la Miner recurre a confiar en los bloques entrantes, al menos temporalmente. También perjudica en cierta medida a la seguridad, ya que una parte de la potencia de cálculo de la red se basa potencialmente en una Blockchain no válida, en lugar de hacerlo en la cadena más sólida y válida.


El segundo punto tiene un efecto negativo en la descentralización de Miner, porque normalmente los pools con la mejor conectividad de red y ancho de banda son también los más grandes, lo que hace que los mineros graviten hacia unos pocos pools grandes.


#### Escala horizontal



El escalado horizontal se refiere a las técnicas que dividen la carga de trabajo entre varias máquinas. Aunque se trata de un método de escalado habitual en sitios web y bases de datos populares, no es fácil de aplicar en Bitcoin.


Mucha gente se refiere a este enfoque de escalado de Bitcoin como *sharding*. Básicamente, consiste en dejar que cada Full node verifique sólo una parte de la Blockchain. Peter Todd ha reflexionado mucho sobre el concepto de fragmentación. Escribió un [artículo de blog](https://petertodd.org/2015/why-scaling-Bitcoin-with-sharding-is-very-Hard) explicando la fragmentación en términos generales, y también presentando su propia idea llamada *treechains*. El artículo es de difícil lectura, pero Todd expone algunos puntos que son bastante digeribles:


> En los sistemas fragmentados la "defensa Full node" no funciona, al menos directamente. La cuestión es que no todo el mundo tiene todos los datos, así que tienes que decidir qué pasa cuando no están disponibles.

A continuación, presenta varias ideas sobre cómo abordar el sharding, o escalado horizontal. Hacia el final del post concluye:


> Sin embargo, hay un gran problema: ¡santo Dios, lo anterior es complejo comparado con Bitcoin! Incluso la versión "infantil" de la fragmentación - mi esquema de linealización en lugar de zk-SNARKS - es probablemente uno o dos órdenes de magnitud más complejo que el uso del protocolo Bitcoin en este momento, sin embargo, en este momento un gran % de las empresas en este espacio parecen haber tirado las manos y utilizar proveedores de API centralizadas en su lugar. Poner en práctica lo anterior y ponerlo en manos de los usuarios finales no será fácil.
>

> Por otra parte, la descentralización no es barata: utilizar PayPal es uno o dos órdenes de magnitud más sencillo que el protocolo Bitcoin.

La conclusión a la que llega es que la fragmentación *podría* ser técnicamente posible, pero a costa de una enorme complejidad. Dado que muchos usuarios ya consideran Bitcoin demasiado complejo y prefieren utilizar servicios centralizados, va a ser Hard convencerles de que utilicen algo aún más complejo.


#### Escalado hacia el interior



Mientras que el escalado horizontal y vertical han funcionado históricamente bien en sistemas centralizados como bases de datos y servidores web, no parecen adecuados para una red descentralizada como Bitcoin debido a sus efectos centralizadores.


Un enfoque que se valora demasiado poco es lo que podemos llamar *inward scaling*, que se traduce como "hacer más con menos". Se refiere al trabajo constante que realizan muchos desarrolladores para optimizar los algoritmos ya existentes, de modo que podamos hacer más dentro de los límites actuales del sistema.


Las mejoras que se han conseguido gracias al escalado hacia el interior son, cuando menos, impresionantes. Para dar una idea general de las mejoras a lo largo de los años, Jameson Lopp [ha realizado pruebas comparativas](https://blog.lopp.net/Bitcoin-core-performance-evolution/) sobre la sincronización de Blockchain, comparando muchas versiones diferentes de Bitcoin Core remontándose a la versión 0.8.


![](assets/Bitcoin-Core-Sync-Performance-1.webp)


Rendimiento inicial de descarga de bloques de varias versiones de Bitcoin Core. En el eje Y se muestra la altura del bloque sincronizado y en el eje X el tiempo que tardó en sincronizarse a esa altura


Las distintas líneas representan diferentes versiones de Bitcoin Core. La línea de más a la izquierda es la más reciente, es decir, la versión 0.22, que se publicó en septiembre de 2021 y tardó 396 minutos en sincronizarse por completo. La de más a la derecha es la versión 0.8 de noviembre de 2013, que tardó 3452 minutos. Toda esta mejora -aproximadamente 10 veces- se debe al escalado hacia dentro.


Las mejoras pueden clasificarse en ahorro de espacio (RAM, disco, ancho de banda, etc.) o ahorro de potencia de cálculo. Ambas categorías contribuyen a las mejoras del diagrama anterior.


Un buen ejemplo de mejora computacional puede encontrarse en la biblioteca [libsecp256k1](https://github.com/Bitcoin-core/secp256k1), que, entre otras cosas, implementa las primitivas criptográficas necesarias para realizar y verificar firmas digitales. Pieter Wuille es uno de los contribuyentes a esta biblioteca, y escribió un [hilo de Twitter](https://twitter.com/pwuille/status/1450471673321381896) mostrando las mejoras de rendimiento logradas a través de varias pull requests.


![](assets/libsecp256k1speedups.webp)


Rendimiento de la verificación de firmas a lo largo del tiempo, con pull requests significativas marcadas en la línea de tiempo


El gráfico muestra la tendencia para dos tipos diferentes de CPU de 64 bits, a saber, ARM y x86. La diferencia de rendimiento se debe a las instrucciones más especializadas disponibles en x86 en comparación con la arquitectura ARM, que tiene menos instrucciones y más genéricas. Sin embargo, la tendencia general es la misma para ambas arquitecturas. Tenga en cuenta que el eje Y es logarítmico, lo que hace que las mejoras parezcan menos impresionantes de lo que realmente son.


También hay varios buenos ejemplos de mejoras para ahorrar espacio que contribuyeron a aumentar el rendimiento. En un

[Medium blog post](https://murchandamus.medium.com/2-of-3-Multisig-inputs-using-Pay-to-Taproot-d5faf2312ba3) sobre la contribución de Taproot al ahorro de espacio, el usuario Murch compara cuánto espacio de bloque requeriría una firma de umbral 2-de-3, utilizando Taproot de varias maneras, así como sin utilizarlo en absoluto.


![](assets/murch-taproot.webp)


Ahorro de espacio para distintos tipos de gastos, Taproot y versiones heredadas.


Un Multisig de 2 de 3 utilizando SegWit nativo requeriría un total de 104,5+43 vB = 147,5 vB, mientras que el uso más conservador del espacio de Taproot requeriría sólo 57,5+43 vB = 100,5 vB en el caso de uso estándar. En el peor de los casos y en raras ocasiones, como cuando un firmante estándar no está disponible por algún motivo, Taproot utilizaría 107,5+43 vB = 150,5 vB. No es necesario que entiendas todos los detalles, pero esto debería darte una idea de cómo piensan los desarrolladores a la hora de ahorrar espacio: cada pequeño byte cuenta.


Aparte del escalado hacia dentro en el software Bitcoin, hay algunas formas en que los usuarios pueden contribuir también al escalado hacia dentro. Pueden hacer sus transacciones de forma más inteligente para ahorrar en gastos de transacción y, al mismo tiempo, reducir su huella en los requisitos de Full node. Dos de las técnicas más utilizadas para lograr este objetivo son la agrupación de transacciones y la consolidación de resultados.


La idea con el procesamiento por lotes de transacciones es combinar varios pagos en una sola transacción, en lugar de hacer una transacción por pago. Esto puede ahorrarte muchas comisiones y, al mismo tiempo, reducir la carga de espacio en bloque.


![](assets/tx-batching.webp)


La agrupación de transacciones combina varios pagos en una sola transacción para ahorrar en comisiones.


La consolidación de salidas consiste en aprovechar los periodos de baja demanda de espacio en bloque para combinar varias salidas en una sola. Esto puede reducir el coste de la cuota más adelante, cuando tengas que realizar un pago mientras la demanda de espacio en bloque sea alta.


![](assets/utxo-consolidation.webp)


Consolidación de salida: Fusiona tus monedas en una gran moneda cuando las comisiones son bajas para ahorrar comisiones más adelante.


Puede que no resulte obvio cómo contribuye la consolidación de la salida al escalado hacia dentro. Al fin y al cabo, la cantidad total de datos de Blockchain aumenta incluso ligeramente con este método. No obstante, el conjunto UTXO, es decir, la base de datos que lleva la cuenta de quién posee qué monedas, se reduce porque se gastan más UTXOs de los que se crean. Esto alivia la carga que supone para los nodos completos mantener sus conjuntos UTXO.


Desgraciadamente, sin embargo, estas dos técnicas de *gestión UTXO* pueden ser perjudiciales para tu privacidad o la de tus beneficiarios. En el caso de la agrupación por lotes, cada beneficiario sabrá que todas las salidas agrupadas por lotes son de usted para otros beneficiarios (excepto posiblemente el cambio). En el caso de la consolidación de UTXO, usted revelará que las salidas que consolida pertenecen a la misma Wallet. Por lo tanto, es posible que tenga que elegir entre rentabilidad y privacidad.


#### Escalado por capas



El enfoque más impactante del escalado es probablemente la estratificación. La idea general que subyace a la estratificación es que un protocolo puede liquidar pagos entre usuarios sin añadir transacciones al Blockchain.


Un protocolo por capas comienza con dos o más personas que se ponen de acuerdo sobre una transacción de inicio que se pone en la Blockchain, como se ilustra en la siguiente figura.


![](assets/scaling-layer.webp)

Un protocolo Layer 2 típico sobre Bitcoin, Layer 1.


Cómo se crea esta transacción de inicio varía entre protocolos, pero un tema común es que los participantes crean una transacción de inicio sin firmar y una serie de transacciones de castigo pre-firmadas, que gastan la salida de la transacción de inicio de varias maneras. Posteriormente, la transacción inicial se firma completamente y se publica en Blockchain, y las transacciones de castigo pueden firmarse completamente y publicarse para castigar a una parte que se haya portado mal. Esto incentiva a los participantes a mantener sus promesas para que el protocolo pueda funcionar de forma Trustless.


Una vez que la transacción de inicio está en la Blockchain, el protocolo puede hacer lo que se supone que debe hacer. Por ejemplo, podría hacer pagos superrápidos entre participantes, implementar algunas técnicas de mejora de la privacidad o hacer scripts más avanzados que no serían compatibles con la Bitcoin Blockchain.


No vamos a detallar cómo funcionan los protocolos específicos, pero como puedes ver en la figura anterior, la Blockchain apenas se utiliza durante el ciclo de vida del protocolo. Toda la acción jugosa ocurre *off-chain*. Hemos visto cómo esto puede ser una victoria para la privacidad si se hace bien, pero también puede ser una ventaja para la escalabilidad.


En un [post de Reddit](https://www.reddit.com/r/Bitcoin/comments/438hx0/a_trip_to_the_moon_requires_a_rocket_with/) titulado "Un viaje a la Luna requiere un cohete con múltiples etapas o, de lo contrario, la ecuación del cohete se comerá tu almuerzo... meter a todo el mundo en un trebuchet al estilo de un coche de payaso y esperar el éxito está fuera de lugar", Gregory Maxwell explica por qué la estratificación es nuestra mejor oportunidad para conseguir que Bitcoin escale en órdenes de magnitud.


Comienza subrayando la falacia de considerar a Visa o Mastercard como los principales competidores de Bitcoin y destacando cómo aumentar el tamaño máximo de bloque es un mal enfoque para hacer frente a dicha competencia. A continuación, habla de cómo marcar una diferencia real mediante el uso de capas:


> Entonces... ¿Significa eso que Bitcoin no puede ser un gran ganador como tecnología de pagos? No. Pero para alcanzar el tipo de capacidad necesaria para atender las necesidades de pago del mundo debemos trabajar de forma más inteligente.
>

> Desde el principio, Bitcoin se diseñó para incorporar capas de forma segura a través de su capacidad de contratación inteligente (¿Qué, crees que se puso ahí sólo para que la gente se pusiera filosófica sobre "DAOs" sin sentido?). En efecto, utilizaremos el sistema Bitcoin como un juez robótico altamente accesible y perfectamente fiable, y llevaremos a cabo la mayor parte de nuestros negocios fuera de la sala del tribunal, pero realizaremos las transacciones de tal forma que, si algo sale mal, dispongamos de todas las pruebas y acuerdos establecidos, de modo que podamos confiar en que el tribunal robótico lo arreglará. (Geek sidebar: si esto te parece imposible, lee este antiguo post sobre el corte de transacciones)
>

> Esto es posible precisamente por las propiedades básicas de Bitcoin. Un sistema base censurable o reversible no es muy adecuado para construir sobre él un potente procesamiento de transacciones de Layer superior... y si el activo subyacente no es sólido, no tiene mucho sentido realizar transacciones con él en absoluto.

La analogía con la jueza es bastante ilustrativa de cómo funciona la estratificación: esta jueza debe ser incorruptible y no cambiar nunca de opinión, de lo contrario las capas por encima de la Bitcoin de base no funcionarán de forma fiable.


Continúa haciendo una observación sobre los servicios centralizados. No suele haber ningún problema en confiar en un servidor central con cantidades triviales de Bitcoin para hacer las cosas: eso también es escalado por capas.


Han pasado muchos años desde que Maxwell escribió el artículo anterior, y sus palabras siguen siendo correctas. El éxito de la Lightning Network demuestra que la superposición de capas es una forma de aumentar la utilidad de la Bitcoin.



### Conclusión sobre la ampliación



Hemos discutido varias maneras a través de las cuales uno podría querer escalar Bitcoin, aumentar la capacidad de uso de Bitcoin. El escalado ha sido una preocupación en Bitcoin desde sus primeros días.


Hoy sabemos que Bitcoin no escala bien verticalmente ("comprar hardware más grande") ni horizontalmente ("verificar sólo partes de los datos"), sino más bien hacia dentro ("hacer más con menos") y en capas ("construir protocolos sobre Bitcoin").


## Cuando la mierda golpea el ventilador

<chapterId>fe39c13c-310f-51fd-84ff-6b92dd01c9e7</chapterId>



![](assets/shtf-banner.webp)

Bitcoin está construido por personas. La gente escribe el software y la gente lo ejecuta. Cuando se descubre una vulnerabilidad de seguridad o un fallo grave -¿hay realmente una distinción entre ambos? - siempre lo descubren personas de carne y hueso. Este capítulo contempla lo que la gente hace, debe y no debe hacer cuando la mierda golpea el ventilador. La primera sección explica el término *revelación responsable*, que se refiere a cómo alguien que descubre una vulnerabilidad puede actuar de forma responsable para ayudar a minimizar los daños derivados de ella. El resto del capítulo hace un recorrido por algunas de las vulnerabilidades más graves descubiertas a lo largo de los años, y cómo fueron tratadas por desarrolladores, mineros y usuarios. Las cosas no eran tan rigurosas en los inicios de Bitcoin como lo son hoy.


### Divulgación responsable



Imagina que descubres un bug en Bitcoin Core, un bug que permite a cualquiera apagar remotamente un nodo Bitcoin Core usando algunos mensajes de red especialmente diseñados. Imagina también que no eres malicioso y que te gustaría que este problema permaneciera sin explotar. ¿Qué haría usted? Si guarda silencio al respecto, es probable que otra persona descubra el problema, y no puede estar seguro de que esa persona no sea malintencionada.


Cuando se descubre un problema de seguridad, la persona que lo descubre debe emplear _revelación responsable_ que es un término usado a menudo entre los desarrolladores de Bitcoin. El término está [explicado en Wikipedia](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure):


> Los desarrolladores de hardware y software suelen necesitar tiempo y recursos para reparar sus errores. A menudo, son los hackers éticos los que encuentran estos
vulnerabilidades. Los piratas informáticos y los especialistas en seguridad informática opinan que es su responsabilidad social dar a conocer al público las vulnerabilidades. Ocultar los problemas podría causar una sensación de falsa seguridad. Para evitarlo, las partes implicadas se coordinan y negocian un plazo razonable para reparar la vulnerabilidad. Dependiendo del impacto potencial de la vulnerabilidad, del tiempo que se prevea necesario para desarrollar y aplicar una solución de emergencia o workaround y de otros factores, este plazo puede variar entre unos pocos días y varios meses.


Esto significa que si encuentra un problema de seguridad, debe informar de ello al equipo responsable del sistema. Pero, ¿qué significa esto en el contexto de Bitcoin? Nadie controla Bitcoin, pero actualmente existe un punto central para el desarrollo de Bitcoin, a saber, el [repositorio Github del núcleo de Bitcoin](https://github.com/Bitcoin/Bitcoin). Los mantenedores de dicho repositorio son responsables del código que contiene, pero no son responsables del sistema en su conjunto, nadie lo es. Sin embargo, la mejor práctica general es enviar un correo electrónico a security@bitcoincore.org.


En un [hilo de correo electrónico](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/015002.html) titulado "Divulgación responsable de errores" de 2017, Anthony Towns intentó resumir lo que él percibía como las mejores prácticas actuales. Había recogido aportaciones de varias fuentes y diferentes personas para fundamentar su punto de vista sobre el tema.




- Las vulnerabilidades deben notificarse a través de security at bitcoincore.org
- Un problema crítico (que puede ser explotado inmediatamente o que ya está siendo explotado causando grandes daños) será tratado por:
  - un parche liberado lo antes posible
  - amplia notificación de la necesidad de actualizar (o de desactivar los sistemas afectados)
  - divulgación mínima del problema real, para retrasar los ataques
- Una vulnerabilidad no crítica (porque es difícil o cara de explotar) será tratada por:
  - parcheo y revisión realizados en el flujo ordinario de desarrollo
  - retroportar una corrección o solución de la versión maestra a la versión actual publicada
- Los desarrolladores intentarán asegurarse de que la publicación de la solución no revele la naturaleza de la vulnerabilidad proporcionando la solución propuesta a desarrolladores experimentados que no hayan sido informados de la vulnerabilidad, diciéndoles que soluciona una vulnerabilidad y pidiéndoles que identifiquen la vulnerabilidad.
- Los desarrolladores pueden recomendar a otras implementaciones de Bitcoin que adopten correcciones de vulnerabilidades antes de que la corrección se publique y se extienda ampliamente, si pueden hacerlo sin revelar la vulnerabilidad; por ejemplo, si la corrección tiene beneficios de rendimiento significativos que justifiquen su inclusión.
- Antes de que una vulnerabilidad se haga pública, los desarrolladores suelen recomendar a los desarrolladores amigos de Altcoin que se pongan al día con las correcciones. Pero esto es sólo después de que las correcciones se despliegan ampliamente en la red Bitcoin.
- Por lo general, los desarrolladores no notificarán a los desarrolladores de Altcoin que se hayan comportado de forma hostil (por ejemplo, utilizando vulnerabilidades para atacar a otros, o que violen embargos).
- Los desarrolladores de Bitcoin no revelarán los detalles de la vulnerabilidad hasta que >80% de los nodos de Bitcoin hayan desplegado las correcciones. Se anima y pide a los descubridores de vulnerabilidades que sigan la misma política. [1] [6]


Esta lista muestra lo cuidadoso que hay que ser al publicar parches para Bitcoin, ya que el propio parche podría delatar la vulnerabilidad. El cuarto punto es especialmente interesante, ya que explica cómo comprobar si un parche se ha disimulado lo suficientemente bien. En efecto, si unos pocos desarrolladores realmente experimentados no pueden detectar la vulnerabilidad aun sabiendo que el parche corrige una, probablemente será realmente Hard difícil que otros la descubran.


El hilo que condujo a este correo electrónico estaba discutiendo si, cuándo y cómo revelar vulnerabilidades a altcoins y otras implementaciones de Bitcoin. Aquí no hay una respuesta clara. "Ayudar a los buenos" parece lo más sensato, pero ¿quién decide quiénes son y dónde está el límite? Bryan Bishop [argumentó](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014983.html) que ayudar a las altcoins e incluso a las scamcoins a defenderse de los exploits de seguridad era un deber moral:


> No basta con defender la Bitcoin y a sus usuarios de las amenazas activas, existe una responsabilidad más general de defender a todo tipo de usuarios y software diferente de muchos tipos de amenazas en cualquiera de sus formas, incluso si la gente está usando software estúpido e inseguro que tú personalmente no mantienes o al que no contribuyes o por el que no abogas. Manejar el conocimiento de una vulnerabilidad es un asunto delicado y podrías estar recibiendo conocimiento con un impacto directo o indirecto más serio que el descrito originalmente.

En la misma línea que el correo electrónico de Town, Gregory Maxwell publicó un [post](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014977.html) en el que sostenía que las vulnerabilidades de seguridad podrían ser más graves de lo que parecen:


> He visto muchas veces cómo un problema de Hard resultaba trivial cuando se encontraba el truco adecuado, o cómo un problema menor se convertía en algo mucho más serio.
>

> Unos simples fallos de rendimiento, implementados con pericia, pueden utilizarse para dividir la red: Miner A y Exchange B en una partición, todos los demás en otra... y duplicar el gasto.
>

> Y así sucesivamente.  Así que, aunque estoy totalmente de acuerdo en que cada cosa debe y puede tratarse de forma diferente, no siempre está tan claro. Es prudente tratar las cosas como más graves de lo que se sabe que son.

Por lo tanto, incluso si una vulnerabilidad parece Hard para explotar, podría ser mejor asumir que es fácilmente explotable y que simplemente no has descubierto cómo todavía.


También menciona que "es algo incorrecto llamar a este hilo algo sobre divulgación, este hilo no es sobre divulgación. Divulgación es cuando se lo dices al vendedor.  Este hilo trata sobre la publicación y eso tiene implicaciones muy diferentes. La publicación es cuando estás seguro de habérselo dicho a los posibles atacantes". Esta última observación sobre la distinción entre divulgación y publicación es importante. La parte fácil es la revelación responsable; la parte Hard es la publicación sensata.


### La infancia traumática de Bitcoin



Bitcoin comenzó como un proyecto de una sola persona (al menos eso es lo que sugiere el seudónimo de su creador), y Bitcoin tuvo inicialmente poco o ningún valor. Como tal, las vulnerabilidades y las correcciones de errores no se trataban con tanto rigor como ahora.


La wiki de Bitcoin tiene una [lista de vulnerabilidades y exposiciones comunes](https://en.Bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures) (CVEs) por las que ha pasado Bitcoin. Esta sección constituye una pequeña exposición de algunos de los problemas e incidentes de seguridad de los primeros años de Bitcoin. No los cubriremos todos, pero hemos seleccionado algunos que nos parecen especialmente interesantes.


#### 2010-07-28: Gastar las monedas de cualquiera (CVE-2010-5141)



El 28 de julio de 2010, un seudónimo llamado ArtForz descubrió un error en la versión 0.3.4 que permitía a cualquiera coger monedas de cualquier otra persona. ArtForz *responsablemente* informó de ello a Satoshi Nakamoto y a otro desarrollador de Bitcoin llamado Gavin Andresen.


El problema era que el operador de script `OP_RETURN` simplemente salía de la ejecución del programa, así que si el scriptPubKey era `<pubkey> OP_CHECKSIG` y scriptSig era `OP_1 OP_RETURN`, la parte del programa en el scriptPubKey nunca se ejecutaría. Lo único que ocurriría sería que `1` se pusiera en la pila y entonces `OP_RETURN` provocaría la salida del programa. Cualquier valor distinto de cero en la parte superior de la pila después de que el programa se haya ejecutado significa que se cumple la condición de gasto. Dado que el elemento `1` de la parte superior de la pila es distinto de cero, el gasto sería correcto.


Este era el código para el manejo de `OP_RETURN`:


```
case OP_RETURN:
{
pc = pend;
}
break;
```

El efecto de `pc = pend;` era que el resto del programa se saltaba, lo que significaba que cualquier script de bloqueo en scriptPubKey sería ignorado. La solución consistió en cambiar el significado de `OP_RETURN` para que fallara inmediatamente.


```
case OP_RETURN:
{
return false;
}
break;
```


Satoshi hizo este cambio localmente y construyó un binario ejecutable con la versión 0.3.5 a partir de él. A continuación, publicó en el foro Bitcointalk `\*** ALERT \*** Upgrade to 0.3.5 ASAP`, instando a los usuarios a instalar esta versión binaria suya, sin presentar el código fuente de la misma:


> Por favor, actualice a 0.3.5 lo antes posible  Hemos corregido un error de implementación por el que era posible que se aceptaran transacciones falsas.  ¡No acepte transacciones Bitcoin como pago hasta que actualice a la versión 0.3.5!

El mensaje original fue editado posteriormente y ya no está disponible en su forma completa. El fragmento anterior procede de una [respuesta citada](https://bitcointalk.org/index.php?topic=626.msg6458#msg6458). Algunos usuarios probaron el binario de Satoshi, pero tuvieron problemas con él. Poco después, [Satoshi escribió](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469):


> Aún no he tenido tiempo de actualizar el SVN.  Espera a la 0.3.6, la estoy construyendo ahora.  Puedes apagar tu nodo mientras tanto.

Y 35 minutos después, [escribió](https://bitcointalk.org/index.php?topic=626.msg6480#msg6480):


> SVN se actualiza con la versión 0.3.6.
>

> Subiendo la versión Windows de 0.3.6 a Sourceforge ahora, luego reconstruiré linux.

En ese momento también parecía haber actualizado el post original para mencionar 0.3.6 en lugar de 0.3.5:


> Por favor, actualice a 0.3.6 lo antes posible  Hemos corregido un error de implementación por el que era posible que se mostraran transacciones falsas como aceptadas.  No acepte transacciones Bitcoin como pago hasta que actualice a la versión 0.3.6
>

> Si no puedes actualizar a 0.3.6 inmediatamente, es mejor que apagues tu nodo Bitcoin hasta que lo hagas.
>

> También en 0.3.6, hashing más rápido:
> - optimización de la caché midstate gracias a tcatm
> - Crypto++ ASM SHA-256 gracias a BlackEye
> Velocidad total de generación 2,4 veces superior.
>

> Descargar:
>

> http://sourceforge.net/projects/Bitcoin/files/Bitcoin/Bitcoin-0.3.6/
>

> Usuarios de Windows y Linux: si tienen la versión 0.3.5, deben actualizar a la 0.3.6.

Observe la diferencia en la caracterización del problema con respecto al primer mensaje: "podría aparecer como aceptado" frente a "podría ser aceptado". Quizá Satoshi restó importancia a la gravedad del fallo en su comunicación para no llamar demasiado la atención sobre el problema real. En cualquier caso, la gente actualizó a 0.3.6 y funcionó como se esperaba. Este problema en particular se resolvió, sorprendentemente, sin pérdidas de Bitcoin.


El mensaje de Satoshi también describía algunas optimizaciones de rendimiento para Mining. No está claro por qué se incluyó eso en una corrección de seguridad crítica, es posible que el propósito fuera ofuscar el verdadero problema. Sin embargo, parece más probable que simplemente publicara lo que había en la cabecera de la rama de desarrollo del repositorio de Subversion, con la corrección de seguridad añadida.


En aquella época, no había tantos usuarios como ahora, y el valor de la Bitcoin era casi nulo. Si esta respuesta a los bugs se llevara a cabo hoy en día, se consideraría una completa cagada por múltiples razones:



- Satoshi publicó una versión 0.3.5 sólo para binarios que contenía la corrección. No se proporcionó ningún parche ni código, tal vez como medida para ocultar el problema.
- 0.3,5 [ni siquiera funcionó](https://bitcointalk.org/index.php?topic=626.msg6455#msg6455).
- La corrección de la 0.3.6 era en realidad una Hard Fork.


Otra cosa discutible es si es bueno o malo que se pidiera a los usuarios que cerraran sus nodos. Esto no sería posible hoy en día, pero en aquella época muchos usuarios seguían activamente los foros en busca de actualizaciones y solían estar al tanto de todo. Dado que era posible hacerlo, podría haber sido una medida sensata.


#### 2010-08-15 Desbordamiento de salida combinado (CVE-2010-5139)



A mediados de agosto de 2010, el usuario del foro Bitcointalk jgarzik, alias Jeff Garzik,

[descubrió que](https://bitcointalk.org/index.php?topic=822.msg9474#msg9474) cierta transacción a la altura del bloque 74638 tenía dos salidas de valor inusualmente alto:


```
"out" : [
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0xB7A73EB128D7EA3D388DB12418302A1CBAD5E890 OP_EQUALVERIFY OP_CHECKSIG"
},
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0x151275508C66F89DEC2C5F43B6F9CBE0B5C4722C OP_EQUALVERIFY OP_CHECKSIG"
}
]
```


> El "valor de salida" en este bloque #74638 es bastante extraño:
>

> 92233720368.54277039 ¿BTC?  ¿Es UINT64_MAX, me pregunto?

Presumiblemente, había un error que provocaba que la suma de dos salidas int64 (no uint64, como suponía Garzik) se desbordara a un valor negativo -0,00997538 BTC. Cualquiera que fuera la suma de las entradas, la "suma" de las salidas sería menor, por lo que esta transacción sería correcta según el código de la época.


En este caso, el fallo se había revelado y publicado a través de un exploit real. Un desafortunado resultado de esto fue que se habían creado unos 2x92.000 millones de Bitcoin, lo que diluyó gravemente el Supply monetario de unos 3,7 millones de monedas que existía en ese momento.


En un hilo relacionado, [Satoshi publicó](https://bitcointalk.org/index.php?topic=823.msg9531#msg9531) que agradecería que la gente dejara de Mining (o *generar*, como lo llamaban entonces):


> Ayudaría que la gente dejara de generar.  Probablemente tendremos que rehacer una rama alrededor de la actual, y cuanto menos generate, más rápido será.
>

> Un primer parche estará en SVN rev 132.  Todavía no está subido.  Estoy empujando algunos otros cambios misc fuera del camino en primer lugar, entonces voy a subir el parche para esto.

Su plan era hacer un Soft Fork para invalidar transacciones como la que se comenta aquí, invalidando así los bloques (especialmente el bloque 74638) que contenían dichas transacciones. Menos de una hora después, confirmó un [parche en la revisión 132](https://sourceforge.net/p/Bitcoin/code/132/) del repositorio de Subversion y [publicó en el foro](https://bitcointalk.org/index.php?topic=823.msg9548#msg9548) describiendo lo que pensaba que debían hacer los usuarios:


> ¡Parche subido a SVN rev 132!
>

> Por ahora, pasos recomendados:
> 1) Apagar.
> 2) Descarga los archivos blk de knightmb.  (reemplaza tus archivos blk0001.dat y blkindex.dat)
> 3) Mejora.
> 4) Debería empezar con menos de 74000 bloques. Deja que vuelva a descargar el resto.
>

> Si no quieres usar los archivos de knightmb, podrías simplemente borrar tus archivos blk*.dat, pero va a ser mucha carga en la red si todo el mundo está descargando todo el índice de bloques a la vez.
>

> Construiré comunicados en breve.

Quería que la gente descargara datos de bloques de un usuario concreto, knightmb, que había publicado su Blockchain tal y como aparecía en su disco, los archivos blkXXXX.dat y blkindex.dat. La razón para descargar los datos de Blockchain de esta forma, en lugar de sincronizarlos desde cero, era reducir los cuellos de botella en el ancho de banda de la red.


Había una gran advertencia al respecto: los datos que los usuarios descargaban de knightmb [no eran verificados por el software Bitcoin](https://Bitcoin.stackexchange.com/a/113682/69518) al iniciarse. El archivo blkindex.dat contenía el conjunto UTXO, y el software aceptaba cualquier dato allí contenido como si ya lo hubiera verificado. knightmb podría haber manipulado los datos para darse a sí mismo o a cualquier otra persona algunos bitcoins.


Una vez más, la gente pareció estar de acuerdo, y la anulación del bloque inválido y sus sucesores fue un éxito. Los mineros empezaron a trabajar en un nuevo sucesor del bloque [74637](https://Mempool.space/block/0000000000606865e679308edf079991764d88e8122ca9250aef5386962b6e84) y, según el Timestamp del bloque, apareció un sucesor a las 23:53 UTC, unas 6 horas después de que se descubriera el problema. A las 08:10 del día siguiente, el 16 de agosto, en torno al bloque 74689, la nueva cadena había superado a la antigua, por lo que todos los nodos no actualizados se reorganizaron para seguir la nueva cadena. Se trata de la reorganización más profunda (52 bloques) en la historia de Bitcoin.


En comparación con el problema de OP_RETURN, este problema se trató de forma algo más limpia:


- No se publicará ningún parche sólo para binarios
- El software liberado funcionaba según lo previsto
- No Hard Fork


También se pidió a los usuarios que dejaran de utilizar Mining durante esta edición. Podemos discutir si es una buena idea o no, pero imagina que eres un Miner y estás convencido de que todos los bloques situados encima del bloque defectuoso acabarán siendo eliminados en una reorganización profunda: ¿por qué ibas a malgastar recursos en bloques Mining condenados al fracaso?


También podrías pensar que es un poco sospechoso hacer lo que sugiere Nakamoto y descargar la Blockchain, incluido el conjunto UTXO, de la unidad Hard de un tipo cualquiera. Si es así, tienes razón: es sospechoso. Pero, dadas las circunstancias, esta respuesta de emergencia fue sensata.


Hay una diferencia importante entre este caso y el anterior de OP_RETURN: este problema fue explotado en la naturaleza, y por lo tanto una solución podría hacerse más directa. En el caso de OP_RETURN, tuvieron que ofuscar la solución y hacer declaraciones públicas que no revelaban directamente cuál era el problema.


#### 2013-03-11 Problema con los bloqueos de la BD 0.7.2 - 0.8.0 (CVE-2013-3220)



En marzo de 2013 surgió un problema muy interesante y educativo. Al parecer, el Blockchain se había dividido (aunque en la cita siguiente se utiliza la palabra "Fork") después del bloque 225429. Los detalles de este incidente se [informaron en BIP50](https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki). El resumen dice:


> Se minó y difundió un bloque que tenía un número de entradas de transacciones totales mayor que el visto anteriormente. Los nodos Bitcoin 0.8 fueron capaces de manejarlo, pero algunos nodos Bitcoin pre-0.8 lo rechazaron, provocando una Fork inesperada de la Blockchain. La cadena pre-0.8 incompatible (de aquí en adelante, la cadena 0.8) tenía en ese momento alrededor del 60% de la potencia Mining Hash, lo que garantizaba que la división no se resolviera automáticamente (como habría ocurrido si la cadena pre-0.8 hubiera superado a la cadena 0.8 en trabajo total, obligando a los nodos 0.8 a reorganizarse a la cadena pre-0.8).
>

> Para restaurar una cadena canónica lo antes posible, BTCGuild y Slush degradaron sus nodos Bitcoin 0.8 a 0.7 para que sus pools también rechazaran el bloque más grande. De este modo, la mayoría del hashpower recayó en la cadena sin el bloque más grande, lo que provocó que los nodos 0.8 se reorganizaran y volvieran a la cadena anterior a 0.8.

La rápida actuación de los pools Mining BTCGuild y Slush fue imprescindible en esta emergencia. Consiguieron que la mayoría del poder de Hash se pasara a la rama anterior a 0.8 de la división, y así ayudaron a restablecer el consenso. Esto dio tiempo a los desarrolladores para encontrar una solución sostenible.


Lo que también es muy interesante en este asunto es que la versión 0.7.2 era incompatible consigo misma, como ocurría también con las versiones anteriores. Esto se explica en la sección [Root cause section of BIP50](https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki#root-cause):


> Con la configuración de bloqueo de BDB insuficientemente alta, implícitamente se había convertido en una regla de consenso de la red que determinaba la validez del bloque (aunque una
regla incoherente e insegura, ya que el uso del bloqueo podría variar de un nodo a otro).


En resumen, el problema es que el número de bloqueos de base de datos que el software Bitcoin Core necesita para verificar un bloque no es determinista. Un nodo puede necesitar X bloqueos mientras que otro puede necesitar X+1 bloqueos. Los nodos también tienen un límite en el número de bloqueos que puede aceptar Bitcoin. Si el número de bloqueos necesarios supera el límite, el bloque se considerará inválido. Así, si X+1 supera el límite pero no X, los dos nodos dividirán el Blockchain y no se pondrán de acuerdo sobre qué rama es válida.


La solución elegida, aparte de las medidas inmediatas adoptadas por las dos agrupaciones para restablecer el consenso, fue



- limitar los bloques tanto en tamaño como en bloqueos necesarios en la versión 0.8.1
- parchear las versiones antiguas (0.7.2 y algunas anteriores) con las mismas reglas nuevas, y aumentar el límite de bloqueo global.


Excepto en el caso del aumento del límite de bloqueo global mencionado en el segundo punto, estas normas se aplicaron temporalmente durante un periodo de tiempo predeterminado. El plan era eliminar estos límites una vez que la mayoría de los nodos se hubieran actualizado.


Esta Soft Fork redujo drásticamente el riesgo de fracaso del consenso, y unos meses más tarde, el 15 de mayo, las normas temporales se desactivaron de forma concertada en toda la red. Nótese que esta desactivación fue en efecto una Hard Fork, pero no fue polémica. Además, se publicó junto con la Fork Soft precedente, por lo que las personas que ejecutaban el software bifurcado Soft eran perfectamente conscientes de que le seguiría una Hard Fork. Por lo tanto, la gran mayoría de los nodos permanecieron en consenso cuando se activó la Hard Fork. Por desgracia, algunos nodos que no se actualizaron se perdieron en el proceso.


Cabe preguntarse si esto sería factible hoy en día. El panorama de Mining es más complejo hoy en día y, dependiendo del poder de Hash de cada lado de la división, podría ser Hard lanzar un parche como el de BIP50 con la suficiente rapidez. Probablemente sería Hard convencer a los mineros de la rama "equivocada" para que se desprendieran de sus recompensas por bloque.


#### BIP66



El PIF66 es interesante porque destaca la importancia de:



- buena selección criptográfica
- divulgación responsable
- despliegue sin revelar la vulnerabilidad
- Mining sobre bloques verificados


BIP66 fue una propuesta para hacer más estrictas las reglas de codificación de firmas en Bitcoin Script. La [motivación](https://github.com/Bitcoin/bips/blob/master/bip-0066.mediawiki#motivation) era poder analizar firmas con software o bibliotecas que no fueran OpenSSL e incluso versiones recientes de OpenSSL. OpenSSL es una librería para criptografía de propósito general que Bitcoin Core usaba en ese momento.


El BIP se activó el 4 de julio de 2015. Sin embargo, aunque lo anterior es cierto, el BIP66 también soluciona un problema mucho más grave que no se menciona en el BIP.


##### La vulnerabilidad



La divulgación completa de este asunto fue publicada el 28 de julio de 2015 por Pieter Wuille en un

[correo electrónico a la lista de correo Bitcoin-dev](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-July/009697.html):


> Hola a todos,
>

> Me gustaría dar a conocer una vulnerabilidad que descubrí en septiembre de 2014 y que dejó de ser explotable cuando se alcanzó el umbral del 95% de BIP66 a principios de este mes.
>

> Breve descripción:
>

> Una transacción especialmente diseñada podría haber bifurcado la Blockchain entre nodos:
>

> - uso de OpenSSL en sistemas de 32 bits y en sistemas Windows de 64 bits
> - uso de OpenSSL en sistemas que no sean Windows de 64 bits (Linux, OSX, ...)
> - uso de algunas bases de código no OpenSSL para el análisis sintáctico de firmas

El correo electrónico explica con más detalle cómo se descubrió el problema y, más exactamente, qué lo causó. Al final, presenta una cronología de los acontecimientos, y aquí reproduciremos algunos de los más importantes. Algunos de ellos, como ilustra la figura anterior, ya se han descrito.


![](assets/bip66-timeline-1.webp)


Cronología de los acontecimientos en torno a la BIP66. Los puntos en negro ya se han explicado.


##### Antes del descubrimiento



Sin que nadie lo supiera, el problema podría haberse resuelto con la ya desaparecida BIP62, que era una propuesta para reducir las posibilidades de maleabilidad de las transacciones. Entre los cambios propuestos en la BIP62 estaba el endurecimiento de las reglas de consenso para la codificación de firmas, o "codificación DER estricta". Pieter Wuille propuso algunos ajustes al BIP en julio de 2014, que habrían resuelto el problema:


> 2014-Jul-18: Para que las reglas de codificación de firmas de Bitcoin no dependieran del analizador sintáctico específico de OpenSSL, modifiqué la propuesta de BIP62 para que su estricto requisito de firmas DER también se aplicara a las transacciones de la versión 1. En aquel momento ya no se minaban firmas que no fueran DER en los bloques, por lo que se asumió que esto no tendría ningún impacto. Véase https://github.com/Bitcoin/bips/pull/90 y http://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2014-July/006299.html. Se desconocía en ese momento, pero si se hubiera implantado habría resuelto la vulnerabilidad.

Debido a la amplitud de este BIP, que abarcaba mucho más que la "codificación DER estricta", cambiaba constantemente y nunca llegó a implantarse. El BIP se retiró posteriormente porque Segregated Witness, BIP141, resolvía la maleabilidad de las transacciones de una forma diferente y más completa.


##### Tras el descubrimiento



OpenSSL publicó nuevas versiones de su software con parches que, si se hubieran utilizado en Bitcoin desde el principio, habrían resuelto el problema. Sin embargo, el uso de cualquier nueva versión de OpenSSL sólo en una nueva versión de Bitcoin Core empeoraría las cosas. Gregory Maxwell lo explica en otro [hilo de correo electrónico](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-January/007097.html) en enero de 2015:


> Mientras que para la mayoría de las aplicaciones suele ser aceptable rechazar de plano algunas firmas, Bitcoin es un sistema de consenso en el que todos los participantes deben estar generalmente de acuerdo sobre la validez o invalidez exacta de los datos de entrada.  En cierto sentido, la coherencia es más importante que la "corrección".
> [...]
> Los parches anteriores, sin embargo, sólo solucionan un síntoma del problema general: depender de software no diseñado o distribuido para uso consensuado (en particular OpenSSL) para un comportamiento normativo consensuado.  Por lo tanto, como mejora incremental, propongo un Soft-Fork específico para imponer pronto el cumplimiento estricto de la DER, utilizando un subconjunto de BIP62.

Señala que utilizar un código que no está pensado para su uso en sistemas de consenso plantea graves riesgos, y propone que Bitcoin implemente una codificación DER estricta. Este es un ejemplo muy claro de la importancia de una buena criptografía de selección.


Estos hechos podrían dar la impresión de que Gregory Maxwell conocía la vulnerabilidad que Pieter Wuille publicó más tarde, pero quería ayudar a colar una solución disfrazada de medida de precaución, sin llamar demasiado la atención sobre el problema real. Podría ser así, pero es pura especulación.


Entonces, como propuso Maxwell, se creó el BIP66 como un subconjunto del BIP62 que especificaba sólo la codificación DER estricta. Este BIP fue aparentemente ampliamente aceptado y desplegado en julio, aunque irónicamente se produjeron dos escisiones de Blockchain debido a *Mining sin validación*. Estas divisiones se discuten en la siguiente sección.


![](assets/bip66-timeline-2.webp)


Una de las principales conclusiones es que los PIF deben ser más o menos *atómicos*, es decir, lo suficientemente completos como para ofrecer algo útil o resolver un problema concreto, pero lo suficientemente pequeños como para permitir un amplio apoyo entre los usuarios. Cuantas más cosas se pongan en un PIF, menores serán las posibilidades de aceptación.


##### Divisiones por falta de validación Mining



Por desgracia, la historia del BIP66 no terminó ahí. Cuando se activó el BIP66, resultó bastante lioso porque algunos mineros no verificaron los bloques que intentaban ampliar. Esto se denomina Mining sin validación, o SPV-Mining (como en Simplified Payment Verification). Se envió un mensaje de alerta a los nodos Bitcoin con un enlace a [una página web que describe el problema](https://Bitcoin.org/en/alert/2015-07-04-spv-Mining):


> A primera hora de la mañana del 4 de julio de 2015, se alcanzó el umbral de 950/1000 (95%). Poco después, un pequeño Miner (parte del 5% no actualizado) minó un bloque no válido, como era de esperar. Desafortunadamente, resultó que aproximadamente la mitad de la tasa de Hash de la red era Mining sin validar completamente los bloques (llamado SPV Mining), y construyó nuevos bloques encima de ese bloque inválido.

La página de alerta indicaba a los usuarios que debían esperar 30 confirmaciones más de lo normal en caso de que estuvieran utilizando versiones anteriores de Bitcoin Core.


La división mencionada anteriormente se produjo en 2015-07-04 a las 02:10 UTC después de la altura del bloque [363730](https://Mempool.space/block/000000000000000006a320d752b46b532ec0f3f815c5dae467aff5715a6e579e). Este problema se resolvió a las 03:50 del mismo día, después de que se minaran 6 bloques no válidos. Desafortunadamente, el mismo problema volvió a ocurrir al día siguiente, es decir, el 2015-07-05 a las 21:50, pero esta vez la rama inválida solo duró 3 bloques.


![](assets/bip66-timeline-3.webp)

Los acontecimientos que condujeron a la BIP66, su despliegue y sus consecuencias son un buen ejemplo de lo cuidadosos que deben ser los desarrolladores de Bitcoin. Algunas conclusiones clave de BIP66:



- El equilibrio entre la apertura y la no publicación de una vulnerabilidad es delicado.
- El despliegue de correcciones para vulnerabilidades no publicadas es un juego complicado.
- El consenso de retención es Hard.
- Los programas informáticos no destinados a sistemas de consenso suelen ser arriesgados.
- Los PIF deben ser algo atómicos.


### Conclusión sobre When Shit Hits The Fan



Bitcoin tiene fallos. Se anima a las personas que descubran fallos a que los comuniquen responsablemente a los desarrolladores de Bitcoin, para que puedan corregirlos sin revelarlos públicamente. En el mejor de los casos, la corrección del fallo se puede disfrazar como una mejora del rendimiento, o alguna otra cortina de humo.


Hemos analizado algunos de los problemas más graves que han surgido a lo largo de los años y cómo se gestionaron. Algunos se descubrieron públicamente a través de exploits, mientras que otros se divulgaron de forma responsable y pudieron solucionarse antes de que los actores maliciosos tuvieran la oportunidad de explotarlos.


## Preguntas para el debate

<chapterId>91462ca7-f09c-55da-a5b9-3e211de31da5</chapterId>


Estas preguntas de debate no son sólo una recapitulación del contenido de "Bitcoin filosofía del desarrollo", sino que pretenden animarte a investigar más, así que asegúrate de salir y explorar.


Puedes poner a prueba la profundidad de tu comprensión escribiendo [mini-ensayo](https://www.youtube.com/watch?v=N4YjXJVzoZY) de 100-300 palabras eligiendo el tema en este grupo de preguntas. Si quieres recibir comentarios sobre tu trabajo puedes enviarlo a mini-essay@planb.network, estaremos encantados de revisarlo.


#### Descentralización



- La descentralización es Hard. ¿Por qué nos tomamos tantas molestias para que funcione? ¿Podríamos optar por un enfoque híbrido, en el que algunas partes estén centralizadas y otras no?
- ¿La descentralización introduce el problema del doble gasto, o el problema del doble gasto requiere descentralización? ¿Cómo resolvió la Satoshi el problema del doble gasto?
- ¿En qué aspectos sigue siendo Bitcoin más propensa a la censura, y por qué es tan mala la censura? ¿Hay argumentos a favor de la censura?
- Se indica que la Bitcoin es permissionless. ¿Hay algún otro método de pago que se pueda considerar permissionless?



#### Desconfianza




- La desconfianza suele ser un espectro, no binario. ¿Qué aspectos de Bitcoin son más bien Trustless y cuáles suelen implicar un mayor nivel de confianza? ¿Pueden mitigarse?
- Desea ejecutar una Full node para poder validar completamente todas las transacciones. Usted descarga Bitcoin Core de https://Bitcoin.org/en/download. ¿Dónde has depositado la confianza y dónde estás completamente Trustless?
- ¿Se puede construir un sistema Trustless sobre un sistema de confianza?



#### Privacidad




- ¿Cuáles son algunos de los beneficios importantes que obtiene un usuario cuando mantiene una buena privacidad al interactuar con Bitcoin? ¿Cuáles son algunos beneficios altruistas para la red?
- ¿Cómo afecta la reutilización de direcciones a su privacidad?
- Bitcoin utiliza un modelo UTXO, mientras que algunas criptomonedas alternativas utilizan un modelo de cuenta. Qué implicaciones tiene esta elección para la privacidad?



#### Finito Supply




- ¿Cuál es la relación entre la Bitcoin finita y la Supply y su emisión de moneda a través de la Coinbase Transaction? ¿Cuál es la relación entre la emisión de monedas y el presupuesto de seguridad, y en qué se contradicen?
- ¿Qué parámetros podría haber modificado Satoshi para cambiar el tope de Supply de Bitcoin? ¿Qué cambiaría si hubiera decidido limitar la Supply a 1 millón? ¿Qué tal 1 billón?
- ¿Por qué hay quien aboga por aumentar la Bitcoin Supply? ¿Cree que esto ocurrirá?


#### Actualización de



- ¿Qué es el Juicio Rápido y por qué era necesario activar Taproot?
- ¿Por qué es necesario un porcentaje tan alto de mineros para actualizar en un softfork? ¿Por qué el umbral no es sólo del 51%?



#### Pensamiento adversario




- ¿Qué es un ataque sibilino y qué hace que una red descentralizada sea tan propensa a él?
- ¿Por qué es importante que todos los agentes de la red Bitcoin -y no sólo los desarrolladores- piensen de forma adversaria?



#### Código abierto




- Sólo un puñado de mantenedores tienen los permisos necesarios en GitHub para fusionar código en el repositorio [Bitcoin Core](https://github.com/Bitcoin/Bitcoin). ¿No es esto contrario a una red sin permisos?
- ¿Es el proceso de desarrollo del código abierto propenso a un ataque sibilino? En caso afirmativo, ¿cómo lo contrarrestaría?
- ¿Cuáles son las ventajas y los inconvenientes de depender de bibliotecas de código abierto de terceros, y cuál es el enfoque adoptado con Bitcoin Core?
- ¿En qué aspectos necesitamos una revisión que vaya más allá de la revisión del código? ¿Cómo determinar cuánta revisión es suficiente?
- ¿Cómo garantizamos que siempre habrá suficientes personas con experiencia trabajando en Bitcoin? ¿Qué ocurre cuando no las hay y cómo evaluamos su integridad y sus intenciones?



#### Escala




- Se argumenta que la fragmentación ofrece ventajas de escalabilidad a costa de la complejidad. ¿Por qué debemos o no adoptar mejoras tecnológicas porque son difíciles de entender, aunque parezcan tecnológicamente sólidas?
- ¿Cuáles son algunos ejemplos de métodos de escalado hacia dentro introducidos en Bitcoin?
- ¿Por qué el escalado vertical es mucho más difícil en un sistema descentralizado? ¿Y el escalado horizontal?
- No parece que estemos cerca de llegar a un consenso sobre cómo podríamos embarcar a todo el mundo en Bitcoin. ¿No debería Satoshi haber pensado al menos en un camino para llegar allí, antes de Mining el primer bloque en 2009?
- ¿Cómo clasificaría (vertical, horizontal, hacia dentro, o no es una técnica de escalado) cada una de las siguientes: fragmentación, aumento del tamaño de los bloques, SegWit, nodos SPV, intercambios centralizados, Lightning Network, disminución del intervalo entre bloques, Taproot, cadenas laterales?



# Sección final


<partId>4b6ff4ef-b9ea-4c48-b05f-62d41a38fbbb</partId>


## Opiniones y valoraciones


<chapterId>d334a837-df46-4989-9cad-8d8779147dbe</chapterId>


<isCourseReview>true</isCourseReview>

## Conclusión


<chapterId>b77ed55c-b13a-430b-a212-37aab527b9e7</chapterId>


<isCourseConclusion>true</isCourseConclusion>
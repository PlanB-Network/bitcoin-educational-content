---
name: Bitaxe Open Source Mining Maestría
goal: Domine el ecosistema completo de Bitaxe, desde el ensamblaje del hardware hasta la personalización avanzada y la optimización del rendimiento
objectives: 

  - Comprender la filosofía del hardware de código abierto Bitcoin mining
  - Construir dispositivos Bitaxe mining desde cero
  - Configurar y optimizar el software de mining, incluidos AxeOS y Public Pool
  - Implementación de optimizaciones avanzadas de rendimiento, incluidos overclocking y benchmarking

---

# Su guía Bitaxe Mining


Bienvenido al completo curso de Bitaxe, donde dominarás el revolucionario hardware de código abierto Bitcoin mining que está democratizando el acceso a la tecnología mining. Este curso te lleva desde la comprensión de los fundamentos filosóficos de la mining descentralizada hasta las técnicas avanzadas de personalización del hardware y optimización del rendimiento.


El proyecto Bitaxe representa un cambio de paradigma en Bitcoin mining, rompiendo el monopolio de los fabricantes propietarios de ASIC al proporcionar diseños, firmware y software totalmente de código abierto. A través de estos capítulos prácticos, adquirirás conocimientos prácticos sobre montaje de hardware, configuración de software, diseño de PCB y optimización del rendimiento.


No se requiere experiencia previa en mining, aunque serán útiles conocimientos básicos de electrónica y familiaridad con GitHub. El curso te transformará de un observador curioso en un constructor y colaborador capaz de Bitaxe.


+++


# Introducción


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Resumen del curso


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Bienvenido al curso MIN 306 _**Dominio de Bitaxe Open Source Mining**_, un completo viaje al mundo de Bitaxe mining. Este curso está diseñado para aquellos que quieren entender, construir y optimizar su propio hardware Bitaxe mining mientras exploran los fundamentos filosóficos y técnicos que hacen que este proyecto sea único dentro del ecosistema Bitcoin.


### Comprender Bitaxe


La primera sección sienta las bases esenciales: descubrirás los orígenes del proyecto Bitaxe, su evolución y los valores de descentralización y transparencia que lo definen. Aprenderás qué es realmente un Bitaxe, en qué se diferencia de los ASIC propietarios y dónde encontrar recursos de la comunidad para profundizar en tus conocimientos. Esta sección proporciona el contexto necesario para entender por qué Bitaxe representa un punto de inflexión en la historia de Bitcoin mining.


### Software y operaciones


La segunda sección se centra en el entorno de software, con una presentación detallada de *AxeOS*: el sistema operativo de código abierto diseñado específicamente para los dispositivos Bitaxe. Aprenderás sus principales características y cómo configurar e interactuar con tu dispositivo para iniciar tu primera operación con mining.


### Comunidad y colaboración


La tercera sección destaca el aspecto colaborativo del proyecto. Explorarás la filosofía de código abierto aplicada al desarrollo tanto de hardware como de software de Bitaxe. A través de ejercicios prácticos, aprenderás a contribuir directamente al código fuente, y también descubrirás _Public Pool_, una plataforma comunitaria para poner en común la potencia de cálculo. También aprenderás a instalarla en un nodo Umbrel para su integración local y soberana.


### Montaje de hardware y solución de problemas


En la cuarta sección, te sumergirás en el hardware propiamente dicho. Aprenderás a identificar las herramientas necesarias para montar un Bitaxe, solucionar problemas de soldadura y realizar un diagnóstico completo utilizando *AxeOS* y herramientas USB. Esta sección hace hincapié en la práctica y en una comprensión profunda de cómo interactúan los componentes de hardware y software.


### Personalización avanzada


La quinta sección está dedicada a la personalización. Aprenderás a modificar la PCB (placa de circuito impreso), a crear un archivo de fábrica y a utilizar el _Bitaxe Web Flasher_. Esta sección está dirigida a aquellos que quieren ir más allá del simple montaje y realmente diseñar versiones personalizadas de su propio dispositivo.


### Optimización del rendimiento


Por último, la sexta sección cubre técnicas avanzadas de optimización. Aprenderás a realizar un benchmark de tu Bitaxe para evaluar su rendimiento y a realizar un overclocking eficiente. Estos conocimientos te ayudarán a sacar el máximo partido a tu hardware respetando sus limitaciones físicas.


Como en todos los cursos de la Academia Plan ₿, la sección final incluye una evaluación diseñada para reforzar tus conocimientos.


Sumérgete de lleno en esta aventura técnica: ¡el futuro de Bitcoin mining está en tus manos!


# Comprender Bitaxe

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## Historia

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

El proyecto Bitaxe representa un cambio revolucionario en el desarrollo de hardware para la Bitcoin mining, aportando principios de código abierto a una industria dominada por soluciones propietarias. Esta serie educativa explora la historia completa, las innovaciones técnicas y la evolución impulsada por la comunidad de Bitaxe, proporcionando información sobre cómo la visión de un solo ingeniero se transformó en un próspero ecosistema de hardware mining descentralizado. A través del examen de los orígenes, retos y logros del proyecto, adquirimos una valiosa comprensión tanto de las complejidades técnicas del desarrollo de la ASIC como del poder de la colaboración de código abierto en el espacio de la Bitcoin.


### La historia del origen: Del descubrimiento de la Ruta de la Seda a la visión del Mining solar


Skot, el fundador de Bitaxe, comenzó su andadura en el Bitcoin en una fiesta universitaria, donde conoció el Bitcoin a través de alguien que compraba artículos en la Ruta de la Seda. Esta exposición inicial al Bitcoin a unos 20 dólares por moneda despertó una curiosidad que más tarde evolucionaría hasta convertirse en un proyecto revolucionario de mining. La base técnica de su futuro trabajo se estableció durante su estancia en la universidad, donde tuvo acceso a amplios recursos FPGA en un entorno de laboratorio. Trabajando junto a su supervisor, Skot comenzó a experimentar con flujos de bits FPGA de código abierto para Bitcoin mining, inicialmente con el modesto objetivo de mining Bitcoin suficiente para comprar una pizza para su oficina.


La transición de la experimentación académica al desarrollo serio se produjo años más tarde, cuando Skot trabajaba en pasarelas alimentadas por energía solar para la recogida remota de datos en África. Esta experiencia profesional con sistemas de energía solar le hizo darse cuenta de que los ASIC Bitcoin mining, al ser fundamentalmente dispositivos de corriente continua de bajo voltaje, encajarían perfectamente con los paneles solares. El concepto parecía natural y elegante. Sin embargo, cuando Skot comenzó a investigar las soluciones existentes, descubrió una importante laguna en el mercado: a diferencia de los primeros días de Bitcoin mining, cuando los diseños FPGA estaban disponibles abiertamente, la llegada de los ASIC había llevado a la industria hacia soluciones completamente propietarias y de código cerrado.


La falta de hardware de código abierto para mining se convirtió en una frustración para Skot, sobre todo teniendo en cuenta su experiencia en el desarrollo de software de código abierto y su convicción de que la naturaleza de código abierto de Bitcoin debía extenderse a su infraestructura de mining. Esta alineación filosófica con los principios del código abierto, combinada con el reto técnico que suponía la ingeniería inversa de los diseños propietarios de ASIC, sentó las bases de lo que se convertiría en el proyecto Bitaxe. La visión inicial era ambiciosa pero práctica: crear un minero Bitcoin alimentado por energía solar que pudiera funcionar de forma independiente sin necesidad de un ordenador separado para su control, lo que lo haría adecuado para su despliegue en lugares remotos bajo paneles solares.


### Retos técnicos y avances en ingeniería inversa


El desarrollo de Bitaxe requirió superar importantes obstáculos técnicos, centrados principalmente en la falta total de documentación de los chips ASIC de Bitmain. La forma en que Skot afrontó este reto ejemplificó la determinación y el ingenio necesarios para llevar a cabo con éxito la ingeniería inversa. Sin acceso a hojas de datos oficiales ni a especificaciones técnicas, recurrió a examinar los chips con microscopios, medir los pasos de los pines con calibradores e incluso escanear los chips para determinar sus requisitos exactos de huella. Este meticuloso proceso dio lugar a varios prototipos fallidos, y las dos primeras iteraciones del "minero diurno" no funcionaron correctamente debido a cálculos incorrectos de la huella.


El gran avance llegó con la tercera iteración en mayo de 2022, cuando Skot creó con éxito un diseño funcional de dos chips utilizando chips BM1387 extraídos de unidades Antminer S9. Este logro marcó el nacimiento del nombre Bitaxe, inspirado en el concepto de pico para Bitcoin mining. El éxito de este diseño validó el enfoque de ingeniería inversa y demostró que los desarrolladores independientes podían crear hardware mining funcional sin el apoyo del fabricante. Sin embargo, los retos técnicos no se limitaron a la interconexión de los chips, sino que incluyeron un complejo diseño de la fuente de alimentación, ya que los ASIC necesitaban una regulación precisa de la tensión a altas corrientes, y a menudo funcionaban a tensiones de tan sólo 0,6 voltios mientras consumían un amperaje considerable.


El desarrollo del firmware presentaba otra capa de complejidad, ya que el proyecto exigía crear un software para mining que pudiera ejecutarse directamente en un microcontrolador ESP32, en lugar de depender de ordenadores externos que ejecutaran software como CGMiner. Este enfoque autónomo era esencial para la visión de Skot de unidades mining desplegables e independientes. La combinación de ingeniería inversa de hardware y desarrollo de firmware embebido supuso un reto técnico de gran envergadura que exigió conocimientos en múltiples disciplinas, desde ingeniería eléctrica y diseño de placas de circuito impreso hasta programación embebida y protocolos de red.


### Formación de comunidades y colaboración de código abierto


La transformación de Bitaxe de un proyecto en solitario a una próspera iniciativa comunitaria representa uno de los aspectos más significativos de su éxito. Al principio, los intentos de Skot de despertar el interés de generate a través de los foros de Bitcoin y las redes sociales se encontraron con una respuesta limitada y un escepticismo ocasional. El gran avance se produjo cuando miembros de la comunidad como SirVapesAlot reconocieron el potencial de la mining de código abierto y crearon el servidor Discord Open Source Miners United (OSMU). Esta plataforma proporcionó el entorno de colaboración necesario para que el proyecto floreciera, atrayendo a colaboradores de diversos orígenes que compartían un interés común por democratizar la tecnología Bitcoin mining.


El modelo de desarrollo impulsado por la comunidad demostró ser notablemente eficaz, con colaboradores clave como johnny9 y Ben, que surgieron para abordar retos técnicos específicos. La experiencia de Johnny9 en el desarrollo de firmware resolvió problemas críticos de implementación de software, mientras que las habilidades de desarrollo front-end de Ben crearon el intuitivo panel AxeOS que simplificó la configuración y monitorización de los dispositivos. Las contribuciones adicionales de Ben incluyeron el establecimiento de capacidades de fabricación y la creación de Public Pool, un pool mining de código abierto optimizado para los dispositivos Bitaxe. Este enfoque colaborativo demostró cómo los principios del código abierto pueden acelerar el desarrollo más allá de lo que cualquier colaborador individual podría lograr por sí solo.


La comunidad OSMU también fomentó un entorno integrador en el que los recién llegados podían aprender y contribuir independientemente de sus conocimientos técnicos iniciales. La propia trayectoria de Ben, que pasó de ser un novato en soldadura a convertirse en un importante fabricante, ejemplifica este enfoque acogedor del desarrollo de habilidades. El compromiso de la comunidad con la educación y el apoyo mutuo creó un círculo virtuoso en el que los miembros experimentados servían de mentores a los recién llegados, que se convertían a su vez en colaboradores. Este modelo resultó esencial para ampliar el proyecto más allá de su alcance original y establecer un ecosistema sostenible para la innovación y el crecimiento continuos.


### Visión de la Mining descentralizada e impacto futuro


La visión a largo plazo de Skot para Bitaxe va mucho más allá de la creación de otro dispositivo mining: se trata de una transformación fundamental del panorama mining de Bitcoin. El ambicioso objetivo de producir un millón de mineros de un terahash crearía un exahash de energía distribuida de mining, lo que representaría un paso significativo hacia la descentralización de mining. Esta visión aborda las preocupaciones críticas sobre la centralización de mining, donde las grandes reservas y las operaciones industriales podrían estar potencialmente sujetas a la presión del gobierno o a la captura reguladora. Al distribuir la energía de mining entre innumerables mineros domésticos, la red se hace más resistente y se alinea con los principios descentralizados de Bitcoin.


El modelo económico que sustenta esta visión se basa en las características únicas de la mining doméstica, en la que los costes de infraestructura son prácticamente nulos y los mineros pueden operar con una supervisión mínima. A diferencia de las operaciones industriales de mining, que requieren grandes inversiones de capital en instalaciones, infraestructura eléctrica y sistemas de refrigeración, los mineros domésticos pueden simplemente conectar sus dispositivos a las tomas de corriente y conexiones a Internet existentes. En teoría, este enfoque podría poner en línea una importante tasa de hash sin las tradicionales barreras de entrada que caracterizan a las operaciones de mining a gran escala.


El éxito del proyecto ya ha empezado a influir en el ecosistema más amplio de Bitcoin mining, con potencial para inspirar a otros fabricantes a adoptar modelos de desarrollo de código abierto. La viabilidad financiera demostrada por los fabricantes de Bitaxe prueba que el hardware de código abierto puede tener éxito comercial manteniendo la transparencia y la participación de la comunidad. A medida que el proyecto sigue evolucionando con nuevas integraciones de chips, diseños mejorados y asociaciones de fabricación ampliadas, sirve como prueba de concepto de cómo Bitcoin mining puede volver a sus raíces descentralizadas a la vez que adopta la tecnología moderna ASIC. El objetivo final va más allá de la mera distribución de la tasa de hash e incluye el impacto educativo, poniendo a más personas en contacto directo con el proceso fundamental de Bitcoin mining y fomentando una comprensión más profunda del modelo de seguridad de la red.


## ¿Qué es el Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Descripción general del hardware y funciones


El ecosistema Bitaxe abarca múltiples iteraciones de hardware, cada una diseñada para optimizar diferentes aspectos de la experiencia mining, manteniendo la filosofía central de accesibilidad de código abierto. Estos dispositivos no sólo sirven como hardware funcional de mining, sino también como herramientas educativas que permiten a los usuarios comprender la intrincada relación entre los chips ASIC, los microcontroladores y el proceso Bitcoin mining. Comprender la filosofía de diseño y la implementación técnica del Bitaxe proporciona valiosos conocimientos sobre el funcionamiento del hardware mining moderno, tanto a nivel de componente como de sistema.



### Bitaxe Max, aplicación de primera generación


El Bitaxe Max representa la implementación fundacional del concepto Bitaxe, utilizando el chip BM1397 ASIC desarrollado originalmente por Bitmain para su serie S17 mining. La integración de este chip demuestra cómo el hardware de código abierto puede reutilizar la tecnología ASIC existente para crear soluciones mining accesibles. Bitaxe Max ofrece una tasa de hash estimada de entre 300 y 400 gigahashes por segundo, lo que la convierte en una plataforma mining educativa y experimental más que en una solución a escala comercial.


La integración del chip BM1397 en el Bitaxe Max exigió un cuidadoso examen de la gestión de la energía, el control térmico y los protocolos de comunicación. El diseño de la placa se adapta a los requisitos específicos de este ASIC, al tiempo que proporciona los circuitos de apoyo necesarios para un funcionamiento estable. Esta implementación muestra cómo el desarrollo de hardware de código abierto puede aprovechar la tecnología de semiconductores existente para crear nuevas aplicaciones y oportunidades de aprendizaje dentro de la comunidad mining.


### Bitaxe Ultra, tecnología de chip avanzada


El Bitaxe Ultra representa la evolución de la plataforma Bitaxe, incorporando el chip BM1366 ASIC más avanzado de la serie S19 de Bitmain. Esta tecnología de chip más reciente aporta a la plataforma Bitaxe unas características de eficiencia y rendimiento mejoradas, al tiempo que mantiene la misma filosofía de diseño fundamental. La actualización al chip BM1366 demuestra la adaptabilidad de la plataforma y el compromiso de la comunidad con la incorporación de avances tecnológicos a las soluciones mining de código abierto.


La transición del chip BM1397 al BM1366 requirió modificaciones en los sistemas de suministro de energía, la gestión térmica y los algoritmos de control de la placa. Estos cambios ilustran la naturaleza iterativa del desarrollo de hardware y la importancia de mantener la compatibilidad al tiempo que se mejora el rendimiento. La implementación de Bitaxe Ultra proporciona a los usuarios acceso a la tecnología ASIC más reciente, al tiempo que preserva la naturaleza educativa y experimental de la plataforma.


### Microcontroladores y sistemas de comunicación


En el corazón de cada dispositivo Bitaxe se encuentra un microcontrolador ESP que sirve como interfaz principal entre el usuario y el chip ASIC. Este microcontrolador ejecuta un software especializado desarrollado por la comunidad Open Source Miners United (OSMU), que permite un control preciso de los parámetros de funcionamiento de la ASIC. La comunicación entre el microcontrolador y ASIC se produce a través de líneas de comunicación en serie cuidadosamente diseñadas que están grabadas directamente en la placa de circuito impreso como trazas visibles.


El papel del microcontrolador va más allá del simple control de ASIC: incluye funciones de gestión de la alimentación, control de la temperatura e interfaz de usuario. A través de la pantalla de visualización integrada, los usuarios pueden supervisar parámetros operativos críticos como la temperatura, la tasa de hash, la dirección IP y otras estadísticas relevantes de mining. Este sistema de retroalimentación en tiempo real proporciona información valiosa sobre el rendimiento del dispositivo y ayuda a los usuarios a optimizar sus operaciones de mining mientras aprenden sobre el comportamiento subyacente del hardware.


### Gestión de la alimentación y consideraciones de seguridad


La plataforma Bitaxe funciona con un estricto requisito de alimentación de 5 voltios, por lo que una selección adecuada de la fuente de alimentación es fundamental para la longevidad y seguridad del dispositivo. El sistema de gestión de la alimentación de las placas Bitaxe incluye sofisticados circuitos diseñados para regular la tensión suministrada al chip ASIC y controlar el consumo de energía en los distintos modos de funcionamiento. Esta capacidad de gestión de la energía permite que el dispositivo funcione de forma eficiente en toda una gama de frecuencias y tensiones internas, con un consumo típico de entre 5 y 25 vatios según la configuración.


Comprender los requisitos de potencia resulta crucial si se tiene en cuenta que una aplicación incorrecta del voltaje puede dañar permanentemente el dispositivo. La relación entre frecuencia, voltaje, consumo de energía y tasa de hash demuestra los principios fundamentales del funcionamiento de ASIC que se aplican a todo el hardware mining. Los usuarios pueden experimentar con diferentes configuraciones de potencia para comprender las compensaciones de eficiencia inherentes a las operaciones de mining, adquiriendo experiencia práctica con conceptos que se aplican a implementaciones de mining a mayor escala.


### Solo Mining Enfoque y participación en la red


La plataforma Bitaxe se dirige específicamente a aplicaciones mining en solitario, en las que mineros individuales intentan resolver bloques Bitcoin de forma independiente en lugar de participar en grandes grupos mining. Aunque la tasa de hash de los dispositivos Bitaxe hace que el descubrimiento exitoso de bloques sea estadísticamente improbable, este enfoque sirve a importantes propósitos educativos y filosóficos dentro de la comunidad Bitcoin. Solo mining con dispositivos Bitaxe ayuda a los usuarios a comprender la mecánica fundamental del sistema proof-of-work de Bitcoin al tiempo que contribuye a la descentralización de la red.


El énfasis en mining en solitario refleja el compromiso de la comunidad OSMU de fomentar la participación individual en el modelo de seguridad de Bitcoin. Al proporcionar hardware accesible que puede funcionar de forma independiente, la plataforma Bitaxe permite a los usuarios ejecutar sus propias operaciones de mining sin depender de la infraestructura del pool. Este enfoque fomenta una comprensión más profunda del mecanismo de consenso de Bitcoin, al tiempo que apoya la naturaleza descentralizada de la red a través de una mayor diversidad de mineros.


### Evolución del hardware y mejoras de producción


La plataforma Bitaxe sigue evolucionando gracias a los comentarios de la comunidad y a la optimización de la producción, y las nuevas versiones incorporan mejoras que mejoran la capacidad de fabricación y la experiencia del usuario. Las actualizaciones de versiones suelen centrarse en la eficiencia de la producción más que en cambios fundamentales en el rendimiento, lo que garantiza que los usuarios actuales no se enfrenten a la presión de la obsolescencia. Características como la transición de conectores micro-USB a USB-C y la mejora de los sistemas de conexión de alimentación reflejan la atención de la comunidad a las mejoras prácticas de usabilidad.


Este enfoque evolutivo demuestra las ventajas del desarrollo de hardware de código abierto, en el que las aportaciones de la comunidad impulsan mejoras graduales que benefician a todos los usuarios. La filosofía de "si tiene hash, tiene hash" enfatiza el enfoque de la plataforma en la funcionalidad por encima de las actualizaciones constantes, animando a los usuarios a mantener y operar sus dispositivos en lugar de perseguir las últimas versiones. Este enfoque apoya las prácticas de hardware sostenibles al tiempo que mantiene el valor educativo de Bitaxe.


## ¿Dónde puedo obtener más información?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

El proyecto Bitaxe representa una amplia iniciativa de código abierto para la mining que va mucho más allá de un único dispositivo. Saber dónde encontrar información fiable, recursos técnicos y apoyo de la comunidad es crucial para cualquiera que desee participar en este ecosistema. Este capítulo proporciona una guía completa de las plataformas y recursos esenciales que forman la base de la comunidad Bitaxe y Open Source Miners United (OSMU).


### Bitaxe.org, el eje central


El sitio web Bitaxe.org es la principal puerta de acceso a toda la información y recursos relacionados con el proyecto. Esta plataforma centralizada funciona como su primer punto de referencia siempre que necesite aprender sobre los dispositivos Bitaxe o explorar otros proyectos dentro de la comunidad OSMU. El diseño del sitio web prioriza la accesibilidad y la organización, presentando a los visitantes enlaces cuidadosamente seleccionados que conectan con diversos recursos especializados de todo el ecosistema.


No se puede exagerar la importancia de este eje central, ya que elimina la confusión que suele acompañar a los proyectos descentralizados de código abierto. En lugar de buscar a través de múltiples plataformas o confiar en información potencialmente obsoleta de fuentes no oficiales, los usuarios pueden confiar en Bitaxe.org para proporcionar enlaces actualizados y verificados a todos los recursos esenciales. Este enfoque garantiza que tanto los recién llegados como los miembros experimentados de la comunidad puedan localizar eficazmente la información específica que necesitan para sus proyectos.


### Recursos técnicos y materiales de desarrollo


El repositorio de archivos de diseño de hardware en GitHub representa uno de los recursos más valiosos para cualquier persona interesada en comprender o construir dispositivos Bitaxe. Este repositorio público contiene documentación exhaustiva que cubre todos los aspectos del proceso de diseño de hardware, desde los conceptos iniciales hasta las especificaciones finales de fabricación. El repositorio incluye imágenes detalladas, objetivos del proyecto, descripciones de características y explicaciones de componentes integrados que proporcionan tanto profundidad técnica como orientación práctica.


Para los interesados en fabricar sus propios dispositivos, el repositorio incluye archivos de documentación específicos como building.md, que ofrece instrucciones paso a paso para todo el proceso de producción. Esta documentación abarca las herramientas de software necesarias para el diseño de PCB, los procedimientos de envío de archivos a los fabricantes y los pasos necesarios para recibir y validar las PCB fabricadas. Este nivel de detalle garantiza que particulares o pequeñas organizaciones puedan desenvolverse con éxito en el proceso de fabricación sin necesidad de contar con una amplia experiencia previa en la producción de hardware.


El repositorio ESP-Miner sirve como ubicación central para todo el código y la documentación relacionados con el firmware. Este repositorio de GitHub contiene todas las líneas de código escritas para el firmware Bitaxe, junto con una completa documentación que explica los requisitos del sistema, las especificaciones de hardware y las opciones de configuración. La estructura del repositorio está diseñada para adaptarse tanto a los usuarios que prefieren archivos binarios precompilados como a los desarrolladores que desean crear el firmware a partir del código fuente.


La documentación de este repositorio incluye secciones detalladas sobre requisitos de hardware, opciones de preconfiguración y valores recomendados para diversos ajustes. Esta información resulta muy valiosa para los usuarios que desean personalizar sus dispositivos o solucionar problemas específicos. Además, el repositorio incluye información sobre nuevos desarrollos, como la integración de Raspberry Pi, lo que garantiza que la documentación se mantiene al día con la evolución continua del proyecto.


### Herramientas de gestión y mantenimiento de dispositivos


El flasheador web de Bitaxe representa una solución práctica para el mantenimiento y las actualizaciones de dispositivos. Esta herramienta basada en web permite a los usuarios actualizar el firmware de sus dispositivos sin necesidad de software especializado ni complejos procedimientos de línea de comandos. El flasheador es compatible con múltiples variantes de dispositivos, incluido el Bitaxe Ultra con varias versiones de puerto y los antiguos modelos Bitaxe Max. Los usuarios pueden elegir entre actualizar el firmware existente a través de la interfaz web o realizar restablecimientos de fábrica completos mediante conexiones USB.


Esta herramienta aborda uno de los retos más comunes a los que se enfrentan los entusiastas del hardware: el mantenimiento y la actualización del firmware de los dispositivos. Al ofrecer una interfaz web fácil de usar, elimina muchas de las barreras técnicas que podrían impedir a los usuarios mantener sus dispositivos actualizados con las últimas versiones de firmware. El diseño de la herramienta da prioridad a la simplicidad, al tiempo que mantiene la flexibilidad necesaria para diferentes configuraciones de dispositivos y escenarios de actualización.


### Plataformas comunitarias y canales de comunicación


El servidor Discord representa el corazón de la interacción y el apoyo de la comunidad en tiempo real dentro del ecosistema Bitaxe. La organización del servidor refleja los diversos intereses y necesidades de los miembros de la comunidad, con canales cuidadosamente estructurados que facilitan debates centrados en temas específicos. Los nuevos miembros se encuentran con un proceso de verificación que requiere la lectura y aceptación de las normas de la comunidad, lo que garantiza que todos los participantes entiendan las expectativas de una interacción respetuosa y productiva.


La estructura de canales del servidor incluye áreas de debate general que cubren temas como la integración de la energía solar, las piscinas mining y las discusiones relacionadas con Bitcoin. Otras secciones más especializadas se centran en dispositivos concretos, como los canales dedicados a las variantes Bitaxe Ultra, Hex y Supra. El canal de firmware ofrece un espacio específico para debates técnicos sobre desarrollo de software y resolución de problemas, mientras que el canal de publicaciones oficiales garantiza que los miembros de la comunidad reciban notificaciones puntuales sobre las novedades.


También cuenta con una zona de abonados que ofrece ventajas adicionales a los miembros de la comunidad que decidan apoyar económicamente el proyecto. Este enfoque escalonado permite a la comunidad ofrecer servicios mejorados al tiempo que mantiene abierto el acceso a la información esencial y a los canales de ayuda. El canal de ayuda es un espacio dedicado a la resolución de problemas y la asistencia técnica, para que los usuarios puedan recibir ayuda rápida cuando tengan dificultades.



La wiki de Open Source Miners United (osmu.wiki) proporciona documentación exhaustiva que complementa los debates en tiempo real que tienen lugar en Discord. A diferencia de las plataformas basadas en chat, la wiki ofrece documentación estructurada en la que se pueden realizar búsquedas y que cubre todos los aspectos del proyecto Bitaxe y las iniciativas relacionadas. Su organización refleja la estructura del proyecto, con secciones dedicadas a las distintas series de dispositivos y completas guías de configuración.


La naturaleza de código abierto de la wiki permite a los miembros de la comunidad contribuir directamente a la documentación. Los usuarios pueden editar páginas, enviar correcciones y añadir nueva información a través de la integración con GitHub, lo que garantiza que la base de conocimientos se mantenga actualizada y transparente. Este enfoque colaborativo aprovecha la experiencia colectiva de la comunidad a la vez que mantiene el control de calidad mediante un proceso de revisión de los cambios enviados.


La wiki incluye recursos prácticos como guías de configuración en PDF que ofrecen instrucciones paso a paso para la configuración y el uso de los dispositivos. Estas guías sirven como valiosas referencias tanto para nuevos usuarios como para miembros experimentados de la comunidad que necesiten acceder rápidamente a procedimientos específicos o detalles de configuración.


### Información sobre compras y proveedores


La lista Bitaxe legit responde a una necesidad crítica de la comunidad de hardware de código abierto: identificar a los vendedores de confianza y evitar a los vendedores fraudulentos. Esta lista incluye distribuidores y fabricantes verificados que cumplen criterios específicos de legitimidad y apoyo a la comunidad. Cada lista incluye enlaces directos a los sitios web de los vendedores, información regional y descripciones de las empresas que ayudan a los usuarios a tomar decisiones de compra informadas.


Y lo que es más importante, la lista indica si cada proveedor contribuye a la comunidad OSMU, ya sea económicamente o mediante otras formas de apoyo. Esta transparencia ayuda a los miembros de la comunidad a saber qué vendedores apoyan activamente el desarrollo y la sostenibilidad del proyecto. La lista también sirve como medida de protección contra estafas comunes, como pedidos anticipados no autorizados de productos no lanzados, que históricamente han causado problemas dentro de la comunidad.


El énfasis en los enlaces no afiliados demuestra el compromiso de la comunidad de ofrecer recomendaciones imparciales de proveedores. Los usuarios pueden confiar en que las recomendaciones se basan en la legitimidad del proveedor y la contribución de la comunidad, y no en incentivos económicos, lo que garantiza que las decisiones de compra apoyen tanto las necesidades individuales como la sostenibilidad de la comunidad.



# Software y operaciones

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## ¿Qué es AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS es una interfaz web y de firmware para los dispositivos Bitaxe mining, que proporciona a los usuarios capacidades completas de control y supervisión a través de un intuitivo panel de control basado en navegador. Este sistema transforma la compleja tarea de gestión de ASIC en una experiencia accesible, permitiendo a los mineros monitorizar el rendimiento, ajustar la configuración y gestionar múltiples dispositivos desde una única interfaz. Comprender AxeOS es esencial para maximizar el potencial de su dispositivo Bitaxe y mantener un funcionamiento óptimo de mining.


### Cuadro de mandos y métricas básicas


El panel de control AxeOS sirve como ventana principal al rendimiento de su dispositivo Bitaxe, presentando métricas críticas de mining en un formato organizado y en tiempo real. Cuando navega a la dirección IP de su dispositivo Bitaxe, se le presentan inmediatamente cuatro indicadores clave de rendimiento que definen el estado actual de su operación mining. La visualización de la tasa de hash muestra la velocidad de cálculo real que su chip ASIC está produciendo a medida que procesa la plantilla de bloques actual, proporcionando información inmediata sobre la funcionalidad central de su dispositivo.


Junto a la tasa de hash, el contador de acciones realiza un seguimiento de cada solución válida que su dispositivo Bitaxe envía al pool mining, incrementándose con cada envío correcto y sirviendo como medida directa de la contribución de su dispositivo a los esfuerzos del pool mining. La métrica de eficiencia proporciona información crucial sobre el rendimiento energético de su dispositivo calculando la relación entre la tasa de hash y el consumo de energía, ayudándole a optimizar la rentabilidad de su operación. El indicador de mejor dificultad conserva un registro de la cuota de dificultad más alta que tu dispositivo haya encontrado nunca, manteniendo este logro incluso a través de reinicios y actualizaciones, reiniciándose sólo cuando realizas un flasheo completo de fábrica.


El sistema de menús ampliable del panel de control, controlado por un botón basculante, proporciona acceso a todas las funciones de AxeOS manteniendo una interfaz limpia. El gráfico de tasa de hachís en vivo representa una de sus características más valiosas, ya que muestra datos de rendimiento en tiempo real que se vuelven más precisos e informativos cuanto más tiempo mantienes la sesión. Las secciones de potencia, calor y rendimiento proporcionan una monitorización completa del estado operativo de tu dispositivo, incluyendo advertencias de voltaje de entrada que te alertan de posibles problemas con la fuente de alimentación a la vez que garantizan un funcionamiento continuado dentro de parámetros seguros.


### Supervisión avanzada e información del sistema


Las capacidades de monitorización de AxeOS van mucho más allá del seguimiento básico de la tasa de hash, proporcionando información detallada sobre cada aspecto del funcionamiento de tu dispositivo Bitaxe. La sección de energía muestra el consumo de energía calculado derivado de los circuitos integrados a bordo, las mediciones de voltaje de entrada de la conexión de la fuente de alimentación y los niveles de voltaje ASIC solicitados. Cuando se producen caídas de tensión, AxeOS presenta inmediatamente notificaciones de advertencia, aunque éstas no suelen afectar al funcionamiento del mining y simplemente indican posibles oportunidades de optimización de la fuente de alimentación.


La monitorización de la temperatura se centra en la gestión térmica del chip ASIC, con lecturas tomadas desde ubicaciones estratégicas del dispositivo para proporcionar datos térmicos precisos con las compensaciones adecuadas para una precisión a nivel de chip. Las pantallas de frecuencia y tensión ofrecen información en tiempo real sobre los parámetros de ajuste de ASIC, y la tensión medida representa la lectura más precisa disponible, tomada directamente en la ubicación del chip ASIC. Esta precisión permite un ajuste fino de los parámetros de rendimiento, manteniendo al mismo tiempo unas condiciones de funcionamiento seguras.


La sección de estado de la conexión proporciona una visibilidad inmediata de la configuración de su pool mining, mostrando la URL actual del stratum, el puerto y la identificación del usuario. Para los dispositivos conectados a pools públicos, AxeOS genera prácticos enlaces rápidos que le transportan directamente a la interfaz web de su pool, donde puede acceder a estadísticas detalladas, listados de dispositivos y datos históricos de rendimiento. Esta integración agiliza el proceso de monitorización conectando la información a nivel de dispositivo y a nivel de pool en un flujo de trabajo sin fisuras.


### Gestión de enjambres y control multidispositivo


La funcionalidad Swarm representa la solución de AxeOS a la complejidad de gestionar múltiples dispositivos Bitaxe a través de una red, eliminando la necesidad de recordar y navegar a numerosas direcciones IP. Este sistema de gestión centralizada permite añadir dispositivos simplemente introduciendo sus direcciones IP, detectando automáticamente los mineros Bitaxe activos e incorporándolos a un panel de control unificado. Una vez configurado, Swarm proporciona un control exhaustivo de todo el funcionamiento de mining desde una única interfaz.


A través de la interfaz Swarm, puede realizar tareas de gestión críticas en varios dispositivos de forma simultánea o individual, incluidos cambios en la configuración del grupo, reinicios de dispositivos, ajustes de frecuencia y supervisión del rendimiento. Este enfoque centralizado reduce significativamente la sobrecarga administrativa de la gestión de grandes operaciones de mining, al tiempo que garantiza una configuración coherente en todos los dispositivos. El sistema mantiene la identidad individual de cada dispositivo a la vez que proporciona capacidades de gestión colectiva, logrando un equilibrio óptimo entre control granular y eficacia operativa.


El panel de control de Swarm presenta cada dispositivo gestionado con su estado actual, métricas de rendimiento y controles de acceso rápido, lo que permite una respuesta rápida a los problemas de rendimiento o cambios de configuración. Esta funcionalidad resulta especialmente valiosa para los mineros que operan varios dispositivos en distintas ubicaciones o para aquellos que ajustan con frecuencia los parámetros de mining en función de las condiciones del mercado o del rendimiento del grupo.


### Gestión de la configuración y ajustes del sistema


La sección Ajustes de AxeOS proporciona un control exhaustivo sobre cada aspecto configurable de su dispositivo Bitaxe, desde la conectividad de red hasta los parámetros de mining y la optimización del hardware. La configuración de la red comienza con la configuración Wi-Fi, donde se especifica el nombre de la red y la contraseña, con AxeOS recomendando nombres de red de una sola palabra sin espacios para garantizar una conectividad fiable. El sistema se encarga de todo el proceso de configuración inalámbrica y permite la gestión y supervisión remotas.


La configuración de Mining se centra en los ajustes de estrato, donde se especifica la URL del pool mining elegido sin prefijos de protocolo ni números de puerto, que se gestionan en campos separados. El campo de usuario de estrato se adapta a varios requisitos de grupo, ya que admite tanto direcciones Bitcoin para mining en solitario como sistemas de nombre de usuario para mining en grupo, con la posibilidad de añadir identificadores de dispositivo para operaciones con varios dispositivos. La función de contraseña de estrato, añadida recientemente, es compatible con las agrupaciones que requieren autenticación, aunque la mayoría de las agrupaciones públicas funcionan sin este requisito.


La optimización del hardware mediante el ajuste de la frecuencia y el voltaje del núcleo representa la capacidad de ajuste del rendimiento más potente de AxeOS. Dependiendo de la versión del dispositivo y del navegador, estos ajustes pueden aparecer como menús desplegables con configuraciones preestablecidas o como campos abiertos que permiten valores personalizados. Los ajustes por defecto de 485 MHz de frecuencia y 1200 mV de voltaje del núcleo proporcionan un funcionamiento estable para las pruebas iniciales, mientras que los usuarios avanzados pueden optimizar estos parámetros para obtener el máximo rendimiento o eficiencia en función de sus requisitos específicos y condiciones de funcionamiento.


### Mantenimiento del sistema y funciones avanzadas


AxeOS incluye sofisticadas funciones de mantenimiento del sistema diseñadas para mantener su dispositivo Bitaxe funcionando al máximo rendimiento, al tiempo que proporciona información de diagnóstico para la solución de problemas y la optimización. El sistema de actualización agiliza la gestión del firmware mostrando la última versión disponible directamente en la interfaz y proporcionando enlaces de descarga directa a los archivos de firmware oficiales. Esta integración elimina la necesidad de navegar manualmente por los repositorios de GitHub o gestionar las descargas de archivos, simplificando el proceso de actualización a unos pocos clics.


La interfaz de actualización acepta archivos de firmware con nombres adecuados, concretamente esp-miner.bin y www.bin, lo que garantiza la compatibilidad y evita errores de instalación. Para los usuarios que experimentan dificultades con el proceso de actualización estándar, AxeOS proporciona referencias a procedimientos completos de flasheo de fábrica que pueden restaurar los dispositivos a su funcionalidad original. Este enfoque dual se adapta tanto a las actualizaciones rutinarias como a los escenarios de recuperación.


El sistema de registro proporciona información en tiempo real sobre el funcionamiento del dispositivo, mostrando información detallada sobre los modelos de chip ASIC, el tiempo de actividad del sistema, el estado de la conectividad Wi-Fi, la memoria disponible, las versiones de firmware y las revisiones de la placa. Estos registros tienen un valor incalculable para desarrolladores y usuarios avanzados que deseen comprender el comportamiento del dispositivo, diagnosticar problemas u optimizar el rendimiento. El visor de registros en tiempo real presenta datos operativos en directo, incluido el procesamiento de nonce, los cálculos de dificultad y los parámetros de envío de mining, ofreciendo una visibilidad sin precedentes del propio proceso de mining.


Otras funciones del sistema son el control de la orientación de la pantalla para dispositivos utilizados en armarios personalizados, la inversión de la polaridad del ventilador para configuraciones de refrigeración especializadas y el control automático del ventilador que ajusta la refrigeración en función de la temperatura de ASIC. El control manual de la velocidad de los ventiladores proporciona una gestión precisa de la refrigeración cuando los sistemas automáticos no cumplen requisitos específicos. Todos los cambios de configuración requieren guardar y reiniciar el dispositivo para que surtan efecto, lo que garantiza un funcionamiento estable y evita estados de configuración parciales que podrían afectar al rendimiento de mining.



# Comunidad y colaboración

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Contribución de código abierto

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub y su papel en el desarrollo de software


GitHub representa un cambio fundamental en la forma de gestionar y compartir proyectos de desarrollo de software en la comunidad mundial de programadores. Como plataforma basada en la nube que aloja proyectos de desarrollo de software utilizando Git, un sistema de control de versiones distribuido, GitHub permite a los desarrolladores colaborar sin problemas en proyectos independientemente de su ubicación física. La plataforma sirve tanto de herramienta técnica como de red social para programadores, permitiéndoles hacer un seguimiento de los cambios, fusionar actualizaciones, mantener diferentes versiones de su código y contribuir a iniciativas de código abierto como el proyecto BitX de Open Source Miners United.


El poder de GitHub reside en su capacidad para simplificar el complejo proceso del desarrollo colaborativo. Cuando varios desarrolladores trabajan en el mismo proyecto, GitHub proporciona la infraestructura necesaria para gestionar las contribuciones, revisar los cambios, gestionar los problemas del proyecto y mantener una documentación exhaustiva. Este enfoque colaborativo ha hecho de GitHub un componente esencial de los flujos de trabajo de desarrollo de software modernos, transformando la forma en que tanto los desarrolladores individuales como las grandes organizaciones abordan la gestión de proyectos y el intercambio de código.


### Navegar por GitHub Interface y la estructura del repositorio


La comprensión de la interfaz de GitHub comienza con el reconocimiento de los elementos clave que componen cualquier página de repositorio. La barra de navegación superior contiene varias secciones críticas, incluyendo Código, Incidencias, Pull Requests, Discusiones, Acciones, Proyectos, Seguridad e Insights. Cada sección tiene un propósito específico en el ecosistema de gestión de proyectos, con la sección Código mostrando los archivos y carpetas que componen el proyecto.


La propia estructura del repositorio refleja el enfoque organizativo de los responsables del proyecto. Algunos repositorios contienen un único archivo, quizás un simple script de shell, mientras que otros, como el proyecto de hardware BitX, contienen numerosos archivos organizados en directorios y subdirectorios. El nombre del repositorio aparece en un lugar destacado y sirve tanto de identificador como de breve descripción del propósito del proyecto. Los elementos interactivos esenciales incluyen el botón Watch para recibir notificaciones sobre las actualizaciones del repositorio, el botón Fork para crear copias personales del repositorio, y el botón Star que funciona como un sistema de aprobación de la comunidad similar a un "pulgar hacia arriba".


La sección Acerca de proporciona información crucial sobre el proyecto en un formato condensado, incluyendo una descripción de una línea, información sobre la licencia y detalles clave del proyecto. En el caso del proyecto BitX, esta sección lo identifica como "open source ASIC Bitcoin miner hardware" y especifica la licencia GPL 3.0. Comprender las licencias es especialmente importante porque GitHub funciona como una plataforma de código abierto en la que los repositorios públicos son accesibles a toda la comunidad, pero el contenido sólo puede utilizarse y distribuirse de acuerdo con las normas de cumplimiento de cada licencia.


### Trabajar con ramas y versiones de proyecto


El concepto de ramas representa una de las características más potentes de GitHub para gestionar diferentes versiones y vías de desarrollo dentro de un mismo proyecto. Una rama esencialmente crea una copia o versión modificada del código base principal, permitiendo a los desarrolladores trabajar en características específicas, correcciones de errores o cambios experimentales sin afectar a la línea de desarrollo principal. La rama maestra suele ser la versión predeterminada y más estable del proyecto, mientras que las ramas adicionales se adaptan a diferentes iteraciones, fases de prueba o variantes de productos completamente diferentes.


En el proyecto de hardware BitX, existen múltiples ramas para gestionar las diferentes versiones y configuraciones de hardware. Por ejemplo, la rama Ultra v2 contiene archivos específicos para esa iteración de hardware, mientras que la rama Super 401 se centra en implementaciones que utilizan el chip S21 ASIC para mejorar la eficiencia. Cada rama puede estar varias confirmaciones por delante o por detrás de la rama maestra, lo que indica el alcance de los cambios y la actividad de desarrollo. Al examinar las distintas ramas, los usuarios observarán estructuras de archivos, documentación e incluso representaciones visuales completamente distintas, que reflejan los requisitos y especificaciones exclusivos de cada variante de hardware.


El sistema de ramas evita confusiones entre colaboradores y usuarios al separar claramente las distintas vías de desarrollo. En lugar de mezclar funciones experimentales con versiones estables, o de combinar distintas versiones de hardware en un mismo lugar, las ramas ofrecen una separación clara al tiempo que mantienen la capacidad de fusionar los cambios realizados con éxito en la línea de desarrollo principal cuando sea necesario. Este enfoque organizativo garantiza que los usuarios puedan localizar fácilmente la versión específica que necesitan, mientras que los desarrolladores pueden trabajar en mejoras sin interrumpir el proyecto principal.


### Contribuir a través de los problemas


La sección de incidencias sirve como principal canal de comunicación entre los usuarios y los responsables del proyecto para informar de problemas, sugerir mejoras y documentar errores. Sin embargo, es crucial entender que la sección de Problemas está diseñada específicamente para problemas técnicos legítimos y no para preguntas generales o solicitudes de soporte. Cuando los usuarios se encuentran con fallos reales, comportamientos inesperados o identifican posibles mejoras, la creación de una incidencia bien documentada ayuda a toda la comunidad al llamar la atención sobre problemas que pueden afectar a varios usuarios.


La notificación eficaz de problemas requiere una documentación detallada del problema, que incluya las circunstancias que lo provocaron, los pasos para reproducir el problema y cualquier detalle técnico relevante. El proyecto BitX demuestra este principio a través de varias incidencias cerradas que muestran el proceso de resolución, desde la identificación inicial del problema hasta su resolución final, pasando por el debate en la comunidad. Algunos problemas dan lugar a mejoras en el hardware, como la adición de orificios de montaje para aumentar las opciones de refrigeración, mientras que otros pueden resolverse mediante la educación de los usuarios o actualizaciones de software.


La distinción entre Temas y Debates es importante para mantener una interacción organizada entre la comunidad. Mientras que las Cuestiones se centran en problemas técnicos específicos, la sección Debates ofrece un entorno tipo foro para preguntas, ideas y participación general de la comunidad. Aunque el servidor Discord se ha convertido en el principal canal de comunicación de la comunidad BitX, la sección Debates de GitHub sigue estando disponible para conversaciones más formales o en las que se pueden realizar búsquedas y que se benefician de una documentación permanente y de una referencia fácil.


### Comprender los Pull Requests


Los pull requests representan el mecanismo a través del cual los colaboradores externos proponen cambios en el repositorio de un proyecto. Cuando alguien identifica una mejora, corrección de errores o nueva función que beneficiaría al proyecto, puede crear una solicitud de extracción para enviar sus cambios para su revisión y posible integración en el código base principal. Este proceso garantiza que todas las modificaciones se someten a revisión antes de pasar a formar parte del proyecto oficial, lo que mantiene la calidad del código y la coherencia del proyecto al tiempo que permite las contribuciones de la comunidad.


El flujo de trabajo de la solicitud de extracción suele comenzar cuando un colaborador bifurca el repositorio, crea su propia copia en la que puede realizar cambios y, a continuación, envía esos cambios al proyecto original a través de una solicitud de extracción. Los responsables del proyecto pueden entonces revisar los cambios propuestos, discutir las modificaciones con el colaborador y, en última instancia, decidir si fusionar los cambios en el proyecto principal. Este proceso de revisión colaborativa ayuda a mantener los estándares del proyecto al tiempo que fomenta la participación y la mejora de la comunidad.


Entender las etiquetas y las versiones añade otra capa a la gestión de proyectos y al control de versiones. Las etiquetas sirven como marcadores en la línea de tiempo de desarrollo, identificando puntos específicos que representan versiones particulares o hitos. En proyectos de hardware como BitX, las etiquetas a menudo corresponden a números de modelo específicos o revisiones de hardware, proporcionando puntos de referencia claros para los usuarios que buscan versiones particulares. Las versiones, más habituales en los proyectos de software, representan distribuciones formales de funciones y correcciones de errores, a menudo acompañadas de notas detalladas y paquetes descargables.


El ecosistema de GitHub crea un entorno integral para la colaboración de código abierto que va mucho más allá del simple intercambio de archivos. Mediante la comprensión de estos diversos componentes y su uso adecuado, los contribuyentes pueden participar eficazmente en proyectos, ayudar a mejorar los diseños de software y hardware, y beneficiarse de los conocimientos colectivos y el esfuerzo de la comunidad mundial de desarrollo. GitHub proporciona las herramientas y la estructura necesarias para una colaboración significativa en el mundo del código abierto, ya sea informando de problemas, sugiriendo mejoras o aportando código.


## Contribución práctica al código abierto

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Partiendo de la base de crear issues y explorar proyectos de código abierto, este capítulo se centra en los aspectos prácticos de hacer contribuciones directas mediante pull requests y gestión de repositorios. La comprensión de cómo fork repositorios, hacer cambios, y presentar solicitudes de extracción representa un conjunto de habilidades cruciales para cualquier desarrollador que quiera contribuir de manera significativa a los proyectos de código abierto, ya se trate de desarrollo de software o diseño de hardware.


El proceso de aportar cambios al código sigue un flujo de trabajo estandarizado que garantiza la integridad del proyecto al tiempo que permite el desarrollo colaborativo. Este flujo de trabajo implica crear tu propia copia del repositorio de un proyecto, realizar modificaciones en un entorno controlado y, a continuación, proponer esos cambios al proyecto original a través de un proceso de revisión formal. Aunque los ejemplos de este capítulo se centran principalmente en las contribuciones de software, los mismos principios y procedimientos se aplican igualmente a los proyectos de hardware que implican diseños de PCB, esquemas y otra documentación técnica.


### Comprender las horquillas y la estructura de los repositorios


La base de la contribución a cualquier proyecto de código abierto comienza con la creación de una fork, que sirve como su copia personal del repositorio original. Cuando navegas a un repositorio de GitHub y haces clic en el botón "fork", creas una copia independiente bajo tu propia cuenta de GitHub que mantiene una clara conexión con la fuente original. Este repositorio bifurcado aparece en tu cuenta con una clara indicación de su origen, mostrando texto como "bifurcado desde [propietario original]/[nombre-del-repositorio]" bajo el título del repositorio.


Tu repositorio bifurcado opera independientemente del original, permitiéndote hacer cambios sin afectar al proyecto principal. Sin embargo, mantiene el conocimiento de las actualizaciones del repositorio original a través de las funciones de sincronización de GitHub. Cuando el repositorio original recibe actualizaciones de las que carece tu fork, GitHub muestra información de estado como "Esta rama está X commits por detrás" o "X commits por delante", proporcionando una clara visibilidad de la relación entre tu fork y el repositorio upstream. Puedes sincronizar tu fork con el repositorio original en cualquier momento haciendo clic en el botón "Sync fork", que extrae los últimos cambios de la fuente upstream.


La relación entre tu fork y el repositorio original cobra especial importancia cuando empiezas a realizar cambios. A medida que implementa modificaciones y las confirma en su fork, GitHub realiza un seguimiento de estas diferencias y las muestra como confirmaciones por delante del repositorio original. Este sistema de seguimiento permite el proceso de solicitud de extracción, donde puede proponer sus cambios para su inclusión en el proyecto principal, manteniendo un historial claro de lo que se ha modificado.


### Configuración del entorno de desarrollo


Crear un entorno de desarrollo eficaz requiere prestar especial atención tanto a las herramientas de desarrollo generales como a los requisitos específicos del proyecto. Visual Studio Code es un excelente entorno de desarrollo integrado (IDE) para la mayoría de las contribuciones de código abierto, ya que ofrece funciones esenciales para la edición de código, la integración del control de versiones y la gestión de proyectos. El primer componente crítico consiste en instalar y configurar la extensión Git, que permite una integración perfecta con los repositorios de GitHub directamente desde el entorno de desarrollo.


Las versiones modernas de Visual Studio Code suelen incluir soporte Git por defecto, pero debes autenticarte con tu cuenta de GitHub para habilitar la funcionalidad completa. Este proceso de autenticación implica iniciar sesión en GitHub a través del IDE, lo que permite clonar repositorios, confirmar cambios y enviar actualizaciones directamente desde el entorno de desarrollo. La integración con GitHub aparece como un icono en la barra lateral izquierda, proporcionando acceso a las funciones de clonación de repositorios, gestión de ramas y sincronización sin necesidad de operaciones de línea de comandos.


Para los proyectos que implican sistemas embebidos o plataformas de hardware específicas, se hacen necesarias herramientas adicionales. La extensión ESP-IDF representa un componente crucial para los proyectos dirigidos a microcontroladores ESP32, y requiere una compatibilidad de versión específica para garantizar una funcionalidad adecuada. El proceso de instalación implica la selección de la versión apropiada de ESP-IDF, la configuración de las rutas de las herramientas y la configuración del entorno contenedor de desarrollo. La versión 5.1.3 representa actualmente la configuración recomendada para muchos proyectos basados en ESP32, aunque estos requisitos pueden evolucionar a medida que los proyectos actualicen sus dependencias y cadenas de herramientas.


### Realización de cambios y gestión de commits


Una vez que su entorno de desarrollo está correctamente configurado, el proceso de hacer contribuciones significativas comienza con la descarga o clonación de su repositorio a su máquina local. Puedes hacerlo descargando un archivo ZIP con el contenido del repositorio o utilizando la funcionalidad de clonación integrada de Visual Studio Code, que proporciona un flujo de trabajo más ágil para el desarrollo en curso. El proceso de clonación crea una copia local de tu repositorio que permanece sincronizada con tu GitHub fork, permitiéndote trabajar sin conexión mientras mantienes las capacidades de control de versiones.


Cuando trabajas con el repositorio local, obtienes acceso a la estructura completa del proyecto, incluidos los archivos de código fuente, los archivos de configuración, la documentación y cualquier archivo de diseño de hardware. La mayoría de los proyectos de firmware utilizan lenguajes de programación como C para la funcionalidad principal, con componentes adicionales escritos en TypeScript para interfaces de usuario o Java para utilidades específicas. La comprensión de la estructura del proyecto le ayuda a identificar los archivos apropiados para modificar y asegura que sus cambios se alinean con los patrones arquitectónicos del proyecto y las normas de codificación.


El proceso de confirmación representa un aspecto fundamental del control de versiones que requiere una cuidadosa atención tanto a la precisión técnica como a la claridad de la comunicación. Antes de realizar cambios, hay que conocer a fondo el código existente y probar las modificaciones en el entorno local. La regla fundamental de la contribución al código abierto es no publicar nunca código no probado, ya que puede introducir errores o vulnerabilidades de seguridad que afecten a toda la comunidad del proyecto. Además, nunca debes publicar información sensible como contraseñas, tokens API o credenciales personales en repositorios públicos, ya que esta información queda permanentemente accesible para cualquiera que tenga acceso al repositorio.


### Creación y gestión de Pull Requests


La culminación de su esfuerzo de contribución implica la creación de una pull request, que sirve como propuesta formal para fusionar sus cambios en el repositorio original del proyecto. Este proceso comienza en tu fork de GitHub, donde puedes revisar las diferencias entre tu repositorio y el de origen. La interfaz de GitHub muestra claramente el número de commits por delante o por detrás, proporcionando una visibilidad inmediata del alcance de los cambios propuestos. Antes de crear una solicitud de extracción, debe asegurarse de que su fork está sincronizado con los últimos cambios para minimizar posibles conflictos.


Para crear una pull request eficaz no basta con enviar los cambios en el código. La descripción de la solicitud de extracción le brinda la oportunidad de comunicar el propósito, el alcance y el impacto de sus modificaciones a los mantenedores del proyecto y a la comunidad. Una descripción bien redactada explica qué problemas abordan los cambios, cómo se ha implementado la solución y las posibles implicaciones para otras partes del proyecto. Esta documentación es especialmente importante cuando se trata de cambios complejos que no resultan evidentes al examinar las diferencias en el código.


El proceso de revisión representa un aspecto colaborativo del desarrollo de código abierto en el que los responsables del proyecto y colaboradores experimentados evalúan los cambios propuestos. Puede solicitar revisores específicos que tengan experiencia en las áreas a las que afectan sus cambios, asegurándose de que miembros de la comunidad con conocimientos examinan su trabajo. El proceso de revisión puede implicar múltiples iteraciones, en las que los revisores aportan comentarios, solicitan modificaciones o piden pruebas adicionales. Este proceso de perfeccionamiento colaborativo ayuda a mantener la calidad del código al tiempo que proporciona valiosas oportunidades de aprendizaje para colaboradores de todos los niveles de experiencia.


Comprender que no todas las pull requests son aceptadas ayuda a establecer expectativas adecuadas para el proceso de contribución. Los responsables del proyecto pueden rechazar pull requests por varias razones, como la falta de alineación con los objetivos del proyecto, la insuficiencia de pruebas o la existencia de soluciones alternativas ya en desarrollo. En lugar de ver el rechazo como un fracaso, debe considerarse una oportunidad para aprender de los comentarios, perfeccionar el enfoque y, potencialmente, aportar soluciones alternativas que satisfagan mejor las necesidades del proyecto. La comunidad del código abierto se nutre de este proceso iterativo de propuesta, revisión y perfeccionamiento que, en última instancia, impulsa los proyectos mediante el esfuerzo colectivo y la experiencia compartida.



## ¿Qué es Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool representa un enfoque revolucionario para Bitcoin mining que aborda muchas de las preocupaciones que los mineros tienen con los pools tradicionales de mining. Como fondo de Bitcoin mining de código abierto, Public Pool cambia radicalmente el modelo de distribución de recompensas al que los mineros están acostumbrados. A diferencia de los pools mining convencionales, en los que los participantes comparten las recompensas cuando cualquier minero del pool encuentra un bloque, Public Pool funciona según el principio de mining en solitario, en el que los mineros individuales retienen el 100% de sus recompensas por bloque cuando minan con éxito un bloque.


La característica más atractiva de Public Pool es su estructura sin comisiones. Cuando los mineros encuentran con éxito un bloque utilizando Public Pool, reciben la recompensa completa del bloque junto con todas las tarifas de transacción asociadas, sin ninguna deducción por los costes de funcionamiento del pool. Esto contrasta fuertemente con los pools mining tradicionales, que suelen cobrar comisiones que oscilan entre el 1% y el 3% de las recompensas mining. El modelo sin comisiones hace que Public Pool resulte especialmente atractivo para los mineros que desean maximizar sus beneficios potenciales al tiempo que mantienen un control total sobre sus operaciones de mining.


Para entender la posición única de Public Pool, es importante comprender la diferencia fundamental entre mining en solitario y mining agrupado. mining en solitario significa que usted mina de forma independiente y recibe la recompensa completa del bloque (actualmente 3,125 BTC + tasas) si encuentra un bloque, pero la probabilidad es proporcional a su tasa de hash frente a toda la red, lo que crea una variación extrema que puede durar meses o años entre recompensas. Los pools tradicionales combinan la potencia de hash para encontrar bloques con mayor frecuencia, distribuyendo las recompensas proporcionalmente y proporcionando ingresos estables y predecibles. Para los mineros con un importante capital invertido en hardware y costes operativos, la mining en solitario pura suele ser poco práctica, independientemente de sus ventajas filosóficas: la varianza hace casi imposible cubrir los costes de electricidad y recuperar las inversiones. Esta realidad económica significa que la mayoría de los mineros elegirán mining agrupados por razones financieras prácticas. Public Pool funciona como un pool de mining en solitario, lo que significa que usted sigue enfrentándose a la varianza de mining en solitario (sólo obtiene recompensa cuando encuentra personalmente un bloque), pero se beneficia de la infraestructura del pool y de un funcionamiento transparente y sin comisiones.


### La ventaja del código abierto y su aplicación técnica


El compromiso de Public Pool con el desarrollo de código abierto proporciona a los mineros una transparencia y un control sin precedentes sobre sus operaciones con mining. Todo el código base está disponible en GitHub, lo que permite a los mineros examinar exactamente cómo funciona el software, modificarlo según sus necesidades e incluso contribuir a su desarrollo. Esta transparencia aborda una preocupación significativa en la comunidad mining con respecto a las configuraciones y prácticas desconocidas de los pools mining tradicionales.


La arquitectura del software incluye tanto la funcionalidad central de mining Pool como un repositorio de interfaz de usuario independiente, ambos disponibles gratuitamente para su descarga y modificación. Los mineros pueden ejecutar Public Pool en varias configuraciones, incluidos contenedores Docker, lo que lo hace adaptable a diferentes configuraciones de hardware y preferencias técnicas. La completa documentación proporcionada en los repositorios de GitHub ofrece guías detalladas de instalación, opciones de configuración e instrucciones de modificación, lo que lo hace accesible a mineros con distintos niveles de conocimientos técnicos.


La conexión a Public Pool requiere una configuración mínima en comparación con las configuraciones tradicionales de mining. Los mineros sólo tienen que configurar sus dispositivos mining con los detalles de conexión de Stratum y proporcionar su dirección Bitcoin como nombre de usuario. Se puede añadir un nombre de trabajador opcional después de un separador de puntos con fines organizativos.


### Características de la Comunidad y modelo de sostenibilidad


Public Pool incorpora varias características innovadoras que refuerzan la comunidad Bitcoin mining al tiempo que mantiene su funcionamiento sin comisiones. La plataforma muestra estadísticas exhaustivas, incluida la tasa total de hash de los mineros conectados, que solía oscilar entre 1 y 2 PetaHash por segundo en 2024 y alrededor de 40 PH/s en noviembre de 2025, y proporciona información detallada sobre los dispositivos mining conectados. Cabe destacar el énfasis de la plataforma en el hardware mining de código abierto, con dispositivos marcados con estrellas que indican diseños totalmente de código abierto, con enlaces a sus respectivos repositorios de GitHub.


La sostenibilidad del funcionamiento sin comisiones de Public Pool se basa en una creativa asociación de programas de afiliación con proveedores de hardware de mining. Cuando los mineros compran equipos de las empresas asociadas utilizando el código de descuento "SOLO", el cincuenta por ciento de los ingresos de los afiliados sirven para sufragar los costes operativos de Public Pool, mientras que el cincuenta por ciento restante se distribuye como recompensa a los mineros que consiguen los porcentajes de dificultad más altos cada mes. Este modelo crea una relación simbiótica en la que los mineros reciben descuentos en la compra de equipos, los proveedores ganan clientes y Public Pool mantiene sus operaciones sin cobrar comisiones directas.


### Filosofía y buenas prácticas de la descentralización


Aunque Public Pool ofrece una excelente alternativa a los pools tradicionales de mining, es importante entender su papel en el contexto más amplio de la descentralización de Bitcoin. La plataforma sirve como trampolín hacia el objetivo final de que cada minero gestione su propio pool de mining. Gestionar tu propio pool de mining representa el máximo nivel de descentralización, ya que elimina la dependencia de cualquier infraestructura o software de terceros, independientemente de lo transparentes o bienintencionados que sean.


La naturaleza de código abierto de Public Pool la convierte en una plataforma de aprendizaje ideal para los mineros que deseen comprender el funcionamiento del pool antes de implementar sus propias soluciones. La disponibilidad de guías de instalación para múltiples sistemas operativos y la exhaustiva documentación proporcionan a los mineros los conocimientos necesarios para pasar de utilizar Public Pool a operar su propia infraestructura de mining. Este aspecto educativo se alinea con los principios fundamentales de Bitcoin de auto-soberanía y descentralización, capacitando a los mineros individuales para tomar el control completo de sus operaciones mining al tiempo que contribuyen a la seguridad general y la descentralización de la red Bitcoin.


La interfaz de usuario de la plataforma ofrece a los mineros funciones de supervisión detalladas, como el estado de los trabajadores, estadísticas de tasa de hash y métricas de rendimiento. Estas funciones ayudan a los mineros a optimizar sus operaciones al tiempo que aprenden principios de gestión de pools que pueden aplicar posteriormente a sus propias implementaciones de pools mining.


## Cómo instalar Public-Pool en Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Gestionar su propia piscina Bitcoin mining en casa es cada vez más accesible gracias al hardware moderno y a las soluciones de software simplificadas. Este capítulo explora la implementación práctica de una piscina pública en casa utilizando hardware de mini PC asequible y software de gestión de nodos simplificado. Al final de esta guía, comprenderá los requisitos de hardware, el proceso de instalación del software y la configuración básica necesarios para establecer su propia infraestructura de mining.


### Requisitos de hardware y configuración


La base de cualquier instalación doméstica de una piscina mining comienza con la selección de un hardware adecuado que equilibre rendimiento, coste y eficiencia energética. Un mini PC representa una solución ideal para esta aplicación, ya que ofrece suficiente capacidad de procesamiento y, al mismo tiempo, ocupa poco espacio y tiene un consumo de energía razonable. La configuración recomendada incluye un procesador Intel N100, que proporciona los recursos computacionales adecuados para las operaciones de pool, junto con al menos un terabyte de almacenamiento NVMe para acomodar el blockchain Bitcoin y los datos asociados.


El requisito de almacenamiento es especialmente crítico, ya que la ejecución de un grupo mining requiere el mantenimiento de un nodo Bitcoin totalmente sincronizado. La unidad NVMe de un terabyte garantiza operaciones rápidas de lectura/escritura esenciales para la sincronización del blockchain y el procesamiento de transacciones en curso. Además, la asignación de RAM suficiente permite un funcionamiento sin problemas tanto del sistema operativo Linux subyacente como del software de gestión de nodos que coordinará las actividades del pool.


### Arquitectura de software y gestión de nodos


La pila de software para una mining doméstica se basa en Linux, que proporciona la estabilidad y seguridad necesarias para las operaciones de Bitcoin. Sobre este sistema base, un software especializado de gestión de nodos como Umbrel crea una interfaz intuitiva para gestionar la infraestructura de Bitcoin. Sobre este sistema base, un software especializado de gestión de nodos como Umbrel crea una interfaz intuitiva para gestionar la infraestructura de Bitcoin. Este enfoque abstrae gran parte de la complejidad tradicionalmente asociada al funcionamiento de los nodos de Bitcoin, lo que hace que el funcionamiento del grupo sea accesible para usuarios sin grandes conocimientos técnicos.


Umbrel es una completa plataforma de gestión de nodos que se encarga de la instalación, sincronización y mantenimiento continuo de Bitcoin Core a través de una interfaz basada en web. El modelo de tienda de aplicaciones de la plataforma permite instalar fácilmente servicios adicionales, incluido el software de mining pool, mediante sencillas operaciones de apuntar y hacer clic. Esta arquitectura garantiza que los usuarios puedan centrarse en el funcionamiento del grupo en lugar de en la administración del sistema, al tiempo que mantienen un control total sobre su infraestructura Bitcoin.


### Instalación y configuración de piscinas públicas


La instalación de software de piscina pública a través de la plataforma Umbrel demuestra la naturaleza racionalizada de la moderna implantación de infraestructuras Bitcoin. El proceso comienza con el acceso a la tienda de aplicaciones Umbrel a través de la interfaz web, donde una simple búsqueda de "piscina pública" revela el software de piscina mining disponible. La instalación sólo requiere unos pocos clics: seleccionar la aplicación, confirmar la instalación y esperar a que finalice el proceso de configuración automatizado.


El proceso de instalación configura automáticamente las conexiones necesarias entre el software del pool público y el nodo Bitcoin subyacente. Esta integración garantiza que el pool pueda validar transacciones, construir plantillas de bloques y distribuir trabajo a los mineros conectados sin necesidad de configurar manualmente complejos parámetros de red. Una vez finalizada la instalación, se puede acceder inmediatamente a la interfaz del pool a través de la red local, lo que proporciona capacidades de supervisión y gestión en tiempo real.


### Conexión de mineros y consideraciones sobre la red


Conectar el hardware mining a su pool recién establecido requiere configurar los ajustes del pool del minero para que apunte a su infraestructura local. Esto implica sustituir la dirección por defecto del pool por tu dirección IP local y el número de puerto apropiado asignado durante la instalación del pool público. El cambio de configuración redirige los esfuerzos computacionales de su hardware mining desde pools externos a su infraestructura doméstica, permitiéndole mantener el control total sobre las operaciones y las posibles recompensas de mining.


La configuración de la red desempeña un papel crucial en la accesibilidad y funcionalidad de la piscina. La configuración de la red local suele implicar un direccionamiento IP estándar, pero los usuarios pueden encontrarse con variaciones en la resolución DNS dependiendo de la configuración de su router. Algunos routers proporcionan servicios DNS locales que crean nombres amigables para los servicios locales, mientras que otros requieren acceso directo a la dirección IP. Para una mayor accesibilidad más allá de la red local, puede ser necesaria la configuración de reenvío de puertos en el router, aunque esto introduce consideraciones de seguridad adicionales que requieren una evaluación cuidadosa de los riesgos y beneficios asociados.


El establecimiento satisfactorio de un grupo de mining doméstico representa un paso importante hacia la infraestructura descentralizada de Bitcoin, ya que proporciona tanto valor educativo como capacidades prácticas de mining, al tiempo que mantiene un control total sobre sus operaciones de Bitcoin.


# Montaje de hardware y solución de problemas

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## ¿Qué herramientas utilizar?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

En el mundo de la soldadura de dispositivos de montaje superficial (SMD), especialmente cuando se trabaja con proyectos Bitaxe, disponer de las herramientas adecuadas marca la diferencia entre la frustración y el éxito. Esta completa guía cubre el equipo esencial necesario para abordar proyectos de soldadura SMD con eficacia, desde herramientas manuales básicas hasta equipos especializados que elevarán sus capacidades de soldadura.


Si quieres consultar documentación sobre los esquemas, consulta este [repositorio de GitHub](https://github.com/skot/bitaxe-doc/tree/main).


### Herramientas manuales básicas e instrumentos de precisión


La base de cualquier configuración de soldadura SMD comienza con unas pinzas de calidad, que sirven como herramientas principales para la colocación de componentes. Hay dos tipos de pinzas que resultan muy útiles para este trabajo: las pinzas estándar de punta recta y las que tienen una ligera curvatura en la punta. Las de punta recta sirven para la mayoría de los componentes SMD que se encuentran en los kits Bitaxe, mientras que las pinzas con la punta doblada son excelentes cuando se trabaja con componentes extremadamente pequeños que requieren una colocación precisa. Estas herramientas suelen venir incluidas en los kits de reparación, como los de iFixit diseñados para reparar teléfonos, por lo que son fácilmente accesibles para la mayoría de los aficionados.


Como complemento de las pinzas, unas buenas tijeras resultan indispensables para cortar cinta aislante, que tiene múltiples usos en los proyectos de electrónica. La cinta aislante es esencial para aislar cables y componentes, y disponer de cinta de calidad agiliza el proceso de soldadura. Estos suministros básicos pueden adquirirse en ferreterías o tiendas en línea sin necesidad de recurrir a proveedores especializados en electrónica.


### Aplicación y gestión de la pasta de soldadura


La aplicación de pasta de soldadura representa uno de los aspectos más críticos de la soldadura SMD, y las herramientas adecuadas hacen que este proceso sea a la vez preciso y agradable. Las pequeñas jeringas no afiladas llenas de pasta de soldadura proporcionan un control excepcional sobre la colocación de la pasta. Este método permite la aplicación precisa de la cantidad exacta de pasta de soldadura necesaria para cada unión, y la mayoría de las personas desarrollan rápidamente la técnica adecuada para controlar la presión y el caudal mediante la práctica.


La elección de la pasta de soldar influye significativamente en el éxito de la soldadura. ChipQuik TS391SNL50 destaca como una pasta de soldadura excepcional para proyectos Bitaxe y trabajos SMD en general. Esta pasta mantiene una consistencia y unas características de fusión adecuadas, evitando los problemas asociados a alternativas más baratas que tienen puntos de fusión excesivamente bajos. Las pastas de soldadura de baja calidad pueden crear problemas en los que las uniones previamente soldadas se vuelven fluidas de nuevo al calentar las zonas adyacentes, lo que provoca el desplazamiento de componentes y conexiones deficientes. Aunque la pasta de soldar de calidad representa una inversión inicial más elevada, la mejora de los resultados y la reducción de la frustración justifican el gasto.


### Herramientas de solución de problemas y limpieza


Incluso los soldadores experimentados se encuentran con problemas que requieren corrección, por lo que el equipo de desoldadura es esencial para cualquier kit de herramientas completo. Un equipo de desoldadura, básicamente una herramienta de vacío calefactada, elimina el exceso de soldadura y corrige las conexiones puenteadas entre las patillas de los componentes. Estas herramientas son más eficaces cuando se combinan con fundente, que mejora el flujo de la soldadura y ayuda a que el proceso de desoldadura sea más eficaz.


El fundente se presenta en diversas formas, tanto sólido como líquido, y tiene múltiples funciones, además de ayudar a desoldar. Cuando la pasta de soldadura empieza a perder su eficacia durante sesiones de trabajo prolongadas, la aplicación de fundente adicional restablece las características de flujo adecuadas y garantiza conexiones fiables. Una pequeña herramienta en forma de cuchara, que suele encontrarse en los kits de reparación de precisión, facilita la aplicación precisa de fundente en zonas específicas sin contaminar los componentes circundantes.


La limpieza del tablero representa el último paso en un trabajo de calidad profesional, y requiere alcohol isopropanol y un cepillo de limpieza específico. Un cepillo de dientes viejo funciona perfectamente para este fin, y una botella exprimible que contenga isopropanol permite una aplicación controlada de la solución limpiadora. Esta combinación elimina los residuos de fundente y los restos de pasta, dejando las placas con un aspecto limpio y profesional que también facilita la inspección de las juntas de soldadura.


### Equipos especializados y herramientas avanzadas


En proyectos con circuitos integrados complejos, especialmente ASIC, las plantillas transforman el tedioso proceso de soldadura manual en una aplicación eficaz y precisa de la pasta. Estas plantillas cortadas con precisión garantizan un grosor y una colocación uniformes de la pasta, lo que reduce drásticamente el tiempo necesario para componentes complejos al tiempo que mejora la fiabilidad. La inversión en patrones de calidad se traduce en ahorro de tiempo y mejores resultados.


La gestión térmica resulta crucial cuando se trabaja con componentes de potencia, por lo que la pasta térmica o la grasa térmica son suministros esenciales. Estos materiales garantizan una transferencia de calor adecuada entre los disipadores térmicos y los circuitos integrados, evitando daños térmicos y asegurando un funcionamiento fiable. Los materiales de interfaz térmica de calidad representan una pequeña inversión que protege componentes mucho más caros.


El corazón de cualquier equipo de soldadura SMD es la estación de retrabajo de aire caliente, que proporciona el calor controlado necesario para el trabajo de montaje superficial. Aunque las estaciones económicas de entre 30 y 50 dólares pueden funcionar adecuadamente, a menudo carecen de la fiabilidad y precisión de los equipos de gama alta. Estas estaciones básicas suelen funcionar eficazmente a 355 °C e incluyen una reducción automática de la temperatura cuando la pieza de mano vuelve a su soporte. Sin embargo, su fiabilidad puede ser irregular y algunas unidades fallan prematuramente. Para un trabajo serio, la inversión en equipos de mayor calidad de proveedores electrónicos especializados proporciona un mejor valor a largo plazo gracias a una mayor fiabilidad y un control más preciso de la temperatura.


La combinación de estas herramientas crea una completa capacidad de soldadura SMD que se extiende mucho más allá de los proyectos Bitaxe para trabajos de electrónica en general. Comprender la función de cada herramienta y seleccionar el equipo de calidad adecuado para su nivel de habilidad y los requisitos del proyecto garantiza resultados satisfactorios y una experiencia de soldadura agradable.



## Solucionar problemas de soldadura

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


El kit de transceptor Bitaxe presenta desafíos únicos durante el montaje que requieren una cuidadosa atención a la orientación de los componentes, la prevención de puentes de soldadura y la gestión adecuada del calor. Comprender estos problemas comunes y sus soluciones es esencial para construir con éxito el kit y evitar costosos daños en los componentes. Este capítulo examina los problemas de soldadura más frecuentes encontrados durante el montaje de Bitaxe y proporciona técnicas prácticas para identificarlos y resolverlos.


### Orientación e identificación de componentes


La correcta orientación de los componentes representa uno de los aspectos más críticos para el éxito del montaje de Bitaxe, especialmente con los MOSFET Q1 y Q2. Estos componentes cuentan con marcadores de orientación distintivos que deben observarse cuidadosamente durante la instalación. Cada MOSFET contiene una pequeña marca que corresponde a una disposición específica de los pads en la placa de circuito. La clave para una orientación correcta reside en comprender la estructura física de estos componentes, que presentan cuatro patillas dispuestas con una almohadilla grande y tres almohadillas más pequeñas que no tienen conexión con la almohadilla grande.


Al instalar Q1 y Q2, examine detenidamente tanto el componente como la placa de circuito. El diseño de la placa muestra claramente la orientación prevista a través de su configuración de pastillas, con cuatro patillas colocadas para que coincidan con la estructura del MOSFET. Antes de soldar un componente grande, compruebe siempre la orientación comparando las marcas físicas del componente con la disposición de los pads de la placa. Este sencillo paso de verificación evita la frustración de desoldar y volver a instalar componentes mal orientados.


Las consecuencias de una orientación incorrecta van más allá de simples problemas de funcionalidad. Los MOSFET mal orientados pueden crear fallos en el circuito difíciles de diagnosticar y que pueden requerir la sustitución completa de los componentes. Tomarse el tiempo necesario para verificar la orientación antes de aplicar calor garantiza el correcto funcionamiento del circuito y evita problemas innecesarios en fases posteriores del proceso de montaje.


### Gestión de puentes de soldadura y excesos de soldadura


Los puentes de soldadura representan otro reto común en el ensamblaje Bitaxe, especialmente alrededor de componentes de paso fino como U10. Estas conexiones no deseadas entre patillas adyacentes pueden provocar fallos en el funcionamiento del circuito y requieren técnicas de eliminación cuidadosas. El método más eficaz consiste en utilizar una mecha desoldadora, un material trenzado de cobre que absorbe el exceso de soldadura cuando se calienta. Esta técnica requiere paciencia y una selección adecuada de la herramienta para evitar dañar componentes delicados.


Cuando trate puentes de soldadura en circuitos integrados, utilice un soporte para PCB o una pinza articulada para sujetar firmemente el componente mientras trabaja. Aplique un calor suave en la zona afectada y pase con cuidado la mecha desoldadora por las conexiones puenteadas. El trenzado de cobre absorbe de forma natural el exceso de soldadura, separando las conexiones no deseadas. Este proceso puede requerir varios intentos, pero la persistencia produce conexiones limpias y correctamente separadas.


La prevención sigue siendo el mejor enfoque para la gestión de puentes de soldadura. Utilizar cantidades adecuadas de pasta de soldar y mantener un control manual firme durante la colocación de los componentes reduce significativamente la formación de puentes. Cuando se produzcan puentes, resuélvalos inmediatamente en lugar de esperar que no afecten al funcionamiento del circuito. Incluso puentes aparentemente menores pueden causar problemas significativos de funcionalidad que son difíciles de diagnosticar una vez que la placa está completamente montada.


### Componentes críticos y consideraciones especiales


El convertidor buck U9 merece especial atención debido a su papel crítico en la conversión de 5 voltios a 1,2 voltios para el chip ASIC. Este componente presenta retos únicos debido a sus cinco pequeñas conexiones y a su tendencia al fallo. Su correcta instalación requiere una aplicación precisa de pasta de soldadura y una cuidadosa gestión del calor. Una cantidad insuficiente de pasta de soldadura bajo el U9 puede dar lugar a conexiones deficientes que impidan una conversión de voltaje adecuada, mientras que un exceso de pasta puede crear puentes que provoquen un mal funcionamiento del circuito.


U9 produce firmas de audio distintivas cuando experimenta problemas en el puente de soldadura, generando ruido de alta frecuencia que difiere del funcionamiento normal de ASIC. Esta técnica de diagnóstico auditivo puede ayudar a identificar problemas, aunque requiere una buena audición de alta frecuencia para detectarla. Cuando el diagnóstico auditivo no es posible, la inspección visual resulta esencial. Examine cuidadosamente todas las conexiones, buscando puentes o una cobertura de soldadura insuficiente.


Si U9 no emite los 1,2 voltios requeridos a pesar de parecer que está bien soldado, considere que la causa probable es una cantidad insuficiente de pasta de soldar. Retire el componente, aplique una pequeña cantidad de pasta de soldadura adicional y vuelva a instalarlo. En los casos en los que las patillas individuales carezcan de una cobertura de soldadura adecuada, aplique con cuidado pequeñas cantidades de pasta de soldadura en lugares específicos utilizando unas pinzas. La pasta de soldar fluirá naturalmente bajo el componente cuando se caliente, creando conexiones adecuadas a través de la acción capilar.


### Gestión del calor y protección de componentes


Una gestión adecuada del calor protege los componentes sensibles de los daños térmicos, al tiempo que garantiza la fiabilidad de las uniones soldadas. Los componentes como el oscilador de cristal Y1 y U1 son especialmente sensibles a la exposición prolongada al calor y requieren un control cuidadoso de la temperatura. Mantenga la temperatura del soldador a 350 grados Celsius, pero minimice el tiempo de aplicación de calor para evitar daños en los componentes. Unas técnicas de soldadura rápidas y eficaces protegen estos componentes sensibles a la vez que consiguen conexiones fiables.


El chip ASIC requiere técnicas de manipulación especiales debido a su compleja estructura de patillas y a su sensibilidad a la tensión mecánica. Cuando utilice plantillas para la aplicación de pasta de soldadura, asegúrese de que la cobertura sea uniforme en todas las patillas para evitar que los componentes se asienten de forma irregular. Si un exceso de pasta de soldadura hace que el ASIC se asiente de forma irregular, deje que el conjunto se enfríe por completo antes de realizar correcciones. Aplique una ligera presión sólo en los bordes etiquetados del componente, nunca en el área central del troquel, mientras recalienta para lograr un asentamiento adecuado.


El componente U8 presenta desafíos únicos debido a sus numerosas patillas y a la posibilidad de que se doblen los cables. Si las patillas se doblan durante la manipulación, utilice un soporte para placas de circuito impreso o una pinza articulada para fijar el componente y enderezar con cuidado las patillas afectadas. Trabaje despacio y con paciencia para evitar romper los delicados cables. Comprender que ciertos grupos de patillas del U8 están conectados internamente puede simplificar la resolución de problemas, ya que los puentes entre estas patillas específicas no afectan al funcionamiento del circuito. Sin embargo, los puentes entre otros pines requieren una eliminación cuidadosa para garantizar una funcionalidad adecuada.


## Cómo depurar tu Bitaxe usando AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Cuando se trabaja con dispositivos Bitaxe mining, los fallos de hardware pueden manifestarse de varias formas que pueden no ser inmediatamente obvias. Entender cómo diagnosticar sistemáticamente estos problemas utilizando el sistema operativo AxeOS puede ahorrar mucho tiempo y evitar sustituciones innecesarias de componentes. Este capítulo explora las técnicas de diagnóstico y las metodologías de resolución de problemas que los técnicos experimentados utilizan para identificar problemas específicos de hardware a través del análisis del software.


### Indicadores de consumo de energía


El primer y más crítico indicador de diagnóstico en AxeOS es la monitorización del consumo de energía. Los dispositivos Bitaxe normales, incluyendo los modelos Bitaxe Ultra y Bitaxe Supra, suelen consumir entre 10 y 17 vatios durante su funcionamiento estándar. Esta medida de referencia sirve como indicador principal de la salud de todo el sistema. Cuando el consumo de energía cae significativamente por debajo de este rango, en particular por debajo de 3 vatios, es señal de un problema fundamental con el chip ASIC o sus circuitos de apoyo.


Los escenarios de bajo consumo de energía requieren atención inmediata porque indican que el chip mining no funciona en absoluto u opera en un estado gravemente degradado. Esta medición por sí sola puede ayudarle a diferenciar rápidamente entre problemas de rendimiento y fallos completos de hardware. La lectura de potencia en AxeOS proporciona información en tiempo real que le permite monitorizar la efectividad de cualquier intento de reparación que realice en el dispositivo.


### Análisis de las mediciones de tensión de ASIC


La función de medición de voltaje ASIC en AxeOS proporciona información de diagnóstico crucial que ayuda a identificar la naturaleza exacta de los problemas de hardware. Al examinar las lecturas de voltaje, es necesario entender la relación entre el voltaje medido y el voltaje solicitado para diagnosticar correctamente los problemas. El sistema muestra tanto el voltaje que se suministra al chip ASIC como el voltaje que el chip solicita al sistema de gestión de energía.


Cuando observe una medición de voltaje de ASIC de exactamente 1,2 voltios combinada con un consumo de energía inferior a 3 vatios, esta combinación específica indica un problema de soldadura con el chip ASIC o un ASIC completamente averiado. Esta lectura de voltaje sugiere que la energía está llegando a la ubicación del chip, pero el chip en sí no está funcionando correctamente. La inspección física del troquel ASIC puede revelar grietas u otros daños visibles que explicarían este patrón de comportamiento.


Un escenario de diagnóstico diferente surge cuando se ve un bajo consumo de energía emparejado con lecturas de voltaje solicitadas muy bajas, como 100 milivoltios o 0,5 voltios. Este patrón indica que el chip ASIC no está recibiendo un suministro de tensión adecuado, lo que normalmente apunta a problemas con el componente convertidor buck U9. El convertidor buck es responsable de proporcionar la regulación de voltaje precisa que los chips ASIC requieren para su correcto funcionamiento.


### Interpretación de datos de registro y comunicación ASIC


El sistema de registro AxeOS proporciona información valiosa sobre si su chip ASIC se está comunicando con el sistema de control. Cuando acceda a los registros a través de la función "show logs", la presencia de entradas "ASIC results" confirma que el chip no sólo está alimentado sino que también está procesando activamente trabajo y devolviendo resultados. Esta comunicación indica que el ASIC está correctamente soldado y mantiene su conexión con el circuito de control.


La ausencia de resultados ASIC en los registros, especialmente cuando se combina con otros síntomas, ayuda a reducir el problema a componentes específicos o problemas de conexión. Este enfoque de diagnóstico permite distinguir entre los chips que no responden en absoluto y los que pueden tener problemas de conexión intermitentes. El análisis de registros resulta especialmente valioso cuando se trata de solucionar problemas complejos en los que varios síntomas pueden sugerir diferentes causas.


### Solución sistemática de problemas


Al diagnosticar problemas de hardware de Bitaxe, seguir un enfoque sistemático evita pasar por alto problemas críticos y garantiza procesos de reparación eficientes. Comience por documentar el consumo de energía y las lecturas de voltaje, luego correlacione estas mediciones con los datos de registro para construir una imagen completa del comportamiento del sistema. Este enfoque metódico ayuda a identificar si los problemas provienen del propio chip ASIC, del sistema de suministro de energía o de las vías de comunicación entre los componentes.


En los casos en los que el problema parezca ser el convertidor Buck U9, puede ser necesaria una inspección física y un posible resoldado. El componente U9 es particularmente susceptible a problemas de soldadura, especialmente en situaciones de primer montaje. Cuando se sospecha de problemas de regulación de tensión, el uso de un multímetro para verificar que 1,2 voltios están realmente presentes en los pines ASIC proporciona una confirmación definitiva de los problemas de suministro de energía. Si hay tensión en las patillas pero la ASIC sigue sin funcionar, y la inspección física no revela daños, el siguiente paso lógico es sustituir el chip ASIC. Si los problemas persisten incluso después de la sustitución de ASIC, el componente U2, que controla el chip ASIC, puede requerir atención como el elemento final en la secuencia de solución de problemas.


## ¿Cómo depurar mediante USB?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Cuando se solucionan problemas en dispositivos Bitaxe mining, tener acceso directo al sistema de registro interno del dispositivo proporciona información muy valiosa que las interfaces basadas en web no pueden ofrecer. Este capítulo explora cómo establecer una conexión serie USB directa a su dispositivo Bitaxe utilizando el framework ESP-IDF, permitiendo la monitorización en tiempo real de los registros del sistema, secuencias de arranque y mensajes de error. Este enfoque de depuración es particularmente crucial cuando se trata de dispositivos que experimentan reinicios frecuentes o fallos de hardware, ya que captura toda la información de diagnóstico que podría perderse durante los reinicios del sistema.


El proceso de depuración requiere Visual Studio Code con la extensión ESP-IDF, aunque se puede utilizar cualquier IDE compatible. Este método funciona con todas las variantes de Bitaxe que incluyen un puerto USB, incluido el Bitaxe Ultra 204 y otros modelos de la serie. La conexión serie directa evita las posibles limitaciones de la interfaz web y proporciona un acceso sin filtros a la información de estado interna del dispositivo.


### Configuración de la comunicación serie


El establecimiento de la comunicación con su dispositivo Bitaxe comienza con la conexión del cable USB y la apertura del terminal ESP-IDF dentro de su entorno de desarrollo. El comando `idf.py monitor` inicia el proceso de conexión, escaneando automáticamente los puertos COM disponibles para establecer la comunicación UART con el chip ESP32 en su dispositivo Bitaxe. El sistema normalmente hace un ciclo a través de los puertos disponibles (COM3, COM4, COM16, etc.) hasta que encuentra la conexión correcta.


Una vez conectado, el terminal muestra la secuencia de arranque completa y los registros operativos en curso. El proceso de conexión inicial puede tardar unos instantes mientras el sistema identifica el puerto de comunicación correcto. Si falla la detección automática de puertos, puede especificar manualmente el puerto COM a través de la interfaz de selección de puertos del IDE. Este canal de comunicación directa permanece activo durante todo el funcionamiento del dispositivo, proporcionando un acceso continuo a los diagnósticos del sistema y a las métricas de rendimiento.


### Interpretación de la secuencia de arranque y de los registros de funcionamiento normal


La secuencia de arranque proporciona información crítica sobre la configuración del hardware de su dispositivo Bitaxe y el proceso de inicialización. Los registros normales de arranque comienzan con la información de la versión ESP-IDF, seguida del distintivo mensaje "Bienvenido al Bitaxe. Hackea el planeta" que confirma que el firmware se ha cargado correctamente. A continuación, el sistema muestra la configuración de frecuencia ASIC, la identificación del modelo del dispositivo y los detalles de la versión de la placa.


Un dispositivo que funcione correctamente mostrará una inicialización I2C exitosa y la regulación de voltaje ASIC ajustada a 1,2 voltios. Los registros muestran información de estado GPIO y secuencias de inicialización Wi-Fi, seguido por la configuración del servidor DHCP y la asignación de la dirección IP. Uno de los indicadores más cruciales es el mensaje de detección de chip ASIC, que debe informar "detectado un chip ASIC" para un dispositivo de un solo chip. Esta confirmación valida que el hardware mining está correctamente conectado y comunicándose con el controlador ESP32.


Los registros operativos revelan múltiples tareas concurrentes que se ejecutan en el dispositivo, incluida la comunicación API del estrato, la coordinación de la tarea principal, la gestión de la tarea ASIC y el procesamiento de la tarea del estrato. Estos diferentes identificadores de tareas ayudan a aislar los problemas en componentes específicos del sistema. El funcionamiento normal incluye el establecimiento de la conexión al pool, los mensajes de ajuste de dificultad, la puesta en cola y retirada de tareas y la generación de informes de nonce. Las operaciones satisfactorias de mining muestran resultados de ASIC con cálculos de dificultad y mining envían confirmaciones cuando las acciones alcanzan el umbral requerido.


### Identificación de fallos de hardware y patrones de error


Los fallos de hardware se manifiestan en los registros a través de patrones de error específicos que indican qué componentes están funcionando mal. El modo de fallo más común implica errores de comunicación I2C con circuitos integrados específicos en la placa Bitaxe. Por ejemplo, los fallos de comunicación DS4432U aparecen como mensajes "ESP_ERROR_CHECK failed" con indicadores de tiempo de espera, señalando problemas de regulación de voltaje o problemas de soldadura que afectan al componente U10 responsable de la comunicación con la pantalla.


Estos mensajes de error incluyen información de depuración detallada, como el archivo fuente específico (main_ds4432u.c), la llamada a la función que falla y el núcleo del procesador que gestiona la tarea. La información de rastreo proporciona contexto adicional para la solución avanzada de problemas. Patrones de error similares pueden ocurrir con el chip de control de temperatura y ventilador EMC2101, cada uno generando firmas de registro distintivas que ayudan a identificar el componente que falla.


Los problemas físicos de hardware suelen presentarse como ciclos de error repetidos seguidos de reinicios del sistema. Si su dispositivo produce ruidos audibles durante el funcionamiento, esto suele indicar problemas de soldadura, como puentes entre las patillas de los componentes o uniones soldadas inadecuadas. Aunque estos problemas mecánicos no siempre generate entradas de registro específicas, crean condiciones de funcionamiento inestables que se manifiestan como bloqueos frecuentes y ciclos de reinicio en la salida de monitorización.


### Estrategias avanzadas de resolución de problemas


La monitorización serie ofrece varias ventajas sobre las interfaces de depuración basadas en web, en particular para fallos intermitentes o dispositivos que experimentan reinicios frecuentes. La captura continua de registros garantiza que no se pierda información de diagnóstico durante los reinicios del sistema, a diferencia de las interfaces web que pueden perder datos durante los eventos de desconexión. Esta completa capacidad de registro permite identificar patrones en los fallos y correlacionar condiciones de error específicas con factores de hardware o ambientales.


Cuando analice dispositivos problemáticos, céntrese en la secuencia de eventos que conducen a los fallos en lugar de en mensajes de error aislados. Una comunicación ASIC correcta debería mostrar ciclos regulares de procesamiento de trabajos, generación de nonce y envío de recursos compartidos. La ausencia de resultados de ASIC en los registros indica fallos de comunicación entre el ESP32 y el chip mining, a menudo causados por problemas de alimentación, trazas dañadas o fallos de componentes.


Para solucionar problemas de forma sistemática, documente los patrones de error y los fallos específicos de cada componente antes de solicitar ayuda a la comunidad. Los registros de errores detallados, que incluyen identificadores de chips específicos y modos de fallo, permiten a los usuarios experimentados proporcionar orientación de reparación específica, como procedimientos de sustitución de componentes o correcciones de soldadura. Este enfoque metódico de la depuración de hardware mejora significativamente las tasas de éxito de las reparaciones y reduce el tiempo de resolución de problemas complejos.


# Personalización avanzada

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Modificar la placa de circuito impreso

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad es una de las herramientas de código abierto más potentes para el diseño y trazado de placas de circuito impreso (PCB). Este software profesional permite a ingenieros y aficionados crear complejos diseños electrónicos colocando componentes en placas virtuales y trazando las intrincadas líneas que conectan estos componentes entre sí. Lo que hace que KiCad sea especialmente valioso para fines educativos y de desarrollo es su naturaleza de código abierto, que permite a los usuarios modificar, personalizar y aprender de los diseños existentes sin restricciones de licencia.


El proyecto Bitaxe ejemplifica el poder del desarrollo de hardware de código abierto, proporcionando un diseño completo de PCB que los usuarios pueden examinar, modificar y personalizar según sus necesidades específicas. Esta accesibilidad crea un excelente entorno de aprendizaje en el que estudiantes y profesionales pueden explorar diseños de PCB del mundo real mientras desarrollan su comprensión de los sistemas electrónicos. La posibilidad de personalizar elementos visuales como logotipos ofrece un punto de entrada accesible para usuarios que puedan sentirse intimidados por la complejidad técnica del diseño electrónico.


### Configuración del entorno KiCad


Antes de comenzar cualquier trabajo de personalización, es esencial configurar correctamente su entorno de desarrollo. El repositorio Bitaxe debe ser descargado a su máquina local, normalmente a través de la funcionalidad de descarga ZIP de GitHub. Este repositorio contiene todos los archivos de proyecto necesarios, incluidos los archivos de proyecto de KiCad, las bibliotecas de componentes y la documentación de diseño necesaria para una modificación satisfactoria.


La instalación de KiCad debe completarse utilizando la distribución oficial de la página web de KiCad, asegurando la compatibilidad con los archivos del proyecto y el acceso a las últimas características. Una vez que tanto el repositorio como KiCad están correctamente instalados, para abrir el proyecto es necesario navegar hasta el archivo de proyecto Bitaxe Ultra KiCad dentro de la estructura del repositorio descargado. Este archivo de proyecto sirve como eje central que enlaza todos los archivos de diseño asociados, bibliotecas de componentes y ajustes de configuración.


La vista inicial de un diseño de PCB complejo puede parecer abrumadora, con numerosos componentes, trazas y capas que crean un denso paisaje visual. Sin embargo, la funcionalidad de visualización en 3D de KiCad proporciona una herramienta inestimable para comprender la disposición física y las relaciones espaciales dentro del diseño. Esta perspectiva tridimensional transforma la representación esquemática abstracta en una visualización realista del producto final fabricado, lo que facilita la comprensión de la colocación de los componentes y la estética general del diseño.


### Proceso de personalización del logotipo


La personalización de logotipos en diseños de placas de circuito impreso representa una de las modificaciones más accesibles para los usuarios nuevos en KiCad, ya que requiere unos conocimientos técnicos mínimos a la vez que proporciona resultados visuales inmediatos. El proceso comienza con la herramienta de conversión de imágenes, que transforma archivos de imagen estándar en formatos de huella compatibles con el software de diseño de PCB. Este proceso de conversión requiere una cuidadosa atención a los parámetros de tamaño, normalmente medidos en milímetros para garantizar una escala adecuada en la placa fabricada final.


El flujo de trabajo de conversión de imágenes implica varios pasos críticos que determinan el aspecto final y la colocación de los logotipos personalizados. La selección de la imagen de origen debe dar prioridad a los diseños de alto contraste que se traduzcan bien al proceso de serigrafía utilizado en la fabricación de placas de circuito impreso. La especificación del tamaño es crucial, ya que los logotipos deben ser lo suficientemente grandes como para seguir siendo legibles después de la fabricación, sin interferir en la colocación o funcionalidad de los componentes. La elección entre las capas de serigrafía delantera y trasera afecta tanto a la visibilidad como a la fabricación.


La gestión de bibliotecas de huellas representa un aspecto fundamental de la personalización de KiCad, ya que requiere que los usuarios comprendan cómo el software organiza y accede a los elementos de diseño. La adición de logotipos personalizados implica la creación de nuevas bibliotecas de huellas o la modificación de las existentes y, a continuación, la vinculación adecuada de estas bibliotecas dentro de la estructura del proyecto. Este proceso garantiza que los elementos personalizados permanezcan accesibles en diferentes sesiones de diseño y puedan compartirse fácilmente con otros miembros del equipo o colaboradores.


### Exploración y comprensión avanzadas del diseño


Más allá de la simple personalización de logotipos, KiCad proporciona potentes herramientas para explorar y comprender complejos diseños de PCB. El sistema de gestión de capas permite a los usuarios ver de forma selectiva diferentes aspectos del diseño, desde la colocación y el enrutamiento de componentes hasta las especificaciones de fabricación y la información de montaje. Este enfoque por capas permite un análisis detallado de elementos de diseño específicos sin el desorden visual de componentes no relacionados.


El análisis del trazado de rutas representa uno de los aspectos más didácticos de la exploración de PCB, ya que revela cómo fluyen las conexiones eléctricas entre componentes y subsistemas. Siguiendo trazas individuales o grupos de señales relacionadas, los usuarios pueden comprender la funcionalidad de los circuitos y las decisiones de diseño. Por ejemplo, el examen de las redes de distribución de energía revela cómo los componentes de regulación y filtrado de tensión trabajan conjuntamente para proporcionar una alimentación limpia y estable a los componentes electrónicos sensibles.


La relación entre el diseño esquemático y la disposición física se hace evidente a través de un examen cuidadoso de la colocación de componentes y las decisiones de enrutamiento. Comprender por qué se colocan determinados componentes en lugares concretos, cómo influyen las consideraciones térmicas en las decisiones de disposición y cómo los requisitos de integridad de la señal determinan las opciones de encaminamiento proporciona una valiosa perspectiva de las prácticas profesionales de diseño de PCB. Estos conocimientos resultan muy valiosos para los usuarios que desarrollan sus propios diseños o modifican los existentes para aplicaciones específicas.


Las completas herramientas de comprobación y verificación de normas de diseño de KiCad garantizan que las modificaciones mantengan la compatibilidad eléctrica y de fabricación. Estos sistemas automatizados ayudan a evitar errores de diseño comunes a la vez que educan a los usuarios sobre los estándares y las mejores prácticas de la industria. La integración de la visualización 3D con los datos de diseño eléctrico crea un potente entorno de aprendizaje en el que los conceptos teóricos se hacen tangibles a través de la representación visual y la exploración interactiva.


## ¿Cómo crear un archivo de fábrica?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

La creación de firmware personalizado para dispositivos mining basados en ESP requiere una cuidadosa atención a la configuración, las dependencias y el proceso de creación adecuado. Esta completa guía recorre el proceso completo de creación tanto de binarios de firmware estándar como de archivos de fábrica que incluyen ajustes preconfigurados, lo que hace que la implementación sea más eficiente y reduce el tiempo de configuración para los usuarios finales.


Tenga en cuenta que este capítulo es bastante técnico y puede hojearlo simplemente por si siente curiosidad.


### Configuración del entorno de desarrollo


Para iniciar el desarrollo del firmware ESP-Miner debe establecer el entorno de desarrollo adecuado en Visual Studio Code, idealmente en una distribución de Linux. La extensión ESP-IDF sirve como piedra angular de esta configuración, proporcionando las herramientas necesarias y la integración del marco para el desarrollo de ESP32. Al instalar la extensión ESP-IDF por primera vez, los usuarios encuentran una guía de configuración que facilita el proceso de configuración.


Una consideración crítica en el proceso de configuración es la selección de la versión apropiada de ESP-IDF. Aunque anteriormente se recomendaba la versión 5.1.3, la experiencia práctica ha revelado que esta versión puede causar problemas de compilación que complican el proceso de desarrollo. Ahora se recomienda utilizar la versión 5.3 Beta 1 de ESP-IDF, que ha demostrado resolver estas complicaciones de compilación y garantiza el correcto funcionamiento de los dispositivos Bitaxe. El proceso de instalación requiere seleccionar la opción de instalación Express y elegir específicamente la versión 5.3 Beta 1 entre las opciones disponibles.


La configuración del entorno de desarrollo va más allá de la instalación de ESP-IDF e incluye la configuración adecuada del terminal. Visual Studio Code proporciona mÃºltiples mÃ©todos para acceder a la funcionalidad ESP-IDF, incluyendo la opciÃ³n de la paleta de comandos para abrir un terminal ESP-IDF o utilizando el icono de terminal dedicado situado en la interfaz. Este entorno de terminal especializado garantiza que todos los comandos ESP-IDF funcionen correctamente y proporciona acceso a toda la cadena de herramientas.


### Configuración de los ajustes del ESP-Miner


El archivo de configuración representa el núcleo del proceso de personalización del ESP-Miner, ya que contiene todos los parámetros esenciales que definen cómo funcionará el dispositivo en su entorno de destino. Esta configuración abarca los ajustes de red, las conexiones de mining pool y los parámetros específicos de hardware que deben adaptarse al escenario de despliegue específico.


La configuración de la red constituye el componente principal del proceso de instalación y requiere la especificación de las credenciales Wi-Fi, incluidos el SSID y la contraseña. En lugar de utilizar valores como "prueba", las configuraciones de producción deben incluir las credenciales de red reales que el dispositivo utilizará en su entorno operativo. La configuración también admite varias configuraciones de agrupaciones mining, tanto privadas con direcciones IP específicas como públicas como public-pool.io con sus correspondientes ajustes de puerto.


Los parámetros de configuración específicos de Mining incluyen la configuración de usuario de estrato, que suele corresponder a la dirección de Bitcoin a la que deben dirigirse las recompensas de mining. Los parámetros de hardware adicionales, como los ajustes de frecuencia, las configuraciones de voltaje y las especificaciones de tipo de ASIC, deben alinearse con la plataforma de hardware de destino. El repositorio de GitHub proporciona ejemplos preconfigurados para diferentes variantes de hardware, como la configuración BM1368 diseñada para dispositivos Super y la configuración BM1366 para variantes Ultra. Las especificaciones de la versión de la placa, como la configuración de la versión del puerto en 401 para las revisiones de hardware más recientes, garantizan la compatibilidad con las características específicas del dispositivo de destino.


### Creación de Web Interface y del firmware central


El proyecto ESP-Miner incorpora una sofisticada interfaz web que requiere una compilación independiente antes de que pueda comenzar el proceso principal de creación del firmware. Esta interfaz web, denominada firmware AxeOS, proporciona a los usuarios una completa interfaz de gestión para supervisar y controlar sus dispositivos mining.


El proceso de construcción de la interfaz web comienza navegando al directorio del servidor HTTP dentro de la estructura del repositorio principal, específicamente el subdirectorio AxeOS. Esta ubicación contiene la aplicación web basada en Node.js que requiere la instalación de dependencias a través del comando npm install. El sistema de compilación asume que Node.js está correctamente instalado en el sistema de desarrollo, ya que esto representa un requisito fundamental para el proceso de compilación de la interfaz web.


Tras la instalación de las dependencias, el comando npm run build compila los componentes de la interfaz web, creando los archivos necesarios que se incrustarán en el firmware ESP32. Este proceso de compilación genera recursos web optimizados que proporcionan la funcionalidad de la interfaz de usuario, manteniendo un uso eficiente de la memoria en la plataforma ESP32. La finalización con éxito de este paso de compilación es esencial antes de proceder a la compilación del firmware principal, ya que el firmware ESP-Miner incorpora estos componentes de interfaz web como funcionalidad integral.


### Creación de archivos de fábrica con configuración integrada


La creación de archivos de fábrica representa una estrategia de despliegue avanzada que incorpora los ajustes de configuración directamente en el binario del firmware, eliminando la necesidad de configuración manual durante la configuración del dispositivo. Este enfoque resulta especialmente valioso para implantaciones a gran escala o situaciones en las que es esencial una configuración coherente en varios dispositivos.


El proceso de creación del archivo de fábrica comienza con la generación de un binario de configuración a partir del archivo de configuración CSV utilizando la herramienta generadora de particiones NVS de ESP-IDF. Esta herramienta, que se encuentra en el directorio de componentes de ESP-IDF bajo nvs-flash/nvs-partition-generator, convierte la configuración legible por humanos en un formato binario adecuado para el almacenamiento directo en memoria flash. El script nvs-partition-gen.py procesa el archivo config.csv y genera un archivo config.binary que tiene como destino el espacio de direcciones de memoria 0x6000.


El ensamblaje final de los archivos de fábrica utiliza scripts de fusión especializados que combinan los binarios del firmware central con los datos de configuración. El repositorio ofrece varias opciones de fusión, incluido un script de fusión estándar para archivos de fábrica básicos y un script de fusión con configuración incluida para archivos de fábrica completos. El script merge-bin-with-config.sh crea archivos de fábrica que incluyen tanto la funcionalidad del firmware como los ajustes preconfigurados, lo que da como resultado un paquete de despliegue completo. Este enfoque permite la creación de archivos de fábrica específicos para cada dispositivo, como versiones adaptadas para dispositivos Bitaxe Ultra con revisiones específicas de la placa, al tiempo que mantiene la flexibilidad para generate archivos de fábrica genéricos sin configuraciones incrustadas para escenarios que requieren flexibilidad de configuración manual.


Los archivos de fábrica completos proporcionan a los equipos de despliegue binarios listos para flashear que incluyen todos los componentes de firmware y ajustes de configuración necesarios, lo que agiliza el proceso de aprovisionamiento de dispositivos y garantiza parámetros operativos coherentes en todos los dispositivos mining desplegados.


## ¿Cómo utilizar Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

El instalador web de Bitaxe representa un enfoque simplificado para la gestión del firmware de los dispositivos Bitaxe, proporcionando a los usuarios múltiples opciones de instalación a través de una interfaz basada en web. Esta completa herramienta elimina la complejidad tradicionalmente asociada con las actualizaciones de firmware y las nuevas instalaciones, haciendo que la gestión de dispositivos sea accesible a los usuarios independientemente de sus conocimientos técnicos. Comprender el uso adecuado de este instalador es crucial para mantener un rendimiento óptimo del dispositivo y evitar errores comunes que pueden dejar los dispositivos temporalmente inoperativos.


### Requisitos de acceso y compatibilidad de navegadores


Se puede acceder al instalador web de Bitaxe a través de la URL dedicada [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (la que se presenta en el vídeo está ahora obsoleta), que sirve como eje central para todas las actividades de instalación del firmware. Sin embargo, el funcionamiento correcto de esta herramienta basada en web requiere la compatibilidad del navegador, ya que el instalador se basa en tecnologías web específicas que no son compatibles universalmente con todos los navegadores. Chrome es el principal navegador recomendado para el instalador, ya que ofrece compatibilidad total con todas las características y funciones. Aunque otros navegadores basados en Chromium pueden ofrecer una funcionalidad similar, las alternativas populares como Brave y Firefox carecen de la compatibilidad necesaria con API de serie web, lo que los hace incompatibles con las operaciones básicas del instalador.


Esta limitación del navegador se debe a que el instalador confía en la comunicación serie directa con los dispositivos Bitaxe a través de la interfaz web. El API serie web, que permite esta comunicación, sigue siendo un estándar web relativamente nuevo que aún no ha logrado la adopción universal de los navegadores. Los usuarios que intenten acceder al instalador a través de navegadores no compatibles se encontrarán con fallos de conexión y la imposibilidad de comunicarse con sus dispositivos, por lo que será necesario cambiar a un navegador compatible antes de proceder con cualquier actividad de instalación.


### Requisitos de alimentación y preparación del dispositivo


Los dispositivos Bitaxe presentan diferentes requisitos de alimentación en función de su modelo y versión específicos, por lo que una gestión adecuada de la alimentación es esencial para el éxito de la instalación del firmware. Los dispositivos con la versión 204 o inferior pueden funcionar únicamente a través de la alimentación USB, tomando suficiente corriente del ordenador conectado para mantener el funcionamiento durante el proceso de flasheo. Esta disposición simplificada de la alimentación hace que estas versiones anteriores resulten especialmente cómodas para actualizar el firmware, ya que los usuarios sólo tienen que conectar un único cable USB para iniciar el proceso de instalación.


Sin embargo, los dispositivos que ejecutan la versión 205 y superiores requieren fuentes de alimentación externas además de la conexión USB, lo que refleja los cambios en el consumo de energía y el diseño de circuitos en las revisiones de hardware más recientes. Estos dispositivos no pueden obtener la alimentación adecuada sólo a través de USB, por lo que es necesario conectarlos a sus fuentes de alimentación estándar durante la instalación del firmware. Si no se suministra la alimentación adecuada a estos nuevos dispositivos, se producirán fallos en la instalación y posibles daños en el proceso de actualización del firmware.


El proceso de conexión física requiere una sincronización específica y la manipulación de botones para garantizar una comunicación adecuada entre el instalador y el dispositivo. Los usuarios deben mantener pulsado el botón de arranque del dispositivo Bitaxe antes de conectar el cable USB-C al ordenador. Esta secuencia coloca el dispositivo en modo cargador de arranque, lo que permite al instalador comunicarse directamente con el almacenamiento de firmware del dispositivo. Si se conecta el cable USB antes de pulsar el botón de arranque, el dispositivo funcionará normalmente y no en el modo de cargador de arranque necesario para la instalación del firmware, lo que impedirá que el instalador establezca el canal de comunicación necesario.


### Opciones de instalación y sus aplicaciones


El instalador web de Bitaxe ofrece cuatro opciones de instalación distintas, cada una diseñada para casos de uso y configuraciones de dispositivos específicos. La versión 4.0.1 de Bitaxe Superboard representa el firmware más actual para los dispositivos del modelo Super, con la versión 4.0.2 prevista para un futuro lanzamiento. Esta opción incluye variantes de fábrica y de actualización, lo que proporciona flexibilidad en el enfoque de la instalación en función de las necesidades del usuario y del estado del dispositivo.


Las instalaciones de fábrica representan sustituciones completas de firmware que reflejan el proceso de fabricación original, incluidos procedimientos de autocomprobación exhaustivos que verifican la funcionalidad del dispositivo en todos los sistemas. Cuando los usuarios seleccionan una instalación de fábrica, el instalador realiza un borrado completo del firmware y los datos de configuración existentes, sustituyéndolos por una instalación nueva y limpia idéntica a la que se aplicaría durante la fabricación. Este proceso incluye una autocomprobación automatizada que valida el correcto funcionamiento del hardware y requiere que los usuarios reinicien sus dispositivos antes de que pueda reanudarse el funcionamiento normal. Las instalaciones de fábrica resultan especialmente valiosas cuando los dispositivos experimentan problemas persistentes o cuando los usuarios desean devolver sus dispositivos a las especificaciones originales de fábrica.


Las instalaciones de actualización ofrecen un enfoque más conservador, ya que conservan los datos de configuración existentes y sólo actualizan los componentes principales del firmware. Esta opción resulta ideal para los usuarios que han personalizado los ajustes de sus dispositivos y desean mantener sus configuraciones personales a la vez que se benefician de las mejoras y correcciones de errores del firmware. El proceso de actualización se centra únicamente en los componentes del firmware que requieren modificación, dejando intactos los ajustes específicos del usuario, las credenciales WiFi y las direcciones Bitcoin durante todo el proceso de instalación.


### Consideraciones críticas sobre la instalación y la protección de datos


La distinción entre instalaciones de fábrica y de actualización tiene implicaciones significativas para la configuración del dispositivo y la conservación de los datos del usuario. Las instalaciones de fábrica realizan un borrado completo del dispositivo, eliminando todos los ajustes configurados por el usuario, incluidas las credenciales WiFi, las direcciones Bitcoin y cualquier parámetro personalizado del dispositivo. Tras una instalación de fábrica, los usuarios deben volver a conectarse a la red WiFi predeterminada del dispositivo y reconfigurar todos los ajustes personales desde cero, tratando esencialmente el dispositivo como si fuera nuevo del fabricante.


Las instalaciones de actualización requieren una cuidadosa atención a la opción de borrar el dispositivo que se presenta durante el proceso de instalación. El instalador preguntará a los usuarios "¿Desea borrar el dispositivo antes de instalar Bitaxe Flasher?" acompañado de una advertencia de que se perderán todos los datos del dispositivo. Los usuarios que realicen instalaciones de actualización deben rechazar esta opción haciendo clic en "Siguiente" en lugar de confirmar la operación de borrado. Aceptar la opción de borrado durante la instalación de una actualización eliminará el archivo de configuración del dispositivo, lo que puede hacer que el dispositivo no funcione hasta que se restablezca la configuración adecuada. Aunque esta situación no daña permanentemente el dispositivo, crea complicaciones innecesarias y requiere pasos de configuración adicionales para restablecer el funcionamiento normal.


El propio proceso de instalación se realiza automáticamente una vez que los usuarios han hecho sus selecciones y confirmado sus elecciones. El instalador se encarga de todos los aspectos técnicos de la transferencia y verificación del firmware, proporcionando indicadores de progreso y actualizaciones de estado durante todo el proceso. Este enfoque automatizado elimina la necesidad de que los usuarios comprendan complejos procedimientos de instalación de firmware, al tiempo que garantiza resultados fiables y coherentes en diferentes modelos de dispositivos y versiones de firmware.


## ¿Cómo crear y encargar la placa de circuito impreso?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Este capítulo se centra en el proceso práctico de generación de archivos de fabricación a partir de proyectos de KiCad y el pedido de placas de circuito impreso profesionales a fabricantes en línea. Utilizando el proyecto Bitaxe como ejemplo, recorreremos el flujo de trabajo completo desde la generación de archivos hasta la realización de un pedido a un fabricante de placas de circuito impreso.


### Comprender el proceso de fabricación de PCB


El viaje desde un diseño de KiCad terminado hasta una placa de circuito impreso física implica varios pasos críticos que tienden un puente entre el diseño digital y la fabricación física. Cuando se trabaja con proyectos complejos como el Bitaxe, el editor de PCB de KiCad proporciona una vista completa del diseño, mostrando todos los componentes y sus interconexiones a través de trazas de colores. Las líneas rojas y azules que se ven representan las conexiones eléctricas entre los distintos circuitos integrados y componentes de la placa. El visor 3D de KiCad le permite visualizar el aspecto final de la placa ensamblada, proporcionándole una valiosa información sobre la colocación de los componentes y los posibles conflictos mecánicos.


El proceso de fabricación requiere formatos de archivo específicos que los fabricantes de placas de circuito impreso puedan interpretar y utilizar para fabricar sus placas. Estos archivos contienen información precisa sobre capas de cobre, taladros, colocación de componentes y otras especificaciones de fabricación. Comprender este flujo de trabajo es esencial tanto si trabaja con el diseño estándar de Bitaxe como si crea modificaciones como añadir logotipos personalizados, cambiar los valores de los componentes o ajustar el diseño de la placa para cumplir requisitos específicos.


### Generación de archivos Gerber para fabricación


Los archivos Gerber son la norma del sector para comunicar a los fabricantes la información sobre el diseño de las placas de circuito impreso. Estos archivos contienen todos los datos necesarios para fabricar su PCB, incluidos los patrones de las capas de cobre, las definiciones de las máscaras de soldadura y las ubicaciones de los taladros. Para generate estos archivos en KiCad, navegue hasta el editor de PCB y acceda a las salidas de fabricación a través del menú Archivos. El software configura automáticamente los ajustes adecuados para los procesos de fabricación estándar, incluida la estructura de directorios de salida adecuada, organizada normalmente como "archivos de fabricación/gerbers."


El proceso de generación crea varios archivos Gerber, cada uno de los cuales representa diferentes aspectos de su diseño de PCB. Estos archivos funcionan conjuntamente para proporcionar a los fabricantes instrucciones completas de fabricación. Una vez generados, estos archivos deben comprimirse en un archivo ZIP, ya que éste es el formato estándar que esperan la mayoría de los fabricantes de PCB. El archivo ZIP contiene todos los datos de fabricación necesarios y garantiza que no se pierda ni se corrompa ningún archivo durante el proceso de carga en el sitio web del fabricante.


Vale la pena señalar que muchos proyectos de código abierto, incluido el Bitaxe, suelen incluir archivos de fabricación pregenerados en sus repositorios. Sin embargo, entender cómo generate estos archivos usted mismo es crucial al hacer modificaciones de diseño o trabajar con diferentes versiones de la placa. Este conocimiento resulta especialmente valioso a la hora de personalizar diseños o solucionar problemas de fabricación.


### Selección de fabricantes de placas de circuito impreso y comprensión de las opciones


El panorama de la fabricación de PCB ofrece varias opciones de buena reputación, con JLCPCB y PCBWay entre las opciones más populares para aficionados y profesionales por igual. Ambos fabricantes ofrecen servicios similares con precios competitivos y calidad fiable, aunque cada uno tiene ventajas específicas en función de los requisitos de su proyecto. JLCPCB suele atraer a los usuarios noveles con precios promocionales e interfaces fáciles de usar, mientras que PCBWay puede ofrecer diferentes opciones de materiales o servicios especializados.


Al cargar sus archivos Gerber en el sitio web de un fabricante, el sistema analiza automáticamente su diseño y presenta varias opciones de fabricación. Los ajustes por defecto que ofrecen estas plataformas suelen ser adecuados para la mayoría de los diseños estándar, y en general se recomienda mantenerlos a menos que tenga requisitos específicos. Los parámetros clave son el grosor de la placa de circuito impreso, el peso del cobre, el acabado superficial y las cantidades mínimas. La mayoría de los fabricantes exigen pedidos mínimos de cinco placas, lo que en realidad funciona bien para proyectos de aficionados en los que tener placas de repuesto o compartirlas con amigos es beneficioso.


Las opciones de color representan una de las pocas opciones estéticas disponibles durante el proceso de fabricación. Aunque el verde sigue siendo la opción tradicional y más rentable, los fabricantes suelen ofrecer alternativas como el azul, el rojo, el amarillo, el morado y el negro. La elección del color es puramente estética y no afecta al rendimiento eléctrico de la placa de circuito impreso, aunque algunos colores pueden tener ligeras implicaciones económicas o plazos de fabricación más largos.


### Consideraciones sobre fabricación avanzada y opciones de montaje


Además de la fabricación básica de placas de circuito impreso, los fabricantes modernos ofrecen servicios adicionales que pueden agilizar considerablemente la realización de su proyecto. Las plantillas representan uno de los servicios adicionales más valiosos, sobre todo para diseños con componentes de paso fino como los chips ASIC que se encuentran en los proyectos Bitcoin mining. Un esténcil es básicamente una plantilla de aluminio cortada con precisión con aberturas que se corresponden exactamente con las ubicaciones de los pads de soldadura de la placa de circuito impreso. Esta herramienta permite una aplicación uniforme y precisa de la pasta de soldadura, lo que mejora notablemente la calidad del montaje y reduce la probabilidad de errores de soldadura.


Las opciones de estarcido suelen incluir estarcidos individuales con patrones superiores e inferiores, o estarcidos separados para cada lado del tablero. Para la mayoría de los proyectos, un esténcil combinado resulta más cómodo y rentable. El grosor del esténcil se calcula cuidadosamente para depositar la cantidad adecuada de pasta de soldadura para los tipos de componentes y tamaños de pad específicos. El uso de una plantilla transforma lo que podría ser un proceso manual tedioso y propenso a errores en un paso de montaje rápido y profesional.


Aunque algunos fabricantes ofrecen servicios de ensamblaje parcial o completo, estas opciones requieren una cuidadosa consideración para proyectos complejos como el Bitaxe. La disponibilidad de componentes, las implicaciones económicas y el valor educativo del autoensamblaje son factores que influyen en esta decisión. Muchos componentes especializados necesarios para los proyectos de Bitcoin mining pueden no estar fácilmente disponibles a través de los servicios estándar de ensamblaje de PCB, por lo que el aprovisionamiento de componentes y el ensamblaje manual son el enfoque más práctico. Los próximos episodios de esta serie cubrirán las estrategias de abastecimiento de componentes y técnicas de montaje para ayudarle a completar con éxito su proyecto Bitaxe desde la PCB desnuda hasta el dispositivo funcional.


El proceso de fabricación y montaje representa un puente crucial entre el diseño digital y la implementación física. Comprender estos flujos de trabajo le permite tomar el control de sus proyectos, reducir costes y adquirir una valiosa experiencia práctica con procesos de fabricación profesionales. Tanto si construye un único prototipo como si planifica una pequeña tirada de producción, el dominio de estos conocimientos abre nuevas posibilidades para dar vida a sus diseños electrónicos.


# Optimización del rendimiento

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Evalúe su Bitaxe

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

La búsqueda de un rendimiento mining óptimo requiere un enfoque sistemático de la configuración del hardware que equilibre hashrate, eficiencia y gestión térmica. El Bitaxe ofrece numerosos parámetros de configuración que pueden afectar significativamente al rendimiento, pero probar manualmente cada combinación de ajustes sería poco práctico y llevaría mucho tiempo. Este capítulo explora cómo aprovechar las herramientas de benchmarking automatizadas para optimizar científicamente el rendimiento de su Bitaxe manteniendo unas condiciones de funcionamiento seguras.


### Comprender las métricas de rendimiento de Bitaxe y la configuración de la línea de base


Antes de sumergirse en las técnicas de optimización, es esencial comprender los indicadores clave de rendimiento que definen la eficiencia operativa de su Bitaxe. Las métricas principales incluyen hashrate medido en terahash por segundo, la eficiencia energética expresada en julios por terahash, la frecuencia ASIC en megahercios y el voltaje del núcleo en voltios. Un Bitaxe bien configurado podría alcanzar aproximadamente 1,1 terahash con una eficiencia de unos 17 julios por terahash, funcionando a 550 megahercios con un voltaje ASIC medido de 1,14 voltios. Estas cifras de referencia sirven para comprender las posibles mejoras que se pueden conseguir mediante una optimización sistemática.


La relación entre estas métricas es compleja e interdependiente. Las frecuencias más altas suelen aumentar el hashrate, pero también el consumo de energía y la generación de calor. Del mismo modo, los ajustes de voltaje afectan tanto al rendimiento como a las características térmicas. El reto consiste en encontrar el equilibrio óptimo que maximice el hashrate o la eficiencia, manteniendo al mismo tiempo un funcionamiento estable dentro de unos límites de temperatura seguros. Este proceso de optimización requiere pruebas metódicas con múltiples combinaciones de parámetros, por lo que las herramientas automatizadas resultan muy valiosas para lograr resultados óptimos.


### Arquitectura de la herramienta de evaluación comparativa Bitaxe Hashrate


La herramienta [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) representa una sofisticada solución basada en Python desarrollada originalmente por WhiteCookie y mejorada posteriormente por mrv777. Esta herramienta de código abierto, distribuida bajo licencia GPLv3, automatiza el complejo proceso de probar múltiples combinaciones de configuración para identificar los ajustes óptimos para su hardware específico. El principal punto fuerte de la herramienta reside en su enfoque sistemático de la comprobación de parámetros, que ajusta progresivamente la configuración de frecuencia y voltaje mientras supervisa continuamente las métricas de rendimiento y las condiciones térmicas.


El proceso de evaluación comparativa suele durar entre 30 y 40 minutos, durante los cuales la herramienta prueba metódicamente varias combinaciones de ajustes de frecuencia y tensión de ASIC. La herramienta comienza con unos valores de referencia conservadores, que suelen ser de 1,15 voltios y 500 megahercios, y va incrementando estos parámetros mientras controla la hashrate, la temperatura y la estabilidad. Y lo que es más importante, la herramienta da prioridad al funcionamiento seguro frente al rendimiento máximo, reduciendo automáticamente los ajustes que provocan una generación excesiva de calor o inestabilidad. Este enfoque conservador garantiza que el proceso de optimización no comprometa la longevidad ni la fiabilidad del hardware.


### Requisitos de instalación y configuración


La implementación de la herramienta Bitaxe Hashrate Benchmark requiere varios componentes de software previos en su ordenador local. Los requisitos principales incluyen Python para ejecutar los scripts de evaluación comparativa, Git para la gestión de repositorios y, opcionalmente, Visual Studio Code para mejorar las capacidades del entorno de desarrollo. Aunque la herramienta puede manejarse desde interfaces de línea de comandos, el uso de un entorno de desarrollo integrado como VS Code proporciona una mejor visibilidad del proceso de evaluación comparativa y del análisis de resultados.


El proceso de instalación sigue las prácticas estándar de desarrollo de Python, comenzando con la clonación del repositorio desde GitHub a tu máquina local. Una vez descargado el repositorio, tendrás que crear un entorno virtual para aislar las dependencias de la herramienta de la instalación de Python de tu sistema. Este aislamiento evita posibles conflictos con otras aplicaciones Python y garantiza un funcionamiento coherente. Después de activar el entorno virtual, instalará las dependencias necesarias utilizando el archivo de requisitos proporcionado, que configura automáticamente todas las bibliotecas y módulos necesarios para el correcto funcionamiento de la herramienta.


### Ejecución de evaluaciones comparativas e interpretación de resultados


Ejecutar el benchmark requiere ejecutar un único comando Python que incluye la dirección IP de su Bitaxe como parámetro. La herramienta se conecta automáticamente a la interfaz web de su minero y comienza el proceso de prueba sistemático. Durante la ejecución, la herramienta proporciona información de registro detallada que muestra la iteración de prueba actual, los ajustes de voltaje y frecuencia aplicados, el hashrate resultante, el voltaje de entrada, las lecturas de temperatura y los datos térmicos de componentes críticos como el convertidor Buck. Esta información en tiempo real le permite supervisar el progreso de la evaluación comparativa y comprender cómo afectan los distintos ajustes al rendimiento de su minero.


La gestión térmica inteligente de la herramienta se hace evidente cuando las temperaturas se acercan al umbral de seguridad de 66 grados Celsius. En lugar de sobrepasar los límites de seguridad, el benchmark reduce automáticamente los ajustes para mantener la estabilidad térmica. Este enfoque conservador garantiza que el proceso de optimización dé prioridad a la fiabilidad del hardware a largo plazo frente a las ganancias de rendimiento a corto plazo. Al finalizar, la herramienta genera resultados completos en formato JSON, clasificando las cinco mejores configuraciones tanto para el máximo hashrate como para la eficiencia óptima. Estos resultados proporcionan una orientación clara para seleccionar la configuración que mejor se adapte a sus prioridades operativas, tanto si se centran en el rendimiento máximo como en la eficiencia energética.


La herramienta de evaluación comparativa también ofrece opciones de personalización para usuarios avanzados que deseen modificar los parámetros de las pruebas. Los argumentos de la línea de comandos permiten especificar voltajes y frecuencias de inicio personalizados, lo que permite una optimización más específica para casos de uso concretos. Por ejemplo, si sabes que tu hardware rinde bien a frecuencias más altas, puedes iniciar la prueba con valores más elevados en lugar de partir de los conservadores valores predeterminados. Esta flexibilidad hace que la herramienta sea valiosa tanto para usuarios principiantes que buscan una optimización automatizada como para mineros experimentados que desean ajustar características de rendimiento específicas.


## Overclockea tu Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

El overclocking de un dispositivo Bitaxe requiere una cuidadosa consideración tanto de las limitaciones del hardware como de los requisitos de refrigeración. Mientras que muchos usuarios prefieren underclockear sus dispositivos para un funcionamiento más silencioso, entender las técnicas adecuadas de overclocking es esencial para aquellos que buscan el máximo rendimiento sin dañar su hardware. El proceso implica aumentar la frecuencia y, potencialmente, ajustar la configuración de voltaje más allá de las especificaciones de fábrica, lo que inherentemente aumenta la generación de calor y el estrés en los componentes.


La base del éxito del overclocking reside en una infraestructura de refrigeración adecuada. Antes de intentar cualquier modificación de frecuencia, debes asegurarte de que tu Bitaxe tiene la capacidad de disipación de calor adecuada. Una Gamma Bitaxe con un disipador y ventilador de calidad proporciona la gestión térmica necesaria para un overclocking seguro. Los dispositivos con disipadores de calor pequeños y ventiladores inadecuados no deben ser overclockeados, ya que un mal rendimiento de refrigeración dará lugar a estrangulamiento térmico y posibles daños en el hardware. Es fundamental comprender la relación entre el calor y la longevidad de los componentes: el calor excesivo genera una tensión que degrada los componentes electrónicos con el paso del tiempo, lo que reduce considerablemente la vida útil del dispositivo.


### Colocación estratégica del disipador térmico


El componente más crítico que requiere refrigeración adicional es el convertidor Buck, un pequeño componente negro situado en la parte trasera del Bitaxe, cerca de la bobina grande. Este dispositivo convierte la fuente de alimentación entrante de 5 V en el voltaje adecuado para el chip ASIC, normalmente alrededor de 1,2 V. El convertidor Buck, a menudo conocido como TPS, genera un calor significativo durante su funcionamiento y representa un cuello de botella térmico que limita el potencial de overclocking. La instalación de un pequeño disipador adhesivo en este componente no sólo permite un mayor margen de overclocking, sino que también mejora la eficiencia general al reducir las pérdidas térmicas.


La colocación de disipadores de calor adicionales puede beneficiar a otras áreas de alta corriente de la placa. El circuito de regulación de voltaje experimenta una tensión eléctrica considerable a medida que la alimentación fluye desde la sección de entrada hacia abajo a través de varias trazas de la placa para alimentar el chip ASIC. Muchos overclockers experimentados instalan disipadores en la parte frontal del Bitaxe en estas zonas de alta corriente para mejorar aún más la disipación térmica. Aunque no son estrictamente necesarias para un overclocking moderado, estas medidas de refrigeración adicionales son importantes cuando se llevan las frecuencias a niveles extremos.


### Consideraciones y limitaciones del sistema de refrigeración


El controlador ESP32, visible como el componente plateado de la placa, no suele necesitar refrigeración adicional. Este componente genera un calor mínimo de forma independiente y sólo se calienta debido a la transferencia térmica de los componentes circundantes. Instalar disipadores cerca del ESP32 puede interferir potencialmente con la antena Wi-Fi adyacente, degradando la conectividad inalámbrica y la calidad de la señal. Concentre los esfuerzos de refrigeración en los componentes de regulación de potencia y la zona ASIC en lugar de en los circuitos de control.


Las configuraciones de doble ventilador presentan oportunidades y limitaciones. Aunque añadir un segundo ventilador para soplar aire por la parte trasera del Bitaxe puede mejorar el rendimiento de la refrigeración, el firmware del dispositivo sólo puede controlar un ventilador correctamente. El Bitaxe tiene dos cabezales de ventilador, pero sólo un controlador de ventilador, lo que significa que la conexión de dos ventiladores confundirá el firmware, ya que recibe señales de RPM en conflicto. Esta configuración funcionará pero puede resultar en un comportamiento impredecible del control del ventilador.


### Evaluación de referencia


Antes de intentar cualquier modificación de overclocking, establece una línea base de rendimiento ejecutando tu Bitaxe con los ajustes de fábrica durante varias horas. Monitoriza la temperatura de ASIC, la temperatura del regulador de voltaje y el porcentaje de velocidad del ventilador a través de la interfaz web. Las temperaturas óptimas de funcionamiento deberían mantener la ASIC por debajo de 60°C y el regulador de voltaje por debajo de 60°C en condiciones normales. Si su dispositivo ya funciona a más de 65°C en la ASIC o a más de 70-80°C en el regulador de voltaje con la configuración de fábrica, es necesario instalar hardware de refrigeración adicional antes de proceder con el overclocking.


El enfoque sistemático para aumentar la frecuencia implica pasos incrementales utilizando las opciones de frecuencia predefinidas en el menú de configuración. Comience por seleccionar el siguiente paso de frecuencia disponible por encima de su configuración actual, manteniendo la tensión del núcleo predeterminada. Este enfoque conservador le permite evaluar los impactos térmicos y de estabilidad antes de realizar cambios adicionales. Deje que el dispositivo funcione con cada nuevo ajuste de frecuencia durante al menos 30 minutos a una hora, controlando las tendencias de temperatura y la estabilidad de la tasa de hash durante todo el período de evaluación.


### Configuración personalizada avanzada


Para acceder a los ajustes personalizados de frecuencia y voltaje es necesario activar la interfaz avanzada de overclocking añadiendo "?OC" a la URL de la interfaz web del dispositivo. Esto desbloquea los campos de entrada manual para un control preciso de la frecuencia y el voltaje, acompañado de advertencias adecuadas sobre los riesgos de operar fuera de los parámetros diseñados. La interfaz personalizada permite un ajuste preciso más allá de los pasos de frecuencia estándar, lo que permite a los usuarios experimentados optimizar el rendimiento para sus configuraciones de refrigeración específicas.


Cuando utilice ajustes personalizados, mantenga tamaños de incremento conservadores de 10-15 MHz por paso de ajuste. Este enfoque metódico evita los picos térmicos repentinos y permite realizar pruebas de estabilidad adecuadas en cada nivel de frecuencia. Algunos usuarios avanzados alcanzan frecuencias en torno a los 700 MHz con tensiones del núcleo ajustadas a 1,175 V o valores similares, pero estos ajustes extremos requieren amplias modificaciones de refrigeración y una cuidadosa monitorización. El regulador de voltaje puede funcionar a temperaturas de hasta 100 °C sin sufrir daños inmediatos, pero las temperaturas más altas reducen la eficiencia y la fiabilidad a largo plazo. El éxito del overclocking requiere paciencia, pruebas sistemáticas y una supervisión continua para lograr mejoras estables del rendimiento y preservar al mismo tiempo la integridad del hardware.


# Sección final

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Evalúe este curso

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusión

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>
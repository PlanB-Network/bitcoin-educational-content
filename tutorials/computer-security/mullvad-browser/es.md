---
name: Navegador Mullvad
description: Cómo utilizar el navegador Mullvad para proteger la intimidad
---

![cover](assets/cover.webp)



En un mundo en el que la vigilancia digital se está convirtiendo en omnipresente, proteger su privacidad en línea nunca ha sido tan crucial. Las empresas utilizan técnicas sofisticadas para rastrearle:





- Cookies de terceros**: pequeños archivos depositados por sitios externos para seguirle de un sitio a otro
- Fingerprinting**: recoge características únicas de su navegador y dispositivo (resolución de pantalla, fuentes instaladas, plugins, etc.) para identificarle sin cookies
- Scripts de seguimiento**: códigos JavaScript invisibles que analizan su comportamiento de navegación (clics, desplazamiento, tiempo empleado)
- Análisis IP Address**: localización geográfica e identificación de su proveedor de servicios de Internet



A continuación, estos datos se combinan para crear perfiles detallados de su comportamiento en línea y se monetizan, a menudo sin su conocimiento. Esta realidad plantea una cuestión fundamental: ¿cómo navegar por Internet preservando el anonimato y la confidencialidad?



La respuesta radica en gran medida en la elección del navegador web. Esta herramienta, que utilizamos a diario para acceder a información, realizar compras o comunicarnos, desempeña un papel decisivo en la protección de nuestros datos personales. Por desgracia, navegadores tan populares como Google Chrome (que acapara alrededor del 65 % del mercado mundial) están diseñados en torno a modelos de negocio basados en la recopilación masiva de datos de los usuarios.



![MULLVAD BROWSER](assets/fr/01.webp)


*Mullvad Browser destaca por su excepcional eficacia en el bloqueo de rastreadores, muy superior a la de los navegadores de consumo*



Ante este reto, surgen nuevos actores con una filosofía diferente: la de situar la privacidad en el centro de su diseño. Entre ellos, Mullvad Browser destaca como una solución innovadora que combina las mejores protecciones de privacidad con una experiencia de navegación fluida y accesible.



A diferencia de los navegadores tradicionales, que tratan de personalizar su experiencia recopilando sus datos, Mullvad Browser adopta el enfoque opuesto: hacer que todos sus usuarios parezcan idénticos en los sitios web, lo que hace prácticamente imposible el seguimiento individualizado.



En este tutorial, descubriremos juntos cómo Mullvad Browser puede transformar su forma de navegar por Internet, ofreciéndole una sólida protección contra la vigilancia sin sacrificar la facilidad de uso.




## Presentación del navegador Mullvad



**Mullvad Browser** es un navegador web centrado en la privacidad desarrollado en colaboración con el Proyecto Tor y distribuido gratuitamente por la empresa sueca Mullvad VPN. Lanzado en abril de 2023, se presenta a sí mismo como un **"Navegador Tor sin la red Tor "**, diseñado para minimizar el rastreo y las huellas digitales en línea al tiempo que permite a los usuarios navegar a través de una VPN de confianza en lugar de la red Tor.



Mullvad Browser es un navegador gratuito y de código abierto basado en Firefox ESR (la versión de larga duración de Mozilla Firefox) y reforzado por expertos del Proyecto Tor. En concreto, incluye la mayoría de las **características de protección del Navegador Tor**, pero **no enruta el tráfico a través de la red Tor**. En su lugar, los usuarios pueden (y deben) vincularlo a una VPN cifrada de confianza para anonimizar su IP Address.



En términos de experiencia de usuario, Mullvad Browser se asemeja a un navegador clásico, ofreciendo una navegación fluida. Está disponible de forma gratuita en Windows, macOS y Linux (sin versión móvil). No necesitas estar suscrito a Mullvad VPN para usarlo; sin embargo, **usar Mullvad Browser sin enmascarar tu IP no proporciona un anonimato completo** - por lo que es muy recomendable usarlo junto con una VPN fiable.



### Objetivos: privacidad y anti-seguimiento



El navegador Mullvad ha sido diseñado con un objetivo principal: **proteger la privacidad del usuario** en línea y contrarrestar las técnicas habituales de rastreo y elaboración de perfiles. Sus principales objetivos son:





- Reduzca drásticamente el rastreo y seguimiento de anuncios** por parte de sitios web y agencias de publicidad. Por defecto, Mullvad Browser bloquea los rastreadores de terceros, las cookies de seguimiento y los scripts de huellas dactilares que podrían identificarle.





- Estandariza la huella digital de tu navegador** para **"mezclarte con la multitud "**. La huella digital es como un "carné de identidad" único creado combinando todas las características de su navegador. Mullvad Browser se asegura de que todos sus usuarios tengan exactamente el mismo "carnet de identidad", haciendo imposible distinguirlos individualmente.





- Ofrece protección inmediata sin extensiones adicionales**. Mullvad Browser viene en una configuración "lista para usar": el usuario no necesita instalar una serie de extensiones ni modificar ninguna configuración para estar protegido.





- No sacrifiques el rendimiento o la ergonomía** más de lo necesario. En ausencia de enrutamiento Tor, Mullvad Browser ofrece una navegación mucho más rápida que Tor Browser, acercándose al rendimiento de un navegador estándar unido a una VPN.



### Características principales de Mullvad Browser



Mullvad Browser incluye una serie de **características de seguridad y privacidad** directamente inspiradas en Tor Browser:





- Navegación privada en todo momento:** El modo de navegación privada está activado por defecto y no se puede desactivar. **No se almacena historial, cookies ni caché de una sesión a otra**. En cuanto cierras Mullvad Browser, se borran todos los datos de navegación.





- Protección mejorada contra el fingerprinting:** El navegador aplica una configuración estricta para frustrar el fingerprinting digital. Esto incluye:
 - Normalización del agente de usuario** y de la versión del navegador
 - Zona horaria ajustada a UTC** para todos los usuarios
 - Letterboxing**: técnica que añade automáticamente márgenes grises alrededor de las páginas web para estandarizar el tamaño de visualización y evitar la identificación por las dimensiones de su pantalla
 - Bloquea las API de huellas dactilares**: Las tecnologías Canvas (dibujo 2D), WebGL (gráficos 3D) y AudioContext (procesamiento de audio) están deshabilitadas porque pueden revelar detalles únicos sobre tu hardware
 - Fuentes de sistema normalizadas** para evitar la identificación por fuentes instaladas





- Bloqueo de rastreadores y publicidad:** Mullvad Browser integra de forma nativa la extensión **uBlock Origin** (preinstalada) con listas de protección adicionales para bloquear **rastreadores de terceros, scripts publicitarios y otros contenidos maliciosos**. Esta protección va acompañada de **First-Party Isolation**: una técnica que almacena las cookies en "cacharros" separados para cada sitio web, impidiendo que un sitio lea las cookies depositadas por otro.





- Botón de reinicio de sesión:** Al igual que el botón "Nueva Identidad" del Navegador Tor, el Navegador Mullvad ofrece un botón para **reiniciar rápidamente el navegador con una nueva sesión en blanco**.





- Niveles de seguridad ajustables:** Puedes ajustar el nivel de seguridad (*Normal*, *Safer*, *Safest*) en la configuración, igual que en el Navegador Tor.



## Extensiones incorporadas por defecto



Mullvad Browser incluye **tres extensiones preinstaladas** que forman el núcleo de su protección anti-seguimiento. **Es crucial no eliminarlas nunca ni modificar sus configuraciones**, ya que esto le haría único entre los usuarios de Mullvad Browser:



### **uBloquear origen**


Esta extensión bloqueadora de anuncios y rastreadores viene preconfigurada con **listas de filtros optimizadas** para bloquear:




- Publicidad intrusiva
- Rastreadores de terceros que recopilan sus datos
- Scripts maliciosos
- Seguimiento del comportamiento Elements



uBlock Origin en Mullvad Browser utiliza parámetros estandarizados para garantizar que todos los usuarios bloquean exactamente el mismo Elements, preservando así la uniformidad de las huellas digitales.



### **NoScript**


NoScript se ejecuta en segundo plano para gestionar los **niveles de seguridad** del navegador. Este:




- Controla la ejecución de JavaScript** según el nivel seleccionado (Normal/Más seguro/Más seguro)
- Filtra automáticamente los ataques XSS** (Cross-Site Scripting)
- Bloquea contenidos activos** peligrosos en sitios no HTTPS
- Su icono está oculto por defecto, pero puede mostrarse a través de "Personalizar la barra de herramientas"



### **Extensión *Mullvad Browser


Esta extensión específica de Mullvad ofrece diferentes funcionalidades dependiendo de si eres o no cliente de Mullvad VPN:



#### **Sin suscripción a Mullvad VPN:**




- Comprobación básica de la conexión**: muestra tu IP pública actual y alguna información sobre la conexión
- Recomendaciones de privacidad**: consejos para mejorar la configuración de seguridad (DNS, sólo HTTPS, motor de búsqueda)
- Control de WebRTC**: activar/desactivar para evitar fugas de IP Address
- Puede eliminarse sin impacto** en su huella digital si no utiliza Mullvad VPN



#### **Con suscripción a Mullvad VPN:**


La extensión revela todo su potencial con funciones avanzadas:





- Proxy SOCKS5 integrado**: conexión con un solo clic al servidor proxy VPN de Mullvad
 - IP Address fija**: a diferencia de una VPN, que puede cambiar su IP Address, un proxy garantiza siempre la misma Address de salida
 - Interruptor de corte automático**: si la VPN se desconecta, el tráfico del navegador se bloquea inmediatamente
 - Compatibilidad con IPv6**: Conectividad IPv6 aunque su conexión VPN no la tenga activada





- Multihop (doble VPN)**: posibilidad de cambiar la ubicación del proxy para crear un túnel dentro del túnel
 - Su tráfico pasa primero por su servidor VPN, luego "salta" a otro servidor Mullvad
 - Utilizar una localización diferente sólo para el navegador





- Supervisión avanzada de la conexión**: supervisión en tiempo real del estado de su VPN, del servidor conectado y detección de fugas DNS





- Acceso a Mullvad Leta**: motor de búsqueda privado reservado a los abonados (aunque no recomendado por Mullvad por razones de correlación con su cuenta)



Estas tres extensiones trabajan juntas para crear un ecosistema coherente de protección, en el que cada usuario se beneficia exactamente de las mismas defensas sin posibilidad de personalización que comprometa el anonimato colectivo.



## Ventajas y desventajas de Mullvad Browser



### Beneficios





- Excelente protección de la privacidad por defecto:** Mullvad Browser aplica una configuración de privacidad muy estricta desde el principio, sin necesidad de configuración manual.





- Mejor rendimiento que Tor Browser:** En ausencia de enrutamiento cebolla, Mullvad Browser es **notablemente más rápido y más sensible** que Tor Browser para la navegación web clásica.





- Simplicidad familiar de Interface:** Mullvad Browser está basado en Interface de Firefox. Si estás acostumbrado a Firefox o incluso Tor Browser, no te sentirás fuera de lugar.





- Colaboración de confianza y código auditado:** Mullvad Browser se beneficia de la experiencia del Proyecto Tor, y todo el código fuente está disponible para auditoría externa.



### Desventajas





- No hay anonimato en la red sin VPN:** El punto más importante es que **Mullvad Browser no oculta tu IP Address por sí mismo** (como todos los demás navegadores, excepto Tor Browser). Su IP Address es como su "Address postal" en Internet: revela su ubicación y su ISP. Por lo tanto **depende en gran medida de una VPN** (red privada virtual) para ocultar esta información crucial.





- No hay versión móvil:** Hasta la fecha, Mullvad Browser sólo está disponible en PC (Windows, Mac, Linux).





- Incompatible con ciertos hábitos:** El **modo privado permanente** significa que no se puede mantener una sesión de un uso al siguiente. Es imposible permanecer conectado a una cuenta web de una sesión a otra.





- Características restringidas:** Para preservar la uniformidad de las huellas, Mullvad Browser ha **deshabilitado varias características** presentes en Firefox y no está pensado para ser personalizado.



## Instalación del navegador Mullvad



Mullvad Browser está disponible gratuitamente para Windows, macOS y Linux. Para instalarlo, visite [el sitio web oficial de Mullvad](https://mullvad.net/browser).



![MULLVAD BROWSER](assets/fr/02.webp)



*Página de inicio oficial de Mullvad Browser con el botón de descarga resaltado.*



![MULLVAD BROWSER](assets/fr/03.webp)



*Seleccione su sistema operativo en la página de descarga de Mullvad Browser.*



Haga clic en el botón **"Descargar "** correspondiente a su sistema operativo.



Para Linux, puede elegir entre distintos formatos en función de su distribución. Una vez finalizada la descarga:



### En Windows


Ejecute el archivo `.exe` descargado y siga las instrucciones de instalación.



### En macOS


Abre el archivo `.dmg` descargado y arrastra la aplicación Mullvad Browser a tu carpeta Aplicaciones.



### En Linux


Extraiga el archivo `.tar.xz` en el directorio de su elección y ejecute el archivo `start-mullvad-browser.desktop`.



## Configuración y primer uso



Cuando inicies Mullvad Browser por primera vez, verás un Interface muy similar al de Tor Browser. El navegador está preconfigurado para la privacidad y no requiere modificaciones especiales.



![MULLVAD BROWSER](assets/fr/04.webp)



*Interface Página de inicio del navegador Mullvad con extensiones, icono de la escoba a generate una nueva identidad y menú de aplicaciones en la parte superior derecha.*



**Importante:** Mullvad Browser no enmascara su IP Address por defecto. Para una protección completa, recomendamos encarecidamente el uso de una VPN en paralelo. Puede utilizar Mullvad VPN o cualquier otro servicio VPN de confianza.



El navegador también incluye **DNS-sobre-HTTPS (DoH)** utilizando el servicio DNS de Mullvad: esta tecnología encripta sus peticiones DNS (traduciendo los nombres de los sitios en direcciones IP) para evitar que su ISP controle los sitios que visita.



### Ajustes de seguridad



Puedes ajustar el nivel de seguridad haciendo clic en el **menú de la aplicación** (tres barras horizontales) en la parte superior derecha, luego en **"Configuración "** y, por último, en la pestaña **"Privacidad y seguridad "**. Desplázate hasta la sección **"Seguridad "**:



![MULLVAD BROWSER](assets/fr/05.webp)



*Elección de los niveles de seguridad: las flechas indican el camino desde el menú de la aplicación hasta la pestaña "Privacidad y seguridad" y las opciones de seguridad*



Mullvad Browser ofrece tres niveles de seguridad:





- Normal** (nivel actual por defecto): Todas las funciones del navegador y del sitio web habilitadas





- Más seguro**: Desactiva funciones de sitios web a menudo peligrosas, lo que puede provocar una pérdida de funcionalidad en algunos sitios web:
 - JavaScript está desactivado en los sitios que no son HTTPS
 - Algunas fuentes y símbolos matemáticos están desactivados
 - El sonido y el vídeo (HTML5 media), así como WebGL, son "click to play"





- El más seguro**: Sólo permite las funciones de sitio web necesarias para sitios estáticos y servicios básicos:
 - JavaScript está desactivado por defecto en todos los sitios
 - Algunas fuentes, iconos, imágenes y símbolos matemáticos están desactivados
 - El sonido y el vídeo (HTML5 media), así como WebGL, son "click to play"



### Botón de nueva sesión



Para reiniciar con una sesión en blanco sin cerrar el navegador, haga clic en el icono de la escoba o utilice el menú de la aplicación > **"Nueva sesión "**.



![MULLVAD BROWSER](assets/fr/06.webp)



*Función "Restablecer su identidad" para reiniciar el navegador con una sesión completamente nueva*



## Uso diario



### Navegación normal



Mullvad Browser se comporta como un navegador clásico para la navegación diaria. Todos los sitios web son accesibles como de costumbre, con la ventaja añadida de una mayor protección contra el rastreo.



### Gestión de cookies e inicio de sesión



Debido al modo privado permanente, tendrás que volver a conectarte a tus cuentas cada vez que te conectes. Es el precio a pagar por la máxima confidencialidad.



### Extensiones



Mullvad Browser técnicamente te permite instalar extensiones adicionales del catálogo de Firefox, pero **es importante entender las implicaciones**. Cada extensión añadida cambia tu huella digital y te distingue de otros usuarios de Mullvad Browser, lo que va en contra del principio fundamental del navegador: hacer que todos los usuarios parezcan idénticos.



Como explica Mullvad: *"A veces, no tener ninguna defensa específica es mejor que tenerla. Al querer aumentar la privacidad en línea, instalas extensiones que, en última instancia, te hacen aún más visible. "*



Si decides instalar extensiones de todos modos, ten en cuenta que estás creando una huella digital única que puede ser utilizada para rastrearte de un sitio a otro. Para obtener la máxima protección, es mejor ceñirse a las tres extensiones preinstaladas, que son idénticas para todos los usuarios.



## Buenas prácticas con Mullvad Browser



1. **Usa siempre una VPN: Mullvad Browser no enmascara tu IP. Una VPN es esencial para el anonimato completo.



2. **No personalices el navegador**: Evita cambiar la configuración o añadir extensiones, ya que esto podría hacerte identificable.



3. **Utiliza el botón de nueva sesión**: Entre diferentes actividades, utiliza la función de reinicio para dividir tus sesiones.



4. **Elija el nivel de seguridad que mejor se adapte a sus necesidades**:




   - Normal (recomendado)**: Para la navegación diaria. Ya ofrece una protección excelente al tiempo que mantiene la funcionalidad de los sitios web. Es el mejor equilibrio para el 95% de los usuarios.
   - Más seguro**: Si visitas sitios desconocidos o potencialmente peligrosos, o para mayor protección en redes Wi-Fi públicas. Algunos sitios pueden funcionar mal.
   - El más seguro**: Reservado para situaciones de alto riesgo (periodismo de investigación, comunicaciones sensibles, entornos hostiles). La mayoría de los sitios modernos estarán rotos, pero ese es el precio de la máxima seguridad.



5. **Comprueba regularmente si hay actualizaciones**: Mantén tu navegador actualizado con los últimos parches de seguridad.



6. **Utiliza motores de búsqueda respetuosos con la privacidad**: Elige DuckDuckGo, Startpage o Searx en lugar de Google.



7. **Habilitar el modo "Sólo HTTPS "**: En la configuración, asegúrate de que el modo "Solo HTTPS" está activado para forzar conexiones seguras.



8. **NO cambie ninguna configuración avanzada**: A diferencia de otros navegadores, Mullvad Browser está diseñado para que TODOS los usuarios tengan exactamente la misma configuración. Modificar la configuración en `about:config` o cambiar la configuración de uBlock Origin/NoScript te haría único y desharía completamente el anonimato del navegador.



## Configuración DNS recomendada



Mullvad Browser integra automáticamente Mullvad DNS-over-HTTPS. Si está utilizando Mullvad VPN, la extensión le recomendará que **desactive Mullvad DoH** ya que es más rápido utilizar el servidor DNS de su servidor VPN. Si no está usando Mullvad VPN, mantenga Mullvad DoH activado para evitar la monitorización de DNS por su ISP.



## Conclusión



Mullvad Browser es una excelente solución para aquellos que buscan una navegación web respetuosa con la privacidad sin las limitaciones de rendimiento de la red Tor. Combinado con una VPN de calidad, ofrece una sólida protección contra el seguimiento y la vigilancia en línea.



Aunque tiene ciertas limitaciones (no tiene versión móvil, sesiones no persistentes), Mullvad Browser es una valiosa herramienta en el arsenal de cualquiera que desee recuperar el control de su privacidad digital. Su facilidad de uso y su configuración por defecto lo convierten en una sabia elección para los usuarios preocupados por su privacidad, ya sean principiantes o experimentados.



## Recursos



### Documentación oficial




- [Sitio web oficial del navegador Mullvad](https://mullvad.net/fr/browser)
- [Página de descarga de Mullvad Browser](https://mullvad.net/en/download/browser)
- [Especificaciones técnicas detalladas](https://mullvad.net/en/browser/Hard-facts)
- [Extensión del navegador Mullvad](https://mullvad.net/en/help/mullvad-browser-extension)



### Guías y explicaciones




- [Por qué es importante la privacidad](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor sin Tor: el concepto de navegador Mullvad](https://mullvad.net/en/browser/tor-without-tor)
- [Cómo elegir un navegador respetuoso con la privacidad](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Comprender la huella digital del navegador](https://mullvad.net/en/browser/browser-fingerprinting)



### Apoyo y ayuda




- [Centro de ayuda del navegador Mullvad](https://mullvad.net/en/help/tag/mullvad-browser)
- [Primeros pasos hacia la privacidad en línea](https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Recursos comunitarios




- [Guía del navegador Mullvad - Guías de privacidad](https://www.privacyguides.org/en/desktop-browsers/)
- [Debates comunitarios](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)
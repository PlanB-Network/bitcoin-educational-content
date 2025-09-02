---
name: Navegador Orion
description: ¿Cómo utilizar Orion Browser para proteger tu privacidad en Mac y iPhone?
---

![cover](assets/cover.webp)



## Introducción



En un contexto en el que la mayoría de los navegadores recopilan masivamente nuestros datos personales, la elección de un navegador respetuoso con la privacidad se vuelve crucial. Chrome domina con un 65% del mercado mundial, pero su modelo de negocio se basa en la explotación de tus datos de navegación. Safari, aunque integrado en el ecosistema de Apple, carece de funciones avanzadas de protección y no admite con flexibilidad extensiones de terceros.



![Répartition du marché des navigateurs](assets/fr/01.webp)


*Desglose del mercado de navegadores web: Chrome domina con más del 65% de cuota de mercado, seguido de Safari, Edge y Firefox*



**Orion Browser** se presenta como una alternativa innovadora para los usuarios de Apple. Desarrollado por Kagi, este navegador combina la velocidad del motor WebKit con una filosofía de telemetría cero. A diferencia de sus competidores, Orion no envía datos a servidores remotos y bloquea de forma nativa el 99,9% de los anuncios y rastreadores, incluido YouTube.



¿Su característica única? Orion es el **único navegador WebKit** que instala de forma nativa extensiones de Chrome **y** Firefox, ofreciendo lo mejor de ambos mundos. Esta compatibilidad, combinada con un consumo de memoria de 2 a 3 veces inferior al de otros navegadores y una integración perfecta con el ecosistema Apple (iCloud, Keychain), lo convierten en la opción ideal para los usuarios de Mac y iPhone preocupados por la privacidad.



## ¿Por qué elegir Orion Browser?



### Principales ventajas



**Máxima protección desde el primer momento**: Orion bloquea por defecto el 99,9% de los anuncios (incluido YouTube) y todos los rastreadores propios y de terceros. Su tecnología combina la Prevención Inteligente de Rastreo de WebKit con las listas de EasyPrivacy para lograr la máxima eficacia. Característica única: Orion bloquea los scripts de fingerprinting **antes de que se ejecuten**, haciendo que el rastreo sea literalmente imposible - un enfoque más radical que otros navegadores que sólo intentan "enmascarar" los datos.



**Cero telemetría verificable**: Orion adopta un enfoque radical de la privacidad, con cero telemetría por diseño. A diferencia de otros navegadores, que realizan cientos de solicitudes de red al iniciarse (exponente IP, huella digital del navegador, información personal), Orion nunca "llama a casa". Esta diferencia fundamental elimina por completo el riesgo de fuga involuntaria de datos.



**Rendimiento excepcional**: Basado en una versión optimizada de WebKit, Orion iguala o incluso supera a Safari en velocidad en el Mac. Las pruebas Speedometer 2.0/2.1 lo sitúan sistemáticamente en primer lugar en los procesadores Apple Silicon. El bloqueo nativo de anuncios acelera aún más la carga de páginas entre un 20 y un 40%.



**Soporte universal de extensiones**: Orion permite instalar extensiones de la Chrome Web Store **y** de Mozilla Add-ons. El soporte de WebExtensions es actualmente experimental, con un objetivo de compatibilidad del 100% en la versión beta. Puedes usar muchas extensiones populares como uBlock Origin, Bitwarden, incluso en iPhone - una primicia mundial en iOS, aunque algunas pueden no funcionar perfectamente.



### Limitaciones que hay que tener en cuenta





- Disponibilidad limitada**: Actualmente reservada para macOS e iOS/iPadOS. Una versión para Linux está alcanzando hitos de desarrollo (Hito 2 en 2025), pero no hay versión pública disponible. Windows y Android no están en desarrollo por falta de recursos.
- Código cerrado**: Aunque algunos componentes son de código abierto, Orion sigue siendo predominantemente propietario, un punto de debate en la comunidad de la privacidad.
- Extensiones experimentales**: El soporte de extensiones sigue en fase beta, con frecuentes incompatibilidades. Las extensiones pueden afectar al rendimiento, y algunas no funcionan en absoluto.
- Seguridad de WebKit**: A diferencia de Chromium, WebKit no ofrece un aislamiento de procesos por sitio tan robusto, lo que puede plantear riesgos de seguridad en determinados escenarios.
- Pruebas de bloqueo**: Orion obtiene deliberadamente malos resultados en las pruebas de publicidad online (26-35%), ya que Kagi considera que estas pruebas son "fundamentalmente defectuosas". La eficacia real en el uso diario es muy superior.



## Instalación de Orion Browser



### En macOS



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*La página de inicio de Kagi presenta Orion Browser como "un navegador sin publicidad con protección total de la privacidad y soporte universal de extensiones "*





- Ir a [kagi.com/orion](https://kagi.com/orion/)
- Haga clic en "**Descargar Orion para macOS**"



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*Página de descarga de Orion Browser para macOS e iOS, con enlaces a la App Store*





- Abra el archivo `.dmg` descargado
- Arrastre la aplicación Orion a la carpeta Aplicaciones
- En el primer inicio, macOS le pedirá que confirme la apertura



**Alternativa Homebrew**:


```bash
brew install --cask orion
```



### En iPhone/iPad





- Abre la **App Store**
- Buscar "**Orion Browser by Kagi**"
- Instala la aplicación gratuita (compatible con iOS 15+)



### Configuración inicial



En el primer lanzamiento, Orion te guía a través de varios pasos:



**1. Pantalla de bienvenida


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*Pantalla de bienvenida de Orion Browser en la que se destacan las principales características: navegación más rápida, telemetría cero, bloqueo de anuncios y compatibilidad con extensiones*



**2. Personalización Interface


![Options de personnalisation](assets/fr/05.webp)


*La pantalla de personalización te permite configurar el aspecto de las pestañas y de Interface según tus preferencias*





- Importación de datos**: Transfiere fácilmente favoritos y contraseñas desde Safari, Chrome o Firefox
- Sincronización con ICloud**: Actívala para encontrar tus favoritos y pestañas en todos tus dispositivos Apple



**3. Instalación en dispositivos móviles**


![Installation sur iOS](assets/fr/06.webp)


*Pantalla de instalación en iOS que muestra el código QR para descargar rápidamente Orion Browser de la App Store*



**4. Interface bienvenida y herramientas esenciales



![Page d'accueil Orion](assets/fr/07.webp)


*Página de inicio de Orion Browser Interface: la flecha indica las tres herramientas clave accesibles directamente desde la barra Address*



Una vez completada la configuración, descubrirá el Interface racionalizado de Orion con sus **tres herramientas esenciales** (indicadas por la flecha):





- Escudo 🛡️**: Muestra el informe de privacidad con el número de elementos bloqueados en la página actual
- Pincel 🖌️**: Personalizar la visualización de la página (tema, fuente, eliminar Elements que distrae)
- Engranaje ⚙️**: Configurar parámetros específicos del sitio web (permisos, bloqueos, etc.)



Estas herramientas están siempre disponibles y le permiten controlar su experiencia de navegación sitio por sitio.



**Importante**: Orion es gratuito y no requiere registro ni creación de cuenta para funcionar.



![Orion+ dans les préférences](assets/fr/08.webp)


*Pantalla de suscripción a Orion+ en las preferencias, que ofrece una suscripción opcional para apoyar el desarrollo*



**Orion+ (opcional)**: Para apoyar el desarrollo de proyectos, Kagi ofrece Orion+ ($5/mes, $50/año, o $150 de por vida). Esta suscripción voluntaria permite a:




- Comunicarse directamente con el equipo de desarrollo
- Influye en la evolución del navegador según tus necesidades
- Acceda a las versiones Nightly con las últimas funciones experimentales
- Benefíciate del último motor WebKit
- Consigue una insignia distintiva en el foro de comentarios



Orion+ garantiza la independencia del proyecto: "Tu contribución financiera nos ayuda a seguir siendo independientes y a mantener nuestra promesa de convertirnos en el mejor navegador para nuestros usuarios". Este modelo de financiación por parte de los usuarios es el que mantiene a Orion libre de publicidad y telemetría.



## Configuración para la máxima confidencialidad



### Parámetros esenciales



Accede a las preferencias a través de **Orion → Preferencias** (o ⌘,):



**1. Búsqueda - Motor de búsqueda privado**



![Configuration du moteur de recherche](assets/fr/09.webp)


*Configuración predeterminada del motor de búsqueda: DuckDuckGo está seleccionado para la máxima privacidad*





- Motor por defecto**: Selecciona **DuckDuckGo**, **Startpage** o **Kagi** para una privacidad óptima (evita Google/Bing)
- Sugerencias de búsqueda**: Desactívalas para evitar que las pulsaciones de teclas se filtren a los servidores de los motores de búsqueda



**2. Protección de la intimidad en general



![Content Blocker dans les préférences](assets/fr/12.webp)


*La configuración de privacidad de Orion muestra un bloqueador de contenidos con 119.156 reglas activas, opciones de eliminación de rastreadores y un agente de usuario personalizado*



**Bloqueador de contenidos activo por defecto**:




- EasyList**: 119k+ reglas de bloqueo de anuncios
- EasyPrivacy**: Protección contra el rastreo
- Gestionar listas de filtros**: Añadir listas adicionales (recomendado Hagezi)



**Opciones de privacidad**:




- Eliminar rastreadores de URL**: "Sólo para navegación privada" limpia los enlaces copiados
- Compartir informes de accidentes**: "Tras pedir aprobación" respeta su consentimiento
- Agente de usuario personalizado**: Puede modificarse para eludir ciertos bloqueos



![YouTube avec Privacy Report](assets/fr/10.webp)


*Ejemplo de YouTube visto con Orion: no se ve publicidad y el informe de privacidad muestra los numerosos Elements bloqueados*



**3. Configuración del sitio web - Control por sitio**



![Website Settings pour YouTube](assets/fr/11.webp)


*Configuración del sitio web para YouTube con opciones de compatibilidad, bloqueo de contenidos y permisos específicos del sitio*



**Acceso rápido**: Haz clic en el engranaje ⚙️ de la barra Address para ajustar:




- Modo de compatibilidad**: Resuelve los problemas de visualización suspendiendo las extensiones
- Bloqueadores de contenido**: Desactivar el bloqueo para un sitio específico si es necesario
- JavaScript/Cookies**: Control granular por sitio
- Permisos**: Cámara, micrófono, localización configurados individualmente



**4. Filtros personalizados avanzados** (véase más abajo)



**Crear filtros personalizados** (Privacidad → Gestionar listas de filtros → Filtros personalizados):



**Sintaxis simplificada** (compatible con Adblock Plus):




- `reddit.com##.promotedlink`: Oculta las publicaciones patrocinadas de Reddit
- `||ads.ejemplo.com^`: Bloquea completamente un dominio publicitario
- `@@||site-utile.com^`: Crea una excepción para un sitio



**Consejo: Visite [FilterLists.com](https://filterlists.com) para obtener miles de listas especializadas listas para usar.



### Extensiones recomendadas



Orion es compatible de forma nativa con las extensiones de Chrome y Firefox. Instálalas directamente desde las tiendas oficiales:



**Esenciales**:




- uBlock Origin**: Añade control granular al bloqueador nativo
- Bitwarden**: Gestor de contraseñas de código abierto
- BorrarURLs**: Elimina los parámetros de seguimiento de URL



**Opcional**:




- LocalCDN**: Sirve bibliotecas compartidas localmente
- Borrado automático de cookies**: Elimina automáticamente las cookies después de cerrar las pestañas
- NoScript**: Control total sobre la ejecución de JavaScript (usuarios avanzados)



Para instalar un:




- Visita [chrome.google.com/webstore](https://chrome.google.com/webstore) o [addons.mozilla.org](https://addons.mozilla.org)
- Haga clic en "Añadir a Chrome/Firefox"
- Orion interceptará e instalará la extensión automáticamente



**Precaución**: Como el soporte de extensiones es experimental, muchas extensiones pueden no funcionar correctamente o afectar al rendimiento. En caso de problema (el sitio deja de funcionar, lentitud), desactive las extensiones una a una para identificar el origen.



## Uso diario



### Interface y características únicas




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Menú de pinceles Orion para personalizar la visualización: tamaño de letra, tema (claro/oscuro), desactivación de cabeceras adhesivas y eliminación de Elements* que distraen la atención



**Herramienta de pincel: personalización avanzada**



La herramienta **brush** de Orion es una función única que le permite personalizar la visualización de cada sitio web:



**Opciones de tema**:




- Cambiar entre temas claros y oscuros para cada sitio
- Adaptación automática a las preferencias del sistema



**Control tipográfico**:




- Tamaño de letra**: Ajuste la legibilidad con los botones A- y A+
- Estilo de fuente**: Cambiar la familia de fuentes (predeterminada o personalizada)



**Limpieza Interface**:




- Desactivar cabeceras pegajosas**: Elimina las cabeceras que se quedan pegadas en la parte superior al desplazarse
- Borrar Elements**: Elimina permanentemente los molestos Elements (anuncios, pop-ups, banners de cookies)
  - Haga clic en "+ Borrar" y seleccione el elemento que desea ocultar
  - Muy útil para sitios con anuncios persistentes o seguimiento visual Elements



**Persistencia**: Todos estos ajustes se guardan por dominio y se vuelven a aplicar automáticamente la próxima vez que lo visites.



**Gestión avanzada de pestañas**:




- Pestañas verticales**: Activación a través de la barra de menús (función Pestañas laterales)
- Compactar pestañas**: En Preferencias → Pestañas → Diseño "Compactar" para ahorrar espacio
- Grupos de pestañas**: Organiza tus sesiones por temas
- Múltiples perfiles**: Cree identidades separadas a través de la barra de menús (función Perfiles) con datos completamente aislados



**Modo de bajo consumo**: Inspirado en el iPhone, este modo suspende automáticamente las pestañas inactivas después de 5 minutos y puede reducir el consumo de energía hasta en un 90%. Actívalo a través de la barra de menú de Orion en Mac, o en ajustes en iOS.



**Herramientas integradas** (menú Edición y otras):




- Editar texto en página**: modificar temporalmente cualquier texto (menú Editar)
- Permitir copiar y pegar**: Evita las restricciones de copia (menú Edición)
- Copiar enlace limpio**: Haga clic con el botón derecho en un enlace para eliminar los parámetros de seguimiento
- Modo Focus**: navegación a pantalla completa sin distracciones
- Imagen en imagen**: Ver vídeos en una ventana flotante
- Abrir en Internet Archive**: Acceso directo a las versiones archivadas
- Informe de privacidad**: Haga clic en el escudo 🛡️ para ver los elementos bloqueados por página



### Gestión de la navegación privada



La navegación privada de Orión (⌘⇧N) ofrece:




- Aislamiento completo de cookies y sesiones
- Eliminación automática al cierre
- Historial y desactivación de la caché
- Mayor protección contra las huellas dactilares



**Consejo**: Para una compartimentación avanzada, crea **perfiles separados** a través de la barra de menús (función Perfiles). Cada perfil aparece como una aplicación independiente en el Dock, con sus propios ajustes, extensiones y datos completamente aislados.



### Optimización del rendimiento y privacidad



Para mantener a Orión rápido y privado:




- Extensiones**: Limitar al mínimo estrictamente necesario (puede reducir el rendimiento)
- Modo de bajo consumo**: Activar para sesiones largas (90% de ahorro posible)
- Informe de privacidad**: Haga clic en el escudo 🛡️ para ver los bloqueos en tiempo real
- Personalización visual**: Utiliza el pincel 🖌️ para adaptar la visualización y eliminar Elements que distraen
- Copiar enlace limpio**: Haga clic con el botón derecho para copiar enlaces sin rastreadores
- Perfiles separados**: Utiliza perfiles dedicados para compartimentar tus actividades
- Configuración del sitio web**: Haga clic en el engranaje ⚙️ para adaptar los permisos por sitio
- Limpieza regular**: Borra la caché a través de Orion → Borrar datos de navegación



## Comparación con alternativas



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**Versus Safari**: Orion ofrece una protección superior con su bloqueador avanzado y su compatibilidad con extensiones, a la vez que mantiene el rendimiento de WebKit.



**Versus Chrome**: privacidad inigualable sin comprometer la compatibilidad, gracias a la compatibilidad con las extensiones de Chrome.



**Versus Firefox**: Más rápido en el Mac, Interface más intuitivo, pero menos control granular y no de código abierto.



**Versus Brave**: Filosofía similar, pero Orion evita las polémicas cripto/BAT y ofrece una mejor integración con Apple.



## Casos de uso recomendados



**Ideal para**:




- Los usuarios de Apple buscan más privacidad que Safari
- Personas que desean bloquear todos los anuncios (incluido YouTube) sin extensiones
- Desarrolladores que necesitan herramientas WebKit con protección de la intimidad integrada
- Los usuarios de iPhone quieren extensiones de escritorio en el móvil (innovación única)
- Profesionales que necesitan compartimentar sus actividades (perfiles múltiples)
- Usuarios de móviles que buscan una mejor gestión de la batería (modo de bajo consumo)



**Evitar si**:




- Utiliza principalmente Windows/Linux (ninguna versión disponible)
- El código abierto total es esencial para su modelo de amenazas
- Dependes de extensiones específicas que pueden no funcionar
- Necesitas sincronización entre plataformas más allá del ecosistema Apple
- Prefiere una solución probada y estable (estado beta permanente desde 2021)



## Puntos de atención y seguridad



### Funciones de seguridad exclusivas



**Protección revolucionaria contra fingerprinting**: Orion es el único navegador que bloquea completamente la ejecución de scripts de fingerprinting antes de que puedan escanear su sistema. Este enfoque de "ningún script en ejecución = ninguna huella digital posible" supera los métodos de enmascaramiento tradicionales utilizados por otros navegadores.



**Lista blanca transparente**: Orion mantiene una pequeña lista pública de sitios (browserbench.org, wizzair.com) en los que el bloqueo se desactiva automáticamente para evitar fallos de funcionamiento. Esta transparencia permite a los usuarios comprender exactamente cuándo y por qué se alivia el bloqueo.



**Extensiones no auditadas**: La compatibilidad con extensiones de Chrome/Firefox introduce riesgos adicionales, ya que estas extensiones no se diseñaron para WebKit y no se auditan específicamente para este entorno.



### Mantenimiento y actualizaciones





- Actualizaciones automáticas**: Orion se actualiza automáticamente en macOS a través de Sparkle
- Seguimiento de vulnerabilidades**: Comprobación periódica de las notas de la versión en busca de parches de seguridad
- Informe de errores**: Utilice [orionfeedback.org](https://orionfeedback.org) para notificar problemas




## Conclusión



Orion Browser representa un importante paso adelante para la privacidad en macOS e iOS. Su enfoque de telemetría cero, combinado con un bloqueador nativo ultraeficiente y un soporte único para extensiones universales, lo convierten en una excelente opción para los usuarios de Apple preocupados por la privacidad.



**Importante**: Orion permanece en beta permanente desde 2021, con limitaciones de compatibilidad de extensiones y riesgos inherentes a WebKit. Evalúe estas compensaciones en función de su modelo de amenazas.



Para el uso diario en un Mac o iPhone, es probablemente el mejor compromiso entre confidencialidad, rendimiento y facilidad de uso disponible en el ecosistema Apple, siempre que aceptes sus limitaciones.



Recuerda: proteger tu privacidad no depende sólo de tu navegador. Combina Orion con las mejores prácticas (contraseñas seguras, 2FA, VPN si es necesario) para una seguridad online óptima.



## Recursos y apoyo



### Documentación oficial




- Página web oficial**: [kagi.com/orion](https://kagi.com/orion/)
- Preguntas más frecuentes**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- Foro de la comunidad**: [community.kagi.com](https://community.kagi.com)
- Seguimiento de errores**: [orionfeedback.org](https://orionfeedback.org)
- GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Componentes de código abierto
- Blog Kagi**: [blog.kagi.com](https://blog.kagi.com) - Noticias y actualizaciones



### Pruebas de verificación recomendadas



Después de la configuración, pruebe su configuración:




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Prueba de huellas dactilares
- [Prueba de fugas DNS](https://www.dnsleaktest.com/) - Compruebe si hay fugas DNS
- [BrowserLeaks](https://browserleaks.com/) - Conjunto completo de pruebas de privacidad



### Alternativas para Plan ₿ Network


Para una protección máxima, consulte nuestras otras guías:




- [Firefox reforzado](https://planb.network/tutorials/computer-security/firefox) - Configuración multiplataforma avanzada
- [Navegador Tor](https://planb.network/tutorials/computer-security/tor-browser) - Anonimato total en la red
- [Mullvad Browser](https://planb.network/tutorials/computer-security/mullvad-browser) - Máxima protección contra huellas dactilares



Si quieres aprender más sobre la historia y el funcionamiento de los navegadores, así como sobre los principales objetos digitales de tu vida cotidiana, te invito a descubrir nuestro nuevo curso de formación gratuito SCU 202, disponible en Plan ₿ Network:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
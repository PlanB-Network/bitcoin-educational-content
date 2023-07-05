---
name: Seguridad informática y gestión de datos
goal: Actualizar la gestión de contraseñas y datos personales. Crear una copia de seguridad, protegerse de los hackers y concienciarse sobre la vigilancia masiva.
objectives:
  - Actualizar sobre la gestión de sus datos personales y las herramientas que refuerzan su seguridad.
  - Implementar un gestor de contraseñas seguro y fácil de usar.
  - Implementar la autenticación de dos factores para fortalecer su seguridad y minimizar los riesgos de hackeo.
---

# Un viaje hacia la protección de sus datos

Es importante entender que las contraseñas simples y reutilizadas pueden ser fácilmente pirateadas por hackers, quienes pueden aprovechar su información personal con fines maliciosos.

Para evitar esto, le mostraremos cómo utilizar un gestor de contraseñas seguro como Bitwarden y migrar sus contraseñas desde otros servicios de almacenamiento. Abordaremos la importancia de proteger sus datos personales, incluyendo el uso de copias de seguridad en discos duros externos y seudónimos para ocultar su identidad en línea.

También discutiremos quién está mejor posicionado para proteger al usuario: las empresas, la regulación o el propio usuario.

Equipo de colaboradores:

- Renaud Lifchitz; profesor
- Thép Pantamis; profesor
- Muriel; diseño
- Rogzy Noury & Fabian; producción
- Théo; contribución

+++

# introducción: Seguridad 101: Refinando su Higiene Digital

![introducción](https://youtu.be/DqLf72XBJUg)

Bienvenidos a todos a este programa educativo dedicado a la seguridad digital. Esta formación está diseñada para ser accesible para todos, sin necesidad de conocimientos informáticos previos. Es un gran placer presentarles a mis colegas expertos, Théo y Renaud, quienes nos acompañarán en este viaje educativo.

Nuestro objetivo principal es proporcionarles los conocimientos y habilidades necesarios para navegar de manera más segura y privada en el mundo digital. Para comenzar, Renaud nos da un valioso consejo: adoptar gradualmente una actitud de desconfianza cautelosa. Esta es un enfoque crucial que debe aplicarse en muchos aspectos de la seguridad digital.

## Sección 1: Teoría - Navegación Segura, Evitación de Enlaces Peligrosos y Protección de la Privacidad en línea

En esta primera sección, abordaremos los aspectos teóricos de la seguridad digital. Discutiremos la navegación segura, la evitación de enlaces peligrosos y la protección de la privacidad en línea. Comprender cómo identificar un enlace potencialmente malicioso y proteger su privacidad son elementos esenciales para protegerse contra las amenazas de ciberseguridad.
Exploraremos consejos prácticos para verificar la fuente de los enlaces antes de hacer clic en ellos y para utilizar herramientas como navegadores web privados, redes privadas virtuales (VPN) y firewalls.

## Sección 2: Práctica - Gestión de Credenciales y Contraseñas, Bandejas de Entrada de Correo y Autenticación de Dos Factores

En esta segunda sección práctica, abordaremos la gestión de credenciales y contraseñas, así como otros aspectos importantes de la seguridad digital. Examinaremos las mejores prácticas para gestionar de manera segura sus credenciales y contraseñas, utilizando administradores de contraseñas. También discutiremos la importancia de proteger sus bandejas de entrada de correo contra ataques e intrusiones.

Presentaremos herramientas y técnicas para crear contraseñas sólidas y únicas para cada cuenta, y explicaremos cómo utilizar un administrador de contraseñas para gestionar eficientemente su información de inicio de sesión. Además, abordaremos la autenticación de dos factores (2FA) como una medida de seguridad adicional para proteger sus cuentas en línea.

Al comprender y aplicar estas prácticas de gestión de credenciales, contraseñas, bandejas de entrada de correo y autenticación de dos factores, fortalecerá considerablemente la seguridad de su información en línea.

## Sección Bonus: Entrevista con Pantamis y Renaud

Como bonificación, les ofrecemos una entrevista exclusiva con Pantamis y Renaud, nuestros expertos en seguridad digital. Compartirán sus conocimientos profundos y consejos adicionales para fortalecer su higiene digital. No pierda esta oportunidad de aprender más de estos profesionales experimentados.

Este programa de capacitación se ofrece de forma gratuita bajo una licencia redistribuible. Queremos expresar nuestro agradecimiento a nuestros Patreons y a nuestro equipo de filmación por su apoyo indispensable en la realización de esta capacitación. También agradecemos a todos nuestros donantes y seguidores que nos permiten seguir produciendo contenido educativo gratuito en tres idiomas.

# Navegación en línea

![navegación en línea](https://youtu.be/BEK7vGnkO64)

## La elección del navegador web

### Errores comunes al navegar por Internet y cómo evitarlos

Al navegar por Internet, es importante evitar algunos errores comunes para preservar su seguridad en línea. Aquí hay algunos consejos para evitarlos:

- Error relacionado con la descarga de software: Se recomienda descargar software desde el sitio web oficial del editor en lugar de sitios genéricos. También se aconseja preferir software de código abierto y gratuito, ya que suelen ser más seguros y libres de software malicioso.
- Error relacionado con los navegadores web: Hay dos grandes familias de navegadores, aquellos basados en Chrome y aquellos basados en Firefox. Aunque ambas familias de navegadores ofrecen un nivel de seguridad similar, se recomienda evitar el navegador Chrome de Google debido a sus rastreadores. Pueden preferirse alternativas más ligeras de Chrome, como Chromium o Brave. Puede ser necesario utilizar diferentes navegadores para acceder a ciertos sitios. Se puede recomendar el uso del navegador Brave debido a su bloqueador de anuncios integrado. También es importante limitar la cantidad de extensiones instaladas para evitar problemas de seguridad y rendimiento.
- Error relacionado con la gestión de cookies: Las cookies son archivos creados por los sitios web para almacenar información en su dispositivo. Algunos sitios requieren el uso de cookies para funcionar correctamente, sin embargo, es importante tener en cuenta que las cookies también pueden ser compartidas con terceros para fines de seguimiento publicitario. Según regulaciones como el RGPD, es posible rechazar las cookies de seguimiento de terceros. Se recomienda aceptar solo las cookies necesarias para el correcto funcionamiento del sitio y eliminar las cookies una vez que haya abandonado el sitio, utilizando una extensión o programa dedicado a la gestión de cookies.

### Los navegadores web: elección, seguridad y gestión de cookies

Ya hemos mencionado que los navegadores basados en Chrome y Firefox ofrecen un nivel de seguridad similar, pero se recomienda evitar el navegador Chrome de Google debido a sus rastreadores. Puede ser necesario utilizar varios navegadores para acceder a ciertos sitios, y Brave puede ser preferido por su bloqueador de anuncios integrado.

En cuanto a la gestión de cookies, es importante rechazar las cookies de seguimiento de terceros mientras se aceptan las cookies necesarias para el funcionamiento del sitio. Después de abandonar un sitio, se recomienda eliminar las cookies asociadas a él utilizando una extensión o programa dedicado.

Algunos navegadores permiten eliminar cookies o sesiones de forma selectiva. Sin embargo, es importante encontrar el equilibrio adecuado entre conveniencia, facilidad de uso y seguridad. Es importante tener en cuenta que incluso si se eliminan las cookies, es posible que la información recopilada por las cookies de diferentes sitios aún esté interconectada.

Teniendo en cuenta estas recomendaciones para la elección de navegadores, la gestión de cookies y la seguridad en línea, podrá navegar por Internet de manera más segura y proteger su privacidad.

### La navegación privada, TOR y otras alternativas para una navegación más segura y anónima

La navegación privada, aunque no oculta la navegación a su proveedor de servicios de Internet, permite no dejar rastros locales en su computadora. Las cookies se eliminan automáticamente al final de cada sesión, lo que permite aceptar todas las cookies sin ser rastreado. La navegación privada puede ser útil al comprar servicios en línea, ya que los sitios web siguen nuestros hábitos de búsqueda y ajustan los precios en consecuencia. Sin embargo, es importante tener en cuenta que la navegación privada se recomienda para sesiones temporales y específicas, no para un uso general de navegación en Internet.

Una alternativa más avanzada es la red TOR (The Onion Router), que ofrece anonimato al ocultar la dirección IP del usuario y permitir el acceso a la Darknet. TOR Browser es un navegador especialmente diseñado para utilizar la red TOR. Permite visitar tanto sitios web convencionales como sitios web en .onion, que generalmente son operados por individuos y pueden ser ilegales.

TOR es legal y es utilizado por periodistas, activistas de la libertad y otras personas que desean evitar la censura en países autoritarios. Sin embargo, es importante entender que TOR no asegura los sitios visitados ni la computadora en sí. Además, el uso de TOR puede ralentizar la conexión a Internet ya que los datos pasan por las computadoras de otras tres personas antes de llegar a su destino. También es esencial tener en cuenta que TOR no es una solución infalible para garantizar el anonimato al 100% y no debe ser utilizado para llevar a cabo actividades ilegales.

## Tutorial: BRAVE

**_Tutorial en construcción, para contribuir o agregarlo, puede pasar por GitHub_**

# VPN y conexión a Internet

![vpn et connexion internet](https://youtu.be/oRO7sGexvzo)

## Utilizar Internet de manera segura

### Los VPN

La higiene digital es un aspecto crucial de la seguridad en línea, y el uso de redes privadas virtuales (VPN) es un método efectivo para mejorar esta seguridad, tanto para empresas como para usuarios individuales.

Los VPN son herramientas que cifran los datos transmitidos por Internet, lo que hace que la conexión sea más segura. En un contexto empresarial, los VPN permiten a los empleados acceder de forma remota a la red interna de la empresa de manera segura. Los datos intercambiados están encriptados, lo que dificulta mucho su interceptación por parte de terceros. Además de asegurar el acceso a una red interna, el uso de un VPN puede permitir que un usuario haga pasar su conexión a Internet a través de la red interna de la empresa, dando la impresión de que su conexión proviene de la empresa. Esto puede ser especialmente útil para acceder a servicios en línea que están geográficamente restringidos.
Il existe deux types principaux de VPN : les VPN d'entreprise et les VPN grand public, comme NordVPN. Les VPN d'entreprise tendent à être plus coûteux et complexes, tandis que les VPN grand public sont généralement plus accessibles et faciles à utiliser. NordVPN, por ejemplo, permite a los usuarios conectarse a internet a través de un servidor ubicado en otro país, lo que puede permitir eludir las restricciones geográficas.

Sin embargo, el uso de un VPN grand public no garantiza una anonimización completa. Muchos proveedores de VPN conservan información sobre sus usuarios, lo que puede comprometer potencialmente su anonimato. Aunque los VPN pueden ser útiles para mejorar la seguridad en línea, no son una solución universal. Son efectivos para algunos usos específicos, como acceder a servicios geográficamente limitados o mejorar la seguridad mientras se está en movimiento, pero no garantizan una seguridad total. Al elegir un VPN, es esencial priorizar la confiabilidad y la tecnicidad en lugar de la popularidad. Los proveedores de VPN que recopilan la menor cantidad de información personal suelen ser los más seguros. Servicios como iVPN y Mulvad no recopilan información personal e incluso permiten pagos con Bitcoin para una mayor privacidad.

Por último, un VPN también se puede utilizar para bloquear anuncios en línea, ofreciendo así una experiencia de navegación más agradable y segura. Sin embargo, es importante realizar su propia investigación para encontrar el VPN más adecuado a sus necesidades específicas. En cuanto a la seguridad en línea, es esencial comprender que la 4G generalmente es más segura que el Wi-Fi público. Sin embargo, el uso de la 4G puede agotar rápidamente su plan de datos móviles. El protocolo HTTPS se ha convertido en la norma para el cifrado de datos en sitios web. Asegura que los datos intercambiados entre el usuario y el sitio web estén seguros. Por lo tanto, es crucial verificar que el sitio que está visitando esté utilizando el protocolo HTTPS.
En la Unión Europea, la protección de datos está regulada por el Reglamento General de Protección de Datos (RGPD). Por lo tanto, es más seguro utilizar proveedores europeos de puntos de acceso Wi-Fi, como la SNCF, que no revenden los datos de conexión de los usuarios. Sin embargo, el simple hecho de que un sitio muestre un candado no garantiza su autenticidad. Es importante verificar la clave pública del sitio utilizando un sistema de certificados para confirmar su autenticidad. Aunque el cifrado de datos evita que terceros intercepten los datos intercambiados, aún es posible que una persona malintencionada se haga pasar por el sitio y transfiera los datos en claro. Para evitar estafas en línea, es crucial verificar la identidad del sitio en el que estás navegando, controlando especialmente la extensión y el nombre de dominio. Además, mantente alerta ante los estafadores que utilizan letras similares en las URL para engañar a los usuarios.

Se recomienda utilizar una VPN para reforzar la seguridad, incluso cuando se navega por Internet desde casa. Esto contribuye a garantizar un nivel más alto de seguridad para los datos intercambiados en línea. Por último, asegúrate de verificar las URL y el candado en la barra de direcciones para confirmar que estás en el sitio que crees estar visitando.

En resumen, el uso de una VPN puede mejorar en gran medida la seguridad en línea, tanto para las empresas como para los usuarios individuales. Además, la adopción de buenas prácticas de navegación puede contribuir a una mejor higiene digital. En el próximo segmento de este curso, abordaremos la seguridad de la computadora, incluyendo las actualizaciones, el antivirus y la gestión de contraseñas.

## Tutorial: IVPN

**_Tutorial en construcción, para contribuir o agregarlo, puedes pasar por GitHub_**

# Uso de la computadora

![Uso de la computadora](https://youtu.be/lzJr5CIulSU)

## Buenas prácticas de uso

La seguridad de nuestras computadoras es un tema importante en el mundo digital actual. Hoy vamos a abordar tres puntos clave: la elección de la computadora, las actualizaciones y el antivirus para una seguridad óptima, y finalmente, las buenas prácticas para la seguridad de la computadora y los datos.

En cuanto a la elección de la computadora, no hay una diferencia significativa de seguridad entre las computadoras antiguas y las nuevas. Sin embargo, existen diferencias de seguridad entre los sistemas operativos: Windows, Linux y Mac. Se recomienda no utilizar una cuenta de administrador a diario, sino crear dos cuentas separadas: una cuenta de administrador y una cuenta para uso diario. Windows a menudo está más expuesto a software malicioso debido a su gran número de usuarios y a la facilidad de cambiar de usuario a administrador. Por otro lado, las amenazas son menos numerosas en Linux y Mac.
El **choix du système d'exploitation** doit être effectué en fonction de vos besoins et de vos préférences. Les systèmes Linux ont considérablement évolué ces dernières années, devenant de plus en plus conviviaux. **Ubuntu** est une alternative intéressante pour les débutants, avec une interface graphique facile à utiliser. Il est possible de partitionner un ordinateur pour expérimenter avec Linux tout en conservant Windows, mais cela peut se révéler complexe. Il est souvent préférable d'avoir un ordinateur dédié, une machine virtuelle ou une clé USB pour tester Linux ou Ubuntu.

En ce qui concerne les **mises à jour et l'antivirus** pour une sécurité optimale, la mise à jour régulière du système d'exploitation et des applications est primordiale. Sur Windows 10, les mises à jour sont quasi continues et il est crucial de ne pas les bloquer ou les retarder. Chaque année, environ 15 000 vulnérabilités sont identifiées, ce qui souligne l'importance de maintenir les logiciels à jour pour se prémunir contre les virus. En général, le support logiciel se termine entre 3 et 5 ans après sa sortie, il est donc nécessaire de passer à la version supérieure pour continuer à bénéficier de la sécurité.

**Windows Defender**, l'antivirus intégré à Windows, est une solution sûre et efficace. Il convient de faire preuve de prudence avec les antivirus téléchargés sur Internet, qui peuvent être malveillants ou obsolètes. Linux et Mac, grâce à leur système de séparation des droits des utilisateurs, n'ont souvent pas besoin d'antivirus. Pour ceux qui souhaitent investir dans un antivirus payant, il est recommandé de choisir un antivirus qui analyse intelligemment les menaces inconnues et émergentes, comme **Kaspersky**. Les mises à jour de l'antivirus sont essentielles pour se protéger contre les nouvelles menaces.

Pour finir, voici quelques **bonnes pratiques pour la sécurité de votre ordinateur et de vos données**. Il est important de choisir un antivirus efficace et agréable à utiliser. Il est également crucial d'adopter de bonnes pratiques sur son ordinateur, comme ne pas insérer de clés USB inconnues ou trouvées à des endroits suspects. Ces clés USB peuvent contenir des programmes malveillants qui peuvent se lancer automatiquement dès leur insertion. Le contrôle de la clé USB ne servira à rien une fois qu'elle aura été insérée. Certaines entreprises ont été victimes de piratage en raison de clés USB laissées négligemment dans des zones accessibles, comme un parking.
Trata tu computadora como lo harías con tu casa: mantente alerta, realiza actualizaciones regularmente, elimina archivos innecesarios y utiliza una contraseña segura para la seguridad. Es crucial cifrar los datos en computadoras portátiles y teléfonos inteligentes para prevenir robos o pérdidas de datos. BitLocker para Windows, Lux para Linux y la opción integrada para Mac son soluciones para el cifrado de datos. Se recomienda activar el cifrado de datos sin dudarlo y anotar la contraseña en un papel para mantenerla segura.

En conclusión, es fundamental optar por un sistema operativo adecuado a tus necesidades y mantenerlo actualizado, al igual que las aplicaciones instaladas en él. También es esencial utilizar un antivirus eficaz y fácil de usar, y adoptar buenas prácticas para la seguridad de tu computadora y tus datos.

## Tutorial: Ubuntu

**_Tutorial en construcción, para contribuir o agregarlo, puedes utilizar GitHub_**

# Hack y gestión de copias de seguridad: protege tus datos

![hack y gestión de copias de seguridad](https://youtu.be/CJDjWPV3PeU)

## Ciberseguridad y prevención

Phishing, precaución ante correos electrónicos fraudulentos:
Permanece atento a los intentos de phishing que buscan obtener información sensible como tus credenciales y contraseñas. Evita hacer clic en enlaces sospechosos y compartir tu información personal sin verificar la legitimidad del remitente.

Cuidado con los adjuntos e imágenes en los correos electrónicos:
Los adjuntos e imágenes en los correos electrónicos pueden contener software malicioso. No descargues ni abras adjuntos de remitentes desconocidos o sospechosos, y asegúrate de que tu antivirus esté actualizado.

Ransomware y tipos de ciberataques:
El ransomware es un tipo de software malicioso que cifra los datos del usuario y exige un rescate para descifrarlos. Infórmate sobre los diferentes tipos de ciberataques y toma medidas para proteger tu sistema y tus datos.

Reacción ante la detección de un virus:
Si detectas un virus en tu computadora, desconéctala de Internet, realiza un análisis antivirus completo y elimina los archivos infectados. Luego, actualiza tus software y sistema operativo, y cambia tus contraseñas para evitar intrusiones adicionales.

## Respaldo de datos

Realiza copias de seguridad periódicas de tus datos importantes en un dispositivo externo o un servicio de almacenamiento en línea seguro. De esta manera, en caso de un ataque informático o un fallo de hardware, podrás recuperar tus datos sin perder información crucial.
Pagar a los hackers, una mala idea: Generalmente se desaconseja pagar a los hackers en caso de ransomware u otros tipos de ataques. Pagar el rescate no garantiza la recuperación de tus datos y puede alentar a los ciberdelincuentes a continuar con sus actividades maliciosas. Es mejor priorizar la prevención y realizar copias de seguridad regulares de tus datos para protegerte.

# Gestión del correo electrónico

![gestión del correo electrónico](https://youtu.be/WjqH882f4cY)

En esta sección, abordaremos tres temas esenciales para garantizar la seguridad de los accesos en línea: la gestión de correos electrónicos, el uso de un gestor de contraseñas y la autenticación de dos factores (2FA).

### Elección del proveedor de correo electrónico y gestión de las direcciones de correo

La gestión adecuada de nuestras direcciones de correo electrónico es crucial para garantizar la seguridad de nuestros accesos en línea. Es importante elegir un proveedor de correo seguro y respetuoso con la privacidad. Por ejemplo, ProtonMail es un servicio de correo seguro y respetuoso con la privacidad.

Al elegir un proveedor de correo electrónico y crear una contraseña, es esencial no reutilizar la misma contraseña para diferentes servicios en línea. Se recomienda crear nuevas direcciones de correo regularmente y separar los usos utilizando diferentes direcciones de correo. Es mejor optar por un servicio de correo seguro para las cuentas críticas. También es importante tener en cuenta que algunos servicios limitan la longitud de las contraseñas, por lo que es importante tener cuidado con esta limitación. También hay servicios disponibles para la creación de direcciones de correo temporales, que se pueden utilizar para cuentas de duración limitada.

Es importante tener en cuenta que los proveedores de correo antiguos como La Poste, Arobase, Wig, Hotmail, todavía se utilizan, pero sus prácticas de seguridad pueden ser peores que las de Gmail. Por lo tanto, se recomienda tener dos direcciones de correo distintas, una para comunicaciones generales y otra para la recuperación de cuentas, esta última debe estar más segura. Es mejor evitar mezclar la dirección de correo con el operador telefónico o proveedor de acceso a Internet, ya que esto puede ser un vector de ataque.
Seguridad de las direcciones de correo y uso de Have I Been Pwned para verificar las filtraciones de datos

Se recomienda utilizar el sitio Have I Been Pwned (¿Has sido hackeado?) para verificar si nuestra dirección de correo ha sido comprometida y para recibir alertas sobre futuras filtraciones de datos. Una base de datos hackeada puede ser aprovechada por los piratas informáticos para enviar correos de phishing o reutilizar contraseñas comprometidas.
El sitio Have I Been Pwned permite verificar si nuestra dirección de correo electrónico ha sido comprometida sin comunicar directamente esta dirección. Por lo tanto, se recomienda crear una segunda dirección de correo electrónico para fines de seguridad adicional. Los correos electrónicos son un medio de comunicación que debería seguir utilizándose durante mucho tiempo. Sin embargo, es crucial asegurar nuestras contraseñas y establecer una autenticación de dos factores para fortalecer la seguridad de nuestras cuentas de correo.

## Tutorial: creación de una cuenta ProtonMail

**_Tutorial en construcción, para contribuir o agregarlo, puedes pasar por GitHub_**

# Gestor de contraseñas

![gestor de contraseñas](https://youtu.be/HzLuZ6noePY)

Para garantizar la seguridad de tu cuenta, es crucial crear contraseñas fuertes y seguras. La longitud de la contraseña no es suficiente para asegurar su seguridad. Los caracteres deben ser completamente aleatorios para resistir los ataques de fuerza bruta. La independencia de los eventos también es importante para evitar las combinaciones más probables. Las contraseñas comunes como "password" son fácilmente comprometidas.

Para crear una contraseña fuerte, se recomienda utilizar un gran número de caracteres aleatorios, sin utilizar palabras o patrones predecibles. También es esencial incluir números y caracteres especiales. Sin embargo, debes tener en cuenta que algunos sitios pueden restringir el uso de ciertos caracteres especiales. Las contraseñas que no se generan de manera aleatoria son fáciles de adivinar. Las variantes o adiciones a las contraseñas no son seguras. Los sitios web no pueden garantizar la seguridad de las contraseñas elegidas por los usuarios.

Las contraseñas generadas de manera aleatoria ofrecen un nivel de seguridad superior, aunque pueden ser más difíciles de recordar. Los gestores de contraseñas pueden generar contraseñas aleatorias más seguras. Al utilizar un gestor de contraseñas, no necesitas memorizar todas tus contraseñas. Es importante reemplazar gradualmente tus contraseñas antiguas por las generadas por el gestor, ya que son más fuertes y más largas. Asegúrate de que la contraseña maestra de tu gestor de contraseñas también sea fuerte y segura.

## Tutorial: creación de una contraseña maestra

**_Tutorial en construcción, para contribuir o agregarlo, puedes pasar por GitHub_**

## Tutorial: BitWarden

**_Tutorial en construcción, para contribuir o agregarlo, puedes pasar por GitHub_**

## Tutorial: KeePass

**_Tutorial en construcción, para contribuir o agregarlo, puedes pasar por GitHub_**

# Los 2 factores de autenticación

![los 2FA](https://youtu.be/863n4N1XNjk)
Las diferentes opciones para la autenticación fuerte ofrecen niveles variables de seguridad. Los SMS no se consideran la mejor opción ya que solo proporcionan una prueba de posesión de un número de teléfono. El 2FA (autenticación de dos factores) es más seguro ya que utiliza varios tipos de pruebas, como el conocimiento, la posesión y la identificación. Los códigos de contraseñas de un solo uso (HOTP y TOTP) son más seguros que los SMS ya que requieren un cálculo criptográfico y se almacenan localmente en lugar de en la memoria. Los tokens físicos, como las llaves USB o las tarjetas inteligentes, ofrecen una seguridad óptima al generar una clave privada única para cada sitio y verificar la URL antes de autorizar la conexión.

Para una seguridad óptima con la autenticación fuerte, se recomienda utilizar una dirección de correo electrónico segura, un administrador de contraseñas seguro y adoptar un 2FA utilizando UBKey. También se recomienda comprar dos UBKey para prever la pérdida o el robo. La biometría se puede utilizar como un sustituto, pero es menos segura que la combinación de conocimiento y posesión. Los datos biométricos deben permanecer en el dispositivo de autenticación y no deben ser divulgados en línea. Es importante tener en cuenta el modelo de amenaza asociado con los diferentes medios de autenticación y adaptar su práctica en consecuencia.

Los tokens de autenticación fuerte, como FIDO, 2F y WebAuthn, asociados con una contraseña, ofrecen un alto nivel de seguridad. Se recomienda tener dos tokens y mantener una copia de seguridad tanto en casa como en uno mismo. El cifrado y la autenticación son conceptos diferentes en criptografía. Para asegurar los datos, es esencial implementar el 2FA y utilizar soluciones como OTI, Google Authenticator y YubiKey.

En conclusión, comprender las diferentes opciones de autenticación fuerte y elegir el método más adecuado es esencial para proteger nuestros datos. Gracias por asistir a esta presentación y no olvide seguir los recursos disponibles para obtener más información y capacitación sobre el tema.

## Tutorial: soluciones 2FA y Yubikey

**_Tutorial en construcción, para contribuir o agregarlo, puede pasar por GitHub_**

# Ir más allá

## cómo trabajar en esta industria

![conclusión y trabajar en la industria](https://youtu.be/YZ2EKaPvoZU)

## Entrevista con Renaud

![Entrevista](https://youtu.be/RVjE-KOSKDs)

### Gestión eficiente de contraseñas y fortalecimiento de la autenticación: un enfoque académico

En el módulo de formación "Sécurité 101" ofrecido por Découvre Bitcoin en la Academia, hemos abordado la importancia de los gestores de contraseñas. Tres dimensiones son esenciales a considerar: la creación, la actualización y la implementación de contraseñas en sitios web.
Generalmente se desaconseja el uso de extensiones de navegador para el autocompletado de contraseñas. Estas herramientas pueden hacer que el usuario sea más vulnerable a ataques de phishing. Renaud, reconocido experto en ciberseguridad, prefiere una gestión manual a través de KeePass, lo que implica copiar y pegar manualmente la contraseña. Las extensiones tienden a aumentar la superficie de ataque, pueden ralentizar el rendimiento del navegador y, por lo tanto, presentan un riesgo significativo. Por lo tanto, se recomienda minimizar el uso de extensiones en el navegador.

Los gestores de contraseñas suelen fomentar el uso de factores de autenticación adicionales, como la autenticación de dos factores. Para una seguridad óptima, se recomienda guardar los OTP (One-Time Passwords) en el dispositivo móvil. AndoTP ofrece una solución de código abierto para generar y almacenar códigos OTP en el teléfono. Si bien Google Authenticator permite exportar las semillas de los códigos de autenticación, la confianza en la copia de seguridad en una cuenta de Google sigue siendo limitada. Por lo tanto, se recomiendan las aplicaciones OTI y AndoTP para una gestión autónoma de los OTP.

La cuestión de la herencia digital y el duelo digital destaca la importancia de tener un procedimiento para transmitir contraseñas después del fallecimiento de una persona. Un gestor de contraseñas facilita esta transición almacenando de forma segura todos los secretos digitales en un solo lugar. El gestor de contraseñas también permite identificar todas las cuentas abiertas y gestionar su cierre o transferencia. Se recomienda anotar la contraseña maestra en papel, pero se debe guardar en un lugar oculto y seguro. Si el disco duro está cifrado y el ordenador está bloqueado, la contraseña no será accesible, incluso en caso de robo.

### Hacia una era post-contraseña: exploración de alternativas creíbles

Las contraseñas, aunque omnipresentes, tienen muchas desventajas, especialmente la posibilidad de una transmisión arriesgada durante el proceso de autenticación. Empresas líderes como Microsoft y Apple ofrecen alternativas innovadoras como la biometría y los tokens de hardware, lo que indica una tendencia progresiva hacia el abandono de las contraseñas.
'Passkeys, por ejemplo, ofrece claves cifradas aleatorias, combinadas con un factor local (biometría o NIP), que son alojadas por un proveedor pero que están fuera de su alcance. Aunque esto requiere una actualización de los sitios web, este enfoque elimina la necesidad de contraseñas, ofreciendo así un alto nivel de seguridad sin las limitaciones asociadas con las contraseñas tradicionales o la gestión de una bóveda digital.

Passkiz es otra alternativa viable y segura para la gestión de contraseñas. Sin embargo, surge una pregunta importante: la disponibilidad en caso de fallo del proveedor. Sería deseable que los gigantes de internet ofrecieran sistemas para garantizar esta disponibilidad.

La autenticación directa en el servicio en cuestión es una opción interesante para no depender de un tercero. Sin embargo, el SSO (Single Sign-On) propuesto por los gigantes de internet también plantea problemas en términos de disponibilidad y riesgos de censura. Para evitar fugas de datos, es crucial minimizar la cantidad de información recopilada durante el proceso de autenticación.

### La seguridad informática: imperativos de prácticas seguras y riesgos relacionados con la negligencia humana

La seguridad informática puede verse comprometida por prácticas simples y el uso de contraseñas predeterminadas, como "admin". No siempre son necesarios ataques sofisticados para poner en peligro la seguridad informática. Por ejemplo, las contraseñas de administrador de un canal de YouTube estaban escritas en el código fuente privado de una empresa. Las vulnerabilidades de seguridad suelen ser consecuencia de la negligencia humana.

También es importante tener en cuenta que Internet está muy centralizado y ampliamente controlado por Estados Unidos. El servidor DNS puede estar sujeto a censura y a menudo utiliza DNS falsos para bloquear el acceso a ciertos sitios. DNS es un protocolo antiguo e insuficientemente seguro, lo que puede ocasionar problemas de seguridad. Han surgido nuevos protocolos, como DNSsec, pero aún se utilizan poco. Para evitar la censura y el bloqueo de anuncios, es posible elegir proveedores DNS alternativos.'
Des alternatives a los anuncios intrusivos incluyen Google DNS, OpenDNS y otros servicios independientes. El protocolo DNS estándar deja las consultas DNS visibles para el proveedor de servicios de Internet. DOH (DNS sobre HTTPS) y DOT (DNS sobre TLS) permiten cifrar la conexión DNS, ofreciendo mayor privacidad y seguridad. Estos protocolos son ampliamente utilizados en empresas debido a su seguridad reforzada y son nativamente compatibles con Windows, Android e iPhone. Para utilizar DOH y DOT, se debe ingresar un nombre de host TLS en lugar de una dirección IP. Los proveedores gratuitos de DOH y DOT están disponibles en línea. DOH y DOT mejoran la privacidad y la seguridad al evitar ataques de tipo "hombre en el medio". Otras consideraciones clave

En el marco del módulo de formación "Seguridad 101" de Découvre Bitcoin en la Academia, también discutimos la autenticación Lightning. Este sistema genera una identificación diferente por servicio, sin necesidad de proporcionar una dirección de correo electrónico o información personal. Es posible tener identidades descentralizadas controladas por el usuario, pero falta normalización y estandarización en los proyectos de identidad descentralizada. Se recomiendan los administradores de paquetes como Nuget y Chocolaté, que permiten descargar software de código abierto fuera de Microsoft Store, para evitar ataques maliciosos. En resumen, el DNS es crucial para la seguridad en línea, pero es necesario estar atento a posibles ataques a los servidores DNS.

# Remerciements et continuez à creuser le terrier du lapin

## Notez la formation & nous soutenir

Ce cours, ainsi que l'intégralité du contenu présent sur cette université, vous a été offert gratuitement par notre communauté. Pour nous soutenir, vous pouvez le partager autour de vous, devenir membre de l'université et même contribuer à son développement via GitHub. Au nom de toute l'équipe, merci !

Un système de notation pour la formation sera bientôt intégré à cette nouvelle plateforme de E-learning ! En attendant, merci beaucoup d'avoir suivi le cours et si vous l'avez apprécié, pensez à le partager autour de vous.

## allez plus loins

Félicitations pour avoir terminé cette formation SECU 101 ! J'espère de tout cœur qu'elle vous a plu et ouvert des portes. vous etes désormais prêt pour obtenir vos premiers bitcoins ou tout simplement continuer l'aventure avec les cours de niveau 2 !

- BTC 101 vous permettra d'avoir les bases théoriques sur Bitcoin
- BTC 102 vous aidera à mettre en place votre plan bitcoin
- LN 201 et 202 vous permettront de découvrir le Lightning Network, un réseau de paiements en seconde couche
- ECON 201 abordera l'économie autrichienne
- MINAGE 201 pour en savoir plus sur le minage
- (et bien d'autres)
  Un immense merci a nuestros Patreon, miembros y donantes por su apoyo financiero, gracias a las personas que comparten y gracias a aquellas que hicieron posible esta formación: Théo pantamis, Renaud, Théo, Fabien, Noury, Muriel y todo el equipo.
  ¡Hasta pronto!

---
name: Proton Authenticator
description: ¿Cómo puedo utilizar Proton Authenticator para proteger mis cuentas con 2FA?
---
![cover](assets/cover.webp)



La autenticación de dos factores (2FA) añade una barrera de seguridad adicional a tus cuentas al requerir, además de tu contraseña, una prueba adicional de que sólo tú la tienes. Activar el 2FA reduce drásticamente el riesgo de pirateo, incluso si su contraseña se ve comprometida a través de phishing o una filtración de datos. Sin 2FA, un atacante sólo necesitaría su contraseña para acceder a sus cuentas; con 2FA, también necesitaría su segundo factor, frustrando la mayoría de los intentos de robo de cuentas.



Existen varios tipos de 2FA. Los códigos SMS son mejores que nada, pero siguen siendo vulnerables a los ataques de intercambio de SIM y a la interceptación. No recomendamos los SMS como 2FA principal. Las aplicaciones de autenticación (TOTP) generate códigos temporales localmente en su dispositivo, haciéndolos mucho más difíciles de interceptar. Las claves de seguridad físicas ofrecen la mejor seguridad, pero requieren hardware dedicado.



Proton Authenticator es un autenticador TOTP. Es la respuesta de Proton a las limitaciones de las aplicaciones existentes: muchas son propietarias, contienen rastreadores de anuncios y no ofrecen copias de seguridad cifradas. Proton Authenticator se distingue por ofrecer una aplicación de código abierto, libre de anuncios y rastreadores, con copia de seguridad cifrada de extremo a extremo.



## Presentación de Proton Authenticator



Proton Authenticator es una aplicación de autenticación TOTP móvil y de escritorio desarrollada por Proton, famosa por sus servicios centrados en la privacidad. Como todos los productos de Proton, la aplicación es de código abierto y se ha sometido a auditorías de seguridad independientes. Está disponible de forma gratuita en todas las plataformas (Android, iOS, Windows, macOS, Linux).



Proton Authenticator ofrece las siguientes características clave:





- Generación de códigos **TOTP** para sus cuentas 2FA, compatible con la mayoría de los sitios que utilizan Google Authenticator, Authy, etc.





- **Copia de seguridad cifrada en la nube opcional**: puedes vincular la aplicación a tu cuenta Proton para realizar copias de seguridad y sincronizar tus códigos con cifrado de extremo a extremo. Si pierdes tu dispositivo, solo tienes que volver a conectar uno nuevo para restaurar todos tus códigos.





- **Sincronización multidispositivo**: al iniciar sesión en Proton en la app, tus códigos 2FA se sincronizan automáticamente entre varios dispositivos mediante cifrado de extremo a extremo. En iOS, una alternativa es la sincronización a través de iCloud.





- **Bloqueo local por contraseña o biométrico**: la aplicación ofrece bloqueo por PIN y/o huella dactilar/identificación facial. Así, aunque alguien acceda físicamente a tu teléfono desbloqueado, no podrá abrir Proton Authenticator.





- **Sin recopilación de datos ni rastreadores**: Protón se compromete a no recopilar datos personales a través de la aplicación. No hay publicidad oculta ni análisis de comportamiento.





- **Fácil importación/exportación**: uno de los puntos fuertes de Proton Authenticator es su asistente de importación de cuentas existentes, compatible con otras aplicaciones (Google Authenticator, Authy, Aegis, etc.). Si lo desea, también puede exportar sus códigos a un archivo.



En resumen, Proton Authenticator pretende ser una solución 2FA sin concesiones: segura, privada y flexible.



## Instalación



Proton Authenticator está disponible gratuitamente en todas las plataformas. Para descargar la aplicación, vaya a la página oficial: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Página oficial de Proton Authenticator en la que se muestran las principales características de la aplicación y Interface*



En esta página encontrará enlaces de descarga para todos los sistemas operativos: Android, iOS, Windows, macOS y Linux. Solo tienes que hacer clic en el sistema operativo que prefieras y seguir los pasos de instalación estándar.



En este tutorial, te mostraremos cómo instalarla y configurarla en macOS, y después veremos cómo instalar la app en iOS y sincronizar tus códigos entre ambos dispositivos.



### Instalación en macOS



Una vez descargada e instalada la aplicación, inicie Proton Authenticator. En el primer inicio, la aplicación le guiará a través de algunas pantallas de configuración inicial:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Pantalla de bienvenida de Proton Authenticator con el mensaje "Seguridad en cada código" y el botón "Comenzar "*



### Importación inicial



Si Proton Authenticator detecta que estaba utilizando previamente otra aplicación 2FA, puede aparecer un asistente de importación. Admite la importación directa desde ciertas aplicaciones (Google Authenticator, 2FAS, Authy, Aegis, etc.). Alternativamente, puede omitir este paso y añadir sus cuentas manualmente más tarde.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Asistente de importación para transferir códigos de otras aplicaciones de autenticación*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Aplicaciones de importación compatibles: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth y Google Authenticator*



### Protección de aplicaciones locales



Establece un PIN de desbloqueo, o activa el desbloqueo biométrico (Touch ID) si está disponible. Este paso es crucial para evitar que cualquiera que utilice tu Mac pueda acceder libremente a tus códigos 2FA.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Pantalla de configuración de Touch ID con el mensaje "Protege tus datos" y el botón "Activar Touch ID "*



### Opciones de sincronización



La aplicación también te permite activar la sincronización con iCloud para hacer copias de seguridad de tus datos de forma segura entre tus dispositivos Apple.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*Opción de sincronización de iCloud con el mensaje "Haz una copia de seguridad de tus datos de forma segura con la sincronización cifrada de iCloud "*



Una vez completados estos pasos, Proton Authenticator estará listo para su uso.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface main Proton Authenticator vacío con las opciones "Crear un nuevo código" e "Importar códigos "*



## Añadir una cuenta 2FA con ProtonMail



Ahora veremos cómo añadir tu primer código 2FA, usando ProtonMail como ejemplo. Este método funciona de forma idéntica para todos los servicios que admiten la autenticación de dos factores.



### Activar 2FA en ProtonMail



En primer lugar, puede consultar nuestra guía sobre ProtonMail para obtener más información:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Accede a tu cuenta de ProtonMail y ve a la configuración de seguridad. Busca la opción "Autenticación de dos factores" y actívala.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*Página de configuración de ProtonMail con la opción "Aplicación Authenticator" en la sección "Autenticación de dos factores "*



Haga clic en el botón para activar el autenticador y ProtonMail le pedirá que elija una aplicación de autenticación.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*Ventana de configuración de ProtonMail 2FA con los botones "Cancelar" y "Siguiente "*



ProtonMail mostrará entonces un código QR para que lo escanees con tu aplicación de autenticación.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*Código QR de ProtonMail para escanear con su aplicación de autenticación, con la opción "Introducir clave manualmente en su lugar" disponible*



Si prefieres introducir la clave manualmente, haz clic en "Introducir clave manualmente en su lugar" para ver la clave secreta.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Introducción manual de la información 2FA: Clave, Intervalo (30) y Dígitos (6)*



### Escanear el código QR con Proton Authenticator



En Proton Authenticator en macOS, haga clic en "Crear un nuevo código". La aplicación le ofrece varias opciones: **Escanear un código QR** o **Introducir la clave manualmente**.



Utiliza la cámara de tu Mac para escanear el código QR que aparece en la pantalla de ProtonMail. Una vez escaneado el código QR, accederás a la pantalla de configuración del nuevo código.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Nueva ventana de creación de entradas con los campos Título (ProtonMail), Secreto, Remitente (Proton), parámetros de dígitos e intervalo*



Proton Authenticator rellenará automáticamente la información. Puede personalizar el nombre si lo desea y, a continuación, haga clic en "Guardar".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*Código TOTP generado para ProtonMail (848 812) con indicación del tiempo restante*



### Validar la configuración



ProtonMail le pedirá que introduzca un código de 6 dígitos generado por Proton Authenticator para confirmar que la 2FA funciona correctamente.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*Pantalla de validación de ProtonMail en la que se le pide que introduzca el código de 6 dígitos (848812)*



Copie el código de la aplicación (haciendo clic en él) y péguelo en ProtonMail para completar la activación.



Una vez validado, ProtonMail te pedirá que descargues tus códigos de recuperación. Es vital que los guardes con cuidado.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*Pantalla de códigos de recuperación de ProtonMail con lista de códigos de rescate y botón "Descargar "*



### Códigos de emergencia



Cuando añada una cuenta, conserve los códigos de recuperación proporcionados por el servicio. La mayoría de los sitios ofrecen códigos de recuperación estáticos de un solo uso para guardar en un lugar seguro. Guarde estos códigos de recuperación fuera de Proton Authenticator para poder acceder a su cuenta si pierde el acceso a la aplicación 2FA.



## Instalación de IOS e importación de código



Ahora que has configurado Proton Authenticator en macOS, puede que también quieras usarlo en tu iPhone o iPad. Aquí te explicamos cómo obtener tus códigos 2FA en varios dispositivos.



### Descargar la aplicación en iOS



Vaya a la App Store y busque "Proton Authenticator". Descargue e instale la aplicación en su dispositivo iOS.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Proceso de instalación en iOS: pantalla de bienvenida, asistente de importación, selección de aplicaciones compatibles y pantalla final "Importar códigos desde Proton Authenticator "*



### Método 1: Exportar/Importar mediante archivo JSON



Si no utilizas la sincronización automática (iCloud o cuenta Proton), tendrás que transferir manualmente tus códigos del Mac al iPhone:



**Paso 1 - Exportar desde macOS** :



En su Mac, abra Proton Authenticator y vaya a Configuración (icono de engranaje). En el menú, haz clic en "Exportar".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Menú de configuración de Proton Authenticator en macOS con la opción "Exportar" visible*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Ventana de exportación con nombre de archivo "Proton_Authenticator_backup_2025" y botón "Guardar "*



Guarda el archivo JSON en tu Mac. Puedes enviarlo por correo electrónico seguro o guardarlo en iCloud Drive para acceder a él desde tu iPhone.



**Paso 2 - Importar en iOS** :



En su iPhone, instale Proton Authenticator y durante la configuración, elija importar códigos. Seleccione "Proton Authenticator" de la lista e importe el archivo JSON.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Proceso de importación en iOS: Localización de archivos JSON, confirmación de la importación y pantallas de configuración con Face ID y opciones de iCloud*



### Método 2: Sincronización automática



**Vía cuenta Proton (para sincronización multiplataforma)** :



Si aún no ha configurado una cuenta Proton y desea sincronizar entre diferentes sistemas operativos, la aplicación le pedirá que cree o conecte una cuenta Proton.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Pantalla de sincronización de dispositivos en la que se le pide que cree una cuenta gratuita de Proton o que se conecte a una cuenta existente*



**Vía iCloud (sólo para el ecosistema Apple)** :


Si solo utilizas dispositivos Apple, puedes elegir la sincronización con iCloud en los ajustes de la aplicación. Este método sincronizará tus códigos de forma automática y segura entre todos tus dispositivos Apple, sin necesidad de tener una cuenta Proton.



## Copia de seguridad y restauración cifradas



Una de las características clave de Proton Authenticator es su copia de seguridad de extremo a extremo de los códigos 2FA, lo que garantiza que una pérdida o cambio de dispositivo no signifique tener que empezar de nuevo.



### Cifrado de extremo a extremo



Cuando se trata de copias de seguridad cifradas en la nube con Proton Authenticator, tus secretos TOTP se cifran localmente en tu dispositivo antes de ser enviados al servidor de Proton. El descifrado sólo es posible por usted, en sus dispositivos conectados a su cuenta Proton. Proton AG no tiene la clave para leer sus códigos registrados.



En iOS, si optas por iCloud en lugar de la cuenta Proton, tus datos se cifran según los estándares de Apple. La copia de seguridad local en Android te permite cifrar el archivo de copia de seguridad con una contraseña de tu elección.



### Restauración en caso de siniestro



Si pierdes el teléfono, te lo roban o cambias de terminal :



**Con la copia de seguridad de Proton activada**: Instale Proton Authenticator en el nuevo dispositivo. Durante la configuración inicial, inicie sesión en la misma cuenta de Proton. Inmediatamente, la aplicación sincronizará y descargará todos tus códigos 2FA de la copia de seguridad cifrada.



**Con copia de seguridad de iCloud (iOS)**: Conecte el nuevo iPhone/iPad con el mismo ID de Apple y asegúrese de activar iCloud Keychain. Después de instalar Proton Authenticator, conéctese a iCloud. Tus códigos deberían sincronizarse a través de iCloud y aparecer.



**No hay copia de seguridad en la nube**: Tendrás que importar tus cuentas manualmente. Si había exportado un archivo de copia de seguridad, utilice la función Importar de Proton Authenticator. En el peor de los casos, si no tenía copia de seguridad, tendrá que utilizar los códigos de copia de seguridad para cada servicio, o ponerse en contacto con el soporte.



Proton Authenticator le permite exportar sus cuentas en cualquier momento, ya sea como un archivo cifrado o como un código QR multicuenta. Estas opciones le ofrecen una mayor seguridad.



## Buenas prácticas



El uso de un autenticador 2FA mejora enormemente su seguridad, pero deben observarse ciertas prácticas recomendadas:



### Guarda tus códigos de emergencia



Cuando activas 2FA en un servicio, a menudo te dan una lista de códigos de recuperación. Guárdalos fuera de tu teléfono (en papel, en un gestor de contraseñas cifrado, etc.). En caso de pérdida total de tu autenticador, estos códigos estáticos te salvarán.



### No confunda sus contraseñas y códigos 2FA



Es tentador utilizar un gestor de contraseñas que también almacene TOTPs. Sin embargo, mantener la contraseña y el código 2FA en el mismo lugar crea un único punto de fallo y debilita la doble autenticación. Para obtener la máxima seguridad, muchos expertos recomiendan separar los dos factores: las contraseñas en un gestor seguro y los códigos 2FA en una aplicación independiente como Proton Authenticator. Sin embargo, utilizar un gestor integrado sigue siendo mejor que no tener ningún 2FA.



### Activar varios métodos 2FA



Lo ideal es que utilices más de un segundo factor en tus cuentas críticas. No dude en añadir una clave de seguridad física si el servicio lo permite. Consulta nuestro tutorial sobre claves físicas Yubikey para más información:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Asimismo, tenga a mano códigos de emergencia impresos.



### Mantén la discreción y protege tu dispositivo



No deje que nadie registre su teléfono desbloqueado. Con Proton Authenticator, tus códigos están protegidos por PIN/biometría - no divulgues este PIN. Del mismo modo, ten cuidado con el phishing: incluso con 2FA, si das un código a un sitio fraudulento en tiempo real, podría ser utilizado por un atacante.



### Actualizaciones y auditorías



Mantener Proton Authenticator al día (las actualizaciones corrigen posibles fallos). Como el código es abierto, la comunidad realiza auditorías informales, y Proton publica los resultados de las auditorías formales.



## Comparación con otras aplicaciones



¿Cómo se compara Proton Authenticator con otras aplicaciones de autenticación? He aquí un resumen comparativo:



**Proton Authenticator**: Código abierto, copia de seguridad cifrada en la nube E2EE opcional, sincronización multidispositivo, bloqueo local, sin seguimiento, disponible en móvil y escritorio.



**Google Authenticator**: Propietario, copia de seguridad a través de la cuenta de Google desde 2023 pero sin cifrado de extremo a extremo (las claves pueden ser vistas por Google), sincronización multidispositivo añadida en 2023, sin bloqueo de aplicaciones por defecto, contiene rastreadores de Google.



**Aegis Authenticator**: Código abierto, solo copia de seguridad local, sin sincronización en la nube, bloqueo por código/biométrico, sin seguimiento, solo Android.



**Auténtico**: Propietario, copia de seguridad en la nube cifrada con contraseña pero de código cerrado, sincronización multidispositivo, bloqueo por PIN/huella dactilar, recoge el número de teléfono, aplicación de escritorio descatalogada en marzo de 2024.



A continuación encontrará nuestra guía sobre Authy:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator es una de las soluciones más completas y seguras disponibles: código abierto, sincronización encriptada multidispositivo, sin seguimiento comercial.



## Recursos y apoyo



### Documentación oficial




- **Sitio web oficial**: [proton.me/authenticator](https://proton.me/authenticator) - Presentación del producto y descargas
- **Página de descarga**: [proton.me/es/authenticator/download](https://proton.me/fr/authenticator/download) - Enlaces para todos los sistemas operativos
- **Soporte Proton**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Guía oficial de activación 2FA
- **Blog de Proton**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Anuncio y características detalladas



### Código fuente y transparencia




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Código fuente abierto
- **Auditorías de seguridad**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Informes de auditoría independientes



### Pruebas de seguridad recomendadas


Después de la configuración, pruebe su configuración:




- [Have I Been Pwned](https://haveibeenpwned.com/) - Comprueba si tus cuentas han sido comprometidas
- [2FA Directory](https://2fa.directory/) - Lista de servicios compatibles con 2FA



### Comunidades y debates




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Comunidad oficial Proton
- **Foro de Guías de Privacidad**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Debates técnicos sobre cuestiones de privacidad
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Consejos generales sobre privacidad



### Otros




- [Have I Been Pwned](https://haveibeenpwned.com/) - Comprueba si tus cuentas han sido comprometidas
- [2FA Directory](https://2fa.directory/) - Lista de servicios compatibles con 2FA
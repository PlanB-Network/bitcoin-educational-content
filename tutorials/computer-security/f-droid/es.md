---
name: F-Cold
description: Catálogo de aplicaciones gratuitas y de código abierto.
---

![cover](assets/cover.webp)



En la era digital, las grandes empresas e instituciones trabajan para centralizar Internet, poniendo su control en sus propias manos y obstaculizando así la privacidad y la libertad de todos los usuarios. Esto no es una utopía, ya está ocurriendo. Como bitcoiner, la descentralización, el respeto a la privacidad y las libertades individuales son principios que tienes muy en cuenta, especialmente en las herramientas que utilizas a diario. Android, a diferencia de iOS, ha permitido durante años la coexistencia de varias tiendas de aplicaciones dentro de su ecosistema, dándote la libertad de encontrar e instalar aplicaciones de tus fuentes favoritas.



En este tutorial, vamos a echar un vistazo a F-droid, un directorio de aplicaciones que representa una alternativa a las tiendas de aplicaciones como Google Play Store y Microsoft Store.



## Primeros pasos con F-Droid



F-Droid es una tienda de aplicaciones y herramientas que permite instalar aplicaciones gratuitas de código abierto en la plataforma Android. F-droid es un proyecto de código abierto iniciado en 2010 por Ciaran Gultnieks y otros colaboradores. El objetivo principal del proyecto es hacer accesibles las aplicaciones de código abierto y permitir que los iniciadores de proyectos de código abierto encuentren una plataforma donde publicar sus herramientas sin tener que recurrir a Google Play Store.



Por desgracia, F-Droid no es una aplicación disponible en iOS, y contiene muchas herramientas diseñadas para sistemas Android.



Puede descargar F-droid desde [el sitio web oficial](https://f-droid.org/) en formato APK e instalarlo manualmente en su teléfono Android.



![download](assets/fr/02.webp)



En Android, asegúrate de conceder permisos de instalación para el navegador desde el que descargaste F-Droid.



Una vez completada la instalación, F-Droid lanzará una actualización de los directorios de aplicaciones Open Source para enriquecer las aplicaciones de la tienda.



![repositories](assets/fr/03.webp)



Ahora puedes instalar aplicaciones en tu teléfono sin pasar por Google Play Store.



## La librería F-Droid



En la tienda de aplicaciones, encontrarás varias categorías de aplicaciones que se adaptan a tus necesidades. En la pestaña **Categorías**, encontrarás más de 20 tipos de aplicaciones, desde navegadores hasta editores de texto libre, y todas requieren la menor cantidad de información por tu parte.



¿Desea instalar una aplicación específica? Haga clic en el botón **Buscar** e introduzca el nombre de la aplicación que busca.



![search](assets/fr/04.webp)



F-Droid proporciona información completa sobre cada aplicación que desee instalar.



Al hacer clic en la aplicación, encontrará, entre otras cosas:




- Funciones y cambios añadidos en la última versión disponible
- Una descripción detallada de la aplicación, sus características, las razones para utilizarla y la comunidad de código abierto que hay detrás del proyecto.



![features](assets/fr/05.webp)





- La licencia utilizada por el proyecto, enlaces al código fuente y a los problemas encontrados al utilizar la aplicación
- Permisos requeridos por la aplicación



![permissions](assets/fr/06.webp)



Más información en nuestro tutorial sobre Thunderbird:



https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid te ofrece toda la información que necesitas para decidir si el uso de una aplicación protege tus datos y mejora tu privacidad. Analiza todas las aplicaciones que quieras utilizar y, a continuación, haz clic en el botón **Instalar** para descargar e instalar tu aplicación.


Conceda derechos de instalación a F-Droid activando la opción en su configuración.



![settings](assets/fr/07.webp)



## Exchange sus aplicaciones



F-Droid fomenta la práctica del código abierto y la contribución de la comunidad, especialmente a través de su opción **Near By** Exchange. Conéctate con los usuarios que te rodean a través de:




- Detección de Bluetooth;
- La misma red Wi-Fi;
- Código QR o IP:PORT Address para entrar en su navegador.



Con esta opción, puede compartir y recibir aplicaciones instaladas en su teléfono Android con amigos y familiares en unos pocos pasos.



![swap](assets/fr/08.webp)



## Actualizaciones



En la pestaña **Actualizar**, consulta la lista de actualizaciones disponibles, y asegúrate de leer también la información sobre las nuevas versiones de cada aplicación para enterarte de cualquier cambio importante en la versión que estás utilizando.



![updates](assets/fr/09.webp)



También puede actualizar la lista de aplicaciones disponibles actualizando la página (desplácese hacia abajo).



## Añada sus propias aplicaciones



F-Droid es un proyecto de código abierto que fomenta las contribuciones a aplicaciones que den prioridad a la privacidad del usuario. Puedes añadir tu propia aplicación móvil Android a la tienda mediante contribuciones al código fuente de F-Droid GitLab.



Su aplicación debe ser de código abierto, con el código fuente disponible públicamente en GitHub o GitLab, por ejemplo.


A continuación, debes preparar un archivo YAML (los metadatos) que describa tu aplicación, incluyendo toda la información y permisos necesarios para su uso, siguiendo la [plantilla de metadatos](https://f-droid.org/docs/Build_Metadata_Reference/) propuesta por F-Droid.



En la sección **Desarrolladores** de la [documentación](https://f-droid.org/en/docs/), encontrarás todos los recursos que necesitas para publicar y mantener tus aplicaciones en F-Droid.



### Integridad y seguridad



Poner una aplicación en código abierto suele ser sinónimo de mayor seguridad, pero también de un riesgo considerable. Cómo se puede garantizar que no haya alteraciones maliciosas en el código fuente de una aplicación disponible en F-Droid?



F-Droid compila las aplicaciones en sus propios servidores, basándose en el código fuente y las instrucciones de compilación oficiales. Cada aplicación publicada es reconstruida y verificada para asegurar que no ha sido comprometida. Esto garantiza que el APK ofrecido es fiel al código fuente publicado por los desarrolladores. Es más, cada aplicación instalada a través de F-Droid se firma digitalmente y, a continuación, la huella digital de la firma se compara con la anunciada por los desarrolladores de la aplicación en el sitio web oficial o en el repositorio Git.



Si te ha gustado este tutorial, infórmate sobre nuestro curso de seguridad informática y gestión de datos:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
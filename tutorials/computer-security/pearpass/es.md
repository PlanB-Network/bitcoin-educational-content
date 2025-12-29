---
name: PearPass
description: Recupere el control de sus contraseñas con un gestor de contraseñas local, de igual a igual y sin nube
---

![cover](assets/cover.webp)



En una época en la que cada individuo gestiona decenas, incluso centenares de cuentas en línea, la seguridad de los inicios de sesión se ha convertido en un tema central de la seguridad informática. Redes sociales, sistemas de mensajería, servicios profesionales, plataformas financieras: cada uno de estos accesos se basa en un secreto, cuyo compromiso puede tener graves consecuencias para su vida.



Y sin embargo, a pesar del creciente número de ataques, las malas prácticas siguen estando muy extendidas entre la población: contraseñas débiles, contraseñas reutilizadas, contraseñas almacenadas en texto claro o contraseñas aproximadamente memorizadas. Para resolver estos problemas sin complicarse la vida a diario, la solución es utilizar un gestor de contraseñas.



Ya existen decenas de gestores de contraseñas, y Plan ₿ Academy ofrece un tutorial para la mayoría de ellos. Pero en este tutorial, me gustaría presentarte uno que destaca claramente del resto en cuanto a su funcionamiento: **PearPass**.



**PearPass es un gestor de contraseñas peer-to-peer de código abierto, diseñado para ofrecer a los usuarios un control total sobre sus datos



![Image](assets/fr/01.webp)



## ¿Por qué elegir PearPass?



Un gestor de contraseñas es un programa informático que genera, almacena y organiza todas tus contraseñas de forma segura. En lugar de memorizar o reutilizar contraseñas, sólo tienes que proteger un secreto: la contraseña maestra, que encripta toda tu caja fuerte. Este enfoque permite utilizar contraseñas únicas, largas y aleatorias para cada servicio, lo que reduce tanto el riesgo de olvido como de compromiso, al tiempo que limita el impacto de cualquier posible filtración. Hoy en día, es una herramienta informática básica que todo el mundo debería utilizar.



Existen dos categorías principales de gestores de contraseñas. Por un lado, está el software solo local, muy seguro porque los datos nunca se almacenan en un servidor central, pero poco práctico, ya que no permite sincronizar fácilmente tus credenciales entre varios dispositivos (ordenador, smartphone, tableta...). Por otro lado, los gestores de contraseñas en la nube almacenan tus credenciales en sus servidores y las sincronizan entre todos tus dispositivos. Su principal ventaja es la comodidad, pero implican un compromiso en la seguridad, ya que tus contraseñas se almacenan en infraestructuras sobre las que no tienes control.



PearPass rompe deliberadamente con ambos modelos. Se posiciona entre los gestores locales y las soluciones en la nube: permite sincronizar tus contraseñas, al tiempo que garantiza que nunca se almacenan en servidores remotos. Como resultado, todas tus credenciales se almacenan localmente en tus dispositivos, y la sincronización entre múltiples máquinas es exclusivamente peer-to-peer. Esta arquitectura elimina los puntos únicos de fallo asociados a las bases de datos centralizadas: no hay servidores que comprometer ni infraestructuras de terceros que accedan a tus credenciales. Las comunicaciones entre tus dispositivos están cifradas de extremo a extremo, lo que garantiza que sólo las claves que posees permiten el acceso a los datos.



![Image](assets/fr/02.webp)



Para hacerlo posible, como su nombre indica, PearPass se basa en **Pears**, un ecosistema tecnológico peer-to-peer dedicado a la creación y ejecución de aplicaciones sin servidor. Pears proporciona el entorno de ejecución, los mecanismos de distribución y las capas de red necesarios para ejecutar aplicaciones totalmente descentralizadas, capaces de sincronizarse directamente entre pares, sin ninguna infraestructura central. En el caso de PearPass, Pears proporciona el descubrimiento de dispositivos, el establecimiento de conexiones cifradas y la sincronización de bóvedas de contraseñas entre sus máquinas. Este enfoque garantiza que PearPass siga siendo funcional, resistente e independiente de cualquier autoridad externa.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Más allá de esta arquitectura innovadora, PearPass es totalmente de código abierto, y todas sus funciones son gratuitas. El software también ha sido auditado de forma independiente por Secfault Security. Además de su arquitectura específica, PearPass ofrece, por supuesto, todas las funciones clásicas que se esperan de un buen gestor de contraseñas, y que descubriremos a lo largo de este tutorial.



En resumen, donde los gestores de contraseñas tradicionales te piden que confíes en una empresa y sus servidores, PearPass adopta una lógica de soberanía: sin nube, sin cuentas centralizadas, sin intermediarios. Conservas el control exclusivo sobre tus credenciales, al tiempo que te beneficias de la sincronización entre tus dispositivos.



## ¿Cómo se instala PearPass?



PearPass está disponible en todas las plataformas: Windows, Linux, macOS, Android, iOS y extensiones de navegador. No hay necesidad de instalar Pears en su máquina: PearPass funciona por sí solo.



### Instalación en Windows



En Windows, PearPass se suministra como un instalador clásico. Vaya a [la página oficial de descargas](https://pass.pears.com/download) y haga clic en el botón `Download Windows installer`.



Una vez descargado el archivo, abra el instalador y siga los pasos indicados por el asistente. A continuación, podrá acceder a la aplicación desde el `menú de inicio` o a través de un acceso directo en el escritorio.



![Image](assets/fr/03.webp)



### Instalación en macOS



En macOS, PearPass se distribuye como imagen de disco (`.dmg`). Vaya a [la página oficial de descargas](https://pass.pears.com/download) y elija la versión correspondiente a la arquitectura de su Mac (Intel o Apple Silicon). Tras la descarga, abra el archivo `.dmg` e inicie la aplicación desde la carpeta `Applications`.



Al iniciarse por primera vez, macOS mostrará un mensaje de seguridad indicando que la aplicación procede de Internet: basta con confirmar para continuar.



### Instalación en Linux



En Linux, PearPass está disponible en formato `.AppImage`, que garantiza una amplia compatibilidad con la mayoría de las distribuciones sin dependencias específicas. Descargue el archivo `.AppImage` de [la página oficial de descargas](https://pass.pears.com/download) y, a continuación, ejecútelo directamente haciendo doble clic.



Dependiendo de su entorno, puede que tenga que hacer que el archivo sea ejecutable a través de las propiedades del archivo (clic con el botón derecho) o con el comando `chmod +x`. Una vez autorizado, PearPass se inicia como una aplicación independiente.



### Instalación de extensiones del navegador



PearPass ofrece una extensión de navegador para el inicio de sesión automático y el acceso rápido a su caja fuerte mientras navega por la web. La extensión está disponible actualmente para Google Chrome y navegadores compatibles. Para instalarla, vaya a [la página oficial de descargas](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Una vez añadida, puede anclarla a la barra de herramientas para un acceso rápido. La activación de la extensión requiere un enlace con la aplicación PearPass instalada localmente en su ordenador (volveremos sobre esto más adelante en el tutorial).



### Instalación en iOS y Android



En iPhone y Android, sólo tienes que descargar la aplicación de tu tienda de aplicaciones:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Además de estos métodos clásicos de instalación, también es posible descargar el software directamente desde los repositorios de GitHub, para cada :




- [Escritorio](https://github.com/tetherto/pearpass-app-desktop);
- [Móvil](https://github.com/tetherto/pearpass-app-mobile);
- [Extensión del navegador](https://github.com/tetherto/pearpass-app-browser-extension).



Una vez instalado PearPass en una o más plataformas, puede pasar a la configuración inicial. En este tutorial, empezaremos configurando el software en el escritorio y, a continuación, lo sincronizaremos con la extensión del navegador y la aplicación móvil.



## ¿Cómo puedo crear una caja fuerte PearPass?



Cuando ejecutas PearPass por primera vez en tu ordenador, la aplicación te guía a través de dos pasos: establecer tu contraseña maestra y, a continuación, crear tu primera caja fuerte.



### Establecer contraseña maestra



Cuando la aplicación se inicia por primera vez en el escritorio, haga clic en el botón `Skip` y luego `Continue` para pasar por la pantalla de introducción y llegar a la etapa de configuración de la contraseña maestra.



![Image](assets/fr/06.webp)



A continuación viene el importante paso de elegir tu contraseña maestra. Como vimos en la introducción, esta contraseña es muy importante, ya que te da acceso a todas las demás contraseñas guardadas en el gestor. Técnicamente, se utiliza para obtener las claves criptográficas utilizadas para cifrar tus datos.



La contraseña maestra conlleva dos riesgos principales: pérdida y compromiso. Si pierdes el acceso a esta contraseña, ya no podrás acceder a tus datos de inicio de sesión. PearPass nunca guarda su contraseña maestra: **Si se pierde, sus datos de acceso se pierden permanentemente**. No existe ningún mecanismo de recuperación. Por el contrario, si esta contraseña se ve comprometida y un atacante consigue acceder a uno de tus dispositivos, podrá acceder a todas tus cuentas.



Para limitar el riesgo de pérdida, puedes hacer una copia de seguridad física de tu contraseña maestra, por ejemplo en papel, y guardarla en un lugar seguro. Lo ideal es sellar esta copia de seguridad en un sobre para poder comprobar periódicamente que no se ha accedido a ella. Por otro lado, nunca haga una copia de seguridad digital de esta contraseña.



Para reducir el riesgo de compromiso, tu contraseña maestra debe ser fuerte. Debe ser lo más larga posible, incluir una amplia variedad de caracteres y elegirse de forma realmente aleatoria. En 2025, las recomendaciones mínimas exigen al menos 13 caracteres, incluyendo mayúsculas y minúsculas, números y símbolos, siempre que la contraseña sea aleatoria. Sin embargo, yo recomendaría una contraseña de al menos 20 caracteres, si no más, con todo tipo de caracteres, para garantizar un nivel de seguridad más duradero.



Introduzca su contraseña maestra en el campo correspondiente, confírmela una segunda vez y pulse el botón `Continuar`.



![Image](assets/fr/07.webp)



A continuación, se le redirigirá a la pantalla de inicio de sesión: introduzca su contraseña maestra para comprobar que todo funciona correctamente.



![Image](assets/fr/08.webp)



### Cree su primera caja fuerte



Una vez que hayas iniciado sesión, PearPass te pedirá que crees tu primera caja fuerte. Una caja fuerte es un contenedor encriptado en el que se almacenan tus contraseñas, IDs, notas seguras y otra información. Cada caja fuerte está aislada y puede identificarse con un nombre distinto, lo que te permite organizar tus datos en función de tus usos (personal, profesional, proyectos específicos...).



Haga clic en el botón `Crear una nueva cámara acorazada`.



![Image](assets/fr/09.webp)



Elija un nombre para este almacén y haga clic de nuevo en "Crear un nuevo almacén" para finalizar la creación.



![Image](assets/fr/10.webp)



Su caja fuerte está inmediatamente lista para su uso. Puedes empezar a añadir contraseñas, inicios de sesión o notas seguras de inmediato.



![Image](assets/fr/11.webp)



## ¿Cómo añado un nombre de usuario a PearPass?



Una vez que hayas creado tu caja fuerte, puedes empezar a guardar tus artículos en ella. PearPass admite el registro de muchos tipos de artículos:




- iniciar sesión en un sitio o servicio ;
- identidad: su información personal para rellenar formularios rápidamente, pero también para almacenar documentos de identidad directamente en PearPass ;
- tarjeta de crédito: los números de su tarjeta de crédito para agilizar el pago al comprar en línea;
- Wi-Fi: contraseñas para sus redes Wi-Fi ;
- PassPhrase: frase secreta compuesta de varias palabras (advertencia: desaconsejo su uso para frases mnemotécnicas wallet Bitcoin);
- nota: crear notas seguras ;
- personalizado: esta función le permite crear un tipo de elemento personalizado, adaptado a sus necesidades específicas.



Comienza abriendo PearPass e inicia sesión con tu contraseña maestra.



![Image](assets/fr/12.webp)



Seleccione la caja fuerte en la que desea guardar este identificador.



![Image](assets/fr/13.webp)



En la página de inicio, haga clic en el botón para añadir un nuevo elemento, en función del tipo de información que desee registrar. En mi caso, quiero añadir un inicio de sesión para mi cuenta en el sitio web de Plan ₿ Academy: así que hago clic en el botón `Crear un inicio de sesión`.



![Image](assets/fr/14.webp)



Una vez que haya seleccionado el tipo de elemento que desea añadir, aparecerá un formulario que le permitirá introducir la información asociada al servicio en cuestión. En función de sus necesidades, puede introducir el nombre del servicio, el nombre de usuario, la contraseña y, si es necesario, la dirección del sitio web y notas adicionales.



PearPass también cuenta con un generador de contraseñas, que le permite crear una contraseña segura directamente desde el formulario. Para utilizarlo, haga clic en el icono que representa tres pequeños puntos en el campo `Contraseña`, elija la longitud deseada y, a continuación, haga clic en `Insertar contraseña`.



Una vez rellenados todos los campos, pulse el botón `Guardar` para guardar el identificador en la caja fuerte.



![Image](assets/fr/15.webp)



El identificador queda guardado. Aparece en la lista de elementos de la caja fuerte seleccionada y puede consultarse haciendo clic sobre él.



![Image](assets/fr/16.webp)



Puede modificar fácilmente un elemento haciendo clic en él y, a continuación, en el botón "Editar". También puede eliminarlo haciendo clic en los tres pequeños puntos de la parte superior derecha de la interfaz y, a continuación, en "Eliminar elemento".



![Image](assets/fr/22.webp)



En el móvil, la lógica sigue siendo la misma, aunque se ha adaptado la interfaz. Tras conectarse, seleccione la caja fuerte deseada, pulse el botón `+`, elija el tipo de artículo que desea crear y, a continuación, rellene la información necesaria.



![Image](assets/fr/17.webp)



## ¿Cómo organizar PearPass?



Como vimos en las secciones anteriores, PearPass le permite crear varias bóvedas distintas. Esto permite separar los distintos usos y constituye un primer nivel de organización para tu gestor de contraseñas. Desde la página de inicio, puedes cambiar fácilmente de un almacén a otro haciendo clic en la flecha situada en la parte superior izquierda de la interfaz.



![Image](assets/fr/18.webp)



Otra forma de organizar tus contraseñas, incluso dentro de un almacén, es crear carpetas. Para ello, en la columna izquierda de la interfaz, haz clic en el símbolo `+` junto a `Todas las carpetas` y, a continuación, introduce el nombre de la carpeta que deseas crear.



![Image](assets/fr/19.webp)



A continuación, puede almacenar los identificadores que desee, ya sea directamente al crear un elemento, o más tarde haciendo clic en `Editar`. Todo lo que tiene que hacer es seleccionar la carpeta deseada en la esquina superior izquierda del formulario.



![Image](assets/fr/20.webp)



Después de abrir un elemento, como un inicio de sesión, puede hacer clic en el icono de la estrella situado en la parte superior derecha de la interfaz para añadirlo a sus favoritos. Los favoritos pueden encontrarse rápidamente en una carpeta específica, además de su carpeta base.



![Image](assets/fr/21.webp)



Por último, hay una barra de búsqueda en la parte superior de la interfaz, para que puedas encontrar rápidamente el elemento que buscas, aunque tu bóveda contenga muchos identificadores.



## ¿Cómo sincronizo PearPass en mi móvil?



Ahora que tienes una bóveda de trabajo con elementos almacenados en tu ordenador, probablemente querrás acceder a tus contraseñas desde tu smartphone u otro dispositivo. PearPass te permite sincronizar tu gestor en múltiples máquinas de forma segura usando Pears. Averigüemos cómo.



Para empezar, en la máquina de origen (su ordenador, por ejemplo), inicie sesión en su almacén utilizando su contraseña maestra. Una vez en la página de inicio, haz clic en el botón "Añadir un dispositivo", situado en la parte inferior derecha de la interfaz.



![Image](assets/fr/23.webp)



PearPass genera entonces un enlace de invitación, también disponible como código QR, para sincronizar el almacén seleccionado en el dispositivo de su elección.



![Image](assets/fr/24.webp)



Si quieres sincronizar en tu dispositivo móvil, primero instala la aplicación y luego ejecútala. Se te pedirá que crees una contraseña maestra para el gestor de tu móvil. Puedes elegir entre utilizar la misma contraseña que en tu ordenador o una diferente. En todos los casos, sigue las mismas recomendaciones: una contraseña fuerte y aleatoria guardada en un soporte físico.



![Image](assets/fr/25.webp)



A continuación, si lo deseas, puedes activar la autenticación biométrica para evitar tener que introducir manualmente tu contraseña maestra cada vez que desbloquees el móvil.



![Image](assets/fr/26.webp)



Vuelva a introducir su contraseña maestra y haga clic en el botón `Continuar`.



![Image](assets/fr/27.webp)



Seleccione la opción "Cargar un almacén" y, a continuación, haga clic en "Escanear código QR" y escanee el código QR de la invitación que PearPass muestra en el equipo de origen (el ordenador).



![Image](assets/fr/28.webp)



Los bóvedas de tu ordenador y tu móvil están ahora sincronizados. Cada ID añadido en un dispositivo se almacenará de forma segura y se replicará en el otro.



![Image](assets/fr/29.webp)



En los teléfonos móviles, también puedes activar el rellenado automático de campos. Para ello, vaya a `Configuración > Avanzado` y, a continuación, haga clic en el botón `Configurar como predeterminado` de la sección `Relleno automático`.



![Image](assets/fr/30.webp)



## ¿Cómo sincronizo PearPass con la extensión del navegador?



Tener un gestor de contraseñas sincronizado entre el ordenador y el smartphone ya es muy práctico, pero integrarlo directamente en el navegador lo es aún más. Para ello, empieza por [añadir la extensión oficial de PearPass a tu navegador](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Desde el software PearPass instalado en su máquina local, vaya a `Configuración > Avanzado`, luego active la opción `Activar extensión del navegador`.



![Image](assets/fr/32.webp)



PearPass genera un archivo de emparejamiento token. Cópialo.



![Image](assets/fr/33.webp)



A continuación, abre la extensión PearPass en tu navegador, pega el emparejamiento token y haz clic en el botón `Verificar`, seguido de `Completar`.



![Image](assets/fr/34.webp)



Tu gestor de contraseñas ya está sincronizado con la extensión del navegador.



![Image](assets/fr/35.webp)



Ahora puedes utilizarlo para conectarte fácilmente a tus distintas cuentas web.



![Image](assets/fr/36.webp)



Ahora ya sabes cómo utilizar el gestor de contraseñas PearPass. Más allá de esta herramienta, la seguridad digital cotidiana depende del uso correcto de las soluciones adecuadas. Si quieres aprender a configurar un entorno digital personal seguro, estable y eficaz, te invito a descubrir nuestro curso de formación dedicado a este tema:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
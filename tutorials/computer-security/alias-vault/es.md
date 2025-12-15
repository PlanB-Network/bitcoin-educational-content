---
name: Alias Vault
description: Potente herramienta para gestionar contraseñas, autenticación de dos factores y alias (con servidor de correo electrónico integrado) - ¡También autoalojado!
---

![cover](assets/cover.webp)



La privacidad y la seguridad en línea es un tema al que cualquier persona, independientemente de su negocio, debe prestar mucha atención.



Además, estas cuestiones forman parte de un mundo en constante ebullición: cada vez son más los desarrolladores que participan en el tema, aportando implementaciones a soluciones ya establecidas y nuevos productos.



Este es el caso de **Leendert de Borst** y su `Alias Vault`, una herramienta revolucionaria (la primera de su clase) que permite gestionar y almacenar contraseñas, utilizar registros de contraseñas para autenticarse en servicios web, administrar autenticación de dos factores, pero sobre todo generate _aliases_ reales, todo en un único Interface.



**Pero Alias Vault no se detiene ahí**.



## Características principales



Alias Vault funciona en la nube en los servidores del desarrollador o autoalojado en su propia infraestructura, opción para la que se dispone de archivos Docker e imagen para instalar con un scipt. Además de la web Interface, hay disponibles extensiones para todos los navegadores populares, así como aplicaciones móviles para iOS y Android; estas últimas también pueden descargarse desde F-Droid, obviando la tienda oficial de Google.



En una Interface Alias Vault es:




- Gratuito y de código abierto**
- Gestor de contraseñas**, para almacenar todas las contraseñas complejas. Mediante la extensión del navegador, el gestor de contraseñas completa los inicios de sesión en sitios web
- 2FA**, para admitir la autenticación de dos factores
- Gestor de alias con servidor de correo electrónico integrado**: Alias Vault no crea alias que reenvíen el correo electrónico al buzón de un usuario, sino que crea alter-egos reales, completos con nombre, apellidos, sexo, nombre de usuario, contraseña y cumpleaños (si se requiere esta información).



El paquete incluye una extensa y exhaustiva documentación que acompañará a los recién llegados en el descubrimiento de esta potente herramienta.



## Sin datos personales



Comienza, como siempre, desde el sitio web [aliasvault.net](aliasvault.net). Como ya se ha mencionado, Alias Vault puede utilizarse en el propio servidor, o desde la nube del desarrollador para familiarizarse con él antes de pasar a la solución autoalojada.



El sitio tiene unos gráficos muy vistosos y cuidados, pero lo bueno viene cuando empiezas a meterle mano: **crea tu cuenta**.



![img](assets/en/01.webp)



Para tu enorme sorpresa, descubrirás que Alias Vault no pide información personal: todo lo que necesitas para crear la cuenta es cualquier apodo, una palabra que te resulte familiar, siempre que esté disponible. Acepta las condiciones del servicio, elige la palabra y continúa.



![img](assets/en/02.webp)



Establece ahora la **`contraseña maestra`**, que es el dato más importante de todo tu nuevo sistema. Con esta contraseña, de hecho, serás el único que pueda acceder/recuperar la cuenta, ya que mantendrá tu ``bóveda`` encriptada en el servidor que alojará tu información.



![img](assets/en/03.webp)



Hecho: Ha creado su propio gestor de contraseñas y su propio gestor de alias, pero sin dar su propio correo electrónico Address, que funciona y es privado.



![img](assets/en/04.webp)



Alias Vault te da la bienvenida a un espacio seguro, nuevo, personal pero también vacío. Y ahora empezamos a poblarlo un poco.



Si ya tienes un gestor de contraseñas, puedes importar el archivo del que estés utilizando, para evaluar las diferencias con otro proveedor, o quizás eliminar el gestor de alias para poder gestionarlo todo en una sola aplicación.



![img](assets/en/05.webp)



Alias Vault es extremadamente simple: tienes una página principal, que es el `Home`, con dos menús:




- credenciales": permite crear y gestionar identidades y alias
- `Email`: una bandeja de entrada en la que puede comprobar los mensajes entrantes de los alias que haya generado.



![img](assets/en/06.webp)



Lo que nos interesa es crear un primer `alias`, así que ve a la parte superior derecha de la página y haz clic en _+Nuevo Alias_.



![img](assets/en/07.webp)



Inicialmente, el menú tiene un aspecto mínimo, como corresponde a la filosofía de Alias Vault. Para descubrir las características de esta función, haga clic en _Crear a través del modo avanzado_.



![img](assets/en/08.webp)



La parte superior de la primera pantalla, puedes utilizarla para importar las credenciales de contraseña que ya utilizas para los servicios con los que estás suscrito, o que utilizas más a menudo en línea.



Si has habilitado la autenticación de dos factores en alguno (o todos) de los servicios anteriores, con Alias Vault también puedes gestionar este Layer adicional de seguridad importando la `clave secreta`. Alias Vault creará el `TOTP` necesario para el acceso.



![img](assets/en/09.webp)



**Precaución**: En el espacio reservado para el correo electrónico Address, Alias Vault propone su propio dominio por defecto; para poder utilizar el Address correcto con el que creó las cuentas anteriormente, haga clic en _Introducir dominio personalizado_, para poder establecer el dominio correcto después de `@`.



![img](assets/en/14.webp)



La parte inferior de esta pantalla es la más divertida. Haz clic en _Generar alias aleatorios_ y Alias Vault te creará identidades separadas para diferentes necesidades, cada una con su propio buzón de correo, contraseñas de nivel muy robusto, complementadas con otros detalles como sexo, fecha de nacimiento y un apodo adecuado.



![img](assets/en/10.webp)



Desde un menú apropiado, puedes cambiar los ajustes que afectan a la generación de contraseñas, como elegir sólo letras minúsculas y eliminar caracteres que puedan resultar ambiguos.



![img](assets/en/11.webp)



Puede utilizar el alias de correo electrónico sugerido por Alias Vault, o cambiar de dominio si hace clic en el menú desplegable correspondiente.



![img](assets/en/12.webp)



Antes de utilizar este correo electrónico para un servicio de inicio de sesión, puede probar su funcionalidad enviando un mensaje desde un Address propio al buzón recién creado.



![img](assets/en/13.webp)



**⚠️ ADVERTENCIA**: La recepción de correos electrónicos es posible gracias al servidor incorporado de Alias Vault, pero esto sólo permite recibir correos y no responder, o utilizar el buzón de correo electrónico con las funciones "convencionales" de un servicio de `alias`. Por lo tanto, difiere mucho de Simple Login, Addy y otras plataformas que se dedican exclusivamente a este tipo de servicio. Para el ejemplo de Simple Login puede ver el tutorial dedicado:



https://planb.academy/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Para eliminar un alias que ha creado como prueba, todo lo que tiene que hacer es entrar en su `Home`, luego `Credentials` y hacer clic en la identidad que desea eliminar. El comando _Borrar_ aparecerá en la esquina superior derecha para que procedas.



![img](assets/en/16.webp)



## Extensión del navegador



Dependiendo de cuáles sean sus necesidades, puede recurrir a la extensión del navegador, que puede encontrarse en los navegadores más utilizados.



![img](assets/en/15.webp)



Se instala como ya hiciste con el resto de extensiones, así que no me detendré en ese detalle.



La extensión del navegador está ahí para facilitar el inicio de sesión en servicios en línea, o para crear nuevos alias según sea necesario: si el servicio está almacenado entre sus registros de Alias Vault, el autorrelleno hace lo necesario.



![img](assets/en/17.webp)



La única precaución es comprobar que Alias Vault está activo. De hecho, la aplicación tiene una configuración predeterminada por la que se pausa tras un periodo de inactividad. Se trata de una función muy útil, **cuando tienes que alejarte del ordenador, por ejemplo, y evitar que otra persona acceda a tus cuentas**. Un procedimiento simplificado te permitirá conectarte de nuevo introduciendo la `contraseña maestra`, si la sesión anterior aún está en la caché. El tiempo de cierre de sesión es uno de los parámetros que puedes personalizar, acortándolo o alargándolo según tus preferencias.



## Aplicación móvil



Como todas las aplicaciones de este tipo que se precien, Alias Vault tiene una versión para dispositivos móviles, tanto en entorno Android como iOS. Para Android, puedes descargar la aplicación desde [F-Droid](https://f-droid.org/packages/net.aliasvault.app/).



En el momento de escribir este artículo (finales de agosto de 2025), la aplicación móvil considera el "rellenado automático" una función experimental, que no funciona excepto con muy pocos sitios. Hasta que esté totalmente implementada, el uso de Alias Vault en el móvil requiere copiar/pegar los datos.



Una vez descargada la aplicación de la tienda, para iniciar sesión basta con introducir el usuario y la `contraseña maestra` creados en la aplicación web.



![img](assets/en/18.webp)



Al abrir tu `bóveda`, se te preguntará si quieres activar el acceso controlado biométricamente, un Layer adicional de seguridad para evitar que otra persona acceda a tus contraseñas si resulta que tiene tu teléfono en la mano.



![img](assets/en/19.webp)



Si decides configurar la comprobación biométrica, adelante. Si te saltas el paso y cambias de opinión, también puedes configurarlo más adelante desde el menú _Configuración_.



Una vez que haya terminado de conectarse, encontrará los datos que ya ha creado sincronizados de nuevo.



![img](assets/en/20.webp)



La aplicación móvil puede dirigirse al enlace a la `bóveda` alojada en su propio servidor.



![img](assets/en/22.webp)



Y es precisamente la versión autoalojada la que Address, brevemente, en la siguiente sección.



## Autoalojamiento: control total sobre sus datos



Alias Vault, para ser justos, no es el primer `gestor de contraseñas` que te permite desplegar el servicio en tu infraestructura. Hay otros, pero algunos tienen limitaciones o son parcialmente de código cerrado.



La oportunidad es única: **acabar con la dependencia de proveedores de servicios externos o nubes, sino utilizar su propio servidor local para proteger y gestionar las contraseñas, los alias y la información extremadamente sensible asociada a todo ello**. Con Alias Vault también puede hacer que el servicio de correo electrónico apunte a su propio servidor de correo electrónico para una mayor confidencialidad.



Es hora de acudir a [documentación](https://docs.aliasvault.net/installation/), para saber cómo proceder para autoalojar Alias Vault.



![img](assets/en/23.webp)



Alias Vault se ejecuta en Docker Compose, por lo que se requiere una experiencia mínima con Linux y Docker. Puede empezar con la instalación básica y luego completarla con soluciones más avanzadas.



Su servidor debe funcionar en un equipo de 64 bits, con una distribución Linux, 1 GB de RAM y al menos 16 GB de almacenamiento; la versión de Docker (CE) debe ser al menos 20.10 o superior, mientras que Docker Compose requiere una versión a partir de 2.0.



Decidí probar Alias Vault con un cliente ligero, en el que DietPi está instalado como distribución, una base Debian Bookworm, optimizada a lo esencial y que ya ejecuta `Docker` y `Docker Compose`.



Primero, para tener un poco de orden, crea un directorio en tu home, abre el `terminal` y pega el comando para ejecutar el script de instalación.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Una vez finalizada la instalación, encontrarás tus credenciales de acceso:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Compruebe el contenido del directorio después de la instalación.



![img](assets/en/29.webp)



Para iniciar Alias Vault utilice el comando:



``` Lanzamiento-Alias-Bóveda


./install.sh inicio


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Consideraciones sobre encriptación y seguridad



![img](assets/en/32.webp)



De acuerdo con lo que Lanedirt afirma en el sitio, en la documentación y en Github, con Alias Vault **toda la información (componentes) que coloques en Alias Vault, permanecen fuertemente ligados al dispositivo, encriptados e inaccesibles para cualquiera que no conozca la `contraseña maestra`**.



La `contraseña maestra` es, por tanto, el elemento fundamental de toda la `bóveda`. Una vez introducida, se procesa con el algoritmo `Argon2id`, una función de derivación de claves de memoria Hard, para evitar que el secreto salga del dispositivo.



Todo permanece oculto incluso para el gestor de la nube o del servicio de hosting. De hecho, desde el panel de administración no se puede acceder a los datos de los usuarios, solo se puede saber si han creado alias, recibido correos y poco más.



Todos los contenidos almacenados se cifran y descifran mediante claves criptográficas derivadas de la `contraseña maestra`. **En el servidor sólo se almacenan datos cifrados, nada aparece en texto plano**. Si un usuario olvida o pierde su `contraseña maestra`, la cuenta vinculada a ella se pierde irreversiblemente, ya que el servidor no puede acceder a los contenidos en texto plano.



Para la versión autoalojada existe el script para restablecer la `contraseña maestra`, pero esto no evita la pérdida de datos.



![img](assets/en/33.webp)



Dado que Alias Vault se encuentra en fase _Beta_, es posible que tengas dificultades para acceder a él si cambias/actualizas la contraseña maestra. Te sugiero que la elijas robusta y compleja desde el principio para que puedas experimentar con el servicio y eventualmente decidir si lo usas. Si tienes dificultades para acceder a la nube tras la actualización de la contraseña, ponte en contacto con el servicio de asistencia de Alias Vault.



Para una comprensión completa de la arquitectura y la seguridad adoptadas por Alias Vault, le recomiendo encarecidamente que consulte [esta página](https://docs.aliasvault.net/architecture/), que contiene detalles de la criptografía subyacente a su funcionamiento.



## Mapa de carreteras


La intención de los desarrolladores es que Alias Vault esté maduro y sea estable para finales de 2025, con el fin de definir sus futuras características de uso.



Alias Vault es y seguirá siendo siempre de código abierto y gratuito, pero probablemente no de forma ilimitada como en la versión beta. Algunas funciones de pago están en proceso de implementación, como ya se ha anunciado.



Existen planes de equipo/familia y compatibilidad con claves de hardware, esta última para la autenticación con FIDO2 o WebAuth.



## ¿Quién necesita Alias Vault



**Una herramienta como ésta es ideal para cualquiera que dé prioridad a la privacidad en línea**.



Su identidad está, con toda probabilidad, en el centro de los negocios que realiza en línea y debe ser salvaguardada por todos los medios para poner **esos** datos lejos de servicios, empresas e intermediarios dispuestos a hacer cualquier cosa para poner sus manos en su comportamiento en línea.



Alias Vault te devuelve el control total sobre tus credenciales, mitigando o eliminando por completo la necesidad de depender de terceros para custodiar y cifrar tus datos más sensibles.



La arquitectura y la facilidad criptográfica de Alias Vault son ideales para particulares soberanos, pequeñas y medianas empresas, equipos de desarrollo y todos los entusiastas de las aplicaciones de **código abierto**. Si perteneces a alguna de estas categorías: diviértete descubriendo Alias Vault.
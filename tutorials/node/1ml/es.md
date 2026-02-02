---
name: 1ML
description: Aprenda a utilizar el explorador 1ML para comprender y analizar la red de rayos de Bitcoin.
---
![cover](assets/cover.webp)



## Introducción



Lightning Network es una solución de pago rápida y de bajo coste construida sobre Bitcoin, que permite realizar transacciones instantáneas y seguras. Observar esta red es esencial para entender cómo funciona, su topología y el estado de los nodos que la componen. Un explorador de Lightning, como 1ML, sirve para visualizar los datos públicos de la red, incluidos los nodos activos, los canales abiertos y la capacidad disponible, proporcionando una valiosa visión de conjunto a usuarios, desarrolladores y operadores de nodos.



## Acceda a 1ML y comprenda la página de inicio



Para acceder al 1ML, basta con abrir el navegador y escribir [https://1ml.com](https://1ml.com). Accederá a la página de inicio, que sirve de panel de control global de Lightning Network.



![capture](assets/fr/03.webp)



Esta página muestra varias estadísticas importantes en la parte superior de la pantalla, incluyendo :





- El **número total de nodos activos** en la red, es decir, los ordenadores que participan en el envío y la recepción de pagos de Rayo.
- El **número de canales abiertos**, que corresponden a las conexiones entre estos nodos que permiten transferencias de fondos.
- La **capacidad total de la red**, expresada en bitcoin (BTC), que indica la suma de las capacidades de todos los canales públicos.



Estas cifras se actualizan periódicamente para reflejar el estado actual de la red. Dan una idea de su tamaño, crecimiento y solidez.



![capture](assets/fr/04.webp)



Justo debajo, la página ofrece listas con clasificaciones:





- Los **nodos más conectados**, que tienen los canales más abiertos a otros nodos.
- Las **capacidades más altas** de los nodos, que indican qué nodos pueden transferir las mayores cantidades.
- Los canales más importantes en términos de capacidad.



También se pueden utilizar filtros para refinar estas listas por ubicación geográfica u otros criterios.



Esta página es un punto de partida ideal para explorar Lightning Network y comprender su topología general.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Exploración de los nodos Lightning



Para explorar un nodo en 1ML, comience por utilizar la barra de búsqueda situada en la parte superior de la página. Puede introducir el **ID del nodo**, es decir, su identificador único, o su **alias**, que es un nombre más fácil de recordar.



Una vez finalizada la búsqueda, haga clic en el nodo correspondiente para acceder a su página detallada.



![capture](assets/fr/07.webp)



En esta página se muestran varios datos importantes:





- ID del nodo**: este identificador único es una larga cadena de caracteres que permite identificar con precisión el nodo en toda la red.



![capture](assets/fr/08.webp)





- Alias**: es el nombre elegido por el propietario del nodo para representarlo públicamente.



![capture](assets/fr/09.webp)





- El **número de canales** indica cuántas conexiones tiene abiertas el nodo con otros nodos, mientras que la **capacidad total** representa la suma de bitcoins disponibles en estos canales. Un nodo con un gran número de canales y una alta capacidad está generalmente bien conectado y es capaz de transferir grandes cantidades de dinero rápidamente a través de la red.



![capture](assets/fr/10.webp)





- El **uptime**, o disponibilidad, mide el tiempo que un nodo ha permanecido activo y accesible en línea, reflejando su fiabilidad. La **edad** del nodo, por su parte, indica cuánto tiempo lleva presente en la red, reflejando su estabilidad y experiencia dentro de Lightning Network.



![capture](assets/fr/11.webp)



Estos datos ayudan a comprender la importancia y fiabilidad de un nodo en Lightning Network. Por ejemplo, un nodo con un gran número de canales, alta capacidad y elevado tiempo de actividad suele ser un actor importante en la red.



## Explorar los canales del rayo



### ¿Qué es un canal Rayo?



Un canal Lightning es una conexión directa entre dos nodos de la red. Permite a estos dos nodos intercambiar pagos instantáneos y de bajo coste sin pasar por la cadena principal de Bitcoin para cada transacción. Los canales son la base que hace que Lightning Network sea rápida y escalable.



### Leer información del canal en 1ML



En 1ML, cada canal tiene su propia página u hoja de descripción que contiene una serie de datos importantes:



Desde la página de un nodo, puede acceder a una lista de sus canales. Al hacer clic en un canal, 1ML muestra una página dedicada con varios datos clave.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Los principales datos visibles son los siguientes:





- Nodos asociados**: cada canal enlaza dos nodos. 1ML muestra ambos identificadores y sus respectivos alias.



![capture](assets/fr/14.webp)





- Capacidad del canal**: es la cantidad total de bitcoins bloqueados en este canal. Esta capacidad representa el límite máximo de pagos que pueden transitar por este canal.



![capture](assets/fr/15.webp)





- Antigüedad del canal**: indica cuánto tiempo lleva abierto el canal. Un canal antiguo suele ser señal de una relación estable entre dos nodos.



![capture](assets/fr/16.webp)



### Límites de visibilidad del canal



Es importante entender que 1ML sólo muestra **parte** de Lightning Network. El explorador sólo muestra los **canales públicos**, es decir, los que se han anunciado en la red. Los canales privados, a menudo utilizados por razones de confidencialidad o estrategia, no son visibles. Además, 1ML no muestra la distribución exacta de los fondos a cada lado de un canal, ni los pagos realizados, ni la liquidez realmente disponible en un momento dado. Por tanto, la información mostrada puede utilizarse para analizar la **estructura general de la red**, pero no su actividad financiera real ni el estado detallado de su liquidez.



## Explorar Lightning Network por ubicación



### Nodos por país y región



1ML le permite explorar Lightning Network según un **desglose geográfico**. Desde la página de inicio o a través de secciones específicas, es posible visualizar los nodos por país o región. Esta función se basa en la información de localización declarada por los operadores de los nodos.


En la barra de navegación, verá el enlace **Ubicación**. En la página, los nodos están agrupados por continente, país y ciudad.



![capture](assets/fr/17.webp)



Al seleccionar un país, 1ML muestra una lista de nodos asociados, junto con estadísticas agregadas como el número de nodos y la capacidad total visible para esa zona geográfica.



#### Qué dice esto sobre la adopción local





- Adopción de la tecnología**: Un gran número de nodos en una región indica que los usuarios, empresas o servicios de Bitcoin están adoptando Lightning Network de forma activa. Esto demuestra madurez tecnológica y voluntad de aprovechar las ventajas de Lightning (transacciones rápidas, menores costes).
- Ecosistema económico** : La densa presencia de nodos también puede señalar la existencia de un tejido económico local en torno a Bitcoin: comerciantes que aceptan Lightning, startups que desarrollan herramientas, eventos comunitarios, etc.
- Seguridad y resistencia**: La distribución geográfica diversa mejora la resistencia de la red ante cortes o restricciones locales. Cuanto más dispersos estén los nodos, más descentralizada y difícil de censurar será la red.
- Políticas y normativas**: Algunos países pueden ver una adopción más rápida gracias a un marco normativo favorable o a una comunidad proactiva. Por el contrario, en zonas donde la normativa es estricta u hostil, el número de nodos será menor.



#### Límites de los datos geográficos



Hay que tener en cuenta, sin embargo, que la geolocalización de los nodos Lightning tiene sus límites y sesgos:





- Ubicación IP aproximada**: 1ML utiliza generalmente la dirección IP pública de los nodos para estimar su ubicación. Sin embargo, este método puede verse distorsionado por el uso de VPN, servidores en la nube (AWS, Google Cloud) o alojamiento en países distintos del domicilio real del propietario del nodo.
- Nodos virtuales**: Algunos operadores alojan sus nodos en servidores remotos por razones de fiabilidad y disponibilidad, lo que puede dar una falsa sensación de ubicación física.
- Movilidad del usuario**: El operador de un nodo puede cambiar de ubicación, trasladar su infraestructura o abrir varios nodos en distintas regiones, lo que complica la lectura de datos.
- Invisibilidad de los nodos privados**: Algunos nodos no publican su dirección IP o utilizan métodos para ocultar su ubicación, lo que imposibilita la geolocalización.



## casos de uso concretos de 1ML



### Comprender la topología de la red



1ML permite visualizar la **estructura general de Lightning Network**. Observando las conexiones entre nodos, el número de canales y la capacidad global, es posible entender cómo está organizada la red, qué nodos desempeñan un papel central y cómo pueden circular teóricamente los flujos de pago.



Esta comprensión es esencial si queremos entender cómo funciona la Lightning Network, y no sólo para el uso de la cartera.



### Identificar los nodos importantes



Gracias a las clasificaciones que ofrece 1ML (nodos más conectados, mayor capacidad, antigüedad), es posible identificar los nodos que ocupan un lugar importante en la red. Estos nodos suelen servir de pasarelas importantes para los pagos Lightning.



![capture](assets/fr/18.webp)



### Comprobar la visibilidad pública de un nodo



Para un operador de nodos, 1ML le permite comprobar si su nodo está **anunciado públicamente** en Lightning Network. Si un nodo aparece en 1ML, significa que es visible y accesible a otros nodos para abrir canales públicos.


Esto puede ser útil para diagnosticar problemas de visibilidad o conectividad.



### Observar la evolución de Lightning Network



Al comparar las estadísticas globales de distintos periodos, 1ML permite observar la evolución de Lightning Network: aumento o disminución del número de nodos, variaciones de la capacidad total o cambios en la distribución geográfica.


Estas observaciones ofrecen una perspectiva interesante sobre el crecimiento, la madurez y las tendencias de la Lightning Network.



## mejores prácticas y limitaciones de 1ML



### Datos públicos ≠ realidad completa



1ML se basa únicamente en los datos **anunciados públicamente** sobre Lightning Network. Esto significa que la herramienta sólo muestra una parte de la realidad. Muchos canales pueden ser privados, algunos nodos pueden no estar anunciados y la liquidez real disponible en los canales no es visible. Por tanto, es fundamental utilizar 1ML como herramienta de análisis global, no como representación exhaustiva de la red.



### Privacidad y rayos



Lightning Network se ha diseñado prestando especial atención a la **privacidad de los pagos**. Las transacciones individuales no son visibles en 1ML, y los saldos exactos de los canales no son públicos. Esta limitación no es culpa del explorador, sino una característica fundamental de Lightning Network, diseñada para proteger la privacidad de los usuarios.



### No saque conclusiones precipitadas



Un nodo con gran capacidad o muchos canales no es necesariamente más "fiable" o "eficiente" en todos los casos. Del mismo modo, un descenso temporal de la capacidad global de la red no significa necesariamente un problema estructural. Las cifras siempre deben interpretarse retrospectivamente y ponerse en contexto.



### Complementariedad con otras herramientas



1ML es un excelente punto de partida para explorar Lightning Network, pero es mejor utilizarlo junto con otras herramientas, como las carteras Lightning, las interfaces de gestión de nodos y otros exploradores. Este enfoque proporciona una visión más completa y matizada de la red.



## opción de conexión 1ML (funcionalidad avanzada)



1ML ofrece la opción de **conectarse / crear una cuenta**, visible en el sitio, pero esto **no es necesario** para ver los datos de Lightning Network. Todas las funciones descritas hasta ahora en este tutorial están disponibles **sin cuenta**.



La conexión está destinada principalmente a los **operadores de nodos Lightning**. En concreto, permite asociar un nodo a una cuenta 1ML para gestionar cierta información pública, como la presentación del nodo, los enlaces de contacto y otros metadatos. Esta función tiene por objeto mejorar la visibilidad e identificación de un nodo dentro del explorador.



Es importante tener en cuenta que 1ML **no es un servicio de custodia**. La creación de una cuenta no da acceso a los fondos, canales o pagos de un nodo. Sólo sirve para interactuar con el explorador desde un punto de vista declarativo e informativo.



Por lo tanto, en el contexto del aprendizaje o del descubrimiento del Lightning Network, esta opción puede considerarse **opcional** y reservarse para un uso más avanzado.



## Conclusión



1ML es una valiosa herramienta para observar y comprender Lightning Network a partir de sus datos públicos. Permite explorar la estructura de la red, analizar nodos y canales y seguir la evolución general de la adopción de Lightning Network a lo largo del tiempo. Sin necesidad de una cuenta ni de manejar fondos, 1ML ofrece una pasarela accesible para cualquiera que desee profundizar en el conocimiento del funcionamiento de Lightning.


Si quieres ir más allá con el Lightning Network, te recomiendo el curso completo de Introducción al Lightning Network:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
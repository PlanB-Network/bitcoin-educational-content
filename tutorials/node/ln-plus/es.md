---
name: Lightning Network+
description: Obtenga liquidez entrante gratuita con aperturas cooperativas en su nodo Lightning
---

![cover](assets/cover.webp)



## Introducción



[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/) es una plataforma comunitaria diseñada para facilitar la cooperación entre los operadores de nodos Lightning Network. Su principal objetivo es mejorar la conectividad, liquidez y descentralización de la red Lightning, sin necesidad de intermediarios centralizados.



Este tutorial se centrará en el servicio **"Swaps "**, que es la característica más utilizada y estructurante de LN+ en la actualidad. También se presentarán los demás servicios que ofrece la plataforma.



## Visión general de LN



### ¿Qué es Lightning Network Plus?



Lightning Network Plus (LN+) es una plataforma comunitaria para operadores de nodos Lightning que deseen cooperar directa y voluntariamente. Su objetivo es facilitar la creación de canales Lightning útiles, equilibrados y sostenibles, evitando al mismo tiempo la necesidad de soluciones centralizadas o concentradores impuestos.



LN+ se basa en un principio fundamental: la cooperación entre iguales, basada en la transparencia, la reciprocidad y la reputación.



### Los servicios de LN



LN+ ofrece varios servicios diseñados para mejorar la topología y la liquidez de la red Lightning, entre ellos :





- Swaps**: apertura recíproca de canales entre operadores (servicio principal).
- Anillos**: aberturas circulares en forma de canal entre varios participantes.
- Swaps basados en la confianza**: variantes que se basan más en la confianza y el historial de los participantes.
- Funciones sociales**: perfiles, comentarios y sistema de reputación.



En el resto de este tutorial, nos centraremos exclusivamente en el servicio **Swaps**, que es el núcleo del uso actual de LN+.



## LN+ Servicio "Swaps



### Definición de un swap LN



Un **swap** de LN+ es un acuerdo voluntario entre dos operadores de nodos Lightning para abrir mutuamente canales Lightning de capacidad equivalente (o preacordada). A diferencia de la apertura unilateral de un canal convencional, el intercambio se basa en la **reciprocidad explícita**.



En la práctica :





- Abres un canal hacia el nodo de tu socio.
- Su socio abre un canal hacia su nodo.
- Ambas partes están inmovilizando una cantidad similar de bitcoins on-chain.



### ¿Para qué sirven los swaps a los operadores de nodos?



El servicio Swaps aborda varios problemas clave a los que se enfrentan los operadores de rayos:





- Conectividad mejorada**: creación de canales bidireccionales útiles en cuanto se abren.
- Mejor gestión de la liquidez**: cada parte tiene capacidad de entrada y de salida.
- Reducción del riesgo de canales innecesarios**: se anima al socio a mantener el canal abierto.
- Mayor descentralización**: conexiones directas entre operadores, sin nodos impuestos.



### ¿Para qué perfiles de nodos son útiles los intercambios?



Los swaps son especialmente útiles para :





- Nuevos nodos que desean mejorar rápidamente su capacidad de enrutamiento.
- Operadores intermediarios que buscan aumentar la densidad de su gráfico de canales.
- Nodos orientados al enrutamiento que desean optimizar su topología.



## Conecta tu nodo Lightning a LN+



### Requisitos técnicos



Antes de empezar, necesitará :





- Un nodo Lightning en funcionamiento (LND, Core Lightning o Eclair).
- Acceso a la interfaz de gestión de tu nodo.
- Suficiente capacidad on-chain para abrir canales.



Acceda al sitio web de [Lightning Network](https://lightningnetwork.plus/) Plus y haga clic en el botón `Login` situado en la parte superior derecha de la interfaz.



![capture](assets/fr/03.webp)



### Autenticación por firma de mensaje



Para autenticarse, debe firmar el mensaje proporcionado utilizando la clave privada de su nodo Lightning. Con ThunderHub, esta operación es muy sencilla.



Comience copiando el mensaje mostrado por LN+.



![capture](assets/fr/04.webp)



En ThunderHub, ve a la pestaña `Herramientas` y pulsa el botón `Firmar` de la sección `Mensajes`.



![capture](assets/fr/05.webp)



Pegue el mensaje de autenticación proporcionado por LN+ y, a continuación, haga clic en `Firmar`.



![capture](assets/fr/06.webp)



A continuación, ThunderHub firma este mensaje utilizando la clave privada de tu nodo. Copie la firma generada.



![capture](assets/fr/07.webp)



Pegue esta firma en el campo correspondiente del sitio LN+ y, a continuación, haga clic en `Iniciar sesión`.



![capture](assets/fr/08.webp)



Ahora está conectado a LN+ con su nodo Lightning. Este proceso permite a LN+ verificar que eres el propietario legítimo del nodo que reclamas en su plataforma.



![capture](assets/fr/09.webp)



Si lo desea, puede personalizar su perfil LN+, por ejemplo añadiendo una breve biografía.



## Participar en un swap existente



### Acceso a ofertas de canje



Para participar en tu primera apertura de canal, ve al menú `Swaps` en la parte superior de la interfaz. Aquí encontrarás todos los intercambios disponibles en función de las características de tu nodo.



![capture](assets/fr/10.webp)



### Condiciones de admisibilidad



Para unirse a una oferta de intercambio existente, basta con seleccionar el anuncio correspondiente y registrarse. Sin embargo, LN+ permite al creador del swap definir ciertas **condiciones de elegibilidad**, como :





- un número mínimo de canales ya abiertos ;
- capacidad total mínima de los nodos ;
- determinados tipos de conexión aceptados.



### Nodos recientes



Como resultado, especialmente en las primeras etapas de uso, es posible que **pocas o ninguna oferta estén disponibles** para su nodo. Esta situación es habitual en los nodos nuevos o que aún no se han conectado.



En mi caso, a pesar de la existencia de algunos canales abiertos, ninguna de las ofertas cumplía los criterios exigidos.



## Cree su propia oferta de intercambio



### ¿Cuándo debe crear su propio canje?



Cuando no hay ninguna oferta disponible, crear su propio canje suele ser la mejor solución. Además, le permite mantener el control sobre los parámetros del canje.



### Configuración de intercambio



Haga clic en **Iniciar Liquidity Swap** y, a continuación, configure los parámetros de su oferta:





- seleccione el número total de participantes (3, 4 o 5);
- indican la capacidad de los canales que se van a abrir;
- definir el periodo de compromiso durante el cual los participantes se comprometen a no cerrar sus canales;
- especificar cualquier restricción aplicable a los participantes (número mínimo de canales, capacidad total mínima, tipo de conexión aceptada).



![capture](assets/fr/11.webp)



### Publicación y expectativas de los participantes



Una vez introducidos todos los parámetros, haga clic en **Iniciar Liquidity Swap** para publicar su oferta. Ahora solo tienes que esperar a que otros operadores se inscriban.



![capture](assets/fr/12.webp)



## Finalizar un canje



### Apertura efectiva del canal



Ahora que se han tomado todas las posiciones de intercambio, cada participante puede ver, desde su interfaz LN+, a qué nodo tiene que abrir un canal Lightning.



![capture](assets/fr/13.webp)



Por tu parte, abre el canal utilizando el ID de nodo proporcionado por LN+ y respetando la cantidad indicada. Esta operación puede realizarse a través de ThunderHub, otro gestor de nodos Lightning o directamente a través de la interfaz básica de tu nodo.



![capture](assets/fr/14.webp)



Una vez abierto, el canal aparece en la sección de canales en espera.



![capture](assets/fr/15.webp)



### Confirmación en LN+



A continuación, vuelva a LN+ para confirmar que ha iniciado la apertura de canales, pulsando el botón `Apertura de canales iniciada`.



![capture](assets/fr/16.webp)



### Fin de la permuta



Cuando todos los participantes han abierto los canales a los que se han comprometido, el canje se considera completado.



## Reputación y buenas prácticas de comunicación



### El sistema de reputación LN



LN+ incorpora un sistema de reputación basado en las opiniones que dejan los participantes al final de los swaps. Estas opiniones son públicas e influyen directamente en la capacidad de un operador para unirse o crear futuros swaps.



![capture](assets/fr/17.webp)



### Buenas prácticas recomendadas



Para preservar una buena reputación y garantizar el buen funcionamiento de los intercambios, se recomienda :





- respetar los plazos de apertura de los canales ;
- comunicarse rápidamente en caso de problema o retraso;
- utilice la sección de comentarios para intercambiar opiniones con otros participantes;
- no cerrar un canal antes de que finalice el periodo de compromiso.




![capture](assets/fr/18.webp)



### Por qué la reputación es fundamental para LN



LN+ se basa en un modelo de cooperación voluntaria, sin fuertes restricciones técnicas. La reputación es, por tanto, el principal incentivo para garantizar la fiabilidad y confianza de los participantes.



## Otros servicios LN



Además de los Swaps, LN+ ofrece otros servicios diseñados para mejorar la conectividad y la coordinación entre los operadores de nodos Lightning. Los anillos** permiten a varios participantes crear un bucle de aperturas de canales, reforzando así la redundancia de las rutas de encaminamiento y la densidad del grafo Lightning. Los swaps basados en la confianza** se basan en principios similares a los swaps clásicos, pero ofrecen mayor flexibilidad a los participantes que ya tienen una reputación establecida en la plataforma.



LN+ también integra funciones sociales como perfiles de nodos públicos, comentarios de intercambio y un sistema de reputación. Estas herramientas no son servicios técnicos propiamente dichos, pero desempeñan un papel central en el buen funcionamiento de la plataforma, facilitando la comunicación, la coordinación y la confianza entre los operadores.



## Conclusión



El servicio Swaps de LN+ es una herramienta eficaz para mejorar la conectividad, la liquidez y la descentralización en la red Lightning. Al promover aperturas de canales recíprocas y coordinadas, LN+ permite a los operadores de nodos reforzar su topología, al tiempo que fomenta una cooperación responsable y descentralizada.
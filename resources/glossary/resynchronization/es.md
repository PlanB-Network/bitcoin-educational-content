---
term: RESYNCHRONIZATION
---

Se refiere a un fenómeno en el cual la blockchain experimenta una modificación de su estructura debido a la existencia de bloques competidores a la misma altura. Esto ocurre cuando una porción de la blockchain es reemplazada por otra cadena con una mayor cantidad de trabajo acumulado.

Estas resincronizaciones son parte del funcionamiento natural de Bitcoin, donde diferentes mineros pueden encontrar nuevos bloques casi simultáneamente, dividiendo así la red de Bitcoin en dos. En tales casos, la red puede dividirse temporalmente en cadenas competidoras. Eventualmente, cuando una de estas cadenas acumula más trabajo, las otras cadenas son abandonadas por los nodos, y sus bloques se convierten en lo que se llama "bloques obsoletos" o "bloques huérfanos". Este proceso de reemplazar una cadena por otra es la resincronización.

![](../../dictionnaire/assets/9.png)

Las resincronizaciones pueden tener varias consecuencias. Primero, si un usuario tenía una transacción confirmada en un bloque que resulta ser abandonado, pero esta transacción no se encuentra en la cadena válida finalmente, entonces su transacción se vuelve no confirmada de nuevo. Es por esto que se aconseja esperar siempre al menos 6 confirmaciones para considerar una transacción como verdaderamente inmutable. Después de 6 bloques de profundidad, las resincronizaciones son tan improbables que la posibilidad de que ocurra una se puede considerar prácticamente nula.

Además, a nivel del sistema global, las resincronizaciones implican un desperdicio del poder computacional de los mineros. De hecho, cuando ocurre una división, algunos mineros estarán en la cadena `A`, y otros en la cadena `B`. Si la cadena `B` es eventualmente abandonada durante una resincronización, entonces todo el poder computacional desplegado por los mineros en esta cadena se desperdicia, por definición. Si hay demasiadas resincronizaciones en la red de Bitcoin, la seguridad general de la red se reduce por lo tanto. Esto es en parte por qué aumentar el tamaño del bloque o reducir el intervalo entre cada bloque (10 minutos) puede ser peligroso.

> ► *Algunos bitcoiners prefieren usar "bloque huérfano" para referirse a un bloque expirado. Además, aunque es un anglicismo, en el lenguaje común, una "reorganización" o un "reorg" a menudo se prefiere sobre "resincronización".*
---
term: REORGANIZACIÓN
---

Se refiere a un fenómeno en el cual la blockchain sufre una modificación de su estructura debido a la existencia de bloques competidores a la misma altura. Esto ocurre cuando una parte de la blockchain es reemplazada por otra cadena que tiene una mayor cantidad de trabajo acumulado.

Estas reorganizaciones son parte del funcionamiento natural de Bitcoin, donde diferentes mineros pueden encontrar nuevos bloques casi simultáneamente, dividiendo así la red de Bitcoin en dos. En tales casos, la red puede dividirse temporalmente en cadenas competidoras. Eventualmente, cuando una de estas cadenas acumula más trabajo, las otras cadenas son abandonadas por los nodos, y sus bloques se convierten en lo que se llama "bloques obsoletos" o "bloques huérfanos". Este proceso de reemplazar una cadena por otra es la reorganización.

![](../../dictionnaire/assets/9.png)

Las reorganizaciones pueden tener varias consecuencias. Primero, si un usuario tenía una transacción confirmada en un bloque que resulta ser abandonado, pero esta transacción no aparece en la cadena válida finalmente, entonces su transacción se vuelve no confirmada de nuevo. Es por esto que se aconseja esperar siempre al menos 6 confirmaciones para considerar una transacción como verdaderamente inmutable. Después de 6 bloques de profundidad, las reorganizaciones son tan improbables que la posibilidad de que ocurra una se puede considerar prácticamente nula.

Además, a nivel del sistema global, las reorganizaciones implican un desperdicio del poder computacional de los mineros. De hecho, cuando ocurre una división, algunos mineros estarán en la cadena `A`, y otros en la cadena `B`. Si la cadena `B` es eventualmente abandonada durante una reorganización, entonces todo el poder computacional desplegado por los mineros en esta cadena se desperdicia, por definición. Si hay demasiadas reorganizaciones en la red de Bitcoin, la seguridad general de la misma se reduce. Esto es en parte por qué aumentar el tamaño del bloque o reducir el intervalo entre cada bloque (10 minutos) puede ser peligroso.

> ► *Algunos bitcoiners prefieren usar "bloque huérfano" para referirse a un bloque expirado. Además, en el lenguaje común, un "reorg" se usa para referirse a una "reorganización". El término "reorganización" es un anglicismo. Para ser más precisos, uno podría hablar de una "resincronización".*
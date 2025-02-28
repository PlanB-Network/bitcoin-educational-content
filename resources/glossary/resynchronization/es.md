---
term: RESINCRONIZACIÓN

---
Se refiere a un fenómeno en el que la blockchain sufre una modificación de su estructura debido a la existencia de bloques en competencia a la misma altura. Esto ocurre cuando una parte de la blockchain es sustituida por otra cadena con una mayor cantidad de trabajo acumulado.

Estas resincronizaciones forman parte del funcionamiento natural de Bitcoin, donde diferentes mineros pueden encontrar nuevos bloques casi simultáneamente, dividiendo así la red Bitcoin en dos. En tales casos, la red puede dividirse temporalmente en cadenas competidoras. Eventualmente, cuando una de estas cadenas acumula más trabajo, las otras cadenas son abandonadas por los nodos, y sus bloques se convierten en lo que se denomina "bloques obsoletos" o "bloques huérfanos" Este proceso de sustitución de una cadena por otra es la resincronización.

![](../../dictionnaire/assets/9.webp)

Las resincronizaciones pueden tener varias consecuencias. En primer lugar, si un usuario tenía una transacción confirmada en un bloque que resulta estar abandonado, pero esta transacción no se encuentra en la cadena válida en última instancia, entonces su transacción vuelve a estar sin confirmar. Por eso se aconseja esperar siempre al menos 6 confirmaciones para considerar que una transacción es realmente inmutable. Después de 6 bloques de profundidad, las resincronizaciones son tan improbables que la posibilidad de que ocurra una puede considerarse prácticamente nula.

Además, a nivel del sistema global, las resincronizaciones implican un desperdicio de la potencia de cálculo de los mineros. En efecto, cuando se produce una división, algunos mineros estarán en la cadena `A` y otros en la cadena `B`. Si la cadena `B` se abandona finalmente durante una resincronización, toda la potencia de cálculo desplegada por los mineros en esta cadena se desperdicia, por definición. Si hay demasiadas resincronizaciones en la red Bitcoin, la seguridad general de la red se reduce. Esta es en parte la razón por la que aumentar el tamaño de los bloques o reducir el intervalo entre cada bloque (10 minutos) puede ser peligroso.

> ► *Algunos bitcoiners prefieren utilizar "bloque huérfano" para referirse a un bloque caducado. Además, aunque se trata de un anglicismo, en el lenguaje común se suele preferir "reorganización" o "reorg" a "resincronización "*
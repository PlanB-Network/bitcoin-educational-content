---
term: OBSOLETO (BLOQUE)
---

Se refiere a un bloque sin hijos: un bloque válido, pero excluido de la cadena principal de Bitcoin. Ocurre cuando dos mineros encuentran un bloque válido en la misma altura de cadena dentro de un corto período de tiempo y lo transmiten a través de la red. Los nodos eventualmente eligen solo un bloque para incluir en la cadena, de acuerdo con el principio de la cadena con el trabajo acumulado más grande, dejando el otro como "obsoleto". El proceso que lleva a la producción de un bloque obsoleto es el siguiente:
* Dos mineros encuentran un bloque válido en la misma altura de cadena dentro de un corto intervalo de tiempo. Llamémoslos `Bloque A` y `Bloque B`;
* Cada uno transmite su bloque a la red de nodos de Bitcoin. Cada nodo ahora tiene 2 bloques a la misma altura. Por lo tanto, hay dos cadenas válidas;
* Los mineros continúan buscando pruebas de trabajo para los siguientes bloques, pero para hacerlo, necesariamente deben elegir solo un bloque entre `Bloque A` y `Bloque B` en el cual minarán;
* Un minero eventualmente encuentra un bloque válido encima de `Bloque B`. Llamémoslo `Bloque B+1`;
* Transmiten `Bloque B+1` a los nodos de la red;
* Dado que los nodos siguen la cadena más larga (con el trabajo acumulado más grande), estimarán que la `Cadena B` es la que deben seguir;
* Abandonarán el `Bloque A` que ya no forma parte de la cadena principal. Se ha convertido así en un bloque obsoleto.

![](../../dictionnaire/assets/9.png)

> ► *En inglés, se le denomina "Stale Block". En francés, también puede llamarse "bloc périmé" o "bloc abandonné". Aunque no estoy de acuerdo con este uso, algunos bitcoiners usan el término "bloc orphelin" para referirse a lo que en realidad es un bloque obsoleto.*
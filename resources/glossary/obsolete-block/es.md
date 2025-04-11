---
term: OBSOLETO (BLOQUE)

---
Se refiere a un bloque sin hijos: un bloque válido, pero excluido de la cadena principal de Bitcoin. Ocurre cuando dos mineros encuentran un bloque válido a la misma altura de la cadena en un corto periodo de tiempo y lo difunden por la red. Al final, los nodos eligen sólo un bloque para incluirlo en la cadena, según el principio de la cadena con más trabajo acumulado, dejando al otro "obsoleto". El proceso que lleva a la producción de un bloque obsoleto es el siguiente:


- Dos mineros encuentran un bloque válido a la misma altura de cadena en un breve intervalo de tiempo. Llamémosles "Bloque A" y "Bloque B";
- Cada uno difunde su bloque a la red de nodos Bitcoin. Cada nodo tiene ahora 2 bloques a la misma altura. Por lo tanto, hay dos cadenas válidas;
- Los mineros siguen buscando pruebas de trabajo para los siguientes bloques, pero para ello deben elegir necesariamente sólo un bloque entre el `Bloque A` y el `Bloque B` sobre el que minarán;
- Un minero acaba encontrando un bloque válido por encima del "Bloque B". Llamémoslo "Bloque B+1";
- Emiten el "Bloque B+1" a los nodos de la red;
- Como los nodos siguen la cadena más larga (con más trabajo acumulado), estimarán que la `Cadena B` es la que hay que seguir;
- Abandonarán el "Bloque A", que ya no forma parte de la cadena principal. Por tanto, se ha convertido en un bloque obsoleto.

![](../../dictionnaire/assets/9.webp)

> ► *En inglés, se denomina "Stale Block". En francés, también puede denominarse "bloc périmé" o "bloc abandonné". Aunque no estoy de acuerdo con este uso, algunos bitcoiners utilizan el término "bloc orphelin" para referirse a lo que en realidad es un bloque obsoleto.*
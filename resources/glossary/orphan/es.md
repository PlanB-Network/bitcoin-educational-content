---
term: ORPHAN

---
Teóricamente, un bloque huérfano se refiere a un bloque válido recibido por un nodo que aún no ha adquirido el bloque padre, es decir, el anterior en la cadena. Aunque válido, este bloque permanece aislado localmente como huérfano.

Sin embargo, en el uso común, el término "bloque huérfano" suele referirse a un bloque sin hijo: un bloque válido, pero no retenido en la cadena principal de Bitcoin. Esto ocurre cuando dos mineros encuentran un bloque válido a la misma altura de la cadena en un corto periodo de tiempo y lo difunden por la red. Los nodos finalmente eligen sólo un bloque para incluirlo en la cadena, basándose en el principio de la cadena con más trabajo acumulado, convirtiendo al otro en "huérfano"

![](../../dictionnaire/assets/9.webp)

> ► *Personalmente, prefiero utilizar el término "bloque huérfano" para hablar de un bloque sin padre y el término "bloque rancio" para referirme a un bloque que no tiene hijo. Me parece más lógico y comprensible, aunque la mayoría de los bitcoiners no siguen este uso.*
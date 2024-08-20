---
term: ORPHAN
---

Teóricamente, un bloque huérfano se refiere a un bloque válido recibido por un nodo que aún no ha adquirido el bloque padre, es decir, el anterior en la cadena. Aunque válido, este bloque permanece aislado localmente como un huérfano.

Sin embargo, en el uso común, el término "bloque huérfano" a menudo se refiere a un bloque sin hijo: un bloque válido, pero no retenido en la cadena principal de Bitcoin. Esto ocurre cuando dos mineros encuentran un bloque válido en la misma altura de la cadena dentro de un corto período y lo transmiten por la red. Los nodos eventualmente eligen solo un bloque para incluir en la cadena, basándose en el principio de la cadena con el mayor trabajo acumulado, haciendo que el otro sea "huérfano".

![](../../dictionnaire/assets/9.png)

> ► *Personalmente, prefiero usar el término "bloque huérfano" para hablar de un bloque sin un padre y el término "bloque obsoleto" para referirme a un bloque que no tiene un hijo. Encuentro esto más lógico y comprensible, aunque la mayoría de los bitcoiners no siguen este uso.*
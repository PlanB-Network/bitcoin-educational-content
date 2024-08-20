---
term: BIP31
---

Propuesta destinada a mejorar los mecanismos de gestión de red por los nodos de Bitcoin. Antes de BIP31, los nodos de Bitcoin no tenían una manera directa de saber si sus pares aún estaban conectados, operativos y no sobrecargados. BIP31 introdujo el uso de un mensaje `pong`, en respuesta a un mensaje `ping`, lo que permite una verificación activa de la conectividad entre nodos.
---
term: Anchors.dat

definition: Un archivo de Bitcoin Core que almacena direcciones IP de nodos a los que el cliente estaba conectado antes del apagado, para facilitar la reconexión al reiniciar.
---
Archivo utilizado en el cliente Bitcoin Core para almacenar las direcciones IP de los nodos salientes a los que un cliente estaba conectado antes de ser apagado. Anchors.dat se crea cada vez que el nodo se detiene y se elimina cuando se reinicia. Los nodos cuyas direcciones IP están contenidas en este archivo se utilizan para ayudar a establecer conexiones rápidamente cuando el nodo se reinicia.
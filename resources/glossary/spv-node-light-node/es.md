---
term: SPV NODE (LIGHT NODE)
---

Un nodo SPV (*Simple Payment Verification*), a veces llamado "nodo ligero", es un cliente ligero de un nodo Bitcoin que permite a los usuarios validar transacciones sin tener que almacenar toda la cadena de bloques. En lugar de eso, un nodo SPV solo almacena los encabezados de los bloques y obtiene información sobre transacciones específicas consultando a los nodos completos cuando es necesario. Este principio de verificación es posible gracias a la estructura de las transacciones en los bloques de Bitcoin, que están organizadas dentro de un acumulador criptográfico (Árbol de Merkle).

Este enfoque es ventajoso para dispositivos con recursos limitados, como teléfonos móviles. Sin embargo, los nodos SPV dependen de los nodos completos para la disponibilidad de información, lo que implica un nivel adicional de confianza y, por consiguiente, menos seguridad en comparación con los nodos completos. Los nodos SPV no pueden validar transacciones de manera autónoma, pero pueden verificar si una transacción está incluida en un bloque consultando las pruebas de Merkle.
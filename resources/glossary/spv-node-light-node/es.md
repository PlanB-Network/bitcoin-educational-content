---
term: NODO SPV (NODO DE LUZ)

---
Un nodo SPV (*Simple Payment Verification*), a veces llamado "nodo ligero", es un cliente ligero de un nodo Bitcoin que permite a los usuarios validar transacciones sin tener que almacenar toda la cadena de bloques. En su lugar, un nodo SPV sólo almacena las cabeceras de bloque y obtiene información sobre transacciones específicas consultando a nodos completos cuando es necesario. Este principio de verificación es posible gracias a la estructura de las transacciones en bloques de Bitcoin, que se organizan dentro de un acumulador criptográfico (Merkle Tree).

Este enfoque es ventajoso para dispositivos con recursos limitados, como los teléfonos móviles. Sin embargo, los nodos SPV dependen de los nodos completos para disponer de información, lo que implica un nivel adicional de confianza y, en consecuencia, menos seguridad en comparación con los nodos completos. Los nodos SPV no pueden validar transacciones de forma autónoma, pero pueden verificar si una transacción está incluida en un bloque consultando las pruebas Merkle.
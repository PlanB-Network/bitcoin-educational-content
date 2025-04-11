---
term: VERIFICACIÓN SIMPLIFICADA DE PAGOS

---
Método que permite a clientes ligeros verificar transacciones Bitcoin sin descargar la cadena de bloques completa. Un nodo que utiliza SPV sólo descarga las cabeceras de bloque, que son mucho más ligeras que los bloques completos. Cuando necesita verificar una transacción, el nodo SPV solicita una prueba Merkle a los nodos completos para confirmar que la transacción está incluida en un bloque específico. Este enfoque es eficiente para dispositivos con recursos limitados, como los smartphones, pero implica una dependencia de los nodos completos, lo que puede reducir la seguridad y aumentar la confianza requerida.

> ► *El acrónimo "SPV" se utiliza a menudo para referirse a este método.*
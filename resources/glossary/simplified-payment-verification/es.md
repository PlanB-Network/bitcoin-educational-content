---
term: VERIFICACIÓN DE PAGO SIMPLIFICADA
---

Método que permite a los clientes ligeros verificar transacciones de Bitcoin sin necesidad de descargar la blockchain completa. Un nodo que utiliza SPV solo descarga los encabezados de los bloques, los cuales son mucho más ligeros que los bloques completos. Cuando necesita verificar una transacción, el nodo SPV solicita una prueba de Merkle a los nodos completos para confirmar que la transacción está incluida en un bloque específico. Este enfoque es eficiente para dispositivos con recursos limitados, como los smartphones, pero implica una dependencia de los nodos completos, lo que puede reducir la seguridad y aumentar la confianza necesaria.

> ► *El acrónimo "SPV" se utiliza a menudo para referirse a este método.*
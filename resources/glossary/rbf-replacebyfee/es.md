---
term: RBF (REPLACE-BY-FEE)
---

Un mecanismo transaccional que permite al remitente reemplazar una transacción con otra pagando tarifas más altas, con el fin de acelerar su confirmación. Si una transacción con tarifas demasiado bajas se queda atascada, el remitente puede usar *Replace-By-Fee* para aumentar las tarifas y priorizar su transacción de reemplazo en los mempools.

RBF es aplicable mientras la transacción esté en los mempools; una vez en un bloque, ya no puede ser reemplazada. Al enviarla inicialmente, la transacción debe especificar su disponibilidad para ser reemplazada ajustando el valor de `nSequence` a un número menor que `0xfffffffe`. Esto se conoce como una "bandera" RBF. Esta configuración señala la posibilidad de actualizar la transacción después de haber sido transmitida, lo que posteriormente permite un RBF. Sin embargo, a veces es posible reemplazar una transacción que no ha señalizado RBF. Los nodos que usan el parámetro de configuración `mempoolfullrbf=1` aceptan este reemplazo incluso si RBF no fue señalado inicialmente.

A diferencia de CPFP (*Child Pays For Parent*), donde el destinatario puede actuar para acelerar la transacción, RBF (*Replace-By-Fee*) permite al remitente tomar la iniciativa para acelerar su propia transacción aumentando las tarifas.
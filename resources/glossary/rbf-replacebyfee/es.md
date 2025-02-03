---
term: RBF (REPLACE-BY-FEE)

---
Mecanismo transaccional que permite al remitente sustituir una transacción por otra pagando tasas más altas, con el fin de acelerar su confirmación. Si una transacción con tasas demasiado bajas se atasca, el remitente puede utilizar *Replace-By-Fee* para aumentar las tasas y dar prioridad a su transacción de sustitución en los mempools.

RBF es aplicable mientras la transacción esté en los mempools; una vez en un bloque, ya no puede ser reemplazada. En el envío inicial, la transacción debe especificar su disponibilidad para ser reemplazada ajustando el valor de `nSequence` a un número menor que `0xfffffffe`. Esto se conoce como "bandera" RBF. Este ajuste señala la posibilidad de actualizar la transacción después de que se haya emitido, lo que permite posteriormente una RBF. Sin embargo, a veces es posible reemplazar una transacción que no ha señalado RBF. Los nodos que utilizan el parámetro de configuración `mempoolfullrbf=1` aceptan este reemplazo incluso si RBF no fue señalizado inicialmente.

A diferencia de la CPFP (*Child Pays For Parent*), en la que el destinatario puede actuar para acelerar la transacción, la RBF (*Replace-By-Fee*) permite al remitente tomar la iniciativa para acelerar su propia transacción aumentando las comisiones.
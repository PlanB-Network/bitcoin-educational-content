---
term: ELTOO
---

Un protocolo general para las segundas capas de Bitcoin que define cómo gestionar conjuntamente la propiedad de un UTXO. Eltoo fue diseñado por Christian Decker, Rusty Russell y Olaoluwa Osuntokun, particularmente para resolver los problemas asociados con los mecanismos de negociación de los estados de canales de Lightning, es decir, entre la apertura y el cierre. La arquitectura de Eltoo simplifica el proceso de negociación al introducir un sistema de gestión de estado lineal, reemplazando el enfoque basado en penalizaciones establecido con un método de actualización más flexible y menos punitivo. Este protocolo requiere el uso de un nuevo tipo de SigHash que permite ignorar todas las entradas en la firma de una transacción. Este SigHash se llamó inicialmente `SIGHASH_NOINPUT`, luego `SIGHASH_ANYPREVOUT` (*Cualquier Salida Anterior*). Su implementación está planeada en el BIP118.

> ► *Eltoo a veces también se refiere como "LN-Symmetry".*
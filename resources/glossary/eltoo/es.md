---
term: ELTOO

---
Un protocolo general para las segundas capas de Bitcoin que define cómo gestionar conjuntamente la propiedad de un UTXO. Eltoo fue diseñado por Christian Decker, Rusty Russell y Olaoluwa Osuntokun, en particular para resolver los problemas asociados a los mecanismos de negociación de los estados del canal Lightning, es decir, entre la apertura y el cierre. La arquitectura Eltoo simplifica el proceso de negociación introduciendo un sistema lineal de gestión de estados, que sustituye el enfoque establecido basado en penalizaciones por un método de actualización más flexible y menos punitivo. Este protocolo requiere el uso de un nuevo tipo de SigHash que permite ignorar todas las entradas en la firma de una transacción. Este SigHash se llamó inicialmente `SIGHASH_NOINPUT`, y después `SIGHASH_ANYPREVOUT` (*Cualquier salida anterior*). Su implementación está prevista en el BIP118.

> ► *Eltoo también se denomina a veces "simetría LN "*
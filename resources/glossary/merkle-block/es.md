---
term: Bloque Merkle

definition: Estructura que proporciona una prueba compacta de la inclusión de una transacción en un bloque para los clientes ligeros.
---
Estructura de datos utilizada en el contexto de BIP37 (*Transaction Bloom Filtering*) para proporcionar una prueba compacta de la inclusión de transacciones específicas en un bloque. Se utiliza especialmente en los monederos SPV. El bloque Merkle contiene las cabeceras de bloque, las transacciones filtradas y un árbol Merkle parcial, lo que permite a los clientes ligeros verificar rápidamente si una transacción pertenece a un bloque sin descargar todas las transacciones.
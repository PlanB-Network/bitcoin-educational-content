---
term: BLOQUE MERKLE

---
Estructura de datos utilizada en el contexto de BIP37 (*Transaction Bloom Filtering*) para proporcionar una prueba compacta de la inclusión de transacciones específicas en un bloque. Se utiliza especialmente en los monederos SPV. El bloque Merkle contiene las cabeceras de bloque, las transacciones filtradas y un árbol Merkle parcial, lo que permite a los clientes ligeros verificar rápidamente si una transacción pertenece a un bloque sin descargar todas las transacciones.
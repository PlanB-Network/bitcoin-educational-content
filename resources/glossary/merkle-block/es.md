---
term: MERKLE BLOCK
---

Una estructura de datos utilizada en el contexto de BIP37 (*Transaction Bloom Filtering*) para proporcionar una prueba compacta de la inclusión de transacciones específicas en un bloque. Se utiliza notablemente para carteras SPV. El MERKLE BLOCK contiene los encabezados de bloque, transacciones filtradas y un árbol de Merkle parcial, permitiendo a los clientes ligeros verificar rápidamente si una transacción pertenece a un bloque sin necesidad de descargar todas las transacciones.
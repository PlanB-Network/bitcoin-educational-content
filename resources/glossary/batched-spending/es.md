---
term: GASTO POR LOTES

---
El gasto por lotes es una técnica de gasto utilizada principalmente por entidades con un gran volumen de transacciones, como las plataformas de intercambio, para optimizar y reducir los costes de transacción. Al agrupar múltiples pagos destinados a diferentes destinatarios en una única transacción Bitcoin, el gasto por lotes permite un menor consumo de espacio en los bloques, reduciendo así las comisiones asociadas. El gasto por lotes se caracteriza por un patrón reconocible durante el análisis de la cadena. Este patrón se evidencia por el uso de unos pocos UTXOs como entradas (a menudo sólo uno) y la creación de múltiples UTXOs como salidas. La interpretación de este patrón es que estamos presenciando un gasto por lotes. Al encontrar este patrón en el análisis de cadenas, se puede deducir que el UTXO de entrada procede de una empresa con una actividad económica importante y que los UTXO de salida estarán dispersos. Algunos pertenecerán a los clientes de la empresa. Otros irán a parar a empresas asociadas. Por último, habrá sin duda una parte que regrese a la empresa emisora.

![](../../dictionnaire/assets/8.webp)

> en francés, "batched spending" puede traducirse como "dépense groupée"
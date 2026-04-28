---
term: BIP0145

definition: Actualización de la llamada JSON-RPC getblocktemplate para integrar el soporte de SegWit y el cálculo del peso de las transacciones.
---
Actualiza la llamada JSON-RPC `getblocktemplate` para incluir soporte para SegWit, de acuerdo con BIP141. Esta actualización permite a los mineros construir bloques teniendo en cuenta la nueva medida del "peso" de las transacciones y los bloques introducida por SegWit, y otros parámetros como el cálculo del límite de sigops.
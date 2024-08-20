---
term: UTXO
---

Acrónimo de *Unspent Transaction Output* (Salida de Transacción no Gastada). Un UTXO es una salida de transacción que aún no ha sido gastada, lo que significa que no ha sido utilizada como entrada para una nueva transacción. Los UTXOs representan la fracción de bitcoins que un usuario posee y que actualmente están disponibles para ser gastados. Cada UTXO está asociado con un script de salida específico (`scriptPubKey`), que define las condiciones necesarias para gastar los bitcoins. Las transacciones en Bitcoin consumen estos UTXOs como entradas y crean nuevos UTXOs como salidas. El modelo UTXO es fundamental para Bitcoin, ya que permite una fácil verificación de que las transacciones no intentan gastar bitcoins que no existen o que ya han sido gastados.
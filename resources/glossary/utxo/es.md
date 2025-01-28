---
term: UTXO

---
Acrónimo de *Salida de transacción no gastada*. Un UTXO es una salida de transacción que aún no se ha gastado, lo que significa que no se ha utilizado como entrada para una nueva transacción. Los UTXOs representan la fracción de bitcoins que un usuario posee y que están actualmente disponibles para ser gastados. Cada UTXO está asociado a un script de salida específico (`scriptPubKey`), que define las condiciones necesarias para gastar los bitcoins. Las transacciones en Bitcoin consumen estos UTXOs como entradas y crean nuevos UTXOs como salidas. El modelo UTXO es fundamental para Bitcoin, ya que permite verificar fácilmente que las transacciones no están intentando gastar bitcoins que no existen o que ya han sido gastados.
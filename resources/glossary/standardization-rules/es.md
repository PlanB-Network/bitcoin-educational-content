---
term: NORMAS DE NORMALIZACIÓN

---
Las reglas de estandarización son adoptadas individualmente por cada nodo Bitcoin, además de las reglas de consenso, para definir la estructura de las transacciones no confirmadas que acepta en su mempool y difunde a sus pares. Estas reglas son configuradas y ejecutadas localmente por cada nodo y pueden variar de un nodo a otro. Se aplican exclusivamente a las transacciones no confirmadas. Por lo tanto, un nodo sólo aceptará una transacción que considere no estándar si ya está incluida en un bloque válido.

Se observa que la mayoría de los nodos dejan las configuraciones por defecto establecidas en Bitcoin Core, creando así una uniformidad de reglas de estandarización en toda la red. Una transacción que, aunque cumpla con las reglas de consenso, no se adhiera a estas reglas de estandarización, tendrá dificultades para ser difundida a través de la red. Sin embargo, puede incluirse en un bloque válido si llega a un minero. En la práctica, estas transacciones, denominadas "no estándar", son a menudo transmitidas directamente a un minero a través de medios externos fuera de la red peer-to-peer de Bitcoin. Esta suele ser la única forma de confirmar este tipo de transacciones.

Por ejemplo, una transacción que no asigna ninguna comisión es válida según las reglas de consenso y no estándar porque la política por defecto de Bitcoin Core para el parámetro `minRelayTxFee` es `0.00001` (en BTC/kB).

> ► *El término "reglas mempool" también se utiliza a veces para referirse a las reglas de normalización.*
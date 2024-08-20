---
term: REGLAS DE ESTANDARIZACIÓN
---

Las reglas de estandarización son adoptadas individualmente por cada nodo de Bitcoin, además de las reglas de consenso, para definir la estructura de las transacciones no confirmadas que acepta en su mempool y transmite a sus pares. Por lo tanto, estas reglas son configuradas y ejecutadas localmente por cada nodo y pueden variar de uno a otro. Se aplican exclusivamente a transacciones no confirmadas. Por lo tanto, un nodo solo aceptará una transacción que considera no estándar si ya está incluida en un bloque válido.

Se nota que la mayoría de los nodos dejan las configuraciones predeterminadas como se establecen en Bitcoin Core, creando así una uniformidad de reglas de estandarización a través de la red. Una transacción que, aunque cumpla con las reglas de consenso, no se adhiere a estas reglas de estandarización, tendrá dificultades para ser transmitida a través de la red. Sin embargo, aún puede ser incluida en un bloque válido si llega a un minero. En la práctica, estas transacciones, referidas como "no estándar", a menudo se transmiten directamente a un minero por medios externos fuera de la red peer-to-peer de Bitcoin. Esta es a menudo la única manera de confirmar este tipo de transacción.

Por ejemplo, una transacción que no asigna comisiones es válida según las reglas de consenso y no estándar porque la política predeterminada de Bitcoin Core para el parámetro `minRelayTxFee` es `0.00001` (en BTC/kB).

> ► *El término "reglas del mempool" también se usa a veces para referirse a las reglas de estandarización.*
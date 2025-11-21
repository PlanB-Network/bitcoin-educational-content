---
term: BIP0330
---

Una propuesta conocida como "*Erlay*", cuyo objetivo es optimizar la propagación de transacciones no confirmadas en la red Bitcoin. En la actualidad, las transacciones se difunden a todos los pares de un nodo, lo que provoca redundancia y un uso excesivo del ancho de banda. BIP330 propone limitar esta difusión a 8 pares por defecto, y luego utilizar un mecanismo de reconciliación para compartir eficientemente las transacciones que faltan. Erlay reduce el consumo de ancho de banda en torno al 40%. También evita un aumento lineal del consumo de ancho de banda con el número de pares conectados al nodo.
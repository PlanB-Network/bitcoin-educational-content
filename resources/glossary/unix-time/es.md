---
term: UNIX TIME
---

Unix Time o Timestamp de Unix representa el número de segundos que han transcurrido desde el 1 de enero de 1970, a medianoche UTC (Unix Epoch). Este sistema se utiliza en los sistemas operativos Unix y derivados para marcar el tiempo de manera universal y estandarizada. Permite la sincronización de relojes y la gestión de eventos basados en el tiempo, independientemente de las zonas horarias.

En el contexto de Bitcoin, se utiliza para el reloj local de los nodos, y por lo tanto para el cálculo de NAT (Network-Adjusted Time, Tiempo Ajustado por la Red). El tiempo ajustado por la red es una mediana de los tiempos de los nodos calculados localmente por cada nodo, y esta referencia se utiliza entonces para verificar la validez de los timestamps de los bloques. De hecho, para que un bloque sea aceptado por un nodo, su timestamp debe estar entre el MTP (Median Time Past de los últimos 11 bloques minados) y el NAT más 2 horas:

```text
MTP < Timestamp Válido < (NAT + 2h)
```

Unix Time también se utiliza para establecer timelocks cuando se basan en tiempo real, en lugar de en un número de bloques.
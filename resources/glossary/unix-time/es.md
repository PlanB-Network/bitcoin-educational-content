---
term: TIEMPO UNIX

---
Unix Time o Unix Timestamp representa el número de segundos que han transcurrido desde el 1 de enero de 1970, a medianoche UTC (Unix Epoch). Este sistema se utiliza en los sistemas operativos Unix y derivados para marcar el tiempo de forma universal y estandarizada. Permite la sincronización de relojes y la gestión de eventos basados en el tiempo, independientemente de las zonas horarias.

En el contexto de Bitcoin, se utiliza para el reloj local de los nodos, y por tanto para el cálculo del NAT (Network-Adjusted Time). El tiempo ajustado a la red es una mediana de los tiempos calculados localmente por cada nodo, y esta referencia se utiliza para verificar la validez de las marcas de tiempo de los bloques. De hecho, para que un bloque sea aceptado por un nodo, su marca de tiempo debe estar comprendida entre la MTP (mediana del tiempo pasado de los últimos 11 bloques minados) y la NAT más 2 horas:

```text
MTP < Valid Timestamp < (NAT + 2h)
```

Unix Time también se utiliza para establecer timelocks cuando se basan en tiempo real, en lugar de en un número de bloques.
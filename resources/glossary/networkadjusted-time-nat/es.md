---
term: NETWORK-ADJUSTED TIME (NAT)
---

Estimación del tiempo universal establecido en los relojes de los nodos de la red. Cada nodo calcula su NAT tomando la mediana de las diferencias de tiempo entre su reloj local (UTC) y aquellos de los nodos a los que está conectado, luego suma su reloj local a la mediana de estas diferencias, hasta un máximo de 70 minutos. El tiempo ajustado de la red es, por lo tanto, una mediana de los tiempos de los nodos calculada localmente por cada nodo. Este marco de referencia se utiliza entonces para verificar la validez de los timestamps de los bloques. De hecho, para que un bloque sea aceptado por un nodo, su timestamp debe estar entre el MTP (tiempo medio de los últimos 11 bloques minados) y el NAT más 2 horas:

```text
MTP < Timestamp Válido < (NAT + 2h)
```
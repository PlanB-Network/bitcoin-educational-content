---
term: TIEMPO AJUSTADO A LA RED (NAT)

---
Estimación de la hora universal establecida en los relojes de los nodos de la red. Cada nodo calcula su NAT tomando la mediana de las diferencias horarias entre su reloj local (UTC) y los de los nodos a los que está conectado, añadiendo después su reloj local a la mediana de estas diferencias, hasta un máximo de 70 minutos. La hora ajustada a la red es, por tanto, la mediana de las horas calculadas localmente por cada nodo. Este marco de referencia se utiliza a continuación para verificar la validez de las marcas de tiempo de los bloques. En efecto, para que un bloque sea aceptado por un nodo, su marca de tiempo debe estar comprendida entre la MTP (mediana del tiempo de los 11 últimos bloques minados) y la NAT más 2 horas:

```text
MTP < Valid Timestamp < (NAT + 2h)
```
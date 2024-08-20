---
term: TRANSACTION FEES
---

Las tarifas de transacción representan una suma que tiene como objetivo compensar a los mineros por su participación en el mecanismo de prueba de trabajo. Estas tarifas incentivan a los mineros a incluir transacciones en los bloques que crean. Resultan de la diferencia entre el total de entradas y el total de salidas en una transacción:

```text
fees = inputs - outputs
```

Se expresan en `sats/vBytes`, lo que significa que las tarifas no dependen de la cantidad de bitcoins enviados, sino del peso de la transacción. Son elegidas libremente por el remitente de una transacción y determinan su velocidad de inclusión en un bloque a través de un mecanismo de subasta. Por ejemplo, digamos que realizo una transacción con una entrada de `100,000 sats`, una salida de `40,000 sats` y otra salida de `58,500 sats`. El total de las salidas es `98,500 sats`. Las tarifas asignadas a esta transacción son `1,500 sats`. El minero que incluya mi transacción puede crear `1,500 sats` en su transacción de coinbase a cambio de los `1,500 sats` que no recuperé en mis salidas.

Las transacciones con tarifas más altas, en relación con su tamaño, son tratadas como una prioridad por los mineros, lo que puede acelerar el proceso de confirmación. Por el contrario, las transacciones con tarifas más bajas pueden retrasarse durante períodos de alta congestión. Vale la pena señalar que las tarifas de transacción de Bitcoin son distintas del subsidio de bloque, que es un incentivo adicional para los mineros. La recompensa de bloque consiste en nuevos bitcoins creados con cada bloque minado (subsidio de bloque), así como las tarifas de transacción recopiladas. Mientras que el subsidio de bloque disminuye con el tiempo debido al límite de suministro total de bitcoins, las tarifas de transacción continuarán desempeñando un papel crucial en incentivar la participación de los mineros.

A nivel de protocolo, nada impide a los usuarios incluir transacciones sin ninguna tarifa en un bloque. En realidad, este tipo de transacción sin tarifas es excepcional. Por defecto, los nodos de Bitcoin no retransmiten transacciones con tarifas inferiores a `1 sat/vBytes`. Si algunas transacciones sin tarifas han pasado, es porque fueron integradas directamente por el minero ganador, sin atravesar la red de nodos. Por ejemplo, la siguiente transacción no incluye tarifas:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

En este ejemplo específico, fue una transacción iniciada por el director del pool de minería F2Pool. Como usuario regular, el límite inferior actual es, por lo tanto, `1 sat/vBytes`.
También es necesario considerar los límites de purga. Durante períodos de alta congestión, los mempools de los nodos purgan sus transacciones pendientes por debajo de cierto umbral, para respetar su límite de RAM asignado. Este límite es elegido libremente por el usuario, pero muchos dejan el valor predeterminado de Bitcoin Core en 300 MB. Se puede modificar en el archivo `bitcoin.conf` con el parámetro `maxmempool`.
> ► *En inglés, nos referimos a ello como "transaction fees".*
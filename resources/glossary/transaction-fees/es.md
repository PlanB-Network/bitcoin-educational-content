---
term: GASTOS DE TRANSACCIÓN

---
Las comisiones por transacción representan una cantidad que pretende compensar a los mineros por su participación en el mecanismo de prueba de trabajo. Estas comisiones animan a los mineros a incluir transacciones en los bloques que crean. Resultan de la diferencia entre la cantidad total de entradas y la cantidad total de salidas en una transacción:

```text
fees = inputs - outputs
```

Se expresan en `sats/vBytes`, lo que significa que las tarifas no dependen de la cantidad de bitcoins enviados, sino del peso de la transacción. Son elegidas libremente por el remitente de una transacción y determinan su velocidad de inclusión en un bloque mediante un mecanismo de subasta. Por ejemplo, supongamos que hago una transacción con una entrada de 100.000 sats, una salida de 40.000 sats y otra salida de 58.500 sats. El total de las salidas es de 98.500 sats. Las tasas asignadas a esta transacción son de 1.500 sats. El minero que incluya mi transacción puede crear 1.500 sats en su transacción de Coinbase a cambio de los 1.500 sats que no recuperé en mis salidas.

Las transacciones con tasas más altas, en relación con su tamaño, son tratadas como prioritarias por los mineros, lo que puede acelerar el proceso de confirmación. Por el contrario, las transacciones con tasas más bajas pueden retrasarse durante periodos de alta congestión. Vale la pena señalar que las tasas de transacción de Bitcoin son distintas de la subvención por bloque, que es un incentivo adicional para los mineros. La recompensa por bloque consiste en nuevos bitcoins creados con cada bloque minado (subvención por bloque), así como las tasas de transacción recaudadas. Aunque la subvención por bloque disminuye con el tiempo debido al límite de la oferta total de bitcoins, las comisiones por transacción seguirán desempeñando un papel crucial para animar a los mineros a participar.

A nivel de protocolo, nada impide a los usuarios incluir transacciones sin comisiones en un bloque. En realidad, este tipo de transacciones sin tasas son excepcionales. Por defecto, los nodos Bitcoin no retransmiten transacciones con tasas inferiores a `1 sat/vBytes`. Si algunas transacciones sin tasas han pasado, es porque fueron integradas directamente por el minero ganador, sin atravesar la red de nodos. Por ejemplo, la siguiente transacción no incluye tasas:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

En este ejemplo concreto, se trataba de una transacción iniciada por el director del pool de minería F2Pool. Como usuario habitual, el límite inferior actual es, por tanto, `1 sat/vBytes`.

También es necesario considerar los límites de la purga. Durante los periodos de alta congestión, los mempools de los nodos purgan sus transacciones pendientes por debajo de un cierto umbral, con el fin de respetar su límite de RAM asignada. Este límite es elegido libremente por el usuario, pero muchos dejan el valor por defecto de Bitcoin Core en 300 MB. Puede ser modificado en el archivo `bitcoin.conf` con el parámetro `maxmempool`.

> ► *En inglés, lo denominamos "transaction fees "*
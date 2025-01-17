---
name: Stonewall
description: Entendiendo y utilizando transacciones Stonewall
---
![cover stonewall](assets/cover.webp)

***ADVERTENCIA:** Tras la detención de los fundadores de Samourai Wallet y la incautación de sus servidores el 24 de abril, el uso de la aplicación Samourai Wallet ahora requiere una conexión a su propio Dojo para funcionar correctamente. Aparte de esto, las transacciones Stonewall no se ven afectadas en absoluto y pueden seguir realizándose sin problemas. De hecho, este tipo de transacciones se llevan a cabo de manera autónoma, sin necesidad de colaboración externa ni conexión a través de Soroban.*

_Estamos siguiendo de cerca la evolución de este caso así como los desarrollos relacionados con las herramientas asociadas. Ten la seguridad de que actualizaremos este tutorial a medida que estén disponibles nuevas informaciones._

_Este tutorial se proporciona únicamente con fines educativos e informativos. No respaldamos ni alentamos el uso de estas herramientas para fines criminales. Es responsabilidad de cada usuario cumplir con las leyes en su jurisdicción._

---

> *"Rompe las suposiciones del análisis de blockchain con dudas matemáticamente probables entre el emisor y el receptor de tus transacciones."*

## ¿Qué es una transacción Stonewall?
Stonewall es una forma específica de transacción de Bitcoin destinada a aumentar la privacidad del usuario durante una transacción al imitar un coinjoin entre dos partes, sin ser realmente uno. De hecho, esta transacción no es colaborativa. Un usuario puede construirla solo, involucrando únicamente sus propios UTXOs como entradas. Por lo tanto, puedes crear una transacción Stonewall para cualquier ocasión sin necesidad de coordinarte con otro usuario.

El funcionamiento de una transacción Stonewall es el siguiente: como entrada, el emisor utiliza 2 UTXOs que le pertenecen. Como salida, la transacción produce 4 salidas, incluidas 2 que serán exactamente del mismo monto. Las otras 2 serán cambio. Entre las 2 salidas del mismo monto, solo una irá realmente al destinatario del pago.

Solo hay 2 roles en una transacción Stonewall:
- El emisor, quien realiza el pago efectivo;
- El destinatario, quien puede desconocer la naturaleza específica de la transacción y simplemente espera un pago del emisor.

Tomemos un ejemplo para entender esta estructura de transacción. Alice está en la panadería para comprar su baguette, que cuesta `4,000 sats`. Ella quiere pagar en bitcoins manteniendo un cierto nivel de privacidad en su pago. Por lo tanto, decide crear una transacción Stonewall para el pago.
![transaction stonewall bakery](assets/es/1.webp)
Analizando esta transacción, podemos ver que el panadero recibió efectivamente `4,000 sats` como pago por la baguette. Alice utilizó 2 UTXOs como entradas: uno de `10,000 sats` y otro de `15,000 sats`. Como salida, recibió 3 UTXOs: uno de `4,000 sats`, uno de `6,000 sats` y otro de `11,000 sats`. Alice tiene un balance neto de `-4,000 sats` en esta transacción, que corresponde al precio de la baguette.

En este ejemplo, omití intencionalmente las comisiones de minería para facilitar la comprensión. En realidad, las comisiones de transacción son cubiertas completamente por el emisor.

## ¿Cuál es la diferencia entre Stonewall y Stonewall x2?
La transacción Stonewall opera de la misma manera que la transacción StonewallX2, con la única diferencia de que esta última requiere colaboración, a diferencia de la transacción Stonewall clásica, de ahí la designación "x2". De hecho, la transacción Stonewall se puede ejecutar sin requerir cooperación externa: el emisor puede llevarla a cabo sin la asistencia de otra persona. Sin embargo, para una transacción Stonewall x2, un participante adicional, llamado "colaborador", se une al proceso. El colaborador aporta sus propios bitcoins como entrada, junto con los del emisor, y recibe la suma total como salida (menos las comisiones de minería).

Revisitemos nuestro ejemplo con Alice en la panadería. Si ella hubiera querido hacer una transacción Stonewall x2, Alice habría tenido que colaborar con Bob (un tercero) al crear la transacción. Cada uno habría proporcionado un UTXO de entrada. Bob entonces habría recibido el monto completo de su entrada como salida. El panadero habría recibido el pago por su baguette de la misma manera que en la transacción Stonewall, mientras que Alice habría recibido su balance inicial de vuelta, menos el costo de la baguette.
![transaction stonewall x2](assets/es/2.webp)
Desde una perspectiva externa, el patrón de la transacción habría permanecido exactamente igual.
![Stonewall o Stonewall x2 ?](assets/es/3.webp)

En resumen, las transacciones Stonewall y Stonewall x2 comparten una estructura idéntica. La distinción entre las dos radica en su naturaleza colaborativa. La transacción Stonewall se desarrolla individualmente, sin necesidad de colaboración. En contraste, la transacción Stonewall x2 depende de la cooperación entre dos individuos para su implementación.

[**-> Descubre más sobre las transacciones Stonewall x2**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)

## ¿Cuál es el propósito de una transacción Stonewall?
La estructura Stonewall añade una cantidad significativa de entropía a la transacción y oscurece el análisis de la cadena. Desde una perspectiva externa, tal transacción puede interpretarse como un pequeño coinjoin entre dos personas. Pero en realidad, al igual que la transacción Stonewall x2, es un pago. Este método, por lo tanto, crea incertidumbres en el análisis de la cadena, y puede incluso llevar a pistas falsas.

Revisemos el ejemplo de Alice en la panadería. La transacción en la blockchain aparecería de la siguiente manera:
![Stonewall o Stonewall x2 ?](assets/es/4.webp)
Un observador externo que se base en heurísticas comunes de análisis de cadena podría concluir erróneamente que "*dos personas han realizado un pequeño coinjoin, con un UTXO cada uno como entrada y dos UTXOs cada uno como salida*".
![Stonewall o Stonewall x2 ?](assets/es/5.webp)
Esta interpretación es incorrecta porque, como sabes, un UTXO fue enviado al panadero, los 2 UTXOs en la entrada provienen de Alice, y ella recibió 3 salidas de cambio.

![transaction stonewall baker](assets/es/1.webp)
Incluso si un observador externo logra identificar el patrón de la transacción Stonewall, no tendrán toda la información. No podrán determinar cuál de los dos UTXOs de los mismos montos corresponde al pago. Además, no podrán determinar si los dos UTXOs en la entrada provienen de dos personas diferentes o si pertenecen a una sola persona que los fusionó. Este último punto se debe al hecho de que las transacciones Stonewall x2, de las que hablamos anteriormente, siguen exactamente el mismo patrón que las transacciones Stonewall. Desde el exterior y sin información adicional sobre el contexto, es imposible diferenciar una transacción Stonewall de una transacción Stonewall x2. Sin embargo, las primeras no son transacciones colaborativas, mientras que las segundas sí lo son. Esto añade aún más dudas sobre este gasto.
![Stonewall o Stonewall x2 ?](assets/es/3.webp)
## ¿Cómo realizar una transacción Stonewall en Samourai Wallet?
A diferencia de las transacciones Stowaway o Stonewall x2 (cahoots), la transacción Stonewall no requiere el uso de Paynyms. Se puede realizar directamente, sin pasos de preparación. Para hacerlo, sigue nuestro tutorial en video sobre Samourai Wallet: 
![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## ¿Cómo realizar una transacción Stonewall en Sparrow Wallet?
A diferencia de las transacciones Stowaway o Stonewall x2 (cahoots), la transacción Stonewall no requiere el uso de Paynyms. Se puede realizar directamente, sin pasos de preparación. Para hacerlo, sigue nuestro tutorial en video sobre Sparrow Wallet:
![Tutorial de Stonewall - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)

**Recursos Externos:**
- https://docs.samourai.io/en/spend-tools#stonewall.

---
name: Stonewall
description: Comprender y utilizar transacciones Stonewall
---
![portada stonewall](assets/cover.jpeg)

> *"Rompe las suposiciones del análisis de blockchain con dudas matemáticamente demostrables entre el remitente y el destinatario de tus transacciones."*

## ¿Qué es una transacción Stonewall?
Stonewall es una forma específica de transacción de Bitcoin que tiene como objetivo aumentar la privacidad del usuario durante un gasto al imitar una coinjoin entre dos personas, sin ser realmente una. De hecho, esta transacción no es colaborativa. Un usuario puede construirla solo, solo involucrando sus propios UTXOs como entradas. Por lo tanto, puedes crear una transacción Stonewall para cualquier ocasión sin necesidad de sincronizarte con otro usuario.

El funcionamiento de una transacción Stonewall es el siguiente: como entrada de la transacción, el remitente utiliza 2 UTXOs que le pertenecen. Como salida, la transacción produce 4 salidas, 2 de las cuales serán exactamente la misma cantidad. Las otras 2 serán cambio. Entre las 2 salidas de la misma cantidad, solo una irá realmente al destinatario del pago.

Por lo tanto, solo hay 2 roles en una transacción Stonewall:
- El remitente, quien realiza el pago real;
- El destinatario, quien puede ignorar la naturaleza específica de la transacción y simplemente esperar un pago del remitente.

Tomemos un ejemplo para entender esta estructura de transacción. Alice está en la panadería para comprar su baguette, que cuesta 4,000 sats. Quiere pagar en bitcoins manteniendo cierto nivel de privacidad para su pago. Por lo tanto, decide construir una transacción Stonewall para el pago.
![transacción stonewall panadería](assets/es/1.png)
Al analizar esta transacción, podemos ver que el panadero efectivamente recibió 4,000 sats como pago por la baguette. Alice utilizó 2 UTXOs como entradas: uno de 10,000 sats y otro de 15,000 sats. Como salida, recibió 3 UTXOs: uno de 4,000 sats, uno de 6,000 sats y uno de 11,000 sats. Por lo tanto, Alice tiene un saldo neto de -4,000 sats en esta transacción, que corresponde al precio de la baguette.

En este ejemplo, intencionalmente omití las tarifas de minería para facilitar la comprensión. En realidad, las tarifas de transacción son completamente cubiertas por el remitente.

¿Cuál es la diferencia entre Stonewall y Stonewall x2?
La transacción Stonewall funciona de la misma manera que la transacción StonewallX2, con la excepción de que esta última requiere colaboración, a diferencia de la transacción Stonewall clásica, de ahí la designación "x2". De hecho, la transacción Stonewall se puede ejecutar sin cooperación externa: el remitente puede completarla sin la ayuda de otra persona. Sin embargo, para una transacción Stonewall x2, un participante adicional, llamado "colaborador", se une al proceso. El colaborador contribuye con sus propios bitcoins como entradas, junto con los del remitente, y recibe la suma total como salidas (menos las tarifas de minería).

Revisemos nuestro ejemplo con Alice en la panadería. Si ella hubiera querido hacer una transacción Stonewall x2, Alice habría tenido que colaborar con Bob (un tercero) durante la creación de la transacción. Cada uno habría proporcionado un UTXO como entrada. Bob luego habría recibido la totalidad de su contribución como salida. El panadero habría recibido el pago por la baguette de la misma manera que en la transacción Stonewall, mientras que Alice habría recibido su saldo inicial, menos el costo de la baguette.
![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)
Como traductor profesional especializado, mi tarea principal es traducir con precisión contenido técnico del inglés a mi lengua materna, el español. Por favor, sigue las siguientes pautas para asegurar una traducción de alta calidad:

Idioma original: El contenido está originalmente en inglés.
Naturaleza del contenido: Encontrarás material técnico, potencialmente incluyendo terminología específica de la industria.
Enlaces y palabras técnicas: No traduzcas URLs o términos técnicos altamente específicos. Si tienes dudas, conserva el término original.
Consistencia de formato: Mantén el mismo diseño y formato de markdown que el texto original. La consistencia de la estructura es crucial.
Propiedades YML: Si una línea comienza con una propiedad YML (por ejemplo, 'name:', 'goal:', 'objectives:'), conserva el nombre de la propiedad en inglés.
Contexto cultural: Para referencias culturales o específicas de contexto que no se puedan traducir directamente, parafrasea para preservar el significado pretendido o proporciona una breve explicación.
El énfasis debe estar en mantener la integridad del contenido técnico mientras se asegura que la traducción sea comprensible y precisa en español.

Este es el texto a traducir:
![Tutorial de Stonewall - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)

**Recursos externos:**
- https://docs.samourai.io/en/spend-tools#stonewall ;
- https://samouraiwallet.com/stonewall.

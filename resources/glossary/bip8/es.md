---
term: BIP8

---
Desarrollado a raíz de los debates sobre SegWit, que utilizó BIP9 para su activación, BIP8 es un método de activación de bifurcación suave que incorpora de forma nativa un mecanismo automático UASF (*User-Activated Soft Fork*). Al igual que el BIP9, el BIP8 utiliza la señalización de los mineros, pero añade el parámetro `LOT` (*Lock-in On Time out*). Si `LOT` se establece en `true`, al expirar el periodo de señalización sin alcanzar el umbral requerido, se activa automáticamente un UASF, forzando la activación de la bifurcación suave. Este enfoque obliga a los mineros a cooperar o arriesgarse a una UASF impuesta por los usuarios. Además, a diferencia del BIP9, el BIP8 define el periodo de señalización en función de la altura del bloque, eliminando posibles manipulaciones a través del hash rate por parte de los mineros. El BIP8 también permite establecer un umbral de votación variable e introduce un parámetro para una altura de bloque mínima para la activación, dando a los mineros tiempo para prepararse y señalar su acuerdo por adelantado sin estar necesariamente listos. Cuando se activa una bifurcación suave a través de BIP8 con el parámetro `LOT=true`, se utiliza un método muy agresivo contra los mineros, que se ven sometidos inmediatamente a la presión de una posible UASF. En efecto, sólo les deja 2 opciones:


- Sea cooperativo y facilite así el proceso de activación;
- No cooperar, en cuyo caso los usuarios realizan automáticamente una UASF para imponer la bifurcación suave.
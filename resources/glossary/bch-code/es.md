---
term: CÓDIGO BCH
---

Clase de códigos de corrección de errores utilizados para detectar y corregir errores en una secuencia de datos. En otras palabras, los códigos de corrección de errores BCH se utilizan para encontrar y corregir errores aleatorios en la información transmitida, con el fin de garantizar que llegue intacta a su destino. Las siglas "BCH" corresponden a las iniciales de los nombres de los inventores de estos códigos: Bose, Ray-Chaudhuri y Hocquenghem.


Esta herramienta se utiliza en muchos ámbitos de la informática, como las unidades SSD, los DVD y los códigos QR. Por ejemplo, gracias a estos códigos de corrección de errores, aunque un código QR esté parcialmente cubierto, sigue siendo posible recuperar la información que codifica.


Como parte de Bitcoin, los códigos BCH se utilizan para la suma de comprobación en los formatos Address Bech32 y Bech32m (post-SegWit). Representan un mejor compromiso entre el tamaño de la suma de comprobación y la capacidad de detección de errores que las sencillas funciones Hash utilizadas anteriormente en las direcciones Legacy. En el contexto de Bitcoin, los códigos BCH sólo se utilizan para la detección de errores, no para su corrección. Así, el software de la cartera Bitcoin identificará e informará al usuario de cualquier error en un Address receptor, pero no cambiará automáticamente el Address incorrecto. Esta elección está motivada por el hecho de que la integración de la corrección de errores afecta inevitablemente a las capacidades de detección de errores del algoritmo.
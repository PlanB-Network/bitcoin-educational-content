---
term: CHECKSUM
---

La suma de comprobación es un valor calculado a partir de un conjunto de datos, utilizado para verificar la integridad y validez de esos datos durante su transmisión o almacenamiento. Los algoritmos de suma de comprobación están diseñados para detectar errores accidentales o alteraciones no intencionadas de los datos, como errores de transmisión o corrupción de archivos. Existen diferentes tipos de algoritmos de sumas de comprobación, como las comprobaciones de paridad, las sumas de comprobación modulares, las funciones criptográficas Hash o los códigos BCH (*Bose, Ray-Chaudhuri y Hocquenghem*).


En Bitcoin, las sumas de comprobación se utilizan a nivel de aplicación para garantizar la integridad de las direcciones de recepción. Se calcula una suma de comprobación a partir de la carga útil de la Address de un usuario, y luego se añade a esa Address para detectar cualquier error en su entrada. Una suma de comprobación también está presente en las frases de recuperación (mnemónicos).


> ► *Generalmente se acepta utilizar el término inglés "checksum" directamente en francés.*
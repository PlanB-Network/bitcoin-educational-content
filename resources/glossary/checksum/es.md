---
term: CHECKSUM

---
Una suma de comprobación es un valor calculado a partir de un conjunto de datos, utilizado para verificar la integridad y validez de esos datos durante su transmisión o almacenamiento. Los algoritmos de suma de comprobación están diseñados para detectar errores accidentales o alteraciones no intencionadas de los datos, como errores de transmisión o corrupciones de archivos. Existen varios tipos de algoritmos de sumas de comprobación, como las comprobaciones de paridad, las sumas de comprobación modulares, las funciones hash criptográficas o los códigos BCH (*Bose, Ray-Chaudhuri y Hocquenghem*).

En Bitcoin, las sumas de comprobación se utilizan a nivel de aplicación para garantizar la integridad de las direcciones recibidas. Una suma de comprobación se calcula a partir de la carga útil de la dirección de un usuario, y luego se añade a esta dirección para detectar posibles errores durante su entrada. Una suma de comprobación también está presente en las frases de recuperación (mnemotécnicas).

> ► *La traducción al inglés de "somme de contrôle" es "checksum". En general, se acepta utilizar directamente el término "checksum" en francés.*
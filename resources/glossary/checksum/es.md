---
term: CHECKSUM
---

Un checksum es un valor calculado a partir de un conjunto de datos, utilizado para verificar la integridad y validez de esos datos durante su transmisión o almacenamiento. Los algoritmos de checksum están diseñados para detectar errores accidentales o alteraciones no intencionadas de los datos, como errores de transmisión o corrupciones de archivos. Existen varios tipos de algoritmos de checksum, como controles de paridad, checksums modulares, funciones hash criptográficas o códigos BCH (*Bose, Ray-Chaudhuri y Hocquenghem*).

En Bitcoin, los checksums se utilizan a nivel de aplicación para asegurar la integridad de las direcciones de recepción. Un checksum se calcula a partir del payload de la dirección de un usuario, luego se añade a esta dirección para detectar posibles errores durante su ingreso. Un checksum también está presente en las frases de recuperación (mnemotécnico).

> ► *La traducción al inglés de "somme de contrôle" es "checksum". Generalmente se acepta usar directamente el término "checksum" en francés.*
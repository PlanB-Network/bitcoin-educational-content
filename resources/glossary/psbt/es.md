---
term: PSBT

---
Acrónimo de "Transacción Bitcoin Parcialmente Firmada". Es una especificación introducida con BIP174 para estandarizar la forma en que se construyen las transacciones inacabadas en el software relacionado con Bitcoin, como el software de monedero. Una PSBT encapsula una transacción en la que las entradas pueden no estar completamente firmadas. Incluye toda la información necesaria para que un participante firme la transacción sin requerir datos adicionales. Así, un PSBT puede adoptar 3 formas diferentes:


- Una transacción totalmente construida, pero aún no firmada;
- Una transacción parcialmente firmada, en la que algunas entradas están firmadas mientras que otras aún no lo están;
- O una transacción Bitcoin totalmente firmada, que puede convertirse para estar lista para su difusión en la red.

El formato PSBT facilita la interoperabilidad entre diferentes software de monedero y dispositivos de firma (monedero hardware). Actualmente se utiliza la versión 0 del PSBT, definida en BIP174, pero se está proponiendo la versión 2 a través de BIP370.

> ► *La versión 1 del PSBT no existe. Dado que la versión 0 fue la primera, la segunda versión se denominó informalmente versión 2. Ava Chow, autora del BIP370, decidió asignar el número 2 a esta nueva versión para evitar confusiones
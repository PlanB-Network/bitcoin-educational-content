---
term: PSBT
---

Acrónimo de "Partially Signed Bitcoin Transaction" (Transacción de Bitcoin Parcialmente Firmada). Es una especificación introducida con BIP174 para estandarizar la manera en que se construyen las transacciones no finalizadas en software relacionado con Bitcoin, como el software de billetera. Un PSBT encapsula una transacción en la cual las entradas pueden no estar completamente firmadas. Incluye toda la información necesaria para que un participante firme la transacción sin requerir datos adicionales. Así, un PSBT puede adoptar 3 formas diferentes:
* Una transacción completamente construida, pero aún no firmada;
* Una transacción parcialmente firmada, donde algunas entradas están firmadas mientras que otras aún no;
* O una transacción de Bitcoin completamente firmada, que puede ser convertida para estar lista para su difusión en la red.

El formato PSBT facilita la interoperabilidad entre diferentes software de billetera y dispositivos de firma (billetera de hardware). Actualmente, se utiliza la versión 0 del PSBT, como se define en BIP174, pero se está proponiendo la versión 2 a través de BIP370.

> ► *La versión 1 del PSBT no existe. Dado que la versión 0 fue la primera versión, la segunda versión se llamó informalmente versión 2. Ava Chow, quien autorizó BIP370, decidió asignar el número 2 a esta nueva versión para evitar cualquier confusión.*
---
term: BIP0090

definition: Propuesta que simplifica la verificación de activación de antiguos soft forks utilizando la altura del bloque en lugar de la señalización de los mineros.
---
Propuesta para simplificar el proceso de activación de las bifurcaciones suaves anteriores sustituyendo el mecanismo de señalización de los mineros mediante números de versión de bloque por simples comprobaciones de la altura de los bloques. Este cambio eliminaría la necesidad de verificar los 1000 bloques anteriores para la activación de reglas de consenso, reduciendo así la deuda técnica asociada a la implementación de estas horquillas suaves.
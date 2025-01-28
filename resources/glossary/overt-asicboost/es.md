---
term: OVERT ASICBOOST

---
La versión abierta y transparente de AsicBoost. AsicBoost es una técnica de optimización algorítmica utilizada en la minería de Bitcoin. Los mineros que utilizan la versión abierta manipulan el campo `nVersion` del bloque candidato y utilizan esta modificación como un nonce adicional. Este método deja el campo "Nonce" real del bloque sin cambios durante cada intento de hash, reduciendo así los cálculos necesarios para cada SHA256, al mantener algunos datos iguales entre los intentos. Esta versión es detectable públicamente y no oculta sus modificaciones al resto de la red, a diferencia de la versión encubierta de AsicBoost.
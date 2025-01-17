---
term: NVERSION

---
El campo `nVersion` en una transacción Bitcoin se utiliza para indicar la versión del formato de transacción que se está utilizando. Permite a la red distinguir entre diferentes evoluciones del formato de transacción a lo largo del tiempo y aplicar las reglas correspondientes. Este campo no tiene impacto en las reglas de consenso. Esto significa que cualquier valor asignado a este campo no provoca la invalidación de la transacción. Sin embargo, el campo `nVersion` tiene reglas de estandarización que actualmente sólo aceptan los valores `1` y `2`. Por ahora, este campo sólo es útil para la activación del campo `nSequence`.
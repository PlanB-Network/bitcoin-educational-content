---
term: LOCK (.LOCK)

---
Archivo utilizado en Bitcoin Core para bloquear el directorio de datos. Se crea cuando se inicia bitcoind o Bitcoin-qt para evitar que varias instancias del software accedan simultáneamente al mismo directorio de datos. El objetivo es evitar conflictos y corrupción de datos. Si el software se detiene inesperadamente, el archivo .lock puede permanecer y debe ser borrado manualmente antes de reiniciar Bitcoin Core.
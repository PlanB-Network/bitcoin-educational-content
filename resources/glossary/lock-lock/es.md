---
término: LOCK (.LOCK)
---

Archivo utilizado en Bitcoin Core para bloquear el directorio de datos. Se crea cuando bitcoind o Bitcoin-qt se inician para evitar que múltiples instancias del software accedan al mismo directorio de datos simultáneamente. El objetivo es prevenir conflictos y corrupción de datos. Si el software se detiene inesperadamente, el archivo .lock puede permanecer y debe ser eliminado manualmente antes de reiniciar Bitcoin Core.
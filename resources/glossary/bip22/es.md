---
term: BIP22
---

BIP propuesto en 2012 por Luke Dashjr que introduce un método estandarizado JSON-RPC para interfaces de minería externas, llamado "getblocktemplate". Con el aumento en la dificultad de minería, el uso de software externo especializado para producir prueba de trabajo se ha desarrollado. Este BIP propone un estándar de comunicación común para la plantilla de bloque entre nodos completos y software especializado en minería. Este método implica enviar la estructura completa del bloque, en lugar de solo el encabezado, para permitir que el minero lo personalice.
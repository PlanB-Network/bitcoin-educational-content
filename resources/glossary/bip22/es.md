---
term: BIP22

---
BIP propuesto en 2012 por Luke Dashjr que introduce un método JSON-RPC estandarizado para interfaces de minería externas, llamado "getblocktemplate". Con el aumento de la dificultad de la minería, se ha desarrollado el uso de software externo especializado para producir pruebas de trabajo. Este BIP propone un estándar común de comunicación para la plantilla de bloques entre nodos completos y software especializado en minería. Este método consiste en enviar la estructura completa del bloque, en lugar de sólo la cabecera, para permitir al minero personalizarlo.
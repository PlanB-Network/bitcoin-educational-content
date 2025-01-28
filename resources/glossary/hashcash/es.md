---
term: HASHCASH

---
HashCash es un sistema de prueba de trabajo diseñado por Adam Back en 1997 para combatir el spam y los ataques DoS. Se basa en el principio de que un remitente debe realizar una tarea computacional (en concreto, encontrar una colisión parcial en una función hash criptográfica) para demostrar su trabajo. Esta tarea es costosa en términos de tiempo y energía para el remitente, pero la verificación del resultado por parte del destinatario es rápida y sencilla. Este protocolo ha demostrado ser especialmente adecuado para luchar contra el spam en las comunicaciones por correo electrónico, ya que supone una carga mínima para los usuarios legítimos al tiempo que supone un obstáculo importante para los spammers. En efecto, enviar un solo correo electrónico requiere unos segundos de cálculo, pero replicar esta operación millones de veces resulta extremadamente costoso en términos de energía y tiempo, lo que a menudo anula el interés económico de las campañas de spam, ya sean con fines de marketing o malintencionadas. Además, permite preservar el anonimato del remitente.

HashCash fue rápidamente adoptado por los cypherpunks que buscaban desarrollar un sistema de moneda electrónica anónima sin intermediarios. De hecho, la innovación de Adam Back introdujo por primera vez el concepto de escasez en el mundo digital. El concepto de prueba de trabajo se encuentra después en varios sistemas de moneda electrónica anteriores a Bitcoin, entre ellos:


- b-money, de Wei Dai, publicado en 1998;
- R-POW de Hal Finney publicado en 2004;
- BitGold por Nick Szabo publicado en 2005.

El principio de HashCash también se encuentra en el protocolo Bitcoin, donde se utiliza como mecanismo de protección contra los ataques Sybil.
---
term: HASHCASH
---

HashCash es un sistema de prueba de trabajo diseñado por Adam Back en 1997 para combatir el spam y los ataques DoS. Se basa en el principio de que el remitente debe realizar una tarea computacional (específicamente, encontrar una colisión parcial en una función hash criptográfica) para probar su trabajo. Esta tarea es costosa en términos de tiempo y energía para el remitente, pero verificar el resultado por parte del destinatario es rápido y sencillo. Este protocolo ha demostrado ser particularmente adecuado para combatir el spam en las comunicaciones por correo electrónico, ya que es mínimamente gravoso para los usuarios legítimos mientras que representa un obstáculo significativo para los spammers. De hecho, enviar un solo correo electrónico requiere unos pocos segundos de computación, pero replicar esta operación millones de veces se vuelve extremadamente costoso en términos de energía y tiempo, lo que a menudo anula el interés económico de las campañas de spam, ya sean con fines de marketing o maliciosos. Además, permite la preservación del anonimato del remitente.

HashCash fue rápidamente adoptado por los cypherpunks que buscaban desarrollar un sistema de moneda electrónica anónima sin intermediarios. De hecho, la innovación de Adam Back introdujo el concepto de escasez en el mundo digital por primera vez. El concepto de prueba de trabajo se encuentra luego en varios sistemas de moneda electrónica anteriores a Bitcoin, incluyendo:
* b-money de Wei Dai publicado en 1998;
* R-POW de Hal Finney publicado en 2004;
* BitGold de Nick Szabo publicado en 2005.

El principio de HashCash también se encuentra dentro del protocolo de Bitcoin, donde se utiliza como mecanismo de protección contra ataques Sybil.
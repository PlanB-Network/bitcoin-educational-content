---
term: PAGOS MULTITRAYECTO (MPP)
---

Término genérico para todas las técnicas de pago en Lightning que permiten dividir una transacción en varias partes más pequeñas y enrutarlas por rutas diferentes. En otras palabras, cada fracción de pago toma una ruta de nodo diferente. Esto permite eludir las limitaciones de liquidez de un único canal en la ruta.


Los pagos multitrayecto también ofrecen ligeras ventajas en términos de confidencialidad, ya que resulta más difícil para un observador vincular cada fragmento de pago a la transacción completa. Sin embargo, en su versión básica, todos los fragmentos comparten el mismo secreto para los HTLC, lo que puede hacer que la transacción sea rastreable si un observador está presente en varias rutas. Además, como el secreto es único para todas las fracciones del pago, no es atómico. Esto significa que algunas partes del pago pueden ejecutarse con éxito, mientras que otras pueden fallar. Estos inconvenientes se corrigen con el "Pago atómico de rutas múltiples".
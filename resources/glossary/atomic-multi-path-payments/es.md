---
term: PAGOS ATÓMICOS MULTIRRUTA
---

Versión mejorada de MPP (*Multi-Path Payments*) en la que cada fragmento de pago tiene un secreto parcial distinto, lo que garantiza que la transacción se liquide atómicamente, es decir, en su totalidad o no.


Los MPP son técnicas de pago en Lightning que permiten dividir una transacción en varias partes más pequeñas y enrutarlas por rutas diferentes. En otras palabras, cada fracción de pago toma una ruta de nodo diferente. De este modo se eluden las limitaciones de liquidez de un único canal en la ruta. En los MPP básicos, cada fracción de pago comparte el mismo secreto y, por tanto, el mismo Hash en los HTLC. Esto puede hacer que la transacción sea rastreable si un observador está presente en varias rutas, ya que puede enlazar todos estos secretos idénticos. Además, como el secreto es único para todas las partes del pago, no es atómico. Esto significa que algunas partes del pago pueden ejecutarse con éxito, mientras que otras pueden fallar.


En AMP, se utilizan secretos parciales únicos para cada fracción. Una vez recibidos todos los fragmentos, permiten al receptor reconstruir el secreto general original y reclamar el pago completo. Este método hace imposible la liquidación parcial del pago, ya que se requiere la posesión de todos los secretos parciales para desbloquear el pago completo. De este modo se garantiza que el pago sea totalmente exitoso o totalmente fallido (es decir, atómico). AMP también mejora la confidencialidad, puesto que ya no hay vínculos visibles entre las distintas rutas.


Una ventaja de los AMP es que funcionan incluso si sólo el receptor y el remitente han implementado este método. Los nodos intermediarios procesan estos pagos como transacciones convencionales utilizando HTLC, sin saber que están procesando fracciones de un pago mayor.
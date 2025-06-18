---
term: FRAGMENTOS (RAYOS)
---

En el contexto de *Pagos de rutas múltiples (MPP)* o *Pagos de rutas múltiples atómicas (AMP)*, un Shard es una fracción de un pago global. Cada Shard representa una parte del pago total, que se enruta por separado a través de una ruta diferente en Lightning.


En MPP, todos los fragmentos comparten el mismo secreto, mientras que en AMP, cada Shard tiene un secreto parcial único. El receptor agrupa los fragmentos para reconstituir y finalizar el pago completo. Este mecanismo elude las limitaciones de liquidez de un único canal.
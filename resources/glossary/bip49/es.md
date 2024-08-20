---
term: BIP49
---

BIP49 es un BIP informativo que introduce el método de derivación utilizado para generar direcciones Nested SegWit en una cartera HD. La ruta de derivación propuesta sigue los estándares de BIP43 y BIP44, con el índice `49'` (derivación reforzada) en la profundidad del objetivo. Por ejemplo, la primera dirección de una cuenta P2SH-P2WPKH se derivaría de la ruta: `m/49'/0'/0'/0/0`. Los scripts Nested SegWit fueron inventados en el lanzamiento de SegWit para facilitar su adopción. Permiten el uso de este nuevo estándar, incluso en carteras que aún no son compatibles de manera nativa con SegWit.
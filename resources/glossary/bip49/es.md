---
term: BIP49

---
El BIP49 es un BIP informativo que introduce el método de derivación utilizado para generar direcciones SegWit anidadas en un monedero HD. La ruta de derivación propuesta sigue los estándares de BIP43 y BIP44, con el índice `49'` (derivación endurecida) en la profundidad de la meta. Por ejemplo, la primera dirección de una cuenta P2SH-P2WPKH se derivaría de la ruta `m/49'/0'/0'/0/0`. Los scripts SegWit anidados se inventaron en el lanzamiento de SegWit para facilitar su adopción. Permiten el uso de este nuevo estándar, incluso en carteras que aún no son compatibles de forma nativa con SegWit.
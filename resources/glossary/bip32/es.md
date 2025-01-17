---
term: BIP32

---
BIP32 introdujo el concepto de cartera jerárquica determinista (cartera HD). Esta propuesta permite generar una jerarquía de pares de claves a partir de una "semilla maestra" común, utilizando funciones de derivación unidireccionales. Cada par de claves generado puede a su vez ser el padre de otras claves hijas, formando así una estructura arborescente (jerárquica). La ventaja de BIP32 es que permite la gestión de múltiples pares de claves diferentes con la necesidad de mantener una sola semilla para regenerarlas. Esta innovación ha contribuido notablemente a combatir el problema de la reutilización de direcciones, grave para la privacidad de los usuarios. BIP32 también permite crear subcarteras dentro de un mismo monedero para facilitar su gestión.
---
term: BIP0093
---

BIP informativo que propone una norma para guardar y restaurar el seed de una cartera jerárquica determinista (según BIP32) utilizando la clave secreta compartida de Shamir. Este protocolo define el formato "codex32", que se inspira en el formato bech32, introduciendo una cadena estructurada que consta de un prefijo, un parámetro de umbral, un identificador, un índice de compartición, una carga útil y una suma de comprobación (BCH). El método permite dividir el seed en hasta 31 comparticiones, de las cuales se requiere un umbral definido (entre 1 y 9) para la recuperación completa del seed.
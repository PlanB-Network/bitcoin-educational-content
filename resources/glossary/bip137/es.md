---
term: BIP137
---

Propone un formato estandarizado para firmar mensajes con claves privadas de Bitcoin y sus direcciones asociadas, con el fin de probar la propiedad de una dirección. Este BIP busca resolver la ambigüedad relacionada con los diferentes tipos de direcciones de Bitcoin (P2PKH, P2SH, P2WPKH...) al firmar un mensaje. Introduce un método para distinguir explícitamente estos formatos de dirección a través de firmas. Estas firmas son útiles para varias aplicaciones como prueba de fondos, auditorías y otros usos que requieren la autenticación de una dirección a través de su clave privada. BIP322 ha introducido desde entonces un nuevo formato de firma que permite extender este estándar y generalizarlo para cualquier tipo de script.
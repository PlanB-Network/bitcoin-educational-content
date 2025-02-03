---
term: BIP137

---
Propone un formato estandarizado para firmar mensajes con claves privadas Bitcoin y sus direcciones asociadas, con el fin de demostrar la propiedad de una dirección. Este BIP pretende resolver la ambigüedad relacionada con los diferentes tipos de direcciones Bitcoin (P2PKH, P2SH, P2WPKH...) a la hora de firmar un mensaje. Introduce un método para distinguir explícitamente estos formatos de dirección a través de firmas. Estas firmas son útiles para diversas aplicaciones, como la prueba de fondos, la auditoría y otros usos que requieren la autenticación de una dirección a través de su clave privada. Desde entonces, BIP322 ha introducido un nuevo formato de firma que permite ampliar esta norma y generalizarla para cualquier tipo de escritura.
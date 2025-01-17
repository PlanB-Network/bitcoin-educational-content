---
term: BIP11

---
BIP introducido por Gavin Andresen en marzo de 2012 que propone un método estándar para crear transacciones multifirma en Bitcoin. Esta propuesta pretende mejorar la seguridad de los bitcoins exigiendo múltiples firmas para validar una transacción. BIP11 introduce un nuevo tipo de escritura, denominada "M-of-N multisig", donde `M` representa el número mínimo de firmas requeridas de entre `N` claves públicas potenciales. Este estándar utiliza el opcode `OP_CHECKMULTISIG`, ya existente en Bitcoin, pero que anteriormente no cumplía con las normas de estandarización de los nodos. Aunque este tipo de script ya no se utiliza comúnmente para los monederos multisig reales, favoreciendo P2SH o P2WSH, su uso sigue siendo posible. Se utiliza especialmente en meta-protocolos como Stamps. Los nodos pueden, sin embargo, elegir no retransmitir estas transacciones P2MS con el parámetro `permitbaremultisig=0`.

> ► *En la actualidad, esta norma se conoce como "bare-multisig" o "P2MS "*
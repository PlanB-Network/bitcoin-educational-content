---
term: BIP11
---

BIP introducido por Gavin Andresen en marzo de 2012 que propone un método estándar para crear transacciones multisignatura en Bitcoin. Esta propuesta tiene como objetivo mejorar la seguridad de los bitcoins al requerir múltiples firmas para validar una transacción. BIP11 introduce un nuevo tipo de script, denominado "multisig M-de-N", donde `M` representa el número mínimo de firmas requeridas de entre `N` posibles claves públicas. Este estándar utiliza el opcode `OP_CHECKMULTISIG`, ya existente en Bitcoin, pero que anteriormente no cumplía con las reglas de estandarización de los nodos. Aunque este tipo de script ya no se utiliza comúnmente para carteras multisig actuales, prefiriendo P2SH o P2WSH, su uso sigue siendo posible. Se utiliza notablemente en meta-protocolos como Stamps. Sin embargo, los nodos pueden elegir no retransmitir estas transacciones P2MS con el parámetro `permitbaremultisig=0`.

> ► *Hoy en día, este estándar es conocido como "bare-multisig" o "P2MS".*
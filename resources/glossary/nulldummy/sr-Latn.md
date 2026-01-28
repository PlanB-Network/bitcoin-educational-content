---
term: Nulldummy
definition: Pravilo koje zahteva da lažni (dummy) element u OP_CHECKMULTISIG bude prazan niz bajtova.
---

Pravilo konsenzusa uvedeno sa BIP147 u SegWit Soft Fork koje zahteva da dummy element korišćen u `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY` opcode-ovima bude prazan niz bajtova (`OP_0`). Ova mera je implementirana kako bi se eliminisao vektor malleabilnosti zabranom bilo koje vrednosti osim `OP_0` za ovaj element.
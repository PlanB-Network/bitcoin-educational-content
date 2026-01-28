---
term: Nulldummy
definition: Regel som kräver att dummy-elementet i OP_CHECKMULTISIG ska vara en tom byte-array.
---

Samförståndsregel införd med BIP147 i SegWit Soft Fork som kräver att dummyelementet som används i opkoderna `OP_CHECKMULTISIG` och `OP_CHECKMULTISIGVERIFY` ska vara en tom bytearray (`OP_0`). Denna åtgärd infördes för att eliminera en felbarhetsvektor genom att förbjuda alla andra värden än `OP_0` för detta element.
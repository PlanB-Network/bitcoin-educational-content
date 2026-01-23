---
term: BIP0017

definition: Alternativní návrh k P2SH zavádějící opcode OP_CHECKHASHVERIFY, který nakonec nebyl přijat ve prospěch BIP16.
---
Návrh Luka Dashjr, který soutěžil s BIP12 a BIP16. BIP17 zavedl nový opkód `OP_CHECKHASHVERIFY`, který má umožnit ověření skriptu obsaženého v `scriptSig` oproti jeho hashi obsaženému v `scriptPubKey` před odemknutím prostředků. Po období intenzivních diskusí byla nakonec dána přednost BIP16 (P2SH) před BIP17 (CHV).
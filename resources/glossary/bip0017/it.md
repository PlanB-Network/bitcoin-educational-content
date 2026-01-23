---
term: BIP0017

definition: Proposta alternativa a P2SH che introduceva l'opcode OP_CHECKHASHVERIFY, alla fine non adottata a favore di BIP16.
---
Proposta di Luke Dashjr in concorrenza con BIP12 e BIP16. BIP17 ha introdotto un nuovo opcode, `OP_CHECKHASHVERIFY`, progettato per consentire la verifica di uno script presente nella `scriptSig` rispetto al suo hash presente nella `scriptPubKey` prima di sbloccare i fondi. Il BIP16 (P2SH) è stato infine preferito al BIP17 (CHV) dopo un periodo di intensi dibattiti.
---
term: OP_CHECKMULTISIG (0XAE)
definition: Opcode som verifierar att M signaturer av N publika nycklar är giltiga.
---

Kontrollerar flera signaturer mot flera publika nycklar. Som indata används en serie med `N` publika nycklar och `M` signaturer, där `M` kan vara mindre än eller lika med `N`. `OP_CHECKMULTISIG` verifierar om minst `M` signaturer matchar `M` av de `N` publika nycklarna. Observera att på grund av ett historiskt fel som inte är ett enda, tas ytterligare ett element bort från stacken av `OP_CHECKMULTISIG`. Detta element kallas "*dummy element*". För att undvika ett fel i `scriptSig`, inkluderas därför en `OP_0`, som är ett värdelöst element, för att uppfylla borttagningen och kringgå buggen. Sedan BIP147 (introducerad med SegWit 2017) måste det värdelösa elementet som förbrukas på grund av buggen vara `OP_0` för att skriptet ska vara giltigt, eftersom det var en formbarhetsvektor. Denna opcode togs bort i Tapscript.
---
term: OP_CHECKSIGADD (0XBA)
definition: Tapscript-opcode som verifierar en signatur och ökar en räknare om den är giltig.
---

Extraherar de tre översta värdena från stacken: en `public key`, ett `CScriptNum` `n` och en `signature`. Om signaturen inte är den tomma vektorn och inte är giltig, avslutas skriptet med ett fel. Om signaturen är giltig eller är den tomma vektorn (`OP_0`), presenteras två scenarier:


- Om signaturen är den tomma vektorn: ett `CScriptNum` med värdet `n` läggs på stacken och körningen fortsätter;
- Om signaturen inte är en tom vektor och fortfarande är giltig: ett `CScriptNum` med värdet `n + 1` läggs på stacken och körningen fortsätter.

För att förenkla utför `OP_CHECKSIGADD` en operation som liknar `OP_CHECKSIG`, men istället för att lägga true eller false på stacken lägger den till `1` till det andra värdet högst upp på stacken om signaturen är giltig, eller lämnar detta värde oförändrat om signaturen representerar den tomma vektorn. `OP_CHECKSIGADD` gör det möjligt att skapa samma multisignaturpolicyer i Tapscript som med `OP_CHECKMULTISIG` och `OP_CHECKMULTISIGVERIFY` men på ett batchverifierbart sätt, vilket innebär att det tar bort uppslagningsprocessen i verifieringen av en traditionell Multisig och därmed påskyndar verifieringen samtidigt som den operativa belastningen på nodernas processorer minskar. Denna opcode lades till i Tapscript enbart för Taproot:s behov.
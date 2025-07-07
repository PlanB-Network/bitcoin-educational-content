---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Kombinerar en `OP_CHECKMULTISIG` och en `OP_VERIFY`. Det tar flera signaturer och offentliga nycklar för att verifiera att `M` av `N` signaturer är giltiga, precis som `OP_CHECKMULTISIG` gör. Om verifieringen misslyckas stoppas skriptet omedelbart med ett felmeddelande, precis som i `OP_VERIFY`. Om verifieringen lyckas fortsätter skriptet utan att lägga något värde på stacken. Denna opcode togs bort i Tapscript.
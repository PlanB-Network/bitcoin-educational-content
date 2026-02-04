---
term: OP_CHECKSIGVERIFY (0XAD)
definition: Kombinerar OP_CHECKSIG och OP_VERIFY, och stoppar skriptet om signaturen är ogiltig.
---

Utför samma operation som `OP_CHECKSIG`, men om signaturverifieringen misslyckas stoppas skriptet omedelbart med ett felmeddelande och transaktionen är därmed ogiltig. Om verifieringen lyckas fortsätter skriptet utan att lägga ett `1`-värde (sant) på stacken. Sammanfattningsvis utför `OP_CHECKSIGVERIFY` operationen `OP_CHECKSIG` följt av `OP_VERIFY`. Denna opcode modifierades i Tapscript för att verifiera Schnorr-signaturer.
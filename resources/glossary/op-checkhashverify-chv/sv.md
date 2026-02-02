---
term: OP_CHECKHASHVERIFY (CHV)
definition: Opcode föreslagen 2012 för funktioner liknande P2SH, aldrig implementerad.
---

En ny opcode som föreslogs 2012 i BIP17 av Luke Dashjr och som skulle erbjuda samma funktioner som `OP_EVAL` eller P2SH. Den var avsedd att Hash slutet av `scriptSig`, jämföra resultatet med toppen av stacken, och göra transaktionen ogiltig om de två hasharna inte matchade. Denna opcode implementerades aldrig.
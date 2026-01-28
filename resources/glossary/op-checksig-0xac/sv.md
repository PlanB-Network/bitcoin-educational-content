---
term: OP_CHECKSIG (0XAC)
definition: Opcode som verifierar giltigheten av en signatur mot en publik nyckel.
---

Verifierar giltigheten av en signatur mot en given publik nyckel. Den tar de två översta Elements från stacken: signaturen och den publika nyckeln, och utvärderar om signaturen är korrekt för transaktionen Hash och den angivna publika nyckeln. Om verifieringen lyckas lägger den värdet `1` (true) på stacken, annars `0` (false). Denna opcode modifierades i Tapscript för att verifiera Schnorr-signaturer.
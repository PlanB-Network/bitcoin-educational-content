---
term: OP_CHECKSIGADD (0XBA)

---
Henter ut de tre øverste verdiene fra stakken: en `public key`, et `CScriptNum` `n` og en `signature`. Hvis signaturen ikke er den tomme vektoren og ikke er gyldig, avsluttes skriptet med en feilmelding. Hvis signaturen er gyldig eller er den tomme vektoren (`OP_0`), presenteres to scenarier:


- Hvis signaturen er den tomme vektoren: et `CScriptNum` med verdien `n` skyves opp på stakken, og kjøringen fortsetter;
- Hvis signaturen ikke er en tom vektor og fortsatt er gyldig, skyves et `CScriptNum` med verdien `n + 1` opp på stakken, og kjøringen fortsetter.

For å forenkle, utfører `OP_CHECKSIGADD` en operasjon som ligner på `OP_CHECKSIG`, men i stedet for å legge true eller false på stakken, legger den til `1` til den andre verdien øverst i stakken hvis signaturen er gyldig, eller lar denne verdien være uendret hvis signaturen representerer en tom vektor. `OP_CHECKSIGADD` gjør det mulig å opprette de samme multisignaturpolicyene i Tapscript som med `OP_CHECKMULTISIG` og `OP_CHECKMULTISIGVERIFY`, men på en batchverifiserbar måte, noe som betyr at den fjerner oppslagsprosessen i verifiseringen av en tradisjonell multisignatur og dermed gjør verifiseringen raskere, samtidig som den reduserer driftsbelastningen på nodenes CPU-er. Denne opkoden ble lagt til i Tapscript utelukkende for Taproots behov.
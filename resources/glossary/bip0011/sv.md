---
term: BIP0011
definition: Standard som introducerar M-of-N-multisignaturtransaktioner på Bitcoin, i dag känd som bare-multisig eller P2MS.
---

BIP introducerad av Gavin Andresen i mars 2012 som föreslår en standardmetod för att skapa multisignaturtransaktioner på Bitcoin. Detta förslag syftar till att förbättra säkerheten för bitcoins genom att kräva flera signaturer för att validera en transaktion. BIP11 introducerar en ny typ av skript som kallas "M-of-N Multisig", där `M` representerar det minsta antalet signaturer som krävs bland `N` potentiella publika nycklar. Denna standard använder opkoden `OP_CHECKMULTISIG`, som redan finns i Bitcoin, men som tidigare inte var förenlig med nodernas standardiseringsregler. Även om den här typen av skript inte längre används för faktiska Multisig-plånböcker, till förmån för P2SH eller P2WSH, är det fortfarande möjligt att använda den. Det används framför allt i metaprotokoll som Stamps. Noder kan dock välja att inte vidarebefordra dessa P2MS-transaktioner med parametern `permitbaremultisig=0`.


> numera är denna standard känd som "bare-Multisig" eller "P2MS"
---
term: BIP11

---
BIP ble introdusert av Gavin Andresen i mars 2012 og foreslår en standardmetode for å opprette multisignaturtransaksjoner på Bitcoin. Dette forslaget tar sikte på å forbedre sikkerheten til bitcoins ved å kreve flere signaturer for å validere en transaksjon. BIP11 introduserer en ny type skript, kalt "M-of-N multisig", der `M` representerer det minste antallet signaturer som kreves blant `N` potensielle offentlige nøkler. Denne standarden bruker opkoden `OP_CHECKMULTISIG`, som allerede finnes i Bitcoin, men som tidligere ikke var i samsvar med nodenes standardiseringsregler. Selv om denne typen skript ikke lenger er vanlig å bruke for faktiske multisig-lommebøker, til fordel for P2SH eller P2WSH, er det fortsatt mulig å bruke den. Det brukes særlig i metaprotokoller som Stamps. Noder kan imidlertid velge å ikke videresende disse P2MS-transaksjonene med parameteren `permitbaremultisig=0`.

> i dag er denne standarden kjent som "bare-multisig" eller "P2MS"
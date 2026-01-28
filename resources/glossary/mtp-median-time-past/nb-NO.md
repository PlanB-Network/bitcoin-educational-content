---
term: MTP (median time past)

definition: Medianen av tidsstemplene til de siste 11 blokkene, som fungerer som tidsreferanse for nettverket.
---
Dette konseptet brukes i Bitcoin-protokollen for å bestemme en margin på nettverkets konsensus-tidsstempel. MTP er definert som medianen av tidsstemplene for de siste 11 utvunnede blokkene. Bruken av denne indikatoren bidrar til å unngå uenigheter mellom noder om det nøyaktige tidspunktet i tilfelle uoverensstemmelser. MTP ble opprinnelig brukt til å verifisere gyldigheten av blokkenes tidsstempler i forhold til fortiden. Siden BIP113 har den også blitt brukt som referanse for nettverkstid for å verifisere gyldigheten av tidslåsingstransaksjoner (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` og `OP_CHECKSEQUENCEVERIFY`).
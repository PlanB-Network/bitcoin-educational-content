---
term: GJENBRUK AV ADRESSE (INT)

---
Gjenbruk av adresser sies å være "internt" når det forekommer innenfor samme transaksjon både som input og output. I denne konfigurasjonen er intern gjenbruk av adresser en heuristikk for blokkjedeanalyse som muliggjør en plausibel hypotese om transaksjonens endring. Hvis det finnes to utganger, og en av dem bruker samme mottakeradresse som inngangen, er det sannsynlig at den andre utgangen forlater den opprinnelige brukerens besittelse. Utdataene med den gjenbrukte adressen representerer sannsynligvis endringen.

![](../../dictionnaire/assets/10.webp)
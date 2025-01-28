---
term: BIP32

---
BIP32 introduserte konseptet med en hierarkisk deterministisk lommebok (HD-lommebok). Dette forslaget gjør det mulig å generere et hierarki av nøkkelpar fra et felles "master seed" ved hjelp av enveis avledningsfunksjoner. Hvert genererte nøkkelpar kan selv være forelder til andre underordnede nøkler, slik at det dannes en trelignende (hierarkisk) struktur. Fordelen med BIP32 er at den gjør det mulig å administrere flere ulike nøkkelpar, samtidig som det bare er nødvendig å oppbevare ett enkelt frø for å generere dem på nytt. Denne nyvinningen har bidratt til å bekjempe problemet med gjenbruk av adresser, noe som er alvorlig for brukernes personvern. BIP32 gjør det også mulig å opprette undergrener innenfor samme lommebok for å gjøre det enklere å administrere den.
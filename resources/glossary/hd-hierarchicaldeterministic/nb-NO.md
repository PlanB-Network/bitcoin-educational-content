---
term: HD (HIERARKISK-DETERMINISTISK)

---
Refererer til en Bitcoin-lommebok som bruker en unik informasjon (seed) til å generere en rekke offentlige og private nøkkelpar på en sekvensiell og reproduserbar måte. Denne metoden for å håndtere nøkler er definert av BIP32-standarden. Den største fordelen med HD-lommebøker er at de gjør det mulig for brukerne å ha en rekke ulike nøkkelpar, særlig for å unngå gjenbruk av adresser, samtidig som de kan regenerere dem alle fra én enkelt informasjon. Denne strukturen beskrives som hierarkisk fordi den gjør det mulig å skape en trelignende organisering av flere nøkler og adresser fra ett enkelt seed. Og den er deterministisk i den forstand at hvert seed alltid genererer den samme sekvensen av nøkler i alle lommebøker som følger dette systemet.
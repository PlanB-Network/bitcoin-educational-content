---
term: ADRESSE GJENBRUK

---
Gjenbruk av adresser refererer til praksisen med å bruke den samme mottakeradressen til å blokkere flere UTXO-er, noen ganger i flere forskjellige transaksjoner. Bitcoins låses vanligvis ved hjelp av et kryptografisk nøkkelpar som tilsvarer en unik adresse. Siden blokkjeden er offentlig, er det enkelt å se hvilke adresser som er knyttet til hvor mange bitcoins. Ved gjenbruk av samme adresse for flere betalinger er det rimelig å tenke seg at alle de tilknyttede UTXO-ene tilhører samme enhet. Derfor utgjør gjenbruk av adresser et problem for brukerens personvern. Det gir mulighet for deterministiske koblinger mellom flere transaksjoner og UTXO-er, i tillegg til at det opprettholder sporing av fond i kjeden. Satoshi Nakamoto nevnte allerede dette problemet i hvitboken sin:

> "Som en ekstra brannmur kan man bruke et nytt nøkkelpar for hver transaksjon, slik at de ikke kan knyttes til en felles eier*." - Nakamoto, S. (2008). "Bitcoin: Et elektronisk peer-to-peer-kontantsystem". Konsultert på https://bitcoin.org/bitcoin.pdf.
For å bevare personvernet på et minimum, anbefales det på det sterkeste å bruke hver mottakeradresse bare én gang. For hver ny betaling er det hensiktsmessig å generere en ny adresse. For endringsutganger bør det også brukes en ny adresse. Takket være deterministiske og hierarkiske lommebøker er det heldigvis blitt svært enkelt å bruke en rekke adresser. Alle nøkkelpar som er knyttet til en lommebok, kan enkelt regenereres fra seed. Dette er også grunnen til at lommebokprogramvaren alltid genererer en ny, annerledes adresse når du klikker på "Receive"-knappen.

> på engelsk kalles det "Address Reuse"
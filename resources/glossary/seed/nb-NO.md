---
term: SEED

---
I den spesifikke konteksten til en hierarkisk deterministisk Bitcoin-lommebok er et seed en 512-biters informasjonsbit som er avledet fra tilfeldigheter. Det brukes til å generere et sett med private nøkler og tilhørende offentlige nøkler for en Bitcoin-lommebok på en deterministisk og hierarkisk måte. Frøet forveksles ofte med selve gjenopprettingsfrasen. Det er imidlertid forskjellig informasjon. Frøet fås ved å bruke `PBKDF2`-funksjonen på den mnemoniske frasen og enhver potensiell passordfrase.

Frøet ble oppfunnet med innføringen av BIP32, som definerer grunnlaget for den hierarkiske, deterministiske lommeboken. I denne standarden var seed 128 bits. Dette gjør det mulig å utlede alle nøklene i en lommebok fra én enkelt informasjon, i motsetning til JBOK-lommebøker (*Just a Bunch Of Keys*), som krever nye sikkerhetskopier for hver genererte nøkkel. BIP39 introduserte senere en koding av dette frøet for å gjøre det enklere for mennesker å lese det. Denne kodingen gjøres i form av en frase, ofte kalt en mnemonisk frase eller gjenopprettingsfrase. Denne standarden bidrar til å unngå feil i sikkerhetskopieringen av seed, blant annet gjennom bruk av en sjekksum.

I kryptografi er et seed et stykke tilfeldig data som brukes som utgangspunkt for å generere kryptografiske nøkler, krypteringer eller pseudotilfeldige sekvenser. Kvaliteten og sikkerheten til mange kryptografiske prosesser avhenger av hvor tilfeldig og konfidensielt seed er.

> den engelske oversettelsen av "graine" er "frø". På fransk bruker mange det engelske ordet direkte om frøet
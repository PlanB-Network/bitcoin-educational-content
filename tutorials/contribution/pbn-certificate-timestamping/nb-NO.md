---
name: Tidsstempling av Plan ₿ Network-sertifikater og diplomer
description: Forstå hvordan Plan ₿ Network utsteder verifiserbart bevis for ditt sertifikat og diplom
---

![cover](assets/cover.webp)

Hvis du leser dette, er det stor sannsynlighet for at du har mottatt enten et Bitcoin-sertifikat eller et fullføringsdiplom for et av kursene du har gjort på Plan ₿ Network, så gratulerer med denne prestasjonen!

I denne veiledningen skal vi se hvordan Plan ₿ Network utsteder verifiserbare bevis for ditt Bitcoin-sertifikat eller ethvert fullføringsdiplom for kurs. Deretter, i en andre del, vil vi se hvordan man kan verifisere ektheten av disse bevisene.

# Plan ₿ Networks bevismekanisme

Hos Plan ₿ Network tilbyr vi deg et sertifikat og diplomer som er kryptografisk signert av oss, og tidsstemplet på Timechain (dvs. Bitcoin-blockchainen). For å oppnå dette måtte vi komme opp med en bevismekanisme som stoler på 2 kryptografiske operasjoner:

1. En GPG-signatur på en tekstfil som oppsummerer dine prestasjoner
2. Tidsstempling av denne signerte filen via [opentimestamps](https://opentimestamps.org/).

I utgangspunktet lar den første operasjonen deg verifisere hvem som utstedte sertifikatet (eller diplomet), mens den andre lar deg verifisere når det ble utstedt.
Vi tror at denne enkle bevismekanismen gjør det mulig for oss å utstede sertifikat og diplom med ubestridelige bevis som hvem som helst kan verifisere på egen hånd.

![image](./assets/proof-mechanism.webp)

Merk at takket være denne bevismekanismen vil ethvert forsøk på å endre selv den minste detalj av ditt sertifikat eller diplom skape en helt annen sha256-hash av den signerte filen, noe som umiddelbart ville avsløre manipulering fordi signaturen og tidsstemplingen ikke ville være gyldige lenger. Videre, hvis noen forsøker å forfalske noen sertifikater eller diplomer på vegne av Plan ₿ Network, ville en enkel verifisering av signaturen avsløre svindelen.

## Hvordan fungerer GPG-signaturen?

GPG-signaturen oppnås med bruk av en åpen kildekode-programvare kalt GNU Private Guard. Denne programvaren lar hvem som helst enkelt opprette private nøkler, signere og verifisere signaturer og også kryptere og dekryptere filer. For dette veiledningens omfang, vit at Plan ₿ Network bruker GPG for å opprette sin private/offentlige nøkkel og for å signere ethvert Bitcoin-sertifikat eller fullføringsdiplom for kurs.

På den annen side, hvis noen ønsker å verifisere ektheten av en signert fil, kan de bruke GPG for å importere utstederens offentlige nøkkel og verifisere. I den andre delen av veiledningen vil vi se hvordan man gjør dette med en terminal.

For de som er nysgjerrige og ønsker å lære mer om denne fantastiske programvaren, kan dere referere til ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## Hvordan fungerer tidsstempling?

Hvem som helst kan bruke OpenTimestamps for å tidsstemple en fil, og oppnå et verifiserbart bevis på filens eksistens. Med andre ord, det gir deg ikke et bevis på når filen ble opprettet, men et bevis på eksistens ikke senere enn et bestemt øyeblikk.
OpenTimestamps er i stand til å tilby denne tjenesten gratis takket være en svært effektiv måte å lagre slikt bevis i Bitcoin Blockchain. Det bruker sha256-hashen av filen som en unik identifikator for filen din og bygger et merkeltre med andre hasher av innsendte filer fra andre brukere og forankrer kun hashen av Merkle-trestrukturen i en OpReturn-transaksjon.
Når denne transaksjonen er i en blokk, kan hvem som helst med den opprinnelige filen og `.ots`-filen som er tilknyttet den, verifisere ektheten av tidsstemplingen. I den andre delen av opplæringen vil vi se hvordan du kan verifisere ditt Bitcoin-sertifikat eller ethvert diplom for kursgjennomføring med en terminal og med et grafisk grensesnitt via nettstedet til OpenTimestamps.

# Hvordan verifisere et Plan ₿ Network-sertifikat eller diplom

## Steg 1. Last ned ditt sertifikat eller diplom

Logg inn på ditt personlige PBN-dashboard.

![image](./assets/login.webp)

Gå til legitimasjonssiden ved å klikke på menyen på venstre side, og velg din eksamensøkt eller ditt diplom for kursgjennomføring.

![image](./assets/credential.webp)

Last ned zip-filen.

![image](./assets/download.webp)

Pakk ut innholdet ved å høyreklikke på `.zip`-filen og velge "Pakk ut". Du vil finne tre forskjellige filer inni:

- Signert tekstfil (f.eks., certificate.txt)
- Åpen tidsstempelfil (OTS) (f.eks., certificate.txt.ots)
- PDF-sertifikat (f.eks., certificate.pdf)

## Steg 2: Verifisering av signaturen til tekstfilen

Åpne først en terminal i mappen der filene er (høyreklikk på mappens vindu og klikk på "Åpne i terminal"). Følg deretter instruksjonene nedenfor

1. Importer Plan ₿ Networks offentlige PGP-nøkkel med følgende kommando:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

Du bør se en melding som følgende hvis du har importert PGP-nøkkelen vellykket

```
gpg: nøkkel 8F12D0C63B1A606E: offentlig nøkkel "PlanB Network (brukt for PBN-plattformen) <admin@planb.network>" importert
gpg: Totalt antall behandlet: 1
gpg:               importert: 1
```

MERK: hvis du ser at 1 nøkkel er behandlet og 0 importert, mest sannsynlig har du allerede importert samme nøkkel tidligere, og det er greit.

2. Verifiser signaturen til sertifikatet eller diplomet med følgende kommando:

```bash
gpg --verify certificate.txt
```

Denne kommandoen bør vise deg detaljer om signaturen, inkludert:

- Hvem som signerte den (Plan ₿ Network)
- Når den ble signert
- Om signaturen er gyldig

Dette er et eksempel på resultatet:

```
gpg: Signatur laget man 11 nov 2024, 00:39:04 CET
gpg:                ved bruk av RSA-nøkkel 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                utsteder "admin@planb.network"
gpg: God signatur fra "PlanB Network (brukt for PBN-plattformen) <admin@planb.network>" [ukjent]
```

Hvis du ser en melding som "DÅRLIG signatur", betyr det at filen har blitt manipulert.

## Steg 3: Verifisering av den åpne tidsstempelet

### Verifisering via et grafisk grensesnitt

1. Besøk OpenTimestamps-nettstedet: https://opentimestamps.org/
2. Klikk på "Stamp & Verify"-fanen.
3. Dra og slipp OTS-filen (f.eks., `certificate.txt.ots`) inn i det angitte området.
4. Dra og slipp den tidsstemplede filen (f.eks. `certificate.txt`) inn i det angitte området.
5. Nettstedet vil automatisk verifisere det åpne tidsstempelet og vise resultatet.

Hvis du ser en melding som følgende er tidsstempelet ditt gyldig:
![cover](assets/opentimestamp_wegui_verified.webp)

### CLI Metode

MERK: denne prosedyren **vil kreve at en lokal Bitcoin-node kjører**

1. Installer OpenTimestamps-klienten fra det offisielle repositoriet: https://github.com/opentimestamps/opentimestamps-client ved å kjøre følgende kommando:

```
pip install opentimestamps-client
```

2. Naviger til mappen som inneholder de utpakkede sertifikatfilene.

3. Kjør følgende kommando for å verifisere det åpne tidsstempelet:

```
ots verify certificate.txt.ots
```

Denne kommandoen vil:

- Sjekke tidsstempelet mot Bitcoins blokkjede
- Vise deg nøyaktig når filen ble tidsstemplet
- Bekrefte tidsstempelets autentisitet

### Endelige resultater

Merk at verifiseringen er vellykket hvis følgende **begge** meldinger vises:

1. GPG-signaturen rapporteres som **"God signatur fra Plan ₿ Network"**
2. OpenTimestamps-verifiseringen viser et spesifikt Bitcoin-blokk-tidsstempel og rapporterer **"Suksess! Bitcoin-blokk [blokkhøyde] bekrefter at data eksisterte per [tidsstempel]"**

Nå som du vet hvordan Plan ₿ Network utsteder verifiserbart bevis for ethvert Bitcoin-sertifikat og diplom for kursgjennomføring, kan du enkelt verifisere integriteten til det.


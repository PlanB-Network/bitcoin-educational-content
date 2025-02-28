---
name: Noeud Bitcoin Core (mac & windows)
description: Installer Bitcoin Core på Mac eller Windows
---

Å installere Bitcoin Core på din vanlige datamaskin kan gjøres, men det er ikke ideelt. Hvis du ikke har noe imot å la datamaskinen din være på 24/7, så vil dette fungere fint. Hvis du trenger å slå av datamaskinen, blir det irriterende å vente på at programvaren skal synkronisere hver gang du slår den på igjen.

Disse instruksjonene er for Mac- eller Windows-brukere. Linux-brukere vil mest sannsynlig ikke trenge min hjelp, men instruksjonene for Linux er veldig like de for Mac.

## Start Clean

Ideelt sett vil du bruke en ren datamaskin, en uten skadelig programvare. Selv om du bruker en maskinvare-lommebok, kan skadelig programvare lure deg til å miste myntene dine.

Du kan enten tørke en gammel datamaskin ren og bruke den som en dedikert Bitcoin-datamaskin, eller kjøpe en dedikert datamaskin/laptop.

## Harddisken

Bitcoin Core vil ta opp omtrent 400 gigabyte med data på disken din, og vil fortsette å vokse. Du kan bruke din interne disk, men du kan også koble til en ekstern harddisk. Jeg vil forklare begge alternativene. Ideelt sett bør du bruke en solid-state drive (SSD). Hvis du har en gammel datamaskin, har den sannsynligvis ikke en av disse internt. Kjøp bare en 1 eller 2 terabyte ekstern SSD og bruk den. Den vanlige disken vil sannsynligvis fungere, men du kan ende opp med å ha problemer, og det vil være mye tregere.

![image](assets/1.webp)

## Last ned Bitcoin Core

Gå til bitcoin.org (sørg for at du ikke går til bitcoin.com, som er en shitcoin-side eid av Roger Ver, som lurer folk til å kjøpe Bitcoin Cash i stedet for Bitcoin)

Når du er der, er det merkelig nok ikke åpenbart hvor du får programvaren. Gå til ressursmenyen og klikk på "Bitcoin Core", som vist nedenfor:

![image](assets/2.webp)

Dette vil ta deg til nedlastingssiden:

![image](assets/3.webp)

Klikk på den oransje knappen Last ned Bitcoin Core:

![image](assets/4.webp)

Det er flere alternativer å velge mellom, avhengig av datamaskinen din. De to første er relevante for denne guiden; velg Windows eller Mac på venstre stolpe. Den vil begynne å laste ned etter at du klikker på den, mest sannsynlig til din Nedlastinger-mappe.

## Verifiser nedlastingen (del 1)

Du trenger filen som inneholder hashene av forskjellige utgivelser. Denne filen pleide å være på nedlastingssiden til bitcoin.org, men har nå flyttet til bitcoincore.org/en/download:

![image](assets/5.webp)

Du trenger SHA256 binære hasher-filen. Denne filen inneholder SHA256-hashene av de forskjellige nedlastingspakkene til Bitcoin Core.

Neste, vi trenger å hashe Bitcoin Core-nedlastingen og sammenligne den med hva filen sier hashen skal være. Da vet vi at nedlastingen er identisk med det som er forventet, ifølge bitcoincore.org.

Naviger til Nedlastinger-mappen igjen og utfør denne kommandoen (erstatt X-ene med det fulle noden bitcoin nedlastingsfilnavnet nøyaktig):

```bash
shasum -a 256 XXXXXXXXXXXX # <--- FOR MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- FOR WINDOWS
```

Du vil få en hash-utdata. Noter den, og sammenlign den med hashen som er inneholdt i SHA256SUMS-filen.

Hvis utdataene er identiske, da har du verifisert at ingen bit av data har blitt tuklet med... nesten. Vi må fortsatt være sikre på at SHA256SUMS-filen ikke er ondsinnet.

For å fortsette med neste steg, må vi ha gpg installert på vår datamaskin.
For å gjøre det, se min SHA256/gpg-guide, og scroll omtrent halvveis til "Download gpg"-seksjonen, og se etter underoverskriften for ditt operativsystem. Kom deretter tilbake hit.
## Få tak i den offentlige nøkkelen

Tilbake på nedlastingssiden, få tak i SHA256 hash signaturfilen

![bilde](assets/6.webp)

Klikk på den og lagre filen på disken, helst i Nedlastingsmappen.

Denne filen inneholder signaturer fra forskjellige personer, av SHA256SUMS-filen.

Vi ønsker å ha hovedutviklerens offentlige nøkkel, Wladimir J. van der Laan, på vår datamaskins nøkkelring. Hans offentlige nøkkel-ID er:
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Kopier den teksten inn i følgende kommando:

```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```

Av interesse, når som helst, kan du se hvilke nøkler som er i datamaskinens nøkkelring med denne kommandoen:

```bash
gpg --list-keys
```

## Verifiser nedlastingen (del 2)

Vi har den offentlige nøkkelen, så vi kan nå verifisere SHA256SUMS-filen som inneholder hashene til Bitcoin Core-nedlastingen, og signaturen for disse hashene.

Åpne Terminal eller CMD igjen, og sørg for at du er i Nedlastingsmappen. Derfra, kjør denne kommandoen:

```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```

Den første oppførte filen er den eksakte stavemåten av signaturfilen. Den andre oppførte filen bør være den eksakte stavemåten av tekstfilen som inneholder hashene. Begge filene bør være i samme mappe, og du må være i mappen til filene, ellers må du skrive ut den fulle banen for hver fil.

Dette er utdataene du bør få

![bilde](assets/7.webp)

Det er trygt å ignorere WARNING-meldingen – det er bare en påminnelse om at du ikke har møtt Wladimir personlig og spurt ham hva hans offentlige nøkkel var, og deretter fortalt datamaskinen din å stole fullstendig på denne nøkkelen.

Hvis du fikk denne meldingen, vet du nå at SHA256SUMS.asc-filen ikke har blitt tuklet med etter at Wladimir signerte den.

## Installer Bitcoin Core

Du burde ikke trenge detaljerte instruksjoner om hvordan du installerer programmet.

![bilde](assets/8.webp)

## Kjør Bitcoin Core

På en Mac, kan du få en advarsel (Apple er fortsatt anti-Bitcoin)

![bilde](assets/9.webp)

Klikk OK, og åpne deretter Systemvalg

![bilde](assets/10.webp)

Klikk på Sikkerhet og Personvern-ikonet:

![bilde](assets/11.webp)

Deretter klikker du på "åpne uansett":

![bilde](assets/12.webp)

Feilen vil dukke opp igjen, men denne gangen vil du ha en ÅPNE-knapp tilgjengelig. Klikk på den.

![bilde](assets/13.webp)

Bitcoin Core bør laste, og du vil bli presentert med noen valg:

![bilde](assets/14.webp)

Her kan du velge å bruke standardbanen for hvor blockchain vil bli lastet ned til, eller du kan velge din eksterne stasjon. Jeg anbefaler å ikke endre standardbanen hvis du skal bruke den interne stasjonen, det gjør ting enklere å sette opp når du installerer annen programvare for å kommunisere med Bitcoin Core.
Du kan velge å kjøre en beskåret node, det sparer plass, men begrenser hva du kan gjøre med noden din. Uansett vil du laste ned hele blokkjeden og verifisere den, så hvis du har plassen, behold det du lastet ned, og ikke beskjær hvis du kan unngå det.
Når du bekrefter, vil blokkjeden begynne å lastes ned. Det vil ta mange dager.

![bilde](assets/15.webp)

Du kan slå av datamaskinen og komme tilbake for å fortsette nedlastingen hvis du vil, det vil ikke forårsake noen skade.
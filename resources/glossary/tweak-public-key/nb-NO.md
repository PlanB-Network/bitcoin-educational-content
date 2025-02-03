---
term: TWEAK (OFFENTLIG NØKKEL)

---
Innenfor kryptografi innebærer "tweaking" av en offentlig nøkkel at man endrer denne nøkkelen ved å bruke en additiv verdi kalt "tweak", slik at den forblir brukbar med kjennskap til den opprinnelige private nøkkelen og tweaken. Teknisk sett er en tweak en skalarverdi som legges til den opprinnelige offentlige nøkkelen. Hvis $P$ er den offentlige nøkkelen og $t$ er justeringen, blir den justerte offentlige nøkkelen

$$
P' = P + tG
$$

Hvor $G$ er generatoren til den elliptiske kurven som brukes. Denne operasjonen gjør det mulig å få en ny offentlig nøkkel avledet fra den opprinnelige nøkkelen, samtidig som den beholder visse kryptografiske egenskaper som gjør den brukbar. Denne metoden brukes for eksempel for Taproot-adresser (P2TR) for å gjøre det mulig å bruke penger enten ved å presentere en Schnorr-signatur på tradisjonell måte eller ved å oppfylle en av betingelsene som er angitt i et Merkle-tre, også kalt "MAST".

![](../../dictionnaire/assets/26.webp)
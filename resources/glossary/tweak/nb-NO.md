---
term: TWEAK
---

I kryptografi betyr å "tweake" en offentlig nøkkel å modifisere den ved hjelp av en additiv verdi som kalles en "tweak", slik at den forblir brukbar med kjennskap til både den opprinnelige private nøkkelen og tweaken. Teknisk sett er en tweak en skalarverdi som legges til den opprinnelige offentlige nøkkelen. Hvis $P$ er den offentlige nøkkelen og $t$ er justeringen, blir den justerte offentlige nøkkelen :


$$
P' = P + tG
$$


Hvor $G$ er generatoren til den elliptiske kurven som brukes. Denne operasjonen produserer en ny offentlig nøkkel avledet fra den opprinnelige, samtidig som den beholder visse kryptografiske egenskaper som gjør at den kan brukes. Denne metoden brukes for eksempel for Taproot-adresser (P2TR), for å muliggjøre bruk enten ved å presentere en Schnorr-signatur på tradisjonell måte, eller ved å oppfylle et av vilkårene som er angitt i en Merkle Tree, også kjent som en "MAST".
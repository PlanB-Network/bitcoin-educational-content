---
term: FORELDET (BLOKK)

---
Refererer til en blokk uten barn: en gyldig blokk, men ekskludert fra Bitcoin-hovedkjeden. Det oppstår når to utvinnere finner en gyldig blokk på samme kjedehøyde i løpet av kort tid og kringkaster den over nettverket. Noder velger til slutt bare én blokk som skal inkluderes i kjeden, i henhold til prinsippet om kjeden med mest akkumulert arbeid, noe som gjør den andre "foreldet". Prosessen som fører til produksjon av en foreldet blokk, er som følger:


- To utvinnere finner en gyldig blokk i samme kjedehøyde i løpet av et kort tidsintervall. La oss kalle dem "blokk A" og "blokk B";
- Hver sender sin blokk til Bitcoin-nodenettverket. Hver node har nå to blokker i samme høyde. Derfor er det to gyldige kjeder;
- Utvinnerne fortsetter å lete etter arbeidsbevis for de neste blokkene, men da må de nødvendigvis bare velge én blokk mellom blokk A og blokk B som de vil utvinne;
- En gruvearbeider finner til slutt en gyldig blokk over `Blokk B`. La oss kalle den `Blokk B+1`;
- De sender `Blokk B+1` til nettverksnodene;
- Siden nodene følger den lengste kjeden (med mest akkumulert arbeid), vil de anslå at `Kjede B` er den som skal følges;
- De vil forlate `Blokk A` som ikke lenger er en del av hovedkjeden. Den har dermed blitt en foreldet blokk.

![](../../dictionnaire/assets/9.webp)

> ► * På engelsk kalles det en "Stale Block". På fransk kan det også kalles "bloc périmé" eller "bloc abandonné". Selv om jeg ikke er enig i denne bruken, bruker noen bitcoinere begrepet "bloc orphelin" for å referere til det som faktisk er en foreldet blokk*
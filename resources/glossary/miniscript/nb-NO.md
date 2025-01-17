---
term: MINISCRIPT

---
Rammeverk utviklet for å tilby et rammeverk for sikker programmering av skript på Bitcoin. Bitcoins eget språk kalles script. Det er ganske komplisert å bruke i praksis, spesielt for sofistikerte og tilpassede applikasjoner. Fremfor alt er det svært vanskelig å verifisere et skripts begrensninger. Miniscript bruker en delmengde av Bitcoin-skript for å forenkle oppretting, analyse og verifisering. Hvert miniscript tilsvarer 1 for 1 med et opprinnelig script. Det brukes et brukervennlig policyspråk, som deretter kompileres til miniscript, slik at det til slutt tilsvarer et opprinnelig skript.

![](../../dictionnaire/assets/30.webp)

Miniscript gjør det dermed mulig for utviklere å bygge sofistikerte skript på en tryggere og mer pålitelig måte. De viktigste egenskapene til Miniscript er som følger:


- Det gjør det mulig å foreta en statisk analyse av skriptet, inkludert hvilke utgiftsbetingelser det tillater, og hva det koster i form av ressurser;
- Det gjør det mulig å lage skript som følger konsensus;
- Det gjør det mulig å analysere om de ulike utgiftsrutinene er i samsvar med nodenes standardregler eller ikke;
- Den etablerer en generell standard som er forståelig og komponerbar for all lommebokprogramvare og -maskinvare.

Miniscript-prosjektet ble lansert i 2018 av Peter Wuille, Andrew Poelstra og Sanket Kanjalkar gjennom selskapet Blockstream. Miniscript ble lagt til i Bitcoin Core-lommeboken i watch-only-modus i desember 2022 med versjon 24.0, og deretter fullt ut i mai 2023 med versjon 25.0.
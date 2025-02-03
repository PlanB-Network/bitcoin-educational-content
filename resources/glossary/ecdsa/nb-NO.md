---
term: ECDSA

---
Forkortelse for "Elliptic Curve Digital Signature Algorithm" Det er en digital signaturalgoritme basert på elliptisk kurvekryptografi (ECC). Det er en variant av DSA (Digital Signature Algorithm). ECDSA utnytter egenskapene til elliptiske kurver for å oppnå sikkerhetsnivåer som kan sammenlignes med tradisjonelle offentlige nøkkelalgoritmer, for eksempel RSA, samtidig som nøkkelstørrelsen er betydelig mindre. ECDSA gjør det mulig å generere nøkkelpar (offentlige og private nøkler) samt å opprette og verifisere digitale signaturer.

I forbindelse med Bitcoin brukes ECDSA til å utlede offentlige nøkler fra private nøkler. Den brukes også til å signere transaksjoner, for å tilfredsstille et skript for å låse opp bitcoins og bruke dem. Den elliptiske kurven som brukes i Bitcoins ECDSA er `secp256k1`, definert av ligningen $y^2 = x^3 + 7$. Denne algoritmen har blitt brukt siden starten av Bitcoin i 2009. I dag deler den plass med Schnorr-protokollen, en annen digital signaturalgoritme som ble introdusert med Taproot i 2021.
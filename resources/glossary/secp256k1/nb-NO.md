---
term: SECP256K1

---
Navnet på en spesifikk elliptisk kurve som brukes i Bitcoin-protokollen for implementeringen av ECDSA (*Elliptic Curve Digital Signature Algorithm*) og Schnorr digitale signaturalgoritmer. Kurven "secp256k1" ble valgt av oppfinneren av Bitcoin, Satoshi Nakamoto. Den har noen interessante egenskaper, særlig ytelsesfordeler.

Bruken av `secp256k1` i Bitcoin betyr at hver private nøkkel (et tilfeldig 256-biters tall) mappes til en tilsvarende offentlig nøkkel gjennom addisjon og dobling av den private nøkkelens punkt med `secp256k1`-kurvens generatorpunkt. Denne operasjonen er enkel å utføre i én retning, men praktisk talt umulig å reversere, noe som danner grunnlaget for sikkerheten til digitale signaturer på Bitcoin.

Kurven `secp256k1` er spesifisert ved den elliptiske kurvelikningen $y^2 = x^3 + 7$, noe som betyr at den har koeffisientene $a$ lik $0$ og $b$ lik $7$ i den generelle formen til en elliptisk kurvelikning $y^2 = x^3 + ax + b$. `secp256k1` er definert over et endelig felt hvis orden er et veldig stort primtall, nærmere bestemt $p = 2^{256} - 2^{32} - 977$. Kurven har også en gruppeorden, som er antallet distinkte punkter på kurven, et forhåndsdefinert generatorpunkt (eller punkt $G$), som brukes i kryptografiske operasjoner for å generere nøkkelpar, og en cofaktor lik $1$.

> "SEC" står for "Standards for Efficient Cryptography" (standarder for effektiv kryptografi). "P256" indikerer at kurven er definert over et felt $\mathbb{Z}_p$ der $p$ er et 256-biters primtall. "K" refererer til navnet på oppfinneren, Neal Koblitz. Til slutt indikerer "1" at dette er den første versjonen av denne kurven
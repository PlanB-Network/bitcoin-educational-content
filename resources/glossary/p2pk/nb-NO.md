---
term: P2PK

---
P2PK står for *Pay to Public Key*. Det er en standard skriptmodell som brukes på Bitcoin for å etablere utgiftsbetingelser på en UTXO. Det gjør det mulig å låse bitcoins direkte til en offentlig nøkkel, i stedet for en adresse.

Teknisk sett inneholder P2PK-skriptet en offentlig nøkkel og en instruksjon som krever en tilsvarende digital signatur for å låse opp midlene. Når eieren ønsker å bruke bitcoinsene, må han eller hun oppgi en signatur som er produsert med den tilhørende private nøkkelen. Signaturen verifiseres ved hjelp av ECDSA (*Elliptic Curve Digital Signature Algorithm*). P2PK ble ofte brukt i de tidlige versjonene av Bitcoin, særlig av Satoshi Nakamoto. Den brukes nesten ikke lenger i dag.
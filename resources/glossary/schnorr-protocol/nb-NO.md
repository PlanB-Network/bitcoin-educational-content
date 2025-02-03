---
term: SCHNORR (PROTOKOLL)

---
Schnorr-protokollen er en elektronisk signaturalgoritme basert på elliptisk kurvekryptografi (ECC). Den brukes i Bitcoin til å utlede en offentlig nøkkel fra en privat nøkkel og til å signere en transaksjon med en privat nøkkel. I Bitcoin, akkurat som ECDSA, er Schnorr basert på bruken av den elliptiske kurven `secp256k1`, karakterisert av ligningen: $y^2 = x^3 + 7$. Schnorr-signaturprotokollen har blitt implementert i Bitcoin-protokollen siden november 2021 med aktiveringen av Taproot-oppdateringen.
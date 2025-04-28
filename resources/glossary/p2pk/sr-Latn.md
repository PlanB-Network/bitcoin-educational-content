---
term: P2PK
---

P2PK označava *Pay to Public Key*. To je standardni model skripte korišćen na Bitcoin za uspostavljanje uslova trošenja na UTXO. Omogućava zaključavanje bitkoina direktno na javni ključ, umesto na Address.

Tehnički, P2PK skripta sadrži javni ključ i instrukciju koja zahteva odgovarajući digitalni potpis za otključavanje sredstava. Kada vlasnik želi da potroši bitkoine, mora da obezbedi potpis proizveden sa povezanim privatnim ključem. Ovaj potpis se verifikuje korišćenjem ECDSA (*Elliptic Curve Digital Signature Algorithm*). P2PK je često korišćen u ranim verzijama Bitcoin, naročito od strane Satoshi Nakamoto. Danas se gotovo više ne koristi.
---
term: BIP66

---
Introduced a standardization of the signature format in transactions. This BIP was proposed in response to a divergence in the way OpenSSL handled signature encoding across different systems. This heterogeneity posed a risk of splitting the blockchain. BIP66 standardized the signature format for all transactions using strict DER encoding (*Distinguished Encoding Rules*). This change required a soft fork. For its activation, BIP66 then used the same mechanism as BIP34, requiring the `nVersion` field to be increased to version 3, and rejecting all version 2 or lower blocks once the 95% miner threshold was reached. This threshold was crossed at block number 363,725 on July 4, 2015.
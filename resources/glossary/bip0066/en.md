---
term: BIP0066
---

Introduced a standardization of the signature format in transactions. 
It was proposed in response to inconsistencies in how OpenSSL handled signature encoding on different systems, which posed a risk of a blockchain split. 
BIP66 standardized the signature format for all transactions using strict DER encoding (*Distinguished Encoding Rules*). 
This change required a soft fork, activated using the same mechanism as BIP34:
- The nVersion field was increased to version 3.
- All blocks of version 2 or lower were rejected once 95% of miners signaled support.
This threshold was reached at block 363,725 on July 4, 2015.
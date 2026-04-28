---
term: HASH256
definition: Function applying SHA256 twice successively, used in various Bitcoin applications.
---

Cryptographic function used for various applications on Bitcoin. It involves applying the SHA256 function twice on the input data. The message is passed through SHA256 once, and the result of this operation is used as the input for a second pass through SHA256. The output of this function is therefore 256 bits.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$
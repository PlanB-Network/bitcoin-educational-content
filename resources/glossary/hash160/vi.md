---
term: HASH160

---
Cryptographic function used in Bitcoin, notably for generating Legacy and SegWit v0 receiving addresses. It combines two hash functions that are executed successively on the input: first SHA256, then RIPEMD160. The output of this function is therefore 160 bits.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$
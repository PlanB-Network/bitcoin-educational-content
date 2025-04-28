---
term: INDEX (KEY)
---

In the context of an HD portfolio, refers to the sequential number assigned to a child key generated from a parent key. This index is used in combination with the parent key and parent string code to deterministically derive unique child keys. It enables structured organization and reproducible generation of multiple pairs of sister child keys from a single parent key. It is a 32-bit integer used in the `HMAC-SHA512` derivation function. This number can be used to differentiate child keys within an HD portfolio.
---
term: INDEX (KEY NUMBER)

---
In the context of an HD wallet, it refers to the sequential number assigned to a child key generated from a parent key. This index is used in combination with the parent key and the parent chain code to deterministically derive unique child keys. It allows for structured organization and the reproducible generation of multiple sibling child key pairs from the same parent key. It is a 32-bit integer used in the `HMAC-SHA512` derivation function. This number thus differentiates sibling child keys within an HD wallet.
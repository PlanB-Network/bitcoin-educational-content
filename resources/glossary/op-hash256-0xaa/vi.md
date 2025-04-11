---
term: OP_HASH256 (0XAA)

---
Takes the top item from the stack and replaces it with its hash by using the `SHA256` function twice. The input is hashed once with `SHA256`, and then the digest is hashed a second time with `SHA256`. This two-step process generates a 256-bit fingerprint.
---
term: BLOCK HEADER
---

A block header is a data structure that serves as a core component of a Bitcoin block. Each block consists of a header and a list of transactions. The block header contains critical information that ensures the integrity and validity of a block within the blockchain. 
A block header is 80 bytes in size and contains the following fields:
*The block version;*
* The hash of the previous block;
* The Merkle tree root of the transactions;
* The block timestamp;
* The difficulty target;
*The nonce.*

Example: Header of block 785,530 (mined by Foundry USA on April 15, 2023) in hexadecimal format:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Breakdown of the header:
**The version:**

```text
00e0ff3f
```

**The previous hash:**

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```

**The Merkle root:**

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```

**The timestamp:**

```text
bcb13a64
```

**The target:**

```text
b2e00517
```

**The nonce:**

```text
43f09a40
```

For a block to be valid, its header, when double‑hashed using `SHA256d`, must produce a hash less than or equal to the difficulty target. 
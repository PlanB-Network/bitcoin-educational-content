---
term: USEFUL LOAD
---

In the general context of computing, a payload is the essential data carried in a larger data packet. For example, in a SegWit V0 over Bitcoin address, the payload corresponds to the hash of the public key, without the various metadata (the HRP, separator, SegWit version and checksum). For example, at address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, we have :


- `bc`: the human-readable part (HRP) ;
- `1`: the separator ;
- `q`: SegWit version. This is version 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa`: the payload, in this case, the hash of the public key ;
- `ys50gj`: checksum.
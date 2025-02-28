---
term: PAYLOAD

---
In the general context of computing, a payload refers to the essential data carried within a larger data packet. For example, in a SegWit V0 address on Bitcoin, the payload corresponds to the hash of the public key, excluding various metadata (the HRP, the separator, the SegWit version, and the checksum). For instance, in the address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, we have:


- `bc` : the human-readable part (HRP);
- `1` : the separator;
- `q` : the SegWit version. Here, it is version 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa` : the payload, here, the hash of the public key;
- `ys50gj` : the checksum.
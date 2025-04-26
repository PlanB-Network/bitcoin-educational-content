---
term: STAMPS

---
A protocol that allows the integration of formatted image data directly onto the Bitcoin blockchain through raw multisignature transactions (P2MS). Stamps encodes the binary content of an image in base 64 and adds it to the keys of a 1/3 P2MS. One key is real and is used to spend the funds, while the other two are dummy keys (the associated private key is unknown) that store the data. By encoding the data directly as public keys rather than using `OP_RETURN` outputs, images stored with the Stamps protocol are particularly workload-intensive for the nodes. This method notably creates multiple UTXOs, which increases the size of the UTXO set and poses problems for full nodes.
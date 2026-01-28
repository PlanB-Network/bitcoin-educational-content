---
term: BIP0011
---

BIP11, introduced by Gavin Andresen in March 2012, proposed a standard method for creating multisignature transactions on Bitcoin. Its goal was to enhance the security of bitcoins by requiring multiple signatures to authorize a transaction. 
BIP11 introduces a new type of script, named "M-of-N multisig," where `M` represents the minimum number of signatures required out of `N` possible public keys. This standard made use of the existing `OP_CHECKMULTISIG` opcode, which previously had not been allowed under Bitcoin's transaction standardness rules. 
Although this bare multisig script type is no longer commonly used for real multisignature wallets, having largely been replaced by P2SH and P2WSH, it remains valid and is still used in certain meta-protocols such as Stamps. Nodes can also choose not to relay these P2MS transactions by setting the parameter `permitbaremultisig=0`.

> ► *Nowadays, this standard is known as "bare-multisig" or "P2MS".*

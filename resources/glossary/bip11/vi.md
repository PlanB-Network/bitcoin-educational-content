---
term: BIP11

---
BIP introduced by Gavin Andresen in March 2012 that proposes a standard method for creating multisignature transactions on Bitcoin. This proposal aims to enhance the security of bitcoins by requiring multiple signatures to validate a transaction. BIP11 introduces a new type of script, named "M-of-N multisig," where `M` represents the minimum number of signatures required from among `N` potential public keys. This standard utilizes the `OP_CHECKMULTISIG` opcode, already existing in Bitcoin, but which was not previously compliant with the standardization rules of the nodes. Although this type of script is no longer commonly used for actual multisig wallets, favoring P2SH or P2WSH, its use remains possible. It is notably used in meta-protocols such as Stamps. Nodes can, however, choose not to relay these P2MS transactions with the parameter `permitbaremultisig=0`.

> ► *Nowadays, this standard is known as "bare-multisig" or "P2MS".*
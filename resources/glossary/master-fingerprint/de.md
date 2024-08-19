---
term: MASTER FINGERPRINT
---

Ein 4-Byte (32-Bit) Fingerprint des Master-Privatschlüssels in einem Hierarchischen Deterministischen (HD) Wallet. Er wird erhalten, indem der `SHA256` Hash des Master-Privatschlüssels berechnet wird, gefolgt von einem `RIPEMD160` Hash, ein Prozess, der bei Bitcoin als `HASH160` bezeichnet wird. Der Master Fingerprint dient dazu, ein HD Wallet unabhängig von den Ableitungspfaden zu identifizieren, wobei jedoch die An- oder Abwesenheit eines Passworts berücksichtigt wird. Es handelt sich um prägnante Informationen, die es ermöglichen, den Ursprung eines Schlüsselsatzes zu referenzieren, ohne sensible Informationen über das Wallet preiszugeben.
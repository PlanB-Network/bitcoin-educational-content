---
term: MASTER-FINGERABDRUCK

---
Ein 4-Byte (32-Bit)-Fingerabdruck des privaten Hauptschlüssels in einer Hierarchical Deterministic (HD) Wallet. Er wird durch die Berechnung des "SHA256"-Hashes des privaten Hauptschlüssels, gefolgt von einem "RIPEMD160"-Hash, einem Prozess, der bei Bitcoin als "HASH160" bezeichnet wird, erhalten. Der Master Fingerprint wird verwendet, um eine HD-Wallet zu identifizieren, unabhängig von den Ableitungspfaden, aber unter Berücksichtigung des Vorhandenseins oder Nichtvorhandenseins einer Passphrase. Es handelt sich dabei um eine prägnante Information, die es ermöglicht, den Ursprung eines Schlüsselsatzes zu referenzieren, ohne sensible Informationen über die Wallet preiszugeben.
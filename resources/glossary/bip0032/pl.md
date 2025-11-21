---
term: BIP0032
---

BIP32 wprowadził koncepcję hierarchicznego deterministycznego Wallet (HD Wallet). Propozycja ta pozwala na generowanie hierarchii par kluczy ze wspólnego "głównego seed", przy użyciu jednokierunkowych funkcji pochodnych. Każda wygenerowana para kluczy może być rodzicem innych kluczy podrzędnych, tworząc w ten sposób strukturę drzewiastą (hierarchiczną). Zaletą BIP32 jest to, że umożliwia zarządzanie wieloma różnymi parami kluczy z koniecznością przechowywania tylko jednego seed w celu ich regeneracji. Ta innowacja pomogła w szczególności zwalczyć kwestię ponownego użycia Address, która jest poważna dla prywatności użytkowników. BIP32 pozwala również na tworzenie podgałęzi w ramach tego samego Wallet, aby ułatwić zarządzanie nim.
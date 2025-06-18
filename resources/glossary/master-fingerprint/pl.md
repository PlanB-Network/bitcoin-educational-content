---
term: GŁÓWNY ODCISK PALCA
---

4-bajtowy (32-bitowy) odcisk palca głównego klucza prywatnego w Hierarchicznym Deterministycznym (HD) Wallet. Uzyskuje się go poprzez obliczenie `SHA256` Hash głównego klucza prywatnego, a następnie `RIPEMD160` Hash, proces określany jako `HASH160` na Bitcoin. Master Fingerprint jest używany do identyfikacji HD Wallet, niezależnie od ścieżek derywacji, ale biorąc pod uwagę obecność lub brak passphrase. Jest to zwięzła informacja, która pozwala na odniesienie się do pochodzenia zestawu kluczy, bez ujawniania poufnych informacji o Wallet.
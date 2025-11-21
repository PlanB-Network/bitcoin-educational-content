---
term: P2PK
---

P2PK to skrót od *Pay to Public Key*. Jest to standardowy model skryptu używany na Bitcoin do ustalania warunków wydawania na UTXO. Pozwala on na blokowanie bitcoinów bezpośrednio na kluczu publicznym, a nie na Address.

Z technicznego punktu widzenia skrypt P2PK zawiera klucz publiczny i instrukcję, która wymaga odpowiedniego podpisu cyfrowego w celu odblokowania środków. Gdy właściciel chce wydać bitcoiny, musi dostarczyć podpis złożony za pomocą powiązanego klucza prywatnego. Podpis ten jest weryfikowany przy użyciu algorytmu ECDSA (*Elliptic Curve Digital Signature Algorithm*). P2PK był często używany we wczesnych wersjach Bitcoin, zwłaszcza przez Satoshi Nakamoto. Obecnie prawie nie jest już używany.
---
term: P2PK
---

P2PK staat voor *Pay to Public Key*. Het is een standaard scriptmodel dat gebruikt wordt op Bitcoin om bestedingsvoorwaarden op een UTXO vast te stellen. Hiermee kunnen bitcoins direct aan een publieke sleutel worden gekoppeld, in plaats van aan een Address.

Technisch gezien bevat het P2PK-script een openbare sleutel en een instructie die een overeenkomstige digitale handtekening vereist om het geld te ontgrendelen. Wanneer de eigenaar de bitcoins wil uitgeven, moet hij een handtekening zetten met de bijbehorende privésleutel. Deze handtekening wordt geverifieerd met ECDSA (*Elliptic Curve Digital Signature Algorithm*). P2PK werd vaak gebruikt in de vroege versies van Bitcoin, met name door Satoshi Nakamoto. Tegenwoordig wordt het bijna niet meer gebruikt.
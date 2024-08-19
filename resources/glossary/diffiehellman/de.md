---
term: DIFFIE-HELLMAN
---

Kryptografisches Verfahren, das es zwei Parteien ermöglicht, ein gemeinsames Geheimnis über einen ungesicherten Kommunikationskanal zu generieren. Dieses Geheimnis kann dann verwendet werden, um die Kommunikation zwischen den beiden Parteien zu verschlüsseln. Diffie-Hellman verwendet modulare Arithmetik, sodass selbst wenn ein Angreifer die Austausche beobachten kann, er das gemeinsame Geheimnis nicht ableiten kann, ohne ein schwieriges mathematisches Problem zu lösen: den diskreten Logarithmus. In Bitcoin wird manchmal eine Variante von DH namens ECDH verwendet, die eine elliptische Kurve nutzt, insbesondere für statische Adressprotokolle wie Silent Payments oder BIP47.
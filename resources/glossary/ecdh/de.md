---
term: ECDH
---

Methode des kryptografischen Schlüsselaustauschs, basierend auf den Prinzipien des Diffie-Hellman-Schlüsselaustauschs, jedoch unter Verwendung elliptischer Kurven, um ein hohes Maß an Sicherheit bei kleineren Schlüsselgrößen zu bieten. Dieses Protokoll ermöglicht es zwei Parteien, ein gemeinsames Geheimnis zu generieren, indem sie ihre öffentlichen und privaten Schlüsselpaare verwenden, ohne jemals die privaten Schlüssel selbst austauschen zu müssen. Das gemeinsame Geheimnis kann dann verwendet werden, um nachfolgende Kommunikationen zu verschlüsseln. Dieser Algorithmus findet sich manchmal in Vorschlägen zur Verbesserung von Bitcoin, insbesondere BIP47 oder BIP352 für das Ableiten frischer Empfangsadressen aus einem statischen Identifikator.
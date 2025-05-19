---
term: LNURL
---

Kommunikationsprotokoll, das eine Reihe von Funktionen zur Vereinfachung der Interaktion zwischen Lightning-Knoten und Kunden sowie Anwendungen von Drittanbietern spezifiziert. Dieses Protokoll basiert auf HTTP und ermöglicht die Erstellung von Links für verschiedene Vorgänge, wie z. B. eine Zahlungsanforderung, eine Abhebungsanforderung oder andere Funktionalitäten, die das Nutzererlebnis verbessern. Jede LNURL ist eine in bech32 kodierte URL mit dem Präfix "lnurl", die beim Scannen eine Reihe von automatischen Aktionen auf dem Lightning Wallet auslöst.


Mit LNURL-withdraw (LUD-03) können Sie beispielsweise Geld von einem Dienst abheben, indem Sie einen QR-Code scannen, ohne manuell einen generate oder Invoice zu verwenden. Oder mit LNURL-auth (LUD-04) können Sie sich mit Online-Diensten verbinden, indem Sie einen privaten Schlüssel auf Ihrem Lightning Wallet anstelle eines Passworts verwenden.
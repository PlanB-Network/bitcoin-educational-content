---
term: BTCPay Server

definition: Open-Source-Zahlungsprozessor, der es ermöglicht, Bitcoin-Zahlungen ohne Zwischenhändler zu akzeptieren.
---

⚠️ **Kritische Sicherheitswarnung (7. August 2026):** Eine kritische Schwachstelle in BTCPay Server wird aktiv ausgenutzt und kann zum Verlust von Geldmitteln führen. Aktualisieren Sie Ihre Instanz umgehend auf **Version 2.4.2** über `Admin Dashboard > Server > Maintenance > Update` und prüfen Sie anschließend, ob in der Fußzeile `2.4.2` angezeigt wird. Falls Sie nicht sofort aktualisieren können, fahren Sie Ihren BTCPay Server herunter. Nach dem Update müssen Sie außerdem Ihre macaroons und Ihre `macaroons.db` vollständig erneuern, die Authentifizierungs-Strings jedes anderen Lightning-Backends vollständig erneuern und, falls Sie eine Hot-Wallet on-chain innerhalb von BTCPay Server erstellt haben, diese Gelder verschieben und die Wallet neu anlegen. Integratoren sollten zudem NBXplorer auf Version 2.6.10 aktualisieren. Quelle: [Release Notes zu BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
BTCPay Server ist ein Open-Source-Zahlungsprozessor, der es Händlern und Nutzern ermöglicht, Bitcoin-Zahlungen zu akzeptieren, ohne sich bei der Transaktionsverarbeitung auf einen Dritten verlassen zu müssen. BTCPay Server wurde 2017 auf den Markt gebracht und bietet eine Lösung zur Integration von Bitcoin-Zahlungen für E-Commerce-Websites, mit fortschrittlichen Funktionen wie Unterstützung für Hardware-Wallets, Abrechnungs- und Buchhaltungstools sowie Kompatibilität mit dem Lightning Network. Seine Entwicklung wurde von Nicolas Dorier initiiert, als Reaktion auf die Aktionen von Bitpay, das seiner Meinung nach seine Nutzer in die Irre geführt hat, indem es sie zur Annahme von SegWit2x drängte, das das Unternehmen fälschlicherweise als den "wahren" Bitcoin ansah. Diese Opposition wurde in einem berühmt gewordenen Tweet von Nicolas Dorier im August 2017 festgehalten:

> "_Das ist Lüge, mein Vertrauen in dich ist gebrochen, ich werde dich überflüssig machen_".

---
term: BTCPay Server
definition: Open-source betalingsverwerker die het mogelijk maakt om bitcoin-betalingen te accepteren zonder tussenpersoon.
---

⚠️ **Kritieke beveiligingswaarschuwing (7 augustus 2026):** een kritieke kwetsbaarheid in BTCPay Server wordt actief misbruikt en kan leiden tot verlies van fondsen. Werk je instance onmiddellijk bij naar **versie 2.4.2** via `Admin Dashboard > Server > Maintenance > Update` en controleer daarna of de footer `2.4.2` weergeeft. Kun je niet direct updaten, schakel dan je BTCPay Server uit. Na de update moet je ook je macaroons en je `macaroons.db` volledig vernieuwen, de authenticatiegegevens van elke andere Lightning-backend volledig vernieuwen en, als je binnen BTCPay Server een hot on-chain wallet hebt aangemaakt, die fondsen verplaatsen en de wallet opnieuw aanmaken. Integrators dienen daarnaast NBXplorer bij te werken naar versie 2.6.10. Bron: [Release-opmerkingen van BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b

BTCPay Server is een open-source betalingsverwerker die handelaren en gebruikers in staat stelt Bitcoin betalingen te accepteren zonder afhankelijk te zijn van een derde partij voor de verwerking van transacties. BTCPay Server werd gelanceerd in 2017 en biedt een Bitcoin betalingsintegratieoplossing voor e-commercesites, met geavanceerde functies zoals ondersteuning voor hardware wallets, facturerings- en accountingtools, en compatibiliteit met de Lightning Network. De ontwikkeling ervan werd geïnitieerd door Nicolas Dorier, als reactie op de acties van Bitpay dat, volgens hem, zijn gebruikers misleidde door hen in de richting van de adoptie van SegWit2x te duwen, wat het bedrijf ten onrechte als de "echte" Bitcoin beschouwde. Deze oppositie werd samengevat in een nu beroemde tweet van Nicolas Dorier in augustus 2017:


> "_Dit zijn leugens, mijn vertrouwen in jou is gebroken, ik zal je overbodig maken_".


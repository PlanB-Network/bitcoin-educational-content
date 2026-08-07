---
term: BTCPay Server

definition: Open-source platební procesor umožňující přijímat platby v bitcoinech bez prostředníka.
---

⚠️ **Kritické bezpečnostní upozornění (7. srpna 2026):** kritická zranitelnost postihující BTCPay Server je aktivně zneužívána a může vést ke ztrátě prostředků. Okamžitě aktualizujte svou instanci na **verzi 2.4.2** přes `Admin Dashboard > Server > Maintenance > Update` a poté ověřte, že se v patičce zobrazuje `2.4.2`. Pokud nemůžete aktualizovat ihned, svůj BTCPay Server vypněte. Po aktualizaci musíte také kompletně obnovit své macaroons a soubor `macaroons.db`, kompletně obnovit ověřovací řetězce jakéhokoli dalšího Lightning backendu, a pokud jste uvnitř BTCPay Server vygenerovali horkou on-chain peněženku, přesuňte z ní prostředky a peněženku vytvořte znovu. Integrátoři by měli rovněž aktualizovat NBXplorer na verzi 2.6.10. Zdroj: [Poznámky k vydání BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
BTCPay Server je platební procesor s otevřeným zdrojovým kódem, který umožňuje obchodníkům a uživatelům přijímat platby v bitcoinech, aniž by se při zpracování transakcí museli spoléhat na třetí stranu. BTCPay Server, který byl spuštěn v roce 2017, poskytuje řešení pro integraci plateb v bitcoinech pro weby elektronických obchodů s pokročilými funkcemi, jako je podpora hardwarových peněženek, fakturační a účetní nástroje a také kompatibilita se sítí Lightning Network. Jeho vývoj inicioval Nicolas Dorier v reakci na kroky společnosti Bitpay, která podle něj uvedla své uživatele v omyl tím, že je tlačila k přijetí SegWit2x, který společnost mylně považovala za "pravý" Bitcoin. Tento odpor byl obsažen v dnes již známém tweetu Nicolase Doriera ze srpna 2017:

> "_Toto je lež, má důvěra v tebe je zlomena, učiním tě zastaralým_".

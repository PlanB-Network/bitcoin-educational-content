---
term: BTCPay Server
definition: Betalningsprocessor med öppen källkod som gör det möjligt att ta emot bitcoinbetalningar utan mellanhänder.
---

⚠️ **Kritisk säkerhetsvarning (7 augusti 2026):** en kritisk sårbarhet som påverkar BTCPay Server utnyttjas aktivt och kan leda till förlust av medel. Uppdatera din instans till **version 2.4.2** omedelbart via `Admin Dashboard > Server > Maintenance > Update` och kontrollera sedan att sidfoten visar `2.4.2`. Om du inte kan uppdatera omgående, stäng ner din BTCPay Server. När uppdateringen är klar måste du dessutom byta ut dina macaroons och din `macaroons.db` helt, byta ut autentiseringssträngarna för eventuella andra Lightning-backends helt, och om du har genererat en hot on-chain-plånbok inuti BTCPay Server ska du flytta dessa medel och skapa plånboken på nytt. Integratörer bör även uppdatera NBXplorer till version 2.6.10. Källa: [Versionsinformation för BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b

BTCPay Server är en betalningsprocessor med öppen källkod som gör det möjligt för handlare och användare att acceptera Bitcoin-betalningar utan att förlita sig på en tredje part för transaktionsbehandling. BTCPay Server lanserades 2017 och tillhandahåller en Bitcoin-betalningsintegrationslösning för e-handelswebbplatser, med avancerade funktioner som stöd för hårdvaruplånböcker, fakturerings- och redovisningsverktyg samt kompatibilitet med Lightning Network. Utvecklingen initierades av Nicolas Dorier, som svar på Bitpays agerande som enligt honom hade vilselett sina användare genom att driva dem mot antagandet av SegWit2x, som företaget felaktigt betraktade som den "sanna" Bitcoin. Denna opposition sammanfattades i en numera berömd tweet från Nicolas Dorier i augusti 2017:


> "_Detta är lögn, mitt förtroende för dig är förbrukat, jag ska göra dig obsolet_".


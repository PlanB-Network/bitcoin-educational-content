---
term: BTCPay Server
definition: Open-source payment processor allowing for the acceptance of bitcoin payments without an intermediary.
---

⚠️ **Critical security alert (7 August 2026):** a critical vulnerability affecting BTCPay Server is being actively exploited and can lead to a loss of funds. Update your instance to **version 2.4.2** immediately via `Admin Dashboard > Server > Maintenance > Update`, then check that the footer displays `2.4.2`. If you cannot update straight away, shut down your BTCPay Server. Once updated, you must also completely refresh your macaroons and your `macaroons.db`, completely refresh the authentication strings of any other Lightning backend, and, if you generated a hot on-chain wallet inside BTCPay Server, move those funds and recreate the wallet. Integrators should also update NBXplorer to version 2.6.10. Source: [BTCPay Server 2.4.2 release notes](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b

BTCPay Server is an open-source payment processor that enables merchants and users to accept Bitcoin payments without relying on a third party for transaction processing. 
Launched in 2017, BTCPay Server provides a Bitcoin payment integration solution for e-commerce sites, with advanced features such as support for hardware wallets, billing and accounting tools, as well as compatibility with the Lightning Network. 
Its development was initiated by Nicolas Dorier, in response to Bitpay's actions which, according to him, misled users by promoting SegWit2x as the "real" Bitcoin. This opposition was encapsulated in a now famous tweet from Nicolas Dorier in August 2017:

> "_This is lies, my trust in you is broken, I will make you obsolete_".


---
term: BTCPay Server
definition: 開源支付處理器，允許在沒有中間人的情況下接受比特幣支付。
---

⚠️ **重大安全警報（2026 年 8 月 7 日）：** 一項影響 BTCPay Server 的重大漏洞正遭到積極利用，可能導致資金損失。請立即透過 `Admin Dashboard > Server > Maintenance > Update` 將您的執行個體更新至 **version 2.4.2**，然後確認頁尾顯示 `2.4.2`。若您無法立即更新，請關閉您的 BTCPay Server。更新完成後，您還必須徹底更換您的 macaroons 與 `macaroons.db`、徹底更換任何其他 Lightning 後端的驗證字串；若您曾在 BTCPay Server 內產生熱錢包（on-chain），請將該筆資金轉出並重新建立錢包。整合商亦應將 NBXplorer 更新至 version 2.6.10。來源：[BTCPay Server 2.4.2 發行說明](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2)。

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b

BTCPay Server 是一款開源支付處理器，可讓商家和用戶接受 Bitcoin 支付，而無需依賴第三方進行交易處理。BTCPay Server 於 2017 年推出，為電子商務網站提供 Bitcoin 支付整合解決方案，具有支援硬體錢包、計費和會計工具等進階功能，並與 Lightning Network 相容。其開發是由 Nicolas Dorier 發起的，目的是回應 Bitpay 的行為，根據他的說法，Bitpay 誤導了其使用者，將他們推向採用 SegWit2x，而該公司誤將 SegWit2x 視為「真正的」Bitcoin。Nicolas Dorier 在 2017 年 8 月發了一條現在很有名的推文，概括了他的反對意見：


> 「_這是謊言，我對您的信任破滅了，我會讓您被淘汰_」。


---
term: BTCPay Server

definition: 开源支付处理器，允许在没有中间人的情况下接受比特币支付。
---

⚠️ **重大安全警告（2026年8月7日）：** 一个影响 BTCPay Server 的严重漏洞正在被积极利用，可能导致资金损失。请立即通过 `Admin Dashboard > Server > Maintenance > Update` 将您的实例更新至 **version 2.4.2**，然后确认页脚显示为 `2.4.2`。如果您无法立即更新，请关闭您的 BTCPay Server。完成更新后，您还必须彻底更换您的 macaroons 和 `macaroons.db`，彻底更换任何其他 Lightning 后端的认证字符串；如果您曾在 BTCPay Server 内生成过 on-chain 热钱包，请转移其中的资金并重新创建钱包。集成方还应将 NBXplorer 更新至 version 2.6.10。来源：[BTCPay Server 2.4.2 版本发布说明](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2)。

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
BTCPay Server是一个开源支付处理器，使商家和用户能够接受比特币支付，而无需依赖第三方进行交易处理。BTCPay Server于2017年推出，为电子商务网站提供比特币支付集成解决方案，具有支持硬件钱包、计费和会计工具以及兼容闪电网络等高级功能。Nicolas Dorier 是为了回应 Bitpay 公司的行为而发起开发的，他认为 Bitpay 公司误导了用户，推动用户采用 SegWit2x，错误地将 SegWit2x 视为 真正的比特币。Nicolas Dorier 在 2017 年 8 月发布了一条现已成为著名推文的推文，概括了他的反对意见：

> "_这是谎言，我对你的信任破灭了，我要让你被淘汰_"。


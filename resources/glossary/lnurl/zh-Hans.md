---
term: LNURL
---

通信协议，规定了一系列旨在简化闪电节点与客户端以及第三方应用程序之间互动的功能。该协议基于HTTP，可为各种操作创建链接，如支付请求、提款请求或其他增强用户体验的功能。每个 LNURL 都是以 bech32 编码的 URL，前缀为 `lnurl`，扫描后会触发 Lightning Wallet 上的一系列自动操作。


例如，LNURL-withdraw（LUD-03）可让您通过扫描二维码从服务中提取资金，而无需手动generate和Invoice。或者 LNURL-auth (LUD-04) 可让您使用 Lightning Wallet 上的私人密钥而不是密码连接到在线服务。
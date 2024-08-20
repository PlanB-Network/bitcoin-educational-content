---
术语：BIP21
---

由Nils Schneider和Matt Corallo撰写的提案，基于Luke Dashjr撰写的BIP20，而BIP20又源自Nils Schneider写的另一份文件。BIP21定义了接收地址应如何在URI（*统一资源标识符*）中编码，以便于支付。例如，遵循BIP21的比特币URI，如果我希望以“*Pandul*”标签请求发送0.1 BTC给我，它看起来会是这样：

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

这种标准化改善了比特币交易的用户体验，允许用户点击链接或扫描二维码来初始化他们的参数。BIP21标准现在已在比特币钱包软件中广泛采用。
---
term: BIP0021

---
该提议由 Nils Schneider 和 Matt Corallo 撰写，其基于 Luke Dashjr 撰写的 BIP20，而 BIP20 又来自 Nils Schneider 撰写的另一份文件。BIP21 定义了如何在 URI（*统一资源标识符*）中对接收地址进行编码，以方便支付。例如，按照 BIP21，假设我请求 *Pandul* 向我发送 0.1 BTC 的比特币 URI 应该是如此写出的：

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

通过点击链接或扫描二维码来启动参数，这一标准化改善了比特币交易的用户体验。BIP21 标准现已被比特币钱包软件广泛采用。

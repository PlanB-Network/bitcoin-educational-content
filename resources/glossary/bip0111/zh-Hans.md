---
term: BIP0111

---
建议增加一个名为 `NODE_BLOOM` 的服务位，以允许节点明确表示它们支持 BIP37 中所述的布隆过滤器。引入 `NODE_BLOOM` 后，节点操作员可以选择不使用该服务，以降低 DoS 风险。BIP37 选项在 Bitcoin Core 中默认是关闭的。若想要启用，必须在配置文件中输入`peerbloomfilters=1`参数。

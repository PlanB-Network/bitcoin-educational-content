---
term: BIP111

---
建议增加一个名为 "NODE_BLOOM "的服务位，以允许节点明确表示它们支持 BIP37 中所述的 Bloom 过滤器。引入 `NODE_BLOOM` 后，节点操作员可以禁用该服务，以降低 DoS 风险。BIP37 选项在 Bitcoin Core 中默认是禁用的。要启用它，必须在配置文件中输入参数 `peerbloomfilters=1` 。
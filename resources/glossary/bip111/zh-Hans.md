---
term: BIP111
---

提议增加一个名为`NODE_BLOOM`的服务位，以允许节点明确表示它们对BIP37中描述的Bloom过滤器的支持。引入`NODE_BLOOM`使节点运营商能够禁用此服务，以减少DoS的风险。在比特币核心中，默认禁用BIP37选项。要启用它，必须在配置文件中输入参数`peerbloomfilters=1`。
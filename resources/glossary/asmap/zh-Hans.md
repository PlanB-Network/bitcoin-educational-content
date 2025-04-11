---
term: ASMAP

---
由 Gleb Naumenko 发明，Bitcoin Core 使用的一种工具，通过分散节点间的连接来增强比特币网络的安全性和拓扑结构。它是将 IP 地址映射到自治系统号（ASN），从而根据 ASN 而不是 IP 前缀更好地分配出站连接。这有助于防止 Eclipse 攻击（包括 Erebus 攻击），使攻击者更难模拟多个节点。
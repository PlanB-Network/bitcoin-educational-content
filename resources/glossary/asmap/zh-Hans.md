---
term: ASMAP

definition: 一个Bitcoin Core工具，根据自治系统(ASN)来多样化节点之间的连接，以防止Eclipse攻击。
---
Bitcoin Core 使用的一种工具，由 Gleb Naumenko 发明，通过分散节点间的连接来增强比特币网络的安全性和网络结构。它是将 IP 地址映射到自治系统编号（ASN）。与根据 IP 前缀的方式相比，基于 ASN 的分配能更有效地分散出站连接。这有助于防止日蚀攻击（包括 Erebus 攻击），使攻击者更难以伪装成多个节点。

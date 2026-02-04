---
term: Extra transaction proof
definition: RGB 协议中用于验证 Tapret 类型承诺的补充数据。
---

在 RGB 协议中，ETP 是 Anchor 的一部分，它整合了验证 Tapret 类型 Commitment（在 Taproot 中）所需的附加数据。除其他外，它还包括与 Taproot 脚本相关的内部公开密钥和*脚本路径花费*所需的特定信息。因此，该组件可确保对加密承诺进行准确验证。
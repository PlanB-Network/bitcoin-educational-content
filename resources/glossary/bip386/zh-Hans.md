---
term: BIP386

---
为 Taproot 引入描述符函数。它定义了用于查找 Taproot 输出的函数 `tr(KEY)` 和 `tr(KEY, TREE)`，其中 `KEY` 是内部键，`TREE` 是脚本路径的可选树。BIP386 已在 Bitcoin Core 22.0 版本中实现。
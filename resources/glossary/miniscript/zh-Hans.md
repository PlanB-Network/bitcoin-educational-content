---
term: MINISCRIPT

---
旨在为比特币上安全的脚本编程提供一个框架。比特币的内用语言叫做脚本。它在实际使用中相当复杂，特别是对于复杂和定制的应用程序。最重要的是，很难验证脚本的局限性。Miniscript 使用比特币脚本的一个子集来简化脚本的创建、分析和验证。每个 miniscript 都与本地脚本一一对应。使用一种用户友好的策略语言，然后将其编译到 miniscript 中，最终与本地脚本相对应。

![](../../dictionnaire/assets/30.webp)

因此，Miniscript 允许开发人员以更安全、更可靠的方式构建复杂的脚本。Miniscript 的基本特性如下：

- 它可以对脚本进行静态分析，包括允许的支出条件和资源成本；
- 可以创建符合共识的脚本；
- 可以分析不同的支出路径是否符合节点的标准规则；
- 它为所有钱包软件和硬件建立了可理解和可组合的通用标准。

Miniscript 项目由 Peter Wuille、Andrew Poelstra 和 Sanket Kanjalkar 于 2018 年通过 Blockstream 公司发起。2022 年 12 月，Miniscript 在 24.0 版本中以仅观察模式被添加到 Bitcoin Core 钱包中，随后在 2023 年 5 月的 25.0 版本中被完全添加。

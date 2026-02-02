---
name: Zeus Swap
description: 介于 On-Chain 和 Lightning Network 比特币之间的非托管 Exchange 服务
---

![cover](assets/cover.webp)



Bitcoin 生态系统具有双重性：主网络（On-Chain）提供最大的安全性，而 Lightning Network 实现即时交易。这种双 Layer 架构带来了一个实际挑战：如何在没有中央中介机构的情况下在这两层之间高效地转移资金？



问题很具体：您收到了一笔闪电支付，但希望将其保存在 Cold 存储器中，或者相反，您拥有 On-Chain 比特币，但需要闪电流动性。传统的解决方案包括手动打开/关闭闪电通道（成本高、技术性强）或需要 KYC 的集中式平台。



Zeus Swap 通过自动、非托管 Exchange 服务解决了这一问题。它由 Zeus LSP 开发，允许您将 On-Chain 比特币双向转换为闪电币，而无需将资金委托给中介。该过程使用原子合约（HTLC），保证 Exchange 完成或取消。



其创新之处在于操作简单：只需点击几下，即可获得维护您金融主权的 Exchange，无需注册或 KYC。



## 什么是 Zeus Swap？



Zeus Swap 是 Zeus LSP 开发的一项流动性 Exchange 服务，可实现 Bitcoin 主网络和 Lightning Network 之间的原子交换。它是一种技术基础设施，利用海底掉期和反向掉期促进 On-Chain BTC 和 Lightning Satoshis 之间的双向转换，同时保持操作的非托管性质。



### 技术架构



Zeus Swap 使用 Boltz 的开源 Bitcoin/Lightning 原子交换技术。该协议使用 Hash 时间锁定合约（HTLC）：锁定资金的合约有两个释放条件（披露加密秘密或时间到期）。



在海底交换（On-Chain → 闪电）中，用户向包含闪电 Invoice 的 Hash 的 Address 发送比特币。Zeus LSP 只有通过支付相应的 Invoice，揭示自动解锁比特币的预图像，才能解锁这些资金。这种机制保证了原子性。



对于反向交换（Lightning → On-Chain），用户支付 Zeus LSP 的 Lightning Invoice，显示一个预图像，以便将准备好的 Bitcoin 交易释放到目的地 Address。



有关 Lightning Network 工作原理的更多详情，请参阅我们的专门课程 ：



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### 业务模式



Zeus LSP 充当做市商，维持 On-Chain 和 Lightning 的流动性，以兑现掉期。对于掉期交易，Zeus 收取可变费用（通常为 0.1% 至 0.5%，取决于方向和条件），外加 Bitcoin 的 Mining 费用，并在验证前透明显示。



作为 "闪电服务提供商"，Zeus 凭借其在按需开通渠道、高效路由和定制流动性解决方案方面的专业知识，优化了成本。



### 整合



Zeus Wallet 本机集成了该服务，无需离开 Interface Bitcoin/Lightning，即可实现交换。这消除了应用程序之间复制和粘贴的摩擦。



所有钱包均可访问独立的 Interface 网络，保证了使用的最大灵活性。



## 主要特点



### 双向交换



Zeus Swap 提供两种类型的 Exchange：



**Submarine swaps (On-Chain → Lightning)**：从 Bitcoin 储备中注入 "闪电 "流动资金，用于为移动 Wallet 或 "闪电 "节点提供能量，而无需手动打开通道。



**反向交换（闪电→On-Chain）**：将闪电比特币转换为 On-Chain 比特币，用于长期存储，避免代价高昂的渠道关闭。



### 用户界面



**Interface web** (swaps.zeuslsp.com)：无需注册的简化体验、实时显示费用和状态的指导流程。



**Zeus Wallet 集成**：从应用程序直接交换，自动管理发票和地址，消除处理错误。



### 安全和恢复



每次交换都会生成唯一的 Contract，其参数不可更改：Hash 闪电、超时、退款 Address。如果发生故障，可通过提供的 Address 自动恢复，与 Zeus LSP 无关。



**Zeus Swaps Rescue Key**：在 On-Chain → Lightning 交换过程中，Zeus 会自动生成一个通用恢复密钥，取代旧的单个退款文件。此独一无二的密钥可在任何设备上使用，并适用于用其创建的所有交换。下载并将此密钥保存在安全位置至关重要，以便在交换失败时恢复您的资金。



### 网络优化



Zeus Swap 可根据网络条件自动调整到期时间和 Mining 费用。Zeus 用户可从高级选项中获益：选择 LSP、定制延迟、与其他服务兼容 (Boltz)。



## 安装和使用



### 访问方法



**Interface web** (swaps.zeuslsp.com)：与所有钱包兼容的通用解决方案，无需安装，适合偶尔使用。



**Zeus应用程序**（iOS/Android）：结合Wallet和交换的综合体验，适合普通用户使用。



请参阅我们的 Zeus 教程，了解有关这款完整的 Wallet 的更多信息：



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### 网络配置



**On-Chain → Lightning**：该过程首先在 Interface Web Zeus Swap 上配置交换。用户可以使用 On-Chain 和 Lightning 字段之间的箭头来反转交换方向。



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus 交换：选择金额（Sats 50,000 → Sats 49,648 （扣除费用）），透明显示网络费用 (Sats 302) 和 Zeus 服务 (Sats 50)。



在此过程中，Zeus 会让您下载通用恢复密钥：



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Zeus Swaps 救援密钥下载对话框--通用密钥，用于替换旧的单个报销文件*。



如果您已经有了密钥，Zeus 允许您检查它：



![Vérification de la clé existante](assets/fr/03.webp)



*Interface 检查现有 Zeus Swaps 救援密钥*的有效性



配置完成后，Zeus 会生成 Bitcoin 车厂 Address，并显示相关说明：



![Adresse de dépôt et instructions](assets/fr/04.webp)



*交换完成页面：二维码和 Bitcoin Address 用于发送 50,000 Satss，并提醒 24 小时有效期*。



然后，交换等待 Bitcoin 的确认：



![Attente de confirmation](assets/fr/05.webp)



*状态 "Mempool 中的交易"--等待 Bitcoin 的确认以最终完成交换*。



一旦确认，交换将自动完成：



![Swap réussi](assets/fr/06.webp)



*确认成功：扣除网络和服务费后，闪电收到 49 648 份 Sats*



### 使用 Zeus 应用程序



**闪电 → On-Chain**：Zeus 应用程序为反向交换（Lightning 至 Bitcoin）提供综合体验。



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Zeus 主屏幕显示 Lightning（69,851 Sats）和 On-Chain（38,018 Sats）的余额，可通过侧边菜单进行交换*。



![Configuration du swap reverse](assets/fr/08.webp)



*Interface 反向交换创建：50,000 Sats Lightning → 49,220 Sats On-Chain，网络费用（530 Sats）和服务（250 Sats）清晰显示。用户可以通过 "generate On-Chain Address "按钮从 Wallet Zeus 手动输入接收 Bitcoin 的 Address，或自动输入接收 generate 的 generate。



![Finalisation du swap mobile](assets/fr/09.webp)



*最终确定屏幕：闪电 Invoice 付款屏幕，显示 "PAY THIS Invoice"（支付此 Invoice），在 9.96 秒内确认闪电付款成功，余额报表显示 49 162 台 Sats 正在等待确认*。



### 监控和安全



每个交换都有一个独特的标识符，可进行实时跟踪。完整的进度显示，到期自动提醒。根据网络条件自动提出充电建议。



## 优势和局限性



### 益处





- 简单**：只需点击几下即可进行交换，无需手动操作通道
- 非托管**：无 KYC、无账户、资金从未委托给第三方
- 透明度**：在验证前明确显示费用（0.1% 至 0.5% + 最低费用，具体取决于用户测试--在每次交换时查看当前费用）
- 移动集成**：Zeus Wallet 中的本地体验



### 局限性





- 过期时间**：最长 24-48 小时，如果 Bitcoin 未及时确认则失效
- 金额限制**：最低 25,000 Sats，Zeus LSP 流动性根据条件而变化
- 跟踪 On-Chain**：可通过 Blockchain 分析识别的 HTLC 脚本
- 需要确认**：Bitcoin 验证至少需要 10 分钟



## 最佳做法



### 时间和费用





- 在拥堵程度较低时关注 Mempool.space
- 首选周末和非高峰时段，以降低 Mining 成本
- 计算盈利能力：小额与直接开通渠道的对比



### 安全





- 仔细检查 Bitcoin 地址（建议复制粘贴）
- 备份 Zeus Swaps 救援密钥**：下载并将救援密钥存储在安全的地方
- 文件：Contract ID、退款 Address、有效期
- 使用适当的 Mining 费用进行及时确认



### 使用策略





- 平衡 On-Chain/Lightning 流动资金，满足您的需求
- Zeus Swap 用于一次性调整，直接渠道满足永久性需求



## 与其他互换服务的比较



### 宙斯交换 vs Boltz Exchange



Zeus Swap 使用 Boltz 的后台技术，但做了一些重要改进：



**宙斯交换的好处** ：




- Interface 统一**：Zeus 中的本地集成 Wallet vs Interface 网络技术 Boltz
- WebSocket API**：实时更新与手动轮询
- 自动管理**：自动计费和 Address 管理
- 移动支持**：仅对智能手机和台式机进行优化
- Swagger 文档**：面向开发人员的完整 REST API



**Boltz 仍具有优势**，可完全独立并与任何 Bitcoin/Lightning 设置一起使用。



Zeus Swap 将成熟的 Boltz 技术转化为主流用户体验，相当于原始协议和用户友好型应用程序之间的区别。



### 宙斯交换 vs 凤凰/布雷兹（综合交换）



Phoenix 和 Breez 集成了透明交换功能，向最终用户隐藏了技术复杂性。Phoenix 使用自动换入/换出系统，用户无需明确区分 Bitcoin 层：他 "发送到 Bitcoin Address"，应用程序在后台处理交换。



这种极端简化的方法非常适合初学者，但却限制了对操作的理解和控制。Zeus Swap 采用了更具教育性的理念：用户明白他们是在两个不同的层之间进行交换，从而逐步加深对两个-Layer Bitcoin 生态系统的理解。



## 费用和限额的详细比较（2024 年）



⚠️ **警告**：根据市场情况和服务更新，费用可能会随时间变化。在验证掉期之前，请务必查看 Interface 中显示的费用。




| 服务 | 潜水艇互换 (BTC→LN) | 逆向互换 (LN→BTC) | 最低金额 |
| ------------- | ----------------------- | --------------------- | --------------- |
| **Zeus Swap** | ~0.1% + 挖矿费用 | 0.5% + 挖矿费用 | 25,000 sats |
| **Boltz** | 0.2% + 挖矿费用 | 0.5% + 挖矿费用 | 50,000 sats |
| **Phoenix** | 仅挖矿费用 | 0.4% 固定 | 10,000 sats |
| **Breez** | 0.25% + 网络费用 | 0.5% + 挖矿费用 | 50,000 sats |

Zeus Swap 在易用性和技术控制之间取得了平衡：比 Boltz 更易用，比 Phoenix/Breez 更灵活，采用严格的非监管方式。



## 结论



Zeus Swap 是 Bitcoin 生态系统中的一项重大创新，它巧妙地解决了主网络与 Lightning Network 之间互操作性的难题。这项服务将原子互换的加密稳健性与便捷的用户体验相结合，在不损害金融主权原则的前提下实现了 Bitcoin 双 Layer 管理的民主化。



Zeus Swap 的非托管架构继承自成熟的 Boltz 技术，可确保您的资金在整个交换过程中始终处于您的独家控制之下。这种方法既尊重了 Bitcoin 的精神，又为主流应用提供了所需的用户便利。价格透明和无 KYC 流程强化了这一独特的价值主张。



对于现代 Bitcoin 用户而言，Zeus Swap 是根据需求优化流动性分配的战略工具：On-Chain 可用于长期储蓄的安全存储，"闪电 "可用于日常支出和小额交易。这种灵活性将 Bitcoin 管理从技术限制转变为竞争优势。



在经验丰富的 Zeus LSP 团队和 Boltz 开源社区的支持下，Zeus Swap 的未来发展有望在成本、处理时间和用户体验方面不断改进。这项服务是 Bitcoin 基础设施走向成熟的大趋势的一部分，在这一过程中，技术的复杂性对最终用户变得透明。



## 资源



### 正式文件




- [Zeus Swap - 网络门户](https://swaps.zeuslsp.com)
- [Zeus Wallet - 移动应用程序](https://zeusln.app)
- [博客宙斯 - 公告和教程](https://blog.zeusln.com)
- [宙斯技术文档](https://docs.zeusln.app)



### 社区和支持




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [电报宙斯](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)
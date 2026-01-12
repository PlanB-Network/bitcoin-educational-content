---
name: ArkadeOS
description: Arkade 产品组合和方舟协议完整指南
---

![cover](assets/cover.webp)



Bitcoin 网络面临着一个重大挑战：可扩展性。虽然主层（第 1 层）具有无与伦比的安全性和分散性，但每秒只能处理有限数量的交易。Lightning Network 已成为一种前景广阔的第二层（第 2 层）解决方案，可实现快速、低成本的支付。然而，"闪电 "也有其自身的限制：渠道管理、对流入流动性的需求以及可能使新用户望而却步的技术复杂性。



这就是**Ark**的背景，它是一种新的第二层协议，旨在提供简化的用户体验，同时不牺牲主权。 **ArkadeOS**（或Arkade）是这一协议的首个主要实施方案，提供了下一代Bitcoin产品组合。



本教程将引导您进入 Arkade 的世界。我们将探究 Ark 协议的工作原理，如何安装和配置 Arkade wallet，以及如何使用它即时、保密地发送和接收比特币，而不会像 Lightning Network 那样产生摩擦。



## 了解方舟协议



在深入了解 Arkade 的使用之前，有必要掌握驱动 Arkade 的方舟协议的关键概念。方舟不是一个独立的区块链，而是 Bitcoin 上的一个智能协调机制。



### VTXO 概念


方舟的核心是**VTXO**（虚拟 UTXO）。VTXO 是尚未在 Bitcoin 区块链上发布的 UTXO：它存在于主链（off-chain）之外，但由区块链上预签名的交易支持。



与中心化交易所的余额不同，VTXO 真正属于你。您持有加密证明，即使方舟服务器消失，您也可以随时在区块链上获取相应的真实比特币。VTXO 使您能够在用户之间即时转移价值，而无需等待区块确认。



### 方舟服务提供商（ASP）的作用


方舟协议以客户端-服务器模式运行。服务器称为 **ASP**（方舟服务提供商）。ASP 扮演指挥者的角色：




- 它为网络提供了必要的流动资金。
- 它协调用户之间的交易。
- 它在区块链上组织结算 "回合"。



必须指出的是，ASP 是**非托管**。它从不持有你的私人密钥，也不能窃取你的资金。它的作用纯粹是技术和后勤方面的。如果 ASP 审查您的交易或宕机，您总是可以通过单边退出程序收回您的资金。



### 巡视和隐私


方舟上的交易分批完成，称为**轮**。ASP 会定期（如每隔几秒）收集所有待处理的交易，并将其锚定在 Bitcoin 区块链上的单个优化交易中。


这种机制有两大优势：




- 可扩展性**：单笔 on-chain 交易可验证数千笔 off-chain 支付，大大降低了用户成本。
- 保密**：每一轮都是**CoinJoin**。所有参与者的资金在以新的 VTXO 的形式重新分配之前都会混合到一个共同的资金池中。这就切断了发送方和接收方之间的联系，使外部观察者即使不是不可能，也很难追踪到付款。



## ArkadeOS 演示



ArkadeOS 是向公众提供方舟协议的具体应用程序。它由方舟实验室开发，是一个完整的生态系统，包括一个组合（Wallet）、一个服务器（操作器）和开发者工具。



对于终端用户而言，Arkade 采用的是优雅、直观的 Web wallet （PWA--渐进式 Web 应用程序）形式。它将 VTXO 和回合的加密复杂性隐藏在熟悉的界面之后。有了 Arkade，您就拥有了一个接收地址、一个发送按钮和一个交易历史记录，就像传统的 wallet 一样，但却拥有了 Ark 的即时性和保密性。



## 安装和配置



由于 Arkade 是一款渐进式 Web 应用程序，因此安装特别简单，而且不一定涉及传统的应用程序商店。



### 进入和安装


您可以通过电脑或手机上的任何现代网络浏览器（Chrome、Safari、Brave）直接访问 Arkade。





- 访问应用程序的官方网站： **[arkade.money](https://arkade.money)**。



![arkade homepage](assets/fr/01.webp)



您会看到一系列介绍性屏幕，向您介绍 Arkade 的关键概念：Bitcoin 的新生态系统、自我保管的重要性以及批量交易的优势。



![arkade onboarding](assets/fr/02.webp)





- 在安卓系统（Chrome/Brave）上** ：按浏览器菜单（三点），选择 "安装应用程序 "或 "添加到主屏幕"。
- 在 iOS (Safari)** 上：按共享按钮（带向上箭头的正方形），然后选择 "在主屏幕上"。



安装完成后，Arkade 就会像本地应用程序一样全屏启动，而且没有地址栏。



### 创建投资组合


首次启动时，系统会要求您配置投资组合。





- 点击 **"创建新的 Wallet"**。



![create wallet](assets/fr/03.webp)





- wallet 是即时创建的。与传统的 Bitcoin 钱包不同，**Arkade 不使用 12 或 24 个字的恢复短语**。相反，Arkade 会自动生成一个 Nostr (nsec) 格式的**私人密钥**，用于备份和恢复 wallet。请记住立即保存此密钥（见下一节）。





- 您将看到 "您的新 wallet 已上线！"屏幕，确认您的 wallet 已准备就绪可以使用。点击**"GO TO WALLET "**进入主界面。



进入 wallet 后，您将进入 Arkade 的主界面。在这里，您可以找到余额、发送和接收资金的按钮，以及一个 "应用程序 "选项卡，该选项卡可让您访问 Boltz（闪电交易所）、LendaSat 和 LendaSwap（借贷服务）以及 Fuji Money（合成资产）等集成应用程序。



![wallet interface](assets/fr/04.webp)



### 与 ASP 的连接


默认情况下，投资组合会自动配置为连接 Arkade Labs 官方 ASP。你可以进入**设置** > **关于**，查看服务器地址（目前为 "https://arkade.computer"）。



在当前的 Arkade（测试版）中，无法手动修改 ASP 服务器。应用程序会自动连接到 Arkade Labs 官方 ASP。将来，用户可以根据自己的喜好选择不同的 ASP，但目前还没有这项功能。



### 备份私人密钥


**Arkade 使用 Nostr (nsec) 格式的私钥作为备份和恢复方法。要备份您的私人密钥 ：





- 从主屏幕进入**设置**。
- 选择 **"备份和隐私 "**。
- 您将看到以 "nsec... "格式显示的**私人密钥**。这一长串字符是恢复 wallet 的唯一方法。
- 按**"COPY NSEC TO CLIPBOARD "**复制您的私人密钥。
- 将此密钥保存在安全的地方**：写在纸上，保存在安全的密码管理器中，或使用任何其他适合你的备份方法。
- Arkade 还提供**"启用 Nostr 备份 "**选项。该功能使用 Nostr 协议（一种分散式网络）将 wallet 中的某些数据以加密形式自动备份到 Nostr 中继站。这有助于多个设备之间的同步，并可更简单地恢复 wallet 的状态。



**重要**：Nostr 备份只是一项**舒适**功能。它们不能取代 nsec 密钥备份。Nostr 中继不保证永久存储数据。您的 Nsec 私钥仍然是您恢复资金的唯一有保证的手段。



![backup private key](assets/fr/05.webp)




## 使用 Arkade



设置好 wallet 后，您就可以探索 Arkade 的功能了。该界面旨在无缝统一不同类型的 Bitcoin 支付（链上支付、闪电支付、方舟支付）。



### 接收资金



要为您的投资组合注资，请按**"收款 "**。Arkade 提供三种收款方式：





- 方舟支付**：如果发件人也使用 Arkade，请共享您的 Ark 地址，以实现即时、保密和几乎免费的转账。
- 链上存款（寄宿）**：使用 Bitcoin 地址 (`bc1p...`)，从经典 wallet 或交易所接收。资金转换为 VTXO 之前需要确认（约 10 分钟）。
- 闪电交换**：生成 Lightning 发票并从外部 wallet Lightning 付款。资金通过自动交换即时到账。



![receive amount](assets/fr/06.webp)



收据屏幕显示所有可用选项：QR 码、方舟地址、Bitcoin (BIP21) 地址和闪电发票。对于 "闪电 "付款，请在交易过程中保持应用程序打开状态。



![receive confirmation](assets/fr/07.webp)



### 发送资金



要发送资金，请按**"发送 "**，然后粘贴收件人地址或扫描二维码。Arkade 会自动检测所需的付款类型：





- 方舟**付款：向方舟地址转账即时、私密且几乎免费（0 SATS 费用）。收款人无需在线。
- 闪电**付款：扫描 Lightning 发票（"lnbc..."），Arkade 自动执行交换。ASP 为您支付发票，并从您的 Arkade 余额中扣除。
- 链上支付**：Arkade 向经典的 Bitcoin 地址（"bc1q... "或 "bc1p..."）发起 "合作输出"，该输出将包含在下一轮 on-chain 中。



检查 "签署交易 "屏幕上的详细信息，然后用 **"轻点签署 "** 加以确认。



![send payment](assets/fr/08.webp)



**当前限制（测试版）**：创建时间不足 24 小时的 VTXO 不能用于 on-chain 输出。如果遇到错误，请等待 VTXO "成熟"。



**on-chain 输出保密性**：下面的示例显示了[mempool.space 上的方舟输出交易](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb)。我们观察到一个分布式输入到 4 个不同的输出，就像一个 CoinJoin。对于外部观察者来说，不可能确定哪个数量属于哪个用户。



![transaction ark mempool](assets/fr/11.webp)



## 高级功能



### VTXO 到期管理


方舟协议的一个技术特点是，VTXO 的寿命**有限。这种时间限制是协议设计中固有的。过期时间可由每个 ASP 服务器配置；在 Arkade Labs 官方 ASP 上，过期时间约为**4 周（≈30 天）**。



**这一限制允许方舟服务器有效地管理流动性，并清理不活跃用户的 VTXO。到期后，方舟服务器可从技术上收回 VTXO 树中的剩余资金。



**为了保持 VTXO 的激活状态，需要在过期前对其进行 "刷新"。刷新包括参与新的 "一轮"，在这一轮中，您即将到期的 VTXO 将被交换为新的 VTXO，新的 VTXO 具有新的完整有效期（在 Arkade Labs ASP 上≈30 天）。



Arkade 产品组合会自动管理这一过程：应用程序会持续监控 VTXO 的状态，并在过期前几天自动刷新。只要您定期打开应用程序（至少每周一次），您的 VTXO 就会自动保持激活状态。



**如果您超过 4 周未打开投资组合，您的 VTXOs 将过期。不过，您并不会损失资金：您仍可选择通过**单边退出**收回资金（见下一节）。这一程序成本较高，速度较慢，但可确保您的资金仍可收回。



由于需要定期打开应用程序，Arkade 成为了**"Hot Wallet"**，专为日常消费而设计，而非长期储蓄的保险箱。要存储比特币而不长期使用，最好选择冷冰冰的 wallet 硬件。



**检查 VTXO 的状态**：您可以在**设置** > **高级**中监控您的VTXO状态。查看 "下次续费"，了解下次自动续费的时间；查看 "虚拟币"，了解所有 VTXO 及其到期日的详细列表。



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale（单方面退出）



单边退出是方舟协议的**基本加密保证**，即使 ASP 消失、审查您的交易或拒绝合作，也能确保您取回资金。从技术上讲，您的 VTXO 是您拥有的**预签名 Bitcoin 交易**。在绝对紧急的情况下，您可以在 Bitcoin 区块链上广播这些交易，在未经任何人授权的情况下收回您的资金。



**它是如何工作的？整个过程分为两个阶段。首先，**解锁**：在交易树中按顺序广播构成 VTXO 的预签名交易。然后是**终结**：一旦时间锁过期（通常是 24 小时），您就可以从标准地址领取比特币。



**目前 Arkade 的状态**：在测试版中，还没有用于单边输出的按钮或简单用户界面。该功能目前需要使用 Arkade SDK 和 TypeScript 编程技术知识。



**即使无法通过按键进入程序，加密保证也会存在。您的 VTXO 包含预签名的交易，这些交易合法地属于您。正是这种技术保证使方舟协议成为**非托管**协议：即使在最坏的情况下，您的资金在技术上仍然可以恢复。Arkade 的未来版本可能会添加简化界面。



## 优势和局限性



为了正确理解 Arkade，让我们来总结一下它目前的优缺点。



### 亮点




- 用户体验（UX）**：无需像 Lightning 那样进行渠道管理、接收容量或复杂的渠道备份。只需安装和使用即可。
- 隐私** ：默认 CoinJoin 架构提供的匿名级别远高于标准 on-chain 或 Lightning 交易。
- 互操作性**：通过单一界面支付任何 Bitcoin QR 码（链上支付或闪电支付）。



### 制约因素




- 年轻的协议**：方舟是一项最新技术。可能存在漏洞。建议不要使用方舟来存储损失严重的金额。
- 依赖于 ASP**：虽然不是监管性的，但系统的流动性依赖于 ASP 的可用性。如果 ASP 离线，您将无法即时交易（只能输出您的 on-chain 资金）。
- 仅适用于 Hot Wallet**：需要定期打开应用程序刷新 VTXO，这不适合冷存储（Cold 存储）。



## 比较：阿卡德 vs 闪电 vs 卡舒



为了更好地理解 Arkade 的定位，让我们将其与其他两大可扩展性解决方案进行比较。



| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade**是理想的折中方案：既有卡舒的简单和保密性，又有闪电的主权（非托管）。



## 支持与援助



如果您在使用 Arkade 的过程中遇到任何问题或有任何疑问，该应用程序可提供多种支持选项：





- 转到**设置** > **支持**。
- 您会发现几种选择：
  - 客户支持**：获取有关投资组合的帮助，报告错误或提出问题。
  - 安全聊天**：您的对话是安全和私密的，会话之间会保留历史记录。
  - 错误报告**：报告您遇到的任何问题，包括重现问题的步骤。
  - 跟踪进度**：随时跟踪您的支持票单和对话。



![support](assets/fr/10.webp)



Arkade 团队还通过 @arkade_os 频道在 Telegram 上积极提供支持和集成机会。



## 重要说明：测试版应用程序



**⚠️ Arkade 目前在 mainnet Bitcoin** 上处于公开测试阶段。虽然该应用程序可以使用真实比特币，但必须采取某些预防措施。



### 使用建议




- 使用小额**：避免在 Arkade 上存储大额资金。将 wallet 用于日常开支，并将储蓄保存在冷藏的 wallet 硬件上。
- 可能存在的错误和限制**：与任何正在开发中的应用程序一样，Arkade 可能会出现错误或意外行为。请通过集成支持报告任何问题。
- 快速发展** ：应用程序和协议不断改进。某些功能可能会在未来版本中更改或添加。



### 目前已知的局限性




- 24 小时延迟 VTXO**：新创建的 VTXO 不能立即用于 on-chain 输出。
- ASP 唯一**：目前还无法在应用程序中更改 ASP 服务器。
- 技术性单边输出**：尚无单边输出的简化接口（需要 SDK）。



Arkade 实验室团队正积极努力在未来版本中放宽这些限制。



## 结论



ArkadeOS 是 Bitcoin 生态系统的重大突破。通过实施方舟协议，它证明了 Bitcoin 的基本原则：不信任，要验证，与简单易用性之间的协调是可能的。



尽管 Arkade 仍处于起步阶段，但它为 Bitcoin 支付的未来提供了迷人的一瞥：即时、私密、所有人都可使用，无需任何技术前提条件。它是您日常开支的完美工具，是您安全储蓄解决方案（Cold Wallet）的补充。



我们鼓励您使用少量 Arkade 进行测试，亲自探索这一新协议。生态系统正在快速发展，而 Arkade 站在了创新的最前沿。



## 资源



要了解更多信息，请查阅官方资源：





- Arkade** 网站：[arkadeos.com](https://arkadeos.com)
- 文档**：[docs.arkadeos.com](https://docs.arkadeos.com)
- 方舟**协议：[ark-protocol.org](https://ark-protocol.org)
- 源代码** ：[GitHub Arkade](https://github.com/arkade-os)
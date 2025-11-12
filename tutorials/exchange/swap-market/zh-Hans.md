---
name: 交换市场
description: Bitcoin 和 Lightning 交换服务聚合器
---

![cover](assets/cover.webp)



要在 Bitcoin on-chain 和 Lightning Network 之间转移资金，一般需要手动打开 "闪电 "通道（技术性强且成本高昂），或者使用带有 KYC 的集中式掉期平台。SwapMarket 提供了另一种选择：通过有竞争力的提供商进行无信任原子互换，无需 KYC。



创新：尽管提供商是中间商，但 HTLC（*Hash 时间锁定合约*）在数学上保证您的资金仍在您的控制之下。多个提供商（Boltz、ZEUS Swaps、Eldamar、Middle Way）的联合创造了价格竞争。Interface 网络开源自托管。



## 什么是 SwapMarket？



SwapMarket 于 2024 年推出，是一个开放源码聚合器，可作为 Bitcoin/Lightning 掉期提供商的比较器。用户可即时比较各种条件（费用、流动性、限额），并选择最佳提供商。



### 技术架构



**前端客户端**：100% 客户端应用程序（fork Boltz Web App）托管在 GitHub 页面上。代码在浏览器中运行，无需后台服务器。历史记录存储在本地（cookies/缓存）。公开且可审计的源代码。



**发现提供商** ：src/configs/mainnet.ts`中的硬编码列表。新的提供程序可通过拉取请求或电子邮件添加。



**独立后端**：每个供应商都有自己的 Boltz 后端。界面实时查询 API，即时比较报价。



**HTLC 原子互换**：Hash 时间锁定合约保证原子性：要么执行掉期，要么各方收回资金。在数学上消除了交易对手风险。



### 哲学



SwapMarket 通过在提供商之间创造费用和流动性竞争来减少集中化。无 KYC、开源自托管代码、多个独立运营商以避免单点故障。



## 主要特点



### 提供商市场



界面显示所有活跃的提供商：提供商名称、适用费用（百分比和/或固定费用）、可用的最低/最高金额以及支持的掉期类型。应用程序可直接查询配置文件中引用的每个提供商的应用程序接口，实时检索报价。提供商之间的竞争保证了最佳费率，标准掉期费率一般在 0.5%左右。



### 双向交换



**Swap-in (on-chain → Lightning)**：将 on-chain BTC 转换为闪电币。用例：为移动 wallet Lightning 提供动力，获得节点上的输入容量，或获得即时流动性。



**Swap-out (Lightning → on-chain)**：将 Lightning satoshis 转换为 on-chain BTC。用例：将 wallet 闪电清空至冷库，或重新平衡各层之间的流动性。



### 安全和恢复



**Trustless 原子交换**：HTLC 保证交换全部完成，或各方收回其赌注。在数学上消除了交易方风险。



**偿还机制**：每笔掉期都有时间限制。如果交换失败，过期后资金将自动退还。用户始终保留取回比特币的选择权。



**恢复密钥**：SwapMarket 可以为正在进行的交换导出恢复密钥。如果出现问题，这些密钥可用于从任何设备最终完成或取消交换。



## 安装和使用



### Interface 网络



SwapMarket 无需安装。通过浏览器访问 https://swapmarket.github.io。为获得最大保密性，请使用 Brave、带有反跟踪扩展的 Firefox 或 LibreWolf。建议使用 Tor 浏览器实现网络匿名。



无需注册、电子邮件或身份验证。



### 自行托管（可选）



对于希望避免依赖 GitHub 官方页面域的技术用户，SwapMarket 可在本地运行：



**通过 npm** ：


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Via Docker** ：


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



应用程序的访问网址为 "http://localhost:3000"。自我托管保证了对界面的完全控制，消除了官方域审查的风险，并允许在执行前对源代码进行审计。



### 初始配置



**Wallet "闪电 "**：请确保您拥有可运行的 wallet Lightning（Phoenix、Zeus、BlueWallet 等）。对于换入，您将获得 generate Lightning 发票。对于换出，您将支付一张 Lightning 发票。



**Wallet on-chain**：对于换入，您需要 wallet Bitcoin on-chain 来发送资金。对于换出，请准备一个 Bitcoin 接收地址。



**可选配置**：SwapMarket 将交换历史记录和偏好保存在浏览器 cookie 中。无需创建账户。



## 访问设置和救援密钥



在首次交换之前，我们强烈建议您下载**应急密钥**。如果出现技术问题或无法访问您的设备，该应急密钥可帮助您恢复资金。



### 访问参数



在 SwapMarket 主页，点击界面右上方交换表格旁边的齿轮图标 (⚙️)。



![Accès aux paramètres](assets/fr/01.webp)



### 页面设置



设置 "页面打开，显示多个配置选项：





- 面值**：可选择 BTC 或 sats
- 小数分隔符**：小数分隔符（, 或 .）
- 音频/浏览器通知**：音频和浏览器通知
- 恢复密钥** ：下载恢复密钥
- 日志**：查看、下载或删除日志



![Page Settings](assets/fr/02.webp)



### 下载救援密钥



点击 "救援密钥 "旁边的**下载**按钮。



**要点** ：




- 救援钥匙是一种**一站式应急钥匙**，适用于您今后的所有交换操作
- 将此密钥保存在**安全和永久**的地方（密码管理器、数字保险箱）
- 如果出现交换问题（超时、技术故障），该密钥允许您恢复资金



## 创建交换的步骤



### 调换：闪电 → Bitcoin



第一个例子展示了如何将闪电币转换成 on-chain 比特币。



**第 1 步：交换配置



从主页上选择交换表格 ：




- 闪电**（上栏）：输入您希望以 sats Lightning 发送的金额（例如：30,000 sats）
- BITCOIN** （下栏）：扣除费用后，将自动显示您收到的金额（例如：29,320 sats）



在最下面的字段中，粘贴您希望接收资金的**收款 Bitcoin 地址**。请仔细核对该地址。



默认提供商通常是 Boltz Exchange。网络费用和提供商费用会清楚地显示出来。



![Configuration swap-out](assets/fr/03.webp)



**第 2 步：选择提供方**



点击提供商下拉菜单（默认为 "Boltz Exchange"），显示所有可用的流动性提供商。



打开一个模式窗口，显示一个对照表：




- 状态**：Green 指示器（如果提供商处于活动状态
- 别名**：提供商名称（Boltz Exchange、Middle Way、Eldamar、ZEUS Swaps）
- 费用**：医疗服务提供者收取的费用（一般在 0.49%至 0.5%之间）
- 最大掉期**：接受的最大掉期金额



比较费用和最高额度，然后选择您心仪的提供商。



**请注意**：提供商选择界面不显示每个提供商的**最低金额**。只有在选择了医疗服务提供者后，该信息才会出现在交换创建界面。最低和最高金额可能因提供方而异，并可能随时间推移而变化。 **在进行掉期**时，请务必检查这些限额：如果您希望掉期的金额超出了某个提供商的限额，您可以选择另一个更适合您交易的提供商。



![Sélection du provider](assets/fr/04.webp)



**第 3 步：创建交换和闪电**付款



点击黄色的**"创建原子交换 "**按钮。SwapMarket 将 generate 闪电发票**（BOLT11），供您用 wallet 闪电支付。



页面显示 ：




- 交换 ID**：唯一交换标识符（例如：J4ymFIMVR6Hm）
- 状态**："swap.created"（交换已创建，等待付款）
- QR 码**：用您的 wallet Lightning 扫描它
- Invoice Lightning**：以 "lnbc "开头的字符串（例如：lnbc300u1p50whiv...gn5dk2szgqkvfkzc）



用您的 wallet Lightning（Phoenix、Zeus、BlueWallet 等）支付该发票。需要支付的确切金额会显示出来（例如：30,000 sats）。



![Paiement Lightning](assets/fr/05.webp)



**第 4 步：确认和接受**



一旦确认闪电付款，SwapMarket 将立即收到您的付款，并将 Bitcoin 交易发送到您的地址。



状态变为 **"invoice.settled "**（发票已付），并显示一条确认信息。



您的 on-chain 比特币将在交易确认后立即可用（通常是几分钟到几小时，取决于提供商选择的 mining 费用）。



![Confirmation swap-out](assets/fr/06.webp)



您可以点击**"OPEN CLAIM TRANSACTION "**，在区块链浏览器上查看 Bitcoin 交易。



### 换入：Bitcoin → 闪电



第二个例子展示了如何将 on-chain 比特币转换成闪电卫星币。



**第 1 步：交换配置



从主页上选择交换表格 ：




- BITCOIN** （上栏）：输入您希望以 sats Bitcoin 发送的金额（例如：63,400 sats）
- LIGHTNING**（底部字段）：扣除费用后自动显示您将收到的金额（例如：62 884 sats）



在底部字段，粘贴从 wallet Lightning 生成的 Lightning** 发票 (BOLT11)，如果 wallet 支持，则使用 LNURL 地址。



![Configuration swap-in](assets/fr/07.webp)



**第 2 步：检查救援密钥**



点击**"创建原子交换 "**后，会出现一个模式窗口，要求您验证救援密钥。



![Modal Rescue Key](assets/fr/08.webp)



**Boltz 救援密钥**：由于您已在初始配置时上传了恢复密钥（见上一节），请单击 **"验证现有密钥 "** 按钮导入您保存的密钥。



选择之前下载的救援密钥文件。验证成功后，界面会自动切换到下一步。



**第 3 步：Bitcoin** 交存地址



SwapMarket 现在会生成一个**独特的 Bitcoin 地址**，其中包含与您的 "闪电 "发票相关联的 HTLC 合同。



页面显示 ：




- 交换 ID**：唯一标识符（例如：1kGmB6JyGqU4）
- 状态**："invoice.set" （发票已设定，等待付款 Bitcoin）
- 二维码**：Bitcoin 车厂地址
- Bitcoin** 地址：通常以 "bc1p...... "开头(例如：bc1p5mvtwxapjkds...9d4n9f）
- 黄色警告** ："请确保您的交易在创建此交换后 ~24 小时内确认！"



这 ~24 小时是 HTLC 合约的**超时**。如果您的 Bitcoin 交易未在此时间段内得到确认，则掉期将失败，您需要使用救援密钥才能取回资金。



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



您可以点击**"地址 "**按钮复制地址，或直接扫描 wallet on-chain 上的二维码。



**第 4 步：发送比特币**



从您的 wallet Bitcoin on-chain 中，向生成的地址发送**精确**的金额（例如 63,400 sats）。



**重要**：使用适当的 mining 费用以保证快速确认。如果费用过低，且交易在超过超时（~24 小时）后仍留在内存池中，交换将失败。



交易发送后，SwapMarket 会检测到交易在内存池中，并显示 ：




- 状态** ："transaction.mempool
- 信息**："交易已进入内存池 - 等待确认以完成交换



![Transaction en mempool](assets/fr/10.webp)



**第 5 步：确认和闪电**接收



一旦 Bitcoin 交易得到首次确认，供应商就会自动支付您的闪电发票。您会立即收到 wallet Lightning 上的卫星币。



状态变为 **"transaction.claim.pending "**，然后显示一条确认信息：



![Confirmation swap-in](assets/fr/11.webp)



您的 "闪电 "卫星可立即进入 wallet。



## 优势和局限性



### 益处



**费率竞争**：提供商的聚集产生了自然竞争，使费用降低（0.49% 至 0.5%）。



**保密性**：无 KYC，100% 客户端界面（不传输个人数据），兼容 Tor 浏览器。



**非托管**：HTLC 在数学上保证了对您资金的独家控制。要么交换成功，要么你拿回你的比特币。



**开源自托管**：可审计的公共代码，可在本地部署，以最大限度地抵制审查。



### 局限性



**流动性有限**：活跃的提供商数量有限（Boltz、Eldamar、MiddleWay，视时期而定）。最高金额可能有限。



**过期时间**：超时从 24 小时到 48 小时不等。如果 on-chain 交易在过期前未得到确认，则需要手动恢复。



**Interface 集中化**：虽然可自行托管，但官方界面托管在 GitHub 页面上。如果 GitHub 对 repo 进行审查，通过 swapmarket.github.io 的访问将被阻止（解决方案：自托管）。



**on-chain 跟踪**：HTLC 脚本有可能被高级区块链分析识别。



## 最佳做法



### 安全配置



**下载救援密钥**：首次交换前，请从 "设置 "中下载您的 "救援密钥"（见上文专用部分）。这个独特的密钥将适用于您今后的所有交换，使您能够在出现问题时收回资金。



**使用 Tor 浏览器**：为了最大限度地保密，请通过 Tor 浏览器访问 SwapMarket 以隐藏您的 IP 地址。



**考虑自托管**：对于技术用户而言，运行自己的 SwapMarket 实例可消除对官方 GitHub 页面域的依赖。



### 交换优化



**密切关注 mempool**：交换前检查 mempool.space。选择活动较少的时间，尽量减少 mining 成本。



**检查地址**：对于交换，请仔细检查您的收件地址。使用复制和粘贴，检查前 5 个字符和后 5 个字符。



**用少量**进行测试：从允许的最小量开始（25,000 至 50,000 sats）。熟练掌握后再逐步增加。



**记录你的交换**：记下每笔掉期的 ID、赎回地址和到期日。这些信息有助于在出现技术问题时进行跟踪和恢复。



### 使用策略



**平衡您的现金流**：使用 SwapMarket，根据您的实际需求调整您在 on-chain （储蓄、长期保障）和 Lightning（日常开支、即时支付）之间的分配。



**计算盈利能力**：对于永久性的闪电流动性需求，比较重复掉期与直接开设闪电通道的累积成本。SwapMarket 擅长一次性调整，但不一定适合大额定期流动。



## SwapMarket 与 Boltz：有什么区别？



### 博尔茨技术与服务



**Boltz 是一种开源技术**（GitHub 上的 `boltz-backend`），通过 HTLC 在 Bitcoin、Lightning 和 Liquid 之间实现原子交换。



**关键点**：所有 SwapMarket 提供商（Boltz Exchange、ZEUS Swaps、Eldamar、Middle Way）都部署了自己的 Boltz 后端实例。因此底层技术是相同的。Boltz 后端中的漏洞可能会影响所有提供商，但系统的开源性质允许社区审计。



**Boltz Exchange** 是由 Boltz 团队运营的一项单一服务，而 **SwapMarket** 则汇集了多家使用 Boltz 技术的供应商，创造了一个具有竞争力的定价环境。



更多详情，请参阅我们的 Boltz 和 Zeus Swap 教程：



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### 主要区别



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**SwapMarket 的优势**：价格竞争、后端实例多样化、实时比较。



**技术替代品**（与 SwapMarket 不兼容）：Lightning Loop (Lightning Labs)、Muun Wallet、NLoop、Breez Wallet。这些解决方案使用各自的海底交换实施方案。



**建议**：使用 Boltz Exchange 以简化操作，或使用 SwapMarket 通过竞争优化成本。二者在安全性方面相当（HTLC 非托管）。



## 结论



SwapMarket 通过将多个提供商聚合到一个界面来促进 Bitcoin/Lightning 交换。HTLC 架构保证了掉期交易的非托管性质，不存在 KYC 以确保保密性，可自行托管的开放源代码增强了抵御审查的能力。



供应商之间的竞争提高了利率，增加了流动性来源。为了优化双层管理（节省 on-chain 费用和闪电费用），SwapMarket 是一种维护金融主权和保密性的实用工具。



## 资源



### 正式文件




- [SwapMarket - 网络应用程序](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [技术文件](https://docs.boltz.exchange/)
- [Guide self-hosting](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### 相关项目




- [Boltz Exchange](https://boltz.exchange) - 原始原子交换服务
- [ZEUS Swaps](https://zeusln.com) - 闪电交换提供商
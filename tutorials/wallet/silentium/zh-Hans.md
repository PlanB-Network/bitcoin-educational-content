---
name: Silentium
description: 支持静默支付的渐进式网络 wallet (BIP-352)
---

![cover](assets/cover.webp)



重复使用 Bitcoin 地址是对用户保密性最直接的威胁之一。当收款人共享一个地址接收多笔付款时，任何观察者都可以追踪所有相关交易并重建他们的财务历史。这个问题尤其会影响那些希望在不泄露隐私的情况下公开显示捐赠地址的内容创建者、慈善机构或活动家。



Silentium 针对这一问题提供了一个可直接从浏览器访问的优雅解决方案。路易斯-辛格（Louis Singer）于 2024 年 5 月推出的这款开源渐进式网络应用程序（PWA）实现了静默支付（BIP-352）：一种可重复使用的静态地址，每笔支付最终都会出现在一个单独的区块链地址上，交易之间没有事先的互动或可观察到的联系。



**重要警告**：Silentium 是一个实验项目，是 Silent Payments 轻量级钱包的*概念验证*。它不应被用作日常 wallet 或存储大量资金。开发者明确指出：



> 使用风险自负。

请注意，该 wallet 可用作测试网络或重新测试。



## 什么是 Silentium？



### 理念和目标



Silentium 是在轻量级 wallet 浏览器中实施静默支付的技术演示。虽然它也支持传统的 Bitcoin 地址，但重点在于静默支付，使用户能够以一种简单的方式试用这种隐私技术。



### 静默支付如何运作？



静默支付 (BIP-352) 使用椭圆曲线 Diffie-Hellman 密钥 Exchange (ECDH)。收款人生成一个静态地址（在 mainnet 中为 "sp1......"，在 testnet 中为 "tsp1......"），该地址由两个公开密钥组成：一个是用于检测付款的扫描密钥，另一个是用于使用付款的消费密钥。



发送方将其私人输入密钥与接收方的扫描密钥相结合，计算出一个共享秘密，生成一个加密 "调整"。这种调整添加到消费密钥中，为每笔交易创建了一个唯一的 Taproot 地址。收款人用自己的私人扫描密钥复制这一计算，无需任何事先交互即可检测和使用资金。



优点：增强了发送方和接收方的保密性，无需第三方服务器，交易与传统的 Taproot 支付无异。主要缺点：需要对区块链进行密集扫描以检测付款。



欲了解更多有关无声支付的理论运作，请参阅 BTC,204 课程的最后一部分：Plan ₿ Academy：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 支持的平台



Silentium 是一款可从任何现代浏览器（手机或桌面）访问的渐进式网络应用程序（PWA）。您可以直接在 "app.silentium.dev "上使用它，也可以通过浏览器将其安装为本地应用程序，或在本地进行部署。安装直接从浏览器完成，无需通过官方商店。



## 使用网络应用程序



### 进入和安装



[从浏览器转到 `https://app.silentium.dev/`](https://app.silentium.dev/)。应用程序会立即加载并显示主屏幕。



要在 iOS 上将其安装为本地应用程序，请按共享按钮（带向上箭头的正方形），然后选择 "在主屏幕上"。在 Android 上，浏览器通常会直接提供 "添加到主屏幕 "通知。安装后，Silentium 会显示专用图标，并作为本地应用程序运行，但需要连接互联网才能同步交易。



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### 创建投资组合



首次启动时，选择 "创建 Wallet "以 generate 一个新的组合，或选择 "还原 Wallet "从现有的恢复短语中还原。



选择 "创建 Wallet"。应用程序会生成一个 12 个字的短语，您必须认真写下来。该短语是恢复资金的唯一途径。即使在测试网上，也要采取良好的备份措施。保存短语后按 "继续"。



然后，应用程序会要求您设置密码，以确保 wallet 的访问安全。选择一个强大的密码并确认。



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



确认短语和设置密码后，您将进入主界面。



### Interface 主要参数和参数



主界面显示的余额单位为 Satoshis（最初为 0 sats），底部有三个按钮：




- 同步**：将 wallet 与区块链同步
- 接收**：接收资金
- 发送**：发送比特币



通过右上角的图标（三个横条）进入设置。设置 "菜单提供多个选项：





- 关于**：申请信息
- 备份**：恢复短语的备份
- 资源管理器**：选择区块链资源管理器（默认为 Mempool）和 Silentiumd 服务器
- 网络**：网络选择（mainnet/testnet）
- 密码**：更改密码
- 重新加载**：重新加载 wallet
- 重置**：完全重置
- 主题**：更改主题



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



资源管理器**部分尤为重要：它可以让你选择使用的区块链资源管理器（默认为 Mempool），还可以显示 Silentiumd 服务器的 URL（mainnet 为 `https://bitcoin.silentium.dev/v1`）。如果你托管自己的 Silentiumd 服务器或希望使用 testnet，就可以在这里配置这些参数。



### 接收资金



在主界面按下 "接收 "按钮。默认情况下，Silentium 会显示带 QR 码的静默支付地址。该地址在 mainnet 上以 "sp1... "开头，在 testnet 上以 "tsp1... "开头。



您可以使用屏幕下方的 "切换到经典地址"/"切换到静默地址 "按钮在静默支付和经典 Bitcoin 地址之间进行切换。



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




交易广播后，请等待几分钟。对于静默支付，Silentium 会自动扫描区块链，查找为您准备的交易。交易在逐步确认之前，会显示为 "未确认 "状态。



### 发送付款



在主界面按下 "发送 "按钮。发送界面会询问您......：



1. **Address**：粘贴静默支付地址（`sp1...` 或`tsp1...`）或传统的 Bitcoin 地址。您可以使用 QR 扫描图标扫描地址。


2. **金额**：输入要发送的金额（单位：沙托希）。数字键盘显示，便于输入。顶部显示您的可用余额，以供参考。



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



输入地址和金额后，按 "Proceed（继续）"继续。在确认交易之前，应用程序会要求您选择所需的费用级别。



## wallet 自托管



### 为什么要自助托管？



Silentium 的本地托管提供了完全的主权、代码验证、开发环境以及面对官方网站故障时的恢复能力。



### 先决条件



Node.js（版本 14 以上）、npm 或 yarn、Git 和大约 500 MB 的磁盘空间。



### 本地安装



克隆版本库并安装 .NET Framework：



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### 启动和使用



以开发模式启动应用程序：



```bash
yarn start
```



在浏览器中访问 `http://localhost:3000`。如需优化生产版本 ：



```bash
yarn build
```



在 `build/` 中生成的文件可以使用 nginx、Apache 或任何网络服务器。默认情况下，Silentium 连接到公共的 `bitcoin.silentium.dev` 服务器。修改参数中的设置，使用 testnet 或您自己的服务器。



## Silentiumd 服务器



### 作用和运作



Silentium 使用**Silentiumd**索引服务器来优化支付检测。扫描所有 Taproot 交易对于浏览器或手机来说过于繁琐。



Silentiumd 为每笔 Taproot 交易预先计算中间数据（调整）。您的 wallet 会下载这些调整（每笔交易几个字节），并在本地执行最终计算，验证付款的所有权。与传统的 Electrum 服务器不同，服务器永远不会知道您的密钥，也无法识别您的交易。



紧凑型 BIP158 过滤器允许您的 wallet 在不泄露地址的情况下确定要扫描的区块，从而保护您的机密性。



### 公共服务器



由 Vulpem Ventures 赞助的公共服务器 `bitcoin.silentium.dev` (mainnet) 提供了简单而直接的体验。虽然保密性得到了维护，但这种方法意味着对第三方基础设施的相对信任。



### 托管您自己的 Silentiumd 服务器



为了获得完全的主权，请托管您自己的 Silentiumd 服务器。前提条件带有 `txindex=1` 和 `blockfilterindex=1` 的 Bitcoin Core 非滞后节点、Go 1.21 以上、10-20 GB 磁盘空间、系统管理技能。



**安装：**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



通过环境变量进行配置（详见版本库的 `config.md`）。服务器会为区块链建立索引，并公开一个 API，供 wallet 查询。



目前还没有针对 Umbrel 或 Start9 的打包解决方案，这限制了非技术用户的使用。



## 优势和局限性



### 亮点





- 最大的可访问性**：可从任何浏览器使用，无需大量安装
- 多平台**：采用 PWA 技术，可在手机（安卓/iOS）和桌面上运行
- 简单的自托管**：只需几个命令即可在本地安装
- 开源**：GitHub 上完全可审计的代码
- 注重隐私**：无跟踪、无分析、本地加密计算
- 独立架构**：wallet（客户端）和索引服务器之间的明确分离
- 无账户**：无需注册或提供个人资料



### 需要考虑的制约因素





- 实验项目**：仅用于概念验证，不用于日常使用或生产
- 无保证**：存在错误、漏洞和可能损失资金的风险
- 支持有限**：几乎没有用户文档，社区规模小，没有官方支持
- 服务器依赖性**：需要运行中的 Silentiumd 服务器（公共或自托管）
- 密集扫描**：静默支付检测消耗带宽
- 功能缩减**：无硬币控制、无闪电、无多重签名



## 最佳做法



### seed 安全



即使是在测试网上，也要认真对待你的恢复短语。写下来并放在安全的地方。为测试网和 mainnet 存放不同的钱包：切勿在用于真实资金的 wallet 上使用测试用的 seed。



### 源代码验证



自托管的优势之一是可以在运行前检查源代码。如果你打算用真实资金使用 Silentium，请花点时间审核代码，或者找一个值得信赖的开发人员来做这件事。还要将部署在`app.silentium.dev`上的代码的哈希值与 GitHub 代码库的哈希值进行比较，以确保代码的真实性。



### 备份和恢复



静默支付资金恢复需要与 BIP-352 协议兼容的 wallet。标准的 wallet 无法扫描区块链以检索您的 UTXO Silent Payments。保持安装 Silentium 或确保您可以访问另一个兼容的 wallet（如 Cake Wallet 或其他未来的实现），以便在必要时恢复您的资金。



## 结论



Silentium 为了解无声支付提供了一个无技术障碍的测试平台。作为概念验证，它展示了如何将这项隐私技术集成到 wallet 浏览器中，同时保持自我监护。在 testnet 上进行实验，探索 on-chain 隐私技术的这一重大突破。



## 资源



### 正式文件




- Silentium GitHub 存储库 (wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub 仓库（服务器）： https://github.com/louisinger/silentiumd
- 网络应用：https://app.silentium.dev/
- 静默支付社区网站：https://silentpayments.xyz
- 规格 BIP-352: https://bips.dev/352



### 文章和资源




- 官方公告（推特）：https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - 无声支付：https://bitcoinops.org/en/topics/silent-payments/



### Testnet 工具




- Testnet 水龙头：https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet
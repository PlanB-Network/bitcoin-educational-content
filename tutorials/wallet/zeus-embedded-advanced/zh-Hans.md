---
name: Zeus 嵌入式 - 高级
description: 多节点自守型 Wallet
---

![Zeus](assets/cover.webp)


## ZEUS Wallet 简介


ZEUS 是一款移动 Bitcoin Wallet 和节点管理应用程序，具有 Bitcoin 闪电 Wallet 的全部功能，可让 Bitcoin 支付变得简单，让用户完全控制自己的财务，并让更高级的用户从掌上管理他们的闪电节点。


### ZEUS 为谁服务？

目前，ZEUS 适用于运行自己的 [Lightning Network Daemon (LND)](https://lightning.engineering/) 或 [Core Lightning lightning (CLN)](https://blockstream.com/lightning/) 家庭/企业节点并通过 Zeus 进行远程管理的用户。


使用 [BTCPay](https://btcpayserver.org/) 或 [LNBits](https://lnbits.com/) 或 [Alby](https://getalby.com/) 的商户（或任何其他 LNDhub 账户）也可以从 ZEUS 连接、使用和管理其节点/账户。


[从v0.8版开始](https://blog.zeusln.com/zeus-v0-8-0-open-beta/)，ZEUS将通过[内置移动闪电节点](https://docs.zeusln.app/category/embedded-node)和集成的[闪电服务提供商（LSP）](https://docs.zeusln.app/lsp/intro)，开始迎合那些只想通过移动设备进行快速、廉价的Bitcoin支付的普通用户的需求。


### 重要的宙斯资源：


- 宙斯官方网页 - [https://zeusln.app/](https://zeusln.app/)
- 宙斯文档 - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [宙斯 Github 存储库](https://github.com/ZeusLN/zeus)
- [Zeus Telegram 支持小组](https://t.me/ZeusLN)
- [NOSTR上的宙斯](https://iris.to/zeus@zeusln.app)
- [宙斯博客公告](https://blog.zeusln.com)


### 宙斯功能

#### 一般特征


- 自我监护，仅 Bitcoin 和 Lightning Wallet
- 无手续费，无 KYC
- 完全开放源代码（APGLv3）
- 支持多节点/账户（您可以管理自己的家庭节点、运行嵌入式 LND 节点、连接到多个 LNDhub 账户
- 易于使用的活动菜单
- PIN 或 passphrase 加密，隐私模式 - 隐藏您的敏感数据
- 联系簿、多主题、多语言


#### 技术特点


- 通过 Tor 连接
- 完全支持 LNURL（支付、提款、认证、通道），发送至 Lightning 地址
- 详细的照明通道管理、MPP/AMP 支持、Keysend、路由费管理
- Replace-by-fee (RBF)和子女为父母支付费用(CPFP)支助
- NFC 支付和请求、签署和验证信息
- 支持 SegWit 和 Taproot
- 简单的 Taproot 通道
- 自我监护闪电地址 (@zeuspay.com)
- Square 销售点（即将开放 PoS）


### 指南和视频教程

为了能够使用 Zeus 并管理闪电渠道、流动性、费用等，最好先阅读一些有关 Lightning Network 的重要指南。


#### 指南：


- [LND - Lightning Network Daemon Documentation](https://docs.lightning.engineering/)
- [CLN - 核心闪电文档](https://lightning.readthedocs.io/index.html)
- [初学者闪电指南](https://bitcoiner.guide/lightning/) - by Bitcoin Q&A
- [闪电节点管理](https://www.lightningnode.info/) - 作者：openoms
- [Lightning Network与机场类比](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [管理闪电节点流动性](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [闪电节点维护](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### BTC 会话视频教程


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## 如何在移动设备上开始使用 Zeus LN 嵌入式节点的简要指南


![Image](assets/en/01.webp)


我将这本指南献给所有希望在移动设备上使用自我监护节点 Wallet 开始新的主权之旅的 Lightning Network （LN）新用户。


让我们考虑一下，您已经通过了所有这些大量的托管 LN 钱包，但您还没有准备好开始运行 PUBLIC 路由 LN 节点，您只是想以一种更加自我托管的方式在 LN 上堆叠更多的 Sats，并通过 LN 定期付款。


Zeus来了，从[在其博客上公布的v0.8.0版本](https://blog.zeusln.com/new-release-zeus-v0-8-0/)开始，现在在应用程序中提供嵌入式LND节点。在此之前，Zeus 只是一个远程节点管理应用程序 + LNDhub 账户。但现在......节点就在手机里！


![Image](assets/en/02.webp)


### 快速回顾 Zeus Node 的主要功能：



- 私有 LND 节点** - 这意味着该节点不会通过您的节点公开路由他人付款。该节点和通道是不公开的（私有的，在公开的 LN 图表上不可见）。接收和付款将通过您连接的 LSP 对等节点完成。请记住：Zeus 嵌入式节点不会进行公开路由！
- 持久 LND 服务** - 用户可以激活此功能，使 LND 服务像任何普通 LN 节点一样持续激活。应用程序无需打开，持久服务将保持所有通信在线。
- 中微子区块过滤器** - 使用[区块过滤器和中微子协议](https://bitcoinops.org/en/topics/compact-block-filters/)进行区块同步（不考虑用户的 On-Chain 资金信息）。提醒：对于高延迟/慢速网络连接，基于中微子的区块同步有时可能会失败。尝试切换到邻近的中微子服务器有助于恢复同步。如果没有同步，您的 LND 节点将无法启动！
- 简单的 Taproot 频道** - 关闭这些频道时，用户产生的费用较少，并可获得更多隐私，因为在检查其 On-Chain 足迹时，它们似乎与任何其他 Taproot 消费一样。
- 集成 LSP** - Olympus 是 Zeus 新的 LSP 节点。用户可以直接通过 LN 接收 Sats，而无需事先设置 LN 信道。只需创建一个 LN Invoice，并使用 Zeus 0-conf 频道服务从任何其他 LN Wallet 支付即可。点击此处了解更多关于 Zeus LSP 的信息。LSP 还通过向用户提供隐藏节点公钥的封装发票，向付款人提供更多隐私保护。
- 联系人簿** - 您可以手动保存联系人或从 NOSTR 中导入，以便轻松向您的固定目的地发送付款。
- 完全支持 LNURL、LN Address 发送和接收** - 现在您可以通过 @zeuspay.com 设置自己的自助托管 LN Address。提醒：您还可以在可以使用 LN 身份验证登录的网站上使用 Zeus 进行 LN-auth。非常方便。
- 销售点** - 现在商家用户可以设置自己的产品项目，并直接从 Zeus 销售，同时集成 PoS。目前包含基本需求，但未来将包含扩展功能。
- LND 日志** - 用户可以实时读取 LND 服务日志，并利用日志调试可能出现的问题（主要是连接不良）。
- 自动备份** - LN 节点通道在奥林巴斯服务器上自动备份。该自动备份与节点 Wallet seed 一起加密（没有 seed 则完全无用）。用户还可以手动导出 SCB（静态通道备份），用于灾难恢复。


### 如何使用 Zeus LN 节点（嵌入式 LND）


在本指南中，我将只讨论嵌入式 LND 节点，而不讨论使用这一宏伟应用程序的其他方式（远程节点管理和 LNDhub 账户）。关于其他类型的连接，请参阅[Zeus 文档页面](https://docs.zeusln.app/category/getting-started)，那里有很好的解释，无需编写专门的指南。


#### 步骤 1 - 初始设置


由于宙斯是一个完整的 LND 节点，我将提出一些初步建议：



- 请勿使用旧设备，否则会影响这款功能强大的应用程序的使用。尤其是在同步期间，该应用程序会大量使用 CPU 和 RAM。缺少这些资源甚至会导致无法使用 Zeus 应用程序。
- 至少使用 Android 11 作为移动操作系统，并尽可能多地更新。对于 iOS 也是一样，尽量使用更高版本的操作系统。
- 数据存储至少需要 1GB 磁盘空间。随着时间的推移，空间可能会越来越大，但有一种功能可以将数据库压缩到 MB 级。
- 没有必要将 Zeus 与 Tor 或 Orbot 服务结合使用。请不要将事情复杂化。在这种情况下，Tor 不会为您提供更多隐私，只会让初始同步变得更糟。使用 VPN 时也要小心，并检查连接到 Neutrino 服务器的延迟。请记住，Neutrino Block filter 不会泄露或追踪您的设备身份，只是提供拦截服务。LN 的流量也是通过私密通道的 LSP 传输的，因此泄露的信息非常少，没必要担心隐私问题。
- 请耐心等待初始同步，可能需要几分钟。尽量使用延迟较好的宽带网络连接。如果您运行自己的 Bitcoin 节点，[您可以激活中微子服务](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) 并将您的宙斯连接到自己的节点，甚至使用内部局域网，这样您将获得最高速度。


设置连接类型为 "嵌入式节点 "后，应用程序将开始同步一段时间。耐心等待完成这部分，然后进入主设置页面。


![Image](assets/en/03.webp)


简而言之，在开始使用 Zeus 之前，让我们深入了解每个 "设置 "部分，并了解其中的一些主要功能：


**a - 设置**


该部分包含整个应用程序的常规设置


**1 - 闪电服务提供商（LSP）**


下面介绍两种 LSP 服务：



- _Just in time channels_ - 当您没有打开任何通道或没有可用的入站流动性时，如果激活了该服务，它将为您即时打开一个通道。如果不想打开更多此类通道，可禁用此选项。
- _提前申请通道_ - 您可以直接在应用程序中通过多种选项和金额（入站和出站）从奥林巴斯 LSP 购买入站通道。


LSP 通过为用户节点开辟支付渠道，帮助用户与 Lightning Network 连接。[点击此处了解有关 LSP 的更多信息](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992)。ZEUS 集成了一个新的 LSP，名为 [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581)，所有使用新嵌入式节点的用户都可以使用。


在本节中，默认设置为奥林巴斯 LSP (https://0conf.lnolymp.us)，但您也可以很快设置另一个支持该协议的 0conf LSP。


牢记：_

当您使用包装好的 LN 发票与奥林巴斯 LSP 开通渠道时，您还可以获得 10 万欧元的入站流动资金！如果您需要立即收到更多的 Sats，这是一个非常好的选择。

例如：您存入 40 万 Sats 以打开 LSP 通道，那么 LSP 将向您的宙斯节点打开一条容量为 50 万 Sats 的通道，并将您存入的 40 万 Sats 推向您的一方。

_"入站流动性"=渠道中更多的接收 "空间"________________________。


我们希望将来能有许多其他的 LSP 可以集成到 Zeus 中并交替使用。新的 LSP 将采用开放标准来处理此类 0conf 通道，这只是时间问题。


如果不想 "即时 "打开新通道，可以禁用该选项。


在同一部分中，当 LSP 向您的 Zeus 节点打开通道时，您还可以选择 "请求简单 Taproot 通道"。这些 "简单 Taproot 频道 "提供更好的 On-Chain 私密性和更低的频道关闭费用。您不想使用它们的原因只有两个：



- 它们是新产品，在使用它们时，LND 中可能仍存在错误。
- 你的对手不支持它们。目前，即使是 LND 节点也必须明确选择加入。


**2 - 付款设置**


该功能将为您提供通过 LN 或链上支付设置自己偏好的费用的方法。还可以选择增加或减少发票的超时时间。


如果 LN 付款失败，您可以增加费用，以找到更好的路线。此外，如果您正在进行链上 tx，您可以设置特定的费用，这样您的 tx 就不会在高费用时期长期停留在 Mempool。


**3 - 发票设置**


本节提供了 generate 发票的一些选项：



- 设置要在 Invoice 和 generate 中显示的标准备忘录
- 过期时间（以秒为单位），如果您希望 Invoice 在特定时间（更长或更短）内付款
- 包含路由提示--提供信息以查找非公开或私人通道。这样就可以将付款路由到网络上不公开的节点。路由提示提供了接收方专用节点与公共节点之间的部分路由。接收方生成的 Invoice 中会包含该路由提示，并提供给付款方。我建议在默认情况下启用路由提示，否则接收方的付款可能会失败（找不到路由）。
- AMP Invoice - 原子多路径支付是由 LND 实现的一种新型闪电支付，允许使用 [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) 在没有特定 Invoice 的情况下接收 Sats。实际上是一种静态支付代码。[更多信息请点击](https://docs.lightning.engineering/lightning-network-tools/LND/amp)。
- 显示自定义预览字段 - 只有在非常特殊的情况下，即您确实希望在预览中使用自定义字段时，才使用此选项。[Read more here](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


本节的另一个选项是如何设置要使用的链上 Address 类型：嵌套 SegWit、SegWit、Taproot。


![Image](assets/en/04.webp)


点击顶部的滚轮按钮，会弹出一个屏幕，选择所需的 Address 类型。设置完成后，下次点击链上接收按钮时，generate 就会显示所选的 Address 类型。您可以随时更改。


**4 - 频道设置**


在这一部分，您可以预先设置一些开放频道的功能，例如



- 确认次数
- 宣布频道（默认为关闭），这意味着它将是未宣布的频道
- 简单的 Taproot 通道
- 显示频道购买按钮


**5 - 隐私设置**


在这里，您可以找到一些基本设置，以便使用 Zeus 应用程序增加更多隐私：



- Block explorer 打开 tx 详情（Mempool.space、blockstream.info 或自定义的个人版本）
- 读取剪贴板 - 如果希望 Zeus 读取设备剪贴板，请切换开/关选项
- 潜伏者模式 - 如果您想从 Zeus 应用程序中隐藏特定的敏感信息，可切换开/关模式。当您制作演示或截图时，这是一个不错的选择。
- Mempool 费用建议 - 如果要使用 [Mempool.space](https://Mempool.space/) 中的建议费用水平，请激活此选项。


**6 - 安全**


该部分在打开应用程序时只有两个安全选项：设置密码或 PIN 码。


设置密码打开应用程序后，您还可以设置 "胁迫密码"。只有在胁迫情况下，如果你受到威胁，才会使用这个额外的秘密 PIN 码。如果您设置了这个 PIN 码，配置将被全部删除。因此，您最好不断更新备份。自动备份默认是开启的，但您也可以在设备外自行备份。


**7 - 货币**


启用或禁用在 Zeus 应用程序使用中显示法定货币换算的选项。目前支持全球 30 多种法定货币。


**8 - 语言**


您可以在多种翻译语言之间切换，Zeus 社区会以母语进行审核。


**9 - 显示**


在此部分，您可以个性化 Zeus 显示屏，选择各种颜色主题、默认屏幕（小键盘或余额）、显示节点别名、激活大键盘按钮、显示更多小数位。


**10 - 销售点**


这是一项特殊功能，用于启用/禁用 Zeus 中的集成 PoS 系统。您可以运行独立的 PoS 系统，也可以与 Square PoS 系统连接。目前，Zeus 只支持 PoS 的基本功能，但足以作为一个良好的开端，并能帮助那些小商户（酒吧/餐馆、杂货店）开始以本地方式接受 BTC。


在该设置中，您可以找到设置 PoS 的各种选项：



- 确认付款类型：仅 LN、0-conf、1-conf
- 为操作 PoS 的员工启用/禁用提示
- 显示/隐藏键盘
- 机票上适用的税率
- 创建产品和产品类别
- 所有销售的简单列表


下面是如何使用 Zeus PoS 的现场演示视频：


**B - 后备 Wallet**


ZEUS 中的嵌入式节点基于 LND 并使用 [aezeed seed 格式](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md)。这与您在大多数 Bitcoin 钱包中看到的典型[BIP39 格式](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki)不同，尽管看起来很相似。Aezeed 包含一些额外的数据，包括 Wallet 的出生日期，这将有助于在恢复过程中更有效地重新扫描。


aezeed 密钥格式应与以下移动钱包兼容：Blixt、BlueWallet 和 Breez。请注意，如果您有打开或等待关闭的通道，仅 seed 将不足以恢复您的所有余额！


有关备份和还原过程的更多信息，请访问 [Zeus Docs 页面](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery)。


电源建议：保存 seed 时，请同时保存节点的发布密钥！有时，将其与 seed 和 SCB（静态信道备份）一起保存在手边，以备需要验证恢复时使用。


只有打开 LN 通道时，才需要 SCB。如果只有链上资金，则不需要。


如果过了很长时间仍未显示旧的历史 txs，请进入 "嵌入式节点"-"对等节点"，禁用 "使用选定对等节点列表 "选项（默认为 btcd.lnolymp.us）。这将触发重启，并以更好的时间响应连接到第一个可用的中微子节点。或者使用下面提到的其他知名中微子节点。


如果您想了解 LND 节点的更多恢复选项，[请阅读我以前的指南](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html)，在那里您可以找到如何将已封堵的 seed 导入麻雀 Wallet 的步骤或其他方法。


**C - 嵌入式节点**


在本节中，我们将找到一些管理集成节点的基本工具：



- _Disaster Recovery_ - LN 频道的自动和手动备份。请在 Zeus 文档页面阅读更多关于如何使用此功能的信息。
- _快速图表同步_ - Zeus 应用程序将从专用服务器下载 LN 八卦数据图表，以实现更快更好的同步，并提供最佳支付路径。您还可以选择在启动时清除以前的图表数据。
- _Peers_ - 用于管理中微子对等设备和 0-conf 对等设备的部分。如果在初始同步时遇到问题，通道无法上线，这是因为设备与已配置的中微子对等设备之间的延迟较高。请尝试切换首选对等设备列表或添加特定的对等设备，因为您知道它的同步延迟更好。已知的中微子服务器有



 - btcd1.lnolymp.us | btcd2.lnolymp.us - 适用于美国地区
 - sg.lnolymp.us - 亚洲地区
 - btcd-Mainnet.lightning.computer - 适用于美国地区
 - uswest.blixtwallet.com （西雅图） - 适用于美国地区
 - europe.blixtwallet.com（德国） - 适用于欧盟地区
 - asia.blixtwallet.com - 适用于亚洲地区
 - node.eldamar.icu - 适用于美国地区
 - noad.sathoarder.com - 适用于美国地区
 - bb1.breez.technology | bb2.breez.technology - 适用于美国地区
 - neutrino.shock.network - 美国地区



- _LND 日志_ - 非常有用的工具，可用于调试 LN 节点问题，并以更高的技术水平深入了解问题所在。
- 高级设置_ - 控制 LND 节点使用的更多工具：



 - _Pathfinding mode_ - bimodal or apriori，为您的 LN 支付找到更好路线的方法，以及重置以前的路线信息。请阅读这些非常好的寻路指南：[寻路](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - 作者：Docs Lightning Engineering 和 [LN 支付寻路](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - 作者：Voltage
 - _Persistent LND_ - 如果您希望 LND 服务在后台持续运行，并让您的节点全天候在线，请激活此模式。如果您将 Zeus 用作小商店的 PoS，或者您正在通过 LN Address 接收许多 LN 提示，这将非常有用。
 - _Rescan wallet_ - 重启时，该选项将触发对 Wallet 所有链上 tx 的全面扫描。只有在 Wallet 丢失某些 tx 的情况下才可激活该选项。重新扫描任务需要几分钟的时间，因此请耐心等待，并随时查看日志以了解进度详情。
 - _Compact Database_ - 如果您的 Zeus 应用程序占用了大量设备空间（请参阅设备设置中的应用程序详情），该选项将非常有用。如果您使用 Zeus 的活动很多，我建议您经常进行压缩。一旦发现 Zeus 应用程序有超过 1-1.5GB 的数据，请执行压缩。它会重新启动并需要一些时间，请耐心等待。
 - 删除中微子文件（Delete Neutrino files）_ - 该选项用于删除中微子文件（重启时），可大大减少数据存储空间的使用。减少数据用量对电池使用也有很大影响，尤其是在持久模式下使用 Zeus 时，可以减少电池用量。


**D - 节点信息**


在本节中，您可以找到有关 Zeus 节点状态的更多详细信息，如



- 别名 - 短节点 ID
- 公开密钥 - 您节点的完整公开密钥，其他节点需要它才能找到通往您节点的路径。请记住，常规 LN 探索器（Mempool、Amboss、1ML 等）上看不到此公钥。只有通过您已连接的 LN 对等节点和频道才能获取此公开密钥。
- LN 实施版本
- Zeus 应用程序版本
- 已同步到链和已同步到图表状态 - 这两项非常重要，可显示节点的正确状态。如果这两项没有显示 "true"（真），就意味着您的节点仍在同步或同步过程中遇到了一些问题。因此建议查看 LND 日志或再等一段时间。
- 区块高度和 Hash - 显示节点看到并同步的最后一个区块和 Hash。


**E - 网络信息**


本部分显示从图表同步数据中提取的有关 Lightning Network 一般状态的更多详细信息：可用公共频道数、节点数、僵尸频道数（脱机或死亡）、图表直径、图表的平均和最大程度。


这些信息数据可能对调试有用，也可能只是用于统计。


**F - 闪电 Address**


在此部分，用户可以设置自己的自我托管 LN Address @zeuspay.com。


ZEUS PAY 利用用户生成的预图像哈希值、HODL 发票和 Zaplocker Nostr 验证方案，允许可能无法全天候在线的用户接收静态闪电 Address 付款。用户只需在 24 小时内登录自己的 ZEUS 钱包，就可以领取付款，否则付款将退回给发款人。


如果您激活 "持续模式"，您的 LN Address 将立即收到所有付款。


了解 [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) 支付的工作原理以及更多有关 [ZeusPay 费用](https://docs.zeusln.app/lightning-Address/fees) 的信息。


**G - Onchain 地址**


在此部分中，您可以查看生成的链上地址，以便更好地控制硬币


**H - 联系方式**


Zeus 0.8.0 版中引入了一个新的联系人簿，您可以用它快速向亲朋好友发送付款，还可以从 Nostr 中导入联系人。


只需输入您的 Nostr npub 或人可读 NIP-05 Address，ZEUS 就会查询 Nostr 中的所有联系人。您可以从这里向联系人快速付款，或将所有或部分联系人导入本地联系人簿。


下面是如何配置和使用 Zeus 联系人的简短视频：


**I - 工具**


在这里，我们有多个分区，提供更多工具：



- _Accounts_ - 在此您可以导入外部账户/钱包、Cold 钱包、Hot 钱包，以控制或用作 Zeus 节点通道的外部资金来源。此功能仍处于试验阶段。
- _加速交易_ - 当您在 Mempool 中的 tx 被卡住并希望提高费用时，此功能会很有帮助。您需要从交易详情中提供交易输出，并选择所需的新费用。新费用必须高于之前的费用，并且要求您的链上 Wallet 有更多可用资金。


![Image](assets/en/05.webp)


您必须进入待处理 tx 并复制 txid 输出点。然后转到此部分并粘贴，然后选择您要用于提升的新费用。这时会弹出一个新的屏幕，显示推荐的费用，您也可以设置自定义费用。记住必须高于之前的费用。


最好在 Zeus onchain Wallet 中保留一个 UTXO 和一个最大容量为 100k 的 Sats，以便在必要时使用它来提升费用。



- _Sign or verify_ - 使用此功能，您可以用 Wallet 密钥签署特定信息。也可用于验证信息，以证明信息来自特定的 Wallet 密钥。
- _Currency converter_ - 一个计算 BTC 和其他法定货币之间汇率换算的简单工具。


**J--商品和支持**


在这里，您可以找到更多关于宙斯、在线商店、赞助商和社交媒体的信息和链接。


**K - 求助**


在最后一部分，您将找到 Zeus 文档页面、Github 问题（如果您想直接向应用程序开发人员发布错误或请求）和电子邮件支持的链接。



### 步骤 2 - 开始使用宙斯节点



请记住，Zeus 主要用作 LN Wallet，用于通过 LN 方便快捷地付款。当然，它也包含一个链上 Wallet，但只能用于打开/关闭 LN 通道，而不能用于咖啡的定期支付。


请阅读我的其他指南[如何使用 Stash 的 3 个级别成为自己的银行](https://darth-coin.github.io/beginner/be-your-own-bank-en.html)。


此时，用户有两种方式开始使用 Zeus：



- 直接通过 LN，使用奥林巴斯 LSP 的 0-conf 信道
- 首先在链上 Wallet 存款，然后与您想要的同行打开一个普通的 LN 渠道。


#### 方法 A - 使用奥林巴斯 LSP


这是让新的 LN 用户使用 Zeus 的一种非常简单直接的方法。它可以是一个没有任何 Sats 帐户的全新 Bitcoin 用户，也可以是一个由朋友介绍加入的新用户，或者是一个首次使用 LN 付款的新商户。


默认情况下，Zeus 将使用自己的 LSP（奥林巴斯）。但随后您也可以切换到其他支持这种 0conf 协议的 LSP 来打开通道。


只需在您的 Zeus 上创建一个 Invoice（输入金额并点击 "申请 "按钮），您就能立即收到这些 Sats。


您 generate 的 Invoice 将被 [包裹](https://docs.zeusln.app/lsp/wrapped-invoices)，如果您支付了服务相关费用，您将看到相关费用。封装后的 Invoice 包含指向您的 Zeus 节点的路由提示，因此 LSP 可以找到您的新节点，并为您存入的新资金打开通道。


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


为了从 LSP 获得一个 LN 频道，并在第一时间收到您想要的资金，必须从另一个 LN Wallet 支付这个 Invoice，然后等待片刻，直到 LSP 向您的宙斯节点打开通道，扣除费用并将剩余的付款金额推送到您的通道一侧。


您只需用另一个闪电 Wallet 支付 ZEUS 中为您生成的 Invoice 费用，您的通道就会立即开通。[请查阅宙斯 LSP 费用](https://docs.zeusln.app/lsp/fees)。


支付通道的另一个好处是零费用路由。这意味着在路由付款时，通过 OLYMPUS by ZEUS 的第一次跳转不会产生路由费用。请注意，超出 OLYMPUS by ZEUS 的跳转仍会向您收取费用。


频道准备就绪后，点击屏幕下方显示 Zeus 频道的右侧按钮。


![Image](assets/en/08.webp)


你会看到这样一个通道，显示你这边的通道平衡：


![Image](assets/en/09.webp)


您从该渠道支出的资金越多，流入的流动资金就越多。从该渠道获得的 Sats 越多，流入的流动性空间就越小。


下面是关于 LN 信道如何工作的简单直观演示（由 Rene Pickhardt 制作）：


此时，考虑到频道的演示屏幕，点击频道名称，您将看到有关该频道的更多详细信息。


您与奥林巴斯之间有一个单通道，总容量为 490 000 Sats，您这边的余额为 378 000 Sats，奥林巴斯这边的余额为 88 000 Sats。这意味着在同一通道中，您最多可以多接收 88k Sats。


如果您需要接收超过 88k Sats（本例中的可用入站流动性）的数据，例如再接收 500k Sats，只需创建一个新的 LN Invoice，就会触发向奥林巴斯 LSP 提出的新通道请求。因此，您将获得第二个通道。


因此，为了避免因打开多个通道而支付更多费用，建议首次打开较大的通道，例如 1-2 百万 Sats。一旦开通，您可以使用本指南中介绍的任何外部交换服务，将这些 Sats 的一部分（例如 50%）交换到链上。


一旦您从该通道换出，比如说换出 50%，并将 Sats 装回您自己的 Zeus onchain Wallet，您就可以进入下一个打开新通道的方法--从链上平衡。


#### 方法 B - 使用链上余额


使用这种方法，您可以打开通往任何其他 LN 节点的通道，包括同一个奥林巴斯 LSP。但如果您已经与奥林巴斯建立了通道，建议您也与另一个节点建立通道，这样更可靠，而且还可以使用 MPP（多部分支付）。


![Image](assets/en/10.webp)


以上是使用 MPP 支付 LN Invoice 的示例。正如您所看到的，在屏幕底部有 "设置"，并将打开一个下拉页面，其中包含有关您即将进行的支付的更多详细信息。在该页面中，如果您至少打开了 2 个通道，则 MPP 功能默认为打开。此外，您还可以激活 AMP（原子多路径）并设置您想要的特定部分。这是一项强大的功能！


对于像宙斯这样的私人节点，我建议拥有 2-3 个良好的通道（最多 4-5）、良好的 LSP 和良好的流动性，以满足您通过 LN 支付或接收 Sats 的所有需求。[请参阅本指南中有关 LN 节点流动性的更多建议](/nodes/managing-lightning-node-liquidity-en.html)。此外，这里还有 Bitcoin 设计团队提供的另一份 [LN 流动性一般指南](https://Bitcoin.design/guide/how-it-works/liquidity/)。


我知道，选择合适的对等节点并不是一件容易的事，即使对经验丰富的用户来说也是如此。[因此，我先给您提供一些选择]（https://github.com/ZeusLN/zeus/discussions/2265），这些是我使用 Zeus 亲自测试过的对等节点（为了避免不兼容问题，我只尝试连接 LND 节点）。


这里还有一份 Zeus 已验证节点同行的列表。如果您知道好的节点，欢迎添加到列表中。


您可以通过点击主视图右下角的频道图标进入频道视图，然后点击右上角的 + 图标，在 Zeus 中打开一个频道。


![Image](assets/en/11.webp)


如果您想与某个特定节点打开通道，请单击（A）顶角扫描节点 QR nodeID（在 Mempool、Amboss、1ML 上可以获得该 QR），所有对等节点的详细信息都会填入。


提醒：


- Zeus 嵌入式节点不使用 Tor 服务！因此，请不要尝试与使用 Tor 服务的节点打开通道！您对自己造成的伤害比增加更多的隐私更严重。Tor 对于 LN 并不能提供更多的隐私，反而会增加更多的麻烦。
- 明智地选择你的同行，最好是好的 LSP、好的路由节点，而不是可能会关闭你的通道且无法提供良好流动性的随意的普通节点。[我在这里写了一份专门的指南](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) 介绍流动性和节点示例。


如果直接点击 "Open Channel to Olympus "按钮，则会弹出打开 [OLYMPUS by ZEUS]（https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581）通道所需的字段。


与付费 LSP 频道不同，您的频道需要使用您的链上资金（您可以在打开频道视图中从您的 UTXOs 中进行选择）进行 On-Chain 确认；它不会立即打开。请先咨询实际的 Mempool 费用，并根据您希望打开通道的速度进行相应调整。


在点击按钮打开频道之前，请向下滑动高级选项：


![Image](assets/en/12.webp)


您还需要确保该频道是未公开的（私人）频道。默认情况下，该选项对于已公布的频道是关闭的。不建议为 Zeus 嵌入式节点激活该选项，只有当您将 Zeus 作为公共路由节点与远程节点一起使用时，该选项才有用。


与付费 LSP 渠道不同的是，使用这种方法开通渠道不会享受零费用路由的好处。


完成后，只需点击 "打开通道 "按钮，等待矿工确认交易。一旦通道打开，您就可以通过您的通道随意交易 Sats。


请记住，这些渠道的所有余额都在您这边，所以您不会有流入的流动资金。正如我之前说过的，换掉或花一些 Sats 购买 LN 上的东西，以 "腾出更多空间 "来接收。


把 LN 频道想象成一杯水。你将一些水（Sats）倒入一个空杯子（你的渠道），直到装满为止。在你喝掉一些水之前，你不能再倒入更多的水。当杯子快空的时候，使用换入服务倒入更多的水 (Sats)。[点击此处了解更多关于外部交换服务的信息](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html)。


此外，还有其他 LSP 服务向您销售入站渠道：LNBig 或 Bitrefill。我想还有更多类似的服务，但现在想不起来了。


因此，如果您需要一个几乎是空的 LN 渠道（余额从一开始就 100%在对等方），以接收超过您现有已填满的渠道所能处理的付款，这可能是一个非常好的选择。您只需为开通这些通道支付一定的费用，就能获得大量的入站空间。



## 提示和技巧


### 入境储备限额


目前，由于 LN 代码的一些限制，无法准确接收 "入站 "中显示的金额。请始终牢记，您在开具发票时应略低于 "通道本地储备金 "的金额。


![Image](assets/en/13.webp)


如上图所示，"入站 "显示我仍能收到 5101 Sats，但事实上此刻已无法收到更多。您可以看到，这与 "本地储备 "的数量相同。


因此，请记住，当您开票收款时，也要考虑一下您的渠道流动性，如果您想把应收账款推到极限，就从该金额中扣除地方储备金。


### 给刚开始使用 Zeus 节点的新用户的快速建议：



- 正确把握新渠道。


例如，如果您知道一周内将收到 100 万 Sats，则应开设一个 200 万 Sats 通道，并将其交换到链上 Wallet 或另一个（临时）托管 LN 账户，占您外向流动性的 50-60%。随时准备好更多的流动性。一旦您需要更多的流动性回到 Zeus 通道，您可以将其从托管账户移回。


如果您知道自己每周将发送 500K Sats，那么就开设一个 100 万 Sats 频道。这样，在您重新填满之前，您仍有储备。



- 如果你是一个商家，而且你经常会收到比你花的更多的钱，那就购买一个专用的入站渠道。这是最便宜的方法。您只需支付极少的费用，就能获得一个 "空 "通道。



- 不要开设 50-100-300-500k Sats 的毫无意义的小通道。即使你只用它们来进行斩波，也会在几天内填满它们。打开更大的、不同的通道，而不仅仅是一个通道。


一旦您打开了一个更大的通道，您就可以随时使用外部潜艇交换将 Sats 移入您的链上钱包（包括返回宙斯链）。保持进出流动性之间的平衡是件好事，而且如果您愿意，还可以 "重复使用 "这些 Sats 来打开更多通道。


### 包裹的 Invoice


如果您想在接收时增加更多隐私，可以使用 "包裹 Invoice "方法。提醒：要做到这一点，您需要一个带有奥林巴斯 LSP 的通道。包裹发票将 "隐藏 "最终目的地（您的 Zeus 节点），并将您的 LSP 节点显示为付款人的目的地。


要获取包装好的 Invoice，请进入主键盘屏幕，输入金额并点击申请。将显示一个普通的 Invoice 二维码。现在，点击右上方的 "X "按钮，您将跳转到 Invoice 的更多选项。


![Image](assets/en/14.webp)


现在，您必须激活顶部的 "启用 LSP "选项，然后点击 "创建 Invoice "按钮。该选项将创建包装好的 Invoice，记住，会收取少量费用。


### 带有路线提示的发票


如果您想管理多个入站通道的流动性，这是一个非常有用的功能。实际上，您可以指定从哪个入站通道接收来自 Invoice 的 Sats。


该功能还可用于循环再平衡，即当您想将流动性从一个充满的通道转移到另一个耗尽的通道时。


如何创建带有路由提示的 Invoice？



- 在主屏幕上，向右滑动 LN 抽屉并点击 "接收"。
- 在 Invoice 设置页面的底部，激活 "插入路线提示 "按钮，然后选择 "自定义 "选项卡。它将打开一个屏幕，显示所有可用频道。选择要接收的频道。
- 填写所有其他 Invoice 详情、金额、备注等，然后点击 "创建 Invoice"。
- 支付 Invoice 将使 Sats 进入指定通道。


如果您想向自己支付该 Invoice（循环再平衡），当您从同一 Zeus 节点支付时，请在支付界面选择您希望用于发送付款的出站渠道（流动性更高的渠道）。


### 使用 Keysend 支付


Keysend 是一项被低估的 LN 功能，用户应该更多地使用它。


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend)允许 Lightning Network 中的用户直接向他人的公钥发送付款，只要他们的节点有公共信道并启用了 Keysend。Keysend 不要求收款人签发 Invoice。


那么，如何才能用宙斯做到这一点呢？


只需扫描或复制目标节点 ID（或使用 Zeus 联系人将常规目标节点保存为联系人），然后在 Zeus 主屏幕上点击 "发送 "按钮。然后在该界面粘贴节点 ID 或从联系人中选择。


输入 Sats 的金额和必要的信息（是的，您也可以将其用作 LN 的秘密聊天工具），然后点击 "发送 "按钮。完成！


![Image](assets/en/15.webp)


如果您与目的地同行有直接渠道，则不会产生任何费用。


如果您与目的地对等方没有直接通道，则 keysend 付款将作为普通 LN Invoice 付款支付费用，与其他付款一样在监管路径上路由。只是，请记住，它不会作为 LN Invoice 留下任何痕迹。


## 融合


我建议您阅读后续指南 [Zeus 的高级用法](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html)，其中包含更多说明和用例。


然后......就这样！从现在起，您只需将 Zeus Node 作为您手机上的普通 BTC/LN Wallet 使用即可。用户界面简单明了，易于使用，对任何类型的用户都很直观，我想我没有必要输入更多关于如何付款和收款的细节。


最后，这里有一张隐私对比图：


![Image](assets/en/16.webp)
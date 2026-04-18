---
name: 代客 Bitcoin
description: 代客将非托管闪电节点带入您的口袋
---

![cover_valet](assets/cover.webp)



## 导言


Valet 是一款轻量级自托管 Bitcoin 和 Lightning wallet，为初学者提供了简单方便的上机过程。它专门为 Bitcoin 社区和循环经济（尤其是偏远地区）量身定制。


它是**Simple Bitcoin Wallet (SBW)**的fork，具有名为**Fiat Channels**的高级托管闪电通道功能，旨在让任何人都能接受闪电支付，而不会有波动风险。


Valet 目前仅适用于安卓设备，可从多个开源应用程序商店下载安装。不过，出于对开发者隐私和 KYC 的考虑，Valet 并未***谷歌应用商店。



## 下载并安装 Valet


Valet 可从 Standard Sats' GitHub 页面下载 APK 文件。[Standard Sats](https://standardsats.github.io/) 是开发 Valet 的公司。


要下载 Valet，请访问标准 Sats [GitHub 页面](https://github.com/standardsats/valet/releases)，找到**最新**版本（通常是最上面的版本）。


👉转到**资产**，点击扩展名只有**.apk**的文件。下载将自动开始。


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


下载完成后，进入设备的**文件管理器** > **下载**，选择 Valet apk 文件。


![Select_valet_apk](assets/en/002.webp)


👉安装它，几秒钟后，你的应用程序就会准备就绪，出现在你的主屏幕上。


![valet_icon_on_homescreen](assets/en/003.webp)


或者，您也可以从 **F-Droid** 应用程序商店下载 Valet。如果您的设备上没有 F-Droid 应用程序，可以 [在此](https://f-droid.org/en/) 下载并安装。


在主屏幕上打开 F-Droid，搜索 **Valet**。从出现的两个选项中选择第一个带有**紫色和白色图标**的选项，然后点击**下载**。


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 下载后，单击**安装**并按照屏幕上的说明操作。安装完成后，您可以点击**打开**从 F-Droid 启动 Valet，或从设备的主屏幕启动它。



## 创建 Bitcoin Wallet


只需两个简单的步骤，您就可以在 Valet 上设置 Bitcoin wallet。


从设备的主屏幕或 F-Droid 应用程序启动 Valet。将出现 wallet 设置屏幕，其中有两个选项： **Create New Wallet** 和 **Restore Existing Wallet**。


👉 选择 **创建新 Wallet**，立即将创建一个新的 wallet，并将您重定向到主页。


![set_up_a\_new_wallet](assets/en/006.webp)



## 备份您的种子词


在 wallet 主页上，单击**Green 卡**，该卡上标有**"点按保存 wallet 恢复短语，以防丢失或更换设备"。


![seed_phrase_green_card](assets/en/007.webp)


👉 将显示一组 12 个英语单词。按照 1 到 12 的顺序将它们写在纸上，并妥善保管。


![the_seed_phrase](assets/en/008.webp)


### 请注意 ⚠️：


注意以下要素：


- 如您所知，Valet 是一种自我监护型 wallet，因此您的 seed 短语是恢复 Wallet 的唯一途径。
- 如果您丢失了 seed 短语，您将***永远无法访问您的 wallet。
- 如果有人得到了你的 seed 短语，他们就会无可挽回地偷走你所有的 Bitcoin 短语。


因此，您需要写下 12 个字的 seed 短语，并将其保存在安全的地方。千万不要截屏、将其保存为电子邮件草稿或保存在任何连接互联网的电子设备上。


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## 代客收发 Bitcoin


Valet 是一种具有 on-chain 和闪电 Bitcoin 功能的自保管 wallet。这意味着您可以通过**链**或**Lightning Network**从 Valet 接收和发送 Bitcoin。


不过，要想通过闪电接收或发送 Bitcoin，您需要用 on-chain Bitcoins 作为 Liquidity 建立一个闪电通道。或者，您也可以从供应商那里购买一些 Lightning 通道流动性。



## 生成链上 Bitcoin Address


要通过 on-chain 接收 Bitcoin，您需要生成一个 Bitcoin 地址。


在 wallet 主页上，您将看到一张**橙色**和一张**紫色**卡，分别标有**Bitcoin**和**闪电**。


点击标有 **Bitcoin** 的橙色卡片。您将跳转到显示 Bitcoin 地址的屏幕。


![click_on_Bitcoin_card](assets/en/009.webp)


👉您可以**复制**地址并将其发送给向您发送 Bitcoins 的人，或者点击**分享**按钮，通过社交媒体或其他通信渠道将二维码发送给对方。


您还可以点击 **编辑**按钮，设置发送到该地址的 Bitcoin 数量。


**注意：** 与发票一样，编辑功能在以下情况下非常有用：您可能希望在某个时间点收到某个地址的特定 Bitcoin 数量；但这并不意味着该地址不能收到更高或更低的数量。


点击**更多新地址**，生成新的随机地址。


![generating_a\_bitcoin_add](assets/en/010.webp)


您也可以点击 wallet 主页底部的**接收**按钮，生成 on-chain Bitcoin 地址。然后选择**接收到比特币地址**，继续上述相同的过程。


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## 通过链上发送 Bitcoin


通过 on-chain 从代客 wallet 发送 Bitcoin 是一项简单的任务。


在 wallet 主页底部，点击**发送**按钮，输入 Bitcoin 地址，或点击**扫描**，扫描地址二维码，然后点击**确定**。


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


输入您要发送的 Bitcoin 金额。您可以手动输入以 Sats 或法币计算的金额，也可以点击 **Max** 使用您所有的 on-chain 余额。


👉您还可以调整要为交易支付的费用，方法是点击标有**费用**的绿色小方框，然后向右或向左滑动白点，分别增加或减少费用。点击 **Ok** 发送交易。


![enter_amount_and_fee_rate](assets/en/015.webp)



## 设置 Lightning Network 频道


如上所述，Valet 是一种自托管 Bitcoin 和 Lightning wallet；因此，要想通过 Lightning 网络发送和接收 Bitcoin，您必须按照以下步骤先建立一个 Lightning 频道：


在主屏幕上，点击标有**闪电**的**紫色卡片**。您将进入包含以下选项的页面：



- 扫描节点 QR
- 在 LNBIG.COM 购买
- 在 BITREFILL.COM 购买
- 请求 LN 图形重新同步。


当您选择**从 lnbig.com 购买**或**从 bitrefill.com 购买**时，您将被重定向到这些公司的网站，在那里您可以购买多种容量的入站流动性。暂时忽略最后一个选项 **要求 LN 图表重新同步**。


因此，我们的首选是**扫描节点 QR**。此时，您必须已经决定并获得了您要打开通道的节点的**QR 码**。您可以选择向任何公共节点开放通道。查看 [1ML](https://1ml.com/) 或 [Amboss](https://amboss.space/)，选择您所选择的任何公共节点，然后扫描您所选择节点的相关二维码。


![channel_opening_options](assets/en/016.webp)


👉 您将自动跳转到下一个页面，在这里您必须为您的频道注资。再次强调，自管闪电网络的使用要求您使用 Bitcoin 为频道提供资金。这意味着您的 on-chain wallet 中必须有 Bitcoin，以便为 Lightning 频道提供资金。请参阅 [Hacken](https://hacken.io/discover/lightning-network/) 的这篇文章，了解有关闪电网络的更多信息。


![fund_channel](assets/en/017.webp)


👉输入您要为通道提供资金的 Bitcoin 的**数量**，或点击**最大**使用您所有的 on-chain Bitcoin 余额。您可以调整**费用**，或保留默认费用设置，然后单击**确定**。


**注意：** 您为通道提供的资金数额将是您的新通道的容量（即该通道可交易的 Sats 总量）。


同样重要的是，在开通通道时，您必须使用超过 **100,000 Sats** 的资金数额。这是因为很多 "闪电 "节点需要至少 100,000 Sats 的容量才能为其开通通道。因此，为了避免试错，只需使用高于该范围的金额即可。


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


此时，当您查看 wallet 主页时，您会看到您的注资金额已从**Bitcoin 卡**转移到**Lightning 卡**。在您的交易历史记录中，您会看到资金交易正在处理中。


![channel_funding_processing](assets/en/020.webp)


👉 如果点击 "闪电卡"，您将看到显示您的 "闪电 "通道正在打开的信息。您还会在交易列表中看到**通道融资交易**。等待您的融资交易在 blockchain 上确认，您的闪电通道就准备就绪了。


![channel_opening](assets/en/021.webp)


👉 资金交易一经确认，点击主页上的**闪电卡**，您就会看到有关您的闪电渠道的信息，如下所示：



- 用点隔开的一组随机数字：** 这些是节点的 IP 地址。(分别为 IPV4 和 IPV6）
- 容量：** 这是该通道可收发的 Sats 总容量
- 可发送量：** 这是您此时可发送的 Sats 数量。您会注意到，它与**容量**几乎相同。这是因为您尚未通过该渠道发送任何付款。
- CAN RECEIVE:** 这是您目前可以接收到的 Sats 数量。(此时几乎没有，因为要想接收，您必须先发送一些 Sats 以创建入站 Liquidity）。
- REFUNDABLE:** 此项显示关闭频道时返还到您 on-chain 地址的金额。这也被称为**频道的本地余额**。请注意，它只是略低于频道容量，这是因为在关闭频道时，您必须支付一定的费用才能在 blockchain 上发布关闭交易，就像您在为频道注资时所做的一样。因此，系统会扣除您要支付的最低金额（约为最低金额）。
- VALUE IN FLIGHT：** 当有人向您的频道发送一些 sats 时，或者当您尝试向某人发送一些 sats 时，无论出于什么原因，交易都会延迟，这通常会显示在此字段中。


![channel_info](assets/en/022.webp)


## 通过您的渠道发送 Sats


通过 Lightning Network 发送 Sats 非常简单。


👉在主页底部，点击**发送**，然后在提供的字段中**粘贴**闪电发票（必须已复制），或点击**扫描**扫描闪电发票二维码。


![click_send_or_scan](assets/en/023.webp)


大多数 "闪电 "发票都预设了付款金额。但在少数情况下，发票可能是开放式的，您必须填写金额。


👉以**美元**或**Sats**为单位输入金额，或点击**最大**，使用您的 "闪电 "通道上的所有余额，然后点击**确定**。一旦找到合适的路径，您的付款将在几秒钟内发送并完成。请留意主页，查看付款是否已完成。支付完成后，会出现一个绿色复选标记。


![enter_the_amount](assets/en/024.webp)


## 通过您的渠道接收 Sats


在您的 "闪电 "通道上接收付款在很大程度上取决于您是否有入站（inbound）Liquidity。打开通道后，您至少要向通道连接的另一端发送一些 Sats 以**创建入站流动性**，才能接收付款。要确认是否可以接收 Sats 以及可以接收的 Sats 数量，请检查您的渠道信息中的**可以接收**字段。这将显示您在每个时间点收到的 Sats 数量。


现在，假设您已经从通道发送了一些 Sats，您现在有了入站流动性，可以接收 Sats。


要在 Lightning 频道上接收，您必须生成发票。与使用地址的 Bitcoin on-chain 不同，闪电网络使用发票。在 Valet 上生成发票有两种途径。


#### 方案 1


在主页底部，点击**接收**，选择**接收到闪电发票**。在发票中填写要接收的金额，然后点击**确定**。复制发票或与付款人共享二维码。


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### 方案 2


点击 wallet 主页上的紫色闪电卡。点击频道上的任意位置，弹出选项列表。选择**接收到频道**，然后输入您接收的金额（Sats 或美元）。在填写发票时，您还会看到可以接收的 Sats 数量（入站容量）。点击 **Ok** 并复制发票或与付款人共享二维码。


![receive_to_channel](assets/en/028.webp)


**注意：** 第一个选项是通用选项，这意味着如果您有多个活动频道，并使用第一个选项，系统将自动选择其中一个频道接收 Sats。


因此，在这种情况下，如果您想接收某个特定频道的 Sats 信号，最好使用第二个选项。


### 频道弹出选项说明


点击频道后，将显示以下选项字段：


![channel_pop_ups](assets/en/029.webp)


**共享 LIGHTNING 频道详细信息：** 通过此功能，您可以共享您的频道详细信息，如远程对等 ID、本地频道 ID、资金交易、创建日期等。


**关闭钱包通道：** 您可以随时关闭您的闪电通道。关闭通道时，系统会检查您在自己通道一侧的 Bitcoin 余额（请记住**"可发送 "**字段，也称为本地余额），然后将余额发送给您。在代客操作中，您可以选择在关闭通道时将 Bitcoin 发送到哪里。因此，**关闭通道至 wallet** 是您的两个选项之一。


👉 单击此选项，然后选择 **Bitcoin**。通道关闭将开始，您的通道 Bitcoin 余额将发回 wallet 的 on-chain 地址。


![close_channel_to_wallet](assets/en/030.webp)


**关闭通道至 ADDRESS：** 这是关闭通道的第二个选项。选择此选项时，系统会提示您输入一个 wallet 地址，您通道上的 Bitcoin 余额将被发送到该地址。请注意，在此选项中，您只能扫描要关闭频道的 Bitcoin 地址的二维码。目前没有手动粘贴地址的选项。


点击该选项，扫描 Bitcoin 地址，然后点击 **确定**。通道关闭将开始，您的闪电 Bitcoin 余额将发送到您扫描的地址。


![scan_address_and_Ok](assets/en/031.webp)


**RECEIVE TO CHANNEL：** 这与生成发票的功能相同，但在某些情况下，您可能拥有不止一个渠道，包括 Fiat 渠道（在 Valet wallet 中可获得的一种独特的闪电渠道）。因此，如果您开通了多个渠道，该选项可确保您能收到特定渠道的付款。


**从其他通道充值：** 该选项允许您从其他现有通道为一个通道充值。例如，如果您有两个不同的 "闪电 "频道（A 和 B），而 A 频道的 Bitcoin 余额已用完，那么使用此选项，您可以轻松地从 B 频道自动补足 A 频道的余额。


**DIRECT NOT PRIVATE RECEIVE:** 这也是一个生成发票以接收付款的选项，但使用该选项时，发件人会直接向您付款。这意味着付款不会像普通闪电付款那样，在到达你手中之前经过不同的节点。因此，从本质上讲，发件人知道他们支付的是你，知道你的通道 ID 等。当您从您信任的来源收款，且不需要保护您的隐私时，通常可以使用此选项。


## 托管和非托管频道


与许多其他 Bitcoin wallet 一样，Valet 也是一款简单、轻便的 Bitcoin 和 Lightning wallet。但它有一个独特的 Lightning 功能，使其有别于其他大多数 Bitcoin wallet。该功能被称为**托管和飞信通道**。


Fiat 通道是闪电实施的一种类型，可以轻松加入和使用闪电网络。它是一种托管解决方案，允许完全匿名，就像普通的闪电通道一样。菲亚特通道技术还能在闪电网络上创建 Bitcoin 衍生工具。例如，使用法币通道，商家可以接受价值稳定的 Bitcoin 支付，而不必担心 Bitcoin 的波动性。


Valet 当前的法定货币渠道实现了创建由 Sats 支持的稳定合成法定货币。它采用主机-客户关系，其中主机是提供该服务的任何 Lightning 节点，客户是 Valet 用户。这是一种托管解决方案，因为所有的 Sats 都在主机端；但是，发票生成、转矩路由和预图像生成仍在客户端进行，就像在普通的 Lightning 通道中一样。


打开一个 Fiat 通道的过程与打开一个 Lightning 通道的过程相同。唯一不同的是，在这种情况下，客户（代客用户）无需投入任何流动资金 on-chain 来创建通道容量。主机会为客户设置通道容量和路由所有付款。


要打开 Fiat 频道，请单击 wallet 主页上的紫色 **Lightning 卡**。选择 **扫描节点 QR**（此时，您必须已确定要打开通道的主机，并获得节点的 QR。标准 Sats 的 SATM 节点就是您可以打开 Fiat 频道的主机节点的一个例子）。


**注意：** 重要的是，任何人都可以成为主机。您只需运行一个带有**菲亚特频道插件**和**连接服务**的闪电节点。Fiat 频道是*Standard Sats*的一个开源项目。请在 [此处](https://github.com/standardsats/fiat-channels-rfc) 和 [此处](https://standardsats.github.io/) 阅读更多相关信息。


下面是 SATM 节点 QR：


![SATM_node_QR](assets/en/032.webp)


👉扫描节点 QR 后，点击**请求美元法币通道**或**请求欧元法币通道**（这是您的法币余额的报价面值）。现在，请选择美元，然后点击**确定**。通道将自动打开，您可以立即开始接收 Sats。就是这么简单


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉进入 wallet 主页，您会看到一张标有**USD**的**浅绿色**卡，这就是您的**菲亚特通道**。


![fiat_channel_card](assets/en/035.webp)


**注意：** 当您在法币渠道接收 Sats 时，您所接收的 Sats 的法币价值将被锁定为稳定余额，而 Sats 的交易量则随 Bitcoin 的价格浮动。这种解决方案主要是为那些希望接受 Sats 支付但又不想面对 Bitcoin 波动挑战的商家设计的。这可以帮助他们在任何时候都保持稳定的价值，同时还能在闪电网络上进行交易，享受 Bitcoin 作为 Lightning Network 的交易媒介所带来的全球影响力和快速结算。


创建 Fiat 频道时，您会看到以下值字段及其含义：


![fiat_channel_info](assets/en/036.webp)



- 用点隔开的一组随机数字：** 这些是节点的 IP 地址。(分别为 IPV4 和 IPV6）
- 服务器价格：** 这是主机向您提供服务的 Bitcoin 市场价格。这通常会与市场主要价格略有不同，因为主机可能会加一点溢价。这一价格完全由主机决定，因此不同主机的价格也会有所不同。
- FIAT BALANCE（法币余额）：** 这是您在此频道上收到的每个卫星的锁定稳定法币值。请记住，如前所述，只要您在菲亚特频道上接收到 Sats，接收时的 Sats 法币价值就会立即锁定为该字段中的合成稳定法币价值。您的**法币余额**值不会随 Bitcoin 市场价格波动。无论何时您想从这个渠道付款，都只能发送与该法定余额等值的 Sats。因此，您可以将其视为由 Sats 支持的数字法定货币。
- CAPACITY（容量）：** 这是可通过此通道发送和接收的 Sats 总音量。(这也由主机设置。与普通 Lightning 通道不同的是，该容量可由主机根据情况进行调整）。
- 可发送量：** 这是根据您的法币余额，您在每个点可以发送的 Sats 数量。这与您在普通 "闪电 "渠道中拥有的价值完全不同，因为该价值随 Bitcoin 价格浮动。因此，您在这里看到的是根据**服务器汇率**，您的法币余额在任何时候的 Sats 价值。
- CAN RECEIVE：** 这是目前该频道可以接收的 Sats 数量。创建频道后，该值应与频道容量相同。
- VALUE IN FLIGHT（飞行中价值）：** 当有人向您的频道发送 sats 时，或者当您尝试向某人发送 sats 时，无论出于什么原因，交易都会延迟，这通常会显示在此字段中。


以下是有关菲亚特渠道的重要注意事项：



- 与普通 "闪电 "频道不同，当您打开法定频道时，您可以立即开始接收 Sats，但不能发送。只有收到 Sats 后，才能发送 Sats。
- 在任何时候，发送和接收的资产都是 Sats。菲亚特余额*只是在任何时间点收到的Bitcoin价值的合成借据。因此，它不是 token 的创造物，也不是一种新的加密货币。
- 对于因担心 Bitcoin 波动而对接受 Bitcoin 支付持怀疑态度的商家/企业来说，法定货币渠道主要是有用的。对于那些希望用 Bitcoin 支付员工工资，而又不想承担 Bitcoin 波动带来的后果（这可能会使他们的工资资本不稳定）的公司来说，它也可能很有用。对于那些居住在 Bitcoin 主要使用地区，但生活费用固定的个人来说，这可能也很有用。
- 请注意，这里没有标有**可收回**的字段。这是因为从技术上讲，您无法关闭菲亚特通道。您只能通过将菲亚特通道的余额转入正常的 "闪电 "通道来停止使用该通道。


### 菲亚特通道弹出式选项说明


点击菲亚特闪电频道后，将显示以下字段：


![fiat_channel_pop_up](assets/en/037.webp)


**共享托管频道详细信息：** 通过此功能，您可以共享 Fiat 频道的详细信息，如远程对等 ID、本地频道 ID、创建日期等。


**EXPORT CHANNEL STATE：** 这可以让您在任何时候导出通道的状态。这通常在修复通道错误时非常有用，如果有需要，主机可能会要求您共享这一功能。


**DRAIN CHANNEL BALANCE：** 如前所述，从技术上讲，您无法关闭菲亚特通道，但您可以将通道余额转入现有的正常 "闪电 "通道。这会自动将相当于你的菲亚特余额的萨特转移到你的正常闪电通道中。


**RECEIVE TO CHANNEL：** 这与生成发票的功能相同，但在某些情况下，用户可能有不止一个菲亚特渠道，而且有不同的主机，包括正常的闪电渠道。因此，如果用户开通了多个渠道，此选项可确保他们能收到特定渠道的付款。


**从其他频道注水：** 该选项允许用户从其他现有频道注水。因此，使用此选项，您可以从普通频道或其他菲亚特频道为您的菲亚特频道注水，就像您可以放水一样。


**非私人接收：** 这也是生成发票接收付款的一个选项，但使用该选项时，发件人会直接向您付款。这意味着付款在到达你手中之前不会经过不同的节点。因此，从本质上讲，发件人知道他们支付的是你，知道你的频道 ID 等。当您收到来自您信任的来源的付款，并且不需要维护您的隐私时，通常可以使用此选项。


## 代客泊车设置：


与其他应用程序一样，Valet 也有应用程序设置，您可以根据自己的喜好进行调整。您可以从主屏幕进入设置页面。


👉在主屏幕上，点击屏幕右上角的**齿轮**图标进入设置。以下是设置部分的组件。


![settings_icon](assets/en/038.webp)


**本地频道备份已启用：** 如果该选项为**禁用，**则应将其启用，因为这是您卸载并重新安装 Valet 后恢复正常闪电频道的唯一方法。我们稍后会对此进行解释。所以点击这个，给Valet权限进入你的**媒体存储**，因为备份文件就保存在那里。


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**存储本地备份的位置：** 只要您授权 Valet 使用您的存储空间，该字段将自动设置为在您的**Downloads**文件夹中存储本地备份。但您也可以点击此处并选择任意文件夹进行更改。


**管理链式钱包** 这是一个有点技术性的问题，除非你有足够的经验，否则不需要为此费心。默认设置就可以了。


**ADD HARDWARE WALLET（添加硬件钱包）：** 除非您有硬件 wallet 需要连接和监控，否则也不必为此费心。使用此设置，您可以扫描和连接硬件 wallet，如 Trezor 或 Cold 卡，并监控其活动。这是一项仅用于观察的功能，这意味着您不能在此对硬件 wallet 执行交易。您只能观察和监控 wallet 的活动、余额等。


**SET CUSTOM ELECTRUM NODE:** 这也是技术性问题，除非你有足够的知识，否则不应该为此费心。默认设置就足够了。


**比特币单位：** 这是您希望 Bitcoin 余额的显示方式。第一个选项以 Satoshi 的形式显示余额，如 1,000,000 Sats，第二个选项以 BTC 的小数点显示余额，如 0.01BTC


**USE PIN AUTHENTICATION** 如果选中此复选框，则必须设置一个 PIN 或指纹，登录 wallet 和验证交易时必须输入该 PIN 或指纹。


**使用 Tor 连接：** 如果选中此复选框，您的交易将通过 Tor 网络进行。它增加了一层额外的隐私保护，但可能会导致支付吞吐量延迟，尤其是闪电支付。


**VIEW BIP39 RECORVERY PHRASE：** 在这里您可以访问您的 12 个字的 seed 短语，以进行备份。因此，如果你之前没有写下来，或者找不到写在哪里，只要你还能访问 Wallet，就可以从这里复制它。


**使用统计：** 显示自 wallet 创建以来您的所有交易和活动的摘要


![usage_stats](assets/en/041.webp)


## Wallet 回收


Valet 是一款非托管型 wallet，因此如果您丢失了设备或卸载了 wallet 应用程序，您需要进行 wallet 恢复才能找回您的 Bitcoin 和 "闪电 "频道。在本教程的开头，我们提到了写下 seed 12 字短语**的重要性，因为它是恢复 wallet 的关键。没有客户服务代表可以帮助您恢复 wallet。


恢复 Valet wallet 需要两个重要工具，这取决于您是否有激活的闪电通道。对于没有激活正常 Lightning 频道的用户，只需按照以下简单步骤，使用**12 个字符的 seed 短语**即可：


👉 安装新的 Valet 应用程序，并启动/启动该程序。


选择 **恢复现有的 Wallet**


![restore_existing_wallet](assets/en/042.webp)


👉仅选择**恢复短语**。


![select_recovery_phrase](assets/en/043.webp)


👉输入 12 个字的恢复短语，然后单击 **确定**。


![input_12_words](assets/en/044.webp)


您的 wallet 将被恢复。在这种情况下，只会恢复您的 on-chain Bitcoin 余额。


但是，如果您有一个激活的普通 "闪电 "频道，而您只用恢复短语恢复了您的 wallet，那么您的 "闪电 "频道将被强制关闭，您在该频道中的任何 Bitcoin 余额都将自动发送到您的 on-chain 余额中。


另一种恢复 Valet wallet 的方法是**使用保存在设备上的本地备份文件和 12 个字的 seed 短语**。如果您使用这两种方法，您的 "闪电 "频道状态将得到恢复，因此您的 "闪电 "频道不会被强制关闭。


步骤如下


👉 安装新的 Valet 应用程序，并启动/启动该程序。


选择 **恢复现有的 Wallet**。


👉 选择 ** 备份 + 恢复短语**。


![select_backup_and_recovery_seed](assets/en/045.webp)


从手机的文件管理器中选择备份文件。(默认情况下，它总是存储在**下载**文件夹中）。


![local_backup_file_in_download_folder](assets/en/046.webp)


选择正确的备份文件后，系统将显示提示，确认**"存在备份文件 "**，然后要求您输入 12 个字符的 seed 短语。


![enter_12_words](assets/en/047.webp)


输入 12 个字的恢复短语，然后单击 **确定**。您将进入 wallet 主页。


等待 Bitcoin 网络同步（**SYNC**）和 Lightning 节点同步（**LN Sync**）完成后，您的 wallet 将完全恢复，包括 Lightning 频道。


![LN_sync](assets/en/048.webp)


## 结论


Valet 是一种令人兴奋的 wallet 解决方案，其功能使其适用于新用户的加入。它还有一个菲亚特通道，这是一种并不太新颖的技术，可确保将菲亚特经营的业务整合到 Bitcoin 标准上。


今天就下载 Valet，试试吧🧡
---
name: 天氣
description: 面向零售商和消费者的闪电工具套件
---

![cover](assets/cover.webp)



在 Bitcoin 生态系统中，实时接受支付仍然是企业和个人面临的一大挑战。传统的解决方案往往需要先进的技术知识、复杂的基础设施来维护，或者需要由中介机构持有资金。尽管 Lightning Network 的技术进步前景广阔，但这种情况阻碍了 Bitcoin 作为日常货币的大规模应用。



Tiankii是一家诞生于2021年的萨尔瓦多公司，为解决这一问题，它提供了一个可访问的模块化Bitcoin基础设施。Tiankii 并不强制采用封闭的生态系统，而是提供一套相互关联的工具，使任何人都能将 Bitcoin Lightning 整合到自己的业务中，而不会牺牲对资金的控制。



## 什么是 Tiankii？



### 起源和理念



Tiankii（纳瓦特尔语，意为 "所有人都能进入的露天市场"）是萨尔瓦多第一家 100% Bitcoin 的初创公司。该公司由达尔文-奥特罗（Darvin Otero）在 Bitcoin 被采纳为该国法定货币后创立，旨在将 Bitcoin 从价值存储转变为日常购物的可交易货币。与托管平台不同，Tiankii 采用非托管方式，用户保留对其资金的控制权，基础设施仅充当技术中介。



### 技术架构



Tiankii 定位为基于 Lightning Network 的 Bitcoin 即服务基础设施提供商。这种第二层技术能以极低的成本实现近乎瞬时的交易，使小额支付和日常购物成为可能。



该架构以三大支柱为基础：



**闪电优先**：在保留 on-chain 对大额交易支持的同时，系统性地支持闪电网络，因为它速度快、成本低。



**开放标准**：使用 LNURL 自动处理支付请求，使用 Lightning Address 可读电子邮件 ID，使用 Bolt Card 实现可互操作的 NFC 支付。



**与wallet无关的模块化**：可连接不同的 Lightning 组合（LNbits、Blink、BlueWallet）或自己的节点，根据所需的专业知识和自主水平提供最大的灵活性。



## 天氣生態系統工具



### Bitcoin POS - 店内支付终端



该应用程序可将智能手机或平板电脑变成闪电终端。商户输入当地货币金额，应用程序就会生成闪电二维码或接受 Bolt 卡。交易即时入账，免收佣金，可自动转换 150 多种货币，并提供小费管理和销售历史记录。



### 商家仪表板 - 统一销售管理



Interface 网络集中连接其 wallet Lightning、实时跟踪交易、开具发票和 generate 会计报告。该平台汇集所有渠道：店内支付（POS）、在线销售（电子商务插件）或 API 集成。支付汇聚到所选的 wallet 上。



### Bitcoin 非接触式卡（Bolt 卡）



NFC Bolt 卡是 Tiankii 在实现 Bitcoin 大众化方面的重大创新。该卡的功能类似于非接触式银行卡，您只需在兼容的终端上轻点一下，即可支付 Bitcoin Lightning 消费。



与传统的托管解决方案不同，该卡采用开放式标准，保证了互操作性。用户可以通过 IBI 应用程序将其与自己的 wallet 相连，从而保留自己的私人密钥并完全控制相关资金。支付只需一秒钟，支付时无需拿出智能手机或连接互联网。



这一解决方案对不熟悉智能手机的人来说尤其具有包容性，为进入 Bitcoin 经济提供了一个无障碍通道。



### IBI App - Interface 单独 Bitcoin



IBI 应用程序（个人 Bitcoin Interface）专为希望每天使用 Bitcoin Lightning 的个人设计。其主要优势在于生成个性化的 Address Lightning，即可通过电子邮件格式读取的支付标识符（例如：alice@ibi.me）。



该标识符大大简化了收款过程：无需为每笔交易开具新的 generate 发票，发件人只需输入闪电地址即可。通过该界面，您还可以管理 Bolt 卡（激活、停用、消费限额），连接各种闪电钱包，并通过扫描二维码进行支付。



### 电子商务插件



与 WooCommerce、Shopify 和 Cloudbeds 的即用集成。安装只需几分钟，即可将 Bitcoin Lightning 添加到结账中。优势：零佣金（信用卡佣金为 2-3%）、即时结算、全球访问、消除退款。付款直接到达商家连接的 wallet。



### Bitcoin API 和开发工具



通过 Tiankii SDK，可以将 Bitcoin Lightning 集成到现有应用程序中，而无需维护自己的节点。API通过托管在谷歌云上的强大基础设施处理发票创建、付款验证和批量邮件。通过Address Lightning，指挥中心可为企业提供自定义域、批量支付以及NFC终端和卡片集中管理等服务。



## 安装和第一步



### 必要的先决条件



使用 Tiankii 无需复杂的技术前提。应用程序通过智能手机、平板电脑或电脑上的网络浏览器运行。无需安装本地应用程序：您只需访问互联网和最新的浏览器即可访问 IBI 或商家控制面板。



**适用于私人用户（IBI 应用程序）**：无需事先安装 wallet Lightning。当您创建账户时，Tiankii会通过[Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html)自动配置一个工作中的Address闪电，这是一个在后台使用Liquid网络的无节点实现。无需任何技术配置，您就可以立即接收和发送付款。该解决方案大大简化了初学者的接入，同时保持自我监管。



**针对商家（商家控制面板）** ：连接现有的 wallet Lightning 是使用销售终端和接收付款的必要条件。Tiankii支持多种解决方案：移动钱包（Blink，Strike），自托管解决方案（LNbits，LND/CLN节点）或网络钱包（Alby）。本教程的资源部分提供了详细的连接指南。



### 针对私人客户：IBI 应用程序



**创建账户



访问 accounts.ibi.me 创建账户。在此页面，您可以选择两种账户类型："个人使用 "用于个人用途，"商业使用 "用于商业用途。选择 "个人使用"，即可使用 Bitcoin 中的收款和付款工具。



![Choix du type de compte](assets/fr/01.webp)



选择 "个人使用 "后，您将自动跳转到 go.ibi.me 完成注册。您可以通过电子邮件、电话号码或使用谷歌、微软或 Twitter 账户完成注册。创建完成后，您可以立即访问您的 IBI 界面，您的 Lightning Address 已经开始运行。



![Création du compte](assets/fr/02.webp)



**Interface 主**



IBI 界面以卫星币和当地货币（美元）显示您的余额。您可以通过三个按钮进行互动："接收 "用于接收付款，"扫描 "用于扫描二维码，"发送 "用于发送卫星币。



![Interface IBI](assets/fr/03.webp)



**接收付款**



要接收卫星币，请按 "接收"。应用程序会自动生成一个 QR 码，并显示您的个性化 Address 闪电（nom@ibi.me 格式）。将此地址或 QR 码与发件人共享：资金会立即到达您的 IBI 账户。



![Réception avec Lightning Address](assets/fr/04.webp)



余额入账后，您可以使用这些 Satoshis 进行支付。



**发送付款**



要发送卫星币，请按 "发送"。您可以扫描闪电 QR 码，或直接输入闪电 Address 目的地。



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



输入所需的沙托西金额，查看等值的当地货币金额，然后确认付款。



![Confirmation du montant](assets/fr/07.webp)



成功通知确认发货，并提供详细信息：发送金额、交易费用和收件人。



![Paiement réussi](assets/fr/08.webp)



**账户管理



在 "设置 "中，您可以管理 Bitcoin NFC 卡（Bolt 卡）。通过该界面可以激活、停用或设置卡的消费限额。



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### 针对商户：商家控制面板和 POS



**创建企业账户



访问 accounts.ibi.me 创建账户。选择 "商业用途 "访问商家工具。此类账户可以访问商家控制面板和销售点终端。



选择 "商业用途 "后，您将自动跳转到商户控制面板 (pay.tiankii.com)。这将带您进入业务管理界面，包括收入跟踪、交易和支付工具。要开始接受付款，您必须首先通过点击页面顶部的链接（见图片上的箭头）连接您的 wallet Lightning。



![Dashboard marchand](assets/fr/11.webp)



**wallet Lightning** 连接



激活销售点的关键步骤：连接 wallet Lightning 接收付款。界面提供多种连接选项。请注意，有些选项（Bitcoin Onchain 和 Lightning Network）仍在开发中，在界面上显示为灰色。



![Options de connexion wallet](assets/fr/12.webp)



本教程使用 Lightning Address 连接，与 Chivo、Blink Wallet 和 Strike 兼容。输入您的 Lightning Address（nom@domaine.com 格式），例如来自 LN Markets、Alby 或任何其他兼容供应商的产品。



![Saisie de la Lightning Address](assets/fr/13.webp)



登录后，您的账户就可以运行了。现在您可以访问 POS 或返回仪表板配置其他设置。



![Connexion réussie](assets/fr/14.webp)



*付款链接** *付款链接



通过 "付款工具 "菜单可以访问 "付款申请"，创建和管理付款链接。该功能有助于生成个性化的付款链接，通过电子邮件或信息发送：捐款、单笔付款、多笔付款，甚至是保护内容的付费墙。您可以创建不同类型的链接，以满足您的业务需求。



![Liens de paiement](assets/fr/15.webp)



**销售终端配置**



要接受店内支付，请访问 "支付工具 "中的 "销售终端 "菜单。这部分允许您创建和管理 POS 终端（终端数量取决于您的计划，请参阅下面的免费计划与商业计划）。点击 "打开"，在浏览器中打开 POS 界面。



![Gestion des terminaux](assets/fr/16.webp)




**创造销售**



POS 终端显示一个数字键盘，用于输入销售金额。用当地货币输入金额（例如 500 sats 相当于 630.74 ARS），然后按 "OK "确认。



![Saisie du montant](assets/fr/17.webp)



该应用程序可立即生成一个 Lightning QR 码和一个 Lightning Address 用于支付。顾客可以用 wallet 扫描二维码，或在 NFC 终端上使用 Bolt 卡。



![QR code de paiement](assets/fr/18.webp)



一旦收到付款，就会出现一个确认屏幕，以当地货币和萨托希显示收到的金额。您可以通过电子邮件发送收据、打印票据或立即开始新的销售。



![Paiement encaissé](assets/fr/19.webp)



**监测和管理**



所有交易都记录在商家控制面板中。您可以按时间段全面跟踪收入、销售总数和详细的历史记录，以便进行会计核算。



设置界面提供多个配置选项卡。在 "常规设置 "选项卡中，您可以管理商家资料和通知。在 "用户 "选项卡中，您可以添加和管理您团队对商家控制面板的访问权限（根据您的计划进行多用户管理）。在 "开发工作区 "选项卡上可以访问用于高级集成的 API 密钥，而在 "订阅 "选项卡上可以管理您的订阅。



![Paramètres du compte marchand](assets/fr/20.webp)



**免费计划与商业计划



Tiankii为商家控制面板提供两种套餐。**免费**计划（免费）适用于初创企业，有以下限制：单个销售点、单个用户、月交易量限制为1000美元，且无法访问电子商务连接器。商业***计划（每笔交易收取 0.5% 费用）提供无限终端、无限用户、无限交易量、WooCommerce/Shopify/Cloudbeds 插件访问权限以及专属 WhatsApp 通知。



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## 效益和制约因素



### 亮点



**自我监管**：您保留自己的私人密钥和对资金的完全控制权。没有账户冻结或第三方平台破产的风险。



**简单**：Lightning Address 作为电子邮件地址，只需轻轻一点即可进行 NFC 支付，界面直观，无需专业技术知识。



**完整的生态系统**：适用于所有情况（个人、零售商、开发商）的工具，可通过模块化集成满足您的需求。



**专业合规**：安全云托管、PCI-DSS 合规性、萨尔瓦多法规合规性。



### 局限性



**闪电限制**：需要永久的 wallet 连接、大容量的流动性管理、收件人离线时的故障风险。Tiankii 通过集成的 LSP 减少了这些方面的问题。



**SaaS 依赖性**：如果 Tiankii 不可用，则暂时无法生成发票（您的资金仍然安全）。



**隐私**：Tiankii可以观察交易元数据（金额、日期）。私密性低于 BTCPay 服务器等自托管解决方案。



## 结论



Tiankii说明了精心设计的基础设施如何消除阻碍Bitcoin作为日常货币被大规模采用的技术障碍。通过将 Lightning Network 的威力与非监管方法和可访问工具相结合，该生态系统在金融主权和易用性之间提供了一条平衡之路。



对于商家来说，Tiankii 是一个大幅降低交易成本的机会，同时还能获得新的客户群。对于消费者来说，闪电 Address 和 NFC 卡将 Bitcoin 转化为一种实用货币，而不需要复杂的技术。



尽管广泛采用 Bitcoin 仍是一项需要教育和时间的挑战，但像 Tiankii 这样的基础设施表明，技术工具已经存在。简化 Bitcoin 支付的使命不再是遥不可及的愿景，而是任何愿意投身其中的人都可以实现的现实。



## 资源



### 正式文件




- [Tiankii 官方网站](https://tiankii.com)
- [Tiankii 帮助中心](https://help.tiankii.com)
- [履行机构申请](https://go.ibi.me)
- [商家仪表板](https://pay.tiankii.com)
- [指挥中心](https://cc.ibi.me)



### Wallet 连接导轨




- [连接 LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connect Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### 社区




- [Lightning Network Plus](https://lightningnetwork.plus) - 闪电教育资源
- [Bitcoin Beach](https://www.bitcoinbeach.com) - 萨尔瓦多循环经济倡议 Bitcoin



### 相关工具




- [Blink Wallet](https://blink.sv)--建议与 Wallet Lightning 兼容
- [LNbits](https://lnbits.com) - 自主托管的 wallet 解决方案
- [标准 Bolt 卡](https://github.com/boltcard) - NFC 卡的技术规格
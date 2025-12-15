---
name: Debifi
description: 获得由 Bitcoin 担保的非监护贷款。
---

![cover](assets/cover.webp)




## 导言



几个世纪以来，传统贷款为许多项目提供了资金。然而，这种方式仍然速度缓慢、成本高昂，而且包容性不强，尤其是对于那些无法利用稳固的银行基础设施的人来说更是如此。



Bitcoin 协议的兴起开创了一个新的金融时代，同时也带来了一系列挑战。其中一个挑战是如何在不被迫出售 Bitcoin 的情况下获得流动资金，从而失去其增长潜力。



这就是**Debifi**，一个将自己定位为现代银行替代品的平台。其目标很明确：通过将传统金融体系的优势与 Bitcoin 提供的自由相结合，使信贷尽可能简单、透明。Debifi 这个名字就反映了这一愿景： *德比菲"（Debifi）这一名称反映了这一愿景："**分散的 Bitcoin 金融***"（Decentralized Bitcoin Finance***），这一缩写说明了分散金融与 Bitcoin 创新的结合。



Debifi 是一个由 Bitcoin 支持的非托管借贷平台，这意味着你可以保留对自己私钥的控制权。它允许用户以其锁定的比特币作为抵押物来释放流动性。与传统银行贷款不同，Debifi 采用多重签名托管系统（四分之三），不接受抵押品再抵押，从而保证了更高的安全性和透明度。



在实践中，这意味着 Debifi 或单个贷款人都不能在未经三方（您、贷款人和可信赖的第三方）同意的情况下使用您的 BTC。这使得系统更加安全：如果您在 Debifi 上借款，您将保留您的 Bitcoin 的所有权，直到贷款全部偿还为止。



## 德比菲的优势



通过 Debifi，您可以获得由 Bitcoin 支持的贷款，这些贷款具有超额抵押和 on-chain 担保。多签名钱包、2FA 和对 Bitcoin 的完全控制确保您的资金安全--您持有您的钥匙，您持有您的硬币。以具有竞争力的利率和全球流动性借入一系列稳定币或法定货币。



下面是 Debifi 贷款与传统银行贷款的简单比较：


| Characteristics        | Loan via Debifi                                                        | Traditional Bank Loan                                                       |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Accessibility          | ✔️ Open to any Bitcoin holder (even without banking history)           | ❌ Often limited to clients with physical collateral and strong records      |
| Speed of approval      | ✔️ Funds available within minutes or hours                             | ❌ Lengthy process (days or weeks)                                           |
| Required guarantees    | ✔️ Bitcoin used as the sole collateral                                 | ❌ Physical guarantees (property, land, stable income)                       |
| Asset control          | ✔️ You keep exposure to Bitcoin and its upside potential               | ❌ No connection between the loan and your financial assets                  |
| Geographic flexibility | ✔️ Available everywhere (no banking jurisdiction constraints)          | ❌ Restricted to the bank’s jurisdiction                                     |
| Main risk              | ❌ Liquidation risk if BTC price drops too sharply                      | ❌ Risk of asset seizure or negative impact on credit score                  |

在逐步向您介绍如何在 Debifi 上借款之前，我认为您需要了解几点。




## 定义





- 发放费** 是在发放贷款时收取的一次性费用，按借款金额的一定百分比计算。这些费用用于支付行政、业务和管理成本。





- 抵押**是您存入以担保贷款的资产。在 Debifi 的案例中，抵押物是 Bitcoin（BTC），借款人将其存入 Multisig 3/4 托管账户。





- Multisig 托管 (3/4)** 系统是一种安全存款机制，借款人的比特币存放在一个多重签名地址中。具体来说，四（4）方（借款人、出借人、Debifi、独立第三方）各持有一个密钥。要转移资金，至少需要 4 个签名中的 3 个签名。





- 稳定币**是一种价值与稳定资产（如美元）挂钩的加密货币，它避免了 Bitcoin 的波动性。例如，1 USDC 的价值总是~1 美元，因为它有法定储备作为支持。





- 贷款的贷款价值比 (LTV)** 决定了您可以为 Bitcoin 借到多少现金作为抵押。LTV 比率 = 贷款额/抵押物金额 * 100。例如，LTV 为 50%，表示贷款价值等于 Bitcoin 存款价值的 50%。




BTC 会话视频教程 ：



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## 开始使用德比菲



要开始使用 Debifi，您需要一些先决条件。


### 先决条件



在向 Debifi 借阅图书之前，请确保您携带了以下物品：





- Bitcoin wallet：您持有 BTC 的地方（最好是非托管的，例如 Hardware Wallet 或可信的移动 wallet）。您将从这个 wallet 向 Debifi 发送 Bitcoin 抵押品，并接收回抵押品。



您可以使用 Aqua、Bitcoin 和 Liquid wallet，它们也支持各种网络上的 USDT 稳定币管理。或者 COLDCARD（Mk4 或 Q），这是 Debifi 目前唯一支持的硬件。



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC（*了解您的客户*）：根据所选择的贷款方案，可能需要进行身份验证。在 Debifi 上，每份报价都会注明是否需要 KYC。因此，请做好相应准备。KYC 由可靠的第三方服务提供商（如 Sumsub）执行。



![image](assets/fr/03.webp)





- 双因素身份验证应用程序：Debifi 的每项重要操作都需要验证码。这是一个额外的安全层。在本教程中，我们将使用 Google Authenticator。或者，您也可以使用其他合适的验证码。



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Debifi 网站和移动应用程序：Debifi 既是一个网站，也是一个移动应用程序，两者协同工作。移动应用程序成为 wallet，存储您的私人密钥，并管理合同的签署。此外，您还需要使用网站提交合同（一个大的 Interface 可让您大致了解贷款合同及其具体内容）。





- 您需要使用 Debifi 移动应用程序（iOS/Android）来申请贷款。您必须下载该应用程序，创建账户并 "链接 "您的设备（将设备注册到您的账户）。Debifi 应用程序支持双因素验证 (2FA)，如果没有智能手机，您将无法在 Debifi 上确认交易。



### 创建账户



请访问 [Debifi 的官方网站](https://debifi.com/app)。



![image](assets/fr/04.webp)



根据您的智能手机类型安装应用程序，然后打开它。



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



进入应用程序后，点击**设置**菜单。



![image](assets/fr/07.webp)



然后点击**登录或创建账户**，用您的电子邮件地址创建一个账户。



![image](assets/fr/08.webp)



![image](assets/fr/09.webp)



![image](assets/fr/10.webp)



您将通过电子邮件收到一个验证码。将验证码复制并粘贴到应用程序中。然后打开智能手机上的 Debifi 应用程序并登录。



![image](assets/fr/11.webp)



### 确保账户安全



为了安全起见，Debifi 将要求您遵循三个步骤。



![image](assets/fr/12.webp)





- 首先，您需要设置一个强大的 PIN 码，以便稍后访问您的应用程序。



![image](assets/fr/13.webp)





- 然后，设置双因素身份验证 (2FA)，使用 2FA 代码将设备与账户关联。



![image](assets/fr/14.webp)





- 最后，将私人密钥的 12 个单词写在可靠的介质上并保存在安全的地方。这一阶段对于恢复账户和管理资金至关重要。



![image](assets/fr/15.webp)





- 为了增加安全性，您甚至可以添加一个 passphrase。



![image](assets/fr/16.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

请注意，只有您注册的智能手机才能打开您的账户（额外的安全措施）。



完成这些步骤后，点击 "**优惠 "菜单，查看可用的贷款优惠。当您点击某项优惠时，系统会将您重定向到 Debifi 网站。



![image](assets/fr/17.webp)



### 访问网站并了解贷款优惠



设备连接后，请访问 [Debifi 网站](https://debifi.com/)。登录以建立 Debifi 移动应用程序与网络平台之间的安全连接。这样，您就可以更方便地与现有贷款优惠进行互动（清晰查看每项优惠的详细信息），并管理您的账户。



![image](assets/fr/18.webp)



![image](assets/fr/19.webp)



![image](assets/fr/20.webp)



![image](assets/fr/21.webp)




关于如何在平台上登录账户的视频教程：



![video](https://youtu.be/cUwCfTKDAOo)



## 贷款申请



该平台为您提供机构质量的流动性，并根据您的需求提供一系列选项。请浏览了解有哪些可供选择。您还可以根据个人风险承受能力和财务状况灵活调整贷款参数。



![image](assets/fr/22.webp)



您可以在平台上查看 Debifi 目前提供的法定货币。



![image](assets/fr/23.webp)



### 明确、灵活的合同条款



Debifi 依靠透明、灵活的贷款条件来满足各方（贷款人和借款人）的需求。主要条款包括



#### 贷款价值比 (LTV)


Bitcoin 贷款批次一般为三批：





- 保守型（30% - 40% LTV）相当于低风险贷款，是最大限度地防止 Bitcoin 价格波动的理想选择；





- 平衡（50%LTV） ；





- 进取型（按揭成数 70%），流动性更强，但在市场低迷时清算风险极高。在选择这一档时，必须积极监控 Bitcoin 的市场状况。



#### 利率



利率的确定一般取决于您所选择的贷款成数、贷款期限、抵押品波动性和平台特定风险评估。利率在贷款期间保持固定。



#### 贷款期限和还款灵活性



还款计划灵活，可满足借款人的需求。只要抵押品符合要求，贷款可随时全部或部分偿还，无需额外费用。在整个贷款期间，利息通常定期支付，本金则在到期时结清。



#### 清算权（追加保证金）



鉴于 Bitcoin 的不稳定性，贷款包括一项明确规定的追加保证金政策。当抵押品价值下降导致抵押率上升时，就会出现追加保证金的情况。Debifi 会通过电子邮件和应用程序通知借款人，允许他们增加抵押品或偿还部分贷款。


75% LTV - 首次预警

80% LTV - 第二警报

85% LTV - 最后警报

90% LTV - 抵押物被清算



### 启动贷款程序



要选择适合您需要的贷款产品，请单击产品查看其特点。



![image](assets/fr/24.webp)



您可以看到 ：


1.贷款机构名称 ；


2.贷款额度范围；


3.您将收到 USDC 以太坊形式的资金；


4.贷款期限、利率和按揭成数；


5.此优惠需要 KYC；


6.必须输入所需的确切金额（该金额必须在范围之内，见 2）；


7.必须输入用于接收资金的以太坊 USDC 地址。



一旦您对报价满意并填写了必要信息，请点击 "Contract 申请"。



![image](assets/fr/25.webp)



返回移动应用程序 "**提供公钥**"。



![image](assets/fr/26.webp)



按 "**提供公钥**"，然后选择公钥来源。贷款人也需要提供公钥。



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



下一步是签署合同。仍在移动应用程序中，按'' **签署 Contract** ''。



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



当您完成合约签署后，Debifi 会自动为您的合约创建一个唯一的多重签名 Bitcoin 地址（托管 3-sur-4）。只要您的比特币还在托管中，就不能在其他地方使用。



### 存入担保金并收到您的资金



最后一步是将您的 Bitcoin 抵押品存入多重签名托管系统。Debifi 会向您显示托管地址（B）和要发送的 BTC 数量（A）（抵押品 + 佣金）。



![image](assets/fr/33.webp)



您的移动应用程序也会收到此通知。



![image](assets/fr/34.webp)



一旦您的存款得到确认，贷款机构就会立即将贷款金额支付到您指定的收款地址，从而完成交易，让您获得所需的资金。



然后，您将收到 Debifi 的通知，要求您支付贷款费用或佣金，以便推进您的贷款状态。



实际上，合同一旦签订，贷款费用就会自动从借款人在多重签名托管地址中托管的抵押物中扣除。



您只需签署一项交易，Debifi 即可从担保金中扣除佣金。您的贷款人也需要签署费用扣除交易，否则 Debifi 将无法收取佣金。



![image](assets/fr/35.webp)



适用的贷款费用为 1.5%-2%，具体取决于合同期限。平台仅以 Bitcoin 为单位收取佣金。



## 贷款跟踪



贷款激活后，Debifi 允许您实时跟踪您的合同。在界面中，您可以找到



- 借款金额和剩余期限。
- 当前的贷款价值比（LTV），当 BTC 价格下降、抵押物价值下降时，贷款价值比就会上升。




抵押物价值下降时，借款人会收到通知，该信息也会显示在合同摘要页面上。要恢复原来的贷款价值比，借款人必须满足以下任一条件



- 存入额外的抵押品；
- 偿还全部或部分债务。




如果抵押品价格上涨，借款人保留抵押品的任何资本收益。他只欠贷款额，而贷款额是预先确定的，与 Bitcoin 的价格无关。




## 偿还和收回抵押品



在约定期限结束时（或根据您的意愿提前），您必须偿还贷款。


在德比菲：





- 转到您的合同，点击**还款**。输入应付款总额（本金+利息）。





- 将稳定币从您的 wallet 发送到指定的放款人地址，然后返回平台确认还款，将还款交易的**ID**复制到专用标签。这样可以方便 Debifi 进行检查。



一旦贷款人（和您）确认付款，Debifi 将要求您**退款。您的 Bitcoin 抵押品将被释放，您可以将其从托管中归还给您自己的 wallet。  不要忘记收回您所有的比特币。



一旦收到比特币，贷款合同就会变为 **Contract 已完成**。



恭喜您您已经完成了流程。




## 最佳做法和安全



无论您的目标或动机是什么--为项目融资、购置房产、购买比特币等--在使用 Bitcoin 支持的贷款之前，请务必谨慎。请花时间仔细评估您的决定，因为 Bitcoin 仍然是一种不稳定的资产。 **价格暴跌可能导致你的比特币被迫清算。



监控您的贷款抵押率 (LTV)。如果可能，设置警报（BTC 价格、LTV）。不要让您的比率接近 90%。如有疑问，请增加抵押物或提前还款。



控制您的钥匙。将您的 BTC 保存在安全的 wallet 中（最好是硬件或信誉良好的 wallet）。不要设置与您生活中重要日期相关的 PIN 码，也不要共享您的恢复短语。在 Debifi 上，您的 generate 私钥在应用程序中 - Debifi 并不知道。



尽可能从小额贷款开始。对于您的第一笔贷款，请先测试适度的金额，以便熟悉贷款流程。



仅使用 Debifi 官方网站了解 Debifi 的最新消息，避免使用不明链接或钓鱼链接。  更新应用程序，使用 PIN 码保护您的智能手机，并选择兼容的 Hardware Wallet。



另外，如果您是贷款人，本教程视频将指导您使用 Debifi 平台。从选择对您的提议感兴趣的借款人，到提供公钥、签署协议、转移稳定币等。



![video](https://youtu.be/g8iLxwI4xT0)



您现在知道如何使用 Debifi 平台获得贷款了吧。



我建议您学习这门课程，深入了解 Bitcoin、稳定币及其对主权的贡献。



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46
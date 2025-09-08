---
name: BIP-85
description: 如何使用 BIP-85 从主 seed 中 generate 多个种子词？
---
![cover](assets/cover.webp)



## 1.了解 BIP-85



### 1.1 什么是 BIP-85？



BIP-85 是一项高级功能，可让您从一个**seed 主短语**创建多个**seed 副短语**。



每个 seed 二级句子可用于创建一个完全独立的 Bitcoin 投资组合。这些投资组合可用于多种用途：手机上的 Hot Wallet、亲戚的投资组合、独立的储蓄组合等。



所有 seed 子短语都是**语法派生的**，但**不可能从子短语追溯到 seed 主短语**。这确保了每个组合之间的完全分离。



只要您能访问您的 seed 主短语（以及相关的 passphrase，如果您使用的是 passphrase），您就可以****地重新生成任何 seed 辅助短语，而无需单独保存。



### 1.2 为什么使用 BIP-85？



如果您想 ：





- 创建多个独立的 Bitcoin 组合，无需多重备份
- 根据不同用途（储蓄、支出、家庭、项目）管理资金
- 为亲属提供保障（"吉姆叔叔 "功能）
- 删除投资组合而不会丢失资金访问权限
- 简化安全性：只需保护一个 seed 关键短语



### 1.3 与 BIP-32 相比的优势



有了 BIP-32，单个 seed 句子就可以使用派生路径（例如：`m/44'/0'/0'/0/0`）来实现 generate 和 Bitcoin 账户和地址的完整层次结构。每个路径可以代表一个单独的账户，但**都与同一个 seed 句子相关联**。因此，如果这个 seed 句子被破坏，**所有派生账户都可以访问**。



通过 BIP-85，一个 seed 主句可用于 generate 多个完全独立的 seed 次句： **如果这些次要种子中的一个被破坏，攻击者将永远无法回到主 seed 或访问其他组合**。


这样就可以将风险分门别类：





- 您可以将辅助 seed 用于 Hot Wallet 或临时使用，接受更高的曝光。
- 即使这个 Hot Wallet 遭到破坏，您的其他资金受到其他二级种子的保护或保持离线状态，**仍然安全**。



另一方面，对于 BIP-32 和 BIP-85，如果主 seed 遭到破坏，**所有资金都会受到**。因此，以最高级别的安全措施保护主 seed 至关重要。



![image](assets/fr/02.webp)


## 2.BIP-85 的实用案例



BIP-85 允许您从单个 seed 核心词组创建多个 Bitcoin 投资组合，每个组合都有自己的 seed 辅助词组。以下是组织和保护 Bitcoin 资金的五个实用案例。每个案例都解释了为什么使用 BIP-85 比通过 BIP-32 用单个 seed 短语管理多个账户更实用。



### 2.1 限制安全性较低的投资组合的风险





- 情景**：您使用 "Hot Wallet "Wallet（安装在联网设备上）进行日常交易。
- 解决方案 BIP-85**：创建一个 seed 二级短语，专门用于该投资组合。
- 与 BIP-32 相比的优势**：您无需将 seed 主要短语导入手机，从而降低了黑客攻击的风险。只有 seed 次要短语会被泄露，从而保护您的其他钱包。使用 BIP-32，您需要使用 seed 主短语和旁路路径，从而暴露您的所有资金。



### 2.2 为家庭成员创建作品集





- 情景**：您为亲近的人（例如您的母亲）设置了一个 Bitcoin Wallet，如果他们丢失了，您还可以恢复它。
- 解决方案 BIP-85**：您创建了一个专门的 seed 二级句子，并只共享这一个。
- 与 BIP-32 相比的优势**：使用 BIP-32，为亲人创建一个账户需要共享您的主 seed 短语，这将使您的所有资金面临风险，并使您亲人的管理复杂化（管理分支路径），或者在您的主 seed 短语之外创建一个新的 seed 短语进行保存。



### 2.3 促进单独投资组合的管理





- 情景**：您将比特币分开用于不同用途（如长期储蓄、非 KYC 资金）。
- 解决方案 BIP-85**：为每个目标创建 seed 二级短语。
- 相对于 BIP-32 的优势**：在 BIP-32 中，所有账户共享相同的 seed 短语，这使得第三方投资组合的管理变得复杂，因为需要管理诸如 `m/44'/0'/0'` 等派生路径。此外，也无法为每个设备分配单独的账户（例如，"Coldcard 上的储蓄"、"移动设备上的日常"、"Trezor 上的假期"）。BIP-85 为每个目标分配了一个独特的 seed 二级短语，便于识别并在每个设备上单独导入。



### 2.4 使用临时 Wallet 进行交易





- 情景**：您需要一个临时投资组合，用于一次性交易或保密（例如：混合资金、与 Exchange KYC 互动等）。
- 解决方案 BIP-85**：您可以创建一个 seed 二级句子，将其用于交易，然后在必要时将其销毁，因为您知道它可以重新生成。
- 相对于 BIP-32 的优势**：使用 BIP-32，临时账户依赖于 seed 主句，一旦受到威胁，您的所有资金都会暴露。





## 3.开始之前





- 硬件**（可选）
 - 冷卡 Mk4 或 Q1
 - MicroSD 卡





- 基础知识
 - 理解 Mnemonic 短语 (BIP-39)：包含 12 至 24 个单词的列表，用于保存作品集。
 - 了解什么是 Bitcoin Wallet：管理比特币的软件或设备，以及如何用 Mnemonic 短语还原它。
 - 更多资源见附件。





- 兼容** 软件
 - Sparrow wallet（计算机，用于仅观察或高级管理）
 - 双节棍（手机，用于多重签名）
 - 蓝色钱包（手机）
 - ...





- 3.4 冷卡**配置
 - 在冷卡上初始化一个包含 24 个单词的 seed 句子。
 - 可选：添加一个 passphrase，以确保 BIP-85 分支的访问安全。
 - 激活有用的选项：NFC（用于导出）、禁用电池 USB（安全）。




## 4.分步教程



请按照以下步骤在 Coldcard 上使用 BIP-85 创建、使用和检索辅助 Mnemonic。



### 4.1 generate a seed 二级判决



您将根据 seed 主短语创建一个 seed 副短语。


打开冷卡，输入密码。





- 1.如果您已将 passphrase 应用于主 seed：**
 - 从主屏幕进入 "passphrase"。
    - 选择 "添加 Word "并输入密码。
    - 按 "应用"。
    - 检查 Wallet 的身份：转到 "Advanced（高级）">"View Identity（查看身份）"，记录 Wallet 的指纹。





- 2.转到 BIP-85** 菜单
 - 从主屏幕，转到 "高级 > 导出 seed B85
 - 阅读警告并确认。



ColdCard 通知您，所生成的种子在数学上源自您的主 seed，但在密码学上是完全独立的。


![image](assets/fr/03.webp)





- 3.选择格式


选择 seed 短语格式：12、18 或 24 个单词。检查您要导入 seed 短语的 Wallet 可接受的字数。


![image](assets/fr/04.webp)





- 4.选择索引
 - 输入 0 到 9999 之间的索引。
 - 该索引对于日后再生二级 seed 至关重要。请小心保存，并贴上标签，如"索引 1 = 移动 Wallet"、"索引 2 = 家庭项目"、"索引 4 = 测试混合物"......
 - 如果丢失，您不会失去资金的使用权，但您必须测试从 0 到 9999 的组合才能找到资金。


![image](assets/fr/05.webp)





- 5.注释或导出 seed 二级句子**


ColdCard 现在可以显示新的 seed 二级句子。您可以 ：




 - 手动**注释**。
 - 新闻 ：
     - 1` 保存在 SD 卡上
     - 2 "在冷卡上**进入 "使用此 seed"** 模式（对导出或签署交易有用）
     - 3` 显示**QR 码**（使用 BlueWallet 或 Nunchuck 等移动应用程序扫描）。
     - 4` 通过**NFC**发送



💡至此，您就拥有了一个独立的 seed 短语，可用于任何 Wallet BIP39（Trezor、Ledger、BlueWallet、Nunchuck......）。


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 使用辅助 seed



现在，您可以使用衍生的 seed 在 .NET Framework 中创建一个新的投资组合：




- 移动应用
- 另一个 Hardware Wallet
- a Multisig 组合



### 4.3 恢复丢失的 seed 二级短语



如需随时检索辅助 seed，请重复此过程：


1.重新启动冷卡


2.输入密码


3.输入您的 passphrase（如果已定义


4.转到 "高级 > 导出 seed B85


5.选择格式（12/18/24 个字）


6.输入相同的索引（例如 `1`）。


7.您将获得完全相同的二级 seed




## 5.限制、风险和最佳做法



### 5.1 依靠 seed 主句 + passphrase



BIP85 的使用完全依赖于 24 个字的 seed 主句，如果您使用了 passphrase，也完全依赖于 seed。




- 从这两个 Elements 中，可以再生出所有 seed 二级短语。
- 如果没有这 2 个 Elements 中的一个，您就无法使用所有衍生产品组合。



### 5.2 多重签名配置的风险



我们强烈建议不要在 multi-sig 配置中使用由同一主 seed 短语生成的次 seed 短语：如果设备或主 seed 短语被入侵，所有 multi-sig 密钥都可能被攻击者重新生成。



### 5.3 软件兼容性



并非所有应用都直接支持 BIP85 派生。不过，通过 BIP85 生成的种子是标准的 BIP39 种子（12、18 或 24 个字），因此可用于任何兼容 BIP39 的组合。



### 5.4 BIP85 账户登记册



建议随时更新 seed 二级短语的个人登记簿。




- 通过它，您可以快速找到哪个 BIP85 指数对应哪个投资组合，而无需保留 seed 二级短语。
- 该注册表应保持简约，不明确提及 Bitcoin，并应与主 seed 分开存储。记得在继承计划中提及它。



寄存器可包含 ：




- 使用的 bIP85 索引（0 至 9999 之间的数字）
- 用途或参考名称（如：Hot Wallet、个人储蓄、妈妈的 Wallet）
- 必要时，在冷卡中验证 Wallet 指纹



### 5.5 备份



备份必须包括 ：




- 主 seed
- gW-76（如使用）



切勿存放在一起：




- 主 seed 和 passphrase
- 主 seed 和 BIP85 账户寄存器



更多资源见附件。




## 附录



## A.1 术语表





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed短语](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 保存恢复短语



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 了解 passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Bitcoin 组合如何运作



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
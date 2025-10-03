---
name: Electrum OP_RETURN
description: 用电子邮筒在 Blockchain Bitcoin 上注册留言
---

![cover](assets/cover.webp)




本教程逐步向您介绍如何使用 Wallet 电子琴在 Blockchain Bitcoin 上编写信息。此操作使用 OP_RETURN 指令将文本插入交易，在 Blockchain 上公开可见。请按照以下简单步骤成功注册。



---
## 先决条件





- 一台电脑（Windows、macOS 或 Linux）。
- 互联网连接。
- 在您的 Wallet 中放入一些萨托希（Sats）或比特币（BTC），以支付交易金额和费用。
- 文本到十六进制转换器（如在线网站）或专用工具，如[本 OP_RETURN 脚本生成器](https://resources.davidcoen.it/opreturnelectrum/)。



---

## 步骤 1：下载并安装 Electrum



![image](assets/fr/01.webp)



1.访问 Electrum 官方网站：[electrum.org](https://electrum.org/).


2.下载与您的操作系统（Windows、macOS、Linux）相对应的版本。


3.按照安装说明安装 Electrum。


4.通过比较文件签名或 Hash 检查下载文件的完整性（可选，但出于安全原因建议使用）。



→ 更多详情，请参阅 "Electrum 教程"：



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 第 2 步：创建或导入 Wallet



1.启动 Electrum。


2.如果已有 seed 短语（恢复短语），请选择创建新的 Wallet 或恢复现有的 Wallet。


3.请按照说明配置您的 Wallet：




 - 对于新的 Wallet，请记下您的 seed 句子，并将其保存在安全的地方（纸张、保险箱等）。
 - 对于现有的 Wallet，请输入您的 seed 短语以恢复它。


4.设置密码以确保 Wallet 的安全。



→ 更多详情，请参阅 "Electrum 教程"：



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 步骤 3：检查可用资金



确保您的 Wallet 包含足够的比特币 (BTC) 或卫星币 (Sats) ：




- 交易金额（例如 0.00001 BTC 或 1000 Sats）。
- 交易费，根据网络规模的不同而不同（一般为几千 Sats）。



查看 Electrum 中的余额，查看您的资金。



![image](assets/fr/02.webp)



如有必要，请将 BTC 或 Sats 转入 Wallet。为此，请转到 "接收 "选项卡并点击 "创建请求"：



![image](assets/fr/03.webp)



这将显示接收 Address：



![image](assets/fr/04.webp)



→ 更多详情，请参阅 "Electrum 教程"：



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 步骤 4：准备要刻写的信息



选择要输入的信息（例如 "Thanks Satoshi"）。注意：OP_RETURN 信息限制为 80 字节，即大约 80 个 ASCII 字符。



*花点时间想一想：您在 Blockchain Bitcoin 上写下的内容是永恒的，所有人都可以访问，所以：*




- 留下我们人性的美丽表达，
- 避免输入可能会让您后悔的内容



*Blockchain 空间和您的比特币都很珍贵，请有意识地合理使用*。



将信息转换为十六进制 ：




- 您可以使用[在线工具](https://www.rapidtables.com/convert/number/ascii-to-hex.html)，但要注意不要在那里处理敏感数据（不过，原则上，打算通过 OP_RETURN 在 Blockchain Bitcoin 上发布的信息不存在任何保密问题）；
- 为提高保密性，请使用一个小型 Python .NET Framework 在本地执行转换：



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



例如："Thanks Satoshi "的 ASCII 编码为 "5468616e6b73205361746f736869"，十六进制编码为 "5468616e6b73205361746f736869"。



准备交易脚本。下面是预期格式的示例：



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



它由 ：





- 目的地 Address：有效的 Bitcoin Address。Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`。如果您希望将转入的资金返还给自己，则该 Address 可以是您自己的 Address；
- 转账金额：交易金额，这里是 `0.00001` BTC。**请注意**：由于 Electrum 使用的单位是 BTC，交易脚本中显示的金额也必须用 BTC 表示，而不是 Sats；
- 脚本 **OP_RETURN**：转换为十六进制的信息，前面加上 script(`OP_RETURN <messsage>), 0`。这里的 `5468616e6b73205361746f736869` 表示十六进制信息。



⚠️ **注意**：在 OP_RETURN 后标注 "0 "非常重要，因为该操作码会将脚本标记为无效，使输出永久无法使用。网络节点将从其 UTXO 设置中删除该输出。如果您输入的值不是 "0"，它将不可挽回地丢失：您的比特币将被视为烧毁。因此，您应该始终在 OP_RETURN 中输入 `0`，以记录所需的数据，但不关联资金，因为资金会丢失。



提示：使用 [OP_RETURN 生成器] 工具 (https://resources.davidcoen.it/opreturnelectrum/) 自动生成 generate 脚本。即使该工具建议以 BTC 输入金额，也请将单位配置为 Electrum。



![image](assets/fr/05.webp)



要更改 Electrum 使用的单位，请在菜单栏中找到 "首选项"，然后在 "单位 "选项卡中选择 BTC / mBTC / bits 或 Sats：



![image](assets/fr/06.webp)




---

## 步骤 5：发送交易



在 Electrum 中，转到 "发送 "选项卡。



![image](assets/fr/07.webp)



在 "付款至 "字段中，粘贴准备好的脚本（例如上面的脚本）。



![image](assets/fr/08.webp)



付款至 "字段应显示为 Green，交易金额应显示在下面一行。



检查金额字段中的金额及其单位。



点击 "支付..."，根据您愿意支付的金额和您希望 Miner 处理您的交易并将其整合到区块中的速度调整您的交易费用。



![image](assets/fr/09.webp)



单击 "确定 "并用密码确认交易。此时会出现一个确认窗口。




---

## 步骤 6：验证注册



交易确认后（可能需要几分钟），进入 "历史记录 "选项卡。



![image](assets/fr/10.webp)



右键单击交易，选择 "在资源管理器上查看"，查看详细信息。



或者，复制目标 Address（例如，`bc1q879cv4p5q6s9537orange3zss33d3turzad8`）并在 Blockchain 浏览器上查看，如 [Mempool.space](https://Mempool.space/) 或 [blockstream.info](https://blockstream.info/) 。



在交易详情中查找 OP_RETURN 字段，查看您的信息。



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## 提示和最佳做法





- 少量测试：从小额交易开始（如 Sats 1000），以避免代价高昂的错误。
- 确保包含 OP_RETURN 的输出等于零，否则比特币将永久丢失。
- 检查单位：确保输入的金额与 Electrum 中显示的单位一致（BTC、mBTC 或 Sats）。
- 交易费：如果网络拥堵，可提高手续费以加快确认速度。
- 短信息：OP_RETURN 条目限制为 80 字节。请相应规划您的信息。



---

## 有用资源





- 下载 Electrum：[electrum.org](https://electrum.org/)
- OP_RETURN 脚本生成器：[resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain 探索者：[Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)
---
name: Lightning Smoke Machine
description: 通过 ESP32 以闪电支付方式触发烟雾机。
---

![cover-lightning-smoke-machine](assets/cover.webp)



## 导言



通过 Lightning Network 将经典烟雾机转化为可在 Bitcoin 中支付的设备。每次付款都会自动触发烟雾喷射！





- 级别： 中级中级
- 预计时间：2-3 小时
- 使用案例Bitcoin 活动、艺术表演、闪电演示、自动舞台效果



## 先决条件



### 知识





 - 基本电子设备（接线、继电器）
 - 焊接（或使用杜邦连接器）
 - 网络配置（WiFi、WebSocket）



### 所需账户





- BTCPay 服务器：功能实例（自托管或托管）
- Blink Wallet : 账户 + 访问 API



### 访问





- BTCPay 服务器的管理员访问权限
- 用于 ESP32 的 WiFi 连接



## 所需材料



### 硬件 - 电子元件





- 1 个微控制器 - ESP32-WROOM-32


*ESP32-WROOM-32 是一款结构紧凑、成本低廉的 WiFi/Bluetooth 微控制器，用于将电子设备连接到互联网并对其进行远程控制*。



![ESP32](assets/fr/1.webp)





- 1 个继电器模块 - 5V 带光耦合器


*继电器就像一个开关，ESP32 可以操作它来打开或关闭烟雾机*。



![relay](assets/fr/2.webp)





- ~10 条杜邦电缆 - 公头/公头和公头/母头



![dupont-cables](assets/fr/3.webp)





- 1 个 ESP32 电源 - 5V USB 或锂电池



![battery](assets/fr/4.webp)





- 1 根微型 USB 电缆 - 连接 ESP32 和电源



![micro-usb-cables](assets/fr/5.webp)





- 1 台 220 伏烟雾机，带 12 伏电池遥控器



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 瓶与烟雾机兼容的液体



### 硬件 - 工具





- 烙铁 + 锡（如果焊接）
- 螺丝刀
- 万用表（推荐）



### 软件





- 固件 BitcoinSwitch ： **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- 兼容 WebSerial 的网络浏览器（Chrome/Edge/Brave）
- 已配置 BTCPay 服务器。有关创建 BTCPay 服务器实例的更多信息，请访问本教程：https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## 系统架构



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **安全警告 - 阅读后再继续** **⚠️**



本项目涉及连接到**220V 主电源**的烟雾机。操作不当可能导致**致命的触电**或**火灾**。



**不可讨价还价的规则：**



1. **在打开遥控器或篡改线路之前，请务必断开烟雾机的电源**。


2. **操作前从遥控器中取出电池**（有短路和损坏部件的风险）


3. **在重新连接之前，检查所有连接是否都已隔离**


4. **在遥控盒关闭并固定之前，切勿重新连接 220V** 电源



如果您不太擅长这种操作，请带一个擅长的人一起去。



---

## 第 1 部分：硬件组装



### 步骤 1：准备遥控器



目标将继电器连接到遥控器上的开/关按钮上


1.打开遥控器




    - 识别开/关按钮
    - 拧开外壳，打开遥控器


2.定位连接




 - 找到电容器的 + 和 - 端子。
 - 用万用表测试连续性（可选）



![smoke-machine-remote](assets/fr/8.webp)



3.按钮接线（焊接或连接器）




    - 将黑色电缆焊接到按钮的 - 端子上
    - 将红色电缆焊接到公共 + 端子上



![smoke-machine-remote](assets/fr/9.webp)



### 步骤 2：连接继电器模块



**提醒继电器术语



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**从遥控器到继电器模块的接线：**




- 来自 ON/OFF 按钮的黑线 **→** NO（常开）
- 红线（共用） **→** COM（共用）



**逻辑：**


当 ESP32 激活继电器时，它会连接 COM 和 NO，这与按下遥控按钮完全相同。


当 ESP32 切断继电器时，COM 和 NO 分离，相当于松开按钮。



![remote-relay](assets/fr/10.webp)



### 步骤 3：将 ESP32 连接到继电器模块



**接线图：**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**验证：**




- VCC 和 GND 连接良好（极性）
- 用于控制信号的 GPIO 21
- 无明显短路



![relay-esp32](assets/fr/11.webp)



**检查点硬件**


在切换到软件之前，请检查 ：




- 正确接线的遥控器
- 与 ESP32 连接的继电器模块
- 无裸线接触其他组件
- 220 伏电压始终断开



![relay-esp32](assets/fr/12.webp)





---


## 第 2 部分：软件配置



我们以*Blink*为例，但如果您喜欢其他选项，*BTCPay 服务器*也提供*Strike、Breez 和 Boltz*。



### 步骤 1：插件，安装 *BitcoinSwitch* + *Blink



1 - 使用管理员账户进入您的*BTCPay服务器*实例



2 - 创建第一个盲点



3 - 在*BTCPay服务器*的左侧，滚动到底部，进入*"管理插件 "*。



![btcpay-plugins](assets/fr/13.webp)



4 - 我们将安装 *BitcoinSwitch* 插件以及 *Blink* 插件。



![btcpay-plugins](assets/fr/14.webp)



5 - 向下滚动插件列表，点击 *"安装 "* ： *BitcoinSwitch 和 Blink*（或您选择的可用 wallet）



![btcpay-plugins](assets/fr/15.webp)



6 - 安装完成后，重启 *BTCPay 服务器*，等待 1 分钟让实例重启



![btcpay-plugins](assets/fr/16.webp)



7 - 返回 *"管理插件 "*，检查两个插件是否都已安装



![btcpay-plugins](assets/fr/17.webp)



### 步骤 2：后台：*BTCPay 服务器 + Blink* 配置



**1 - 创建一个 wallet *Blink***




- 访问 https://www.blink.sv
- 创建账户。请参阅教程 ：



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - 生成 API 密钥 *Blink***




- 访问 API 界面： **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** 并使用创建 wallet *Blink* 时使用的同一账户登录



![blink-api](assets/fr/18.webp)





   - 连接后，转到 *API 键* 选项卡



![blink-api](assets/fr/19.webp)





   - 点击右上角的 *"+"*，访问您的 API 密钥配置



![blink-api](assets/fr/20.webp)





   - 为您的 API 密钥命名，并保留默认设置。然后，在第三步中，记下您的 API 密钥--您只能看到一次：`blink_mZ5KxxxxxxxxxxxxxNbmX`。



![blink-api](assets/fr/21.webp)





   - 创建后，它应该会出现在你的活动 API 密钥列表中。



![blink-api](assets/fr/22.webp)



**3 - 将 *Blink* 连接到 *BTCPay 服务器****。




- 打开您的 *BTCPay 服务器
- 导航至 ： *Wallet* **→** *闪电



![btcpay-server](assets/fr/23.webp)





- 点击 *使用自定义节点*。
- 粘贴以下连接字符串：



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **重要** ：




- 不要修改第一部分：type=blink;server=https://api.blink.sv/graphql`；
- 仅更换 ：
    - api-key= *通过您的 API Blink* 密钥
    - wallet-id= *通过您的 wallet Blink* ID
- 然后点击*测试连接*，再点击*保存*。



![btcpay-server](assets/fr/24.webp)





 - 检查连接是否已建立（绿色状态）



![btcpay-server](assets/fr/25.webp)



**4 - 创建销售点（PoS）**




- 在 BTCPay 服务器中，进入 "插件 "选项卡，点击 "销售点"。



![btcpay-server](assets/fr/26.webp)





- 为 PoS 命个名，然后点击 *创建*。



![btcpay-server](assets/fr/27.webp)





- PoS 配置 ：
    - 选择一种销售点样式 = *打印展示 *
    - 货币 = *SATS*
    - 点击 *保存*



![btcpay-server](assets/fr/28.webp)





- 产品配置 ：
    - 删除所有默认产品
    - 然后点击*添加项目*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- 配置产品：
    - 标题 ： *烟雾机*
    - 价格 ： *10 sats*
    - Bitcoin GPIO 开关：21
    - Bitcoin 开关持续时间（毫秒） ：5000
    - 点击*关闭*，然后点击*保存*保存新产品



![btcpay-server](assets/fr/31.webp)



### 步骤 3：固件：刷新 ESP32



**1 - 转到闪存网站




- 转至 ：[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash BitcoinSwitch 固件**




- 用 USB/Micro-USB数据线将ESP32连接到电脑上
- 然后点击 *连接到设备*。
- 打开一个窗口，选择 ESP32 的 USB 端口，然后点击*连接*。



![bitcoinswitch-lnbits](assets/fr/33.webp)





- 连接好 ESP32 后，我们将更新 BitcoinSwitch 固件。在 *T-Display* 部分，点击 *Upload Firmware* 获取最新版本（当前： *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- 等待上传，当日志显示*"Leaving..."*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- 拔下 ESP32 插头



**3 - 检查 BitcoinSwitch 固件安装情况




- 重新载入页面：[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- 用 USB/Micro-USB电缆将 ESP32 重新连接到电脑上
- 然后点击 *连接到设备
- 选择 ESP32 的 USB 端口，然后点击 *连接*，如上所述
- 连接后，按下 ESP32 上的 **RESET** 按钮
- 检查日志中最后几行是否显示 ：



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(这是正常现象，表示还没有配置，但固件已经安装）。



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - 生成 WebSocket LNURL** URL



预期最终格式 ：



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



生成步骤 ：




- 打开您的 BTCPay 服务器实例，然后转到我们稍后创建的 PoS。
- 然后点击 "查看"，在浏览器中打开 PoS



![btcpay-server-https](assets/fr/37.webp)





- 复制页面的 URL，例如 ：



![btcpay-server-https](assets/fr/38.webp)



让我们来解读一下这个 URL：



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → 您的 BTCPay 服务器实例的域名
- 46XXXXXXXXXXXXXXwFB` → 您的 PoS 唯一标识符
- `/pos` → 表示销售点



改造它：




- 用 `wss://` 替换 `https://
- 在末尾添加 `/bitcoinswitch



结果



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



保留此 URL 以备将来配置，因为它将使您的 ESP32 能够与 BTCPay 服务器进行实时通信。WebSocket 协议 (`wss://`)可在两者之间建立永久连接：一旦在您的 PoS 上确认了闪电支付，BTCPay 就会立即将信息发送到 ESP32，然后 ESP32 就可以触发您的烟雾机。



**5 - 配置 WiFi 和 WebSocket




- 返回页面：连接了 ESP32 的 [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- 进入 *配置设备* → *无线设置*。



通知 ：




- WiFi SSID：WiFi 网络的名称
- WiFi 密码：您的 WiFi 密码



![bitcoinswitch-lnbits](assets/fr/39.webp)





- 在 *LNbits 设备 URL* 部分，粘贴上一步创建的 WebSocket URL
- 点击 *上传配置*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- 等待上传完成；日志中应显示您刚刚输入的参数（SSID、密码和 WebSocket URL）



![bitcoinswitch-lnbits](assets/fr/41.webp)





- 等待 ESP32 建立 WebSocket 连接。您将看到 ：



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- 现在您可以断开 ESP32 的连接



---
## 保点软件



最后测试前，检查 ：





- 连接到 BTCPay 的 Blink
- 创建了至少 1 个项目的 PoS
- 使用 BitcoinSwitch 更新 ESP32
- 在 ESP32 上配置了 WiFi
- WebSocket URL 正确
- 无错误的 ESP32 日志



---

## 测试和调试



### 完成最终测试



1.插入烟雾机（220 伏）并打开开关


2.为 ESP32 供电（电池或 USB）


3.在浏览器中打开 BTCPay PoS


4.扫描 "烟雾机 "项目


5.使用 wallet Lightning（Blink 或其他 wallet）付款


6.观察：




 - 继电器发出咔嗒声（声音响起，继电器 LED 亮起）
 - 启动烟雾机
 - 产生烟雾！



### 公平问题和解决方案



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## 资源



### 实用链接





- BitcoinSwitch 固件：[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay 服务器文档 ：[https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 引脚布局 ：[https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### 社区与支持





- BTCPay 服务器** ：[chat.btcpayserver.org](https://chat.btcpayserver.org/) - 官方 Mattermost
- BTCPay 服务器 Telegram** ：[t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** ：[t.me/lnbits](https://t.me/lnbits) - 官方 Telegram，活跃社区
- BitcoinSwitch (固件错误)**：[github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### 源代码





- BitcoinSwitch 固件源代码：[https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** 堆叠 sats，制造烟雾，享受乐趣，保持谦逊！ **⚡**
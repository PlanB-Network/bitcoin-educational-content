---
name: Canaan Avalon Mini 3
description: 将 ASIC Avalon 配置为独矿或 Miner 矿池
---

![cover](assets/cover.webp)



在本教程中，我们将介绍如何设置 Canaan Avalon Mini 3，以便在家中轻松使用 Miner。



在此之前，专为执行特定任务而设计的 ASIC（*专用集成电路*）机器--在这种情况下，Bitcoin 的 Miner 的 Hash 计算（SHA-256）--特别不适合家庭使用。噪音、产生的热量以及为支持这些设备的巨大能量而对电气设备进行调整的需要，都阻碍了我们中的大多数人参与其中。



如今，作为 ASIC 设备的主要制造商之一，迦南决定通过提供一系列噪音相对较低、安装非常简单（即插即用）的产品，来满足希望在家中使用 Miner 设备的个人市场需求。



这些设备在市场上销售，**Avalon Nano 3S（140 瓦）** 是辅助加热器，**Avalon Mini 3** 是输出功率**800 瓦**的微型散热器。



https://planb.network/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

请注意，在绝大多数情况下，与同等功率的传统加热器之间的价格差异不会让您获得经济利润。除非您能获得免费（剩余）或非常便宜的电力，否则 Mining 活动所产生的 satoshis 永远无法弥补这种价格差异。



在我看来，对于那些出于个人原因希望在家中实现 Miner 的人来说，这些设备更应该被视为一种简单的方法： *获得非 KYC Satss / 通过 Solominating 玩 "彩票"/参与 Hashrate 分散化等等......*。但至少在大多数情况下（西方国家），这并不是一种省钱的方式。



## 开箱和功能



### 阿瓦隆纳米 3S



首先，让我们看看 Avalon Mini 3 包装盒里有什么。



![image](assets/fr/24.webp)



打开包装盒，操作手册就摆在眼前，但更重要的是，WIFI 接收模块就藏在操作手册左侧的圆形白色贴纸下面。您稍后会用到它。



![image](assets/fr/25.webp)



泡沫塑料块下面是设备，从盒子里取出后就是 Supply 电源装置。



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## 开机并连接本地网络



打开包装后，尽可能将 Avalon Mini 3 放置在相对开阔的地方，以便热量正常循环。然后将小型 WIFI 接收模块插入设备底部的 USB 接口，插入电源 Supply，并确保电源按钮位于 "1 "位置。



![image](assets/fr/28.webp)



完成这些步骤后，设备的 LED 显示屏会亮起并显示 "蓝牙 "符号，表明它已准备好通过 Avalon Family 应用程序连接到本地网络。



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



为此，请访问您的移动应用程序商店，搜索并下载 **Avalon Family** 应用程序。



![image](assets/fr/11.webp)


安装完成后，点击右上角的 "跳过 "打开，然后点击 "添加 "按钮，最后点击 "搜索"。确保智能手机已启用蓝牙，以便顺利检测设备。



![image](assets/fr/12.webp)


应用程序检测到设备后，点击设备并选择 "连接"。然后，您将进入输入 WIFI 连接详细信息的界面。


![image](assets/fr/13.webp)


连接到本地网络后，Mini 3 将显示 IP Address、时间、Hashrate 和电量等信息。



下面是 Mini 3 的一般技术指标汇总表：



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## 连接到 Mining pool



**这部分与 Nano 3s 和 Mini 3 设备通用，因为流程完全相同 **



无论是 "独占 "还是 Miner "池"，我们都需要连接到 Mining pool。事实上，我们的设备只是一个 Hash 制造器，对 Bitcoin 网络没有任何感知。将它连接到池中，它就能访问 Bitcoin 网络，并接收区块模板进行工作。



### 使用应用程序连接 Mining pool



在 Avalon Family 应用程序中，选择设备，如下图所示。系统会自动要求您更改机器的管理员密码。如果要更改，请单击 "OK（确定）"；如果要保留默认访问密码 "admin"，请单击 "Cancel（取消）"。


![image](assets/fr/16.webp)


然后选择 "设置"，再选择 "池配置"，输入 3 个所需池的参数。


如果其中一个池出现故障，2 号池和 3 号池将作为备份，这样你的 Miner 就不会白白工作。默认情况下，Hashrate 将指向 1 号池



就我们而言，我们选择




- 1 - 公共游泳池、
- 2 - CkPool、
- 3 - 海洋



![image](assets/fr/17.webp)



有关如何连接 Mining pool 的详细信息，请参阅这些教程 ：



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.network/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

总之，我们需要





- 池 Address，通常为 **stratum+tcp://xxxxxxxx:port**。





- 由 *your Bitcoin Address* 和您为设备选择的 *pseudo* 组成的 "工作者 "名称，2 之间用 *dot* 分隔，例如：**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- 密码，通常总是 "**x**"



输入泳池信息后，点击 "保存"。



![image](assets/fr/18.webp)


按照说明重新启动设备，等待几分钟，直到 Hashrate 指向您的首选泳池 (#1)。



### 使用浏览器连接 Mining pool



您还可以连接到 Mining pool，更广泛地说，可以通过您喜欢的浏览器访问设备的 Interface 管理系统。



为此，请在浏览器搜索栏中输入下图所示设备的 IP Address，例如 **192.168.144.6**



![image](assets/fr/15.webp)



将出现以下页面，要求您打开 Avalon Family 应用程序并扫描应用程序显示的 QR 代码。



![image](assets/fr/20.webp)



打开应用程序，点击右上角的 3 个破折号，然后点击扫描。扫描浏览器的二维码，然后输入应用程序的管理员密码，点击确定。



![image](assets/fr/21.webp)



这里是与 Avalon 交互的网页。与其说它是一种配置手段，不如说它是一个显示机器指标的仪表盘。



但仍可通过点击右下角的**"池配置 "**来访问池设置。



![image](assets/fr/22.webp)



与手机应用程序相同，您可以在此输入泳池参数。



![image](assets/fr/23.webp)



## 通过 Avalon Family 应用程序控制设备



现在，我们已经将家用 Miner 连接到本地网络，并将 Hashrate 对准 Minings 水池。现在，让我们通过 Avalon Family 应用程序来了解我们机器的基本功能。



在 Avalon 系列应用程序的主菜单中，点击与 Avalon Mini 3 相对应的图标。您将直接进入管理运行模式的菜单。



有 3 个选项可供选择："加热器 "模式、"Mining "模式或 "夜间 "模式。





- 在 "加热器 "模式下，有两个功率级别 "节能 "或 "超级"。


生态 "级别对应的加热功率为 500 瓦，Hashrate 约为 25 Th/s，声级为 40 dB。


超级 "电平相当于 650 W 的输出功率（约 30Th/s 和 45 dB）。在该模式下，您可以设定一个最高环境温度，当温度超过该温度时，设备将停止工作。



![image](assets/fr/36.webp)




- 在 "Mining "模式下，设备以最大速度运行，无需设定目标温度（当然，除了内置的过热限制）。这样做的目的是充分发挥 Miner 的性能。在该模式下，输出功率接近 800 W，速度约为 37.5 Th/s，噪音水平为 50-55 dB。



![image](assets/fr/37.webp)


最后，在 "夜间 "模式下，Mini 3 可以最低速度运行，噪音最小。400 瓦、20 Th/s 和约 33 分贝。



在这里，您也可以设置一个目标温度，当温度超过该温度时，设备将进入非激活模式并停止 Miner。如果温度下降，设备将重新启动并恢复加热和 Miner。在此模式下，LED 显示屏默认关闭，但您可以根据需要选择打开，以便在黑暗中照亮房间，就像夜灯一样（见下图）。



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



最后，您还可以通过 "显示 "菜单对 Avalon 的 LED 进行操作。您可以选择滚动显示相关的操作信息，也可以选择显示时间，甚至是自定义（像素化）图像。



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



与 Avalon Nano 3S 一样，"设置 "菜单可让您更改管理员密码、水池设置、检查过滤器阻塞情况（位于设备底部）、联系技术支持或查看设备日志。



![image](assets/fr/42.webp)



同样，可以用吸尘器清洁设备底部的过滤器，而且越定期越好。



本教程的最后，我们将学习如何将 Avalon Mini 3 连接到本地网络，如何将 Hashrate 指向 Mining 池，以及如何使用 Avalon Family 应用程序浏览选项和设置。



要了解更多信息，请参阅我们关于缩小版 Avalon：Nano 3S 的教程。



https://planb.network/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6
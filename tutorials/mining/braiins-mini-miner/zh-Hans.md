---
name: Braiins Mini Miner
description: 在家轻松制作 Mining。
---
![cover](assets/cover.webp)



## 导言



迷你型 Miner Braiins BMM 100 是 Mining pool Braiins 推出的一款产品。该设备设计美观，噪音极低。它的计算能力为 1.1 Th/s，功耗约为 40 瓦。与其他设备不同的是，它不是开源的，但安装非常简单，只需点击几下即可！Mini Miner BMM 100 是发布的第一个版本。现在，第二版正在生产中，名为 BMM 101，与第一版不同的是，它的显示屏更大，而且带有 Wi-Fi，但安装程序是一样的。



您还可以直接在 [制造商网站](https://braiins.com/hardware/mini-Miner-bmm-100) 上查看完整指南，了解更多重要信息。



## BMM 100概览



该设备看起来像一个平行六面体，正面有显示屏



![image](assets/en/01.webp)



上风扇



![image](assets/en/02.webp)



背面有：电源孔、SD 卡空间（可能需要用于任何更新）、一个写有 "IP 报告 "的小按钮，可让您知道迷你 Miner 的 IP Address，访问设备仪表板需要使用 Address。按下按钮后，IP Address 会显示约 5 秒钟，然后消失，重新出现设置屏幕。不过，如果您需要更改某些设置，只需再次按下相关按钮，IP Address 就会重新出现在屏幕上。继续查看列表，我们会发现一个以太网端口和一个执行设备重置的入口，为此您需要抓住一个针脚并按住 10 秒钟，以重置迷你 Miner 的所有设置。最后，我们还可以看到两个指示灯，一个是 Green 指示灯，另一个是红色指示灯，用于指示 Miner 的状态。



![image](assets/en/03.webp)



## 连接迷你 Miner



您需要通过以太网将设备连接到互联网，请注意新版本（BMM 101）不再需要这样做。回到这个迷你 Miner，找到位置后，我们需要先将其连接到互联网线路，然后再连接到电源：设备会自动打开，并在屏幕上显示其 IP Address。



## 配置



我们需要打开浏览器，在搜索栏中输入显示迷你 Miner 的 IP Address。我提醒您，要在网络上找到设备，您必须是本地用户，因此您使用的电脑必须与迷你 Miner 连接到同一网络。输入 IP Address 后，按下回车键，屏幕上将出现迷你 Miner 操作系统（Braiins OS）的登录页面。



![image](assets/en/06.webp)



要登录，您必须输入 "root "作为用户名，密码可以留空。点击登录，您的迷你 Miner 面板就会出现。



![image](assets/en/07.webp)



## 常规设置



让我们进入系统



![image](assets/en/24.webp)



在设置中，我们可以找到一些常规设置，如主题（浅色或深色）、语言、时区和密码更改。



![image](assets/en/25.webp)



如果我们转到 "迷你 Miner 屏幕"，则可以对迷你 Miner 进行设置，例如屏幕显示。我们可以选择是显示时间、Bitcoin 的价格，还是显示机器状态信息，如产品 Hash、温度、消耗功率等。我们还可以改变屏幕亮度，设置夜间模式，以 12 小时或 24 小时格式显示时间。



![image](assets/en/26.webp)



更改完成后，点击 "保存更改"，即可在设备屏幕上看到更改内容。



![image](assets/en/27.webp)



## 与 Mining pool 连接



现在我们还不能运行，因为我们必须连接到一个池才能启动 Mining，所以我们必须转到 "配置 "页面



![image](assets/en/08.webp)



而第一个条目只是 `Pools`。



![image](assets/en/09.webp)



在这里，我们必须决定使用哪个池。在本教程中，我将向你展示两种选择。第一种是连接到 Mining pool Braiins，从本教程中可以看出，专业矿工也在使用该矿池：



https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

第二种方法是将我们连接到单机版的 Mining pool，如 Public Pool，请按照本指南进行操作：



https://planb.academy/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### 布雷恩斯游泳池



要连接到该池，我们需要创建一个账户。该池也使用 Lightning Network 进行支付，因此我们每天可以收到一些 Sats。为此，我们需要设置一个接收奖励的 Address 闪电。如果您不知道如何在 Braiins pool 上创建帐户或如何设置您的 Address 闪电，可以参考本指南：



https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

完成后，我们就进入了Braiins矿池仪表盘。我们要做的就是告诉矿池，我们要连接我们的矿工，所以在屏幕左侧，你会发现很多条目。我们需要转到 "工人"。



![image](assets/en/04.webp)



我们需要点击右侧的紫色按钮，上面写着 "连接工人"。



![image](assets/en/05.webp)



这里会出现一个窗口，提供我们将迷你 Miner 连接到池所需的信息。在这里，我们唯一能做的更改就是选择 Stratum V2。要了解什么是 Stratum v2，请参阅 [词汇表](https://planb.academy/en/resources/glossary/stratum-v2) 中的此条目。



![image](assets/en/10.webp)



现在，我们需要复制这个以 stratumv2 开头的字符串。因此，我们点击小 "复制 "符号，然后转到迷你 Miner 的仪表板，我们在配置和池中留下了迷你 Miner。点击添加新池



![image](assets/en/11.webp)



并将我们复制的字符串粘贴到 Pool URL 下方的空格中。



![image](assets/en/12.webp)



现在我们需要添加用户名和密码。让我们回到池 dashboad。下面还有用户名和密码。用户 ID 和我们的用户名，即创建账户时给出的用户名，再加上我们要输入的 Miner 的名称。您可以决定是否为连接到池中的设备赋予一个名称，这是可选项，但建议您输入，这样如果您连接了多个设备，就能更容易地立即识别它们。如果不想输入任何信息，可以不填 `workerName`。



![image](assets/en/13.webp)



然后，我们进入迷你 Miner 并输入用户名。在我的例子中，我们将输入 "finalstepbitcoin"，这是我的用户 ID，最小点数。这是我决定给设备起的名字。如果你不想给它命名，只需输入 userid dot workername 即可。在我的例子中就是 finalstepbitcoin.workername。输入用户名后，您可以选择一个密码，并将其写入空白区域。您也可以输入 anithing123，这也是在池屏幕上显示的密码，但它只是想表明您可以输入任何您想要的密码。



输入所有数据后，您必须按下右侧的保存按钮（软盘形状的那个），这样您就在迷你 Miner 中配置了池数据。



![image](assets/en/14.webp)



现在，您必须返回到池仪表板并单击 "已连接！返回"。



![image](assets/en/15.webp)



我们已将迷你 Miner 连接到 Braiins 池！现在您可以在工人列表中看到它了。如果没有显示，只需刷新并等待片刻。一旦出现，请确认其状态为 "OK"，并带有 Green 复选标记。



![image](assets/en/17.webp)



如果您回到仪表板，您应该开始看到图表上的移动，并看到我们设备的 Hashrate。这意味着水池正在接收我们的工作，因此我们的目的就是破坏。



![image](assets/en/16.webp)



### 公共游泳池



通过这个矿池，我们可以试试自己的运气，靠着矿池独自挖矿。在这种情况下，我们不会获得奖励，但如果我们成功挖出一个区块，我们将获得全部奖励。然后，我们将链接到完全开源的 Mining 公共矿池。我们在浏览器上打开一个新窗口，进入 [web.public-pool.io](https://web.public-pool.io/#/)。



![image](assets/en/18.webp)



就会出现一个包含我们所需的所有信息的页面。然后，我们在这里复制地层 Address



![image](assets/en/19.webp)



然后，我们回到迷你 Miner 的仪表板，转到配置和池，点击添加新池（与上述过程相同），并在池 url 下粘贴 "stratum Address"。



![image](assets/en/20.webp)



现在，让我们回到 "池 "页面，看看作为用户名，我们必须输入 Bitcoin Address（如果我们破坏了一个区块，就会在这个区块上获得奖励），然后输入一个点，然后输入我们的设备名称，就像我们之前在 "Braiins Pool "中做的那样，而密码我们可以自己选择。



![image](assets/en/21.webp)



我们回到迷你 Miner，在用户名下粘贴一个 Address Bitcoin，后面跟句号和名称，我将输入 "miniminer"。在密码中，我将填入 test，你可以随意输入。



![image](assets/en/22.webp)



现在我们保存设置并禁用 Braiins 池。



![image](assets/en/23.webp)



很好！我们现在是公共泳池的 Mining！



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)
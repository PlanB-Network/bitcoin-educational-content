---
name: Tor浏览器
description: 如何使用Tor浏览器？
---
![cover](assets/cover.webp)

正如其名称所示，浏览器是一种用于浏览互联网的软件。它充当用户机器与网络之间的网关，将网站的代码转换为互动和可读的页面。选择您的浏览器非常重要，因为它不仅影响您的浏览体验，还影响您的在线安全和隐私。

注意不要将浏览器与搜索引擎混淆。浏览器是您用来访问互联网的软件（如Chrome或Firefox），而搜索引擎是一种服务，例如Google或Bing，它帮助您在线查找信息。

如今，Google Chrome是目前最广泛使用的浏览器。它占全球市场的大约65%（截至2024年）。Chrome因其速度和性能而受到赞赏，但它不一定是每个人的最佳选择，特别是如果隐私对您来说是优先考虑的话。Chrome属于Google，这是一家以收集和分析用户大量数据而闻名的公司。实际上，他们的内部浏览器是他们监视策略的核心。这款软件是您大多数在线互动的中心组成部分。掌握浏览器上的数据收集对Google来说是一个重要问题。
![TOR BROWSER](assets/notext/01.webp)
*来源: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*

浏览器有几个主要的家族，每个家族都基于特定的渲染引擎。像Google Chrome、Microsoft Edge、Brave、Opera或Vivaldi这样的浏览器都建立在Chromium浏览器上，这是Google开发的Chrome的轻量级和开源版本。所有这些浏览器都使用Blink渲染引擎，它是WebKit的一个分支，而WebKit本身是从KHTML衍生出来的。Chromium在市场上的主导地位使得基于它的浏览器特别高效，因为网页开发者倾向于主要为Blink优化他们的网站。

苹果的浏览器Safari使用的是WebKit，它也来源于KHTML。

另一方面，像Mozilla Firefox、LibreWolf和Tor浏览器这样的浏览器依赖于Gecko，这是一个不同的渲染引擎，最初来自Netscape浏览器。

选择合适的浏览器取决于您的需求。但如果您至少关心您的隐私，因此也关心您的安全，我推荐一般使用Firefox，为了更多的隐私则使用Tor浏览器。在这个教程中，我将向您展示如何轻松开始使用Tor浏览器。
![TOR BROWSER](assets/notext/02.webp)

## Tor浏览器简介

Tor浏览器是一款专为尽可能安全和私密的互联网导航而设计的浏览器。该浏览器基于Firefox，因此基于Gecko渲染引擎。
Tor浏览器使用Tor网络加密并通过多个中继服务器路由您的流量，然后再将其传输到目的地。这种称为“洋葱路由”的多层路由过程有助于隐藏您的真实IP地址，使得难以识别您的位置和在线活动。然而，与不使用Tor网络的标准浏览器相比，浏览速度必然更慢，因为它是间接的。
与其他浏览器不同，Tor浏览器集成了特定功能以防止跟踪您的在线活动，例如隔离每个访问的网站，并在关闭时自动删除cookies和历史记录。它还旨在最小化指纹识别的风险，通过使所有用户对访问的网站看起来尽可能相似。
您完全可以使用Tor浏览器访问标准网站（如`.com`、`.org`等）。在这种情况下，您的流量通过多个Tor节点匿名传输，最后到达一个出口节点，该节点与明网上的最终站点通信。![TOR BROWSER](assets/notext/03.webp)
您也可以使用Tor浏览器访问隐藏服务（以`.onion`结尾的地址）。在这种场景下，所有流量都保留在Tor网络内，没有出口节点，确保了用户和目的服务器的完全隐私。这种操作模式通常用于访问有时被称为“*暗网*”的互联网部分，这部分互联网不被传统搜索引擎索引。
![TOR BROWSER](assets/notext/04.webp)

## Tor网络与Tor浏览器有什么区别？

Tor网络和Tor浏览器是两个不应混淆的不同事物，但它们是互补的。Tor网络是一个由用户操作的全球中继服务器基础设施，通过在将互联网流量通过多个节点传输后再将其定向到最终目的地，从而实现匿名化。这就是著名的洋葱路由。

另一方面，Tor浏览器是一个特定的浏览器，旨在以简单的方式访问这个网络。它默认集成了连接到Tor网络所需的所有设置，并使用了修改版的Firefox，以提供熟悉的浏览体验，同时最大化隐私和安全性。

Tor网络不仅仅被Tor浏览器使用。它可以被各种软件和应用程序用来保护它们的通信。例如，可以在您的比特币节点上启用通过Tor网络的通信，以隐藏您的IP地址免于其他用户的查看，并防止您的互联网服务提供商监视您与比特币相关的流量。
总而言之，Tor网络是提供我们互联网浏览隐私的基础设施，而Tor浏览器是允许我们在网页浏览中使用这个网络的软件。

## 如何安装Tor浏览器？

Tor浏览器适用于电脑的Windows、Linux和macOS，以及智能手机的Android。要在您的电脑上安装Tor浏览器，请访问[官方Tor项目网站](https://www.torproject.org/)。
![TOR BROWSER](assets/notext/05.webp)
点击“*下载Tor浏览器*”按钮。
![TOR BROWSER](assets/notext/06.webp)
选择适合您操作系统的版本。
![TOR BROWSER](assets/notext/07.webp)
点击可执行文件开始安装，然后选择您的语言。
![TOR BROWSER](assets/notext/08.webp)
选择软件将要安装的文件夹，然后点击“*安装*”按钮。
![TOR BROWSER](assets/notext/09.webp)
等待安装完成。
![TOR BROWSER](assets/notext/10.webp)
最后，点击“*完成*”按钮。
![TOR BROWSER](assets/notext/11.webp)

## 如何使用Tor浏览器？

Tor浏览器的使用方式类似于标准浏览器。
![TOR BROWSER](assets/notext/12.webp)
首次启动时，浏览器会向您展示一个页面，邀请您连接到Tor网络。只需点击“*连接*”按钮即可建立连接。
![TOR BROWSER](assets/notext/13.webp)
如果您希望软件在您将来使用时自动连接到Tor网络，请勾选“*总是自动连接*”选项。
![TOR BROWSER](assets/notext/14.webp)
一旦连接到Tor网络，您将到达首页。
要在互联网上进行搜索，只需在搜索栏中输入您的查询内容并按下“*enter*”键。
然后，您将以与其他浏览器相同的方式获得来自您的搜索引擎的结果。
DuckDuckGo上的“*Onionize*”选项允许您通过访问其在Tor网络上的`.onion`地址，使用该搜索引擎的隐藏服务。

## 如何配置Tor浏览器？

在浏览器屏幕的顶部，您会找到一个导入收藏夹的选项。这允许您自动将旧浏览器中的书签集成到Tor浏览器中。
您还可以通过点击正在访问的网页右上角的星形图标来添加新的书签。
在右侧的菜单中，您可以访问各种选项。"*New identity*"按钮允许您更改您的Tor身份。具体来说，这使您能够在Tor上开始一个新的用户会话，意味着更改您的IP地址并重置cookies和打开的会话。
"*Bookmarks*"菜单允许您管理您的书签。
"*History*"允许您访问您的浏览历史，如果您在设置中启用了它。
"*Add-ons and themes*"菜单允许您自定义浏览器的外观或添加扩展。由于Tor浏览器基于Mozilla Firefox，您可以使用适用于Firefox的主题和扩展。
最后，"*Settings*"按钮让您访问浏览器的设置。
在设置的"*General*"标签中，有各种选项允许您自定义Tor浏览器用户界面。
在"*Home*"标签中，您可以选择更改打开Tor浏览器和打开新标签页时显示的默认页面。
在"*Search*"标签中，您可以选择搜索引擎。Tor浏览器默认使用DuckDuckGo，这是一个专注于保护用户隐私的搜索引擎，但您也可以选择Google或Startpage等。
您还可以为您的搜索引擎设置快捷方式。
例如，您可以在浏览器的搜索栏中输入“*@wikipedia*”后跟您的搜索词，如“*Bitcoin*”。
这个功能随后会直接在Wikipedia网站上搜索您的术语。
您可以为不同的网站设置其他自定义快捷方式。

接下来，在“*Privacy & Security*”标签中，您将找到所有与隐私和安全相关的设置。
您可以选择保留或删除您的浏览历史。
![TOR 浏览器](assets/notext/34.webp)您还可以管理您授予不同网站的访问权限。
![TOR 浏览器](assets/notext/35.webp)
为了您浏览器的整体安全，“*更安全*”和“*最安全*”模式允许您调整访问网站时执行的网页功能和脚本。这最小化了利用漏洞的风险，但也会相应地影响网站的显示和交互性。![TOR 浏览器](assets/notext/36.webp) 您将找到其他安全选项，包括危险内容阻止器和仅限 HTTPS 模式，确保与网站的连接始终遵循此协议。![TOR 浏览器](assets/notext/37.webp) 最后，在“*连接*”标签中，您将找到所有与连接到 Tor 网络相关的设置。这是您可以配置桥接以从可能审查其访问的地区访问 Tor 的地方。![TOR 浏览器](assets/notext/38.webp) 就这样，您现在已经准备好以更安全、更私密的方式浏览互联网了！如果在线隐私是您感兴趣的话题，我还推荐发现这个关于 Mullvad VPN 的其他教程：

https://planb.network/tutorials/others/general/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8
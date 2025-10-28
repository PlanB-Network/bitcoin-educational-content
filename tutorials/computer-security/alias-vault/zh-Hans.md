---
name: Alias Vault
description: 管理密码、双因素身份验证和别名的强大工具（内置电子邮件服务器）--也可自行托管！
---

![cover](assets/cover.webp)



网络隐私和安全是任何人，无论从事何种业务，都应密切关注的话题。



此外，这些问题也是这个不断动荡的世界的一部分：越来越多的开发人员参与到这一主题中来，为已有的解决方案和新产品提供实施方案。



这就是**Leendert de Borst**和他的 "别名保险库"（Alias Vault）的情况，这是一个革命性的工具（同类产品中的第一个），允许您管理和存储密码，使用密码记录验证网络服务，管理双因素验证，但最重要的是generate真正的别名，所有这些都在一个单一的Interface中。



**但是，Alias Vault 并没有就此止步**。



## 主要功能



Alias Vault 可在开发者的服务器云端运行，也可在自己的基础架构中自托管，Docker 文件和镜像可通过 scipt 安装。除了网络版 Interface，还提供适用于所有流行浏览器的扩展，以及适用于 iOS 和 Android 的移动应用程序；后者也可以绕过谷歌官方商店，从 F-Droid 下载。



其中一个 Interface 别名 Vault 是：




- 免费开放源代码**
- 密码管理器**，用于存储所有复杂密码。使用浏览器扩展，密码管理器可完成网站登录
- 2FA**，支持双因素身份验证
- 带有嵌入式电子邮件服务器的别名管理器**：Alias Vault 不会创建将电子邮件转发到用户邮箱的别名；相反，它会创建实际的别名，包括名、姓、性别、用户名、密码和生日（如果需要这些信息）。



软件包中还包含大量详尽的文档，将帮助新用户发现这一强大的工具。



## 无个人数据！



一如既往，它从 [aliasvault.net](aliasvault.net) 网站开始。如前所述，Alias Vault 可以在自己的服务器上使用，也可以从开发人员的云端使用，以便在转为自托管解决方案之前熟悉它。



该网站的图形非常醒目，而且维护得很好： **创建账户**。



![img](assets/en/01.webp)



让您大吃一惊的是，Alias Vault 并不要求您提供个人信息：创建账户所需的只是任何昵称，只要是您熟悉的单词即可。同意服务条款，选择单词，然后继续。



![img](assets/en/02.webp)



现在设置**"主密码 "**，这是您整个新系统中最重要的信息。事实上，有了这个密码，您将是唯一可以访问/恢复该账户的人，因为它将使您的 "保险库 "在托管您信息的服务器上保持加密。



![img](assets/en/03.webp)



事实：您创建了自己的密码管理器和别名管理器，但没有提供自己的工作专用电子邮件 Address。



![img](assets/en/04.webp)



Alias Vault 欢迎您来到一个安全、崭新、个性化但也空旷的空间。现在，我们开始填充它。



如果您已经有了密码管理器，可以从正在使用的密码管理器中导入文件，以评估与其他提供商的不同之处，或者也可以取消别名管理器，以便在一个应用程序中管理所有内容。



![img](assets/en/05.webp)



Alias Vault 非常简单：只有一个主页面，即 "主页"，有两个菜单：




- 证书"：可让您创建并管理身份和别名
- 电子邮件"：收件箱，您可以在其中检查所生成别名的来信。



![img](assets/en/06.webp)



我们感兴趣的是创建第一个 "别名"，因此请转到页面右上方，点击 _+New Alias_（新建别名）。



![img](assets/en/07.webp)



按照 Alias Vault 的设计理念，最初的菜单看起来非常简约。要了解此功能的特点，请单击_通过高级模式创建_。



![img](assets/en/08.webp)



在第一个屏幕的上半部分，你可以用它来导入已订阅的服务或最常用的在线服务的密码凭证。



如果您在上述任何（或所有）服务上启用了双因素身份验证，您还可以使用 Alias Vault 通过导入 "秘钥 "来管理这一额外的 Layer 安全性。Alias Vault 将创建访问所需的 "TOTP"。



![img](assets/en/09.webp)



**注意**：在为电子邮件 Address 预留的空间中，Alias Vault 默认设置了自己的域名；为了使用您之前创建的正确 Address 账户，请单击 _Enter custom domain_（输入自定义域名），以便在 `@`后设置正确的域名。



![img](assets/en/14.webp)



这个屏幕的底部是最有趣的部分。点击_Generate Random Alias_（生成随机别名），Alias Vault 就会根据不同的需要为您创建不同的身份，每个身份都有自己的邮箱、非常强大的密码级别，并辅以其他详细信息，如性别、出生日期和合适的昵称。



![img](assets/en/10.webp)



在相应的菜单中，您可以更改影响密码生成的设置，如只选择小写字母和删除可能含糊不清的字符。



![img](assets/en/11.webp)



您可以使用 Alias Vault 建议的别名电子邮件，也可以点击相应的下拉菜单更改域。



![img](assets/en/12.webp)



在将此电子邮件用于登录服务之前，您可以通过从自己的 Address 向新创建的邮箱发送信息来测试其功能。



![img](assets/en/13.webp)



**⚠️ 警告**：由于 Alias Vault 的内置服务器，您可以接收电子邮件，但这只允许您接收电子邮件，不允许您回复，也不允许您使用具有 "传统 "别名服务功能的电子邮件信箱。因此，它与 Simple Login、Addy 和其他专门提供此类服务的平台有很大不同。有关简单登录的示例，请参阅专门的教程：



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

要删除作为测试创建的别名，只需登录 "主页"，然后登录 "证书"，点击要删除的身份。右上角会出现_Delete_（删除）命令供您执行。



![img](assets/en/16.webp)



## 浏览器扩展



根据您的需要，您可以使用浏览器扩展，这可以在最广泛使用的浏览器上找到。



![img](assets/en/15.webp)



它的安装方式与其他扩展一样，所以我就不多说了。



浏览器扩展的作用是方便登录在线服务，或根据需要创建新的别名：如果服务存储在别名保险库的记录中，自动填充功能就会完成所需的操作。



![img](assets/en/17.webp)



唯一需要注意的是，要确认 Alias Vault 处于活动状态。事实上，应用程序有一个默认设置，即在一段时间不活动后会暂停。这是一项非常有用的功能，例如，当您必须离开电脑，防止他人访问您的账户时**。如果上一次会话仍在缓存中，则通过简化程序，输入 "主密码 "即可再次登录。注销时间是您可以自定义的参数之一，您可以根据自己的喜好缩短或延长注销时间。



## 移动应用程序



与所有此类值得尊敬的应用程序一样，Alias Vault 也有 Android 和 iOS 移动设备版本。安卓版可从 [F-Droid](https://f-droid.org/packages/net.aliasvault.app/) 下载。



在撰写本文时（2025 年 8 月末），移动应用程序认为 "自动填充 "是一项试验性功能，除极少数网站外无法使用。在完全实现之前，在移动设备上使用 Alias Vault 需要复制/粘贴数据。



从商店下载应用程序后，只需输入在网络应用程序上创建的用户和 "主密码 "即可登录。



![img](assets/en/18.webp)



打开 "保险库 "时，系统会询问您是否要启用生物识别控制访问，这是一种额外的 Layer 安全措施，可防止其他人碰巧拿着您的手机访问您的密码。



![img](assets/en/19.webp)



如果您决定设置生物识别检查，请继续。如果跳过这一步又改变主意，也可以稍后从_设置_菜单中进行配置。



完成登录后，您会发现已经创建的数据再次同步。



![img](assets/en/20.webp)



移动应用程序可通过路由连接到其服务器上托管的 "保险库"。



![img](assets/en/22.webp)



下一节我们将简要介绍的正是自托管版本。



## 自助托管：完全控制您的数据



公平地说，Alias Vault 并不是第一个允许您在基础设施上部署服务的 "密码管理器"。还有其他一些产品，但有的存在局限性，有的则部分关闭了源代码。



机会是独一无二的： **不再依赖外部服务提供商或云，而是使用自己的本地服务器来保护和管理密码、别名以及与之相关的极其敏感的信息**。使用 Alias Vault，您还可以将电子邮件服务指向自己的电子邮件服务器，以提高保密性。



现在，请查阅 [文档](https://docs.aliasvault.net/installation/)，了解如何继续自托管 Alias Vault。



![img](assets/en/23.webp)



Alias Vault 在 Docker Compose 上运行，因此只需具备最低限度的 Linux 和 Docker 经验。您可以从基本安装开始，然后完成更高级的解决方案。



您的服务器必须运行在 64 位机器上，使用 Linux 发行版、1 GB 内存和至少 16 GB 的存储空间；Docker (CE) 的版本必须至少是 20.10 或更高，而 Docker Compose 需要 2.0 或更高版本。



我决定用瘦客户机试用 Alias Vault，瘦客户机上安装了 DietPi 作为发行版，它以 Debian Bookworm 为基础，已优化到最基本的程度，并已运行了 "Docker "和 "Docker Compose"。



首先，为了保持一定的顺序，请在主目录下创建一个目录，打开 "终端 "并粘贴运行安装脚本的命令。



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



安装完成后，您将找到自己的访问凭证：


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



安装后检查目录内容。



![img](assets/en/29.webp)



使用命令启动 Alias Vault：



``` 启动-别名-保险库


./install.sh 启动


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## 关于加密和安全的考虑



![img](assets/en/32.webp)



根据 Lanedirt 在网站、文档和 Github 上的说明，使用 Alias Vault，**您放在 Alias Vault 上的所有信息（组件）都会与设备紧密绑定，经过加密，不知道 "主密码 "的任何人都无法访问**。



因此，"主密码 "是整个 "保险库 "的基本要素。输入密码后，将通过 Hard 密钥推导功能的 "Argon2id "算法进行处理，以防止密码离开设备。



即使是云或托管服务经理也无法看到所有信息。事实上，在管理面板上无法访问用户的详细信息，只能知道他们是否创建了别名、是否收到了电子邮件，其他几乎一无所知。



所有存储的内容都通过从 "主密码 "中提取的加密密钥进行加密和解密。 **服务器上只存储加密数据，不会出现纯文本**。如果用户忘记或丢失了 "主密码"，与其相关的账户将不可逆转地丢失，因为服务器无法访问明文内容。



自托管版本有重置 "主密码 "的脚本，但这并不能防止数据丢失。



![img](assets/en/33.webp)



由于 Alias Vault 还处于 _Beta_ 阶段，如果您更改/更新主密码，可能会很难访问它。我建议您从一开始就选择稳健、复杂的密码，这样您可以尝试使用该服务，并最终决定是否使用。如果您在更新密码后难以访问云，请联系 Alias Vault 支持。



要全面了解 Alias Vault 采用的架构和安全性，我强烈建议您查阅 [本页](https://docs.aliasvault.net/architecture/)，其中包含其运行所依据的加密技术的详细信息。



## 路线图


开发人员的目标是到 2025 年底使 Alias Vault 成熟稳定，从而确定其未来的使用特点。



Alias Vault 现在是、将来也会一直是开源和免费的，但可能不会像测试版那样无限制地免费。一些付费功能正在实施过程中，已经公布。



有团队/家庭计划和对硬件密钥的支持，后者用于使用 FIDO2 或 WebAuth 进行身份验证。



## 谁需要 Alias Vault



**这样的工具非常适合把网络隐私放在第一位的人**。



您的身份很可能是您在网上开展业务的核心，因此必须采取一切手段保护您的身份数据，防止那些不择手段获取您网上行为数据的服务、公司和中间商窃取您的身份数据。



Alias Vault 让您重新获得对凭证的完全控制权，减少或完全消除依赖第三方保护和加密您最敏感数据的需要。



Alias Vault 的架构和加密设施是主权个人、中小型企业、开发团队和所有**开源**应用程序爱好者的理想选择。如果您属于这些类别中的任何一类：请尽情探索 Alias Vault。
---
name: 贡献 - GitHub 桌面教程（中级）
description: 使用 GitHub 桌面在 Plan ₿ 网络上提出教程的完整指南
---
![cover](assets/cover.webp)

在学习本教程添加新教程之前，您必须完成一些初步步骤。如果您还没有这样做，我请您先查阅本入门教程，然后再回到这里：

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
你已经有了：


- 选择教程主题；
- 通过[Telegram 群组](https://t.me/PlanBNetwork_ContentBuilder) 或 paolo@planb.network 与 Plan ₿ Network 团队联系；
- 选择您的贡献工具。

在本教程中，我们将了解如何通过 GitHub Desktop 设置本地环境，在 Plan ₿ Network 上添加自己的教程。如果你已经熟练掌握 Git，可能就没必要看这么详细的教程了。我建议您参考另一篇教程，其中只介绍了主要指南，没有详细的分步指导：


- 经验丰富的用户**：

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
如果你不想设置本地环境，可以参考另一篇专为初学者设计的教程，我们将直接通过 GitHub 的网页界面进行更改：


- 初学者（网络界面）**：

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## 先决条件

学习本教程所需的软件：


- [GitHub Desktop](https://desktop.github.com/)；
- 类似 [Obsidian](https://obsidian.md/) 的标记文件编辑器；
- 代码编辑器（[VSC](https://code.visualstudio.com/) 或 [Sublime Text](https://www.sublimetext.com/)）。

![TUTO](assets/fr/01.webp)

开始教程前的先决条件：


- 拥有 [GitHub 账户](https://github.com/signup)；
- 有一个 [Plan ₿ Network source repository](https://github.com/PlanB-Network/bitcoin-educational-content) 的 fork；
- 有 [Plan ₿ Network 上的教授简介](https://planb.network/professors)（仅限于您提出的完整教程）。

如果您在获得这些先决条件方面需要帮助，我的其他教程将为您提供帮助：

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
一旦一切就绪，本地环境中的 Plan ₿ Network 分支也设置妥当，就可以开始添加教程了。


## 1 - 创建新分支

打开浏览器，进入 Plan ₿ Network 代码库的分叉页面。这是您在 GitHub 上建立的分叉。你的分叉的 URL 应该是这样的: https://github.com/PlanB-Network/bitcoin-educational-content

![TUTO](assets/fr/03.webp)

确保你在主分支 `dev` 上，然后点击 `Sync fork` 按钮。如果您的分叉不是最新的，GitHub 会提供更新分支的服务。继续更新。相反，如果您的分支已经是最新的，GitHub 会通知您：

![TUTO](assets/fr/04.webp)

打开 GitHub 桌面软件，确保在窗口左上角正确选择了你的 fork：

![TUTO](assets/fr/05.webp)

点击 "Fetch origin "按钮。如果本地版本库已经是最新的，GitHub Desktop 不会建议采取任何额外行动。否则，"Pull origin "选项就会出现。点击该按钮更新本地版本库：

![TUTO](assets/fr/06.webp)

确认您确实在主分支 `dev` 上：

![TUTO](assets/fr/07.webp)

单击该分支，然后单击 "新建分支 "按钮：

![TUTO](assets/fr/08.webp)

确保新分支基于源代码库，即 `PlanB-Network/bitcoin-educational-content`。

使用破折号分隔每个单词，为分支命名时要明确标题的目的。例如，假设我们的目标是编写 Sparrow Wallet 软件的使用教程。在这种情况下，用于编写该教程的工作分支可以命名为：`tuto-sparrow-wallet-loic`。输入适当的名称后，点击 "创建分支 "确认分支的创建：

![TUTO](assets/fr/09.webp)

现在点击 "发布分支 "按钮，将新的工作分支保存到 GitHub 上的在线分叉中：

![TUTORIAL](assets/fr/10.webp)

现在，在 GitHub 桌面上，你应该能找到自己的新分支。这意味着你在本地电脑上所做的所有改动都将保存在这个分支上。此外，只要在 GitHub 桌面上选中该分支，在本地计算机上可见的文件就会是该分支（`tuto-sprow-wallet-loic`）的文件，而不是主分支（`dev`）的文件。

![TUTORIAL](assets/fr/11.webp)

每发布一篇新文章，都需要从 `dev` 创建一个新分支。Git 中的分支是项目的并行版本，可以在不影响主分支的情况下进行修改，直到工作准备好合并。

## 2 - 添加教程文件

现在工作分支已经创建，是时候整合新教程了。您有两种选择：使用我的 Python 脚本自动创建必要的文件，或者手动创建每个文件。我们将看看每种选择的步骤。

### 使用我的 Python 脚本

您需要在机器上安装：


- Python 3.8 或更高版本。

要使用脚本，请导航至存放脚本的文件夹。该脚本位于 Plan ₿ Network 数据储存库中，路径为bitcoin-educational-content/scripts/tutorial-related/data-creator`。

进入文件夹后，安装依赖项：

```
pip install -r requirements.txt
```

然后使用命令启动软件：

```
python3 main.py
```

此时将打开一个图形用户界面 (GUI)。第一次使用时，您需要输入所有必要信息，但在以后的使用中，脚本会记住您的个人信息，因此您无需再次输入。

![DATA-CREATOR-PY](assets/fr/37.webp)

首先，在您克隆的仓库中输入`/tutorials`文件夹的本地路径（`.../bitcoin-educational-content/tutorials/`）。您可以手动输入，或者点击 "浏览 "按钮，使用文件资源管理器进行导航。

![DATA-CREATOR-PY](assets/fr/38.webp)

选择编写教程所使用的语言。

![DATA-CREATOR-PY](assets/fr/39.webp)

在 "贡献者的 GitHub ID "字段中，输入您的 GitHub 用户名。

![DATA-CREATOR-PY](assets/fr/40.webp)

在 "PBN 教授 ID "字段中，使用 BIP39 列表中的单词输入您的标识符，该标识符显示在[您的教授简介](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors)中。

![DATA-CREATOR-PY](assets/fr/41.webp)

如果您还没有教授档案，请查看本教程：

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
然后点击 "新教程 "按钮。

![DATA-CREATOR-PY](assets/fr/42.webp)

为您的教程选择一个主类别。然后，根据所选的主类别选择相关的子类别。

![DATA-CREATOR-PY](assets/fr/43.webp)

确定教程的难度级别。

![DATA-CREATOR-PY](assets/fr/44.webp)

为专门为教程创建的目录选择一个名称。该文件夹的名称应反映教程中涉及的软件，使用连字符分隔单词。例如，文件夹可以命名为 "red-wallet"：

![DATA-CREATOR-PY](assets/fr/45.webp)

project_id "是教程中涉及的工具背后的公司或组织的 UUID，可在[项目列表](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects)中找到。例如，关于 Sparrow Wallet 的教程，您可以在文件中找到它的 `project_id` ：bitcoin-educational-content/resources/projects/sparrow/project.yml`。该信息被添加到您教程的 YAML 文件中，是因为 Plan ₿ Network 维护着一个活跃于比特币或相关项目的公司和组织的数据库。通过添加相关的 `project_id`，您可以将您的内容链接到相关实体。

***更新：*** 在新版本的脚本中，您不再需要手动输入 `project_id`。新版本添加了搜索功能，可按名称查找项目并自动检索相应的 `project_id`。在 "项目名称 "字段中输入项目名称的开头进行搜索，然后从下拉菜单中选择所需的公司。项目id "将自动填充到下面的字段中。如有需要，您也可以手动输入。

![DATA-CREATOR-PY](assets/fr/46.webp)

对于标签，请从[计划 ₿ 网络标签列表](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md)中选择 2 或 3 个与教程内容相关的关键字。软件还提供下拉列表关键字搜索功能。

![DATA-CREATOR-PY](assets/fr/47.webp)

输入并验证所有信息后，单击 "创建教程 "确认教程文件的创建。这将在本地生成所选类别中的教程文件夹和所有必要文件。

![DATA-CREATOR-PY](assets/fr/48.webp)

现在您可以跳过 "不使用 Python 脚本 "小节和步骤 3 "填写 YAML 文件"，因为脚本已经为您完成了这些操作。直接进入第 4 步，开始编写教程。

有关此 Python 脚本的更多信息，您也可以查看 [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md)。

### 没有我的 Python 脚本

打开你的文件管理器，导航到 `bitcoin-educational-content` 文件夹，它代表了你的仓库的本地克隆。你通常可以在 `Documents\GitHub\bitcoin-educational-content` 下找到它。

在该目录下，您需要找到合适的子文件夹来放置您的教程。文件夹的组织结构反映了 Plan ₿ Network 网站的不同部分。在我们的例子中，由于我们要添加关于麻雀钱包的教程，我们应该导航到以下路径：bitcoin-educational-content/tutorials/wallet"，对应网站上的 "WALLET "部分：

![TUTO](assets/fr/12.webp)

您需要在 `wallet` 文件夹中新建一个目录，专门用于您的教程。该文件夹的名称应与教程中涉及的软件相呼应，确保用破折号将单词连接起来。在我的例子中，文件夹将命名为 `sparrow-wallet`：

![TUTO](assets/fr/13.webp)

在这个专门用于教程的新子文件夹中，需要添加几个元素：


- 创建一个 "assets "文件夹，用于接收教程所需的所有插图；
- 在 "assets "文件夹中，您需要创建一个子文件夹，根据教程的原始语言代码命名。例如，如果教程是用英语编写的，则该子文件夹必须命名为 `en`。将教程的所有视觉资料（图表、图像、截图等）放在该文件夹中。
- 必须创建一个 `tutorial.yml` 文件，以记录与教程相关的详细信息；
- 要创建一个标记符格式的文件来撰写教程的实际内容。该文件的标题必须与编写的语言代码一致。例如，对于用法语编写的教程，文件名必须为 `fr.md`。

![TUTO](assets/fr/14.webp)

概括地说，要创建的文件层次如下：

```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - 填写 YAML 文件

复制以下模板，填写 `tutorial.yml` 文件：

```
id:
project_id:
tags:
-
-
-
category:
level:
credits:
professor:
# Proofreading metadata
original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributors_id:
-
reward:
```

以下是必填字段的详细信息：


- id**：UUID（通用唯一标识符），用于唯一标识教程。您可以使用[在线工具](https://www.uuidgenerator.net/version4)生成它。唯一的要求是该 UUID 必须是随机的，以避免与平台上的其他 UUID 冲突；
- project_id**：教程中介绍的工具背后的公司或组织的 UUID[来自项目列表](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects)。例如，如果您要创建 Sparrow 钱包软件教程，您可以在以下文件中找到此 `project_id`：bitcoin-educational-content/resources/projects/sparrow/project.yml`。将此信息添加到您的教程的 YAML 文件中，是因为 Plan ₿ Network 维护着一个所有在比特币或相关项目上运营的公司和组织的数据库。通过添加与您的教程相关的实体的`project_id`，您就在这两个元素之间创建了一个链接；
- 标签**：从 Plan ₿ Network 的标签列表中](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md)专门选择 2 或 3 个与教程内容相关的关键词；
- 类别**：根据计划₿ 网络站点的结构，与教程内容相对应的子类别（例如钱包："桌面"、"硬件"、"移动"、"备份"）；
- 级别**：教程的难度级别：
    - 初学者
    - 中级
    - 高级
    - 专家
- 教授**：您在[您的教授简介](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors)中显示的 "贡献者 ID"（BIP39 字样）；
- original_language**：教程的原始语言（例如`fr`、`en`等）；
- 校对**：有关校对过程的信息。填写第一部分，因为校对自己的教程算作第一次验证：
    - language**：校对语言代码（如`fr`、`en`等）。
    - last_contribution_date**：今天的日期。
    - 紧迫性**：留空。
    - contributors_id**：您的 GitHub ID。
    - 奖励**：留空。

有关教授标识符的详细信息，请参阅相应的教程：

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
下面是一个完成的`tutorial.yml`文件示例，用于介绍Blockstream绿色钱包：

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143
project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8
tags:
- wallets
- software
- keys
category: mobile
level: beginner
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributors_id:
- LoicPandul
reward: 0
```

完成对 `tutorial.yml` 文件的修改后，单击 `File > Save` 保存文档：

![TUTO](assets/fr/16.webp)

现在可以关闭代码编辑器了。

## 4 - 填写 Markdown 文件

现在，您可以打开将存放教程的文件，该文件以您的语言代码命名，如 `fr.md`。进入黑曜石，在窗口左侧滚动文件夹树，直到找到教程文件夹和要找的文件：

![TUTO](assets/fr/18.webp)

点击文件打开：

![TUTO](assets/fr/19.webp)

我们首先要填写文件顶部的 "属性 "部分。

![TUTO](assets/fr/20.webp)

手动添加并填写以下代码块：

```
---
name: [Title]
description: [Description]
---
```

![TUTO](assets/fr/21.webp)

填写教程名称和简短说明：

![TUTO](assets/fr/22.webp)

然后，在教程开头添加封面图像的路径。为此，请注意

```
![cover-sparrow](assets/cover.webp)
```

如果需要在教程中添加图片，该语法将非常有用。感叹号表示这是一张图片，在括号之间指定了备选文本 (alt)。括号之间表示图片的路径：

![TUTO](assets/fr/23.webp)

## 5 - 添加徽标和封面

您必须在`assets`文件夹中添加一个名为`logo.webp`的文件，它将作为您文章的缩略图。该图片必须为`.webp`格式，尺寸必须为正方形，以便与用户界面相协调。您可以自由选择教程中涉及的软件的徽标或任何其他相关图片，但必须是无版权的。此外，还请在同一位置添加名为 "cover.webp "的图片。该图片将显示在教程的顶部。确保该图片与徽标一样，尊重使用权并适合教程的上下文：

## 6 - 编写教程并添加视觉效果

继续编写教程，起草内容。当您想加入副标题时，请在文本前加上`##`，应用适当的标记符格式：

![TUTO](assets/fr/24.webp)

assets "文件夹中的语言子文件夹用于存储教程中的图表和视觉效果。请尽可能避免在图片中包含文字，以便国际受众也能阅读您的内容。当然，所介绍的软件会包含文字，但如果您在软件截图上添加图表或其他说明，请不要使用文字，如果证明文字不可或缺，请使用英文。

![TUTO](assets/fr/25.webp)

要为图片命名，只需使用与它们在教程中出现的顺序相对应的数字，格式为两位数（如果教程包含 99 张以上的图片，则为三位数）。例如，将第一张图片命名为 `01.webp`，第二张命名为 `02.webp`，以此类推。

您的图片必须完全是 `.webp` 格式。如有需要，您可以使用 [我的图像转换软件](https://github.com/LoicPandul/ImagesConverter)。

![TUTO](assets/fr/26.webp)

要在文档中插入图表，请使用以下 Markdown 命令，确保指定适当的替代文本以及正确的图片路径：

```
![sparrow](assets/fr/01.webp)
```

开头的感叹号表示这是一张图片。括号之间是备选文本，有助于无障碍访问和搜索引擎优化。最后，括号之间标明了图片的路径。

如果您想创建自己的图表，请务必遵守 Plan ₿ Network 的图形章程，以确保视觉一致性：


- 字体**：使用 [Rubik](https://fonts.google.com/specimen/Rubik)；
- 颜色**：
 - 橙色#FF5C00
 - 黑色：#000000
 - 白色#FFFFFF

**在您的教程中集成的所有视觉效果必须是无版权或尊重源文件许可的**。此外，在 Plan ₿ Network 上发布的所有图表均采用 CC-BY-SA 许可，与文本相同。

**-> 提示：** 在公开共享图片等文件时，一定要删除任何不必要的元数据。元数据可能包含敏感信息，如位置数据、创建日期或有关作者的详细信息。为了保护你的隐私，建议删除这些元数据。为了简化这一过程，您可以使用 [Exif Cleaner](https://exifcleaner.com/) 等专业工具，它可以通过简单的拖放操作来清理文档的元数据。

## 7 - 保存并提交教程

一旦您用自己选择的语言完成了教程的撰写，下一步就是提交**拉动请求**。然后，管理员将通过我们的自动翻译方法和人工审核，为您添加教程中缺失的翻译。

要继续提交拉取请求，请打开 GitHub Desktop 软件。软件会自动检测你在本地分支上对原始版本库所做的改动。在继续之前，请在界面左侧仔细检查这些更改是否与您的预期相符：

![TUTO](assets/fr/28.webp)

为你的提交添加一个标题，然后点击蓝色的 "提交到 [你的分支]"按钮来验证这些更改：

![TUTO](assets/fr/29.webp)

提交是对分支所做更改的保存，并附有描述性信息，可以跟踪项目随时间的演变。它就像是一个中间检查点。

然后点击 `Push origin` 按钮。这将把你的提交发送到你的分叉：

![TUTO](assets/fr/30.webp)

如果您还没有完成您的教程，您可以稍后再回来做新的提交。如果您已完成对该分支的修改，请单击 "预览 Pull Request "按钮：

![TUTO](assets/fr/31.webp)

您可以最后检查一次修改是否正确，然后点击 "创建拉取请求 "按钮：

![TUTO](assets/fr/32.webp)

拉动请求是将您的分支中的更改整合到 Plan ₿ Network 资源库主分支的请求，这样可以在合并之前对更改进行审查和讨论。

您在 GitHub 上的浏览器将自动重定向到您的拉取请求的准备页面：

![TUTO](assets/fr/33.webp)

指明一个标题，简要概括您希望与源代码库合并的更改。添加一个简短的注释来描述这些更改（如果您有一个与创建教程相关的问题编号，记得在注释中注明 "关闭 #{ 问题编号}"），然后点击绿色的 "创建拉取请求 "按钮来确认合并请求：

![TUTO](assets/fr/34.webp)

然后，您的 PR 将出现在主计划₿ 网络存储库的 "拉取请求 "选项卡中。您所要做的就是等待管理员与您联系，确认合并您的贡献或要求任何其他修改。

![TUTO](assets/fr/35.webp)

在您的 PR 与主分支合并后，建议删除您的工作分支 (`tuto-sprow-wallet`)，以保持您的分叉上的历史清白。GitHub 会在您的 PR 页面自动提供该选项：

![TUTO](assets/fr/36.webp)

在 GitHub 桌面软件上，你可以切换回分叉的主分支 (`dev`)。

![TUTO](assets/fr/07.webp)

如果您在提交 PR 后希望更改会费，程序取决于 PR 的当前状态：


- 如果您的 PR 仍未合并，请在同一分支上进行本地修改。修改完成后，使用 "Push origin "按钮为仍未合并的 PR 添加新提交；
- 如果您的 PR 已与主分支合并，则需要重新创建一个新分支，然后提交一份新 PR。在继续之前，请确保本地版本库与 Plan ₿ Network 源版本库同步。

如果您在提交教程时遇到技术问题，请随时在[我们的专用投稿 Telegram 群组](https://t.me/PlanBNetwork_ContentBuilder)上寻求帮助。谢谢！


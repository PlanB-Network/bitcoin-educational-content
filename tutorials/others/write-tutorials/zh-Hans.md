---
name: 贡献 - 教程
description: 如何在PlanB网络上提出一个新的教程？
---
![cover](assets/cover.webp)

PlanB的使命是提供顶级的比特币教育资源，尽可能用多种语言。网站上发布的所有内容都是开源的，并托管在GitHub上，这为任何人参与丰富平台提供了机会。贡献可以采取多种形式：更正和校对现有文本、翻译成其他语言、更新信息或创建我们网站上尚未提供的新教程。

在本教程中，我将解释如何修改PlanB网络的“教程”部分。如果您希望添加新的教程或改进现有的教程，这篇文章就是为您准备的！我们将详细查看如何通过GitHub为PlanB网络做出贡献，同时使用Obsidian这一写作工具。

## 先决条件

要为PlanB网络做出贡献，根据您对GitHub的熟悉程度，您有3种选择：
1. **有经验的用户**：继续使用您通常的方法，并参考本教程以熟悉PlanB仓库的结构、特定要求和工作流程。
2. **准备学习的初学者**：我建议设置您自己的工作环境。按照本教程以及下面列出的我们的其他文章一步一步指导您。
3. **小修改的初学者**：对于需要较少修改的任务，如校对或更正，直接使用GitHub的网页界面，无需设置完整的本地环境。

**跟随我的教程需要的软件：**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- 一个代码编辑器（[VSC](https://code.visualstudio.com/) 或 [Sublime Text](https://www.sublimetext.com/)）
![tutorial](assets/1.webp)
**开始教程之前的先决条件：**
- 拥有一个[GitHub账户](https://github.com/signup)。
- 拥有[PlanB网络源仓库的一个分支](https://github.com/PlanB-Network/bitcoin-educational-content)。
- 在PlanB网络上拥有[一个教授资料](https://planb.network/professors)（仅当您提出完整教程时）。

**如果您需要帮助获取这些先决条件，我的其他教程将指导您：**
- **[理解Git和GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
- **[创建GitHub账户](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
- **[设置您的工作环境](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**
- **[创建教授资料](https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4)**
## 在PlanB网络上写什么类型的内容？
我们主要寻找与比特币或其生态系统相关的工具教程。这些内容可以围绕六个主要类别组织：
- 钱包；
- 节点；
- 挖矿；
- 商户；
- 交易所；
- 隐私。
![tutorial](assets/2.webp)
除了与比特币特别相关的主题外，PlanB还在寻找强调个人主权的主题，如：
- 开源工具；
- 计算机；
- 密码学；
- 能源；
- 数学；
- 经济学；
- DIY；
- 生活黑客...
例如，我们目前有关于Tails、Nostr或GrapheneOS的教程。这些工具与比特币没有直接关系，但它们是在数字世界中追求主权过程中可能会感兴趣的系统。这些内容可以整合到“其他”部分的子分类中。
您可以选择从头开始设计一个教程，或者选择之前在您的网站上发布的教程（前提是您拥有版权），也在PlanB Network上分享，并添加原文链接。

无论您选择哪种方式，请记住在PlanB Network上发布的所有内容都在[CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/)免费许可下。该许可允许任何人复制并可能修改您的内容，前提是必须正确归功于原始来源。

## 如何在PlanB Network上提议一个教程？

一切就绪后，您的本地环境已经通过您自己的PlanB Network分支设置好，您就可以开始添加教程了。

### 创建一个新分支

- 打开您的浏览器，前往您在GitHub上建立的PlanB仓库的分支页面。您的分支URL应该看起来像：`https://github.com/[your-username]/bitcoin-educational-content`:
![教程](assets/3.webp)
- 确保您处于主分支`dev`，然后点击`Sync fork`按钮。如果您的分支不是最新的，GitHub会提议更新您的分支。继续进行这次更新。相反，如果您的分支已经是最新的，GitHub会通知您：
![教程](assets/4.webp)
- 打开GitHub Desktop软件，确保您的分支在窗口的左上角被正确选择：
![教程](assets/5.webp)
- 点击`Fetch origin`按钮。如果您的本地仓库已经是最新的，GitHub Desktop不会建议任何进一步的操作。否则，`Pull origin`选项会出现。点击这个按钮来更新您的本地仓库：![教程](assets/6.webp)
- 确保您处于主分支`dev`：
![教程](assets/7.webp)
- 点击这个分支，然后点击`New Branch`按钮：
![教程](assets/8.webp)
- 确保新分支基于源仓库，即`PlanB-Network/bitcoin-educational-content`。
- 以清晰表明其目的的方式命名您的分支，使用破折号分隔每个单词。例如，假设我们的目标是编写一个关于使用Sparrow Wallet软件的教程。在这种情况下，专门用于编写这个教程的工作分支可以命名为：`tuto-sparrow-wallet-loic`。输入适当的名称后，点击`Create branch`来确认创建分支：
![教程](assets/9.webp)
- 现在点击`Publish branch`按钮，将您的新工作分支保存到GitHub上您的在线分支中：
![教程](assets/10.webp)
现在，在GitHub Desktop上，您应该处于您的新分支。这意味着在您的计算机上本地所做的所有更改将仅记录在这个特定的分支上。同时，只要这个分支在GitHub Desktop上保持选中状态，您机器上本地可见的文件对应于这个分支（`tuto-sparrow-wallet-loic`），而不是主分支（`dev`）。
![教程](assets/11.webp)
对于您希望发布的每篇新文章，您需要从 `dev` 分支创建一个新的分支。在 Git 中，分支是项目的平行版本，它允许您在不影响主分支的情况下进行更改，直到工作准备好合并。

### 添加教程

现在工作分支已经创建，是时候集成您的新教程了。
- 打开您的文件管理器，导航到 `bitcoin-educational-content` 文件夹，该文件夹代表您仓库的本地克隆。通常，您应该在 `Documents\GitHub\bitcoin-educational-content` 下找到它。在这个目录中，需要找到适当的子文件夹来放置您的教程。文件夹的组织反映了 PlanB 网络网站的不同部分。在我们的例子中，由于我们希望添加一个关于 Sparrow Wallet 的教程，因此适合前往以下路径：`bitcoin-educational-content\tutorials\wallet`，该路径对应于网站上的 `WALLET` 部分： ![tutorial](assets/12.webp)
- 在 `wallet` 文件夹内，您需要创建一个专门用于您的教程的新目录。这个文件夹的名称必须唤起教程中涉及的软件，确保用破折号连接单词。例如，文件夹将被命名为 `sparrow-wallet`：
![tutorial](assets/13.webp)
- 在这个专门用于您的教程的新子文件夹中，需要添加几个元素：
	- 创建一个 `assets` 文件夹，旨在接收教程所需的所有插图；
    - 在这个 `assets` 文件夹中，您需要创建 8 个子文件夹，命名为 `fr`、`de`、`en`、`it`、`es`、`ja`、`vi` 和 `pt`，以便根据相应的语言对视觉素材进行分类。您还必须添加一个 `notext` 子文件夹，用于不需要翻译的视觉素材，例如截图；
	- 必须创建一个 `tutorial.yml` 文件来记录与您的教程相关的详细信息；
	- 要创建一个 markdown 格式的文件来编写教程的实际内容。这个文件必须根据写作的语言代码命名。例如，对于用法语编写的教程，文件应该称为 `fr.md`。
![tutorial](assets/14.webp)
- 总结一下，这里是需要创建的文件层次结构：
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (根据正确的类别进行修改)
        └── sparrow-wallet/ (根据教程的名称进行修改)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (根据适当的语言代码进行修改)
```

- 首先，使用您的代码编辑器打开 `tutorial.yml` 文件。
- 用下面指定的信息填写每个字段：
- **builder**: 输入您正在为其创建教程的软件的生产公司的名称；
- **tags**: 确定一系列与您文章主题密切相关的关键词，以便于其搜索和索引；
- **类别**：在PlanB网站上可用的子类别中选择一个适合您教程内容的类别。例如，对于`WALLET`部分的教程，可用选项包括`桌面端`、`硬件`和`移动端`；
- **难度级别**：通过选择以下四个类别中的一个来指示您的教程的难度级别：
    - 初学者（`beginner`），
    - 中级（`intermediary`），
    - 高级（`advanced`），
    - 专家（`expert`）。
- **教授**：提供您在教授个人资料上显示的贡献者ID。更多详情，请参考[相应的教程](https://planb.network/fr/tutorials/others/create-teacher-profile)；
- **链接**（可选）：如果您希望为您正在开发的教程信用一个来源网站，比如您自己的个人网站，这里可以添加相关链接。
![教程](assets/15.webp)
- 完成修改您的`tutorial.yml`文件后，通过点击`文件 > 保存`来保存您的文档：
![教程](assets/16.webp)
- 现在，您可以关闭您的代码编辑器。
- 在`assets`文件夹中，您必须添加一个名为`logo.webp`的文件，它将作为您文章的缩略图。这个图片必须是`.webp`格式，并且必须保持正方形尺寸以与用户界面协调。您可以自由选择教程中涉及的软件的标志或任何其他相关图片，前提是它是免版权的。此外，还要在同一位置添加一个名为`cover.webp`的图片。这张图片将显示在您的教程顶部。确保这张图片，像标志一样，尊重使用权并适合您的教程上下文：
![教程](assets/17.webp)
- 现在，您可以打开将承载您的教程的文件，以您的语言代码命名，例如`fr.md`。转到Obsidian，在窗口的左侧，通过文件夹树滚动到您的教程文件夹和所寻找的文件：
![教程](assets/18.webp)
- 点击文件以打开它：
![教程](assets/19.webp)
- 我们将开始填写文档顶部的`属性`部分。如果您的文件缺少这一部分（如果文档完全为空白），您可以通过从另一个现有教程复制它来复制它：![教程](assets/20.webp)
- 您也可以用这种方式手动添加它，使用您的代码编辑器：
```markdown
---
name: [标题]
description: [描述]
---
```
![教程](assets/21.webp)
- 填写您的教程名称和简短描述：
![教程](assets/22.webp)
- 然后在您的教程开头添加您的封面图片。为此，请输入：
```markdown
![cover-sparrow](assets/cover.webp)
```
- 每当需要在您的教程中添加图片时，这种语法都会很有用。感叹号表示这是一张图片，替代文本（alt）在括号之间指定。图片的路径在括号之间指示：
![教程](assets/23.webp)
- 继续编写您的教程内容。当您想要集成一个副标题时，通过在文本前加上`##`来应用适当的Markdown格式化：
![教程](assets/24.webp)

### 如何在教程中添加图表？
在您的教程中添加图表，可以帮助更清晰地解释复杂的概念或流程。要添加图表，您可以使用以下方法之一：

1. **使用在线图表工具**：有许多在线工具允许您创建图表，然后将其导出为图片格式（如`.webp`）。创建图表后，您可以将图表图片保存到您的`assets`文件夹中，并使用上述相同的Markdown语法将其插入到教程中。

2. **手动绘制并扫描**：如果您更喜欢手绘图表，可以手绘它们，然后扫描或拍照，将图像转换为适合的数字格式。确保图像清晰可读，并遵循上述步骤将其添加到您的教程中。

3. **使用代码生成图表**：对于更技术性的教程，您可能想要直接在Markdown文件中使用代码生成图表。某些Markdown解析器支持内嵌图表代码（如Mermaid图表），这可以直接在Markdown文件中渲染图表。

无论您选择哪种方法，确保图表清晰、相关，并且增加了对教程主题的理解。
`assets`文件夹中的语言子文件夹旨在组织将伴随您的教程的图表和视觉效果。如果您的图片包含文本，请确保为每种相关语言翻译它们，以使您的内容对国际受众可访问。对于无需翻译文本的图表或截图，请直接将它们放在`notext`子文件夹中。![tutorial](assets/25.webp)
为了命名您的图片，只需按照教程中出现的顺序在图片名称中放置数字。例如，将您的第一张图片命名为`1.webp`，第二张为`2.webp`，依此类推。

如果同一图表被翻译成多种语言，请在语言子文件夹中为不同的翻译保持相同的文件名，例如`en/1.webp`、`fr/1.webp`、`pt/1.webp`等。

您可以选择使用不同的图片格式，如`jpeg`、`png`或`webp`。建议选择`webp`格式，以便图片更加轻量。
![tutorial](assets/26.webp)
要在文档中插入图表，请在Markdown中使用以下命令，并确保指定适当的替代文本和图片的正确路径：
```markdown
![sparrow](assets/notext/1.webp)
```
开头的感叹号表示这是一张图片。替代文本，有助于提高可访问性和SEO，放在括号之间。最后，图片的路径在括号之间指明：![tutorial](assets/27.webp)
如果您希望创建自己的图表，请确保遵守PlanB Network的图形规范，以确保视觉上的一致性：
- **字体**：使用 [Rubik](https://fonts.google.com/specimen/Rubik)；
- **颜色**：
	- 橙色：#FF5C00
	- 黑色：#000000
	- 白色：#FFFFFF

**务必确保所有集成到您教程中的视觉内容都是免版税的，或符合源文件的许可证**。此外，PlanB Network上发布的所有图表都在CC-BY-SA许可证下提供，与文本的方式相同。

**-> 提示：** 当公开分享文件，如图片时，重要的是要移除任何多余的元数据。这可能包含敏感信息，如位置数据、创建日期或关于作者的细节。为了保护您的隐私，建议移除这些元数据。为了简化这个操作，您可以使用专门的工具，如 [Exif Cleaner](https://exifcleaner.com/)，它提供了一个简单的拖放操作来清理文档的元数据。

### 如何保存和推送教程？

一旦您用所选的语言完成了教程的编写，下一步是提交一个**Pull Request**。然后管理员会添加您的教程缺失的翻译，感谢我们的自动化翻译方法。

- 要继续进行Pull Request，请打开GitHub Desktop软件。
- 软件应自动检测到您本地相对于原始仓库所做的更改。在继续之前，请仔细检查界面左侧这些更改是否完全符合您的预期：![tutorial](assets/28.webp)
- 为您的提交添加一个标题，然后点击蓝色的`Commit to [your branch]`按钮以验证这些更改：![tutorial](assets/29.webp)
提交是对分支所做更改的保存，伴随着描述性消息，允许随时间跟踪项目的演进。因此，它是一种中间检查点。
- 然后点击 `Push origin` 按钮。这将把你的提交发送到你的分支：![教程](assets/30.webp)- 如果你还没有完成你的教程，你可以稍后回来继续并进行新的提交。
- 如果你已经完成了这个分支的编辑，现在点击 `Preview Pull Request` 按钮：![教程](assets/31.webp)
- 你可以最后一次检查你的修改是否正确，然后点击 `Create pull request` 按钮：
![教程](assets/32.webp)
一个 Pull Request 是一个请求，用于将你分支的更改整合到 PlanB Network 仓库的主分支中，这允许在合并更改之前对其进行审查和讨论。

- 你的浏览器将自动重定向到 GitHub 上你的 Pull Request 准备页面：
![教程](assets/33.webp)
- 提供一个简要总结你希望与源仓库合并的修改的标题。
- 添加一个简短的评论描述这些更改。
- 点击绿色的 `Create pull request` 按钮以确认合并请求：
![教程](assets/34.webp)
你的 PR 然后会在 PlanB Network 主仓库的 `Pull Request` 标签页中可见。你现在要做的就是等待直到管理员联系你以确认合并你的贡献或请求任何额外的修改。
![教程](assets/35.webp)
在你的 PR 与主分支合并后，建议删除你的工作分支（`tuto-sparrow-wallet`）以在你的分支上保持清洁的历史记录。GitHub 将在你的 PR 页面上自动为你提供这个选项：
![教程](assets/36.webp)
在 GitHub Desktop 软件上，你可以切换回你分支的主分支（`dev`）。
![教程](assets/7.webp)
如果你希望在已经提交你的 PR 之后对你的贡献进行修改，接下来的程序取决于你的 PR 的当前状态：
- 如果你的 PR 仍然是开放的并且尚未被合并，就在同一个分支上本地进行修改。一旦修改完成，使用 `Push origin` 按钮将一个新的提交添加到你仍然开放的 PR 中；
- 在你的 PR 已经与主分支合并的情况下，你需要从头开始重新进行这个过程，创建一个新的分支，然后提交一个新的 PR。在进行之前确保你的本地仓库与 PlanB Network 的源仓库同步。

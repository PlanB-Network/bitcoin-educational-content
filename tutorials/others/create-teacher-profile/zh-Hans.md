---
name: PlanB 教授
description: 如何在PlanB网络上添加您的教授个人资料？
---
![封面](assets/cover.webp)

PlanB的使命是提供顶级的比特币教育资源，尽可能多的语言。网站上发布的所有内容都是开源的，并托管在GitHub上，这允许任何人参与丰富平台。贡献可以采取各种形式：更正和校对现有文本、制作培训课程、翻译成其他语言、更新信息或创建我们网站上尚未提供的新教程。

如果您希望在PlanB网络上添加一个新的完整教程或课程，您将需要创建您的教授个人资料。这将允许您为您在网站上产生的内容得到适当的归功。
![教程](assets/1.webp)
如果您之前已经为PlanB网络做出了贡献，您可能已经有了一个贡献者ID。您可以在[此页面](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors)访问的教授文件夹中找到它。如果是这种情况，您可以跳过这个教程并直接开始贡献。
![教程](assets/2.webp)

让我们一起发现如何在本教程中添加新教授！

## 先决条件

**遵循我的教程所需的软件：**
- [GitHub Desktop](https://desktop.github.com/)
- 代码编辑器（[VSC](https://code.visualstudio.com/) 或 [Sublime Text](https://www.sublimetext.com/)）
![教程](assets/3.webp)
**开始教程之前的先决条件：**
- 拥有一个[GitHub账户](https://github.com/signup)。
- 拥有[PlanB网络源代码库](https://github.com/PlanB-Network/bitcoin-educational-content)的一个分支。

**如果您需要帮助获取这些先决条件，我的其他教程将指导您：**
- **[理解Git和GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
- **[创建GitHub账户](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
- **[设置您的工作环境](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**

## 如何创建新的教授个人资料？

- 打开您的浏览器并导航到您的PlanB仓库分支的页面。您的分支的URL应该看起来像：`https://github.com/[username]/bitcoin-educational-content`
![教程](assets/4.webp)
- 确保您处于主分支`dev`，然后点击`Sync fork`按钮。如果您的分支不是最新的，GitHub将提供更新您的分支。继续进行这个同步。

- 如果另一方面，您的分支已经是最新的，GitHub将通知您：
![教程](assets/5.webp)- 打开GitHub Desktop并确保您的分支在窗口的左上角正确选择：
![教程](assets/6.webp)
- 点击`Fetch origin`按钮。

- 如果您的本地仓库已经是最新的，GitHub Desktop不会建议任何进一步的操作。否则，`Pull origin`选项将出现。点击这个按钮来更新您的本地仓库：
![教程](assets/7.webp)
- 确保您处于主分支`dev`：
![教程](assets/8.webp)
- 点击这个分支，然后点击`New Branch`按钮：
![教程](assets/9.webp)
- 确保新分支基于源仓库，即 `PlanB-Network/bitcoin-educational-content`。
- 以清晰表明其目的的方式命名您的分支，使用破折号分隔每个单词。由于这个分支是用于添加教授资料的，一个例子名称可能是：`add-professor-[你的名字]`。输入名称后，点击 `Create branch` 来确认其创建：
![教程](assets/10.webp)
- 现在点击 `Publish branch` 按钮将您的新工作分支保存到 GitHub 上的在线分叉中：
![教程](assets/11.webp)
- 此时，在 GitHub Desktop 上，您应该处于您的新分支上。这意味着在您的电脑上本地做的所有修改将专门记录在这个特定的分支上。同时，只要这个分支在 GitHub Desktop 上保持选中状态，您机器上本地可见的文件对应于这个分支（`add-professor-your-name`），而不是主分支（`dev`）：
![教程](assets/12.webp)
- 要添加您的教授资料，请打开您的文件资源管理器并导航到您的本地仓库，在 `professors` 文件夹中。您将在路径：`\GitHub\bitcoin-educational-content\professors` 下找到它。

- 在这个文件夹中，创建一个以您的名字或假名命名的新文件夹。确保文件夹名称中没有空格。因此，如果您的名字是 "Loic Pandul" 并且没有其他教授使用这个名字，要创建的文件夹将被命名为 `loic-pandul`：
![教程](assets/13.webp)
- 为了简化操作，您可以已经将另一个教授的所有文档复制并粘贴到您自己的文件夹中。然后我们将继续修改这些文档以根据您的资料进行定制：
![教程](assets/14.webp)
- 首先，导航到 `assets` 文件夹。删除您之前复制的教授的个人照片，并用您自己的个人照片替换。这张图片必须是 `.webp` 格式的，并且命名为 `profile`，从而给出完整的文件名 `profile.webp`。请注意，这张图片将被发布在互联网上并且对所有人可见：![教程](assets/15.webp)
- 接下来，用您的代码编辑器（例如 VSC 或 Sublime Text）打开 `professor.yml` 文件。您将看到从现有教授那里复制的文件：
![教程](assets/16.webp)
- 您必须用您自己的信息更新现有信息：
	- **name:** 写下您的名字或假名；
	- **links:** 指出您在社交网络上的账户，如 Twitter 和 Nostr，以及您个人网站的 URL（可选）；
	- **affiliation:** 提及雇佣您的公司的名称（可选）；
	- **tags:** 从以下列表中指定您的专业领域，知道您可以添加自己的主题。但是，请确保标签数量最多不超过4个，以确保良好的 UI：
	    - 隐私，
	    - 密码学，
	    - 比特币，
	    - 挖矿，
	    - 闪电网络，
	    - 经济，
	    - 历史，
	    - 商人，
	    - 安全，
	    - ...
	- **tips:** 提供您的 Lightning 地址以接受捐赠，以便您未来的教程的读者可以发送给您一些 sats（可选）；
	- **company:** 如果您拥有一家公司，指明您公司的名称（可选）。然后您必须用您自己的信息更新现有信息：
![教程](assets/17.webp)- 你还需要修改 `contributor-id`。这个标识符用于在网站上识别你，但不会在GitHub之外公开。你可以自由选择任意两个单词的组合，参考[BIP39的英文2048词列表](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt)。不要忘记在两个选定的单词之间插入破折号。例如，这里，我选择了 `crazy-cactus`：
![教程](assets/18.webp)
- 一旦你完成了对 `professor.yml` 文档的修改，点击 `File > Save` 以保存你的文件。然后你可以退出代码编辑器：
![教程](assets/19.webp)
- 在你的教授文件夹内，你可以删除那些与你无关的语言所写的文档，这些文档最初是从另一个教授那里复制过来的。只保留与你的母语相对应的文件。例如，在我的案例中，我只保留了 `fr.yml` 文件，因为我的语言是法语：![教程](assets/20.webp)
- 双击此文件，用你的代码编辑器打开它。

- 在这个文件中，你有机会在 `bio` 部分下编写你的完整传记，并在 `short_bio` 下编写一个摘要或简洁的标题：
![教程](assets/21.webp)
- 保存你的 `fr.yml` 文档后，你需要为以下八种语言中的每一种创建此文件的副本：
    - 德语 (DE);
    - 英语 (EN);
    - 法语 (FR);
    - 西班牙语 (ES);
    - 意大利语 (IT);
    - 葡萄牙语 (PT);
    - 日语 (JA);
    - 越南语 (VI).

- 继续复制并粘贴你的原始文件，然后将每个文档翻译成相应的语言。如果你精通该语言，你可以手动进行翻译。否则，随意使用自动翻译工具或聊天机器人：
![教程](assets/22.webp)
- 如果你愿意，也可以只保留你的母语传记；然后我们将在你提交Pull Request后处理翻译。

- 你的教授文件夹应该如下所示：
![教程](assets/23.webp)
```plaintext
first-name-last-name/
├── fr.yml
├── it.yml
├── es.yml
├── en.yml
├── de.yml
├── pt.yml
├── ja.yml
├── vi.yml
├── professor.yml
└── assets/
    └── profile.webp
```
- 现在返回到GitHub Desktop。
- 在你的窗口左侧，你应该能看到对文档所做的、特定于你的分支的所有修改。确保这些修改是正确的：
![教程](assets/24.webp)
- 如果修改看起来对你来说是正确的，为你的提交添加一个标题。提交是对分支所做修改的保存，伴随着描述性消息，允许随时间跟踪项目的演变。
- 输入标题后，按下蓝色的 `Commit to [your branch]` 按钮以验证这些修改：
![教程](assets/25.webp)
- 然后点击 `Push origin` 按钮。这将会把你的提交发送到你的fork：
![教程](assets/26.webp)
- 如果你已经完成了这个分支的修改，现在点击 `Preview Pull Request` 按钮：
![教程](assets/27.webp)
- 您可以最后一次检查您的修改是否正确，然后点击 `Create pull request` 按钮：![教程](assets/28.webp)- 您将自动被重定向到GitHub上的Pull Request准备页面。Pull Request是一种请求，用于将您分支上的更改整合到PlanB Network仓库的主分支中，这允许在合并更改之前对其进行审查和讨论：![教程](assets/29.webp)
- 在这个准备页面上，指定一个简短总结您希望与源仓库合并的修改的标题。
- 添加一个简短的评论描述这些更改。
- 完成这些步骤后，点击绿色的 `Create pull request` 按钮以确认合并请求：![教程](assets/30.webp)
- 您的PR随后将在PlanB Network主仓库的 `Pull Request` 标签页中可见。您现在需要做的就是等待管理员联系您，以确认合并您的贡献或请求任何额外的修改：![教程](assets/31.webp)
- 在您的PR与主分支合并后，建议删除您的工作分支（`add-professor-your-name`）以保持您的fork上的历史记录清洁。GitHub将在您的PR页面上自动为您提供这个选项：![教程](assets/32.webp)
- 在GitHub Desktop软件上，您可以切换回您fork的主分支（`dev`）：![教程](assets/8.webp)
- 如果您希望在已经提交PR之后对您的个人资料进行修改，程序取决于您的PR当前的状态：
	- 如果您的PR仍然开放并且尚未合并，当保持在同一分支上时本地进行修改。一旦修改完成，使用 `Push origin` 按钮将一个新的提交添加到您仍然开放的PR中；
	- 在您的PR已经与主分支合并的情况下，您将需要通过创建一个新的分支，然后提交一个新的PR来重新开始这个过程。在进行之前，请确保您的本地仓库与PlanB Network源仓库同步。

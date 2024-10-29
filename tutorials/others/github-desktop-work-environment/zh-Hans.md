---
name: GitHub Desktop
description: 如何设置您的本地工作环境？
---
![github](assets/cover.webp)

PlanB 的使命是以尽可能多的语言提供关于比特币的顶级教育资源。网站上发布的所有内容都是开源的，并托管在 GitHub 上，这允许任何人参与丰富平台。贡献可以采取各种形式：更正和校对现有文本、翻译成其他语言、更新信息或创建我们网站上尚未提供的新教程。

如果您希望为 PlanB 网络做出贡献，您将需要使用 GitHub 提出更改。为此，您有两个选项：
- **直接通过 GitHub 的网页界面贡献**：这是最简单的方法。如果您是初学者或者您计划只做少量的小贡献，这个选项可能是最适合您的；
- **使用 Git 本地贡献**：如果您计划对 PlanB 网络进行定期或重大贡献，这种方法更合适。虽然一开始在您的电脑上设置本地 Git 环境可能看起来复杂，但从长远来看，这种方法更高效。它允许更灵活地管理更改。如果您对此感到新奇，不用担心，**我们在本教程中解释了设置环境的整个过程**（承诺，您不需要输入任何命令行^^）。

如果您不知道 GitHub 是什么，或者如果您想了解更多与 Git 和 GitHub 相关的技术术语，我建议您[阅读我们的入门文章以熟悉这些概念](https://planb.network/tutorials/others/basics-of-github)。

- 首先，您显然需要一个 GitHub 账户。如果您已经有一个，您可以登录，否则，您可以使用[我们的教程创建一个新账户](https://planb.network/tutorials/others/create-github-account)。

## 第 1 步：安装 GitHub Desktop

- 访问 https://desktop.github.com/ 下载 GitHub Desktop 软件。这款软件允许您轻松地与 GitHub 交互，无需使用终端：
![github-desktop](assets/1.webp)
- 当您首次启动软件时，将被要求连接您的 GitHub 账户。为此，请点击 `Sign in to GitHub.com`：
![github-desktop](assets/2.webp)
- 您的浏览器将打开一个认证页面。输入创建账户时选择的电子邮件地址和密码，然后点击 `Sign in` 按钮：
![github-desktop](assets/3.webp)
- 点击 `Authorize desktop` 确认您的账户与软件之间的连接：
![github-desktop](assets/4.webp)
- 您将自动重定向到 GitHub Desktop 软件。点击 `Finish`： ![github-desktop](assets/5.webp)
- 如果您刚刚创建了您的 GitHub 账户，您将被重定向到一个页面，表明您尚未创建任何仓库。此时，暂时搁置 GitHub Desktop 软件；我们稍后会回到它： ![github-desktop](assets/6.webp)

## 第 2 步：安装 Obsidian

接下来我们来安装写作软件。这里，您有几个选项。您将需要支持编辑 Markdown 文件的软件，因为 PlanB 网络在其仓库中使用这种格式进行文本文件的编辑。
有许多软件专门用于编辑Markdown文件，例如为写作特别设计的Typora。虽然这不是理想选择，但也可以选择代码编辑器，如Visual Studio Code (VSC)或Sublime Text。然而，作为一名作家，我更喜欢使用Obsidian软件。让我们一起看看如何安装并开始使用它。
- 访问https://obsidian.md/download 并下载软件：![github-desktop](assets/7.webp)
- 安装Obsidian，启动软件，选择你的语言，然后点击`Quick Start`：![github-desktop](assets/8.webp)
- 你将进入Obsidian软件。目前，你没有打开任何文件：![github-desktop](assets/9.webp)

## 第3步：Fork PlanB Network仓库

- 访问以下地址的PlanB Network数据仓库：[https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content)：![github-desktop](assets/10.webp)
- 在此页面，点击窗口右上角的`Fork`按钮：![github-desktop](assets/11.webp)
- 在创建菜单中，你可以保留默认设置。确保勾选了`Copy the dev branch only`框，然后点击`Create fork`按钮：![github-desktop](assets/12.webp)
- 然后你将进入你自己的PlanB Network仓库的fork版本：![github-desktop](assets/13.webp)
这个fork构成了一个与原始仓库分离的独立仓库，尽管它目前包含相同的数据。你现在将在这个新仓库上工作。

我们以某种方式复制了PlanB Network源仓库。你的fork（副本）和原始仓库现在将独立于彼此发展。在原始仓库上，其他贡献者可能会添加新数据，而你，在你的fork上，将进行你自己的修改。
为了保持这两个仓库之间的一致性，将需要定期同步它们，以便它们检索相同的信息。要将你的更改发送到源仓库，你将使用所谓的**Pull Request**。而要将源仓库的更改集成到你的fork中，你将使用GitHub网页界面上可用的**Sync fork**命令。
![github-desktop](assets/14.webp)

## 第4步：克隆fork

- 返回到GitHub Desktop软件。到目前为止，你的fork应该出现在`Your repositories`部分。如果你立即看不到它，使用双箭头按钮刷新列表。当你的fork出现时，点击它进行选择：
![github-desktop](assets/15.webp)
- 然后点击蓝色按钮：`Clone [username]/bitcoin-educational-content`：
![github-desktop](assets/16.webp)
- 保持默认路径。确认后，点击蓝色`Clone`按钮：
![github-desktop](assets/17.webp)
- 等待GitHub Desktop将你的fork克隆到本地：
![github-desktop](assets/18.webp)
- 克隆仓库后，软件为您提供两个选项。您必须选择第一个：`为父项目做贡献`。这个选择将允许您将未来的工作作为对父项目（`PlanB-Network/bitcoin-educational-content`）的贡献展示，而不仅仅是您个人分支（`[username]/bitcoin-educational-content`）的修改。选择该选项后，点击`继续`：![github-desktop](assets/19.webp)
- 您的GitHub桌面现在已正确配置。现在，您可以在后台保持软件开启，以跟踪我们将进行的修改。
![github-desktop](assets/20.webp)
我们在这个阶段实现的是创建您的仓库的本地副本，该仓库托管在GitHub上。提醒一下，这个仓库是PlanB网络源仓库的一个分支。您将能够对这个本地副本进行修改，例如添加教程、翻译或更正。一旦这些修改完成，您将使用**推送源**命令将您的本地修改发送到托管在GitHub上的您的分支。

您还可以从分支中检索修改，例如，在与PlanB网络仓库同步期间。为此，您将使用**获取源**命令下载修改到您的本地副本（您的克隆），然后使用**拉取源**命令将它们与您的工作合并。这允许您在有效地贡献的同时，保持与项目的最新发展同步。

![github-desktop](assets/21.webp)
## 第5步：创建一个新的Obsidian保险库

- 打开Obsidian软件并点击窗口左下角的小保险库图标：
![github-desktop](assets/22.webp)
- 点击`打开`按钮以打开一个现有文件夹作为保险库：![github-desktop](assets/23.webp)
- 您的文件资源管理器将打开。您需要定位并选择标题为`GitHub`的文件夹，该文件夹应该在您的`文档`目录中。这个路径对应于您在第4步中建立的路径。选择文件夹后，确认其选择。然后，您的保险库在Obsidian软件的新页面上创建：

![github-desktop](assets/24.webp)
-> **注意**，在Obsidian中创建新保险库时，重要的是不要选择`bitcoin-educational-content`文件夹。相反，选择父文件夹`GitHub`。如果您选择了`bitcoin-educational-content`文件夹，配置文件夹`.obsidian`，包含您的本地Obsidian设置，将自动集成到仓库中。我们希望避免这种情况，因为不需要将您的Obsidian配置转移到PlanB网络仓库。另一种方法是将`.obsidian`文件夹添加到`.gitignore`文件中，但这种方法也会修改源仓库的`.gitignore`文件，这是不可取的。

- 在窗口的左侧，您可以看到已经在本地克隆的不同GitHub仓库的文件树。
- 通过点击文件夹名称旁边的箭头，您可以展开它们以访问仓库的子文件夹及其文档：
![github-desktop](assets/25.webp)
- 不要忘记将Obsidian设置为暗模式：“光吸引虫子” ;)

## 第6步：安装代码编辑器
您的大部分修改将针对Markdown格式（`.md`）的文件。要编辑这些文档，您可以使用我们之前讨论过的软件Obsidian。然而，PlanB网络使用其他文件格式，您将需要修改其中的一些文件。
例如，在创建新教程时，您需要创建一个YAML（`.yml`）文件来输入您的教程标签、标题和教师ID。Obsidian不提供修改这类文件的可能性，因此您将需要一个代码编辑器。

对此，您有几个选项。尽管可以使用计算机的标准记事本进行这些修改，但这种解决方案对于整洁的工作来说并不理想。我推荐选择专为此目的设计的软件，如[VS Code](https://code.visualstudio.com/download)或[Sublime Text](https://www.sublimetext.com/download)。Sublime Text特别轻便，将非常适合我们的需求。
- 安装这些软件程序中的一个，并为您未来的修改保留它。![github-desktop](assets/26.webp)
恭喜您！您的工作环境现在已经设置好，可以为PlanB网络做出贡献了。您现在可以探索[我们的其他特定教程](https://planb.network/tutorials/others)来了解每种类型的贡献（翻译、校对、写作...）。

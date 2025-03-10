---
name: 贡献 - GitHub 桌面教程（中级）
description: 使用 GitHub 桌面在 Plan ₿ 网络上提出教程的完整指南
---
![cover](assets/cover.webp)

在学习本教程添加新教程之前，您必须完成一些初步步骤。如果您还没有这样做，我请您先查阅本入门教程，然后再回到这里：

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

你已经有了：


- 选择教程主题；
- 通过 [Telegram 群组](https://t.me/PlanBNetwork_ContentBuilder) 或 paolo@planb.network 与 Plan ₿ Network 团队联系；
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

打开浏览器，进入 Plan ₿ Network 代码库的分叉页面。这是您在 GitHub 上建立的分叉。你的分叉的 URL 应该是这样的https://github.com/[您的用户名]/bitcoin-educational-content`：

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

现在，在 GitHub 桌面上，你应该能找到自己的新分支。这意味着你在本地电脑上所做的所有改动都将保存在这个分支上。此外，只要在 GitHub 桌面上选中该分支，在本地计算机上可见的文件就是该分支 (`tuto-sprow-wallet-loic`)的文件，而不是主分支 (`dev`)的文件。

![TUTORIAL](assets/fr/11.webp)

每发布一篇新文章，都需要从 `dev` 创建一个新分支。Git 中的分支是项目的并行版本，可以在不影响主分支的情况下进行修改，直到工作准备好合并。

## 2 - 添加教程文件

现在工作分支已经创建，是时候整合新教程了。您有两种选择：使用我的 Python 脚本自动创建必要的文件，或者手动创建每个文件。我们将看看每种选择的步骤。

### 使用我的 Python 脚本

您需要在您的计算机上安装：
- Python 3.8 或更高版本。

要使用此脚本，请转到其存储的文件夹。该脚本位于 Plan ₿ Network 的数据存储库中，路径如下：`bitcoin-educational-content/scripts/tutorial-related/data-creator`。

进入文件夹后，安装依赖项：

```bash
pip install -r requirements.txt
```

然后使用以下命令启动软件：

```bash
python3 main.py
```

图形用户界面（GUI）将会打开。首次使用时，您需要输入所有必要的信息，但在后续使用中，脚本会记住您的个人信息，因此您无需再次输入。

![DATA-CREATOR-PY](assets/fr/37.webp)

首先，输入您的克隆存储库中 `/tutorials` 文件夹的本地路径（`.../bitcoin-educational-content/tutorials/`）。您可以手动输入，也可以点击 "Browse" 按钮，通过文件管理器浏览选择。

![DATA-CREATOR-PY](assets/fr/38.webp)

选择您将使用的教程编写语言。

![DATA-CREATOR-PY](assets/fr/39.webp)

在 "Contributor's GitHub ID" 字段中，输入您的 GitHub 用户名。

![DATA-CREATOR-PY](assets/fr/40.webp)

在 "PBN professor's ID" 字段中，使用 BIP39 词表中的单词输入您的标识符，格式应与 [您的教授资料](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) 中显示的内容一致。

![DATA-CREATOR-PY](assets/fr/41.webp)

如果您还没有教授资料，请参考以下教程：

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

然后点击 "New Tutorial" 按钮。

![DATA-CREATOR-PY](assets/fr/42.webp)

选择教程的主要类别。然后，根据所选主要类别，选择适当的子类别。

![DATA-CREATOR-PY](assets/fr/43.webp)

确定教程的难度级别。

![DATA-CREATOR-PY](assets/fr/44.webp)

选择专门为您的教程创建的目录名称。此文件夹的名称应反映教程所涉及的软件，并使用连字符连接单词。例如，该文件夹可以命名为 `red-wallet`：

![DATA-CREATOR-PY](assets/fr/45.webp)

`project_id` 是教程涉及的软件背后的公司或组织的 UUID，可在 [项目列表](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects) 中找到。例如，对于 Sparrow Wallet 的教程，您可以在以下文件中找到 `project_id`：`bitcoin-educational-content/resources/projects/sparrow/project.yml`。此信息被添加到您的教程 YAML 文件中，因为 Plan ₿ Network 维护着一个数据库，其中包含活跃在比特币领域的公司及相关项目。通过在您的教程中添加 `project_id`，您可以将您的内容与相关实体建立联系。

***更新:*** 在最新版本的脚本中，您不再需要手动输入 `project_id`。已添加搜索功能，可根据项目名称查找项目并自动获取相应的 `project_id`。在 "Project Name" 字段中输入项目名称的开头以进行搜索，然后从下拉菜单中选择所需的公司。`project_id` 将自动填充到下方的字段中。如果需要，您仍然可以手动输入。

![DATA-CREATOR-PY](assets/fr/46.webp)

对于标签（tags），请选择 2 至 3 个与教程内容相关的关键字，并且必须从 [Plan ₿ Network 标签列表](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) 中选择。该软件还提供了关键字搜索功能，并带有下拉选择列表。

![DATA-CREATOR-PY](assets/fr/47.webp)

在输入和验证所有信息后，点击 "Create Tutorial" 以确认创建教程文件。这将在您的本地系统上生成教程文件夹以及所有必要的文件，并存放在所选类别下。

![DATA-CREATOR-PY](assets/fr/48.webp)

您现在可以跳过 "不使用 Python 脚本" 部分，以及第 3 步 "填写 YAML 文件"，因为脚本已经自动完成了这些步骤。请直接进入第 4 步，并开始撰写您的教程。

有关此 Python 脚本的更多信息，您还可以参考 [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md)。

### 不使用我的 Python 脚本

打开您的文件管理器，并导航到 `bitcoin-educational-content` 文件夹，该文件夹是您的本地克隆存储库。通常，它应该位于 `Documents\GitHub\bitcoin-educational-content` 目录下。

在此目录中，您需要找到合适的子文件夹来放置您的教程。文件夹结构反映了 Plan ₿ Network 网站的不同部分。在本示例中，由于我们希望添加有关 Sparrow Wallet 的教程，因此需要导航到以下路径：`bitcoin-educational-content\tutorials\wallet`，它对应于网站上的 `WALLET` 部分：

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

```plaintext
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

```yaml
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
```

last_contribution_date: 紧迫性：

贡献者_id：

-

奖励：

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
- 教授**：您在[您的教授简介](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) 中显示的 "贡献者 ID"（BIP39 字样）；
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

```yaml
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
urgency:
contributors_id:
- LoicPandul
reward:
Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![TUTO](assets/fr/16.webp)
You can now close your code editor.
## 4 - Fill in the Markdown File
Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree until you find the folder of your tutorial and the file you are looking for:
![TUTO](assets/fr/18.webp)
Click on the file to open it:
![TUTO](assets/fr/19.webp)
We will start by filling in the `Properties` section at the top of the document.
![TUTO](assets/fr/20.webp)
Manually add and fill in the following code block:
```

---
name: [标题]
description: [说明]
---
```
![TUTO](assets/fr/21.webp)
Fill in the name of your tutorial and a short description of it:
![TUTO](assets/fr/22.webp)
Then, add the path of the cover image at the beginning of your tutorial. To do this, note:
```

![cover-sparrow](assets/cover.webp)

```
This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![TUTO](assets/fr/23.webp)
## 5 - Add the Logo and Cover
Within the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You are free to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same place. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
## 6 - Writing the Tutorial and Adding Visuals
Continue writing your tutorial by drafting your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![TUTO](assets/fr/24.webp)
The language subfolder in the `assets` folder is used to store diagrams and visuals that will accompany your tutorial. As much as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software being presented will contain text, but if you add diagrams or additional indications on software screenshots, do so without text or, if it proves indispensable, use English.
![TUTO](assets/fr/25.webp)
To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted with two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.
Your images must be in `.webp` format exclusively. If needed, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).
![TUTO](assets/fr/26.webp)
To insert a diagram into your document, use the following Markdown command, making sure to specify the appropriate alternative text as well as the correct path of the image:
```

![sparrow](assets/fr/01.webp)

```
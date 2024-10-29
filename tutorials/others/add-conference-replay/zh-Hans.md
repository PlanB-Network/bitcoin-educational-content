---
name: 添加会议回放
description: 如何在PlanB网络上添加会议回放？
---
![conference](assets/cover.webp)

PlanB的使命是以尽可能多的语言提供关于比特币的顶级教育资源。网站上发布的所有内容都是开源的，并托管在GitHub上，允许任何人为平台的丰富做出贡献。

你想在PlanB网络站点上添加你的比特币会议回放，并为这个事件增加曝光度，但不知道如何操作？这个教程是为你准备的！

然而，如果你想添加将来会举行的会议，我建议你[阅读这个其他教程](https://planb.network/tutorials/others/add-event)，我们在其中解释了如何向网站添加新事件。
![conference](assets/01.webp)
- 首先，你需要在GitHub上有一个账户。如果你不知道如何创建账户，我们制作了[一个详细的教程来指导你](https://planb.network/tutorials/others/create-github-account)。
- 前往[PlanB专门用于数据的GitHub仓库](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference)的`resources/conference/`部分：
![conference](assets/02.webp)
- 点击右上角的`Add file`按钮，然后点击`Create new file`：
![conference](assets/03.webp)
- 如果你之前从未为PlanB网络的内容做出过贡献，你将需要创建原始仓库的分支。分支一个仓库意味着在你自己的GitHub账户上创建该仓库的副本，这允许你在不影响原始仓库的情况下进行项目工作。点击`Fork this repository`按钮：
![conference](assets/04.webp)
- 然后你将进入GitHub编辑页面：
![conference](assets/05.webp)
- 为你的会议创建一个文件夹。为此，在`Name your file...`框中，用破折号代替空格写下你的会议名称。例如，如果你的会议叫做"Paris Bitcoin Conference"，你应该记为`paris-bitcoin-conference`。还要添加你的会议年份，例如：`paris-bitcoin-conference-2024`：
![conference](assets/06.webp)
- 要验证文件夹的创建，只需在同一个框中的名称后面加上斜杠，例如：`paris-bitcoin-conference-2024/`。添加斜杠会自动创建一个文件夹而不是文件：
![conference](assets/07.webp)
- 在这个文件夹中，你将创建一个名为`conference.yml`的第一个YAML文件：
![conference](assets/08.webp)
使用此模板填写与你的会议相关的信息：
```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

例如，你的YAML文件可能看起来像这样：

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - International
  - All Public
```

![conference](assets/09.webp)
如果您的组织尚未拥有"*builder*"标识符，您可以通过[遵循此教程](https://planb.network/tutorials/others/add-builder)添加。
- 完成对该文件的更改后，通过点击`Commit changes...`按钮保存更改：
![conference](assets/10.webp)
- 为您的更改添加标题以及简短描述：
![conference](assets/11.webp)
- 点击绿色的`Propose changes`按钮：
![conference](assets/12.webp)
- 接下来您将进入一个页面，总结您所有的更改：
![conference](assets/13.webp)
- 点击右上角的GitHub个人资料图片，然后点击`Your Repositories`：
![conference](assets/14.webp)
- 选择您fork的PlanB Network仓库：
![conference](assets/15.webp)
- 您应该会在窗口顶部看到一个带有新分支的通知。它可能被称为`patch-1`。点击它：
![conference](assets/16.webp)
- 您现在位于您的工作分支上：
![conference](assets/17.webp)
- 返回到`resources/conference/`文件夹，并选择您在之前的提交中刚创建的会议文件夹：
![conference](assets/18.webp)
- 在您的会议文件夹中，点击`Add file`按钮，然后点击`Create new file`：
![conference](assets/19.webp)
- 将这个新文件夹命名为`assets`，并通过在末尾添加斜杠`/`确认其创建：
![conference](assets/20.webp)
- 在这个`assets`文件夹中，创建一个名为`.gitkeep`的文件：
![conference](assets/21.webp)
- 点击`Commit changes...`按钮：
![conference](assets/22.webp)
- 保留默认的提交标题，并确保选中了`Commit directly to the patch-1 branch`框，然后点击`Commit changes`：
![conference](assets/23.webp)
- 返回到`assets`文件夹：
![conference](assets/24.webp)
- 点击`Add file`按钮，然后点击`Upload files`：
![conference](assets/25.webp)
- 一个新页面将打开。拖放一个代表您的会议并将在PlanB Network站点上显示的图片：![conference](assets/26.webp)
- 它可以是一个logo、一个缩略图，甚至是一个海报：
![conference](assets/27.webp)
- 图片上传后，检查`Commit directly to the patch-1 branch`框是否被选中，然后点击`Commit changes`：
![conference](assets/28.webp)
- 注意，您的图片必须命名为`thumbnail`并且必须是`.webp`格式。因此，完整的文件名应该是：`thumbnail.webp`：
![conference](assets/29.webp)
- 返回到您的`assets`文件夹并点击`.gitkeep`中间文件：
![conference](assets/30.webp)
- 在文件上，点击右上角的3个小点然后点击`Delete file`：
![conference](assets/31.webp)
- 验证您仍在同一个工作分支上，然后点击`Commit changes`按钮：
![conference](assets/32.webp)
- 为您的提交添加标题和描述，然后点击`Commit changes`：
![conference](assets/33.webp)
- 返回到您的会议文件夹：![conference](assets/34.webp)
- 点击 `Add file` 按钮，然后点击 `Create new file`：
![conference](assets/35.webp)
- 通过用您的母语指示符命名来创建一个新的markdown (.md) 文件。这个文件将用于您的会议重播。例如，如果我想用英语编写会议描述，我会将这个文件命名为 en.md：
![conference](assets/36.webp)
- 使用您可以适应您的会议配置的这个模板填写这个markdown文件：

```markdown
---
name: 2024年巴黎比特币会议
description: 法国最大的比特币会议，每年有超过8,000名参与者！
--- 

# 主舞台

## 周五上午

![video](https://youtu.be/XXXXXXXXXXXX)

## 周五下午

![video](https://youtu.be/XXXXXXXXXXXX)

## 周六上午

![video](https://youtu.be/XXXXXXXXXXXX)

## 周六下午

![video](https://youtu.be/XXXXXXXXXXXX)

# 工作坊室

## 比特币挖矿的未来：挑战与创新

![video](https://youtu.be/XXXXXXXXXXXX)

演讲者: 中本聪, 中本聪

## 在比特币上还能保持隐私吗？

![video](https://youtu.be/XXXXXXXXXXXX)

演讲者: 中本聪

## 比特币核心：深入代码库

![video](https://youtu.be/XXXXXXXXXXXX)

演讲者: 中本聪, 中本聪, 中本聪, 中本聪

## 使用Miniscript构建和保护比特币钱包

![video](https://youtu.be/XXXXXXXXXXXX)

演讲者: 中本聪
```

![conference](assets/37.webp)
- 在您的文档开头的 "front matter" 中，用您的会议名称和重播的年份填写 `name:` 字段。在 `description:` 字段中，用文件的语言写下您的活动的简短描述。例如，对于一个名为 `en.md` 的文件，描述应该用英语。PlanB Network团队将使用他们的模型翻译您的描述。
- 一级标题，由 `#` 标记，用于按场景组织会议。例如，`# 主舞台` 用于主舞台，`# 工作坊室` 用于专门的工作坊舞台。

- 二级标题，由双 `##` 标记，用于分隔不同的重播视频。如果会议在半天内连续拍摄，请例如指出 `## 周五上午`。如果会议被单独拍摄和广播，请直接用二级标题命名会议。

- 在每个二级标题下，插入对应重播视频的链接。语法应为：`![video](https://youtu.be/XXXXXXXXXXXX)`，将 `XXXXXXXXXXXX` 替换为实际的视频链接。

- 如果格式允许（单独的会议），您可以添加演讲者的名字。为此，在视频链接下添加 `演讲者:` 字段，后跟演讲者的名字或假名。如果有多个演讲者，像这样用逗号分隔每个名字：例如：`演讲者: 中本聪, 中本聪, 中本聪, 中本聪`。

---

- 完成对这个文件的修改后，通过点击 `Commit changes...` 按钮保存它们：
![conference](assets/38.webp)
- 为您的修改添加一个标题，以及一个简短的描述：
![conference](assets/39.webp)
- 点击 `Commit changes` 按钮：![conference](assets/40.webp)
- 此时您的会议文件夹应该看起来像这样：
![conference](assets/41.webp)
- 如果一切符合您的满意，返回到您分支的根目录：
![conference](assets/42.webp)
- 您应该会看到一条消息，指示您的分支已经发生了修改。点击 `Compare & pull request` 按钮：
![conference](assets/43.webp)
- 为您的PR添加一个清晰的标题和描述：
![conference](assets/44.webp)
- 点击 `Create pull request` 按钮：
![conference](assets/45.webp)
恭喜！您的PR已经成功创建。管理员现在将对其进行审查，如果一切顺利，将其合并到PlanB Network的主仓库中。几天后，您应该会在网站上看到您会议的回放。

请确保跟踪您PR的进度。管理员可能会留下评论，要求提供额外信息。只要您的PR未被验证，您就可以在PlanB Network的GitHub仓库下的 `Pull requests` 标签下查看它：
![conference](assets/46.webp)

非常感谢您的宝贵贡献！:)

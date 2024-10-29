---
name: 在PlanB网络上添加一个事件
description: 我如何建议在PlanB网络上添加一个新事件？
---
![event](assets/cover.webp)

PlanB的使命是以尽可能多的语言提供关于比特币的顶级教育资源。网站上发布的所有内容都是开源的，并托管在GitHub上，为任何人提供了为平台丰富内容的机会。

如果你想在PlanB Network网站上添加一个比特币会议，以增加你活动的可见性，但不知道如何操作？这个教程就是为你准备的！
![event](assets/01.webp)
- 首先，你需要在GitHub上拥有一个账户。如果你不知道如何创建账户，我们制作了[一个详细的教程来指导你](https://planb.network/tutorials/others/create-github-account)。
- 前往[PlanB专门用于数据的GitHub仓库](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference)的`resources/conference/`部分：
![event](assets/02.webp)
- 点击右上角的`Add file`按钮，然后点击`Create new file`：
![event](assets/03.webp)
- 如果你之前从未为PlanB Network的内容做出过贡献，你将需要创建原始仓库的分支。分支一个仓库意味着在你自己的GitHub账户上创建该仓库的一个副本，允许你在不影响原始仓库的情况下进行项目工作。点击`Fork this repository`按钮：
![event](assets/04.webp)
- 然后你将进入GitHub编辑页面：
![event](assets/05.webp)
- 为你的会议创建一个文件夹。为此，在`Name your file...`框中，用破折号代替空格写下你的会议名称。例如，如果你的会议叫做"Paris Bitcoin Conference"，你应该记为`paris-bitcoin-conference`。还要添加你会议的年份，例如：`paris-bitcoin-conference-2024`：
![event](assets/06.webp)
- 要验证文件夹的创建，只需在同一个框中的名称后面加上斜杠，例如：`paris-bitcoin-conference-2024/`。添加斜杠会自动创建一个文件夹而不是一个文件：
![event](assets/07.webp)
- 在这个文件夹中，你将创建一个名为`events.yml`的第一个YAML文件：
![event](assets/08.webp)
- 使用此模板填写有关你会议的信息：

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website:
    replay_url:    
    live_url :
  tags: 
    - 
```

例如，你的YAML文件可能看起来像这样：

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: 巴黎, 法国
  address_line_2: 
  address_line_3: 
  name: 2024年巴黎比特币会议
  builder: 巴黎比特币会议
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
描述：法国最大的比特币会议，每年有超过8,000名参与者！
语言：
    - fr
    - en
    - es
    - it
链接：
    网站：https://paris.bitcoin.fr/conference
    重播网址：
    直播网址：
标签：
    - 比特币爱好者
    - 通用
    - 国际
```
![活动](assets/09.webp)
如果您的组织还没有一个“*构建者*”标识符，您可以[按照这个教程添加](https://planb.network/tutorials/others/add-builder)。

- 完成对此文件的修改后，点击 `Commit changes...` 按钮保存更改：
![活动](assets/10.webp)
- 为您的更改添加一个标题，以及一个简短的描述：
![活动](assets/11.webp)
- 点击绿色的 `Propose changes` 按钮：
![活动](assets/12.webp)
- 然后您将进入一个页面，总结您所有的更改：
![活动](assets/13.webp)
- 点击右上角的GitHub个人资料图片，然后点击 `Your Repositories`：
![活动](assets/14.webp)
- 选择您fork的PlanB Network仓库：
![活动](assets/15.webp)
- 您应该会在窗口顶部看到一个带有您新分支的通知。它可能被称为 `patch-1`。点击它：
![活动](assets/16.webp)
- 您现在处于您的工作分支：
![活动](assets/17.webp)
- 返回到 `resources/conference/` 文件夹，并选择您在上一个提交中刚创建的会议文件夹：
![活动](assets/18.webp)
- 在您的会议文件夹中，点击 `Add file` 按钮，然后点击 `Create new file`：
![活动](assets/19.webp)
- 将这个新文件夹命名为 `assets` 并通过在末尾添加斜杠 `/` 来确认其创建：
![活动](assets/20.webp)
- 在这个 `assets` 文件夹中，创建一个名为 `.gitkeep` 的文件：
![活动](assets/21.webp)
- 点击 `Commit changes...` 按钮：
![活动](assets/22.webp)
- 保留默认的提交标题，并确保选中了 `Commit directly to the patch-1 branch` 框，然后点击 `Commit changes`：
![活动](assets/23.webp)
- 返回到 `assets` 文件夹：
![活动](assets/24.webp)
- 点击 `Add file` 按钮，然后点击 `Upload files`： ![活动](assets/25.webp)
- 一个新页面将打开。拖放一个代表您的会议并将在PlanB Network站点上显示的图片：
![活动](assets/26.webp)
- 它可以是logo、缩略图，甚至是海报：
![活动](assets/27.webp)
- 图片上传后，检查是否勾选了 `Commit directly to the patch-1 branch` 框，然后点击 `Commit changes`：
![活动](assets/28.webp)
- 注意，您的图片必须命名为 `thumbnail` 并且必须是 `.webp` 格式。因此，完整的文件名应该是：`thumbnail.webp`：
![活动](assets/29.webp)
- 返回到您的 `assets` 文件夹并点击中间文件 `.gitkeep`：
![活动](assets/30.webp)
- 在文件上，点击右上角的3个小点，然后点击`删除文件`：![event](assets/31.webp)
- 确认您仍在同一个工作分支上，然后点击`提交更改`按钮：
![event](assets/32.webp)
- 为您的提交添加一个标题和描述，然后点击`提交更改`：
![event](assets/33.webp)
- 返回到您的仓库根目录：
![event](assets/34.webp)
- 您应该会看到一条消息，指示您的分支发生了变化。点击`比较 & 拉取请求`按钮：
![event](assets/35.webp)
- 为您的PR添加一个清晰的标题和描述：
![event](assets/36.webp)
- 点击`创建拉取请求`按钮：
![event](assets/37.webp)
恭喜！您的PR已成功创建。现在，管理员将会检查它，如果一切顺利，将其合并到PlanB Network的主仓库中。几天后，您应该会在网站上看到您的事件。

确保跟踪您PR的进展。管理员可能会留下评论，要求提供额外信息。只要您的PR未被验证，您就可以在PlanB Network GitHub仓库的`拉取请求`标签中查看它：
![event](assets/38.webp)
非常感谢您的宝贵贡献！:)

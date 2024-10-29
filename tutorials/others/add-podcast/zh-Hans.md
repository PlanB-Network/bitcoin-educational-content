---
name: 将播客添加到PlanB网络
description: 如何将新播客添加到PlanB网络？
---
![podcast](assets/cover.webp)

PlanB的使命是以尽可能多的语言提供关于比特币的顶级教育资源。网站上发布的所有内容都是开源的，并托管在GitHub上，允许任何人参与丰富该平台。

您是否正在寻找将比特币播客添加到PlanB网络站点并为您的节目增加曝光度，但不知道如何操作？这个教程是为您准备的！
![podcast](assets/01.webp)
- 首先，您需要拥有一个GitHub账户。如果您不知道如何创建一个，我们制作了[一个详细的教程来指导您](https://planb.network/tutorials/others/create-github-account)。
- 转到[PlanB专用于数据的GitHub仓库](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts)的`resources/podcasts/`部分：
![podcast](assets/02.webp)
- 点击右上角的`Add file`按钮，然后点击`Create new file`：
![podcast](assets/03.webp)
- 如果您以前从未为PlanB网络的内容做出过贡献，您将需要创建原始仓库的分支。分支一个仓库意味着在您自己的GitHub账户上创建该仓库的副本，允许您在不影响原始仓库的情况下进行项目工作。点击`Fork this repository`按钮：
![podcast](assets/04.webp)
- 然后您将进入GitHub编辑页面：
![podcast](assets/05.webp)
- 为您的播客创建一个文件夹。为此，在`Name your file...`框中，用短划线代替空格写下您的播客名称。例如，如果您的节目叫做"Super Podcast Bitcoin"，您应该写`super-podcast-bitcoin`：
![podcast](assets/06.webp)
- 要验证文件夹的创建，只需在同一个框中的播客名称后添加一个斜杠，例如：`super-podcast-bitcoin/`。添加斜杠会自动创建一个文件夹而不是文件：
![podcast](assets/07.webp)
- 在这个文件夹中，您将创建一个名为`podcast.yml`的第一个YAML文件：
![podcast](assets/08.webp)
- 使用以下模板填写有关您播客的信息：

```yaml
name: 
host: 
language: 
links:
  podcast: 
  twitter: 
  website: 
description: |
  
tags:
  - 
  - 
contributors:
  - 
```

以下是每个字段填写的详细信息：

- **`name`**: 指明您播客的名称。
- **`host`**: 列出播客的主持人或主讲人的名字或化名。每个名字应该用逗号分隔。
- **`language`**: 指明您播客中使用的语言的语言代码。例如，对于英语，注明`en`，对于意大利语`it`...

- **`links`**: 提供指向您内容的链接。您有两个选择：
	- `podcast`：您播客的链接，
	- `twitter`：播客或制作播客的组织的Twitter个人资料的链接，
	- `website`：播客或制作播客的组织的网站的链接。
- **`description`**: 添加一个简短的段落来描述你的播客。描述必须与`language:`字段中指示的语言相同。
- **`tags`**: 添加与你的播客相关的两个标签。例如：
    - `比特币`
    - `技术`
    - `经济`
    - `教育`...

- **`contributors`**: 如果你有贡献者ID，请提及。

例如，你的YAML文件可能看起来像这样：

```yaml
name: 超级比特币播客
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: zh
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  超级比特币播客是每周一次在Twitter上举行的技术直播会议，深入探讨比特币协议、二层解决方案以及所有令人兴奋的事物。我们的主持人Lounes, Pantamis, Loïc和Sosthene将回答你的问题，并提供世界上最技术化的比特币展示。

tags:
  - 比特币
  - 技术
contributors:
  - rabbit-hole
```

![播客](assets/09.webp)

- 完成对这个文件的修改后，通过点击`Commit changes...`按钮来保存它们：
![播客](assets/10.webp)
- 为你的更改添加一个标题，以及一个简短的描述：
![播客](assets/11.webp)
- 点击绿色的`Propose changes`按钮：
![播客](assets/12.webp)
- 然后你将到达一个总结你所有更改的页面：
![播客](assets/13.webp)
- 点击右上角的你的GitHub头像，然后点击`Your Repositories`：
![播客](assets/14.webp)
- 选择你fork的PlanB Network仓库：
![播客](assets/15.webp)
- 你应该会在窗口顶部看到一个带有你的新分支的通知。它可能被称为`patch-1`。点击它：
![播客](assets/16.webp)
- 你现在在你的工作分支上：
![播客](assets/17.webp)
- 返回到`resources/podcast/`文件夹，并选择你在上一个提交中刚创建的播客文件夹：![播客](assets/18.webp)
- 在你的播客文件夹中，点击`Add file`按钮，然后点击`Create new file`：
![播客](assets/19.webp)
- 将这个新文件夹命名为`assets`，并通过在末尾添加斜杠`/`来确认其创建：
![播客](assets/20.webp)
- 在这个`assets`文件夹中，创建一个名为`.gitkeep`的文件：
![播客](assets/21.webp)
- 点击`Commit changes...`按钮：
![播客](assets/22.webp)
- 保留默认的提交标题，并确保选中了`Commit directly to the patch-1 branch`框，然后点击`Commit changes`：
![播客](assets/23.webp)
- 返回到`assets`文件夹：
![播客](assets/24.webp)
- 点击`Add file`按钮，然后点击`Upload files`：
![播客](assets/25.webp)
- 将打开一个新页面。将您的播客徽标拖放到该区域中。这张图片将会在PlanB Network站点上显示：![podcast](assets/26.webp)
- 注意，图片必须是正方形的，以最适合我们的网站：![podcast](assets/27.webp)
- 图片上传后，验证`Commit directly to the patch-1 branch`框是否已勾选，然后点击`Commit changes`：![podcast](assets/28.webp)
- 注意，您的图片必须命名为`logo`并且必须是`.webp`格式。因此，完整的文件名应该是：`logo.webp`：![podcast](assets/29.webp)
- 返回到您的`assets`文件夹并点击中间文件`.gitkeep`：![podcast](assets/30.webp)
- 在文件上，点击右上角的三个小点然后点击`Delete file`：![podcast](assets/31.webp)
- 验证您是否仍在同一个工作分支上，然后点击`Commit changes`按钮：![podcast](assets/32.webp)
- 为您的提交添加标题和描述，然后点击`Commit changes`：![podcast](assets/33.webp)
- 返回到您的仓库根目录：![podcast](assets/34.webp)
- 您应该看到一条消息，指示您的分支已经发生了变化。点击`Compare & pull request`按钮：![podcast](assets/35.webp)
- 为您的PR添加清晰的标题和描述：![podcast](assets/36.webp)
- 点击`Create pull request`按钮：![podcast](assets/37.webp)
恭喜！您的PR已经成功创建。管理员现在将对其进行审查，如果一切顺利，将其合并到PlanB Network的主仓库中。几天后，您应该会在网站上看到您的播客。

请确保跟踪您PR的进展。管理员可能会留下评论，要求提供额外信息。只要您的PR未被验证，您就可以在PlanB Network GitHub仓库的`Pull requests`标签中查看它：![podcast](assets/38.webp)
非常感谢您的宝贵贡献！:)

---
name: 将一本书添加到PlanB网络
description: 如何将一本新书添加到PlanB网络？
---
![book](assets/cover.webp)

PlanB的使命是以尽可能多的语言提供关于比特币的顶级教育资源。网站上发布的所有内容都是开源的，并托管在GitHub上，允许任何人为平台的丰富做出贡献。

**你想在PlanB网络站点上添加一本与比特币相关的书籍，并增加你作品的可见性，但不知道如何操作？这个教程是为你准备的！**
![book](assets/01.webp)
- 首先，你需要拥有一个GitHub账户。如果你不知道如何创建账户，我们制作了[一个详细的教程来指导你](https://planb.network/tutorials/others/create-github-account)。
- 前往[PlanB专门用于数据的GitHub仓库](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books)的`resources/books/`部分：
![book](assets/02.webp)
- 点击右上角的`Add file`按钮，然后点击`Create new file`：
![book](assets/03.webp)
- 如果你之前从未为PlanB网络的内容做过贡献，你将需要创建你自己的原始仓库的分支。分支一个仓库意味着在你自己的GitHub账户上创建该仓库的一个副本，允许你在不影响原始仓库的情况下进行项目工作。点击`Fork this repository`按钮：
![book](assets/04.webp)
- 然后你将进入GitHub编辑页面：
![book](assets/05.webp)
- 为你的书创建一个文件夹。为此，在`Name your file...`框中，用短划线代替空格写下你书的名字。例如，如果你的书叫"*My Bitcoin Book*"，你应该记为`my-bitcoin-book`：
![book](assets/06.webp)
- 要验证文件夹的创建，只需在同一个框中的书名后添加一个斜杠，例如：`my-bitcoin-book/`。添加斜杠会自动创建一个文件夹而不是一个文件：
![book](assets/07.webp)
- 在这个文件夹中，你将创建一个名为`book.yml`的第一个YAML文件：
![book](assets/08.webp)
- 使用此模板填写有关你书的信息：

```yaml
author: 
level: 
tags:
  - 
  - 
```

这里是每个字段需要填写的详细信息：
- **`author`**：指明书的作者名字。
- **`level`**：指明阅读和理解书籍所需的水平。从以下级别中选择一个：
	- `beginner`
	- `intermediate`
- `advanced` - `expert`
- **`tags`**：添加两到三个与你的书相关的标签。例如：
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`...

例如，你的YAML文件可能看起来像这样：

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![book](assets/09.webp)
- 一旦你完成了对这个文件的更改，通过点击`Commit changes...`按钮保存它们：
![book](assets/10.webp)
- 为您的更改添加标题以及简短描述：![book](assets/11.webp)
- 点击绿色的 `Propose changes` 按钮：![book](assets/12.webp)
- 接下来，您将进入一个页面，总结您所有的更改：![book](assets/13.webp)
- 点击右上角的 GitHub 个人资料图片，然后点击 `Your Repositories`：![book](assets/14.webp)
- 选择您分叉的 PlanB Network 仓库：![book](assets/15.webp)
- 您应该会在窗口顶部看到一个带有您新分支的通知。它可能被称为 `patch-1`。点击它：![book](assets/16.webp)
- 您现在处于您的工作分支上：![book](assets/17.webp)
- 返回到 `resources/books/` 文件夹，并选择您在之前的提交中刚创建的书籍文件夹：![book](assets/18.webp)
- 在您的书籍文件夹中，点击 `Add file` 按钮，然后点击 `Create new file`：![book](assets/19.webp)
- 将这个新文件夹命名为 `assets` 并通过在末尾添加斜杠 `/` 来确认其创建：![book](assets/20.webp)
- 在这个 `assets` 文件夹中，创建一个名为 `.gitkeep` 的文件：![book](assets/21.webp)
- 点击 `Commit changes...` 按钮：![book](assets/22.webp)
- 保留默认的提交标题，并确保选中了 `Commit directly to the patch-1 branch` 框，然后点击 `Commit changes`：![book](assets/23.webp)
- 返回到 `assets` 文件夹：![book](assets/24.webp)
- 点击 `Add file` 按钮，然后点击 `Upload files`：![book](assets/25.webp)
- 一个新页面将打开。将您书籍的封面图片拖放到区域中。这张图片将在 PlanB Network 网站上显示：![book](assets/26.webp)
- 注意，图片必须是书籍的格式，以最佳适应我们的网站，例如：![book](assets/27.webp)
- 一旦图片上传，确保选中了 `Commit directly to the patch-1 branch` 框，然后点击 `Commit changes`：![book](assets/28.webp)- 请注意，如果封面是英文的，您的图片必须命名为 `cover_en`，并且必须是 `.webp` 格式。因此，完整的文件名应该是 `cover_en.webp`、`cover_fr.webp`、`cover_it.webp` 等。如果您希望每种语言使用不同的封面图片，例如在书籍翻译的情况下，您可以将它们放在 `assets` 文件夹的同一位置：![book](assets/29.webp)
- 返回到您的 `assets` 文件夹并点击 `.gitkeep` 中间文件：![book](assets/30.webp)
- 一旦在文件上，点击右上角的 3 个小点，然后点击 `Delete file`：![book](assets/31.webp)
- 确保您仍在同一个工作分支上，然后点击 `Commit changes...` 按钮：![book](assets/32.webp)
- 添加标题和描述到您的提交，然后点击 `Commit changes`：![book](assets/33.webp)
- 返回到您的书籍文件夹：![book](assets/34.webp)
- 点击 `Add file` 按钮，然后点击 `Create new file`：
![book](assets/35.webp)
- 通过以书籍的语言指示符命名来创建一个新的YAML文件。这个文件将用于书籍的描述。例如，如果我想用英语编写我的描述，我会将这个文件命名为 `en.yml`：
![book](assets/36.webp)
- 使用以下模板填写这个YAML文件：
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

这里是每个字段需要填写的细节：
- **`title`**：用引号标明书籍的名称。
- **`publication_year`**：标明书籍的出版年份。
- **`cover`**：标明与您当前正在编辑的YAML文件语言相对应的封面图片文件名。例如，如果您正在编辑 `en.yml` 文件，并且之前已经添加了标题为 `cover_en.webp` 的英文封面图片，只需在此字段中标明 `cover_en.webp`。
- **`description`**：添加一个简短的段落描述书籍。描述必须与YAML文件标题中指明的语言相同。
- **`contributors`**：如果您有贡献者ID，请添加。

例如，您的YAML文件可能看起来像这样：

```yaml
title: "我的比特币书籍"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
探索比特币的开创性世界，这是一本为初学者量身定制的综合指南。我的比特币书籍揭示了比特币的复杂性，提供了一个清晰简洁的介绍，说明了协议是如何工作的。从其革命性技术到其对全球经济的潜在影响，本书提供了宝贵的见解和实用知识。非常适合比特币新手，它涵盖了基础知识、安全提示和数字金融的未来。深入了解金钱的未来，并赋予自己信心地导航数字时代的知识。

contributors:
  - pretty-private

![book](assets/37.webp)
- 点击 `Commit changes...` 按钮：
![book](assets/38.webp)
- 确保选中了 `Commit directly to the patch-1 branch` 复选框，添加标题，然后点击 `Commit changes`：
![book](assets/39.webp)
- 书籍文件夹现在应该看起来像这样：
![book](assets/40.webp)
- 如果一切看起来都不错，返回到您的fork的根目录：
![book](assets/41.webp)
- 您应该看到一条消息，表明您的分支已被修改。点击 `Compare & pull request` 按钮：
![book](assets/42.webp)
- 为您的PR添加一个清晰的标题和描述：
![book](assets/43.webp)
- 点击 `Create pull request` 按钮：
![book](assets/44.webp)
恭喜！您的PR已成功创建。管理员现在将对其进行审查，如果一切顺利，将其合并到PlanB Network的主仓库中。几天后，您应该会在网站上看到您的书籍出现。

确保跟踪您PR的进展。管理员可能会留下评论，要求提供额外信息。只要您的PR未被验证，您就可以在PlanB Network的GitHub仓库的 `Pull requests` 标签中查看它。
非常感谢您的宝贵贡献！:)

---
name: 贡献 - Git 教程（高级）
description: 为高级用户提供计划教程的指南 ₿ 与 Git 联网
---
![cover](assets/cover.webp)

在学习本教程添加新教程之前，您需要完成几个初步步骤。如果您还没有这样做，请先看看这个入门教程，然后再回到这里：

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

您已经拥有 ：


- 为您的教程选择一个主题；
- 通过 [Telegram 群组](https://t.me/PlanBNetwork_ContentBuilder) 或 paolo@planb.network 与计划 ₿ 网络团队联系；
- 选择您的捐助工具。

在这篇面向资深 Git 用户的教程中，我们将简要总结提供新计划 ₿ 网络教程的关键步骤和基本准则。如果您对 Git 和 GitHub 不熟悉，我建议您参考另外两本更详细的教程，它们将一步一步地指导您：


- 中级（GitHub 桌面）** ：

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- 初学者（网络界面）** ：

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## 建议使用的工具

用于编辑 Markdown 文件 ：


- 黑曜石**（免费，非开源）
- 标记文本** （免费、开源）
- Zettlr** （免费，开源）
- Typora**（付费软件，~15 欧元，非开源）

用于 Git ：


- Git**（免费、开源）
- GitHub 桌面**（免费、开源）
- Sourcetree** （免费，非开源）

用于编辑 YAML 文件 ：


- Visual Studio Code**（免费，开源）
- Sublime Text**（免费但有限制，非开源）

创建图表和视觉效果


- Canva**（免费，有付费选项，非开源）
- Inkscape**（免费，开源）
- Penpot**（免费、开源）

## 工作流程

### 1 - 配置本地环境


- 您必须拥有自己的 [GitHub 上的 Plan ₿ Network 代码库](https://github.com/PlanB-Network/bitcoin-educational-content) fork。
- 将分叉的主分支 (`dev`) 与源代码版本库同步。
- 更新本地克隆。

```
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<votre-nom-utilisateur>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```

### 2 - 创建新分支


- 确保你所在的是 `dev` 分支。
- 创建一个新分支，并使用一个描述性的名称（如 `tuto-green-wallet-loic`）。
- 在您的在线分叉上发布该分支。

```
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - 添加教程文件

***注：*** 您可以使用[我的 Python GUI 脚本](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation)自动执行第 3 和第 4 步。直接从本地克隆文件夹中运行该脚本，然后在图形用户界面上填写所需字段。有关如何安装和使用的详细信息，请参阅 [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md)。

如果您喜欢手动操作，请按照以下步骤进行：


- 在本地存储库中找到相应文件夹（如 `tutorials/wallet`）。
- 创建一个名称明确的教程专用目录（例如 "green-wallet"）。该文件夹名称也将决定教程的 URL 路径。文件夹名称应使用小写字母，不包含特殊字符（连字符除外），也不包含空格。
- 在此目录中添加以下项目：
    - 一个名为 `assets` 的子文件夹，其中包含 ：
        - 两个`.webp`图像：
            - logo.webp`：教程徽标（带背景的正方形格式）。该徽标必须代表所介绍的软件或工具。如果教程不是针对某个工具（例如：生成记忆短语的一般指南），则可以选择合适的视觉效果（例如：通用图标）。
            - cover.webp`：教程开始时显示的封面图片。
        - 包含教程原始语言代码的子文件夹。例如，如果教程是用英语编写的，该子文件夹应命名为 "en"。将教程的所有视觉资料（图表、图像、截图等）放在此文件夹中。
    - 包含元数据（作者、标签、类别、难度等）的 `tutorial.yml` 文件。
    - 包含教程的 Markdown 文件，根据语言代码命名（如 `fr.md`、`en.md` 等）。

```
# Positionnez-vous dans le dossier approprié
cd tutorials/wallet
# Créez le répertoire dédié au tutoriel
mkdir green-wallet
cd green-wallet
# Créez le sous-dossier 'assets'
mkdir -p assets
# Créez le sous-dossier pour le code de la langue d’origine (exemple : 'en' pour l’anglais)
mkdir -p assets/en
# Créez les fichiers de métadonnées et le tutoriel Markdown (exemple : 'en.md' pour l’anglais)
touch tutorial.yml en.md
```

### 4 - 填写 YAML 文件


- 按如下方式完成 `tutorial.yml` 文件：

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

以下是必填字段：


- id**：UUID（通用唯一标识符），用于唯一标识教程。您可以使用[在线工具](https://www.uuidgenerator.net/version4)生成它。唯一的限制是该 UUID 必须是随机的，以免与平台上的其他 UUID 冲突；
- project_id** ：教程中介绍的工具背后的公司或组织的 UUID[来自项目列表](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects)。例如，如果你正在做一个关于绿色钱包软件的教程，你可以在以下文件中找到这个 `project_id` ：bitcoin-educational-content/resources/projects/blockstream/project.yml`。之所以在教程的 YAML 文件中添加此信息，是因为 Plan ₿ Network 维护着一个所有在比特币或相关项目上运营的公司和组织的数据库。将链接实体的 `project_id` 添加到您的教程中，就在两个元素之间建立了链接；
- 标签**：从计划₿ 网络标签列表]中专门选择 2 或 3 个与教程内容相关的关键字(https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md)；
- 类别** ：根据计划₿ 网络结构（例如钱包："桌面"、"硬件"、"移动"、"备份"），与教程内容相对应的子类别；
- 级别** ：教程难度级别，从 ：
    - 初学者
    - 中级
    - 高级
    - 专家
- 教授**：您在[您的教师简介](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors)中显示的 "贡献者 ID"（BIP39 字样）；
- original_language** ：教程的原始语言（如`fr`、`en`等）；
- 校对**：有关校对过程的信息。填写第一部分，因为校对自己的教程也算第一次验证：
    - 语言**：校对语言代码（如`fr`、`en`等）。
    - last_contribution_date**：今天的日期。
    - 紧迫性** ：留空。
    - contributors_id** ：您的 GitHub ID。
    - 奖励** ：留空。

有关教师 ID 的详细信息，请参阅相应的教程 ：

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

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
urgency:
contributors_id:
- LoicPandul
reward:
```

### 5 - 撰写内容


- 用......完成 Markdown 文件属性：
    - 标题（`name`）。
    - 简短描述 (`description`)。
- 使用 Markdown 语法在教程顶部添加封面图片（用显示的工具名称替换 "绿色"）：

```
![cover-green](assets/cover.webp)
```


- 用 Markdown 编写教程内容：
    - 使用结构合理的标题 (`##`)、列表和段落。
    - 使用 Markdown 语法插入视觉效果：

```
![nom-image](assets/en/001.webp)
```


- 将图表和图像放入`/assets`中相应的语言子文件夹。

### 6 - 保存并提交教程


- 创建带有说明性信息的提交，将更改保存到本地。
- 将更改推送到 GitHub 分支。

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- 完成后，在 GitHub 上创建一个拉取请求 (PR)，提议整合您的修改。
- 为 PR 添加标题和简要说明。在注释中注明相应的问题编号。

### 7 - 校对与合并


- 等待管理员的确认或反馈。
- 如有必要，进行修改并推送新的提交。

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- 合并 PR 后，就可以删除工作分支了。

## 内容创建标准


- 平台支持的格式** ：
    - 经典 Markdown：列表、链接、图片、引号、粗体、斜体等。
    - LaTeX（仅限块，非内联）：以 `$$` 分隔。
    - 内联代码：带有单个回车键的语法。
    - 代码块：带有三个反标点的语法，例如 ：

```
print("Hello, Bitcoin!")
```


- 插图和图表** ：
    - 所有图片必须为 WebP 格式。如有需要，请使用此免费工具进行转换：[ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - 用 2 或 3 个数字为视觉效果命名（如 `001.webp`、`002.webp`）。
    - 对于手机或硬件钱包教程，请使用模型。
    - 仅使用自制或免版税的视觉效果。
    - 确保它们具有相关性和高质量。
- 图形章程** ：
    - 字体：[Rubik](https://fonts.google.com/specimen/Rubik).
    - 颜色计划 ₿ 网络 ：
        - 橙色：`#FF5C00
        - 黑色：`#000000
        - 白色： `#FFFFFF

如果您在提交教程时遇到技术问题，请不要犹豫，在[我们专门的 Telegram 投稿群组](https://t.me/PlanBNetwork_ContentBuilder)上寻求帮助。非常感谢！
---
name: Plan ₿ Network 教授
description: 如何在 Plan ₿ Network 上添加或修改我的教师档案？
---
![cover](assets/cover.webp)

如果您计划通过编写新教程或课程为 Plan ₿ Network 做出贡献，则需要建立教师档案。有了教师档案，您就可以为您在平台上贡献的内容获得相应的学分。

对于已经在 Plan ₿ Network 上参与创建教育内容的人来说，您可能已经有了一个教师配置文件。您可以在 `/professors`文件夹中找到它[在我们的 GitHub 存储库中](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors)。如果您的配置文件已经存在，请在 `professor.yml` 文件中找到您的登录名。

要更改您的个人资料，请访问本教程末尾的 "编辑您的教师个人资料 "部分。

## 使用我们的软件添加新教师

在 Plan ₿ Network 上创建教师档案的最简单方法是使用我们集成的 Python 工具。具体操作如下

### 1 - 配置本地环境

您必须从 [GitHub 上的 Plan ₿ Network 代码库](https://github.com/PlanB-Network/Bitcoin-educational-content) 安装自己的 Fork。

将 Fork 的主分支 (`dev`) 与源代码库同步。

更新本地克隆。

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
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

确保你在 `dev` 分支上。创建一个新分支，取一个描述性的名称（如 `add-professor-loic-morel`）。

在 Fork 上在线发布该分支。

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```

### 3 - 创建您的教师简介

转到本地克隆上的 `scripts/tutorial-related/data-creator/` 文件夹。确保已经安装了软件所需的所有依赖项，首先安装 Python .NET Framework：

```bash
pip install -r requirements.txt
```

然后使用命令 ：

```bash
python3 main.py
```

进入主页后，输入克隆仓库的本地路径、编写语言和 GitHub ID。如果您是为他人创建此配置文件，并且已经拥有教授配置文件，请在 "*PBN Professor's ID*"字段中输入您的 ID。如果您正在创建自己的个人档案，您还没有教授 ID，因为您正在创建过程中，所以请将此字段留空。

然后点击 "*新教授*"按钮。

![Image](assets/fr/01.webp)

填写所需信息（请注意，所有信息都将在我们的平台和 GitHub 上公开）：


- 您的教师档案名称（使用您的名和姓或化名，小写） ；
- 您的姓名或昵称 ；
- 随机生成您的登录名；
- 您的网站和个人简介 X（可选） ；
- 接收读者捐款的 Lightning Address（可选） ；
- 从列表中选择 2 或 3 个标签；
- 点击 "*选择图像*"，从本地文件夹中选择一张配置文件图像（图像可以使用任何名称和格式，软件会自动调整。只需确保图片为正方形即可）；
- 撰写简短的个人简介。

点击 "*创建教授*"完成创建。这将自动 generate 您的个人资料所需的所有文件。

![Image](assets/fr/02.webp)

创建一个带有说明信息的提交，将更改保存在本地。将更改推送到 Fork GitHub。

```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```

完成后，在 GitHub 上创建一个拉取请求 (PR)，建议整合您的修改。在 PR 中添加标题和简要说明。

### 4 - 校对与合并

等待管理员的验证或反馈。如有必要，进行更正并推送新的提交。

```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```

合并 PR 后，就可以删除工作分支了。

## 修改您的教师简介

如果你已经掌握了 Git 的使用方法，可以通过创建一个新分支并直接在现有文件夹中编辑相关文件来修改你的教师配置文件。根据需要修改的信息，可以在 `professor.yml` 文件或 markdown 文件中进行修改。在本地完成更改后，将其推送到 Fork 并提交 PR。

对于初学者，我建议直接通过 GitHub 的 Interface web 进行修改。请确保你有一个 GitHub 账户。如果不知道如何创建账户，请参考本教程：

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
访问 [Plan ₿ Network 数据专用 GitHub 存储库](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors)。

![Image](assets/fr/03.webp)

点击 "*教授*"文件夹，然后进入个人文件夹。

![Image](assets/fr/04.webp)

要更改您的个人资料元数据，如闪电 Address、名称或链接，请选择 "*professor.yml*"文件。要更改描述，请点击您所使用语言的 YAML 文件（如 "*en.yml*"或 "*fr.yml*"）。

如果您修改了描述，请记得删除所有过时的翻译。然后，您可以在 LLM 的帮助下将您的描述翻译成其他语言，或者只保留您的母语描述，并在您的拉动请求中提及您的描述需要我们团队的翻译。

![Image](assets/fr/05.webp)

打开要修改的文件后，点击铅笔图标。

![Image](assets/fr/06.webp)

如果您还没有 Plan ₿ Network 仓库中的 Fork，GitHub 会建议您创建一个。点击 "*Fork this repository*"。

![Image](assets/fr/07.webp)

对文件进行所需的更改。完成后，点击 "*提交更改*"。

![Image](assets/fr/08.webp)

输入描述更改的信息，然后选择 "*提出更改*"。

![Image](assets/fr/09.webp)

系统将显示您所做更改的摘要。如果您想对您的配置文件做进一步修改，可以返回文件夹并做进一步提交。完成后，点击 "*创建拉取请求*"。

拉取请求是将您的分支中的更改整合到 Plan ₿ Network 版本库主分支中的请求，允许在合并之前对更改进行审查和讨论。

![Image](assets/fr/10.webp)

确保在 Interface 的顶层，你的工作分支与 Plan ₿ Network 版本库的 `dev` 分支（即主分支）合并。

输入一个标题，简要概括您希望与源代码库合并的更改。添加一个简短的注释来描述这些更改，然后点击 Green 的 "*创建拉取请求*"按钮来确认拉取请求：

![Image](assets/fr/11.webp)

然后，您的 PR 就会出现在 Plan ₿ Network 主版本库的 "*Pull Request*（*拉取请求*）"选项卡中。您现在要做的就是等待管理员合并您的修改。

![Image](assets/fr/12.webp)

如果您在提交更改时遇到任何技术问题，请随时在[我们专门用于贡献的 Telegram 群组](https://t.me/PlanBNetwork_ContentBuilder)上寻求帮助。非常感谢！
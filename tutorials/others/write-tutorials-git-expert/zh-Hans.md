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

在这篇面向资深 Git 用户的教程中，我们将简要总结提供新计划₿ 网络教程的关键步骤和基本准则。如果您对 Git 和 GitHub 不熟悉，我建议您参考另外两个更详细的教程，它们将一步一步地教您：


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

```bash
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

```bash
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

```bash
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
last_contribution_date:
urgency:
contributors_id:
-
reward:
````
Voici le détail des champs obligatoires :
- **id** : Un UUID (_Universally Unique Identifier_) permettant d’identifier de manière unique le tutoriel. Vous pouvez le générer avec [un outil en ligne](https://www.uuidgenerator.net/version4). La seule contrainte est que cet UUID soit aléatoire pour ne pas avoir de conflit avec un autre UUID sur la plateforme ;
- **project_id** : L'UUID de l’entreprise ou de l’organisation derrière l’outil présenté dans le tutoriel [depuis la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, si vous réalisez un tutoriel sur le logiciel Green Wallet, vous pouvez trouver ce `project_id` dans le fichier suivant : `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Cette information est ajoutée dans le fichier YAML de votre tutoriel parce que Plan ₿ Network maintient une base de données de toutes les entreprises et organisations opérant sur Bitcoin ou des projets connexes. En ajoutant le `project_id` de l'entité liée à votre tutoriel, vous créez un lien entre les deux éléments ;
- **tags** : 2 ou 3 mots-clés pertinents liés au contenu du tutoriel, choisis exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ;
- **category** : La sous-catégorie correspondant au contenu du tutoriel, selon la structure du site Plan ₿ Network (par exemple pour les wallets : `desktop`, `hardware`, `mobile`, `backup`) ;
- **level** : Le niveau de difficulté du tutoriel, parmi :
- `beginner`
- `intermediate`
- `advanced`
- `expert`
- **professor** : Votre `contributor_id` (mots BIP39) tel qu'affiché sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) ;
- **original_language** : La langue d’origine du tutoriel (par exemple `fr`, `en`, etc.) ;
- **proofreading** : Informations sur le processus de relecture. Remplissez la première partie, car la relecture de votre propre tutoriel compte comme une première validation :
- **language** : Code de langue de la relecture (par exemple `fr`, `en`, etc.).
- **last_contribution_date** : Date du jour.
- **urgency** : Laissez vide.
- **contributors_id** : Votre ID GitHub.
- **reward** : Laissez vide.
Pour davantage de détails sur votre identifiant de professeur, reportez-vous au tutoriel correspondant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
```

id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id：3b2f45e6-d612-412c-95ba-cf65b49aa5b8

标签


  - 钱包
  - 软件
  - 钥匙

类别：移动

级别：初级

学分

教授：pretty-private

# 校对元数据

original_language: fr

校对：


  - 语言：法语

last_contribution_date: 2024-11-20

紧迫性：

贡献者_id：


      - LoicPandul

奖励：

```
### 5 - Rédigez le contenu
- Complétez les propriétés du fichier Markdown avec :
- Le titre (`name`).
- Une courte description (`description`).
- Ajoutez l’image de couverture en haut du tutoriel avec la syntaxe Markdown (remplacez "green" par le nom de l’outil présenté) :
```

![cover-green](assets/cover.webp)

```
- Rédigez le contenu du tutoriel en Markdown :
- Utilisez des titres bien structurés (`##`), des listes et des paragraphes.
- Insérez des visuels avec la syntaxe Markdown :
```

![nom-image](assets/en/001.webp)

```
- Placez les schémas et images dans le sous-dossier de langue correspondant, dans `/assets`.
### 6 - Enregistrez et soumettez le tutoriel
- Enregistrez vos modifications localement en créant un commit avec un message descriptif.
- Poussez les changements sur votre fork GitHub.
```

# 创建带有描述性信息的提交

git commit -m "添加绿色钱包教程"

# 将改良品推到叉子上

git push origin tuto-green-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# 创建一个提交，描述所做的更正

git commit -m "审查绿色钱包教程后的更正"

# 推动叉子修正

git push origin tuto-green-wallet-loic

```
- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.
## Normes de création de contenu
- **Formatage supporté sur la plateforme** :
- Markdown classique : listes, liens, images, citations, gras, italique, etc.
- LaTeX (en bloc uniquement, pas inline) : délimité par `$$`.
- Code inline : Syntaxe avec un seul backtick.
- Blocs de code : Syntaxe avec trois backtick, par exemple :
```

print("Hello, Bitcoin!")

```
---
name: 貢献 - Gitチュートリアル（上級）
description: プランのチュートリアルを提供する上級者向けガイド ₿ Gitを使ったネットワーク
---
![cover](assets/cover.webp)

新しいチュートリアルを追加するためのこのチュートリアルに従う前に、いくつかの予備ステップを完了する必要があります。まだ完了していない場合は、まずこの入門チュートリアルをご覧ください：

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
あなたはすでに持っている：


- チュートリアルのテーマを決めてください；
- Plan ₿ Networkチームに[Telegram group](https://t.me/PlanBNetwork_ContentBuilder)またはpaolo@planb.network；
- 貢献ツールを選ぶ

このチュートリアルでは、Git の経験豊富なユーザーを対象に、新しい Plan ₋ Network チュートリアルを提供するための重要なステップと重要なガイドラインを簡単にまとめます。Git や GitHub に慣れていない場合は、以下の 2 つのチュートリアルを参考にすることをお勧めします：


- 中級（GitHub Desktop）** ：

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- 初心者向け（ウェブインターフェース）** ：

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## 推奨ツール

Markdownファイル編集用：


- オブシディアン**（フリー、オープンソースではない）
- マークテキスト**（無料、オープンソース）
- Zettlr**（無料、オープンソース）
- Typora** （有料、～15ユーロ、オープンソースではない）

ギットのために：


- Git**（フリー、オープンソース）
- GitHub Desktop** （無料、オープンソース）
- ソースツリー**（無料、オープンソースではない）

YAMLファイルの編集 ：


- Visual Studio Code**（無料、オープンソース）
- Sublime Text** （制限付きで無料、オープンソースではない）

ダイアグラムやビジュアルを作成する：


- Canva**（無料、有料オプションあり、オープンソースではない）
- Inkscape**（フリー、オープンソース）
- Penpot**（無料、オープンソース）

## ワークフロー

### 1 - ローカル環境を設定する


- GitHub 上の Plan ₿ Network リポジトリ](https://github.com/PlanB-Network/bitcoin-educational-content) をフォークする必要があります。
- フォークのメインブランチ (`dev`) をソースリポジトリと同期させます。
- ローカルのクローンを更新する。

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

### 2 - 新しいブランチを作る


- dev`ブランチにいることを確認してください。
- わかりやすい名前（例：`tuto-green-wallet-loic`）で新しいブランチを作成する。
- このブランチをオンラインフォークで公開する。

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - チュートリアルのドキュメントを追加する

***注：*** ステップ 3 と 4 は、[私の Python GUI スクリプト](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation) を使って自動化できます。ローカルクローンのフォルダから直接実行し、GUI上で必要なフィールドを埋めてください。インストールと使用方法の詳細については、[README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md)を参照してください。

手動で行う場合は、以下の手順に従ってください：


- ローカルリポジトリ内の適切なフォルダを探します（例：`tutorials/wallet`）。
- チュートリアル専用のディレクトリをわかりやすい名前で作成します（例：`green-wallet`）。このフォルダ名はチュートリアルのURLパスも決定します。小文字で、特殊文字（ハイフンを除く）とスペースは使用しないでください。
- このディレクトリに以下の項目を追加する：
    - assets`というサブフォルダには.NET Frameworkが格納されている：
        - 2つの `.webp` 画像：
            - `logo.webp`：チュートリアルのロゴ（背景付きの正方形のフォーマット）。このロゴは紹介するソフトウェアやツールを表していなければなりません。チュートリアルがツールに特化していない場合（例：ニーモニックフレーズを生成するための一般的なガイド）、適切なビジュアル（例：一般的なアイコン）を選択することができます。
            - cover.webp`：チュートリアルの最初に表示されるカバー画像。
        - チュートリアルの元の言語のコードを持つサブフォルダです。例えば、チュートリアルが英語で書かれている場合、このサブフォルダは `en' という名前にします。チュートリアルのすべてのビジュアル（図、画像、スクリーンショットなど）をこのフォルダに置きます。
    - メタデータ（作者、タグ、カテゴリー、難易度など）を含む`tutorial.yml`ファイル。
    - チュートリアルを含む Markdown ファイルで、言語コードに従って名前が付けられます (例 `fr.md`、`en.md` など)。

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

### 4 - YAMLファイルを埋める


- 以下のように`tutorial.yml`ファイルを完成させる：

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

プロジェクトID3b2f45e6-d612-412c-95ba-cf65b49aa5b8

のタグがある：


  - 財布
  - ソフトウェア
  - キー

category:モバイル

レベル：初心者

のクレジットがある：

教授：プリティ・プライベート

# メタデータの校正

原語: fr

校正：


  - 言語: fr

last_contribution_date: 2024-11-20

急を要する：

contributors_id：


      - ロイック・パンドゥル

報奨金だ：

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

# 説明的なメッセージを含むコミットを作成する

git commit -m "グリーンウォレットのチュートリアルを追加"

# 修正をフォークに押し付ける

git push origin tuto-green-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# 修正内容を記述したコミットを作成する

git commit -m "グリーンウォレットのチュートリアルのレビュー後の修正"

# フォークを押して修正する

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

print("こんにちは、ビットコイン！")

```
---
name: 貢献 - Gitチュートリアル（上級）
description: プランのチュートリアルを提供する上級者向けガイド ₿ Gitを使ったネットワーク
---
![cover](assets/cover.webp)

新しいチュートリアルを追加するためのこのチュートリアルに従う前に、いくつかの予備ステップを完了する必要があります。まだ完了していない場合は、まずこの入門チュートリアルをご覧ください：

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

あなたはすでに持っている：


- チュートリアルのテーマを決めてください；
- Plan ₿ Networkチームに[Telegram group](https://t.me/PlanBNetwork_ContentBuilder)またはpaolo@planb.network；
- 貢献ツールを選ぶ

このチュートリアルでは、Git の使用経験が豊富なユーザーを対象に、新しい Plan ₋ Network チュートリアルを提供するための重要なステップと重要なガイドラインを簡単にまとめます。Git や GitHub にあまりなじみがないのなら、以下の 2 つのチュートリアルを参考にすることをおすすめします：


- 中級（GitHub Desktop）** ：

https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- 初心者向け（ウェブインターフェース）** ：

https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

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

### 2 - 新しいブランチを作る


- dev`ブランチにいることを確認してください。
- わかりやすい名前（例：`tuto-green-wallet-loic`）で新しいブランチを作成する。
- このブランチをオンラインフォークで公開する。

```
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

### 4 - YAMLファイルを埋める


- 以下のように`tutorial.yml`ファイルを完成させる：

```
id: 

project_id: 

tags:
  - 
  - 
  - 

category: 

level: 

professor_id:

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributor_names:
      - 
    reward:
```

必須フィールドは次のとおりです：

- **id** : チュートリアルを一意に識別する UUID (_Universally Unique Identifier_)。 [オンラインツール](https://www.uuidgenerator.net/version4)を使用して生成できます。 この UUID はランダムである必要があり、プラットフォーム上の他の UUID と競合しないことが条件です;

- **project_id** : チュートリアルで紹介されているツールの背後にある企業または組織の UUID [プロジェクトのリストから](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects)。 たとえば、Green Wallet ソフトウェアに関するチュートリアルを作成している場合、この `project_id` は次のファイルにあります: `bitcoin-educational-content/resources/projects/blockstream/project.yml`。 Plan ₿ Network は、Bitcoin または関連プロジェクトに取り組んでいるすべての企業および組織のデータベースを維持しているため、この情報はチュートリアルの YAML ファイルに追加されます。 チュートリアルに関連するエンティティの `project_id` を追加することで、2 つの要素間のリンクを作成できます;

- **tags** : チュートリアルの内容に関連する 2 または 3 の適切なキーワード、[Plan ₿ Network のタグリスト](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) からのみ選択可能;

- **category** : Plan ₿ Network サイトの構造に従った、チュートリアルの内容に対応するサブカテゴリ（例：ウォレットの場合：`desktop`、`hardware`、`mobile`、`backup`）;

- **level** : チュートリアルの難易度レベル、以下から選択：
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id** : [あなたの教授プロフィール](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) に表示される `professor_id` (UUID);

- **original_language** : チュートリアルの元の言語（例：`fr`、`en` など）;

- **proofreading** : 校正プロセスに関する情報。 自分自身のチュートリアルを校正することは、最初の検証としてカウントされるため、最初の部分を記入してください：
    - **language** : 校正言語のコード（例：`fr`、`en` など）。
    - **last_contribution_date** : 本日の日付。
    - **urgency** : 1
    - **contributor_names** : あなたの GitHub ID。
    - **reward** : 0

教師IDの詳細については、対応するチュートリアルを参照してください：

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
  - wallets
  - software
  - keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
  - language: fr
    last_contribution_date: 2024-11-20
    urgency: 1
    contributor_names:
      - LoicPandul
    reward: 0
```

### 5 - コンテンツを書く


- Markdownファイルのプロパティを：
    - タイトル(`name`)。
    - 短い説明 (`description`).
- Markdown構文を使用して、チュートリアルの上部にカバー画像を追加します（"green "を表示されているツールの名前に置き換えてください）：

```
![cover-green](assets/cover.webp)
```


- チュートリアルの内容をMarkdownで書く：
    - 構造化された見出し(`##`)、リスト、段落を使用する。
    - Markdown構文を使ってビジュアルを挿入する：

```
![nom-image](assets/en/001.webp)
```


- ダイアグラムと画像は、`/assets`の中の対応する言語のサブフォルダーに置いてください。

### 6 - チュートリアルを保存して送信する


- 変更をローカルに保存するには、説明的なメッセージとともにコミットを作成します。
- 変更をGitHubのフォークにプッシュする。

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- 完了したら、GitHubにPull Request (PR)を作成し、修正内容の統合を提案します。
- PRにタイトルと簡単な説明を加える。コメントには、対応する課題番号を記載してください。

### 7 - 校正とマージ


- 管理者からの検証またはフィードバックを待つ。
- 必要であれば修正し、新しいコミットをプッシュする。

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- PRがマージされたら、作業ブランチを削除することができます。

## コンテンツ作成基準


- プラットフォームでサポートされているフォーマット** ：
    - クラシックなMarkdown：リスト、リンク、画像、引用、太字、斜体など。
    - LaTeX（ブロックのみ、インライン不可）：`$$`で区切る。
    - インラインコード：シングル・バックティック付きの構文。
    - コードブロック：3つのバックスティックを持つ構文：

```
print("Hello, Bitcoin!")
```


- イラストと図** ：
    - すべての画像はWebP形式でなければなりません。必要であれば、この無料ツールを使って変換してください：[ImagesConverter](https://github.com/LoicPandul/ImagesConverter)。
    - ビジュアルに 2 桁または 3 桁の数字で名前をつけます （例：`001.webp`、`002.webp`）。
    - モバイルウォレットやハードウェアウォレットのチュートリアルには、モックアップを使いましょう。
    - 自作またはロイヤリティフリーのビジュアルのみを使用すること。
    - 関連性があり、質の高いものであることを確認してください。
- グラフィック・チャーター** ：
    - フォント：[ルービック](https://fonts.google.com/specimen/Rubik)。
    - カラーズプラン ȏ ネットワーク ：
        - オレンジ: `#FF5C00`
        - 黒: `#000000`
        - 白: `#FFFFFF`

チュートリアルの投稿に技術的な問題がある場合は、遠慮なく[投稿専用のTelegramグループ](https://t.me/PlanBNetwork_ContentBuilder)に助けを求めてください。ありがとうございました！
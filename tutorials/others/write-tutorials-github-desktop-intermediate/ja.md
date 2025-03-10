---
name: コントリビューション - GitHub Desktopを使ったチュートリアル (中級)
description: GitHub Desktop を使って Plan ₿ Network にチュートリアルを提案する完全ガイド
---
![cover](assets/cover.webp)

新しいチュートリアルの追加に関するこのチュートリアルに従う前に、いくつかの予備ステップを完了している必要があります。まだ完了していない場合は、まずこの入門チュートリアルを参照し、それからここに戻ってきてください：

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

あなたはすでにそうしている：


- チュートリアルのテーマを決める；
- Plan ₿ Networkチームに[Telegram group](https://t.me/PlanBNetwork_ContentBuilder)またはpaolo@planb.network；
- 貢献ツールを選ぶ

このチュートリアルでは、GitHub Desktop を使ってローカル環境を構築し、Plan ȋ Network にチュートリアルを追加する方法を説明します。すでに Git を使いこなしている方には、この詳細なチュートリアルは必要ないかもしれません。むしろ、このチュートリアルを参考にすることをお勧めします。このチュートリアルでは、詳細なステップバイステップのガイダンスを使わずに、主なガイドラインだけを紹介します：


- 経験豊富なユーザー

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

ローカル環境を構築したくない場合は、初心者向けの別のチュートリアルを参考にしてください。このチュートリアルでは、GitHub のウェブインターフェイスを使って直接変更を行います：


- 初心者（ウェブインターフェース）**：

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## 前提条件

このチュートリアルに従うために必要なソフトウェア：


- [GitHub Desktop](https://desktop.github.com/)；
- Obsidian](https://obsidian.md/)のようなマークダウン・ファイル・エディター；
- コードエディター（[VSC](https://code.visualstudio.com/)または[Sublime Text](https://www.sublimetext.com/)）。

![TUTO](assets/fr/01.webp)

チュートリアルを始める前の前提条件


- GitHubアカウント](https://github.com/signup)を持っている；
- Plan ₿ Networkソースリポジトリ](https://github.com/PlanB-Network/bitcoin-educational-content)をフォークしてください；
- Plan ₿ Network上の教授プロフィール](https://planb.network/professors)を持つ（完全なチュートリアルを提案する場合のみ）。

これらの前提条件の取得に助けが必要な場合は、私の他のチュートリアルがお手伝いします：

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb

すべての準備が整い、ローカル環境にプラン₿ネットワークのフォークが適切にセットアップされたら、チュートリアルの追加を開始できます。

## 1 - 新しいブランチを作る

ブラウザを開き、Plan ₿ Networkリポジトリのフォークのページに移動します。これは、GitHub で確立したフォークです。フォークのURLは以下のようになります：https://github.com/[あなたのユーザー名]/bitcoin-educational-content`：

![TUTO](assets/fr/03.webp)

メインブランチの `dev` にいることを確認してから、`Sync fork` ボタンをクリックします。フォークが最新でない場合は、GitHub がブランチの更新を提案します。更新を進めてください。逆に、あなたのブランチがすでに最新である場合は、GitHub があなたに通知します：

![TUTO](assets/fr/04.webp)

GitHub Desktopソフトウェアを開き、ウィンドウの左上でフォークが正しく選択されていることを確認します：

![TUTO](assets/fr/05.webp)

Fetch origin` ボタンをクリックします。ローカルリポジトリがすでに最新の状態であれば、GitHub Desktop は追加のアクションを提案しません。そうでない場合は、`Pull origin` オプションが表示されます。このボタンをクリックすると、ローカルリポジトリが更新されます：

![TUTO](assets/fr/06.webp)

メインブランチ `dev` にいることを確認してください：

![TUTO](assets/fr/07.webp)

このブランチをクリックし、`新規ブランチ`ボタンをクリックします：

![TUTO](assets/fr/08.webp)

新しいブランチがソースリポジトリ（`PlanB-Network/bitcoin-educational-content`）に基づいていることを確認してください。

各単語をダッシュで区切って、目的が明確になるようにタイトルをつけてください。たとえば、Sparrow Wallet の使い方のチュートリアルを書くのが目的だとしましょう。この場合、このチュートリアルを書くための作業ブランチの名前は `tuto-sparrow-wallet-loic` とします。適切な名前を入力したら、`Create branch`をクリックしてブランチの作成を確定します：

![TUTO](assets/fr/09.webp)

ここで、`Publish branch` ボタンをクリックして、新しい作業ブランチを GitHub 上のオンラインフォークに保存します：

![TUTORIAL](assets/fr/10.webp)

これで、GitHub Desktop 上で新しいブランチにいることがわかります。つまり、ローカルで行った変更はすべてこのブランチに保存されるということです。また、GitHub Desktop 上でこのブランチが選択されている間は、あなたのマシンのローカルに表示されるファイルはこのブランチ (`tuto-sparrow-wallet-loic`) のものになり、メインブランチ (`dev`) のものにはなりません。

![TUTORIAL](assets/fr/11.webp)

新しい記事を公開するたびに、`dev` から新しいブランチを作成する必要があります。Git におけるブランチとはプロジェクトの並行バージョンのことで、メインブランチに影響を与えずに変更を加えることができます。

## 2 - チュートリアルファイルの追加

作業ブランチができたので、いよいよ新しいチュートリアルを統合します。必要なドキュメントの作成を自動化する Python スクリプトを使うか、手動で各ファイルを作成するかです。それぞれのオプションの手順を説明します。

### 私のPythonスクリプトで

マシンにインストールする必要があります:
- Python 3.8 以上。

スクリプトを使用するには、保存されているフォルダに移動してください。スクリプトは Plan ₿ Network のデータリポジトリにあり、パスは次のとおりです: `bitcoin-educational-content/scripts/tutorial-related/data-creator`。

フォルダ内に移動したら、依存関係をインストールします:

```bash
pip install -r requirements.txt
```

次のコマンドを使用してソフトウェアを起動します:

```bash
python3 main.py
```

グラフィカルユーザーインターフェース（GUI）が開きます。最初の使用時には、必要な情報をすべて入力する必要がありますが、次回以降の使用時にはスクリプトが個人情報を記憶するため、再入力する必要はありません。

![DATA-CREATOR-PY](assets/fr/37.webp)

まず、クローンしたリポジトリ内の `/tutorials` フォルダへのローカルパスを入力してください（`.../bitcoin-educational-content/tutorials/`）。手動で入力するか、「Browse」ボタンをクリックしてファイルエクスプローラーで参照できます。

![DATA-CREATOR-PY](assets/fr/38.webp)

チュートリアルを作成する言語を選択してください。

![DATA-CREATOR-PY](assets/fr/39.webp)

「Contributor's GitHub ID」欄に GitHub のユーザー名を入力してください。

![DATA-CREATOR-PY](assets/fr/40.webp)

「PBN professor's ID」欄には、BIP39 リストの単語を使用して、[教授プロフィール](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors)に表示される識別子を入力してください。

![DATA-CREATOR-PY](assets/fr/41.webp)

まだ教授プロフィールを作成していない場合は、以下のチュートリアルを参照してください：

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

その後、「New Tutorial」ボタンをクリックしてください。

![DATA-CREATOR-PY](assets/fr/42.webp)

チュートリアルのメインカテゴリを選択してください。その後、選択したメインカテゴリに応じて適切なサブカテゴリを選択します。

![DATA-CREATOR-PY](assets/fr/43.webp)

チュートリアルの難易度を設定してください。

![DATA-CREATOR-PY](assets/fr/44.webp)

チュートリアル専用に作成されるディレクトリの名前を選択してください。このフォルダ名は、チュートリアルで扱うソフトウェアを反映し、単語をハイフンでつなぐ形式にしてください。たとえば、`red-wallet` というフォルダ名になります。

![DATA-CREATOR-PY](assets/fr/45.webp)

`project_id` は、チュートリアルで扱うツールを提供する企業または組織の UUID であり、[プロジェクト一覧](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects)にあります。例えば、Sparrow Wallet のチュートリアルでは、次のファイルに `project_id` が記載されています：`bitcoin-educational-content/resources/projects/sparrow/project.yml`。この情報は YAML ファイルに追加されます。Plan ₿ Network は、Bitcoin に関連する企業やプロジェクトのデータベースを管理しており、`project_id` を追加することでチュートリアルと関連組織の間にリンクを作成できます。

***更新:*** 最新版のスクリプトでは、`project_id` を手動で入力する必要がなくなりました。プロジェクト名で検索し、対応する `project_id` を自動取得できる機能が追加されました。「Project Name」欄にプロジェクト名の一部を入力すると検索でき、ドロップダウンメニューから適切な企業を選択できます。選択後、`project_id` が自動入力されます。必要に応じて手動で入力することも可能です。

![DATA-CREATOR-PY](assets/fr/46.webp)

タグを選択する際は、チュートリアルの内容に関連する 2 ～ 3 個のキーワードを、[Plan ₿ Network のタグリスト](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) から選択してください。また、検索機能を利用してキーワードを探すこともできます。

![DATA-CREATOR-PY](assets/fr/47.webp)

すべての情報を入力し、確認が完了したら、「Create Tutorial」ボタンをクリックしてチュートリアルのファイル作成を確定してください。これにより、選択したカテゴリ内にチュートリアルのフォルダおよび必要なファイルがローカルで生成されます。

![DATA-CREATOR-PY](assets/fr/48.webp)

「Python スクリプトなし」セクションおよび「YAML ファイルの記入（ステップ 3）」を省略できます。スクリプトがすでにこれらの作業を自動的に完了しているため、直接ステップ 4 に進み、チュートリアルの執筆を開始してください。

この Python スクリプトの詳細については、[README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md) を参照してください。

### Python スクリプトなしで

ファイルマネージャーを開き、リポジトリのローカルクローンである `bitcoin-educational-content` フォルダに移動します。通常、`Documents\GitHub\bitcoin-educational-content` にあります。

このディレクトリ内で、チュートリアルを配置する適切なサブフォルダを見つける必要があります。フォルダの構成は、Plan ₿ Network のウェブサイトの各セクションを反映しています。この例では、Sparrow Wallet に関するチュートリアルを追加したいので、次のパスに移動します: `bitcoin-educational-content\tutorials\wallet`。これはウェブサイト上の `WALLET` セクションに対応しています：

![TUTO](assets/fr/12.webp)

wallet`フォルダの中に、チュートリアル専用の新しいディレクトリを作成する必要があります。このフォルダの名前は、チュートリアルで扱うソフトウェアを連想させるものにします。私の例では、フォルダのタイトルは `sparrow-wallet` とします：

![TUTO](assets/fr/13.webp)

このチュートリアル専用の新しいサブフォルダに、いくつかの要素を追加する必要があります：


- assets`フォルダを作成し、チュートリアルに必要なすべてのイラストを保存します；
- この `assets` フォルダの中に、チュートリアルの元の言語コードに応じた名前のサブフォルダを作成する必要があります。例えば、チュートリアルが英語で書かれている場合、このサブフォルダは `en` という名前にする必要があります。そこにチュートリアルのすべてのビジュアル（図、画像、スクリーンショットなど）を置きます。
- チュートリアルに関する詳細を記録するために `tutorial.yml` ファイルを作成する必要があります；
- チュートリアルの実際の内容を書くために、マークダウン形式のファイルを作成する必要があります。このファイルのタイトルはチュートリアルの言語コードに従わなければなりません。例えば、フランス語で書かれたチュートリアルの場合、ファイルは `fr.md` という名前でなければなりません。

![TUTO](assets/fr/14.webp)

まとめると、作成するファイルの階層は以下のようになる：

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

## 3 - YAMLファイルを埋める

以下のテンプレートをコピーして `tutorial.yml` ファイルを埋める：

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

以下は必須項目の詳細である：


- **id**：チュートリアルを一意に識別するための UUID (_Universally Unique Identifier_) です。オンラインツール](https://www.uuidgenerator.net/version4) で生成できます。唯一の要件は、プラットフォーム上の他のUUIDとの衝突を避けるために、このUUIDがランダムであることです；
- **project_id**：チュートリアルで紹介するツールの背後にある会社または組織のUUID [プロジェクトのリストから](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects)。例えば、Sparrow Walletソフトウェアのチュートリアルを作成する場合、この`project_id`は以下のファイルにあります：bitcoin-educational-content/resources/projects/sparrow/project.yml`。この情報がチュートリアルの YAML ファイルに追加されるのは、Plan ↪Sc_20BF がビットコインや関連プロジェクトで活動しているすべての企業や組織のデータベースを管理しているからです。チュートリアルに関連するエンティティの `project_id` を追加することで、2 つの要素の間にリンクが作成されます；
- **tags**：Plan ₿ Networkのタグリストから](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md)、チュートリアルの内容に関連するキーワードを2～3個選んでください；
- **category**：カテゴリ**: Plan ȏ Networkサイトの構造に従って、チュートリアルの内容に対応するサブカテゴリ（例：財布の場合、`デスクトップ`、`ハードウェア`、`モバイル`、`バックアップ`）；
- **level**：チュートリアルの難易度：
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**：あなたの教授プロフィール](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors)に表示されているあなたの`contributor_id` (BIP39ワード)；
- **original_language**：チュートリアルの元の言語 (例 `fr`、`en` など)；
- **proofreading**：校正プロセスに関する情報。自分自身のチュートリアルの校正は最初の検証としてカウントされますので、最初の部分を記入してください：
    - **language**：校正の言語コード（例えば `fr`、`en` など）。
    - **last_contribution_date**：今日の日付。
    - **urgency**：空欄のまま
    - **contributors_id**：あなたの GitHub ID。
    - **reward**：空白のままにする。

教授識別子の詳細については、対応するチュートリアルを参照してください：

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

以下は、Blockstream Green ウォレットのチュートリアル用に完成した `tutorial.yml` ファイルの例です：

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
name: [タイトル］
description: 説明
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
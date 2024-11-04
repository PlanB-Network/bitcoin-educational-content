---
name: 教育ツールの追加
description: PlanBネットワークに新しい教育資料をどのように追加するか？
---
![event](assets/cover.webp)

PlanBのミッションは、できるだけ多くの言語でBitcoinに関する最先端の教育リソースを提供することです。サイトに公開されているすべてのコンテンツはオープンソースであり、GitHub上でホストされているため、誰でもプラットフォームを豊かにするために参加することができます。

チュートリアルやトレーニングを超えて、PlanBネットワークは、誰もがアクセスできるBitcoinに関する多様な教育コンテンツの広大なライブラリも提供しています。これは、[「BET」(_Bitcoin Educational Toolkit_)セクション](https://planb.network/resources/bet)でアクセスできます。このデータベースには、教育用ポスター、ミーム、ユーモラスなプロパガンダポスター、技術図、ロゴ、およびユーザー向けのその他のツールが含まれています。この取り組みの目的は、世界中でBitcoinを教える個人やコミュニティを、必要な視覚資源を提供することによって支援することです。

このデータベースを豊かにすることに参加したいですが、どうすればいいかわかりませんか？このチュートリアルはあなたのためです！

*サイトに統合されるすべてのコンテンツは、権利がないか、またはソースファイルのライセンスを尊重する必要があります。また、PlanBネットワークで公開されるすべてのビジュアルは、[CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/)ライセンスの下で利用可能になります。*
![event](assets/01.webp)
- まず、GitHubアカウントを持っている必要があります。アカウントの作成方法がわからない場合は、詳細なチュートリアルを用意しています。

https://planb.network/tutorials/others/create-github-account


- `resources/bet/`セクションの[PlanB専用のGitHubリポジトリ](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet)に移動します：
![event](assets/02.webp)
- 右上の`Add file`ボタンをクリックし、次に`Create new file`をクリックします：
![event](assets/03.webp)
- 以前にPlanBネットワークのコンテンツに貢献したことがない場合は、元のリポジトリのフォークを作成する必要があります。リポジトリをフォークするとは、そのリポジトリのコピーを自分のGitHubアカウントに作成することを意味し、元のリポジトリに影響を与えることなくプロジェクトに取り組むことができます。`Fork this repository`ボタンをクリックします：
![event](assets/04.webp)
- その後、GitHubの編集ページに到着します：
![event](assets/05.webp)
- コンテンツ用のフォルダを作成します。これを行うには、`Name your file...`ボックスに、スペースの代わりにダッシュを使用して小文字でコンテンツの名前を書きます。私の例では、2048語のBIP39リストのPDFビジュアルを追加したいとします。したがって、フォルダを`bip39-wordlist`と呼びます： ![event](assets/06.webp)
- フォルダの作成を確認するには、同じボックスの名前の後にスラッシュを追加するだけです。例：`bip39-wordlist/`。スラッシュを追加すると、ファイルではなくフォルダが自動的に作成されます：
![event](assets/07.webp)
- このフォルダ内に、`bet.yml`という名前の最初のYAMLファイルを作成します：
![event](assets/08.webp)
- このテンプレートを使用して、関連するコンテンツの情報をファイルに記入します：

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```

各フィールドに記入する詳細は次のとおりです：
```yaml
builder: 組織の識別子をPlanB Network上で指定します。もしまだ会社用の「builder」識別子を持っていない場合は、このチュートリアルに従って作成することができます。

https://planb.network/tutorials/others/add-builder

もし持っていない場合は、builderプロファイルを作成せずに、あなたの名前、偽名、または会社の名前をそのまま使用できます。
type: コンテンツの性質を以下の二つのオプションから選択してください：
  - `Educational Content` 教育コンテンツ用。
  - `Visual Content` その他様々なタイプのコンテンツ用。

links: コンテンツへのリンクを提供してください。二つのオプションがあります：
  - PlanBのGitHub上に直接コンテンツをホストする場合は、次のステップでこのファイルへのリンクを追加する必要があります。
  - コンテンツが個人のウェブサイトなど他の場所にホストされている場合は、ここに該当するリンクを示してください：
      - `download`: コンテンツをダウンロードするためのリンク。
      - `view`: コンテンツを閲覧するためのリンク（ダウンロードリンクと同じでも構いません）。コンテンツが複数の言語で利用可能な場合は、各言語のリンクを追加してください。

tags: コンテンツに関連する二つのタグを追加してください。例：
  - bitcoin
  - technology
  - economy
  - education
  - meme...

contributors: もし貢献者識別子を持っている場合は、それを記載してください。

例えば、あなたのYAMLファイルは以下のようになるかもしれません：

```yaml
builder: PlanB-Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- この例では、PDFを直接GitHubに追加するため、リンクは一時的に空のままにします：
![event](assets/09.webp)
- このファイルへの変更が完了したら、`Commit changes...`ボタンをクリックして保存します：
![event](assets/10.webp)
- 変更のタイトルと短い説明を追加します：
![event](assets/11.webp)
- 緑色の`Propose changes`ボタンをクリックします：
![event](assets/12.webp)
- そうすると、あなたの変更をまとめたページに到着します：
![event](assets/13.webp)
- 右上のGitHubプロフィール画像をクリックし、`Your Repositories`を選択します：
![event](assets/14.webp)
- PlanB Networkリポジトリのフォークを選択します：
![event](assets/15.webp)
- 新しいブランチに関する通知がウィンドウの上部に表示されるはずです。おそらく`patch-1`と呼ばれています。それをクリックします：
![event](assets/16.webp)
- これで、作業ブランチにいます（**以前の変更と同じブランチにいることを確認してください、これは重要です！**）：
![event](assets/17.webp)
- `resources/bet/`フォルダに戻り、前のコミットで作成したコンテンツのフォルダを選択します：
![event](assets/18.webp)
- コンテンツのフォルダ内で、`Add file`ボタンをクリックし、`Create new file`を選択します：
![event](assets/19.webp)
- この新しいフォルダに`assets`と名付け、スラッシュ`/`を末尾に付けてその作成を確認します：
![event](assets/20.webp)
- この`assets`フォルダ内に、`.gitkeep`という名前のファイルを作成します： ![event](assets/21.webp)
```
- `Commit changes...` ボタンをクリックしてください: ![event](assets/22.webp) - コミットタイトルはデフォルトのままにし、`Commit directly to the patch-1 branch` ボックスがチェックされていることを確認した後、`Commit changes` をクリックしてください: ![event](assets/23.webp)
- `assets` フォルダに戻ってください: ![event](assets/24.webp)
- `Add file` ボタンをクリックし、次に `Upload files` を選択してください: ![event](assets/25.webp)
- 新しいページが開きます。コンテンツを代表するサムネイルをエリアにドラッグアンドドロップしてください。この画像はPlanB Networkサイトに表示されます: ![event](assets/26.webp)
- プレビュー、ロゴ、またはアイコンが可能です: ![event](assets/27.webp)
- 画像がアップロードされたら、`Commit directly to the patch-1 branch` ボックスがチェックされていることを確認し、`Commit changes` をクリックしてください: ![event](assets/28.webp)
- 注意してください、画像は `logo` と命名され、`.webp` 形式でなければなりません。完全なファイル名は次のようになります: `logo.webp`: ![event](assets/29.webp)
- `assets` フォルダに戻り、中間ファイル `.gitkeep` をクリックしてください: ![event](assets/30.webp)
- ファイル上で、右上の三つの小さな点をクリックし、次に `Delete file` を選択してください: ![event](assets/31.webp)
- 同じ作業ブランチ上にまだいることを確認し、`Commit changes` ボタンをクリックしてください: ![event](assets/32.webp)
- コミットにタイトルと説明を追加し、`Commit changes` をクリックしてください: ![event](assets/33.webp)
- コンテンツのフォルダに戻ってください: ![event](assets/34.webp)
- `Add file` ボタンをクリックし、`Create new file` を選択してください: ![event](assets/35.webp)
- 母国語の指標を使用して名前を付けることで、新しいYAMLファイルを作成してください。このファイルはコンテンツの説明に使用されます。例えば、私が説明を英語で書きたい場合、このファイルには `en.yml` と名付けます: ![event](assets/36.webp)
- このテンプレートを使用してYAMLファイルを記入してください:

```yaml
name: 
description: |
  
```

- `name` キーには、コンテンツの名前を追加できます。
- `description` キーには、コンテンツを簡単に説明する短い段落を追加するだけです。説明はファイル名と同じ言語でなければなりません。この説明をサイトでサポートされているすべての言語に翻訳する必要はありません。PlanBチームがモデルを使用して行います。
例えば、あなたのファイルは次のようになるかもしれません:

```yaml
name: BIP39 WORDLIST
description: |
  BIP39辞書からの2048の英語の単語の完全かつ番号付きリストで、ニーモニックフレーズをエンコードするために使用されます。このドキュメントは1ページに印刷することができます。
```

![event](assets/37.webp)
- `Commit changes...` ボタンをクリックしてください:
![event](assets/38.webp)
- `Commit directly to the patch-1 branch` ボックスがチェックされていることを確認し、タイトルを追加してから `Commit changes` をクリックしてください:
![event](assets/39.webp)
- あなたのコンテンツフォルダは、今このように見えるはずです:
![event](assets/40.webp)
GitHubにコンテンツを追加したくない場合、または以前の手順で`bet.yml`ファイルにリンクを記載している場合は、このセクションをスキップして、Pull Requestの作成に関する部分に直接進むことができます。
- `/assets`フォルダに戻ります：
![イベント](assets/41.webp)
- `Add file`ボタンをクリックし、次に`Upload files`をクリックします：
![イベント](assets/42.webp)
- 新しいページが開きます。共有したいコンテンツをエリアにドラッグ＆ドロップします：
![イベント](assets/43.webp)
- 例えば、BIP39リストのPDFファイルを追加しました：
![イベント](assets/44.webp)
- コンテンツがアップロードされたら、`Commit directly to the patch-1 branch`ボックスがチェックされていることを確認し、`Commit changes`をクリックします：
![イベント](assets/45.webp)
- `/assets`フォルダに戻り、アップロードしたばかりのファイルをクリックします：
![イベント](assets/46.webp)
- ファイルの中間URLを取得します。例えば、私の場合、URLは以下の通りです：

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- URLの`/resources`以降の部分のみを保持します：

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- 正しいリンクを得るために、以下の情報をURLのベースに追加します：

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

ここで行っていることは、提案がPlanB Networkのソースリポジトリにマージされた後のファイルへの将来のリンクを予測しています。
- `bet.yml`ファイルに戻り、鉛筆アイコンをクリックします： ![イベント](assets/47.webp)
- そこにリンクを追加します：
![イベント](assets/48.webp)
- 変更が完了したら、`Commit changes...`ボタンをクリックします：
![イベント](assets/49.webp)
- 変更のタイトルと短い説明を追加します：
![イベント](assets/50.webp)
- 緑色の`Commit changes`ボタンをクリックします：
![イベント](assets/51.webp)

---

- すべてが良さそうに見える場合は、フォークのルートに戻ります：
![イベント](assets/52.webp)
- ブランチが変更されたことを示すメッセージが表示されるはずです。`Compare & pull request`ボタンをクリックします：
![イベント](assets/53.webp)
- PRに明確なタイトルと説明を追加します：
![イベント](assets/54.webp)
- `Create pull request`ボタンをクリックします：
![イベント](assets/55.webp)
おめでとうございます！PRは正常に作成されました。管理者がこれをレビューし、すべてが順序どおりであれば、PlanB Networkのメインリポジトリにマージします。数日後には、ウェブサイト上であなたのBETが表示されるはずです。

PRの進行状況をフォローしてください。管理者が追加情報を求めるコメントを残すことがあります。PRが承認されるまで、PlanB Network GitHubリポジトリのPull requestsタブでそれを確認することができます：
![イベント](assets/56.webp)
貴重な貢献をいただき、誠にありがとうございます！ :)

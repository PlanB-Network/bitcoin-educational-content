---
name: PlanBネットワークに本を追加する
description: PlanBネットワークに新しい本をどのように追加しますか？
---
![book](assets/cover.webp)

PlanBのミッションは、可能な限り多くの言語でビットコインに関する最高級の教育リソースを提供することです。サイトに公開されているすべてのコンテンツはオープンソースであり、GitHub上でホストされているため、誰でもプラットフォームの充実に貢献することができます。

**PlanBネットワークサイトにビットコインに関連する本を追加して、あなたの作品の可視性を高めたいですが、方法がわからないですか？このチュートリアルはあなたのためです！**
![book](assets/01.webp)
- まず、GitHubアカウントを持っている必要があります。アカウントの作成方法がわからない場合は、詳細なチュートリアルを用意しています。

https://planb.network/tutorials/others/create-github-account


- `resources/books/`セクションにある[PlanB専用のデータGitHubリポジトリ](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books)にアクセスしてください：
![book](assets/02.webp)
- 右上の`Add file`ボタンをクリックし、次に`Create new file`をクリックします：
![book](assets/03.webp)
- 以前にPlanB Networkのコンテンツに貢献したことがない場合は、元のリポジトリのフォークを作成する必要があります。リポジトリをフォークするとは、そのリポジトリのコピーを自分のGitHubアカウント上に作成することを意味し、元のリポジトリに影響を与えることなくプロジェクトに取り組むことができます。`Fork this repository`ボタンをクリックしてください：
![book](assets/04.webp)
- そうすると、GitHubの編集ページに到着します：
![book](assets/05.webp)
- 本のためのフォルダを作成します。これを行うには、`Name your file...`ボックスに、スペースの代わりにダッシュを使用して本の名前を小文字で記入します。例えば、あなたの本が"*My Bitcoin Book*"と呼ばれている場合は、`my-bitcoin-book`と記入する必要があります：
![book](assets/06.webp)
- フォルダの作成を確定するには、同じボックスで本の名前の後にスラッシュを追加します。例えば：`my-bitcoin-book/`。スラッシュを追加すると、ファイルではなくフォルダが自動的に作成されます：
![book](assets/07.webp)
- このフォルダ内に、最初のYAMLファイル`book.yml`を作成します：
![book](assets/08.webp)
- このテンプレートを使用して、本に関する情報をファイルに記入します：

```yaml
author: 
level: 
tags:
  - 
  - 
```

各フィールドに記入する詳細は以下の通りです：
- **`author`**: 本の著者の名前を記載してください。
- **`level`**: 本をよく理解するために必要なレベルを示してください。以下の中からレベルを選択してください：
	- `beginner`
	- `intermediate`
- `advanced` - `expert`
- **`tags`**: 本に関連する2つまたは3つのタグを追加してください。例えば：
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`...

例えば、あなたのYAMLファイルはこのようになるかもしれません：

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![book](assets/09.webp)
- このファイルへの変更を終えたら、`Commit changes...`ボタンをクリックして保存します：
![book](assets/10.webp)
- 変更にタイトルと短い説明を追加してください：![book](assets/11.webp)
- 緑色の「Propose changes」ボタンをクリックします：![book](assets/12.webp)
- そうすると、あなたの変更のすべてをまとめたページに到着します：![book](assets/13.webp)
- 右上にあるあなたのGitHubプロフィール画像をクリックし、次に「Your Repositories」をクリックします：![book](assets/14.webp)
- PlanB Networkリポジトリのあなたのフォークを選択します：![book](assets/15.webp)
- 新しいブランチであなたの通知がウィンドウの上部に表示されるはずです。それはおそらく「patch-1」と呼ばれています。それをクリックします：![book](assets/16.webp)
- これで、作業中のブランチにいます：![book](assets/17.webp)
- `resources/books/`フォルダに戻り、前のコミットで作成したあなたの本のフォルダを選択します：![book](assets/18.webp)
- あなたの本のフォルダ内で、「Add file」ボタンをクリックし、次に「Create new file」をクリックします：![book](assets/19.webp)
- この新しいフォルダに「assets」と名付け、スラッシュ「/」を末尾に付けてその作成を確認します：![book](assets/20.webp)
- この`assets`フォルダ内に、`.gitkeep`という名前のファイルを作成します：![book](assets/21.webp)
- 「Commit changes...」ボタンをクリックします：![book](assets/22.webp)
- コミットタイトルをデフォルトのままにし、「Commit directly to the patch-1 branch」ボックスがチェックされていることを確認し、次に「Commit changes」をクリックします：![book](assets/23.webp)
- `assets`フォルダに戻ります：![book](assets/24.webp)
- 「Add file」ボタンをクリックし、次に「Upload files」をクリックします：![book](assets/25.webp)
- 新しいページが開きます。あなたの本の表紙画像をエリアにドラッグアンドドロップします。この画像はPlanB Networkサイトに表示されます：![book](assets/26.webp)
- 注意してください、画像は本の形式でなければならず、私たちのウェブサイトに最適に適応するように、例えばこのようになります：![book](assets/27.webp)
- 画像がアップロードされたら、「Commit directly to the patch-1 branch」ボックスがチェックされていることを確認し、「Commit changes」をクリックします：![book](assets/28.webp)- 画像は英語の表紙の場合は`cover_en`と名付けられていなければならず、`.webp`形式でなければなりません。したがって、完全なファイル名は`cover_en.webp`、`cover_fr.webp`、`cover_it.webp`などになります。本の翻訳など、各言語で異なる表紙画像を使用したい場合は、`assets`フォルダの同じ場所に配置できます：![book](assets/29.webp)
- `assets`フォルダに戻り、`.gitkeep`の中間ファイルをクリックします：![book](assets/30.webp)
- ファイル上にいるとき、右上の3つの小さな点をクリックし、次に「Delete file」をクリックします：![book](assets/31.webp)
- 同じ作業ブランチにまだいることを確認し、「Commit changes...」ボタンをクリックします：![book](assets/32.webp)
- コミットにタイトルと説明を追加し、「Commit changes」をクリックします：![book](assets/33.webp)
- あなたの本のフォルダに戻ります：![book](assets/34.webp)
- `Add file` ボタンをクリックし、その後 `Create new file` をクリックします：
![book](assets/35.webp)
- 本の言語インディケーターを使って命名し、新しいYAMLファイルを作成します。このファイルは本の説明に使用されます。例えば、私が英語で説明を書きたい場合、このファイルには `en.yml` と名付けます：
![book](assets/36.webp)
- このテンプレートを使用してYAMLファイルを記入します：
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

各フィールドに記入する詳細は以下の通りです：
- **`title`**: 本の名前を引用符で示します。
- **`publication_year`**: 本が出版された年を示します。
- **`cover`**: 現在編集しているYAMLファイルの言語に応じたカバー画像のファイル名を示します。例えば、`en.yml` ファイルを編集していて、以前に英語のカバー画像 `cover_en.webp` を追加していた場合、このフィールドには単に `cover_en.webp` を指定します。
- **`description`**: 本を短い段落で説明します。説明はYAMLファイルのタイトルに示された言語と同じ言語でなければなりません。
- **`contributors`**: コントリビューターIDがある場合は追加します。

例えば、あなたのYAMLファイルはこのようになるかもしれません：

```yaml
title: "My Bitcoin Book"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
ビットコインの画期的な世界をこの包括的なガイドで発見してください。My Bitcoin Bookは、ビットコインの複雑さを解き明かし、プロトコルがどのように機能するかについて明確で簡潔な紹介を提供します。その革命的な技術から世界経済への潜在的な影響まで、この本は貴重な洞察と実用的な知識を提供します。ビットコインの初心者に最適で、基本、セキュリティのヒント、デジタルファイナンスの未来についてカバーしています。お金の未来に飛び込み、デジタル時代を自信を持ってナビゲートするための知識を身につけましょう。

contributors:
  - pretty-private

![book](assets/37.webp)
- `Commit changes...` ボタンをクリックします：
![book](assets/38.webp)
- `Commit directly to the patch-1 branch` ボックスがチェックされていることを確認し、タイトルを追加してから `Commit changes` をクリックします：
![book](assets/39.webp)
- 本のフォルダはこれで以下のようになるはずです：
![book](assets/40.webp)
- すべてが良さそうに見える場合は、フォークのルートに戻ります：
![book](assets/41.webp)
- ブランチが変更されたことを示すメッセージが表示されるはずです。`Compare & pull request` ボタンをクリックします：
![book](assets/42.webp)
- PRに明確なタイトルと説明を追加します：
![book](assets/43.webp)
- `Create pull request` ボタンをクリックします：
![book](assets/44.webp)
おめでとうございます！あなたのPRは正常に作成されました。管理者が今後レビューし、すべてが順調であれば、PlanB Networkのメインリポジトリにマージされます。数日後には、あなたの本がウェブサイトに表示されるはずです。

PRの進行状況を確認してください。管理者が追加情報を求めるコメントを残すことがあります。PRが承認されない限り、PlanB NetworkのGitHubリポジトリの `Pull requests` タブでそれを見ることができます。
熟練したプロの翻訳者として、あなたの主な任務は、英語から母国語である日本語への技術コンテンツの正確な翻訳です。以下のガイドラインに従って、高品質な翻訳を行ってください。

元の言語：コンテンツはもともと英語で書かれています。
コンテンツの性質：業界固有の専門用語を含む可能性のある技術的な資料に出会うことになります。
リンクと技術用語：URLや非常に特定の技術用語は翻訳しないでください。不確かな場合は、元の用語を保持してください。
書式の一貫性：元のテキストと同じマークダウンのレイアウトと書式を維持してください。構造の一貫性が重要です。
YMLプロパティ：行がYAMLプロパティ（例：「name:」、「goal:」、「objectives:」）で始まる場合は、プロパティ名を英語で保持してください。
文化的な文脈：直接翻訳できない文化的な参照や文脈に関連するものについては、意図した意味を保持するために言い換えるか、簡単な説明を提供してください。
重点は、技術コンテンツの完全性を保ちつつ、日本語で理解可能で文脈に即した正確な翻訳を行うことです。

![book](assets/45.webp) 貴重なご貢献をいただき、誠にありがとうございます！ :)

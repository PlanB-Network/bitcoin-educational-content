---
name: ビルダーの追加
description: PlanB Networkに新しいビルダーを提案する方法は？
---
![builder](assets/cover.webp)

PlanBのミッションは、できるだけ多くの言語でBitcoinに関する最高級の教育リソースを提供することです。サイトに公開されているすべてのコンテンツはオープンソースであり、GitHubにホストされているため、誰でもプラットフォームを豊かにするために参加することができます。

あなたの会社やソフトウェアに可視性を与えるために、PlanB Networkサイトに新しいBitcoin "ビルダー"を追加したいですか？しかし、どのようにすればよいかわかりませんか？このチュートリアルはあなたのためのものです！
![builder](assets/01.webp)
- まず、GitHubアカウントを持っている必要があります。アカウントの作成方法がわからない場合は、詳細なチュートリアルを用意しています。

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- `resources/builder/`セクションにある[PlanB専用のデータGitHubリポジトリ](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders)にアクセスしてください：
![builder](assets/02.webp)
- 右上の`Add file`ボタンをクリックし、次に`Create new file`をクリックします：
![builder](assets/03.webp)
- 以前にPlanB Networkのコンテンツに貢献したことがない場合は、元のリポジトリのフォークを作成する必要があります。リポジトリをフォークするとは、そのリポジトリのコピーを自分のGitHubアカウント上に作成することを意味し、元のリポジトリに影響を与えることなくプロジェクトに取り組むことができます。`Fork this repository`ボタンをクリックしてください：
![builder](assets/04.webp)
- そうすると、GitHubの編集ページに到着します：
![builder](assets/05.webp)
- 会社のためのフォルダを作成します。これを行うには、`Name your file...`ボックスに、スペースの代わりにダッシュを使用して、会社の名前を小文字で書きます。例えば、会社が"Bitcoin Baguette"と呼ばれている場合は、`bitcoin-baguette`と書くべきです：
![builder](assets/06.webp)
- フォルダの作成を確定するには、同じボックスで名前の後にスラッシュを追加するだけです。例：`bitcoin-baguette/`。スラッシュを追加すると、ファイルではなくフォルダが自動的に作成されます：
![builder](assets/07.webp)
- このフォルダ内に、最初のYAMLファイル`builder.yml`を作成します：
![builder](assets/08.webp)
- このテンプレートを使用して、会社に関する情報をこのファイルに記入してください：

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

各キーに何を記入するか：
- `name`: 会社の名前（必須）;
- `address` : 事業所の所在地（任意）;
- `language` : 事業が運営されている国またはサポートされている言語（任意）;
- `links` : 事業の各種公式リンク（任意）;
- `tags` : 事業を特徴づける2つの用語（必須）;
- `category` : 事業が運営されている分野を最もよく表すカテゴリー。以下の選択肢から選んでください：
	- `wallet`,
	- `infrastructure`,
	- `exchange`,
	- `education`,
	- `service`,
	- `communities`,
	- `conference`,
	- `privacy`,
	- `investment`,
	- `node`,
	- `mining`,
	- `news`,
	- `manufacturer`.
例として、あなたのYAMLファイルは以下のようになるかもしれません：
```yaml
name: Bitcoin Baguette

address_line_1: パリ, フランス
address_line_2:
address_line_3: 

language:
  - fr
  - en

links:
  website: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tags:
  - bitcoin
  - education

category: education
```

![builder](assets/09.webp)
- このファイルに変更を加え終わったら、`Commit changes...` ボタンをクリックして保存してください：
![builder](assets/10.webp)
- 変更のタイトルと短い説明を追加してください：
![builder](assets/11.webp)
- 緑色の `Propose changes` ボタンをクリックしてください：
![builder](assets/12.webp)
- そうすると、あなたの変更の要約が表示されるページに移動します：
![builder](assets/13.webp)
- 右上のGitHubプロフィール画像をクリックし、`Your Repositories` を選択してください：
![builder](assets/14.webp)
- PlanB Networkリポジトリのフォークを選択してください：
![builder](assets/15.webp)
- 新しいブランチに関する通知がウィンドウの上部に表示されるはずです。恐らく `patch-1` と呼ばれています。それをクリックしてください：
![builder](assets/16.webp)
- これで、作業ブランチにいます（**以前の変更と同じブランチにいることを確認してください、これは重要です！**）：
![builder](assets/17.webp)
- `resources/builders/` フォルダに戻り、前のコミットで作成したビジネスのフォルダを選択してください：
![builder](assets/18.webp)
- ビジネスのフォルダ内で、`Add file` ボタンをクリックし、`Create new file` を選択してください：
![builder](assets/19.webp)
- この新しいフォルダに `assets` と名付け、スラッシュ `/` を末尾に付けてその作成を確認してください：
![builder](assets/20.webp)
- この `assets` フォルダ内に `.gitkeep` というファイルを作成してください：
![builder](assets/21.webp)
- `Commit changes...` ボタンをクリックしてください：
![builder](assets/22.webp)
- コミットタイトルはデフォルトのままにし、`Commit directly to the patch-1 branch` ボックスがチェックされていることを確認し、`Commit changes` をクリックしてください： ![builder](assets/23.webp)
- `assets` フォルダに戻ってください：
![builder](assets/24.webp)
- `Add file` ボタンをクリックし、`Upload files` を選択してください：
![builder](assets/25.webp)
- 新しいページが開きます。あなたの会社やソフトウェアの画像をエリアにドラッグアンドドロップしてください。この画像はPlanB Networkサイトに表示されます：
![builder](assets/26.webp)
- ロゴまたはアイコンでも構いません：
![builder](assets/27.webp)
- 画像がアップロードされたら、`Commit directly to the patch-1 branch` ボックスがチェックされていることを確認し、`Commit changes` をクリックしてください：
![builder](assets/28.webp)
- 注意してください、画像は正方形でなければならず、`logo` と名付けられ、`.webp` 形式である必要があります。完全なファイル名は次のようになります：`logo.webp`：
![builder](assets/29.webp)
- `assets` フォルダに戻り、`.gitkeep` 中間ファイルをクリックしてください：
ファイル上にいるときは、右上の三つの小さな点をクリックし、その後`Delete file`をクリックしてください：
![builder](assets/31.webp)
- 作業中のブランチが同じであることを確認し、その後`Commit changes`ボタンをクリックしてください：
![builder](assets/32.webp)
- コミットにタイトルと説明を追加し、その後`Commit changes`をクリックしてください：
![builder](assets/33.webp)
- あなたの会社のフォルダに戻ってください：
![builder](assets/34.webp)
- `Add file`ボタンをクリックし、その後`Create new file`を選択してください：
![builder](assets/35.webp)
- あなたの母国語の指標を使って名前を付けることで、新しいYAMLファイルを作成してください。このファイルはビルダーの説明に使用されます。例えば、私が英語で説明を書きたい場合、このファイルには`en.yml`と名付けます：
![builder](assets/36.webp)
- このテンプレートを使用してYAMLファイルを記入してください：
```yaml
description: |
 
contributors:
 - 
```

- `contributors`キーには、PlanB Networkに貢献者識別子がある場合はそれを追加できます。ない場合は、このフィールドを空にしてください。
- `description`キーには、あなたの会社またはソフトウェアを簡単に説明する短い段落を追加するだけです。説明はファイル名と同じ言語でなければなりません。この説明をサイトでサポートされているすべての言語に翻訳する必要はありません。PlanBチームがそのモデルを使用して行います。例えば、あなたのファイルがどのように見えるかはこちらです：
```yaml
description: |
2017年に設立されたBitcoin Baguetteは、ビットコインのミートアップと技術ワークショップを主催するパリに拠点を置く団体です。私たちは、熱心な人々、専門家、そして好奇心旺盛な心を集め、ビットコイン技術の複雑さを探求し議論します。私たちのイベントは、知識共有、ネットワーキング、そしてビットコインの内部機能のより深い理解を促進するプラットフォームを提供します。パリのビットコインコミュニティの一員として、そしてこの分野の最新の進歩に更新されたままでいるために、Bitcoin Baguetteに参加してください。

contributors:
- 
```
![builder](assets/37.webp)
- `Commit changes`ボタンをクリックしてください：
![builder](assets/38.webp)
- `Commit directly to the patch-1 branch`ボックスがチェックされていることを確認し、タイトルを追加してから`Commit changes`をクリックしてください：
![builder](assets/39.webp)
- あなたの会社のフォルダは、これで以下のようになるはずです：
![builder](assets/40.webp)
- すべてがご満足いただける場合は、フォークのルートに戻ってください：
![builder](assets/41.webp)
- ブランチに変更があったことを示すメッセージが表示されるはずです。`Compare & pull request`ボタンをクリックしてください：
![builder](assets/42.webp)
- PRに明確なタイトルと説明を追加してください：
![builder](assets/43.webp)
- `Create pull request`ボタンをクリックしてください：
![builder](assets/44.webp)
おめでとうございます！あなたのPRは正常に作成されました。管理者が今後レビューし、すべてが順調であれば、PlanB Networkのメインリポジトリに統合されます。数日後には、あなたのビルダープロファイルがウェブサイトに表示されるはずです。

PRの進捗状況をフォローしてください。管理者が追加情報を求めるコメントを残すことがあります。PRが承認されるまで、PlanB Network GitHubリポジトリの`Pull requests`タブでそれを確認することができます：
![builder](assets/45.webp)
貴重な貢献をいただき、誠にありがとうございます！ :)

---
name: コンファレンスリプレイの追加
description: PlanB Networkにコンファレンスのリプレイを追加する方法は？
---
![conference](assets/cover.webp)

PlanBのミッションは、できるだけ多くの言語でBitcoinに関する最高水準の教育リソースを提供することです。サイトに公開されるすべてのコンテンツはオープンソースであり、GitHubにホストされているため、誰でもプラットフォームの充実に貢献することができます。

PlanB NetworkサイトにあなたのBitcoinコンファレンスのリプレイを追加して、このイベントに可視性を与えたいけれど、どうすればいいかわからないですか？このチュートリアルはあなたのためのものです！

しかし、将来行われるコンファレンスを追加したい場合は、サイトに新しいイベントを追加する方法を説明するこの他のチュートリアルを読むことをお勧めします。

https://planb.network/tutorials/others/contribution/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)
- まず、GitHubにアカウントを持っている必要があります。アカウントの作成方法がわからない場合は、ガイドする詳細なチュートリアルを作成しました。

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- `resources/conference/`セクションで[PlanBに専用のデータのGitHubリポジトリ](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference)にアクセスしてください：
![conference](assets/02.webp)
- 右上の`Add file`ボタンをクリックし、次に`Create new file`をクリックします：
![conference](assets/03.webp)
- 以前にPlanB Networkのコンテンツに貢献したことがない場合は、元のリポジトリのフォークを作成する必要があります。リポジトリをフォークするとは、そのリポジトリのコピーを自分のGitHubアカウント上に作成することを意味し、元のリポジトリに影響を与えることなくプロジェクトに取り組むことができます。`Fork this repository`ボタンをクリックします：
![conference](assets/04.webp)
- そうすると、GitHubの編集ページに到着します：
![conference](assets/05.webp)
- コンファレンス用のフォルダを作成します。これを行うには、`Name your file...`ボックスに、スペースの代わりにダッシュを使用してコンファレンスの名前を小文字で記入します。例えば、コンファレンスが「Paris Bitcoin Conference」と呼ばれている場合は、`paris-bitcoin-conference`と記載する必要があります。また、コンファレンスの年も追加します。例：`paris-bitcoin-conference-2024`：
![conference](assets/06.webp)
- フォルダの作成を確定するには、同じボックスで名前の後にスラッシュを記載します。例：`paris-bitcoin-conference-2024/`。スラッシュを追加すると、ファイルではなくフォルダが自動的に作成されます：
![conference](assets/07.webp)
- このフォルダ内に、`conference.yml`という名前の最初のYAMLファイルを作成します：
![conference](assets/08.webp)
このテンプレートを使用して、コンファレンスに関連する情報をこのファイルに記入します：
```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

例えば、あなたのYAMLファイルは次のようになるかもしれません：

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - International
  - All Public
```

![conference](assets/09.webp)
もしまだお使いの組織に"*builder*"識別子がない場合は、この他のチュートリアルに従って追加することができます。
https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

- このファイルへの変更が完了したら、`Commit changes...`ボタンをクリックして保存してください：
![conference](assets/10.webp)
- 変更のタイトルと短い説明を追加してください：
![conference](assets/11.webp)
- 緑色の`Propose changes`ボタンをクリックしてください：
![conference](assets/12.webp)
- そうすると、あなたの変更のすべてをまとめたページに到着します：
![conference](assets/13.webp)
- 右上のGitHubプロフィール画像をクリックし、`Your Repositories`を選択してください：
![conference](assets/14.webp)
- PlanB Networkリポジトリのフォークを選択してください：
![conference](assets/15.webp)
- 新しいブランチに関する通知がウィンドウの上部に表示されるはずです。おそらく`patch-1`と呼ばれています。それをクリックしてください：
![conference](assets/16.webp)
- これで、作業ブランチにいます：
![conference](assets/17.webp)
- `resources/conference/`フォルダに戻り、前のコミットで作成したあなたのカンファレンスのフォルダを選択してください：
![conference](assets/18.webp)
- あなたのカンファレンスのフォルダ内で、`Add file`ボタンをクリックし、`Create new file`を選択してください：
![conference](assets/19.webp)
- この新しいフォルダに`assets`と名付け、スラッシュ`/`を末尾に付けてその作成を確認してください：
![conference](assets/20.webp)
- この`assets`フォルダ内に、`.gitkeep`という名前のファイルを作成してください：
![conference](assets/21.webp)
- `Commit changes...`ボタンをクリックしてください：
![conference](assets/22.webp)
- コミットタイトルはデフォルトのままにし、`Commit directly to the patch-1 branch`ボックスがチェックされていることを確認し、`Commit changes`をクリックしてください：
![conference](assets/23.webp)
- `assets`フォルダに戻ってください：
![conference](assets/24.webp)
- `Add file`ボタンをクリックし、`Upload files`を選択してください：
![conference](assets/25.webp)
- 新しいページが開きます。PlanB Networkサイトに表示されるあなたのカンファレンスを代表する画像をドラッグアンドドロップしてください： ![conference](assets/26.webp)
- それはロゴ、サムネイル、またはポスターでも構いません：
![conference](assets/27.webp)
- 画像がアップロードされたら、`Commit directly to the patch-1 branch`ボックスがチェックされていることを確認し、`Commit changes`をクリックしてください：
![conference](assets/28.webp)
- 注意してください、あなたの画像は`thumbnail`と名付けられ、`.webp`形式でなければなりません。したがって、完全なファイル名は`thumbnail.webp`であるべきです：
![conference](assets/29.webp)
- `assets`フォルダに戻り、`.gitkeep`中間ファイルをクリックしてください：
![conference](assets/30.webp)
- ファイル上にいるとき、右上隅の3つの小さな点をクリックし、`Delete file`を選択してください：
![conference](assets/31.webp)
- 同じ作業ブランチにいることを確認し、`Commit changes`ボタンをクリックしてください：
![conference](assets/32.webp)
- コミットにタイトルと説明を追加し、`Commit changes`をクリックしてください：
![conference](assets/33.webp)
- 会議フォルダに戻ります：![conference](assets/34.webp)
- `Add file` ボタンをクリックし、次に `Create new file` をクリックします：
![conference](assets/35.webp)
- ネイティブ言語の指標を使って命名することで、新しいマークダウン (.md) ファイルを作成します。このファイルは、あなたの会議のリプレイ用に使用されます。例えば、私が英語で会議の説明を書きたい場合、このファイルには en.md と名付けます：
![conference](assets/36.webp)
- 会議の設定に合わせて適応できるこのテンプレートを使用して、このマークダウンファイルに記入してください：

```markdown
---
name: Paris Bitcoin Conference 2024
description: フランスで最大のビットコイン会議で、毎年8,000人以上の参加者がいます！
--- 

# メインステージ

## 金曜日の朝

![video](https://youtu.be/XXXXXXXXXXXX)

## 金曜日の午後

![video](https://youtu.be/XXXXXXXXXXXX)

## 土曜日の朝

![video](https://youtu.be/XXXXXXXXXXXX)

## 土曜日の午後

![video](https://youtu.be/XXXXXXXXXXXX)

# ワークショップルーム

## ビットコインマイニングの未来：課題と革新

![video](https://youtu.be/XXXXXXXXXXXX)

講演者: Satoshi Nakamoto, Satoshi Nakamoto

## ビットコイン上でのプライバシーはまだ可能か？

![video](https://youtu.be/XXXXXXXXXXXX)

講演者: Satoshi Nakamoto

## Bitcoin Core：コードベースへの深い潜入

![video](https://youtu.be/XXXXXXXXXXXX)

講演者: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Miniscriptを使ったビットコインウォレットの構築とセキュリティ

![video](https://youtu.be/XXXXXXXXXXXX)

講演者: Satoshi Nakamoto
```

![conference](assets/37.webp)
- 文書の最初に、「front matter」で、`name:` フィールドに会議の名前とリプレイの年を記入します。`description:` フィールドには、ファイルの言語でイベントの短い説明を書きます。例えば、`en.md` という名前のファイルの場合、説明は英語であるべきです。PlanB Network チームがモデルを使用して説明を翻訳します。
- 一級タイトル（`#`によってマークされる）は、メインステージのような会議をシーン別に整理するために使用されます。例えば、ワークショップ専用のステージの場合は `# Workshop Room` です。

- 二級タイトル（二重の `##` でマークされる）は、異なるリプレイビデオを分けるために使用されます。もし会議が半日にわたって連続して撮影された場合は、例えば `## 金曜日の朝` と示します。会議が個別に撮影され、放送された場合は、二級タイトルで直接会議の名前を付けます。

- 各二級タイトルの下に、対応するリプレイビデオへのリンクを挿入します。構文は次のようになります：`![video](https://youtu.be/XXXXXXXXXXXX)`、`XXXXXXXXXXXX`を実際のビデオリンクに置き換えてください。

- 形式が許す場合（個別の会議）、講演者の名前を追加できます。これを行うには、ビデオリンクの下に `Speaker:` フィールドを追加し、講演者の名前または偽名を続けます。複数の講演者がいる場合は、例えばこのように、各名前をコンマで区切ります：`講演者: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`。

---

- このファイルへの変更が完了したら、`Commit changes...` ボタンをクリックして保存します：
![conference](assets/38.webp)
- 変更のタイトルと短い説明を追加します：
![conference](assets/39.webp)
- `Commit changes`をクリックしてください：![conference](assets/40.webp)
- これで、あなたのカンファレンスフォルダはこのようになっているはずです：
![conference](assets/41.webp)
- すべてがご満足いただける場合は、フォークのルートに戻ってください：
![conference](assets/42.webp)
- ブランチに変更が加えられたことを示すメッセージが表示されるはずです。`Compare & pull request`ボタンをクリックしてください：
![conference](assets/43.webp)
- PRに明確なタイトルと説明を追加してください：
![conference](assets/44.webp)
- `Create pull request`ボタンをクリックしてください：
![conference](assets/45.webp)
おめでとうございます！あなたのPRは正常に作成されました。管理者がこれをレビューし、すべてが順調であれば、PlanB Networkのメインリポジトリにマージされます。数日後には、あなたのカンファレンスのリプレイがウェブサイト上に表示されるはずです。

PRの進捗状況を確認し続けてください。管理者が追加情報を求めるコメントを残す可能性があります。PRが承認されるまで、PlanB NetworkのGitHubリポジトリの`Pull requests`タブの下でそれを見ることができます：
![conference](assets/46.webp)

貴重な貢献をいただき、誠にありがとうございます！ :)

---
name: 貢献 - 訂正
description: PlanB Networkでエラーを訂正する方法は？
---
![cover](assets/cover.webp)

PlanBのミッションは、できるだけ多くの言語でBitcoinに関する最先端の教育リソースを提供することです。サイトに公開されているすべてのコンテンツはオープンソースであり、GitHubにホストされているため、誰でもプラットフォームを豊かにするために参加することができます。貢献は、既存のテキストの訂正や校正、他の言語への翻訳、情報の更新、または当サイトにまだない新しいチュートリアルの作成など、さまざまな形を取ります。

私たちの教育コンテンツ（チュートリアル、トレーニング、リソースなど）を参照している際に、スペルミス、文法、母国語でのわずかな翻訳エラー、またはタイポなどのエラーを見つけた場合、自分で素早く訂正を提案していただけると非常に感謝します。

このチュートリアルでは、これらの小さなエラーを訂正するプロセスをステップバイステップで案内します。Gitの複雑さに踏み込みたくない初心者向けのチュートリアルです。しかし、Gitに慣れている場合は、こちらが簡単な要約です：[PlanB Networkデータリポジトリ](https://github.com/PlanB-Network/bitcoin-educational-content)をフォークし、専用のブランチで変更を加え、ソースリポジトリの`dev`ブランチに対してプルリクエストを提出するだけです。

ドキュメントの完全なレビューと改訂、特にコンテンツの翻訳を行う予定の場合は、この他の詳細なチュートリアルをご覧ください。

https://planb.network/tutorials/others/content-review-tutorial

ここでは、小さなエラーに対する素早い訂正の方法にのみ焦点を当てます。

- まず、GitHubアカウントを持っている必要があります。アカウントの作成方法がわからない場合は、詳細なチュートリアルを用意しています。

https://planb.network/tutorials/others/create-github-account


- [PlanB専用のデータGitHubリポジトリ](https://github.com/PlanB-Network/bitcoin-educational-content)にアクセスしてください：
![typos](assets/01.webp)
- ここでは、すべてのコンテンツが部分ごとに整理されています。
- 例えば、チュートリアルを修正したい場合は、`tutorials`フォルダに進んでください：
![typos](assets/02.webp)
- そこでは、私たちのウェブサイトの異なるカテゴリのチュートリアルを見つけることができます。例えば、`Privacy`カテゴリのチュートリアルを修正したい場合は、該当するフォルダをクリックしてください：
![typos](assets/03.webp)
- 次に、訂正したいコンテンツに対応するフォルダを選択してください：
![typos](assets/04.webp)
- 各コンテンツフォルダには、異なる言語で利用可能なデータがあります。例えば、`en.md`ファイルはチュートリアルの英語版に対応し、`fr.md`ファイルはフランス語版を表しています。修正したい言語に対応するファイルを選択してください： ![typos](assets/05.webp)
- そうすると、コンテンツのGitHubページに到着します。修正しようとしているドキュメントにいることを確認してください： ![typos](assets/06.webp)
- 左上の小さな鉛筆アイコンをクリックしてください： ![typos](assets/07.webp)
- 以前にPlanB Networkのコンテンツに貢献したことがない場合は、元のリポジトリのフォークを作成する必要があります。リポジトリをフォークするとは、そのリポジトリのコピーを自分のGitHubアカウントに作成することであり、元のリポジトリに影響を与えることなくプロジェクトに取り組むことができます。`Fork this repository`ボタンをクリックしてください： ![typos](assets/08.webp)
- それでは、GitHubの編集ページに到着します: ![typos](assets/09.webp) - 見つけたエラーを修正するためにテキストを変更してください。恐れることはありません、現在あなたは自分のフォーク上にいるので、今のところPlanB Networkサイトには何も変更されません。例えば、ここでは「entrées」という単語をスペルミスがあったために修正したと想像してみましょう: ![typos](assets/10.webp)
- このドキュメントの修正が完了したら、緑色の `Commit Changes...` ボタンをクリックできます。コミットは、特定の瞬間における作業の瞬間的なスナップショットのようなもので、変更の履歴を保持することを可能にします: ![typos](assets/11.webp)
- 修正のためのタイトルと短い説明を追加してください: ![typos](assets/12.webp)
- 緑色の `Propose changes` ボタンをクリックしてください: ![typos](assets/13.webp)
- そうすると、変更内容をまとめたページに到着します: ![typos](assets/14.webp)
- 下にスクロールすると、行った具体的な修正を見ることができます: ![typos](assets/15.webp)
- すべてが適切で、修正が完了したら、緑色の `Create Pull Request` ボタンをクリックできます: ![typos](assets/16.webp)
- PRページに到着します。Pull Requestは、貢献者がリモートリポジトリのブランチに修正をプッシュしたことを示すリクエストであり、これらの修正がリポジトリのメインブランチにレビューされ、可能であればマージされることを希望しています: ![typos](assets/17.webp)
- PRのためのタイトルと短い説明を追加できます: ![typos](assets/18.webp)
- すべてが良さそうに見える場合は、緑色の `Create Pull Request` ボタンをクリックできます: ![typos](assets/19.webp)
- おめでとうございます、あなたのPRは送信されました！その進行状況は [PlanB Network GitHubリポジトリ](https://github.com/PlanB-Network/bitcoin-educational-content/pulls) の `Pull requests` タブで追跡できます: ![typos](assets/20.webp)
ご協力いただきありがとうございます！PlanB Networkへのコンテンツ作成や翻訳など、他の種類の貢献を行いたい場合は、「Contribution」セクションの他のチュートリアルをチェックしてください。

https://planb.network/tutorials/others



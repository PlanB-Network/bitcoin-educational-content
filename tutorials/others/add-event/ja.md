---
name: PlanB Network にイベントを追加する
description: PlanB Network に新しいイベントを追加することを提案するにはどうすればよいですか?
---
![event](assets/cover.webp)

PlanBのミッションは、できるだけ多くの言語でBitcoinに関する最高級の教育リソースを提供することです。サイトに公開されているすべてのコンテンツはオープンソースであり、GitHubにホストされているため、誰でもプラットフォームの充実に貢献する機会を得ることができます。

PlanB NetworkサイトにBitcoinカンファレンスを追加してイベントの可視性を高めたいけれど、方法がわからない場合、このチュートリアルはあなたのためのものです！
![event](assets/01.webp)
- まず、GitHubにアカウントを持っている必要があります。アカウントの作成方法がわからない場合は、詳細なチュートリアルを用意しています。

https://planb.network/tutorials/others/create-github-account


- `resources/conference/`セクションにある[PlanB専用のデータGitHubリポジトリ](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference)にアクセスしてください：
![event](assets/02.webp)
- 右上の`Add file`ボタンをクリックし、次に`Create new file`をクリックします：
![event](assets/03.webp)
- もしPlanB Networkのコンテンツに以前から貢献したことがない場合、オリジナルのリポジトリのフォークを作成する必要があります。リポジトリをフォークするとは、そのリポジトリのコピーを自分のGitHubアカウント上に作成することで、オリジナルのリポジトリに影響を与えることなくプロジェクトに取り組むことができるようになります。`Fork this repository`ボタンをクリックしてください：
![event](assets/04.webp)
- そうすると、GitHubの編集ページに到着します：
![event](assets/05.webp)
- あなたのカンファレンス用のフォルダを作成します。これを行うには、`Name your file...`ボックスに、スペースの代わりにダッシュを使用して、カンファレンスの名前を小文字で記入します。例えば、カンファレンスが"Paris Bitcoin Conference"と呼ばれている場合、`paris-bitcoin-conference`と記入する必要があります。また、カンファレンスの年も追加してください。例：`paris-bitcoin-conference-2024`：
![event](assets/06.webp)
- フォルダの作成を確定するには、同じボックスで名前の後にスラッシュを記入するだけです。例：`paris-bitcoin-conference-2024/`。スラッシュを追加すると、自動的にフォルダが作成され、ファイルではなくなります：
![event](assets/07.webp)
- このフォルダ内に、`events.yml`という名前の最初のYAMLファイルを作成します：
![event](assets/08.webp)
- このテンプレートを使用して、カンファレンスに関する情報をファイルに記入します：

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website:
    replay_url:    
    live_url :
  tags: 
    - 
```

例えば、あなたのYAMLファイルは以下のようになるかもしれません：

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Paris, France
  address_line_2: 
  address_line_3: 
  name: Paris Bitcoin Conference 2024
  builder: Paris Bitcoin Conference
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description: フランスで最大のBitcoinカンファレンスで、毎年8,000人以上の参加者がいます！
  language:
- fr    - en
    - es
    - it
  リンク:
    website: https://paris.bitcoin.fr/conference
    replay_url:
    live_url :
  タグ: 
    - Bitcoiner
    - General
    - International
```
![イベント](assets/09.webp)
もしまだあなたの組織に「*builder*」という識別子がない場合は、この他のチュートリアルに従って追加することができます。

https://planb.network/tutorials/others/add-builder



- このファイルへの変更が完了したら、`Commit changes...`ボタンをクリックして保存してください：
![イベント](assets/10.webp)
- 変更のタイトルと短い説明を追加してください：
![イベント](assets/11.webp)
- 緑色の`Propose changes`ボタンをクリックしてください：
![イベント](assets/12.webp)
- そうすると、あなたの変更をすべてまとめたページに到着します：
![イベント](assets/13.webp)
- 右上のGitHubプロフィール画像をクリックし、`Your Repositories`を選択してください：
![イベント](assets/14.webp)
- PlanB Networkリポジトリのフォークを選択してください：
![イベント](assets/15.webp)
- 新しいブランチに関する通知がウィンドウの上部に表示されるはずです。おそらく`patch-1`と呼ばれています。それをクリックしてください：
![イベント](assets/16.webp)
- これで、作業ブランチにいます：
![イベント](assets/17.webp)
- `resources/conference/`フォルダに戻り、前のコミットで作成したあなたのカンファレンスのフォルダを選択してください：
![イベント](assets/18.webp)
- あなたのカンファレンスのフォルダ内で、`Add file`ボタンをクリックし、`Create new file`を選択してください：
![イベント](assets/19.webp)
- この新しいフォルダに`assets`と名付け、スラッシュ`/`を末尾に付けてその作成を確認してください：
![イベント](assets/20.webp)
- この`assets`フォルダ内に、`.gitkeep`というファイルを作成してください：
![イベント](assets/21.webp)
- `Commit changes...`ボタンをクリックしてください：
![イベント](assets/22.webp)
- コミットタイトルはデフォルトのままにし、`Commit directly to the patch-1 branch`ボックスがチェックされていることを確認し、`Commit changes`をクリックしてください：
![イベント](assets/23.webp)
- `assets`フォルダに戻ってください：
![イベント](assets/24.webp)
- `Add file`ボタンをクリックし、`Upload files`を選択してください： ![イベント](assets/25.webp)
- 新しいページが開きます。PlanB Networkサイトに表示されるあなたのカンファレンスを代表する画像をドラッグアンドドロップしてください：
![イベント](assets/26.webp)
- それはロゴ、サムネイル、またはポスターでも構いません：
![イベント](assets/27.webp)
- 画像がアップロードされたら、`Commit directly to the patch-1 branch`ボックスがチェックされていることを確認し、`Commit changes`をクリックしてください：
![イベント](assets/28.webp)
- 注意してください、あなたの画像は`thumbnail`と名付けられ、`.webp`フォーマットでなければなりません。したがって、完全なファイル名は`thumbnail.webp`であるべきです：
![イベント](assets/29.webp)
- `assets`フォルダに戻り、中間ファイル`.gitkeep`をクリックしてください：
![イベント](assets/30.webp)
- ファイル上にいるとき、右上の3つの小さな点をクリックし、`Delete file`を選択してください：
- 現在作業中のブランチにまだいることを確認し、`Commit changes`ボタンをクリックしてください：
![event](assets/31.webp)
- コミットにタイトルと説明を追加し、`Commit changes`をクリックしてください：
![event](assets/33.webp)
- リポジトリのルートに戻ってください：
![event](assets/34.webp)
- ブランチに変更があったことを示すメッセージが表示されるはずです。`Compare & pull request`ボタンをクリックしてください：
![event](assets/35.webp)
- PRに明確なタイトルと説明を追加してください：
![event](assets/36.webp)
- `Create pull request`ボタンをクリックしてください：
![event](assets/37.webp)
おめでとうございます！PRは正常に作成されました。管理者がこれを確認し、すべてが順調であれば、PlanB Networkのメインリポジトリにマージされます。数日後には、ウェブサイト上であなたのイベントが表示されるはずです。

PRの進行状況を確認し続けてください。管理者が追加情報を求めるコメントを残すことがあります。PRが承認されるまで、PlanB Network GitHubリポジトリの`Pull requests`タブでそれを確認することができます：
![event](assets/38.webp)
貴重な貢献をいただき、ありがとうございます！ :)


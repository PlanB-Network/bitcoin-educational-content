---
name: Plan ₿ Network教授
description: Plan ₿ Networkに教師プロフィールを追加または変更するにはどうすればよいですか？
---
![cover](assets/cover.webp)

新しいチュートリアルやコースを書いてPlan ₿ Networkに貢献することを計画している場合、教師プロファイルが必要です。このプロフィールは、あなたがプラットフォームに貢献したコンテンツに対して適切なクレジットを受け取ることを可能にします。

すでにPlan ₿ Networkで教育コンテンツの作成に携わっている方は、すでに先生プロフィールをお持ちでしょう。GitHubリポジトリの`/professors`フォルダ(https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors)にあります。もし既にプロフィールが存在する場合は、`professor.yml`ファイルでログインを確認してください。

プロフィールを変更するには、このチュートリアルの最後にある「教師プロフィールを編集する」のセクションに進んでください。

## 私たちのソフトウェアで新しい教師を加える

Plan ₿ Networkに先生プロフィールを作成する最も簡単な方法は、統合されたPythonツールを使用することです。その方法は以下の通りです。

### 1 - ローカル環境を設定する

Forkは[Plan ₿ Network repository on GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content)から入手してください。

Forkのメインブランチ(`dev`)をソースリポジトリと同期させる。

ローカルのクローンを更新する。

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
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

dev` ブランチにいることを確認する。わかりやすい名前で新しいブランチを作成する（例：`add-professor-loic-morel`）。

このブランチをForkオンラインに公開する。

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```

### 3 - 教師プロフィールを作成する

ローカルクローンの `scripts/tutorial-related/data-creator/` フォルダに移動します。まずPython .NET Frameworkをインストールし、ソフトウェアに必要な依存関係をすべてインストールしたことを確認してください：

```bash
pip install -r requirements.txt
```

次に、.NETコマンドでソフトウェアを起動する：

```bash
python3 main.py
```

ホームページにアクセスしたら、リポジトリクローンへのローカルパス、書いている言語、GitHub IDを入力します。誰かのためにこのプロフィールを作成していて、すでにProfessorのプロフィールを持っている場合は、"*PBN Professor's ID*"フィールドにあなたのIDを入力してください。自分自身のプロフィールを作成する場合は、プロフェッサーIDはまだありません。

次に「*新しい教授*」ボタンをクリックします。

![Image](assets/fr/01.webp)

必要な情報を入力してください（これらの情報はGitHubだけでなく、私たちのプラットフォーム上でも公開されることに注意してください）：


- 教師ファイルの名前（姓名または仮名を小文字で）；
- あなたの名前またはニックネーム；
- ログインのランダム生成；
- あなたのウェブサイトとプロフィールX（オプション）；
- 読者からの寄付を受け取るためのライトニングAddress（オプション）；
- リストから2つまたは3つのタグを選択します；
- 画像を選択*」をクリックして、ローカルフォルダからプロファイル画像を選択します（画像には任意の名前と形式を使用でき、ソフトウェアが自動的に適応します）。画像が正方形であることを確認してください）；
- プロフィールの簡単な説明を書いてください。

プロフェッサーを作成する "をクリックして作成を確定します。これで、あなたのプロフィールに必要なすべてのファイルが自動的にgenerateされます。

![Image](assets/fr/02.webp)

変更内容をコミットしてローカルに保存します。変更をForkのGitHubにプッシュしてください。

```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```

作業が完了したら、GitHub に Pull Request (PR) を作成し、修正内容の統合を提案します。PRにはタイトルと簡単な説明を追加してください。

### 4 - 校正とマージ

管理者からの検証やフィードバックを待つ。必要であれば、修正して新しいコミットをプッシュしてください。

```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```

PRがマージされたら、作業ブランチを削除することができます。

## 教師プロフィールの変更

Git の使い方をマスターしているのであれば、新しいブランチを作成して既存のフォルダにある関連ファイルを直接編集することで、教師プロファイルを修正しましょう。変更は、修正する情報に応じて `professor.yml` ファイルかマークダウン・ファイルのどちらかで行います。ローカルで変更を加えたら、ForkにプッシュしてPRを提出してください。

初心者の方には、GitHubのInterfaceウェブから直接修正することをお勧めします。GitHubのアカウントを持っていることを確認してください。作り方がわからない場合は、こちらのチュートリアルを参考にしてください：

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
データ専用のPlan ₿ Network GitHubリポジトリ](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors)にアクセスしてください。

![Image](assets/fr/03.webp)

professors*」フォルダをクリックし、個人フォルダに移動します。

![Image](assets/fr/04.webp)

ライトニングAddress、名前、リンクなどのプロフィールメタデータを変更するには、「*professor.yml*」ファイルを選択してください。説明を変更するには、あなたの言語のYAMLファイル（例："*en.yml*"または "*fr.yml*"）をクリックしてください。

説明を修正した場合は、古い翻訳をすべて削除することを忘れないでください。その後、LLM の助けを借りて説明文を他の言語に翻訳するか、説明文だけをあなたの母国語に残し、Pull Request にあなたの説明文が私たちのチームによる翻訳が必要であることを書いてください。

![Image](assets/fr/05.webp)

修正したいファイルに移動したら、鉛筆のアイコンをクリックします。

![Image](assets/fr/06.webp)

Plan ₿ NetworkリポジトリからまだForkを持っていない場合は、GitHubが作成を勧めてくれます。Fork this repository*」をクリックしてください。

![Image](assets/fr/07.webp)

ファイルに必要な変更を加える。完了したら、「*変更をコミット*」をクリックする。

![Image](assets/fr/08.webp)

変更内容を説明するメッセージを入力し、「*変更を提案する*」を選択します。

![Image](assets/fr/09.webp)

変更内容の要約が表示されます。プロフィールにさらに変更を加えたい場合は、フォルダに戻ってさらにコミットすることができます。完了したら、"*Create pull request*"をクリックしてください。

プルリクエストとは、あなたのブランチからの変更を Plan ₿ Network リポジトリのメインブランチに統合するために行われるリクエストで、マージされる前に変更を確認し、議論することができます。

![Image](assets/fr/10.webp)

Interfaceの先頭で、作業ブランチがPlan ₿ Networkリポジトリの`dev`ブランチ（メインブランチです）にマージされていることを確認してください。

ソースリポジトリにマージしたい変更点を簡潔にまとめたタイトルを入力します。これらの変更を説明する簡単なコメントを追加し、Greenの「*プルリクエストを作成*」ボタンをクリックしてプルリクエストを確定します：

![Image](assets/fr/11.webp)

あなたの PR は Plan ₿ Network リポジトリの "*Pull Request*" タブに表示されます。あとは管理者があなたの修正をマージしてくれるのを待つだけです。

![Image](assets/fr/12.webp)

変更を提出する際に技術的な問題が発生した場合は、遠慮なく[コントリビューション専用のTelegramグループ](https://t.me/PlanBNetwork_ContentBuilder)に助けを求めてください。ありがとうございました！
---
name: Plan ₿ Networkプラットフォームローカル運用ガイド
description: Plan ₿ Networkでのコンテンツ投稿や教育コンテンツの校正・校閲をテストしたいのですが、ローカル環境でPlan ₿ Networkを動かすにはどうすればよいですか？
---
![github](assets/cover.webp)

## まとめ

このチュートリアルでは、Docker、ダミーキー、およびカスタムリポジトリ設定を使用して、ローカルマシン上でPlan ₿ NetworkからBitcoin学習管理システムをセットアップするためのステップバイステップの手順を提供します。

もし上の部分が理解できなかったとしても、心配しないでほしい！

---
## **Bitcoin学習管理システムをローカルで運用するには**？

このチュートリアルでは、プラットフォームのセットアップ、ダミーキーの取り扱い、リポジトリのカスタマイズについて、詳細な手順を説明します。以下の手順に従って、よくある問題を回避し、ローカル環境を適切に設定してください。

**1.前提条件


- DockerとDocker ComposeがインストールされたLinuxマシン（Windowsでも動作報告あり）。
- 十分な `nodejs` バージョン (テスト済み: 22.12.0)
- pnpm`をシステムにインストールする。
- リポジトリのクローン用に設定されたGit。

**2.リポジトリをクローンする**。

リポジトリをローカルマシンにクローンします：

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system࿼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system࿼cd) Bitcoin-学習管理システム

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3.環境変数の設定

1\..env.example`ファイルを複製する：

```bash
cp .env.example .env
```

1..env`ファイルを編集し、名前の.exampleの部分を削除する。例

⚠️ これは必須のステップであり、これをスキップすると、いくつかのコンテナ間で接続が拒否されるなどのエラーが発生する。

Github専用のPATもファイルに追加することをお忘れなく。

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4.依存関係のインストール

nodejsの適切なバージョンをインストールしてください。2024-12現在、v22.12.0 (LTS)が動作確認されています。

⚠️ Ubuntu 22.04 リポジトリの nodejs のバージョンは 12.22.9 です。

nodejsをインストールするには、[こちら](https://nodejs.org/en/download/package-manager)を参照してください。例えば、`nvm`というインストール方法を使うこともできます。

---
必要なパッケージのpnpmインストール・フェーズを開始する前に、すべての依存パッケージがインストールされていることを確認してください：

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
.../Bitcoin-learning-management-system/`フォルダの中で、以下のコマンドを実行して `pnpm` をインストールする。

```bash
pnpm install
```

__TIP:__ 依存関係とpnpm自体の両方を時々更新することを忘れないでください。

**5.コンテナを実行する**。

.../Bitcoin-learning-management-system/`フォルダ内で、Dockerで開発環境を起動します：

```bash
docker compose up --build -V
```

次のコマンドもこの方法で実行すると、ターミナルにログが表示されなくなる。

```bash
docker compose up -d --build -V
```

これは、ドッカーズから必要なコンテナをすべてビルドして起動する。

**6.アプリケーションにアクセスする

コンテナが起動したら、フロントエンドにアクセスする：

\[<http://localhost:8181](http://localhost:8181)>。

![Plan ₿ Network Local](assets/en/1.webp)

注意：ソースファイルを変更すると、アプリは自動的にリロードされます。

**データベースのセットアップ Schema

最初の実行では、DBマイグレーションを実行する必要がある。

そのためには、マイグレーションスクリプトを実行する。

```markdown
pnpm run dev:db:migrate
```

**8.リポジトリからデータをインポート

データベースにデータをインポートするには、APIにリクエストする：

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9.同期ボリュームのアクセスに関する問題を修正しました。

もし `cdn` ボリュームと `sync` ボリュームへのアクセスに問題が発生した場合は、以下を実行してください：

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

そしてまた：

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10.リポジトリをカスタマイズする（オプション）***。

Forkや特定のブランチを使う必要がある場合：

1..env`ファイルを編集して、以下の変数を更新する：

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\.Dockerを再起動する：

```markdown
docker compose down -v
docker compose up --build -V
```

3\.リポジトリデータを再同期する：

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

このチュートリアルでは、ダミーキー、依存関係のインストール、必要に応じてカスタマイズされたリポジトリなど、プラットフォームが正しくセットアップされていることを確認します。セットアップを頑張ってください！

**追加ヘルプ**のためのコマンド

すべてのコンテナを停止する

```
docker compose down
```

既存のコンテナとボリュームをすべて削除する

```
docker container prune -f
docker volume prune --all
```

公式ガイドとランチ・シンク・スクリプトで使用したものと同じコマンドでコンテナを再作成する：

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```

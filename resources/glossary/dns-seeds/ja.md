---
用語DNS SEEDS

---
ネットワークに参加する新しいビットコインノードのための初期接続ポイント。これらのシードは、実際には特定のDNSサーバーであり、そのアドレスはビットコインコアのコードに恒久的に埋め込まれている。新しいノードが起動すると、これらのサーバーに連絡し、おそらくアクティブなビットコインノードのIPアドレスのランダムなリストを取得します。その後、新しいノードはこのリストにあるノードと接続を確立し、初期ブロックダウンロード（IBD）を実行し、最も多くの作業を蓄積しているチェーンと同期するために必要な情報を得ることができます。2024年現在、ビットコインコアのDNSシードのリストと、そのメンテナンスに責任を持つ個人は以下の通りである（https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp）：


- seed.bitcoin.sipa.be：Pieter Wuille；
- dnsseed.bluematt.me：マット・コラロ
- dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us：Luke Dashjr；
- seed.bitcoinstats.com：クリスチャン・デッカー
- seed.bitcoin.jonasschnelli.ch：ジョナス・シュネリ
- seed.btc.petertodd.net：ピーター・トッド
- seed.bitcoin.sprovoost.nl：Sjors Provoost；
- dnsseed.emzy.de：ステファン・オエステ
- seed.bitcoin.wiz.biz：ジェイソン・モーリス
- seed.mainnet.achownodes.xyz：アバ・チャウ

DNSシードは、ビットコインノードが接続を確立するための、優先順位の高い2番目の方法です。最初の方法は、ノード自身が作成した peers.dat ファイルを使用することです。このファイルは、ユーザーが手動で変更しない限り、新しいノードの場合は当然空です。

> 注意：DNSシードは「シードノード」と混同してはならない。
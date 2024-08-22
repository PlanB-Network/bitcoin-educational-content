---
term: DNS SEEDS
---

新しいBitcoinノードがネットワークに参加するための初期接続ポイントです。これらのシードは、実際には特定のDNSサーバーであり、そのアドレスはBitcoin Coreのコードに永久に埋め込まれています。新しいノードが起動すると、これらのサーバーに接触して、おそらくアクティブなBitcoinノードのランダムなIPアドレスリストを取得します。新しいノードは、このリスト上のノードと接続を確立して、初期ブロックダウンロード（IBD）を実行し、最も累積作業があるチェーンと同期するために必要な情報を取得できます。2024年現在、以下はBitcoin Core DNSシードとそのメンテナンスを担当する個人のリストです(https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
* seed.bitcoin.sipa.be: Pieter Wuille;
* dnsseed.bluematt.me: Matt Corallo;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
* seed.bitcoinstats.com: Christian Decker;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

DNSシードは、Bitcoinノードが接続を確立するための優先順位で二番目の方法です。最初の方法は、ノード自体が作成したpeers.datファイルを使用することです。このファイルは、新しいノードの場合は自然に空ですが、ユーザーが手動で変更していない限りです。

> ► *注記、DNSシードは「シードノード」と混同してはいけません。これは接続を確立するための三番目の方法です。*
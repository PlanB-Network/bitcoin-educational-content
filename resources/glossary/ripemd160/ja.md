---
term: RIPEMD160
---

*Research and development in Advanced Communications technologies in Europe Integrity Primitives Evaluation Message Digest 160*の略称です。任意の入力から160ビットのダイジェストを生成する暗号化ハッシュ関数です。Bitcoinでは、公開鍵をレガシーおよびSegWit v0標準（SegWit v1の場合、公開鍵はハッシュ化されません）の受信アドレスに変換するために使用されます。このプロセスは、まず公開鍵に`SHA256`ハッシュ関数を適用し、その結果に`RIPEMD160`を適用することを含みます。この2つの異なるハッシュ関数の組み合わせは、Bitcoinの文脈では`HASH160`として知られています。`RIPEMD160`は、キーフィンガープリントを計算するために決定論的および階層的ウォレットでも使用されます。具体的には、`HASH160`は親キーのフィンガープリントを計算するために使用され、その後、拡張キー（xpub、xprv...）のメタデータに含まれます。
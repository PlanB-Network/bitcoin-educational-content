---
term: WITNESSSCRIPT
---
P2WSH または P2SH-P2WSH UTXO からビットコインを使用できる条件を指定するスクリプト。通常、`witnessScript` は SegWit 標準のマルチシグネチャウォレットの条件を決定する。これらのスクリプト標準では、UTXOの`scriptPubKey`（出力）には`witnessScript`のハッシュが含まれています。この UTXO を新しいトランザクションの入力として使用するには、所持者は `scriptPubKey` 内のフィンガープリントとの一致を証明するために、オリジナルの `witnessScript` を公開しなければならない。それから `witnessScript` をトランザクションの `scriptWitness` に含めなければならない。 `scriptWitness` には署名などのスクリプトを検証するのに必要な要素も含まれる。したがって、`witnessScript` は SegWit では P2SH トランザクションの `redeemScript` と等価であるが、`scriptSig` の中ではなくトランザクションの証人の中に置かれるという違いがある。

> 注意: `witnessScript` は `scriptWitness` と混同しないでください。witnessScript`はP2WSHまたはP2SH-P2WSH UTXOの支出条件を定義し、それ自体がスクリプトを構成するのに対し、`scriptWitness`はあらゆるSegWit入力の目撃データを含む*。
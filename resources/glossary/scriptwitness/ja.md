---
用語SCRIPTWITNESS

---
SegWitトランザクションエントリーの要素で、トランザクションで送信されたビットコインのロックを解除するために必要な署名と公開鍵を含む。レガシー取引の `scriptSig` と同様に、`scriptWitness` は同じ場所には置かれない。実際、"証人"（英語では`*witness*`）と呼ばれるこの部分は、トランザクションの不正操作の問題を解決するために別のデータベースに移される。それぞれのSegWit入力はそれ自身の `scriptWitness` を持ち、すべての `scriptWitness` 要素は一緒になってトランザクションの `Witness` フィールドを形成する。

> scriptWitness` と `witnessScript` を混同しないように注意してください。scriptWitness`にはSegWit入力の目撃データが含まれていますが、`witnessScript`はP2WSHまたはP2SH-P2WSH UTXOの支出条件を定義し、P2SH出力の`redeemScript`と同様に、それ自体がスクリプトを構成します。
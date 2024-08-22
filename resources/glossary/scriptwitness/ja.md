---
term: SCRIPTWITNESS
---

SegWitトランザクションエントリに含まれる要素で、トランザクションで送られたビットコインを解除するために必要な署名と公開鍵を含んでいます。従来のトランザクションの`scriptSig`に似ていますが、`scriptWitness`は同じ場所に配置されません。実際には、この部分は「証人」（英語で`*witness*`）と呼ばれ、トランザクションの可変性問題を解決するために別のデータベースに移動されます。各SegWit入力には独自の`scriptWitness`があり、すべての`scriptWitness`要素が合わせてトランザクションの`Witness`フィールドを形成します。

> ► `scriptWitness`と`witnessScript`を混同しないように注意してください。`scriptWitness`は任意のSegWit入力の証人データを含んでいますが、`witnessScript`はP2WSHまたはP2SH-P2WSH UTXOの支払い条件を定義し、P2SH出力の`redeemScript`に似た独自のスクリプトを構成します。
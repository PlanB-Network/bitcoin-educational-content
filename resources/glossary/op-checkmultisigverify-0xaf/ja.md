---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

`OP_CHECKMULTISIG`と`OP_VERIFY`を組み合わせたものです。複数の署名と公開鍵を取り、`M`個の署名が`N`個の中で有効であることを`OP_CHECKMULTISIG`と同様に検証します。その後、`OP_VERIFY`のように、検証が失敗した場合は、スクリプトはエラーで直ちに停止します。検証が成功した場合は、スタックに何もプッシュせずにスクリプトが続行します。このオペコードはTapscriptで削除されました。
---
term: OP_CHECKSIGVERIFY (0XAD)

definition: OP_CHECKSIGとOP_VERIFYを組み合わせたもので、署名が無効な場合にスクリプトを停止する。
---
OP_CHECKSIG` と同じ処理を行うが、署名の検証に失敗した場合、スクリプトは即座にエラーで停止し、トランザクションは無効となる。検証が成功した場合、スクリプトは `1` (true)をスタックにプッシュすることなく続行する。まとめると、`OP_CHECKSIGVERIFY` は `OP_CHECKSIG` の後に `OP_VERIFY` を実行する。このオペコードはシュナー署名を検証するために Tapscript で変更された。
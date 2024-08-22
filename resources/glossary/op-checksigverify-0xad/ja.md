---
term: OP_CHECKSIGVERIFY (0XAD)
---

`OP_CHECKSIGVERIFY`は`OP_CHECKSIG`と同じ操作を行いますが、署名の検証に失敗すると、スクリプトは直ちにエラーで停止し、その結果トランザクションは無効になります。検証に成功した場合、スクリプトはスタックに`1`（真）の値をプッシュすることなく続行します。要約すると、`OP_CHECKSIGVERIFY`は`OP_CHECKSIG`の操作に続いて`OP_VERIFY`を実行します。このオペコードはTapscriptでSchnorr署名を検証するために変更されました。
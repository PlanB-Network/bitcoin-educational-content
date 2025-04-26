---
term: op_checkmultisigverify (0xaf)

---
OP_CHECKMULTISIG` と `OP_VERIFY` を組み合わせたものである。OP_CHECKMULTISIG` と同じように、複数の署名と公開鍵を用いて `N` 個の署名のうち `M` 個が有効かどうかを検証する。そして `OP_VERIFY` と同様に、検証に失敗するとスクリプトは直ちにエラーで停止する。検証が成功した場合、スクリプトはスタックに値をプッシュすることなく続行します。このオペコードは Tapscript で削除された。
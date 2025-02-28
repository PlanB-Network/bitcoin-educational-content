---
term: sighash_all/sighash_acp

---
ビットコインのトランザクション署名で使用される `SIGHASH_ANYONECANPAY` 修飾子 (`SIGHASH_ACP`) と組み合わせた SigHash フラグ (`0x81`) のタイプ。この組み合わせは、署名がトランザクションのすべての出力と特定の入力にのみ適用されることを指定する。SIGHASH_ALL | SIGHASH_ANYONECANPAY` は、他の参加者が最初の署名の後にトランザクションに追加の入力を追加することを可能にする。これは、クラウドファンディングのような協調的なシナリオにおいて特に有用である。
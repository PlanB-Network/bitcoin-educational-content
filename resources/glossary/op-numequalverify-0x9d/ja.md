---
term: op_numequalverify (0x9d)

---
OP_NUMEQUAL` と `OP_VERIFY` の操作を組み合わせる。スタックの一番上の 2 つの要素を数値で比較します。値が等しい場合、 `OP_NUMEQUALVERIFY` はスタックから真の結果を取り除き、スクリプトの実行を続行します。値が等しくない場合、結果は偽となり、スクリプトは直ちに失敗する。
---
term: OP_NUMEQUALVERIFY (0X9D)

definition: OP_NUMEQUALとOP_VERIFYを組み合わせたもので、数値が異なる場合に失敗します。
---
OP_NUMEQUAL` と `OP_VERIFY` の操作を組み合わせる。スタックの一番上の 2 つの要素を数値で比較します。値が等しい場合、 `OP_NUMEQUALVERIFY` はスタックから真の結果を取り除き、スクリプトの実行を続行します。値が等しくない場合、結果は偽となり、スクリプトは直ちに失敗する。
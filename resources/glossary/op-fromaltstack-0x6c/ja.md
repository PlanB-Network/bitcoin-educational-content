---
term: OP_FROMALTSTACK (0X6C)

definition: 代替スタックからメインスタックに要素を移動するOpcode。
---
代替スタック (*alt stack*) から先頭の項目を取り除き、メインスタック (*main stack*) の先頭に置く。このオペコードは、代替スタックに一時的に格納されたデータを取り出すために使用される。簡単に言うと、`OP_TOALTSTACK` の逆の操作です。
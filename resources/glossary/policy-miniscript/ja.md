---
term: POLICY (MINISCRIPT)
---

高レベルでユーザー指向の言語であり、Miniscriptのフレームワーク内でUTXOがアンロックされる条件を簡単に指定できます。ポリシーは支出ルールの抽象的な記述です。それから、ビットコインのネイティブスクリプト言語からの操作と一対一に相当するminiscriptにコンパイルすることができます。

![](../../dictionnaire/assets/30.png)

ポリシー言語はminiscript言語とは少し異なります。例えば、主要なパスがキーAで、リカバリーパスがキーBであるセキュリティシステムを想像してみてくださいが、1年のタイムロック（約52,560ブロック）の下にあります。ポリシーでは、これは以下のようになります：

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

miniscriptにコンパイルされると、以下のようになります：

```plaintext
andor(pk(B),older(52560),pk(A))
```

そして、ネイティブスクリプトに変換されると、以下のようになります：

```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```
---
term: (MINISKRIPT)

---
Vysokoúrovňový, uživatelsky orientovaný jazyk, který umožňuje jednoduchou specifikaci podmínek, za kterých lze UTXO odemknout v rámci Miniscriptu. Politika je abstraktní popis pravidel pro vynakládání prostředků. Poté ji lze zkompilovat do miniskriptu, který je ekvivalentem jedna ku jedné s operacemi z nativního skriptovacího jazyka Bitcoinu.

![](../../dictionnaire/assets/30.webp)

Jazyk zásad se mírně liší od jazyka miniskriptů. Představte si například bezpečnostní systém, jehož primární cesta je klíč A a cesta obnovy je klíč B, ale s časovým zámkem na jeden rok (přibližně 52 560 bloků). V zásadách by to bylo následující:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Po zkompilování do miniskriptu by to bylo:

```plaintext
andor(pk(B),older(52560),pk(A))
```

A po převedení do nativního písma by to bylo:

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